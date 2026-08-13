# 线上统计：LXQI222.pdf

## 基本信息

- 文件：`LXQI222.pdf`
- 大小：62937.7 KB
- PDF 总页数：10
- doc_id：`a4816fe696d111f19d3ab1cda0a97c3d`
- 处理方式：upload_file+upload
- 状态：run=DONE  progress=1.0
- chunk_count(status)：5  orm_synced：False
- 处理耗时(服务端)：483.03113s  脚本耗时：492.5s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 4c14d858 | 4 | 1-4 | 入院记录 姓名： 床号：23-03床 病历号：0 科室：呼吸与危重医学科医生 站 |
| 2 | feddb89d | 3 | 5-7 | 出院记录 姓名： 床号：23-03床 病历号：0 科室：呼吸与危重医学科医生站  |
| 3 | 96b7ff2f | 1 | 8-8 | 肺功能通气阻力检查报告 姓名： 性别：女 身高：151 cm 病历号： 年龄：7 |
| 4 | 791e3463 | 1 | 9-9 | 对比试验 姓名： 性别：女 身高：151 cm 病历号： 年龄：72 Years |
| 5 | 2f0f6f6b | 1 | 10-10 | 亦康互联网医院 普通 处方 已使用 已使用 已使用 处方笺 NO.: 2025- |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- 覆盖页数：10 / 10（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 0 | - | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 1 | encounter_date, dm_admission_time, cc_text, department | - | **OK** |
| DischargeRecord | 出院 | 1 | admission_date, discharge_date, department, outcome | - | **OK** |
| MedicationRecord | 购药 | 0 | - | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 1 | encounter_date, prescriber, diagnosis | - | **OK** |
| ExaminationReport | 检查报告 | 2 | exam_date, report_date, exam_name, body_part | department | **OK** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |
