# 线上统计：TEET-男-23岁-哮喘.pdf

## 基本信息

- 文件：`TEET-男-23岁-哮喘.pdf`
- 大小：2158.0 KB
- PDF 总页数：-
- doc_id：`77f36374872411f1bb8027103a248952`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：5  orm_synced：True
- 处理耗时(服务端)：287.71964s  脚本耗时：289.1s
- 重解析前快照（无基线结果）：chunk_count=5 run=DONE clinical 类型记录数={'LabReport': 2, 'ExaminationReport': 1, 'AdmissionRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 1def03ae | 1 | 1-1 | (cT2N1M1 IV期) 入院时间:2025-01-08 14:29:35 过 |
| 2 | 592635b5 | 2 | 2-3 | 出院病情证明 性别：男 年龄：58岁 科室：肿瘤科三病区 床号：46 住院号：1 |
| 3 | 819d96a3 | 1 | 3-3 | 15870541 检查部位 头部CT 检查类别 CT 检查名称 胸部CT增强扫描 |
| 4 | 66ee4c74 | 1 | 4-4 | <table><tr><td>血小板平均分</td><td>None</td>< |
| 5 | da53d1ee | 1 | 5-5 | <table><tr><td>中性粒细胞百分比</td><td>None</td |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[1, 2, 3, 4, 5]`
- 覆盖页数：5 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 1 | 1 | ✅ |
| LabReport | 检验报告 | 2 | 2 | ✅ |

- 判定：✅ 全部类型匹配
