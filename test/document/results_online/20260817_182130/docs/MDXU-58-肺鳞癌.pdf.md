# 线上统计：MDXU-58-肺鳞癌.pdf

## 基本信息

- 文件：`MDXU-58-肺鳞癌.pdf`
- 大小：6142.9 KB
- PDF 总页数：-
- doc_id：`a0fdc04e7b8e11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：20  orm_synced：True
- 处理耗时(服务端)：428.04626s  脚本耗时：429.1s
- 重解析前快照（无基线结果）：chunk_count=19 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'AdmissionRecord': 1, 'LabReport': 14}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 14bc60bc | 1 | 1-1 | 姓名： 性别：男 年龄：58岁 婚姻：已婚 入院日期：2026年02月02日 0 |
| 2 | 58033af0 | 1 | 2-2 | 中南大学湘雅二医院 病理体视学检查与图像分析诊断报告 病理号 姓 性别：男 年龄 |
| 3 | 80456e1f | 1 | 3-3 | 中南大学湘雅二医院 THE SECOND XIANGYA HOSPITAL OF |
| 4 | d8679429 | 1 | 4-4 | 中南大学湘雅二医院 心电图报告 患者编> 心室率(60~100):90 bpm  |
| 5 | 35256999 | 1 | 20-20 | xiangya 中南大学湘雅三医院 The Third Xiangya Hosp |
| 6 | 4022ecf7 | 1 | 6-6 | <table><tr><td>半乳甘露聚糖(GM试验)</td><td>GMSY |
| 7 | c1104cf5 | 1 | 7-7 | <table><tr><td>结核分枝杆菌复合群DNA</td><td>TB-D |
| 8 | 6871e8a4 | 1 | 9-9 | <table><tr><td>乙肝病毒核酸定量</td><td>HBV-DNA< |
| 9 | 3de243e0 | 1 | 11-11 | <table><tr><td>头孢唑啉</td><td>None</td><td |
| 10 | 69b55f28 | 1 | 12-12 | <table><tr><td>*乙肝表面抗原定量</td><td>HBsAg</ |
| 11 | 94401f62 | 1 | 13-13 | <table><tr><td>高敏肌钙蛋白T</td><td>TNTsh</td |
| 12 | 4900c1ad | 1 | 14-14 | <table><tr><td>纤维蛋白降解产物</td><td>FDP</td> |
| 13 | fb2ded5f | 1 | 17-17 | <table><tr><td>镁</td><td>Mg</td><td>0.81 |
| 14 | 9d2488fd | 1 | 19-19 | <table><tr><td>单核细胞比值</td><td>MONO%</td> |
| 15 | 5a36cc5e | 1 | 5-5 | <table><tr><td>抗酸染色(自动细胞离心涂片)</td><td>AF |
| 16 | 59f129c7 | 1 | 8-8 | <table><tr><td>铜绿假单胞菌</td><td>ORGANI</td |
| 17 | f651a8fd | 1 | 10-10 | <table><tr><td>梅毒螺旋体抗体试验</td><td>Syphili |
| 18 | e3a8e85a | 1 | 15-15 | <table><tr><td>前白蛋白</td><td>PAB</td><td> |
| 19 | b7d767b4 | 1 | 16-16 | <table><tr><td>总胆汁酸</td><td>TBA</td><td> |
| 20 | 188a4fda | 1 | 18-18 | <table><tr><td>白细胞计数</td><td>WBC</td><td |

- chunks 总数：20
- 各 chunk 页数合计（含跨页重复）：20
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]`
- 覆盖页数：20 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 4 | 4 | ✅ |
| LabReport | 检验报告 | 15 | 15 | ✅ |

- 判定：✅ 全部类型匹配
