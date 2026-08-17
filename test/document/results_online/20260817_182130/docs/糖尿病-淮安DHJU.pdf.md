# 线上统计：糖尿病-淮安DHJU.pdf

## 基本信息

- 文件：`糖尿病-淮安DHJU.pdf`
- 大小：3200.7 KB
- PDF 总页数：-
- doc_id：`492688ba7a7b11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：2  orm_synced：True
- 处理耗时(服务端)：178.20908s  脚本耗时：181.2s
- 重解析前快照（无基线结果）：chunk_count=2 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'LabReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 0b7f297a | 1 | 1-1 | 五河县人民医院 门诊病历 姓名： 性别：男 年龄：64岁 门诊号：2501126 |
| 2 | ecdf3a53 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HbA1C</td> |

- chunks 总数：2
- 各 chunk 页数合计（含跨页重复）：2
- 页码并集：`[1, 2]`
- 覆盖页数：2 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 1 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
