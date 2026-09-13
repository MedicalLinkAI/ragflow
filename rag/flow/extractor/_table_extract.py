# _table_extract.py — HTML table parsing helpers for ExaminationReport ERT pages
#
# Used by process_text() in qwen_vl_ocr.py when:
#   - rec_type == "ExaminationReport"
#   - allow_examination_report_table_text canvas variable is True
#   - canvas page_table_html contains HTML tables from ERT parser

import re


def html_parse_all_tables(html: str) -> list:
    """Parse ALL HTML ``<table>`` blocks into tables, each a 2-D cell array.

    Uses BeautifulSoup when available; falls back to regex extraction
    otherwise.  Empty ``<td></td>`` cells are preserved (never dropped),
    which is the main advantage over naive regex.

    Returns: list of tables, each table is list[list[str]].
    """
    tables = []
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        for table in soup.find_all('table'):
            rows = []
            for tr in table.find_all('tr'):
                cells = []
                for td in tr.find_all(['td', 'th']):
                    cells.append(td.get_text(strip=True))
                # strip trailing empty cells, preserve internal ones
                while cells and cells[-1] == '':
                    cells.pop()
                if cells:
                    rows.append(cells)
            if rows:
                tables.append(rows)
    except ImportError:
        # Regex fallback: find <table>...</table>, then <tr>...</tr>, then <td|th>...</td|th>
        for table_m in re.finditer(
            r'<table[^>]*>(.*?)</table>', html, re.DOTALL | re.IGNORECASE
        ):
            table_body = table_m.group(1)
            rows = []
            for tr_m in re.finditer(
                r'<tr[^>]*>(.*?)</tr>', table_body, re.DOTALL | re.IGNORECASE
            ):
                tr_body = tr_m.group(1)
                cells = []
                for cell_m in re.finditer(
                    r'<t[hd][^>]*>(.*?)</t[hd]>', tr_body, re.DOTALL | re.IGNORECASE
                ):
                    cells.append(_strip_html_tags(cell_m.group(1)).strip())
                while cells and cells[-1] == '':
                    cells.pop()
                if cells:
                    rows.append(cells)
            if rows:
                tables.append(rows)
    return tables


def _strip_html_tags(s: str) -> str:
    """Remove HTML tags from a string, decode common entities."""
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    s = s.replace('&nbsp;', ' ').replace('&quot;', '"')
    return s
