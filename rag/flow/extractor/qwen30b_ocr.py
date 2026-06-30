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

# ── 表格 Prompt（LabReport） ──
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
        "直接输出JSON数组，每个元素包含text和bbox两个字段。\n"
        "正确示例：\n"
        '[\n'
        '  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},\n'
        '  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}\n'
        ']\n'
        "错误示例（禁止省略字段名）：\n"
        '[\n'
        '  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]}, "白细胞计数", "bbox": [100, 250, 400, 280]}\n'
        ']\n'
        "请直接输出纯JSON数组，不要用markdown代码块包裹。"
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


# ── 图片渲染工具 ──

def _render_page_image(ext, ck, tag, multi_page_skip=True):
    """Render a chunk's page as PNG image at 200 DPI.

    Uses the same logic as Extractor._process_qwen_ocr_vl_table.

    Args:
        ext: Extractor instance.
        ck: Chunk dict.
        tag: Logging tag.
        multi_page_skip: If True, skip multi-page chunks (for table mode).

    Returns:
        tuple: (img_bytes, page_num_0based, page_w, page_h) or None
    """
    import fitz
    from api.db.services.file2document_service import File2DocumentService
    from common import settings

    doc_id = ext._canvas._doc_id
    # row_positions: 1-indexed page_num, positions: 0-indexed page_num
    row_positions = ck.get("row_positions", [])
    positions_list = ck.get("positions", [])
    if row_positions:
        positions = row_positions
        is_row_positions = True
    elif positions_list:
        positions = positions_list
        is_row_positions = False
    else:
        return None

    page_num = positions[0][0] if isinstance(positions[0], (list, tuple)) and positions[0] else 0
    if is_row_positions:
        page_num = page_num - 1  # row_positions 是 1-indexed，转为 0-indexed

    if multi_page_skip and positions:
        page_nums = {int(p[0]) for p in positions if isinstance(p, (list, tuple)) and p}
        if len(page_nums) > 1:
            logging.info(f"{tag} multi-page chunk (pages={page_nums}), skipping")
            return None

    b, n = File2DocumentService.get_storage_address(doc_id=doc_id)
    pdf_bytes = settings.STORAGE_IMPL.get(b, n)
    if not pdf_bytes:
        logging.warning(f"{tag} Failed to get PDF for doc_id={doc_id}")
        return None

    pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    if page_num < 0 or page_num >= len(pdf_doc):
        logging.warning(f"{tag} page_num={page_num} out of range (total={len(pdf_doc)})")
        pdf_doc.close()
        return None

    page = pdf_doc[page_num]
    page_w = page.rect.width
    page_h = page.rect.height
    dpi = 200
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    img_bytes = pix.tobytes("png")
    pdf_doc.close()

    logging.info(
        f"{tag} rendered page={page_num}, page_rect={page_w:.0f}x{page_h:.0f}, "
        f"dpi={dpi}, img_size=({pix.width}x{pix.height})"
    )
    return img_bytes, page_num, page_w, page_h


# ── 表格处理（LabReport） ──

async def process_table(ext, ck: dict):
    """Process LabReport chunks using qwen3-vl-30b-instruct.

    Replaces _process_qwen_ocr_vl_table. Uses qwen3-vl-30b-instruct to directly
    extract item name/code + bbox coordinates, then builds row_positions and HTML table.

    Flow:
    1. Check type == LabReport
    2. Check extracted_data items
    3. Render page image at 200 DPI
    4. Call qwen3-vl-30b with TABLE_PROMPT
    5. Build row_positions from bbox + HTML table
    6. Save results to chunk
    """
    TAG = "[qwen30b-table]"
    try:
        t_start = time.time()

        # ── Step 1: Check extracted_data items ──
        extracted_raw = ck.get(ext._param.field_name, "")
        if not extracted_raw:
            return
        extracted_data = json.loads(extracted_raw) if isinstance(extracted_raw, str) else extracted_raw
        items = extracted_data.get("items", [])
        if not items:
            return

        item_names = [
            it.get("name", "") or it.get("item_code", "")
            for it in items
        ]
        item_names = [n for n in item_names if n]
        if not item_names:
            return

        logging.info(
            f"{TAG} ═══ START ═══ type=LabReport, "
            f"doc_id={ck.get('doc_id')}, "
            f"items={len(items)}, names={item_names}, "
            f"img_id={ck.get('img_id', '')}"
        )

        # ── Step 3: Render page image at 200 DPI ──
        result = _render_page_image(ext, ck, TAG, multi_page_skip=True)
        if not result:
            return
        img_bytes, page_num, page_w, page_h = result

        # ── Step 4: Call qwen3-vl-30b with dynamic TABLE_PROMPT ──
        table_prompt = _build_table_prompt(item_names)
        ocr_items, api_elapsed, status = _call_qwen30b(img_bytes, table_prompt, TAG)
        if status != "ok" or not ocr_items:
            logging.warning(f"{TAG} OCR failed: {status}")
            return

        logging.info(f"{TAG} Step4: {len(ocr_items)} items from qwen3-vl-30b, api_time={api_elapsed:.1f}s")

        # ── Step 5: Match OCR results with known item_names + build row_positions ──
        # qwen3-vl-30b bbox is normalized 0-1000 [x1,y1,x2,y2]
        scale_x = page_w / 1000.0
        scale_y = page_h / 1000.0

        # Build lookup: text -> bbox from OCR results
        ocr_lookup = {}
        for ocr_item in ocr_items:
            text = ocr_item.get("text", "")
            bbox = ocr_item.get("bbox")
            if text and bbox and len(bbox) == 4:
                ocr_lookup[text] = bbox

        row_positions = []
        matched = 0
        for name in item_names:
            bbox = ocr_lookup.get(name)
            if bbox:
                left = bbox[0] * scale_x
                right = bbox[2] * scale_x
                top = bbox[1] * scale_y
                bottom = bbox[3] * scale_y
                row_positions.append([page_num + 1, left, right, top, bottom])
                matched += 1
                logging.info(
                    f"{TAG} '{name}' -> "
                    f"[{page_num + 1}, {left:.1f}, {right:.1f}, {top:.1f}, {bottom:.1f}]"
                )
            else:
                logging.info(f"{TAG} '{name}' not found in OCR results")
                row_positions.append([page_num + 1, 0, 0, 0, 0])

        logging.info(f"{TAG} Step5: matched {matched}/{len(item_names)} items")

        # Build HTML table from upstream extracted items
        html_rows = []
        for it in items:
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

        if matched > 0:
            ck["row_positions"] = row_positions
            ck["positions"] = []
            ck["content_with_weight"] = html_table
            ck[ext._param.field_name] = json.dumps(extracted_data, ensure_ascii=False)

            elapsed = time.time() - t_start
            logging.info(
                f"{TAG} ═══ DONE ═══ "
                f"matched={matched}/{len(item_names)}, "
                f"total_time={elapsed:.1f}s"
            )
        else:
            logging.warning(f"{TAG} No items matched from qwen3-vl-30b output")

    except json.JSONDecodeError as e:
        logging.warning(f"{TAG} JSON parse error: {e}")
    except Exception:
        logging.exception(f"{TAG} Unexpected error")


# ── 文本处理（非 LabReport） ──

async def process_text(ext, ck: dict):
    """Process non-LabReport chunks using qwen3-vl-30b-instruct.

    Called from extractor.py when type != LabReport.
    Uses qwen3-vl-30b-instruct for OCR text extraction, then feeds assembled
    text through LLM prompt for structured extraction.

    Flow:
    1. Get record type (for crop logic)
    2. Render pages at 200 DPI + crop
    3. Call qwen3-vl-30b with TEXT_PROMPT per page
    4. Assemble text from JSON items[].text → ocr_assembled_text
    5. LLM extraction via _sys_prompt_and_msg + _generate_async
    6. Parse extracted JSON + update encounter_date
    7. Convert bbox to PDF coordinates
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

        # ── Step 3: Call qwen3-vl-30b with TEXT_PROMPT per page ──
        all_page_items = []   # [(pn, items, cox, coy, cw, ch), ...]
        all_page_texts = []

        for pn, img_bytes, page_w, page_h, cox, coy, cw, ch in page_img_data:
            items, api_elapsed, status = _call_qwen30b(img_bytes, TEXT_PROMPT, TAG)
            if status != "ok" or not items:
                logging.warning(f"{TAG} Step3: page={pn} OCR failed: {status}")
                continue

            page_text = "\n".join(it.get("text", "") for it in items if it.get("text"))
            all_page_items.append((pn, items, cox, coy, cw, ch))
            all_page_texts.append(page_text)
            logging.info(
                f"{TAG} Step3: page={pn} — {len(items)} items, "
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

        # ── Step 7: Convert bbox (0-1000) → PDF coordinates ──
        new_positions = []
        for pn, page_items, cox, coy, cw, ch in all_page_items:
            scale_x = cw / 1000.0
            scale_y = ch / 1000.0
            for it in page_items:
                bbox = it.get("bbox")
                if not bbox or len(bbox) != 4:
                    continue
                left = bbox[0] * scale_x + cox
                right = bbox[2] * scale_x + cox
                top = bbox[1] * scale_y + coy
                bottom = bbox[3] * scale_y + coy
                new_positions.append([pn, left, right, top, bottom])

        ck["positions"] = new_positions
        ck["row_positions"] = []
        logging.info(f"{TAG} Step7: {len(new_positions)} positions stored, row_positions=[]")

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
