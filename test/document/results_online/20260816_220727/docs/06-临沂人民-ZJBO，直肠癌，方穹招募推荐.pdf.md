# 线上统计：06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf

## 基本信息

- 文件：`06-临沂人民-ZJBO，直肠癌，方穹招募推荐.pdf`
- 大小：3274.2 KB
- PDF 总页数：-
- doc_id：`df229e1a94e011f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：11  orm_synced：True
- 处理耗时(服务端)：434.3936s  脚本耗时：456.4s
- 重解析前快照（无基线结果）：chunk_count=11 run=DONE clinical 类型记录数={'ExaminationReport': 5, 'LabReport': 3, 'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 7acd8617 | 4 | 1-4 | 20200113根治术 术后XELOX 6周期 20240510复发 20240 |
| 2 | 60764c5e | 1 | 5-5 | 性别：男 年龄：64岁 出院日期：2026-01-07 17:10 住院天数：1 |
| 3 | 2fdebbef | 1 | 8-8 | 【检查描述】：心搏次数：97(60~100)bpm，PR间隔：144ms，QRS |
| 4 | a5f8e5f6 | 1 | 8-8 | 【手术信息】：肿瘤位于直肠上段 【取材部位】：1:直肠×1 【取材描述】：#:肿 |
| 5 | d77721cd | 1 | 9-9 | 【手术信息】：纵隔淋巴结肿大 【取材部位】：1:EBUS组织×1 2:EBUS刷 |
| 6 | 96421b1b | 1 | 9-9 | 【检查日期】：2026/1/16 8:18:01 【检查所见】：右肺术后改变，术 |
| 7 | 49ada3f9 | 1 | 9-9 | 【检查日期】：2025/11/18 14:25:00 【检查所见】：右肺术后改变 |
| 8 | a912e155 | 2 | 10-11 | 2026-02-03 10:41 主 诉：本次访视为评价注射用HLN601脂质体 |
| 9 | bcacd6e4 | 1 | 6-6 | <table><tr><td>KRAS Exon-2 (G12S,G12D)</ |
| 10 | a52d30af | 1 | 6-6 | <table><tr><td>红细胞</td><td>None</td><td> |
| 11 | f759c1d3 | 1 | 7-7 | <table><tr><td>总蛋白</td><td>TP</td><td>75 |

- chunks 总数：11
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`
- 覆盖页数：11 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 5 | 5 | ✅ |
| LabReport | 检验报告 | 3 | 3 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
