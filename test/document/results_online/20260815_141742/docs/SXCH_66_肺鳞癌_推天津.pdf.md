# 线上统计：SXCH 66 肺鳞癌 推天津.pdf

## 基本信息

- 文件：`SXCH 66 肺鳞癌 推天津.pdf`
- 大小：11966.1 KB
- PDF 总页数：-
- doc_id：`f223409c7b8f11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：7  orm_synced：True
- 处理耗时(服务端)：477.37698s  脚本耗时：480.3s
- 重解析前快照（无基线结果）：chunk_count=7 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'LabReport': 2, 'ExaminationReport': 3, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | ff9d1514 | 1 | 1-1 | 病理补充报告单 性别：女 年龄：66岁 病理号： 送检医院：总院 送检科室： 送 |
| 2 | 25af3309 | 2 | 2-3 | 入院时间：2025-11-26 12:25 出院时间：2025-12-05 10 |
| 3 | e970ae0d | 2 | 4-5 | 性别：女 职业：农民 年龄：66岁 出生地：河北省保定市 民族：汉族 入院时间： |
| 4 | 2b283554 | 1 | 6-6 | 检查名称： 颅脑,胸部 平扫,平扫+增强扫描 检查技术： 检查所见： 双侧侧脑室 |
| 5 | 96cf466c | 2 | 7-8 | PET/CT报告单 姓 别：女 年龄：66岁 床号： 送诊科室 送诊医生 住院号 |
| 6 | 76d0720c | 1 | 9-9 | <table><tr><td>白细胞</td><td>WBC</td><td>5 |
| 7 | d1ac69ab | 1 | 10-10 | <table><tr><td>甘油三酯</td><td>TG</td><td>1 |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- 覆盖页数：10 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 0 | ❌ |
| DischargeRecord | 出院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 3 | 0 | ❌ |
| LabReport | 检验报告 | 2 | 0 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, DischargeRecord, ExaminationReport, LabReport
