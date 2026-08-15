# 线上统计：RREE-男-23岁-哮喘.pdf

## 基本信息

- 文件：`RREE-男-23岁-哮喘.pdf`
- 大小：3340.9 KB
- PDF 总页数：-
- doc_id：`c5e85c18872b11f1bb8027103a248952`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：4  orm_synced：True
- 处理耗时(服务端)：602.1118s  脚本耗时：603.7s
- 重解析前快照（无基线结果）：chunk_count=4 run=DONE clinical 类型记录数={'LabReport': 3, 'AdmissionRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 65b38322 | 6 | 1-6 | 成都市金牛区人民医院·四川省人民医院金牛医院 入院记录 姓名： 性别：女 年龄： |
| 2 | 7f2d4db9 | 1 | 8-8 | <table><tr><td>天门冬氨酸氨基转移酶</td><td>AST</t |
| 3 | 76ae971c | 1 | 9-9 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |
| 4 | c1cab2f7 | 1 | 7-7 | <table><tr><td>白细胞计数</td><td>WBC</td><td |

- chunks 总数：4
- 各 chunk 页数合计（含跨页重复）：9
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：9 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| LabReport | 检验报告 | 3 | 3 | ✅ |

- 判定：✅ 全部类型匹配
