# 线上统计：07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-WGJU，结直肠癌，方穹招募推荐.pdf`
- 大小：11225.9 KB
- PDF 总页数：-
- doc_id：`a646f41e94e611f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：11  orm_synced：True
- 处理耗时(服务端)：379.34418s  脚本耗时：394.3s
- 重解析前快照（无基线结果）：chunk_count=12 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 7}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 70dfe451 | 2 | 1-2 | 20231129根治术，术后无治疗 20240410肝转移，一线治疗奥沙+卡培  |
| 2 | 18595845 | 1 | 3-3 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号 姓名 性别：男 年龄：51 |
| 3 | e823d689 | 2 | 4-5 | 青岛大学附属医院 市南院区 病理检查诊断报告 病理号. 姓  夕 性  别：男  |
| 4 | 4ce57933 | 2 | 5-6 | 2.检测结果总览 本检测基于MGI（DNBSeq T7）测序平台对样本进行高通量 |
| 5 | 2aa61076 | 2 | 7-8 | 19:08 41 × 报告单详情 www.jkqd.org.cn 2026030 |
| 6 | e32aa269 | 1 | 13-13 | <table><tr><td>红细胞计数</td><td>RBC</td><td |
| 7 | 8f73a2e9 | 1 | 14-14 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |
| 8 | 982fa1c6 | 1 | 9-9 | <table><tr><td>丙氨酸氨基转移酶</td><td>ALT</td> |
| 9 | e0747229 | 1 | 10-10 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |
| 10 | 9aa91d31 | 1 | 11-11 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 11 | ca80f684 | 1 | 12-12 | <table><tr><td>粪便颜色</td><td>Colour</td>< |

- chunks 总数：11
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 4 | 4 | ✅ |
| LabReport | 检验报告 | 6 | 6 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
