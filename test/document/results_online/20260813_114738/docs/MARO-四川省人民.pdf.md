# 线上统计：MARO-四川省人民.pdf

## 基本信息

- 文件：`MARO-四川省人民.pdf`
- 大小：6032.8 KB
- PDF 总页数：14
- doc_id：`006bbade96da11f19d3ab1cda0a97c3d`
- 处理方式：upload_file+upload
- 状态：run=DONE  progress=1.0
- chunk_count(status)：10  orm_synced：True
- 处理耗时(服务端)：517.19684s  脚本耗时：524.3s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | e5a2756a | 1 | 1-1 | 门诊 就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁 闭 |
| 2 | 0d4c1792 | 1 | 2-2 | 就诊类型: 门诊 就诊时间: 2026-02-24 21:35:00 接诊年龄: |
| 3 | b94d7e92 | 1 | 3-3 | 四川省医学科学院四川省人民医院 互联网门诊病历 姓名: 性别:女 年龄:62 门 |
| 4 | 8e4fd73c | 1 | 4-4 | 就诊类型: 门诊 就诊时间: 2026-01-23 13:19:40 接诊年龄: |
| 5 | 925eefd4 | 1 | 5-5 | 四川省医学科学院四川省人民医院 互联网门诊病历 姓名 性别：女 年龄：62 门诊 |
| 6 | f689d0c6 | 1 | 6-6 | 流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29  |
| 7 | 94a9e865 | 1 | 9-9 | 就诊类型：门诊 就诊时间：2025-12-09 17:00:36 接诊年龄：62 |
| 8 | fb25eea8 | 1 | 10-10 | 就诊类型: 门诊 就诊时间: 2025-09-02 13:50:11 接诊年龄: |
| 9 | 34269344 | 4 | 11-14 | 四川省医学科学院·四川省人民医院 门诊病历 姓名： 性别：女 年龄：60岁 门诊 |
| 10 | 1bda8e83 | 2 | 7-8 | <table><tr><td>白细胞计数</td><td>WBC</td><td |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：14
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / 14（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 6 | encounter_date, chief_complaint, diagnosis | - | **OK** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | - | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | - | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 3 | encounter_date, prescriber, diagnosis | - | **OK** |
| ExaminationReport | 检查报告 | 0 | - | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 1 | - | report_time, report_category, report_name | **OK** |
