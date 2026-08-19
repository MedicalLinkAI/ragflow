#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""单张图片 压缩前/后 调用 VL 模型解析耗时对比脚本。

对同一张图生成两个变体：
- original  ：原图字节（MIME 按魔数嗅探）
- compressed：vl_image_prep.downscale_vl_image 压缩结果
              （不满足触发条件 bytes>2MB/长边>3840 时直通原图，
                加 --force 则无视触发条件强制 JPEG q85 重编码，便于小图对比）

然后以与 qwen_vl_parser._call_vlm 同构的 payload
（image_url data-URL + prompt，temperature=0，max_tokens=16384）
交替轮流打同一 vLLM 端点，逐次计时，输出压缩前/后耗时对比。

用法:
    python bench_vl_image_compress.py <image_path>
    python bench_vl_image_compress.py img.png --rounds 5 --force
    python bench_vl_image_compress.py img.png --prompt "请以LaTeX tabular输出表格"
    python bench_vl_image_compress.py img.png --endpoint http://10.16.3.16:8090/v1/chat/completions
"""

from __future__ import annotations

import argparse
import base64
import importlib.util
import io
import json
import statistics
import sys
import time
from pathlib import Path

import requests

RAGFLOW_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_ENDPOINT = "http://10.16.3.16:8090/v1/chat/completions"
DEFAULT_PROMPT = "请提取该页图片中的全部文字内容，保持原有排版。"


def load_vl_image_prep():
    """按文件路径直载 vl_image_prep，避免触发 rag 包 __init__ 的重依赖链。"""
    spec = importlib.util.spec_from_file_location(
        "vl_image_prep", RAGFLOW_ROOT / "rag" / "flow" / "extractor" / "vl_image_prep.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def force_jpeg(img_bytes: bytes, quality: int = 85) -> bytes:
    """无视触发条件强制 JPEG 重编码（与 downscale 阶梯首档同参数）。"""
    from PIL import Image
    with Image.open(io.BytesIO(img_bytes)) as im:
        im = im.convert("RGB")
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=quality)
        return buf.getvalue()


def image_dims(img_bytes: bytes) -> tuple[int, int]:
    try:
        from PIL import Image
        with Image.open(io.BytesIO(img_bytes)) as im:
            return im.size
    except Exception:
        return (0, 0)


def data_url(img_bytes: bytes) -> str:
    mime = "jpeg" if img_bytes[:3] == b"\xff\xd8\xff" else "png"
    return f"data:image/{mime};base64,{base64.b64encode(img_bytes).decode('ascii')}"


def resolve_model(endpoint: str, model: str) -> str:
    if model:
        return model
    base = endpoint.rsplit("/chat/completions", 1)[0]
    resp = requests.get(f"{base}/models", timeout=15)
    resp.raise_for_status()
    picked = resp.json()["data"][0]["id"]
    print(f"[info] 自动探测模型: {picked}")
    return picked


def call_vlm(endpoint: str, model: str, img_bytes: bytes, prompt: str,
             timeout: int) -> tuple[float, int, str]:
    """与 _call_vlm 同构的单次调用；返回 (耗时s, 响应字符数, 状态)。"""
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": data_url(img_bytes)}},
                {"type": "text", "text": prompt},
            ]},
        ],
        "temperature": 0,
        "max_tokens": 16384,
    }
    t0 = time.time()
    try:
        resp = requests.post(endpoint, json=payload,
                             headers={"Content-Type": "application/json"},
                             timeout=timeout)
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        return time.time() - t0, len(content), "OK"
    except Exception as e:
        return time.time() - t0, 0, f"ERR:{type(e).__name__}"


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    p = argparse.ArgumentParser(description="单图压缩前/后 VL 解析耗时对比")
    p.add_argument("image", help="图片路径（PNG/JPEG）")
    p.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    p.add_argument("--model", default="", help="模型 ID（空=GET /v1/models 自动探测）")
    p.add_argument("--prompt", default=DEFAULT_PROMPT)
    p.add_argument("--rounds", type=int, default=3, help="每个变体的计时轮数")
    p.add_argument("--force", action="store_true",
                   help="图不满足压缩触发条件时强制 JPEG q85 重编码")
    p.add_argument("--timeout", type=int, default=300)
    args = p.parse_args()

    prep = load_vl_image_prep()
    orig = Path(args.image).read_bytes()
    comp = prep.downscale_vl_image(orig)
    triggered = comp is not orig and comp != orig
    if not triggered and args.force:
        comp = force_jpeg(orig)
        note = "未触发压缩，--force 强制 JPEG q85 重编码"
    elif not triggered:
        note = "未触发压缩且未加 --force，compressed=original（对比无意义）"
    else:
        note = "命中 downscale_vl_image 压缩"

    ow, oh = image_dims(orig)
    cw, ch = image_dims(comp)
    model = resolve_model(args.endpoint, args.model)

    print("=" * 72)
    print(f"图片     : {args.image}")
    print(f"original : {len(orig)/1048576:.2f}MB {ow}x{oh}")
    print(f"compressed: {len(comp)/1048576:.2f}MB {cw}x{ch}（{note}）")
    print(f"endpoint : {args.endpoint}  model={model}")
    print(f"轮数     : {args.rounds}（交替轮流，另含 1 次 warmup 不计入）")
    print("=" * 72)

    # warmup（不计入统计）
    dt, n, st = call_vlm(args.endpoint, model, comp, args.prompt, args.timeout)
    print(f"[warmup] {st} {dt:.1f}s resp_len={n}")

    times: dict[str, list[float]] = {"original": [], "compressed": []}
    lens: dict[str, list[int]] = {"original": [], "compressed": []}
    order = ["original", "compressed"]
    for rnd in range(args.rounds):
        seq = order if rnd % 2 == 0 else order[::-1]  # 交替顺序消除先后偏差
        for variant in seq:
            blob = orig if variant == "original" else comp
            dt, n, st = call_vlm(args.endpoint, model, blob, args.prompt, args.timeout)
            print(f"[round {rnd + 1}] {variant:<10} {st} {dt:.1f}s resp_len={n}")
            if st == "OK":
                times[variant].append(dt)
                lens[variant].append(n)

    print("-" * 72)
    for variant in ["original", "compressed"]:
        ts = times[variant]
        if not ts:
            print(f"{variant:<10}: 无成功调用")
            continue
        avg = statistics.mean(ts)
        print(f"{variant:<10}: n={len(ts)} 均{avg:.1f}s 中位{statistics.median(ts):.1f}s "
              f"min={min(ts):.1f}s max={max(ts):.1f}s 平均响应{statistics.mean(lens[variant]):.0f}字")
    if times["original"] and times["compressed"]:
        a = statistics.mean(times["original"])
        b = statistics.mean(times["compressed"])
        print(f"对比      : 压缩后均耗 {b:.1f}s vs 压缩前 {a:.1f}s "
              f"→ {(b - a) / a * 100:+.1f}%（负=提速）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
