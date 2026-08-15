# 线上统计：07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf`
- 大小：11225.9 KB
- PDF 总页数：-
- doc_id：`c99b75cc7c5c11f18d62dd81525255fa`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：12  orm_synced：True
- 处理耗时(服务端)：273.9929s  脚本耗时：279.4s
- 重解析前快照（无基线结果）：chunk_count=12 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 7}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | e5910c04 | 2 | 1-2 | 20231129根治术，术后无治疗 20240410肝转移，一线治疗奥沙+卡培  |
| 2 | 7d57003d | 1 | 3-3 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号 姓名 性别：男 年龄：51 |
| 3 | 24a146ed | 2 | 4-5 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号. 姓  夕 性  别：男  |
| 4 | 6b99c38b | 2 | 7-8 | 报告单详情 www.jkqd.org.cn 20260307检 查 1.双肺多发 |
| 5 | 2847de24 | 1 | 11-11 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 6 | 571a631f | 1 | 13-13 | <table><tr><td>红细胞计数</td><td>RBC</td><td |
| 7 | dbfeb821 | 2 | 5-6 | <table><tr><td>TMB(同义突变&非同义突变)</td><td>T |
| 8 | 4f7b6aa5 | 1 | 9-9 | <table><tr><td>丙氨酸氨基转移酶</td><td>ALT</td> |
| 9 | b70d6f7f | 1 | 9-9 | <table><tr><td>唾液酸</td><td>SA</td><td>96 |
| 10 | ee0b7592 | 1 | 10-10 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |
| 11 | 8bb60d6d | 1 | 12-12 | <table><tr><td>粪便颜色</td><td>Colour</td>< |
| 12 | 3f97c3df | 1 | 14-14 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：16
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 3 | 0 | ❌ |
| LabReport | 检验报告 | 8 | 0 | ❌ |
| OutpatientRecord | 门诊 | 1 | 0 | ❌ |

- 判定：❌ 不匹配类型: ExaminationReport, LabReport, OutpatientRecord
