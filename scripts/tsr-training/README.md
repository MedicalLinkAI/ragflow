# YOLO11m TSR Training Pipeline

Train a YOLO11m model on PubTables-1M for Table Structure Recognition (TSR), producing an ONNX model that can replace RAGflow's built-in YOLOv8 TSR model.

## Overview

| Item | Value |
|------|-------|
| **Task** | Table Structure Recognition (TSR) — detect rows, columns, headers, and spanning cells within table images |
| **Base model** | `yolo11m.pt` (20.1M params, COCO-pretrained) |
| **Dataset** | [PubTables-1M](https://github.com/microsoft/table-transformer) (~947K table images from PubMed) |
| **Classes** | 6 (table, table column, table row, table column header, table projected row header, table spanning cell) |
| **Output** | ONNX model compatible with RAGflow's `TableStructureRecognizer` |

### Why YOLO11?

- YOLO11m is the successor to YOLOv8m with improved accuracy and similar inference speed.
- The ONNX output tensor shape `[1, 11, 8400]` for 6 classes is schema-compatible with YOLOv8: RAGflow's existing post-processing code works without modification.
- PubTables-1M provides ~40× more training data than the default YOLO TSR model was trained on.

## Prerequisites

### Server Requirements

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| GPU | 1× A100/A800 40GB | 1× A800 80GB |
| VRAM | 24 GB (batch=16) | 40+ GB (batch=32) |
| System RAM | 32 GB | 64 GB |
| Disk space | 100 GB | 200 GB |
| CUDA | 11.8+ | 12.x |

### Target Server

- **Host**: 172.16.1.116
- **GPUs**: 4× NVIDIA A800 80GB (using GPU 2 to avoid conflicts)
- **CUDA**: 12.x

### Software

```bash
# Create a dedicated conda environment
conda create -n tsr-train python=3.11 -y
conda activate tsr-train

# Install PyTorch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Install Ultralytics (includes YOLO11 support)
pip install ultralytics>=8.3.0

# For dataset download
pip install huggingface_hub

# Verify
python3 -c "import ultralytics; print(ultralytics.__version__)"
python3 -c "import torch; print(torch.cuda.is_available())"
```

## Dataset: PubTables-1M

[PubTables-1M](https://arxiv.org/abs/2110.00061) (Smock et al., CVPR 2022) contains ~947K table images from PubMed scientific papers with fine-grained structure annotations.

### Splits

| Split | Images | Purpose |
|-------|--------|---------|
| train | ~758K | Training |
| val | ~95K | Validation during training |
| test | ~95K | Final evaluation |

### Classes (6 effective classes)

| ID | Name | Description |
|----|------|-------------|
| 0 | `table` | Full table bounding box |
| 1 | `table column` | Column region |
| 2 | `table row` | Row region |
| 3 | `table column header` | Column header region |
| 4 | `table projected row header` | Projected row header |
| 5 | `table spanning cell` | Cell spanning multiple rows/columns |

> **Note**: PubTables-1M also defines a 7th class `no object` (class ID 6) which is a DETR-specific artifact. It carries no annotations and is excluded from YOLO training. RAGflow's post-processing does a bounds check on `class_id` against `label_list`, so any class_id ≥ 6 would be safely ignored at inference time.

### Annotation Format

PubTables-1M provides PASCAL VOC XML annotations. The `convert_voc_to_yolo.py` script converts them to YOLO `.txt` format (one file per image, one line per object: `class_id cx cy w h`, all normalized to [0, 1]).

## Step-by-Step Instructions

### 1. Upload scripts to the training server

```bash
scp -r scripts/tsr-training/ user@172.16.1.116:/data/training/tsr-scripts/
ssh user@172.16.1.116
cd /data/training/tsr-scripts/
```

### 2. Download PubTables-1M

```bash
# Option A: HuggingFace Hub (handles resume, recommended)
python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('bsmock/pubtables-1m', local_dir='/data/datasets/pubtables1m-tsr', repo_type='dataset')
"

# Option B: Direct wget (if HF is slow)
mkdir -p /data/datasets/pubtables1m-tsr
cd /data/datasets/pubtables1m-tsr
wget -c https://huggingface.co/datasets/bsmock/pubtables-1m/resolve/main/PubTables-1M-Image_Table_Structure_PASCAL_VOC.tar.gz
wget -c https://huggingface.co/datasets/bsmock/pubtables-1m/resolve/main/PubTables-1M-Image_Table_Structure_Images.tar.gz
tar xzf PubTables-1M-Image_Table_Structure_PASCAL_VOC.tar.gz
tar xzf PubTables-1M-Image_Table_Structure_Images.tar.gz
```

**Expected directory structure after extraction:**

```
/data/datasets/pubtables1m-tsr/
├── images/
│   ├── train/   (~758K .jpg files)
│   ├── val/     (~95K .jpg files)
│   └── test/    (~95K .jpg files)
└── PubTables-1M-Structure_Table_Structure_PASCAL_VOC/
    ├── train/   (~758K .xml files)
    ├── val/     (~95K .xml files)
    └── test/    (~95K .xml files)
```

> If images are not in `images/{split}/`, create symlinks or move them accordingly. The YOLO data config expects `images/` and `labels/` directories at the dataset root.

### 3. Convert VOC to YOLO format

```bash
for split in train val test; do
  python3 convert_voc_to_yolo.py \
    --input-dir /data/datasets/pubtables1m-tsr/PubTables-1M-Structure_Table_Structure_PASCAL_VOC/$split \
    --output-dir /data/datasets/pubtables1m-tsr/labels/$split \
    --workers 8
done
```

**Expected output** (per split):

```
Found 758,849 XML files in .../train
Converting: 100%|████████████████| 758849/758849 [05:30<00:00]

============================================================
CONVERSION SUMMARY
============================================================
  Total XML files:          758,849
  Successful:               758,849
  Errors (skipped):               0
  Total annotations:      9,876,543

  Per-class annotation counts:
    [0] table                          758,849
    [1] table column                 3,456,789
    [2] table row                    4,321,098
    [3] table column header            654,321
    [4] table projected row header     123,456
    [5] table spanning cell            562,030
============================================================
```

### 4. Train the model

Run the all-in-one training script:

```bash
bash train_yolo11_tsr.sh
```

Or run training step only:

```bash
CUDA_VISIBLE_DEVICES=2 python3 -m ultralytics train \
    model=yolo11m.pt \
    data=pubtables1m-tsr.yaml \
    epochs=100 \
    batch=32 \
    imgsz=640 \
    patience=20 \
    workers=8 \
    device=0 \
    project=/data/training/tsr-yolo11 \
    name=yolo11m-tsr \
    exist_ok=true \
    plots=true \
    save_period=10
```

**Expected training time**: 8–12 hours on a single A800 80GB.

**Expected output**: Ultralytics prints per-epoch metrics. Watch for:
- `mAP50` converging above 0.90
- `mAP50-95` converging above 0.70
- Early stopping triggers after 20 epochs without improvement

### 5. Validate

```bash
CUDA_VISIBLE_DEVICES=2 python3 -m ultralytics val \
    model=/data/training/tsr-yolo11/yolo11m-tsr/weights/best.pt \
    data=pubtables1m-tsr.yaml \
    split=test \
    imgsz=640 \
    device=0
```

### 6. Export to ONNX

```bash
python3 export_onnx.py \
    --weights /data/training/tsr-yolo11/yolo11m-tsr/weights/best.pt \
    --output tsr-yolo11.onnx \
    --imgsz 640 \
    --opset 17
```

**Expected output file**: `tsr-yolo11.onnx` (~80 MB)

## ONNX Schema Compatibility

The YOLO11m ONNX model is **schema-compatible** with the YOLOv8 model that RAGflow already uses:

| Property | YOLOv8 (current) | YOLO11m (new) |
|----------|-------------------|---------------|
| Input tensor | `[1, 3, 640, 640]` | `[1, 3, 640, 640]` |
| Output tensor | `[1, N+5, 8400]` | `[1, N+5, 8400]` |
| N (classes) | 6 | 6 |
| Output shape | `[1, 11, 8400]` | `[1, 11, 8400]` |
| NMS | Post-hoc (in RAGflow) | Post-hoc (in RAGflow) |

RAGflow's `TableStructureRecognizer` already handles this output layout. No post-processing code changes are needed — only swap the ONNX file and set the model selector.

## RAGflow Integration

1. **Copy the ONNX model** to the RAGflow model directory:
   ```bash
   cp tsr-yolo11.onnx /path/to/ragflow/rag/res/deepdoc/tsr-yolo11.onnx
   ```

2. **Activate the model** via environment variable:
   ```bash
   export TSR_MODEL=yolov11
   ```
   Or set in RAGflow's `.env` / Docker Compose config.

3. **Verify** by uploading a PDF with tables and checking the table parsing results.

## Expected Metrics

Reference mAP scores from PubTables-1M benchmarks (Table Transformer paper):

| Model | mAP50 | mAP50-95 |
|-------|-------|----------|
| Table Transformer (DETR-based) | 0.970 | 0.790 |
| YOLOv8m (estimated baseline) | 0.950+ | 0.750+ |
| **YOLO11m (expected)** | **0.960+** | **0.770+** |

> Actual metrics will vary. YOLO models typically achieve slightly lower mAP than DETR-based models on this dataset but offer significantly faster inference.

## Troubleshooting

### CUDA Out of Memory (OOM)

Reduce batch size:
```bash
# batch=16 fits in ~24GB VRAM
CUDA_VISIBLE_DEVICES=2 python3 -m ultralytics train \
    model=yolo11m.pt data=pubtables1m-tsr.yaml batch=16 ...
```

Or use a smaller model:
```bash
# yolo11s.pt (9.4M params) uses ~60% less VRAM
model=yolo11s.pt batch=64
```

### HuggingFace Download Issues

```bash
# Use mirror (China)
export HF_ENDPOINT=https://hf-mirror.com
python3 -c "from huggingface_hub import snapshot_download; ..."

# Or use aria2 for faster multi-threaded download
pip install huggingface_hub[hf_transfer]
export HF_HUB_ENABLE_HF_TRANSFER=1
```

### Slow Data Loading

- Increase `--workers` to match CPU core count (but no more than 16).
- Ensure dataset is on a fast SSD/NVMe, not a network mount.
- Pre-cache: after the first epoch, Ultralytics caches label parsing.

### Training Not Converging

- Check that images and labels match (same basenames in `images/` and `labels/`).
- Verify label format: `class_id cx cy w h` with values in [0, 1].
- Run a quick sanity check:
  ```bash
  # Check a few label files
  head -5 /data/datasets/pubtables1m-tsr/labels/train/PMC1234567_table_0.txt
  # Expected: lines like "2 0.500000 0.123456 0.980000 0.045678"
  ```

### ONNX Export Fails

- Ensure `onnxsim` is installed: `pip install onnxsim`
- Try without simplification: set `simplify=False`
- Try a lower opset: `--opset 13`

## Files in This Directory

| File | Purpose |
|------|---------|
| `convert_voc_to_yolo.py` | Convert PubTables-1M PASCAL VOC XML → YOLO txt labels |
| `pubtables1m-tsr.yaml` | Ultralytics dataset configuration |
| `train_yolo11_tsr.sh` | End-to-end training script (download → convert → train → export) |
| `export_onnx.py` | Standalone ONNX export script |
| `README.md` | This documentation |
