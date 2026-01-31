#!/usr/bin/env python3
"""
Generate comparison reports from OmniDocBench evaluation results.

Outputs:
- Markdown table
- Heatmap visualization
- Per-parser detailed CSV

Usage:
    python scripts/generate_report.py validation_omnidoc_20260131_123456.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any

try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    PLOTTING_AVAILABLE = True
except ImportError:
    print("Warning: matplotlib/seaborn/pandas not installed. Visualizations disabled.")
    PLOTTING_AVAILABLE = False


def load_results(json_path: str) -> Dict[str, Any]:
    """Load evaluation results from JSON"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_markdown_table(results: Dict[str, Any], output_path: str):
    """Generate Markdown comparison table"""
    
    lines = [
        "# RAGflow PDF Parser Comparison (OmniDocBench)\n",
        f"**Evaluation Date:** {results['timestamp']}\n",
        f"**Samples:** {results['config']['max_samples']}\n",
        "\n## Overall Comparison\n",
        "| Parser | Success Rate | Text Edit Distance ↓ | Table TEDS ↑ | Avg Time (s) | Overall Score ↑ |",
        "|--------|--------------|---------------------|--------------|--------------|----------------|",
    ]
    
    # Sort by overall score (descending)
    sorted_results = sorted(
        results['results'].items(),
        key=lambda x: x[1]['overall_score'],
        reverse=True
    )
    
    for parser_name, metrics in sorted_results:
        lines.append(
            f"| **{parser_name}** | "
            f"{metrics['success_rate']*100:.1f}% | "
            f"{metrics['avg_text_edit_distance']:.4f} | "
            f"{metrics['avg_table_teds']:.4f} | "
            f"{metrics['avg_time_s']:.2f} | "
            f"**{metrics['overall_score']:.2f}** |"
        )
    
    lines.append("\n## Metric Explanations\n")
    lines.append("- **Success Rate**: % of pages successfully parsed")
    lines.append("- **Text Edit Distance**: Normalized edit distance (0=perfect, 1=completely wrong)")
    lines.append("- **Table TEDS**: Table Edit Distance-based Similarity (0=wrong, 1=perfect)")
    lines.append("- **Overall Score**: `((1 - Text_ED) * 100 + TEDS) / 2`")
    
    lines.append("\n## Winner 🏆\n")
    winner_name, winner_metrics = sorted_results[0]
    lines.append(f"**{winner_name}** with Overall Score of **{winner_metrics['overall_score']:.2f}**\n")
    
    # Write
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"✓ Markdown table saved to: {output_path}")


def generate_heatmap(results: Dict[str, Any], output_path: str):
    """Generate heatmap visualization"""
    
    if not PLOTTING_AVAILABLE:
        print("✗ Heatmap skipped (matplotlib/seaborn not installed)")
        return
    
    # Prepare data
    parsers = []
    metrics_data = {
        'Success Rate': [],
        'Text Accuracy': [],  # 1 - ED
        'Table TEDS': [],
        'Speed': [],  # 1 / time (inverted, higher is better)
    }
    
    for parser_name, metrics in results['results'].items():
        parsers.append(parser_name)
        metrics_data['Success Rate'].append(metrics['success_rate'] * 100)
        metrics_data['Text Accuracy'].append((1 - metrics['avg_text_edit_distance']) * 100)
        metrics_data['Table TEDS'].append(metrics['avg_table_teds'] * 100)
        
        # Speed: normalize to 0-100 (faster = higher score)
        avg_time = metrics['avg_time_s']
        speed_score = min(100, (1.0 / avg_time) * 10) if avg_time > 0 else 0
        metrics_data['Speed'].append(speed_score)
    
    # Create DataFrame
    df = pd.DataFrame(metrics_data, index=parsers)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(
        df.T,
        annot=True,
        fmt='.1f',
        cmap='RdYlGn',
        cbar_kws={'label': 'Score (0-100)'},
        ax=ax,
        vmin=0,
        vmax=100,
    )
    
    ax.set_title('RAGflow PDF Parser Comparison (OmniDocBench)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Parser', fontsize=12)
    ax.set_ylabel('Metric', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Heatmap saved to: {output_path}")


def generate_detailed_csv(results: Dict[str, Any], output_dir: str):
    """Generate per-parser detailed CSV files"""
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for parser_name, metrics in results['results'].items():
        csv_path = output_dir / f"{parser_name}_detailed.csv"
        
        # Extract detailed results
        detailed = metrics.get('detailed_results', [])
        if not detailed:
            continue
        
        # Write CSV
        with open(csv_path, 'w', encoding='utf-8') as f:
            # Header
            f.write("pdf,page,success,time_s,text_edit_distance,table_teds,chars_pred,chars_gt,error\n")
            
            # Rows
            for result in detailed:
                f.write(
                    f"{result.get('pdf', 'N/A')},"
                    f"{result.get('page', 0)},"
                    f"{result.get('success', False)},"
                    f"{result.get('time_s', 0.0):.2f},"
                    f"{result.get('text_edit_distance', 1.0):.4f},"
                    f"{result.get('table_teds', 0.0):.4f},"
                    f"{result.get('chars_pred', 0)},"
                    f"{result.get('chars_gt', 0)},"
                    f"\"{result.get('error', '')}\"\n"
                )
        
        print(f"✓ Detailed CSV saved to: {csv_path}")


def generate_recommendation(results: Dict[str, Any], output_path: str):
    """Generate scenario-based recommendation"""
    
    # Analyze results
    parsers_by_metric = {}
    
    for parser_name, metrics in results['results'].items():
        if parser_name not in parsers_by_metric:
            parsers_by_metric[parser_name] = {}
        
        parsers_by_metric[parser_name]['text_accuracy'] = 1 - metrics['avg_text_edit_distance']
        parsers_by_metric[parser_name]['table_accuracy'] = metrics['avg_table_teds']
        parsers_by_metric[parser_name]['speed'] = 1.0 / metrics['avg_time_s'] if metrics['avg_time_s'] > 0 else 0
        parsers_by_metric[parser_name]['overall'] = metrics['overall_score']
    
    # Find best for each scenario
    best_overall = max(parsers_by_metric.items(), key=lambda x: x[1]['overall'])
    best_text = max(parsers_by_metric.items(), key=lambda x: x[1]['text_accuracy'])
    best_table = max(parsers_by_metric.items(), key=lambda x: x[1]['table_accuracy'])
    best_speed = max(parsers_by_metric.items(), key=lambda x: x[1]['speed'])
    
    lines = [
        "# RAGflow PDF Parser Recommendation\n",
        f"Based on OmniDocBench evaluation ({results['config']['max_samples']} samples)\n",
        "\n## 🏆 Best Overall\n",
        f"**{best_overall[0]}** (Score: {best_overall[1]['overall']:.2f})\n",
        "- Use this as default for balanced performance\n",
        "\n## 📝 Best for Text-Heavy Documents\n",
        f"**{best_text[0]}** (Accuracy: {best_text[1]['text_accuracy']*100:.1f}%)\n",
        "- Ideal for: Academic papers, reports, long-form articles\n",
        "\n## 📊 Best for Table-Heavy Documents\n",
        f"**{best_table[0]}** (TEDS: {best_table[1]['table_accuracy']:.3f})\n",
        "- Ideal for: Financial reports, spreadsheets, data tables\n",
        "\n## ⚡ Best for Speed\n",
        f"**{best_speed[0]}** (Speed score: {best_speed[1]['speed']:.2f})\n",
        "- Ideal for: Batch processing, real-time applications\n",
        "\n## 📋 Full Comparison\n",
        "| Parser | Text Acc | Table Acc | Speed | Overall |",
        "|--------|----------|-----------|-------|---------|",
    ]
    
    for parser_name, metrics in sorted(parsers_by_metric.items(), key=lambda x: x[1]['overall'], reverse=True):
        lines.append(
            f"| {parser_name} | "
            f"{metrics['text_accuracy']*100:.1f}% | "
            f"{metrics['table_accuracy']*100:.1f}% | "
            f"{metrics['speed']:.2f} | "
            f"{metrics['overall']:.2f} |"
        )
    
    # Write
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"✓ Recommendation saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate comparison reports from OmniDocBench results")
    parser.add_argument(
        "json_file",
        help="Path to validation results JSON file"
    )
    parser.add_argument(
        "--output-dir",
        default="./reports",
        help="Output directory for reports (default: ./reports)"
    )
    
    args = parser.parse_args()
    
    # Load results
    print(f"Loading results from: {args.json_file}")
    results = load_results(args.json_file)
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\nGenerating reports in: {output_dir}")
    
    # Generate reports
    generate_markdown_table(results, output_dir / "comparison_table.md")
    generate_heatmap(results, output_dir / "comparison_heatmap.png")
    generate_detailed_csv(results, output_dir / "detailed")
    generate_recommendation(results, output_dir / "recommendation.md")
    
    print(f"\n✓ All reports generated in: {output_dir}")
    print("\nGenerated files:")
    print(f"  - comparison_table.md")
    print(f"  - comparison_heatmap.png")
    print(f"  - recommendation.md")
    print(f"  - detailed/<parser>_detailed.csv")
    
    return 0


if __name__ == "__main__":
    exit(main())
