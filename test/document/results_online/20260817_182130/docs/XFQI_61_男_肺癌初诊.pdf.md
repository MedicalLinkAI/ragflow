# 线上统计：XFQI 61 男 肺癌初诊.pdf

## 基本信息

- 文件：`XFQI 61 男 肺癌初诊.pdf`
- 大小：1376.0 KB
- PDF 总页数：-
- doc_id：`89835e9279b811f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：20  orm_synced：True
- 处理耗时(服务端)：510.12936s  脚本耗时：511.8s
- 重解析前快照（无基线结果）：chunk_count=20 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'ExaminationReport': 6, 'LabReport': 13}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 421f3e51 | 1 | 1-1 | 图像: 镜下所见: 病理诊断: 常规报告: 超声空化加快标本：（右侧臀部穿刺组织 |
| 2 | 43a58f16 | 2 | 1-2 | HONOR 100 肉眼所见: 图像: 镜下所见: 病理诊断: 常规报告: 会诊 |
| 3 | e57dff91 | 2 | 2-3 | HONOR 100 超声所见： 右侧臀部皮下软组织内可见一大小约为78x43x4 |
| 4 | 48d8fea6 | 2 | 3-4 | HONOR 100 性别：男 检查号：C 病区： 年龄：61岁 病案号： 身份证 |
| 5 | 10c7a33a | 2 | 4-5 | HONOR 100 姓名： 性别：男 年龄：61岁 检查号： 登记号： 病案号： |
| 6 | 0169c76e | 2 | 5-6 | HONOR 100 Flow [L/s] F/V ex 6 Vol [L] 4  |
| 7 | 5114f68b | 2 | 20-21 | 入院记录 第1次入院 姓名： 出生地：邵阳市 性别：男 民族：汉族 年龄：61岁 |
| 8 | 308af95e | 1 | 7-7 | <table><tr><td>CEA</td><td>None</td><td> |
| 9 | aa96de54 | 1 | 8-8 | <table><tr><td>降钙素原</td><td>PCT</td><td> |
| 10 | ec52459c | 1 | 11-11 | <table><tr><td>ABO血型</td><td>None</td><t |
| 11 | b4435950 | 1 | 12-12 | <table><tr><td>丙型肝炎抗体</td><td>Anti-HCV</ |
| 12 | b5c9d971 | 1 | 13-13 | <table><tr><td>游离甲状腺素*</td><td>FT4</td>< |
| 13 | 21c0206e | 1 | 15-15 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |
| 14 | a83ca3ea | 1 | 19-19 | <table><tr><td>WBC</td><td>None</td><td> |
| 15 | e62104f3 | 1 | 9-9 | <table><tr><td>C-反应蛋白</td><td>CRP</td><t |
| 16 | 84f21d36 | 1 | 10-10 | <table><tr><td>总T细胞(CD3+)</td><td>T</td> |
| 17 | 2e677cf6 | 1 | 14-14 | <table><tr><td>hsTNT</td><td>None</td><t |
| 18 | 19cf0641 | 1 | 16-16 | <table><tr><td>*钾</td><td>K</td><td>4.19 |
| 19 | 5038e136 | 1 | 17-17 | <table><tr><td>COLOR 颜色</td><td>COLOR</t |
| 20 | 6c52b36d | 1 | 18-18 | <table><tr><td>颜色</td><td>COLOR</td><td> |

- chunks 总数：20
- 各 chunk 页数合计（含跨页重复）：26
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]`
- 覆盖页数：21 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 6 | 6 | ✅ |
| LabReport | 检验报告 | 13 | 13 | ✅ |

- 判定：✅ 全部类型匹配
