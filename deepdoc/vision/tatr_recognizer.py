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
#
"""TATR v1.1-All Table Structure Recognizer (DETR architecture).

Uses PyTorch inference (not ONNX).  Output format matches
``TableStructureRecognizer.__call__`` so the caller in
``paddleocr_parser.py`` can use either backend interchangeably.
"""

import logging
import os

import cv2
import numpy as np
import torch
from PIL import Image

from common.file_utils import get_project_base_directory


class TATRRecognizer:
    """Drop-in replacement for ``TableStructureRecognizer`` using the
    TATR v1.1-All (DETR-based) model with PyTorch inference.

    The ``__call__`` signature and return format are identical to
    ``TableStructureRecognizer.__call__``:

    .. code-block:: python

        results = recognizer([img_bgr_np], thr=0.2)
        # results: list[list[dict]]
        #   each dict: {"label", "score", "x0", "x1", "top", "bottom"}
    """

    labels = [
        "table",
        "table column",
        "table row",
        "table column header",
        "table projected row header",
        "table spanning cell",
    ]

    def __init__(self):
        from transformers import (
            DetrConfig,
            DetrImageProcessor,
            ResNetConfig,
            TableTransformerForObjectDetection,
        )

        model_dir = os.path.join(
            get_project_base_directory(), "rag/res/deepdoc"
        )
        weights_path = os.path.join(model_dir, "tatr-v1.1-all.pth")

        if not os.path.exists(weights_path):
            raise FileNotFoundError(
                f"TATR weights not found at {weights_path}. "
                "Download from: https://huggingface.co/bsmock/TATR-v1.1-All/"
                "resolve/main/TATR-v1.1-All-msft.pth"
            )

        # ---- Build config manually to avoid huggingface-hub strict
        #      validation crash (dilation=null in upstream config). ----
        backbone_config = ResNetConfig(
            depths=[3, 4, 6, 3],
            hidden_sizes=[256, 512, 1024, 2048],
            layer_type="bottleneck",
            num_channels=3,
            out_features=["stage2", "stage3", "stage4"],
            out_indices=[2, 3, 4],
            embedding_size=64,
            downsample_in_bottleneck=True,
            dilation=False,
        )
        config = DetrConfig(
            backbone_config=backbone_config,
            num_labels=6,
            num_queries=100,
        )

        # ---- Build model & load local weights ----
        self.model = TableTransformerForObjectDetection(config)
        state_dict = torch.load(weights_path, map_location="cpu")
        self.model.load_state_dict(state_dict, strict=False)
        self.model.eval()

        self.device = torch.device("cpu")
        self.model.to(self.device)

        # ---- Image processor ----
        try:
            self.processor = DetrImageProcessor.from_pretrained(
                "microsoft/table-transformer-structure-recognition-v1.1-all"
            )
            # Newer transformers require both shortest_edge + longest_edge
            # with non-None values; upstream config may only set longest_edge.
            sz = getattr(self.processor, "size", None) or {}
            if not sz.get("shortest_edge") and not sz.get("height"):
                self.processor.size = {
                    "shortest_edge": 800,
                    "longest_edge": 1333,
                }
        except Exception:
            self.processor = DetrImageProcessor(
                size={"shortest_edge": 800, "longest_edge": 1333},
                do_normalize=True,
                image_mean=[0.485, 0.456, 0.406],
                image_std=[0.229, 0.224, 0.225],
            )

        logging.info(
            "[TSR-TATR] TATR v1.1-All model loaded from %s", weights_path
        )

    # ------------------------------------------------------------------
    # Internal: run DETR on a single image → raw detection list
    # ------------------------------------------------------------------
    def _detect(self, img_bgr: np.ndarray, thr: float):
        """Return list of ``{"type", "bbox", "score"}`` dicts — same
        intermediate format that ``Recognizer.postprocess`` produces so
        the alignment post-processing can be shared verbatim.
        """
        h, w = img_bgr.shape[:2]
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)

        inputs = self.processor(images=pil_img, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model(**inputs)

        # outputs.logits: [1, 125, 7]  outputs.pred_boxes: [1, 125, 4]
        logits = outputs.logits[0]       # [125, 7]
        pred_boxes = outputs.pred_boxes[0]  # [125, 4] cxcywh normalised

        probs = torch.softmax(logits, dim=-1)
        # Exclude "no object" class (index 6)
        max_probs, class_ids = probs[:, :-1].max(dim=-1)

        detections: list[dict] = []
        for idx in range(len(max_probs)):
            score = max_probs[idx].item()
            if score < thr:
                continue
            cid = class_ids[idx].item()
            if cid >= len(self.labels):
                continue

            cx, cy, bw, bh = pred_boxes[idx].tolist()
            x0 = max(0.0, min(float(w), (cx - bw / 2) * w))
            y0 = max(0.0, min(float(h), (cy - bh / 2) * h))
            x1 = max(0.0, min(float(w), (cx + bw / 2) * w))
            y1 = max(0.0, min(float(h), (cy + bh / 2) * h))

            detections.append(
                {
                    "type": self.labels[cid],
                    "bbox": [x0, y0, x1, y1],
                    "score": score,
                }
            )

        return detections

    # ------------------------------------------------------------------
    # Public interface — matches TableStructureRecognizer.__call__
    # ------------------------------------------------------------------
    def __call__(self, images, thr=0.2):
        """Run TATR inference on a list of images.

        Args:
            images: list of numpy arrays (BGR, HWC) or PIL images.
            thr: confidence threshold.

        Returns:
            ``list[list[dict]]`` — each inner dict has keys
            ``label``, ``score``, ``x0``, ``x1``, ``top``, ``bottom``.
            Format is identical to ``TableStructureRecognizer.__call__``.
        """
        # --- Phase 1: raw detections (same format as Recognizer output) ---
        tbls: list[list[dict]] = []
        for img in images:
            if not isinstance(img, np.ndarray):
                img = np.array(img)
            tbls.append(self._detect(img, thr))

        # --- Phase 2: post-processing (copied from TableStructureRecognizer)
        #     Transform {"type","bbox","score"} → {"label","score","x0","x1","top","bottom"}
        #     then align row left/right, column top/bottom.
        res: list[list[dict]] = []
        for tbl in tbls:
            lts = [
                {
                    "label": b["type"],
                    "score": b["score"],
                    "x0": b["bbox"][0],
                    "x1": b["bbox"][2],
                    "top": b["bbox"][1],
                    "bottom": b["bbox"][-1],
                }
                for b in tbl
            ]
            if not lts:
                continue

            # Align left & right for rows / headers
            left = [
                b["x0"]
                for b in lts
                if b["label"].find("row") > 0
                or b["label"].find("header") > 0
            ]
            right = [
                b["x1"]
                for b in lts
                if b["label"].find("row") > 0
                or b["label"].find("header") > 0
            ]
            if not left:
                continue
            left = np.mean(left) if len(left) > 4 else np.min(left)
            right = np.mean(right) if len(right) > 4 else np.max(right)
            for b in lts:
                if (
                    b["label"].find("row") > 0
                    or b["label"].find("header") > 0
                ):
                    if b["x0"] > left:
                        b["x0"] = left
                    if b["x1"] < right:
                        b["x1"] = right

            # Align top & bottom for columns
            top = [
                b["top"] for b in lts if b["label"] == "table column"
            ]
            bottom = [
                b["bottom"] for b in lts if b["label"] == "table column"
            ]
            if not top:
                res.append(lts)
                continue
            top = np.median(top) if len(top) > 4 else np.min(top)
            bottom = (
                np.median(bottom) if len(bottom) > 4 else np.max(bottom)
            )
            for b in lts:
                if b["label"] == "table column":
                    if b["top"] > top:
                        b["top"] = top
                    if b["bottom"] < bottom:
                        b["bottom"] = bottom

            res.append(lts)

        return res

    def close(self):
        """Release model resources."""
        if hasattr(self, "model"):
            del self.model
        logging.info("[TSR-TATR] TATR model released")
