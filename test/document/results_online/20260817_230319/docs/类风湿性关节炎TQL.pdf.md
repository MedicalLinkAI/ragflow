# 线上统计：类风湿性关节炎TQL.pdf

## 基本信息

- 文件：`类风湿性关节炎TQL.pdf`
- 大小：274.6 KB
- PDF 总页数：-
- doc_id：`60a35dfc7c5011f18d62dd81525255fa`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：3  orm_synced：True
- 处理耗时(服务端)：224.3419s  脚本耗时：228.9s
- 重解析前快照（无基线结果）：chunk_count=3 run=DONE clinical 类型记录数={'DischargeRecord': 1, 'LabReport': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | b05fd9c5 | 1 | 1-1 | TQL一男.44. 类风湿性关节炎 出院记录 蛋白:15.75mg/L↑;类风湿 |
| 2 | 3e72de75 | 1 | 3-3 | <table><tr><td>钾</td><td>K</td><td>3.90< |
| 3 | 219ab433 | 1 | 2-2 | <table><tr><td>白细胞总数</td><td>WBC</td><td |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：3
- 页码并集：`[1, 2, 3]`
- 覆盖页数：3 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| LabReport | 检验报告 | 2 | 2 | ✅ |

- 判定：✅ 全部类型匹配
