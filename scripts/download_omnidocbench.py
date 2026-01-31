#!/usr/bin/env python3
"""
Download OmniDocBench dataset for PDF parser evaluation.

Usage:
    python scripts/download_omnidocbench.py --max-samples 100
    python scripts/download_omnidocbench.py --max-samples 1355  # Full dataset
"""

import argparse
import json
from pathlib import Path
from datasets import load_dataset


def download_dataset(max_samples: int = 100, cache_dir: str = "./data/omnidocbench"):
    """
    Download OmniDocBench dataset from HuggingFace.
    
    Args:
        max_samples: Number of samples to download (default: 100, max: 1355)
        cache_dir: Directory to cache downloaded data
    """
    print(f"Downloading OmniDocBench dataset (max {max_samples} samples)...")
    print(f"Cache directory: {cache_dir}")
    
    # Create cache directory
    Path(cache_dir).mkdir(parents=True, exist_ok=True)
    
    # Download dataset
    dataset = load_dataset(
        "opendatalab/OmniDocBench",
        cache_dir=cache_dir,
        trust_remote_code=True
    )
    
    # Extract test split
    test_data = dataset['test']
    
    # Limit samples if specified
    if max_samples < len(test_data):
        test_data = test_data.select(range(max_samples))
    
    print(f"✓ Downloaded {len(test_data)} samples")
    
    # Save metadata
    metadata_path = Path(cache_dir) / "metadata.json"
    metadata = {
        "total_samples": len(test_data),
        "dataset_name": "OmniDocBench",
        "dataset_url": "https://huggingface.co/datasets/opendatalab/OmniDocBench",
        "features": list(test_data.features.keys()),
    }
    
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Saved metadata to {metadata_path}")
    print(f"\nDataset features: {metadata['features']}")
    
    return test_data


def main():
    parser = argparse.ArgumentParser(description="Download OmniDocBench dataset")
    parser.add_argument(
        "--max-samples",
        type=int,
        default=100,
        help="Maximum number of samples to download (default: 100, max: 1355)"
    )
    parser.add_argument(
        "--cache-dir",
        type=str,
        default="./data/omnidocbench",
        help="Cache directory for downloaded data"
    )
    
    args = parser.parse_args()
    
    # Validate max_samples
    if args.max_samples < 1:
        print("Error: --max-samples must be >= 1")
        return 1
    
    if args.max_samples > 1355:
        print(f"Warning: OmniDocBench has only 1355 samples, limiting to 1355")
        args.max_samples = 1355
    
    # Download
    download_dataset(args.max_samples, args.cache_dir)
    
    print("\n✓ Done! You can now run validate_with_omnidocbench.py")
    return 0


if __name__ == "__main__":
    exit(main())
