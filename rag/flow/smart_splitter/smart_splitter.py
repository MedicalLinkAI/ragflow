#
#  Custom Operator: SmartSplitter
#  NOT a RAGflow official component — custom extension for MedLinkAI Pipeline v3.0
#
#  Purpose: LLM-based semantic splitting + classification in one step.
#  Replaces Splitter + Classify (Extractor) — zero mixed-type chunks.
#
#  Auto-discovered by rag/flow/__init__.py via pkgutil.walk_packages
#
import asyncio
import json
import logging
import random
import re
from copy import deepcopy
from functools import partial
from typing import Any

from common.misc_utils import get_uuid
from rag.utils.base64_image import id2image, image2id
from rag.nlp import concat_img
from deepdoc.parser.pdf_parser import RAGFlowPdfParser
from rag.flow.base import ProcessBase, ProcessParamBase
from rag.flow.splitter.schema import SplitterFromUpstream
from agent.component.llm import LLMParam, LLM
from common import settings


def strip_markdown_json_fence(text: str) -> str:
    """Strip markdown code fences (```json ... ```) from LLM output."""
    if not isinstance(text, str):
        return text
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json|JSON)?\s*\n?", "", stripped)
        stripped = re.sub(r"\n?```\s*$", "", stripped)
        return stripped.strip()
    return text


def _add_row_markers(html_text: str, bbox_idx: int) -> str:
    """在表格 HTML 的每个 <tr> 前插入行号标记 [BBOX-{idx}-R{n}]，供 LLM 引用。
    
    仅用于构建发给 LLM 的 user_message，不影响最终 chunk content。
    """
    counter = [0]
    def replacer(match):
        rn = counter[0]
        counter[0] += 1
        return f"[BBOX-{bbox_idx}-R{rn}]{match.group(0)}"
    return re.sub(r"<tr>", replacer, html_text, flags=re.IGNORECASE)


def _trim_table_rows(html_text: str, row_start: int, row_end: int) -> str:
    """从表格 HTML 中提取 [row_start, row_end] 范围的 <tr> 行，保留 <table> 包裹。
    
    同时去掉行号标记 [BBOX-N-Rn]（它们只是给 LLM 看的，不应出现在最终 content 中）。
    """
    # 去掉行号标记
    clean = re.sub(r"\[BBOX-\d+-R\d+\]", "", html_text)
    
    rows = re.findall(r"<tr>[\s\S]*?</tr>", clean, re.IGNORECASE)
    if not rows:
        return html_text  # 无 <tr>，原样返回
    
    # 裁剪行范围
    selected = rows[row_start:row_end + 1]
    if not selected:
        return html_text  # 范围无效，原样返回
    
    # 保留 <caption>（如果有）
    caption = ""
    cap_match = re.search(r"<caption>[\s\S]*?</caption>", clean, re.IGNORECASE)
    if cap_match:
        caption = cap_match.group(0) + "\n"
    
    return f"<table>\n{caption}" + "\n".join(selected) + "\n</table>"


# ─── Default prompt ──────────────────────────────────────────────
DEFAULT_SMART_SPLIT_PROMPT = ""  # Will be set via DSL sys_prompt

# ─── bbox inference helpers ──────────────────────────────────────
def _infer_bbox_end(b_start: int, seg_idx: int, segments: list, total: int) -> int:
    """Dynamically infer bbox_end from the next segment's bbox_start."""
    if seg_idx + 1 < len(segments):
        next_seg = segments[seg_idx + 1]
        ns = next_seg.get("bbox_start")
        if isinstance(ns, str):
            try:
                ns = int(ns)
            except (ValueError, TypeError):
                ns = -1
        if isinstance(ns, int) and ns > b_start:
            return min(ns - 1, total - 1)
    return total - 1


def _infer_bbox_start(b_end: int, seg_idx: int, segments: list) -> int:
    """Dynamically infer bbox_start from the previous segment's bbox_end."""
    if seg_idx > 0:
        prev_seg = segments[seg_idx - 1]
        pe = prev_seg.get("bbox_end")
        if isinstance(pe, str):
            try:
                pe = int(pe)
            except (ValueError, TypeError):
                pe = -1
        if isinstance(pe, int) and 0 <= pe < b_end:
            return pe + 1
    return 0


class SmartSplitterParam(ProcessParamBase, LLMParam):
    """SmartSplitter parameters — combines Splitter + LLM (Classify)."""

    def __init__(self):
        super().__init__()
        self.classify_field = "classify_result_tks"

    def check(self):
        super().check()
        self.check_empty(self.classify_field, "Classify field name")


class SmartSplitter(ProcessBase, LLM):
    """
    LLM-based semantic splitter + classifier for medical documents.

    NOT a RAGflow official component — custom extension for MedLinkAI project.

    Replaces: Splitter (token-counting) + Extractor:Classify (LLM labeling)
    Into:     One operator that does both in a single LLM call.

    Input:  Parser output (json bboxes with text + position_tag + img_id)
    Output: Semantically-split chunks, each with classify_result_tks attached.
            Format is identical to Splitter + Classify combined output.
    """
    component_name = "SmartSplitter"

    async def _invoke(self, **kwargs):
        try:
            from_upstream = SplitterFromUpstream.model_validate(kwargs)
        except Exception as e:
            self.set_output("_ERROR", f"Input error: {str(e)}")
            return

        self.set_output("output_format", "chunks")
        self.callback(random.randint(1, 5) / 100.0, "Start SmartSplitter: semantic split + classify.")

        # ── Step 0: Only handle JSON (OCR bbox) input ──
        if from_upstream.output_format != "json":
            self.set_output("_ERROR",
                            f"SmartSplitter only supports JSON (OCR bbox) input, got: {from_upstream.output_format}")
            return

        json_result = from_upstream.json_result or []
        if not json_result:
            self.set_output("chunks", [])
            self.callback(1, "No input bboxes.")
            return

        # ── Step 1: Build sections from bboxes (same as Splitter) ──
        sections = []  # [(text, position_tag), ...]
        section_images = []
        # ── 增强：收集每个 bbox 的 row_positions（仅表格 bbox 有） ──
        section_row_positions = []
        for o in json_result:
            pos_tag = o.get("position_tag", "")
            # Fallback: table/figure bboxes from Parser have positions but no position_tag.
            # Reconstruct position_tag from positions using the same format as _line_tag().
            if not pos_tag and o.get("positions"):
                p = o["positions"][0]  # [page, x0, x1, top, bottom]
                pos_tag = "@@{}\t{:.1f}\t{:.1f}\t{:.1f}\t{:.1f}##".format(*p)
            sections.append((o.get("text", ""), pos_tag))
            section_images.append(
                id2image(o.get("img_id"),
                         partial(settings.STORAGE_IMPL.get, tenant_id=self._canvas._tenant_id))
            )
            section_row_positions.append(o.get("row_positions"))  # ← 增强：透传 row_positions

        self.callback(0.1, f"Loaded {len(sections)} OCR bboxes.")

        # ── Step 2: Concatenate all bbox text into full document text ──
        #    Keep track of each bbox's char range in the full text
        #    ✨ Enhancement: Add bbox index prefix for LLM to reference
        bbox_ranges = []  # [(start_char, end_char), ...] for each bbox
        full_text_parts = []
        char_offset = 0
        for i, (text, _pos_tag) in enumerate(sections):
            clean_text = text.strip()
            if not clean_text:
                bbox_ranges.append((char_offset, char_offset))
                continue
            start = char_offset
            # ✨ Enhancement: Add row markers [BBOX-N-Rn] for table bboxes with row_positions
            display_text = clean_text
            if "<tr>" in clean_text.lower() and section_row_positions[i]:
                display_text = _add_row_markers(clean_text, i)
            # ✨ Add bbox index prefix: [BBOX-0], [BBOX-1], ...
            indexed_text = f"[BBOX-{i}] {display_text}"
            full_text_parts.append(indexed_text)
            char_offset += len(indexed_text) + 1  # +1 for \n separator
            bbox_ranges.append((start, char_offset - 1))  # end is exclusive of \n

        full_text = "\n".join(full_text_parts)
        self.callback(0.15, f"Full document: {len(full_text)} chars, {len(sections)} bboxes.")

        if not full_text.strip():
            self.set_output("chunks", [])
            self.callback(1, "Empty document text.")
            return

        # ── Step 3: Call LLM for semantic splitting + classification ──
        sys_prompt = self._param.sys_prompt
        if not sys_prompt or not sys_prompt.strip():
            self.set_output("_ERROR", "SmartSplitter sys_prompt is empty. Configure it in DSL.")
            return

        msg = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": full_text}
        ]

        self.callback(0.2, "Calling LLM for semantic splitting...")
        # NOTE: Do NOT use response_format={"type": "json_object"} here.
        # vLLM's json_object mode forces output as a single dict, not an array.
        # The prompt already instructs the model to return a JSON array.
        llm_response = await self._generate_async(msg)
        llm_response = strip_markdown_json_fence(llm_response)

        self.callback(0.5, "LLM responded. Parsing segments...")

        # ── Guard: if LLM backend returned an error string (e.g. connection failure, retries exhausted),
        #    propagate it directly instead of attempting JSON parse.
        if isinstance(llm_response, str) and llm_response.startswith("**ERROR**"):
            logging.error(f"[SmartSplitter] LLM backend error: {llm_response[:500]}")
            self.set_output("_ERROR", llm_response)
            return

        try:
            segments = json.loads(llm_response)
            if not isinstance(segments, list):
                raise ValueError(f"Expected JSON array, got {type(segments).__name__}")
        except (json.JSONDecodeError, ValueError) as e:
            logging.error(f"[SmartSplitter] LLM JSON parse failed: {e}\nRaw: {llm_response[:500]}")
            self.set_output("_ERROR", f"LLM returned invalid JSON: {e}")
            return

        if not segments:
            self.set_output("chunks", [])
            self.callback(1, "LLM returned 0 segments.")
            return

        self.callback(0.55, f"LLM returned {len(segments)} segments. Cutting text...")

        # ── Step 4: Cut by bbox_id (priority) or first_line (fallback) ──
        #    ✨ Enhancement: If LLM returns bbox_start/bbox_end, use direct bbox slicing.
        #    Otherwise, fallback to first_line matching (existing logic).
        
        chunks = []
        segments_using_bbox = 0
        segments_using_firstline = 0
        
        for seg_idx, seg in enumerate(segments):
            # ✨ Priority path: bbox_id-based slicing
            if "bbox_start" in seg and "bbox_end" in seg:
                b_start = seg.get("bbox_start")
                b_end = seg.get("bbox_end")

                # 类型转换：如果是字符串，尝试转换为整数
                if isinstance(b_start, str):
                    try:
                        b_start = int(b_start)
                    except (ValueError, TypeError):
                        b_start = -1
                if isinstance(b_end, str):
                    try:
                        b_end = int(b_end)
                    except (ValueError, TypeError):
                        b_end = -1

                # Validate bbox_id range
                if not isinstance(b_start, int) or not isinstance(b_end, int):
                    logging.warning(f"[SmartSplitter] Segment {seg_idx} has non-integer bbox_id: start={b_start}, end={b_end}, fallback to first_line")
                elif b_start < 0 or b_end < 0 or b_end >= len(sections) or b_start > b_end:
                    # ✨ 增强：bbox_id 无效时，尝试智能推断 bbox 范围
                    first_line = seg.get("first_line", "").strip()
                    doc_type = seg.get("type", "").strip()

                    # 策略1：如果有 first_line，优先使用精确匹配
                    if first_line:
                        for i, (text, _) in enumerate(sections):
                            if first_line in text or text.startswith(first_line[:20]):
                                if b_start < 0:
                                    b_start = i
                                if b_end < 0:
                                    b_end = _infer_bbox_end(i, seg_idx, segments, len(sections))
                                logging.warning(
                                    f"[SmartSplitter] Segment {seg_idx} type={doc_type} bbox_id invalid, "
                                    f"matched first_line at bbox {i}, inferred range: [{b_start}, {b_end}]"
                                )
                                break

                    # 策略2：如果b_start有效但b_end无效，或反之，尝试推断
                    if b_start >= 0 and b_end < 0:
                        # b_start有效，从下一个segment推断b_end
                        b_end = _infer_bbox_end(b_start, seg_idx, segments, len(sections))
                        logging.warning(
                            f"[SmartSplitter] Segment {seg_idx} type={doc_type}, "
                            f"bbox_start={b_start} valid but bbox_end=-1, inferred bbox_end={b_end}"
                        )
                    elif b_end >= 0 and b_start < 0:
                        # b_end有效，从上一个segment反向推断b_start
                        b_start = _infer_bbox_start(b_end, seg_idx, segments)
                        logging.warning(
                            f"[SmartSplitter] Segment {seg_idx} type={doc_type}, "
                            f"bbox_end={b_end} valid but bbox_start=-1, inferred bbox_start={b_start}"
                        )

                    # 如果仍然无法修正，记录警告
                    if b_start < 0 or b_end < 0:
                        logging.warning(
                            f"[SmartSplitter] Segment {seg_idx} type={doc_type} bbox_id invalid [{b_start}, {b_end}], "
                            f"no match found, fallback to first_line path"
                        )

                # 再次验证修正后的范围
                if not (0 <= b_start <= b_end < len(sections)):
                    # 仍然无效，走 fallback
                    continue

                # ✅ Valid bbox_id range — direct slicing
                chunk_text_parts = []
                chunk_position_tags = []
                chunk_images = []

                # ── 增强：读取 LLM 返回的行范围（二级索引，可选） ──
                row_start = seg.get("row_start")
                row_end = seg.get("row_end")
                has_valid_row_range = (
                    row_start is not None and row_end is not None
                    and isinstance(row_start, int) and isinstance(row_end, int)
                )

                for i in range(b_start, b_end + 1):
                    text, pos_tag = sections[i]
                    clean = text.strip()
                    if not clean:
                        if pos_tag:
                            chunk_position_tags.append(pos_tag)
                        continue

                    # ── 增强：表格 bbox + 有效行范围 → 按行裁剪 content ──
                    if has_valid_row_range and "<tr>" in clean.lower() and section_row_positions[i]:
                        trimmed = _trim_table_rows(clean, row_start, row_end)
                        chunk_text_parts.append(trimmed)
                    else:
                        chunk_text_parts.append(clean)

                    if pos_tag:
                        chunk_position_tags.append(pos_tag)
                    if section_images[i] is not None:
                        chunk_images.append(section_images[i].copy())

                chunk_text = "\n".join(chunk_text_parts)

                # Build position-tagged text
                tagged_parts = []
                for i in range(b_start, b_end + 1):
                    text, pos_tag = sections[i]
                    if text.strip():
                        tagged_parts.append(f"{pos_tag}{text.strip()}")
                tagged_text = "\n".join(tagged_parts)

                # Extract positions
                positions = [
                    [pos[0][-1], *pos[1:]]
                    for pos in RAGFlowPdfParser.extract_positions(tagged_text)
                ]

                # ── 增强：将多行 OCR block 拆分为子位置 ──
                # V4 PaddleOCR 可能将多个物理行合并为一个 block，
                # 导致多行 content 共享同一个粗粒度 position。
                # 按文本长度比例分配 block 的 bbox 高度，使 positions 与 text_lines 1:1 对齐。
                # 原理：字符数越多的行在 PDF 中占据越多的物理垂直空间（自动换行），
                # 因此用字符数作为权重来分配高度，比等分更准确。
                expanded_positions = []
                expansion_applied = False
                for part_idx, part in enumerate(chunk_text_parts):
                    sub_lines = part.split("\n")
                    n_lines = len(sub_lines)
                    if part_idx >= len(positions):
                        pos_to_use = positions[-1] if positions else [1, 0, 0, 0, 0]
                        for _ in range(n_lines):
                            expanded_positions.append(list(pos_to_use))
                    elif n_lines <= 1:
                        expanded_positions.append(positions[part_idx])
                    else:
                        orig = positions[part_idx]
                        page, x0, x1, top, bottom = orig[0], orig[1], orig[2], orig[3], orig[4]
                        total_h = bottom - top
                        if total_h <= 0:
                            for _ in range(n_lines):
                                expanded_positions.append(list(orig))
                        else:
                            # 按字符数比例分配高度（空行最小权重 1）
                            char_weights = [max(len(sl.strip()), 1) for sl in sub_lines]
                            total_weight = sum(char_weights)
                            current_top = float(top)
                            for li in range(n_lines):
                                proportion = char_weights[li] / total_weight
                                sub_h = total_h * proportion
                                sub_top = round(current_top)
                                sub_bottom = round(current_top + sub_h)
                                expanded_positions.append([page, x0, x1, sub_top, sub_bottom])
                                current_top += sub_h
                        expansion_applied = True
                if expansion_applied:
                    logging.info(
                        f"[SmartSplitter] position expansion: {len(positions)} blocks → "
                        f"{len(expanded_positions)} sub-positions"
                    )
                positions = expanded_positions
                    
                # ── 构建 position_line_map（兼容保留） ──
                # 展开后 positions 与 text_lines 通常已 1:1 对齐，
                # position_line_map 不会被存储（条件 len(text_lines)!=len(positions) 为 false）。
                # 保留此逻辑作为边界情况的安全网。
                position_line_map = []
                for part_idx, part in enumerate(chunk_text_parts):
                    part_lines = part.split("\n")
                    for _ in part_lines:
                        position_line_map.append(part_idx)
                # 裁剪到 positions 长度范围内（防止越界）
                if positions:
                    position_line_map = [
                        min(v, len(positions) - 1) for v in position_line_map
                    ]
                
                # Merge images
                merged_image = None
                for img in chunk_images:
                    merged_image = concat_img(merged_image, img)
                
                # ── 增强：按 row_start/row_end 裁剪 row_positions（二级索引） ──
                chunk_row_positions = []
                for i in range(b_start, b_end + 1):
                    rp = section_row_positions[i]
                    if not rp:
                        continue
                    
                    if has_valid_row_range:
                        # 二级索引模式：只取 [row_start, row_end] 范围内的行
                        if 0 <= row_start <= row_end < len(rp):
                            chunk_row_positions.extend(rp[row_start:row_end + 1])
                        else:
                            # row 索引越界 → 降级：给全部
                            logging.warning(
                                f"[SmartSplitter] Segment {seg_idx} row range [{row_start},{row_end}] "
                                f"out of bounds (total {len(rp)} rows), fallback to full row_positions"
                            )
                            chunk_row_positions.extend(rp)
                    else:
                        # 无二级索引 → 现有行为：全部给
                        chunk_row_positions.extend(rp)
                    
                # Build chunk (same format as first_line path)
                chunk = {
                    "text": chunk_text,
                    "image": merged_image,
                    "positions": positions,
                    self._param.classify_field: json.dumps(seg, ensure_ascii=False),
                }
                if chunk_row_positions:
                    chunk["row_positions"] = chunk_row_positions
                    # ── DIAG-LOG-3: SmartSplitter chunk 输出 ──
                    logging.info(
                        f"[DIAG-SPLITTER] chunk row_positions len={len(chunk_row_positions)} "
                        f"row[0]={chunk_row_positions[0]} row[-1]={chunk_row_positions[-1]}"
                    )
                # 当 lines 和 positions 不对齐时，加入映射字段
                text_lines = chunk_text.split("\n")
                if len(text_lines) != len(positions) and position_line_map:
                    chunk["position_line_map"] = position_line_map
                
                chunks.append(chunk)
                segments_using_bbox += 1
                continue  # Skip fallback
            
            # ── Fallback path: first_line matching (existing logic) ──
            segments_using_firstline += 1
            # (existing first_line matching code will be preserved below)
        
        # If all segments used bbox_id, skip the old first_line matching logic
        if segments_using_bbox == len(segments):
            self.callback(0.8, f"All {len(segments)} segments used bbox_id slicing. Saving images...")
            
            # Save images
            tasks = []
            for d in chunks:
                tasks.append(asyncio.create_task(
                    image2id(d, partial(settings.STORAGE_IMPL.put, tenant_id=self._canvas._tenant_id), get_uuid())
                ))
            try:
                await asyncio.gather(*tasks, return_exceptions=False)
            except Exception as e:
                logging.error(f"[SmartSplitter] Error saving images: {e}")
                for t in tasks:
                    t.cancel()
                await asyncio.gather(*tasks, return_exceptions=True)
                raise
            
            self.set_output("chunks", chunks)
            
            # Log summary
            type_counts = {}
            for ck in chunks:
                try:
                    t = json.loads(ck[self._param.classify_field]).get("type", "?")
                except Exception:
                    t = "?"
                type_counts[t] = type_counts.get(t, 0) + 1
            
            summary = f"SmartSplitter done: {len(chunks)} chunks from {len(segments)} LLM segments (all bbox_id). Types: {type_counts}"
            logging.info(f"[SmartSplitter] {summary}")
            self.callback(1, summary)
            return
        
        # Otherwise, process segments that need first_line matching
        self.callback(0.6, f"{segments_using_bbox} segments used bbox_id, {segments_using_firstline} need first_line matching...")
        
        # ── Step 4 (original): Cut full_text by first_line anchors (sequential find) ──
        #    Enhanced matching: exact → strip-space → progressive shorten → backtrack
        def _normalize_for_search(s: str) -> str:
            """Remove spaces/punctuation for fuzzy matching."""
            return re.sub(r'[\s\u3000\-—.．。·、,，:：;；\(\)（）\[\]【】]', '', s)

        def _find_normalized(text: str, needle: str, start: int) -> int:
            """Find needle in text, ignoring whitespace/punctuation differences."""
            norm_needle = _normalize_for_search(needle)
            if not norm_needle:
                return -1
            # Character-by-character normalized search
            i = start
            while i <= len(text) - 1:
                j = i  # position in original text
                k = 0  # position in norm_needle
                while j < len(text) and k < len(norm_needle):
                    ch = text[j]
                    if re.match(r'[\s\u3000\-—.．。·、,，:：;；\(\)（）\[\]【】]', ch):
                        j += 1
                        continue
                    if ch == norm_needle[k]:
                        k += 1
                        j += 1
                    else:
                        break
                if k == len(norm_needle):
                    return i
                i += 1
            return -1

        cut_points = []  # [(start_char, segment_data), ...]
        search_from = 0
        for seg_idx, seg in enumerate(segments):
            # Skip segments that already used bbox_id
            if "bbox_start" in seg and "bbox_end" in seg:
                b_start = seg.get("bbox_start")
                b_end = seg.get("bbox_end")
                if isinstance(b_start, int) and isinstance(b_end, int) and 0 <= b_start <= b_end < len(sections):
                    continue  # Already processed in priority path
            
            first_line = seg.get("first_line", "").strip()
            if not first_line:
                logging.warning(f"[SmartSplitter] Segment {seg_idx} missing first_line: {seg}")
                continue

            pos = -1

            # Strategy 1: Exact match
            pos = full_text.find(first_line, search_from)

            # Strategy 2: Normalized match (ignore spaces/punctuation)
            if pos < 0:
                pos = _find_normalized(full_text, first_line, search_from)
                if pos >= 0:
                    logging.info(f"[SmartSplitter] Normalized match for '{first_line[:30]}' at pos={pos}")

            # Strategy 3: Progressive shortening (try first 20, 12, 8 chars)
            if pos < 0:
                for try_len in [20, 12, 8]:
                    short = first_line[:try_len]
                    pos = full_text.find(short, search_from)
                    if pos >= 0:
                        logging.info(f"[SmartSplitter] Short match ({try_len} chars) for '{short}' at pos={pos}")
                        break
                    # Also try normalized short
                    pos = _find_normalized(full_text, short, search_from)
                    if pos >= 0:
                        logging.info(f"[SmartSplitter] Norm-short match ({try_len}) for '{short}' at pos={pos}")
                        break

            # Strategy 4: Search from beginning (in case search_from is too far ahead)
            if pos < 0 and search_from > 0:
                pos = full_text.find(first_line, 0)
                if pos < 0:
                    pos = _find_normalized(full_text, first_line, 0)
                if pos >= 0:
                    logging.info(f"[SmartSplitter] Backtrack match for '{first_line[:30]}' at pos={pos}")

            if pos < 0:
                logging.warning(f"[SmartSplitter] Cannot locate segment {seg_idx} first_line='{first_line[:40]}' — skipped")
                continue

            cut_points.append((pos, seg))
            search_from = pos + 1

        if not cut_points:
            # If some segments were already processed via bbox_id, that's OK
            if chunks:
                logging.info(f"[SmartSplitter] No first_line segments located, but {len(chunks)} chunks already created via bbox_id.")
            else:
                logging.error("[SmartSplitter] No segments could be located in text!")
                self.set_output("_ERROR", "Failed to locate any LLM segments in document text.")
                return

        # Debug: log final cut_points for diagnostics
        for i, (p, s) in enumerate(cut_points):
            logging.info(
                f"[SmartSplitter] cut_point[{i}]: pos={p}, type={s.get('type','?')}, "
                f"dates={s.get('encounter_dates', [])}, first_line='{s.get('first_line', '')[:30]}'"
            )

        # ── Step 5: Extract text slices and assign bboxes/positions ──
        cks = []
        for idx, (start_char, seg_data) in enumerate(cut_points):
            # End = next segment start, or end of text
            if idx + 1 < len(cut_points):
                end_char = cut_points[idx + 1][0]
            else:
                end_char = len(full_text)

            chunk_text = full_text[start_char:end_char].strip()
            if not chunk_text:
                continue

            # Find which bboxes fall in [start_char, end_char)
            chunk_position_tags = []
            chunk_images = []
            for bi, (b_start, b_end) in enumerate(bbox_ranges):
                # bbox overlaps with chunk range
                if b_end > start_char and b_start < end_char:
                    _text, pos_tag = sections[bi]
                    if pos_tag:
                        chunk_position_tags.append(pos_tag)
                    if section_images[bi] is not None:
                        # CRITICAL: .copy() to avoid shared PIL Image reference across chunks.
                        # Without copy(), concurrent image2id threads would race on the same
                        # Image object's lazy-loaded fp, causing 'NoneType' has no attribute 'read'.
                        # See: JpegImagePlugin.load() sets self.fp = None after reading.
                        chunk_images.append(section_images[bi].copy())

            # Build position-tagged text (same format as naive_merge_with_images output)
            # Reconstruct text with position tags for RAGFlowPdfParser.extract_positions
            tagged_parts = []
            for bi, (b_start, b_end) in enumerate(bbox_ranges):
                if b_end > start_char and b_start < end_char:
                    _text, pos_tag = sections[bi]
                    if _text.strip():
                        tagged_parts.append(f"{pos_tag}{_text.strip()}")

            tagged_text = "\n".join(tagged_parts)

            # Extract positions using RAGFlow's standard method
            positions = [
                [pos[0][-1], *pos[1:]]
                for pos in RAGFlowPdfParser.extract_positions(tagged_text)
            ]

            # Merge images — use concat_img (same as native Splitter's naive_merge_with_images)
            merged_image = None
            for img in chunk_images:
                merged_image = concat_img(merged_image, img)

            # Build classify_result_tks (same format as Extractor:Classify output)
            classify_data = {
                "type": seg_data.get("type", "Other"),
                "encounter_dates": seg_data.get("encounter_dates", []),
                "department": seg_data.get("department"),
                "record_count": seg_data.get("record_count", 1),
            }

            ck = {
                "text": chunk_text,
                "image": merged_image,
                "positions": positions,
                self._param.classify_field: json.dumps(classify_data, ensure_ascii=False),
            }

            # ── 增强：透传 row_positions（仅含表格 section 的 chunk 才有） ──
            # row_positions[i] 坐标对应 content 中第 i 个 <tr>
            # 精确裁剪：部分重叠时只取 chunk 文本范围内的 <tr> 对应坐标
            chunk_row_positions = []
            for bi, (b_start, b_end) in enumerate(bbox_ranges):
                if b_end > start_char and b_start < end_char:
                    if section_row_positions[bi]:
                        # Fast path: bbox 完全在 chunk 内 → 全部保留
                        if b_start >= start_char and b_end <= end_char:
                            chunk_row_positions.extend(section_row_positions[bi])
                        else:
                            # Partial overlap: 只取重叠区间内的 <tr> 坐标
                            bbox_text = full_text[b_start:b_end]
                            ov_start = max(b_start, start_char) - b_start
                            ov_end = min(b_end, end_char) - b_start
                            ov_text = bbox_text[ov_start:ov_end]
                            tr_in_ov = ov_text.lower().count("<tr")
                            if tr_in_ov > 0:
                                tr_before = bbox_text[:ov_start].lower().count("<tr")
                                chunk_row_positions.extend(
                                    section_row_positions[bi][tr_before:tr_before + tr_in_ov]
                                )
            if chunk_row_positions:
                ck["row_positions"] = chunk_row_positions
                # ── DIAG-LOG-3b: SmartSplitter first_line path 输出 ──
                logging.info(
                    f"[DIAG-SPLITTER-FL] chunk row_positions len={len(chunk_row_positions)} "
                    f"row[0]={chunk_row_positions[0]} row[-1]={chunk_row_positions[-1]}"
                )

            cks.append(ck)

        # ✨ Merge chunks from bbox_id path and first_line path
        all_chunks = chunks + cks  # bbox_id chunks first, then first_line chunks
        
        self.callback(0.8, f"Built {len(all_chunks)} chunks ({len(chunks)} from bbox_id, {len(cks)} from first_line). Saving images...")

        # ── Step 6: Save images to storage (same as Splitter) ──
        tasks = []
        for d in all_chunks:
            tasks.append(asyncio.create_task(
                image2id(d, partial(settings.STORAGE_IMPL.put, tenant_id=self._canvas._tenant_id), get_uuid())
            ))
        try:
            await asyncio.gather(*tasks, return_exceptions=False)
        except Exception as e:
            logging.error(f"[SmartSplitter] Error saving images: {e}")
            for t in tasks:
                t.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            raise

        self.set_output("chunks", all_chunks)

        # Log summary
        type_counts = {}
        for ck in all_chunks:
            try:
                t = json.loads(ck[self._param.classify_field]).get("type", "?")
            except Exception:
                t = "?"
            type_counts[t] = type_counts.get(t, 0) + 1

        summary = f"SmartSplitter done: {len(all_chunks)} chunks from {len(segments)} LLM segments ({len(chunks)} bbox_id, {len(cks)} first_line). Types: {type_counts}"
        logging.info(f"[SmartSplitter] {summary}")
        self.callback(1, summary)

    