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
import logging
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
_common_mod = _fake_pkg("common", os.path.join(project_root, "common"))
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
from rag.flow.extractor.qwen_vl_ocr import _split_text_pages, _detex  # noqa: E402


# ================================================================
# 0. _detex — LaTeX 转义归一化（含数学模式比较值 $<14$）
# ================================================================

class TestDetex:
    def test_math_wrapped_comparison_value(self):
        # LBZH 实证：LaTeX 表格参考范围输出为 $<14$（整个值包在数学模式）
        assert _detex("$<14$") == "<14"
        assert _detex("$>100$") == ">100"

    def test_bare_comparison_operator(self):
        assert _detex("$<$14") == "<14"

    def test_greek_letter_symbol(self):
        assert _detex("$\\mu$mol/L") == "μmol/L"

    def test_plain_text_untouched(self):
        assert _detex("肌钙蛋白T") == "肌钙蛋白T"


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


class _FakeExt2(_FakeExt):
    """pn=0 页额外提取肌酐：用于验证同页多 item 的索引顺序对应。"""

    async def _generate_async(self, msg):
        user = next(m["content"] for m in msg if m.get("role") == "user")
        items = []
        if "ALB" in user:
            items.append({"name": "白蛋白", "item_code": "ALB", "value": "38.4",
                          "unit": "g/L", "reference_range": "40-55", "abnormal": True})
            items.append({"name": "肌酐", "item_code": None, "value": "62",
                          "unit": None, "reference_range": None, "abnormal": False})
        if "TnT & 5" in user:
            items.append({"name": "肌钙蛋白T", "item_code": "TnT", "value": "5",
                          "unit": "ng/L", "reference_range": "<14", "abnormal": False})
        if "WBC" in user:
            items.append({"name": "*白细胞计数", "item_code": "WBC", "value": "6.18",
                          "unit": None, "reference_range": "3.5-9.5", "abnormal": False})
        return json.dumps({"report_date": None, "items": items}, ensure_ascii=False)


class TestProcessTableIndexMapping:
    """Step C 坐标映射：coord 返回与输入 names 顺序一致时按索引直取 bbox。

    YXLA p3 回归：coord text 带括号缩写（"白细胞(WDC)"）与 LLM name
    （"白细胞"）文本不同，旧实现的 LCS 分数被长 key 稀释到 0.3-0.46
    （阈值 0.5），导致 5/24 匹配失败填 [0,0,0,0,0]、另有 6 处错配。
    数量一致时必须按索引直取，不再做文本匹配。
    """

    def _run(self, monkeypatch, fake_coord, ext=None):
        monkeypatch.setattr(qvl, "resolve_vl_ocr_endpoint",
                            lambda tenant, llm: ("http://fake/v1", "fake-model", "key"))
        monkeypatch.setattr(qvl, "_call_qwen30b_coord", fake_coord)
        ck = {"doc_id": "doc-x", "text": _make_chunk_text(), "positions": _make_positions()}
        asyncio.run(qvl.process_table(ext or _FakeExt(), ck, "fake-llm"))
        return ck

    def test_counts_match_index_mapping_ignores_text_diff(self, monkeypatch):
        """数量一致时按索引直取：coord text 与 name 不同也必须成功，
        坐标 = bbox × (page_w/1000, page_h/1000)，按输入顺序一一对应。"""

        def fake_coord(img_bytes, prompt, tag, endpoint_cfg, page_num=0):
            seg = prompt.split("## 需要定位的检验项目名称\n", 1)[1].split("\n\n", 1)[0]
            names = seg.split("、")
            # 返回顺序与输入一致，但 text 带括号缩写（线上 coord 模型行为）
            return (
                [{"text": f"{n}(X)", "bbox": [10 + 50 * i, 10, 100 + 50 * i, 20]}
                 for i, n in enumerate(names)],
                0.1, "ok",
            )

        ck = self._run(monkeypatch, fake_coord, ext=_FakeExt2())
        rows = ck["row_positions"]
        assert len(rows) == 4
        # 索引直取：4 行全部拿到真实坐标，无 [0,0,0,0,0] 占位
        for rp in rows:
            assert rp[0] != 0, f"按索引直取应全部成功，实际出现全 0: {rows}"
        # 同组内按输入顺序一一对应：白蛋白 i=0，肌酐 i=1
        # 坐标 = bbox × (595/1000, 842/1000)
        assert rows[0][1] == pytest.approx(10 * 595 / 1000.0)    # 白蛋白 left
        assert rows[1][1] == pytest.approx(60 * 595 / 1000.0)    # 肌酐 left（第 2 个 name）
        assert rows[0][3] == pytest.approx(10 * 842 / 1000.0)    # top

    def test_count_mismatch_warns_and_looks_up_by_name(self, monkeypatch, caplog):
        """数量不一致（模型漏检）→ warning + 按名字匹配兜底。"""

        def fake_coord(img_bytes, prompt, tag, endpoint_cfg, page_num=0):
            seg = prompt.split("## 需要定位的检验项目名称\n", 1)[1].split("\n\n", 1)[0]
            names = seg.split("、")
            # 模拟模型漏检：每组只返回第一个 name 的 bbox
            return [{"text": names[0], "bbox": [10, 10, 100, 20]}], 0.1, "ok"

        with caplog.at_level(logging.WARNING):
            ck = self._run(monkeypatch, fake_coord, ext=_FakeExt2())

        # 长度不一致时必须记录 warning
        assert any("coord count mismatch" in r.message for r in caplog.records), \
            [r.message for r in caplog.records]
        # 名字兜底：白蛋白精确命中（非 0），肌酐查不到 → 占位 0
        rows = ck["row_positions"]
        assert len(rows) == 4
        assert rows[0][0] != 0, f"白蛋白按名字匹配应成功: {rows}"
        assert rows[1][0] == 0, f"肌酐查不到应填 0: {rows}"


class TestProcessTextCountMismatchWarning:
    """process_text Step 4：coord 返回数量与文本行数不一致时必须打 warning
    （与 process_table 的索引直取/名字兜底模式对齐）。"""

    def test_count_mismatch_logs_warning(self, monkeypatch, caplog):
        def fake_coord(img_bytes, prompt, tag, endpoint_cfg, page_num=0):
            # 模拟模型漏检：3 行只返回 1 个 bbox（名字互不相同，避免 fuzzy 命中）
            return [{"text": "alpha", "bbox": [10, 10, 100, 20]}], 0.1, "ok"

        monkeypatch.setattr(qvl, "resolve_vl_ocr_endpoint",
                            lambda tenant, llm: ("http://fake/v1", "fake-model", "key"))
        monkeypatch.setattr(qvl, "_call_qwen30b_coord", fake_coord)

        ck = {
            "doc_id": "doc-x",
            "text": "alpha\nbeta\ngamma",
            "positions": [[0, 0, 0, 0, 0]] * 3,
            "classify_result_tks": json.dumps({"type": "progress_note"}),
        }
        with caplog.at_level(logging.WARNING):
            asyncio.run(qvl.process_text(_FakeExt(), ck, "fake-llm"))

        # 数量不一致必须记录 warning
        assert any("coord count mismatch" in r.message for r in caplog.records), \
            [r.message for r in caplog.records]
        # 前 1 行按索引成功（非 0），多余行名字兜底失败 → 占位 0
        rows = ck["positions"]
        assert len(rows) == 3
        assert rows[0][0] == 0 and rows[0][1] != 0, f"首行应按索引成功: {rows}"
        assert rows[1] == [0, 0, 0, 0, 0], f"多余行应占位 0: {rows}"
        assert rows[2] == [0, 0, 0, 0, 0], f"多余行应占位 0: {rows}"


class TestBuildLogTag:
    """日志 TAG 归因：多 executor 共享同一进程日志流，coord 调用日志必须带
    doc/task/case 标识，否则超时无法归属（LBZH page 21/23 误归因教训）。"""

    DOC_ID = "dbef275894d711f1bd9827cf206dfa2d"
    TASK_ID = "c3fe5538998211f18e23b137b0b8cefc"
    CASE_NAME = "LBZH，男，63岁，胃癌一线(1).pdf"

    def _ext_with_canvas(self):
        return types.SimpleNamespace(_canvas=types.SimpleNamespace(
            _doc_id=self.DOC_ID, task_id=self.TASK_ID, _doc_name=self.CASE_NAME))

    def test_tag_contains_doc_task_case(self):
        tag = qvl._build_log_tag(self._ext_with_canvas(), "[qwen-vl-text]")
        assert tag.startswith("[qwen-vl-text]")
        assert "doc=dbef2758" in tag      # 截前 8 位
        assert "task=c3fe5538" in tag
        assert f"case={self.CASE_NAME}" in tag

    def test_missing_canvas_attrs_degrade_to_dash(self):
        ext = types.SimpleNamespace()  # 无 _canvas
        tag = qvl._build_log_tag(ext, "[qwen-vl-table]")
        assert tag.startswith("[qwen-vl-table]")
        assert "doc=-" in tag
        assert "task=-" in tag
        assert "case=" not in tag

    def test_process_text_passes_attribution_tag_to_coord(self, monkeypatch):
        """process_text 传给 coord 的 tag 必须携带 doc/task/case 归因信息。"""
        captured = {}

        def fake_coord(img_bytes, prompt, tag, endpoint_cfg, page_num=0):
            captured["tag"] = tag
            return [{"text": "alpha", "bbox": [10, 10, 100, 20]}], 0.1, "ok"

        monkeypatch.setattr(qvl, "resolve_vl_ocr_endpoint",
                            lambda tenant, llm: ("http://fake/v1", "fake-model", "key"))
        monkeypatch.setattr(qvl, "_call_qwen30b_coord", fake_coord)

        ext = _FakeExt()
        ext._canvas = types.SimpleNamespace(
            get_tenant_id=lambda: "tenant-x",
            _doc_id=self.DOC_ID,
            task_id=self.TASK_ID,
            _doc_name=self.CASE_NAME,
        )
        ext._sys_prompt_and_msg = lambda history, args: (
            [{"role": "user", "content": args.get("text", "")}], "SYS")
        async def _gen(msg):
            return json.dumps({"report_date": None, "items": []}, ensure_ascii=False)
        ext._generate_async = _gen

        ck = {
            "doc_id": "doc-x",
            "text": "alpha",
            "positions": [[0, 0, 0, 0, 0]],
            "classify_result_tks": json.dumps({"type": "progress_note"}),
        }
        asyncio.run(qvl.process_text(ext, ck, "fake-llm"))

        tag = captured.get("tag", "")
        assert "doc=dbef2758" in tag, f"coord tag 缺 doc 归因: {tag}"
        assert "task=c3fe5538" in tag, f"coord tag 缺 task 归因: {tag}"
        assert f"case={self.CASE_NAME}" in tag, f"coord tag 缺 case 归因: {tag}"


class TestCoordLogDedup:
    """日志理清：coord raw response 全文已包含全部 items 的 text/bbox，
    逐条 coord item[i] 日志与之完全重复；汇总行（raw/valid 计数）保留。
    不截断任何全文，仅去重复。"""

    def test_coord_items_not_logged_per_item(self, monkeypatch, caplog):
        fake_resp = types.SimpleNamespace(status_code=200)
        fake_resp.json = lambda: {"choices": [{"message": {"content": json.dumps([
            {"text": "白蛋白", "bbox": [10, 10, 100, 20]},
            {"text": "肌酥", "bbox": [10, 30, 100, 40]},
        ])}}]}
        monkeypatch.setattr(qvl.requests, "post", lambda *a, **k: fake_resp)

        with caplog.at_level(logging.INFO):
            items, _elapsed, status = qvl._call_qwen30b_coord(
                b"img", "prompt", "[qwen-vl-table]", ("http://fake/v1", "m", "key"))

        assert status == "ok" and len(items) == 2
        msgs = [r.getMessage() for r in caplog.records]
        assert any("raw_items=2" in m and "valid_items=2" in m for m in msgs), \
            f"coord 汇总行应保留: {msgs}"
        assert not any("coord item[" in m for m in msgs), \
            "逐条 item 日志与 raw response 全文重复"


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
