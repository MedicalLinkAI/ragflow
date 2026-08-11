#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Tests for rag/flow/extractor/qwen_vl_ocr.py (process_table / LabReport 路径)
#
#  回归背景（LBZH，男，63岁，胃癌一线(1).pdf，chunk c8735e1c）：
#    - 第 4 页（pn=3）唯一数据行"肌钙蛋白T/TnT/5"被 Step C 子串回退归属到
#      第 1 页（"肌钙蛋白T"在 HIS 表格左栏每页重复出现，取文档序首个命中）
#    - 导致 coord grouping 缺 pn=3，第 4 页从未做坐标定位
#    - 且 page_text_map 按行数均分（不用 positions），Step B 各页输入跨页
#
import asyncio
import json
import os
import sys
import types

import pytest

# ── Bootstrap: fake heavy packages before importing module under test ──
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


# rag / rag.flow / rag.flow.extractor: fake packages with real __path__
# (avoids rag/flow/__init__.py's walk-import of every submodule)
_fake_pkg("rag", os.path.join(project_root, "rag"))
_fake_pkg("rag.flow", os.path.join(project_root, "rag", "flow"))
_fake_pkg("rag.flow.extractor", os.path.join(project_root, "rag", "flow", "extractor"))

# rag.flow.extractor.extractor — heavy module; only strip_markdown_json_fence needed
_extractor_stub = types.ModuleType("rag.flow.extractor.extractor")
_extractor_stub.strip_markdown_json_fence = lambda s: s
sys.modules["rag.flow.extractor.extractor"] = _extractor_stub

# api.db.services.file2document_service
for _n in ("api", "api.db", "api.db.services"):
    _fake_pkg(_n)
_fds_mod = types.ModuleType("api.db.services.file2document_service")


class _File2DocumentService:
    @staticmethod
    def get_storage_address(doc_id=None):
        return "bucket", "name"


_fds_mod.File2DocumentService = _File2DocumentService
sys.modules["api.db.services.file2document_service"] = _fds_mod

# common.settings with STORAGE_IMPL
_common_mod = _fake_pkg("common")
_settings_mod = types.ModuleType("common.settings")


class _Storage:
    @staticmethod
    def get(b, n):
        return b"%PDF-FAKE"


_settings_mod.STORAGE_IMPL = _Storage
sys.modules["common.settings"] = _settings_mod
_common_mod.settings = _settings_mod


# fitz fake: renders any page as a fixed-size pixmap
class _FakePixmap:
    width = 1000
    height = 1400

    def tobytes(self, fmt):
        return b"PNGDATA"


class _FakeRect:
    width = 595.0
    height = 842.0


class _FakePage:
    rect = _FakeRect()

    def get_pixmap(self, matrix):
        return _FakePixmap()


class _FakeDoc:
    def __init__(self, n=20):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        return _FakePage()

    def close(self):
        pass


_fitz_mod = types.ModuleType("fitz")
_fitz_mod.open = lambda stream=None, filetype=None: _FakeDoc()
_fitz_mod.Matrix = lambda a, b: None
sys.modules["fitz"] = _fitz_mod

# ── Import module under test ──────────────────────────────────────────
import rag.flow.extractor.qwen_vl_ocr as qvl  # noqa: E402
from rag.flow.extractor.qwen_vl_ocr import _split_text_pages  # noqa: E402


# ================================================================
# 1. _split_text_pages — 方案 A：按 positions 页码分页（非行数均分）
# ================================================================

class TestSplitTextPages:
    def test_uneven_pages_follow_positions_not_even_split(self):
        # 各页行数 5/2/2（均分会切成 3/3/3）——必须按 positions 分页
        lines = [f"line{i}" for i in range(9)]
        positions = (
            [[0, 0, 0, 0, 0]] * 5
            + [[1, 0, 0, 0, 0]] * 2
            + [[2, 0, 0, 0, 0]] * 2
        )
        result = _split_text_pages("\n".join(lines), positions, [0, 1, 2])
        assert len(result[0].split("\n")) == 5
        assert len(result[1].split("\n")) == 2
        assert len(result[2].split("\n")) == 2
        assert result[0].split("\n")[0] == "line0"
        assert result[1].split("\n")[0] == "line5"
        assert result[2].split("\n")[0] == "line7"

    def test_single_page_returns_whole_text(self):
        text = "a\nb\nc"
        result = _split_text_pages(text, [[0, 0, 0, 0, 0]] * 3, [0])
        assert result == {0: text}

    def test_extra_lines_fall_back_to_last_position_page(self):
        # 行数 > positions 数：超出的行归属最后一个 position 的页码
        lines = ["l0", "l1", "l2", "l3"]
        positions = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        result = _split_text_pages("\n".join(lines), positions, [0, 1])
        assert result[0] == "l0"
        assert result[1] == "l1\nl2\nl3"

    def test_empty_positions_falls_back_to_first_page(self):
        result = _split_text_pages("a\nb", [], [3, 4])
        assert result == {3: "a\nb"}


# ================================================================
# 2. process_table 回归 — 方案 B：item 归属提取来源页
# ================================================================

def _make_positions():
    # 17 行：pn0×10, pn1×1, pn2×1, pn3×2(含数据行), pn4×3
    # 行数均分（17//5=3）会把 pn3 的数据行切进 pn4 的片段
    pns = [0] * 10 + [1] + [2] + [3] * 2 + [4] * 3
    return [[pn, 0.0, 0.0, 0.0, 0.0] for pn in pns]


def _make_chunk_text():
    lines = [
        "\\begin{tabular}{ccccc}",                    # L0  pn0
        "肌钙蛋白T & G002 & 血清 & & \\\\",            # L1  pn0 左栏出现
        "白蛋白 & ALB & 38.4 & 40-55 & g/L \\\\",      # L2  pn0 数据行
        "共6份报告",                                    # L3  pn0
        "GGT & 50",                                    # L4  pn0
        "ALP & 93",                                    # L5  pn0
        "LDH & 208",                                   # L6  pn0
        "尿素 & 3.12",                                 # L7  pn0
        "肌酐 & 62",                                   # L8  pn0
        "\\end{tabular}",                              # L9  pn0
        "\\begin{tabular}{ccccc}",                     # L10 pn1
        "\\end{tabular}",                              # L11 pn2
        "肌钙蛋白T & TnT & 5 & $<14$ & ng/L \\\\",     # L12 pn3 数据行（第4页）
        "\\end{tabular}",                              # L13 pn3
        "\\begin{tabular}{ccccc}",                     # L14 pn4
        "*白细胞计数 & WBC & 6.18",                    # L15 pn4
        "\\end{tabular}",                              # L16 pn4
    ]
    return "\n".join(lines)


class _FakeExt:
    """Stub extractor component: Step B LLM simulated from user content."""

    def __init__(self):
        self._canvas = types.SimpleNamespace(
            get_tenant_id=lambda: "tenant-x", _doc_id="doc-x"
        )
        self._param = types.SimpleNamespace(field_name="lab_result")

    def get_input_elements(self):
        return {"text": {"value": []}}

    def _sys_prompt_and_msg(self, history, args):
        return [{"role": "user", "content": args["text"]}], "SYS"

    async def _generate_async(self, msg):
        user = next(m["content"] for m in msg if m.get("role") == "user")
        items = []
        if "TnT & 5" in user:
            items.append({"name": "肌钙蛋白T", "item_code": "TnT", "value": "5",
                          "unit": "ng/L", "reference_range": "<14", "abnormal": False})
        if "ALB" in user:
            items.append({"name": "白蛋白", "item_code": "ALB", "value": "38.4",
                          "unit": "g/L", "reference_range": "40-55", "abnormal": True})
        if "WBC" in user:
            items.append({"name": "*白细胞计数", "item_code": "WBC", "value": "6.18",
                          "unit": None, "reference_range": "3.5-9.5", "abnormal": False})
        return json.dumps({"report_date": None, "items": items}, ensure_ascii=False)


def _run_process_table(monkeypatch, coord_calls):
    monkeypatch.setattr(qvl, "resolve_vl_ocr_endpoint",
                        lambda tenant, llm: ("http://fake/v1", "fake-model", "key"))

    def fake_coord(img_bytes, prompt, tag, endpoint_cfg, page_num=0):
        seg = prompt.split("## 需要定位的检验项目名称\n", 1)[1].split("\n\n", 1)[0]
        names = seg.split("、")
        coord_calls.append((page_num, names))
        return [{"text": n, "bbox": [10, 10, 100, 20]} for n in names], 0.1, "ok"

    monkeypatch.setattr(qvl, "_call_qwen30b_coord", fake_coord)

    ck = {
        "doc_id": "doc-x",
        "text": _make_chunk_text(),
        "positions": _make_positions(),
    }
    asyncio.run(qvl.process_table(_FakeExt(), ck, "fake-llm"))
    return ck


class TestProcessTablePageAttribution:
    def test_page4_item_attributed_to_extraction_page(self, monkeypatch):
        """LBZH 回归：第 4 页数据行 item 必须归属 pn=3 并在第 4 页做坐标定位。"""
        coord_calls = []
        ck = _run_process_table(monkeypatch, coord_calls)
        # 关键断言 1：coord 定位对 pn=3（第 4 页）发生过调用
        pages_called = [pn for pn, _ in coord_calls]
        assert 3 in pages_called, f"第 4 页(pn=3)未做坐标定位, calls={coord_calls}"
        # 关键断言 2：pn=3 的调用携带肌钙蛋白T
        names_p3 = next(names for pn, names in coord_calls if pn == 3)
        assert "肌钙蛋白T" in names_p3
        # 行坐标页码 = pn+1：应包含第 4 页（肌钙蛋白T）、第 1 页（白蛋白）、第 5 页（WBC）
        pages_in_rows = sorted(rp[0] for rp in ck["row_positions"])
        assert pages_in_rows == [1, 4, 5], f"row_positions 页码错误: {ck['row_positions']}"

    def test_page1_item_keeps_its_own_page(self, monkeypatch):
        """白蛋白（第 1 页数据行）不被误挂到其他页。"""
        coord_calls = []
        _run_process_table(monkeypatch, coord_calls)
        names_p0 = next((names for pn, names in coord_calls if pn == 0), [])
        assert "白蛋白" in names_p0
