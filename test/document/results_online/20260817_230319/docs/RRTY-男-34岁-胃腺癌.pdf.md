# 线上统计：RRTY-男-34岁-胃腺癌.pdf

## 基本信息

- 文件：`RRTY-男-34岁-胃腺癌.pdf`
- 大小：10096.9 KB
- PDF 总页数：-
- doc_id：`5d2374ee872911f1bb8027103a248952`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：7  orm_synced：True
- 处理耗时(服务端)：822.7042s  脚本耗时：828.1s
- 重解析前快照（无基线结果）：chunk_count=7 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'MedicalOrder': 1, 'LabReport': 4, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 47893ead | 3 | 1-3 | 2125 科室: 肿瘤科、血液科 病历号: 2025004913 费别: 异地医 |
| 2 | f4f6efbd | 3 | 4-6 | 成都市金牛区人民医院·四川省人民医院金牛医院 出院证明书 姓名: 科别:肿瘤科、 |
| 3 | 6aae2e22 | 4 | 12-15 | 姓名: 性别:女年龄:58岁身份证号: 科室:肿瘤科、血液科病历号:202500 |
| 4 | 05488e80 | 1 | 8-8 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 5 | 0d37258a | 1 | 10-10 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 6 | c462d13e | 1 | 7-7 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 7 | 674d41bf | 1 | 9-9 | <table><tr><td>白细胞计数</td><td>WBC</td><td |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：14
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]`
- 覆盖页数：14 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| LabReport | 检验报告 | 4 | 4 | ✅ |
| MedicalOrder | 医嘱 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
