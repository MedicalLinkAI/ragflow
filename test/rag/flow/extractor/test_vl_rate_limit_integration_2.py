#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Integration tests: 其余 VL 调用点必须受进程级信号量保护
#    - qwen30b_ocr._call_qwen30b_to_coord / _call_qwen30b_text_only / _call_qwen30b_latex_only
#    - qwen_vl_parser.QwenVLParser._call_vlm
#
#  与 test_vl_rate_limit_integration.py 同因：22:28 洪峰时这些调用与 coord
#  共享同一块 GPU，必须一起受全局限流约束。
#
import os
import sys
import threading
import time
import types
from unittest.mock import MagicMock, patch

import pytest

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


# rag 包：fake 壳 + 真实 __path__（避开 rag/flow/__init__.py 的全量 walk-import）
_fake_pkg("rag", os.path.join(project_root, "rag"))
_fake_pkg("rag.flow", os.path.join(project_root, "rag", "flow"))
_fake_pkg("rag.flow.extractor", os.path.join(project_root, "rag", "flow", "extractor"))

_extractor_stub = types.ModuleType("rag.flow.extractor.extractor")
_extractor_stub.strip_markdown_json_fence = lambda s: s
sys.modules["rag.flow.extractor.extractor"] = _extractor_stub

for _n in ("api", "api.db", "api.db.services"):
    _fake_pkg(_n)
_fds_mod = types.ModuleType("api.db.services.file2document_service")


class _File2DocumentService:
    @staticmethod
    def get_storage_address(doc_id=None):
        return "bucket", "name"


_fds_mod.File2DocumentService = _File2DocumentService
sys.modules["api.db.services.file2document_service"] = _fds_mod

# 挂真实 __path__：qwen_vl_ocr 导入 common.log_tag（TAG 归因），
# 纯 ModuleType 不是包会导致 ModuleNotFoundError
_common_mod = _fake_pkg("common", os.path.join(project_root, "common"))
_settings_mod = types.ModuleType("common.settings")


class _Storage:
    @staticmethod
    def get(b, n):
        return b"%PDF-FAKE"


_settings_mod.STORAGE_IMPL = _Storage
sys.modules["common.settings"] = _settings_mod
_common_mod.settings = _settings_mod

# deepdoc 包 fake（qwen_vl_parser 只依赖 deepdoc.parser.pdf_parser）
_fake_pkg("deepdoc", os.path.join(project_root, "deepdoc"))
_fake_pkg("deepdoc.parser", os.path.join(project_root, "deepdoc", "parser"))
_pdf_parser_stub = types.ModuleType("deepdoc.parser.pdf_parser")
_pdf_parser_stub.RAGFlowPdfParser = object
sys.modules["deepdoc.parser.pdf_parser"] = _pdf_parser_stub

for _mod_name in ("pdfplumber",):
    if _mod_name not in sys.modules:
        sys.modules[_mod_name] = types.ModuleType(_mod_name)

import rag.flow.extractor.vl_rate_limit as vrl  # noqa: E402
import rag.flow.extractor.qwen30b_ocr as q30b  # noqa: E402
import deepdoc.parser.qwen_vl_parser as qvp  # noqa: E402


class _FakeResponse:
    status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return {"choices": [{"message": {"content": '[{"text": "a", "bbox": [1,2,3,4]}]'}}]}


def _run_concurrent(target_mod, call_fn, n=10):
    """n 线程并发执行 call_fn，返回在飞 requests.post 峰值。

    target_mod: 被 patch requests.post 的模块（调用方所在模块）。
    """
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

    with patch.object(target_mod.requests, "post", side_effect=fake_post):
        threads = [threading.Thread(target=call_fn) for _ in range(n)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    return peak


@pytest.fixture(autouse=True)
def _limit_three():
    vrl.VL_GLOBAL_CONCURRENCY = 3
    vrl._rebuild_semaphore()
    yield


ENDPOINT_CFG = ("http://fake/chat/completions", "Qwen3-VL-30B", "")


def test_qwen30b_to_coord_capped():
    peak = _run_concurrent(
        q30b, lambda: q30b._call_qwen30b_to_coord(b"img", "prompt", "[test]", ENDPOINT_CFG)
    )
    assert peak <= 3, f"_call_qwen30b_to_coord 在飞峰值 {peak} 超过全局限流 3"


def test_qwen30b_text_only_capped():
    peak = _run_concurrent(
        q30b, lambda: q30b._call_qwen30b_text_only(b"img", "prompt", "[test]", ENDPOINT_CFG)
    )
    assert peak <= 3, f"_call_qwen30b_text_only 在飞峰值 {peak} 超过全局限流 3"


def test_qwen30b_latex_only_capped():
    peak = _run_concurrent(
        q30b, lambda: q30b._call_qwen30b_latex_only(b"img", "prompt", "[test]", ENDPOINT_CFG)
    )
    assert peak <= 3, f"_call_qwen30b_latex_only 在飞峰值 {peak} 超过全局限流 3"


def test_parser_call_vlm_capped():
    parser = qvp.QwenVLParser(api_url="http://fake/chat/completions", model="Qwen3-VL-30B")
    peak = _run_concurrent(qvp, lambda: parser._call_vlm(b"img", "prompt"))
    assert peak <= 3, f"QwenVLParser._call_vlm 在飞峰值 {peak} 超过全局限流 3"
