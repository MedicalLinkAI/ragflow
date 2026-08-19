# 线上统计：成都-哮喘Ⅱb-SCRO.pdf

## 基本信息

- 文件：`成都-哮喘Ⅱb-SCRO.pdf`
- 大小：1155.3 KB
- PDF 总页数：-
- doc_id：`664e29dc84af11f1af97e3985ba7f8da`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：2  orm_synced：True
- 处理耗时(服务端)：199.15932s  脚本耗时：202.6s
- 重解析前快照（无基线结果）：chunk_count=2 run=DONE clinical 类型记录数={'LabReport': 1, 'OutpatientRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 7f7bab44 | 3 | 1-3 | 0179405 科室: 呼吸与危重症医学科门诊 病历 x GCP门诊病历 民医院 |
| 2 | e1e5c77a | 1 | 4-4 | <table><tr><td>红细胞分布宽度</td><td>None</td> |

- chunks 总数：2
- 各 chunk 页数合计（含跨页重复）：4
- 页码并集：`[1, 2, 3, 4]`
- 覆盖页数：4 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 1 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
