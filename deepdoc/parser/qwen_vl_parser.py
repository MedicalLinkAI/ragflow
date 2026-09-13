#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  QwenVLParser — Qwen3-VL based PDF parser for MedLinkAI pipeline.
#  Classifies each page as text/table, extracts content via VLM.
#  Outputs clean text (no BBOX markers); coordinates are placeholder;
#  actual coordinate extraction is handled by the Extractor layer.
#
from __future__ import annotations

import base64
import json
import logging
import time
import types

TAG = "[qwen-vl-parser]"
_logger = logging.getLogger("qwen_vl_parser")

# 类方法内页级日志用实例归因 tag self._log_tag（__init__ 构造）；
# 模块级纯函数的退化防御日志无实例上下文，继续用模块级 TAG。
# 归因实现统一在 common.log_tag（零依赖），不再经 qwen_vl_ocr 导入
from common.log_tag import build_log_tag as _build_log_tag

import os
import re
from io import BytesIO
from os import PathLike
from pathlib import Path
from typing import Any, Callable, Optional, Union

import pdfplumber
import requests
import fitz
from PIL import Image

try:
    from deepdoc.parser.pdf_parser import RAGFlowPdfParser
except Exception:

    class RAGFlowPdfParser:
        pass


SectionTuple = tuple[str, int]  # (text, page_0based) — consistent with PaddleOCR-VL
ParseResult = tuple[list[SectionTuple], list]


# ── Prompts ────────────────────────────────────────────────────────

CLASSIFY_PROMPT = (
    '判断这张图片的主体内容类型，并提取报告时间。\n'
    '\n'
    '输出 JSON 格式：{"type": "table" 或 "text", "report_date": "YYYY-MM-DD 或 null"}\n'
    '\n'
    'type 判断规则：\n'
    '输出 table 的条件（必须同时满足）：\n'
    '- 这是一份检验报告单/化验单（如血常规、尿常规、生化检验、免疫检验等）\n'
    '- 内容以检验指标表格为主体（有序号、项目名称、结果、参考值、单位等列）\n'
    '\n'
    '输出 text 的情况（以下全部归为 text）：\n'
    '- 门诊病历、入院记录、出院记录、病程记录\n'
    '- 处方、购药单\n'
    '- 收费票据、发票、收据（即使有费用明细表格）\n'
    '- 诊断证明、诊断报告、检查报告单（影像/病理/心电图/肝功能等）\n'
    '- 功能检查报告单（肺功能、骨密度、肌电图、脑电图、听力、眼底等，即使含参数表格也归 text）\n'
    '- 各种靶向药、基因检测、变异检测、免疫检测\n'
    '- 其他非检验报告的医疗文档\n'
    '\n'
    'report_date 提取规则：\n'
    '- 仅当 type 为 table 时提取，否则填 null\n'
    '- 必须在图片中找到明确标注的日期字段，如"报告时间"、"检验时间"、"送检时间"、"采样时间"、"检测时间"、"审核时间"等\n'
    '- 只提取这些字段后面紧跟的日期值，格式为 YYYY-MM-DD\n'
    '- 严禁猜测、推断、编造日期。图片中没有任何时间字段时，必须填 null\n'
    '- 参考区间中的日期、参考值中的数字都不是报告时间，不得提取\n'
    '- 如果不确定，填 null\n'
    '\n'
    '关键区分：收费票据/发票/收据/各类检查报告单（含功能检查报告）虽然可能有表格或参数，但不是检验报告，type 必须输出 text。\n'
    '检查报告单的参数（如肺功能 FVC/FEV1、骨密度 T 值等）是检查结果，不是检验指标表，不得归为 table。'
)

TEXT_PROMPT = (
    "你是一个专业的医疗文档OCR识别引擎。请逐行识别图片中的所有可见文字内容。\n"
    "\n"
    "## 规则\n"
    "1. 每一行文字作为一个独立条目\n"
    "2. 长段落按实际换行拆分为多行，每行单独一条\n"
    "3. 同一行的标签+值（如'性别：女'）合并为一条，不要拆分\n"
    "4. 不得跳过任何可见文字，包括签名、日期、声明、页码等\n"
    "5. 严禁输出图片中的水印文字（如“网页仅供浏览”“扫描全能王”等），这些不是病历内容\n"
    '6. 双栏布局时，同一行的左栏和右栏内容分别作为独立条目，按从上到下、从左到右顺序输出，不得遗漏右栏\n'
    "\n"
    "## 输出格式\n"
    "直接输出JSON字符串数组，每个元素是该行的文本内容。\n"
    "正确示例：\n"
    '["性别：女", "职业：农民", "年龄：68岁", "入院时间：2026-01-01 08:52", "民族：汉族", "记录时间：2026-01-01 09:14"]\n'
    "请直接输出纯JSON数组，不要用markdown代码块包裹。"
)

TABLE_PROMPT = (
    "你是一个专业的医疗文档表格识别引擎。请将图片中的表格精确转换为 LaTeX tabular 格式。\n"
    "\n"
    "## 核心规则\n"
    "1. **列数完全一致**：数据行的列数必须与图片中表头的列数完全一致。"
    "图片有 N 列，输出就必须有 N 列。\n"
    "2. **不丢列**：图片中看到的每一列都必须输出。"
    "医疗检验表格中常见的列包括：序号、项目代码（英文缩写）、项目名称（中文全称）、"
    "前回値、結果、異常标识（H/L）、単位、参考区間。"
    "所有这些列都必须完整保留，绝不允许跳过任何一列。\n"
    "3. 使用标准 LaTeX tabular 语法：\n"
    "   \\begin{tabular}{ccc...c}\n"
    "   \\hline\n"
    "   列1 & 列2 & ... & 列N \\\\\n"
    "   \\hline\n"
    "   値1 & 値2 & ... & 値N \\\\\n"
    "   ...\n"
    "   \\hline\n"
    "   \\end{tabular}\n"
    "4. 列对齐全部使用 c（居中），如 5 列就是 {ccccc}。\n"
    "5. **保留原文**：所有可见文字原样输出，包括空格、↑↓箭头、★符号、H/L标识等。"
    "↑↓箭头等符号直接输出原字符，严禁用 \\textup{}、\\textbf{} 等 LaTeX 命令包裹任何单元格内容。\n"
    "6. LaTeX 特殊字符转义：# → \\#，% → \\%，& → \\&（作为内容时），"
    "_ → \\_，~ → \\textasciitilde{}。\n"
    "7. 空单元格直接留空（两个 & 之间不放空格以外的内容）。\n"
    "8. 数据结束后立即输出 \\hline 和 \\end{tabular}，不要输出空行。\n"
    "\n"
    "## 多表格规则\n"
    "如果图片中有多个独立的表格（上下排列），"
    "每个表格独立输出为一个 \\begin{tabular}...\\end{tabular} 环境，"
    "表格之间用空行分隔。\n"
    "\n"
    "## 输出要求\n"
    "直接输出纯 LaTeX tabular 代码，不要使用代码块包裹，不要有任何额外文字。"
)


# ERT 专用分类 prompt：只判断是否为 examination_report_table_text
CLASSIFY_PROMPT_WITH_ERT = (
    '判断这张图片是否同时满足以下全部条件：\n'
    '1. 这是一份功能检查报告（肺功能检查、支气管舒张试验、FeNO等）\n'
    '2. 页面同时包含叙述性描述文字和数据表格\n'
    '3. 有明确的区域划分：检查所见区域 + 结论区域\n'
    '\n'
    '数据表格判断规则：\n'
    '- 个人信息区（姓名、性别、年龄、科室、床号、住院号等）不视为数据表格\n'
    '- 即使没有明确的边框线，只要行列对齐，就视为数据表格。\n'
    '- 例如：肺功能参数表\n'
    '\n'
    '输出 JSON 格式：{"type": "examination_report_table_text" 或 "other", "report_date": "YYYY-MM-DD 或 null"}\n'
    '\n'
    '- 如果全部满足条件，type 输出 "examination_report_table_text"\n'
    '- 否则 type 输出 "other"\n'
    '- report_date：提取图片中的报告时间（如"报告时间"、"检查时间"等字段后的日期），格式 YYYY-MM-DD\n'
    '- 如果不确定或找不到日期，report_date 填 null'
)

# ── Examination Report Table+Text (ERT) prompts ──────────────────
# 用于检查报告（肺功能、支气管舒张试验、骨密度、心电图等）页面同时包含
# 叙述文字和参数表格的场景。拆分为两个独立 prompt 分别提取，比混合 prompt 更可靠。

EXAMINATION_TEXT_PROMPT = (
    "你是一个专业的医疗文档OCR识别引擎。请逐行识别图片中所有叙述性文字内容。\n"
    "\n"
    "## 规则\n"
    "1. 每一行叙述文字作为一个独立条目\n"
    "2. 长段落按实际换行拆分为多行，每行单独一条\n"
    "3. 同一行的标签+值（如'性别：女'、'检查日期：2026-01-01'）合并为一条\n"
    "4. 不得跳过任何叙述性文字，包括签名、日期、声明、页码等\n"
    "5. 严禁输出水印文字\n"
    "6. 双栏布局时，左右栏分别作为独立条目\n"
    "\n"
    "## 严禁提取以下内容到 text_lines\n"
    "- 表格标题行/表头行（如 Parameter、UM、Pred.、BEST#1 等列标题）\n"
    "- 表格数据行（如 FVC、FEV1、PEF 等参数行及其对应的数值）\n"
    "- 参考值表、对比表等任何行列对齐的数据区域\n"
    "- 测量参数区域：在'检测结果'、'测量参数'、'测定条件'等小标题下的键值对数据\n"
    "  （如'呼气方式：在线'、'测定温度：26℃'、'呼气时间：10s'等），"
    "  即使它们是两列键值对形式，也必须作为表格输出\n"
    "- 坐标图/曲线图/趋势图中的任何内容（图表标题、坐标轴刻度值、坐标轴标签等）\n"
    "\n"
    "## 以下区域属于叙述文字，必须提取\n"
    "- 患者信息区（姓名、性别、年龄、科室、床号等）\n"
    "- 报告标题/页眉\n"
    "- 检查所见/检查描述的叙述段落\n"
    "- 结论/诊断意见的叙述段落\n"
    "- 签名区（医生签名、审核签名）\n"
    "\n"
    "## 输出格式\n"
    "直接输出JSON字符串数组，每个元素是该行的文本内容。\n"
    "请直接输出纯JSON数组，不要用markdown代码块包裹。"
)

EXAMINATION_TABLE_PROMPT = (
    "你是一个专业的医疗文档表格识别引擎。请将图片中所有数据表格精确转换为 HTML <table> 格式，"
    "并判断每张表格属于检查报告的哪个部分。\n"
    "\n"
    "## 表格提取规则\n"
    "1. 使用标准 HTML 表格标签：<table>、<tr>、<th>（表头单元格）、<td>（数据单元格）\n"
    "2. 表头行用 <th>，数据行用 <td>\n"
    "3. 数据行的列数必须与表头列数一致，不丢列\n"
    "4. 空单元格必须保留：<td></td>，不得跳过\n"
    "5. 保留所有原文内容（包括↑↓箭头、★符号、H/L标识等），直接写入标签内，无需转义\n"
    "6. 如果页面有多个独立表格，每个独立输出一个 <table>...</table>\n"
    "7. ⚠️ 患者基本信息区绝对不是表格，严禁提取！包括：姓名、性别、年龄、科室、床号、住院号、就诊卡号、检查时间等字段区域，"
    "即使这些字段排列整齐、有网格线或分隔线，也不是数据表格，不要提取为 <table>\n"
    "8. 键值对不视为表格，不要提取为 <table>\n"
    "\n"
    "## 表格归属分类（table_sections）\n"
    "检查报告中的表格按语义归属分类：\n"
    "- \"findings\"（检查所见）：所有包含详细测量参数/指标数据的表格。"
    "例如肺功能参数表（FVC、FEV1、PEF 等含实测值/预测值/百分比的表格）、"
    "任何含具体数值/单位/参考区间的检验指标表。"
    "规则：只要表格包含具体测量数值，一律归为 findings\n"
    "- \"conclusion\"（结论）：出现在\"结论\"/\"诊断意见\"/\"临床解析\"标题下方的表格，"
    "且表格内容为诊断结论性文字（如参考值范围、炎症类型判断标准、诊断分级等），"
    "而非具体测量数值。例如：FeNO 临床解析中的参考值表格（<25ppb 非嗜酸性、25-50ppb 混合型等）应归为 conclusion\n"
    "- 默认规则：不确定时，归为 findings（因为绝大多数检查报告的表格都是 findings）\n"
    "- table_sections 数组长度必须与 tables_html 数组长度完全一致，一一对应\n"
    "\n"
    "## 输出格式\n"
    "严格输出纯JSON，禁止使用代码块包裹，禁止输出任何非JSON文字：\n"
    '{\n'
    '  "tables_html": ["<table>表格1</table>", "<table>表格2</table>"],\n'
    '  "table_sections": ["findings", "conclusion"]\n'
    '}\n'
    "- tables_html：HTML字符串数组，每个元素是一个完整的 <table>...</table> 代码\n"
    "- table_sections：字符串数组，与 tables_html 一一对应，每个值为 \"findings\" 或 \"conclusion\"\n"
    "- 如果页面没有数据表格，tables_html 输出 []，table_sections 也输出 []\n"
    "- 严禁遗漏任何数据表格"
)


# ── Helpers ────────────────────────────────────────────────────────

def _strip_fence(text: str) -> str:
    """Strip markdown code fences from LLM output."""
    if not isinstance(text, str):
        return text
    text = text.strip()
    text = re.sub(r"^```(?:json|latex|tex)?\s*\n?", "", text)
    text = re.sub(r"\n?\s*```$", "", text)
    return text.strip()


def _fix_tabular_colspec(latex: str, max_cols: int = 20) -> str:
    """Collapse degenerate tabular column specs like {l l l l l ... (500+)}.

    VLM sometimes hallucinates hundreds of column specifiers. This detects
    such patterns and truncates to a reasonable column count.
    """
    def _replace_colspec(m: re.Match) -> str:
        prefix = m.group(1)  # e.g. \\begin{tabular}
        spec = m.group(2)    # e.g. "l l l l l ..."
        # Count actual column chars (l, c, r, p, m, b, X)
        cols = re.findall(r'[lcrpmbX]', spec)
        if len(cols) > max_cols:
            logging.warning(
                f"{TAG} degenerate tabular colspec: {len(cols)} columns, "
                f"truncating to {max_cols}"
            )
            # Use 'c' for all columns
            return f"{prefix}{{{('c' * max_cols)}}}"
        return m.group(0)  # keep original

    return re.sub(
        r'(\\begin\{tabular\*?\})\{([^}]{30,})\}',
        _replace_colspec,
        latex,
    )


_MIN_COLSPEC_RUN = 4

# Runaway loop INSIDE the tabular column spec itself: the VLM emits
# \begin{tabular}{|c|c|c|... (hundreds/thousands of repeats, often one
# huge line truncated mid-spec with no closing brace), burning the whole
# token budget before any data row. Line/row-based detectors cannot see
# this shape. Anchored to \begin{tabular}{ so real cell text never trips.
_COLSPEC_RUN_RE = re.compile(
    r'\\begin\{tabular\*?\}\{((?:\|?\s*[lcrpmbX]){' + str(_MIN_COLSPEC_RUN) + r',})([^}]*)\}?'
)


def _collapse_colspec_run(
    latex: str, max_cols: int = 20
) -> tuple[str, Optional[tuple[str, int]]]:
    """Truncate a runaway colspec run ({|c|c|c|... Nx, N >= 30) to max_cols.

    Salvage mirror of _fix_tabular_colspec for the pipe-separated runaway
    shape: keeps the first max_cols column units, preserves everything
    after the run (data rows the loop may have left intact).

    Returns (latex, rep_info); rep_info=(col_char, count) when a run of
    >= _MIN_COLSPEC_RUN column units was truncated, else None.
    """
    m = _COLSPEC_RUN_RE.search(latex or "")
    if not m:
        return latex, None
    run = m.group(1)
    units = re.findall(r'\|?\s*[lcrpmbX]', run)
    if len(units) <= max_cols:
        return latex, None
    result = latex[: m.start(1)] + "".join(units[:max_cols]) + latex[m.end(1):]
    col_char = units[0][-1]
    logging.warning(
        f"{TAG} degenerate colspec run: '{col_char}' repeated "
        f"{len(units)}x, truncating to {max_cols}"
    )
    return result, (col_char, len(units))


# ── Degenerate repetition-loop defense (VLM hallucination) ────────
# Greedy decoding (temperature=0) can fall into runaway loops like
# \textup{\textup{\textup{... when emitting arrows/symbols, burning the
# whole max_tokens budget and truncating the rest of the table.

_REPETITION_LOOP_RE = re.compile(r"(?:\\[a-zA-Z]+\{){10,}")


def _has_repetition_loop(latex: str) -> bool:
    """Detect runaway LaTeX command nesting like \\textup{\\textup{... ."""
    return bool(_REPETITION_LOOP_RE.search(latex or ""))


def _truncate_repetition_loop(latex: str) -> str:
    """Cut output at the repetition loop start, salvaging the valid prefix.

    The row in which the loop started is incomplete (no \\ terminator),
    so it is dropped along with the loop.
    """
    m = _REPETITION_LOOP_RE.search(latex or "")
    if not m:
        return latex
    cut = latex[: m.start()]
    lines = cut.split("\n")
    if lines:
        last = lines[-1].strip()
        if last and not last.endswith("\\\\") and not re.search(r"\\(?:begin|end|hline)", last):
            lines = lines[:-1]
    result = "\n".join(lines)
    logging.warning(
        f"{TAG} degenerate repetition loop at char {m.start()}, "
        f"truncating {len(latex)}→{len(result)} chars"
    )
    return result


_SYMBOL_ONLY_RE = re.compile(r'^[+\-*=#|~_·•\s]+$')


_MIN_ROW_RUN = 5
_MIN_TEXT_RUN = 5
_MAX_UNIQUENESS_RATIO = 0.05
_MIN_EMPTY_RUN = 20
_MIN_ALT_RUN = 50  # period-2 alternation (A B A B ...) longer than this = spam

# A run of N consecutive "" elements: "","",... separated only by commas
_EMPTY_RUN_RE = re.compile(r'""(?:\s*,\s*""){%d,}' % (_MIN_EMPTY_RUN - 1))


def _is_empty_flood(raw: Optional[str]) -> bool:
    """Detect empty-string flooding: greedy loop emitting "" elements.

    The fingerprint is a LONG CONSECUTIVE run of empty elements — real
    transcription content never produces dozens of them back to back,
    while tables legitimately carry interspersed empty cells (e.g. 3
    empty columns per row). Counting total empties instead misfires on
    such tables (75 separated empties across 25 rows is not a flood).
    Content-based, independent of response size.
    """
    if not raw:
        return False
    return bool(_EMPTY_RUN_RE.search(_strip_fence(raw)))


def _is_truncated_array(raw: Optional[str]) -> bool:
    """Detect token-budget truncation: array opened with '[' but no ']'.

    A legitimate response is either a fully closed JSON array or '[]' for
    an empty page, so an unclosed array is structural evidence of a
    runaway loop regardless of response length.
    """
    if not raw:
        return False
    stripped = _strip_fence(raw)
    return stripped.startswith("[") and "]" not in stripped


def _dedup_repeated_blocks(
    lines: list[str],
) -> tuple[list[str], Optional[tuple[int, int, int]]]:
    """Detect and truncate repeated content (model hallucination).

    Covers four shapes, applied iteratively until the output is clean
    (a single response may contain several spam segments):
    1. prefix block cycle: consecutive repetitions of lines[0:cycle]
       (cycle >= 3), collapsed to a single occurrence while keeping the
       unique tail — medical forms legitimately repeat header fields
       (e.g. 姓名/性别/年龄 printed in two columns), so truncating to the
       prefix would destroy real content
    2. identical-row run at any position: one line repeated >= _MIN_TEXT_RUN
       times in a row (e.g. a trailing "病理诊断：" spam filling the token
       budget), collapsed to a single occurrence
    3. two-value alternation (A B A B ...) at any position: a long run of
       period-2 repeats (e.g. YXLA p15 emitted "10"/"12" for 3800+ lines),
       collapsed to one occurrence of each value
    4. degenerate uniqueness: huge output with almost no distinct lines

    Returns (lines, rep_info); rep_info=(cycle, repeats, n) describes the
    first pattern detected, None when the input is clean. cycle=2 marks the
    two-value alternation shape, cycle=1 single-line run / uniqueness, and
    cycle>=3 a prefix block cycle.
    """
    if len(lines) <= 20:
        return lines, None
    first_rep: Optional[tuple[int, int, int]] = None
    for _ in range(10):  # bounded passes; each removes one spam pattern
        n = len(lines)
        detected: Optional[tuple[tuple[int, int, int], list[str]]] = None
        # 1) prefix block cycle: collapse the consecutive run of the prefix
        #    block, preserving the unique tail (form headers like 姓名/性别/年龄
        #    are physically printed twice in two-column forms — not hallucination)
        for cycle in range(3, n // 2 + 1):
            if lines[cycle:2 * cycle] == lines[0:cycle] and n // cycle >= 2:
                k = 2
                while (
                    (k + 1) * cycle <= n
                    and lines[k * cycle:(k + 1) * cycle] == lines[0:cycle]
                ):
                    k += 1
                detected = ((cycle, n // cycle, n), lines[:cycle] + lines[k * cycle:])
                break
        # 2) identical-line run at any position
        if not detected:
            i = 0
            while i < n:
                j = i + 1
                while j < n and lines[j] == lines[i]:
                    j += 1
                if j - i >= _MIN_TEXT_RUN:
                    detected = ((1, j - i, n), lines[: i + 1] + lines[j:])
                    break
                i = j
        # 3) two-value alternation (A B A B ...) at any position: long
        #    period-2 runs are never legitimate medical content (a real form
        #    would need to alternate the same two values 50+ times), while
        #    chart-axis spam emits exactly this (YXLA p15: "10"/"12" x3836)
        if not detected:
            start = 0
            while start < n - 1:
                a, b = lines[start], lines[start + 1]
                if a == b:
                    start += 1
                    continue
                end = start + 2
                while end < n and lines[end] == lines[end - 2]:
                    end += 1
                if end - start >= _MIN_ALT_RUN:
                    detected = (
                        (2, end - start, n),
                        lines[:start] + [a, b] + lines[end:],
                    )
                    break
                start = end - 1
        # 4) degenerate uniqueness ratio
        if not detected and n >= 100 and len(set(lines)) <= _MAX_UNIQUENESS_RATIO * n:
            uniq: list[str] = []
            for t in lines:
                if not uniq or uniq[-1] != t:
                    uniq.append(t)
            detected = ((1, n, n), uniq)
        if not detected:
            break
        if first_rep is None:
            first_rep = detected[0]
        lines = detected[1]
        if len(lines) <= 20:
            break
    return lines, first_rep


def _dedup_latex_rows(
    latex: str,
) -> tuple[str, Optional[tuple[str, int]]]:
    """Collapse runs of consecutive identical data rows (model hallucination).

    Covers the single-macro runaway pattern (e.g. \\multicolumn rows repeated
    verbatim until the token budget is exhausted), which the nested-macro
    detector _has_repetition_loop cannot see.

    Returns (latex, rep_info); rep_info=(row_preview, repeats) when a run of
    >= _MIN_ROW_RUN identical data rows was collapsed to one, else None.
    """
    lines = latex.split("\n")
    out: list[str] = []
    rep_info: Optional[tuple[str, int]] = None
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if "&" in stripped:
            j = i + 1
            while j < n and lines[j].strip() == stripped:
                j += 1
            if j - i >= _MIN_ROW_RUN:
                if rep_info is None:
                    rep_info = (stripped[:60], j - i)
                out.append(line)  # keep first occurrence only
                i = j
                continue
        out.append(line)
        i += 1
    if rep_info is None:
        return latex, None
    return "\n".join(out), rep_info


def _parse_json_array(raw: str) -> Optional[list[str]]:
    """Parse JSON array with fallback (json_repair)."""
    if not raw:
        return None
    raw = _strip_fence(raw)

    # Try direct parse
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            return [str(x).strip() for x in data if str(x).strip()]
    except json.JSONDecodeError:
        pass

    # Try json_repair
    try:
        import json_repair
        data = json_repair.loads(raw)
        if isinstance(data, list):
            return [str(x).strip() for x in data if str(x).strip()]
    except Exception:
        pass

    # Try regex extraction
    m = re.search(r"\[.*\]", raw, re.DOTALL)
    if m:
        try:
            import json_repair
            data = json_repair.loads(m.group())
            if isinstance(data, list):
                return [str(x).strip() for x in data if str(x).strip()]
        except Exception:
            pass

    return None


def _split_latex_lines(latex_text: str) -> list[str]:
    """Split LaTeX tabular content into individual lines.

    Preserves LaTeX special characters. Each non-empty line becomes one entry.
    """
    lines = []
    for line in latex_text.split("\n"):
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
    return lines


class QwenVLParser(RAGFlowPdfParser):
    """PDF parser using Qwen3-VL model for content extraction.

    Classifies each page as text or table, extracts content via VLM API.
    Coordinates use placeholder values — actual coordinate extraction is
    delegated to the Extractor layer.
    """

    # 页级并发度：同时在飞的页数上限。实测 vLLM 接 4~6 并发零排队，
    # 超过后单请求速度被摊薄且总吞吐不再增长。
    PAGE_CONCURRENCY = 4

    def __init__(
        self,
        api_url: Optional[str] = None,
        model: Optional[str] = None,
        *,
        api_key: Optional[str] = None,
        request_timeout: int = 300,
        max_retries: int = 2,
        retry_backoff: float = 3.0,
        doc_id: Optional[str] = None,
        task_id: Optional[str] = None,
        doc_name: Optional[str] = None,
        page_concurrency: Optional[int] = None,
        allow_ert: bool = False,
    ):
        super().__init__()

        self.outlines: list = []
        self._allow_ert = allow_ert
        # page_types: page_idx (0-based) → "table"|"text"|"examination_report_table_text"
        self.page_types: dict[int, str] = {}
        # page_table_html: page_idx (0-based) → list of HTML strings (one per table)
        self.page_table_html: dict[int, list[str]] = {}
        # page_table_sections: page_idx (0-based) → list of "findings"/"conclusion" per table
        self.page_table_sections: dict[int, list[str]] = {}
        # 端点/模型/密钥由调用方从 tenant_llm 表解析后传入，不再读环境变量
        self.api_url = api_url
        self.model = model
        self.api_key = api_key or ""
        self.request_timeout = request_timeout
        # 页级并发由 DSL 驱动（setups.pdf.vl_global_concurrency 派生一半）：
        # 仅合法正整数遮蔽类默认值，非法值/未传保持类属性（naive 路径不受影响）
        if isinstance(page_concurrency, int) and not isinstance(page_concurrency, bool) and page_concurrency > 0:
            self.PAGE_CONCURRENCY = page_concurrency
            logging.info(f"{TAG} page_concurrency overridden by DSL: {page_concurrency}")
        elif page_concurrency is not None:
            logging.warning(f"{TAG} invalid page_concurrency={page_concurrency!r}, keeping class default {self.PAGE_CONCURRENCY}")
        # 超时重试：8/17 压测实证 300s read timeout 后服务端仍会完成请求，
        # 洪峰已过时重试大概率成功；仅对瞬时网络错误生效，业务错误不重试
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff
        # 日志归因：多 task_executor 共享进程日志流，页级日志需 doc/task/case
        # 才能把超时/失败归属到真实文档（与 extractor 侧 _build_log_tag 口径
        # 一致）；调用方未传（如 naive 路径）时降级 doc=- task=-
        self._log_tag = _build_log_tag(
            types.SimpleNamespace(
                _canvas=types.SimpleNamespace(
                    _doc_id=doc_id or "",
                    task_id=task_id or "",
                    _doc_name=doc_name or "",
                )
            ),
            TAG,
        )
        self.logger = logging.getLogger(self.__class__.__name__)
        # Ensure propagation to root logger
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = True

        # Page images (populated by parse_pdf)
        self.page_images: list[Image.Image] = []
        self.page_from = 0

    def check_installation(self) -> tuple[bool, str]:
        """Check if the VLM API is configured."""
        if not self.api_url:
            return False, "[QwenVL] API URL not configured"
        return True, ""

    def parse_pdf(
        self,
        filepath: str | PathLike[str],
        binary: Optional[Union[BytesIO, bytes]] = None,
        callback: Optional[Callable[[float, str], None]] = None,
        **kwargs: Any,
    ) -> ParseResult:
        """Parse PDF using Qwen3-VL: classify each page, extract content."""
        if not self.api_url:
            raise RuntimeError("[QwenVL] API URL missing")

        # Generate page images
        input_source = filepath if binary is None else binary
        try:
            self._render_page_images(input_source)
        except Exception as e:
            logging.warning(f"{self._log_tag} Failed to render page images: {e}")
            self.page_images = []

        if not self.page_images:
            if callback:
                callback(1, "[QwenVL] No pages to process.")
            return [], []

        total_pages = len(self.page_images)
        if callback:
            callback(0.1, f"[QwenVL] Processing {total_pages} pages...")

        logging.info(f"{self._log_tag} parse_pdf start, total_pages={total_pages}")

        sections: list[SectionTuple] = []
        bbox_idx = 0  # global BBOX counter

        # 页级并发：每页独立 classify + extract，线程池限流 PAGE_CONCURRENCY
        from concurrent.futures import ThreadPoolExecutor, as_completed

        def _process_page(page_idx: int):
            page_1based = page_idx + 1
            try:
                page_img = self.page_images[page_idx]

                # Convert page image to bytes — JPEG 直出替代 PNG：
                # PNG 无损编码在大页面上可达数十 MB，JPEG(q=90) 压缩一个
                # 数量级，减少瞬时字节驻留。下游 downscale_vl_image 与
                # vl_image_data_url 均按 magic bytes 判格式，JPEG 直通。
                if page_img.mode != "RGB":
                    page_img = page_img.convert("RGB")
                buf = BytesIO()
                page_img.save(buf, format="JPEG", quality=90)
                img_bytes = buf.getvalue()
                # 页图用完即弃：PIL 位图在送 VLM 前即置 None，峰值驻留
                # 从"全本页图"降为"并发窗口×单页"（8/23 客户事故取证结论：
                # 单页 6545×9067≈178MB 全本驻留是 worker RSS 160G 的主因）
                self.page_images[page_idx] = None

                # Step 1: Classify page
                page_type, report_date = self._classify_page(img_bytes)
                logging.info(f"{self._log_tag} page={page_1based} classify={page_type} report_date={report_date}")

                # Record page type for downstream canvas publishing
                self.page_types[page_idx] = page_type

                # Step 2: Extract content based on type.
                # 传入 bbox_idx=0 做页内局部编号；全局编号在结果按页序
                # 汇总后统一分配，避免乱序。
                if page_type == "table":
                    page_sections, _ = self._extract_table_page(
                        img_bytes, page_1based, 0, report_date
                    )
                elif page_type == "examination_report_table_text":
                    page_sections, _ = self._extract_ert_page(
                        img_bytes, page_1based, 0
                    )
                else:
                    page_sections, _ = self._extract_text_page(
                        img_bytes, page_1based, 0
                    )

                logging.info(
                    f"{self._log_tag} page={page_1based} {page_type}: {len(page_sections)} sections"
                )
                return page_idx, page_type, page_sections
            except Exception as e:
                # 单页提取失败（含超时重试耗尽）：降级为跳过该页继续剩余页，
                # 不拖死整篇、不丢弃其他页已解析成果（8/17 压测 8 文档
                # 因单页 300s 超时整篇 chunks=0 的实证教训）
                logging.error(
                    f"{self._log_tag} page={page_1based} extraction failed, skipping page: {e}"
                )
                return page_idx, "failed", []

        executor = ThreadPoolExecutor(
            max_workers=self.PAGE_CONCURRENCY,
            thread_name_prefix="qwen-vl-page",
        )
        futures = [executor.submit(_process_page, i) for i in range(total_pages)]
        executor.shutdown(wait=False)

        # 进度回调：按完成数推进（顺序不确定，但进度单调递增）
        if callback:
            done_count = 0
            for _fut in as_completed(futures):
                done_count += 1
                progress = 0.1 + 0.8 * (done_count / total_pages)
                callback(progress, f"[QwenVL] {done_count}/{total_pages} pages done")

        # 按提交顺序（=页序）收集结果；页内异常已在 _process_page 降级为
        # 跳过该页，f.result() 不再携带页级异常
        results = [f.result() for f in futures]
        results.sort(key=lambda r: r[0])

        # 按页序汇总：sections 顺序与串行版一致，bbox 全局编号连续分配
        for page_idx, _page_type, page_sections in results:
            if page_sections:
                start = bbox_idx
                bbox_idx += len(page_sections)
                logging.info(
                    f"{self._log_tag} page={page_idx + 1} assigned global bbox {start}-{bbox_idx - 1}"
                )
            sections.extend(page_sections)

        # 收尾兜底清空：正常路径每页已在 _process_page 内置 None，
        # 此处覆盖"编码前异常未置 None"的残余引用，确保 parse_pdf
        # 返回后不再有任何页图随实例滞留
        self.page_images = []

        logging.info(f"{self._log_tag} parse_pdf done: {len(sections)} sections from {total_pages} pages.")

        if callback:
            callback(0.95, f"[QwenVL] Done: {len(sections)} sections from {total_pages} pages.")

        # tables=[] — coordinate extraction is handled by Extractor layer
        return sections, []

    # ── Internal methods ───────────────────────────────────────────

    def _render_page_images(self, input_source: Any) -> None:
        """Render PDF pages as PIL images using fitz at 200 DPI."""
        self.page_images = []
        try:
            if isinstance(input_source, (str, PathLike)):
                pdf_doc = fitz.open(input_source)
            else:
                pdf_doc = fitz.open(stream=input_source, filetype="pdf")
            dpi = 200
            zoom = dpi / 72.0
            mat = fitz.Matrix(zoom, zoom)
            for page in pdf_doc:
                pix = page.get_pixmap(matrix=mat)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                self.page_images.append(img)
            pdf_doc.close()
        except Exception as e:
            logging.error(f"{self._log_tag} render_page_images failed: {e}")
            raise

    def _classify_page(self, img_bytes: bytes) -> tuple[str, Optional[str]]:
        """Classify page as 'text', 'table', or 'examination_report_table_text' via VLM.

        Two-step approach when allow_ert is enabled:
        1. First check if it's examination_report_table_text (ERT)
        2. If not ERT, use CLASSIFY_PROMPT for table/text classification
        """
        try:
            import json

            # Step 1: Check if ERT (when enabled)
            if self._allow_ert:
                raw_ert = self._call_vlm(img_bytes, CLASSIFY_PROMPT_WITH_ERT)
                if raw_ert:
                    raw_ert = raw_ert.strip()
                    raw_ert = re.sub(r"^```(?:json)?\s*\n?", "", raw_ert)
                    raw_ert = re.sub(r"\n?\s*```$", "", raw_ert)
                    raw_ert = raw_ert.strip()
                    try:
                        result_ert = json.loads(raw_ert)
                        page_type = result_ert.get("type", "").lower()
                        report_date = result_ert.get("report_date", None)
                        if page_type == "examination_report_table_text":
                            return "examination_report_table_text", report_date
                    except json.JSONDecodeError:
                        # If JSON parse fails, check if raw contains type keyword
                        if "examination_report_table_text" in raw_ert.lower():
                            return "examination_report_table_text", None

            # Step 2: Use CLASSIFY_PROMPT for table/text classification
            raw = self._call_vlm(img_bytes, CLASSIFY_PROMPT)
            if not raw:
                return "text", None

            # Try to parse JSON response
            raw = raw.strip()
            # Strip markdown code fences if present
            raw = re.sub(r"^```(?:json)?\s*\n?", "", raw)
            raw = re.sub(r"\n?\s*```$", "", raw)
            raw = raw.strip()

            try:
                result = json.loads(raw)
                page_type = result.get("type", "text").lower()
                report_date = result.get("report_date", None)
                if page_type not in ("table", "text"):
                    page_type = "text"
                return page_type, report_date
            except json.JSONDecodeError:
                # Fallback: check if raw contains type keywords
                if "table" in raw.lower():
                    return "table", None
                return "text", None

        except Exception as e:
            logging.warning(f"{self._log_tag} classify failed: {e}, defaulting to text")
            return "text", None

    def _extract_text_page(
        self, img_bytes: bytes, page_1based: int, bbox_idx: int
    ) -> tuple[list[SectionTuple], int]:
        """Extract text page via VLM → JSON array → sections."""
        raw = self._call_vlm(img_bytes, TEXT_PROMPT)
        lines = _parse_json_array(raw)

        # Empty-string flood / truncated-array defense: a greedy loop can
        # burn max_tokens on "" elements, leaving an unclosed array that
        # fails every parse fallback. Fingerprints are content-based
        # (empty-element count, missing ']'), independent of size.
        if _is_empty_flood(raw) or _is_truncated_array(raw):
            logging.warning(
                f"{self._log_tag} page={page_1based} text output degenerated into "
                f"empty-string flood/truncated array, retrying with repetition_penalty"
            )
            raw2 = self._call_vlm(
                img_bytes, TEXT_PROMPT, extra_params={"repetition_penalty": 1.2}
            )
            if raw2 and not _is_empty_flood(raw2) and not _is_truncated_array(raw2):
                lines2 = _parse_json_array(raw2)
                if lines2 is not None:
                    lines = lines2
            # retry still flooded/unparseable: keep the original salvage

        if not lines:
            logging.warning(f"{self._log_tag} page={page_1based} text extraction returned no lines")
            return [], bbox_idx

        # Filter: keep only string elements, skip pure symbol lines (e.g. "++", "--", "+")
        lines = [t for t in lines if isinstance(t, str) and not _SYMBOL_ONLY_RE.match(t.strip())]

        # Dedup: detect and truncate repeated content blocks (model hallucination)
        lines, rep = _dedup_repeated_blocks(lines)
        if rep:
            cycle, repeats, n = rep
            logging.warning(
                f"{self._log_tag} page={page_1based} detected repetition "
                f"(cycle={cycle}, repeats={repeats}x), collapsing {n}→{len(lines)} lines"
            )
            # Retry once with repetition_penalty: if the model looped early,
            # the collapsed version may still be missing content the loop ate.
            raw2 = self._call_vlm(
                img_bytes, TEXT_PROMPT, extra_params={"repetition_penalty": 1.2}
            )
            lines2 = _parse_json_array(raw2)
            if lines2:
                lines2 = [
                    t for t in lines2
                    if isinstance(t, str) and not _SYMBOL_ONLY_RE.match(t.strip())
                ]
                lines2, rep2 = _dedup_repeated_blocks(lines2)
                # Only adopt the retry when it is clean AND strictly longer
                # than the collapsed version — a shorter clean retry would
                # silently drop content the collapse already salvaged.
                if lines2 and not rep2 and len(lines2) > len(lines):
                    logging.info(
                        f"{self._log_tag} page={page_1based} retry recovered {len(lines2)} lines"
                    )
                    lines = lines2

        if not lines:
            logging.warning(f"{self._log_tag} page={page_1based} text extraction returned no lines after filtering")
            return [], bbox_idx

        sections: list[SectionTuple] = []

        for line in lines:
            text = line.strip()
            if not text:
                continue
            sections.append((text, page_1based - 1))  # store 0-based, consistent with PaddleOCR-VL
            bbox_idx += 1

        # 行数/bbox 段摘要已去重：parse_pdf 层 sections 汇总 + 全局 bbox 分配日志已覆盖
        return sections, bbox_idx

    def _extract_table_page(
        self, img_bytes: bytes, page_1based: int, bbox_idx: int,
        report_date: Optional[str] = None,
    ) -> tuple[list[SectionTuple], int]:
        """Extract table page via VLM → LaTeX → sections.

        Keeps LaTeX special characters intact.
        If report_date is provided, inject it as the first row after \begin{tabular}.
        """
        raw = self._call_vlm(img_bytes, TABLE_PROMPT)
        latex = _strip_fence(raw) if raw else ""

        if not latex:
            logging.warning(f"{self._log_tag} page={page_1based} table extraction returned empty")
            return [], bbox_idx

        # Colspec-run defense: the greedy loop can sit inside the tabular
        # column spec itself ({|c|c|c|... thousands of repeats, one huge
        # line), burning the token budget before any data row. Line/row
        # detectors cannot see this shape — detect it explicitly and retry
        # with repetition_penalty; fall back to the collapsed spec.
        latex, colspec_rep = _collapse_colspec_run(latex)
        if colspec_rep:
            unit, count = colspec_rep
            logging.warning(
                f"{self._log_tag} page={page_1based} table colspec '{unit}' repeated {count}x, "
                f"retrying with repetition_penalty"
            )
            raw2 = self._call_vlm(
                img_bytes, TABLE_PROMPT, extra_params={"repetition_penalty": 1.2}
            )
            latex2 = _strip_fence(raw2) if raw2 else ""
            latex2, rep2 = _collapse_colspec_run(latex2)
            if latex2 and not rep2 and not _has_repetition_loop(latex2):
                latex = latex2
            # else: keep the collapsed version

        # Repetition-loop defense: retry once with repetition_penalty to
        # escape the greedy loop and recover the truncated tail rows;
        # if the retry also loops, salvage the valid prefix.
        if _has_repetition_loop(latex):
            logging.warning(
                f"{self._log_tag} page={page_1based} table output degenerated into "
                f"repetition loop, retrying with repetition_penalty"
            )
            raw2 = self._call_vlm(
                img_bytes, TABLE_PROMPT, extra_params={"repetition_penalty": 1.2}
            )
            latex2 = _strip_fence(raw2) if raw2 else ""
            if latex2 and not _has_repetition_loop(latex2):
                latex = latex2
            else:
                latex = _truncate_repetition_loop(latex)

        # Row-repetition defense: identical data rows repeated verbatim in a
        # run (single-macro runaway, e.g. \multicolumn 刷屏). Same pattern:
        # retry with repetition_penalty, fall back to the collapsed version.
        latex, row_rep = _dedup_latex_rows(latex)
        if row_rep:
            preview, repeats = row_rep
            logging.warning(
                f"{self._log_tag} page={page_1based} table row repeated {repeats}x "
                f"({preview}...), retrying with repetition_penalty"
            )
            raw2 = self._call_vlm(
                img_bytes, TABLE_PROMPT, extra_params={"repetition_penalty": 1.2}
            )
            latex2 = _strip_fence(raw2) if raw2 else ""
            latex2, rep2 = _dedup_latex_rows(latex2)
            if latex2 and not rep2 and not _has_repetition_loop(latex2):
                latex = latex2
            # else: keep the collapsed version

        # Fix degenerate column specs (VLM hallucination)
        latex = _fix_tabular_colspec(latex)

        # Split LaTeX into individual lines
        latex_lines = _split_latex_lines(latex)
        if not latex_lines:
            return [], bbox_idx

        # Inject report_date after \begin{tabular} line
        if report_date:
            injected_lines: list[str] = []
            for line in latex_lines:
                injected_lines.append(line)
                if r"\begin{tabular}" in line:
                    injected_lines.append(f"报告时间: {report_date}")
            latex_lines = injected_lines

        sections: list[SectionTuple] = []

        for line in latex_lines:
            sections.append((line, page_1based - 1))  # store 0-based, consistent with PaddleOCR-VL
            bbox_idx += 1

        # LaTeX 行数/bbox 段摘要已去重：parse_pdf 层 sections 汇总 + 全局 bbox 分配日志已覆盖
        return sections, bbox_idx

    def _extract_ert_page(
        self, img_bytes: bytes, page_1based: int, bbox_idx: int,
    ) -> tuple[list[SectionTuple], int]:
        """Extract mixed text+table page via two separate VLM calls.

        1. EXAMINATION_TEXT_PROMPT → narrative text lines → sections
        2. EXAMINATION_TABLE_PROMPT → HTML tables + section classification → canvas vars

        Stores:
        - self.page_table_html[page_idx] = list of HTML strings
        - self.page_table_sections[page_idx] = list of "findings"/"conclusion" per table
        """
        import json as _json

        # ── Call 1: Extract narrative text ──
        raw_text = self._call_vlm(img_bytes, EXAMINATION_TEXT_PROMPT)
        text_lines = _parse_json_array(raw_text) or []

        # Filter: keep only string elements, skip pure symbol lines
        text_lines = [
            t for t in text_lines
            if isinstance(t, str) and t.strip() and not _SYMBOL_ONLY_RE.match(t.strip())
        ]

        # Dedup repeated blocks
        text_lines, rep = _dedup_repeated_blocks(text_lines)
        if rep:
            cycle, repeats, n = rep
            logging.warning(
                f"{self._log_tag} page={page_1based} ERT text detected repetition "
                f"(cycle={cycle}, repeats={repeats}x), collapsing {n}→{len(text_lines)} lines"
            )

        # ── Call 2: Extract tables as HTML + section classification ──
        raw_table = self._call_vlm(img_bytes, EXAMINATION_TABLE_PROMPT)
        tables_html: list[str] = []
        table_sections: list[str] = []

        if raw_table:
            cleaned = _strip_fence(raw_table).strip()
            parsed = None
            try:
                parsed = _json.loads(cleaned)
            except _json.JSONDecodeError:
                try:
                    from json_repair import repair_json
                    parsed = _json.loads(repair_json(cleaned))
                except Exception:
                    pass
            if isinstance(parsed, dict):
                tables_html = [t for t in parsed.get("tables_html", []) if isinstance(t, str)]
                table_sections = [
                    s for s in parsed.get("table_sections", [])
                    if isinstance(s, str) and s in ("findings", "conclusion")
                ]

        logging.info(
            f"{self._log_tag} page={page_1based} ERT: "
            f"{len(text_lines)} text_lines, {len(tables_html)} tables_html, "
            f"table_sections={table_sections}"
        )

        # Store HTML tables and their section classification for downstream Extractor
        if tables_html:
            self.page_table_html[page_1based - 1] = tables_html
            # Ensure table_sections length matches tables_html
            if len(table_sections) == len(tables_html):
                self.page_table_sections[page_1based - 1] = table_sections
            else:
                logging.warning(
                    f"{self._log_tag} page={page_1based} ERT table_sections length mismatch: "
                    f"{len(table_sections)} vs {len(tables_html)} tables, defaulting all to findings"
                )
                self.page_table_sections[page_1based - 1] = ["findings"] * len(tables_html)

        # Build sections from text lines
        sections: list[SectionTuple] = []
        for line in text_lines:
            text = line.strip()
            if text:
                sections.append((text, page_1based - 1))
                bbox_idx += 1

        return sections, bbox_idx

    def _call_vlm(
        self,
        img_bytes: bytes,
        prompt: str,
        extra_params: Optional[dict] = None,
    ) -> Optional[str]:
        """Call Qwen3-VL API with image + prompt."""
        # 大图预处理：>2MB 或长边>3840 的页面图缩至长边≤3840 JPEG(<1.8MB)，
        # 降低 vLLM prefill 耗时，规避 300s read timeout
        from rag.flow.extractor.vl_image_prep import downscale_vl_image, vl_image_data_url

        img_bytes = downscale_vl_image(img_bytes)
        prompt_tag = "classify" if "table" in prompt.lower() or "text" in prompt.lower() and len(prompt) < 100 else ("table" if "LaTeX" in prompt else "text")
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": vl_image_data_url(img_bytes)},
                        },
                        {"type": "text", "text": prompt},
                    ],
                }
            ],
            "temperature": 0,
            "max_tokens": 16384,
        }
        if extra_params:
            payload.update(extra_params)

        headers = {"Content-Type": "application/json"}
        api_key = self.api_key
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        logging.info(f"{self._log_tag} {prompt_tag} API call start, endpoint={self.api_url}, model={self.model}, img_bytes={len(img_bytes)}, prompt_len={len(prompt)}")

        # 进程级 VL 全局限流：页级并发叠加时防止打爆 vLLM prefill
        from rag.flow.extractor.vl_rate_limit import acquire_vl_slot, release_vl_slot

        max_attempts = self.max_retries + 1
        last_exc: Optional[Exception] = None
        for attempt in range(1, max_attempts + 1):
            acquire_vl_slot()
            try:
                resp = requests.post(
                    self.api_url,
                    json=payload,
                    headers=headers,
                    timeout=self.request_timeout,
                )
                resp.raise_for_status()
                content = resp.json()["choices"][0]["message"]["content"]
                logging.info(f"{self._log_tag} {prompt_tag} API response (len={len(content)}):\n{content}")
                return content
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                # 瞬时网络错误（含 300s read timeout）：重试而非整篇判失败
                last_exc = e
                logging.error(f"{self._log_tag} {prompt_tag} API call failed (attempt {attempt}/{max_attempts}): {e}")
            except requests.exceptions.HTTPError as e:
                # 事故 §11 S6：vLLM 引擎死亡时 APIServer 回 500（EngineDeadError），
                # 容器 ~15s 内自动拉起；5xx 走重试等引擎回来，4xx 快速失败
                if getattr(e.response, "status_code", 0) >= 500:
                    last_exc = e
                    logging.error(
                        f"{self._log_tag} {prompt_tag} engine-dead HTTP "
                        f"{e.response.status_code} (attempt {attempt}/{max_attempts}): {e}"
                    )
                else:
                    logging.error(f"{self._log_tag} {prompt_tag} API call failed: {e}")
                    raise
            except Exception as e:
                logging.error(f"{self._log_tag} {prompt_tag} API call failed: {e}")
                raise
            finally:
                release_vl_slot()
            if attempt < max_attempts:
                logging.warning(f"{self._log_tag} {prompt_tag} retrying in {self.retry_backoff}s")
                time.sleep(self.retry_backoff)
        raise last_exc

    # ── Compat methods (for crop() in downstream) ─────────────────

    def __images__(self, fnm: Any, page_from: int = 0, page_to: int = 100, callback: Any = None) -> None:
        """Compatibility: populate page_images (not used directly by QwenVLParser)."""
        self.page_from = page_from
        try:
            with (
                pdfplumber.open(fnm)
                if isinstance(fnm, (str, PathLike))
                else pdfplumber.open(BytesIO(fnm))
            ) as pdf:
                self.page_images = [
                    p.to_image(resolution=72, antialias=True).original
                    for p in pdf.pages[page_from:page_to]
                ]
        except Exception as e:
            self.page_images = []
            logging.exception(f"{self._log_tag} __images__ failed: {e}")

    @staticmethod
    def extract_positions(txt: str) -> list:
        """Extract position information from text tags."""
        poss = []
        for tag in re.findall(r"@@[0-9-]+\t[0-9.\t]+##", txt):
            pn, left, right, top, bottom = tag.strip("#").strip("@").split("\t")
            left, right, top, bottom = float(left), float(right), float(top), float(bottom)
            poss.append(([int(p) - 1 for p in pn.split("-")], left, right, top, bottom))
        return poss


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = QwenVLParser()
    ok, reason = parser.check_installation()
    print("QwenVL available:", ok, reason)
