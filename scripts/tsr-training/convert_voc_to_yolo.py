#!/usr/bin/env python3
"""Convert PubTables-1M PASCAL VOC XML annotations to YOLO format.

PubTables-1M TSR classes:
    0: table
    1: table column
    2: table row
    3: table column header
    4: table projected row header
    5: table spanning cell
    6: no object  (skipped — DETR artifact, no annotations expected)

Usage:
    python convert_voc_to_yolo.py \
        --input-dir /data/datasets/pubtables1m-tsr/PubTables-1M-Structure_Table_Structure_PASCAL_VOC/train \
        --output-dir /data/datasets/pubtables1m-tsr/labels/train \
        --workers 8
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

from tqdm import tqdm

# ---------------------------------------------------------------------------
# Class mapping: VOC name → YOLO class_id
# ---------------------------------------------------------------------------
VOC_NAME_TO_CLASS_ID: dict[str, int] = {
    "table": 0,
    "table column": 1,
    "table row": 2,
    "table column header": 3,
    "table projected row header": 4,
    "table spanning cell": 5,
    # "no object" (class 6) is intentionally omitted — skip during conversion
}

SKIP_CLASSES: set[str] = {"no object"}

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Result container
# ---------------------------------------------------------------------------
@dataclass
class ConvertResult:
    """Result from converting a single VOC XML file."""

    success: bool = True
    annotation_count: int = 0
    class_counts: Counter = field(default_factory=Counter)
    skipped_classes: Counter = field(default_factory=Counter)
    error_message: str = ""


# ---------------------------------------------------------------------------
# Core conversion
# ---------------------------------------------------------------------------
def convert_one(xml_path: str, output_dir: str) -> ConvertResult:
    """Parse one PASCAL VOC XML and write the corresponding YOLO .txt file.

    Returns a ConvertResult with per-class counts and error info.
    """
    result = ConvertResult()

    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as exc:
        result.success = False
        result.error_message = f"{xml_path}: XML parse error — {exc}"
        return result
    except Exception as exc:  # noqa: BLE001
        result.success = False
        result.error_message = f"{xml_path}: unexpected error — {exc}"
        return result

    root = tree.getroot()

    # --- image dimensions ---------------------------------------------------
    size_el = root.find("size")
    if size_el is None:
        result.success = False
        result.error_message = f"{xml_path}: missing <size> element"
        return result

    width_el = size_el.find("width")
    height_el = size_el.find("height")
    if width_el is None or height_el is None:
        result.success = False
        result.error_message = f"{xml_path}: missing <width> or <height>"
        return result

    try:
        img_w = int(width_el.text)  # type: ignore[arg-type]
        img_h = int(height_el.text)  # type: ignore[arg-type]
    except (ValueError, TypeError) as exc:
        result.success = False
        result.error_message = f"{xml_path}: invalid dimensions — {exc}"
        return result

    if img_w <= 0 or img_h <= 0:
        result.success = False
        result.error_message = f"{xml_path}: non-positive dimensions ({img_w}×{img_h})"
        return result

    # --- objects -------------------------------------------------------------
    lines: list[str] = []
    for obj in root.iter("object"):
        name_el = obj.find("name")
        if name_el is None or name_el.text is None:
            continue

        cls_name: str = name_el.text.strip()

        if cls_name in SKIP_CLASSES:
            result.skipped_classes[cls_name] += 1
            continue

        class_id = VOC_NAME_TO_CLASS_ID.get(cls_name)
        if class_id is None:
            result.skipped_classes[cls_name] += 1
            logger.warning("%s: unknown class '%s' — skipped", xml_path, cls_name)
            continue

        bbox = obj.find("bndbox")
        if bbox is None:
            logger.warning("%s: object '%s' missing <bndbox> — skipped", xml_path, cls_name)
            continue

        try:
            xmin = float(bbox.findtext("xmin", ""))  # type: ignore[arg-type]
            ymin = float(bbox.findtext("ymin", ""))  # type: ignore[arg-type]
            xmax = float(bbox.findtext("xmax", ""))  # type: ignore[arg-type]
            ymax = float(bbox.findtext("ymax", ""))  # type: ignore[arg-type]
        except (ValueError, TypeError):
            logger.warning("%s: object '%s' has invalid bbox — skipped", xml_path, cls_name)
            continue

        # Clamp to image bounds
        xmin = max(0.0, min(xmin, img_w))
        ymin = max(0.0, min(ymin, img_h))
        xmax = max(0.0, min(xmax, img_w))
        ymax = max(0.0, min(ymax, img_h))

        if xmax <= xmin or ymax <= ymin:
            logger.warning(
                "%s: object '%s' has degenerate bbox (%s,%s,%s,%s) — skipped",
                xml_path, cls_name, xmin, ymin, xmax, ymax,
            )
            continue

        # Convert to YOLO normalized center format
        cx = ((xmin + xmax) / 2.0) / img_w
        cy = ((ymin + ymax) / 2.0) / img_h
        w = (xmax - xmin) / img_w
        h = (ymax - ymin) / img_h

        lines.append(f"{class_id} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")
        result.class_counts[cls_name] += 1

    # --- write output --------------------------------------------------------
    stem = Path(xml_path).stem
    out_path = os.path.join(output_dir, f"{stem}.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
        if lines:
            fh.write("\n")

    result.annotation_count = len(lines)
    return result


# ---------------------------------------------------------------------------
# Parallel driver
# ---------------------------------------------------------------------------
def convert_dataset(
    input_dir: str,
    output_dir: str,
    workers: int = 4,
) -> None:
    """Convert all VOC XML files under *input_dir* to YOLO format in *output_dir*."""

    input_path = Path(input_dir)
    if not input_path.is_dir():
        print(f"ERROR: input directory does not exist: {input_dir}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    xml_files: list[str] = sorted(str(p) for p in input_path.rglob("*.xml"))
    if not xml_files:
        print(f"WARNING: no XML files found under {input_dir}", file=sys.stderr)
        return

    total_files = len(xml_files)
    print(f"Found {total_files:,} XML files in {input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Workers: {workers}")
    print()

    # Aggregate counters
    total_annotations = 0
    total_errors = 0
    class_totals: Counter = Counter()
    skipped_totals: Counter = Counter()

    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(convert_one, xml_path, output_dir): xml_path
            for xml_path in xml_files
        }

        with tqdm(total=total_files, unit="file", desc="Converting") as pbar:
            for future in as_completed(futures):
                result = future.result()
                if not result.success:
                    total_errors += 1
                    logger.warning(result.error_message)
                else:
                    total_annotations += result.annotation_count
                    class_totals.update(result.class_counts)
                    skipped_totals.update(result.skipped_classes)
                pbar.update(1)

    # --- summary -------------------------------------------------------------
    print()
    print("=" * 60)
    print("CONVERSION SUMMARY")
    print("=" * 60)
    print(f"  Total XML files:       {total_files:>10,}")
    print(f"  Successful:            {total_files - total_errors:>10,}")
    print(f"  Errors (skipped):      {total_errors:>10,}")
    print(f"  Total annotations:     {total_annotations:>10,}")
    print()
    print("  Per-class annotation counts:")
    for cls_name, cls_id in sorted(VOC_NAME_TO_CLASS_ID.items(), key=lambda x: x[1]):
        count = class_totals.get(cls_name, 0)
        print(f"    [{cls_id}] {cls_name:<30s} {count:>10,}")
    if skipped_totals:
        print()
        print("  Skipped classes:")
        for cls_name, count in skipped_totals.most_common():
            print(f"    {cls_name:<30s} {count:>10,}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert PubTables-1M PASCAL VOC annotations to YOLO format.",
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        help="Directory containing PASCAL VOC XML annotation files.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory to write YOLO .txt label files.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of parallel workers (default: 4).",
    )
    args = parser.parse_args()

    convert_dataset(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        workers=args.workers,
    )


if __name__ == "__main__":
    main()
