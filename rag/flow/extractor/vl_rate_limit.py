# vl_rate_limit.py — 进程级 VL 模型（vLLM 8090）请求全局限流
#
# 背景（2026-08-15 22:28 全量重解析洪峰）：
#   QwenVLParser 页级并发 6（每页 classify + text/table 两次调用）与
#   Extractor chunk 级并发 6 两层叠加，瞬时 16+ 大图请求打 vLLM，
#   GPU prefill 风暴导致 generation throughput 从 200~300 跌至 0.1~24 tok/s，
#   4 个 coord 请求 120s 超时（335 个占位 bbox）。
#
# 本模块提供进程内共享信号量：所有打 VL 卡的 HTTP 调用（qwen_vl_parser.py
# _call_vlm / qwen_vl_ocr.py _call_qwen30b_coord / qwen30b_ocr.py 三个
# _call_qwen30b_*）在发出请求前 acquire，使单进程在飞 VL 请求数不超过
# VL_GLOBAL_CONCURRENCY（默认 26）。
#
# 配置来源（环境变量已废弃）：闸值由 DSL setups.pdf.vl_global_concurrency
# 驱动——Parser 组件启动解析时调用 set_vl_limit() 动态调闸；页级并发
# （QwenVLParser.PAGE_CONCURRENCY）与 chunk 级并发（Extractor.CHUNK_CONCURRENCY）
# 均派生为闸值的一半（向下取整，最小 1），不再各自读环境变量。
#
# 注意：RAGFlow 有 4 个 task_executor 进程，进程间无法共享该信号量；
# 跨进程兜底依赖 vLLM 侧 --max-num-seqs 配置。

import logging
import threading
import time

_DEFAULT_CONCURRENCY = 8

# Incident 2026-08-22 §4.3: acquire() without timeout can block a consumer
# thread forever when the engine stalls (vLLM crash / zombie holders),
# cascading into a fully occupied executor. Fail fast instead — the bound
# matches the 60-minute task watchdog so a healthy request queued behind
# normal work is never killed early.
VL_SLOT_ACQUIRE_TIMEOUT = 60 * 60

# 线程安全记账：_INFLIGHT = 已 acquire 未 release 的请求数；
# _RECLAIM_ON_RELEASE = 下调闸值时延迟回收的 permit 数（随 release 逐个吞掉，
# 不阻塞在飞请求）。
_LOCK = threading.Lock()
_INFLIGHT = 0
_RECLAIM_ON_RELEASE = 0

VL_GLOBAL_CONCURRENCY = _DEFAULT_CONCURRENCY
_VL_SEMAPHORE = threading.Semaphore(VL_GLOBAL_CONCURRENCY)


def resolve_vl_limit(raw) -> int:
    """解析 DSL 传入的闸值：正整数（含整数字符串）采纳，其余回退默认值。

    float（如 2.7）、负数、0、None、非法字符串一律不采纳。
    """
    if isinstance(raw, bool):
        return _DEFAULT_CONCURRENCY
    if isinstance(raw, int):
        return raw if raw > 0 else _DEFAULT_CONCURRENCY
    if isinstance(raw, str):
        try:
            value = int(raw)
        except ValueError:
            return _DEFAULT_CONCURRENCY
        return value if value > 0 else _DEFAULT_CONCURRENCY
    return _DEFAULT_CONCURRENCY


def derived_sub_concurrency(limit: int) -> int:
    """页级/chunk 级子并发 = 全局闸值的一半（向下取整，最小 1）。"""
    return max(1, limit // 2)


def set_vl_limit(new_limit) -> None:
    """动态调整全局闸值（由 Parser 组件按 DSL 配置调用）。

    - 非法值（非正整数）：告警并忽略；
    - 同值：noop；
    - 上调：立即补足 permit；
    - 下调：空闲 permit 立即收回，被在飞请求占住的随 release 逐个回收，
      不阻塞也不打断在飞请求。
    """
    global VL_GLOBAL_CONCURRENCY, _INFLIGHT, _RECLAIM_ON_RELEASE
    if isinstance(new_limit, bool) or not isinstance(new_limit, int) or new_limit <= 0:
        logging.warning(
            f"[vl-rate-limit] invalid set_vl_limit({new_limit!r}), "
            f"keeping {VL_GLOBAL_CONCURRENCY}"
        )
        return
    with _LOCK:
        old = VL_GLOBAL_CONCURRENCY
        if new_limit == old:
            return
        VL_GLOBAL_CONCURRENCY = new_limit
        if new_limit > old:
            for _ in range(new_limit - old):
                _VL_SEMAPHORE.release()
            logging.info(f"[vl-rate-limit] limit raised {old} -> {new_limit}")
        else:
            deficit = old - new_limit
            free = max(old - _INFLIGHT, 0)
            immediate = min(deficit, free)
            for _ in range(immediate):
                _VL_SEMAPHORE.acquire(timeout=0)
            _RECLAIM_ON_RELEASE += deficit - immediate
            logging.info(
                f"[vl-rate-limit] limit lowered {old} -> {new_limit} "
                f"(reclaimed {immediate} idle, {_RECLAIM_ON_RELEASE} deferred)"
            )


def _rebuild_semaphore() -> None:
    """按当前 VL_GLOBAL_CONCURRENCY 重建信号量（测试专用）。"""
    global _VL_SEMAPHORE
    _VL_SEMAPHORE = threading.Semaphore(VL_GLOBAL_CONCURRENCY)


def acquire_vl_slot() -> None:
    """获取 VL 请求槽位；排队超过 0.5s 时输出等待日志。

    等待超过 VL_SLOT_ACQUIRE_TIMEOUT 时抛 TimeoutError 快速失败（事故 §4.3：
    无超时等待会在引擎停摆时永久阻塞消费线程，进而占满整个执行器）。
    """
    global _INFLIGHT
    t0 = time.time()
    if not _VL_SEMAPHORE.acquire(timeout=VL_SLOT_ACQUIRE_TIMEOUT):
        raise TimeoutError(
            f"[vl-rate-limit] waited {time.time() - t0:.1f}s for a VL slot "
            f"(limit={VL_GLOBAL_CONCURRENCY}) and gave up; engine likely stalled"
        )
    with _LOCK:
        _INFLIGHT += 1
    wait = time.time() - t0
    if wait > 0.5:
        logging.info(f"[vl-rate-limit] waited {wait:.1f}s for a VL slot (limit={VL_GLOBAL_CONCURRENCY})")


def release_vl_slot() -> None:
    """释放 VL 请求槽位。

    若存在下调闸值遗留的延迟回收配额，本次归还改为吞掉该 permit（容量 -1），
    而非放回信号量。
    """
    global _INFLIGHT, _RECLAIM_ON_RELEASE
    with _LOCK:
        _INFLIGHT -= 1
        if _RECLAIM_ON_RELEASE > 0:
            _RECLAIM_ON_RELEASE -= 1
            return
    _VL_SEMAPHORE.release()
