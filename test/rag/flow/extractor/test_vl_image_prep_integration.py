#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Integration test: 所有 VL 发送点在 payload 组装前必须对超限页面图做
#  downscale（长边 ≤3840px、JPEG q85、<1.8MB），MIME 随实际编码切换。
#
#  背景（2026-08-16 并发重解析基准）：200 DPI 病案页 PNG 中位数 1.46MB、
#  p90 4.67MB、max 14.7MB；>2MB 调用占 34%，是 120s/300s 超时的高风险区。
#  样本为 MedLinkAI page-image API 真实页面（5.28MB PNG, 2339x1653）。
#
import base64
import os
import sys
import types
from pathlib import Path
from unittest.mock import MagicMock, patch

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)
sys.path.insert(0, project_root)


def _fake_pkg(name, path=None):
    mod = types.ModuleType(name)
    if path:
        mod.__path__ = [path]
    sys.modules.setdefault(name, mod)
    return mod


# ── rag 包 bootstrap（与 test_vl_rate_limit_integration.py 一致） ──
_fake_pkg("rag", os.path.join(project_root, "rag"))
_fake_pkg("rag.flow", os.path.join(project_root, "rag", "flow"))
_fake_pkg("rag.flow.extractor", os.path.join(project_root, "rag", "flow", "extractor"))

_extractor_stub = types.ModuleType("rag.flow.extractor.extractor")
_extractor_stub.strip_markdown_json_fence = lambda s: s
sys.modules.setdefault("rag.flow.extractor.extractor", _extractor_stub)

for _n in ("api", "api.db", "api.db.services"):
    _fake_pkg(_n)
_tls_stub = types.ModuleType("api.db.services.tenant_llm_service")


class _TenantLLMService:
    @staticmethod
    def get_api_key(tenant_id, llm_name):
        return None


_tls_stub.TenantLLMService = _TenantLLMService
sys.modules.setdefault("api.db.services.tenant_llm_service", _tls_stub)

# ── deepdoc 包 bootstrap（与 test_qwen_vl_parser.py 一致） ──
_deepdoc = _fake_pkg("deepdoc", os.path.join(project_root, "deepdoc"))
_deepdoc_parser = _fake_pkg("deepdoc.parser", os.path.join(project_root, "deepdoc", "parser"))
_pdf_parser_stub = types.ModuleType("deepdoc.parser.pdf_parser")
_pdf_parser_stub.RAGFlowPdfParser = object
sys.modules["deepdoc.parser.pdf_parser"] = _pdf_parser_stub

for _mod_name in ("pdfplumber", "fitz"):
    if _mod_name not in sys.modules:
        sys.modules[_mod_name] = types.ModuleType(_mod_name)
if not hasattr(sys.modules["fitz"], "open"):
    sys.modules["fitz"].open = MagicMock()
    sys.modules["fitz"].Matrix = MagicMock()

import rag.flow.extractor.qwen_vl_ocr as qvl  # noqa: E402
import rag.flow.extractor.qwen30b_ocr as q30  # noqa: E402
import rag.flow.extractor.vl_image_prep as prep  # noqa: E402
from deepdoc.parser.qwen_vl_parser import QwenVLParser  # noqa: E402
import deepdoc.parser.qwen_vl_parser as qvl_parser_mod  # noqa: E402

FIXTURE = Path(project_root) / "rag" / "tests" / "fixtures" / "real_page_5mb.png"
ENDPOINT_CFG = ("http://fake/chat/completions", "Qwen3-VL-30B", "")


def _small_png() -> bytes:
    from PIL import Image
    import io

    row = bytes(x % 256 for x in range(300))
    img = Image.frombytes("RGB", (100, 100), row * 100)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


class _FakeResponse:
    status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return {"choices": [{"message": {"content": '[{"text": "a", "bbox": [1,2,3,4]}]'}}]}


def _capture_payload(fn, *args, **kwargs):
    """Run fn with requests.post patched; return the captured JSON payload."""
    captured = {}

    def fake_post(url, json=None, **kw):
        captured["payload"] = json
        return _FakeResponse()

    with patch.object(qvl.requests, "post", side_effect=fake_post), \
         patch.object(q30.requests, "post", side_effect=fake_post), \
         patch.object(qvl_parser_mod.requests, "post", side_effect=fake_post):
        fn(*args, **kwargs)
    return captured["payload"]


def _image_url(payload):
    for msg in payload["messages"]:
        if msg["role"] == "user":
            for part in msg["content"]:
                if part.get("type") == "image_url":
                    return part["image_url"]["url"]
    raise AssertionError("payload 中没有 image_url")


def _assert_downscaled(payload, original: bytes):
    url = _image_url(payload)
    assert url.startswith("data:image/jpeg;base64,"), \
        f"超限图应转为 JPEG data URL，实际前缀: {url[:40]}"
    decoded = base64.b64decode(url.split(",", 1)[1])
    assert len(decoded) <= prep.TARGET_BYTES, \
        f"payload 图像 {len(decoded)/1048576:.2f}MB 超过目标 1.8MB"
    assert len(decoded) < len(original), \
        f"payload 图像未变小: {len(decoded)} >= {len(original)}"


def test_coord_call_downscales_oversized_image():
    if not FIXTURE.exists():
        raise AssertionError("真实页面 fixture 缺失")
    big = FIXTURE.read_bytes()
    payload = _capture_payload(qvl._call_qwen30b_coord, big, "p", "[test]", ENDPOINT_CFG, 0)
    _assert_downscaled(payload, big)


def test_30b_to_coord_downscales_oversized_image():
    big = FIXTURE.read_bytes()
    payload = _capture_payload(q30._call_qwen30b_to_coord, big, "p", "[test]", ENDPOINT_CFG)
    _assert_downscaled(payload, big)


def test_30b_text_only_downscales_oversized_image():
    big = FIXTURE.read_bytes()
    payload = _capture_payload(q30._call_qwen30b_text_only, big, "p", "[test]", ENDPOINT_CFG)
    _assert_downscaled(payload, big)


def test_30b_latex_only_downscales_oversized_image():
    big = FIXTURE.read_bytes()
    payload = _capture_payload(q30._call_qwen30b_latex_only, big, "p", "[test]", ENDPOINT_CFG)
    _assert_downscaled(payload, big)


def test_parser_call_vlm_downscales_oversized_image():
    big = FIXTURE.read_bytes()
    parser = QwenVLParser()
    parser.model = "Qwen3-VL-30B"
    parser.api_key = ""
    parser.api_url = "http://fake/chat/completions"
    parser.request_timeout = 5
    payload = _capture_payload(parser._call_vlm, big, "p")
    _assert_downscaled(payload, big)


def test_small_image_passes_through_as_png():
    small = _small_png()
    payload = _capture_payload(qvl._call_qwen30b_coord, small, "p", "[test]", ENDPOINT_CFG, 0)
    url = _image_url(payload)
    assert url.startswith("data:image/png;base64,"), \
        f"小图应保持 PNG，实际前缀: {url[:40]}"
    assert base64.b64decode(url.split(",", 1)[1]) == small, "小图字节应原样直通"
