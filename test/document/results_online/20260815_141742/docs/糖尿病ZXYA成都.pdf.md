# 线上统计：糖尿病ZXYA成都.pdf

## 基本信息

- 文件：`糖尿病ZXYA成都.pdf`
- 大小：2026.0 KB
- PDF 总页数：-
- doc_id：`0948b6b47e6811f1af97e3985ba7f8da`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：115.13083s  脚本耗时：119.6s
- 重解析前快照（无基线结果）：chunk_count=7 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'MedicationRecord': 2, 'PrescriptionRecord': 2, 'LabReport': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 35e66bd6 | 1 | 1-1 | 成都市武侯区玉林社区卫生服务中心 全科门诊病历 门诊号：2404093152 姓 |
| 2 | f8ae3c61 | 1 | 4-4 | 23:12 京东买药 [力唐宁] 盐酸二甲双胍缓释片0.5g*30片/盒 盐酸二 |
| 3 | 13e22ed9 | 1 | 5-5 | 银川京东互联网医院 普通 处方 处方笺 NO. 127961482746935  |
| 4 | c425b091 | 1 | 6-6 | 23:12 京东买药 [力唐宁] 盐酸二甲双胍缓释片0.5g*30片/盒 数量: |
| 5 | a148dd2e | 1 | 7-7 | 银川京东互联网医院 普通 处方 已使用 已使用 处方笺 已使用 NO. 1284 |
| 6 | 5c9d2589 | 2 | 2-3 | <table><tr><td>葡萄糖</td><td>Glu</td><td>1 |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6, 7]`
- 覆盖页数：7 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 0 | ❌ |
| MedicationRecord | 购药 | 2 | 0 | ❌ |
| OutpatientRecord | 门诊 | 1 | 0 | ❌ |
| PrescriptionRecord | 处方 | 2 | 0 | ❌ |

- 判定：❌ 不匹配类型: LabReport, MedicationRecord, OutpatientRecord, PrescriptionRecord
