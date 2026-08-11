# 基准测试汇总

- 时间：20260810_140626
- PDF 目录：D:\futureCode\三月病历\诺和德美-哮喘
- dataset_id：fb850778372011f195bd2a5fbb884e34
- MedLinkAI：http://localhost:3160  RAGFlow：http://localhost:19380/api/v1
- 文档数：10

| 文件 | PDF页数 | doc_id | run | chunks | 覆盖页 | 缺失页 | 页数核对 | 门诊 | 入院 | 出院 | 购药 | 处方 | 检查报告 | 检验报告 |
|------|---------|--------|-----|--------|--------|--------|----------|------|------|------|------|------|----------|----------|
| FXJI 三门峡.pdf | 5 | 6a1ab2ce899b11f1bbbdc9c8a7f3b25f | DONE | 0 | - | [] | - | - | - | - | - | - | - | - |
| GFXI 商丘.pdf | 4 | b40fb046948111f1bd9827cf206dfa2d | DONE | 0 | - | [] | - | - | OK | - | - | - | OK | - |
| GWHU-48岁-男(2).pdf | 2 | 40948096948211f1bd9827cf206dfa2d | DONE | 0 | - | [] | - | OK | - | - | - | - | OK | - |
| LGWE-艾特美哮喘-洛阳三.pdf | 3 | db492056948211f1bd9827cf206dfa2d | DONE | 0 | - | [] | - | OK | - | - | - | - | OK | - |
| LIJI 徐州中心医院.pdf | 2 | 3d3d441e871711f1a42715083c6c5e0f | DONE | 0 | - | [] | - | - | - | - | - | - | - | - |
| LTSH 三门峡.pdf | 5 | ab76d5fc948311f1bd9827cf206dfa2d | DONE | 0 | - | [] | - | OK | - | - | - | - | OK | - |
| LYBI-艾特美哮喘(1).pdf | 3 | 5f64042c948411f1bd9827cf206dfa2d | DONE | 3 | 3 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | - | - | OK | - |
| MEFE(1).pdf | 3 | e6e9ad0c948411f1bd9827cf206dfa2d | DONE | 0 | - | [] | - | OK | - | - | - | - | OK | - |
| ZCXI-开封.pdf | 2 | 534cda0a948511f1bd9827cf206dfa2d | DONE | 0 | - | [] | - | OK | - | - | - | - | OK | - |
| ZZYU 男 65岁 推济南(1).pdf | 2 | a0dba990948511f1bd9827cf206dfa2d | DONE | 0 | - | [] | - | OK | - | - | - | - | OK | - |

判定说明：OK=该类型有 chunk 落库；LOST=SmartSplitter 已识别但最终未落库（多为 SyncChunks 同步失败）
