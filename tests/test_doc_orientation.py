"""Tests for DocOrientationClassifier.

Validates PP-LCNet ONNX orientation detection against real PDF pages
and synthetic rotations. All tests use the model at rag/res/deepdoc/.
"""
import os
import sys
import pytest
import numpy as np
from PIL import Image

# Ensure project root is importable
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from deepdoc.vision.doc_orientation_classifier import (
    DocOrientationClassifier,
    ORIENTATION_MARGIN_THRESHOLD,
    _softmax,
)

PDF_DIR = os.environ.get(
    "MEDLINK_PDF_DIR",
    "/Users/weixiaofeng/Desktop/medlink 数据",
)

BXLI_PDF = os.path.join(PDF_DIR, "Bxli糖尿病 郑州中心.pdf")
LGPI_PDF = os.path.join(PDF_DIR, "LGPI-女-类风湿性关节炎-山东菏泽中心.pdf")

_skip_no_pdf = pytest.mark.skipif(
    not os.path.exists(BXLI_PDF),
    reason="Test PDFs not available",
)


def _render_page(pdf_path: str, page_idx: int, dpi: int = 72) -> Image.Image:
    """Render a PDF page to PIL Image."""
    import pdfplumber

    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_idx]
        pil_img = page.to_image(resolution=dpi).original
    return pil_img


@pytest.fixture(scope="module")
def classifier():
    return DocOrientationClassifier.get_instance()


# ── Unit Tests ──────────────────────────────────────────────────

class TestSoftmax:
    def test_basic(self):
        result = _softmax(np.array([1.0, 2.0, 3.0, 4.0]))
        assert abs(result.sum() - 1.0) < 1e-6
        assert result[3] > result[2] > result[1] > result[0]

    def test_numerical_stability(self):
        result = _softmax(np.array([1000.0, 1001.0, 999.0, 998.0]))
        assert abs(result.sum() - 1.0) < 1e-6


class TestPreprocessing:
    def test_output_shape(self, classifier):
        img = Image.new("RGB", (640, 480), color=(128, 128, 128))
        tensor = classifier._preprocess(img)
        assert tensor.shape == (1, 3, 224, 224)
        assert tensor.dtype == np.float32

    def test_small_image(self, classifier):
        img = Image.new("RGB", (50, 50), color=(200, 100, 50))
        tensor = classifier._preprocess(img)
        assert tensor.shape == (1, 3, 224, 224)

    def test_grayscale_converted(self, classifier):
        img = Image.new("L", (300, 400))
        tensor = classifier._preprocess(img)
        assert tensor.shape == (1, 3, 224, 224)

    def test_deterministic(self, classifier):
        img = Image.new("RGB", (300, 400), color=(10, 20, 30))
        t1 = classifier._preprocess(img)
        t2 = classifier._preprocess(img)
        np.testing.assert_array_equal(t1, t2)


class TestDetectBasic:
    def test_synthetic_normal(self, classifier):
        img = Image.new("RGB", (400, 600), color=(255, 255, 255))
        angle, margin = classifier.detect(img)
        assert angle in (0, 90, 180, 270)
        assert isinstance(margin, float)
        assert margin >= 0.0

    def test_model_not_loaded_returns_safe_default(self):
        clf = DocOrientationClassifier.__new__(DocOrientationClassifier)
        clf._session = None
        angle, margin = clf.detect(Image.new("RGB", (100, 100)))
        assert angle == 0
        assert margin == 0.0


class TestSingleton:
    def test_same_instance(self):
        a = DocOrientationClassifier.get_instance()
        b = DocOrientationClassifier.get_instance()
        assert a is b
        assert a._session is not None


# ── Integration Tests with Real PDFs ───────────────────────────

@_skip_no_pdf
class TestRotatedPages:
    """Bxli p4/p5 are 90° rotated scans — must detect correctly."""

    def test_bxli_page4_rotated(self, classifier):
        img = _render_page(BXLI_PDF, 3)  # 0-indexed
        angle, margin = classifier.detect(img)
        assert angle == 90, f"Expected 90°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD

    def test_bxli_page5_rotated(self, classifier):
        img = _render_page(BXLI_PDF, 4)
        angle, margin = classifier.detect(img)
        assert angle == 90, f"Expected 90°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD


@_skip_no_pdf
class TestNormalPages:
    """Normal (non-rotated) pages must return 0° or margin < threshold."""

    @pytest.mark.parametrize("page_idx", [0, 1, 2, 5, 6])
    def test_bxli_normal_pages(self, classifier, page_idx):
        img = _render_page(BXLI_PDF, page_idx)
        angle, margin = classifier.detect(img)
        is_safe = (angle == 0) or (margin < ORIENTATION_MARGIN_THRESHOLD)
        assert is_safe, (
            f"Bxli page {page_idx+1}: false positive {angle}° margin={margin:.4f}"
        )

    def test_lgpi_page23(self, classifier):
        img = _render_page(LGPI_PDF, 22)  # 0-indexed
        angle, margin = classifier.detect(img)
        is_safe = (angle == 0) or (margin < ORIENTATION_MARGIN_THRESHOLD)
        assert is_safe, (
            f"LGPI page 23: false positive {angle}° margin={margin:.4f}"
        )


@_skip_no_pdf
class TestSyntheticRotation:
    """Programmatically rotate a normal page and check detection."""

    def _get_normal_page(self):
        return _render_page(BXLI_PDF, 0)

    def test_synthetic_0(self, classifier):
        img = self._get_normal_page()
        angle, margin = classifier.detect(img)
        is_safe = (angle == 0) or (margin < ORIENTATION_MARGIN_THRESHOLD)
        assert is_safe

    def test_synthetic_90(self, classifier):
        img = self._get_normal_page().rotate(-90, expand=True)
        angle, margin = classifier.detect(img)
        assert angle == 90, f"Expected 90°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD

    def test_synthetic_180(self, classifier):
        img = self._get_normal_page().rotate(-180, expand=True)
        angle, margin = classifier.detect(img)
        assert angle == 180, f"Expected 180°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD

    def test_synthetic_270(self, classifier):
        img = self._get_normal_page().rotate(-270, expand=True)
        angle, margin = classifier.detect(img)
        assert angle == 270, f"Expected 270°, got {angle}° (margin={margin:.4f})"
        assert margin >= ORIENTATION_MARGIN_THRESHOLD
