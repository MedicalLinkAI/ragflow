# 基准结果：12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf

## 基本信息

- 文件：`12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf`
- 大小：37500.0 KB
- PDF 总页数：18
- doc_id：`37bdfdce94ed11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T02:56:38  完成时间：2026-08-11T03:08:22  耗时：704.2s
- progress_msg：`19:08:19 Indexing done (0.07s). Task done (647.70s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 834f131a | 5 | 1-5 | 姓名 现住址 性别：女 职业：农民 年龄：60岁 入院时间：2024年01月17 |
| 2 | e6e90eeb | 1 | 5-5 | 出院记录 入院日期：2024年1月17日10点52分 性别：女 出院日期：202 |
| 3 | e514c8d0 | 1 | 6-6 | 门诊病历 初诊 复诊 门诊号 就诊 姓名 性别：女 年龄：60岁 身份 职业：农 |
| 4 | 6e01708f | 1 | 7-7 | 门诊病历 性别：女 年龄：61岁 民族：汉族 婚姻：已婚 职业：农民 证件类型： |
| 5 | 2444a750 | 1 | 8-8 | 门诊病历 性别：女 证件类型：居民身份证 年龄：62岁 证件 民族：汉族 门诊编 |
| 6 | e1a7fb96 | 1 | 9-9 | 门诊病历 性别：女 年龄：63岁 民族：汉族 婚姻：已婚 职业：农民 证件类型： |
| 7 | 1ab76b90 | 1 | 10-10 | 病理检查报告单 检查号 住院号 姓名 性别:女 结论: (右肺上叶)形态符合腺癌 |
| 8 | f061de99 | 1 | 11-11 | 病理检查报告单 检查号 住院号 门诊号: 姓名 性别:女 年龄:57岁 结合20 |
| 9 | 83687355 | 2 | 12-13 | 分子病理基因检测报告单 样本信息 项目编号：PCR20-1135 姓名 性别：女 |
| 10 | 8eab2a95 | 1 | 14-14 | 本报告仅供临床浏览，严禁私自打印。报告单以放射科室打印 放射科CT报告单 姓名  |
| 11 | 5f983120 | 1 | 15-15 | <table><tr><td>白细胞</td><td>WBC</td><td>8 |
| 12 | 96da4fa0 | 1 | 16-16 | <table><tr><td>丙氨酸氨基转移酶</td><td>ALT</td> |
| 13 | 931e1790 | 1 | 17-17 | <table><tr><td>甲胎蛋白</td><td>AFP</td><td> |

- chunks 总数：13
- 各 chunk 页数合计（含跨页重复）：18
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]`
- 覆盖页数：17 / 18；缺失页：`[18]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 17/18 页，缺失 [18]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 4 | 0 | 4 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 4 | 4 | 4 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 3 | 0 | 3 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "DischargeRecord": 1, "OutpatientRecord": 4, "ExaminationReport": 4, "LabReport": 3}`
- ChunkMerger：`{"found": true, "merged": 13, "sources": 9, "stats": {"Extractor:LabExam": 3, "Extractor:Imaging": 1, "Extractor:Clinical": 4, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 4, "Extractor:Progress": 1}, "filtered_noise": 4}`
- Extractor skip 证据：2 条
  - `[no_text_noise] 2026-08-10 19:02:27,585 INFO     29 [ChunkMerger] Merged 23 chunks from 9 sources: {'Extractor:LabExam': 13, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Pres`
  - `[no_text_noise] 2026-08-10 19:08:17,611 INFO     29 [ChunkMerger] Merged 13 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 18:56:42,405 INFO     29 handle_task begin for task {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 18:56:42,643 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 18:56:42,767 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 18:56:42,797 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:56:42,797 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 18:56:42,797 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 18:56:42,816 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 18:56:42,816 INFO     29 ============================================================
2026-08-10 18:56:42,816 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 18:56:42,816 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 18:56:42,816 INFO     29 ============================================================
2026-08-10 18:56:42,816 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 18:56:42,816 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 18:56:42,819 INFO     29 No torch found.
2026-08-10 18:56:44,724 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=18
2026-08-10 18:56:45,036 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3381245, prompt_len=764
2026-08-10 18:56:45,524 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:56:45.523+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:56:48,125 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:56:48,126 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 18:56:48,139 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3381245, prompt_len=401
2026-08-10 18:56:56,641 INFO     29 [qwen-vl-parser] text API response (len=1501):
["姓名", "现住址", "性别：女", "职业：农民", "年龄：60岁", "入院时间：2024年01月17日10点52分", "民族：汉族", "记录时间：2024年01月17日16点00分", "婚姻：已婚", "病史陈述者", "陈述者与患者关系：本人", "陈述者内容可靠标志：可靠", "主诉：肺腺癌5周期化疗后2年进展后化疗5周期后。", "现病史：患者2020.8月体检时行胸部CT检查提示右肺上叶片状影，无咳嗽、咳痰、", "咯血、痰中带血及胸痛、发热、盗汗等不适，遂就诊于当地医院给予“左氧氟沙星、", "法罗培南”等药物抗感染治疗，复查胸部CT提示吸收欠佳。患者为求进一步诊治就诊", "于我院，行胸部CT检查考虑右肺上叶浸润性肺腺Ca，在排除相关禁忌并取得患者家属", "知情同意后，行经皮肺穿刺活检，病理结果示：（右肺上叶）穿刺肺组织呈显著慢性", "炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变", "炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1(+)，CK7(+)，Ki-67阳性", "率10%。为排查肿瘤全身转移情况行骨ECT及腹部强化CT检查未见明显转移征象，行颅", "脑MRI提示右颞枕叶、左侧小脑下蚓部异常信号，结合肿瘤病史，建议增强扫描除外", "转移，为排除颅脑转移，进一步行颅脑强化MRI提示右侧颞枕叶脑沟内条片状轻度强", "化，考虑软脑膜增厚强化，结合肺Ca病史，脑膜转移不除外，建议脑脊液检查。脑脊", "液检查未见肿瘤细胞。在取得外科会诊意见明确患者具有手术指征后，患者于2020-0", "8-31于胸外科行右肺上叶切除并肺部、纵膈淋巴结清扫术，术后病理示：（右肺上叶", "）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，", "肿物切面面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；", "肺组织内查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚", "查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔", "淋巴结4枚，其中2枚查见转移癌（2/4）。另送第7组淋巴结9枚（0/9）、第9组淋巴结", "1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。术后行EGFR等十基因检测", "（石蜡包埋组织）示EFGR基因 Exon-20（外显子） 20-ins突变阳性。后患者为行", "进一步治疗就诊我科，告知患者其Exon-20突变不适合靶向药物治疗，建议行化疗治", "疗，在排除相关禁忌并取得患者及家属知情同意后，于2020-10-16、2020-11-10、", "2020-12-04、2020-12-26、2021-1-18行“培美曲塞二钠0.8g d1+卡铂400mg d1", "”方案化疗5周期，患者耐受可。2023.9.21、2023.10.13、2023.11.8、2023.12", ".4、2023.12.26排除禁忌给予卡铂+培美曲塞二钠联合贝伐珠单抗治疗5周期，耐受", "可。2023.11.07复查CT示：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19", "CT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂", "肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水", "；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著", "第1页"]
2026-08-10 18:56:56,642 INFO     29 [qwen-vl-parser] page=1 text: 43 lines (bbox 0-42)
2026-08-10 18:56:56,642 INFO     29 [qwen-vl-parser] page=1 text: 43 sections
2026-08-10 18:56:56,892 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3763585, prompt_len=764
2026-08-10 18:56:57,861 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:56:57,861 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 18:56:57,872 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3763585, prompt_len=401
2026-08-10 18:56:57,951 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:56:57,951 INFO     29 [qwen-vl-text] LLM output (len=3552):
{
  "encounter_date": "2026-02-02",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 57,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "农民",
  "dm_admission_time": "2026-02-02 14:26",
  "dm_record_time": "2026-02-02 15:08",
  "dm_history_provider": "患者及患者家属",
  "cc_text": "确诊肺恶性肿瘤2年余，再治疗。",
  "cc_main_symptoms": [
    "确诊肺恶性肿瘤",
    "再治疗"
  ],
  "cc_duration": "2年余",
  "pi_text": "患者于2年余前（2023.06）患者无明显诱因出现间断咳嗽、咳白色痰，伴有胸闷、纳差、乏力症状，活动后胸闷症状加重，于我院门诊行胸部CT示：两肺多发异常密度病变，较2023-03-15老片病变范围增大，结合2021-09-07片和2023-03-15片，注意警惕肺粘膜相关性淋巴瘤或肺炎型肺癌并两肺转移的可能性，建议支气管镜活检病理学检查，给予支气管肺泡灌洗（2024.06.15）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组织细胞，另见少许异型细胞，呈腺样结构，不除外腺癌，请结合临床及影像学。后至郑州大学第一附属医院确诊为肺腺癌（未见报告），具体不详，给予靶向治疗初始为阿美替尼，后调整为伏美替尼（不详）；复查CT（2024.11.12）：1、肺癌治疗后改变，对比2024-08-20片病变较前范围增大；2、左肺上叶下舌段及下叶后底段局限性支气管扩张；3、两肺多发微、小结节，较前右肺中叶结节稍增大，余相仿；4、右肺中叶少许慢性炎症；5、左侧第6肋骨顺位欠佳；6、提示左侧肾上腺结节，建议动态观察；请结合临床、病史及其它相关检查。2024.11.16调整为贝福替尼靶向治疗，2024.12.12于郑州大学第一附属医院复查CT：1.左肺多发团片影；2.双肺炎症，较前减轻；3.双肺多发结节，较前部分增大；4.双侧胸膜局限性增厚；5.左侧肾上腺内侧支结节，较前变化不大。给予抗感染及对症支持治疗后好转出院。2025.5.7复查CT：、肺癌治疗后改变，对比2025-01-11片病变较前增大；2、双肺局限性支气管扩张；3、左肺下叶空腔病灶，较前增大；4、两肺多发微、小结节，建议动态观察；5、双肺炎性病变；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，对比较前相仿；请结合临床、病史及其它相关检查。综合评估患者病情进展，与患者及家属沟通后，排除禁忌症后，2025.5.15，2025.6.14给予AP方案化疗2周期，过程顺利。基因检测（2025.7.12）：BRAF突变、EGFR突变、MSS型。后给予曲美替尼联合达拉替尼靶向治疗，期间因病情缓慢进展，加用阿美替尼靶向治疗：复查CT（2025.12.20）：1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-03片较前相仿：2、双肺局限性支气管扩张；3、双肺小空泡病灶，较前壁增厚；4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；5、双肺炎性病变，较前相仿；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，考虑转移，较前大致相仿；8、肝囊肿；请结合临床、病史及其它相关检查。排除禁忌症后，2026.1.14给予AC+AK112方案治疗1周期，过程顺利。近两日患者诉纳差乏力，伴胸闷、气短，伴咳嗽咳痰，现患者为进一步治疗入院，门诊以“肺恶性肿瘤”收入院。患病来，神志清，精神差，饮食量少，睡眠可，大便可，小便可，近期体重未监测。",
  "pmh_disease_history": [
    "慢性乙型病毒性肝炎病史30年"
  ],
  "pmh_allergy_history": [
    "无"
  ],
  "pmh_surgery_trauma_history": [
    "否认手术史",
    "否认外伤史"
  ],
  "ph_smoking": "否认吸烟史",
  "ph_drinking": "否认嗜酒史",
  "oh_menarche_age": 13,
  "oh_menopause_age": 52,
  "oh_pregnancies": "妊娠3次，生产3次，无流产、早产、手术产、死产，无节育、绝育。育有3个子女，均顺产。",
  "fh_text": "父亲体健，母亲已故，死因不详，1弟2妹身体健康。无类似患者疾病、传染性疾病、遗传性疾病。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.1,
  "vs_pulse_bpm": 108,
  "vs_respiration_rpm": 21,
  "vs_systolic_bp_mmhg": 89,
  "vs_diastolic_bp_mmhg": 63,
  "pe_general_condition": "发育正常，营养中等，神志清晰，精神差，体位主动，面容正常，表情安静，步态正常，检查合作。",
  "pe_skin_mucosa": "色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。",
  "pe_lymph_nodes": "浅表淋巴结无无肿大。",
  "pe_lungs": "呼吸运动正常，呼吸节律正常，语颤正常，未触及胸膜摩擦感，双肺叩诊呈清音，呼吸规整，双肺呼吸音减弱，可闻及湿性啰音，语音传导正常，未及明显胸膜摩擦音。",
  "pe_heart": "胸廓基本对称，心前区无隆起，心尖搏动正常，位于第五肋间左侧锁骨中线0.5cm，强度及范围正常，无负性心尖搏动。心尖搏动正常，无震颤，无心包摩擦音。心脏相对浊音界正常。心率108次/分，心律齐，心音无额外心音，无杂音无心包摩擦音。",
  "pe_abdomen": "腹部平坦，胃肠蠕动波无，腹式呼吸存在，未见腹壁静脉曲张。腹柔软，液波震颤无，振水声无，腹部包块未触及，无压痛、无反跳痛，脾肝未触及，Murphy's征阴性，肾无压痛，叩击痛，腹部血管搏动未见明显异常。输尿管压痛点无明显压痛。肝浊音界存在，肝上界位于右锁骨中线肋间，移动性浊音无。无明显肾区叩击痛，肠鸣音正常。",
  "pe_extremities": "脊柱正常，四肢无畸形，四肢关节活动及动脉搏动未见明显异常。",
  "pe_nervous_system": "生理反射存在，病理反射未引出。",
  "pe_specialist_exam": "神志清，精神差，全身浅表淋巴结未触及肿大，双肺呼吸音减弱，可闻及湿性啰音，心率108次/分，心律齐，各瓣膜听诊区未闻及杂音，腹软，未触及肿块，肝脾肋下未触及，双下肢无水肿。",
  "pe_ecog_score": null,
  "pat_text": "支气管肺泡灌洗（2024.06.15 我院）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组织细胞，另见少许异型细胞，呈腺样结构，不除外腺癌，请结合临床及影像学。",
  "pat_items": [
    "支气管肺泡灌洗（2024.06.15 我院）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组织细胞，另见少许异型细胞，呈腺样结构，不除外腺癌，请结合临床及影像学。"
  ],
  "preliminary_diagnoses": [
    {
      "name": "恶性肿瘤支持治疗",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "左肺恶性肿瘤 cTxNxM1 IV期",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "肺部感染",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": "肿瘤内科病区"
}
2026-08-10 18:56:57,951 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-02]
2026-08-10 18:56:57,955 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2777257, prompt_len=1932
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共47行）
["原阳县人民医院", "入院记录", "姓名：", "科室：肿瘤内科病区 床号：13床 住院号：023", "科室：肿瘤内科病区 第（9）次住院", "药物过敏史：无", "姓名：", "性别：女", "年龄：57岁", "入院时间：2026-02-02 14:26", "职业：农民", "民族：汉族", "婚姻：已婚", "记录时间：2026-02-02 15:08", "籍贯：河南省新乡市", "入院情况：一般", "联系方式：187491", "现住址：河南省新乡市原阳县", "病史陈述者：患者及", "可靠程度：可靠", "患者家属", "工作单位：-", "身份证号：4107251968", "联系人：", "与患者关系：配偶", "联系人电话：1383", "主诉：确诊肺恶性肿瘤2年余，再治疗。", "现病史：患者于2年余前（2023.06）患者无明显诱因出现间断咳嗽、咳白色痰，伴有胸", "闷、纳差、乏力症状，活动后胸闷症状加重，于我院门诊行胸部CT示：两肺多发异常密度病变，", "较2023-03-15老片病变范围增大，结合2021-09-07片和2023-03-15片，注意警惕肺粘膜相关性淋", "巴瘤或肺炎型肺癌并两肺转移的可能性，建议支气管镜活检病理学检查，给予支气管肺泡灌洗（", "2024.06.15）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组织细胞，另见少许异型细", "胞，呈腺样结构，不除外腺癌，请结合临床及影像学。后至郑州大学第一附属医院确诊为肺腺癌", "（未见报告），具体不详，给予靶向治疗初始为阿美替尼，后调整为伏美替尼（不详）；复查CT", "（2024.11.12）：1、肺癌治疗后改变，对比2024-08-20片病变较前范围增大；2、左肺上叶下舌", "段及下叶后底段局限性支气管扩张；3、两肺多发微、小结节，较前右肺中叶结节稍增大，余相", "仿；4、右肺中叶少许慢性炎症；5、左侧第6肋骨顺位欠佳；6、提示左侧肾上腺结节，建议动态", "观察；请结合临床、病史及其它相关检查。2024.11.16调整为贝福替尼靶向治疗，2024.12.12于", "郑州大学第一附属医院复查CT：1.左肺多发团片影；2.双肺炎症，较前减轻；3.双肺多发结节，", "较前部分增大；4.双侧胸膜局限性增厚；5.左侧肾上腺内侧支结节，较前变化不大。给予抗感染", "及对症支持治疗后好转出院。2025.5.7复查CT：、肺癌治疗后改变，对比2025-01-11片病变较前", "增大；2、双肺局限性支气管扩张；3、左肺下叶空腔病灶，较前增大；4、两肺多发微、小结", "节，建议动态观察；5、双肺炎性病变；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，对比较", "前相仿；请结合临床、病史及其它相关检查。综合评估患者病情进展，与患者及家属沟通后，排", "除禁忌症后，2025.5.15，2025.6.14给予AP方案化疗2周期，过程顺利。基因检测（", "2025.7.12）：BRAF突变、EGFR突变、MSS型。后给予曲美替尼联合达拉替尼靶向治疗，期间因病", "第1页"]

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
2026-08-10 18:57:08,508 INFO     29 [qwen-vl-parser] text API response (len=936):
["入院记录", "姓名", "住院号", "。患者治疗后出现发热，体温38.7°C，化验示白细胞2.05*109/L，中性粒细胞0.7", "5*109/L，给予升白对症处理。患者自上次出院后，饮食、睡眠可，大小便未见明显", "异常，体重无明显改变。", "既往史：既往身体健康，否认高血压，否认糖尿病，否认冠心病，否认结核等传染病", "史及密切接触史，否认外伤史，否认手术史，否认输血史，预防接种史：随当地，过", "敏史：食物过敏史：无，药物过敏史：无。", "个人史：生于原籍，无外地久居史，无疫区到访及停留史，无工业毒物、粉尘、放射", "性物质接触史，吸烟史：无，饮酒史：无。", "月经史：已绝经。", "婚育史：已婚，已育。", "家族史：否认家族遗传病史。", "体格检查", "T:36℃ P:97次/分 R:23次/分 血压：154/94mmHg 体重：72kg 身高：16", "0cm NRS：0", "一般情况：老年女性，神志清晰，精神好，发育正常，营养良好，自主体位，查体合作", "。", "皮肤、粘膜：颜色红润，无皮肤黄疸，无明显皮肤红肿硬肿，无凹陷性水肿，无皮疹", "，未见出血点，未见瘀斑。皮肤弹性好。无肿大淋巴结。", "头部及其器官：头颅无畸形；双眼无畸形，双侧瞳孔等大，对光反射存在；双耳无畸", "形；鼻无畸形。口唇红润，无唇裂，咽无充血。", "颈部：无抵抗感，气管居中，胸锁乳突肌包块：无。甲状腺正常，无颈部淋巴结肿大", "。", "胸部：双侧对称，无畸形；双肩等高，呼吸动度双侧一致，三凹征阴性。肺呼吸音：", "清，未闻及干湿性啰音，未闻及胸膜摩擦音。", "心脏：心前区无隆起，心尖搏动位于左侧锁骨中线第5肋间，心音有力，心律齐，未", "闻及明显杂音，无心包摩擦音。", "腹部：腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。腹部叩诊呈", "鼓音；肠鸣音正常，4次/分。", "肛门外生殖器：肛门位置正常。外阴外观无畸形。", "脊柱：脊柱生理曲度正常。", "四肢：四肢肌力正常，肌张力正常。", "神经系统：双侧腱反射正常，脑膜刺激征阴性，双侧病理征阴性。", "专科情况", "无。"]
2026-08-10 18:57:08,508 INFO     29 [qwen-vl-parser] page=2 text: 37 lines (bbox 43-79)
2026-08-10 18:57:08,508 INFO     29 [qwen-vl-parser] page=2 text: 37 sections
2026-08-10 18:57:08,748 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3575834, prompt_len=764
2026-08-10 18:57:09,669 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:57:09,669 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 18:57:09,684 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3575834, prompt_len=401
2026-08-10 18:57:14,964 INFO     29 [qwen-vl-parser] text API response (len=738):
["入院记录", "辅助检查", "日期", "项目", "结果", "2020-07-29", "胸部CT", "考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检，双肺间质性改变，右肾结石", "2020-08-10", "肺功能", "肺通气功能正常", "2020-08-10", "胸部强化CT", "考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检；右肺门淋巴结肿大；双肺纤维灶；肝囊肿；右肾结石", "2020-08-10", "肺组织活检", "（右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1 (+), CK7(+), Ki-67阳性率10%", "2020-08-14", "骨扫描", "1.右肺坐骨支局限性骨质代谢增高观察；2.L5山医", "2020-08-16", "颅脑MR强化", "强化后FLAIR显示右侧颞枕叶脑沟内条片状轻度山医", "2020-08-31", "肺组织术后病理", "（右肺上叶）浸润性腺癌，腺泡型（60%），乳山医", "2020-09-23", "基因检测", "EGFR等十基因检测（石蜡包埋组织）：EFGR基山医", "2022-06-01", "胸部CT平扫", "右肺术后CT表现，请结合临床；双肺纤维灶左山医", "2023-03-29", "胸部CT平扫", "右肺术后CT表现，较2022-06-01 前片变化不大；双肺多发小结节，对比2022-06-01 前片", "2023-09-13", "CT平扫", "双侧基底节区少许缺血变性灶，必要时结合MRI", "第 3 页"]
2026-08-10 18:57:14,965 INFO     29 [qwen-vl-parser] page=3 text: 39 lines (bbox 80-118)
2026-08-10 18:57:14,965 INFO     29 [qwen-vl-parser] page=3 text: 39 sections
2026-08-10 18:57:15,150 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2691417, prompt_len=764
2026-08-10 18:57:15,905 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:57:15,905 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 18:57:15,919 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2691417, prompt_len=401
2026-08-10 18:57:21,075 INFO     29 [qwen-vl-parser] text API response (len=383):
["入院记录", "住", "2023-11-07", "强化CT", "右肺术后，右肺纤维灶，右侧胸膜增厚，较", "2023-09-19 CT变化不著；双肺多发小结节，", "较前变化不著，请结合临床、随诊复查；提示", "轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊", "肿、左肾盂旁囊肿；右肾小结石、右肾轻度积", "水；右侧附件区囊性低密度，请结合临床及妇", "科超声；左侧耻骨高密度，较前变化不著", "初步诊断：", "1. 右肺上叶浸润性腺癌术后（T1bN2M0, I", "IIA期 EGFR突变：Exon-20（外显子） 20-i", "ns突变阳性）", "2. 右肾结石", "3. 子宫切除术后", "4. 化疗后骨髓抑制", "记录者：", "项目内容", "患方签名", "以上所记录内容属实", "签字时间", "年 月 日 时 分"]
2026-08-10 18:57:21,076 INFO     29 [qwen-vl-parser] page=4 text: 24 lines (bbox 119-142)
2026-08-10 18:57:21,076 INFO     29 [qwen-vl-parser] page=4 text: 24 sections
2026-08-10 18:57:21,306 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3791969, prompt_len=764
2026-08-10 18:57:22,177 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:57:22,177 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 18:57:22,189 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3791969, prompt_len=401
2026-08-10 18:57:26,595 INFO     29 [qwen-vl-text] coord API raw response (len=3241):
[
	{"text": "原阳县人民医院", "bbox": [411, 208, 618, 234]},
	{"text": "入院记录", "bbox": [457, 236, 574, 258]},
	{"text": "姓名：", "bbox": [160, 250, 194, 262]},
	{"text": "科室：肿瘤内科病区 床号：13床 住院号：023", "bbox": [263, 253, 575, 272]},
	{"text": "科室：肿瘤内科病区 第（9）次住院", "bbox": [160, 269, 457, 290]},
	{"text": "药物过敏史：无", "bbox": [575, 280, 695, 296]},
	{"text": "姓名：", "bbox": [160, 288, 200, 300]},
	{"text": "性别：女", "bbox": [307, 291, 375, 306]},
	{"text": "年龄：57岁", "bbox": [424, 294, 508, 309]},
	{"text": "入院时间：2026-02-02 14:26", "bbox": [575, 299, 794, 317]},
	{"text": "职业：农民", "bbox": [158, 306, 242, 320]},
	{"text": "民族：汉族", "bbox": [305, 310, 391, 325]},
	{"text": "婚姻：已婚", "bbox": [422, 313, 508, 328]},
	{"text": "记录时间：2026-02-02 15:08", "bbox": [574, 318, 793, 336]},
	{"text": "籍贯：河南省新乡市", "bbox": [156, 325, 308, 341]},
	{"text": "入院情况：一般", "bbox": [421, 332, 540, 348]},
	{"text": "联系方式：187491", "bbox": [572, 336, 711, 352]},
	{"text": "现住址：河南省新乡市原阳县", "bbox": [154, 343, 388, 361]},
	{"text": "病史陈述者：患者及", "bbox": [470, 351, 623, 367]},
	{"text": "可靠程度：可靠", "bbox": [640, 356, 760, 370]},
	{"text": "患者家属", "bbox": [469, 368, 538, 381]},
	{"text": "工作单位：-", "bbox": [148, 378, 242, 392]},
	{"text": "身份证号：4107251968", "bbox": [468, 385, 645, 401]},
	{"text": "联系人：", "bbox": [143, 396, 202, 409]},
	{"text": "与患者关系：配偶", "bbox": [368, 400, 506, 416]},
	{"text": "联系人电话：1383", "bbox": [588, 405, 732, 420]},
	{"text": "主诉：确诊肺恶性肿瘤2年余，再治疗。", "bbox": [173, 414, 468, 432]},
	{"text": "现病史：患者于2年余前（2023.06）患者无明显诱因出现间断咳嗽、咳白色痰，伴有胸", "bbox": [170, 432, 834, 459]},
	{"text": "闷、纳差、乏力症状，活动后胸闷症状加重，于我院门诊行胸部CT示：两肺多发异常密度病变，", "bbox": [132, 450, 856, 478]},
	{"text": "较2023-03-15老片病变范围增大，结合2021-09-07片和2023-03-15片，注意警惕肺粘膜相关性淋", "bbox": [129, 468, 868, 496]},
	{"text": "巴瘤或肺炎型肺癌并两肺转移的可能性，建议支气管镜活检病理学检查，给予支气管肺泡灌洗（", "bbox": [127, 487, 867, 515]},
	{"text": "2024.06.15）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组织细胞，另见少许异型细", "bbox": [123, 506, 870, 534]},
	{"text": "胞，呈腺样结构，不除外腺癌，请结合临床及影像学。后至郑州大学第一附属医院确诊为肺腺癌", "bbox": [120, 525, 870, 553]},
	{"text": "（未见报告），具体不详，给予靶向治疗初始为阿美替尼，后调整为伏美替尼（不详）；复查CT", "bbox": [125, 544, 871, 572]},
	{"text": "（2024.11.12）：1、肺癌治疗后改变，对比2024-08-20片病变较前范围增大；2、左肺上叶下舌", "bbox": [109, 563, 871, 591]},
	{"text": "段及下叶后底段局限性支气管扩张；3、两肺多发微、小结节，较前右肺中叶结节稍增大，余相", "bbox": [108, 582, 865, 610]},
	{"text": "仿；4、右肺中叶少许慢性炎症；5、左侧第6肋骨顺位欠佳；6、提示左侧肾上腺结节，建议动态", "bbox": [105, 601, 874, 630]},
	{"text": "观察；请结合临床、病史及其它相关检查。2024.11.16调整为贝福替尼靶向治疗，2024.12.12于", "bbox": [100, 621, 875, 650]},
	{"text": "郑州大学第一附属医院复查CT：1.左肺多发团片影；2.双肺炎症，较前减轻；3.双肺多发结节，", "bbox": [95, 641, 867, 670]},
	{"text": "较前部分增大；4.双侧胸膜局限性增厚；5.左侧肾上腺内侧支结节，较前变化不大。给予抗感染", "bbox": [89, 661, 881, 691]},
	{"text": "及对症支持治疗后好转出院。2025.5.7复查CT：、肺癌治疗后改变，对比2025-01-11片病变较前", "bbox": [83, 681, 884, 712]},
	{"text": "增大；2、双肺局限性支气管扩张；3、左肺下叶空腔病灶，较前增大；4、两肺多发微、小结", "bbox": [76, 702, 858, 734]},
	{"text": "节，建议动态观察；5、双肺炎性病变；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，对比较", "bbox": [71, 724, 892, 758]},
	{"text": "前相仿；请结合临床、病史及其它相关检查。综合评估患者病情进展，与患者及家属沟通后，排", "bbox": [62, 746, 896, 781]},
	{"text": "除禁忌症后，2025.5.15，2025.6.14给予AP方案化疗2周期，过程顺利。基因检测（", "bbox": [52, 770, 788, 805]},
	{"text": "2025.7.12）：BRAF突变、EGFR突变、MSS型。后给予曲美替尼联合达拉替尼靶向治疗，期间因病", "bbox": [42, 795, 907, 833]},
	{"text": "第1页", "bbox": [432, 855, 499, 870]}
]
2026-08-10 18:57:26,596 INFO     29 [qwen-vl-text] coord API: raw_items=47, valid_items=47, elapsed=28.6s
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[411, 208, 618, 234]
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[457, 236, 574, 258]
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[160, 250, 194, 262]
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[3]: text=科室：肿瘤内科病区 床号：13床 住院号：023, bbox=[263, 253, 575, 272]
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[4]: text=科室：肿瘤内科病区 第（9）次住院, bbox=[160, 269, 457, 290]
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[5]: text=药物过敏史：无, bbox=[575, 280, 695, 296]
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[6]: text=姓名：, bbox=[160, 288, 200, 300]
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[7]: text=性别：女, bbox=[307, 291, 375, 306]
2026-08-10 18:57:26,598 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：57岁, bbox=[424, 294, 508, 309]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[9]: text=入院时间：2026-02-02 14:26, bbox=[575, 299, 794, 317]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[10]: text=职业：农民, bbox=[158, 306, 242, 320]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[11]: text=民族：汉族, bbox=[305, 310, 391, 325]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[12]: text=婚姻：已婚, bbox=[422, 313, 508, 328]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[13]: text=记录时间：2026-02-02 15:08, bbox=[574, 318, 793, 336]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[14]: text=籍贯：河南省新乡市, bbox=[156, 325, 308, 341]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[15]: text=入院情况：一般, bbox=[421, 332, 540, 348]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[16]: text=联系方式：187491, bbox=[572, 336, 711, 352]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[17]: text=现住址：河南省新乡市原阳县, bbox=[154, 343, 388, 361]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[18]: text=病史陈述者：患者及, bbox=[470, 351, 623, 367]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[19]: text=可靠程度：可靠, bbox=[640, 356, 760, 370]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[20]: text=患者家属, bbox=[469, 368, 538, 381]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[21]: text=工作单位：-, bbox=[148, 378, 242, 392]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[22]: text=身份证号：4107251968, bbox=[468, 385, 645, 401]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[23]: text=联系人：, bbox=[143, 396, 202, 409]
2026-08-10 18:57:26,599 INFO     29 [qwen-vl-text] coord item[24]: text=与患者关系：配偶, bbox=[368, 400, 506, 416]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[25]: text=联系人电话：1383, bbox=[588, 405, 732, 420]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[26]: text=主诉：确诊肺恶性肿瘤2年余，再治疗。, bbox=[173, 414, 468, 432]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[27]: text=现病史：患者于2年余前（2023.06）患者无明显诱因出现间断咳嗽、咳白色痰，伴有胸, bbox=[170, 432, 834, 459]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[28]: text=闷、纳差、乏力症状，活动后胸闷症状加重，于我院门诊行胸部CT示：两肺多发异常密度病变，, bbox=[132, 450, 856, 478]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[29]: text=较2023-03-15老片病变范围增大，结合2021-09-07片和2023-03-15片，注意警惕肺粘膜相关性淋, bbox=[129, 468, 868, 496]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[30]: text=巴瘤或肺炎型肺癌并两肺转移的可能性，建议支气管镜活检病理学检查，给予支气管肺泡灌洗（, bbox=[127, 487, 867, 515]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[31]: text=2024.06.15）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组织细胞，另见少许异型细, bbox=[123, 506, 870, 534]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[32]: text=胞，呈腺样结构，不除外腺癌，请结合临床及影像学。后至郑州大学第一附属医院确诊为肺腺癌, bbox=[120, 525, 870, 553]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[33]: text=（未见报告），具体不详，给予靶向治疗初始为阿美替尼，后调整为伏美替尼（不详）；复查CT, bbox=[125, 544, 871, 572]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[34]: text=（2024.11.12）：1、肺癌治疗后改变，对比2024-08-20片病变较前范围增大；2、左肺上叶下舌, bbox=[109, 563, 871, 591]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[35]: text=段及下叶后底段局限性支气管扩张；3、两肺多发微、小结节，较前右肺中叶结节稍增大，余相, bbox=[108, 582, 865, 610]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[36]: text=仿；4、右肺中叶少许慢性炎症；5、左侧第6肋骨顺位欠佳；6、提示左侧肾上腺结节，建议动态, bbox=[105, 601, 874, 630]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[37]: text=观察；请结合临床、病史及其它相关检查。2024.11.16调整为贝福替尼靶向治疗，2024.12.12于, bbox=[100, 621, 875, 650]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[38]: text=郑州大学第一附属医院复查CT：1.左肺多发团片影；2.双肺炎症，较前减轻；3.双肺多发结节，, bbox=[95, 641, 867, 670]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[39]: text=较前部分增大；4.双侧胸膜局限性增厚；5.左侧肾上腺内侧支结节，较前变化不大。给予抗感染, bbox=[89, 661, 881, 691]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[40]: text=及对症支持治疗后好转出院。2025.5.7复查CT：、肺癌治疗后改变，对比2025-01-11片病变较前, bbox=[83, 681, 884, 712]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[41]: text=增大；2、双肺局限性支气管扩张；3、左肺下叶空腔病灶，较前增大；4、两肺多发微、小结, bbox=[76, 702, 858, 734]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[42]: text=节，建议动态观察；5、双肺炎性病变；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，对比较, bbox=[71, 724, 892, 758]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[43]: text=前相仿；请结合临床、病史及其它相关检查。综合评估患者病情进展，与患者及家属沟通后，排, bbox=[62, 746, 896, 781]
2026-08-10 18:57:26,600 INFO     29 [qwen-vl-text] coord item[44]: text=除禁忌症后，2025.5.15，2025.6.14给予AP方案化疗2周期，过程顺利。基因检测（, bbox=[52, 770, 788, 805]
2026-08-10 18:57:26,601 INFO     29 [qwen-vl-text] coord item[45]: text=2025.7.12）：BRAF突变、EGFR突变、MSS型。后给予曲美替尼联合达拉替尼靶向治疗，期间因病, bbox=[42, 795, 907, 833]
2026-08-10 18:57:26,601 INFO     29 [qwen-vl-text] coord item[46]: text=第1页, bbox=[432, 855, 499, 870]
2026-08-10 18:57:26,601 INFO     29 [qwen-vl-text] page=5 — 47/47 coords, api_time=28.6s
2026-08-10 18:57:26,606 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2716842, prompt_len=1638
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["原阳县人民医院", "入院记录", "姓名：", "科室：肿瘤内科病区 床号：13床 住院号：02", "情缓慢进展，加用阿美替尼靶向治疗：复查CT（2025.12.20）：1、肺癌并纵隔淋巴结转移治疗", "后改变，对比2025-12-03片较前相仿：2、双肺局限性支气管扩张；3、双肺小空泡病灶，较前壁", "增厚；4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；5、双肺炎性病变，较前相", "仿；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，考虑转移，较前大致相仿；8、肝囊肿；请", "结合临床、病史及其它相关检查。排除禁忌症后，2026.1.14给予AC+AK112方案治疗1周期，过程", "顺利。近两日患者诉纳差乏力，伴胸闷、气短，伴咳嗽咳痰，现患者为进一步治疗入院，门诊以", "“肺恶性肿瘤”收入院。患病来，神志清，精神差，饮食量少，睡眠可，大便可，小便可，近期", "体重未监测。", "既往史：否认高血压，否认心脏病史，否认糖尿病，否认哮喘，否认脑血管，否认精神疾病史,", "既往有“慢性乙型病毒性肝炎”病史30年。否认结核，否认疟疾，否认手术史，否认外伤史，否", "认输血史，否认食物、药物过敏史，预防接种史不详。", "个人史：生于河南省新乡市原阳县，无长期外地居住史。无特殊生活习惯，否认嗜酒史、", "吸烟史，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，否认疫水，疫源接触史，无冶游", "史。", "婚育史：已婚，22岁结婚，配偶健在。育有2子1女，子女体健。", "月经生育史：妊娠3次，生产3次，无流产、早产、手术产、死产，无节育、绝育。育有3个", "5-7", "子女，均顺产。初潮13岁28-30末次月经时间52岁。月经周期规则，月经量中等，颜色正常。无血", "块、无痛经", "家族史：父亲体健，母亲已故，死因不详，1弟2妹身体健康。无类似患者疾病、传染性疾", "病、遗传性疾病。", "患者信息及病史采集真实准确 患者（授权人）确认签字：", "签名日期：2026-02-02 15:10", "体格检查", "体温：36.1℃ 脉搏：108次/分 呼吸：21次/分 血压：89/63mmHg", "身高：165cm 体重：60Kg S：1.68m2", "一般情况：发育正常，营养中等，神志清晰，精神差，体位主动，面容正常，表情安静，步态正常，", "检查合作。", "第2页"]

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
2026-08-10 18:57:28,483 INFO     29 [qwen-vl-parser] text API response (len=665):
["X光号：", "出院记录", "入院日期：2024年1月17日10点52分", "性别：女", "出院日期：2024年1月20日07点00分", "年龄：60岁", "住院天数：3天", "入院情况：1. 患者老年女性因“肺腺癌5周期化疗后2年进展后化疗5周期后", "”入院治疗。2. 体格检查：双肺呼吸音清，未闻及干湿性啰音，未闻及胸膜摩擦", "音。心律齐，未闻及明显杂音，无心包摩擦音。腹部平坦，无腹壁静脉曲张。全", "腹柔软，无包块；脾肋下未触及。", "入院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo", "n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨", "髓抑制", "诊疗经过：入院后完善各项相关检查，排除禁忌于2024.1.19给予培美曲塞", "二钠800mg+卡铂400mg，耐受可。", "出院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo", "n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨", "髓抑制", "出院情况：一般状况可。", "出院医嘱：出院后注意休息，加强营养，避免感染；定期复查血常规，每周", "1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；2024.2.9返院继续", "治疗；不适务必及时随诊。", "医师签名：", "签字时间：2024年1月20日07点00分", "第1页"]
2026-08-10 18:57:28,483 INFO     29 [qwen-vl-parser] page=5 text: 26 lines (bbox 143-168)
2026-08-10 18:57:28,483 INFO     29 [qwen-vl-parser] page=5 text: 26 sections
2026-08-10 18:57:28,746 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3306772, prompt_len=764
2026-08-10 18:57:33,446 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:57:33,447 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 18:57:33,465 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3306772, prompt_len=401
2026-08-10 18:57:38,222 INFO     29 [qwen-vl-parser] text API response (len=742):
["门诊病历", "初诊", "复诊", "门诊号", "就诊", "姓名", "性别：女", "年龄：60岁", "身份", "职业：农民", "就诊时间：2024-03-01 08:13:19", "联系人", "联系电话", "现住址", "T:", "℃", "P:", "次/分", "R:", "次/分", "BP:", "/", "mmHg", "处方", "检查", "检验", "医疗医嘱", "主诉：", "肺Ca术后3年余，肺结节？", "现病史：", "3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）", "20-ins突变阳性。", "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双", "肺多发小结节，较前变化不著，请结合临床、随诊复查。", "既往史：", "否认其他病史。", "家族史：", "否认家族史。", "过敏史：", "体征：", "辅助检查：", "2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小", "结节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于", "左肺下叶外基底段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03", "提示浸润性腺癌，大小3*2.5cm，查见淋巴结转移癌", "初步诊断：", "肺癌", "修正诊断：", "肺癌术后肺结节", "处方：", "检查：", "检验：", "医疗医嘱：", "其他建议：", "建议3月后复查", "已告知患者病情及可能的药物不良反应。", "医生签"]
2026-08-10 18:57:38,224 INFO     29 [qwen-vl-parser] page=6 text: 57 lines (bbox 169-225)
2026-08-10 18:57:38,224 INFO     29 [qwen-vl-parser] page=6 text: 57 sections
2026-08-10 18:57:38,463 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3539559, prompt_len=764
2026-08-10 18:57:39,593 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:57:39,594 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 18:57:39,606 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3539559, prompt_len=401
2026-08-10 18:57:46,150 INFO     29 [qwen-vl-parser] text API response (len=962):
["门诊病历", "性别：女", "年龄：61岁", "民族：汉族", "婚姻：已婚", "职业：农民", "证件类型：居民身份证", "证件号码", "门诊编号", "就诊医院", "就诊科室：", "就诊日期：2024-08-13 08:50:41", "初诊/复诊：初诊  复诊", "陪检者姓名：", "陪检者与患者的关系：", "联系电话", "处方", "检查", "检验", "医疗医嘱", "主诉：肺Ca术后3年余，肺结节？", "现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "ins突变阳性。", "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "节，较前变化不著，请结合临床、随诊复查。", "既往史：否认其他病史。", "家族史：否认家族史", "过敏史：无", "体温（℃）", "脉博（次/分）", "收缩压（mmHg）", "舒张压（mmHg）", "呼吸（次/分）", "意识状态  清醒", "主要症状和体征：", "体格检查：", "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "3*2.5cm，查见淋巴结转移癌", "初步诊断：肺癌", "修正诊断：肺癌术后", "处", "方：", "检", "验：", "门诊检验申请单（生化检验申请单），项目为：血生化 肝功 血脂（生化室）肾功（生", "化）", "门诊检验申请单（门诊检验申请单），项目为：血细胞分析五分类（静脉）（门化）", "门诊检验申请单（中心检验申请单），项目为：AFP-甲胎蛋白 CEA-癌胚抗原 NSE-神经", "元特异性烯化醇酶 非小细胞癌相关抗原（中心）", "检", "查：", "门诊检查申请单（CT检查申请单（新）），项目为：胸部CT平扫", "医疗医嘱：", "其他建议："]
2026-08-10 18:57:46,151 INFO     29 [qwen-vl-parser] page=7 text: 56 lines (bbox 226-281)
2026-08-10 18:57:46,151 INFO     29 [qwen-vl-parser] page=7 text: 56 sections
2026-08-10 18:57:46,427 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2789604, prompt_len=764
2026-08-10 18:57:47,259 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:57:47,260 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 18:57:47,276 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2789604, prompt_len=401
2026-08-10 18:57:47,808 INFO     29 [qwen-vl-text] coord API raw response (len=2377):
[
	{"text": "原阳县人民医院", "bbox": [426, 199, 640, 223]},
	{"text": "入院记录", "bbox": [474, 227, 595, 249]},
	{"text": "姓名：", "bbox": [167, 243, 206, 255]},
	{"text": "科室：肿瘤内科病区 床号：13床 住院号：02", "bbox": [274, 246, 587, 263]},
	{"text": "情缓慢进展，加用阿美替尼靶向治疗：复查CT（2025.12.20）：1、肺癌并纵隔淋巴结转移治疗", "bbox": [167, 263, 894, 293]},
	{"text": "后改变，对比2025-12-03片较前相仿：2、双肺局限性支气管扩张；3、双肺小空泡病灶，较前壁", "bbox": [165, 281, 894, 311]},
	{"text": "增厚；4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；5、双肺炎性病变，较前相", "bbox": [163, 300, 879, 329]},
	{"text": "仿；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，考虑转移，较前大致相仿；8、肝囊肿；请", "bbox": [161, 319, 898, 348]},
	{"text": "结合临床、病史及其它相关检查。排除禁忌症后，2026.1.14给予AC+AK112方案治疗1周期，过程", "bbox": [157, 338, 900, 366]},
	{"text": "顺利。近两日患者诉纳差乏力，伴胸闷、气短，伴咳嗽咳痰，现患者为进一步治疗入院，门诊以", "bbox": [154, 356, 900, 384]},
	{"text": "“肺恶性肿瘤”收入院。患病来，神志清，精神差，饮食量少，睡眠可，大便可，小便可，近期", "bbox": [154, 374, 903, 402]},
	{"text": "体重未监测。", "bbox": [148, 393, 246, 406]},
	{"text": "既往史：否认高血压，否认心脏病史，否认糖尿病，否认哮喘，否认脑血管，否认精神疾病史,", "bbox": [180, 412, 895, 436]},
	{"text": "既往有“慢性乙型病毒性肝炎”病史30年。否认结核，否认疟疾，否认手术史，否认外伤史，否", "bbox": [141, 430, 908, 454]},
	{"text": "认输血史，否认食物、药物过敏史，预防接种史不详。", "bbox": [139, 448, 565, 468]},
	{"text": "个人史：生于河南省新乡市原阳县，无长期外地居住史。无特殊生活习惯，否认嗜酒史、", "bbox": [173, 468, 884, 491]},
	{"text": "吸烟史，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，否认疫水，疫源接触史，无冶游", "bbox": [132, 486, 903, 510]},
	{"text": "史。", "bbox": [129, 507, 156, 518]},
	{"text": "婚育史：已婚，22岁结婚，配偶健在。育有2子1女，子女体健。", "bbox": [163, 527, 686, 547]},
	{"text": "月经生育史：妊娠3次，生产3次，无流产、早产、手术产、死产，无节育、绝育。育有3个", "bbox": [160, 547, 900, 570]},
	{"text": "5-7", "bbox": [323, 570, 351, 580]},
	{"text": "子女，均顺产。初潮13岁28-30末次月经时间52岁。月经周期规则，月经量中等，颜色正常。无血", "bbox": [117, 574, 904, 601]},
	{"text": "块、无痛经", "bbox": [111, 594, 206, 608]},
	{"text": "家族史：父亲体健，母亲已故，死因不详，1弟2妹身体健康。无类似患者疾病、传染性疾", "bbox": [145, 615, 907, 643]},
	{"text": "病、遗传性疾病。", "bbox": [101, 636, 245, 652]},
	{"text": "患者信息及病史采集真实准确 患者（授权人）确认签字：", "bbox": [143, 668, 647, 690]},
	{"text": "签名日期：2026-02-02 15:10", "bbox": [454, 696, 721, 715]},
	{"text": "体格检查", "bbox": [436, 719, 551, 735]},
	{"text": "体温：36.1℃ 脉搏：108次/分 呼吸：21次/分 血压：89/63mmHg", "bbox": [85, 735, 824, 765]},
	{"text": "身高：165cm 体重：60Kg S：1.68m2", "bbox": [78, 760, 561, 784]},
	{"text": "一般情况：发育正常，营养中等，神志清晰，精神差，体位主动，面容正常，表情安静，步态正常，", "bbox": [60, 782, 940, 816]},
	{"text": "检查合作。", "bbox": [50, 805, 142, 822]},
	{"text": "第2页", "bbox": [458, 874, 527, 889]}
]
2026-08-10 18:57:47,808 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=21.2s
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[426, 199, 640, 223]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[474, 227, 595, 249]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[167, 243, 206, 255]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[3]: text=科室：肿瘤内科病区 床号：13床 住院号：02, bbox=[274, 246, 587, 263]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[4]: text=情缓慢进展，加用阿美替尼靶向治疗：复查CT（2025.12.20）：1、肺癌并纵隔淋巴结转移治疗, bbox=[167, 263, 894, 293]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[5]: text=后改变，对比2025-12-03片较前相仿：2、双肺局限性支气管扩张；3、双肺小空泡病灶，较前壁, bbox=[165, 281, 894, 311]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[6]: text=增厚；4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；5、双肺炎性病变，较前相, bbox=[163, 300, 879, 329]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[7]: text=仿；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，考虑转移，较前大致相仿；8、肝囊肿；请, bbox=[161, 319, 898, 348]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[8]: text=结合临床、病史及其它相关检查。排除禁忌症后，2026.1.14给予AC+AK112方案治疗1周期，过程, bbox=[157, 338, 900, 366]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[9]: text=顺利。近两日患者诉纳差乏力，伴胸闷、气短，伴咳嗽咳痰，现患者为进一步治疗入院，门诊以, bbox=[154, 356, 900, 384]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[10]: text=“肺恶性肿瘤”收入院。患病来，神志清，精神差，饮食量少，睡眠可，大便可，小便可，近期, bbox=[154, 374, 903, 402]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[11]: text=体重未监测。, bbox=[148, 393, 246, 406]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[12]: text=既往史：否认高血压，否认心脏病史，否认糖尿病，否认哮喘，否认脑血管，否认精神疾病史,, bbox=[180, 412, 895, 436]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[13]: text=既往有“慢性乙型病毒性肝炎”病史30年。否认结核，否认疟疾，否认手术史，否认外伤史，否, bbox=[141, 430, 908, 454]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[14]: text=认输血史，否认食物、药物过敏史，预防接种史不详。, bbox=[139, 448, 565, 468]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[15]: text=个人史：生于河南省新乡市原阳县，无长期外地居住史。无特殊生活习惯，否认嗜酒史、, bbox=[173, 468, 884, 491]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[16]: text=吸烟史，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，否认疫水，疫源接触史，无冶游, bbox=[132, 486, 903, 510]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[17]: text=史。, bbox=[129, 507, 156, 518]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[18]: text=婚育史：已婚，22岁结婚，配偶健在。育有2子1女，子女体健。, bbox=[163, 527, 686, 547]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[19]: text=月经生育史：妊娠3次，生产3次，无流产、早产、手术产、死产，无节育、绝育。育有3个, bbox=[160, 547, 900, 570]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[20]: text=5-7, bbox=[323, 570, 351, 580]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[21]: text=子女，均顺产。初潮13岁28-30末次月经时间52岁。月经周期规则，月经量中等，颜色正常。无血, bbox=[117, 574, 904, 601]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[22]: text=块、无痛经, bbox=[111, 594, 206, 608]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[23]: text=家族史：父亲体健，母亲已故，死因不详，1弟2妹身体健康。无类似患者疾病、传染性疾, bbox=[145, 615, 907, 643]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[24]: text=病、遗传性疾病。, bbox=[101, 636, 245, 652]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[25]: text=患者信息及病史采集真实准确 患者（授权人）确认签字：, bbox=[143, 668, 647, 690]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[26]: text=签名日期：2026-02-02 15:10, bbox=[454, 696, 721, 715]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[27]: text=体格检查, bbox=[436, 719, 551, 735]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[28]: text=体温：36.1℃ 脉搏：108次/分 呼吸：21次/分 血压：89/63mmHg, bbox=[85, 735, 824, 765]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[29]: text=身高：165cm 体重：60Kg S：1.68m2, bbox=[78, 760, 561, 784]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[30]: text=一般情况：发育正常，营养中等，神志清晰，精神差，体位主动，面容正常，表情安静，步态正常，, bbox=[60, 782, 940, 816]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[31]: text=检查合作。, bbox=[50, 805, 142, 822]
2026-08-10 18:57:47,809 INFO     29 [qwen-vl-text] coord item[32]: text=第2页, bbox=[458, 874, 527, 889]
2026-08-10 18:57:47,810 INFO     29 [qwen-vl-text] page=6 — 33/33 coords, api_time=21.2s
2026-08-10 18:57:47,813 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2713079, prompt_len=1666
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["原阳县人民医院", "入院记录", "姓名：", "科室：肿瘤内科病区 床号：13床 住院号：", "皮肤、粘膜：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，无淤点、", "紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。", "浅表淋巴结：浅表淋巴结无无肿大。", "头部及其他器官：头颅大小正常，无异常面容，眼睑无浮肿，结膜无苍白，巩膜无黄染，双侧", "瞳孔等大等圆，左瞳孔对光反射灵敏，右瞳孔对光反射灵敏。鼻无畸形，无鼻翼煽动。鼻旁窦未", "触及明显压痛。耳廓无畸形，外耳道无异常分泌物。唇红润，口腔黏膜未见明显异常。齿龈无出", "血。双侧扁桃体无肿大。", "颈部：颈部无抵抗，颈动脉搏动正常，颈静脉正常，气管正中，肝颈静脉回流征阴性，甲状腺", "未及肿大。", "胸部：双侧胸廓正常。双侧乳房对称，左侧正常，右侧正常。胸壁无有静脉曲张或充盈、皮下", "气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。", "肺：呼吸运动正常，呼吸节律正常，语颤正常，未触及胸膜摩擦感，双肺叩诊呈清音，呼吸规", "整，双肺呼吸音减弱，可闻及湿性啰音，语音传导正常，未及明显胸膜摩擦音。", "心：胸廓基本对称，心前区无隆起，心尖搏动正常，位于第五肋间左侧锁骨中线0.5cm，强度及", "范围正常，无负性心尖搏动。心尖搏动正常，无震颤，无心包摩擦音。心脏相对浊音界正常。心", "率108次/分，心律齐，心音无额外心音，无杂音无心包摩擦音。", "桡动脉：脉搏正常，节律规则，无奇脉、交替脉。", "周围血管征：无毛细血管搏动、射枪音、水冲脉、动脉异常搏动。", "腹部：腹部平坦，胃肠蠕动波无，腹式呼吸存在，未见腹壁静脉曲张。腹柔软，液波震颤无，", "振水声无，腹部包块未触及，无压痛、无反跳痛，脾肝未触及，Murphy's征阴性，肾无压痛，叩", "击痛，腹部血管搏动未见明显异常。输尿管压痛点无明显压痛。肝浊音界存在，肝上界位于右锁", "骨中线肋间，移动性浊音无。无明显肾区叩击痛，肠鸣音正常。", "肛门、直肠：未查或详见专科检查。", "脊柱四肢：脊柱正常，四肢无畸形，四肢关节活动及动脉搏动未见明显异常。", "神经反射：生理反射存在，病理反射未引出。", "专科检查", "神志清，精神差，全身浅表淋巴结未触及肿大，双肺呼吸音减弱，可闻及湿性啰音，心率", "108次/分，心律齐，各瓣膜听诊区未闻及杂音，腹软，未触及肿块，肝脾肋下未触及，双下肢无", "第3页"]

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
2026-08-10 18:57:59,030 INFO     29 [qwen-vl-parser] text API response (len=785):
["门诊病历", "性别：女", "证件类型：居民身份证", "年龄：62岁", "证件", "民族：汉族", "门诊编", "婚姻：已婚", "就诊医院", "职业：农民", "就诊科室", "就诊日期：2025-08-12 08:11:41", "陪检者姓名：", "初诊/复诊：初诊□复诊", "陪检者与患者的关系：", "联系电话", "处方", "检查", "检验", "医疗医嘱", "主诉：肺Ca术后3年余，肺结节？", "现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "ins突变阳性。", "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "节，较前变化不著，请结合临床、随诊复查。", "既往史：否认其他病史。", "家族史：否认家族史", "过敏史：无", "体温（℃）", "脉搏（次/分）", "收缩压（mmHg）", "舒张压（mmHg）", "呼吸（次/分）", "意识状态 清醒", "主要症状和体征：", "体格检查：", "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "3*2.5cm，查见淋巴结转移癌", "初步诊断：肺癌", "修正诊断：肺癌术后", "处", "方：", "检", "验：", "检", "查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫", "医疗医嘱：", "其他建议："]
2026-08-10 18:57:59,031 INFO     29 [qwen-vl-parser] page=8 text: 50 lines (bbox 282-331)
2026-08-10 18:57:59,031 INFO     29 [qwen-vl-parser] page=8 text: 50 sections
2026-08-10 18:57:59,286 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3577488, prompt_len=764
2026-08-10 18:58:01,632 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:58:01,632 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 18:58:01,642 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3577488, prompt_len=401
2026-08-10 18:58:07,672 INFO     29 [qwen-vl-parser] text API response (len=891):
["门诊病历", "性别：女", "年龄：63岁", "民族：汉族", "婚姻：已婚", "职业：农民", "证件类型：居民身份证", "证件号", "门诊编", "就诊医院", "就诊科室", "就诊日期：2026-03-10 08:35:11", "初诊/复诊：初诊 □ 复诊", "联系电", "陪伴者姓名：", "陪伴者与患者的关系：", "处方", "检查", "检验", "医疗医嘱", "主诉：肺Ca术后4年余，肺结节？", "现病史：4年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "ins突变阳性。", "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "节，较前变化不著，请结合临床、随诊复查。", "2025.8.11CT：双肺多发小结节，较大者位于左肺外周，均较前片变化不著", "既往史：否认其他病史。", "家族史：否认家族史", "过敏史：无", "体温（℃）", "脉搏（次/分）", "收缩压（mmHg）", "舒张压（mmHg）", "呼吸（次/分）", "意识状态 清醒", "主要症状和体征：", "体格检查：", "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "3*2.5cm，查见淋巴结转移癌", "初步诊断：肺癌,肺结节", "修正诊断：肺癌,肺结节", "处方：", "检验：门诊检验申请单(临床生化检验一(临床生化检验))，项目为：血糖 糖化血红蛋白测定", "检查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫", "医疗医嘱：", "其他建议：", "已告知患者病情及可能的药物不良反应。", "医生"]
2026-08-10 18:58:07,672 INFO     29 [qwen-vl-parser] page=9 text: 50 lines (bbox 332-381)
2026-08-10 18:58:07,672 INFO     29 [qwen-vl-parser] page=9 text: 50 sections
2026-08-10 18:58:07,802 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2382202, prompt_len=764
2026-08-10 18:58:08,723 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:58:08,724 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 18:58:08,746 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2382202, prompt_len=401
2026-08-10 18:58:10,072 INFO     29 [qwen-vl-parser] text API response (len=175):
["病理检查报告单", "检查号", "住院号", "姓名", "性别:女", "结论: (右肺上叶)形态符合腺癌,待常规病理免疫组化确诊。", "此报告尚未打印", "当前报告状态: 已打印", "江苏省捷达科技发展有限公司 版权所有 © 2015", "Copyright 2007-2015 JEDA all rights reserved"]
2026-08-10 18:58:10,072 INFO     29 [qwen-vl-parser] page=10 text: 10 lines (bbox 382-391)
2026-08-10 18:58:10,072 INFO     29 [qwen-vl-parser] page=10 text: 10 sections
2026-08-10 18:58:10,207 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=897720, prompt_len=764
2026-08-10 18:58:10,789 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:58:10,790 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 18:58:10,805 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=897720, prompt_len=401
2026-08-10 18:58:11,469 INFO     29 [qwen-vl-text] coord API raw response (len=2402):
[
	{"text": "原阳县人民医院", "bbox": [417, 234, 620, 254]},
	{"text": "入院记录", "bbox": [463, 260, 577, 279]},
	{"text": "姓名：", "bbox": [170, 276, 206, 288]},
	{"text": "科室：肿瘤内科病区 床号：13床 住院号：", "bbox": [273, 278, 550, 292]},
	{"text": "皮肤、粘膜：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，无淤点、", "bbox": [169, 295, 845, 316]},
	{"text": "紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。", "bbox": [167, 313, 541, 330]},
	{"text": "浅表淋巴结：浅表淋巴结无无肿大。", "bbox": [164, 330, 424, 346]},
	{"text": "头部及其他器官：头颅大小正常，无异常面容，眼睑无浮肿，结膜无苍白，巩膜无黄染，双侧", "bbox": [162, 348, 858, 368]},
	{"text": "瞳孔等大等圆，左瞳孔对光反射灵敏，右瞳孔对光反射灵敏。鼻无畸形，无鼻翼煽动。鼻旁窦未", "bbox": [158, 365, 876, 385]},
	{"text": "触及明显压痛。耳廓无畸形，外耳道无异常分泌物。唇红润，口腔黏膜未见明显异常。齿龈无出", "bbox": [155, 381, 878, 401]},
	{"text": "血。双侧扁桃体无肿大。", "bbox": [152, 398, 332, 412]},
	{"text": "颈部：颈部无抵抗，颈动脉搏动正常，颈静脉正常，气管正中，肝颈静脉回流征阴性，甲状腺", "bbox": [148, 416, 866, 435]},
	{"text": "未及肿大。", "bbox": [145, 433, 221, 446]},
	{"text": "胸部：双侧胸廓正常。双侧乳房对称，左侧正常，右侧正常。胸壁无有静脉曲张或充盈、皮下", "bbox": [141, 451, 869, 470]},
	{"text": "气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。", "bbox": [139, 468, 480, 484]},
	{"text": "肺：呼吸运动正常，呼吸节律正常，语颤正常，未触及胸膜摩擦感，双肺叩诊呈清音，呼吸规", "bbox": [135, 487, 872, 507]},
	{"text": "整，双肺呼吸音减弱，可闻及湿性啰音，语音传导正常，未及明显胸膜摩擦音。", "bbox": [133, 505, 751, 524]},
	{"text": "心：胸廓基本对称，心前区无隆起，心尖搏动正常，位于第五肋间左侧锁骨中线0.5cm，强度及", "bbox": [129, 525, 884, 546]},
	{"text": "范围正常，无负性心尖搏动。心尖搏动正常，无震颤，无心包摩擦音。心脏相对浊音界正常。心", "bbox": [126, 543, 896, 565]},
	{"text": "率108次/分，心律齐，心音无额外心音，无杂音无心包摩擦音。", "bbox": [122, 563, 612, 581]},
	{"text": "桡动脉：脉搏正常，节律规则，无奇脉、交替脉。", "bbox": [117, 583, 501, 601]},
	{"text": "周围血管征：无毛细血管搏动、射枪音、水冲脉、动脉异常搏动。", "bbox": [113, 604, 641, 624]},
	{"text": "腹部：腹部平坦，胃肠蠕动波无，腹式呼吸存在，未见腹壁静脉曲张。腹柔软，液波震颤无，", "bbox": [107, 624, 874, 650]},
	{"text": "振水声无，腹部包块未触及，无压痛、无反跳痛，脾肝未触及，Murphy's征阴性，肾无压痛，叩", "bbox": [103, 645, 904, 673]},
	{"text": "击痛，腹部血管搏动未见明显异常。输尿管压痛点无明显压痛。肝浊音界存在，肝上界位于右锁", "bbox": [98, 667, 912, 696]},
	{"text": "骨中线肋间，移动性浊音无。无明显肾区叩击痛，肠鸣音正常。", "bbox": [92, 688, 621, 712]},
	{"text": "肛门、直肠：未查或详见专科检查。", "bbox": [85, 710, 385, 729]},
	{"text": "脊柱四肢：脊柱正常，四肢无畸形，四肢关节活动及动脉搏动未见明显异常。", "bbox": [79, 732, 747, 760]},
	{"text": "神经反射：生理反射存在，病理反射未引出。", "bbox": [71, 754, 458, 778]},
	{"text": "专科检查", "bbox": [444, 787, 527, 803]},
	{"text": "神志清，精神差，全身浅表淋巴结未触及肿大，双肺呼吸音减弱，可闻及湿性啰音，心率", "bbox": [52, 801, 873, 837]},
	{"text": "108次/分，心律齐，各瓣膜听诊区未闻及杂音，腹软，未触及肿块，肝脾肋下未触及，双下肢无", "bbox": [42, 825, 946, 864]},
	{"text": "第3页", "bbox": [443, 885, 512, 901]}
]
2026-08-10 18:58:11,469 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=23.7s
2026-08-10 18:58:11,469 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[417, 234, 620, 254]
2026-08-10 18:58:11,469 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[463, 260, 577, 279]
2026-08-10 18:58:11,469 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[170, 276, 206, 288]
2026-08-10 18:58:11,469 INFO     29 [qwen-vl-text] coord item[3]: text=科室：肿瘤内科病区 床号：13床 住院号：, bbox=[273, 278, 550, 292]
2026-08-10 18:58:11,469 INFO     29 [qwen-vl-text] coord item[4]: text=皮肤、粘膜：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，无淤点、, bbox=[169, 295, 845, 316]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[5]: text=紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。, bbox=[167, 313, 541, 330]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[6]: text=浅表淋巴结：浅表淋巴结无无肿大。, bbox=[164, 330, 424, 346]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[7]: text=头部及其他器官：头颅大小正常，无异常面容，眼睑无浮肿，结膜无苍白，巩膜无黄染，双侧, bbox=[162, 348, 858, 368]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[8]: text=瞳孔等大等圆，左瞳孔对光反射灵敏，右瞳孔对光反射灵敏。鼻无畸形，无鼻翼煽动。鼻旁窦未, bbox=[158, 365, 876, 385]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[9]: text=触及明显压痛。耳廓无畸形，外耳道无异常分泌物。唇红润，口腔黏膜未见明显异常。齿龈无出, bbox=[155, 381, 878, 401]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[10]: text=血。双侧扁桃体无肿大。, bbox=[152, 398, 332, 412]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[11]: text=颈部：颈部无抵抗，颈动脉搏动正常，颈静脉正常，气管正中，肝颈静脉回流征阴性，甲状腺, bbox=[148, 416, 866, 435]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[12]: text=未及肿大。, bbox=[145, 433, 221, 446]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[13]: text=胸部：双侧胸廓正常。双侧乳房对称，左侧正常，右侧正常。胸壁无有静脉曲张或充盈、皮下, bbox=[141, 451, 869, 470]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[14]: text=气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。, bbox=[139, 468, 480, 484]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[15]: text=肺：呼吸运动正常，呼吸节律正常，语颤正常，未触及胸膜摩擦感，双肺叩诊呈清音，呼吸规, bbox=[135, 487, 872, 507]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[16]: text=整，双肺呼吸音减弱，可闻及湿性啰音，语音传导正常，未及明显胸膜摩擦音。, bbox=[133, 505, 751, 524]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[17]: text=心：胸廓基本对称，心前区无隆起，心尖搏动正常，位于第五肋间左侧锁骨中线0.5cm，强度及, bbox=[129, 525, 884, 546]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[18]: text=范围正常，无负性心尖搏动。心尖搏动正常，无震颤，无心包摩擦音。心脏相对浊音界正常。心, bbox=[126, 543, 896, 565]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[19]: text=率108次/分，心律齐，心音无额外心音，无杂音无心包摩擦音。, bbox=[122, 563, 612, 581]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[20]: text=桡动脉：脉搏正常，节律规则，无奇脉、交替脉。, bbox=[117, 583, 501, 601]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[21]: text=周围血管征：无毛细血管搏动、射枪音、水冲脉、动脉异常搏动。, bbox=[113, 604, 641, 624]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[22]: text=腹部：腹部平坦，胃肠蠕动波无，腹式呼吸存在，未见腹壁静脉曲张。腹柔软，液波震颤无，, bbox=[107, 624, 874, 650]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[23]: text=振水声无，腹部包块未触及，无压痛、无反跳痛，脾肝未触及，Murphy's征阴性，肾无压痛，叩, bbox=[103, 645, 904, 673]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[24]: text=击痛，腹部血管搏动未见明显异常。输尿管压痛点无明显压痛。肝浊音界存在，肝上界位于右锁, bbox=[98, 667, 912, 696]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[25]: text=骨中线肋间，移动性浊音无。无明显肾区叩击痛，肠鸣音正常。, bbox=[92, 688, 621, 712]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[26]: text=肛门、直肠：未查或详见专科检查。, bbox=[85, 710, 385, 729]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[27]: text=脊柱四肢：脊柱正常，四肢无畸形，四肢关节活动及动脉搏动未见明显异常。, bbox=[79, 732, 747, 760]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[28]: text=神经反射：生理反射存在，病理反射未引出。, bbox=[71, 754, 458, 778]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[29]: text=专科检查, bbox=[444, 787, 527, 803]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[30]: text=神志清，精神差，全身浅表淋巴结未触及肿大，双肺呼吸音减弱，可闻及湿性啰音，心率, bbox=[52, 801, 873, 837]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[31]: text=108次/分，心律齐，各瓣膜听诊区未闻及杂音，腹软，未触及肿块，肝脾肋下未触及，双下肢无, bbox=[42, 825, 946, 864]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] coord item[32]: text=第3页, bbox=[443, 885, 512, 901]
2026-08-10 18:58:11,470 INFO     29 [qwen-vl-text] page=7 — 33/33 coords, api_time=23.7s
2026-08-10 18:58:11,473 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2057048, prompt_len=867
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共15行）
["原阳县人民医院", "入院记录", "姓名：", "科室：肿瘤内科病区 床号：13床 住院号：02", "水肿。", "辅助检查", "支气管肺泡灌洗（2024.06.15 我院）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组", "织细胞，另见少许异型细胞，呈腺样结构，不除外腺癌，请结合临床及影像学。", "初步诊断：", "西医诊断：", "1.恶性肿瘤支持治疗", "2.左肺恶性肿瘤 cTxNxM1 IV期", "3.肺部感染", "主治医师：爱振化", "签名日期：2026-02-02"]

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
2026-08-10 18:58:13,163 INFO     29 [qwen-vl-parser] text API response (len=355):
["病理检查报告单", "检查号", "住院号", "门诊号:", "姓名", "性别:女", "年龄:57岁", "结合202036909（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体", "呈周围型，肿物切面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内", "结论:查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第", "11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌(2/4)。另送第7组", "淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。", "此报告尚未打印", "当前报告状态:已打印"]
2026-08-10 18:58:13,164 INFO     29 [qwen-vl-parser] page=11 text: 14 lines (bbox 392-405)
2026-08-10 18:58:13,164 INFO     29 [qwen-vl-parser] page=11 text: 14 sections
2026-08-10 18:58:13,469 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3106185, prompt_len=764
2026-08-10 18:58:18,403 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2020-09-23"
}
```
2026-08-10 18:58:18,405 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2020-09-23
2026-08-10 18:58:18,431 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3106185, prompt_len=401
2026-08-10 18:58:23,022 INFO     29 [qwen-vl-parser] text API response (len=609):
["分子病理基因检测报告单", "样本信息", "项目编号：PCR20-1135", "姓名", "性别：女", "年龄：57岁", "住院号", "病理号", "送检医生", "标本类别：石蜡包埋组织", "送检科室", "送检时间：2020-09-23", "送检医院：本院", "联系电话", "检测方法：ARMS PCR", "检测位点：", "检查项目：九基因", "检测结果", "检测项目", "外显因子", "突变类型", "检测结果", "EGFR基因", "Exon19", "19-del", "野生型", "Exon21", "L858R", "野生型", "Exon20", "T790M", "野生型", "Exon18", "G719X", "野生型", "Exon20", "S768I", "野生型", "Exon21", "L861Q", "野生型", "Exon20", "20-ins", "突变型", "KRAS基因", "Exon-2", "G12D/S", "野生型", "G12A/V/R/C、G13C", "野生型", "BRAF基因", "Exon-15", "V600E/K/R/D", "野生型", "NRAS基因", "Exon-3", "Q61R/K/L/H", "野生型", "初诊医师：戚美", "复诊医师：刘龙", "报告日期：2020-09-23"]
2026-08-10 18:58:23,024 INFO     29 [qwen-vl-parser] page=12 text: 61 lines (bbox 406-466)
2026-08-10 18:58:23,024 INFO     29 [qwen-vl-parser] page=12 text: 61 sections
2026-08-10 18:58:24,622 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3528127, prompt_len=764
2026-08-10 18:58:25,242 INFO     29 [qwen-vl-text] coord API raw response (len=872):
[
	{"text": "原阳县人民医院", "bbox": [418, 189, 636, 214]},
	{"text": "入院记录", "bbox": [466, 218, 590, 240]},
	{"text": "姓名：", "bbox": [150, 233, 190, 245]},
	{"text": "科室：肿瘤内科病区 床号：13床 住院号：02", "bbox": [260, 237, 580, 254]},
	{"text": "水肿。", "bbox": [150, 253, 191, 265]},
	{"text": "辅助检查", "bbox": [486, 281, 558, 295]},
	{"text": "支气管肺泡灌洗（2024.06.15 我院）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组", "bbox": [143, 291, 892, 323]},
	{"text": "织细胞，另见少许异型细胞，呈腺样结构，不除外腺癌，请结合临床及影像学。", "bbox": [139, 309, 767, 338]},
	{"text": "初步诊断：", "bbox": [509, 356, 590, 369]},
	{"text": "西医诊断：", "bbox": [508, 374, 590, 387]},
	{"text": "1.恶性肿瘤支持治疗", "bbox": [590, 394, 760, 408]},
	{"text": "2.左肺恶性肿瘤 cTxNxM1 IV期", "bbox": [588, 412, 850, 427]},
	{"text": "3.肺部感染", "bbox": [587, 431, 686, 444]},
	{"text": "主治医师：爱振化", "bbox": [720, 460, 868, 473]},
	{"text": "签名日期：2026-02-02", "bbox": [668, 480, 868, 495]}
]
2026-08-10 18:58:25,243 INFO     29 [qwen-vl-text] coord API: raw_items=15, valid_items=15, elapsed=13.8s
2026-08-10 18:58:25,243 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[418, 189, 636, 214]
2026-08-10 18:58:25,243 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[466, 218, 590, 240]
2026-08-10 18:58:25,243 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[150, 233, 190, 245]
2026-08-10 18:58:25,243 INFO     29 [qwen-vl-text] coord item[3]: text=科室：肿瘤内科病区 床号：13床 住院号：02, bbox=[260, 237, 580, 254]
2026-08-10 18:58:25,243 INFO     29 [qwen-vl-text] coord item[4]: text=水肿。, bbox=[150, 253, 191, 265]
2026-08-10 18:58:25,243 INFO     29 [qwen-vl-text] coord item[5]: text=辅助检查, bbox=[486, 281, 558, 295]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[6]: text=支气管肺泡灌洗（2024.06.15 我院）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组, bbox=[143, 291, 892, 323]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[7]: text=织细胞，另见少许异型细胞，呈腺样结构，不除外腺癌，请结合临床及影像学。, bbox=[139, 309, 767, 338]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[8]: text=初步诊断：, bbox=[509, 356, 590, 369]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[9]: text=西医诊断：, bbox=[508, 374, 590, 387]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[10]: text=1.恶性肿瘤支持治疗, bbox=[590, 394, 760, 408]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[11]: text=2.左肺恶性肿瘤 cTxNxM1 IV期, bbox=[588, 412, 850, 427]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[12]: text=3.肺部感染, bbox=[587, 431, 686, 444]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[13]: text=主治医师：爱振化, bbox=[720, 460, 868, 473]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] coord item[14]: text=签名日期：2026-02-02, bbox=[668, 480, 868, 495]
2026-08-10 18:58:25,244 INFO     29 [qwen-vl-text] page=8 — 15/15 coords, api_time=13.8s
2026-08-10 18:58:25,245 INFO     29 [qwen-vl-text] new_positions (128):
[[5, 443.88000000000005, 667.44, 399.36, 449.28], [5, 493.56000000000006, 619.9200000000001, 453.12, 495.35999999999996], [5, 172.8, 209.52, 480.0, 503.03999999999996], [5, 284.04, 621.0, 485.76, 522.24], [5, 172.8, 493.56000000000006, 516.48, 556.8], [5, 621.0, 750.6, 537.6, 568.3199999999999], [5, 172.8, 216.0, 552.96, 576.0], [5, 331.56, 405.0, 558.72, 587.52], [5, 457.92, 548.64, 564.48, 593.28], [5, 621.0, 857.5200000000001, 574.0799999999999, 608.64], [5, 170.64000000000001, 261.36, 587.52, 614.4], [5, 329.40000000000003, 422.28000000000003, 595.1999999999999, 624.0], [5, 455.76000000000005, 548.64, 600.9599999999999, 629.76], [5, 619.9200000000001, 856.44, 610.56, 645.12], [5, 168.48000000000002, 332.64000000000004, 624.0, 654.72], [5, 454.68, 583.2, 637.4399999999999, 668.16], [5, 617.76, 767.88, 645.12, 675.8399999999999], [5, 166.32000000000002, 419.04, 658.56, 693.12], [5, 507.6, 672.84, 673.92, 704.64], [5, 691.2, 820.8000000000001, 683.52, 710.4], [5, 506.52000000000004, 581.0400000000001, 706.56, 731.52], [5, 159.84, 261.36, 725.76, 752.64], [5, 505.44000000000005, 696.6, 739.1999999999999, 769.92], [5, 154.44, 218.16000000000003, 760.3199999999999, 785.28], [5, 397.44000000000005, 546.48, 768.0, 798.72], [5, 635.0400000000001, 790.5600000000001, 777.6, 806.4], [5, 186.84, 505.44000000000005, 794.88, 829.4399999999999], [5, 183.60000000000002, 900.72, 829.4399999999999, 881.28], [5, 142.56, 924.48, 864.0, 917.76], [5, 139.32000000000002, 937.44, 898.56, 952.3199999999999], [5, 137.16, 936.36, 935.04, 988.8], [5, 132.84, 939.6, 971.52, 1025.28], [5, 129.60000000000002, 939.6, 1008.0, 1061.76], [5, 135.0, 940.6800000000001, 1044.48, 1098.24], [5, 117.72000000000001, 940.6800000000001, 1080.96, 1134.72], [5, 116.64000000000001, 934.2, 1117.44, 1171.2], [5, 113.4, 943.9200000000001, 1153.9199999999998, 1209.6], [5, 108.0, 945.0000000000001, 1192.32, 1248.0], [5, 102.60000000000001, 936.36, 1230.72, 1286.3999999999999], [5, 96.12, 951.48, 1269.12, 1326.72], [5, 89.64, 954.72, 1307.52, 1367.04], [5, 82.08000000000001, 926.6400000000001, 1347.84, 1409.28], [5, 76.68, 963.36, 1390.08, 1455.36], [5, 66.96000000000001, 967.6800000000001, 1432.32, 1499.52], [5, 56.160000000000004, 851.0400000000001, 1478.3999999999999, 1545.6], [5, 45.36, 979.5600000000001, 1526.3999999999999, 1599.36], [5, 466.56000000000006, 538.9200000000001, 1641.6, 1670.3999999999999], [6, 460.08000000000004, 691.2, 382.08, 428.15999999999997], [6, 511.92, 642.6, 435.84, 478.08], [6, 180.36, 222.48000000000002, 466.56, 489.59999999999997], [6, 295.92, 633.96, 472.32, 504.96], [6, 180.36, 965.5200000000001, 504.96, 562.56], [6, 178.20000000000002, 965.5200000000001, 539.52, 597.12], [6, 176.04000000000002, 949.32, 576.0, 631.68], [6, 173.88000000000002, 969.84, 612.48, 668.16], [6, 169.56, 972.0000000000001, 648.9599999999999, 702.72], [6, 166.32000000000002, 972.0000000000001, 683.52, 737.28], [6, 166.32000000000002, 975.24, 718.0799999999999, 771.8399999999999], [6, 159.84, 265.68, 754.56, 779.52], [6, 194.4, 966.6, 791.04, 837.12], [6, 152.28, 980.6400000000001, 825.6, 871.68], [6, 150.12, 610.2, 860.16, 898.56], [6, 186.84, 954.72, 898.56, 942.7199999999999], [6, 142.56, 975.24, 933.12, 979.1999999999999], [6, 139.32000000000002, 168.48000000000002, 973.4399999999999, 994.56], [6, 176.04000000000002, 740.88, 1011.8399999999999, 1050.24], [6, 172.8, 972.0000000000001, 1050.24, 1094.3999999999999], [6, 348.84000000000003, 379.08000000000004, 1094.3999999999999, 1113.6], [6, 126.36000000000001, 976.32, 1102.08, 1153.9199999999998], [6, 119.88000000000001, 222.48000000000002, 1140.48, 1167.36], [6, 156.60000000000002, 979.5600000000001, 1180.8, 1234.56], [6, 109.08000000000001, 264.6, 1221.12, 1251.84], [6, 154.44, 698.76, 1282.56, 1324.8], [6, 490.32000000000005, 778.6800000000001, 1336.32, 1372.8], [6, 470.88000000000005, 595.08, 1380.48, 1411.2], [6, 91.80000000000001, 889.9200000000001, 1411.2, 1468.8], [6, 84.24000000000001, 605.88, 1459.2, 1505.28], [6, 64.80000000000001, 1015.2, 1501.44, 1566.72], [6, 54.0, 153.36, 1545.6, 1578.24], [6, 494.64000000000004, 569.1600000000001, 1678.08, 1706.8799999999999], [7, 450.36, 669.6, 449.28, 487.68], [7, 500.04, 623.1600000000001, 499.2, 535.68], [7, 183.60000000000002, 222.48000000000002, 529.92, 552.96], [7, 294.84000000000003, 594.0, 533.76, 560.64], [7, 182.52, 912.6, 566.4, 606.72], [7, 180.36, 584.2800000000001, 600.9599999999999, 633.6], [7, 177.12, 457.92, 633.6, 664.3199999999999], [7, 174.96, 926.6400000000001, 668.16, 706.56], [7, 170.64000000000001, 946.08, 700.8, 739.1999999999999], [7, 167.4, 948.24, 731.52, 769.92], [7, 164.16000000000003, 358.56, 764.16, 791.04], [7, 159.84, 935.2800000000001, 798.72, 835.1999999999999], [7, 156.60000000000002, 238.68, 831.36, 856.3199999999999], [7, 152.28, 938.5200000000001, 865.92, 902.4], [7, 150.12, 518.4000000000001, 898.56, 929.28], [7, 145.8, 941.7600000000001, 935.04, 973.4399999999999], [7, 143.64000000000001, 811.08, 969.5999999999999, 1006.0799999999999], [7, 139.32000000000002, 954.72, 1008.0, 1048.32], [7, 136.08, 967.6800000000001, 1042.56, 1084.8], [7, 131.76000000000002, 660.96, 1080.96, 1115.52], [7, 126.36000000000001, 541.08, 1119.36, 1153.9199999999998], [7, 122.04, 692.2800000000001, 1159.68, 1198.08], [7, 115.56, 943.9200000000001, 1198.08, 1248.0], [7, 111.24000000000001, 976.32, 1238.3999999999999, 1292.1599999999999], [7, 105.84, 984.96, 1280.6399999999999, 1336.32], [7, 99.36000000000001, 670.6800000000001, 1320.96, 1367.04], [7, 91.80000000000001, 415.8, 1363.2, 1399.6799999999998], [7, 85.32000000000001, 806.7600000000001, 1405.44, 1459.2], [7, 76.68, 494.64000000000004, 1447.6799999999998, 1493.76], [7, 479.52000000000004, 569.1600000000001, 1511.04, 1541.76], [7, 56.160000000000004, 942.84, 1537.9199999999998, 1607.04], [7, 45.36, 1021.6800000000001, 1584.0, 1658.8799999999999], [7, 478.44000000000005, 552.96, 1699.2, 1729.9199999999998], [8, 451.44000000000005, 686.88, 362.88, 410.88], [8, 503.28000000000003, 637.2, 418.56, 460.79999999999995], [8, 162.0, 205.20000000000002, 447.35999999999996, 470.4], [8, 280.8, 626.4000000000001, 455.03999999999996, 487.68], [8, 162.0, 206.28, 485.76, 508.79999999999995], [8, 524.88, 602.64, 539.52, 566.4], [8, 154.44, 963.36, 558.72, 620.16], [8, 150.12, 828.36, 593.28, 648.9599999999999], [8, 549.72, 637.2, 683.52, 708.48], [8, 548.64, 637.2, 718.0799999999999, 743.04], [8, 637.2, 820.8000000000001, 756.48, 783.36], [8, 635.0400000000001, 918.0000000000001, 791.04, 819.8399999999999], [8, 633.96, 740.88, 827.52, 852.48], [8, 777.6, 937.44, 883.1999999999999, 908.16], [8, 721.44, 937.44, 921.5999999999999, 950.4]]
2026-08-10 18:58:25,245 INFO     29 [qwen-vl-text] ═══ DONE ═══ 128 positions, pages=4, time=132.0s
2026-08-10 18:58:25,245 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:58:25,250 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:58:25,250 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 18:58:25,250 INFO     29 [qwen-vl-text] positions(62): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:58:25,250 INFO     29 [qwen-vl-text] page grouping: [10, 11], lines per page: [41, 21]
2026-08-10 18:58:25,460 INFO     29 [qwen-vl-text] page=10, rect=810x1440, img=(2250x4000), dpi=200
2026-08-10 18:58:25,637 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2020-09-23"}
```
2026-08-10 18:58:25,637 INFO     29 [qwen-vl-text] page=11, rect=810x1440, img=(2250x4000), dpi=200
2026-08-10 18:58:25,639 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1400
2026-08-10 18:58:25,639 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:58:25,640 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 378, \"bbox_end\": 439, \"encounter_dates\": [\"2025-07-03\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "郑州大学第一附属医院\nThe First Affiliated Hospital of Zhengzhou University\n入院记录\n姓名：\n性别：女\n年龄：67岁\n住院号：100\n无外伤、输血史，无食物、药物过敏史。\n个人史：生于河南省新乡市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿\n山、高氟区、低碘区居住史，无化学性物质、放射性物质、有毒物质接触史，无吸毒史，无\n吸烟、饮酒史，否认冶游史。\n婚姻史：己婚，20岁结婚，爱人体健，夫妻关系和睦，有2子，1女。\n月经生育史：初潮14岁 周期28天 每次持续5天 52岁，月经周期规则，月经量中等，颜色正常，无血\n块、无痛经；\n家族史：父母体健。同胞4人，健康状况良好，无与患者类似疾病，无家族性遗传病\n史。\n体格检查\n体温\n脉搏86次/分\n呼吸19次/分\n血压105/74mmHg\n36.50℃\n身高165cm\n体重62.0kg\n发育正常，营养良好，体型匀称，神志清楚，自主体位，正常面容，表情自如，查体合\n作。全身皮肤黏膜无黄染，无皮疹、皮下出血、皮下结节、瘢痕，无肝掌、蜘蛛痣。全身浅\n表淋巴结未触及。角膜无云翳、白斑、软化、溃疡、瘢痕、反射、色素环。双眼瞳孔等大等\n圆，直径3mm，对光反射灵敏，调节反射正常。口唇黏膜无斑疹、溃疡、出血点。软硬腭位\n置居中。扁桃体无肿大，声音正常。颈软、无抵抗。颈动脉搏动正常、颈静脉无怒张。气管\n居中。肝颈静脉回流征阴性。甲状腺无肿大、无压痛、震颤、血管杂音。胸廓对称，无局部\n隆起、塌陷、压痛，呼吸运动正常。乳房正常对称、无包块、红肿、压痛、左、右乳头无分\n泌物。胸壁无静脉曲张、皮下气肿。胸骨无叩痛。呼吸运动正常，肋间隙正常、语颤正常。\n无胸膜摩擦感，无皮下捻发感，双肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正\n常。心前区无隆起，心尖搏动正常，心浊音界正常，心前区无异常搏动，心率86次/分，律\n齐，心脉率一致，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，无腹壁静脉曲张、无\n胃肠型，无蠕动波，腹式呼吸存在。脐正常、无分泌物。腹部无压痛、反跳痛、腹部柔软、\n无包块。肝脏肋缘下未触及，脾脏肋缘下未触及，Murphy氏征阴性，左、右肾区无叩击痛，\n输尿管点无压痛，移动性浊音阴性，无液波震颤，肠鸣音正常、3次/分、无过水声、无肠鸣\n杂音。肛门及外生殖器拒绝。脊柱活动正常，无侧凸、前凸、后凸，棘突无压痛、叩击痛、\n四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾）、水肿。关节无红肿、疼痛、活动\n第2页\n郑州大学第一附属医院\nThe First Affiliated Hospital of Zhengzhou University\n入院记录\n姓名：\n性别：女\n年龄：57岁\n住院号：00\n积液、活动度受限、畸形，肌肉无萎缩。腹壁反射正常，肌张力正常，肌力V级，肢体无瘫\n痪，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski's sign阴性，\n双侧Hoffmann征阴性，Kernig's sign阴性。\n专科检查\n呼吸运动正常，肋间隙正常，语颤正常，无胸膜摩擦感，无皮下捻发感，叩诊清音，双\n肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正常。\n辅助检查\n暂无\n初步诊断：\n1.肺恶性肿瘤\n2.慢性乙型病毒性肝炎\n副主任医师：\n王欢\n2025年07月03日",
    "role": "user"
  }
]
2026-08-10 18:58:25,640 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=2020-09-23
2026-08-10 18:58:25,645 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:58:25.642+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:58:25,657 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3528127, prompt_len=401
2026-08-10 18:58:28,712 INFO     29 [qwen-vl-parser] text API response (len=615):
["分子病理基因检测报告单", "检测项目", "外显因子", "突变类型", "检测结果", "PIK3CA基因", "Exon-20", "H1047R", "野生型", "Exon-9", "E545K", "ALK融合基因", "ALK-Exon-20", "具体突变类型见附录", "野生型", "ROS1融合基因", "ROS1-Exon-32/34/35", "具体突变类型见附录", "野生型", "RET融合基因", "RET-Exon-12", "具体突变类型见附录", "野生型", "HER2基因", "Exon-20", "20-ins/G776>VC(1)", "野生型", "MET基因", "MET-Exon-14", "MET exon13;METexon15", "野生型", "备注：", "由于肿瘤存在异质性现象，此检测结果只针对本次样本有效。结果仅供临床参考", "，不可作为临床诊治的唯一依据。", "驱动基因突变状态是靶向药物治疗的重要疗效预测因子，EGFR和KRAS突变状态可", "以指导EGFR-TKIs的用药；ALK、ROS1基因融合突变及MET外显子14跳跃突变可以", "从ALK/ROS1/MET抑制剂中明显受益；BRAF基因突变患者可以从RAF抑制剂和MEK", "抑制剂中明显受益", "初诊医师：戚美", "复诊医师：刘龙", "报告日期：2020-09-23"]
2026-08-10 18:58:28,713 INFO     29 [qwen-vl-parser] page=13 text: 41 lines (bbox 467-507)
2026-08-10 18:58:28,713 INFO     29 [qwen-vl-parser] page=13 text: 41 sections
2026-08-10 18:58:28,960 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3755465, prompt_len=764
2026-08-10 18:58:29,916 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:58:29,916 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-10 18:58:29,931 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3755465, prompt_len=401
2026-08-10 18:58:31,605 INFO     29 Retrying request to /chat/completions in 0.909306 seconds
2026-08-10 18:58:34,273 INFO     29 [qwen-vl-parser] text API response (len=730):
["本报告仅供临床浏览，严禁私自打印。报告单以放射科室打印", "放射科CT报告单", "姓名", "性别 女", "年龄 63岁", "病人编", "检查编号 CT02901334", "门诊号", "检查日期 2026-03-10 09:33 报告日期 2026-03-10 12:07 病人来源 门诊", "检查方法及部位 胸部CT平扫,上腹部CT平扫", "检查所见:", "结合病史，右肺术后，局部见条片状高密度及点线状致密灶，右侧肺门结构", "紊乱，右侧肋骨术后态；右侧胸膜增厚，右膈略抬高。双肺见多发大小不等", "结节灶，部分呈磨玻璃密度，结节较大者位于左肺下叶IM32，为部分实性小", "结节，大小约1.4cm×1.0cm，可见分叶、胸膜凹陷征象；双肺纹理增多、紊", "乱，见纤维灶。左肺段以上支气管开口通畅，左肺门不大，纵隔内见增大淋", "巴结，大者最大短径约1.2cm。未见胸腔积液征象。冠状动脉钙化。双腋窝", "见小淋巴结。", "肝脏形态可，肝实质密度稍低，肝右叶见数个小圆形低密度灶，肝内另见", "斑点状高密度。肝内外胆管无扩张。胆囊不大，壁不厚，内未见高密度灶。", "胰腺未见明显异常。脾脏不大，质均匀。右肾盂肾盏轻度扩张；左肾及左肾", "窦见小类圆形低密度灶。双肾上腺未见明显异常。腹膜后未见肿大淋巴结。", "骨窗示局部腰椎变扁。", "检查结论:", "右肺术后，右肺纤维灶，右侧胸膜增厚", "双肺多发小结节，考虑双肺多发转移可能，较前2025-08-12CT增多、增", "大，请结合临床", "冠状动脉钙化", "提示轻度脂肪肝；肝内钙化灶；肝囊肿", "左肾囊肿；右肾轻度积水", "局部腰椎变扁"]
2026-08-10 18:58:34,274 INFO     29 [qwen-vl-parser] page=14 text: 31 lines (bbox 508-538)
2026-08-10 18:58:34,274 INFO     29 [qwen-vl-parser] page=14 text: 31 sections
2026-08-10 18:58:34,534 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3521363, prompt_len=764
2026-08-10 18:58:35,502 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-10"
}
```
2026-08-10 18:58:35,503 INFO     29 [qwen-vl-parser] page=15 classify=table report_date=2026-03-10
2026-08-10 18:58:35,526 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3521363, prompt_len=756
2026-08-10 18:58:44,296 INFO     29 [qwen-vl-parser] table API response (len=1698):
\begin{tabular}{llllllllll}
\hline
NO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 & \\
\hline
1 & *★白细胞 & WBC & 8.22 & & 3.5-9.5 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\
2 & 中性粒细胞比率 & NEU\% & 72.10 & & 40-75 & \% & XN9100 & 半导体激光器的流式细胞计数法 & \\
3 & 淋巴细胞比率 & LYM\% & 20.30 & & 20-50 & \% & XN9100 & 半导体激光器的流式细胞计数法 & \\
4 & 嗜酸性粒细胞比率 & EOS\% & 0.40 & & 0.4-8.0 & \% & XN9100 & 半导体激光器的流式细胞计数法 & \\
5 & 嗜碱性粒细胞比率 & BAS\% & 0.40 & & 0-1 & \% & XN9100 & 半导体激光器的流式细胞计数法 & \\
6 & 单核细胞比率 & MON\% & 6.80 & & 3-10 & \% & XN9100 & 半导体激光器的流式细胞计数法 & \\
7 & 中性粒细胞计数 & NEU\# & 5.93 & & 1.8-6.3 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\
8 & 淋巴细胞计数 & LYM\# & 1.67 & & 1.1-3.2 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\
9 & 嗜酸性粒细胞计数 & EOS\# & 0.03 & & 0.02-0.52 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\
10 & 嗜碱性粒细胞计数 & BAS\# & 0.03 & & 0-0.06 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\
11 & 单核细胞计数 & MON\# & 0.56 & & 0.1-0.6 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\
12 & *★红细胞 & RBC & 5.22 & 1 & 3.8-5.1 & 10^12/L & XN9100 & 液压聚焦（DC检测） & \\
13 & *★血红蛋白 & HGB & 147.0 & & 115-150 & g/L & XN9100 & SLS-血红蛋白法 & \\
14 & *★红细胞压积 & HCT & 44.90 & & 35.0-45.0 & \% & XN9100 & 脉冲信号累积法 & \\
15 & *平均红细胞体积 & MCV & 86.0 & & 82-100 & fL & XN9100 & 计算法 & \\
16 & *平均血红蛋白含量 & MCH & 28.2 & & 27-34 & pg & XN9100 & 计算法 & \\
17 & *平均血红蛋白浓度 & MCHC & 327.0 & & 316-354 & g/L & XN9100 & 计算法 & \\
18 & 红细胞平均宽度 & RDW & 12.6 & & 10-14.6 & \% & XN9100 & 直方图解析测量 & \\
19 & *★血小板计数 & PLT & 309 & & 125-350 & 10^9/L & XN9100 & 液压聚焦（DC检测） & \\
20 & 血小板平均宽度 & PDW & 8.30 & & 9-17 & fL & XN9100 & 直方图解析测量 & \\
21 & 平均血小板体积 & MPV & 8.30 & & 6-14 & fL & XN9100 & 计算法 & \\
22 & 血小板压积 & PCT & 0.260 & & 0.114-0.282 & \% & XN9100 & 脉冲信号累积法 & \\
\hline
\end{tabular}
2026-08-10 18:58:44,298 INFO     29 [qwen-vl-parser] page=15 table: 29 LaTeX lines (bbox 539-567)
2026-08-10 18:58:44,298 INFO     29 [qwen-vl-parser] page=15 table: 29 sections
2026-08-10 18:58:44,593 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3442802, prompt_len=764
2026-08-10 18:58:45,524 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-10"
}
```
2026-08-10 18:58:45,524 INFO     29 [qwen-vl-parser] page=16 classify=table report_date=2026-03-10
2026-08-10 18:58:45,546 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3442802, prompt_len=756
2026-08-10 18:58:57,867 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:58:57.864+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:58:59,374 INFO     29 [qwen-vl-parser] table API response (len=2544):
\begin{tabular}{llllllllll}
\hline
NO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 \\
\hline
1 & *★丙氨酸氨基转移酶 & ALT & 13 & & 7-40 & U/L & Roche\_3 & 速率法 \\
2 & *★天门冬氨酸氨基转移酶 & AST & 15 & & 13-35 & U/L & Roche\_3 & 速率法 \\
3 & 谷氨酸脱氢酶 & GLDH & 5.7 & & $<$7.4 & U/L & Roche\_3 & 速率法 \\
4 & *★γ-谷丙酰基转肽酶 & GGT & 15 & & 7-45 & U/L & Roche\_3 & 速率法 \\
5 & ★碱性磷酸酶 & AKP & 93 & & 50-135 & U/L & Roche\_3 & 速率法 \\
6 & 腺苷脱氨酶 & ADA & 8 & & 4-18 & U/L & Roche\_3 & 速率法 \\
7 & *★总胆红素 & TBIL & 8.2 & & 5.0-21.0 & $\mu$mol/L & Roche\_3 & 重氮法 \\
8 & *直接胆红素 & DBIL & 2.6 & & $<$6.0 & $\mu$mol/L & Roche\_3 & 重氮法 \\
9 & 间接胆红素 & IBIL & 5.6 & & 2.0-15.0 & $\mu$mol/L & & 计算 \\
10 & *前白蛋白 & PA & 30.2 & & 17.0-40.0 & mg/dl & Roche\_3 & 免疫比浊法 \\
11 & *★总蛋白 & TP & 75.4 & & 60.0-85.0 & g/L & Roche\_3 & 双缩脲法 \\
12 & *★白蛋白 & ALB & 48.6 & & 40.0-55.0 & g/L & Roche\_3 & 溴钾酚绿 \\
13 & 球蛋白 & GLB & 26.8 & & 20.0-40.0 & g/L & & 计算 \\
14 & 白/球比例 & A/G & 1.81 & & 1.2-2.4 & & & 计算 \\
15 & 总胆汁酸 & TBA & 1.3 & & $<$15.0 & $\mu$mol/L & Roche\_3 & 循环酶法 \\
16 & *★总胆固醇 & Cho & 7.28 & & 2.80-6.00 & mmol/L & Roche\_3 & 酶法 \\
17 & *★高密度脂蛋白胆固醇 & HDL-C & 1.78 & $\uparrow$ & 0.80-2.00 & mmol/L & Roche\_3 & 酶法 \\
18 & *★低密度脂蛋白胆固醇 & LDL-C & 4.89 & $\uparrow$ & 1.00-3.37 & mmol/L & Roche\_3 & 酶法 \\
19 & 小而密低密度脂蛋白 & sdLDL & 2.01 & $\uparrow$ & 0.25-1.17 & mmol/L & Roche\_3 & 酶法 \\
20 & *血清载脂蛋白A1 & APOA1 & 1.96 & $\uparrow$ & 1.00-1.60 & g/L & Roche\_3 & 免疫比浊法 \\
21 & *血清载脂蛋白B & APOB & 1.53 & $\uparrow$ & 0.60-1.00 & g/L & Roche\_3 & 免疫比浊法 \\
22 & *★甘油三酯 & TG & 2.30 & $\uparrow$ & 0.30-1.70 & mmol/L & Roche\_3 & 酶法 \\
23 & 脂蛋白a & LP(a) & 9.70 & & $<$75.00 & nmol/L & Roche\_3 & 免疫比浊法 \\
24 & 游离脂肪酸 & NEFA & 125.0 & $\uparrow$ & 10.0-85.0 & umol/dl & Roche\_3 & 酶法 \\
25 & 脂蛋白磷脂酶A2 & PLA2 & 728 & $\uparrow$ & $<$659 & U/L & Roche\_3 & 酶法 \\
26 & *★尿素 & Urea & 3.59 & & 2.30-7.80 & mmol/L & Roche\_3 & 酶法 \\
27 & *★肌酐 & Cr & 38 & $\downarrow$ & 53-97 & $\mu$mol/L & Roche\_3 & 酶法 \\
28 & *胱抑素C & Cys-C & 0.76 & & 0.51-1.09 & mg/L & Roche\_3 & 免疫比浊法 \\
29 & 肾小球滤过率 & eGFR & 108.600 & & & ml/min & Roche\_3 & 计算 \\
30 & *★钾 & K & 4.23 & & 3.50-5.30 & mmol/L & Roche\_3 & 离子选择电极 \\
31 & *★钠 & NA & 139 & & 137-147 & mmol/L & Roche\_3 & 离子选择电极法 \\
32 & *★氯 & CL & 104 & & 99-110 & mmol/L & Roche\_3 & 离子选择电极法 \\
33 & 二氧化碳结合力 & CO2 & 21.5 & & 18.0-28.0 & mmol/L & Roche\_3 & 酶法 \\
34 & *★钙 & Ca & 2.36 & & 2.11-2.52 & mmol/L & Roche\_3 & 比色法 \\
35 & ★磷 & P & 1.21 & & 0.60-1.60 & mmol/L & Roche\_3 & 比色法 \\
36 & *镁 & Mg & 0.86 & & 0.65-1.10 & mmol/L & Roche\_3 & 比色法 \\
\hline
\end{tabular}
2026-08-10 18:58:59,376 INFO     29 [qwen-vl-parser] page=16 table: 43 LaTeX lines (bbox 568-610)
2026-08-10 18:58:59,376 INFO     29 [qwen-vl-parser] page=16 table: 43 sections
2026-08-10 18:58:59,706 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3527398, prompt_len=764
2026-08-10 18:59:00,042 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:59:00,042 INFO     29 [qwen-vl-text] LLM output (len=1994):
{
  "encounter_date": "2025-07-03",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 67,
  "dm_ethnicity": null,
  "dm_marital_status": "已婚",
  "dm_occupation": null,
  "dm_admission_time": null,
  "dm_record_time": "2025-07-03",
  "dm_history_provider": null,
  "cc_text": null,
  "cc_main_symptoms": [],
  "cc_duration": null,
  "pi_text": null,
  "pmh_disease_history": [
    "慢性乙型病毒性肝炎"
  ],
  "pmh_allergy_history": [
    "无食物、药物过敏史"
  ],
  "pmh_surgery_trauma_history": [
    "无外伤、输血史"
  ],
  "ph_smoking": "无吸烟史",
  "ph_drinking": "无饮酒史",
  "oh_menarche_age": 14,
  "oh_menopause_age": 52,
  "oh_pregnancies": "有2子，1女",
  "fh_text": "父母体健。同胞4人，健康状况良好，无与患者类似疾病，无家族性遗传病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 86,
  "vs_respiration_rpm": 19,
  "vs_systolic_bp_mmhg": 105,
  "vs_diastolic_bp_mmhg": 74,
  "pe_general_condition": "发育正常，营养良好，体型匀称，神志清楚，自主体位，正常面容，表情自如，查体合作。",
  "pe_skin_mucosa": "全身皮肤黏膜无黄染，无皮疹、皮下出血、皮下结节、瘢痕，无肝掌、蜘蛛痣。",
  "pe_lymph_nodes": "全身浅表淋巴结未触及。",
  "pe_lungs": "胸廓对称，无局部隆起、塌陷、压痛，呼吸运动正常。呼吸运动正常，肋间隙正常、语颤正常。无胸膜摩擦感，无皮下捻发感，双肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正常。",
  "pe_heart": "心前区无隆起，心尖搏动正常，心浊音界正常，心前区无异常搏动，心率86次/分，律齐，心脉率一致，各瓣膜听诊区未闻及杂音，无心包摩擦音。",
  "pe_abdomen": "腹平坦，无腹壁静脉曲张、无胃肠型，无蠕动波，腹式呼吸存在。脐正常、无分泌物。腹部无压痛、反跳痛、腹部柔软、无包块。肝脏肋缘下未触及，脾脏肋缘下未触及，Murphy氏征阴性，左、右肾区无叩击痛，输尿管点无压痛，移动性浊音阴性，无液波震颤，肠鸣音正常、3次/分、无过水声、无肠鸣杂音。",
  "pe_extremities": "四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾）、水肿。关节无红肿、疼痛、活动积液、活动度受限、畸形，肌肉无萎缩。",
  "pe_nervous_system": "脊柱活动正常，无侧凸、前凸、后凸，棘突无压痛、叩击痛。腹壁反射正常，肌张力正常，肌力V级，肢体无瘫痪，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski's sign阴性，双侧Hoffmann征阴性，Kernig's sign阴性。",
  "pe_specialist_exam": "呼吸运动正常，肋间隙正常，语颤正常，无胸膜摩擦感，无皮下捻发感，叩诊清音，双肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正常。",
  "pe_ecog_score": null,
  "pat_text": "暂无",
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "肺恶性肿瘤",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "慢性乙型病毒性肝炎",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 18:59:00,042 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-03]
2026-08-10 18:59:00,044 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1139668, prompt_len=1795
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共41行）
["郑州大学第一附属医院", "The First Affiliated Hospital of Zhengzhou University", "入院记录", "姓名：", "性别：女", "年龄：67岁", "住院号：100", "无外伤、输血史，无食物、药物过敏史。", "个人史：生于河南省新乡市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿", "山、高氟区、低碘区居住史，无化学性物质、放射性物质、有毒物质接触史，无吸毒史，无", "吸烟、饮酒史，否认冶游史。", "婚姻史：己婚，20岁结婚，爱人体健，夫妻关系和睦，有2子，1女。", "月经生育史：初潮14岁 周期28天 每次持续5天 52岁，月经周期规则，月经量中等，颜色正常，无血", "块、无痛经；", "家族史：父母体健。同胞4人，健康状况良好，无与患者类似疾病，无家族性遗传病", "史。", "体格检查", "体温", "脉搏86次/分", "呼吸19次/分", "血压105/74mmHg", "36.50℃", "身高165cm", "体重62.0kg", "发育正常，营养良好，体型匀称，神志清楚，自主体位，正常面容，表情自如，查体合", "作。全身皮肤黏膜无黄染，无皮疹、皮下出血、皮下结节、瘢痕，无肝掌、蜘蛛痣。全身浅", "表淋巴结未触及。角膜无云翳、白斑、软化、溃疡、瘢痕、反射、色素环。双眼瞳孔等大等", "圆，直径3mm，对光反射灵敏，调节反射正常。口唇黏膜无斑疹、溃疡、出血点。软硬腭位", "置居中。扁桃体无肿大，声音正常。颈软、无抵抗。颈动脉搏动正常、颈静脉无怒张。气管", "居中。肝颈静脉回流征阴性。甲状腺无肿大、无压痛、震颤、血管杂音。胸廓对称，无局部", "隆起、塌陷、压痛，呼吸运动正常。乳房正常对称、无包块、红肿、压痛、左、右乳头无分", "泌物。胸壁无静脉曲张、皮下气肿。胸骨无叩痛。呼吸运动正常，肋间隙正常、语颤正常。", "无胸膜摩擦感，无皮下捻发感，双肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正", "常。心前区无隆起，心尖搏动正常，心浊音界正常，心前区无异常搏动，心率86次/分，律", "齐，心脉率一致，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，无腹壁静脉曲张、无", "胃肠型，无蠕动波，腹式呼吸存在。脐正常、无分泌物。腹部无压痛、反跳痛、腹部柔软、", "无包块。肝脏肋缘下未触及，脾脏肋缘下未触及，Murphy氏征阴性，左、右肾区无叩击痛，", "输尿管点无压痛，移动性浊音阴性，无液波震颤，肠鸣音正常、3次/分、无过水声、无肠鸣", "杂音。肛门及外生殖器拒绝。脊柱活动正常，无侧凸、前凸、后凸，棘突无压痛、叩击痛、", "四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾）、水肿。关节无红肿、疼痛、活动", "第2页"]

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
2026-08-10 18:59:00,713 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-10"
}
```
2026-08-10 18:59:00,714 INFO     29 [qwen-vl-parser] page=17 classify=table report_date=2026-03-10
2026-08-10 18:59:00,732 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3527398, prompt_len=756
2026-08-10 18:59:05,341 INFO     29 [qwen-vl-parser] table API response (len=404):
\begin{tabular}{llllllllll}
\hline
NO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 \\
\hline
1 & *★甲胎蛋白 & AFP & 3.41 & & 0.00-7.00 & ng/ml & Roche\_4 & 电化学发光 \\
2 & *★癌胚抗原 & CEA & 3.52 & & 0.00-5.00 & ng/ml & Roche\_4 & 电化学发光 \\
3 & 非小细胞肺癌相关抗原 & CYFRA21-1 & 1.70 & & 0.00-3.30 & ng/ml & Roche\_4 & 电化学发光 \\
4 & 神经元特异性烯醇化酶 & NSE & 16.60 & 1 & 0.00-16.30 & ng/ml & Roche\_4 & 电化学发光 \\
\hline
\end{tabular}
2026-08-10 18:59:05,342 INFO     29 [qwen-vl-parser] page=17 table: 11 LaTeX lines (bbox 611-621)
2026-08-10 18:59:05,342 INFO     29 [qwen-vl-parser] page=17 table: 11 sections
2026-08-10 18:59:05,363 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=45963, prompt_len=764
2026-08-10 18:59:05,978 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 18:59:05,978 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=None
2026-08-10 18:59:05,987 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=45963, prompt_len=401
2026-08-10 18:59:06,896 INFO     29 [qwen-vl-parser] text API response (len=100):
["20200831手术 术后病理肺腺癌", "20201016~20210118培美+卡铂5周期", "20230931~20231226培美+卡铂+贝伐5周期", "20240119培美+卡铂"]
2026-08-10 18:59:06,897 INFO     29 [qwen-vl-parser] page=18 text: 4 lines (bbox 622-625)
2026-08-10 18:59:06,897 INFO     29 [qwen-vl-parser] page=18 text: 4 sections
2026-08-10 18:59:06,897 INFO     29 [qwen-vl-parser] parse_pdf done: 626 sections from 18 pages.
2026-08-10 18:59:06,903 INFO     29 Close text detector.
2026-08-10 18:59:07,328 INFO     29 Close text recognizer.
2026-08-10 18:59:07,737 INFO     29 Close recognizer.
2026-08-10 18:59:08,120 INFO     29 Close recognizer.
2026-08-10 18:59:18,050 INFO     29 [qwen-vl-text] coord API raw response (len=2840):
[
	{"text": "郑州大学第一附属医院", "bbox": [164, 34, 410, 55]},
	{"text": "The First Affiliated Hospital of Zhengzhou University", "bbox": [164, 53, 414, 64]},
	{"text": "入院记录", "bbox": [431, 72, 584, 92]},
	{"text": "姓名：", "bbox": [103, 108, 150, 121]},
	{"text": "性别：女", "bbox": [311, 103, 385, 116]},
	{"text": "年龄：67岁", "bbox": [520, 98, 612, 111]},
	{"text": "住院号：100", "bbox": [736, 93, 841, 107]},
	{"text": "无外伤、输血史，无食物、药物过敏史。", "bbox": [97, 121, 455, 141]},
	{"text": "个人史：生于河南省新乡市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿", "bbox": [138, 134, 900, 164]},
	{"text": "山、高氟区、低碘区居住史，无化学性物质、放射性物质、有毒物质接触史，无吸毒史，无", "bbox": [99, 154, 946, 187]},
	{"text": "吸烟、饮酒史，否认冶游史。", "bbox": [99, 190, 354, 208]},
	{"text": "婚姻史：己婚，20岁结婚，爱人体健，夫妻关系和睦，有2子，1女。", "bbox": [140, 204, 755, 231]},
	{"text": "月经生育史：初潮14岁 周期28天 每次持续5天 52岁，月经周期规则，月经量中等，颜色正常，无血", "bbox": [142, 240, 934, 268]},
	{"text": "块、无痛经；", "bbox": [100, 283, 208, 297]},
	{"text": "家族史：父母体健。同胞4人，健康状况良好，无与患者类似疾病，无家族性遗传病", "bbox": [140, 294, 916, 318]},
	{"text": "史。", "bbox": [100, 328, 128, 341]},
	{"text": "体格检查", "bbox": [431, 343, 582, 358]},
	{"text": "体温", "bbox": [146, 369, 187, 382]},
	{"text": "脉搏86次/分", "bbox": [294, 367, 409, 381]},
	{"text": "呼吸19次/分", "bbox": [458, 366, 575, 379]},
	{"text": "血压105/74mmHg", "bbox": [652, 364, 805, 378]},
	{"text": "36.50℃", "bbox": [103, 392, 175, 404]},
	{"text": "身高165cm", "bbox": [143, 412, 237, 425]},
	{"text": "体重62.0kg", "bbox": [288, 411, 394, 425]},
	{"text": "发育正常，营养良好，体型匀称，神志清楚，自主体位，正常面容，表情自如，查体合", "bbox": [134, 432, 955, 448]},
	{"text": "作。全身皮肤黏膜无黄染，无皮疹、皮下出血、皮下结节、瘢痕，无肝掌、蜘蛛痣。全身浅", "bbox": [84, 454, 955, 471]},
	{"text": "表淋巴结未触及。角膜无云翳、白斑、软化、溃疡、瘢痕、反射、色素环。双眼瞳孔等大等", "bbox": [82, 476, 955, 493]},
	{"text": "圆，直径3mm，对光反射灵敏，调节反射正常。口唇黏膜无斑疹、溃疡、出血点。软硬腭位", "bbox": [78, 498, 944, 516]},
	{"text": "置居中。扁桃体无肿大，声音正常。颈软、无抵抗。颈动脉搏动正常、颈静脉无怒张。气管", "bbox": [74, 520, 957, 538]},
	{"text": "居中。肝颈静脉回流征阴性。甲状腺无肿大、无压痛、震颤、血管杂音。胸廓对称，无局部", "bbox": [70, 543, 960, 561]},
	{"text": "隆起、塌陷、压痛，呼吸运动正常。乳房正常对称、无包块、红肿、压痛、左、右乳头无分", "bbox": [66, 566, 960, 585]},
	{"text": "泌物。胸壁无静脉曲张、皮下气肿。胸骨无叩痛。呼吸运动正常，肋间隙正常、语颤正常。", "bbox": [63, 589, 945, 608]},
	{"text": "无胸膜摩擦感，无皮下捻发感，双肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正", "bbox": [60, 612, 964, 633]},
	{"text": "常。心前区无隆起，心尖搏动正常，心浊音界正常，心前区无异常搏动，心率86次/分，律", "bbox": [57, 636, 955, 657]},
	{"text": "齐，心脉率一致，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，无腹壁静脉曲张、无", "bbox": [51, 661, 971, 685]},
	{"text": "胃肠型，无蠕动波，腹式呼吸存在。脐正常、无分泌物。腹部无压痛、反跳痛、腹部柔软、", "bbox": [50, 687, 958, 712]},
	{"text": "无包块。肝脏肋缘下未触及，脾脏肋缘下未触及，Murphy氏征阴性，左、右肾区无叩击痛，", "bbox": [44, 712, 957, 738]},
	{"text": "输尿管点无压痛，移动性浊音阴性，无液波震颤，肠鸣音正常、3次/分、无过水声、无肠鸣", "bbox": [39, 738, 975, 765]},
	{"text": "杂音。肛门及外生殖器拒绝。脊柱活动正常，无侧凸、前凸、后凸，棘突无压痛、叩击痛、", "bbox": [36, 764, 962, 791]},
	{"text": "四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾）、水肿。关节无红肿、疼痛、活动", "bbox": [30, 790, 962, 818]},
	{"text": "第2页", "bbox": [467, 829, 538, 843]}
]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord API: raw_items=41, valid_items=41, elapsed=18.0s
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[0]: text=郑州大学第一附属医院, bbox=[164, 34, 410, 55]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[1]: text=The First Affiliated Hospital of Zhengzhou University, bbox=[164, 53, 414, 64]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[2]: text=入院记录, bbox=[431, 72, 584, 92]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[103, 108, 150, 121]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[311, 103, 385, 116]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：67岁, bbox=[520, 98, 612, 111]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[6]: text=住院号：100, bbox=[736, 93, 841, 107]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[7]: text=无外伤、输血史，无食物、药物过敏史。, bbox=[97, 121, 455, 141]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[8]: text=个人史：生于河南省新乡市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿, bbox=[138, 134, 900, 164]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[9]: text=山、高氟区、低碘区居住史，无化学性物质、放射性物质、有毒物质接触史，无吸毒史，无, bbox=[99, 154, 946, 187]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[10]: text=吸烟、饮酒史，否认冶游史。, bbox=[99, 190, 354, 208]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[11]: text=婚姻史：己婚，20岁结婚，爱人体健，夫妻关系和睦，有2子，1女。, bbox=[140, 204, 755, 231]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[12]: text=月经生育史：初潮14岁 周期28天 每次持续5天 52岁，月经周期规则，月经量中等，颜色正常，无血, bbox=[142, 240, 934, 268]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[13]: text=块、无痛经；, bbox=[100, 283, 208, 297]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[14]: text=家族史：父母体健。同胞4人，健康状况良好，无与患者类似疾病，无家族性遗传病, bbox=[140, 294, 916, 318]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[15]: text=史。, bbox=[100, 328, 128, 341]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[16]: text=体格检查, bbox=[431, 343, 582, 358]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[17]: text=体温, bbox=[146, 369, 187, 382]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[18]: text=脉搏86次/分, bbox=[294, 367, 409, 381]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[19]: text=呼吸19次/分, bbox=[458, 366, 575, 379]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[20]: text=血压105/74mmHg, bbox=[652, 364, 805, 378]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[21]: text=36.50℃, bbox=[103, 392, 175, 404]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[22]: text=身高165cm, bbox=[143, 412, 237, 425]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[23]: text=体重62.0kg, bbox=[288, 411, 394, 425]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[24]: text=发育正常，营养良好，体型匀称，神志清楚，自主体位，正常面容，表情自如，查体合, bbox=[134, 432, 955, 448]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[25]: text=作。全身皮肤黏膜无黄染，无皮疹、皮下出血、皮下结节、瘢痕，无肝掌、蜘蛛痣。全身浅, bbox=[84, 454, 955, 471]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[26]: text=表淋巴结未触及。角膜无云翳、白斑、软化、溃疡、瘢痕、反射、色素环。双眼瞳孔等大等, bbox=[82, 476, 955, 493]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[27]: text=圆，直径3mm，对光反射灵敏，调节反射正常。口唇黏膜无斑疹、溃疡、出血点。软硬腭位, bbox=[78, 498, 944, 516]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[28]: text=置居中。扁桃体无肿大，声音正常。颈软、无抵抗。颈动脉搏动正常、颈静脉无怒张。气管, bbox=[74, 520, 957, 538]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[29]: text=居中。肝颈静脉回流征阴性。甲状腺无肿大、无压痛、震颤、血管杂音。胸廓对称，无局部, bbox=[70, 543, 960, 561]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[30]: text=隆起、塌陷、压痛，呼吸运动正常。乳房正常对称、无包块、红肿、压痛、左、右乳头无分, bbox=[66, 566, 960, 585]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[31]: text=泌物。胸壁无静脉曲张、皮下气肿。胸骨无叩痛。呼吸运动正常，肋间隙正常、语颤正常。, bbox=[63, 589, 945, 608]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[32]: text=无胸膜摩擦感，无皮下捻发感，双肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正, bbox=[60, 612, 964, 633]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[33]: text=常。心前区无隆起，心尖搏动正常，心浊音界正常，心前区无异常搏动，心率86次/分，律, bbox=[57, 636, 955, 657]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[34]: text=齐，心脉率一致，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，无腹壁静脉曲张、无, bbox=[51, 661, 971, 685]
2026-08-10 18:59:18,051 INFO     29 [qwen-vl-text] coord item[35]: text=胃肠型，无蠕动波，腹式呼吸存在。脐正常、无分泌物。腹部无压痛、反跳痛、腹部柔软、, bbox=[50, 687, 958, 712]
2026-08-10 18:59:18,052 INFO     29 [qwen-vl-text] coord item[36]: text=无包块。肝脏肋缘下未触及，脾脏肋缘下未触及，Murphy氏征阴性，左、右肾区无叩击痛，, bbox=[44, 712, 957, 738]
2026-08-10 18:59:18,052 INFO     29 [qwen-vl-text] coord item[37]: text=输尿管点无压痛，移动性浊音阴性，无液波震颤，肠鸣音正常、3次/分、无过水声、无肠鸣, bbox=[39, 738, 975, 765]
2026-08-10 18:59:18,052 INFO     29 [qwen-vl-text] coord item[38]: text=杂音。肛门及外生殖器拒绝。脊柱活动正常，无侧凸、前凸、后凸，棘突无压痛、叩击痛、, bbox=[36, 764, 962, 791]
2026-08-10 18:59:18,052 INFO     29 [qwen-vl-text] coord item[39]: text=四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾）、水肿。关节无红肿、疼痛、活动, bbox=[30, 790, 962, 818]
2026-08-10 18:59:18,052 INFO     29 [qwen-vl-text] coord item[40]: text=第2页, bbox=[467, 829, 538, 843]
2026-08-10 18:59:18,052 INFO     29 [qwen-vl-text] page=10 — 41/41 coords, api_time=18.0s
2026-08-10 18:59:18,053 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=786688, prompt_len=1016
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["郑州大学第一附属医院", "The First Affiliated Hospital of Zhengzhou University", "入院记录", "姓名：", "性别：女", "年龄：57岁", "住院号：00", "积液、活动度受限、畸形，肌肉无萎缩。腹壁反射正常，肌张力正常，肌力V级，肢体无瘫", "痪，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski's sign阴性，", "双侧Hoffmann征阴性，Kernig's sign阴性。", "专科检查", "呼吸运动正常，肋间隙正常，语颤正常，无胸膜摩擦感，无皮下捻发感，叩诊清音，双", "肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正常。", "辅助检查", "暂无", "初步诊断：", "1.肺恶性肿瘤", "2.慢性乙型病毒性肝炎", "副主任医师：", "王欢", "2025年07月03日"]

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
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord API raw response (len=1262):
[
	{"text": "郑州大学第一附属医院", "bbox": [142, 250, 392, 271]},
	{"text": "The First Affiliated Hospital of Zhengzhou University", "bbox": [142, 267, 395, 278]},
	{"text": "入院记录", "bbox": [412, 285, 569, 305]},
	{"text": "姓名：", "bbox": [78, 321, 125, 334]},
	{"text": "性别：女", "bbox": [291, 316, 367, 329]},
	{"text": "年龄：57岁", "bbox": [504, 309, 599, 323]},
	{"text": "住院号：00", "bbox": [722, 303, 820, 317]},
	{"text": "积液、活动度受限、畸形，肌肉无萎缩。腹壁反射正常，肌张力正常，肌力V级，肢体无瘫", "bbox": [70, 320, 937, 355]},
	{"text": "痪，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski's sign阴性，", "bbox": [70, 342, 915, 378]},
	{"text": "双侧Hoffmann征阴性，Kernig's sign阴性。", "bbox": [71, 377, 475, 400]},
	{"text": "专科检查", "bbox": [417, 397, 572, 413]},
	{"text": "呼吸运动正常，肋间隙正常，语颤正常，无胸膜摩擦感，无皮下捻发感，叩诊清音，双", "bbox": [113, 409, 948, 444]},
	{"text": "肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正常。", "bbox": [70, 440, 643, 467]},
	{"text": "辅助检查", "bbox": [417, 465, 575, 481]},
	{"text": "暂无", "bbox": [112, 498, 154, 511]},
	{"text": "初步诊断：", "bbox": [414, 513, 513, 528]},
	{"text": "1.肺恶性肿瘤", "bbox": [460, 535, 592, 551]},
	{"text": "2.慢性乙型病毒性肝炎", "bbox": [460, 557, 687, 574]},
	{"text": "副主任医师：", "bbox": [698, 602, 824, 617]},
	{"text": "王欢", "bbox": [838, 582, 937, 617]},
	{"text": "2025年07月03日", "bbox": [794, 629, 960, 644]}
]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=11.0s
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[0]: text=郑州大学第一附属医院, bbox=[142, 250, 392, 271]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[1]: text=The First Affiliated Hospital of Zhengzhou University, bbox=[142, 267, 395, 278]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[2]: text=入院记录, bbox=[412, 285, 569, 305]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[78, 321, 125, 334]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[291, 316, 367, 329]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：57岁, bbox=[504, 309, 599, 323]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[6]: text=住院号：00, bbox=[722, 303, 820, 317]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[7]: text=积液、活动度受限、畸形，肌肉无萎缩。腹壁反射正常，肌张力正常，肌力V级，肢体无瘫, bbox=[70, 320, 937, 355]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[8]: text=痪，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski's sign阴性，, bbox=[70, 342, 915, 378]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[9]: text=双侧Hoffmann征阴性，Kernig's sign阴性。, bbox=[71, 377, 475, 400]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[10]: text=专科检查, bbox=[417, 397, 572, 413]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[11]: text=呼吸运动正常，肋间隙正常，语颤正常，无胸膜摩擦感，无皮下捻发感，叩诊清音，双, bbox=[113, 409, 948, 444]
2026-08-10 18:59:29,048 INFO     29 [qwen-vl-text] coord item[12]: text=肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正常。, bbox=[70, 440, 643, 467]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] coord item[13]: text=辅助检查, bbox=[417, 465, 575, 481]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] coord item[14]: text=暂无, bbox=[112, 498, 154, 511]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断：, bbox=[414, 513, 513, 528]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] coord item[16]: text=1.肺恶性肿瘤, bbox=[460, 535, 592, 551]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] coord item[17]: text=2.慢性乙型病毒性肝炎, bbox=[460, 557, 687, 574]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] coord item[18]: text=副主任医师：, bbox=[698, 602, 824, 617]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] coord item[19]: text=王欢, bbox=[838, 582, 937, 617]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] coord item[20]: text=2025年07月03日, bbox=[794, 629, 960, 644]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] page=11 — 21/21 coords, api_time=11.0s
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] new_positions (62):
[[10, 132.84, 332.1, 48.96, 79.2], [10, 132.84, 335.34000000000003, 76.32, 92.16], [10, 349.11, 473.04, 103.67999999999999, 132.48], [10, 83.43, 121.50000000000001, 155.51999999999998, 174.23999999999998], [10, 251.91000000000003, 311.85, 148.32, 167.04], [10, 421.20000000000005, 495.72, 141.12, 159.84], [10, 596.1600000000001, 681.21, 133.92, 154.07999999999998], [10, 78.57000000000001, 368.55, 174.23999999999998, 203.04], [10, 111.78, 729.0, 192.95999999999998, 236.16], [10, 80.19000000000001, 766.2600000000001, 221.76, 269.28], [10, 80.19000000000001, 286.74, 273.59999999999997, 299.52], [10, 113.4, 611.5500000000001, 293.76, 332.64], [10, 115.02000000000001, 756.5400000000001, 345.59999999999997, 385.91999999999996], [10, 81.0, 168.48000000000002, 407.52, 427.68], [10, 113.4, 741.96, 423.35999999999996, 457.91999999999996], [10, 81.0, 103.68, 472.32, 491.03999999999996], [10, 349.11, 471.42, 493.91999999999996, 515.52], [10, 118.26, 151.47, 531.36, 550.0799999999999], [10, 238.14000000000001, 331.29, 528.48, 548.64], [10, 370.98, 465.75000000000006, 527.04, 545.76], [10, 528.12, 652.0500000000001, 524.16, 544.3199999999999], [10, 83.43, 141.75, 564.48, 581.76], [10, 115.83000000000001, 191.97, 593.28, 612.0], [10, 233.28000000000003, 319.14000000000004, 591.84, 612.0], [10, 108.54, 773.5500000000001, 622.0799999999999, 645.12], [10, 68.04, 773.5500000000001, 653.76, 678.24], [10, 66.42, 773.5500000000001, 685.4399999999999, 709.92], [10, 63.18000000000001, 764.6400000000001, 717.12, 743.04], [10, 59.940000000000005, 775.1700000000001, 748.8, 774.72], [10, 56.7, 777.6, 781.92, 807.8399999999999], [10, 53.46, 777.6, 815.04, 842.4], [10, 51.03, 765.45, 848.16, 875.52], [10, 48.6, 780.84, 881.28, 911.52], [10, 46.17, 773.5500000000001, 915.8399999999999, 946.0799999999999], [10, 41.31, 786.5100000000001, 951.8399999999999, 986.4], [10, 40.5, 775.98, 989.28, 1025.28], [10, 35.64, 775.1700000000001, 1025.28, 1062.72], [10, 31.590000000000003, 789.75, 1062.72, 1101.6], [10, 29.160000000000004, 779.22, 1100.1599999999999, 1139.04], [10, 24.3, 779.22, 1137.6, 1177.9199999999998], [10, 378.27000000000004, 435.78000000000003, 1193.76, 1213.9199999999998], [11, 115.02000000000001, 317.52000000000004, 360.0, 390.24], [11, 115.02000000000001, 319.95000000000005, 384.47999999999996, 400.32], [11, 333.72, 460.89000000000004, 410.4, 439.2], [11, 63.18000000000001, 101.25, 462.24, 480.96], [11, 235.71, 297.27000000000004, 455.03999999999996, 473.76], [11, 408.24, 485.19000000000005, 444.96, 465.12], [11, 584.82, 664.2, 436.32, 456.47999999999996], [11, 56.7, 758.97, 460.79999999999995, 511.2], [11, 56.7, 741.1500000000001, 492.47999999999996, 544.3199999999999], [11, 57.510000000000005, 384.75, 542.88, 576.0], [11, 337.77000000000004, 463.32000000000005, 571.68, 594.72], [11, 91.53, 767.88, 588.9599999999999, 639.36], [11, 56.7, 520.83, 633.6, 672.48], [11, 337.77000000000004, 465.75000000000006, 669.6, 692.64], [11, 90.72, 124.74000000000001, 717.12, 735.8399999999999], [11, 335.34000000000003, 415.53000000000003, 738.72, 760.3199999999999], [11, 372.6, 479.52000000000004, 770.4, 793.4399999999999], [11, 372.6, 556.47, 802.0799999999999, 826.56], [11, 565.38, 667.44, 866.88, 888.48], [11, 678.7800000000001, 758.97, 838.0799999999999, 888.48], [11, 643.14, 777.6, 905.76, 927.36]]
2026-08-10 18:59:29,049 INFO     29 [qwen-vl-text] ═══ DONE ═══ 62 positions, pages=2, time=63.8s
2026-08-10 18:59:29,061 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 18:59:29,061 INFO     29 [Trace] task=ffaf4fc0 | doc=10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf | Extractor:Admission | outputs={"chunks": "2 items, types={'AdmissionRecord': 2}", "html": "", "json": "958 items", "markdown": "", "text": "", "name": "10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 2, \"chunks_LabExam\": 13}"}
2026-08-10 18:59:29,061 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 18:59:29,068 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:59:29,069 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:59:29,069 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:59:29,069 INFO     29 [qwen-vl-text] positions(18): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:59:29,069 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [18]
2026-08-10 18:59:29,406 INFO     29 [qwen-vl-text] page=0, rect=1080x1920, img=(3000x5334), dpi=200
2026-08-10 18:59:29,409 INFO     29 [qwen-vl-text] LLM extraction start, text_len=231
2026-08-10 18:59:29,409 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:59:29,409 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 17, \"encounter_dates\": [\"2025-07-10\"], \"department\": \"呼吸内五科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "郑州大学第一附属医院\n组织病理学检查与诊断报告\n姓名：\n性别：女\n年龄：57岁\n送检医院：本院\n送检科室：呼吸内五科\n送检医生：刘莹\n报告日期：2025-07-10 10:06\n标本名称：左肺\n临床诊断：肺恶性肿瘤\n肉眼所见：（左肺）暗红组织一块，大小约1.6*0.7*0.3cm。\n病理诊断：（左肺活检）非小细胞癌，组织学形态考虑腺癌，需补费后免疫组化协诊。\n病理号：B25-\n收到日期：2025-01-08\n住院号：0004\n第4页 共5页\n标本号：9041",
    "role": "user"
  }
]
2026-08-10 18:59:29,625 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 18:59:29,626 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Parser:MedLink | outputs={"html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "json"}
2026-08-10 18:59:29,626 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 18:59:29,645 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:59:29,645 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 姓名\n[BBOX-1] 现住址\n[BBOX-2] 性别：女\n[BBOX-3] 职业：农民\n[BBOX-4] 年龄：60岁\n[BBOX-5] 入院时间：2024年01月17日10点52分\n[BBOX-6] 民族：汉族\n[BBOX-7] 记录时间：2024年01月17日16点00分\n[BBOX-8] 婚姻：已婚\n[BBOX-9] 病史陈述者\n[BBOX-10] 陈述者与患者关系：本人\n[BBOX-11] 陈述者内容可靠标志：可靠\n[BBOX-12] 主诉：肺腺癌5周期化疗后2年进展后化疗5周期后。\n[BBOX-13] 现病史：患者2020.8月体检时行胸部CT检查提示右肺上叶片状影，无咳嗽、咳痰、\n[BBOX-14] 咯血、痰中带血及胸痛、发热、盗汗等不适，遂就诊于当地医院给予“左氧氟沙星、\n[BBOX-15] 法罗培南”等药物抗感染治疗，复查胸部CT提示吸收欠佳。患者为求进一步诊治就诊\n[BBOX-16] 于我院，行胸部CT检查考虑右肺上叶浸润性肺腺Ca，在排除相关禁忌并取得患者家属\n[BBOX-17] 知情同意后，行经皮肺穿刺活检，病理结果示：（右肺上叶）穿刺肺组织呈显著慢性\n[BBOX-18] 炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变\n[BBOX-19] 炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1(+)，CK7(+)，Ki-67阳性\n[BBOX-20] 率10%。为排查肿瘤全身转移情况行骨ECT及腹部强化CT检查未见明显转移征象，行颅\n[BBOX-21] 脑MRI提示右颞枕叶、左侧小脑下蚓部异常信号，结合肿瘤病史，建议增强扫描除外\n[BBOX-22] 转移，为排除颅脑转移，进一步行颅脑强化MRI提示右侧颞枕叶脑沟内条片状轻度强\n[BBOX-23] 化，考虑软脑膜增厚强化，结合肺Ca病史，脑膜转移不除外，建议脑脊液检查。脑脊\n[BBOX-24] 液检查未见肿瘤细胞。在取得外科会诊意见明确患者具有手术指征后，患者于2020-0\n[BBOX-25] 8-31于胸外科行右肺上叶切除并肺部、纵膈淋巴结清扫术，术后病理示：（右肺上叶\n[BBOX-26] ）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，\n[BBOX-27] 肿物切面面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；\n[BBOX-28] 肺组织内查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚\n[BBOX-29] 查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔\n[BBOX-30] 淋巴结4枚，其中2枚查见转移癌（2/4）。另送第7组淋巴结9枚（0/9）、第9组淋巴结\n[BBOX-31] 1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。术后行EGFR等十基因检测\n[BBOX-32] （石蜡包埋组织）示EFGR基因 Exon-20（外显子） 20-ins突变阳性。后患者为行\n[BBOX-33] 进一步治疗就诊我科，告知患者其Exon-20突变不适合靶向药物治疗，建议行化疗治\n[BBOX-34] 疗，在排除相关禁忌并取得患者及家属知情同意后，于2020-10-16、2020-11-10、\n[BBOX-35] 2020-12-04、2020-12-26、2021-1-18行“培美曲塞二钠0.8g d1+卡铂400mg d1\n[BBOX-36] ”方案化疗5周期，患者耐受可。2023.9.21、2023.10.13、2023.11.8、2023.12\n[BBOX-37] .4、2023.12.26排除禁忌给予卡铂+培美曲塞二钠联合贝伐珠单抗治疗5周期，耐受\n[BBOX-38] 可。2023.11.07复查CT示：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19\n[BBOX-39] CT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂\n[BBOX-40] 肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水\n[BBOX-41] ；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著\n[BBOX-42] 第1页\n[BBOX-43] 入院记录\n[BBOX-44] 姓名\n[BBOX-45] 住院号\n[BBOX-46] 。患者治疗后出现发热，体温38.7°C，化验示白细胞2.05*109/L，中性粒细胞0.7\n[BBOX-47] 5*109/L，给予升白对症处理。患者自上次出院后，饮食、睡眠可，大小便未见明显\n[BBOX-48] 异常，体重无明显改变。\n[BBOX-49] 既往史：既往身体健康，否认高血压，否认糖尿病，否认冠心病，否认结核等传染病\n[BBOX-50] 史及密切接触史，否认外伤史，否认手术史，否认输血史，预防接种史：随当地，过\n[BBOX-51] 敏史：食物过敏史：无，药物过敏史：无。\n[BBOX-52] 个人史：生于原籍，无外地久居史，无疫区到访及停留史，无工业毒物、粉尘、放射\n[BBOX-53] 性物质接触史，吸烟史：无，饮酒史：无。\n[BBOX-54] 月经史：已绝经。\n[BBOX-55] 婚育史：已婚，已育。\n[BBOX-56] 家族史：否认家族遗传病史。\n[BBOX-57] 体格检查\n[BBOX-58] T:36℃ P:97次/分 R:23次/分 血压：154/94mmHg 体重：72kg 身高：16\n[BBOX-59] 0cm NRS：0\n[BBOX-60] 一般情况：老年女性，神志清晰，精神好，发育正常，营养良好，自主体位，查体合作\n[BBOX-61] 。\n[BBOX-62] 皮肤、粘膜：颜色红润，无皮肤黄疸，无明显皮肤红肿硬肿，无凹陷性水肿，无皮疹\n[BBOX-63] ，未见出血点，未见瘀斑。皮肤弹性好。无肿大淋巴结。\n[BBOX-64] 头部及其器官：头颅无畸形；双眼无畸形，双侧瞳孔等大，对光反射存在；双耳无畸\n[BBOX-65] 形；鼻无畸形。口唇红润，无唇裂，咽无充血。\n[BBOX-66] 颈部：无抵抗感，气管居中，胸锁乳突肌包块：无。甲状腺正常，无颈部淋巴结肿大\n[BBOX-67] 。\n[BBOX-68] 胸部：双侧对称，无畸形；双肩等高，呼吸动度双侧一致，三凹征阴性。肺呼吸音：\n[BBOX-69] 清，未闻及干湿性啰音，未闻及胸膜摩擦音。\n[BBOX-70] 心脏：心前区无隆起，心尖搏动位于左侧锁骨中线第5肋间，心音有力，心律齐，未\n[BBOX-71] 闻及明显杂音，无心包摩擦音。\n[BBOX-72] 腹部：腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。腹部叩诊呈\n[BBOX-73] 鼓音；肠鸣音正常，4次/分。\n[BBOX-74] 肛门外生殖器：肛门位置正常。外阴外观无畸形。\n[BBOX-75] 脊柱：脊柱生理曲度正常。\n[BBOX-76] 四肢：四肢肌力正常，肌张力正常。\n[BBOX-77] 神经系统：双侧腱反射正常，脑膜刺激征阴性，双侧病理征阴性。\n[BBOX-78] 专科情况\n[BBOX-79] 无。\n[BBOX-80] 入院记录\n[BBOX-81] 辅助检查\n[BBOX-82] 日期\n[BBOX-83] 项目\n[BBOX-84] 结果\n[BBOX-85] 2020-07-29\n[BBOX-86] 胸部CT\n[BBOX-87] 考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检，双肺间质性改变，右肾结石\n[BBOX-88] 2020-08-10\n[BBOX-89] 肺功能\n[BBOX-90] 肺通气功能正常\n[BBOX-91] 2020-08-10\n[BBOX-92] 胸部强化CT\n[BBOX-93] 考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检；右肺门淋巴结肿大；双肺纤维灶；肝囊肿；右肾结石\n[BBOX-94] 2020-08-10\n[BBOX-95] 肺组织活检\n[BBOX-96] （右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1 (+), CK7(+), Ki-67阳性率10%\n[BBOX-97] 2020-08-14\n[BBOX-98] 骨扫描\n[BBOX-99] 1.右肺坐骨支局限性骨质代谢增高观察；2.L5山医\n[BBOX-100] 2020-08-16\n[BBOX-101] 颅脑MR强化\n[BBOX-102] 强化后FLAIR显示右侧颞枕叶脑沟内条片状轻度山医\n[BBOX-103] 2020-08-31\n[BBOX-104] 肺组织术后病理\n[BBOX-105] （右肺上叶）浸润性腺癌，腺泡型（60%），乳山医\n[BBOX-106] 2020-09-23\n[BBOX-107] 基因检测\n[BBOX-108] EGFR等十基因检测（石蜡包埋组织）：EFGR基山医\n[BBOX-109] 2022-06-01\n[BBOX-110] 胸部CT平扫\n[BBOX-111] 右肺术后CT表现，请结合临床；双肺纤维灶左山医\n[BBOX-112] 2023-03-29\n[BBOX-113] 胸部CT平扫\n[BBOX-114] 右肺术后CT表现，较2022-06-01 前片变化不大；双肺多发小结节，对比2022-06-01 前片\n[BBOX-115] 2023-09-13\n[BBOX-116] CT平扫\n[BBOX-117] 双侧基底节区少许缺血变性灶，必要时结合MRI\n[BBOX-118] 第 3 页\n[BBOX-119] 入院记录\n[BBOX-120] 住\n[BBOX-121] 2023-11-07\n[BBOX-122] 强化CT\n[BBOX-123] 右肺术后，右肺纤维灶，右侧胸膜增厚，较\n[BBOX-124] 2023-09-19 CT变化不著；双肺多发小结节，\n[BBOX-125] 较前变化不著，请结合临床、随诊复查；提示\n[BBOX-126] 轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊\n[BBOX-127] 肿、左肾盂旁囊肿；右肾小结石、右肾轻度积\n[BBOX-128] 水；右侧附件区囊性低密度，请结合临床及妇\n[BBOX-129] 科超声；左侧耻骨高密度，较前变化不著\n[BBOX-130] 初步诊断：\n[BBOX-131] 1. 右肺上叶浸润性腺癌术后（T1bN2M0, I\n[BBOX-132] IIA期 EGFR突变：Exon-20（外显子） 20-i\n[BBOX-133] ns突变阳性）\n[BBOX-134] 2. 右肾结石\n[BBOX-135] 3. 子宫切除术后\n[BBOX-136] 4. 化疗后骨髓抑制\n[BBOX-137] 记录者：\n[BBOX-138] 项目内容\n[BBOX-139] 患方签名\n[BBOX-140] 以上所记录内容属实\n[BBOX-141] 签字时间\n[BBOX-142] 年 月 日 时 分\n[BBOX-143] X光号：\n[BBOX-144] 出院记录\n[BBOX-145] 入院日期：2024年1月17日10点52分\n[BBOX-146] 性别：女\n[BBOX-147] 出院日期：2024年1月20日07点00分\n[BBOX-148] 年龄：60岁\n[BBOX-149] 住院天数：3天\n[BBOX-150] 入院情况：1. 患者老年女性因“肺腺癌5周期化疗后2年进展后化疗5周期后\n[BBOX-151] ”入院治疗。2. 体格检查：双肺呼吸音清，未闻及干湿性啰音，未闻及胸膜摩擦\n[BBOX-152] 音。心律齐，未闻及明显杂音，无心包摩擦音。腹部平坦，无腹壁静脉曲张。全\n[BBOX-153] 腹柔软，无包块；脾肋下未触及。\n[BBOX-154] 入院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo\n[BBOX-155] n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨\n[BBOX-156] 髓抑制\n[BBOX-157] 诊疗经过：入院后完善各项相关检查，排除禁忌于2024.1.19给予培美曲塞\n[BBOX-158] 二钠800mg+卡铂400mg，耐受可。\n[BBOX-159] 出院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo\n[BBOX-160] n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨\n[BBOX-161] 髓抑制\n[BBOX-162] 出院情况：一般状况可。\n[BBOX-163] 出院医嘱：出院后注意休息，加强营养，避免感染；定期复查血常规，每周\n[BBOX-164] 1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；2024.2.9返院继续\n[BBOX-165] 治疗；不适务必及时随诊。\n[BBOX-166] 医师签名：\n[BBOX-167] 签字时间：2024年1月20日07点00分\n[BBOX-168] 第1页\n[BBOX-169] 门诊病历\n[BBOX-170] 初诊\n[BBOX-171] 复诊\n[BBOX-172] 门诊号\n[BBOX-173] 就诊\n[BBOX-174] 姓名\n[BBOX-175] 性别：女\n[BBOX-176] 年龄：60岁\n[BBOX-177] 身份\n[BBOX-178] 职业：农民\n[BBOX-179] 就诊时间：2024-03-01 08:13:19\n[BBOX-180] 联系人\n[BBOX-181] 联系电话\n[BBOX-182] 现住址\n[BBOX-183] T:\n[BBOX-184] ℃\n[BBOX-185] P:\n[BBOX-186] 次/分\n[BBOX-187] R:\n[BBOX-188] 次/分\n[BBOX-189] BP:\n[BBOX-190] /\n[BBOX-191] mmHg\n[BBOX-192] 处方\n[BBOX-193] 检查\n[BBOX-194] 检验\n[BBOX-195] 医疗医嘱\n[BBOX-196] 主诉：\n[BBOX-197] 肺Ca术后3年余，肺结节？\n[BBOX-198] 现病史：\n[BBOX-199] 3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）\n[BBOX-200] 20-ins突变阳性。\n[BBOX-201] 2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双\n[BBOX-202] 肺多发小结节，较前变化不著，请结合临床、随诊复查。\n[BBOX-203] 既往史：\n[BBOX-204] 否认其他病史。\n[BBOX-205] 家族史：\n[BBOX-206] 否认家族史。\n[BBOX-207] 过敏史：\n[BBOX-208] 体征：\n[BBOX-209] 辅助检查：\n[BBOX-210] 2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小\n[BBOX-211] 结节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于\n[BBOX-212] 左肺下叶外基底段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03\n[BBOX-213] 提示浸润性腺癌，大小3*2.5cm，查见淋巴结转移癌\n[BBOX-214] 初步诊断：\n[BBOX-215] 肺癌\n[BBOX-216] 修正诊断：\n[BBOX-217] 肺癌术后肺结节\n[BBOX-218] 处方：\n[BBOX-219] 检查：\n[BBOX-220] 检验：\n[BBOX-221] 医疗医嘱：\n[BBOX-222] 其他建议：\n[BBOX-223] 建议3月后复查\n[BBOX-224] 已告知患者病情及可能的药物不良反应。\n[BBOX-225] 医生签\n[BBOX-226] 门诊病历\n[BBOX-227] 性别：女\n[BBOX-228] 年龄：61岁\n[BBOX-229] 民族：汉族\n[BBOX-230] 婚姻：已婚\n[BBOX-231] 职业：农民\n[BBOX-232] 证件类型：居民身份证\n[BBOX-233] 证件号码\n[BBOX-234] 门诊编号\n[BBOX-235] 就诊医院\n[BBOX-236] 就诊科室：\n[BBOX-237] 就诊日期：2024-08-13 08:50:41\n[BBOX-238] 初诊/复诊：初诊  复诊\n[BBOX-239] 陪检者姓名：\n[BBOX-240] 陪检者与患者的关系：\n[BBOX-241] 联系电话\n[BBOX-242] 处方\n[BBOX-243] 检查\n[BBOX-244] 检验\n[BBOX-245] 医疗医嘱\n[BBOX-246] 主诉：肺Ca术后3年余，肺结节？\n[BBOX-247] 现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-\n[BBOX-248] ins突变阳性。\n[BBOX-249] 2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结\n[BBOX-250] 节，较前变化不著，请结合临床、随诊复查。\n[BBOX-251] 既往史：否认其他病史。\n[BBOX-252] 家族史：否认家族史\n[BBOX-253] 过敏史：无\n[BBOX-254] 体温（℃）\n[BBOX-255] 脉博（次/分）\n[BBOX-256] 收缩压（mmHg）\n[BBOX-257] 舒张压（mmHg）\n[BBOX-258] 呼吸（次/分）\n[BBOX-259] 意识状态  清醒\n[BBOX-260] 主要症状和体征：\n[BBOX-261] 体格检查：\n[BBOX-262] 辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结\n[BBOX-263] 节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底\n[BBOX-264] 段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小\n[BBOX-265] 3*2.5cm，查见淋巴结转移癌\n[BBOX-266] 初步诊断：肺癌\n[BBOX-267] 修正诊断：肺癌术后\n[BBOX-268] 处\n[BBOX-269] 方：\n[BBOX-270] 检\n[BBOX-271] 验：\n[BBOX-272] 门诊检验申请单（生化检验申请单），项目为：血生化 肝功 血脂（生化室）肾功（生\n[BBOX-273] 化）\n[BBOX-274] 门诊检验申请单（门诊检验申请单），项目为：血细胞分析五分类（静脉）（门化）\n[BBOX-275] 门诊检验申请单（中心检验申请单），项目为：AFP-甲胎蛋白 CEA-癌胚抗原 NSE-神经\n[BBOX-276] 元特异性烯化醇酶 非小细胞癌相关抗原（中心）\n[BBOX-277] 检\n[BBOX-278] 查：\n[BBOX-279] 门诊检查申请单（CT检查申请单（新）），项目为：胸部CT平扫\n[BBOX-280] 医疗医嘱：\n[BBOX-281] 其他建议：\n[BBOX-282] 门诊病历\n[BBOX-283] 性别：女\n[BBOX-284] 证件类型：居民身份证\n[BBOX-285] 年龄：62岁\n[BBOX-286] 证件\n[BBOX-287] 民族：汉族\n[BBOX-288] 门诊编\n[BBOX-289] 婚姻：已婚\n[BBOX-290] 就诊医院\n[BBOX-291] 职业：农民\n[BBOX-292] 就诊科室\n[BBOX-293] 就诊日期：2025-08-12 08:11:41\n[BBOX-294] 陪检者姓名：\n[BBOX-295] 初诊/复诊：初诊□复诊\n[BBOX-296] 陪检者与患者的关系：\n[BBOX-297] 联系电话\n[BBOX-298] 处方\n[BBOX-299] 检查\n[BBOX-300] 检验\n[BBOX-301] 医疗医嘱\n[BBOX-302] 主诉：肺Ca术后3年余，肺结节？\n[BBOX-303] 现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-\n[BBOX-304] ins突变阳性。\n[BBOX-305] 2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结\n[BBOX-306] 节，较前变化不著，请结合临床、随诊复查。\n[BBOX-307] 既往史：否认其他病史。\n[BBOX-308] 家族史：否认家族史\n[BBOX-309] 过敏史：无\n[BBOX-310] 体温（℃）\n[BBOX-311] 脉搏（次/分）\n[BBOX-312] 收缩压（mmHg）\n[BBOX-313] 舒张压（mmHg）\n[BBOX-314] 呼吸（次/分）\n[BBOX-315] 意识状态 清醒\n[BBOX-316] 主要症状和体征：\n[BBOX-317] 体格检查：\n[BBOX-318] 辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结\n[BBOX-319] 节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底\n[BBOX-320] 段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小\n[BBOX-321] 3*2.5cm，查见淋巴结转移癌\n[BBOX-322] 初步诊断：肺癌\n[BBOX-323] 修正诊断：肺癌术后\n[BBOX-324] 处\n[BBOX-325] 方：\n[BBOX-326] 检\n[BBOX-327] 验：\n[BBOX-328] 检\n[BBOX-329] 查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫\n[BBOX-330] 医疗医嘱：\n[BBOX-331] 其他建议：\n[BBOX-332] 门诊病历\n[BBOX-333] 性别：女\n[BBOX-334] 年龄：63岁\n[BBOX-335] 民族：汉族\n[BBOX-336] 婚姻：已婚\n[BBOX-337] 职业：农民\n[BBOX-338] 证件类型：居民身份证\n[BBOX-339] 证件号\n[BBOX-340] 门诊编\n[BBOX-341] 就诊医院\n[BBOX-342] 就诊科室\n[BBOX-343] 就诊日期：2026-03-10 08:35:11\n[BBOX-344] 初诊/复诊：初诊 □ 复诊\n[BBOX-345] 联系电\n[BBOX-346] 陪伴者姓名：\n[BBOX-347] 陪伴者与患者的关系：\n[BBOX-348] 处方\n[BBOX-349] 检查\n[BBOX-350] 检验\n[BBOX-351] 医疗医嘱\n[BBOX-352] 主诉：肺Ca术后4年余，肺结节？\n[BBOX-353] 现病史：4年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-\n[BBOX-354] ins突变阳性。\n[BBOX-355] 2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结\n[BBOX-356] 节，较前变化不著，请结合临床、随诊复查。\n[BBOX-357] 2025.8.11CT：双肺多发小结节，较大者位于左肺外周，均较前片变化不著\n[BBOX-358] 既往史：否认其他病史。\n[BBOX-359] 家族史：否认家族史\n[BBOX-360] 过敏史：无\n[BBOX-361] 体温（℃）\n[BBOX-362] 脉搏（次/分）\n[BBOX-363] 收缩压（mmHg）\n[BBOX-364] 舒张压（mmHg）\n[BBOX-365] 呼吸（次/分）\n[BBOX-366] 意识状态 清醒\n[BBOX-367] 主要症状和体征：\n[BBOX-368] 体格检查：\n[BBOX-369] 辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结\n[BBOX-370] 节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底\n[BBOX-371] 段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小\n[BBOX-372] 3*2.5cm，查见淋巴结转移癌\n[BBOX-373] 初步诊断：肺癌,肺结节\n[BBOX-374] 修正诊断：肺癌,肺结节\n[BBOX-375] 处方：\n[BBOX-376] 检验：门诊检验申请单(临床生化检验一(临床生化检验))，项目为：血糖 糖化血红蛋白测定\n[BBOX-377] 检查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫\n[BBOX-378] 医疗医嘱：\n[BBOX-379] 其他建议：\n[BBOX-380] 已告知患者病情及可能的药物不良反应。\n[BBOX-381] 医生\n[BBOX-382] 病理检查报告单\n[BBOX-383] 检查号\n[BBOX-384] 住院号\n[BBOX-385] 姓名\n[BBOX-386] 性别:女\n[BBOX-387] 结论: (右肺上叶)形态符合腺癌,待常规病理免疫组化确诊。\n[BBOX-388] 此报告尚未打印\n[BBOX-389] 当前报告状态: 已打印\n[BBOX-390] 江苏省捷达科技发展有限公司 版权所有 © 2015\n[BBOX-391] Copyright 2007-2015 JEDA all rights reserved\n[BBOX-392] 病理检查报告单\n[BBOX-393] 检查号\n[BBOX-394] 住院号\n[BBOX-395] 门诊号:\n[BBOX-396] 姓名\n[BBOX-397] 性别:女\n[BBOX-398] 年龄:57岁\n[BBOX-399] 结合202036909（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体\n[BBOX-400] 呈周围型，肿物切面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内\n[BBOX-401] 结论:查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第\n[BBOX-402] 11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌(2/4)。另送第7组\n[BBOX-403] 淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。\n[BBOX-404] 此报告尚未打印\n[BBOX-405] 当前报告状态:已打印\n[BBOX-406] 分子病理基因检测报告单\n[BBOX-407] 样本信息\n[BBOX-408] 项目编号：PCR20-1135\n[BBOX-409] 姓名\n[BBOX-410] 性别：女\n[BBOX-411] 年龄：57岁\n[BBOX-412] 住院号\n[BBOX-413] 病理号\n[BBOX-414] 送检医生\n[BBOX-415] 标本类别：石蜡包埋组织\n[BBOX-416] 送检科室\n[BBOX-417] 送检时间：2020-09-23\n[BBOX-418] 送检医院：本院\n[BBOX-419] 联系电话\n[BBOX-420] 检测方法：ARMS PCR\n[BBOX-421] 检测位点：\n[BBOX-422] 检查项目：九基因\n[BBOX-423] 检测结果\n[BBOX-424] 检测项目\n[BBOX-425] 外显因子\n[BBOX-426] 突变类型\n[BBOX-427] 检测结果\n[BBOX-428] EGFR基因\n[BBOX-429] Exon19\n[BBOX-430] 19-del\n[BBOX-431] 野生型\n[BBOX-432] Exon21\n[BBOX-433] L858R\n[BBOX-434] 野生型\n[BBOX-435] Exon20\n[BBOX-436] T790M\n[BBOX-437] 野生型\n[BBOX-438] Exon18\n[BBOX-439] G719X\n[BBOX-440] 野生型\n[BBOX-441] Exon20\n[BBOX-442] S768I\n[BBOX-443] 野生型\n[BBOX-444] Exon21\n[BBOX-445] L861Q\n[BBOX-446] 野生型\n[BBOX-447] Exon20\n[BBOX-448] 20-ins\n[BBOX-449] 突变型\n[BBOX-450] KRAS基因\n[BBOX-451] Exon-2\n[BBOX-452] G12D/S\n[BBOX-453] 野生型\n[BBOX-454] G12A/V/R/C、G13C\n[BBOX-455] 野生型\n[BBOX-456] BRAF基因\n[BBOX-457] Exon-15\n[BBOX-458] V600E/K/R/D\n[BBOX-459] 野生型\n[BBOX-460] NRAS基因\n[BBOX-461] Exon-3\n[BBOX-462] Q61R/K/L/H\n[BBOX-463] 野生型\n[BBOX-464] 初诊医师：戚美\n[BBOX-465] 复诊医师：刘龙\n[BBOX-466] 报告日期：2020-09-23\n[BBOX-467] 分子病理基因检测报告单\n[BBOX-468] 检测项目\n[BBOX-469] 外显因子\n[BBOX-470] 突变类型\n[BBOX-471] 检测结果\n[BBOX-472] PIK3CA基因\n[BBOX-473] Exon-20\n[BBOX-474] H1047R\n[BBOX-475] 野生型\n[BBOX-476] Exon-9\n[BBOX-477] E545K\n[BBOX-478] ALK融合基因\n[BBOX-479] ALK-Exon-20\n[BBOX-480] 具体突变类型见附录\n[BBOX-481] 野生型\n[BBOX-482] ROS1融合基因\n[BBOX-483] ROS1-Exon-32/34/35\n[BBOX-484] 具体突变类型见附录\n[BBOX-485] 野生型\n[BBOX-486] RET融合基因\n[BBOX-487] RET-Exon-12\n[BBOX-488] 具体突变类型见附录\n[BBOX-489] 野生型\n[BBOX-490] HER2基因\n[BBOX-491] Exon-20\n[BBOX-492] 20-ins/G776>VC(1)\n[BBOX-493] 野生型\n[BBOX-494] MET基因\n[BBOX-495] MET-Exon-14\n[BBOX-496] MET exon13;METexon15\n[BBOX-497] 野生型\n[BBOX-498] 备注：\n[BBOX-499] 由于肿瘤存在异质性现象，此检测结果只针对本次样本有效。结果仅供临床参考\n[BBOX-500] ，不可作为临床诊治的唯一依据。\n[BBOX-501] 驱动基因突变状态是靶向药物治疗的重要疗效预测因子，EGFR和KRAS突变状态可\n[BBOX-502] 以指导EGFR-TKIs的用药；ALK、ROS1基因融合突变及MET外显子14跳跃突变可以\n[BBOX-503] 从ALK/ROS1/MET抑制剂中明显受益；BRAF基因突变患者可以从RAF抑制剂和MEK\n[BBOX-504] 抑制剂中明显受益\n[BBOX-505] 初诊医师：戚美\n[BBOX-506] 复诊医师：刘龙\n[BBOX-507] 报告日期：2020-09-23\n[BBOX-508] 本报告仅供临床浏览，严禁私自打印。报告单以放射科室打印\n[BBOX-509] 放射科CT报告单\n[BBOX-510] 姓名\n[BBOX-511] 性别 女\n[BBOX-512] 年龄 63岁\n[BBOX-513] 病人编\n[BBOX-514] 检查编号 CT02901334\n[BBOX-515] 门诊号\n[BBOX-516] 检查日期 2026-03-10 09:33 报告日期 2026-03-10 12:07 病人来源 门诊\n[BBOX-517] 检查方法及部位 胸部CT平扫,上腹部CT平扫\n[BBOX-518] 检查所见:\n[BBOX-519] 结合病史，右肺术后，局部见条片状高密度及点线状致密灶，右侧肺门结构\n[BBOX-520] 紊乱，右侧肋骨术后态；右侧胸膜增厚，右膈略抬高。双肺见多发大小不等\n[BBOX-521] 结节灶，部分呈磨玻璃密度，结节较大者位于左肺下叶IM32，为部分实性小\n[BBOX-522] 结节，大小约1.4cm×1.0cm，可见分叶、胸膜凹陷征象；双肺纹理增多、紊\n[BBOX-523] 乱，见纤维灶。左肺段以上支气管开口通畅，左肺门不大，纵隔内见增大淋\n[BBOX-524] 巴结，大者最大短径约1.2cm。未见胸腔积液征象。冠状动脉钙化。双腋窝\n[BBOX-525] 见小淋巴结。\n[BBOX-526] 肝脏形态可，肝实质密度稍低，肝右叶见数个小圆形低密度灶，肝内另见\n[BBOX-527] 斑点状高密度。肝内外胆管无扩张。胆囊不大，壁不厚，内未见高密度灶。\n[BBOX-528] 胰腺未见明显异常。脾脏不大，质均匀。右肾盂肾盏轻度扩张；左肾及左肾\n[BBOX-529] 窦见小类圆形低密度灶。双肾上腺未见明显异常。腹膜后未见肿大淋巴结。\n[BBOX-530] 骨窗示局部腰椎变扁。\n[BBOX-531] 检查结论:\n[BBOX-532] 右肺术后，右肺纤维灶，右侧胸膜增厚\n[BBOX-533] 双肺多发小结节，考虑双肺多发转移可能，较前2025-08-12CT增多、增\n[BBOX-534] 大，请结合临床\n[BBOX-535] 冠状动脉钙化\n[BBOX-536] 提示轻度脂肪肝；肝内钙化灶；肝囊肿\n[BBOX-537] 左肾囊肿；右肾轻度积水\n[BBOX-538] 局部腰椎变扁\n[BBOX-539] \\begin{tabular}{llllllllll}\n[BBOX-540] 报告时间: 2026-03-10\n[BBOX-541] \\hline\n[BBOX-542] NO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 & \\\\\n[BBOX-543] \\hline\n[BBOX-544] 1 & *★白细胞 & WBC & 8.22 & & 3.5-9.5 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-545] 2 & 中性粒细胞比率 & NEU\\% & 72.10 & & 40-75 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-546] 3 & 淋巴细胞比率 & LYM\\% & 20.30 & & 20-50 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-547] 4 & 嗜酸性粒细胞比率 & EOS\\% & 0.40 & & 0.4-8.0 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-548] 5 & 嗜碱性粒细胞比率 & BAS\\% & 0.40 & & 0-1 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-549] 6 & 单核细胞比率 & MON\\% & 6.80 & & 3-10 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-550] 7 & 中性粒细胞计数 & NEU\\# & 5.93 & & 1.8-6.3 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-551] 8 & 淋巴细胞计数 & LYM\\# & 1.67 & & 1.1-3.2 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-552] 9 & 嗜酸性粒细胞计数 & EOS\\# & 0.03 & & 0.02-0.52 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-553] 10 & 嗜碱性粒细胞计数 & BAS\\# & 0.03 & & 0-0.06 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-554] 11 & 单核细胞计数 & MON\\# & 0.56 & & 0.1-0.6 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n[BBOX-555] 12 & *★红细胞 & RBC & 5.22 & 1 & 3.8-5.1 & 10^12/L & XN9100 & 液压聚焦（DC检测） & \\\\\n[BBOX-556] 13 & *★血红蛋白 & HGB & 147.0 & & 115-150 & g/L & XN9100 & SLS-血红蛋白法 & \\\\\n[BBOX-557] 14 & *★红细胞压积 & HCT & 44.90 & & 35.0-45.0 & \\% & XN9100 & 脉冲信号累积法 & \\\\\n[BBOX-558] 15 & *平均红细胞体积 & MCV & 86.0 & & 82-100 & fL & XN9100 & 计算法 & \\\\\n[BBOX-559] 16 & *平均血红蛋白含量 & MCH & 28.2 & & 27-34 & pg & XN9100 & 计算法 & \\\\\n[BBOX-560] 17 & *平均血红蛋白浓度 & MCHC & 327.0 & & 316-354 & g/L & XN9100 & 计算法 & \\\\\n[BBOX-561] 18 & 红细胞平均宽度 & RDW & 12.6 & & 10-14.6 & \\% & XN9100 & 直方图解析测量 & \\\\\n[BBOX-562] 19 & *★血小板计数 & PLT & 309 & & 125-350 & 10^9/L & XN9100 & 液压聚焦（DC检测） & \\\\\n[BBOX-563] 20 & 血小板平均宽度 & PDW & 8.30 & & 9-17 & fL & XN9100 & 直方图解析测量 & \\\\\n[BBOX-564] 21 & 平均血小板体积 & MPV & 8.30 & & 6-14 & fL & XN9100 & 计算法 & \\\\\n[BBOX-565] 22 & 血小板压积 & PCT & 0.260 & & 0.114-0.282 & \\% & XN9100 & 脉冲信号累积法 & \\\\\n[BBOX-566] \\hline\n[BBOX-567] \\end{tabular}\n[BBOX-568] \\begin{tabular}{llllllllll}\n[BBOX-569] 报告时间: 2026-03-10\n[BBOX-570] \\hline\n[BBOX-571] NO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 \\\\\n[BBOX-572] \\hline\n[BBOX-573] 1 & *★丙氨酸氨基转移酶 & ALT & 13 & & 7-40 & U/L & Roche\\_3 & 速率法 \\\\\n[BBOX-574] 2 & *★天门冬氨酸氨基转移酶 & AST & 15 & & 13-35 & U/L & Roche\\_3 & 速率法 \\\\\n[BBOX-575] 3 & 谷氨酸脱氢酶 & GLDH & 5.7 & & $<$7.4 & U/L & Roche\\_3 & 速率法 \\\\\n[BBOX-576] 4 & *★γ-谷丙酰基转肽酶 & GGT & 15 & & 7-45 & U/L & Roche\\_3 & 速率法 \\\\\n[BBOX-577] 5 & ★碱性磷酸酶 & AKP & 93 & & 50-135 & U/L & Roche\\_3 & 速率法 \\\\\n[BBOX-578] 6 & 腺苷脱氨酶 & ADA & 8 & & 4-18 & U/L & Roche\\_3 & 速率法 \\\\\n[BBOX-579] 7 & *★总胆红素 & TBIL & 8.2 & & 5.0-21.0 & $\\mu$mol/L & Roche\\_3 & 重氮法 \\\\\n[BBOX-580] 8 & *直接胆红素 & DBIL & 2.6 & & $<$6.0 & $\\mu$mol/L & Roche\\_3 & 重氮法 \\\\\n[BBOX-581] 9 & 间接胆红素 & IBIL & 5.6 & & 2.0-15.0 & $\\mu$mol/L & & 计算 \\\\\n[BBOX-582] 10 & *前白蛋白 & PA & 30.2 & & 17.0-40.0 & mg/dl & Roche\\_3 & 免疫比浊法 \\\\\n[BBOX-583] 11 & *★总蛋白 & TP & 75.4 & & 60.0-85.0 & g/L & Roche\\_3 & 双缩脲法 \\\\\n[BBOX-584] 12 & *★白蛋白 & ALB & 48.6 & & 40.0-55.0 & g/L & Roche\\_3 & 溴钾酚绿 \\\\\n[BBOX-585] 13 & 球蛋白 & GLB & 26.8 & & 20.0-40.0 & g/L & & 计算 \\\\\n[BBOX-586] 14 & 白/球比例 & A/G & 1.81 & & 1.2-2.4 & & & 计算 \\\\\n[BBOX-587] 15 & 总胆汁酸 & TBA & 1.3 & & $<$15.0 & $\\mu$mol/L & Roche\\_3 & 循环酶法 \\\\\n[BBOX-588] 16 & *★总胆固醇 & Cho & 7.28 & & 2.80-6.00 & mmol/L & Roche\\_3 & 酶法 \\\\\n[BBOX-589] 17 & *★高密度脂蛋白胆固醇 & HDL-C & 1.78 & $\\uparrow$ & 0.80-2.00 & mmol/L & Roche\\_3 & 酶法 \\\\\n[BBOX-590] 18 & *★低密度脂蛋白胆固醇 & LDL-C & 4.89 & $\\uparrow$ & 1.00-3.37 & mmol/L & Roche\\_3 & 酶法 \\\\\n[BBOX-591] 19 & 小而密低密度脂蛋白 & sdLDL & 2.01 & $\\uparrow$ & 0.25-1.17 & mmol/L & Roche\\_3 & 酶法 \\\\\n[BBOX-592] 20 & *血清载脂蛋白A1 & APOA1 & 1.96 & $\\uparrow$ & 1.00-1.60 & g/L & Roche\\_3 & 免疫比浊法 \\\\\n[BBOX-593] 21 & *血清载脂蛋白B & APOB & 1.53 & $\\uparrow$ & 0.60-1.00 & g/L & Roche\\_3 & 免疫比浊法 \\\\\n[BBOX-594] 22 & *★甘油三酯 & TG & 2.30 & $\\uparrow$ & 0.30-1.70 & mmol/L & Roche\\_3 & 酶法 \\\\\n[BBOX-595] 23 & 脂蛋白a & LP(a) & 9.70 & & $<$75.00 & nmol/L & Roche\\_3 & 免疫比浊法 \\\\\n[BBOX-596] 24 & 游离脂肪酸 & NEFA & 125.0 & $\\uparrow$ & 10.0-85.0 & umol/dl & Roche\\_3 & 酶法 \\\\\n[BBOX-597] 25 & 脂蛋白磷脂酶A2 & PLA2 & 728 & $\\uparrow$ & $<$659 & U/L & Roche\\_3 & 酶法 \\\\\n[BBOX-598] 26 & *★尿素 & Urea & 3.59 & & 2.30-7.80 & mmol/L & Roche\\_3 & 酶法 \\\\\n[BBOX-599] 27 & *★肌酐 & Cr & 38 & $\\downarrow$ & 53-97 & $\\mu$mol/L & Roche\\_3 & 酶法 \\\\\n[BBOX-600] 28 & *胱抑素C & Cys-C & 0.76 & & 0.51-1.09 & mg/L & Roche\\_3 & 免疫比浊法 \\\\\n[BBOX-601] 29 & 肾小球滤过率 & eGFR & 108.600 & & & ml/min & Roche\\_3 & 计算 \\\\\n[BBOX-602] 30 & *★钾 & K & 4.23 & & 3.50-5.30 & mmol/L & Roche\\_3 & 离子选择电极 \\\\\n[BBOX-603] 31 & *★钠 & NA & 139 & & 137-147 & mmol/L & Roche\\_3 & 离子选择电极法 \\\\\n[BBOX-604] 32 & *★氯 & CL & 104 & & 99-110 & mmol/L & Roche\\_3 & 离子选择电极法 \\\\\n[BBOX-605] 33 & 二氧化碳结合力 & CO2 & 21.5 & & 18.0-28.0 & mmol/L & Roche\\_3 & 酶法 \\\\\n[BBOX-606] 34 & *★钙 & Ca & 2.36 & & 2.11-2.52 & mmol/L & Roche\\_3 & 比色法 \\\\\n[BBOX-607] 35 & ★磷 & P & 1.21 & & 0.60-1.60 & mmol/L & Roche\\_3 & 比色法 \\\\\n[BBOX-608] 36 & *镁 & Mg & 0.86 & & 0.65-1.10 & mmol/L & Roche\\_3 & 比色法 \\\\\n[BBOX-609] \\hline\n[BBOX-610] \\end{tabular}\n[BBOX-611] \\begin{tabular}{llllllllll}\n[BBOX-612] 报告时间: 2026-03-10\n[BBOX-613] \\hline\n[BBOX-614] NO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 \\\\\n[BBOX-615] \\hline\n[BBOX-616] 1 & *★甲胎蛋白 & AFP & 3.41 & & 0.00-7.00 & ng/ml & Roche\\_4 & 电化学发光 \\\\\n[BBOX-617] 2 & *★癌胚抗原 & CEA & 3.52 & & 0.00-5.00 & ng/ml & Roche\\_4 & 电化学发光 \\\\\n[BBOX-618] 3 & 非小细胞肺癌相关抗原 & CYFRA21-1 & 1.70 & & 0.00-3.30 & ng/ml & Roche\\_4 & 电化学发光 \\\\\n[BBOX-619] 4 & 神经元特异性烯醇化酶 & NSE & 16.60 & 1 & 0.00-16.30 & ng/ml & Roche\\_4 & 电化学发光 \\\\\n[BBOX-620] \\hline\n[BBOX-621] \\end{tabular}\n[BBOX-622] 20200831手术 术后病理肺腺癌\n[BBOX-623] 20201016~20210118培美+卡铂5周期\n[BBOX-624] 20230931~20231226培美+卡铂+贝伐5周期\n[BBOX-625] 20240119培美+卡铂"
  }
]
2026-08-10 18:59:30,089 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T18:59:30.087+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 18:59:40,742 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:59:40,743 INFO     29 [qwen-vl-text] LLM output (len=392):
{
  "exam_date": "2025-01-08",
  "report_date": "2025-07-10",
  "exam_name": "组织病理学检查与诊断报告",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "呼吸内五科",
  "bed_number": null,
  "findings": "肉眼所见：（左肺）暗红组织一块，大小约1.6*0.7*0.3cm。",
  "conclusion": "病理诊断：（左肺活检）非小细胞癌，组织学形态考虑腺癌，需补费后免疫组化协诊。",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:59:40,748 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1850457, prompt_len=898
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["郑州大学第一附属医院", "组织病理学检查与诊断报告", "姓名：", "性别：女", "年龄：57岁", "送检医院：本院", "送检科室：呼吸内五科", "送检医生：刘莹", "报告日期：2025-07-10 10:06", "标本名称：左肺", "临床诊断：肺恶性肿瘤", "肉眼所见：（左肺）暗红组织一块，大小约1.6*0.7*0.3cm。", "病理诊断：（左肺活检）非小细胞癌，组织学形态考虑腺癌，需补费后免疫组化协诊。", "病理号：B25-", "收到日期：2025-01-08", "住院号：0004", "第4页 共5页", "标本号：9041"]

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
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord API raw response (len=1018):
[
	{"text": "郑州大学第一附属医院", "bbox": [350, 237, 713, 273]},
	{"text": "组织病理学检查与诊断报告", "bbox": [335, 262, 727, 296]},
	{"text": "姓名：", "bbox": [70, 338, 152, 360]},
	{"text": "性别：女", "bbox": [385, 338, 470, 358]},
	{"text": "年龄：57岁", "bbox": [552, 344, 654, 362]},
	{"text": "送检医院：本院", "bbox": [65, 360, 208, 381]},
	{"text": "送检科室：呼吸内五科", "bbox": [385, 363, 604, 384]},
	{"text": "送检医生：刘莹", "bbox": [60, 382, 206, 403]},
	{"text": "报告日期：2025-07-10 10:06", "bbox": [384, 387, 670, 407]},
	{"text": "标本名称：左肺", "bbox": [54, 410, 205, 429]},
	{"text": "临床诊断：肺恶性肿瘤", "bbox": [50, 435, 277, 453]},
	{"text": "肉眼所见：（左肺）暗红组织一块，大小约1.6*0.7*0.3cm。", "bbox": [45, 464, 639, 483]},
	{"text": "病理诊断：（左肺活检）非小细胞癌，组织学形态考虑腺癌，需补费后免疫组化协诊。", "bbox": [25, 672, 916, 694]},
	{"text": "病理号：B25-", "bbox": [709, 322, 848, 339]},
	{"text": "收到日期：2025-01-08", "bbox": [709, 348, 918, 365]},
	{"text": "住院号：0004", "bbox": [709, 371, 864, 388]},
	{"text": "第4页 共5页", "bbox": [878, 97, 960, 120]},
	{"text": "标本号：9041", "bbox": [888, 111, 970, 134]}
]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=11.7s
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[0]: text=郑州大学第一附属医院, bbox=[350, 237, 713, 273]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[1]: text=组织病理学检查与诊断报告, bbox=[335, 262, 727, 296]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[70, 338, 152, 360]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[385, 338, 470, 358]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：57岁, bbox=[552, 344, 654, 362]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[5]: text=送检医院：本院, bbox=[65, 360, 208, 381]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[6]: text=送检科室：呼吸内五科, bbox=[385, 363, 604, 384]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[7]: text=送检医生：刘莹, bbox=[60, 382, 206, 403]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[8]: text=报告日期：2025-07-10 10:06, bbox=[384, 387, 670, 407]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[9]: text=标本名称：左肺, bbox=[54, 410, 205, 429]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[10]: text=临床诊断：肺恶性肿瘤, bbox=[50, 435, 277, 453]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[11]: text=肉眼所见：（左肺）暗红组织一块，大小约1.6*0.7*0.3cm。, bbox=[45, 464, 639, 483]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[12]: text=病理诊断：（左肺活检）非小细胞癌，组织学形态考虑腺癌，需补费后免疫组化协诊。, bbox=[25, 672, 916, 694]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[13]: text=病理号：B25-, bbox=[709, 322, 848, 339]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[14]: text=收到日期：2025-01-08, bbox=[709, 348, 918, 365]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[15]: text=住院号：0004, bbox=[709, 371, 864, 388]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[16]: text=第4页 共5页, bbox=[878, 97, 960, 120]
2026-08-10 18:59:52,402 INFO     29 [qwen-vl-text] coord item[17]: text=标本号：9041, bbox=[888, 111, 970, 134]
2026-08-10 18:59:52,403 INFO     29 [qwen-vl-text] page=0 — 18/18 coords, api_time=11.7s
2026-08-10 18:59:52,403 INFO     29 [qwen-vl-text] new_positions (18):
[[0, 378.0, 770.0400000000001, 455.03999999999996, 524.16], [0, 361.8, 785.1600000000001, 503.03999999999996, 568.3199999999999], [0, 75.60000000000001, 164.16000000000003, 648.9599999999999, 691.1999999999999], [0, 415.8, 507.6, 648.9599999999999, 687.36], [0, 596.1600000000001, 706.32, 660.48, 695.04], [0, 70.2, 224.64000000000001, 691.1999999999999, 731.52], [0, 415.8, 652.32, 696.9599999999999, 737.28], [0, 64.80000000000001, 222.48000000000002, 733.4399999999999, 773.76], [0, 414.72, 723.6, 743.04, 781.4399999999999], [0, 58.32000000000001, 221.4, 787.1999999999999, 823.68], [0, 54.0, 299.16, 835.1999999999999, 869.76], [0, 48.6, 690.12, 890.88, 927.36], [0, 27.0, 989.2800000000001, 1290.24, 1332.48], [0, 765.72, 915.84, 618.24, 650.88], [0, 765.72, 991.44, 668.16, 700.8], [0, 765.72, 933.1200000000001, 712.3199999999999, 744.9599999999999], [0, 948.24, 1036.8000000000002, 186.23999999999998, 230.39999999999998], [0, 959.0400000000001, 1047.6000000000001, 213.12, 257.28]]
2026-08-10 18:59:52,403 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=23.3s
2026-08-10 18:59:52,403 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 18:59:52,405 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 18:59:52,405 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 18:59:52,405 INFO     29 [qwen-vl-text] positions(16): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 18:59:52,405 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [16]
2026-08-10 18:59:52,769 INFO     29 [qwen-vl-text] page=1, rect=1080x1920, img=(3000x5334), dpi=200
2026-08-10 18:59:52,772 INFO     29 [qwen-vl-text] LLM extraction start, text_len=201
2026-08-10 18:59:52,772 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:59:52,772 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 27, \"bbox_end\": 42, \"encounter_dates\": [\"2025-07-10\"], \"department\": \"呼吸内五科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "郑州大学第一附属医院\n细胞病理学检查与诊断报告\n病理号：C25\n姓名：\n性别：女\n年龄：57岁\n收到日期：2025-07-08\n送检医院：本院\n送检科室：呼吸内五科\n住院号：00049\n送检医生：刘莹\n报告日期：2025-07-10 15:31\n标本名称：TCT肺\n临床诊断：肺恶性肿瘤\n镜下所见：（左肺穿刺TCT）镜下见少量核浆比大的细胞。\n病理诊断：提示：发现可疑肿瘤细胞，具体诊断请结合活检结果。",
    "role": "user"
  }
]
2026-08-10 18:59:57,961 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 18:59:57,961 INFO     29 [qwen-vl-text] LLM output (len=377):
{
  "exam_date": "2025-07-08",
  "report_date": "2025-07-10",
  "exam_name": "细胞病理学检查与诊断报告",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "呼吸内五科",
  "bed_number": null,
  "findings": "镜下所见：（左肺穿刺TCT）镜下见少量核浆比大的细胞。",
  "conclusion": "病理诊断：提示：发现可疑肿瘤细胞，具体诊断请结合活检结果。",
  "physician": null,
  "reviewer": null
}
2026-08-10 18:59:57,964 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1826579, prompt_len=862
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["郑州大学第一附属医院", "细胞病理学检查与诊断报告", "病理号：C25", "姓名：", "性别：女", "年龄：57岁", "收到日期：2025-07-08", "送检医院：本院", "送检科室：呼吸内五科", "住院号：00049", "送检医生：刘莹", "报告日期：2025-07-10 15:31", "标本名称：TCT肺", "临床诊断：肺恶性肿瘤", "镜下所见：（左肺穿刺TCT）镜下见少量核浆比大的细胞。", "病理诊断：提示：发现可疑肿瘤细胞，具体诊断请结合活检结果。"]

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
2026-08-10 19:00:09,852 INFO     29 [qwen-vl-text] coord API raw response (len=908):
[
	{"text": "郑州大学第一附属医院", "bbox": [363, 282, 685, 307]},
	{"text": "细胞病理学检查与诊断报告", "bbox": [353, 305, 700, 328]},
	{"text": "病理号：C25", "bbox": [691, 343, 813, 359]},
	{"text": "姓名：", "bbox": [115, 382, 200, 403]},
	{"text": "性别：女", "bbox": [407, 374, 483, 390]},
	{"text": "年龄：57岁", "bbox": [554, 370, 645, 386]},
	{"text": "收到日期：2025-07-08", "bbox": [694, 363, 883, 381]},
	{"text": "送检医院：本院", "bbox": [115, 400, 253, 422]},
	{"text": "送检科室：呼吸内五科", "bbox": [409, 392, 604, 410]},
	{"text": "住院号：00049", "bbox": [698, 385, 838, 402]},
	{"text": "送检医生：刘莹", "bbox": [115, 420, 255, 441]},
	{"text": "报告日期：2025-07-10 15:31", "bbox": [411, 410, 667, 430]},
	{"text": "标本名称：TCT肺", "bbox": [115, 445, 268, 467]},
	{"text": "临床诊断：肺恶性肿瘤", "bbox": [115, 465, 325, 488]},
	{"text": "镜下所见：（左肺穿刺TCT）镜下见少量核浆比大的细胞。", "bbox": [130, 641, 663, 687]},
	{"text": "病理诊断：提示：发现可疑肿瘤细胞，具体诊断请结合活检结果。", "bbox": [131, 659, 740, 710]}
]
2026-08-10 19:00:09,852 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=11.9s
2026-08-10 19:00:09,852 INFO     29 [qwen-vl-text] coord item[0]: text=郑州大学第一附属医院, bbox=[363, 282, 685, 307]
2026-08-10 19:00:09,852 INFO     29 [qwen-vl-text] coord item[1]: text=细胞病理学检查与诊断报告, bbox=[353, 305, 700, 328]
2026-08-10 19:00:09,852 INFO     29 [qwen-vl-text] coord item[2]: text=病理号：C25, bbox=[691, 343, 813, 359]
2026-08-10 19:00:09,852 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[115, 382, 200, 403]
2026-08-10 19:00:09,852 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[407, 374, 483, 390]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：57岁, bbox=[554, 370, 645, 386]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[6]: text=收到日期：2025-07-08, bbox=[694, 363, 883, 381]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[7]: text=送检医院：本院, bbox=[115, 400, 253, 422]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[8]: text=送检科室：呼吸内五科, bbox=[409, 392, 604, 410]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[9]: text=住院号：00049, bbox=[698, 385, 838, 402]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[10]: text=送检医生：刘莹, bbox=[115, 420, 255, 441]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[11]: text=报告日期：2025-07-10 15:31, bbox=[411, 410, 667, 430]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[12]: text=标本名称：TCT肺, bbox=[115, 445, 268, 467]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[13]: text=临床诊断：肺恶性肿瘤, bbox=[115, 465, 325, 488]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[14]: text=镜下所见：（左肺穿刺TCT）镜下见少量核浆比大的细胞。, bbox=[130, 641, 663, 687]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] coord item[15]: text=病理诊断：提示：发现可疑肿瘤细胞，具体诊断请结合活检结果。, bbox=[131, 659, 740, 710]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] page=1 — 16/16 coords, api_time=11.9s
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] new_positions (16):
[[1, 392.04, 739.8000000000001, 541.4399999999999, 589.4399999999999], [1, 381.24, 756.0, 585.6, 629.76], [1, 746.2800000000001, 878.0400000000001, 658.56, 689.28], [1, 124.2, 216.0, 733.4399999999999, 773.76], [1, 439.56, 521.64, 718.0799999999999, 748.8], [1, 598.32, 696.6, 710.4, 741.12], [1, 749.5200000000001, 953.6400000000001, 696.9599999999999, 731.52], [1, 124.2, 273.24, 768.0, 810.24], [1, 441.72, 652.32, 752.64, 787.1999999999999], [1, 753.84, 905.0400000000001, 739.1999999999999, 771.8399999999999], [1, 124.2, 275.40000000000003, 806.4, 846.7199999999999], [1, 443.88000000000005, 720.36, 787.1999999999999, 825.6], [1, 124.2, 289.44, 854.4, 896.64], [1, 124.2, 351.0, 892.8, 936.9599999999999], [1, 140.4, 716.0400000000001, 1230.72, 1319.04], [1, 141.48000000000002, 799.2, 1265.28, 1363.2]]
2026-08-10 19:00:09,853 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=17.4s
2026-08-10 19:00:09,853 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:00:09,854 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:00:09,854 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:00:09,854 INFO     29 [qwen-vl-text] positions(30): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:00:09,854 INFO     29 [qwen-vl-text] page grouping: [14, 15], lines per page: [29, 1]
2026-08-10 19:00:10,249 INFO     29 [qwen-vl-text] page=14, rect=1080x1920, img=(3000x5334), dpi=200
2026-08-10 19:00:10,526 INFO     29 [qwen-vl-text] page=15, rect=1080x1919, img=(3000x5331), dpi=200
2026-08-10 19:00:10,529 INFO     29 [qwen-vl-text] LLM extraction start, text_len=498
2026-08-10 19:00:10,529 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:00:10,530 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 493, \"bbox_end\": 522, \"encounter_dates\": [\"2026-02-03\"], \"department\": \"肿瘤内科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "原阳县人民医院\nCT检查报告单\n病人ID:\n姓名:\n性别:女\n年龄:57岁\n检查类型:CT\n病人来源:住院\n住院号:02\n床号:/\n申请科室:肿瘤内科病区\n检查部位:胸部平扫(CT)\n检查时2026-02-03 08:40:46\n间:\n影像所见:\n双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，内见含气支气管。双肺可\n见多发微、小结节、增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺\n可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴结。左侧胸膜可见增厚，\n未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。附见左侧肾上腺见结节状软组织\n密度影。\n影像诊断:\n1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-20片纵隔淋巴结稍增大；\n2、双肺局限性支气管扩张；\n3、双肺小空泡病灶，较前大致相仿；\n4、两肺多发微、小结节，考虑转移瘤，较前增多；\n5、两肺炎性病变较前进展；\n6、左侧胸膜增厚；左侧第6肋骨顺位欠佳；\n7、左侧肾上腺结节，考虑转移，较前大致相仿；\n请结合临床、病史及其它相关检查。\n2026.2.6",
    "role": "user"
  }
]
2026-08-10 19:00:10,534 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:00:10.533+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:00:10,536 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:00:10,697 INFO     29 [SmartSplitter] SmartSplitter done: 13 chunks from 13 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 4, 'ExaminationReport': 4, 'LabReport': 3}
2026-08-10 19:00:10,706 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 19:00:10,706 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "13 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 4, 'ExaminationReport': 4, 'LabReport': 3}"}
2026-08-10 19:00:10,707 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 19:00:10,707 INFO     29 [ChunkRouter] Routed 13 chunks into 5 groups: {'chunks_Admission': 1, 'chunks_Discharge': 1, 'chunks_Clinical': 4, 'chunks_Examination': 4, 'chunks_LabExam': 3}
2026-08-10 19:00:10,715 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 19:00:10,715 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | ChunkRouter:Router | outputs={"html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "13 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 4, 'ExaminationReport': 4, 'LabReport': 3}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:00:10,715 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 19:00:10,720 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:00:10,720 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:00:10,720 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[14]
2026-08-10 19:00:10,720 INFO     29 [qwen-vl-table] positions ： [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:00:10,969 INFO     29 [qwen-vl-table] page=14, rect=410x539, img=(1139x1498)
2026-08-10 19:00:10,969 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:00:10,970 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 540, \"bbox_end\": 567, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "报告时间: 2026-03-10\n\\hline\nNO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 & \\\\\n\\hline\n1 & *★白细胞 & WBC & 8.22 & & 3.5-9.5 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n2 & 中性粒细胞比率 & NEU\\% & 72.10 & & 40-75 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n3 & 淋巴细胞比率 & LYM\\% & 20.30 & & 20-50 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n4 & 嗜酸性粒细胞比率 & EOS\\% & 0.40 & & 0.4-8.0 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n5 & 嗜碱性粒细胞比率 & BAS\\% & 0.40 & & 0-1 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n6 & 单核细胞比率 & MON\\% & 6.80 & & 3-10 & \\% & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n7 & 中性粒细胞计数 & NEU\\# & 5.93 & & 1.8-6.3 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n8 & 淋巴细胞计数 & LYM\\# & 1.67 & & 1.1-3.2 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n9 & 嗜酸性粒细胞计数 & EOS\\# & 0.03 & & 0.02-0.52 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n10 & 嗜碱性粒细胞计数 & BAS\\# & 0.03 & & 0-0.06 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n11 & 单核细胞计数 & MON\\# & 0.56 & & 0.1-0.6 & 10^9/L & XN9100 & 半导体激光器的流式细胞计数法 & \\\\\n12 & *★红细胞 & RBC & 5.22 & 1 & 3.8-5.1 & 10^12/L & XN9100 & 液压聚焦（DC检测） & \\\\\n13 & *★血红蛋白 & HGB & 147.0 & & 115-150 & g/L & XN9100 & SLS-血红蛋白法 & \\\\\n14 & *★红细胞压积 & HCT & 44.90 & & 35.0-45.0 & \\% & XN9100 & 脉冲信号累积法 & \\\\\n15 & *平均红细胞体积 & MCV & 86.0 & & 82-100 & fL & XN9100 & 计算法 & \\\\\n16 & *平均血红蛋白含量 & MCH & 28.2 & & 27-34 & pg & XN9100 & 计算法 & \\\\\n17 & *平均血红蛋白浓度 & MCHC & 327.0 & & 316-354 & g/L & XN9100 & 计算法 & \\\\\n18 & 红细胞平均宽度 & RDW & 12.6 & & 10-14.6 & \\% & XN9100 & 直方图解析测量 & \\\\\n19 & *★血小板计数 & PLT & 309 & & 125-350 & 10^9/L & XN9100 & 液压聚焦（DC检测） & \\\\\n20 & 血小板平均宽度 & PDW & 8.30 & & 9-17 & fL & XN9100 & 直方图解析测量 & \\\\\n21 & 平均血小板体积 & MPV & 8.30 & & 6-14 & fL & XN9100 & 计算法 & \\\\\n22 & 血小板压积 & PCT & 0.260 & & 0.114-0.282 & \\% & XN9100 & 脉冲信号累积法 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:00:21,610 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:00:21,610 INFO     29 [qwen-vl-text] LLM output (len=677):
{
  "exam_date": "2026-02-03",
  "report_date": "2026-02-06",
  "exam_name": "胸部平扫(CT)",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "肿瘤内科病区",
  "bed_number": null,
  "findings": "双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，内见含气支气管。双肺可见多发微、小结节、增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴结。左侧胸膜可见增厚，未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。附见左侧肾上腺见结节状软组织密度影。",
  "conclusion": "1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-20片纵隔淋巴结稍增大；\n2、双肺局限性支气管扩张；\n3、双肺小空泡病灶，较前大致相仿；\n4、两肺多发微、小结节，考虑转移瘤，较前增多；\n5、两肺炎性病变较前进展；\n6、左侧胸膜增厚；左侧第6肋骨顺位欠佳；\n7、左侧肾上腺结节，考虑转移，较前大致相仿；\n请结合临床、病史及其它相关检查。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:00:21,619 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3910610, prompt_len=1189
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["原阳县人民医院", "CT检查报告单", "病人ID:", "姓名:", "性别:女", "年龄:57岁", "检查类型:CT", "病人来源:住院", "住院号:02", "床号:/", "申请科室:肿瘤内科病区", "检查部位:胸部平扫(CT)", "检查时2026-02-03 08:40:46", "间:", "影像所见:", "双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，内见含气支气管。双肺可", "见多发微、小结节、增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺", "可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴结。左侧胸膜可见增厚，", "未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。附见左侧肾上腺见结节状软组织", "密度影。", "影像诊断:", "1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-20片纵隔淋巴结稍增大；", "2、双肺局限性支气管扩张；", "3、双肺小空泡病灶，较前大致相仿；", "4、两肺多发微、小结节，考虑转移瘤，较前增多；", "5、两肺炎性病变较前进展；", "6、左侧胸膜增厚；左侧第6肋骨顺位欠佳；", "7、左侧肾上腺结节，考虑转移，较前大致相仿；", "请结合临床、病史及其它相关检查。"]

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
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord API raw response (len=1768):
[
	{"text": "原阳县人民医院", "bbox": [373, 132, 637, 155]},
	{"text": "CT检查报告单", "bbox": [413, 160, 590, 179]},
	{"text": "病人ID:", "bbox": [127, 203, 187, 214]},
	{"text": "姓名:", "bbox": [127, 220, 187, 232]},
	{"text": "性别:女", "bbox": [313, 219, 390, 231]},
	{"text": "年龄:57岁", "bbox": [451, 218, 530, 230]},
	{"text": "检查类型:CT", "bbox": [563, 217, 664, 229]},
	{"text": "病人来源:住院", "bbox": [127, 238, 243, 250]},
	{"text": "住院号:02", "bbox": [313, 237, 390, 249]},
	{"text": "床号:/", "bbox": [452, 237, 507, 248]},
	{"text": "申请科室:肿瘤内科病区", "bbox": [564, 235, 748, 247]},
	{"text": "检查部位:胸部平扫(CT)", "bbox": [129, 255, 327, 268]},
	{"text": "检查时2026-02-03 08:40:46", "bbox": [450, 253, 693, 266]},
	{"text": "间:", "bbox": [450, 266, 478, 278]},
	{"text": "影像所见:", "bbox": [134, 279, 210, 291]},
	{"text": "双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，内见含气支气管。双肺可", "bbox": [134, 287, 900, 300]},
	{"text": "见多发微、小结节、增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺", "bbox": [134, 298, 900, 311]},
	{"text": "可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴结。左侧胸膜可见增厚，", "bbox": [134, 309, 898, 322]},
	{"text": "未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。附见左侧肾上腺见结节状软组织", "bbox": [134, 320, 908, 333]},
	{"text": "密度影。", "bbox": [134, 334, 193, 347]},
	{"text": "影像诊断:", "bbox": [145, 460, 220, 471]},
	{"text": "1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-20片纵隔淋巴结稍增大；", "bbox": [145, 471, 707, 484]},
	{"text": "2、双肺局限性支气管扩张；", "bbox": [145, 483, 345, 496]},
	{"text": "3、双肺小空泡病灶，较前大致相仿；", "bbox": [145, 494, 410, 507]},
	{"text": "4、两肺多发微、小结节，考虑转移瘤，较前增多；", "bbox": [145, 505, 509, 518]},
	{"text": "5、两肺炎性病变较前进展；", "bbox": [145, 516, 345, 529]},
	{"text": "6、左侧胸膜增厚；左侧第6肋骨顺位欠佳；", "bbox": [145, 526, 452, 539]},
	{"text": "7、左侧肾上腺结节，考虑转移，较前大致相仿；", "bbox": [145, 537, 493, 550]},
	{"text": "请结合临床、病史及其它相关检查。", "bbox": [145, 548, 405, 560]}
]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=17.0s
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[373, 132, 637, 155]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[1]: text=CT检查报告单, bbox=[413, 160, 590, 179]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID:, bbox=[127, 203, 187, 214]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[127, 220, 187, 232]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[313, 219, 390, 231]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:57岁, bbox=[451, 218, 530, 230]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[6]: text=检查类型:CT, bbox=[563, 217, 664, 229]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[7]: text=病人来源:住院, bbox=[127, 238, 243, 250]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[8]: text=住院号:02, bbox=[313, 237, 390, 249]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[9]: text=床号:/, bbox=[452, 237, 507, 248]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[10]: text=申请科室:肿瘤内科病区, bbox=[564, 235, 748, 247]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位:胸部平扫(CT), bbox=[129, 255, 327, 268]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[12]: text=检查时2026-02-03 08:40:46, bbox=[450, 253, 693, 266]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[13]: text=间:, bbox=[450, 266, 478, 278]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[14]: text=影像所见:, bbox=[134, 279, 210, 291]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[15]: text=双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，内见含气支气管。双肺可, bbox=[134, 287, 900, 300]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[16]: text=见多发微、小结节、增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺, bbox=[134, 298, 900, 311]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[17]: text=可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴结。左侧胸膜可见增厚，, bbox=[134, 309, 898, 322]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[18]: text=未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。附见左侧肾上腺见结节状软组织, bbox=[134, 320, 908, 333]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[19]: text=密度影。, bbox=[134, 334, 193, 347]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[20]: text=影像诊断:, bbox=[145, 460, 220, 471]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[21]: text=1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-20片纵隔淋巴结稍增大；, bbox=[145, 471, 707, 484]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[22]: text=2、双肺局限性支气管扩张；, bbox=[145, 483, 345, 496]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[23]: text=3、双肺小空泡病灶，较前大致相仿；, bbox=[145, 494, 410, 507]
2026-08-10 19:00:38,577 INFO     29 [qwen-vl-text] coord item[24]: text=4、两肺多发微、小结节，考虑转移瘤，较前增多；, bbox=[145, 505, 509, 518]
2026-08-10 19:00:38,578 INFO     29 [qwen-vl-text] coord item[25]: text=5、两肺炎性病变较前进展；, bbox=[145, 516, 345, 529]
2026-08-10 19:00:38,578 INFO     29 [qwen-vl-text] coord item[26]: text=6、左侧胸膜增厚；左侧第6肋骨顺位欠佳；, bbox=[145, 526, 452, 539]
2026-08-10 19:00:38,578 INFO     29 [qwen-vl-text] coord item[27]: text=7、左侧肾上腺结节，考虑转移，较前大致相仿；, bbox=[145, 537, 493, 550]
2026-08-10 19:00:38,578 INFO     29 [qwen-vl-text] coord item[28]: text=请结合临床、病史及其它相关检查。, bbox=[145, 548, 405, 560]
2026-08-10 19:00:38,578 INFO     29 [qwen-vl-text] page=14 — 29/29 coords, api_time=17.0s
2026-08-10 19:00:38,583 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2971266, prompt_len=623
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["2026.2.6"]

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
2026-08-10 19:00:45,300 INFO     29 [qwen-vl-text] coord API raw response (len=54):
[
	{"text": "2026.2.6", "bbox": [337, 87, 492, 107]}
]
2026-08-10 19:00:45,301 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=6.7s
2026-08-10 19:00:45,301 INFO     29 [qwen-vl-text] coord item[0]: text=2026.2.6, bbox=[337, 87, 492, 107]
2026-08-10 19:00:45,303 INFO     29 [qwen-vl-text] page=15 — 1/1 coords, api_time=6.7s
2026-08-10 19:00:45,303 INFO     29 [qwen-vl-text] new_positions (30):
[[14, 402.84000000000003, 687.96, 253.44, 297.59999999999997], [14, 446.04, 637.2, 307.2, 343.68], [14, 137.16, 201.96, 389.76, 410.88], [14, 137.16, 201.96, 422.4, 445.44], [14, 338.04, 421.20000000000005, 420.47999999999996, 443.52], [14, 487.08000000000004, 572.4000000000001, 418.56, 441.59999999999997], [14, 608.0400000000001, 717.12, 416.64, 439.68], [14, 137.16, 262.44, 456.96, 480.0], [14, 338.04, 421.20000000000005, 455.03999999999996, 478.08], [14, 488.16, 547.5600000000001, 455.03999999999996, 476.15999999999997], [14, 609.12, 807.84, 451.2, 474.24], [14, 139.32000000000002, 353.16, 489.59999999999997, 514.56], [14, 486.00000000000006, 748.44, 485.76, 510.71999999999997], [14, 486.00000000000006, 516.24, 510.71999999999997, 533.76], [14, 144.72, 226.8, 535.68, 558.72], [14, 144.72, 972.0000000000001, 551.04, 576.0], [14, 144.72, 972.0000000000001, 572.16, 597.12], [14, 144.72, 969.84, 593.28, 618.24], [14, 144.72, 980.6400000000001, 614.4, 639.36], [14, 144.72, 208.44000000000003, 641.28, 666.24], [14, 156.60000000000002, 237.60000000000002, 883.1999999999999, 904.3199999999999], [14, 156.60000000000002, 763.5600000000001, 904.3199999999999, 929.28], [14, 156.60000000000002, 372.6, 927.36, 952.3199999999999], [14, 156.60000000000002, 442.8, 948.48, 973.4399999999999], [14, 156.60000000000002, 549.72, 969.5999999999999, 994.56], [14, 156.60000000000002, 372.6, 990.7199999999999, 1015.68], [14, 156.60000000000002, 488.16, 1009.92, 1034.8799999999999], [14, 156.60000000000002, 532.44, 1031.04, 1056.0], [14, 156.60000000000002, 437.40000000000003, 1052.1599999999999, 1075.2], [15, 363.96000000000004, 531.36, 166.95822509765625, 205.33942626953126]]
2026-08-10 19:00:45,303 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=2, time=35.5s
2026-08-10 19:00:45,303 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:00:45,306 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:00:45,306 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:00:45,306 INFO     29 [qwen-vl-text] positions(34): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:00:45,307 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [34]
2026-08-10 19:00:45,692 INFO     29 [qwen-vl-text] page=16, rect=1080x1920, img=(3000x5334), dpi=200
2026-08-10 19:00:45,695 INFO     29 [qwen-vl-text] LLM extraction start, text_len=696
2026-08-10 19:00:45,695 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:00:45,697 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 561, \"bbox_end\": 594, \"encounter_dates\": [\"2025-12-20\"], \"department\": \"肿瘤内科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CT检查报告单\n病人ID:\n姓名:\n性别:女\n年龄:57岁\n检查编号:CT02\n病人来源:住院\n住院号:02\n床号:/\n检查类型:CT\n申请科室:肿瘤内科病区\n检查部位:上腹部CT增强+延迟(CT);胸部增强(C检查时间:2025-12-20 08:31:12\nT):\n影像所见:\n双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，增强病变可见明显强化，\n内见含气支气管。双肺可见多发微、小结节，增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶\n局部支气管稍扩张，双肺可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴\n结，增强可见环形强化。两侧胸膜未见明显增厚，未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未\n见明显破坏征象。\n肝脏边缘光滑，肝实质见小类圆形无强化低密度，肝内外胆管未见扩张。胆囊不大，壁厚薄均匀，\n未见异常强化，未见阳性结石影。胰腺大小、形态及密度正常，未见异常强化。脾不大，实质密度均\n匀，未见异常强化。左侧肾上腺见结节状高密度，增强可见轻中度强化，双肾大小形态正常，实质密度\n均匀，未见异常强化，肾盂未见扩张，未见阳性结石影。腹腔内及腹膜后未见强化肿大淋巴结，未见腹\n水征象。\n影像诊断:\n1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-03片较前相仿；\n2、双肺局限性支气管扩张；\n3、双肺小空泡病灶，较前壁增厚；\n4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；\n5、双肺炎性病变，较前相仿；\n6、左侧第6肋骨顺位欠佳；\n7、左侧肾上腺结节，考虑转移，较前大致相仿；\n8、肝囊肿；\n请结合临床、病史及其它相关检查。",
    "role": "user"
  }
]
2026-08-10 19:00:45,700 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:00:45.699+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:00:52,275 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:00:52,275 INFO     29 [qwen-vl-table] page=14 LLM output (len=3737):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "8.22",
      "unit": "10^9/L",
      "reference_range": "3.5-9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞比率",
      "item_code": "NEU%",
      "value": "72.10",
      "unit": "%",
      "reference_range": "40-75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞比率",
      "item_code": "LYM%",
      "value": "20.30",
      "unit": "%",
      "reference_range": "20-50",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞比率",
      "item_code": "EOS%",
      "value": "0.40",
      "unit": "%",
      "reference_range": "0.4-8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞比率",
      "item_code": "BAS%",
      "value": "0.40",
      "unit": "%",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "单核细胞比率",
      "item_code": "MON%",
      "value": "6.80",
      "unit": "%",
      "reference_range": "3-10",
      "abnormal": false
    },
    {
      "name": "中性粒细胞计数",
      "item_code": "NEU#",
      "value": "5.93",
      "unit": "10^9/L",
      "reference_range": "1.8-6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞计数",
      "item_code": "LYM#",
      "value": "1.67",
      "unit": "10^9/L",
      "reference_range": "1.1-3.2",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞计数",
      "item_code": "EOS#",
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞计数",
      "item_code": "BAS#",
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0-0.06",
      "abnormal": false
    },
    {
      "name": "单核细胞计数",
      "item_code": "MON#",
      "value": "0.56",
      "unit": "10^9/L",
      "reference_range": "0.1-0.6",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "5.22",
      "unit": "10^12/L",
      "reference_range": "3.8-5.1",
      "abnormal": true
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "147.0",
      "unit": "g/L",
      "reference_range": "115-150",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "44.90",
      "unit": "%",
      "reference_range": "35.0-45.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "86.0",
      "unit": "fL",
      "reference_range": "82-100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白含量",
      "item_code": "MCH",
      "value": "28.2",
      "unit": "pg",
      "reference_range": "27-34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": "MCHC",
      "value": "327.0",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "红细胞平均宽度",
      "item_code": "RDW",
      "value": "12.6",
      "unit": "%",
      "reference_range": "10-14.6",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "309",
      "unit": "10^9/L",
      "reference_range": "125-350",
      "abnormal": false
    },
    {
      "name": "血小板平均宽度",
      "item_code": "PDW",
      "value": "8.30",
      "unit": "fL",
      "reference_range": "9-17",
      "abnormal": true
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "8.30",
      "unit": "fL",
      "reference_range": "6-14",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.260",
      "unit": "%",
      "reference_range": "0.114-0.282",
      "abnormal": false
    }
  ]
}
2026-08-10 19:00:52,275 INFO     29 [qwen-vl-table] coord grouping: {14: 22}
2026-08-10 19:00:52,284 INFO     29 [qwen-vl-table] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4191637, prompt_len=667
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞、中性粒细胞比率、淋巴细胞比率、嗜酸性粒细胞比率、嗜碱性粒细胞比率、单核细胞比率、中性粒细胞计数、淋巴细胞计数、嗜酸性粒细胞计数、嗜碱性粒细胞计数、单核细胞计数、红细胞、血红蛋白、红细胞压积、平均红细胞体积、平均血红蛋白含量、平均血红蛋白浓度、红细胞平均宽度、血小板计数、血小板平均宽度、平均血小板体积、血小板压积

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
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord API raw response (len=1109):
[
	{"text": "白细胞", "bbox": [40, 122, 118, 137]},
	{"text": "中性粒细胞比率", "bbox": [40, 150, 160, 165]},
	{"text": "淋巴细胞比率", "bbox": [40, 177, 144, 192]},
	{"text": "嗜酸性粒细胞比率", "bbox": [40, 205, 178, 220]},
	{"text": "嗜碱性粒细胞比率", "bbox": [40, 233, 178, 248]},
	{"text": "单核细胞比率", "bbox": [40, 261, 144, 276]},
	{"text": "中性粒细胞计数", "bbox": [40, 289, 160, 304]},
	{"text": "淋巴细胞计数", "bbox": [40, 317, 144, 332]},
	{"text": "嗜酸性粒细胞计数", "bbox": [40, 345, 178, 360]},
	{"text": "嗜碱性粒细胞计数", "bbox": [40, 373, 178, 388]},
	{"text": "单核细胞计数", "bbox": [40, 401, 144, 416]},
	{"text": "红细胞", "bbox": [40, 430, 120, 445]},
	{"text": "血红蛋白", "bbox": [40, 458, 136, 473]},
	{"text": "红细胞压积", "bbox": [40, 476, 154, 491]},
	{"text": "平均红细胞体积", "bbox": [40, 494, 172, 509]},
	{"text": "平均血红蛋白含量", "bbox": [40, 512, 190, 527]},
	{"text": "平均血红蛋白浓度", "bbox": [40, 529, 190, 544]},
	{"text": "红细胞平均宽度", "bbox": [40, 547, 162, 562]},
	{"text": "血小板计数", "bbox": [40, 565, 154, 580]},
	{"text": "血小板平均宽度", "bbox": [40, 593, 162, 608]},
	{"text": "平均血小板体积", "bbox": [40, 610, 162, 625]},
	{"text": "血小板压积", "bbox": [40, 628, 130, 643]}
]
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord API: raw_items=22, valid_items=22, elapsed=5.8s
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[40, 122, 118, 137]
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞比率, bbox=[40, 150, 160, 165]
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞比率, bbox=[40, 177, 144, 192]
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord item[3]: text=嗜酸性粒细胞比率, bbox=[40, 205, 178, 220]
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord item[4]: text=嗜碱性粒细胞比率, bbox=[40, 233, 178, 248]
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord item[5]: text=单核细胞比率, bbox=[40, 261, 144, 276]
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞计数, bbox=[40, 289, 160, 304]
2026-08-10 19:00:58,071 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞计数, bbox=[40, 317, 144, 332]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[8]: text=嗜酸性粒细胞计数, bbox=[40, 345, 178, 360]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[9]: text=嗜碱性粒细胞计数, bbox=[40, 373, 178, 388]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[10]: text=单核细胞计数, bbox=[40, 401, 144, 416]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞, bbox=[40, 430, 120, 445]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[40, 458, 136, 473]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[40, 476, 154, 491]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积, bbox=[40, 494, 172, 509]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[15]: text=平均血红蛋白含量, bbox=[40, 512, 190, 527]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[16]: text=平均血红蛋白浓度, bbox=[40, 529, 190, 544]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞平均宽度, bbox=[40, 547, 162, 562]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[18]: text=血小板计数, bbox=[40, 565, 154, 580]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[19]: text=血小板平均宽度, bbox=[40, 593, 162, 608]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板体积, bbox=[40, 610, 162, 625]
2026-08-10 19:00:58,072 INFO     29 [qwen-vl-table] coord item[21]: text=血小板压积, bbox=[40, 628, 130, 643]
2026-08-10 19:00:58,073 INFO     29 [qwen-vl-table] page=14 coord: matched 22/22, time=5.8s
2026-08-10 19:00:58,074 INFO     29 [qwen-vl-table] new_positions (22):
[[15, 16.4, 48.379999999999995, 65.75800000000001, 73.843], [15, 16.4, 65.6, 80.85000000000001, 88.935], [15, 16.4, 59.04, 95.403, 103.488], [15, 16.4, 72.97999999999999, 110.495, 118.58000000000001], [15, 16.4, 72.97999999999999, 125.587, 133.672], [15, 16.4, 59.04, 140.679, 148.764], [15, 16.4, 65.6, 155.77100000000002, 163.85600000000002], [15, 16.4, 59.04, 170.863, 178.948], [15, 16.4, 72.97999999999999, 185.955, 194.04000000000002], [15, 16.4, 72.97999999999999, 201.04700000000003, 209.132], [15, 16.4, 59.04, 216.139, 224.22400000000002], [15, 16.4, 49.199999999999996, 231.77, 239.85500000000002], [15, 16.4, 55.76, 246.86200000000002, 254.947], [15, 16.4, 63.13999999999999, 256.564, 264.649], [15, 16.4, 70.52, 266.266, 274.351], [15, 16.4, 77.89999999999999, 275.968, 284.053], [15, 16.4, 77.89999999999999, 285.13100000000003, 293.216], [15, 16.4, 66.42, 294.833, 302.918], [15, 16.4, 63.13999999999999, 304.535, 312.62], [15, 16.4, 66.42, 319.627, 327.71200000000005], [15, 16.4, 66.42, 328.79, 336.875], [15, 16.4, 53.3, 338.492, 346.577]]
2026-08-10 19:00:58,074 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=22, matched=22, pages=1, time=47.4s
2026-08-10 19:00:58,076 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:00:58,078 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:00:58,078 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[15]
2026-08-10 19:00:58,078 INFO     29 [qwen-vl-table] positions ： [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:00:58,334 INFO     29 [qwen-vl-table] page=15, rect=410x534, img=(1139x1484)
2026-08-10 19:00:58,335 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:00:58,335 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 568, \"bbox_end\": 610, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllllll}\n报告时间: 2026-03-10\n\\hline\nNO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 \\\\\n\\hline\n1 & *★丙氨酸氨基转移酶 & ALT & 13 & & 7-40 & U/L & Roche\\_3 & 速率法 \\\\\n2 & *★天门冬氨酸氨基转移酶 & AST & 15 & & 13-35 & U/L & Roche\\_3 & 速率法 \\\\\n3 & 谷氨酸脱氢酶 & GLDH & 5.7 & & $<$7.4 & U/L & Roche\\_3 & 速率法 \\\\\n4 & *★γ-谷丙酰基转肽酶 & GGT & 15 & & 7-45 & U/L & Roche\\_3 & 速率法 \\\\\n5 & ★碱性磷酸酶 & AKP & 93 & & 50-135 & U/L & Roche\\_3 & 速率法 \\\\\n6 & 腺苷脱氨酶 & ADA & 8 & & 4-18 & U/L & Roche\\_3 & 速率法 \\\\\n7 & *★总胆红素 & TBIL & 8.2 & & 5.0-21.0 & $\\mu$mol/L & Roche\\_3 & 重氮法 \\\\\n8 & *直接胆红素 & DBIL & 2.6 & & $<$6.0 & $\\mu$mol/L & Roche\\_3 & 重氮法 \\\\\n9 & 间接胆红素 & IBIL & 5.6 & & 2.0-15.0 & $\\mu$mol/L & & 计算 \\\\\n10 & *前白蛋白 & PA & 30.2 & & 17.0-40.0 & mg/dl & Roche\\_3 & 免疫比浊法 \\\\\n11 & *★总蛋白 & TP & 75.4 & & 60.0-85.0 & g/L & Roche\\_3 & 双缩脲法 \\\\\n12 & *★白蛋白 & ALB & 48.6 & & 40.0-55.0 & g/L & Roche\\_3 & 溴钾酚绿 \\\\\n13 & 球蛋白 & GLB & 26.8 & & 20.0-40.0 & g/L & & 计算 \\\\\n14 & 白/球比例 & A/G & 1.81 & & 1.2-2.4 & & & 计算 \\\\\n15 & 总胆汁酸 & TBA & 1.3 & & $<$15.0 & $\\mu$mol/L & Roche\\_3 & 循环酶法 \\\\\n16 & *★总胆固醇 & Cho & 7.28 & & 2.80-6.00 & mmol/L & Roche\\_3 & 酶法 \\\\\n17 & *★高密度脂蛋白胆固醇 & HDL-C & 1.78 & $\\uparrow$ & 0.80-2.00 & mmol/L & Roche\\_3 & 酶法 \\\\\n18 & *★低密度脂蛋白胆固醇 & LDL-C & 4.89 & $\\uparrow$ & 1.00-3.37 & mmol/L & Roche\\_3 & 酶法 \\\\\n19 & 小而密低密度脂蛋白 & sdLDL & 2.01 & $\\uparrow$ & 0.25-1.17 & mmol/L & Roche\\_3 & 酶法 \\\\\n20 & *血清载脂蛋白A1 & APOA1 & 1.96 & $\\uparrow$ & 1.00-1.60 & g/L & Roche\\_3 & 免疫比浊法 \\\\\n21 & *血清载脂蛋白B & APOB & 1.53 & $\\uparrow$ & 0.60-1.00 & g/L & Roche\\_3 & 免疫比浊法 \\\\\n22 & *★甘油三酯 & TG & 2.30 & $\\uparrow$ & 0.30-1.70 & mmol/L & Roche\\_3 & 酶法 \\\\\n23 & 脂蛋白a & LP(a) & 9.70 & & $<$75.00 & nmol/L & Roche\\_3 & 免疫比浊法 \\\\\n24 & 游离脂肪酸 & NEFA & 125.0 & $\\uparrow$ & 10.0-85.0 & umol/dl & Roche\\_3 & 酶法 \\\\\n25 & 脂蛋白磷脂酶A2 & PLA2 & 728 & $\\uparrow$ & $<$659 & U/L & Roche\\_3 & 酶法 \\\\\n26 & *★尿素 & Urea & 3.59 & & 2.30-7.80 & mmol/L & Roche\\_3 & 酶法 \\\\\n27 & *★肌酐 & Cr & 38 & $\\downarrow$ & 53-97 & $\\mu$mol/L & Roche\\_3 & 酶法 \\\\\n28 & *胱抑素C & Cys-C & 0.76 & & 0.51-1.09 & mg/L & Roche\\_3 & 免疫比浊法 \\\\\n29 & 肾小球滤过率 & eGFR & 108.600 & & & ml/min & Roche\\_3 & 计算 \\\\\n30 & *★钾 & K & 4.23 & & 3.50-5.30 & mmol/L & Roche\\_3 & 离子选择电极 \\\\\n31 & *★钠 & NA & 139 & & 137-147 & mmol/L & Roche\\_3 & 离子选择电极法 \\\\\n32 & *★氯 & CL & 104 & & 99-110 & mmol/L & Roche\\_3 & 离子选择电极法 \\\\\n33 & 二氧化碳结合力 & CO2 & 21.5 & & 18.0-28.0 & mmol/L & Roche\\_3 & 酶法 \\\\\n34 & *★钙 & Ca & 2.36 & & 2.11-2.52 & mmol/L & Roche\\_3 & 比色法 \\\\\n35 & ★磷 & P & 1.21 & & 0.60-1.60 & mmol/L & Roche\\_3 & 比色法 \\\\\n36 & *镁 & Mg & 0.86 & & 0.65-1.10 & mmol/L & Roche\\_3 & 比色法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:00:58,340 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:00:58,340 INFO     29 [qwen-vl-text] LLM output (len=876):
{
  "exam_date": "2025-12-20",
  "report_date": null,
  "exam_name": "上腹部CT增强+延迟(CT);胸部增强(CT)",
  "exam_category": "imaging",
  "body_part": "上腹部;胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "肿瘤内科病区",
  "bed_number": null,
  "findings": "双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，增强病变可见明显强化，内见含气支气管。双肺可见多发微、小结节，增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴结，增强可见环形强化。两侧胸膜未见明显增厚，未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。\n肝脏边缘光滑，肝实质见小类圆形无强化低密度，肝内外胆管未见扩张。胆囊不大，壁厚薄均匀，未见异常强化，未见阳性结石影。胰腺大小、形态及密度正常，未见异常强化。脾不大，实质密度均匀，未见异常强化。左侧肾上腺见结节状高密度，增强可见轻中度强化，双肾大小形态正常，实质密度均匀，未见异常强化，肾盂未见扩张，未见阳性结石影。腹腔内及腹膜后未见强化肿大淋巴结，未见腹水征象。",
  "conclusion": "1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-03片较前相仿；\n2、双肺局限性支气管扩张；\n3、双肺小空泡病灶，较前壁增厚；\n4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；\n5、双肺炎性病变，较前相仿；\n6、左侧第6肋骨顺位欠佳；\n7、左侧肾上腺结节，考虑转移，较前大致相仿；\n8、肝囊肿；\n请结合临床、病史及其它相关检查。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:00:58,348 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3866342, prompt_len=1411
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["CT检查报告单", "病人ID:", "姓名:", "性别:女", "年龄:57岁", "检查编号:CT02", "病人来源:住院", "住院号:02", "床号:/", "检查类型:CT", "申请科室:肿瘤内科病区", "检查部位:上腹部CT增强+延迟(CT);胸部增强(C检查时间:2025-12-20 08:31:12", "T):", "影像所见:", "双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，增强病变可见明显强化，", "内见含气支气管。双肺可见多发微、小结节，增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶", "局部支气管稍扩张，双肺可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴", "结，增强可见环形强化。两侧胸膜未见明显增厚，未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未", "见明显破坏征象。", "肝脏边缘光滑，肝实质见小类圆形无强化低密度，肝内外胆管未见扩张。胆囊不大，壁厚薄均匀，", "未见异常强化，未见阳性结石影。胰腺大小、形态及密度正常，未见异常强化。脾不大，实质密度均", "匀，未见异常强化。左侧肾上腺见结节状高密度，增强可见轻中度强化，双肾大小形态正常，实质密度", "均匀，未见异常强化，肾盂未见扩张，未见阳性结石影。腹腔内及腹膜后未见强化肿大淋巴结，未见腹", "水征象。", "影像诊断:", "1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-03片较前相仿；", "2、双肺局限性支气管扩张；", "3、双肺小空泡病灶，较前壁增厚；", "4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；", "5、双肺炎性病变，较前相仿；", "6、左侧第6肋骨顺位欠佳；", "7、左侧肾上腺结节，考虑转移，较前大致相仿；", "8、肝囊肿；", "请结合临床、病史及其它相关检查。"]

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
2026-08-10 19:01:19,078 INFO     29 [qwen-vl-text] coord API raw response (len=2172):
[
	{"text": "CT检查报告单", "bbox": [412, 250, 611, 273]},
	{"text": "病人ID:", "bbox": [75, 290, 148, 303]},
	{"text": "姓名:", "bbox": [75, 310, 148, 325]},
	{"text": "性别:女", "bbox": [351, 315, 438, 330]},
	{"text": "年龄:57岁", "bbox": [533, 319, 626, 334]},
	{"text": "检查编号:CT02", "bbox": [688, 300, 824, 315]},
	{"text": "病人来源:住院", "bbox": [75, 333, 230, 348]},
	{"text": "住院号:02", "bbox": [350, 337, 444, 351]},
	{"text": "床号:/", "bbox": [533, 340, 600, 354]},
	{"text": "检查类型:CT", "bbox": [688, 322, 804, 336]},
	{"text": "申请科室:肿瘤内科病区", "bbox": [688, 342, 894, 357]},
	{"text": "检查部位:上腹部CT增强+延迟(CT);胸部增强(C检查时间:2025-12-20 08:31:12", "bbox": [75, 354, 807, 373]},
	{"text": "T):", "bbox": [198, 369, 230, 381]},
	{"text": "影像所见:", "bbox": [80, 380, 173, 393]},
	{"text": "双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，增强病变可见明显强化，", "bbox": [117, 395, 925, 412]},
	{"text": "内见含气支气管。双肺可见多发微、小结节，增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶", "bbox": [77, 408, 937, 425]},
	{"text": "局部支气管稍扩张，双肺可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴", "bbox": [77, 421, 937, 438]},
	{"text": "结，增强可见环形强化。两侧胸膜未见明显增厚，未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未", "bbox": [77, 434, 944, 450]},
	{"text": "见明显破坏征象。", "bbox": [77, 445, 230, 458]},
	{"text": "肝脏边缘光滑，肝实质见小类圆形无强化低密度，肝内外胆管未见扩张。胆囊不大，壁厚薄均匀，", "bbox": [117, 458, 922, 474]},
	{"text": "未见异常强化，未见阳性结石影。胰腺大小、形态及密度正常，未见异常强化。脾不大，实质密度均", "bbox": [77, 471, 915, 487]},
	{"text": "匀，未见异常强化。左侧肾上腺见结节状高密度，增强可见轻中度强化，双肾大小形态正常，实质密度", "bbox": [77, 484, 933, 499]},
	{"text": "均匀，未见异常强化，肾盂未见扩张，未见阳性结石影。腹腔内及腹膜后未见强化肿大淋巴结，未见腹", "bbox": [77, 496, 933, 511]},
	{"text": "水征象。", "bbox": [77, 508, 150, 520]},
	{"text": "影像诊断:", "bbox": [85, 586, 175, 599]},
	{"text": "1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-03片较前相仿；", "bbox": [80, 601, 654, 615]},
	{"text": "2、双肺局限性支气管扩张；", "bbox": [80, 614, 316, 627]},
	{"text": "3、双肺小空泡病灶，较前壁增厚；", "bbox": [80, 626, 374, 640]},
	{"text": "4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；", "bbox": [80, 638, 579, 652]},
	{"text": "5、双肺炎性病变，较前相仿；", "bbox": [80, 651, 336, 665]},
	{"text": "6、左侧第6肋骨顺位欠佳；", "bbox": [80, 664, 307, 678]},
	{"text": "7、左侧肾上腺结节，考虑转移，较前大致相仿；", "bbox": [80, 675, 487, 690]},
	{"text": "8、肝囊肿；", "bbox": [80, 690, 179, 703]},
	{"text": "请结合临床、病史及其它相关检查。", "bbox": [80, 701, 385, 715]}
]
2026-08-10 19:01:19,078 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=20.7s
2026-08-10 19:01:19,078 INFO     29 [qwen-vl-text] coord item[0]: text=CT检查报告单, bbox=[412, 250, 611, 273]
2026-08-10 19:01:19,078 INFO     29 [qwen-vl-text] coord item[1]: text=病人ID:, bbox=[75, 290, 148, 303]
2026-08-10 19:01:19,078 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[75, 310, 148, 325]
2026-08-10 19:01:19,078 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[351, 315, 438, 330]
2026-08-10 19:01:19,078 INFO     29 [qwen-vl-text] coord item[4]: text=年龄:57岁, bbox=[533, 319, 626, 334]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[5]: text=检查编号:CT02, bbox=[688, 300, 824, 315]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[6]: text=病人来源:住院, bbox=[75, 333, 230, 348]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[7]: text=住院号:02, bbox=[350, 337, 444, 351]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[8]: text=床号:/, bbox=[533, 340, 600, 354]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[9]: text=检查类型:CT, bbox=[688, 322, 804, 336]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[10]: text=申请科室:肿瘤内科病区, bbox=[688, 342, 894, 357]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位:上腹部CT增强+延迟(CT);胸部增强(C检查时间:2025-12-20 08:31:12, bbox=[75, 354, 807, 373]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[12]: text=T):, bbox=[198, 369, 230, 381]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[13]: text=影像所见:, bbox=[80, 380, 173, 393]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[14]: text=双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，增强病变可见明显强化，, bbox=[117, 395, 925, 412]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[15]: text=内见含气支气管。双肺可见多发微、小结节，增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶, bbox=[77, 408, 937, 425]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[16]: text=局部支气管稍扩张，双肺可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴, bbox=[77, 421, 937, 438]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[17]: text=结，增强可见环形强化。两侧胸膜未见明显增厚，未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未, bbox=[77, 434, 944, 450]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[18]: text=见明显破坏征象。, bbox=[77, 445, 230, 458]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[19]: text=肝脏边缘光滑，肝实质见小类圆形无强化低密度，肝内外胆管未见扩张。胆囊不大，壁厚薄均匀，, bbox=[117, 458, 922, 474]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[20]: text=未见异常强化，未见阳性结石影。胰腺大小、形态及密度正常，未见异常强化。脾不大，实质密度均, bbox=[77, 471, 915, 487]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[21]: text=匀，未见异常强化。左侧肾上腺见结节状高密度，增强可见轻中度强化，双肾大小形态正常，实质密度, bbox=[77, 484, 933, 499]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[22]: text=均匀，未见异常强化，肾盂未见扩张，未见阳性结石影。腹腔内及腹膜后未见强化肿大淋巴结，未见腹, bbox=[77, 496, 933, 511]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[23]: text=水征象。, bbox=[77, 508, 150, 520]
2026-08-10 19:01:19,079 INFO     29 [qwen-vl-text] coord item[24]: text=影像诊断:, bbox=[85, 586, 175, 599]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[25]: text=1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-03片较前相仿；, bbox=[80, 601, 654, 615]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[26]: text=2、双肺局限性支气管扩张；, bbox=[80, 614, 316, 627]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[27]: text=3、双肺小空泡病灶，较前壁增厚；, bbox=[80, 626, 374, 640]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[28]: text=4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；, bbox=[80, 638, 579, 652]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[29]: text=5、双肺炎性病变，较前相仿；, bbox=[80, 651, 336, 665]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[30]: text=6、左侧第6肋骨顺位欠佳；, bbox=[80, 664, 307, 678]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[31]: text=7、左侧肾上腺结节，考虑转移，较前大致相仿；, bbox=[80, 675, 487, 690]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[32]: text=8、肝囊肿；, bbox=[80, 690, 179, 703]
2026-08-10 19:01:19,080 INFO     29 [qwen-vl-text] coord item[33]: text=请结合临床、病史及其它相关检查。, bbox=[80, 701, 385, 715]
2026-08-10 19:01:19,081 INFO     29 [qwen-vl-text] page=16 — 34/34 coords, api_time=20.7s
2026-08-10 19:01:19,081 INFO     29 [qwen-vl-text] new_positions (34):
[[16, 444.96000000000004, 659.88, 480.0, 524.16], [16, 81.0, 159.84, 556.8, 581.76], [16, 81.0, 159.84, 595.1999999999999, 624.0], [16, 379.08000000000004, 473.04, 604.8, 633.6], [16, 575.64, 676.08, 612.48, 641.28], [16, 743.0400000000001, 889.9200000000001, 576.0, 604.8], [16, 81.0, 248.4, 639.36, 668.16], [16, 378.0, 479.52000000000004, 647.04, 673.92], [16, 575.64, 648.0, 652.8, 679.68], [16, 743.0400000000001, 868.32, 618.24, 645.12], [16, 743.0400000000001, 965.5200000000001, 656.64, 685.4399999999999], [16, 81.0, 871.5600000000001, 679.68, 716.16], [16, 213.84, 248.4, 708.48, 731.52], [16, 86.4, 186.84, 729.6, 754.56], [16, 126.36000000000001, 999.0000000000001, 758.4, 791.04], [16, 83.16000000000001, 1011.96, 783.36, 816.0], [16, 83.16000000000001, 1011.96, 808.3199999999999, 840.9599999999999], [16, 83.16000000000001, 1019.5200000000001, 833.28, 864.0], [16, 83.16000000000001, 248.4, 854.4, 879.36], [16, 126.36000000000001, 995.7600000000001, 879.36, 910.0799999999999], [16, 83.16000000000001, 988.2, 904.3199999999999, 935.04], [16, 83.16000000000001, 1007.6400000000001, 929.28, 958.0799999999999], [16, 83.16000000000001, 1007.6400000000001, 952.3199999999999, 981.12], [16, 83.16000000000001, 162.0, 975.36, 998.4], [16, 91.80000000000001, 189.0, 1125.12, 1150.08], [16, 86.4, 706.32, 1153.9199999999998, 1180.8], [16, 86.4, 341.28000000000003, 1178.8799999999999, 1203.84], [16, 86.4, 403.92, 1201.9199999999998, 1228.8], [16, 86.4, 625.32, 1224.96, 1251.84], [16, 86.4, 362.88, 1249.9199999999998, 1276.8], [16, 86.4, 331.56, 1274.8799999999999, 1301.76], [16, 86.4, 525.96, 1296.0, 1324.8], [16, 86.4, 193.32000000000002, 1324.8, 1349.76], [16, 86.4, 415.8, 1345.9199999999998, 1372.8]]
2026-08-10 19:01:19,081 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=33.8s
2026-08-10 19:01:19,082 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:01:19,084 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:01:19,084 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:01:19,084 INFO     29 [qwen-vl-text] positions(33): [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:01:19,084 INFO     29 [qwen-vl-text] page grouping: [17], lines per page: [33]
2026-08-10 19:01:19,486 INFO     29 [qwen-vl-text] page=17, rect=1080x1920, img=(3000x5334), dpi=200
2026-08-10 19:01:19,489 INFO     29 [qwen-vl-text] LLM extraction start, text_len=500
2026-08-10 19:01:19,489 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:01:19,489 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 609, \"bbox_end\": 641, \"encounter_dates\": [\"2025-12-03\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "原阳县人民医院\nCT检查报告单\n病人ID:\nP\n检查编号: CTO.\n姓名:\n薛\n性别:女\n年龄:57岁\n检查类型: CT\n病人来源: 门诊\n住院号:\n床号:\n申请科室: 呼吸与危重症医学科\n门诊\n检查部位:\n胸部平扫(CT);\n检查时间: 2025-12-03 09:26:58\n影像所见:\n左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两\n肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片\n状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见\n明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显\n破坏征象。\n影像诊断:\n1、肺癌治疗后改变，对比2025-11-05片较前相仿；\n2、双肺局限性支气管扩张；\n3、左肺下叶小空泡病灶，较前增多，壁增厚；\n4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；\n5、双肺炎性病变，较前相仿；\n6、左侧第6肋骨顺位欠佳；\n7、提示左侧肾上腺结节，较前大致相仿；\n请结合临床、病史及其它相关检查。",
    "role": "user"
  }
]
2026-08-10 19:01:19,676 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:01:19.674+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:01:28,834 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:01:28,834 INFO     29 [qwen-vl-text] LLM output (len=659):
{
  "exam_date": "2025-12-03",
  "report_date": null,
  "exam_name": "胸部平扫(CT)",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": "薛",
  "patient_gender": "女",
  "department": "呼吸与危重症医学科",
  "bed_number": null,
  "findings": "左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。",
  "conclusion": "1、肺癌治疗后改变，对比2025-11-05片较前相仿；\n2、双肺局限性支气管扩张；\n3、左肺下叶小空泡病灶，较前增多，壁增厚；\n4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；\n5、双肺炎性病变，较前相仿；\n6、左侧第6肋骨顺位欠佳；\n7、提示左侧肾上腺结节，较前大致相仿；\n请结合临床、病史及其它相关检查。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:01:28,843 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3673772, prompt_len=1212
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["原阳县人民医院", "CT检查报告单", "病人ID:", "P", "检查编号: CTO.", "姓名:", "薛", "性别:女", "年龄:57岁", "检查类型: CT", "病人来源: 门诊", "住院号:", "床号:", "申请科室: 呼吸与危重症医学科", "门诊", "检查部位:", "胸部平扫(CT);", "检查时间: 2025-12-03 09:26:58", "影像所见:", "左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两", "肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片", "状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见", "明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显", "破坏征象。", "影像诊断:", "1、肺癌治疗后改变，对比2025-11-05片较前相仿；", "2、双肺局限性支气管扩张；", "3、左肺下叶小空泡病灶，较前增多，壁增厚；", "4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；", "5、双肺炎性病变，较前相仿；", "6、左侧第6肋骨顺位欠佳；", "7、提示左侧肾上腺结节，较前大致相仿；", "请结合临床、病史及其它相关检查。"]

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
2026-08-10 19:01:48,352 INFO     29 [qwen-vl-text] coord API raw response (len=1955):
[
	{"text": "原阳县人民医院", "bbox": [383, 285, 675, 313]},
	{"text": "CT检查报告单", "bbox": [428, 321, 623, 342]},
	{"text": "病人ID:", "bbox": [100, 363, 171, 375]},
	{"text": "P", "bbox": [209, 364, 220, 375]},
	{"text": "检查编号: CTO.", "bbox": [699, 367, 827, 380]},
	{"text": "姓名:", "bbox": [100, 383, 171, 396]},
	{"text": "薛", "bbox": [209, 384, 229, 396]},
	{"text": "性别:女", "bbox": [369, 385, 455, 398]},
	{"text": "年龄:57岁", "bbox": [547, 387, 638, 399]},
	{"text": "检查类型: CT", "bbox": [698, 388, 814, 400]},
	{"text": "病人来源: 门诊", "bbox": [100, 404, 250, 417]},
	{"text": "住院号:", "bbox": [369, 405, 435, 417]},
	{"text": "床号:", "bbox": [547, 407, 593, 418]},
	{"text": "申请科室: 呼吸与危重症医学科", "bbox": [698, 407, 955, 419]},
	{"text": "门诊", "bbox": [792, 418, 829, 430]},
	{"text": "检查部位:", "bbox": [103, 428, 193, 440]},
	{"text": "胸部平扫(CT);", "bbox": [222, 428, 349, 441]},
	{"text": "检查时间: 2025-12-03 09:26:58", "bbox": [539, 430, 816, 442]},
	{"text": "影像所见:", "bbox": [107, 448, 197, 460]},
	{"text": "左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两", "bbox": [103, 461, 945, 473]},
	{"text": "肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片", "bbox": [103, 472, 944, 485]},
	{"text": "状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见", "bbox": [103, 484, 944, 497]},
	{"text": "明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显", "bbox": [103, 496, 951, 509]},
	{"text": "破坏征象。", "bbox": [105, 510, 195, 521]},
	{"text": "影像诊断:", "bbox": [116, 645, 203, 657]},
	{"text": "1、肺癌治疗后改变，对比2025-11-05片较前相仿；", "bbox": [112, 658, 522, 671]},
	{"text": "2、双肺局限性支气管扩张；", "bbox": [112, 671, 340, 684]},
	{"text": "3、左肺下叶小空泡病灶，较前增多，壁增厚；", "bbox": [112, 682, 487, 696]},
	{"text": "4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；", "bbox": [112, 694, 593, 707]},
	{"text": "5、双肺炎性病变，较前相仿；", "bbox": [112, 707, 359, 720]},
	{"text": "6、左侧第6肋骨顺位欠佳；", "bbox": [112, 719, 331, 732]},
	{"text": "7、提示左侧肾上腺结节，较前大致相仿；", "bbox": [112, 729, 450, 743]},
	{"text": "请结合临床、病史及其它相关检查。", "bbox": [114, 740, 407, 754]}
]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=19.5s
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[0]: text=原阳县人民医院, bbox=[383, 285, 675, 313]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[1]: text=CT检查报告单, bbox=[428, 321, 623, 342]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID:, bbox=[100, 363, 171, 375]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[3]: text=P, bbox=[209, 364, 220, 375]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[4]: text=检查编号: CTO., bbox=[699, 367, 827, 380]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[5]: text=姓名:, bbox=[100, 383, 171, 396]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[6]: text=薛, bbox=[209, 384, 229, 396]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[7]: text=性别:女, bbox=[369, 385, 455, 398]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[8]: text=年龄:57岁, bbox=[547, 387, 638, 399]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[9]: text=检查类型: CT, bbox=[698, 388, 814, 400]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[10]: text=病人来源: 门诊, bbox=[100, 404, 250, 417]
2026-08-10 19:01:48,353 INFO     29 [qwen-vl-text] coord item[11]: text=住院号:, bbox=[369, 405, 435, 417]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[12]: text=床号:, bbox=[547, 407, 593, 418]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[13]: text=申请科室: 呼吸与危重症医学科, bbox=[698, 407, 955, 419]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[14]: text=门诊, bbox=[792, 418, 829, 430]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[15]: text=检查部位:, bbox=[103, 428, 193, 440]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[16]: text=胸部平扫(CT);, bbox=[222, 428, 349, 441]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[17]: text=检查时间: 2025-12-03 09:26:58, bbox=[539, 430, 816, 442]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[18]: text=影像所见:, bbox=[107, 448, 197, 460]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[19]: text=左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两, bbox=[103, 461, 945, 473]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[20]: text=肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片, bbox=[103, 472, 944, 485]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[21]: text=状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见, bbox=[103, 484, 944, 497]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[22]: text=明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显, bbox=[103, 496, 951, 509]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[23]: text=破坏征象。, bbox=[105, 510, 195, 521]
2026-08-10 19:01:48,354 INFO     29 [qwen-vl-text] coord item[24]: text=影像诊断:, bbox=[116, 645, 203, 657]
2026-08-10 19:01:48,355 INFO     29 [qwen-vl-text] coord item[25]: text=1、肺癌治疗后改变，对比2025-11-05片较前相仿；, bbox=[112, 658, 522, 671]
2026-08-10 19:01:48,355 INFO     29 [qwen-vl-text] coord item[26]: text=2、双肺局限性支气管扩张；, bbox=[112, 671, 340, 684]
2026-08-10 19:01:48,355 INFO     29 [qwen-vl-text] coord item[27]: text=3、左肺下叶小空泡病灶，较前增多，壁增厚；, bbox=[112, 682, 487, 696]
2026-08-10 19:01:48,355 INFO     29 [qwen-vl-text] coord item[28]: text=4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；, bbox=[112, 694, 593, 707]
2026-08-10 19:01:48,355 INFO     29 [qwen-vl-text] coord item[29]: text=5、双肺炎性病变，较前相仿；, bbox=[112, 707, 359, 720]
2026-08-10 19:01:48,355 INFO     29 [qwen-vl-text] coord item[30]: text=6、左侧第6肋骨顺位欠佳；, bbox=[112, 719, 331, 732]
2026-08-10 19:01:48,355 INFO     29 [qwen-vl-text] coord item[31]: text=7、提示左侧肾上腺结节，较前大致相仿；, bbox=[112, 729, 450, 743]
2026-08-10 19:01:48,355 INFO     29 [qwen-vl-text] coord item[32]: text=请结合临床、病史及其它相关检查。, bbox=[114, 740, 407, 754]
2026-08-10 19:01:48,356 INFO     29 [qwen-vl-text] page=17 — 33/33 coords, api_time=19.5s
2026-08-10 19:01:48,356 INFO     29 [qwen-vl-text] new_positions (33):
[[17, 413.64000000000004, 729.0, 547.1999999999999, 600.9599999999999], [17, 462.24, 672.84, 616.3199999999999, 656.64], [17, 108.0, 184.68, 696.9599999999999, 720.0], [17, 225.72000000000003, 237.60000000000002, 698.88, 720.0], [17, 754.9200000000001, 893.1600000000001, 704.64, 729.6], [17, 108.0, 184.68, 735.36, 760.3199999999999], [17, 225.72000000000003, 247.32000000000002, 737.28, 760.3199999999999], [17, 398.52000000000004, 491.40000000000003, 739.1999999999999, 764.16], [17, 590.76, 689.0400000000001, 743.04, 766.0799999999999], [17, 753.84, 879.12, 744.9599999999999, 768.0], [17, 108.0, 270.0, 775.68, 800.64], [17, 398.52000000000004, 469.8, 777.6, 800.64], [17, 590.76, 640.44, 781.4399999999999, 802.56], [17, 753.84, 1031.4, 781.4399999999999, 804.48], [17, 855.36, 895.32, 802.56, 825.6], [17, 111.24000000000001, 208.44000000000003, 821.76, 844.8], [17, 239.76000000000002, 376.92, 821.76, 846.7199999999999], [17, 582.12, 881.2800000000001, 825.6, 848.64], [17, 115.56, 212.76000000000002, 860.16, 883.1999999999999], [17, 111.24000000000001, 1020.6, 885.12, 908.16], [17, 111.24000000000001, 1019.5200000000001, 906.24, 931.1999999999999], [17, 111.24000000000001, 1019.5200000000001, 929.28, 954.24], [17, 111.24000000000001, 1027.0800000000002, 952.3199999999999, 977.28], [17, 113.4, 210.60000000000002, 979.1999999999999, 1000.3199999999999], [17, 125.28, 219.24, 1238.3999999999999, 1261.44], [17, 120.96000000000001, 563.76, 1263.36, 1288.32], [17, 120.96000000000001, 367.20000000000005, 1288.32, 1313.28], [17, 120.96000000000001, 525.96, 1309.44, 1336.32], [17, 120.96000000000001, 640.44, 1332.48, 1357.44], [17, 120.96000000000001, 387.72, 1357.44, 1382.3999999999999], [17, 120.96000000000001, 357.48, 1380.48, 1405.44], [17, 120.96000000000001, 486.00000000000006, 1399.6799999999998, 1426.56], [17, 123.12, 439.56, 1420.8, 1447.6799999999998]]
2026-08-10 19:01:48,356 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=29.3s
2026-08-10 19:01:48,356 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:01:48,359 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:01:48,359 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:01:48,359 INFO     29 [qwen-vl-text] positions(28): [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:01:48,359 INFO     29 [qwen-vl-text] page grouping: [18], lines per page: [28]
2026-08-10 19:01:48,759 INFO     29 [qwen-vl-text] page=18, rect=1080x1920, img=(3000x5334), dpi=200
2026-08-10 19:01:48,761 INFO     29 [qwen-vl-text] LLM extraction start, text_len=479
2026-08-10 19:01:48,762 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:01:48,762 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 657, \"bbox_end\": 684, \"encounter_dates\": [\"2025-11-05\"], \"department\": \"血液内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CT检查报告单\n病人ID:\n姓名:\n性别:女\n年龄:57岁\n检查编号:CTC\n病人来源:门诊\n住院号:\n床号:\n检查类型:CT\n申请科室:血液内科门诊\n检查部位:胸部平扫(CT)\n检查时间:2025-11-05 09:32:29\n影像所见:\n左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两\n肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片\n状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见\n明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显\n破坏征象。\n影像诊断:\n1、肺癌治疗后改变，对比2025-08-27片病变范围增大；\n2、双肺局限性支气管扩张；\n3、左肺下叶小空泡病灶，较前增多，壁增厚；\n4、两肺多发微、小结节，考虑转移瘤，较前明显增多、增大；\n5、双肺炎性病变，较前病变增多；\n6、左侧第6肋骨顺位欠佳；\n7、提示左侧肾上腺结节，较前大致相仿；\n请结合临床、病史及其它相关检查。",
    "role": "user"
  }
]
2026-08-10 19:01:51,886 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:01:51.886+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:01:59,296 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:01:59,296 INFO     29 [qwen-vl-text] LLM output (len=662):
{
  "exam_date": "2025-11-05",
  "report_date": null,
  "exam_name": "胸部平扫(CT)",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "血液内科门诊",
  "bed_number": null,
  "findings": "左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。",
  "conclusion": "1、肺癌治疗后改变，对比2025-08-27片病变范围增大；\n2、双肺局限性支气管扩张；\n3、左肺下叶小空泡病灶，较前增多，壁增厚；\n4、两肺多发微、小结节，考虑转移瘤，较前明显增多、增大；\n5、双肺炎性病变，较前病变增多；\n6、左侧第6肋骨顺位欠佳；\n7、提示左侧肾上腺结节，较前大致相仿；\n请结合临床、病史及其它相关检查。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:01:59,304 INFO     29 [qwen-vl-text] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3608642, prompt_len=1176
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["CT检查报告单", "病人ID:", "姓名:", "性别:女", "年龄:57岁", "检查编号:CTC", "病人来源:门诊", "住院号:", "床号:", "检查类型:CT", "申请科室:血液内科门诊", "检查部位:胸部平扫(CT)", "检查时间:2025-11-05 09:32:29", "影像所见:", "左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两", "肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片", "状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见", "明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显", "破坏征象。", "影像诊断:", "1、肺癌治疗后改变，对比2025-08-27片病变范围增大；", "2、双肺局限性支气管扩张；", "3、左肺下叶小空泡病灶，较前增多，壁增厚；", "4、两肺多发微、小结节，考虑转移瘤，较前明显增多、增大；", "5、双肺炎性病变，较前病变增多；", "6、左侧第6肋骨顺位欠佳；", "7、提示左侧肾上腺结节，较前大致相仿；", "请结合临床、病史及其它相关检查。"]

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
2026-08-10 19:02:17,675 INFO     29 [qwen-vl-text] coord API raw response (len=1714):
[
	{"text": "CT检查报告单", "bbox": [436, 309, 630, 332]},
	{"text": "病人ID:", "bbox": [109, 353, 180, 366]},
	{"text": "姓名:", "bbox": [109, 372, 180, 386]},
	{"text": "性别:女", "bbox": [377, 374, 462, 388]},
	{"text": "年龄:57岁", "bbox": [554, 376, 645, 389]},
	{"text": "检查编号:CTC", "bbox": [704, 357, 828, 369]},
	{"text": "病人来源:门诊", "bbox": [111, 393, 260, 406]},
	{"text": "住院号:", "bbox": [377, 395, 444, 407]},
	{"text": "床号:", "bbox": [554, 396, 600, 408]},
	{"text": "检查类型:CT", "bbox": [704, 377, 819, 389]},
	{"text": "申请科室:血液内科门诊", "bbox": [704, 396, 906, 408]},
	{"text": "检查部位:胸部平扫(CT)", "bbox": [111, 413, 358, 426]},
	{"text": "检查时间:2025-11-05 09:32:29", "bbox": [546, 414, 820, 426]},
	{"text": "影像所见:", "bbox": [118, 433, 207, 445]},
	{"text": "左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两", "bbox": [118, 445, 948, 458]},
	{"text": "肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片", "bbox": [117, 457, 947, 470]},
	{"text": "状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见", "bbox": [117, 469, 947, 482]},
	{"text": "明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显", "bbox": [117, 480, 954, 493]},
	{"text": "破坏征象。", "bbox": [117, 493, 205, 506]},
	{"text": "影像诊断:", "bbox": [130, 627, 216, 639]},
	{"text": "1、肺癌治疗后改变，对比2025-08-27片病变范围增大；", "bbox": [127, 639, 565, 653]},
	{"text": "2、双肺局限性支气管扩张；", "bbox": [127, 652, 350, 666]},
	{"text": "3、左肺下叶小空泡病灶，较前增多，壁增厚；", "bbox": [127, 664, 494, 678]},
	{"text": "4、两肺多发微、小结节，考虑转移瘤，较前明显增多、增大；", "bbox": [127, 675, 618, 689]},
	{"text": "5、双肺炎性病变，较前病变增多；", "bbox": [127, 688, 405, 701]},
	{"text": "6、左侧第6肋骨顺位欠佳；", "bbox": [127, 700, 342, 713]},
	{"text": "7、提示左侧肾上腺结节，较前大致相仿；", "bbox": [127, 710, 458, 724]},
	{"text": "请结合临床、病史及其它相关检查。", "bbox": [130, 722, 415, 735]}
]
2026-08-10 19:02:17,675 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=18.4s
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[0]: text=CT检查报告单, bbox=[436, 309, 630, 332]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[1]: text=病人ID:, bbox=[109, 353, 180, 366]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[109, 372, 180, 386]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[377, 374, 462, 388]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[4]: text=年龄:57岁, bbox=[554, 376, 645, 389]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[5]: text=检查编号:CTC, bbox=[704, 357, 828, 369]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[6]: text=病人来源:门诊, bbox=[111, 393, 260, 406]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[7]: text=住院号:, bbox=[377, 395, 444, 407]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[8]: text=床号:, bbox=[554, 396, 600, 408]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[9]: text=检查类型:CT, bbox=[704, 377, 819, 389]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[10]: text=申请科室:血液内科门诊, bbox=[704, 396, 906, 408]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位:胸部平扫(CT), bbox=[111, 413, 358, 426]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[12]: text=检查时间:2025-11-05 09:32:29, bbox=[546, 414, 820, 426]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[13]: text=影像所见:, bbox=[118, 433, 207, 445]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[14]: text=左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两, bbox=[118, 445, 948, 458]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[15]: text=肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片, bbox=[117, 457, 947, 470]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[16]: text=状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见, bbox=[117, 469, 947, 482]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[17]: text=明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显, bbox=[117, 480, 954, 493]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[18]: text=破坏征象。, bbox=[117, 493, 205, 506]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[19]: text=影像诊断:, bbox=[130, 627, 216, 639]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[20]: text=1、肺癌治疗后改变，对比2025-08-27片病变范围增大；, bbox=[127, 639, 565, 653]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[21]: text=2、双肺局限性支气管扩张；, bbox=[127, 652, 350, 666]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[22]: text=3、左肺下叶小空泡病灶，较前增多，壁增厚；, bbox=[127, 664, 494, 678]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[23]: text=4、两肺多发微、小结节，考虑转移瘤，较前明显增多、增大；, bbox=[127, 675, 618, 689]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[24]: text=5、双肺炎性病变，较前病变增多；, bbox=[127, 688, 405, 701]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[25]: text=6、左侧第6肋骨顺位欠佳；, bbox=[127, 700, 342, 713]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[26]: text=7、提示左侧肾上腺结节，较前大致相仿；, bbox=[127, 710, 458, 724]
2026-08-10 19:02:17,676 INFO     29 [qwen-vl-text] coord item[27]: text=请结合临床、病史及其它相关检查。, bbox=[130, 722, 415, 735]
2026-08-10 19:02:17,677 INFO     29 [qwen-vl-text] page=18 — 28/28 coords, api_time=18.4s
2026-08-10 19:02:17,677 INFO     29 [qwen-vl-text] new_positions (28):
[[18, 470.88000000000005, 680.4000000000001, 593.28, 637.4399999999999], [18, 117.72000000000001, 194.4, 677.76, 702.72], [18, 117.72000000000001, 194.4, 714.24, 741.12], [18, 407.16, 498.96000000000004, 718.0799999999999, 744.9599999999999], [18, 598.32, 696.6, 721.92, 746.88], [18, 760.32, 894.24, 685.4399999999999, 708.48], [18, 119.88000000000001, 280.8, 754.56, 779.52], [18, 407.16, 479.52000000000004, 758.4, 781.4399999999999], [18, 598.32, 648.0, 760.3199999999999, 783.36], [18, 760.32, 884.5200000000001, 723.8399999999999, 746.88], [18, 760.32, 978.48, 760.3199999999999, 783.36], [18, 119.88000000000001, 386.64000000000004, 792.9599999999999, 817.92], [18, 589.6800000000001, 885.6, 794.88, 817.92], [18, 127.44000000000001, 223.56, 831.36, 854.4], [18, 127.44000000000001, 1023.84, 854.4, 879.36], [18, 126.36000000000001, 1022.7600000000001, 877.4399999999999, 902.4], [18, 126.36000000000001, 1022.7600000000001, 900.48, 925.4399999999999], [18, 126.36000000000001, 1030.3200000000002, 921.5999999999999, 946.56], [18, 126.36000000000001, 221.4, 946.56, 971.52], [18, 140.4, 233.28000000000003, 1203.84, 1226.8799999999999], [18, 137.16, 610.2, 1226.8799999999999, 1253.76], [18, 137.16, 378.0, 1251.84, 1278.72], [18, 137.16, 533.52, 1274.8799999999999, 1301.76], [18, 137.16, 667.44, 1296.0, 1322.8799999999999], [18, 137.16, 437.40000000000003, 1320.96, 1345.9199999999998], [18, 137.16, 369.36, 1344.0, 1368.96], [18, 137.16, 494.64000000000004, 1363.2, 1390.08], [18, 140.4, 448.20000000000005, 1386.24, 1411.2]]
2026-08-10 19:02:17,677 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=29.3s
2026-08-10 19:02:17,690 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 19:02:17,690 INFO     29 [Trace] task=ffaf4fc0 | doc=10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf | Extractor:ExaminationReport | outputs={"chunks": "6 items, types={'ExaminationReport': 6}", "html": "", "json": "958 items", "markdown": "", "text": "", "name": "10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 2, \"chunks_LabExam\": 13}"}
2026-08-10 19:02:17,690 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 19:02:17,697 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:17,697 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:02:17,701 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:17,702 INFO     29 [qwen-vl-table] page=15 LLM output (len=6076):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": "ALT",
      "value": "13",
      "unit": "U/L",
      "reference_range": "7-40",
      "abnormal": false
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": "AST",
      "value": "15",
      "unit": "U/L",
      "reference_range": "13-35",
      "abnormal": false
    },
    {
      "name": "谷氨酸脱氢酶",
      "item_code": "GLDH",
      "value": "5.7",
      "unit": "U/L",
      "reference_range": "<7.4",
      "abnormal": false
    },
    {
      "name": "γ-谷丙酰基转肽酶",
      "item_code": "GGT",
      "value": "15",
      "unit": "U/L",
      "reference_range": "7-45",
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "AKP",
      "value": "93",
      "unit": "U/L",
      "reference_range": "50-135",
      "abnormal": false
    },
    {
      "name": "腺苷脱氨酶",
      "item_code": "ADA",
      "value": "8",
      "unit": "U/L",
      "reference_range": "4-18",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "8.2",
      "unit": "μmol/L",
      "reference_range": "5.0-21.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "2.6",
      "unit": "μmol/L",
      "reference_range": "<6.0",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "5.6",
      "unit": "μmol/L",
      "reference_range": "2.0-15.0",
      "abnormal": false
    },
    {
      "name": "前白蛋白",
      "item_code": "PA",
      "value": "30.2",
      "unit": "mg/dl",
      "reference_range": "17.0-40.0",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "75.4",
      "unit": "g/L",
      "reference_range": "60.0-85.0",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "48.6",
      "unit": "g/L",
      "reference_range": "40.0-55.0",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLB",
      "value": "26.8",
      "unit": "g/L",
      "reference_range": "20.0-40.0",
      "abnormal": false
    },
    {
      "name": "白/球比例",
      "item_code": "A/G",
      "value": "1.81",
      "unit": null,
      "reference_range": "1.2-2.4",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": "TBA",
      "value": "1.3",
      "unit": "μmol/L",
      "reference_range": "<15.0",
      "abnormal": false
    },
    {
      "name": "总胆固醇",
      "item_code": "Cho",
      "value": "7.28",
      "unit": "mmol/L",
      "reference_range": "2.80-6.00",
      "abnormal": true
    },
    {
      "name": "高密度脂蛋白胆固醇",
      "item_code": "HDL-C",
      "value": "1.78",
      "unit": "mmol/L",
      "reference_range": "0.80-2.00",
      "abnormal": false
    },
    {
      "name": "低密度脂蛋白胆固醇",
      "item_code": "LDL-C",
      "value": "4.89",
      "unit": "mmol/L",
      "reference_range": "1.00-3.37",
      "abnormal": true
    },
    {
      "name": "小而密低密度脂蛋白",
      "item_code": "sdLDL",
      "value": "2.01",
      "unit": "mmol/L",
      "reference_range": "0.25-1.17",
      "abnormal": true
    },
    {
      "name": "血清载脂蛋白A1",
      "item_code": "APOA1",
      "value": "1.96",
      "unit": "g/L",
      "reference_range": "1.00-1.60",
      "abnormal": true
    },
    {
      "name": "血清载脂蛋白B",
      "item_code": "APOB",
      "value": "1.53",
      "unit": "g/L",
      "reference_range": "0.60-1.00",
      "abnormal": true
    },
    {
      "name": "甘油三酯",
      "item_code": "TG",
      "value": "2.30",
      "unit": "mmol/L",
      "reference_range": "0.30-1.70",
      "abnormal": true
    },
    {
      "name": "脂蛋白a",
      "item_code": "LP(a)",
      "value": "9.70",
      "unit": "nmol/L",
      "reference_range": "<75.00",
      "abnormal": false
    },
    {
      "name": "游离脂肪酸",
      "item_code": "NEFA",
      "value": "125.0",
      "unit": "umol/dl",
      "reference_range": "10.0-85.0",
      "abnormal": true
    },
    {
      "name": "脂蛋白磷脂酶A2",
      "item_code": "PLA2",
      "value": "728",
      "unit": "U/L",
      "reference_range": "<659",
      "abnormal": true
    },
    {
      "name": "尿素",
      "item_code": "Urea",
      "value": "3.59",
      "unit": "mmol/L",
      "reference_range": "2.30-7.80",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": "Cr",
      "value": "38",
      "unit": "μmol/L",
      "reference_range": "53-97",
      "abnormal": true
    },
    {
      "name": "胱抑素C",
      "item_code": "Cys-C",
      "value": "0.76",
      "unit": "mg/L",
      "reference_range": "0.51-1.09",
      "abnormal": false
    },
    {
      "name": "肾小球滤过率",
      "item_code": "eGFR",
      "value": "108.600",
      "unit": "ml/min",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "4.23",
      "unit": "mmol/L",
      "reference_range": "3.50-5.30",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "NA",
      "value": "139",
      "unit": "mmol/L",
      "reference_range": "137-147",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "CL",
      "value": "104",
      "unit": "mmol/L",
      "reference_range": "99-110",
      "abnormal": false
    },
    {
      "name": "二氧化碳结合力",
      "item_code": "CO2",
      "value": "21.5",
      "unit": "mmol/L",
      "reference_range": "18.0-28.0",
      "abnormal": false
    },
    {
      "name": "钙",
      "item_code": "Ca",
      "value": "2.36",
      "unit": "mmol/L",
      "reference_range": "2.11-2.52",
      "abnormal": false
    },
    {
      "name": "磷",
      "item_code": "P",
      "value": "1.21",
      "unit": "mmol/L",
      "reference_range": "0.60-1.60",
      "abnormal": false
    },
    {
      "name": "镁",
      "item_code": "Mg",
      "value": "0.86",
      "unit": "mmol/L",
      "reference_range": "0.65-1.10",
      "abnormal": false
    }
  ]
}
2026-08-10 19:02:17,702 INFO     29 [qwen-vl-table] coord grouping: {15: 36}
2026-08-10 19:02:17,721 INFO     29 [qwen-vl-table] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4100183, prompt_len=715
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
丙氨酸氨基转移酶、天门冬氨酸氨基转移酶、谷氨酸脱氢酶、γ-谷丙酰基转肽酶、碱性磷酸酶、腺苷脱氨酶、总胆红素、直接胆红素、间接胆红素、前白蛋白、总蛋白、白蛋白、球蛋白、白/球比例、总胆汁酸、总胆固醇、高密度脂蛋白胆固醇、低密度脂蛋白胆固醇、小而密低密度脂蛋白、血清载脂蛋白A1、血清载脂蛋白B、甘油三酯、脂蛋白a、游离脂肪酸、脂蛋白磷脂酶A2、尿素、肌酐、胱抑素C、肾小球滤过率、钾、钠、氯、二氧化碳结合力、钙、磷、镁

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
2026-08-10 19:02:26,408 INFO     29 [qwen-vl-table] coord API raw response (len=1753):
[
	{"text": "丙氨酸氨基转移酶", "bbox": [58, 117, 216, 132]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [58, 134, 248, 148]},
	{"text": "谷氨酸脱氢酶", "bbox": [58, 150, 156, 165]},
	{"text": "γ-谷丙酰基转肽酶", "bbox": [58, 167, 223, 182]},
	{"text": "碱性磷酸酶", "bbox": [58, 184, 156, 199]},
	{"text": "腺苷脱氨酶", "bbox": [58, 201, 140, 215]},
	{"text": "总胆红素", "bbox": [58, 217, 147, 232]},
	{"text": "直接胆红素", "bbox": [58, 234, 147, 249]},
	{"text": "间接胆红素", "bbox": [58, 251, 138, 266]},
	{"text": "前白蛋白", "bbox": [58, 268, 130, 283]},
	{"text": "总蛋白", "bbox": [58, 285, 130, 300]},
	{"text": "白蛋白", "bbox": [58, 302, 128, 317]},
	{"text": "球蛋白", "bbox": [58, 319, 105, 334]},
	{"text": "白/球比例", "bbox": [58, 336, 130, 351]},
	{"text": "总胆汁酸", "bbox": [58, 353, 123, 368]},
	{"text": "总胆固醇", "bbox": [58, 370, 147, 385]},
	{"text": "高密度脂蛋白胆固醇", "bbox": [58, 387, 230, 402]},
	{"text": "低密度脂蛋白胆固醇", "bbox": [58, 404, 230, 419]},
	{"text": "小而密低密度脂蛋白", "bbox": [58, 421, 203, 436]},
	{"text": "血清载脂蛋白A1", "bbox": [58, 438, 177, 453]},
	{"text": "血清载脂蛋白B", "bbox": [58, 455, 171, 470]},
	{"text": "甘油三酯", "bbox": [58, 472, 147, 487]},
	{"text": "脂蛋白a", "bbox": [58, 489, 113, 504]},
	{"text": "游离脂肪酸", "bbox": [58, 506, 138, 521]},
	{"text": "脂蛋白磷脂酶A2", "bbox": [58, 523, 171, 538]},
	{"text": "尿素", "bbox": [58, 540, 113, 555]},
	{"text": "肌酐", "bbox": [58, 557, 113, 572]},
	{"text": "胱抑素C", "bbox": [58, 574, 121, 589]},
	{"text": "肾小球滤过率", "bbox": [58, 591, 154, 606]},
	{"text": "钾", "bbox": [58, 608, 97, 623]},
	{"text": "钠", "bbox": [58, 625, 97, 640]},
	{"text": "氯", "bbox": [58, 642, 97, 657]},
	{"text": "二氧化碳结合力", "bbox": [58, 659, 171, 674]},
	{"text": "钙", "bbox": [58, 676, 97, 691]},
	{"text": "磷", "bbox": [58, 693, 89, 708]},
	{"text": "镁", "bbox": [58, 710, 82, 725]}
]
2026-08-10 19:02:26,408 INFO     29 [qwen-vl-table] coord API: raw_items=36, valid_items=36, elapsed=8.7s
2026-08-10 19:02:26,408 INFO     29 [qwen-vl-table] coord item[0]: text=丙氨酸氨基转移酶, bbox=[58, 117, 216, 132]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[1]: text=天门冬氨酸氨基转移酶, bbox=[58, 134, 248, 148]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[2]: text=谷氨酸脱氢酶, bbox=[58, 150, 156, 165]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[3]: text=γ-谷丙酰基转肽酶, bbox=[58, 167, 223, 182]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[4]: text=碱性磷酸酶, bbox=[58, 184, 156, 199]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[5]: text=腺苷脱氨酶, bbox=[58, 201, 140, 215]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[6]: text=总胆红素, bbox=[58, 217, 147, 232]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[7]: text=直接胆红素, bbox=[58, 234, 147, 249]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[8]: text=间接胆红素, bbox=[58, 251, 138, 266]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[9]: text=前白蛋白, bbox=[58, 268, 130, 283]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[10]: text=总蛋白, bbox=[58, 285, 130, 300]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[11]: text=白蛋白, bbox=[58, 302, 128, 317]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[12]: text=球蛋白, bbox=[58, 319, 105, 334]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[13]: text=白/球比例, bbox=[58, 336, 130, 351]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[14]: text=总胆汁酸, bbox=[58, 353, 123, 368]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[15]: text=总胆固醇, bbox=[58, 370, 147, 385]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[16]: text=高密度脂蛋白胆固醇, bbox=[58, 387, 230, 402]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[17]: text=低密度脂蛋白胆固醇, bbox=[58, 404, 230, 419]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[18]: text=小而密低密度脂蛋白, bbox=[58, 421, 203, 436]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[19]: text=血清载脂蛋白A1, bbox=[58, 438, 177, 453]
2026-08-10 19:02:26,409 INFO     29 [qwen-vl-table] coord item[20]: text=血清载脂蛋白B, bbox=[58, 455, 171, 470]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[21]: text=甘油三酯, bbox=[58, 472, 147, 487]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[22]: text=脂蛋白a, bbox=[58, 489, 113, 504]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[23]: text=游离脂肪酸, bbox=[58, 506, 138, 521]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[24]: text=脂蛋白磷脂酶A2, bbox=[58, 523, 171, 538]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[25]: text=尿素, bbox=[58, 540, 113, 555]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[26]: text=肌酐, bbox=[58, 557, 113, 572]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[27]: text=胱抑素C, bbox=[58, 574, 121, 589]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[28]: text=肾小球滤过率, bbox=[58, 591, 154, 606]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[29]: text=钾, bbox=[58, 608, 97, 623]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[30]: text=钠, bbox=[58, 625, 97, 640]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[31]: text=氯, bbox=[58, 642, 97, 657]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[32]: text=二氧化碳结合力, bbox=[58, 659, 171, 674]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[33]: text=钙, bbox=[58, 676, 97, 691]
2026-08-10 19:02:26,410 INFO     29 [qwen-vl-table] coord item[34]: text=磷, bbox=[58, 693, 89, 708]
2026-08-10 19:02:26,411 INFO     29 [qwen-vl-table] coord item[35]: text=镁, bbox=[58, 710, 82, 725]
2026-08-10 19:02:26,411 INFO     29 [qwen-vl-table] page=15 coord: matched 36/36, time=8.7s
2026-08-10 19:02:26,412 INFO     29 [qwen-vl-table] new_positions (36):
[[16, 23.779999999999998, 88.55999999999999, 62.478, 70.488], [16, 23.779999999999998, 101.67999999999999, 71.556, 79.03200000000001], [16, 23.779999999999998, 63.959999999999994, 80.10000000000001, 88.11], [16, 23.779999999999998, 91.42999999999999, 89.17800000000001, 97.188], [16, 23.779999999999998, 63.959999999999994, 98.256, 106.266], [16, 23.779999999999998, 57.4, 107.334, 114.81], [16, 23.779999999999998, 60.269999999999996, 115.878, 123.888], [16, 23.779999999999998, 60.269999999999996, 124.956, 132.966], [16, 23.779999999999998, 56.58, 134.03400000000002, 142.044], [16, 23.779999999999998, 53.3, 143.112, 151.122], [16, 23.779999999999998, 53.3, 152.19, 160.20000000000002], [16, 23.779999999999998, 52.48, 161.268, 169.27800000000002], [16, 23.779999999999998, 43.05, 170.346, 178.35600000000002], [16, 23.779999999999998, 53.3, 179.424, 187.434], [16, 23.779999999999998, 50.43, 188.502, 196.512], [16, 23.779999999999998, 60.269999999999996, 197.58, 205.59], [16, 23.779999999999998, 94.3, 206.65800000000002, 214.668], [16, 23.779999999999998, 94.3, 215.73600000000002, 223.746], [16, 23.779999999999998, 83.22999999999999, 224.81400000000002, 232.824], [16, 23.779999999999998, 72.57, 233.89200000000002, 241.90200000000002], [16, 23.779999999999998, 70.11, 242.97000000000003, 250.98000000000002], [16, 23.779999999999998, 60.269999999999996, 252.048, 260.058], [16, 23.779999999999998, 46.33, 261.12600000000003, 269.136], [16, 23.779999999999998, 56.58, 270.204, 278.214], [16, 23.779999999999998, 70.11, 279.28200000000004, 287.29200000000003], [16, 23.779999999999998, 46.33, 288.36, 296.37], [16, 23.779999999999998, 46.33, 297.43800000000005, 305.44800000000004], [16, 23.779999999999998, 49.61, 306.516, 314.526], [16, 23.779999999999998, 63.13999999999999, 315.594, 323.60400000000004], [16, 23.779999999999998, 39.769999999999996, 324.672, 332.682], [16, 23.779999999999998, 39.769999999999996, 333.75, 341.76], [16, 23.779999999999998, 39.769999999999996, 342.82800000000003, 350.838], [16, 23.779999999999998, 70.11, 351.906, 359.916], [16, 23.779999999999998, 39.769999999999996, 360.98400000000004, 368.994], [16, 23.779999999999998, 36.489999999999995, 370.062, 378.072], [16, 23.779999999999998, 33.62, 379.14000000000004, 387.15000000000003]]
2026-08-10 19:02:26,412 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=36, matched=36, pages=1, time=88.3s
2026-08-10 19:02:26,414 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:02:26,415 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:02:26,415 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[16]
2026-08-10 19:02:26,415 INFO     29 [qwen-vl-table] positions ： [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:02:26,676 INFO     29 [qwen-vl-table] page=16, rect=410x566, img=(1139x1573)
2026-08-10 19:02:26,677 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:26,677 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 611, \"bbox_end\": 621, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllllll}\n报告时间: 2026-03-10\n\\hline\nNO & 项目 & 代码 & 结果 & 提示 & 参考区间 & 单位 & 检测仪器 & 检测方法 \\\\\n\\hline\n1 & *★甲胎蛋白 & AFP & 3.41 & & 0.00-7.00 & ng/ml & Roche\\_4 & 电化学发光 \\\\\n2 & *★癌胚抗原 & CEA & 3.52 & & 0.00-5.00 & ng/ml & Roche\\_4 & 电化学发光 \\\\\n3 & 非小细胞肺癌相关抗原 & CYFRA21-1 & 1.70 & & 0.00-3.30 & ng/ml & Roche\\_4 & 电化学发光 \\\\\n4 & 神经元特异性烯醇化酶 & NSE & 16.60 & 1 & 0.00-16.30 & ng/ml & Roche\\_4 & 电化学发光 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:02:26,832 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:02:26.830+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 9, "lag": 0, "done": 87, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "ffaf4fc094ea11f1bd9827cf206dfa2d": {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:02:27,575 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:27,583 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 19:02:27,583 INFO     29 [Trace] task=ffaf4fc0 | doc=10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "958 items", "markdown": "", "text": "", "name": "10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 2, \"chunks_LabExam\": 13}"}
2026-08-10 19:02:27,583 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 19:02:27,585 INFO     29 [ChunkMerger] Merged 23 chunks from 9 sources: {'Extractor:LabExam': 13, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 2, 'Extractor:Admission': 2, 'Extractor:ExaminationReport': 6, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 19:02:27,594 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 19:02:27,594 INFO     29 [Trace] task=ffaf4fc0 | doc=10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "23 items, types={'LabReport': 13, 'DischargeRecord': 2, 'AdmissionRecord': 2, 'ExaminationReport': 6}", "name": "10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf"}
2026-08-10 19:02:27,594 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 19:02:28,510 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786388202640, 'update_date': datetime.datetime(2026, 8, 10, 18, 56, 42), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1360893, 'status': '1'}
2026-08-10 19:02:28,755 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   血管内皮生长因子  VEGF  179.44  pg/ml  0-160pg/ml：肿瘤安全期。160-400pg/ml：有肿瘤风险。>400pg/ml：有肿瘤重度风险。  True   
---
   谷丙转氨酶  ALT  19  U/L  7—40  False    谷草转氨酶  AST  39  U/L  13—35  True    谷草/谷丙比值  AST/ALT  2.05  None  None  False    总蛋白  TP  63.0  g/L  65—87  True    白蛋白  ALB  26.3  g/L  40—55  True    球蛋白  GLOB  36.7  g/L  20—40  False    白球比  A/G  0.72  None  1.2—2.4  True    前白蛋白  PA  81  mg/L  150—380  True    碱性磷酸酶  ALP  238  U/L  50—135  True    谷氨酰转肽酶  GGT  30  U/L  7—45  False    总胆红素  TBIL  7.0  umol/L  3.42—23.5  False    总胆汁酸  TBA  1.6  umol/L  0—10  False    胆碱酯酶  CHE  3942  U/L  5100—11700  True    直接胆红素  DBIL  3.1  umol/L  0—8.0  False    间接胆红素  IBIL  3.9  umol/L  ≤17  False    葡萄糖  GLU  4.66  mmol/L  3.89—6.11  False    甘油三酯  TG  0.97  mmol/L  0.34—1.7  False    血清总胆固醇  TCHOL  2.99  mmol/L  3.1—5.17  True   
---
   高密度脂蛋白胆固醇  HDL-C  0.81  mmol/L  1.10-1.74  True    低密度脂蛋白胆固醇  LDL-C  1.60  mmol/L  健康人群 <3.4mmol/L; 中高危人群 <2.6mmol/L; 极高危人群 <1.8mmol/L; 超高危人群 <1.4mmol/L  False    非高密度脂蛋白胆固醇  非HDL-C  2.18  mmol/L  健康人群 <4.1mmol/L; 中高危人群 <3.4mmol/L; 极高危人群 <2.6mmol/L; 超高危人群 <2.2mmol/L  False    尿素  UREA  3.81  mmol/L  2.6-7.5  False    肌酐  CREA  51.7  umol/L  41-73  False    估算肾小球滤过率  eGRF  102.34  ml/min  ≥70  False    尿酸  UA  305  umol/L  155-357  False    肌酸激酶  CK  49  U/L  40-200  False    肌酸激酶同工酶  CK-MB  11  None  None  False    乳酸脱氢酶  LDH  321  None  None  False    钾  K  4.58  mmol/L  3.5-5.3  False    钠  NA  133.1  mmol/L  137-147  True   
---
   *氯  CL  98.4  mmol/L  99-110  True    *钙  CA  2.03  mmol/L  2.11-2.52  True   
---
   促甲状腺激素  TSH  4.60  mIU/L  0.75—5.60  False    三碘甲状腺原氨酸  T3  1.93  nmol/L  1.30—2.40  False    甲状腺素  T4  113.60  nmol/L  70.0—140.0  False    游离三碘甲状腺原氨酸  FT3  3.29  pmol/L  3.10—6.80  False    游离甲状腺素  FT4  19.01  pmol/L  12.80—21.3  False    *癌胚抗原  CEA  3.84  ng/mL  0—4.7  False    细胞角蛋白19片段21-1  CYFRA  15.22  ng/mL  0—3.3  True    神经元特异性烯醇化酶测定  NSE  52.84  ng/mL  0—16.3  True   
---
   颜色  F-YS  黄褐色  None  黄色  True    性状  F-XZ  软便  None  软  True    隐血  FOB(M)  -  None  阴性  False    隐血  FOB(H)  -  None  阴性  False    红细胞  F-HXB  未见  个/HP  未见  False    白细胞  F-BXB  未见  个/HP  0-1  False    吞噬细胞  TSXB  未见  个/HP  未见  False    脂肪球  F-ZFQ  未见  个/HP  未见  False    真菌  ZJ  未见  个/HP  未见  False    虫卵  F-CL  未见  None  未见  False    寄生虫  JSC  未见  None  未见  False    结晶  JJ  未见  None  未见  False    滴虫  DC  未见  None  未见  False    淀粉颗粒  DFKL  未见  个/LP  未见  False   
---
   凝血因子功能  R  4.5  Min  4-9  False    纤维蛋白原功能  K  1.3  Min  1-3  False    纤维蛋白原功能  Angle  64.9  deg  53-72  False    血小板聚集功能  MA  59.4  mm  50-70  False    纤维蛋白溶解功能  LY30  0.0  %  0-8  False    预测纤溶指数  EPL  0.0  %  0-15  False    综合凝血指数  CI  1.0  None  -3-3  False   
---
   *葡萄糖  GLU  -  mmol/L  阴性 (-)  False    *尿潜血  BLD  -  None  阴性 (-)  False    *白细胞  LEU  1+  None  阴性 (-)  True    *蛋白质  PRO  -  g/L  阴性 (-)  False    *亚硝酸盐  NIT  -  umol/L  阴性 (-)  False    *尿胆原  URO  正常  umol/L  阴性 (-)  False    *胆红素  BIL  -  umol/L  阴性 (-)  False    *酮体  KET  -  mmol/L  阴性 (-)  False    *PH值  PH  6.0  None  5-7.5  False    *比重  SG  1.025  None  1.01-1.03  False    维生素C  ASC  >=5.7  mmol/L  <=0.4  True    红细胞  RBC  13  /ul  0-17  False    白细胞  WBC  99  /ul  0-28  True    白细胞团  WBCG  0  /ul  0-2  False    病理管型  UNCC  0  /LP  0-1  False    透明管型  HYAL  0  /LP  0-1  False    鳞状上皮细胞  SQEP  1  /ul  0-28  False    非鳞状上皮细胞  NSE  1  /ul  0-6  False    粘液丝  MUSC  292  /ul  0-28  True    未分类结晶  UNCX  97  /ul  0-28  True    细菌计数  BACT  24  /ul  0-7  True    酵母菌  BYST  0  /ul  0-1  False   
---
   N末端脑利钠肽前体  NT-proBNP  350.37  ng/L  1.急性心衰排除标准：<300 ng/L 2.心衰诊断：<50岁：>450 ng/L >50岁：>900 ng/L >75岁：>1800 ng/L 3.慢性心衰排除标准：<125ng/L  False   
---
   *白细胞数  WBC  4.70  10^9/L  3.5—9.5  False    *红细胞数  RBC  3.56  10^12/L  13.8—5.1  False    *血红蛋白浓度  HGB  117  g/L  115—150  False    *红细胞压积  HCT  33.90  %  135—45  False    *平均红细胞体积  MCV  95.2  fL  82—100  False    *平均红细胞血红蛋白含量  MCH  32.9  pg  27—34  False    *平均红细胞血红蛋白浓度  MCHC  345  g/L  316—354  False    *血小板  PLT  167  10^9/L  125—350  False    血小板压积  PCT  0.160  %  0.16—0.43  False    平均血小板体积  MPV  9.5  fL  9.1—12.1  False    血小板体积分布宽度  PDW  9.6  fL  9.6—15.2  False    中性粒细胞绝对值  NEUT#  3.56  10^9/L  1.8—6.3  False    淋巴细胞绝对值  LYMPH#  0.59  10^9/L  1.1—3.2  True    单核细胞绝对值  MONO#  0.28  10^9/L  0.1—1  False    嗜酸性粒细胞绝对值  E0#  0.24  10^9/L  0.02—0.52  False    嗜碱性粒细胞绝对值  BASO#  0.03  10^9/L  0—0.06  False    中性粒细胞百分比  NEUT%  None  None  None  False    淋巴细胞百分比  LYMPH%  None  None  None  False    单核细胞百分比  MONO%  None  None  None  False    嗜酸性粒细胞百分比  E0%  None  None  None  False    嗜碱性粒细胞百分比  BASO%  None  None  None  False    红细胞体积分布宽度CV  RDW-CV  None  None  None  False    红细胞体积分布宽度SD  RDW-SD  None  None  None  False    大血小板比率  P-LCR  None  None  None  False    *C反应蛋白  CRP  None  None  None  False   
---
   *高敏乙型肝炎病毒(HBV-DNA)定量  HBV-DNA  <2.00E+01  IU/ml  None  False   
---
   乙型肝炎病毒表面抗原  None  >250.000  IU/mL  0--0.05  True    丙型肝炎病毒IgG抗体  None  0.011阴性  S/CO  0--1  False    梅毒螺旋体特异抗体  None  0.02阴性  S/CO  0--1  False    人类免疫缺陷病毒抗体和抗原  None  0.031阴性  S/CO  0--1  False   
---
   明确/潜在临床意义的变异  None  BRAFp.V600E;BRAFp.D287H;EGFRp.L858R;EGFRp.C797S;EGFRp.R776H  None  None  True    临床意义不明的变异  None  1个  None  None  False    微卫星不稳定评估（MSI）  MSI  微卫星稳定型（MSS）  None  None  False    NGS质量控制评估结果  None  合格  None  None  False   
---
原阳县人民医院
出院记录
姓名：
科室：肿瘤内科病区 床号：3床 住院号：02
姓名：
性别：女
年龄：57岁
入院日期：2026-01-08 14:37
出院日期：2026-01-18 09:42
住院天数：10
入院情况：以“确诊肺恶性肿瘤2年余，再治疗。”为主诉入院。患者于2年余前（2023.06）患
者无明显诱因出现间断咳嗽、咳白色痰，伴有胸闷、纳差、乏力症状，活动后胸闷症状加重，于
我院门诊行胸部CT示：两肺多发异常密度病变，较2023-03-15老片病变范围增大，结合
2021-09-07片和2023-03-15片，注意警惕肺粘膜相关性淋巴瘤或肺炎型肺癌并两肺转移的可能
性，建议支气管镜活检病理学检查，给予支气管肺泡灌洗（2024.06.15）示：（肺灌洗液）镜下
见呼吸道上皮细胞、炎性细胞及组织细胞，另见少许异型细胞，呈腺样结构，不除外腺癌，请结
合临床及影像学。后至郑州大学第一附属医院确诊为肺腺癌（未见报告），具体不详，给予靶向
治疗初始为阿美替尼，后调整为伏美替尼（不详）；复查CT（2024.11.12）：1、肺癌治疗后改
变，对比2024-08-20片病变较前范围增大；2、左肺上叶下舌段及下叶后底段局限性支气管扩
张；3、两肺多发微、小结节，较前右肺中叶结节稍增大，余相仿；4、右肺中叶少许慢性炎症；
5、左侧第6肋骨顺位欠佳；6、提示左侧肾上腺结节，建议动态观察；请结合临床、病史及其它
相关检查。2024.11.16调整为贝福替尼靶向治疗，2024.12.12于郑州大学第一附属医院复查CT：
Dell
原阳县人民
费别：
姓名：
科室：
临床诊断：
Rp：
核对：
发药：
审核：
调配：
时24分病情：一般
费别：
住院天数：8
总费用：-VTE评分：3(低危)
出院科室
出院日期
出院诊断
住院号
患者姓名
经治医师
入院年龄
付费方式
病案质量
入院情
内科病区
2026-01-18 09:42...
02317135
贾振欣
57岁
城镇居民基本医疗保险
甲
一般
内科病区
2025-12-27 14:55...
02317135
贾振欣
57岁
城镇居民基本医疗保险
甲
一般
1·1·2·1·3·1·4·1·5·1·6·1·7·1·8·1·9·1·10·1·11·1·12·1·13·1·14·1·15·1·16·1·17·1·18·1·19·1·20·1·21
合临床及影像学。后至郑州大学第一附属医院确诊为肺腺癌(未见报告)，具体不详，给予靶向
治疗初始为阿美替尼，后调整为伏美替尼(不详)；复查CT(2024.11.12)：1、肺癌治疗后改
变，对比2024-08-20片病变较前范围增大；2、左肺上叶下舌段及下叶后底段局限性支气管扩
张；3、两肺多发微、小结节，较前右肺中叶结节稍增大，余相仿；4、右肺中叶少许慢性炎症；
5、左侧第6肋骨顺位欠佳；6、提示左侧肾上腺结节，建议动态观察；请结合临床、病史及其它
相关检查。2024.11.16调整为贝福替尼靶向治疗，2024.12.12于郑州大学第一附属医院复查CT：
1.左肺多发团片影；2.双肺炎症，较前减轻；3.双肺多发结节，较前部分增大；4.双侧胸膜局限
性增厚；5.左侧肾上腺内侧支结节，较前变化不大。给予抗感染及对症支持治疗后好转出院。
2025.5.7复查CT：、肺癌治疗后改变，对比2025-01-11片病变较前增大；2、双肺局限性支气管
扩张；3、左肺下叶空腔病灶，较前增大；4、两肺多发微、小结节，建议动态观察；5、双肺炎
性病变；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，对比较前相仿；请结合临床、病史及
其它相关检查。综合评估患者病情进展，与患者及家属沟通后，排除禁忌症后，2025.5.15,
2025.6.14给予AP方案化疗2周期，过程顺利。基因检测(2025.7.12)：BRAF突变、EGFR突变、
MSS型。后给予曲美替尼联合达拉替尼靶向治疗，期间因病情缓慢进展，加用阿美替尼靶向治
疗；今日患者出现胸闷、气短，伴咳嗽、咳少量痰粘，伴纳差乏力，现患者为进一步治疗入院，
门诊以“肺恶性肿瘤”收入院。患病来，神志清，精神差，饮食量少，睡眠可，大便可，小便
可，近期体重未监测。否认高血压，否认心脏病史，否认糖尿病，否认哮喘，否认脑血管，否认精神
疾病史，既往有“慢性乙型病毒性肝炎”病史30年。否认结核，否认疟疾，否认手术史，否认外
伤史，否认输血史，否认食物、药物过敏史，预防接种史不详。
第1页
原阳县人民
Dell
原阳县人
费别：自费 公费 医保
姓名：
性别：男
年龄：68岁
科室：
临床诊断：
Rp：
审核：
核对：
发药：
调配：
14时24分病情：一般
费别：
住院天数：8
总费用：-VTE评分：3(低危)
出院科室
出院日期
出院诊断
住院号
患者姓名
经治医师
入院年龄
付费方式
病案质量
入院情况
自付费
瘤内科病区
2026-01-18 09:42...
02317135
贾振欣
57岁
城镇居民基本医疗保险
甲
一般
瘤内科病区
2025-12-27 14:55...
02317135
贾振欣
57岁
城镇居民基本医疗保险
甲
一般
1·1·2·1·3·1·4·1·5·1·6·1·7·1·8·1·9·1·10·1·11·1·12·1·13·1·14·1·15·1·16·1·17·1·18·1·19·1·20·1·21·
文字
原阳县人民医院
出院记录
姓名：
科室：肿瘤内科病区 床号：3床 住院号：023
入院诊断：1.恶性肿瘤支持治疗 2.肺恶性肿瘤 cTxNxM1 IV期 3.肺部感染
诊疗经过：完善相关检查，与患者及家属沟通后，给予培美曲塞+卡铂+依沃西单抗方案治疗，
并给予抗感染、止咳化痰、护胃、保肝、止吐及对症支持治疗。
出院诊断：1.恶性肿瘤靶向治疗 2.肺恶性肿瘤cTxNxM1 IV期 3.肺部感染
出院情况：神志清，精神较前好转，饮食量较前好转，睡眠可，大小便可。
出院时症状与体征：神诉胸闷、气短、乏力较前好转，诉咳嗽、咳少量痰粘较前好转，查体：体
温36.3℃，脉搏71次/分，呼吸20次/分，血压128/71mmHg，神志清，双肺呼吸音清晰，未闻
及干湿性啰音，心率71次/分，律齐，各瓣膜听诊区未闻及病理性杂音，腹软，无压痛，肝脾肋
下未触及，双下肢无水肿。
出院医嘱：2026.2.3返院治疗，提前2天联系，院外监测血常规/3-5天，避免下肢静脉血栓形
成，不适随诊。
我科电话：0373-7291816
主治医师签名：
更振化
---
郑州大学第一附属医院
The First Affiliated Hospital of Zhengzhou University
出院证明书
姓名：
性别：女
年龄：57岁
住院号：00045
诊疗经过：患者以“确诊肺腺癌2年余”为主诉，初诊为“1.肺恶性肿瘤
2.慢性乙型病毒性肝炎”，于2025年07月03日收入我科。[入院完善相关检查检
验：传染病、甲功三项、PCT未见异常，2025-07-04 血细胞分析或血常规：红细
胞计数 3.65↓×10^12/L，中性粒细胞百分数 78.4↑%，淋巴细胞百分数
13.9↓%；2025-07-04 心肌酶+肾功能+葡萄糖测定+小肝功(2)+小血脂(3)+电解
质：白蛋白 33.2↓g/L，前白蛋白 152↓mg/L，乳酸脱氢酶 311↑U/L，a-
羟丁酸脱氢酶 214↑U/L；2025-07-04 炎症Ⅱ：C反应蛋白 25.13↑mg/L，血沉
62.00↑mm/h；2025-07-04 7项肿瘤标志物检测（肺）：肿瘤相关抗原72-4
7.03↑U/mL；2025-07-04 FDP全定量+血浆D-二聚体+血凝试验：活化部分凝血活
酶时间 25.10↓s，纤维蛋白原测定 4.63↑g/L；2025-07-09 乙型肝炎病毒
HBV病：高敏乙型肝炎病毒载量 4.27E+06↑IU/mL；CT：病史示肺ca治疗后复查：
左肺及右中肺多发团片影，较2025-3-19片加重，请结合临床评估。左肺阻塞性炎
症存在，较前加重。双肺炎症，较前加重。双肺多发结节，较前增多、增大。双侧
胸膜局限性增厚。左侧肾上腺内侧肢结节，较前变化不大。ECG：正常范围心电图
CT：病史示肺ca治疗后复查：左肺及右中肺多发团片影，较2025-07-03片变化不
大，请结合临床评估。左肺阻塞性炎症存在，较前相仿。双肺炎症，较前相仿。双
肺多发结节，较前相仿。双侧胸膜局限性增厚。左侧肾上腺内侧肢结节，较前变
化不大。patho：(左肺活检)非小细胞癌，组织学形态考虑腺癌，需补费后免疫组
化协诊。patho：提示：发现可疑肿瘤细胞，具体诊断请结合活检结果。patho：病
理诊断：非小细胞肺癌 检测结果：ALK增强免疫组化结果：阴性。建议行EGFR、
ROS1、Met、Ret、Her2及Braf检测以指导靶向治疗。ECG：1、窦性心动过速 2、
下壁及侧壁导联异常Q波 3、QRS波肢体导联低电压。肺恶性肿瘤患者，入院后
胸部CT提示病变较前进展，已排除禁忌症，于2025.07.08日行CT引导下穿刺
术，病理回示非小细胞癌，术中见少量气胸，予胸腔穿刺置管引流术，今复查
胸部CT，观片气胸好转，予以拔管处理。余给予解痉平喘、扩张气道、消炎、
抗感染等对症支持治疗。]现患者一般情况良好，要求出院，请示上级医师并嘱
其注意事项后予以办理出院。
第1页
郑州大学第一附属医院
The First Affiliated Hospital of Zhengzhou University
出院证明书
出院诊断：1.肺恶性肿瘤 2.间质性肺病 3.肺部感染 4.慢性乙型病毒性肝
炎 5.肿瘤标志物升高 6.低蛋白血症 7.气胸
出院医嘱：1.遵医嘱用药。
2.低盐低脂饮食。
3.注意休
息，避免劳累、避免受凉、避免刺激。
4.定期复查。
5.不适
随诊。
呼吸内五科
医师(职称)： 副主任医师：
2025-07-21
(不盖章证明无效)
在线复诊：
第 2 页
---
原阳县人民医院
入院记录
姓名：
科室：肿瘤内科病区 床号：13床 住院号：023
科室：肿瘤内科病区 第（9）次住院
药物过敏史：无
姓名：
性别：女
年龄：57岁
入院时间：2026-02-02 14:26
职业：农民
民族：汉族
婚姻：已婚
记录时间：2026-02-02 15:08
籍贯：河南省新乡市
入院情况：一般
联系方式：187491
现住址：河南省新乡市原阳县
病史陈述者：患者及
可靠程度：可靠
患者家属
工作单位：-
身份证号：4107251968
联系人：
与患者关系：配偶
联系人电话：1383
主诉：确诊肺恶性肿瘤2年余，再治疗。
现病史：患者于2年余前（2023.06）患者无明显诱因出现间断咳嗽、咳白色痰，伴有胸
闷、纳差、乏力症状，活动后胸闷症状加重，于我院门诊行胸部CT示：两肺多发异常密度病变，
较2023-03-15老片病变范围增大，结合2021-09-07片和2023-03-15片，注意警惕肺粘膜相关性淋
巴瘤或肺炎型肺癌并两肺转移的可能性，建议支气管镜活检病理学检查，给予支气管肺泡灌洗（
2024.06.15）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组织细胞，另见少许异型细
胞，呈腺样结构，不除外腺癌，请结合临床及影像学。后至郑州大学第一附属医院确诊为肺腺癌
（未见报告），具体不详，给予靶向治疗初始为阿美替尼，后调整为伏美替尼（不详）；复查CT
（2024.11.12）：1、肺癌治疗后改变，对比2024-08-20片病变较前范围增大；2、左肺上叶下舌
段及下叶后底段局限性支气管扩张；3、两肺多发微、小结节，较前右肺中叶结节稍增大，余相
仿；4、右肺中叶少许慢性炎症；5、左侧第6肋骨顺位欠佳；6、提示左侧肾上腺结节，建议动态
观察；请结合临床、病史及其它相关检查。2024.11.16调整为贝福替尼靶向治疗，2024.12.12于
郑州大学第一附属医院复查CT：1.左肺多发团片影；2.双肺炎症，较前减轻；3.双肺多发结节，
较前部分增大；4.双侧胸膜局限性增厚；5.左侧肾上腺内侧支结节，较前变化不大。给予抗感染
及对症支持治疗后好转出院。2025.5.7复查CT：、肺癌治疗后改变，对比2025-01-11片病变较前
增大；2、双肺局限性支气管扩张；3、左肺下叶空腔病灶，较前增大；4、两肺多发微、小结
节，建议动态观察；5、双肺炎性病变；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，对比较
前相仿；请结合临床、病史及其它相关检查。综合评估患者病情进展，与患者及家属沟通后，排
除禁忌症后，2025.5.15，2025.6.14给予AP方案化疗2周期，过程顺利。基因检测（
2025.7.12）：BRAF突变、EGFR突变、MSS型。后给予曲美替尼联合达拉替尼靶向治疗，期间因病
第1页
原阳县人民医院
入院记录
姓名：
科室：肿瘤内科病区 床号：13床 住院号：02
情缓慢进展，加用阿美替尼靶向治疗：复查CT（2025.12.20）：1、肺癌并纵隔淋巴结转移治疗
后改变，对比2025-12-03片较前相仿：2、双肺局限性支气管扩张；3、双肺小空泡病灶，较前壁
增厚；4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；5、双肺炎性病变，较前相
仿；6、左侧第6肋骨顺位欠佳；7、左侧肾上腺结节，考虑转移，较前大致相仿；8、肝囊肿；请
结合临床、病史及其它相关检查。排除禁忌症后，2026.1.14给予AC+AK112方案治疗1周期，过程
顺利。近两日患者诉纳差乏力，伴胸闷、气短，伴咳嗽咳痰，现患者为进一步治疗入院，门诊以
“肺恶性肿瘤”收入院。患病来，神志清，精神差，饮食量少，睡眠可，大便可，小便可，近期
体重未监测。
既往史：否认高血压，否认心脏病史，否认糖尿病，否认哮喘，否认脑血管，否认精神疾病史,
既往有“慢性乙型病毒性肝炎”病史30年。否认结核，否认疟疾，否认手术史，否认外伤史，否
认输血史，否认食物、药物过敏史，预防接种史不详。
个人史：生于河南省新乡市原阳县，无长期外地居住史。无特殊生活习惯，否认嗜酒史、
吸烟史，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，否认疫水，疫源接触史，无冶游
史。
婚育史：已婚，22岁结婚，配偶健在。育有2子1女，子女体健。
月经生育史：妊娠3次，生产3次，无流产、早产、手术产、死产，无节育、绝育。育有3个
5-7
子女，均顺产。初潮13岁28-30末次月经时间52岁。月经周期规则，月经量中等，颜色正常。无血
块、无痛经
家族史：父亲体健，母亲已故，死因不详，1弟2妹身体健康。无类似患者疾病、传染性疾
病、遗传性疾病。
患者信息及病史采集真实准确 患者（授权人）确认签字：
签名日期：2026-02-02 15:10
体格检查
体温：36.1℃ 脉搏：108次/分 呼吸：21次/分 血压：89/63mmHg
身高：165cm 体重：60Kg S：1.68m2
一般情况：发育正常，营养中等，神志清晰，精神差，体位主动，面容正常，表情安静，步态正常，
检查合作。
第2页
原阳县人民医院
入院记录
姓名：
科室：肿瘤内科病区 床号：13床 住院号：
皮肤、粘膜：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，无淤点、
紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。
浅表淋巴结：浅表淋巴结无无肿大。
头部及其他器官：头颅大小正常，无异常面容，眼睑无浮肿，结膜无苍白，巩膜无黄染，双侧
瞳孔等大等圆，左瞳孔对光反射灵敏，右瞳孔对光反射灵敏。鼻无畸形，无鼻翼煽动。鼻旁窦未
触及明显压痛。耳廓无畸形，外耳道无异常分泌物。唇红润，口腔黏膜未见明显异常。齿龈无出
血。双侧扁桃体无肿大。
颈部：颈部无抵抗，颈动脉搏动正常，颈静脉正常，气管正中，肝颈静脉回流征阴性，甲状腺
未及肿大。
胸部：双侧胸廓正常。双侧乳房对称，左侧正常，右侧正常。胸壁无有静脉曲张或充盈、皮下
气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。
肺：呼吸运动正常，呼吸节律正常，语颤正常，未触及胸膜摩擦感，双肺叩诊呈清音，呼吸规
整，双肺呼吸音减弱，可闻及湿性啰音，语音传导正常，未及明显胸膜摩擦音。
心：胸廓基本对称，心前区无隆起，心尖搏动正常，位于第五肋间左侧锁骨中线0.5cm，强度及
范围正常，无负性心尖搏动。心尖搏动正常，无震颤，无心包摩擦音。心脏相对浊音界正常。心
率108次/分，心律齐，心音无额外心音，无杂音无心包摩擦音。
桡动脉：脉搏正常，节律规则，无奇脉、交替脉。
周围血管征：无毛细血管搏动、射枪音、水冲脉、动脉异常搏动。
腹部：腹部平坦，胃肠蠕动波无，腹式呼吸存在，未见腹壁静脉曲张。腹柔软，液波震颤无，
振水声无，腹部包块未触及，无压痛、无反跳痛，脾肝未触及，Murphy's征阴性，肾无压痛，叩
击痛，腹部血管搏动未见明显异常。输尿管压痛点无明显压痛。肝浊音界存在，肝上界位于右锁
骨中线肋间，移动性浊音无。无明显肾区叩击痛，肠鸣音正常。
肛门、直肠：未查或详见专科检查。
脊柱四肢：脊柱正常，四肢无畸形，四肢关节活动及动脉搏动未见明显异常。
神经反射：生理反射存在，病理反射未引出。
专科检查
神志清，精神差，全身浅表淋巴结未触及肿大，双肺呼吸音减弱，可闻及湿性啰音，心率
108次/分，心律齐，各瓣膜听诊区未闻及杂音，腹软，未触及肿块，肝脾肋下未触及，双下肢无
第3页
原阳县人民医院
入院记录
姓名：
科室：肿瘤内科病区 床号：13床 住院号：02
水肿。
辅助检查
支气管肺泡灌洗（2024.06.15 我院）示：（肺灌洗液）镜下见呼吸道上皮细胞、炎性细胞及组
织细胞，另见少许异型细胞，呈腺样结构，不除外腺癌，请结合临床及影像学。
初步诊断：
西医诊断：
1.恶性肿瘤支持治疗
2.左肺恶性肿瘤 cTxNxM1 IV期
3.肺部感染
主治医师：爱振化
签名日期：2026-02-02
2026-08-10 19:02:29,750 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=郑州大学第一附属医院
The First Affiliated Hospital of Zhengzhou University
入院记录
姓名：
性别：女
年龄：67岁
住院号：100
无外伤、输血史，无食物、药物过敏史。
个人史：生于河南省新乡市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿
山、高氟区、低碘区居住史，无化学性物质、放射性物质、有毒物质接触史，无吸毒史，无
吸烟、饮酒史，否认冶游史。
婚姻史：己婚，20岁结婚，爱人体健，夫妻关系和睦，有2子，1女。
月经生育史：初潮14岁 周期28天 每次持续5天 52岁，月经周期规则，月经量中等，颜色正常，无血
块、无痛经；
家族史：父母体健。同胞4人，健康状况良好，无与患者类似疾病，无家族性遗传病
史。
体格检查
体温
脉搏86次/分
呼吸19次/分
血压105/74mmHg
36.50℃
身高165cm
体重62.0kg
发育正常，营养良好，体型匀称，神志清楚，自主体位，正常面容，表情自如，查体合
作。全身皮肤黏膜无黄染，无皮疹、皮下出血、皮下结节、瘢痕，无肝掌、蜘蛛痣。全身浅
表淋巴结未触及。角膜无云翳、白斑、软化、溃疡、瘢痕、反射、色素环。双眼瞳孔等大等
圆，直径3mm，对光反射灵敏，调节反射正常。口唇黏膜无斑疹、溃疡、出血点。软硬腭位
置居中。扁桃体无肿大，声音正常。颈软、无抵抗。颈动脉搏动正常、颈静脉无怒张。气管
居中。肝颈静脉回流征阴性。甲状腺无肿大、无压痛、震颤、血管杂音。胸廓对称，无局部
隆起、塌陷、压痛，呼吸运动正常。乳房正常对称、无包块、红肿、压痛、左、右乳头无分
泌物。胸壁无静脉曲张、皮下气肿。胸骨无叩痛。呼吸运动正常，肋间隙正常、语颤正常。
无胸膜摩擦感，无皮下捻发感，双肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正
常。心前区无隆起，心尖搏动正常，心浊音界正常，心前区无异常搏动，心率86次/分，律
齐，心脉率一致，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，无腹壁静脉曲张、无
胃肠型，无蠕动波，腹式呼吸存在。脐正常、无分泌物。腹部无压痛、反跳痛、腹部柔软、
无包块。肝脏肋缘下未触及，脾脏肋缘下未触及，Murphy氏征阴性，左、右肾区无叩击痛，
输尿管点无压痛，移动性浊音阴性，无液波震颤，肠鸣音正常、3次/分、无过水声、无肠鸣
杂音。肛门及外生殖器拒绝。脊柱活动正常，无侧凸、前凸、后凸，棘突无压痛、叩击痛、
四肢活动自如，无畸形、下肢静脉曲张、杵状指（趾）、水肿。关节无红肿、疼痛、活动
第2页
郑州大学第一附属医院
The First Affiliated Hospital of Zhengzhou University
入院记录
姓名：
性别：女
年龄：57岁
住院号：00
积液、活动度受限、畸形，肌肉无萎缩。腹壁反射正常，肌张力正常，肌力V级，肢体无瘫
痪，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski's sign阴性，
双侧Hoffmann征阴性，Kernig's sign阴性。
专科检查
呼吸运动正常，肋间隙正常，语颤正常，无胸膜摩擦感，无皮下捻发感，叩诊清音，双
肺呼吸音清、无干、湿啰音，无胸膜摩擦音，语音共振正常。
辅助检查
暂无
初步诊断：
1.肺恶性肿瘤
2.慢性乙型病毒性肝炎
副主任医师：
王欢
2025年07月03日
---
郑州大学第一附属医院
组织病理学检查与诊断报告
姓名：
性别：女
年龄：57岁
送检医院：本院
送检科室：呼吸内五科
送检医生：刘莹
报告日期：2025-07-10 10:06
标本名称：左肺
临床诊断：肺恶性肿瘤
肉眼所见：（左肺）暗红组织一块，大小约1.6*0.7*0.3cm。
病理诊断：（左肺活检）非小细胞癌，组织学形态考虑腺癌，需补费后免疫组化协诊。
病理号：B25-
收到日期：2025-01-08
住院号：0004
第4页 共5页
标本号：9041
---
郑州大学第一附属医院
细胞病理学检查与诊断报告
病理号：C25
姓名：
性别：女
年龄：57岁
收到日期：2025-07-08
送检医院：本院
送检科室：呼吸内五科
住院号：00049
送检医生：刘莹
报告日期：2025-07-10 15:31
标本名称：TCT肺
临床诊断：肺恶性肿瘤
镜下所见：（左肺穿刺TCT）镜下见少量核浆比大的细胞。
病理诊断：提示：发现可疑肿瘤细胞，具体诊断请结合活检结果。
---
原阳县人民医院
CT检查报告单
病人ID:
姓名:
性别:女
年龄:57岁
检查类型:CT
病人来源:住院
住院号:02
床号:/
申请科室:肿瘤内科病区
检查部位:胸部平扫(CT)
检查时2026-02-03 08:40:46
间:
影像所见:
双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，内见含气支气管。双肺可
见多发微、小结节、增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺
可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴结。左侧胸膜可见增厚，
未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未见明显破坏征象。附见左侧肾上腺见结节状软组织
密度影。
影像诊断:
1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-20片纵隔淋巴结稍增大；
2、双肺局限性支气管扩张；
3、双肺小空泡病灶，较前大致相仿；
4、两肺多发微、小结节，考虑转移瘤，较前增多；
5、两肺炎性病变较前进展；
6、左侧胸膜增厚；左侧第6肋骨顺位欠佳；
7、左侧肾上腺结节，考虑转移，较前大致相仿；
请结合临床、病史及其它相关检查。
2026.2.6
---
CT检查报告单
病人ID:
姓名:
性别:女
年龄:57岁
检查编号:CT02
病人来源:住院
住院号:02
床号:/
检查类型:CT
申请科室:肿瘤内科病区
检查部位:上腹部CT增强+延迟(CT);胸部增强(C检查时间:2025-12-20 08:31:12
T):
影像所见:
双肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，增强病变可见明显强化，
内见含气支气管。双肺可见多发微、小结节，增强可见强化，左肺上叶下舌段、下叶后底段及右肺中叶
局部支气管稍扩张，双肺可见多发小空腔影。气管及主支气管通畅。纵隔结构清楚，内见多发增大淋巴
结，增强可见环形强化。两侧胸膜未见明显增厚，未见胸腔积液。左侧第6肋骨顺位欠佳，余所示骨质未
见明显破坏征象。
肝脏边缘光滑，肝实质见小类圆形无强化低密度，肝内外胆管未见扩张。胆囊不大，壁厚薄均匀，
未见异常强化，未见阳性结石影。胰腺大小、形态及密度正常，未见异常强化。脾不大，实质密度均
匀，未见异常强化。左侧肾上腺见结节状高密度，增强可见轻中度强化，双肾大小形态正常，实质密度
均匀，未见异常强化，肾盂未见扩张，未见阳性结石影。腹腔内及腹膜后未见强化肿大淋巴结，未见腹
水征象。
影像诊断:
1、肺癌并纵隔淋巴结转移治疗后改变，对比2025-12-03片较前相仿；
2、双肺局限性支气管扩张；
3、双肺小空泡病灶，较前壁增厚；
4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；
5、双肺炎性病变，较前相仿；
6、左侧第6肋骨顺位欠佳；
7、左侧肾上腺结节，考虑转移，较前大致相仿；
8、肝囊肿；
请结合临床、病史及其它相关检查。
---
原阳县人民医院
CT检查报告单
病人ID:
P
检查编号: CTO.
姓名:
薛
性别:女
年龄:57岁
检查类型: CT
病人来源: 门诊
住院号:
床号:
申请科室: 呼吸与危重症医学科
门诊
检查部位:
胸部平扫(CT);
检查时间: 2025-12-03 09:26:58
影像所见:
左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两
肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片
状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见
明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显
破坏征象。
影像诊断:
1、肺癌治疗后改变，对比2025-11-05片较前相仿；
2、双肺局限性支气管扩张；
3、左肺下叶小空泡病灶，较前增多，壁增厚；
4、两肺多发微、小结节，考虑转移瘤，对比老片变化不大；
5、双肺炎性病变，较前相仿；
6、左侧第6肋骨顺位欠佳；
7、提示左侧肾上腺结节，较前大致相仿；
请结合临床、病史及其它相关检查。
---
CT检查报告单
病人ID:
姓名:
性别:女
年龄:57岁
检查编号:CTC
病人来源:门诊
住院号:
床号:
检查类型:CT
申请科室:血液内科门诊
检查部位:胸部平扫(CT)
检查时间:2025-11-05 09:32:29
影像所见:
左肺散在多发斑片状、片状高密度并两肺弥漫性多发云絮状稍高密度影，病变内见含气支气管。两
肺可见多发微、小结节，左肺上叶下舌段、下叶后底段及右肺中叶局部支气管稍扩张，双肺见多发斑片
状高密度，左肺下叶可见小空腔影。气管支气管通畅。纵隔结构清楚，未见肿大淋巴结。两侧胸膜未见
明显增厚，未见胸腔积液。附见左侧肾上腺可见结节状影。左侧第6肋骨顺位欠佳，余所示骨质未见明显
破坏征象。
影像诊断:
1、肺癌治疗后改变，对比2025-08-27片病变范围增大；
2、双肺局限性支气管扩张；
3、左肺下叶小空泡病灶，较前增多，壁增厚；
4、两肺多发微、小结节，考虑转移瘤，较前明显增多、增大；
5、双肺炎性病变，较前病变增多；
6、左侧第6肋骨顺位欠佳；
7、提示左侧肾上腺结节，较前大致相仿；
请结合临床、病史及其它相关检查。
2026-08-10 19:02:30,124 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 19:02:30,124 INFO     29 [Trace] task=ffaf4fc0 | doc=10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "23 items, types={'LabReport': 13, 'DischargeRecord': 2, 'AdmissionRecord': 2, 'ExaminationReport': 6}", "name": "10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf", "embedding_token_consumption": 12488}
2026-08-10 19:02:30,124 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 19:02:30,605 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 19:02:30,605 INFO     29 [Trace] task=ffaf4fc0 | doc=10-武汉协和-XJJA，后线肺癌，方穹招募推荐.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"partial\",\"synced_chunks\":20,\"skipped_hallucinated\":0,\"failed\":[{\"chunk_id\":\"4b4b1601f2765bf0\",\"error\":\"(sqlalchemy.dialects.postgresql.asyncpg.Error) <class 'asyncpg.exceptions.StringDataRi...(9403 chars)"}
2026-08-10 19:02:30,615 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(20, 725, 908, 320, 345) row[-1]=(20, 725, 908, 320, 345)
2026-08-10 19:02:30,615 INFO     29 [DIAG-EXECUTOR] row_position_int len=18 row[0]=(21, 744, 867, 299, 322) row[-1]=(21, 744, 894, 785, 807)
2026-08-10 19:02:30,615 INFO     29 [DIAG-EXECUTOR] row_position_int len=12 row[0]=(22, 746, 908, 224, 245) row[-1]=(22, 639, 662, 588, 605)
2026-08-10 19:02:30,615 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(22, 752, 777, 895, 911) row[-1]=(22, 752, 777, 914, 930)
2026-08-10 19:02:30,615 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(23, 696, 796, 361, 379) row[-1]=(23, 696, 894, 514, 531)
2026-08-10 19:02:30,615 INFO     29 [DIAG-EXECUTOR] row_position_int len=14 row[0]=(24, 735, 775, 318, 336) row[-1]=(24, 735, 812, 640, 658)
2026-08-10 19:02:30,616 INFO     29 [DIAG-EXECUTOR] row_position_int len=7 row[0]=(25, 602, 706, 355, 374) row[-1]=(25, 602, 706, 535, 554)
2026-08-10 19:02:30,616 INFO     29 [DIAG-EXECUTOR] row_position_int len=22 row[0]=(26, 689, 752, 366, 384) row[-1]=(26, 1209, 1261, 578, 596)
2026-08-10 19:02:30,616 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(27, 800, 979, 365, 387) row[-1]=(27, 800, 979, 365, 387)
2026-08-10 19:02:30,616 INFO     29 [DIAG-EXECUTOR] row_position_int len=25 row[0]=(28, 698, 779, 375, 394) row[-1]=(28, 1219, 1305, 537, 556)
2026-08-10 19:02:30,616 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(29, 374, 768, 510, 536) row[-1]=(29, 374, 768, 510, 536)
2026-08-10 19:02:30,616 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(30, 284, 672, 385, 429) row[-1]=(30, 288, 781, 653, 695)
2026-08-10 19:02:30,616 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(31, 324, 491, 1411, 1435) row[-1]=(31, 102, 255, 1538, 1560)
2026-08-10 19:02:30,617 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,617 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,617 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,617 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,617 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,618 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,618 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,618 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:02:30,625 INFO     29 set_progress(ffaf4fc094ea11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 19:02:30 [DOC Engine]:
Start to index...
2026-08-10 19:02:30,660 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.021s]
2026-08-10 19:02:30,664 INFO     29 set_progress(ffaf4fc094ea11f1bd9827cf206dfa2d), progress: 0.8043478260869565, progress_msg: 
2026-08-10 19:02:30,694 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:02:30,718 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:02:30,735 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-10 19:02:30,750 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-10 19:02:30,762 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.005s]
2026-08-10 19:02:30,767 INFO     29 set_progress(ffaf4fc094ea11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 19:02:30 Indexing done (0.14s). Task done (1216.47s)
2026-08-10 19:02:30,770 INFO     29 [Done], chunks(23), token(12488), elapsed:1216.47
2026-08-10 19:02:31,140 INFO     29 handle_task done for task {"id": "ffaf4fc094ea11f1bd9827cf206dfa2d", "doc_id": "ff265efe94ea11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "10-\u6b66\u6c49\u534f\u548c-XJJA\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 23099458, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786387245815, "task_type": "dataflow", "root_trace_id": "614d868b7b324a7e909fee83e536e14f", "root_traceparent": "00-614d868b7b324a7e909fee83e536e14f-7c0f1c9a36717113-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 19:02:33,969 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:33,969 INFO     29 [qwen-vl-table] page=16 LLM output (len=745):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "甲胎蛋白",
      "item_code": "AFP",
      "value": "3.41",
      "unit": "ng/ml",
      "reference_range": "0.00-7.00",
      "abnormal": false
    },
    {
      "name": "癌胚抗原",
      "item_code": "CEA",
      "value": "3.52",
      "unit": "ng/ml",
      "reference_range": "0.00-5.00",
      "abnormal": false
    },
    {
      "name": "非小细胞肺癌相关抗原",
      "item_code": "CYFRA21-1",
      "value": "1.70",
      "unit": "ng/ml",
      "reference_range": "0.00-3.30",
      "abnormal": false
    },
    {
      "name": "神经元特异性烯醇化酶",
      "item_code": "NSE",
      "value": "16.60",
      "unit": "ng/ml",
      "reference_range": "0.00-16.30",
      "abnormal": true
    }
  ]
}
2026-08-10 19:02:33,969 INFO     29 [qwen-vl-table] coord grouping: {16: 4}
2026-08-10 19:02:33,976 INFO     29 [qwen-vl-table] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4150521, prompt_len=538
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
甲胎蛋白、癌胚抗原、非小细胞肺癌相关抗原、神经元特异性烯醇化酶

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
2026-08-10 19:02:35,771 INFO     29 [qwen-vl-table] coord API raw response (len=205):
[
	{"text": "甲胎蛋白", "bbox": [63, 90, 150, 104]},
	{"text": "癌胚抗原", "bbox": [63, 107, 150, 120]},
	{"text": "非小细胞肺癌相关抗原", "bbox": [56, 123, 228, 137]},
	{"text": "神经元特异性烯醇化酶", "bbox": [56, 139, 228, 153]}
]
2026-08-10 19:02:35,772 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=1.8s
2026-08-10 19:02:35,772 INFO     29 [qwen-vl-table] coord item[0]: text=甲胎蛋白, bbox=[63, 90, 150, 104]
2026-08-10 19:02:35,772 INFO     29 [qwen-vl-table] coord item[1]: text=癌胚抗原, bbox=[63, 107, 150, 120]
2026-08-10 19:02:35,772 INFO     29 [qwen-vl-table] coord item[2]: text=非小细胞肺癌相关抗原, bbox=[56, 123, 228, 137]
2026-08-10 19:02:35,772 INFO     29 [qwen-vl-table] coord item[3]: text=神经元特异性烯醇化酶, bbox=[56, 139, 228, 153]
2026-08-10 19:02:35,773 INFO     29 [qwen-vl-table] page=16 coord: matched 4/4, time=1.8s
2026-08-10 19:02:35,773 INFO     29 [qwen-vl-table] new_positions (4):
[[17, 25.83, 61.49999999999999, 50.94, 58.864], [17, 25.83, 61.49999999999999, 60.562, 67.91999999999999], [17, 22.959999999999997, 93.47999999999999, 69.618, 77.54199999999999], [17, 22.959999999999997, 93.47999999999999, 78.67399999999999, 86.598]]
2026-08-10 19:02:35,774 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=4, matched=4, pages=1, time=9.4s
2026-08-10 19:02:35,788 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 19:02:35,789 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:LabExam | outputs={"chunks": "3 items, types={'LabReport': 3}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:02:35,789 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 19:02:35,794 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:35,794 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:02:36,636 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:36,650 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 19:02:36,651 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:02:36,651 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 19:02:36,657 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:02:36,658 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:02:36,658 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 19:02:36,658 INFO     29 [qwen-vl-text] positions(57): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:02:36,658 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [57]
2026-08-10 19:02:36,904 INFO     29 [qwen-vl-text] page=5, rect=410x518, img=(1139x1439), dpi=200
2026-08-10 19:02:36,907 INFO     29 [qwen-vl-text] LLM extraction start, text_len=570
2026-08-10 19:02:36,907 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:36,907 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 169, \"bbox_end\": 225, \"encounter_dates\": [\"2024-03-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n初诊\n复诊\n门诊号\n就诊\n姓名\n性别：女\n年龄：60岁\n身份\n职业：农民\n就诊时间：2024-03-01 08:13:19\n联系人\n联系电话\n现住址\nT:\n℃\nP:\n次/分\nR:\n次/分\nBP:\n/\nmmHg\n处方\n检查\n检验\n医疗医嘱\n主诉：\n肺Ca术后3年余，肺结节？\n现病史：\n3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）\n20-ins突变阳性。\n2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双\n肺多发小结节，较前变化不著，请结合临床、随诊复查。\n既往史：\n否认其他病史。\n家族史：\n否认家族史。\n过敏史：\n体征：\n辅助检查：\n2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小\n结节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于\n左肺下叶外基底段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03\n提示浸润性腺癌，大小3*2.5cm，查见淋巴结转移癌\n初步诊断：\n肺癌\n修正诊断：\n肺癌术后肺结节\n处方：\n检查：\n检验：\n医疗医嘱：\n其他建议：\n建议3月后复查\n已告知患者病情及可能的药物不良反应。\n医生签",
    "role": "user"
  }
]
2026-08-10 19:02:44,146 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:02:44,146 INFO     29 [qwen-vl-text] LLM output (len=314):
{
  "encounter_date": "2024-03-01",
  "chief_complaint": "肺Ca术后3年余，肺结节？",
  "present_illness": "3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-ins突变阳性。2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结节，较前变化不著，请结合临床、随诊复查。",
  "past_history": "否认其他病史。",
  "diagnosis": "肺癌术后肺结节",
  "treatment_plan": "建议3月后复查"
}
2026-08-10 19:02:44,147 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-03-01]
2026-08-10 19:02:44,160 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3925077, prompt_len=1354
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共57行）
["门诊病历", "初诊", "复诊", "门诊号", "就诊", "姓名", "性别：女", "年龄：60岁", "身份", "职业：农民", "就诊时间：2024-03-01 08:13:19", "联系人", "联系电话", "现住址", "T:", "℃", "P:", "次/分", "R:", "次/分", "BP:", "/", "mmHg", "处方", "检查", "检验", "医疗医嘱", "主诉：", "肺Ca术后3年余，肺结节？", "现病史：", "3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）", "20-ins突变阳性。", "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双", "肺多发小结节，较前变化不著，请结合临床、随诊复查。", "既往史：", "否认其他病史。", "家族史：", "否认家族史。", "过敏史：", "体征：", "辅助检查：", "2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小", "结节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于", "左肺下叶外基底段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03", "提示浸润性腺癌，大小3*2.5cm，查见淋巴结转移癌", "初步诊断：", "肺癌", "修正诊断：", "肺癌术后肺结节", "处方：", "检查：", "检验：", "医疗医嘱：", "其他建议：", "建议3月后复查", "已告知患者病情及可能的药物不良反应。", "医生签"]

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
2026-08-10 19:03:07,689 INFO     29 [qwen-vl-text] coord API raw response (len=4707):
[
	{"text": "门诊病历", "bbox": [367, 34, 580, 62]},
	{"text": "初诊", "bbox": [89, 83, 129, 103], "bbox": [89, 83, 129, 103]},
	{"text": "复诊", "bbox": [90, 108, 129, 126], "bbox": [90, 108, 129, 126]},
	{"text": "门诊号", "bbox": [672, 78, 726, 95], "bbox": [672, 78, 726, 95]},
	{"text": "就诊", "bbox": [652, 108, 689, 124], "bbox": [652, 108, 689, 124]},
	{"text": "姓名", "bbox": [46, 141, 95, 158], "bbox": [46, 141, 95, 158]},
	{"text": "性别：女", "bbox": [292, 140, 372, 158], "bbox": [292, 140, 372, 158]},
	{"text": "年龄：60岁", "bbox": [435, 140, 527, 157], "bbox": [435, 140, 527, 157]},
	{"text": "身份", "bbox": [591, 141, 628, 158], "bbox": [591, 141, 628, 158]},
	{"text": "职业：农民", "bbox": [47, 174, 165, 191], "bbox": [47, 174, 165, 191]},
	{"text": "就诊时间：2024-03-01 08:13:19", "bbox": [291, 175, 570, 193], "bbox": [291, 175, 570, 193]},
	{"text": "联系人", "bbox": [50, 210, 100, 227], "bbox": [50, 210, 100, 227]},
	{"text": "联系电话", "bbox": [291, 210, 362, 227], "bbox": [291, 210, 362, 227]},
	{"text": "现住址", "bbox": [557, 210, 613, 227], "bbox": [557, 210, 613, 227]},
	{"text": "T:", "bbox": [62, 245, 80, 262], "bbox": [62, 245, 80, 262]},
	{"text": "℃", "bbox": [143, 245, 161, 262], "bbox": [143, 245, 161, 262]},
	{"text": "P:", "bbox": [214, 245, 231, 262], "bbox": [214, 245, 231, 262]},
	{"text": "次/分", "bbox": [284, 245, 329, 262], "bbox": [284, 245, 329, 262]},
	{"text": "R:", "bbox": [372, 245, 391, 262], "bbox": [372, 245, 391, 262]},
	{"text": "次/分", "bbox": [431, 245, 476, 262], "bbox": [431, 245, 476, 262]},
	{"text": "BP:", "bbox": [525, 245, 555, 262], "bbox": [525, 245, 555, 262]},
	{"text": "/", "bbox": [604, 245, 614, 262], "bbox": [604, 245, 614, 262]},
	{"text": "mmHg", "bbox": [659, 245, 719, 262], "bbox": [659, 245, 719, 262]},
	{"text": "处方", "bbox": [241, 280, 290, 304], "bbox": [241, 280, 290, 304]},
	{"text": "检查", "bbox": [375, 280, 425, 304], "bbox": [375, 280, 425, 304]},
	{"text": "检验", "bbox": [517, 280, 566, 304], "bbox": [517, 280, 566, 304]},
	{"text": "医疗医嘱", "bbox": [650, 280, 708, 304], "bbox": [650, 280, 708, 304]},
	{"text": "主诉：", "bbox": [46, 320, 117, 340], "bbox": [46, 320, 117, 340]},
	{"text": "肺Ca术后3年余，肺结节？", "bbox": [184, 313, 403, 333], "bbox": [184, 313, 403, 333]},
	{"text": "现病史：", "bbox": [46, 355, 117, 374], "bbox": [46, 355, 117, 374]},
	{"text": "3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）", "bbox": [184, 347, 904, 367], "bbox": [184, 347, 904, 367]},
	{"text": "20-ins突变阳性。", "bbox": [145, 366, 293, 383], "bbox": [145, 366, 293, 383]},
	{"text": "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双", "bbox": [184, 383, 912, 402], "bbox": [184, 383, 912, 402]},
	{"text": "肺多发小结节，较前变化不著，请结合临床、随诊复查。", "bbox": [145, 401, 624, 419], "bbox": [145, 401, 624, 419]},
	{"text": "既往史：", "bbox": [47, 445, 117, 464], "bbox": [47, 445, 117, 464]},
	{"text": "否认其他病史。", "bbox": [186, 439, 313, 458], "bbox": [186, 439, 313, 458]},
	{"text": "家族史：", "bbox": [47, 478, 117, 497], "bbox": [47, 478, 117, 497]},
	{"text": "否认家族史。", "bbox": [186, 472, 293, 491], "bbox": [186, 472, 293, 491]},
	{"text": "过敏史：", "bbox": [47, 512, 117, 531], "bbox": [47, 512, 117, 531]},
	{"text": "体征：", "bbox": [50, 550, 120, 568], "bbox": [50, 550, 120, 568]},
	{"text": "辅助检查：", "bbox": [50, 582, 140, 600], "bbox": [50, 582, 140, 600]},
	{"text": "2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小", "bbox": [207, 576, 905, 594], "bbox": [207, 576, 905, 594]},
	{"text": "结节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于", "bbox": [150, 593, 905, 612], "bbox": [150, 593, 905, 612]},
	{"text": "左肺下叶外基底段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03", "bbox": [150, 611, 905, 629], "bbox": [150, 611, 905, 629]},
	{"text": "提示浸润性腺癌，大小3*2.5cm，查见淋巴结转移癌", "bbox": [150, 628, 583, 646], "bbox": [150, 628, 583, 646]},
	{"text": "初步诊断：", "bbox": [54, 670, 144, 689], "bbox": [54, 670, 144, 689]},
	{"text": "肺癌", "bbox": [190, 665, 228, 682], "bbox": [190, 665, 228, 682]},
	{"text": "修正诊断：", "bbox": [55, 702, 145, 721], "bbox": [55, 702, 145, 721]},
	{"text": "肺癌术后肺结节", "bbox": [190, 696, 324, 715], "bbox": [190, 696, 324, 715]},
	{"text": "处方：", "bbox": [55, 735, 126, 754], "bbox": [55, 735, 126, 754]},
	{"text": "检查：", "bbox": [55, 767, 126, 786], "bbox": [55, 767, 126, 786]},
	{"text": "检验：", "bbox": [55, 800, 126, 819], "bbox": [55, 800, 126, 819]},
	{"text": "医疗医嘱：", "bbox": [55, 833, 146, 852], "bbox": [55, 833, 146, 852]},
	{"text": "其他建议：", "bbox": [60, 864, 148, 883], "bbox": [60, 864, 148, 883]},
	{"text": "建议3月后复查", "bbox": [194, 858, 318, 876], "bbox": [194, 858, 318, 876]},
	{"text": "已告知患者病情及可能的药物不良反应。", "bbox": [62, 897, 370, 915], "bbox": [62, 897, 370, 915]},
	{"text": "医生签", "bbox": [589, 901, 646, 918], "bbox": [589, 901, 646, 918]}
]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord API: raw_items=57, valid_items=57, elapsed=23.5s
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[367, 34, 580, 62]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[1]: text=初诊, bbox=[89, 83, 129, 103]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[2]: text=复诊, bbox=[90, 108, 129, 126]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号, bbox=[672, 78, 726, 95]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[4]: text=就诊, bbox=[652, 108, 689, 124]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[46, 141, 95, 158]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女, bbox=[292, 140, 372, 158]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：60岁, bbox=[435, 140, 527, 157]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[8]: text=身份, bbox=[591, 141, 628, 158]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[9]: text=职业：农民, bbox=[47, 174, 165, 191]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[10]: text=就诊时间：2024-03-01 08:13:19, bbox=[291, 175, 570, 193]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[11]: text=联系人, bbox=[50, 210, 100, 227]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[12]: text=联系电话, bbox=[291, 210, 362, 227]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[13]: text=现住址, bbox=[557, 210, 613, 227]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[14]: text=T:, bbox=[62, 245, 80, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[15]: text=℃, bbox=[143, 245, 161, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[16]: text=P:, bbox=[214, 245, 231, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[17]: text=次/分, bbox=[284, 245, 329, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[18]: text=R:, bbox=[372, 245, 391, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[19]: text=次/分, bbox=[431, 245, 476, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[20]: text=BP:, bbox=[525, 245, 555, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[21]: text=/, bbox=[604, 245, 614, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[22]: text=mmHg, bbox=[659, 245, 719, 262]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[23]: text=处方, bbox=[241, 280, 290, 304]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[24]: text=检查, bbox=[375, 280, 425, 304]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[25]: text=检验, bbox=[517, 280, 566, 304]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[26]: text=医疗医嘱, bbox=[650, 280, 708, 304]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[27]: text=主诉：, bbox=[46, 320, 117, 340]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[28]: text=肺Ca术后3年余，肺结节？, bbox=[184, 313, 403, 333]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[29]: text=现病史：, bbox=[46, 355, 117, 374]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[30]: text=3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）, bbox=[184, 347, 904, 367]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[31]: text=20-ins突变阳性。, bbox=[145, 366, 293, 383]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[32]: text=2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双, bbox=[184, 383, 912, 402]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[33]: text=肺多发小结节，较前变化不著，请结合临床、随诊复查。, bbox=[145, 401, 624, 419]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[34]: text=既往史：, bbox=[47, 445, 117, 464]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[35]: text=否认其他病史。, bbox=[186, 439, 313, 458]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[36]: text=家族史：, bbox=[47, 478, 117, 497]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[37]: text=否认家族史。, bbox=[186, 472, 293, 491]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[38]: text=过敏史：, bbox=[47, 512, 117, 531]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[39]: text=体征：, bbox=[50, 550, 120, 568]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[40]: text=辅助检查：, bbox=[50, 582, 140, 600]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[41]: text=2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小, bbox=[207, 576, 905, 594]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[42]: text=结节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于, bbox=[150, 593, 905, 612]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[43]: text=左肺下叶外基底段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03, bbox=[150, 611, 905, 629]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[44]: text=提示浸润性腺癌，大小3*2.5cm，查见淋巴结转移癌, bbox=[150, 628, 583, 646]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[45]: text=初步诊断：, bbox=[54, 670, 144, 689]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[46]: text=肺癌, bbox=[190, 665, 228, 682]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[47]: text=修正诊断：, bbox=[55, 702, 145, 721]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[48]: text=肺癌术后肺结节, bbox=[190, 696, 324, 715]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[49]: text=处方：, bbox=[55, 735, 126, 754]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[50]: text=检查：, bbox=[55, 767, 126, 786]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[51]: text=检验：, bbox=[55, 800, 126, 819]
2026-08-10 19:03:07,690 INFO     29 [qwen-vl-text] coord item[52]: text=医疗医嘱：, bbox=[55, 833, 146, 852]
2026-08-10 19:03:07,691 INFO     29 [qwen-vl-text] coord item[53]: text=其他建议：, bbox=[60, 864, 148, 883]
2026-08-10 19:03:07,691 INFO     29 [qwen-vl-text] coord item[54]: text=建议3月后复查, bbox=[194, 858, 318, 876]
2026-08-10 19:03:07,691 INFO     29 [qwen-vl-text] coord item[55]: text=已告知患者病情及可能的药物不良反应。, bbox=[62, 897, 370, 915]
2026-08-10 19:03:07,691 INFO     29 [qwen-vl-text] coord item[56]: text=医生签, bbox=[589, 901, 646, 918]
2026-08-10 19:03:07,691 INFO     29 [qwen-vl-text] page=5 — 57/57 coords, api_time=23.5s
2026-08-10 19:03:07,691 INFO     29 [qwen-vl-text] new_positions (57):
[[5, 150.47, 237.79999999999998, 17.612000000000002, 32.116], [5, 36.489999999999995, 52.88999999999999, 42.994, 53.354], [5, 36.9, 52.88999999999999, 55.944, 65.268], [5, 275.52, 297.65999999999997, 40.404, 49.21], [5, 267.32, 282.49, 55.944, 64.232], [5, 18.86, 38.949999999999996, 73.038, 81.84400000000001], [5, 119.72, 152.51999999999998, 72.52, 81.84400000000001], [5, 178.35, 216.07, 72.52, 81.32600000000001], [5, 242.30999999999997, 257.47999999999996, 73.038, 81.84400000000001], [5, 19.27, 67.64999999999999, 90.132, 98.938], [5, 119.30999999999999, 233.7, 90.65, 99.974], [5, 20.5, 41.0, 108.78, 117.586], [5, 119.30999999999999, 148.42, 108.78, 117.586], [5, 228.36999999999998, 251.32999999999998, 108.78, 117.586], [5, 25.419999999999998, 32.8, 126.91000000000001, 135.716], [5, 58.629999999999995, 66.00999999999999, 126.91000000000001, 135.716], [5, 87.74, 94.71, 126.91000000000001, 135.716], [5, 116.44, 134.89, 126.91000000000001, 135.716], [5, 152.51999999999998, 160.31, 126.91000000000001, 135.716], [5, 176.70999999999998, 195.16, 126.91000000000001, 135.716], [5, 215.25, 227.54999999999998, 126.91000000000001, 135.716], [5, 247.64, 251.73999999999998, 126.91000000000001, 135.716], [5, 270.19, 294.78999999999996, 126.91000000000001, 135.716], [5, 98.80999999999999, 118.89999999999999, 145.04, 157.472], [5, 153.75, 174.25, 145.04, 157.472], [5, 211.97, 232.05999999999997, 145.04, 157.472], [5, 266.5, 290.28, 145.04, 157.472], [5, 18.86, 47.97, 165.76, 176.12], [5, 75.44, 165.23, 162.13400000000001, 172.494], [5, 18.86, 47.97, 183.89000000000001, 193.732], [5, 75.44, 370.64, 179.746, 190.106], [5, 59.449999999999996, 120.13, 189.588, 198.394], [5, 75.44, 373.91999999999996, 198.394, 208.23600000000002], [5, 59.449999999999996, 255.83999999999997, 207.71800000000002, 217.042], [5, 19.27, 47.97, 230.51000000000002, 240.352], [5, 76.25999999999999, 128.32999999999998, 227.40200000000002, 237.244], [5, 19.27, 47.97, 247.604, 257.446], [5, 76.25999999999999, 120.13, 244.496, 254.338], [5, 19.27, 47.97, 265.216, 275.058], [5, 20.5, 49.199999999999996, 284.90000000000003, 294.224], [5, 20.5, 57.4, 301.476, 310.8], [5, 84.86999999999999, 371.04999999999995, 298.368, 307.692], [5, 61.49999999999999, 371.04999999999995, 307.17400000000004, 317.016], [5, 61.49999999999999, 371.04999999999995, 316.498, 325.822], [5, 61.49999999999999, 239.02999999999997, 325.30400000000003, 334.628], [5, 22.139999999999997, 59.04, 347.06, 356.902], [5, 77.89999999999999, 93.47999999999999, 344.47, 353.276], [5, 22.549999999999997, 59.449999999999996, 363.636, 373.478], [5, 77.89999999999999, 132.84, 360.528, 370.37], [5, 22.549999999999997, 51.66, 380.73, 390.572], [5, 22.549999999999997, 51.66, 397.30600000000004, 407.148], [5, 22.549999999999997, 51.66, 414.40000000000003, 424.242], [5, 22.549999999999997, 59.86, 431.494, 441.336], [5, 24.599999999999998, 60.68, 447.552, 457.394], [5, 79.53999999999999, 130.38, 444.444, 453.76800000000003], [5, 25.419999999999998, 151.7, 464.646, 473.97], [5, 241.48999999999998, 264.85999999999996, 466.718, 475.524]]
2026-08-10 19:03:07,692 INFO     29 [qwen-vl-text] ═══ DONE ═══ 57 positions, pages=1, time=31.0s
2026-08-10 19:03:07,692 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:03:07,698 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:03:07,698 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 19:03:07,698 INFO     29 [qwen-vl-text] positions(56): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:03:07,698 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [56]
2026-08-10 19:03:07,935 INFO     29 [qwen-vl-text] page=6, rect=410x534, img=(1139x1484), dpi=200
2026-08-10 19:03:07,937 INFO     29 [qwen-vl-text] LLM extraction start, text_len=793
2026-08-10 19:03:07,937 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:03:07,938 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 226, \"bbox_end\": 281, \"encounter_dates\": [\"2024-08-13\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n性别：女\n年龄：61岁\n民族：汉族\n婚姻：已婚\n职业：农民\n证件类型：居民身份证\n证件号码\n门诊编号\n就诊医院\n就诊科室：\n就诊日期：2024-08-13 08:50:41\n初诊/复诊：初诊  复诊\n陪检者姓名：\n陪检者与患者的关系：\n联系电话\n处方\n检查\n检验\n医疗医嘱\n主诉：肺Ca术后3年余，肺结节？\n现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-\nins突变阳性。\n2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结\n节，较前变化不著，请结合临床、随诊复查。\n既往史：否认其他病史。\n家族史：否认家族史\n过敏史：无\n体温（℃）\n脉博（次/分）\n收缩压（mmHg）\n舒张压（mmHg）\n呼吸（次/分）\n意识状态  清醒\n主要症状和体征：\n体格检查：\n辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结\n节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底\n段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小\n3*2.5cm，查见淋巴结转移癌\n初步诊断：肺癌\n修正诊断：肺癌术后\n处\n方：\n检\n验：\n门诊检验申请单（生化检验申请单），项目为：血生化 肝功 血脂（生化室）肾功（生\n化）\n门诊检验申请单（门诊检验申请单），项目为：血细胞分析五分类（静脉）（门化）\n门诊检验申请单（中心检验申请单），项目为：AFP-甲胎蛋白 CEA-癌胚抗原 NSE-神经\n元特异性烯化醇酶 非小细胞癌相关抗原（中心）\n检\n查：\n门诊检查申请单（CT检查申请单（新）），项目为：胸部CT平扫\n医疗医嘱：\n其他建议：",
    "role": "user"
  }
]
2026-08-10 19:03:07,940 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:03:07.940+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 88, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:03:14,981 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:03:14,982 INFO     29 [qwen-vl-text] LLM output (len=308):
{
  "encounter_date": "2024-08-13",
  "chief_complaint": "肺Ca术后3年余，肺结节？",
  "present_illness": "3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-ins突变阳性。\n2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结节，较前变化不著，请结合临床、随诊复查。",
  "past_history": "否认其他病史。",
  "diagnosis": "肺癌术后",
  "treatment_plan": null
}
2026-08-10 19:03:14,982 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-08-13]
2026-08-10 19:03:14,992 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4249235, prompt_len=1574
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共56行）
["门诊病历", "性别：女", "年龄：61岁", "民族：汉族", "婚姻：已婚", "职业：农民", "证件类型：居民身份证", "证件号码", "门诊编号", "就诊医院", "就诊科室：", "就诊日期：2024-08-13 08:50:41", "初诊/复诊：初诊  复诊", "陪检者姓名：", "陪检者与患者的关系：", "联系电话", "处方", "检查", "检验", "医疗医嘱", "主诉：肺Ca术后3年余，肺结节？", "现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "ins突变阳性。", "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "节，较前变化不著，请结合临床、随诊复查。", "既往史：否认其他病史。", "家族史：否认家族史", "过敏史：无", "体温（℃）", "脉博（次/分）", "收缩压（mmHg）", "舒张压（mmHg）", "呼吸（次/分）", "意识状态  清醒", "主要症状和体征：", "体格检查：", "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "3*2.5cm，查见淋巴结转移癌", "初步诊断：肺癌", "修正诊断：肺癌术后", "处", "方：", "检", "验：", "门诊检验申请单（生化检验申请单），项目为：血生化 肝功 血脂（生化室）肾功（生", "化）", "门诊检验申请单（门诊检验申请单），项目为：血细胞分析五分类（静脉）（门化）", "门诊检验申请单（中心检验申请单），项目为：AFP-甲胎蛋白 CEA-癌胚抗原 NSE-神经", "元特异性烯化醇酶 非小细胞癌相关抗原（中心）", "检", "查：", "门诊检查申请单（CT检查申请单（新）），项目为：胸部CT平扫", "医疗医嘱：", "其他建议："]

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
2026-08-10 19:03:30,686 INFO     29 [qwen-vl-text] coord API raw response (len=3220):
[
	{"text": "门诊病历", "bbox": [408, 15, 590, 44]},
	{"text": "性别：女", "bbox": [62, 82, 120, 102]},
	{"text": "年龄：61岁", "bbox": [62, 109, 144, 129]},
	{"text": "民族：汉族", "bbox": [62, 137, 142, 157]},
	{"text": "婚姻：已婚", "bbox": [62, 164, 142, 184]},
	{"text": "职业：农民", "bbox": [62, 191, 142, 211]},
	{"text": "证件类型：居民身份证", "bbox": [536, 55, 734, 75]},
	{"text": "证件号码", "bbox": [536, 85, 618, 105]},
	{"text": "门诊编号", "bbox": [536, 113, 616, 133]},
	{"text": "就诊医院", "bbox": [536, 141, 616, 160]},
	{"text": "就诊科室：", "bbox": [536, 168, 625, 188]},
	{"text": "就诊日期：2024-08-13 08:50:41", "bbox": [536, 195, 832, 214]},
	{"text": "初诊/复诊：初诊  复诊", "bbox": [536, 222, 778, 241]},
	{"text": "陪检者姓名：", "bbox": [27, 223, 140, 243]},
	{"text": "陪检者与患者的关系：", "bbox": [27, 249, 220, 269]},
	{"text": "联系电话", "bbox": [536, 250, 595, 269]},
	{"text": "处方", "bbox": [223, 283, 279, 308]},
	{"text": "检查", "bbox": [387, 283, 444, 308]},
	{"text": "检验", "bbox": [555, 283, 612, 308]},
	{"text": "医疗医嘱", "bbox": [723, 283, 789, 308]},
	{"text": "主诉：肺Ca术后3年余，肺结节？", "bbox": [67, 320, 376, 340]},
	{"text": "现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "bbox": [67, 346, 972, 366]},
	{"text": "ins突变阳性。", "bbox": [27, 372, 153, 391]},
	{"text": "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "bbox": [67, 396, 972, 416]},
	{"text": "节，较前变化不著，请结合临床、随诊复查。", "bbox": [27, 421, 444, 441]},
	{"text": "既往史：否认其他病史。", "bbox": [70, 445, 300, 465]},
	{"text": "家族史：否认家族史", "bbox": [70, 470, 268, 490]},
	{"text": "过敏史：无", "bbox": [70, 494, 184, 514]},
	{"text": "体温（℃）", "bbox": [70, 518, 167, 538]},
	{"text": "脉博（次/分）", "bbox": [507, 518, 632, 538]},
	{"text": "收缩压（mmHg）", "bbox": [70, 542, 209, 562]},
	{"text": "舒张压（mmHg）", "bbox": [454, 542, 590, 562]},
	{"text": "呼吸（次/分）", "bbox": [70, 566, 200, 586]},
	{"text": "意识状态  清醒", "bbox": [486, 566, 632, 586]},
	{"text": "主要症状和体征：", "bbox": [74, 590, 240, 610]},
	{"text": "体格检查：", "bbox": [74, 614, 174, 634]},
	{"text": "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "bbox": [74, 638, 965, 658]},
	{"text": "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "bbox": [36, 662, 965, 682]},
	{"text": "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "bbox": [36, 686, 965, 706]},
	{"text": "3*2.5cm，查见淋巴结转移癌", "bbox": [36, 710, 298, 730]},
	{"text": "初步诊断：肺癌", "bbox": [47, 730, 225, 750]},
	{"text": "修正诊断：肺癌术后", "bbox": [47, 756, 267, 776]},
	{"text": "处", "bbox": [47, 785, 67, 803]},
	{"text": "方：", "bbox": [103, 785, 135, 803]},
	{"text": "检", "bbox": [47, 811, 67, 829]},
	{"text": "验：", "bbox": [103, 811, 135, 829]},
	{"text": "门诊检验申请单（生化检验申请单），项目为：血生化 肝功 血脂（生化室）肾功（生", "bbox": [174, 808, 960, 828]},
	{"text": "化）", "bbox": [135, 833, 164, 853]},
	{"text": "门诊检验申请单（门诊检验申请单），项目为：血细胞分析五分类（静脉）（门化）", "bbox": [174, 855, 876, 875]},
	{"text": "门诊检验申请单（中心检验申请单），项目为：AFP-甲胎蛋白 CEA-癌胚抗原 NSE-神经", "bbox": [174, 878, 957, 898]},
	{"text": "元特异性烯化醇酶 非小细胞癌相关抗原（中心）", "bbox": [135, 902, 556, 922]},
	{"text": "检", "bbox": [52, 920, 72, 938]},
	{"text": "查：", "bbox": [107, 920, 140, 938]},
	{"text": "门诊检查申请单（CT检查申请单（新）），项目为：胸部CT平扫", "bbox": [174, 920, 711, 940]},
	{"text": "医疗医嘱：", "bbox": [55, 945, 146, 964]},
	{"text": "其他建议：", "bbox": [55, 970, 146, 989]}
]
2026-08-10 19:03:30,686 INFO     29 [qwen-vl-text] coord API: raw_items=56, valid_items=56, elapsed=15.7s
2026-08-10 19:03:30,686 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[408, 15, 590, 44]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[1]: text=性别：女, bbox=[62, 82, 120, 102]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：61岁, bbox=[62, 109, 144, 129]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[3]: text=民族：汉族, bbox=[62, 137, 142, 157]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[4]: text=婚姻：已婚, bbox=[62, 164, 142, 184]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[5]: text=职业：农民, bbox=[62, 191, 142, 211]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[6]: text=证件类型：居民身份证, bbox=[536, 55, 734, 75]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[7]: text=证件号码, bbox=[536, 85, 618, 105]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[8]: text=门诊编号, bbox=[536, 113, 616, 133]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[9]: text=就诊医院, bbox=[536, 141, 616, 160]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[10]: text=就诊科室：, bbox=[536, 168, 625, 188]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[11]: text=就诊日期：2024-08-13 08:50:41, bbox=[536, 195, 832, 214]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[12]: text=初诊/复诊：初诊  复诊, bbox=[536, 222, 778, 241]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[13]: text=陪检者姓名：, bbox=[27, 223, 140, 243]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[14]: text=陪检者与患者的关系：, bbox=[27, 249, 220, 269]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[15]: text=联系电话, bbox=[536, 250, 595, 269]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[16]: text=处方, bbox=[223, 283, 279, 308]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[17]: text=检查, bbox=[387, 283, 444, 308]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[18]: text=检验, bbox=[555, 283, 612, 308]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[19]: text=医疗医嘱, bbox=[723, 283, 789, 308]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[20]: text=主诉：肺Ca术后3年余，肺结节？, bbox=[67, 320, 376, 340]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[21]: text=现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-, bbox=[67, 346, 972, 366]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[22]: text=ins突变阳性。, bbox=[27, 372, 153, 391]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[23]: text=2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结, bbox=[67, 396, 972, 416]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[24]: text=节，较前变化不著，请结合临床、随诊复查。, bbox=[27, 421, 444, 441]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[25]: text=既往史：否认其他病史。, bbox=[70, 445, 300, 465]
2026-08-10 19:03:30,688 INFO     29 [qwen-vl-text] coord item[26]: text=家族史：否认家族史, bbox=[70, 470, 268, 490]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[27]: text=过敏史：无, bbox=[70, 494, 184, 514]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[28]: text=体温（℃）, bbox=[70, 518, 167, 538]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[29]: text=脉博（次/分）, bbox=[507, 518, 632, 538]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[30]: text=收缩压（mmHg）, bbox=[70, 542, 209, 562]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[31]: text=舒张压（mmHg）, bbox=[454, 542, 590, 562]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[32]: text=呼吸（次/分）, bbox=[70, 566, 200, 586]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[33]: text=意识状态  清醒, bbox=[486, 566, 632, 586]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[34]: text=主要症状和体征：, bbox=[74, 590, 240, 610]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[35]: text=体格检查：, bbox=[74, 614, 174, 634]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[36]: text=辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结, bbox=[74, 638, 965, 658]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[37]: text=节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底, bbox=[36, 662, 965, 682]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[38]: text=段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小, bbox=[36, 686, 965, 706]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[39]: text=3*2.5cm，查见淋巴结转移癌, bbox=[36, 710, 298, 730]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[40]: text=初步诊断：肺癌, bbox=[47, 730, 225, 750]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[41]: text=修正诊断：肺癌术后, bbox=[47, 756, 267, 776]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[42]: text=处, bbox=[47, 785, 67, 803]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[43]: text=方：, bbox=[103, 785, 135, 803]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[44]: text=检, bbox=[47, 811, 67, 829]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[45]: text=验：, bbox=[103, 811, 135, 829]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[46]: text=门诊检验申请单（生化检验申请单），项目为：血生化 肝功 血脂（生化室）肾功（生, bbox=[174, 808, 960, 828]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[47]: text=化）, bbox=[135, 833, 164, 853]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[48]: text=门诊检验申请单（门诊检验申请单），项目为：血细胞分析五分类（静脉）（门化）, bbox=[174, 855, 876, 875]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[49]: text=门诊检验申请单（中心检验申请单），项目为：AFP-甲胎蛋白 CEA-癌胚抗原 NSE-神经, bbox=[174, 878, 957, 898]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[50]: text=元特异性烯化醇酶 非小细胞癌相关抗原（中心）, bbox=[135, 902, 556, 922]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[51]: text=检, bbox=[52, 920, 72, 938]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[52]: text=查：, bbox=[107, 920, 140, 938]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[53]: text=门诊检查申请单（CT检查申请单（新）），项目为：胸部CT平扫, bbox=[174, 920, 711, 940]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[54]: text=医疗医嘱：, bbox=[55, 945, 146, 964]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] coord item[55]: text=其他建议：, bbox=[55, 970, 146, 989]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] page=6 — 56/56 coords, api_time=15.7s
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] new_positions (56):
[[6, 167.28, 241.89999999999998, 8.01, 23.496000000000002], [6, 25.419999999999998, 49.199999999999996, 43.788000000000004, 54.468], [6, 25.419999999999998, 59.04, 58.206, 68.88600000000001], [6, 25.419999999999998, 58.22, 73.158, 83.83800000000001], [6, 25.419999999999998, 58.22, 87.57600000000001, 98.256], [6, 25.419999999999998, 58.22, 101.994, 112.674], [6, 219.76, 300.94, 29.37, 40.050000000000004], [6, 219.76, 253.38, 45.39, 56.07], [6, 219.76, 252.55999999999997, 60.342000000000006, 71.022], [6, 219.76, 252.55999999999997, 75.29400000000001, 85.44], [6, 219.76, 256.25, 89.712, 100.39200000000001], [6, 219.76, 341.12, 104.13000000000001, 114.27600000000001], [6, 219.76, 318.97999999999996, 118.548, 128.69400000000002], [6, 11.069999999999999, 57.4, 119.08200000000001, 129.762], [6, 11.069999999999999, 90.19999999999999, 132.966, 143.64600000000002], [6, 219.76, 243.95, 133.5, 143.64600000000002], [6, 91.42999999999999, 114.38999999999999, 151.122, 164.472], [6, 158.67, 182.04, 151.122, 164.472], [6, 227.54999999999998, 250.92, 151.122, 164.472], [6, 296.43, 323.49, 151.122, 164.472], [6, 27.47, 154.16, 170.88, 181.56], [6, 27.47, 398.52, 184.764, 195.44400000000002], [6, 11.069999999999999, 62.73, 198.64800000000002, 208.794], [6, 27.47, 398.52, 211.464, 222.144], [6, 11.069999999999999, 182.04, 224.81400000000002, 235.494], [6, 28.7, 122.99999999999999, 237.63000000000002, 248.31], [6, 28.7, 109.88, 250.98000000000002, 261.66], [6, 28.7, 75.44, 263.796, 274.476], [6, 28.7, 68.47, 276.612, 287.29200000000003], [6, 207.86999999999998, 259.12, 276.612, 287.29200000000003], [6, 28.7, 85.69, 289.428, 300.108], [6, 186.14, 241.89999999999998, 289.428, 300.108], [6, 28.7, 82.0, 302.244, 312.92400000000004], [6, 199.26, 259.12, 302.244, 312.92400000000004], [6, 30.34, 98.39999999999999, 315.06, 325.74], [6, 30.34, 71.33999999999999, 327.87600000000003, 338.55600000000004], [6, 30.34, 395.65, 340.692, 351.372], [6, 14.76, 395.65, 353.50800000000004, 364.18800000000005], [6, 14.76, 395.65, 366.324, 377.004], [6, 14.76, 122.17999999999999, 379.14000000000004, 389.82000000000005], [6, 19.27, 92.25, 389.82000000000005, 400.5], [6, 19.27, 109.47, 403.704, 414.384], [6, 19.27, 27.47, 419.19, 428.802], [6, 42.23, 55.349999999999994, 419.19, 428.802], [6, 19.27, 27.47, 433.074, 442.68600000000004], [6, 42.23, 55.349999999999994, 433.074, 442.68600000000004], [6, 71.33999999999999, 393.59999999999997, 431.47200000000004, 442.15200000000004], [6, 55.349999999999994, 67.24, 444.822, 455.502], [6, 71.33999999999999, 359.15999999999997, 456.57000000000005, 467.25], [6, 71.33999999999999, 392.37, 468.85200000000003, 479.53200000000004], [6, 55.349999999999994, 227.95999999999998, 481.668, 492.348], [6, 21.32, 29.52, 491.28000000000003, 500.89200000000005], [6, 43.87, 57.4, 491.28000000000003, 500.89200000000005], [6, 71.33999999999999, 291.51, 491.28000000000003, 501.96000000000004], [6, 22.549999999999997, 59.86, 504.63000000000005, 514.7760000000001], [6, 22.549999999999997, 59.86, 517.98, 528.126]]
2026-08-10 19:03:30,689 INFO     29 [qwen-vl-text] ═══ DONE ═══ 56 positions, pages=1, time=23.0s
2026-08-10 19:03:30,690 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:03:30,691 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:03:30,691 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 19:03:30,691 INFO     29 [qwen-vl-text] positions(50): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:03:30,691 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [50]
2026-08-10 19:03:30,899 INFO     29 [qwen-vl-text] page=7, rect=410x466, img=(1139x1295), dpi=200
2026-08-10 19:03:30,900 INFO     29 [qwen-vl-text] LLM extraction start, text_len=634
2026-08-10 19:03:30,900 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:03:30,901 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 282, \"bbox_end\": 331, \"encounter_dates\": [\"2025-08-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n性别：女\n证件类型：居民身份证\n年龄：62岁\n证件\n民族：汉族\n门诊编\n婚姻：已婚\n就诊医院\n职业：农民\n就诊科室\n就诊日期：2025-08-12 08:11:41\n陪检者姓名：\n初诊/复诊：初诊□复诊\n陪检者与患者的关系：\n联系电话\n处方\n检查\n检验\n医疗医嘱\n主诉：肺Ca术后3年余，肺结节？\n现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-\nins突变阳性。\n2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结\n节，较前变化不著，请结合临床、随诊复查。\n既往史：否认其他病史。\n家族史：否认家族史\n过敏史：无\n体温（℃）\n脉搏（次/分）\n收缩压（mmHg）\n舒张压（mmHg）\n呼吸（次/分）\n意识状态 清醒\n主要症状和体征：\n体格检查：\n辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结\n节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底\n段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小\n3*2.5cm，查见淋巴结转移癌\n初步诊断：肺癌\n修正诊断：肺癌术后\n处\n方：\n检\n验：\n检\n查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫\n医疗医嘱：\n其他建议：",
    "role": "user"
  }
]
2026-08-10 19:03:37,258 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:03:37,259 INFO     29 [qwen-vl-text] LLM output (len=332):
{
  "encounter_date": "2025-08-12",
  "chief_complaint": "肺Ca术后3年余，肺结节？",
  "present_illness": "3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-ins突变阳性。2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结节，较前变化不著，请结合临床、随诊复查。",
  "past_history": "否认其他病史。",
  "diagnosis": "肺癌术后",
  "treatment_plan": "门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫"
}
2026-08-10 19:03:37,259 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-08-12]
2026-08-10 19:03:37,269 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3495883, prompt_len=1397
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共50行）
["门诊病历", "性别：女", "证件类型：居民身份证", "年龄：62岁", "证件", "民族：汉族", "门诊编", "婚姻：已婚", "就诊医院", "职业：农民", "就诊科室", "就诊日期：2025-08-12 08:11:41", "陪检者姓名：", "初诊/复诊：初诊□复诊", "陪检者与患者的关系：", "联系电话", "处方", "检查", "检验", "医疗医嘱", "主诉：肺Ca术后3年余，肺结节？", "现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "ins突变阳性。", "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "节，较前变化不著，请结合临床、随诊复查。", "既往史：否认其他病史。", "家族史：否认家族史", "过敏史：无", "体温（℃）", "脉搏（次/分）", "收缩压（mmHg）", "舒张压（mmHg）", "呼吸（次/分）", "意识状态 清醒", "主要症状和体征：", "体格检查：", "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "3*2.5cm，查见淋巴结转移癌", "初步诊断：肺癌", "修正诊断：肺癌术后", "处", "方：", "检", "验：", "检", "查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫", "医疗医嘱：", "其他建议："]

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
2026-08-10 19:04:00,733 INFO     29 [qwen-vl-text] coord API raw response (len=4227):
[
	{"text": "门诊病历", "bbox": [388, 5, 565, 35]},
	{"text": "性别：女", "bbox": [54, 81, 110, 104], "bbox": [15, 54, 110, 77]},
	{"text": "证件类型：居民身份证", "bbox": [514, 48, 705, 69], "bbox": [514, 48, 705, 69]},
	{"text": "年龄：62岁", "bbox": [54, 110, 133, 132], "bbox": [15, 109, 133, 132]},
	{"text": "证件", "bbox": [514, 81, 550, 101], "bbox": [514, 81, 550, 101]},
	{"text": "民族：汉族", "bbox": [54, 140, 131, 162], "bbox": [15, 139, 131, 162]},
	{"text": "门诊编", "bbox": [514, 112, 585, 132], "bbox": [514, 112, 585, 132]},
	{"text": "婚姻：已婚", "bbox": [54, 169, 131, 191], "bbox": [15, 169, 131, 191]},
	{"text": "就诊医院", "bbox": [514, 142, 588, 162], "bbox": [514, 142, 588, 162]},
	{"text": "职业：农民", "bbox": [54, 199, 133, 221], "bbox": [15, 199, 133, 221]},
	{"text": "就诊科室", "bbox": [514, 172, 588, 192], "bbox": [514, 172, 588, 192]},
	{"text": "就诊日期：2025-08-12 08:11:41", "bbox": [514, 201, 800, 221], "bbox": [514, 201, 800, 221]},
	{"text": "陪检者姓名：", "bbox": [23, 235, 130, 256], "bbox": [23, 235, 130, 256]},
	{"text": "初诊/复诊：初诊□复诊", "bbox": [514, 232, 748, 253], "bbox": [514, 232, 748, 253]},
	{"text": "陪检者与患者的关系：", "bbox": [23, 265, 207, 286], "bbox": [23, 265, 207, 286]},
	{"text": "联系电话", "bbox": [514, 264, 586, 284], "bbox": [514, 264, 586, 284]},
	{"text": "处方", "bbox": [168, 298, 265, 330], "bbox": [168, 298, 265, 330]},
	{"text": "检查", "bbox": [325, 298, 425, 330], "bbox": [325, 298, 425, 330]},
	{"text": "检验", "bbox": [487, 298, 586, 330], "bbox": [487, 298, 586, 330]},
	{"text": "医疗医嘱", "bbox": [658, 298, 758, 330], "bbox": [658, 298, 758, 330]},
	{"text": "主诉：肺Ca术后3年余，肺结节？", "bbox": [62, 343, 360, 365], "bbox": [62, 343, 360, 365]},
	{"text": "现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "bbox": [62, 369, 938, 391], "bbox": [62, 369, 938, 391]},
	{"text": "ins突变阳性。", "bbox": [23, 399, 144, 420], "bbox": [23, 399, 144, 420]},
	{"text": "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "bbox": [62, 424, 938, 446], "bbox": [62, 424, 938, 446]},
	{"text": "节，较前变化不著，请结合临床、随诊复查。", "bbox": [23, 453, 425, 475], "bbox": [23, 453, 425, 475]},
	{"text": "既往史：否认其他病史。", "bbox": [65, 480, 287, 502], "bbox": [65, 480, 287, 502]},
	{"text": "家族史：否认家族史", "bbox": [65, 507, 255, 528], "bbox": [65, 507, 255, 528]},
	{"text": "过敏史：无", "bbox": [65, 534, 173, 555], "bbox": [65, 534, 173, 555]},
	{"text": "体温（℃）", "bbox": [68, 559, 158, 580], "bbox": [68, 559, 158, 580]},
	{"text": "脉搏（次/分）", "bbox": [485, 559, 606, 580], "bbox": [485, 559, 606, 580]},
	{"text": "收缩压（mmHg）", "bbox": [68, 586, 200, 607], "bbox": [68, 586, 200, 607]},
	{"text": "舒张压（mmHg）", "bbox": [435, 586, 565, 607], "bbox": [435, 586, 565, 607]},
	{"text": "呼吸（次/分）", "bbox": [68, 612, 190, 633], "bbox": [68, 612, 190, 633]},
	{"text": "意识状态 清醒", "bbox": [465, 612, 607, 633], "bbox": [465, 612, 607, 633]},
	{"text": "主要症状和体征：", "bbox": [72, 639, 230, 660], "bbox": [72, 639, 230, 660]},
	{"text": "体格检查：", "bbox": [72, 665, 168, 686], "bbox": [72, 665, 168, 686]},
	{"text": "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "bbox": [72, 690, 927, 712], "bbox": [72, 690, 927, 712]},
	{"text": "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "bbox": [37, 717, 927, 739], "bbox": [37, 717, 927, 739]},
	{"text": "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "bbox": [37, 743, 927, 765], "bbox": [37, 743, 927, 765]},
	{"text": "3*2.5cm，查见淋巴结转移癌", "bbox": [37, 770, 287, 791], "bbox": [37, 770, 287, 791]},
	{"text": "初步诊断：肺癌", "bbox": [46, 815, 217, 836], "bbox": [46, 815, 217, 836]},
	{"text": "修正诊断：肺癌术后", "bbox": [46, 843, 257, 864], "bbox": [46, 843, 257, 864]},
	{"text": "处", "bbox": [46, 873, 68, 893], "bbox": [46, 873, 68, 893]},
	{"text": "方：", "bbox": [100, 873, 131, 893], "bbox": [100, 873, 131, 893]},
	{"text": "检", "bbox": [46, 899, 68, 919], "bbox": [46, 899, 68, 919]},
	{"text": "验：", "bbox": [100, 899, 131, 919], "bbox": [100, 899, 131, 919]},
	{"text": "检", "bbox": [46, 926, 68, 946], "bbox": [46, 926, 68, 946]},
	{"text": "查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫", "bbox": [100, 926, 670, 946], "bbox": [100, 926, 670, 946]},
	{"text": "医疗医嘱：", "bbox": [52, 956, 140, 976], "bbox": [52, 956, 140, 976]},
	{"text": "其他建议：", "bbox": [52, 982, 140, 999], "bbox": [52, 982, 140, 999]}
]
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord API: raw_items=50, valid_items=50, elapsed=23.5s
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[388, 5, 565, 35]
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord item[1]: text=性别：女, bbox=[15, 54, 110, 77]
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord item[2]: text=证件类型：居民身份证, bbox=[514, 48, 705, 69]
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：62岁, bbox=[15, 109, 133, 132]
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord item[4]: text=证件, bbox=[514, 81, 550, 101]
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord item[5]: text=民族：汉族, bbox=[15, 139, 131, 162]
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord item[6]: text=门诊编, bbox=[514, 112, 585, 132]
2026-08-10 19:04:00,734 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻：已婚, bbox=[15, 169, 131, 191]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[8]: text=就诊医院, bbox=[514, 142, 588, 162]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[9]: text=职业：农民, bbox=[15, 199, 133, 221]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[10]: text=就诊科室, bbox=[514, 172, 588, 192]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[11]: text=就诊日期：2025-08-12 08:11:41, bbox=[514, 201, 800, 221]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[12]: text=陪检者姓名：, bbox=[23, 235, 130, 256]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[13]: text=初诊/复诊：初诊□复诊, bbox=[514, 232, 748, 253]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[14]: text=陪检者与患者的关系：, bbox=[23, 265, 207, 286]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[15]: text=联系电话, bbox=[514, 264, 586, 284]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[16]: text=处方, bbox=[168, 298, 265, 330]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[17]: text=检查, bbox=[325, 298, 425, 330]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[18]: text=检验, bbox=[487, 298, 586, 330]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[19]: text=医疗医嘱, bbox=[658, 298, 758, 330]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[20]: text=主诉：肺Ca术后3年余，肺结节？, bbox=[62, 343, 360, 365]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[21]: text=现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-, bbox=[62, 369, 938, 391]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[22]: text=ins突变阳性。, bbox=[23, 399, 144, 420]
2026-08-10 19:04:00,735 INFO     29 [qwen-vl-text] coord item[23]: text=2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结, bbox=[62, 424, 938, 446]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[24]: text=节，较前变化不著，请结合临床、随诊复查。, bbox=[23, 453, 425, 475]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[25]: text=既往史：否认其他病史。, bbox=[65, 480, 287, 502]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[26]: text=家族史：否认家族史, bbox=[65, 507, 255, 528]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[27]: text=过敏史：无, bbox=[65, 534, 173, 555]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[28]: text=体温（℃）, bbox=[68, 559, 158, 580]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[29]: text=脉搏（次/分）, bbox=[485, 559, 606, 580]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[30]: text=收缩压（mmHg）, bbox=[68, 586, 200, 607]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[31]: text=舒张压（mmHg）, bbox=[435, 586, 565, 607]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[32]: text=呼吸（次/分）, bbox=[68, 612, 190, 633]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[33]: text=意识状态 清醒, bbox=[465, 612, 607, 633]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[34]: text=主要症状和体征：, bbox=[72, 639, 230, 660]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[35]: text=体格检查：, bbox=[72, 665, 168, 686]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[36]: text=辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结, bbox=[72, 690, 927, 712]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[37]: text=节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底, bbox=[37, 717, 927, 739]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[38]: text=段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小, bbox=[37, 743, 927, 765]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[39]: text=3*2.5cm，查见淋巴结转移癌, bbox=[37, 770, 287, 791]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[40]: text=初步诊断：肺癌, bbox=[46, 815, 217, 836]
2026-08-10 19:04:00,736 INFO     29 [qwen-vl-text] coord item[41]: text=修正诊断：肺癌术后, bbox=[46, 843, 257, 864]
2026-08-10 19:04:00,737 INFO     29 [qwen-vl-text] coord item[42]: text=处, bbox=[46, 873, 68, 893]
2026-08-10 19:04:00,737 INFO     29 [qwen-vl-text] coord item[43]: text=方：, bbox=[100, 873, 131, 893]
2026-08-10 19:04:00,737 INFO     29 [qwen-vl-text] coord item[44]: text=检, bbox=[46, 899, 68, 919]
2026-08-10 19:04:00,737 INFO     29 [qwen-vl-text] coord item[45]: text=验：, bbox=[100, 899, 131, 919]
2026-08-10 19:04:00,737 INFO     29 [qwen-vl-text] coord item[46]: text=检, bbox=[46, 926, 68, 946]
2026-08-10 19:04:00,737 INFO     29 [qwen-vl-text] coord item[47]: text=查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫, bbox=[100, 926, 670, 946]
2026-08-10 19:04:00,737 INFO     29 [qwen-vl-text] coord item[48]: text=医疗医嘱：, bbox=[52, 956, 140, 976]
2026-08-10 19:04:00,737 INFO     29 [qwen-vl-text] coord item[49]: text=其他建议：, bbox=[52, 982, 140, 999]
2026-08-10 19:04:00,738 INFO     29 [qwen-vl-text] page=7 — 50/50 coords, api_time=23.5s
2026-08-10 19:04:00,739 INFO     29 [qwen-vl-text] new_positions (50):
[[7, 159.07999999999998, 231.64999999999998, 2.33, 16.310000000000002], [7, 6.1499999999999995, 45.099999999999994, 25.164, 35.882000000000005], [7, 210.73999999999998, 289.04999999999995, 22.368000000000002, 32.154], [7, 6.1499999999999995, 54.529999999999994, 50.794000000000004, 61.512], [7, 210.73999999999998, 225.5, 37.746, 47.066], [7, 6.1499999999999995, 53.709999999999994, 64.774, 75.492], [7, 210.73999999999998, 239.85, 52.192, 61.512], [7, 6.1499999999999995, 53.709999999999994, 78.754, 89.006], [7, 210.73999999999998, 241.07999999999998, 66.172, 75.492], [7, 6.1499999999999995, 54.529999999999994, 92.73400000000001, 102.986], [7, 210.73999999999998, 241.07999999999998, 80.152, 89.47200000000001], [7, 210.73999999999998, 328.0, 93.66600000000001, 102.986], [7, 9.43, 53.3, 109.51, 119.296], [7, 210.73999999999998, 306.68, 108.11200000000001, 117.89800000000001], [7, 9.43, 84.86999999999999, 123.49000000000001, 133.276], [7, 210.73999999999998, 240.26, 123.024, 132.344], [7, 68.88, 108.64999999999999, 138.868, 153.78], [7, 133.25, 174.25, 138.868, 153.78], [7, 199.67, 240.26, 138.868, 153.78], [7, 269.78, 310.78, 138.868, 153.78], [7, 25.419999999999998, 147.6, 159.83800000000002, 170.09], [7, 25.419999999999998, 384.58, 171.954, 182.20600000000002], [7, 9.43, 59.04, 185.934, 195.72], [7, 25.419999999999998, 384.58, 197.584, 207.836], [7, 9.43, 174.25, 211.098, 221.35000000000002], [7, 26.65, 117.66999999999999, 223.68, 233.93200000000002], [7, 26.65, 104.55, 236.262, 246.048], [7, 26.65, 70.92999999999999, 248.84400000000002, 258.63], [7, 27.88, 64.78, 260.494, 270.28000000000003], [7, 198.85, 248.45999999999998, 260.494, 270.28000000000003], [7, 27.88, 82.0, 273.076, 282.862], [7, 178.35, 231.64999999999998, 273.076, 282.862], [7, 27.88, 77.89999999999999, 285.192, 294.978], [7, 190.64999999999998, 248.86999999999998, 285.192, 294.978], [7, 29.52, 94.3, 297.774, 307.56], [7, 29.52, 68.88, 309.89000000000004, 319.67600000000004], [7, 29.52, 380.07, 321.54, 331.79200000000003], [7, 15.17, 380.07, 334.122, 344.374], [7, 15.17, 380.07, 346.238, 356.49], [7, 15.17, 117.66999999999999, 358.82, 368.606], [7, 18.86, 88.97, 379.79, 389.576], [7, 18.86, 105.36999999999999, 392.838, 402.624], [7, 18.86, 27.88, 406.81800000000004, 416.13800000000003], [7, 41.0, 53.709999999999994, 406.81800000000004, 416.13800000000003], [7, 18.86, 27.88, 418.934, 428.254], [7, 41.0, 53.709999999999994, 418.934, 428.254], [7, 18.86, 27.88, 431.516, 440.836], [7, 41.0, 274.7, 431.516, 440.836], [7, 21.32, 57.4, 445.49600000000004, 454.81600000000003], [7, 21.32, 57.4, 457.612, 465.53400000000005]]
2026-08-10 19:04:00,739 INFO     29 [qwen-vl-text] ═══ DONE ═══ 50 positions, pages=1, time=30.0s
2026-08-10 19:04:00,739 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:04:00,749 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:04:00,750 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 19:04:00,750 INFO     29 [qwen-vl-text] positions(50): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:04:00,750 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [50]
2026-08-10 19:04:01,003 INFO     29 [qwen-vl-text] page=8, rect=410x547, img=(1139x1520), dpi=200
2026-08-10 19:04:01,005 INFO     29 [qwen-vl-text] LLM extraction start, text_len=740
2026-08-10 19:04:01,005 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:04:01,005 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 332, \"bbox_end\": 381, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n性别：女\n年龄：63岁\n民族：汉族\n婚姻：已婚\n职业：农民\n证件类型：居民身份证\n证件号\n门诊编\n就诊医院\n就诊科室\n就诊日期：2026-03-10 08:35:11\n初诊/复诊：初诊 □ 复诊\n联系电\n陪伴者姓名：\n陪伴者与患者的关系：\n处方\n检查\n检验\n医疗医嘱\n主诉：肺Ca术后4年余，肺结节？\n现病史：4年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-\nins突变阳性。\n2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结\n节，较前变化不著，请结合临床、随诊复查。\n2025.8.11CT：双肺多发小结节，较大者位于左肺外周，均较前片变化不著\n既往史：否认其他病史。\n家族史：否认家族史\n过敏史：无\n体温（℃）\n脉搏（次/分）\n收缩压（mmHg）\n舒张压（mmHg）\n呼吸（次/分）\n意识状态 清醒\n主要症状和体征：\n体格检查：\n辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结\n节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底\n段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小\n3*2.5cm，查见淋巴结转移癌\n初步诊断：肺癌,肺结节\n修正诊断：肺癌,肺结节\n处方：\n检验：门诊检验申请单(临床生化检验一(临床生化检验))，项目为：血糖 糖化血红蛋白测定\n检查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫\n医疗医嘱：\n其他建议：\n已告知患者病情及可能的药物不良反应。\n医生",
    "role": "user"
  }
]
2026-08-10 19:04:01,007 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:04:01.006+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 88, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:04:06,604 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:04:06,604 INFO     29 [qwen-vl-text] LLM output (len=350):
{
  "encounter_date": "2026-03-10",
  "chief_complaint": "肺Ca术后4年余，肺结节？",
  "present_illness": "4年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-ins突变阳性。\n2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结节，较前变化不著，请结合临床、随诊复查。\n2025.8.11CT：双肺多发小结节，较大者位于左肺外周，均较前片变化不著",
  "past_history": "否认其他病史。",
  "diagnosis": "肺癌,肺结节",
  "treatment_plan": null
}
2026-08-10 19:04:06,604 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-10]
2026-08-10 19:04:06,618 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4273643, prompt_len=1503
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共50行）
["门诊病历", "性别：女", "年龄：63岁", "民族：汉族", "婚姻：已婚", "职业：农民", "证件类型：居民身份证", "证件号", "门诊编", "就诊医院", "就诊科室", "就诊日期：2026-03-10 08:35:11", "初诊/复诊：初诊 □ 复诊", "联系电", "陪伴者姓名：", "陪伴者与患者的关系：", "处方", "检查", "检验", "医疗医嘱", "主诉：肺Ca术后4年余，肺结节？", "现病史：4年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "ins突变阳性。", "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "节，较前变化不著，请结合临床、随诊复查。", "2025.8.11CT：双肺多发小结节，较大者位于左肺外周，均较前片变化不著", "既往史：否认其他病史。", "家族史：否认家族史", "过敏史：无", "体温（℃）", "脉搏（次/分）", "收缩压（mmHg）", "舒张压（mmHg）", "呼吸（次/分）", "意识状态 清醒", "主要症状和体征：", "体格检查：", "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "3*2.5cm，查见淋巴结转移癌", "初步诊断：肺癌,肺结节", "修正诊断：肺癌,肺结节", "处方：", "检验：门诊检验申请单(临床生化检验一(临床生化检验))，项目为：血糖 糖化血红蛋白测定", "检查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫", "医疗医嘱：", "其他建议：", "已告知患者病情及可能的药物不良反应。", "医生"]

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
2026-08-10 19:04:23,328 INFO     29 [qwen-vl-text] coord API raw response (len=2899):
[
	{"text": "门诊病历", "bbox": [388, 7, 565, 32]},
	{"text": "性别：女", "bbox": [18, 73, 109, 93]},
	{"text": "年龄：63岁", "bbox": [18, 98, 132, 118]},
	{"text": "民族：汉族", "bbox": [18, 123, 130, 143]},
	{"text": "婚姻：已婚", "bbox": [18, 148, 130, 168]},
	{"text": "职业：农民", "bbox": [18, 173, 130, 193]},
	{"text": "证件类型：居民身份证", "bbox": [513, 43, 707, 63]},
	{"text": "证件号", "bbox": [513, 70, 571, 90]},
	{"text": "门诊编", "bbox": [513, 97, 590, 117]},
	{"text": "就诊医院", "bbox": [513, 123, 588, 143]},
	{"text": "就诊科室", "bbox": [513, 150, 588, 170]},
	{"text": "就诊日期：2026-03-10 08:35:11", "bbox": [513, 176, 804, 195]},
	{"text": "初诊/复诊：初诊 □ 复诊", "bbox": [513, 202, 750, 222]},
	{"text": "联系电", "bbox": [513, 229, 567, 248]},
	{"text": "陪伴者姓名：", "bbox": [21, 204, 128, 222]},
	{"text": "陪伴者与患者的关系：", "bbox": [21, 230, 206, 249]},
	{"text": "处方", "bbox": [165, 259, 262, 290]},
	{"text": "检查", "bbox": [322, 259, 422, 290]},
	{"text": "检验", "bbox": [485, 259, 585, 290]},
	{"text": "医疗医嘱", "bbox": [658, 260, 760, 290]},
	{"text": "主诉：肺Ca术后4年余，肺结节？", "bbox": [60, 297, 357, 317]},
	{"text": "现病史：4年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-", "bbox": [60, 322, 942, 342]},
	{"text": "ins突变阳性。", "bbox": [21, 347, 142, 366]},
	{"text": "2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结", "bbox": [60, 370, 942, 390]},
	{"text": "节，较前变化不著，请结合临床、随诊复查。", "bbox": [21, 394, 424, 414]},
	{"text": "2025.8.11CT：双肺多发小结节，较大者位于左肺外周，均较前片变化不著", "bbox": [60, 417, 733, 437]},
	{"text": "既往史：否认其他病史。", "bbox": [60, 440, 284, 460]},
	{"text": "家族史：否认家族史", "bbox": [60, 463, 252, 483]},
	{"text": "过敏史：无", "bbox": [60, 486, 170, 505]},
	{"text": "体温（℃）", "bbox": [65, 508, 155, 527]},
	{"text": "脉搏（次/分）", "bbox": [482, 508, 605, 527]},
	{"text": "收缩压（mmHg）", "bbox": [65, 530, 195, 549]},
	{"text": "舒张压（mmHg）", "bbox": [432, 530, 563, 549]},
	{"text": "呼吸（次/分）", "bbox": [65, 552, 186, 571]},
	{"text": "意识状态 清醒", "bbox": [463, 552, 605, 571]},
	{"text": "主要症状和体征：", "bbox": [68, 575, 225, 594]},
	{"text": "体格检查：", "bbox": [68, 597, 162, 616]},
	{"text": "辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结", "bbox": [68, 620, 934, 640]},
	{"text": "节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底", "bbox": [30, 643, 934, 663]},
	{"text": "段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小", "bbox": [30, 666, 934, 686]},
	{"text": "3*2.5cm，查见淋巴结转移癌", "bbox": [30, 688, 282, 708]},
	{"text": "初步诊断：肺癌,肺结节", "bbox": [41, 724, 277, 743]},
	{"text": "修正诊断：肺癌,肺结节", "bbox": [41, 750, 282, 769]},
	{"text": "处方：", "bbox": [41, 776, 127, 795]},
	{"text": "检验：门诊检验申请单(临床生化检验一(临床生化检验))，项目为：血糖 糖化血红蛋白测定", "bbox": [95, 801, 900, 824]},
	{"text": "检查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫", "bbox": [95, 827, 668, 848]},
	{"text": "医疗医嘱：", "bbox": [41, 850, 134, 869]},
	{"text": "其他建议：", "bbox": [41, 873, 134, 892]},
	{"text": "已告知患者病情及可能的药物不良反应。", "bbox": [45, 903, 370, 921]},
	{"text": "医生", "bbox": [638, 913, 675, 928]}
]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord API: raw_items=50, valid_items=50, elapsed=16.7s
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[388, 7, 565, 32]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[1]: text=性别：女, bbox=[18, 73, 109, 93]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：63岁, bbox=[18, 98, 132, 118]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[3]: text=民族：汉族, bbox=[18, 123, 130, 143]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[4]: text=婚姻：已婚, bbox=[18, 148, 130, 168]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[5]: text=职业：农民, bbox=[18, 173, 130, 193]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[6]: text=证件类型：居民身份证, bbox=[513, 43, 707, 63]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[7]: text=证件号, bbox=[513, 70, 571, 90]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[8]: text=门诊编, bbox=[513, 97, 590, 117]
2026-08-10 19:04:23,329 INFO     29 [qwen-vl-text] coord item[9]: text=就诊医院, bbox=[513, 123, 588, 143]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[10]: text=就诊科室, bbox=[513, 150, 588, 170]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[11]: text=就诊日期：2026-03-10 08:35:11, bbox=[513, 176, 804, 195]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[12]: text=初诊/复诊：初诊 □ 复诊, bbox=[513, 202, 750, 222]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[13]: text=联系电, bbox=[513, 229, 567, 248]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[14]: text=陪伴者姓名：, bbox=[21, 204, 128, 222]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[15]: text=陪伴者与患者的关系：, bbox=[21, 230, 206, 249]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[16]: text=处方, bbox=[165, 259, 262, 290]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[17]: text=检查, bbox=[322, 259, 422, 290]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[18]: text=检验, bbox=[485, 259, 585, 290]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[19]: text=医疗医嘱, bbox=[658, 260, 760, 290]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[20]: text=主诉：肺Ca术后4年余，肺结节？, bbox=[60, 297, 357, 317]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[21]: text=现病史：4年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-, bbox=[60, 322, 942, 342]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[22]: text=ins突变阳性。, bbox=[21, 347, 142, 366]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[23]: text=2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结, bbox=[60, 370, 942, 390]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[24]: text=节，较前变化不著，请结合临床、随诊复查。, bbox=[21, 394, 424, 414]
2026-08-10 19:04:23,330 INFO     29 [qwen-vl-text] coord item[25]: text=2025.8.11CT：双肺多发小结节，较大者位于左肺外周，均较前片变化不著, bbox=[60, 417, 733, 437]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[26]: text=既往史：否认其他病史。, bbox=[60, 440, 284, 460]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[27]: text=家族史：否认家族史, bbox=[60, 463, 252, 483]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[28]: text=过敏史：无, bbox=[60, 486, 170, 505]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[29]: text=体温（℃）, bbox=[65, 508, 155, 527]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[30]: text=脉搏（次/分）, bbox=[482, 508, 605, 527]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[31]: text=收缩压（mmHg）, bbox=[65, 530, 195, 549]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[32]: text=舒张压（mmHg）, bbox=[432, 530, 563, 549]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[33]: text=呼吸（次/分）, bbox=[65, 552, 186, 571]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[34]: text=意识状态 清醒, bbox=[463, 552, 605, 571]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[35]: text=主要症状和体征：, bbox=[68, 575, 225, 594]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[36]: text=体格检查：, bbox=[68, 597, 162, 616]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[37]: text=辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结, bbox=[68, 620, 934, 640]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[38]: text=节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底, bbox=[30, 643, 934, 663]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[39]: text=段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小, bbox=[30, 666, 934, 686]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[40]: text=3*2.5cm，查见淋巴结转移癌, bbox=[30, 688, 282, 708]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[41]: text=初步诊断：肺癌,肺结节, bbox=[41, 724, 277, 743]
2026-08-10 19:04:23,331 INFO     29 [qwen-vl-text] coord item[42]: text=修正诊断：肺癌,肺结节, bbox=[41, 750, 282, 769]
2026-08-10 19:04:23,332 INFO     29 [qwen-vl-text] coord item[43]: text=处方：, bbox=[41, 776, 127, 795]
2026-08-10 19:04:23,332 INFO     29 [qwen-vl-text] coord item[44]: text=检验：门诊检验申请单(临床生化检验一(临床生化检验))，项目为：血糖 糖化血红蛋白测定, bbox=[95, 801, 900, 824]
2026-08-10 19:04:23,332 INFO     29 [qwen-vl-text] coord item[45]: text=检查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫, bbox=[95, 827, 668, 848]
2026-08-10 19:04:23,332 INFO     29 [qwen-vl-text] coord item[46]: text=医疗医嘱：, bbox=[41, 850, 134, 869]
2026-08-10 19:04:23,332 INFO     29 [qwen-vl-text] coord item[47]: text=其他建议：, bbox=[41, 873, 134, 892]
2026-08-10 19:04:23,332 INFO     29 [qwen-vl-text] coord item[48]: text=已告知患者病情及可能的药物不良反应。, bbox=[45, 903, 370, 921]
2026-08-10 19:04:23,332 INFO     29 [qwen-vl-text] coord item[49]: text=医生, bbox=[638, 913, 675, 928]
2026-08-10 19:04:23,333 INFO     29 [qwen-vl-text] page=8 — 50/50 coords, api_time=16.7s
2026-08-10 19:04:23,333 INFO     29 [qwen-vl-text] new_positions (50):
[[8, 159.07999999999998, 231.64999999999998, 3.829, 17.504], [8, 7.38, 44.69, 39.931000000000004, 50.871], [8, 7.38, 54.12, 53.606, 64.546], [8, 7.38, 53.3, 67.281, 78.221], [8, 7.38, 53.3, 80.956, 91.896], [8, 7.38, 53.3, 94.631, 105.57100000000001], [8, 210.32999999999998, 289.87, 23.521, 34.461000000000006], [8, 210.32999999999998, 234.10999999999999, 38.290000000000006, 49.230000000000004], [8, 210.32999999999998, 241.89999999999998, 53.059000000000005, 63.999], [8, 210.32999999999998, 241.07999999999998, 67.281, 78.221], [8, 210.32999999999998, 241.07999999999998, 82.05000000000001, 92.99000000000001], [8, 210.32999999999998, 329.64, 96.272, 106.665], [8, 210.32999999999998, 307.5, 110.49400000000001, 121.43400000000001], [8, 210.32999999999998, 232.47, 125.263, 135.656], [8, 8.61, 52.48, 111.58800000000001, 121.43400000000001], [8, 8.61, 84.46, 125.81000000000002, 136.203], [8, 67.64999999999999, 107.41999999999999, 141.673, 158.63000000000002], [8, 132.01999999999998, 173.01999999999998, 141.673, 158.63000000000002], [8, 198.85, 239.85, 141.673, 158.63000000000002], [8, 269.78, 311.59999999999997, 142.22, 158.63000000000002], [8, 24.599999999999998, 146.37, 162.459, 173.399], [8, 24.599999999999998, 386.21999999999997, 176.13400000000001, 187.074], [8, 8.61, 58.22, 189.80900000000003, 200.20200000000003], [8, 24.599999999999998, 386.21999999999997, 202.39000000000001, 213.33], [8, 8.61, 173.84, 215.51800000000003, 226.45800000000003], [8, 24.599999999999998, 300.53, 228.09900000000002, 239.03900000000002], [8, 24.599999999999998, 116.44, 240.68, 251.62000000000003], [8, 24.599999999999998, 103.32, 253.26100000000002, 264.201], [8, 24.599999999999998, 69.7, 265.84200000000004, 276.235], [8, 26.65, 63.55, 277.87600000000003, 288.269], [8, 197.61999999999998, 248.04999999999998, 277.87600000000003, 288.269], [8, 26.65, 79.94999999999999, 289.91, 300.303], [8, 177.11999999999998, 230.82999999999998, 289.91, 300.303], [8, 26.65, 76.25999999999999, 301.944, 312.33700000000005], [8, 189.82999999999998, 248.04999999999998, 301.944, 312.33700000000005], [8, 27.88, 92.25, 314.52500000000003, 324.918], [8, 27.88, 66.42, 326.559, 336.952], [8, 27.88, 382.94, 339.14000000000004, 350.08000000000004], [8, 12.299999999999999, 382.94, 351.721, 362.661], [8, 12.299999999999999, 382.94, 364.302, 375.242], [8, 12.299999999999999, 115.61999999999999, 376.336, 387.276], [8, 16.81, 113.57, 396.028, 406.42100000000005], [8, 16.81, 115.61999999999999, 410.25000000000006, 420.64300000000003], [8, 16.81, 52.07, 424.47200000000004, 434.865], [8, 38.949999999999996, 369.0, 438.14700000000005, 450.728], [8, 38.949999999999996, 273.88, 452.369, 463.85600000000005], [8, 16.81, 54.94, 464.95000000000005, 475.343], [8, 16.81, 54.94, 477.53100000000006, 487.92400000000004], [8, 18.45, 151.7, 493.94100000000003, 503.78700000000003], [8, 261.58, 276.75, 499.41100000000006, 507.61600000000004]]
2026-08-10 19:04:23,333 INFO     29 [qwen-vl-text] ═══ DONE ═══ 50 positions, pages=1, time=22.6s
2026-08-10 19:04:23,345 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 19:04:23,346 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:Clinical | outputs={"chunks": "4 items, types={'OutpatientRecord': 4}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:04:23,346 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 19:04:23,352 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:04:23,352 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:04:25,485 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:04:25,495 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 19:04:25,496 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:04:25,496 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 19:04:25,505 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:04:25,505 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:04:26,188 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:04:26,194 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 19:04:26,194 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:04:26,194 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 19:04:26,198 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:04:26,199 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:04:26,199 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 19:04:26,199 INFO     29 [qwen-vl-text] positions(25): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:04:26,199 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [25]
2026-08-10 19:04:26,447 INFO     29 [qwen-vl-text] page=4, rect=410x546, img=(1139x1517), dpi=200
2026-08-10 19:04:26,449 INFO     29 [qwen-vl-text] LLM extraction start, text_len=581
2026-08-10 19:04:26,449 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:04:26,449 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 144, \"bbox_end\": 168, \"encounter_dates\": [\"2024-01-17\", \"2024-01-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n入院日期：2024年1月17日10点52分\n性别：女\n出院日期：2024年1月20日07点00分\n年龄：60岁\n住院天数：3天\n入院情况：1. 患者老年女性因“肺腺癌5周期化疗后2年进展后化疗5周期后\n”入院治疗。2. 体格检查：双肺呼吸音清，未闻及干湿性啰音，未闻及胸膜摩擦\n音。心律齐，未闻及明显杂音，无心包摩擦音。腹部平坦，无腹壁静脉曲张。全\n腹柔软，无包块；脾肋下未触及。\n入院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo\nn-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨\n髓抑制\n诊疗经过：入院后完善各项相关检查，排除禁忌于2024.1.19给予培美曲塞\n二钠800mg+卡铂400mg，耐受可。\n出院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo\nn-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨\n髓抑制\n出院情况：一般状况可。\n出院医嘱：出院后注意休息，加强营养，避免感染；定期复查血常规，每周\n1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；2024.2.9返院继续\n治疗；不适务必及时随诊。\n医师签名：\n签字时间：2024年1月20日07点00分\n第1页",
    "role": "user"
  }
]
2026-08-10 19:04:33,255 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:04:33.253+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 88, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:04:49,930 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:04:49,931 INFO     29 [qwen-vl-text] LLM output (len=1728):
{
  "encounter_date": "2024-01-20",
  "admission_date": "2024-01-17",
  "discharge_date": "2024-01-20",
  "hospital_days": 3,
  "department": null,
  "bed_number": null,
  "admission_condition": "1. 患者老年女性因“肺腺癌5周期化疗后2年进展后化疗5周期后”入院治疗。2. 体格检查：双肺呼吸音清，未闻及干湿性啰音，未闻及胸膜摩擦音。心律齐，未闻及明显杂音，无心包摩擦音。腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。",
  "admission_diagnoses": [
    {
      "name": "右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exon-20（外显子） 20-ins突变阳性）",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肾结石",
      "diagnosis_type": "西医"
    },
    {
      "name": "子宫切除术后",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗后骨髓抑制",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后完善各项相关检查，排除禁忌于2024.1.19给予培美曲塞二钠800mg+卡铂400mg，耐受可。",
  "auxiliary_exams": null,
  "imaging_findings": null,
  "discharge_diagnoses": [
    {
      "name": "右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exon-20（外显子） 20-ins突变阳性）",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肾结石",
      "diagnosis_type": "西医"
    },
    {
      "name": "子宫切除术后",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗后骨髓抑制",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "一般状况可。",
  "outcome": null,
  "discharge_orders": "出院后注意休息，加强营养，避免感染；定期复查血常规，每周1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；2024.2.9返院继续治疗；不适务必及时随诊。",
  "do_medications": [],
  "do_follow_up": "定期复查血常规，每周1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；不适务必及时随诊。",
  "do_precautions": [
    "注意休息",
    "加强营养",
    "避免感染"
  ],
  "next_treatment_date": "2024-02-09",
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 19:04:49,931 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-01-20]
2026-08-10 19:04:49,942 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4322732, prompt_len=1269
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["出院记录", "入院日期：2024年1月17日10点52分", "性别：女", "出院日期：2024年1月20日07点00分", "年龄：60岁", "住院天数：3天", "入院情况：1. 患者老年女性因“肺腺癌5周期化疗后2年进展后化疗5周期后", "”入院治疗。2. 体格检查：双肺呼吸音清，未闻及干湿性啰音，未闻及胸膜摩擦", "音。心律齐，未闻及明显杂音，无心包摩擦音。腹部平坦，无腹壁静脉曲张。全", "腹柔软，无包块；脾肋下未触及。", "入院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo", "n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨", "髓抑制", "诊疗经过：入院后完善各项相关检查，排除禁忌于2024.1.19给予培美曲塞", "二钠800mg+卡铂400mg，耐受可。", "出院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo", "n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨", "髓抑制", "出院情况：一般状况可。", "出院医嘱：出院后注意休息，加强营养，避免感染；定期复查血常规，每周", "1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；2024.2.9返院继续", "治疗；不适务必及时随诊。", "医师签名：", "签字时间：2024年1月20日07点00分", "第1页"]

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
2026-08-10 19:05:00,353 INFO     29 [qwen-vl-text] coord API raw response (len=1675):
[
	{"text": "出院记录", "bbox": [465, 92, 575, 114]},
	{"text": "入院日期：2024年1月17日10点52分", "bbox": [545, 140, 888, 160]},
	{"text": "性别：女", "bbox": [160, 177, 245, 195]},
	{"text": "出院日期：2024年1月20日07点00分", "bbox": [545, 180, 888, 199]},
	{"text": "年龄：60岁", "bbox": [160, 217, 267, 236]},
	{"text": "住院天数：3天", "bbox": [545, 217, 690, 236]},
	{"text": "入院情况：1. 患者老年女性因“肺腺癌5周期化疗后2年进展后化疗5周期后", "bbox": [143, 257, 944, 277]},
	{"text": "”入院治疗。2. 体格检查：双肺呼吸音清，未闻及干湿性啰音，未闻及胸膜摩擦", "bbox": [96, 280, 944, 300]},
	{"text": "音。心律齐，未闻及明显杂音，无心包摩擦音。腹部平坦，无腹壁静脉曲张。全", "bbox": [96, 303, 944, 323]},
	{"text": "腹柔软，无包块；脾肋下未触及。", "bbox": [96, 326, 440, 346]},
	{"text": "入院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo", "bbox": [143, 391, 944, 411]},
	{"text": "n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨", "bbox": [96, 414, 944, 434]},
	{"text": "髓抑制", "bbox": [96, 437, 164, 456]},
	{"text": "诊疗经过：入院后完善各项相关检查，排除禁忌于2024.1.19给予培美曲塞", "bbox": [143, 501, 938, 521]},
	{"text": "二钠800mg+卡铂400mg，耐受可。", "bbox": [96, 524, 445, 544]},
	{"text": "出院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo", "bbox": [143, 587, 938, 607]},
	{"text": "n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨", "bbox": [96, 610, 938, 630]},
	{"text": "髓抑制", "bbox": [96, 633, 164, 652]},
	{"text": "出院情况：一般状况可。", "bbox": [150, 683, 385, 702]},
	{"text": "出院医嘱：出院后注意休息，加强营养，避免感染；定期复查血常规，每周", "bbox": [150, 733, 920, 752]},
	{"text": "1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；2024.2.9返院继续", "bbox": [103, 755, 920, 775]},
	{"text": "治疗；不适务必及时随诊。", "bbox": [103, 778, 370, 797]},
	{"text": "医师签名：", "bbox": [574, 897, 667, 916]},
	{"text": "签字时间：2024年1月20日07点00分", "bbox": [574, 931, 907, 950]},
	{"text": "第1页", "bbox": [483, 987, 540, 999]}
]
2026-08-10 19:05:00,353 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=10.4s
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[465, 92, 575, 114]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[1]: text=入院日期：2024年1月17日10点52分, bbox=[545, 140, 888, 160]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[160, 177, 245, 195]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[3]: text=出院日期：2024年1月20日07点00分, bbox=[545, 180, 888, 199]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：60岁, bbox=[160, 217, 267, 236]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[5]: text=住院天数：3天, bbox=[545, 217, 690, 236]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[6]: text=入院情况：1. 患者老年女性因“肺腺癌5周期化疗后2年进展后化疗5周期后, bbox=[143, 257, 944, 277]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[7]: text=”入院治疗。2. 体格检查：双肺呼吸音清，未闻及干湿性啰音，未闻及胸膜摩擦, bbox=[96, 280, 944, 300]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[8]: text=音。心律齐，未闻及明显杂音，无心包摩擦音。腹部平坦，无腹壁静脉曲张。全, bbox=[96, 303, 944, 323]
2026-08-10 19:05:00,354 INFO     29 [qwen-vl-text] coord item[9]: text=腹柔软，无包块；脾肋下未触及。, bbox=[96, 326, 440, 346]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[10]: text=入院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo, bbox=[143, 391, 944, 411]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[11]: text=n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨, bbox=[96, 414, 944, 434]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[12]: text=髓抑制, bbox=[96, 437, 164, 456]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[13]: text=诊疗经过：入院后完善各项相关检查，排除禁忌于2024.1.19给予培美曲塞, bbox=[143, 501, 938, 521]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[14]: text=二钠800mg+卡铂400mg，耐受可。, bbox=[96, 524, 445, 544]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[15]: text=出院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo, bbox=[143, 587, 938, 607]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[16]: text=n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨, bbox=[96, 610, 938, 630]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[17]: text=髓抑制, bbox=[96, 633, 164, 652]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[18]: text=出院情况：一般状况可。, bbox=[150, 683, 385, 702]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[19]: text=出院医嘱：出院后注意休息，加强营养，避免感染；定期复查血常规，每周, bbox=[150, 733, 920, 752]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[20]: text=1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；2024.2.9返院继续, bbox=[103, 755, 920, 775]
2026-08-10 19:05:00,355 INFO     29 [qwen-vl-text] coord item[21]: text=治疗；不适务必及时随诊。, bbox=[103, 778, 370, 797]
2026-08-10 19:05:00,356 INFO     29 [qwen-vl-text] coord item[22]: text=医师签名：, bbox=[574, 897, 667, 916]
2026-08-10 19:05:00,356 INFO     29 [qwen-vl-text] coord item[23]: text=签字时间：2024年1月20日07点00分, bbox=[574, 931, 907, 950]
2026-08-10 19:05:00,356 INFO     29 [qwen-vl-text] coord item[24]: text=第1页, bbox=[483, 987, 540, 999]
2026-08-10 19:05:00,358 INFO     29 [qwen-vl-text] page=4 — 25/25 coords, api_time=10.4s
2026-08-10 19:05:00,358 INFO     29 [qwen-vl-text] new_positions (25):
[[4, 190.64999999999998, 235.75, 50.232000000000006, 62.24400000000001], [4, 223.45, 364.08, 76.44000000000001, 87.36000000000001], [4, 65.6, 100.44999999999999, 96.64200000000001, 106.47000000000001], [4, 223.45, 364.08, 98.28, 108.65400000000001], [4, 65.6, 109.47, 118.48200000000001, 128.85600000000002], [4, 223.45, 282.9, 118.48200000000001, 128.85600000000002], [4, 58.629999999999995, 387.03999999999996, 140.322, 151.24200000000002], [4, 39.36, 387.03999999999996, 152.88000000000002, 163.8], [4, 39.36, 387.03999999999996, 165.43800000000002, 176.358], [4, 39.36, 180.39999999999998, 177.996, 188.91600000000003], [4, 58.629999999999995, 387.03999999999996, 213.48600000000002, 224.406], [4, 39.36, 387.03999999999996, 226.044, 236.96400000000003], [4, 39.36, 67.24, 238.602, 248.97600000000003], [4, 58.629999999999995, 384.58, 273.546, 284.466], [4, 39.36, 182.45, 286.10400000000004, 297.024], [4, 58.629999999999995, 384.58, 320.502, 331.422], [4, 39.36, 384.58, 333.06, 343.98], [4, 39.36, 67.24, 345.61800000000005, 355.992], [4, 61.49999999999999, 157.85, 372.918, 383.29200000000003], [4, 61.49999999999999, 377.2, 400.218, 410.59200000000004], [4, 42.23, 377.2, 412.23, 423.15000000000003], [4, 42.23, 151.7, 424.788, 435.16200000000003], [4, 235.33999999999997, 273.46999999999997, 489.76200000000006, 500.136], [4, 235.33999999999997, 371.87, 508.326, 518.7], [4, 198.03, 221.39999999999998, 538.902, 545.4540000000001]]
2026-08-10 19:05:00,358 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=34.2s
2026-08-10 19:05:00,371 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 19:05:00,371 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:05:00,371 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 19:05:00,378 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:05:00,379 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:05:00,379 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 19:05:00,379 INFO     29 [qwen-vl-text] positions(144): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:05:00,380 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3, 4], lines per page: [43, 37, 39, 24, 1]
2026-08-10 19:05:00,594 INFO     29 [qwen-vl-text] page=0, rect=410x526, img=(1139x1462), dpi=200
2026-08-10 19:05:00,833 INFO     29 [qwen-vl-text] page=1, rect=410x552, img=(1139x1534), dpi=200
2026-08-10 19:05:01,056 INFO     29 [qwen-vl-text] page=2, rect=410x564, img=(1139x1567), dpi=200
2026-08-10 19:05:01,246 INFO     29 [qwen-vl-text] page=3, rect=410x414, img=(1139x1150), dpi=200
2026-08-10 19:05:01,491 INFO     29 [qwen-vl-text] page=4, rect=410x546, img=(1139x1517), dpi=200
2026-08-10 19:05:01,494 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3133
2026-08-10 19:05:01,494 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:05:01,495 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 143, \"encounter_dates\": [\"2024-01-17\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "姓名\n现住址\n性别：女\n职业：农民\n年龄：60岁\n入院时间：2024年01月17日10点52分\n民族：汉族\n记录时间：2024年01月17日16点00分\n婚姻：已婚\n病史陈述者\n陈述者与患者关系：本人\n陈述者内容可靠标志：可靠\n主诉：肺腺癌5周期化疗后2年进展后化疗5周期后。\n现病史：患者2020.8月体检时行胸部CT检查提示右肺上叶片状影，无咳嗽、咳痰、\n咯血、痰中带血及胸痛、发热、盗汗等不适，遂就诊于当地医院给予“左氧氟沙星、\n法罗培南”等药物抗感染治疗，复查胸部CT提示吸收欠佳。患者为求进一步诊治就诊\n于我院，行胸部CT检查考虑右肺上叶浸润性肺腺Ca，在排除相关禁忌并取得患者家属\n知情同意后，行经皮肺穿刺活检，病理结果示：（右肺上叶）穿刺肺组织呈显著慢性\n炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变\n炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1(+)，CK7(+)，Ki-67阳性\n率10%。为排查肿瘤全身转移情况行骨ECT及腹部强化CT检查未见明显转移征象，行颅\n脑MRI提示右颞枕叶、左侧小脑下蚓部异常信号，结合肿瘤病史，建议增强扫描除外\n转移，为排除颅脑转移，进一步行颅脑强化MRI提示右侧颞枕叶脑沟内条片状轻度强\n化，考虑软脑膜增厚强化，结合肺Ca病史，脑膜转移不除外，建议脑脊液检查。脑脊\n液检查未见肿瘤细胞。在取得外科会诊意见明确患者具有手术指征后，患者于2020-0\n8-31于胸外科行右肺上叶切除并肺部、纵膈淋巴结清扫术，术后病理示：（右肺上叶\n）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，\n肿物切面面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；\n肺组织内查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚\n查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔\n淋巴结4枚，其中2枚查见转移癌（2/4）。另送第7组淋巴结9枚（0/9）、第9组淋巴结\n1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。术后行EGFR等十基因检测\n（石蜡包埋组织）示EFGR基因 Exon-20（外显子） 20-ins突变阳性。后患者为行\n进一步治疗就诊我科，告知患者其Exon-20突变不适合靶向药物治疗，建议行化疗治\n疗，在排除相关禁忌并取得患者及家属知情同意后，于2020-10-16、2020-11-10、\n2020-12-04、2020-12-26、2021-1-18行“培美曲塞二钠0.8g d1+卡铂400mg d1\n”方案化疗5周期，患者耐受可。2023.9.21、2023.10.13、2023.11.8、2023.12\n.4、2023.12.26排除禁忌给予卡铂+培美曲塞二钠联合贝伐珠单抗治疗5周期，耐受\n可。2023.11.07复查CT示：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19\nCT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂\n肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水\n；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著\n第1页\n入院记录\n姓名\n住院号\n。患者治疗后出现发热，体温38.7°C，化验示白细胞2.05*109/L，中性粒细胞0.7\n5*109/L，给予升白对症处理。患者自上次出院后，饮食、睡眠可，大小便未见明显\n异常，体重无明显改变。\n既往史：既往身体健康，否认高血压，否认糖尿病，否认冠心病，否认结核等传染病\n史及密切接触史，否认外伤史，否认手术史，否认输血史，预防接种史：随当地，过\n敏史：食物过敏史：无，药物过敏史：无。\n个人史：生于原籍，无外地久居史，无疫区到访及停留史，无工业毒物、粉尘、放射\n性物质接触史，吸烟史：无，饮酒史：无。\n月经史：已绝经。\n婚育史：已婚，已育。\n家族史：否认家族遗传病史。\n体格检查\nT:36℃ P:97次/分 R:23次/分 血压：154/94mmHg 体重：72kg 身高：16\n0cm NRS：0\n一般情况：老年女性，神志清晰，精神好，发育正常，营养良好，自主体位，查体合作\n。\n皮肤、粘膜：颜色红润，无皮肤黄疸，无明显皮肤红肿硬肿，无凹陷性水肿，无皮疹\n，未见出血点，未见瘀斑。皮肤弹性好。无肿大淋巴结。\n头部及其器官：头颅无畸形；双眼无畸形，双侧瞳孔等大，对光反射存在；双耳无畸\n形；鼻无畸形。口唇红润，无唇裂，咽无充血。\n颈部：无抵抗感，气管居中，胸锁乳突肌包块：无。甲状腺正常，无颈部淋巴结肿大\n。\n胸部：双侧对称，无畸形；双肩等高，呼吸动度双侧一致，三凹征阴性。肺呼吸音：\n清，未闻及干湿性啰音，未闻及胸膜摩擦音。\n心脏：心前区无隆起，心尖搏动位于左侧锁骨中线第5肋间，心音有力，心律齐，未\n闻及明显杂音，无心包摩擦音。\n腹部：腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。腹部叩诊呈\n鼓音；肠鸣音正常，4次/分。\n肛门外生殖器：肛门位置正常。外阴外观无畸形。\n脊柱：脊柱生理曲度正常。\n四肢：四肢肌力正常，肌张力正常。\n神经系统：双侧腱反射正常，脑膜刺激征阴性，双侧病理征阴性。\n专科情况\n无。\n入院记录\n辅助检查\n日期\n项目\n结果\n2020-07-29\n胸部CT\n考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检，双肺间质性改变，右肾结石\n2020-08-10\n肺功能\n肺通气功能正常\n2020-08-10\n胸部强化CT\n考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检；右肺门淋巴结肿大；双肺纤维灶；肝囊肿；右肾结石\n2020-08-10\n肺组织活检\n（右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1 (+), CK7(+), Ki-67阳性率10%\n2020-08-14\n骨扫描\n1.右肺坐骨支局限性骨质代谢增高观察；2.L5山医\n2020-08-16\n颅脑MR强化\n强化后FLAIR显示右侧颞枕叶脑沟内条片状轻度山医\n2020-08-31\n肺组织术后病理\n（右肺上叶）浸润性腺癌，腺泡型（60%），乳山医\n2020-09-23\n基因检测\nEGFR等十基因检测（石蜡包埋组织）：EFGR基山医\n2022-06-01\n胸部CT平扫\n右肺术后CT表现，请结合临床；双肺纤维灶左山医\n2023-03-29\n胸部CT平扫\n右肺术后CT表现，较2022-06-01 前片变化不大；双肺多发小结节，对比2022-06-01 前片\n2023-09-13\nCT平扫\n双侧基底节区少许缺血变性灶，必要时结合MRI\n第 3 页\n入院记录\n住\n2023-11-07\n强化CT\n右肺术后，右肺纤维灶，右侧胸膜增厚，较\n2023-09-19 CT变化不著；双肺多发小结节，\n较前变化不著，请结合临床、随诊复查；提示\n轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊\n肿、左肾盂旁囊肿；右肾小结石、右肾轻度积\n水；右侧附件区囊性低密度，请结合临床及妇\n科超声；左侧耻骨高密度，较前变化不著\n初步诊断：\n1. 右肺上叶浸润性腺癌术后（T1bN2M0, I\nIIA期 EGFR突变：Exon-20（外显子） 20-i\nns突变阳性）\n2. 右肾结石\n3. 子宫切除术后\n4. 化疗后骨髓抑制\n记录者：\n项目内容\n患方签名\n以上所记录内容属实\n签字时间\n年 月 日 时 分\nX光号：",
    "role": "user"
  }
]
2026-08-10 19:05:05,552 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:05:05.549+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 88, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:05:37,755 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:05:37.753+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 88, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:06:03,755 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:06:03,755 INFO     29 [qwen-vl-text] LLM output (len=4114):
{
  "encounter_date": "2024-01-17",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 60,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "农民",
  "dm_admission_time": "2024-01-17 10:52",
  "dm_record_time": "2024-01-17 16:00",
  "dm_history_provider": "本人",
  "cc_text": "肺腺癌5周期化疗后2年进展后化疗5周期后。",
  "cc_main_symptoms": [
    "肺腺癌化疗后进展"
  ],
  "cc_duration": "2年",
  "pi_text": "患者2020.8月体检时行胸部CT检查提示右肺上叶片状影，无咳嗽、咳痰、咯血、痰中带血及胸痛、发热、盗汗等不适，遂就诊于当地医院给予“左氧氟沙星、法罗培南”等药物抗感染治疗，复查胸部CT提示吸收欠佳。患者为求进一步诊治就诊于我院，行胸部CT检查考虑右肺上叶浸润性肺腺Ca，在排除相关禁忌并取得患者家属知情同意后，行经皮肺穿刺活检，病理结果示：（右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1(+)，CK7(+)，Ki-67阳性率10%。为排查肿瘤全身转移情况行骨ECT及腹部强化CT检查未见明显转移征象，行颅脑MRI提示右颞枕叶、左侧小脑下蚓部异常信号，结合肿瘤病史，建议增强扫描除外转移，为排除颅脑转移，进一步行颅脑强化MRI提示右侧颞枕叶脑沟内条片状轻度强化，考虑软脑膜增厚强化，结合肺Ca病史，脑膜转移不除外，建议脑脊液检查。脑脊液检查未见肿瘤细胞。在取得外科会诊意见明确患者具有手术指征后，患者于2020-08-31于胸外科行右肺上叶切除并肺部、纵膈淋巴结清扫术，术后病理示：（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，肿物切面面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌（2/4）。另送第7组淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。术后行EGFR等十基因检测（石蜡包埋组织）示EFGR基因 Exon-20（外显子） 20-ins突变阳性。后患者为行进一步治疗就诊我科，告知患者其Exon-20突变不适合靶向药物治疗，建议行化疗治疗，在排除相关禁忌并取得患者及家属知情同意后，于2020-10-16、2020-11-10、2020-12-04、2020-12-26、2021-1-18行“培美曲塞二钠0.8g d1+卡铂400mg d1”方案化疗5周期，患者耐受可。2023.9.21、2023.10.13、2023.11.8、2023.12.4、2023.12.26排除禁忌给予卡铂+培美曲塞二钠联合贝伐珠单抗治疗5周期，耐受可。2023.11.07复查CT示：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19 CT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著。患者治疗后出现发热，体温38.7°C，化验示白细胞2.05*109/L，中性粒细胞0.75*109/L，给予升白对症处理。患者自上次出院后，饮食、睡眠可，大小便未见明显异常，体重无明显改变。",
  "pmh_disease_history": [
    "否认高血压",
    "否认糖尿病",
    "否认冠心病",
    "否认结核等传染病史及密切接触史"
  ],
  "pmh_allergy_history": [
    "无"
  ],
  "pmh_surgery_trauma_history": [
    "否认外伤史",
    "否认手术史",
    "否认输血史"
  ],
  "ph_smoking": "无",
  "ph_drinking": "无",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": "已婚，已育",
  "fh_text": "否认家族遗传病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36,
  "vs_pulse_bpm": 97,
  "vs_respiration_rpm": 23,
  "vs_systolic_bp_mmhg": 154,
  "vs_diastolic_bp_mmhg": 94,
  "pe_general_condition": "老年女性，神志清晰，精神好，发育正常，营养良好，自主体位，查体合作。",
  "pe_skin_mucosa": "颜色红润，无皮肤黄疸，无明显皮肤红肿硬肿，无凹陷性水肿，无皮疹，未见出血点，未见瘀斑。皮肤弹性好。",
  "pe_lymph_nodes": "无肿大淋巴结。",
  "pe_lungs": "双侧对称，无畸形；双肩等高，呼吸动度双侧一致，三凹征阴性。肺呼吸音：清，未闻及干湿性啰音，未闻及胸膜摩擦音。",
  "pe_heart": "心前区无隆起，心尖搏动位于左侧锁骨中线第5肋间，心音有力，心律齐，未闻及明显杂音，无心包摩擦音。",
  "pe_abdomen": "腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。腹部叩诊呈鼓音；肠鸣音正常，4次/分。",
  "pe_extremities": "四肢肌力正常，肌张力正常。",
  "pe_nervous_system": "双侧腱反射正常，脑膜刺激征阴性，双侧病理征阴性。",
  "pe_specialist_exam": "无。",
  "pe_ecog_score": null,
  "pat_text": null,
  "pat_items": [
    "2020-07-29 胸部CT: 考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检，双肺间质性改变，右肾结石",
    "2020-08-10 肺功能: 肺通气功能正常",
    "2020-08-10 胸部强化CT: 考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检；右肺门淋巴结肿大；双肺纤维灶；肝囊肿；右肾结石",
    "2020-08-10 肺组织活检: （右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1 (+), CK7(+), Ki-67阳性率10%",
    "2020-08-14 骨扫描: 1.右肺坐骨支局限性骨质代谢增高观察；2.L5山医",
    "2020-08-16 颅脑MR强化: 强化后FLAIR显示右侧颞枕叶脑沟内条片状轻度山医",
    "2020-08-31 肺组织术后病理: （右肺上叶）浸润性腺癌，腺泡型（60%），乳山医",
    "2020-09-23 基因检测: EGFR等十基因检测（石蜡包埋组织）：EFGR基山医",
    "2022-06-01 胸部CT平扫: 右肺术后CT表现，请结合临床；双肺纤维灶左山医",
    "2023-03-29 胸部CT平扫: 右肺术后CT表现，较2022-06-01 前片变化不大；双肺多发小结节，对比2022-06-01 前片",
    "2023-09-13 CT平扫: 双侧基底节区少许缺血变性灶，必要时结合MRI",
    "2023-11-07 强化CT: 右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19 CT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著"
  ],
  "preliminary_diagnoses": [
    {
      "name": "右肺上叶浸润性腺癌术后（T1bN2M0, IIA期 EGFR突变：Exon-20（外显子） 20-ins突变阳性）",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "右肾结石",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "子宫切除术后",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "化疗后骨髓抑制",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 19:06:03,755 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-01-17]
2026-08-10 19:06:03,764 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4128829, prompt_len=2113
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["姓名", "现住址", "性别：女", "职业：农民", "年龄：60岁", "入院时间：2024年01月17日10点52分", "民族：汉族", "记录时间：2024年01月17日16点00分", "婚姻：已婚", "病史陈述者", "陈述者与患者关系：本人", "陈述者内容可靠标志：可靠", "主诉：肺腺癌5周期化疗后2年进展后化疗5周期后。", "现病史：患者2020.8月体检时行胸部CT检查提示右肺上叶片状影，无咳嗽、咳痰、", "咯血、痰中带血及胸痛、发热、盗汗等不适，遂就诊于当地医院给予“左氧氟沙星、", "法罗培南”等药物抗感染治疗，复查胸部CT提示吸收欠佳。患者为求进一步诊治就诊", "于我院，行胸部CT检查考虑右肺上叶浸润性肺腺Ca，在排除相关禁忌并取得患者家属", "知情同意后，行经皮肺穿刺活检，病理结果示：（右肺上叶）穿刺肺组织呈显著慢性", "炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变", "炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1(+)，CK7(+)，Ki-67阳性", "率10%。为排查肿瘤全身转移情况行骨ECT及腹部强化CT检查未见明显转移征象，行颅", "脑MRI提示右颞枕叶、左侧小脑下蚓部异常信号，结合肿瘤病史，建议增强扫描除外", "转移，为排除颅脑转移，进一步行颅脑强化MRI提示右侧颞枕叶脑沟内条片状轻度强", "化，考虑软脑膜增厚强化，结合肺Ca病史，脑膜转移不除外，建议脑脊液检查。脑脊", "液检查未见肿瘤细胞。在取得外科会诊意见明确患者具有手术指征后，患者于2020-0", "8-31于胸外科行右肺上叶切除并肺部、纵膈淋巴结清扫术，术后病理示：（右肺上叶", "）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，", "肿物切面面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；", "肺组织内查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚", "查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔", "淋巴结4枚，其中2枚查见转移癌（2/4）。另送第7组淋巴结9枚（0/9）、第9组淋巴结", "1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。术后行EGFR等十基因检测", "（石蜡包埋组织）示EFGR基因 Exon-20（外显子） 20-ins突变阳性。后患者为行", "进一步治疗就诊我科，告知患者其Exon-20突变不适合靶向药物治疗，建议行化疗治", "疗，在排除相关禁忌并取得患者及家属知情同意后，于2020-10-16、2020-11-10、", "2020-12-04、2020-12-26、2021-1-18行“培美曲塞二钠0.8g d1+卡铂400mg d1", "”方案化疗5周期，患者耐受可。2023.9.21、2023.10.13、2023.11.8、2023.12", ".4、2023.12.26排除禁忌给予卡铂+培美曲塞二钠联合贝伐珠单抗治疗5周期，耐受", "可。2023.11.07复查CT示：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19", "CT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂", "肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水", "；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著", "第1页"]

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
2026-08-10 19:06:20,265 INFO     29 [qwen-vl-text] coord API raw response (len=3221):
[
	{"text": "姓名", "bbox": [74, 16, 119, 36]},
	{"text": "现住址", "bbox": [506, 16, 575, 36]},
	{"text": "性别：女", "bbox": [74, 50, 158, 70]},
	{"text": "职业：农民", "bbox": [506, 50, 620, 70]},
	{"text": "年龄：60岁", "bbox": [74, 83, 183, 103]},
	{"text": "入院时间：2024年01月17日10点52分", "bbox": [506, 83, 867, 103]},
	{"text": "民族：汉族", "bbox": [74, 116, 183, 136]},
	{"text": "记录时间：2024年01月17日16点00分", "bbox": [506, 116, 867, 136]},
	{"text": "婚姻：已婚", "bbox": [74, 149, 183, 169]},
	{"text": "病史陈述者", "bbox": [506, 149, 620, 169]},
	{"text": "陈述者与患者关系：本人", "bbox": [74, 182, 323, 202]},
	{"text": "陈述者内容可靠标志：可靠", "bbox": [506, 182, 777, 202]},
	{"text": "主诉：肺腺癌5周期化疗后2年进展后化疗5周期后。", "bbox": [31, 215, 583, 235]},
	{"text": "现病史：患者2020.8月体检时行胸部CT检查提示右肺上叶片状影，无咳嗽、咳痰、", "bbox": [26, 244, 952, 264]},
	{"text": "咯血、痰中带血及胸痛、发热、盗汗等不适，遂就诊于当地医院给予“左氧氟沙星、", "bbox": [26, 270, 952, 290]},
	{"text": "法罗培南”等药物抗感染治疗，复查胸部CT提示吸收欠佳。患者为求进一步诊治就诊", "bbox": [26, 296, 964, 316]},
	{"text": "于我院，行胸部CT检查考虑右肺上叶浸润性肺腺Ca，在排除相关禁忌并取得患者家属", "bbox": [26, 322, 964, 342]},
	{"text": "知情同意后，行经皮肺穿刺活检，病理结果示：（右肺上叶）穿刺肺组织呈显著慢性", "bbox": [26, 348, 964, 368]},
	{"text": "炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变", "bbox": [26, 374, 964, 394]},
	{"text": "炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1(+)，CK7(+)，Ki-67阳性", "bbox": [26, 399, 964, 419]},
	{"text": "率10%。为排查肿瘤全身转移情况行骨ECT及腹部强化CT检查未见明显转移征象，行颅", "bbox": [26, 425, 964, 445]},
	{"text": "脑MRI提示右颞枕叶、左侧小脑下蚓部异常信号，结合肿瘤病史，建议增强扫描除外", "bbox": [26, 451, 964, 471]},
	{"text": "转移，为排除颅脑转移，进一步行颅脑强化MRI提示右侧颞枕叶脑沟内条片状轻度强", "bbox": [26, 477, 964, 497]},
	{"text": "化，考虑软脑膜增厚强化，结合肺Ca病史，脑膜转移不除外，建议脑脊液检查。脑脊", "bbox": [26, 503, 964, 523]},
	{"text": "液检查未见肿瘤细胞。在取得外科会诊意见明确患者具有手术指征后，患者于2020-0", "bbox": [26, 529, 964, 549]},
	{"text": "8-31于胸外科行右肺上叶切除并肺部、纵膈淋巴结清扫术，术后病理示：（右肺上叶", "bbox": [26, 555, 964, 575]},
	{"text": "）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，", "bbox": [26, 580, 948, 600]},
	{"text": "肿物切面面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；", "bbox": [26, 606, 948, 626]},
	{"text": "肺组织内查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚", "bbox": [26, 632, 964, 652]},
	{"text": "查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔", "bbox": [26, 658, 964, 678]},
	{"text": "淋巴结4枚，其中2枚查见转移癌（2/4）。另送第7组淋巴结9枚（0/9）、第9组淋巴结", "bbox": [26, 684, 955, 704]},
	{"text": "1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。术后行EGFR等十基因检测", "bbox": [26, 710, 955, 730]},
	{"text": "（石蜡包埋组织）示EFGR基因 Exon-20（外显子） 20-ins突变阳性。后患者为行", "bbox": [26, 736, 955, 756]},
	{"text": "进一步治疗就诊我科，告知患者其Exon-20突变不适合靶向药物治疗，建议行化疗治", "bbox": [26, 762, 955, 782]},
	{"text": "疗，在排除相关禁忌并取得患者及家属知情同意后，于2020-10-16、2020-11-10、", "bbox": [26, 788, 948, 808]},
	{"text": "2020-12-04、2020-12-26、2021-1-18行“培美曲塞二钠0.8g d1+卡铂400mg d1", "bbox": [26, 814, 955, 834]},
	{"text": "”方案化疗5周期，患者耐受可。2023.9.21、2023.10.13、2023.11.8、2023.12", "bbox": [26, 840, 955, 860]},
	{"text": ".4、2023.12.26排除禁忌给予卡铂+培美曲塞二钠联合贝伐珠单抗治疗5周期，耐受", "bbox": [26, 866, 955, 886]},
	{"text": "可。2023.11.07复查CT示：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19", "bbox": [26, 892, 955, 912]},
	{"text": "CT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂", "bbox": [26, 918, 955, 938]},
	{"text": "肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水", "bbox": [26, 944, 955, 964]},
	{"text": "；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著", "bbox": [26, 970, 955, 990]},
	{"text": "第1页", "bbox": [482, 987, 545, 1000]}
]
2026-08-10 19:06:20,266 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=16.5s
2026-08-10 19:06:20,266 INFO     29 [qwen-vl-text] coord item[0]: text=姓名, bbox=[74, 16, 119, 36]
2026-08-10 19:06:20,266 INFO     29 [qwen-vl-text] coord item[1]: text=现住址, bbox=[506, 16, 575, 36]
2026-08-10 19:06:20,266 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[74, 50, 158, 70]
2026-08-10 19:06:20,266 INFO     29 [qwen-vl-text] coord item[3]: text=职业：农民, bbox=[506, 50, 620, 70]
2026-08-10 19:06:20,266 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：60岁, bbox=[74, 83, 183, 103]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[5]: text=入院时间：2024年01月17日10点52分, bbox=[506, 83, 867, 103]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[6]: text=民族：汉族, bbox=[74, 116, 183, 136]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[7]: text=记录时间：2024年01月17日16点00分, bbox=[506, 116, 867, 136]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[8]: text=婚姻：已婚, bbox=[74, 149, 183, 169]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[9]: text=病史陈述者, bbox=[506, 149, 620, 169]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[10]: text=陈述者与患者关系：本人, bbox=[74, 182, 323, 202]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[11]: text=陈述者内容可靠标志：可靠, bbox=[506, 182, 777, 202]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[12]: text=主诉：肺腺癌5周期化疗后2年进展后化疗5周期后。, bbox=[31, 215, 583, 235]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[13]: text=现病史：患者2020.8月体检时行胸部CT检查提示右肺上叶片状影，无咳嗽、咳痰、, bbox=[26, 244, 952, 264]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[14]: text=咯血、痰中带血及胸痛、发热、盗汗等不适，遂就诊于当地医院给予“左氧氟沙星、, bbox=[26, 270, 952, 290]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[15]: text=法罗培南”等药物抗感染治疗，复查胸部CT提示吸收欠佳。患者为求进一步诊治就诊, bbox=[26, 296, 964, 316]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[16]: text=于我院，行胸部CT检查考虑右肺上叶浸润性肺腺Ca，在排除相关禁忌并取得患者家属, bbox=[26, 322, 964, 342]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[17]: text=知情同意后，行经皮肺穿刺活检，病理结果示：（右肺上叶）穿刺肺组织呈显著慢性, bbox=[26, 348, 964, 368]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[18]: text=炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变, bbox=[26, 374, 964, 394]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[19]: text=炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1(+)，CK7(+)，Ki-67阳性, bbox=[26, 399, 964, 419]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[20]: text=率10%。为排查肿瘤全身转移情况行骨ECT及腹部强化CT检查未见明显转移征象，行颅, bbox=[26, 425, 964, 445]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[21]: text=脑MRI提示右颞枕叶、左侧小脑下蚓部异常信号，结合肿瘤病史，建议增强扫描除外, bbox=[26, 451, 964, 471]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[22]: text=转移，为排除颅脑转移，进一步行颅脑强化MRI提示右侧颞枕叶脑沟内条片状轻度强, bbox=[26, 477, 964, 497]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[23]: text=化，考虑软脑膜增厚强化，结合肺Ca病史，脑膜转移不除外，建议脑脊液检查。脑脊, bbox=[26, 503, 964, 523]
2026-08-10 19:06:20,267 INFO     29 [qwen-vl-text] coord item[24]: text=液检查未见肿瘤细胞。在取得外科会诊意见明确患者具有手术指征后，患者于2020-0, bbox=[26, 529, 964, 549]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[25]: text=8-31于胸外科行右肺上叶切除并肺部、纵膈淋巴结清扫术，术后病理示：（右肺上叶, bbox=[26, 555, 964, 575]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[26]: text=）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，, bbox=[26, 580, 948, 600]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[27]: text=肿物切面面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；, bbox=[26, 606, 948, 626]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[28]: text=肺组织内查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚, bbox=[26, 632, 964, 652]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[29]: text=查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔, bbox=[26, 658, 964, 678]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[30]: text=淋巴结4枚，其中2枚查见转移癌（2/4）。另送第7组淋巴结9枚（0/9）、第9组淋巴结, bbox=[26, 684, 955, 704]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[31]: text=1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。术后行EGFR等十基因检测, bbox=[26, 710, 955, 730]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[32]: text=（石蜡包埋组织）示EFGR基因 Exon-20（外显子） 20-ins突变阳性。后患者为行, bbox=[26, 736, 955, 756]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[33]: text=进一步治疗就诊我科，告知患者其Exon-20突变不适合靶向药物治疗，建议行化疗治, bbox=[26, 762, 955, 782]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[34]: text=疗，在排除相关禁忌并取得患者及家属知情同意后，于2020-10-16、2020-11-10、, bbox=[26, 788, 948, 808]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[35]: text=2020-12-04、2020-12-26、2021-1-18行“培美曲塞二钠0.8g d1+卡铂400mg d1, bbox=[26, 814, 955, 834]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[36]: text=”方案化疗5周期，患者耐受可。2023.9.21、2023.10.13、2023.11.8、2023.12, bbox=[26, 840, 955, 860]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[37]: text=.4、2023.12.26排除禁忌给予卡铂+培美曲塞二钠联合贝伐珠单抗治疗5周期，耐受, bbox=[26, 866, 955, 886]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[38]: text=可。2023.11.07复查CT示：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19, bbox=[26, 892, 955, 912]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[39]: text=CT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂, bbox=[26, 918, 955, 938]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[40]: text=肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水, bbox=[26, 944, 955, 964]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[41]: text=；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著, bbox=[26, 970, 955, 990]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] coord item[42]: text=第1页, bbox=[482, 987, 545, 1000]
2026-08-10 19:06:20,268 INFO     29 [qwen-vl-text] page=0 — 43/43 coords, api_time=16.5s
2026-08-10 19:06:20,282 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4449772, prompt_len=1548
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["入院记录", "姓名", "住院号", "。患者治疗后出现发热，体温38.7°C，化验示白细胞2.05*109/L，中性粒细胞0.7", "5*109/L，给予升白对症处理。患者自上次出院后，饮食、睡眠可，大小便未见明显", "异常，体重无明显改变。", "既往史：既往身体健康，否认高血压，否认糖尿病，否认冠心病，否认结核等传染病", "史及密切接触史，否认外伤史，否认手术史，否认输血史，预防接种史：随当地，过", "敏史：食物过敏史：无，药物过敏史：无。", "个人史：生于原籍，无外地久居史，无疫区到访及停留史，无工业毒物、粉尘、放射", "性物质接触史，吸烟史：无，饮酒史：无。", "月经史：已绝经。", "婚育史：已婚，已育。", "家族史：否认家族遗传病史。", "体格检查", "T:36℃ P:97次/分 R:23次/分 血压：154/94mmHg 体重：72kg 身高：16", "0cm NRS：0", "一般情况：老年女性，神志清晰，精神好，发育正常，营养良好，自主体位，查体合作", "。", "皮肤、粘膜：颜色红润，无皮肤黄疸，无明显皮肤红肿硬肿，无凹陷性水肿，无皮疹", "，未见出血点，未见瘀斑。皮肤弹性好。无肿大淋巴结。", "头部及其器官：头颅无畸形；双眼无畸形，双侧瞳孔等大，对光反射存在；双耳无畸", "形；鼻无畸形。口唇红润，无唇裂，咽无充血。", "颈部：无抵抗感，气管居中，胸锁乳突肌包块：无。甲状腺正常，无颈部淋巴结肿大", "。", "胸部：双侧对称，无畸形；双肩等高，呼吸动度双侧一致，三凹征阴性。肺呼吸音：", "清，未闻及干湿性啰音，未闻及胸膜摩擦音。", "心脏：心前区无隆起，心尖搏动位于左侧锁骨中线第5肋间，心音有力，心律齐，未", "闻及明显杂音，无心包摩擦音。", "腹部：腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。腹部叩诊呈", "鼓音；肠鸣音正常，4次/分。", "肛门外生殖器：肛门位置正常。外阴外观无畸形。", "脊柱：脊柱生理曲度正常。", "四肢：四肢肌力正常，肌张力正常。", "神经系统：双侧腱反射正常，脑膜刺激征阴性，双侧病理征阴性。", "专科情况", "无。"]

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
2026-08-10 19:06:35,222 INFO     29 [qwen-vl-text] coord API raw response (len=2419):
[
	{"text": "入院记录", "bbox": [430, 93, 535, 113]},
	{"text": "姓名", "bbox": [63, 128, 100, 145]},
	{"text": "住院号", "bbox": [698, 127, 752, 144]},
	{"text": "。患者治疗后出现发热，体温38.7°C，化验示白细胞2.05*109/L，中性粒细胞0.7", "bbox": [65, 156, 906, 173]},
	{"text": "5*109/L，给予升白对症处理。患者自上次出院后，饮食、睡眠可，大小便未见明显", "bbox": [65, 178, 906, 195]},
	{"text": "异常，体重无明显改变。", "bbox": [65, 200, 300, 217]},
	{"text": "既往史：既往身体健康，否认高血压，否认糖尿病，否认冠心病，否认结核等传染病", "bbox": [65, 226, 906, 243]},
	{"text": "史及密切接触史，否认外伤史，否认手术史，否认输血史，预防接种史：随当地，过", "bbox": [65, 248, 906, 265]},
	{"text": "敏史：食物过敏史：无，药物过敏史：无。", "bbox": [65, 271, 482, 288]},
	{"text": "个人史：生于原籍，无外地久居史，无疫区到访及停留史，无工业毒物、粉尘、放射", "bbox": [65, 297, 906, 314]},
	{"text": "性物质接触史，吸烟史：无，饮酒史：无。", "bbox": [65, 320, 482, 337]},
	{"text": "月经史：已绝经。", "bbox": [65, 351, 240, 368]},
	{"text": "婚育史：已婚，已育。", "bbox": [65, 377, 284, 394]},
	{"text": "家族史：否认家族遗传病史。", "bbox": [65, 402, 351, 419]},
	{"text": "体格检查", "bbox": [444, 426, 532, 443]},
	{"text": "T:36℃ P:97次/分 R:23次/分 血压：154/94mmHg 体重：72kg 身高：16", "bbox": [65, 449, 903, 466]},
	{"text": "0cm NRS：0", "bbox": [65, 472, 205, 489]},
	{"text": "一般情况：老年女性，神志清晰，精神好，发育正常，营养良好，自主体位，查体合作", "bbox": [65, 498, 900, 515]},
	{"text": "。", "bbox": [65, 521, 82, 538]},
	{"text": "皮肤、粘膜：颜色红润，无皮肤黄疸，无明显皮肤红肿硬肿，无凹陷性水肿，无皮疹", "bbox": [65, 545, 906, 563]},
	{"text": "，未见出血点，未见瘀斑。皮肤弹性好。无肿大淋巴结。", "bbox": [65, 568, 617, 585]},
	{"text": "头部及其器官：头颅无畸形；双眼无畸形，双侧瞳孔等大，对光反射存在；双耳无畸", "bbox": [65, 593, 906, 611]},
	{"text": "形；鼻无畸形。口唇红润，无唇裂，咽无充血。", "bbox": [65, 616, 532, 633]},
	{"text": "颈部：无抵抗感，气管居中，胸锁乳突肌包块：无。甲状腺正常，无颈部淋巴结肿大", "bbox": [65, 642, 906, 659]},
	{"text": "。", "bbox": [65, 665, 82, 682]},
	{"text": "胸部：双侧对称，无畸形；双肩等高，呼吸动度双侧一致，三凹征阴性。肺呼吸音：", "bbox": [65, 689, 895, 706]},
	{"text": "清，未闻及干湿性啰音，未闻及胸膜摩擦音。", "bbox": [65, 712, 509, 729]},
	{"text": "心脏：心前区无隆起，心尖搏动位于左侧锁骨中线第5肋间，心音有力，心律齐，未", "bbox": [65, 737, 906, 755]},
	{"text": "闻及明显杂音，无心包摩擦音。", "bbox": [65, 760, 377, 777]},
	{"text": "腹部：腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。腹部叩诊呈", "bbox": [65, 786, 906, 803]},
	{"text": "鼓音；肠鸣音正常，4次/分。", "bbox": [65, 809, 360, 826]},
	{"text": "肛门外生殖器：肛门位置正常。外阴外观无畸形。", "bbox": [65, 835, 552, 852]},
	{"text": "脊柱：脊柱生理曲度正常。", "bbox": [65, 858, 341, 876]},
	{"text": "四肢：四肢肌力正常，肌张力正常。", "bbox": [65, 883, 427, 901]},
	{"text": "神经系统：双侧腱反射正常，脑膜刺激征阴性，双侧病理征阴性。", "bbox": [65, 907, 715, 925]},
	{"text": "专科情况", "bbox": [450, 932, 537, 949]},
	{"text": "无。", "bbox": [82, 953, 115, 969]}
]
2026-08-10 19:06:35,222 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=14.9s
2026-08-10 19:06:35,222 INFO     29 [qwen-vl-text] coord item[0]: text=入院记录, bbox=[430, 93, 535, 113]
2026-08-10 19:06:35,222 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[63, 128, 100, 145]
2026-08-10 19:06:35,222 INFO     29 [qwen-vl-text] coord item[2]: text=住院号, bbox=[698, 127, 752, 144]
2026-08-10 19:06:35,222 INFO     29 [qwen-vl-text] coord item[3]: text=。患者治疗后出现发热，体温38.7°C，化验示白细胞2.05*109/L，中性粒细胞0.7, bbox=[65, 156, 906, 173]
2026-08-10 19:06:35,222 INFO     29 [qwen-vl-text] coord item[4]: text=5*109/L，给予升白对症处理。患者自上次出院后，饮食、睡眠可，大小便未见明显, bbox=[65, 178, 906, 195]
2026-08-10 19:06:35,222 INFO     29 [qwen-vl-text] coord item[5]: text=异常，体重无明显改变。, bbox=[65, 200, 300, 217]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[6]: text=既往史：既往身体健康，否认高血压，否认糖尿病，否认冠心病，否认结核等传染病, bbox=[65, 226, 906, 243]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[7]: text=史及密切接触史，否认外伤史，否认手术史，否认输血史，预防接种史：随当地，过, bbox=[65, 248, 906, 265]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[8]: text=敏史：食物过敏史：无，药物过敏史：无。, bbox=[65, 271, 482, 288]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[9]: text=个人史：生于原籍，无外地久居史，无疫区到访及停留史，无工业毒物、粉尘、放射, bbox=[65, 297, 906, 314]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[10]: text=性物质接触史，吸烟史：无，饮酒史：无。, bbox=[65, 320, 482, 337]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[11]: text=月经史：已绝经。, bbox=[65, 351, 240, 368]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[12]: text=婚育史：已婚，已育。, bbox=[65, 377, 284, 394]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[13]: text=家族史：否认家族遗传病史。, bbox=[65, 402, 351, 419]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[14]: text=体格检查, bbox=[444, 426, 532, 443]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[15]: text=T:36℃ P:97次/分 R:23次/分 血压：154/94mmHg 体重：72kg 身高：16, bbox=[65, 449, 903, 466]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[16]: text=0cm NRS：0, bbox=[65, 472, 205, 489]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[17]: text=一般情况：老年女性，神志清晰，精神好，发育正常，营养良好，自主体位，查体合作, bbox=[65, 498, 900, 515]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[18]: text=。, bbox=[65, 521, 82, 538]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[19]: text=皮肤、粘膜：颜色红润，无皮肤黄疸，无明显皮肤红肿硬肿，无凹陷性水肿，无皮疹, bbox=[65, 545, 906, 563]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[20]: text=，未见出血点，未见瘀斑。皮肤弹性好。无肿大淋巴结。, bbox=[65, 568, 617, 585]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[21]: text=头部及其器官：头颅无畸形；双眼无畸形，双侧瞳孔等大，对光反射存在；双耳无畸, bbox=[65, 593, 906, 611]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[22]: text=形；鼻无畸形。口唇红润，无唇裂，咽无充血。, bbox=[65, 616, 532, 633]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[23]: text=颈部：无抵抗感，气管居中，胸锁乳突肌包块：无。甲状腺正常，无颈部淋巴结肿大, bbox=[65, 642, 906, 659]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[24]: text=。, bbox=[65, 665, 82, 682]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[25]: text=胸部：双侧对称，无畸形；双肩等高，呼吸动度双侧一致，三凹征阴性。肺呼吸音：, bbox=[65, 689, 895, 706]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[26]: text=清，未闻及干湿性啰音，未闻及胸膜摩擦音。, bbox=[65, 712, 509, 729]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[27]: text=心脏：心前区无隆起，心尖搏动位于左侧锁骨中线第5肋间，心音有力，心律齐，未, bbox=[65, 737, 906, 755]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[28]: text=闻及明显杂音，无心包摩擦音。, bbox=[65, 760, 377, 777]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[29]: text=腹部：腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。腹部叩诊呈, bbox=[65, 786, 906, 803]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[30]: text=鼓音；肠鸣音正常，4次/分。, bbox=[65, 809, 360, 826]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[31]: text=肛门外生殖器：肛门位置正常。外阴外观无畸形。, bbox=[65, 835, 552, 852]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[32]: text=脊柱：脊柱生理曲度正常。, bbox=[65, 858, 341, 876]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[33]: text=四肢：四肢肌力正常，肌张力正常。, bbox=[65, 883, 427, 901]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[34]: text=神经系统：双侧腱反射正常，脑膜刺激征阴性，双侧病理征阴性。, bbox=[65, 907, 715, 925]
2026-08-10 19:06:35,223 INFO     29 [qwen-vl-text] coord item[35]: text=专科情况, bbox=[450, 932, 537, 949]
2026-08-10 19:06:35,224 INFO     29 [qwen-vl-text] coord item[36]: text=无。, bbox=[82, 953, 115, 969]
2026-08-10 19:06:35,224 INFO     29 [qwen-vl-text] page=1 — 37/37 coords, api_time=14.9s
2026-08-10 19:06:35,230 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4275073, prompt_len=1350
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共39行）
["入院记录", "辅助检查", "日期", "项目", "结果", "2020-07-29", "胸部CT", "考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检，双肺间质性改变，右肾结石", "2020-08-10", "肺功能", "肺通气功能正常", "2020-08-10", "胸部强化CT", "考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检；右肺门淋巴结肿大；双肺纤维灶；肝囊肿；右肾结石", "2020-08-10", "肺组织活检", "（右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1 (+), CK7(+), Ki-67阳性率10%", "2020-08-14", "骨扫描", "1.右肺坐骨支局限性骨质代谢增高观察；2.L5山医", "2020-08-16", "颅脑MR强化", "强化后FLAIR显示右侧颞枕叶脑沟内条片状轻度山医", "2020-08-31", "肺组织术后病理", "（右肺上叶）浸润性腺癌，腺泡型（60%），乳山医", "2020-09-23", "基因检测", "EGFR等十基因检测（石蜡包埋组织）：EFGR基山医", "2022-06-01", "胸部CT平扫", "右肺术后CT表现，请结合临床；双肺纤维灶左山医", "2023-03-29", "胸部CT平扫", "右肺术后CT表现，较2022-06-01 前片变化不大；双肺多发小结节，对比2022-06-01 前片", "2023-09-13", "CT平扫", "双侧基底节区少许缺血变性灶，必要时结合MRI", "第 3 页"]

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
2026-08-10 19:06:47,594 INFO     29 [qwen-vl-text] coord API raw response (len=2444):
[
	{"text": "入院记录", "bbox": [427, 79, 533, 100]},
	{"text": "辅助检查", "bbox": [441, 136, 525, 153]},
	{"text": "日期", "bbox": [108, 163, 148, 179]},
	{"text": "项目", "bbox": [258, 163, 298, 179]},
	{"text": "结果", "bbox": [547, 160, 589, 176]},
	{"text": "2020-07-29", "bbox": [60, 187, 165, 203]},
	{"text": "胸部CT", "bbox": [198, 187, 258, 202]},
	{"text": "考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检，双肺间质性改变，右肾结石", "bbox": [367, 182, 762, 212]},
	{"text": "2020-08-10", "bbox": [60, 227, 165, 243]},
	{"text": "肺功能", "bbox": [198, 225, 258, 241]},
	{"text": "肺通气功能正常", "bbox": [367, 222, 504, 239]},
	{"text": "2020-08-10", "bbox": [60, 266, 165, 282]},
	{"text": "胸部强化CT", "bbox": [198, 265, 298, 280]},
	{"text": "考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检；右肺门淋巴结肿大；双肺纤维灶；肝囊肿；右肾结石", "bbox": [367, 260, 762, 307]},
	{"text": "2020-08-10", "bbox": [60, 320, 165, 336]},
	{"text": "肺组织活检", "bbox": [198, 319, 298, 335]},
	{"text": "（右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1 (+), CK7(+), Ki-67阳性率10%", "bbox": [367, 315, 773, 390]},
	{"text": "2020-08-14", "bbox": [60, 403, 165, 419]},
	{"text": "骨扫描", "bbox": [200, 402, 258, 418]},
	{"text": "1.右肺坐骨支局限性骨质代谢增高观察；2.L5山医", "bbox": [367, 400, 794, 445]},
	{"text": "2020-08-16", "bbox": [60, 458, 165, 474]},
	{"text": "颅脑MR强化", "bbox": [198, 457, 300, 473]},
	{"text": "强化后FLAIR显示右侧颞枕叶脑沟内条片状轻度山医", "bbox": [367, 454, 794, 499]},
	{"text": "2020-08-31", "bbox": [60, 526, 165, 542]},
	{"text": "肺组织术后病理", "bbox": [198, 525, 342, 541]},
	{"text": "（右肺上叶）浸润性腺癌，腺泡型（60%），乳山医", "bbox": [367, 522, 794, 567]},
	{"text": "2020-09-23", "bbox": [60, 694, 172, 710]},
	{"text": "基因检测", "bbox": [200, 693, 283, 709]},
	{"text": "EGFR等十基因检测（石蜡包埋组织）：EFGR基山医", "bbox": [367, 690, 794, 721]},
	{"text": "2022-06-01", "bbox": [60, 734, 172, 750]},
	{"text": "胸部CT平扫", "bbox": [200, 733, 304, 749]},
	{"text": "右肺术后CT表现，请结合临床；双肺纤维灶左山医", "bbox": [367, 730, 794, 775]},
	{"text": "2023-03-29", "bbox": [60, 802, 172, 818]},
	{"text": "胸部CT平扫", "bbox": [200, 801, 304, 817]},
	{"text": "右肺术后CT表现，较2022-06-01 前片变化不大；双肺多发小结节，对比2022-06-01 前片", "bbox": [367, 798, 794, 843]},
	{"text": "2023-09-13", "bbox": [60, 857, 172, 873]},
	{"text": "CT平扫", "bbox": [200, 856, 268, 872]},
	{"text": "双侧基底节区少许缺血变性灶，必要时结合MRI", "bbox": [367, 853, 773, 872]},
	{"text": "检查；右肺术后CT表现，较前片（2023-03-29）变化不著；双肺多发小结节，对比前片（2023-03-29）增多，建议随诊；脂肪肝；右肾结石", "bbox": [367, 870, 773, 928]},
	{"text": "第 3 页", "bbox": [485, 962, 542, 975]}
]
2026-08-10 19:06:47,594 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=12.4s
2026-08-10 19:06:47,594 INFO     29 [qwen-vl-text] coord item[0]: text=入院记录, bbox=[427, 79, 533, 100]
2026-08-10 19:06:47,594 INFO     29 [qwen-vl-text] coord item[1]: text=辅助检查, bbox=[441, 136, 525, 153]
2026-08-10 19:06:47,594 INFO     29 [qwen-vl-text] coord item[2]: text=日期, bbox=[108, 163, 148, 179]
2026-08-10 19:06:47,595 INFO     29 [qwen-vl-text] coord item[3]: text=项目, bbox=[258, 163, 298, 179]
2026-08-10 19:06:47,595 INFO     29 [qwen-vl-text] coord item[4]: text=结果, bbox=[547, 160, 589, 176]
2026-08-10 19:06:47,595 INFO     29 [qwen-vl-text] coord item[5]: text=2020-07-29, bbox=[60, 187, 165, 203]
2026-08-10 19:06:47,595 INFO     29 [qwen-vl-text] coord item[6]: text=胸部CT, bbox=[198, 187, 258, 202]
2026-08-10 19:06:47,595 INFO     29 [qwen-vl-text] coord item[7]: text=考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检，双肺间质性改变，右肾结石, bbox=[367, 182, 762, 212]
2026-08-10 19:06:47,595 INFO     29 [qwen-vl-text] coord item[8]: text=2020-08-10, bbox=[60, 227, 165, 243]
2026-08-10 19:06:47,595 INFO     29 [qwen-vl-text] coord item[9]: text=肺功能, bbox=[198, 225, 258, 241]
2026-08-10 19:06:47,595 INFO     29 [qwen-vl-text] coord item[10]: text=肺通气功能正常, bbox=[367, 222, 504, 239]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[11]: text=2020-08-10, bbox=[60, 266, 165, 282]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[12]: text=胸部强化CT, bbox=[198, 265, 298, 280]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[13]: text=考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检；右肺门淋巴结肿大；双肺纤维灶；肝囊肿；右肾结石, bbox=[367, 260, 762, 307]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[14]: text=2020-08-10, bbox=[60, 320, 165, 336]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[15]: text=肺组织活检, bbox=[198, 319, 298, 335]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[16]: text=（右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1 (+), CK7(+), Ki-67阳性率10%, bbox=[367, 315, 773, 390]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[17]: text=2020-08-14, bbox=[60, 403, 165, 419]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[18]: text=骨扫描, bbox=[200, 402, 258, 418]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[19]: text=1.右肺坐骨支局限性骨质代谢增高观察；2.L5山医, bbox=[367, 400, 794, 445]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[20]: text=2020-08-16, bbox=[60, 458, 165, 474]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[21]: text=颅脑MR强化, bbox=[198, 457, 300, 473]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[22]: text=强化后FLAIR显示右侧颞枕叶脑沟内条片状轻度山医, bbox=[367, 454, 794, 499]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[23]: text=2020-08-31, bbox=[60, 526, 165, 542]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[24]: text=肺组织术后病理, bbox=[198, 525, 342, 541]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[25]: text=（右肺上叶）浸润性腺癌，腺泡型（60%），乳山医, bbox=[367, 522, 794, 567]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[26]: text=2020-09-23, bbox=[60, 694, 172, 710]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[27]: text=基因检测, bbox=[200, 693, 283, 709]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[28]: text=EGFR等十基因检测（石蜡包埋组织）：EFGR基山医, bbox=[367, 690, 794, 721]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[29]: text=2022-06-01, bbox=[60, 734, 172, 750]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[30]: text=胸部CT平扫, bbox=[200, 733, 304, 749]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[31]: text=右肺术后CT表现，请结合临床；双肺纤维灶左山医, bbox=[367, 730, 794, 775]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[32]: text=2023-03-29, bbox=[60, 802, 172, 818]
2026-08-10 19:06:47,596 INFO     29 [qwen-vl-text] coord item[33]: text=胸部CT平扫, bbox=[200, 801, 304, 817]
2026-08-10 19:06:47,597 INFO     29 [qwen-vl-text] coord item[34]: text=右肺术后CT表现，较2022-06-01 前片变化不大；双肺多发小结节，对比2022-06-01 前片, bbox=[367, 798, 794, 843]
2026-08-10 19:06:47,597 INFO     29 [qwen-vl-text] coord item[35]: text=2023-09-13, bbox=[60, 857, 172, 873]
2026-08-10 19:06:47,597 INFO     29 [qwen-vl-text] coord item[36]: text=CT平扫, bbox=[200, 856, 268, 872]
2026-08-10 19:06:47,597 INFO     29 [qwen-vl-text] coord item[37]: text=双侧基底节区少许缺血变性灶，必要时结合MRI, bbox=[367, 853, 773, 872]
2026-08-10 19:06:47,597 INFO     29 [qwen-vl-text] coord item[38]: text=检查；右肺术后CT表现，较前片（2023-03-29）变化不著；双肺多发小结节，对比前片（2023-03-29）增多，建议随诊；脂肪肝；右肾结石, bbox=[367, 870, 773, 928]
2026-08-10 19:06:47,597 INFO     29 [qwen-vl-text] coord item[39]: text=第 3 页, bbox=[485, 962, 542, 975]
2026-08-10 19:06:47,599 INFO     29 [qwen-vl-text] page=2 — 39/39 coords, api_time=12.4s
2026-08-10 19:06:47,606 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3064473, prompt_len=995
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["入院记录", "住", "2023-11-07", "强化CT", "右肺术后，右肺纤维灶，右侧胸膜增厚，较", "2023-09-19 CT变化不著；双肺多发小结节，", "较前变化不著，请结合临床、随诊复查；提示", "轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊", "肿、左肾盂旁囊肿；右肾小结石、右肾轻度积", "水；右侧附件区囊性低密度，请结合临床及妇", "科超声；左侧耻骨高密度，较前变化不著", "初步诊断：", "1. 右肺上叶浸润性腺癌术后（T1bN2M0, I", "IIA期 EGFR突变：Exon-20（外显子） 20-i", "ns突变阳性）", "2. 右肾结石", "3. 子宫切除术后", "4. 化疗后骨髓抑制", "记录者：", "项目内容", "患方签名", "以上所记录内容属实", "签字时间", "年 月 日 时 分"]

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
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord API raw response (len=1364):
[
	{"text": "入院记录", "bbox": [391, 125, 504, 154]},
	{"text": "住", "bbox": [677, 175, 698, 198]},
	{"text": "2023-11-07", "bbox": [5, 215, 114, 236]},
	{"text": "强化CT", "bbox": [150, 215, 212, 236]},
	{"text": "右肺术后，右肺纤维灶，右侧胸膜增厚，较", "bbox": [325, 213, 727, 235]},
	{"text": "2023-09-19 CT变化不著；双肺多发小结节，", "bbox": [325, 234, 727, 255]},
	{"text": "较前变化不著，请结合临床、随诊复查；提示", "bbox": [325, 254, 749, 276]},
	{"text": "轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊", "bbox": [325, 275, 727, 296]},
	{"text": "肿、左肾盂旁囊肿；右肾小结石、右肾轻度积", "bbox": [325, 295, 749, 317]},
	{"text": "水；右侧附件区囊性低密度，请结合临床及妇", "bbox": [325, 316, 749, 337]},
	{"text": "科超声；左侧耻骨高密度，较前变化不著", "bbox": [325, 336, 706, 358]},
	{"text": "初步诊断：", "bbox": [406, 383, 500, 404]},
	{"text": "1. 右肺上叶浸润性腺癌术后（T1bN2M0, I", "bbox": [460, 412, 900, 434]},
	{"text": "IIA期 EGFR突变：Exon-20（外显子） 20-i", "bbox": [412, 442, 899, 464]},
	{"text": "ns突变阳性）", "bbox": [412, 472, 544, 494]},
	{"text": "2. 右肾结石", "bbox": [460, 503, 578, 524]},
	{"text": "3. 子宫切除术后", "bbox": [462, 532, 625, 554]},
	{"text": "4. 化疗后骨髓抑制", "bbox": [462, 562, 651, 584]},
	{"text": "记录者：", "bbox": [591, 595, 664, 616]},
	{"text": "项目内容", "bbox": [43, 680, 127, 703]},
	{"text": "患方签名", "bbox": [257, 682, 344, 704]},
	{"text": "以上所记录内容属实", "bbox": [46, 719, 233, 742]},
	{"text": "签字时间", "bbox": [46, 760, 130, 782]},
	{"text": "年 月 日 时 分", "bbox": [312, 762, 561, 785]}
]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=7.0s
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[0]: text=入院记录, bbox=[391, 125, 504, 154]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[1]: text=住, bbox=[677, 175, 698, 198]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[2]: text=2023-11-07, bbox=[5, 215, 114, 236]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[3]: text=强化CT, bbox=[150, 215, 212, 236]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[4]: text=右肺术后，右肺纤维灶，右侧胸膜增厚，较, bbox=[325, 213, 727, 235]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[5]: text=2023-09-19 CT变化不著；双肺多发小结节，, bbox=[325, 234, 727, 255]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[6]: text=较前变化不著，请结合临床、随诊复查；提示, bbox=[325, 254, 749, 276]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[7]: text=轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊, bbox=[325, 275, 727, 296]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[8]: text=肿、左肾盂旁囊肿；右肾小结石、右肾轻度积, bbox=[325, 295, 749, 317]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[9]: text=水；右侧附件区囊性低密度，请结合临床及妇, bbox=[325, 316, 749, 337]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[10]: text=科超声；左侧耻骨高密度，较前变化不著, bbox=[325, 336, 706, 358]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[11]: text=初步诊断：, bbox=[406, 383, 500, 404]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[12]: text=1. 右肺上叶浸润性腺癌术后（T1bN2M0, I, bbox=[460, 412, 900, 434]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[13]: text=IIA期 EGFR突变：Exon-20（外显子） 20-i, bbox=[412, 442, 899, 464]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[14]: text=ns突变阳性）, bbox=[412, 472, 544, 494]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[15]: text=2. 右肾结石, bbox=[460, 503, 578, 524]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[16]: text=3. 子宫切除术后, bbox=[462, 532, 625, 554]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[17]: text=4. 化疗后骨髓抑制, bbox=[462, 562, 651, 584]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[18]: text=记录者：, bbox=[591, 595, 664, 616]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[19]: text=项目内容, bbox=[43, 680, 127, 703]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[20]: text=患方签名, bbox=[257, 682, 344, 704]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[21]: text=以上所记录内容属实, bbox=[46, 719, 233, 742]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[22]: text=签字时间, bbox=[46, 760, 130, 782]
2026-08-10 19:06:54,639 INFO     29 [qwen-vl-text] coord item[23]: text=年 月 日 时 分, bbox=[312, 762, 561, 785]
2026-08-10 19:06:54,640 INFO     29 [qwen-vl-text] page=3 — 24/24 coords, api_time=7.0s
2026-08-10 19:06:54,647 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4322732, prompt_len=619
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["X光号："]

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
2026-08-10 19:06:55,444 INFO     29 [qwen-vl-text] coord API raw response (len=60):
```json
[
	{"text": "X光号：", "bbox": [73, 55, 138, 73]}
]
```
2026-08-10 19:06:55,444 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.8s
2026-08-10 19:06:55,444 INFO     29 [qwen-vl-text] coord item[0]: text=X光号：, bbox=[73, 55, 138, 73]
2026-08-10 19:06:55,444 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=0.8s
2026-08-10 19:06:55,444 INFO     29 [qwen-vl-text] new_positions (144):
[[0, 30.34, 48.79, 8.416, 18.936], [0, 207.45999999999998, 235.75, 8.416, 18.936], [0, 30.34, 64.78, 26.3, 36.82], [0, 207.45999999999998, 254.2, 26.3, 36.82], [0, 30.34, 75.03, 43.658, 54.178000000000004], [0, 207.45999999999998, 355.46999999999997, 43.658, 54.178000000000004], [0, 30.34, 75.03, 61.016000000000005, 71.536], [0, 207.45999999999998, 355.46999999999997, 61.016000000000005, 71.536], [0, 30.34, 75.03, 78.37400000000001, 88.894], [0, 207.45999999999998, 254.2, 78.37400000000001, 88.894], [0, 30.34, 132.42999999999998, 95.732, 106.25200000000001], [0, 207.45999999999998, 318.57, 95.732, 106.25200000000001], [0, 12.709999999999999, 239.02999999999997, 113.09, 123.61], [0, 10.66, 390.32, 128.344, 138.864], [0, 10.66, 390.32, 142.02, 152.54000000000002], [0, 10.66, 395.23999999999995, 155.696, 166.216], [0, 10.66, 395.23999999999995, 169.372, 179.892], [0, 10.66, 395.23999999999995, 183.048, 193.568], [0, 10.66, 395.23999999999995, 196.72400000000002, 207.244], [0, 10.66, 395.23999999999995, 209.874, 220.394], [0, 10.66, 395.23999999999995, 223.55, 234.07000000000002], [0, 10.66, 395.23999999999995, 237.226, 247.746], [0, 10.66, 395.23999999999995, 250.90200000000002, 261.422], [0, 10.66, 395.23999999999995, 264.57800000000003, 275.098], [0, 10.66, 395.23999999999995, 278.254, 288.774], [0, 10.66, 395.23999999999995, 291.93, 302.45], [0, 10.66, 388.67999999999995, 305.08000000000004, 315.6], [0, 10.66, 388.67999999999995, 318.75600000000003, 329.276], [0, 10.66, 395.23999999999995, 332.432, 342.952], [0, 10.66, 395.23999999999995, 346.108, 356.62800000000004], [0, 10.66, 391.54999999999995, 359.784, 370.30400000000003], [0, 10.66, 391.54999999999995, 373.46000000000004, 383.98], [0, 10.66, 391.54999999999995, 387.136, 397.656], [0, 10.66, 391.54999999999995, 400.812, 411.332], [0, 10.66, 388.67999999999995, 414.488, 425.00800000000004], [0, 10.66, 391.54999999999995, 428.16400000000004, 438.684], [0, 10.66, 391.54999999999995, 441.84000000000003, 452.36], [0, 10.66, 391.54999999999995, 455.516, 466.036], [0, 10.66, 391.54999999999995, 469.192, 479.71200000000005], [0, 10.66, 391.54999999999995, 482.868, 493.38800000000003], [0, 10.66, 391.54999999999995, 496.54400000000004, 507.064], [0, 10.66, 391.54999999999995, 510.22, 520.74], [0, 197.61999999999998, 223.45, 519.162, 526.0], [1, 176.29999999999998, 219.35, 51.336000000000006, 62.376000000000005], [1, 25.83, 41.0, 70.656, 80.04], [1, 286.18, 308.32, 70.104, 79.488], [1, 26.65, 371.46, 86.11200000000001, 95.49600000000001], [1, 26.65, 371.46, 98.25600000000001, 107.64000000000001], [1, 26.65, 122.99999999999999, 110.4, 119.784], [1, 26.65, 371.46, 124.75200000000001, 134.13600000000002], [1, 26.65, 371.46, 136.89600000000002, 146.28], [1, 26.65, 197.61999999999998, 149.592, 158.976], [1, 26.65, 371.46, 163.94400000000002, 173.328], [1, 26.65, 197.61999999999998, 176.64000000000001, 186.02400000000003], [1, 26.65, 98.39999999999999, 193.752, 203.13600000000002], [1, 26.65, 116.44, 208.104, 217.48800000000003], [1, 26.65, 143.91, 221.90400000000002, 231.288], [1, 182.04, 218.11999999999998, 235.15200000000002, 244.53600000000003], [1, 26.65, 370.22999999999996, 247.848, 257.232], [1, 26.65, 84.05, 260.54400000000004, 269.928], [1, 26.65, 369.0, 274.896, 284.28000000000003], [1, 26.65, 33.62, 287.59200000000004, 296.976], [1, 26.65, 371.46, 300.84000000000003, 310.776], [1, 26.65, 252.97, 313.536, 322.92], [1, 26.65, 371.46, 327.336, 337.27200000000005], [1, 26.65, 218.11999999999998, 340.03200000000004, 349.41600000000005], [1, 26.65, 371.46, 354.384, 363.76800000000003], [1, 26.65, 33.62, 367.08000000000004, 376.46400000000006], [1, 26.65, 366.95, 380.32800000000003, 389.71200000000005], [1, 26.65, 208.69, 393.02400000000006, 402.408], [1, 26.65, 371.46, 406.824, 416.76000000000005], [1, 26.65, 154.57, 419.52000000000004, 428.90400000000005], [1, 26.65, 371.46, 433.872, 443.25600000000003], [1, 26.65, 147.6, 446.56800000000004, 455.95200000000006], [1, 26.65, 226.32, 460.92, 470.30400000000003], [1, 26.65, 139.81, 473.61600000000004, 483.552], [1, 26.65, 175.07, 487.41600000000005, 497.35200000000003], [1, 26.65, 293.15, 500.66400000000004, 510.6], [1, 184.5, 220.17, 514.464, 523.8480000000001], [1, 33.62, 47.15, 526.056, 534.888], [2, 175.07, 218.53, 44.556, 56.39999999999999], [2, 180.81, 215.25, 76.704, 86.29199999999999], [2, 44.279999999999994, 60.68, 91.93199999999999, 100.95599999999999], [2, 105.77999999999999, 122.17999999999999, 91.93199999999999, 100.95599999999999], [2, 224.26999999999998, 241.48999999999998, 90.24, 99.264], [2, 24.599999999999998, 67.64999999999999, 105.46799999999999, 114.49199999999999], [2, 81.17999999999999, 105.77999999999999, 105.46799999999999, 113.92799999999998], [2, 150.47, 312.41999999999996, 102.648, 119.56799999999998], [2, 24.599999999999998, 67.64999999999999, 128.028, 137.052], [2, 81.17999999999999, 105.77999999999999, 126.89999999999999, 135.92399999999998], [2, 150.47, 206.64, 125.20799999999998, 134.796], [2, 24.599999999999998, 67.64999999999999, 150.02399999999997, 159.04799999999997], [2, 81.17999999999999, 122.17999999999999, 149.45999999999998, 157.92], [2, 150.47, 312.41999999999996, 146.64, 173.148], [2, 24.599999999999998, 67.64999999999999, 180.48, 189.504], [2, 81.17999999999999, 122.17999999999999, 179.916, 188.93999999999997], [2, 150.47, 316.93, 177.66, 219.95999999999998], [2, 24.599999999999998, 67.64999999999999, 227.29199999999997, 236.31599999999997], [2, 82.0, 105.77999999999999, 226.72799999999998, 235.75199999999998], [2, 150.47, 325.53999999999996, 225.59999999999997, 250.98], [2, 24.599999999999998, 67.64999999999999, 258.31199999999995, 267.33599999999996], [2, 81.17999999999999, 122.99999999999999, 257.748, 266.772], [2, 150.47, 325.53999999999996, 256.056, 281.436], [2, 24.599999999999998, 67.64999999999999, 296.664, 305.688], [2, 81.17999999999999, 140.22, 296.09999999999997, 305.12399999999997], [2, 150.47, 325.53999999999996, 294.40799999999996, 319.78799999999995], [2, 24.599999999999998, 70.52, 391.41599999999994, 400.43999999999994], [2, 82.0, 116.02999999999999, 390.852, 399.876], [2, 150.47, 325.53999999999996, 389.15999999999997, 406.64399999999995], [2, 24.599999999999998, 70.52, 413.97599999999994, 422.99999999999994], [2, 82.0, 124.63999999999999, 413.412, 422.436], [2, 150.47, 325.53999999999996, 411.71999999999997, 437.09999999999997], [2, 24.599999999999998, 70.52, 452.328, 461.352], [2, 82.0, 124.63999999999999, 451.76399999999995, 460.78799999999995], [2, 150.47, 325.53999999999996, 450.07199999999995, 475.45199999999994], [2, 24.599999999999998, 70.52, 483.34799999999996, 492.37199999999996], [2, 82.0, 109.88, 482.78399999999993, 491.80799999999994], [2, 150.47, 316.93, 481.0919999999999, 491.80799999999994], [2, 150.47, 316.93, 490.67999999999995, 523.3919999999999], [3, 160.31, 206.64, 51.75, 63.756], [3, 277.57, 286.18, 72.45, 81.972], [3, 2.05, 46.739999999999995, 89.00999999999999, 97.704], [3, 61.49999999999999, 86.92, 89.00999999999999, 97.704], [3, 133.25, 298.07, 88.182, 97.28999999999999], [3, 133.25, 298.07, 96.87599999999999, 105.57], [3, 133.25, 307.09, 105.15599999999999, 114.264], [3, 133.25, 298.07, 113.85, 122.544], [3, 133.25, 307.09, 122.13, 131.238], [3, 133.25, 307.09, 130.82399999999998, 139.518], [3, 133.25, 289.46, 139.10399999999998, 148.212], [3, 166.45999999999998, 205.0, 158.56199999999998, 167.256], [3, 188.6, 369.0, 170.56799999999998, 179.676], [3, 168.92, 368.59, 182.988, 192.096], [3, 168.92, 223.04, 195.408, 204.516], [3, 188.6, 236.98, 208.242, 216.93599999999998], [3, 189.42, 256.25, 220.248, 229.356], [3, 189.42, 266.90999999999997, 232.66799999999998, 241.77599999999998], [3, 242.30999999999997, 272.24, 246.32999999999998, 255.024], [3, 17.63, 52.07, 281.52, 291.042], [3, 105.36999999999999, 141.04, 282.348, 291.45599999999996], [3, 18.86, 95.53, 297.666, 307.188], [3, 18.86, 53.3, 314.64, 323.748], [3, 127.91999999999999, 230.01, 315.46799999999996, 324.99], [4, 29.93, 56.58, 30.03, 39.858000000000004]]
2026-08-10 19:06:55,444 INFO     29 [qwen-vl-text] ═══ DONE ═══ 144 positions, pages=5, time=115.1s
2026-08-10 19:06:55,459 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 19:06:55,460 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:06:55,460 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 19:06:55,460 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:06:55.460+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 88, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:06:55,466 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:06:55,467 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:06:55,467 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:06:55,467 INFO     29 [qwen-vl-text] positions(10): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:06:55,467 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [10]
2026-08-10 19:06:55,639 INFO     29 [qwen-vl-text] page=9, rect=410x359, img=(1139x998), dpi=200
2026-08-10 19:06:55,641 INFO     29 [qwen-vl-text] LLM extraction start, text_len=144
2026-08-10 19:06:55,641 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:06:55,641 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 382, \"bbox_end\": 391, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "病理检查报告单\n检查号\n住院号\n姓名\n性别:女\n结论: (右肺上叶)形态符合腺癌,待常规病理免疫组化确诊。\n此报告尚未打印\n当前报告状态: 已打印\n江苏省捷达科技发展有限公司 版权所有 © 2015\nCopyright 2007-2015 JEDA all rights reserved",
    "role": "user"
  }
]
2026-08-10 19:07:02,807 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:07:02,807 INFO     29 [qwen-vl-text] LLM output (len=323):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "右肺上叶",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": null,
  "conclusion": "(右肺上叶)形态符合腺癌,待常规病理免疫组化确诊。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:07:02,811 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2884309, prompt_len=787
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共10行）
["病理检查报告单", "检查号", "住院号", "姓名", "性别:女", "结论: (右肺上叶)形态符合腺癌,待常规病理免疫组化确诊。", "此报告尚未打印", "当前报告状态: 已打印", "江苏省捷达科技发展有限公司 版权所有 © 2015", "Copyright 2007-2015 JEDA all rights reserved"]

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
2026-08-10 19:07:05,940 INFO     29 [qwen-vl-text] coord API raw response (len=583):
[
	{"text": "病理检查报告单", "bbox": [577, 23, 835, 64]},
	{"text": "检查号", "bbox": [110, 93, 182, 120]},
	{"text": "住院号", "bbox": [651, 93, 723, 120]},
	{"text": "姓名", "bbox": [110, 140, 182, 168]},
	{"text": "性别:女", "bbox": [651, 140, 765, 168]},
	{"text": "结论: (右肺上叶)形态符合腺癌,待常规病理免疫组化确诊。", "bbox": [110, 187, 811, 216]},
	{"text": "此报告尚未打印", "bbox": [615, 305, 827, 342]},
	{"text": "当前报告状态: 已打印", "bbox": [434, 389, 752, 427]},
	{"text": "江苏省捷达科技发展有限公司 版权所有 © 2015", "bbox": [577, 791, 919, 814]},
	{"text": "Copyright 2007-2015 JEDA all rights reserved", "bbox": [575, 815, 924, 838]}
]
2026-08-10 19:07:05,940 INFO     29 [qwen-vl-text] coord API: raw_items=10, valid_items=10, elapsed=3.1s
2026-08-10 19:07:05,940 INFO     29 [qwen-vl-text] coord item[0]: text=病理检查报告单, bbox=[577, 23, 835, 64]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[1]: text=检查号, bbox=[110, 93, 182, 120]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[2]: text=住院号, bbox=[651, 93, 723, 120]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[110, 140, 182, 168]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[651, 140, 765, 168]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[5]: text=结论: (右肺上叶)形态符合腺癌,待常规病理免疫组化确诊。, bbox=[110, 187, 811, 216]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[6]: text=此报告尚未打印, bbox=[615, 305, 827, 342]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[7]: text=当前报告状态: 已打印, bbox=[434, 389, 752, 427]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[8]: text=江苏省捷达科技发展有限公司 版权所有 © 2015, bbox=[577, 791, 919, 814]
2026-08-10 19:07:05,941 INFO     29 [qwen-vl-text] coord item[9]: text=Copyright 2007-2015 JEDA all rights reserved, bbox=[575, 815, 924, 838]
2026-08-10 19:07:05,942 INFO     29 [qwen-vl-text] page=9 — 10/10 coords, api_time=3.1s
2026-08-10 19:07:05,943 INFO     29 [qwen-vl-text] new_positions (10):
[[9, 236.57, 342.34999999999997, 8.257, 22.976], [9, 45.099999999999994, 74.61999999999999, 33.387, 43.08], [9, 266.90999999999997, 296.43, 33.387, 43.08], [9, 45.099999999999994, 74.61999999999999, 50.26, 60.312], [9, 266.90999999999997, 313.65, 50.26, 60.312], [9, 45.099999999999994, 332.51, 67.133, 77.544], [9, 252.14999999999998, 339.07, 109.49499999999999, 122.77799999999999], [9, 177.94, 308.32, 139.65099999999998, 153.293], [9, 236.57, 376.78999999999996, 283.969, 292.226], [9, 235.75, 378.84, 292.585, 300.842]]
2026-08-10 19:07:05,943 INFO     29 [qwen-vl-text] ═══ DONE ═══ 10 positions, pages=1, time=10.5s
2026-08-10 19:07:05,943 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:07:05,945 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:07:05,945 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:07:05,945 INFO     29 [qwen-vl-text] positions(14): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:07:05,946 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [14]
2026-08-10 19:07:06,034 INFO     29 [qwen-vl-text] page=10, rect=410x203, img=(1139x564), dpi=200
2026-08-10 19:07:06,036 INFO     29 [qwen-vl-text] LLM extraction start, text_len=312
2026-08-10 19:07:06,036 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:07:06,036 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 392, \"bbox_end\": 405, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "病理检查报告单\n检查号\n住院号\n门诊号:\n姓名\n性别:女\n年龄:57岁\n结合202036909（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体\n呈周围型，肿物切面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内\n结论:查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第\n11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌(2/4)。另送第7组\n淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。\n此报告尚未打印\n当前报告状态:已打印",
    "role": "user"
  }
]
2026-08-10 19:07:10,862 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:07:10,863 INFO     29 [qwen-vl-text] LLM output (len=546):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "右肺上叶",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "结合202036909（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，肿物切面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内",
  "conclusion": "查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌(2/4)。另送第7组淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:07:10,865 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1378717, prompt_len=967
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["病理检查报告单", "检查号", "住院号", "门诊号:", "姓名", "性别:女", "年龄:57岁", "结合202036909（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体", "呈周围型，肿物切面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内", "结论:查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第", "11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌(2/4)。另送第7组", "淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。", "此报告尚未打印", "当前报告状态:已打印"]

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
2026-08-10 19:07:15,967 INFO     29 [qwen-vl-text] coord API raw response (len=955):
[
	{"text": "病理检查报告单", "bbox": [397, 33, 582, 88]},
	{"text": "检查号", "bbox": [65, 127, 118, 165], "bbox": [65, 127, 118, 165]},
	{"text": "住院号", "bbox": [437, 127, 480, 165]},
	{"text": "门诊号:", "bbox": [787, 127, 844, 165]},
	{"text": "姓名", "bbox": [65, 188, 118, 226]},
	{"text": "性别:女", "bbox": [437, 188, 517, 226]},
	{"text": "年龄:57岁", "bbox": [787, 188, 888, 226]},
	{"text": "结合202036909（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体", "bbox": [133, 247, 938, 285]},
	{"text": "呈周围型，肿物切面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内", "bbox": [134, 295, 938, 333]},
	{"text": "结论:查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第", "bbox": [70, 343, 938, 381]},
	{"text": "11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌(2/4)。另送第7组", "bbox": [134, 391, 938, 429]},
	{"text": "淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。", "bbox": [134, 440, 813, 478]},
	{"text": "此报告尚未打印", "bbox": [420, 588, 568, 628]},
	{"text": "当前报告状态:已打印", "bbox": [291, 690, 514, 730]}
]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=5.1s
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[0]: text=病理检查报告单, bbox=[397, 33, 582, 88]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[1]: text=检查号, bbox=[65, 127, 118, 165]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[2]: text=住院号, bbox=[437, 127, 480, 165]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号:, bbox=[787, 127, 844, 165]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[65, 188, 118, 226]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[5]: text=性别:女, bbox=[437, 188, 517, 226]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:57岁, bbox=[787, 188, 888, 226]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[7]: text=结合202036909（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体, bbox=[133, 247, 938, 285]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[8]: text=呈周围型，肿物切面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内, bbox=[134, 295, 938, 333]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[9]: text=结论:查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第, bbox=[70, 343, 938, 381]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[10]: text=11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌(2/4)。另送第7组, bbox=[134, 391, 938, 429]
2026-08-10 19:07:15,968 INFO     29 [qwen-vl-text] coord item[11]: text=淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。, bbox=[134, 440, 813, 478]
2026-08-10 19:07:15,969 INFO     29 [qwen-vl-text] coord item[12]: text=此报告尚未打印, bbox=[420, 588, 568, 628]
2026-08-10 19:07:15,969 INFO     29 [qwen-vl-text] coord item[13]: text=当前报告状态:已打印, bbox=[291, 690, 514, 730]
2026-08-10 19:07:15,969 INFO     29 [qwen-vl-text] page=10 — 14/14 coords, api_time=5.1s
2026-08-10 19:07:15,969 INFO     29 [qwen-vl-text] new_positions (14):
[[10, 162.76999999999998, 238.61999999999998, 6.699000000000001, 17.864], [10, 26.65, 48.379999999999995, 25.781000000000002, 33.495000000000005], [10, 179.17, 196.79999999999998, 25.781000000000002, 33.495000000000005], [10, 322.66999999999996, 346.03999999999996, 25.781000000000002, 33.495000000000005], [10, 26.65, 48.379999999999995, 38.164, 45.878], [10, 179.17, 211.97, 38.164, 45.878], [10, 322.66999999999996, 364.08, 38.164, 45.878], [10, 54.529999999999994, 384.58, 50.141000000000005, 57.855000000000004], [10, 54.94, 384.58, 59.885000000000005, 67.599], [10, 28.7, 384.58, 69.629, 77.343], [10, 54.94, 384.58, 79.373, 87.087], [10, 54.94, 333.33, 89.32000000000001, 97.034], [10, 172.2, 232.88, 119.364, 127.48400000000001], [10, 119.30999999999999, 210.73999999999998, 140.07000000000002, 148.19]]
2026-08-10 19:07:15,969 INFO     29 [qwen-vl-text] ═══ DONE ═══ 14 positions, pages=1, time=10.0s
2026-08-10 19:07:15,969 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:07:15,971 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:07:15,971 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:07:15,971 INFO     29 [qwen-vl-text] positions(102): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:07:15,972 INFO     29 [qwen-vl-text] page grouping: [11, 12], lines per page: [61, 41]
2026-08-10 19:07:16,211 INFO     29 [qwen-vl-text] page=11, rect=410x508, img=(1139x1412), dpi=200
2026-08-10 19:07:16,454 INFO     29 [qwen-vl-text] page=12, rect=410x546, img=(1139x1517), dpi=200
2026-08-10 19:07:16,455 INFO     29 [qwen-vl-text] LLM extraction start, text_len=917
2026-08-10 19:07:16,455 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:07:16,456 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 406, \"bbox_end\": 507, \"encounter_dates\": [\"2020-09-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "分子病理基因检测报告单\n样本信息\n项目编号：PCR20-1135\n姓名\n性别：女\n年龄：57岁\n住院号\n病理号\n送检医生\n标本类别：石蜡包埋组织\n送检科室\n送检时间：2020-09-23\n送检医院：本院\n联系电话\n检测方法：ARMS PCR\n检测位点：\n检查项目：九基因\n检测结果\n检测项目\n外显因子\n突变类型\n检测结果\nEGFR基因\nExon19\n19-del\n野生型\nExon21\nL858R\n野生型\nExon20\nT790M\n野生型\nExon18\nG719X\n野生型\nExon20\nS768I\n野生型\nExon21\nL861Q\n野生型\nExon20\n20-ins\n突变型\nKRAS基因\nExon-2\nG12D/S\n野生型\nG12A/V/R/C、G13C\n野生型\nBRAF基因\nExon-15\nV600E/K/R/D\n野生型\nNRAS基因\nExon-3\nQ61R/K/L/H\n野生型\n初诊医师：戚美\n复诊医师：刘龙\n报告日期：2020-09-23\n分子病理基因检测报告单\n检测项目\n外显因子\n突变类型\n检测结果\nPIK3CA基因\nExon-20\nH1047R\n野生型\nExon-9\nE545K\nALK融合基因\nALK-Exon-20\n具体突变类型见附录\n野生型\nROS1融合基因\nROS1-Exon-32/34/35\n具体突变类型见附录\n野生型\nRET融合基因\nRET-Exon-12\n具体突变类型见附录\n野生型\nHER2基因\nExon-20\n20-ins/G776>VC(1)\n野生型\nMET基因\nMET-Exon-14\nMET exon13;METexon15\n野生型\n备注：\n由于肿瘤存在异质性现象，此检测结果只针对本次样本有效。结果仅供临床参考\n，不可作为临床诊治的唯一依据。\n驱动基因突变状态是靶向药物治疗的重要疗效预测因子，EGFR和KRAS突变状态可\n以指导EGFR-TKIs的用药；ALK、ROS1基因融合突变及MET外显子14跳跃突变可以\n从ALK/ROS1/MET抑制剂中明显受益；BRAF基因突变患者可以从RAF抑制剂和MEK\n抑制剂中明显受益\n初诊医师：戚美\n复诊医师：刘龙\n报告日期：2020-09-23",
    "role": "user"
  }
]
2026-08-10 19:07:27,740 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:07:27.739+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 88, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:07:27,942 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:07:27,942 INFO     29 [qwen-vl-text] LLM output (len=1349):
{
  "exam_date": "2020-09-23",
  "report_date": "2020-09-23",
  "exam_name": "分子病理基因检测",
  "exam_category": "pathology",
  "body_part": "石蜡包埋组织",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "检测方法：ARMS PCR\n检测位点：\n检查项目：九基因\n检测结果\n| 检测项目 | 外显因子 | 突变类型 | 检测结果 |\n| :--- | :--- | :--- | :--- |\n| EGFR基因 | Exon19 | 19-del | 野生型 |\n| EGFR基因 | Exon21 | L858R | 野生型 |\n| EGFR基因 | Exon20 | T790M | 野生型 |\n| EGFR基因 | Exon18 | G719X | 野生型 |\n| EGFR基因 | Exon20 | S768I | 野生型 |\n| EGFR基因 | Exon21 | L861Q | 野生型 |\n| EGFR基因 | Exon20 | 20-ins | 突变型 |\n| KRAS基因 | Exon-2 | G12D/S | 野生型 |\n| KRAS基因 | Exon-2 | G12A/V/R/C、G13C | 野生型 |\n| BRAF基因 | Exon-15 | V600E/K/R/D | 野生型 |\n| NRAS基因 | Exon-3 | Q61R/K/L/H | 野生型 |\n| PIK3CA基因 | Exon-20 | H1047R | 野生型 |\n| PIK3CA基因 | Exon-9 | E545K | 野生型 |\n| ALK融合基因 | ALK-Exon-20 | 具体突变类型见附录 | 野生型 |\n| ROS1融合基因 | ROS1-Exon-32/34/35 | 具体突变类型见附录 | 野生型 |\n| RET融合基因 | RET-Exon-12 | 具体突变类型见附录 | 野生型 |\n| HER2基因 | Exon-20 | 20-ins/G776>VC(1) | 野生型 |\n| MET基因 | MET-Exon-14 | MET exon13;METexon15 | 野生型 |",
  "conclusion": "备注：\n由于肿瘤存在异质性现象，此检测结果只针对本次样本有效。结果仅供临床参考\n，不可作为临床诊治的唯一依据。\n驱动基因突变状态是靶向药物治疗的重要疗效预测因子，EGFR和KRAS突变状态可\n以指导EGFR-TKIs的用药；ALK、ROS1基因融合突变及MET外显子14跳跃突变可以\n从ALK/ROS1/MET抑制剂中明显受益；BRAF基因突变患者可以从RAF抑制剂和MEK\n抑制剂中明显受益",
  "physician": "戚美",
  "reviewer": "刘龙"
}
2026-08-10 19:07:27,951 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3880681, prompt_len=1221
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共61行）
["分子病理基因检测报告单", "样本信息", "项目编号：PCR20-1135", "姓名", "性别：女", "年龄：57岁", "住院号", "病理号", "送检医生", "标本类别：石蜡包埋组织", "送检科室", "送检时间：2020-09-23", "送检医院：本院", "联系电话", "检测方法：ARMS PCR", "检测位点：", "检查项目：九基因", "检测结果", "检测项目", "外显因子", "突变类型", "检测结果", "EGFR基因", "Exon19", "19-del", "野生型", "Exon21", "L858R", "野生型", "Exon20", "T790M", "野生型", "Exon18", "G719X", "野生型", "Exon20", "S768I", "野生型", "Exon21", "L861Q", "野生型", "Exon20", "20-ins", "突变型", "KRAS基因", "Exon-2", "G12D/S", "野生型", "G12A/V/R/C、G13C", "野生型", "BRAF基因", "Exon-15", "V600E/K/R/D", "野生型", "NRAS基因", "Exon-3", "Q61R/K/L/H", "野生型", "初诊医师：戚美", "复诊医师：刘龙", "报告日期：2020-09-23"]

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
2026-08-10 19:07:44,936 INFO     29 [qwen-vl-text] coord API raw response (len=3093):
[
	{"text": "分子病理基因检测报告单", "bbox": [379, 19, 706, 46]},
	{"text": "样本信息", "bbox": [60, 40, 178, 67]},
	{"text": "项目编号：PCR20-1135", "bbox": [48, 81, 278, 102]},
	{"text": "姓名", "bbox": [48, 125, 140, 148]},
	{"text": "性别：女", "bbox": [331, 125, 467, 148]},
	{"text": "年龄：57岁", "bbox": [617, 125, 807, 148]},
	{"text": "住院号", "bbox": [48, 174, 140, 197]},
	{"text": "病理号", "bbox": [331, 174, 424, 197]},
	{"text": "送检医生", "bbox": [617, 174, 706, 197]},
	{"text": "标本类别：石蜡包埋组织", "bbox": [48, 224, 300, 247]},
	{"text": "送检科室", "bbox": [331, 224, 420, 247]},
	{"text": "送检时间：2020-09-23", "bbox": [617, 224, 850, 247]},
	{"text": "送检医院：本院", "bbox": [50, 273, 208, 296]},
	{"text": "联系电话", "bbox": [617, 273, 706, 296]},
	{"text": "检测方法：ARMS PCR", "bbox": [48, 318, 254, 339]},
	{"text": "检测位点：", "bbox": [351, 318, 450, 339]},
	{"text": "检查项目：九基因", "bbox": [619, 318, 790, 339]},
	{"text": "检测结果", "bbox": [74, 347, 190, 371]},
	{"text": "检测项目", "bbox": [98, 405, 192, 428]},
	{"text": "外显因子", "bbox": [308, 405, 403, 428]},
	{"text": "突变类型", "bbox": [515, 405, 610, 428]},
	{"text": "检测结果", "bbox": [744, 405, 840, 428]},
	{"text": "EGFR基因", "bbox": [92, 540, 192, 560]},
	{"text": "Exon19", "bbox": [316, 442, 389, 461]},
	{"text": "19-del", "bbox": [532, 440, 600, 459]},
	{"text": "野生型", "bbox": [758, 440, 824, 461]},
	{"text": "Exon21", "bbox": [316, 473, 387, 491]},
	{"text": "L858R", "bbox": [531, 473, 590, 491]},
	{"text": "野生型", "bbox": [758, 473, 824, 491]},
	{"text": "Exon20", "bbox": [316, 506, 389, 524]},
	{"text": "T790M", "bbox": [531, 506, 590, 524]},
	{"text": "野生型", "bbox": [758, 506, 824, 524]},
	{"text": "Exon18", "bbox": [316, 540, 389, 558]},
	{"text": "G719X", "bbox": [531, 540, 590, 558]},
	{"text": "野生型", "bbox": [758, 540, 824, 558]},
	{"text": "Exon20", "bbox": [316, 572, 389, 590]},
	{"text": "S768I", "bbox": [531, 572, 589, 590]},
	{"text": "野生型", "bbox": [758, 572, 824, 590]},
	{"text": "Exon21", "bbox": [316, 604, 387, 623]},
	{"text": "L861Q", "bbox": [528, 607, 589, 625]},
	{"text": "野生型", "bbox": [758, 604, 824, 623]},
	{"text": "Exon20", "bbox": [316, 638, 389, 656]},
	{"text": "20-ins", "bbox": [529, 635, 600, 654]},
	{"text": "突变型", "bbox": [754, 635, 819, 656]},
	{"text": "KRAS基因", "bbox": [90, 691, 190, 711]},
	{"text": "Exon-2", "bbox": [314, 687, 387, 705]},
	{"text": "G12D/S", "bbox": [528, 668, 600, 687]},
	{"text": "野生型", "bbox": [754, 668, 819, 687]},
	{"text": "G12A/V/R/C、G13C", "bbox": [472, 703, 661, 721]},
	{"text": "野生型", "bbox": [754, 703, 819, 721]},
	{"text": "BRAF基因", "bbox": [90, 737, 188, 756]},
	{"text": "Exon-15", "bbox": [314, 734, 398, 752]},
	{"text": "V600E/K/R/D", "bbox": [505, 734, 634, 752]},
	{"text": "野生型", "bbox": [754, 734, 819, 752]},
	{"text": "NRAS基因", "bbox": [90, 769, 188, 788]},
	{"text": "Exon-3", "bbox": [314, 769, 387, 787]},
	{"text": "Q61R/K/L/H", "bbox": [505, 769, 622, 787]},
	{"text": "野生型", "bbox": [754, 769, 819, 787]},
	{"text": "初诊医师：戚美", "bbox": [95, 911, 259, 931]},
	{"text": "复诊医师：刘龙", "bbox": [592, 908, 747, 928]},
	{"text": "报告日期：2020-09-23", "bbox": [592, 941, 819, 961]}
]
2026-08-10 19:07:44,938 INFO     29 [qwen-vl-text] coord API: raw_items=61, valid_items=61, elapsed=17.0s
2026-08-10 19:07:44,938 INFO     29 [qwen-vl-text] coord item[0]: text=分子病理基因检测报告单, bbox=[379, 19, 706, 46]
2026-08-10 19:07:44,938 INFO     29 [qwen-vl-text] coord item[1]: text=样本信息, bbox=[60, 40, 178, 67]
2026-08-10 19:07:44,938 INFO     29 [qwen-vl-text] coord item[2]: text=项目编号：PCR20-1135, bbox=[48, 81, 278, 102]
2026-08-10 19:07:44,938 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[48, 125, 140, 148]
2026-08-10 19:07:44,938 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[331, 125, 467, 148]
2026-08-10 19:07:44,938 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：57岁, bbox=[617, 125, 807, 148]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[6]: text=住院号, bbox=[48, 174, 140, 197]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[7]: text=病理号, bbox=[331, 174, 424, 197]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[8]: text=送检医生, bbox=[617, 174, 706, 197]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[9]: text=标本类别：石蜡包埋组织, bbox=[48, 224, 300, 247]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[10]: text=送检科室, bbox=[331, 224, 420, 247]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[11]: text=送检时间：2020-09-23, bbox=[617, 224, 850, 247]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[12]: text=送检医院：本院, bbox=[50, 273, 208, 296]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[13]: text=联系电话, bbox=[617, 273, 706, 296]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[14]: text=检测方法：ARMS PCR, bbox=[48, 318, 254, 339]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[15]: text=检测位点：, bbox=[351, 318, 450, 339]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[16]: text=检查项目：九基因, bbox=[619, 318, 790, 339]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[17]: text=检测结果, bbox=[74, 347, 190, 371]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[18]: text=检测项目, bbox=[98, 405, 192, 428]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[19]: text=外显因子, bbox=[308, 405, 403, 428]
2026-08-10 19:07:44,939 INFO     29 [qwen-vl-text] coord item[20]: text=突变类型, bbox=[515, 405, 610, 428]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[21]: text=检测结果, bbox=[744, 405, 840, 428]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[22]: text=EGFR基因, bbox=[92, 540, 192, 560]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[23]: text=Exon19, bbox=[316, 442, 389, 461]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[24]: text=19-del, bbox=[532, 440, 600, 459]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[25]: text=野生型, bbox=[758, 440, 824, 461]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[26]: text=Exon21, bbox=[316, 473, 387, 491]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[27]: text=L858R, bbox=[531, 473, 590, 491]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[28]: text=野生型, bbox=[758, 473, 824, 491]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[29]: text=Exon20, bbox=[316, 506, 389, 524]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[30]: text=T790M, bbox=[531, 506, 590, 524]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[31]: text=野生型, bbox=[758, 506, 824, 524]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[32]: text=Exon18, bbox=[316, 540, 389, 558]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[33]: text=G719X, bbox=[531, 540, 590, 558]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[34]: text=野生型, bbox=[758, 540, 824, 558]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[35]: text=Exon20, bbox=[316, 572, 389, 590]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[36]: text=S768I, bbox=[531, 572, 589, 590]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[37]: text=野生型, bbox=[758, 572, 824, 590]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[38]: text=Exon21, bbox=[316, 604, 387, 623]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[39]: text=L861Q, bbox=[528, 607, 589, 625]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[40]: text=野生型, bbox=[758, 604, 824, 623]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[41]: text=Exon20, bbox=[316, 638, 389, 656]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[42]: text=20-ins, bbox=[529, 635, 600, 654]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[43]: text=突变型, bbox=[754, 635, 819, 656]
2026-08-10 19:07:44,940 INFO     29 [qwen-vl-text] coord item[44]: text=KRAS基因, bbox=[90, 691, 190, 711]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[45]: text=Exon-2, bbox=[314, 687, 387, 705]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[46]: text=G12D/S, bbox=[528, 668, 600, 687]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[47]: text=野生型, bbox=[754, 668, 819, 687]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[48]: text=G12A/V/R/C、G13C, bbox=[472, 703, 661, 721]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[49]: text=野生型, bbox=[754, 703, 819, 721]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[50]: text=BRAF基因, bbox=[90, 737, 188, 756]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[51]: text=Exon-15, bbox=[314, 734, 398, 752]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[52]: text=V600E/K/R/D, bbox=[505, 734, 634, 752]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[53]: text=野生型, bbox=[754, 734, 819, 752]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[54]: text=NRAS基因, bbox=[90, 769, 188, 788]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[55]: text=Exon-3, bbox=[314, 769, 387, 787]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[56]: text=Q61R/K/L/H, bbox=[505, 769, 622, 787]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[57]: text=野生型, bbox=[754, 769, 819, 787]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[58]: text=初诊医师：戚美, bbox=[95, 911, 259, 931]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[59]: text=复诊医师：刘龙, bbox=[592, 908, 747, 928]
2026-08-10 19:07:44,941 INFO     29 [qwen-vl-text] coord item[60]: text=报告日期：2020-09-23, bbox=[592, 941, 819, 961]
2026-08-10 19:07:44,942 INFO     29 [qwen-vl-text] page=11 — 61/61 coords, api_time=17.0s
2026-08-10 19:07:44,954 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4249086, prompt_len=1227
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共41行）
["分子病理基因检测报告单", "检测项目", "外显因子", "突变类型", "检测结果", "PIK3CA基因", "Exon-20", "H1047R", "野生型", "Exon-9", "E545K", "ALK融合基因", "ALK-Exon-20", "具体突变类型见附录", "野生型", "ROS1融合基因", "ROS1-Exon-32/34/35", "具体突变类型见附录", "野生型", "RET融合基因", "RET-Exon-12", "具体突变类型见附录", "野生型", "HER2基因", "Exon-20", "20-ins/G776>VC(1)", "野生型", "MET基因", "MET-Exon-14", "MET exon13;METexon15", "野生型", "备注：", "由于肿瘤存在异质性现象，此检测结果只针对本次样本有效。结果仅供临床参考", "，不可作为临床诊治的唯一依据。", "驱动基因突变状态是靶向药物治疗的重要疗效预测因子，EGFR和KRAS突变状态可", "以指导EGFR-TKIs的用药；ALK、ROS1基因融合突变及MET外显子14跳跃突变可以", "从ALK/ROS1/MET抑制剂中明显受益；BRAF基因突变患者可以从RAF抑制剂和MEK", "抑制剂中明显受益", "初诊医师：戚美", "复诊医师：刘龙", "报告日期：2020-09-23"]

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
2026-08-10 19:07:55,892 INFO     29 [qwen-vl-text] coord API raw response (len=2284):
[
	{"text": "分子病理基因检测报告单", "bbox": [350, 134, 679, 158]},
	{"text": "检测项目", "bbox": [90, 244, 184, 265]},
	{"text": "外显因子", "bbox": [309, 244, 406, 265]},
	{"text": "突变类型", "bbox": [507, 244, 605, 265]},
	{"text": "检测结果", "bbox": [726, 244, 824, 265]},
	{"text": "PIK3CA基因", "bbox": [77, 312, 202, 331]},
	{"text": "Exon-20", "bbox": [319, 292, 393, 308]},
	{"text": "H1047R", "bbox": [516, 292, 590, 308]},
	{"text": "野生型", "bbox": [734, 313, 802, 332]},
	{"text": "Exon-9", "bbox": [317, 338, 380, 354]},
	{"text": "E545K", "bbox": [511, 338, 570, 354]},
	{"text": "ALK融合基因", "bbox": [77, 383, 210, 402]},
	{"text": "ALK-Exon-20", "bbox": [294, 387, 409, 403]},
	{"text": "具体突变类型见附录", "bbox": [475, 387, 638, 405]},
	{"text": "野生型", "bbox": [736, 388, 804, 407]},
	{"text": "ROS1融合基因", "bbox": [73, 428, 218, 447]},
	{"text": "ROS1-Exon-32/34/35", "bbox": [263, 432, 448, 449]},
	{"text": "具体突变类型见附录", "bbox": [474, 433, 635, 451]},
	{"text": "野生型", "bbox": [735, 434, 803, 453]},
	{"text": "RET融合基因", "bbox": [81, 470, 214, 489]},
	{"text": "RET-Exon-12", "bbox": [291, 474, 411, 490]},
	{"text": "具体突变类型见附录", "bbox": [473, 475, 633, 493]},
	{"text": "野生型", "bbox": [734, 476, 802, 495]},
	{"text": "HER2基因", "bbox": [95, 512, 193, 530]},
	{"text": "Exon-20", "bbox": [324, 517, 396, 533]},
	{"text": "20-ins/G776>VC(1)", "bbox": [470, 518, 643, 537]},
	{"text": "野生型", "bbox": [734, 520, 802, 539]},
	{"text": "MET基因", "bbox": [103, 555, 189, 573]},
	{"text": "MET-Exon-14", "bbox": [285, 565, 406, 580]},
	{"text": "MET exon13;METexon15", "bbox": [461, 566, 643, 582]},
	{"text": "野生型", "bbox": [734, 568, 802, 587]},
	{"text": "备注：", "bbox": [89, 623, 153, 644]},
	{"text": "由于肿瘤存在异质性现象，此检测结果只针对本次样本有效。结果仅供临床参考", "bbox": [73, 650, 835, 677]},
	{"text": "，不可作为临床诊治的唯一依据。", "bbox": [73, 668, 384, 690]},
	{"text": "驱动基因突变状态是靶向药物治疗的重要疗效预测因子，EGFR和KRAS突变状态可", "bbox": [73, 687, 838, 713]},
	{"text": "以指导EGFR-TKIs的用药；ALK、ROS1基因融合突变及MET外显子14跳跃突变可以", "bbox": [73, 705, 837, 731]},
	{"text": "从ALK/ROS1/MET抑制剂中明显受益；BRAF基因突变患者可以从RAF抑制剂和MEK", "bbox": [73, 723, 827, 749]},
	{"text": "抑制剂中明显受益", "bbox": [73, 737, 243, 757]},
	{"text": "初诊医师：戚美", "bbox": [75, 831, 224, 851]},
	{"text": "复诊医师：刘龙", "bbox": [537, 839, 697, 859]},
	{"text": "报告日期：2020-09-23", "bbox": [545, 870, 768, 892]}
]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord API: raw_items=41, valid_items=41, elapsed=10.9s
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[0]: text=分子病理基因检测报告单, bbox=[350, 134, 679, 158]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[1]: text=检测项目, bbox=[90, 244, 184, 265]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[2]: text=外显因子, bbox=[309, 244, 406, 265]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[3]: text=突变类型, bbox=[507, 244, 605, 265]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[4]: text=检测结果, bbox=[726, 244, 824, 265]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[5]: text=PIK3CA基因, bbox=[77, 312, 202, 331]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[6]: text=Exon-20, bbox=[319, 292, 393, 308]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[7]: text=H1047R, bbox=[516, 292, 590, 308]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[8]: text=野生型, bbox=[734, 313, 802, 332]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[9]: text=Exon-9, bbox=[317, 338, 380, 354]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[10]: text=E545K, bbox=[511, 338, 570, 354]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[11]: text=ALK融合基因, bbox=[77, 383, 210, 402]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[12]: text=ALK-Exon-20, bbox=[294, 387, 409, 403]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[13]: text=具体突变类型见附录, bbox=[475, 387, 638, 405]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[14]: text=野生型, bbox=[736, 388, 804, 407]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[15]: text=ROS1融合基因, bbox=[73, 428, 218, 447]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[16]: text=ROS1-Exon-32/34/35, bbox=[263, 432, 448, 449]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[17]: text=具体突变类型见附录, bbox=[474, 433, 635, 451]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[18]: text=野生型, bbox=[735, 434, 803, 453]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[19]: text=RET融合基因, bbox=[81, 470, 214, 489]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[20]: text=RET-Exon-12, bbox=[291, 474, 411, 490]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[21]: text=具体突变类型见附录, bbox=[473, 475, 633, 493]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[22]: text=野生型, bbox=[734, 476, 802, 495]
2026-08-10 19:07:55,893 INFO     29 [qwen-vl-text] coord item[23]: text=HER2基因, bbox=[95, 512, 193, 530]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[24]: text=Exon-20, bbox=[324, 517, 396, 533]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[25]: text=20-ins/G776>VC(1), bbox=[470, 518, 643, 537]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[26]: text=野生型, bbox=[734, 520, 802, 539]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[27]: text=MET基因, bbox=[103, 555, 189, 573]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[28]: text=MET-Exon-14, bbox=[285, 565, 406, 580]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[29]: text=MET exon13;METexon15, bbox=[461, 566, 643, 582]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[30]: text=野生型, bbox=[734, 568, 802, 587]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[31]: text=备注：, bbox=[89, 623, 153, 644]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[32]: text=由于肿瘤存在异质性现象，此检测结果只针对本次样本有效。结果仅供临床参考, bbox=[73, 650, 835, 677]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[33]: text=，不可作为临床诊治的唯一依据。, bbox=[73, 668, 384, 690]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[34]: text=驱动基因突变状态是靶向药物治疗的重要疗效预测因子，EGFR和KRAS突变状态可, bbox=[73, 687, 838, 713]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[35]: text=以指导EGFR-TKIs的用药；ALK、ROS1基因融合突变及MET外显子14跳跃突变可以, bbox=[73, 705, 837, 731]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[36]: text=从ALK/ROS1/MET抑制剂中明显受益；BRAF基因突变患者可以从RAF抑制剂和MEK, bbox=[73, 723, 827, 749]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[37]: text=抑制剂中明显受益, bbox=[73, 737, 243, 757]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[38]: text=初诊医师：戚美, bbox=[75, 831, 224, 851]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[39]: text=复诊医师：刘龙, bbox=[537, 839, 697, 859]
2026-08-10 19:07:55,894 INFO     29 [qwen-vl-text] coord item[40]: text=报告日期：2020-09-23, bbox=[545, 870, 768, 892]
2026-08-10 19:07:55,896 INFO     29 [qwen-vl-text] page=12 — 41/41 coords, api_time=10.9s
2026-08-10 19:07:55,896 INFO     29 [qwen-vl-text] new_positions (102):
[[11, 155.39, 289.46, 9.652000000000001, 23.368000000000002], [11, 24.599999999999998, 72.97999999999999, 20.32, 34.036], [11, 19.68, 113.97999999999999, 41.148, 51.816], [11, 19.68, 57.4, 63.5, 75.184], [11, 135.70999999999998, 191.47, 63.5, 75.184], [11, 252.97, 330.87, 63.5, 75.184], [11, 19.68, 57.4, 88.392, 100.07600000000001], [11, 135.70999999999998, 173.84, 88.392, 100.07600000000001], [11, 252.97, 289.46, 88.392, 100.07600000000001], [11, 19.68, 122.99999999999999, 113.792, 125.476], [11, 135.70999999999998, 172.2, 113.792, 125.476], [11, 252.97, 348.5, 113.792, 125.476], [11, 20.5, 85.28, 138.684, 150.368], [11, 252.97, 289.46, 138.684, 150.368], [11, 19.68, 104.14, 161.544, 172.212], [11, 143.91, 184.5, 161.544, 172.212], [11, 253.79, 323.9, 161.544, 172.212], [11, 30.34, 77.89999999999999, 176.276, 188.468], [11, 40.18, 78.72, 205.74, 217.424], [11, 126.27999999999999, 165.23, 205.74, 217.424], [11, 211.14999999999998, 250.1, 205.74, 217.424], [11, 305.03999999999996, 344.4, 205.74, 217.424], [11, 37.72, 78.72, 274.32, 284.48], [11, 129.56, 159.48999999999998, 224.536, 234.18800000000002], [11, 218.11999999999998, 245.99999999999997, 223.52, 233.172], [11, 310.78, 337.84, 223.52, 234.18800000000002], [11, 129.56, 158.67, 240.284, 249.428], [11, 217.70999999999998, 241.89999999999998, 240.284, 249.428], [11, 310.78, 337.84, 240.284, 249.428], [11, 129.56, 159.48999999999998, 257.048, 266.192], [11, 217.70999999999998, 241.89999999999998, 257.048, 266.192], [11, 310.78, 337.84, 257.048, 266.192], [11, 129.56, 159.48999999999998, 274.32, 283.464], [11, 217.70999999999998, 241.89999999999998, 274.32, 283.464], [11, 310.78, 337.84, 274.32, 283.464], [11, 129.56, 159.48999999999998, 290.576, 299.72], [11, 217.70999999999998, 241.48999999999998, 290.576, 299.72], [11, 310.78, 337.84, 290.576, 299.72], [11, 129.56, 158.67, 306.832, 316.484], [11, 216.48, 241.48999999999998, 308.356, 317.5], [11, 310.78, 337.84, 306.832, 316.484], [11, 129.56, 159.48999999999998, 324.104, 333.248], [11, 216.89, 245.99999999999997, 322.58, 332.232], [11, 309.14, 335.78999999999996, 322.58, 333.248], [11, 36.9, 77.89999999999999, 351.028, 361.188], [11, 128.73999999999998, 158.67, 348.996, 358.14], [11, 216.48, 245.99999999999997, 339.344, 348.996], [11, 309.14, 335.78999999999996, 339.344, 348.996], [11, 193.51999999999998, 271.01, 357.124, 366.26800000000003], [11, 309.14, 335.78999999999996, 357.124, 366.26800000000003], [11, 36.9, 77.08, 374.396, 384.048], [11, 128.73999999999998, 163.17999999999998, 372.872, 382.016], [11, 207.04999999999998, 259.94, 372.872, 382.016], [11, 309.14, 335.78999999999996, 372.872, 382.016], [11, 36.9, 77.08, 390.652, 400.30400000000003], [11, 128.73999999999998, 158.67, 390.652, 399.796], [11, 207.04999999999998, 255.01999999999998, 390.652, 399.796], [11, 309.14, 335.78999999999996, 390.652, 399.796], [11, 38.949999999999996, 106.19, 462.788, 472.948], [11, 242.72, 306.27, 461.264, 471.424], [11, 242.72, 335.78999999999996, 478.028, 488.188], [12, 143.5, 278.39, 73.164, 86.268], [12, 36.9, 75.44, 133.22400000000002, 144.69], [12, 126.69, 166.45999999999998, 133.22400000000002, 144.69], [12, 207.86999999999998, 248.04999999999998, 133.22400000000002, 144.69], [12, 297.65999999999997, 337.84, 133.22400000000002, 144.69], [12, 31.569999999999997, 82.82, 170.352, 180.72600000000003], [12, 130.79, 161.13, 159.43200000000002, 168.168], [12, 211.55999999999997, 241.89999999999998, 159.43200000000002, 168.168], [12, 300.94, 328.82, 170.89800000000002, 181.27200000000002], [12, 129.97, 155.79999999999998, 184.548, 193.28400000000002], [12, 209.51, 233.7, 184.548, 193.28400000000002], [12, 31.569999999999997, 86.1, 209.11800000000002, 219.49200000000002], [12, 120.53999999999999, 167.69, 211.30200000000002, 220.038], [12, 194.75, 261.58, 211.30200000000002, 221.13000000000002], [12, 301.76, 329.64, 211.848, 222.222], [12, 29.93, 89.38, 233.68800000000002, 244.062], [12, 107.83, 183.67999999999998, 235.872, 245.15400000000002], [12, 194.33999999999997, 260.34999999999997, 236.418, 246.246], [12, 301.34999999999997, 329.22999999999996, 236.96400000000003, 247.33800000000002], [12, 33.21, 87.74, 256.62, 266.994], [12, 119.30999999999999, 168.51, 258.80400000000003, 267.54], [12, 193.92999999999998, 259.53, 259.35, 269.178], [12, 300.94, 328.82, 259.896, 270.27000000000004], [12, 38.949999999999996, 79.13, 279.552, 289.38], [12, 132.84, 162.35999999999999, 282.28200000000004, 291.01800000000003], [12, 192.7, 263.63, 282.82800000000003, 293.202], [12, 300.94, 328.82, 283.92, 294.29400000000004], [12, 42.23, 77.49, 303.03000000000003, 312.858], [12, 116.85, 166.45999999999998, 308.49, 316.68], [12, 189.01, 263.63, 309.036, 317.77200000000005], [12, 300.94, 328.82, 310.12800000000004, 320.502], [12, 36.489999999999995, 62.73, 340.158, 351.624], [12, 29.93, 342.34999999999997, 354.90000000000003, 369.64200000000005], [12, 29.93, 157.44, 364.728, 376.74], [12, 29.93, 343.58, 375.10200000000003, 389.298], [12, 29.93, 343.16999999999996, 384.93, 399.12600000000003], [12, 29.93, 339.07, 394.75800000000004, 408.954], [12, 29.93, 99.63, 402.40200000000004, 413.322], [12, 30.749999999999996, 91.83999999999999, 453.72600000000006, 464.646], [12, 220.17, 285.77, 458.09400000000005, 469.014], [12, 223.45, 314.88, 475.02000000000004, 487.03200000000004]]
2026-08-10 19:07:55,896 INFO     29 [qwen-vl-text] ═══ DONE ═══ 102 positions, pages=2, time=39.9s
2026-08-10 19:07:55,896 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:07:55,899 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:07:55,899 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:07:55,899 INFO     29 [qwen-vl-text] positions(32): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:07:55,899 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [31]
2026-08-10 19:07:56,144 INFO     29 [qwen-vl-text] page=13, rect=410x547, img=(1139x1520), dpi=200
2026-08-10 19:07:56,145 INFO     29 [qwen-vl-text] LLM extraction start, text_len=636
2026-08-10 19:07:56,145 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:07:56,146 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 508, \"bbox_end\": 539, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "本报告仅供临床浏览，严禁私自打印。报告单以放射科室打印\n放射科CT报告单\n姓名\n性别 女\n年龄 63岁\n病人编\n检查编号 CT02901334\n门诊号\n检查日期 2026-03-10 09:33 报告日期 2026-03-10 12:07 病人来源 门诊\n检查方法及部位 胸部CT平扫,上腹部CT平扫\n检查所见:\n结合病史，右肺术后，局部见条片状高密度及点线状致密灶，右侧肺门结构\n紊乱，右侧肋骨术后态；右侧胸膜增厚，右膈略抬高。双肺见多发大小不等\n结节灶，部分呈磨玻璃密度，结节较大者位于左肺下叶IM32，为部分实性小\n结节，大小约1.4cm×1.0cm，可见分叶、胸膜凹陷征象；双肺纹理增多、紊\n乱，见纤维灶。左肺段以上支气管开口通畅，左肺门不大，纵隔内见增大淋\n巴结，大者最大短径约1.2cm。未见胸腔积液征象。冠状动脉钙化。双腋窝\n见小淋巴结。\n肝脏形态可，肝实质密度稍低，肝右叶见数个小圆形低密度灶，肝内另见\n斑点状高密度。肝内外胆管无扩张。胆囊不大，壁不厚，内未见高密度灶。\n胰腺未见明显异常。脾脏不大，质均匀。右肾盂肾盏轻度扩张；左肾及左肾\n窦见小类圆形低密度灶。双肾上腺未见明显异常。腹膜后未见肿大淋巴结。\n骨窗示局部腰椎变扁。\n检查结论:\n右肺术后，右肺纤维灶，右侧胸膜增厚\n双肺多发小结节，考虑双肺多发转移可能，较前2025-08-12CT增多、增\n大，请结合临床\n冠状动脉钙化\n提示轻度脂肪肝；肝内钙化灶；肝囊肿\n左肾囊肿；右肾轻度积水\n局部腰椎变扁",
    "role": "user"
  }
]
2026-08-10 19:07:59,971 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:07:59.971+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 88, "failed": 0, "current": {"c552e81694e811f1bd9827cf206dfa2d": {"id": "c552e81694e811f1bd9827cf206dfa2d", "doc_id": "c50f9bd894e811f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-ZPQI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 7054845, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786386288908, "task_type": "dataflow", "root_trace_id": "037d26a7850946e78f8eb13566ae4367", "root_traceparent": "00-037d26a7850946e78f8eb13566ae4367-a439c6e4a17210ed-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "385fbb6494ed11f1bd9827cf206dfa2d": {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:08:06,255 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:08:06,255 INFO     29 [qwen-vl-text] LLM output (len=791):
{
  "exam_date": "2026-03-10",
  "report_date": "2026-03-10",
  "exam_name": "胸部CT平扫,上腹部CT平扫",
  "exam_category": "imaging",
  "body_part": "胸部,上腹部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "门诊",
  "bed_number": null,
  "findings": "结合病史，右肺术后，局部见条片状高密度及点线状致密灶，右侧肺门结构紊乱，右侧肋骨术后态；右侧胸膜增厚，右膈略抬高。双肺见多发大小不等结节灶，部分呈磨玻璃密度，结节较大者位于左肺下叶IM32，为部分实性小结节，大小约1.4cm×1.0cm，可见分叶、胸膜凹陷征象；双肺纹理增多、紊乱，见纤维灶。左肺段以上支气管开口通畅，左肺门不大，纵隔内见增大淋巴结，大者最大短径约1.2cm。未见胸腔积液征象。冠状动脉钙化。双腋窝见小淋巴结。\n肝脏形态可，肝实质密度稍低，肝右叶见数个小圆形低密度灶，肝内另见斑点状高密度。肝内外胆管无扩张。胆囊不大，壁不厚，内未见高密度灶。胰腺未见明显异常。脾脏不大，质均匀。右肾盂肾盏轻度扩张；左肾及左肾窦见小类圆形低密度灶。双肾上腺未见明显异常。腹膜后未见肿大淋巴结。\n骨窗示局部腰椎变扁。",
  "conclusion": "右肺术后，右肺纤维灶，右侧胸膜增厚\n双肺多发小结节，考虑双肺多发转移可能，较前2025-08-12CT增多、增大，请结合临床\n冠状动脉钙化\n提示轻度脂肪肝；肝内钙化灶；肝囊肿\n左肾囊肿；右肾轻度积水\n局部腰椎变扁",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:08:06,264 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4488673, prompt_len=1342
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["本报告仅供临床浏览，严禁私自打印。报告单以放射科室打印", "放射科CT报告单", "姓名", "性别 女", "年龄 63岁", "病人编", "检查编号 CT02901334", "门诊号", "检查日期 2026-03-10 09:33 报告日期 2026-03-10 12:07 病人来源 门诊", "检查方法及部位 胸部CT平扫,上腹部CT平扫", "检查所见:", "结合病史，右肺术后，局部见条片状高密度及点线状致密灶，右侧肺门结构", "紊乱，右侧肋骨术后态；右侧胸膜增厚，右膈略抬高。双肺见多发大小不等", "结节灶，部分呈磨玻璃密度，结节较大者位于左肺下叶IM32，为部分实性小", "结节，大小约1.4cm×1.0cm，可见分叶、胸膜凹陷征象；双肺纹理增多、紊", "乱，见纤维灶。左肺段以上支气管开口通畅，左肺门不大，纵隔内见增大淋", "巴结，大者最大短径约1.2cm。未见胸腔积液征象。冠状动脉钙化。双腋窝", "见小淋巴结。", "肝脏形态可，肝实质密度稍低，肝右叶见数个小圆形低密度灶，肝内另见", "斑点状高密度。肝内外胆管无扩张。胆囊不大，壁不厚，内未见高密度灶。", "胰腺未见明显异常。脾脏不大，质均匀。右肾盂肾盏轻度扩张；左肾及左肾", "窦见小类圆形低密度灶。双肾上腺未见明显异常。腹膜后未见肿大淋巴结。", "骨窗示局部腰椎变扁。", "检查结论:", "右肺术后，右肺纤维灶，右侧胸膜增厚", "双肺多发小结节，考虑双肺多发转移可能，较前2025-08-12CT增多、增", "大，请结合临床", "冠状动脉钙化", "提示轻度脂肪肝；肝内钙化灶；肝囊肿", "左肾囊肿；右肾轻度积水", "局部腰椎变扁"]

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
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord API raw response (len=1973):
[
	{"text": "本报告仅供临床浏览，严禁私自打印。报告单以放射科室打印", "bbox": [134, 0, 728, 20]},
	{"text": "放射科CT报告单", "bbox": [364, 53, 631, 85]},
	{"text": "姓名", "bbox": [55, 104, 102, 122]},
	{"text": "性别 女", "bbox": [371, 107, 420, 124]},
	{"text": "年龄 63岁", "bbox": [683, 108, 833, 127]},
	{"text": "病人编", "bbox": [55, 138, 124, 156]},
	{"text": "检查编号 CT02901334", "bbox": [371, 141, 607, 159]},
	{"text": "门诊号", "bbox": [683, 143, 750, 161]},
	{"text": "检查日期 2026-03-10 09:33 报告日期 2026-03-10 12:07 病人来源 门诊", "bbox": [55, 173, 830, 194]},
	{"text": "检查方法及部位 胸部CT平扫,上腹部CT平扫", "bbox": [78, 267, 696, 293]},
	{"text": "检查所见:", "bbox": [80, 347, 194, 369]},
	{"text": "结合病史，右肺术后，局部见条片状高密度及点线状致密灶，右侧肺门结构", "bbox": [80, 382, 922, 405]},
	{"text": "紊乱，右侧肋骨术后态；右侧胸膜增厚，右膈略抬高。双肺见多发大小不等", "bbox": [80, 407, 922, 430]},
	{"text": "结节灶，部分呈磨玻璃密度，结节较大者位于左肺下叶IM32，为部分实性小", "bbox": [80, 432, 935, 455]},
	{"text": "结节，大小约1.4cm×1.0cm，可见分叶、胸膜凹陷征象；双肺纹理增多、紊", "bbox": [80, 457, 935, 480]},
	{"text": "乱，见纤维灶。左肺段以上支气管开口通畅，左肺门不大，纵隔内见增大淋", "bbox": [80, 482, 922, 505]},
	{"text": "巴结，大者最大短径约1.2cm。未见胸腔积液征象。冠状动脉钙化。双腋窝", "bbox": [80, 507, 919, 529]},
	{"text": "见小淋巴结。", "bbox": [80, 532, 221, 555]},
	{"text": "肝脏形态可，肝实质密度稍低，肝右叶见数个小圆形低密度灶，肝内另见", "bbox": [80, 560, 935, 583]},
	{"text": "斑点状高密度。肝内外胆管无扩张。胆囊不大，壁不厚，内未见高密度灶。", "bbox": [80, 585, 907, 608]},
	{"text": "胰腺未见明显异常。脾脏不大，质均匀。右肾盂肾盏轻度扩张；左肾及左肾", "bbox": [80, 610, 922, 633]},
	{"text": "窦见小类圆形低密度灶。双肾上腺未见明显异常。腹膜后未见肿大淋巴结。", "bbox": [80, 635, 907, 658]},
	{"text": "骨窗示局部腰椎变扁。", "bbox": [80, 660, 325, 683]},
	{"text": "检查结论:", "bbox": [80, 717, 196, 739]},
	{"text": "右肺术后，右肺纤维灶，右侧胸膜增厚", "bbox": [80, 751, 528, 774]},
	{"text": "双肺多发小结节，考虑双肺多发转移可能，较前2025-08-12CT增多、增", "bbox": [80, 775, 893, 798]},
	{"text": "大，请结合临床", "bbox": [80, 800, 266, 823]},
	{"text": "冠状动脉钙化", "bbox": [80, 825, 240, 848]},
	{"text": "提示轻度脂肪肝；肝内钙化灶；肝囊肿", "bbox": [80, 850, 521, 873]},
	{"text": "左肾囊肿；右肾轻度积水", "bbox": [80, 875, 370, 898]},
	{"text": "局部腰椎变扁", "bbox": [80, 900, 240, 923]}
]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=10.3s
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[0]: text=本报告仅供临床浏览，严禁私自打印。报告单以放射科室打印, bbox=[134, 0, 728, 20]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[1]: text=放射科CT报告单, bbox=[364, 53, 631, 85]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[55, 104, 102, 122]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[3]: text=性别 女, bbox=[371, 107, 420, 124]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[4]: text=年龄 63岁, bbox=[683, 108, 833, 127]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[5]: text=病人编, bbox=[55, 138, 124, 156]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[6]: text=检查编号 CT02901334, bbox=[371, 141, 607, 159]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[7]: text=门诊号, bbox=[683, 143, 750, 161]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[8]: text=检查日期 2026-03-10 09:33 报告日期 2026-03-10 12:07 病人来源 门诊, bbox=[55, 173, 830, 194]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[9]: text=检查方法及部位 胸部CT平扫,上腹部CT平扫, bbox=[78, 267, 696, 293]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[10]: text=检查所见:, bbox=[80, 347, 194, 369]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[11]: text=结合病史，右肺术后，局部见条片状高密度及点线状致密灶，右侧肺门结构, bbox=[80, 382, 922, 405]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[12]: text=紊乱，右侧肋骨术后态；右侧胸膜增厚，右膈略抬高。双肺见多发大小不等, bbox=[80, 407, 922, 430]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[13]: text=结节灶，部分呈磨玻璃密度，结节较大者位于左肺下叶IM32，为部分实性小, bbox=[80, 432, 935, 455]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[14]: text=结节，大小约1.4cm×1.0cm，可见分叶、胸膜凹陷征象；双肺纹理增多、紊, bbox=[80, 457, 935, 480]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[15]: text=乱，见纤维灶。左肺段以上支气管开口通畅，左肺门不大，纵隔内见增大淋, bbox=[80, 482, 922, 505]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[16]: text=巴结，大者最大短径约1.2cm。未见胸腔积液征象。冠状动脉钙化。双腋窝, bbox=[80, 507, 919, 529]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[17]: text=见小淋巴结。, bbox=[80, 532, 221, 555]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[18]: text=肝脏形态可，肝实质密度稍低，肝右叶见数个小圆形低密度灶，肝内另见, bbox=[80, 560, 935, 583]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[19]: text=斑点状高密度。肝内外胆管无扩张。胆囊不大，壁不厚，内未见高密度灶。, bbox=[80, 585, 907, 608]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[20]: text=胰腺未见明显异常。脾脏不大，质均匀。右肾盂肾盏轻度扩张；左肾及左肾, bbox=[80, 610, 922, 633]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[21]: text=窦见小类圆形低密度灶。双肾上腺未见明显异常。腹膜后未见肿大淋巴结。, bbox=[80, 635, 907, 658]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[22]: text=骨窗示局部腰椎变扁。, bbox=[80, 660, 325, 683]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[23]: text=检查结论:, bbox=[80, 717, 196, 739]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[24]: text=右肺术后，右肺纤维灶，右侧胸膜增厚, bbox=[80, 751, 528, 774]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[25]: text=双肺多发小结节，考虑双肺多发转移可能，较前2025-08-12CT增多、增, bbox=[80, 775, 893, 798]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[26]: text=大，请结合临床, bbox=[80, 800, 266, 823]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[27]: text=冠状动脉钙化, bbox=[80, 825, 240, 848]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[28]: text=提示轻度脂肪肝；肝内钙化灶；肝囊肿, bbox=[80, 850, 521, 873]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[29]: text=左肾囊肿；右肾轻度积水, bbox=[80, 875, 370, 898]
2026-08-10 19:08:16,595 INFO     29 [qwen-vl-text] coord item[30]: text=局部腰椎变扁, bbox=[80, 900, 240, 923]
2026-08-10 19:08:16,596 INFO     29 [qwen-vl-text] page=13 — 31/31 coords, api_time=10.3s
2026-08-10 19:08:16,596 INFO     29 [qwen-vl-text] new_positions (31):
[[13, 54.94, 298.47999999999996, 0.0, 10.940000000000001], [13, 149.23999999999998, 258.71, 28.991000000000003, 46.495000000000005], [13, 22.549999999999997, 41.82, 56.888000000000005, 66.73400000000001], [13, 152.10999999999999, 172.2, 58.529, 67.828], [13, 280.03, 341.53, 59.07600000000001, 69.46900000000001], [13, 22.549999999999997, 50.839999999999996, 75.486, 85.33200000000001], [13, 152.10999999999999, 248.86999999999998, 77.12700000000001, 86.97300000000001], [13, 280.03, 307.5, 78.221, 88.06700000000001], [13, 22.549999999999997, 340.29999999999995, 94.631, 106.11800000000001], [13, 31.979999999999997, 285.35999999999996, 146.049, 160.27100000000002], [13, 32.8, 79.53999999999999, 189.80900000000003, 201.84300000000002], [13, 32.8, 378.02, 208.954, 221.53500000000003], [13, 32.8, 378.02, 222.62900000000002, 235.21], [13, 32.8, 383.34999999999997, 236.30400000000003, 248.88500000000002], [13, 32.8, 383.34999999999997, 249.979, 262.56], [13, 32.8, 378.02, 263.654, 276.235], [13, 32.8, 376.78999999999996, 277.329, 289.363], [13, 32.8, 90.61, 291.004, 303.58500000000004], [13, 32.8, 383.34999999999997, 306.32000000000005, 318.901], [13, 32.8, 371.87, 319.995, 332.576], [13, 32.8, 378.02, 333.67, 346.25100000000003], [13, 32.8, 371.87, 347.345, 359.92600000000004], [13, 32.8, 133.25, 361.02000000000004, 373.60100000000006], [13, 32.8, 80.36, 392.199, 404.233], [13, 32.8, 216.48, 410.797, 423.37800000000004], [13, 32.8, 366.13, 423.925, 436.50600000000003], [13, 32.8, 109.05999999999999, 437.6, 450.18100000000004], [13, 32.8, 98.39999999999999, 451.27500000000003, 463.85600000000005], [13, 32.8, 213.60999999999999, 464.95000000000005, 477.53100000000006], [13, 32.8, 151.7, 478.62500000000006, 491.206], [13, 32.8, 98.39999999999999, 492.3, 504.88100000000003]]
2026-08-10 19:08:16,596 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=20.7s
2026-08-10 19:08:16,604 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 19:08:16,605 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:ExaminationReport | outputs={"chunks": "4 items, types={'ExaminationReport': 4}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:08:16,605 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 19:08:16,609 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:08:16,609 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:08:17,605 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:08:17,610 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 19:08:17,610 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 19:08:17,610 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 19:08:17,611 INFO     29 [ChunkMerger] Merged 13 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 4, 'Extractor:Progress': 1} (filtered 4 noise chunks)
2026-08-10 19:08:17,619 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 19:08:17,620 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "13 items, types={'LabReport': 3, 'OutpatientRecord': 4, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 4}", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf"}
2026-08-10 19:08:17,620 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 19:08:17,907 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786388550110, 'update_date': datetime.datetime(2026, 8, 10, 19, 2, 30), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1373381, 'status': '1'}
2026-08-10 19:08:18,105 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞  WBC  8.22  10^9/L  3.5-9.5  False    中性粒细胞比率  NEU%  72.10  %  40-75  False    淋巴细胞比率  LYM%  20.30  %  20-50  False    嗜酸性粒细胞比率  EOS%  0.40  %  0.4-8.0  False    嗜碱性粒细胞比率  BAS%  0.40  %  0-1  False    单核细胞比率  MON%  6.80  %  3-10  False    中性粒细胞计数  NEU#  5.93  10^9/L  1.8-6.3  False    淋巴细胞计数  LYM#  1.67  10^9/L  1.1-3.2  False    嗜酸性粒细胞计数  EOS#  0.03  10^9/L  0.02-0.52  False    嗜碱性粒细胞计数  BAS#  0.03  10^9/L  0-0.06  False    单核细胞计数  MON#  0.56  10^9/L  0.1-0.6  False    红细胞  RBC  5.22  10^12/L  3.8-5.1  True    血红蛋白  HGB  147.0  g/L  115-150  False    红细胞压积  HCT  44.90  %  35.0-45.0  False    平均红细胞体积  MCV  86.0  fL  82-100  False    平均血红蛋白含量  MCH  28.2  pg  27-34  False    平均血红蛋白浓度  MCHC  327.0  g/L  316-354  False    红细胞平均宽度  RDW  12.6  %  10-14.6  False    血小板计数  PLT  309  10^9/L  125-350  False    血小板平均宽度  PDW  8.30  fL  9-17  True    平均血小板体积  MPV  8.30  fL  6-14  False    血小板压积  PCT  0.260  %  0.114-0.282  False   
---
   丙氨酸氨基转移酶  ALT  13  U/L  7-40  False    天门冬氨酸氨基转移酶  AST  15  U/L  13-35  False    谷氨酸脱氢酶  GLDH  5.7  U/L  <7.4  False    γ-谷丙酰基转肽酶  GGT  15  U/L  7-45  False    碱性磷酸酶  AKP  93  U/L  50-135  False    腺苷脱氨酶  ADA  8  U/L  4-18  False    总胆红素  TBIL  8.2  μmol/L  5.0-21.0  False    直接胆红素  DBIL  2.6  μmol/L  <6.0  False    间接胆红素  IBIL  5.6  μmol/L  2.0-15.0  False    前白蛋白  PA  30.2  mg/dl  17.0-40.0  False    总蛋白  TP  75.4  g/L  60.0-85.0  False    白蛋白  ALB  48.6  g/L  40.0-55.0  False    球蛋白  GLB  26.8  g/L  20.0-40.0  False    白/球比例  A/G  1.81  None  1.2-2.4  False    总胆汁酸  TBA  1.3  μmol/L  <15.0  False    总胆固醇  Cho  7.28  mmol/L  2.80-6.00  True    高密度脂蛋白胆固醇  HDL-C  1.78  mmol/L  0.80-2.00  False    低密度脂蛋白胆固醇  LDL-C  4.89  mmol/L  1.00-3.37  True    小而密低密度脂蛋白  sdLDL  2.01  mmol/L  0.25-1.17  True    血清载脂蛋白A1  APOA1  1.96  g/L  1.00-1.60  True    血清载脂蛋白B  APOB  1.53  g/L  0.60-1.00  True    甘油三酯  TG  2.30  mmol/L  0.30-1.70  True    脂蛋白a  LP(a)  9.70  nmol/L  <75.00  False    游离脂肪酸  NEFA  125.0  umol/dl  10.0-85.0  True    脂蛋白磷脂酶A2  PLA2  728  U/L  <659  True    尿素  Urea  3.59  mmol/L  2.30-7.80  False    肌酐  Cr  38  μmol/L  53-97  True    胱抑素C  Cys-C  0.76  mg/L  0.51-1.09  False    肾小球滤过率  eGFR  108.600  ml/min  None  False    钾  K  4.23  mmol/L  3.50-5.30  False    钠  NA  139  mmol/L  137-147  False    氯  CL  104  mmol/L  99-110  False    二氧化碳结合力  CO2  21.5  mmol/L  18.0-28.0  False    钙  Ca  2.36  mmol/L  2.11-2.52  False    磷  P  1.21  mmol/L  0.60-1.60  False    镁  Mg  0.86  mmol/L  0.65-1.10  False   
---
   甲胎蛋白  AFP  3.41  ng/ml  0.00-7.00  False    癌胚抗原  CEA  3.52  ng/ml  0.00-5.00  False    非小细胞肺癌相关抗原  CYFRA21-1  1.70  ng/ml  0.00-3.30  False    神经元特异性烯醇化酶  NSE  16.60  ng/ml  0.00-16.30  True   
---
门诊病历
初诊
复诊
门诊号
就诊
姓名
性别：女
年龄：60岁
身份
职业：农民
就诊时间：2024-03-01 08:13:19
联系人
联系电话
现住址
T:
℃
P:
次/分
R:
次/分
BP:
/
mmHg
处方
检查
检验
医疗医嘱
主诉：
肺Ca术后3年余，肺结节？
现病史：
3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）
20-ins突变阳性。
2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双
肺多发小结节，较前变化不著，请结合临床、随诊复查。
既往史：
否认其他病史。
家族史：
否认家族史。
过敏史：
体征：
辅助检查：
2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小
结节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于
左肺下叶外基底段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03
提示浸润性腺癌，大小3*2.5cm，查见淋巴结转移癌
初步诊断：
肺癌
修正诊断：
肺癌术后肺结节
处方：
检查：
检验：
医疗医嘱：
其他建议：
建议3月后复查
已告知患者病情及可能的药物不良反应。
医生签
---
门诊病历
性别：女
年龄：61岁
民族：汉族
婚姻：已婚
职业：农民
证件类型：居民身份证
证件号码
门诊编号
就诊医院
就诊科室：
就诊日期：2024-08-13 08:50:41
初诊/复诊：初诊  复诊
陪检者姓名：
陪检者与患者的关系：
联系电话
处方
检查
检验
医疗医嘱
主诉：肺Ca术后3年余，肺结节？
现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-
ins突变阳性。
2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结
节，较前变化不著，请结合临床、随诊复查。
既往史：否认其他病史。
家族史：否认家族史
过敏史：无
体温（℃）
脉博（次/分）
收缩压（mmHg）
舒张压（mmHg）
呼吸（次/分）
意识状态  清醒
主要症状和体征：
体格检查：
辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结
节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底
段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小
3*2.5cm，查见淋巴结转移癌
初步诊断：肺癌
修正诊断：肺癌术后
处
方：
检
验：
门诊检验申请单（生化检验申请单），项目为：血生化 肝功 血脂（生化室）肾功（生
化）
门诊检验申请单（门诊检验申请单），项目为：血细胞分析五分类（静脉）（门化）
门诊检验申请单（中心检验申请单），项目为：AFP-甲胎蛋白 CEA-癌胚抗原 NSE-神经
元特异性烯化醇酶 非小细胞癌相关抗原（中心）
检
查：
门诊检查申请单（CT检查申请单（新）），项目为：胸部CT平扫
医疗医嘱：
其他建议：
---
门诊病历
性别：女
证件类型：居民身份证
年龄：62岁
证件
民族：汉族
门诊编
婚姻：已婚
就诊医院
职业：农民
就诊科室
就诊日期：2025-08-12 08:11:41
陪检者姓名：
初诊/复诊：初诊□复诊
陪检者与患者的关系：
联系电话
处方
检查
检验
医疗医嘱
主诉：肺Ca术后3年余，肺结节？
现病史：3年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-
ins突变阳性。
2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结
节，较前变化不著，请结合临床、随诊复查。
既往史：否认其他病史。
家族史：否认家族史
过敏史：无
体温（℃）
脉搏（次/分）
收缩压（mmHg）
舒张压（mmHg）
呼吸（次/分）
意识状态 清醒
主要症状和体征：
体格检查：
辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结
节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底
段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小
3*2.5cm，查见淋巴结转移癌
初步诊断：肺癌
修正诊断：肺癌术后
处
方：
检
验：
检
查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫
医疗医嘱：
其他建议：
---
门诊病历
性别：女
年龄：63岁
民族：汉族
婚姻：已婚
职业：农民
证件类型：居民身份证
证件号
门诊编
就诊医院
就诊科室
就诊日期：2026-03-10 08:35:11
初诊/复诊：初诊 □ 复诊
联系电
陪伴者姓名：
陪伴者与患者的关系：
处方
检查
检验
医疗医嘱
主诉：肺Ca术后4年余，肺结节？
现病史：4年前于我院行肺腺Ca切除术，术后行4次辅助化疗，EGFR突变 Exon-20（外显子）20-
ins突变阳性。
2024.2.28CT：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-12-25 CT变化不著双肺多发小结
节，较前变化不著，请结合临床、随诊复查。
2025.8.11CT：双肺多发小结节，较大者位于左肺外周，均较前片变化不著
既往史：否认其他病史。
家族史：否认家族史
过敏史：无
体温（℃）
脉搏（次/分）
收缩压（mmHg）
舒张压（mmHg）
呼吸（次/分）
意识状态 清醒
主要症状和体征：
体格检查：
辅助检查：2023-03-29胸部CT：右肺术后CT表现，较2022-06-01 前片变化不大，双肺多发小结
节（双肺见多发小结节，长径范围约3-6mm，较大者大小约6mm×4mm，边界清晰，位于左肺下叶外基底
段IM37），对比2022-06-01 前片增多，建议随诊，肝囊肿。2020-09-03提示浸润性腺癌，大小
3*2.5cm，查见淋巴结转移癌
初步诊断：肺癌,肺结节
修正诊断：肺癌,肺结节
处方：
检验：门诊检验申请单(临床生化检验一(临床生化检验))，项目为：血糖 糖化血红蛋白测定
检查：门诊检查申请单(CT检查申请单)，项目为：上腹部CT平扫
医疗医嘱：
其他建议：
已告知患者病情及可能的药物不良反应。
医生
---
出院记录
入院日期：2024年1月17日10点52分
性别：女
出院日期：2024年1月20日07点00分
年龄：60岁
住院天数：3天
入院情况：1. 患者老年女性因“肺腺癌5周期化疗后2年进展后化疗5周期后
”入院治疗。2. 体格检查：双肺呼吸音清，未闻及干湿性啰音，未闻及胸膜摩擦
音。心律齐，未闻及明显杂音，无心包摩擦音。腹部平坦，无腹壁静脉曲张。全
腹柔软，无包块；脾肋下未触及。
入院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo
n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨
髓抑制
诊疗经过：入院后完善各项相关检查，排除禁忌于2024.1.19给予培美曲塞
二钠800mg+卡铂400mg，耐受可。
出院诊断：1. 右肺上叶浸润性腺癌术后（T1bN2M0, IIIA期 EGFR突变：Exo
n-20（外显子） 20-ins突变阳性） 2. 右肾结石 3. 子宫切除术后 4. 化疗后骨
髓抑制
出院情况：一般状况可。
出院医嘱：出院后注意休息，加强营养，避免感染；定期复查血常规，每周
1-2次，发热、腹泻随时查，必要时给予升白等对症治疗；2024.2.9返院继续
治疗；不适务必及时随诊。
医师签名：
签字时间：2024年1月20日07点00分
第1页
---
姓名
现住址
性别：女
职业：农民
年龄：60岁
入院时间：2024年01月17日10点52分
民族：汉族
记录时间：2024年01月17日16点00分
婚姻：已婚
病史陈述者
陈述者与患者关系：本人
陈述者内容可靠标志：可靠
主诉：肺腺癌5周期化疗后2年进展后化疗5周期后。
现病史：患者2020.8月体检时行胸部CT检查提示右肺上叶片状影，无咳嗽、咳痰、
咯血、痰中带血及胸痛、发热、盗汗等不适，遂就诊于当地医院给予“左氧氟沙星、
法罗培南”等药物抗感染治疗，复查胸部CT提示吸收欠佳。患者为求进一步诊治就诊
于我院，行胸部CT检查考虑右肺上叶浸润性肺腺Ca，在排除相关禁忌并取得患者家属
知情同意后，行经皮肺穿刺活检，病理结果示：（右肺上叶）穿刺肺组织呈显著慢性
炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变
炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1(+)，CK7(+)，Ki-67阳性
率10%。为排查肿瘤全身转移情况行骨ECT及腹部强化CT检查未见明显转移征象，行颅
脑MRI提示右颞枕叶、左侧小脑下蚓部异常信号，结合肿瘤病史，建议增强扫描除外
转移，为排除颅脑转移，进一步行颅脑强化MRI提示右侧颞枕叶脑沟内条片状轻度强
化，考虑软脑膜增厚强化，结合肺Ca病史，脑膜转移不除外，建议脑脊液检查。脑脊
液检查未见肿瘤细胞。在取得外科会诊意见明确患者具有手术指征后，患者于2020-0
8-31于胸外科行右肺上叶切除并肺部、纵膈淋巴结清扫术，术后病理示：（右肺上叶
）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体呈周围型，
肿物切面面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；
肺组织内查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚
查见转移癌（1/3）。另送第11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔
淋巴结4枚，其中2枚查见转移癌（2/4）。另送第7组淋巴结9枚（0/9）、第9组淋巴结
1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。术后行EGFR等十基因检测
（石蜡包埋组织）示EFGR基因 Exon-20（外显子） 20-ins突变阳性。后患者为行
进一步治疗就诊我科，告知患者其Exon-20突变不适合靶向药物治疗，建议行化疗治
疗，在排除相关禁忌并取得患者及家属知情同意后，于2020-10-16、2020-11-10、
2020-12-04、2020-12-26、2021-1-18行“培美曲塞二钠0.8g d1+卡铂400mg d1
”方案化疗5周期，患者耐受可。2023.9.21、2023.10.13、2023.11.8、2023.12
.4、2023.12.26排除禁忌给予卡铂+培美曲塞二钠联合贝伐珠单抗治疗5周期，耐受
可。2023.11.07复查CT示：右肺术后，右肺纤维灶，右侧胸膜增厚，较2023-09-19
CT变化不著；双肺多发小结节，较前变化不著，请结合临床、随诊复查；提示轻度脂
肪肝；肝内钙化灶；肝囊肿；左肾囊肿、左肾盂旁囊肿；右肾小结石、右肾轻度积水
；右侧附件区囊性低密度，请结合临床及妇科超声；左侧耻骨高密度，较前变化不著
第1页
入院记录
姓名
住院号
。患者治疗后出现发热，体温38.7°C，化验示白细胞2.05*109/L，中性粒细胞0.7
5*109/L，给予升白对症处理。患者自上次出院后，饮食、睡眠可，大小便未见明显
异常，体重无明显改变。
既往史：既往身体健康，否认高血压，否认糖尿病，否认冠心病，否认结核等传染病
史及密切接触史，否认外伤史，否认手术史，否认输血史，预防接种史：随当地，过
敏史：食物过敏史：无，药物过敏史：无。
个人史：生于原籍，无外地久居史，无疫区到访及停留史，无工业毒物、粉尘、放射
性物质接触史，吸烟史：无，饮酒史：无。
月经史：已绝经。
婚育史：已婚，已育。
家族史：否认家族遗传病史。
体格检查
T:36℃ P:97次/分 R:23次/分 血压：154/94mmHg 体重：72kg 身高：16
0cm NRS：0
一般情况：老年女性，神志清晰，精神好，发育正常，营养良好，自主体位，查体合作
。
皮肤、粘膜：颜色红润，无皮肤黄疸，无明显皮肤红肿硬肿，无凹陷性水肿，无皮疹
，未见出血点，未见瘀斑。皮肤弹性好。无肿大淋巴结。
头部及其器官：头颅无畸形；双眼无畸形，双侧瞳孔等大，对光反射存在；双耳无畸
形；鼻无畸形。口唇红润，无唇裂，咽无充血。
颈部：无抵抗感，气管居中，胸锁乳突肌包块：无。甲状腺正常，无颈部淋巴结肿大
。
胸部：双侧对称，无畸形；双肩等高，呼吸动度双侧一致，三凹征阴性。肺呼吸音：
清，未闻及干湿性啰音，未闻及胸膜摩擦音。
心脏：心前区无隆起，心尖搏动位于左侧锁骨中线第5肋间，心音有力，心律齐，未
闻及明显杂音，无心包摩擦音。
腹部：腹部平坦，无腹壁静脉曲张。全腹柔软，无包块；脾肋下未触及。腹部叩诊呈
鼓音；肠鸣音正常，4次/分。
肛门外生殖器：肛门位置正常。外阴外观无畸形。
脊柱：脊柱生理曲度正常。
四肢：四肢肌力正常，肌张力正常。
神经系统：双侧腱反射正常，脑膜刺激征阴性，双侧病理征阴性。
专科情况
无。
入院记录
辅助检查
日期
项目
结果
2020-07-29
胸部CT
考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检，双肺间质性改变，右肾结石
2020-08-10
肺功能
肺通气功能正常
2020-08-10
胸部强化CT
考虑右肺上叶浸润性肺腺Ca，请结合临床并建议穿刺活检；右肺门淋巴结肿大；双肺纤维灶；肝囊肿；右肾结石
2020-08-10
肺组织活检
（右肺上叶）穿刺肺组织呈显著慢性炎伴纤维组织增生，肺泡上皮显著增生，并轻-中度异型，较符合原位腺癌改变，病变炎症反应较重，须完整切除后明确诊断。免疫组化：TTF-1 (+), CK7(+), Ki-67阳性率10%
2020-08-14
骨扫描
1.右肺坐骨支局限性骨质代谢增高观察；2.L5山医
2020-08-16
颅脑MR强化
强化后FLAIR显示右侧颞枕叶脑沟内条片状轻度山医
2020-08-31
肺组织术后病理
（右肺上叶）浸润性腺癌，腺泡型（60%），乳山医
2020-09-23
基因检测
EGFR等十基因检测（石蜡包埋组织）：EFGR基山医
2022-06-01
胸部CT平扫
右肺术后CT表现，请结合临床；双肺纤维灶左山医
2023-03-29
胸部CT平扫
右肺术后CT表现，较2022-06-01 前片变化不大；双肺多发小结节，对比2022-06-01 前片
2023-09-13
CT平扫
双侧基底节区少许缺血变性灶，必要时结合MRI
第 3 页
入院记录
住
2023-11-07
强化CT
右肺术后，右肺纤维灶，右侧胸膜增厚，较
2023-09-19 CT变化不著；双肺多发小结节，
较前变化不著，请结合临床、随诊复查；提示
轻度脂肪肝；肝内钙化灶；肝囊肿；左肾囊
肿、左肾盂旁囊肿；右肾小结石、右肾轻度积
水；右侧附件区囊性低密度，请结合临床及妇
科超声；左侧耻骨高密度，较前变化不著
初步诊断：
1. 右肺上叶浸润性腺癌术后（T1bN2M0, I
IIA期 EGFR突变：Exon-20（外显子） 20-i
ns突变阳性）
2. 右肾结石
3. 子宫切除术后
4. 化疗后骨髓抑制
记录者：
项目内容
患方签名
以上所记录内容属实
签字时间
年 月 日 时 分
X光号：
---
病理检查报告单
检查号
住院号
姓名
性别:女
结论: (右肺上叶)形态符合腺癌,待常规病理免疫组化确诊。
此报告尚未打印
当前报告状态: 已打印
江苏省捷达科技发展有限公司 版权所有 © 2015
Copyright 2007-2015 JEDA all rights reserved
---
病理检查报告单
检查号
住院号
门诊号:
姓名
性别:女
年龄:57岁
结合202036909（右肺上叶）浸润性腺癌，腺泡型（60%），乳头型（20%），附壁型（20%），大体
呈周围型，肿物切面积3*2.5cm，未侵及脏层胸膜；未查见脉管内癌栓；支气管断端未查见癌；肺组织内
结论:查见淋巴结1枚，其内查见转移癌（1/1）。支气管周围淋巴结3枚，其中1枚查见转移癌（1/3）。另送第
11组淋巴结5枚，其中2枚查见转移癌（2/5）；上纵隔淋巴结4枚，其中2枚查见转移癌(2/4)。另送第7组
淋巴结9枚（0/9）、第9组淋巴结1枚（0/1）、第10组淋巴结5枚（0/5）未查见转移癌。
此报告尚未打印
当前报告状态:已打印
---
分子病理基因检测报告单
样本信息
项目编号：PCR20-1135
姓名
性别：女
年龄：57岁
住院号
病理号
送检医生
标本类别：石蜡包埋组织
送检科室
送检时间：2020-09-23
送检医院：本院
联系电话
检测方法：ARMS PCR
检测位点：
检查项目：九基因
检测结果
检测项目
外显因子
突变类型
检测结果
EGFR基因
Exon19
19-del
野生型
Exon21
L858R
野生型
Exon20
T790M
野生型
Exon18
G719X
野生型
Exon20
S768I
野生型
Exon21
L861Q
野生型
Exon20
20-ins
突变型
KRAS基因
Exon-2
G12D/S
野生型
G12A/V/R/C、G13C
野生型
BRAF基因
Exon-15
V600E/K/R/D
野生型
NRAS基因
Exon-3
Q61R/K/L/H
野生型
初诊医师：戚美
复诊医师：刘龙
报告日期：2020-09-23
分子病理基因检测报告单
检测项目
外显因子
突变类型
检测结果
PIK3CA基因
Exon-20
H1047R
野生型
Exon-9
E545K
ALK融合基因
ALK-Exon-20
具体突变类型见附录
野生型
ROS1融合基因
ROS1-Exon-32/34/35
具体突变类型见附录
野生型
RET融合基因
RET-Exon-12
具体突变类型见附录
野生型
HER2基因
Exon-20
20-ins/G776>VC(1)
野生型
MET基因
MET-Exon-14
MET exon13;METexon15
野生型
备注：
由于肿瘤存在异质性现象，此检测结果只针对本次样本有效。结果仅供临床参考
，不可作为临床诊治的唯一依据。
驱动基因突变状态是靶向药物治疗的重要疗效预测因子，EGFR和KRAS突变状态可
以指导EGFR-TKIs的用药；ALK、ROS1基因融合突变及MET外显子14跳跃突变可以
从ALK/ROS1/MET抑制剂中明显受益；BRAF基因突变患者可以从RAF抑制剂和MEK
抑制剂中明显受益
初诊医师：戚美
复诊医师：刘龙
报告日期：2020-09-23
---
本报告仅供临床浏览，严禁私自打印。报告单以放射科室打印
放射科CT报告单
姓名
性别 女
年龄 63岁
病人编
检查编号 CT02901334
门诊号
检查日期 2026-03-10 09:33 报告日期 2026-03-10 12:07 病人来源 门诊
检查方法及部位 胸部CT平扫,上腹部CT平扫
检查所见:
结合病史，右肺术后，局部见条片状高密度及点线状致密灶，右侧肺门结构
紊乱，右侧肋骨术后态；右侧胸膜增厚，右膈略抬高。双肺见多发大小不等
结节灶，部分呈磨玻璃密度，结节较大者位于左肺下叶IM32，为部分实性小
结节，大小约1.4cm×1.0cm，可见分叶、胸膜凹陷征象；双肺纹理增多、紊
乱，见纤维灶。左肺段以上支气管开口通畅，左肺门不大，纵隔内见增大淋
巴结，大者最大短径约1.2cm。未见胸腔积液征象。冠状动脉钙化。双腋窝
见小淋巴结。
肝脏形态可，肝实质密度稍低，肝右叶见数个小圆形低密度灶，肝内另见
斑点状高密度。肝内外胆管无扩张。胆囊不大，壁不厚，内未见高密度灶。
胰腺未见明显异常。脾脏不大，质均匀。右肾盂肾盏轻度扩张；左肾及左肾
窦见小类圆形低密度灶。双肾上腺未见明显异常。腹膜后未见肿大淋巴结。
骨窗示局部腰椎变扁。
检查结论:
右肺术后，右肺纤维灶，右侧胸膜增厚
双肺多发小结节，考虑双肺多发转移可能，较前2025-08-12CT增多、增
大，请结合临床
冠状动脉钙化
提示轻度脂肪肝；肝内钙化灶；肝囊肿
左肾囊肿；右肾轻度积水
局部腰椎变扁
2026-08-10 19:08:18,914 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 19:08:18,914 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "13 items, types={'LabReport': 3, 'OutpatientRecord': 4, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 4}", "name": "12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf", "embedding_token_consumption": 8548}
2026-08-10 19:08:18,914 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 19:08:19,169 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 19:08:19,169 INFO     29 [Trace] task=385fbb64 | doc=12-山肿-KFXI，后线肺癌，方穹招募推荐.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":13,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 19:08:19,176 INFO     29 [DIAG-EXECUTOR] row_position_int len=22 row[0]=(15, 16, 48, 65, 73) row[-1]=(15, 16, 53, 338, 346)
2026-08-10 19:08:19,176 INFO     29 [DIAG-EXECUTOR] row_position_int len=36 row[0]=(16, 23, 88, 62, 70) row[-1]=(16, 23, 33, 379, 387)
2026-08-10 19:08:19,176 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(17, 25, 61, 50, 58) row[-1]=(17, 22, 93, 78, 86)
2026-08-10 19:08:19,176 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,176 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,177 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,177 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,177 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,177 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,177 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,177 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,178 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,178 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:08:19,182 INFO     29 set_progress(385fbb6494ed11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 19:08:19 [DOC Engine]:
Start to index...
2026-08-10 19:08:19,197 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:08:19,201 INFO     29 set_progress(385fbb6494ed11f1bd9827cf206dfa2d), progress: 0.8076923076923077, progress_msg: 
2026-08-10 19:08:19,215 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:08:19,243 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 19:08:19,251 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.005s]
2026-08-10 19:08:19,256 INFO     29 set_progress(385fbb6494ed11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 19:08:19 Indexing done (0.07s). Task done (647.70s)
2026-08-10 19:08:19,259 INFO     29 [Done], chunks(13), token(8548), elapsed:647.70
2026-08-10 19:08:19,454 INFO     29 handle_task done for task {"id": "385fbb6494ed11f1bd9827cf206dfa2d", "doc_id": "37bdfdce94ed11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-KFXI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 38399969, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786388199918, "task_type": "dataflow", "root_trace_id": "8f93d2005da541248b89bfa311e65e68", "root_traceparent": "00-8f93d2005da541248b89bfa311e65e68-2a26d8dbc44f622b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
