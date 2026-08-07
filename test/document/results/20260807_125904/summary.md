# 基准测试汇总

- 时间：20260807_125904
- PDF 目录：D:\futureCode\三月病历\706-101
- dataset_id：fb850778372011f195bd2a5fbb884e34
- MedLinkAI：http://localhost:3160  RAGFlow：http://localhost:19380/api/v1
- 文档数：5

| 文件 | PDF页数 | doc_id | run | chunks | 覆盖页 | 缺失页 | 页数核对 | 门诊 | 入院 | 出院 | 购药 | 处方 | 检查报告 | 检验报告 |
|------|---------|--------|-----|--------|--------|--------|----------|------|------|------|------|------|----------|----------|
| Wlge-肝癌-男-57岁.pdf | 16 | 85a8e7ec918711f18dbe1f8f96f1c395 | DONE | 16 | 16 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | OK | OK | - | - | OK | OK |
| 十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | 12 | 688aee0a918011f18dbe1f8f96f1c395 | DONE | 9 | 12 | [] | ✅ 完全覆盖：chunk 页码并集 =  | - | OK | - | - | - | OK | OK |
| 广西-KLYY-肺腺癌-方穹推荐706-IB期.pdf | 26 | f701d642918211f18dbe1f8f96f1c395 | DONE | 18 | 26 | [] | ✅ 完全覆盖：chunk 页码并集 =  | - | OK | - | - | - | OK | OK |
| 徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | 14 | de8a02fc918111f18dbe1f8f96f1c395 | DONE | 8 | 14 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | OK | - | - | OK | OK |
| 湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | 9 | 0e185858918611f18dbe1f8f96f1c395 | DONE | 3 | 8 | [8] | ❌ 未完全覆盖：覆盖 8/9 页，缺失  | - | - | OK | - | - | OK | - |

判定说明：OK=该类型有 chunk 落库；LOST=SmartSplitter 已识别但最终未落库（多为 SyncChunks 同步失败）
