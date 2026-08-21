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
# VL_GLOBAL_CONCURRENCY（默认 8，可用环境变量 VL_GLOBAL_CONCURRENCY 覆盖）。
#
# 注意：RAGFlow 有 4 个 task_executor 进程，进程间无法共享该信号量；
# 跨进程兜底依赖 vLLM 侧 --max-num-seqs 配置。

import logging
import os
import threading
import time

_DEFAULT_CONCURRENCY = 8


def _resolve_limit() -> int:
    raw = os.environ.get("VL_GLOBAL_CONCURRENCY", "")
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return _DEFAULT_CONCURRENCY
    if value <= 0:
        logging.warning(
            f"[vl-rate-limit] invalid VL_GLOBAL_CONCURRENCY={raw}, "
            f"fallback to {_DEFAULT_CONCURRENCY}"
        )
        return _DEFAULT_CONCURRENCY
    return value


VL_GLOBAL_CONCURRENCY = _resolve_limit()
_VL_SEMAPHORE = threading.Semaphore(VL_GLOBAL_CONCURRENCY)


def _rebuild_semaphore() -> None:
    """按当前 VL_GLOBAL_CONCURRENCY 重建信号量（测试专用）。"""
    global _VL_SEMAPHORE
    _VL_SEMAPHORE = threading.Semaphore(VL_GLOBAL_CONCURRENCY)


def acquire_vl_slot() -> None:
    """获取 VL 请求槽位；排队超过 0.5s 时输出等待日志。"""
    t0 = time.time()
    _VL_SEMAPHORE.acquire()
    wait = time.time() - t0
    if wait > 0.5:
        logging.info(f"[vl-rate-limit] waited {wait:.1f}s for a VL slot (limit={VL_GLOBAL_CONCURRENCY})")


def release_vl_slot() -> None:
    """释放 VL 请求槽位。"""
    _VL_SEMAPHORE.release()
