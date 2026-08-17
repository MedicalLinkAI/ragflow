# 线上统计：LIJI-女-45岁-类风湿性关节炎.pdf

## 基本信息

- 文件：`LIJI-女-45岁-类风湿性关节炎.pdf`
- 大小：235.8 KB
- PDF 总页数：-
- doc_id：`d8be4928871811f1bb8027103a248952`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：2  orm_synced：False
- 处理耗时(服务端)：192.90814s  脚本耗时：196.8s
- 重解析前快照（无基线结果）：chunk_count=2 run=DONE clinical 类型记录数={'ExaminationReport': 1, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 92a81822 | 1 | 1-1 | 徐州矿务集团总医院 徐州医科大学第二附属医院 间病房入、出院记录 ：十二病区护理 |
| 2 | 103e8629 | 1 | 2-2 | 徐州医科大学附属医院 肺功能检查报告 舒张试验 姓名： 科别： 性别： 身高：1 |

- chunks 总数：2
- 各 chunk 页数合计（含跨页重复）：2
- 页码并集：`[1, 2]`
- 覆盖页数：2 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
