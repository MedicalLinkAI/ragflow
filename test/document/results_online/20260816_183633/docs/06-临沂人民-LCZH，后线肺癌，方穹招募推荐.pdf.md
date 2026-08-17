# 线上统计：06-临沂人民-LCZH，后线肺癌，方穹招募推荐.pdf

## 基本信息

- 文件：`06-临沂人民-LCZH，后线肺癌，方穹招募推荐.pdf`
- 大小：171676.3 KB
- PDF 总页数：-
- doc_id：`0486861a94de11f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：9  orm_synced：True
- 处理耗时(服务端)：843.4639s  脚本耗时：856.3s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'ExaminationReport': 2, 'OutpatientRecord': 2, 'LabReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 0d94e5c2 | 6 | 1-6 | 就诊时间：2026-03-04 18:34 主诉：诊肺癌1年，靶向治疗后进展。  |
| 2 | 1516c682 | 3 | 7-9 | 2026-03-06 10:12 患者于2026-03-05来院行EOT检查，今 |
| 3 | 8fe46694 | 1 | 10-10 | 检查名称：下腹部CT平扫+增强(能量成像)_上腹部CT平扫+增强(能量成像)_胸 |
| 4 | 7a56a7d2 | 1 | 11-11 | 检查名称：颅脑MR平扫+增强 影像表现： 脑内白质区见多发点片状长T1长T2异常 |
| 5 | b877ae26 | 3 | 16-18 | 性别：女 职业：农民 年龄：57岁 入院时间：2025-10-15 14:53  |
| 6 | 65bf1087 | 1 | 12-12 | <table><tr><td>丙氨酸氨基转移酶</td><td>None</td |
| 7 | 96efd741 | 1 | 13-13 | <table><tr><td>凝血酶原时间</td><td>None</td>< |
| 8 | 66e47fa3 | 1 | 14-14 | <table><tr><td>*白细胞</td><td>None</td><td |
| 9 | a4b073e5 | 1 | 15-15 | <table><tr><td>白细胞计数</td><td>None</td><t |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：18
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]`
- 覆盖页数：18 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 2 | 2 | ✅ |
| LabReport | 检验报告 | 4 | 4 | ✅ |
| OutpatientRecord | 门诊 | 2 | 2 | ✅ |

- 判定：✅ 全部类型匹配
