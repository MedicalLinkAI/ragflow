# 线上统计：07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf`
- 大小：11225.9 KB
- PDF 总页数：-
- doc_id：`a646f41e94e611f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：12  orm_synced：True
- 处理耗时(服务端)：324.1941s  脚本耗时：342.5s
- 重解析前快照（无基线结果）：chunk_count=11 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 6}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 0639b6cb | 1 | 2-2 | 康复大学青岛中心医院 门诊病历 姓名： 性别：男 出生日期：19 龄：53岁 门 |
| 2 | 098b57ac | 1 | 3-3 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号 姓名 性别：男 年龄：51 |
| 3 | d126485c | 1 | 4-4 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号. 姓  夕 性  别：男  |
| 4 | 9f3762f3 | 2 | 5-6 | 青岛市中心医疗集团 2.检测结果总览 本检测基于MGI（DNBSeq T7）测序 |
| 5 | c22c14b2 | 2 | 7-8 | 19:08 41 × 报告单详情 www.jkqd.org.cn 2026030 |
| 6 | abbe06f7 | 1 | 12-12 | <table><tr><td>粪便颜色</td><td>Colour</td>< |
| 7 | e32aa269 | 1 | 13-13 | <table><tr><td>红细胞计数</td><td>RBC</td><td |
| 8 | 8f73a2e9 | 1 | 14-14 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |
| 9 | bf9b0f13 | 1 | 9-9 | <table><tr><td>唾液酸</td><td>SA</td><td>96 |
| 10 | c00c9cd9 | 1 | 10-10 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |
| 11 | 215a4130 | 1 | 11-11 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 12 | 07f42712 | 1 | 9-9 | <table><tr><td>丙氨酸氨基转移酶</td><td>ALT</td> |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：14
- 页码并集：`[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：13 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 4 | 4 | ✅ |
| LabReport | 检验报告 | 7 | 7 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
