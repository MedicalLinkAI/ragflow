#!/usr/bin/env python3
"""
PDF Parser Comparative Validation Script

Compare 4 PDF parsers: DeepDOC, MinerU, Docling, DeepSeek-OCR2
Outputs quantitative metrics for objective evaluation.

Usage:
    cd ragflow/.worktrees/feature-deepseek-ocr2
    source .venv/bin/activate
    python scripts/validate_parsers.py --install-deps
    python scripts/validate_parsers.py "/Users/weixiaofeng/Desktop/中诚信"
"""

import os
import sys
import subprocess
import time
import json
import traceback
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


def install_dependencies():
    """Install required dependencies for validation.

    Note: this is intentionally "lightweight" (script dependencies + common PDF libs).
    Full RAGFlow runtime deps should be installed via the repo's normal install path.
    """
    deps = [
        "psutil",
        "tabulate",
        "PyMuPDF",
        "pypdf",
        "pdfplumber",
        "Pillow",
        "numpy",
        "beartype",  # required by deepdoc/__init__.py
        "python-docx",  # optional, but avoid import surprises
        "docling",  # IBM Docling parser
    ]
    print("Installing required dependencies...")
    for dep in deps:
        print(f"  Installing {dep}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", dep, "-q"], 
                               capture_output=True, text=True)
        if result.returncode != 0:
            print(f"    Warning: {dep} installation may have issues")
    print("Dependencies installed!\n")


def _pop_flag(flag: str) -> bool:
    if flag in sys.argv:
        sys.argv.remove(flag)
        return True
    return False


# Check for --install-deps flag
if _pop_flag("--install-deps"):
    install_dependencies()


try:
    import psutil
except ImportError:
    psutil = None
    print("Warning: psutil not installed. Run with --install-deps")

try:
    from tabulate import tabulate
except ImportError:
    tabulate = None
    print("Warning: tabulate not installed. Run with --install-deps")


class ParserResult:
    """Container for parser output metrics"""
    def __init__(self, name: str):
        self.name = name
        self.success = False
        self.error_msg = ""
        self.time_seconds = 0.0
        self.memory_mb = 0.0
        self.text_length = 0
        self.sections_count = 0
        self.tables_count = 0
        self.sample_text = ""
        self.raw_output = None
        
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "success": self.success,
            "error": self.error_msg,
            "time_s": round(self.time_seconds, 2),
            "memory_mb": round(self.memory_mb, 1),
            "chars": self.text_length,
            "sections": self.sections_count,
            "tables": self.tables_count,
        }


def get_memory_usage() -> float:
    """Get current process RSS memory in MB (best-effort)."""
    if psutil:
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024
    return 0.0


def validate_deepdoc(pdf_path: str) -> ParserResult:
    """Validate DeepDOC parser (RAGFlow native PDF parser)."""
    result = ParserResult("DeepDOC")
    try:
        mem_before = get_memory_usage()
        start = time.time()

        # IMPORTANT: Use the same core parser implementation RAGFlow uses for PDFs.
        # Avoid importing deepdoc.parser (which may pull optional deps).
        try:
            from deepdoc.parser.pdf_parser import RAGFlowPdfParser
        except ModuleNotFoundError as e:
            result.error_msg = (
                f"RAGFlow deps missing: {e}. "
                "Run: python3 scripts/validate_parsers.py --install-deps <pdf_or_dir> "
                "or install RAGFlow requirements (recommended for real comparison)."
            )
            return result

        parser = RAGFlowPdfParser()
        bboxes, tables = parser(pdf_path, need_image=False)

        # Flatten bboxes -> text
        full_text_parts = []
        sections = 0
        for page_bxs in (bboxes or []):
            page_text = "".join((bx.get("text") or "") for bx in (page_bxs or []) if isinstance(bx, dict))
            if page_text.strip():
                sections += 1
                full_text_parts.append(page_text)

        full_text = "\n".join(full_text_parts)

        result.time_seconds = time.time() - start
        result.memory_mb = max(0.0, get_memory_usage() - mem_before)
        result.text_length = len(full_text)
        result.sections_count = sections
        result.tables_count = len(tables) if tables else 0
        result.sample_text = full_text[:500] if full_text else ""

        if result.text_length == 0:
            result.success = False
            result.error_msg = "DeepDOC produced empty text"
        else:
            result.success = True

    except Exception as e:
        result.error_msg = str(e)
        traceback.print_exc()

    return result


def validate_mineru(pdf_path: str) -> ParserResult:
    """Validate MinerU parser"""
    result = ParserResult("MinerU")
    try:
        # Check if MinerU is available
        try:
            from magic_pdf.pipe.UNIPipe import UNIPipe
            from magic_pdf.rw.DiskReaderWriter import DiskReaderWriter
        except ImportError:
            result.error_msg = "MinerU not installed (pip install magic-pdf)"
            return result
        
        mem_before = get_memory_usage()
        start = time.time()
        
        # MinerU parsing logic
        with open(pdf_path, 'rb') as f:
            pdf_bytes = f.read()
        
        output_dir = f"/tmp/mineru_output_{os.getpid()}"
        os.makedirs(output_dir, exist_ok=True)
        
        pipe = UNIPipe(pdf_bytes, jso_useful_key={})
        pipe.pipe_classify()
        pipe.pipe_analyze()
        pipe.pipe_parse()
        
        md_content = pipe.pipe_mk_markdown(output_dir, DiskReaderWriter(output_dir))
        
        result.time_seconds = time.time() - start
        result.memory_mb = get_memory_usage() - mem_before
        result.text_length = len(md_content) if md_content else 0
        result.sections_count = md_content.count('\n#') if md_content else 0
        result.tables_count = md_content.count('|---|') if md_content else 0
        result.sample_text = md_content[:500] if md_content else ""
        result.success = True
        
    except Exception as e:
        result.error_msg = str(e)
        traceback.print_exc()
    
    return result


def validate_docling(pdf_path: str) -> ParserResult:
    """Validate Docling parser"""
    result = ParserResult("Docling")
    try:
        try:
            from docling.document_converter import DocumentConverter
        except ImportError:
            result.error_msg = "Docling not installed (pip install docling)"
            return result
        
        mem_before = get_memory_usage()
        start = time.time()
        
        converter = DocumentConverter()
        doc_result = converter.convert(pdf_path)
        md_content = doc_result.document.export_to_markdown()
        
        result.time_seconds = time.time() - start
        result.memory_mb = get_memory_usage() - mem_before
        result.text_length = len(md_content) if md_content else 0
        result.sections_count = md_content.count('\n#') if md_content else 0
        result.tables_count = md_content.count('|---|') if md_content else 0
        result.sample_text = md_content[:500] if md_content else ""
        result.success = True
        
    except Exception as e:
        result.error_msg = str(e)
        traceback.print_exc()
    
    return result


def validate_deepseek_ocr2(pdf_path: str) -> ParserResult:
    """Validate DeepSeek-OCR2 parser."""
    result = ParserResult("DeepSeek-OCR2")
    try:
        mem_before = get_memory_usage()
        start = time.time()

        try:
            from deepdoc.parser.deepseek_ocr2_parser import DeepSeekOcr2Parser
        except ModuleNotFoundError as e:
            result.error_msg = (
                f"RAGFlow deps missing: {e}. "
                "Run with --install-deps, then install torch+transformers on GPU host."
            )
            return result

        parser = DeepSeekOcr2Parser(
            backend=os.environ.get("DEEPSEEK_OCR2_BACKEND", "local"),
            api_url=os.environ.get("DEEPSEEK_OCR2_API_URL"),
            api_key=os.environ.get("DEEPSEEK_OCR2_API_KEY"),
        )

        ok, reason = parser.check_available()
        if not ok:
            result.error_msg = reason or "DeepSeek-OCR2 not available"
            return result

        sections, tables = parser.parse_pdf(pdf_path)

        result.time_seconds = time.time() - start
        result.memory_mb = max(0.0, get_memory_usage() - mem_before)

        full_text_parts = []
        for sec in (sections or []):
            if isinstance(sec, dict) and "text" in sec:
                full_text_parts.append(sec["text"] or "")
            elif isinstance(sec, str):
                full_text_parts.append(sec)

        full_text = "\n".join(t for t in full_text_parts if t)
        result.text_length = len(full_text)
        result.sections_count = len(sections) if sections else 0
        result.tables_count = len(tables) if tables else 0
        result.sample_text = full_text[:500] if full_text else ""

        if result.text_length == 0:
            result.success = False
            result.error_msg = "DeepSeek-OCR2 produced empty text"
        else:
            result.success = True

    except Exception as e:
        result.error_msg = str(e)
        traceback.print_exc()

    return result


def calculate_score(result: ParserResult, baseline_chars: int) -> int:
    """Calculate overall score (0-100) for a parser result."""
    if (not result.success) or result.text_length == 0:
        return 0
    
    score = 0
    
    # Text completeness (40 points max)
    if baseline_chars > 0:
        completeness = min(result.text_length / baseline_chars, 1.0)
        score += int(completeness * 40)
    
    # Section detection (20 points max)
    if result.sections_count > 0:
        score += min(result.sections_count * 2, 20)
    
    # Table detection (15 points max)
    if result.tables_count > 0:
        score += min(result.tables_count * 5, 15)
    
    # Speed bonus (15 points max, <10s = full points)
    if result.time_seconds < 10:
        score += 15
    elif result.time_seconds < 30:
        score += 10
    elif result.time_seconds < 60:
        score += 5
    
    # Memory efficiency (10 points max, <500MB = full points)
    if result.memory_mb < 500:
        score += 10
    elif result.memory_mb < 1000:
        score += 5
    
    return min(score, 100)


def get_pdf_info(pdf_path: str) -> Dict:
    """Get basic PDF information"""
    info = {
        "path": pdf_path,
        "filename": os.path.basename(pdf_path),
        "size_mb": os.path.getsize(pdf_path) / 1024 / 1024,
        "pages": 0
    }
    
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf_path)
        info["pages"] = len(doc)
        doc.close()
    except:
        try:
            from pypdf import PdfReader
            reader = PdfReader(pdf_path)
            info["pages"] = len(reader.pages)
        except:
            pass
    
    return info


def run_validation(pdf_path: str, parsers_to_test: List[str] = None) -> Dict:
    """Run full validation on a single PDF"""
    print(f"\n{'='*60}")
    print(f"Validating: {os.path.basename(pdf_path)}")
    print(f"{'='*60}")
    
    # Get PDF info
    pdf_info = get_pdf_info(pdf_path)
    print(f"Pages: {pdf_info['pages']}, Size: {pdf_info['size_mb']:.2f} MB")
    
    # Available parsers
    all_parsers = [
        ("DeepDOC", validate_deepdoc),
        ("MinerU", validate_mineru),
        ("Docling", validate_docling),
        ("DeepSeek-OCR2", validate_deepseek_ocr2),
    ]
    
    # Filter parsers if specified
    if parsers_to_test:
        parsers = [(n, v) for n, v in all_parsers if n in parsers_to_test]
    else:
        parsers = all_parsers
    
    results = []
    for name, validator in parsers:
        print(f"\n[{name}] Processing...")
        result = validator(pdf_path)
        if result.success:
            print(f"[{name}] ✓ Done in {result.time_seconds:.2f}s, {result.text_length} chars")
        else:
            print(f"[{name}] ✗ Failed: {result.error_msg}")
        results.append(result)
    
    # Calculate scores (use max text length as baseline)
    baseline_chars = max(r.text_length for r in results if r.success) if any(r.success for r in results) else 1
    
    scored_results = []
    for r in results:
        score = calculate_score(r, baseline_chars)
        scored_results.append((r, score))
    
    # Generate report
    report = {
        "file": pdf_info,
        "timestamp": datetime.now().isoformat(),
        "results": []
    }
    
    print(f"\n{'='*60}")
    print("RESULTS")
    print(f"{'='*60}")
    
    if tabulate:
        table_data = []
        for r, score in scored_results:
            status = "✓" if r.success else "✗"
            table_data.append([
                r.name,
                status,
                f"{r.time_seconds:.2f}" if r.success else "-",
                f"{r.memory_mb:.1f}" if r.success else "-",
                r.text_length if r.success else "-",
                r.sections_count if r.success else "-",
                r.tables_count if r.success else "-",
                score
            ])
        
        headers = ["Parser", "Status", "Time(s)", "Mem(MB)", "Chars", "Sections", "Tables", "Score"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        for r, score in scored_results:
            data = r.to_dict()
            data["score"] = score
            print(f"{r.name}: {data}")
    
    # Find winner
    winner = max(scored_results, key=lambda x: x[1])
    print(f"\n🏆 Winner: {winner[0].name} (Score: {winner[1]})")
    
    # Add to report
    for r, score in scored_results:
        data = r.to_dict()
        data["score"] = score
        report["results"].append(data)
    
    report["winner"] = winner[0].name
    report["winner_score"] = winner[1]
    
    return report


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_parsers.py <pdf_file_or_directory>")
        print("\nExample:")
        print("  python validate_parsers.py /path/to/test.pdf")
        print("  python validate_parsers.py /path/to/pdf_folder/")
        sys.exit(1)
    
    path = sys.argv[1]
    
    if os.path.isfile(path):
        pdf_files = [path]
    elif os.path.isdir(path):
        pdf_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.pdf')]
    else:
        print(f"Error: Path not found: {path}")
        sys.exit(1)
    
    if not pdf_files:
        print("No PDF files found")
        sys.exit(1)
    
    print(f"Found {len(pdf_files)} PDF file(s) to validate")
    
    all_reports = []
    for pdf_file in sorted(pdf_files):
        report = run_validation(pdf_file)
        all_reports.append(report)
    
    # Save combined report
    report_path = f"validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(all_reports, f, ensure_ascii=False, indent=2)
    
    print(f"\n📊 Full report saved to: {report_path}")
    
    # Summary
    if len(all_reports) > 1:
        print(f"\n{'='*60}")
        print("OVERALL SUMMARY")
        print(f"{'='*60}")
        
        parser_scores = {}
        for report in all_reports:
            for r in report["results"]:
                name = r["name"]
                if name not in parser_scores:
                    parser_scores[name] = []
                parser_scores[name].append(r["score"])
        
        for name, scores in parser_scores.items():
            avg = sum(scores) / len(scores)
            print(f"{name}: Average Score = {avg:.1f}")
        
        # Overall winner
        avg_scores = {name: sum(scores)/len(scores) for name, scores in parser_scores.items()}
        overall_winner = max(avg_scores, key=avg_scores.get)
        print(f"\n🏆 Overall Winner: {overall_winner} (Avg Score: {avg_scores[overall_winner]:.1f})")


if __name__ == "__main__":
    main()
