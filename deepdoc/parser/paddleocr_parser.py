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

                # ── TEMP DEBUG: dump per-page VL block stats ──
                _labels = [b.get("block_label", "?") for b in parsing_res_list]
                _contents = [b.get("block_content", "") for b in parsing_res_list]
                _empty_ct = sum(1 for c in _contents if not c.strip())
                logging.info(
                    "[DIAG-VL-PAGE] page=%d total_blocks=%d empty=%d labels=%s",
                    page_idx + 1, len(parsing_res_list), _empty_ct, _labels,
                )
                for _bi, _b in enumerate(parsing_res_list):
                    _bc = _b.get("block_content", "")
                    _bl = _b.get("block_label", "?")
                    _bb = _b.get("block_bbox", [])
                    _snippet = _bc.strip()[:120].replace("\n", " ")
                    logging.info(
                        "[DIAG-VL-BLOCK] page=%d block=%d label=%s bbox=%s len=%d snippet='%s'",
                        page_idx + 1, _bi, _bl, _bb, len(_bc), _snippet,
                    )
                # ── END TEMP DEBUG ──

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

        # 延迟初始化 TSR（不用不加载模型）— 多模型路由
        if PaddleOCRParser._tsr_instance is None:
            tsr_model = os.getenv("TSR_MODEL", "yolov8").lower()
            if tsr_model == "yolov8":
                # 原始行为：暴力 stretch 640×640
                from deepdoc.vision import TableStructureRecognizer
                PaddleOCRParser._tsr_instance = TableStructureRecognizer()
            elif tsr_model in ("yolov11", "yolov26"):
                # letterbox 预处理（保持宽高比）
                from deepdoc.vision import TableStructureRecognizer4Letterbox
                model_name_map = {
                    "yolov11": "tsr-yolo11",
                    "yolov26": "tsr-yolo26",
                }
                model_name = model_name_map[tsr_model]
                PaddleOCRParser._tsr_instance = TableStructureRecognizer4Letterbox(model_name=model_name)
            elif tsr_model == "tatr":
                from deepdoc.vision.tatr_recognizer import TATRRecognizer
                PaddleOCRParser._tsr_instance = TATRRecognizer()
            else:
                raise ValueError(
                    f"Unknown TSR_MODEL: {tsr_model}. "
                    f"Valid: yolov8, yolov11, yolov26, tatr"
                )
            # 打印实际加载的模型
            if tsr_model in ("yolov11", "yolov26"):
                _model_dir = os.path.join(
                    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "rag", "res", "deepdoc",
                )
                actual_onnx = os.path.join(_model_dir, model_name_map[tsr_model] + ".onnx")
                onnx_exists = os.path.exists(actual_onnx)
                onnx_size = os.path.getsize(actual_onnx) if onnx_exists else 0
                logging.info(
                    "[TSR] Model loaded: TSR_MODEL=%s onnx=%s (exists=%s, size=%.1fMB)",
                    tsr_model, actual_onnx, onnx_exists, onnx_size / 1024 / 1024
                )
            elif tsr_model == "yolov8":
                logging.info("[TSR] Model loaded: TSR_MODEL=yolov8 (original TableStructureRecognizer)")
            else:
                logging.info("[TSR] Model loaded: TSR_MODEL=%s (non-ONNX)", tsr_model)

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

        # M5: 分离收集 — data row 与 column header 各自独立
        # 避免 column header 混入 row_boxes 导致 gap 虚高（如 gap=2 的根因）
        row_boxes = [
            b for b in tsr_results[0]
            if b["label"] == "table row"
        ]
        # header_boxes 收集所有表头类标签（column header + projected row header）
        # 用于 Level-1 语义重叠检测，帮助精确识别多余行
        header_boxes = [
            b for b in tsr_results[0]
            if b["label"] in ("table column header", "table projected row header")
        ]
        logging.info(
            "[TSR-ENHANCE] page=%d M5分离收集: row_boxes=%d, header_boxes=%d",
            page_idx + 1, len(row_boxes), len(header_boxes),
        )
        if not row_boxes:
            logging.info("[TSR-ENHANCE] No row boxes detected for page=%d", page_idx + 1)
            return None

        # 按 top 排序
        row_boxes.sort(key=lambda b: b["top"])
        if header_boxes:
            header_boxes.sort(key=lambda b: b["top"])

        # 去重：TSR 可能在同一位置检测出多个重叠的 table row
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

        # 匹配度检查：TSR 行数与 <tr> 行数差距
        gap = abs(len(row_boxes) - num_rows)
        if gap > 2:
            logging.info(
                "[TSR-ENHANCE] page=%d gap=%d > 2 → 进入四层递进 (TSR=%d vs TR=%d)",
                page_idx + 1, gap, len(row_boxes), num_rows,
            )
            # ── Layer 1: 高度过滤降 gap（复用 gap=2 已验证逻辑）──
            _l1_heights = [rb["bottom"] - rb["top"] for rb in row_boxes]
            _l1_sorted = sorted(_l1_heights)
            _l1_median = _l1_sorted[len(_l1_sorted) // 2] if _l1_sorted else 0
            _l1_resolved = False
            if _l1_median > 0:
                _l1_low = _l1_median * 0.7
                _l1_high = _l1_median * 1.8
                _l1_filtered = [
                    rb for rb, h in zip(row_boxes, _l1_heights)
                    if _l1_low <= h <= _l1_high
                ]
                _l1_new_gap = abs(len(_l1_filtered) - num_rows)
                _l1_removed = len(row_boxes) - len(_l1_filtered)
                logging.info(
                    "[TSR-ENHANCE] page=%d Layer-1: 高度过滤 %d→%d (removed=%d "
                    "median=%.1f low=%.1f high=%.1f) → new_gap=%d",
                    page_idx + 1, len(row_boxes), len(_l1_filtered),
                    _l1_removed, _l1_median, _l1_low, _l1_high, _l1_new_gap,
                )
                if _l1_new_gap <= 2:
                    # 过滤后 gap 降到 ≤2，用过滤后的 row_boxes 继续走正常路径
                    row_boxes = sorted(_l1_filtered, key=lambda b: b["top"])
                    gap = _l1_new_gap
                    _l1_resolved = True
                    logging.info(
                        "[TSR-ENHANCE] page=%d Layer-1 成功: gap降至%d → 走正常路径",
                        page_idx + 1, gap,
                    )

            # ── Layer 2: PP-LCNet 旋转检测门 ──
            if not _l1_resolved:
                _l2_resolved = False
                try:
                    from deepdoc.vision.doc_orientation_classifier import (
                        DocOrientationClassifier,
                        ORIENTATION_MARGIN_THRESHOLD,
                    )
                    _clf = DocOrientationClassifier.get_instance()
                    _l2_angle, _l2_margin = _clf.detect(table_crop)
                    logging.info(
                        "[TSR-ENHANCE] page=%d Layer-2: PP-LCNet detect → "
                        "angle=%d° margin=%.4f (threshold=%.2f)",
                        page_idx + 1, _l2_angle, _l2_margin,
                        ORIENTATION_MARGIN_THRESHOLD,
                    )
                    if _l2_angle != 0 and _l2_margin >= ORIENTATION_MARGIN_THRESHOLD:
                        # 确认旋转 → 旋转裁剪图重跑 TSR
                        from PIL import Image as _PILImage
                        _rotated_crop = table_crop.rotate(
                            -_l2_angle, expand=True
                        )
                        _rot_np = np.array(_rotated_crop)
                        _rot_results = tsr([_rot_np], thr=0.2)
                        if _rot_results and _rot_results[0]:
                            _rot_row_boxes = sorted(
                                [b for b in _rot_results[0]
                                 if b["label"] == "table row"],
                                key=lambda b: b["top"],
                            )
                            _rot_gap = abs(len(_rot_row_boxes) - num_rows)
                            logging.info(
                                "[TSR-ENHANCE] page=%d Layer-2: 旋转%d° 重跑TSR → "
                                "new_rows=%d new_gap=%d",
                                page_idx + 1, _l2_angle,
                                len(_rot_row_boxes), _rot_gap,
                            )
                            if _rot_gap <= 2 and _rot_row_boxes:
                                # 旋转后 gap 合理 → 坐标反向映射
                                _rot_w, _rot_h = _rotated_crop.size
                                _orig_w = crop_right - crop_left
                                _orig_h = crop_bottom - crop_top

                                def _reverse_map_rb(rb, angle, rot_w, rot_h,
                                                     orig_w, orig_h):
                                    """Map TSR coords from rotated space back to original."""
                                    x0, top_r, x1, bot_r = (
                                        rb["x0"], rb["top"],
                                        rb["x1"], rb["bottom"],
                                    )
                                    if angle == 90:
                                        # 90° CW: (x',y') → (rot_w-y', x')
                                        # but we need bbox corners, not points
                                        new_x0 = top_r
                                        new_x1 = bot_r
                                        new_top = rot_w - x1
                                        new_bot = rot_w - x0
                                    elif angle == 180:
                                        new_x0 = rot_w - x1
                                        new_x1 = rot_w - x0
                                        new_top = rot_h - bot_r
                                        new_bot = rot_h - top_r
                                    elif angle == 270:
                                        new_x0 = rot_h - bot_r
                                        new_x1 = rot_h - top_r
                                        new_top = x0
                                        new_bot = x1
                                    else:
                                        new_x0, new_x1 = x0, x1
                                        new_top, new_bot = top_r, bot_r
                                    return {
                                        "x0": new_x0, "x1": new_x1,
                                        "top": new_top, "bottom": new_bot,
                                    }

                                _mapped_boxes = [
                                    _reverse_map_rb(
                                        rb, _l2_angle, _rot_w, _rot_h,
                                        _orig_w, _orig_h,
                                    )
                                    for rb in _rot_row_boxes
                                ]
                                _mapped_boxes.sort(key=lambda b: b["top"])
                                row_boxes = _mapped_boxes
                                gap = _rot_gap
                                _l2_resolved = True
                                logging.info(
                                    "[TSR-ENHANCE] page=%d Layer-2 成功: "
                                    "旋转%d° + 坐标映射 → gap=%d → 走正常路径",
                                    page_idx + 1, _l2_angle, gap,
                                )
                        else:
                            logging.info(
                                "[TSR-ENHANCE] page=%d Layer-2: "
                                "旋转后 TSR 无结果 → 跳过",
                                page_idx + 1,
                            )
                except Exception:
                    logging.exception(
                        "[TSR-ENHANCE] page=%d Layer-2 异常 → 跳过",
                        page_idx + 1,
                    )
                    _l2_resolved = False

                # ── Layer 3: VL 欠检救济 ──
                if not _l2_resolved:
                    if num_rows <= 2 and len(row_boxes) >= 5:
                        logging.info(
                            "[TSR-ENHANCE] page=%d Layer-3: VL 欠检救济 "
                            "(num_rows=%d ≤ 2, TSR=%d ≥ 5) → 信任 TSR",
                            page_idx + 1, num_rows, len(row_boxes),
                        )
                        # 信任 TSR 行位置，直接映射所有 row_boxes
                        page_1based = page_idx + 1
                        row_positions = []
                        def _map_rb_l3(rb):
                            return [
                                page_1based,
                                int(crop_left + rb["x0"]),
                                int(crop_left + rb["x1"]),
                                int(crop_top + rb["top"]),
                                int(crop_top + rb["bottom"]),
                            ]
                        for rb in row_boxes:
                            row_positions.append(_map_rb_l3(rb))
                        logging.info(
                            "[TSR-ENHANCE] page=%d tsr_rows=%d tr_rows=%d "
                            "→ %d positions (Layer-3 VL欠检救济) "
                            "row[0]=%s row[-1]=%s",
                            page_idx + 1, len(row_boxes), num_rows,
                            len(row_positions),
                            row_positions[0], row_positions[-1],
                        )
                        return row_positions

                    # ── Layer 4: 放弃 → Uniform fallback ──
                    logging.info(
                        "[TSR-ENHANCE] page=%d Layer-4: 四层均未命中 "
                        "(TSR=%d TR=%d gap=%d) → 回退 uniform",
                        page_idx + 1, len(row_boxes), num_rows, gap,
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
            # TSR 多一行 → M3 三层降级: Level 1 语义 → Level 2 数值 → Level 3 智能丢行

            # ── Level 1: 语义优先 — 利用 header_boxes 精确定位重叠行 ──
            level1_used = False
            if header_boxes:
                best_drop_idx = -1
                best_overlap = 0.0
                for i, rb in enumerate(row_boxes):
                    for hb in header_boxes:
                        ov = min(rb["bottom"], hb["bottom"]) - max(rb["top"], hb["top"])
                        if ov > best_overlap:
                            best_overlap = ov
                            best_drop_idx = i

                if best_drop_idx >= 0 and best_overlap > 0:
                    level1_rows = [rb for j, rb in enumerate(row_boxes) if j != best_drop_idx]
                    level1_used = True
                    logging.info(
                        "[TSR-ENHANCE] page=%d Level-1 语义丢行: "
                        "best_drop_idx=%d best_overlap=%.1f → %d == %d 匹配",
                        page_1based, best_drop_idx, best_overlap,
                        len(level1_rows), num_rows,
                    )
                    for rb in level1_rows:
                        row_positions.append(_map_rb(rb))
                else:
                    logging.info(
                        "[TSR-ENHANCE] page=%d Level-1: header 与 row_boxes 无重叠 → 降级 Level-2",
                        page_1based,
                    )
            else:
                logging.info(
                    "[TSR-ENHANCE] page=%d Level-1: 无 header_boxes → 降级 Level-2",
                    page_1based,
                )

            # ── Level 2: 双向数值过滤 (仅在 Level 1 未命中时执行) ──
            if not level1_used:
                heights = [rb["bottom"] - rb["top"] for rb in row_boxes]
                sorted_h = sorted(heights)
                median_h = sorted_h[len(sorted_h) // 2]

                if median_h > 0:
                    threshold_low = median_h * 0.7
                    threshold_high = median_h * 1.8
                    filtered = [
                        rb for rb, h in zip(row_boxes, heights)
                        if threshold_low <= h <= threshold_high
                    ]
                else:
                    filtered = []

                if len(filtered) == num_rows:
                    removed_info = [
                        (i, round(heights[i], 1),
                         "too_small" if heights[i] < threshold_low else "too_large")
                        for i in range(len(heights))
                        if not (threshold_low <= heights[i] <= threshold_high)
                    ]
                    logging.info(
                        "[TSR-ENHANCE] page=%d Level-2 双向过滤: median_h=%.1f "
                        "low=%.1f high=%.1f filtered %d→%d (removed %s)",
                        page_1based, median_h, threshold_low, threshold_high,
                        len(row_boxes), len(filtered), removed_info,
                    )
                    for rb in filtered:
                        row_positions.append(_map_rb(rb))
                else:
                    # Level 3: 智能丢行 — 比较首尾与中位数偏差，丢偏差大的
                    first_dev = abs(heights[0] - median_h)
                    last_dev = abs(heights[-1] - median_h)
                    if first_dev > last_dev:
                        smart_rows = row_boxes[1:]
                        drop_label = "first"
                    else:
                        smart_rows = row_boxes[:-1]
                        drop_label = "last"

                    logging.info(
                        "[TSR-ENHANCE] page=%d Level-3 智能丢行: drop_%s "
                        "(first_dev=%.1f last_dev=%.1f median_h=%.1f) %d→%d",
                        page_1based, drop_label,
                        first_dev, last_dev, median_h,
                        len(row_boxes), len(smart_rows),
                    )
                    for rb in smart_rows:
                        row_positions.append(_map_rb(rb))
        else:
            # ── gap ≤ 2 但不满足 exact/±1 (即 gap=2) ──
            # Step 0: 先尝试对 row_boxes 做双向高度过滤（复用 M3 Level-2 逻辑）
            # 如果能过滤到 exact/±1 范围就直接走已验证的映射路径
            _heights = [rb["bottom"] - rb["top"] for rb in row_boxes]
            _sorted_h = sorted(_heights)
            _median_h = _sorted_h[len(_sorted_h) // 2] if _sorted_h else 0

            _gap2_resolved = False
            if _median_h > 0:
                _thr_low = _median_h * 0.7
                _thr_high = _median_h * 1.8
                _filtered = [
                    rb for rb, h in zip(row_boxes, _heights)
                    if _thr_low <= h <= _thr_high
                ]
                _removed_info = [
                    (i, round(_heights[i], 1),
                     "too_small" if _heights[i] < _thr_low else "too_large")
                    for i in range(len(_heights))
                    if not (_thr_low <= _heights[i] <= _thr_high)
                ]

                if len(_filtered) == num_rows:
                    # 过滤后精确匹配 → 直接采用
                    logging.info(
                        "[TSR-ENHANCE] page=%d gap=%d 双向高度过滤: median_h=%.1f "
                        "low=%.1f high=%.1f filtered %d→%d (removed %s) → exact 匹配",
                        page_1based, gap, _median_h, _thr_low, _thr_high,
                        len(row_boxes), len(_filtered), _removed_info,
                    )
                    for rb in _filtered:
                        row_positions.append(_map_rb(rb))
                    _gap2_resolved = True
                elif len(_filtered) == num_rows - 1:
                    # 过滤后少 1 行 → 补表头
                    logging.info(
                        "[TSR-ENHANCE] page=%d gap=%d 双向高度过滤: median_h=%.1f "
                        "filtered %d→%d (removed %s) → num_rows-1 补表头",
                        page_1based, gap, _median_h,
                        len(row_boxes), len(_filtered), _removed_info,
                    )
                    _filtered.sort(key=lambda b: b["top"])
                    row_positions.append([
                        page_1based,
                        int(left // zm),
                        int(right // zm),
                        int(top // zm),
                        int(crop_top + _filtered[0]["top"]),
                    ])
                    for rb in _filtered:
                        row_positions.append(_map_rb(rb))
                    _gap2_resolved = True
                elif len(_filtered) == num_rows + 1:
                    # 过滤后多 1 行 → 复用 M3 Level-3 智能丢行
                    _filtered.sort(key=lambda b: b["top"])
                    _fh = [b["bottom"] - b["top"] for b in _filtered]
                    _fm = sorted(_fh)[len(_fh) // 2]
                    _fd_first = abs(_fh[0] - _fm)
                    _fd_last = abs(_fh[-1] - _fm)
                    if _fd_first > _fd_last:
                        _smart = _filtered[1:]
                        _dl = "first"
                    else:
                        _smart = _filtered[:-1]
                        _dl = "last"
                    logging.info(
                        "[TSR-ENHANCE] page=%d gap=%d 双向高度过滤: "
                        "filtered %d→%d then 智能丢行 drop_%s → %d == num_rows=%d",
                        page_1based, gap,
                        len(row_boxes), len(_filtered), _dl,
                        len(_smart), num_rows,
                    )
                    for rb in _smart:
                        row_positions.append(_map_rb(rb))
                    _gap2_resolved = True
                else:
                    logging.info(
                        "[TSR-ENHANCE] page=%d gap=%d 双向高度过滤: median_h=%.1f "
                        "filtered %d→%d (removed %s) → 仍不匹配 num_rows=%d, 降级 M5 secondary",
                        page_1based, gap, _median_h,
                        len(row_boxes), len(_filtered), _removed_info, num_rows,
                    )

            # Step 1: 高度过滤未解决 → 走 M5 secondary（合回 header_boxes）
            if not _gap2_resolved and header_boxes:
                all_boxes = sorted(
                    row_boxes + header_boxes, key=lambda b: b["top"]
                )
                # 合并后去重 — header 和 row 在同一位置重叠时只保留一个
                if len(all_boxes) > 1:
                    deduped_all = [all_boxes[0]]
                    for rb in all_boxes[1:]:
                        prev = deduped_all[-1]
                        overlap = min(prev["bottom"], rb["bottom"]) - max(prev["top"], rb["top"])
                        min_h = min(
                            prev["bottom"] - prev["top"],
                            rb["bottom"] - rb["top"],
                        )
                        if min_h > 0 and overlap / min_h > 0.5:
                            continue
                        deduped_all.append(rb)
                    all_boxes = deduped_all

                total = len(all_boxes)
                if total == num_rows:
                    logging.info(
                        "[TSR-ENHANCE] page=%d M5-secondary-exact: "
                        "row=%d + header=%d = %d == num_rows=%d → 直接映射",
                        page_1based, len(row_boxes), len(header_boxes),
                        total, num_rows,
                    )
                    for rb in all_boxes:
                        row_positions.append(_map_rb(rb))
                elif total == num_rows - 1:
                    logging.info(
                        "[TSR-ENHANCE] page=%d M5-secondary-prepend: "
                        "total=%d == num_rows-1=%d → 补表头",
                        page_1based, total, num_rows - 1,
                    )
                    row_positions.append([
                        page_1based,
                        int(left // zm),
                        int(right // zm),
                        int(top // zm),
                        int(crop_top + all_boxes[0]["top"]),
                    ])
                    for rb in all_boxes:
                        row_positions.append(_map_rb(rb))
                elif total == num_rows + 1:
                    heights = [b["bottom"] - b["top"] for b in all_boxes]
                    sorted_h = sorted(heights)
                    median_h = sorted_h[len(sorted_h) // 2]
                    first_dev = abs(heights[0] - median_h)
                    last_dev = abs(heights[-1] - median_h)
                    if first_dev > last_dev:
                        smart_rows = all_boxes[1:]
                        drop_label = "first"
                    else:
                        smart_rows = all_boxes[:-1]
                        drop_label = "last"
                    logging.info(
                        "[TSR-ENHANCE] page=%d M5-secondary-plus1: "
                        "total=%d → drop_%s",
                        page_1based, total, drop_label,
                    )
                    for rb in smart_rows:
                        row_positions.append(_map_rb(rb))
                else:
                    logging.info(
                        "[TSR-ENHANCE] page=%d M5-secondary-fail: "
                        "total=%d vs num_rows=%d → 回退 uniform",
                        page_1based, total, num_rows,
                    )
                    return None
            elif not _gap2_resolved:
                logging.info(
                    "[TSR-ENHANCE] page=%d gap=%d 无 header_boxes 且高度过滤未命中 → 回退 uniform",
                    page_1based, gap,
                )
                return None

        if not row_positions:
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
