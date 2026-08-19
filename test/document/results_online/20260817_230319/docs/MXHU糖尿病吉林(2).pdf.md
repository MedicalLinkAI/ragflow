# 线上统计：MXHU糖尿病吉林(2).pdf

## 基本信息

- 文件：`MXHU糖尿病吉林(2).pdf`
- 大小：1559.0 KB
- PDF 总页数：-
- doc_id：`03939cb875ba11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：111.98684s  脚本耗时：114.7s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'MedicationRecord': 3, 'LabReport': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | a6eb582a | 1 | 3-3 | 通化市东昌区人民医院 门诊病历 科室:内分泌科门诊 姓名: 性别:男,年龄:66 |
| 2 | 331f421e | 1 | 4-4 | 每周六、周日为会员日 通化万兴医药连锁第十三分店 顾客联 营业员:王鑫华 126 |
| 3 | 8385ed9a | 1 | 4-4 | 通化万兴医药连锁第十三分店 顾客联 营业员:袁清铭 125 收银员:11307  |
| 4 | 7b2c4248 | 1 | 4-4 | 通化万兴医药连锁第十三分店 顾客联 营业员:赵洪微 122 收银员:11306  |
| 5 | ca9cb182 | 1 | 1-1 | <table><tr><td>葡萄糖</td><td>HR</td><td>9. |
| 6 | 70f9edb4 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[1, 2, 3, 4]`
- 覆盖页数：4 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 2 | 2 | ✅ |
| MedicationRecord | 购药 | 3 | 3 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
