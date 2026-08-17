# 线上统计：07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-YSKA，后线肺癌，方穹招募推荐.pdf`
- 大小：16316.6 KB
- PDF 总页数：-
- doc_id：`8f6c718294e711f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：10  orm_synced：True
- 处理耗时(服务端)：671.06854s  脚本耗时：678.4s
- 重解析前快照（无基线结果）：chunk_count=10 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'AdmissionRecord': 1, 'LabReport': 5}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | ed425497 | 8 | 1-8 | 性别：男 婚姻：已婚 年龄：69岁 入院日期：2026-03-11 08:04  |
| 2 | 05bdf902 | 1 | 10-10 | 报告时间: 2026-03-12 【检查日期】: 2026/3/11 12:07 |
| 3 | 153e5a60 | 1 | 11-11 | 【检查日期】：2026/1/8 13:58:55 【检查所见】：右侧胸廓塌陷，右 |
| 4 | 45316ac4 | 1 | 11-11 | 【检查描述】：心搏次数：97(60~100)bpm，PR间隔：160ms，QRS |
| 5 | 02b96ed6 | 1 | 12-12 | 【手术信息】：胸腔积液 【取材部位】：1:胸膜×1 2:细胞蜡块1×1 【取材描 |
| 6 | 01868afc | 1 | 8-8 | <table><tr><td>红细胞</td><td>None</td><td> |
| 7 | 145a6ac4 | 1 | 9-9 | <table><tr><td>总蛋白</td><td>TP</td><td>70 |
| 8 | 7477c55b | 1 | 10-10 | <table><tr><td>白细胞</td><td>None</td><td> |
| 9 | fe07ec22 | 1 | 10-10 | <table><tr><td>*白细胞</td><td>None</td><td |
| 10 | 9e363ba4 | 1 | 10-10 | <table><tr><td>大便颜色</td><td>None</td><td |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：17
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`
- 覆盖页数：12 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 4 | 4 | ✅ |
| LabReport | 检验报告 | 5 | 5 | ✅ |

- 判定：✅ 全部类型匹配
