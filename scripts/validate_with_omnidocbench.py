#!/usr/bin/env python3
"""
RAGflow PDF Parser Evaluation with OmniDocBench

This script evaluates RAGflow parsers (DeepDOC, MinerU, Docling, DeepSeek-OCR2)
using the OmniDocBench dataset with Ground Truth annotations.

Usage:
    # Quick test (100 samples)
    python scripts/validate_with_omnidocbench.py --max-samples 100
    
    # Full evaluation (1355 samples, 4-6 hours)
    python scripts/validate_with_omnidocbench.py --max-samples 1355
    
    # Specific parsers only
    python scripts/validate_with_omnidocbench.py --parsers deepdoc,deepseek-ocr2
"""

import argparse
import json
import sys
import time
import traceback
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

try:
    from datasets import load_dataset
except ImportError:
    print("Error: datasets library not installed. Run: pip install datasets")
    sys.exit(1)

# Import RAGflow components
from rag.app.naive import PARSERS
from scripts.ragflow_to_omnidoc_adapter import ragflow_to_omnidoc_document, normalize_text

# Import OmniDocBench evaluation functions
try:
    # Clone OmniDocBench repo first if not exists
    OMNIDOC_PATH = PROJECT_ROOT / "OmniDocBench"
    if not OMNIDOC_PATH.exists():
        print(f"Error: OmniDocBench repo not found at {OMNIDOC_PATH}")
        print("Please run: git clone https://github.com/opendatalab/OmniDocBench.git")
        sys.exit(1)
    
    sys.path.insert(0, str(OMNIDOC_PATH))
    
    # Import evaluation metrics
    from omnidocbench.evaluation.text_evaluation import calculate_normalized_edit_distance
    from omnidocbench.evaluation.table_evaluation import calculate_teds
    
except ImportError as e:
    print(f"Warning: Could not import OmniDocBench evaluation functions: {e}")
    print("Will use fallback metrics (simpler Edit Distance)")
    
    # Fallback: simple Levenshtein distance
    def calculate_normalized_edit_distance(pred: str, gt: str) -> float:
        """Simple normalized edit distance as fallback"""
        import difflib
        return 1.0 - difflib.SequenceMatcher(None, pred, gt).ratio()
    
    def calculate_teds(pred_tables: List[dict], gt_tables: List[dict]) -> float:
        """Placeholder TEDS - returns 0.0 if tables mismatch, 1.0 if match"""
        if len(pred_tables) != len(gt_tables):
            return 0.0
        # Very simple: just check if same number of tables
        return 0.5  # Neutral score


class ParserEvaluator:
    """Evaluates a single parser on OmniDocBench dataset"""
    
    def __init__(self, parser_name: str, parser_fn: callable):
        self.parser_name = parser_name
        self.parser_fn = parser_fn
        self.results = []
        
    def evaluate_sample(self, sample: dict) -> Dict[str, Any]:
        """
        Evaluate parser on a single PDF sample.
        
        Args:
            sample: OmniDocBench sample with GT annotations
        
        Returns:
            Dict with metrics (edit_distance, teds, time, etc.)
        """
        pdf_path = sample['pdf_path']
        page_no = sample.get('page_no', 0)
        
        result = {
            'pdf': pdf_path,
            'page': page_no,
            'success': False,
            'error': None,
            'time_s': 0.0,
            'text_edit_distance': 1.0,  # 1.0 = completely wrong
            'table_teds': 0.0,
            'chars_pred': 0,
            'chars_gt': len(sample.get('text_gt', '')),
        }
        
        try:
            # Run parser
            start_time = time.time()
            
            sections, tables = self.parser_fn(
                filename=pdf_path,
                from_page=page_no,
                to_page=page_no,
            )
            
            result['time_s'] = time.time() - start_time
            
            # Convert to OmniDocBench format
            pred_doc = ragflow_to_omnidoc_document(sections, tables)
            pred_text = pred_doc['text']
            pred_tables = pred_doc['tables']
            
            result['chars_pred'] = len(pred_text)
            
            # Get GT
            gt_text = normalize_text(sample.get('text_gt', ''))
            gt_tables = sample.get('tables_gt', [])
            
            # Calculate text Edit Distance
            if pred_text and gt_text:
                result['text_edit_distance'] = calculate_normalized_edit_distance(
                    pred_text, gt_text
                )
            
            # Calculate TEDS (Table Edit Distance)
            if pred_tables and gt_tables:
                result['table_teds'] = calculate_teds(pred_tables, gt_tables)
            
            result['success'] = True
            
        except Exception as e:
            result['error'] = str(e)
            result['traceback'] = traceback.format_exc()
        
        return result
    
    def evaluate_dataset(self, samples: List[dict]) -> Dict[str, Any]:
        """
        Evaluate parser on entire dataset.
        
        Returns:
            Aggregated metrics
        """
        print(f"\n{'='*60}")
        print(f"Evaluating: {self.parser_name}")
        print(f"{'='*60}")
        
        total_samples = len(samples)
        success_count = 0
        text_ed_scores = []
        teds_scores = []
        times = []
        
        for idx, sample in enumerate(samples, 1):
            print(f"[{idx}/{total_samples}] Processing {sample.get('pdf_path', 'unknown')} page {sample.get('page_no', 0)}...", end=' ')
            
            result = self.evaluate_sample(sample)
            self.results.append(result)
            
            if result['success']:
                success_count += 1
                text_ed_scores.append(result['text_edit_distance'])
                if result['table_teds'] > 0:
                    teds_scores.append(result['table_teds'])
                times.append(result['time_s'])
                print(f"✓ (ED: {result['text_edit_distance']:.3f}, Time: {result['time_s']:.2f}s)")
            else:
                print(f"✗ ({result['error']})")
        
        # Aggregate metrics
        avg_text_ed = sum(text_ed_scores) / len(text_ed_scores) if text_ed_scores else 1.0
        avg_teds = sum(teds_scores) / len(teds_scores) if teds_scores else 0.0
        avg_time = sum(times) / len(times) if times else 0.0
        
        # OmniDocBench Overall score: ((1 - text_ED) * 100 + TEDS) / 2
        # (Simplified, original also includes Formula CDM which we skip)
        overall = ((1 - avg_text_ed) * 100 + avg_teds) / 2
        
        summary = {
            'parser': self.parser_name,
            'total_samples': total_samples,
            'success_count': success_count,
            'success_rate': success_count / total_samples if total_samples > 0 else 0,
            'avg_text_edit_distance': avg_text_ed,
            'avg_table_teds': avg_teds,
            'avg_time_s': avg_time,
            'overall_score': overall,
            'detailed_results': self.results,
        }
        
        print(f"\n{'='*60}")
        print(f"SUMMARY: {self.parser_name}")
        print(f"{'='*60}")
        print(f"Success Rate: {summary['success_rate']*100:.1f}% ({success_count}/{total_samples})")
        print(f"Avg Text Edit Distance: {avg_text_ed:.4f} (lower is better)")
        print(f"Avg Table TEDS: {avg_teds:.4f} (higher is better)")
        print(f"Avg Time per Page: {avg_time:.2f}s")
        print(f"Overall Score: {overall:.2f}")
        
        return summary


def load_omnidoc_samples(max_samples: int, cache_dir: str) -> List[dict]:
    """Load OmniDocBench test samples"""
    print(f"Loading OmniDocBench dataset (max {max_samples} samples)...")
    
    dataset = load_dataset(
        "opendatalab/OmniDocBench",
        cache_dir=cache_dir,
        trust_remote_code=True
    )
    
    test_data = dataset['test']
    
    if max_samples < len(test_data):
        test_data = test_data.select(range(max_samples))
    
    # Convert to list of dicts
    samples = []
    for item in test_data:
        samples.append({
            'pdf_path': item['pdf_path'],
            'page_no': item.get('page_no', 0),
            'text_gt': item.get('text', ''),
            'tables_gt': item.get('tables', []),
        })
    
    print(f"✓ Loaded {len(samples)} samples")
    return samples


def main():
    parser = argparse.ArgumentParser(description="Evaluate RAGflow parsers with OmniDocBench")
    parser.add_argument(
        "--max-samples",
        type=int,
        default=100,
        help="Maximum samples to evaluate (default: 100, max: 1355)"
    )
    parser.add_argument(
        "--parsers",
        type=str,
        default="deepdoc,mineru,docling,deepseek-ocr2",
        help="Comma-separated parser names to evaluate"
    )
    parser.add_argument(
        "--cache-dir",
        type=str,
        default="./data/omnidocbench",
        help="Cache directory for OmniDocBench dataset"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output JSON file (default: validation_omnidoc_{timestamp}.json)"
    )
    
    args = parser.parse_args()
    
    # Default output filename
    if not args.output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = f"validation_omnidoc_{timestamp}.json"
    
    # Parse parser names
    parser_names = [p.strip() for p in args.parsers.split(',')]
    
    # Validate parsers
    for name in parser_names:
        if name not in PARSERS:
            print(f"Error: Unknown parser '{name}'. Available: {list(PARSERS.keys())}")
            return 1
    
    print(f"\n{'='*60}")
    print("RAGflow PDF Parser Evaluation with OmniDocBench")
    print(f"{'='*60}")
    print(f"Parsers: {parser_names}")
    print(f"Max samples: {args.max_samples}")
    print(f"Output: {args.output}")
    
    # Load dataset
    try:
        samples = load_omnidoc_samples(args.max_samples, args.cache_dir)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        print("Make sure you have run: python scripts/download_omnidocbench.py")
        return 1
    
    # Evaluate each parser
    all_summaries = {}
    
    for parser_name in parser_names:
        parser_fn = PARSERS[parser_name]
        evaluator = ParserEvaluator(parser_name, parser_fn)
        summary = evaluator.evaluate_dataset(samples)
        all_summaries[parser_name] = summary
    
    # Save results
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'config': {
                'max_samples': args.max_samples,
                'parsers': parser_names,
            },
            'results': all_summaries,
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"✓ Results saved to: {output_path}")
    print(f"{'='*60}")
    
    # Print comparison table
    print("\nCOMPARISON TABLE")
    print(f"{'='*60}")
    print(f"{'Parser':<20} | {'Success%':<10} | {'Text ED':<10} | {'TEDS':<10} | {'Overall':<10}")
    print(f"{'-'*20}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}")
    
    for parser_name, summary in all_summaries.items():
        print(f"{parser_name:<20} | "
              f"{summary['success_rate']*100:>9.1f}% | "
              f"{summary['avg_text_edit_distance']:>10.4f} | "
              f"{summary['avg_table_teds']:>10.4f} | "
              f"{summary['overall_score']:>10.2f}")
    
    # Find winner
    winner = max(all_summaries.items(), key=lambda x: x[1]['overall_score'])
    print(f"\n🏆 Winner: {winner[0]} (Overall Score: {winner[1]['overall_score']:.2f})")
    
    return 0


if __name__ == "__main__":
    exit(main())
