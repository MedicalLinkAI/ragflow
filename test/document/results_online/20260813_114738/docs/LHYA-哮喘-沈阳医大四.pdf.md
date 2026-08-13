# 线上统计：LHYA-哮喘-沈阳医大四.pdf

## 基本信息

- 文件：`LHYA-哮喘-沈阳医大四.pdf`
- 大小：4483.0 KB
- PDF 总页数：7
- doc_id：`a57842ea96d011f19d3ab1cda0a97c3d`
- 处理方式：upload_file+upload
- 状态：run=DONE  progress=1.0
- chunk_count(status)：7  orm_synced：True
- 处理耗时(服务端)：254.0303s  脚本耗时：260.8s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | a9592912 | 1 | 1-1 | 四平市中心人民医院 门诊诊断书 0003316 (患者保管) SPZXYy-JL |
| 2 | b09dc0c1 | 1 | 2-2 | 四平市中医医院 门诊病历 初诊 2025年11月26日 肾病糖尿病科 姓名 性别 |
| 3 | d1018e4e | 1 | 3-3 | 四平市中医医院 内二疗区 门诊病历 初诊 2025年12月31日 姓名 性别：女 |
| 4 | a6baea9e | 1 | 4-4 | 四平市中心人民医院 常规通气+舒张试验 姓名： 年龄：53岁 住院号：11163 |
| 5 | 079563e8 | 1 | 5-5 | 四平市中心人民医院 常规通气 姓名：李洪燕 性别：女 年龄：53岁 吸烟史： 住 |
| 6 | dad2f80e | 1 | 6-6 | 信康大药房--佳合分店 单号：250927207100156 日期：2025-0 |
| 7 | 102142f7 | 1 | 7-7 | 信康大药房--佳合分店 单号：251128207100163 日期：2025-1 |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6, 7]`
- 覆盖页数：7 / 7（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 3 | encounter_date, chief_complaint, diagnosis | - | **OK** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | - | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | encounter_date, pharmacy, payment_total | - | **OK** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | exam_date, report_date, exam_name, body_part | department | **OK** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |
