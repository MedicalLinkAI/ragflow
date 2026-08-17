# 线上统计：BBYU-男-23岁-哮喘.pdf

## 基本信息

- 文件：`BBYU-男-23岁-哮喘.pdf`
- 大小：9808.0 KB
- PDF 总页数：-
- doc_id：`4413853e923211f19f644920a769b91a`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：8  orm_synced：True
- 处理耗时(服务端)：383.62222s  脚本耗时：387.8s
- 重解析前快照（无基线结果）：chunk_count=8 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'ExaminationReport': 1, 'LabReport': 6}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | f713e551 | 6 | 1-6 | 322195509214595 科室:肿瘤科、血液科 病历号: 费别:异地医保  |
| 2 | 213e5e74 | 1 | 13-13 | 肿瘤科、血液科 病历号: 费别: 异地医保 报告 报告内容 金牛区人民医院CT报 |
| 3 | 65b56b24 | 1 | 7-7 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 4 | 9e98ac8f | 1 | 11-11 | <table><tr><td>神经元特异性烯醇化酶</td><td>NSE</t |
| 5 | 73a6e4d6 | 1 | 12-12 | <table><tr><td>肌钙蛋白I</td><td>cTnI</td><t |
| 6 | 4a15bb7a | 1 | 8-8 | <table><tr><td>天门冬氨酸氨基转移酶</td><td>AST</t |
| 7 | 0fd476a6 | 1 | 9-9 | <table><tr><td>r-谷氨酰基转酞酶</td><td>GGT</td |
| 8 | facb29e8 | 1 | 10-10 | <table><tr><td>白细胞计数</td><td>WBC</td><td |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：13
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]`
- 覆盖页数：13 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 1 | 1 | ✅ |
| LabReport | 检验报告 | 6 | 6 | ✅ |

- 判定：✅ 全部类型匹配
