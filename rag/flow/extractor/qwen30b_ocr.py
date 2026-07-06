# qwen3-vl-30b-a3b-instruct OCR 处理器
# 使用 qwen3-vl-30b-instruct 替代 qwen-vl-ocr 进行文本和表格 OCR
# 文本处理：提取全量文字 + 坐标，再经 LLM prompt 结构化提取
# 表格处理（LabReport）：直接提取检验项 name/code + bbox，构建 row_positions 和 HTML 表格

import base64
import json
import logging
import os
import re
import time

import json_repair
import requests


# ── 文本 Prompt ──
TEXT_PROMPT = (
    "你是一个专业的医疗文档OCR识别引擎。请逐行识别图片中的所有可见文字内容，包括标题、正文、表格、页脚等。\n"
    "\n"
    "## 规则\n"
    "1. 每一行文字作为一个独立条目，输出该行的完整文本内容和bbox坐标\n"
    "2. 长段落按实际换行拆分为多行，每行单独一条\n"
    "3. 同一行的标签+值（如'性别：女'）合并为一条，不要拆分\n"
    "4. 不得跳过任何可见文字，包括签名、日期、声明、页码等\n"
    "5. bbox为该行文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]\n"
    "\n"
    "## 严格JSON格式要求\n"
    "直接输出JSON数组，每个元素包含text和bbox两个字段。\n"
    "正确示例：\n"
    '[\n'
    '  {"text": "性别：女", "bbox": [100, 200, 250, 230]},\n'
    '  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]},\n'
    '  {"text": "职业：农民", "bbox": [500, 210, 620, 231]}\n'
    ']\n'
    "错误示例（禁止省略字段名）：\n"
    '[\n'
    '  {"text": "性别：女", "bbox": [100, 200, 250, 230]}, "职业：农民", "bbox": [500, 210, 620, 231]}\n'
    ']\n'
    "请直接输出纯JSON数组，不要用markdown代码块包裹。"
)

# ── 纯文本 Prompt（Step3a: 只识别文本，不返回坐标）──
TEXT_ONLY_PROMPT = (
    "你是一个专业的医疗文档OCR识别引擎。请逐行识别图片中的所有可见文字内容。\n"
    "\n"
    "## 规则\n"
    "1. 每一行文字作为一个独立条目\n"
    "2. 长段落按实际换行拆分为多行，每行单独一条\n"
    "3. 同一行的标签+值（如'性别：女'）合并为一条，不要拆分\n"
    "4. 不得跳过任何可见文字，包括签名、日期、声明、页码等\n"
    "5. 严禁重复输出相同内容，每行只输出一次\n"
    "\n"
    "## 输出格式\n"
    "直接输出JSON字符串数组，每个元素是该行的文本内容。\n"
    "正确示例：\n"
    '["性别：女", "年龄：68岁", "职业：农民"]\n'
    "请直接输出纯JSON数组，不要用markdown代码块包裹。"
)

# ── 坐标定位 Prompt（Step7: 根据已知文本定位坐标）──
def _build_table_prompt(item_names: list) -> str:
    """根据已知检验项名称列表，生成定位坐标的 prompt。"""
    names_str = "、".join(item_names)
    return (
        "你是一个专业的医疗文档OCR识别引擎。\n"
        "以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。\n"
        "\n"
        f"## 需要定位的检验项目名称\n"
        f"{names_str}\n"
        "\n"
        "## 规则\n"
        "1. 对于列表中的每个名称，找到它在图片中出现的位置\n"
        "2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]\n"
        "3. 如果某个名称在图片中未找到，可以跳过不输出\n"
        "4. text字段必须与给定的名称完全一致，不要修改或缩写\n"
        "\n"
        "## 严格JSON格式要求\n"
        "直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。\n"
        "正确示例：\n"
        '[\n'
        '  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},\n'
        '  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}\n'
        ']\n'
        "错误示例（禁止额外字段）：\n"
        '[\n'
        '  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}\n'
        ']\n'
        "请直接输出纯JSON数组，不要用markdown代码块包裹。"
    )


def _build_coord_prompt(text_lines: list) -> str:
    """根据已知文本行数组，生成定位坐标的 prompt。"""
    texts_json = json.dumps(text_lines, ensure_ascii=False)
    return (
        "你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。\n"
        "\n"
        f"## 需要定位的文本行（共{len(text_lines)}行）\n"
        f"{texts_json}\n"
        "\n"
        "## 定位规则\n"
        "1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置\n"
        "2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域\n"
        "3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]\n"
        "4. 如果某行文本在图片中未找到，跳过不输出\n"
        "5. text字段必须与给定的文本完全一致\n"
        "\n"
        "## 包围框精度要求\n"
        "- x1必须紧贴该行第一个字符的左边缘\n"
        "- x2必须紧贴该行最后一个字符的右边缘\n"
        "- y1必须紧贴该行文字的顶部\n"
        "- y2必须紧贴该行文字的底部\n"
        "- 禁止将多行文字合并到同一个bbox中\n"
        "\n"
        "## 严格JSON格式要求\n"
        "直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。\n"
        "正确示例：\n"
        '[\n'
        '  {"text": "性别：女", "bbox": [100, 200, 250, 230]},\n'
        '  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}\n'
        ']\n'
        "错误示例（禁止额外字段）：\n"
        '[\n'
        '  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}\n'
        ']\n'
        "请直接输出纯JSON数组，不要用markdown代码块包裹。"
    )

# ── LaTeX 表格 Prompt（Step A: 图片 → LaTeX tabular）──
TABLE_TO_LATEX_PROMPT = (
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

API_ENDPOINT = os.environ.get("QWEN30B_OCR_API_ENDPOINT", "http://10.16.3.16:8090/v1/chat/completions")
MODEL_NAME = os.environ.get("QWEN30B_OCR_MODEL", "Qwen/Qwen3-VL-30B-A3B-Instruct-FP8")


# ── API 调用 ──

def _call_qwen30b(img_bytes: bytes, prompt: str, tag: str) -> tuple:
    """Call qwen3-vl-30b via OpenAI-compatible API (local vLLM or DashScope).

    Args:
        img_bytes: PNG image bytes.
        prompt: Text prompt (TEXT_PROMPT or TABLE_PROMPT).
        tag: Logging tag prefix.

    Returns:
        tuple: (items, elapsed, status)
            items: list of parsed items, or None on failure.
            elapsed: API call duration in seconds.
            status: "ok" or error description.
    """
    api_key = os.environ.get("DASHSCOPE_API_KEY", "")
    b64 = base64.b64encode(img_bytes).decode()
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
            {"type": "text", "text": prompt},
        ]}],
        "max_tokens": 8192,
        "temperature": 0.1,
    }
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    logging.info(f"{tag} API call start, endpoint={API_ENDPOINT}, model={MODEL_NAME}, img_bytes={len(img_bytes)}")
    
    t0 = time.time()
    try:
        r = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=120)
    except requests.RequestException as e:
        elapsed = time.time() - t0
        logging.warning(f"{tag} API request failed: {e}")
        return None, elapsed, f"request error: {e}"
    elapsed = time.time() - t0

    if r.status_code != 200:
        logging.warning(f"{tag} API failed: HTTP {r.status_code}, body={r.text}")
        return None, elapsed, f"HTTP {r.status_code}"

    content = r.json()["choices"][0]["message"]["content"]
    logging.info(f"{tag} API raw response (len={len(content)}):\n{content}")
    # Strip markdown fences
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json|JSON)?\s*\n?", "", content)
        content = re.sub(r"\n?```\s*$", "", content)
        content = content.strip()

    try:
        data = json.loads(content, object_pairs_hook=lambda pairs: dict(pairs))
    except json.JSONDecodeError:
        logging.info(f"{tag} JSON strict parse failed, trying json_repair")
        try:
            data = json_repair.loads(content)
        except Exception as e2:
            logging.warning(f"{tag} json_repair also failed: {e2}, content={content}")
            return None, elapsed, "JSON parse error"

    # 支持两种输出格式：{"items": [...]} 或直接 JSON 数组 [...]
    if isinstance(data, dict):
        raw_items = data.get("items", [])
    elif isinstance(data, list):
        raw_items = data
    else:
        raw_items = []
    valid_items = []
    for it in raw_items:
        if not isinstance(it, dict):
            continue  # 跳过非 dict 元素（如字符串数组）
        # 支持两种字段名：text（通用文本）或 name（表格结构化）
        text = it.get("name") or it.get("text", "")
        bbox = it.get("bbox") or it.get("bbox_2d")
        if text and bbox and len(bbox) == 4:
            item = {"text": text, "bbox": bbox}
            for k in ["code", "result", "reference", "unit"]:
                if k in it:
                    item[k] = it[k]
            valid_items.append(item)
    logging.info(f"{tag} API returned {len(valid_items)} items, elapsed={elapsed:.1f}s")
    return valid_items, elapsed, "ok"


def _call_qwen30b_text_only(img_bytes: bytes, prompt: str, tag: str) -> tuple:
    """Call qwen3-vl-30b and return raw parsed JSON (no item validation).

    Used for text-only extraction (Step3a) and coordinate localization (Step7).

    Returns:
        tuple: (data, elapsed, status)
            data: parsed JSON (list or dict), or None on failure.
    """
    api_key = os.environ.get("DASHSCOPE_API_KEY", "")
    b64 = base64.b64encode(img_bytes).decode()
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
            {"type": "text", "text": prompt},
        ]}],
        "max_tokens": 16384,
        "temperature": 0.1,
    }
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    logging.info(f"{tag} API call start, endpoint={API_ENDPOINT}, model={MODEL_NAME}, img_bytes={len(img_bytes)}")
    t0 = time.time()
    try:
        r = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=120)
    except requests.RequestException as e:
        elapsed = time.time() - t0
        logging.warning(f"{tag} API request failed: {e}")
        return None, elapsed, f"request error: {e}"
    elapsed = time.time() - t0

    if r.status_code != 200:
        logging.warning(f"{tag} API failed: HTTP {r.status_code}, body={r.text}")
        return None, elapsed, f"HTTP {r.status_code}"

    content = r.json()["choices"][0]["message"]["content"]
    logging.info(f"{tag} API raw response (len={len(content)}):\n{content}")

    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json|JSON)?\s*\n?", "", content)
        content = re.sub(r"\n?```\s*$", "", content)
        content = content.strip()

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        try:
            data = json_repair.loads(content)
        except Exception as e2:
            logging.warning(f"{tag} JSON parse failed: {e2}, content={content[:200]}")
            return None, elapsed, "JSON parse error"

    return data, elapsed, "ok"

def _call_qwen30b_raw(img_bytes: bytes, prompt: str, tag: str, system_msg: str = None) -> tuple:
    """Call qwen3-vl-30b and return raw text content (no JSON parsing).

    Used for LaTeX extraction (Step A) where output is LaTeX markup, not JSON.

    Returns:
        tuple: (content, elapsed, status)
            content: raw text string, or None on failure.
    """
    api_key = os.environ.get("DASHSCOPE_API_KEY", "")
    b64 = base64.b64encode(img_bytes).decode()
    messages = [{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
        {"type": "text", "text": prompt},
    ]}]
    if system_msg:
        messages.insert(0, {"role": "system", "content": system_msg})
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": 16384,
        "temperature": 0.1,
    }
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    logging.info(f"{tag} API call start (raw), endpoint={API_ENDPOINT}, model={MODEL_NAME}")
    t0 = time.time()
    try:
        r = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=120)
    except requests.RequestException as e:
        elapsed = time.time() - t0
        logging.warning(f"{tag} API request failed: {e}")
        return None, elapsed, f"request error: {e}"
    elapsed = time.time() - t0

    if r.status_code != 200:
        logging.warning(f"{tag} API failed: HTTP {r.status_code}, body={r.text[:200]}")
        return None, elapsed, f"HTTP {r.status_code}"

    content = r.json()["choices"][0]["message"]["content"]
    logging.info(f"{tag} API raw response (len={len(content)})")
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:latex|tex|json|JSON)?\s*\n?", "", content)
        content = re.sub(r"\n?\s*```$", "", content)
        content = content.strip()
    return content, elapsed, "ok"


# ── 表格处理（LabReport） ──

async def process_table(ext, ck: dict):
    """Process LabReport chunks — 3-step pipeline per page.

    Step A: Image → LaTeX tabular (qwen3-vl-30b, ensures complete item recognition)
    Step B: LaTeX → JSON (pipeline LLM prompt, extracts structured data)
    Step C: Image + item_names → coordinates (qwen3-vl-30b, bbox localization)

    After all pages:
    - Build html_table from all items → content_with_weight
    - Save total JSON → extracted_data.items
    """
    TAG = "[qwen30b-table]"
    try:
        t_start = time.time()

        # ── Step 1: Render pages at 200 DPI ──
        import fitz
        from api.db.services.file2document_service import File2DocumentService
        from common import settings
        from rag.flow.extractor.extractor import strip_markdown_json_fence

        doc_id = ext._canvas._doc_id
        row_positions_raw = ck.get("row_positions", [])
        positions_list = ck.get("positions", [])
        if row_positions_raw:
            src_positions = row_positions_raw
            is_row_positions = True
        elif positions_list:
            src_positions = positions_list
            is_row_positions = False
        else:
            logging.warning(f"{TAG} No positions found in chunk")
            return

        # Group positions by page number
        page_positions = {}
        for p in src_positions:
            if isinstance(p, (list, tuple)) and p:
                pn = int(p[0])
                if is_row_positions:
                    pn = pn - 1  # row_positions 是 1-indexed，转为 0-indexed
                page_positions.setdefault(pn, []).append(p)
        sorted_pages = sorted(page_positions.keys())
        logging.info(
            f"{TAG} ═══ START ═══ type=LabReport, "
            f"doc_id={ck.get('doc_id')}, "
            f"pages={sorted_pages}, "
            f"img_id={ck.get('img_id', '')}"
        )

        b, n = File2DocumentService.get_storage_address(doc_id=doc_id)
        pdf_bytes = settings.STORAGE_IMPL.get(b, n)
        if not pdf_bytes:
            logging.warning(f"{TAG} Step1: Failed to get PDF for doc_id={doc_id}")
            return

        pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        dpi = 200
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)

        page_img_data = []  # [(pn, img_bytes, page_w, page_h, crop_offset_x, crop_offset_y, crop_w, crop_h), ...]
        for pn in sorted_pages:
            if pn < 0 or pn >= len(pdf_doc):
                logging.warning(f"{TAG} Step1: page={pn} out of range (total={len(pdf_doc)}), skipping")
                continue

            page = pdf_doc[pn]
            page_w = page.rect.width
            page_h = page.rect.height
            pix = page.get_pixmap(matrix=mat)
            logging.info(
                f"{TAG} Step1: page={pn}, rect={page_w:.0f}x{page_h:.0f}, "
                f"img=({pix.width}x{pix.height}), positions={len(page_positions.get(pn, []))}"
            )

            # Crop to bounding box of all positions on this page
            crop_offset_x = 0.0
            crop_offset_y = 0.0
            crop_w = page_w
            crop_h = page_h
            page_pos = page_positions.get(pn, [])
            if len(sorted_pages) > 1 and page_pos:
                crop_left = min(float(pp[-4]) for pp in page_pos if len(pp) >= 5)
                crop_right = max(float(pp[-3]) for pp in page_pos if len(pp) >= 5)
                crop_top = min(float(pp[-2]) for pp in page_pos if len(pp) >= 5)
                crop_bottom = max(float(pp[-1]) for pp in page_pos if len(pp) >= 5)
                crop_offset_x = crop_left
                crop_offset_y = crop_top
                crop_w = crop_right - crop_left
                crop_h = crop_bottom - crop_top
                px_l = max(0, int(crop_left * zoom))
                px_t = max(0, int(crop_top * zoom))
                px_r = min(pix.width, int(crop_right * zoom))
                px_b = min(pix.height, int(crop_bottom * zoom))
                if px_r > px_l and px_b > px_t:
                    from PIL import Image
                    import io
                    img = Image.open(io.BytesIO(pix.tobytes("png")))
                    img = img.crop((px_l, px_t, px_r, px_b))
                    buf = io.BytesIO()
                    img.save(buf, format="PNG")
                    img_bytes = buf.getvalue()
                    logging.info(
                        f"{TAG} Step1a: page={pn} cropped to "
                        f"[{crop_left:.0f},{crop_top:.0f},{crop_right:.0f},{crop_bottom:.0f}] pts "
                        f"→ px({px_l},{px_t},{px_r},{px_b}), img=({img.width}x{img.height})"
                    )
                else:
                    logging.warning(f"{TAG} Step1a: page={pn} invalid crop bbox, using full page")
                    img_bytes = pix.tobytes("png")
            else:
                img_bytes = pix.tobytes("png")

            page_img_data.append((pn, img_bytes, page_w, page_h, crop_offset_x, crop_offset_y, crop_w, crop_h))

        pdf_doc.close()

        if not page_img_data:
            logging.warning(f"{TAG} Step1: No valid pages to process")
            return

        # ── Per-page loop: LaTeX → JSON → coordinates ──
        all_items = []
        all_row_positions = []
        # 缓存每页的 item_names，用于 Step C 定位
        page_item_names = {}  # pn -> [names]

        for pn, img_bytes, page_w, page_h, crop_offset_x, crop_offset_y, crop_w, crop_h in page_img_data:
            # ── Step A: Image → LaTeX ──
            latex_content, latex_elapsed, latex_status = _call_qwen30b_raw(
                img_bytes, TABLE_TO_LATEX_PROMPT, TAG,
                system_msg="你是一个医疗文档表格识别专家。请将图片中的表格精确转换为LaTeX tabular格式输出。"
            )
            if latex_status != "ok" or not latex_content:
                logging.warning(f"{TAG} StepA: page={pn} LaTeX failed: {latex_status}")
                continue
            logging.info(
                f"{TAG} StepA: page={pn} — LaTeX: {latex_content}"
                f"time={latex_elapsed:.1f}s"
            )

            # ── Step B: LaTeX → JSON (pipeline LLM prompt) ──
            inputs = ext.get_input_elements()
            chunks_key = next(
                (k for k, v in inputs.items() if isinstance(v.get("value"), list)),
                "text"
            )
            args = {chunks_key: latex_content}
            for _fn, _fv in ck.items():
                if _fn not in ("text", "image", "positions", "img_id", "id", "doc_id", "mom"):
                    args[_fn] = _fv
            msg, sys_prompt = ext._sys_prompt_and_msg([], args)
            msg.insert(0, {"role": "system", "content": sys_prompt})

            json_str = strip_markdown_json_fence(await ext._generate_async(msg))
            logging.info(
                f"{TAG} StepB: page={pn} — JSON :{json_str}"
            )

            # Parse JSON
            try:
                page_data = json.loads(json_str)
            except json.JSONDecodeError as e:
                logging.warning(f"{TAG} StepB: page={pn} JSON parse error: {e}")
                page_data = {}
            if isinstance(page_data, list):
                logging.warning(f"{TAG} StepB: page={pn} JSON is list, skip")
                page_data = {}

            page_items = page_data.get("items", [])
            if not page_items:
                logging.warning(f"{TAG} StepB: page={pn} no items extracted")
                continue

            page_item_names_list = [
                it.get("name", "") or it.get("item_code", "")
                for it in page_items
            ]
            page_item_names_list = [n for n in page_item_names_list if n]
            page_item_names[pn] = page_item_names_list

            logging.info(
                f"{TAG} StepB: page={pn} = {page_items}"
                f"names={page_item_names_list}"
            )

            # 累积 items
            all_items.extend(page_items)

            # ── Step C: 用 item_names 在原图定位坐标 ──
            if page_item_names_list:
                table_prompt = _build_table_prompt(page_item_names_list)
                ocr_items, coord_elapsed, coord_status = _call_qwen30b(
                    img_bytes, table_prompt, TAG
                )
                if coord_status == "ok" and ocr_items:
                    # scale: model 0-1000 → cropped image pts, then offset back to page pts
                    scale_x = crop_w / 1000.0
                    scale_y = crop_h / 1000.0
                    # 构建 lookup: text -> bbox
                    coord_lookup = {}
                    for ocr_item in ocr_items:
                        text = ocr_item.get("text", "")
                        bbox = ocr_item.get("bbox")
                        if text and bbox and len(bbox) == 4:
                            coord_lookup[text] = bbox

                    matched = 0
                    for name in page_item_names_list:
                        bbox = coord_lookup.get(name)
                        if bbox:
                            left = bbox[0] * scale_x + crop_offset_x
                            right = bbox[2] * scale_x + crop_offset_x
                            top = bbox[1] * scale_y + crop_offset_y
                            bottom = bbox[3] * scale_y + crop_offset_y
                            all_row_positions.append([pn + 1, left, right, top, bottom])
                            matched += 1
                        else:
                            all_row_positions.append([0, 0, 0, 0, 0])

                    logging.info(
                        f"{TAG} StepC: page={pn} — matched {matched}/{len(page_item_names_list)}, "
                        f"time={coord_elapsed:.1f}s"
                    )
                else:
                    logging.warning(
                        f"{TAG} StepC: page={pn} coord failed: {coord_status}, "
                        f"adding {len(page_item_names_list)} placeholder(s)"
                    )
                    for _ in page_item_names_list:
                        all_row_positions.append([0, 0, 0, 0, 0])

        if not all_items:
            logging.warning(f"{TAG} No items extracted from any page")
            return

        # ── Build HTML table from all items ──
        html_rows = []
        for it in all_items:
            cells = [
                it.get("name", ""),
                it.get("item_code", ""),
                it.get("value", ""),
                it.get("unit", ""),
                it.get("reference_range", ""),
                it.get("abnormal", ""),
            ]
            html_rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
        html_table = "<table>" + "".join(html_rows) + "</table>"

        # ── Save results ──
        extracted_data = {"items": all_items}
        ck["row_positions"] = all_row_positions
        ck["positions"] = []
        ck["content_with_weight"] = html_table
        ck[ext._param.field_name] = json.dumps(extracted_data, ensure_ascii=False)

        total_matched = sum(1 for rp in all_row_positions if rp[0] != 0)
        elapsed = time.time() - t_start
        logging.info(
            f"{TAG} ═══ DONE ═══ "
            f"items={len(all_items)}, matched={total_matched}, "
            f"pages={len(page_img_data)}, total_time={elapsed:.1f}s"
        )

    except json.JSONDecodeError as e:
        logging.warning(f"{TAG} JSON parse error: {e}")
    except Exception:
        logging.exception(f"{TAG} Unexpected error")


# ── 文本处理（非 LabReport） ──

async def process_text(ext, ck: dict):
    """Process non-LabReport chunks using qwen3-vl-30b-instruct.

    Called from extractor.py when type != LabReport.
    Two-phase OCR: text extraction then coordinate localization.

    Flow:
    1. Get record type (for crop logic)
    2. Render pages at 200 DPI + crop
    3. Call qwen3-vl-30b with TEXT_ONLY_PROMPT per page → text array
    4. Assemble text from JSONArray → ocr_assembled_text
    5. LLM extraction via _sys_prompt_and_msg + _generate_async
    6. Parse extracted JSON + update encounter_date
    7. Call qwen3-vl-30b with coord prompt → bbox arrays, assign to positions
    8. Save results
    """
    TAG = "[qwen30b-text]"
    try:
        t_start = time.time()

        # ── Step 1: Get record type (for crop logic) ──
        classify_raw = ck.get("classify_result_tks", "")
        classify_data = json.loads(classify_raw) if isinstance(classify_raw, str) and classify_raw else {}
        rec_type = classify_data.get("type", "")

        content = ck.get("content_with_weight", "")
        logging.info(
            f"{TAG} ═══ START ═══ type={rec_type}, "
            f"doc_id={ck.get('doc_id')}, "
            f"img_id={ck.get('img_id', '')}, "
            f"content_len={len(content)}"
        )

        # ── Step 2: Render pages at 200 DPI + crop (same logic as _process_qwen_ocr_vl_text) ──
        import fitz
        from api.db.services.file2document_service import File2DocumentService
        from common import settings

        doc_id = ext._canvas._doc_id
        positions = ck.get("positions", [])
        page_positions = {}
        for p in positions:
            if isinstance(p, (list, tuple)) and p:
                pn = int(p[0])
                page_positions.setdefault(pn, []).append(p)
        sorted_pages = sorted(page_positions.keys())
        logging.info(f"{TAG} Step2: {len(sorted_pages)} page(s) {sorted_pages}")

        b, n = File2DocumentService.get_storage_address(doc_id=doc_id)
        pdf_bytes = settings.STORAGE_IMPL.get(b, n)
        if not pdf_bytes:
            logging.warning(f"{TAG} Step2: Failed to get PDF for doc_id={doc_id}")
            return

        pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        dpi = 200
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)

        page_img_data = []  # [(pn, img_bytes, page_w, page_h, crop_offset_x, crop_offset_y, crop_w, crop_h), ...]

        for pn in sorted_pages:
            page_pos = page_positions[pn]
            if pn < 0 or pn >= len(pdf_doc):
                logging.warning(f"{TAG} Step2: page={pn} out of range (total={len(pdf_doc)}), skipping")
                continue

            page = pdf_doc[pn]
            page_w = page.rect.width
            page_h = page.rect.height
            pix = page.get_pixmap(matrix=mat)
            logging.info(
                f"{TAG} Step2: page={pn}, rect={page_w:.0f}x{page_h:.0f}, "
                f"img=({pix.width}x{pix.height}), positions={len(page_pos)}"
            )

            # Crop logic (same as _process_qwen_ocr_vl_text)
            crop_offset_x = 0.0
            crop_offset_y = 0.0
            crop_w = page_w
            crop_h = page_h
            if (len(sorted_pages) > 1 or rec_type in ("PrescriptionRecord", "MedicationRecord")) and page_pos:
                crop_left = min(float(pp[-4]) for pp in page_pos if len(pp) >= 5)
                crop_right = max(float(pp[-3]) for pp in page_pos if len(pp) >= 5)
                crop_top = min(float(pp[-2]) for pp in page_pos if len(pp) >= 5)
                crop_bottom = max(float(pp[-1]) for pp in page_pos if len(pp) >= 5)
                crop_offset_x = crop_left
                crop_offset_y = crop_top
                crop_w = crop_right - crop_left
                crop_h = crop_bottom - crop_top
                px_l = max(0, int(crop_left * zoom))
                px_t = max(0, int(crop_top * zoom))
                px_r = min(pix.width, int(crop_right * zoom))
                px_b = min(pix.height, int(crop_bottom * zoom))
                if px_r > px_l and px_b > px_t:
                    from PIL import Image
                    import io
                    img = Image.open(io.BytesIO(pix.tobytes("png")))
                    img = img.crop((px_l, px_t, px_r, px_b))
                    buf = io.BytesIO()
                    img.save(buf, format="PNG")
                    img_bytes = buf.getvalue()
                    logging.info(
                        f"{TAG} Step2a: page={pn} cropped to "
                        f"[{crop_left:.0f},{crop_top:.0f},{crop_right:.0f},{crop_bottom:.0f}] pts "
                        f"\u2192 px({px_l},{px_t},{px_r},{px_b}), img=({img.width}x{img.height})"
                    )
                else:
                    logging.warning(f"{TAG} Step2a: page={pn} invalid crop bbox, using full page")
                    img_bytes = pix.tobytes("png")
            else:
                img_bytes = pix.tobytes("png")

            page_img_data.append((pn, img_bytes, page_w, page_h, crop_offset_x, crop_offset_y, crop_w, crop_h))

        pdf_doc.close()

        if not page_img_data:
            logging.warning(f"{TAG} Step2: No valid pages to process")
            return

        # ── Step 3: OCR text extraction (text only, no coordinates) ──
        page_text_data = []  # [(pn, text_lines, cox, coy, cw, ch), ...]
        all_page_texts = []

        for pn, img_bytes, page_w, page_h, cox, coy, cw, ch in page_img_data:
            data, api_elapsed, status = _call_qwen30b_text_only(img_bytes, TEXT_ONLY_PROMPT, TAG)
            if status != "ok" or not isinstance(data, list):
                logging.warning(f"{TAG} Step3: page={pn} OCR failed: {status}")
                continue

            # Filter: keep only string elements, skip pure symbol lines (e.g. "++", "--", "+")
            _SYMBOL_ONLY_RE = re.compile(r'^[+\-*=#|~_·•\s]+$')
            text_lines = [t for t in data if isinstance(t, str) and not _SYMBOL_ONLY_RE.match(t.strip())]
            if not text_lines:
                logging.warning(f"{TAG} Step3: page={pn} returned empty text array")
                continue

            # Dedup: detect and truncate repeated content blocks (model hallucination)
            n = len(text_lines)
            if n > 20:
                for cycle in range(3, n // 2 + 1):
                    # Check if lines[cycle:2*cycle] == lines[0:cycle]
                    if text_lines[cycle:2 * cycle] == text_lines[0:cycle]:
                        repeats = n // cycle
                        if repeats >= 2:
                            logging.warning(
                                f"{TAG} Step3: page={pn} detected repetition "
                                f"(cycle={cycle}, repeats={repeats}x), truncating {n}→{cycle} lines"
                            )
                            text_lines = text_lines[:cycle]
                            n = cycle
                            break

            page_text = "\n".join(text_lines)
            page_text_data.append((pn, text_lines, cox, coy, cw, ch))
            all_page_texts.append(page_text)
            logging.info(
                f"{TAG} Step3: page={pn} — {len(text_lines)} lines, "
                f"{len(page_text)} chars, api_time={api_elapsed:.1f}s"
            )

        if not all_page_texts:
            logging.warning(f"{TAG} Step3: No OCR text from any page")
            return

        # ── Step 4: Assemble text → ocr_assembled_text ──
        ocr_assembled_text = "\n".join(all_page_texts)
        old_content_len = len(ck.get("content_with_weight", ""))
        logging.info(
            f"{TAG} Step4: Assembled content ({old_content_len}\u2192{len(ocr_assembled_text)} chars, "
            f"{len(sorted_pages)} pages)\n"
            f"{TAG} Step4: preview:\n{ocr_assembled_text}"
        )

        # ── Step 5: LLM extraction with ocr_assembled_text ──
        inputs = ext.get_input_elements()
        chunks_key = next(
            (k for k, v in inputs.items() if isinstance(v.get("value"), list)),
            "text"
        )
        args = {chunks_key: ocr_assembled_text}
        for _fn, _fv in ck.items():
            if _fn not in ("text", "image", "positions", "img_id", "id", "doc_id", "mom"):
                args[_fn] = _fv
        msg, sys_prompt = ext._sys_prompt_and_msg([], args)
        msg.insert(0, {"role": "system", "content": sys_prompt})

        logging.info(f"{TAG} Step5: ═══ LLM INPUT ═══")
        logging.info(f"{TAG} Step5:   chunks_key='{chunks_key}', text_len={len(ocr_assembled_text)}")
        logging.info(f"{TAG} Step5:   sys_prompt (len={len(sys_prompt)}):\n{sys_prompt}")
        for _mi, _m in enumerate(msg):
            _role = _m.get("role", "")
            _content = _m.get("content", "")
            if isinstance(_content, str):
                logging.info(f"{TAG} Step5:   msg[{_mi}] role={_role} content_len={len(_content)}:\n{_content}")
            else:
                logging.info(f"{TAG} Step5:   msg[{_mi}] role={_role} content={type(_content)}")

        from rag.flow.extractor.extractor import strip_markdown_json_fence
        t_llm = time.time()
        extracted_json_str = strip_markdown_json_fence(await ext._generate_async(msg))
        llm_elapsed = time.time() - t_llm
        logging.info(
            f"{TAG} Step5: ═══ LLM OUTPUT ═══ elapsed={llm_elapsed:.1f}s, "
            f"result_len={len(extracted_json_str)}"
        )
        logging.info(f"{TAG} Step5: raw_output:\n{extracted_json_str}")

        # ── Step 6: Parse extracted JSON ──
        try:
            extracted_data = json.loads(extracted_json_str)
        except json.JSONDecodeError as e:
            logging.warning(f"{TAG} JSON parse error: {e}, raw={extracted_json_str}")
            return

        if isinstance(extracted_data, list):
            logging.warning(f"{TAG} extracted_data is list (len={len(extracted_data)}), skip saves")
            return

        # Save results
        ck["content_with_weight"] = ocr_assembled_text
        ck["text"] = ocr_assembled_text
        ck[ext._param.field_name] = extracted_json_str

        # ── Step 6a: Update encounter_date → classify_result_tks ──
        encounter_date = extracted_data.get("encounter_date")
        if encounter_date:
            try:
                classify_raw = ck.get("classify_result_tks", "")
                classify_data = json.loads(classify_raw) if isinstance(classify_raw, str) else classify_raw
                classify_data["encounter_dates"] = [encounter_date]
                ck["classify_result_tks"] = json.dumps(classify_data, ensure_ascii=False)
                logging.info(f"{TAG} Step6a: Updated encounter_dates=[{encounter_date}]")
            except Exception as e:
                logging.warning(f"{TAG} Step6a: Failed to update encounter_dates: {e}")

        # ── Step 7: Coordinate localization — find bbox for each text line ──
        new_positions = []
        for pn, text_lines, cox, coy, cw, ch in page_text_data:
            coord_prompt = _build_coord_prompt(text_lines)
            img_bytes = next(ib for _pn, ib, *_ in page_img_data if _pn == pn)
            ocr_items, api_elapsed, status = _call_qwen30b(img_bytes, coord_prompt, TAG)
            if status != "ok" or not ocr_items:
                logging.warning(f"{TAG} Step7: page={pn} coord failed: {status}, "
                                f"adding {len(text_lines)} placeholder(s)")
                # 坐标提取失败时仍为每行文本添加占位，保持与文本行 1:1 对齐
                for _ in text_lines:
                    new_positions.append([pn, 0, 0, 0, 0])
                continue

            # Build lookup: text -> bbox
            coord_lookup = {}
            for ocr_item in ocr_items:
                text = ocr_item.get("text", "")
                bbox = ocr_item.get("bbox")
                if text and bbox and len(bbox) == 4:
                    coord_lookup[text] = bbox

            scale_x = cw / 1000.0
            scale_y = ch / 1000.0

            # ── 按 text_lines 顺序收集 bbox，未匹配的标记 None ──
            raw_bboxes = []
            for tl in text_lines:
                bbox = coord_lookup.get(tl)
                if bbox:
                    raw_bboxes.append(list(bbox))
                else:
                    raw_bboxes.append(None)

            # ── 计算平均行高，插值填充 null bbox ──
            heights = [b[3] - b[1] for b in raw_bboxes if b is not None]
            avg_h = sum(heights) / len(heights) if heights else 20

            for i in range(len(raw_bboxes)):
                if raw_bboxes[i] is None:
                    nxt = next((j for j in range(i + 1, len(raw_bboxes)) if raw_bboxes[j] is not None), None)
                    if nxt is not None:
                        gap = nxt - i
                        est_top = raw_bboxes[nxt][1] - avg_h * gap
                        est_bot = raw_bboxes[nxt][3] - avg_h * gap
                        raw_bboxes[i] = [raw_bboxes[nxt][0], est_top, raw_bboxes[nxt][2], est_bot]
                    else:
                        prv = next((j for j in range(i - 1, -1, -1) if raw_bboxes[j] is not None), None)
                        if prv is not None:
                            gap = i - prv
                            est_top = raw_bboxes[prv][1] + avg_h * gap
                            est_bot = raw_bboxes[prv][3] + avg_h * gap
                            raw_bboxes[i] = [raw_bboxes[prv][0], est_top, raw_bboxes[prv][2], est_bot]

            # ── 转换为 PDF 坐标 ──
            matched = sum(1 for b in raw_bboxes if b is not None)
            for bbox in raw_bboxes:
                if bbox is not None:
                    left = bbox[0] * scale_x + cox
                    right = bbox[2] * scale_x + cox
                    top = bbox[1] * scale_y + coy
                    bottom = bbox[3] * scale_y + coy
                    new_positions.append([pn, left, right, top, bottom])
                else:
                    new_positions.append([pn, 0, 0, 0, 0])

            logging.info(
                f"{TAG} Step7: page={pn} — {matched}/{len(text_lines)} coords, "
                f"api_time={api_elapsed:.1f}s"
            )

        # 保留所有占位，确保与文本行 1:1 对齐
        ck["positions"] = new_positions
        ck["row_positions"] = []
        logging.info(f"{TAG} Step7: {len(ck['positions'])} positions stored, row_positions=[]")

        # ── Step 8: Save extracted_data ──
        ck[ext._param.field_name] = json.dumps(extracted_data, ensure_ascii=False)
        elapsed = time.time() - t_start
        logging.info(
            f"{TAG} ═══ DONE ═══ "
            f"{len(new_positions)} positions, "
            f"total_time={elapsed:.1f}s (OCR {len(sorted_pages)} page(s) + LLM)"
        )

    except json.JSONDecodeError as e:
        logging.warning(f"{TAG} JSON parse error: {e}")
    except Exception:
        logging.exception(f"{TAG} Unexpected error")
