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
"""
Letterbox-aware TSR 子类。

仅 paddleocr_parser.py 使用本子类。
通用 PDF 解析 (pdf_parser.py) 继续使用原始 TableStructureRecognizer，
避免 letterbox 改动影响非 PaddleOCR 业务场景。

设计模式参考: LayoutRecognizer4YOLOv10（同样是子类覆写 preprocess/postprocess）。
"""
import logging
from collections import Counter

import cv2
import numpy as np

from .table_structure_recognizer import TableStructureRecognizer


class TableStructureRecognizer4Letterbox(TableStructureRecognizer):
    """子类覆写 preprocess/postprocess，实现 letterbox resize + 坐标反映射。

    父类 Recognizer.preprocess() 使用 cv2.resize 直接拉伸到 640×640（暴力变形）。
    本子类改为保持宽高比缩放 + 灰色 (114) padding，消除几何畸变，
    提升 TSR 对非正方形表格图片的行检测精度。
    """

    def preprocess(self, image_list):
        """Letterbox preprocess: 保持宽高比缩放，pad 到 640×640，填充灰色 (114)。"""
        inputs = []
        hh, ww = self.input_shape  # (640, 640)
        for img in image_list:
            h, w = img.shape[:2]
            if h == 0 or w == 0:
                logging.warning("[TSR-LETTERBOX] preprocess: skip zero-dim image %dx%d", w, h)
                continue
            r = min(hh / h, ww / w)
            new_unpad = int(round(w * r)), int(round(h * r))
            dw = (ww - new_unpad[0]) / 2.0
            dh = (hh - new_unpad[1]) / 2.0

            logging.info(
                "[TSR-LETTERBOX] preprocess: orig=%dx%d ratio=%.4f "
                "resized=%dx%d pad=(%.1f,%.1f) target=%dx%d",
                w, h, r, new_unpad[0], new_unpad[1], dw, dh, ww, hh,
            )

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32)
            img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
            top_pad = int(round(dh - 0.1))
            bottom_pad = int(round(dh + 0.1))
            left_pad = int(round(dw - 0.1))
            right_pad = int(round(dw + 0.1))
            img = cv2.copyMakeBorder(
                img, top_pad, bottom_pad, left_pad, right_pad,
                cv2.BORDER_CONSTANT, value=(114, 114, 114),
            )
            img /= 255.0
            img = img.transpose(2, 0, 1)
            img = img[np.newaxis, :, :, :].astype(np.float32)
            # scale_factor 4 元素: [orig_w/resized_w, orig_h/resized_h, padding_x, padding_y]
            inputs.append({
                self.input_names[0]: img,
                "scale_factor": [w / new_unpad[0], h / new_unpad[1], dw, dh],
            })
        return inputs

    def postprocess(self, boxes, inputs, thr):
        """Letterbox-aware postprocess: 反向 padding → 还原原始坐标 → per-class NMS。"""

        def xywh2xyxy(x):
            y = np.copy(x)
            y[:, 0] = x[:, 0] - x[:, 2] / 2
            y[:, 1] = x[:, 1] - x[:, 3] / 2
            y[:, 2] = x[:, 0] + x[:, 2] / 2
            y[:, 3] = x[:, 1] + x[:, 3] / 2
            return y

        def compute_iou(box, boxes_arr):
            xmin = np.maximum(box[0], boxes_arr[:, 0])
            ymin = np.maximum(box[1], boxes_arr[:, 1])
            xmax = np.minimum(box[2], boxes_arr[:, 2])
            ymax = np.minimum(box[3], boxes_arr[:, 3])
            intersection_area = np.maximum(0, xmax - xmin) * np.maximum(0, ymax - ymin)
            box_area = (box[2] - box[0]) * (box[3] - box[1])
            boxes_area = (boxes_arr[:, 2] - boxes_arr[:, 0]) * (boxes_arr[:, 3] - boxes_arr[:, 1])
            union_area = box_area + boxes_area - intersection_area
            union_area = np.maximum(union_area, 1e-6)  # 防零面积 box 导致 NaN
            return intersection_area / union_area

        def iou_filter(boxes_arr, scores_arr, iou_threshold):
            sorted_indices = np.argsort(scores_arr)[::-1]
            keep_boxes = []
            while sorted_indices.size > 0:
                box_id = sorted_indices[0]
                keep_boxes.append(box_id)
                ious = compute_iou(boxes_arr[box_id, :], boxes_arr[sorted_indices[1:], :])
                keep_indices = np.where(ious < iou_threshold)[0]
                sorted_indices = sorted_indices[keep_indices + 1]
            return keep_boxes

        boxes = np.squeeze(boxes).T
        total_raw = boxes.shape[0]
        scores = np.max(boxes[:, 4:], axis=1)
        boxes = boxes[scores > thr, :]
        scores = scores[scores > thr]
        if len(boxes) == 0:
            logging.info(
                "[TSR-LETTERBOX] postprocess: raw=%d after_thr(%.2f)=0 → empty",
                total_raw, thr,
            )
            return []

        class_ids = np.argmax(boxes[:, 4:], axis=1)
        boxes = boxes[:, :4]  # cxcywh in letterboxed 640×640 space

        # 反向 letterbox: 从 cx/cy 减去 padding（w/h 不受 padding 影响）
        dw, dh = inputs["scale_factor"][2], inputs["scale_factor"][3]
        boxes[:, 0] -= dw  # cx
        boxes[:, 1] -= dh  # cy

        # 还原到原始图片坐标
        scale_x, scale_y = inputs["scale_factor"][0], inputs["scale_factor"][1]
        input_shape = np.array([scale_x, scale_y, scale_x, scale_y])
        boxes = np.multiply(boxes, input_shape, dtype=np.float32)

        # cxcywh → xyxy
        boxes = xywh2xyxy(boxes)

        # Per-class NMS (IoU=0.2)
        unique_class_ids = np.unique(class_ids)
        indices = []
        for class_id in unique_class_ids:
            class_indices = np.where(class_ids == class_id)[0]
            class_boxes = boxes[class_indices, :]
            class_scores = scores[class_indices]
            class_keep_boxes = iou_filter(class_boxes, class_scores, 0.2)
            indices.extend(class_indices[class_keep_boxes])

        # 过滤越界 class_id（防模型/label_list 版本不匹配导致 IndexError）
        indices = [i for i in indices if class_ids[i] < len(self.label_list)]

        label_counts = Counter(self.label_list[class_ids[i]] for i in indices)
        logging.info(
            "[TSR-LETTERBOX] postprocess: raw=%d after_thr(%.2f)=%d "
            "after_nms=%d labels=%s pad=(%.1f,%.1f) scale=(%.3f,%.3f)",
            total_raw, thr, len(scores), len(indices),
            dict(label_counts), dw, dh, scale_x, scale_y,
        )

        return [{
            "type": self.label_list[class_ids[i]].lower(),
            "bbox": [float(t) for t in boxes[i].tolist()],
            "score": float(scores[i]),
        } for i in indices]
