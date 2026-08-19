# 线上统计：HBDE-男-67岁-肺鳞癌初治-辽宁.pdf

## 基本信息

- 文件：`HBDE-男-67岁-肺鳞癌初治-辽宁.pdf`
- 大小：6279.3 KB
- PDF 总页数：-
- doc_id：`6baa1b5e7b8e11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：8  orm_synced：True
- 处理耗时(服务端)：208.04094s  脚本耗时：212.4s
- 重解析前快照（无基线结果）：chunk_count=8 run=DONE clinical 类型记录数={'ExaminationReport': 5, 'LabReport': 3}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 32c7aa62 | 1 | 1-1 | 中国医科大学附属第一医院 病理检查补充报告 病理号: 姓名: 男 性别: 男 年 |
| 2 | 2da92960 | 1 | 2-2 | 中国医科大学附属第一医院核医学科 PET/CT 检查报告 PET/CT 号 姓名 |
| 3 | caa9427d | 2 | 3-4 | RiMAG 一脉阳光医学影像 辽宁HR 辽宁一脉阳光医学影像诊断中心 *扫一扫看 |
| 4 | 8fe3fb0b | 1 | 5-5 | 辽宁HR 营口市人民医院 (营口经济技术开发区中心医院) 全身CT检查报告单 微 |
| 5 | 734b07ec | 1 | 6-6 | 营口市人民医院(营口经济技术开发区中心医院) 彩色超声检查图文报告 姓名： 性别 |
| 6 | c74cbcdd | 1 | 7-7 | <table><tr><td>白细胞</td><td>WBC</td><td>1 |
| 7 | b796de23 | 1 | 7-7 | <table><tr><td>总胆红素</td><td>TBil</td><td |
| 8 | 3401cecf | 1 | 8-8 | <table><tr><td>酸碱度</td><td>None</td><td> |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：9
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8]`
- 覆盖页数：8 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 5 | 5 | ✅ |
| LabReport | 检验报告 | 3 | 3 | ✅ |

- 判定：✅ 全部类型匹配
