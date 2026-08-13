# 线上统计：LZK 哮喘 广三(1).pdf

## 基本信息

- 文件：`LZK 哮喘 广三(1).pdf`
- 大小：5325.3 KB
- PDF 总页数：16
- doc_id：`749dd6e696d311f19d3ab1cda0a97c3d`
- 处理方式：upload_file+upload
- 状态：run=RUNNING  progress=0.10882353
- chunk_count(status)：0  orm_synced：False
- 处理耗时(服务端)：197.37886s  脚本耗时：2327.4s
- 备注：进度等待超时（未达终态）。 

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | e7400f8c | 4 | 1-4 | 病历编号： 性别：男 年龄：40岁 就诊科室：内科门诊（荔湾） 就诊时间：202 |
| 2 | dc893970 | 1 | 5-5 | 门(急)诊处方 就诊时间:2025-07-18 就诊科室:内科门诊 主诊医 姓名 |
| 3 | 9beed22e | 1 | 6-6 | 门(急)诊处方 就诊时间:2025-04-25 就诊科室:内科门诊 主诊 姓名  |
| 4 | 10ae4909 | 1 | 7-7 | 门(急)诊处方 就诊时间:2025-02-26 就诊科室:内科门诊 主诊 性别: |
| 5 | 5cd6667e | 1 | 8-8 | 门(急)诊处方 就诊时间:2025-01-24 就诊科室:内科门诊 主诊医 姓名 |
| 6 | 5000a239 | 1 | 9-9 | 门(急)诊处方 就诊时间:2025-01-03 就诊科室:内科门诊 主诊 性别: |
| 7 | 71fd1576 | 1 | 10-10 | 门(急)诊处方 就诊时间:2024-12-04 就诊科室:内科门诊 主诊 姓名  |
| 8 | 218b013c | 1 | 11-11 | 激发试验检查报告 姓名： 测试号： 门诊/住院号： 000 年龄： 出生日期：  |
| 9 | 60d7e952 | 1 | 12-12 | 检查日期：2021/1/21 检查时间：16:43 编号：16 广州医科大学附属 |
| 10 | 8895371e | 1 | 13-13 | 广州医科大学附属第三医院 处方笺 普通 诊疗卡 患者姓名 年龄：41岁 费别：南 |
| 11 | 8f1b5f0c | 2 | 14-15 | 广州医科大学附属第三医院 The Third Affiliated Hospit |
| 12 | 311fc15c | 1 | 16-16 | 广州医科大学附属第三医院 肺功能检查报告 地址：广州市多宝路63号    电话： |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：16
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- 覆盖页数：16 / 16（覆盖率 100.0%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 关键字段提取统计（基于 chunks extracted_data_tks）

| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |
|------|------|-----------|--------------|----------|------|
| OutpatientRecord | 门诊 | 7 | encounter_date, diagnosis | chief_complaint | **OK** |
| AdmissionRecord | 入院 | 0 | - | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | - | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | - | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | - | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 3 | exam_date, report_date, exam_name, body_part, department | - | **OK** |
| LabReport | 检验报告 | 0 | - | report_time, report_category, report_name | **-** |

- 未归类提取记录：2 条
