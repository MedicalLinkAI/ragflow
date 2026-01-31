#!/bin/bash
#
# One-click deployment script for RAGflow evaluation on 5090 GPU server
#
# Usage:
#   bash scripts/deploy_to_5090.sh
#
# Prerequisites:
#   - NVIDIA GPU with CUDA installed
#   - Python 3.11+
#   - Git
#

set -e

echo "========================================"
echo "RAGflow 5090 Deployment Script"
echo "========================================"

# Configuration
WORKSPACE_DIR="/workspace/ragflow-eval"
REPO_URL="git@github.com:redleaves/ragflow.git"
BRANCH="develop"
PYTHON_VERSION="python3.11"

# Step 1: Check prerequisites
echo ""
echo "=== Step 1: Checking prerequisites ==="

# Check NVIDIA GPU
if ! command -v nvidia-smi &> /dev/null; then
    echo "Error: nvidia-smi not found. Please install NVIDIA drivers."
    exit 1
fi

echo "✓ NVIDIA GPU detected:"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader

# Check CUDA
if ! command -v nvcc &> /dev/null; then
    echo "Warning: nvcc not found. CUDA may not be properly installed."
else
    echo "✓ CUDA version:"
    nvcc --version | grep "release"
fi

# Check Python
if ! command -v $PYTHON_VERSION &> /dev/null; then
    echo "Error: $PYTHON_VERSION not found. Please install Python 3.11+."
    exit 1
fi

echo "✓ Python version:"
$PYTHON_VERSION --version

# Check Git
if ! command -v git &> /dev/null; then
    echo "Error: git not found. Please install git."
    exit 1
fi

echo "✓ Git version:"
git --version

# Step 2: Clone or update repository
echo ""
echo "=== Step 2: Setting up codebase ==="

if [ -d "$WORKSPACE_DIR" ]; then
    echo "Directory $WORKSPACE_DIR already exists. Updating..."
    cd "$WORKSPACE_DIR"
    git fetch origin
    git checkout $BRANCH
    git pull origin $BRANCH
else
    echo "Cloning repository to $WORKSPACE_DIR..."
    mkdir -p "$(dirname $WORKSPACE_DIR)"
    git clone -b $BRANCH $REPO_URL $WORKSPACE_DIR
    cd "$WORKSPACE_DIR"
fi

echo "✓ Current commit:"
git log -1 --oneline

# Step 3: Set up Python environment
echo ""
echo "=== Step 3: Setting up Python environment ==="

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_VERSION -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "✓ Python in venv:"
which python
python --version

# Step 4: Install dependencies
echo ""
echo "=== Step 4: Installing dependencies ==="

echo "Upgrading pip..."
pip install --upgrade pip -q

echo "Installing RAGflow core dependencies..."
pip install -e . -q

echo "Installing DeepSeek-OCR2 dependencies..."
pip install -e .[deepseek-ocr2] -q

echo "Installing MinerU..."
pip install magic-pdf -q

echo "Installing Docling..."
pip install docling -q

echo "Installing OmniDocBench evaluation dependencies..."
pip install datasets tabulate psutil matplotlib seaborn -q

echo "✓ Dependencies installed"

# Step 5: Clone OmniDocBench evaluation toolkit
echo ""
echo "=== Step 5: Setting up OmniDocBench toolkit ==="

if [ ! -d "OmniDocBench" ]; then
    echo "Cloning OmniDocBench..."
    git clone https://github.com/opendatalab/OmniDocBench.git
    cd OmniDocBench
    pip install -r requirements.txt -q
    cd ..
else
    echo "✓ OmniDocBench already exists"
fi

# Step 6: Verify GPU accessibility
echo ""
echo "=== Step 6: Verifying GPU accessibility ==="

python -c "
import torch
print(f'PyTorch version: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'CUDA version: {torch.version.cuda}')
    print(f'GPU name: {torch.cuda.get_device_name(0)}')
    print(f'GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB')
else:
    print('ERROR: CUDA not available!')
    exit(1)
"

echo "✓ GPU verified"

# Step 7: Download OmniDocBench dataset (test subset first)
echo ""
echo "=== Step 7: Downloading OmniDocBench test dataset ==="

echo "Downloading 100 sample subset for quick test..."
python scripts/download_omnidocbench.py --max-samples 100

echo "✓ Dataset downloaded"

# Step 8: Verify RAGflow parsers
echo ""
echo "=== Step 8: Verifying RAGflow parsers ==="

python -c "
import sys
sys.path.insert(0, '.')
from rag.app.naive import PARSERS
print('Available parsers:')
for name in PARSERS.keys():
    print(f'  - {name}')
" || {
    echo "Error: Failed to import RAGflow parsers"
    exit 1
}

echo "✓ Parsers verified"

# Done
echo ""
echo "========================================"
echo "✓ Deployment complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Quick test (100 samples, ~30 min):"
echo "   cd $WORKSPACE_DIR"
echo "   source .venv/bin/activate"
echo "   python scripts/validate_with_omnidocbench.py --max-samples 100"
echo ""
echo "2. Full evaluation (1355 samples, ~4-6 hours):"
echo "   python scripts/validate_with_omnidocbench.py --max-samples 1355"
echo ""
echo "3. Specific parsers only:"
echo "   python scripts/validate_with_omnidocbench.py --parsers deepdoc,deepseek-ocr2"
echo ""
