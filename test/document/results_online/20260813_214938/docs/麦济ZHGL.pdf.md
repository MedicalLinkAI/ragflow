# 线上统计：麦济ZHGL.pdf

## 基本信息

- 文件：`麦济ZHGL.pdf`
- 大小：4723.3 KB
- PDF 总页数：6
- doc_id：`daac0b0e96e411f19d3ab1cda0a97c3d`
- 处理方式：existing+reparse
- 状态：run=DONE  progress=1.0
- chunk_count(status)：5  orm_synced：True
- 处理耗时(服务端)：123.073586s  脚本耗时：125.0s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 94c191c2 | 1 | 1-1 | 电子发票(普通发票) 发票号码：25152000000077385777 开票日 |
| 2 | 05fe4f96 | 1 | 2-2 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：51岁 诊疗号：001107274 |
| 3 | 399bc652 | 2 | 3-4 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：51岁 诊疗号：001107274 |
| 4 | 3db2eada | 1 | 5-5 | 欣源药业 NO:2026011900323 商品名称 单价 数量 小计 布地奈德 |
| 5 | 17970da5 | 1 | 6-6 | 内蒙古医科大学附属医院 门诊缴费凭证 诊疗号: 0011072747 姓名: 收 |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[1, 2, 3, 4, 5, 6]`
- 覆盖页数：6 / 6（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 2 | encounter_date, chief_complaint, diagnosis | - | **OK** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | - | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 3 | encounter_date, pharmacy, payment_total | - | **OK** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | - | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |
