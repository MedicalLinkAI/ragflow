# 线上统计：ZYXI.pdf

## 基本信息

- 文件：`ZYXI.pdf`
- 大小：6020.8 KB
- PDF 总页数：-
- doc_id：`909ccb847b9111f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：9  orm_synced：True
- 处理耗时(服务端)：283.36636s  脚本耗时：284.9s
- 重解析前快照（无基线结果）：chunk_count=9 run=DONE clinical 类型记录数={'LabReport': 2, 'ExaminationReport': 6, 'AdmissionRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | b91df230 | 3 | 1-3 | 临清市人民医院 入院记录 床号： 别：男 年龄：66岁 科别：血液肿瘤科 住院  |
| 2 | dd448d49 | 1 | 13-13 | 山东大学齐鲁医院 病理检查报告单 申请号 病理号：2025111633 姓名 性 |
| 3 | 400b742c | 1 | 14-14 | 印报告 - IMPAX RIS 山东大学齐鲁医院 扫一扫查看云胶片 放射科CT报 |
| 4 | b064a657 | 1 | 15-15 | 山东大学齐鲁医院 一扫查看云胶片 放射科CT报告单 姓名 性别 男 年龄 66岁 |
| 5 | 7cdd16a1 | 1 | 16-16 | 山东大学齐鲁医院呼吸科 电子支气管镜检查治疗报告单 检查编号 姓 性别：男 年龄 |
| 6 | a00b2f63 | 5 | 6-11 | <table><tr><td>基因组变异检测结果</td><td>None</t |
| 7 | 2f9f9a8f | 1 | 4-4 | <table><tr><td>PD-L1 蛋白表达水平 (TPS)</td><t |
| 8 | 9f5e4ead | 1 | 17-17 | <table><tr><td>*★癌胚抗原</td><td>CEA</td><t |
| 9 | 976b86dd | 1 | 18-18 | <table><tr><td>白细胞</td><td>WBC</td><td>8 |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18]`
- 覆盖页数：15 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 4 | 4 | ✅ |
| LabReport | 检验报告 | 4 | 4 | ✅ |

- 判定：✅ 全部类型匹配
