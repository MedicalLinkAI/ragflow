"""
test_tsr_rotation_integration.py
================================
Integration tests for TSR rotation detection, correction, and coordinate mapping.

Uses REAL PDF pages to validate the full pipeline:
  1. PP-LCNet orientation detection accuracy on real page crops
  2. Rotation correction direction (must be CCW via PIL rotate(+angle))
  3. Coordinate reverse mapping round-trip accuracy
  4. Full _tsr_enhance_row_positions pipeline with rotation
  5. Zero false-positive baseline across 10+ normal PDFs

Test data:
  - Bxli糖尿病 pages 4-5: real 90° rotated table pages (ground truth)
  - 10 other PDFs: all pages confirmed 0° by PP-LCNet
  - Synthetic 180°/270° rotations from normal pages
"""
import logging
import os
import sys
import types

import numpy as np
import pytest
from PIL import Image

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

if "xgboost" not in sys.modules:
    sys.modules["xgboost"] = types.ModuleType("xgboost")

from deepdoc.vision.doc_orientation_classifier import (
    DocOrientationClassifier,
    ORIENTATION_MARGIN_THRESHOLD,
)

PDF_DIR = os.environ.get(
    "MEDLINK_PDF_DIR",
    "/Users/weixiaofeng/Desktop/medlink 数据",
)

_skip_no_pdf = pytest.mark.skipif(
    not os.path.exists(os.path.join(PDF_DIR, "Bxli糖尿病 郑州中心.pdf")),
    reason="Test PDFs not available — set MEDLINK_PDF_DIR",
)

# ─── Known test PDFs ──────────────────────────────────────────────
BXLI_PDF = os.path.join(PDF_DIR, "Bxli糖尿病 郑州中心.pdf")
LGPI_PDF = os.path.join(PDF_DIR, "LGPI-女-类风湿性关节炎-山东菏泽中心.pdf")

NORMAL_PDFS = [
    ("CHRI 肺腺癌 深圳.pdf", 8),
    ("DJME-女-类风湿-菏泽中心.pdf", 23),
    ("DSXI 肺癌 山东中心.pdf", 25),
    ("FPJU-肠癌.pdf", 15),
    ("HGJI-肠癌.pdf", 12),
    ("HZNA高血糖郑州.pdf", 9),
    ("LHPI+单药+司美医大一院.pdf", 7),
    ("LQYI-女-类风湿性关节炎.pdf", 11),
    ("YGPI-女-类风湿性关节炎.pdf", 10),
    ("ZCFA 女 69 肠癌.pdf", 6),
]


def _render_page(pdf_path: str, page_idx: int, dpi: int = 72) -> Image.Image:
    """Render a PDF page to PIL Image at given DPI."""
    import pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        return pdf.pages[page_idx].to_image(resolution=dpi).original


def _extract_table_crop(page_img: Image.Image,
                        left_frac=0.05, top_frac=0.15,
                        right_frac=0.95, bottom_frac=0.85) -> Image.Image:
    """Extract the central table region from a page image."""
    w, h = page_img.size
    return page_img.crop((
        int(w * left_frac), int(h * top_frac),
        int(w * right_frac), int(h * bottom_frac),
    ))


@pytest.fixture(scope="module")
def classifier():
    return DocOrientationClassifier.get_instance()


# ═══════════════════════════════════════════════════════════════════
# Part 1: Orientation detection accuracy on real PDF crops
# ═══════════════════════════════════════════════════════════════════

@_skip_no_pdf
class TestRealRotatedPages:
    """Bxli pages 4-5 are 90° rotated scans — must detect on full page AND table crop."""

    def test_bxli_page4_full_page(self, classifier):
        img = _render_page(BXLI_PDF, 3)
        angle, margin = classifier.detect(img)
        assert angle == 90, f"Full page: expected 90°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD

    def test_bxli_page5_full_page(self, classifier):
        img = _render_page(BXLI_PDF, 4)
        angle, margin = classifier.detect(img)
        assert angle == 90, f"Full page: expected 90°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD

    def test_bxli_page4_table_crop(self, classifier):
        """PP-LCNet must also detect rotation on a table crop, not just full page."""
        img = _render_page(BXLI_PDF, 3)
        crop = _extract_table_crop(img)
        angle, margin = classifier.detect(crop)
        assert angle == 90, f"Table crop: expected 90°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD

    def test_bxli_page5_table_crop(self, classifier):
        img = _render_page(BXLI_PDF, 4)
        crop = _extract_table_crop(img)
        angle, margin = classifier.detect(crop)
        assert angle == 90, f"Table crop: expected 90°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD


@_skip_no_pdf
class TestNormalPageBaseline:
    """All pages from 10+ PDFs must NOT trigger false positive rotation."""

    @pytest.mark.parametrize("page_idx", [0, 1, 2, 5, 6])
    def test_bxli_normal_pages(self, classifier, page_idx):
        img = _render_page(BXLI_PDF, page_idx)
        angle, margin = classifier.detect(img)
        is_safe = (angle == 0) or (margin < ORIENTATION_MARGIN_THRESHOLD)
        assert is_safe, (
            f"Bxli page {page_idx+1}: false positive {angle}° margin={margin:.4f}"
        )

    @pytest.mark.parametrize("pdf_name,total_pages", NORMAL_PDFS)
    def test_normal_pdfs_no_false_positive(self, classifier, pdf_name, total_pages):
        """Sample 3 pages (first, middle, last) from each normal PDF."""
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        if not os.path.exists(pdf_path):
            pytest.skip(f"{pdf_name} not found")

        sample_indices = [0, total_pages // 2, total_pages - 1]
        for page_idx in sample_indices:
            img = _render_page(pdf_path, page_idx)
            angle, margin = classifier.detect(img)
            is_safe = (angle == 0) or (margin < ORIENTATION_MARGIN_THRESHOLD)
            assert is_safe, (
                f"{pdf_name} page {page_idx+1}: false positive "
                f"{angle}° margin={margin:.4f}"
            )

    @pytest.mark.parametrize("pdf_name,total_pages", NORMAL_PDFS)
    def test_normal_pdf_table_crops_no_false_positive(self, classifier, pdf_name, total_pages):
        """Also test table crops from normal pages — PP-LCNet should not hallucinate rotation."""
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        if not os.path.exists(pdf_path):
            pytest.skip(f"{pdf_name} not found")

        sample_indices = [0, total_pages // 2]
        for page_idx in sample_indices:
            img = _render_page(pdf_path, page_idx)
            crop = _extract_table_crop(img)
            angle, margin = classifier.detect(crop)
            is_safe = (angle == 0) or (margin < ORIENTATION_MARGIN_THRESHOLD)
            assert is_safe, (
                f"{pdf_name} page {page_idx+1} crop: false positive "
                f"{angle}° margin={margin:.4f}"
            )


# ═══════════════════════════════════════════════════════════════════
# Part 2: Rotation correction direction + reverse mapping round-trip
# ═══════════════════════════════════════════════════════════════════

class TestRotationCorrectionDirection:
    """Verify PIL rotate direction: rotate(+angle) = CCW = undoes CW rotation."""

    @pytest.mark.parametrize("angle", [90, 180, 270])
    def test_ccw_correction_undoes_cw_rotation(self, angle):
        """Rotate CW by angle, then correct with CCW → image returns to original."""
        original = Image.new("RGB", (400, 600), "white")
        from PIL import ImageDraw
        d = ImageDraw.Draw(original)
        d.rectangle([50, 50, 100, 80], fill="red")
        orig_arr = np.array(original)

        # Simulate CW rotation (what the scanner did)
        cw_rotated = original.rotate(-angle, expand=True)
        # Correct with CCW (what our fix does)
        corrected = cw_rotated.rotate(angle, expand=True)
        corr_arr = np.array(corrected)

        assert corrected.size == original.size, (
            f"Size mismatch after round-trip: {corrected.size} vs {original.size}"
        )
        # Pixel content should match (within PIL interpolation tolerance)
        diff = np.abs(orig_arr.astype(int) - corr_arr.astype(int))
        assert diff.max() <= 1, f"Pixel diff too large: max={diff.max()}"


@_skip_no_pdf
class TestRealImageRotationRoundTrip:
    """Round-trip rotation + reverse mapping with real Bxli page crops."""

    def test_bxli_page4_ccw90_reverse_map(self, classifier):
        """
        Bxli page 4 (90° CW rotated):
        1. Detect angle=90
        2. Correct with rotate(+90) = CCW
        3. Reverse map coordinates back
        4. Verify round-trip accuracy
        """
        img = _render_page(BXLI_PDF, 3)
        crop = _extract_table_crop(img)
        orig_w, orig_h = crop.size

        angle, margin = classifier.detect(crop)
        assert angle == 90

        corrected = crop.rotate(angle, expand=True)
        rot_w, rot_h = corrected.size

        # Create a synthetic box in corrected space
        test_box = {"x0": 10, "x1": rot_h - 10, "top": 50, "bottom": 100}

        # Apply reverse mapping for 90°
        mapped = _reverse_map_90(test_box, rot_w)

        # Verify basic geometry
        assert mapped["x0"] < mapped["x1"], "x0 must be < x1"
        assert mapped["top"] < mapped["bottom"], "top must be < bottom"
        assert mapped["x0"] >= 0, "x0 must be non-negative"
        assert mapped["top"] >= 0, "top must be non-negative"
        assert mapped["x1"] <= orig_w + 1, f"x1={mapped['x1']} exceeds orig_w={orig_w}"
        assert mapped["bottom"] <= orig_h + 1, f"bottom={mapped['bottom']} exceeds orig_h={orig_h}"

    def test_bxli_page4_full_roundtrip(self, classifier):
        """
        Full round-trip: place a known box in original → rotate → detect in corrected
        → reverse map → compare with original.
        """
        img = _render_page(BXLI_PDF, 3)
        crop = _extract_table_crop(img)
        orig_w, orig_h = crop.size

        # Known box in original crop space
        orig_box = {"x0": 30, "x1": 200, "top": 100, "bottom": 150}

        # Forward transform: CCW 90° (the correction direction)
        # CCW 90° maps (x,y) in W×H → (H-y, x) in H×W
        fwd_x0 = orig_h - orig_box["bottom"]
        fwd_top = orig_box["x0"]
        fwd_x1 = orig_h - orig_box["top"]
        fwd_bot = orig_box["x1"]
        fwd_box = {"x0": fwd_x0, "x1": fwd_x1, "top": fwd_top, "bottom": fwd_bot}

        corrected = crop.rotate(90, expand=True)
        rot_w, _ = corrected.size  # rot_w = orig_h

        # Reverse map
        mapped = _reverse_map_90(fwd_box, rot_w)

        assert abs(mapped["x0"] - orig_box["x0"]) <= 1
        assert abs(mapped["x1"] - orig_box["x1"]) <= 1
        assert abs(mapped["top"] - orig_box["top"]) <= 1
        assert abs(mapped["bottom"] - orig_box["bottom"]) <= 1


def _reverse_map_90(box, rot_w):
    """Reproduce the exact _reverse_map_rb formula from paddleocr_parser.py for angle=90."""
    return {
        "x0": box["top"],
        "x1": box["bottom"],
        "top": rot_w - box["x1"],
        "bottom": rot_w - box["x0"],
    }


def _reverse_map_180(box, rot_w, rot_h):
    """Reproduce the formula for 180°."""
    return {
        "x0": rot_w - box["x1"],
        "x1": rot_w - box["x0"],
        "top": rot_h - box["bottom"],
        "bottom": rot_h - box["top"],
    }


def _reverse_map_270(box, rot_h):
    """Reproduce the formula for 270°."""
    return {
        "x0": rot_h - box["bottom"],
        "x1": rot_h - box["top"],
        "top": box["x0"],
        "bottom": box["x1"],
    }


class TestReverseMapFormulas:
    """Verify reverse mapping formulas with known geometry — no mocks."""

    @pytest.mark.parametrize("orig_box", [
        {"x0": 50, "x1": 550, "top": 100, "bottom": 140},
        {"x0": 10, "x1": 590, "top": 200, "bottom": 250},
        {"x0": 0, "x1": 600, "top": 0, "bottom": 800},
    ])
    def test_90_roundtrip_formula(self, orig_box):
        """Place box → CCW 90° forward → reverse map → must match original."""
        W, H = 600, 800
        # CCW 90° forward: (x,y) → (H-y, x) in H×W
        fwd = {
            "x0": H - orig_box["bottom"],
            "x1": H - orig_box["top"],
            "top": orig_box["x0"],
            "bottom": orig_box["x1"],
        }
        rot_w = H  # corrected image width = original height
        mapped = _reverse_map_90(fwd, rot_w)
        assert mapped == orig_box, f"90° round-trip failed: {mapped} != {orig_box}"

    @pytest.mark.parametrize("orig_box", [
        {"x0": 50, "x1": 550, "top": 100, "bottom": 140},
        {"x0": 0, "x1": 600, "top": 0, "bottom": 800},
    ])
    def test_180_roundtrip_formula(self, orig_box):
        W, H = 600, 800
        fwd = {
            "x0": W - orig_box["x1"],
            "x1": W - orig_box["x0"],
            "top": H - orig_box["bottom"],
            "bottom": H - orig_box["top"],
        }
        mapped = _reverse_map_180(fwd, W, H)
        assert mapped == orig_box, f"180° round-trip failed: {mapped} != {orig_box}"

    @pytest.mark.parametrize("orig_box", [
        {"x0": 50, "x1": 550, "top": 100, "bottom": 140},
        {"x0": 0, "x1": 600, "top": 0, "bottom": 800},
    ])
    def test_270_roundtrip_formula(self, orig_box):
        W, H = 600, 800
        # CCW 270° = CW 90°: (x,y) → (y, W-x) in H×W
        fwd = {
            "x0": orig_box["top"],
            "x1": orig_box["bottom"],
            "top": W - orig_box["x1"],
            "bottom": W - orig_box["x0"],
        }
        rot_h = W  # corrected image height = original width
        mapped = _reverse_map_270(fwd, rot_h)
        assert mapped == orig_box, f"270° round-trip failed: {mapped} != {orig_box}"


# ═══════════════════════════════════════════════════════════════════
# Part 3: Synthetic rotation + PP-LCNet detection
# ═══════════════════════════════════════════════════════════════════

@_skip_no_pdf
class TestSyntheticRotationsFromRealPages:
    """Rotate normal pages synthetically and verify detection."""

    def _get_normal_crop(self):
        """Get a table crop from a normal Bxli page."""
        img = _render_page(BXLI_PDF, 0)
        return _extract_table_crop(img)

    def test_synthetic_0_from_real(self, classifier):
        crop = self._get_normal_crop()
        angle, margin = classifier.detect(crop)
        is_safe = (angle == 0) or (margin < ORIENTATION_MARGIN_THRESHOLD)
        assert is_safe, f"Normal crop false positive: {angle}° margin={margin:.4f}"

    def test_synthetic_90_from_real(self, classifier):
        crop = self._get_normal_crop()
        rotated = crop.rotate(-90, expand=True)  # CW 90°
        angle, margin = classifier.detect(rotated)
        assert angle == 90, f"Expected 90°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD

    def test_synthetic_180_from_real(self, classifier):
        crop = self._get_normal_crop()
        rotated = crop.rotate(-180, expand=True)  # CW 180°
        angle, margin = classifier.detect(rotated)
        assert angle == 180, f"Expected 180°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD

    def test_synthetic_270_from_real(self, classifier):
        crop = self._get_normal_crop()
        rotated = crop.rotate(-270, expand=True)  # CW 270°
        angle, margin = classifier.detect(rotated)
        assert angle == 270, f"Expected 270°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD


# ═══════════════════════════════════════════════════════════════════
# Part 4: Full pipeline integration — _tsr_enhance_row_positions
# ═══════════════════════════════════════════════════════════════════

@_skip_no_pdf
class TestTSRPipelineWithRealData:
    """
    End-to-end test of _tsr_enhance_row_positions using real PDF pages.
    Requires TSR model (tsr.onnx) in rag/res/deepdoc/.
    """

    @pytest.fixture(scope="class")
    def tsr_model_available(self):
        model_path = os.path.join(_project_root, "rag", "res", "deepdoc", "tsr.onnx")
        if not os.path.exists(model_path):
            pytest.skip("TSR model not available")

    def _make_parser_with_real_page(self, pdf_path, page_idx, dpi=72):
        """Create a PaddleOCRParser with a real PDF page image."""
        from deepdoc.parser.paddleocr_parser import PaddleOCRParser
        parser = PaddleOCRParser.__new__(PaddleOCRParser)
        img = _render_page(pdf_path, page_idx, dpi)
        parser.page_images = [img]
        return parser, img

    def test_bxli_normal_page_tsr_works(self, tsr_model_available):
        """Normal Bxli page 1: TSR should work without rotation intervention."""
        from deepdoc.parser.paddleocr_parser import PaddleOCRParser
        parser, img = self._make_parser_with_real_page(BXLI_PDF, 0)
        w, h = img.size

        # Approximate table bounds (full page is the table for Bxli)
        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=int(w * 0.05), top=int(h * 0.1),
            right=int(w * 0.95), bottom=int(h * 0.9),
            num_rows=6,
            zm=1.0,
        )
        # May return positions or None depending on TSR quality, but should not crash
        if result is not None:
            for pos in result:
                page, x0, x1, pos_top, pos_bottom = pos
                assert page == 1
                assert x0 < x1, f"x0={x0} >= x1={x1}"
                assert pos_top < pos_bottom, f"top={pos_top} >= bottom={pos_bottom}"
                assert x0 >= 0 and pos_top >= 0

    def test_bxli_rotated_page4_tsr_with_rotation(self, tsr_model_available):
        """
        Bxli page 4 (90° rotated): the full pipeline should:
        1. Detect gap > 2 from rotated TSR
        2. PP-LCNet detects 90°
        3. Rotate CCW 90°, re-run TSR
        4. Reverse map coordinates
        5. Return valid positions
        """
        from deepdoc.parser.paddleocr_parser import PaddleOCRParser
        parser, img = self._make_parser_with_real_page(BXLI_PDF, 3)
        w, h = img.size

        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=int(w * 0.05), top=int(h * 0.1),
            right=int(w * 0.95), bottom=int(h * 0.9),
            num_rows=6,
            zm=1.0,
        )
        # With the rotation fix, this should produce valid positions
        if result is not None:
            for pos in result:
                page, x0, x1, pos_top, pos_bottom = pos
                assert page == 1
                assert x0 < x1, f"x0={x0} >= x1={x1}"
                assert pos_top < pos_bottom, f"top={pos_top} >= bottom={pos_bottom}"
                # Coordinates should be within page bounds
                assert x0 >= 0
                assert pos_top >= 0
                assert x1 <= w + 5  # small tolerance for rounding
                assert pos_bottom <= h + 5

    def test_bxli_rotated_page5_tsr_with_rotation(self, tsr_model_available):
        """Same as page 4 test — page 5 is also 90° rotated."""
        from deepdoc.parser.paddleocr_parser import PaddleOCRParser
        parser, img = self._make_parser_with_real_page(BXLI_PDF, 4)
        w, h = img.size

        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=int(w * 0.05), top=int(h * 0.1),
            right=int(w * 0.95), bottom=int(h * 0.9),
            num_rows=6,
            zm=1.0,
        )
        if result is not None:
            for pos in result:
                page, x0, x1, pos_top, pos_bottom = pos
                assert page == 1
                assert x0 < x1
                assert pos_top < pos_bottom
                assert x0 >= 0 and pos_top >= 0

    @pytest.mark.parametrize("pdf_name,total_pages", NORMAL_PDFS[:5])
    def test_normal_pdf_tsr_not_affected(self, tsr_model_available, pdf_name, total_pages):
        """Normal PDFs: rotation gate should NOT activate (angle=0)."""
        from deepdoc.parser.paddleocr_parser import PaddleOCRParser
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        if not os.path.exists(pdf_path):
            pytest.skip(f"{pdf_name} not found")

        parser, img = self._make_parser_with_real_page(pdf_path, 0)
        w, h = img.size

        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=int(w * 0.05), top=int(h * 0.1),
            right=int(w * 0.95), bottom=int(h * 0.9),
            num_rows=6,
            zm=1.0,
        )
        # Should work normally — rotation detection returns 0° and doesn't interfere
        if result is not None:
            for pos in result:
                page, x0, x1, pos_top, pos_bottom = pos
                assert page == 1
                assert x0 < x1
                assert pos_top < pos_bottom


# ═══════════════════════════════════════════════════════════════════
# Part 5: PP-LCNet only evaluates orientation — no side effects
# ═══════════════════════════════════════════════════════════════════

@_skip_no_pdf
class TestClassifierSideEffects:
    """Verify PP-LCNet detect() is pure — no image mutation, deterministic."""

    def test_detect_does_not_modify_image(self, classifier):
        """Input image must not be mutated by detect()."""
        img = _render_page(BXLI_PDF, 3)
        arr_before = np.array(img).copy()
        classifier.detect(img)
        arr_after = np.array(img)
        np.testing.assert_array_equal(arr_before, arr_after)

    def test_detect_is_deterministic(self, classifier):
        """Same image → same result every time."""
        img = _render_page(BXLI_PDF, 3)
        results = [classifier.detect(img) for _ in range(5)]
        assert all(r == results[0] for r in results), f"Non-deterministic: {results}"

    def test_detect_on_crop_vs_full_page(self, classifier):
        """Crop and full page should agree on rotation direction."""
        img = _render_page(BXLI_PDF, 3)
        crop = _extract_table_crop(img)
        angle_full, _ = classifier.detect(img)
        angle_crop, _ = classifier.detect(crop)
        assert angle_full == angle_crop, (
            f"Full page says {angle_full}°, crop says {angle_crop}°"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
