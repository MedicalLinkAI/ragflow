"""
test_gap_strategy.py
====================
Unit 2 test suite for gap>2 four-layer progressive strategy.

Tests the four layers:
  Layer 1: Height filtering to reduce gap
  Layer 2: PP-LCNet rotation gate + TSR rerun
  Layer 3: VL undercount rescue
  Layer 4: Uniform fallback (return None)
"""
import logging
import os
import sys
import types
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from PIL import Image

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# Stub xgboost to avoid compat import error in test env
if "xgboost" not in sys.modules:
    sys.modules["xgboost"] = types.ModuleType("xgboost")

from deepdoc.parser.paddleocr_parser import PaddleOCRParser


# ─── Helpers ─────────────────────────────────────────────────────────
def _make_parser_with_image(img_w=600, img_h=800):
    """Create a PaddleOCRParser stub with a dummy page image."""
    parser = PaddleOCRParser.__new__(PaddleOCRParser)
    dummy_img = Image.new("RGB", (img_w, img_h), (255, 255, 255))
    parser.page_images = [dummy_img]
    return parser


def _make_row_boxes(n, start_y=50, row_h=30, gap_y=5, x0=10, x1=500):
    """Generate n uniform row_boxes."""
    boxes = []
    y = start_y
    for _ in range(n):
        boxes.append({
            "label": "table row",
            "x0": x0, "x1": x1,
            "top": y, "bottom": y + row_h,
        })
        y += row_h + gap_y
    return boxes


def _make_mixed_row_boxes(normal_n, outlier_sizes, start_y=50, normal_h=30):
    """Generate row_boxes with normal rows + height outliers."""
    boxes = _make_row_boxes(normal_n, start_y=start_y, row_h=normal_h)
    y = boxes[-1]["bottom"] + 5 if boxes else start_y
    for oh in outlier_sizes:
        boxes.append({
            "label": "table row",
            "x0": 10, "x1": 500,
            "top": y, "bottom": y + oh,
        })
        y += oh + 5
    return boxes


# ─── Layer 1 Tests ───────────────────────────────────────────────────
class TestLayer1HeightFiltering:
    """Layer 1: height filtering reduces gap to ≤2."""

    def test_l1_filters_outliers_to_exact_match(self):
        """8 normal + 3 tiny outliers, num_rows=8 → filter to 8 → gap=0."""
        parser = _make_parser_with_image()
        # 8 normal (h=30) + 3 tiny (h=3, well below median*0.7=21)
        row_boxes = _make_mixed_row_boxes(8, [3, 3, 3])

        with patch.object(type(parser), '_tsr_instance',
                          create=True, new_callable=lambda: property(lambda s: None)):
            pass

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=10, top=50, right=500, bottom=600,
            num_rows=8,
            zm=1.0,
        )
        assert result is not None
        assert len(result) == 8

    def test_l1_filters_outliers_to_gap1(self):
        """7 normal + 3 outliers, num_rows=8 → filter to 7 → gap=1 (补表头)."""
        parser = _make_parser_with_image()
        row_boxes = _make_mixed_row_boxes(7, [3, 3, 3])

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=10, top=50, right=500, bottom=600,
            num_rows=8,
            zm=1.0,
        )
        assert result is not None
        assert len(result) == 8  # 7 + 1 header

    def test_l1_cannot_reduce_gap(self):
        """10 uniform rows, num_rows=4 → height filter removes 0 → gap still 6."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(10)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        # No rotation, so Layer-2 will detect 0° → skip → Layer 4 returns None
        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            instance = MagicMock()
            instance.detect.return_value = (0, 0.99)
            mock_cls.get_instance.return_value = instance

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=4,
                zm=1.0,
            )
        assert result is None


# ─── Pre-TSR Rotation Detection Tests ────────────────────────────────
class TestPreTSRRotationDetection:
    """Pre-TSR rotation: PP-LCNet detects rotation → corrects before TSR."""

    def test_rotation_detected_tsr_on_corrected_image(self):
        """Rotation 90° detected → TSR runs on corrected image → gap=0."""
        parser = _make_parser_with_image(600, 800)
        # TSR on corrected image returns 5 rows matching num_rows
        corrected_boxes = _make_row_boxes(5, x0=10, x1=400)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [corrected_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            instance = MagicMock()
            instance.detect.return_value = (90, 0.25)
            mock_cls.get_instance.return_value = instance

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=5,
                zm=1.0,
            )

        assert result is not None
        assert len(result) == 5

    def test_no_rotation_normal_path(self):
        """PP-LCNet says 0° → no correction, TSR on original → gap>2 fallback."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(10)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            instance = MagicMock()
            instance.detect.return_value = (0, 0.99)
            mock_cls.get_instance.return_value = instance

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=4,
                zm=1.0,
            )
        assert result is None

    def test_low_margin_skips_rotation(self):
        """PP-LCNet says 90° but margin < threshold → no correction."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(10)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            instance = MagicMock()
            instance.detect.return_value = (90, 0.05)  # below 0.10 threshold
            mock_cls.get_instance.return_value = instance

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=4,
                zm=1.0,
            )
        assert result is None

    def test_l2_exception_gracefully_falls_through(self):
        """If PP-LCNet throws, Layer 2 is skipped → Layer 4."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(10)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            mock_cls.get_instance.side_effect = RuntimeError("model load failed")

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=4,
                zm=1.0,
            )
        assert result is None


# ─── Layer 3 Tests ───────────────────────────────────────────────────
class TestLayer3VLUndercountRescue:
    """Layer 3: VL undercount rescue (num_rows ≤ 2, TSR ≥ 5)."""

    def test_l3_vl_undercount_trusts_tsr(self):
        """num_rows=2, TSR=8 → gap=6, no outliers, 0° → Layer 3 rescue."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(8)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            instance = MagicMock()
            instance.detect.return_value = (0, 0.99)
            mock_cls.get_instance.return_value = instance

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=2,
                zm=1.0,
            )
        assert result is not None
        assert len(result) == 8  # trust TSR's 8 rows

    def test_l3_not_triggered_when_num_rows_gt_2(self):
        """num_rows=5, TSR=10 → Layer 3 condition not met → Layer 4 None."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(10)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            instance = MagicMock()
            instance.detect.return_value = (0, 0.99)
            mock_cls.get_instance.return_value = instance

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=5,
                zm=1.0,
            )
        assert result is None


# ─── Layer 4 Tests ───────────────────────────────────────────────────
class TestLayer4UniformFallback:
    """Layer 4: all layers fail → return None (uniform fallback)."""

    def test_l4_all_layers_exhausted(self):
        """Uniform rows, 0° rotation, num_rows=5, TSR=10 → None."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(10)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            instance = MagicMock()
            instance.detect.return_value = (0, 0.99)
            mock_cls.get_instance.return_value = instance

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=5,
                zm=1.0,
            )
        assert result is None


# ─── Integration: gap≤2 path unaffected ──────────────────────────────
class TestGapLe2NotAffected:
    """Ensure gap≤2 paths still work correctly (regression guard)."""

    def test_exact_match_still_works(self):
        """TSR=5, num_rows=5, gap=0 → 5 positions."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(5)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=10, top=50, right=500, bottom=600,
            num_rows=5,
            zm=1.0,
        )
        assert result is not None
        assert len(result) == 5

    def test_gap1_minus_header_prepend(self):
        """TSR=4, num_rows=5, gap=1 → 5 positions (header prepended)."""
        parser = _make_parser_with_image()
        row_boxes = _make_row_boxes(4, start_y=80)

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=10, top=50, right=500, bottom=600,
            num_rows=5,
            zm=1.0,
        )
        assert result is not None
        assert len(result) == 5

    def test_gap2_height_filter_resolves(self):
        """TSR=7, num_rows=5, gap=2 → height filter fixes to 5."""
        parser = _make_parser_with_image()
        # 5 normal (h=30) + 2 tiny (h=3)
        row_boxes = _make_mixed_row_boxes(5, [3, 3])

        tsr_mock = MagicMock()
        tsr_mock.return_value = [row_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        result = parser._tsr_enhance_row_positions(
            page_idx=0,
            left=10, top=50, right=500, bottom=600,
            num_rows=5,
            zm=1.0,
        )
        assert result is not None
        assert len(result) == 5


# ─── Coordinate reverse mapping ──────────────────────────────────────
class TestCoordinateReverseMapping:
    """Verify pre-TSR rotation + reverse mapping produces correct coordinates."""

    def test_90_degree_mapping_symmetry(self):
        """After 90° correction + TSR + reverse map, positions stay coherent."""
        parser = _make_parser_with_image(600, 800)
        # TSR on corrected image returns 5 rows (matching num_rows)
        corrected_boxes = [
            {"label": "table row", "x0": 10, "x1": 750,
             "top": 50 + i * 100, "bottom": 50 + i * 100 + 80}
            for i in range(5)
        ]

        tsr_mock = MagicMock()
        tsr_mock.return_value = [corrected_boxes]
        PaddleOCRParser._tsr_instance = tsr_mock

        with patch(
            "deepdoc.vision.doc_orientation_classifier.DocOrientationClassifier"
        ) as mock_cls:
            instance = MagicMock()
            instance.detect.return_value = (90, 0.30)
            mock_cls.get_instance.return_value = instance

            result = parser._tsr_enhance_row_positions(
                page_idx=0,
                left=10, top=50, right=500, bottom=600,
                num_rows=5,
                zm=1.0,
            )

        assert result is not None
        assert len(result) == 5
        for pos in result:
            assert len(pos) == 5
            page, x0, x1, pos_top, pos_bottom = pos
            assert page == 1
            assert pos_top < pos_bottom


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
