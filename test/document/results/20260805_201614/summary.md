# 基准测试汇总

- 时间：20260806_merged（合并 20 个文档）
- PDF 目录：D:\futureCode\三月病历\麦济哮喘
- dataset_id：fb850778372011f195bd2a5fbb884e34
- 说明：由 20260806_full_rescan / _2 / lzk_reparse / LZQ 单独 合并（3160 间歇超时补齐）

| 文件 | PDF页数 | doc_id | run | chunks | 覆盖页 | 缺失页 | 页数核对 | 门诊 | 入院 | 出院 | 购药 | 处方 | 检查报告 | 检验报告 |
|------|---------|--------|-----|--------|--------|--------|----------|------|------|------|------|------|----------|----------|
| 1_GWYA-女-35岁222.pdf | 5 | 093de34c90ba11f1a3da71efcdd7cc1f | - | 4 | 5 | [] | ✅ 完全覆盖：chunk 页码并集 =  | - | OK | - | - | OK | - | - |
| chho-麦济122-哮喘-沈阳-医大四院.pdf | 13 | 814bf36a90ba11f1a3da71efcdd7cc1f | - | 12 | 13 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | OK | OK | OK |
| DAXI-哮喘.pdf | 52 | 399fea9890bb11f1a3da71efcdd7cc1f | - | 37 | 40 | [10, 11, 12, 13, 14, 32, 33, 34, 35, 36, 37, 38] | ❌ 未完全覆盖：覆盖 40/52 页，缺 | OK | OK | OK | - | OK | OK | OK |
| HXJ 哮喘 广三.pdf | 17 | 71cc805090bd11f1a3da71efcdd7cc1f | - | 16 | 17 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | - | OK | - | OK |
| LHYA-哮喘-沈阳医大四.pdf | 7 | 4392c81a90be11f1a3da71efcdd7cc1f | - | 6 | 7 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | OK | - |
| lsju-哮喘-沈阳(1).pdf | 9 | 446d2b8690be11f1a3da71efcdd7cc1f | - | 7 | 7 | [1, 2] | ❌ 未完全覆盖：覆盖 7/9 页，缺失  | OK | - | - | OK | - | - | - |
| LXQI222.pdf | 10 | 46065ec290be11f1a3da71efcdd7cc1f | - | 5 | 10 | [] | ✅ 完全覆盖：chunk 页码并集 =  | - | OK | OK | - | OK | OK | - |
| lzga-哮喘-沈阳(1).pdf | 5 | 470cfbaa90be11f1a3da71efcdd7cc1f | - | 6 | 5 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | OK | OK | - | - | - |
| LZK 哮喘 广三(1).pdf | 16 | 5963bc44913b11f19b5e81513a69a703 | - | 15 | 16 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | - | OK | OK | - |
| LZQ 64 哮喘 深圳二院.pdf | 20 | 493f7d0890be11f1a3da71efcdd7cc1f | - | 11 | 20 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | - | - |
| MARO-四川省人民.pdf | 14 | 4b35869890be11f1a3da71efcdd7cc1f | - | 10 | 13 | [8] | ❌ 未完全覆盖：覆盖 13/14 页，缺 | OK | - | - | - | OK | - | OK |
| XALI麦济新乡 2026-03-06 17.04 (1).pdf | 27 | 3543a40e90bf11f1a3da71efcdd7cc1f | - | 12 | 12 | [5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 22, 23] | ❌ 未完全覆盖：覆盖 12/27 页，缺 | OK | OK | OK | - | OK | OK | - |
| yayu-哮喘-麦济122-沈阳-医大四(1).pdf | 6 | ab5b749290be11f1a3da71efcdd7cc1f | - | 7 | 6 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | OK | - |
| YJXI 68 哮喘 山西(1).pdf | 11 | ac1fbd9890be11f1a3da71efcdd7cc1f | - | 10 | 11 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | OK | OK | OK | OK | OK |
| YXLA（支气管哮喘）222.pdf | 19 | ad4ce53890be11f1a3da71efcdd7cc1f | - | 13 | 19 | [] | ✅ 完全覆盖：chunk 页码并集 =  | - | OK | OK | OK | OK | OK | - |
| 哮喘-HJCH222   2.27.pdf | 17 | ae83c98a90be11f1a3da71efcdd7cc1f | - | 7 | 11 | [10, 11, 12, 13, 15, 17] | ❌ 未完全覆盖：覆盖 11/17 页，缺 | OK | OK | OK | - | - | OK | - |
| 麦济WRNA(2).pdf | 9 | af8df0da90be11f1a3da71efcdd7cc1f | - | 9 | 9 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | - | - |
| 麦济WZWA222.pdf | 5 | b0745f3490be11f1a3da71efcdd7cc1f | - | 5 | 5 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | OK | - |
| 麦济ZHGL.pdf | 6 | b169d0b890be11f1a3da71efcdd7cc1f | - | 5 | 6 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | - | - |
| 麦济ZHYH.pdf | 6 | b2448c9e90be11f1a3da71efcdd7cc1f | - | 6 | 6 | [] | ✅ 完全覆盖：chunk 页码并集 =  | OK | - | - | OK | - | - | - |

判定说明：OK=该类型有 chunk 落库；LOST=SmartSplitter 已识别但最终未落库（多为 SyncChunks 同步失败）
