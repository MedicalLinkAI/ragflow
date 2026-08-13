# 线上统计：lzga-哮喘-沈阳(1).pdf

## 基本信息

- 文件：`lzga-哮喘-沈阳(1).pdf`
- 大小：5899.8 KB
- PDF 总页数：5
- doc_id：`c6c7d30096d211f19d3ab1cda0a97c3d`
- 处理方式：upload_file+upload
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：287.64072s  脚本耗时：291.5s

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 53585388 | 1 | 1-1 | 信4个月 医疗机构：凤城市中医院 (组织机构代码：46376203-6) 中医住 |
| 2 | ba8a2c62 | 1 | 2-2 | 凤城诚岳中医院 门诊 病 历 诊断专用章 编号：54474 姓名： 性别：男 年 |
| 3 | 1c302d4c | 1 | 3-3 | 凤城诚岳中医院 诊断专用笺 病 历 编号：104474 姓名： 性别： 男 年龄 |
| 4 | 198835c7 | 1 | 4-4 | 欢迎光临健康大药房凤鸣分店 日期：2026-02-08 09:50:51 单号： |
| 5 | 01616ac4 | 1 | 5-5 | 医疗保险定点药店收费明细 辽宁天士力大药房连锁有限公司 药店名称： 凤城石桥路店 |
| 6 | 490f9341 | 1 | 5-5 | 医疗保险定点药店收费明细 辽宁天士力大药房连锁有限公司 药店名称： 凤城石桥路店 |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[1, 2, 3, 4, 5]`
- 覆盖页数：5 / 5（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 2 | encounter_date, chief_complaint, diagnosis | - | **OK** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | admission_date, discharge_date, department | outcome | **OK** |
| MedicationRecord | 购药 | 3 | encounter_date, pharmacy, payment_total | - | **OK** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | - | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |
