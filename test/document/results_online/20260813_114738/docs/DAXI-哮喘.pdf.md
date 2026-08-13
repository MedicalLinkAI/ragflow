# 线上统计：DAXI-哮喘.pdf

## 基本信息

- 文件：`DAXI-哮喘.pdf`
- 大小：24796.9 KB
- PDF 总页数：52
- doc_id：`d071b5d0953111f18f67cb8e99b562ad`
- 处理方式：existing+reparse
- 状态：run=RUNNING  progress=0.7082353
- chunk_count(status)：0  orm_synced：True
- 处理耗时(服务端)：1795.6143s  脚本耗时：1855.6s
- 备注：进度等待超时（未达终态）。 

## 1. 页面覆盖率

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 0 | - | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | - | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | - | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | - | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |
