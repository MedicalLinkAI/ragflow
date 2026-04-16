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
"""Document orientation classifier using PP-LCNet ONNX model.

Detects page/table orientation (0°, 90°, 180°, 270°) from an image.
Used as a rotation gate in TSR gap>2 processing — only invoked when
TSR row count deviates significantly from VL row count.

Model: PP-LCNet_x1_0_doc_ori (PaddlePaddle official, 6.5MB ONNX)
"""
import logging
import os
import threading

import numpy as np

from common.file_utils import get_project_base_directory

ORIENTATION_MARGIN_THRESHOLD = 0.10
ORIENTATION_CLASSES = [0, 90, 180, 270]

_MODEL_FILENAME = "PP-LCNet_x1_0_doc_ori.onnx"

_instance_lock = threading.Lock()
_instance = None


def _softmax(logits: np.ndarray) -> np.ndarray:
    """Numerically stable softmax."""
    x = logits - np.max(logits)
    e = np.exp(x)
    return e / e.sum()


class DocOrientationClassifier:
    """Singleton classifier for document orientation detection.

    Usage::

        clf = DocOrientationClassifier.get_instance()
        angle, margin = clf.detect(pil_image)
        # angle: 0, 90, 180, or 270
        # margin: confidence gap between best and second-best class
    """

    def __init__(self, model_dir: str | None = None):
        if model_dir is None:
            model_dir = os.path.join(
                get_project_base_directory(), "rag", "res", "deepdoc"
            )
        model_path = os.path.join(model_dir, _MODEL_FILENAME)
        if not os.path.exists(model_path):
            logging.warning(
                "[DocOrientation] Model not found: %s — orientation detection disabled",
                model_path,
            )
            self._session = None
            return

        try:
            import onnxruntime as ort

            sess_opts = ort.SessionOptions()
            sess_opts.graph_optimization_level = (
                ort.GraphOptimizationLevel.ORT_ENABLE_ALL
            )
            self._session = ort.InferenceSession(
                model_path, sess_options=sess_opts
            )
            self._input_name = self._session.get_inputs()[0].name
            logging.info(
                "[DocOrientation] Model loaded: %s (%.1fMB)",
                model_path,
                os.path.getsize(model_path) / 1024 / 1024,
            )
        except Exception:
            logging.exception("[DocOrientation] Failed to load ONNX model")
            self._session = None

    @classmethod
    def get_instance(cls) -> "DocOrientationClassifier":
        global _instance
        if _instance is None:
            with _instance_lock:
                if _instance is None:
                    _instance = cls()
        return _instance

    def detect(self, pil_image) -> tuple[int, float]:
        """Detect document orientation.

        Args:
            pil_image: PIL.Image.Image (RGB or other mode).

        Returns:
            (angle, margin) where angle is 0/90/180/270 and margin is
            the confidence gap between best and second-best prediction.
            Returns (0, 0.0) on any error (safe fallback — no rotation).
        """
        if self._session is None:
            return 0, 0.0

        try:
            tensor = self._preprocess(pil_image)
            logits = self._session.run(None, {self._input_name: tensor})[0]
            probs = _softmax(logits[0])

            sorted_idx = np.argsort(probs)[::-1]
            best_idx = sorted_idx[0]
            second_idx = sorted_idx[1]
            margin = float(probs[best_idx] - probs[second_idx])
            angle = ORIENTATION_CLASSES[best_idx]

            return angle, margin
        except Exception:
            logging.exception("[DocOrientation] Detection failed")
            return 0, 0.0

    @staticmethod
    def _preprocess(pil_image) -> np.ndarray:
        """PP-LCNet official preprocessing: ResizeShort(256) → CenterCrop(224) → Normalize."""
        from PIL import Image

        img = pil_image.convert("RGB")

        # ResizeShort: scale so shortest side = 256, keep aspect ratio
        w, h = img.size
        short = min(w, h)
        scale = 256.0 / short
        new_w, new_h = int(w * scale + 0.5), int(h * scale + 0.5)
        img = img.resize((new_w, new_h), Image.BILINEAR)

        # CenterCrop 224×224
        cw, ch = img.size
        left = (cw - 224) // 2
        top = (ch - 224) // 2
        img = img.crop((left, top, left + 224, top + 224))

        # Normalize: ImageNet mean/std
        arr = np.array(img, dtype=np.float32) / 255.0
        mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
        std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
        arr = (arr - mean) / std

        # HWC → NCHW
        arr = arr.transpose(2, 0, 1)[np.newaxis, ...]
        return arr.astype(np.float32)
