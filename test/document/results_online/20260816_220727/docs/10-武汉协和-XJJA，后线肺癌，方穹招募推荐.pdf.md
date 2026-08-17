# 线上统计：10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf

## 基本信息

- 文件：`10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf`
- 大小：22558.1 KB
- PDF 总页数：-
- doc_id：`ff265efe94ea11f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：23  orm_synced：True
- 处理耗时(服务端)：815.2148s  脚本耗时：822.8s
- 重解析前快照（无基线结果）：chunk_count=23 run=DONE clinical 类型记录数={'AdmissionRecord': 2, 'ExaminationReport': 6, 'LabReport': 13, 'DischargeRecord': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | f2ce7bff | 1 | 1-1 | 郑州大学第一附属医院 组织病理学检查与诊断报告 姓名： 性别：女 年龄：57岁  |
| 2 | f6635d99 | 1 | 2-2 | 郑州大学第一附属医院 细胞病理学检查与诊断报告 病理号：C25 姓名： 性别：女 |
| 3 | ee2fc909 | 3 | 3-5 | 原阳县人民医院 出院记录 姓名： 科室：肿瘤内科病区 床号：3床 住院号：02  |
| 4 | bf64428b | 4 | 6-9 | 原阳县人民医院 入院记录 姓名： 科室：肿瘤内科病区 床号：13床 住院号：02 |
| 5 | 704de681 | 4 | 9-12 | 第 4 页 姓名： 性别：女 年龄：57岁 婚姻：已婚 民族：汉族 职业：农民  |
| 6 | cfef85f1 | 2 | 13-14 | 郑州大学第一附属医院 The First Affiliated Hospital |
| 7 | 86d329e2 | 2 | 15-16 | 原阳县人民医院 CT检查报告单 病人ID: 4 姓名: 性别:女 年龄:57岁  |
| 8 | 788c135a | 1 | 17-17 | CT检查报告单 病人ID: 姓名: 性别:女 年龄:57岁 检查编号:CT02  |
| 9 | 89fd385d | 1 | 18-18 | 原阳县人民医院 CT检查报告单 病人ID: P 检查编号:CTO. 姓名:薛 性 |
| 10 | 88ec2f01 | 1 | 19-19 | 原阳县人民医院 CT检查报告单 病人ID: 姓名: 性别:女 年龄:57岁 检查 |
| 11 | 68d1043f | 1 | 21-21 | <table><tr><td>谷丙转氨酶</td><td>ALT</td><td |
| 12 | af2340f8 | 1 | 22-22 | <table><tr><td>高密度脂蛋白胆固醇</td><td>HDL-C</ |
| 13 | af945026 | 1 | 23-23 | <table><tr><td>促甲状腺激素</td><td>TSH</td><t |
| 14 | 6310450f | 1 | 24-24 | <table><tr><td>颜色</td><td>F-YS</td><td>黄 |
| 15 | 84b3f007 | 1 | 25-25 | <table><tr><td>凝血因子功能</td><td>R</td><td> |
| 16 | 3536817f | 1 | 27-27 | <table><tr><td>N末端脑利钠肽前体</td><td>NT-proB |
| 17 | eaa545f9 | 1 | 31-31 | <table><tr><td>明确/潜在临床意义的变异</td><td>None |
| 18 | 48e4b85b | 1 | 20-20 | <table><tr><td>血管内皮生长因子</td><td>VEGF</td |
| 19 | b266a1ac | 1 | 22-22 | <table><tr><td>*氯</td><td>CL</td><td>98. |
| 20 | 8dc0d89b | 1 | 26-26 | <table><tr><td>*葡萄糖</td><td>GLU</td><td> |
| 21 | 18e86005 | 1 | 28-28 | <table><tr><td>*白细胞数</td><td>WBC</td><td |
| 22 | 81fdcfd4 | 1 | 29-29 | <table><tr><td>*高敏乙型肝炎病毒(HBV-DNA)定量</td> |
| 23 | d8baaf26 | 1 | 30-30 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>None</ |

- chunks 总数：23
- 各 chunk 页数合计（含跨页重复）：33
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]`
- 覆盖页数：31 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 2 | 2 | ✅ |
| DischargeRecord | 出院 | 2 | 2 | ✅ |
| ExaminationReport | 检查报告 | 6 | 6 | ✅ |
| LabReport | 检验报告 | 13 | 13 | ✅ |

- 判定：✅ 全部类型匹配
