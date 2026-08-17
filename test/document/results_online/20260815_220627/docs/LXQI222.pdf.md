# 线上统计：LXQI222.pdf

## 基本信息

- 文件：`LXQI222.pdf`
- 大小：62937.7 KB
- PDF 总页数：-
- doc_id：`a4816fe696d111f19d3ab1cda0a97c3d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：5  orm_synced：False
- 处理耗时(服务端)：324.60385s  脚本耗时：325.9s
- 基线对比（20260814_095003）：基线 chunks=4 → 本次 chunks=5

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 76379f25 | 4 | 1-4 | 入院记录 姓名： 床号：23-03床 病历号：0 科室：呼吸与危重医学科医生 站 |
| 2 | feddb89d | 3 | 5-7 | 出院记录 姓名： 床号：23-03床 病历号：0 科室：呼吸与危重医学科医生站  |
| 3 | 0bc3c06f | 1 | 8-8 | 肺功能通气阻力检查报告 姓名： 性别：女 身高：151 cm 病历号： 年龄：7 |
| 4 | 6c8c1ee7 | 1 | 9-9 | 贵州医科大学附属医院 THE AFFILIATED HOSPITAL OF GU |
| 5 | 61352fa8 | 1 | 10-10 | 亦康互联网医院 普通 处方 已使用 已使用 已使用 联 处方笺 NO.: 202 |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- 覆盖页数：10 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 2 | 2 | ✅ |
| PrescriptionRecord | 处方 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
