# vl_engine_retry.py — vLLM 引擎死亡时的快速失败 + 有界退避重试
#
# 背景（2026-08-22 事故，报告 §11 S6）：
#   vLLM EngineCore 崩溃后向所有在飞请求回 500（EngineDeadError），
#   容器 15~60s 内自动拉起。旧客户端收到 500 立即判失败、无任何重试，
#   整个重启窗口内的请求全部白白牺牲（日志实锤 239 次失败）。
#
# 本模块只针对"引擎死亡"特征做有限重试（3 次尝试、退避 2s → 4s）：
#   - HTTP 500 且响应体含引擎死亡签名（EngineDeadError / 引擎启动失败）；
#   - HTTP 502/503（反向代理看到后端引擎已死，响应体可能无签名）；
#   - ConnectionError（重启窗口内端口关闭，连接直接被拒）。
# 其余错误（400 类请求错误、无签名的 500、ReadTimeout）维持现状：
#   - 无签名 500 / 4xx 重试无意义，快速失败；
#   - ReadTimeout（120s 挂起）由 60 分钟任务看门狗兜底，此处重试只会
#     给停摆引擎叠加负载。

import logging
import time

import requests

# 总尝试次数（含首次）；退避序列 = 2s, 4s（指数、有界）
VL_ENGINE_MAX_ATTEMPTS = 3
VL_ENGINE_BACKOFF_BASE = 2

# vLLM APIServer 在引擎死亡时写入响应体的典型签名
_ENGINE_DEAD_SIGNATURES = (
    "EngineDeadError",
    "Engine core initialization failed",
    "EngineCore failed to start",
)
# 网关/代理视角的后端不可用：无需签名也重试
_GATEWAY_DEAD_STATUSES = (502, 503)


def _is_engine_dead_response(resp) -> bool:
    if resp.status_code in _GATEWAY_DEAD_STATUSES:
        return True
    if resp.status_code == 500:
        body = getattr(resp, "text", "") or ""
        return any(sig in body for sig in _ENGINE_DEAD_SIGNATURES)
    return False


def post_with_engine_retry(url, **kwargs):
    """requests.post 的引擎死亡重试包装。

    引擎死亡特征（签名 500 / 502 / 503 / ConnectionError）按退避重试，
    覆盖容器重启窗口；耗尽尝试后返回最后一次响应（或抛出最后一次
    ConnectionError）。其余异常（含 ReadTimeout/ConnectTimeout）原样上抛。
    """
    last_exc = None
    for attempt in range(1, VL_ENGINE_MAX_ATTEMPTS + 1):
        try:
            resp = requests.post(url, **kwargs)
        except requests.exceptions.ConnectionError as e:
            # 重启窗口内端口关闭：等引擎回来
            last_exc = e
            logging.warning(
                f"[vl-engine-retry] connection failed (attempt {attempt}/{VL_ENGINE_MAX_ATTEMPTS}): {e}"
            )
        else:
            if not _is_engine_dead_response(resp):
                return resp
            logging.warning(
                f"[vl-engine-retry] engine-dead response HTTP {resp.status_code} "
                f"(attempt {attempt}/{VL_ENGINE_MAX_ATTEMPTS}), body={resp.text[:200]}"
            )
        if attempt < VL_ENGINE_MAX_ATTEMPTS:
            time.sleep(VL_ENGINE_BACKOFF_BASE ** attempt)
    if last_exc is not None:
        raise last_exc
    return resp
