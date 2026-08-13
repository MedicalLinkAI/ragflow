# 线上统计：麦济WZWA222.pdf

## 基本信息

- 文件：`麦济WZWA222.pdf`
- 大小：9514.5 KB
- PDF 总页数：5
- doc_id：`6d7206c496e411f19d3ab1cda0a97c3d`
- 处理方式：upload_file+upload
- 状态：run=DONE  progress=1.0
- chunk_count(status)：5  orm_synced：True
- 处理耗时(服务端)：178.3023s  脚本耗时：183.4s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 41971893 | 1 | 1-1 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：70岁 诊疗号：002254289 |
| 2 | bf2484b8 | 2 | 2-3 | 丰镇市医院 诊断证明书 姓名： 年龄： 性别：男 病案号：10017815 印象 |
| 3 | 00dd2f6e | 2 | 3-4 | 肺常规通气检查报告 测试号：0022542899 姓名： 出生日期： 身高：16 |
| 4 | 4dc67932 | 1 | 4-4 | 舒张试验测试报告 测试号：0022542899 姓名： 出生日期： 身高：cm  |
| 5 | d106b75a | 1 | 5-5 | 东吉轩药店 日期: 2026.01.23 09: 23: 37 单号: 2026 |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5]`
- 覆盖页数：5 / 5（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 2 | encounter_date, chief_complaint, diagnosis | - | **OK** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | - | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 1 | encounter_date, pharmacy, payment_total | - | **OK** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | exam_date, report_date, exam_name, body_part | department | **OK** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |
