# 线上统计：麦济WRNA(2).pdf

## 基本信息

- 文件：`麦济WRNA(2).pdf`
- 大小：12723.2 KB
- PDF 总页数：9
- doc_id：`de1ebdfa96e311f19d3ab1cda0a97c3d`
- 处理方式：existing+reparse
- 状态：run=DONE  progress=1.0
- chunk_count(status)：9  orm_synced：True
- 处理耗时(服务端)：186.95569s  脚本耗时：192.1s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 71494245 | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：54岁 诊疗号：001030409 |
| 2 | d846c9f2 | 1 | 2-2 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：54岁 诊疗号：001030409 |
| 3 | f21d9d7f | 1 | 3-3 | 鹤春堂大药房 2026-01-21 17:23:52 收银员：张星 名称 单价  |
| 4 | 2183596d | 1 | 4-4 | 电子票预览 www.chinaebill.cn 内蒙古自治区医疗门诊收费票据（电 |
| 5 | 702983d0 | 2 | 5-6 | wwwwwwwwwwwwwwwwww.pdf 电子发票(普通发票) 国家税务总局 |
| 6 | 7ae06f2c | 1 | 6-6 | 内蒙古医科大学附属医院门诊病历 姓名 年龄:51岁 诊疗号:0010304094 |
| 7 | 01983a5c | 1 | 7-7 | 内蒙古自治区国际蒙医医院 门诊病历 门诊号：2602120916 姓 科室：呼吸 |
| 8 | 88b6e9fc | 1 | 8-8 | 医疗收费明细（电子） 所属电 15060125 所属电子票据号码:0127705 |
| 9 | 23bec5b4 | 1 | 9-9 | 鹤春堂大药房 2025-12-26 12:29:31 收银员：张星 名称 单价  |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：9 / 9（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 4 | encounter_date, chief_complaint, diagnosis | - | **OK** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | - | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 5 | encounter_date, pharmacy, payment_total | - | **OK** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | - | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |
