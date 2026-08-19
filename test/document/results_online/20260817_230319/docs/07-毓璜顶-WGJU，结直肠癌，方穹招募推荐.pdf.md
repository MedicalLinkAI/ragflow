# 线上统计：07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf`
- 大小：11225.9 KB
- PDF 总页数：-
- doc_id：`c99b75cc7c5c11f18d62dd81525255fa`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：12  orm_synced：True
- 处理耗时(服务端)：388.81152s  脚本耗时：389.6s
- 重解析前快照（无基线结果）：chunk_count=11 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 6}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | e5910c04 | 2 | 1-2 | 20231129根治术，术后无治疗 20240410肝转移，一线治疗奥沙+卡培  |
| 2 | e0c77a9e | 1 | 3-3 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号 姓名 性别：男 年龄：51 |
| 3 | 81942ccf | 1 | 4-4 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号. 姓  夕 性  别：男  |
| 4 | 29d2ed82 | 2 | 5-6 | 青岛市中心医疗集团 2.检测结果总览 本检测基于MGI（DNBSeq T7）测序 |
| 5 | 96372d8f | 2 | 7-8 | 19:08 41 × 报告单详情 www.jkqd.org.cn 2026030 |
| 6 | 2847de24 | 1 | 11-11 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 7 | 5b8d61bd | 1 | 12-12 | <table><tr><td>粪便颜色</td><td>Colour</td>< |
| 8 | 571a631f | 1 | 13-13 | <table><tr><td>红细胞计数</td><td>RBC</td><td |
| 9 | 4f7b6aa5 | 1 | 9-9 | <table><tr><td>丙氨酸氨基转移酶</td><td>ALT</td> |
| 10 | b70d6f7f | 1 | 9-9 | <table><tr><td>唾液酸</td><td>SA</td><td>96 |
| 11 | ee0b7592 | 1 | 10-10 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |
| 12 | 3f97c3df | 1 | 14-14 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 4 | 4 | ✅ |
| LabReport | 检验报告 | 7 | 7 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
