# 线上统计：西安-糖尿病-CXMI.pdf

## 基本信息

- 文件：`西安-糖尿病-CXMI.pdf`
- 大小：292.4 KB
- PDF 总页数：-
- doc_id：`bf316d7278f011f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：2  orm_synced：True
- 处理耗时(服务端)：99.259705s  脚本耗时：104.4s
- 重解析前快照（无基线结果）：chunk_count=2 run=DONE clinical 类型记录数={'MedicationRecord': 1, 'LabReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | eda8b27d | 1 | 2-2 | 电子发票(普通发票) 发票号码:25612000000033680358 开票日 |
| 2 | af3408bc | 1 | 1-1 | <table><tr><td>葡萄糖(胰岛)</td><td>GLU</td>< |

- chunks 总数：2
- 各 chunk 页数合计（含跨页重复）：2
- 页码并集：`[1, 2]`
- 覆盖页数：2 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 1 | ✅ |
| MedicationRecord | 购药 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
