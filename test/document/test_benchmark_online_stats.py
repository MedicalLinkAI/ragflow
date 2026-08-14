# -*- coding: utf-8 -*-
"""benchmark_online.py 类型一致性统计的单元测试。

统计口径：
1. 从 status 接口 progress_msg 的 "SmartSplitter done: ... Types: {...}" 日志
   解析 chunk 类型个数；
2. 从 clinical 接口 encounters 各类型列表长度汇总落库记录个数；
3. 两边按类型比对是否匹配。
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import benchmark_online as bo

SAMPLE_MSG = (
    "\n21:49:41 Task has been received.\n"
    "-------------------------------------\n"
    "[SmartSplitter:MedLink]:\n"
    "22:05:09: SmartSplitter done: 45 chunks from 45 LLM segments (all bbox_id). "
    "Types: {'ExaminationReport': 5, 'AdmissionRecord': 1, 'ProgressNote': 7, "
    "'DischargeRecord': 1, 'OutpatientRecord': 14, 'PrescriptionRecord': 2, 'LabReport': 15}\n"
    "22:05:09: Done\n"
)


def test_parse_smart_splitter_types_extracts_counts():
    assert bo.parse_smart_splitter_types(SAMPLE_MSG) == {
        "ExaminationReport": 5,
        "AdmissionRecord": 1,
        "ProgressNote": 7,
        "DischargeRecord": 1,
        "OutpatientRecord": 14,
        "PrescriptionRecord": 2,
        "LabReport": 15,
    }


def test_parse_smart_splitter_types_no_line_returns_empty():
    assert bo.parse_smart_splitter_types("21:49:42: File fetched.\nDone") == {}
    assert bo.parse_smart_splitter_types(None) == {}


def test_parse_smart_splitter_types_takes_last_line():
    msg = (
        "SmartSplitter done: 4 chunks from 4 LLM segments (all bbox_id). "
        "Types: {'AdmissionRecord': 1}\n"
        "SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). "
        "Types: {'AdmissionRecord': 2, 'LabReport': 4}\n"
    )
    assert bo.parse_smart_splitter_types(msg) == {"AdmissionRecord": 2, "LabReport": 4}


def test_count_clinical_types_sums_across_encounters():
    encounters = [
        {"admission_records": [{}], "prescriptions": [{}, {}], "outpatients": []},
        {"lab_reports": [{}, {}, {}], "prescriptions": [{}], "medications": [{}]},
    ]
    assert bo.count_clinical_types(encounters) == {
        "AdmissionRecord": 1,
        "PrescriptionRecord": 3,
        "LabReport": 3,
        "MedicationRecord": 1,
    }


def test_count_clinical_types_empty():
    assert bo.count_clinical_types([]) == {}
    assert bo.count_clinical_types(None) == {}


def test_compare_type_counts_match_and_mismatch():
    splitter = {"OutpatientRecord": 2, "LabReport": 1, "PrescriptionRecord": 4}
    clinical = {"OutpatientRecord": 2, "LabReport": 2, "MedicationRecord": 3}
    cmp = bo.compare_type_counts(splitter, clinical)
    assert cmp["OutpatientRecord"] == {"splitter": 2, "clinical": 2, "match": True}
    assert cmp["LabReport"] == {"splitter": 1, "clinical": 2, "match": False}
    # 仅一侧出现的类型也要列出（另一侧按 0 计）
    assert cmp["PrescriptionRecord"] == {"splitter": 4, "clinical": 0, "match": False}
    assert cmp["MedicationRecord"] == {"splitter": 0, "clinical": 3, "match": False}


def test_compare_type_counts_both_empty():
    assert bo.compare_type_counts({}, {}) == {}
