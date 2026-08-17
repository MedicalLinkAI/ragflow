"""Unit tests for vl_image_prep.py.

Run (from repo root):
    cd ragflow && python rag/tests/test_vl_image_prep.py

Validated thresholds (from production timeout investigation):
- images >4000x4000px or >2MB frequently trigger 120s read timeout on the
  Qwen3-VL coord/text API
- target: long edge <=3840px, JPEG quality 85, output <1.8MB
"""
import importlib.util
import io
import os
import sys
import unittest
from pathlib import Path

_HERE = Path(__file__).resolve().parent
REPO_ROOT = _HERE.parent.parent
TARGET = REPO_ROOT / "rag" / "flow" / "extractor" / "vl_image_prep.py"

spec = importlib.util.spec_from_file_location("vl_image_prep", TARGET)
mod = importlib.util.module_from_spec(spec)
sys.modules["vl_image_prep"] = mod
spec.loader.exec_module(mod)

from PIL import Image  # noqa: E402


def _png_bytes(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def _jpeg_bytes(img: Image.Image, quality: int) -> bytes:
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="JPEG", quality=quality)
    return buf.getvalue()


def _gradient_img(w: int, h: int) -> Image.Image:
    """Deterministic textured image (gradient rows), compressible like scans."""
    row = bytes(x % 256 for x in range(w * 3))
    return Image.frombytes("RGB", (w, h), row * h)


def _scanlike_img(w: int, h: int) -> Image.Image:
    """Gradient base + low-amplitude noise: big as PNG, JPEG-compressible
    like a real scanned page."""
    base = _gradient_img(w, h).convert("L")
    noise = Image.effect_noise((w, h), 12)
    merged = Image.blend(base, noise, 0.5)
    return Image.merge("RGB", (merged, merged, merged))


def _open(data: bytes) -> Image.Image:
    return Image.open(io.BytesIO(data))


class TestDownscalePassthrough(unittest.TestCase):
    def test_small_png_passes_through_unchanged(self):
        raw = _png_bytes(_gradient_img(800, 1200))
        self.assertLess(len(raw), 2 * 1024 * 1024)
        out = mod.downscale_vl_image(raw)
        self.assertEqual(out, raw)

    def test_small_jpeg_passes_through_unchanged(self):
        raw = _jpeg_bytes(_gradient_img(1600, 2200), 90)
        self.assertLess(len(raw), 2 * 1024 * 1024)
        out = mod.downscale_vl_image(raw)
        self.assertEqual(out, raw)

    def test_large_bytes_but_short_side_passes_through(self):
        """Long edge <=3840 AND bytes <=2MB → passthrough even if not tiny."""
        raw = _jpeg_bytes(_gradient_img(3840, 2000), 95)
        if len(raw) > 2 * 1024 * 1024:
            self.skipTest("generated sample exceeds 2MB trigger")
        out = mod.downscale_vl_image(raw)
        self.assertEqual(out, raw)


class TestDownscaleTriggered(unittest.TestCase):
    def test_oversized_long_edge_is_rescaled_to_3840(self):
        raw = _png_bytes(_gradient_img(2000, 5000))  # long edge 5000 > 3840
        out = mod.downscale_vl_image(raw)
        self.assertNotEqual(out, raw)
        img = _open(out)
        self.assertLessEqual(max(img.size), 3840)
        # aspect ratio preserved (within rounding)
        self.assertAlmostEqual(img.size[0] / img.size[1], 2000 / 5000, delta=0.01)

    def test_output_is_jpeg_when_processed(self):
        raw = _png_bytes(_gradient_img(4500, 3000))
        out = mod.downscale_vl_image(raw)
        self.assertEqual(out[:3], b"\xff\xd8\xff")  # JPEG magic

    def test_big_png_over_2mb_compressed_below_target(self):
        # 2900x4000 scan-like PNG: long edge > 3840, bytes > 2MB
        raw = _png_bytes(_scanlike_img(2900, 4000))
        self.assertGreater(len(raw), 2 * 1024 * 1024)
        out = mod.downscale_vl_image(raw)
        self.assertLessEqual(len(out), mod.TARGET_BYTES)
        img = _open(out)
        self.assertLessEqual(max(img.size), 3840)

    def test_corrupt_bytes_passes_through(self):
        raw = b"not-an-image" * 10
        out = mod.downscale_vl_image(raw)
        self.assertEqual(out, raw)


class TestRealPageFixture(unittest.TestCase):
    """Real medical record page from MedLinkAI page-image API (200 DPI).

    5.28MB PNG, 2339x1653 — long edge below 3840, triggered by bytes only.
    """

    FIXTURE = _HERE / "fixtures" / "real_page_5mb.png"

    def setUp(self):
        if not self.FIXTURE.exists():
            self.skipTest("real page fixture not present")
        self.raw = self.FIXTURE.read_bytes()

    def test_real_oversized_png_compressed_below_target(self):
        self.assertGreater(len(self.raw), 2 * 1024 * 1024)
        out = mod.downscale_vl_image(self.raw)
        self.assertLessEqual(len(out), mod.TARGET_BYTES)
        self.assertEqual(out[:3], b"\xff\xd8\xff")

    def test_real_page_keeps_page_dimensions(self):
        """2339x1653 is below the side trigger: no rescale, only re-encode."""
        out = mod.downscale_vl_image(self.raw)
        img = _open(out)
        self.assertEqual(img.size, (2339, 1653))


class TestDataUrl(unittest.TestCase):
    def test_png_magic_yields_png_mime(self):
        raw = _png_bytes(_gradient_img(100, 100))
        url = mod.vl_image_data_url(raw)
        self.assertTrue(url.startswith("data:image/png;base64,"))

    def test_jpeg_magic_yields_jpeg_mime(self):
        raw = _jpeg_bytes(_gradient_img(100, 100), 85)
        url = mod.vl_image_data_url(raw)
        self.assertTrue(url.startswith("data:image/jpeg;base64,"))

    def test_unknown_magic_defaults_to_png(self):
        url = mod.vl_image_data_url(b"\x00\x01\x02\x03")
        self.assertTrue(url.startswith("data:image/png;base64,"))

    def test_round_trip_payload_matches_input(self):
        import base64

        raw = _png_bytes(_gradient_img(120, 80))
        url = mod.vl_image_data_url(raw)
        b64 = url.split(",", 1)[1]
        self.assertEqual(base64.b64decode(b64), raw)


if __name__ == "__main__":
    unittest.main(verbosity=2)
