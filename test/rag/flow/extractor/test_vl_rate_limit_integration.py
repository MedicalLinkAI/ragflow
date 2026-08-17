#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Integration test: _call_qwen30b_coord 必须受进程级 VL 信号量保护
#
#  背景（2026-08-15 22:28 洪峰）：chunk 级并发 6 × 多线程同时打 vLLM(8090)，
#  prefill 风暴导致 generation throughput 崩溃、4 个 coord 120s 超时。
#  本测试验证：10 个线程并发调用 _call_qwen30b_coord 时，同时在飞的
#  requests.post 数量峰值不超过 VL_GLOBAL_CONCURRENCY。
#
import os
import sys
import threading
import time
import types
from unittest.mock import patch

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)
sys.path.insert(0, project_root)


def _fake_pkg(name, path=None):
    mod = types.ModuleType(name)
    if path:
        mod.__path__ = [path]
    sys.modules[name] = mod
    return mod


_fake_pkg("rag", os.path.join(project_root, "rag"))
_fake_pkg("rag.flow", os.path.join(project_root, "rag", "flow"))
_fake_pkg("rag.flow.extractor", os.path.join(project_root, "rag", "flow", "extractor"))

_extractor_stub = types.ModuleType("rag.flow.extractor.extractor")
_extractor_stub.strip_markdown_json_fence = lambda s: s
sys.modules["rag.flow.extractor.extractor"] = _extractor_stub

for _n in ("api", "api.db", "api.db.services"):
    _fake_pkg(_n)
_tls_stub = types.ModuleType("api.db.services.tenant_llm_service")


class _TenantLLMService:
    @staticmethod
    def get_api_key(tenant_id, llm_name):
        return None


_tls_stub.TenantLLMService = _TenantLLMService
sys.modules["api.db.services.tenant_llm_service"] = _tls_stub

import rag.flow.extractor.vl_rate_limit as vrl  # noqa: E402
import rag.flow.extractor.qwen_vl_ocr as qvl  # noqa: E402


class _FakeResponse:
    status_code = 200

    def json(self):
        return {"choices": [{"message": {"content": '[{"text": "a", "bbox": [1,2,3,4]}]'}}]}


def test_coord_calls_capped_by_global_semaphore():
    vrl.VL_GLOBAL_CONCURRENCY = 3
    vrl._rebuild_semaphore()

    active = 0
    peak = 0
    lock = threading.Lock()

    def fake_post(*args, **kwargs):
        nonlocal active, peak
        with lock:
            active += 1
            peak = max(peak, active)
        time.sleep(0.05)
        with lock:
            active -= 1
        return _FakeResponse()

    endpoint_cfg = ("http://fake/chat/completions", "Qwen3-VL-30B", "")

    def one_call():
        qvl._call_qwen30b_coord(b"img", "prompt", "[test]", endpoint_cfg, 0)

    with patch.object(qvl.requests, "post", side_effect=fake_post):
        threads = [threading.Thread(target=one_call) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    assert peak <= 3, f"在飞请求峰值 {peak} 超过全局限流上限 3"
