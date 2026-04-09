#  Copyright 2026 The InfiniFlow Authors. All Rights Reserved.
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
#
from __future__ import annotations

import base64
import logging
import os
import re
from dataclasses import asdict, dataclass, field, fields
from io import BytesIO
from os import PathLike
from pathlib import Path
from typing import Any, Callable, ClassVar, Literal, Optional, Union, Tuple, List

import numpy as np
import pdfplumber
import requests
from PIL import Image

try:
    from deepdoc.parser.pdf_parser import RAGFlowPdfParser
except Exception:

    class RAGFlowPdfParser:
        pass


AlgorithmType = Literal["PaddleOCR-VL", "PaddleOCR-VL-1.5"]
SectionTuple = tuple[str, ...]
TableTuple = tuple[str, ...]
# ParseResult: sections are always list[SectionTuple]; tables can be list[TableTuple]
# (legacy) or list[dict] (PaddleOCR-VL table info with row_positions).
ParseResult = tuple[list[SectionTuple], list]


_MARKDOWN_IMAGE_PATTERN = re.compile(
    r"""
        <div[^>]*>\s*
        <img[^>]*/>\s*
        </div>
        |
        <img[^>]*/>
        """,
    re.IGNORECASE | re.VERBOSE | re.DOTALL,
)


def _remove_images_from_markdown(markdown: str) -> str:
    return _MARKDOWN_IMAGE_PATTERN.sub("", markdown)


def _normalize_bbox(bbox: list[Any] | tuple[Any, ...]) -> tuple[float, float, float, float]:
    if len(bbox) < 4:
        return 0.0, 0.0, 0.0, 0.0

    left, top, right, bottom = (float(bbox[0]), float(bbox[1]), float(bbox[2]), float(bbox[3]))
    if left > right:
        left, right = right, left
    if top > bottom:
        top, bottom = bottom, top
    return left, top, right, bottom


@dataclass
class PaddleOCRVLConfig:
    """Configuration for PaddleOCR-VL algorithm."""

    use_doc_orientation_classify: Optional[bool] = False
    use_doc_unwarping: Optional[bool] = False
    use_layout_detection: Optional[bool] = None
    use_chart_recognition: Optional[bool] = None
    use_seal_recognition: Optional[bool] = None
    use_ocr_for_image_block: Optional[bool] = None
    layout_threshold: Optional[Union[float, dict]] = None
    layout_nms: Optional[bool] = None
    layout_unclip_ratio: Optional[Union[float, Tuple[float, float], dict]] = None
    layout_merge_bboxes_mode: Optional[Union[str, dict]] = None
    layout_shape_mode: Optional[str] = None
    prompt_label: Optional[str] = None
    format_block_content: Optional[bool] = True
    repetition_penalty: Optional[float] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    min_pixels: Optional[int] = None
    max_pixels: Optional[int] = None
    max_new_tokens: Optional[int] = None
    merge_layout_blocks: Optional[bool] = False
    markdown_ignore_labels: Optional[List[str]] = None
    vlm_extra_args: Optional[dict] = None
    restructure_pages: Optional[bool] = False
    merge_tables: Optional[bool] = None
    relevel_titles: Optional[bool] = None


@dataclass
class PaddleOCRConfig:
    """Main configuration for PaddleOCR parser."""

    api_url: str = ""
    access_token: Optional[str] = None
    algorithm: AlgorithmType = "PaddleOCR-VL"
    request_timeout: int = 600
    prettify_markdown: bool = True
    show_formula_number: bool = True
    visualize: bool = False
    additional_params: dict[str, Any] = field(default_factory=dict)
    algorithm_config: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, config: Optional[dict[str, Any]]) -> "PaddleOCRConfig":
        """Create configuration from dictionary."""
        if not config:
            return cls()

        cfg = config.copy()
        algorithm = cfg.get("algorithm", "PaddleOCR-VL")

        # Validate algorithm
        if algorithm not in ("PaddleOCR-VL", "PaddleOCR-VL-1.5"):
            raise ValueError(f"Unsupported algorithm: {algorithm}")

        # Extract algorithm-specific configuration
        algorithm_config: dict[str, Any] = {}
        if algorithm == "PaddleOCR-VL":
            algorithm_config = asdict(PaddleOCRVLConfig())
        elif algorithm == "PaddleOCR-VL-1.5":
            algorithm_config = asdict(PaddleOCRVLConfig())
        algorithm_config_user = cfg.get("algorithm_config")
        if isinstance(algorithm_config_user, dict):
            algorithm_config.update({k: v for k, v in algorithm_config_user.items() if v is not None})

        # Remove processed keys
        cfg.pop("algorithm_config", None)

        # Prepare initialization arguments
        field_names = {field.name for field in fields(cls)}
        init_kwargs: dict[str, Any] = {}

        for field_name in field_names:
            if field_name in cfg:
                init_kwargs[field_name] = cfg[field_name]

        init_kwargs["algorithm_config"] = algorithm_config

        return cls(**init_kwargs)

    @classmethod
    def from_kwargs(cls, **kwargs: Any) -> "PaddleOCRConfig":
        """Create configuration from keyword arguments."""
        return cls.from_dict(kwargs)


class PaddleOCRParser(RAGFlowPdfParser):
    """Parser for PDF documents using PaddleOCR API."""

    _ZOOMIN = 2

    _COMMON_FIELD_MAPPING: ClassVar[dict[str, str]] = {
        "prettify_markdown": "prettifyMarkdown",
        "show_formula_number": "showFormulaNumber",
        "visualize": "visualize",
    }

    _ALGORITHM_FIELD_MAPPINGS: ClassVar[dict[str, dict[str, str]]] = {
        "PaddleOCR-VL": {
            "use_doc_orientation_classify": "useDocOrientationClassify",
            "use_doc_unwarping": "useDocUnwarping",
            "use_layout_detection": "useLayoutDetection",
            "use_chart_recognition": "useChartRecognition",
            "use_seal_recognition": "useSealRecognition",
            "use_ocr_for_image_block": "useOcrForImageBlock",
            "layout_threshold": "layoutThreshold",
            "layout_nms": "layoutNms",
            "layout_unclip_ratio": "layoutUnclipRatio",
            "layout_merge_bboxes_mode": "layoutMergeBboxesMode",
            "layout_shape_mode": "layoutShapeMode",
            "prompt_label": "promptLabel",
            "format_block_content": "formatBlockContent",
            "repetition_penalty": "repetitionPenalty",
            "temperature": "temperature",
            "top_p": "topP",
            "min_pixels": "minPixels",
            "max_pixels": "maxPixels",
            "max_new_tokens": "maxNewTokens",
            "merge_layout_blocks": "mergeLayoutBlocks",
            "markdown_ignore_labels": "markdownIgnoreLabels",
            "vlm_extra_args": "vlmExtraArgs",
            "restructure_pages": "restructurePages",
            "merge_tables": "mergeTables",
            "relevel_titles": "relevelTitles",
        },
        # PaddleOCR-VL-1.5: same HTTP API interface as PaddleOCR-VL (unified interface per official docs).
        # Model version is determined by which server is deployed (--model_name PaddleOCR-VL-1.5-0.9B).
        "PaddleOCR-VL-1.5": {
            "use_doc_orientation_classify": "useDocOrientationClassify",
            "use_doc_unwarping": "useDocUnwarping",
            "use_layout_detection": "useLayoutDetection",
            "use_chart_recognition": "useChartRecognition",
            "use_seal_recognition": "useSealRecognition",
            "use_ocr_for_image_block": "useOcrForImageBlock",
            "layout_threshold": "layoutThreshold",
            "layout_nms": "layoutNms",
            "layout_unclip_ratio": "layoutUnclipRatio",
            "layout_merge_bboxes_mode": "layoutMergeBboxesMode",
            "layout_shape_mode": "layoutShapeMode",
            "prompt_label": "promptLabel",
            "format_block_content": "formatBlockContent",
            "repetition_penalty": "repetitionPenalty",
            "temperature": "temperature",
            "top_p": "topP",
            "min_pixels": "minPixels",
            "max_pixels": "maxPixels",
            "max_new_tokens": "maxNewTokens",
            "merge_layout_blocks": "mergeLayoutBlocks",
            "markdown_ignore_labels": "markdownIgnoreLabels",
            "vlm_extra_args": "vlmExtraArgs",
            "restructure_pages": "restructurePages",
            "merge_tables": "mergeTables",
            "relevel_titles": "relevelTitles",
        },
    }

    def __init__(
        self,
        api_url: Optional[str] = None,
        access_token: Optional[str] = None,
        algorithm: AlgorithmType = "PaddleOCR-VL",
        *,
        request_timeout: int = 600,
    ):
        """Initialize PaddleOCR parser."""
        super().__init__()

        self.outlines = []
        self.api_url = api_url.rstrip("/") if api_url else os.getenv("PADDLEOCR_API_URL", "")
        self.access_token = access_token or os.getenv("PADDLEOCR_ACCESS_TOKEN")
        self.algorithm = algorithm
        self.request_timeout = request_timeout
        self.logger = logging.getLogger(self.__class__.__name__)

        # Force PDF file type
        self.file_type = 0

        # Initialize page images for cropping
        self.page_images: list[Image.Image] = []
        self.page_from = 0

    # Public methods
    def check_installation(self) -> tuple[bool, str]:
        """Check if the parser is properly installed and configured."""
        if not self.api_url:
            return False, "[PaddleOCR] API URL not configured"

        # TODO [@Bobholamovic]: Check URL availability and token validity

        return True, ""

    def parse_pdf(
        self,
        filepath: str | PathLike[str],
        binary: BytesIO | bytes | None = None,
        callback: Optional[Callable[[float, str], None]] = None,
        *,
        parse_method: str = "raw",
        api_url: Optional[str] = None,
        access_token: Optional[str] = None,
        algorithm: Optional[AlgorithmType] = None,
        request_timeout: Optional[int] = None,
        prettify_markdown: Optional[bool] = None,
        show_formula_number: Optional[bool] = None,
        visualize: Optional[bool] = None,
        additional_params: Optional[dict[str, Any]] = None,
        algorithm_config: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> ParseResult:
        """Parse PDF document using PaddleOCR API."""
        # Create configuration - pass all kwargs to capture VL config parameters
        config_dict = {
            "api_url": api_url if api_url is not None else self.api_url,
            "access_token": access_token if access_token is not None else self.access_token,
            "algorithm": algorithm if algorithm is not None else self.algorithm,
            "request_timeout": request_timeout if request_timeout is not None else self.request_timeout,
        }
        if prettify_markdown is not None:
            config_dict["prettify_markdown"] = prettify_markdown
        if show_formula_number is not None:
            config_dict["show_formula_number"] = show_formula_number
        if visualize is not None:
            config_dict["visualize"] = visualize
        if additional_params is not None:
            config_dict["additional_params"] = additional_params
        if algorithm_config is not None:
            config_dict["algorithm_config"] = algorithm_config

        cfg = PaddleOCRConfig.from_dict(config_dict)

        if not cfg.api_url:
            raise RuntimeError("[PaddleOCR] API URL missing")

        # Prepare file data and generate page images for cropping
        data_bytes = self._prepare_file_data(filepath, binary)

        # Generate page images for cropping functionality
        input_source = filepath if binary is None else binary
        try:
            self.__images__(input_source, callback=callback)
        except Exception as e:
            self.logger.warning(f"[PaddleOCR] Failed to generate page images for cropping: {e}")

        # Build and send request
        result = self._send_request(data_bytes, cfg, callback)

        # Process response
        sections = self._transfer_to_sections(result, algorithm=cfg.algorithm, parse_method=parse_method)
        if callback:
            callback(0.9, f"[PaddleOCR] done, sections: {len(sections)}")

        tables = self._transfer_to_tables(result)
        if callback:
            callback(1.0, f"[PaddleOCR] done, tables: {len(tables)}")

        return sections, tables

    def _prepare_file_data(self, filepath: str | PathLike[str], binary: BytesIO | bytes | None) -> bytes:
        """Prepare file data for API request."""
        source_path = Path(filepath)

        if binary is not None:
            if isinstance(binary, (bytes, bytearray)):
                return binary
            return binary.getbuffer().tobytes()

        if not source_path.exists():
            raise FileNotFoundError(f"[PaddleOCR] file not found: {source_path}")

        return source_path.read_bytes()

    def _build_payload(self, data: bytes, file_type: int, config: PaddleOCRConfig) -> dict[str, Any]:
        """Build payload for API request."""
        payload: dict[str, Any] = {
            "file": base64.b64encode(data).decode("ascii"),
            "fileType": file_type,
        }

        # Add common parameters
        for param_key, param_value in [
            ("prettify_markdown", config.prettify_markdown),
            ("show_formula_number", config.show_formula_number),
            ("visualize", config.visualize),
        ]:
            if param_value is not None:
                api_param = self._COMMON_FIELD_MAPPING[param_key]
                payload[api_param] = param_value

        # Add algorithm-specific parameters
        algorithm_mapping = self._ALGORITHM_FIELD_MAPPINGS.get(config.algorithm, {})
        for param_key, param_value in config.algorithm_config.items():
            if param_value is not None and param_key in algorithm_mapping:
                api_param = algorithm_mapping[param_key]
                payload[api_param] = param_value

        # Add any additional parameters
        if config.additional_params:
            payload.update(config.additional_params)

        return payload

    def _send_request(self, data: bytes, config: PaddleOCRConfig, callback: Optional[Callable[[float, str], None]]) -> dict[str, Any]:
        """Send request to PaddleOCR API and parse response."""
        # Build payload
        payload = self._build_payload(data, self.file_type, config)

        # Prepare headers
        headers = {"Content-Type": "application/json", "Client-Platform": "ragflow"}
        if config.access_token:
            headers["Authorization"] = f"token {config.access_token}"

        self.logger.info("[PaddleOCR] invoking API")
        if callback:
            callback(0.1, "[PaddleOCR] submitting request")

        # Send request
        try:
            resp = requests.post(config.api_url, json=payload, headers=headers, timeout=self.request_timeout)
            resp.raise_for_status()
        except Exception as exc:
            if callback:
                callback(-1, f"[PaddleOCR] request failed: {exc}")
            raise RuntimeError(f"[PaddleOCR] request failed: {exc}")

        # Parse response
        try:
            response_data = resp.json()
        except Exception as exc:
            raise RuntimeError(f"[PaddleOCR] response is not JSON: {exc}") from exc

        if callback:
            callback(0.8, "[PaddleOCR] response received")

        # Validate response format
        if response_data.get("errorCode") != 0 or not isinstance(response_data.get("result"), dict):
            if callback:
                callback(-1, "[PaddleOCR] invalid response format")
            raise RuntimeError("[PaddleOCR] invalid response format")

        return response_data["result"]

    def _transfer_to_sections(self, result: dict[str, Any], algorithm: AlgorithmType, parse_method: str) -> list[SectionTuple]:
        """Convert API response to section tuples."""
        sections: list[SectionTuple] = []

        if algorithm in ("PaddleOCR-VL", "PaddleOCR-VL-1.5"):
            layout_parsing_results = result.get("layoutParsingResults", [])

            for page_idx, layout_result in enumerate(layout_parsing_results):
                pruned_result = layout_result.get("prunedResult", {})
                parsing_res_list = pruned_result.get("parsing_res_list", [])

                for block in parsing_res_list:
                    block_content = block.get("block_content", "").strip()
                    if not block_content:
                        continue

                    # Remove images
                    block_content = _remove_images_from_markdown(block_content)

                    label = block.get("block_label", "")
                    block_bbox = block.get("block_bbox", [0, 0, 0, 0])
                    left, top, right, bottom = _normalize_bbox(block_bbox)

                    tag = f"@@{page_idx + 1}\t{left // self._ZOOMIN}\t{right // self._ZOOMIN}\t{top // self._ZOOMIN}\t{bottom // self._ZOOMIN}##"

                    if parse_method == "manual":
                        sections.append((block_content, label, tag))
                    elif parse_method == "paper":
                        sections.append((block_content + tag, label))
                    else:
                        sections.append((block_content, tag))

        return sections

    # ── TSR Enhancement: 乐高式可插拔模块 ──────────────────────────
    _tsr_instance = None  # 延迟初始化，不用不加载

    def _tsr_enhance_row_positions(
        self,
        page_idx: int,
        left, top, right, bottom,
        num_rows: int,
        zm,
    ) -> list[list[int]] | None:
        """用 TableStructureRecognizer 对表格区域做二次精确行识别。

        仅在 PaddleOCR-VL 的精确模式失败时调用（乐高式增强，可熔断）。
        从 self.page_images 中裁剪表格区域，调用 TSR 模型识别行坐标。

        Returns:
            行坐标列表 [[page, x0, x1, top, bottom], ...] 或 None（识别失败/不匹配时）
        """
        if not getattr(self, "page_images", None) or page_idx >= len(self.page_images):
            return None

        page_img = self.page_images[page_idx]
        img_w, img_h = page_img.size

        # page_images 分辨率是 72dpi，PaddleOCR API 坐标是 zm*72dpi
        # bbox 坐标需要映射到 72dpi 图片坐标
        scale = 1.0 / zm
        crop_left = max(0, int(left * scale))
        crop_top = max(0, int(top * scale))
        crop_right = min(img_w, int(right * scale))
        crop_bottom = min(img_h, int(bottom * scale))

        if crop_right <= crop_left or crop_bottom <= crop_top:
            return None

        # 裁剪表格区域
        import numpy as np
        table_crop = page_img.crop((crop_left, crop_top, crop_right, crop_bottom))
        table_np = np.array(table_crop)

        # 延迟初始化 TSR（不用不加载模型）
        if PaddleOCRParser._tsr_instance is None:
            from deepdoc.vision import TableStructureRecognizer
            PaddleOCRParser._tsr_instance = TableStructureRecognizer()
            logging.info("[TSR-ENHANCE] TableStructureRecognizer initialized (lazy)")

        tsr = PaddleOCRParser._tsr_instance
        tsr_results = tsr([table_np], thr=0.2)
        if not tsr_results or not tsr_results[0]:
            logging.info("[TSR-ENHANCE] TSR returned no results for page=%d", page_idx + 1)
            return None

        # 诊断：输出 TSR 模型的完整原始输出（所有 label + score）
        all_labels_summary = {}
        for b in tsr_results[0]:
            lbl = b["label"]
            all_labels_summary.setdefault(lbl, []).append(
                round(b.get("score", 0), 3)
            )
        logging.info(
            "[TSR-RAW] page=%d TSR原始输出: 共%d个box, 标签分布: %s",
            page_idx + 1, len(tsr_results[0]),
            {k: f"count={len(v)} scores={sorted(v)}" for k, v in all_labels_summary.items()},
        )

        # 提取 "table row" 和 "table column header" 的 bbox
        row_boxes = [
            b for b in tsr_results[0]
            if b["label"] in ("table row", "table column header")
        ]
        if not row_boxes:
            logging.info("[TSR-ENHANCE] No row boxes detected for page=%d", page_idx + 1)
            return None

        # 按 top 排序
        row_boxes.sort(key=lambda b: b["top"])

        # 去重：column header 和 table row 在同一位置重叠时只保留一个
        # TSR 经常把表头同时检测为 column header + table row
        if len(row_boxes) > 1:
            deduped = [row_boxes[0]]
            for rb in row_boxes[1:]:
                prev = deduped[-1]
                overlap = min(prev["bottom"], rb["bottom"]) - max(prev["top"], rb["top"])
                min_height = min(prev["bottom"] - prev["top"], rb["bottom"] - rb["top"])
                if min_height > 0 and overlap / min_height > 0.5:
                    # 重叠超过 50% → 跳过（保留前一个）
                    logging.info(
                        "[TSR-ENHANCE] Dedup: skip overlapping box (prev_top=%.1f rb_top=%.1f overlap=%.1f)",
                        prev["top"], rb["top"], overlap,
                    )
                    continue
                deduped.append(rb)
            row_boxes = deduped

        # 匹配度检查：TSR 行数与 <tr> 行数差距 <= 2 才采用
        gap = abs(len(row_boxes) - num_rows)
        if gap > 2:
            logging.info(
                "[TSR-ENHANCE] Row count mismatch: TSR=%d vs TR=%d (gap=%d > 2), skip",
                len(row_boxes), num_rows, gap,
            )
            return None

        # 坐标映射说明：
        # - TSR 输出坐标：相对于 72dpi 裁剪图的像素坐标
        # - crop_left/crop_top：裁剪原点在 72dpi 全页图中的位置
        # - 最终 row_positions 格式：[page, x0, x1, top, bottom] 单位是 72dpi 像素
        #   （与 uniform fallback 一致：API坐标 / zm = 72dpi）
        page_1based = page_idx + 1
        row_positions = []

        def _map_rb(rb):
            """TSR bbox → row_positions 格式"""
            return [
                page_1based,
                int(crop_left + rb["x0"]),
                int(crop_left + rb["x1"]),
                int(crop_top + rb["top"]),
                int(crop_top + rb["bottom"]),
            ]

        if len(row_boxes) == num_rows:
            # 完美匹配：1:1 映射
            for rb in row_boxes:
                row_positions.append(_map_rb(rb))
        elif len(row_boxes) == num_rows - 1:
            # TSR 少一行（通常是表头未检测为 row）→ 补一行表头
            row_positions.append([
                page_1based,
                int(left // zm),
                int(right // zm),
                int(top // zm),
                int(crop_top + row_boxes[0]["top"]),
            ])
            for rb in row_boxes:
                row_positions.append(_map_rb(rb))
        elif len(row_boxes) == num_rows + 1:
            # TSR 多一行 → 用中位行高过滤噪声行
            heights = [rb["bottom"] - rb["top"] for rb in row_boxes]
            sorted_h = sorted(heights)
            median_h = sorted_h[len(sorted_h) // 2]
            if median_h > 0:
                threshold = median_h * 0.7
                filtered = [rb for rb, h in zip(row_boxes, heights) if h >= threshold]
            else:
                filtered = []
            if len(filtered) == num_rows:
                # 过滤后刚好匹配 TR 行数 → 采用
                logging.info(
                    "[TSR-ENHANCE] page=%d median_h=%.1f threshold=%.1f "
                    "filtered %d→%d rows (removed %s)",
                    page_1based, median_h, threshold,
                    len(row_boxes), len(filtered),
                    [(i, heights[i]) for i in range(len(heights)) if heights[i] < threshold],
                )
                for rb in filtered:
                    row_positions.append(_map_rb(rb))
            else:
                # 过滤后数量不匹配 → 保守回退丢尾
                logging.info(
                    "[TSR-ENHANCE] page=%d 丢尾分支: median_h=%.1f threshold=%.1f "
                    "filtered=%d (expected %d). 全部行框: %s",
                    page_1based, median_h, threshold,
                    len(filtered), num_rows,
                    [(i, rb.get("label", "?"), round(heights[i], 1))
                     for i, rb in enumerate(row_boxes)],
                )
                for rb in row_boxes[:num_rows]:
                    row_positions.append(_map_rb(rb))
        else:
            return None

        logging.info(
            "[TSR-ENHANCE] page=%d tsr_rows=%d tr_rows=%d → %d positions "
            "row[0]=%s row[-1]=%s",
            page_1based, len(row_boxes), num_rows, len(row_positions),
            row_positions[0], row_positions[-1],
        )
        return row_positions

    @staticmethod
    def _cluster_row_boundaries(
        boxes: list[dict],
        table_bbox: tuple[float, float, float, float],
        num_tr: int,
        merge_gap: float = 12.0,
    ) -> list[tuple[float, float]] | None:
        """Cluster layout_det_res boxes inside *table_bbox* into row boundaries.

        Returns a list of (row_top, row_bottom) in API pixel coordinates,
        one per detected row, **sorted by y**.  Returns ``None`` when the
        detected rows are too few to be useful (< 50 % of *num_tr*).

        Algorithm
        ---------
        1. Collect every non-table box whose vertical centre falls inside the
           table bbox.
        2. Sort by y-top and merge nearby entries (gap < *merge_gap*) into the
           same row band.
        3. Each band's top = min(y_tops), bottom = max(y_bottoms) of its
           members.
        """
        t_left, t_top, t_right, t_bottom = table_bbox

        # Step 1 – collect candidate boxes inside the table region
        candidates: list[tuple[float, float]] = []  # (y_top, y_bottom)
        _skip_labels = {"table", "chart", "figure", "image"}
        for b in boxes:
            if b.get("label", "") in _skip_labels:
                continue  # skip non-text boxes
            coord = b.get("coordinate", [0, 0, 0, 0])
            bx0, by0, bx1, by1 = coord[0], coord[1], coord[2], coord[3]
            # Box centre must be inside the table bbox (with small tolerance)
            cy = (by0 + by1) / 2
            cx = (bx0 + bx1) / 2
            if t_top - 5 <= cy <= t_bottom + 5 and t_left - 5 <= cx <= t_right + 5:
                candidates.append((float(by0), float(by1)))

        if not candidates:
            return None

        # Step 2 – sort by y-top, merge into row bands
        candidates.sort()
        bands: list[list[tuple[float, float]]] = [[candidates[0]]]
        for y_top, y_bot in candidates[1:]:
            last_band = bands[-1]
            # Compare with the *average* y-top of the current band
            avg_top = sum(t for t, _ in last_band) / len(last_band)
            if y_top - avg_top < merge_gap:
                last_band.append((y_top, y_bot))
            else:
                bands.append([(y_top, y_bot)])

        # Step 3 – derive row boundaries from each band, clamped to table bbox
        row_bounds: list[tuple[float, float]] = []
        for band in bands:
            band_top = max(min(t for t, _ in band), t_top)
            band_bot = min(max(b for _, b in band), t_bottom)
            if band_bot <= band_top:
                continue  # degenerate band, skip
            row_bounds.append((band_top, band_bot))

        # Sanity check: at least 50 % of <tr> rows must be detected
        if len(row_bounds) < max(num_tr * 0.5, 1):
            return None

        return row_bounds

    def _transfer_to_tables(self, result: dict[str, Any]) -> list[dict[str, Any]]:
        """Extract table blocks from API response with row-level bounding boxes.

        Returns a list of table info dicts, each containing:
        - page: 1-indexed page number
        - bbox: [x0, y0, x1, y1] in original pixel coordinates
        - html: the <table> HTML content
        - row_positions: list of [page(1-indexed), x0, x1, top, bottom]
                         coordinates divided by _ZOOMIN (matching section tag coords)

        Row positions are computed in two ways:
        1. **Precise mode** – when ``layout_det_res.boxes`` contains enough
           text-level bboxes inside the table, cluster them into row bands and
           derive per-row top/bottom from the actual text positions.
        2. **Uniform fallback** – evenly divide the table bbox height by the
           number of ``<tr>`` rows (less accurate for tables with varying row
           heights or embedded charts).
        """
        tables: list[dict[str, Any]] = []

        layout_parsing_results = result.get("layoutParsingResults", [])
        for page_idx, layout_result in enumerate(layout_parsing_results):
            pruned_result = layout_result.get("prunedResult", {})
            parsing_res_list = pruned_result.get("parsing_res_list", [])

            # Gather layout_det_res boxes for this page (used by precise mode)
            det_boxes = (
                pruned_result.get("layout_det_res", {}).get("boxes", [])
            )

            for block in parsing_res_list:
                if block.get("block_label") != "table":
                    continue

                html_content = block.get("block_content", "").strip()
                if not html_content:
                    continue

                block_bbox = block.get("block_bbox", [0, 0, 0, 0])
                left, top, right, bottom = _normalize_bbox(block_bbox)

                # Count <tr> rows in the HTML
                tr_matches = re.findall(r"<tr[^>]*>", html_content, re.IGNORECASE)
                num_rows = len(tr_matches)
                if num_rows == 0:
                    num_rows = 1  # fallback: treat entire table as 1 row

                page_1based = page_idx + 1
                zm = self._ZOOMIN
                mode = "uniform"  # track which mode was used (for logging)

                # ── Try precise row positioning from layout_det_res ──
                row_positions = []
                if det_boxes:
                    clustered = self._cluster_row_boundaries(
                        det_boxes, (left, top, right, bottom), num_rows,
                    )
                    if clustered is not None:
                        # ── Coverage check: bands must span a meaningful
                        # portion of the table height. If detected text blocks
                        # only cover a small slice (e.g. only header area),
                        # precise modes are unreliable. Use refined-uniform
                        # with a tighter effective region instead.
                        bands_span = clustered[-1][1] - clustered[0][0]
                        table_height = bottom - top
                        coverage = bands_span / table_height if table_height > 0 else 0
                        if coverage < 0.3 and len(clustered) >= 1:
                            # Estimate effective data region from detected bands
                            n_bands = len(clustered)
                            avg_h = bands_span / max(n_bands - 1, 1)
                            if avg_h < 1:
                                avg_h = bands_span  # single band
                            eff_top = max(clustered[0][0] - avg_h, top)
                            # Extra rows beyond detected bands extend downward
                            extra_rows = max(num_rows - n_bands, 1)
                            eff_bot = min(
                                clustered[-1][1] + avg_h * extra_rows * 1.5,
                                bottom,
                            )
                            row_height = (eff_bot - eff_top) / num_rows
                            for i in range(num_rows):
                                row_positions.append([
                                    page_1based,
                                    int(left // zm),
                                    int(right // zm),
                                    int((eff_top + i * row_height) // zm),
                                    int((eff_top + (i + 1) * row_height) // zm),
                                ])
                            mode = "refined-uniform-cov"
                            clustered = None  # skip precise modes below

                    if clustered is not None:
                        n_bands = len(clustered)
                        gap = num_rows - n_bands

                        if gap == 0:
                            # Exact match: 1:1 mapping using midpoints
                            boundaries: list[float] = [top]
                            for i in range(n_bands - 1):
                                mid = (clustered[i][1] + clustered[i + 1][0]) / 2
                                boundaries.append(mid)
                            boundaries.append(bottom)
                            for i in range(num_rows):
                                row_positions.append([
                                    page_1based,
                                    int(left // zm),
                                    int(right // zm),
                                    int(boundaries[i] // zm),
                                    int(boundaries[i + 1] // zm),
                                ])
                            mode = "precise"

                        elif gap == 1:
                            # One row undetected.  Determine whether it is the
                            # header (top) or trailer (bottom) by checking how
                            # far band[0] sits from the table top.
                            avg_bh = (clustered[-1][1] - clustered[0][0]) / max(n_bands - 1, 1)
                            header_gap = clustered[0][0] - top
                            if header_gap > avg_bh * 0.5:
                                # band[0] is far from table top → header missing
                                row_positions.append([
                                    page_1based,
                                    int(left // zm),
                                    int(right // zm),
                                    int(top // zm),
                                    int(clustered[0][0] // zm),
                                ])
                                for i in range(n_bands):
                                    r_top = clustered[i][0] if i == 0 else (clustered[i - 1][1] + clustered[i][0]) / 2
                                    r_bot = (clustered[i][1] + clustered[i + 1][0]) / 2 if i + 1 < n_bands else bottom
                                    row_positions.append([
                                        page_1based,
                                        int(left // zm),
                                        int(right // zm),
                                        int(r_top // zm),
                                        int(r_bot // zm),
                                    ])
                                mode = "precise-h"
                            else:
                                # band[0] starts near table top → trailer missing
                                for i in range(n_bands):
                                    r_top = top if i == 0 else (clustered[i - 1][1] + clustered[i][0]) / 2
                                    r_bot = (clustered[i][1] + clustered[i + 1][0]) / 2 if i + 1 < n_bands else clustered[i][1]
                                    row_positions.append([
                                        page_1based,
                                        int(left // zm),
                                        int(right // zm),
                                        int(r_top // zm),
                                        int(r_bot // zm),
                                    ])
                                # Append trailer row
                                row_positions.append([
                                    page_1based,
                                    int(left // zm),
                                    int(right // zm),
                                    int(clustered[-1][1] // zm),
                                    int(bottom // zm),
                                ])
                                mode = "precise-t"

                        elif gap == 2:
                            # Header + trailer missing: prepend header, append trailer
                            row_positions.append([
                                page_1based,
                                int(left // zm),
                                int(right // zm),
                                int(top // zm),
                                int(clustered[0][0] // zm),
                            ])
                            for i in range(n_bands):
                                r_top = clustered[i][0] if i == 0 else (clustered[i - 1][1] + clustered[i][0]) / 2
                                r_bot = (clustered[i][1] + clustered[i + 1][0]) / 2 if i + 1 < n_bands else clustered[i][1]
                                row_positions.append([
                                    page_1based,
                                    int(left // zm),
                                    int(right // zm),
                                    int(r_top // zm),
                                    int(r_bot // zm),
                                ])
                            # Trailer row: from last band bottom to table bottom
                            row_positions.append([
                                page_1based,
                                int(left // zm),
                                int(right // zm),
                                int(clustered[-1][1] // zm),
                                int(bottom // zm),
                            ])
                            mode = "precise-ht"

                        else:
                            # gap > 2: use detected bands to refine effective
                            # data region, then uniform-divide within that region
                            avg_h = (clustered[-1][1] - clustered[0][0]) / max(n_bands - 1, 1)
                            eff_top = max(clustered[0][0] - avg_h, top)
                            eff_bot = min(clustered[-1][1] + avg_h, bottom)
                            row_height = (eff_bot - eff_top) / num_rows
                            for i in range(num_rows):
                                row_positions.append([
                                    page_1based,
                                    int(left // zm),
                                    int(right // zm),
                                    int((eff_top + i * row_height) // zm),
                                    int((eff_top + (i + 1) * row_height) // zm),
                                ])
                            mode = "refined-uniform"

                # ── Level 1 结果日志 ──
                if row_positions:
                    logging.info(
                        f"[ROW-POS] page={page_1based} Level-1(det_boxes) SUCCESS → mode={mode} "
                        f"rows={len(row_positions)} row[0]={row_positions[0]} row[-1]={row_positions[-1]}"
                    )
                else:
                    logging.info(
                        f"[ROW-POS] page={page_1based} Level-1(det_boxes) MISS → "
                        f"det_boxes={len(det_boxes) if det_boxes else 0} num_rows={num_rows} "
                        f"reason: clustered行数不足50%或det_boxes为空"
                    )

                # ── TSR Enhancement（Level 2）: 用 TableStructureRecognizer 精确识别行坐标 ──
                # 乐高式设计：可通过 PADDLEOCR_TSR_ENHANCE 环境变量开关（默认开启）
                # 仅在 Level 1 失败时触发，不影响已有 precise/refined-uniform 路径
                tsr_enabled = os.getenv("PADDLEOCR_TSR_ENHANCE", "true").lower() in ("true", "1", "yes")
                if not row_positions and tsr_enabled:
                    logging.info(
                        f"[ROW-POS] page={page_1based} Level-2(TSR) ENTER → "
                        f"bbox=[{left},{top},{right},{bottom}] zm={zm} num_rows={num_rows}"
                    )
                    try:
                        tsr_positions = self._tsr_enhance_row_positions(
                            page_idx, left, top, right, bottom, num_rows, zm,
                        )
                        if tsr_positions:
                            row_positions = tsr_positions
                            mode = "tsr-precise"
                            logging.info(
                                f"[ROW-POS] page={page_1based} Level-2(TSR) SUCCESS → "
                                f"rows={len(row_positions)} row[0]={row_positions[0]} row[-1]={row_positions[-1]}"
                            )
                        else:
                            logging.info(
                                f"[ROW-POS] page={page_1based} Level-2(TSR) MISS → "
                                f"返回 None（详细原因见上方 [TSR-ENHANCE] 日志）"
                            )
                    except Exception as e:
                        logging.warning(
                            f"[ROW-POS] page={page_1based} Level-2(TSR) ERROR → "
                            f"异常捕获，降级到 Level-3: {e}"
                        )
                elif not row_positions and not tsr_enabled:
                    logging.info(
                        f"[ROW-POS] page={page_1based} Level-2(TSR) SKIP → "
                        f"开关关闭(PADDLEOCR_TSR_ENHANCE={os.getenv('PADDLEOCR_TSR_ENHANCE', 'true')})"
                    )

                # ── Uniform fallback（Level 3）──
                if not row_positions:
                    logging.info(
                        f"[ROW-POS] page={page_1based} Level-3(Uniform) ENTER → "
                        f"bbox_height={bottom - top} / {num_rows} rows = {(bottom - top) / num_rows:.1f}px/row"
                    )
                    table_height = bottom - top
                    row_height = table_height / num_rows
                    for row_idx in range(num_rows):
                        row_top = top + row_idx * row_height
                        row_bottom = top + (row_idx + 1) * row_height
                        row_positions.append([
                            page_1based,
                            int(left // zm),
                            int(right // zm),
                            int(row_top // zm),
                            int(row_bottom // zm),
                        ])
                    mode = "uniform"

                tables.append({
                    "page": page_1based,
                    "bbox": [left, top, right, bottom],
                    "html": html_content,
                    "row_positions": row_positions,
                    "position_tag": f"@@{page_1based}\t{int(left // zm)}\t{int(right // zm)}\t{int(top // zm)}\t{int(bottom // zm)}##",
                })

                # ── DIAG-LOG-1: _transfer_to_tables 出口 ──
                logging.info(
                    f"[DIAG-TABLE] page={page_1based} mode={mode} "
                    f"bbox=[{left},{top},{right},{bottom}] zm={zm} num_rows={num_rows} "
                    f"row[0]={row_positions[0]} row[-1]={row_positions[-1]}"
                )

        return tables

    def __images__(self, fnm, page_from=0, page_to=100, callback=None):
        """Generate page images from PDF for cropping."""
        self.page_from = page_from
        self.page_to = page_to
        try:
            with pdfplumber.open(fnm) if isinstance(fnm, (str, PathLike)) else pdfplumber.open(BytesIO(fnm)) as pdf:
                self.pdf = pdf
                self.page_images = [p.to_image(resolution=72, antialias=True).original for i, p in enumerate(self.pdf.pages[page_from:page_to])]
        except Exception as e:
            self.page_images = None
            self.logger.exception(e)

    @staticmethod
    def extract_positions(txt: str):
        """Extract position information from text tags."""
        poss = []
        for tag in re.findall(r"@@[0-9-]+\t[0-9.\t]+##", txt):
            pn, left, right, top, bottom = tag.strip("#").strip("@").split("\t")
            left, right, top, bottom = float(left), float(right), float(top), float(bottom)
            poss.append(([int(p) - 1 for p in pn.split("-")], left, right, top, bottom))
        return poss

    def crop(self, text: str, need_position: bool = False):
        """Crop images from PDF based on position tags in text."""
        imgs = []
        poss = self.extract_positions(text)

        if not poss:
            if need_position:
                return None, None
            return

        if not getattr(self, "page_images", None):
            self.logger.warning("[PaddleOCR] crop called without page images; skipping image generation.")
            if need_position:
                return None, None
            return

        page_count = len(self.page_images)

        filtered_poss = []
        for pns, left, right, top, bottom in poss:
            if not pns:
                self.logger.warning("[PaddleOCR] Empty page index list in crop; skipping this position.")
                continue
            valid_pns = [p for p in pns if 0 <= p < page_count]
            if not valid_pns:
                self.logger.warning(f"[PaddleOCR] All page indices {pns} out of range for {page_count} pages; skipping.")
                continue
            filtered_poss.append((valid_pns, left, right, top, bottom))

        poss = filtered_poss
        if not poss:
            self.logger.warning("[PaddleOCR] No valid positions after filtering; skip cropping.")
            if need_position:
                return None, None
            return

        max_width = max(np.max([right - left for (_, left, right, _, _) in poss]), 6)
        GAP = 6
        pos = poss[0]
        first_page_idx = pos[0][0]
        poss.insert(0, ([first_page_idx], pos[1], pos[2], max(0, pos[3] - 120), max(pos[3] - GAP, 0)))
        pos = poss[-1]
        last_page_idx = pos[0][-1]
        if not (0 <= last_page_idx < page_count):
            self.logger.warning(f"[PaddleOCR] Last page index {last_page_idx} out of range for {page_count} pages; skipping crop.")
            if need_position:
                return None, None
            return
        last_page_height = self.page_images[last_page_idx].size[1]
        poss.append(
            (
                [last_page_idx],
                pos[1],
                pos[2],
                min(last_page_height, pos[4] + GAP),
                min(last_page_height, pos[4] + 120),
            )
        )

        positions = []
        for ii, (pns, left, right, top, bottom) in enumerate(poss):
            right = left + max_width

            if bottom <= top:
                bottom = top + 2

            for pn in pns[1:]:
                if 0 <= pn - 1 < page_count:
                    bottom += self.page_images[pn - 1].size[1]
                else:
                    self.logger.warning(f"[PaddleOCR] Page index {pn}-1 out of range for {page_count} pages during crop; skipping height accumulation.")

            if not (0 <= pns[0] < page_count):
                self.logger.warning(f"[PaddleOCR] Base page index {pns[0]} out of range for {page_count} pages during crop; skipping this segment.")
                continue

            img0 = self.page_images[pns[0]]
            x0, y0, x1, y1 = int(left), int(top), int(right), int(min(bottom, img0.size[1]))
            if x0 > x1:
                x0, x1 = x1, x0
            if y0 > y1:
                y0, y1 = y1, y0
            x0 = max(0, min(x0, img0.size[0]))
            x1 = max(0, min(x1, img0.size[0]))
            y0 = max(0, min(y0, img0.size[1]))
            y1 = max(0, min(y1, img0.size[1]))
            if x1 <= x0 or y1 <= y0:
                continue
            crop0 = img0.crop((x0, y0, x1, y1))
            imgs.append(crop0)
            if 0 < ii < len(poss) - 1:
                positions.append((pns[0] + self.page_from, x0, x1, y0, y1))

            bottom -= img0.size[1]
            for pn in pns[1:]:
                if not (0 <= pn < page_count):
                    self.logger.warning(f"[PaddleOCR] Page index {pn} out of range for {page_count} pages during crop; skipping this page.")
                    continue
                page = self.page_images[pn]
                x0, y0, x1, y1 = int(left), 0, int(right), int(min(bottom, page.size[1]))
                if x0 > x1:
                    x0, x1 = x1, x0
                if y0 > y1:
                    y0, y1 = y1, y0
                x0 = max(0, min(x0, page.size[0]))
                x1 = max(0, min(x1, page.size[0]))
                y0 = max(0, min(y0, page.size[1]))
                y1 = max(0, min(y1, page.size[1]))
                if x1 <= x0 or y1 <= y0:
                    bottom -= page.size[1]
                    continue
                cimgp = page.crop((x0, y0, x1, y1))
                imgs.append(cimgp)
                if 0 < ii < len(poss) - 1:
                    positions.append((pn + self.page_from, x0, x1, y0, y1))
                bottom -= page.size[1]

        if not imgs:
            if need_position:
                return None, None
            return

        total_height = 0
        max_width = 0
        img_sizes = []
        for img in imgs:
            w, h = img.size
            img_sizes.append((w, h))
            max_width = max(max_width, w)
            total_height += h + GAP

        pic = Image.new("RGB", (max_width, int(total_height)), (245, 245, 245))
        current_height = 0
        imgs_count = len(imgs)
        for ii, (img, (w, h)) in enumerate(zip(imgs, img_sizes)):
            if ii == 0 or ii + 1 == imgs_count:
                img = img.convert("RGBA")
                overlay = Image.new("RGBA", img.size, (0, 0, 0, 128))
                img = Image.alpha_composite(img, overlay).convert("RGB")
            pic.paste(img, (0, int(current_height)))
            current_height += h + GAP

        if need_position:
            return pic, positions
        return pic


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = PaddleOCRParser(api_url=os.getenv("PADDLEOCR_API_URL", ""), algorithm=os.getenv("PADDLEOCR_ALGORITHM", "PaddleOCR-VL"))
    ok, reason = parser.check_installation()
    print("PaddleOCR available:", ok, reason)
