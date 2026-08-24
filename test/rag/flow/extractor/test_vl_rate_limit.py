#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Tests for rag/flow/extractor/vl_rate_limit.py — 进程级 VL 请求全局限流
#
#  背景（2026-08-15 22:28 YXLA 重解析洪峰）：
#    - QwenVLParser 页级并发 × 每页 2 次调用，Extractor chunk 级并发，
#      两层并发叠加瞬时 16+ 请求打 vLLM(8090)，generation throughput 从
#      200~300 跌至 0.1~24 tok/s，4 个 coord 请求 120s 超时
#    - 本组测试验证进程级信号量：
#      - 默认上限 26（无环境变量，由 DSL setups.pdf.vl_global_concurrency 驱动）
#      - 并发峰值不超上限
#      - 异常路径释放信号量
#      - 排队等待 > 0.5s 输出等待日志
#      - set_vl_limit 动态调闸：上调即时、下调延迟收缩、非法值忽略
#      - resolve_vl_limit / derived_sub_concurrency 取值规则
#
import importlib.util
import os
import threading
import time

import pytest

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "vl_rate_limit",
        os.path.join(project_root, "rag", "flow", "extractor", "vl_rate_limit.py"),
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_default_limit_is_26():
    mod = _load_module()
    assert mod.VL_GLOBAL_CONCURRENCY == 26


def test_no_env_override(monkeypatch):
    """环境变量已废弃：即使设置了 env，默认值仍是 26。"""
    monkeypatch.setenv("VL_GLOBAL_CONCURRENCY", "4")
    mod = _load_module()
    assert mod.VL_GLOBAL_CONCURRENCY == 26


def test_concurrency_capped_at_limit():
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 2
    mod._rebuild_semaphore()

    active = 0
    peak = 0
    lock = threading.Lock()
    errors = []

    def task():
        nonlocal active, peak
        try:
            mod.acquire_vl_slot()
            with lock:
                active += 1
                peak = max(peak, active)
            time.sleep(0.02)
            with lock:
                active -= 1
        except Exception as e:  # pragma: no cover
            errors.append(e)
        finally:
            mod.release_vl_slot()

    threads = [threading.Thread(target=task) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert not errors
    assert peak <= 2, f"并发峰值 {peak} 超过上限 2"


def test_slot_released_on_exception():
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 1
    mod._rebuild_semaphore()

    def failing():
        mod.acquire_vl_slot()
        try:
            raise RuntimeError("boom")
        finally:
            mod.release_vl_slot()

    with pytest.raises(RuntimeError):
        failing()

    # 信号量已释放：下一次 acquire 不应阻塞超过短暂时间
    done = threading.Event()

    def reacquire():
        mod.acquire_vl_slot()
        mod.release_vl_slot()
        done.set()

    t = threading.Thread(target=reacquire)
    t.start()
    t.join(timeout=2)
    assert done.is_set(), "异常后信号量未释放，后续请求被永久阻塞"


def test_wait_logged_when_exceeding_half_second(caplog):
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 1
    mod._rebuild_semaphore()

    mod.acquire_vl_slot()
    hold_started = threading.Event()
    wait_done = threading.Event()

    def holder():
        hold_started.set()
        time.sleep(0.7)
        mod.release_vl_slot()

    h = threading.Thread(target=holder)
    h.start()
    hold_started.wait()

    with caplog.at_level("INFO"):
        t0 = time.time()
        mod.acquire_vl_slot()
        elapsed = time.time() - t0
    mod.release_vl_slot()
    h.join()

    assert elapsed >= 0.5
    assert any("vl-rate-limit" in rec.getMessage() for rec in caplog.records), (
        "排队超过 0.5s 应输出等待日志"
    )


# ────────────────────────────────────────────────────────────────────
# set_vl_limit 动态调闸
# ────────────────────────────────────────────────────────────────────


def _peak_concurrency(mod, n_tasks, hold=0.03):
    """并发跑 n_tasks 个 acquire/release，返回在飞峰值。"""
    active = 0
    peak = 0
    lock = threading.Lock()

    def task():
        nonlocal active, peak
        mod.acquire_vl_slot()
        try:
            with lock:
                active += 1
                peak = max(peak, active)
            time.sleep(hold)
            with lock:
                active -= 1
        finally:
            mod.release_vl_slot()

    threads = [threading.Thread(target=task) for _ in range(n_tasks)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return peak


def test_set_vl_limit_raise_takes_effect_immediately():
    """上调闸值：立即放行更多并发。"""
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 2
    mod._rebuild_semaphore()
    assert _peak_concurrency(mod, 6) <= 2

    mod.set_vl_limit(5)
    assert mod.VL_GLOBAL_CONCURRENCY == 5
    assert _peak_concurrency(mod, 6) >= 4


def test_set_vl_limit_shrink_idle_immediate():
    """下调闸值（无在飞请求）：空闲 permit 立即收回。"""
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 6
    mod._rebuild_semaphore()

    mod.set_vl_limit(2)
    assert mod.VL_GLOBAL_CONCURRENCY == 2
    assert _peak_concurrency(mod, 6) <= 2


def test_set_vl_limit_shrink_deferred_with_inflight():
    """下调闸值（有在飞请求）：不阻塞在飞请求，随 release 逐个收缩。"""
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 2
    mod._rebuild_semaphore()

    mod.acquire_vl_slot()  # 在飞 1，剩余 permit 1
    mod.set_vl_limit(1)
    mod.release_vl_slot()  # 该 permit 应被回收而非归还

    assert mod.VL_GLOBAL_CONCURRENCY == 1
    assert _peak_concurrency(mod, 4) <= 1


def test_set_vl_limit_same_value_noop():
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 3
    mod._rebuild_semaphore()
    mod.set_vl_limit(3)
    assert _peak_concurrency(mod, 5) == 3


def test_set_vl_limit_invalid_ignored(caplog):
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 26
    mod._rebuild_semaphore()
    with caplog.at_level("WARNING"):
        mod.set_vl_limit("abc")
        mod.set_vl_limit(-1)
        mod.set_vl_limit(0)
        mod.set_vl_limit(None)
    assert mod.VL_GLOBAL_CONCURRENCY == 26, "非法闸值不得生效"


def test_resolve_vl_limit_rules():
    mod = _load_module()
    assert mod.resolve_vl_limit(40) == 40
    assert mod.resolve_vl_limit("40") == 40
    assert mod.resolve_vl_limit(None) == 26
    assert mod.resolve_vl_limit("abc") == 26
    assert mod.resolve_vl_limit(-3) == 26
    assert mod.resolve_vl_limit(0) == 26
    assert mod.resolve_vl_limit(2.7) == 26  # 非整数不采纳


def test_derived_sub_concurrency_is_half():
    """页级/chunk 级子并发 = 闸值的一半（向下取整，最小 1）。"""
    mod = _load_module()
    assert mod.derived_sub_concurrency(26) == 13
    assert mod.derived_sub_concurrency(18) == 9
    assert mod.derived_sub_concurrency(1) == 1
    assert mod.derived_sub_concurrency(3) == 1


# ────────────────────────────────────────────────────────────────────
# acquire_vl_slot 超时（2026-08-22 事故 §4.3：无超时等待可永久阻塞线程）
# ────────────────────────────────────────────────────────────────────


def test_acquire_timeout_default_is_60_minutes():
    """默认等待上限与 60 分钟任务看门狗对齐。"""
    mod = _load_module()
    assert mod.VL_SLOT_ACQUIRE_TIMEOUT == 60 * 60


def test_acquire_times_out_when_slots_exhausted():
    """槽位耗尽且等待超限时必须抛 TimeoutError，而不是永久阻塞。

    用保护线程执行：若 acquire 无超时实现会永久阻塞，线程 join 超时后
    测试失败（而不是把整个测试套件挂死）。
    """
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 1
    mod._rebuild_semaphore()

    mod.acquire_vl_slot()  # 唯一槽位被占住
    result = {}

    def waiter():
        mod.VL_SLOT_ACQUIRE_TIMEOUT = 0.2
        t0 = time.time()
        try:
            mod.acquire_vl_slot()
        except TimeoutError:
            result["timed_out"] = True
            result["elapsed"] = time.time() - t0
            return
        result["acquired"] = True
        mod.release_vl_slot()

    t = threading.Thread(target=waiter, daemon=True)
    t.start()
    t.join(timeout=3)

    mod.release_vl_slot()  # 清理：归还自己占的槽位
    assert not t.is_alive(), "acquire 在槽位耗尽时永久阻塞——缺少超时保护（事故 §4.3）"
    assert result.get("timed_out"), f"槽位耗尽且超过等待上限时必须抛 TimeoutError，实际: {result}"
    assert result["elapsed"] < 2, "超时后应立即失败，而非继续阻塞"


def test_acquire_timeout_does_not_leak_permit():
    """超时失败后不得占用 permit：释放一个槽位后立即可以正常获取。"""
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 1
    mod._rebuild_semaphore()

    mod.acquire_vl_slot()
    mod.VL_SLOT_ACQUIRE_TIMEOUT = 0.2

    def waiter():
        try:
            mod.acquire_vl_slot()
            mod.release_vl_slot()  # 若意外拿到，立刻归还保持守恒
        except TimeoutError:
            pass

    t = threading.Thread(target=waiter, daemon=True)
    t.start()
    t.join(timeout=3)
    assert not t.is_alive(), "超时等待路径阻塞，无法验证 permit 守恒"

    mod.release_vl_slot()

    # 若超时路径误占了 permit，这里会拿不到槽位
    mod.VL_SLOT_ACQUIRE_TIMEOUT = 1
    got = threading.Event()

    def reacquire():
        try:
            mod.acquire_vl_slot()
            got.set()
            mod.release_vl_slot()
        except TimeoutError:
            pass

    t2 = threading.Thread(target=reacquire, daemon=True)
    t2.start()
    t2.join(timeout=3)
    assert got.is_set(), "超时失败的 acquire 误占了 permit，导致后续请求饥饿"


def test_acquire_succeeds_within_timeout():
    """在超时窗口内拿到槽位时正常返回（不误杀）。"""
    mod = _load_module()
    mod.VL_GLOBAL_CONCURRENCY = 1
    mod._rebuild_semaphore()

    mod.acquire_vl_slot()
    released = threading.Event()

    def holder():
        time.sleep(0.3)
        mod.release_vl_slot()
        released.set()

    h = threading.Thread(target=holder)
    h.start()

    mod.VL_SLOT_ACQUIRE_TIMEOUT = 2
    mod.acquire_vl_slot()  # 应等到 0.3s 后的释放，不抛异常
    mod.release_vl_slot()
    h.join()
    assert released.is_set()
