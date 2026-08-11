# 基准结果：YXLA（支气管哮喘）222.pdf

## 基本信息

- 文件：`YXLA（支气管哮喘）222.pdf`
- 大小：20976.6 KB
- PDF 总页数：19
- doc_id：`b37cdb2a94b511f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T20:19:12  完成时间：2026-08-10T20:31:51  耗时：758.9s
- progress_msg：`12:31:47 Indexing done (0.08s). Task done (719.71s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 78446c5d | 1 | 1-1 | 人民医院 H43120200207, 院区: 舊城院区) 基本就诊信息 姓名:  |
| 2 | dc94e0ac | 1 | 2-2 | 基本就诊信息 姓名：杨 医生： 挂号单：26000068319 医保号：5200 |
| 3 | 6247a644 | 2 | 3-4 | 报告时间: 2025-02-24 怀化市肿瘤医院 怀化市第二人民医院 鹤城院区  |
| 4 | 919acb97 | 1 | 5-5 | 怀化市中心医院 HUAIHUA CENTRAL HOSPITAL 怀化市肿瘤医院 |
| 5 | ecc922de | 2 | 6-7 | HUAIHUA CENTRAL HOSPITAL 怀化市肿瘤医院 姓名： 性别： |
| 6 | 58f22740 | 2 | 7-8 | 37岁 科室：呼吸与危重症医学科 床号：42 住院号： 出院记录 入院时间：20 |
| 7 | dd0b5a91 | 3 | 9-11 | 221028180 第2次入院记录 姓名： 性别：女 年龄：37岁 婚姻：已婚  |
| 8 | 5a453220 | 2 | 12-13 | 221028180 第2次入院记录 姓名： 出生地：贵州省天柱县 性别：女 民族 |
| 9 | 9c277292 | 1 | 14-14 | 姓名： 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：  |
| 10 | 4e62d2e1 | 1 | 15-15 | 姓名： 年龄：38岁 性别：女 科别： 保险： 预计值模式：Standard-n |
| 11 | e5dc303b | 2 | 15-16 | CS 扫描全能王 3亿人都在用的扫描App 呼出气一氧化氮检测报告单 姓名：杨  |
| 12 | 1c352643 | 1 | 17-17 | 一口气法弥散功能报告 姓名： 年龄：38岁 性别：女 科别： 保险： 预计值模式 |
| 13 | b097db9b | 1 | 18-18 | 肺功能试验报告 姓名： 年龄：38岁 性别：女 科别： 保险： 预计值模式：St |
| 14 | 7025082a | 1 | 19-19 | 金城大药房 会员号: 积分:112550 本次积分:596.00 名称 规格 数 |

- chunks 总数：14
- 各 chunk 页数合计（含跨页重复）：21
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`
- 覆盖页数：19 / 19；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 3 | 3 | 3 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 2 | 2 | 2 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 1 | 1 | 1 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 2 | 2 | 2 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 6 | 6 | 6 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"PrescriptionRecord": 2, "ExaminationReport": 6, "DischargeRecord": 2, "AdmissionRecord": 3, "MedicationRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 14, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 2, "Extractor:Discharge": 2, "Extractor:Admission": 3, "Extractor:ExaminationReport": 6, "Extractor:Progress": 1}, "filtered_noise": 4}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 12:31:45,630 INFO     29 [ChunkMerger] Merged 14 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 12:19:17,689 INFO     29 handle_task begin for task {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 12:19:17,892 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 12:19:18,009 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 12:19:18,032 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:19:18,032 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 12:19:18,032 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 12:19:18,040 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 12:19:18,040 INFO     29 ============================================================
2026-08-10 12:19:18,040 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 12:19:18,040 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 12:19:18,040 INFO     29 ============================================================
2026-08-10 12:19:18,040 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 12:19:18,040 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 12:19:18,043 INFO     29 No torch found.
2026-08-10 12:19:20,200 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=19
2026-08-10 12:19:20,335 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=866058, prompt_len=764
2026-08-10 12:19:21,891 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-30"}
```
2026-08-10 12:19:21,892 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-09-30
2026-08-10 12:19:21,898 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=866058, prompt_len=401
2026-08-10 12:19:24,156 INFO     29 [qwen-vl-parser] text API response (len=349):
["人民医院", "H43120200207, 院区: 舊城院区)", "基本就诊信息", "姓名: 核", "医生: 旅", "挂号单: 25000448502", "医保号: 5200002600000000600637839", "付款: 城乡居民基本医疗 费别: 普通", "门诊号: 2502240221", "社区号:", "门诊就诊:呼吸内科门诊,2025-09-30 14:50", "医嘱", "报告", "已作废", "全部", "处方", "其他", "生效时间", "内容", "用法", "2025-09-30", "孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/", "睡前口服,每天一次,共30天", "14:51", "盒,共10盒,每次10mg", ""]
2026-08-10 12:19:24,157 INFO     29 [qwen-vl-parser] page=1 text: 25 lines (bbox 0-24)
2026-08-10 12:19:24,157 INFO     29 [qwen-vl-parser] page=1 text: 25 sections
2026-08-10 12:19:24,305 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=951375, prompt_len=764
2026-08-10 12:19:25,738 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-09"}
```
2026-08-10 12:19:25,738 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2026-02-09
2026-08-10 12:19:25,752 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=951375, prompt_len=401
2026-08-10 12:19:26,616 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:19:26.614+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:19:28,634 INFO     29 [qwen-vl-parser] text API response (len=474):
["基本就诊信息", "姓名：杨", "医生：", "挂号单：26000068319", "医保号：52000026000000006006378395", "付款：城乡居民基本医疗 费别：普通", "门诊号：2502240221", "社区号：", "门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04", "医嘱|报告|", "已作废|全部|处方|其他", "生效时间", "内容", "用法", "2026-02-09", "肺功能全套+支气管舒张试验,共1次", "", "2026-02-09", "(基)硫酸沙丁胺醇吸入气雾剂 (山东)", "吸入,一次,共1天", "11:08", "100ug*200揿/瓶,共1瓶,每次400ug", "", "2026-02-09", "呼出气一氧化氮测定,共1次", "", "2026-02-09", "沙美特罗替卡松粉吸入剂(法国GLAXO)", "吸入,每天二次,共1天", "12.33", "50ug/500ug*60吸/瓶,共1瓶,每次50ug", ""]
2026-08-10 12:19:28,635 INFO     29 [qwen-vl-parser] page=2 text: 28 lines (bbox 25-52)
2026-08-10 12:19:28,635 INFO     29 [qwen-vl-parser] page=2 text: 28 sections
2026-08-10 12:19:28,843 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1648211, prompt_len=764
2026-08-10 12:19:30,345 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2025-02-24"}
```
2026-08-10 12:19:30,346 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2025-02-24
2026-08-10 12:19:30,365 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1648211, prompt_len=756
2026-08-10 12:19:57,856 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:19:57.854+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:20:29,097 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:20:29.096+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:21:00,466 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:21:00.465+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:21:31,730 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:21:31.730+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:21:39,945 INFO     29 [qwen-vl-parser] table API response (len=16394):
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c
2026-08-10 12:21:39,948 INFO     29 [qwen-vl-parser] page=3 table: 2 LaTeX lines (bbox 53-54)
2026-08-10 12:21:39,948 INFO     29 [qwen-vl-parser] page=3 table: 2 sections
2026-08-10 12:21:40,047 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=713058, prompt_len=764
2026-08-10 12:21:41,447 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-02-25"}
```
2026-08-10 12:21:41,447 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-02-25
2026-08-10 12:21:41,459 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=713058, prompt_len=401
2026-08-10 12:21:44,135 INFO     29 [qwen-vl-parser] text API response (len=438):
["怀化市肿瘤医院", "怀化市第二人民医院", "鹤城院区", "湖南HR", "CT影像诊断报告单", "ID: 86562633", "检查号: CT00525514", "姓名:", "性别: 女", "年龄: 37岁", "住院号: 220999152", "床号: 46", "申请科室: 呼吸与危重症医学科", "申请医生: 易莹", "检查日期: 2025.02.25", "报告日期: 2025.02.25 09:45:16", "检查项目: CT成套:胸部(平扫(三维重建))", "检查所见:", "右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见", "条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主", "要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "意见:", "1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。", "2. 右肺中叶少许慢性炎症。"]
2026-08-10 12:21:44,135 INFO     29 [qwen-vl-parser] page=4 text: 24 lines (bbox 55-78)
2026-08-10 12:21:44,135 INFO     29 [qwen-vl-parser] page=4 text: 24 sections
2026-08-10 12:21:44,245 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=747519, prompt_len=764
2026-08-10 12:21:45,681 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-07-11"}
```
2026-08-10 12:21:45,682 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2025-07-11
2026-08-10 12:21:45,694 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=747519, prompt_len=401
2026-08-10 12:21:49,914 INFO     29 [qwen-vl-parser] text API response (len=503):
["怀化市中心医院", "HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "湖南HR", "CT影像诊断报告单", "ID: 93717786", "检查号: CT00568277", "姓名:", "性别: 女", "年龄: 37岁", "住院号: 221028180", "床号: 42", "申请科室: 呼吸与危重症医学科", "申请医生:", "检查日期: 2025.07.11", "报告日期: 2025.07.11 16:08:56", "检查项目: CT成套胸部平扫(三维重建)", "检查所见:", "与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。", "右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部", "分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "意见:", "1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。", "2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。"]
2026-08-10 12:21:49,914 INFO     29 [qwen-vl-parser] page=5 text: 24 lines (bbox 79-102)
2026-08-10 12:21:49,914 INFO     29 [qwen-vl-parser] page=5 text: 24 sections
2026-08-10 12:21:50,086 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1489979, prompt_len=764
2026-08-10 12:21:51,414 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:21:51,415 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 12:21:51,429 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1489979, prompt_len=401
2026-08-10 12:21:58,283 INFO     29 [qwen-vl-parser] text API response (len=1206):
["HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "221028180", "3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总", "神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓", "浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经", "(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞", "<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌", "(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支", "持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司", "特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前", "好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。", "出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发", "热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，", "BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。", "心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧", "段结节（LU-RADS 2类）。", "出院医嘱：", "1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生", "活习惯，增强体质，适当运动，加强营养；", "2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复", "查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；", "3.出院后继续服用中药。", "4.出院带药：", "舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱", "口，根据动态复查肺功能结果，调整用药）", "祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次", "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次", "5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；", "6.如有不适，随时医院就诊，我科随诊。", "科室护士办公室电话：0745-2329117。主管医师电话：13789357317", "医师签名：主治医师", ""]
2026-08-10 12:21:58,284 INFO     29 [qwen-vl-parser] page=6 text: 35 lines (bbox 103-137)
2026-08-10 12:21:58,284 INFO     29 [qwen-vl-parser] page=6 text: 35 sections
2026-08-10 12:21:58,476 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1724875, prompt_len=764
2026-08-10 12:21:59,921 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:21:59,922 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 12:21:59,930 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1724875, prompt_len=401
2026-08-10 12:22:02,972 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:22:02.969+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:22:08,891 INFO     29 [qwen-vl-parser] text API response (len=1523):
["zz1028180", "37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "出院记录", "入院时间：2025-07-11 08:57", "出院时间：2025-07-22 15:00", "住院天数：11天", "记录时间：2025-07-21 16:14", "入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；", "4.腹胀查因：功能性消化不良？反流性食管炎？其他。", "入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T", "36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面", "容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及", "少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，", "无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，", "LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功", "能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散", "功能在正常范围；肺总量在正常范围，残气量、残总比增高。", "诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分", "压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中", "性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；", "尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红", "细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；", "电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C", "蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链", "DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生", "虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：", "胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.", "支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气", "功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、", "MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重", "减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳", "性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，", "绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），", "2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO："]
2026-08-10 12:22:08,892 INFO     29 [qwen-vl-parser] page=7 text: 34 lines (bbox 138-171)
2026-08-10 12:22:08,892 INFO     29 [qwen-vl-parser] page=7 text: 34 sections
2026-08-10 12:22:09,022 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=959069, prompt_len=764
2026-08-10 12:22:10,322 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:22:10,323 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 12:22:10,328 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=959069, prompt_len=401
2026-08-10 12:22:14,195 INFO     29 [qwen-vl-parser] text API response (len=647):
["怀化市中心医院", "HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "221028180", "[心前区无隆起]，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，", "[各瓣膜听诊区未闻及杂音]。腹部平坦，[腹壁静脉无曲张]，无胃肠型和蠕动波，[全", "腹柔软]，[腹部无压痛]，[腹部无反跳痛]，[肝脾肋下未扪及]，Murphy征(-)，叩", "诊呈[鼓音]，移动性浊音(-)。肠鸣音正常，[无气过水声]。外生殖器[未查]，肛门", "直肠[正常]。脊柱四肢[正常]。 双下肢无浮肿，生理反射正常，病理反射阴性。", "辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复", "查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占", "预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量", "在正常范围，残气量、残总比增高。", "入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？", "3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其", "他。", "主治医师：", "副主任医师：", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 12:22:14,196 INFO     29 [qwen-vl-parser] page=8 text: 22 lines (bbox 172-193)
2026-08-10 12:22:14,196 INFO     29 [qwen-vl-parser] page=8 text: 22 sections
2026-08-10 12:22:14,373 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1557912, prompt_len=764
2026-08-10 12:22:15,674 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:22:15,675 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 12:22:15,690 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1557912, prompt_len=401
2026-08-10 12:22:23,867 INFO     29 [qwen-vl-parser] text API response (len=1165):
["221028180", "第2次入院记录", "姓名：", "性别：女", "年龄：37岁", "婚姻：已婚", "入院时间：2025-07-11 08:57", "入院方式：步行", "主诉：反复胸闷、气促8年，加重1月。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "病史陈述者签名：", "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。", "出生地：贵州省天柱县", "民族：苗族", "职业：农民", "住址：贵州省天柱县远口镇大祥村白蜡树脚组", "记录时间：2025-07-11 14:36", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 12:22:23,867 INFO     29 [qwen-vl-parser] page=9 text: 21 lines (bbox 194-214)
2026-08-10 12:22:23,867 INFO     29 [qwen-vl-parser] page=9 text: 21 sections
2026-08-10 12:22:24,168 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2682307, prompt_len=764
2026-08-10 12:22:25,668 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 12:22:25,670 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 12:22:25,690 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2682307, prompt_len=401
2026-08-10 12:22:33,484 INFO     29 [qwen-vl-parser] text API response (len=1311):
["出院记录", "入院时间：2025-02-24 12:22", "出院时间：2025-03-01 10:00", "住院天数：5天", "记录时间：2025-02-28 20:39", "入院诊断：胸闷、气促查因：支气管哮喘可能性大", "入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89", "次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。", "诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C", "+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、", "肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体", "测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。", "心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1", "0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范", "围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO", "2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球", "菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、", "两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，", "LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能", "结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、", "抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者", "及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。", "出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶", "心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，", "BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心", "率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：", "功能性消化不良？反流性食管炎？其他。", "出院医嘱：", "（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺", "激性烟雾及吸入二手烟；"]
2026-08-10 12:22:33,485 INFO     29 [qwen-vl-parser] page=10 text: 33 lines (bbox 215-247)
2026-08-10 12:22:33,485 INFO     29 [qwen-vl-parser] page=10 text: 33 sections
2026-08-10 12:22:33,606 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=845994, prompt_len=764
2026-08-10 12:22:34,233 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:22:34.231+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:22:34,833 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:22:34,834 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 12:22:34,846 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=845994, prompt_len=401
2026-08-10 12:22:37,647 INFO     29 [qwen-vl-parser] text API response (len=433):
["姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；", "(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；", "(4) 继续用药：", "舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服", "布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入", "(吸入后漱口，根据动态复查肺功能结果，调整用药)", "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服", "止咳祛痰：润肺膏 每次15g 每天2次，口服", "调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服", "(5) 如有不适，随时医院就诊，我科随诊。", "科室电话：0745-2329117 主管医师电话：13789357317", "医师签名：主治医师："]
2026-08-10 12:22:37,648 INFO     29 [qwen-vl-parser] page=11 text: 15 lines (bbox 248-262)
2026-08-10 12:22:37,648 INFO     29 [qwen-vl-parser] page=11 text: 15 sections
2026-08-10 12:22:37,826 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1540592, prompt_len=764
2026-08-10 12:22:39,215 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:22:39,216 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-10 12:22:39,224 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1540592, prompt_len=401
2026-08-10 12:22:45,960 INFO     29 [qwen-vl-parser] text API response (len=1133):
["221028180", "第2次入院记录", "姓名：", "出生地：贵州省天柱县", "性别：女", "民族：苗族", "年龄：37岁", "职业：农民", "婚姻：已婚", "住址：贵", "入院时间：2025-07-11 08:57", "记录时间：2025-07-11 14:36", "入院方式：步行", "主诉：反复胸闷、气促8年，加重1月。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "病史陈述者签名：", "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。", "眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，", "甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。", "叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。"]
2026-08-10 12:22:45,961 INFO     29 [qwen-vl-parser] page=12 text: 22 lines (bbox 263-284)
2026-08-10 12:22:45,961 INFO     29 [qwen-vl-parser] page=12 text: 22 sections
2026-08-10 12:22:46,106 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1153832, prompt_len=764
2026-08-10 12:22:47,375 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:22:47,375 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 12:22:47,388 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1153832, prompt_len=401
2026-08-10 12:22:52,738 INFO     29 [qwen-vl-parser] text API response (len=647):
["家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。", "病史陈述者签名：", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋", "姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:", "辅助检查结果：无", "入院初步诊断：胸闷、气促查因：支气管哮喘可能性大", "主治医师：", "主任医师："]
2026-08-10 12:22:52,739 INFO     29 [qwen-vl-parser] page=13 text: 10 lines (bbox 285-294)
2026-08-10 12:22:52,739 INFO     29 [qwen-vl-parser] page=13 text: 10 sections
2026-08-10 12:22:52,926 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1578095, prompt_len=764
2026-08-10 12:22:54,290 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:22:54,290 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-10 12:22:54,298 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1578095, prompt_len=401
2026-08-10 12:23:00,747 INFO     29 [qwen-vl-parser] text API response (len=1104):
["姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "入院记录", "姓名：", "出生地：贵州省天柱县远口镇大样村白蜡树脚组", "性别：女", "民族：苗族", "年龄：37岁", "职业：自由职业者", "婚姻：已婚", "住址：贵", "入院时间：2025-02-24 12:22", "记录时间：2025-02-24 14:28", "入院方式：步行", "主诉：反复胸闷、气促8年，加重半年。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳", "嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐", "渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，", "无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，", "约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，", "门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期", "体重无改变。", "既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病", "史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。", "个人史：[出生于原籍，常住本地，无粉尘放射性物质接触史，否认疫区居住", "史]，[无吸烟史，无饮酒史，否认性病及冶游史]。", "月经史：162~32025/2/21，月经周期规律，色红，量少，无痛经。", "婚育史：24岁结婚，育有1子1女，配偶及子女体健。", "家族史：家族中无同类病人。直系亲属体健。无遗传倾向疾患。", "病史陈述者签名：", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜", "色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，", "巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常", "分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-", "颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤", "正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦", ""]
2026-08-10 12:23:00,747 INFO     29 [qwen-vl-parser] page=14 text: 38 lines (bbox 295-332)
2026-08-10 12:23:00,747 INFO     29 [qwen-vl-parser] page=14 text: 38 sections
2026-08-10 12:23:00,857 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=869774, prompt_len=764
2026-08-10 12:23:02,260 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 12:23:02,261 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-10 12:23:02,275 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=869774, prompt_len=401
2026-08-10 12:23:05,485 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:23:05.485+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:23:11,739 INFO     29 [qwen-vl-parser] text API response (len=1970):
["姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-new", "常规通气报告", "测试号：2026020917", "身高：165 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "Pred", "Bst % (B/Pd", "A1", "A2", "A3", "FVC", "[L]", "2.99", "2.21", "74.02", "2.21", "2.12", "2.09", "FEV 1", "[L]", "2.67", "1.26", "48.56", "1.26", "1.13", "1.18", "FEV6", "[L]", "2.12", "2.12", "2.05", "2.02", "FEV 1 % FVC", "[%]", "84.19", "56.48", "67.09", "56.48", "53.33", "56.67", "FEV 1 % VC MAX", "[%]", "81.88", "55.26", "67.48", "55.26", "50.10", "52.31", "VC MAX", "[L]", "3.03", "2.26", "74.60", "PEF", "[L/s]", "6.28", "2.66", "42.36", "2.66", "2.58", "2.43", "MMEF 75/25", "[L/s]", "3.57", "0.51", "14.35", "0.51", "0.49", "0.41", "MEF 75", "[L/s]", "5.64", "1.47", "26.14", "1.47", "0.80", "1.21", "MEF 50", "[L/s]", "4.01", "0.68", "16.97", "0.68", "0.72", "0.57", "MEF 25", "[L/s]", "1.79", "0.19", "10.52", "0.19", "0.18", "0.15", "V backextrapolation ex", "[L]", "0.05", "0.05", "0.03", "0.04", "V backextrapol. % FVC", "[%]", "2.07", "2.07", "1.50", "1.81", "FET", "[s]", "7.63", "7.63", "7.35", "7.55", "FEF 200-1200", "[L/s]", "1.19", "1.19", "0.98", "1.05", "FVC IN", "[L]", "3.03", "2.26", "74.60", "2.26", "2.15", "2.13", "FIV1", "[L]", "2.21", "2.21", "2.12", "2.09", "FIV1 % FVC", "[%]", "97.79", "97.79", "98.68", "98.05", "FEF50 % FIF50", "[%]", "22.86", "22.86", "25.05", "19.46", "PIF", "[L/s]", "3.04", "3.04", "3.04", "2.99", "MVV", "[L/min]", "99.77", "46.21", "46.32", "46.21", "BF MVV", "[1/min]", "75.55", "75.55", "意见：", "1. 重度混合性肺通气功能障碍。", "2. 最大分钟通气量（MVV）：显著减退。", "Date", "20/2/00", "Timo", "11:48:04上午", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "Vol [L]", "Time [s]", "F/V in", "10", "8", "6", "4", "2", "0", "1", "2", "3", "4", "5", "10", "8", "6", "4", "2", "0", "100", "80", "60", "40", "20", "0", "2", "4", "6", "8", "10", "12", "1", "0", "2", "4", "6", "8", "10", "12", "1", "0", "2", "4", "6", "8", "10", "12", "1", "张", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 12:23:11,740 INFO     29 [qwen-vl-parser] page=15 text: 232 lines (bbox 333-564)
2026-08-10 12:23:11,741 INFO     29 [qwen-vl-parser] page=15 text: 232 sections
2026-08-10 12:23:11,882 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1055456, prompt_len=764
2026-08-10 12:23:13,255 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-09"
}
```
2026-08-10 12:23:13,255 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=2026-02-09
2026-08-10 12:23:13,263 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1055456, prompt_len=401
2026-08-10 12:23:19,676 INFO     29 [qwen-vl-parser] text API response (len=1117):
["呼出气一氧化氮检测报告单", "姓名：杨", "性别：女", "出生日期：1987-12-01", "年龄：38岁2个月", "ID号：", "测试日期：2026-02-09", "科室：呼吸科门诊", "医生：张", "问卷调查：", "激素：正在使用口 三天内未使用口 从未使用口", "抗生素：正在使用口 三天内未使用口 从未使用口", "吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口", "症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：", "病史：过敏史口 其他：", "注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。", "检测信息：", "项目：在线", "呼气压力：8.8cmH2O 呼气流速：45ml/s", "呼气时间：5s 温度：21.8℃ 湿度：38.9%", "呼气浓度：10、11、12、11、11、11、10、10、10、", "10、10、10、11、10、11、11、11、11ppb", "项目：小气道", "呼气压力：11.3cmH2O 呼气流速：202ml/s", "呼气时间：3s 温度：22.0℃ 湿度：39.0%", "呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0", "0.0、0.0、0.0、0.0、1.0、1.0、1.0、", "1.0、1.0、0.0、0.0、0.0ppb", "参考意义：", "(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)", "测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型", "FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症", "25 - 50ppb 20 - 35ppb* 混合型气道炎症", "> 50ppb > 35ppb* 嗜酸性气道炎症", "CaNO ≤ 5ppb ≤ 3ppb 小气道正常", "> 5ppb > 3ppb 小气道炎症", "FaNO < 125ppb 考虑Kartagener综合征、PCD、CF或", "重度的鼻窦炎或鼻息肉", "125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉", "250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断", "> 500ppb 考虑过敏性鼻炎", "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "此结果仅对本次呼气检测负责", "测定结果：FeNO 60:11ppb CaNO :1.0ppb", "操作员：蒋细萍", "张日石", ""]
2026-08-10 12:23:19,677 INFO     29 [qwen-vl-parser] page=16 text: 46 lines (bbox 565-610)
2026-08-10 12:23:19,677 INFO     29 [qwen-vl-parser] page=16 text: 46 sections
2026-08-10 12:23:19,789 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=680206, prompt_len=764
2026-08-10 12:23:21,016 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 12:23:21,016 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=None
2026-08-10 12:23:21,031 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=680206, prompt_len=401
2026-08-10 12:23:26,990 INFO     29 [qwen-vl-parser] text API response (len=993):
["一口气法弥散功能报告", "姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-now", "测试号：2026020917", "身高：155 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "CO (%)", "Volume [L]", "CH4 [%]", "0.25", "0.20", "0.15", "0.10", "0.05", "0.00", "Time [s]", "Pred", "Best", "Best%", "Act1", "DLCO SB", "[mmol/min/kPa]", "8.08", "9.45", "116.9", "9.45", "DLCO/VA", "[mmol/min/kPa/L]", "1.82", "2.38", "130.8", "2.38", "VA", "[L]", "4.29", "3.97", "92.5", "3.97", "VC IN", "[L]", "3.03", "2.26", "74.6", "Discard vol", "[L]", "1.00", "Sample vol", "[L]", "0.53", "ERV", "[L]", "1.10", "IRV", "[L]", "IC", "[L]", "1.93", "VT", "[L]", "0.43", "VC MAX", "[L]", "3.03", "2.26", "74.6", "TLC-SB", "[L]", "4.44", "4.10", "92.4", "4.10", "RV-SB", "[L]", "1.41", "2.18", "154.5", "2.18", "RV%TLC-SB", "[%]", "31.88", "53.26", "167.1", "53.26", "FRC-SB", "[L]", "2.51", "2.39", "95.2", "2.39", "FRC%TLC-SB", "[%]", "51.18", "58.28", "113.9", "58.28", "测试日期", "26/2/0", "意见：", "1.弥散功能在正常范围。", "2.残气量、残总比增高，肺总量在正常范围。", "张"]
2026-08-10 12:23:26,991 INFO     29 [qwen-vl-parser] page=17 text: 108 lines (bbox 611-718)
2026-08-10 12:23:26,991 INFO     29 [qwen-vl-parser] page=17 text: 108 sections
2026-08-10 12:23:27,121 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=929802, prompt_len=764
2026-08-10 12:23:28,627 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 12:23:28,628 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=None
2026-08-10 12:23:28,644 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=929802, prompt_len=401
2026-08-10 12:23:36,773 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:23:36.770+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:23:39,839 INFO     29 [qwen-vl-parser] text API response (len=2227):
["肺功能试验报告", "姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-new", "测试号：2026020017", "身高：166 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "Pred", "A1 A1/Pd", "P1 A2/Pd chg%l", "P2 A3/Pd chg%2", "P3 A4/Pd chg%3", "FVC", "[L]", "2.99", "2.21", "74.0", "2.63", "87.9", "18.72", "2.04", "88.2", "19.17", "2.67", "86.0", "16.23", "FEV 1", "[L]", "2.67", "1.25", "48.6", "1.62", "69.2", "21.85", "1.84", "69.8", "23.23", "1.60", "68.4", "20.23", "FEV 1 % FVC", "[%]", "84.19", "56.48", "67.1", "67.97", "68.9", "2.64", "68.40", "69.4", "3.41", "68.42", "69.4", "3.44", "FEV 1 % VC MAX", "[%]", "81.88", "65.26", "67.6", "67.97", "70.8", "4.91", "68.40", "71.3", "6.70", "68.42", "71.4", "5.73", "VC MAX", "[L]", "3.03", "2.26", "74.6", "2.63", "86.6", "16.14", "2.64", "87.0", "16.69", "2.57", "84.8", "13.71", "PEF", "[L/s]", "6.28", "2.66", "42.4", "2.90", "46.2", "9.17", "3.37", "53.7", "26.79", "3.42", "64.6", "28.64", "MMEF 75/25", "[L/s]", "3.57", "0.61", "14.4", "0.67", "18.8", "31.03", "0.73", "20.4", "42.01", "0.69", "19.4", "35.02", "MEF 50", "[L/s]", "4.01", "0.68", "17.0", "0.90", "22.5", "32.75", "0.89", "22.1", "30.15", "0.88", "21.9", "29.17", "MEF 25", "[L/s]", "1.79", "0.19", "10.5", "0.27", "15.2", "44.16", "0.33", "18.7", "77.66", "0.31", "17.6", "66.49", "FET", "[s]", "7.63", "8.01", "4.99", "7.79", "2.14", "7.43", "-2.60", "V backextrapolation ex [L]", "0.05", "0.04", "-11.67", "0.04", "-18.64", "0.04", "-13.51", "PIF", "[L/s]", "3.04", "3.37", "10.91", "3.51", "15.70", "3.60", "18.67", "FIV1", "[L]", "2.21", "2.56", "15.71", "2.56", "15.66", "2.50", "13.09", "PEF50 % FIF50", "[%]", "22.86", "28.15", "23.14", "25.36", "10.95", "27.28", "19.33", "MVV", "[L/min]", "99.77", "46.21", "46.3", "BF MVV", "[1/min]", "75.55", "10", "Flow [L/s]", "F/V ex", "1", "2", "3", "4", "6", "8", "4", "2", "0", "Vol [L]", "1", "2", "3", "4", "5", "10", "F/V In", "Vol%VCmax", "0", "0", "Vol [L]", "20", "40", "60", "80", "100", "1", "2", "VCmax", "3", "4", "5", "6", "Time [s]", "0", "2", "4", "6", "8", "10", "12", "14", "意见：", "1. 中重度阻塞性肺通气功能障碍。", "2. 支气管舒张试验阳性。", "(1. 24h内无支气管舒张药物使用史)", "(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)", "(3. 检查质量：舒张前：A级；舒张后：A级)", "张四彩", "CS 扫描全能王", "3 亿人都在用的扫描 App"]
2026-08-10 12:23:39,839 INFO     29 [qwen-vl-parser] page=18 text: 250 lines (bbox 719-968)
2026-08-10 12:23:39,839 INFO     29 [qwen-vl-parser] page=18 text: 250 sections
2026-08-10 12:23:40,002 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1413782, prompt_len=764
2026-08-10 12:23:41,358 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:23:41,358 INFO     29 [qwen-vl-parser] page=19 classify=text report_date=None
2026-08-10 12:23:41,375 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1413782, prompt_len=401
2026-08-10 12:23:43,391 INFO     29 [qwen-vl-parser] text API response (len=318):
["金城大药房", "会员号:", "积分:112550", "本次积分:596.00", "名称", "规格", "数量", "厂家", "批号", "单价", "金额", "1-布地奈德福莫特罗吸入粉雾剂", "320ug:9ug*60吸/支", "2.00", "阿斯利康制药", "PKMR", "300.00", "596.00", "运动员慎用!!!", "***重打销售单***", "总计数量:2.00", "应收:600.00", "优惠:4.00", "付款:596.00", "找零:0.00", "销售单号:251210031062", "款台号:2", "日期:2025-12-10", "15:21:53"]
2026-08-10 12:23:43,392 INFO     29 [qwen-vl-parser] page=19 text: 29 lines (bbox 969-997)
2026-08-10 12:23:43,392 INFO     29 [qwen-vl-parser] page=19 text: 29 sections
2026-08-10 12:23:43,392 INFO     29 [qwen-vl-parser] parse_pdf done: 998 sections from 19 pages.
2026-08-10 12:23:43,406 INFO     29 Close text detector.
2026-08-10 12:23:43,833 INFO     29 Close text recognizer.
2026-08-10 12:23:44,271 INFO     29 Close recognizer.
2026-08-10 12:23:44,662 INFO     29 Close recognizer.
2026-08-10 12:23:45,117 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 12:23:45,117 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Parser:MedLink | outputs={"html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "json"}
2026-08-10 12:23:45,118 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 12:23:45,139 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:23:45,139 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 人民医院\n[BBOX-1] H43120200207, 院区: 舊城院区)\n[BBOX-2] 基本就诊信息\n[BBOX-3] 姓名: 核\n[BBOX-4] 医生: 旅\n[BBOX-5] 挂号单: 25000448502\n[BBOX-6] 医保号: 5200002600000000600637839\n[BBOX-7] 付款: 城乡居民基本医疗 费别: 普通\n[BBOX-8] 门诊号: 2502240221\n[BBOX-9] 社区号:\n[BBOX-10] 门诊就诊:呼吸内科门诊,2025-09-30 14:50\n[BBOX-11] 医嘱\n[BBOX-12] 报告\n[BBOX-13] 已作废\n[BBOX-14] 全部\n[BBOX-15] 处方\n[BBOX-16] 其他\n[BBOX-17] 生效时间\n[BBOX-18] 内容\n[BBOX-19] 用法\n[BBOX-20] 2025-09-30\n[BBOX-21] 孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/\n[BBOX-22] 睡前口服,每天一次,共30天\n[BBOX-23] 14:51\n[BBOX-24] 盒,共10盒,每次10mg\n[BBOX-25] 基本就诊信息\n[BBOX-26] 姓名：杨\n[BBOX-27] 医生：\n[BBOX-28] 挂号单：26000068319\n[BBOX-29] 医保号：52000026000000006006378395\n[BBOX-30] 付款：城乡居民基本医疗 费别：普通\n[BBOX-31] 门诊号：2502240221\n[BBOX-32] 社区号：\n[BBOX-33] 门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04\n[BBOX-34] 医嘱|报告|\n[BBOX-35] 已作废|全部|处方|其他\n[BBOX-36] 生效时间\n[BBOX-37] 内容\n[BBOX-38] 用法\n[BBOX-39] 2026-02-09\n[BBOX-40] 肺功能全套+支气管舒张试验,共1次\n[BBOX-41] 2026-02-09\n[BBOX-42] (基)硫酸沙丁胺醇吸入气雾剂 (山东)\n[BBOX-43] 吸入,一次,共1天\n[BBOX-44] 11:08\n[BBOX-45] 100ug*200揿/瓶,共1瓶,每次400ug\n[BBOX-46] 2026-02-09\n[BBOX-47] 呼出气一氧化氮测定,共1次\n[BBOX-48] 2026-02-09\n[BBOX-49] 沙美特罗替卡松粉吸入剂(法国GLAXO)\n[BBOX-50] 吸入,每天二次,共1天\n[BBOX-51] 12.33\n[BBOX-52] 50ug/500ug*60吸/瓶,共1瓶,每次50ug\n[BBOX-53] \\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c\n[BBOX-54] 报告时间: 2025-02-24\n[BBOX-55] 怀化市肿瘤医院\n[BBOX-56] 怀化市第二人民医院\n[BBOX-57] 鹤城院区\n[BBOX-58] 湖南HR\n[BBOX-59] CT影像诊断报告单\n[BBOX-60] ID: 86562633\n[BBOX-61] 检查号: CT00525514\n[BBOX-62] 姓名:\n[BBOX-63] 性别: 女\n[BBOX-64] 年龄: 37岁\n[BBOX-65] 住院号: 220999152\n[BBOX-66] 床号: 46\n[BBOX-67] 申请科室: 呼吸与危重症医学科\n[BBOX-68] 申请医生: 易莹\n[BBOX-69] 检查日期: 2025.02.25\n[BBOX-70] 报告日期: 2025.02.25 09:45:16\n[BBOX-71] 检查项目: CT成套:胸部(平扫(三维重建))\n[BBOX-72] 检查所见:\n[BBOX-73] 右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见\n[BBOX-74] 条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主\n[BBOX-75] 要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。\n[BBOX-76] 意见:\n[BBOX-77] 1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。\n[BBOX-78] 2. 右肺中叶少许慢性炎症。\n[BBOX-79] 怀化市中心医院\n[BBOX-80] HUAIHUA CENTRAL HOSPITAL\n[BBOX-81] 怀化市肿瘤医院\n[BBOX-82] 湖南HR\n[BBOX-83] CT影像诊断报告单\n[BBOX-84] ID: 93717786\n[BBOX-85] 检查号: CT00568277\n[BBOX-86] 姓名:\n[BBOX-87] 性别: 女\n[BBOX-88] 年龄: 37岁\n[BBOX-89] 住院号: 221028180\n[BBOX-90] 床号: 42\n[BBOX-91] 申请科室: 呼吸与危重症医学科\n[BBOX-92] 申请医生:\n[BBOX-93] 检查日期: 2025.07.11\n[BBOX-94] 报告日期: 2025.07.11 16:08:56\n[BBOX-95] 检查项目: CT成套胸部平扫(三维重建)\n[BBOX-96] 检查所见:\n[BBOX-97] 与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。\n[BBOX-98] 右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部\n[BBOX-99] 分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。\n[BBOX-100] 意见:\n[BBOX-101] 1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。\n[BBOX-102] 2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。\n[BBOX-103] HUAIHUA CENTRAL HOSPITAL\n[BBOX-104] 怀化市肿瘤医院\n[BBOX-105] 姓名：\n[BBOX-106] 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n[BBOX-107] 221028180\n[BBOX-108] 3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总\n[BBOX-109] 神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓\n[BBOX-110] 浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经\n[BBOX-111] (感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞\n[BBOX-112] <10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌\n[BBOX-113] (TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支\n[BBOX-114] 持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司\n[BBOX-115] 特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前\n[BBOX-116] 好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。\n[BBOX-117] 出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发\n[BBOX-118] 热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，\n[BBOX-119] BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。\n[BBOX-120] 心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。\n[BBOX-121] 出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧\n[BBOX-122] 段结节（LU-RADS 2类）。\n[BBOX-123] 出院医嘱：\n[BBOX-124] 1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生\n[BBOX-125] 活习惯，增强体质，适当运动，加强营养；\n[BBOX-126] 2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复\n[BBOX-127] 查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；\n[BBOX-128] 3.出院后继续服用中药。\n[BBOX-129] 4.出院带药：\n[BBOX-130] 舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱\n[BBOX-131] 口，根据动态复查肺功能结果，调整用药）\n[BBOX-132] 祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次\n[BBOX-133] 抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次\n[BBOX-134] 5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；\n[BBOX-135] 6.如有不适，随时医院就诊，我科随诊。\n[BBOX-136] 科室护士办公室电话：0745-2329117。主管医师电话：13789357317\n[BBOX-137] 医师签名：主治医师\n[BBOX-138] zz1028180\n[BBOX-139] 37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n[BBOX-140] 出院记录\n[BBOX-141] 入院时间：2025-07-11 08:57\n[BBOX-142] 出院时间：2025-07-22 15:00\n[BBOX-143] 住院天数：11天\n[BBOX-144] 记录时间：2025-07-21 16:14\n[BBOX-145] 入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；\n[BBOX-146] 4.腹胀查因：功能性消化不良？反流性食管炎？其他。\n[BBOX-147] 入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T\n[BBOX-148] 36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面\n[BBOX-149] 容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及\n[BBOX-150] 少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，\n[BBOX-151] 无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，\n[BBOX-152] LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功\n[BBOX-153] 能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散\n[BBOX-154] 功能在正常范围；肺总量在正常范围，残气量、残总比增高。\n[BBOX-155] 诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分\n[BBOX-156] 压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中\n[BBOX-157] 性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；\n[BBOX-158] 尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红\n[BBOX-159] 细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；\n[BBOX-160] 电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C\n[BBOX-161] 蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链\n[BBOX-162] DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生\n[BBOX-163] 虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：\n[BBOX-164] 胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.\n[BBOX-165] 支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气\n[BBOX-166] 功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、\n[BBOX-167] MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重\n[BBOX-168] 减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳\n[BBOX-169] 性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，\n[BBOX-170] 绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），\n[BBOX-171] 2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：\n[BBOX-172] 怀化市中心医院\n[BBOX-173] HUAIHUA CENTRAL HOSPITAL\n[BBOX-174] 怀化市肿瘤医院\n[BBOX-175] 姓名：\n[BBOX-176] 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n[BBOX-177] 221028180\n[BBOX-178] [心前区无隆起]，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，\n[BBOX-179] [各瓣膜听诊区未闻及杂音]。腹部平坦，[腹壁静脉无曲张]，无胃肠型和蠕动波，[全\n[BBOX-180] 腹柔软]，[腹部无压痛]，[腹部无反跳痛]，[肝脾肋下未扪及]，Murphy征(-)，叩\n[BBOX-181] 诊呈[鼓音]，移动性浊音(-)。肠鸣音正常，[无气过水声]。外生殖器[未查]，肛门\n[BBOX-182] 直肠[正常]。脊柱四肢[正常]。 双下肢无浮肿，生理反射正常，病理反射阴性。\n[BBOX-183] 辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复\n[BBOX-184] 查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占\n[BBOX-185] 预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量\n[BBOX-186] 在正常范围，残气量、残总比增高。\n[BBOX-187] 入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？\n[BBOX-188] 3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其\n[BBOX-189] 他。\n[BBOX-190] 主治医师：\n[BBOX-191] 副主任医师：\n[BBOX-192] CS 扫描全能王\n[BBOX-193] 3亿人都在用的扫描App\n[BBOX-194] 221028180\n[BBOX-195] 第2次入院记录\n[BBOX-196] 姓名：\n[BBOX-197] 性别：女\n[BBOX-198] 年龄：37岁\n[BBOX-199] 婚姻：已婚\n[BBOX-200] 入院时间：2025-07-11 08:57\n[BBOX-201] 入院方式：步行\n[BBOX-202] 主诉：反复胸闷、气促8年，加重1月。\n[BBOX-203] 现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。\n[BBOX-204] 出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。\n[BBOX-205] 既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。\n[BBOX-206] 病史陈述者签名：\n[BBOX-207] 体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。\n[BBOX-208] 出生地：贵州省天柱县\n[BBOX-209] 民族：苗族\n[BBOX-210] 职业：农民\n[BBOX-211] 住址：贵州省天柱县远口镇大祥村白蜡树脚组\n[BBOX-212] 记录时间：2025-07-11 14:36\n[BBOX-213] CS 扫描全能王\n[BBOX-214] 3亿人都在用的扫描App\n[BBOX-215] 出院记录\n[BBOX-216] 入院时间：2025-02-24 12:22\n[BBOX-217] 出院时间：2025-03-01 10:00\n[BBOX-218] 住院天数：5天\n[BBOX-219] 记录时间：2025-02-28 20:39\n[BBOX-220] 入院诊断：胸闷、气促查因：支气管哮喘可能性大\n[BBOX-221] 入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。\n[BBOX-222] 体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸\n[BBOX-223] 氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89\n[BBOX-224] 次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下���无浮肿。辅助检查：无。\n[BBOX-225] 诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C\n[BBOX-226] +3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、\n[BBOX-227] 肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体\n[BBOX-228] 测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。\n[BBOX-229] 心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1\n[BBOX-230] 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范\n[BBOX-231] 围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO\n[BBOX-232] 2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球\n[BBOX-233] 菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、\n[BBOX-234] 两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，\n[BBOX-235] LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能\n[BBOX-236] 结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、\n[BBOX-237] 抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者\n[BBOX-238] 及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。\n[BBOX-239] 出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶\n[BBOX-240] 心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，\n[BBOX-241] BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心\n[BBOX-242] 率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。\n[BBOX-243] 出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：\n[BBOX-244] 功能性消化不良？反流性食管炎？其他。\n[BBOX-245] 出院医嘱：\n[BBOX-246] （1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺\n[BBOX-247] 激性烟雾及吸入二手烟；\n[BBOX-248] 姓名：\n[BBOX-249] 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n[BBOX-250] 220999152\n[BBOX-251] (2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；\n[BBOX-252] (3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；\n[BBOX-253] (4) 继续用药：\n[BBOX-254] 舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服\n[BBOX-255] 布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入\n[BBOX-256] (吸入后漱口，根据动态复查肺功能结果，调整用药)\n[BBOX-257] 抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服\n[BBOX-258] 止咳祛痰：润肺膏 每次15g 每天2次，口服\n[BBOX-259] 调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服\n[BBOX-260] (5) 如有不适，随时医院就诊，我科随诊。\n[BBOX-261] 科室电话：0745-2329117 主管医师电话：13789357317\n[BBOX-262] 医师签名：主治医师：\n[BBOX-263] 221028180\n[BBOX-264] 第2次入院记录\n[BBOX-265] 姓名：\n[BBOX-266] 出生地：贵州省天柱县\n[BBOX-267] 性别：女\n[BBOX-268] 民族：苗族\n[BBOX-269] 年龄：37岁\n[BBOX-270] 职业：农民\n[BBOX-271] 婚姻：已婚\n[BBOX-272] 住址：贵\n[BBOX-273] 入院时间：2025-07-11 08:57\n[BBOX-274] 记录时间：2025-07-11 14:36\n[BBOX-275] 入院方式：步行\n[BBOX-276] 主诉：反复胸闷、气促8年，加重1月。\n[BBOX-277] 现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。\n[BBOX-278] 出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。\n[BBOX-279] 既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。\n[BBOX-280] 病史陈述者签名：\n[BBOX-281] 体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。\n[BBOX-282] 眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，\n[BBOX-283] 甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。\n[BBOX-284] 叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。\n[BBOX-285] 家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。\n[BBOX-286] 病史陈述者签名：\n[BBOX-287] 体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋\n[BBOX-288] 姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n[BBOX-289] 220999152\n[BBOX-290] 下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:\n[BBOX-291] 辅助检查结果：无\n[BBOX-292] 入院初步诊断：胸闷、气促查因：支气管哮喘可能性大\n[BBOX-293] 主治医师：\n[BBOX-294] 主任医师：\n[BBOX-295] 姓名：\n[BBOX-296] 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n[BBOX-297] 220999152\n[BBOX-298] 入院记录\n[BBOX-299] 姓名：\n[BBOX-300] 出生地：贵州省天柱县远口镇大样村白蜡树脚组\n[BBOX-301] 性别：女\n[BBOX-302] 民族：苗族\n[BBOX-303] 年龄：37岁\n[BBOX-304] 职业：自由职业者\n[BBOX-305] 婚姻：已婚\n[BBOX-306] 住址：贵\n[BBOX-307] 入院时间：2025-02-24 12:22\n[BBOX-308] 记录时间：2025-02-24 14:28\n[BBOX-309] 入院方式：步行\n[BBOX-310] 主诉：反复胸闷、气促8年，加重半年。\n[BBOX-311] 现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳\n[BBOX-312] 嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐\n[BBOX-313] 渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，\n[BBOX-314] 无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，\n[BBOX-315] 约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，\n[BBOX-316] 门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期\n[BBOX-317] 体重无改变。\n[BBOX-318] 既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病\n[BBOX-319] 史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。\n[BBOX-320] 个人史：[出生于原籍，常住本地，无粉尘放射性物质接触史，否认疫区居住\n[BBOX-321] 史]，[无吸烟史，无饮酒史，否认性病及冶游史]。\n[BBOX-322] 月经史：162~32025/2/21，月经周期规律，色红，量少，无痛经。\n[BBOX-323] 婚育史：24岁结婚，育有1子1女，配偶及子女体健。\n[BBOX-324] 家族史：家族中无同类病人。直系亲属体健。无遗传倾向疾患。\n[BBOX-325] 病史陈述者签名：\n[BBOX-326] 体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸\n[BBOX-327] 氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜\n[BBOX-328] 色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，\n[BBOX-329] 巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常\n[BBOX-330] 分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-\n[BBOX-331] 颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤\n[BBOX-332] 正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦\n[BBOX-333] 姓名：\n[BBOX-334] 年龄：38岁\n[BBOX-335] 性别：女\n[BBOX-336] 科别：\n[BBOX-337] 保险：\n[BBOX-338] 预计值模式：Standard-new\n[BBOX-339] 常规通气报告\n[BBOX-340] 测试号：2026020917\n[BBOX-341] 身高：165 cm\n[BBOX-342] 体重：60 kg\n[BBOX-343] 备注：\n[BBOX-344] 联系电话：\n[BBOX-345] 操作者：蒋细萍\n[BBOX-346] Pred\n[BBOX-347] Bst % (B/Pd\n[BBOX-348] A1\n[BBOX-349] A2\n[BBOX-350] A3\n[BBOX-351] FVC\n[BBOX-352] [L]\n[BBOX-353] 2.99\n[BBOX-354] 2.21\n[BBOX-355] 74.02\n[BBOX-356] 2.21\n[BBOX-357] 2.12\n[BBOX-358] 2.09\n[BBOX-359] FEV 1\n[BBOX-360] [L]\n[BBOX-361] 2.67\n[BBOX-362] 1.26\n[BBOX-363] 48.56\n[BBOX-364] 1.26\n[BBOX-365] 1.13\n[BBOX-366] 1.18\n[BBOX-367] FEV6\n[BBOX-368] [L]\n[BBOX-369] 2.12\n[BBOX-370] 2.12\n[BBOX-371] 2.05\n[BBOX-372] 2.02\n[BBOX-373] FEV 1 % FVC\n[BBOX-374] [%]\n[BBOX-375] 84.19\n[BBOX-376] 56.48\n[BBOX-377] 67.09\n[BBOX-378] 56.48\n[BBOX-379] 53.33\n[BBOX-380] 56.67\n[BBOX-381] FEV 1 % VC MAX\n[BBOX-382] [%]\n[BBOX-383] 81.88\n[BBOX-384] 55.26\n[BBOX-385] 67.48\n[BBOX-386] 55.26\n[BBOX-387] 50.10\n[BBOX-388] 52.31\n[BBOX-389] VC MAX\n[BBOX-390] [L]\n[BBOX-391] 3.03\n[BBOX-392] 2.26\n[BBOX-393] 74.60\n[BBOX-394] PEF\n[BBOX-395] [L/s]\n[BBOX-396] 6.28\n[BBOX-397] 2.66\n[BBOX-398] 42.36\n[BBOX-399] 2.66\n[BBOX-400] 2.58\n[BBOX-401] 2.43\n[BBOX-402] MMEF 75/25\n[BBOX-403] [L/s]\n[BBOX-404] 3.57\n[BBOX-405] 0.51\n[BBOX-406] 14.35\n[BBOX-407] 0.51\n[BBOX-408] 0.49\n[BBOX-409] 0.41\n[BBOX-410] MEF 75\n[BBOX-411] [L/s]\n[BBOX-412] 5.64\n[BBOX-413] 1.47\n[BBOX-414] 26.14\n[BBOX-415] 1.47\n[BBOX-416] 0.80\n[BBOX-417] 1.21\n[BBOX-418] MEF 50\n[BBOX-419] [L/s]\n[BBOX-420] 4.01\n[BBOX-421] 0.68\n[BBOX-422] 16.97\n[BBOX-423] 0.68\n[BBOX-424] 0.72\n[BBOX-425] 0.57\n[BBOX-426] MEF 25\n[BBOX-427] [L/s]\n[BBOX-428] 1.79\n[BBOX-429] 0.19\n[BBOX-430] 10.52\n[BBOX-431] 0.19\n[BBOX-432] 0.18\n[BBOX-433] 0.15\n[BBOX-434] V backextrapolation ex\n[BBOX-435] [L]\n[BBOX-436] 0.05\n[BBOX-437] 0.05\n[BBOX-438] 0.03\n[BBOX-439] 0.04\n[BBOX-440] V backextrapol. % FVC\n[BBOX-441] [%]\n[BBOX-442] 2.07\n[BBOX-443] 2.07\n[BBOX-444] 1.50\n[BBOX-445] 1.81\n[BBOX-446] FET\n[BBOX-447] [s]\n[BBOX-448] 7.63\n[BBOX-449] 7.63\n[BBOX-450] 7.35\n[BBOX-451] 7.55\n[BBOX-452] FEF 200-1200\n[BBOX-453] [L/s]\n[BBOX-454] 1.19\n[BBOX-455] 1.19\n[BBOX-456] 0.98\n[BBOX-457] 1.05\n[BBOX-458] FVC IN\n[BBOX-459] [L]\n[BBOX-460] 3.03\n[BBOX-461] 2.26\n[BBOX-462] 74.60\n[BBOX-463] 2.26\n[BBOX-464] 2.15\n[BBOX-465] 2.13\n[BBOX-466] FIV1\n[BBOX-467] [L]\n[BBOX-468] 2.21\n[BBOX-469] 2.21\n[BBOX-470] 2.12\n[BBOX-471] 2.09\n[BBOX-472] FIV1 % FVC\n[BBOX-473] [%]\n[BBOX-474] 97.79\n[BBOX-475] 97.79\n[BBOX-476] 98.68\n[BBOX-477] 98.05\n[BBOX-478] FEF50 % FIF50\n[BBOX-479] [%]\n[BBOX-480] 22.86\n[BBOX-481] 22.86\n[BBOX-482] 25.05\n[BBOX-483] 19.46\n[BBOX-484] PIF\n[BBOX-485] [L/s]\n[BBOX-486] 3.04\n[BBOX-487] 3.04\n[BBOX-488] 3.04\n[BBOX-489] 2.99\n[BBOX-490] MVV\n[BBOX-491] [L/min]\n[BBOX-492] 99.77\n[BBOX-493] 46.21\n[BBOX-494] 46.32\n[BBOX-495] 46.21\n[BBOX-496] BF MVV\n[BBOX-497] [1/min]\n[BBOX-498] 75.55\n[BBOX-499] 75.55\n[BBOX-500] 意见：\n[BBOX-501] 1. 重度混合性肺通气功能障碍。\n[BBOX-502] 2. 最大分钟通气量（MVV）：显著减退。\n[BBOX-503] Date\n[BBOX-504] 20/2/00\n[BBOX-505] Timo\n[BBOX-506] 11:48:04上午\n[BBOX-507] Flow [L/s]\n[BBOX-508] F/V ex\n[BBOX-509] Vol [L]\n[BBOX-510] Vol%VCmax\n[BBOX-511] VCmax\n[BBOX-512] Time [s]\n[BBOX-513] Vol [L]\n[BBOX-514] Time [s]\n[BBOX-515] F/V in\n[BBOX-516] 10\n[BBOX-517] 8\n[BBOX-518] 6\n[BBOX-519] 4\n[BBOX-520] 2\n[BBOX-521] 0\n[BBOX-522] 1\n[BBOX-523] 2\n[BBOX-524] 3\n[BBOX-525] 4\n[BBOX-526] 5\n[BBOX-527] 10\n[BBOX-528] 8\n[BBOX-529] 6\n[BBOX-530] 4\n[BBOX-531] 2\n[BBOX-532] 0\n[BBOX-533] 100\n[BBOX-534] 80\n[BBOX-535] 60\n[BBOX-536] 40\n[BBOX-537] 20\n[BBOX-538] 0\n[BBOX-539] 2\n[BBOX-540] 4\n[BBOX-541] 6\n[BBOX-542] 8\n[BBOX-543] 10\n[BBOX-544] 12\n[BBOX-545] 1\n[BBOX-546] 0\n[BBOX-547] 2\n[BBOX-548] 4\n[BBOX-549] 6\n[BBOX-550] 8\n[BBOX-551] 10\n[BBOX-552] 12\n[BBOX-553] 1\n[BBOX-554] 0\n[BBOX-555] 2\n[BBOX-556] 4\n[BBOX-557] 6\n[BBOX-558] 8\n[BBOX-559] 10\n[BBOX-560] 12\n[BBOX-561] 1\n[BBOX-562] 张\n[BBOX-563] CS 扫描全能王\n[BBOX-564] 3亿人都在用的扫描App\n[BBOX-565] 呼出气一氧化氮检测报告单\n[BBOX-566] 姓名：杨\n[BBOX-567] 性别：女\n[BBOX-568] 出生日期：1987-12-01\n[BBOX-569] 年龄：38岁2个月\n[BBOX-570] ID号：\n[BBOX-571] 测试日期：2026-02-09\n[BBOX-572] 科室：呼吸科门诊\n[BBOX-573] 医生：张\n[BBOX-574] 问卷调查���\n[BBOX-575] 激素：正在使用口 三天内未使用口 从未使用口\n[BBOX-576] 抗生素：正在使用口 三天内未使用口 从未使用口\n[BBOX-577] 吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口\n[BBOX-578] 症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：\n[BBOX-579] 病史：过敏史口 其他：\n[BBOX-580] 注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。\n[BBOX-581] 检测信息：\n[BBOX-582] 项目：在线\n[BBOX-583] 呼气压力：8.8cmH2O 呼气流速：45ml/s\n[BBOX-584] 呼气时间：5s 温度：21.8℃ 湿度：38.9%\n[BBOX-585] 呼气浓度：10、11、12、11、11、11、10、10、10、\n[BBOX-586] 10、10、10、11、10、11、11、11、11ppb\n[BBOX-587] 项目：小气道\n[BBOX-588] 呼气压力：11.3cmH2O 呼气流速：202ml/s\n[BBOX-589] 呼气时间：3s 温度：22.0℃ 湿度：39.0%\n[BBOX-590] 呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0\n[BBOX-591] 0.0、0.0、0.0、0.0、1.0、1.0、1.0、\n[BBOX-592] 1.0、1.0、0.0、0.0、0.0ppb\n[BBOX-593] 参考意义：\n[BBOX-594] (根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)\n[BBOX-595] 测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型\n[BBOX-596] FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症\n[BBOX-597] 25 - 50ppb 20 - 35ppb* 混合型气道炎症\n[BBOX-598] > 50ppb > 35ppb* 嗜酸性气道炎症\n[BBOX-599] CaNO ≤ 5ppb ≤ 3ppb 小气道正常\n[BBOX-600] > 5ppb > 3ppb 小气道炎症\n[BBOX-601] FaNO < 125ppb 考虑Kartagener综合征、PCD、CF或\n[BBOX-602] 重度的鼻窦炎或鼻息肉\n[BBOX-603] 125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉\n[BBOX-604] 250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断\n[BBOX-605] > 500ppb 考虑过敏性鼻炎\n[BBOX-606] (*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n[BBOX-607] 此结果仅对本次呼气检测负责\n[BBOX-608] 测定结果：FeNO 60:11ppb CaNO :1.0ppb\n[BBOX-609] 操作员：蒋细萍\n[BBOX-610] 张日石\n[BBOX-611] 一口气法弥散功能报告\n[BBOX-612] 姓名：\n[BBOX-613] 年龄：38岁\n[BBOX-614] 性别：女\n[BBOX-615] 科别：\n[BBOX-616] 保险：\n[BBOX-617] 预计值模式：Standard-now\n[BBOX-618] 测试号：2026020917\n[BBOX-619] 身高：155 cm\n[BBOX-620] 体重：60 kg\n[BBOX-621] 备注：\n[BBOX-622] 联系电话：\n[BBOX-623] 操作者：蒋细萍\n[BBOX-624] CO (%)\n[BBOX-625] Volume [L]\n[BBOX-626] CH4 [%]\n[BBOX-627] 0.25\n[BBOX-628] 0.20\n[BBOX-629] 0.15\n[BBOX-630] 0.10\n[BBOX-631] 0.05\n[BBOX-632] 0.00\n[BBOX-633] Time [s]\n[BBOX-634] Pred\n[BBOX-635] Best\n[BBOX-636] Best%\n[BBOX-637] Act1\n[BBOX-638] DLCO SB\n[BBOX-639] [mmol/min/kPa]\n[BBOX-640] 8.08\n[BBOX-641] 9.45\n[BBOX-642] 116.9\n[BBOX-643] 9.45\n[BBOX-644] DLCO/VA\n[BBOX-645] [mmol/min/kPa/L]\n[BBOX-646] 1.82\n[BBOX-647] 2.38\n[BBOX-648] 130.8\n[BBOX-649] 2.38\n[BBOX-650] VA\n[BBOX-651] [L]\n[BBOX-652] 4.29\n[BBOX-653] 3.97\n[BBOX-654] 92.5\n[BBOX-655] 3.97\n[BBOX-656] VC IN\n[BBOX-657] [L]\n[BBOX-658] 3.03\n[BBOX-659] 2.26\n[BBOX-660] 74.6\n[BBOX-661] Discard vol\n[BBOX-662] [L]\n[BBOX-663] 1.00\n[BBOX-664] Sample vol\n[BBOX-665] [L]\n[BBOX-666] 0.53\n[BBOX-667] ERV\n[BBOX-668] [L]\n[BBOX-669] 1.10\n[BBOX-670] IRV\n[BBOX-671] [L]\n[BBOX-672] IC\n[BBOX-673] [L]\n[BBOX-674] 1.93\n[BBOX-675] VT\n[BBOX-676] [L]\n[BBOX-677] 0.43\n[BBOX-678] VC MAX\n[BBOX-679] [L]\n[BBOX-680] 3.03\n[BBOX-681] 2.26\n[BBOX-682] 74.6\n[BBOX-683] TLC-SB\n[BBOX-684] [L]\n[BBOX-685] 4.44\n[BBOX-686] 4.10\n[BBOX-687] 92.4\n[BBOX-688] 4.10\n[BBOX-689] RV-SB\n[BBOX-690] [L]\n[BBOX-691] 1.41\n[BBOX-692] 2.18\n[BBOX-693] 154.5\n[BBOX-694] 2.18\n[BBOX-695] RV%TLC-SB\n[BBOX-696] [%]\n[BBOX-697] 31.88\n[BBOX-698] 53.26\n[BBOX-699] 167.1\n[BBOX-700] 53.26\n[BBOX-701] FRC-SB\n[BBOX-702] [L]\n[BBOX-703] 2.51\n[BBOX-704] 2.39\n[BBOX-705] 95.2\n[BBOX-706] 2.39\n[BBOX-707] FRC%TLC-SB\n[BBOX-708] [%]\n[BBOX-709] 51.18\n[BBOX-710] 58.28\n[BBOX-711] 113.9\n[BBOX-712] 58.28\n[BBOX-713] 测试日期\n[BBOX-714] 26/2/0\n[BBOX-715] 意见：\n[BBOX-716] 1.弥散功能在正常范围。\n[BBOX-717] 2.残气量、残总比增高，肺总量在正常范围。\n[BBOX-718] 张\n[BBOX-719] 肺功能试验报告\n[BBOX-720] 姓名：\n[BBOX-721] 年龄：38岁\n[BBOX-722] 性别：女\n[BBOX-723] 科别：\n[BBOX-724] 保险：\n[BBOX-725] 预计值模式：Standard-new\n[BBOX-726] 测试号：2026020017\n[BBOX-727] 身高：166 cm\n[BBOX-728] 体重：60 kg\n[BBOX-729] 备注：\n[BBOX-730] 联系电话：\n[BBOX-731] 操作者：蒋细萍\n[BBOX-732] Pred\n[BBOX-733] A1 A1/Pd\n[BBOX-734] P1 A2/Pd chg%l\n[BBOX-735] P2 A3/Pd chg%2\n[BBOX-736] P3 A4/Pd chg%3\n[BBOX-737] FVC\n[BBOX-738] [L]\n[BBOX-739] 2.99\n[BBOX-740] 2.21\n[BBOX-741] 74.0\n[BBOX-742] 2.63\n[BBOX-743] 87.9\n[BBOX-744] 18.72\n[BBOX-745] 2.04\n[BBOX-746] 88.2\n[BBOX-747] 19.17\n[BBOX-748] 2.67\n[BBOX-749] 86.0\n[BBOX-750] 16.23\n[BBOX-751] FEV 1\n[BBOX-752] [L]\n[BBOX-753] 2.67\n[BBOX-754] 1.25\n[BBOX-755] 48.6\n[BBOX-756] 1.62\n[BBOX-757] 69.2\n[BBOX-758] 21.85\n[BBOX-759] 1.84\n[BBOX-760] 69.8\n[BBOX-761] 23.23\n[BBOX-762] 1.60\n[BBOX-763] 68.4\n[BBOX-764] 20.23\n[BBOX-765] FEV 1 % FVC\n[BBOX-766] [%]\n[BBOX-767] 84.19\n[BBOX-768] 56.48\n[BBOX-769] 67.1\n[BBOX-770] 67.97\n[BBOX-771] 68.9\n[BBOX-772] 2.64\n[BBOX-773] 68.40\n[BBOX-774] 69.4\n[BBOX-775] 3.41\n[BBOX-776] 68.42\n[BBOX-777] 69.4\n[BBOX-778] 3.44\n[BBOX-779] FEV 1 % VC MAX\n[BBOX-780] [%]\n[BBOX-781] 81.88\n[BBOX-782] 65.26\n[BBOX-783] 67.6\n[BBOX-784] 67.97\n[BBOX-785] 70.8\n[BBOX-786] 4.91\n[BBOX-787] 68.40\n[BBOX-788] 71.3\n[BBOX-789] 6.70\n[BBOX-790] 68.42\n[BBOX-791] 71.4\n[BBOX-792] 5.73\n[BBOX-793] VC MAX\n[BBOX-794] [L]\n[BBOX-795] 3.03\n[BBOX-796] 2.26\n[BBOX-797] 74.6\n[BBOX-798] 2.63\n[BBOX-799] 86.6\n[BBOX-800] 16.14\n[BBOX-801] 2.64\n[BBOX-802] 87.0\n[BBOX-803] 16.69\n[BBOX-804] 2.57\n[BBOX-805] 84.8\n[BBOX-806] 13.71\n[BBOX-807] PEF\n[BBOX-808] [L/s]\n[BBOX-809] 6.28\n[BBOX-810] 2.66\n[BBOX-811] 42.4\n[BBOX-812] 2.90\n[BBOX-813] 46.2\n[BBOX-814] 9.17\n[BBOX-815] 3.37\n[BBOX-816] 53.7\n[BBOX-817] 26.79\n[BBOX-818] 3.42\n[BBOX-819] 64.6\n[BBOX-820] 28.64\n[BBOX-821] MMEF 75/25\n[BBOX-822] [L/s]\n[BBOX-823] 3.57\n[BBOX-824] 0.61\n[BBOX-825] 14.4\n[BBOX-826] 0.67\n[BBOX-827] 18.8\n[BBOX-828] 31.03\n[BBOX-829] 0.73\n[BBOX-830] 20.4\n[BBOX-831] 42.01\n[BBOX-832] 0.69\n[BBOX-833] 19.4\n[BBOX-834] 35.02\n[BBOX-835] MEF 50\n[BBOX-836] [L/s]\n[BBOX-837] 4.01\n[BBOX-838] 0.68\n[BBOX-839] 17.0\n[BBOX-840] 0.90\n[BBOX-841] 22.5\n[BBOX-842] 32.75\n[BBOX-843] 0.89\n[BBOX-844] 22.1\n[BBOX-845] 30.15\n[BBOX-846] 0.88\n[BBOX-847] 21.9\n[BBOX-848] 29.17\n[BBOX-849] MEF 25\n[BBOX-850] [L/s]\n[BBOX-851] 1.79\n[BBOX-852] 0.19\n[BBOX-853] 10.5\n[BBOX-854] 0.27\n[BBOX-855] 15.2\n[BBOX-856] 44.16\n[BBOX-857] 0.33\n[BBOX-858] 18.7\n[BBOX-859] 77.66\n[BBOX-860] 0.31\n[BBOX-861] 17.6\n[BBOX-862] 66.49\n[BBOX-863] FET\n[BBOX-864] [s]\n[BBOX-865] 7.63\n[BBOX-866] 8.01\n[BBOX-867] 4.99\n[BBOX-868] 7.79\n[BBOX-869] 2.14\n[BBOX-870] 7.43\n[BBOX-871] -2.60\n[BBOX-872] V backextrapolation ex [L]\n[BBOX-873] 0.05\n[BBOX-874] 0.04\n[BBOX-875] -11.67\n[BBOX-876] 0.04\n[BBOX-877] -18.64\n[BBOX-878] 0.04\n[BBOX-879] -13.51\n[BBOX-880] PIF\n[BBOX-881] [L/s]\n[BBOX-882] 3.04\n[BBOX-883] 3.37\n[BBOX-884] 10.91\n[BBOX-885] 3.51\n[BBOX-886] 15.70\n[BBOX-887] 3.60\n[BBOX-888] 18.67\n[BBOX-889] FIV1\n[BBOX-890] [L]\n[BBOX-891] 2.21\n[BBOX-892] 2.56\n[BBOX-893] 15.71\n[BBOX-894] 2.56\n[BBOX-895] 15.66\n[BBOX-896] 2.50\n[BBOX-897] 13.09\n[BBOX-898] PEF50 % FIF50\n[BBOX-899] [%]\n[BBOX-900] 22.86\n[BBOX-901] 28.15\n[BBOX-902] 23.14\n[BBOX-903] 25.36\n[BBOX-904] 10.95\n[BBOX-905] 27.28\n[BBOX-906] 19.33\n[BBOX-907] MVV\n[BBOX-908] [L/min]\n[BBOX-909] 99.77\n[BBOX-910] 46.21\n[BBOX-911] 46.3\n[BBOX-912] BF MVV\n[BBOX-913] [1/min]\n[BBOX-914] 75.55\n[BBOX-915] 10\n[BBOX-916] Flow [L/s]\n[BBOX-917] F/V ex\n[BBOX-918] 1\n[BBOX-919] 2\n[BBOX-920] 3\n[BBOX-921] 4\n[BBOX-922] 6\n[BBOX-923] 8\n[BBOX-924] 4\n[BBOX-925] 2\n[BBOX-926] 0\n[BBOX-927] Vol [L]\n[BBOX-928] 1\n[BBOX-929] 2\n[BBOX-930] 3\n[BBOX-931] 4\n[BBOX-932] 5\n[BBOX-933] 10\n[BBOX-934] F/V In\n[BBOX-935] Vol%VCmax\n[BBOX-936] 0\n[BBOX-937] 0\n[BBOX-938] Vol [L]\n[BBOX-939] 20\n[BBOX-940] 40\n[BBOX-941] 60\n[BBOX-942] 80\n[BBOX-943] 100\n[BBOX-944] 1\n[BBOX-945] 2\n[BBOX-946] VCmax\n[BBOX-947] 3\n[BBOX-948] 4\n[BBOX-949] 5\n[BBOX-950] 6\n[BBOX-951] Time [s]\n[BBOX-952] 0\n[BBOX-953] 2\n[BBOX-954] 4\n[BBOX-955] 6\n[BBOX-956] 8\n[BBOX-957] 10\n[BBOX-958] 12\n[BBOX-959] 14\n[BBOX-960] 意见：\n[BBOX-961] 1. 中重度阻塞性肺通气功能障碍。\n[BBOX-962] 2. 支气管舒张试验阳性。\n[BBOX-963] (1. 24h内无支气管舒张药物使用史)\n[BBOX-964] (2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)\n[BBOX-965] (3. 检查质量：舒张前：A级；舒张后：A级)\n[BBOX-966] 张四彩\n[BBOX-967] CS 扫描全能王\n[BBOX-968] 3 亿人都在用的扫描 App\n[BBOX-969] 金城大药房\n[BBOX-970] 会员号:\n[BBOX-971] 积分:112550\n[BBOX-972] 本次积分:596.00\n[BBOX-973] 名称\n[BBOX-974] 规格\n[BBOX-975] 数量\n[BBOX-976] 厂家\n[BBOX-977] 批号\n[BBOX-978] 单价\n[BBOX-979] 金额\n[BBOX-980] 1-布地奈德福莫特罗吸入粉雾剂\n[BBOX-981] 320ug:9ug*60吸/支\n[BBOX-982] 2.00\n[BBOX-983] 阿斯利康制药\n[BBOX-984] PKMR\n[BBOX-985] 300.00\n[BBOX-986] 596.00\n[BBOX-987] 运动员慎用!!!\n[BBOX-988] ***重打销售单***\n[BBOX-989] 总计数量:2.00\n[BBOX-990] 应收:600.00\n[BBOX-991] 优惠:4.00\n[BBOX-992] 付款:596.00\n[BBOX-993] 找零:0.00\n[BBOX-994] 销售单号:251210031062\n[BBOX-995] 款台号:2\n[BBOX-996] 日期:2025-12-10\n[BBOX-997] 15:21:53"
  }
]
2026-08-10 12:24:08,057 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:24:08.054+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:24:17,475 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:17,500 INFO     29 [SmartSplitter] SmartSplitter done: 14 chunks from 14 LLM segments (all bbox_id). Types: {'PrescriptionRecord': 2, 'ExaminationReport': 6, 'DischargeRecord': 2, 'AdmissionRecord': 3, 'MedicationRecord': 1}
2026-08-10 12:24:17,510 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 12:24:17,510 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks": "14 items, types={'PrescriptionRecord': 2, 'ExaminationReport': 6, 'DischargeRecord': 2, 'AdmissionRecord': 3, 'MedicationRecord': 1}"}
2026-08-10 12:24:17,510 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 12:24:17,512 INFO     29 [ChunkRouter] Routed 14 chunks into 5 groups: {'chunks_Prescription': 2, 'chunks_Examination': 6, 'chunks_Discharge': 2, 'chunks_Admission': 3, 'chunks_Medication': 1}
2026-08-10 12:24:17,519 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 12:24:17,519 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | ChunkRouter:Router | outputs={"html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks": "14 items, types={'PrescriptionRecord': 2, 'ExaminationReport': 6, 'DischargeRecord': 2, 'AdmissionRecord': 3, 'MedicationRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:24:17,519 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 12:24:17,524 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:17,524 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:24:18,139 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:18,144 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 12:24:18,144 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:24:18,144 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 12:24:18,150 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:18,150 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:24:18,558 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:18,563 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 12:24:18,564 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:24:18,564 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 12:24:18,568 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:18,569 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:24:19,075 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:19,083 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 12:24:19,084 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:24:19,084 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 12:24:19,090 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:24:19,091 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:24:19,091 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 12:24:19,091 INFO     29 [qwen-vl-text] positions(29): [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:24:19,091 INFO     29 [qwen-vl-text] page grouping: [18], lines per page: [29]
2026-08-10 12:24:19,221 INFO     29 [qwen-vl-text] page=18, rect=842x592, img=(2339x1646), dpi=200
2026-08-10 12:24:19,223 INFO     29 [qwen-vl-text] LLM extraction start, text_len=230
2026-08-10 12:24:19,223 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:19,223 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 969, \"bbox_end\": 997, \"encounter_dates\": [\"2025-12-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "金城大药房\n会员号:\n积分:112550\n本次积分:596.00\n名称\n规格\n数量\n厂家\n批号\n单价\n金额\n1-布地奈德福莫特罗吸入粉雾剂\n320ug:9ug*60吸/支\n2.00\n阿斯利康制药\nPKMR\n300.00\n596.00\n运动员慎用!!!\n***重打销售单***\n总计数量:2.00\n应收:600.00\n优惠:4.00\n付款:596.00\n找零:0.00\n销售单号:251210031062\n款台号:2\n日期:2025-12-10\n15:21:53",
    "role": "user"
  }
]
2026-08-10 12:24:21,136 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:21,136 INFO     29 [qwen-vl-text] LLM output (len=432):
{
  "encounter_date": "2025-12-10",
  "pharmacy": "金城大药房",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": "320ug:9ug*60吸/支",
      "dosage": null,
      "quantity": 2.00,
      "unit_price": 300.00,
      "total_price": 596.00,
      "frequency": null,
      "route": null,
      "manufacturer": "阿斯利康制药",
      "approval_number": null
    }
  ],
  "payment_total": 596.00,
  "payment_method": null
}
2026-08-10 12:24:21,137 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-10]
2026-08-10 12:24:21,140 INFO     29 [qwen-vl-text] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1895666, prompt_len=930
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["金城大药房", "会员号:", "积分:112550", "本次积分:596.00", "名称", "规格", "数量", "厂家", "批号", "单价", "金额", "1-布地奈德福莫特罗吸入粉雾剂", "320ug:9ug*60吸/支", "2.00", "阿斯利康制药", "PKMR", "300.00", "596.00", "运动员慎用!!!", "***重打销售单***", "总计数量:2.00", "应收:600.00", "优惠:4.00", "付款:596.00", "找零:0.00", "销售单号:251210031062", "款台号:2", "日期:2025-12-10", "15:21:53"]

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
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord API raw response (len=1508):
[
	{"text": "金城大药房", "bbox": [477, 74, 584, 108]},
	{"text": "会员号:", "bbox": [434, 138, 474, 162]},
	{"text": "积分:112550", "bbox": [433, 170, 514, 194]},
	{"text": "本次积分:596.00", "bbox": [433, 202, 532, 226]},
	{"text": "名称", "bbox": [430, 264, 458, 289]},
	{"text": "规格", "bbox": [429, 297, 457, 322]},
	{"text": "数量", "bbox": [569, 300, 596, 323]},
	{"text": "厂家", "bbox": [428, 332, 456, 357]},
	{"text": "批号", "bbox": [427, 365, 455, 390]},
	{"text": "单价", "bbox": [494, 368, 522, 393]},
	{"text": "金额", "bbox": [562, 367, 589, 390]},
	{"text": "1-布地奈德福莫特罗吸入粉雾剂", "bbox": [427, 434, 614, 461]},
	{"text": "320ug:9ug*60吸/支", "bbox": [425, 471, 542, 499]},
	{"text": "2.00", "bbox": [575, 473, 601, 494]},
	{"text": "阿斯利康制药", "bbox": [425, 506, 507, 532]},
	{"text": "PKMR", "bbox": [424, 543, 462, 564]},
	{"text": "300.00", "bbox": [494, 543, 534, 564]},
	{"text": "596.00", "bbox": [562, 543, 602, 564]},
	{"text": "运动员慎用!!!", "bbox": [423, 575, 523, 601]},
	{"text": "***重打销售单***", "bbox": [469, 649, 573, 674]},
	{"text": "总计数量:2.00", "bbox": [420, 685, 516, 712]},
	{"text": "应收:600.00", "bbox": [419, 721, 503, 750]},
	{"text": "优惠:4.00", "bbox": [532, 721, 602, 749]},
	{"text": "付款:596.00", "bbox": [419, 760, 503, 789]},
	{"text": "找零:0.00", "bbox": [532, 760, 602, 788]},
	{"text": "销售单号:251210031062", "bbox": [418, 843, 580, 872]},
	{"text": "款台号:2", "bbox": [417, 882, 482, 912]},
	{"text": "日期:2025-12-10", "bbox": [417, 925, 537, 954]},
	{"text": "15:21:53", "bbox": [555, 927, 608, 951]}
]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=9.1s
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[0]: text=金城大药房, bbox=[477, 74, 584, 108]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[1]: text=会员号:, bbox=[434, 138, 474, 162]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[2]: text=积分:112550, bbox=[433, 170, 514, 194]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[3]: text=本次积分:596.00, bbox=[433, 202, 532, 226]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[4]: text=名称, bbox=[430, 264, 458, 289]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[5]: text=规格, bbox=[429, 297, 457, 322]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[6]: text=数量, bbox=[569, 300, 596, 323]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[7]: text=厂家, bbox=[428, 332, 456, 357]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[8]: text=批号, bbox=[427, 365, 455, 390]
2026-08-10 12:24:30,230 INFO     29 [qwen-vl-text] coord item[9]: text=单价, bbox=[494, 368, 522, 393]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[10]: text=金额, bbox=[562, 367, 589, 390]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[11]: text=1-布地奈德福莫特罗吸入粉雾剂, bbox=[427, 434, 614, 461]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[12]: text=320ug:9ug*60吸/支, bbox=[425, 471, 542, 499]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[13]: text=2.00, bbox=[575, 473, 601, 494]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[14]: text=阿斯利康制药, bbox=[425, 506, 507, 532]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[15]: text=PKMR, bbox=[424, 543, 462, 564]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[16]: text=300.00, bbox=[494, 543, 534, 564]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[17]: text=596.00, bbox=[562, 543, 602, 564]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[18]: text=运动员慎用!!!, bbox=[423, 575, 523, 601]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[19]: text=***重打销售单***, bbox=[469, 649, 573, 674]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[20]: text=总计数量:2.00, bbox=[420, 685, 516, 712]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[21]: text=应收:600.00, bbox=[419, 721, 503, 750]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[22]: text=优惠:4.00, bbox=[532, 721, 602, 749]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[23]: text=付款:596.00, bbox=[419, 760, 503, 789]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[24]: text=找零:0.00, bbox=[532, 760, 602, 788]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[25]: text=销售单号:251210031062, bbox=[418, 843, 580, 872]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[26]: text=款台号:2, bbox=[417, 882, 482, 912]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[27]: text=日期:2025-12-10, bbox=[417, 925, 537, 954]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] coord item[28]: text=15:21:53, bbox=[555, 927, 608, 951]
2026-08-10 12:24:30,231 INFO     29 [qwen-vl-text] page=18 — 29/29 coords, api_time=9.1s
2026-08-10 12:24:30,232 INFO     29 [qwen-vl-text] new_positions (29):
[[18, 401.5815369873047, 491.6637685546875, 43.840632446289064, 63.98362573242187], [18, 365.3802663574219, 399.0558669433594, 81.75685510253906, 95.9754385986328], [18, 364.53837634277346, 432.7314675292969, 100.71496643066406, 114.9335499267578], [18, 364.53837634277346, 447.8854877929687, 119.67307775878906, 133.89166125488282], [18, 362.0127062988281, 385.58562670898436, 156.40441845703126, 171.2154429321289], [18, 361.1708162841797, 384.74373669433595, 175.95497076416015, 190.76599523925782], [18, 479.0354183349609, 501.76644873046877, 177.73229370117187, 191.35843621826172], [18, 360.3289262695312, 383.9018466796875, 196.69040502929687, 211.50142950439454], [18, 359.4870362548828, 383.05995666503907, 216.24095733642577, 231.05198181152343], [18, 415.8936672363281, 439.46658764648436, 218.01828027343748, 232.82930474853515], [18, 473.14218823242186, 495.8732186279297, 217.4258392944336, 231.05198181152343], [18, 359.4870362548828, 516.9204689941406, 257.11938488769533, 273.1152913208008], [18, 357.8032562255859, 456.30438793945314, 279.0397011108398, 295.6280485229492], [18, 484.0867584228516, 505.97589880371095, 280.22458306884766, 292.6658436279297], [18, 357.8032562255859, 426.8382374267578, 299.77513537597656, 315.1786008300781], [18, 356.9613662109375, 388.95318676757813, 321.6954515991211, 334.1367121582031], [18, 415.8936672363281, 449.5692678222656, 321.6954515991211, 334.1367121582031], [18, 473.14218823242186, 506.81778881835936, 321.6954515991211, 334.1367121582031], [18, 356.11947619628904, 440.3084776611328, 340.65356292724607, 356.05702838134766], [18, 394.8464168701172, 482.4029783935547, 384.49419537353515, 399.3052198486328], [18, 353.59380615234375, 434.41524755859376, 405.82207061767576, 421.8179770507812], [18, 352.75191613769533, 423.47067736816405, 427.1499458618164, 444.3307342529297], [18, 447.8854877929687, 506.81778881835936, 427.1499458618164, 443.73829327392576], [18, 352.75191613769533, 423.47067736816405, 450.25514404296877, 467.435932434082], [18, 447.8854877929687, 506.81778881835936, 450.25514404296877, 466.8434914550781], [18, 351.91002612304686, 488.29620849609375, 499.42774530029294, 516.6085336914063], [18, 351.06813610839845, 405.79098706054685, 522.5329434814453, 540.3061728515625], [18, 351.06813610839845, 452.09493786621096, 548.0079055786133, 565.1886939697265], [18, 467.2489581298828, 511.86912890625, 549.192787536621, 563.4113710327148]]
2026-08-10 12:24:30,232 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=11.1s
2026-08-10 12:24:30,237 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 12:24:30,238 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:Medication | outputs={"chunks": "1 items, types={'MedicationRecord': 1}", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:24:30,238 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 12:24:30,244 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:24:30,245 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:24:30,245 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 12:24:30,245 INFO     29 [qwen-vl-text] positions(25): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:24:30,245 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [25]
2026-08-10 12:24:30,412 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:24:30,414 INFO     29 [qwen-vl-text] LLM extraction start, text_len=269
2026-08-10 12:24:30,414 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:30,414 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 0, \"bbox_end\": 24, \"encounter_dates\": [\"2025-09-30\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "人民医院\nH43120200207, 院区: 舊城院区)\n基本就诊信息\n姓名: 核\n医生: 旅\n挂号单: 25000448502\n医保号: 5200002600000000600637839\n付款: 城乡居民基本医疗 费别: 普通\n门诊号: 2502240221\n社区号:\n门诊就诊:呼吸内科门诊,2025-09-30 14:50\n医嘱\n报告\n已作废\n全部\n处方\n其他\n生效时间\n内容\n用法\n2025-09-30\n孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/\n睡前口服,每天一次,共30天\n14:51\n盒,共10盒,每次10mg",
    "role": "user"
  }
]
2026-08-10 12:24:32,532 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:32,532 INFO     29 [qwen-vl-text] LLM output (len=409):
{
  "encounter_date": "2025-09-30",
  "prescription_type": "门诊处方",
  "prescriber": "旅",
  "department": "呼吸内科门诊",
  "diagnosis": null,
  "items": [
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": "默沙东",
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "每天一次",
      "route": "口服",
      "duration_days": 30,
      "quantity": "10盒",
      "notes": "睡前服用"
    }
  ]
}
2026-08-10 12:24:32,532 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-30]
2026-08-10 12:24:32,537 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1095422, prompt_len=957
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["人民医院", "H43120200207, 院区: 舊城院区)", "基本就诊信息", "姓名: 核", "医生: 旅", "挂号单: 25000448502", "医保号: 5200002600000000600637839", "付款: 城乡居民基本医疗 费别: 普通", "门诊号: 2502240221", "社区号:", "门诊就诊:呼吸内科门诊,2025-09-30 14:50", "医嘱", "报告", "已作废", "全部", "处方", "其他", "生效时间", "内容", "用法", "2025-09-30", "孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/", "睡前口服,每天一次,共30天", "14:51", "盒,共10盒,每次10mg"]

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
2026-08-10 12:24:40,318 INFO     29 [qwen-vl-text] coord API raw response (len=1353):
[
	{"text": "人民医院", "bbox": [7, 45, 92, 68]},
	{"text": "H43120200207, 院区: 舊城院区)", "bbox": [288, 45, 642, 68]},
	{"text": "基本就诊信息", "bbox": [28, 90, 163, 113]},
	{"text": "姓名: 核", "bbox": [30, 124, 107, 147]},
	{"text": "医生: 旅", "bbox": [270, 124, 347, 147]},
	{"text": "挂号单: 25000448502", "bbox": [432, 124, 632, 145]},
	{"text": "医保号: 5200002600000000600637839", "bbox": [653, 124, 997, 145]},
	{"text": "付款: 城乡居民基本医疗 费别: 普通", "bbox": [31, 152, 370, 175]},
	{"text": "门诊号: 2502240221", "bbox": [432, 152, 618, 175]},
	{"text": "社区号:", "bbox": [652, 152, 725, 175]},
	{"text": "门诊就诊:呼吸内科门诊,2025-09-30 14:50", "bbox": [40, 212, 462, 235]},
	{"text": "医嘱", "bbox": [14, 252, 75, 275]},
	{"text": "报告", "bbox": [109, 252, 170, 275]},
	{"text": "已作废", "bbox": [37, 296, 104, 319]},
	{"text": "全部", "bbox": [161, 296, 205, 319]},
	{"text": "处方", "bbox": [251, 296, 298, 319]},
	{"text": "其他", "bbox": [345, 296, 392, 319]},
	{"text": "生效时间", "bbox": [54, 334, 142, 357]},
	{"text": "内容", "bbox": [417, 334, 462, 357]},
	{"text": "用法", "bbox": [853, 334, 897, 357]},
	{"text": "2025-09-30", "bbox": [35, 364, 145, 382]},
	{"text": "孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/", "bbox": [195, 362, 673, 385]},
	{"text": "睡前口服,每天一次,共30天", "bbox": [731, 372, 985, 395]},
	{"text": "14:51", "bbox": [37, 385, 90, 403]},
	{"text": "盒,共10盒,每次10mg", "bbox": [195, 385, 401, 407]}
]
2026-08-10 12:24:40,318 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=7.8s
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[0]: text=人民医院, bbox=[7, 45, 92, 68]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[1]: text=H43120200207, 院区: 舊城院区), bbox=[288, 45, 642, 68]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[2]: text=基本就诊信息, bbox=[28, 90, 163, 113]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[3]: text=姓名: 核, bbox=[30, 124, 107, 147]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[4]: text=医生: 旅, bbox=[270, 124, 347, 147]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[5]: text=挂号单: 25000448502, bbox=[432, 124, 632, 145]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[6]: text=医保号: 5200002600000000600637839, bbox=[653, 124, 997, 145]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[7]: text=付款: 城乡居民基本医疗 费别: 普通, bbox=[31, 152, 370, 175]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[8]: text=门诊号: 2502240221, bbox=[432, 152, 618, 175]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[9]: text=社区号:, bbox=[652, 152, 725, 175]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[10]: text=门诊就诊:呼吸内科门诊,2025-09-30 14:50, bbox=[40, 212, 462, 235]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[11]: text=医嘱, bbox=[14, 252, 75, 275]
2026-08-10 12:24:40,319 INFO     29 [qwen-vl-text] coord item[12]: text=报告, bbox=[109, 252, 170, 275]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[13]: text=已作废, bbox=[37, 296, 104, 319]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[14]: text=全部, bbox=[161, 296, 205, 319]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[15]: text=处方, bbox=[251, 296, 298, 319]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[16]: text=其他, bbox=[345, 296, 392, 319]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[17]: text=生效时间, bbox=[54, 334, 142, 357]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[18]: text=内容, bbox=[417, 334, 462, 357]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[19]: text=用法, bbox=[853, 334, 897, 357]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[20]: text=2025-09-30, bbox=[35, 364, 145, 382]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[21]: text=孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/, bbox=[195, 362, 673, 385]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[22]: text=睡前口服,每天一次,共30天, bbox=[731, 372, 985, 395]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[23]: text=14:51, bbox=[37, 385, 90, 403]
2026-08-10 12:24:40,320 INFO     29 [qwen-vl-text] coord item[24]: text=盒,共10盒,每次10mg, bbox=[195, 385, 401, 407]
2026-08-10 12:24:40,321 INFO     29 [qwen-vl-text] page=0 — 25/25 coords, api_time=7.8s
2026-08-10 12:24:40,321 INFO     29 [qwen-vl-text] new_positions (25):
[[0, 5.894, 77.464, 26.775, 40.46], [0, 242.49599999999998, 540.564, 26.775, 40.46], [0, 23.576, 137.246, 53.55, 67.235], [0, 25.259999999999998, 90.094, 73.78, 87.46499999999999], [0, 227.34, 292.174, 73.78, 87.46499999999999], [0, 363.74399999999997, 532.144, 73.78, 86.27499999999999], [0, 549.826, 839.4739999999999, 73.78, 86.27499999999999], [0, 26.102, 311.53999999999996, 90.44, 104.125], [0, 363.74399999999997, 520.356, 90.44, 104.125], [0, 548.984, 610.4499999999999, 90.44, 104.125], [0, 33.68, 389.00399999999996, 126.14, 139.825], [0, 11.788, 63.15, 149.94, 163.625], [0, 91.77799999999999, 143.14, 149.94, 163.625], [0, 31.154, 87.568, 176.12, 189.80499999999998], [0, 135.56199999999998, 172.60999999999999, 176.12, 189.80499999999998], [0, 211.34199999999998, 250.916, 176.12, 189.80499999999998], [0, 290.49, 330.06399999999996, 176.12, 189.80499999999998], [0, 45.467999999999996, 119.564, 198.73, 212.415], [0, 351.114, 389.00399999999996, 198.73, 212.415], [0, 718.226, 755.274, 198.73, 212.415], [0, 29.47, 122.08999999999999, 216.57999999999998, 227.29], [0, 164.19, 566.6659999999999, 215.39, 229.075], [0, 615.502, 829.37, 221.34, 235.02499999999998], [0, 31.154, 75.78, 229.075, 239.785], [0, 164.19, 337.642, 229.075, 242.165]]
2026-08-10 12:24:40,321 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=10.1s
2026-08-10 12:24:40,321 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:24:40,324 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:24:40,324 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 12:24:40,324 INFO     29 [qwen-vl-text] positions(28): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:24:40,324 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [28]
2026-08-10 12:24:40,486 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:24:40,488 INFO     29 [qwen-vl-text] LLM extraction start, text_len=373
2026-08-10 12:24:40,488 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:40,488 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 25, \"bbox_end\": 52, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"怀化市刘仁水介入呼吸病学工作室\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "基本就诊信息\n姓名：杨\n医生：\n挂号单：26000068319\n医保号：52000026000000006006378395\n付款：城乡居民基本医疗 费别：普通\n门诊号：2502240221\n社区号：\n门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04\n医嘱|报告|\n已作废|全部|处方|其他\n生效时间\n内容\n用法\n2026-02-09\n肺功能全套+支气管舒张试验,共1次\n2026-02-09\n(基)硫酸沙丁胺醇吸入气雾剂 (山东)\n吸入,一次,共1天\n11:08\n100ug*200揿/瓶,共1瓶,每次400ug\n2026-02-09\n呼出气一氧化氮测定,共1次\n2026-02-09\n沙美特罗替卡松粉吸入剂(法国GLAXO)\n吸入,每天二次,共1天\n12.33\n50ug/500ug*60吸/瓶,共1瓶,每次50ug",
    "role": "user"
  }
]
2026-08-10 12:24:40,490 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:24:40.490+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:24:43,503 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:43,503 INFO     29 [qwen-vl-text] LLM output (len=699):
{
  "encounter_date": "2026-02-09",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "怀化市刘仁水介入呼吸病学工作室",
  "diagnosis": null,
  "items": [
    {
      "drug_generic_name": "硫酸沙丁胺醇吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "400ug",
      "frequency": "一次",
      "route": "吸入",
      "duration_days": 1,
      "quantity": "1瓶",
      "notes": "100ug*200揿/瓶"
    },
    {
      "drug_generic_name": "沙美特罗替卡松粉吸入剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "50ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": 1,
      "quantity": "1瓶",
      "notes": "50ug/500ug*60吸/瓶"
    }
  ]
}
2026-08-10 12:24:43,503 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-09]
2026-08-10 12:24:43,506 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1192752, prompt_len=1070
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["基本就诊信息", "姓名：杨", "医生：", "挂号单：26000068319", "医保号：52000026000000006006378395", "付款：城乡居民基本医疗 费别：普通", "门诊号：2502240221", "社区号：", "门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04", "医嘱|报告|", "已作废|全部|处方|其他", "生效时间", "内容", "用法", "2026-02-09", "肺功能全套+支气管舒张试验,共1次", "2026-02-09", "(基)硫酸沙丁胺醇吸入气雾剂 (山东)", "吸入,一次,共1天", "11:08", "100ug*200揿/瓶,共1瓶,每次400ug", "2026-02-09", "呼出气一氧化氮测定,共1次", "2026-02-09", "沙美特罗替卡松粉吸入剂(法国GLAXO)", "吸入,每天二次,共1天", "12.33", "50ug/500ug*60吸/瓶,共1瓶,每次50ug"]

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
2026-08-10 12:24:52,746 INFO     29 [qwen-vl-text] coord API raw response (len=1595):
[
	{"text": "基本就诊信息", "bbox": [44, 284, 169, 306]},
	{"text": "姓名：杨", "bbox": [45, 315, 120, 337]},
	{"text": "医生：", "bbox": [270, 315, 337, 337]},
	{"text": "挂号单：26000068319", "bbox": [425, 315, 619, 337]},
	{"text": "医保号：52000026000000006006378395", "bbox": [639, 315, 994, 337]},
	{"text": "付款：城乡居民基本医疗 费别：普通", "bbox": [45, 341, 365, 363]},
	{"text": "门诊号：2502240221", "bbox": [424, 341, 606, 363]},
	{"text": "社区号：", "bbox": [638, 341, 712, 363]},
	{"text": "门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04", "bbox": [52, 392, 647, 413]},
	{"text": "医嘱|报告|", "bbox": [28, 426, 195, 449]},
	{"text": "已作废|全部|处方|其他", "bbox": [17, 463, 388, 486]},
	{"text": "生效时间", "bbox": [65, 498, 149, 519]},
	{"text": "内容", "bbox": [410, 498, 453, 519]},
	{"text": "用法", "bbox": [844, 498, 887, 519]},
	{"text": "2026-02-09", "bbox": [48, 525, 152, 541]},
	{"text": "肺功能全套+支气管舒张试验,共1次", "bbox": [200, 523, 530, 545]},
	{"text": "2026-02-09", "bbox": [48, 550, 152, 567]},
	{"text": "(基)硫酸沙丁胺醇吸入气雾剂 (山东)", "bbox": [201, 548, 571, 569]},
	{"text": "吸入,一次,共1天", "bbox": [720, 556, 883, 578]},
	{"text": "11:08", "bbox": [50, 568, 102, 584]},
	{"text": "100ug*200揿/瓶,共1瓶,每次400ug", "bbox": [200, 567, 521, 587]},
	{"text": "2026-02-09", "bbox": [48, 591, 152, 607]},
	{"text": "呼出气一氧化氮测定,共1次", "bbox": [200, 590, 457, 610]},
	{"text": "2026-02-09", "bbox": [48, 616, 152, 632]},
	{"text": "沙美特罗替卡松粉吸入剂(法国GLAXO)", "bbox": [200, 614, 551, 635]},
	{"text": "吸入,每天二次,共1天", "bbox": [720, 622, 924, 644]},
	{"text": "12.33", "bbox": [50, 634, 102, 650]},
	{"text": "50ug/500ug*60吸/瓶,共1瓶,每次50ug", "bbox": [200, 633, 553, 653]}
]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=9.2s
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[0]: text=基本就诊信息, bbox=[44, 284, 169, 306]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：杨, bbox=[45, 315, 120, 337]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[2]: text=医生：, bbox=[270, 315, 337, 337]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[3]: text=挂号单：26000068319, bbox=[425, 315, 619, 337]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[4]: text=医保号：52000026000000006006378395, bbox=[639, 315, 994, 337]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[5]: text=付款：城乡居民基本医疗 费别：普通, bbox=[45, 341, 365, 363]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[6]: text=门诊号：2502240221, bbox=[424, 341, 606, 363]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[7]: text=社区号：, bbox=[638, 341, 712, 363]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[8]: text=门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04, bbox=[52, 392, 647, 413]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[9]: text=医嘱|报告|, bbox=[28, 426, 195, 449]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[10]: text=已作废|全部|处方|其他, bbox=[17, 463, 388, 486]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[11]: text=生效时间, bbox=[65, 498, 149, 519]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[12]: text=内容, bbox=[410, 498, 453, 519]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[13]: text=用法, bbox=[844, 498, 887, 519]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[14]: text=2026-02-09, bbox=[48, 525, 152, 541]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[15]: text=肺功能全套+支气管舒张试验,共1次, bbox=[200, 523, 530, 545]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[16]: text=2026-02-09, bbox=[48, 550, 152, 567]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[17]: text=(基)硫酸沙丁胺醇吸入气雾剂 (山东), bbox=[201, 548, 571, 569]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[18]: text=吸入,一次,共1天, bbox=[720, 556, 883, 578]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[19]: text=11:08, bbox=[50, 568, 102, 584]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[20]: text=100ug*200揿/瓶,共1瓶,每次400ug, bbox=[200, 567, 521, 587]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[21]: text=2026-02-09, bbox=[48, 591, 152, 607]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[22]: text=呼出气一氧化氮测定,共1次, bbox=[200, 590, 457, 610]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[23]: text=2026-02-09, bbox=[48, 616, 152, 632]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[24]: text=沙美特罗替卡松粉吸入剂(法国GLAXO), bbox=[200, 614, 551, 635]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[25]: text=吸入,每天二次,共1天, bbox=[720, 622, 924, 644]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[26]: text=12.33, bbox=[50, 634, 102, 650]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] coord item[27]: text=50ug/500ug*60吸/瓶,共1瓶,每次50ug, bbox=[200, 633, 553, 653]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] page=1 — 28/28 coords, api_time=9.2s
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] new_positions (28):
[[1, 37.048, 142.298, 168.98, 182.07], [1, 37.89, 101.03999999999999, 187.42499999999998, 200.515], [1, 227.34, 283.75399999999996, 187.42499999999998, 200.515], [1, 357.84999999999997, 521.198, 187.42499999999998, 200.515], [1, 538.038, 836.948, 187.42499999999998, 200.515], [1, 37.89, 307.33, 202.89499999999998, 215.98499999999999], [1, 357.008, 510.252, 202.89499999999998, 215.98499999999999], [1, 537.196, 599.504, 202.89499999999998, 215.98499999999999], [1, 43.784, 544.774, 233.23999999999998, 245.73499999999999], [1, 23.576, 164.19, 253.47, 267.155], [1, 14.314, 326.69599999999997, 275.485, 289.16999999999996], [1, 54.73, 125.458, 296.31, 308.805], [1, 345.21999999999997, 381.426, 296.31, 308.805], [1, 710.648, 746.8539999999999, 296.31, 308.805], [1, 40.416, 127.984, 312.375, 321.895], [1, 168.4, 446.26, 311.185, 324.275], [1, 40.416, 127.984, 327.25, 337.365], [1, 169.242, 480.782, 326.06, 338.555], [1, 606.24, 743.486, 330.82, 343.90999999999997], [1, 42.1, 85.884, 337.96, 347.47999999999996], [1, 168.4, 438.68199999999996, 337.365, 349.265], [1, 40.416, 127.984, 351.645, 361.16499999999996], [1, 168.4, 384.794, 351.05, 362.95], [1, 40.416, 127.984, 366.52, 376.03999999999996], [1, 168.4, 463.942, 365.33, 377.825], [1, 606.24, 778.0079999999999, 370.09, 383.18], [1, 42.1, 85.884, 377.22999999999996, 386.75], [1, 168.4, 465.626, 376.635, 388.53499999999997]]
2026-08-10 12:24:52,747 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=12.4s
2026-08-10 12:24:52,759 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 12:24:52,760 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:Prescription | outputs={"chunks": "2 items, types={'PrescriptionRecord': 2}", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:24:52,760 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 12:24:52,764 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:24:52,765 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:24:52,765 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 12:24:52,766 INFO     29 [qwen-vl-text] positions(36): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:24:52,766 INFO     29 [qwen-vl-text] page grouping: [5, 6], lines per page: [35, 1]
2026-08-10 12:24:53,025 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:24:53,303 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:24:53,306 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1106
2026-08-10 12:24:53,306 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:24:53,308 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 103, \"bbox_end\": 138, \"encounter_dates\": [\"2025-07-11\", \"2025-07-22\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "HUAIHUA CENTRAL HOSPITAL\n怀化市肿瘤医院\n姓名：\n性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n221028180\n3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总\n神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓\n浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经\n(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞\n<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌\n(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支\n持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司\n特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前\n好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。\n出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发\n热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，\nBP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。\n心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。\n出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧\n段结节（LU-RADS 2类）。\n出院医嘱：\n1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生\n活习惯，增强体质，适当运动，加强营养；\n2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复\n查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；\n3.出院后继续服用中药。\n4.出院带药：\n舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱\n口，根据动态复查肺功能结果，调整用药）\n祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次\n抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次\n5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；\n6.如有不适，随时医院就诊，我科随诊。\n科室护士办公室电话：0745-2329117。主管医师电话：13789357317\n医师签名：主治医师\nzz1028180",
    "role": "user"
  }
]
2026-08-10 12:25:04,971 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:25:04,971 INFO     29 [qwen-vl-text] LLM output (len=2071):
{
  "encounter_date": null,
  "admission_date": null,
  "discharge_date": null,
  "hospital_days": null,
  "department": "呼吸与危重症医学科",
  "bed_number": "42",
  "admission_condition": null,
  "admission_diagnoses": [],
  "treatment_summary": "入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。",
  "auxiliary_exams": "神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞 <10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌(TB-DNA)定性、细菌及真菌培养均阴性。",
  "imaging_findings": null,
  "discharge_diagnoses": [
    {
      "name": "支气管哮喘急性发作期 IgE介导",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺炎（CURB-65 0分）",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肺中叶内侧段结节（LU-RADS 2类）",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。",
  "outcome": "好转",
  "discharge_orders": "1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生活习惯，增强体质，适当运动，加强营养；2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；3.出院后继续服用中药。4.出院带药：舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱口，根据动态复查肺功能结果，调整用药）祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；6.如有不适，随时医院就诊，我科随诊。",
  "do_medications": [
    "布地奈德福莫特罗吸入粉雾剂 320ug 每天2次",
    "乙酰半胱氨酸片 0.6g 每天2次",
    "孟鲁司特钠片 10mg 每晚1次"
  ],
  "do_follow_up": "2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；定期复查神经传导速度，神经内科、风湿免疫科门诊随诊",
  "do_precautions": [
    "注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生活习惯，增强体质，适当运动，加强营养",
    "出院后继续服用中药",
    "如有不适，随时医院就诊"
  ],
  "next_treatment_date": null,
  "attending_physician": "张田慧",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 12:25:04,977 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1391013, prompt_len=1814
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "221028180", "3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总", "神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓", "浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经", "(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞", "<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌", "(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支", "持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司", "特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前", "好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。", "出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发", "热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，", "BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。", "心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧", "段结节（LU-RADS 2类）。", "出院医嘱：", "1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生", "活习惯，增强体质，适当运动，加强营养；", "2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复", "查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；", "3.出院后继续服用中药。", "4.出院带药：", "舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱", "口，根据动态复查肺功能结果，调整用药）", "祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次", "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次", "5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；", "6.如有不适，随时医院就诊，我科随诊。", "科室护士办公室电话：0745-2329117。主管医师电话：13789357317", "医师签名：主治医师"]

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
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord API raw response (len=2629):
[
	{"text": "HUAIHUA CENTRAL HOSPITAL", "bbox": [282, 10, 444, 23]},
	{"text": "怀化市肿瘤医院", "bbox": [282, 24, 444, 39]},
	{"text": "姓名：", "bbox": [188, 59, 226, 77]},
	{"text": "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "bbox": [289, 60, 757, 78]},
	{"text": "221028180", "bbox": [188, 77, 259, 92]},
	{"text": "3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总", "bbox": [188, 102, 805, 120]},
	{"text": "神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓", "bbox": [188, 128, 805, 146]},
	{"text": "浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经", "bbox": [188, 154, 805, 172]},
	{"text": "(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞", "bbox": [194, 180, 759, 199]},
	{"text": "<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌", "bbox": [190, 207, 798, 225]},
	{"text": "(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支", "bbox": [190, 233, 805, 252]},
	{"text": "持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司", "bbox": [188, 260, 798, 278]},
	{"text": "特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前", "bbox": [188, 286, 805, 304]},
	{"text": "好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。", "bbox": [188, 313, 646, 331]},
	{"text": "出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发", "bbox": [205, 340, 805, 358]},
	{"text": "热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，", "bbox": [188, 366, 744, 384]},
	{"text": "BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。", "bbox": [188, 392, 805, 410]},
	{"text": "心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "bbox": [188, 418, 776, 437]},
	{"text": "出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧", "bbox": [188, 445, 805, 463]},
	{"text": "段结节（LU-RADS 2类）。", "bbox": [188, 471, 361, 489]},
	{"text": "出院医嘱：", "bbox": [205, 498, 272, 516]},
	{"text": "1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生", "bbox": [213, 524, 800, 543]},
	{"text": "活习惯，增强体质，适当运动，加强营养；", "bbox": [188, 550, 475, 569]},
	{"text": "2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复", "bbox": [213, 577, 800, 595]},
	{"text": "查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；", "bbox": [188, 603, 660, 621]},
	{"text": "3.出院后继续服用中药。", "bbox": [213, 630, 377, 648]},
	{"text": "4.出院带药：", "bbox": [213, 656, 296, 674]},
	{"text": "舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱", "bbox": [213, 683, 807, 701]},
	{"text": "口，根据动态复查肺功能结果，调整用药）", "bbox": [188, 709, 478, 727]},
	{"text": "祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次", "bbox": [259, 735, 647, 754]},
	{"text": "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次", "bbox": [213, 762, 647, 780]},
	{"text": "5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；", "bbox": [213, 788, 622, 806]},
	{"text": "6.如有不适，随时医院就诊，我科随诊。", "bbox": [213, 815, 488, 833]},
	{"text": "科室护士办公室电话：0745-2329117。主管医师电话：13789357317", "bbox": [188, 841, 648, 859]},
	{"text": "医师签名：主治医师", "bbox": [519, 867, 660, 886]}
]
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=14.4s
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord item[0]: text=HUAIHUA CENTRAL HOSPITAL, bbox=[282, 10, 444, 23]
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord item[1]: text=怀化市肿瘤医院, bbox=[282, 24, 444, 39]
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[188, 59, 226, 77]
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：, bbox=[289, 60, 757, 78]
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord item[4]: text=221028180, bbox=[188, 77, 259, 92]
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord item[5]: text=3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总, bbox=[188, 102, 805, 120]
2026-08-10 12:25:19,354 INFO     29 [qwen-vl-text] coord item[6]: text=神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓, bbox=[188, 128, 805, 146]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[7]: text=浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经, bbox=[188, 154, 805, 172]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[8]: text=(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞, bbox=[194, 180, 759, 199]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[9]: text=<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌, bbox=[190, 207, 798, 225]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[10]: text=(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支, bbox=[190, 233, 805, 252]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[11]: text=持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司, bbox=[188, 260, 798, 278]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[12]: text=特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前, bbox=[188, 286, 805, 304]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[13]: text=好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。, bbox=[188, 313, 646, 331]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[14]: text=出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发, bbox=[205, 340, 805, 358]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[15]: text=热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，, bbox=[188, 366, 744, 384]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[16]: text=BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。, bbox=[188, 392, 805, 410]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[17]: text=心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。, bbox=[188, 418, 776, 437]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[18]: text=出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧, bbox=[188, 445, 805, 463]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[19]: text=段结节（LU-RADS 2类）。, bbox=[188, 471, 361, 489]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[20]: text=出院医嘱：, bbox=[205, 498, 272, 516]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[21]: text=1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生, bbox=[213, 524, 800, 543]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[22]: text=活习惯，增强体质，适当运动，加强营养；, bbox=[188, 550, 475, 569]
2026-08-10 12:25:19,355 INFO     29 [qwen-vl-text] coord item[23]: text=2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复, bbox=[213, 577, 800, 595]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[24]: text=查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；, bbox=[188, 603, 660, 621]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[25]: text=3.出院后继续服用中药。, bbox=[213, 630, 377, 648]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[26]: text=4.出院带药：, bbox=[213, 656, 296, 674]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[27]: text=舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱, bbox=[213, 683, 807, 701]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[28]: text=口，根据动态复查肺功能结果，调整用药）, bbox=[188, 709, 478, 727]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[29]: text=祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次, bbox=[259, 735, 647, 754]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[30]: text=抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次, bbox=[213, 762, 647, 780]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[31]: text=5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；, bbox=[213, 788, 622, 806]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[32]: text=6.如有不适，随时医院就诊，我科随诊。, bbox=[213, 815, 488, 833]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[33]: text=科室护士办公室电话：0745-2329117。主管医师电话：13789357317, bbox=[188, 841, 648, 859]
2026-08-10 12:25:19,356 INFO     29 [qwen-vl-text] coord item[34]: text=医师签名：主治医师, bbox=[519, 867, 660, 886]
2026-08-10 12:25:19,357 INFO     29 [qwen-vl-text] page=5 — 35/35 coords, api_time=14.4s
2026-08-10 12:25:19,361 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1584125, prompt_len=624
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["zz1028180"]

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
2026-08-10 12:25:20,833 INFO     29 [qwen-vl-text] coord API raw response (len=66):
```json
[
	{"text": "zz1028180", "bbox": [171, 34, 246, 52]}
]
```
2026-08-10 12:25:20,834 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 12:25:20,834 INFO     29 [qwen-vl-text] coord item[0]: text=zz1028180, bbox=[171, 34, 246, 52]
2026-08-10 12:25:20,835 INFO     29 [qwen-vl-text] page=6 — 1/1 coords, api_time=1.5s
2026-08-10 12:25:20,836 INFO     29 [qwen-vl-text] new_positions (36):
[[5, 237.444, 373.848, 5.949999999999999, 13.684999999999999], [5, 237.444, 373.848, 14.28, 23.205], [5, 158.296, 190.292, 35.105, 45.815], [5, 243.338, 637.394, 35.699999999999996, 46.41], [5, 158.296, 218.078, 45.815, 54.739999999999995], [5, 158.296, 677.81, 60.69, 71.39999999999999], [5, 158.296, 677.81, 76.16, 86.86999999999999], [5, 158.296, 677.81, 91.63, 102.33999999999999], [5, 163.34799999999998, 639.078, 107.1, 118.405], [5, 159.98, 671.9159999999999, 123.16499999999999, 133.875], [5, 159.98, 677.81, 138.635, 149.94], [5, 158.296, 671.9159999999999, 154.7, 165.41], [5, 158.296, 677.81, 170.17, 180.88], [5, 158.296, 543.932, 186.23499999999999, 196.945], [5, 172.60999999999999, 677.81, 202.29999999999998, 213.01], [5, 158.296, 626.448, 217.76999999999998, 228.48], [5, 158.296, 677.81, 233.23999999999998, 243.95], [5, 158.296, 653.3919999999999, 248.70999999999998, 260.015], [5, 158.296, 677.81, 264.775, 275.485], [5, 158.296, 303.962, 280.245, 290.955], [5, 172.60999999999999, 229.024, 296.31, 307.02], [5, 179.346, 673.6, 311.78, 323.085], [5, 158.296, 399.95, 327.25, 338.555], [5, 179.346, 673.6, 343.315, 354.025], [5, 158.296, 555.72, 358.78499999999997, 369.495], [5, 179.346, 317.43399999999997, 374.84999999999997, 385.56], [5, 179.346, 249.232, 390.32, 401.03], [5, 179.346, 679.494, 406.385, 417.09499999999997], [5, 158.296, 402.476, 421.85499999999996, 432.565], [5, 218.078, 544.774, 437.325, 448.63], [5, 179.346, 544.774, 453.39, 464.09999999999997], [5, 179.346, 523.7239999999999, 468.85999999999996, 479.57], [5, 179.346, 410.89599999999996, 484.92499999999995, 495.635], [5, 158.296, 545.616, 500.395, 511.10499999999996], [5, 436.998, 555.72, 515.865, 527.17], [6, 143.982, 207.132, 20.23, 30.939999999999998]]
2026-08-10 12:25:20,836 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=2, time=28.1s
2026-08-10 12:25:20,836 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:25:20,838 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:25:20,838 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 12:25:20,838 INFO     29 [qwen-vl-text] positions(69): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:25:20,839 INFO     29 [qwen-vl-text] page grouping: [8, 9, 10], lines per page: [21, 33, 15]
2026-08-10 12:25:21,099 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:25:21,424 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:25:21,616 INFO     29 [qwen-vl-text] page=10, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:25:21,618 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2701
2026-08-10 12:25:21,618 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:25:21,618 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 194, \"bbox_end\": 262, \"encounter_dates\": [\"2025-02-24\", \"2025-03-01\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "221028180\n第2次入院记录\n姓名：\n性别：女\n年龄：37岁\n婚姻：已婚\n入院时间：2025-07-11 08:57\n入院方式：步行\n主诉：反复胸闷、气促8年，加重1月。\n现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。\n出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。\n既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。\n病史陈述者签名：\n体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。\n出生地：贵州省天柱县\n民族：苗族\n职业：农民\n住址：贵州省天柱县远口镇大祥村白蜡树脚组\n记录时间：2025-07-11 14:36\nCS 扫描全能王\n3亿人都在用的扫描App\n出院记录\n入院时间：2025-02-24 12:22\n出院时间：2025-03-01 10:00\n住院天数：5天\n记录时间：2025-02-28 20:39\n入院诊断：胸闷、气促查因：支气管哮喘可能性大\n入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。\n体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸\n氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89\n次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。\n诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C\n+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、\n肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体\n测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。\n心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1\n0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范\n围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO\n2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球\n菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、\n两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，\nLU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能\n结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、\n抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者\n及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。\n出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶\n心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，\nBP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心\n率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。\n出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：\n功能性消化不良？反流性食管炎？其他。\n出院医嘱：\n（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺\n激性烟雾及吸入二手烟；\n姓名：\n性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n220999152\n(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；\n(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；\n(4) 继续用药：\n舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服\n布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入\n(吸入后漱口，根据动态复查肺功能结果，调整用药)\n抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服\n止咳祛痰：润肺膏 每次15g 每天2次，口服\n调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服\n(5) 如有不适，随时医院就诊，我科随诊。\n科室电话：0745-2329117 主管医师电话：13789357317\n医师签名：主治医师：",
    "role": "user"
  }
]
2026-08-10 12:25:21,620 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:25:21.619+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:25:39,211 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:25:39,211 INFO     29 [qwen-vl-text] LLM output (len=3130):
{
  "encounter_date": "2025-03-01",
  "admission_date": "2025-02-24",
  "discharge_date": "2025-03-01",
  "hospital_days": 5,
  "department": "呼吸与危重症医学科",
  "bed_number": "46",
  "admission_condition": "青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。",
  "admission_diagnoses": [
    {
      "name": "胸闷、气促查因：支气管哮喘可能性大",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C +3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO 2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。",
  "auxiliary_exams": "尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C +3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO 2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、两次抗酸染色、TB-DNA均阴性。",
  "imaging_findings": "心电图：1.窦性心律 2.正常心电图。胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。",
  "discharge_diagnoses": [
    {
      "name": "支气管哮喘急性发作期",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肺中叶内侧段结节，LU-RADS 2类",
      "diagnosis_type": "西医"
    },
    {
      "name": "腹胀查因：功能性消化不良？反流性食管炎？其他",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。",
  "outcome": "好转",
  "discharge_orders": "（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺激性烟雾及吸入二手烟；(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；(4) 继续用药：舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服；布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入(吸入后漱口，根据动态复查肺功能结果，调整用药)；抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服；止咳祛痰：润肺膏 每次15g 每天2次，口服；调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服；(5) 如有不适，随时医院就诊，我科随诊。",
  "do_medications": [
    "复方甲氧那明胶囊 每次2粒 每天3次",
    "布地奈德福莫特罗吸入粉雾剂 每次320ug 每天1次",
    "孟鲁司特钠片 每次10mg 每晚1次",
    "润肺膏 每次15g 每天2次",
    "马来酸曲美布汀片 每次0.1g 每天3次"
  ],
  "do_follow_up": "3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；如有不适，随时医院就诊，我科随诊。",
  "do_precautions": [
    "避免接触一切可能过敏源",
    "注意保暖",
    "避免感冒受凉",
    "避免剧烈运动",
    "避免接触刺激性烟雾及吸入二手烟"
  ],
  "next_treatment_date": null,
  "attending_physician": "刘仁水",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": 36.6,
  "vs_pulse_bpm": 89,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 129,
  "vs_diastolic_bp_mmhg": 90
}
2026-08-10 12:25:39,211 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-01]
2026-08-10 12:25:39,214 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1474463, prompt_len=1777
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["221028180", "第2次入院记录", "姓名：", "性别：女", "年龄：37岁", "婚姻：已婚", "入院时间：2025-07-11 08:57", "入院方式：步行", "主诉：反复胸闷、气促8年，加重1月。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "病史陈述者签名：", "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。", "出生地：贵州省天柱县", "民族：苗族", "职业：农民", "住址：贵州省天柱县远口镇大祥村白蜡树脚组", "记录时间：2025-07-11 14:36", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 12:25:51,191 INFO     29 [qwen-vl-text] coord API raw response (len=2022):
[
	{"text": "221028180", "bbox": [186, 17, 258, 32]},
	{"text": "第2次入院记录", "bbox": [439, 47, 567, 67]},
	{"text": "姓名：", "bbox": [185, 85, 230, 104]},
	{"text": "性别：女", "bbox": [185, 112, 249, 131]},
	{"text": "年龄：37岁", "bbox": [185, 138, 263, 157]},
	{"text": "婚姻：已婚", "bbox": [185, 165, 266, 184]},
	{"text": "入院时间：2025-07-11 08:57", "bbox": [185, 191, 391, 210]},
	{"text": "入院方式：步行", "bbox": [185, 217, 298, 236]},
	{"text": "主诉：反复胸闷、气促8年，加重1月。", "bbox": [185, 243, 447, 262]},
	{"text": "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "bbox": [185, 270, 813, 471]},
	{"text": "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "bbox": [185, 479, 815, 630]},
	{"text": "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "bbox": [185, 637, 633, 656]},
	{"text": "病史陈述者签名：", "bbox": [185, 664, 303, 683]},
	{"text": "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。", "bbox": [185, 690, 817, 893]},
	{"text": "出生地：贵州省天柱县", "bbox": [454, 85, 612, 104]},
	{"text": "民族：苗族", "bbox": [454, 112, 534, 131]},
	{"text": "职业：农民", "bbox": [454, 138, 534, 157]},
	{"text": "住址：贵州省天柱县远口镇大祥村白蜡树脚组", "bbox": [454, 165, 767, 184]},
	{"text": "记录时间：2025-07-11 14:36", "bbox": [454, 191, 661, 210]},
	{"text": "CS 扫描全能王", "bbox": [903, 942, 983, 963]},
	{"text": "3亿人都在用的扫描App", "bbox": [903, 970, 983, 981]}
]
2026-08-10 12:25:51,192 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=12.0s
2026-08-10 12:25:51,192 INFO     29 [qwen-vl-text] coord item[0]: text=221028180, bbox=[186, 17, 258, 32]
2026-08-10 12:25:51,192 INFO     29 [qwen-vl-text] coord item[1]: text=第2次入院记录, bbox=[439, 47, 567, 67]
2026-08-10 12:25:51,192 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[185, 85, 230, 104]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[185, 112, 249, 131]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：37岁, bbox=[185, 138, 263, 157]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[5]: text=婚姻：已婚, bbox=[185, 165, 266, 184]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[6]: text=入院时间：2025-07-11 08:57, bbox=[185, 191, 391, 210]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[7]: text=入院方式：步行, bbox=[185, 217, 298, 236]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：反复胸闷、气促8年，加重1月。, bbox=[185, 243, 447, 262]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。, bbox=[185, 270, 813, 471]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[10]: text=出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。, bbox=[185, 479, 815, 630]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[11]: text=既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。, bbox=[185, 637, 633, 656]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[12]: text=病史陈述者签名：, bbox=[185, 664, 303, 683]
2026-08-10 12:25:51,193 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。, bbox=[185, 690, 817, 893]
2026-08-10 12:25:51,194 INFO     29 [qwen-vl-text] coord item[14]: text=出生地：贵州省天柱县, bbox=[454, 85, 612, 104]
2026-08-10 12:25:51,194 INFO     29 [qwen-vl-text] coord item[15]: text=民族：苗族, bbox=[454, 112, 534, 131]
2026-08-10 12:25:51,194 INFO     29 [qwen-vl-text] coord item[16]: text=职业：农民, bbox=[454, 138, 534, 157]
2026-08-10 12:25:51,194 INFO     29 [qwen-vl-text] coord item[17]: text=住址：贵州省天柱县远口镇大祥村白蜡树脚组, bbox=[454, 165, 767, 184]
2026-08-10 12:25:51,194 INFO     29 [qwen-vl-text] coord item[18]: text=记录时间：2025-07-11 14:36, bbox=[454, 191, 661, 210]
2026-08-10 12:25:51,194 INFO     29 [qwen-vl-text] coord item[19]: text=CS 扫描全能王, bbox=[903, 942, 983, 963]
2026-08-10 12:25:51,194 INFO     29 [qwen-vl-text] coord item[20]: text=3亿人都在用的扫描App, bbox=[903, 970, 983, 981]
2026-08-10 12:25:51,195 INFO     29 [qwen-vl-text] page=8 — 21/21 coords, api_time=12.0s
2026-08-10 12:25:51,207 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2954195, prompt_len=1923
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["出院记录", "入院时间：2025-02-24 12:22", "出院时间：2025-03-01 10:00", "住院天数：5天", "记录时间：2025-02-28 20:39", "入院诊断：胸闷、气促查因：支气管哮喘可能性大", "入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89", "次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。", "诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C", "+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、", "肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体", "测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。", "心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1", "0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范", "围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO", "2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球", "菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、", "两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，", "LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能", "结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、", "抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者", "及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。", "出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶", "心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，", "BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心", "率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：", "功能性消化不良？反流性食管炎？其他。", "出院医嘱：", "（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺", "激性烟雾及吸入二手烟；"]

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
2026-08-10 12:26:06,759 INFO     29 [qwen-vl-text] coord API raw response (len=2660):
[
	{"text": "出院记录", "bbox": [476, 18, 557, 40]},
	{"text": "入院时间：2025-02-24 12:22", "bbox": [194, 50, 404, 69]},
	{"text": "出院时间：2025-03-01 10:00", "bbox": [194, 77, 404, 95]},
	{"text": "住院天数：5天", "bbox": [194, 103, 299, 121]},
	{"text": "记录时间：2025-02-28 20:39", "bbox": [194, 129, 403, 147]},
	{"text": "入院诊断：胸闷、气促查因：支气管哮喘可能性大", "bbox": [194, 155, 544, 174]},
	{"text": "入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。", "bbox": [194, 180, 814, 200]},
	{"text": "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "bbox": [194, 207, 822, 226]},
	{"text": "氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89", "bbox": [194, 233, 831, 253]},
	{"text": "次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。", "bbox": [194, 260, 797, 279]},
	{"text": "诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C", "bbox": [194, 286, 790, 305]},
	{"text": "+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、", "bbox": [194, 313, 829, 332]},
	{"text": "肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体", "bbox": [194, 339, 820, 359]},
	{"text": "测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。", "bbox": [194, 366, 820, 385]},
	{"text": "心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1", "bbox": [194, 392, 796, 411]},
	{"text": "0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范", "bbox": [194, 418, 819, 438]},
	{"text": "围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO", "bbox": [194, 445, 816, 464]},
	{"text": "2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球", "bbox": [194, 471, 825, 490]},
	{"text": "菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、", "bbox": [194, 497, 832, 517]},
	{"text": "两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，", "bbox": [194, 524, 814, 543]},
	{"text": "LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能", "bbox": [194, 550, 815, 569]},
	{"text": "结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、", "bbox": [194, 576, 814, 596]},
	{"text": "抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者", "bbox": [194, 603, 821, 622]},
	{"text": "及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。", "bbox": [194, 629, 625, 648]},
	{"text": "出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶", "bbox": [194, 655, 820, 674]},
	{"text": "心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，", "bbox": [194, 681, 755, 699]},
	{"text": "BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心", "bbox": [194, 707, 811, 726]},
	{"text": "率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "bbox": [194, 733, 757, 752]},
	{"text": "出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：", "bbox": [194, 759, 815, 778]},
	{"text": "功能性消化不良？反流性食管炎？其他。", "bbox": [194, 785, 466, 804]},
	{"text": "出院医嘱：", "bbox": [194, 811, 260, 829]},
	{"text": "（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺", "bbox": [223, 837, 815, 855]},
	{"text": "激性烟雾及吸入二手烟；", "bbox": [194, 862, 353, 880]}
]
2026-08-10 12:26:06,762 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=15.6s
2026-08-10 12:26:06,762 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[476, 18, 557, 40]
2026-08-10 12:26:06,762 INFO     29 [qwen-vl-text] coord item[1]: text=入院时间：2025-02-24 12:22, bbox=[194, 50, 404, 69]
2026-08-10 12:26:06,762 INFO     29 [qwen-vl-text] coord item[2]: text=出院时间：2025-03-01 10:00, bbox=[194, 77, 404, 95]
2026-08-10 12:26:06,762 INFO     29 [qwen-vl-text] coord item[3]: text=住院天数：5天, bbox=[194, 103, 299, 121]
2026-08-10 12:26:06,762 INFO     29 [qwen-vl-text] coord item[4]: text=记录时间：2025-02-28 20:39, bbox=[194, 129, 403, 147]
2026-08-10 12:26:06,762 INFO     29 [qwen-vl-text] coord item[5]: text=入院诊断：胸闷、气促查因：支气管哮喘可能性大, bbox=[194, 155, 544, 174]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[6]: text=入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。, bbox=[194, 180, 814, 200]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[7]: text=体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸, bbox=[194, 207, 822, 226]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[8]: text=氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89, bbox=[194, 233, 831, 253]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[9]: text=次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。, bbox=[194, 260, 797, 279]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[10]: text=诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C, bbox=[194, 286, 790, 305]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[11]: text=+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、, bbox=[194, 313, 829, 332]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[12]: text=肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体, bbox=[194, 339, 820, 359]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[13]: text=测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。, bbox=[194, 366, 820, 385]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[14]: text=心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1, bbox=[194, 392, 796, 411]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[15]: text=0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范, bbox=[194, 418, 819, 438]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[16]: text=围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO, bbox=[194, 445, 816, 464]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[17]: text=2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球, bbox=[194, 471, 825, 490]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[18]: text=菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、, bbox=[194, 497, 832, 517]
2026-08-10 12:26:06,763 INFO     29 [qwen-vl-text] coord item[19]: text=两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，, bbox=[194, 524, 814, 543]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[20]: text=LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能, bbox=[194, 550, 815, 569]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[21]: text=结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、, bbox=[194, 576, 814, 596]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[22]: text=抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者, bbox=[194, 603, 821, 622]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[23]: text=及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。, bbox=[194, 629, 625, 648]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[24]: text=出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶, bbox=[194, 655, 820, 674]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[25]: text=心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，, bbox=[194, 681, 755, 699]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[26]: text=BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心, bbox=[194, 707, 811, 726]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[27]: text=率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。, bbox=[194, 733, 757, 752]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[28]: text=出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：, bbox=[194, 759, 815, 778]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[29]: text=功能性消化不良？反流性食管炎？其他。, bbox=[194, 785, 466, 804]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[30]: text=出院医嘱：, bbox=[194, 811, 260, 829]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[31]: text=（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺, bbox=[223, 837, 815, 855]
2026-08-10 12:26:06,764 INFO     29 [qwen-vl-text] coord item[32]: text=激性烟雾及吸入二手烟；, bbox=[194, 862, 353, 880]
2026-08-10 12:26:06,765 INFO     29 [qwen-vl-text] page=9 — 33/33 coords, api_time=15.6s
2026-08-10 12:26:06,768 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=812427, prompt_len=1045
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共15行）
["姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；", "(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；", "(4) 继续用药：", "舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服", "布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入", "(吸入后漱口，根据动态复查肺功能结果，调整用药)", "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服", "止咳祛痰：润肺膏 每次15g 每天2次，口服", "调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服", "(5) 如有不适，随时医院就诊，我科随诊。", "科室电话：0745-2329117 主管医师电话：13789357317", "医师签名：主治医师："]

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
2026-08-10 12:26:13,400 INFO     29 [qwen-vl-text] coord API raw response (len=1050):
[
	{"text": "姓名：", "bbox": [114, 117, 187, 139]},
	{"text": "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "bbox": [250, 117, 871, 139]},
	{"text": "220999152", "bbox": [114, 140, 207, 158]},
	{"text": "(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；", "bbox": [145, 173, 940, 196]},
	{"text": "(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；", "bbox": [145, 206, 848, 230]},
	{"text": "(4) 继续用药：", "bbox": [145, 241, 275, 264]},
	{"text": "舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服", "bbox": [124, 274, 818, 298]},
	{"text": "布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入", "bbox": [245, 308, 817, 332]},
	{"text": "(吸入后漱口，根据动态复查肺功能结果，调整用药)", "bbox": [236, 342, 706, 366]},
	{"text": "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服", "bbox": [123, 375, 815, 399]},
	{"text": "止咳祛痰：润肺膏 每次15g 每天2次，口服", "bbox": [144, 408, 814, 432]},
	{"text": "调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服", "bbox": [114, 442, 813, 466]},
	{"text": "(5) 如有不适，随时医院就诊，我科随诊。", "bbox": [145, 475, 517, 498]},
	{"text": "科室电话：0745-2329117 主管医师电话：13789357317", "bbox": [114, 508, 680, 528]},
	{"text": "医师签名：主治医师：", "bbox": [540, 531, 791, 559]}
]
2026-08-10 12:26:13,400 INFO     29 [qwen-vl-text] coord API: raw_items=15, valid_items=15, elapsed=6.6s
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[114, 117, 187, 139]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[1]: text=性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：, bbox=[250, 117, 871, 139]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[2]: text=220999152, bbox=[114, 140, 207, 158]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[3]: text=(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；, bbox=[145, 173, 940, 196]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[4]: text=(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；, bbox=[145, 206, 848, 230]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[5]: text=(4) 继续用药：, bbox=[145, 241, 275, 264]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[6]: text=舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服, bbox=[124, 274, 818, 298]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[7]: text=布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入, bbox=[245, 308, 817, 332]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[8]: text=(吸入后漱口，根据动态复查肺功能结果，调整用药), bbox=[236, 342, 706, 366]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[9]: text=抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服, bbox=[123, 375, 815, 399]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[10]: text=止咳祛痰：润肺膏 每次15g 每天2次，口服, bbox=[144, 408, 814, 432]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[11]: text=调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服, bbox=[114, 442, 813, 466]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[12]: text=(5) 如有不适，随时医院就诊，我科随诊。, bbox=[145, 475, 517, 498]
2026-08-10 12:26:13,401 INFO     29 [qwen-vl-text] coord item[13]: text=科室电话：0745-2329117 主管医师电话：13789357317, bbox=[114, 508, 680, 528]
2026-08-10 12:26:13,402 INFO     29 [qwen-vl-text] coord item[14]: text=医师签名：主治医师：, bbox=[540, 531, 791, 559]
2026-08-10 12:26:13,402 INFO     29 [qwen-vl-text] page=10 — 15/15 coords, api_time=6.6s
2026-08-10 12:26:13,402 INFO     29 [qwen-vl-text] new_positions (69):
[[8, 156.612, 217.236, 10.115, 19.04], [8, 369.638, 477.414, 27.965, 39.864999999999995], [8, 155.76999999999998, 193.66, 50.574999999999996, 61.879999999999995], [8, 155.76999999999998, 209.658, 66.64, 77.945], [8, 155.76999999999998, 221.446, 82.11, 93.41499999999999], [8, 155.76999999999998, 223.97199999999998, 98.175, 109.47999999999999], [8, 155.76999999999998, 329.222, 113.645, 124.94999999999999], [8, 155.76999999999998, 250.916, 129.11499999999998, 140.42], [8, 155.76999999999998, 376.37399999999997, 144.58499999999998, 155.89], [8, 155.76999999999998, 684.5459999999999, 160.65, 280.245], [8, 155.76999999999998, 686.23, 285.005, 374.84999999999997], [8, 155.76999999999998, 532.986, 379.015, 390.32], [8, 155.76999999999998, 255.126, 395.08, 406.385], [8, 155.76999999999998, 687.914, 410.54999999999995, 531.3349999999999], [8, 382.268, 515.304, 50.574999999999996, 61.879999999999995], [8, 382.268, 449.628, 66.64, 77.945], [8, 382.268, 449.628, 82.11, 93.41499999999999], [8, 382.268, 645.814, 98.175, 109.47999999999999], [8, 382.268, 556.562, 113.645, 124.94999999999999], [8, 760.326, 827.6859999999999, 560.49, 572.985], [8, 760.326, 827.6859999999999, 577.15, 583.6949999999999], [9, 400.792, 468.99399999999997, 10.709999999999999, 23.799999999999997], [9, 163.34799999999998, 340.168, 29.75, 41.055], [9, 163.34799999999998, 340.168, 45.815, 56.525], [9, 163.34799999999998, 251.75799999999998, 61.285, 71.99499999999999], [9, 163.34799999999998, 339.32599999999996, 76.755, 87.46499999999999], [9, 163.34799999999998, 458.048, 92.225, 103.53], [9, 163.34799999999998, 685.3879999999999, 107.1, 119.0], [9, 163.34799999999998, 692.124, 123.16499999999999, 134.47], [9, 163.34799999999998, 699.702, 138.635, 150.535], [9, 163.34799999999998, 671.074, 154.7, 166.005], [9, 163.34799999999998, 665.18, 170.17, 181.475], [9, 163.34799999999998, 698.018, 186.23499999999999, 197.54], [9, 163.34799999999998, 690.4399999999999, 201.70499999999998, 213.605], [9, 163.34799999999998, 690.4399999999999, 217.76999999999998, 229.075], [9, 163.34799999999998, 670.232, 233.23999999999998, 244.545], [9, 163.34799999999998, 689.598, 248.70999999999998, 260.61], [9, 163.34799999999998, 687.072, 264.775, 276.08], [9, 163.34799999999998, 694.65, 280.245, 291.55], [9, 163.34799999999998, 700.544, 295.715, 307.615], [9, 163.34799999999998, 685.3879999999999, 311.78, 323.085], [9, 163.34799999999998, 686.23, 327.25, 338.555], [9, 163.34799999999998, 685.3879999999999, 342.71999999999997, 354.62], [9, 163.34799999999998, 691.2819999999999, 358.78499999999997, 370.09], [9, 163.34799999999998, 526.25, 374.255, 385.56], [9, 163.34799999999998, 690.4399999999999, 389.72499999999997, 401.03], [9, 163.34799999999998, 635.7099999999999, 405.195, 415.905], [9, 163.34799999999998, 682.862, 420.66499999999996, 431.96999999999997], [9, 163.34799999999998, 637.394, 436.135, 447.44], [9, 163.34799999999998, 686.23, 451.60499999999996, 462.90999999999997], [9, 163.34799999999998, 392.372, 467.075, 478.38], [9, 163.34799999999998, 218.92, 482.54499999999996, 493.255], [9, 187.766, 686.23, 498.015, 508.72499999999997], [9, 163.34799999999998, 297.226, 512.89, 523.6], [10, 95.988, 157.454, 69.615, 82.705], [10, 210.5, 733.382, 69.615, 82.705], [10, 95.988, 174.29399999999998, 83.3, 94.00999999999999], [10, 122.08999999999999, 791.48, 102.935, 116.61999999999999], [10, 122.08999999999999, 714.016, 122.57, 136.85], [10, 122.08999999999999, 231.54999999999998, 143.39499999999998, 157.07999999999998], [10, 104.408, 688.756, 163.03, 177.31], [10, 206.29, 687.914, 183.26, 197.54], [10, 198.712, 594.452, 203.48999999999998, 217.76999999999998], [10, 103.566, 686.23, 223.125, 237.405], [10, 121.24799999999999, 685.3879999999999, 242.76, 257.03999999999996], [10, 95.988, 684.5459999999999, 262.99, 277.27], [10, 122.08999999999999, 435.31399999999996, 282.625, 296.31], [10, 95.988, 572.56, 302.26, 314.15999999999997], [10, 454.68, 666.0219999999999, 315.945, 332.60499999999996]]
2026-08-10 12:26:13,402 INFO     29 [qwen-vl-text] ═══ DONE ═══ 69 positions, pages=3, time=52.6s
2026-08-10 12:26:13,417 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 12:26:13,417 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:Discharge | outputs={"chunks": "2 items, types={'DischargeRecord': 2}", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:26:13,417 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 12:26:13,418 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:26:13.417+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:26:13,423 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:26:13,424 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:26:13,424 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 12:26:13,424 INFO     29 [qwen-vl-text] positions(53): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:26:13,424 INFO     29 [qwen-vl-text] page grouping: [6, 7], lines per page: [33, 20]
2026-08-10 12:26:13,704 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:26:13,907 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:26:13,908 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1969
2026-08-10 12:26:13,909 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:26:13,909 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 139, \"bbox_end\": 191, \"encounter_dates\": [\"2025-07-11\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n出院记录\n入院时间：2025-07-11 08:57\n出院时间：2025-07-22 15:00\n住院天数：11天\n记录时间：2025-07-21 16:14\n入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；\n4.腹胀查因：功能性消化不良？反流性食管炎？其他。\n入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T\n36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面\n容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及\n少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，\n无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，\nLU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功\n能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散\n功能在正常范围；肺总量在正常范围，残气量、残总比增高。\n诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分\n压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中\n性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；\n尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红\n细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；\n电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C\n蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链\nDNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生\n虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：\n胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.\n支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气\n功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、\nMEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重\n减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳\n性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，\n绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），\n2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：\n怀化市中心医院\nHUAIHUA CENTRAL HOSPITAL\n怀化市肿瘤医院\n姓名：\n性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n221028180\n[心前区无隆起]，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，\n[各瓣膜听诊区未闻及杂音]。腹部平坦，[腹壁静脉无曲张]，无胃肠型和蠕动波，[全\n腹柔软]，[腹部无压痛]，[腹部无反跳痛]，[肝脾肋下未扪及]，Murphy征(-)，叩\n诊呈[鼓音]，移动性浊音(-)。肠鸣音正常，[无气过水声]。外生殖器[未查]，肛门\n直肠[正常]。脊柱四肢[正常]。 双下肢无浮肿，生理反射正常，病理反射阴性。\n辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复\n查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占\n预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量\n在正常范围，残气量、残总比增高。\n入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？\n3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其\n他。\n主治医师：\n副主任医师：",
    "role": "user"
  }
]
2026-08-10 12:26:35,438 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:26:35,438 INFO     29 [qwen-vl-text] LLM output (len=3916):
{
  "encounter_date": "2025-07-11",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 37,
  "dm_ethnicity": null,
  "dm_marital_status": null,
  "dm_occupation": null,
  "dm_admission_time": "2025-07-11 08:57",
  "dm_record_time": "2025-07-21 16:14",
  "dm_history_provider": null,
  "cc_text": "反复胸闷、气促8年，加重1月",
  "cc_main_symptoms": [
    "胸闷",
    "气促"
  ],
  "cc_duration": "8年，加重1月",
  "pi_text": null,
  "pmh_disease_history": [],
  "pmh_allergy_history": [],
  "pmh_surgery_trauma_history": [],
  "ph_smoking": null,
  "ph_drinking": null,
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": null,
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 70,
  "vs_respiration_rpm": 24,
  "vs_systolic_bp_mmhg": 139,
  "vs_diastolic_bp_mmhg": 92,
  "pe_general_condition": "急性面容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈",
  "pe_skin_mucosa": null,
  "pe_lymph_nodes": null,
  "pe_lungs": "双肺呼吸音清，可闻及少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音",
  "pe_heart": "心率70次/分，心律齐，无杂音。心前区无隆起，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，各瓣膜听诊区未闻及杂音",
  "pe_abdomen": "腹部平软，无压痛及反跳痛。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋下未扪及，Murphy征(-)，叩诊呈鼓音，移动性浊音(-)。肠鸣音正常，无气过水声",
  "pe_extremities": "双下肢无浮肿。脊柱四肢正常",
  "pe_nervous_system": "生理反射正常，病理反射阴性",
  "pe_specialist_exam": null,
  "pe_ecog_score": null,
  "pat_text": "2025-02-25胸部CT平扫，右肺中叶内侧段结节，LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量在正常范围，残气量、残总比增高。血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：",
  "pat_items": [
    "2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症",
    "肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量在正常范围，残气量、残总比增高",
    "血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓",
    "血常规：白细胞 5.94×10^9/L、中性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L",
    "尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红细胞 + /HP、（镜检）上皮细胞 + /LP",
    "尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00",
    "电解质：钾 3.48 mmol/L ↓",
    "总IgE 261.95IU/ml",
    "大便常规、肝肾功能、心肌酶、超敏C蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生虫全套、IgG4、血管炎四项均未见明显异常",
    "心电图：1.窦性心律 2.正常心电图",
    "CT成套：胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.支气管疾患并双肺少许炎性病变，病灶较前稍增多",
    "肺功能常规通气：1.重度混合性肺通气功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重减退（占预计值39.61%）",
    "舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，绝对值增加≥200ml）",
    "一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），2.残气量上升、残总比上升 肺总量在正常范围",
    "呼出气一氧化氮，FeNO50：20ppd，CaNO："
  ],
  "preliminary_diagnoses": [
    {
      "name": "支气管哮喘急性发作期",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "肺炎？",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "右肺中叶内侧段结节（LU-RADS 2类）",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "腹胀查因：功能性消化不良？反流性食管炎？其他",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": "呼吸与危重症医学科"
}
2026-08-10 12:26:35,439 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-11]
2026-08-10 12:26:35,446 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1584125, prompt_len=2122
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "出院记录", "入院时间：2025-07-11 08:57", "出院时间：2025-07-22 15:00", "住院天数：11天", "记录时间：2025-07-21 16:14", "入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；", "4.腹胀查因：功能性消化不良？反流性食管炎？其他。", "入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T", "36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面", "容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及", "少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，", "无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，", "LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功", "能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散", "功能在正常范围；肺总量在正常范围，残气量、残总比增高。", "诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分", "压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中", "性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；", "尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红", "细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；", "电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C", "蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链", "DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生", "虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：", "胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.", "支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气", "功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、", "MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重", "减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳", "性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，", "绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），", "2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO："]

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
2026-08-10 12:26:51,095 INFO     29 [qwen-vl-text] coord API raw response (len=2912):
[
	{"text": "zz1028180", "bbox": [171, 34, 246, 52]},
	{"text": "37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "bbox": [405, 18, 778, 37]},
	{"text": "出院记录", "bbox": [463, 68, 545, 89]},
	{"text": "入院时间：2025-07-11 08:57", "bbox": [170, 99, 387, 117]},
	{"text": "出院时间：2025-07-22 15:00", "bbox": [170, 125, 387, 143]},
	{"text": "住院天数：11天", "bbox": [170, 150, 289, 169]},
	{"text": "记录时间：2025-07-21 16:14", "bbox": [170, 178, 387, 196]},
	{"text": "入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；", "bbox": [186, 204, 835, 223]},
	{"text": "4.腹胀查因：功能性消化不良？反流性食管炎？其他。", "bbox": [170, 231, 558, 250]},
	{"text": "入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T", "bbox": [170, 258, 804, 277]},
	{"text": "36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面", "bbox": [170, 284, 819, 303]},
	{"text": "容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及", "bbox": [170, 311, 827, 330]},
	{"text": "少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，", "bbox": [170, 337, 808, 356]},
	{"text": "无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，", "bbox": [170, 364, 834, 383]},
	{"text": "LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功", "bbox": [170, 390, 827, 409]},
	{"text": "能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散", "bbox": [170, 416, 828, 435]},
	{"text": "功能在正常范围；肺总量在正常范围，残气量、残总比增高。", "bbox": [170, 443, 607, 462]},
	{"text": "诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分", "bbox": [186, 470, 828, 489]},
	{"text": "压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中", "bbox": [170, 497, 819, 516]},
	{"text": "性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；", "bbox": [170, 523, 835, 542]},
	{"text": "尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红", "bbox": [170, 550, 820, 569]},
	{"text": "细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；", "bbox": [170, 576, 810, 595]},
	{"text": "电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C", "bbox": [170, 603, 821, 622]},
	{"text": "蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链", "bbox": [170, 629, 813, 648]},
	{"text": "DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生", "bbox": [170, 656, 820, 675]},
	{"text": "虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：", "bbox": [170, 682, 827, 701]},
	{"text": "胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.", "bbox": [170, 709, 833, 728]},
	{"text": "支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气", "bbox": [170, 735, 828, 754]},
	{"text": "功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、", "bbox": [170, 762, 836, 781]},
	{"text": "MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重", "bbox": [170, 788, 819, 807]},
	{"text": "减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳", "bbox": [170, 815, 828, 834]},
	{"text": "性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，", "bbox": [170, 841, 825, 860]},
	{"text": "绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），", "bbox": [170, 868, 826, 887]},
	{"text": "2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：", "bbox": [170, 894, 820, 913]}
]
2026-08-10 12:26:51,095 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=15.6s
2026-08-10 12:26:51,095 INFO     29 [qwen-vl-text] coord item[0]: text=zz1028180, bbox=[171, 34, 246, 52]
2026-08-10 12:26:51,095 INFO     29 [qwen-vl-text] coord item[1]: text=37岁 科室：呼吸与危重症医学科 床号：42 住院号：, bbox=[405, 18, 778, 37]
2026-08-10 12:26:51,095 INFO     29 [qwen-vl-text] coord item[2]: text=出院记录, bbox=[463, 68, 545, 89]
2026-08-10 12:26:51,095 INFO     29 [qwen-vl-text] coord item[3]: text=入院时间：2025-07-11 08:57, bbox=[170, 99, 387, 117]
2026-08-10 12:26:51,095 INFO     29 [qwen-vl-text] coord item[4]: text=出院时间：2025-07-22 15:00, bbox=[170, 125, 387, 143]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[5]: text=住院天数：11天, bbox=[170, 150, 289, 169]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[6]: text=记录时间：2025-07-21 16:14, bbox=[170, 178, 387, 196]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[7]: text=入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；, bbox=[186, 204, 835, 223]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[8]: text=4.腹胀查因：功能性消化不良？反流性食管炎？其他。, bbox=[170, 231, 558, 250]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[9]: text=入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T, bbox=[170, 258, 804, 277]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[10]: text=36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面, bbox=[170, 284, 819, 303]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[11]: text=容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及, bbox=[170, 311, 827, 330]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[12]: text=少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，, bbox=[170, 337, 808, 356]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[13]: text=无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，, bbox=[170, 364, 834, 383]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[14]: text=LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功, bbox=[170, 390, 827, 409]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[15]: text=能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散, bbox=[170, 416, 828, 435]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[16]: text=功能在正常范围；肺总量在正常范围，残气量、残总比增高。, bbox=[170, 443, 607, 462]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[17]: text=诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分, bbox=[186, 470, 828, 489]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[18]: text=压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中, bbox=[170, 497, 819, 516]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[19]: text=性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；, bbox=[170, 523, 835, 542]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[20]: text=尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红, bbox=[170, 550, 820, 569]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[21]: text=细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；, bbox=[170, 576, 810, 595]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[22]: text=电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C, bbox=[170, 603, 821, 622]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[23]: text=蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链, bbox=[170, 629, 813, 648]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[24]: text=DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生, bbox=[170, 656, 820, 675]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[25]: text=虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：, bbox=[170, 682, 827, 701]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[26]: text=胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2., bbox=[170, 709, 833, 728]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[27]: text=支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气, bbox=[170, 735, 828, 754]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[28]: text=功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、, bbox=[170, 762, 836, 781]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[29]: text=MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重, bbox=[170, 788, 819, 807]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[30]: text=减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳, bbox=[170, 815, 828, 834]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[31]: text=性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，, bbox=[170, 841, 825, 860]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[32]: text=绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），, bbox=[170, 868, 826, 887]
2026-08-10 12:26:51,096 INFO     29 [qwen-vl-text] coord item[33]: text=2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：, bbox=[170, 894, 820, 913]
2026-08-10 12:26:51,097 INFO     29 [qwen-vl-text] page=6 — 33/33 coords, api_time=15.6s
2026-08-10 12:26:51,099 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=921584, prompt_len=1231
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["怀化市中心医院", "HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "221028180", "[心前区无隆起]，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，", "[各瓣膜听诊区未闻及杂音]。腹部平坦，[腹壁静脉无曲张]，无胃肠型和蠕动波，[全", "腹柔软]，[腹部无压痛]，[腹部无反跳痛]，[肝脾肋下未扪及]，Murphy征(-)，叩", "诊呈[鼓音]，移动性浊音(-)。肠鸣音正常，[无气过水声]。外生殖器[未查]，肛门", "直肠[正常]。脊柱四肢[正常]。 双下肢无浮肿，生理反射正常，病理反射阴性。", "辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复", "查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占", "预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量", "在正常范围，残气量、残总比增高。", "入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？", "3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其", "他。", "主治医师：", "副主任医师："]

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
2026-08-10 12:26:59,510 INFO     29 [qwen-vl-text] coord API raw response (len=1435):
[
	{"text": "怀化市中心医院", "bbox": [248, 50, 438, 70]},
	{"text": "HUAIHUA CENTRAL HOSPITAL", "bbox": [248, 70, 438, 80]},
	{"text": "怀化市肿瘤医院", "bbox": [248, 84, 438, 98]},
	{"text": "姓名：", "bbox": [141, 127, 190, 147]},
	{"text": "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "bbox": [260, 127, 798, 147]},
	{"text": "221028180", "bbox": [141, 147, 222, 163]},
	{"text": "[心前区无隆起]，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，", "bbox": [145, 175, 835, 196]},
	{"text": "[各瓣膜听诊区未闻及杂音]。腹部平坦，[腹壁静脉无曲张]，无胃肠型和蠕动波，[全", "bbox": [145, 204, 845, 225]},
	{"text": "腹柔软]，[腹部无压痛]，[腹部无反跳痛]，[肝脾肋下未扪及]，Murphy征(-)，叩", "bbox": [141, 234, 845, 255]},
	{"text": "诊呈[鼓音]，移动性浊音(-)。肠鸣音正常，[无气过水声]。外生殖器[未查]，肛门", "bbox": [141, 264, 845, 285]},
	{"text": "直肠[正常]。脊柱四肢[正常]。 双下肢无浮肿，生理反射正常，病理反射阴性。", "bbox": [141, 294, 830, 315]},
	{"text": "辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复", "bbox": [141, 324, 847, 345]},
	{"text": "查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占", "bbox": [141, 354, 847, 375]},
	{"text": "预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量", "bbox": [141, 383, 855, 404]},
	{"text": "在正常范围，残气量、残总比增高。", "bbox": [141, 413, 420, 434]},
	{"text": "入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？", "bbox": [453, 443, 855, 464]},
	{"text": "3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其", "bbox": [141, 472, 860, 493]},
	{"text": "他。", "bbox": [141, 502, 167, 521]},
	{"text": "主治医师：", "bbox": [584, 530, 664, 550]},
	{"text": "副主任医师：", "bbox": [580, 560, 690, 580]}
]
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=8.4s
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord item[0]: text=怀化市中心医院, bbox=[248, 50, 438, 70]
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord item[1]: text=HUAIHUA CENTRAL HOSPITAL, bbox=[248, 70, 438, 80]
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord item[2]: text=怀化市肿瘤医院, bbox=[248, 84, 438, 98]
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[141, 127, 190, 147]
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：, bbox=[260, 127, 798, 147]
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord item[5]: text=221028180, bbox=[141, 147, 222, 163]
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord item[6]: text=[心前区无隆起]，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，, bbox=[145, 175, 835, 196]
2026-08-10 12:26:59,511 INFO     29 [qwen-vl-text] coord item[7]: text=[各瓣膜听诊区未闻及杂音]。腹部平坦，[腹壁静脉无曲张]，无胃肠型和蠕动波，[全, bbox=[145, 204, 845, 225]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[8]: text=腹柔软]，[腹部无压痛]，[腹部无反跳痛]，[肝脾肋下未扪及]，Murphy征(-)，叩, bbox=[141, 234, 845, 255]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[9]: text=诊呈[鼓音]，移动性浊音(-)。肠鸣音正常，[无气过水声]。外生殖器[未查]，肛门, bbox=[141, 264, 845, 285]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[10]: text=直肠[正常]。脊柱四肢[正常]。 双下肢无浮肿，生理反射正常，病理反射阴性。, bbox=[141, 294, 830, 315]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[11]: text=辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复, bbox=[141, 324, 847, 345]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[12]: text=查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占, bbox=[141, 354, 847, 375]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[13]: text=预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量, bbox=[141, 383, 855, 404]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[14]: text=在正常范围，残气量、残总比增高。, bbox=[141, 413, 420, 434]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[15]: text=入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？, bbox=[453, 443, 855, 464]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[16]: text=3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其, bbox=[141, 472, 860, 493]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[17]: text=他。, bbox=[141, 502, 167, 521]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[18]: text=主治医师：, bbox=[584, 530, 664, 550]
2026-08-10 12:26:59,512 INFO     29 [qwen-vl-text] coord item[19]: text=副主任医师：, bbox=[580, 560, 690, 580]
2026-08-10 12:26:59,513 INFO     29 [qwen-vl-text] page=7 — 20/20 coords, api_time=8.4s
2026-08-10 12:26:59,513 INFO     29 [qwen-vl-text] new_positions (53):
[[6, 143.982, 207.132, 20.23, 30.939999999999998], [6, 341.01, 655.076, 10.709999999999999, 22.015], [6, 389.846, 458.89, 40.46, 52.955], [6, 143.14, 325.854, 58.904999999999994, 69.615], [6, 143.14, 325.854, 74.375, 85.085], [6, 143.14, 243.338, 89.25, 100.55499999999999], [6, 143.14, 325.854, 105.91, 116.61999999999999], [6, 156.612, 703.0699999999999, 121.38, 132.685], [6, 143.14, 469.83599999999996, 137.445, 148.75], [6, 143.14, 676.968, 153.51, 164.815], [6, 143.14, 689.598, 168.98, 180.285], [6, 143.14, 696.334, 185.045, 196.35], [6, 143.14, 680.336, 200.515, 211.82], [6, 143.14, 702.228, 216.57999999999998, 227.885], [6, 143.14, 696.334, 232.04999999999998, 243.355], [6, 143.14, 697.1759999999999, 247.51999999999998, 258.825], [6, 143.14, 511.094, 263.585, 274.89], [6, 156.612, 697.1759999999999, 279.65, 290.955], [6, 143.14, 689.598, 295.715, 307.02], [6, 143.14, 703.0699999999999, 311.185, 322.49], [6, 143.14, 690.4399999999999, 327.25, 338.555], [6, 143.14, 682.02, 342.71999999999997, 354.025], [6, 143.14, 691.2819999999999, 358.78499999999997, 370.09], [6, 143.14, 684.5459999999999, 374.255, 385.56], [6, 143.14, 690.4399999999999, 390.32, 401.625], [6, 143.14, 696.334, 405.78999999999996, 417.09499999999997], [6, 143.14, 701.386, 421.85499999999996, 433.15999999999997], [6, 143.14, 697.1759999999999, 437.325, 448.63], [6, 143.14, 703.9119999999999, 453.39, 464.695], [6, 143.14, 689.598, 468.85999999999996, 480.16499999999996], [6, 143.14, 697.1759999999999, 484.92499999999995, 496.22999999999996], [6, 143.14, 694.65, 500.395, 511.7], [6, 143.14, 695.492, 516.4599999999999, 527.765], [7, 208.816, 368.796, 29.75, 41.65], [7, 208.816, 368.796, 41.65, 47.599999999999994], [7, 208.816, 368.796, 49.98, 58.309999999999995], [7, 118.722, 159.98, 75.565, 87.46499999999999], [7, 218.92, 671.9159999999999, 75.565, 87.46499999999999], [7, 118.722, 186.924, 87.46499999999999, 96.985], [7, 122.08999999999999, 703.0699999999999, 104.125, 116.61999999999999], [7, 122.08999999999999, 711.49, 121.38, 133.875], [7, 118.722, 711.49, 139.23, 151.725], [7, 118.722, 711.49, 157.07999999999998, 169.575], [7, 118.722, 698.86, 174.92999999999998, 187.42499999999998], [7, 118.722, 713.174, 192.78, 205.27499999999998], [7, 118.722, 713.174, 210.63, 223.125], [7, 118.722, 719.91, 227.885, 240.38], [7, 118.722, 353.64, 245.73499999999999, 258.22999999999996], [7, 381.426, 719.91, 263.585, 276.08], [7, 118.722, 724.12, 280.84, 293.335], [7, 118.722, 140.614, 298.69, 309.995], [7, 491.728, 559.088, 315.34999999999997, 327.25], [7, 488.35999999999996, 580.98, 333.2, 345.09999999999997]]
2026-08-10 12:26:59,513 INFO     29 [qwen-vl-text] ═══ DONE ═══ 53 positions, pages=2, time=46.1s
2026-08-10 12:26:59,513 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:26:59,526 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:26:59,526 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 12:26:59,526 INFO     29 [qwen-vl-text] positions(32): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:26:59,526 INFO     29 [qwen-vl-text] page grouping: [11, 12], lines per page: [22, 10]
2026-08-10 12:26:59,782 INFO     29 [qwen-vl-text] page=11, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:27:00,008 INFO     29 [qwen-vl-text] page=12, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:27:00,010 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1683
2026-08-10 12:27:00,011 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:27:00,011 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 263, \"bbox_end\": 294, \"encounter_dates\": [\"2025-07-11\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "221028180\n第2次入院记录\n姓名：\n出生地：贵州省天柱县\n性别：女\n民族：苗族\n年龄：37岁\n职业：农民\n婚姻：已婚\n住址：贵\n入院时间：2025-07-11 08:57\n记录时间：2025-07-11 14:36\n入院方式：步行\n主诉：反复胸闷、气促8年，加重1月。\n现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。\n出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。\n既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。\n病史陈述者签名：\n体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。\n眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，\n甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。\n叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。\n家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。\n病史陈述者签名：\n体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋\n姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n220999152\n下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:\n辅助检查结果：无\n入院初步诊断：胸闷、气促查因：支气管哮喘可能性大\n主治医师：\n主任医师：",
    "role": "user"
  }
]
2026-08-10 12:27:00,013 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:27:00.012+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:27:11,137 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:27:11,138 INFO     29 [qwen-vl-text] LLM output (len=2123):
{
  "encounter_date": "2025-07-11",
  "dm_name": "杨细兰",
  "dm_gender": "女",
  "dm_age": 37,
  "dm_ethnicity": "苗族",
  "dm_marital_status": "已婚",
  "dm_occupation": "农民",
  "dm_admission_time": "2025-07-11 08:57",
  "dm_record_time": "2025-07-11 14:36",
  "dm_history_provider": null,
  "cc_text": "反复胸闷、气促8年，加重1月。",
  "cc_main_symptoms": [
    "胸闷",
    "气促"
  ],
  "cc_duration": "8年，加重1月",
  "pi_text": "患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。",
  "pmh_disease_history": [],
  "pmh_allergy_history": [],
  "pmh_surgery_trauma_history": [],
  "ph_smoking": null,
  "ph_drinking": null,
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.6,
  "vs_pulse_bpm": 89,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 129,
  "vs_diastolic_bp_mmhg": 90,
  "pe_general_condition": "发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。",
  "pe_skin_mucosa": "全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣。",
  "pe_lymph_nodes": "全身浅表淋巴结未触及肿大。",
  "pe_lungs": "胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。",
  "pe_heart": "心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。",
  "pe_abdomen": "腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。",
  "pe_extremities": "脊柱四肢正常。双下肢无浮肿。",
  "pe_nervous_system": "生理反射正常，病理反射阴性。",
  "pe_specialist_exam": null,
  "pe_ecog_score": null,
  "pat_text": "无",
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "胸闷、气促查因：支气管哮喘可能性大",
      "diagnosis_type": "西医",
      "is_primary": true
    }
  ],
  "department": "呼吸与危重症医学科"
}
2026-08-10 12:27:11,138 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-11]
2026-08-10 12:27:11,143 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1451457, prompt_len=1745
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["221028180", "第2次入院记录", "姓名：", "出生地：贵州省天柱县", "性别：女", "民族：苗族", "年龄：37岁", "职业：农民", "婚姻：已婚", "住址：贵", "入院时间：2025-07-11 08:57", "记录时间：2025-07-11 14:36", "入院方式：步行", "主诉：反复胸闷、气促8年，加重1月。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "病史陈述者签名：", "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。", "眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，", "甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。", "叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。"]

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
2026-08-10 12:27:24,400 INFO     29 [qwen-vl-text] coord API raw response (len=2031):
[
	{"text": "221028180", "bbox": [186, 17, 258, 32]},
	{"text": "第2次入院记录", "bbox": [439, 47, 568, 67]},
	{"text": "姓名：", "bbox": [185, 85, 244, 105]},
	{"text": "出生地：贵州省天柱县", "bbox": [455, 85, 613, 105]},
	{"text": "性别：女", "bbox": [185, 112, 248, 132]},
	{"text": "民族：苗族", "bbox": [455, 112, 535, 132]},
	{"text": "年龄：37岁", "bbox": [185, 138, 263, 158]},
	{"text": "职业：农民", "bbox": [455, 138, 535, 158]},
	{"text": "婚姻：已婚", "bbox": [185, 165, 266, 184]},
	{"text": "住址：贵", "bbox": [455, 165, 518, 184]},
	{"text": "入院时间：2025-07-11 08:57", "bbox": [185, 191, 392, 210]},
	{"text": "记录时间：2025-07-11 14:36", "bbox": [455, 191, 662, 210]},
	{"text": "入院方式：步行", "bbox": [185, 217, 298, 237]},
	{"text": "主诉：反复胸闷、气促8年，加重1月。", "bbox": [185, 243, 448, 263]},
	{"text": "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "bbox": [185, 270, 813, 471]},
	{"text": "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "bbox": [185, 478, 817, 630]},
	{"text": "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "bbox": [185, 637, 633, 657]},
	{"text": "病史陈述者签名：", "bbox": [185, 664, 303, 683]},
	{"text": "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。", "bbox": [185, 690, 817, 760]},
	{"text": "眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，", "bbox": [185, 767, 811, 840]},
	{"text": "甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。", "bbox": [193, 847, 797, 867]},
	{"text": "叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。", "bbox": [185, 873, 804, 893]}
]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=13.3s
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[0]: text=221028180, bbox=[186, 17, 258, 32]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[1]: text=第2次入院记录, bbox=[439, 47, 568, 67]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[185, 85, 244, 105]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[3]: text=出生地：贵州省天柱县, bbox=[455, 85, 613, 105]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[185, 112, 248, 132]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[5]: text=民族：苗族, bbox=[455, 112, 535, 132]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：37岁, bbox=[185, 138, 263, 158]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[7]: text=职业：农民, bbox=[455, 138, 535, 158]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[8]: text=婚姻：已婚, bbox=[185, 165, 266, 184]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[9]: text=住址：贵, bbox=[455, 165, 518, 184]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[10]: text=入院时间：2025-07-11 08:57, bbox=[185, 191, 392, 210]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[11]: text=记录时间：2025-07-11 14:36, bbox=[455, 191, 662, 210]
2026-08-10 12:27:24,401 INFO     29 [qwen-vl-text] coord item[12]: text=入院方式：步行, bbox=[185, 217, 298, 237]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[13]: text=主诉：反复胸闷、气促8年，加重1月。, bbox=[185, 243, 448, 263]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[14]: text=现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。, bbox=[185, 270, 813, 471]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[15]: text=出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。, bbox=[185, 478, 817, 630]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[16]: text=既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。, bbox=[185, 637, 633, 657]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[17]: text=病史陈述者签名：, bbox=[185, 664, 303, 683]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[18]: text=体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。, bbox=[185, 690, 817, 760]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[19]: text=眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，, bbox=[185, 767, 811, 840]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[20]: text=甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。, bbox=[193, 847, 797, 867]
2026-08-10 12:27:24,402 INFO     29 [qwen-vl-text] coord item[21]: text=叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。, bbox=[185, 873, 804, 893]
2026-08-10 12:27:24,403 INFO     29 [qwen-vl-text] page=11 — 22/22 coords, api_time=13.3s
2026-08-10 12:27:24,408 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1064952, prompt_len=1259
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共10行）
["家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。", "病史陈述者签名：", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋", "姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:", "辅助检查结果：无", "入院初步诊断：胸闷、气促查因：支气管哮喘可能性大", "主治医师：", "主任医师："]

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
2026-08-10 12:27:31,363 INFO     29 [qwen-vl-text] coord API raw response (len=1054):
[
	{"text": "家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。", "bbox": [145, 27, 668, 50]},
	{"text": "病史陈述者签名：", "bbox": [145, 57, 277, 79]},
	{"text": "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋", "bbox": [145, 86, 853, 339]},
	{"text": "姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "bbox": [147, 574, 797, 595]},
	{"text": "220999152", "bbox": [147, 594, 228, 610]},
	{"text": "下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:", "bbox": [147, 620, 852, 697]},
	{"text": "辅助检查结果：无", "bbox": [147, 706, 290, 726]},
	{"text": "入院初步诊断：胸闷、气促查因：支气管哮喘可能性大", "bbox": [433, 734, 853, 754]},
	{"text": "主治医师：", "bbox": [648, 763, 724, 783]},
	{"text": "主任医师：", "bbox": [648, 791, 724, 811]}
]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord API: raw_items=10, valid_items=10, elapsed=7.0s
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[0]: text=家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。, bbox=[145, 27, 668, 50]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[1]: text=病史陈述者签名：, bbox=[145, 57, 277, 79]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[2]: text=体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋, bbox=[145, 86, 853, 339]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：, bbox=[147, 574, 797, 595]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[4]: text=220999152, bbox=[147, 594, 228, 610]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[5]: text=下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:, bbox=[147, 620, 852, 697]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[6]: text=辅助检查结果：无, bbox=[147, 706, 290, 726]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[7]: text=入院初步诊断：胸闷、气促查因：支气管哮喘可能性大, bbox=[433, 734, 853, 754]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[8]: text=主治医师：, bbox=[648, 763, 724, 783]
2026-08-10 12:27:31,364 INFO     29 [qwen-vl-text] coord item[9]: text=主任医师：, bbox=[648, 791, 724, 811]
2026-08-10 12:27:31,365 INFO     29 [qwen-vl-text] page=12 — 10/10 coords, api_time=7.0s
2026-08-10 12:27:31,365 INFO     29 [qwen-vl-text] new_positions (32):
[[11, 156.612, 217.236, 10.115, 19.04], [11, 369.638, 478.256, 27.965, 39.864999999999995], [11, 155.76999999999998, 205.44799999999998, 50.574999999999996, 62.474999999999994], [11, 383.11, 516.146, 50.574999999999996, 62.474999999999994], [11, 155.76999999999998, 208.816, 66.64, 78.53999999999999], [11, 383.11, 450.46999999999997, 66.64, 78.53999999999999], [11, 155.76999999999998, 221.446, 82.11, 94.00999999999999], [11, 383.11, 450.46999999999997, 82.11, 94.00999999999999], [11, 155.76999999999998, 223.97199999999998, 98.175, 109.47999999999999], [11, 383.11, 436.156, 98.175, 109.47999999999999], [11, 155.76999999999998, 330.06399999999996, 113.645, 124.94999999999999], [11, 383.11, 557.404, 113.645, 124.94999999999999], [11, 155.76999999999998, 250.916, 129.11499999999998, 141.015], [11, 155.76999999999998, 377.216, 144.58499999999998, 156.48499999999999], [11, 155.76999999999998, 684.5459999999999, 160.65, 280.245], [11, 155.76999999999998, 687.914, 284.40999999999997, 374.84999999999997], [11, 155.76999999999998, 532.986, 379.015, 390.91499999999996], [11, 155.76999999999998, 255.126, 395.08, 406.385], [11, 155.76999999999998, 687.914, 410.54999999999995, 452.2], [11, 155.76999999999998, 682.862, 456.36499999999995, 499.79999999999995], [11, 162.506, 671.074, 503.965, 515.865], [11, 155.76999999999998, 676.968, 519.435, 531.3349999999999], [12, 122.08999999999999, 562.456, 16.064999999999998, 29.75], [12, 122.08999999999999, 233.23399999999998, 33.915, 47.004999999999995], [12, 122.08999999999999, 718.226, 51.169999999999995, 201.70499999999998], [12, 123.774, 671.074, 341.53, 354.025], [12, 123.774, 191.976, 353.43, 362.95], [12, 123.774, 717.384, 368.9, 414.715], [12, 123.774, 244.17999999999998, 420.07, 431.96999999999997], [12, 364.586, 718.226, 436.72999999999996, 448.63], [12, 545.616, 609.608, 453.98499999999996, 465.885], [12, 545.616, 609.608, 470.645, 482.54499999999996]]
2026-08-10 12:27:31,365 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=2, time=31.9s
2026-08-10 12:27:31,365 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:27:31,373 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:27:31,374 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 12:27:31,374 INFO     29 [qwen-vl-text] positions(38): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:27:31,374 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [38]
2026-08-10 12:27:31,634 INFO     29 [qwen-vl-text] page=13, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:27:31,636 INFO     29 [qwen-vl-text] LLM extraction start, text_len=985
2026-08-10 12:27:31,636 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:27:31,636 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 295, \"bbox_end\": 332, \"encounter_dates\": [\"2025-02-24\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "姓名：\n性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n220999152\n入院记录\n姓名：\n出生地：贵州省天柱县远口镇大样村白蜡树脚组\n性别：女\n民族：苗族\n年龄：37岁\n职业：自由职业者\n婚姻：已婚\n住址：贵\n入院时间：2025-02-24 12:22\n记录时间：2025-02-24 14:28\n入院方式：步行\n主诉：反复胸闷、气促8年，加重半年。\n现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳\n嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐\n渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，\n无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，\n约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，\n门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期\n体重无改变。\n既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病\n史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。\n个人史：[出生于原籍，常住本地，无粉尘放射性物质接触史，否认疫区居住\n史]，[无吸烟史，无饮酒史，否认性病及冶游史]。\n月经史：162~32025/2/21，月经周期规律，色红，量少，无痛经。\n婚育史：24岁结婚，育有1子1女，配偶及子女体健。\n家族史：家族中无同类病人。直系亲属体健。无遗传倾向疾患。\n病史陈述者签名：\n体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸\n氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜\n色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，\n巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常\n分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-\n颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤\n正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦",
    "role": "user"
  }
]
2026-08-10 12:27:32,363 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:27:32.361+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:27:40,529 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:27:40,529 INFO     29 [qwen-vl-text] LLM output (len=1793):
{
  "encounter_date": "2025-02-24",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 37,
  "dm_ethnicity": "苗族",
  "dm_marital_status": "已婚",
  "dm_occupation": "自由职业者",
  "dm_admission_time": "2025-02-24 12:22",
  "dm_record_time": "2025-02-24 14:28",
  "dm_history_provider": null,
  "cc_text": "反复胸闷、气促8年，加重半年。",
  "cc_main_symptoms": [
    "胸闷",
    "气促"
  ],
  "cc_duration": "8年，加重半年",
  "pi_text": "患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期体重无改变。",
  "pmh_disease_history": [
    "否认高血压病",
    "否认糖尿病",
    "否认心脏病病史",
    "否认肝炎",
    "否认结核等传染病病史"
  ],
  "pmh_allergy_history": [
    "无食物、药物过敏史"
  ],
  "pmh_surgery_trauma_history": [
    "无手术史",
    "无外伤史",
    "无输血史"
  ],
  "ph_smoking": "无吸烟史",
  "ph_drinking": "无饮酒史",
  "oh_menarche_age": 16,
  "oh_menopause_age": null,
  "oh_pregnancies": "育有1子1女",
  "fh_text": "家族中无同类病人。直系亲属体健。无遗传倾向疾患。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.6,
  "vs_pulse_bpm": 89,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 129,
  "vs_diastolic_bp_mmhg": 90,
  "pe_general_condition": "发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。",
  "pe_skin_mucosa": "全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣。",
  "pe_lymph_nodes": "全身浅表淋巴结未触及肿大。",
  "pe_lungs": "胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦",
  "pe_heart": null,
  "pe_abdomen": null,
  "pe_extremities": null,
  "pe_nervous_system": null,
  "pe_specialist_exam": null,
  "pe_ecog_score": null,
  "pat_text": null,
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "支气管哮喘",
      "diagnosis_type": "西医",
      "is_primary": true
    }
  ],
  "department": "呼吸与危重症医学科"
}
2026-08-10 12:27:40,529 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-24]
2026-08-10 12:27:40,532 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1493729, prompt_len=1712
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "入院记录", "姓名：", "出生地：贵州省天柱县远口镇大样村白蜡树脚组", "性别：女", "民族：苗族", "年龄：37岁", "职业：自由职业者", "婚姻：已婚", "住址：贵", "入院时间：2025-02-24 12:22", "记录时间：2025-02-24 14:28", "入院方式：步行", "主诉：反复胸闷、气促8年，加重半年。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳", "嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐", "渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，", "无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，", "约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，", "门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期", "体重无改变。", "既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病", "史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。", "个人史：[出生于原籍，常住本地，无粉尘放射性物质接触史，否认疫区居住", "史]，[无吸烟史，无饮酒史，否认性病及冶游史]。", "月经史：162~32025/2/21，月经周期规律，色红，量少，无痛经。", "婚育史：24岁结婚，育有1子1女，配偶及子女体健。", "家族史：家族中无同类病人。直系亲属体健。无遗传倾向疾患。", "病史陈述者签名：", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜", "色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，", "巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常", "分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-", "颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤", "正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦"]

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
2026-08-10 12:27:55,066 INFO     29 [qwen-vl-text] coord API raw response (len=2653):
[
	{"text": "姓名：", "bbox": [173, 31, 214, 50]},
	{"text": "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "bbox": [285, 31, 798, 50]},
	{"text": "220999152", "bbox": [173, 50, 250, 67]},
	{"text": "入院记录", "bbox": [477, 87, 547, 105]},
	{"text": "姓名：", "bbox": [173, 126, 214, 145]},
	{"text": "出生地：贵州省天柱县远口镇大样村白蜡树脚组", "bbox": [451, 126, 805, 145]},
	{"text": "性别：女", "bbox": [173, 155, 241, 173]},
	{"text": "民族：苗族", "bbox": [451, 155, 535, 173]},
	{"text": "年龄：37岁", "bbox": [173, 182, 256, 200]},
	{"text": "职业：自由职业者", "bbox": [451, 182, 584, 200]},
	{"text": "婚姻：已婚", "bbox": [173, 209, 257, 227]},
	{"text": "住址：贵", "bbox": [451, 209, 517, 227]},
	{"text": "入院时间：2025-02-24 12:22", "bbox": [173, 237, 394, 255]},
	{"text": "记录时间：2025-02-24 14:28", "bbox": [451, 237, 670, 255]},
	{"text": "入院方式：步行", "bbox": [173, 264, 291, 282]},
	{"text": "主诉：反复胸闷、气促8年，加重半年。", "bbox": [173, 291, 461, 309]},
	{"text": "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳", "bbox": [173, 318, 837, 337]},
	{"text": "嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐", "bbox": [173, 345, 844, 364]},
	{"text": "渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，", "bbox": [173, 372, 833, 391]},
	{"text": "无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，", "bbox": [173, 399, 833, 418]},
	{"text": "约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，", "bbox": [173, 426, 850, 445]},
	{"text": "门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期", "bbox": [173, 453, 844, 472]},
	{"text": "体重无改变。", "bbox": [173, 480, 273, 499]},
	{"text": "既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病", "bbox": [173, 507, 844, 526]},
	{"text": "史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。", "bbox": [173, 534, 753, 553]},
	{"text": "个人史：[出生于原籍，常住本地，无粉尘放射性物质接触史，否认疫区居住", "bbox": [173, 561, 845, 580]},
	{"text": "史]，[无吸烟史，无饮酒史，否认性病及冶游史]。", "bbox": [173, 588, 637, 607]},
	{"text": "月经史：162~32025/2/21，月经周期规律，色红，量少，无痛经。", "bbox": [173, 615, 676, 634]},
	{"text": "婚育史：24岁结婚，育有1子1女，配偶及子女体健。", "bbox": [173, 643, 553, 662]},
	{"text": "家族史：家族中无同类病人。直系亲属体健。无遗传倾向疾患。", "bbox": [173, 670, 670, 689]},
	{"text": "病史陈述者签名：", "bbox": [173, 697, 299, 716]},
	{"text": "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "bbox": [173, 724, 845, 743]},
	{"text": "氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜", "bbox": [173, 751, 845, 770]},
	{"text": "色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，", "bbox": [173, 778, 835, 797]},
	{"text": "巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常", "bbox": [173, 805, 836, 824]},
	{"text": "分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-", "bbox": [173, 832, 836, 851]},
	{"text": "颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤", "bbox": [173, 859, 845, 878]},
	{"text": "正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦", "bbox": [173, 886, 845, 905]}
]
2026-08-10 12:27:55,067 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=14.5s
2026-08-10 12:27:55,067 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[173, 31, 214, 50]
2026-08-10 12:27:55,067 INFO     29 [qwen-vl-text] coord item[1]: text=性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：, bbox=[285, 31, 798, 50]
2026-08-10 12:27:55,067 INFO     29 [qwen-vl-text] coord item[2]: text=220999152, bbox=[173, 50, 250, 67]
2026-08-10 12:27:55,067 INFO     29 [qwen-vl-text] coord item[3]: text=入院记录, bbox=[477, 87, 547, 105]
2026-08-10 12:27:55,067 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[173, 126, 214, 145]
2026-08-10 12:27:55,068 INFO     29 [qwen-vl-text] coord item[5]: text=出生地：贵州省天柱县远口镇大样村白蜡树脚组, bbox=[451, 126, 805, 145]
2026-08-10 12:27:55,068 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女, bbox=[173, 155, 241, 173]
2026-08-10 12:27:55,068 INFO     29 [qwen-vl-text] coord item[7]: text=民族：苗族, bbox=[451, 155, 535, 173]
2026-08-10 12:27:55,068 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：37岁, bbox=[173, 182, 256, 200]
2026-08-10 12:27:55,068 INFO     29 [qwen-vl-text] coord item[9]: text=职业：自由职业者, bbox=[451, 182, 584, 200]
2026-08-10 12:27:55,070 INFO     29 [qwen-vl-text] coord item[10]: text=婚姻：已婚, bbox=[173, 209, 257, 227]
2026-08-10 12:27:55,070 INFO     29 [qwen-vl-text] coord item[11]: text=住址：贵, bbox=[451, 209, 517, 227]
2026-08-10 12:27:55,070 INFO     29 [qwen-vl-text] coord item[12]: text=入院时间：2025-02-24 12:22, bbox=[173, 237, 394, 255]
2026-08-10 12:27:55,070 INFO     29 [qwen-vl-text] coord item[13]: text=记录时间：2025-02-24 14:28, bbox=[451, 237, 670, 255]
2026-08-10 12:27:55,070 INFO     29 [qwen-vl-text] coord item[14]: text=入院方式：步行, bbox=[173, 264, 291, 282]
2026-08-10 12:27:55,070 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：反复胸闷、气促8年，加重半年。, bbox=[173, 291, 461, 309]
2026-08-10 12:27:55,070 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳, bbox=[173, 318, 837, 337]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[17]: text=嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐, bbox=[173, 345, 844, 364]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[18]: text=渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，, bbox=[173, 372, 833, 391]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[19]: text=无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，, bbox=[173, 399, 833, 418]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[20]: text=约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，, bbox=[173, 426, 850, 445]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[21]: text=门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期, bbox=[173, 453, 844, 472]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[22]: text=体重无改变。, bbox=[173, 480, 273, 499]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[23]: text=既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病, bbox=[173, 507, 844, 526]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[24]: text=史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。, bbox=[173, 534, 753, 553]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[25]: text=个人史：[出生于原籍，常住本地，无粉尘放射性物质接触史，否认疫区居住, bbox=[173, 561, 845, 580]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[26]: text=史]，[无吸烟史，无饮酒史，否认性病及冶游史]。, bbox=[173, 588, 637, 607]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[27]: text=月经史：162~32025/2/21，月经周期规律，色红，量少，无痛经。, bbox=[173, 615, 676, 634]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[28]: text=婚育史：24岁结婚，育有1子1女，配偶及子女体健。, bbox=[173, 643, 553, 662]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[29]: text=家族史：家族中无同类病人。直系亲属体健。无遗传倾向疾患。, bbox=[173, 670, 670, 689]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[30]: text=病史陈述者签名：, bbox=[173, 697, 299, 716]
2026-08-10 12:27:55,071 INFO     29 [qwen-vl-text] coord item[31]: text=体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸, bbox=[173, 724, 845, 743]
2026-08-10 12:27:55,072 INFO     29 [qwen-vl-text] coord item[32]: text=氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜, bbox=[173, 751, 845, 770]
2026-08-10 12:27:55,072 INFO     29 [qwen-vl-text] coord item[33]: text=色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，, bbox=[173, 778, 835, 797]
2026-08-10 12:27:55,072 INFO     29 [qwen-vl-text] coord item[34]: text=巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常, bbox=[173, 805, 836, 824]
2026-08-10 12:27:55,072 INFO     29 [qwen-vl-text] coord item[35]: text=分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-, bbox=[173, 832, 836, 851]
2026-08-10 12:27:55,072 INFO     29 [qwen-vl-text] coord item[36]: text=颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤, bbox=[173, 859, 845, 878]
2026-08-10 12:27:55,072 INFO     29 [qwen-vl-text] coord item[37]: text=正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦, bbox=[173, 886, 845, 905]
2026-08-10 12:27:55,072 INFO     29 [qwen-vl-text] page=13 — 38/38 coords, api_time=14.5s
2026-08-10 12:27:55,072 INFO     29 [qwen-vl-text] new_positions (38):
[[13, 145.666, 180.188, 18.445, 29.75], [13, 239.97, 671.9159999999999, 18.445, 29.75], [13, 145.666, 210.5, 29.75, 39.864999999999995], [13, 401.63399999999996, 460.574, 51.765, 62.474999999999994], [13, 145.666, 180.188, 74.97, 86.27499999999999], [13, 379.74199999999996, 677.81, 74.97, 86.27499999999999], [13, 145.666, 202.922, 92.225, 102.935], [13, 379.74199999999996, 450.46999999999997, 92.225, 102.935], [13, 145.666, 215.552, 108.28999999999999, 119.0], [13, 379.74199999999996, 491.728, 108.28999999999999, 119.0], [13, 145.666, 216.394, 124.35499999999999, 135.065], [13, 379.74199999999996, 435.31399999999996, 124.35499999999999, 135.065], [13, 145.666, 331.748, 141.015, 151.725], [13, 379.74199999999996, 564.14, 141.015, 151.725], [13, 145.666, 245.022, 157.07999999999998, 167.79], [13, 145.666, 388.162, 173.14499999999998, 183.855], [13, 145.666, 704.754, 189.20999999999998, 200.515], [13, 145.666, 710.648, 205.27499999999998, 216.57999999999998], [13, 145.666, 701.386, 221.34, 232.64499999999998], [13, 145.666, 701.386, 237.405, 248.70999999999998], [13, 145.666, 715.6999999999999, 253.47, 264.775], [13, 145.666, 710.648, 269.53499999999997, 280.84], [13, 145.666, 229.86599999999999, 285.59999999999997, 296.905], [13, 145.666, 710.648, 301.66499999999996, 312.96999999999997], [13, 145.666, 634.026, 317.72999999999996, 329.03499999999997], [13, 145.666, 711.49, 333.79499999999996, 345.09999999999997], [13, 145.666, 536.3539999999999, 349.85999999999996, 361.16499999999996], [13, 145.666, 569.192, 365.925, 377.22999999999996], [13, 145.666, 465.626, 382.585, 393.89], [13, 145.666, 564.14, 398.65, 409.955], [13, 145.666, 251.75799999999998, 414.715, 426.02], [13, 145.666, 711.49, 430.78, 442.085], [13, 145.666, 711.49, 446.84499999999997, 458.15], [13, 145.666, 703.0699999999999, 462.90999999999997, 474.215], [13, 145.666, 703.9119999999999, 478.97499999999997, 490.28], [13, 145.666, 703.9119999999999, 495.03999999999996, 506.34499999999997], [13, 145.666, 711.49, 511.10499999999996, 522.41], [13, 145.666, 711.49, 527.17, 538.475]]
2026-08-10 12:27:55,073 INFO     29 [qwen-vl-text] ═══ DONE ═══ 38 positions, pages=1, time=23.7s
2026-08-10 12:27:55,080 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 12:27:55,080 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:Admission | outputs={"chunks": "3 items, types={'AdmissionRecord': 3}", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:27:55,080 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 12:27:55,088 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:27:55,089 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:27:55,089 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:27:55,090 INFO     29 [qwen-vl-text] positions(25): [[2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:27:55,090 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [1, 24]
2026-08-10 12:27:55,355 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:27:55,537 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:27:55,539 INFO     29 [qwen-vl-text] LLM extraction start, text_len=382
2026-08-10 12:27:55,539 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:27:55,540 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 54, \"bbox_end\": 78, \"encounter_dates\": [\"2025-02-25\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告时间: 2025-02-24\n怀化市肿瘤医院\n怀化市第二人民医院\n鹤城院区\n湖南HR\nCT影像诊断报告单\nID: 86562633\n检查号: CT00525514\n姓名:\n性别: 女\n年龄: 37岁\n住院号: 220999152\n床号: 46\n申请科室: 呼吸与危重症医学科\n申请医生: 易莹\n检查日期: 2025.02.25\n报告日期: 2025.02.25 09:45:16\n检查项目: CT成套:胸部(平扫(三维重建))\n检查所见:\n右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见\n条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主\n要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。\n意见:\n1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。\n2. 右肺中叶少许慢性炎症。",
    "role": "user"
  }
]
2026-08-10 12:27:58,664 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:27:58,664 INFO     29 [qwen-vl-text] LLM output (len=482):
{
  "exam_date": "2025-02-25",
  "report_date": "2025-02-25",
  "exam_name": "CT成套:胸部(平扫(三维重建))",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "呼吸与危重症医学科",
  "bed_number": "46",
  "findings": "右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。",
  "conclusion": "1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。\n2. 右肺中叶少许慢性炎症。",
  "physician": null,
  "reviewer": null
}
2026-08-10 12:27:58,667 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1719494, prompt_len=631
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["报告时间: 2025-02-24"]

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
2026-08-10 12:28:00,202 INFO     29 [qwen-vl-text] coord API raw response (len=75):
```json
[
	{"text": "报告时间: 2025-02-24", "bbox": [478, 152, 598, 166]}
]
```
2026-08-10 12:28:00,202 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 12:28:00,202 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间: 2025-02-24, bbox=[478, 152, 598, 166]
2026-08-10 12:28:00,203 INFO     29 [qwen-vl-text] page=2 — 1/1 coords, api_time=1.5s
2026-08-10 12:28:00,204 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=699247, prompt_len=1050
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["怀化市肿瘤医院", "怀化市第二人民医院", "鹤城院区", "湖南HR", "CT影像诊断报告单", "ID: 86562633", "检查号: CT00525514", "姓名:", "性别: 女", "年龄: 37岁", "住院号: 220999152", "床号: 46", "申请科室: 呼吸与危重症医学科", "申请医生: 易莹", "检查日期: 2025.02.25", "报告日期: 2025.02.25 09:45:16", "检查项目: CT成套:胸部(平扫(三维重建))", "检查所见:", "右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见", "条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主", "要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "意见:", "1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。", "2. 右肺中叶少许慢性炎症。"]

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
2026-08-10 12:28:09,515 INFO     29 [qwen-vl-text] coord API raw response (len=1415):
[
	{"text": "怀化市肿瘤医院", "bbox": [206, 35, 389, 57]},
	{"text": "怀化市第二人民医院", "bbox": [206, 62, 389, 83]},
	{"text": "鹤城院区", "bbox": [393, 46, 482, 68]},
	{"text": "湖南HR", "bbox": [630, 50, 712, 75]},
	{"text": "CT影像诊断报告单", "bbox": [400, 95, 620, 120]},
	{"text": "ID: 86562633", "bbox": [142, 132, 261, 147]},
	{"text": "检查号: CT00525514", "bbox": [482, 126, 631, 142]},
	{"text": "姓名:", "bbox": [141, 160, 182, 177]},
	{"text": "性别: 女", "bbox": [335, 160, 402, 177]},
	{"text": "年龄: 37岁", "bbox": [470, 160, 546, 177]},
	{"text": "住院号: 220999152", "bbox": [589, 160, 726, 177]},
	{"text": "床号: 46", "bbox": [764, 160, 825, 177]},
	{"text": "申请科室: 呼吸与危重症医学科", "bbox": [142, 184, 373, 202]},
	{"text": "申请医生: 易莹", "bbox": [471, 184, 588, 202]},
	{"text": "检查日期: 2025.02.25", "bbox": [141, 210, 307, 227]},
	{"text": "报告日期: 2025.02.25 09:45:16", "bbox": [470, 210, 710, 227]},
	{"text": "检查项目: CT成套:胸部(平扫(三维重建))", "bbox": [139, 239, 441, 257]},
	{"text": "检查所见:", "bbox": [140, 299, 212, 317]},
	{"text": "右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见", "bbox": [183, 326, 854, 345]},
	{"text": "条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主", "bbox": [147, 350, 854, 369]},
	{"text": "要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "bbox": [146, 375, 657, 394]},
	{"text": "意见:", "bbox": [136, 704, 174, 722]},
	{"text": "1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。", "bbox": [144, 727, 610, 746]},
	{"text": "2. 右肺中叶少许慢性炎症。", "bbox": [144, 747, 366, 767]}
]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=9.3s
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[0]: text=怀化市肿瘤医院, bbox=[206, 35, 389, 57]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[1]: text=怀化市第二人民医院, bbox=[206, 62, 389, 83]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[2]: text=鹤城院区, bbox=[393, 46, 482, 68]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[3]: text=湖南HR, bbox=[630, 50, 712, 75]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[4]: text=CT影像诊断报告单, bbox=[400, 95, 620, 120]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[5]: text=ID: 86562633, bbox=[142, 132, 261, 147]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[6]: text=检查号: CT00525514, bbox=[482, 126, 631, 142]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[141, 160, 182, 177]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[8]: text=性别: 女, bbox=[335, 160, 402, 177]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[9]: text=年龄: 37岁, bbox=[470, 160, 546, 177]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[10]: text=住院号: 220999152, bbox=[589, 160, 726, 177]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[11]: text=床号: 46, bbox=[764, 160, 825, 177]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[12]: text=申请科室: 呼吸与危重症医学科, bbox=[142, 184, 373, 202]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[13]: text=申请医生: 易莹, bbox=[471, 184, 588, 202]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[14]: text=检查日期: 2025.02.25, bbox=[141, 210, 307, 227]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[15]: text=报告日期: 2025.02.25 09:45:16, bbox=[470, 210, 710, 227]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[16]: text=检查项目: CT成套:胸部(平扫(三维重建)), bbox=[139, 239, 441, 257]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[17]: text=检查所见:, bbox=[140, 299, 212, 317]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[18]: text=右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见, bbox=[183, 326, 854, 345]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[19]: text=条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主, bbox=[147, 350, 854, 369]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[20]: text=要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。, bbox=[146, 375, 657, 394]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[21]: text=意见:, bbox=[136, 704, 174, 722]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[22]: text=1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。, bbox=[144, 727, 610, 746]
2026-08-10 12:28:09,516 INFO     29 [qwen-vl-text] coord item[23]: text=2. 右肺中叶少许慢性炎症。, bbox=[144, 747, 366, 767]
2026-08-10 12:28:09,517 INFO     29 [qwen-vl-text] page=3 — 24/24 coords, api_time=9.3s
2026-08-10 12:28:09,517 INFO     29 [qwen-vl-text] new_positions (25):
[[2, 402.476, 503.51599999999996, 90.44, 98.77], [3, 173.452, 327.538, 20.825, 33.915], [3, 173.452, 327.538, 36.89, 49.385], [3, 330.906, 405.844, 27.369999999999997, 40.46], [3, 530.46, 599.504, 29.75, 44.625], [3, 336.8, 522.04, 56.525, 71.39999999999999], [3, 119.564, 219.762, 78.53999999999999, 87.46499999999999], [3, 405.844, 531.302, 74.97, 84.49], [3, 118.722, 153.244, 95.19999999999999, 105.315], [3, 282.07, 338.484, 95.19999999999999, 105.315], [3, 395.74, 459.73199999999997, 95.19999999999999, 105.315], [3, 495.938, 611.292, 95.19999999999999, 105.315], [3, 643.288, 694.65, 95.19999999999999, 105.315], [3, 119.564, 314.066, 109.47999999999999, 120.19], [3, 396.582, 495.096, 109.47999999999999, 120.19], [3, 118.722, 258.49399999999997, 124.94999999999999, 135.065], [3, 395.74, 597.8199999999999, 124.94999999999999, 135.065], [3, 117.038, 371.322, 142.20499999999998, 152.915], [3, 117.88, 178.504, 177.905, 188.61499999999998], [3, 154.08599999999998, 719.068, 193.97, 205.27499999999998], [3, 123.774, 719.068, 208.25, 219.55499999999998], [3, 122.932, 553.194, 223.125, 234.42999999999998], [3, 114.512, 146.50799999999998, 418.88, 429.59], [3, 121.24799999999999, 513.62, 432.565, 443.87], [3, 121.24799999999999, 308.17199999999997, 444.465, 456.36499999999995]]
2026-08-10 12:28:09,517 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=2, time=14.4s
2026-08-10 12:28:09,517 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:28:09,523 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:28:09,523 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:28:09,523 INFO     29 [qwen-vl-text] positions(24): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:28:09,523 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [24]
2026-08-10 12:28:09,709 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 12:28:09,710 INFO     29 [qwen-vl-text] LLM extraction start, text_len=430
2026-08-10 12:28:09,710 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:28:09,710 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 79, \"bbox_end\": 102, \"encounter_dates\": [\"2025-07-11\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "怀化市中心医院\nHUAIHUA CENTRAL HOSPITAL\n怀化市肿瘤医院\n湖南HR\nCT影像诊断报告单\nID: 93717786\n检查号: CT00568277\n姓名:\n性别: 女\n年龄: 37岁\n住院号: 221028180\n床号: 42\n申请科室: 呼吸与危重症医学科\n申请医生:\n检查日期: 2025.07.11\n报告日期: 2025.07.11 16:08:56\n检查项目: CT成套胸部平扫(三维重建)\n检查所见:\n与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。\n右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部\n分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。\n意见:\n1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。\n2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。",
    "role": "user"
  }
]
2026-08-10 12:28:09,712 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:28:09.712+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:28:13,166 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:28:13,166 INFO     29 [qwen-vl-text] LLM output (len=534):
{
  "exam_date": "2025-07-11",
  "report_date": "2025-07-11",
  "exam_name": "CT成套胸部平扫(三维重建)",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "呼吸与危重症医学科",
  "bed_number": "42",
  "findings": "与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。\n右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。",
  "conclusion": "1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。\n2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。",
  "physician": null,
  "reviewer": null
}
2026-08-10 12:28:13,169 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=724530, prompt_len=1115
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["怀化市中心医院", "HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "湖南HR", "CT影像诊断报告单", "ID: 93717786", "检查号: CT00568277", "姓名:", "性别: 女", "年龄: 37岁", "住院号: 221028180", "床号: 42", "申请科室: 呼吸与危重症医学科", "申请医生:", "检查日期: 2025.07.11", "报告日期: 2025.07.11 16:08:56", "检查项目: CT成套胸部平扫(三维重建)", "检查所见:", "与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。", "右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部", "分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "意见:", "1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。", "2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。"]

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
2026-08-10 12:28:23,672 INFO     29 [qwen-vl-text] coord API raw response (len=1870):
[
	{"text": "怀化市中心医院", "bbox": [204, 27, 356, 48]},
	{"text": "HUAIHUA CENTRAL HOSPITAL", "bbox": [204, 49, 356, 60]},
	{"text": "怀化市肿瘤医院", "bbox": [204, 65, 356, 80]},
	{"text": "湖南HR", "bbox": [632, 43, 718, 69]},
	{"text": "CT影像诊断报告单", "bbox": [395, 89, 622, 116]},
	{"text": "ID: 93717786", "bbox": [137, 129, 255, 144]},
	{"text": "检查号: CT00568277", "bbox": [480, 122, 633, 138]},
	{"text": "姓名:", "bbox": [136, 157, 177, 175], "bbox": [136, 157, 177, 175]},
	{"text": "性别: 女", "bbox": [330, 157, 398, 175]},
	{"text": "年龄: 37岁", "bbox": [468, 157, 546, 175]},
	{"text": "住院号: 221028180", "bbox": [590, 157, 731, 175]},
	{"text": "床号: 42", "bbox": [770, 157, 833, 175]},
	{"text": "申请科室: 呼吸与危重症医学科", "bbox": [137, 182, 370, 200], "bbox": [137, 182, 370, 200]},
	{"text": "申请医生:", "bbox": [470, 182, 546, 200], "bbox": [470, 182, 546, 200]},
	{"text": "检查日期: 2025.07.11", "bbox": [136, 208, 304, 226], "bbox": [136, 208, 304, 226]},
	{"text": "报告日期: 2025.07.11 16:08:56", "bbox": [468, 208, 714, 226], "bbox": [468, 208, 714, 226]},
	{"text": "检查项目: CT成套胸部平扫(三维重建)", "bbox": [134, 237, 414, 255], "bbox": [134, 237, 414, 255]},
	{"text": "检查所见:", "bbox": [137, 296, 210, 314], "bbox": [137, 296, 210, 314]},
	{"text": "与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。", "bbox": [175, 323, 854, 340], "bbox": [175, 323, 854, 340]},
	{"text": "右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部", "bbox": [143, 342, 860, 359], "bbox": [143, 342, 860, 359]},
	{"text": "分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "bbox": [143, 361, 838, 378], "bbox": [143, 361, 838, 378]},
	{"text": "意见:", "bbox": [136, 703, 176, 721], "bbox": [136, 703, 176, 721]},
	{"text": "1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。", "bbox": [144, 727, 691, 745], "bbox": [144, 727, 691, 745]},
	{"text": "2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。", "bbox": [144, 746, 604, 765], "bbox": [144, 746, 604, 765]}
]
2026-08-10 12:28:23,673 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=10.5s
2026-08-10 12:28:23,673 INFO     29 [qwen-vl-text] coord item[0]: text=怀化市中心医院, bbox=[204, 27, 356, 48]
2026-08-10 12:28:23,673 INFO     29 [qwen-vl-text] coord item[1]: text=HUAIHUA CENTRAL HOSPITAL, bbox=[204, 49, 356, 60]
2026-08-10 12:28:23,673 INFO     29 [qwen-vl-text] coord item[2]: text=怀化市肿瘤医院, bbox=[204, 65, 356, 80]
2026-08-10 12:28:23,673 INFO     29 [qwen-vl-text] coord item[3]: text=湖南HR, bbox=[632, 43, 718, 69]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[4]: text=CT影像诊断报告单, bbox=[395, 89, 622, 116]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[5]: text=ID: 93717786, bbox=[137, 129, 255, 144]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[6]: text=检查号: CT00568277, bbox=[480, 122, 633, 138]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[136, 157, 177, 175]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[8]: text=性别: 女, bbox=[330, 157, 398, 175]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[9]: text=年龄: 37岁, bbox=[468, 157, 546, 175]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[10]: text=住院号: 221028180, bbox=[590, 157, 731, 175]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[11]: text=床号: 42, bbox=[770, 157, 833, 175]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[12]: text=申请科室: 呼吸与危重症医学科, bbox=[137, 182, 370, 200]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[13]: text=申请医生:, bbox=[470, 182, 546, 200]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[14]: text=检查日期: 2025.07.11, bbox=[136, 208, 304, 226]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[15]: text=报告日期: 2025.07.11 16:08:56, bbox=[468, 208, 714, 226]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[16]: text=检查项目: CT成套胸部平扫(三维重建), bbox=[134, 237, 414, 255]
2026-08-10 12:28:23,674 INFO     29 [qwen-vl-text] coord item[17]: text=检查所见:, bbox=[137, 296, 210, 314]
2026-08-10 12:28:23,675 INFO     29 [qwen-vl-text] coord item[18]: text=与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。, bbox=[175, 323, 854, 340]
2026-08-10 12:28:23,675 INFO     29 [qwen-vl-text] coord item[19]: text=右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部, bbox=[143, 342, 860, 359]
2026-08-10 12:28:23,675 INFO     29 [qwen-vl-text] coord item[20]: text=分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。, bbox=[143, 361, 838, 378]
2026-08-10 12:28:23,675 INFO     29 [qwen-vl-text] coord item[21]: text=意见:, bbox=[136, 703, 176, 721]
2026-08-10 12:28:23,675 INFO     29 [qwen-vl-text] coord item[22]: text=1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。, bbox=[144, 727, 691, 745]
2026-08-10 12:28:23,675 INFO     29 [qwen-vl-text] coord item[23]: text=2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。, bbox=[144, 746, 604, 765]
2026-08-10 12:28:23,675 INFO     29 [qwen-vl-text] page=4 — 24/24 coords, api_time=10.5s
2026-08-10 12:28:23,675 INFO     29 [qwen-vl-text] new_positions (24):
[[4, 171.768, 299.752, 16.064999999999998, 28.56], [4, 171.768, 299.752, 29.154999999999998, 35.699999999999996], [4, 171.768, 299.752, 38.675, 47.599999999999994], [4, 532.144, 604.5559999999999, 25.584999999999997, 41.055], [4, 332.59, 523.7239999999999, 52.955, 69.02], [4, 115.354, 214.70999999999998, 76.755, 85.67999999999999], [4, 404.15999999999997, 532.986, 72.59, 82.11], [4, 114.512, 149.034, 93.41499999999999, 104.125], [4, 277.86, 335.116, 93.41499999999999, 104.125], [4, 394.056, 459.73199999999997, 93.41499999999999, 104.125], [4, 496.78, 615.502, 93.41499999999999, 104.125], [4, 648.34, 701.386, 93.41499999999999, 104.125], [4, 115.354, 311.53999999999996, 108.28999999999999, 119.0], [4, 395.74, 459.73199999999997, 108.28999999999999, 119.0], [4, 114.512, 255.968, 123.75999999999999, 134.47], [4, 394.056, 601.188, 123.75999999999999, 134.47], [4, 112.828, 348.58799999999997, 141.015, 151.725], [4, 115.354, 176.82, 176.12, 186.82999999999998], [4, 147.35, 719.068, 192.185, 202.29999999999998], [4, 120.40599999999999, 724.12, 203.48999999999998, 213.605], [4, 120.40599999999999, 705.596, 214.795, 224.91], [4, 114.512, 148.192, 418.28499999999997, 428.995], [4, 121.24799999999999, 581.822, 432.565, 443.275], [4, 121.24799999999999, 508.568, 443.87, 455.17499999999995]]
2026-08-10 12:28:23,676 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=14.2s
2026-08-10 12:28:23,676 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:28:23,678 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:28:23,678 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:28:23,678 INFO     29 [qwen-vl-text] positions(230): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:28:23,678 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [230]
2026-08-10 12:28:23,858 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:28:23,859 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1251
2026-08-10 12:28:23,859 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:28:23,859 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 333, \"bbox_end\": 562, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"呼吸科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "姓名：\n年龄：38岁\n性别：女\n科别：\n保险：\n预计值模式：Standard-new\n常规通气报告\n测试号：2026020917\n身高：165 cm\n体重：60 kg\n备注：\n联系电话：\n操作者：蒋细萍\nPred\nBst % (B/Pd\nA1\nA2\nA3\nFVC\n[L]\n2.99\n2.21\n74.02\n2.21\n2.12\n2.09\nFEV 1\n[L]\n2.67\n1.26\n48.56\n1.26\n1.13\n1.18\nFEV6\n[L]\n2.12\n2.12\n2.05\n2.02\nFEV 1 % FVC\n[%]\n84.19\n56.48\n67.09\n56.48\n53.33\n56.67\nFEV 1 % VC MAX\n[%]\n81.88\n55.26\n67.48\n55.26\n50.10\n52.31\nVC MAX\n[L]\n3.03\n2.26\n74.60\nPEF\n[L/s]\n6.28\n2.66\n42.36\n2.66\n2.58\n2.43\nMMEF 75/25\n[L/s]\n3.57\n0.51\n14.35\n0.51\n0.49\n0.41\nMEF 75\n[L/s]\n5.64\n1.47\n26.14\n1.47\n0.80\n1.21\nMEF 50\n[L/s]\n4.01\n0.68\n16.97\n0.68\n0.72\n0.57\nMEF 25\n[L/s]\n1.79\n0.19\n10.52\n0.19\n0.18\n0.15\nV backextrapolation ex\n[L]\n0.05\n0.05\n0.03\n0.04\nV backextrapol. % FVC\n[%]\n2.07\n2.07\n1.50\n1.81\nFET\n[s]\n7.63\n7.63\n7.35\n7.55\nFEF 200-1200\n[L/s]\n1.19\n1.19\n0.98\n1.05\nFVC IN\n[L]\n3.03\n2.26\n74.60\n2.26\n2.15\n2.13\nFIV1\n[L]\n2.21\n2.21\n2.12\n2.09\nFIV1 % FVC\n[%]\n97.79\n97.79\n98.68\n98.05\nFEF50 % FIF50\n[%]\n22.86\n22.86\n25.05\n19.46\nPIF\n[L/s]\n3.04\n3.04\n3.04\n2.99\nMVV\n[L/min]\n99.77\n46.21\n46.32\n46.21\nBF MVV\n[1/min]\n75.55\n75.55\n意见：\n1. 重度混合性肺通气功能障碍。\n2. 最大分钟通气量（MVV）：显著减退。\nDate\n20/2/00\nTimo\n11:48:04上午\nFlow [L/s]\nF/V ex\nVol [L]\nVol%VCmax\nVCmax\nTime [s]\nVol [L]\nTime [s]\nF/V in\n10\n8\n6\n4\n2\n0\n1\n2\n3\n4\n5\n10\n8\n6\n4\n2\n0\n100\n80\n60\n40\n20\n0\n2\n4\n6\n8\n10\n12\n1\n0\n2\n4\n6\n8\n10\n12\n1\n0\n2\n4\n6\n8\n10\n12\n1\n张",
    "role": "user"
  }
]
2026-08-10 12:28:35,126 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:28:35,126 INFO     29 [qwen-vl-text] LLM output (len=1872):
{
  "exam_date": "2026-02-09",
  "report_date": "2026-02-09",
  "exam_name": "常规通气报告",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "呼吸科门诊",
  "bed_number": null,
  "findings": "预计值模式：Standard-new\n常规通气报告\n测试号：2026020917\n身高：165 cm\n体重：60 kg\n\n| 指标 | 单位 | Pred | Bst | % (B/Pd) | A1 | A2 | A3 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| FVC | [L] | 2.99 | 2.21 | 74.02 | 2.21 | 2.12 | 2.09 |\n| FEV 1 | [L] | 2.67 | 1.26 | 48.56 | 1.26 | 1.13 | 1.18 |\n| FEV6 | [L] | - | 2.12 | - | 2.12 | 2.05 | 2.02 |\n| FEV 1 % FVC | [%] | 84.19 | 56.48 | 67.09 | 56.48 | 53.33 | 56.67 |\n| FEV 1 % VC MAX | [%] | 81.88 | 55.26 | 67.48 | 55.26 | 50.10 | 52.31 |\n| VC MAX | [L] | 3.03 | 2.26 | 74.60 | - | - | - |\n| PEF | [L/s] | 6.28 | 2.66 | 42.36 | 2.66 | 2.58 | 2.43 |\n| MMEF 75/25 | [L/s] | 3.57 | 0.51 | 14.35 | 0.51 | 0.49 | 0.41 |\n| MEF 75 | [L/s] | 5.64 | 1.47 | 26.14 | 1.47 | 0.80 | 1.21 |\n| MEF 50 | [L/s] | 4.01 | 0.68 | 16.97 | 0.68 | 0.72 | 0.57 |\n| MEF 25 | [L/s] | 1.79 | 0.19 | 10.52 | 0.19 | 0.18 | 0.15 |\n| V backextrapolation ex | [L] | - | 0.05 | - | 0.05 | 0.03 | 0.04 |\n| V backextrapol. % FVC | [%] | - | 2.07 | - | 2.07 | 1.50 | 1.81 |\n| FET | [s] | - | 7.63 | - | 7.63 | 7.35 | 7.55 |\n| FEF 200-1200 | [L/s] | - | 1.19 | - | 1.19 | 0.98 | 1.05 |\n| FVC IN | [L] | 3.03 | 2.26 | 74.60 | 2.26 | 2.15 | 2.13 |\n| FIV1 | [L] | - | 2.21 | - | 2.21 | 2.12 | 2.09 |\n| FIV1 % FVC | [%] | - | 97.79 | - | 97.79 | 98.68 | 98.05 |\n| FEF50 % FIF50 | [%] | - | 22.86 | - | 22.86 | 25.05 | 19.46 |\n| PIF | [L/s] | - | 3.04 | - | 3.04 | 3.04 | 2.99 |\n| MVV | [L/min] | 99.77 | 46.21 | 46.32 | 46.21 | - | - |\n| BF MVV | [1/min] | - | 75.55 | - | 75.55 | - | - |",
  "conclusion": "意见：\n1. 重度混合性肺通气功能障碍。\n2. 最大分钟通气量（MVV）：显著减退。",
  "physician": "蒋细萍",
  "reviewer": null
}
2026-08-10 12:28:35,128 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=819324, prompt_len=2555
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共230行）
["姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-new", "常规通气报告", "测试号：2026020917", "身高：165 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "Pred", "Bst % (B/Pd", "A1", "A2", "A3", "FVC", "[L]", "2.99", "2.21", "74.02", "2.21", "2.12", "2.09", "FEV 1", "[L]", "2.67", "1.26", "48.56", "1.26", "1.13", "1.18", "FEV6", "[L]", "2.12", "2.12", "2.05", "2.02", "FEV 1 % FVC", "[%]", "84.19", "56.48", "67.09", "56.48", "53.33", "56.67", "FEV 1 % VC MAX", "[%]", "81.88", "55.26", "67.48", "55.26", "50.10", "52.31", "VC MAX", "[L]", "3.03", "2.26", "74.60", "PEF", "[L/s]", "6.28", "2.66", "42.36", "2.66", "2.58", "2.43", "MMEF 75/25", "[L/s]", "3.57", "0.51", "14.35", "0.51", "0.49", "0.41", "MEF 75", "[L/s]", "5.64", "1.47", "26.14", "1.47", "0.80", "1.21", "MEF 50", "[L/s]", "4.01", "0.68", "16.97", "0.68", "0.72", "0.57", "MEF 25", "[L/s]", "1.79", "0.19", "10.52", "0.19", "0.18", "0.15", "V backextrapolation ex", "[L]", "0.05", "0.05", "0.03", "0.04", "V backextrapol. % FVC", "[%]", "2.07", "2.07", "1.50", "1.81", "FET", "[s]", "7.63", "7.63", "7.35", "7.55", "FEF 200-1200", "[L/s]", "1.19", "1.19", "0.98", "1.05", "FVC IN", "[L]", "3.03", "2.26", "74.60", "2.26", "2.15", "2.13", "FIV1", "[L]", "2.21", "2.21", "2.12", "2.09", "FIV1 % FVC", "[%]", "97.79", "97.79", "98.68", "98.05", "FEF50 % FIF50", "[%]", "22.86", "22.86", "25.05", "19.46", "PIF", "[L/s]", "3.04", "3.04", "3.04", "2.99", "MVV", "[L/min]", "99.77", "46.21", "46.32", "46.21", "BF MVV", "[1/min]", "75.55", "75.55", "意见：", "1. 重度混合性肺通气功能障碍。", "2. 最大分钟通气量（MVV）：显著减退。", "Date", "20/2/00", "Timo", "11:48:04上午", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%VCmax", "VCmax", "Time [s]", "Vol [L]", "Time [s]", "F/V in", "10", "8", "6", "4", "2", "0", "1", "2", "3", "4", "5", "10", "8", "6", "4", "2", "0", "100", "80", "60", "40", "20", "0", "2", "4", "6", "8", "10", "12", "1", "0", "2", "4", "6", "8", "10", "12", "1", "0", "2", "4", "6", "8", "10", "12", "1", "张"]

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
2026-08-10 12:29:29,472 INFO     29 [qwen-vl-text] coord API raw response (len=10633):
[
	{"text": "姓名：", "bbox": [225, 80, 265, 93]},
	{"text": "年龄：38岁", "bbox": [225, 93, 408, 107]},
	{"text": "性别：女", "bbox": [225, 107, 385, 120]},
	{"text": "科别：", "bbox": [225, 120, 265, 133]},
	{"text": "保险：", "bbox": [225, 133, 265, 146]},
	{"text": "预计值模式：Standard-new", "bbox": [225, 146, 464, 159]},
	{"text": "常规通气报告", "bbox": [472, 67, 563, 80]},
	{"text": "测试号：2026020917", "bbox": [519, 80, 738, 93]},
	{"text": "身高：165 cm", "bbox": [519, 93, 708, 107]},
	{"text": "体重：60 kg", "bbox": [660, 107, 700, 120]},
	{"text": "备注：", "bbox": [519, 120, 557, 133]},
	{"text": "联系电话：", "bbox": [519, 133, 587, 146]},
	{"text": "操作者：蒋细萍", "bbox": [519, 146, 707, 159]},
	{"text": "Pred", "bbox": [341, 161, 374, 173]},
	{"text": "Bst % (B/Pd", "bbox": [405, 161, 487, 173]},
	{"text": "A1", "bbox": [527, 161, 542, 173]},
	{"text": "A2", "bbox": [584, 161, 601, 173]},
	{"text": "A3", "bbox": [642, 161, 658, 173]},
	{"text": "FVC", "bbox": [90, 188, 114, 200]},
	{"text": "[L]", "bbox": [293, 188, 315, 200]},
	{"text": "2.99", "bbox": [341, 188, 374, 200]},
	{"text": "2.21", "bbox": [398, 188, 429, 200]},
	{"text": "74.02", "bbox": [447, 188, 487, 200]},
	{"text": "2.21", "bbox": [512, 188, 542, 200]},
	{"text": "2.12", "bbox": [569, 188, 601, 200]},
	{"text": "2.09", "bbox": [625, 188, 658, 200]},
	{"text": "FEV 1", "bbox": [90, 201, 128, 213]},
	{"text": "[L]", "bbox": [293, 201, 315, 213]},
	{"text": "2.67", "bbox": [341, 201, 374, 213]},
	{"text": "1.26", "bbox": [398, 201, 429, 213]},
	{"text": "48.56", "bbox": [447, 201, 487, 213]},
	{"text": "1.26", "bbox": [512, 201, 542, 213]},
	{"text": "1.13", "bbox": [569, 201, 601, 213]},
	{"text": "1.18", "bbox": [625, 201, 658, 213]},
	{"text": "FEV6", "bbox": [90, 214, 121, 226]},
	{"text": "[L]", "bbox": [293, 214, 315, 226]},
	{"text": "2.12", "bbox": [398, 214, 429, 226]},
	{"text": "2.12", "bbox": [512, 214, 542, 226]},
	{"text": "2.05", "bbox": [569, 214, 601, 226]},
	{"text": "2.02", "bbox": [625, 214, 658, 226]},
	{"text": "FEV 1 % FVC", "bbox": [90, 227, 179, 239]},
	{"text": "[%]", "bbox": [293, 227, 315, 239]},
	{"text": "84.19", "bbox": [334, 227, 374, 239]},
	{"text": "56.48", "bbox": [391, 227, 429, 239]},
	{"text": "67.09", "bbox": [447, 227, 487, 239]},
	{"text": "56.48", "bbox": [504, 227, 542, 239]},
	{"text": "53.33", "bbox": [561, 227, 601, 239]},
	{"text": "56.67", "bbox": [617, 227, 658, 239]},
	{"text": "FEV 1 % VC MAX", "bbox": [90, 240, 203, 253]},
	{"text": "[%]", "bbox": [293, 240, 315, 253]},
	{"text": "81.88", "bbox": [334, 240, 374, 253]},
	{"text": "55.26", "bbox": [391, 240, 429, 253]},
	{"text": "67.48", "bbox": [447, 240, 487, 253]},
	{"text": "55.26", "bbox": [504, 240, 542, 253]},
	{"text": "50.10", "bbox": [561, 240, 601, 253]},
	{"text": "52.31", "bbox": [617, 240, 658, 253]},
	{"text": "VC MAX", "bbox": [90, 254, 138, 266]},
	{"text": "[L]", "bbox": [293, 254, 315, 266]},
	{"text": "3.03", "bbox": [341, 254, 374, 266]},
	{"text": "2.26", "bbox": [398, 254, 429, 266]},
	{"text": "74.60", "bbox": [447, 254, 487, 266]},
	{"text": "PEF", "bbox": [90, 267, 114, 279]},
	{"text": "[L/s]", "bbox": [277, 267, 315, 279]},
	{"text": "6.28", "bbox": [341, 267, 374, 279]},
	{"text": "2.66", "bbox": [398, 267, 429, 279]},
	{"text": "42.36", "bbox": [447, 267, 487, 279]},
	{"text": "2.66", "bbox": [512, 267, 542, 279]},
	{"text": "2.58", "bbox": [569, 267, 601, 279]},
	{"text": "2.43", "bbox": [625, 267, 658, 279]},
	{"text": "MMEF 75/25", "bbox": [90, 280, 170, 292]},
	{"text": "[L/s]", "bbox": [277, 280, 315, 292]},
	{"text": "3.57", "bbox": [341, 280, 374, 292]},
	{"text": "0.51", "bbox": [398, 280, 429, 292]},
	{"text": "14.35", "bbox": [447, 280, 487, 292]},
	{"text": "0.51", "bbox": [512, 280, 542, 292]},
	{"text": "0.49", "bbox": [569, 280, 601, 292]},
	{"text": "0.41", "bbox": [625, 280, 658, 292]},
	{"text": "MEF 75", "bbox": [90, 293, 138, 306]},
	{"text": "[L/s]", "bbox": [277, 293, 315, 306]},
	{"text": "5.64", "bbox": [341, 293, 374, 306]},
	{"text": "1.47", "bbox": [398, 293, 429, 306]},
	{"text": "26.14", "bbox": [447, 293, 487, 306]},
	{"text": "1.47", "bbox": [512, 293, 542, 306]},
	{"text": "0.80", "bbox": [569, 293, 601, 306]},
	{"text": "1.21", "bbox": [625, 293, 658, 306]},
	{"text": "MEF 50", "bbox": [90, 306, 138, 319]},
	{"text": "[L/s]", "bbox": [277, 306, 315, 319]},
	{"text": "4.01", "bbox": [341, 306, 374, 319]},
	{"text": "0.68", "bbox": [398, 306, 429, 319]},
	{"text": "16.97", "bbox": [447, 306, 487, 319]},
	{"text": "0.68", "bbox": [512, 306, 542, 319]},
	{"text": "0.72", "bbox": [569, 306, 601, 319]},
	{"text": "0.57", "bbox": [625, 306, 658, 319]},
	{"text": "MEF 25", "bbox": [90, 319, 138, 332]},
	{"text": "[L/s]", "bbox": [277, 319, 315, 332]},
	{"text": "1.79", "bbox": [341, 319, 374, 332]},
	{"text": "0.19", "bbox": [398, 319, 429, 332]},
	{"text": "10.52", "bbox": [447, 319, 487, 332]},
	{"text": "0.19", "bbox": [512, 319, 542, 332]},
	{"text": "0.18", "bbox": [569, 319, 601, 332]},
	{"text": "0.15", "bbox": [625, 319, 658, 332]},
	{"text": "V backextrapolation ex", "bbox": [90, 333, 267, 345]},
	{"text": "[L]", "bbox": [293, 333, 315, 345]},
	{"text": "0.05", "bbox": [398, 333, 429, 345]},
	{"text": "0.05", "bbox": [512, 333, 542, 345]},
	{"text": "0.03", "bbox": [569, 333, 601, 345]},
	{"text": "0.04", "bbox": [625, 333, 658, 345]},
	{"text": "V backextrapol. % FVC", "bbox": [90, 346, 260, 359]},
	{"text": "[%]", "bbox": [293, 346, 315, 359]},
	{"text": "2.07", "bbox": [398, 346, 429, 359]},
	{"text": "2.07", "bbox": [512, 346, 542, 359]},
	{"text": "1.50", "bbox": [569, 346, 601, 359]},
	{"text": "1.81", "bbox": [625, 346, 658, 359]},
	{"text": "FET", "bbox": [90, 359, 115, 372]},
	{"text": "[s]", "bbox": [293, 359, 315, 372]},
	{"text": "7.63", "bbox": [398, 359, 429, 372]},
	{"text": "7.63", "bbox": [512, 359, 542, 372]},
	{"text": "7.35", "bbox": [569, 359, 601, 372]},
	{"text": "7.55", "bbox": [625, 359, 658, 372]},
	{"text": "FEF 200-1200", "bbox": [90, 373, 187, 385]},
	{"text": "[L/s]", "bbox": [277, 373, 315, 385]},
	{"text": "1.19", "bbox": [405, 373, 432, 385]},
	{"text": "1.19", "bbox": [512, 373, 542, 385]},
	{"text": "0.98", "bbox": [569, 373, 601, 385]},
	{"text": "1.05", "bbox": [625, 373, 658, 385]},
	{"text": "FVC IN", "bbox": [90, 386, 139, 398]},
	{"text": "[L]", "bbox": [293, 386, 315, 398]},
	{"text": "3.03", "bbox": [341, 386, 374, 398]},
	{"text": "2.26", "bbox": [398, 386, 429, 398]},
	{"text": "74.60", "bbox": [447, 386, 487, 398]},
	{"text": "2.26", "bbox": [512, 386, 542, 398]},
	{"text": "2.15", "bbox": [569, 386, 601, 398]},
	{"text": "2.13", "bbox": [625, 386, 658, 398]},
	{"text": "FIV1", "bbox": [90, 399, 121, 412]},
	{"text": "[L]", "bbox": [293, 399, 315, 412]},
	{"text": "2.21", "bbox": [398, 399, 429, 412]},
	{"text": "2.21", "bbox": [512, 399, 542, 412]},
	{"text": "2.12", "bbox": [569, 399, 601, 412]},
	{"text": "2.09", "bbox": [625, 399, 658, 412]},
	{"text": "FIV1 % FVC", "bbox": [90, 413, 170, 425]},
	{"text": "[%]", "bbox": [293, 413, 315, 425]},
	{"text": "97.79", "bbox": [391, 413, 429, 425]},
	{"text": "97.79", "bbox": [504, 413, 542, 425]},
	{"text": "98.68", "bbox": [561, 413, 601, 425]},
	{"text": "98.05", "bbox": [617, 413, 658, 425]},
	{"text": "FEF50 % FIF50", "bbox": [90, 426, 194, 438]},
	{"text": "[%]", "bbox": [293, 426, 315, 438]},
	{"text": "22.86", "bbox": [391, 426, 429, 438]},
	{"text": "22.86", "bbox": [504, 426, 542, 438]},
	{"text": "25.05", "bbox": [561, 426, 601, 438]},
	{"text": "19.46", "bbox": [617, 426, 658, 438]},
	{"text": "PIF", "bbox": [90, 439, 114, 452]},
	{"text": "[L/s]", "bbox": [277, 439, 315, 452]},
	{"text": "3.04", "bbox": [398, 439, 429, 452]},
	{"text": "3.04", "bbox": [512, 439, 542, 452]},
	{"text": "3.04", "bbox": [569, 439, 601, 452]},
	{"text": "2.99", "bbox": [625, 439, 658, 452]},
	{"text": "MVV", "bbox": [90, 453, 114, 465]},
	{"text": "[L/min]", "bbox": [261, 453, 315, 465]},
	{"text": "99.77", "bbox": [334, 453, 374, 465]},
	{"text": "46.21", "bbox": [391, 453, 429, 465]},
	{"text": "46.32", "bbox": [447, 453, 487, 465]},
	{"text": "46.21", "bbox": [504, 453, 542, 465]},
	{"text": "BF MVV", "bbox": [90, 466, 138, 478]},
	{"text": "[1/min]", "bbox": [261, 466, 315, 478]},
	{"text": "75.55", "bbox": [391, 466, 429, 478]},
	{"text": "75.55",bbox": [504, 466, 542, 478]},
	{"text": "意见：", "bbox": [82, 775, 129, 789]},
	{"text": "1. 重度混合性肺通气功能障碍。", "bbox": [82, 789, 295, 802]},
	{"text": "2. 最大分钟通气量（MVV）：显著减退。", "bbox": [82, 802, 352, 815]},
	{"text": "Date", "bbox": [802, 37, 826, 46]},
	{"text": "20/2/00", "bbox": [873, 37, 914, 46]},
	{"text": "Timo", "bbox": [802, 46, 826, 55]},
	{"text": "11:48:04上午", "bbox": [847, 46, 914, 55]},
	{"text": "Flow [L/s]", "bbox": [255, 500, 307, 511]},
	{"text": "F/V ex", "bbox": [357, 501, 391, 510]},
	{"text": "Vol [L]", "bbox": [638, 508, 673, 520]},
	{"text": "Vol%VCmax", "bbox": [589, 566, 653, 576]},
	{"text": "VCmax", "bbox": [650, 581, 688, 590]},
	{"text": "Time [s]", "bbox": [767, 610, 809, 620]},
	{"text": "Vol [L]", "bbox": [613, 646, 650, 657]},
	{"text": "Time [s]", "bbox": [755, 747, 799, 757]},
	{"text": "F/V in", "bbox": [357, 761, 389, 770]},
	{"text": "10", "bbox": [235, 497, 248, 506]},
	{"text": "8", "bbox": [240, 523, 248, 531]},
	{"text": "6", "bbox": [240, 550, 248, 558]},
	{"text": "4", "bbox": [240, 577, 248, 585]},
	{"text": "2", "bbox": [240, 604, 248, 612]},
	{"text": "0", "bbox": [240, 631, 248, 639]},
	{"text": "1", "bbox": [286, 642, 293, 650]},
	{"text": "2", "bbox": [321, 642, 328, 650]},
	{"text": "3", "bbox": [357, 642, 364, 650]},
	{"text": "4", "bbox": [393, 642, 400, 650]},
	{"text": "5", "bbox": [429, 642, 436, 650]},
	{"text": "10", "bbox": [235, 767, 248, 775]},
	{"text": "8", "bbox": [240, 740, 248, 748]},
	{"text": "6", "bbox": [240, 713, 248, 721]},
	{"text": "4", "bbox": [240, 686, 248, 694]},
	{"text": "2", "bbox": [240, 659, 248, 667]},
	{"text": "0", "bbox": [608, 620, 616, 628]},
	{"text": "2", "bbox": [673, 630, 680, 638]},
	{"text": "4", "bbox": [714, 630, 721, 638]},
	{"text": "6", "bbox": [755, 630, 762, 638]},
	{"text": "8", "bbox": [796, 630, 803, 638]},
	{"text": "10", "bbox": [836, 630, 847, 638]},
	{"text": "12", "bbox": [876, 630, 888, 638]},
	{"text": "1", "bbox": [918, 630, 925, 638]},
	{"text": "0", "bbox": [608, 767, 616, 775]},
	{"text": "2", "bbox": [653, 767, 660, 775]},
	{"text": "4", "bbox": [697, 767, 704, 775]},
	{"text": "6", "bbox": [741, 767, 748, 775]},
	{"text": "8", "bbox": [785, 767, 792, 775]},
	{"text": "10", "bbox": [830, 767, 842, 775]},
	{"text": "12", "bbox": [876, 767, 888, 775]},
	{"text": "张", "bbox": [870, 903, 909, 923]}
]
2026-08-10 12:29:29,473 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 12:29:29,475 INFO     29 [qwen-vl-text] coord API: raw_items=215, valid_items=215, elapsed=54.3s
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[225, 80, 265, 93]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[1]: text=年龄：38岁, bbox=[225, 93, 408, 107]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[225, 107, 385, 120]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[3]: text=科别：, bbox=[225, 120, 265, 133]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[4]: text=保险：, bbox=[225, 133, 265, 146]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[5]: text=预计值模式：Standard-new, bbox=[225, 146, 464, 159]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[6]: text=常规通气报告, bbox=[472, 67, 563, 80]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：2026020917, bbox=[519, 80, 738, 93]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[8]: text=身高：165 cm, bbox=[519, 93, 708, 107]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[9]: text=体重：60 kg, bbox=[660, 107, 700, 120]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[10]: text=备注：, bbox=[519, 120, 557, 133]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话：, bbox=[519, 133, 587, 146]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[12]: text=操作者：蒋细萍, bbox=[519, 146, 707, 159]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[13]: text=Pred, bbox=[341, 161, 374, 173]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[14]: text=Bst % (B/Pd, bbox=[405, 161, 487, 173]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[15]: text=A1, bbox=[527, 161, 542, 173]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[16]: text=A2, bbox=[584, 161, 601, 173]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[17]: text=A3, bbox=[642, 161, 658, 173]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[18]: text=FVC, bbox=[90, 188, 114, 200]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[19]: text=[L], bbox=[293, 188, 315, 200]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[20]: text=2.99, bbox=[341, 188, 374, 200]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[21]: text=2.21, bbox=[398, 188, 429, 200]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[22]: text=74.02, bbox=[447, 188, 487, 200]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[23]: text=2.21, bbox=[512, 188, 542, 200]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[24]: text=2.12, bbox=[569, 188, 601, 200]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[25]: text=2.09, bbox=[625, 188, 658, 200]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[26]: text=FEV 1, bbox=[90, 201, 128, 213]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[27]: text=[L], bbox=[293, 201, 315, 213]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[28]: text=2.67, bbox=[341, 201, 374, 213]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[29]: text=1.26, bbox=[398, 201, 429, 213]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[30]: text=48.56, bbox=[447, 201, 487, 213]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[31]: text=1.26, bbox=[512, 201, 542, 213]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[32]: text=1.13, bbox=[569, 201, 601, 213]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[33]: text=1.18, bbox=[625, 201, 658, 213]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[34]: text=FEV6, bbox=[90, 214, 121, 226]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[35]: text=[L], bbox=[293, 214, 315, 226]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[36]: text=2.12, bbox=[398, 214, 429, 226]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[37]: text=2.12, bbox=[512, 214, 542, 226]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[38]: text=2.05, bbox=[569, 214, 601, 226]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[39]: text=2.02, bbox=[625, 214, 658, 226]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[40]: text=FEV 1 % FVC, bbox=[90, 227, 179, 239]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[41]: text=[%], bbox=[293, 227, 315, 239]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[42]: text=84.19, bbox=[334, 227, 374, 239]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[43]: text=56.48, bbox=[391, 227, 429, 239]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[44]: text=67.09, bbox=[447, 227, 487, 239]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[45]: text=56.48, bbox=[504, 227, 542, 239]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[46]: text=53.33, bbox=[561, 227, 601, 239]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[47]: text=56.67, bbox=[617, 227, 658, 239]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[48]: text=FEV 1 % VC MAX, bbox=[90, 240, 203, 253]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[49]: text=[%], bbox=[293, 240, 315, 253]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[50]: text=81.88, bbox=[334, 240, 374, 253]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[51]: text=55.26, bbox=[391, 240, 429, 253]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[52]: text=67.48, bbox=[447, 240, 487, 253]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[53]: text=55.26, bbox=[504, 240, 542, 253]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[54]: text=50.10, bbox=[561, 240, 601, 253]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[55]: text=52.31, bbox=[617, 240, 658, 253]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[56]: text=VC MAX, bbox=[90, 254, 138, 266]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[57]: text=[L], bbox=[293, 254, 315, 266]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[58]: text=3.03, bbox=[341, 254, 374, 266]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[59]: text=2.26, bbox=[398, 254, 429, 266]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[60]: text=74.60, bbox=[447, 254, 487, 266]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[61]: text=PEF, bbox=[90, 267, 114, 279]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[62]: text=[L/s], bbox=[277, 267, 315, 279]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[63]: text=6.28, bbox=[341, 267, 374, 279]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[64]: text=2.66, bbox=[398, 267, 429, 279]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[65]: text=42.36, bbox=[447, 267, 487, 279]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[66]: text=2.66, bbox=[512, 267, 542, 279]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[67]: text=2.58, bbox=[569, 267, 601, 279]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[68]: text=2.43, bbox=[625, 267, 658, 279]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[69]: text=MMEF 75/25, bbox=[90, 280, 170, 292]
2026-08-10 12:29:29,476 INFO     29 [qwen-vl-text] coord item[70]: text=[L/s], bbox=[277, 280, 315, 292]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[71]: text=3.57, bbox=[341, 280, 374, 292]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[72]: text=0.51, bbox=[398, 280, 429, 292]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[73]: text=14.35, bbox=[447, 280, 487, 292]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[74]: text=0.51, bbox=[512, 280, 542, 292]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[75]: text=0.49, bbox=[569, 280, 601, 292]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[76]: text=0.41, bbox=[625, 280, 658, 292]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[77]: text=MEF 75, bbox=[90, 293, 138, 306]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[78]: text=[L/s], bbox=[277, 293, 315, 306]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[79]: text=5.64, bbox=[341, 293, 374, 306]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[80]: text=1.47, bbox=[398, 293, 429, 306]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[81]: text=26.14, bbox=[447, 293, 487, 306]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[82]: text=1.47, bbox=[512, 293, 542, 306]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[83]: text=0.80, bbox=[569, 293, 601, 306]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[84]: text=1.21, bbox=[625, 293, 658, 306]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[85]: text=MEF 50, bbox=[90, 306, 138, 319]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[86]: text=[L/s], bbox=[277, 306, 315, 319]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[87]: text=4.01, bbox=[341, 306, 374, 319]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[88]: text=0.68, bbox=[398, 306, 429, 319]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[89]: text=16.97, bbox=[447, 306, 487, 319]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[90]: text=0.68, bbox=[512, 306, 542, 319]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[91]: text=0.72, bbox=[569, 306, 601, 319]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[92]: text=0.57, bbox=[625, 306, 658, 319]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[93]: text=MEF 25, bbox=[90, 319, 138, 332]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[94]: text=[L/s], bbox=[277, 319, 315, 332]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[95]: text=1.79, bbox=[341, 319, 374, 332]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[96]: text=0.19, bbox=[398, 319, 429, 332]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[97]: text=10.52, bbox=[447, 319, 487, 332]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[98]: text=0.19, bbox=[512, 319, 542, 332]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[99]: text=0.18, bbox=[569, 319, 601, 332]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[100]: text=0.15, bbox=[625, 319, 658, 332]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[101]: text=V backextrapolation ex, bbox=[90, 333, 267, 345]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[102]: text=[L], bbox=[293, 333, 315, 345]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[103]: text=0.05, bbox=[398, 333, 429, 345]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[104]: text=0.05, bbox=[512, 333, 542, 345]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[105]: text=0.03, bbox=[569, 333, 601, 345]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[106]: text=0.04, bbox=[625, 333, 658, 345]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[107]: text=V backextrapol. % FVC, bbox=[90, 346, 260, 359]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[108]: text=[%], bbox=[293, 346, 315, 359]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[109]: text=2.07, bbox=[398, 346, 429, 359]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[110]: text=2.07, bbox=[512, 346, 542, 359]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[111]: text=1.50, bbox=[569, 346, 601, 359]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[112]: text=1.81, bbox=[625, 346, 658, 359]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[113]: text=FET, bbox=[90, 359, 115, 372]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[114]: text=[s], bbox=[293, 359, 315, 372]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[115]: text=7.63, bbox=[398, 359, 429, 372]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[116]: text=7.63, bbox=[512, 359, 542, 372]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[117]: text=7.35, bbox=[569, 359, 601, 372]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[118]: text=7.55, bbox=[625, 359, 658, 372]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[119]: text=FEF 200-1200, bbox=[90, 373, 187, 385]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[120]: text=[L/s], bbox=[277, 373, 315, 385]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[121]: text=1.19, bbox=[405, 373, 432, 385]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[122]: text=1.19, bbox=[512, 373, 542, 385]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[123]: text=0.98, bbox=[569, 373, 601, 385]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[124]: text=1.05, bbox=[625, 373, 658, 385]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[125]: text=FVC IN, bbox=[90, 386, 139, 398]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[126]: text=[L], bbox=[293, 386, 315, 398]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[127]: text=3.03, bbox=[341, 386, 374, 398]
2026-08-10 12:29:29,477 INFO     29 [qwen-vl-text] coord item[128]: text=2.26, bbox=[398, 386, 429, 398]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[129]: text=74.60, bbox=[447, 386, 487, 398]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[130]: text=2.26, bbox=[512, 386, 542, 398]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[131]: text=2.15, bbox=[569, 386, 601, 398]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[132]: text=2.13, bbox=[625, 386, 658, 398]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[133]: text=FIV1, bbox=[90, 399, 121, 412]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[134]: text=[L], bbox=[293, 399, 315, 412]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[135]: text=2.21, bbox=[398, 399, 429, 412]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[136]: text=2.21, bbox=[512, 399, 542, 412]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[137]: text=2.12, bbox=[569, 399, 601, 412]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[138]: text=2.09, bbox=[625, 399, 658, 412]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[139]: text=FIV1 % FVC, bbox=[90, 413, 170, 425]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[140]: text=[%], bbox=[293, 413, 315, 425]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[141]: text=97.79, bbox=[391, 413, 429, 425]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[142]: text=97.79, bbox=[504, 413, 542, 425]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[143]: text=98.68, bbox=[561, 413, 601, 425]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[144]: text=98.05, bbox=[617, 413, 658, 425]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[145]: text=FEF50 % FIF50, bbox=[90, 426, 194, 438]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[146]: text=[%], bbox=[293, 426, 315, 438]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[147]: text=22.86, bbox=[391, 426, 429, 438]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[148]: text=22.86, bbox=[504, 426, 542, 438]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[149]: text=25.05, bbox=[561, 426, 601, 438]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[150]: text=19.46, bbox=[617, 426, 658, 438]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[151]: text=PIF, bbox=[90, 439, 114, 452]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[152]: text=[L/s], bbox=[277, 439, 315, 452]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[153]: text=3.04, bbox=[398, 439, 429, 452]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[154]: text=3.04, bbox=[512, 439, 542, 452]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[155]: text=3.04, bbox=[569, 439, 601, 452]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[156]: text=2.99, bbox=[625, 439, 658, 452]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[157]: text=MVV, bbox=[90, 453, 114, 465]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[158]: text=[L/min], bbox=[261, 453, 315, 465]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[159]: text=99.77, bbox=[334, 453, 374, 465]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[160]: text=46.21, bbox=[391, 453, 429, 465]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[161]: text=46.32, bbox=[447, 453, 487, 465]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[162]: text=46.21, bbox=[504, 453, 542, 465]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[163]: text=BF MVV, bbox=[90, 466, 138, 478]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[164]: text=[1/min], bbox=[261, 466, 315, 478]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[165]: text=75.55, bbox=[391, 466, 429, 478]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[166]: text=75.55, bbox=[504, 466, 542, 478]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[167]: text=意见：, bbox=[82, 775, 129, 789]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[168]: text=1. 重度混合性肺通气功能障碍。, bbox=[82, 789, 295, 802]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[169]: text=2. 最大分钟通气量（MVV）：显著减退。, bbox=[82, 802, 352, 815]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[170]: text=Date, bbox=[802, 37, 826, 46]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[171]: text=20/2/00, bbox=[873, 37, 914, 46]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[172]: text=Timo, bbox=[802, 46, 826, 55]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[173]: text=11:48:04上午, bbox=[847, 46, 914, 55]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[174]: text=Flow [L/s], bbox=[255, 500, 307, 511]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[175]: text=F/V ex, bbox=[357, 501, 391, 510]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[176]: text=Vol [L], bbox=[638, 508, 673, 520]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[177]: text=Vol%VCmax, bbox=[589, 566, 653, 576]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[178]: text=VCmax, bbox=[650, 581, 688, 590]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[179]: text=Time [s], bbox=[767, 610, 809, 620]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[180]: text=Vol [L], bbox=[613, 646, 650, 657]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[181]: text=Time [s], bbox=[755, 747, 799, 757]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[182]: text=F/V in, bbox=[357, 761, 389, 770]
2026-08-10 12:29:29,478 INFO     29 [qwen-vl-text] coord item[183]: text=10, bbox=[235, 497, 248, 506]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[184]: text=8, bbox=[240, 523, 248, 531]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[185]: text=6, bbox=[240, 550, 248, 558]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[186]: text=4, bbox=[240, 577, 248, 585]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[187]: text=2, bbox=[240, 604, 248, 612]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[188]: text=0, bbox=[240, 631, 248, 639]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[189]: text=1, bbox=[286, 642, 293, 650]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[190]: text=2, bbox=[321, 642, 328, 650]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[191]: text=3, bbox=[357, 642, 364, 650]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[192]: text=4, bbox=[393, 642, 400, 650]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[193]: text=5, bbox=[429, 642, 436, 650]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[194]: text=10, bbox=[235, 767, 248, 775]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[195]: text=8, bbox=[240, 740, 248, 748]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[196]: text=6, bbox=[240, 713, 248, 721]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[197]: text=4, bbox=[240, 686, 248, 694]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[198]: text=2, bbox=[240, 659, 248, 667]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[199]: text=0, bbox=[608, 620, 616, 628]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[200]: text=2, bbox=[673, 630, 680, 638]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[201]: text=4, bbox=[714, 630, 721, 638]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[202]: text=6, bbox=[755, 630, 762, 638]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[203]: text=8, bbox=[796, 630, 803, 638]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[204]: text=10, bbox=[836, 630, 847, 638]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[205]: text=12, bbox=[876, 630, 888, 638]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[206]: text=1, bbox=[918, 630, 925, 638]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[207]: text=0, bbox=[608, 767, 616, 775]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[208]: text=2, bbox=[653, 767, 660, 775]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[209]: text=4, bbox=[697, 767, 704, 775]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[210]: text=6, bbox=[741, 767, 748, 775]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[211]: text=8, bbox=[785, 767, 792, 775]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[212]: text=10, bbox=[830, 767, 842, 775]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[213]: text=12, bbox=[876, 767, 888, 775]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] coord item[214]: text=张, bbox=[870, 903, 909, 923]
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] page=14 — 230/230 coords, api_time=54.3s
2026-08-10 12:29:29,479 INFO     29 [qwen-vl-text] new_positions (230):
[[14, 133.875, 157.67499999999998, 67.36, 78.306], [14, 133.875, 242.76, 78.306, 90.094], [14, 133.875, 229.075, 90.094, 101.03999999999999], [14, 133.875, 157.67499999999998, 101.03999999999999, 111.98599999999999], [14, 133.875, 157.67499999999998, 111.98599999999999, 122.932], [14, 133.875, 276.08, 122.932, 133.878], [14, 280.84, 334.98499999999996, 56.414, 67.36], [14, 308.805, 439.10999999999996, 67.36, 78.306], [14, 308.805, 421.26, 78.306, 90.094], [14, 392.7, 416.5, 90.094, 101.03999999999999], [14, 308.805, 331.41499999999996, 101.03999999999999, 111.98599999999999], [14, 308.805, 349.265, 111.98599999999999, 122.932], [14, 308.805, 420.66499999999996, 122.932, 133.878], [14, 202.89499999999998, 222.53, 135.56199999999998, 145.666], [14, 240.975, 289.765, 135.56199999999998, 145.666], [14, 313.565, 322.49, 135.56199999999998, 145.666], [14, 347.47999999999996, 357.59499999999997, 135.56199999999998, 145.666], [14, 381.99, 391.51, 135.56199999999998, 145.666], [14, 53.55, 67.83, 158.296, 168.4], [14, 174.33499999999998, 187.42499999999998, 158.296, 168.4], [14, 202.89499999999998, 222.53, 158.296, 168.4], [14, 236.81, 255.255, 158.296, 168.4], [14, 265.965, 289.765, 158.296, 168.4], [14, 304.64, 322.49, 158.296, 168.4], [14, 338.555, 357.59499999999997, 158.296, 168.4], [14, 371.875, 391.51, 158.296, 168.4], [14, 53.55, 76.16, 169.242, 179.346], [14, 174.33499999999998, 187.42499999999998, 169.242, 179.346], [14, 202.89499999999998, 222.53, 169.242, 179.346], [14, 236.81, 255.255, 169.242, 179.346], [14, 265.965, 289.765, 169.242, 179.346], [14, 304.64, 322.49, 169.242, 179.346], [14, 338.555, 357.59499999999997, 169.242, 179.346], [14, 371.875, 391.51, 169.242, 179.346], [14, 53.55, 71.99499999999999, 180.188, 190.292], [14, 174.33499999999998, 187.42499999999998, 180.188, 190.292], [14, 236.81, 255.255, 180.188, 190.292], [14, 304.64, 322.49, 180.188, 190.292], [14, 338.555, 357.59499999999997, 180.188, 190.292], [14, 371.875, 391.51, 180.188, 190.292], [14, 53.55, 106.505, 191.134, 201.238], [14, 174.33499999999998, 187.42499999999998, 191.134, 201.238], [14, 198.73, 222.53, 191.134, 201.238], [14, 232.64499999999998, 255.255, 191.134, 201.238], [14, 265.965, 289.765, 191.134, 201.238], [14, 299.88, 322.49, 191.134, 201.238], [14, 333.79499999999996, 357.59499999999997, 191.134, 201.238], [14, 367.115, 391.51, 191.134, 201.238], [14, 53.55, 120.785, 202.07999999999998, 213.02599999999998], [14, 174.33499999999998, 187.42499999999998, 202.07999999999998, 213.02599999999998], [14, 198.73, 222.53, 202.07999999999998, 213.02599999999998], [14, 232.64499999999998, 255.255, 202.07999999999998, 213.02599999999998], [14, 265.965, 289.765, 202.07999999999998, 213.02599999999998], [14, 299.88, 322.49, 202.07999999999998, 213.02599999999998], [14, 333.79499999999996, 357.59499999999997, 202.07999999999998, 213.02599999999998], [14, 367.115, 391.51, 202.07999999999998, 213.02599999999998], [14, 53.55, 82.11, 213.868, 223.97199999999998], [14, 174.33499999999998, 187.42499999999998, 213.868, 223.97199999999998], [14, 202.89499999999998, 222.53, 213.868, 223.97199999999998], [14, 236.81, 255.255, 213.868, 223.97199999999998], [14, 265.965, 289.765, 213.868, 223.97199999999998], [14, 53.55, 67.83, 224.814, 234.91799999999998], [14, 164.815, 187.42499999999998, 224.814, 234.91799999999998], [14, 202.89499999999998, 222.53, 224.814, 234.91799999999998], [14, 236.81, 255.255, 224.814, 234.91799999999998], [14, 265.965, 289.765, 224.814, 234.91799999999998], [14, 304.64, 322.49, 224.814, 234.91799999999998], [14, 338.555, 357.59499999999997, 224.814, 234.91799999999998], [14, 371.875, 391.51, 224.814, 234.91799999999998], [14, 53.55, 101.14999999999999, 235.76, 245.864], [14, 164.815, 187.42499999999998, 235.76, 245.864], [14, 202.89499999999998, 222.53, 235.76, 245.864], [14, 236.81, 255.255, 235.76, 245.864], [14, 265.965, 289.765, 235.76, 245.864], [14, 304.64, 322.49, 235.76, 245.864], [14, 338.555, 357.59499999999997, 235.76, 245.864], [14, 371.875, 391.51, 235.76, 245.864], [14, 53.55, 82.11, 246.706, 257.652], [14, 164.815, 187.42499999999998, 246.706, 257.652], [14, 202.89499999999998, 222.53, 246.706, 257.652], [14, 236.81, 255.255, 246.706, 257.652], [14, 265.965, 289.765, 246.706, 257.652], [14, 304.64, 322.49, 246.706, 257.652], [14, 338.555, 357.59499999999997, 246.706, 257.652], [14, 371.875, 391.51, 246.706, 257.652], [14, 53.55, 82.11, 257.652, 268.598], [14, 164.815, 187.42499999999998, 257.652, 268.598], [14, 202.89499999999998, 222.53, 257.652, 268.598], [14, 236.81, 255.255, 257.652, 268.598], [14, 265.965, 289.765, 257.652, 268.598], [14, 304.64, 322.49, 257.652, 268.598], [14, 338.555, 357.59499999999997, 257.652, 268.598], [14, 371.875, 391.51, 257.652, 268.598], [14, 53.55, 82.11, 268.598, 279.544], [14, 164.815, 187.42499999999998, 268.598, 279.544], [14, 202.89499999999998, 222.53, 268.598, 279.544], [14, 236.81, 255.255, 268.598, 279.544], [14, 265.965, 289.765, 268.598, 279.544], [14, 304.64, 322.49, 268.598, 279.544], [14, 338.555, 357.59499999999997, 268.598, 279.544], [14, 371.875, 391.51, 268.598, 279.544], [14, 53.55, 158.86499999999998, 280.38599999999997, 290.49], [14, 174.33499999999998, 187.42499999999998, 280.38599999999997, 290.49], [14, 236.81, 255.255, 280.38599999999997, 290.49], [14, 304.64, 322.49, 280.38599999999997, 290.49], [14, 338.555, 357.59499999999997, 280.38599999999997, 290.49], [14, 371.875, 391.51, 280.38599999999997, 290.49], [14, 53.55, 154.7, 291.332, 302.27799999999996], [14, 174.33499999999998, 187.42499999999998, 291.332, 302.27799999999996], [14, 236.81, 255.255, 291.332, 302.27799999999996], [14, 304.64, 322.49, 291.332, 302.27799999999996], [14, 338.555, 357.59499999999997, 291.332, 302.27799999999996], [14, 371.875, 391.51, 291.332, 302.27799999999996], [14, 53.55, 68.425, 302.27799999999996, 313.224], [14, 174.33499999999998, 187.42499999999998, 302.27799999999996, 313.224], [14, 236.81, 255.255, 302.27799999999996, 313.224], [14, 304.64, 322.49, 302.27799999999996, 313.224], [14, 338.555, 357.59499999999997, 302.27799999999996, 313.224], [14, 371.875, 391.51, 302.27799999999996, 313.224], [14, 53.55, 111.265, 314.066, 324.17], [14, 164.815, 187.42499999999998, 314.066, 324.17], [14, 240.975, 257.03999999999996, 314.066, 324.17], [14, 304.64, 322.49, 314.066, 324.17], [14, 338.555, 357.59499999999997, 314.066, 324.17], [14, 371.875, 391.51, 314.066, 324.17], [14, 53.55, 82.705, 325.012, 335.116], [14, 174.33499999999998, 187.42499999999998, 325.012, 335.116], [14, 202.89499999999998, 222.53, 325.012, 335.116], [14, 236.81, 255.255, 325.012, 335.116], [14, 265.965, 289.765, 325.012, 335.116], [14, 304.64, 322.49, 325.012, 335.116], [14, 338.555, 357.59499999999997, 325.012, 335.116], [14, 371.875, 391.51, 325.012, 335.116], [14, 53.55, 71.99499999999999, 335.95799999999997, 346.904], [14, 174.33499999999998, 187.42499999999998, 335.95799999999997, 346.904], [14, 236.81, 255.255, 335.95799999999997, 346.904], [14, 304.64, 322.49, 335.95799999999997, 346.904], [14, 338.555, 357.59499999999997, 335.95799999999997, 346.904], [14, 371.875, 391.51, 335.95799999999997, 346.904], [14, 53.55, 101.14999999999999, 347.746, 357.84999999999997], [14, 174.33499999999998, 187.42499999999998, 347.746, 357.84999999999997], [14, 232.64499999999998, 255.255, 347.746, 357.84999999999997], [14, 299.88, 322.49, 347.746, 357.84999999999997], [14, 333.79499999999996, 357.59499999999997, 347.746, 357.84999999999997], [14, 367.115, 391.51, 347.746, 357.84999999999997], [14, 53.55, 115.42999999999999, 358.692, 368.796], [14, 174.33499999999998, 187.42499999999998, 358.692, 368.796], [14, 232.64499999999998, 255.255, 358.692, 368.796], [14, 299.88, 322.49, 358.692, 368.796], [14, 333.79499999999996, 357.59499999999997, 358.692, 368.796], [14, 367.115, 391.51, 358.692, 368.796], [14, 53.55, 67.83, 369.638, 380.584], [14, 164.815, 187.42499999999998, 369.638, 380.584], [14, 236.81, 255.255, 369.638, 380.584], [14, 304.64, 322.49, 369.638, 380.584], [14, 338.555, 357.59499999999997, 369.638, 380.584], [14, 371.875, 391.51, 369.638, 380.584], [14, 53.55, 67.83, 381.426, 391.53], [14, 155.295, 187.42499999999998, 381.426, 391.53], [14, 198.73, 222.53, 381.426, 391.53], [14, 232.64499999999998, 255.255, 381.426, 391.53], [14, 265.965, 289.765, 381.426, 391.53], [14, 299.88, 322.49, 381.426, 391.53], [14, 53.55, 82.11, 392.372, 402.476], [14, 155.295, 187.42499999999998, 392.372, 402.476], [14, 232.64499999999998, 255.255, 392.372, 402.476], [14, 299.88, 322.49, 392.372, 402.476], [14, 48.79, 76.755, 652.55, 664.338], [14, 48.79, 175.525, 664.338, 675.284], [14, 48.79, 209.44, 675.284, 686.23], [14, 477.19, 491.46999999999997, 31.154, 38.732], [14, 519.435, 543.8299999999999, 31.154, 38.732], [14, 477.19, 491.46999999999997, 38.732, 46.309999999999995], [14, 503.965, 543.8299999999999, 38.732, 46.309999999999995], [14, 151.725, 182.665, 421.0, 430.262], [14, 212.415, 232.64499999999998, 421.842, 429.41999999999996], [14, 379.60999999999996, 400.435, 427.736, 437.84], [14, 350.455, 388.53499999999997, 476.572, 484.99199999999996], [14, 386.75, 409.35999999999996, 489.202, 496.78], [14, 456.36499999999995, 481.35499999999996, 513.62, 522.04], [14, 364.73499999999996, 386.75, 543.932, 553.194], [14, 449.22499999999997, 475.405, 628.9739999999999, 637.394], [14, 212.415, 231.45499999999998, 640.762, 648.34], [14, 139.825, 147.56, 418.474, 426.05199999999996], [14, 142.79999999999998, 147.56, 440.366, 447.102], [14, 142.79999999999998, 147.56, 463.09999999999997, 469.83599999999996], [14, 142.79999999999998, 147.56, 485.834, 492.57], [14, 142.79999999999998, 147.56, 508.568, 515.304], [14, 142.79999999999998, 147.56, 531.302, 538.038], [14, 170.17, 174.33499999999998, 540.564, 547.3], [14, 190.995, 195.16, 540.564, 547.3], [14, 212.415, 216.57999999999998, 540.564, 547.3], [14, 233.83499999999998, 238.0, 540.564, 547.3], [14, 255.255, 259.42, 540.564, 547.3], [14, 139.825, 147.56, 645.814, 652.55], [14, 142.79999999999998, 147.56, 623.0799999999999, 629.816], [14, 142.79999999999998, 147.56, 600.346, 607.082], [14, 142.79999999999998, 147.56, 577.612, 584.348], [14, 142.79999999999998, 147.56, 554.8779999999999, 561.614], [14, 361.76, 366.52, 522.04, 528.776], [14, 400.435, 404.59999999999997, 530.46, 537.196], [14, 424.83, 428.995, 530.46, 537.196], [14, 449.22499999999997, 453.39, 530.46, 537.196], [14, 473.62, 477.78499999999997, 530.46, 537.196], [14, 497.41999999999996, 503.965, 530.46, 537.196], [14, 521.22, 528.36, 530.46, 537.196], [14, 546.2099999999999, 550.375, 530.46, 537.196], [14, 361.76, 366.52, 645.814, 652.55], [14, 388.53499999999997, 392.7, 645.814, 652.55], [14, 414.715, 418.88, 645.814, 652.55], [14, 440.895, 445.06, 645.814, 652.55], [14, 467.075, 471.23999999999995, 645.814, 652.55], [14, 493.84999999999997, 500.98999999999995, 645.814, 652.55], [14, 521.22, 528.36, 645.814, 652.55], [14, 517.65, 540.855, 760.326, 777.1659999999999], [14, 414.715, 418.88, 645.814, 652.55], [14, 440.895, 445.06, 645.814, 652.55], [14, 467.075, 471.23999999999995, 645.814, 652.55], [14, 493.84999999999997, 500.98999999999995, 645.814, 652.55], [14, 521.22, 528.36, 645.814, 652.55], [14, 546.2099999999999, 550.375, 530.46, 537.196], [14, 361.76, 366.52, 645.814, 652.55], [14, 388.53499999999997, 392.7, 645.814, 652.55], [14, 414.715, 418.88, 645.814, 652.55], [14, 440.895, 445.06, 645.814, 652.55], [14, 467.075, 471.23999999999995, 645.814, 652.55], [14, 493.84999999999997, 500.98999999999995, 645.814, 652.55], [14, 521.22, 528.36, 645.814, 652.55], [14, 546.2099999999999, 550.375, 530.46, 537.196], [14, 517.65, 540.855, 760.326, 777.1659999999999]]
2026-08-10 12:29:29,480 INFO     29 [qwen-vl-text] ═══ DONE ═══ 230 positions, pages=1, time=65.8s
2026-08-10 12:29:29,480 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:29:29,487 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:29:29,487 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:29:29,487 INFO     29 [qwen-vl-text] positions(48): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:29:29,487 INFO     29 [qwen-vl-text] page grouping: [14, 15], lines per page: [2, 46]
2026-08-10 12:29:29,664 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:29:29,859 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:29:29,861 INFO     29 [qwen-vl-text] LLM extraction start, text_len=996
2026-08-10 12:29:29,861 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:29:29,861 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 563, \"bbox_end\": 610, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"呼吸科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CS 扫描全能王\n3亿人都在用的扫描App\n呼出气一氧化氮检测报告单\n姓名：杨\n性别：女\n出生日期：1987-12-01\n年龄：38岁2个月\nID号：\n测试日期：2026-02-09\n科室：呼吸科门诊\n医生：张\n问卷调查：\n激素：正在使用口 三天内未使用口 从未使用口\n抗生素：正在使用口 三天内未使用口 从未使用口\n吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口\n症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：\n病史：过敏史口 其他：\n注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。\n检测信息：\n项目：在线\n呼气压力：8.8cmH2O 呼气流速：45ml/s\n呼气时间：5s 温度：21.8℃ 湿度：38.9%\n呼气浓度：10、11、12、11、11、11、10、10、10、\n10、10、10、11、10、11、11、11、11ppb\n项目：小气道\n呼气压力：11.3cmH2O 呼气流速：202ml/s\n呼气时间：3s 温度：22.0℃ 湿度：39.0%\n呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0\n0.0、0.0、0.0、0.0、1.0、1.0、1.0、\n1.0、1.0、0.0、0.0、0.0ppb\n参考意义：\n(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)\n测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型\nFeNO < 25ppb < 20ppb* 非嗜酸性气道炎症\n25 - 50ppb 20 - 35ppb* 混合型气道炎症\n> 50ppb > 35ppb* 嗜酸性气道炎症\nCaNO ≤ 5ppb ≤ 3ppb 小气道正常\n> 5ppb > 3ppb 小气道炎症\nFaNO < 125ppb 考虑Kartagener综合征、PCD、CF或\n重度的鼻窦炎或鼻息肉\n125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉\n250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断\n> 500ppb 考虑过敏性鼻炎\n(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n此结果仅对本次呼气检测负责\n测定结果：FeNO 60:11ppb CaNO :1.0ppb\n操作员：蒋细萍\n张日石",
    "role": "user"
  }
]
2026-08-10 12:29:29,863 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:29:29.862+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:29:34,142 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:29:34,142 INFO     29 [qwen-vl-text] LLM output (len=617):
{
  "exam_date": "2026-02-09",
  "report_date": null,
  "exam_name": "呼出气一氧化氮检测",
  "exam_category": "other",
  "body_part": "呼出气",
  "patient_name": "杨",
  "patient_gender": "女",
  "department": "呼吸科门诊",
  "bed_number": null,
  "findings": "检测信息：\n项目：在线\n呼气压力：8.8cmH2O 呼气流速：45ml/s\n呼气时间：5s 温度：21.8℃ 湿度：38.9%\n呼气浓度：10、11、12、11、11、11、10、10、10、\n10、10、10、11、10、11、11、11、11ppb\n项目：小气道\n呼气压力：11.3cmH2O 呼气流速：202ml/s\n呼气时间：3s 温度：22.0℃ 湿度：39.0%\n呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0\n0.0、0.0、0.0、0.0、1.0、1.0、1.0、\n1.0、1.0、0.0、0.0、0.0ppb",
  "conclusion": "测定结果：FeNO 60:11ppb CaNO :1.0ppb",
  "physician": "蒋细萍",
  "reviewer": null
}
2026-08-10 12:29:34,144 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=819324, prompt_len=639
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 12:29:35,129 INFO     29 [qwen-vl-text] coord API raw response (len=124):
```json
[
	{"text": "CS 扫描全能王", "bbox": [862, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [862, 977, 977, 987]}
]
```
2026-08-10 12:29:35,130 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=1.0s
2026-08-10 12:29:35,130 INFO     29 [qwen-vl-text] coord item[0]: text=CS 扫描全能王, bbox=[862, 958, 977, 974]
2026-08-10 12:29:35,130 INFO     29 [qwen-vl-text] coord item[1]: text=3亿人都在用的扫描App, bbox=[862, 977, 977, 987]
2026-08-10 12:29:35,130 INFO     29 [qwen-vl-text] page=14 — 2/2 coords, api_time=1.0s
2026-08-10 12:29:35,132 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1026194, prompt_len=1725
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共46行）
["呼出气一氧化氮检测报告单", "姓名：杨", "性别：女", "出生日期：1987-12-01", "年龄：38岁2个月", "ID号：", "测试日期：2026-02-09", "科室：呼吸科门诊", "医生：张", "问卷调查：", "激素：正在使用口 三天内未使用口 从未使用口", "抗生素：正在使用口 三天内未使用口 从未使用口", "吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口", "症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：", "病史：过敏史口 其他：", "注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。", "检测信息：", "项目：在线", "呼气压力：8.8cmH2O 呼气流速：45ml/s", "呼气时间：5s 温度：21.8℃ 湿度：38.9%", "呼气浓度：10、11、12、11、11、11、10、10、10、", "10、10、10、11、10、11、11、11、11ppb", "项目：小气道", "呼气压力：11.3cmH2O 呼气流速：202ml/s", "呼气时间：3s 温度：22.0℃ 湿度：39.0%", "呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0", "0.0、0.0、0.0、0.0、1.0、1.0、1.0、", "1.0、1.0、0.0、0.0、0.0ppb", "参考意义：", "(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)", "测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型", "FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症", "25 - 50ppb 20 - 35ppb* 混合型气道炎症", "> 50ppb > 35ppb* 嗜酸性气道炎症", "CaNO ≤ 5ppb ≤ 3ppb 小气道正常", "> 5ppb > 3ppb 小气道炎症", "FaNO < 125ppb 考虑Kartagener综合征、PCD、CF或", "重度的鼻窦炎或鼻息肉", "125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉", "250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断", "> 500ppb 考虑过敏性鼻炎", "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "此结果仅对本次呼气检测负责", "测定结果：FeNO 60:11ppb CaNO :1.0ppb", "操作员：蒋细萍", "张日石"]

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
2026-08-10 12:29:51,942 INFO     29 [qwen-vl-text] coord API raw response (len=2994):
[
	{"text": "呼出气一氧化氮检测报告单", "bbox": [386, 70, 603, 85]},
	{"text": "姓名：杨", "bbox": [168, 100, 270, 114]},
	{"text": "性别：女", "bbox": [413, 100, 498, 114]},
	{"text": "出生日期：1987-12-01", "bbox": [637, 100, 804, 114]},
	{"text": "年龄：38岁2个月", "bbox": [168, 116, 294, 130]},
	{"text": "ID号：", "bbox": [413, 116, 472, 130]},
	{"text": "测试日期：2026-02-09", "bbox": [637, 116, 804, 130]},
	{"text": "科室：呼吸科门诊", "bbox": [168, 133, 303, 147]},
	{"text": "医生：张", "bbox": [413, 133, 555, 147]},
	{"text": "问卷调查：", "bbox": [157, 149, 237, 163]},
	{"text": "激素：正在使用口 三天内未使用口 从未使用口", "bbox": [168, 171, 742, 188]},
	{"text": "抗生素：正在使用口 三天内未使用口 从未使用口", "bbox": [168, 191, 742, 208]},
	{"text": "吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口", "bbox": [168, 212, 742, 229]},
	{"text": "症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：", "bbox": [168, 232, 742, 249]},
	{"text": "病史：过敏史口 其他：", "bbox": [168, 253, 422, 269]},
	{"text": "注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。", "bbox": [175, 272, 768, 285]},
	{"text": "检测信息：", "bbox": [157, 288, 237, 302]},
	{"text": "项目：在线", "bbox": [172, 310, 236, 323]},
	{"text": "呼气压力：8.8cmH2O 呼气流速：45ml/s", "bbox": [172, 327, 445, 340]},
	{"text": "呼气时间：5s 温度：21.8℃ 湿度：38.9%", "bbox": [172, 344, 474, 357]},
	{"text": "呼气浓度：10、11、12、11、11、11、10、10、10、", "bbox": [172, 360, 487, 373]},
	{"text": "10、10、10、11、10、11、11、11、11ppb", "bbox": [178, 377, 445, 389]},
	{"text": "项目：小气道", "bbox": [522, 310, 600, 323]},
	{"text": "呼气压力：11.3cmH2O 呼气流速：202ml/s", "bbox": [522, 327, 802, 340]},
	{"text": "呼气时间：3s 温度：22.0℃ 湿度：39.0%", "bbox": [522, 344, 825, 357]},
	{"text": "呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0", "bbox": [522, 360, 790, 373]},
	{"text": "0.0、0.0、0.0、0.0、1.0、1.0、1.0、", "bbox": [527, 377, 774, 389]},
	{"text": "1.0、1.0、0.0、0.0、0.0ppb", "bbox": [527, 393, 718, 405]},
	{"text": "参考意义：", "bbox": [157, 540, 235, 554]},
	{"text": "(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)", "bbox": [184, 559, 655, 571]},
	{"text": "测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型", "bbox": [168, 577, 848, 594]},
	{"text": "FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症", "bbox": [168, 597, 848, 614]},
	{"text": "25 - 50ppb 20 - 35ppb* 混合型气道炎症", "bbox": [168, 617, 848, 634]},
	{"text": "> 50ppb > 35ppb* 嗜酸性气道炎症", "bbox": [168, 637, 848, 654]},
	{"text": "CaNO ≤ 5ppb ≤ 3ppb 小气道正常", "bbox": [168, 658, 848, 675]},
	{"text": "> 5ppb > 3ppb 小气道炎症", "bbox": [168, 678, 848, 695]},
	{"text": "< 125ppb 考虑Kartagener综合征、PCD、CF或", "bbox": [168, 700, 848, 717]},
	{"text": "重度的鼻窦炎或鼻息肉", "bbox": [617, 719, 745, 731]},
	{"text": "125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉", "bbox": [168, 739, 848, 756]},
	{"text": "250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断", "bbox": [168, 759, 848, 776]},
	{"text": "> 500ppb 考虑过敏性鼻炎", "bbox": [168, 779, 848, 796]},
	{"text": "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "bbox": [178, 797, 603, 809]},
	{"text": "此结果仅对本次呼气检测负责", "bbox": [178, 810, 343, 822]},
	{"text": "测定结果：FeNO 60:11ppb CaNO :1.0ppb", "bbox": [178, 833, 543, 847]},
	{"text": "操作员：蒋细萍", "bbox": [178, 852, 297, 866]},
	{"text": "张日石", "bbox": [718, 870, 786, 897]}
]
2026-08-10 12:29:51,942 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=16.8s
2026-08-10 12:29:51,942 INFO     29 [qwen-vl-text] coord item[0]: text=呼出气一氧化氮检测报告单, bbox=[386, 70, 603, 85]
2026-08-10 12:29:51,942 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：杨, bbox=[168, 100, 270, 114]
2026-08-10 12:29:51,942 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[413, 100, 498, 114]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[3]: text=出生日期：1987-12-01, bbox=[637, 100, 804, 114]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：38岁2个月, bbox=[168, 116, 294, 130]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[5]: text=ID号：, bbox=[413, 116, 472, 130]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[6]: text=测试日期：2026-02-09, bbox=[637, 116, 804, 130]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[7]: text=科室：呼吸科门诊, bbox=[168, 133, 303, 147]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[8]: text=医生：张, bbox=[413, 133, 555, 147]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[9]: text=问卷调查：, bbox=[157, 149, 237, 163]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[10]: text=激素：正在使用口 三天内未使用口 从未使用口, bbox=[168, 171, 742, 188]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[11]: text=抗生素：正在使用口 三天内未使用口 从未使用口, bbox=[168, 191, 742, 208]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[12]: text=吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口, bbox=[168, 212, 742, 229]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[13]: text=症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：, bbox=[168, 232, 742, 249]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[14]: text=病史：过敏史口 其他：, bbox=[168, 253, 422, 269]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[15]: text=注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。, bbox=[175, 272, 768, 285]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[16]: text=检测信息：, bbox=[157, 288, 237, 302]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[17]: text=项目：在线, bbox=[172, 310, 236, 323]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[18]: text=呼气压力：8.8cmH2O 呼气流速：45ml/s, bbox=[172, 327, 445, 340]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[19]: text=呼气时间：5s 温度：21.8℃ 湿度：38.9%, bbox=[172, 344, 474, 357]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[20]: text=呼气浓度：10、11、12、11、11、11、10、10、10、, bbox=[172, 360, 487, 373]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[21]: text=10、10、10、11、10、11、11、11、11ppb, bbox=[178, 377, 445, 389]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[22]: text=项目：小气道, bbox=[522, 310, 600, 323]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[23]: text=呼气压力：11.3cmH2O 呼气流速：202ml/s, bbox=[522, 327, 802, 340]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[24]: text=呼气时间：3s 温度：22.0℃ 湿度：39.0%, bbox=[522, 344, 825, 357]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[25]: text=呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0, bbox=[522, 360, 790, 373]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[26]: text=0.0、0.0、0.0、0.0、1.0、1.0、1.0、, bbox=[527, 377, 774, 389]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[27]: text=1.0、1.0、0.0、0.0、0.0ppb, bbox=[527, 393, 718, 405]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[28]: text=参考意义：, bbox=[157, 540, 235, 554]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[29]: text=(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断), bbox=[184, 559, 655, 571]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[30]: text=测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型, bbox=[168, 577, 848, 594]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[31]: text=FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症, bbox=[168, 597, 848, 614]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[32]: text=25 - 50ppb 20 - 35ppb* 混合型气道炎症, bbox=[168, 617, 848, 634]
2026-08-10 12:29:51,943 INFO     29 [qwen-vl-text] coord item[33]: text=> 50ppb > 35ppb* 嗜酸性气道炎症, bbox=[168, 637, 848, 654]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[34]: text=CaNO ≤ 5ppb ≤ 3ppb 小气道正常, bbox=[168, 658, 848, 675]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[35]: text=> 5ppb > 3ppb 小气道炎症, bbox=[168, 678, 848, 695]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[36]: text=< 125ppb 考虑Kartagener综合征、PCD、CF或, bbox=[168, 700, 848, 717]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[37]: text=重度的鼻窦炎或鼻息肉, bbox=[617, 719, 745, 731]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[38]: text=125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉, bbox=[168, 739, 848, 756]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[39]: text=250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断, bbox=[168, 759, 848, 776]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[40]: text=> 500ppb 考虑过敏性鼻炎, bbox=[168, 779, 848, 796]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[41]: text=(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb), bbox=[178, 797, 603, 809]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[42]: text=此结果仅对本次呼气检测负责, bbox=[178, 810, 343, 822]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[43]: text=测定结果：FeNO 60:11ppb CaNO :1.0ppb, bbox=[178, 833, 543, 847]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[44]: text=操作员：蒋细萍, bbox=[178, 852, 297, 866]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] coord item[45]: text=张日石, bbox=[718, 870, 786, 897]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] page=15 — 46/46 coords, api_time=16.8s
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] new_positions (48):
[[14, 512.89, 581.3149999999999, 806.636, 820.108], [14, 512.89, 581.3149999999999, 822.634, 831.054], [15, 229.67, 358.78499999999997, 58.94, 71.57], [15, 99.96, 160.65, 84.2, 95.988], [15, 245.73499999999999, 296.31, 84.2, 95.988], [15, 379.015, 478.38, 84.2, 95.988], [15, 99.96, 174.92999999999998, 97.672, 109.46], [15, 245.73499999999999, 280.84, 97.672, 109.46], [15, 379.015, 478.38, 97.672, 109.46], [15, 99.96, 180.285, 111.98599999999999, 123.774], [15, 245.73499999999999, 330.22499999999997, 111.98599999999999, 123.774], [15, 93.41499999999999, 141.015, 125.458, 137.246], [15, 99.96, 441.48999999999995, 143.982, 158.296], [15, 99.96, 441.48999999999995, 160.822, 175.136], [15, 99.96, 441.48999999999995, 178.504, 192.81799999999998], [15, 99.96, 441.48999999999995, 195.344, 209.658], [15, 99.96, 251.08999999999997, 213.02599999999998, 226.498], [15, 104.125, 456.96, 229.024, 239.97], [15, 93.41499999999999, 141.015, 242.49599999999998, 254.284], [15, 102.33999999999999, 140.42, 261.02, 271.966], [15, 102.33999999999999, 264.775, 275.334, 286.28], [15, 102.33999999999999, 282.03, 289.64799999999997, 300.594], [15, 102.33999999999999, 289.765, 303.12, 314.066], [15, 105.91, 264.775, 317.43399999999997, 327.538], [15, 310.59, 357.0, 261.02, 271.966], [15, 310.59, 477.19, 275.334, 286.28], [15, 310.59, 490.875, 289.64799999999997, 300.594], [15, 310.59, 470.04999999999995, 303.12, 314.066], [15, 313.565, 460.53, 317.43399999999997, 327.538], [15, 313.565, 427.21, 330.906, 341.01], [15, 93.41499999999999, 139.825, 454.68, 466.46799999999996], [15, 109.47999999999999, 389.72499999999997, 470.678, 480.782], [15, 99.96, 504.56, 485.834, 500.14799999999997], [15, 99.96, 504.56, 502.674, 516.9879999999999], [15, 99.96, 504.56, 519.514, 533.828], [15, 99.96, 504.56, 536.3539999999999, 550.668], [15, 99.96, 504.56, 554.036, 568.35], [15, 99.96, 504.56, 570.876, 585.1899999999999], [15, 99.96, 504.56, 589.4, 603.7139999999999], [15, 367.115, 443.275, 605.398, 615.502], [15, 99.96, 504.56, 622.2379999999999, 636.552], [15, 99.96, 504.56, 639.078, 653.3919999999999], [15, 99.96, 504.56, 655.918, 670.232], [15, 105.91, 358.78499999999997, 671.074, 681.178], [15, 105.91, 204.08499999999998, 682.02, 692.124], [15, 105.91, 323.085, 701.386, 713.174], [15, 105.91, 176.715, 717.384, 729.172], [15, 427.21, 467.66999999999996, 732.54, 755.274]]
2026-08-10 12:29:51,944 INFO     29 [qwen-vl-text] ═══ DONE ═══ 48 positions, pages=2, time=22.5s
2026-08-10 12:29:51,944 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:29:51,946 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:29:51,946 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:29:51,946 INFO     29 [qwen-vl-text] positions(108): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:29:51,946 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [108]
2026-08-10 12:29:52,117 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:29:52,118 INFO     29 [qwen-vl-text] LLM extraction start, text_len=668
2026-08-10 12:29:52,118 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:29:52,118 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 611, \"bbox_end\": 718, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"呼吸科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "一口气法弥散功能报告\n姓名：\n年龄：38岁\n性别：女\n科别：\n保险：\n预计值模式：Standard-now\n测试号：2026020917\n身高：155 cm\n体重：60 kg\n备注：\n联系电话：\n操作者：蒋细萍\nCO (%)\nVolume [L]\nCH4 [%]\n0.25\n0.20\n0.15\n0.10\n0.05\n0.00\nTime [s]\nPred\nBest\nBest%\nAct1\nDLCO SB\n[mmol/min/kPa]\n8.08\n9.45\n116.9\n9.45\nDLCO/VA\n[mmol/min/kPa/L]\n1.82\n2.38\n130.8\n2.38\nVA\n[L]\n4.29\n3.97\n92.5\n3.97\nVC IN\n[L]\n3.03\n2.26\n74.6\nDiscard vol\n[L]\n1.00\nSample vol\n[L]\n0.53\nERV\n[L]\n1.10\nIRV\n[L]\nIC\n[L]\n1.93\nVT\n[L]\n0.43\nVC MAX\n[L]\n3.03\n2.26\n74.6\nTLC-SB\n[L]\n4.44\n4.10\n92.4\n4.10\nRV-SB\n[L]\n1.41\n2.18\n154.5\n2.18\nRV%TLC-SB\n[%]\n31.88\n53.26\n167.1\n53.26\nFRC-SB\n[L]\n2.51\n2.39\n95.2\n2.39\nFRC%TLC-SB\n[%]\n51.18\n58.28\n113.9\n58.28\n测试日期\n26/2/0\n意见：\n1.弥散功能在正常范围。\n2.残气量、残总比增高，肺总量在正常范围。\n张",
    "role": "user"
  }
]
2026-08-10 12:29:58,829 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:29:58,829 INFO     29 [qwen-vl-text] LLM output (len=935):
{
  "exam_date": "2026-02-09",
  "report_date": null,
  "exam_name": "一口气法弥散功能报告",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "CO (%)\nVolume [L]\nCH4 [%]\n0.25\n0.20\n0.15\n0.10\n0.05\n0.00\nTime [s]\nPred\nBest\nBest%\nAct1\nDLCO SB\n[mmol/min/kPa]\n8.08\n9.45\n116.9\n9.45\nDLCO/VA\n[mmol/min/kPa/L]\n1.82\n2.38\n130.8\n2.38\nVA\n[L]\n4.29\n3.97\n92.5\n3.97\nVC IN\n[L]\n3.03\n2.26\n74.6\nDiscard vol\n[L]\n1.00\nSample vol\n[L]\n0.53\nERV\n[L]\n1.10\nIRV\n[L]\nIC\n[L]\n1.93\nVT\n[L]\n0.43\nVC MAX\n[L]\n3.03\n2.26\n74.6\nTLC-SB\n[L]\n4.44\n4.10\n92.4\n4.10\nRV-SB\n[L]\n1.41\n2.18\n154.5\n2.18\nRV%TLC-SB\n[%]\n31.88\n53.26\n167.1\n53.26\nFRC-SB\n[L]\n2.51\n2.39\n95.2\n2.39\nFRC%TLC-SB\n[%]\n51.18\n58.28\n113.9\n58.28",
  "conclusion": "1.弥散功能在正常范围。\n2.残气量、残总比增高，肺总量在正常范围。",
  "physician": "张",
  "reviewer": null
}
2026-08-10 12:29:58,832 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=658017, prompt_len=1606
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共108行）
["一口气法弥散功能报告", "姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-now", "测试号：2026020917", "身高：155 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "CO (%)", "Volume [L]", "CH4 [%]", "0.25", "0.20", "0.15", "0.10", "0.05", "0.00", "Time [s]", "Pred", "Best", "Best%", "Act1", "DLCO SB", "[mmol/min/kPa]", "8.08", "9.45", "116.9", "9.45", "DLCO/VA", "[mmol/min/kPa/L]", "1.82", "2.38", "130.8", "2.38", "VA", "[L]", "4.29", "3.97", "92.5", "3.97", "VC IN", "[L]", "3.03", "2.26", "74.6", "Discard vol", "[L]", "1.00", "Sample vol", "[L]", "0.53", "ERV", "[L]", "1.10", "IRV", "[L]", "IC", "[L]", "1.93", "VT", "[L]", "0.43", "VC MAX", "[L]", "3.03", "2.26", "74.6", "TLC-SB", "[L]", "4.44", "4.10", "92.4", "4.10", "RV-SB", "[L]", "1.41", "2.18", "154.5", "2.18", "RV%TLC-SB", "[%]", "31.88", "53.26", "167.1", "53.26", "FRC-SB", "[L]", "2.51", "2.39", "95.2", "2.39", "FRC%TLC-SB", "[%]", "51.18", "58.28", "113.9", "58.28", "测试日期", "26/2/0", "意见：", "1.弥散功能在正常范围。", "2.残气量、残总比增高，肺总量在正常范围。", "张"]

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
2026-08-10 12:30:26,612 INFO     29 [qwen-vl-text] coord API raw response (len=5422):
[
	{"text": "一口气法弥散功能报告", "bbox": [417, 91, 678, 107]},
	{"text": "姓名：", "bbox": [223, 119, 261, 131]},
	{"text": "年龄：38岁", "bbox": [223, 131, 405, 144]},
	{"text": "性别：女", "bbox": [223, 144, 383, 157]},
	{"text": "科别：", "bbox": [223, 157, 261, 169]},
	{"text": "保险：", "bbox": [223, 169, 261, 181]},
	{"text": "预计值模式：Standard-now", "bbox": [223, 181, 463, 194]},
	{"text": "测试号：2026020917", "bbox": [517, 119, 740, 131]},
	{"text": "身高：155 cm", "bbox": [517, 131, 709, 144]},
	{"text": "体重：60 kg", "bbox": [517, 144, 702, 157]},
	{"text": "备注：", "bbox": [517, 157, 555, 169]},
	{"text": "联系电话：", "bbox": [517, 169, 587, 181]},
	{"text": "操作者：蒋细萍", "bbox": [517, 181, 710, 194]},
	{"text": "CO (%)", "bbox": [798, 204, 835, 216]},
	{"text": "Volume [L]", "bbox": [250, 205, 307, 216]},
	{"text": "CH4 [%]", "bbox": [250, 216, 296, 226]},
	{"text": "0.25", "bbox": [250, 233, 278, 242]},
	{"text": "0.20", "bbox": [250, 264, 278, 273]},
	{"text": "0.15", "bbox": [250, 295, 278, 304]},
	{"text": "0.10", "bbox": [250, 327, 278, 336]},
	{"text": "0.05", "bbox": [250, 359, 278, 368]},
	{"text": "0.00", "bbox": [843, 393, 866, 402]},
	{"text": "Time [s]", "bbox": [523, 383, 567, 393]},
	{"text": "Pred", "bbox": [455, 412, 502, 423]},
	{"text": "Best", "bbox": [534, 412, 580, 423]},
	{"text": "Best%", "bbox": [602, 412, 660, 423]},
	{"text": "Act1", "bbox": [693, 412, 740, 423]},
	{"text": "DLCO SB", "bbox": [116, 444, 199, 456]},
	{"text": "[mmol/min/kPa]", "bbox": [261, 444, 417, 456]},
	{"text": "8.08", "bbox": [455, 444, 502, 456]},
	{"text": "9.45", "bbox": [534, 444, 580, 456]},
	{"text": "116.9", "bbox": [602, 444, 660, 456]},
	{"text": "9.45", "bbox": [693, 444, 740, 456]},
	{"text": "DLCO/VA", "bbox": [116, 460, 199, 472]},
	{"text": "[mmol/min/kPa/L]", "bbox": [237, 460, 417, 472]},
	{"text": "1.82", "bbox": [455, 460, 502, 472]},
	{"text": "2.38", "bbox": [534, 460, 580, 472]},
	{"text": "130.8", "bbox": [602, 460, 660, 472]},
	{"text": "2.38", "bbox": [693, 460, 740, 472]},
	{"text": "VA", "bbox": [116, 476, 142, 488]},
	{"text": "[L]", "bbox": [388, 476, 417, 488]},
	{"text": "4.29", "bbox": [455, 476, 502, 488]},
	{"text": "3.97", "bbox": [534, 476, 580, 488]},
	{"text": "92.5", "bbox": [615, 476, 660, 488]},
	{"text": "3.97", "bbox": [693, 476, 740, 488]},
	{"text": "VC IN", "bbox": [116, 492, 176, 504]},
	{"text": "[L]", "bbox": [388, 492, 417, 504]},
	{"text": "3.03", "bbox": [455, 492, 502, 504]},
	{"text": "2.26", "bbox": [534, 492, 580, 504]},
	{"text": "74.6", "bbox": [615, 492, 660, 504]},
	{"text": "Discard vol", "bbox": [116, 508, 245, 520]},
	{"text": "[L]", "bbox": [388, 508, 417, 520]},
	{"text": "1.00", "bbox": [693, 508, 740, 520]},
	{"text": "Sample vol", "bbox": [116, 524, 234, 536]},
	{"text": "[L]", "bbox": [388, 524, 417, 536]},
	{"text": "0.53", "bbox": [693, 524, 740, 536]},
	{"text": "ERV", "bbox": [116, 557, 153, 569]},
	{"text": "[L]", "bbox": [388, 557, 417, 569]},
	{"text": "1.10", "bbox": [455, 557, 502, 569]},
	{"text": "IRV", "bbox": [116, 573, 153, 585]},
	{"text": "[L]", "bbox": [388, 573, 417, 585]},
	{"text": "IC", "bbox": [116, 589, 141, 601]},
	{"text": "[L]", "bbox": [388, 589, 417, 601]},
	{"text": "1.93", "bbox": [455, 589, 502, 601]},
	{"text": "VT", "bbox": [116, 605, 141, 617]},
	{"text": "[L]", "bbox": [388, 605, 417, 617]},
	{"text": "0.43", "bbox": [455, 605, 502, 617]},
	{"text": "VC MAX", "bbox": [116, 621, 189, 633]},
	{"text": "[L]", "bbox": [388, 621, 417, 633]},
	{"text": "3.03", "bbox": [455, 621, 502, 633]},
	{"text": "2.26", "bbox": [534, 621, 580, 633]},
	{"text": "74.6", "bbox": [615, 621, 660, 633]},
	{"text": "TLC-SB", "bbox": [116, 638, 187, 650]},
	{"text": "[L]", "bbox": [388, 638, 417, 650]},
	{"text": "4.44", "bbox": [455, 638, 502, 650]},
	{"text": "4.10", "bbox": [534, 638, 580, 650]},
	{"text": "92.4", "bbox": [615, 638, 660, 650]},
	{"text": "4.10", "bbox": [693, 638, 740, 650]},
	{"text": "RV-SB", "bbox": [116, 654, 176, 666]},
	{"text": "[L]", "bbox": [388, 654, 417, 666]},
	{"text": "1.41", "bbox": [455, 654, 502, 666]},
	{"text": "2.18", "bbox": [534, 654, 580, 666]},
	{"text": "154.5", "bbox": [602, 654, 660, 666]},
	{"text": "2.18", "bbox": [693, 654, 740, 666]},
	{"text": "RV%TLC-SB", "bbox": [116, 670, 222, 682]},
	{"text": "[%]", "bbox": [388, 670, 417, 682]},
	{"text": "31.88", "bbox": [444, 670, 502, 682]},
	{"text": "53.26", "bbox": [523, 670, 580, 682]},
	{"text": "167.1", "bbox": [602, 670, 660, 682]},
	{"text": "53.26", "bbox": [683, 670, 740, 682]},
	{"text": "FRC-SB", "bbox": [116, 687, 187, 699]},
	{"text": "[L]", "bbox": [388, 687, 417, 699]},
	{"text": "2.51", "bbox": [455, 687, 502, 699]},
	{"text": "2.39", "bbox": [534, 687, 580, 699]},
	{"text": "95.2", "bbox": [615, 687, 660, 699]},
	{"text": "2.39", "bbox": [693, 687, 740, 699]},
	{"text": "FRC%TLC-SB", "bbox": [116, 703, 234, 715]},
	{"text": "[%]", "bbox": [388, 703, 417, 715]},
	{"text": "51.18", "bbox": [444, 703, 502, 715]},
	{"text": "58.28", "bbox": [523, 703, 580, 715]},
	{"text": "113.9", "bbox": [602, 703, 660, 715]},
	{"text": "58.28", "bbox": [683, 703, 740, 715]},
	{"text": "测试日期", "bbox": [116, 735, 210, 750]},
	{"text": "26/2/0", "bbox": [513, 737, 580, 749]},
	{"text": "意见：", "bbox": [116, 752, 173, 767]},
	{"text": "1.弥散功能在正常范围。", "bbox": [140, 771, 345, 784]},
	{"text": "2.残气量、残总比增高，肺总量在正常范围。", "bbox": [140, 784, 518, 797]},
	{"text": "张", "bbox": [878, 875, 928, 895]}
]
2026-08-10 12:30:26,612 INFO     29 [qwen-vl-text] coord API: raw_items=108, valid_items=108, elapsed=27.8s
2026-08-10 12:30:26,612 INFO     29 [qwen-vl-text] coord item[0]: text=一口气法弥散功能报告, bbox=[417, 91, 678, 107]
2026-08-10 12:30:26,612 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[223, 119, 261, 131]
2026-08-10 12:30:26,612 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：38岁, bbox=[223, 131, 405, 144]
2026-08-10 12:30:26,612 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[223, 144, 383, 157]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[4]: text=科别：, bbox=[223, 157, 261, 169]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[5]: text=保险：, bbox=[223, 169, 261, 181]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[6]: text=预计值模式：Standard-now, bbox=[223, 181, 463, 194]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：2026020917, bbox=[517, 119, 740, 131]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[8]: text=身高：155 cm, bbox=[517, 131, 709, 144]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[9]: text=体重：60 kg, bbox=[517, 144, 702, 157]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[10]: text=备注：, bbox=[517, 157, 555, 169]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话：, bbox=[517, 169, 587, 181]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[12]: text=操作者：蒋细萍, bbox=[517, 181, 710, 194]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[13]: text=CO (%), bbox=[798, 204, 835, 216]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[14]: text=Volume [L], bbox=[250, 205, 307, 216]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[15]: text=CH4 [%], bbox=[250, 216, 296, 226]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[16]: text=0.25, bbox=[250, 233, 278, 242]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[17]: text=0.20, bbox=[250, 264, 278, 273]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[18]: text=0.15, bbox=[250, 295, 278, 304]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[19]: text=0.10, bbox=[250, 327, 278, 336]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[20]: text=0.05, bbox=[250, 359, 278, 368]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[21]: text=0.00, bbox=[843, 393, 866, 402]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[22]: text=Time [s], bbox=[523, 383, 567, 393]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[23]: text=Pred, bbox=[455, 412, 502, 423]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[24]: text=Best, bbox=[534, 412, 580, 423]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[25]: text=Best%, bbox=[602, 412, 660, 423]
2026-08-10 12:30:26,613 INFO     29 [qwen-vl-text] coord item[26]: text=Act1, bbox=[693, 412, 740, 423]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[27]: text=DLCO SB, bbox=[116, 444, 199, 456]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[28]: text=[mmol/min/kPa], bbox=[261, 444, 417, 456]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[29]: text=8.08, bbox=[455, 444, 502, 456]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[30]: text=9.45, bbox=[534, 444, 580, 456]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[31]: text=116.9, bbox=[602, 444, 660, 456]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[32]: text=9.45, bbox=[693, 444, 740, 456]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[33]: text=DLCO/VA, bbox=[116, 460, 199, 472]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[34]: text=[mmol/min/kPa/L], bbox=[237, 460, 417, 472]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[35]: text=1.82, bbox=[455, 460, 502, 472]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[36]: text=2.38, bbox=[534, 460, 580, 472]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[37]: text=130.8, bbox=[602, 460, 660, 472]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[38]: text=2.38, bbox=[693, 460, 740, 472]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[39]: text=VA, bbox=[116, 476, 142, 488]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[40]: text=[L], bbox=[388, 476, 417, 488]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[41]: text=4.29, bbox=[455, 476, 502, 488]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[42]: text=3.97, bbox=[534, 476, 580, 488]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[43]: text=92.5, bbox=[615, 476, 660, 488]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[44]: text=3.97, bbox=[693, 476, 740, 488]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[45]: text=VC IN, bbox=[116, 492, 176, 504]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[46]: text=[L], bbox=[388, 492, 417, 504]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[47]: text=3.03, bbox=[455, 492, 502, 504]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[48]: text=2.26, bbox=[534, 492, 580, 504]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[49]: text=74.6, bbox=[615, 492, 660, 504]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[50]: text=Discard vol, bbox=[116, 508, 245, 520]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[51]: text=[L], bbox=[388, 508, 417, 520]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[52]: text=1.00, bbox=[693, 508, 740, 520]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[53]: text=Sample vol, bbox=[116, 524, 234, 536]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[54]: text=[L], bbox=[388, 524, 417, 536]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[55]: text=0.53, bbox=[693, 524, 740, 536]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[56]: text=ERV, bbox=[116, 557, 153, 569]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[57]: text=[L], bbox=[388, 557, 417, 569]
2026-08-10 12:30:26,614 INFO     29 [qwen-vl-text] coord item[58]: text=1.10, bbox=[455, 557, 502, 569]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[59]: text=IRV, bbox=[116, 573, 153, 585]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[60]: text=[L], bbox=[388, 573, 417, 585]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[61]: text=IC, bbox=[116, 589, 141, 601]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[62]: text=[L], bbox=[388, 589, 417, 601]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[63]: text=1.93, bbox=[455, 589, 502, 601]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[64]: text=VT, bbox=[116, 605, 141, 617]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[65]: text=[L], bbox=[388, 605, 417, 617]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[66]: text=0.43, bbox=[455, 605, 502, 617]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[67]: text=VC MAX, bbox=[116, 621, 189, 633]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[68]: text=[L], bbox=[388, 621, 417, 633]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[69]: text=3.03, bbox=[455, 621, 502, 633]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[70]: text=2.26, bbox=[534, 621, 580, 633]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[71]: text=74.6, bbox=[615, 621, 660, 633]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[72]: text=TLC-SB, bbox=[116, 638, 187, 650]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[73]: text=[L], bbox=[388, 638, 417, 650]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[74]: text=4.44, bbox=[455, 638, 502, 650]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[75]: text=4.10, bbox=[534, 638, 580, 650]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[76]: text=92.4, bbox=[615, 638, 660, 650]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[77]: text=4.10, bbox=[693, 638, 740, 650]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[78]: text=RV-SB, bbox=[116, 654, 176, 666]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[79]: text=[L], bbox=[388, 654, 417, 666]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[80]: text=1.41, bbox=[455, 654, 502, 666]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[81]: text=2.18, bbox=[534, 654, 580, 666]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[82]: text=154.5, bbox=[602, 654, 660, 666]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[83]: text=2.18, bbox=[693, 654, 740, 666]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[84]: text=RV%TLC-SB, bbox=[116, 670, 222, 682]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[85]: text=[%], bbox=[388, 670, 417, 682]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[86]: text=31.88, bbox=[444, 670, 502, 682]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[87]: text=53.26, bbox=[523, 670, 580, 682]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[88]: text=167.1, bbox=[602, 670, 660, 682]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[89]: text=53.26, bbox=[683, 670, 740, 682]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[90]: text=FRC-SB, bbox=[116, 687, 187, 699]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[91]: text=[L], bbox=[388, 687, 417, 699]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[92]: text=2.51, bbox=[455, 687, 502, 699]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[93]: text=2.39, bbox=[534, 687, 580, 699]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[94]: text=95.2, bbox=[615, 687, 660, 699]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[95]: text=2.39, bbox=[693, 687, 740, 699]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[96]: text=FRC%TLC-SB, bbox=[116, 703, 234, 715]
2026-08-10 12:30:26,615 INFO     29 [qwen-vl-text] coord item[97]: text=[%], bbox=[388, 703, 417, 715]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[98]: text=51.18, bbox=[444, 703, 502, 715]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[99]: text=58.28, bbox=[523, 703, 580, 715]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[100]: text=113.9, bbox=[602, 703, 660, 715]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[101]: text=58.28, bbox=[683, 703, 740, 715]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[102]: text=测试日期, bbox=[116, 735, 210, 750]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[103]: text=26/2/0, bbox=[513, 737, 580, 749]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[104]: text=意见：, bbox=[116, 752, 173, 767]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[105]: text=1.弥散功能在正常范围。, bbox=[140, 771, 345, 784]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[106]: text=2.残气量、残总比增高，肺总量在正常范围。, bbox=[140, 784, 518, 797]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] coord item[107]: text=张, bbox=[878, 875, 928, 895]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] page=16 — 108/108 coords, api_time=27.8s
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] new_positions (108):
[[16, 248.11499999999998, 403.40999999999997, 76.622, 90.094], [16, 132.685, 155.295, 100.198, 110.30199999999999], [16, 132.685, 240.975, 110.30199999999999, 121.24799999999999], [16, 132.685, 227.885, 121.24799999999999, 132.194], [16, 132.685, 155.295, 132.194, 142.298], [16, 132.685, 155.295, 142.298, 152.402], [16, 132.685, 275.485, 152.402, 163.34799999999998], [16, 307.615, 440.29999999999995, 100.198, 110.30199999999999], [16, 307.615, 421.85499999999996, 110.30199999999999, 121.24799999999999], [16, 307.615, 417.69, 121.24799999999999, 132.194], [16, 307.615, 330.22499999999997, 132.194, 142.298], [16, 307.615, 349.265, 142.298, 152.402], [16, 307.615, 422.45, 152.402, 163.34799999999998], [16, 474.81, 496.825, 171.768, 181.87199999999999], [16, 148.75, 182.665, 172.60999999999999, 181.87199999999999], [16, 148.75, 176.12, 181.87199999999999, 190.292], [16, 148.75, 165.41, 196.186, 203.76399999999998], [16, 148.75, 165.41, 222.28799999999998, 229.86599999999999], [16, 148.75, 165.41, 248.39, 255.968], [16, 148.75, 165.41, 275.334, 282.912], [16, 148.75, 165.41, 302.27799999999996, 309.856], [16, 501.585, 515.27, 330.906, 338.484], [16, 311.185, 337.365, 322.486, 330.906], [16, 270.72499999999997, 298.69, 346.904, 356.166], [16, 317.72999999999996, 345.09999999999997, 346.904, 356.166], [16, 358.19, 392.7, 346.904, 356.166], [16, 412.335, 440.29999999999995, 346.904, 356.166], [16, 69.02, 118.405, 373.848, 383.952], [16, 155.295, 248.11499999999998, 373.848, 383.952], [16, 270.72499999999997, 298.69, 373.848, 383.952], [16, 317.72999999999996, 345.09999999999997, 373.848, 383.952], [16, 358.19, 392.7, 373.848, 383.952], [16, 412.335, 440.29999999999995, 373.848, 383.952], [16, 69.02, 118.405, 387.32, 397.424], [16, 141.015, 248.11499999999998, 387.32, 397.424], [16, 270.72499999999997, 298.69, 387.32, 397.424], [16, 317.72999999999996, 345.09999999999997, 387.32, 397.424], [16, 358.19, 392.7, 387.32, 397.424], [16, 412.335, 440.29999999999995, 387.32, 397.424], [16, 69.02, 84.49, 400.792, 410.89599999999996], [16, 230.85999999999999, 248.11499999999998, 400.792, 410.89599999999996], [16, 270.72499999999997, 298.69, 400.792, 410.89599999999996], [16, 317.72999999999996, 345.09999999999997, 400.792, 410.89599999999996], [16, 365.925, 392.7, 400.792, 410.89599999999996], [16, 412.335, 440.29999999999995, 400.792, 410.89599999999996], [16, 69.02, 104.72, 414.264, 424.368], [16, 230.85999999999999, 248.11499999999998, 414.264, 424.368], [16, 270.72499999999997, 298.69, 414.264, 424.368], [16, 317.72999999999996, 345.09999999999997, 414.264, 424.368], [16, 365.925, 392.7, 414.264, 424.368], [16, 69.02, 145.775, 427.736, 437.84], [16, 230.85999999999999, 248.11499999999998, 427.736, 437.84], [16, 412.335, 440.29999999999995, 427.736, 437.84], [16, 69.02, 139.23, 441.20799999999997, 451.312], [16, 230.85999999999999, 248.11499999999998, 441.20799999999997, 451.312], [16, 412.335, 440.29999999999995, 441.20799999999997, 451.312], [16, 69.02, 91.035, 468.99399999999997, 479.09799999999996], [16, 230.85999999999999, 248.11499999999998, 468.99399999999997, 479.09799999999996], [16, 270.72499999999997, 298.69, 468.99399999999997, 479.09799999999996], [16, 69.02, 91.035, 482.466, 492.57], [16, 230.85999999999999, 248.11499999999998, 482.466, 492.57], [16, 69.02, 83.895, 495.938, 506.042], [16, 230.85999999999999, 248.11499999999998, 495.938, 506.042], [16, 270.72499999999997, 298.69, 495.938, 506.042], [16, 69.02, 83.895, 509.40999999999997, 519.514], [16, 230.85999999999999, 248.11499999999998, 509.40999999999997, 519.514], [16, 270.72499999999997, 298.69, 509.40999999999997, 519.514], [16, 69.02, 112.455, 522.882, 532.986], [16, 230.85999999999999, 248.11499999999998, 522.882, 532.986], [16, 270.72499999999997, 298.69, 522.882, 532.986], [16, 317.72999999999996, 345.09999999999997, 522.882, 532.986], [16, 365.925, 392.7, 522.882, 532.986], [16, 69.02, 111.265, 537.196, 547.3], [16, 230.85999999999999, 248.11499999999998, 537.196, 547.3], [16, 270.72499999999997, 298.69, 537.196, 547.3], [16, 317.72999999999996, 345.09999999999997, 537.196, 547.3], [16, 365.925, 392.7, 537.196, 547.3], [16, 412.335, 440.29999999999995, 537.196, 547.3], [16, 69.02, 104.72, 550.668, 560.7719999999999], [16, 230.85999999999999, 248.11499999999998, 550.668, 560.7719999999999], [16, 270.72499999999997, 298.69, 550.668, 560.7719999999999], [16, 317.72999999999996, 345.09999999999997, 550.668, 560.7719999999999], [16, 358.19, 392.7, 550.668, 560.7719999999999], [16, 412.335, 440.29999999999995, 550.668, 560.7719999999999], [16, 69.02, 132.09, 564.14, 574.244], [16, 230.85999999999999, 248.11499999999998, 564.14, 574.244], [16, 264.18, 298.69, 564.14, 574.244], [16, 311.185, 345.09999999999997, 564.14, 574.244], [16, 358.19, 392.7, 564.14, 574.244], [16, 406.385, 440.29999999999995, 564.14, 574.244], [16, 69.02, 111.265, 578.454, 588.558], [16, 230.85999999999999, 248.11499999999998, 578.454, 588.558], [16, 270.72499999999997, 298.69, 578.454, 588.558], [16, 317.72999999999996, 345.09999999999997, 578.454, 588.558], [16, 365.925, 392.7, 578.454, 588.558], [16, 412.335, 440.29999999999995, 578.454, 588.558], [16, 69.02, 139.23, 591.9259999999999, 602.03], [16, 230.85999999999999, 248.11499999999998, 591.9259999999999, 602.03], [16, 264.18, 298.69, 591.9259999999999, 602.03], [16, 311.185, 345.09999999999997, 591.9259999999999, 602.03], [16, 358.19, 392.7, 591.9259999999999, 602.03], [16, 406.385, 440.29999999999995, 591.9259999999999, 602.03], [16, 69.02, 124.94999999999999, 618.87, 631.5], [16, 305.235, 345.09999999999997, 620.554, 630.658], [16, 69.02, 102.935, 633.184, 645.814], [16, 83.3, 205.27499999999998, 649.182, 660.1279999999999], [16, 83.3, 308.21, 660.1279999999999, 671.074], [16, 522.41, 552.16, 736.75, 753.5899999999999]]
2026-08-10 12:30:26,616 INFO     29 [qwen-vl-text] ═══ DONE ═══ 108 positions, pages=1, time=34.7s
2026-08-10 12:30:26,616 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:30:26,623 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:30:26,623 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:30:26,623 INFO     29 [qwen-vl-text] positions(248): [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:30:26,623 INFO     29 [qwen-vl-text] page grouping: [17], lines per page: [248]
2026-08-10 12:30:26,806 INFO     29 [qwen-vl-text] page=17, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:30:26,808 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1452
2026-08-10 12:30:26,808 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:30:26,809 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 719, \"bbox_end\": 966, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"呼吸科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能试验报告\n姓名：\n年龄：38岁\n性别：女\n科别：\n保险：\n预计值模式：Standard-new\n测试号：2026020017\n身高：166 cm\n体重：60 kg\n备注：\n联系电话：\n操作者：蒋细萍\nPred\nA1 A1/Pd\nP1 A2/Pd chg%l\nP2 A3/Pd chg%2\nP3 A4/Pd chg%3\nFVC\n[L]\n2.99\n2.21\n74.0\n2.63\n87.9\n18.72\n2.04\n88.2\n19.17\n2.67\n86.0\n16.23\nFEV 1\n[L]\n2.67\n1.25\n48.6\n1.62\n69.2\n21.85\n1.84\n69.8\n23.23\n1.60\n68.4\n20.23\nFEV 1 % FVC\n[%]\n84.19\n56.48\n67.1\n67.97\n68.9\n2.64\n68.40\n69.4\n3.41\n68.42\n69.4\n3.44\nFEV 1 % VC MAX\n[%]\n81.88\n65.26\n67.6\n67.97\n70.8\n4.91\n68.40\n71.3\n6.70\n68.42\n71.4\n5.73\nVC MAX\n[L]\n3.03\n2.26\n74.6\n2.63\n86.6\n16.14\n2.64\n87.0\n16.69\n2.57\n84.8\n13.71\nPEF\n[L/s]\n6.28\n2.66\n42.4\n2.90\n46.2\n9.17\n3.37\n53.7\n26.79\n3.42\n64.6\n28.64\nMMEF 75/25\n[L/s]\n3.57\n0.61\n14.4\n0.67\n18.8\n31.03\n0.73\n20.4\n42.01\n0.69\n19.4\n35.02\nMEF 50\n[L/s]\n4.01\n0.68\n17.0\n0.90\n22.5\n32.75\n0.89\n22.1\n30.15\n0.88\n21.9\n29.17\nMEF 25\n[L/s]\n1.79\n0.19\n10.5\n0.27\n15.2\n44.16\n0.33\n18.7\n77.66\n0.31\n17.6\n66.49\nFET\n[s]\n7.63\n8.01\n4.99\n7.79\n2.14\n7.43\n-2.60\nV backextrapolation ex [L]\n0.05\n0.04\n-11.67\n0.04\n-18.64\n0.04\n-13.51\nPIF\n[L/s]\n3.04\n3.37\n10.91\n3.51\n15.70\n3.60\n18.67\nFIV1\n[L]\n2.21\n2.56\n15.71\n2.56\n15.66\n2.50\n13.09\nPEF50 % FIF50\n[%]\n22.86\n28.15\n23.14\n25.36\n10.95\n27.28\n19.33\nMVV\n[L/min]\n99.77\n46.21\n46.3\nBF MVV\n[1/min]\n75.55\n10\nFlow [L/s]\nF/V ex\n1\n2\n3\n4\n6\n8\n4\n2\n0\nVol [L]\n1\n2\n3\n4\n5\n10\nF/V In\nVol%VCmax\n0\n0\nVol [L]\n20\n40\n60\n80\n100\n1\n2\nVCmax\n3\n4\n5\n6\nTime [s]\n0\n2\n4\n6\n8\n10\n12\n14\n意见：\n1. 中重度阻塞性肺通气功能障碍。\n2. 支气管舒张试验阳性。\n(1. 24h内无支气管舒张药物使用史)\n(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)\n(3. 检查质量：舒张前：A级；舒张后：A级)\n张四彩",
    "role": "user"
  }
]
2026-08-10 12:30:26,812 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:30:26.811+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:30:39,715 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:30:39,715 INFO     29 [qwen-vl-text] LLM output (len=2168):
{
  "exam_date": "2026-02-09",
  "report_date": "2026-02-09",
  "exam_name": "肺功能试验",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "呼吸科门诊",
  "bed_number": null,
  "findings": "预计值模式：Standard-new\n测试号：2026020017\n身高：166 cm\n体重：60 kg\n操作者：蒋细萍\n\n| 指标 | Pred | A1 | A1/Pd | P1 | A2/Pd | chg%l | P2 | A3/Pd | chg%2 | P3 | A4/Pd | chg%3 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| FVC [L] | 2.99 | 2.21 | 74.0 | 2.63 | 87.9 | 18.72 | 2.04 | 88.2 | 19.17 | 2.67 | 86.0 | 16.23 |\n| FEV 1 [L] | 2.67 | 1.25 | 48.6 | 1.62 | 69.2 | 21.85 | 1.84 | 69.8 | 23.23 | 1.60 | 68.4 | 20.23 |\n| FEV 1 % FVC [%] | 84.19 | 56.48 | 67.1 | 67.97 | 68.9 | 2.64 | 68.40 | 69.4 | 3.41 | 68.42 | 69.4 | 3.44 |\n| FEV 1 % VC MAX [%] | 81.88 | 65.26 | 67.6 | 67.97 | 70.8 | 4.91 | 68.40 | 71.3 | 6.70 | 68.42 | 71.4 | 5.73 |\n| VC MAX [L] | 3.03 | 2.26 | 74.6 | 2.63 | 86.6 | 16.14 | 2.64 | 87.0 | 16.69 | 2.57 | 84.8 | 13.71 |\n| PEF [L/s] | 6.28 | 2.66 | 42.4 | 2.90 | 46.2 | 9.17 | 3.37 | 53.7 | 26.79 | 3.42 | 64.6 | 28.64 |\n| MMEF 75/25 [L/s] | 3.57 | 0.61 | 14.4 | 0.67 | 18.8 | 31.03 | 0.73 | 20.4 | 42.01 | 0.69 | 19.4 | 35.02 |\n| MEF 50 [L/s] | 4.01 | 0.68 | 17.0 | 0.90 | 22.5 | 32.75 | 0.89 | 22.1 | 30.15 | 0.88 | 21.9 | 29.17 |\n| MEF 25 [L/s] | 1.79 | 0.19 | 10.5 | 0.27 | 15.2 | 44.16 | 0.33 | 18.7 | 77.66 | 0.31 | 17.6 | 66.49 |\n| FET [s] | 7.63 | 8.01 | 4.99 | 7.79 | 2.14 | 7.43 | -2.60 | | | | | |\n| V backextrapolation ex [L] | 0.05 | 0.04 | -11.67 | 0.04 | -18.64 | 0.04 | -13.51 | | | | | |\n| PIF [L/s] | 3.04 | 3.37 | 10.91 | 3.51 | 15.70 | 3.60 | 18.67 | | | | | |\n| FIV1 [L] | 2.21 | 2.56 | 15.71 | 2.56 | 15.66 | 2.50 | 13.09 | | | | | |\n| PEF50 % FIF50 [%] | 22.86 | 28.15 | 23.14 | 25.36 | 10.95 | 27.28 | 19.33 | | | | | |\n| MVV [L/min] | 99.77 | 46.21 | 46.3 | | | | | | | | | |\n| BF MVV [1/min] | 75.55 | 10 | | | | | | | | | | |",
  "conclusion": "意见：\n1. 中重度阻塞性肺通气功能障碍。\n2. 支气管舒张试验阳性。\n(1. 24h内无支气管舒张药物使用史)\n(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)\n(3. 检查质量：舒张前：A级；舒张后：A级)",
  "physician": "张四彩",
  "reviewer": null
}
2026-08-10 12:30:39,717 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=864636, prompt_len=2810
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共248行）
["肺功能试验报告", "姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-new", "测试号：2026020017", "身高：166 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "Pred", "A1 A1/Pd", "P1 A2/Pd chg%l", "P2 A3/Pd chg%2", "P3 A4/Pd chg%3", "FVC", "[L]", "2.99", "2.21", "74.0", "2.63", "87.9", "18.72", "2.04", "88.2", "19.17", "2.67", "86.0", "16.23", "FEV 1", "[L]", "2.67", "1.25", "48.6", "1.62", "69.2", "21.85", "1.84", "69.8", "23.23", "1.60", "68.4", "20.23", "FEV 1 % FVC", "[%]", "84.19", "56.48", "67.1", "67.97", "68.9", "2.64", "68.40", "69.4", "3.41", "68.42", "69.4", "3.44", "FEV 1 % VC MAX", "[%]", "81.88", "65.26", "67.6", "67.97", "70.8", "4.91", "68.40", "71.3", "6.70", "68.42", "71.4", "5.73", "VC MAX", "[L]", "3.03", "2.26", "74.6", "2.63", "86.6", "16.14", "2.64", "87.0", "16.69", "2.57", "84.8", "13.71", "PEF", "[L/s]", "6.28", "2.66", "42.4", "2.90", "46.2", "9.17", "3.37", "53.7", "26.79", "3.42", "64.6", "28.64", "MMEF 75/25", "[L/s]", "3.57", "0.61", "14.4", "0.67", "18.8", "31.03", "0.73", "20.4", "42.01", "0.69", "19.4", "35.02", "MEF 50", "[L/s]", "4.01", "0.68", "17.0", "0.90", "22.5", "32.75", "0.89", "22.1", "30.15", "0.88", "21.9", "29.17", "MEF 25", "[L/s]", "1.79", "0.19", "10.5", "0.27", "15.2", "44.16", "0.33", "18.7", "77.66", "0.31", "17.6", "66.49", "FET", "[s]", "7.63", "8.01", "4.99", "7.79", "2.14", "7.43", "-2.60", "V backextrapolation ex [L]", "0.05", "0.04", "-11.67", "0.04", "-18.64", "0.04", "-13.51", "PIF", "[L/s]", "3.04", "3.37", "10.91", "3.51", "15.70", "3.60", "18.67", "FIV1", "[L]", "2.21", "2.56", "15.71", "2.56", "15.66", "2.50", "13.09", "PEF50 % FIF50", "[%]", "22.86", "28.15", "23.14", "25.36", "10.95", "27.28", "19.33", "MVV", "[L/min]", "99.77", "46.21", "46.3", "BF MVV", "[1/min]", "75.55", "10", "Flow [L/s]", "F/V ex", "1", "2", "3", "4", "6", "8", "4", "2", "0", "Vol [L]", "1", "2", "3", "4", "5", "10", "F/V In", "Vol%VCmax", "0", "0", "Vol [L]", "20", "40", "60", "80", "100", "1", "2", "VCmax", "3", "4", "5", "6", "Time [s]", "0", "2", "4", "6", "8", "10", "12", "14", "意见：", "1. 中重度阻塞性肺通气功能障碍。", "2. 支气管舒张试验阳性。", "(1. 24h内无支气管舒张药物使用史)", "(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)", "(3. 检查质量：舒张前：A级；舒张后：A级)", "张四彩"]

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
2026-08-10 12:31:44,559 INFO     29 [qwen-vl-text] coord API raw response (len=12318):
[
	{"text": "肺功能试验报告", "bbox": [475, 71, 561, 84]},
	{"text": "姓名：", "bbox": [250, 100, 286, 112]},
	{"text": "年龄：38岁", "bbox": [250, 112, 422, 124]},
	{"text": "性别：女", "bbox": [250, 124, 402, 137]},
	{"text": "科别：", "bbox": [250, 137, 286, 149]},
	{"text": "保险：", "bbox": [250, 149, 286, 161]},
	{"text": "预计值模式：Standard-new", "bbox": [250, 161, 475, 174]},
	{"text": "测试号：2026020017", "bbox": [528, 98, 740, 110]},
	{"text": "身高：166 cm", "bbox": [528, 110, 710, 123]},
	{"text": "体重：60 kg", "bbox": [528, 123, 704, 135]},
	{"text": "备注：", "bbox": [528, 135, 564, 148]},
	{"text": "联系电话：", "bbox": [528, 148, 594, 160]},
	{"text": "操作者：蒋细萍", "bbox": [666, 160, 709, 173]},
	{"text": "Pred", "bbox": [338, 188, 370, 200]},
	{"text": "A1 A1/Pd", "bbox": [398, 188, 461, 200]},
	{"text": "P1 A2/Pd chg%l", "bbox": [490, 188, 602, 200]},
	{"text": "P2 A3/Pd chg%2", "bbox": [634, 188, 748, 200]},
	{"text": "P3 A4/Pd chg%3", "bbox": [780, 188, 892, 200]},
	{"text": "FVC", "bbox": [128, 215, 152, 227]},
	{"text": "[L]", "bbox": [303, 215, 323, 227]},
	{"text": "2.99", "bbox": [338, 215, 370, 227]},
	{"text": "2.21", "bbox": [384, 215, 415, 227]},
	{"text": "74.0", "bbox": [429, 215, 461, 227]},
	{"text": "2.63", "bbox": [475, 215, 506, 227]},
	{"text": "87.9", "bbox": [520, 215, 551, 227]},
	{"text": "18.72", "bbox": [566, 215, 604, 227]},
	{"text": "2.04", "bbox": [619, 215, 650, 227]},
	{"text": "88.2", "bbox": [665, 215, 697, 227]},
	{"text": "19.17", "bbox": [711, 215, 748, 227]},
	{"text": "2.67", "bbox": [764, 215, 795, 227]},
	{"text": "86.0", "bbox": [810, 215, 841, 227]},
	{"text": "16.23", "bbox": [855, 215, 892, 227]},
	{"text": "FEV 1", "bbox": [128, 227, 165, 240]},
	{"text": "[L]", "bbox": [303, 227, 323, 240]},
	{"text": "2.67", "bbox": [338, 227, 370, 240]},
	{"text": "1.25", "bbox": [384, 227, 415, 240]},
	{"text": "48.6", "bbox": [429, 227, 461, 240]},
	{"text": "1.62", "bbox": [475, 227, 506, 240]},
	{"text": "69.2", "bbox": [520, 227, 551, 240]},
	{"text": "21.85", "bbox": [566, 227, 604, 240]},
	{"text": "1.84", "bbox": [619, 227, 650, 240]},
	{"text": "69.8", "bbox": [665, 227, 697, 240]},
	{"text": "23.23", "bbox": [711, 227, 748, 240]},
	{"text": "1.60", "bbox": [764, 227, 795, 240]},
	{"text": "68.4", "bbox": [810, 227, 841, 240]},
	{"text": "20.23", "bbox": [855, 227, 892, 240]},
	{"text": "FEV 1 % FVC", "bbox": [128, 240, 212, 252]},
	{"text": "[%]", "bbox": [303, 240, 323, 252]},
	{"text": "84.19", "bbox": [338, 240, 370, 252]},
	{"text": "56.48", "bbox": [384, 240, 415, 252]},
	{"text": "67.1", "bbox": [429, 240, 461, 252]},
	{"text": "67.97", "bbox": [475, 240, 506, 252]},
	{"text": "68.9", "bbox": [520, 240, 551, 252]},
	{"text": "2.64", "bbox": [566, 240, 604, 252]},
	{"text": "68.40", "bbox": [619, 240, 650, 252]},
	{"text": "69.4", "bbox": [665, 240, 697, 252]},
	{"text": "3.41", "bbox": [711, 240, 748, 252]},
	{"text": "68.42", "bbox": [764, 240, 795, 252]},
	{"text": "69.4", "bbox": [810, 240, 841, 252]},
	{"text": "3.44", "bbox": [855, 240, 892, 252]},
	{"text": "FEV 1 % VC MAX", "bbox": [128, 252, 234, 265]},
	{"text": "[%]", "bbox": [303, 252, 323, 265]},
	{"text": "81.88", "bbox": [338, 252, 370, 265]},
	{"text": "65.26", "bbox": [384, 252, 415, 265]},
	{"text": "67.6", "bbox": [429, 252, 461, 265]},
	{"text": "67.97", "bbox": [475, 252, 506, 265]},
	{"text": "70.8", "bbox": [520, 252, 551, 265]},
	{"text": "4.91", "bbox": [566, 252, 604, 265]},
	{"text": "68.40", "bbox": [619, 252, 650, 265]},
	{"text": "71.3", "bbox": [665, 252, 697, 265]},
	{"text": "6.70", "bbox": [711, 252, 748, 265]},
	{"text": "68.42", "bbox": [764, 252, 795, 265]},
	{"text": "71.4", "bbox": [810, 252, 841, 265]},
	{"text": "5.73", "bbox": [855, 252, 892, 265]},
	{"text": "VC MAX", "bbox": [128, 265, 174, 277]},
	{"text": "[L]", "bbox": [303, 265, 323, 277]},
	{"text": "3.03", "bbox": [338, 265, 370, 277]},
	{"text": "2.26", "bbox": [384, 265, 415, 277]},
	{"text": "74.6", "bbox": [429, 265, 461, 277]},
	{"text": "2.63", "bbox": [475, 265, 506, 277]},
	{"text": "86.6", "bbox": [520, 265, 551, 277]},
	{"text": "16.14", "bbox": [566, 265, 604, 277]},
	{"text": "2.64", "bbox": [619, 265, 650, 277]},
	{"text": "87.0", "bbox": [665, 265, 697, 277]},
	{"text": "16.69", "bbox": [711, 265, 748, 277]},
	{"text": "2.57", "bbox": [764, 265, 795, 277]},
	{"text": "84.8", "bbox": [810, 265, 841, 277]},
	{"text": "13.71", "bbox": [855, 265, 892, 277]},
	{"text": "PEF", "bbox": [128, 277, 152, 290]},
	{"text": "[L/s]", "bbox": [288, 277, 323, 290]},
	{"text": "6.28", "bbox": [338, 277, 370, 290]},
	{"text": "2.66", "bbox": [384, 277, 415, 290]},
	{"text": "42.4", "bbox": [429, 277, 461, 290]},
	{"text": "2.90", "bbox": [475, 277, 506, 290]},
	{"text": "46.2", "bbox": [520, 277, 551, 290]},
	{"text": "9.17", "bbox": [566, 277, 604, 290]},
	{"text": "3.37", "bbox": [619, 277, 650, 290]},
	{"text": "53.7", "bbox": [665, 277, 697, 290]},
	{"text": "26.79", "bbox": [711, 277, 748, 290]},
	{"text": "3.42", "bbox": [764, 277, 795, 290]},
	{"text": "64.6", "bbox": [810, 277, 841, 290]},
	{"text": "28.64", "bbox": [855, 277, 892, 290]},
	{"text": "MMEF 75/25", "bbox": [128, 290, 203, 303]},
	{"text": "[L/s]", "bbox": [288, 290, 323, 303]},
	{"text": "3.57", "bbox": [338, 290, 370, 303]},
	{"text": "0.61", "bbox": [384, 290, 415, 303]},
	{"text": "14.4", "bbox": [429, 290, 461, 303]},
	{"text": "0.67", "bbox": [475, 290, 506, 303]},
	{"text": "18.8", "bbox": [520, 290, 551, 303]},
	{"text": "31.03", "bbox": [566, 290, 604, 303]},
	{"text": "0.73", "bbox": [619, 290, 650, 303]},
	{"text": "20.4", "bbox": [665, 290, 697, 303]},
	{"text": "42.01", "bbox": [711, 290, 748, 303]},
	{"text": "0.69", "bbox": [764, 290, 795, 303]},
	{"text": "19.4", "bbox": [810, 290, 841, 303]},
	{"text": "35.02", "bbox": [855, 290, 892, 303]},
	{"text": "MEF 50", "bbox": [128, 303, 174, 315]},
	{"text": "[L/s]", "bbox": [288, 303, 323, 315]},
	{"text": "4.01", "bbox": [338, 303, 370, 315]},
	{"text": "0.68", "bbox": [384, 303, 415, 315]},
	{"text": "17.0", "bbox": [429, 303, 461, 315]},
	{"text": "0.90", "bbox": [475, 303, 506, 315]},
	{"text": "22.5", "bbox": [520, 303, 551, 315]},
	{"text": "32.75", "bbox": [566, 303, 604, 315]},
	{"text": "0.89", "bbox": [619, 303, 650, 315]},
	{"text": "22.1", "bbox": [665, 303, 697, 315]},
	{"text": "30.15", "bbox": [711, 303, 748, 315]},
	{"text": "0.88", "bbox": [764, 303, 795, 315]},
	{"text": "21.9", "bbox": [810, 303, 841, 315]},
	{"text": "29.17", "bbox": [855, 303, 892, 315]},
	{"text": "MEF 25", "bbox": [128, 315, 174, 328]},
	{"text": "[L/s]", "bbox": [288, 315, 323, 328]},
	{"text": "1.79", "bbox": [338, 315, 370, 328]},
	{"text": "0.19", "bbox": [384, 315, 415, 328]},
	{"text": "10.5", "bbox": [429, 315, 461, 328]},
	{"text": "0.27", "bbox": [475, 315, 506, 328]},
	{"text": "15.2", "bbox": [520, 315, 551, 328]},
	{"text": "44.16", "bbox": [566, 315, 604, 328]},
	{"text": "0.33", "bbox": [619, 315, 650, 328]},
	{"text": "18.7", "bbox": [665, 315, 697, 328]},
	{"text": "77.66", "bbox": [711, 315, 748, 328]},
	{"text": "0.31", "bbox": [764, 315, 795, 328]},
	{"text": "17.6", "bbox": [810, 315, 841, 328]},
	{"text": "66.49", "bbox": [855, 315, 892, 328]},
	{"text": "FET", "bbox": [128, 328, 152, 341]},
	{"text": "[s]", "bbox": [303, 328, 323, 341]},
	{"text": "7.63", "bbox": [384, 328, 415, 341]},
	{"text": "8.01", "bbox": [475, 328, 506, 341]},
	{"text": "4.99", "bbox": [571, 328, 604, 341]},
	{"text": "7.79", "bbox": [619, 328, 650, 341]},
	{"text": "2.14", "bbox": [717, 328, 748, 341]},
	{"text": "7.43", "bbox": [764, 328, 795, 341]},
	{"text": "-2.60", "bbox": [855, 328, 892, 341]},
	{"text": "V backextrapolation ex [L]", "bbox": [128, 341, 323, 354]},
	{"text": "0.05", "bbox": [384, 341, 415, 354]},
	{"text": "0.04", "bbox": [475, 341, 506, 354]},
	{"text": "-11.67", "bbox": [556, 341, 604, 354]},
	{"text": "0.04", "bbox": [619, 341, 650, 354]},
	{"text": "-18.64", "bbox": [704, 341, 748, 354]},
	{"text": "0.04", "bbox": [764, 341, 795, 354]},
	{"text": "-13.51", "bbox": [847, 341, 892, 354]},
	{"text": "PIF", "bbox": [128, 354, 152, 367]},
	{"text": "[L/s]", "bbox": [288, 354, 323, 367]},
	{"text": "3.04", "bbox": [384, 354, 415, 367]},
	{"text": "3.37", "bbox": [475, 354, 506, 367]},
	{"text": "10.91", "bbox": [566, 354, 604, 367]},
	{"text": "3.51", "bbox": [619, 354, 650, 367]},
	{"text": "15.70", "bbox": [711, 354, 748, 367]},
	{"text": "3.60", "bbox": [764, 354, 795, 367]},
	{"text": "18.67", "bbox": [855, 354, 892, 367]},
	{"text": "FIV1", "bbox": [128, 367, 158, 380]},
	{"text": "[L]", "bbox": [303, 367, 323, 380]},
	{"text": "2.21", "bbox": [384, 367, 415, 380]},
	{"text": "2.56", "bbox": [475, 367, 506, 380]},
	{"text": "15.71", "bbox": [566, 367, 604, 380]},
	{"text": "2.56", "bbox": [619, 367, 650, 380]},
	{"text": "15.66", "bbox": [711, 367, 748, 380]},
	{"text": "2.50", "bbox": [764, 367, 795, 380]},
	{"text": "13.09", "bbox": [855, 367, 892, 380]},
	{"text": "PEF50 % FIF50", "bbox": [128, 380, 225, 393]},
	{"text": "[%]", "bbox": [303, 380, 323, 393]},
	{"text": "22.86", "bbox": [375, 380, 415, 393]},
	{"text": "28.15", "bbox": [467, 380, 506, 393]},
	{"text": "23.14", "bbox": [566, 380, 604, 393]},
	{"text": "25.36", "bbox": [619, 380, 650, 393]},
	{"text": "10.95", "bbox": [711, 380, 748, 393]},
	{"text": "27.28", "bbox": [756, 380, 795, 393]},
	{"text": "19.33", "bbox": [855, 380, 892, 393]},
	{"text": "MVV", "bbox": [128, 393, 152, 406]},
	{"text": "[L/min]", "bbox": [272, 393, 323, 406]},
	{"text": "99.77", "bbox": [331, 393, 370, 406]},
	{"text": "46.21", "bbox": [378, 393, 415, 406]},
	{"text": "46.3", "bbox": [429, 393, 461, 406]},
	{"text": "BF MVV", "bbox": [128, 406, 174, 419]},
	{"text": "[1/min]", "bbox": [272, 406, 323, 419]},
	{"text": "75.55", "bbox": [375, 406, 415, 419]},
	{"text": "10", "bbox": [216, 457, 227, 467]},
	{"text": "Flow [L/s]", "bbox": [235, 460, 284, 471]},
	{"text": "F/V ex", "bbox": [328, 460, 361, 470]},
	{"text": "1", "bbox": [430, 460, 459, 470]},
	{"text": "2", "bbox": [430, 470, 459, 480]},
	{"text": "3", "bbox": [430, 480, 459, 490]},
	{"text": "4", "bbox": [430, 490, 459, 500]},
	{"text": "6", "bbox": [220, 508, 229, 517]},
	{"text": "8", "bbox": [220, 483, 229, 492]},
	{"text": "4", "bbox": [220, 533, 229, 542]},
	{"text": "2", "bbox": [220, 558, 229, 567]},
	{"text": "0", "bbox": [220, 583, 229, 592]},
	{"text": "Vol [L]", "bbox": [367, 574, 402, 585]},
	{"text": "1", "bbox": [264, 593, 272, 602]},
	{"text": "2", "bbox": [296, 593, 304, 602]},
	{"text": "3", "bbox": [330, 593, 338, 602]},
	{"text": "4", "bbox": [363, 593, 371, 602]},
	{"text": "5", "bbox": [397, 593, 405, 602]},
	{"text": "10", "bbox": [216, 712, 227, 721]},
	{"text": "F/V In", "bbox": [330, 706, 360, 716]},
	{"text": "Vol%VCmax", "bbox": [516, 503, 574, 513]},
	{"text": "0", "bbox": [529, 513, 538, 523]},
	{"text": "0", "bbox": [547, 513, 556, 523]},
	{"text": "Vol [L]", "bbox": [563, 517, 594, 528]},
	{"text": "20", "bbox": [524, 525, 538, 535]},
	{"text": "40", "bbox": [524, 537, 538, 547]},
	{"text": "60", "bbox": [524, 549, 538, 559]},
	{"text": "80", "bbox": [524, 561, 538, 571]},
	{"text": "100", "bbox": [519, 573, 538, 583]},
	{"text": "2", "bbox": [547, 559, 556, 569]},
	{"text": "VCmax", "bbox": [571, 570, 608, 579]},
	{"text": "3", "bbox": [547, 581, 556, 591]},
	{"text": "4", "bbox": [547, 605, 556, 615]},
	{"text": "5", "bbox": [547, 628, 556, 638]},
	{"text": "6", "bbox": [547, 651, 556, 661]},
	{"text": "Time [s]", "bbox": [714, 642, 754, 653]},
	{"text": "0", "bbox": [556, 661, 564, 670]},
	{"text": "2", "bbox": [603, 661, 611, 670]},
	{"text": "4", "bbox": [650, 661, 658, 670]},
	{"text": "6", "bbox": [697, 661, 705, 670]},
	{"text": "8", "bbox": [743, 661, 751, 670]},
	{"text": "10", "bbox": [789, 661, 800, 670]},
	{"text": "12", "bbox": [835, 661, 847, 670]},
	{"text": "14", "bbox": [882, 661, 894, 670]},
	{"text": "意见：", "bbox": [107, 735, 151, 749]},
	{"text": "1. 中重度阻塞性肺通气功能障碍。", "bbox": [107, 750, 325, 763]},
	{"text": "2. 支气管舒张试验阳性。", "bbox": [107, 763, 265, 775]},
	{"text": "(1. 24h内无支气管舒张药物使用史)", "bbox": [112, 775, 348, 787]},
	{"text": "(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)", "bbox": [107, 786, 651, 798]},
	{"text": "(3. 检查质量：舒张前：A级；舒张后：A级)", "bbox": [107, 798, 392, 810]},
	{"text": "张四彩", "bbox": [816, 875, 877, 894]}
]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord API: raw_items=247, valid_items=247, elapsed=64.8s
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能试验报告, bbox=[475, 71, 561, 84]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[250, 100, 286, 112]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：38岁, bbox=[250, 112, 422, 124]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[250, 124, 402, 137]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[4]: text=科别：, bbox=[250, 137, 286, 149]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[5]: text=保险：, bbox=[250, 149, 286, 161]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[6]: text=预计值模式：Standard-new, bbox=[250, 161, 475, 174]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：2026020017, bbox=[528, 98, 740, 110]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[8]: text=身高：166 cm, bbox=[528, 110, 710, 123]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[9]: text=体重：60 kg, bbox=[528, 123, 704, 135]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[10]: text=备注：, bbox=[528, 135, 564, 148]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话：, bbox=[528, 148, 594, 160]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[12]: text=操作者：蒋细萍, bbox=[666, 160, 709, 173]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[13]: text=Pred, bbox=[338, 188, 370, 200]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[14]: text=A1 A1/Pd, bbox=[398, 188, 461, 200]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[15]: text=P1 A2/Pd chg%l, bbox=[490, 188, 602, 200]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[16]: text=P2 A3/Pd chg%2, bbox=[634, 188, 748, 200]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[17]: text=P3 A4/Pd chg%3, bbox=[780, 188, 892, 200]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[18]: text=FVC, bbox=[128, 215, 152, 227]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[19]: text=[L], bbox=[303, 215, 323, 227]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[20]: text=2.99, bbox=[338, 215, 370, 227]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[21]: text=2.21, bbox=[384, 215, 415, 227]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[22]: text=74.0, bbox=[429, 215, 461, 227]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[23]: text=2.63, bbox=[475, 215, 506, 227]
2026-08-10 12:31:44,560 INFO     29 [qwen-vl-text] coord item[24]: text=87.9, bbox=[520, 215, 551, 227]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[25]: text=18.72, bbox=[566, 215, 604, 227]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[26]: text=2.04, bbox=[619, 215, 650, 227]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[27]: text=88.2, bbox=[665, 215, 697, 227]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[28]: text=19.17, bbox=[711, 215, 748, 227]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[29]: text=2.67, bbox=[764, 215, 795, 227]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[30]: text=86.0, bbox=[810, 215, 841, 227]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[31]: text=16.23, bbox=[855, 215, 892, 227]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[32]: text=FEV 1, bbox=[128, 227, 165, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[33]: text=[L], bbox=[303, 227, 323, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[34]: text=2.67, bbox=[338, 227, 370, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[35]: text=1.25, bbox=[384, 227, 415, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[36]: text=48.6, bbox=[429, 227, 461, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[37]: text=1.62, bbox=[475, 227, 506, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[38]: text=69.2, bbox=[520, 227, 551, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[39]: text=21.85, bbox=[566, 227, 604, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[40]: text=1.84, bbox=[619, 227, 650, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[41]: text=69.8, bbox=[665, 227, 697, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[42]: text=23.23, bbox=[711, 227, 748, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[43]: text=1.60, bbox=[764, 227, 795, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[44]: text=68.4, bbox=[810, 227, 841, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[45]: text=20.23, bbox=[855, 227, 892, 240]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[46]: text=FEV 1 % FVC, bbox=[128, 240, 212, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[47]: text=[%], bbox=[303, 240, 323, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[48]: text=84.19, bbox=[338, 240, 370, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[49]: text=56.48, bbox=[384, 240, 415, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[50]: text=67.1, bbox=[429, 240, 461, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[51]: text=67.97, bbox=[475, 240, 506, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[52]: text=68.9, bbox=[520, 240, 551, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[53]: text=2.64, bbox=[566, 240, 604, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[54]: text=68.40, bbox=[619, 240, 650, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[55]: text=69.4, bbox=[665, 240, 697, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[56]: text=3.41, bbox=[711, 240, 748, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[57]: text=68.42, bbox=[764, 240, 795, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[58]: text=69.4, bbox=[810, 240, 841, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[59]: text=3.44, bbox=[855, 240, 892, 252]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[60]: text=FEV 1 % VC MAX, bbox=[128, 252, 234, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[61]: text=[%], bbox=[303, 252, 323, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[62]: text=81.88, bbox=[338, 252, 370, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[63]: text=65.26, bbox=[384, 252, 415, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[64]: text=67.6, bbox=[429, 252, 461, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[65]: text=67.97, bbox=[475, 252, 506, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[66]: text=70.8, bbox=[520, 252, 551, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[67]: text=4.91, bbox=[566, 252, 604, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[68]: text=68.40, bbox=[619, 252, 650, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[69]: text=71.3, bbox=[665, 252, 697, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[70]: text=6.70, bbox=[711, 252, 748, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[71]: text=68.42, bbox=[764, 252, 795, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[72]: text=71.4, bbox=[810, 252, 841, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[73]: text=5.73, bbox=[855, 252, 892, 265]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[74]: text=VC MAX, bbox=[128, 265, 174, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[75]: text=[L], bbox=[303, 265, 323, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[76]: text=3.03, bbox=[338, 265, 370, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[77]: text=2.26, bbox=[384, 265, 415, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[78]: text=74.6, bbox=[429, 265, 461, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[79]: text=2.63, bbox=[475, 265, 506, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[80]: text=86.6, bbox=[520, 265, 551, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[81]: text=16.14, bbox=[566, 265, 604, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[82]: text=2.64, bbox=[619, 265, 650, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[83]: text=87.0, bbox=[665, 265, 697, 277]
2026-08-10 12:31:44,561 INFO     29 [qwen-vl-text] coord item[84]: text=16.69, bbox=[711, 265, 748, 277]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[85]: text=2.57, bbox=[764, 265, 795, 277]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[86]: text=84.8, bbox=[810, 265, 841, 277]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[87]: text=13.71, bbox=[855, 265, 892, 277]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[88]: text=PEF, bbox=[128, 277, 152, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[89]: text=[L/s], bbox=[288, 277, 323, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[90]: text=6.28, bbox=[338, 277, 370, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[91]: text=2.66, bbox=[384, 277, 415, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[92]: text=42.4, bbox=[429, 277, 461, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[93]: text=2.90, bbox=[475, 277, 506, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[94]: text=46.2, bbox=[520, 277, 551, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[95]: text=9.17, bbox=[566, 277, 604, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[96]: text=3.37, bbox=[619, 277, 650, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[97]: text=53.7, bbox=[665, 277, 697, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[98]: text=26.79, bbox=[711, 277, 748, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[99]: text=3.42, bbox=[764, 277, 795, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[100]: text=64.6, bbox=[810, 277, 841, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[101]: text=28.64, bbox=[855, 277, 892, 290]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[102]: text=MMEF 75/25, bbox=[128, 290, 203, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[103]: text=[L/s], bbox=[288, 290, 323, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[104]: text=3.57, bbox=[338, 290, 370, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[105]: text=0.61, bbox=[384, 290, 415, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[106]: text=14.4, bbox=[429, 290, 461, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[107]: text=0.67, bbox=[475, 290, 506, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[108]: text=18.8, bbox=[520, 290, 551, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[109]: text=31.03, bbox=[566, 290, 604, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[110]: text=0.73, bbox=[619, 290, 650, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[111]: text=20.4, bbox=[665, 290, 697, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[112]: text=42.01, bbox=[711, 290, 748, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[113]: text=0.69, bbox=[764, 290, 795, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[114]: text=19.4, bbox=[810, 290, 841, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[115]: text=35.02, bbox=[855, 290, 892, 303]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[116]: text=MEF 50, bbox=[128, 303, 174, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[117]: text=[L/s], bbox=[288, 303, 323, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[118]: text=4.01, bbox=[338, 303, 370, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[119]: text=0.68, bbox=[384, 303, 415, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[120]: text=17.0, bbox=[429, 303, 461, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[121]: text=0.90, bbox=[475, 303, 506, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[122]: text=22.5, bbox=[520, 303, 551, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[123]: text=32.75, bbox=[566, 303, 604, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[124]: text=0.89, bbox=[619, 303, 650, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[125]: text=22.1, bbox=[665, 303, 697, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[126]: text=30.15, bbox=[711, 303, 748, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[127]: text=0.88, bbox=[764, 303, 795, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[128]: text=21.9, bbox=[810, 303, 841, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[129]: text=29.17, bbox=[855, 303, 892, 315]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[130]: text=MEF 25, bbox=[128, 315, 174, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[131]: text=[L/s], bbox=[288, 315, 323, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[132]: text=1.79, bbox=[338, 315, 370, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[133]: text=0.19, bbox=[384, 315, 415, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[134]: text=10.5, bbox=[429, 315, 461, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[135]: text=0.27, bbox=[475, 315, 506, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[136]: text=15.2, bbox=[520, 315, 551, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[137]: text=44.16, bbox=[566, 315, 604, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[138]: text=0.33, bbox=[619, 315, 650, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[139]: text=18.7, bbox=[665, 315, 697, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[140]: text=77.66, bbox=[711, 315, 748, 328]
2026-08-10 12:31:44,562 INFO     29 [qwen-vl-text] coord item[141]: text=0.31, bbox=[764, 315, 795, 328]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[142]: text=17.6, bbox=[810, 315, 841, 328]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[143]: text=66.49, bbox=[855, 315, 892, 328]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[144]: text=FET, bbox=[128, 328, 152, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[145]: text=[s], bbox=[303, 328, 323, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[146]: text=7.63, bbox=[384, 328, 415, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[147]: text=8.01, bbox=[475, 328, 506, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[148]: text=4.99, bbox=[571, 328, 604, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[149]: text=7.79, bbox=[619, 328, 650, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[150]: text=2.14, bbox=[717, 328, 748, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[151]: text=7.43, bbox=[764, 328, 795, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[152]: text=-2.60, bbox=[855, 328, 892, 341]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[153]: text=V backextrapolation ex [L], bbox=[128, 341, 323, 354]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[154]: text=0.05, bbox=[384, 341, 415, 354]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[155]: text=0.04, bbox=[475, 341, 506, 354]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[156]: text=-11.67, bbox=[556, 341, 604, 354]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[157]: text=0.04, bbox=[619, 341, 650, 354]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[158]: text=-18.64, bbox=[704, 341, 748, 354]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[159]: text=0.04, bbox=[764, 341, 795, 354]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[160]: text=-13.51, bbox=[847, 341, 892, 354]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[161]: text=PIF, bbox=[128, 354, 152, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[162]: text=[L/s], bbox=[288, 354, 323, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[163]: text=3.04, bbox=[384, 354, 415, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[164]: text=3.37, bbox=[475, 354, 506, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[165]: text=10.91, bbox=[566, 354, 604, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[166]: text=3.51, bbox=[619, 354, 650, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[167]: text=15.70, bbox=[711, 354, 748, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[168]: text=3.60, bbox=[764, 354, 795, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[169]: text=18.67, bbox=[855, 354, 892, 367]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[170]: text=FIV1, bbox=[128, 367, 158, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[171]: text=[L], bbox=[303, 367, 323, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[172]: text=2.21, bbox=[384, 367, 415, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[173]: text=2.56, bbox=[475, 367, 506, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[174]: text=15.71, bbox=[566, 367, 604, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[175]: text=2.56, bbox=[619, 367, 650, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[176]: text=15.66, bbox=[711, 367, 748, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[177]: text=2.50, bbox=[764, 367, 795, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[178]: text=13.09, bbox=[855, 367, 892, 380]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[179]: text=PEF50 % FIF50, bbox=[128, 380, 225, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[180]: text=[%], bbox=[303, 380, 323, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[181]: text=22.86, bbox=[375, 380, 415, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[182]: text=28.15, bbox=[467, 380, 506, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[183]: text=23.14, bbox=[566, 380, 604, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[184]: text=25.36, bbox=[619, 380, 650, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[185]: text=10.95, bbox=[711, 380, 748, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[186]: text=27.28, bbox=[756, 380, 795, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[187]: text=19.33, bbox=[855, 380, 892, 393]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[188]: text=MVV, bbox=[128, 393, 152, 406]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[189]: text=[L/min], bbox=[272, 393, 323, 406]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[190]: text=99.77, bbox=[331, 393, 370, 406]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[191]: text=46.21, bbox=[378, 393, 415, 406]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[192]: text=46.3, bbox=[429, 393, 461, 406]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[193]: text=BF MVV, bbox=[128, 406, 174, 419]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[194]: text=[1/min], bbox=[272, 406, 323, 419]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[195]: text=75.55, bbox=[375, 406, 415, 419]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[196]: text=10, bbox=[216, 457, 227, 467]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[197]: text=Flow [L/s], bbox=[235, 460, 284, 471]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[198]: text=F/V ex, bbox=[328, 460, 361, 470]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[199]: text=1, bbox=[430, 460, 459, 470]
2026-08-10 12:31:44,563 INFO     29 [qwen-vl-text] coord item[200]: text=2, bbox=[430, 470, 459, 480]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[201]: text=3, bbox=[430, 480, 459, 490]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[202]: text=4, bbox=[430, 490, 459, 500]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[203]: text=6, bbox=[220, 508, 229, 517]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[204]: text=8, bbox=[220, 483, 229, 492]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[205]: text=4, bbox=[220, 533, 229, 542]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[206]: text=2, bbox=[220, 558, 229, 567]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[207]: text=0, bbox=[220, 583, 229, 592]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[208]: text=Vol [L], bbox=[367, 574, 402, 585]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[209]: text=1, bbox=[264, 593, 272, 602]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[210]: text=2, bbox=[296, 593, 304, 602]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[211]: text=3, bbox=[330, 593, 338, 602]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[212]: text=4, bbox=[363, 593, 371, 602]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[213]: text=5, bbox=[397, 593, 405, 602]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[214]: text=10, bbox=[216, 712, 227, 721]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[215]: text=F/V In, bbox=[330, 706, 360, 716]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[216]: text=Vol%VCmax, bbox=[516, 503, 574, 513]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[217]: text=0, bbox=[529, 513, 538, 523]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[218]: text=0, bbox=[547, 513, 556, 523]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[219]: text=Vol [L], bbox=[563, 517, 594, 528]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[220]: text=20, bbox=[524, 525, 538, 535]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[221]: text=40, bbox=[524, 537, 538, 547]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[222]: text=60, bbox=[524, 549, 538, 559]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[223]: text=80, bbox=[524, 561, 538, 571]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[224]: text=100, bbox=[519, 573, 538, 583]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[225]: text=2, bbox=[547, 559, 556, 569]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[226]: text=VCmax, bbox=[571, 570, 608, 579]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[227]: text=3, bbox=[547, 581, 556, 591]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[228]: text=4, bbox=[547, 605, 556, 615]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[229]: text=5, bbox=[547, 628, 556, 638]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[230]: text=6, bbox=[547, 651, 556, 661]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[231]: text=Time [s], bbox=[714, 642, 754, 653]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[232]: text=0, bbox=[556, 661, 564, 670]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[233]: text=2, bbox=[603, 661, 611, 670]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[234]: text=4, bbox=[650, 661, 658, 670]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[235]: text=6, bbox=[697, 661, 705, 670]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[236]: text=8, bbox=[743, 661, 751, 670]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[237]: text=10, bbox=[789, 661, 800, 670]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[238]: text=12, bbox=[835, 661, 847, 670]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[239]: text=14, bbox=[882, 661, 894, 670]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[240]: text=意见：, bbox=[107, 735, 151, 749]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[241]: text=1. 中重度阻塞性肺通气功能障碍。, bbox=[107, 750, 325, 763]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[242]: text=2. 支气管舒张试验阳性。, bbox=[107, 763, 265, 775]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[243]: text=(1. 24h内无支气管舒张药物使用史), bbox=[112, 775, 348, 787]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[244]: text=(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml), bbox=[107, 786, 651, 798]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[245]: text=(3. 检查质量：舒张前：A级；舒张后：A级), bbox=[107, 798, 392, 810]
2026-08-10 12:31:44,564 INFO     29 [qwen-vl-text] coord item[246]: text=张四彩, bbox=[816, 875, 877, 894]
2026-08-10 12:31:44,565 INFO     29 [qwen-vl-text] page=17 — 248/248 coords, api_time=64.8s
2026-08-10 12:31:44,565 INFO     29 [qwen-vl-text] new_positions (248):
[[17, 282.625, 333.79499999999996, 59.782, 70.728], [17, 148.75, 170.17, 84.2, 94.304], [17, 148.75, 251.08999999999997, 94.304, 104.408], [17, 148.75, 239.19, 104.408, 115.354], [17, 148.75, 170.17, 115.354, 125.458], [17, 148.75, 170.17, 125.458, 135.56199999999998], [17, 148.75, 282.625, 135.56199999999998, 146.50799999999998], [17, 314.15999999999997, 440.29999999999995, 82.51599999999999, 92.61999999999999], [17, 314.15999999999997, 422.45, 92.61999999999999, 103.566], [17, 314.15999999999997, 418.88, 103.566, 113.67], [17, 314.15999999999997, 335.58, 113.67, 124.616], [17, 314.15999999999997, 353.43, 124.616, 134.72], [17, 396.27, 421.85499999999996, 134.72, 145.666], [17, 201.10999999999999, 220.14999999999998, 158.296, 168.4], [17, 236.81, 274.295, 158.296, 168.4], [17, 291.55, 358.19, 158.296, 168.4], [17, 377.22999999999996, 445.06, 158.296, 168.4], [17, 464.09999999999997, 530.74, 158.296, 168.4], [17, 76.16, 90.44, 181.03, 191.134], [17, 180.285, 192.185, 181.03, 191.134], [17, 201.10999999999999, 220.14999999999998, 181.03, 191.134], [17, 228.48, 246.92499999999998, 181.03, 191.134], [17, 255.255, 274.295, 181.03, 191.134], [17, 282.625, 301.07, 181.03, 191.134], [17, 309.4, 327.84499999999997, 181.03, 191.134], [17, 336.77, 359.38, 181.03, 191.134], [17, 368.305, 386.75, 181.03, 191.134], [17, 395.67499999999995, 414.715, 181.03, 191.134], [17, 423.04499999999996, 445.06, 181.03, 191.134], [17, 454.58, 473.025, 181.03, 191.134], [17, 481.95, 500.395, 181.03, 191.134], [17, 508.72499999999997, 530.74, 181.03, 191.134], [17, 76.16, 98.175, 191.134, 202.07999999999998], [17, 180.285, 192.185, 191.134, 202.07999999999998], [17, 201.10999999999999, 220.14999999999998, 191.134, 202.07999999999998], [17, 228.48, 246.92499999999998, 191.134, 202.07999999999998], [17, 255.255, 274.295, 191.134, 202.07999999999998], [17, 282.625, 301.07, 191.134, 202.07999999999998], [17, 309.4, 327.84499999999997, 191.134, 202.07999999999998], [17, 336.77, 359.38, 191.134, 202.07999999999998], [17, 368.305, 386.75, 191.134, 202.07999999999998], [17, 395.67499999999995, 414.715, 191.134, 202.07999999999998], [17, 423.04499999999996, 445.06, 191.134, 202.07999999999998], [17, 454.58, 473.025, 191.134, 202.07999999999998], [17, 481.95, 500.395, 191.134, 202.07999999999998], [17, 508.72499999999997, 530.74, 191.134, 202.07999999999998], [17, 76.16, 126.14, 202.07999999999998, 212.184], [17, 180.285, 192.185, 202.07999999999998, 212.184], [17, 201.10999999999999, 220.14999999999998, 202.07999999999998, 212.184], [17, 228.48, 246.92499999999998, 202.07999999999998, 212.184], [17, 255.255, 274.295, 202.07999999999998, 212.184], [17, 282.625, 301.07, 202.07999999999998, 212.184], [17, 309.4, 327.84499999999997, 202.07999999999998, 212.184], [17, 336.77, 359.38, 202.07999999999998, 212.184], [17, 368.305, 386.75, 202.07999999999998, 212.184], [17, 395.67499999999995, 414.715, 202.07999999999998, 212.184], [17, 423.04499999999996, 445.06, 202.07999999999998, 212.184], [17, 454.58, 473.025, 202.07999999999998, 212.184], [17, 481.95, 500.395, 202.07999999999998, 212.184], [17, 508.72499999999997, 530.74, 202.07999999999998, 212.184], [17, 76.16, 139.23, 212.184, 223.13], [17, 180.285, 192.185, 212.184, 223.13], [17, 201.10999999999999, 220.14999999999998, 212.184, 223.13], [17, 228.48, 246.92499999999998, 212.184, 223.13], [17, 255.255, 274.295, 212.184, 223.13], [17, 282.625, 301.07, 212.184, 223.13], [17, 309.4, 327.84499999999997, 212.184, 223.13], [17, 336.77, 359.38, 212.184, 223.13], [17, 368.305, 386.75, 212.184, 223.13], [17, 395.67499999999995, 414.715, 212.184, 223.13], [17, 423.04499999999996, 445.06, 212.184, 223.13], [17, 454.58, 473.025, 212.184, 223.13], [17, 481.95, 500.395, 212.184, 223.13], [17, 508.72499999999997, 530.74, 212.184, 223.13], [17, 76.16, 103.53, 223.13, 233.23399999999998], [17, 180.285, 192.185, 223.13, 233.23399999999998], [17, 201.10999999999999, 220.14999999999998, 223.13, 233.23399999999998], [17, 228.48, 246.92499999999998, 223.13, 233.23399999999998], [17, 255.255, 274.295, 223.13, 233.23399999999998], [17, 282.625, 301.07, 223.13, 233.23399999999998], [17, 309.4, 327.84499999999997, 223.13, 233.23399999999998], [17, 336.77, 359.38, 223.13, 233.23399999999998], [17, 368.305, 386.75, 223.13, 233.23399999999998], [17, 395.67499999999995, 414.715, 223.13, 233.23399999999998], [17, 423.04499999999996, 445.06, 223.13, 233.23399999999998], [17, 454.58, 473.025, 223.13, 233.23399999999998], [17, 481.95, 500.395, 223.13, 233.23399999999998], [17, 508.72499999999997, 530.74, 223.13, 233.23399999999998], [17, 76.16, 90.44, 233.23399999999998, 244.17999999999998], [17, 171.35999999999999, 192.185, 233.23399999999998, 244.17999999999998], [17, 201.10999999999999, 220.14999999999998, 233.23399999999998, 244.17999999999998], [17, 228.48, 246.92499999999998, 233.23399999999998, 244.17999999999998], [17, 255.255, 274.295, 233.23399999999998, 244.17999999999998], [17, 282.625, 301.07, 233.23399999999998, 244.17999999999998], [17, 309.4, 327.84499999999997, 233.23399999999998, 244.17999999999998], [17, 336.77, 359.38, 233.23399999999998, 244.17999999999998], [17, 368.305, 386.75, 233.23399999999998, 244.17999999999998], [17, 395.67499999999995, 414.715, 233.23399999999998, 244.17999999999998], [17, 423.04499999999996, 445.06, 233.23399999999998, 244.17999999999998], [17, 454.58, 473.025, 233.23399999999998, 244.17999999999998], [17, 481.95, 500.395, 233.23399999999998, 244.17999999999998], [17, 508.72499999999997, 530.74, 233.23399999999998, 244.17999999999998], [17, 76.16, 120.785, 244.17999999999998, 255.126], [17, 171.35999999999999, 192.185, 244.17999999999998, 255.126], [17, 201.10999999999999, 220.14999999999998, 244.17999999999998, 255.126], [17, 228.48, 246.92499999999998, 244.17999999999998, 255.126], [17, 255.255, 274.295, 244.17999999999998, 255.126], [17, 282.625, 301.07, 244.17999999999998, 255.126], [17, 309.4, 327.84499999999997, 244.17999999999998, 255.126], [17, 336.77, 359.38, 244.17999999999998, 255.126], [17, 368.305, 386.75, 244.17999999999998, 255.126], [17, 395.67499999999995, 414.715, 244.17999999999998, 255.126], [17, 423.04499999999996, 445.06, 244.17999999999998, 255.126], [17, 454.58, 473.025, 244.17999999999998, 255.126], [17, 481.95, 500.395, 244.17999999999998, 255.126], [17, 508.72499999999997, 530.74, 244.17999999999998, 255.126], [17, 76.16, 103.53, 255.126, 265.23], [17, 171.35999999999999, 192.185, 255.126, 265.23], [17, 201.10999999999999, 220.14999999999998, 255.126, 265.23], [17, 228.48, 246.92499999999998, 255.126, 265.23], [17, 255.255, 274.295, 255.126, 265.23], [17, 282.625, 301.07, 255.126, 265.23], [17, 309.4, 327.84499999999997, 255.126, 265.23], [17, 336.77, 359.38, 255.126, 265.23], [17, 368.305, 386.75, 255.126, 265.23], [17, 395.67499999999995, 414.715, 255.126, 265.23], [17, 423.04499999999996, 445.06, 255.126, 265.23], [17, 454.58, 473.025, 255.126, 265.23], [17, 481.95, 500.395, 255.126, 265.23], [17, 508.72499999999997, 530.74, 255.126, 265.23], [17, 76.16, 103.53, 265.23, 276.176], [17, 171.35999999999999, 192.185, 265.23, 276.176], [17, 201.10999999999999, 220.14999999999998, 265.23, 276.176], [17, 228.48, 246.92499999999998, 265.23, 276.176], [17, 255.255, 274.295, 265.23, 276.176], [17, 282.625, 301.07, 265.23, 276.176], [17, 309.4, 327.84499999999997, 265.23, 276.176], [17, 336.77, 359.38, 265.23, 276.176], [17, 368.305, 386.75, 265.23, 276.176], [17, 395.67499999999995, 414.715, 265.23, 276.176], [17, 423.04499999999996, 445.06, 265.23, 276.176], [17, 454.58, 473.025, 265.23, 276.176], [17, 481.95, 500.395, 265.23, 276.176], [17, 508.72499999999997, 530.74, 265.23, 276.176], [17, 76.16, 90.44, 276.176, 287.122], [17, 180.285, 192.185, 276.176, 287.122], [17, 228.48, 246.92499999999998, 276.176, 287.122], [17, 282.625, 301.07, 276.176, 287.122], [17, 339.745, 359.38, 276.176, 287.122], [17, 368.305, 386.75, 276.176, 287.122], [17, 426.615, 445.06, 276.176, 287.122], [17, 454.58, 473.025, 276.176, 287.122], [17, 508.72499999999997, 530.74, 276.176, 287.122], [17, 76.16, 192.185, 287.122, 298.068], [17, 228.48, 246.92499999999998, 287.122, 298.068], [17, 282.625, 301.07, 287.122, 298.068], [17, 330.82, 359.38, 287.122, 298.068], [17, 368.305, 386.75, 287.122, 298.068], [17, 418.88, 445.06, 287.122, 298.068], [17, 454.58, 473.025, 287.122, 298.068], [17, 503.965, 530.74, 287.122, 298.068], [17, 76.16, 90.44, 298.068, 309.014], [17, 171.35999999999999, 192.185, 298.068, 309.014], [17, 228.48, 246.92499999999998, 298.068, 309.014], [17, 282.625, 301.07, 298.068, 309.014], [17, 336.77, 359.38, 298.068, 309.014], [17, 368.305, 386.75, 298.068, 309.014], [17, 423.04499999999996, 445.06, 298.068, 309.014], [17, 454.58, 473.025, 298.068, 309.014], [17, 508.72499999999997, 530.74, 298.068, 309.014], [17, 76.16, 94.00999999999999, 309.014, 319.96], [17, 180.285, 192.185, 309.014, 319.96], [17, 228.48, 246.92499999999998, 309.014, 319.96], [17, 282.625, 301.07, 309.014, 319.96], [17, 336.77, 359.38, 309.014, 319.96], [17, 368.305, 386.75, 309.014, 319.96], [17, 423.04499999999996, 445.06, 309.014, 319.96], [17, 454.58, 473.025, 309.014, 319.96], [17, 508.72499999999997, 530.74, 309.014, 319.96], [17, 76.16, 133.875, 319.96, 330.906], [17, 180.285, 192.185, 319.96, 330.906], [17, 223.125, 246.92499999999998, 319.96, 330.906], [17, 277.865, 301.07, 319.96, 330.906], [17, 336.77, 359.38, 319.96, 330.906], [17, 368.305, 386.75, 319.96, 330.906], [17, 423.04499999999996, 445.06, 319.96, 330.906], [17, 449.82, 473.025, 319.96, 330.906], [17, 508.72499999999997, 530.74, 319.96, 330.906], [17, 76.16, 90.44, 330.906, 341.852], [17, 161.84, 192.185, 330.906, 341.852], [17, 196.945, 220.14999999999998, 330.906, 341.852], [17, 224.91, 246.92499999999998, 330.906, 341.852], [17, 255.255, 274.295, 330.906, 341.852], [17, 76.16, 103.53, 341.852, 352.798], [17, 161.84, 192.185, 341.852, 352.798], [17, 223.125, 246.92499999999998, 341.852, 352.798], [17, 128.51999999999998, 135.065, 384.794, 393.214], [17, 139.825, 168.98, 387.32, 396.582], [17, 195.16, 214.795, 387.32, 395.74], [17, 255.85, 273.10499999999996, 387.32, 395.74], [17, 255.85, 273.10499999999996, 395.74, 404.15999999999997], [17, 255.85, 273.10499999999996, 404.15999999999997, 412.58], [17, 255.85, 273.10499999999996, 412.58, 421.0], [17, 130.9, 136.255, 427.736, 435.31399999999996], [17, 130.9, 136.255, 406.686, 414.264], [17, 130.9, 136.255, 448.786, 456.364], [17, 130.9, 136.255, 469.83599999999996, 477.414], [17, 130.9, 136.255, 490.88599999999997, 498.464], [17, 218.36499999999998, 239.19, 483.308, 492.57], [17, 157.07999999999998, 161.84, 499.306, 506.88399999999996], [17, 176.12, 180.88, 499.306, 506.88399999999996], [17, 196.35, 201.10999999999999, 499.306, 506.88399999999996], [17, 215.98499999999999, 220.74499999999998, 499.306, 506.88399999999996], [17, 236.215, 240.975, 499.306, 506.88399999999996], [17, 128.51999999999998, 135.065, 599.504, 607.082], [17, 196.35, 214.2, 594.452, 602.872], [17, 307.02, 341.53, 423.526, 431.94599999999997], [17, 314.755, 320.11, 431.94599999999997, 440.366], [17, 325.465, 330.82, 431.94599999999997, 440.366], [17, 334.98499999999996, 353.43, 435.31399999999996, 444.57599999999996], [17, 311.78, 320.11, 442.05, 450.46999999999997], [17, 311.78, 320.11, 452.154, 460.574], [17, 311.78, 320.11, 462.258, 470.678], [17, 311.78, 320.11, 472.36199999999997, 480.782], [17, 308.805, 320.11, 482.466, 490.88599999999997], [17, 325.465, 330.82, 470.678, 479.09799999999996], [17, 339.745, 361.76, 479.94, 487.518], [17, 325.465, 330.82, 489.202, 497.62199999999996], [17, 325.465, 330.82, 509.40999999999997, 517.8299999999999], [17, 325.465, 330.82, 528.776, 537.196], [17, 325.465, 330.82, 548.1419999999999, 556.562], [17, 424.83, 448.63, 540.564, 549.826], [17, 330.82, 335.58, 556.562, 564.14], [17, 358.78499999999997, 363.54499999999996, 556.562, 564.14], [17, 386.75, 391.51, 556.562, 564.14], [17, 414.715, 419.47499999999997, 556.562, 564.14], [17, 442.085, 446.84499999999997, 556.562, 564.14], [17, 469.455, 476.0, 556.562, 564.14], [17, 496.825, 503.965, 556.562, 564.14], [17, 524.79, 531.93, 556.562, 564.14], [17, 63.665, 89.845, 618.87, 630.658], [17, 63.665, 193.375, 631.5, 642.446], [17, 63.665, 157.67499999999998, 642.446, 652.55], [17, 66.64, 207.06, 652.55, 662.654], [17, 63.665, 387.34499999999997, 661.812, 671.9159999999999], [17, 63.665, 233.23999999999998, 671.9159999999999, 682.02], [17, 485.52, 521.8149999999999, 736.75, 752.7479999999999], [17, 485.52, 521.8149999999999, 736.75, 752.7479999999999]]
2026-08-10 12:31:44,565 INFO     29 [qwen-vl-text] ═══ DONE ═══ 248 positions, pages=1, time=77.9s
2026-08-10 12:31:44,578 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 12:31:44,579 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:ExaminationReport | outputs={"chunks": "6 items, types={'ExaminationReport': 6}", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:31:44,579 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 12:31:44,580 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:31:44.579+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 29, "failed": 0, "current": {"b3b7aba694b511f1bd9827cf206dfa2d": {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:31:44,586 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:31:44,586 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:31:45,621 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:31:45,628 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 12:31:45,628 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "998 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "3 items, types={'AdmissionRecord': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 3, \"chunks_Medication\": 1}"}
2026-08-10 12:31:45,629 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 12:31:45,630 INFO     29 [ChunkMerger] Merged 14 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 2, 'Extractor:Discharge': 2, 'Extractor:Admission': 3, 'Extractor:ExaminationReport': 6, 'Extractor:Progress': 1} (filtered 4 noise chunks)
2026-08-10 12:31:45,640 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 12:31:45,640 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "14 items, types={'MedicationRecord': 1, 'PrescriptionRecord': 2, 'DischargeRecord': 2, 'AdmissionRecord': 3, 'ExaminationReport': 6}", "name": "YXLA（支气管哮喘）222.pdf"}
2026-08-10 12:31:45,640 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 12:31:45,849 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786364357886, 'update_date': datetime.datetime(2026, 8, 10, 12, 19, 17), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 973813, 'status': '1'}
2026-08-10 12:31:46,155 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=金城大药房
会员号:
积分:112550
本次积分:596.00
名称
规格
数量
厂家
批号
单价
金额
1-布地奈德福莫特罗吸入粉雾剂
320ug:9ug*60吸/支
2.00
阿斯利康制药
PKMR
300.00
596.00
运动员慎用!!!
***重打销售单***
总计数量:2.00
应收:600.00
优惠:4.00
付款:596.00
找零:0.00
销售单号:251210031062
款台号:2
日期:2025-12-10
15:21:53
---
人民医院
H43120200207, 院区: 舊城院区)
基本就诊信息
姓名: 核
医生: 旅
挂号单: 25000448502
医保号: 5200002600000000600637839
付款: 城乡居民基本医疗 费别: 普通
门诊号: 2502240221
社区号:
门诊就诊:呼吸内科门诊,2025-09-30 14:50
医嘱
报告
已作废
全部
处方
其他
生效时间
内容
用法
2025-09-30
孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/
睡前口服,每天一次,共30天
14:51
盒,共10盒,每次10mg
---
基本就诊信息
姓名：杨
医生：
挂号单：26000068319
医保号：52000026000000006006378395
付款：城乡居民基本医疗 费别：普通
门诊号：2502240221
社区号：
门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04
医嘱|报告|
已作废|全部|处方|其他
生效时间
内容
用法
2026-02-09
肺功能全套+支气管舒张试验,共1次
2026-02-09
(基)硫酸沙丁胺醇吸入气雾剂 (山东)
吸入,一次,共1天
11:08
100ug*200揿/瓶,共1瓶,每次400ug
2026-02-09
呼出气一氧化氮测定,共1次
2026-02-09
沙美特罗替卡松粉吸入剂(法国GLAXO)
吸入,每天二次,共1天
12.33
50ug/500ug*60吸/瓶,共1瓶,每次50ug
---
HUAIHUA CENTRAL HOSPITAL
怀化市肿瘤医院
姓名：
性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：
221028180
3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总
神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓
浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经
(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞
<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌
(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支
持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司
特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前
好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。
出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发
热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，
BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。
心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。
出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧
段结节（LU-RADS 2类）。
出院医嘱：
1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生
活习惯，增强体质，适当运动，加强营养；
2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复
查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；
3.出院后继续服用中药。
4.出院带药：
舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱
口，根据动态复查肺功能结果，调整用药）
祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次
抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次
5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；
6.如有不适，随时医院就诊，我科随诊。
科室护士办公室电话：0745-2329117。主管医师电话：13789357317
医师签名：主治医师
zz1028180
---
221028180
第2次入院记录
姓名：
性别：女
年龄：37岁
婚姻：已婚
入院时间：2025-07-11 08:57
入院方式：步行
主诉：反复胸闷、气促8年，加重1月。
现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。
出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。
既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。
病史陈述者签名：
体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。
出生地：贵州省天柱县
民族：苗族
职业：农民
住址：贵州省天柱县远口镇大祥村白蜡树脚组
记录时间：2025-07-11 14:36
CS 扫描全能王
3亿人都在用的扫描App
出院记录
入院时间：2025-02-24 12:22
出院时间：2025-03-01 10:00
住院天数：5天
记录时间：2025-02-28 20:39
入院诊断：胸闷、气促查因：支气管哮喘可能性大
入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。
体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸
氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89
次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。
诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C
+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、
肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体
测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。
心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1
0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范
围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO
2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球
菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、
两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，
LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能
结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、
抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者
及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。
出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶
心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，
BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心
率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。
出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：
功能性消化不良？反流性食管炎？其他。
出院医嘱：
（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺
激性烟雾及吸入二手烟；
姓名：
性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：
220999152
(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；
(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；
(4) 继续用药：
舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服
布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入
(吸入后漱口，根据动态复查肺功能结果，调整用药)
抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服
止咳祛痰：润肺膏 每次15g 每天2次，口服
调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服
(5) 如有不适，随时医院就诊，我科随诊。
科室电话：0745-2329117 主管医师电话：13789357317
医师签名：主治医师：
---
37岁 科室：呼吸与危重症医学科 床号：42 住院号：
出院记录
入院时间：2025-07-11 08:57
出院时间：2025-07-22 15:00
住院天数：11天
记录时间：2025-07-21 16:14
入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；
4.腹胀查因：功能性消化不良？反流性食管炎？其他。
入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T
36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面
容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及
少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，
无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，
LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功
能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散
功能在正常范围；肺总量在正常范围，残气量、残总比增高。
诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分
压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中
性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；
尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红
细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；
电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C
蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链
DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生
虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：
胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.
支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气
功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、
MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重
减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳
性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，
绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），
2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：
怀化市中心医院
HUAIHUA CENTRAL HOSPITAL
怀化市肿瘤医院
姓名：
性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：
221028180
[心前区无隆起]，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，
[各瓣膜听诊区未闻及杂音]。腹部平坦，[腹壁静脉无曲张]，无胃肠型和蠕动波，[全
腹柔软]，[腹部无压痛]，[腹部无反跳痛]，[肝脾肋下未扪及]，Murphy征(-)，叩
诊呈[鼓音]，移动性浊音(-)。肠鸣音正常，[无气过水声]。外生殖器[未查]，肛门
直肠[正常]。脊柱四肢[正常]。 双下肢无浮肿，生理反射正常，病理反射阴性。
辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复
查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占
预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量
在正常范围，残气量、残总比增高。
入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？
3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其
他。
主治医师：
副主任医师：
---
221028180
第2次入院记录
姓名：
出生地：贵州省天柱县
性别：女
民族：苗族
年龄：37岁
职业：农民
婚姻：已婚
住址：贵
入院时间：2025-07-11 08:57
记录时间：2025-07-11 14:36
入院方式：步行
主诉：反复胸闷、气促8年，加重1月。
现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。
出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。
既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。
病史陈述者签名：
体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。
眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，
甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。
叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。
家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。
病史陈述者签名：
体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋
姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：
220999152
下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:
辅助检查结果：无
入院初步诊断：胸闷、气促查因：支气管哮喘可能性大
主治医师：
主任医师：
---
姓名：
性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：
220999152
入院记录
姓名：
出生地：贵州省天柱县远口镇大样村白蜡树脚组
性别：女
民族：苗族
年龄：37岁
职业：自由职业者
婚姻：已婚
住址：贵
入院时间：2025-02-24 12:22
记录时间：2025-02-24 14:28
入院方式：步行
主诉：反复胸闷、气促8年，加重半年。
现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳
嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐
渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，
无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，
约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，
门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期
体重无改变。
既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病
史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。
个人史：[出生于原籍，常住本地，无粉尘放射性物质接触史，否认疫区居住
史]，[无吸烟史，无饮酒史，否认性病及冶游史]。
月经史：162~32025/2/21，月经周期规律，色红，量少，无痛经。
婚育史：24岁结婚，育有1子1女，配偶及子女体健。
家族史：家族中无同类病人。直系亲属体健。无遗传倾向疾患。
病史陈述者签名：
体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸
氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜
色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，
巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常
分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-
颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤
正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦
---
报告时间: 2025-02-24
怀化市肿瘤医院
怀化市第二人民医院
鹤城院区
湖南HR
CT影像诊断报告单
ID: 86562633
检查号: CT00525514
姓名:
性别: 女
年龄: 37岁
住院号: 220999152
床号: 46
申请科室: 呼吸与危重症医学科
申请医生: 易莹
检查日期: 2025.02.25
报告日期: 2025.02.25 09:45:16
检查项目: CT成套:胸部(平扫(三维重建))
检查所见:
右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见
条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主
要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。
意见:
1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。
2. 右肺中叶少许慢性炎症。
---
怀化市中心医院
HUAIHUA CENTRAL HOSPITAL
怀化市肿瘤医院
湖南HR
CT影像诊断报告单
ID: 93717786
检查号: CT00568277
姓名:
性别: 女
年龄: 37岁
住院号: 221028180
床号: 42
申请科室: 呼吸与危重症医学科
申请医生:
检查日期: 2025.07.11
报告日期: 2025.07.11 16:08:56
检查项目: CT成套胸部平扫(三维重建)
检查所见:
与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。
右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部
分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。
意见:
1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。
2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。
---
姓名：
年龄：38岁
性别：女
科别：
保险：
预计值模式：Standard-new
常规通气报告
测试号：2026020917
身高：165 cm
体重：60 kg
备注：
联系电话：
操作者：蒋细萍
Pred
Bst % (B/Pd
A1
A2
A3
FVC
[L]
2.99
2.21
74.02
2.21
2.12
2.09
FEV 1
[L]
2.67
1.26
48.56
1.26
1.13
1.18
FEV6
[L]
2.12
2.12
2.05
2.02
FEV 1 % FVC
[%]
84.19
56.48
67.09
56.48
53.33
56.67
FEV 1 % VC MAX
[%]
81.88
55.26
67.48
55.26
50.10
52.31
VC MAX
[L]
3.03
2.26
74.60
PEF
[L/s]
6.28
2.66
42.36
2.66
2.58
2.43
MMEF 75/25
[L/s]
3.57
0.51
14.35
0.51
0.49
0.41
MEF 75
[L/s]
5.64
1.47
26.14
1.47
0.80
1.21
MEF 50
[L/s]
4.01
0.68
16.97
0.68
0.72
0.57
MEF 25
[L/s]
1.79
0.19
10.52
0.19
0.18
0.15
V backextrapolation ex
[L]
0.05
0.05
0.03
0.04
V backextrapol. % FVC
[%]
2.07
2.07
1.50
1.81
FET
[s]
7.63
7.63
7.35
7.55
FEF 200-1200
[L/s]
1.19
1.19
0.98
1.05
FVC IN
[L]
3.03
2.26
74.60
2.26
2.15
2.13
FIV1
[L]
2.21
2.21
2.12
2.09
FIV1 % FVC
[%]
97.79
97.79
98.68
98.05
FEF50 % FIF50
[%]
22.86
22.86
25.05
19.46
PIF
[L/s]
3.04
3.04
3.04
2.99
MVV
[L/min]
99.77
46.21
46.32
46.21
BF MVV
[1/min]
75.55
75.55
意见：
1. 重度混合性肺通气功能障碍。
2. 最大分钟通气量（MVV）：显著减退。
Date
20/2/00
Timo
11:48:04上午
Flow [L/s]
F/V ex
Vol [L]
Vol%VCmax
VCmax
Time [s]
Vol [L]
Time [s]
F/V in
10
8
6
4
2
0
1
2
3
4
5
10
8
6
4
2
0
100
80
60
40
20
0
2
4
6
8
10
12
1
0
2
4
6
8
10
12
1
0
2
4
6
8
10
12
1
张
---
CS 扫描全能王
3亿人都在用的扫描App
呼出气一氧化氮检测报告单
姓名：杨
性别：女
出生日期：1987-12-01
年龄：38岁2个月
ID号：
测试日期：2026-02-09
科室：呼吸科门诊
医生：张
问卷调查：
激素：正在使用口 三天内未使用口 从未使用口
抗生素：正在使用口 三天内未使用口 从未使用口
吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口
症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：
病史：过敏史口 其他：
注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。
检测信息：
项目：在线
呼气压力：8.8cmH2O 呼气流速：45ml/s
呼气时间：5s 温度：21.8℃ 湿度：38.9%
呼气浓度：10、11、12、11、11、11、10、10、10、
10、10、10、11、10、11、11、11、11ppb
项目：小气道
呼气压力：11.3cmH2O 呼气流速：202ml/s
呼气时间：3s 温度：22.0℃ 湿度：39.0%
呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0
0.0、0.0、0.0、0.0、1.0、1.0、1.0、
1.0、1.0、0.0、0.0、0.0ppb
参考意义：
(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)
测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型
FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症
25 - 50ppb 20 - 35ppb* 混合型气道炎症
> 50ppb > 35ppb* 嗜酸性气道炎症
CaNO ≤ 5ppb ≤ 3ppb 小气道正常
> 5ppb > 3ppb 小气道炎症
FaNO < 125ppb 考虑Kartagener综合征、PCD、CF或
重度的鼻窦炎或鼻息肉
125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉
250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断
> 500ppb 考虑过敏性鼻炎
(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)
此结果仅对本次呼气检测负责
测定结果：FeNO 60:11ppb CaNO :1.0ppb
操作员：蒋细萍
张日石
---
一口气法弥散功能报告
姓名：
年龄：38岁
性别：女
科别：
保险：
预计值模式：Standard-now
测试号：2026020917
身高：155 cm
体重：60 kg
备注：
联系电话：
操作者：蒋细萍
CO (%)
Volume [L]
CH4 [%]
0.25
0.20
0.15
0.10
0.05
0.00
Time [s]
Pred
Best
Best%
Act1
DLCO SB
[mmol/min/kPa]
8.08
9.45
116.9
9.45
DLCO/VA
[mmol/min/kPa/L]
1.82
2.38
130.8
2.38
VA
[L]
4.29
3.97
92.5
3.97
VC IN
[L]
3.03
2.26
74.6
Discard vol
[L]
1.00
Sample vol
[L]
0.53
ERV
[L]
1.10
IRV
[L]
IC
[L]
1.93
VT
[L]
0.43
VC MAX
[L]
3.03
2.26
74.6
TLC-SB
[L]
4.44
4.10
92.4
4.10
RV-SB
[L]
1.41
2.18
154.5
2.18
RV%TLC-SB
[%]
31.88
53.26
167.1
53.26
FRC-SB
[L]
2.51
2.39
95.2
2.39
FRC%TLC-SB
[%]
51.18
58.28
113.9
58.28
测试日期
26/2/0
意见：
1.弥散功能在正常范围。
2.残气量、残总比增高，肺总量在正常范围。
张
---
肺功能试验报告
姓名：
年龄：38岁
性别：女
科别：
保险：
预计值模式：Standard-new
测试号：2026020017
身高：166 cm
体重：60 kg
备注：
联系电话：
操作者：蒋细萍
Pred
A1 A1/Pd
P1 A2/Pd chg%l
P2 A3/Pd chg%2
P3 A4/Pd chg%3
FVC
[L]
2.99
2.21
74.0
2.63
87.9
18.72
2.04
88.2
19.17
2.67
86.0
16.23
FEV 1
[L]
2.67
1.25
48.6
1.62
69.2
21.85
1.84
69.8
23.23
1.60
68.4
20.23
FEV 1 % FVC
[%]
84.19
56.48
67.1
67.97
68.9
2.64
68.40
69.4
3.41
68.42
69.4
3.44
FEV 1 % VC MAX
[%]
81.88
65.26
67.6
67.97
70.8
4.91
68.40
71.3
6.70
68.42
71.4
5.73
VC MAX
[L]
3.03
2.26
74.6
2.63
86.6
16.14
2.64
87.0
16.69
2.57
84.8
13.71
PEF
[L/s]
6.28
2.66
42.4
2.90
46.2
9.17
3.37
53.7
26.79
3.42
64.6
28.64
MMEF 75/25
[L/s]
3.57
0.61
14.4
0.67
18.8
31.03
0.73
20.4
42.01
0.69
19.4
35.02
MEF 50
[L/s]
4.01
0.68
17.0
0.90
22.5
32.75
0.89
22.1
30.15
0.88
21.9
29.17
MEF 25
[L/s]
1.79
0.19
10.5
0.27
15.2
44.16
0.33
18.7
77.66
0.31
17.6
66.49
FET
[s]
7.63
8.01
4.99
7.79
2.14
7.43
-2.60
V backextrapolation ex [L]
0.05
0.04
-11.67
0.04
-18.64
0.04
-13.51
PIF
[L/s]
3.04
3.37
10.91
3.51
15.70
3.60
18.67
FIV1
[L]
2.21
2.56
15.71
2.56
15.66
2.50
13.09
PEF50 % FIF50
[%]
22.86
28.15
23.14
25.36
10.95
27.28
19.33
MVV
[L/min]
99.77
46.21
46.3
BF MVV
[1/min]
75.55
10
Flow [L/s]
F/V ex
1
2
3
4
6
8
4
2
0
Vol [L]
1
2
3
4
5
10
F/V In
Vol%VCmax
0
0
Vol [L]
20
40
60
80
100
1
2
VCmax
3
4
5
6
Time [s]
0
2
4
6
8
10
12
14
意见：
1. 中重度阻塞性肺通气功能障碍。
2. 支气管舒张试验阳性。
(1. 24h内无支气管舒张药物使用史)
(2. 吸入万托林气雾剂400ug15分钟后，FEV1和FVC上升≥12%，绝对值增加≥200ml)
(3. 检查质量：舒张前：A级；舒张后：A级)
张四彩
2026-08-10 12:31:47,132 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 12:31:47,132 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "14 items, types={'MedicationRecord': 1, 'PrescriptionRecord': 2, 'DischargeRecord': 2, 'AdmissionRecord': 3, 'ExaminationReport': 6}", "name": "YXLA（支气管哮喘）222.pdf", "embedding_token_consumption": 11790}
2026-08-10 12:31:47,132 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 12:31:47,428 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 12:31:47,428 INFO     29 [Trace] task=b3b7aba6 | doc=YXLA（支气管哮喘）222.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":14,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,436 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,437 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,437 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,437 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:31:47,442 INFO     29 set_progress(b3b7aba694b511f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 12:31:47 [DOC Engine]:
Start to index...
2026-08-10 12:31:47,458 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.012s]
2026-08-10 12:31:47,462 INFO     29 set_progress(b3b7aba694b511f1bd9827cf206dfa2d), progress: 0.8071428571428572, progress_msg: 
2026-08-10 12:31:47,479 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 12:31:47,502 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-10 12:31:47,513 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 12:31:47,520 INFO     29 set_progress(b3b7aba694b511f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 12:31:47 Indexing done (0.08s). Task done (719.71s)
2026-08-10 12:31:47,523 INFO     29 [Done], chunks(14), token(11790), elapsed:719.71
2026-08-10 12:31:47,774 INFO     29 handle_task done for task {"id": "b3b7aba694b511f1bd9827cf206dfa2d", "doc_id": "b37cdb2a94b511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480000, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786364355037, "task_type": "dataflow", "root_trace_id": "5310840a043f4d94857495aa3a197433", "root_traceparent": "00-5310840a043f4d94857495aa3a197433-db81509ba0072b75-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
