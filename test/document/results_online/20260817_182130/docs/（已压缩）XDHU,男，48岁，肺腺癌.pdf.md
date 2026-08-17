# 线上统计：（已压缩）XDHU,男，48岁，肺腺癌.pdf

## 基本信息

- 文件：`（已压缩）XDHU,男，48岁，肺腺癌.pdf`
- 大小：12291.8 KB
- PDF 总页数：-
- doc_id：`8b8ebe7679b711f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：15  orm_synced：True
- 处理耗时(服务端)：1027.6586s  脚本耗时：1032.6s
- 重解析前快照（无基线结果）：chunk_count=15 run=DONE clinical 类型记录数={'ExaminationReport': 3, 'AdmissionRecord': 1, 'LabReport': 7, 'MedicalOrder': 3}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 2a7ad669 | 3 | 1-3 | 单 询 全选 反选 长期√临时 医嘱/治疗项目管理(医院库) C 议是否有改医嘱 |
| 2 | 581bf6e6 | 2 | 3-4 | 科室床位列表 医嘱管理 医嘱目录查询 在院病人查询 医嘱停止/取消 数字化医院信 |
| 3 | b2213110 | 2 | 4-5 | 末位列表 医嘱管理 医嘱目录查询 在院病人查询 医嘱停止/取消 数字化医院信息系 |
| 4 | 7bc20ea1 | 1 | 6-6 | 姓名： 申请科室：呼吸内科 病人ID号：00 7 检查号：NC20260421- |
| 5 | c85993e0 | 2 | 6-7 | 门诊病人 送检日期：2026/4/24 送检医生：邓平浩 标本名称：肺穿刺组织  |
| 6 | 61ce8448 | 1 | 8-8 | 门诊号： 住院号：49381 科室：三病区 病区： 心率：75bpm SV1/R |
| 7 | 9a2533e7 | 1 | 15-15 | \begin{tabular}{ll} 报告时间: 2026-04-24 \hl |
| 8 | 911e082a | 2 | 17-18 | 入院时间： 2026-04-23 09:35 病史陈述者： 病史由患者本人自述  |
| 9 | d984e8e5 | 1 | 9-9 | <table><tr><td>ABO正定型</td><td>ABO</td><t |
| 10 | d527e3b1 | 1 | 10-10 | <table><tr><td>白细胞</td><td>WBC</td><td>6 |
| 11 | 8b959d50 | 1 | 12-12 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HbsAg< |
| 12 | 17d200d9 | 1 | 13-13 | <table><tr><td>凝血酶原时间</td><td>PT_s</td>< |
| 13 | 5fb97ded | 1 | 14-14 | <table><tr><td>癌胚抗原</td><td>CEA</td><td> |
| 14 | 671aa7d5 | 1 | 15-15 | <table><tr><td>颜色</td><td>DB-YS</td><td> |
| 15 | 725d0621 | 1 | 11-11 | <table><tr><td>葡萄糖</td><td>None</td><td> |

- chunks 总数：15
- 各 chunk 页数合计（含跨页重复）：21
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18]`
- 覆盖页数：17 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 3 | 3 | ✅ |
| LabReport | 检验报告 | 8 | 7 | ❌ |
| MedicalOrder | 医嘱 | 3 | 3 | ✅ |

- 判定：❌ 不匹配类型: LabReport
