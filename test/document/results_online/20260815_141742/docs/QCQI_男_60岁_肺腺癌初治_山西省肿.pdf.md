# 线上统计：QCQI  男 60岁 肺腺癌初治 山西省肿.pdf

## 基本信息

- 文件：`QCQI  男 60岁 肺腺癌初治 山西省肿.pdf`
- 大小：16509.7 KB
- PDF 总页数：-
- doc_id：`5350b6447b8e11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：20  orm_synced：True
- 处理耗时(服务端)：932.39325s  脚本耗时：933.5s
- 重解析前快照（无基线结果）：chunk_count=20 run=DONE clinical 类型记录数={'LabReport': 14, 'AdmissionRecord': 1, 'ExaminationReport': 4, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | b990cab1 | 3 | 1-3 | 入院记录 女 姓名： 出生地：山西省临汾市尧都区 性别：男 职业：其他 年龄：6 |
| 2 | 3d418b31 | 1 | 4-4 | 出院记录 姓名： 性别：男 年龄：60岁 职业：其他 入院日期：2026年03月 |
| 3 | d41dc0ff | 2 | 5-6 | 病理检查报告单 S202603702 病理号: S202603702 姓名: 男 |
| 4 | 4d91e713 | 2 | 12-13 | 核医学科 PET/CT 检查报告 检查号： 189551371 姓 名： 性 别 |
| 5 | 9f211dfc | 1 | 7-7 | <table><tr><td>白蛋白</td><td>ALB</td><td>4 |
| 6 | 8859b5f2 | 1 | 7-7 | <table><tr><td>【全国HR】梅毒螺旋体抗体</td><td>TP- |
| 7 | c4c1be00 | 1 | 8-8 | <table><tr><td>白细胞</td><td>WBC</td><td>5 |
| 8 | 5ce5320c | 1 | 8-8 | <table><tr><td>淋巴细胞数</td><td>L#</td><td> |
| 9 | 5abf42ef | 1 | 9-9 | <table><tr><td>结核抗体</td><td>None</td><td |
| 10 | 60276f97 | 1 | 11-11 | <table><tr><td>三碘甲状腺原氨酸</td><td>T3</td>< |
| 11 | 7cb29c23 | 1 | 11-11 | <table><tr><td>癌胚抗原</td><td>CEA</td><td> |
| 12 | a3eead61 | 4 | 15-18 | <table><tr><td>BIM</td><td>None</td><td> |
| 13 | 2f3993c9 | 1 | 19-19 | <table><tr><td>淋巴细胞培养+干扰素（基础水平N）</td><td |
| 14 | f8e39ee1 | 1 | 7-7 | <table><tr><td>抗凝血酶III活性测定</td><td>AT</t |
| 15 | fc1523e4 | 1 | 7-7 | <table><tr><td>乙肝表面抗原</td><td>HBsAg</td> |
| 16 | 787c4572 | 1 | 8-8 | <table><tr><td>糖类抗原199</td><td>CA199</td |
| 17 | ec722ff9 | 1 | 9-9 | <table><tr><td>便潜血</td><td>None</td><td> |
| 18 | b47bfa87 | 1 | 10-10 | <table><tr><td>脂蛋白(a)</td><td>LPa</td><t |
| 19 | bf6cfdda | 1 | 10-10 | <table><tr><td>肌酸激酶同工酶</td><td>CK-MB</td |
| 20 | 59e7c46e | 1 | 14-14 | <table><tr><td>PD-L1 免疫组化</td><td>None</ |

- chunks 总数：20
- 各 chunk 页数合计（含跨页重复）：27
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`
- 覆盖页数：19 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 0 | ❌ |
| DischargeRecord | 出院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 2 | 0 | ❌ |
| LabReport | 检验报告 | 16 | 0 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, DischargeRecord, ExaminationReport, LabReport
