# qwen_vl_ocr.py — QwenVLParser 坐标定位处理器
# 当 OCR_PARSER=qwen-vl 时由 extractor.py 调用
#
# 职责：
#   - LabReport:  用 extracted_data.items[].name 在对应页图片上定位坐标 → row_positions
#   - 非LabReport: 对 BBOX 包装的文本做 LLM 提取 + 用文本行定位坐标 → positions
#
# 关键区别（vs qwen30b_ocr.py）：
#   - 不裁剪图片（positions 后4位全为 0，无有效裁剪框）
#   - 文本已由 QwenVLParser 提取，不需要再做 text-only OCR

import base64
import json
import logging
import os
import re
import time

import json_repair
import requests


# ── 坐标定位 Prompt（复用 qwen30b_ocr 的逻辑）──

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


API_ENDPOINT = os.environ.get("QWEN30B_OCR_API_ENDPOINT", "http://10.16.3.16:8090/v1/chat/completions")
MODEL_NAME = os.environ.get("QWEN30B_OCR_MODEL", "Qwen/Qwen3-VL-30B-A3B-Instruct-FP8")


def _call_qwen30b_coord(img_bytes: bytes, prompt: str, tag: str, page_num: int = 0) -> tuple:
    """Call qwen3-vl-30b for coordinate localization.

    Returns:
        tuple: (items, elapsed, status)
            items: list of {"text": ..., "bbox": [x1,y1,x2,y2]}, or None
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
        "temperature": 0,
    }
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    logging.info(
        f"{tag} coord API call start, page={page_num}, endpoint={API_ENDPOINT}, "
        f"model={MODEL_NAME}, img_bytes={len(img_bytes)}, prompt_len={len(prompt)}\n"
        f"{tag} coord prompt:\n{prompt}"
    )
    t0 = time.time()
    try:
        r = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=120)
    except requests.RequestException as e:
        elapsed = time.time() - t0
        logging.warning(f"{tag} coord API request failed: {e}")
        return None, elapsed, f"request error: {e}"
    elapsed = time.time() - t0

    if r.status_code != 200:
        logging.warning(f"{tag} coord API failed: HTTP {r.status_code}, body={r.text}")
        return None, elapsed, f"HTTP {r.status_code}"

    content = r.json()["choices"][0]["message"]["content"]
    logging.info(f"{tag} coord API raw response (len={len(content)}):\n{content}")

    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json|JSON)?\s*\n?", "", content)
        content = re.sub(r"\n?```\s*$", "", content)
        content = content.strip()

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        logging.info(f"{tag} coord JSON strict parse failed, trying json_repair")
        try:
            data = json_repair.loads(content)
        except Exception as e2:
            logging.warning(f"{tag} coord json_repair also failed: {e2}, content={content}")
            return None, elapsed, "JSON parse error"

    if isinstance(data, dict):
        raw_items = data.get("items", [])
    elif isinstance(data, list):
        raw_items = data
    else:
        raw_items = []

    valid_items = []
    for it in raw_items:
        if not isinstance(it, dict):
            continue
        text = it.get("name") or it.get("text", "")
        bbox = it.get("bbox") or it.get("bbox_2d")
        if text and bbox and len(bbox) == 4:
            valid_items.append({"text": text, "bbox": bbox})

    logging.info(
        f"{tag} coord API: raw_items={len(raw_items)}, valid_items={len(valid_items)}, "
        f"elapsed={elapsed:.1f}s"
    )
    for i, vi in enumerate(valid_items):
        logging.info(f"{tag} coord item[{i}]: text={vi['text']}, bbox={vi['bbox']}")
    return valid_items, elapsed, "ok"


def _fuzzy_lookup_bbox(name: str, coord_lookup: dict, threshold: float = 0.5):
    """Fuzzy bbox lookup with LCS similarity fallback."""
    if name in coord_lookup:
        return coord_lookup[name]

    name_clean = name.lstrip("*").strip()
    for key, bbox in coord_lookup.items():
        if key.lstrip("*").strip() == name_clean:
            return bbox

    best_bbox, best_score = None, 0.0
    for key, bbox in coord_lookup.items():
        key_clean = key.lstrip("*").strip()
        m, n = len(name_clean), len(key_clean)
        if m == 0 or n == 0:
            continue
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if name_clean[i - 1] == key_clean[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        lcs_len = dp[m][n]
        score = lcs_len / max(m, n) if max(m, n) > 0 else 0
        if score > best_score:
            best_score = score
            best_bbox = bbox if score >= threshold else None
    return best_bbox if best_score >= threshold else None


def _strip_bbox_tags(text: str) -> str:
    """Strip [BBOX-N] ... [BBOX-N] wrappers, return clean text."""
    return re.sub(r"\[BBOX-\d+\]\s*", "", text).strip()


def _fix_tabular_colspec(latex: str, max_cols: int = 20) -> str:
    """Collapse degenerate tabular column specs like {l l l l l ... (500+)}."""
    def _replace_colspec(m: re.Match) -> str:
        spec = m.group(2)
        cols = re.findall(r'[lcrpmbX]', spec)
        if len(cols) > max_cols:
            return f"{m.group(1)}{{{('c' * max_cols)}}}"
        return m.group(0)
    return re.sub(
        r'(\\begin\{tabular\*?\})\{([^}]{30,})\}',
        _replace_colspec,
        latex,
    )


def _latex_to_plain_text(line: str) -> str:
    """Convert a LaTeX line to plain text for coordinate localization.

    If the line contains LaTeX tabular syntax (\\begin, \\end, &, \\\\\\),
    extract cell contents and join with spaces.
    Otherwise return as-is.
    """
    # Detect LaTeX tabular content
    if not re.search(r"\\begin\{|\\end\{|\\hline|&|\\\\", line):
        return line

    # Strip \begin{tabular}{...}, \end{tabular}, \hline
    line = re.sub(r"\\begin\{tabular\}\{[^}]*\}", "", line)
    line = re.sub(r"\\end\{tabular\}", "", line)
    line = re.sub(r"\\hline", "", line)

    # Split cells by & and join
    cells = [c.strip() for c in line.split("&")]
    # Strip trailing \\
    cells = [re.sub(r"\\\\+$", "", c).strip() for c in cells]
    # Strip LaTeX escapes
    cells = [re.sub(r"\\([#%&_~{}])", r"\1", c) for c in cells]
    cells = [re.sub(r"\\text[a-z]+\{([^}]*)\}", r"\1", c) for c in cells]
    cells = [c for c in cells if c]

    return " ".join(cells)


def _render_page_image(doc_id: str, page_num_0based: int, tag: str):
    """Render a single PDF page at 200 DPI. No cropping.

    Returns:
        tuple: (img_bytes, page_w, page_h) or (None, 0, 0) on failure.
    """
    import fitz
    from api.db.services.file2document_service import File2DocumentService
    from common import settings

    b, n = File2DocumentService.get_storage_address(doc_id=doc_id)
    pdf_bytes = settings.STORAGE_IMPL.get(b, n)
    if not pdf_bytes:
        logging.warning(f"{tag} Failed to get PDF for doc_id={doc_id}")
        return None, 0, 0

    pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    if page_num_0based < 0 or page_num_0based >= len(pdf_doc):
        logging.warning(f"{tag} page={page_num_0based} out of range (total={len(pdf_doc)})")
        pdf_doc.close()
        return None, 0, 0

    page = pdf_doc[page_num_0based]
    page_w = page.rect.width
    page_h = page.rect.height
    dpi = 200
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    img_bytes = pix.tobytes("png")
    pdf_doc.close()

    logging.info(
        f"{tag} page={page_num_0based}, rect={page_w:.0f}x{page_h:.0f}, "
        f"img=({pix.width}x{pix.height}), dpi={dpi}"
    )
    return img_bytes, page_w, page_h


# ── LabReport 处理（用 item name 定位坐标，不裁剪，支持多页） ──

async def process_table(ext, ck: dict):
    """Process LabReport chunks when OCR_PARSER=qwen-vl.

    Multi-page support: groups positions by page, processes each page independently.
    2-step pipeline per page (vs qwen30b_ocr's 3-step — Step A skipped since
    QwenVLParser already extracted LaTeX):
      Step B: LaTeX → JSON (LLM extraction)
      Step C: item names → coordinate localization on page image

    No image cropping (positions last 4 values are 0).
    """
    TAG = "[qwen-vl-table]"
    try:
        t_start = time.time()

        doc_id = ext._canvas._doc_id
        from rag.flow.extractor.extractor import strip_markdown_json_fence
        import fitz
        from api.db.services.file2document_service import File2DocumentService
        from common import settings

        # ── Step 1: Group positions by page, render page images (no crop) ──
        positions = ck.get("positions", [])
        page_positions = {}
        for p in positions:
            if isinstance(p, (list, tuple)) and p:
                pn = int(p[0])
                page_positions.setdefault(pn, []).append(p)
        sorted_pages = sorted(page_positions.keys())

        
        logging.info(
            f"{TAG} ═══ START ═══ doc_id={ck.get('doc_id')}, "
            f"pages={sorted_pages}"
        )
        logging.info(f"{TAG} positions ： {positions}")
        
        b, n = File2DocumentService.get_storage_address(doc_id=doc_id)
        pdf_bytes = settings.STORAGE_IMPL.get(b, n)
        if not pdf_bytes:
            logging.warning(f"{TAG} Failed to get PDF for doc_id={doc_id}")
            return

        pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        dpi = 200
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)

        page_img_data = {}  # pn → (img_bytes, page_w, page_h)
        for pn in sorted_pages:
            pn_0based = pn  # positions are 1-based, fitz needs 0-based
            if pn_0based < 0 or pn_0based >= len(pdf_doc):
                logging.warning(f"{TAG} page={pn} out of range (total={len(pdf_doc)}), skipping")
                continue
            page = pdf_doc[pn_0based]
            page_w = page.rect.width
            page_h = page.rect.height
            pix = page.get_pixmap(matrix=mat)
            img_bytes = pix.tobytes("png")
            page_img_data[pn] = (img_bytes, page_w, page_h)
            logging.info(
                f"{TAG} page={pn}, rect={page_w:.0f}x{page_h:.0f}, "
                f"img=({pix.width}x{pix.height})"
            )
        pdf_doc.close()

        if not page_img_data:
            logging.warning(f"{TAG} No page images rendered")
            return

        # ── Step 2: Get LaTeX content (already extracted by QwenVLParser) ──
        # Strip BBOX tags + LaTeX→plain text for LLM input
        raw_text = ck.get("text", "") or ck.get("content_with_weight", "")
        if not raw_text:
            logging.warning(f"{TAG} No LaTeX content in chunk")
            return

        # Split by page using BBOX position mapping
        # Build page→text mapping from positions
        page_text_map = {}  # pn → list of text lines for that page
        if len(sorted_pages) == 1:
            # Single page: all text belongs to that page
            page_text_map[sorted_pages[0]] = raw_text
        else:
            # Multi-page: split BBOX-wrapped lines by page number
            # Build bbox_idx → page_num lookup from positions
            bbox_to_page = {}
            for p in positions:
                if isinstance(p, (list, tuple)) and len(p) >= 1:
                    pn = int(p[0])
                    # Each position corresponds to a section; use index as bbox hint
                    pass
            # Fallback: split lines and distribute by page order
            lines = raw_text.split("\n")
            chunk_size = max(1, len(lines) // len(sorted_pages))
            for i, pn in enumerate(sorted_pages):
                start = i * chunk_size
                end = start + chunk_size if i < len(sorted_pages) - 1 else len(lines)
                page_text_map[pn] = "\n".join(lines[start:end])

        # ── Per-page loop: Step B (LaTeX→JSON) ──
        all_items = []
        all_row_positions = []

        # Build name → source page mapping from raw_text + positions
        raw_lines = raw_text.split("\n")
        name_to_page = {}  # cleaned_line → page_num
        for i, raw_line in enumerate(raw_lines):
            clean = _strip_bbox_tags(raw_line.strip())
            if not clean:
                continue
            if i < len(positions) and isinstance(positions[i], (list, tuple)) and positions[i]:
                pn = int(positions[i][0])
            elif positions and isinstance(positions[0], (list, tuple)) and positions[0]:
                pn = int(positions[0][0])
            else:
                pn = sorted_pages[0] if sorted_pages else 0
            name_to_page[clean] = pn

        for pn in sorted_pages:
            if pn not in page_img_data:
                continue
            page_latex = page_text_map.get(pn, "").strip()
            if not page_latex:
                logging.warning(f"{TAG} page={pn}: no LaTeX content, skip")
                continue

            # Strip BBOX tags before sending to LLM
            page_latex_clean = "\n".join(
                _strip_bbox_tags(line) for line in page_latex.split("\n") if _strip_bbox_tags(line)
            )
            # Fix degenerate column specs (VLM hallucination)
            page_latex_clean = _fix_tabular_colspec(page_latex_clean)
            if not page_latex_clean:
                logging.warning(f"{TAG} page={pn}: empty after BBOX stripping, skip")
                continue

            # ── Step B: LaTeX → JSON (LLM extraction) ──
            inputs = ext.get_input_elements()
            chunks_key = next(
                (k for k, v in inputs.items() if isinstance(v.get("value"), list)),
                "text"
            )
            args = {chunks_key: page_latex_clean}
            # Ensure 'text' key always has content (prompt templates reference {text})
            if chunks_key != "text":
                args["text"] = page_latex_clean
            for _fn, _fv in ck.items():
                if _fn not in ("text", "image", "positions", "img_id", "id", "doc_id", "mom"):
                    args[_fn] = _fv
            msg, sys_prompt = ext._sys_prompt_and_msg([], args)
            msg.insert(0, {"role": "system", "content": sys_prompt})

            # Skip LLM call if user message content is empty
            user_content = next((m["content"] for m in msg if m.get("role") == "user"), "")
            if not user_content or not user_content.strip():
                logging.warning(f"{TAG} page={pn}: user message is empty, skip LLM")
                continue

            json_str = strip_markdown_json_fence(await ext._generate_async(msg))
            logging.info(f"{TAG} page={pn} LLM output (len={len(json_str)}):\n{json_str}")

            try:
                page_data = json.loads(json_str)
            except json.JSONDecodeError as e:
                logging.warning(f"{TAG} page={pn} JSON parse error: {e}")
                continue

            if isinstance(page_data, list):
                logging.warning(f"{TAG} page={pn} JSON is list, skip")
                continue

            page_items = page_data.get("items", [])
            if not page_items:
                logging.warning(f"{TAG} page={pn} no items extracted")
                continue

            all_items.extend(page_items)

        # ── Step C: Locate item names — group by SOURCE page from positions ──
        # Each item_name → find in raw_text lines → positions[i][0] = source page
        page_item_names = {}  # source_pn → [name, ...]
        for it in all_items:
            name = it.get("name", "") or it.get("item_code", "")
            if not name:
                continue
            # Find source page: exact match first, then substring
            source_pn = name_to_page.get(name)
            if source_pn is None:
                for line_text, line_pn in name_to_page.items():
                    if name in line_text or line_text in name:
                        source_pn = line_pn
                        break
            if source_pn is None:
                source_pn = sorted_pages[0] if sorted_pages else 0
            page_item_names.setdefault(source_pn, []).append(name)

        logging.info(
            f"{TAG} coord grouping: { {pn: len(names) for pn, names in page_item_names.items()} }"
        )

        for pn, names in page_item_names.items():
            if pn not in page_img_data:
                logging.warning(f"{TAG} page={pn}: no page image, skip coord")
                for _ in names:
                    all_row_positions.append([0, 0, 0, 0, 0])
                continue

            img_bytes, page_w, page_h = page_img_data[pn]
            table_prompt = _build_table_prompt(names)
            ocr_items, coord_elapsed, coord_status = _call_qwen30b_coord(
                img_bytes, table_prompt, TAG, page_num=pn
            )
            if coord_status == "ok" and ocr_items:
                scale_x = page_w / 1000.0
                scale_y = page_h / 1000.0
                coord_lookup = {}
                for ocr_item in ocr_items:
                    coord_lookup[ocr_item["text"]] = ocr_item["bbox"]

                matched = 0
                for name in names:
                    bbox = coord_lookup.get(name)
                    if not bbox:
                        bbox = _fuzzy_lookup_bbox(name, coord_lookup)
                    if bbox:
                        left = bbox[0] * scale_x
                        right = bbox[2] * scale_x
                        top = bbox[1] * scale_y
                        bottom = bbox[3] * scale_y
                        all_row_positions.append([pn+1, left, right, top, bottom])
                        matched += 1
                    else:
                        all_row_positions.append([0, 0, 0, 0, 0])

                logging.info(
                    f"{TAG} page={pn} coord: matched {matched}/{len(names)}, "
                    f"time={coord_elapsed:.1f}s"
                )
            else:
                logging.warning(f"{TAG} page={pn} coord failed: {coord_status}")
                for _ in names:
                    all_row_positions.append([0, 0, 0, 0, 0])

        logging.info(f"{TAG} new_positions ({len(all_row_positions)}):\n{all_row_positions}")

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
        ck["text"] = html_table
        ck[ext._param.field_name] = json.dumps(extracted_data, ensure_ascii=False)

        total_matched = sum(1 for rp in all_row_positions if rp[0] != 0)
        elapsed = time.time() - t_start
        logging.info(
            f"{TAG} ═══ DONE ═══ items={len(all_items)}, matched={total_matched}, "
            f"pages={len(page_img_data)}, time={elapsed:.1f}s"
        )

    except json.JSONDecodeError as e:
        logging.warning(f"{TAG} JSON parse error: {e}")
    except Exception:
        logging.exception(f"{TAG} Unexpected error")


# ── 非 LabReport 文本处理（用文本行定位坐标，不裁剪） ──

async def process_text(ext, ck: dict):
    """Process non-LabReport chunks when OCR_PARSER=qwen-vl.

    The chunk text is already extracted by QwenVLParser (BBOX-wrapped).
    1. Strip BBOX tags → clean text lines
    2. LLM extraction → extracted_data
    3. Use text lines to locate coordinates on page image
    4. Store in positions

    No image cropping (positions last 4 values are 0).
    """
    TAG = "[qwen-vl-text]"
    try:
        t_start = time.time()

        doc_id = ext._canvas._doc_id
        from rag.flow.extractor.extractor import strip_markdown_json_fence

        # ── Get record type ──
        classify_raw = ck.get("classify_result_tks", "")
        classify_data = json.loads(classify_raw) if isinstance(classify_raw, str) and classify_raw else {}
        rec_type = classify_data.get("type", "")

        logging.info(
            f"{TAG} ═══ START ═══ type={rec_type}, "
            f"doc_id={ck.get('doc_id')}"
        )

        # ── Step 1: Get text, strip BBOX tags → text lines ──
        raw_text = ck.get("text", "")
        if not raw_text:
            raw_text = ck.get("content_with_weight", "")
        if not raw_text:
            logging.warning(f"{TAG} No text in chunk")
            return

        # ── Step 1a: Get positions, determine page per line ──
        positions = ck.get("positions", [])
        logging.info(f"{TAG} positions({len(positions)}): {positions}")

        # raw_text 按 \n 分割后与 positions 一一对应，
        # 每行文本用 positions[i][0] 的页码决定归属哪一页
        raw_lines = raw_text.split("\n")
        page_text_lines = {}  # pn → [cleaned_text_line, ...]
        for i, raw_line in enumerate(raw_lines):
            clean = _strip_bbox_tags(raw_line.strip())
            if not clean:
                continue
            clean = _latex_to_plain_text(clean)
            if not clean:
                continue
            # 确定该行所属页码
            if i < len(positions) and isinstance(positions[i], (list, tuple)) and positions[i]:
                pn = int(positions[i][0])
            elif positions and isinstance(positions[0], (list, tuple)) and positions[0]:
                pn = int(positions[0][0])  # fallback: 用第一个 position 的页码
            else:
                pn = 0
            page_text_lines.setdefault(pn, []).append(clean)

        text_lines = [line for lines in page_text_lines.values() for line in lines]
        if not text_lines:
            logging.warning(f"{TAG} No text lines after stripping BBOX tags")
            return

        sorted_pages = sorted(page_text_lines.keys())
        logging.info(
            f"{TAG} page grouping: {sorted_pages}, "
            f"lines per page: {[len(page_text_lines[p]) for p in sorted_pages]}"
        )

        # Render page images (no cropping)
        page_img_data = {}  # pn → (img_bytes, page_w, page_h)
        for pn in sorted_pages:
            img_bytes, page_w, page_h = _render_page_image(doc_id, pn, TAG)
            if img_bytes:
                page_img_data[pn] = (img_bytes, page_w, page_h)

        if not page_img_data:
            logging.warning(f"{TAG} No page images rendered")
            return

        # ── Step 3: LLM extraction ──
        assembled_text = "\n".join(text_lines).strip()
        if not assembled_text:
            logging.warning(f"{TAG} assembled_text is empty after stripping, skip LLM extraction")
            return
        inputs = ext.get_input_elements()
        chunks_key = next(
            (k for k, v in inputs.items() if isinstance(v.get("value"), list)),
            "text"
        )
        args = {chunks_key: assembled_text}
        # Ensure 'text' key always has content (prompt templates reference {text})
        if chunks_key != "text":
            args["text"] = assembled_text
        for _fn, _fv in ck.items():
            if _fn not in ("text", "image", "positions", "img_id", "id", "doc_id", "mom"):
                args[_fn] = _fv
        msg, sys_prompt = ext._sys_prompt_and_msg([], args)
        msg.insert(0, {"role": "system", "content": sys_prompt})

        # Skip LLM call if user message content is empty
        user_content = next((m["content"] for m in msg if m.get("role") == "user"), "")
        if not user_content or not user_content.strip():
            logging.warning(f"{TAG} user message is empty, skip LLM, proceed to coord only")
            extracted_data = {}
            extracted_json_str = "{}"
        else:
            logging.info(f"{TAG} LLM extraction start, text_len={len(assembled_text)}")
            extracted_json_str = strip_markdown_json_fence(await ext._generate_async(msg))
            logging.info(f"{TAG} LLM output (len={len(extracted_json_str)}):\n{extracted_json_str}")

            try:
                extracted_data = json.loads(extracted_json_str)
            except json.JSONDecodeError as e:
                logging.warning(f"{TAG} JSON parse error: {e}")
                extracted_data = {}
                extracted_json_str = "{}"

            if isinstance(extracted_data, list):
                logging.warning(f"{TAG} extracted_data is list, treat as empty")
                extracted_data = {}
                extracted_json_str = "{}"

        # Save intermediate results
        ck["content_with_weight"] = assembled_text
        ck["text"] = assembled_text
        ck[ext._param.field_name] = extracted_json_str

        # ── Step 3a: Update encounter_date → classify_result_tks ──
        encounter_date = extracted_data.get("encounter_date")
        if encounter_date:
            try:
                classify_data["encounter_dates"] = [encounter_date]
                ck["classify_result_tks"] = json.dumps(classify_data, ensure_ascii=False)
                logging.info(f"{TAG} Updated encounter_dates=[{encounter_date}]")
            except Exception as e:
                logging.warning(f"{TAG} Failed to update encounter_dates: {e}")

        # ── Step 4: Coordinate localization per page ──
        new_positions = []
        for pn in sorted_pages:
            if pn not in page_img_data or pn not in page_text_lines:
                continue
            img_bytes, page_w, page_h = page_img_data[pn]
            lines = page_text_lines[pn]
            if not lines:
                continue

            coord_prompt = _build_coord_prompt(lines)
            ocr_items, api_elapsed, status = _call_qwen30b_coord(
                img_bytes, coord_prompt, TAG, page_num=pn
            )
            if status != "ok" or not ocr_items:
                logging.warning(
                    f"{TAG} page={pn} coord failed: {status}, "
                    f"adding {len(lines)} placeholder(s)"
                )
                for _ in lines:
                    new_positions.append([pn, 0, 0, 0, 0])
                continue

            # Build lookup: text -> bbox
            coord_lookup = {}
            for ocr_item in ocr_items:
                coord_lookup[ocr_item["text"]] = ocr_item["bbox"]

            scale_x = page_w / 1000.0
            scale_y = page_h / 1000.0

            # Match text lines to bboxes
            raw_bboxes = []
            for tl in lines:
                bbox = coord_lookup.get(tl)
                if bbox:
                    raw_bboxes.append(list(bbox))
                else:
                    bbox = _fuzzy_lookup_bbox(tl, coord_lookup)
                    if bbox:
                        raw_bboxes.append(list(bbox))
                    else:
                        raw_bboxes.append(None)

            # Interpolation for missing bboxes
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

            matched = sum(1 for b in raw_bboxes if b is not None)
            for bbox in raw_bboxes:
                if bbox is not None:
                    left = bbox[0] * scale_x
                    right = bbox[2] * scale_x
                    top = bbox[1] * scale_y
                    bottom = bbox[3] * scale_y
                    new_positions.append([pn, left, right, top, bottom])
                else:
                    new_positions.append([pn, 0, 0, 0, 0])

            logging.info(
                f"{TAG} page={pn} — {matched}/{len(lines)} coords, "
                f"api_time={api_elapsed:.1f}s"
            )

        logging.info(f"{TAG} new_positions ({len(new_positions)}):\n{new_positions}")
        ck["positions"] = new_positions
        ck["row_positions"] = []

        # ── Step 5: Save extracted_data ──
        ck[ext._param.field_name] = json.dumps(extracted_data, ensure_ascii=False)
        elapsed = time.time() - t_start
        logging.info(
            f"{TAG} ═══ DONE ═══ {len(new_positions)} positions, "
            f"pages={len(sorted_pages)}, time={elapsed:.1f}s"
        )

    except json.JSONDecodeError as e:
        logging.warning(f"{TAG} JSON parse error: {e}")
    except Exception:
        logging.exception(f"{TAG} Unexpected error")
