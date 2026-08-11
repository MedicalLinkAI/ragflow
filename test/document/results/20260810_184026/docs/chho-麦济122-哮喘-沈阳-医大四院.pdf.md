# 基准结果：chho-麦济122-哮喘-沈阳-医大四院.pdf

## 基本信息

- 文件：`chho-麦济122-哮喘-沈阳-医大四院.pdf`
- 大小：8763.4 KB
- PDF 总页数：13
- doc_id：`7168f13694a811f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T18:44:18  完成时间：2026-08-10T18:48:53  耗时：275.0s
- progress_msg：`10:48:52 Indexing done (0.11s). Task done (260.85s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 7d043227 | 1 | 1-1 | 2/4 沈阳市第四人民医院 THE FOURTH PEOPLE'S HOSPIT |
| 2 | a3f962fe | 1 | 2-2 | 中国医科大学沈阳市第四人民医院 报告单 出生日期：1983-6-17 性别：女  |
| 3 | a3e738fb | 1 | 3-3 | 中国医科大学沈阳市第四人民医院 肺功能报告单 姓名： 出生日期： 1983-6- |
| 4 | 785e0393 | 1 | 6-6 | 辽宁崇文厚德医院 门诊病历 科室：呼吸内一科门诊 姓名： 职业： 就诊日期：20 |
| 5 | e6b6e663 | 1 | 7-7 | 新药特药大药房总店 流水单号 10020045213 结账时间 2025-11- |
| 6 | 44ca8745 | 1 | 8-8 | 2/4 科 室:呼吸与危重症一门诊 诊断:(J45.900x001)支气管哮喘  |
| 7 | 30bfb8bf | 1 | 9-9 | 新药特药大药房总店 流水单号 10020044912 结账时间 2025-10- |
| 8 | 65ab6129 | 1 | 10-10 | 1/1 NO:25004949727 4号窗口 25/11/03 16:39 普 |
| 9 | 2d27c455 | 1 | 11-11 | 沈阳市第四人民医院 处方笺 医疗类别:市医保 NO:25005558582 4号 |
| 10 | 7752f4c3 | 1 | 12-12 | 新药特药大药房总店 流水单号 10020046503 结账时间 2026-01- |
| 11 | eb46b391 | 1 | 13-13 | 沈阳市第四人民医院 处方笺 医疗类别:市医保 NO:26000513029 3号 |
| 12 | 418075c8 | 2 | 4-5 | <table><tr><td>白细胞</td><td>None</td><td> |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：13
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]`
- 覆盖页数：13 / 13；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 3 | 3 | 3 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 4 | 4 | 4 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "ExaminationReport": 2, "LabReport": 1, "MedicationRecord": 3, "PrescriptionRecord": 4}`
- ChunkMerger：`{"found": true, "merged": 12, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 3, "Extractor:Prescription": 4, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2, "Extractor:Progress": 1}, "filtered_noise": 4}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 10:48:50,861 INFO     29 [ChunkMerger] Merged 12 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 10:44:23,434 INFO     29 handle_task begin for task {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 10:44:23,638 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 10:44:23,758 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 10:44:23,778 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:44:23,778 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 10:44:23,778 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 10:44:23,787 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 10:44:23,787 INFO     29 ============================================================
2026-08-10 10:44:23,787 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 10:44:23,787 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 10:44:23,787 INFO     29 ============================================================
2026-08-10 10:44:23,787 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 10:44:23,787 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 10:44:23,790 INFO     29 No torch found.
2026-08-10 10:44:25,802 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=13
2026-08-10 10:44:26,015 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=931963, prompt_len=764
2026-08-10 10:44:28,271 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-08-23"}
```
2026-08-10 10:44:28,271 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2024-08-23
2026-08-10 10:44:28,285 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=931963, prompt_len=401
2026-08-10 10:44:31,064 INFO     29 [qwen-vl-parser] text API response (len=478):
["2/4", "沈阳市第四人民医院", "THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG", "门诊病历", "业：现住址：辽宁省沈阳市皇姑区延河街", "就诊科别：呼吸与危重症医学科门诊", "就诊时间：2024-08-23 16:00", "书写时间：2024-08-23 16:59", "供史者：患者本人", "主诉：支气管哮喘开药", "现病史：患者支气管哮喘，继续巩固治疗：", "沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒", "孟鲁司特钠片", "10mg*5片，共10片", "每次10mg，QD", "睡前口服", "查体/专科查体：", "辅助检查：", "诊断：", "支气管哮喘", "处理意见：", "建议患者定期复查肺功能，肺部CT.", "我科随诊。", "建议休息天数：0天。", "患者下转：", "签名：杨昕", "患者签名：", "门诊病历专用章", "(1)", "vivo X80 此份", "书同等效力。", "2024/08/23 16:29"]
2026-08-10 10:44:31,064 INFO     29 [qwen-vl-parser] page=1 text: 32 lines (bbox 0-31)
2026-08-10 10:44:31,064 INFO     29 [qwen-vl-parser] page=1 text: 32 sections
2026-08-10 10:44:31,322 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1353736, prompt_len=764
2026-08-10 10:44:33,518 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 10:44:33,519 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 10:44:33,541 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1353736, prompt_len=401
2026-08-10 10:44:38,686 INFO     29 [qwen-vl-parser] text API response (len=851):
["16:16", "5GA", "24", "中国医科大学沈阳市第四人民医院", "报告单", "出生日期：1983-6-17", "性别：女", "住院号：890730", "年龄：42 Years", "身高：163 cm", "测试号：2025011002", "体重：70 kg", "预计 实1 %(实1/预) 实2 %(实2/预) 变异率", "Time", "14:07:", "14:26:", "FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6", "FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9", "FEV 1 % FVC [%] 69.69 74.33 6.7", "FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7", "PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5", "MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4", "MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 4.7 -6.2", "MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0", "MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V in", "医生意见：", "阻塞型轻度通气功能障碍，小气道功能障碍。", "支气管舒张试验：吸入沙丁胺醇气雾剂400微克，", "FEV1增加360毫升，改善率为16.9%。支气管舒张试验阳性。", "操作者：", "vivo X80 · ZEISS", "2025/09/19 18:09"]
2026-08-10 10:44:38,686 INFO     29 [qwen-vl-parser] page=2 text: 46 lines (bbox 32-77)
2026-08-10 10:44:38,686 INFO     29 [qwen-vl-parser] page=2 text: 46 sections
2026-08-10 10:44:38,973 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1645938, prompt_len=764
2026-08-10 10:44:40,039 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T10:44:40.037+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"71a9158694a811f1bd9827cf206dfa2d": {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 10:44:41,181 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-02"}
```
2026-08-10 10:44:41,181 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2025-09-02
2026-08-10 10:44:41,200 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1645938, prompt_len=401
2026-08-10 10:44:52,861 INFO     29 [qwen-vl-parser] text API response (len=2218):
["16:16", "5GA", "25", "<", "扫描全能王 2025-12-11 11.00.pdf", "4/4", "中国医科大学沈阳市第四人民医院", "肺功能报告单", "姓名：", "出生日期：", "1983-6-17", "住院号：", "890730", "身高：", "163 cm", "性别：", "女", "年龄：", "42 Years", "测试号：", "2025011002", "体重：", "70 kg", "Date", "Time", "预计", "实测", "%(实/预)", "25-9-02", "14:07:38", "VT", "[L]", "0.50", "BF", "[1/min]", "20.00", "MV", "[L/min]", "10.00", "ERV", "[L]", "1.07", "VC MAX", "[L]", "3.31", "3.36", "101.6", "FVC", "[L]", "3.24", "3.05", "94.1", "FEV 1", "[L]", "2.79", "2.12", "76.1", "FEV 1 % FVC", "[%]", "69.69", "FEV 1 % VC MAX", "[%]", "81.12", "63.16", "77.9", "PEF", "[L/s]", "6.59", "6.83", "103.5", "MEF 75", "[L/s]", "5.80", "3.41", "58.8", "MEF 50", "[L/s]", "4.10", "2.30", "56.2", "MEF 25", "[L/s]", "1.77", "0.45", "25.4", "MMEF 75/25", "[L/s]", "3.53", "0.95", "26.9", "MVV", "[L/min]", "103.77", "FEV 1*30", "[L/min]", "103.77", "63.70", "61.4", "RV-SB", "[L]", "1.62", "2.06", "127.2", "RV%TLC-SB", "[%]", "33.24", "40.20", "120.9", "TLC-SB", "[L]", "4.97", "5.13", "103.3", "FRC-SB", "[L]", "2.69", "2.97", "110.3", "FRC%TLC-SB", "[%]", "51.82", "57.88", "111.7", "DLCO SB", "[mmol/min/kPa]", "8.54", "5.51", "(64.6)", "医生意见：", "阻塞型轻度通气功能障碍，小气道功能障碍。", "弥散功能降低。残总比 40.20 %。", "vivo X80 · ZEISS", "2025/09/19 18:09", "操作者：", "Vol [L]", "6", "6", "TLC", "FRC", "R", "0", "Pred", "0.5", "1.0", "1.5", "2.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "1", "5", "10", "F/V in", "100", "Vol [L]", "Vol [L]", "10", "80", "60", "40", "20", "0", "0", "2", "4", "6", "8", "10", "Time [s]", "Volume [L]", "4", "2", "0", "0", "2", "4", "10", "20", "30", "40", "Time [s]", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
2026-08-10 10:44:52,861 INFO     29 [qwen-vl-parser] page=3 text: 288 lines (bbox 78-365)
2026-08-10 10:44:52,861 INFO     29 [qwen-vl-parser] page=3 text: 288 sections
2026-08-10 10:44:52,971 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=663828, prompt_len=764
2026-08-10 10:44:54,446 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-09-02"
}
```
2026-08-10 10:44:54,446 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-09-02
2026-08-10 10:44:54,461 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=663828, prompt_len=756
2026-08-10 10:44:57,182 INFO     29 [qwen-vl-parser] table API response (len=499):
\begin{tabular}{l r l l}
\hline
检查项目 & 结果 & 单位 & 参考值 \\
\hline
白细胞 & 8.40 & 10^9/L & 3.5--9.5 \\
红细胞 & 4.94 & 10^12/L & 3.8--5.1 \\
血红蛋白 & 138 & g/L & 115--150 \\
血小板 & 300 & 10^9/L & 125--350 \\
红细胞压积 & 41.30 & \% & 35--45 \\
红细胞平均体积 & 83.60 & fL & 82--100 \\
平均血红蛋白量 & 28.00 & pg & 27--34 \\
平均血红蛋白浓 & 334 & g/L & 316--354 \\
度 & & & \\
中性粒细胞比率 & 54.20 & \% & 40--75 \\
淋巴细胞比率 & 36.10 & \% & 20--50 \\
单核细胞比率 & 3.70 & \% & 3--10 \\
嗜酸性粒细胞比 & 5.50 & \% & 0.4--8.0 \\
率 & & & \\
\hline
\end{tabular}
2026-08-10 10:44:57,184 INFO     29 [qwen-vl-parser] page=4 table: 21 LaTeX lines (bbox 366-386)
2026-08-10 10:44:57,184 INFO     29 [qwen-vl-parser] page=4 table: 21 sections
2026-08-10 10:44:57,319 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=870835, prompt_len=764
2026-08-10 10:44:58,726 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 10:44:58,727 INFO     29 [qwen-vl-parser] page=5 classify=table report_date=None
2026-08-10 10:44:58,741 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=870835, prompt_len=756
2026-08-10 10:45:03,623 INFO     29 [qwen-vl-parser] table API response (len=957):
\begin{tabular}{cccccc}
\hline
& & & & & \\
红细胞 & 4.94 & 10^12/L & 3.8--5.1 & & \\
血红蛋白 & 138 & g/L & 115--150 & & \\
血小板 & 300 & 10^9/L & 125--350 & & \\
红细胞压积 & 41.30 & \% & 35--45 & & \\
红细胞平均体积 & 83.60 & fL & 82--100 & & \\
平均血红蛋白量 & 28.00 & pg & 27--34 & & \\
平均血红蛋白浓 & 334 & g/L & 316--354 & & \\
度 & & & & & \\
中性粒细胞比率 & 54.20 & \% & 40--75 & & \\
淋巴细胞比率 & 36.10 & \% & 20--50 & & \\
单核细胞比率 & 3.70 & \% & 3--10 & & \\
嗜酸性粒细胞比 & 5.50 & \% & 0.4--8.0 & & \\
率 & & & & & \\
嗜碱性粒细胞比 & 0.50 & \% & 0--1 & & \\
率 & & & & & \\
中性粒细胞数 & 4.56 & 10^9/L & 1.8--6.3 & & \\
淋巴细胞数 & 3.03 & 10^9/L & 1.1--3.2 & & \\
单核细胞数 & 0.31 & 10^9/L & 0.10--0.60 & & \\
嗜酸性粒细胞 & 0.46 & 10^9/L & 0.02--0.52 & & \\
嗜碱性粒细胞 & 0.04 & 10^9/L & 0--0.06 & & \\
红细胞分布宽度 & 12.9 & \% & 11.0--16.0 & & \\
变异系数 & & & & & \\
血小板分布宽度 & 16.5 & fL & 8.0--18.1 & & \\
平均血小板体积 & 10.2 & fL & 9--13 & & \\
血小板压积 & 0.31 & \% & 0.10--0.28 & & \\
C反应蛋白 & 7.92 & mg/L & 0--6 & & \\
\hline
\end{tabular}
2026-08-10 10:45:03,625 INFO     29 [qwen-vl-parser] page=5 table: 31 LaTeX lines (bbox 387-417)
2026-08-10 10:45:03,625 INFO     29 [qwen-vl-parser] page=5 table: 31 sections
2026-08-10 10:45:04,066 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2162983, prompt_len=764
2026-08-10 10:45:05,837 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 10:45:05,837 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 10:45:05,849 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2162983, prompt_len=401
2026-08-10 10:45:08,738 INFO     29 [qwen-vl-parser] text API response (len=452):
["辽宁崇文厚德医院", "门诊病历", "科室：呼吸内一科门诊", "姓名：", "职业：", "就诊日期：2025/11/08 10:11:23", "主诉：反复喘息2年，加重1周", "现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万", "林”治疗，症状稍有改善，为求进一步诊治来我院就诊。", "既往史：否认。", "过敏史：{无}", "体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。", "辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试", "性。", "抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.", "初步诊断：1、支气管哮喘 急性发作期", "处理：", "1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。", "2.1周后复诊，病情变化随诊。", "医生签名：王春", "王春", "日", "第 1 页"]
2026-08-10 10:45:08,738 INFO     29 [qwen-vl-parser] page=6 text: 23 lines (bbox 418-440)
2026-08-10 10:45:08,738 INFO     29 [qwen-vl-parser] page=6 text: 23 sections
2026-08-10 10:45:09,177 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2233042, prompt_len=764
2026-08-10 10:45:10,465 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 10:45:10,465 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 10:45:10,480 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2233042, prompt_len=401
2026-08-10 10:45:11,018 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T10:45:11.017+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"71a9158694a811f1bd9827cf206dfa2d": {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 10:45:12,431 INFO     29 [qwen-vl-parser] text API response (len=263):
["新药特药大药房总店", "流水单号 10020045213", "结账时间 2025-11-08 15:22:19", "编号 数量 单价 金额 营业员", "甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It", "Sr1/库存2", "0310145 2 盒 34.00 68.00", "合计 68.00", "优惠：0.00 微信：0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据，药品为特殊、", "商品，售出概不退还！"]
2026-08-10 10:45:12,431 INFO     29 [qwen-vl-parser] page=7 text: 16 lines (bbox 441-456)
2026-08-10 10:45:12,431 INFO     29 [qwen-vl-parser] page=7 text: 16 sections
2026-08-10 10:45:12,613 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=769833, prompt_len=764
2026-08-10 10:45:14,063 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-19"}
```
2026-08-10 10:45:14,064 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-09-19
2026-08-10 10:45:14,077 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=769833, prompt_len=401
2026-08-10 10:45:16,216 INFO     29 [qwen-vl-parser] text API response (len=315):
["2/4", "科 室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "孟鲁司特钠片【舒宁安】乙", "超量说明:", "【10mg*5片】", "(4.96元/盒)", "3盒", "用法用量:每次10mg,睡前口服,每天一次", "医师:杨沂发药:修泉涌配药:沈瑶", "vivo X80 · ZEISS", "计:208.48/208.48", "第1页/共1页", "2025/09/19 18:04"]
2026-08-10 10:45:16,216 INFO     29 [qwen-vl-parser] page=8 text: 19 lines (bbox 457-475)
2026-08-10 10:45:16,216 INFO     29 [qwen-vl-parser] page=8 text: 19 sections
2026-08-10 10:45:16,344 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=951955, prompt_len=764
2026-08-10 10:45:17,745 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 10:45:17,745 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 10:45:17,753 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=951955, prompt_len=401
2026-08-10 10:45:19,702 INFO     29 [qwen-vl-parser] text API response (len=274):
["新药特药大药房总店", "流水单号 10020044912", "结账时间 2025-10-14 08:34:01", "编号 数量 单价 金额 营业员", "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug", "泡/葛兰素史克(集团)/库存1", "0200127 1 盒 199.00 199.00", "合计 199.00", "优惠:0.00 微信:0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据,药品为特殊、", "商品,售出概不退还!"]
2026-08-10 10:45:19,702 INFO     29 [qwen-vl-parser] page=9 text: 16 lines (bbox 476-491)
2026-08-10 10:45:19,702 INFO     29 [qwen-vl-parser] page=9 text: 16 sections
2026-08-10 10:45:19,883 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=759977, prompt_len=764
2026-08-10 10:45:22,237 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 10:45:22,237 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 10:45:22,248 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=759977, prompt_len=401
2026-08-10 10:45:24,317 INFO     29 [qwen-vl-parser] text API response (len=303):
["1/1", "NO:25004949727", "4号窗口", "25/11/03 16:39", "普通", "病志号:55161248", "科", "室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "医师:杨昕发药:沈瑶配药:巴艺洁", "vivo X80 · ZEISS", "金额合计:193.6/193.6", "第1页/共1页", "2025/11/05 14:51"]
2026-08-10 10:45:24,318 INFO     29 [qwen-vl-parser] page=10 text: 19 lines (bbox 492-510)
2026-08-10 10:45:24,318 INFO     29 [qwen-vl-parser] page=10 text: 19 sections
2026-08-10 10:45:24,608 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1190809, prompt_len=764
2026-08-10 10:45:26,010 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 10:45:26,011 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 10:45:26,028 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1190809, prompt_len=401
2026-08-10 10:45:28,092 INFO     29 [qwen-vl-parser] text API response (len=304):
["沈阳市第四人民医院", "处方笺", "医疗类别:市医保", "NO:25005558582", "4号窗口", "25/12/08 14:00", "普通", "病志号:55161248", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "vivo X80 · ZEISS", "医师:杨昕发药:李琳配药:巴艺洁", "2025/12/31 18:28金额合计:193.6/193.6", "第1页/共1页"]
2026-08-10 10:45:28,092 INFO     29 [qwen-vl-parser] page=11 text: 18 lines (bbox 511-528)
2026-08-10 10:45:28,092 INFO     29 [qwen-vl-parser] page=11 text: 18 sections
2026-08-10 10:45:28,472 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1883034, prompt_len=764
2026-08-10 10:45:29,606 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 10:45:29,607 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-10 10:45:29,620 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1883034, prompt_len=401
2026-08-10 10:45:31,658 INFO     29 [qwen-vl-parser] text API response (len=269):
["新药特药大药房总店", "流水单号 10020046503", "结账时间 2026-01-02 18:12:29", "编号 数量 单价 金额 营业员", "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:", "泡/葛兰素史克(集团)/库存1", "0200127 1 盒 199.00 199.00", "合计 199.00", "优惠:0.00 微信:0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据,药品为特殊、", "商品,售出概不退还!"]
2026-08-10 10:45:31,658 INFO     29 [qwen-vl-parser] page=12 text: 16 lines (bbox 529-544)
2026-08-10 10:45:31,659 INFO     29 [qwen-vl-parser] page=12 text: 16 sections
2026-08-10 10:45:31,966 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1396520, prompt_len=764
2026-08-10 10:45:33,435 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 10:45:33,435 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 10:45:33,456 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1396520, prompt_len=401
2026-08-10 10:45:35,345 INFO     29 [qwen-vl-parser] text API response (len=270):
["沈阳市第四人民医院", "处方笺", "医疗类别:市医保", "NO:26000513029", "3号窗口", "26/01/30 13:26", "普通", "科 室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "医师:杨昕发药:李琳 配药:乔军", "金额合计:193.6/193.6", "第1页/共1页"]
2026-08-10 10:45:35,345 INFO     29 [qwen-vl-parser] page=13 text: 17 lines (bbox 545-561)
2026-08-10 10:45:35,345 INFO     29 [qwen-vl-parser] page=13 text: 17 sections
2026-08-10 10:45:35,345 INFO     29 [qwen-vl-parser] parse_pdf done: 562 sections from 13 pages.
2026-08-10 10:45:35,356 INFO     29 Close text detector.
2026-08-10 10:45:35,766 INFO     29 Close text recognizer.
2026-08-10 10:45:36,157 INFO     29 Close recognizer.
2026-08-10 10:45:36,559 INFO     29 Close recognizer.
2026-08-10 10:45:36,996 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 10:45:36,997 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Parser:MedLink | outputs={"html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "json"}
2026-08-10 10:45:36,997 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 10:45:37,025 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:45:37,025 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 2/4\n[BBOX-1] 沈阳市第四人民医院\n[BBOX-2] THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG\n[BBOX-3] 门诊病历\n[BBOX-4] 业：现住址：辽宁省沈阳市皇姑区延河街\n[BBOX-5] 就诊科别：呼吸与危重症医学科门诊\n[BBOX-6] 就诊时间：2024-08-23 16:00\n[BBOX-7] 书写时间：2024-08-23 16:59\n[BBOX-8] 供史者：患者本人\n[BBOX-9] 主诉：支气管哮喘开药\n[BBOX-10] 现病史：患者支气管哮喘，继续巩固治疗：\n[BBOX-11] 沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒\n[BBOX-12] 孟鲁司特钠片\n[BBOX-13] 10mg*5片，共10片\n[BBOX-14] 每次10mg，QD\n[BBOX-15] 睡前口服\n[BBOX-16] 查体/专科查体：\n[BBOX-17] 辅助检查：\n[BBOX-18] 诊断：\n[BBOX-19] 支气管哮喘\n[BBOX-20] 处理意见：\n[BBOX-21] 建议患者定期复查肺功能，肺部CT.\n[BBOX-22] 我科随诊。\n[BBOX-23] 建议休息天数：0天。\n[BBOX-24] 患者下转：\n[BBOX-25] 签名：杨昕\n[BBOX-26] 患者签名：\n[BBOX-27] 门诊病历专用章\n[BBOX-28] (1)\n[BBOX-29] vivo X80 此份\n[BBOX-30] 书同等效力。\n[BBOX-31] 2024/08/23 16:29\n[BBOX-32] 16:16\n[BBOX-33] 5GA\n[BBOX-34] 24\n[BBOX-35] 中国医科大学沈阳市第四人民医院\n[BBOX-36] 报告单\n[BBOX-37] 出生日期：1983-6-17\n[BBOX-38] 性别：女\n[BBOX-39] 住院号：890730\n[BBOX-40] 年龄：42 Years\n[BBOX-41] 身高：163 cm\n[BBOX-42] 测试号：2025011002\n[BBOX-43] 体重：70 kg\n[BBOX-44] 预计 实1 %(实1/预) 实2 %(实2/预) 变异率\n[BBOX-45] Time\n[BBOX-46] 14:07:\n[BBOX-47] 14:26:\n[BBOX-48] FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6\n[BBOX-49] FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9\n[BBOX-50] FEV 1 % FVC [%] 69.69 74.33 6.7\n[BBOX-51] FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7\n[BBOX-52] PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5\n[BBOX-53] MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4\n[BBOX-54] MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 4.7 -6.2\n[BBOX-55] MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0\n[BBOX-56] MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1\n[BBOX-57] Flow [L/s]\n[BBOX-58] F/V ex\n[BBOX-59] 10\n[BBOX-60] 5\n[BBOX-61] 0\n[BBOX-62] 1\n[BBOX-63] 2\n[BBOX-64] 3\n[BBOX-65] 4\n[BBOX-66] 5\n[BBOX-67] 6\n[BBOX-68] 7\n[BBOX-69] 10\n[BBOX-70] F/V in\n[BBOX-71] 医生意见：\n[BBOX-72] 阻塞型轻度通气功能障碍，小气道功能障碍。\n[BBOX-73] 支气管舒张试验：吸入沙丁胺醇气雾剂400微克，\n[BBOX-74] FEV1增加360毫升，改善率为16.9%。支气管舒张试验阳性。\n[BBOX-75] 操作者：\n[BBOX-76] vivo X80 · ZEISS\n[BBOX-77] 2025/09/19 18:09\n[BBOX-78] 16:16\n[BBOX-79] 5GA\n[BBOX-80] 25\n[BBOX-81] <\n[BBOX-82] 扫描全能王 2025-12-11 11.00.pdf\n[BBOX-83] 4/4\n[BBOX-84] 中国医科大学沈阳市第四人民医院\n[BBOX-85] 肺功能报告单\n[BBOX-86] 姓名：\n[BBOX-87] 出生日期：\n[BBOX-88] 1983-6-17\n[BBOX-89] 住院号：\n[BBOX-90] 890730\n[BBOX-91] 身高：\n[BBOX-92] 163 cm\n[BBOX-93] 性别：\n[BBOX-94] 女\n[BBOX-95] 年龄：\n[BBOX-96] 42 Years\n[BBOX-97] 测试号：\n[BBOX-98] 2025011002\n[BBOX-99] 体重：\n[BBOX-100] 70 kg\n[BBOX-101] Date\n[BBOX-102] Time\n[BBOX-103] 预计\n[BBOX-104] 实测\n[BBOX-105] %(实/预)\n[BBOX-106] 25-9-02\n[BBOX-107] 14:07:38\n[BBOX-108] VT\n[BBOX-109] [L]\n[BBOX-110] 0.50\n[BBOX-111] BF\n[BBOX-112] [1/min]\n[BBOX-113] 20.00\n[BBOX-114] MV\n[BBOX-115] [L/min]\n[BBOX-116] 10.00\n[BBOX-117] ERV\n[BBOX-118] [L]\n[BBOX-119] 1.07\n[BBOX-120] VC MAX\n[BBOX-121] [L]\n[BBOX-122] 3.31\n[BBOX-123] 3.36\n[BBOX-124] 101.6\n[BBOX-125] FVC\n[BBOX-126] [L]\n[BBOX-127] 3.24\n[BBOX-128] 3.05\n[BBOX-129] 94.1\n[BBOX-130] FEV 1\n[BBOX-131] [L]\n[BBOX-132] 2.79\n[BBOX-133] 2.12\n[BBOX-134] 76.1\n[BBOX-135] FEV 1 % FVC\n[BBOX-136] [%]\n[BBOX-137] 69.69\n[BBOX-138] FEV 1 % VC MAX\n[BBOX-139] [%]\n[BBOX-140] 81.12\n[BBOX-141] 63.16\n[BBOX-142] 77.9\n[BBOX-143] PEF\n[BBOX-144] [L/s]\n[BBOX-145] 6.59\n[BBOX-146] 6.83\n[BBOX-147] 103.5\n[BBOX-148] MEF 75\n[BBOX-149] [L/s]\n[BBOX-150] 5.80\n[BBOX-151] 3.41\n[BBOX-152] 58.8\n[BBOX-153] MEF 50\n[BBOX-154] [L/s]\n[BBOX-155] 4.10\n[BBOX-156] 2.30\n[BBOX-157] 56.2\n[BBOX-158] MEF 25\n[BBOX-159] [L/s]\n[BBOX-160] 1.77\n[BBOX-161] 0.45\n[BBOX-162] 25.4\n[BBOX-163] MMEF 75/25\n[BBOX-164] [L/s]\n[BBOX-165] 3.53\n[BBOX-166] 0.95\n[BBOX-167] 26.9\n[BBOX-168] MVV\n[BBOX-169] [L/min]\n[BBOX-170] 103.77\n[BBOX-171] FEV 1*30\n[BBOX-172] [L/min]\n[BBOX-173] 103.77\n[BBOX-174] 63.70\n[BBOX-175] 61.4\n[BBOX-176] RV-SB\n[BBOX-177] [L]\n[BBOX-178] 1.62\n[BBOX-179] 2.06\n[BBOX-180] 127.2\n[BBOX-181] RV%TLC-SB\n[BBOX-182] [%]\n[BBOX-183] 33.24\n[BBOX-184] 40.20\n[BBOX-185] 120.9\n[BBOX-186] TLC-SB\n[BBOX-187] [L]\n[BBOX-188] 4.97\n[BBOX-189] 5.13\n[BBOX-190] 103.3\n[BBOX-191] FRC-SB\n[BBOX-192] [L]\n[BBOX-193] 2.69\n[BBOX-194] 2.97\n[BBOX-195] 110.3\n[BBOX-196] FRC%TLC-SB\n[BBOX-197] [%]\n[BBOX-198] 51.82\n[BBOX-199] 57.88\n[BBOX-200] 111.7\n[BBOX-201] DLCO SB\n[BBOX-202] [mmol/min/kPa]\n[BBOX-203] 8.54\n[BBOX-204] 5.51\n[BBOX-205] (64.6)\n[BBOX-206] 医生意见：\n[BBOX-207] 阻塞型轻度通气功能障碍，小气道功能障碍。\n[BBOX-208] 弥散功能降低。残总比 40.20 %。\n[BBOX-209] vivo X80 · ZEISS\n[BBOX-210] 2025/09/19 18:09\n[BBOX-211] 操作者：\n[BBOX-212] Vol [L]\n[BBOX-213] 6\n[BBOX-214] 6\n[BBOX-215] TLC\n[BBOX-216] FRC\n[BBOX-217] R\n[BBOX-218] 0\n[BBOX-219] Pred\n[BBOX-220] 0.5\n[BBOX-221] 1.0\n[BBOX-222] 1.5\n[BBOX-223] 2.0\n[BBOX-224] Time [min]\n[BBOX-225] Flow [L/s]\n[BBOX-226] F/V ex\n[BBOX-227] 10\n[BBOX-228] 5\n[BBOX-229] 0\n[BBOX-230] 2\n[BBOX-231] 4\n[BBOX-232] 6\n[BBOX-233] 1\n[BBOX-234] 5\n[BBOX-235] 10\n[BBOX-236] F/V in\n[BBOX-237] 100\n[BBOX-238] Vol [L]\n[BBOX-239] Vol [L]\n[BBOX-240] 10\n[BBOX-241] 80\n[BBOX-242] 60\n[BBOX-243] 40\n[BBOX-244] 20\n[BBOX-245] 0\n[BBOX-246] 0\n[BBOX-247] 2\n[BBOX-248] 4\n[BBOX-249] 6\n[BBOX-250] 8\n[BBOX-251] 10\n[BBOX-252] Time [s]\n[BBOX-253] Volume [L]\n[BBOX-254] 4\n[BBOX-255] 2\n[BBOX-256] 0\n[BBOX-257] 0\n[BBOX-258] 2\n[BBOX-259] 4\n[BBOX-260] 10\n[BBOX-261] 20\n[BBOX-262] 30\n[BBOX-263] 40\n[BBOX-264] Time [s]\n[BBOX-265] 0\n[BBOX-266] 1\n[BBOX-267] 2\n[BBOX-268] 3\n[BBOX-269] 4\n[BBOX-270] 5\n[BBOX-271] 6\n[BBOX-272] 7\n[BBOX-273] 8\n[BBOX-274] 9\n[BBOX-275] 10\n[BBOX-276] 11\n[BBOX-277] 12\n[BBOX-278] 13\n[BBOX-279] 14\n[BBOX-280] 15\n[BBOX-281] 16\n[BBOX-282] 17\n[BBOX-283] 18\n[BBOX-284] 19\n[BBOX-285] 20\n[BBOX-286] 21\n[BBOX-287] 22\n[BBOX-288] 23\n[BBOX-289] 24\n[BBOX-290] 25\n[BBOX-291] 26\n[BBOX-292] 27\n[BBOX-293] 28\n[BBOX-294] 29\n[BBOX-295] 30\n[BBOX-296] 31\n[BBOX-297] 32\n[BBOX-298] 33\n[BBOX-299] 34\n[BBOX-300] 35\n[BBOX-301] 36\n[BBOX-302] 37\n[BBOX-303] 38\n[BBOX-304] 39\n[BBOX-305] 40\n[BBOX-306] 41\n[BBOX-307] 42\n[BBOX-308] 43\n[BBOX-309] 44\n[BBOX-310] 45\n[BBOX-311] 46\n[BBOX-312] 47\n[BBOX-313] 48\n[BBOX-314] 49\n[BBOX-315] 50\n[BBOX-316] 51\n[BBOX-317] 52\n[BBOX-318] 53\n[BBOX-319] 54\n[BBOX-320] 55\n[BBOX-321] 56\n[BBOX-322] 57\n[BBOX-323] 58\n[BBOX-324] 59\n[BBOX-325] 60\n[BBOX-326] 61\n[BBOX-327] 62\n[BBOX-328] 63\n[BBOX-329] 64\n[BBOX-330] 65\n[BBOX-331] 66\n[BBOX-332] 67\n[BBOX-333] 68\n[BBOX-334] 69\n[BBOX-335] 70\n[BBOX-336] 71\n[BBOX-337] 72\n[BBOX-338] 73\n[BBOX-339] 74\n[BBOX-340] 75\n[BBOX-341] 76\n[BBOX-342] 77\n[BBOX-343] 78\n[BBOX-344] 79\n[BBOX-345] 80\n[BBOX-346] 81\n[BBOX-347] 82\n[BBOX-348] 83\n[BBOX-349] 84\n[BBOX-350] 85\n[BBOX-351] 86\n[BBOX-352] 87\n[BBOX-353] 88\n[BBOX-354] 89\n[BBOX-355] 90\n[BBOX-356] 91\n[BBOX-357] 92\n[BBOX-358] 93\n[BBOX-359] 94\n[BBOX-360] 95\n[BBOX-361] 96\n[BBOX-362] 97\n[BBOX-363] 98\n[BBOX-364] 99\n[BBOX-365] 100\n[BBOX-366] \\begin{tabular}{l r l l}\n[BBOX-367] 报告时间: 2025-09-02\n[BBOX-368] \\hline\n[BBOX-369] 检查项目 & 结果 & 单位 & 参考值 \\\\\n[BBOX-370] \\hline\n[BBOX-371] 白细胞 & 8.40 & 10^9/L & 3.5--9.5 \\\\\n[BBOX-372] 红细胞 & 4.94 & 10^12/L & 3.8--5.1 \\\\\n[BBOX-373] 血红蛋白 & 138 & g/L & 115--150 \\\\\n[BBOX-374] 血小板 & 300 & 10^9/L & 125--350 \\\\\n[BBOX-375] 红细胞压积 & 41.30 & \\% & 35--45 \\\\\n[BBOX-376] 红细胞平均体积 & 83.60 & fL & 82--100 \\\\\n[BBOX-377] 平均血红蛋白量 & 28.00 & pg & 27--34 \\\\\n[BBOX-378] 平均血红蛋白浓 & 334 & g/L & 316--354 \\\\\n[BBOX-379] 度 & & & \\\\\n[BBOX-380] 中性粒细胞比率 & 54.20 & \\% & 40--75 \\\\\n[BBOX-381] 淋巴细胞比率 & 36.10 & \\% & 20--50 \\\\\n[BBOX-382] 单核细胞比率 & 3.70 & \\% & 3--10 \\\\\n[BBOX-383] 嗜酸性粒细胞比 & 5.50 & \\% & 0.4--8.0 \\\\\n[BBOX-384] 率 & & & \\\\\n[BBOX-385] \\hline\n[BBOX-386] \\end{tabular}\n[BBOX-387] \\begin{tabular}{cccccc}\n[BBOX-388] \\hline\n[BBOX-389] & & & & & \\\\\n[BBOX-390] 红细胞 & 4.94 & 10^12/L & 3.8--5.1 & & \\\\\n[BBOX-391] 血红蛋白 & 138 & g/L & 115--150 & & \\\\\n[BBOX-392] 血小板 & 300 & 10^9/L & 125--350 & & \\\\\n[BBOX-393] 红细胞压积 & 41.30 & \\% & 35--45 & & \\\\\n[BBOX-394] 红细胞平均体积 & 83.60 & fL & 82--100 & & \\\\\n[BBOX-395] 平均血红蛋白量 & 28.00 & pg & 27--34 & & \\\\\n[BBOX-396] 平均血红蛋白浓 & 334 & g/L & 316--354 & & \\\\\n[BBOX-397] 度 & & & & & \\\\\n[BBOX-398] 中性粒细胞比率 & 54.20 & \\% & 40--75 & & \\\\\n[BBOX-399] 淋巴细胞比率 & 36.10 & \\% & 20--50 & & \\\\\n[BBOX-400] 单核细胞比率 & 3.70 & \\% & 3--10 & & \\\\\n[BBOX-401] 嗜酸性粒细胞比 & 5.50 & \\% & 0.4--8.0 & & \\\\\n[BBOX-402] 率 & & & & & \\\\\n[BBOX-403] 嗜碱性粒细胞比 & 0.50 & \\% & 0--1 & & \\\\\n[BBOX-404] 率 & & & & & \\\\\n[BBOX-405] 中性粒细胞数 & 4.56 & 10^9/L & 1.8--6.3 & & \\\\\n[BBOX-406] 淋巴细胞数 & 3.03 & 10^9/L & 1.1--3.2 & & \\\\\n[BBOX-407] 单核细胞数 & 0.31 & 10^9/L & 0.10--0.60 & & \\\\\n[BBOX-408] 嗜酸性粒细胞 & 0.46 & 10^9/L & 0.02--0.52 & & \\\\\n[BBOX-409] 嗜碱性粒细胞 & 0.04 & 10^9/L & 0--0.06 & & \\\\\n[BBOX-410] 红细胞分布宽度 & 12.9 & \\% & 11.0--16.0 & & \\\\\n[BBOX-411] 变异系数 & & & & & \\\\\n[BBOX-412] 血小板分布宽度 & 16.5 & fL & 8.0--18.1 & & \\\\\n[BBOX-413] 平均血小板体积 & 10.2 & fL & 9--13 & & \\\\\n[BBOX-414] 血小板压积 & 0.31 & \\% & 0.10--0.28 & & \\\\\n[BBOX-415] C反应蛋白 & 7.92 & mg/L & 0--6 & & \\\\\n[BBOX-416] \\hline\n[BBOX-417] \\end{tabular}\n[BBOX-418] 辽宁崇文厚德医院\n[BBOX-419] 门诊病历\n[BBOX-420] 科室：呼吸内一科门诊\n[BBOX-421] 姓名：\n[BBOX-422] 职业：\n[BBOX-423] 就诊日期：2025/11/08 10:11:23\n[BBOX-424] 主诉：反复喘息2年，加重1周\n[BBOX-425] 现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万\n[BBOX-426] 林”治疗，症状稍有改善，为求进一步诊治来我院就诊。\n[BBOX-427] 既往史：否认。\n[BBOX-428] 过敏史：{无}\n[BBOX-429] 体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。\n[BBOX-430] 辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试\n[BBOX-431] 性。\n[BBOX-432] 抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.\n[BBOX-433] 初步诊断：1、支气管哮喘 急性发作期\n[BBOX-434] 处理：\n[BBOX-435] 1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。\n[BBOX-436] 2.1周后复诊，病情变化随诊。\n[BBOX-437] 医生签名：王春\n[BBOX-438] 王春\n[BBOX-439] 日\n[BBOX-440] 第 1 页\n[BBOX-441] 新药特药大药房总店\n[BBOX-442] 流水单号 10020045213\n[BBOX-443] 结账时间 2025-11-08 15:22:19\n[BBOX-444] 编号 数量 单价 金额 营业员\n[BBOX-445] 甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It\n[BBOX-446] Sr1/库存2\n[BBOX-447] 0310145 2 盒 34.00 68.00\n[BBOX-448] 合计 68.00\n[BBOX-449] 优惠：0.00 微信：0.00\n[BBOX-450] 收银 1002\n[BBOX-451] 银台\n[BBOX-452] 会员\n[BBOX-453] 本次积分 0.00\n[BBOX-454] 累计积分 0.00\n[BBOX-455] 此票为开发票依据，药品为特殊、\n[BBOX-456] 商品，售出概不退还！\n[BBOX-457] 2/4\n[BBOX-458] 科 室:呼吸与危重症一门诊\n[BBOX-459] 诊断:(J45.900x001)支气管哮喘\n[BBOX-460] Rp\n[BBOX-461] 沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n[BBOX-462] 【50ug:250ug/泡*60泡/(193.60元/盒)\n[BBOX-463] 1盒\n[BBOX-464] 用法用量:每次300ug,吸入,每天二次\n[BBOX-465] 孟鲁司特钠片【舒宁安】乙\n[BBOX-466] 超量说明:\n[BBOX-467] 【10mg*5片】\n[BBOX-468] (4.96元/盒)\n[BBOX-469] 3盒\n[BBOX-470] 用法用量:每次10mg,睡前口服,每天一次\n[BBOX-471] 医师:杨沂发药:修泉涌配药:沈瑶\n[BBOX-472] vivo X80 · ZEISS\n[BBOX-473] 计:208.48/208.48\n[BBOX-474] 第1页/共1页\n[BBOX-475] 2025/09/19 18:04\n[BBOX-476] 新药特药大药房总店\n[BBOX-477] 流水单号 10020044912\n[BBOX-478] 结账时间 2025-10-14 08:34:01\n[BBOX-479] 编号 数量 单价 金额 营业员\n[BBOX-480] 沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug\n[BBOX-481] 泡/葛兰素史克(集团)/库存1\n[BBOX-482] 0200127 1 盒 199.00 199.00\n[BBOX-483] 合计 199.00\n[BBOX-484] 优惠:0.00 微信:0.00\n[BBOX-485] 收银 1002\n[BBOX-486] 银台\n[BBOX-487] 会员\n[BBOX-488] 本次积分 0.00\n[BBOX-489] 累计积分 0.00\n[BBOX-490] 此票为开发票依据,药品为特殊、\n[BBOX-491] 商品,售出概不退还!\n[BBOX-492] 1/1\n[BBOX-493] NO:25004949727\n[BBOX-494] 4号窗口\n[BBOX-495] 25/11/03 16:39\n[BBOX-496] 普通\n[BBOX-497] 病志号:55161248\n[BBOX-498] 科\n[BBOX-499] 室:呼吸与危重症一门诊\n[BBOX-500] 诊断:(J45.900x001)支气管哮喘\n[BBOX-501] Rp\n[BBOX-502] 沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n[BBOX-503] 【50ug:250ug/泡*60泡/(193.60元/盒)\n[BBOX-504] 1盒\n[BBOX-505] 用法用量:每次300ug,吸入,每天二次\n[BBOX-506] 医师:杨昕发药:沈瑶配药:巴艺洁\n[BBOX-507] vivo X80 · ZEISS\n[BBOX-508] 金额合计:193.6/193.6\n[BBOX-509] 第1页/共1页\n[BBOX-510] 2025/11/05 14:51\n[BBOX-511] 沈阳市第四人民医院\n[BBOX-512] 处方笺\n[BBOX-513] 医疗类别:市医保\n[BBOX-514] NO:25005558582\n[BBOX-515] 4号窗口\n[BBOX-516] 25/12/08 14:00\n[BBOX-517] 普通\n[BBOX-518] 病志号:55161248\n[BBOX-519] 诊断:(J45.900x001)支气管哮喘\n[BBOX-520] Rp\n[BBOX-521] 沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n[BBOX-522] 【50ug:250ug/泡*60泡/(193.60元/盒)\n[BBOX-523] 1盒\n[BBOX-524] 用法用量:每次300ug,吸入,每天二次\n[BBOX-525] vivo X80 · ZEISS\n[BBOX-526] 医师:杨昕发药:李琳配药:巴艺洁\n[BBOX-527] 2025/12/31 18:28金额合计:193.6/193.6\n[BBOX-528] 第1页/共1页\n[BBOX-529] 新药特药大药房总店\n[BBOX-530] 流水单号 10020046503\n[BBOX-531] 结账时间 2026-01-02 18:12:29\n[BBOX-532] 编号 数量 单价 金额 营业员\n[BBOX-533] 沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:\n[BBOX-534] 泡/葛兰素史克(集团)/库存1\n[BBOX-535] 0200127 1 盒 199.00 199.00\n[BBOX-536] 合计 199.00\n[BBOX-537] 优惠:0.00 微信:0.00\n[BBOX-538] 收银 1002\n[BBOX-539] 银台\n[BBOX-540] 会员\n[BBOX-541] 本次积分 0.00\n[BBOX-542] 累计积分 0.00\n[BBOX-543] 此票为开发票依据,药品为特殊、\n[BBOX-544] 商品,售出概不退还!\n[BBOX-545] 沈阳市第四人民医院\n[BBOX-546] 处方笺\n[BBOX-547] 医疗类别:市医保\n[BBOX-548] NO:26000513029\n[BBOX-549] 3号窗口\n[BBOX-550] 26/01/30 13:26\n[BBOX-551] 普通\n[BBOX-552] 科 室:呼吸与危重症一门诊\n[BBOX-553] 诊断:(J45.900x001)支气管哮喘\n[BBOX-554] Rp\n[BBOX-555] 沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙\n[BBOX-556] 【50ug:250ug/泡*60泡/(193.60元/盒)\n[BBOX-557] 1盒\n[BBOX-558] 用法用量:每次300ug,吸入,每天二次\n[BBOX-559] 医师:杨昕发药:李琳 配药:乔军\n[BBOX-560] 金额合计:193.6/193.6\n[BBOX-561] 第1页/共1页"
  }
]
2026-08-10 10:45:41,984 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T10:45:41.983+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"71a9158694a811f1bd9827cf206dfa2d": {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 10:45:50,136 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:45:50,162 INFO     29 [SmartSplitter] SmartSplitter done: 12 chunks from 12 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'ExaminationReport': 2, 'LabReport': 1, 'MedicationRecord': 3, 'PrescriptionRecord': 4}
2026-08-10 10:45:50,177 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 10:45:50,177 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks": "12 items, types={'OutpatientRecord': 2, 'ExaminationReport': 2, 'LabReport': 1, 'MedicationRecord': 3, 'PrescriptionRecord': 4}"}
2026-08-10 10:45:50,177 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 10:45:50,178 INFO     29 [ChunkRouter] Routed 12 chunks into 5 groups: {'chunks_Clinical': 2, 'chunks_Examination': 2, 'chunks_LabExam': 1, 'chunks_Medication': 3, 'chunks_Prescription': 4}
2026-08-10 10:45:50,189 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 10:45:50,189 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | ChunkRouter:Router | outputs={"html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks": "12 items, types={'OutpatientRecord': 2, 'ExaminationReport': 2, 'LabReport': 1, 'MedicationRecord': 3, 'PrescriptionRecord': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:45:50,189 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 10:45:50,198 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:45:50,198 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:45:50,199 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3, 4]
2026-08-10 10:45:50,199 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:45:50,404 INFO     29 [qwen-vl-table] page=3, rect=595x843, img=(1654x2342)
2026-08-10 10:45:50,616 INFO     29 [qwen-vl-table] page=4, rect=595x843, img=(1654x2342)
2026-08-10 10:45:50,617 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:45:50,617 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 366, \"bbox_end\": 417, \"encounter_dates\": [\"2025-09-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l r l l}\n报告时间: 2025-09-02\n\\hline\n检查项目 & 结果 & 单位 & 参考值 \\\\\n\\hline\n白细胞 & 8.40 & 10^9/L & 3.5--9.5 \\\\\n红细胞 & 4.94 & 10^12/L & 3.8--5.1 \\\\\n血红蛋白 & 138 & g/L & 115--150 \\\\\n血小板 & 300 & 10^9/L & 125--350 \\\\\n红细胞压积 & 41.30 & \\% & 35--45 \\\\\n红细胞平均体积 & 83.60 & fL & 82--100 \\\\\n平均血红蛋白量 & 28.00 & pg & 27--34 \\\\\n平均血红蛋白浓 & 334 & g/L & 316--354 \\\\\n度 & & & \\\\\n中性粒细胞比率 & 54.20 & \\% & 40--75 \\\\\n淋巴细胞比率 & 36.10 & \\% & 20--50 \\\\\n单核细胞比率 & 3.70 & \\% & 3--10 \\\\\n嗜酸性粒细胞比 & 5.50 & \\% & 0.4--8.0 \\\\\n率 & & & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{cccccc}\n\\hline\n& & & & & \\\\\n红细胞 & 4.94 & 10^12/L & 3.8--5.1 & & \\\\\n血红蛋白 & 138 & g/L & 115--150 & & \\\\",
    "role": "user"
  }
]
2026-08-10 10:45:58,154 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:45:58,154 INFO     29 [qwen-vl-table] page=3 LLM output (len=2037):
{
  "report_date": "2025-09-02",
  "items": [
    {
      "name": "白细胞",
      "item_code": null,
      "value": "8.40",
      "unit": "10^9/L",
      "reference_range": "3.5--9.5",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": null,
      "value": "4.94",
      "unit": "10^12/L",
      "reference_range": "3.8--5.1",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": null,
      "value": "138",
      "unit": "g/L",
      "reference_range": "115--150",
      "abnormal": false
    },
    {
      "name": "血小板",
      "item_code": null,
      "value": "300",
      "unit": "10^9/L",
      "reference_range": "125--350",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": null,
      "value": "41.30",
      "unit": "%",
      "reference_range": "35--45",
      "abnormal": false
    },
    {
      "name": "红细胞平均体积",
      "item_code": null,
      "value": "83.60",
      "unit": "fL",
      "reference_range": "82--100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": null,
      "value": "28.00",
      "unit": "pg",
      "reference_range": "27--34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": null,
      "value": "334",
      "unit": "g/L",
      "reference_range": "316--354",
      "abnormal": false
    },
    {
      "name": "中性粒细胞比率",
      "item_code": null,
      "value": "54.20",
      "unit": "%",
      "reference_range": "40--75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞比率",
      "item_code": null,
      "value": "36.10",
      "unit": "%",
      "reference_range": "20--50",
      "abnormal": false
    },
    {
      "name": "单核细胞比率",
      "item_code": null,
      "value": "3.70",
      "unit": "%",
      "reference_range": "3--10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞比率",
      "item_code": null,
      "value": "5.50",
      "unit": "%",
      "reference_range": "0.4--8.0",
      "abnormal": false
    }
  ]
}
2026-08-10 10:45:58,154 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:45:58,154 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 366, \"bbox_end\": 417, \"encounter_dates\": [\"2025-09-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "血小板 & 300 & 10^9/L & 125--350 & & \\\\\n红细胞压积 & 41.30 & \\% & 35--45 & & \\\\\n红细胞平均体积 & 83.60 & fL & 82--100 & & \\\\\n平均血红蛋白量 & 28.00 & pg & 27--34 & & \\\\\n平均血红蛋白浓 & 334 & g/L & 316--354 & & \\\\\n度 & & & & & \\\\\n中性粒细胞比率 & 54.20 & \\% & 40--75 & & \\\\\n淋巴细胞比率 & 36.10 & \\% & 20--50 & & \\\\\n单核细胞比率 & 3.70 & \\% & 3--10 & & \\\\\n嗜酸性粒细胞比 & 5.50 & \\% & 0.4--8.0 & & \\\\\n率 & & & & & \\\\\n嗜碱性粒细胞比 & 0.50 & \\% & 0--1 & & \\\\\n率 & & & & & \\\\\n中性粒细胞数 & 4.56 & 10^9/L & 1.8--6.3 & & \\\\\n淋巴细胞数 & 3.03 & 10^9/L & 1.1--3.2 & & \\\\\n单核细胞数 & 0.31 & 10^9/L & 0.10--0.60 & & \\\\\n嗜酸性粒细胞 & 0.46 & 10^9/L & 0.02--0.52 & & \\\\\n嗜碱性粒细胞 & 0.04 & 10^9/L & 0--0.06 & & \\\\\n红细胞分布宽度 & 12.9 & \\% & 11.0--16.0 & & \\\\\n变异系数 & & & & & \\\\\n血小板分布宽度 & 16.5 & fL & 8.0--18.1 & & \\\\\n平均血小板体积 & 10.2 & fL & 9--13 & & \\\\\n血小板压积 & 0.31 & \\% & 0.10--0.28 & & \\\\\nC反应蛋白 & 7.92 & mg/L & 0--6 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 10:46:08,830 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:08,831 INFO     29 [qwen-vl-table] page=4 LLM output (len=3383):
{
  "report_date": "2025-09-02",
  "items": [
    {
      "name": "血小板",
      "item_code": null,
      "value": "300",
      "unit": "10^9/L",
      "reference_range": "125--350",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": null,
      "value": "41.30",
      "unit": "%",
      "reference_range": "35--45",
      "abnormal": false
    },
    {
      "name": "红细胞平均体积",
      "item_code": null,
      "value": "83.60",
      "unit": "fL",
      "reference_range": "82--100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": null,
      "value": "28.00",
      "unit": "pg",
      "reference_range": "27--34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": null,
      "value": "334",
      "unit": "g/L",
      "reference_range": "316--354",
      "abnormal": false
    },
    {
      "name": "中性粒细胞比率",
      "item_code": null,
      "value": "54.20",
      "unit": "%",
      "reference_range": "40--75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞比率",
      "item_code": null,
      "value": "36.10",
      "unit": "%",
      "reference_range": "20--50",
      "abnormal": false
    },
    {
      "name": "单核细胞比率",
      "item_code": null,
      "value": "3.70",
      "unit": "%",
      "reference_range": "3--10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞比率",
      "item_code": null,
      "value": "5.50",
      "unit": "%",
      "reference_range": "0.4--8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞比率",
      "item_code": null,
      "value": "0.50",
      "unit": "%",
      "reference_range": "0--1",
      "abnormal": false
    },
    {
      "name": "中性粒细胞数",
      "item_code": null,
      "value": "4.56",
      "unit": "10^9/L",
      "reference_range": "1.8--6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞数",
      "item_code": null,
      "value": "3.03",
      "unit": "10^9/L",
      "reference_range": "1.1--3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞数",
      "item_code": null,
      "value": "0.31",
      "unit": "10^9/L",
      "reference_range": "0.10--0.60",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞",
      "item_code": null,
      "value": "0.46",
      "unit": "10^9/L",
      "reference_range": "0.02--0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞",
      "item_code": null,
      "value": "0.04",
      "unit": "10^9/L",
      "reference_range": "0--0.06",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度变异系数",
      "item_code": null,
      "value": "12.9",
      "unit": "%",
      "reference_range": "11.0--16.0",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": null,
      "value": "16.5",
      "unit": "fL",
      "reference_range": "8.0--18.1",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": null,
      "value": "10.2",
      "unit": "fL",
      "reference_range": "9--13",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": null,
      "value": "0.31",
      "unit": "%",
      "reference_range": "0.10--0.28",
      "abnormal": true
    },
    {
      "name": "C反应蛋白",
      "item_code": null,
      "value": "7.92",
      "unit": "mg/L",
      "reference_range": "0--6",
      "abnormal": true
    }
  ]
}
2026-08-10 10:46:08,831 INFO     29 [qwen-vl-table] coord grouping: {3: 24, 4: 8}
2026-08-10 10:46:08,833 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=707641, prompt_len=679
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞、红细胞、血红蛋白、血小板、红细胞压积、红细胞平均体积、平均血红蛋白量、平均血红蛋白浓度、中性粒细胞比率、淋巴细胞比率、单核细胞比率、嗜酸性粒细胞比率、血小板、红细胞压积、红细胞平均体积、平均血红蛋白量、平均血红蛋白浓度、中性粒细胞比率、淋巴细胞比率、单核细胞比率、嗜酸性粒细胞比率、嗜碱性粒细胞比率、嗜酸性粒细胞、红细胞分布宽度变异系数

## 规则
1. 对于列表中的每个名称，找到它在图片中出现的位置
2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]
3. 如果某个名称在图片中未找到，可以跳过不输出
4. text字段必须与给定的名称完全一致，不要修改或缩写

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},
  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:46:15,899 INFO     29 [qwen-vl-table] coord API raw response (len=1231):
[
	{"text": "白细胞", "bbox": [199, 457, 282, 479]},
	{"text": "红细胞", "bbox": [199, 497, 282, 518]},
	{"text": "血红蛋白", "bbox": [199, 536, 307, 558]},
	{"text": "血小板", "bbox": [199, 576, 282, 598]},
	{"text": "红细胞压积", "bbox": [199, 616, 337, 638]},
	{"text": "红细胞平均体积", "bbox": [199, 656, 391, 678]},
	{"text": "平均血红蛋白量", "bbox": [199, 695, 391, 717]},
	{"text": "平均血红蛋白浓度", "bbox": [199, 735, 391, 757]},
	{"text": "中性粒细胞比率", "bbox": [199, 805, 391, 827]},
	{"text": "淋巴细胞比率", "bbox": [199, 845, 364, 867]},
	{"text": "单核细胞比率", "bbox": [199, 884, 364, 906]},
	{"text": "嗜酸性粒细胞比率", "bbox": [199, 924, 391, 946]},
	{"text": "血小板", "bbox": [199, 576, 282, 598]},
	{"text": "红细胞压积", "bbox": [199, 616, 337, 638]},
	{"text": "红细胞平均体积", "bbox": [199, 656, 391, 678]},
	{"text": "平均血红蛋白量", "bbox": [199, 695, 391, 717]},
	{"text": "平均血红蛋白浓度", "bbox": [199, 735, 391, 757]},
	{"text": "中性粒细胞比率", "bbox": [199, 805, 391, 827]},
	{"text": "淋巴细胞比率", "bbox": [199, 845, 364, 867]},
	{"text": "单核细胞比率", "bbox": [199, 884, 364, 906]},
	{"text": "嗜酸性粒细胞比率", "bbox": [199, 924, 391, 946]},
	{"text": "嗜碱性粒细胞比率", "bbox": [199, 964, 391, 986]},
	{"text": "嗜酸性粒细胞", "bbox": [199, 964, 391, 986]},
	{"text": "红细胞分布宽度变异系数", "bbox": [199, 964, 391, 986]}
]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=7.1s
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[199, 457, 282, 479]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞, bbox=[199, 497, 282, 518]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白, bbox=[199, 536, 307, 558]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[3]: text=血小板, bbox=[199, 576, 282, 598]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[4]: text=红细胞压积, bbox=[199, 616, 337, 638]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[5]: text=红细胞平均体积, bbox=[199, 656, 391, 678]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[6]: text=平均血红蛋白量, bbox=[199, 695, 391, 717]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[7]: text=平均血红蛋白浓度, bbox=[199, 735, 391, 757]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[8]: text=中性粒细胞比率, bbox=[199, 805, 391, 827]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[9]: text=淋巴细胞比率, bbox=[199, 845, 364, 867]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[10]: text=单核细胞比率, bbox=[199, 884, 364, 906]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[11]: text=嗜酸性粒细胞比率, bbox=[199, 924, 391, 946]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[12]: text=血小板, bbox=[199, 576, 282, 598]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[199, 616, 337, 638]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞平均体积, bbox=[199, 656, 391, 678]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[15]: text=平均血红蛋白量, bbox=[199, 695, 391, 717]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[16]: text=平均血红蛋白浓度, bbox=[199, 735, 391, 757]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[17]: text=中性粒细胞比率, bbox=[199, 805, 391, 827]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[18]: text=淋巴细胞比率, bbox=[199, 845, 364, 867]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[19]: text=单核细胞比率, bbox=[199, 884, 364, 906]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[20]: text=嗜酸性粒细胞比率, bbox=[199, 924, 391, 946]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[21]: text=嗜碱性粒细胞比率, bbox=[199, 964, 391, 986]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[22]: text=嗜酸性粒细胞, bbox=[199, 964, 391, 986]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] coord item[23]: text=红细胞分布宽度变异系数, bbox=[199, 964, 391, 986]
2026-08-10 10:46:15,900 INFO     29 [qwen-vl-table] page=3 coord: matched 24/24, time=7.1s
2026-08-10 10:46:15,902 INFO     29 [qwen-vl-table] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=923168, prompt_len=560
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
中性粒细胞数、淋巴细胞数、单核细胞数、嗜碱性粒细胞、血小板分布宽度、平均血小板体积、血小板压积、C反应蛋白

## 规则
1. 对于列表中的每个名称，找到它在图片中出现的位置
2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]
3. 如果某个名称在图片中未找到，可以跳过不输出
4. text字段必须与给定的名称完全一致，不要修改或缩写

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},
  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:46:19,117 INFO     29 [qwen-vl-table] coord API raw response (len=416):
[
  {"text": "中性粒细胞数", "bbox": [198, 583, 364, 605]},
  {"text": "淋巴细胞数", "bbox": [198, 623, 336, 645]},
  {"text": "单核细胞数", "bbox": [198, 663, 336, 685]},
  {"text": "嗜碱性粒细胞", "bbox": [198, 742, 364, 764]},
  {"text": "血小板分布宽度", "bbox": [198, 851, 391, 873]},
  {"text": "平均血小板体积", "bbox": [198, 890, 391, 912]},
  {"text": "血小板压积", "bbox": [198, 930, 336, 952]},
  {"text": "C反应蛋白", "bbox": [198, 970, 324, 992]}
]
2026-08-10 10:46:19,117 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=3.2s
2026-08-10 10:46:19,117 INFO     29 [qwen-vl-table] coord item[0]: text=中性粒细胞数, bbox=[198, 583, 364, 605]
2026-08-10 10:46:19,117 INFO     29 [qwen-vl-table] coord item[1]: text=淋巴细胞数, bbox=[198, 623, 336, 645]
2026-08-10 10:46:19,117 INFO     29 [qwen-vl-table] coord item[2]: text=单核细胞数, bbox=[198, 663, 336, 685]
2026-08-10 10:46:19,117 INFO     29 [qwen-vl-table] coord item[3]: text=嗜碱性粒细胞, bbox=[198, 742, 364, 764]
2026-08-10 10:46:19,118 INFO     29 [qwen-vl-table] coord item[4]: text=血小板分布宽度, bbox=[198, 851, 391, 873]
2026-08-10 10:46:19,118 INFO     29 [qwen-vl-table] coord item[5]: text=平均血小板体积, bbox=[198, 890, 391, 912]
2026-08-10 10:46:19,118 INFO     29 [qwen-vl-table] coord item[6]: text=血小板压积, bbox=[198, 930, 336, 952]
2026-08-10 10:46:19,118 INFO     29 [qwen-vl-table] coord item[7]: text=C反应蛋白, bbox=[198, 970, 324, 992]
2026-08-10 10:46:19,118 INFO     29 [qwen-vl-table] page=4 coord: matched 8/8, time=3.2s
2026-08-10 10:46:19,118 INFO     29 [qwen-vl-table] new_positions (32):
[[4, 118.45985131835937, 167.86772900390625, 385.26650854492186, 403.81325512695315], [4, 118.45985131835937, 167.86772900390625, 418.9878659667969, 436.69157861328125], [4, 118.45985131835937, 182.74961987304687, 451.866189453125, 470.41293603515624], [4, 118.45985131835937, 167.86772900390625, 485.587546875, 504.1342934570313], [4, 118.45985131835937, 200.6078889160156, 519.308904296875, 537.8556508789062], [4, 118.45985131835937, 232.75277319335936, 553.03026171875, 571.5770083007812], [4, 118.45985131835937, 232.75277319335936, 585.9085852050781, 604.4553317871093], [4, 118.45985131835937, 232.75277319335936, 619.6299426269532, 638.1766892089844], [4, 118.45985131835937, 232.75277319335936, 678.6423181152344, 697.1890646972656], [4, 118.45985131835937, 216.68033105468749, 712.3636755371094, 730.9104221191407], [4, 118.45985131835937, 216.68033105468749, 745.2419990234375, 763.7887456054688], [4, 118.45985131835937, 232.75277319335936, 778.9633564453125, 797.5101030273438], [4, 118.45985131835937, 167.86772900390625, 485.587546875, 504.1342934570313], [4, 118.45985131835937, 200.6078889160156, 519.308904296875, 537.8556508789062], [4, 118.45985131835937, 232.75277319335936, 553.03026171875, 571.5770083007812], [4, 118.45985131835937, 232.75277319335936, 585.9085852050781, 604.4553317871093], [4, 118.45985131835937, 232.75277319335936, 619.6299426269532, 638.1766892089844], [4, 118.45985131835937, 232.75277319335936, 678.6423181152344, 697.1890646972656], [4, 118.45985131835937, 216.68033105468749, 712.3636755371094, 730.9104221191407], [4, 118.45985131835937, 216.68033105468749, 745.2419990234375, 763.7887456054688], [4, 118.45985131835937, 232.75277319335936, 778.9633564453125, 797.5101030273438], [4, 118.45985131835937, 232.75277319335936, 812.6847138671875, 831.2314604492187], [4, 118.45985131835937, 232.75277319335936, 812.6847138671875, 831.2314604492187], [4, 118.45985131835937, 232.75277319335936, 812.6847138671875, 831.2314604492187], [5, 117.86457568359374, 216.68033105468749, 491.4887844238281, 510.03553100585935], [5, 117.86457568359374, 200.01261328124997, 525.2101418457031, 543.7568884277343], [5, 117.86457568359374, 200.01261328124997, 558.9314992675781, 577.4782458496094], [5, 117.86457568359374, 216.68033105468749, 625.5311801757813, 644.0779267578125], [5, 117.86457568359374, 232.75277319335936, 717.4218791503906, 735.9686257324219], [5, 117.86457568359374, 232.75277319335936, 750.3002026367187, 768.84694921875], [5, 117.86457568359374, 200.01261328124997, 784.0215600585938, 802.568306640625], [5, 117.86457568359374, 192.8693056640625, 817.7429174804688, 836.2896640625]]
2026-08-10 10:46:19,119 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=32, matched=32, pages=2, time=28.9s
2026-08-10 10:46:19,134 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 10:46:19,134 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:46:19,134 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 10:46:19,135 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T10:46:19.134+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"71a9158694a811f1bd9827cf206dfa2d": {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 10:46:19,145 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:19,145 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 10:46:20,045 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:20,051 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 10:46:20,052 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:46:20,052 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 10:46:20,059 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:46:20,059 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:46:20,060 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 10:46:20,060 INFO     29 [qwen-vl-text] positions(28): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:46:20,060 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [28]
2026-08-10 10:46:20,330 INFO     29 [qwen-vl-text] page=0, rect=595x1290, img=(1654x3583), dpi=200
2026-08-10 10:46:20,331 INFO     29 [qwen-vl-text] LLM extraction start, text_len=341
2026-08-10 10:46:20,331 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:20,332 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 27, \"encounter_dates\": [\"2024-08-23\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "2/4\n沈阳市第四人民医院\nTHE FOURTH PEOPLE'S HOSPITAL OF SHENYANG\n门诊病历\n业：现住址：辽宁省沈阳市皇姑区延河街\n就诊科别：呼吸与危重症医学科门诊\n就诊时间：2024-08-23 16:00\n书写时间：2024-08-23 16:59\n供史者：患者本人\n主诉：支气管哮喘开药\n现病史：患者支气管哮喘，继续巩固治疗：\n沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒\n孟鲁司特钠片\n10mg*5片，共10片\n每次10mg，QD\n睡前口服\n查体/专科查体：\n辅助检查：\n诊断：\n支气管哮喘\n处理意见：\n建议患者定期复查肺功能，肺部CT.\n我科随诊。\n建议休息天数：0天。\n患者下转：\n签名：杨昕\n患者签名：\n门诊病历专用章",
    "role": "user"
  }
]
2026-08-10 10:46:24,074 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:24,074 INFO     29 [qwen-vl-text] LLM output (len=565):
{
  "encounter_date": "2024-08-23",
  "chief_complaint": "支气管哮喘开药",
  "present_illness": "患者支气管哮喘，继续巩固治疗：\n沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒\n孟鲁司特钠片\n10mg*5片，共10片\n每次10mg，QD\n睡前口服",
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    {
      "drug_name": "沙美特罗替卡松吸入粉雾剂",
      "specification": "50ug：250ug/泡*60泡/盒",
      "quantity": "1盒"
    },
    {
      "drug_name": "孟鲁司特钠片",
      "specification": "10mg*5片",
      "quantity": "10片",
      "dosage": "10mg",
      "frequency": "QD",
      "route": "口服",
      "timing": "睡前"
    }
  ]
}
2026-08-10 10:46:24,074 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-08-23]
2026-08-10 10:46:24,076 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1369676, prompt_len=1038
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["2/4", "沈阳市第四人民医院", "THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG", "门诊病历", "业：现住址：辽宁省沈阳市皇姑区延河街", "就诊科别：呼吸与危重症医学科门诊", "就诊时间：2024-08-23 16:00", "书写时间：2024-08-23 16:59", "供史者：患者本人", "主诉：支气管哮喘开药", "现病史：患者支气管哮喘，继续巩固治疗：", "沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒", "孟鲁司特钠片", "10mg*5片，共10片", "每次10mg，QD", "睡前口服", "查体/专科查体：", "辅助检查：", "诊断：", "支气管哮喘", "处理意见：", "建议患者定期复查肺功能，肺部CT.", "我科随诊。", "建议休息天数：0天。", "患者下转：", "签名：杨昕", "患者签名：", "门诊病历专用章"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:46:33,752 INFO     29 [qwen-vl-text] coord API raw response (len=1621):
[
	{"text": "2/4", "bbox": [78, 118, 138, 135]},
	{"text": "沈阳市第四人民医院", "bbox": [395, 183, 708, 202]},
	{"text": "THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG", "bbox": [395, 202, 708, 209]},
	{"text": "门诊病历", "bbox": [454, 212, 595, 230]},
	{"text": "业：现住址：辽宁省沈阳市皇姑区延河街", "bbox": [538, 237, 842, 247]},
	{"text": "就诊科别：呼吸与危重症医学科门诊", "bbox": [157, 282, 430, 291]},
	{"text": "就诊时间：2024-08-23 16:00", "bbox": [157, 295, 378, 304],
	"text": "书写时间：2024-08-23 16:59", "bbox": [157, 308, 378, 317]},
	{"text": "供史者：患者本人", "bbox": [157, 321, 288, 330]},
	{"text": "主诉：支气管哮喘开药", "bbox": [157, 339, 333, 348]},
	{"text": "现病史：患者支气管哮喘，继续巩固治疗：", "bbox": [157, 366, 480, 376]},
	{"text": "沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒", "bbox": [157, 388, 614, 398]},
	{"text": "孟鲁司特钠片", "bbox": [157, 399, 260, 408]},
	{"text": "10mg*5片，共10片", "bbox": [315, 400, 446, 408]},
	{"text": "每次10mg，QD", "bbox": [552, 400, 650, 408]},
	{"text": "睡前口服", "bbox": [725, 400, 794, 408]},
	{"text": "查体/专科查体：", "bbox": [157, 427, 277, 436]},
	{"text": "辅助检查：", "bbox": [157, 467, 234, 476]},
	{"text": "诊断：", "bbox": [157, 517, 197, 526]},
	{"text": "支气管哮喘", "bbox": [157, 528, 243, 537]},
	{"text": "处理意见：", "bbox": [157, 557, 234, 566]},
	{"text": "建议患者定期复查肺功能，肺部CT.", "bbox": [157, 568, 427, 577]},
	{"text": "我科随诊。", "bbox": [157, 579, 234, 588]},
	{"text": "建议休息天数：0天。", "bbox": [157, 590, 321, 600]},
	{"text": "患者下转：", "bbox": [157, 602, 234, 611]},
	{"text": "签名：杨昕", "bbox": [517, 628, 643, 650]},
	{"text": "患者签名：", "bbox": [164, 641, 241, 651]},
	{"text": "门诊病历专用章", "bbox": [669, 785, 778, 798]},
	{"text": "(1)", "bbox": [708, 800, 739, 810]}
]
2026-08-10 10:46:33,752 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=9.7s
2026-08-10 10:46:33,752 INFO     29 [qwen-vl-text] coord item[0]: text=2/4, bbox=[78, 118, 138, 135]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[1]: text=沈阳市第四人民医院, bbox=[395, 183, 708, 202]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[2]: text=THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG, bbox=[395, 202, 708, 209]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[3]: text=门诊病历, bbox=[454, 212, 595, 230]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[4]: text=业：现住址：辽宁省沈阳市皇姑区延河街, bbox=[538, 237, 842, 247]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[5]: text=就诊科别：呼吸与危重症医学科门诊, bbox=[157, 282, 430, 291]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[6]: text=书写时间：2024-08-23 16:59, bbox=[157, 308, 378, 317]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[7]: text=供史者：患者本人, bbox=[157, 321, 288, 330]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：支气管哮喘开药, bbox=[157, 339, 333, 348]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：患者支气管哮喘，继续巩固治疗：, bbox=[157, 366, 480, 376]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[10]: text=沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒, bbox=[157, 388, 614, 398]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[11]: text=孟鲁司特钠片, bbox=[157, 399, 260, 408]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[12]: text=10mg*5片，共10片, bbox=[315, 400, 446, 408]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[13]: text=每次10mg，QD, bbox=[552, 400, 650, 408]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[14]: text=睡前口服, bbox=[725, 400, 794, 408]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[15]: text=查体/专科查体：, bbox=[157, 427, 277, 436]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查：, bbox=[157, 467, 234, 476]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[17]: text=诊断：, bbox=[157, 517, 197, 526]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[18]: text=支气管哮喘, bbox=[157, 528, 243, 537]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[19]: text=处理意见：, bbox=[157, 557, 234, 566]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[20]: text=建议患者定期复查肺功能，肺部CT., bbox=[157, 568, 427, 577]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[21]: text=我科随诊。, bbox=[157, 579, 234, 588]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[22]: text=建议休息天数：0天。, bbox=[157, 590, 321, 600]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[23]: text=患者下转：, bbox=[157, 602, 234, 611]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[24]: text=签名：杨昕, bbox=[517, 628, 643, 650]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[25]: text=患者签名：, bbox=[164, 641, 241, 651]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[26]: text=门诊病历专用章, bbox=[669, 785, 778, 798]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] coord item[27]: text=(1), bbox=[708, 800, 739, 810]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] page=0 — 28/28 coords, api_time=9.7s
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] new_positions (28):
[[0, 46.43149951171875, 82.14803759765624, 152.19214208984374, 174.11812866210937], [0, 235.13387573242184, 421.4551494140625, 236.02679663085937, 260.5323110351562], [0, 235.13387573242184, 421.4551494140625, 260.5323110351562, 269.5606584472656], [0, 270.2551381835937, 354.1890026855468, 273.4299501953125, 296.6457006835937], [0, 320.2582915039062, 501.2220844726562, 305.6740480957031, 318.57168725585933], [0, 93.45827465820312, 255.96852294921874, 363.71342431640625, 375.32129956054683], [0, 93.45827465820312, 225.01418994140624, 397.24728613281246, 408.8551613769531], [0, 93.45827465820312, 171.43938281249999, 414.01421704101557, 425.6220922851562], [0, 93.45827465820312, 198.2267863769531, 437.22996752929686, 448.83784277343744], [0, 93.45827465820312, 285.7323046875, 472.05359326171873, 484.951232421875], [0, 93.45827465820312, 365.49923974609374, 500.4283994140625, 513.3260385742187], [0, 93.45827465820312, 154.7716650390625, 514.6158024902344, 526.223677734375], [0, 187.51182495117186, 265.49293310546875, 515.9055664062499, 526.223677734375], [0, 328.59215039062497, 386.9291625976562, 515.9055664062499, 526.223677734375], [0, 431.5748352050781, 472.6488540039062, 515.9055664062499, 526.223677734375], [0, 93.45827465820312, 164.89135083007812, 550.7291921386718, 562.3370673828125], [0, 93.45827465820312, 139.29449853515624, 602.3197487792968, 613.9276240234375], [0, 93.45827465820312, 117.26930004882811, 666.8079445800781, 678.4158198242187], [0, 93.45827465820312, 144.65197924804687, 680.9953476562499, 692.6032229003906], [0, 93.45827465820312, 139.29449853515624, 718.3985012207031, 730.0063764648437], [0, 93.45827465820312, 254.18269604492184, 732.5859042968749, 744.1937795410156], [0, 93.45827465820312, 139.29449853515624, 746.7733073730468, 758.3811826171874], [0, 93.45827465820312, 191.0834787597656, 760.9607104492187, 773.858349609375], [0, 93.45827465820312, 139.29449853515624, 776.4378774414062, 788.0457526855469], [0, 307.7575031738281, 382.76223315429684, 809.9717392578125, 838.3465454101562], [0, 97.62520410156249, 143.46142797851562, 826.7386701660156, 839.6363093261718], [0, 398.23939965820307, 463.1244438476562, 1012.4646740722656, 1029.2316049804688], [0, 421.4551494140625, 439.90869409179686, 1031.8111328124999, 1044.7087719726562]]
2026-08-10 10:46:33,753 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=13.7s
2026-08-10 10:46:33,753 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:46:33,755 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:46:33,755 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 10:46:33,755 INFO     29 [qwen-vl-text] positions(21): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:46:33,755 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [21]
2026-08-10 10:46:34,208 INFO     29 [qwen-vl-text] page=5, rect=595x1010, img=(1654x2805), dpi=200
2026-08-10 10:46:34,209 INFO     29 [qwen-vl-text] LLM extraction start, text_len=374
2026-08-10 10:46:34,209 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:34,209 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 418, \"bbox_end\": 438, \"encounter_dates\": [\"2025-11-08\"], \"department\": \"呼吸内一科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "辽宁崇文厚德医院\n门诊病历\n科室：呼吸内一科门诊\n姓名：\n职业：\n就诊日期：2025/11/08 10:11:23\n主诉：反复喘息2年，加重1周\n现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万\n林”治疗，症状稍有改善，为求进一步诊治来我院就诊。\n既往史：否认。\n过敏史：{无}\n体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。\n辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试\n性。\n抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.\n初步诊断：1、支气管哮喘 急性发作期\n处理：\n1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。\n2.1周后复诊，病情变化随诊。\n医生签名：王春\n王春",
    "role": "user"
  }
]
2026-08-10 10:46:36,447 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:36,447 INFO     29 [qwen-vl-text] LLM output (len=299):
{
  "encounter_date": "2025-11-08",
  "chief_complaint": "反复喘息2年，加重1周",
  "present_illness": "3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万林”治疗，症状稍有改善，为求进一步诊治来我院就诊。",
  "past_history": "否认。",
  "diagnosis": "1、支气管哮喘 急性发作期",
  "treatment_plan": "1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。\n2.1周后复诊，病情变化随诊。"
}
2026-08-10 10:46:36,447 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-08]
2026-08-10 10:46:36,452 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2759372, prompt_len=1050
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["辽宁崇文厚德医院", "门诊病历", "科室：呼吸内一科门诊", "姓名：", "职业：", "就诊日期：2025/11/08 10:11:23", "主诉：反复喘息2年，加重1周", "现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万", "林”治疗，症状稍有改善，为求进一步诊治来我院就诊。", "既往史：否认。", "过敏史：{无}", "体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。", "辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试", "性。", "抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.", "初步诊断：1、支气管哮喘 急性发作期", "处理：", "1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。", "2.1周后复诊，病情变化随诊。", "医生签名：王春", "王春"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:46:44,151 INFO     29 [qwen-vl-text] coord API raw response (len=1269):
[
	{"text": "辽宁崇文厚德医院", "bbox": [356, 39, 667, 63]},
	{"text": "门诊病历", "bbox": [437, 72, 588, 95]},
	{"text": "科室：呼吸内一科门诊", "bbox": [35, 105, 280, 120]},
	{"text": "姓名：", "bbox": [30, 161, 89, 176]},
	{"text": "职业：", "bbox": [28, 187, 87, 202]},
	{"text": "就诊日期：2025/11/08 10:11:23", "bbox": [27, 214, 390, 230]},
	{"text": "主诉：反复喘息2年，加重1周", "bbox": [25, 243, 350, 259]},
	{"text": "现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万", "bbox": [22, 270, 997, 288]},
	{"text": "林”治疗，症状稍有改善，为求进一步诊治来我院就诊。", "bbox": [7, 300, 630, 317]},
	{"text": "既往史：否认。", "bbox": [17, 334, 178, 350]},
	{"text": "过敏史：{无}", "bbox": [14, 365, 160, 381]},
	{"text": "体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。", "bbox": [12, 393, 955, 411]},
	{"text": "辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试", "bbox": [8, 422, 995, 440]},
	{"text": "性。", "bbox": [7, 455, 44, 471]},
	{"text": "抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.", "bbox": [6, 489, 620, 505]},
	{"text": "初步诊断：1、支气管哮喘 急性发作期", "bbox": [28, 518, 462, 535]},
	{"text": "处理：", "bbox": [3, 548, 65, 564]},
	{"text": "1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。", "bbox": [3, 575, 980, 592]},
	{"text": "2.1周后复诊，病情变化随诊。", "bbox": [3, 605, 312, 621]},
	{"text": "医生签名：王春", "bbox": [535, 724, 719, 740]},
	{"text": "王春", "bbox": [778, 670, 927, 737]}
]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=7.7s
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[0]: text=辽宁崇文厚德医院, bbox=[356, 39, 667, 63]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[437, 72, 588, 95]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[2]: text=科室：呼吸内一科门诊, bbox=[35, 105, 280, 120]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[30, 161, 89, 176]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[4]: text=职业：, bbox=[28, 187, 87, 202]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[5]: text=就诊日期：2025/11/08 10:11:23, bbox=[27, 214, 390, 230]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：反复喘息2年，加重1周, bbox=[25, 243, 350, 259]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万, bbox=[22, 270, 997, 288]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[8]: text=林”治疗，症状稍有改善，为求进一步诊治来我院就诊。, bbox=[7, 300, 630, 317]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：否认。, bbox=[17, 334, 178, 350]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[10]: text=过敏史：{无}, bbox=[14, 365, 160, 381]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[11]: text=体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。, bbox=[12, 393, 955, 411]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[12]: text=辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试, bbox=[8, 422, 995, 440]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[13]: text=性。, bbox=[7, 455, 44, 471]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[14]: text=抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%., bbox=[6, 489, 620, 505]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断：1、支气管哮喘 急性发作期, bbox=[28, 518, 462, 535]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[16]: text=处理：, bbox=[3, 548, 65, 564]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[17]: text=1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。, bbox=[3, 575, 980, 592]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[18]: text=2.1周后复诊，病情变化随诊。, bbox=[3, 605, 312, 621]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[19]: text=医生签名：王春, bbox=[535, 724, 719, 740]
2026-08-10 10:46:44,152 INFO     29 [qwen-vl-text] coord item[20]: text=王春, bbox=[778, 670, 927, 737]
2026-08-10 10:46:44,153 INFO     29 [qwen-vl-text] page=5 — 21/21 coords, api_time=7.7s
2026-08-10 10:46:44,153 INFO     29 [qwen-vl-text] new_positions (21):
[[5, 211.9181259765625, 397.04884838867184, 39.38157824707031, 63.61639562988281], [5, 260.1354523925781, 350.02207324218745, 72.7044521484375, 95.92948547363281], [5, 20.834647216796874, 166.677177734375, 106.02732604980469, 121.1740869140625], [5, 17.85826904296875, 52.97953149414062, 162.5752332763672, 177.721994140625], [5, 16.6677177734375, 51.78898022460937, 188.82961877441406, 203.97637963867186], [5, 16.072442138671875, 232.15749755859372, 216.09378833007813, 232.25033325195312], [5, 14.881890869140623, 208.34647216796873, 245.37752600097656, 261.5340709228516], [5, 13.096063964843749, 593.4898078613281, 272.6416955566406, 290.81780859375], [5, 4.166929443359375, 375.0236499023437, 302.9352172851562, 320.10154626464845], [5, 10.119685791015623, 105.95906298828125, 337.2678752441406, 353.42442016601564], [5, 8.33385888671875, 95.24410156249999, 368.5711810302734, 384.72772595214843], [5, 7.143307617187499, 568.4882312011719, 396.8451346435547, 415.02124768066403], [5, 4.762205078125, 592.2992565917968, 426.12887231445313, 444.3049853515625], [5, 4.166929443359375, 26.192127929687498, 459.4517462158203, 475.6082911376953], [5, 3.5716538085937497, 369.0708935546875, 493.7844041748047, 509.9409490966797], [5, 16.6677177734375, 275.01734326171874, 523.0681418457032, 540.2344708251953], [5, 1.7858269042968749, 38.692916259765624, 553.3616635742187, 569.5182084960937], [5, 1.7858269042968749, 583.3701220703125, 580.6258331298828, 597.792162109375], [5, 1.7858269042968749, 185.725998046875, 610.9193548583984, 627.0758997802734], [5, 318.47246459960934, 428.00318139648436, 731.0836577148438, 747.2402026367188], [5, 463.1244438476562, 551.8205134277343, 676.5553186035156, 744.2108504638671]]
2026-08-10 10:46:44,153 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=10.4s
2026-08-10 10:46:44,164 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 10:46:44,165 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:46:44,165 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 10:46:44,172 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:46:44,173 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:46:44,173 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 10:46:44,173 INFO     29 [qwen-vl-text] positions(16): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:46:44,173 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [16]
2026-08-10 10:46:44,523 INFO     29 [qwen-vl-text] page=6, rect=544x842, img=(1511x2339), dpi=200
2026-08-10 10:46:44,524 INFO     29 [qwen-vl-text] LLM extraction start, text_len=214
2026-08-10 10:46:44,524 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:44,524 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 441, \"bbox_end\": 456, \"encounter_dates\": [\"2025-11-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "新药特药大药房总店\n流水单号 10020045213\n结账时间 2025-11-08 15:22:19\n编号 数量 单价 金额 营业员\n甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It\nSr1/库存2\n0310145 2 盒 34.00 68.00\n合计 68.00\n优惠：0.00 微信：0.00\n收银 1002\n银台\n会员\n本次积分 0.00\n累计积分 0.00\n此票为开发票依据，药品为特殊、\n商品，售出概不退还！",
    "role": "user"
  }
]
2026-08-10 10:46:46,638 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:46,638 INFO     29 [qwen-vl-text] LLM output (len=419):
{
  "encounter_date": "2025-11-08",
  "pharmacy": "新药特药大药房总店",
  "medications": [
    {
      "name": "甲泼尼龙片（美卓乐）",
      "specification": "4mg*30片",
      "dosage": null,
      "quantity": 2,
      "unit_price": 34.00,
      "total_price": 68.00,
      "frequency": null,
      "route": null,
      "manufacturer": "Pfizer",
      "approval_number": null
    }
  ],
  "payment_total": 68.00,
  "payment_method": "微信"
}
2026-08-10 10:46:46,638 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-08]
2026-08-10 10:46:46,643 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3289204, prompt_len=875
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["新药特药大药房总店", "流水单号 10020045213", "结账时间 2025-11-08 15:22:19", "编号 数量 单价 金额 营业员", "甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It", "Sr1/库存2", "0310145 2 盒 34.00 68.00", "合计 68.00", "优惠：0.00 微信：0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据，药品为特殊、", "商品，售出概不退还！"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord API raw response (len=903):
[
	{"text": "新药特药大药房总店", "bbox": [153, 134, 722, 178]},
	{"text": "流水单号 10020045213", "bbox": [15, 193, 719, 226]},
	{"text": "结账时间 2025-11-08 15:22:19", "bbox": [14, 246, 719, 280]},
	{"text": "编号 数量 单价 金额 营业员", "bbox": [11, 297, 861, 339]},
	{"text": "甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It", "bbox": [14, 350, 995, 392]},
	{"text": "Sr1/库存2", "bbox": [7, 405, 243, 439]},
	{"text": "0310145 2 盒 34.00 68.00", "bbox": [7, 461, 909, 496]},
	{"text": "合计 68.00", "bbox": [10, 512, 280, 544]},
	{"text": "优惠：0.00 微信：0.00", "bbox": [10, 567, 660, 600]},
	{"text": "收银 1002", "bbox": [7, 617, 255, 650]},
	{"text": "银台", "bbox": [7, 670, 100, 701]},
	{"text": "会员", "bbox": [7, 723, 100, 754]},
	{"text": "本次积分 0.00", "bbox": [10, 775, 351, 807]},
	{"text": "累计积分 0.00", "bbox": [14, 827, 467, 858]},
	{"text": "此票为开发票依据，药品为特殊、", "bbox": [210, 875, 870, 905]},
	{"text": "商品，售出概不退还！", "bbox": [353, 920, 777, 950]}
]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.7s
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[0]: text=新药特药大药房总店, bbox=[153, 134, 722, 178]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[1]: text=流水单号 10020045213, bbox=[15, 193, 719, 226]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[2]: text=结账时间 2025-11-08 15:22:19, bbox=[14, 246, 719, 280]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[3]: text=编号 数量 单价 金额 营业员, bbox=[11, 297, 861, 339]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[4]: text=甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It, bbox=[14, 350, 995, 392]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[5]: text=Sr1/库存2, bbox=[7, 405, 243, 439]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[6]: text=0310145 2 盒 34.00 68.00, bbox=[7, 461, 909, 496]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[7]: text=合计 68.00, bbox=[10, 512, 280, 544]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[8]: text=优惠：0.00 微信：0.00, bbox=[10, 567, 660, 600]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[9]: text=收银 1002, bbox=[7, 617, 255, 650]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[10]: text=银台, bbox=[7, 670, 100, 701]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[11]: text=会员, bbox=[7, 723, 100, 754]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[12]: text=本次积分 0.00, bbox=[10, 775, 351, 807]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[13]: text=累计积分 0.00, bbox=[14, 827, 467, 858]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[14]: text=此票为开发票依据，药品为特殊、, bbox=[210, 875, 870, 905]
2026-08-10 10:46:52,358 INFO     29 [qwen-vl-text] coord item[15]: text=商品，售出概不退还！, bbox=[353, 920, 777, 950]
2026-08-10 10:46:52,359 INFO     29 [qwen-vl-text] page=6 — 16/16 coords, api_time=5.7s
2026-08-10 10:46:52,359 INFO     29 [qwen-vl-text] new_positions (16):
[[6, 83.2106244506836, 392.66712976074217, 112.81322924804688, 149.85637915039064], [6, 8.157904357910157, 391.03554888916017, 162.48472570800783, 190.26708813476563], [6, 7.614044067382812, 391.03554888916017, 207.10488354492188, 235.7291357421875], [6, 5.982463195800781, 468.263710144043, 250.04126184082034, 285.4006322021485], [6, 7.614044067382812, 541.140989074707, 294.6614196777344, 330.02079003906255], [6, 3.807022033691406, 132.15805059814454, 340.9653570556641, 369.58960925292973], [6, 3.807022033691406, 494.3690040893555, 388.11118420410156, 417.57732617187503], [6, 5.438602905273438, 152.28088134765625, 431.0475625, 457.98803515625], [6, 5.438602905273438, 358.9477917480469, 477.3514998779297, 505.1338623046875], [6, 3.807022033691406, 138.68437408447267, 519.4459884033204, 547.2283508300782], [6, 3.807022033691406, 54.38602905273437, 564.0661462402344, 590.1647291259766], [6, 3.807022033691406, 54.38602905273437, 608.6863040771485, 634.7848869628907], [6, 5.438602905273438, 190.89496197509766, 652.4645721435547, 679.4050447998047], [6, 7.614044067382812, 253.98275567626953, 696.242840209961, 722.3414230957031], [6, 114.21066101074219, 473.15845275878905, 736.6535491943359, 761.9102423095703], [6, 191.98268255615235, 422.5794457397461, 774.5385888671875, 799.7952819824219]]
2026-08-10 10:46:52,359 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=8.2s
2026-08-10 10:46:52,359 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:46:52,360 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:46:52,361 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 10:46:52,361 INFO     29 [qwen-vl-text] positions(16): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:46:52,361 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [16]
2026-08-10 10:46:52,588 INFO     29 [qwen-vl-text] page=8, rect=595x843, img=(1654x2342), dpi=200
2026-08-10 10:46:52,590 INFO     29 [qwen-vl-text] LLM extraction start, text_len=225
2026-08-10 10:46:52,590 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:52,590 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 476, \"bbox_end\": 491, \"encounter_dates\": [\"2025-10-14\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "新药特药大药房总店\n流水单号 10020044912\n结账时间 2025-10-14 08:34:01\n编号 数量 单价 金额 营业员\n沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug\n泡/葛兰素史克(集团)/库存1\n0200127 1 盒 199.00 199.00\n合计 199.00\n优惠:0.00 微信:0.00\n收银 1002\n银台\n会员\n本次积分 0.00\n累计积分 0.00\n此票为开发票依据,药品为特殊、\n商品,售出概不退还!",
    "role": "user"
  }
]
2026-08-10 10:46:52,592 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T10:46:52.591+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"71a9158694a811f1bd9827cf206dfa2d": {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 10:46:55,846 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:46:55,846 INFO     29 [qwen-vl-text] LLM output (len=435):
{
  "encounter_date": "2025-10-14",
  "pharmacy": "新药特药大药房总店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂(舒利迭)",
      "specification": "50ug:250ug",
      "dosage": null,
      "quantity": 1,
      "unit_price": 199.00,
      "total_price": 199.00,
      "frequency": null,
      "route": null,
      "manufacturer": "葛兰素史克(集团)",
      "approval_number": null
    }
  ],
  "payment_total": 199.00,
  "payment_method": "微信"
}
2026-08-10 10:46:55,846 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-14]
2026-08-10 10:46:55,848 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=936924, prompt_len=886
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["新药特药大药房总店", "流水单号 10020044912", "结账时间 2025-10-14 08:34:01", "编号 数量 单价 金额 营业员", "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug", "泡/葛兰素史克(集团)/库存1", "0200127 1 盒 199.00 199.00", "合计 199.00", "优惠:0.00 微信:0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据,药品为特殊、", "商品,售出概不退还!"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord API raw response (len=919):
[
	{"text": "新药特药大药房总店", "bbox": [165, 162, 642, 199]},
	{"text": "流水单号 10020044912", "bbox": [48, 210, 642, 243]},
	{"text": "结账时间 2025-10-14 08:34:01", "bbox": [48, 262, 642, 293]},
	{"text": "编号 数量 单价 金额 营业员", "bbox": [48, 310, 764, 347]},
	{"text": "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug", "bbox": [48, 360, 946, 395]},
	{"text": "泡/葛兰素史克(集团)/库存1", "bbox": [48, 409, 613, 441]},
	{"text": "0200127 1 盒 199.00 199.00", "bbox": [48, 460, 861, 490]},
	{"text": "合计 199.00", "bbox": [48, 508, 293, 537]},
	{"text": "优惠:0.00 微信:0.00", "bbox": [48, 558, 607, 590]},
	{"text": "收银 1002", "bbox": [48, 608, 252, 639]},
	{"text": "银台", "bbox": [48, 660, 123, 690]},
	{"text": "会员", "bbox": [48, 710, 123, 741]},
	{"text": "本次积分 0.00", "bbox": [48, 762, 339, 793]},
	{"text": "累计积分 0.00", "bbox": [48, 813, 448, 845]},
	{"text": "此票为开发票依据,药品为特殊、", "bbox": [219, 863, 817, 895]},
	{"text": "商品,售出概不退还!", "bbox": [350, 913, 730, 943]}
]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.9s
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[0]: text=新药特药大药房总店, bbox=[165, 162, 642, 199]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[1]: text=流水单号 10020044912, bbox=[48, 210, 642, 243]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[2]: text=结账时间 2025-10-14 08:34:01, bbox=[48, 262, 642, 293]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[3]: text=编号 数量 单价 金额 营业员, bbox=[48, 310, 764, 347]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[4]: text=沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug, bbox=[48, 360, 946, 395]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[5]: text=泡/葛兰素史克(集团)/库存1, bbox=[48, 409, 613, 441]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[6]: text=0200127 1 盒 199.00 199.00, bbox=[48, 460, 861, 490]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[7]: text=合计 199.00, bbox=[48, 508, 293, 537]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[8]: text=优惠:0.00 微信:0.00, bbox=[48, 558, 607, 590]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[9]: text=收银 1002, bbox=[48, 608, 252, 639]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[10]: text=银台, bbox=[48, 660, 123, 690]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[11]: text=会员, bbox=[48, 710, 123, 741]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[12]: text=本次积分 0.00, bbox=[48, 762, 339, 793]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[13]: text=累计积分 0.00, bbox=[48, 813, 448, 845]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[14]: text=此票为开发票依据,药品为特殊、, bbox=[219, 863, 817, 895]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] coord item[15]: text=商品,售出概不退还!, bbox=[350, 913, 730, 943]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] page=8 — 16/16 coords, api_time=5.9s
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] new_positions (16):
[[8, 98.22047973632812, 382.1669575195312, 136.57149755859376, 167.76375317382812], [8, 28.573230468749998, 382.1669575195312, 177.03712646484374, 204.85724633789061], [8, 28.573230468749998, 382.1669575195312, 220.87489111328125, 247.0089431152344], [8, 28.573230468749998, 454.79058496093745, 261.34052001953125, 292.53277563476564], [8, 28.573230468749998, 563.1307504882813, 303.492216796875, 332.99840454101565], [8, 28.573230468749998, 364.9039641113281, 344.80087963867186, 371.7779655761719], [8, 28.573230468749998, 512.5323215332031, 387.7956103515625, 413.08662841796877], [8, 28.573230468749998, 174.4157609863281, 428.2612392578125, 452.7092233886719], [8, 28.573230468749998, 361.33231030273436, 470.41293603515624, 497.39002197265626], [8, 28.573230468749998, 150.00945996093748, 512.5646328125, 538.6986848144531], [8, 28.573230468749998, 73.21890307617187, 556.4023974609376, 581.6934155273437], [8, 28.573230468749998, 73.21890307617187, 598.5540942382812, 624.6881462402343], [8, 28.573230468749998, 201.79844018554687, 642.3918588867188, 668.5259108886719], [8, 28.573230468749998, 266.683484375, 685.3865895996094, 712.3636755371094], [8, 130.36536401367186, 486.34019360351556, 727.5382863769531, 754.5153723144531], [8, 208.34647216796873, 434.5512133789062, 769.6899831542969, 794.9810012207031]]
2026-08-10 10:47:01,699 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=9.3s
2026-08-10 10:47:01,700 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:47:01,701 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:47:01,702 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 10:47:01,702 INFO     29 [qwen-vl-text] positions(16): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:47:01,702 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [16]
2026-08-10 10:47:02,028 INFO     29 [qwen-vl-text] page=11, rect=466x842, img=(1294x2339), dpi=200
2026-08-10 10:47:02,029 INFO     29 [qwen-vl-text] LLM extraction start, text_len=220
2026-08-10 10:47:02,029 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:02,029 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 529, \"bbox_end\": 544, \"encounter_dates\": [\"2026-01-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "新药特药大药房总店\n流水单号 10020046503\n结账时间 2026-01-02 18:12:29\n编号 数量 单价 金额 营业员\n沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:\n泡/葛兰素史克(集团)/库存1\n0200127 1 盒 199.00 199.00\n合计 199.00\n优惠:0.00 微信:0.00\n收银 1002\n银台\n会员\n本次积分 0.00\n累计积分 0.00\n此票为开发票依据,药品为特殊、\n商品,售出概不退还!",
    "role": "user"
  }
]
2026-08-10 10:47:04,256 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:04,256 INFO     29 [qwen-vl-text] LLM output (len=431):
{
  "encounter_date": "2026-01-02",
  "pharmacy": "新药特药大药房总店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂(舒利迭)",
      "specification": "50ug:泡",
      "dosage": null,
      "quantity": 1,
      "unit_price": 199.00,
      "total_price": 199.00,
      "frequency": null,
      "route": null,
      "manufacturer": "葛兰素史克(集团)",
      "approval_number": null
    }
  ],
  "payment_total": 199.00,
  "payment_method": "微信"
}
2026-08-10 10:47:04,256 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-02]
2026-08-10 10:47:04,264 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2659913, prompt_len=881
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["新药特药大药房总店", "流水单号 10020046503", "结账时间 2026-01-02 18:12:29", "编号 数量 单价 金额 营业员", "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:", "泡/葛兰素史克(集团)/库存1", "0200127 1 盒 199.00 199.00", "合计 199.00", "优惠:0.00 微信:0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据,药品为特殊、", "商品,售出概不退还!"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord API raw response (len=914):
[
	{"text": "新药特药大药房总店", "bbox": [181, 124, 755, 160]},
	{"text": "流水单号 10020046503", "bbox": [50, 175, 752, 204]},
	{"text": "结账时间 2026-01-02 18:12:29", "bbox": [50, 224, 752, 251]},
	{"text": "编号 数量 单价 金额 营业员", "bbox": [45, 269, 895, 303]},
	{"text": "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:", "bbox": [45, 317, 972, 348]},
	{"text": "泡/葛兰素史克(集团)/库存1", "bbox": [45, 365, 712, 394]},
	{"text": "0200127 1 盒 199.00 199.00", "bbox": [48, 413, 998, 441]},
	{"text": "合计 199.00", "bbox": [48, 458, 339, 485]},
	{"text": "优惠:0.00 微信:0.00", "bbox": [45, 505, 700, 533]},
	{"text": "收银 1002", "bbox": [42, 550, 285, 577]},
	{"text": "银台", "bbox": [42, 596, 130, 623]},
	{"text": "会员", "bbox": [42, 642, 130, 670]},
	{"text": "本次积分 0.00", "bbox": [42, 688, 380, 715]},
	{"text": "累计积分 0.00", "bbox": [48, 730, 503, 757]},
	{"text": "此票为开发票依据,药品为特殊、", "bbox": [243, 773, 915, 800]},
	{"text": "商品,售出概不退还!", "bbox": [388, 812, 819, 835]}
]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.7s
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[0]: text=新药特药大药房总店, bbox=[181, 124, 755, 160]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[1]: text=流水单号 10020046503, bbox=[50, 175, 752, 204]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[2]: text=结账时间 2026-01-02 18:12:29, bbox=[50, 224, 752, 251]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[3]: text=编号 数量 单价 金额 营业员, bbox=[45, 269, 895, 303]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[4]: text=沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:, bbox=[45, 317, 972, 348]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[5]: text=泡/葛兰素史克(集团)/库存1, bbox=[45, 365, 712, 394]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[6]: text=0200127 1 盒 199.00 199.00, bbox=[48, 413, 998, 441]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[7]: text=合计 199.00, bbox=[48, 458, 339, 485]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[8]: text=优惠:0.00 微信:0.00, bbox=[45, 505, 700, 533]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[9]: text=收银 1002, bbox=[42, 550, 285, 577]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[10]: text=银台, bbox=[42, 596, 130, 623]
2026-08-10 10:47:09,935 INFO     29 [qwen-vl-text] coord item[11]: text=会员, bbox=[42, 642, 130, 670]
2026-08-10 10:47:09,936 INFO     29 [qwen-vl-text] coord item[12]: text=本次积分 0.00, bbox=[42, 688, 380, 715]
2026-08-10 10:47:09,936 INFO     29 [qwen-vl-text] coord item[13]: text=累计积分 0.00, bbox=[48, 730, 503, 757]
2026-08-10 10:47:09,936 INFO     29 [qwen-vl-text] coord item[14]: text=此票为开发票依据,药品为特殊、, bbox=[243, 773, 915, 800]
2026-08-10 10:47:09,936 INFO     29 [qwen-vl-text] coord item[15]: text=商品,售出概不退还!, bbox=[388, 812, 819, 835]
2026-08-10 10:47:09,936 INFO     29 [qwen-vl-text] page=11 — 16/16 coords, api_time=5.7s
2026-08-10 10:47:09,936 INFO     29 [qwen-vl-text] new_positions (16):
[[11, 84.25646664428712, 351.45653213500975, 104.39433154296876, 134.70236328125], [11, 23.275267028808592, 350.0600161132813, 147.3307098388672, 171.74551318359377], [11, 23.275267028808592, 350.0600161132813, 188.58330859375002, 211.31433239746096], [11, 20.947740325927736, 416.62727981567383, 226.46834826660157, 255.0926004638672], [11, 20.947740325927736, 452.47119104003906, 266.8790572509766, 292.9776401367188], [11, 20.947740325927736, 331.4398024902344, 307.2897662353516, 331.70456958007816], [11, 22.34425634765625, 464.57432989501956, 347.70047521972657, 371.27338879394534], [11, 22.34425634765625, 157.80631045532226, 385.58551489257815, 408.3165386962891], [11, 20.947740325927736, 325.85373840332034, 425.15433410644533, 448.7272476806641], [11, 19.55122430419922, 132.66902206420897, 463.0393737792969, 485.7703975830078], [11, 19.55122430419922, 60.515694274902344, 501.7663032226563, 524.4973270263672], [11, 19.55122430419922, 60.515694274902344, 540.4932326660156, 564.0661462402344], [11, 19.55122430419922, 176.89202941894533, 579.220162109375, 601.951185913086], [11, 22.34425634765625, 234.14918630981447, 614.5795324707032, 637.3105562744141], [11, 113.11779776000976, 425.93738662719727, 650.7807926025391, 673.5118164062501], [11, 180.61607214355467, 381.24887393188476, 683.6144936523438, 702.9779583740235]]
2026-08-10 10:47:09,936 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=8.2s
2026-08-10 10:47:09,946 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 10:47:09,946 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Medication | outputs={"chunks": "3 items, types={'MedicationRecord': 3}", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:47:09,946 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 10:47:09,956 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:47:09,956 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:47:09,956 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 10:47:09,957 INFO     29 [qwen-vl-text] positions(18): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:47:09,957 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [18]
2026-08-10 10:47:10,167 INFO     29 [qwen-vl-text] page=7, rect=595x843, img=(1654x2342), dpi=200
2026-08-10 10:47:10,169 INFO     29 [qwen-vl-text] LLM extraction start, text_len=240
2026-08-10 10:47:10,169 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:10,169 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 457, \"bbox_end\": 474, \"encounter_dates\": [\"2025-09-19\"], \"department\": \"呼吸与危重症一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "2/4\n科 室:呼吸与危重症一门诊\n诊断:(J45.900x001)支气管哮喘\nRp\n沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n【50ug:250ug/泡*60泡/(193.60元/盒)\n1盒\n用法用量:每次300ug,吸入,每天二次\n孟鲁司特钠片【舒宁安】乙\n超量说明:\n【10mg*5片】\n(4.96元/盒)\n3盒\n用法用量:每次10mg,睡前口服,每天一次\n医师:杨沂发药:修泉涌配药:沈瑶\nvivo X80 · ZEISS\n计:208.48/208.48\n第1页/共1页",
    "role": "user"
  }
]
2026-08-10 10:47:13,103 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:13,103 INFO     29 [qwen-vl-text] LLM output (len=693):
{
  "encounter_date": "2025-09-19",
  "prescription_type": "门诊处方",
  "prescriber": "杨沂",
  "department": "呼吸与危重症一门诊",
  "diagnosis": "(J45.900x001)支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭",
      "drug_category": "西药",
      "dosage": "300ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": "舒宁安",
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "每天一次",
      "route": "口服",
      "duration_days": null,
      "quantity": "3盒",
      "notes": "睡前服用"
    }
  ]
}
2026-08-10 10:47:13,103 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-19]
2026-08-10 10:47:13,105 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1054189, prompt_len=907
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["2/4", "科 室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "孟鲁司特钠片【舒宁安】乙", "超量说明:", "【10mg*5片】", "(4.96元/盒)", "3盒", "用法用量:每次10mg,睡前口服,每天一次", "医师:杨沂发药:修泉涌配药:沈瑶", "vivo X80 · ZEISS", "计:208.48/208.48", "第1页/共1页"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord API raw response (len=1033):
[
	{"text": "2/4", "bbox": [471, 62, 525, 78]},
	{"text": "科 室:呼吸与危重症一门诊", "bbox": [314, 447, 519, 460]},
	{"text": "诊断:(J45.900x001)支气管哮喘", "bbox": [310, 464, 469, 473]},
	{"text": "Rp", "bbox": [306, 479, 323, 489]},
	{"text": "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "bbox": [308, 502, 594, 513]},
	{"text": "【50ug:250ug/泡*60泡/(193.60元/盒)", "bbox": [326, 518, 552, 528]},
	{"text": "1盒", "bbox": [594, 519, 614, 528]},
	{"text": "用法用量:每次300ug,吸入,每天二次", "bbox": [328, 532, 540, 543]},
	{"text": "孟鲁司特钠片【舒宁安】乙", "bbox": [308, 547, 476, 558]},
	{"text": "超量说明:", "bbox": [514, 548, 572, 558]},
	{"text": "【10mg*5片】", "bbox": [326, 563, 397, 573]},
	{"text": "(4.96元/盒)", "bbox": [468, 564, 538, 573]},
	{"text": "3盒", "bbox": [592, 564, 612, 573]},
	{"text": "用法用量:每次10mg,睡前口服,每天一次", "bbox": [329, 578, 560, 588]},
	{"text": "医师:杨沂发药:修泉涌配药:沈瑶", "bbox": [316, 757, 511, 768]},
	{"text": "vivo X80 · ZEISS", "bbox": [200, 769, 361, 781]},
	{"text": "计:208.48/208.48", "bbox": [361, 775, 460, 784]},
	{"text": "第1页/共1页", "bbox": [482, 776, 553, 786]}
]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=6.5s
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[0]: text=2/4, bbox=[471, 62, 525, 78]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[1]: text=科 室:呼吸与危重症一门诊, bbox=[314, 447, 519, 460]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[2]: text=诊断:(J45.900x001)支气管哮喘, bbox=[310, 464, 469, 473]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[3]: text=Rp, bbox=[306, 479, 323, 489]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[4]: text=沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙, bbox=[308, 502, 594, 513]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[5]: text=【50ug:250ug/泡*60泡/(193.60元/盒), bbox=[326, 518, 552, 528]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[6]: text=1盒, bbox=[594, 519, 614, 528]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[7]: text=用法用量:每次300ug,吸入,每天二次, bbox=[328, 532, 540, 543]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[8]: text=孟鲁司特钠片【舒宁安】乙, bbox=[308, 547, 476, 558]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[9]: text=超量说明:, bbox=[514, 548, 572, 558]
2026-08-10 10:47:19,609 INFO     29 [qwen-vl-text] coord item[10]: text=【10mg*5片】, bbox=[326, 563, 397, 573]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] coord item[11]: text=(4.96元/盒), bbox=[468, 564, 538, 573]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] coord item[12]: text=3盒, bbox=[592, 564, 612, 573]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] coord item[13]: text=用法用量:每次10mg,睡前口服,每天一次, bbox=[329, 578, 560, 588]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] coord item[14]: text=医师:杨沂发药:修泉涌配药:沈瑶, bbox=[316, 757, 511, 768]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] coord item[15]: text=vivo X80 · ZEISS, bbox=[200, 769, 361, 781]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] coord item[16]: text=计:208.48/208.48, bbox=[361, 775, 460, 784]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] coord item[17]: text=第1页/共1页, bbox=[482, 776, 553, 786]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] page=7 — 18/18 coords, api_time=6.5s
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] new_positions (18):
[[7, 280.37482397460934, 312.5197082519531, 52.26810400390625, 65.75664697265626], [7, 186.91654931640625, 308.94805444335935, 376.83616918945313, 387.7956103515625], [7, 184.53544677734374, 279.1842727050781, 391.16774609375, 398.7550515136719], [7, 182.15434423828123, 192.27403002929685, 403.81325512695315, 412.2435944824219], [7, 183.34489550781248, 353.59372705078124, 423.20303564453127, 432.4764089355469], [7, 194.05985693359372, 328.59215039062497, 436.69157861328125, 445.12191796875], [7, 353.59372705078124, 365.49923974609374, 437.53461254882814, 445.12191796875], [7, 195.25040820312498, 321.4488427734375, 448.4940537109375, 457.76742700195314], [7, 183.34489550781248, 283.3512021484375, 461.1395627441406, 470.41293603515624], [7, 305.9716762695312, 340.49766308593746, 461.9825966796875, 470.41293603515624], [7, 194.05985693359372, 236.3244270019531, 474.6281057128906, 483.0584450683594], [7, 278.5889970703125, 320.2582915039062, 475.4711396484375, 483.0584450683594], [7, 352.40317578124996, 364.30868847656245, 475.4711396484375, 483.0584450683594], [7, 195.84568383789062, 333.35435546875, 487.27361474609376, 495.7039541015625], [7, 188.10710058593747, 304.18584936523433, 638.1766892089844, 647.4500625000001], [7, 119.05512695312498, 214.89450415039062, 648.2930964355469, 658.4095036621094], [7, 214.89450415039062, 273.82679199218745, 653.3513000488281, 660.93860546875], [7, 286.92285595703123, 329.1874260253906, 654.194333984375, 662.6246733398438]]
2026-08-10 10:47:19,610 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=9.7s
2026-08-10 10:47:19,610 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:47:19,612 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:47:19,612 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 10:47:19,612 INFO     29 [qwen-vl-text] positions(19): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:47:19,612 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [19]
2026-08-10 10:47:19,831 INFO     29 [qwen-vl-text] page=9, rect=595x843, img=(1654x2342), dpi=200
2026-08-10 10:47:19,832 INFO     29 [qwen-vl-text] LLM extraction start, text_len=245
2026-08-10 10:47:19,832 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:19,832 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 492, \"bbox_end\": 510, \"encounter_dates\": [\"2025-11-03\"], \"department\": \"呼吸与危重症一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "1/1\nNO:25004949727\n4号窗口\n25/11/03 16:39\n普通\n病志号:55161248\n科\n室:呼吸与危重症一门诊\n诊断:(J45.900x001)支气管哮喘\nRp\n沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n【50ug:250ug/泡*60泡/(193.60元/盒)\n1盒\n用法用量:每次300ug,吸入,每天二次\n医师:杨昕发药:沈瑶配药:巴艺洁\nvivo X80 · ZEISS\n金额合计:193.6/193.6\n第1页/共1页\n2025/11/05 14:51",
    "role": "user"
  }
]
2026-08-10 10:47:22,178 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:22,178 INFO     29 [qwen-vl-text] LLM output (len=435):
{
  "encounter_date": "2025-11-03",
  "prescription_type": "门诊处方",
  "prescriber": "杨昕",
  "department": "呼吸与危重症一门诊",
  "diagnosis": "(J45.900x001)支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭",
      "drug_category": "西药",
      "dosage": "300ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": null
    }
  ]
}
2026-08-10 10:47:22,178 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-03]
2026-08-10 10:47:22,180 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1081223, prompt_len=915
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["1/1", "NO:25004949727", "4号窗口", "25/11/03 16:39", "普通", "病志号:55161248", "科", "室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "医师:杨昕发药:沈瑶配药:巴艺洁", "vivo X80 · ZEISS", "金额合计:193.6/193.6", "第1页/共1页", "2025/11/05 14:51"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:47:29,831 INFO     29 [qwen-vl-text] coord API raw response (len=1082):
[
	{"text": "1/1", "bbox": [476, 62, 520, 78]},
	{"text": "NO:25004949727", "bbox": [294, 295, 417, 308]},
	{"text": "4号窗口", "bbox": [462, 297, 524, 309]},
	{"text": "25/11/03 16:39", "bbox": [290, 316, 413, 329]},
	{"text": "普通", "bbox": [461, 316, 496, 329]},
	{"text": "病志号:55161248", "bbox": [290, 340, 444, 353]},
	{"text": "科", "bbox": [301, 430, 319, 442]},
	{"text": "室:呼吸与危重症一门诊", "bbox": [353, 430, 528, 443]},
	{"text": "诊断:(J45.900x001)支气管哮喘", "bbox": [296, 448, 473, 458]},
	{"text": "Rp", "bbox": [296, 466, 314, 476]},
	{"text": "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "bbox": [300, 489, 607, 500]},
	{"text": "【50ug:250ug/泡*60泡/(193.60元/盒)", "bbox": [323, 505, 562, 515]},
	{"text": "1盒", "bbox": [607, 505, 627, 515]},
	{"text": "用法用量:每次300ug,吸入,每天二次", "bbox": [324, 520, 550, 530]},
	{"text": "医师:杨昕发药:沈瑶配药:巴艺洁", "bbox": [309, 761, 521, 773]},
	{"text": "vivo X80 · ZEISS", "bbox": [200, 770, 361, 782]},
	{"text": "金额合计:193.6/193.6", "bbox": [309, 783, 451, 793]},
	{"text": "第1页/共1页", "bbox": [492, 781, 568, 792]},
	{"text": "2025/11/05 14:51", "bbox": [200, 793, 344, 803]}
]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=7.7s
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[0]: text=1/1, bbox=[476, 62, 520, 78]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[1]: text=NO:25004949727, bbox=[294, 295, 417, 308]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[2]: text=4号窗口, bbox=[462, 297, 524, 309]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[3]: text=25/11/03 16:39, bbox=[290, 316, 413, 329]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[4]: text=普通, bbox=[461, 316, 496, 329]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[5]: text=病志号:55161248, bbox=[290, 340, 444, 353]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[6]: text=科, bbox=[301, 430, 319, 442]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[7]: text=室:呼吸与危重症一门诊, bbox=[353, 430, 528, 443]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[8]: text=诊断:(J45.900x001)支气管哮喘, bbox=[296, 448, 473, 458]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[9]: text=Rp, bbox=[296, 466, 314, 476]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[10]: text=沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙, bbox=[300, 489, 607, 500]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[11]: text=【50ug:250ug/泡*60泡/(193.60元/盒), bbox=[323, 505, 562, 515]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[12]: text=1盒, bbox=[607, 505, 627, 515]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[13]: text=用法用量:每次300ug,吸入,每天二次, bbox=[324, 520, 550, 530]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[14]: text=医师:杨昕发药:沈瑶配药:巴艺洁, bbox=[309, 761, 521, 773]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[15]: text=vivo X80 · ZEISS, bbox=[200, 770, 361, 782]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[16]: text=金额合计:193.6/193.6, bbox=[309, 783, 451, 793]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[17]: text=第1页/共1页, bbox=[492, 781, 568, 792]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] coord item[18]: text=2025/11/05 14:51, bbox=[200, 793, 344, 803]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] page=9 — 19/19 coords, api_time=7.7s
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] new_positions (19):
[[9, 283.3512021484375, 309.543330078125, 52.26810400390625, 65.75664697265626], [9, 175.01103662109372, 248.2299396972656, 248.69501098632813, 259.6544521484375], [9, 275.01734326171874, 311.92443261718745, 250.38107885742187, 260.49748608398437], [9, 172.62993408203124, 245.8488371582031, 266.3987236328125, 277.3581647949219], [9, 274.4220676269531, 295.25671484375, 266.3987236328125, 277.3581647949219], [9, 172.62993408203124, 264.30238183593747, 286.6315380859375, 297.5909792480469], [9, 179.1779660644531, 189.89292749023437, 362.50459228515626, 372.62099951171876], [9, 210.1322990722656, 314.30553515624996, 362.50459228515626, 373.46403344726565], [9, 176.20158789062498, 281.5653752441406, 377.679203125, 386.10954248046875], [9, 176.20158789062498, 186.91654931640625, 392.85381396484377, 401.2841533203125], [9, 178.5826904296875, 361.33231030273436, 412.2435944824219, 421.5169677734375], [9, 192.27403002929685, 334.5449067382812, 425.73213745117187, 434.1624768066406], [9, 361.33231030273436, 373.23782299804685, 425.73213745117187, 434.1624768066406], [9, 192.8693056640625, 327.40159912109374, 438.377646484375, 446.80798583984375], [9, 183.94017114257812, 310.1386057128906, 641.5488249511719, 651.6652321777344], [9, 119.05512695312498, 214.89450415039062, 649.1361303710937, 659.2525375976562], [9, 183.94017114257812, 268.46931127929685, 660.0955715332032, 668.5259108886719], [9, 292.8756123046875, 338.11656054687495, 658.4095036621094, 667.682876953125], [9, 119.05512695312498, 204.774818359375, 668.5259108886719, 676.9562502441406]]
2026-08-10 10:47:29,832 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=10.2s
2026-08-10 10:47:29,832 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:47:29,839 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:47:29,839 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 10:47:29,839 INFO     29 [qwen-vl-text] positions(18): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:47:29,839 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [18]
2026-08-10 10:47:30,047 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1654x2340), dpi=200
2026-08-10 10:47:30,048 INFO     29 [qwen-vl-text] LLM extraction start, text_len=249
2026-08-10 10:47:30,049 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:30,049 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 511, \"bbox_end\": 528, \"encounter_dates\": [\"2025-12-08\"], \"department\": \"呼吸与危重症一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "沈阳市第四人民医院\n处方笺\n医疗类别:市医保\nNO:25005558582\n4号窗口\n25/12/08 14:00\n普通\n病志号:55161248\n诊断:(J45.900x001)支气管哮喘\nRp\n沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n【50ug:250ug/泡*60泡/(193.60元/盒)\n1盒\n用法用量:每次300ug,吸入,每天二次\nvivo X80 · ZEISS\n医师:杨昕发药:李琳配药:巴艺洁\n2025/12/31 18:28金额合计:193.6/193.6\n第1页/共1页",
    "role": "user"
  }
]
2026-08-10 10:47:30,051 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T10:47:30.050+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"71a9158694a811f1bd9827cf206dfa2d": {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 10:47:32,260 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:32,261 INFO     29 [qwen-vl-text] LLM output (len=422):
{
  "encounter_date": "2025-12-08",
  "prescription_type": "门诊处方",
  "prescriber": "杨昕",
  "department": "呼吸与危重症一门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭",
      "drug_category": "西药",
      "dosage": "300ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": null
    }
  ]
}
2026-08-10 10:47:32,261 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-08]
2026-08-10 10:47:32,264 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1719940, prompt_len=916
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["沈阳市第四人民医院", "处方笺", "医疗类别:市医保", "NO:25005558582", "4号窗口", "25/12/08 14:00", "普通", "病志号:55161248", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "vivo X80 · ZEISS", "医师:杨昕发药:李琳配药:巴艺洁", "2025/12/31 18:28金额合计:193.6/193.6", "第1页/共1页"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord API raw response (len=1040):
[
	{"text": "沈阳市第四人民医院", "bbox": [362, 190, 628, 220]},
	{"text": "处方笺", "bbox": [454, 217, 543, 240]},
	{"text": "医疗类别:市医保", "bbox": [383, 241, 552, 263]},
	{"text": "NO:25005558582", "bbox": [268, 264, 430, 284]},
	{"text": "4号窗口", "bbox": [487, 270, 567, 289]},
	{"text": "25/12/08 14:00", "bbox": [263, 294, 424, 313],
	"text": "普通", "bbox": [485, 298, 530, 316]},
	{"text": "病志号:55161248", "bbox": [268, 327, 463, 347]},
	{"text": "诊断:(J45.900x001)支气管哮喘", "bbox": [259, 467, 495, 483]},
	{"text": "Rp", "bbox": [254, 490, 277, 505]},
	{"text": "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "bbox": [255, 523, 675, 542]},
	{"text": "【50ug:250ug/泡*60泡/(193.60元/盒)", "bbox": [284, 546, 614, 564]},
	{"text": "1盒", "bbox": [675, 550, 704, 565]},
	{"text": "用法用量:每次300ug,吸入,每天二次", "bbox": [285, 568, 597, 586]},
	{"text": "vivo X80 · ZEISS", "bbox": [31, 893, 282, 912]},
	{"text": "医师:杨昕发药:李琳配药:巴艺洁", "bbox": [255, 900, 545, 916]},
	{"text": "2025/12/31 18:28金额合计:193.6/193.6", "bbox": [31, 927, 449, 944]},
	{"text": "第1页/共1页", "bbox": [504, 925, 605, 940]}
]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=6.5s
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[0]: text=沈阳市第四人民医院, bbox=[362, 190, 628, 220]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[1]: text=处方笺, bbox=[454, 217, 543, 240]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[2]: text=医疗类别:市医保, bbox=[383, 241, 552, 263]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[3]: text=NO:25005558582, bbox=[268, 264, 430, 284]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[4]: text=4号窗口, bbox=[487, 270, 567, 289]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[5]: text=普通, bbox=[485, 298, 530, 316]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[6]: text=病志号:55161248, bbox=[268, 327, 463, 347]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[7]: text=诊断:(J45.900x001)支气管哮喘, bbox=[259, 467, 495, 483]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[8]: text=Rp, bbox=[254, 490, 277, 505]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[9]: text=沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙, bbox=[255, 523, 675, 542]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[10]: text=【50ug:250ug/泡*60泡/(193.60元/盒), bbox=[284, 546, 614, 564]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[11]: text=1盒, bbox=[675, 550, 704, 565]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[12]: text=用法用量:每次300ug,吸入,每天二次, bbox=[285, 568, 597, 586]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[13]: text=vivo X80 · ZEISS, bbox=[31, 893, 282, 912]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[14]: text=医师:杨昕发药:李琳配药:巴艺洁, bbox=[255, 900, 545, 916]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[15]: text=2025/12/31 18:28金额合计:193.6/193.6, bbox=[31, 927, 449, 944]
2026-08-10 10:47:38,772 INFO     29 [qwen-vl-text] coord item[16]: text=第1页/共1页, bbox=[504, 925, 605, 940]
2026-08-10 10:47:38,773 INFO     29 [qwen-vl-text] page=10 — 18/18 coords, api_time=6.5s
2026-08-10 10:47:38,773 INFO     29 [qwen-vl-text] new_positions (18):
[[10, 215.48977978515623, 373.8330986328125, 160.0541143798828, 185.3258166503906], [10, 270.2551381835937, 323.23466967773436, 182.79864642333985, 202.17361816406247], [10, 227.99056811523437, 328.59215039062497, 203.01600823974607, 221.54858990478513], [10, 159.5338701171875, 255.96852294921874, 222.39097998046873, 239.2387814941406], [10, 289.8992341308593, 337.52128491210937, 227.4453204345703, 243.45073187255858], [10, 288.7086828613281, 315.49608642578124, 251.03224255371092, 266.1952639160156], [10, 159.5338701171875, 275.6126188964844, 275.46155474853515, 292.309356262207], [10, 154.17638940429686, 294.66143920898435, 393.3961653442383, 406.87440655517577], [10, 151.20001123046873, 164.89135083007812, 412.7711370849609, 425.4069882202148], [10, 151.79528686523437, 401.81105346679686, 440.5700095825195, 456.5754210205078], [10, 169.05828027343748, 365.49923974609374, 459.94498132324213, 475.10800268554686], [10, 401.81105346679686, 419.07404687499996, 463.3145416259765, 475.95039276123043], [10, 169.65355590820312, 355.3795539550781, 478.4775629882812, 493.6405843505859], [10, 18.453544677734374, 167.86772900390625, 752.2543375854492, 768.2597490234375], [10, 151.79528686523437, 324.4252209472656, 758.1510681152344, 771.6293093261718], [10, 18.453544677734374, 267.2787600097656, 780.8956001586913, 795.2162314453125], [10, 300.01891992187495, 360.1417590332031, 779.2108200073242, 791.8466711425781], [10, 300.01891992187495, 360.1417590332031, 779.2108200073242, 791.8466711425781]]
2026-08-10 10:47:38,773 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=8.9s
2026-08-10 10:47:38,773 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:47:38,774 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:47:38,774 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 10:47:38,774 INFO     29 [qwen-vl-text] positions(17): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:47:38,774 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [17]
2026-08-10 10:47:38,990 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1654x2340), dpi=200
2026-08-10 10:47:38,991 INFO     29 [qwen-vl-text] LLM extraction start, text_len=218
2026-08-10 10:47:38,991 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:38,992 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 545, \"bbox_end\": 561, \"encounter_dates\": [\"2026-01-30\"], \"department\": \"呼吸与危重症一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "沈阳市第四人民医院\n处方笺\n医疗类别:市医保\nNO:26000513029\n3号窗口\n26/01/30 13:26\n普通\n科 室:呼吸与危重症一门诊\n诊断:(J45.900x001)支气管哮喘\nRp\n沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙\n【50ug:250ug/泡*60泡/(193.60元/盒)\n1盒\n用法用量:每次300ug,吸入,每天二次\n医师:杨昕发药:李琳 配药:乔军\n金额合计:193.6/193.6\n第1页/共1页",
    "role": "user"
  }
]
2026-08-10 10:47:41,278 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:41,278 INFO     29 [qwen-vl-text] LLM output (len=435):
{
  "encounter_date": "2026-01-30",
  "prescription_type": "门诊处方",
  "prescriber": "杨昕",
  "department": "呼吸与危重症一门诊",
  "diagnosis": "(J45.900x001)支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭",
      "drug_category": "西药",
      "dosage": "300ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": null
    }
  ]
}
2026-08-10 10:47:41,278 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-30]
2026-08-10 10:47:41,282 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2163548, prompt_len=882
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["沈阳市第四人民医院", "处方笺", "医疗类别:市医保", "NO:26000513029", "3号窗口", "26/01/30 13:26", "普通", "科 室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "医师:杨昕发药:李琳 配药:乔军", "金额合计:193.6/193.6", "第1页/共1页"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:47:47,409 INFO     29 [qwen-vl-text] coord API raw response (len=967):
[
	{"text": "沈阳市第四人民医院", "bbox": [333, 101, 614, 128]},
	{"text": "处方笺", "bbox": [430, 124, 524, 147]},
	{"text": "医疗类别:市医保", "bbox": [356, 148, 535, 171],
	"text": "NO:26000513029", "bbox": [230, 171, 405, 192]},
	{"text": "3号窗口", "bbox": [467, 179, 552, 198]},
	{"text": "26/01/30 13:26", "bbox": [224, 202, 400, 223]},
	{"text": "普通", "bbox": [465, 208, 513, 227]},
	{"text": "科 室:呼吸与危重症一门诊", "bbox": [227, 362, 554, 389]},
	{"text": "诊断:(J45.900x001)支气管哮喘", "bbox": [220, 390, 477, 409]},
	{"text": "Rp", "bbox": [216, 415, 242, 432]},
	{"text": "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙", "bbox": [219, 452, 667, 472]},
	{"text": "【50ug:250ug/泡*60泡/(193.60元/盒)", "bbox": [251, 477, 601, 496]},
	{"text": "1盒", "bbox": [668, 480, 697, 496]},
	{"text": "用法用量:每次300ug,吸入,每天二次", "bbox": [253, 500, 584, 519]},
	{"text": "医师:杨昕发药:李琳 配药:乔军", "bbox": [215, 870, 515, 890]},
	{"text": "金额合计:193.6/193.6", "bbox": [217, 903, 428, 924]},
	{"text": "第1页/共1页", "bbox": [490, 905, 607, 924]}
]
2026-08-10 10:47:47,409 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=6.1s
2026-08-10 10:47:47,409 INFO     29 [qwen-vl-text] coord item[0]: text=沈阳市第四人民医院, bbox=[333, 101, 614, 128]
2026-08-10 10:47:47,409 INFO     29 [qwen-vl-text] coord item[1]: text=处方笺, bbox=[430, 124, 524, 147]
2026-08-10 10:47:47,409 INFO     29 [qwen-vl-text] coord item[2]: text=NO:26000513029, bbox=[230, 171, 405, 192]
2026-08-10 10:47:47,409 INFO     29 [qwen-vl-text] coord item[3]: text=3号窗口, bbox=[467, 179, 552, 198]
2026-08-10 10:47:47,409 INFO     29 [qwen-vl-text] coord item[4]: text=26/01/30 13:26, bbox=[224, 202, 400, 223]
2026-08-10 10:47:47,409 INFO     29 [qwen-vl-text] coord item[5]: text=普通, bbox=[465, 208, 513, 227]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[6]: text=科 室:呼吸与危重症一门诊, bbox=[227, 362, 554, 389]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[7]: text=诊断:(J45.900x001)支气管哮喘, bbox=[220, 390, 477, 409]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[8]: text=Rp, bbox=[216, 415, 242, 432]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[9]: text=沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙, bbox=[219, 452, 667, 472]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[10]: text=【50ug:250ug/泡*60泡/(193.60元/盒), bbox=[251, 477, 601, 496]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[11]: text=1盒, bbox=[668, 480, 697, 496]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[12]: text=用法用量:每次300ug,吸入,每天二次, bbox=[253, 500, 584, 519]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[13]: text=医师:杨昕发药:李琳 配药:乔军, bbox=[215, 870, 515, 890]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[14]: text=金额合计:193.6/193.6, bbox=[217, 903, 428, 924]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] coord item[15]: text=第1页/共1页, bbox=[490, 905, 607, 924]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] page=12 — 17/17 coords, api_time=6.1s
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] new_positions (17):
[[12, 198.2267863769531, 365.49923974609374, 85.08139764404297, 107.8259296875], [12, 255.96852294921874, 311.92443261718745, 104.45636938476562, 123.83134112548828], [12, 136.91339599609373, 241.08663208007812, 144.04870294189453, 161.73889453125], [12, 277.99372143554683, 328.59215039062497, 150.78782354736327, 166.79323498535155], [12, 133.3417421875, 238.11025390624997, 170.16279528808593, 187.8529868774414], [12, 276.8031701660156, 305.3764006347656, 175.21713574218748, 191.22254718017578], [12, 135.12756909179686, 329.78270166015625, 304.94520739746093, 327.68973944091795], [12, 130.96063964843748, 283.9464777832031, 328.5321295166015, 344.5375409545898], [12, 128.579537109375, 144.05670361328123, 349.5918814086914, 363.9125126953125], [12, 130.36536401367186, 397.04884838867184, 380.76031420898437, 397.60811572265624], [12, 149.41418432617186, 357.7606564941406, 401.8200661010742, 417.8254775390625], [12, 397.6441240234375, 414.9071174316406, 404.34723632812495, 417.8254775390625], [12, 150.60473559570312, 347.640970703125, 421.1950378417969, 437.2004492797851], [12, 127.98426147460937, 306.56695190429684, 732.8793658447265, 749.7271673583984], [12, 129.1748127441406, 254.77797167968748, 760.6782383422851, 778.3684299316405], [12, 291.68506103515625, 361.33231030273436, 762.3630184936522, 778.3684299316405], [12, 291.68506103515625, 361.33231030273436, 762.3630184936522, 778.3684299316405]]
2026-08-10 10:47:47,410 INFO     29 [qwen-vl-text] ═══ DONE ═══ 17 positions, pages=1, time=8.6s
2026-08-10 10:47:47,424 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 10:47:47,424 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Prescription | outputs={"chunks": "4 items, types={'PrescriptionRecord': 4}", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:47:47,424 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 10:47:47,431 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:47,431 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 10:47:48,266 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:48,272 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 10:47:48,272 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:47:48,272 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 10:47:48,280 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:48,280 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 10:47:48,773 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:48,780 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 10:47:48,781 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:47:48,781 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 10:47:48,787 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:47:48,788 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:47:48,788 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 10:47:48,788 INFO     29 [qwen-vl-text] positions(41): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:47:48,788 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [41]
2026-08-10 10:47:49,100 INFO     29 [qwen-vl-text] page=1, rect=595x1290, img=(1654x3583), dpi=200
2026-08-10 10:47:49,102 INFO     29 [qwen-vl-text] LLM extraction start, text_len=665
2026-08-10 10:47:49,102 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:49,102 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 35, \"bbox_end\": 75, \"encounter_dates\": [\"2025-09-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "中国医科大学沈阳市第四人民医院\n报告单\n出生日期：1983-6-17\n性别：女\n住院号：890730\n年龄：42 Years\n身高：163 cm\n测试号：2025011002\n体重：70 kg\n预计 实1 %(实1/预) 实2 %(实2/预) 变异率\nTime\n14:07:\n14:26:\nFVC [L] 3.24 3.05 94.1 3.34 103.1 9.6\nFEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9\nFEV 1 % FVC [%] 69.69 74.33 6.7\nFEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7\nPEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5\nMEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4\nMEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 4.7 -6.2\nMEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0\nMMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\nF/V in\n医生意见：\n阻塞型轻度通气功能障碍，小气道功能障碍。\n支气管舒张试验：吸入沙丁胺醇气雾剂400微克，\nFEV1增加360毫升，改善率为16.9%。支气管舒张试验阳性。\n操作者：",
    "role": "user"
  }
]
2026-08-10 10:47:54,126 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:47:54,126 INFO     29 [qwen-vl-text] LLM output (len=882):
{
  "exam_date": "2025-01-10",
  "report_date": null,
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "预计 实1 %(实1/预) 实2 %(实2/预) 变异率\nTime\n14:07:\n14:26:\nFVC [L] 3.24 3.05 94.1 3.34 103.1 9.6\nFEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9\nFEV 1 % FVC [%] 69.69 74.33 6.7\nFEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7\nPEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5\nMEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4\nMEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 4.7 -6.2\nMEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0\nMMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\nF/V in",
  "conclusion": "阻塞型轻度通气功能障碍，小气道功能障碍。\n支气管舒张试验：吸入沙丁胺醇气雾剂400微克，\nFEV1增加360毫升，改善率为16.9%。支气管舒张试验阳性。",
  "physician": null,
  "reviewer": null
}
2026-08-10 10:47:54,130 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1927411, prompt_len=1401
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共41行）
["中国医科大学沈阳市第四人民医院", "报告单", "出生日期：1983-6-17", "性别：女", "住院号：890730", "年龄：42 Years", "身高：163 cm", "测试号：2025011002", "体重：70 kg", "预计 实1 %(实1/预) 实2 %(实2/预) 变异率", "Time", "14:07:", "14:26:", "FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6", "FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9", "FEV 1 % FVC [%] 69.69 74.33 6.7", "FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7", "PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5", "MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4", "MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 4.7 -6.2", "MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0", "MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V in", "医生意见：", "阻塞型轻度通气功能障碍，小气道功能障碍。", "支气管舒张试验：吸入沙丁胺醇气雾剂400微克，", "FEV1增加360毫升，改善率为16.9%。支气管舒张试验阳性。", "操作者："]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:48:09,499 INFO     29 [qwen-vl-text] coord API raw response (len=2447):
[
	{"text": "中国医科大学沈阳市第四人民医院", "bbox": [260, 253, 720, 272]},
	{"text": "报告单", "bbox": [490, 274, 574, 290]},
	{"text": "出生日期：1983-6-17", "bbox": [44, 303, 369, 315]},
	{"text": "性别：女", "bbox": [490, 292, 728, 305]},
	{"text": "住院号：890730", "bbox": [44, 313, 335, 326]},
	{"text": "年龄：42 Years", "bbox": [705, 305, 802, 315]},
	{"text": "身高：163 cm", "bbox": [44, 325, 335, 337]},
	{"text": "测试号：2025011002", "bbox": [490, 315, 826, 326]},
	{"text": "体重：70 kg", "bbox": [490, 326, 766, 337]},
	{"text": "预计 实1 %(实1/预) 实2 %(实2/预) 变异率", "bbox": [369, 343, 894, 358]},
	{"text": "Time", "bbox": [58, 358, 115, 369]},
	{"text": "14:07:", "bbox": [428, 358, 490, 369]},
	{"text": "14:26:", "bbox": [612, 358, 675, 369]},
	{"text": "FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6", "bbox": [58, 385, 894, 398]},
	{"text": "FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9", "bbox": [58, 398, 894, 411]},
	{"text": "FEV 1 % FVC [%] 69.69 74.33 6.7", "bbox": [58, 411, 894, 424]},
	{"text": "FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7", "bbox": [58, 424, 894, 437]},
	{"text": "PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5", "bbox": [58, 437, 894, 450]},
	{"text": "MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4", "bbox": [58, 450, 894, 464]},
	{"text": "MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 4.7 -6.2", "bbox": [58, 464, 894, 477]},
	{"text": "MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0", "bbox": [58, 477, 894, 490]},
	{"text": "MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1", "bbox": [58, 490, 894, 504]},
	{"text": "Flow [L/s]", "bbox": [104, 541, 160, 550]},
	{"text": "F/V ex", "bbox": [595, 543, 632, 551]},
	{"text": "10", "bbox": [80, 559, 94, 567]},
	{"text": "5", "bbox": [85, 585, 94, 592]},
	{"text": "0", "bbox": [85, 611, 94, 618]},
	{"text": "1", "bbox": [190, 617, 198, 624]},
	{"text": "2", "bbox": [287, 617, 296, 624]},
	{"text": "3", "bbox": [383, 617, 392, 624]},
	{"text": "4", "bbox": [479, 617, 488, 624]},
	{"text": "5", "bbox": [575, 617, 584, 624]},
	{"text": "6", "bbox": [672, 617, 681, 624]},
	{"text": "7", "bbox": [768, 617, 777, 624]},
	{"text": "10", "bbox": [80, 662, 94, 670]},
	{"text": "F/V in", "bbox": [594, 680, 627, 688]},
	{"text": "医生意见：", "bbox": [52, 706, 170, 719]},
	{"text": "阻塞型轻度通气功能障碍，小气道功能障碍。", "bbox": [52, 725, 435, 736]},
	{"text": "支气管舒张试验：吸入沙丁胺醇气雾剂400微克，", "bbox": [52, 735, 465, 746]},
	{"text": "FEV1增加360毫升，改善率为16.9%。支气管舒张试验阳性。", "bbox": [52, 744, 595, 756]},
	{"text": "操作者：", "bbox": [636, 811, 726, 826]}
]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord API: raw_items=41, valid_items=41, elapsed=15.4s
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[0]: text=中国医科大学沈阳市第四人民医院, bbox=[260, 253, 720, 272]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[1]: text=报告单, bbox=[490, 274, 574, 290]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[2]: text=出生日期：1983-6-17, bbox=[44, 303, 369, 315]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[490, 292, 728, 305]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[4]: text=住院号：890730, bbox=[44, 313, 335, 326]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：42 Years, bbox=[705, 305, 802, 315]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[6]: text=身高：163 cm, bbox=[44, 325, 335, 337]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：2025011002, bbox=[490, 315, 826, 326]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[8]: text=体重：70 kg, bbox=[490, 326, 766, 337]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[9]: text=预计 实1 %(实1/预) 实2 %(实2/预) 变异率, bbox=[369, 343, 894, 358]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[10]: text=Time, bbox=[58, 358, 115, 369]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[11]: text=14:07:, bbox=[428, 358, 490, 369]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[12]: text=14:26:, bbox=[612, 358, 675, 369]
2026-08-10 10:48:09,500 INFO     29 [qwen-vl-text] coord item[13]: text=FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6, bbox=[58, 385, 894, 398]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[14]: text=FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9, bbox=[58, 398, 894, 411]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[15]: text=FEV 1 % FVC [%] 69.69 74.33 6.7, bbox=[58, 411, 894, 424]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[16]: text=FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7, bbox=[58, 424, 894, 437]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[17]: text=PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5, bbox=[58, 437, 894, 450]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[18]: text=MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4, bbox=[58, 450, 894, 464]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[19]: text=MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 4.7 -6.2, bbox=[58, 464, 894, 477]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[20]: text=MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0, bbox=[58, 477, 894, 490]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[21]: text=MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1, bbox=[58, 490, 894, 504]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[22]: text=Flow [L/s], bbox=[104, 541, 160, 550]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[23]: text=F/V ex, bbox=[595, 543, 632, 551]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[24]: text=10, bbox=[80, 559, 94, 567]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[25]: text=5, bbox=[85, 585, 94, 592]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[26]: text=0, bbox=[85, 611, 94, 618]
2026-08-10 10:48:09,501 INFO     29 [qwen-vl-text] coord item[27]: text=1, bbox=[190, 617, 198, 624]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[28]: text=2, bbox=[287, 617, 296, 624]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[29]: text=3, bbox=[383, 617, 392, 624]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[30]: text=4, bbox=[479, 617, 488, 624]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[31]: text=5, bbox=[575, 617, 584, 624]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[32]: text=6, bbox=[672, 617, 681, 624]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[33]: text=7, bbox=[768, 617, 777, 624]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[34]: text=10, bbox=[80, 662, 94, 670]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[35]: text=F/V in, bbox=[594, 680, 627, 688]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[36]: text=医生意见：, bbox=[52, 706, 170, 719]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[37]: text=阻塞型轻度通气功能障碍，小气道功能障碍。, bbox=[52, 725, 435, 736]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[38]: text=支气管舒张试验：吸入沙丁胺醇气雾剂400微克，, bbox=[52, 735, 465, 746]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[39]: text=FEV1增加360毫升，改善率为16.9%。支气管舒张试验阳性。, bbox=[52, 744, 595, 756]
2026-08-10 10:48:09,502 INFO     29 [qwen-vl-text] coord item[40]: text=操作者：, bbox=[636, 811, 726, 826]
2026-08-10 10:48:09,503 INFO     29 [qwen-vl-text] page=1 — 41/41 coords, api_time=15.4s
2026-08-10 10:48:09,503 INFO     29 [qwen-vl-text] new_positions (41):
[[1, 154.7716650390625, 428.59845703124995, 326.3102707519531, 350.81578515624994], [1, 291.68506103515625, 341.68821435546874, 353.3953129882812, 374.03153564453123], [1, 26.192127929687498, 219.6567092285156, 390.79846655273434, 406.27563354492185], [1, 291.68506103515625, 433.36066210937497, 376.6110634765625, 393.3779943847656], [1, 26.192127929687498, 199.41733764648436, 403.6961057128906, 420.4630366210937], [1, 419.6693225097656, 477.4110590820312, 393.3779943847656, 406.27563354492185], [1, 26.192127929687498, 199.41733764648436, 419.1732727050781, 434.6504396972656], [1, 291.68506103515625, 491.6976743164062, 406.27563354492185, 420.4630366210937], [1, 291.68506103515625, 455.98113623046873, 420.4630366210937, 434.6504396972656], [1, 219.6567092285156, 532.1764174804687, 442.3890231933593, 461.7354819335937], [1, 34.525986816406245, 68.45669799804686, 461.7354819335937, 475.9228850097656], [1, 254.77797167968748, 291.68506103515625, 461.7354819335937, 475.9228850097656], [1, 364.30868847656245, 401.81105346679686, 461.7354819335937, 475.9228850097656], [1, 34.525986816406245, 532.1764174804687, 496.55910766601556, 513.3260385742187], [1, 34.525986816406245, 532.1764174804687, 513.3260385742187, 530.0929694824218], [1, 34.525986816406245, 532.1764174804687, 530.0929694824218, 546.859900390625], [1, 34.525986816406245, 532.1764174804687, 546.859900390625, 563.626831298828], [1, 34.525986816406245, 532.1764174804687, 563.626831298828, 580.3937622070312], [1, 34.525986816406245, 532.1764174804687, 580.3937622070312, 598.4504570312499], [1, 34.525986816406245, 532.1764174804687, 598.4504570312499, 615.217387939453], [1, 34.525986816406245, 532.1764174804687, 615.217387939453, 631.9843188476563], [1, 34.525986816406245, 532.1764174804687, 631.9843188476563, 650.0410136718749], [1, 61.908666015624995, 95.24410156249999, 697.762278564453, 709.3701538085937], [1, 354.1890026855468, 376.21420117187495, 700.3418063964843, 710.6599177246093], [1, 47.622050781249996, 55.95590966796875, 720.9780290527343, 731.2961403808594], [1, 50.59842895507812, 55.95590966796875, 754.5118908691405, 763.5402382812499], [1, 50.59842895507812, 55.95590966796875, 788.0457526855469, 797.0741000976562], [1, 113.10237060546874, 117.86457568359374, 795.7843361816406, 804.81268359375], [1, 170.84410717773437, 176.20158789062498, 795.7843361816406, 804.81268359375], [1, 227.99056811523437, 233.34804882812497, 795.7843361816406, 804.81268359375], [1, 285.13702905273436, 290.49450976562497, 795.7843361816406, 804.81268359375], [1, 342.28348999023433, 347.640970703125, 795.7843361816406, 804.81268359375], [1, 400.02522656249994, 405.3827072753906, 795.7843361816406, 804.81268359375], [1, 457.17168749999996, 462.52916821289057, 795.7843361816406, 804.81268359375], [1, 47.622050781249996, 55.95590966796875, 853.8237124023436, 864.1418237304687], [1, 353.59372705078124, 373.23782299804685, 877.0394628906249, 887.35757421875], [1, 30.954333007812497, 101.19685791015624, 910.5733247070311, 927.3402556152344], [1, 30.954333007812497, 258.94490112304686, 935.0788391113281, 949.2662421875], [1, 30.954333007812497, 276.8031701660156, 947.9764782714843, 962.1638813476562], [1, 30.954333007812497, 354.1890026855468, 959.5843535156249, 975.0615205078125], [1, 378.59530371093746, 432.1701108398437, 1045.9985358886718, 1065.344994628906]]
2026-08-10 10:48:09,503 INFO     29 [qwen-vl-text] ═══ DONE ═══ 41 positions, pages=1, time=20.7s
2026-08-10 10:48:09,503 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 10:48:09,512 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 10:48:09,512 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 10:48:09,513 INFO     29 [qwen-vl-text] positions(125): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 10:48:09,513 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [125]
2026-08-10 10:48:09,850 INFO     29 [qwen-vl-text] page=2, rect=595x1290, img=(1654x3583), dpi=200
2026-08-10 10:48:09,852 INFO     29 [qwen-vl-text] LLM extraction start, text_len=770
2026-08-10 10:48:09,852 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:48:09,853 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 84, \"bbox_end\": 208, \"encounter_dates\": [\"2025-09-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "中国医科大学沈阳市第四人民医院\n肺功能报告单\n姓名：\n出生日期：\n1983-6-17\n住院号：\n890730\n身高：\n163 cm\n性别：\n女\n年龄：\n42 Years\n测试号：\n2025011002\n体重：\n70 kg\nDate\nTime\n预计\n实测\n%(实/预)\n25-9-02\n14:07:38\nVT\n[L]\n0.50\nBF\n[1/min]\n20.00\nMV\n[L/min]\n10.00\nERV\n[L]\n1.07\nVC MAX\n[L]\n3.31\n3.36\n101.6\nFVC\n[L]\n3.24\n3.05\n94.1\nFEV 1\n[L]\n2.79\n2.12\n76.1\nFEV 1 % FVC\n[%]\n69.69\nFEV 1 % VC MAX\n[%]\n81.12\n63.16\n77.9\nPEF\n[L/s]\n6.59\n6.83\n103.5\nMEF 75\n[L/s]\n5.80\n3.41\n58.8\nMEF 50\n[L/s]\n4.10\n2.30\n56.2\nMEF 25\n[L/s]\n1.77\n0.45\n25.4\nMMEF 75/25\n[L/s]\n3.53\n0.95\n26.9\nMVV\n[L/min]\n103.77\nFEV 1*30\n[L/min]\n103.77\n63.70\n61.4\nRV-SB\n[L]\n1.62\n2.06\n127.2\nRV%TLC-SB\n[%]\n33.24\n40.20\n120.9\nTLC-SB\n[L]\n4.97\n5.13\n103.3\nFRC-SB\n[L]\n2.69\n2.97\n110.3\nFRC%TLC-SB\n[%]\n51.82\n57.88\n111.7\nDLCO SB\n[mmol/min/kPa]\n8.54\n5.51\n(64.6)\n医生意见：\n阻塞型轻度通气功能障碍，小气道功能障碍。\n弥散功能降低。残总比 40.20 %。",
    "role": "user"
  }
]
2026-08-10 10:48:09,854 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T10:48:09.854+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"71a9158694a811f1bd9827cf206dfa2d": {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 10:48:16,851 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:48:16,851 INFO     29 [qwen-vl-text] LLM output (len=1285):
{
  "exam_date": "2025-09-02",
  "report_date": "2025-09-02",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | 单位 | 预计值 | 实测值 | %(实/预) |\n|---|---|---|---|---|\n| VT | [L] | 0.50 | - | - |\n| BF | [1/min] | 20.00 | - | - |\n| MV | [L/min] | 10.00 | - | - |\n| ERV | [L] | 1.07 | - | - |\n| VC MAX | [L] | 3.31 | 3.36 | 101.6 |\n| FVC | [L] | 3.24 | 3.05 | 94.1 |\n| FEV 1 | [L] | 2.79 | 2.12 | 76.1 |\n| FEV 1 % FVC | [%] | 69.69 | - | - |\n| FEV 1 % VC MAX | [%] | 81.12 | 63.16 | 77.9 |\n| PEF | [L/s] | 6.59 | 6.83 | 103.5 |\n| MEF 75 | [L/s] | 5.80 | 3.41 | 58.8 |\n| MEF 50 | [L/s] | 4.10 | 2.30 | 56.2 |\n| MEF 25 | [L/s] | 1.77 | 0.45 | 25.4 |\n| MMEF 75/25 | [L/s] | 3.53 | 0.95 | 26.9 |\n| MVV | [L/min] | 103.77 | - | - |\n| FEV 1*30 | [L/min] | 103.77 | 63.70 | 61.4 |\n| RV-SB | [L] | 1.62 | 2.06 | 127.2 |\n| RV%TLC-SB | [%] | 33.24 | 40.20 | 120.9 |\n| TLC-SB | [L] | 4.97 | 5.13 | 103.3 |\n| FRC-SB | [L] | 2.69 | 2.97 | 110.3 |\n| FRC%TLC-SB | [%] | 51.82 | 57.88 | 111.7 |\n| DLCO SB | [mmol/min/kPa] | 8.54 | 5.51 | (64.6) |",
  "conclusion": "阻塞型轻度通气功能障碍，小气道功能障碍。\n弥散功能降低。残总比 40.20 %。",
  "physician": null,
  "reviewer": null
}
2026-08-10 10:48:16,861 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2329839, prompt_len=1759
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共125行）
["中国医科大学沈阳市第四人民医院", "肺功能报告单", "姓名：", "出生日期：", "1983-6-17", "住院号：", "890730", "身高：", "163 cm", "性别：", "女", "年龄：", "42 Years", "测试号：", "2025011002", "体重：", "70 kg", "Date", "Time", "预计", "实测", "%(实/预)", "25-9-02", "14:07:38", "VT", "[L]", "0.50", "BF", "[1/min]", "20.00", "MV", "[L/min]", "10.00", "ERV", "[L]", "1.07", "VC MAX", "[L]", "3.31", "3.36", "101.6", "FVC", "[L]", "3.24", "3.05", "94.1", "FEV 1", "[L]", "2.79", "2.12", "76.1", "FEV 1 % FVC", "[%]", "69.69", "FEV 1 % VC MAX", "[%]", "81.12", "63.16", "77.9", "PEF", "[L/s]", "6.59", "6.83", "103.5", "MEF 75", "[L/s]", "5.80", "3.41", "58.8", "MEF 50", "[L/s]", "4.10", "2.30", "56.2", "MEF 25", "[L/s]", "1.77", "0.45", "25.4", "MMEF 75/25", "[L/s]", "3.53", "0.95", "26.9", "MVV", "[L/min]", "103.77", "FEV 1*30", "[L/min]", "103.77", "63.70", "61.4", "RV-SB", "[L]", "1.62", "2.06", "127.2", "RV%TLC-SB", "[%]", "33.24", "40.20", "120.9", "TLC-SB", "[L]", "4.97", "5.13", "103.3", "FRC-SB", "[L]", "2.69", "2.97", "110.3", "FRC%TLC-SB", "[%]", "51.82", "57.88", "111.7", "DLCO SB", "[mmol/min/kPa]", "8.54", "5.51", "(64.6)", "医生意见：", "阻塞型轻度通气功能障碍，小气道功能障碍。", "弥散功能降低。残总比 40.20 %。"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 10:48:49,876 INFO     29 [qwen-vl-text] coord API raw response (len=6195):
[
	{"text": "中国医科大学沈阳市第四人民医院", "bbox": [258, 215, 765, 234]},
	{"text": "肺功能报告单", "bbox": [422, 233, 601, 248]},
	{"text": "姓名：", "bbox": [79, 251, 133, 263]},
	{"text": "出生日期：", "bbox": [79, 263, 176, 275]},
	{"text": "1983-6-17", "bbox": [285, 266, 382, 277]},
	{"text": "住院号：", "bbox": [79, 275, 155, 287]},
	{"text": "890730", "bbox": [285, 278, 351, 289]},
	{"text": "身高：", "bbox": [79, 287, 133, 299]},
	{"text": "163 cm", "bbox": [285, 290, 351, 301]},
	{"text": "性别：", "bbox": [500, 253, 553, 265]},
	{"text": "女", "bbox": [703, 253, 724, 265]},
	{"text": "年龄：", "bbox": [500, 265, 553, 277]},
	{"text": "42 Years", "bbox": [702, 266, 787, 277]},
	{"text": "测试号：", "bbox": [500, 277, 574, 289]},
	{"text": "2025011002", "bbox": [702, 278, 808, 289]},
	{"text": "体重：", "bbox": [500, 289, 553, 301]},
	{"text": "70 kg", "bbox": [702, 290, 756, 301]},
	{"text": "Date", "bbox": [68, 326, 115, 337]},
	{"text": "Time", "bbox": [68, 338, 115, 349]},
	{"text": "预计", "bbox": [418, 313, 464, 325]},
	{"text": "实测 %(实/预)", "bbox": [513, 313, 662, 325]},
	{"text": "25-9-02", "bbox": [483, 326, 560, 337]},
	{"text": "14:07:38", "bbox": [475, 338, 560, 349]},
	{"text": "VT", "bbox": [68, 361, 93, 372]},
	{"text": "[L]", "bbox": [346, 361, 377, 372]},
	{"text": "0.50", "bbox": [418, 361, 464, 372]},
	{"text": "BF", "bbox": [68, 373, 93, 384]},
	{"text": "[1/min]", "bbox": [300, 373, 377, 384]},
	{"text": "20.00", "bbox": [408, 373, 464, 384]},
	{"text": "MV", "bbox": [68, 385, 93, 396]},
	{"text": "[L/min]", "bbox": [300, 385, 377, 396]},
	{"text": "10.00", "bbox": [408, 385, 464, 396]},
	{"text": "ERV", "bbox": [68, 397, 104, 408]},
	{"text": "[L]", "bbox": [346, 397, 377, 408]},
	{"text": "1.07", "bbox": [418, 397, 464, 408]},
	{"text": "VC MAX", "bbox": [68, 408, 138, 419]},
	{"text": "[L]", "bbox": [346, 408, 377, 419]},
	{"text": "3.31", "bbox": [418, 408, 464, 419]},
	{"text": "3.36", "bbox": [513, 408, 559, 419]},
	{"text": "101.6", "bbox": [612, 408, 667, 419]},
	{"text": "FVC", "bbox": [68, 431, 104, 442]},
	{"text": "[L]", "bbox": [346, 431, 377, 442]},
	{"text": "3.24", "bbox": [418, 431, 464, 442]},
	{"text": "3.05", "bbox": [513, 431, 559, 442]},
	{"text": "94.1", "bbox": [621, 431, 667, 442]},
	{"text": "FEV 1", "bbox": [68, 443, 124, 454]},
	{"text": "[L]", "bbox": [346, 443, 377, 454]},
	{"text": "2.79", "bbox": [418, 443, 464, 454]},
	{"text": "2.12", "bbox": [513, 443, 559, 454]},
	{"text": "76.1", "bbox": [621, 443, 667, 454]},
	{"text": "FEV 1 % FVC", "bbox": [68, 455, 193, 466]},
	{"text": "[%]", "bbox": [346, 455, 377, 466]},
	{"text": "69.69", "bbox": [504, 455, 559, 466]},
	{"text": "FEV 1 % VC MAX", "bbox": [68, 466, 226, 477]},
	{"text": "[%]", "bbox": [346, 466, 377, 477]},
	{"text": "81.12", "bbox": [408, 466, 464, 477]},
	{"text": "63.16", "bbox": [504, 466, 559, 477]},
	{"text": "77.9", "bbox": [621, 466, 667, 477]},
	{"text": "PEF", "bbox": [68, 478, 104, 489]},
	{"text": "[L/s]", "bbox": [323, 478, 377, 489]},
	{"text": "6.59", "bbox": [418, 478, 464, 489]},
	{"text": "6.83", "bbox": [513, 478, 559, 489]},
	{"text": "103.5", "bbox": [612, 478, 667, 489]},
	{"text": "MEF 75", "bbox": [68, 489, 138, 500]},
	{"text": "[L/s]", "bbox": [323, 489, 377, 500]},
	{"text": "5.80", "bbox": [418, 489, 464, 500]},
	{"text": "3.41", "bbox": [513, 489, 559, 500]},
	{"text": "58.8", "bbox": [621, 489, 667, 500]},
	{"text": "MEF 50", "bbox": [68, 501, 138, 512]},
	{"text": "[L/s]", "bbox": [323, 501, 377, 512]},
	{"text": "4.10", "bbox": [418, 501, 464, 512]},
	{"text": "2.30", "bbox": [513, 501, 559, 512]},
	{"text": "56.2", "bbox": [621, 501, 667, 512]},
	{"text": "MEF 25", "bbox": [68, 512, 138, 523]},
	{"text": "[L/s]", "bbox": [323, 512, 377, 523]},
	{"text": "1.77", "bbox": [418, 512, 464, 523]},
	{"text": "0.45", "bbox": [513, 512, 559, 523]},
	{"text": "25.4", "bbox": [621, 512, 667, 523]},
	{"text": "MMEF 75/25", "bbox": [68, 523, 183, 534]},
	{"text": "[L/s]", "bbox": [323, 523, 377, 534]},
	{"text": "3.53", "bbox": [418, 523, 464, 534]},
	{"text": "0.95", "bbox": [513, 523, 559, 534]},
	{"text": "26.9", "bbox": [621, 523, 667, 534]},
	{"text": "MVV", "bbox": [68, 545, 104, 556]},
	{"text": "[L/min]", "bbox": [300, 545, 377, 556]},
	{"text": "103.77", "bbox": [398, 545, 464, 556]},
	{"text": "FEV 1*30", "bbox": [68, 557, 161, 568]},
	{"text": "[L/min]", "bbox": [300, 557, 377, 568]},
	{"text": "103.77", "bbox": [398, 557, 464, 568]},
	{"text": "63.70", "bbox": [504, 557, 559, 568]},
	{"text": "61.4", "bbox": [621, 557, 667, 568]},
	{"text": "RV-SB", "bbox": [68, 579, 130, 590]},
	{"text": "[L]", "bbox": [346, 579, 377, 590]},
	{"text": "1.62", "bbox": [418, 579, 464, 590]},
	{"text": "2.06", "bbox": [513, 579, 559, 590]},
	{"text": "127.2", "bbox": [612, 579, 667, 590]},
	{"text": "RV%TLC-SB", "bbox": [68, 591, 173, 602]},
	{"text": "[%]", "bbox": [346, 591, 377, 602]},
	{"text": "33.24", "bbox": [408, 591, 464, 602]},
	{"text": "40.20", "bbox": [504, 591, 559, 602]},
	{"text": "120.9", "bbox": [612, 591, 667, 602]},
	{"text": "TLC-SB", "bbox": [68, 603, 140, 614]},
	{"text": "[L]", "bbox": [346, 603, 377, 614]},
	{"text": "4.97", "bbox": [418, 603, 464, 614]},
	{"text": "5.13", "bbox": [513, 603, 559, 614]},
	{"text": "103.3", "bbox": [612, 603, 667, 614]},
	{"text": "FRC-SB", "bbox": [68, 614, 140, 625]},
	{"text": "[L]", "bbox": [346, 614, 377, 625]},
	{"text": "2.69", "bbox": [418, 614, 464, 625]},
	{"text": "2.97", "bbox": [513, 614, 559, 625]},
	{"text": "110.3", "bbox": [612, 614, 667, 625]},
	{"text": "FRC%TLC-SB", "bbox": [68, 626, 183, 637]},
	{"text": "[%]", "bbox": [346, 626, 377, 637]},
	{"text": "51.82", "bbox": [408, 626, 464, 637]},
	{"text": "57.88", "bbox": [504, 626, 559, 637]},
	{"text": "111.7", "bbox": [612, 626, 667, 637]},
	{"text": "DLCO SB", "bbox": [68, 637, 150, 648]},
	{"text": "[mmol/min/kPa]", "bbox": [223, 637, 377, 648]},
	{"text": "8.54", "bbox": [418, 637, 464, 648]},
	{"text": "5.51", "bbox": [513, 637, 559, 648]},
	{"text": "(64.6)", "bbox": [612, 637, 667, 648]},
	{"text": "医生意见：", "bbox": [62, 688, 190, 703]},
	{"text": "阻塞型轻度通气功能障碍，小气道功能障碍。", "bbox": [55, 709, 477, 720]},
	{"text": "弥散功能降低。残总比 40.20 %。", "bbox": [55, 719, 380, 730]}
]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord API: raw_items=124, valid_items=124, elapsed=33.0s
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[0]: text=中国医科大学沈阳市第四人民医院, bbox=[258, 215, 765, 234]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能报告单, bbox=[422, 233, 601, 248]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[79, 251, 133, 263]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[3]: text=出生日期：, bbox=[79, 263, 176, 275]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[4]: text=1983-6-17, bbox=[285, 266, 382, 277]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[79, 275, 155, 287]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[6]: text=890730, bbox=[285, 278, 351, 289]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[7]: text=身高：, bbox=[79, 287, 133, 299]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[8]: text=163 cm, bbox=[285, 290, 351, 301]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[9]: text=性别：, bbox=[500, 253, 553, 265]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[10]: text=女, bbox=[703, 253, 724, 265]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[11]: text=年龄：, bbox=[500, 265, 553, 277]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[12]: text=42 Years, bbox=[702, 266, 787, 277]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[13]: text=测试号：, bbox=[500, 277, 574, 289]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[14]: text=2025011002, bbox=[702, 278, 808, 289]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[15]: text=体重：, bbox=[500, 289, 553, 301]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[16]: text=70 kg, bbox=[702, 290, 756, 301]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[17]: text=Date, bbox=[68, 326, 115, 337]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[18]: text=Time, bbox=[68, 338, 115, 349]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[19]: text=预计, bbox=[418, 313, 464, 325]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[20]: text=实测 %(实/预), bbox=[513, 313, 662, 325]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[21]: text=25-9-02, bbox=[483, 326, 560, 337]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[22]: text=14:07:38, bbox=[475, 338, 560, 349]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[23]: text=VT, bbox=[68, 361, 93, 372]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[24]: text=[L], bbox=[346, 361, 377, 372]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[25]: text=0.50, bbox=[418, 361, 464, 372]
2026-08-10 10:48:49,877 INFO     29 [qwen-vl-text] coord item[26]: text=BF, bbox=[68, 373, 93, 384]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[27]: text=[1/min], bbox=[300, 373, 377, 384]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[28]: text=20.00, bbox=[408, 373, 464, 384]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[29]: text=MV, bbox=[68, 385, 93, 396]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[30]: text=[L/min], bbox=[300, 385, 377, 396]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[31]: text=10.00, bbox=[408, 385, 464, 396]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[32]: text=ERV, bbox=[68, 397, 104, 408]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[33]: text=[L], bbox=[346, 397, 377, 408]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[34]: text=1.07, bbox=[418, 397, 464, 408]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[35]: text=VC MAX, bbox=[68, 408, 138, 419]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[36]: text=[L], bbox=[346, 408, 377, 419]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[37]: text=3.31, bbox=[418, 408, 464, 419]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[38]: text=3.36, bbox=[513, 408, 559, 419]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[39]: text=101.6, bbox=[612, 408, 667, 419]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[40]: text=FVC, bbox=[68, 431, 104, 442]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[41]: text=[L], bbox=[346, 431, 377, 442]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[42]: text=3.24, bbox=[418, 431, 464, 442]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[43]: text=3.05, bbox=[513, 431, 559, 442]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[44]: text=94.1, bbox=[621, 431, 667, 442]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[45]: text=FEV 1, bbox=[68, 443, 124, 454]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[46]: text=[L], bbox=[346, 443, 377, 454]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[47]: text=2.79, bbox=[418, 443, 464, 454]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[48]: text=2.12, bbox=[513, 443, 559, 454]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[49]: text=76.1, bbox=[621, 443, 667, 454]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[50]: text=FEV 1 % FVC, bbox=[68, 455, 193, 466]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[51]: text=[%], bbox=[346, 455, 377, 466]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[52]: text=69.69, bbox=[504, 455, 559, 466]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[53]: text=FEV 1 % VC MAX, bbox=[68, 466, 226, 477]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[54]: text=[%], bbox=[346, 466, 377, 477]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[55]: text=81.12, bbox=[408, 466, 464, 477]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[56]: text=63.16, bbox=[504, 466, 559, 477]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[57]: text=77.9, bbox=[621, 466, 667, 477]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[58]: text=PEF, bbox=[68, 478, 104, 489]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[59]: text=[L/s], bbox=[323, 478, 377, 489]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[60]: text=6.59, bbox=[418, 478, 464, 489]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[61]: text=6.83, bbox=[513, 478, 559, 489]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[62]: text=103.5, bbox=[612, 478, 667, 489]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[63]: text=MEF 75, bbox=[68, 489, 138, 500]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[64]: text=[L/s], bbox=[323, 489, 377, 500]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[65]: text=5.80, bbox=[418, 489, 464, 500]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[66]: text=3.41, bbox=[513, 489, 559, 500]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[67]: text=58.8, bbox=[621, 489, 667, 500]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[68]: text=MEF 50, bbox=[68, 501, 138, 512]
2026-08-10 10:48:49,878 INFO     29 [qwen-vl-text] coord item[69]: text=[L/s], bbox=[323, 501, 377, 512]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[70]: text=4.10, bbox=[418, 501, 464, 512]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[71]: text=2.30, bbox=[513, 501, 559, 512]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[72]: text=56.2, bbox=[621, 501, 667, 512]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[73]: text=MEF 25, bbox=[68, 512, 138, 523]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[74]: text=[L/s], bbox=[323, 512, 377, 523]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[75]: text=1.77, bbox=[418, 512, 464, 523]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[76]: text=0.45, bbox=[513, 512, 559, 523]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[77]: text=25.4, bbox=[621, 512, 667, 523]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[78]: text=MMEF 75/25, bbox=[68, 523, 183, 534]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[79]: text=[L/s], bbox=[323, 523, 377, 534]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[80]: text=3.53, bbox=[418, 523, 464, 534]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[81]: text=0.95, bbox=[513, 523, 559, 534]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[82]: text=26.9, bbox=[621, 523, 667, 534]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[83]: text=MVV, bbox=[68, 545, 104, 556]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[84]: text=[L/min], bbox=[300, 545, 377, 556]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[85]: text=103.77, bbox=[398, 545, 464, 556]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[86]: text=FEV 1*30, bbox=[68, 557, 161, 568]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[87]: text=[L/min], bbox=[300, 557, 377, 568]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[88]: text=103.77, bbox=[398, 557, 464, 568]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[89]: text=63.70, bbox=[504, 557, 559, 568]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[90]: text=61.4, bbox=[621, 557, 667, 568]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[91]: text=RV-SB, bbox=[68, 579, 130, 590]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[92]: text=[L], bbox=[346, 579, 377, 590]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[93]: text=1.62, bbox=[418, 579, 464, 590]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[94]: text=2.06, bbox=[513, 579, 559, 590]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[95]: text=127.2, bbox=[612, 579, 667, 590]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[96]: text=RV%TLC-SB, bbox=[68, 591, 173, 602]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[97]: text=[%], bbox=[346, 591, 377, 602]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[98]: text=33.24, bbox=[408, 591, 464, 602]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[99]: text=40.20, bbox=[504, 591, 559, 602]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[100]: text=120.9, bbox=[612, 591, 667, 602]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[101]: text=TLC-SB, bbox=[68, 603, 140, 614]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[102]: text=[L], bbox=[346, 603, 377, 614]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[103]: text=4.97, bbox=[418, 603, 464, 614]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[104]: text=5.13, bbox=[513, 603, 559, 614]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[105]: text=103.3, bbox=[612, 603, 667, 614]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[106]: text=FRC-SB, bbox=[68, 614, 140, 625]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[107]: text=[L], bbox=[346, 614, 377, 625]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[108]: text=2.69, bbox=[418, 614, 464, 625]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[109]: text=2.97, bbox=[513, 614, 559, 625]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[110]: text=110.3, bbox=[612, 614, 667, 625]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[111]: text=FRC%TLC-SB, bbox=[68, 626, 183, 637]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[112]: text=[%], bbox=[346, 626, 377, 637]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[113]: text=51.82, bbox=[408, 626, 464, 637]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[114]: text=57.88, bbox=[504, 626, 559, 637]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[115]: text=111.7, bbox=[612, 626, 667, 637]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[116]: text=DLCO SB, bbox=[68, 637, 150, 648]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[117]: text=[mmol/min/kPa], bbox=[223, 637, 377, 648]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[118]: text=8.54, bbox=[418, 637, 464, 648]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[119]: text=5.51, bbox=[513, 637, 559, 648]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[120]: text=(64.6), bbox=[612, 637, 667, 648]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[121]: text=医生意见：, bbox=[62, 688, 190, 703]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[122]: text=阻塞型轻度通气功能障碍，小气道功能障碍。, bbox=[55, 709, 477, 720]
2026-08-10 10:48:49,879 INFO     29 [qwen-vl-text] coord item[123]: text=弥散功能降低。残总比 40.20 %。, bbox=[55, 719, 380, 730]
2026-08-10 10:48:49,880 INFO     29 [qwen-vl-text] page=2 — 125/125 coords, api_time=33.0s
2026-08-10 10:48:49,880 INFO     29 [qwen-vl-text] new_positions (125):
[[2, 153.58111376953124, 455.3858605957031, 277.29924194335933, 301.8047563476562], [2, 251.20631787109372, 357.7606564941406, 300.5149924316406, 319.861451171875], [2, 47.02677514648437, 79.17165942382812, 323.73074291992185, 339.20790991210936], [2, 47.02677514648437, 104.76851171874999, 339.20790991210936, 354.68507690429686], [2, 169.65355590820312, 227.39529248046873, 343.0772016601562, 357.2646047363281], [2, 47.02677514648437, 92.26772338867187, 354.68507690429686, 370.16224389648437], [2, 169.65355590820312, 208.94174780273437, 358.5543686523437, 372.7417717285156], [2, 47.02677514648437, 79.17165942382812, 370.16224389648437, 385.6394108886718], [2, 169.65355590820312, 208.94174780273437, 374.03153564453123, 388.2189387207031], [2, 297.6378173828125, 329.1874260253906, 326.3102707519531, 341.7874377441406], [2, 418.4787712402343, 430.97955957031246, 326.3102707519531, 341.7874377441406], [2, 297.6378173828125, 329.1874260253906, 341.7874377441406, 357.2646047363281], [2, 417.88349560546874, 468.4819245605468, 343.0772016601562, 357.2646047363281], [2, 297.6378173828125, 341.68821435546874, 357.2646047363281, 372.7417717285156], [2, 417.88349560546874, 480.98271289062495, 358.5543686523437, 372.7417717285156], [2, 297.6378173828125, 329.1874260253906, 372.7417717285156, 388.2189387207031], [2, 417.88349560546874, 450.0283798828125, 374.03153564453123, 388.2189387207031], [2, 40.47874316406249, 68.45669799804686, 420.4630366210937, 434.6504396972656], [2, 40.47874316406249, 68.45669799804686, 435.9402036132812, 450.1276066894531], [2, 248.82521533203123, 276.20789453124996, 403.6961057128906, 419.1732727050781], [2, 305.3764006347656, 394.0724702148437, 403.6961057128906, 419.1732727050781], [2, 287.5181315917969, 333.35435546875, 420.4630366210937, 434.6504396972656], [2, 282.75592651367185, 333.35435546875, 435.9402036132812, 450.1276066894531], [2, 40.47874316406249, 55.36063403320312, 465.6047736816406, 479.79217675781246], [2, 205.96536962890625, 224.4189143066406, 465.6047736816406, 479.79217675781246], [2, 248.82521533203123, 276.20789453124996, 465.6047736816406, 479.79217675781246], [2, 40.47874316406249, 55.36063403320312, 481.0819406738281, 495.26934374999996], [2, 178.5826904296875, 224.4189143066406, 481.0819406738281, 495.26934374999996], [2, 242.872458984375, 276.20789453124996, 481.0819406738281, 495.26934374999996], [2, 40.47874316406249, 55.36063403320312, 496.55910766601556, 510.74651074218747], [2, 178.5826904296875, 224.4189143066406, 496.55910766601556, 510.74651074218747], [2, 242.872458984375, 276.20789453124996, 496.55910766601556, 510.74651074218747], [2, 40.47874316406249, 61.908666015624995, 512.0362746582031, 526.223677734375], [2, 205.96536962890625, 224.4189143066406, 512.0362746582031, 526.223677734375], [2, 248.82521533203123, 276.20789453124996, 512.0362746582031, 526.223677734375], [2, 40.47874316406249, 82.14803759765624, 526.223677734375, 540.4110808105469], [2, 205.96536962890625, 224.4189143066406, 526.223677734375, 540.4110808105469], [2, 248.82521533203123, 276.20789453124996, 526.223677734375, 540.4110808105469], [2, 305.3764006347656, 332.75907983398434, 526.223677734375, 540.4110808105469], [2, 364.30868847656245, 397.04884838867184, 526.223677734375, 540.4110808105469], [2, 40.47874316406249, 61.908666015624995, 555.8882478027343, 570.0756508789062], [2, 205.96536962890625, 224.4189143066406, 555.8882478027343, 570.0756508789062], [2, 248.82521533203123, 276.20789453124996, 555.8882478027343, 570.0756508789062], [2, 305.3764006347656, 332.75907983398434, 555.8882478027343, 570.0756508789062], [2, 369.6661691894531, 397.04884838867184, 555.8882478027343, 570.0756508789062], [2, 40.47874316406249, 73.8141787109375, 571.3654147949218, 585.5528178710937], [2, 205.96536962890625, 224.4189143066406, 571.3654147949218, 585.5528178710937], [2, 248.82521533203123, 276.20789453124996, 571.3654147949218, 585.5528178710937], [2, 305.3764006347656, 332.75907983398434, 571.3654147949218, 585.5528178710937], [2, 369.6661691894531, 397.04884838867184, 571.3654147949218, 585.5528178710937], [2, 40.47874316406249, 114.88819750976562, 586.8425817871093, 601.0299848632812], [2, 205.96536962890625, 224.4189143066406, 586.8425817871093, 601.0299848632812], [2, 300.01891992187495, 332.75907983398434, 586.8425817871093, 601.0299848632812], [2, 40.47874316406249, 134.53229345703124, 601.0299848632812, 615.217387939453], [2, 205.96536962890625, 224.4189143066406, 601.0299848632812, 615.217387939453], [2, 242.872458984375, 276.20789453124996, 601.0299848632812, 615.217387939453], [2, 300.01891992187495, 332.75907983398434, 601.0299848632812, 615.217387939453], [2, 369.6661691894531, 397.04884838867184, 601.0299848632812, 615.217387939453], [2, 40.47874316406249, 61.908666015624995, 616.5071518554687, 630.6945549316406], [2, 192.27403002929685, 224.4189143066406, 616.5071518554687, 630.6945549316406], [2, 248.82521533203123, 276.20789453124996, 616.5071518554687, 630.6945549316406], [2, 305.3764006347656, 332.75907983398434, 616.5071518554687, 630.6945549316406], [2, 364.30868847656245, 397.04884838867184, 616.5071518554687, 630.6945549316406], [2, 40.47874316406249, 82.14803759765624, 630.6945549316406, 644.8819580078125], [2, 192.27403002929685, 224.4189143066406, 630.6945549316406, 644.8819580078125], [2, 248.82521533203123, 276.20789453124996, 630.6945549316406, 644.8819580078125], [2, 305.3764006347656, 332.75907983398434, 630.6945549316406, 644.8819580078125], [2, 369.6661691894531, 397.04884838867184, 630.6945549316406, 644.8819580078125], [2, 40.47874316406249, 82.14803759765624, 646.171721923828, 660.359125], [2, 192.27403002929685, 224.4189143066406, 646.171721923828, 660.359125], [2, 248.82521533203123, 276.20789453124996, 646.171721923828, 660.359125], [2, 305.3764006347656, 332.75907983398434, 646.171721923828, 660.359125], [2, 369.6661691894531, 397.04884838867184, 646.171721923828, 660.359125], [2, 40.47874316406249, 82.14803759765624, 660.359125, 674.5465280761719], [2, 192.27403002929685, 224.4189143066406, 660.359125, 674.5465280761719], [2, 248.82521533203123, 276.20789453124996, 660.359125, 674.5465280761719], [2, 305.3764006347656, 332.75907983398434, 660.359125, 674.5465280761719], [2, 369.6661691894531, 397.04884838867184, 660.359125, 674.5465280761719], [2, 40.47874316406249, 108.93544116210937, 674.5465280761719, 688.7339311523436], [2, 192.27403002929685, 224.4189143066406, 674.5465280761719, 688.7339311523436], [2, 248.82521533203123, 276.20789453124996, 674.5465280761719, 688.7339311523436], [2, 305.3764006347656, 332.75907983398434, 674.5465280761719, 688.7339311523436], [2, 369.6661691894531, 397.04884838867184, 674.5465280761719, 688.7339311523436], [2, 40.47874316406249, 61.908666015624995, 702.9213342285155, 717.1087373046875], [2, 178.5826904296875, 224.4189143066406, 702.9213342285155, 717.1087373046875], [2, 236.91970263671874, 276.20789453124996, 702.9213342285155, 717.1087373046875], [2, 40.47874316406249, 95.83937719726562, 718.3985012207031, 732.5859042968749], [2, 178.5826904296875, 224.4189143066406, 718.3985012207031, 732.5859042968749], [2, 236.91970263671874, 276.20789453124996, 718.3985012207031, 732.5859042968749], [2, 300.01891992187495, 332.75907983398434, 718.3985012207031, 732.5859042968749], [2, 369.6661691894531, 397.04884838867184, 718.3985012207031, 732.5859042968749], [2, 40.47874316406249, 77.38583251953125, 746.7733073730468, 760.9607104492187], [2, 205.96536962890625, 224.4189143066406, 746.7733073730468, 760.9607104492187], [2, 248.82521533203123, 276.20789453124996, 746.7733073730468, 760.9607104492187], [2, 305.3764006347656, 332.75907983398434, 746.7733073730468, 760.9607104492187], [2, 364.30868847656245, 397.04884838867184, 746.7733073730468, 760.9607104492187], [2, 40.47874316406249, 102.98268481445312, 762.2504743652344, 776.4378774414062], [2, 205.96536962890625, 224.4189143066406, 762.2504743652344, 776.4378774414062], [2, 242.872458984375, 276.20789453124996, 762.2504743652344, 776.4378774414062], [2, 300.01891992187495, 332.75907983398434, 762.2504743652344, 776.4378774414062], [2, 364.30868847656245, 397.04884838867184, 762.2504743652344, 776.4378774414062], [2, 40.47874316406249, 83.3385888671875, 777.7276413574218, 791.9150444335937], [2, 205.96536962890625, 224.4189143066406, 777.7276413574218, 791.9150444335937], [2, 248.82521533203123, 276.20789453124996, 777.7276413574218, 791.9150444335937], [2, 305.3764006347656, 332.75907983398434, 777.7276413574218, 791.9150444335937], [2, 364.30868847656245, 397.04884838867184, 777.7276413574218, 791.9150444335937], [2, 40.47874316406249, 83.3385888671875, 791.9150444335937, 806.1024475097655], [2, 205.96536962890625, 224.4189143066406, 791.9150444335937, 806.1024475097655], [2, 248.82521533203123, 276.20789453124996, 791.9150444335937, 806.1024475097655], [2, 305.3764006347656, 332.75907983398434, 791.9150444335937, 806.1024475097655], [2, 364.30868847656245, 397.04884838867184, 791.9150444335937, 806.1024475097655], [2, 40.47874316406249, 108.93544116210937, 807.3922114257812, 821.5796145019531], [2, 205.96536962890625, 224.4189143066406, 807.3922114257812, 821.5796145019531], [2, 242.872458984375, 276.20789453124996, 807.3922114257812, 821.5796145019531], [2, 300.01891992187495, 332.75907983398434, 807.3922114257812, 821.5796145019531], [2, 364.30868847656245, 397.04884838867184, 807.3922114257812, 821.5796145019531], [2, 40.47874316406249, 89.29134521484374, 821.5796145019531, 835.767017578125], [2, 132.74646655273438, 224.4189143066406, 821.5796145019531, 835.767017578125], [2, 248.82521533203123, 276.20789453124996, 821.5796145019531, 835.767017578125], [2, 305.3764006347656, 332.75907983398434, 821.5796145019531, 835.767017578125], [2, 364.30868847656245, 397.04884838867184, 821.5796145019531, 835.767017578125], [2, 36.90708935546875, 113.10237060546874, 887.35757421875, 906.7040329589843], [2, 32.74015991210937, 283.9464777832031, 914.4426164550781, 928.6300195312499], [2, 32.74015991210937, 226.20474121093747, 927.3402556152344, 941.5276586914061], [2, 32.74015991210937, 226.20474121093747, 927.3402556152344, 941.5276586914061]]
2026-08-10 10:48:49,880 INFO     29 [qwen-vl-text] ═══ DONE ═══ 125 positions, pages=1, time=40.4s
2026-08-10 10:48:49,895 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 10:48:49,895 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:48:49,895 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 10:48:49,896 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T10:48:49.896+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"71a9158694a811f1bd9827cf206dfa2d": {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 10:48:49,903 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:48:49,903 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 10:48:50,844 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 10:48:50,859 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 10:48:50,860 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "562 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-10 10:48:50,860 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 10:48:50,861 INFO     29 [ChunkMerger] Merged 12 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescription': 4, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2, 'Extractor:Progress': 1} (filtered 4 noise chunks)
2026-08-10 10:48:50,873 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 10:48:50,873 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "12 items, types={'LabReport': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3, 'PrescriptionRecord': 4, 'ExaminationReport': 2}", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf"}
2026-08-10 10:48:50,873 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 10:48:50,989 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786358663635, 'update_date': datetime.datetime(2026, 8, 10, 10, 44, 23), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 876917, 'status': '1'}
2026-08-10 10:48:51,312 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞  None  8.40  10^9/L  3.5--9.5  False    红细胞  None  4.94  10^12/L  3.8--5.1  False    血红蛋白  None  138  g/L  115--150  False    血小板  None  300  10^9/L  125--350  False    红细胞压积  None  41.30  %  35--45  False    红细胞平均体积  None  83.60  fL  82--100  False    平均血红蛋白量  None  28.00  pg  27--34  False    平均血红蛋白浓度  None  334  g/L  316--354  False    中性粒细胞比率  None  54.20  %  40--75  False    淋巴细胞比率  None  36.10  %  20--50  False    单核细胞比率  None  3.70  %  3--10  False    嗜酸性粒细胞比率  None  5.50  %  0.4--8.0  False    血小板  None  300  10^9/L  125--350  False    红细胞压积  None  41.30  %  35--45  False    红细胞平均体积  None  83.60  fL  82--100  False    平均血红蛋白量  None  28.00  pg  27--34  False    平均血红蛋白浓度  None  334  g/L  316--354  False    中性粒细胞比率  None  54.20  %  40--75  False    淋巴细胞比率  None  36.10  %  20--50  False    单核细胞比率  None  3.70  %  3--10  False    嗜酸性粒细胞比率  None  5.50  %  0.4--8.0  False    嗜碱性粒细胞比率  None  0.50  %  0--1  False    中性粒细胞数  None  4.56  10^9/L  1.8--6.3  False    淋巴细胞数  None  3.03  10^9/L  1.1--3.2  False    单核细胞数  None  0.31  10^9/L  0.10--0.60  False    嗜酸性粒细胞  None  0.46  10^9/L  0.02--0.52  False    嗜碱性粒细胞  None  0.04  10^9/L  0--0.06  False    红细胞分布宽度变异系数  None  12.9  %  11.0--16.0  False    血小板分布宽度  None  16.5  fL  8.0--18.1  False    平均血小板体积  None  10.2  fL  9--13  False    血小板压积  None  0.31  %  0.10--0.28  True    C反应蛋白  None  7.92  mg/L  0--6  True   
---
2/4
沈阳市第四人民医院
THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG
门诊病历
业：现住址：辽宁省沈阳市皇姑区延河街
就诊科别：呼吸与危重症医学科门诊
就诊时间：2024-08-23 16:00
书写时间：2024-08-23 16:59
供史者：患者本人
主诉：支气管哮喘开药
现病史：患者支气管哮喘，继续巩固治疗：
沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒
孟鲁司特钠片
10mg*5片，共10片
每次10mg，QD
睡前口服
查体/专科查体：
辅助检查：
诊断：
支气管哮喘
处理意见：
建议患者定期复查肺功能，肺部CT.
我科随诊。
建议休息天数：0天。
患者下转：
签名：杨昕
患者签名：
门诊病历专用章
---
辽宁崇文厚德医院
门诊病历
科室：呼吸内一科门诊
姓名：
职业：
就诊日期：2025/11/08 10:11:23
主诉：反复喘息2年，加重1周
现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万
林”治疗，症状稍有改善，为求进一步诊治来我院就诊。
既往史：否认。
过敏史：{无}
体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。
辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试
性。
抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.
初步诊断：1、支气管哮喘 急性发作期
处理：
1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。
2.1周后复诊，病情变化随诊。
医生签名：王春
王春
---
新药特药大药房总店
流水单号 10020045213
结账时间 2025-11-08 15:22:19
编号 数量 单价 金额 营业员
甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It
Sr1/库存2
0310145 2 盒 34.00 68.00
合计 68.00
优惠：0.00 微信：0.00
收银 1002
银台
会员
本次积分 0.00
累计积分 0.00
此票为开发票依据，药品为特殊、
商品，售出概不退还！
---
新药特药大药房总店
流水单号 10020044912
结账时间 2025-10-14 08:34:01
编号 数量 单价 金额 营业员
沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug
泡/葛兰素史克(集团)/库存1
0200127 1 盒 199.00 199.00
合计 199.00
优惠:0.00 微信:0.00
收银 1002
银台
会员
本次积分 0.00
累计积分 0.00
此票为开发票依据,药品为特殊、
商品,售出概不退还!
---
新药特药大药房总店
流水单号 10020046503
结账时间 2026-01-02 18:12:29
编号 数量 单价 金额 营业员
沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:
泡/葛兰素史克(集团)/库存1
0200127 1 盒 199.00 199.00
合计 199.00
优惠:0.00 微信:0.00
收银 1002
银台
会员
本次积分 0.00
累计积分 0.00
此票为开发票依据,药品为特殊、
商品,售出概不退还!
---
2/4
科 室:呼吸与危重症一门诊
诊断:(J45.900x001)支气管哮喘
Rp
沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙
【50ug:250ug/泡*60泡/(193.60元/盒)
1盒
用法用量:每次300ug,吸入,每天二次
孟鲁司特钠片【舒宁安】乙
超量说明:
【10mg*5片】
(4.96元/盒)
3盒
用法用量:每次10mg,睡前口服,每天一次
医师:杨沂发药:修泉涌配药:沈瑶
vivo X80 · ZEISS
计:208.48/208.48
第1页/共1页
---
1/1
NO:25004949727
4号窗口
25/11/03 16:39
普通
病志号:55161248
科
室:呼吸与危重症一门诊
诊断:(J45.900x001)支气管哮喘
Rp
沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙
【50ug:250ug/泡*60泡/(193.60元/盒)
1盒
用法用量:每次300ug,吸入,每天二次
医师:杨昕发药:沈瑶配药:巴艺洁
vivo X80 · ZEISS
金额合计:193.6/193.6
第1页/共1页
2025/11/05 14:51
---
沈阳市第四人民医院
处方笺
医疗类别:市医保
NO:25005558582
4号窗口
25/12/08 14:00
普通
病志号:55161248
诊断:(J45.900x001)支气管哮喘
Rp
沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙
【50ug:250ug/泡*60泡/(193.60元/盒)
1盒
用法用量:每次300ug,吸入,每天二次
vivo X80 · ZEISS
医师:杨昕发药:李琳配药:巴艺洁
2025/12/31 18:28金额合计:193.6/193.6
第1页/共1页
---
沈阳市第四人民医院
处方笺
医疗类别:市医保
NO:26000513029
3号窗口
26/01/30 13:26
普通
科 室:呼吸与危重症一门诊
诊断:(J45.900x001)支气管哮喘
Rp
沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙
【50ug:250ug/泡*60泡/(193.60元/盒)
1盒
用法用量:每次300ug,吸入,每天二次
医师:杨昕发药:李琳 配药:乔军
金额合计:193.6/193.6
第1页/共1页
---
中国医科大学沈阳市第四人民医院
报告单
出生日期：1983-6-17
性别：女
住院号：890730
年龄：42 Years
身高：163 cm
测试号：2025011002
体重：70 kg
预计 实1 %(实1/预) 实2 %(实2/预) 变异率
Time
14:07:
14:26:
FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6
FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9
FEV 1 % FVC [%] 69.69 74.33 6.7
FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7
PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5
MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4
MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 4.7 -6.2
MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0
MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1
Flow [L/s]
F/V ex
10
5
0
1
2
3
4
5
6
7
10
F/V in
医生意见：
阻塞型轻度通气功能障碍，小气道功能障碍。
支气管舒张试验：吸入沙丁胺醇气雾剂400微克，
FEV1增加360毫升，改善率为16.9%。支气管舒张试验阳性。
操作者：
---
中国医科大学沈阳市第四人民医院
肺功能报告单
姓名：
出生日期：
1983-6-17
住院号：
890730
身高：
163 cm
性别：
女
年龄：
42 Years
测试号：
2025011002
体重：
70 kg
Date
Time
预计
实测
%(实/预)
25-9-02
14:07:38
VT
[L]
0.50
BF
[1/min]
20.00
MV
[L/min]
10.00
ERV
[L]
1.07
VC MAX
[L]
3.31
3.36
101.6
FVC
[L]
3.24
3.05
94.1
FEV 1
[L]
2.79
2.12
76.1
FEV 1 % FVC
[%]
69.69
FEV 1 % VC MAX
[%]
81.12
63.16
77.9
PEF
[L/s]
6.59
6.83
103.5
MEF 75
[L/s]
5.80
3.41
58.8
MEF 50
[L/s]
4.10
2.30
56.2
MEF 25
[L/s]
1.77
0.45
25.4
MMEF 75/25
[L/s]
3.53
0.95
26.9
MVV
[L/min]
103.77
FEV 1*30
[L/min]
103.77
63.70
61.4
RV-SB
[L]
1.62
2.06
127.2
RV%TLC-SB
[%]
33.24
40.20
120.9
TLC-SB
[L]
4.97
5.13
103.3
FRC-SB
[L]
2.69
2.97
110.3
FRC%TLC-SB
[%]
51.82
57.88
111.7
DLCO SB
[mmol/min/kPa]
8.54
5.51
(64.6)
医生意见：
阻塞型轻度通气功能障碍，小气道功能障碍。
弥散功能降低。残总比 40.20 %。
2026-08-10 10:48:51,920 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 10:48:51,920 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "12 items, types={'LabReport': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3, 'PrescriptionRecord': 4, 'ExaminationReport': 2}", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "embedding_token_consumption": 4055}
2026-08-10 10:48:51,920 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 10:48:52,210 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 10:48:52,210 INFO     29 [Trace] task=71a91586 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":12,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 10:48:52,216 INFO     29 [DIAG-EXECUTOR] row_position_int len=32 row[0]=(4, 118, 167, 385, 403) row[-1]=(5, 117, 192, 817, 836)
2026-08-10 10:48:52,216 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,216 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,216 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,216 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,216 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,216 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,216 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,217 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,217 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,217 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,217 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 10:48:52,221 INFO     29 set_progress(71a9158694a811f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 10:48:52 [DOC Engine]:
Start to index...
2026-08-10 10:48:52,260 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.034s]
2026-08-10 10:48:52,264 INFO     29 set_progress(71a9158694a811f1bd9827cf206dfa2d), progress: 0.8083333333333333, progress_msg: 
2026-08-10 10:48:52,294 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.023s]
2026-08-10 10:48:52,322 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 10:48:52,337 INFO     29 set_progress(71a9158694a811f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 10:48:52 Indexing done (0.11s). Task done (260.85s)
2026-08-10 10:48:52,344 INFO     29 [Done], chunks(12), token(4055), elapsed:260.85
2026-08-10 10:48:52,496 INFO     29 handle_task done for task {"id": "71a9158694a811f1bd9827cf206dfa2d", "doc_id": "7168f13694a811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786358660757, "task_type": "dataflow", "root_trace_id": "1bdd578ee86a4968aad8dfcd30209269", "root_traceparent": "00-1bdd578ee86a4968aad8dfcd30209269-d5a3b5a27aab43e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
