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
    "每个item必须是完整的JSON对象，包含text和bbox两个字段，缺一不可。\n"
    "正确示例：\n"
    '{"items": [\n'
    '  {"text": "性别：女", "bbox": [100, 200, 250, 230]},\n'
    '  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]},\n'
    '  {"text": "职业：农民", "bbox": [500, 210, 620, 231]}\n'
    ']}\n'
    "错误示例（禁止省略字段名）：\n"
    '{"items": [\n'
    '  {"text": "性别：女", "bbox": [100, 200, 250, 230]}, "职业：农民", "bbox": [500, 210, 620, 231]}\n'
    ']}\n'
    "请直接输出纯JSON，不要用markdown代码块包裹。"
)

# ── 表格 Prompt（LabReport） ──
TABLE_PROMPT = (
    "你是一个专业的医疗检验报告OCR识别引擎。\n"
    "请识别表格中的每一行检验项目，输出结构化的JSON对象。\n"
    "\n"
    "## 规则\n"
    "1. 每个检验项目作为一条独立条目\n"
    "2. 提取以下字段：\n"
    "   - code: 项目代码（英文缩写，如CRP、RBC、HGB、ALT等）\n"
    "   - name: 项目名称（中文全称，如C反应蛋白、红细胞计数、血红蛋白等）\n"
    "   - result: 结果值\n"
    "   - reference: 参考范围\n"
    "   - unit: 单位\n"
    "3. **name必须是中文名称**，code必须是英文代码，两者都要提取\n"
    "4. **只输出项目名称(name)的bbox坐标**，用于定位该项目在图片中的位置\n"
    "5. 如果某字段为空或不存在，使用空字符串\n"
    "6. bbox坐标归一化到0-1000，格式为[x1,y1,x2,y2]\n"
    "\n"
    "## 严格JSON格式要求\n"
    "每个item必须是完整的JSON对象，包含所有字段，缺一不可。\n"
    "正确示例：\n"
    '{"items": [\n'
    '  {"code": "CRP", "name": "C反应蛋白", "result": "0.29", "reference": "0-10", "unit": "mg/L", "bbox": [100, 200, 400, 230]},\n'
    '  {"code": "WBC", "name": "白细胞计数", "result": "6.5", "reference": "4-10", "unit": "10^9/L", "bbox": [100, 250, 400, 280]}\n'
    ']}\n'
    "请直接输出纯JSON，不要用markdown代码块包裹。"
)

API_ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"


# ── API 调用 ──

def _call_qwen30b(img_bytes: bytes, prompt: str, tag: str) -> tuple:
    """Call qwen3-vl-30b-a3b-instruct via DashScope OpenAI-compatible API.

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
    api_key = os.environ.get("DASHSCOPE_API_KEY", "sk-fad19b13dde544f6a5ca9e9725b133a3")
    b64 = base64.b64encode(img_bytes).decode()
    payload = {
        "model": "qwen3-vl-30b-a3b-instruct",
        "messages": [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
            {"type": "text", "text": prompt},
        ]}],
        "max_tokens": 8192,
        "temperature": 0,
    }
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    logging.info(f"{tag} API call start, img_bytes={len(img_bytes)}")
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
            logging.warning(f"{tag} json_repair also failed: {e2}, content[:200]={content[:200]}")
            return None, elapsed, "JSON parse error"

    raw_items = data.get("items", []) if isinstance(data, dict) else []
    valid_items = []
    for it in raw_items:
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
    positions = ck.get("row_positions", []) or ck.get("positions", [])
    if not positions:
        return None

    page_num = positions[0][0] if isinstance(positions[0], (list, tuple)) and positions[0] else 1
    page_num = page_num - 1  # 0-based

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

        # ── Step 1: Check type == LabReport ──
        classify_raw = ck.get("classify_result_tks", "")
        if not classify_raw:
            return
        classify_data = json.loads(classify_raw) if isinstance(classify_raw, str) else classify_raw
        if classify_data.get("type") != "LabReport":
            return

        # ── Step 2: Check extracted_data items ──
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
            f"items={len(items)}, names={item_names[:5]}, "
            f"img_id={ck.get('img_id', '')[:40]}"
        )

        # ── Step 3: Render page image at 200 DPI ──
        result = _render_page_image(ext, ck, TAG, multi_page_skip=True)
        if not result:
            return
        img_bytes, page_num, page_w, page_h = result

        # ── Step 4: Call qwen3-vl-30b with TABLE_PROMPT ──
        ocr_items, api_elapsed, status = _call_qwen30b(img_bytes, TABLE_PROMPT, TAG)
        if status != "ok" or not ocr_items:
            logging.warning(f"{TAG} OCR failed: {status}")
            return

        logging.info(f"{TAG} Step4: {len(ocr_items)} items from qwen3-vl-30b, api_time={api_elapsed:.1f}s")

        # ── Step 5: Build row_positions from bbox + HTML table ──
        # qwen3-vl-30b bbox is normalized 0-1000 [x1,y1,x2,y2]
        scale_x = page_w / 1000.0
        scale_y = page_h / 1000.0
        row_positions = []

        for ocr_item in ocr_items:
            bbox = ocr_item["bbox"]  # [x1, y1, x2, y2] normalized 0-1000
            left = bbox[0] * scale_x
            right = bbox[2] * scale_x
            top = bbox[1] * scale_y
            bottom = bbox[3] * scale_y
            row_positions.append([page_num + 1, left, right, top, bottom])
            logging.info(
                f"{TAG} '{ocr_item['text']}' -> "
                f"[{page_num + 1}, {left:.1f}, {right:.1f}, {top:.1f}, {bottom:.1f}]"
            )

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

        if row_positions:
            ck["row_positions"] = row_positions
            ck["positions"] = []
            ck["content_with_weight"] = html_table
            ck[ext._param.field_name] = json.dumps(extracted_data, ensure_ascii=False)

            elapsed = time.time() - t_start
            logging.info(
                f"{TAG} ═══ DONE ═══ "
                f"row_positions={len(row_positions)} rows, "
                f"total_time={elapsed:.1f}s"
            )
        else:
            logging.warning(f"{TAG} Could not build any row_positions from qwen3-vl-30b output")

    except json.JSONDecodeError as e:
        logging.warning(f"{TAG} JSON parse error: {e}")
    except Exception:
        logging.exception(f"{TAG} Unexpected error")


# ── 文本处理（非 LabReport） ──

async def process_text(ext, ck: dict):
    """Process non-LabReport chunks using qwen3-vl-30b-instruct.

    Replaces _process_qwen_ocr_vl_text. Uses qwen3-vl-30b-instruct for OCR text
    extraction, then feeds assembled text through LLM prompt for structured extraction.

    Flow:
    1. Check type (skip LabReport)
    2. Render pages at 200 DPI + crop (same logic as _process_qwen_ocr_vl_text)
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

        # ── Step 1: Check type (skip LabReport) ──
        classify_raw = ck.get("classify_result_tks", "")
        if not classify_raw:
            return
        classify_data = json.loads(classify_raw) if isinstance(classify_raw, str) else classify_raw
        rec_type = classify_data.get("type", "")
        if rec_type == "LabReport":
            return

        content = ck.get("content_with_weight", "")
        logging.info(
            f"{TAG} ═══ START ═══ type={rec_type}, "
            f"doc_id={ck.get('doc_id')}, "
            f"img_id={ck.get('img_id', '')[:40]}, "
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
