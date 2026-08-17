# 线上统计：JLYI初治胃癌，含补充资料.pdf

## 基本信息

- 文件：`JLYI初治胃癌，含补充资料.pdf`
- 大小：6509.2 KB
- PDF 总页数：-
- doc_id：`8554c62878f811f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：15  orm_synced：True
- 处理耗时(服务端)：474.6387s  脚本耗时：475.2s
- 重解析前快照（无基线结果）：chunk_count=16 run=DONE clinical 类型记录数={'ExaminationReport': 6, 'AdmissionRecord': 1, 'LabReport': 9}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 94524544 | 1 | 1-1 | 检查项目:CT平扫+增强【胸部】,CT平扫+增强-全腹部 影像学表现: 双肺支气 |
| 2 | ee789b7a | 1 | 3-3 | 记录时间：2026-02-23 15:23 现用药史：无 病史陈述者：患者本人  |
| 3 | 1f6e3d3b | 1 | 4-4 | 检查项目：CT平扫+增强（上腹部-薄层），CT平扫+增强（下腹部-薄层），CT平 |
| 4 | c4fc592e | 1 | 12-12 | 检查项目：CT平扫+增强（上腹部-薄层），CT平扫+增强（下腹部-薄层），CT平 |
| 5 | 7114ce53 | 1 | 13-13 | 送检部位：胃窦息肉样肿块×3；胃窦溃疡性肿 临床诊断： 大体描述： 胃窦息肉样肿 |
| 6 | 04e84833 | 2 | 14-15 | 检测信息： 检测方法：荧光原位杂交（FISH） 标本类型：组织 临床诊断：胃癌  |
| 7 | b8d0147f | 1 | 8-8 | <table><tr><td>丙型肝炎抗体</td><td>Anti-HC</t |
| 8 | 1f626a2f | 1 | 10-10 | <table><tr><td>超敏肌钙蛋白T</td><td>hsTNT</td |
| 9 | 3699863f | 1 | 16-16 | <table><tr><td>丙氨酸氨基转移酶</td><td>None</td |
| 10 | 2bdb1d75 | 1 | 17-17 | <table><tr><td>中性粒细胞数目</td><td>None</td> |
| 11 | d4bd0990 | 1 | 2-2 | <table><tr><td>颜色</td><td>None</td><td>黄 |
| 12 | 6527a348 | 1 | 6-6 | <table><tr><td>ABO血型</td><td>None</td><t |
| 13 | cb1fd726 | 1 | 7-7 | <table><tr><td>颜色</td><td>COLOR</td><td> |
| 14 | 695c7a8f | 1 | 9-9 | <table><tr><td>*凝血酶原时间</td><td>PT</td><t |
| 15 | 8c99d56e | 1 | 11-11 | <table><tr><td>钾</td><td>K</td><td>4.60< |

- chunks 总数：15
- 各 chunk 页数合计（含跨页重复）：16
- 页码并集：`[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]`
- 覆盖页数：16 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 5 | 5 | ✅ |
| LabReport | 检验报告 | 9 | 9 | ✅ |

- 判定：✅ 全部类型匹配
