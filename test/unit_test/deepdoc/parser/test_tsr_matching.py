"""
TSR (Table Structure Recognition) 行匹配逻辑单元测试。

测试边界:
  - Mock 掉: 用户上传 → paddleocr-vl 服务调用 → result JSON (写死真实数据)
  - Mock 掉: page_images 生成 (用采集的真实页面 PNG)
  - 真实执行: _transfer_to_tables(result) 的全部逻辑
    包括 Level-1(det_boxes) → Level-2(TSR 模型推理 + 匹配) → Level-3(Uniform)

测试用例来源:
  - DSXI 肺癌 山东中心: pages 8, 10, 11 (回归案例)
  - 天津-PGFE-乳腺癌-方穹推荐: pages 6, 7, 9 (正向案例)

fixture 数据采集方式:
  export TSR_FIXTURE_DIR=/tmp/tsr_fixtures
  然后上传对应 PDF，从 /tmp/tsr_fixtures/ 获取 result.json + page_images/

Usage:
  cd /path/to/ragflow
  python -m pytest test/unit_test/deepdoc/parser/test_tsr_matching.py -v
"""

import json
import logging
import os
import sys
from pathlib import Path
from typing import Any
from unittest.mock import patch, PropertyMock

import pytest

# ── 项目路径设置 ──
RAGFLOW_ROOT = Path(__file__).resolve().parents[4]  # ragflow/
sys.path.insert(0, str(RAGFLOW_ROOT))

# ── Fixture 数据目录 ──
FIXTURE_DIR = Path(__file__).parent / "fixtures" / "tsr_matching"

logging.basicConfig(level=logging.INFO, format="%(message)s")


# ──────────────────────────────────────────────────────────────────
# Fixture 加载工具
# ──────────────────────────────────────────────────────────────────

def _load_vl_result(case_name: str) -> dict[str, Any]:
    """加载 paddleocr-vl 响应 JSON (写死的真实数据)。"""
    p = FIXTURE_DIR / case_name / "vl_response" / "result.json"
    if not p.exists():
        pytest.skip(f"Fixture not found: {p}  — run fixture capture first")
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def _load_page_images(case_name: str):
    """加载真实页面 PNG 图片，返回 PIL.Image 列表。"""
    from PIL import Image
    img_dir = FIXTURE_DIR / case_name / "page_images"
    if not img_dir.exists():
        pytest.skip(f"Page images not found: {img_dir}  — run fixture capture first")
    images = []
    idx = 0
    while True:
        p = img_dir / f"page_{idx}.png"
        if not p.exists():
            break
        images.append(Image.open(p))
        idx += 1
    if not images:
        pytest.skip(f"No page images in {img_dir}")
    return images


# ──────────────────────────────────────────────────────────────────
# Parser 实例化工具 (绕过 VL 服务调用)
# ──────────────────────────────────────────────────────────────────

def _make_parser_with_images(page_images):
    """
    创建 PaddleOCRParser 实例，注入 page_images，
    绕过 __init__ 中的 API URL 检查和文件上传流程。
    """
    from deepdoc.parser.paddleocr_parser import PaddleOCRParser

    # 使用一个 dummy URL 避免 __init__ 报错
    parser = PaddleOCRParser.__new__(PaddleOCRParser)
    # 手动设置必要属性
    parser.page_images = page_images
    parser.logger = logging.getLogger("test_tsr")
    return parser


# ──────────────────────────────────────────────────────────────────
# 通用验证工具
# ──────────────────────────────────────────────────────────────────

def _extract_table_by_page(tables: list[dict], page_1based: int) -> list[dict]:
    """从 _transfer_to_tables 输出中提取指定页的所有表格。"""
    return [t for t in tables if t["page"] == page_1based]


def _validate_row_count(table: dict, expected_rows: int, tolerance: int = 0):
    """验证表格行数是否符合预期。"""
    actual = len(table["row_positions"])
    assert abs(actual - expected_rows) <= tolerance, (
        f"page={table['page']} expected {expected_rows}±{tolerance} rows, "
        f"got {actual}. row[0]={table['row_positions'][0]}, "
        f"row[-1]={table['row_positions'][-1]}"
    )


def _validate_no_overlap(table: dict, max_overlap_px: int = 5):
    """验证行之间没有严重重叠（top/bottom 坐标不应大幅交叉）。"""
    rows = table["row_positions"]
    for i in range(len(rows) - 1):
        # row format: [page, x0, x1, top, bottom]
        cur_bottom = rows[i][4]
        next_top = rows[i + 1][3]
        overlap = cur_bottom - next_top
        assert overlap <= max_overlap_px, (
            f"page={table['page']} row[{i}] bottom={cur_bottom} overlaps "
            f"row[{i+1}] top={next_top} by {overlap}px (max={max_overlap_px})"
        )


def _validate_coverage(table: dict, min_coverage: float = 0.8):
    """验证行坐标是否覆盖了表格 bbox 的大部分高度。"""
    rows = table["row_positions"]
    if not rows:
        return
    # bbox 是原始坐标, row_positions 已除以 zm
    # 这里只检查 row 自身的覆盖率
    rows_top = rows[0][3]
    rows_bottom = rows[-1][4]
    rows_span = rows_bottom - rows_top
    # 每行平均高度
    total_height = sum(r[4] - r[3] for r in rows)
    # 行间 gap 不应太大
    gap_total = rows_span - total_height
    gap_ratio = gap_total / rows_span if rows_span > 0 else 0
    assert gap_ratio < (1 - min_coverage), (
        f"page={table['page']} gap_ratio={gap_ratio:.2%} > "
        f"{1 - min_coverage:.0%} — 行之间存在过大间隙"
    )


def _validate_monotonic(table: dict):
    """验证行坐标是单调递增的 (top[i] < top[i+1])。"""
    rows = table["row_positions"]
    for i in range(len(rows) - 1):
        assert rows[i][3] < rows[i + 1][3], (
            f"page={table['page']} row[{i}].top={rows[i][3]} >= "
            f"row[{i+1}].top={rows[i+1][3]} — 行顺序不单调"
        )


def _validate_min_row_height(table: dict, min_height_px: int = 5):
    """验证每行至少有最小高度（排除异常窄行）。"""
    rows = table["row_positions"]
    for i, r in enumerate(rows):
        h = r[4] - r[3]
        assert h >= min_height_px, (
            f"page={table['page']} row[{i}] height={h}px < {min_height_px}px "
            f"— 行过窄，可能是坐标映射错误"
        )


# ──────────────────────────────────────────────────────────────────
# Test Cases: DSXI 肺癌 山东中心
# ──────────────────────────────────────────────────────────────────

class TestDSXI:
    """DSXI 肺癌 山东中心 — 回归测试用例。

    验证 TSR 修改不会破坏已知正确的场景。
    """

    CASE = "dsxi"

    @pytest.fixture(scope="class")
    def tables(self):
        """一次性解析 DSXI 的所有表格，供各 test 方法复用。"""
        result = _load_vl_result(self.CASE)
        page_images = _load_page_images(self.CASE)
        parser = _make_parser_with_images(page_images)
        tables = parser._transfer_to_tables(result)
        logging.info(
            "[DSXI] _transfer_to_tables returned %d tables: pages=%s",
            len(tables), [t["page"] for t in tables],
        )
        return tables

    # ── Page 8: 血液检查表格 (35行, 关键: C反应蛋白 定位准确) ──

    def test_p8_row_count(self, tables):
        """p8 表格应有 ~35 行 (num_rows from <tr> count)。"""
        p8_tables = _extract_table_by_page(tables, 8)
        assert len(p8_tables) >= 1, "DSXI page 8 should have at least 1 table"
        # 主表格 (bbox 最大的那个)
        main = max(p8_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_row_count(main, expected_rows=35, tolerance=2)

    def test_p8_monotonic(self, tables):
        p8_tables = _extract_table_by_page(tables, 8)
        main = max(p8_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_monotonic(main)

    def test_p8_no_overlap(self, tables):
        p8_tables = _extract_table_by_page(tables, 8)
        main = max(p8_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_no_overlap(main)

    def test_p8_min_row_height(self, tables):
        """p8 每行不应小于 5px (排除 letterbox 映射产生的窄行 bug)。"""
        p8_tables = _extract_table_by_page(tables, 8)
        main = max(p8_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_min_row_height(main, min_height_px=5)

    # ── Page 10: 检验报告表格 (12行) ──

    def test_p10_row_count(self, tables):
        p10_tables = _extract_table_by_page(tables, 10)
        assert len(p10_tables) >= 1, "DSXI page 10 should have at least 1 table"
        main = max(p10_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_row_count(main, expected_rows=12, tolerance=1)

    def test_p10_monotonic(self, tables):
        p10_tables = _extract_table_by_page(tables, 10)
        main = max(p10_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_monotonic(main)

    def test_p10_no_overlap(self, tables):
        p10_tables = _extract_table_by_page(tables, 10)
        main = max(p10_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_no_overlap(main)

    def test_p10_min_row_height(self, tables):
        p10_tables = _extract_table_by_page(tables, 10)
        main = max(p10_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_min_row_height(main, min_height_px=5)

    # ── Page 11: 检验报告表格 (14行) ──

    def test_p11_row_count(self, tables):
        p11_tables = _extract_table_by_page(tables, 11)
        assert len(p11_tables) >= 1, "DSXI page 11 should have at least 1 table"
        main = max(p11_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_row_count(main, expected_rows=14, tolerance=1)

    def test_p11_monotonic(self, tables):
        p11_tables = _extract_table_by_page(tables, 11)
        main = max(p11_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_monotonic(main)

    def test_p11_no_overlap(self, tables):
        p11_tables = _extract_table_by_page(tables, 11)
        main = max(p11_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_no_overlap(main)

    def test_p11_min_row_height(self, tables):
        p11_tables = _extract_table_by_page(tables, 11)
        main = max(p11_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_min_row_height(main, min_height_px=5)

    # ── Page 9: 表头优化案例 (之前小于中位数方案优化过，不应被破坏) ──

    def test_p9_exists(self, tables):
        """p9 应有表格存在。"""
        p9_tables = _extract_table_by_page(tables, 9)
        assert len(p9_tables) >= 1, "DSXI page 9 should have at least 1 table"

    def test_p9_monotonic(self, tables):
        p9_tables = _extract_table_by_page(tables, 9)
        main = max(p9_tables, key=lambda t: (t["bbox"][2] - t["bbox"][0]) * (t["bbox"][3] - t["bbox"][1]))
        _validate_monotonic(main)


# ──────────────────────────────────────────────────────────────────
# Test Cases: 天津-PGFE-乳腺癌-方穹推荐
# ──────────────────────────────────────────────────────────────────

class TestPGFE:
    """天津-PGFE-乳腺癌-方穹推荐 — 正向验证用例。

    这些页面在当前修改下表现正确，确保改进不会引入回归。
    """

    CASE = "pgfe"

    @pytest.fixture(scope="class")
    def tables(self):
        result = _load_vl_result(self.CASE)
        page_images = _load_page_images(self.CASE)
        parser = _make_parser_with_images(page_images)
        tables = parser._transfer_to_tables(result)
        logging.info(
            "[PGFE] _transfer_to_tables returned %d tables: pages=%s",
            len(tables), [t["page"] for t in tables],
        )
        return tables

    # ── Page 6 ──

    def test_p6_exists(self, tables):
        p6_tables = _extract_table_by_page(tables, 6)
        assert len(p6_tables) >= 1, "PGFE page 6 should have at least 1 table"

    def test_p6_monotonic(self, tables):
        p6_tables = _extract_table_by_page(tables, 6)
        for t in p6_tables:
            _validate_monotonic(t)

    def test_p6_no_overlap(self, tables):
        p6_tables = _extract_table_by_page(tables, 6)
        for t in p6_tables:
            _validate_no_overlap(t)

    def test_p6_min_row_height(self, tables):
        p6_tables = _extract_table_by_page(tables, 6)
        for t in p6_tables:
            _validate_min_row_height(t)

    # ── Page 7 ──

    def test_p7_exists(self, tables):
        p7_tables = _extract_table_by_page(tables, 7)
        assert len(p7_tables) >= 1, "PGFE page 7 should have at least 1 table"

    def test_p7_monotonic(self, tables):
        p7_tables = _extract_table_by_page(tables, 7)
        for t in p7_tables:
            _validate_monotonic(t)

    def test_p7_no_overlap(self, tables):
        p7_tables = _extract_table_by_page(tables, 7)
        for t in p7_tables:
            _validate_no_overlap(t)

    # ── Page 9: 关键表头优化案例 ──

    def test_p9_exists(self, tables):
        p9_tables = _extract_table_by_page(tables, 9)
        assert len(p9_tables) >= 1, "PGFE page 9 should have at least 1 table"

    def test_p9_monotonic(self, tables):
        p9_tables = _extract_table_by_page(tables, 9)
        for t in p9_tables:
            _validate_monotonic(t)

    def test_p9_no_overlap(self, tables):
        p9_tables = _extract_table_by_page(tables, 9)
        for t in p9_tables:
            _validate_no_overlap(t)

    def test_p9_min_row_height(self, tables):
        p9_tables = _extract_table_by_page(tables, 9)
        for t in p9_tables:
            _validate_min_row_height(t)


# ──────────────────────────────────────────────────────────────────
# 诊断输出 (不是 assert, 仅打印帮助分析)
# ──────────────────────────────────────────────────────────────────

class TestDiagnostics:
    """诊断测试 — 打印详细的行坐标信息，帮助人工分析。

    这些测试不会 fail，只输出诊断信息。
    """

    @pytest.mark.parametrize("case,pages", [
        ("dsxi", [8, 9, 10, 11]),
        ("pgfe", [6, 7, 9]),
    ])
    def test_print_row_details(self, case, pages):
        """打印每个表格的行坐标详情。"""
        try:
            result = _load_vl_result(case)
            page_images = _load_page_images(case)
        except Exception:
            pytest.skip(f"Fixtures for {case} not available")

        parser = _make_parser_with_images(page_images)
        tables = parser._transfer_to_tables(result)

        for page in pages:
            page_tables = _extract_table_by_page(tables, page)
            for ti, t in enumerate(page_tables):
                rows = t["row_positions"]
                print(f"\n{'='*60}")
                print(f"[{case.upper()}] Page {page} Table #{ti}")
                print(f"  bbox: {t['bbox']}")
                print(f"  num_rows (from HTML <tr>): {len(rows)}")
                print(f"  row_positions:")
                for ri, r in enumerate(rows):
                    h = r[4] - r[3]
                    print(f"    [{ri:2d}] top={r[3]:5d} bottom={r[4]:5d} height={h:4d}")
                print(f"{'='*60}")
