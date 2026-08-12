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
    _has_repetition_loop,
    _truncate_repetition_loop,
    _dedup_repeated_blocks,
    _dedup_latex_rows,
    _is_empty_flood,
    _is_truncated_array,
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
        # 端点/模型不再从环境变量取默认值，未传入时为 None，由 check_installation 拦截
        assert parser.api_url is None
        assert parser.model is None
        assert parser.api_key == ""
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
        # api_key 由调用方构造注入（零环境变量约定），不再读环境变量
        parser = QwenVLParser(
            api_url="http://mock:8080/v1/chat/completions",
            api_key="test-key-123",
        )
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "choices": [{"message": {"content": "ok"}}]
        }
        mock_resp.raise_for_status = MagicMock()

        with patch.object(qwen_vl_mod.requests, "post", return_value=mock_resp) as mock_post:
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

    def test_table_prompt_forbids_textup_wrapping(self):
        # 生产幻觉案例：模型用 \textup{ 包裹 ↑ 箭头后陷入重复循环
        assert "\\textup" in qwen_vl_mod.TABLE_PROMPT


# ================================================================
# 14. Repetition-loop hallucination defense (table path)
# ================================================================

LOOP = "\\textup{" * 500  # degenerate nesting as seen in production logs


class TestHasRepetitionLoop:
    def test_detects_nested_textup_loop(self):
        latex = "\\begin{tabular}{cc}\na & b \\\\\n[AST/ALT]谷草/谷丙 & 2.14 & & " + LOOP
        assert _has_repetition_loop(latex) is True

    def test_normal_latex_no_loop(self):
        latex = "\\begin{tabular}{cc}\na & \\textmu mol/L \\\\\n\\end{tabular}"
        assert _has_repetition_loop(latex) is False

    def test_single_textup_not_loop(self):
        # 合法的单个 \textup{↑} 不应被判为循环
        assert _has_repetition_loop("x & \\textup{↑} & y \\\\") is False

    def test_empty_input(self):
        assert _has_repetition_loop("") is False
        assert _has_repetition_loop(None) is False


class TestTruncateRepetitionLoop:
    def test_cut_drops_incomplete_row(self):
        prefix = "\\begin{tabular}{cc}\na & b \\\\\n[AST]谷草 & 15 & & "
        out = _truncate_repetition_loop(prefix + LOOP)
        assert "\\textup" not in out
        assert "a & b" in out
        assert "[AST]" not in out  # 循环所在的不完整行被丢弃

    def test_cut_keeps_complete_rows(self):
        prefix = "\\begin{tabular}{cc}\na & b \\\\\nc & d \\\\\n"
        out = _truncate_repetition_loop(prefix + LOOP)
        assert "\\textup" not in out
        assert "c & d" in out

    def test_no_loop_unchanged(self):
        latex = "\\begin{tabular}{c}\na \\\\\n\\end{tabular}"
        assert _truncate_repetition_loop(latex) == latex


class TestTableRepetitionRetry:
    def _make_parser(self):
        return QwenVLParser(api_url="http://mock:8080/v1")

    def test_retry_recovers_full_table(self):
        parser = self._make_parser()
        looped = "\\begin{tabular}{cc}\na & b \\\\\nc & " + LOOP
        clean = "\\begin{tabular}{cc}\na & b \\\\\nc & d \\\\\n\\end{tabular}"
        with patch.object(parser, "_call_vlm", side_effect=[looped, clean]) as m:
            sections, _ = parser._extract_table_page(b"img", 1, 0)
        assert m.call_count == 2
        # 重试必须携带 repetition_penalty 以跳出贪心循环
        extra = m.call_args_list[1].kwargs.get("extra_params")
        assert extra and extra.get("repetition_penalty", 1) > 1
        texts = "\n".join(s[0] for s in sections)
        assert "c & d" in texts  # 重试恢复了完整表格
        assert "\\textup" not in texts

    def test_both_looped_salvages_prefix(self):
        parser = self._make_parser()
        looped1 = "\\begin{tabular}{cc}\na & b \\\\\nx & 1 & & " + LOOP
        looped2 = "\\begin{tabular}{cc}\n" + LOOP
        with patch.object(parser, "_call_vlm", side_effect=[looped1, looped2]):
            sections, _ = parser._extract_table_page(b"img", 1, 0)
        texts = "\n".join(s[0] for s in sections)
        assert "\\textup" not in texts
        assert "a & b" in texts  #  salvaged 前缀行保留

    def test_no_loop_no_retry(self):
        parser = self._make_parser()
        clean = "\\begin{tabular}{cc}\na & b \\\\\n\\end{tabular}"
        with patch.object(parser, "_call_vlm", return_value=clean) as m:
            sections, _ = parser._extract_table_page(b"img", 1, 0)
        assert m.call_count == 1
        assert len(sections) > 0

    def test_extra_params_merged_into_payload(self):
        parser = QwenVLParser(api_url="http://mock:8080/v1", model="m")
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"choices": [{"message": {"content": "ok"}}]}
        mock_resp.raise_for_status = MagicMock()
        with patch.object(qwen_vl_mod.requests, "post", return_value=mock_resp) as mock_post:
            parser._call_vlm(b"img", "prompt", extra_params={"repetition_penalty": 1.2})
        payload = mock_post.call_args.kwargs.get("json", {})
        assert payload["repetition_penalty"] == 1.2
        # 默认调用不带 repetition_penalty
        with patch.object(qwen_vl_mod.requests, "post", return_value=mock_resp) as mock_post2:
            parser._call_vlm(b"img", "prompt")
        payload2 = mock_post2.call_args.kwargs.get("json", {})
        assert "repetition_penalty" not in payload2


class TestDedupRepeatedBlocks:
    def test_detects_cycle(self):
        out, rep = _dedup_repeated_blocks(["a", "b", "c"] * 8)
        assert out == ["a", "b", "c"]
        assert rep == (3, 8, 24)

    def test_no_repetition(self):
        lines = [f"line{i}" for i in range(30)]
        out, rep = _dedup_repeated_blocks(lines)
        assert out == lines
        assert rep is None

    def test_short_input_untouched(self):
        lines = ["a", "b"] * 5  # 10 行 < 20 阈值
        out, rep = _dedup_repeated_blocks(lines)
        assert rep is None

    def test_tail_run_collapsed(self):
        """真实案例（page=9）：尾部同一行刷屏，非从头开始。"""
        head = [f"line{i}" for i in range(20)]
        out, rep = _dedup_repeated_blocks(head + ["病理诊断："] * 300)
        assert rep == (1, 300, 320)
        assert out == head + ["病理诊断："]

    def test_mid_run_collapsed(self):
        head = [f"line{i}" for i in range(10)]
        mid = ["x"] * 30
        tail = [f"tail{i}" for i in range(10)]
        out, rep = _dedup_repeated_blocks(head + mid + tail)
        assert rep == (1, 30, 50)
        assert out == head + ["x"] + tail

    def test_run_below_threshold_untouched(self):
        lines = [f"line{i}" for i in range(20)] + ["dup"] * 4
        out, rep = _dedup_repeated_blocks(lines)
        assert rep is None
        assert out == lines

    def test_low_uniqueness_ratio_collapsed(self):
        """小段交替重复：单 run < 5 但唯一率极低。"""
        lines = (["正常", "3.5"] * 5 + ["正常", "4.0"] * 5) * 15  # 300 行仅 3 唯一
        out, rep = _dedup_repeated_blocks(lines)
        assert rep is not None
        assert len(out) < len(lines)

    def test_form_header_double_block_keeps_tail(self):
        """真实案例（XJJA page=10）：双栏表单表头 姓名/性别/年龄 物理印两次，
        属真实内容而非幻觉。应仅折叠重复块，唯一尾部必须保留
        （旧版误判为 cycle=3 幻觉，45→3 行截断丢掉了主诉/现病史）。"""
        header = ["姓名：", "性别：女", "年龄：57岁"]
        tail = [f"content{i}" for i in range(39)]
        lines = header * 2 + tail
        out, rep = _dedup_repeated_blocks(lines)
        assert rep == (3, 15, 45)
        assert out == header + tail  # 42 行保留，尾部不丢

    def test_cycle_run_collapsed_tail_kept(self):
        """前缀块连续重复 N 次：折叠整个连续段，保留后续唯一尾部。"""
        block = ["a", "b", "c"]
        tail = [f"tail{i}" for i in range(10)]
        out, rep = _dedup_repeated_blocks(block * 5 + tail)
        assert rep == (3, 8, 25)  # repeats = n // cycle = 25 // 3
        assert out == block + tail


class TestTextRepetitionRetry:
    def _make_parser(self):
        return QwenVLParser(api_url="http://mock:8080/v1")

    def test_retry_recovers_full_text(self):
        parser = self._make_parser()
        repeated = json.dumps(["a", "b", "c"] * 8)  # 24 行, cycle=3
        clean = json.dumps(["l1", "l2", "l3", "l4", "l5"])
        with patch.object(parser, "_call_vlm", side_effect=[repeated, clean]) as m:
            sections, _ = parser._extract_text_page(b"img", 1, 0)
        assert m.call_count == 2
        extra = m.call_args_list[1].kwargs.get("extra_params")
        assert extra and extra.get("repetition_penalty", 1) > 1
        assert len(sections) == 5  # 重试恢复完整页

    def test_retry_also_repeated_keeps_truncated(self):
        parser = self._make_parser()
        repeated = json.dumps(["a", "b", "c"] * 8)
        with patch.object(parser, "_call_vlm", return_value=repeated) as m:
            sections, _ = parser._extract_text_page(b"img", 1, 0)
        assert m.call_count == 2
        assert len(sections) == 3  # 截断兕底
    
    def test_retry_shorter_than_collapsed_keeps_collapsed(self):
        """重试结果干净但比折叠版更短：保留折叠版，避免二次丢内容。"""
        parser = self._make_parser()
        header = ["姓名：", "性别：女", "年龄：57岁"]
        first = json.dumps(header * 2 + [f"line{i}" for i in range(39)])  # 折叠后 42 行
        shorter_clean = json.dumps(["l1", "l2", "l3", "l4", "l5"])
        with patch.object(parser, "_call_vlm", side_effect=[first, shorter_clean]) as m:
            sections, _ = parser._extract_text_page(b"img", 1, 0)
        assert m.call_count == 2
        assert len(sections) == 42  # 保留折叠版，不采纳更短的重试

    def test_no_repetition_single_call(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value='["x", "y"]') as m:
            sections, _ = parser._extract_text_page(b"img", 1, 0)
        assert m.call_count == 1
        assert len(sections) == 2


# ---------------------------------------------------------------------------
# 15. 表格行级刷屏防御（\multicolumn 单宏刷屏、同一行重复 N 次）
# ---------------------------------------------------------------------------

_RUN_ROW = r"\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} \\"
_RUN_LATEX = "\n".join(
    [
        r"\begin{tabular}{cccc}",
        r"\hline",
        r"\multicolumn{2}{c}{项目} & \multicolumn{2}{c}{结果} \\",
        r"\hline",
        r"A & 1 \\",
        r"B & 2 \\",
    ]
    + [_RUN_ROW] * 100
)


class TestDedupLatexRows:
    def test_collapses_identical_row_run(self):
        out, rep = _dedup_latex_rows(_RUN_LATEX)
        assert rep is not None
        preview, repeats = rep
        assert repeats == 100
        lines = [l for l in out.split("\n") if l.strip() == _RUN_ROW]
        assert len(lines) == 1  # 110 行折叠为 1 行

    def test_short_run_untouched(self):
        latex = "\n".join([r"A & 1 \\"] * 4)  # < 5 阈值，合法重复行不动
        out, rep = _dedup_latex_rows(latex)
        assert rep is None
        assert out == latex

    def test_no_repetition_untouched(self):
        out, rep = _dedup_latex_rows(r"\begin{tabular}{cc}" + "\n" + r"A & 1 \\" + "\n" + r"B & 2 \\")
        assert rep is None

    def test_structure_lines_not_treated_as_data(self):
        latex = "\n".join([r"\hline"] * 10)  # 无 & 的结构行不参与检测
        out, rep = _dedup_latex_rows(latex)
        assert rep is None


class TestTableRowRepetitionRetry:
    def _make_parser(self):
        return QwenVLParser(api_url="http://mock:8080/v1")

    def test_retry_recovers_clean_table(self):
        parser = self._make_parser()
        clean = "\n".join(
            [r"\begin{tabular}{cc}", r"\hline", r"A & 1 \\", r"B & 2 \\", r"C & 3 \\"]
        )
        with patch.object(parser, "_call_vlm", side_effect=[_RUN_LATEX, clean]) as m:
            sections, _ = parser._extract_table_page(b"img", 1, 0)
        assert m.call_count == 2
        extra = m.call_args_list[1].kwargs.get("extra_params")
        assert extra and extra.get("repetition_penalty", 1) > 1
        # 采用重试的干净表格，而非折叠版
        assert any("C & 3" in s[0] for s in sections)

    def test_retry_also_repeated_keeps_collapsed(self):
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value=_RUN_LATEX) as m:
            sections, _ = parser._extract_table_page(b"img", 1, 0)
        assert m.call_count == 2
        run_rows = [s for s in sections if s[0].strip() == _RUN_ROW]
        assert len(run_rows) == 1  # 兕底：折叠版保留 1 行

    def test_no_row_repetition_single_call(self):
        parser = self._make_parser()
        clean = "\n".join([r"\begin{tabular}{cc}", r"A & 1 \\", r"B & 2 \\"])
        with patch.object(parser, "_call_vlm", return_value=clean) as m:
            sections, _ = parser._extract_table_page(b"img", 1, 0)
        assert m.call_count == 1


# ================================================================
# 16. 空串刷屏防御（"" flood / 数组被 max_tokens 截断）
# ================================================================
# 真实案例（page=18，len=65498）：模型贪心循环刷 "" 空元素烧穿
# token 预算，数组未闭合 → _parse_json_array 全部兜底失败 →
# 旧代码直接 "returned no lines" 放弃，从未触发 repetition_penalty
# 重试。指纹与响应大小无关：小响应的空串刷屏同样是故障。

_FLOOD_CLEAN = json.dumps([f"line{i}" for i in range(10)])
_FLOOD_DIRTY = json.dumps(["病历文书", "医嘱"] + [""] * 200)  # 闭合但空串刷屏
_TRUNCATED = '["病历文书", "医嘱", ' + ", ".join(['""'] * 300)  # 无闭合 ]


class TestEmptyFloodHelpers:
    def test_flood_detected_by_empty_elements(self):
        assert _is_empty_flood(_FLOOD_DIRTY) is True

    def test_small_flood_detected(self):
        """~100 字节的小响应照样触发——指纹不依赖响应大小。"""
        assert _is_empty_flood(json.dumps([""] * 20)) is True

    def test_below_threshold_not_flood(self):
        """少量空串（<20）保持容忍，不误伤。"""
        assert _is_empty_flood(json.dumps(["a", "b"] + [""] * 19)) is False

    def test_interspersed_empty_cells_not_flood(self):
        """真实误报反例（page=18 医嘱表）：每行带 3 个空单元格（单价/备注），
        空串被内容隔开、总数 75 个，属合法表格而非刷屏。"""
        rows = []
        for i in range(25):
            rows += [f"2026/1/{i + 1}", f"医嘱内容{i}", "停用", "", "", ""]
        assert _is_empty_flood(json.dumps(rows)) is False

    def test_clean_array_not_flood(self):
        assert _is_empty_flood(_FLOOD_CLEAN) is False

    def test_none_not_flood(self):
        assert _is_empty_flood(None) is False

    def test_truncated_array_detected(self):
        assert _is_truncated_array(_TRUNCATED) is True

    def test_closed_array_not_truncated(self):
        assert _is_truncated_array('["a", "b"]') is False

    def test_empty_page_not_truncated(self):
        """真·空页 '[]' 完整闭合，不是截断。"""
        assert _is_truncated_array("[]") is False

    def test_fence_wrapped_truncated(self):
        assert _is_truncated_array('```json\n["a", "b"\n') is True

    def test_none_not_truncated(self):
        assert _is_truncated_array(None) is False


class TestTextEmptyFloodRetry:
    def _make_parser(self):
        return QwenVLParser(api_url="http://mock:8080/v1")

    def test_truncated_array_retries_with_penalty(self):
        """真实案例形态：未闭合空串数组，解析失败 → 带惩罚因子重试。"""
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", side_effect=[_TRUNCATED, _FLOOD_CLEAN]) as m:
            sections, _ = parser._extract_text_page(b"img", 18, 0)
        assert m.call_count == 2
        extra = m.call_args_list[1].kwargs.get("extra_params")
        assert extra and extra.get("repetition_penalty", 1) > 1
        assert len(sections) == 10  # 采纳重试的干净结果

    def test_small_closed_flood_retries(self):
        """闭合数组但空串刷屏：响应再小也触发重试。"""
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", side_effect=[_FLOOD_DIRTY, _FLOOD_CLEAN]) as m:
            sections, _ = parser._extract_text_page(b"img", 18, 0)
        assert m.call_count == 2
        extra = m.call_args_list[1].kwargs.get("extra_params")
        assert extra and extra.get("repetition_penalty", 1) > 1
        assert len(sections) == 10

    def test_retry_also_flooded_keeps_salvage(self):
        """重试仍刷屏：只重试一次不无限循环，保留原解析的可用前缀。"""
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value=_TRUNCATED) as m:
            sections, _ = parser._extract_text_page(b"img", 18, 0)
        assert m.call_count == 2
        # json_repair 兜底从未闭合数组里救回前缀真实内容
        assert [s[0] for s in sections] == ["病历文书", "医嘱"]

    def test_empty_page_no_retry(self):
        """真·空页：'[]' 不命中任何指纹，单次调用。"""
        parser = self._make_parser()
        with patch.object(parser, "_call_vlm", return_value="[]") as m:
            sections, _ = parser._extract_text_page(b"img", 18, 0)
        assert m.call_count == 1
        assert sections == []

    def test_interspersed_empty_cells_single_call(self):
        """医嘱表每行 3 个空单元格：不触发重试，原样采纳。"""
        parser = self._make_parser()
        rows = []
        for i in range(25):
            rows += [f"2026/1/{i + 1}", f"医嘱内容{i}", "停用", "", "", ""]
        with patch.object(parser, "_call_vlm", return_value=json.dumps(rows)) as m:
            sections, _ = parser._extract_text_page(b"img", 18, 0)
        assert m.call_count == 1
        assert len(sections) == 75  # 25 行 × 3 非空单元格，空串被过滤
