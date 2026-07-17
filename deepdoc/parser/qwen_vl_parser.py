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

TAG = "[qwen-vl-parser]"
_logger = logging.getLogger("qwen_vl_parser")

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
    '- 这是一份检验报告单/化验单/检查报告（如血常规、尿常规、生化检验、免疫检验等）\n'
    '- 内容以检验指标表格为主体（有序号、项目名称、结果、参考值、单位等列）\n'
    '\n'
    '输出 text 的情况（以下全部归为 text）：\n'
    '- 门诊病历、入院记录、出院记录、病程记录\n'
    '- 处方、购药单\n'
    '- 收费票据、发票、收据（即使有费用明细表格）\n'
    '- 诊断证明、诊断报告、检查报告单（影像/病理/心电图等）\n'
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
    '关键区分：收费票据/发票/收据虽然可能有费用表格，但不是检验报告，type 必须输出 text。'
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
    "5. **保留原文**：所有可见文字原样输出，包括空格、↑↓箭头、★符号、H/L标识等。\n"
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

    def __init__(
        self,
        api_url: Optional[str] = None,
        model: Optional[str] = None,
        *,
        request_timeout: int = 300,
    ):
        super().__init__()

        self.outlines: list = []
        self.api_url = api_url or os.getenv(
            "QWEN30B_OCR_API_ENDPOINT",
            "http://10.16.3.16:8090/v1/chat/completions",
        )
        self.model = model or os.getenv(
            "QWEN30B_OCR_MODEL",
            "Qwen/Qwen3-VL-30B-A3B-Instruct-FP8",
        )
        self.request_timeout = request_timeout
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
            logging.warning(f"{TAG} Failed to render page images: {e}")
            self.page_images = []

        if not self.page_images:
            if callback:
                callback(1, "[QwenVL] No pages to process.")
            return [], []

        total_pages = len(self.page_images)
        if callback:
            callback(0.1, f"[QwenVL] Processing {total_pages} pages...")

        logging.info(f"{TAG} parse_pdf start, total_pages={total_pages}")

        sections: list[SectionTuple] = []
        bbox_idx = 0  # global BBOX counter

        for page_idx in range(total_pages):
            page_img = self.page_images[page_idx]
            page_1based = page_idx + 1

            # Convert page image to bytes
            buf = BytesIO()
            page_img.save(buf, format="PNG")
            img_bytes = buf.getvalue()

            # Step 1: Classify page
            page_type, report_date = self._classify_page(img_bytes)
            logging.info(f"{TAG} page={page_1based} classify={page_type} report_date={report_date}")

            if callback:
                progress = 0.1 + 0.8 * (page_idx / total_pages)
                callback(progress, f"[QwenVL] page {page_1based}/{total_pages} ({page_type})")

            # Step 2: Extract content based on type
            if page_type == "table":
                page_sections, bbox_idx = self._extract_table_page(
                    img_bytes, page_1based, bbox_idx, report_date
                )
            else:
                page_sections, bbox_idx = self._extract_text_page(
                    img_bytes, page_1based, bbox_idx
                )

            logging.info(
                f"{TAG} page={page_1based} {page_type}: {len(page_sections)} sections"
            )
            sections.extend(page_sections)

        logging.info(f"{TAG} parse_pdf done: {len(sections)} sections from {total_pages} pages.")

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
            logging.error(f"{TAG} render_page_images failed: {e}")
            raise

    def _classify_page(self, img_bytes: bytes) -> tuple[str, Optional[str]]:
        """Classify page as 'text' or 'table' via VLM, also extract report_date."""
        try:
            raw = self._call_vlm(img_bytes, CLASSIFY_PROMPT)
            if not raw:
                return "text", None

            # Try to parse JSON response
            raw = raw.strip()
            # Strip markdown code fences if present
            raw = re.sub(r"^```(?:json)?\s*\n?", "", raw)
            raw = re.sub(r"\n?\s*```$", "", raw)
            raw = raw.strip()

            import json
            try:
                result = json.loads(raw)
                page_type = result.get("type", "text").lower()
                report_date = result.get("report_date", None)
                if page_type not in ("table", "text"):
                    page_type = "text"
                return page_type, report_date
            except json.JSONDecodeError:
                # Fallback: check if raw contains "table"
                if "table" in raw.lower():
                    return "table", None
                return "text", None

        except Exception as e:
            logging.warning(f"{TAG} classify failed: {e}, defaulting to text")
            return "text", None

    def _extract_text_page(
        self, img_bytes: bytes, page_1based: int, bbox_idx: int
    ) -> tuple[list[SectionTuple], int]:
        """Extract text page via VLM → JSON array → sections."""
        raw = self._call_vlm(img_bytes, TEXT_PROMPT)
        lines = _parse_json_array(raw)

        if not lines:
            logging.warning(f"{TAG} page={page_1based} text extraction returned no lines")
            return [], bbox_idx

        # Filter: keep only string elements, skip pure symbol lines (e.g. "++", "--", "+")
        _SYMBOL_ONLY_RE = re.compile(r'^[+\-*=#|~_·•\s]+$')
        lines = [t for t in lines if isinstance(t, str) and not _SYMBOL_ONLY_RE.match(t.strip())]

        # Dedup: detect and truncate repeated content blocks (model hallucination)
        n = len(lines)
        if n > 20:
            for cycle in range(3, n // 2 + 1):
                if lines[cycle:2 * cycle] == lines[0:cycle]:
                    repeats = n // cycle
                    if repeats >= 2:
                        logging.warning(
                            f"{TAG} page={page_1based} detected repetition "
                            f"(cycle={cycle}, repeats={repeats}x), truncating {n}→{cycle} lines"
                        )
                        lines = lines[:cycle]
                        break

        if not lines:
            logging.warning(f"{TAG} page={page_1based} text extraction returned no lines after filtering")
            return [], bbox_idx

        sections: list[SectionTuple] = []

        for line in lines:
            text = line.strip()
            if not text:
                continue
            sections.append((text, page_1based - 1))  # store 0-based, consistent with PaddleOCR-VL
            bbox_idx += 1

        logging.info(
            f"{TAG} page={page_1based} text: {len(sections)} lines "
            f"(bbox {bbox_idx - len(sections)}-{bbox_idx - 1})"
        )
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
            logging.warning(f"{TAG} page={page_1based} table extraction returned empty")
            return [], bbox_idx

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

        logging.info(
            f"{TAG} page={page_1based} table: {len(sections)} LaTeX lines "
            f"(bbox {bbox_idx - len(sections)}-{bbox_idx - 1})"
        )
        return sections, bbox_idx

    def _call_vlm(self, img_bytes: bytes, prompt: str) -> Optional[str]:
        """Call Qwen3-VL API with image + prompt."""
        b64 = base64.b64encode(img_bytes).decode("ascii")
        prompt_tag = "classify" if "table" in prompt.lower() or "text" in prompt.lower() and len(prompt) < 100 else ("table" if "LaTeX" in prompt else "text")
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{b64}"},
                        },
                        {"type": "text", "text": prompt},
                    ],
                }
            ],
            "temperature": 0,
            "max_tokens": 16384,
        }

        headers = {"Content-Type": "application/json"}
        api_key = os.environ.get("DASHSCOPE_API_KEY", "")
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        logging.info(f"{TAG} {prompt_tag} API call start, endpoint={self.api_url}, model={self.model}, img_bytes={len(img_bytes)}, prompt_len={len(prompt)}")

        try:
            resp = requests.post(
                self.api_url,
                json=payload,
                headers=headers,
                timeout=self.request_timeout,
            )
            resp.raise_for_status()
            content = resp.json()["choices"][0]["message"]["content"]
            logging.info(f"{TAG} {prompt_tag} API response (len={len(content)}):\n{content}")
            return content
        except Exception as e:
            logging.error(f"{TAG} {prompt_tag} API call failed: {e}")
            raise

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
            logging.exception(f"{TAG} __images__ failed: {e}")

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
