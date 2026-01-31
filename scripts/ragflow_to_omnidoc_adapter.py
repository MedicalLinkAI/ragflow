#!/usr/bin/env python3
"""
Adapter: Convert RAGflow parser output to OmniDocBench GT format.

RAGflow parsers return: (sections: List[dict], tables: List[dict])
OmniDocBench expects: normalized text (for Edit Distance) and table HTML/LaTeX (for TEDS)
"""

import re
from typing import List, Dict, Any


def normalize_text(text: str) -> str:
    """
    Normalize text following OmniDocBench conventions.
    
    Rules:
    - UTF-8 encoding
    - Unified newlines to \n
    - Remove excessive whitespace
    - Strip coordinate tags (e.g., @@...##)
    - Remove headers/footers markers (if present)
    """
    if not text:
        return ""
    
    # Ensure UTF-8
    if isinstance(text, bytes):
        text = text.decode('utf-8', errors='ignore')
    
    # Unified newlines
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Remove coordinate tags (e.g., @@1,2,3,4##)
    text = re.sub(r'@@[\d,\.]+##', '', text)
    
    # Remove multiple spaces (but preserve single spaces)
    text = re.sub(r' {2,}', ' ', text)
    
    # Remove multiple newlines (max 2 consecutive)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def ragflow_sections_to_text(sections: List[dict]) -> str:
    """
    Convert RAGflow sections to normalized plain text.
    
    Args:
        sections: List of section dicts from RAGflow parser
                  Format: [{"text": "...", "type": "title|paragraph|...", ...}]
    
    Returns:
        Normalized plain text for Edit Distance calculation
    """
    if not sections:
        return ""
    
    texts = []
    for section in sections:
        # Extract text field
        section_text = section.get('text', '') or section.get('content', '')
        if section_text:
            texts.append(section_text)
    
    # Join with double newline to preserve structure
    full_text = '\n\n'.join(texts)
    
    # Normalize
    return normalize_text(full_text)


def cells_to_html(cells: List[List[str]]) -> str:
    """
    Convert 2D cell array to HTML table.
    
    Args:
        cells: 2D array of cell contents
               Example: [["a", "b"], ["c", "d"]]
    
    Returns:
        HTML table string
    """
    if not cells or not cells[0]:
        return "<table></table>"
    
    html = ["<table>"]
    
    for row_idx, row in enumerate(cells):
        html.append("  <tr>")
        for cell in row:
            # First row as header (optional, can be configured)
            tag = "th" if row_idx == 0 else "td"
            cell_text = str(cell).strip() if cell else ""
            html.append(f"    <{tag}>{cell_text}</{tag}>")
        html.append("  </tr>")
    
    html.append("</table>")
    return '\n'.join(html)


def cells_to_latex(cells: List[List[str]]) -> str:
    """
    Convert 2D cell array to LaTeX table.
    
    Args:
        cells: 2D array of cell contents
    
    Returns:
        LaTeX table string
    """
    if not cells or not cells[0]:
        return "\\begin{tabular}{}\n\\end{tabular}"
    
    # Determine column format (all left-aligned)
    num_cols = len(cells[0])
    col_format = 'l' * num_cols
    
    latex = [f"\\begin{{tabular}}{{{col_format}}}"]
    latex.append("\\hline")
    
    for row in cells:
        # Escape special LaTeX characters
        escaped_row = [str(cell).replace('&', '\\&').replace('%', '\\%').replace('_', '\\_') 
                       for cell in row]
        latex.append(" & ".join(escaped_row) + " \\\\")
    
    latex.append("\\hline")
    latex.append("\\end{tabular}")
    
    return '\n'.join(latex)


def ragflow_tables_to_omnidoc(tables: List[dict]) -> List[Dict[str, str]]:
    """
    Convert RAGflow tables to OmniDocBench format.
    
    Args:
        tables: List of table dicts from RAGflow parser
                Format: [{"cells": [[...]], "bbox": [...], ...}]
    
    Returns:
        List of dicts with 'html' and 'latex' keys for TEDS calculation
    """
    if not tables:
        return []
    
    result = []
    for table in tables:
        cells = table.get('cells', [])
        if not cells:
            continue
        
        result.append({
            'html': cells_to_html(cells),
            'latex': cells_to_latex(cells),
        })
    
    return result


def ragflow_to_omnidoc_document(sections: List[dict], tables: List[dict]) -> Dict[str, Any]:
    """
    Convert RAGflow parser output to OmniDocBench document format.
    
    Args:
        sections: RAGflow sections
        tables: RAGflow tables
    
    Returns:
        Dict with 'text' (for Edit Distance) and 'tables' (for TEDS)
    """
    return {
        'text': ragflow_sections_to_text(sections),
        'tables': ragflow_tables_to_omnidoc(tables),
    }


# Example usage
if __name__ == "__main__":
    # Test sections
    test_sections = [
        {"text": "Title\n\n", "type": "title"},
        {"text": "This is a paragraph.\n", "type": "paragraph"},
    ]
    
    # Test tables
    test_tables = [
        {"cells": [["Header1", "Header2"], ["Cell1", "Cell2"]]},
    ]
    
    # Convert
    doc = ragflow_to_omnidoc_document(test_sections, test_tables)
    
    print("Text:")
    print(doc['text'])
    print("\nTables:")
    for i, table in enumerate(doc['tables']):
        print(f"\n=== Table {i+1} HTML ===")
        print(table['html'])
        print(f"\n=== Table {i+1} LaTeX ===")
        print(table['latex'])
