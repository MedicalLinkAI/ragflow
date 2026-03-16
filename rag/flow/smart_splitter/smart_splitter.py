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


# ─── Default prompt ──────────────────────────────────────────────
DEFAULT_SMART_SPLIT_PROMPT = ""  # Will be set via DSL sys_prompt


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

        self.callback(0.1, f"Loaded {len(sections)} OCR bboxes.")

        # ── Step 2: Concatenate all bbox text into full document text ──
        #    Keep track of each bbox's char range in the full text
        bbox_ranges = []  # [(start_char, end_char), ...] for each bbox
        full_text_parts = []
        char_offset = 0
        for text, _pos_tag in sections:
            clean_text = text.strip()
            if not clean_text:
                bbox_ranges.append((char_offset, char_offset))
                continue
            start = char_offset
            full_text_parts.append(clean_text)
            char_offset += len(clean_text) + 1  # +1 for \n separator
            bbox_ranges.append((start, char_offset - 1))  # end is exclusive of \n

        full_text = "\n".join(full_text_parts)
        self.callback(0.15, f"Full document: {len(full_text)} chars, {len(full_text_parts)} text blocks.")

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
        llm_response = await self._generate_async(msg)
        llm_response = strip_markdown_json_fence(llm_response)

        self.callback(0.5, "LLM responded. Parsing segments...")

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

        # ── Step 4: Cut full_text by first_line anchors (sequential find) ──
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
            logging.error("[SmartSplitter] No segments could be located in text!")
            self.set_output("_ERROR", "Failed to locate any LLM segments in document text.")
            return

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
            cks.append(ck)

        self.callback(0.8, f"Built {len(cks)} chunks. Saving images...")

        # ── Step 6: Save images to storage (same as Splitter) ──
        tasks = []
        for d in cks:
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

        self.set_output("chunks", cks)

        # Log summary
        type_counts = {}
        for ck in cks:
            try:
                t = json.loads(ck[self._param.classify_field]).get("type", "?")
            except Exception:
                t = "?"
            type_counts[t] = type_counts.get(t, 0) + 1

        summary = f"SmartSplitter done: {len(cks)} chunks from {len(segments)} LLM segments. Types: {type_counts}"
        logging.info(f"[SmartSplitter] {summary}")
        self.callback(1, summary)
