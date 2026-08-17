# 线上统计：xypp-吉大一 .pdf

## 基本信息

- 文件：`xypp-吉大一 .pdf`
- 大小：1353.1 KB
- PDF 总页数：-
- doc_id：`7132fab8858f11f1bb8027103a248952`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：3  orm_synced：True
- 处理耗时(服务端)：70.625s  脚本耗时：74.2s
- 重解析前快照（无基线结果）：chunk_count=3 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'MedicationRecord': 1, 'LabReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 8dc5bd74 | 3 | 1-3 | 联勤保障部队第九六四医院 中国人民解放军 第九六四医院 中国人民解放军 第九六四 |
| 2 | 9a276c58 | 1 | 4-4 | 益诚大药房 单号:2023090125002651 日期:2023-09-01  |
| 3 | e9a72f44 | 1 | 5-5 | <table><tr><td>ESR</td><td>None</td><td> |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：5
- 页码并集：`[1, 2, 3, 4, 5]`
- 覆盖页数：5 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 1 | ✅ |
| MedicationRecord | 购药 | 1 | 1 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
