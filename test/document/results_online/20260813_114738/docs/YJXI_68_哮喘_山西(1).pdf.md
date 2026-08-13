# 线上统计：YJXI 68 哮喘 山西(1).pdf

## 基本信息

- 文件：`YJXI 68 哮喘 山西(1).pdf`
- 大小：7775.6 KB
- PDF 总页数：11
- doc_id：`0c14c48e96df11f19d3ab1cda0a97c3d`
- 处理方式：upload_file+upload
- 状态：run=DONE  progress=1.0
- chunk_count(status)：10  orm_synced：True
- 处理耗时(服务端)：298.97382s  脚本耗时：302.5s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | da90f06b | 1 | 1-1 | 门诊电子病历（初诊） 姓名： 性别：女性 年龄：68岁 科室：呼吸与危重症医学门 |
| 2 | 4d9984a2 | 2 | 2-3 | 出院记录 姓名： 性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号： 住 |
| 3 | 04dfeef5 | 1 | 4-4 | CT检查报告单 检查 病人姓名 性别：女 年龄：66岁 申请科室：呼吸与危重症二 |
| 4 | 7efe97bc | 1 | 5-5 | 【处方】导引单 ID: 姓名: 年龄：68岁 性别：女 费别：普通患者 诊断：支 |
| 5 | 3a1ce0d8 | 1 | 6-6 | [G532]  心草招县西人乡连锁 店 交易日期：2025-10-31 11:4 |
| 6 | d192f65c | 1 | 7-7 | 山西省医疗门诊收费票据（电子） 山西省 财政部监制 票据号码：004008195 |
| 7 | 035611d7 | 1 | 8-8 | 山西省医疗门诊收费票据（电子） 山西省 财政部监制 票据代码： 交款人话一社会信 |
| 8 | 9b50c97e | 1 | 9-9 | 山西省医疗门诊收费票据（电子） 山西省 财政部监制 票据代码:1/ 交款人统一社 |
| 9 | 48dd2e25 | 1 | 10-10 | 山西省医疗门诊收费票据（电子） 山西省 财政部监制 票据代码:14060124  |
| 10 | 9d753c72 | 1 | 11-11 | <table><tr><td>白细胞计数</td><td>WBC</td><td |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：11
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`
- 覆盖页数：11 / 11（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 2 | encounter_date, chief_complaint, diagnosis | - | **OK** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | admission_date, discharge_date, department, outcome | - | **OK** |
| MedicationRecord | 购药 | 5 | encounter_date, pharmacy, payment_total | - | **OK** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 1 | exam_date, report_date, exam_name, body_part, department | - | **OK** |
| LabReport | 检验报告 | 1 | - | report_time, report_category, report_name | **OK** |
