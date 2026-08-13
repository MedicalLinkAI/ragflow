# 线上统计：麦济ZHYH.pdf

## 基本信息

- 文件：`麦济ZHYH.pdf`
- 大小：10282.5 KB
- PDF 总页数：6
- doc_id：`3888b5ec96e511f19d3ab1cda0a97c3d`
- 处理方式：upload_file+upload
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：172.08763s  脚本耗时：178.3s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 8e18874f | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：62岁 诊疗号：001449878 |
| 2 | 8e2399c3 | 1 | 2-2 | 萱堂大药房 单号：2025111853212 日期：25/11/18 时间：13 |
| 3 | 1f1bd333 | 1 | 3-3 | 电子发票(普通发票) 国家税务总局 江苏省税务局 发票号码：2532200000 |
| 4 | a0af6609 | 2 | 4-5 | 电子发票(普通发票) 国家税务总局 江苏省税务局 发票号码：2532200000 |
| 5 | 32178215 | 1 | 5-5 | 报告 闭环管理 治疗 健康调阅 三诺血糖 华益血糖 门诊记录: 病历信息 □痕迹 |
| 6 | e1a3903a | 1 | 6-6 | 电子发票(普通发票) 国家税务总局 内蒙古自治区税务局 发票号码：2615200 |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：7
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
| MedicationRecord | 购药 | 4 | encounter_date, pharmacy, payment_total | - | **OK** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | - | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |
