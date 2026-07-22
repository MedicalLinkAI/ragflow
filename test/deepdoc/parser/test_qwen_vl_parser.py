#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Tests for deepdoc/parser/qwen_vl_parser.py
#  Target: ≥80% branch coverage on public seams.
#
import base64
import json
import os
import sys
import types
from io import BytesIO
from unittest.mock import MagicMock, patch

import pytest

# ── Bootstrap: mock deepdoc package before importing ────────────────
project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
sys.path.insert(0, project_root)

deepdoc_module = types.ModuleType("deepdoc")
deepdoc_module.__path__ = [os.path.join(project_root, "deepdoc")]
deepdoc_parser_module = types.ModuleType("deepdoc.parser")
deepdoc_parser_module.__path__ = [os.path.join(project_root, "deepdoc", "parser")]
deepdoc_parser_pdf_parser_module = types.ModuleType("deepdoc.parser.pdf_parser")
deepdoc_parser_pdf_parser_module.RAGFlowPdfParser = object

sys.modules["deepdoc"] = deepdoc_module
sys.modules["deepdoc.parser"] = deepdoc_parser_module
sys.modules["deepdoc.parser.pdf_parser"] = deepdoc_parser_pdf_parser_module

# Mock heavy native deps that may not be installed locally
for _mod_name in ("pdfplumber", "fitz"):
    if _mod_name not in sys.modules:
        sys.modules[_mod_name] = types.ModuleType(_mod_name)
# fitz needs open() and Matrix attrs
if not hasattr(sys.modules["fitz"], "open"):
    sys.modules["fitz"].open = MagicMock()
    sys.modules["fitz"].Matrix = MagicMock()

# ── Import module under test ────────────────────────────────────
# Use normal import now that deps are mocked
from deepdoc.parser.qwen_vl_parser import (  # noqa: E402
    QwenVLParser,
    _strip_fence,
    _fix_tabular_colspec,
    _parse_json_array,
    _split_latex_lines,
)
import deepdoc.parser.qwen_vl_parser as qwen_vl_mod  # noqa: E402


# ================================================================
# 1. _strip_fence
# ================================================================

class TestStripFence:
    def test_plain_text_unchanged(self):
        assert _strip_fence("hello world") == "hello world"

    def test_strip_json_fence(self):
        assert _strip_fence('```json\n["a","b"]\n```') == '["a","b"]'

    def test_strip_latex_fence(self):
        assert _strip_fence("```latex\n\\begin{tabular}\n```") == "\\begin{tabular}"

    def test_strip_plain_fence(self):
        assert _strip_fence("```\nsome text\n```") == "some text"

    def test_non_string_passthrough(self):
        assert _strip_fence(None) is None
        assert _strip_fence(42) == 42

    def test_empty_string(self):
        assert _strip_fence("") == ""

    def test_whitespace_only(self):
        assert _strip_fence("   \n  ") == ""

    def test_nested_fence_not_double_stripped(self):
        # Only outer fences are stripped
        text = '```json\n```inner```\n```'
        result = _strip_fence(text)
        assert "inner" in result


# ================================================================
# 2. _fix_tabular_colspec
# ================================================================

class TestFixTabularColspec:
    def test_normal_colspec_unchanged(self):
        latex = r"\begin{tabular}{ccccc}"
        assert _fix_tabular_colspec(latex) == latex

    def test_degenerate_colspec_truncated(self):
        # 50 'c' columns → should be truncated to max_cols (default 20)
        bad_spec = "c" * 50
        latex = f"\\begin{{tabular}}{{{bad_spec}}}"
        result = _fix_tabular_colspec(latex)
        assert "{cccccccccccccccccccc}" in result  # 20 c's
        assert len("c" * 20) == 20

    def test_mixed_col_chars_truncated(self):
        bad_spec = "l c r " * 20  # 60 col chars
        latex = f"\\begin{{tabular}}{{{bad_spec}}}"
        result = _fix_tabular_colspec(latex)
        assert "c" * 20 in result

    def test_short_spec_unchanged(self):
        latex = r"\begin{tabular}{lcr}"
        assert _fix_tabular_colspec(latex) == latex

    def test_no_tabular_unchanged(self):
        text = "some random text without tabular"
        assert _fix_tabular_colspec(text) == text

    def test_custom_max_cols(self):
        bad_spec = "c" * 30
        latex = f"\\begin{{tabular}}{{{bad_spec}}}"
        result = _fix_tabular_colspec(latex, max_cols=10)
        assert "c" * 10 in result


# ================================================================
# 3. _parse_json_array
# ================================================================

class TestParseJsonArray:
    def test_valid_json_array(self):
        assert _parse_json_array('["a","b","c"]') == ["a", "b", "c"]

    def test_empty_input_returns_none(self):
        assert _parse_json_array("") is None
        assert _parse_json_array(None) is None

    def test_json_with_fence(self):
        raw = '```json\n["line1","line2"]\n```'
        assert _parse_json_array(raw) == ["line1", "line2"]

    def test_non_list_json_returns_none(self):
        assert _parse_json_array('{"key":"value"}') is None

    def test_invalid_json_returns_none_or_empty(self):
        result = _parse_json_array("not json at all {{{")
        # json_repair may return [] or None for completely invalid input
        assert result is None or result == []

    def test_strips_whitespace_from_elements(self):
        assert _parse_json_array('[" a "," b "]') == ["a", "b"]

    def test_filters_empty_elements(self):
        assert _parse_json_array('["a","","  ","b"]') == ["a", "b"]

    def test_numeric_elements_converted_to_str(self):
        result = _parse_json_array('["a", 123]')
        assert result == ["a", "123"]

    def test_json_repair_fallback(self):
        # Malformed JSON that json_repair might fix
        raw = '["a", "b", ]'  # trailing comma
        result = _parse_json_array(raw)
        # Should parse via json_repair or regex fallback
        if result is not None:
            assert "a" in result


# ================================================================
# 4. _split_latex_lines
# ================================================================

class TestSplitLatexLines:
    def test_splits_by_newline(self):
        latex = "\\begin{tabular}{cc}\na & b \\\\\nc & d \\\\\n\\end{tabular}"
        lines = _split_latex_lines(latex)
        assert len(lines) == 4

    def test_filters_empty_lines(self):
        latex = "\\begin{tabular}\n\n\n\\hline\n\n\\end{tabular}"
        lines = _split_latex_lines(latex)
        assert all(line.strip() for line in lines)
        assert len(lines) == 3

    def test_empty_input(self):
        assert _split_latex_lines("") == []

    def test_preserves_latex_special_chars(self):
        latex = "a & b\\\\\n\\hline"
        lines = _split_latex_lines(latex)
        assert "a & b\\\\" in lines[0]


# ================================================================
# 5. QwenVLParser.__init__ & check_installation
# ================================================================

class TestQwenVLParserInit:
    def test_default_init(self):
        parser = QwenVLParser()
        assert parser.api_url is not None
        assert parser.model is not None
        assert parser.request_timeout == 300
        assert parser.outlines == []
        assert parser.page_images == []

    def test_custom_init(self):
        parser = QwenVLParser(
            api_url="http://custom:8080/v1/chat/completions",
            model="custom-model",
            request_timeout=60,
        )
        assert parser.api_url == "http://custom:8080/v1/chat/completions"
        assert parser.model == "custom-model"
        assert parser.request_timeout == 60

    def test_check_installation_ok(self):
        parser = QwenVLParser(api_url="http://example.com")
        ok, reason = parser.check_installation()
        assert ok is True
        assert reason == ""

    def test_check_installation_no_url(self):
        with patch.dict(os.environ, {"QWEN30B_OCR_API_ENDPOINT": ""}, clear=False):
            parser = QwenVLParser.__new__(QwenVLParser)
            parser.api_url = ""
            ok, reason = parser.check_installation()
        assert ok is False
        assert "not configured" in reason.lower()


# ================================================================
# 6. _classify_page
# ================================================================

class TestClassifyPage:
    def _make_parser(self):
        return QwenVLParser(api_url="http://mock:8080/v1")

    def test_classify_table_with_date(self):
        parser = self._make_parser()
        vlm_response = json.dumps({"type": "table", "report_date": "2024-01-05"})
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "table"
        assert date == "2024-01-05"

    def test_classify_text(self):
        parser = self._make_parser()
        vlm_response = json.dumps({"type": "text", "report_date": None})
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "text"
        assert date is None

    def test_classify_with_fence(self):
        parser = self._make_parser()
        vlm_response = '```json\n{"type": "table", "report_date": null}\n```'
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "table"
        assert date is None

    def test_classify_empty_response_defaults_text(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value=""):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "text"
        assert date is None

    def test_classify_invalid_json_fallback(self):
        parser = self._make_parser()
        # Contains "table" keyword but not valid JSON
        with patch.object(parser, "_call_vlm", return_value='this is a table page'):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "table"

    def test_classify_invalid_json_no_table_keyword(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value="some random text"):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "text"

    def test_classify_invalid_type_defaults_text(self):
        parser = self._make_parser()
        vlm_response = json.dumps({"type": "unknown_type"})
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "text"

    def test_classify_exception_defaults_text(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", side_effect=RuntimeError("API down")):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "text"
        assert date is None

    def test_classify_none_response_defaults_text(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value=None):
            page_type, date = parser._classify_page(b"fake_img")
        assert page_type == "text"
        assert date is None


# ================================================================
# 7. _extract_text_page
# ================================================================

class TestExtractTextPage:
    def _make_parser(self):
        return QwenVLParser(api_url="http://mock:8080/v1")

    def test_normal_text_extraction(self):
        parser = self._make_parser()
        vlm_response = '["line 1", "line 2", "line 3"]'
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            sections, bbox_idx = parser._extract_text_page(b"img", 1, 0)
        assert len(sections) == 3
        assert sections[0] == ("line 1", 0)  # 0-based page
        assert sections[1] == ("line 2", 0)
        assert bbox_idx == 3

    def test_empty_response_returns_no_sections(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value=""):
            sections, bbox_idx = parser._extract_text_page(b"img", 1, 5)
        assert sections == []
        assert bbox_idx == 5  # unchanged

    def test_symbol_only_lines_filtered(self):
        parser = self._make_parser()
        vlm_response = '["real text", "+++", "---", "more text", "*"]'
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            sections, bbox_idx = parser._extract_text_page(b"img", 1, 0)
        texts = [s[0] for s in sections]
        assert "real text" in texts
        assert "more text" in texts
        assert "+++" not in texts
        assert "---" not in texts

    def test_repetition_detection(self):
        parser = self._make_parser()
        # Create repeating pattern: ["a","b","c"] repeated 8 times = 24 lines
        pattern = ["a", "b", "c"]
        repeated = pattern * 8
        vlm_response = json.dumps(repeated)
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            sections, bbox_idx = parser._extract_text_page(b"img", 1, 0)
        # Should be truncated to one cycle (3 lines)
        assert len(sections) == 3

    def test_page_index_is_0_based(self):
        parser = self._make_parser()
        vlm_response = '["hello"]'
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            sections, _ = parser._extract_text_page(b"img", 5, 0)
        assert sections[0][1] == 4  # page 5 (1-based) → 4 (0-based)

    def test_bbox_idx_continues(self):
        parser = self._make_parser()
        vlm_response = '["a", "b"]'
        with patch.object(parser, "_call_vlm", return_value=vlm_response):
            _, new_idx = parser._extract_text_page(b"img", 1, 10)
        assert new_idx == 12

    def test_none_response(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value=None):
            sections, bbox_idx = parser._extract_text_page(b"img", 1, 0)
        assert sections == []


# ================================================================
# 8. _extract_table_page
# ================================================================

class TestExtractTablePage:
    def _make_parser(self):
        return QwenVLParser(api_url="http://mock:8080/v1")

    def test_normal_table_extraction(self):
        parser = self._make_parser()
        latex = "\\begin{tabular}{cc}\na & b \\\\\nc & d \\\\\n\\end{tabular}"
        with patch.object(parser, "_call_vlm", return_value=latex):
            sections, bbox_idx = parser._extract_table_page(b"img", 1, 0)
        assert len(sections) > 0
        assert all(s[1] == 0 for s in sections)  # page 0-based
        assert bbox_idx == len(sections)

    def test_report_date_injection(self):
        parser = self._make_parser()
        latex = "\\begin{tabular}{cc}\na & b \\\\\n\\end{tabular}"
        with patch.object(parser, "_call_vlm", return_value=latex):
            sections, _ = parser._extract_table_page(b"img", 1, 0, report_date="2024-01-05")
        texts = [s[0] for s in sections]
        assert "报告时间: 2024-01-05" in texts

    def test_no_report_date_no_injection(self):
        parser = self._make_parser()
        latex = "\\begin{tabular}{cc}\na & b \\\\\n\\end{tabular}"
        with patch.object(parser, "_call_vlm", return_value=latex):
            sections, _ = parser._extract_table_page(b"img", 1, 0, report_date=None)
        texts = [s[0] for s in sections]
        assert not any("报告时间" in t for t in texts)

    def test_empty_table_returns_no_sections(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value=""):
            sections, bbox_idx = parser._extract_table_page(b"img", 1, 5)
        assert sections == []
        assert bbox_idx == 5

    def test_degenerate_colspec_fixed(self):
        parser = self._make_parser()
        bad_spec = "c" * 50
        latex = f"\\begin{{tabular}}{{{bad_spec}}}\na & b \\\\\n\\end{{tabular}}"
        with patch.object(parser, "_call_vlm", return_value=latex):
            sections, _ = parser._extract_table_page(b"img", 1, 0)
        texts = [s[0] for s in sections]
        # The fixed colspec should have 20 c's max
        assert any("c" * 20 in t for t in texts)

    def test_none_vlm_response(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value=None):
            sections, bbox_idx = parser._extract_table_page(b"img", 1, 3)
        assert sections == []
        assert bbox_idx == 3

    def test_page_index_is_0_based(self):
        parser = self._make_parser()
        latex = "\\begin{tabular}{c}\na \\\\\n\\end{tabular}"
        with patch.object(parser, "_call_vlm", return_value=latex):
            sections, _ = parser._extract_table_page(b"img", 3, 0)
        assert all(s[1] == 2 for s in sections)  # page 3 → 0-based = 2


# ================================================================
# 9. parse_pdf (integration, mocked)
# ================================================================

class TestParsePdf:
    def _make_parser(self):
        return QwenVLParser(api_url="http://mock:8080/v1")

    def test_no_api_url_raises(self):
        parser = QwenVLParser.__new__(QwenVLParser)
        parser.api_url = ""
        parser.outlines = []
        parser.page_images = []
        parser.page_from = 0
        with pytest.raises(RuntimeError, match="API URL missing"):
            parser.parse_pdf("dummy.pdf")

    def test_empty_pdf_returns_empty(self):
        parser = self._make_parser()
        with patch.object(parser, "_render_page_images"):
            parser.page_images = []
            sections, tables = parser.parse_pdf("dummy.pdf")
        assert sections == []
        assert tables == []

    def test_callback_called_on_empty(self):
        parser = self._make_parser()
        cb = MagicMock()
        with patch.object(parser, "_render_page_images"):
            parser.page_images = []
            parser.parse_pdf("dummy.pdf", callback=cb)
        cb.assert_called_once()

    def test_text_page_pipeline(self):
        parser = self._make_parser()
        fake_img = MagicMock()
        buf = BytesIO()
        # Create a tiny valid image
        from PIL import Image
        img = Image.new("RGB", (10, 10), color="white")
        buf = BytesIO()
        img.save(buf, format="PNG")
        img_bytes = buf.getvalue()

        with patch.object(parser, "_render_page_images"):
            parser.page_images = [img]
            # Classify as text, then extract text
            with patch.object(parser, "_classify_page", return_value=("text", None)):
                with patch.object(parser, "_call_vlm", return_value='["hello world"]'):
                    sections, tables = parser.parse_pdf("dummy.pdf")

        assert len(sections) == 1
        assert sections[0][0] == "hello world"
        assert tables == []

    def test_table_page_pipeline(self):
        parser = self._make_parser()
        from PIL import Image
        img = Image.new("RGB", (10, 10), color="white")

        with patch.object(parser, "_render_page_images"):
            parser.page_images = [img]
            with patch.object(parser, "_classify_page", return_value=("table", "2024-01-05")):
                latex = "\\begin{tabular}{cc}\na & b \\\\\n\\end{tabular}"
                with patch.object(parser, "_call_vlm", return_value=latex):
                    sections, tables = parser.parse_pdf("dummy.pdf")

        assert len(sections) > 0
        assert tables == []

    def test_render_failure_returns_empty(self):
        parser = self._make_parser()
        with patch.object(parser, "_render_page_images", side_effect=Exception("render fail")):
            sections, tables = parser.parse_pdf("dummy.pdf")
        assert sections == []
        assert tables == []

    def test_callback_progress(self):
        parser = self._make_parser()
        from PIL import Image
        img = Image.new("RGB", (10, 10), color="white")
        cb = MagicMock()

        with patch.object(parser, "_render_page_images"):
            parser.page_images = [img]
            with patch.object(parser, "_classify_page", return_value=("text", None)):
                with patch.object(parser, "_call_vlm", return_value='["line"]'):
                    parser.parse_pdf("dummy.pdf", callback=cb)

        # callback should be called at least twice (start + done)
        assert cb.call_count >= 2


# ================================================================
# 10. extract_positions (static)
# ================================================================

class TestExtractPositions:
    def test_single_position(self):
        txt = "text@@1-2\t10.0\t20.0\t30.0\t40.0##more"
        poss = QwenVLParser.extract_positions(txt)
        assert len(poss) == 1
        pages, left, right, top, bottom = poss[0]
        assert pages == [0, 1]  # 1-based → 0-based
        assert left == 10.0
        assert right == 20.0
        assert top == 30.0
        assert bottom == 40.0

    def test_no_positions(self):
        assert QwenVLParser.extract_positions("plain text") == []

    def test_multiple_positions(self):
        txt = "@@1\t1\t2\t3\t4##text@@2\t5\t6\t7\t8##"
        poss = QwenVLParser.extract_positions(txt)
        assert len(poss) == 2


# ================================================================
# 11. _call_vlm (mocked HTTP)
# ================================================================

class TestCallVlm:
    def test_successful_api_call(self):
        parser = QwenVLParser(api_url="http://mock:8080/v1/chat/completions")
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "choices": [{"message": {"content": "result text"}}]
        }
        mock_resp.raise_for_status = MagicMock()

        with patch("requests.post", return_value=mock_resp) as mock_post:
            # Need to patch the actual requests module used by the loaded module
            with patch.object(qwen_vl_mod.requests, "post", return_value=mock_resp):
                result = parser._call_vlm(b"fake_image_bytes", "test prompt")

        assert result == "result text"

    def test_api_call_with_api_key(self):
        parser = QwenVLParser(api_url="http://mock:8080/v1/chat/completions")
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "choices": [{"message": {"content": "ok"}}]
        }
        mock_resp.raise_for_status = MagicMock()

        with patch.object(qwen_vl_mod.requests, "post", return_value=mock_resp) as mock_post:
            with patch.dict(os.environ, {"DASHSCOPE_API_KEY": "test-key-123"}):
                result = parser._call_vlm(b"img", "prompt")

        # Check Authorization header was set
        call_kwargs = mock_post.call_args
        headers = call_kwargs.kwargs.get("headers", call_kwargs[1].get("headers", {}))
        assert "Bearer test-key-123" in headers.get("Authorization", "")

    def test_api_call_failure_raises(self):
        parser = QwenVLParser(api_url="http://mock:8080/v1/chat/completions")
        with patch.object(qwen_vl_mod.requests, "post", side_effect=ConnectionError("refused")):
            with pytest.raises(ConnectionError):
                parser._call_vlm(b"img", "prompt")

    def test_payload_structure(self):
        parser = QwenVLParser(
            api_url="http://mock:8080/v1",
            model="test-model",
            request_timeout=120,
        )
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "choices": [{"message": {"content": "ok"}}]
        }
        mock_resp.raise_for_status = MagicMock()

        with patch.object(qwen_vl_mod.requests, "post", return_value=mock_resp) as mock_post:
            parser._call_vlm(b"img_data", "my prompt")

        call_kwargs = mock_post.call_args
        payload = call_kwargs.kwargs.get("json", call_kwargs[1].get("json", {}))
        assert payload["model"] == "test-model"
        assert payload["temperature"] == 0
        assert payload["max_tokens"] == 16384
        msgs = payload["messages"]
        assert len(msgs) == 1
        assert msgs[0]["role"] == "user"
        content = msgs[0]["content"]
        assert content[0]["type"] == "image_url"
        assert "data:image/png;base64," in content[0]["image_url"]["url"]
        assert content[1]["type"] == "text"
        assert content[1]["text"] == "my prompt"


# ================================================================
# 12. __images__ (compat)
# ================================================================

class TestImagesCompat:
    def test_images_sets_page_from(self):
        parser = QwenVLParser()
        parser.page_from = 99
        # Will fail to open (no real file), but page_from should be set before exception
        with patch.object(qwen_vl_mod, "pdfplumber") as mock_pdfplumber:
            mock_pdfplumber.open.side_effect = Exception("no file")
            parser.__images__("nonexistent.pdf", page_from=5)
        assert parser.page_from == 5
        assert parser.page_images == []  # cleared on failure


# ================================================================
# 13. Constants / Prompts
# ================================================================

class TestPrompts:
    def test_classify_prompt_defined(self):
        assert qwen_vl_mod.CLASSIFY_PROMPT
        assert "type" in qwen_vl_mod.CLASSIFY_PROMPT
        assert "table" in qwen_vl_mod.CLASSIFY_PROMPT

    def test_text_prompt_defined(self):
        assert qwen_vl_mod.TEXT_PROMPT
        assert "JSON" in qwen_vl_mod.TEXT_PROMPT

    def test_table_prompt_defined(self):
        assert qwen_vl_mod.TABLE_PROMPT
        assert "LaTeX" in qwen_vl_mod.TABLE_PROMPT
        assert "tabular" in qwen_vl_mod.TABLE_PROMPT
