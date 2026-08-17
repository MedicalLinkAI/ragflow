# 线上统计：湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf

## 基本信息

- 文件：`湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf`
- 大小：2015.3 KB
- PDF 总页数：-
- doc_id：`7a4fd96c7eb011f1af97e3985ba7f8da`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：3  orm_synced：False
- 处理耗时(服务端)：311.96622s  脚本耗时：316.2s
- 重解析前快照（无基线结果）：chunk_count=3 run=DONE clinical 类型记录数={'ExaminationReport': 2, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 5eb7c670 | 6 | 1-6 | 金域医学 KngMed Diagnostics 病理诊断报告书 1/1 标本条码 |
| 2 | b5ba39a5 | 1 | 7-7 | 长沙益康肿瘤医院 出院记录 性别 男 年龄 49岁 病区 号 入院时间：2026 |
| 3 | b845b421 | 1 | 9-9 | 长沙市第四医院（长沙市中西医结合医院） 湖南HR CT 诊断报告单 姓名： 性别 |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：8
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 9]`
- 覆盖页数：8 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 2 | 2 | ✅ |

- 判定：✅ 全部类型匹配
