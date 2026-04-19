#!/usr/bin/env python3
"""
独立测试: _evaluate_table_orientation 旋转检测准确性验证

测试目标:
  1. 旋转案例 (Bxli糖尿病 p4/p5) → 应检测出 90° 或 270°
  2. 正常案例 (LGPI p20/p21/p23, PGFE p6/p7) → 应检测出 0°

调用的是 pdf_parser.py 中 _evaluate_table_orientation 的原生逻辑，
后续业务集成时直接使用同一方法（通过继承链 PaddleOCRParser → RAGFlowPdfParser）。

运行:
  cd /Users/weixiaofeng/Desktop/zxwl/coding/ragflow
  python tests/test_rotation_detection.py
"""

import sys
import os
import logging
import time

# 确保 ragflow 根目录在 sys.path 中
RAGFLOW_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAGFLOW_ROOT)

import pdfplumber
from PIL import Image
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


# ─── 测试用例定义 ───
PDF_DIR = "/Users/weixiaofeng/Desktop/medlink 数据"

TEST_CASES = [
    # ── 旋转案例：Bxli糖尿病 郑州中心 (使用 VL 返回的精确表格 bbox) ──
    # VL bbox (zm*72dpi 空间): [190,626,3410,4328] → 72dpi: 除以 zm
    # zm = VL_scale / 72dpi_scale，这里先用全页80%裁剪，再用精确bbox裁剪对比
    {
        "pdf": os.path.join(PDF_DIR, "Bxli糖尿病 郑州中心.pdf"),
        "page": 4,
        "bbox_72dpi": None,  # 全页80%裁剪
        "expected": [90, 270],
        "desc": "Bxli p4 全页 — 90°旋转",
        "dpi": 200,  # 更高分辨率
    },
    {
        "pdf": os.path.join(PDF_DIR, "Bxli糖尿病 郑州中心.pdf"),
        "page": 5,
        "bbox_72dpi": None,
        "expected": [90, 270],
        "desc": "Bxli p5 全页 — 90°旋转",
        "dpi": 200,
    },

    # ── 正常案例：LGPI ──
    {
        "pdf": os.path.join(PDF_DIR, "LGPI-女-类风湿性关节炎-山东菏泽中心.pdf"),
        "page": 20,
        "bbox_72dpi": None,
        "expected": [0],
        "desc": "LGPI p20 — 正常竖版",
        "dpi": 200,
    },
    {
        "pdf": os.path.join(PDF_DIR, "LGPI-女-类风湿性关节炎-山东菏泽中心.pdf"),
        "page": 23,
        "bbox_72dpi": None,
        "expected": [0],
        "desc": "LGPI p23 — 正常横版",
        "dpi": 200,
    },

    # ── 正常案例：PGFE ──
    {
        "pdf": os.path.join(PDF_DIR, "天津-PGFE-乳腺癌-方穹推荐.pdf"),
        "page": 7,
        "bbox_72dpi": None,
        "expected": [0],
        "desc": "PGFE p7 — 正常横版",
        "dpi": 200,
    },
]


def render_page_image(pdf_path: str, page_1based: int, dpi: int = 72) -> Image.Image:
    """用 pdfplumber 渲染 PDF 页面为 PIL Image"""
    pdf = pdfplumber.open(pdf_path)
    page = pdf.pages[page_1based - 1]
    img = page.to_image(resolution=dpi, antialias=True).original
    pdf.close()
    return img.convert("RGB")


def crop_table(page_img: Image.Image, bbox_72dpi: tuple | None) -> Image.Image:
    """裁剪表格区域。如果 bbox 为 None，使用页面中心 80% 区域"""
    if bbox_72dpi:
        left, top, right, bottom = bbox_72dpi
        return page_img.crop((left, top, right, bottom))
    else:
        w, h = page_img.size
        margin_x = int(w * 0.1)
        margin_y = int(h * 0.1)
        return page_img.crop((margin_x, margin_y, w - margin_x, h - margin_y))


def main():
    logger.info("=" * 70)
    logger.info("初始化 RAGFlowPdfParser（加载 PP-OCRv4 模型）...")
    logger.info("=" * 70)

    from deepdoc.parser.pdf_parser import RAGFlowPdfParser
    parser = RAGFlowPdfParser()
    logger.info("PP-OCRv4 加载完成 ✓")

    results = []

    for i, tc in enumerate(TEST_CASES):
        logger.info("")
        logger.info("─" * 60)
        logger.info(f"[{i+1}/{len(TEST_CASES)}] {tc['desc']}")
        logger.info(f"  PDF: {os.path.basename(tc['pdf'])}")
        logger.info(f"  Page: {tc['page']}")
        logger.info(f"  Expected: {tc['expected']}°")
        logger.info("─" * 60)

        if not os.path.exists(tc["pdf"]):
            logger.error(f"  ❌ PDF不存在: {tc['pdf']}")
            results.append({"desc": tc["desc"], "status": "SKIP", "reason": "PDF不存在"})
            continue

        # 渲染页面（使用用例指定的 DPI）
        dpi = tc.get("dpi", 72)
        t0 = time.time()
        page_img = render_page_image(tc["pdf"], tc["page"], dpi=dpi)
        logger.info(f"  页面渲染: {page_img.size[0]}x{page_img.size[1]} @{dpi}dpi ({time.time()-t0:.2f}s)")

        # 裁剪表格区域
        table_crop = crop_table(page_img, tc.get("bbox_72dpi"))
        logger.info(f"  表格裁剪: {table_crop.size[0]}x{table_crop.size[1]}")

        # ── 核心测试：调用 _evaluate_table_orientation ──
        t1 = time.time()
        best_angle, best_img, scores = parser._evaluate_table_orientation(table_crop)
        elapsed = time.time() - t1

        # 输出各角度详细得分
        logger.info(f"  ┌─ 检测结果 ─────────────────────────")
        logger.info(f"  │ 检测角度: {best_angle}°")
        logger.info(f"  │ 期望角度: {tc['expected']}°")
        logger.info(f"  │ 耗时: {elapsed:.2f}s")
        logger.info(f"  │ 各角度得分:")
        for angle in [0, 90, 180, 270]:
            s = scores.get(angle, {})
            marker = " ◀ BEST" if angle == best_angle else ""
            logger.info(
                f"  │   {angle:>3}°: combined={s.get('combined_score',0):.4f}  "
                f"avg_conf={s.get('avg_confidence',0):.4f}  "
                f"regions={s.get('total_regions',0)}{marker}"
            )

        # 安全阈值判断详情
        score_0 = scores.get(0, {}).get("combined_score", 0)
        best_score = scores.get(best_angle, {}).get("combined_score", 0)
        if best_angle != 0:
            margin = best_score - score_0
            logger.info(f"  │ 安全阈值: best-score_0={margin:.4f} (需>0.2), score_0={score_0:.4f} (需<0.8)")

        passed = best_angle in tc["expected"]
        status = "✅ PASS" if passed else "❌ FAIL"
        logger.info(f"  └─ {status}")

        results.append({
            "desc": tc["desc"],
            "expected": tc["expected"],
            "actual": best_angle,
            "elapsed": elapsed,
            "scores": scores,
            "status": "PASS" if passed else "FAIL",
        })

    # ─── 汇总 ───
    logger.info("")
    logger.info("=" * 70)
    logger.info("测试汇总")
    logger.info("=" * 70)
    pass_count = sum(1 for r in results if r["status"] == "PASS")
    fail_count = sum(1 for r in results if r["status"] == "FAIL")
    skip_count = sum(1 for r in results if r["status"] == "SKIP")

    for r in results:
        icon = "✅" if r["status"] == "PASS" else ("❌" if r["status"] == "FAIL" else "⏭")
        if r["status"] in ("PASS", "FAIL"):
            logger.info(
                f"  {icon} {r['desc']}: "
                f"expected={r['expected']}° actual={r['actual']}° "
                f"({r['elapsed']:.2f}s)"
            )
        else:
            logger.info(f"  {icon} {r['desc']}: {r.get('reason', 'skipped')}")

    logger.info("")
    logger.info(f"  PASS: {pass_count}  FAIL: {fail_count}  SKIP: {skip_count}")
    logger.info("=" * 70)

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
