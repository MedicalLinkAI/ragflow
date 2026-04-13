#!/bin/bash
# ============================================================================
# YOLO11m TSR Training on PubTables-1M
# ============================================================================
# Server:   172.16.1.116  (4× A800 80GB)
# GPU:      2 (single GPU, to avoid conflicts)
# Model:    yolo11m.pt (20.1M params, pretrained on COCO)
# Dataset:  PubTables-1M (~947K table images, 6 classes)
# Expected: 8-12 hours training, ~30GB VRAM peak
# ============================================================================

set -euo pipefail

# ── Configuration ───────────────────────────────────────────────────────────
DATASET_ROOT="/data/datasets/pubtables1m-tsr"
WORK_DIR="/data/training/tsr-yolo11"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GPU_ID=0
MODEL="yolo11m.pt"
EPOCHS=100
BATCH=32
IMGSZ=640
PATIENCE=20
WORKERS=8

# ── Step 0: Environment check ──────────────────────────────────────────────
echo "============================================================"
echo "Step 0: Check environment"
echo "============================================================"

# Verify Python packages
python3 -c "
import ultralytics, torch
print(f'Ultralytics {ultralytics.__version__}')
print(f'PyTorch     {torch.__version__}')
print(f'CUDA avail  {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'CUDA ver    {torch.version.cuda}')
    for i in range(torch.cuda.device_count()):
        name = torch.cuda.get_device_name(i)
        mem  = torch.cuda.get_device_properties(i).total_mem / 1024**3
        print(f'  GPU {i}: {name} ({mem:.0f} GB)')
"

nvidia-smi --query-gpu=index,name,memory.total,memory.free \
           --format=csv,noheader

echo ""

# ── Step 1: Download PubTables-1M ──────────────────────────────────────────
echo "============================================================"
echo "Step 1: Download PubTables-1M (if needed)"
echo "============================================================"

mkdir -p "$DATASET_ROOT"

# Uncomment ONE of the following download options:

# Option A: HuggingFace Hub (recommended — handles resume automatically)
# pip install huggingface_hub  # if not installed
# python3 -c "
# from huggingface_hub import snapshot_download
# snapshot_download(
#     'bsmock/pubtables-1m',
#     local_dir='$DATASET_ROOT',
#     repo_type='dataset',
# )
# "

# Option B: Direct download (if HuggingFace is slow in China)
# TSR_URL="https://huggingface.co/datasets/bsmock/pubtables-1m/resolve/main"
# wget -c "\${TSR_URL}/PubTables-1M-Image_Table_Structure_PASCAL_VOC.tar.gz" \
#      -O "$DATASET_ROOT/tsr-voc.tar.gz"
# wget -c "\${TSR_URL}/PubTables-1M-Image_Table_Structure_Images.tar.gz" \
#      -O "$DATASET_ROOT/tsr-images.tar.gz"
# tar xzf "$DATASET_ROOT/tsr-voc.tar.gz"   -C "$DATASET_ROOT"
# tar xzf "$DATASET_ROOT/tsr-images.tar.gz" -C "$DATASET_ROOT"

echo "Dataset root: $DATASET_ROOT"
echo "Checking dataset structure..."
for split in train val test; do
    img_count=$(find "$DATASET_ROOT/images/$split" -name "*.jpg" 2>/dev/null | wc -l || echo "0")
    echo "  images/$split: $img_count images"
done
echo ""

# ── Step 2: Convert VOC annotations to YOLO format ────────────────────────
echo "============================================================"
echo "Step 2: Convert VOC → YOLO format"
echo "============================================================"

# PubTables-1M structure after extraction:
#   PubTables-1M-Structure_Table_Structure_PASCAL_VOC/{train,val,test}/*.xml
#
# Adjust the path below if your extraction layout differs.
VOC_BASE="$DATASET_ROOT/PubTables-1M-Structure_Table_Structure_PASCAL_VOC"

for split in train val test; do
    voc_dir="$VOC_BASE/$split"
    label_dir="$DATASET_ROOT/labels/$split"

    if [ -d "$label_dir" ] && [ "$(ls -A "$label_dir" 2>/dev/null)" ]; then
        echo "  labels/$split already exists — skipping conversion"
        continue
    fi

    if [ ! -d "$voc_dir" ]; then
        echo "  WARNING: $voc_dir not found — skipping"
        continue
    fi

    echo "  Converting $split ..."
    python3 "$SCRIPT_DIR/convert_voc_to_yolo.py" \
        --input-dir "$voc_dir" \
        --output-dir "$label_dir" \
        --workers "$WORKERS"
done

echo ""

# ── Step 3: Verify dataset layout ─────────────────────────────────────────
echo "============================================================"
echo "Step 3: Verify dataset layout"
echo "============================================================"

# YOLO expects:
#   $DATASET_ROOT/images/{train,val,test}/*.jpg
#   $DATASET_ROOT/labels/{train,val,test}/*.txt  (same basenames)

errors=0
for split in train val test; do
    img_dir="$DATASET_ROOT/images/$split"
    lbl_dir="$DATASET_ROOT/labels/$split"

    if [ ! -d "$img_dir" ]; then
        echo "  ERROR: missing $img_dir"
        errors=$((errors + 1))
        continue
    fi
    if [ ! -d "$lbl_dir" ]; then
        echo "  ERROR: missing $lbl_dir"
        errors=$((errors + 1))
        continue
    fi

    n_img=$(find "$img_dir" -name "*.jpg" | wc -l)
    n_lbl=$(find "$lbl_dir" -name "*.txt" | wc -l)
    echo "  $split: $n_img images, $n_lbl labels"

    if [ "$n_img" -eq 0 ] || [ "$n_lbl" -eq 0 ]; then
        echo "    WARNING: empty split"
    fi
done

if [ "$errors" -gt 0 ]; then
    echo ""
    echo "Dataset layout errors detected. Fix before training."
    exit 1
fi

echo ""

# ── Step 4: Copy dataset config ───────────────────────────────────────────
echo "============================================================"
echo "Step 4: Prepare dataset config"
echo "============================================================"

cp "$SCRIPT_DIR/pubtables1m-tsr.yaml" "$WORK_DIR/pubtables1m-tsr.yaml"
echo "Dataset config: $WORK_DIR/pubtables1m-tsr.yaml"
echo ""

# ── Step 5: Train ──────────────────────────────────────────────────────────
echo "============================================================"
echo "Step 5: Start YOLO11m training"
echo "============================================================"
echo "  Model:     $MODEL"
echo "  Epochs:    $EPOCHS"
echo "  Batch:     $BATCH"
echo "  Image sz:  $IMGSZ"
echo "  Patience:  $PATIENCE"
echo "  GPU:       $GPU_ID"
echo "  Output:    $WORK_DIR/yolo11m-tsr/"
echo ""

mkdir -p "$WORK_DIR"

CUDA_VISIBLE_DEVICES=$GPU_ID python3 -m ultralytics train \
    model="$MODEL" \
    data="$WORK_DIR/pubtables1m-tsr.yaml" \
    epochs="$EPOCHS" \
    batch="$BATCH" \
    imgsz="$IMGSZ" \
    patience="$PATIENCE" \
    workers="$WORKERS" \
    device=0 \
    project="$WORK_DIR" \
    name="yolo11m-tsr" \
    exist_ok=true \
    plots=true \
    val=true \
    save=true \
    save_period=10

echo ""
echo "Training complete."
echo ""

# ── Step 6: Validate best model ───────────────────────────────────────────
echo "============================================================"
echo "Step 6: Validate best model on test set"
echo "============================================================"

BEST_PT="$WORK_DIR/yolo11m-tsr/weights/best.pt"
if [ ! -f "$BEST_PT" ]; then
    echo "ERROR: best.pt not found at $BEST_PT"
    exit 1
fi

CUDA_VISIBLE_DEVICES=$GPU_ID python3 -m ultralytics val \
    model="$BEST_PT" \
    data="$WORK_DIR/pubtables1m-tsr.yaml" \
    split=test \
    imgsz="$IMGSZ" \
    device=0

echo ""

# ── Step 7: Export to ONNX ─────────────────────────────────────────────────
echo "============================================================"
echo "Step 7: Export to ONNX"
echo "============================================================"

CUDA_VISIBLE_DEVICES=$GPU_ID python3 "$SCRIPT_DIR/export_onnx.py" \
    --weights "$BEST_PT" \
    --output "$WORK_DIR/yolo11m-tsr/weights/best.onnx" \
    --imgsz "$IMGSZ" \
    --opset 17

echo ""

# ── Done ───────────────────────────────────────────────────────────────────
echo "============================================================"
echo "ALL DONE"
echo "============================================================"
echo ""
echo "Artifacts:"
echo "  Best weights (PT):   $BEST_PT"
echo "  Best weights (ONNX): $WORK_DIR/yolo11m-tsr/weights/best.onnx"
echo "  Training logs:       $WORK_DIR/yolo11m-tsr/"
echo ""
echo "RAGflow integration:"
echo "  cp $WORK_DIR/yolo11m-tsr/weights/best.onnx rag/res/deepdoc/tsr-yolo11.onnx"
echo "  # Then set environment variable: TSR_MODEL=yolov11"
echo ""
