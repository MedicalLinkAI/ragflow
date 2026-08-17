"""VL image preprocessing: downscale oversized page images before sending.

Qwen3-VL-30B-A3B 对输入图像敏感：长边 >4000px 或体积 >2MB 的页面图易触发
120s read timeout（prefill 耗时与像素面积成正比）。本模块在发送前把超限图
缩放至长边 ≤3840px 并 JPEG 压缩（quality 85），目标 <1.8MB。

Safety:
- 坐标不受影响：模型返回相对输入图的 1000-unit 归一化坐标，缩放只改输入图。
- 小图直通：不满足触发条件（bytes>2MB 或 长边>3840）时原样返回，零开销。
- 损坏字节直通：无法解码时原样返回，由下游按原逻辑处理。
"""

from __future__ import annotations

import base64
import io
import logging

TAG = "[vl-img-prep]"

# 触发阈值（生产超时排查结论：>2MB 或 >4000px 易超时）
SIZE_TRIGGER_BYTES = 2 * 1024 * 1024
MAX_SIDE_TRIGGER = 3840

# 目标上限
TARGET_BYTES = int(1.8 * 1024 * 1024)

# 回退阶梯：先降 quality，再降长边
_QUALITY_STEPS = (85, 75, 65)
_SIDE_STEPS = (3840, 3072, 2560)


def downscale_vl_image(img_bytes: bytes) -> bytes:
    """Downscale an oversized page image before VL API call.

    Returns the input unchanged when:
    - bytes <= 2MB AND long edge <= 3840 (no trigger), or
    - the bytes cannot be decoded as an image.

    Otherwise returns a JPEG (long edge <=3840, quality 85) that is
    iteratively tightened (quality then side) until <= TARGET_BYTES.
    """
    if len(img_bytes) <= SIZE_TRIGGER_BYTES:
        # Only the long-edge trigger may still apply; need to decode to know
        # the size. Small images that don't decode also pass through.
        try:
            from PIL import Image

            with Image.open(io.BytesIO(img_bytes)) as im:
                if max(im.size) <= MAX_SIDE_TRIGGER:
                    return img_bytes
        except Exception:
            return img_bytes

    try:
        from PIL import Image

        with Image.open(io.BytesIO(img_bytes)) as im:
            im = im.convert("RGB")
            orig_w, orig_h = im.size
            result = None
            for side in _SIDE_STEPS:
                if max(orig_w, orig_h) > side:
                    scale = side / max(orig_w, orig_h)
                    resized = im.resize(
                        (max(1, round(orig_w * scale)), max(1, round(orig_h * scale))),
                        Image.LANCZOS,
                    )
                else:
                    resized = im
                for quality in _QUALITY_STEPS:
                    buf = io.BytesIO()
                    resized.save(buf, format="JPEG", quality=quality)
                    result = buf.getvalue()
                    if len(result) <= TARGET_BYTES:
                        logging.info(
                            f"{TAG} downscaled {len(img_bytes)/1048576:.2f}MB "
                            f"PNG({orig_w}x{orig_h}) -> {len(result)/1048576:.2f}MB "
                            f"JPEG({resized.size[0]}x{resized.size[1]}, q={quality})"
                        )
                        return result
            logging.warning(
                f"{TAG} downscaled image still exceeds target "
                f"({len(result)/1048576:.2f}MB > 1.8MB), sending best-effort"
            )
            return result
    except Exception as e:
        logging.warning(f"{TAG} downscale failed ({e}), sending original")
        return img_bytes


def vl_image_data_url(img_bytes: bytes) -> str:
    """Build a base64 data URL with MIME sniffed from magic bytes."""
    if img_bytes[:3] == b"\xff\xd8\xff":
        mime = "jpeg"
    else:
        mime = "png"
    b64 = base64.b64encode(img_bytes).decode("ascii")
    return f"data:image/{mime};base64,{b64}"
