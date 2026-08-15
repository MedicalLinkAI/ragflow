# 线上统计：LYLN.pdf

## 基本信息

- 文件：`LYLN.pdf`
- 大小：1147.2 KB
- PDF 总页数：-
- doc_id：`856d5b6c75b911f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：4  orm_synced：True
- 处理耗时(服务端)：50.2406s  脚本耗时：52.6s
- 重解析前快照（无基线结果）：chunk_count=4 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'LabReport': 2, 'MedicationRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | c0c469f7 | 1 | 1-1 | 长春新 院 门诊病历 门诊号：1 姓名： 性别：女 年龄：40岁 科 别： 内科 |
| 2 | 162a42d1 | 1 | 4-4 | 元康大药房 时间：2026-01-12 13:09:18 单号：10020260 |
| 3 | 5b432275 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 4 | 39b5c0ef | 1 | 3-3 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |

- chunks 总数：4
- 各 chunk 页数合计（含跨页重复）：4
- 页码并集：`[1, 2, 3, 4]`
- 覆盖页数：4 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 2 | 0 | ❌ |
| MedicationRecord | 购药 | 1 | 0 | ❌ |
| OutpatientRecord | 门诊 | 1 | 0 | ❌ |

- 判定：❌ 不匹配类型: LabReport, MedicationRecord, OutpatientRecord
