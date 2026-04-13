#!/usr/bin/env python3
"""Export trained YOLO11 TSR model to ONNX format for RAGflow integration.

Usage:
    python export_onnx.py --weights /path/to/best.pt --output tsr-yolo11.onnx

The exported ONNX model should be placed in rag/res/deepdoc/tsr-yolo11.onnx
and activated with TSR_MODEL=yolov11 environment variable.

ONNX output tensor shape: [1, 11, 8400]
  - 11 = 5 (x, y, w, h, obj_conf) + 6 (class scores)
  - 8400 = number of detection anchors at 640×640
This is schema-compatible with YOLOv8 ONNX format that RAGflow already handles.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export YOLO11 TSR model to ONNX for RAGflow.",
    )
    parser.add_argument(
        "--weights",
        required=True,
        help="Path to trained .pt weights (e.g. best.pt).",
    )
    parser.add_argument(
        "--output",
        default="tsr-yolo11.onnx",
        help="Output ONNX file path (default: tsr-yolo11.onnx).",
    )
    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="Input image size (default: 640).",
    )
    parser.add_argument(
        "--opset",
        type=int,
        default=17,
        help="ONNX opset version (default: 17).",
    )
    args = parser.parse_args()

    weights_path = Path(args.weights)
    if not weights_path.exists():
        print(f"ERROR: weights file not found: {args.weights}", file=sys.stderr)
        sys.exit(1)

    try:
        from ultralytics import YOLO
    except ImportError:
        print(
            "ERROR: ultralytics is not installed. "
            "Run: pip install ultralytics>=8.3.0",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Loading model from {args.weights} ...")
    model = YOLO(str(weights_path))

    print(f"Exporting to ONNX (opset={args.opset}, imgsz={args.imgsz}) ...")
    model.export(
        format="onnx",
        imgsz=args.imgsz,
        opset=args.opset,
        simplify=True,
        dynamic=False,
    )

    # Ultralytics writes the .onnx next to the .pt file
    exported_path = weights_path.with_suffix(".onnx")
    output_path = Path(args.output)

    if not exported_path.exists():
        print(f"ERROR: expected ONNX file not found at {exported_path}", file=sys.stderr)
        sys.exit(1)

    if exported_path.resolve() != output_path.resolve():
        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(exported_path), str(output_path))

    print()
    print(f"ONNX model exported: {output_path}")
    print(f"  Input shape:  [1, 3, {args.imgsz}, {args.imgsz}]")
    print(f"  Output shape: [1, 11, 8400]  (6 classes + 5 bbox/conf)")
    print()
    print("RAGflow integration:")
    print(f"  cp {output_path} rag/res/deepdoc/tsr-yolo11.onnx")
    print("  # Set environment variable: TSR_MODEL=yolov11")


if __name__ == "__main__":
    main()
