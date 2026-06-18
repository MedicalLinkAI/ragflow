#
#  Copyright 2025 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import base64
import json
import logging
import math
import os
import random
import re
from copy import deepcopy
from functools import partial
from io import BytesIO

import xxhash


def strip_markdown_json_fence(text: str) -> str:
    """Strip markdown code fences from LLM JSON output.

    LLMs sometimes wrap JSON in ```json ... ``` despite being told not to.
    This is a deterministic safeguard — prompt is probabilistic.
    """
    if not isinstance(text, str):
        return text
    stripped = text.strip()
    if stripped.startswith("```"):
        # Remove opening fence (```json, ```JSON, or just ```)
        stripped = re.sub(r"^```(?:json|JSON)?\s*\n?", "", stripped)
        # Remove closing fence
        stripped = re.sub(r"\n?```\s*$", "", stripped)
        return stripped.strip()
    return text

from agent.component.llm import LLMParam, LLM
from rag.flow.base import ProcessBase, ProcessParamBase
from rag.prompts.generator import run_toc_from_text
from rag.utils.base64_image import id2image
from common import settings


class ExtractorParam(ProcessParamBase, LLMParam):
    def __init__(self):
        super().__init__()
        self.field_name = ""

    def check(self):
        super().check()
        self.check_empty(self.field_name, "Result Destination")


class Extractor(ProcessBase, LLM):
    component_name = "Extractor"

    async def _build_TOC(self, docs):
        self.callback(0.2,message="Start to generate table of content ...")
        docs = sorted(docs, key=lambda d:(
            d.get("page_num_int", 0)[0] if isinstance(d.get("page_num_int", 0), list) else d.get("page_num_int", 0),
            d.get("top_int", 0)[0] if isinstance(d.get("top_int", 0), list) else d.get("top_int", 0)
        ))
        toc = await run_toc_from_text([d["text"] for d in docs], self.chat_mdl)
        logging.info("------------ T O C -------------\n"+json.dumps(toc, ensure_ascii=False, indent='  '))
        ii = 0
        while ii < len(toc):
            try:
                idx = int(toc[ii]["chunk_id"])
                del toc[ii]["chunk_id"]
                toc[ii]["ids"] = [docs[idx]["id"]]
                if ii == len(toc) -1:
                    break
                for jj in range(idx+1, int(toc[ii+1]["chunk_id"])+1):
                    toc[ii]["ids"].append(docs[jj]["id"])
            except Exception as e:
                logging.exception(e)
            ii += 1

        if toc:
            d = deepcopy(docs[-1])
            d["doc_id"] = self._canvas._doc_id
            d["content_with_weight"] = json.dumps(toc, ensure_ascii=False)
            d["toc_kwd"] = "toc"
            d["available_int"] = 0
            d["page_num_int"] = [100000000]
            d["id"] = xxhash.xxh64((d["content_with_weight"] + str(d["doc_id"])).encode("utf-8", "surrogatepass")).hexdigest()
            return d
        return None

    async def _invoke(self, **kwargs):
        self.set_output("output_format", "chunks")
        self.callback(random.randint(1, 5) / 100.0, "Start to generate.")
        inputs = self.get_input_elements()
        chunks = []
        chunks_key = ""
        args = {}
        for k, v in inputs.items():
            args[k] = v["value"]
            if isinstance(args[k], list):
                chunks = deepcopy(args[k])
                chunks_key = k

        if chunks:
            if self._param.field_name == "toc":
                for ck in chunks:
                    ck["doc_id"] = self._canvas._doc_id
                    ck["id"] = xxhash.xxh64((ck["text"] + str(ck["doc_id"])).encode("utf-8")).hexdigest()
                toc =await self._build_TOC(chunks)
                chunks.append(toc)
                self.set_output("chunks", chunks)
                return

            prog = 0
            for i, ck in enumerate(chunks):
                args[chunks_key] = ck["text"]
                # Pass through upstream business fields so downstream prompts can reference them via {field_name}
                for _fn, _fv in ck.items():
                    if _fn not in ("text", "image", "positions", "img_id", "id", "doc_id", "mom"):
                        args[_fn] = _fv
                msg, sys_prompt = self._sys_prompt_and_msg([], args)
                msg.insert(0, {"role": "system", "content": sys_prompt})
                ck[self._param.field_name] = strip_markdown_json_fence(await self._generate_async(msg))

                # For LabReport chunks with exactly 1 item, use advanced_recognition
                # to locate the item name in the image and store coordinates in item.location
                # 通过环境变量 ENABLE_OCR_VL_TABLE 控制，默认为 true
                if os.environ.get("ENABLE_OCR_VL_TABLE", "true").lower() == "true":
                    await self._process_qwen_ocr_vl_table(ck)

                # For OutpatientRecord chunks with table content:
                # OCR → markdown → LLM JSON → coordinate extraction
                # 通过环境变量 ENABLE_OCR_VL_TEXT 控制，默认为 true
                if os.environ.get("ENABLE_OCR_VL_TEXT", "false").lower() == "true":
                    await self._process_qwen_ocr_vl_text(ck)

                prog += 1./len(chunks)
                if i % (len(chunks)//100+1) == 1:
                    self.callback(prog, f"{i+1} / {len(chunks)}")
            self.set_output("chunks", chunks)
        else:
            msg, sys_prompt = self._sys_prompt_and_msg([], args)
            msg.insert(0, {"role": "system", "content": sys_prompt})
            self.set_output("chunks", [{self._param.field_name: strip_markdown_json_fence(await self._generate_async(msg))}])

    async def _process_qwen_ocr_vl_table(self, ck: dict):
        """For LabReport chunks with exactly 1 extracted item, use DashScope
        advanced_recognition to find the item name's coordinates in the image
        and store them in row_positions."""
        TAG = "[Extractor._qwen-vl-ocr-table]"
        try:
            import time
            t_start = time.time()

            # ── Step 1: Check type == LabReport ──
            classify_raw = ck.get("classify_result_tks", "")
            if not classify_raw:
                return
            classify_data = json.loads(classify_raw) if isinstance(classify_raw, str) else classify_raw
            if classify_data.get("type") != "LabReport":
                return

            # ── Step 2: Check extracted_data has exactly 1 item ──
            extracted_raw = ck.get(self._param.field_name, "")
            if not extracted_raw:
                return
            extracted_data = json.loads(extracted_raw) if isinstance(extracted_raw, str) else extracted_raw
            items = extracted_data.get("items", [])
            if len(items) != 1:
                return

            item = items[0]
            item_name = item.get("name", "") or item.get("item_code", "")
            if not item_name:
                return

            logging.info(
                f"{TAG} ═══ START ═══ type=LabReport, "
                f"doc_id={ck.get('doc_id')}, "
                f"item_name='{item_name}', "
                f"img_id={ck.get('img_id', '')[:40]}"
            )

            # ── Step 3: Render page image at 200 DPI ──
            import fitz
            from api.db.services.file2document_service import File2DocumentService

            doc_id = self._canvas._doc_id
            positions = ck.get("positions", [])
            page_num = positions[0][0] if positions and isinstance(positions[0], (list, tuple)) and positions[0] else 1

            b, n = File2DocumentService.get_storage_address(doc_id=doc_id)
            pdf_bytes = settings.STORAGE_IMPL.get(b, n)
            if not pdf_bytes:
                logging.warning(f"{TAG} Step3: Failed to get PDF for doc_id={doc_id}")
                return

            pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            if page_num < 0 or page_num >= len(pdf_doc):
                logging.warning(f"{TAG} Step3: page_num={page_num} out of range (total={len(pdf_doc)})")
                pdf_doc.close()
                return

            page = pdf_doc[page_num]
            page_w = page.rect.width
            page_h = page.rect.height
            page_rect = f"{page_w:.0f}x{page_h:.0f}"
            dpi = 200
            zoom = dpi / 72.0
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            img_bytes = pix.tobytes("png")
            pdf_doc.close()
            logging.info(f"{TAG} Step3: page_num={page_num}, page_rect={page_rect}, dpi={dpi}, img_size=({pix.width}x{pix.height})")

            # ── Step 4: Convert to base64 data URL ──
            b64_str = base64.b64encode(img_bytes).decode("utf-8")
            data_url = f"data:image/png;base64,{b64_str}"

            # ── Step 5: DashScope advanced_recognition ──
            import dashscope
            dashscope.base_http_api_url = "https://dashscope.aliyuncs.com/api/v1"
            api_key = os.environ.get("DASHSCOPE_API_KEY", "sk-fad19b13dde544f6a5ca9e9725b133a3")
            if not api_key:
                logging.warning(f"{TAG} DASHSCOPE_API_KEY not set, skipping")
                return

            img_content = {
                "image": data_url,
                "min_pixels": 32 * 32 * 64,
                "max_pixels": 32 * 32 * 8192,
                "enable_rotate": False,
            }
            messages = [{"role": "user", "content": [img_content]}]
            logging.info(
                f"{TAG} Step5: ═══ OCR INPUT ═══\n"
                f"{TAG} Step5:   model=qwen-vl-ocr-2025-11-20\n"
                f"{TAG} Step5:   ocr_options={{task: advanced_recognition}}\n"
                f"{TAG} Step5:   image_size=({pix.width}x{pix.height}), png_bytes={len(img_bytes)}\n"
                f"{TAG} Step5:   item_name='{item_name}'"
            )
            t_ocr = time.time()
            resp = dashscope.MultiModalConversation.call(
                api_key=api_key,
                model="qwen-vl-ocr-2025-11-20",
                messages=messages,
                ocr_options={"task": "advanced_recognition"},
            )
            ocr_elapsed = time.time() - t_ocr
            logging.info(f"{TAG} Step5: ═══ OCR OUTPUT ═══ status={resp.status_code}, elapsed={ocr_elapsed:.1f}s")
            if resp.status_code != 200:
                logging.warning(f"{TAG} Step5: failed: {resp.code} - {resp.message}")
                return

            content = resp["output"]["choices"][0]["message"]["content"]
            raw_text = content[0].get("text", "") if content else ""
            if not isinstance(raw_text, str):
                logging.warning(f"{TAG} Step5: invalid response type={type(raw_text)}")
                return

            # Strip markdown fences
            raw_text = raw_text.strip()
            if raw_text.startswith("```"):
                raw_text = re.sub(r"^```(?:json|JSON)?\s*\n?", "", raw_text)
                raw_text = re.sub(r"\n?```\s*$", "", raw_text)
                raw_text = raw_text.strip()

            # ── Step 6: Parse OCR lines ──
            ocr_lines = json.loads(raw_text)
            if not isinstance(ocr_lines, list):
                logging.warning(f"{TAG} Step6: result is not a list, type={type(ocr_lines)}")
                return

            logging.info(f"{TAG} Step6: {len(ocr_lines)} OCR lines")
            for _li, _line in enumerate(ocr_lines):
                _text = _line.get("text", "")
                _coord = _line.get("rotate_rect") or _line.get("bbox")
                logging.info(f"{TAG} Step6:   [{_li:02d}] text='{_text[:60]}' coord={_coord}")

            # ── Step 7: Find matching line for item_name ──
            location = self._find_name_location(item_name, ocr_lines)
            if location:
                logging.info(f"{TAG} Step7: Found '{item_name}' location={location}")

                # ── Step 8: Convert location → bbox → PDF points → row_positions ──
                scale_x = page_w / 1000.0
                scale_y = page_h / 1000.0
                if len(location) == 5:
                    location = Extractor._rotate_rect_to_4corners(location)
                if len(location) >= 8:
                    xs = [location[0], location[2], location[4], location[6]]
                    ys = [location[1], location[3], location[5], location[7]]
                    left = min(xs) * scale_x
                    right = max(xs) * scale_x
                    top = min(ys) * scale_y
                    bottom = max(ys) * scale_y
                    ck["row_positions"] = [[page_num+1, left, right, top, bottom]]
                    ck["positions"] = []
                    logging.info(f"{TAG} Step8: row_positions={ck['row_positions']}, positions=[]")

                # ── Step 9: Build HTML table from items → content_with_weight ──
                html_rows = []
                for it in items:
                    cells = [it.get("name", ""),it.get("item_code", ""), it.get("value", ""), it.get("unit", ""),
                             it.get("reference_range", ""), it.get("abnormal", "")]
                    html_rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
                html_table = "<table>" + "".join(html_rows) + "</table>"
                ck["content_with_weight"] = html_table
                logging.info(f"{TAG} Step9: content_with_weight={html_table[:100]}...")

                # Update extracted_data
                ck[self._param.field_name] = json.dumps(extracted_data, ensure_ascii=False)

                elapsed = time.time() - t_start
                logging.info(f"{TAG} ═══ DONE ═══ total_time={elapsed:.1f}s")
            else:
                all_ocr_texts = [line.get("text", "")[:80] for line in ocr_lines if line.get("text")]
                logging.warning(
                    f"{TAG} Step7: Could not locate '{item_name}' in OCR results\n"
                    f"{TAG} Step7: OCR texts ({len(all_ocr_texts)}):\n" +
                    "\n".join(f"{TAG} Step7:   [{i}] {t}" for i, t in enumerate(all_ocr_texts[:15]))
                )

        except json.JSONDecodeError as e:
            logging.warning(f"{TAG} JSON parse error: {e}")
        except Exception:
            logging.exception(f"{TAG} Unexpected error")

    async def _process_qwen_ocr_vl_text(self, ck: dict):
        """For OutpatientRecord chunks:
        Step 1: qwen-vl-ocr (advanced_recognition) → text + coordinates (一次调用)
        Step 2: Assemble OCR text → LLM → extracted_data JSON
        Step 3: Match extracted JSON values to OCR coordinates
        """
        TAG = "[Extractor._qwen-vl-ocr-text]"
        try:
            import time
            t_start = time.time()

            # ── Step 1: Check type == OutpatientRecord ──
            classify_raw = ck.get("classify_result_tks", "")
            if not classify_raw:
                return
            classify_data = json.loads(classify_raw) if isinstance(classify_raw, str) else classify_raw
            rec_type = classify_data.get("type", "")
            # 如果是检验报告就不处理
            if rec_type == "LabReport":
                return

            content = ck.get("content_with_weight", "")
            logging.info(
                f"{TAG} ═══ START ═══ type={rec_type}, "
                f"doc_id={ck.get('doc_id')}, "
                f"img_id={ck.get('img_id', '')[:40]}, "
                f"content_len={len(content)}"
            )

            # ── Step 2: Render page image at 200 DPI ──
            import fitz
            from api.db.services.file2document_service import File2DocumentService

            doc_id = self._canvas._doc_id
            positions = ck.get("positions", [])
            page_num = int(positions[0][0]) if positions and isinstance(positions[0], (list, tuple)) and positions[0] else 0
            logging.info(f"{TAG} Step2: page_num={page_num}, doc_id={doc_id}")

            b, n = File2DocumentService.get_storage_address(doc_id=doc_id)
            pdf_bytes = settings.STORAGE_IMPL.get(b, n)
            if not pdf_bytes:
                logging.warning(f"{TAG} Step2: Failed to get PDF for doc_id={doc_id}")
                return

            pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            if page_num < 0 or page_num >= len(pdf_doc):
                logging.warning(f"{TAG} Step2: page_num={page_num} out of range (total={len(pdf_doc)})")
                pdf_doc.close()
                return

            page = pdf_doc[page_num]
            page_w = page.rect.width  # PDF 宽度 (points)
            page_h = page.rect.height  # PDF 高度 (points)
            page_rect = f"{page_w:.0f}x{page_h:.0f}"
            dpi = 200
            zoom = dpi / 72.0
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            img_bytes = pix.tobytes("png")
            pdf_doc.close()
            logging.info(f"{TAG} Step2: page_rect={page_rect}, dpi={dpi}, img_size=({pix.width}x{pix.height})")

            b64_str = base64.b64encode(img_bytes).decode("utf-8")
            data_url = f"data:image/png;base64,{b64_str}"

            # ── Step 3: DashScope advanced_recognition → text + coordinates (一次调用) ──
            import dashscope
            dashscope.base_http_api_url = "https://dashscope.aliyuncs.com/api/v1"
            api_key = os.environ.get("DASHSCOPE_API_KEY", "sk-fad19b13dde544f6a5ca9e9725b133a3")
            if not api_key:
                logging.warning(f"{TAG} DASHSCOPE_API_KEY not set, skipping")
                return

            img_content = {
                "image": data_url,
                "min_pixels": 32 * 32 * 64,
                "max_pixels": 30720000,
                "enable_rotate": False,
            }
            messages = [{"role": "user", "content": [img_content]}]
            logging.info(
                f"{TAG} Step3: ═══ OCR INPUT ═══\n"
                f"{TAG} Step3:   model=qwen-vl-ocr-2025-11-20\n"
                f"{TAG} Step3:   ocr_options={{task: advanced_recognition}}\n"
                f"{TAG} Step3:   image_size=({pix.width}x{pix.height}), png_bytes={len(img_bytes)}\n"
                f"{TAG} Step3:   min_pixels={img_content['min_pixels']}, max_pixels={img_content['max_pixels']}\n"
                f"{TAG} Step3:   enable_rotate={img_content['enable_rotate']}"
            )
            t_ocr = time.time()
            resp = dashscope.MultiModalConversation.call(
                api_key=api_key,
                model="qwen-vl-ocr-2025-11-20",
                messages=messages,
                ocr_options={"task": "advanced_recognition"},
            )
            ocr_elapsed = time.time() - t_ocr
            logging.info(f"{TAG} Step3: ═══ OCR OUTPUT ═══ status={resp.status_code}, elapsed={ocr_elapsed:.1f}s")
            if resp.status_code != 200:
                logging.warning(f"{TAG} Step3: failed: {resp.code} - {resp.message}")
                return

            ocr_content = resp["output"]["choices"][0]["message"]["content"]
            raw_ocr_text = ocr_content[0].get("text", "") if ocr_content else ""
            if not isinstance(raw_ocr_text, str):
                logging.warning(f"{TAG} Step3: invalid response type={type(raw_ocr_text)}")
                return

            raw_ocr_text_stripped = raw_ocr_text.strip()
            if raw_ocr_text_stripped.startswith("```"):
                raw_ocr_text_stripped = re.sub(r"^```(?:json|JSON)?\s*\n?", "", raw_ocr_text_stripped)
                raw_ocr_text_stripped = re.sub(r"\n?```\s*$", "", raw_ocr_text_stripped)
                raw_ocr_text_stripped = raw_ocr_text_stripped.strip()
            logging.info(f"{TAG} Step3: raw_text_len={len(raw_ocr_text)}, cleaned_len={len(raw_ocr_text_stripped)}")
            logging.info(f"{TAG} Step3: raw_text_preview:\n{raw_ocr_text_stripped[:1000]}")
            raw_ocr_text = raw_ocr_text_stripped

            ocr_lines = json.loads(raw_ocr_text)
            if not isinstance(ocr_lines, list):
                logging.warning(f"{TAG} Step3: result is not a list, type={type(ocr_lines)}")
                return

            logging.info(f"{TAG} Step3: OK — {len(ocr_lines)} OCR lines")
            for _li, _line in enumerate(ocr_lines):
                _text = _line.get("text", "")
                _coord = _line.get("rotate_rect") or _line.get("bbox")
                logging.info(f"{TAG} Step3:   [{_li:02d}] text='{_text[:60]}' coord={_coord}")

            # ── Step 4: Assemble OCR text lines → update content_with_weight ──
            ocr_assembled_text = "\n".join(
                line.get("text", "") for line in ocr_lines if line.get("text")
            )
            old_content_len = len(ck.get("content_with_weight", ""))
            ck["content_with_weight"] = ocr_assembled_text
            ck["text"] = ocr_assembled_text
            logging.info(
                f"{TAG} Step4: Updated content ({old_content_len}→{len(ocr_assembled_text)} chars)\n"
                f"{TAG} Step4: preview:\n{ocr_assembled_text[:500]}"
            )

            # ── Step 5: LLM extraction with assembled OCR text ──
            inputs = self.get_input_elements()
            chunks_key = next((k for k, v in inputs.items() if isinstance(v.get("value"), list)), "text")
            args = {chunks_key: ocr_assembled_text}
            for _fn, _fv in ck.items():
                if _fn not in ("text", "image", "positions", "img_id", "id", "doc_id", "mom"):
                    args[_fn] = _fv
            msg, sys_prompt = self._sys_prompt_and_msg([], args)
            msg.insert(0, {"role": "system", "content": sys_prompt})
            # 打印 LLM 入参
            logging.info(f"{TAG} Step5: ═══ LLM INPUT ═══")
            logging.info(f"{TAG} Step5:   sys_prompt (len={len(sys_prompt)}):\n{sys_prompt[:500]}")
            for _mi, _m in enumerate(msg):
                _role = _m.get("role", "")
                _content = _m.get("content", "")
                if isinstance(_content, str):
                    logging.info(f"{TAG} Step5:   msg[{_mi}] role={_role} content_len={len(_content)}:\n{_content[:800]}")
                else:
                    logging.info(f"{TAG} Step5:   msg[{_mi}] role={_role} content={type(_content)}")
            logging.info(f"{TAG} Step5:   total msg_count={len(msg)}")
            t_llm = time.time()
            extracted_json_str = strip_markdown_json_fence(await self._generate_async(msg))
            llm_elapsed = time.time() - t_llm
            # 打印 LLM 出参
            logging.info(
                f"{TAG} Step5: ═══ LLM OUTPUT ═══ elapsed={llm_elapsed:.1f}s, "
                f"result_len={len(extracted_json_str)}"
            )
            logging.info(f"{TAG} Step5: raw_output:\n{extracted_json_str[:1000]}")
            ck[self._param.field_name] = extracted_json_str

            # ── Step 6: Parse extracted JSON ──
            try:
                extracted_data = json.loads(extracted_json_str)
            except json.JSONDecodeError as e:
                logging.warning(f"{TAG} JSON parse error: {e}, raw={extracted_json_str[:200]}")
                return

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

            # ── Step 7: 将 ocr_lines 坐标转为 bbox → PDF点坐标 → 存入 positions ──
            # OCR 坐标是 1000-unit 归一化，需转换为 PDF 点坐标 bbox
            # 每个 position 格式: [page_num, left, right, top, bottom] (5元素)
            new_positions = []
            scale_x = page_w / 1000.0  # 1000-unit → PDF points X
            scale_y = page_h / 1000.0  # 1000-unit → PDF points Y
            for _li, _line in enumerate(ocr_lines):
                _text = _line.get("text", "")
                _coord = _line.get("rotate_rect") or _line.get("bbox")
                if not _text or not _coord:
                    continue
                # rotate_rect (5元素) → 4角坐标 (8元素)
                if len(_coord) == 5:
                    _coord = Extractor._rotate_rect_to_4corners(_coord)
                if len(_coord) >= 8:
                    # 4角坐标 → bbox (left, right, top, bottom)
                    xs = [_coord[0], _coord[2], _coord[4], _coord[6]]
                    ys = [_coord[1], _coord[3], _coord[5], _coord[7]]
                    left = min(xs) * scale_x
                    right = max(xs) * scale_x
                    top = min(ys) * scale_y
                    bottom = max(ys) * scale_y
                    pos_entry = [page_num, left, right, top, bottom]
                    new_positions.append(pos_entry)

            # 更新 positions（ES: position_int）和清空 row_position_int
            ck["positions"] = new_positions
            ck["row_positions"] = []
            logging.info(f"{TAG} Step7: {len(new_positions)} positions stored, row_position_int=[]")
            for _pi, _pos in enumerate(new_positions):
                logging.info(f"{TAG} Step7:   [{_pi}] position={_pos}")

            # ── Step 8: Save extracted_data back ──
            ck[self._param.field_name] = json.dumps(extracted_data, ensure_ascii=False)
            elapsed = time.time() - t_start
            logging.info(
                f"{TAG} Step8:  ═══ DONE ═══ "
                f"{len(new_positions)} positions stored, "
                f"total_time={elapsed:.1f}s (OCR+LLM 2 calls)"
            )

        except json.JSONDecodeError as e:
            logging.warning(f"{TAG} JSON parse error: {e}")
        except Exception:
            logging.exception(f"{TAG} Unexpected error")

    @staticmethod
    def _rotate_rect_to_4corners(rr: list) -> list:
        """Convert rotate_rect [cx, cy, w, h, angle_deg] to 4-corner coords.

        Output: [x1,y1, x2,y2, x3,y3, x4,y4]
        Order: top-left, top-right, bottom-right, bottom-left (CCW from TL).
        """
        if not rr or len(rr) != 5:
            return rr or []
        cx, cy, w, h, angle = rr
        rad = math.radians(angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        hw, hh = w / 2.0, h / 2.0
        # 4 corners relative to center (before rotation)
        corners = [(-hw, -hh), (hw, -hh), (hw, hh), (-hw, hh)]
        result = []
        for dx, dy in corners:
            rx = cx + dx * cos_a - dy * sin_a
            ry = cy + dx * sin_a + dy * cos_a
            result.extend([round(rx, 1), round(ry, 1)])
        return result

    @staticmethod
    def _find_name_location(item_name: str, ocr_lines: list) -> list | None:
        """Find the OCR line whose text best matches item_name and return its coordinates.

        Always returns 4-corner format [x1,y1, x2,y2, x3,y3, x4,y4] (8 elements) or None.
        """
        if not ocr_lines or not item_name:
            return None

        # Normalize: lowercase, strip whitespace/punctuation for fuzzy matching
        def _norm(s: str) -> str:
            return re.sub(r"\s+", "", s).lower()

        name_norm = _norm(item_name)
        best_location = None
        best_score = 0.0

        for line in ocr_lines:
            text = _norm(line.get("text", ""))
            if not text:
                continue

            # Exact substring match
            if name_norm in text or text in name_norm:
                score = min(len(text), len(name_norm)) / max(len(text), len(name_norm), 1)
            else:
                # Character overlap ratio (for OCR errors)
                overlap = len(set(name_norm) & set(text))
                min_len = min(len(name_norm), len(text), 1)
                max_len = max(len(name_norm), len(text), 1)
                len_diff_pct = abs(len(name_norm) - len(text)) / max_len

                # Relaxed matching for long text (allow larger length difference)
                if len(name_norm) > 10:
                    # For long text: 60% overlap and length diff < 30%
                    if overlap / min_len >= 0.6 and len_diff_pct < 0.3:
                        score = overlap / max_len * 0.7
                    else:
                        continue
                else:
                    # For short text: stricter matching
                    if overlap / min_len >= 0.7 and abs(len(name_norm) - len(text)) <= 3:
                        score = overlap / max_len * 0.8
                    else:
                        continue

            if score > best_score:
                best_score = score
                # Prefer rotate_rect, fallback to bbox
                best_location = line.get("rotate_rect") or line.get("bbox")

        # Fallback: prefix matching for very long text (first 10+ chars)
        if best_score <= 0.3 and len(name_norm) >= 10:
            prefix = name_norm[:10]
            for line in ocr_lines:
                text = _norm(line.get("text", ""))
                if text and prefix in text:
                    best_location = line.get("rotate_rect") or line.get("bbox")
                    best_score = 0.31  # Just above threshold
                    break

        if best_score <= 0.3 or not best_location:
            return None

        # Convert rotate_rect (5-elem) to 4-corner (8-elem) for uniform output
        if len(best_location) == 5:
            best_location = Extractor._rotate_rect_to_4corners(best_location)

        return best_location
