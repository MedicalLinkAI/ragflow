# 线上统计：糖尿病-THXI-北京.pdf

## 基本信息

- 文件：`糖尿病-THXI-北京.pdf`
- 大小：1162.9 KB
- PDF 总页数：-
- doc_id：`3c9e14c27c3e11f18d62dd81525255fa`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：3  orm_synced：True
- 处理耗时(服务端)：96.857376s  脚本耗时：99.0s
- 重解析前快照（无基线结果）：chunk_count=3 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'LabReport': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 6c72a033 | 1 | 2-2 | 丰台街道东大街社区卫生服务站 患者病历 ：男性 年龄：67岁 就诊科室：中医科  |
| 2 | d0c61dff | 1 | 1-1 | <table><tr><td>γ-谷氨酰基转移酶</td><td>GGT</td |
| 3 | 147ad593 | 1 | 3-3 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：3
- 页码并集：`[1, 2, 3]`
- 覆盖页数：3 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 2 | 2 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
