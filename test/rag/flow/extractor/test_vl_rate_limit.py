#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Tests for rag/flow/extractor/vl_rate_limit.py — 进程级 VL 请求全局限流
#
#  背景（2026-08-15 22:28 YXLA 重解析洪峰）：
#    - QwenVLParser 页级并发 6 × 每页 2 次调用，Extractor chunk 级并发 6，
#      两层并发叠加瞬时 16+ 请求打 vLLM(8090)，generation throughput 从
#      200~300 跌至 0.1~24 tok/s，4 个 coord 请求 120s 超时
#    - 本组测试验证进程级信号量：
#      - 默认上限 8，可被 VL_GLOBAL_CONCURRENCY 覆盖
#      - 并发峰值不超上限
#      - 异常路径释放信号量
#      - 排队等待 > 0.5s 输出等待日志
#
import importlib.util
import os
import sys
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


def test_default_limit_is_8():
    mod = _load_module()
    assert mod.VL_GLOBAL_CONCURRENCY == 8


def test_env_override(monkeypatch):
    monkeypatch.setenv("VL_GLOBAL_CONCURRENCY", "4")
    mod = _load_module()
    assert mod.VL_GLOBAL_CONCURRENCY == 4


def test_invalid_env_falls_back_to_default(monkeypatch):
    monkeypatch.setenv("VL_GLOBAL_CONCURRENCY", "not-a-number")
    mod = _load_module()
    assert mod.VL_GLOBAL_CONCURRENCY == 8


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
