# 基准结果：LGWE-艾特美哮喘-洛阳三.pdf

## 基本信息

- 文件：`LGWE-艾特美哮喘-洛阳三.pdf`
- 大小：1610.3 KB
- PDF 总页数：3
- doc_id：`02179af894bc11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:04:22  完成时间：2026-08-10T21:06:16  耗时：113.8s
- progress_msg：`13:06:12 Indexing done (0.02s). Task done (101.93s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 15e43432 | 1 | 1-1 | 郑州市第一人民医院门诊病历 科室：呼吸内科一门诊 就诊日期：2025-05-25 |
| 2 | 011bd696 | 1 | 2-2 | 郑州市第一人民医院 肺功能检查报告 舒张试验 姓名： 性别：男 年龄：61岁 身 |
| 3 | 2c69e1fa | 1 | 3-3 | 郑州市第一人民医院 肺功能检查报告 常规通气 姓名： 性别：男 年龄：61岁 身 |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：3
- 页码并集：`[1, 2, 3]`
- 覆盖页数：3 / 3；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "ExaminationReport": 2}`
- ChunkMerger：`{"found": true, "merged": 3, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:06:11,290 INFO     29 [ChunkMerger] Merged 3 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:04:25,208 INFO     29 handle_task begin for task {"id": "024fb09694bc11f1bd9827cf206dfa2d", "doc_id": "02179af894bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367063876, "task_type": "dataflow", "root_trace_id": "705d979565f34369b938d12c0fe850b1", "root_traceparent": "00-705d979565f34369b938d12c0fe850b1-1f6f65e8a05ccfc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:04:25,401 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 13:04:25,511 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:04:25,522 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:04:25,522 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:04:25,522 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:04:25,532 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:04:25,532 INFO     29 ============================================================
2026-08-10 13:04:25,532 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:04:25,532 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:04:25,532 INFO     29 ============================================================
2026-08-10 13:04:25,532 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:04:25,533 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:04:25,538 INFO     29 No torch found.
2026-08-10 13:04:26,100 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=3
2026-08-10 13:04:26,202 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=716317, prompt_len=764
2026-08-10 13:04:27,592 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:04:27,593 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:04:27,605 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=716317, prompt_len=401
2026-08-10 13:04:29,763 INFO     29 [qwen-vl-parser] text API response (len=343):
["郑州市第一人民医院门诊病历", "科室：呼吸内科一门诊", "就诊日期：2025-05-25", "初诊", "姓名：", "性别：男", "年龄：61岁", "ID：", "主 诉：咳嗽、胸闷3月", "现 病 史：3月前出现咳嗽、胸闷，来诊", "既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无", "药物过敏史。", "体格检查：神志清，双肺呼吸音粗，未闻及啰音；", "处 理：完善肺功能", "建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，", "请随时就诊", "诊 断：1.支气管哮喘；", "检查", "肺功能检查+支气管舒张实验", "医生：张朝杰", "打印日期：2025-05-25 12:03", "第 1 页，共 1 页"]
2026-08-10 13:04:29,764 INFO     29 [qwen-vl-parser] page=1 text: 22 lines (bbox 0-21)
2026-08-10 13:04:29,764 INFO     29 [qwen-vl-parser] page=1 text: 22 sections
2026-08-10 13:04:29,867 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=664058, prompt_len=764
2026-08-10 13:04:31,273 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:04:31,274 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:04:31,288 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=664058, prompt_len=401
2026-08-10 13:04:37,098 INFO     29 [qwen-vl-parser] text API response (len=924):
["郑州市第一人民医院", "肺功能检查报告", "舒张试验", "姓名：", "性别：男", "年龄：61岁", "身高：174 cm", "体重：85 kg", "科别：呼吸内科", "住院号：", "测试号：2025052513", "吸烟史：", "联系电话：", "测试日期 25-5-25", "测试时间 11:46:55", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "25-5-25", "25-5-25", "11:46:55", "11:57:14", "FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91", "FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81", "FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90", "PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68", "MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76", "MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19", "MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56", "MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "F/V In", "Vol [L]", "6", "5", "Vol%Vcmax", "100", "80", "60", "40", "20", "0", "0.0", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "Vcmax", "Time [s]", "测试结果：", "支气管舒张试验阳性。", "(请结合临床全面诊断)", "医生签字：毛锦涛", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 13:04:37,099 INFO     29 [qwen-vl-parser] page=2 text: 69 lines (bbox 22-90)
2026-08-10 13:04:37,099 INFO     29 [qwen-vl-parser] page=2 text: 69 sections
2026-08-10 13:04:37,215 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=785551, prompt_len=764
2026-08-10 13:04:39,390 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:04:39,390 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 13:04:39,397 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=785551, prompt_len=401
2026-08-10 13:04:45,380 INFO     29 [qwen-vl-parser] text API response (len=1100):
["郑州市第一人民医院", "肺功能检查报告", "常规通气", "姓名：", "性别：男", "年龄：61岁", "身高：174 cm", "科别：呼吸内科", "住院号：门诊", "测试号：2025052513", "体重：85 kg", "测试日期 25-5-25", "测试时间 11:46:55", "预计值 实测值 实/预", "IRV [L] 1.14", "ERV [L] 3.12", "IC [L] 0.61", "VT [L] 4.26 0.65 106.5", "VC IN [L] 4.26 3.01 70.7", "VC EX [L] 4.26 2.84 66.8", "BF [1/min] 20.00 17.72 88.6", "MV [L/min] 12.14 11.46 94.4", "VC MAX [L] 4.26 3.01 70.7", "FVC [L] 4.10 2.84 69.4", "FEV 1 [L] 3.22 2.51 78.0", "FEV 1 % FVC [%] 83.40 88.46 106.1", "FEV 1 % VC MAX [%] 76.23 83.54 109.6", "PEF [L/s] 8.21 6.40 77.9", "MEF 75 [L/s] 7.26 6.18 85.1", "MEF 50 [L/s] 4.35 3.04 69.9", "MEF 25 [L/s] 1.62 1.18 72.8", "MMEF 75/25 [L/s] . 3.45 2.26 65.4", "MVV [L/min] 119.91 77.46 64.6", "FEV 1*30 [L/min] 119.91 75.39 62.9", "Vol [L]", "TLC 6", "FRC pleth", "RV 2", "PredA0.0 0.2 0.4 0.6 0.8 1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "F/V in", "2", "Vol [L]", "1", "0", "1", "2", "Time [s]", "0 2 4 6 8 10 12", "测试结果：", "提示：", "1、轻度阻塞性肺通气功能障碍；", "2、肺储备功能下降。", "(请结合临床全面诊断)", "医生签字：毛锦涛", "报告日期：2025-5-27", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 13:04:45,381 INFO     29 [qwen-vl-parser] page=3 text: 68 lines (bbox 91-158)
2026-08-10 13:04:45,381 INFO     29 [qwen-vl-parser] page=3 text: 68 sections
2026-08-10 13:04:45,381 INFO     29 [qwen-vl-parser] parse_pdf done: 159 sections from 3 pages.
2026-08-10 13:04:45,402 INFO     29 Close text detector.
2026-08-10 13:04:45,831 INFO     29 Close text recognizer.
2026-08-10 13:04:46,245 INFO     29 Close recognizer.
2026-08-10 13:04:46,644 INFO     29 Close recognizer.
2026-08-10 13:04:47,089 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:04:46.644+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 38, "failed": 0, "current": {"024fb09694bc11f1bd9827cf206dfa2d": {"id": "024fb09694bc11f1bd9827cf206dfa2d", "doc_id": "02179af894bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367063876, "task_type": "dataflow", "root_trace_id": "705d979565f34369b938d12c0fe850b1", "root_traceparent": "00-705d979565f34369b938d12c0fe850b1-1f6f65e8a05ccfc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:04:47,100 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:04:47,101 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Parser:MedLink | outputs={"html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "json"}
2026-08-10 13:04:47,101 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:04:47,126 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:47,127 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 郑州市第一人民医院门诊病历\n[BBOX-1] 科室：呼吸内科一门诊\n[BBOX-2] 就诊日期：2025-05-25\n[BBOX-3] 初诊\n[BBOX-4] 姓名：\n[BBOX-5] 性别：男\n[BBOX-6] 年龄：61岁\n[BBOX-7] ID：\n[BBOX-8] 主 诉：咳嗽、胸闷3月\n[BBOX-9] 现 病 史：3月前出现咳嗽、胸闷，来诊\n[BBOX-10] 既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无\n[BBOX-11] 药物过敏史。\n[BBOX-12] 体格检查：神志清，双肺呼吸音粗，未闻及啰音；\n[BBOX-13] 处 理：完善肺功能\n[BBOX-14] 建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，\n[BBOX-15] 请随时就诊\n[BBOX-16] 诊 断：1.支气管哮喘；\n[BBOX-17] 检查\n[BBOX-18] 肺功能检查+支气管舒张实验\n[BBOX-19] 医生：张朝杰\n[BBOX-20] 打印日期：2025-05-25 12:03\n[BBOX-21] 第 1 页，共 1 页\n[BBOX-22] 郑州市第一人民医院\n[BBOX-23] 肺功能检查报告\n[BBOX-24] 舒张试验\n[BBOX-25] 姓名：\n[BBOX-26] 性别：男\n[BBOX-27] 年龄：61岁\n[BBOX-28] 身高：174 cm\n[BBOX-29] 体重：85 kg\n[BBOX-30] 科别：呼吸内科\n[BBOX-31] 住院号：\n[BBOX-32] 测试号：2025052513\n[BBOX-33] 吸烟史：\n[BBOX-34] 联系电话：\n[BBOX-35] 测试日期 25-5-25\n[BBOX-36] 测试时间 11:46:55\n[BBOX-37] 预计值\n[BBOX-38] 前次\n[BBOX-39] 前/预\n[BBOX-40] 后次\n[BBOX-41] 后/预\n[BBOX-42] 改善率\n[BBOX-43] 25-5-25\n[BBOX-44] 25-5-25\n[BBOX-45] 11:46:55\n[BBOX-46] 11:57:14\n[BBOX-47] FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91\n[BBOX-48] FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81\n[BBOX-49] FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90\n[BBOX-50] PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68\n[BBOX-51] MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76\n[BBOX-52] MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19\n[BBOX-53] MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56\n[BBOX-54] MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80\n[BBOX-55] Flow [L/s]\n[BBOX-56] F/V ex\n[BBOX-57] 10\n[BBOX-58] 5\n[BBOX-59] 0\n[BBOX-60] 1\n[BBOX-61] 2\n[BBOX-62] 3\n[BBOX-63] 4\n[BBOX-64] 5\n[BBOX-65] F/V In\n[BBOX-66] Vol [L]\n[BBOX-67] 6\n[BBOX-68] 5\n[BBOX-69] Vol%Vcmax\n[BBOX-70] 100\n[BBOX-71] 80\n[BBOX-72] 60\n[BBOX-73] 40\n[BBOX-74] 20\n[BBOX-75] 0\n[BBOX-76] 0.0\n[BBOX-77] 0.5\n[BBOX-78] 1.0\n[BBOX-79] 1.5\n[BBOX-80] 2.0\n[BBOX-81] 2.5\n[BBOX-82] 3.0\n[BBOX-83] Vcmax\n[BBOX-84] Time [s]\n[BBOX-85] 测试结果：\n[BBOX-86] 支气管舒张试验阳性。\n[BBOX-87] (请结合临床全面诊断)\n[BBOX-88] 医生签字：毛锦涛\n[BBOX-89] CS 扫描全能王\n[BBOX-90] 3亿人都在用的扫描App\n[BBOX-91] 郑州市第一人民医院\n[BBOX-92] 肺功能检查报告\n[BBOX-93] 常规通气\n[BBOX-94] 姓名：\n[BBOX-95] 性别：男\n[BBOX-96] 年龄：61岁\n[BBOX-97] 身高：174 cm\n[BBOX-98] 科别：呼吸内科\n[BBOX-99] 住院号：门诊\n[BBOX-100] 测试号：2025052513\n[BBOX-101] 体重：85 kg\n[BBOX-102] 测试日期 25-5-25\n[BBOX-103] 测试时间 11:46:55\n[BBOX-104] 预计值 实测值 实/预\n[BBOX-105] IRV [L] 1.14\n[BBOX-106] ERV [L] 3.12\n[BBOX-107] IC [L] 0.61\n[BBOX-108] VT [L] 4.26 0.65 106.5\n[BBOX-109] VC IN [L] 4.26 3.01 70.7\n[BBOX-110] VC EX [L] 4.26 2.84 66.8\n[BBOX-111] BF [1/min] 20.00 17.72 88.6\n[BBOX-112] MV [L/min] 12.14 11.46 94.4\n[BBOX-113] VC MAX [L] 4.26 3.01 70.7\n[BBOX-114] FVC [L] 4.10 2.84 69.4\n[BBOX-115] FEV 1 [L] 3.22 2.51 78.0\n[BBOX-116] FEV 1 % FVC [%] 83.40 88.46 106.1\n[BBOX-117] FEV 1 % VC MAX [%] 76.23 83.54 109.6\n[BBOX-118] PEF [L/s] 8.21 6.40 77.9\n[BBOX-119] MEF 75 [L/s] 7.26 6.18 85.1\n[BBOX-120] MEF 50 [L/s] 4.35 3.04 69.9\n[BBOX-121] MEF 25 [L/s] 1.62 1.18 72.8\n[BBOX-122] MMEF 75/25 [L/s] . 3.45 2.26 65.4\n[BBOX-123] MVV [L/min] 119.91 77.46 64.6\n[BBOX-124] FEV 1*30 [L/min] 119.91 75.39 62.9\n[BBOX-125] Vol [L]\n[BBOX-126] TLC 6\n[BBOX-127] FRC pleth\n[BBOX-128] RV 2\n[BBOX-129] PredA0.0 0.2 0.4 0.6 0.8 1.0\n[BBOX-130] Time [min]\n[BBOX-131] Flow [L/s]\n[BBOX-132] F/V ex\n[BBOX-133] 10\n[BBOX-134] 5\n[BBOX-135] 0\n[BBOX-136] 1\n[BBOX-137] 2\n[BBOX-138] 3\n[BBOX-139] 4\n[BBOX-140] 5\n[BBOX-141] F/V in\n[BBOX-142] 2\n[BBOX-143] Vol [L]\n[BBOX-144] 1\n[BBOX-145] 0\n[BBOX-146] 1\n[BBOX-147] 2\n[BBOX-148] Time [s]\n[BBOX-149] 0 2 4 6 8 10 12\n[BBOX-150] 测试结果：\n[BBOX-151] 提示：\n[BBOX-152] 1、轻度阻塞性肺通气功能障碍；\n[BBOX-153] 2、肺储备功能下降。\n[BBOX-154] (请结合临床全面诊断)\n[BBOX-155] 医生签字：毛锦涛\n[BBOX-156] 报告日期：2025-5-27\n[BBOX-157] CS 扫描全能王\n[BBOX-158] 3亿人都在用的扫描App"
  }
]
2026-08-10 13:04:50,993 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:51,007 INFO     29 [SmartSplitter] SmartSplitter done: 3 chunks from 3 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 2}
2026-08-10 13:04:51,016 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:04:51,016 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}"}
2026-08-10 13:04:51,016 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:04:51,016 INFO     29 [ChunkRouter] Routed 3 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 2}
2026-08-10 13:04:51,026 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:04:51,026 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | ChunkRouter:Router | outputs={"html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:04:51,026 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:04:51,031 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:51,031 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:04:51,594 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:51,598 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:04:51,598 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:04:51,599 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:04:51,603 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:51,604 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:04:52,024 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:52,033 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:04:52,033 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:04:52,033 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:04:52,040 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:04:52,041 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:04:52,041 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:04:52,041 INFO     29 [qwen-vl-text] positions(22): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:04:52,041 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [22]
2026-08-10 13:04:52,252 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:04:52,253 INFO     29 [qwen-vl-text] LLM extraction start, text_len=276
2026-08-10 13:04:52,253 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:52,253 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 21, \"encounter_dates\": [\"2025-05-25\"], \"department\": \"呼吸内科一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "郑州市第一人民医院门诊病历\n科室：呼吸内科一门诊\n就诊日期：2025-05-25\n初诊\n姓名：\n性别：男\n年龄：61岁\nID：\n主 诉：咳嗽、胸闷3月\n现 病 史：3月前出现咳嗽、胸闷，来诊\n既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无\n药物过敏史。\n体格检查：神志清，双肺呼吸音粗，未闻及啰音；\n处 理：完善肺功能\n建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，\n请随时就诊\n诊 断：1.支气管哮喘；\n检查\n肺功能检查+支气管舒张实验\n医生：张朝杰\n打印日期：2025-05-25 12:03\n第 1 页，共 1 页",
    "role": "user"
  }
]
2026-08-10 13:04:53,671 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:53,671 INFO     29 [qwen-vl-text] LLM output (len=225):
{
  "encounter_date": "2025-05-25",
  "chief_complaint": "咳嗽、胸闷3月",
  "present_illness": "3月前出现咳嗽、胸闷，来诊",
  "past_history": "无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无药物过敏史。",
  "diagnosis": "1.支气管哮喘；",
  "treatment_plan": "完善肺功能；门诊口服药物治疗"
}
2026-08-10 13:04:53,671 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-25]
2026-08-10 13:04:53,672 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=709343, prompt_len=955
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["郑州市第一人民医院门诊病历", "科室：呼吸内科一门诊", "就诊日期：2025-05-25", "初诊", "姓名：", "性别：男", "年龄：61岁", "ID：", "主 诉：咳嗽、胸闷3月", "现 病 史：3月前出现咳嗽、胸闷，来诊", "既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无", "药物过敏史。", "体格检查：神志清，双肺呼吸音粗，未闻及啰音；", "处 理：完善肺功能", "建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，", "请随时就诊", "诊 断：1.支气管哮喘；", "检查", "肺功能检查+支气管舒张实验", "医生：张朝杰", "打印日期：2025-05-25 12:03", "第 1 页，共 1 页"]

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
2026-08-10 13:05:00,785 INFO     29 [qwen-vl-text] coord API raw response (len=1239):
[
	{"text": "郑州市第一人民医院门诊病历", "bbox": [295, 31, 742, 63]},
	{"text": "科室：呼吸内科一门诊", "bbox": [166, 77, 381, 96]},
	{"text": "就诊日期：2025-05-25", "bbox": [523, 76, 734, 94]},
	{"text": "初诊", "bbox": [793, 77, 835, 94]},
	{"text": "姓名：", "bbox": [166, 108, 218, 126]},
	{"text": "性别：男", "bbox": [373, 108, 453, 125]},
	{"text": "年龄：61岁", "bbox": [495, 107, 600, 125]},
	{"text": "ID：", "bbox": [630, 108, 664, 124]},
	{"text": "主 诉：咳嗽、胸闷3月", "bbox": [173, 139, 416, 157]},
	{"text": "现 病 史：3月前出现咳嗽、胸闷，来诊", "bbox": [173, 177, 545, 195]},
	{"text": "既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无", "bbox": [173, 245, 837, 263]},
	{"text": "药物过敏史。", "bbox": [173, 264, 290, 281]},
	{"text": "体格检查：神志清，双肺呼吸音粗，未闻及啰音；", "bbox": [173, 303, 627, 321]},
	{"text": "处 理：完善肺功能", "bbox": [173, 406, 388, 423]},
	{"text": "建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，", "bbox": [173, 491, 817, 509]},
	{"text": "请随时就诊", "bbox": [173, 509, 279, 526]},
	{"text": "诊 断：1.支气管哮喘；", "bbox": [173, 597, 418, 615]},
	{"text": "检查", "bbox": [176, 672, 219, 689]},
	{"text": "肺功能检查+支气管舒张实验", "bbox": [173, 696, 442, 714]},
	{"text": "医生：张朝杰", "bbox": [178, 751, 360, 770]},
	{"text": "打印日期：2025-05-25 12:03", "bbox": [541, 753, 811, 769]},
	{"text": "第 1 页，共 1 页", "bbox": [434, 818, 588, 836]}
]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=7.1s
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市第一人民医院门诊病历, bbox=[295, 31, 742, 63]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[1]: text=科室：呼吸内科一门诊, bbox=[166, 77, 381, 96]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[2]: text=就诊日期：2025-05-25, bbox=[523, 76, 734, 94]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[3]: text=初诊, bbox=[793, 77, 835, 94]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[166, 108, 218, 126]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[373, 108, 453, 125]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：61岁, bbox=[495, 107, 600, 125]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[7]: text=ID：, bbox=[630, 108, 664, 124]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[8]: text=主 诉：咳嗽、胸闷3月, bbox=[173, 139, 416, 157]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[9]: text=现 病 史：3月前出现咳嗽、胸闷，来诊, bbox=[173, 177, 545, 195]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[10]: text=既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无, bbox=[173, 245, 837, 263]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[11]: text=药物过敏史。, bbox=[173, 264, 290, 281]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[12]: text=体格检查：神志清，双肺呼吸音粗，未闻及啰音；, bbox=[173, 303, 627, 321]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[13]: text=处 理：完善肺功能, bbox=[173, 406, 388, 423]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[14]: text=建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，, bbox=[173, 491, 817, 509]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[15]: text=请随时就诊, bbox=[173, 509, 279, 526]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[16]: text=诊 断：1.支气管哮喘；, bbox=[173, 597, 418, 615]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[17]: text=检查, bbox=[176, 672, 219, 689]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[18]: text=肺功能检查+支气管舒张实验, bbox=[173, 696, 442, 714]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[19]: text=医生：张朝杰, bbox=[178, 751, 360, 770]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[20]: text=打印日期：2025-05-25 12:03, bbox=[541, 753, 811, 769]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] coord item[21]: text=第 1 页，共 1 页, bbox=[434, 818, 588, 836]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] page=0 — 22/22 coords, api_time=7.1s
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] new_positions (22):
[[0, 175.525, 441.48999999999995, 26.102, 53.046], [0, 98.77, 226.695, 64.834, 80.832], [0, 311.185, 436.72999999999996, 63.992, 79.148], [0, 471.835, 496.825, 64.834, 79.148], [0, 98.77, 129.71, 90.93599999999999, 106.092], [0, 221.935, 269.53499999999997, 90.93599999999999, 105.25], [0, 294.525, 357.0, 90.094, 105.25], [0, 374.84999999999997, 395.08, 90.93599999999999, 104.408], [0, 102.935, 247.51999999999998, 117.038, 132.194], [0, 102.935, 324.275, 149.034, 164.19], [0, 102.935, 498.015, 206.29, 221.446], [0, 102.935, 172.54999999999998, 222.28799999999998, 236.602], [0, 102.935, 373.065, 255.126, 270.282], [0, 102.935, 230.85999999999999, 341.852, 356.166], [0, 102.935, 486.11499999999995, 413.42199999999997, 428.578], [0, 102.935, 166.005, 428.578, 442.892], [0, 102.935, 248.70999999999998, 502.674, 517.8299999999999], [0, 104.72, 130.305, 565.824, 580.138], [0, 102.935, 262.99, 586.0319999999999, 601.188], [0, 105.91, 214.2, 632.342, 648.34], [0, 321.895, 482.54499999999996, 634.026, 647.4979999999999], [0, 258.22999999999996, 349.85999999999996, 688.756, 703.9119999999999]]
2026-08-10 13:05:00,786 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=8.7s
2026-08-10 13:05:00,792 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:05:00,792 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:05:00,793 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:05:00,797 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:00,797 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:05:02,332 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:02,339 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:05:02,340 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:05:02,340 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:05:02,344 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:02,344 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:05:02,750 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:02,754 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:05:02,754 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:05:02,754 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:05:02,759 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:02,759 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:05:03,209 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:03,214 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:05:03,214 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:05:03,214 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:05:03,218 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:03,218 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:05:03,702 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:03,707 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:05:03,707 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:05:03,707 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:05:03,711 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:05:03,712 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:05:03,712 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:05:03,712 INFO     29 [qwen-vl-text] positions(69): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:05:03,712 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [69]
2026-08-10 13:05:03,837 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:05:03,837 INFO     29 [qwen-vl-text] LLM extraction start, text_len=716
2026-08-10 13:05:03,837 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:03,838 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 22, \"bbox_end\": 90, \"encounter_dates\": [\"2025-05-25\"], \"department\": \"呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "郑州市第一人民医院\n肺功能检查报告\n舒张试验\n姓名：\n性别：男\n年龄：61岁\n身高：174 cm\n体重：85 kg\n科别：呼吸内科\n住院号：\n测试号：2025052513\n吸烟史：\n联系电话：\n测试日期 25-5-25\n测试时间 11:46:55\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n25-5-25\n25-5-25\n11:46:55\n11:57:14\nFVC [L] 4.10 2.84 69.4 3.49 85.2 22.91\nFEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81\nFEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90\nPEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68\nMEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76\nMEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19\nMEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56\nMMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\nF/V In\nVol [L]\n6\n5\nVol%Vcmax\n100\n80\n60\n40\n20\n0\n0.0\n0.5\n1.0\n1.5\n2.0\n2.5\n3.0\nVcmax\nTime [s]\n测试结果：\n支气管舒张试验阳性。\n(请结合临床全面诊断)\n医生签字：毛锦涛\nCS 扫描全能王\n3亿人都在用的扫描App",
    "role": "user"
  }
]
2026-08-10 13:05:09,678 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:09,679 INFO     29 [qwen-vl-text] LLM output (len=925):
{
  "exam_date": "2025-05-25",
  "report_date": "2025-05-25",
  "exam_name": "肺功能检查报告 舒张试验",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸内科",
  "bed_number": null,
  "findings": "预计值\n前次\n前/预\n后次\n后/预\n改善率\n25-5-25\n25-5-25\n11:46:55\n11:57:14\nFVC [L] 4.10 2.84 69.4 3.49 85.2 22.91\nFEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81\nFEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90\nPEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68\nMEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76\nMEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19\nMEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56\nMMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\nF/V In\nVol [L]\n6\n5\nVol%Vcmax\n100\n80\n60\n40\n20\n0\n0.0\n0.5\n1.0\n1.5\n2.0\n2.5\n3.0\nVcmax\nTime [s]",
  "conclusion": "测试结果：\n支气管舒张试验阳性。\n(请结合临床全面诊断)",
  "physician": "毛锦涛",
  "reviewer": null
}
2026-08-10 13:05:09,681 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=650512, prompt_len=1536
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共69行）
["郑州市第一人民医院", "肺功能检查报告", "舒张试验", "姓名：", "性别：男", "年龄：61岁", "身高：174 cm", "体重：85 kg", "科别：呼吸内科", "住院号：", "测试号：2025052513", "吸烟史：", "联系电话：", "测试日期 25-5-25", "测试时间 11:46:55", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "25-5-25", "25-5-25", "11:46:55", "11:57:14", "FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91", "FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81", "FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90", "PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68", "MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76", "MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19", "MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56", "MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "F/V In", "Vol [L]", "6", "5", "Vol%Vcmax", "100", "80", "60", "40", "20", "0", "0.0", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "Vcmax", "Time [s]", "测试结果：", "支气管舒张试验阳性。", "(请结合临床全面诊断)", "医生签字：毛锦涛", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 13:05:30,554 INFO     29 [qwen-vl-text] coord API raw response (len=3735):
[
	{"text": "郑州市第一人民医院", "bbox": [382, 50, 634, 77]},
	{"text": "肺功能检查报告", "bbox": [410, 83, 603, 106]},
	{"text": "舒张试验", "bbox": [447, 114, 557, 138]},
	{"text": "姓名：", "bbox": [171, 165, 213, 177]},
	{"text": "性别：男", "bbox": [171, 176, 352, 188]},
	{"text": "年龄：61岁", "bbox": [171, 187, 380, 199]},
	{"text": "身高：174 cm", "bbox": [171, 199, 391, 210]},
	{"text": "体重：85 kg", "bbox": [171, 210, 380, 222]},
	{"text": "科别：呼吸内科", "bbox": [511, 157, 752, 171]},
	{"text": "住院号：", "bbox": [511, 170, 710, 183]},
	{"text": "测试号：2025052513", "bbox": [679, 182, 771, 195]},
	{"text": "吸烟史：", "bbox": [511, 195, 575, 207]},
	{"text": "联系电话：", "bbox": [511, 207, 593, 220]},
	{"text": "测试日期", "bbox": [108, 274, 184, 288]},
	{"text": "测试时间", "bbox": [108, 289, 184, 303]},
	{"text": "预计值", "bbox": [393, 253, 457, 268]},
	{"text": "前次", "bbox": [507, 253, 546, 268]},
	{"text": "前/预", "bbox": [587, 253, 638, 268]},
	{"text": "后次", "bbox": [690, 253, 730, 268]},
	{"text": "后/预", "bbox": [772, 253, 821, 268]},
	{"text": "改善率", "bbox": [851, 253, 910, 268]},
	{"text": "25-5-25", "bbox": [476, 268, 545, 281]},
	{"text": "25-5-25", "bbox": [659, 268, 730, 281]},
	{"text": "11:46:55", "bbox": [467, 283, 545, 296]},
	{"text": "11:57:14", "bbox": [650, 283, 730, 296]},
	{"text": "FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91", "bbox": [108, 317, 910, 331]},
	{"text": "FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81", "bbox": [108, 333, 910, 347]},
	{"text": "FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90", "bbox": [108, 348, 910, 362]},
	{"text": "PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68", "bbox": [108, 363, 910, 377]},
	{"text": "MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76", "bbox": [108, 378, 910, 392]},
	{"text": "MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19", "bbox": [108, 393, 910, 407]},
	{"text": "MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56", "bbox": [108, 408, 910, 422]},
	{"text": "MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80", "bbox": [108, 423, 910, 437]},
	{"text": "Flow [L/s]", "bbox": [181, 489, 230, 500]},
	{"text": "F/V ex", "bbox": [377, 487, 412, 497]},
	{"text": "10", "bbox": [163, 508, 176, 517]},
	{"text": "5", "bbox": [167, 537, 176, 546]},
	{"text": "0", "bbox": [165, 565, 174, 574]},
	{"text": "1", "bbox": [224, 575, 233, 584]},
	{"text": "2", "bbox": [279, 575, 288, 584]},
	{"text": "3", "bbox": [335, 575, 343, 584]},
	{"text": "4", "bbox": [389, 575, 398, 584]},
	{"text": "5", "bbox": [445, 575, 454, 584]},
	{"text": "F/V In", "bbox": [380, 640, 410, 650]},
	{"text": "Vol [L]", "bbox": [586, 490, 619, 501]},
	{"text": "6", "bbox": [570, 487, 579, 496]},
	{"text": "5", "bbox": [570, 511, 579, 520]},
	{"text": "Vol%Vcmax", "bbox": [537, 531, 600, 541]},
	{"text": "100", "bbox": [540, 542, 560, 551]},
	{"text": "80", "bbox": [546, 561, 559, 570]},
	{"text": "60", "bbox": [546, 580, 559, 589]},
	{"text": "40", "bbox": [546, 597, 559, 606]},
	{"text": "20", "bbox": [546, 615, 559, 624]},
	{"text": "0", "bbox": [551, 633, 560, 642]},
	{"text": "0.0", "bbox": [573, 644, 592, 653]},
	{"text": "0.5", "bbox": [624, 644, 643, 653]},
	{"text": "1.0", "bbox": [677, 644, 693, 653]},
	{"text": "1.5", "bbox": [725, 644, 742, 653]},
	{"text": "2.0", "bbox": [774, 644, 790, 653]},
	{"text": "2.5", "bbox": [821, 644, 838, 653]},
	{"text": "3.0", "bbox": [868, 644, 885, 653]},
	{"text": "Vcmax", "bbox": [598, 547, 635, 556]},
	{"text": "Time [s]", "bbox": [713, 624, 754, 634]},
	{"text": "测试结果：", "bbox": [105, 667, 197, 684]},
	{"text": "支气管舒张试验阳性。", "bbox": [128, 702, 300, 714]},
	{"text": "(请结合临床全面诊断)", "bbox": [132, 827, 345, 845]},
	{"text": "医生签字：毛锦涛", "bbox": [556, 829, 868, 868]},
	{"text": "CS 扫描全能王", "bbox": [862, 958, 976, 973]},
	{"text": "3亿人都在用的扫描App", "bbox": [862, 977, 976, 986]}
]
2026-08-10 13:05:30,555 INFO     29 [qwen-vl-text] coord API: raw_items=69, valid_items=69, elapsed=20.9s
2026-08-10 13:05:30,555 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市第一人民医院, bbox=[382, 50, 634, 77]
2026-08-10 13:05:30,555 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[410, 83, 603, 106]
2026-08-10 13:05:30,555 INFO     29 [qwen-vl-text] coord item[2]: text=舒张试验, bbox=[447, 114, 557, 138]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[171, 165, 213, 177]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[171, 176, 352, 188]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：61岁, bbox=[171, 187, 380, 199]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[6]: text=身高：174 cm, bbox=[171, 199, 391, 210]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[7]: text=体重：85 kg, bbox=[171, 210, 380, 222]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[8]: text=科别：呼吸内科, bbox=[511, 157, 752, 171]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[9]: text=住院号：, bbox=[511, 170, 710, 183]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[10]: text=测试号：2025052513, bbox=[679, 182, 771, 195]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[11]: text=吸烟史：, bbox=[511, 195, 575, 207]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[12]: text=联系电话：, bbox=[511, 207, 593, 220]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[13]: text=测试日期, bbox=[108, 274, 184, 288]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[14]: text=测试时间, bbox=[108, 289, 184, 303]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[15]: text=预计值, bbox=[393, 253, 457, 268]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[16]: text=前次, bbox=[507, 253, 546, 268]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[17]: text=前/预, bbox=[587, 253, 638, 268]
2026-08-10 13:05:30,556 INFO     29 [qwen-vl-text] coord item[18]: text=后次, bbox=[690, 253, 730, 268]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[19]: text=后/预, bbox=[772, 253, 821, 268]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[20]: text=改善率, bbox=[851, 253, 910, 268]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[21]: text=25-5-25, bbox=[476, 268, 545, 281]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[22]: text=25-5-25, bbox=[659, 268, 730, 281]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[23]: text=11:46:55, bbox=[467, 283, 545, 296]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[24]: text=11:57:14, bbox=[650, 283, 730, 296]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[25]: text=FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91, bbox=[108, 317, 910, 331]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[26]: text=FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81, bbox=[108, 333, 910, 347]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[27]: text=FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90, bbox=[108, 348, 910, 362]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[28]: text=PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68, bbox=[108, 363, 910, 377]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[29]: text=MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76, bbox=[108, 378, 910, 392]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[30]: text=MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19, bbox=[108, 393, 910, 407]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[31]: text=MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56, bbox=[108, 408, 910, 422]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[32]: text=MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80, bbox=[108, 423, 910, 437]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[33]: text=Flow [L/s], bbox=[181, 489, 230, 500]
2026-08-10 13:05:30,557 INFO     29 [qwen-vl-text] coord item[34]: text=F/V ex, bbox=[377, 487, 412, 497]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[35]: text=10, bbox=[163, 508, 176, 517]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[36]: text=5, bbox=[167, 537, 176, 546]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[37]: text=0, bbox=[165, 565, 174, 574]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[38]: text=1, bbox=[224, 575, 233, 584]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[39]: text=2, bbox=[279, 575, 288, 584]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[40]: text=3, bbox=[335, 575, 343, 584]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[41]: text=4, bbox=[389, 575, 398, 584]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[42]: text=5, bbox=[445, 575, 454, 584]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[43]: text=F/V In, bbox=[380, 640, 410, 650]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[44]: text=Vol [L], bbox=[586, 490, 619, 501]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[45]: text=6, bbox=[570, 487, 579, 496]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[46]: text=5, bbox=[570, 511, 579, 520]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[47]: text=Vol%Vcmax, bbox=[537, 531, 600, 541]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[48]: text=100, bbox=[540, 542, 560, 551]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[49]: text=80, bbox=[546, 561, 559, 570]
2026-08-10 13:05:30,558 INFO     29 [qwen-vl-text] coord item[50]: text=60, bbox=[546, 580, 559, 589]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[51]: text=40, bbox=[546, 597, 559, 606]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[52]: text=20, bbox=[546, 615, 559, 624]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[53]: text=0, bbox=[551, 633, 560, 642]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[54]: text=0.0, bbox=[573, 644, 592, 653]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[55]: text=0.5, bbox=[624, 644, 643, 653]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[56]: text=1.0, bbox=[677, 644, 693, 653]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[57]: text=1.5, bbox=[725, 644, 742, 653]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[58]: text=2.0, bbox=[774, 644, 790, 653]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[59]: text=2.5, bbox=[821, 644, 838, 653]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[60]: text=3.0, bbox=[868, 644, 885, 653]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[61]: text=Vcmax, bbox=[598, 547, 635, 556]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[62]: text=Time [s], bbox=[713, 624, 754, 634]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[63]: text=测试结果：, bbox=[105, 667, 197, 684]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[64]: text=支气管舒张试验阳性。, bbox=[128, 702, 300, 714]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[65]: text=(请结合临床全面诊断), bbox=[132, 827, 345, 845]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[66]: text=医生签字：毛锦涛, bbox=[556, 829, 868, 868]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[67]: text=CS 扫描全能王, bbox=[862, 958, 976, 973]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] coord item[68]: text=3亿人都在用的扫描App, bbox=[862, 977, 976, 986]
2026-08-10 13:05:30,559 INFO     29 [qwen-vl-text] page=1 — 69/69 coords, api_time=20.9s
2026-08-10 13:05:30,560 INFO     29 [qwen-vl-text] new_positions (69):
[[1, 227.29, 377.22999999999996, 42.1, 64.834], [1, 243.95, 358.78499999999997, 69.886, 89.252], [1, 265.965, 331.41499999999996, 95.988, 116.196], [1, 101.74499999999999, 126.735, 138.93, 149.034], [1, 101.74499999999999, 209.44, 148.192, 158.296], [1, 101.74499999999999, 226.1, 157.454, 167.558], [1, 101.74499999999999, 232.64499999999998, 167.558, 176.82], [1, 101.74499999999999, 226.1, 176.82, 186.924], [1, 304.04499999999996, 447.44, 132.194, 143.982], [1, 304.04499999999996, 422.45, 143.14, 154.08599999999998], [1, 404.005, 458.745, 153.244, 164.19], [1, 304.04499999999996, 342.125, 164.19, 174.29399999999998], [1, 304.04499999999996, 352.835, 174.29399999999998, 185.23999999999998], [1, 64.25999999999999, 109.47999999999999, 230.708, 242.49599999999998], [1, 64.25999999999999, 109.47999999999999, 243.338, 255.126], [1, 233.83499999999998, 271.91499999999996, 213.02599999999998, 225.656], [1, 301.66499999999996, 324.87, 213.02599999999998, 225.656], [1, 349.265, 379.60999999999996, 213.02599999999998, 225.656], [1, 410.54999999999995, 434.34999999999997, 213.02599999999998, 225.656], [1, 459.34, 488.495, 213.02599999999998, 225.656], [1, 506.34499999999997, 541.4499999999999, 213.02599999999998, 225.656], [1, 283.21999999999997, 324.275, 225.656, 236.602], [1, 392.10499999999996, 434.34999999999997, 225.656, 236.602], [1, 277.865, 324.275, 238.286, 249.232], [1, 386.75, 434.34999999999997, 238.286, 249.232], [1, 64.25999999999999, 541.4499999999999, 266.914, 278.702], [1, 64.25999999999999, 541.4499999999999, 280.38599999999997, 292.174], [1, 64.25999999999999, 541.4499999999999, 293.01599999999996, 304.804], [1, 64.25999999999999, 541.4499999999999, 305.646, 317.43399999999997], [1, 64.25999999999999, 541.4499999999999, 318.276, 330.06399999999996], [1, 64.25999999999999, 541.4499999999999, 330.906, 342.69399999999996], [1, 64.25999999999999, 541.4499999999999, 343.536, 355.324], [1, 64.25999999999999, 541.4499999999999, 356.166, 367.954], [1, 107.695, 136.85, 411.738, 421.0], [1, 224.315, 245.14, 410.054, 418.474], [1, 96.985, 104.72, 427.736, 435.31399999999996], [1, 99.365, 104.72, 452.154, 459.73199999999997], [1, 98.175, 103.53, 475.72999999999996, 483.308], [1, 133.28, 138.635, 484.15, 491.728], [1, 166.005, 171.35999999999999, 484.15, 491.728], [1, 199.325, 204.08499999999998, 484.15, 491.728], [1, 231.45499999999998, 236.81, 484.15, 491.728], [1, 264.775, 270.13, 484.15, 491.728], [1, 226.1, 243.95, 538.88, 547.3], [1, 348.66999999999996, 368.305, 412.58, 421.842], [1, 339.15, 344.505, 410.054, 417.632], [1, 339.15, 344.505, 430.262, 437.84], [1, 319.515, 357.0, 447.102, 455.522], [1, 321.3, 333.2, 456.364, 463.942], [1, 324.87, 332.60499999999996, 472.36199999999997, 479.94], [1, 324.87, 332.60499999999996, 488.35999999999996, 495.938], [1, 324.87, 332.60499999999996, 502.674, 510.252], [1, 324.87, 332.60499999999996, 517.8299999999999, 525.408], [1, 327.84499999999997, 333.2, 532.986, 540.564], [1, 340.935, 352.24, 542.2479999999999, 549.826], [1, 371.28, 382.585, 542.2479999999999, 549.826], [1, 402.815, 412.335, 542.2479999999999, 549.826], [1, 431.375, 441.48999999999995, 542.2479999999999, 549.826], [1, 460.53, 470.04999999999995, 542.2479999999999, 549.826], [1, 488.495, 498.60999999999996, 542.2479999999999, 549.826], [1, 516.4599999999999, 526.5749999999999, 542.2479999999999, 549.826], [1, 355.81, 377.825, 460.574, 468.152], [1, 424.23499999999996, 448.63, 525.408, 533.828], [1, 62.474999999999994, 117.21499999999999, 561.614, 575.928], [1, 76.16, 178.5, 591.084, 601.188], [1, 78.53999999999999, 205.27499999999998, 696.334, 711.49], [1, 330.82, 516.4599999999999, 698.018, 730.856], [1, 512.89, 580.72, 806.636, 819.266], [1, 512.89, 580.72, 822.634, 830.212]]
2026-08-10 13:05:30,560 INFO     29 [qwen-vl-text] ═══ DONE ═══ 69 positions, pages=1, time=26.8s
2026-08-10 13:05:30,560 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:05:30,569 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:05:30,569 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:05:30,569 INFO     29 [qwen-vl-text] positions(68): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:05:30,569 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [68]
2026-08-10 13:05:30,783 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:05:30,784 INFO     29 [qwen-vl-text] LLM extraction start, text_len=895
2026-08-10 13:05:30,784 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:30,785 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 91, \"bbox_end\": 158, \"encounter_dates\": [\"2025-05-25\"], \"department\": \"呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "郑州市第一人民医院\n肺功能检查报告\n常规通气\n姓名：\n性别：男\n年龄：61岁\n身高：174 cm\n科别：呼吸内科\n住院号：门诊\n测试号：2025052513\n体重：85 kg\n测试日期 25-5-25\n测试时间 11:46:55\n预计值 实测值 实/预\nIRV [L] 1.14\nERV [L] 3.12\nIC [L] 0.61\nVT [L] 4.26 0.65 106.5\nVC IN [L] 4.26 3.01 70.7\nVC EX [L] 4.26 2.84 66.8\nBF [1/min] 20.00 17.72 88.6\nMV [L/min] 12.14 11.46 94.4\nVC MAX [L] 4.26 3.01 70.7\nFVC [L] 4.10 2.84 69.4\nFEV 1 [L] 3.22 2.51 78.0\nFEV 1 % FVC [%] 83.40 88.46 106.1\nFEV 1 % VC MAX [%] 76.23 83.54 109.6\nPEF [L/s] 8.21 6.40 77.9\nMEF 75 [L/s] 7.26 6.18 85.1\nMEF 50 [L/s] 4.35 3.04 69.9\nMEF 25 [L/s] 1.62 1.18 72.8\nMMEF 75/25 [L/s] . 3.45 2.26 65.4\nMVV [L/min] 119.91 77.46 64.6\nFEV 1*30 [L/min] 119.91 75.39 62.9\nVol [L]\nTLC 6\nFRC pleth\nRV 2\nPredA0.0 0.2 0.4 0.6 0.8 1.0\nTime [min]\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\nF/V in\n2\nVol [L]\n1\n0\n1\n2\nTime [s]\n0 2 4 6 8 10 12\n测试结果：\n提示：\n1、轻度阻塞性肺通气功能障碍；\n2、肺储备功能下降。\n(请结合临床全面诊断)\n医生签字：毛锦涛\n报告日期：2025-5-27\nCS 扫描全能王\n3亿人都在用的扫描App",
    "role": "user"
  }
]
2026-08-10 13:05:30,788 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:05:30.787+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 38, "failed": 0, "current": {"024fb09694bc11f1bd9827cf206dfa2d": {"id": "024fb09694bc11f1bd9827cf206dfa2d", "doc_id": "02179af894bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367063876, "task_type": "dataflow", "root_trace_id": "705d979565f34369b938d12c0fe850b1", "root_traceparent": "00-705d979565f34369b938d12c0fe850b1-1f6f65e8a05ccfc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:05:37,541 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:05:37,541 INFO     29 [qwen-vl-text] LLM output (len=1097):
{
  "exam_date": "2025-05-25",
  "report_date": "2025-05-27",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸内科",
  "bed_number": null,
  "findings": "常规通气\n预计值 实测值 实/预\nIRV [L] 1.14\nERV [L] 3.12\nIC [L] 0.61\nVT [L] 4.26 0.65 106.5\nVC IN [L] 4.26 3.01 70.7\nVC EX [L] 4.26 2.84 66.8\nBF [1/min] 20.00 17.72 88.6\nMV [L/min] 12.14 11.46 94.4\nVC MAX [L] 4.26 3.01 70.7\nFVC [L] 4.10 2.84 69.4\nFEV 1 [L] 3.22 2.51 78.0\nFEV 1 % FVC [%] 83.40 88.46 106.1\nFEV 1 % VC MAX [%] 76.23 83.54 109.6\nPEF [L/s] 8.21 6.40 77.9\nMEF 75 [L/s] 7.26 6.18 85.1\nMEF 50 [L/s] 4.35 3.04 69.9\nMEF 25 [L/s] 1.62 1.18 72.8\nMMEF 75/25 [L/s] . 3.45 2.26 65.4\nMVV [L/min] 119.91 77.46 64.6\nFEV 1*30 [L/min] 119.91 75.39 62.9\nVol [L]\nTLC 6\nFRC pleth\nRV 2\nPredA0.0 0.2 0.4 0.6 0.8 1.0\nTime [min]\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\nF/V in\n2\nVol [L]\n1\n0\n1\n2\nTime [s]\n0 2 4 6 8 10 12",
  "conclusion": "测试结果：\n提示：\n1、轻度阻塞性肺通气功能障碍；\n2、肺储备功能下降。\n(请结合临床全面诊断)",
  "physician": "毛锦涛",
  "reviewer": null
}
2026-08-10 13:05:37,542 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=756233, prompt_len=1712
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共68行）
["郑州市第一人民医院", "肺功能检查报告", "常规通气", "姓名：", "性别：男", "年龄：61岁", "身高：174 cm", "科别：呼吸内科", "住院号：门诊", "测试号：2025052513", "体重：85 kg", "测试日期 25-5-25", "测试时间 11:46:55", "预计值 实测值 实/预", "IRV [L] 1.14", "ERV [L] 3.12", "IC [L] 0.61", "VT [L] 4.26 0.65 106.5", "VC IN [L] 4.26 3.01 70.7", "VC EX [L] 4.26 2.84 66.8", "BF [1/min] 20.00 17.72 88.6", "MV [L/min] 12.14 11.46 94.4", "VC MAX [L] 4.26 3.01 70.7", "FVC [L] 4.10 2.84 69.4", "FEV 1 [L] 3.22 2.51 78.0", "FEV 1 % FVC [%] 83.40 88.46 106.1", "FEV 1 % VC MAX [%] 76.23 83.54 109.6", "PEF [L/s] 8.21 6.40 77.9", "MEF 75 [L/s] 7.26 6.18 85.1", "MEF 50 [L/s] 4.35 3.04 69.9", "MEF 25 [L/s] 1.62 1.18 72.8", "MMEF 75/25 [L/s] . 3.45 2.26 65.4", "MVV [L/min] 119.91 77.46 64.6", "FEV 1*30 [L/min] 119.91 75.39 62.9", "Vol [L]", "TLC 6", "FRC pleth", "RV 2", "PredA0.0 0.2 0.4 0.6 0.8 1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "F/V in", "2", "Vol [L]", "1", "0", "1", "2", "Time [s]", "0 2 4 6 8 10 12", "测试结果：", "提示：", "1、轻度阻塞性肺通气功能障碍；", "2、肺储备功能下降。", "(请结合临床全面诊断)", "医生签字：毛锦涛", "报告日期：2025-5-27", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 13:06:10,337 INFO     29 [qwen-vl-text] coord API raw response (len=6006):
[
	{"text": "郑州市第一人民医院", "bbox": [390, 28, 660, 48]},
	{"text": "肺功能检查报告", "bbox": [416, 55, 622, 75]},
	{"text": "常规通气", "bbox": [463, 79, 580, 101]},
	{"text": "姓名：", "bbox": [137, 112, 187, 125]},
	{"text": "性别：", "bbox": [137, 125, 187, 137]},
	{"text": "年龄：", "bbox": [137, 137, 187, 149]},
	{"text": "身高：", "bbox": [137, 149, 187, 161]},
	{"text": "男", "bbox": [335, 127, 354, 138]},
	{"text": "61岁", "bbox": [335, 138, 384, 149]},
	{"text": "174 cm", "bbox": [335, 150, 396, 161]},
	{"text": "科别：", "bbox": [529, 114, 575, 126]},
	{"text": "住院号：", "bbox": [529, 126, 593, 138]},
	{"text": "测试号：", "bbox": [529, 138, 593, 150]},
	{"text": "体重：", "bbox": [529, 150, 575, 162]},
	{"text": "呼吸内科", "bbox": [714, 114, 796, 126]},
	{"text": "门诊", "bbox": [714, 126, 755, 138]},
	{"text": "2025052513", "bbox": [714, 138, 816, 149]},
	{"text": "85 kg", "bbox": [714, 150, 766, 162]},
	{"text": "测试日期", "bbox": [77, 201, 161, 214], "bbox": [77, 201, 161, 214]},
	{"text": "测试时间", "bbox": [77, 214, 161, 226], "bbox": [77, 214, 161, 226]},
	{"text": "25-5-25", "bbox": [490, 202, 558, 214], "bbox": [490, 202, 558, 214]},
	{"text": "11:46:55", "bbox": [470, 214, 558, 226], "bbox": [470, 214, 558, 226]},
	{"text": "预计值 实测值 实/预", "bbox": [396, 187, 665, 200], "bbox": [396, 187, 665, 200]},
	{"text": "IRV [L] 1.14", "bbox": [77, 243, 458, 256], "bbox": [77, 243, 458, 256]},
	{"text": "ERV [L] 3.12", "bbox": [77, 256, 458, 269], "bbox": [77, 256, 458, 269]},
	{"text": "IC [L] 0.61", "bbox": [77, 269, 458, 282], "bbox": [77, 269, 458, 282]},
	{"text": "VT [L] 4.26 0.65 106.5", "bbox": [77, 282, 665, 295], "bbox": [77, 282, 665, 295]},
	{"text": "VC IN [L] 4.26 3.01 70.7", "bbox": [77, 295, 665, 308], "bbox": [77, 295, 665, 308]},
	{"text": "VC EX [L] 4.26 2.84 66.8", "bbox": [77, 308, 665, 321], "bbox": [77, 308, 665, 321]},
	{"text": "BF [1/min] 20.00 17.72 88.6", "bbox": [77, 321, 665, 334], "bbox": [77, 321, 665, 334]},
	{"text": "MV [L/min] 12.14 11.46 94.4", "bbox": [77, 334, 665, 347], "bbox": [77, 334, 665, 347]},
	{"text": "VC MAX [L] 4.26 3.01 70.7", "bbox": [77, 347, 665, 360], "bbox": [77, 347, 665, 360]},
	{"text": "FVC [L] 4.10 2.84 69.4", "bbox": [77, 369, 665, 382], "bbox": [77, 369, 665, 382]},
	{"text": "FEV 1 [L] 3.22 2.51 78.0", "bbox": [77, 382, 665, 395], "bbox": [77, 382, 665, 395]},
	{"text": "FEV 1 % FVC [%] 83.40 88.46 106.1", "bbox": [77, 395, 665, 408], "bbox": [77, 395, 665, 408]},
	{"text": "FEV 1 % VC MAX [%] 76.23 83.54 109.6", "bbox": [77, 408, 665, 421], "bbox": [77, 408, 665, 421]},
	{"text": "PEF [L/s] 8.21 6.40 77.9", "bbox": [77, 421, 665, 434], "bbox": [77, 421, 665, 434]},
	{"text": "MEF 75 [L/s] 7.26 6.18 85.1", "bbox": [77, 434, 665, 447], "bbox": [77, 434, 665, 447]},
	{"text": "MEF 50 [L/s] 4.35 3.04 69.9", "bbox": [77, 447, 665, 460], "bbox": [77, 447, 665, 460]},
	{"text": "MEF 25 [L/s] 1.62 1.18 72.8", "bbox": [77, 460, 665, 473], "bbox": [77, 460, 665, 473]},
	{"text": "MMEF 75/25 [L/s] . 3.45 2.26 65.4", "bbox": [77, 473, 665, 486], "bbox": [77, 473, 665, 486]},
	{"text": "MVV [L/min] 119.91 77.46 64.6", "bbox": [77, 498, 665, 511], "bbox": [77, 498, 665, 511]},
	{"text": "FEV 1*30 [L/min] 119.91 75.39 62.9", "bbox": [77, 511, 665, 524], "bbox": [77, 511, 665, 524]},
	{"text": "Vol [L]", "bbox": [723, 194, 762, 205], "bbox": [723, 194, 762, 205]},
	{"text": "TLC 6", "bbox": [678, 203, 717, 214], "bbox": [678, 203, 717, 214]},
	{"text": "FRC pleth", "bbox": [678, 255, 728, 266], "bbox": [678, 255, 728, 266]},
	{"text": "RV 2", "bbox": [678, 272, 717, 283], "bbox": [678, 272, 717, 283]},
	{"text": "PredA0.0 0.2 0.4 0.6 0.8 1.0", "bbox": [678, 313, 960, 324], "bbox": [678, 313, 960, 324]},
	{"text": "Time [min]", "bbox": [809, 295, 868, 305], "bbox": [809, 295, 868, 305]},
	{"text": "Flow [L/s]", "bbox": [708, 332, 764, 343], "bbox": [708, 332, 764, 343]},
	{"text": "F/V ex", "bbox": [853, 332, 888, 342], "bbox": [853, 332, 888, 342]},
	{"text": "10", "bbox": [687, 344, 702, 354], "bbox": [687, 344, 702, 354]},
	{"text": "5", "bbox": [693, 365, 702, 375], "bbox": [693, 365, 702, 375]},
	{"text": "0", "bbox": [693, 387, 702, 397], "bbox": [693, 387, 702, 397]},
	{"text": "1", "bbox": [744, 397, 753, 405], "bbox": [744, 397, 753, 405]},
	{"text": "2", "bbox": [785, 397, 794, 405], "bbox": [785, 397, 794, 405]},
	{"text": "3", "bbox": [826, 397, 835, 405], "bbox": [826, 397, 835, 405]},
	{"text": "4", "bbox": [867, 397, 875, 405], "bbox": [867, 397, 875, 405]},
	{"text": "5", "bbox": [907, 397, 915, 405], "bbox": [907, 397, 915, 405]},
	{"text": "F/V in", "bbox": [853, 440, 884, 450], "bbox": [853, 440, 884, 450]},
	{"text": "2", "bbox": [693, 471, 702, 481], "bbox": [693, 471, 702, 481]},
	{"text": "Vol [L]", "bbox": [708, 467, 745, 477], "bbox": [708, 467, 745, 477]},
	{"text": "1", "bbox": [693, 494, 702, 504], "bbox": [693, 494, 702, 504]},
	{"text": "0", "bbox": [693, 516, 702, 526], "bbox": [693, 516, 702, 526]},
	{"text": "1", "bbox": [693, 540, 702, 550], "bbox": [693, 540, 702, 550]},
	{"text": "2", "bbox": [693, 563, 702, 573], "bbox": [693, 563, 702, 573]},
	{"text": "Time [s]", "bbox": [809, 567, 854, 578], "bbox": [809, 567, 854, 578]},
	{"text": "0 2 4 6 8 10 12", "bbox": [705, 585, 940, 596], "bbox": [705, 585, 940, 596]},
	{"text": "测试结果：", "bbox": [66, 603, 170, 620], "bbox": [66, 603, 170, 620]},
	{"text": "提示：", "bbox": [79, 645, 134, 662], "bbox": [79, 645, 134, 662]},
	{"text": "1、轻度阻塞性肺通气功能障碍；", "bbox": [79, 662, 418, 678], "bbox": [79, 662, 418, 678]},
	{"text": "2、肺储备功能下降。", "bbox": [79, 678, 296, 694], "bbox": [79, 678, 296, 694]},
	{"text": "(请结合临床全面诊断)", "bbox": [112, 761, 405, 780], "bbox": [112, 761, 405, 780]},
	{"text": "医生签字：毛锦涛", "bbox": [552, 765, 914, 807], "bbox": [552, 765, 914, 807]},
	{"text": "报告日期：2025-5-27", "bbox": [654, 829, 896, 845], "bbox": [654, 829, 896, 845]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 976, 973], "bbox": [861, 958, 976, 973]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 978, 976, 987], "bbox": [861, 978, 976, 987]}
]
2026-08-10 13:06:10,338 INFO     29 [qwen-vl-text] coord API: raw_items=77, valid_items=77, elapsed=32.8s
2026-08-10 13:06:10,338 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市第一人民医院, bbox=[390, 28, 660, 48]
2026-08-10 13:06:10,338 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[416, 55, 622, 75]
2026-08-10 13:06:10,338 INFO     29 [qwen-vl-text] coord item[2]: text=常规通气, bbox=[463, 79, 580, 101]
2026-08-10 13:06:10,338 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[137, 112, 187, 125]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[4]: text=性别：, bbox=[137, 125, 187, 137]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：, bbox=[137, 137, 187, 149]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[6]: text=身高：, bbox=[137, 149, 187, 161]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[7]: text=男, bbox=[335, 127, 354, 138]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[8]: text=61岁, bbox=[335, 138, 384, 149]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[9]: text=174 cm, bbox=[335, 150, 396, 161]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[10]: text=科别：, bbox=[529, 114, 575, 126]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[11]: text=住院号：, bbox=[529, 126, 593, 138]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[12]: text=测试号：, bbox=[529, 138, 593, 150]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[13]: text=体重：, bbox=[529, 150, 575, 162]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[14]: text=呼吸内科, bbox=[714, 114, 796, 126]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[15]: text=门诊, bbox=[714, 126, 755, 138]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[16]: text=2025052513, bbox=[714, 138, 816, 149]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[17]: text=85 kg, bbox=[714, 150, 766, 162]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[18]: text=测试日期, bbox=[77, 201, 161, 214]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[19]: text=测试时间, bbox=[77, 214, 161, 226]
2026-08-10 13:06:10,339 INFO     29 [qwen-vl-text] coord item[20]: text=25-5-25, bbox=[490, 202, 558, 214]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[21]: text=11:46:55, bbox=[470, 214, 558, 226]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[22]: text=预计值 实测值 实/预, bbox=[396, 187, 665, 200]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[23]: text=IRV [L] 1.14, bbox=[77, 243, 458, 256]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[24]: text=ERV [L] 3.12, bbox=[77, 256, 458, 269]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[25]: text=IC [L] 0.61, bbox=[77, 269, 458, 282]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[26]: text=VT [L] 4.26 0.65 106.5, bbox=[77, 282, 665, 295]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[27]: text=VC IN [L] 4.26 3.01 70.7, bbox=[77, 295, 665, 308]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[28]: text=VC EX [L] 4.26 2.84 66.8, bbox=[77, 308, 665, 321]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[29]: text=BF [1/min] 20.00 17.72 88.6, bbox=[77, 321, 665, 334]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[30]: text=MV [L/min] 12.14 11.46 94.4, bbox=[77, 334, 665, 347]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[31]: text=VC MAX [L] 4.26 3.01 70.7, bbox=[77, 347, 665, 360]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[32]: text=FVC [L] 4.10 2.84 69.4, bbox=[77, 369, 665, 382]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[33]: text=FEV 1 [L] 3.22 2.51 78.0, bbox=[77, 382, 665, 395]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[34]: text=FEV 1 % FVC [%] 83.40 88.46 106.1, bbox=[77, 395, 665, 408]
2026-08-10 13:06:10,340 INFO     29 [qwen-vl-text] coord item[35]: text=FEV 1 % VC MAX [%] 76.23 83.54 109.6, bbox=[77, 408, 665, 421]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[36]: text=PEF [L/s] 8.21 6.40 77.9, bbox=[77, 421, 665, 434]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[37]: text=MEF 75 [L/s] 7.26 6.18 85.1, bbox=[77, 434, 665, 447]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[38]: text=MEF 50 [L/s] 4.35 3.04 69.9, bbox=[77, 447, 665, 460]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[39]: text=MEF 25 [L/s] 1.62 1.18 72.8, bbox=[77, 460, 665, 473]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[40]: text=MMEF 75/25 [L/s] . 3.45 2.26 65.4, bbox=[77, 473, 665, 486]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[41]: text=MVV [L/min] 119.91 77.46 64.6, bbox=[77, 498, 665, 511]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[42]: text=FEV 1*30 [L/min] 119.91 75.39 62.9, bbox=[77, 511, 665, 524]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[43]: text=Vol [L], bbox=[723, 194, 762, 205]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[44]: text=TLC 6, bbox=[678, 203, 717, 214]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[45]: text=FRC pleth, bbox=[678, 255, 728, 266]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[46]: text=RV 2, bbox=[678, 272, 717, 283]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[47]: text=PredA0.0 0.2 0.4 0.6 0.8 1.0, bbox=[678, 313, 960, 324]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[48]: text=Time [min], bbox=[809, 295, 868, 305]
2026-08-10 13:06:10,341 INFO     29 [qwen-vl-text] coord item[49]: text=Flow [L/s], bbox=[708, 332, 764, 343]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[50]: text=F/V ex, bbox=[853, 332, 888, 342]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[51]: text=10, bbox=[687, 344, 702, 354]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[52]: text=5, bbox=[693, 365, 702, 375]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[53]: text=0, bbox=[693, 387, 702, 397]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[54]: text=1, bbox=[744, 397, 753, 405]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[55]: text=2, bbox=[785, 397, 794, 405]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[56]: text=3, bbox=[826, 397, 835, 405]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[57]: text=4, bbox=[867, 397, 875, 405]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[58]: text=5, bbox=[907, 397, 915, 405]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[59]: text=F/V in, bbox=[853, 440, 884, 450]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[60]: text=2, bbox=[693, 471, 702, 481]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[61]: text=Vol [L], bbox=[708, 467, 745, 477]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[62]: text=1, bbox=[693, 494, 702, 504]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[63]: text=0, bbox=[693, 516, 702, 526]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[64]: text=1, bbox=[693, 540, 702, 550]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[65]: text=2, bbox=[693, 563, 702, 573]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[66]: text=Time [s], bbox=[809, 567, 854, 578]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[67]: text=0 2 4 6 8 10 12, bbox=[705, 585, 940, 596]
2026-08-10 13:06:10,342 INFO     29 [qwen-vl-text] coord item[68]: text=测试结果：, bbox=[66, 603, 170, 620]
2026-08-10 13:06:10,343 INFO     29 [qwen-vl-text] coord item[69]: text=提示：, bbox=[79, 645, 134, 662]
2026-08-10 13:06:10,343 INFO     29 [qwen-vl-text] coord item[70]: text=1、轻度阻塞性肺通气功能障碍；, bbox=[79, 662, 418, 678]
2026-08-10 13:06:10,343 INFO     29 [qwen-vl-text] coord item[71]: text=2、肺储备功能下降。, bbox=[79, 678, 296, 694]
2026-08-10 13:06:10,343 INFO     29 [qwen-vl-text] coord item[72]: text=(请结合临床全面诊断), bbox=[112, 761, 405, 780]
2026-08-10 13:06:10,343 INFO     29 [qwen-vl-text] coord item[73]: text=医生签字：毛锦涛, bbox=[552, 765, 914, 807]
2026-08-10 13:06:10,343 INFO     29 [qwen-vl-text] coord item[74]: text=报告日期：2025-5-27, bbox=[654, 829, 896, 845]
2026-08-10 13:06:10,343 INFO     29 [qwen-vl-text] coord item[75]: text=CS 扫描全能王, bbox=[861, 958, 976, 973]
2026-08-10 13:06:10,343 INFO     29 [qwen-vl-text] coord item[76]: text=3亿人都在用的扫描App, bbox=[861, 978, 976, 987]
2026-08-10 13:06:10,344 INFO     29 [qwen-vl-text] page=2 — 68/68 coords, api_time=32.8s
2026-08-10 13:06:10,344 INFO     29 [qwen-vl-text] new_positions (68):
[[2, 232.04999999999998, 392.7, 23.576, 40.416], [2, 247.51999999999998, 370.09, 46.309999999999995, 63.15], [2, 275.485, 345.09999999999997, 66.518, 85.042], [2, 81.515, 111.265, 94.304, 105.25], [2, 81.515, 111.265, 105.25, 115.354], [2, 81.515, 111.265, 115.354, 125.458], [2, 81.515, 111.265, 125.458, 135.56199999999998], [2, 199.325, 210.63, 106.934, 116.196], [2, 199.325, 228.48, 116.196, 125.458], [2, 199.325, 235.61999999999998, 126.3, 135.56199999999998], [2, 314.755, 342.125, 95.988, 106.092], [2, 314.755, 352.835, 106.092, 116.196], [2, 314.755, 352.835, 116.196, 126.3], [2, 314.755, 342.125, 126.3, 136.404], [2, 424.83, 473.62, 95.988, 106.092], [2, 424.83, 449.22499999999997, 106.092, 116.196], [2, 424.83, 485.52, 116.196, 125.458], [2, 424.83, 455.77, 126.3, 136.404], [2, 45.815, 95.795, 169.242, 180.188], [2, 45.815, 95.795, 180.188, 190.292], [2, 291.55, 332.01, 170.084, 180.188], [2, 279.65, 332.01, 180.188, 190.292], [2, 235.61999999999998, 395.67499999999995, 157.454, 168.4], [2, 45.815, 272.51, 204.606, 215.552], [2, 45.815, 272.51, 215.552, 226.498], [2, 45.815, 272.51, 226.498, 237.444], [2, 45.815, 395.67499999999995, 237.444, 248.39], [2, 45.815, 395.67499999999995, 248.39, 259.336], [2, 45.815, 395.67499999999995, 259.336, 270.282], [2, 45.815, 395.67499999999995, 270.282, 281.228], [2, 45.815, 395.67499999999995, 281.228, 292.174], [2, 45.815, 395.67499999999995, 292.174, 303.12], [2, 45.815, 395.67499999999995, 310.698, 321.644], [2, 45.815, 395.67499999999995, 321.644, 332.59], [2, 45.815, 395.67499999999995, 332.59, 343.536], [2, 45.815, 395.67499999999995, 343.536, 354.48199999999997], [2, 45.815, 395.67499999999995, 354.48199999999997, 365.428], [2, 45.815, 395.67499999999995, 365.428, 376.37399999999997], [2, 45.815, 395.67499999999995, 376.37399999999997, 387.32], [2, 45.815, 395.67499999999995, 387.32, 398.26599999999996], [2, 45.815, 395.67499999999995, 398.26599999999996, 409.212], [2, 45.815, 395.67499999999995, 419.316, 430.262], [2, 45.815, 395.67499999999995, 430.262, 441.20799999999997], [2, 430.185, 453.39, 163.34799999999998, 172.60999999999999], [2, 403.40999999999997, 426.615, 170.926, 180.188], [2, 403.40999999999997, 433.15999999999997, 214.70999999999998, 223.97199999999998], [2, 403.40999999999997, 426.615, 229.024, 238.286], [2, 403.40999999999997, 571.1999999999999, 263.546, 272.808], [2, 481.35499999999996, 516.4599999999999, 248.39, 256.81], [2, 421.26, 454.58, 279.544, 288.806], [2, 507.53499999999997, 528.36, 279.544, 287.964], [2, 408.765, 417.69, 289.64799999999997, 298.068], [2, 412.335, 417.69, 307.33, 315.75], [2, 412.335, 417.69, 325.854, 334.274], [2, 442.68, 448.03499999999997, 334.274, 341.01], [2, 467.075, 472.43, 334.274, 341.01], [2, 491.46999999999997, 496.825, 334.274, 341.01], [2, 515.865, 520.625, 334.274, 341.01], [2, 539.665, 544.425, 334.274, 341.01], [2, 507.53499999999997, 525.98, 370.47999999999996, 378.9], [2, 412.335, 417.69, 396.582, 405.002], [2, 421.26, 443.275, 393.214, 401.63399999999996], [2, 412.335, 417.69, 415.948, 424.368], [2, 412.335, 417.69, 434.472, 442.892], [2, 412.335, 417.69, 454.68, 463.09999999999997], [2, 412.335, 417.69, 474.046, 482.466], [2, 481.35499999999996, 508.13, 477.414, 486.676], [2, 419.47499999999997, 559.3, 492.57, 501.832]]
2026-08-10 13:06:10,344 INFO     29 [qwen-vl-text] ═══ DONE ═══ 68 positions, pages=1, time=39.8s
2026-08-10 13:06:10,360 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:06:10,360 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:06:10,360 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:06:10,361 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:06:10.360+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 38, "failed": 0, "current": {"024fb09694bc11f1bd9827cf206dfa2d": {"id": "024fb09694bc11f1bd9827cf206dfa2d", "doc_id": "02179af894bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367063876, "task_type": "dataflow", "root_trace_id": "705d979565f34369b938d12c0fe850b1", "root_traceparent": "00-705d979565f34369b938d12c0fe850b1-1f6f65e8a05ccfc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:06:10,366 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:10,366 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:06:11,281 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:11,289 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:06:11,289 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "159 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 13:06:11,289 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:06:11,290 INFO     29 [ChunkMerger] Merged 3 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:06:11,300 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:06:11,300 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "name": "LGWE-艾特美哮喘-洛阳三.pdf"}
2026-08-10 13:06:11,300 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:06:11,333 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786367065395, 'update_date': datetime.datetime(2026, 8, 10, 13, 4, 25), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1022372, 'status': '1'}
2026-08-10 13:06:12,365 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=郑州市第一人民医院门诊病历
科室：呼吸内科一门诊
就诊日期：2025-05-25
初诊
姓名：
性别：男
年龄：61岁
ID：
主 诉：咳嗽、胸闷3月
现 病 史：3月前出现咳嗽、胸闷，来诊
既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无
药物过敏史。
体格检查：神志清，双肺呼吸音粗，未闻及啰音；
处 理：完善肺功能
建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，
请随时就诊
诊 断：1.支气管哮喘；
检查
肺功能检查+支气管舒张实验
医生：张朝杰
打印日期：2025-05-25 12:03
第 1 页，共 1 页
---
郑州市第一人民医院
肺功能检查报告
舒张试验
姓名：
性别：男
年龄：61岁
身高：174 cm
体重：85 kg
科别：呼吸内科
住院号：
测试号：2025052513
吸烟史：
联系电话：
测试日期 25-5-25
测试时间 11:46:55
预计值
前次
前/预
后次
后/预
改善率
25-5-25
25-5-25
11:46:55
11:57:14
FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91
FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81
FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90
PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68
MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76
MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19
MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56
MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80
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
F/V In
Vol [L]
6
5
Vol%Vcmax
100
80
60
40
20
0
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Vcmax
Time [s]
测试结果：
支气管舒张试验阳性。
(请结合临床全面诊断)
医生签字：毛锦涛
CS 扫描全能王
3亿人都在用的扫描App
---
郑州市第一人民医院
肺功能检查报告
常规通气
姓名：
性别：男
年龄：61岁
身高：174 cm
科别：呼吸内科
住院号：门诊
测试号：2025052513
体重：85 kg
测试日期 25-5-25
测试时间 11:46:55
预计值 实测值 实/预
IRV [L] 1.14
ERV [L] 3.12
IC [L] 0.61
VT [L] 4.26 0.65 106.5
VC IN [L] 4.26 3.01 70.7
VC EX [L] 4.26 2.84 66.8
BF [1/min] 20.00 17.72 88.6
MV [L/min] 12.14 11.46 94.4
VC MAX [L] 4.26 3.01 70.7
FVC [L] 4.10 2.84 69.4
FEV 1 [L] 3.22 2.51 78.0
FEV 1 % FVC [%] 83.40 88.46 106.1
FEV 1 % VC MAX [%] 76.23 83.54 109.6
PEF [L/s] 8.21 6.40 77.9
MEF 75 [L/s] 7.26 6.18 85.1
MEF 50 [L/s] 4.35 3.04 69.9
MEF 25 [L/s] 1.62 1.18 72.8
MMEF 75/25 [L/s] . 3.45 2.26 65.4
MVV [L/min] 119.91 77.46 64.6
FEV 1*30 [L/min] 119.91 75.39 62.9
Vol [L]
TLC 6
FRC pleth
RV 2
PredA0.0 0.2 0.4 0.6 0.8 1.0
Time [min]
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
F/V in
2
Vol [L]
1
0
1
2
Time [s]
0 2 4 6 8 10 12
测试结果：
提示：
1、轻度阻塞性肺通气功能障碍；
2、肺储备功能下降。
(请结合临床全面诊断)
医生签字：毛锦涛
报告日期：2025-5-27
CS 扫描全能王
3亿人都在用的扫描App
2026-08-10 13:06:12,758 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:06:12,758 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "embedding_token_consumption": 1559}
2026-08-10 13:06:12,758 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:06:12,860 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:06:12,860 INFO     29 [Trace] task=024fb096 | doc=LGWE-艾特美哮喘-洛阳三.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":3,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:06:12,863 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:06:12,864 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:06:12,864 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:06:12,868 INFO     29 set_progress(024fb09694bc11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:06:12 [DOC Engine]:
Start to index...
2026-08-10 13:06:12,879 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 13:06:12,883 INFO     29 set_progress(024fb09694bc11f1bd9827cf206dfa2d), progress: 0.8333333333333334, progress_msg: 
2026-08-10 13:06:12,890 INFO     29 set_progress(024fb09694bc11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:06:12 Indexing done (0.02s). Task done (101.93s)
2026-08-10 13:06:12,894 INFO     29 [Done], chunks(3), token(1559), elapsed:101.93
2026-08-10 13:06:12,953 INFO     29 handle_task done for task {"id": "024fb09694bc11f1bd9827cf206dfa2d", "doc_id": "02179af894bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786367063876, "task_type": "dataflow", "root_trace_id": "705d979565f34369b938d12c0fe850b1", "root_traceparent": "00-705d979565f34369b938d12c0fe850b1-1f6f65e8a05ccfc1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
