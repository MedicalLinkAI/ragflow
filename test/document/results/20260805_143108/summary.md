# 基准测试汇总

- 时间：20260805_143108
- PDF 目录：D:\futureCode\三月病历\麦济哮喘
- dataset_id：fb850778372011f195bd2a5fbb884e34
- MedLinkAI：http://localhost:3160  RAGFlow：http://localhost:19380/api/v1
- 文档数：20

| 文件 | PDF页数 | doc_id | run | chunks | 覆盖页 | 缺失页 | 页数核对 | 门诊 | 入院 | 出院 | 购药 | 处方 | 检查报告 | 检验报告 |
|------|---------|--------|-----|--------|--------|--------|----------|------|------|------|------|------|----------|----------|
| 1_GWYA-女-35岁222.pdf | 5 | 288b2fa2908311f1a3da71efcdd7cc1f | - | 4 | 5 | [] | ✅ 完全覆盖：chunk 页码并集 =  | - | OK | - | - | OK | - | - |
| chho-麦济122-哮喘-沈阳-医大四院.pdf | 13 | a747105e908311f1a3da71efcdd7cc1f | - | 12 | 13 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | OK | OK | OK |
| DAXI-哮喘.pdf | 52 | 4f971ac4908411f1a3da71efcdd7cc1f | - | 34 | 40 | [10, 11, 12, 13, 14, 32, 33, 34, 35, 36, 37, 38] | ❌ 未完全覆盖：覆盖 40/52 页，缺 | OK | OK | OK | - | OK | OK | OK |
| HXJ 哮喘 广三.pdf | 17 | 32f80906908811f1a3da71efcdd7cc1f | - | 16 | 17 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | - | OK | - | OK |
| LHYA-哮喘-沈阳医大四.pdf | 7 | 1f329962908911f1a3da71efcdd7cc1f | - | 6 | 7 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | OK | - |
| lsju-哮喘-沈阳(1).pdf | 9 | 83997060908911f1a3da71efcdd7cc1f | - | 4 | 4 | [1, 2, 6, 7, 8] | ❌ 未完全覆盖：覆盖 4/9 页，缺失  | OK | - | - | OK | - | - | - |
| LXQI222.pdf | 10 | c9872b6c908911f1a3da71efcdd7cc1f | - | 4 | 10 | [] | ✅ 完全覆盖：chunk 页码并集 =  | - | OK | OK | - | OK | OK | - |
| lzga-哮喘-沈阳(1).pdf | 5 | e1b14d16908a11f1a3da71efcdd7cc1f | - | 6 | 5 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | OK | OK | - | - | - |
| LZK 哮喘 广三(1).pdf | 16 | 4e10ceb4908b11f1a3da71efcdd7cc1f | - | 13 | 16 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | - | OK | OK | - |
| LZQ 64 哮喘 深圳二院.pdf | 20 | d7626528908c11f1a3da71efcdd7cc1f | - | 11 | 20 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | - | - |
| MARO-四川省人民.pdf | 14 | feba5e4a908d11f1a3da71efcdd7cc1f | - | 10 | 13 | [8] | ❌ 未完全覆盖：覆盖 13/14 页，缺 | OK | - | - | - | OK | - | OK |
| XALI麦济新乡 2026-03-06 17.04 (1).pdf | 27 | - | - | 0 | - | [] | - | - | - | - | - | - | - | - |
| yayu-哮喘-麦济122-沈阳-医大四(1).pdf | 6 | 4691aeac908f11f1a3da71efcdd7cc1f | - | 7 | 6 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | OK | - |
| YJXI 68 哮喘 山西(1).pdf | 11 | a0687fe6908f11f1a3da71efcdd7cc1f | - | 10 | 11 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | OK | OK | OK | OK | OK |
| YXLA（支气管哮喘）222.pdf | 19 | 5986c9ec909011f1a3da71efcdd7cc1f | - | 15 | 19 | [] | ✅ 完全覆盖：chunk 页码并集 =  | - | OK | OK | OK | OK | OK | - |
| 哮喘-HJCH222   2.27.pdf | 17 | fd9c5c4e909111f1a3da71efcdd7cc1f | - | 7 | 11 | [10, 11, 12, 13, 15, 17] | ❌ 未完全覆盖：覆盖 11/17 页，缺 | OK | OK | OK | - | - | OK | - |
| 麦济WRNA(2).pdf | 9 | fdb3bc58909211f1a3da71efcdd7cc1f | - | 9 | 9 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | - | - |
| 麦济WZWA222.pdf | 5 | c9526904909311f1a3da71efcdd7cc1f | - | 4 | 5 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | OK | - |
| 麦济ZHGL.pdf | 6 | 2d7d9c50909411f1a3da71efcdd7cc1f | - | 5 | 6 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | - | - |
| 麦济ZHYH.pdf | 6 | 8b75f8fc909411f1a3da71efcdd7cc1f | - | 6 | 6 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | - | - |

判定说明：OK=该类型有 chunk 落库；LOST=SmartSplitter 已识别但最终未落库（多为 SyncChunks 同步失败）
