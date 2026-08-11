# 基准结果：MARO-四川省人民.pdf

## 基本信息

- 文件：`MARO-四川省人民.pdf`
- 大小：6032.8 KB
- PDF 总页数：14
- doc_id：`4e16a27e94b111f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T19:47:45  完成时间：2026-08-10T19:56:04  耗时：498.6s
- progress_msg：`11:56:01 Indexing done (0.10s). Task done (473.14s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | cfbda2b1 | 1 | 1-1 | 门诊 就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁 闭 |
| 2 | bad8dd7c | 1 | 2-2 | 65753497 就诊类型: 门诊 就诊时间: 2026-02-24 21:35 |
| 3 | 15810e6e | 1 | 3-3 | 四川省医学科学院四川省人民医院 互联网门诊病历 姓名: 性别:女 年龄:62 门 |
| 4 | d79f4c62 | 1 | 4-4 | 生日: 196****16 过敏史: 否 62岁 身份证号: 510****** |
| 5 | ba44fcae | 1 | 5-5 | 四川省医学科学院四川省人民医院 互联网门诊病历 姓名 性别：女 年龄：62 门诊 |
| 6 | 8c8cacc2 | 1 | 6-6 | 流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29  |
| 7 | e2118e49 | 1 | 9-9 | 就诊类型: 门诊 就诊时间: 2025-12-09 17:00:36 接诊年龄: |
| 8 | 193dc0ae | 1 | 10-10 | 出生日期: 196******16 过敏史: 无 年龄: 62岁 身份证号: 5 |
| 9 | ffa5de1b | 4 | 11-14 | 四川省医学科学院·四川省人民医院 门诊病历 姓名： 性别：女 年龄：60岁 门诊 |
| 10 | 8ce9fec0 | 1 | 7-7 | <table><tr><td>*白细胞计数</td><td>WBC</td><t |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：13
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：13 / 14；缺失页：`[8]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 13/14 页，缺失 [8]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 6 | 0 | 6 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 3 | 3 | 3 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 6, "PrescriptionRecord": 3, "LabReport": 1}`
- ChunkMerger：`{"found": true, "merged": 10, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 6, "Extractor:Medication": 1, "Extractor:Prescription": 3, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 11:56:00,305 INFO     29 [ChunkMerger] Merged 10 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 6, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 11:47:49,957 INFO     29 handle_task begin for task {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:47:50,182 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 11:47:50,304 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 11:47:50,321 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:47:50,321 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 11:47:50,321 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 11:47:50,326 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 11:47:50,326 INFO     29 ============================================================
2026-08-10 11:47:50,326 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 11:47:50,326 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 11:47:50,326 INFO     29 ============================================================
2026-08-10 11:47:50,326 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 11:47:50,326 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 11:47:50,327 INFO     29 No torch found.
2026-08-10 11:47:53,228 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=14
2026-08-10 11:47:53,521 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=996376, prompt_len=764
2026-08-10 11:48:02,419 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:48:02,420 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 11:48:02,428 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=996376, prompt_len=401
2026-08-10 11:48:05,659 INFO     29 [qwen-vl-parser] text API response (len=480):
["门诊", "就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁", "闭环", "病历详情", "病历文档", "四川省醫學科學院·四川省人民醫院", "门诊病历", "姓名:", "别: 女年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109", "住址: 四川省成都******* 联系电话: 133****6101 挂号流水号: 66150482", "复诊记录", "记录时间: 2026-03-10 19:04", "主诉:", "支气管哮喘复诊", "简要病史:", "支气管哮喘复诊, 目前哮喘症状稳定", "既往病史:", "阴性", "过敏史:", "阴性", "流行病学", "史:", "阴性", "体格检查:", "阴性", "门诊诊断:", "支气管哮喘", "处置:", "继续使用舒利迭控制哮喘", "婚姻史: 月经史:", "是否下转: 否, 是否外伤: 否, 是否美容: 否", "医师签名:", "燕海荣", "共1页, 第1页", "0", "异常项", "1"]
2026-08-10 11:48:05,660 INFO     29 [qwen-vl-parser] page=1 text: 37 lines (bbox 0-36)
2026-08-10 11:48:05,660 INFO     29 [qwen-vl-parser] page=1 text: 37 sections
2026-08-10 11:48:05,991 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233213, prompt_len=764
2026-08-10 11:48:13,654 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:48:13,655 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 11:48:13,674 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233213, prompt_len=401
2026-08-10 11:48:17,385 INFO     29 [qwen-vl-parser] text API response (len=574):
["view/#/webMedicalRecord", "院营养诊疗系统", "DoCare", "美康智营药学服务...", "单病种数据上报", "PMS医院绩效管理...", "POCT信息管理系统", "联众数字化病案浏...", "出生日期: 196****16", "过敏史: 无", "年龄: 62岁", "身份证号: 510***********045", "更多", "65753497", "就诊类型: 门诊", "就诊时间: 2026-02-24 21:35:00", "接诊年龄: 62岁", "闭环", "历web版", "2026年3月12日 12:21:13", "姓名:", "性别: 女", "年龄: 63岁", "门诊卡号: 0009922109", "科室: 互联网医院门诊", "主诊断: 支气管哮喘", "门诊医嘱", "门诊医嘱", "开立时间", "开立医生", "▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入", "2026/02/24 22:19", "燕海英", "集采7*甲泼尼龙片(兴)(基) 1盒 20mg 每日1次 口服", "2026/02/25 09:00", "燕海英", "CS 扫描全能王", "3亿人都在用的扫描App", "2"]
2026-08-10 11:48:17,385 INFO     29 [qwen-vl-parser] page=2 text: 39 lines (bbox 37-75)
2026-08-10 11:48:17,385 INFO     29 [qwen-vl-parser] page=2 text: 39 sections
2026-08-10 11:48:17,678 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1130678, prompt_len=764
2026-08-10 11:48:18,684 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:48:18.683+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:48:25,305 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:48:25,306 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 11:48:25,328 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1130678, prompt_len=401
2026-08-10 11:48:27,731 INFO     29 [qwen-vl-parser] text API response (len=344):
["四川省医学科学院四川省人民医院", "互联网门诊病历", "姓名:", "性别:女", "年龄:62", "门诊科室:互联网医院门诊", "门诊病历号:0009922109", "工作单位或住址:四川省成都市邛崃市临邛街道", "联系电话:", "复诊记录", "记录时间:2026-02-24 22:18", "主诉:咳嗽,喘息,加重3天", "简要病史:咳嗽,喘息,加重3天,3天前受凉后出现喘息加重,无发热。", "既往病史:", "过敏史:", "流行病学史:无", "体格检查:无", "门诊诊断:支气管哮喘,支气管哮喘急性发作", "处理意见:无", "是否下转:否", "是否外伤:否", "是否美容:否", "是否体检:否", "燕海荣", "医师签名:", "3"]
2026-08-10 11:48:27,731 INFO     29 [qwen-vl-parser] page=3 text: 26 lines (bbox 76-101)
2026-08-10 11:48:27,731 INFO     29 [qwen-vl-parser] page=3 text: 26 sections
2026-08-10 11:48:28,092 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1218603, prompt_len=764
2026-08-10 11:48:36,880 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:48:36,881 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 11:48:36,892 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1218603, prompt_len=401
2026-08-10 11:48:40,244 INFO     29 [qwen-vl-parser] text API response (len=519):
["#/webMedicalRecord", "诊疗系统", "DoCare", "美康智慧药学服务...", "单病种数据上报", "PMS医院绩效管理...", "POCT信息管理系统", "联众数字化病案浏...", "生日: 196****16", "过敏史: 否", "62岁", "身份证号: 510***********045", "更多", "005", "就诊类型: 门诊", "就诊时间: 2026-01-23 13:19:40", "接诊年龄: 62岁", "闭环", "eb版", "2026年3月12日 12:22:03 注销", "姓名:", "性别: 女", "年龄: 63岁", "门诊卡号: 0009922109", "科室: 互联网医院门诊", "主诊断: 支气管哮喘", "门诊医嘱", "门诊医嘱", "开立时间", "开立医生", "259698508 ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入", "2026/01/23 13:48", "燕海英", "0", "异常项", "CS", "扫描全能王", "3亿人都在用的扫描App", "4"]
2026-08-10 11:48:40,245 INFO     29 [qwen-vl-parser] page=4 text: 39 lines (bbox 102-140)
2026-08-10 11:48:40,245 INFO     29 [qwen-vl-parser] page=4 text: 39 sections
2026-08-10 11:48:40,526 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1004098, prompt_len=764
2026-08-10 11:48:48,266 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:48:48,267 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 11:48:48,279 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1004098, prompt_len=401
2026-08-10 11:48:49,838 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:48:49.835+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:48:50,430 INFO     29 [qwen-vl-parser] text API response (len=305):
["四川省医学科学院四川省人民医院", "互联网门诊病历", "姓名", "性别：女", "年龄：62", "门诊科室：互联网医院门诊", "门诊病历号：0009922109", "工作单位或住址：四川省成都市邛崃市临邛街道", "联系电话：", "复诊记录", "记录时间：2026-01-23 13:20", "主诉：支气管哮喘", "简要病史：支气管哮喘", "既往病史：", "过敏史：", "流行病学史：无", "体格检查：无", "门诊诊断：支气管哮喘", "处理意见：无", "是否下转：否", "是否外伤：否", "是否美容：否", "是否体检：否", "燕海荣", "医师签名：", "5"]
2026-08-10 11:48:50,431 INFO     29 [qwen-vl-parser] page=5 text: 26 lines (bbox 141-166)
2026-08-10 11:48:50,431 INFO     29 [qwen-vl-parser] page=5 text: 26 sections
2026-08-10 11:48:50,715 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1035148, prompt_len=764
2026-08-10 11:48:57,877 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:48:57,877 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 11:48:57,900 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1035148, prompt_len=401
2026-08-10 11:49:02,416 INFO     29 [qwen-vl-parser] text API response (len=630):
["流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29 10:01:20 接诊年龄: 62岁", "闭环", "病历详情", "病历文档", "四川省醫學科學院·四川省人民醫院", "门诊病历", "姓名:", "性别: 女 年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109", "住址: 四川省成都******** 联系电话: 133****6101 挂号流水号: 64363836", "复诊记录", "记录时间: 2025-12-29 10:38", "主诉: 发作性喘息。", "简要病史: 哮喘复诊, 1周前吼喘一次持续3天, 自觉呼吸困难", "既往病史: 焦虑型抑郁症", "过敏史: 有过敏源", "流行病学", "史: /", "体格检查: 指尖氧饱和度95%, 心率78次/分", "门诊诊断: 哮喘急性发作、失眠", "处置: 血eos 0.4", "集采7*甲泼尼龙片(兴)(基)20mg/次 口服 每日1次 6天", "▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500)1泡/次 经口吸入 每日2次 31天", "阿育吠陀片(精2)(基)0.4mg/次 口服 每晚1次 20天", "血细胞分析(CBC+DIFF)", "婚姻史: 月经史:", "是否下转: 否, 是否外伤: 否, 是否美容: 否", "医师签名: 燕海荣", "共2页, 第2页", "6"]
2026-08-10 11:49:02,416 INFO     29 [qwen-vl-parser] page=6 text: 29 lines (bbox 167-195)
2026-08-10 11:49:02,417 INFO     29 [qwen-vl-parser] page=6 text: 29 sections
2026-08-10 11:49:03,322 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2512192, prompt_len=764
2026-08-10 11:49:11,214 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 11:49:11,215 INFO     29 [qwen-vl-parser] page=7 classify=table report_date=None
2026-08-10 11:49:11,240 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2512192, prompt_len=756
2026-08-10 11:49:19,804 INFO     29 [qwen-vl-parser] table API response (len=1595):
\begin{tabular}{l l l l l l l}
\hline
\multicolumn{2}{c}{姓名(Name):} & \multicolumn{2}{l}{病历号(Case No): 0009922109} & \multicolumn{3}{l}{病区(Section): 呼吸与危重症医学科门诊} \\
\multicolumn{2}{c}{性别(Gender): 女} & \multicolumn{2}{l}{条码号(Barcode): 1057544035} & \multicolumn{3}{l}{床号(Bed No):} \\
\multicolumn{2}{c}{年龄(Age): 62 岁} & \multicolumn{2}{l}{检测号(Test No): 311187} & \multicolumn{3}{l}{标本(Specimen): 全血} \\
\multicolumn{2}{c}{实验室(Lab): 临检组} & \multicolumn{5}{l}{诊断(Diagnosis): 哮喘急性发作} \\
\hline
\multicolumn{2}{c}{项目名称} & \multicolumn{2}{c}{缩写} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{单位} & \multicolumn{2}{c}{参考区间} \\
\hline
1 & *白细胞计数 & WBC & 6.65 & $10^9$/L & 3.50--9.50 \\
2 & 中性粒细胞数 & NEUT\# & 4.47 & $10^9$/L & 1.80--6.30 \\
3 & 淋巴细胞数 & LYMPH\# & 1.41 & $10^9$/L & 1.10--3.20 \\
4 & 单核细胞数 & MONO\# & 0.33 & $10^9$/L & 0.10--0.60 \\
5 & 嗜酸性粒细胞数 & EOS\# & 0.40 & $10^9$/L & 0.02--0.52 \\
6 & 嗜碱性粒细胞数 & BASO\# & 0.04 & $10^9$/L & 0.00--0.06 \\
7 & 中性粒细胞率 & NEUT\% & 67.2 & \% & 40.0--75.0 \\
8 & 淋巴细胞率 & LYMPH\% & 21.2 & \% & 20.0--50.0 \\
9 & 单核细胞率 & MONO\% & 5.0 & \% & 3.0--10.0 \\
10 & 嗜酸性粒细胞率 & EOS\% & 6.0 & \% & 0.4--8.0 \\
11 & 嗜碱性粒细胞率 & BASO\% & 0.6 & \% & 0--1.0 \\
12 & *红细胞计数 & RBC & 4.66 & $10^{12}$/L & 3.80--5.10 \\
13 & *血红蛋白量 & HGB & 131 & g/L & 115--150 \\
14 & *红细胞比积 & HCT & 42.5 & \% & 35.0--45.0 \\
15 & *平均红细胞体积 & MCV & 91.1 & fL & 82.0--100.0 \\
16 & *平均红细胞血红蛋白量 & MCH & 28.1 & pg & 27.0--34.0 \\
17 & *平均红细胞血红蛋白浓度 & MCHC & 308 & g/L & 316--354 \\
18 & 红细胞分布宽度 & RDW-SD & 48.5 & fL & 38.4--47.8 \\
19 & *血小板计数 & PLT & 178 & $10^9$/L & 101--320 \\
\hline
\end{tabular}
2026-08-10 11:49:19,806 INFO     29 [qwen-vl-parser] page=7 table: 30 LaTeX lines (bbox 196-225)
2026-08-10 11:49:19,807 INFO     29 [qwen-vl-parser] page=7 table: 30 sections
2026-08-10 11:49:20,173 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1813785, prompt_len=764
2026-08-10 11:49:20,983 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:49:20.980+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:49:27,883 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-12-29"
}
```
2026-08-10 11:49:27,883 INFO     29 [qwen-vl-parser] page=8 classify=table report_date=2025-12-29
2026-08-10 11:49:27,893 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1813785, prompt_len=756
2026-08-10 11:49:37,355 INFO     29 [qwen-vl-parser] table API response (len=1625):
\begin{tabular}{lllllll}
\hline
6 & 嗜碱性粒细胞数 & BASO\# & 0.04 & 10$^9$/L & 0.00--0.06 & \\
7 & 中性粒细胞率 & NEUT\% & 67.2 & \% & 40.0--75.0 & \\
8 & 淋巴细胞率 & LYMPH\% & 21.2 & \% & 20.0--50.0 & \\
9 & 单核细胞率 & MONO\% & 5.0 & \% & 3.0--10.0 & \\
10 & 嗜酸性粒细胞率 & EOS\% & 6.0 & \% & 0.4--8.0 & \\
11 & 嗜碱性粒细胞率 & BASO\% & 0.6 & \% & 0--1.0 & \\
12 & *红细胞计数 & RBC & 4.66 & 10$^{12}$/L & 3.80--5.10 & \\
13 & *血红蛋白量 & HGB & 131 & g/L & 115--150 & \\
14 & *红细胞比积 & HCT & 42.5 & \% & 35.0--45.0 & \\
15 & *平均红细胞体积 & MCV & 91.1 & fL & 82.0--100.0 & \\
16 & *平均红细胞血红蛋白量 & MCH & 28.1 & pg & 27.0--34.0 & \\
17 & *平均红细胞血红蛋白浓度 & MCHC & 308 & g/L & 316--354 & \\
18 & 红细胞分布宽度 & RDW-SD & 48.5 & fL & 38.4--47.8 & \\
19 & *血小板计数 & PLT & 178 & 10$^9$/L & 101--320 & \\
\hline
\end{tabular}

\begin{tabular}{llllllll}
\hline
\multicolumn{2}{c}{DIFF} & \multicolumn{2}{c}{WNB} & \multicolumn{2}{c}{RBC} & \multicolumn{2}{c}{PLT} \\
\multicolumn{2}{c}{\includegraphics[width=0.25\textwidth]{image}} & \multicolumn{2}{c}{\includegraphics[width=0.25\textwidth]{image}} & \multicolumn{2}{c}{\includegraphics[width=0.25\textwidth]{image}} & \multicolumn{2}{c}{\includegraphics[width=0.25\textwidth]{image}} \\
\hline
\end{tabular}

\begin{tabular}{llll}
\hline
\multicolumn{4}{l}{声明：此结果仅对此标本负责} \\
\multicolumn{4}{l}{*为川渝互认项目} \\
\hline
采集时间: 2025-12-29 10:49:41 & \multicolumn{2}{l}{接收时间: 2025-12-29 10:50:50} & 申请医生: 燕海英 \\
报告时间: 2025-12-29 11:17:24 & \multicolumn{2}{l}{打印时间: 2025-12-29 11:17:26} & 检验者: 郭志刚 \\
联系电话: 028-87394636 & \multicolumn{2}{l}{} & 审核者: \textbf{杨怡} \\
实验室地址: 成都市一环路西二段32号 & \multicolumn{2}{l}{} & \\
\hline
\end{tabular}

第 1 页 共 1 页
2026-08-10 11:49:37,356 INFO     29 [qwen-vl-parser] page=8 table: 39 LaTeX lines (bbox 226-264)
2026-08-10 11:49:37,356 INFO     29 [qwen-vl-parser] page=8 table: 39 sections
2026-08-10 11:49:37,878 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2656188, prompt_len=764
2026-08-10 11:49:45,106 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:49:45,107 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 11:49:45,145 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2656188, prompt_len=401
2026-08-10 11:49:52,127 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:49:52.124+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:49:52,850 INFO     29 [qwen-vl-parser] text API response (len=1308):
["阿普唑仑片(精2)(基)", "ew/#/medicalRecord", "营养诊疗系统", "DoCare", "美康智营药学服务...", "单病种数据上报", "PMS医院绩效管理...", "POCT信息管理系统", "联众数字化病案浏...", "出生日期: 196******16", "过敏史: 无", "年龄: 62岁", "身份证号: 510***********045", "更多", "931786", "就诊类型: 门诊", "就诊时间: 2025-12-09 17:00:36", "接诊年龄: 62岁", "闭环", "病历详情", "病历文档", "四川省醫學科學院·四川省人民醫院", "门诊病历", "姓名:", "性别: 女年龄: 62岁门诊科室: 呼吸与危重症医学科门诊门诊病历号: 0009922109", "住址: 四川省成都市邛崃市联系电话: 133****6101挂号流水号: 63931786", "复诊记录", "记录时间: 2025-12-09 17:00", "主诉: 发作性喘息, 参加LOGOS (D5982C00008) 临床研究, 今日行电话回访。", "简要病史: 哮喘病史", "既往病史: 焦虑型抑郁症", "过敏史: 有过敏源花粉过敏, 未见报告, 具体不详", "流行病学史: /", "体格检查: NA", "门诊诊断: 哮喘", "处置: 今日15:35对受试者行电话回访, 受试者电话: 133****6101, 感谢受试者参加有关布地奈德、格隆溴铵和富马酸福莫特罗吸入器 (也简称为BGFMDI或PT010) 的临床试验, 该临床试验是一项双盲研究, 在所有临床试验受试者的通力配合下, 研究人员正在查明此药物是否有助于治疗哮喘患者。试验开始时, 受试者已经知道会接受BGF MDI、布地奈德和富马酸福莫特罗 (也简称为BFF MDI) 或Symbicort, 接受BGF MDI或BFF MDI的参加者也接受了看起来像Symbicort的安慰剂吸入器。接受了Symbicort的参加者还接受了看起来BGF MDI和BFF MDI的安慰剂吸入器, 安慰剂外观像研究治疗药物, 但其中不含任何药物。患者也知道, 任何人 (包括研究者和试验工作人员在内) 在试验结束之前都不知道您接受的是哪种治疗。", "告知受试者本试验已结束, 可告知患者接受的是布地奈德和富马酸福莫特罗定量吸入器 (BFF MDI), 受试者无疑问, 嘱受试者注意休息, 避免受凉感冒, 行肺功能锻炼, 病情加重时及时就诊。", "告知受试者可以通过trialsunmaries.com网站在线查看总体研究结果的摘要, 可使用D5982C00008在上述网站搜索本试验, 此网站不会收集、储存或使用可用于识别受试者的身份信息, 该摘要将为受试者介绍本试验的总体结果。", "婚烟史: 月经史:", "是否下转: 否。是否外伤: 否。是否美容: 否", "共2页, 第2页", "医师签名: 张利", "CS 扫描全能王", "3亿人都在用的扫描App", "9"]
2026-08-10 11:49:52,851 INFO     29 [qwen-vl-parser] page=9 text: 45 lines (bbox 265-309)
2026-08-10 11:49:52,851 INFO     29 [qwen-vl-parser] page=9 text: 45 sections
2026-08-10 11:49:53,237 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1530480, prompt_len=764
2026-08-10 11:50:00,603 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:50:00,603 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 11:50:00,612 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1530480, prompt_len=401
2026-08-10 11:50:04,267 INFO     29 [qwen-vl-parser] text API response (len=598):
["view/#/webMedicalRecord", "院营养诊疗系统", "DoCare", "美康智慧药学服务...", "单病种数据上报", "PMS医院绩效管理...", "POCT信息管理系统", "联众数字化病案浏...", "出生日期: 196******16", "过敏史: 无", "年龄: 62岁", "身份证号: 510***********045", "更多", "548559 就诊类型: 门诊 就诊时间: 2025-09-02 13:50:11 接诊年龄: 62岁", "闭环", "web版", "2026年3月12日 12:26:27", "姓名", "性别: 女", "年龄: 63岁", "门诊卡号: 0009922109", "科室: 互联网医院门诊", "主诊断: 支气管哮喘", "门诊医嘱", "门诊医嘱", "开立时间", "开立医生", "244166554 省集11*▲布地奈德福莫特罗吸入粉雾剂(II)信必可都保(基)(兴) 2盒 2吸 每日2次 经口吸入", "2025/09/03 09:14", "燕海英", "版权所有: 东软集团 Copyright 2011-2012 Neusoft Enterprises Limited 返回", "四川省人民医院集...", "CS 扫描全能王", "3亿人都在用的扫描App", "10"]
2026-08-10 11:50:04,267 INFO     29 [qwen-vl-parser] page=10 text: 35 lines (bbox 310-344)
2026-08-10 11:50:04,267 INFO     29 [qwen-vl-parser] page=10 text: 35 sections
2026-08-10 11:50:04,880 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4000258, prompt_len=764
2026-08-10 11:50:13,920 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2024-04-15"
}
```
2026-08-10 11:50:13,921 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2024-04-15
2026-08-10 11:50:13,952 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4000258, prompt_len=401
2026-08-10 11:50:22,299 INFO     29 [qwen-vl-parser] text API response (len=1203):
["四川省医学科学院·四川省人民医院", "门诊病历", "姓名：", "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667", "复诊记录", "记录时间：2024-04-15 09:26", "主诉：发作性喘息，参加LOGOS（D5982C00008）临床研究，行V1访视", "简要病史：患者今日7:40到院，自诉：哮喘病史：于2022年5月UK日首次出现哮喘症状，于2022年5月16日首次", "确诊为哮喘，2024年1月15日开始规范使用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次", "经口吸入 每日2次，控制症状，近一年未发生急性加重。", "既往病史：焦虑型抑郁症：2021年2月UK日-至今，采取以下药物治疗：", "草酸艾司西酞普兰片：2022年2月UK日-至今，20mg/次，qd；", "枸橼酸坦度螺酮胶囊：2022年2月UK日-至今，10mg/次，tid。", "过敏史：有过敏源花粉 因患者无法记得开始时间，故开始时间不详", "流行病学史：此前3个月内，患者无可能相关的视力变化；否认青光眼史；患者不存在具有临床意义的症性前列腺肥大或膀胱颈梗阻", "/尿潴留；患者在此前5年内不存在未完全缓解的不可切除的癌症，患者未在既往或当前在任何布地奈德和富马酸福莫特", "罗研究(PT009)，布地奈德、格隆安和富马酸福莫特罗(PT010)或格隆安(PT001)中接受随机化；患者无计划研究期间住院，", "患者否认访视前1个月内住过院，否认访视前4周内完成对呼吸道感染或哮喘急性发作的全身性激素治疗，否认有危机", "生命的哮喘，否认访视1前12个月内已知有药物滥用或酗酒史，否认对β2-激动剂、激素、抗胆碱药或MDI或pMDI中的", "任何组分发生超敏反应，否认既往或当前入组AEROSPHERE项目中的研究。", "体格检查：神志清楚，精神尚可，呼吸平稳，全身皮肤无黄染，无瘀点、瘀斑，皮肤皮温不高，皮肤无汗湿。浅表淋巴结", "未触及，头颅五官无畸形，眼球活动自如，睑结膜无充血苍白，球结膜无水肿，巩膜无黄染。口唇无发绀，", "伸舌居中，咽无充血，双侧扁桃体无肿大。颈软，颈静脉充盈，气管居中，甲状腺未扪及肿大。桶状胸，", "双肺呼吸音降低，双肺未闻及明显湿性啰音及哮鸣音。心界无明显增大，律齐，各瓣膜区未闻测量血", "共4页，第1页", "四川省医学科学院·四川省人民医院", "门诊病历", "姓名：马蓉 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667", ""]
2026-08-10 11:50:22,300 INFO     29 [qwen-vl-parser] page=11 text: 30 lines (bbox 345-374)
2026-08-10 11:50:22,300 INFO     29 [qwen-vl-parser] page=11 text: 30 sections
2026-08-10 11:50:22,853 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3586701, prompt_len=764
2026-08-10 11:50:23,293 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:50:23.289+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:50:30,187 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:50:30,188 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-10 11:50:30,224 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3586701, prompt_len=401
2026-08-10 11:50:38,181 INFO     29 [qwen-vl-parser] text API response (len=1048):
["四川省医学科学院·四川省人民医院", "门诊病历", "姓名：", "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：", "挂号流水号：49735667", "压）及病理性杂音。腹软，无压痛、反跳痛及肌紧张，肝脾肋下未触及，肝肾区无叩痛，肠鸣音不活跃。", "双下肢对称无明显水肿，四肢肌力及肌张力正常。生命体征详见生命体征表（受试者已在休息5分钟后", "取坐位）", "门诊诊断：", "哮喘", "处", "置：", "知情过程：根据患者已有既往资料的情况，考虑受试者可能符合“一项随机、双盲、双模拟、平行分组、", "多中心、24至52周可变时长的研究，评估布地奈德、格隆铵和富马酸福莫特罗定量吸入器（MDI）与布地", "奈德和富马酸福莫特罗MDI以及信必可®加压MDI相比在哮喘未充分控制的成人和青少年受试者中的疗", "效和安全性（LOGOS）”的临床试验，今日7时55分当面与患者本人及家属进行充分知情，详细讲解本研究", "的目的、方法、流程及可能的获益及风险，并给予患者充分的时间考虑，患者仔细阅读无疑问，自愿同意", "参加本项临床试验，于2024年4月15日8时15分与患者本人共同签署两份成人研究受试者主要信息", "和知情同意书（研究信息和知情同意书）（研究中心版本号1429-2.0，研究中心版本日期：2023年10月", "31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日当面与患者本人详细讲解中国个人", "信息保护附录相关内容，患者表示无疑问并充分理解接受，于2024年4月15日8时18分签署两份中国", "个人信息保护附录（中国个人信息保护附录）（研究中心版本号1429-2.0 研究中心版本日期2023年10", "月31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日同时告知患者12小时PFT子研", "究者相关内容，患者表示拒绝。", "人口统计学信息：出生日期：1963年8月16日 性别：女 民族：汉族 种族：中国人", "患者否认哮喘相关家族史，否认吸烟及饮酒，自诉无输血史及手术史，患者目前已绝经（经期：开始时间：", "1978年，结束时间：2014年）。", "疫苗接种史：目前已无法查询新冠疫苗接种史，患者自诉2021年-2022年期间接种三针（具体相关信息", "无法提供）", "共4页，第2页", "12"]
2026-08-10 11:50:38,182 INFO     29 [qwen-vl-parser] page=12 text: 32 lines (bbox 375-406)
2026-08-10 11:50:38,182 INFO     29 [qwen-vl-parser] page=12 text: 32 sections
2026-08-10 11:50:38,747 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3268838, prompt_len=764
2026-08-10 11:50:46,609 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:50:46,609 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 11:50:46,630 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3268838, prompt_len=401
2026-08-10 11:50:53,087 INFO     29 [qwen-vl-parser] text API response (len=1034):
["四川省医学科学院·四川省人民医院", "门诊病历", "姓名：", "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667", "询问患者最近一次进食时间，患者自诉19:10，今与患者确认测量前6小时内未使用SABA类药物，并确认前一晚吸入沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次 经口吸入 每日2次 时间为", "20:00，至今未使用任何药物。", "患者静息10分钟后以仰卧位行12导联ECG检查，详见ECG报告。在肺功能测量前进行FoNO检测，检测一小时前无饮水及进食，随后行给药前-60min、-30min肺功能检查，患者者给药前FEV1%：78.85%。", "检查结果详见报告。", "完成ACQ-6及ACQ-7问卷，ACQ-7评分≥1.5。", "患者性别：女，已绝经，故未使用中心试验室提供的试剂进行尿妊娠试验。", "采集血样；完成血液标本采集后进行处理，并送往中心实验室进行检测。", "患者目前符合所有入选标准，不符合任一排除标准，嘱患者自今日起停用沙美特罗替卡松吸入粉雾剂", "|舒利迭(兴)(50ug/250ug)1泡/次 经口吸入 每日2次。IRT系统登记，筛选号；E1429021，并获得培训", "装置1瓶，药物编号：117165-EQ；获得导入期BFP1瓶，药物编号为；661331-BD。使用培训装置对患者进行", "吸入器使用培训及检查吸入装置技术，完成给药培训后当场回收；于11:08指导患者对导入期BFP进行", "预喷并给药2喷，给药结束时间为：11:10。发放急救药物万托林1瓶，嘱患者必要时使用。", "发放ePRO设备和峰流速仪，协助患者完成使用培训，同时发放白色吸入器使用指南，受试者参与卡。", "受试者感谢卡、哮喘监测仪AMS患者快速入门指南、峰流速计AM3使用指南，手持设备患者快速指南。", "预约患者下周一来院进行下次访视；", "嘱患者带上发放的峰速仪、ePRO以及导入期药物；", "嘱患者带上自上次访视以来的住院、门诊、急诊等病历记录；", "嘱患者下次访视前急救药物沙丁胺醇暂停≥6小时；", "嘱患者下次访视前早间剂量必须暂停，直至完成当此访视所有给药前评价；", "嘱患者按要求清洗给药装置；", "共4页，第3页", "13"]
2026-08-10 11:50:53,087 INFO     29 [qwen-vl-parser] page=13 text: 27 lines (bbox 407-433)
2026-08-10 11:50:53,088 INFO     29 [qwen-vl-parser] page=13 text: 27 sections
2026-08-10 11:50:53,352 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=842244, prompt_len=764
2026-08-10 11:50:54,474 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:50:54.473+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:51:00,484 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:51:00,484 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-10 11:51:00,502 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=842244, prompt_len=401
2026-08-10 11:51:02,266 INFO     29 [qwen-vl-parser] text API response (len=225):
["四川省医学科学院·四川省人民医院", "门诊病历", "姓名：", "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：", "挂号流水号：49735667", "嘱患者用药期间如有任何不适，及时复诊。", "婚姻史：", "月经史：", "是否下转： 否", "是否外伤：否", "是否美容： 否", "医师签名： 燕海荣", "共4页，第4页", "14"]
2026-08-10 11:51:02,267 INFO     29 [qwen-vl-parser] page=14 text: 15 lines (bbox 434-448)
2026-08-10 11:51:02,267 INFO     29 [qwen-vl-parser] page=14 text: 15 sections
2026-08-10 11:51:02,267 INFO     29 [qwen-vl-parser] parse_pdf done: 449 sections from 14 pages.
2026-08-10 11:51:02,278 INFO     29 Close text detector.
2026-08-10 11:51:02,857 INFO     29 Close text recognizer.
2026-08-10 11:51:03,253 INFO     29 Close recognizer.
2026-08-10 11:51:03,665 INFO     29 Close recognizer.
2026-08-10 11:51:04,128 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 11:51:04,128 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Parser:MedLink | outputs={"html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "json"}
2026-08-10 11:51:04,128 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 11:51:04,158 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:04,158 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 门诊\n[BBOX-1] 就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁\n[BBOX-2] 闭环\n[BBOX-3] 病历详情\n[BBOX-4] 病历文档\n[BBOX-5] 四川省醫學科學院·四川省人民醫院\n[BBOX-6] 门诊病历\n[BBOX-7] 姓名:\n[BBOX-8] 别: 女年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109\n[BBOX-9] 住址: 四川省成都******* 联系电话: 133****6101 挂号流水号: 66150482\n[BBOX-10] 复诊记录\n[BBOX-11] 记录时间: 2026-03-10 19:04\n[BBOX-12] 主诉:\n[BBOX-13] 支气管哮喘复诊\n[BBOX-14] 简要病史:\n[BBOX-15] 支气管哮喘复诊, 目前哮喘症状稳定\n[BBOX-16] 既往病史:\n[BBOX-17] 阴性\n[BBOX-18] 过敏史:\n[BBOX-19] 阴性\n[BBOX-20] 流行病学\n[BBOX-21] 史:\n[BBOX-22] 阴性\n[BBOX-23] 体格检查:\n[BBOX-24] 阴性\n[BBOX-25] 门诊诊断:\n[BBOX-26] 支气管哮喘\n[BBOX-27] 处置:\n[BBOX-28] 继续使用舒利迭控制哮喘\n[BBOX-29] 婚姻史: 月经史:\n[BBOX-30] 是否下转: 否, 是否外伤: 否, 是否美容: 否\n[BBOX-31] 医师签名:\n[BBOX-32] 燕海荣\n[BBOX-33] 共1页, 第1页\n[BBOX-34] 0\n[BBOX-35] 异常项\n[BBOX-36] 1\n[BBOX-37] view/#/webMedicalRecord\n[BBOX-38] 院营养诊疗系统\n[BBOX-39] DoCare\n[BBOX-40] 美康智营药学服务...\n[BBOX-41] 单病种数据上报\n[BBOX-42] PMS医院绩效管理...\n[BBOX-43] POCT信息管理系统\n[BBOX-44] 联众数字化病案浏...\n[BBOX-45] 出生日期: 196****16\n[BBOX-46] 过敏史: 无\n[BBOX-47] 年龄: 62岁\n[BBOX-48] 身份证号: 510***********045\n[BBOX-49] 更多\n[BBOX-50] 65753497\n[BBOX-51] 就诊类型: 门诊\n[BBOX-52] 就诊时间: 2026-02-24 21:35:00\n[BBOX-53] 接诊年龄: 62岁\n[BBOX-54] 闭环\n[BBOX-55] 历web版\n[BBOX-56] 2026年3月12日 12:21:13\n[BBOX-57] 姓名:\n[BBOX-58] 性别: 女\n[BBOX-59] 年龄: 63岁\n[BBOX-60] 门诊卡号: 0009922109\n[BBOX-61] 科室: 互联网医院门诊\n[BBOX-62] 主诊断: 支气管哮喘\n[BBOX-63] 门诊医嘱\n[BBOX-64] 门诊医嘱\n[BBOX-65] 开立时间\n[BBOX-66] 开立医生\n[BBOX-67] ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入\n[BBOX-68] 2026/02/24 22:19\n[BBOX-69] 燕海英\n[BBOX-70] 集采7*甲泼尼龙片(兴)(基) 1盒 20mg 每日1次 口服\n[BBOX-71] 2026/02/25 09:00\n[BBOX-72] 燕海英\n[BBOX-73] CS 扫描全能王\n[BBOX-74] 3亿人都在用的扫描App\n[BBOX-75] 2\n[BBOX-76] 四川省医学科学院四川省人民医院\n[BBOX-77] 互联网门诊病历\n[BBOX-78] 姓名:\n[BBOX-79] 性别:女\n[BBOX-80] 年龄:62\n[BBOX-81] 门诊科室:互联网医院门诊\n[BBOX-82] 门诊病历号:0009922109\n[BBOX-83] 工作单位或住址:四川省成都市邛崃市临邛街道\n[BBOX-84] 联系电话:\n[BBOX-85] 复诊记录\n[BBOX-86] 记录时间:2026-02-24 22:18\n[BBOX-87] 主诉:咳嗽,喘息,加重3天\n[BBOX-88] 简要病史:咳嗽,喘息,加重3天,3天前受凉后出现喘息加重,无发热。\n[BBOX-89] 既往病史:\n[BBOX-90] 过敏史:\n[BBOX-91] 流行病学史:无\n[BBOX-92] 体格检查:无\n[BBOX-93] 门诊诊断:支气管哮喘,支气管哮喘急性发作\n[BBOX-94] 处理意见:无\n[BBOX-95] 是否下转:否\n[BBOX-96] 是否外伤:否\n[BBOX-97] 是否美容:否\n[BBOX-98] 是否体检:否\n[BBOX-99] 燕海荣\n[BBOX-100] 医师签名:\n[BBOX-101] 3\n[BBOX-102] #/webMedicalRecord\n[BBOX-103] 诊疗系统\n[BBOX-104] DoCare\n[BBOX-105] 美康智慧药学服务...\n[BBOX-106] 单病种数据上报\n[BBOX-107] PMS医院绩效管理...\n[BBOX-108] POCT信息管理系统\n[BBOX-109] 联众数字化病案浏...\n[BBOX-110] 生日: 196****16\n[BBOX-111] 过敏史: 否\n[BBOX-112] 62岁\n[BBOX-113] 身份证号: 510***********045\n[BBOX-114] 更多\n[BBOX-115] 005\n[BBOX-116] 就诊类型: 门诊\n[BBOX-117] 就诊时间: 2026-01-23 13:19:40\n[BBOX-118] 接诊年龄: 62岁\n[BBOX-119] 闭环\n[BBOX-120] eb版\n[BBOX-121] 2026年3月12日 12:22:03 注销\n[BBOX-122] 姓名:\n[BBOX-123] 性别: 女\n[BBOX-124] 年龄: 63岁\n[BBOX-125] 门诊卡号: 0009922109\n[BBOX-126] 科室: 互联网医院门诊\n[BBOX-127] 主诊断: 支气管哮喘\n[BBOX-128] 门诊医嘱\n[BBOX-129] 门诊医嘱\n[BBOX-130] 开立时间\n[BBOX-131] 开立医生\n[BBOX-132] 259698508 ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入\n[BBOX-133] 2026/01/23 13:48\n[BBOX-134] 燕海英\n[BBOX-135] 0\n[BBOX-136] 异常项\n[BBOX-137] CS\n[BBOX-138] 扫描全能王\n[BBOX-139] 3亿人都在用的扫描App\n[BBOX-140] 4\n[BBOX-141] 四川省医学科学院四川省人民医院\n[BBOX-142] 互联网门诊病历\n[BBOX-143] 姓名\n[BBOX-144] 性别：女\n[BBOX-145] 年龄：62\n[BBOX-146] 门诊科室：互联网医院门诊\n[BBOX-147] 门诊病历号：0009922109\n[BBOX-148] 工作单位或住址：四川省成都市邛崃市临邛街道\n[BBOX-149] 联系电话：\n[BBOX-150] 复诊记录\n[BBOX-151] 记录时间：2026-01-23 13:20\n[BBOX-152] 主诉：支气管哮喘\n[BBOX-153] 简要病史：支气管哮喘\n[BBOX-154] 既往病史：\n[BBOX-155] 过敏史：\n[BBOX-156] 流行病学史：无\n[BBOX-157] 体格检查：无\n[BBOX-158] 门诊诊断：支气管哮喘\n[BBOX-159] 处理意见：无\n[BBOX-160] 是否下转：否\n[BBOX-161] 是否外伤：否\n[BBOX-162] 是否美容：否\n[BBOX-163] 是否体检：否\n[BBOX-164] 燕海荣\n[BBOX-165] 医师签名：\n[BBOX-166] 5\n[BBOX-167] 流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29 10:01:20 接诊年龄: 62岁\n[BBOX-168] 闭环\n[BBOX-169] 病历详情\n[BBOX-170] 病历文档\n[BBOX-171] 四川省醫學科學院·四川省人民醫院\n[BBOX-172] 门诊病历\n[BBOX-173] 姓名:\n[BBOX-174] 性别: 女 年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109\n[BBOX-175] 住址: 四川省成都******** 联系电话: 133****6101 挂号流水号: 64363836\n[BBOX-176] 复诊记录\n[BBOX-177] 记录时间: 2025-12-29 10:38\n[BBOX-178] 主诉: 发作性喘息。\n[BBOX-179] 简要病史: 哮喘复诊, 1周前吼喘一次持续3天, 自觉呼吸困难\n[BBOX-180] 既往病史: 焦虑型抑郁症\n[BBOX-181] 过敏史: 有过敏源\n[BBOX-182] 流行病学\n[BBOX-183] 史: /\n[BBOX-184] 体格检查: 指尖氧饱和度95%, 心率78次/分\n[BBOX-185] 门诊诊断: 哮喘急性发作、失眠\n[BBOX-186] 处置: 血eos 0.4\n[BBOX-187] 集采7*甲泼尼龙片(兴)(基)20mg/次 口服 每日1次 6天\n[BBOX-188] ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500)1泡/次 经口吸入 每日2次 31天\n[BBOX-189] 阿育吠陀片(精2)(基)0.4mg/次 口服 每晚1次 20天\n[BBOX-190] 血细胞分析(CBC+DIFF)\n[BBOX-191] 婚姻史: 月经史:\n[BBOX-192] 是否下转: 否, 是否外伤: 否, 是否美容: 否\n[BBOX-193] 医师签名: 燕海荣\n[BBOX-194] 共2页, 第2页\n[BBOX-195] 6\n[BBOX-196] \\begin{tabular}{l l l l l l l}\n[BBOX-197] \\hline\n[BBOX-198] \\multicolumn{2}{c}{姓名(Name):} & \\multicolumn{2}{l}{病历号(Case No): 0009922109} & \\multicolumn{3}{l}{病区(Section): 呼吸与危重症医学科门诊} \\\\\n[BBOX-199] \\multicolumn{2}{c}{性别(Gender): 女} & \\multicolumn{2}{l}{条码号(Barcode): 1057544035} & \\multicolumn{3}{l}{床号(Bed No):} \\\\\n[BBOX-200] \\multicolumn{2}{c}{年龄(Age): 62 岁} & \\multicolumn{2}{l}{检测号(Test No): 311187} & \\multicolumn{3}{l}{标本(Specimen): 全血} \\\\\n[BBOX-201] \\multicolumn{2}{c}{实验室(Lab): 临检组} & \\multicolumn{5}{l}{诊断(Diagnosis): 哮喘急性发作} \\\\\n[BBOX-202] \\hline\n[BBOX-203] \\multicolumn{2}{c}{项目名称} & \\multicolumn{2}{c}{缩写} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{单位} & \\multicolumn{2}{c}{参考区间} \\\\\n[BBOX-204] \\hline\n[BBOX-205] 1 & *白细胞计数 & WBC & 6.65 & $10^9$/L & 3.50--9.50 \\\\\n[BBOX-206] 2 & 中性粒细胞数 & NEUT\\# & 4.47 & $10^9$/L & 1.80--6.30 \\\\\n[BBOX-207] 3 & 淋巴细胞数 & LYMPH\\# & 1.41 & $10^9$/L & 1.10--3.20 \\\\\n[BBOX-208] 4 & 单核细胞数 & MONO\\# & 0.33 & $10^9$/L & 0.10--0.60 \\\\\n[BBOX-209] 5 & 嗜酸性粒细胞数 & EOS\\# & 0.40 & $10^9$/L & 0.02--0.52 \\\\\n[BBOX-210] 6 & 嗜碱性粒细胞数 & BASO\\# & 0.04 & $10^9$/L & 0.00--0.06 \\\\\n[BBOX-211] 7 & 中性粒细胞率 & NEUT\\% & 67.2 & \\% & 40.0--75.0 \\\\\n[BBOX-212] 8 & 淋巴细胞率 & LYMPH\\% & 21.2 & \\% & 20.0--50.0 \\\\\n[BBOX-213] 9 & 单核细胞率 & MONO\\% & 5.0 & \\% & 3.0--10.0 \\\\\n[BBOX-214] 10 & 嗜酸性粒细胞率 & EOS\\% & 6.0 & \\% & 0.4--8.0 \\\\\n[BBOX-215] 11 & 嗜碱性粒细胞率 & BASO\\% & 0.6 & \\% & 0--1.0 \\\\\n[BBOX-216] 12 & *红细胞计数 & RBC & 4.66 & $10^{12}$/L & 3.80--5.10 \\\\\n[BBOX-217] 13 & *血红蛋白量 & HGB & 131 & g/L & 115--150 \\\\\n[BBOX-218] 14 & *红细胞比积 & HCT & 42.5 & \\% & 35.0--45.0 \\\\\n[BBOX-219] 15 & *平均红细胞体积 & MCV & 91.1 & fL & 82.0--100.0 \\\\\n[BBOX-220] 16 & *平均红细胞血红蛋白量 & MCH & 28.1 & pg & 27.0--34.0 \\\\\n[BBOX-221] 17 & *平均红细胞血红蛋白浓度 & MCHC & 308 & g/L & 316--354 \\\\\n[BBOX-222] 18 & 红细胞分布宽度 & RDW-SD & 48.5 & fL & 38.4--47.8 \\\\\n[BBOX-223] 19 & *血小板计数 & PLT & 178 & $10^9$/L & 101--320 \\\\\n[BBOX-224] \\hline\n[BBOX-225] \\end{tabular}\n[BBOX-226] \\begin{tabular}{lllllll}\n[BBOX-227] 报告时间: 2025-12-29\n[BBOX-228] \\hline\n[BBOX-229] 6 & 嗜碱性粒细胞数 & BASO\\# & 0.04 & 10$^9$/L & 0.00--0.06 & \\\\\n[BBOX-230] 7 & 中性粒细胞率 & NEUT\\% & 67.2 & \\% & 40.0--75.0 & \\\\\n[BBOX-231] 8 & 淋巴细胞率 & LYMPH\\% & 21.2 & \\% & 20.0--50.0 & \\\\\n[BBOX-232] 9 & 单核细胞率 & MONO\\% & 5.0 & \\% & 3.0--10.0 & \\\\\n[BBOX-233] 10 & 嗜酸性粒细胞率 & EOS\\% & 6.0 & \\% & 0.4--8.0 & \\\\\n[BBOX-234] 11 & 嗜碱性粒细胞率 & BASO\\% & 0.6 & \\% & 0--1.0 & \\\\\n[BBOX-235] 12 & *红细胞计数 & RBC & 4.66 & 10$^{12}$/L & 3.80--5.10 & \\\\\n[BBOX-236] 13 & *血红蛋白量 & HGB & 131 & g/L & 115--150 & \\\\\n[BBOX-237] 14 & *红细胞比积 & HCT & 42.5 & \\% & 35.0--45.0 & \\\\\n[BBOX-238] 15 & *平均红细胞体积 & MCV & 91.1 & fL & 82.0--100.0 & \\\\\n[BBOX-239] 16 & *平均红细胞血红蛋白量 & MCH & 28.1 & pg & 27.0--34.0 & \\\\\n[BBOX-240] 17 & *平均红细胞血红蛋白浓度 & MCHC & 308 & g/L & 316--354 & \\\\\n[BBOX-241] 18 & 红细胞分布宽度 & RDW-SD & 48.5 & fL & 38.4--47.8 & \\\\\n[BBOX-242] 19 & *血小板计数 & PLT & 178 & 10$^9$/L & 101--320 & \\\\\n[BBOX-243] \\hline\n[BBOX-244] \\end{tabular}\n[BBOX-245] \\begin{tabular}{llllllll}\n[BBOX-246] 报告时间: 2025-12-29\n[BBOX-247] \\hline\n[BBOX-248] \\multicolumn{2}{c}{DIFF} & \\multicolumn{2}{c}{WNB} & \\multicolumn{2}{c}{RBC} & \\multicolumn{2}{c}{PLT} \\\\\n[BBOX-249] \\multicolumn{2}{c}{\\includegraphics[width=0.25\\textwidth]{image}} & \\multicolumn{2}{c}{\\includegraphics[width=0.25\\textwidth]{image}} & \\multicolumn{2}{c}{\\includegraphics[width=0.25\\textwidth]{image}} & \\multicolumn{2}{c}{\\includegraphics[width=0.25\\textwidth]{image}} \\\\\n[BBOX-250] \\hline\n[BBOX-251] \\end{tabular}\n[BBOX-252] \\begin{tabular}{llll}\n[BBOX-253] 报告时间: 2025-12-29\n[BBOX-254] \\hline\n[BBOX-255] \\multicolumn{4}{l}{声明：此结果仅对此标本负责} \\\\\n[BBOX-256] \\multicolumn{4}{l}{*为川渝互认项目} \\\\\n[BBOX-257] \\hline\n[BBOX-258] 采集时间: 2025-12-29 10:49:41 & \\multicolumn{2}{l}{接收时间: 2025-12-29 10:50:50} & 申请医生: 燕海英 \\\\\n[BBOX-259] 报告时间: 2025-12-29 11:17:24 & \\multicolumn{2}{l}{打印时间: 2025-12-29 11:17:26} & 检验者: 郭志刚 \\\\\n[BBOX-260] 联系电话: 028-87394636 & \\multicolumn{2}{l}{} & 审核者: \\textbf{杨怡} \\\\\n[BBOX-261] 实验室地址: 成都市一环路西二段32号 & \\multicolumn{2}{l}{} & \\\\\n[BBOX-262] \\hline\n[BBOX-263] \\end{tabular}\n[BBOX-264] 第 1 页 共 1 页\n[BBOX-265] 阿普唑仑片(精2)(基)\n[BBOX-266] ew/#/medicalRecord\n[BBOX-267] 营养诊疗系统\n[BBOX-268] DoCare\n[BBOX-269] 美康智营药学服务...\n[BBOX-270] 单病种数据上报\n[BBOX-271] PMS医院绩效管理...\n[BBOX-272] POCT信息管理系统\n[BBOX-273] 联众数字化病案浏...\n[BBOX-274] 出生日期: 196******16\n[BBOX-275] 过敏史: 无\n[BBOX-276] 年龄: 62岁\n[BBOX-277] 身份证号: 510***********045\n[BBOX-278] 更多\n[BBOX-279] 931786\n[BBOX-280] 就诊类型: 门诊\n[BBOX-281] 就诊时间: 2025-12-09 17:00:36\n[BBOX-282] 接诊年龄: 62岁\n[BBOX-283] 闭环\n[BBOX-284] 病历详情\n[BBOX-285] 病历文档\n[BBOX-286] 四川省醫學科學院·四川省人民醫院\n[BBOX-287] 门诊病历\n[BBOX-288] 姓名:\n[BBOX-289] 性别: 女年龄: 62岁门诊科室: 呼吸与危重症医学科门诊门诊病历号: 0009922109\n[BBOX-290] 住址: 四川省成都市邛崃市联系电话: 133****6101挂号流水号: 63931786\n[BBOX-291] 复诊记录\n[BBOX-292] 记录时间: 2025-12-09 17:00\n[BBOX-293] 主诉: 发作性喘息, 参加LOGOS (D5982C00008) 临床研究, 今日行电话回访。\n[BBOX-294] 简要病史: 哮喘病史\n[BBOX-295] 既往病史: 焦虑型抑郁症\n[BBOX-296] 过敏史: 有过敏源花粉过敏, 未见报告, 具体不详\n[BBOX-297] 流行病学史: /\n[BBOX-298] 体格检查: NA\n[BBOX-299] 门诊诊断: 哮喘\n[BBOX-300] 处置: 今日15:35对受试者行电话回访, 受试者电话: 133****6101, 感谢受试者参加有关布地奈德、格隆溴铵和富马酸福莫特罗吸入器 (也简称为BGFMDI或PT010) 的临床试验, 该临床试验是一项双盲研究, 在所有临床试验受试者的通力配合下, 研究人员正在查明此药物是否有助于治疗哮喘患者。试验开始时, 受试者已经知道会接受BGF MDI、布地奈德和富马酸福莫特罗 (也简称为BFF MDI) 或Symbicort, 接受BGF MDI或BFF MDI的参加者也接受了看起来像Symbicort的安慰剂吸入器。接受了Symbicort的参加者还接受了看起来BGF MDI和BFF MDI的安慰剂吸入器, 安慰剂外观像研究治疗药物, 但其中不含任何药物。患者也知道, 任何人 (包括研究者和试验工作人员在内) 在试验结束之前都不知道您接受的是哪种治疗。\n[BBOX-301] 告知受试者本试验已结束, 可告知患者接受的是布地奈德和富马酸福莫特罗定量吸入器 (BFF MDI), 受试者无疑问, 嘱受试者注意休息, 避免受凉感冒, 行肺功能锻炼, 病情加重时及时就诊。\n[BBOX-302] 告知受试者可以通过trialsunmaries.com网站在线查看总体研究结果的摘要, 可使用D5982C00008在上述网站搜索本试验, 此网站不会收集、储存或使用可用于识别受试者的身份信息, 该摘要将为受试者介绍本试验的总体结果。\n[BBOX-303] 婚烟史: 月经史:\n[BBOX-304] 是否下转: 否。是否外伤: 否。是否美容: 否\n[BBOX-305] 共2页, 第2页\n[BBOX-306] 医师签名: 张利\n[BBOX-307] CS 扫描全能王\n[BBOX-308] 3亿人都在用的扫描App\n[BBOX-309] 9\n[BBOX-310] view/#/webMedicalRecord\n[BBOX-311] 院营养诊疗系统\n[BBOX-312] DoCare\n[BBOX-313] 美康智慧药学服务...\n[BBOX-314] 单病种数据上报\n[BBOX-315] PMS医院绩效管理...\n[BBOX-316] POCT信息管理系统\n[BBOX-317] 联众数字化病案浏...\n[BBOX-318] 出生日期: 196******16\n[BBOX-319] 过敏史: 无\n[BBOX-320] 年龄: 62岁\n[BBOX-321] 身份证号: 510***********045\n[BBOX-322] 更多\n[BBOX-323] 548559 就诊类型: 门诊 就诊时间: 2025-09-02 13:50:11 接诊年龄: 62岁\n[BBOX-324] 闭环\n[BBOX-325] web版\n[BBOX-326] 2026年3月12日 12:26:27\n[BBOX-327] 姓名\n[BBOX-328] 性别: 女\n[BBOX-329] 年龄: 63岁\n[BBOX-330] 门诊卡号: 0009922109\n[BBOX-331] 科室: 互联网医院门诊\n[BBOX-332] 主诊断: 支气管哮喘\n[BBOX-333] 门诊医嘱\n[BBOX-334] 门诊医嘱\n[BBOX-335] 开立时间\n[BBOX-336] 开立医生\n[BBOX-337] 244166554 省集11*▲布地奈德福莫特罗吸入粉雾剂(II)信必可都保(基)(兴) 2盒 2吸 每日2次 经口吸入\n[BBOX-338] 2025/09/03 09:14\n[BBOX-339] 燕海英\n[BBOX-340] 版权所有: 东软集团 Copyright 2011-2012 Neusoft Enterprises Limited 返回\n[BBOX-341] 四川省人民医院集...\n[BBOX-342] CS 扫描全能王\n[BBOX-343] 3亿人都在用的扫描App\n[BBOX-344] 10\n[BBOX-345] 四川省医学科学院·四川省人民医院\n[BBOX-346] 门诊病历\n[BBOX-347] 姓名：\n[BBOX-348] 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n[BBOX-349] 住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667\n[BBOX-350] 复诊记录\n[BBOX-351] 记录时间：2024-04-15 09:26\n[BBOX-352] 主诉：发作性喘息，参加LOGOS（D5982C00008）临床研究，行V1访视\n[BBOX-353] 简要病史：患者今日7:40到院，自诉：哮喘病史：于2022年5月UK日首次出现哮喘症状，于2022年5月16日首次\n[BBOX-354] 确诊为哮喘，2024年1月15日开始规范使用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次\n[BBOX-355] 经口吸入 每日2次，控制症状，近一年未发生急性加重。\n[BBOX-356] 既往病史：焦虑型抑郁症：2021年2月UK日-至今，采取以下药物治疗：\n[BBOX-357] 草酸艾司西酞普兰片：2022年2月UK日-至今，20mg/次，qd；\n[BBOX-358] 枸橼酸坦度螺酮胶囊：2022年2月UK日-至今，10mg/次，tid。\n[BBOX-359] 过敏史：有过敏源花粉 因患者无法记得开始时间，故开始时间不详\n[BBOX-360] 流行病学史：此前3个月内，患者无可能相关的视力变化；否认青光眼史；患者不存在具有临床意义的症性前列腺肥大或膀胱颈梗阻\n[BBOX-361] /尿潴留；患者在此前5年内不存在未完全缓解的不可切除的癌症，患者未在既往或当前在任何布地奈德和富马酸福莫特\n[BBOX-362] 罗研究(PT009)，布地奈德、格隆安和富马酸福莫特罗(PT010)或格隆安(PT001)中接受随机化；患者无计划研究期间住院，\n[BBOX-363] 患者否认访视前1个月内住过院，否认访视前4周内完成对呼吸道感染或哮喘急性发作的全身性激素治疗，否认有危机\n[BBOX-364] 生命的哮喘，否认访视1前12个月内已知有药物滥用或酗酒史，否认对β2-激动剂、激素、抗胆碱药或MDI或pMDI中的\n[BBOX-365] 任何组分发生超敏反应，否认既往或当前入组AEROSPHERE项目中的研究。\n[BBOX-366] 体格检查：神志清楚，精神尚可，呼吸平稳，全身皮肤无黄染，无瘀点、瘀斑，皮肤皮温不高，皮肤无汗湿。浅表淋巴结\n[BBOX-367] 未触及，头颅五官无畸形，眼球活动自如，睑结膜无充血苍白，球结膜无水肿，巩膜无黄染。口唇无发绀，\n[BBOX-368] 伸舌居中，咽无充血，双侧扁桃体无肿大。颈软，颈静脉充盈，气管居中，甲状腺未扪及肿大。桶状胸，\n[BBOX-369] 双肺呼吸音降低，双肺未闻及明显湿性啰音及哮鸣音。心界无明显增大，律齐，各瓣膜区未闻测量血\n[BBOX-370] 共4页，第1页\n[BBOX-371] 四川省医学科学院·四川省人民医院\n[BBOX-372] 门诊病历\n[BBOX-373] 姓名：马蓉 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n[BBOX-374] 住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667\n[BBOX-375] 四川省医学科学院·四川省人民医院\n[BBOX-376] 门诊病历\n[BBOX-377] 姓名：\n[BBOX-378] 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n[BBOX-379] 住址：四川省成都市邛崃市 联系电话：\n[BBOX-380] 挂号流水号：49735667\n[BBOX-381] 压）及病理性杂音。腹软，无压痛、反跳痛及肌紧张，肝脾肋下未触及，肝肾区无叩痛，肠鸣音不活跃。\n[BBOX-382] 双下肢对称无明显水肿，四肢肌力及肌张力正常。生命体征详见生命体征表（受试者已在休息5分钟后\n[BBOX-383] 取坐位）\n[BBOX-384] 门诊诊断：\n[BBOX-385] 哮喘\n[BBOX-386] 处\n[BBOX-387] 置：\n[BBOX-388] 知情过程：根据患者已有既往资料的情况，考虑受试者可能符合“一项随机、双盲、双模拟、平行分组、\n[BBOX-389] 多中心、24至52周可变时长的研究，评估布地奈德、格隆铵和富马酸福莫特罗定量吸入器（MDI）与布地\n[BBOX-390] 奈德和富马酸福莫特罗MDI以及信必可®加压MDI相比在哮喘未充分控制的成人和青少年受试者中的疗\n[BBOX-391] 效和安全性（LOGOS）”的临床试验，今日7时55分当面与患者本人及家属进行充分知情，详细讲解本研究\n[BBOX-392] 的目的、方法、流程及可能的获益及风险，并给予患者充分的时间考虑，患者仔细阅读无疑问，自愿同意\n[BBOX-393] 参加本项临床试验，于2024年4月15日8时15分与患者本人共同签署两份成人研究受试者主要信息\n[BBOX-394] 和知情同意书（研究信息和知情同意书）（研究中心版本号1429-2.0，研究中心版本日期：2023年10月\n[BBOX-395] 31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日当面与患者本人详细讲解中国个人\n[BBOX-396] 信息保护附录相关内容，患者表示无疑问并充分理解接受，于2024年4月15日8时18分签署两份中国\n[BBOX-397] 个人信息保护附录（中国个人信息保护附录）（研究中心版本号1429-2.0 研究中心版本日期2023年10\n[BBOX-398] 月31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日同时告知患者12小时PFT子研\n[BBOX-399] 究者相关内容，患者表示拒绝。\n[BBOX-400] 人口统计学信息：出生日期：1963年8月16日 性别：女 民族：汉族 种族：中国人\n[BBOX-401] 患者否认哮喘相关家族史，否认吸烟及饮酒，自诉无输血史及手术史，患者目前已绝经（经期：开始时间：\n[BBOX-402] 1978年，结束时间：2014年）。\n[BBOX-403] 疫苗接种史：目前已无法查询新冠疫苗接种史，患者自诉2021年-2022年期间接种三针（具体相关信息\n[BBOX-404] 无法提供）\n[BBOX-405] 共4页，第2页\n[BBOX-406] 12\n[BBOX-407] 四川省医学科学院·四川省人民医院\n[BBOX-408] 门诊病历\n[BBOX-409] 姓名：\n[BBOX-410] 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n[BBOX-411] 住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667\n[BBOX-412] 询问患者最近一次进食时间，患者自诉19:10，今与患者确认测量前6小时内未使用SABA类药物，并确认前一晚吸入沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次 经口吸入 每日2次 时间为\n[BBOX-413] 20:00，至今未使用任何药物。\n[BBOX-414] 患者静息10分钟后以仰卧位行12导联ECG检查，详见ECG报告。在肺功能测量前进行FoNO检测，检测一小时前无饮水及进食，随后行给药前-60min、-30min肺功能检查，患者者给药前FEV1%：78.85%。\n[BBOX-415] 检查结果详见报告。\n[BBOX-416] 完成ACQ-6及ACQ-7问卷，ACQ-7评分≥1.5。\n[BBOX-417] 患者性别：女，已绝经，故未使用中心试验室提供的试剂进行尿妊娠试验。\n[BBOX-418] 采集血样；完成血液标本采集后进行处理，并送往中心实验室进行检测。\n[BBOX-419] 患者目前符合所有入选标准，不符合任一排除标准，嘱患者自今日起停用沙美特罗替卡松吸入粉雾剂\n[BBOX-420] |舒利迭(兴)(50ug/250ug)1泡/次 经口吸入 每日2次。IRT系统登记，筛选号；E1429021，并获得培训\n[BBOX-421] 装置1瓶，药物编号：117165-EQ；获得导入期BFP1瓶，药物编号为；661331-BD。使用培训装置对患者进行\n[BBOX-422] 吸入器使用培训及检查吸入装置技术，完成给药培训后当场回收；于11:08指导患者对导入期BFP进行\n[BBOX-423] 预喷并给药2喷，给药结束时间为：11:10。发放急救药物万托林1瓶，嘱患者必要时使用。\n[BBOX-424] 发放ePRO设备和峰流速仪，协助患者完成使用培训，同时发放白色吸入器使用指南，受试者参与卡。\n[BBOX-425] 受试者感谢卡、哮喘监测仪AMS患者快速入门指南、峰流速计AM3使用指南，手持设备患者快速指南。\n[BBOX-426] 预约患者下周一来院进行下次访视；\n[BBOX-427] 嘱患者带上发放的峰速仪、ePRO以及导入期药物；\n[BBOX-428] 嘱患者带上自上次访视以来的住院、门诊、急诊等病历记录；\n[BBOX-429] 嘱患者下次访视前急救药物沙丁胺醇暂停≥6小时；\n[BBOX-430] 嘱患者下次访视前早间剂量必须暂停，直至完成当此访视所有给药前评价；\n[BBOX-431] 嘱患者按要求清洗给药装置；\n[BBOX-432] 共4页，第3页\n[BBOX-433] 13\n[BBOX-434] 四川省医学科学院·四川省人民医院\n[BBOX-435] 门诊病历\n[BBOX-436] 姓名：\n[BBOX-437] 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n[BBOX-438] 住址：四川省成都市邛崃市 联系电话：\n[BBOX-439] 挂号流水号：49735667\n[BBOX-440] 嘱患者用药期间如有任何不适，及时复诊。\n[BBOX-441] 婚姻史：\n[BBOX-442] 月经史：\n[BBOX-443] 是否下转： 否\n[BBOX-444] 是否外伤：否\n[BBOX-445] 是否美容： 否\n[BBOX-446] 医师签名： 燕海荣\n[BBOX-447] 共4页，第4页\n[BBOX-448] 14"
  }
]
2026-08-10 11:51:17,873 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:17,901 INFO     29 [SmartSplitter] SmartSplitter done: 10 chunks from 10 LLM segments (all bbox_id). Types: {'OutpatientRecord': 6, 'PrescriptionRecord': 3, 'LabReport': 1}
2026-08-10 11:51:17,915 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 11:51:17,916 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks": "10 items, types={'OutpatientRecord': 6, 'PrescriptionRecord': 3, 'LabReport': 1}"}
2026-08-10 11:51:17,916 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 11:51:17,916 INFO     29 [ChunkRouter] Routed 10 chunks into 3 groups: {'chunks_Clinical': 6, 'chunks_Prescription': 3, 'chunks_LabExam': 1}
2026-08-10 11:51:17,932 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 11:51:17,932 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | ChunkRouter:Router | outputs={"html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks": "10 items, types={'OutpatientRecord': 6, 'PrescriptionRecord': 3, 'LabReport': 1}", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:51:17,932 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 11:51:17,942 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:51:17,942 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:51:17,943 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[6, 7]
2026-08-10 11:51:17,943 INFO     29 [qwen-vl-table] positions ： [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:51:18,446 INFO     29 [qwen-vl-table] page=6, rect=1239x1754, img=(3442x4873)
2026-08-10 11:51:18,873 INFO     29 [qwen-vl-table] page=7, rect=1239x1754, img=(3442x4873)
2026-08-10 11:51:18,874 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:18,874 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 196, \"bbox_end\": 264, \"encounter_dates\": [\"2025-12-29\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l l l l l l l}\n\\hline\n\\multicolumn{2}{c}{姓名(Name):} & \\multicolumn{2}{l}{病历号(Case No): 0009922109} & \\multicolumn{3}{l}{病区(Section): 呼吸与危重症医学科门诊} \\\\\n\\multicolumn{2}{c}{性别(Gender): 女} & \\multicolumn{2}{l}{条码号(Barcode): 1057544035} & \\multicolumn{3}{l}{床号(Bed No):} \\\\\n\\multicolumn{2}{c}{年龄(Age): 62 岁} & \\multicolumn{2}{l}{检测号(Test No): 311187} & \\multicolumn{3}{l}{标本(Specimen): 全血} \\\\\n\\multicolumn{2}{c}{实验室(Lab): 临检组} & \\multicolumn{5}{l}{诊断(Diagnosis): 哮喘急性发作} \\\\\n\\hline\n\\multicolumn{2}{c}{项目名称} & \\multicolumn{2}{c}{缩写} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{单位} & \\multicolumn{2}{c}{参考区间} \\\\\n\\hline\n1 & *白细胞计数 & WBC & 6.65 & $10^9$/L & 3.50--9.50 \\\\\n2 & 中性粒细胞数 & NEUT\\# & 4.47 & $10^9$/L & 1.80--6.30 \\\\\n3 & 淋巴细胞数 & LYMPH\\# & 1.41 & $10^9$/L & 1.10--3.20 \\\\\n4 & 单核细胞数 & MONO\\# & 0.33 & $10^9$/L & 0.10--0.60 \\\\\n5 & 嗜酸性粒细胞数 & EOS\\# & 0.40 & $10^9$/L & 0.02--0.52 \\\\\n6 & 嗜碱性粒细胞数 & BASO\\# & 0.04 & $10^9$/L & 0.00--0.06 \\\\\n7 & 中性粒细胞率 & NEUT\\% & 67.2 & \\% & 40.0--75.0 \\\\\n8 & 淋巴细胞率 & LYMPH\\% & 21.2 & \\% & 20.0--50.0 \\\\\n9 & 单核细胞率 & MONO\\% & 5.0 & \\% & 3.0--10.0 \\\\\n10 & 嗜酸性粒细胞率 & EOS\\% & 6.0 & \\% & 0.4--8.0 \\\\\n11 & 嗜碱性粒细胞率 & BASO\\% & 0.6 & \\% & 0--1.0 \\\\\n12 & *红细胞计数 & RBC & 4.66 & $10^{12}$/L & 3.80--5.10 \\\\\n13 & *血红蛋白量 & HGB & 131 & g/L & 115--150 \\\\\n14 & *红细胞比积 & HCT & 42.5 & \\% & 35.0--45.0 \\\\\n15 & *平均红细胞体积 & MCV & 91.1 & fL & 82.0--100.0 \\\\\n16 & *平均红细胞血红蛋白量 & MCH & 28.1 & pg & 27.0--34.0 \\\\\n17 & *平均红细胞血红蛋白浓度 & MCHC & 308 & g/L & 316--354 \\\\\n18 & 红细胞分布宽度 & RDW-SD & 48.5 & fL & 38.4--47.8 \\\\\n19 & *血小板计数 & PLT & 178 & $10^9$/L & 101--320 \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{lllllll}\n报告时间: 2025-12-29\n\\hline\n6 & 嗜碱性粒细胞数 & BASO\\# & 0.04 & 10$^9$/L & 0.00--0.06 & \\\\",
    "role": "user"
  }
]
2026-08-10 11:51:25,622 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:51:25.619+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:51:29,798 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:29,798 INFO     29 [qwen-vl-table] page=6 LLM output (len=3308):
{
  "report_date": "2025-12-29",
  "items": [
    {
      "name": "*白细胞计数",
      "item_code": "WBC",
      "value": "6.65",
      "unit": "10^9/L",
      "reference_range": "3.50--9.50",
      "abnormal": false
    },
    {
      "name": "中性粒细胞数",
      "item_code": "NEUT#",
      "value": "4.47",
      "unit": "10^9/L",
      "reference_range": "1.80--6.30",
      "abnormal": false
    },
    {
      "name": "淋巴细胞数",
      "item_code": "LYMPH#",
      "value": "1.41",
      "unit": "10^9/L",
      "reference_range": "1.10--3.20",
      "abnormal": false
    },
    {
      "name": "单核细胞数",
      "item_code": "MONO#",
      "value": "0.33",
      "unit": "10^9/L",
      "reference_range": "0.10--0.60",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞数",
      "item_code": "EOS#",
      "value": "0.40",
      "unit": "10^9/L",
      "reference_range": "0.02--0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞数",
      "item_code": "BASO#",
      "value": "0.04",
      "unit": "10^9/L",
      "reference_range": "0.00--0.06",
      "abnormal": false
    },
    {
      "name": "中性粒细胞率",
      "item_code": "NEUT%",
      "value": "67.2",
      "unit": "%",
      "reference_range": "40.0--75.0",
      "abnormal": false
    },
    {
      "name": "淋巴细胞率",
      "item_code": "LYMPH%",
      "value": "21.2",
      "unit": "%",
      "reference_range": "20.0--50.0",
      "abnormal": false
    },
    {
      "name": "单核细胞率",
      "item_code": "MONO%",
      "value": "5.0",
      "unit": "%",
      "reference_range": "3.0--10.0",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞率",
      "item_code": "EOS%",
      "value": "6.0",
      "unit": "%",
      "reference_range": "0.4--8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞率",
      "item_code": "BASO%",
      "value": "0.6",
      "unit": "%",
      "reference_range": "0--1.0",
      "abnormal": false
    },
    {
      "name": "*红细胞计数",
      "item_code": "RBC",
      "value": "4.66",
      "unit": "10^12/L",
      "reference_range": "3.80--5.10",
      "abnormal": false
    },
    {
      "name": "*血红蛋白量",
      "item_code": "HGB",
      "value": "131",
      "unit": "g/L",
      "reference_range": "115--150",
      "abnormal": false
    },
    {
      "name": "*红细胞比积",
      "item_code": "HCT",
      "value": "42.5",
      "unit": "%",
      "reference_range": "35.0--45.0",
      "abnormal": false
    },
    {
      "name": "*平均红细胞体积",
      "item_code": "MCV",
      "value": "91.1",
      "unit": "fL",
      "reference_range": "82.0--100.0",
      "abnormal": false
    },
    {
      "name": "*平均红细胞血红蛋白量",
      "item_code": "MCH",
      "value": "28.1",
      "unit": "pg",
      "reference_range": "27.0--34.0",
      "abnormal": false
    },
    {
      "name": "*平均红细胞血红蛋白浓度",
      "item_code": "MCHC",
      "value": "308",
      "unit": "g/L",
      "reference_range": "316--354",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度",
      "item_code": "RDW-SD",
      "value": "48.5",
      "unit": "fL",
      "reference_range": "38.4--47.8",
      "abnormal": true
    },
    {
      "name": "*血小板计数",
      "item_code": "PLT",
      "value": "178",
      "unit": "10^9/L",
      "reference_range": "101--320",
      "abnormal": false
    }
  ]
}
2026-08-10 11:51:29,799 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:29,799 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 196, \"bbox_end\": 264, \"encounter_dates\": [\"2025-12-29\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "7 & 中性粒细胞率 & NEUT\\% & 67.2 & \\% & 40.0--75.0 & \\\\\n8 & 淋巴细胞率 & LYMPH\\% & 21.2 & \\% & 20.0--50.0 & \\\\\n9 & 单核细胞率 & MONO\\% & 5.0 & \\% & 3.0--10.0 & \\\\\n10 & 嗜酸性粒细胞率 & EOS\\% & 6.0 & \\% & 0.4--8.0 & \\\\\n11 & 嗜碱性粒细胞率 & BASO\\% & 0.6 & \\% & 0--1.0 & \\\\\n12 & *红细胞计数 & RBC & 4.66 & 10$^{12}$/L & 3.80--5.10 & \\\\\n13 & *血红蛋白量 & HGB & 131 & g/L & 115--150 & \\\\\n14 & *红细胞比积 & HCT & 42.5 & \\% & 35.0--45.0 & \\\\\n15 & *平均红细胞体积 & MCV & 91.1 & fL & 82.0--100.0 & \\\\\n16 & *平均红细胞血红蛋白量 & MCH & 28.1 & pg & 27.0--34.0 & \\\\\n17 & *平均红细胞血红蛋白浓度 & MCHC & 308 & g/L & 316--354 & \\\\\n18 & 红细胞分布宽度 & RDW-SD & 48.5 & fL & 38.4--47.8 & \\\\\n19 & *血小板计数 & PLT & 178 & 10$^9$/L & 101--320 & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{llllllll}\n报告时间: 2025-12-29\n\\hline\n\\multicolumn{2}{c}{DIFF} & \\multicolumn{2}{c}{WNB} & \\multicolumn{2}{c}{RBC} & \\multicolumn{2}{c}{PLT} \\\\\n\\multicolumn{2}{c}{\\includegraphics[width=0.25\\textwidth]{image}} & \\multicolumn{2}{c}{\\includegraphics[width=0.25\\textwidth]{image}} & \\multicolumn{2}{c}{\\includegraphics[width=0.25\\textwidth]{image}} & \\multicolumn{2}{c}{\\includegraphics[width=0.25\\textwidth]{image}} \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{llll}\n报告时间: 2025-12-29\n\\hline\n\\multicolumn{4}{l}{声明：此结果仅对此标本负责} \\\\\n\\multicolumn{4}{l}{*为川渝互认项目} \\\\\n\\hline\n采集时间: 2025-12-29 10:49:41 & \\multicolumn{2}{l}{接收时间: 2025-12-29 10:50:50} & 申请医生: 燕海英 \\\\\n报告时间: 2025-12-29 11:17:24 & \\multicolumn{2}{l}{打印时间: 2025-12-29 11:17:26} & 检验者: 郭志刚 \\\\\n联系电话: 028-87394636 & \\multicolumn{2}{l}{} & 审核者: \\textbf{杨怡} \\\\\n实验室地址: 成都市一环路西二段32号 & \\multicolumn{2}{l}{} & \\\\\n\\hline\n\\end{tabular}\n第 1 页 共 1 页",
    "role": "user"
  }
]
2026-08-10 11:51:37,344 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:37,344 INFO     29 [qwen-vl-table] page=7 LLM output (len=2253):
{
  "report_date": "2025-12-29",
  "items": [
    {
      "name": "中性粒细胞率",
      "item_code": "NEUT%",
      "value": "67.2",
      "unit": "%",
      "reference_range": "40.0--75.0",
      "abnormal": false
    },
    {
      "name": "淋巴细胞率",
      "item_code": "LYMPH%",
      "value": "21.2",
      "unit": "%",
      "reference_range": "20.0--50.0",
      "abnormal": false
    },
    {
      "name": "单核细胞率",
      "item_code": "MONO%",
      "value": "5.0",
      "unit": "%",
      "reference_range": "3.0--10.0",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞率",
      "item_code": "EOS%",
      "value": "6.0",
      "unit": "%",
      "reference_range": "0.4--8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞率",
      "item_code": "BASO%",
      "value": "0.6",
      "unit": "%",
      "reference_range": "0--1.0",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "4.66",
      "unit": "10^12/L",
      "reference_range": "3.80--5.10",
      "abnormal": false
    },
    {
      "name": "血红蛋白量",
      "item_code": "HGB",
      "value": "131",
      "unit": "g/L",
      "reference_range": "115--150",
      "abnormal": false
    },
    {
      "name": "红细胞比积",
      "item_code": "HCT",
      "value": "42.5",
      "unit": "%",
      "reference_range": "35.0--45.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "91.1",
      "unit": "fL",
      "reference_range": "82.0--100.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白量",
      "item_code": "MCH",
      "value": "28.1",
      "unit": "pg",
      "reference_range": "27.0--34.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": "MCHC",
      "value": "308",
      "unit": "g/L",
      "reference_range": "316--354",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度",
      "item_code": "RDW-SD",
      "value": "48.5",
      "unit": "fL",
      "reference_range": "38.4--47.8",
      "abnormal": true
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "178",
      "unit": "10^9/L",
      "reference_range": "101--320",
      "abnormal": false
    }
  ]
}
2026-08-10 11:51:37,344 INFO     29 [qwen-vl-table] coord grouping: {6: 32}
2026-08-10 11:51:37,350 INFO     29 [qwen-vl-table] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2890130, prompt_len=751
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
*白细胞计数、中性粒细胞数、淋巴细胞数、单核细胞数、嗜酸性粒细胞数、嗜碱性粒细胞数、中性粒细胞率、淋巴细胞率、单核细胞率、嗜酸性粒细胞率、嗜碱性粒细胞率、*红细胞计数、*血红蛋白量、*红细胞比积、*平均红细胞体积、*平均红细胞血红蛋白量、*平均红细胞血红蛋白浓度、红细胞分布宽度、*血小板计数、中性粒细胞率、淋巴细胞率、单核细胞率、嗜酸性粒细胞率、嗜碱性粒细胞率、红细胞计数、血红蛋白量、红细胞比积、平均红细胞体积、平均红细胞血红蛋白量、平均红细胞血红蛋白浓度、红细胞分布宽度、血小板计数

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
2026-08-10 11:51:54,426 INFO     29 [qwen-vl-table] coord API raw response (len=1655):
[
	{"text": "*白细胞计数", "bbox": [129, 436, 219, 450]},
	{"text": "中性粒细胞数", "bbox": [130, 454, 226, 467]},
	{"text": "淋巴细胞数", "bbox": [130, 470, 210, 483]},
	{"text": "单核细胞数", "bbox": [130, 487, 210, 500]},
	{"text": "嗜酸性粒细胞数", "bbox": [130, 503, 242, 516]},
	{"text": "嗜碱性粒细胞数", "bbox": [130, 519, 242, 532]},
	{"text": "中性粒细胞率", "bbox": [130, 536, 225, 549]},
	{"text": "淋巴细胞率", "bbox": [130, 552, 210, 565]},
	{"text": "单核细胞率", "bbox": [130, 569, 210, 582]},
	{"text": "嗜酸性粒细胞率", "bbox": [130, 586, 242, 599]},
	{"text": "嗜碱性粒细胞率", "bbox": [130, 602, 242, 615]},
	{"text": "*红细胞计数", "bbox": [129, 619, 218, 632]},
	{"text": "*血红蛋白量", "bbox": [129, 635, 218, 648]},
	{"text": "*红细胞比积", "bbox": [129, 652, 218, 665]},
	{"text": "*平均红细胞体积", "bbox": [129, 669, 250, 682]},
	{"text": "*平均红细胞血红蛋白量", "bbox": [129, 685, 298, 698]},
	{"text": "*平均红细胞血红蛋白浓度", "bbox": [129, 702, 320, 715]},
	{"text": "红细胞分布宽度", "bbox": [129, 718, 245, 731]},
	{"text": "*血小板计数", "bbox": [129, 735, 218, 748]},
	{"text": "中性粒细胞率", "bbox": [130, 536, 225, 549]},
	{"text": "淋巴细胞率", "bbox": [130, 552, 210, 565]},
	{"text": "单核细胞率", "bbox": [130, 569, 210, 582]},
	{"text": "嗜酸性粒细胞率", "bbox": [130, 586, 242, 599]},
	{"text": "嗜碱性粒细胞率", "bbox": [130, 602, 242, 615]},
	{"text": "红细胞计数", "bbox": [130, 619, 218, 632]},
	{"text": "血红蛋白量", "bbox": [130, 635, 218, 648]},
	{"text": "红细胞比积", "bbox": [130, 652, 218, 665]},
	{"text": "平均红细胞体积", "bbox": [130, 669, 250, 682]},
	{"text": "平均红细胞血红蛋白量", "bbox": [130, 685, 298, 698]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [130, 702, 320, 715]},
	{"text": "红细胞分布宽度", "bbox": [130, 718, 245, 731]},
	{"text": "血小板计数", "bbox": [130, 735, 218, 748]}
]
2026-08-10 11:51:54,427 INFO     29 [qwen-vl-table] coord API: raw_items=32, valid_items=32, elapsed=17.1s
2026-08-10 11:51:54,427 INFO     29 [qwen-vl-table] coord item[0]: text=*白细胞计数, bbox=[129, 436, 219, 450]
2026-08-10 11:51:54,427 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞数, bbox=[130, 454, 226, 467]
2026-08-10 11:51:54,427 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞数, bbox=[130, 470, 210, 483]
2026-08-10 11:51:54,427 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞数, bbox=[130, 487, 210, 500]
2026-08-10 11:51:54,427 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞数, bbox=[130, 503, 242, 516]
2026-08-10 11:51:54,427 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞数, bbox=[130, 519, 242, 532]
2026-08-10 11:51:54,427 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞率, bbox=[130, 536, 225, 549]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞率, bbox=[130, 552, 210, 565]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞率, bbox=[130, 569, 210, 582]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞率, bbox=[130, 586, 242, 599]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞率, bbox=[130, 602, 242, 615]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[11]: text=*红细胞计数, bbox=[129, 619, 218, 632]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[12]: text=*血红蛋白量, bbox=[129, 635, 218, 648]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[13]: text=*红细胞比积, bbox=[129, 652, 218, 665]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[14]: text=*平均红细胞体积, bbox=[129, 669, 250, 682]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[15]: text=*平均红细胞血红蛋白量, bbox=[129, 685, 298, 698]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[16]: text=*平均红细胞血红蛋白浓度, bbox=[129, 702, 320, 715]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度, bbox=[129, 718, 245, 731]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[18]: text=*血小板计数, bbox=[129, 735, 218, 748]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[19]: text=中性粒细胞率, bbox=[130, 536, 225, 549]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[20]: text=淋巴细胞率, bbox=[130, 552, 210, 565]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[21]: text=单核细胞率, bbox=[130, 569, 210, 582]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[22]: text=嗜酸性粒细胞率, bbox=[130, 586, 242, 599]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[23]: text=嗜碱性粒细胞率, bbox=[130, 602, 242, 615]
2026-08-10 11:51:54,428 INFO     29 [qwen-vl-table] coord item[24]: text=红细胞计数, bbox=[130, 619, 218, 632]
2026-08-10 11:51:54,429 INFO     29 [qwen-vl-table] coord item[25]: text=血红蛋白量, bbox=[130, 635, 218, 648]
2026-08-10 11:51:54,429 INFO     29 [qwen-vl-table] coord item[26]: text=红细胞比积, bbox=[130, 652, 218, 665]
2026-08-10 11:51:54,429 INFO     29 [qwen-vl-table] coord item[27]: text=平均红细胞体积, bbox=[130, 669, 250, 682]
2026-08-10 11:51:54,429 INFO     29 [qwen-vl-table] coord item[28]: text=平均红细胞血红蛋白量, bbox=[130, 685, 298, 698]
2026-08-10 11:51:54,429 INFO     29 [qwen-vl-table] coord item[29]: text=平均红细胞血红蛋白浓度, bbox=[130, 702, 320, 715]
2026-08-10 11:51:54,429 INFO     29 [qwen-vl-table] coord item[30]: text=红细胞分布宽度, bbox=[130, 718, 245, 731]
2026-08-10 11:51:54,429 INFO     29 [qwen-vl-table] coord item[31]: text=血小板计数, bbox=[130, 735, 218, 748]
2026-08-10 11:51:54,430 INFO     29 [qwen-vl-table] page=6 coord: matched 32/32, time=17.1s
2026-08-10 11:51:54,430 INFO     29 [qwen-vl-table] new_positions (32):
[[7, 159.83100000000002, 271.341, 764.744, 789.3], [7, 161.07000000000002, 280.014, 796.316, 819.118], [7, 161.07000000000002, 260.19, 824.38, 847.182], [7, 161.07000000000002, 260.19, 854.198, 877.0], [7, 161.07000000000002, 299.838, 882.2620000000001, 905.064], [7, 161.07000000000002, 299.838, 910.326, 933.128], [7, 161.07000000000002, 278.77500000000003, 940.144, 962.946], [7, 161.07000000000002, 260.19, 968.208, 991.01], [7, 161.07000000000002, 260.19, 998.026, 1020.828], [7, 161.07000000000002, 299.838, 1027.844, 1050.646], [7, 161.07000000000002, 299.838, 1055.908, 1078.71], [7, 159.83100000000002, 270.10200000000003, 1085.726, 1108.528], [7, 159.83100000000002, 270.10200000000003, 1113.79, 1136.592], [7, 159.83100000000002, 270.10200000000003, 1143.608, 1166.41], [7, 159.83100000000002, 309.75, 1173.426, 1196.228], [7, 159.83100000000002, 369.22200000000004, 1201.49, 1224.292], [7, 159.83100000000002, 396.48, 1231.308, 1254.11], [7, 161.07000000000002, 303.555, 1259.372, 1282.174], [7, 159.83100000000002, 270.10200000000003, 1289.19, 1311.992], [7, 161.07000000000002, 278.77500000000003, 940.144, 962.946], [7, 161.07000000000002, 260.19, 968.208, 991.01], [7, 161.07000000000002, 260.19, 998.026, 1020.828], [7, 161.07000000000002, 299.838, 1027.844, 1050.646], [7, 161.07000000000002, 299.838, 1055.908, 1078.71], [7, 161.07000000000002, 270.10200000000003, 1085.726, 1108.528], [7, 161.07000000000002, 270.10200000000003, 1113.79, 1136.592], [7, 161.07000000000002, 270.10200000000003, 1143.608, 1166.41], [7, 161.07000000000002, 309.75, 1173.426, 1196.228], [7, 161.07000000000002, 369.22200000000004, 1201.49, 1224.292], [7, 161.07000000000002, 396.48, 1231.308, 1254.11], [7, 161.07000000000002, 303.555, 1259.372, 1282.174], [7, 161.07000000000002, 270.10200000000003, 1289.19, 1311.992]]
2026-08-10 11:51:54,431 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=32, matched=32, pages=2, time=36.5s
2026-08-10 11:51:54,444 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 11:51:54,444 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:51:54,444 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 11:51:54,453 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:54,454 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:51:55,299 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:55,312 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 11:51:55,312 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:51:55,312 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 11:51:55,320 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:51:55,321 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:51:55,321 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:51:55,321 INFO     29 [qwen-vl-text] positions(33): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:51:55,321 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [33]
2026-08-10 11:51:55,636 INFO     29 [qwen-vl-text] page=0, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:51:55,639 INFO     29 [qwen-vl-text] LLM extraction start, text_len=351
2026-08-10 11:51:55,639 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:55,640 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 32, \"encounter_dates\": [\"2026-03-10\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊\n就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁\n闭环\n病历详情\n病历文档\n四川省醫學科學院·四川省人民醫院\n门诊病历\n姓名:\n别: 女年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109\n住址: 四川省成都******* 联系电话: 133****6101 挂号流水号: 66150482\n复诊记录\n记录时间: 2026-03-10 19:04\n主诉:\n支气管哮喘复诊\n简要病史:\n支气管哮喘复诊, 目前哮喘症状稳定\n既往病史:\n阴性\n过敏史:\n阴性\n流行病学\n史:\n阴性\n体格检查:\n阴性\n门诊诊断:\n支气管哮喘\n处置:\n继续使用舒利迭控制哮喘\n婚姻史: 月经史:\n是否下转: 否, 是否外伤: 否, 是否美容: 否\n医师签名:\n燕海荣",
    "role": "user"
  }
]
2026-08-10 11:51:56,734 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:51:56.731+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:51:56,910 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:51:56,910 INFO     29 [qwen-vl-text] LLM output (len=193):
{
  "encounter_date": "2026-03-10",
  "chief_complaint": "支气管哮喘复诊",
  "present_illness": "支气管哮喘复诊, 目前哮喘症状稳定",
  "past_history": "阴性",
  "diagnosis": "支气管哮喘",
  "treatment_plan": "继续使用舒利迭控制哮喘"
}
2026-08-10 11:51:56,911 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-10]
2026-08-10 11:51:56,912 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1148592, prompt_len=1063
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门诊", "就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁", "闭环", "病历详情", "病历文档", "四川省醫學科學院·四川省人民醫院", "门诊病历", "姓名:", "别: 女年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109", "住址: 四川省成都******* 联系电话: 133****6101 挂号流水号: 66150482", "复诊记录", "记录时间: 2026-03-10 19:04", "主诉:", "支气管哮喘复诊", "简要病史:", "支气管哮喘复诊, 目前哮喘症状稳定", "既往病史:", "阴性", "过敏史:", "阴性", "流行病学", "史:", "阴性", "体格检查:", "阴性", "门诊诊断:", "支气管哮喘", "处置:", "继续使用舒利迭控制哮喘", "婚姻史: 月经史:", "是否下转: 否, 是否外伤: 否, 是否美容: 否", "医师签名:", "燕海荣"]

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
2026-08-10 11:52:14,524 INFO     29 [qwen-vl-text] coord API raw response (len=1803):
[
	{"text": "门诊", "bbox": [98, 342, 119, 351]},
	{"text": "就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁", "bbox": [131, 342, 360, 351]},
	{"text": "闭环", "bbox": [877, 342, 899, 351]},
	{"text": "病历详情", "bbox": [9, 366, 50, 374]},
	{"text": "病历文档", "bbox": [77, 366, 118, 374]},
	{"text": "四川省醫學科學院·四川省人民醫院", "bbox": [413, 400, 601, 409]},
	{"text": "门诊病历", "bbox": [456, 413, 527, 423]},
	{"text": "姓名:", "bbox": [9, 428, 34, 437]},
	{"text": "别: 女年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109", "bbox": [69, 428, 422, 437]},
	{"text": "住址: 四川省成都******* 联系电话: 133****6101 挂号流水号: 66150482", "bbox": [9, 441, 337, 449]},
	{"text": "复诊记录", "bbox": [467, 455, 515, 464]},
	{"text": "记录时间:", "bbox": [12, 469, 54, 477]},
	{"text": "2026-03-10 19:04", "bbox": [70, 469, 149, 477]},
	{"text": "主诉:", "bbox": [12, 484, 38, 492]},
	{"text": "支气管哮喘复诊", "bbox": [69, 484, 136, 492]},
	{"text": "简要病史:", "bbox": [12, 499, 54, 507]},
	{"text": "支气管哮喘复诊, 目前哮喘症状稳定", "bbox": [69, 499, 219, 507]},
	{"text": "既往病史:", "bbox": [12, 513, 54, 521]},
	{"text": "阴性", "bbox": [70, 513, 90, 521]},
	{"text": "过敏史:", "bbox": [12, 528, 51, 536]},
	{"text": "阴性", "bbox": [70, 528, 90, 536]},
	{"text": "流行病学", "bbox": [12, 543, 51, 551]},
	{"text": "史:", "bbox": [12, 549, 26, 557]},
	{"text": "阴性", "bbox": [70, 546, 89, 554]},
	{"text": "体格检查:", "bbox": [12, 563, 54, 571]},
	{"text": "阴性", "bbox": [70, 563, 90, 571]},
	{"text": "门诊诊断:", "bbox": [12, 577, 54, 585]},
	{"text": "支气管哮喘", "bbox": [70, 577, 117, 585]},
	{"text": "处置:", "bbox": [12, 592, 38, 600]},
	{"text": "继续使用舒利迭控制哮喘", "bbox": [70, 592, 170, 600]},
	{"text": "婚姻史: 月经史:", "bbox": [10, 606, 83, 614]},
	{"text": "是否下转: 否, 是否外伤: 否, 是否美容: 否", "bbox": [10, 617, 208, 625]},
	{"text": "医师签名:", "bbox": [854, 632, 894, 640]},
	{"text": "燕海荣", "bbox": [908, 631, 952, 644]}
]
2026-08-10 11:52:14,524 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=17.6s
2026-08-10 11:52:14,524 INFO     29 [qwen-vl-text] coord item[0]: text=门诊, bbox=[98, 342, 119, 351]
2026-08-10 11:52:14,524 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁, bbox=[131, 342, 360, 351]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[2]: text=闭环, bbox=[877, 342, 899, 351]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[3]: text=病历详情, bbox=[9, 366, 50, 374]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[4]: text=病历文档, bbox=[77, 366, 118, 374]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[5]: text=四川省醫學科學院·四川省人民醫院, bbox=[413, 400, 601, 409]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[6]: text=门诊病历, bbox=[456, 413, 527, 423]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[9, 428, 34, 437]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[8]: text=别: 女年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109, bbox=[69, 428, 422, 437]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[9]: text=住址: 四川省成都******* 联系电话: 133****6101 挂号流水号: 66150482, bbox=[9, 441, 337, 449]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[10]: text=复诊记录, bbox=[467, 455, 515, 464]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[11]: text=记录时间:, bbox=[12, 469, 54, 477]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[12]: text=2026-03-10 19:04, bbox=[70, 469, 149, 477]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[13]: text=主诉:, bbox=[12, 484, 38, 492]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[14]: text=支气管哮喘复诊, bbox=[69, 484, 136, 492]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[15]: text=简要病史:, bbox=[12, 499, 54, 507]
2026-08-10 11:52:14,525 INFO     29 [qwen-vl-text] coord item[16]: text=支气管哮喘复诊, 目前哮喘症状稳定, bbox=[69, 499, 219, 507]
2026-08-10 11:52:14,526 INFO     29 [qwen-vl-text] coord item[17]: text=既往病史:, bbox=[12, 513, 54, 521]
2026-08-10 11:52:14,526 INFO     29 [qwen-vl-text] coord item[18]: text=阴性, bbox=[70, 513, 90, 521]
2026-08-10 11:52:14,526 INFO     29 [qwen-vl-text] coord item[19]: text=过敏史:, bbox=[12, 528, 51, 536]
2026-08-10 11:52:14,526 INFO     29 [qwen-vl-text] coord item[20]: text=阴性, bbox=[70, 528, 90, 536]
2026-08-10 11:52:14,526 INFO     29 [qwen-vl-text] coord item[21]: text=流行病学, bbox=[12, 543, 51, 551]
2026-08-10 11:52:14,526 INFO     29 [qwen-vl-text] coord item[22]: text=史:, bbox=[12, 549, 26, 557]
2026-08-10 11:52:14,526 INFO     29 [qwen-vl-text] coord item[23]: text=阴性, bbox=[70, 546, 89, 554]
2026-08-10 11:52:14,526 INFO     29 [qwen-vl-text] coord item[24]: text=体格检查:, bbox=[12, 563, 54, 571]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[25]: text=阴性, bbox=[70, 563, 90, 571]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[26]: text=门诊诊断:, bbox=[12, 577, 54, 585]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[27]: text=支气管哮喘, bbox=[70, 577, 117, 585]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[28]: text=处置:, bbox=[12, 592, 38, 600]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[29]: text=继续使用舒利迭控制哮喘, bbox=[70, 592, 170, 600]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[30]: text=婚姻史: 月经史:, bbox=[10, 606, 83, 614]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[31]: text=是否下转: 否, 是否外伤: 否, 是否美容: 否, bbox=[10, 617, 208, 625]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[32]: text=医师签名:, bbox=[854, 632, 894, 640]
2026-08-10 11:52:14,527 INFO     29 [qwen-vl-text] coord item[33]: text=燕海荣, bbox=[908, 631, 952, 644]
2026-08-10 11:52:14,528 INFO     29 [qwen-vl-text] page=0 — 33/33 coords, api_time=17.6s
2026-08-10 11:52:14,528 INFO     29 [qwen-vl-text] new_positions (33):
[[0, 121.42200000000001, 147.441, 599.868, 615.654], [0, 162.30900000000003, 446.04, 599.868, 615.654], [0, 1086.603, 1113.861, 599.868, 615.654], [0, 11.151000000000002, 61.95, 641.964, 655.996], [0, 95.403, 146.202, 641.964, 655.996], [0, 511.70700000000005, 744.639, 701.6, 717.386], [0, 564.984, 652.9530000000001, 724.402, 741.942], [0, 11.151000000000002, 42.126000000000005, 750.712, 766.498], [0, 85.49100000000001, 522.8580000000001, 750.712, 766.498], [0, 11.151000000000002, 417.543, 773.514, 787.546], [0, 578.613, 638.085, 798.07, 813.856], [0, 14.868000000000002, 66.906, 822.626, 836.658], [0, 86.73, 184.61100000000002, 822.626, 836.658], [0, 14.868000000000002, 47.082, 848.936, 862.968], [0, 85.49100000000001, 168.50400000000002, 848.936, 862.968], [0, 14.868000000000002, 66.906, 875.246, 889.278], [0, 85.49100000000001, 271.341, 875.246, 889.278], [0, 14.868000000000002, 66.906, 899.802, 913.834], [0, 86.73, 111.51, 899.802, 913.834], [0, 14.868000000000002, 63.18900000000001, 926.112, 940.144], [0, 86.73, 111.51, 926.112, 940.144], [0, 14.868000000000002, 63.18900000000001, 952.422, 966.454], [0, 14.868000000000002, 32.214000000000006, 962.946, 976.978], [0, 86.73, 110.27100000000002, 957.684, 971.716], [0, 14.868000000000002, 66.906, 987.502, 1001.534], [0, 86.73, 111.51, 987.502, 1001.534], [0, 14.868000000000002, 66.906, 1012.058, 1026.09], [0, 86.73, 144.96300000000002, 1012.058, 1026.09], [0, 14.868000000000002, 47.082, 1038.368, 1052.4], [0, 86.73, 210.63000000000002, 1038.368, 1052.4], [0, 12.39, 102.837, 1062.924, 1076.956], [0, 12.39, 257.71200000000005, 1082.218, 1096.25], [0, 1058.106, 1107.6660000000002, 1108.528, 1122.56]]
2026-08-10 11:52:14,528 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=19.2s
2026-08-10 11:52:14,528 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:52:14,537 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:52:14,538 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:52:14,538 INFO     29 [qwen-vl-text] positions(25): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:52:14,538 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [25]
2026-08-10 11:52:14,894 INFO     29 [qwen-vl-text] page=2, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:52:14,897 INFO     29 [qwen-vl-text] LLM extraction start, text_len=263
2026-08-10 11:52:14,897 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:52:14,897 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 76, \"bbox_end\": 100, \"encounter_dates\": [\"2026-02-24\"], \"department\": \"互联网医院门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四川省医学科学院四川省人民医院\n互联网门诊病历\n姓名:\n性别:女\n年龄:62\n门诊科室:互联网医院门诊\n门诊病历号:0009922109\n工作单位或住址:四川省成都市邛崃市临邛街道\n联系电话:\n复诊记录\n记录时间:2026-02-24 22:18\n主诉:咳嗽,喘息,加重3天\n简要病史:咳嗽,喘息,加重3天,3天前受凉后出现喘息加重,无发热。\n既往病史:\n过敏史:\n流行病学史:无\n体格检查:无\n门诊诊断:支气管哮喘,支气管哮喘急性发作\n处理意见:无\n是否下转:否\n是否外伤:否\n是否美容:否\n是否体检:否\n燕海荣\n医师签名:",
    "role": "user"
  }
]
2026-08-10 11:52:16,507 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:52:16,507 INFO     29 [qwen-vl-text] LLM output (len=208):
{
  "encounter_date": "2026-02-24",
  "chief_complaint": "咳嗽,喘息,加重3天",
  "present_illness": "咳嗽,喘息,加重3天,3天前受凉后出现喘息加重,无发热。",
  "past_history": null,
  "diagnosis": "支气管哮喘,支气管哮喘急性发作",
  "treatment_plan": null
}
2026-08-10 11:52:16,507 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-24]
2026-08-10 11:52:16,509 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1225744, prompt_len=951
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["四川省医学科学院四川省人民医院", "互联网门诊病历", "姓名:", "性别:女", "年龄:62", "门诊科室:互联网医院门诊", "门诊病历号:0009922109", "工作单位或住址:四川省成都市邛崃市临邛街道", "联系电话:", "复诊记录", "记录时间:2026-02-24 22:18", "主诉:咳嗽,喘息,加重3天", "简要病史:咳嗽,喘息,加重3天,3天前受凉后出现喘息加重,无发热。", "既往病史:", "过敏史:", "流行病学史:无", "体格检查:无", "门诊诊断:支气管哮喘,支气管哮喘急性发作", "处理意见:无", "是否下转:否", "是否外伤:否", "是否美容:否", "是否体检:否", "燕海荣", "医师签名:"]

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
2026-08-10 11:52:31,097 INFO     29 [qwen-vl-text] coord API raw response (len=1351):
[
	{"text": "四川省医学科学院四川省人民医院", "bbox": [324, 311, 725, 333]},
	{"text": "互联网门诊病历", "bbox": [404, 333, 671, 353]},
	{"text": "姓名:", "bbox": [61, 357, 100, 370]},
	{"text": "性别:女", "bbox": [189, 357, 257, 370]},
	{"text": "年龄:62", "bbox": [302, 357, 370, 370]},
	{"text": "门诊科室:互联网医院门诊", "bbox": [412, 357, 612, 370]},
	{"text": "门诊病历号:0009922109", "bbox": [655, 357, 841, 370]},
	{"text": "工作单位或住址:四川省成都市邛崃市临邛街道", "bbox": [61, 376, 420, 389]},
	{"text": "联系电话:", "bbox": [470, 376, 544, 389]},
	{"text": "复诊记录", "bbox": [268, 415, 336, 428]},
	{"text": "记录时间:2026-02-24 22:18", "bbox": [61, 435, 285, 448]},
	{"text": "主诉:咳嗽,喘息,加重3天", "bbox": [61, 455, 311, 468]},
	{"text": "简要病史:咳嗽,喘息,加重3天,3天前受凉后出现喘息加重,无发热。", "bbox": [61, 473, 595, 487]},
	{"text": "既往病史:", "bbox": [61, 493, 136, 506]},
	{"text": "过敏史:", "bbox": [61, 512, 136, 525]},
	{"text": "流行病学史:无", "bbox": [61, 532, 180, 545]},
	{"text": "体格检查:无", "bbox": [61, 551, 163, 564]},
	{"text": "门诊诊断:支气管哮喘,支气管哮喘急性发作", "bbox": [61, 570, 395, 583]},
	{"text": "处理意见:无", "bbox": [61, 590, 163, 603]},
	{"text": "是否下转:否", "bbox": [61, 610, 163, 623]},
	{"text": "是否外伤:否", "bbox": [61, 629, 163, 642]},
	{"text": "是否美容:否", "bbox": [61, 649, 163, 662]},
	{"text": "是否体检:否", "bbox": [61, 668, 163, 681]},
	{"text": "燕海荣", "bbox": [444, 645, 508, 664]},
	{"text": "医师签名:", "bbox": [465, 684, 538, 697]}
]
2026-08-10 11:52:31,098 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=14.6s
2026-08-10 11:52:31,098 INFO     29 [qwen-vl-text] coord item[0]: text=四川省医学科学院四川省人民医院, bbox=[324, 311, 725, 333]
2026-08-10 11:52:31,098 INFO     29 [qwen-vl-text] coord item[1]: text=互联网门诊病历, bbox=[404, 333, 671, 353]
2026-08-10 11:52:31,098 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[61, 357, 100, 370]
2026-08-10 11:52:31,098 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[189, 357, 257, 370]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[4]: text=年龄:62, bbox=[302, 357, 370, 370]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[5]: text=门诊科室:互联网医院门诊, bbox=[412, 357, 612, 370]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[6]: text=门诊病历号:0009922109, bbox=[655, 357, 841, 370]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[7]: text=工作单位或住址:四川省成都市邛崃市临邛街道, bbox=[61, 376, 420, 389]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[8]: text=联系电话:, bbox=[470, 376, 544, 389]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[9]: text=复诊记录, bbox=[268, 415, 336, 428]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[10]: text=记录时间:2026-02-24 22:18, bbox=[61, 435, 285, 448]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[11]: text=主诉:咳嗽,喘息,加重3天, bbox=[61, 455, 311, 468]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[12]: text=简要病史:咳嗽,喘息,加重3天,3天前受凉后出现喘息加重,无发热。, bbox=[61, 473, 595, 487]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[13]: text=既往病史:, bbox=[61, 493, 136, 506]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[14]: text=过敏史:, bbox=[61, 512, 136, 525]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[15]: text=流行病学史:无, bbox=[61, 532, 180, 545]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[16]: text=体格检查:无, bbox=[61, 551, 163, 564]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[17]: text=门诊诊断:支气管哮喘,支气管哮喘急性发作, bbox=[61, 570, 395, 583]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[18]: text=处理意见:无, bbox=[61, 590, 163, 603]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[19]: text=是否下转:否, bbox=[61, 610, 163, 623]
2026-08-10 11:52:31,099 INFO     29 [qwen-vl-text] coord item[20]: text=是否外伤:否, bbox=[61, 629, 163, 642]
2026-08-10 11:52:31,100 INFO     29 [qwen-vl-text] coord item[21]: text=是否美容:否, bbox=[61, 649, 163, 662]
2026-08-10 11:52:31,100 INFO     29 [qwen-vl-text] coord item[22]: text=是否体检:否, bbox=[61, 668, 163, 681]
2026-08-10 11:52:31,100 INFO     29 [qwen-vl-text] coord item[23]: text=燕海荣, bbox=[444, 645, 508, 664]
2026-08-10 11:52:31,100 INFO     29 [qwen-vl-text] coord item[24]: text=医师签名:, bbox=[465, 684, 538, 697]
2026-08-10 11:52:31,100 INFO     29 [qwen-vl-text] page=2 — 25/25 coords, api_time=14.6s
2026-08-10 11:52:31,100 INFO     29 [qwen-vl-text] new_positions (25):
[[2, 401.43600000000004, 898.2750000000001, 545.494, 584.082], [2, 500.55600000000004, 831.369, 584.082, 619.162], [2, 75.57900000000001, 123.9, 626.178, 648.98], [2, 234.17100000000002, 318.423, 626.178, 648.98], [2, 374.17800000000005, 458.43000000000006, 626.178, 648.98], [2, 510.468, 758.268, 626.178, 648.98], [2, 811.5450000000001, 1041.999, 626.178, 648.98], [2, 75.57900000000001, 520.38, 659.504, 682.306], [2, 582.33, 674.0160000000001, 659.504, 682.306], [2, 332.052, 416.30400000000003, 727.91, 750.712], [2, 75.57900000000001, 353.115, 762.99, 785.792], [2, 75.57900000000001, 385.329, 798.07, 820.872], [2, 75.57900000000001, 737.205, 829.642, 854.198], [2, 75.57900000000001, 168.50400000000002, 864.722, 887.524], [2, 75.57900000000001, 168.50400000000002, 898.048, 920.85], [2, 75.57900000000001, 223.02, 933.128, 955.93], [2, 75.57900000000001, 201.95700000000002, 966.454, 989.256], [2, 75.57900000000001, 489.40500000000003, 999.78, 1022.582], [2, 75.57900000000001, 201.95700000000002, 1034.86, 1057.662], [2, 75.57900000000001, 201.95700000000002, 1069.94, 1092.742], [2, 75.57900000000001, 201.95700000000002, 1103.266, 1126.068], [2, 75.57900000000001, 201.95700000000002, 1138.346, 1161.148], [2, 75.57900000000001, 201.95700000000002, 1171.672, 1194.474], [2, 550.1160000000001, 629.412, 1131.33, 1164.656], [2, 576.135, 666.5820000000001, 1199.736, 1222.538]]
2026-08-10 11:52:31,101 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=16.6s
2026-08-10 11:52:31,101 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:52:31,103 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:52:31,103 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:52:31,103 INFO     29 [qwen-vl-text] positions(25): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:52:31,103 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [25]
2026-08-10 11:52:31,450 INFO     29 [qwen-vl-text] page=4, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:52:31,452 INFO     29 [qwen-vl-text] LLM extraction start, text_len=224
2026-08-10 11:52:31,452 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:52:31,453 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 141, \"bbox_end\": 165, \"encounter_dates\": [\"2026-01-23\"], \"department\": \"互联网医院门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四川省医学科学院四川省人民医院\n互联网门诊病历\n姓名\n性别：女\n年龄：62\n门诊科室：互联网医院门诊\n门诊病历号：0009922109\n工作单位或住址：四川省成都市邛崃市临邛街道\n联系电话：\n复诊记录\n记录时间：2026-01-23 13:20\n主诉：支气管哮喘\n简要病史：支气管哮喘\n既往病史：\n过敏史：\n流行病学史：无\n体格检查：无\n门诊诊断：支气管哮喘\n处理意见：无\n是否下转：否\n是否外伤：否\n是否美容：否\n是否体检：否\n燕海荣\n医师签名：",
    "role": "user"
  }
]
2026-08-10 11:52:31,455 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:52:31.455+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:52:33,082 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:52:33,082 INFO     29 [qwen-vl-text] LLM output (len=170):
{
  "encounter_date": "2026-01-23",
  "chief_complaint": "支气管哮喘",
  "present_illness": "支气管哮喘",
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": null
}
2026-08-10 11:52:33,082 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-23]
2026-08-10 11:52:33,085 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1107683, prompt_len=912
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["四川省医学科学院四川省人民医院", "互联网门诊病历", "姓名", "性别：女", "年龄：62", "门诊科室：互联网医院门诊", "门诊病历号：0009922109", "工作单位或住址：四川省成都市邛崃市临邛街道", "联系电话：", "复诊记录", "记录时间：2026-01-23 13:20", "主诉：支气管哮喘", "简要病史：支气管哮喘", "既往病史：", "过敏史：", "流行病学史：无", "体格检查：无", "门诊诊断：支气管哮喘", "处理意见：无", "是否下转：否", "是否外伤：否", "是否美容：否", "是否体检：否", "燕海荣", "医师签名："]

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
2026-08-10 11:52:48,057 INFO     29 [qwen-vl-text] coord API raw response (len=1311):
[
	{"text": "四川省医学科学院四川省人民医院", "bbox": [325, 317, 725, 339]},
	{"text": "互联网门诊病历", "bbox": [404, 338, 673, 358]},
	{"text": "姓名", "bbox": [60, 362, 93, 375]},
	{"text": "性别：女", "bbox": [189, 362, 258, 375]},
	{"text": "年龄：62", "bbox": [303, 362, 371, 375]},
	{"text": "门诊科室：互联网医院门诊", "bbox": [413, 362, 614, 375]},
	{"text": "门诊病历号：0009922109", "bbox": [658, 362, 841, 375]},
	{"text": "工作单位或住址：四川省成都市邛崃市临邛街道", "bbox": [60, 380, 421, 393]},
	{"text": "联系电话：", "bbox": [472, 380, 546, 393]},
	{"text": "复诊记录", "bbox": [269, 420, 338, 433]},
	{"text": "记录时间：2026-01-23 13:20", "bbox": [60, 440, 287, 453]},
	{"text": "主诉：支气管哮喘", "bbox": [60, 459, 233, 472]},
	{"text": "简要病史：支气管哮喘", "bbox": [60, 477, 233, 490]},
	{"text": "既往病史：", "bbox": [60, 496, 136, 509]},
	{"text": "过敏史：", "bbox": [60, 515, 136, 528]},
	{"text": "流行病学史：无", "bbox": [60, 534, 180, 547]},
	{"text": "体格检查：无", "bbox": [60, 553, 163, 566]},
	{"text": "门诊诊断：支气管哮喘", "bbox": [60, 571, 233, 584]},
	{"text": "处理意见：无", "bbox": [60, 591, 163, 604]},
	{"text": "是否下转：否", "bbox": [60, 610, 163, 623]},
	{"text": "是否外伤：否", "bbox": [60, 629, 163, 642]},
	{"text": "是否美容：否", "bbox": [60, 648, 163, 661]},
	{"text": "是否体检：否", "bbox": [60, 667, 163, 680]},
	{"text": "燕海荣", "bbox": [445, 642, 510, 661]},
	{"text": "医师签名：", "bbox": [467, 680, 540, 693]}
]
2026-08-10 11:52:48,057 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=15.0s
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[0]: text=四川省医学科学院四川省人民医院, bbox=[325, 317, 725, 339]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[1]: text=互联网门诊病历, bbox=[404, 338, 673, 358]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[60, 362, 93, 375]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[189, 362, 258, 375]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：62, bbox=[303, 362, 371, 375]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[5]: text=门诊科室：互联网医院门诊, bbox=[413, 362, 614, 375]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[6]: text=门诊病历号：0009922109, bbox=[658, 362, 841, 375]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[7]: text=工作单位或住址：四川省成都市邛崃市临邛街道, bbox=[60, 380, 421, 393]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[8]: text=联系电话：, bbox=[472, 380, 546, 393]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[9]: text=复诊记录, bbox=[269, 420, 338, 433]
2026-08-10 11:52:48,058 INFO     29 [qwen-vl-text] coord item[10]: text=记录时间：2026-01-23 13:20, bbox=[60, 440, 287, 453]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[11]: text=主诉：支气管哮喘, bbox=[60, 459, 233, 472]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[12]: text=简要病史：支气管哮喘, bbox=[60, 477, 233, 490]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[13]: text=既往病史：, bbox=[60, 496, 136, 509]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[14]: text=过敏史：, bbox=[60, 515, 136, 528]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[15]: text=流行病学史：无, bbox=[60, 534, 180, 547]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[16]: text=体格检查：无, bbox=[60, 553, 163, 566]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[17]: text=门诊诊断：支气管哮喘, bbox=[60, 571, 233, 584]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[18]: text=处理意见：无, bbox=[60, 591, 163, 604]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[19]: text=是否下转：否, bbox=[60, 610, 163, 623]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[20]: text=是否外伤：否, bbox=[60, 629, 163, 642]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[21]: text=是否美容：否, bbox=[60, 648, 163, 661]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[22]: text=是否体检：否, bbox=[60, 667, 163, 680]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[23]: text=燕海荣, bbox=[445, 642, 510, 661]
2026-08-10 11:52:48,059 INFO     29 [qwen-vl-text] coord item[24]: text=医师签名：, bbox=[467, 680, 540, 693]
2026-08-10 11:52:48,060 INFO     29 [qwen-vl-text] page=4 — 25/25 coords, api_time=15.0s
2026-08-10 11:52:48,060 INFO     29 [qwen-vl-text] new_positions (25):
[[4, 402.675, 898.2750000000001, 556.018, 594.606], [4, 500.55600000000004, 833.8470000000001, 592.852, 627.932], [4, 74.34, 115.227, 634.948, 657.75], [4, 234.17100000000002, 319.66200000000003, 634.948, 657.75], [4, 375.41700000000003, 459.66900000000004, 634.948, 657.75], [4, 511.70700000000005, 760.7460000000001, 634.948, 657.75], [4, 815.2620000000001, 1041.999, 634.948, 657.75], [4, 74.34, 521.619, 666.52, 689.322], [4, 584.808, 676.494, 666.52, 689.322], [4, 333.29100000000005, 418.78200000000004, 736.68, 759.482], [4, 74.34, 355.593, 771.76, 794.562], [4, 74.34, 288.687, 805.086, 827.888], [4, 74.34, 288.687, 836.658, 859.46], [4, 74.34, 168.50400000000002, 869.984, 892.7860000000001], [4, 74.34, 168.50400000000002, 903.31, 926.112], [4, 74.34, 223.02, 936.636, 959.438], [4, 74.34, 201.95700000000002, 969.962, 992.764], [4, 74.34, 288.687, 1001.534, 1024.336], [4, 74.34, 201.95700000000002, 1036.614, 1059.416], [4, 74.34, 201.95700000000002, 1069.94, 1092.742], [4, 74.34, 201.95700000000002, 1103.266, 1126.068], [4, 74.34, 201.95700000000002, 1136.592, 1159.394], [4, 74.34, 201.95700000000002, 1169.918, 1192.72], [4, 551.355, 631.8900000000001, 1126.068, 1159.394], [4, 578.613, 669.0600000000001, 1192.72, 1215.522]]
2026-08-10 11:52:48,060 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=17.0s
2026-08-10 11:52:48,061 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:52:48,070 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:52:48,070 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:52:48,070 INFO     29 [qwen-vl-text] positions(27): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:52:48,070 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [27]
2026-08-10 11:52:48,422 INFO     29 [qwen-vl-text] page=5, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:52:48,424 INFO     29 [qwen-vl-text] LLM extraction start, text_len=531
2026-08-10 11:52:48,424 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:52:48,425 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 167, \"bbox_end\": 193, \"encounter_dates\": [\"2025-12-29\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29 10:01:20 接诊年龄: 62岁\n闭环\n病历详情\n病历文档\n四川省醫學科學院·四川省人民醫院\n门诊病历\n姓名:\n性别: 女 年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109\n住址: 四川省成都******** 联系电话: 133****6101 挂号流水号: 64363836\n复诊记录\n记录时间: 2025-12-29 10:38\n主诉: 发作性喘息。\n简要病史: 哮喘复诊, 1周前吼喘一次持续3天, 自觉呼吸困难\n既往病史: 焦虑型抑郁症\n过敏史: 有过敏源\n流行病学\n史: /\n体格检查: 指尖氧饱和度95%, 心率78次/分\n门诊诊断: 哮喘急性发作、失眠\n处置: 血eos 0.4\n集采7*甲泼尼龙片(兴)(基)20mg/次 口服 每日1次 6天\n▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500)1泡/次 经口吸入 每日2次 31天\n阿育吠陀片(精2)(基)0.4mg/次 口服 每晚1次 20天\n血细胞分析(CBC+DIFF)\n婚姻史: 月经史:\n是否下转: 否, 是否外伤: 否, 是否美容: 否\n医师签名: 燕海荣",
    "role": "user"
  }
]
2026-08-10 11:52:51,282 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:52:51,282 INFO     29 [qwen-vl-text] LLM output (len=334):
{
  "encounter_date": "2025-12-29",
  "chief_complaint": "发作性喘息。",
  "present_illness": "哮喘复诊, 1周前吼喘一次持续3天, 自觉呼吸困难",
  "past_history": "焦虑型抑郁症",
  "diagnosis": "哮喘急性发作、失眠",
  "treatment_plan": [
    "集采7*甲泼尼龙片(兴)(基) 20mg/次 口服 每日1次 6天",
    "沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1泡/次 经口吸入 每日2次 31天",
    "阿育吠陀片(精2)(基) 0.4mg/次 口服 每晚1次 20天"
  ]
}
2026-08-10 11:52:51,282 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-29]
2026-08-10 11:52:51,285 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1062495, prompt_len=1225
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29 10:01:20 接诊年龄: 62岁", "闭环", "病历详情", "病历文档", "四川省醫學科學院·四川省人民醫院", "门诊病历", "姓名:", "性别: 女 年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109", "住址: 四川省成都******** 联系电话: 133****6101 挂号流水号: 64363836", "复诊记录", "记录时间: 2025-12-29 10:38", "主诉: 发作性喘息。", "简要病史: 哮喘复诊, 1周前吼喘一次持续3天, 自觉呼吸困难", "既往病史: 焦虑型抑郁症", "过敏史: 有过敏源", "流行病学", "史: /", "体格检查: 指尖氧饱和度95%, 心率78次/分", "门诊诊断: 哮喘急性发作、失眠", "处置: 血eos 0.4", "集采7*甲泼尼龙片(兴)(基)20mg/次 口服 每日1次 6天", "▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500)1泡/次 经口吸入 每日2次 31天", "阿育吠陀片(精2)(基)0.4mg/次 口服 每晚1次 20天", "血细胞分析(CBC+DIFF)", "婚姻史: 月经史:", "是否下转: 否, 是否外伤: 否, 是否美容: 否", "医师签名: 燕海荣"]

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
2026-08-10 11:53:13,859 INFO     29 [qwen-vl-text] coord API raw response (len=2549):
[
	{"text": "流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29 10:01:20 接诊年龄: 62岁", "bbox": [0, 340, 411, 351]},
	{"text": "闭环", "bbox": [933, 338, 967, 352], "bbox": [933, 338, 967, 352]},
	{"text": "病历详情", "bbox": [58, 365, 100, 374], "bbox": [58, 365, 100, 374]},
	{"text": "病历文档", "bbox": [126, 365, 167, 374], "bbox": [126, 365, 167, 374]},
	{"text": "四川省醫學科學院·四川省人民醫院", "bbox": [462, 400, 655, 410], "bbox": [462, 400, 655, 410]},
	{"text": "门诊病历", "bbox": [506, 414, 579, 424], "bbox": [506, 414, 579, 424]},
	{"text": "姓名:", "bbox": [58, 429, 85, 438], "bbox": [58, 429, 85, 438]},
	{"text": "性别: 女 年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109", "bbox": [114, 429, 471, 438], "bbox": [114, 429, 471, 438]},
	{"text": "住址: 四川省成都******** 联系电话: 133****6101 挂号流水号: 64363836", "bbox": [58, 442, 385, 451], "bbox": [58, 442, 385, 451]},
	{"text": "复诊记录", "bbox": [516, 457, 565, 466], "bbox": [516, 457, 565, 466]},
	{"text": "记录时间: 2025-12-29 10:38", "bbox": [60, 471, 197, 479], "bbox": [60, 471, 197, 479]},
	{"text": "主诉: 发作性喘息。", "bbox": [60, 486, 168, 494], "bbox": [60, 486, 168, 494]},
	{"text": "简要病史: 哮喘复诊, 1周前吼喘一次持续3天, 自觉呼吸困难", "bbox": [60, 500, 326, 508], "bbox": [60, 500, 326, 508]},
	{"text": "既往病史: 焦虑型抑郁症", "bbox": [60, 515, 174, 523], "bbox": [60, 515, 174, 523]},
	{"text": "过敏史: 有过敏源", "bbox": [60, 536, 155, 544], "bbox": [60, 536, 155, 544]},
	{"text": "流行病学", "bbox": [60, 551, 100, 559], "bbox": [60, 551, 100, 559]},
	{"text": "史: /", "bbox": [60, 557, 123, 565], "bbox": [60, 557, 123, 565]},
	{"text": "体格检查: 指尖氧饱和度95%, 心率78次/分", "bbox": [60, 571, 254, 579], "bbox": [60, 571, 254, 579]},
	{"text": "门诊诊断: 哮喘急性发作、失眠", "bbox": [60, 586, 201, 594], "bbox": [60, 586, 201, 594]},
	{"text": "处置: 血eos 0.4", "bbox": [60, 601, 158, 609], "bbox": [60, 601, 158, 609]},
	{"text": "集采7*甲泼尼龙片(兴)(基)20mg/次 口服 每日1次 6天", "bbox": [117, 613, 340, 621], "bbox": [117, 613, 340, 621]},
	{"text": "▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500)1泡/次 经口吸入 每日2次 31天", "bbox": [117, 618, 448, 626], "bbox": [117, 618, 448, 626]},
	{"text": "阿育吠陀片(精2)(基)0.4mg/次 口服 每晚1次 20天", "bbox": [117, 624, 324, 631], "bbox": [117, 624, 324, 631]},
	{"text": "血细胞分析(CBC+DIFF)", "bbox": [117, 629, 214, 637], "bbox": [117, 629, 214, 637]},
	{"text": "婚姻史: 月经史:", "bbox": [58, 642, 131, 650], "bbox": [58, 642, 131, 650]},
	{"text": "是否下转: 否, 是否外伤: 否, 是否美容: 否", "bbox": [58, 654, 257, 662], "bbox": [58, 654, 257, 662]},
	{"text": "医师签名: 燕海荣", "bbox": [899, 667, 998, 680], "bbox": [899, 667, 998, 680]},
	{"text": "共2页, 第2页", "bbox": [58, 686, 128, 694], "bbox": [58, 686, 128, 694]}
]
2026-08-10 11:53:13,859 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=22.6s
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[0]: text=流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29 10:01:20 接诊年龄: 62岁, bbox=[0, 340, 411, 351]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[1]: text=闭环, bbox=[933, 338, 967, 352]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[2]: text=病历详情, bbox=[58, 365, 100, 374]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[3]: text=病历文档, bbox=[126, 365, 167, 374]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[4]: text=四川省醫學科學院·四川省人民醫院, bbox=[462, 400, 655, 410]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[5]: text=门诊病历, bbox=[506, 414, 579, 424]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[6]: text=姓名:, bbox=[58, 429, 85, 438]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[7]: text=性别: 女 年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109, bbox=[114, 429, 471, 438]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[8]: text=住址: 四川省成都******** 联系电话: 133****6101 挂号流水号: 64363836, bbox=[58, 442, 385, 451]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[9]: text=复诊记录, bbox=[516, 457, 565, 466]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[10]: text=记录时间: 2025-12-29 10:38, bbox=[60, 471, 197, 479]
2026-08-10 11:53:13,860 INFO     29 [qwen-vl-text] coord item[11]: text=主诉: 发作性喘息。, bbox=[60, 486, 168, 494]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[12]: text=简要病史: 哮喘复诊, 1周前吼喘一次持续3天, 自觉呼吸困难, bbox=[60, 500, 326, 508]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[13]: text=既往病史: 焦虑型抑郁症, bbox=[60, 515, 174, 523]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[14]: text=过敏史: 有过敏源, bbox=[60, 536, 155, 544]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[15]: text=流行病学, bbox=[60, 551, 100, 559]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[16]: text=史: /, bbox=[60, 557, 123, 565]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[17]: text=体格检查: 指尖氧饱和度95%, 心率78次/分, bbox=[60, 571, 254, 579]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[18]: text=门诊诊断: 哮喘急性发作、失眠, bbox=[60, 586, 201, 594]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[19]: text=处置: 血eos 0.4, bbox=[60, 601, 158, 609]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[20]: text=集采7*甲泼尼龙片(兴)(基)20mg/次 口服 每日1次 6天, bbox=[117, 613, 340, 621]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[21]: text=▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500)1泡/次 经口吸入 每日2次 31天, bbox=[117, 618, 448, 626]
2026-08-10 11:53:13,861 INFO     29 [qwen-vl-text] coord item[22]: text=阿育吠陀片(精2)(基)0.4mg/次 口服 每晚1次 20天, bbox=[117, 624, 324, 631]
2026-08-10 11:53:13,862 INFO     29 [qwen-vl-text] coord item[23]: text=血细胞分析(CBC+DIFF), bbox=[117, 629, 214, 637]
2026-08-10 11:53:13,862 INFO     29 [qwen-vl-text] coord item[24]: text=婚姻史: 月经史:, bbox=[58, 642, 131, 650]
2026-08-10 11:53:13,862 INFO     29 [qwen-vl-text] coord item[25]: text=是否下转: 否, 是否外伤: 否, 是否美容: 否, bbox=[58, 654, 257, 662]
2026-08-10 11:53:13,862 INFO     29 [qwen-vl-text] coord item[26]: text=医师签名: 燕海荣, bbox=[899, 667, 998, 680]
2026-08-10 11:53:13,862 INFO     29 [qwen-vl-text] coord item[27]: text=共2页, 第2页, bbox=[58, 686, 128, 694]
2026-08-10 11:53:13,862 INFO     29 [qwen-vl-text] page=5 — 27/27 coords, api_time=22.6s
2026-08-10 11:53:13,863 INFO     29 [qwen-vl-text] new_positions (27):
[[5, 0.0, 509.22900000000004, 596.36, 615.654], [5, 1155.987, 1198.113, 592.852, 617.408], [5, 71.86200000000001, 123.9, 640.21, 655.996], [5, 156.114, 206.913, 640.21, 655.996], [5, 572.418, 811.5450000000001, 701.6, 719.14], [5, 626.9340000000001, 717.3810000000001, 726.156, 743.696], [5, 71.86200000000001, 105.31500000000001, 752.466, 768.252], [5, 141.246, 583.5690000000001, 752.466, 768.252], [5, 71.86200000000001, 477.01500000000004, 775.268, 791.054], [5, 639.3240000000001, 700.0350000000001, 801.578, 817.364], [5, 74.34, 244.08300000000003, 826.134, 840.166], [5, 74.34, 208.15200000000002, 852.444, 866.476], [5, 74.34, 403.91400000000004, 877.0, 891.032], [5, 74.34, 215.586, 903.31, 917.342], [5, 74.34, 192.04500000000002, 940.144, 954.176], [5, 74.34, 123.9, 966.454, 980.486], [5, 74.34, 152.39700000000002, 976.978, 991.01], [5, 74.34, 314.706, 1001.534, 1015.566], [5, 74.34, 249.03900000000002, 1027.844, 1041.876], [5, 74.34, 195.76200000000003, 1054.154, 1068.186], [5, 144.96300000000002, 421.26000000000005, 1075.202, 1089.234], [5, 144.96300000000002, 555.072, 1083.972, 1098.004], [5, 144.96300000000002, 401.43600000000004, 1094.496, 1106.7740000000001], [5, 144.96300000000002, 265.146, 1103.266, 1117.298], [5, 71.86200000000001, 162.30900000000003, 1126.068, 1140.1], [5, 71.86200000000001, 318.423, 1147.116, 1161.148], [5, 1113.861, 1236.5220000000002, 1169.918, 1192.72]]
2026-08-10 11:53:13,863 INFO     29 [qwen-vl-text] ═══ DONE ═══ 27 positions, pages=1, time=25.8s
2026-08-10 11:53:13,863 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:53:13,865 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:53:13,865 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:53:13,865 INFO     29 [qwen-vl-text] positions(27): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:53:13,866 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [27]
2026-08-10 11:53:14,374 INFO     29 [qwen-vl-text] page=8, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:53:14,376 INFO     29 [qwen-vl-text] LLM extraction start, text_len=979
2026-08-10 11:53:14,376 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:53:14,376 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 280, \"bbox_end\": 306, \"encounter_dates\": [\"2025-12-09\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "就诊类型: 门诊\n就诊时间: 2025-12-09 17:00:36\n接诊年龄: 62岁\n闭环\n病历详情\n病历文档\n四川省醫學科學院·四川省人民醫院\n门诊病历\n姓名:\n性别: 女年龄: 62岁门诊科室: 呼吸与危重症医学科门诊门诊病历号: 0009922109\n住址: 四川省成都市邛崃市联系电话: 133****6101挂号流水号: 63931786\n复诊记录\n记录时间: 2025-12-09 17:00\n主诉: 发作性喘息, 参加LOGOS (D5982C00008) 临床研究, 今日行电话回访。\n简要病史: 哮喘病史\n既往病史: 焦虑型抑郁症\n过敏史: 有过敏源花粉过敏, 未见报告, 具体不详\n流行病学史: /\n体格检查: NA\n门诊诊断: 哮喘\n处置: 今日15:35对受试者行电话回访, 受试者电话: 133****6101, 感谢受试者参加有关布地奈德、格隆溴铵和富马酸福莫特罗吸入器 (也简称为BGFMDI或PT010) 的临床试验, 该临床试验是一项双盲研究, 在所有临床试验受试者的通力配合下, 研究人员正在查明此药物是否有助于治疗哮喘患者。试验开始时, 受试者已经知道会接受BGF MDI、布地奈德和富马酸福莫特罗 (也简称为BFF MDI) 或Symbicort, 接受BGF MDI或BFF MDI的参加者也接受了看起来像Symbicort的安慰剂吸入器。接受了Symbicort的参加者还接受了看起来BGF MDI和BFF MDI的安慰剂吸入器, 安慰剂外观像研究治疗药物, 但其中不含任何药物。患者也知道, 任何人 (包括研究者和试验工作人员在内) 在试验结束之前都不知道您接受的是哪种治疗。\n告知受试者本试验已结束, 可告知患者接受的是布地奈德和富马酸福莫特罗定量吸入器 (BFF MDI), 受试者无疑问, 嘱受试者注意休息, 避免受凉感冒, 行肺功能锻炼, 病情加重时及时就诊。\n告知受试者可以通过trialsunmaries.com网站在线查看总体研究结果的摘要, 可使用D5982C00008在上述网站搜索本试验, 此网站不会收集、储存或使用可用于识别受试者的身份信息, 该摘要将为受试者介绍本试验的总体结果。\n婚烟史: 月经史:\n是否下转: 否。是否外伤: 否。是否美容: 否\n共2页, 第2页\n医师签名: 张利",
    "role": "user"
  }
]
2026-08-10 11:53:14,378 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:53:14.377+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:53:16,754 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:53:16,754 INFO     29 [qwen-vl-text] LLM output (len=242):
{
  "encounter_date": "2025-12-09",
  "chief_complaint": "发作性喘息, 参加LOGOS (D5982C00008) 临床研究, 今日行电话回访。",
  "present_illness": "哮喘病史",
  "past_history": "焦虑型抑郁症",
  "diagnosis": "哮喘",
  "treatment_plan": "嘱受试者注意休息, 避免受凉感冒, 行肺功能锻炼, 病情加重时及时就诊。"
}
2026-08-10 11:53:16,754 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-09]
2026-08-10 11:53:16,768 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3492899, prompt_len=1673
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["就诊类型: 门诊", "就诊时间: 2025-12-09 17:00:36", "接诊年龄: 62岁", "闭环", "病历详情", "病历文档", "四川省醫學科學院·四川省人民醫院", "门诊病历", "姓名:", "性别: 女年龄: 62岁门诊科室: 呼吸与危重症医学科门诊门诊病历号: 0009922109", "住址: 四川省成都市邛崃市联系电话: 133****6101挂号流水号: 63931786", "复诊记录", "记录时间: 2025-12-09 17:00", "主诉: 发作性喘息, 参加LOGOS (D5982C00008) 临床研究, 今日行电话回访。", "简要病史: 哮喘病史", "既往病史: 焦虑型抑郁症", "过敏史: 有过敏源花粉过敏, 未见报告, 具体不详", "流行病学史: /", "体格检查: NA", "门诊诊断: 哮喘", "处置: 今日15:35对受试者行电话回访, 受试者电话: 133****6101, 感谢受试者参加有关布地奈德、格隆溴铵和富马酸福莫特罗吸入器 (也简称为BGFMDI或PT010) 的临床试验, 该临床试验是一项双盲研究, 在所有临床试验受试者的通力配合下, 研究人员正在查明此药物是否有助于治疗哮喘患者。试验开始时, 受试者已经知道会接受BGF MDI、布地奈德和富马酸福莫特罗 (也简称为BFF MDI) 或Symbicort, 接受BGF MDI或BFF MDI的参加者也接受了看起来像Symbicort的安慰剂吸入器。接受了Symbicort的参加者还接受了看起来BGF MDI和BFF MDI的安慰剂吸入器, 安慰剂外观像研究治疗药物, 但其中不含任何药物。患者也知道, 任何人 (包括研究者和试验工作人员在内) 在试验结束之前都不知道您接受的是哪种治疗。", "告知受试者本试验已结束, 可告知患者接受的是布地奈德和富马酸福莫特罗定量吸入器 (BFF MDI), 受试者无疑问, 嘱受试者注意休息, 避免受凉感冒, 行肺功能锻炼, 病情加重时及时就诊。", "告知受试者可以通过trialsunmaries.com网站在线查看总体研究结果的摘要, 可使用D5982C00008在上述网站搜索本试验, 此网站不会收集、储存或使用可用于识别受试者的身份信息, 该摘要将为受试者介绍本试验的总体结果。", "婚烟史: 月经史:", "是否下转: 否。是否外伤: 否。是否美容: 否", "共2页, 第2页", "医师签名: 张利"]

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
2026-08-10 11:53:37,302 INFO     29 [qwen-vl-text] coord API raw response (len=2143):
[
	{"text": "就诊类型: 门诊", "bbox": [50, 467, 120, 476]},
	{"text": "就诊时间: 2025-12-09 17:00:36", "bbox": [134, 467, 280, 476]},
	{"text": "接诊年龄: 62岁", "bbox": [292, 467, 364, 476]},
	{"text": "闭环", "bbox": [888, 464, 924, 479]},
	{"text": "病历详情", "bbox": [10, 491, 52, 500]},
	{"text": "病历文档", "bbox": [78, 491, 120, 500]},
	{"text": "四川省醫學科學院·四川省人民醫院", "bbox": [416, 521, 610, 532]},
	{"text": "门诊病历", "bbox": [461, 535, 534, 546]},
	{"text": "姓名:", "bbox": [10, 551, 35, 560]},
	{"text": "性别: 女年龄: 62岁门诊科室: 呼吸与危重症医学科门诊门诊病历号: 0009922109", "bbox": [63, 551, 426, 560]},
	{"text": "住址: 四川省成都市邛崃市联系电话: 133****6101挂号流水号: 63931786", "bbox": [10, 564, 342, 573]},
	{"text": "复诊记录", "bbox": [473, 579, 521, 589]},
	{"text": "记录时间: 2025-12-09 17:00", "bbox": [13, 594, 150, 603]},
	{"text": "主诉: 发作性喘息, 参加LOGOS (D5982C00008) 临床研究, 今日行电话回访。", "bbox": [13, 610, 376, 619]},
	{"text": "简要病史: 哮喘病史", "bbox": [13, 626, 108, 635]},
	{"text": "既往病史: 焦虑型抑郁症", "bbox": [13, 641, 127, 650]},
	{"text": "过敏史: 有过敏源花粉过敏, 未见报告, 具体不详", "bbox": [13, 662, 242, 671]},
	{"text": "流行病学史: /", "bbox": [13, 677, 75, 691]},
	{"text": "体格检查: NA", "bbox": [13, 699, 86, 708]},
	{"text": "门诊诊断: 哮喘", "bbox": [13, 714, 90, 723]},
	{"text": "处置: 今日15:35对受试者行电话回访, 受试者电话: 133****6101, 感谢受试者参加有关布地奈德、格隆溴铵和富马酸福莫特罗吸入器 (也简称为BGFMDI或PT010) 的临床试验, 该临床试验是一项双盲研究, 在所有临床试验受试者的通力配合下, 研究人员正在查明此药物是否有助于治疗哮喘患者。试验开始时, 受试者已经知道会接受BGF MDI、布地奈德和富马酸福莫特罗 (也简称为BFF MDI) 或Symbicort, 接受BGF MDI或BFF MDI的参加者也接受了看起来像Symbicort的安慰剂吸入器。接受了Symbicort的参加者还接受了看起来BGF MDI和BFF MDI的安慰剂吸入器, 安慰剂外观像研究治疗药物, 但其中不含任何药物。患者也知道, 任何人 (包括研究者和试验工作人员在内) 在试验结束之前都不知道您接受的是哪种治疗。", "bbox": [13, 730, 508, 773]},
	{"text": "告知受试者本试验已结束, 可告知患者接受的是布地奈德和富马酸福莫特罗定量吸入器 (BFF MDI), 受试者无疑问, 嘱受试者注意休息, 避免受凉感冒, 行肺功能锻炼, 病情加重时及时就诊。", "bbox": [70, 777, 506, 790]},
	{"text": "告知受试者可以通过trialsunmaries.com网站在线查看总体研究结果的摘要, 可使用D5982C00008在上述网站搜索本试验, 此网站不会收集、储存或使用可用于识别受试者的身份信息, 该摘要将为受试者介绍本试验的总体结果。", "bbox": [70, 795, 502, 815]},
	{"text": "婚烟史: 月经史:", "bbox": [13, 821, 84, 830]},
	{"text": "是否下转: 否。是否外伤: 否。是否美容: 否", "bbox": [13, 833, 212, 842]},
	{"text": "共2页, 第2页", "bbox": [13, 868, 81, 877]},
	{"text": "医师签名: 张利", "bbox": [874, 846, 977, 860]}
]
2026-08-10 11:53:37,302 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=20.5s
2026-08-10 11:53:37,302 INFO     29 [qwen-vl-text] coord item[0]: text=就诊类型: 门诊, bbox=[50, 467, 120, 476]
2026-08-10 11:53:37,302 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间: 2025-12-09 17:00:36, bbox=[134, 467, 280, 476]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[2]: text=接诊年龄: 62岁, bbox=[292, 467, 364, 476]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[3]: text=闭环, bbox=[888, 464, 924, 479]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[4]: text=病历详情, bbox=[10, 491, 52, 500]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[5]: text=病历文档, bbox=[78, 491, 120, 500]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[6]: text=四川省醫學科學院·四川省人民醫院, bbox=[416, 521, 610, 532]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[7]: text=门诊病历, bbox=[461, 535, 534, 546]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[8]: text=姓名:, bbox=[10, 551, 35, 560]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[9]: text=性别: 女年龄: 62岁门诊科室: 呼吸与危重症医学科门诊门诊病历号: 0009922109, bbox=[63, 551, 426, 560]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[10]: text=住址: 四川省成都市邛崃市联系电话: 133****6101挂号流水号: 63931786, bbox=[10, 564, 342, 573]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[11]: text=复诊记录, bbox=[473, 579, 521, 589]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[12]: text=记录时间: 2025-12-09 17:00, bbox=[13, 594, 150, 603]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[13]: text=主诉: 发作性喘息, 参加LOGOS (D5982C00008) 临床研究, 今日行电话回访。, bbox=[13, 610, 376, 619]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[14]: text=简要病史: 哮喘病史, bbox=[13, 626, 108, 635]
2026-08-10 11:53:37,303 INFO     29 [qwen-vl-text] coord item[15]: text=既往病史: 焦虑型抑郁症, bbox=[13, 641, 127, 650]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[16]: text=过敏史: 有过敏源花粉过敏, 未见报告, 具体不详, bbox=[13, 662, 242, 671]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[17]: text=流行病学史: /, bbox=[13, 677, 75, 691]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[18]: text=体格检查: NA, bbox=[13, 699, 86, 708]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[19]: text=门诊诊断: 哮喘, bbox=[13, 714, 90, 723]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[20]: text=处置: 今日15:35对受试者行电话回访, 受试者电话: 133****6101, 感谢受试者参加有关布地奈德、格隆溴铵和富马酸福莫特罗吸入器 (也简称为BGFMDI或PT010) 的临床试验, 该临床试验是一项双盲研究, 在所有临床试验受试者的通力配合下, 研究人员正在查明此药物是否有助于治疗哮喘患者。试验开始时, 受试者已经知道会接受BGF MDI、布地奈德和富马酸福莫特罗 (也简称为BFF MDI) 或Symbicort, 接受BGF MDI或BFF MDI的参加者也接受了看起来像Symbicort的安慰剂吸入器。接受了Symbicort的参加者还接受了看起来BGF MDI和BFF MDI的安慰剂吸入器, 安慰剂外观像研究治疗药物, 但其中不含任何药物。患者也知道, 任何人 (包括研究者和试验工作人员在内) 在试验结束之前都不知道您接受的是哪种治疗。, bbox=[13, 730, 508, 773]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[21]: text=告知受试者本试验已结束, 可告知患者接受的是布地奈德和富马酸福莫特罗定量吸入器 (BFF MDI), 受试者无疑问, 嘱受试者注意休息, 避免受凉感冒, 行肺功能锻炼, 病情加重时及时就诊。, bbox=[70, 777, 506, 790]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[22]: text=告知受试者可以通过trialsunmaries.com网站在线查看总体研究结果的摘要, 可使用D5982C00008在上述网站搜索本试验, 此网站不会收集、储存或使用可用于识别受试者的身份信息, 该摘要将为受试者介绍本试验的总体结果。, bbox=[70, 795, 502, 815]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[23]: text=婚烟史: 月经史:, bbox=[13, 821, 84, 830]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[24]: text=是否下转: 否。是否外伤: 否。是否美容: 否, bbox=[13, 833, 212, 842]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[25]: text=共2页, 第2页, bbox=[13, 868, 81, 877]
2026-08-10 11:53:37,304 INFO     29 [qwen-vl-text] coord item[26]: text=医师签名: 张利, bbox=[874, 846, 977, 860]
2026-08-10 11:53:37,306 INFO     29 [qwen-vl-text] page=8 — 27/27 coords, api_time=20.5s
2026-08-10 11:53:37,307 INFO     29 [qwen-vl-text] new_positions (27):
[[8, 61.95, 148.68, 819.118, 834.904], [8, 166.026, 346.92, 819.118, 834.904], [8, 361.788, 450.99600000000004, 819.118, 834.904], [8, 1100.2320000000002, 1144.836, 813.856, 840.166], [8, 12.39, 64.42800000000001, 861.214, 877.0], [8, 96.64200000000001, 148.68, 861.214, 877.0], [8, 515.4240000000001, 755.7900000000001, 913.834, 933.128], [8, 571.1790000000001, 661.6260000000001, 938.39, 957.684], [8, 12.39, 43.365, 966.454, 982.24], [8, 78.057, 527.8140000000001, 966.454, 982.24], [8, 12.39, 423.73800000000006, 989.256, 1005.042], [8, 586.047, 645.519, 1015.566, 1033.106], [8, 16.107000000000003, 185.85000000000002, 1041.876, 1057.662], [8, 16.107000000000003, 465.86400000000003, 1069.94, 1085.726], [8, 16.107000000000003, 133.812, 1098.004, 1113.79], [8, 16.107000000000003, 157.353, 1124.314, 1140.1], [8, 16.107000000000003, 299.838, 1161.148, 1176.934], [8, 16.107000000000003, 92.92500000000001, 1187.458, 1212.014], [8, 16.107000000000003, 106.554, 1226.046, 1241.832], [8, 16.107000000000003, 111.51, 1252.356, 1268.142], [8, 16.107000000000003, 629.412, 1280.42, 1355.842], [8, 86.73, 626.9340000000001, 1362.858, 1385.66], [8, 86.73, 621.9780000000001, 1394.43, 1429.51], [8, 16.107000000000003, 104.07600000000001, 1440.034, 1455.82], [8, 16.107000000000003, 262.668, 1461.082, 1476.868], [8, 16.107000000000003, 100.35900000000001, 1522.472, 1538.258], [8, 1082.8860000000002, 1210.5030000000002, 1483.884, 1508.44]]
2026-08-10 11:53:37,307 INFO     29 [qwen-vl-text] ═══ DONE ═══ 27 positions, pages=1, time=23.4s
2026-08-10 11:53:37,307 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:53:37,319 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:53:37,319 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:53:37,319 INFO     29 [qwen-vl-text] positions(103): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:53:37,319 INFO     29 [qwen-vl-text] page grouping: [10, 11, 12, 13], lines per page: [30, 32, 27, 14]
2026-08-10 11:53:38,014 INFO     29 [qwen-vl-text] page=10, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:53:38,633 INFO     29 [qwen-vl-text] page=11, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:53:39,232 INFO     29 [qwen-vl-text] page=12, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:53:39,565 INFO     29 [qwen-vl-text] page=13, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:53:39,567 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3190
2026-08-10 11:53:39,567 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:53:39,568 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 345, \"bbox_end\": 447, \"encounter_dates\": [\"2024-04-15\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四川省医学科学院·四川省人民医院\n门诊病历\n姓名：\n性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667\n复诊记录\n记录时间：2024-04-15 09:26\n主诉：发作性喘息，参加LOGOS（D5982C00008）临床研究，行V1访视\n简要病史：患者今日7:40到院，自诉：哮喘病史：于2022年5月UK日首次出现哮喘症状，于2022年5月16日首次\n确诊为哮喘，2024年1月15日开始规范使用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次\n经口吸入 每日2次，控制症状，近一年未发生急性加重。\n既往病史：焦虑型抑郁症：2021年2月UK日-至今，采取以下药物治疗：\n草酸艾司西酞普兰片：2022年2月UK日-至今，20mg/次，qd；\n枸橼酸坦度螺酮胶囊：2022年2月UK日-至今，10mg/次，tid。\n过敏史：有过敏源花粉 因患者无法记得开始时间，故开始时间不详\n流行病学史：此前3个月内，患者无可能相关的视力变化；否认青光眼史；患者不存在具有临床意义的症性前列腺肥大或膀胱颈梗阻\n/尿潴留；患者在此前5年内不存在未完全缓解的不可切除的癌症，患者未在既往或当前在任何布地奈德和富马酸福莫特\n罗研究(PT009)，布地奈德、格隆安和富马酸福莫特罗(PT010)或格隆安(PT001)中接受随机化；患者无计划研究期间住院，\n患者否认访视前1个月内住过院，否认访视前4周内完成对呼吸道感染或哮喘急性发作的全身性激素治疗，否认有危机\n生命的哮喘，否认访视1前12个月内已知有药物滥用或酗酒史，否认对β2-激动剂、激素、抗胆碱药或MDI或pMDI中的\n任何组分发生超敏反应，否认既往或当前入组AEROSPHERE项目中的研究。\n体格检查：神志清楚，精神尚可，呼吸平稳，全身皮肤无黄染，无瘀点、瘀斑，皮肤皮温不高，皮肤无汗湿。浅表淋巴结\n未触及，头颅五官无畸形，眼球活动自如，睑结膜无充血苍白，球结膜无水肿，巩膜无黄染。口唇无发绀，\n伸舌居中，咽无充血，双侧扁桃体无肿大。颈软，颈静脉充盈，气管居中，甲状腺未扪及肿大。桶状胸，\n双肺呼吸音降低，双肺未闻及明显湿性啰音及哮鸣音。心界无明显增大，律齐，各瓣膜区未闻测量血\n共4页，第1页\n四川省医学科学院·四川省人民医院\n门诊病历\n姓名：马蓉 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667\n四川省医学科学院·四川省人民医院\n门诊病历\n姓名：\n性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n住址：四川省成都市邛崃市 联系电话：\n挂号流水号：49735667\n压）及病理性杂音。腹软，无压痛、反跳痛及肌紧张，肝脾肋下未触及，肝肾区无叩痛，肠鸣音不活跃。\n双下肢对称无明显水肿，四肢肌力及肌张力正常。生命体征详见生命体征表（受试者已在休息5分钟后\n取坐位）\n门诊诊断：\n哮喘\n处\n置：\n知情过程：根据患者已有既往资料的情况，考虑受试者可能符合“一项随机、双盲、双模拟、平行分组、\n多中心、24至52周可变时长的研究，评估布地奈德、格隆铵和富马酸福莫特罗定量吸入器（MDI）与布地\n奈德和富马酸福莫特罗MDI以及信必可®加压MDI相比在哮喘未充分控制的成人和青少年受试者中的疗\n效和安全性（LOGOS）”的临床试验，今日7时55分当面与患者本人及家属进行充分知情，详细讲解本研究\n的目的、方法、流程及可能的获益及风险，并给予患者充分的时间考虑，患者仔细阅读无疑问，自愿同意\n参加本项临床试验，于2024年4月15日8时15分与患者本人共同签署两份成人研究受试者主要信息\n和知情同意书（研究信息和知情同意书）（研究中心版本号1429-2.0，研究中心版本日期：2023年10月\n31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日当面与患者本人详细讲解中国个人\n信息保护附录相关内容，患者表示无疑问并充分理解接受，于2024年4月15日8时18分签署两份中国\n个人信息保护附录（中国个人信息保护附录）（研究中心版本号1429-2.0 研究中心版本日期2023年10\n月31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日同时告知患者12小时PFT子研\n究者相关内容，患者表示拒绝。\n人口统计学信息：出生日期：1963年8月16日 性别：女 民族：汉族 种族：中国人\n患者否认哮喘相关家族史，否认吸烟及饮酒，自诉无输血史及手术史，患者目前已绝经（经期：开始时间：\n1978年，结束时间：2014年）。\n疫苗接种史：目前已无法查询新冠疫苗接种史，患者自诉2021年-2022年期间接种三针（具体相关信息\n无法提供）\n共4页，第2页\n12\n四川省医学科学院·四川省人民医院\n门诊病历\n姓名：\n性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667\n询问患者最近一次进食时间，患者自诉19:10，今与患者确认测量前6小时内未使用SABA类药物，并确认前一晚吸入沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次 经口吸入 每日2次 时间为\n20:00，至今未使用任何药物。\n患者静息10分钟后以仰卧位行12导联ECG检查，详见ECG报告。在肺功能测量前进行FoNO检测，检测一小时前无饮水及进食，随后行给药前-60min、-30min肺功能检查，患者者给药前FEV1%：78.85%。\n检查结果详见报告。\n完成ACQ-6及ACQ-7问卷，ACQ-7评分≥1.5。\n患者性别：女，已绝经，故未使用中心试验室提供的试剂进行尿妊娠试验。\n采集血样；完成血液标本采集后进行处理，并送往中心实验室进行检测。\n患者目前符合所有入选标准，不符合任一排除标准，嘱患者自今日起停用沙美特罗替卡松吸入粉雾剂\n|舒利迭(兴)(50ug/250ug)1泡/次 经口吸入 每日2次。IRT系统登记，筛选号；E1429021，并获得培训\n装置1瓶，药物编号：117165-EQ；获得导入期BFP1瓶，药物编号为；661331-BD。使用培训装置对患者进行\n吸入器使用培训及检查吸入装置技术，完成给药培训后当场回收；于11:08指导患者对导入期BFP进行\n预喷并给药2喷，给药结束时间为：11:10。发放急救药物万托林1瓶，嘱患者必要时使用。\n发放ePRO设备和峰流速仪，协助患者完成使用培训，同时发放白色吸入器使用指南，受试者参与卡。\n受试者感谢卡、哮喘监测仪AMS患者快速入门指南、峰流速计AM3使用指南，手持设备患者快速指南。\n预约患者下周一来院进行下次访视；\n嘱患者带上发放的峰速仪、ePRO以及导入期药物；\n嘱患者带上自上次访视以来的住院、门诊、急诊等病历记录；\n嘱患者下次访视前急救药物沙丁胺醇暂停≥6小时；\n嘱患者下次访视前早间剂量必须暂停，直至完成当此访视所有给药前评价；\n嘱患者按要求清洗给药装置；\n共4页，第3页\n13\n四川省医学科学院·四川省人民医院\n门诊病历\n姓名：\n性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109\n住址：四川省成都市邛崃市 联系电话：\n挂号流水号：49735667\n嘱患者用药期间如有任何不适，及时复诊。\n婚姻史：\n月经史：\n是否下转： 否\n是否外伤：否\n是否美容： 否\n医师签名： 燕海荣\n共4页，第4页",
    "role": "user"
  }
]
2026-08-10 11:53:46,192 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:53:46.191+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:53:48,292 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:53:48,293 INFO     29 [qwen-vl-text] LLM output (len=1155):
{
  "encounter_date": "2024-04-15",
  "chief_complaint": "发作性喘息，参加LOGOS（D5982C00008）临床研究，行V1访视",
  "present_illness": "患者今日7:40到院，自诉：哮喘病史：于2022年5月UK日首次出现哮喘症状，于2022年5月16日首次确诊为哮喘，2024年1月15日开始规范使用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次经口吸入 每日2次，控制症状，近一年未发生急性加重。",
  "past_history": "焦虑型抑郁症：2021年2月UK日-至今，采取以下药物治疗：草酸艾司西酞普兰片：2022年2月UK日-至今，20mg/次，qd；枸橼酸坦度螺酮胶囊：2022年2月UK日-至今，10mg/次，tid。过敏史：有过敏源花粉 因患者无法记得开始时间，故开始时间不详。流行病学史：此前3个月内，患者无可能相关的视力变化；否认青光眼史；患者不存在具有临床意义的症性前列腺肥大或膀胱颈梗阻/尿潴留；患者在此前5年内不存在未完全缓解的不可切除的癌症，患者未在既往或当前在任何布地奈德和富马酸福莫特罗研究(PT009)，布地奈德、格隆安和富马酸福莫特罗(PT010)或格隆安(PT001)中接受随机化；患者无计划研究期间住院，患者否认访视前1个月内住过院，否认访视前4周内完成对呼吸道感染或哮喘急性发作的全身性激素治疗，否认有危机生命的哮喘，否认访视1前12个月内已知有药物滥用或酗酒史，否认对β2-激动剂、激素、抗胆碱药或MDI或pMDI中的任何组分发生超敏反应，否认既往或当前入组AEROSPHERE项目中的研究。",
  "diagnosis": "哮喘",
  "treatment_plan": "1. 停用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50ug/250ug)1泡/次 经口吸入 每日2次；2. 导入期BFP 1瓶（药物编号：661331-BD），预喷并给药2喷；3. 急救药物万托林 1瓶，必要时使用；4. 发放ePRO设备和峰流速仪，协助患者完成使用培训；5. 发放白色吸入器使用指南，受试者参与卡，受试者感谢卡，哮喘监测仪AMS患者快速入门指南，峰流速计AM3使用指南，手持设备患者快速指南；6. 预约患者下周一来院进行下次访视；7. 嘱患者带上发放的峰速仪、ePRO以及导入期药物；8. 嘱患者带上自上次访视以来的住院、门诊、急诊等病历记录；9. 嘱患者下次访视前急救药物沙丁胺醇暂停≥6小时；10. 嘱患者下次访视前早间剂量必须暂停，直至完成当此访视所有给药前评价；11. 嘱患者按要求清洗给药装置；12. 嘱患者用药期间如有任何不适，及时复诊。"
}
2026-08-10 11:53:48,293 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-04-15]
2026-08-10 11:53:48,308 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4107680, prompt_len=1811
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["四川省医学科学院·四川省人民医院", "门诊病历", "姓名：", "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667", "复诊记录", "记录时间：2024-04-15 09:26", "主诉：发作性喘息，参加LOGOS（D5982C00008）临床研究，行V1访视", "简要病史：患者今日7:40到院，自诉：哮喘病史：于2022年5月UK日首次出现哮喘症状，于2022年5月16日首次", "确诊为哮喘，2024年1月15日开始规范使用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次", "经口吸入 每日2次，控制症状，近一年未发生急性加重。", "既往病史：焦虑型抑郁症：2021年2月UK日-至今，采取以下药物治疗：", "草酸艾司西酞普兰片：2022年2月UK日-至今，20mg/次，qd；", "枸橼酸坦度螺酮胶囊：2022年2月UK日-至今，10mg/次，tid。", "过敏史：有过敏源花粉 因患者无法记得开始时间，故开始时间不详", "流行病学史：此前3个月内，患者无可能相关的视力变化；否认青光眼史；患者不存在具有临床意义的症性前列腺肥大或膀胱颈梗阻", "/尿潴留；患者在此前5年内不存在未完全缓解的不可切除的癌症，患者未在既往或当前在任何布地奈德和富马酸福莫特", "罗研究(PT009)，布地奈德、格隆安和富马酸福莫特罗(PT010)或格隆安(PT001)中接受随机化；患者无计划研究期间住院，", "患者否认访视前1个月内住过院，否认访视前4周内完成对呼吸道感染或哮喘急性发作的全身性激素治疗，否认有危机", "生命的哮喘，否认访视1前12个月内已知有药物滥用或酗酒史，否认对β2-激动剂、激素、抗胆碱药或MDI或pMDI中的", "任何组分发生超敏反应，否认既往或当前入组AEROSPHERE项目中的研究。", "体格检查：神志清楚，精神尚可，呼吸平稳，全身皮肤无黄染，无瘀点、瘀斑，皮肤皮温不高，皮肤无汗湿。浅表淋巴结", "未触及，头颅五官无畸形，眼球活动自如，睑结膜无充血苍白，球结膜无水肿，巩膜无黄染。口唇无发绀，", "伸舌居中，咽无充血，双侧扁桃体无肿大。颈软，颈静脉充盈，气管居中，甲状腺未扪及肿大。桶状胸，", "双肺呼吸音降低，双肺未闻及明显湿性啰音及哮鸣音。心界无明显增大，律齐，各瓣膜区未闻测量血", "共4页，第1页", "四川省医学科学院·四川省人民医院", "门诊病历", "姓名：马蓉 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667"]

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
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord API raw response (len=2419):
[
	{"text": "四川省医学科学院·四川省人民医院", "bbox": [353, 240, 712, 259]},
	{"text": "门诊病历", "bbox": [425, 269, 573, 290]},
	{"text": "姓名：", "bbox": [48, 295, 91, 308]},
	{"text": "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "bbox": [147, 295, 821, 308]},
	{"text": "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667", "bbox": [48, 313, 675, 327]},
	{"text": "复诊记录", "bbox": [466, 333, 549, 348]},
	{"text": "记录时间：2024-04-15 09:26", "bbox": [54, 354, 306, 367]},
	{"text": "主诉：发作性喘息，参加LOGOS（D5982C00008）临床研究，行V1访视", "bbox": [54, 376, 658, 389]},
	{"text": "简要病史：患者今日7:40到院，自诉：哮喘病史：于2022年5月UK日首次出现哮喘症状，于2022年5月16日首次", "bbox": [54, 398, 952, 412]},
	{"text": "确诊为哮喘，2024年1月15日开始规范使用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次", "bbox": [164, 415, 952, 428]},
	{"text": "经口吸入 每日2次，控制症状，近一年未发生急性加重。", "bbox": [164, 430, 610, 443]},
	{"text": "既往病史：焦虑型抑郁症：2021年2月UK日-至今，采取以下药物治疗：", "bbox": [54, 453, 637, 466]},
	{"text": "草酸艾司西酞普兰片：2022年2月UK日-至今，20mg/次，qd；", "bbox": [164, 468, 644, 481]},
	{"text": "枸橼酸坦度螺酮胶囊：2022年2月UK日-至今，10mg/次，tid。", "bbox": [164, 483, 654, 496]},
	{"text": "过敏史：有过敏源花粉 因患者无法记得开始时间，故开始时间不详", "bbox": [54, 505, 620, 518]},
	{"text": "流行病学史：此前3个月内，患者无可能相关的视力变化；否认青光眼史；患者不存在具有临床意义的症性前列腺肥大或膀胱颈梗阻", "bbox": [54, 525, 952, 538]},
	{"text": "/尿潴留；患者在此前5年内不存在未完全缓解的不可切除的癌症，患者未在既往或当前在任何布地奈德和富马酸福莫特", "bbox": [164, 539, 952, 552]},
	{"text": "罗研究(PT009)，布地奈德、格隆安和富马酸福莫特罗(PT010)或格隆安(PT001)中接受随机化；患者无计划研究期间住院，", "bbox": [164, 553, 957, 566]},
	{"text": "患者否认访视前1个月内住过院，否认访视前4周内完成对呼吸道感染或哮喘急性发作的全身性激素治疗，否认有危机", "bbox": [164, 567, 952, 580]},
	{"text": "生命的哮喘，否认访视1前12个月内已知有药物滥用或酗酒史，否认对β2-激动剂、激素、抗胆碱药或MDI或pMDI中的", "bbox": [164, 581, 952, 594]},
	{"text": "任何组分发生超敏反应，否认既往或当前入组AEROSPHERE项目中的研究。", "bbox": [164, 595, 652, 607]},
	{"text": "体格检查：神志清楚，精神尚可，呼吸平稳，全身皮肤无黄染，无瘀点、瘀斑，皮肤皮温不高，皮肤无汗湿。浅表淋巴结", "bbox": [54, 615, 952, 628]},
	{"text": "未触及，头颅五官无畸形，眼球活动自如，睑结膜无充血苍白，球结膜无水肿，巩膜无黄染。口唇无发绀，", "bbox": [164, 630, 957, 643]},
	{"text": "伸舌居中，咽无充血，双侧扁桃体无肿大。颈软，颈静脉充盈，气管居中，甲状腺未扪及肿大。桶状胸，", "bbox": [164, 645, 957, 658]},
	{"text": "双肺呼吸音降低，双肺未闻及明显湿性啰音及哮鸣音。心界无明显增大，律齐，各瓣膜区未闻测量血", "bbox": [164, 660, 952, 673]},
	{"text": "共4页，第1页", "bbox": [450, 690, 569, 703]},
	{"text": "四川省医学科学院·四川省人民医院", "bbox": [353, 762, 712, 779]},
	{"text": "门诊病历", "bbox": [425, 790, 573, 810]},
	{"text": "姓名：马蓉 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "bbox": [48, 817, 819, 830]},
	{"text": "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667", "bbox": [48, 835, 672, 848]}
]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=21.4s
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[0]: text=四川省医学科学院·四川省人民医院, bbox=[353, 240, 712, 259]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[425, 269, 573, 290]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[48, 295, 91, 308]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109, bbox=[147, 295, 821, 308]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[4]: text=住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667, bbox=[48, 313, 675, 327]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[5]: text=复诊记录, bbox=[466, 333, 549, 348]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[6]: text=记录时间：2024-04-15 09:26, bbox=[54, 354, 306, 367]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[7]: text=主诉：发作性喘息，参加LOGOS（D5982C00008）临床研究，行V1访视, bbox=[54, 376, 658, 389]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[8]: text=简要病史：患者今日7:40到院，自诉：哮喘病史：于2022年5月UK日首次出现哮喘症状，于2022年5月16日首次, bbox=[54, 398, 952, 412]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[9]: text=确诊为哮喘，2024年1月15日开始规范使用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次, bbox=[164, 415, 952, 428]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[10]: text=经口吸入 每日2次，控制症状，近一年未发生急性加重。, bbox=[164, 430, 610, 443]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[11]: text=既往病史：焦虑型抑郁症：2021年2月UK日-至今，采取以下药物治疗：, bbox=[54, 453, 637, 466]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[12]: text=草酸艾司西酞普兰片：2022年2月UK日-至今，20mg/次，qd；, bbox=[164, 468, 644, 481]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[13]: text=枸橼酸坦度螺酮胶囊：2022年2月UK日-至今，10mg/次，tid。, bbox=[164, 483, 654, 496]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[14]: text=过敏史：有过敏源花粉 因患者无法记得开始时间，故开始时间不详, bbox=[54, 505, 620, 518]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[15]: text=流行病学史：此前3个月内，患者无可能相关的视力变化；否认青光眼史；患者不存在具有临床意义的症性前列腺肥大或膀胱颈梗阻, bbox=[54, 525, 952, 538]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[16]: text=/尿潴留；患者在此前5年内不存在未完全缓解的不可切除的癌症，患者未在既往或当前在任何布地奈德和富马酸福莫特, bbox=[164, 539, 952, 552]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[17]: text=罗研究(PT009)，布地奈德、格隆安和富马酸福莫特罗(PT010)或格隆安(PT001)中接受随机化；患者无计划研究期间住院，, bbox=[164, 553, 957, 566]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[18]: text=患者否认访视前1个月内住过院，否认访视前4周内完成对呼吸道感染或哮喘急性发作的全身性激素治疗，否认有危机, bbox=[164, 567, 952, 580]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[19]: text=生命的哮喘，否认访视1前12个月内已知有药物滥用或酗酒史，否认对β2-激动剂、激素、抗胆碱药或MDI或pMDI中的, bbox=[164, 581, 952, 594]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[20]: text=任何组分发生超敏反应，否认既往或当前入组AEROSPHERE项目中的研究。, bbox=[164, 595, 652, 607]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[21]: text=体格检查：神志清楚，精神尚可，呼吸平稳，全身皮肤无黄染，无瘀点、瘀斑，皮肤皮温不高，皮肤无汗湿。浅表淋巴结, bbox=[54, 615, 952, 628]
2026-08-10 11:54:09,699 INFO     29 [qwen-vl-text] coord item[22]: text=未触及，头颅五官无畸形，眼球活动自如，睑结膜无充血苍白，球结膜无水肿，巩膜无黄染。口唇无发绀，, bbox=[164, 630, 957, 643]
2026-08-10 11:54:09,700 INFO     29 [qwen-vl-text] coord item[23]: text=伸舌居中，咽无充血，双侧扁桃体无肿大。颈软，颈静脉充盈，气管居中，甲状腺未扪及肿大。桶状胸，, bbox=[164, 645, 957, 658]
2026-08-10 11:54:09,700 INFO     29 [qwen-vl-text] coord item[24]: text=双肺呼吸音降低，双肺未闻及明显湿性啰音及哮鸣音。心界无明显增大，律齐，各瓣膜区未闻测量血, bbox=[164, 660, 952, 673]
2026-08-10 11:54:09,700 INFO     29 [qwen-vl-text] coord item[25]: text=共4页，第1页, bbox=[450, 690, 569, 703]
2026-08-10 11:54:09,700 INFO     29 [qwen-vl-text] coord item[26]: text=四川省医学科学院·四川省人民医院, bbox=[353, 762, 712, 779]
2026-08-10 11:54:09,700 INFO     29 [qwen-vl-text] coord item[27]: text=门诊病历, bbox=[425, 790, 573, 810]
2026-08-10 11:54:09,700 INFO     29 [qwen-vl-text] coord item[28]: text=姓名：马蓉 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109, bbox=[48, 817, 819, 830]
2026-08-10 11:54:09,700 INFO     29 [qwen-vl-text] coord item[29]: text=住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667, bbox=[48, 835, 672, 848]
2026-08-10 11:54:09,700 INFO     29 [qwen-vl-text] page=10 — 30/30 coords, api_time=21.4s
2026-08-10 11:54:09,707 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3685351, prompt_len=1660
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["四川省医学科学院·四川省人民医院", "门诊病历", "姓名：", "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：", "挂号流水号：49735667", "压）及病理性杂音。腹软，无压痛、反跳痛及肌紧张，肝脾肋下未触及，肝肾区无叩痛，肠鸣音不活跃。", "双下肢对称无明显水肿，四肢肌力及肌张力正常。生命体征详见生命体征表（受试者已在休息5分钟后", "取坐位）", "门诊诊断：", "哮喘", "处", "置：", "知情过程：根据患者已有既往资料的情况，考虑受试者可能符合“一项随机、双盲、双模拟、平行分组、", "多中心、24至52周可变时长的研究，评估布地奈德、格隆铵和富马酸福莫特罗定量吸入器（MDI）与布地", "奈德和富马酸福莫特罗MDI以及信必可®加压MDI相比在哮喘未充分控制的成人和青少年受试者中的疗", "效和安全性（LOGOS）”的临床试验，今日7时55分当面与患者本人及家属进行充分知情，详细讲解本研究", "的目的、方法、流程及可能的获益及风险，并给予患者充分的时间考虑，患者仔细阅读无疑问，自愿同意", "参加本项临床试验，于2024年4月15日8时15分与患者本人共同签署两份成人研究受试者主要信息", "和知情同意书（研究信息和知情同意书）（研究中心版本号1429-2.0，研究中心版本日期：2023年10月", "31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日当面与患者本人详细讲解中国个人", "信息保护附录相关内容，患者表示无疑问并充分理解接受，于2024年4月15日8时18分签署两份中国", "个人信息保护附录（中国个人信息保护附录）（研究中心版本号1429-2.0 研究中心版本日期2023年10", "月31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日同时告知患者12小时PFT子研", "究者相关内容，患者表示拒绝。", "人口统计学信息：出生日期：1963年8月16日 性别：女 民族：汉族 种族：中国人", "患者否认哮喘相关家族史，否认吸烟及饮酒，自诉无输血史及手术史，患者目前已绝经（经期：开始时间：", "1978年，结束时间：2014年）。", "疫苗接种史：目前已无法查询新冠疫苗接种史，患者自诉2021年-2022年期间接种三针（具体相关信息", "无法提供）", "共4页，第2页", "12"]

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
2026-08-10 11:54:30,728 INFO     29 [qwen-vl-text] coord API raw response (len=2358):
[
	{"text": "四川省医学科学院·四川省人民医院", "bbox": [352, 315, 712, 334]},
	{"text": "门诊病历", "bbox": [423, 344, 570, 365]},
	{"text": "姓名：", "bbox": [44, 369, 88, 382]},
	{"text": "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "bbox": [145, 369, 819, 382]},
	{"text": "住址：四川省成都市邛崃市 联系电话：", "bbox": [44, 387, 360, 400]},
	{"text": "挂号流水号：49735667", "bbox": [488, 387, 673, 400]},
	{"text": "压）及病理性杂音。腹软，无压痛、反跳痛及肌紧张，肝脾肋下未触及，肝肾区无叩痛，肠鸣音不活跃。", "bbox": [162, 407, 958, 420]},
	{"text": "双下肢对称无明显水肿，四肢肌力及肌张力正常。生命体征详见生命体征表（受试者已在休息5分钟后", "bbox": [162, 422, 950, 436]},
	{"text": "取坐位）", "bbox": [162, 438, 226, 451]},
	{"text": "门诊诊断：", "bbox": [51, 461, 129, 474]},
	{"text": "哮喘", "bbox": [162, 461, 198, 474]},
	{"text": "处", "bbox": [51, 484, 68, 497]},
	{"text": "置：", "bbox": [104, 484, 129, 497]},
	{"text": "知情过程：根据患者已有既往资料的情况，考虑受试者可能符合“一项随机、双盲、双模拟、平行分组、", "bbox": [162, 482, 958, 495]},
	{"text": "多中心、24至52周可变时长的研究，评估布地奈德、格隆铵和富马酸福莫特罗定量吸入器（MDI）与布地", "bbox": [162, 497, 950, 510]},
	{"text": "奈德和富马酸福莫特罗MDI 以及信必可®加压MDI 相比在哮喘未充分控制的成人和青少年受试者中的疗", "bbox": [162, 512, 950, 525]},
	{"text": "效和安全性（LOGOS）”的临床试验，今日7时55分当面与患者本人及家属进行充分知情，详细讲解本研究", "bbox": [162, 527, 950, 540]},
	{"text": "的目的、方法、流程及可能的获益及风险，并给予患者充分的时间考虑，患者仔细阅读无疑问，自愿同意", "bbox": [162, 542, 950, 555]},
	{"text": "参加本项临床试验，于2024年4月15日8时15分与患者本人共同签署两份成人研究受试者主要信息", "bbox": [162, 557, 950, 570]},
	{"text": "和知情同意书（研究信息和知情同意书）（研究中心版本号1429-2.0，研究中心版本日期：2023年10月", "bbox": [162, 572, 950, 585]},
	{"text": "31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日当面与患者本人详细讲解中国个人", "bbox": [162, 587, 950, 600]},
	{"text": "信息保护附录相关内容，患者表示无疑问并充分理解接受，于2024年4月15日8时18分签署两份中国", "bbox": [162, 602, 950, 615]},
	{"text": "个人信息保护附录（中国个人信息保护附录）（研究中心版本号1429-2.0 研究中心版本日期2023年10", "bbox": [162, 617, 950, 630]},
	{"text": "月31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日同时告知患者12小时PFT子研", "bbox": [162, 632, 950, 645]},
	{"text": "究者相关内容，患者表示拒绝。", "bbox": [162, 648, 403, 661]},
	{"text": "人口统计学信息：出生日期：1963年8月16日 性别：女 民族：汉族 种族：中国人", "bbox": [162, 664, 819, 677]},
	{"text": "患者否认哮喘相关家族史，否认吸烟及饮酒，自诉无输血史及手术史，患者目前已绝经（经期：开始时间：", "bbox": [162, 679, 958, 692]},
	{"text": "1978年，结束时间：2014年）。", "bbox": [162, 694, 401, 707]},
	{"text": "疫苗接种史：目前已无法查询新冠疫苗接种史，患者自诉2021年-2022年期间接种三针（具体相关信息", "bbox": [162, 710, 950, 723]},
	{"text": "无法提供）", "bbox": [162, 725, 241, 738]},
	{"text": "共4页，第2页", "bbox": [445, 760, 565, 773]},
	{"text": "12", "bbox": [916, 980, 944, 993]}
]
2026-08-10 11:54:30,729 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=21.0s
2026-08-10 11:54:30,729 INFO     29 [qwen-vl-text] coord item[0]: text=四川省医学科学院·四川省人民医院, bbox=[352, 315, 712, 334]
2026-08-10 11:54:30,729 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[423, 344, 570, 365]
2026-08-10 11:54:30,729 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[44, 369, 88, 382]
2026-08-10 11:54:30,729 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109, bbox=[145, 369, 819, 382]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[4]: text=住址：四川省成都市邛崃市 联系电话：, bbox=[44, 387, 360, 400]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[5]: text=挂号流水号：49735667, bbox=[488, 387, 673, 400]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[6]: text=压）及病理性杂音。腹软，无压痛、反跳痛及肌紧张，肝脾肋下未触及，肝肾区无叩痛，肠鸣音不活跃。, bbox=[162, 407, 958, 420]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[7]: text=双下肢对称无明显水肿，四肢肌力及肌张力正常。生命体征详见生命体征表（受试者已在休息5分钟后, bbox=[162, 422, 950, 436]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[8]: text=取坐位）, bbox=[162, 438, 226, 451]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[9]: text=门诊诊断：, bbox=[51, 461, 129, 474]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[10]: text=哮喘, bbox=[162, 461, 198, 474]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[11]: text=处, bbox=[51, 484, 68, 497]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[12]: text=置：, bbox=[104, 484, 129, 497]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[13]: text=知情过程：根据患者已有既往资料的情况，考虑受试者可能符合“一项随机、双盲、双模拟、平行分组、, bbox=[162, 482, 958, 495]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[14]: text=多中心、24至52周可变时长的研究，评估布地奈德、格隆铵和富马酸福莫特罗定量吸入器（MDI）与布地, bbox=[162, 497, 950, 510]
2026-08-10 11:54:30,730 INFO     29 [qwen-vl-text] coord item[15]: text=奈德和富马酸福莫特罗MDI 以及信必可®加压MDI 相比在哮喘未充分控制的成人和青少年受试者中的疗, bbox=[162, 512, 950, 525]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[16]: text=效和安全性（LOGOS）”的临床试验，今日7时55分当面与患者本人及家属进行充分知情，详细讲解本研究, bbox=[162, 527, 950, 540]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[17]: text=的目的、方法、流程及可能的获益及风险，并给予患者充分的时间考虑，患者仔细阅读无疑问，自愿同意, bbox=[162, 542, 950, 555]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[18]: text=参加本项临床试验，于2024年4月15日8时15分与患者本人共同签署两份成人研究受试者主要信息, bbox=[162, 557, 950, 570]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[19]: text=和知情同意书（研究信息和知情同意书）（研究中心版本号1429-2.0，研究中心版本日期：2023年10月, bbox=[162, 572, 950, 585]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[20]: text=31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日当面与患者本人详细讲解中国个人, bbox=[162, 587, 950, 600]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[21]: text=信息保护附录相关内容，患者表示无疑问并充分理解接受，于2024年4月15日8时18分签署两份中国, bbox=[162, 602, 950, 615]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[22]: text=个人信息保护附录（中国个人信息保护附录）（研究中心版本号1429-2.0 研究中心版本日期2023年10, bbox=[162, 617, 950, 630]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[23]: text=月31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日同时告知患者12小时PFT子研, bbox=[162, 632, 950, 645]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[24]: text=究者相关内容，患者表示拒绝。, bbox=[162, 648, 403, 661]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[25]: text=人口统计学信息：出生日期：1963年8月16日 性别：女 民族：汉族 种族：中国人, bbox=[162, 664, 819, 677]
2026-08-10 11:54:30,731 INFO     29 [qwen-vl-text] coord item[26]: text=患者否认哮喘相关家族史，否认吸烟及饮酒，自诉无输血史及手术史，患者目前已绝经（经期：开始时间：, bbox=[162, 679, 958, 692]
2026-08-10 11:54:30,732 INFO     29 [qwen-vl-text] coord item[27]: text=1978年，结束时间：2014年）。, bbox=[162, 694, 401, 707]
2026-08-10 11:54:30,732 INFO     29 [qwen-vl-text] coord item[28]: text=疫苗接种史：目前已无法查询新冠疫苗接种史，患者自诉2021年-2022年期间接种三针（具体相关信息, bbox=[162, 710, 950, 723]
2026-08-10 11:54:30,732 INFO     29 [qwen-vl-text] coord item[29]: text=无法提供）, bbox=[162, 725, 241, 738]
2026-08-10 11:54:30,732 INFO     29 [qwen-vl-text] coord item[30]: text=共4页，第2页, bbox=[445, 760, 565, 773]
2026-08-10 11:54:30,732 INFO     29 [qwen-vl-text] coord item[31]: text=12, bbox=[916, 980, 944, 993]
2026-08-10 11:54:30,733 INFO     29 [qwen-vl-text] page=11 — 32/32 coords, api_time=21.0s
2026-08-10 11:54:30,745 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4136561, prompt_len=1646
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["四川省医学科学院·四川省人民医院", "门诊病历", "姓名：", "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667", "询问患者最近一次进食时间，患者自诉19:10，今与患者确认测量前6小时内未使用SABA类药物，并确认前一晚吸入沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次 经口吸入 每日2次 时间为", "20:00，至今未使用任何药物。", "患者静息10分钟后以仰卧位行12导联ECG检查，详见ECG报告。在肺功能测量前进行FoNO检测，检测一小时前无饮水及进食，随后行给药前-60min、-30min肺功能检查，患者者给药前FEV1%：78.85%。", "检查结果详见报告。", "完成ACQ-6及ACQ-7问卷，ACQ-7评分≥1.5。", "患者性别：女，已绝经，故未使用中心试验室提供的试剂进行尿妊娠试验。", "采集血样；完成血液标本采集后进行处理，并送往中心实验室进行检测。", "患者目前符合所有入选标准，不符合任一排除标准，嘱患者自今日起停用沙美特罗替卡松吸入粉雾剂", "|舒利迭(兴)(50ug/250ug)1泡/次 经口吸入 每日2次。IRT系统登记，筛选号；E1429021，并获得培训", "装置1瓶，药物编号：117165-EQ；获得导入期BFP1瓶，药物编号为；661331-BD。使用培训装置对患者进行", "吸入器使用培训及检查吸入装置技术，完成给药培训后当场回收；于11:08指导患者对导入期BFP进行", "预喷并给药2喷，给药结束时间为：11:10。发放急救药物万托林1瓶，嘱患者必要时使用。", "发放ePRO设备和峰流速仪，协助患者完成使用培训，同时发放白色吸入器使用指南，受试者参与卡。", "受试者感谢卡、哮喘监测仪AMS患者快速入门指南、峰流速计AM3使用指南，手持设备患者快速指南。", "预约患者下周一来院进行下次访视；", "嘱患者带上发放的峰速仪、ePRO以及导入期药物；", "嘱患者带上自上次访视以来的住院、门诊、急诊等病历记录；", "嘱患者下次访视前急救药物沙丁胺醇暂停≥6小时；", "嘱患者下次访视前早间剂量必须暂停，直至完成当此访视所有给药前评价；", "嘱患者按要求清洗给药装置；", "共4页，第3页", "13"]

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
2026-08-10 11:54:50,685 INFO     29 [qwen-vl-text] coord API raw response (len=2140):
[
	{"text": "四川省医学科学院·四川省人民医院", "bbox": [350, 316, 709, 334]},
	{"text": "门诊病历", "bbox": [422, 344, 569, 364]},
	{"text": "姓名：", "bbox": [45, 369, 88, 382]},
	{"text": "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "bbox": [144, 369, 818, 382]},
	{"text": "住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667", "bbox": [45, 387, 670, 400]},
	{"text": "询问患者最近一次进食时间，患者自诉19:10，今与患者确认测量前6小时内未使用SABA类药物，并确认前一晚吸入沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次 经口吸入 每日2次 时间为", "bbox": [162, 407, 948, 420]},
	{"text": "20:00，至今未使用任何药物。", "bbox": [162, 438, 395, 451]},
	{"text": "患者静息10分钟后以仰卧位行12导联ECG检查，详见ECG报告。在肺功能测量前进行FoNO检测，检测一小时前无饮水及进食，随后行给药前-60min、-30min肺功能检查，患者者给药前FEV1%：78.85%。", "bbox": [162, 454, 948, 467]},
	{"text": "检查结果详见报告。", "bbox": [162, 483, 315, 496]},
	{"text": "完成ACQ-6及ACQ-7问卷，ACQ-7评分≥1.5。", "bbox": [181, 499, 524, 512]},
	{"text": "患者性别：女，已绝经，故未使用中心试验室提供的试剂进行尿妊娠试验。", "bbox": [181, 514, 754, 527]},
	{"text": "采集血样；完成血液标本采集后进行处理，并送往中心实验室进行检测。", "bbox": [181, 529, 736, 542]},
	{"text": "患者目前符合所有入选标准，不符合任一排除标准，嘱患者自今日起停用沙美特罗替卡松吸入粉雾剂", "bbox": [181, 544, 948, 557]},
	{"text": "|舒利迭(兴)(50ug/250ug)1泡/次 经口吸入 每日2次。IRT系统登记，筛选号；E1429021，并获得培训", "bbox": [162, 560, 948, 573]},
	{"text": "装置1瓶，药物编号：117165-EQ；获得导入期BFP1瓶，药物编号为；661331-BD。使用培训装置对患者进行", "bbox": [162, 575, 948, 588]},
	{"text": "吸入器使用培训及检查吸入装置技术，完成给药培训后当场回收；于11:08指导患者对导入期BFP进行", "bbox": [162, 590, 948, 603]},
	{"text": "预喷并给药2喷，给药结束时间为：11:10。发放急救药物万托林1瓶，嘱患者必要时使用。", "bbox": [162, 605, 868, 618]},
	{"text": "发放ePRO设备和峰流速仪，协助患者完成使用培训，同时发放白色吸入器使用指南，受试者参与卡。", "bbox": [181, 620, 956, 633]},
	{"text": "受试者感谢卡、哮喘监测仪AMS患者快速入门指南、峰流速计AM3使用指南，手持设备患者快速指南。", "bbox": [162, 636, 948, 649]},
	{"text": "预约患者下周一来院进行下次访视；", "bbox": [181, 651, 452, 664]},
	{"text": "嘱患者带上发放的峰速仪、ePRO以及导入期药物；", "bbox": [181, 666, 561, 679]},
	{"text": "嘱患者带上自上次访视以来的住院、门诊、急诊等病历记录；", "bbox": [181, 681, 647, 694]},
	{"text": "嘱患者下次访视前急救药物沙丁胺醇暂停≥6小时；", "bbox": [181, 697, 570, 710]},
	{"text": "嘱患者下次访视前早间剂量必须暂停，直至完成当此访视所有给药前评价；", "bbox": [181, 712, 754, 725]},
	{"text": "嘱患者按要求清洗给药装置；", "bbox": [181, 727, 400, 740]},
	{"text": "共4页，第3页", "bbox": [445, 762, 564, 774]},
	{"text": "13", "bbox": [916, 980, 944, 993]}
]
2026-08-10 11:54:50,686 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=19.9s
2026-08-10 11:54:50,686 INFO     29 [qwen-vl-text] coord item[0]: text=四川省医学科学院·四川省人民医院, bbox=[350, 316, 709, 334]
2026-08-10 11:54:50,686 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[422, 344, 569, 364]
2026-08-10 11:54:50,686 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[45, 369, 88, 382]
2026-08-10 11:54:50,686 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109, bbox=[144, 369, 818, 382]
2026-08-10 11:54:50,686 INFO     29 [qwen-vl-text] coord item[4]: text=住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667, bbox=[45, 387, 670, 400]
2026-08-10 11:54:50,686 INFO     29 [qwen-vl-text] coord item[5]: text=询问患者最近一次进食时间，患者自诉19:10，今与患者确认测量前6小时内未使用SABA类药物，并确认前一晚吸入沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次 经口吸入 每日2次 时间为, bbox=[162, 407, 948, 420]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[6]: text=20:00，至今未使用任何药物。, bbox=[162, 438, 395, 451]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[7]: text=患者静息10分钟后以仰卧位行12导联ECG检查，详见ECG报告。在肺功能测量前进行FoNO检测，检测一小时前无饮水及进食，随后行给药前-60min、-30min肺功能检查，患者者给药前FEV1%：78.85%。, bbox=[162, 454, 948, 467]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[8]: text=检查结果详见报告。, bbox=[162, 483, 315, 496]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[9]: text=完成ACQ-6及ACQ-7问卷，ACQ-7评分≥1.5。, bbox=[181, 499, 524, 512]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[10]: text=患者性别：女，已绝经，故未使用中心试验室提供的试剂进行尿妊娠试验。, bbox=[181, 514, 754, 527]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[11]: text=采集血样；完成血液标本采集后进行处理，并送往中心实验室进行检测。, bbox=[181, 529, 736, 542]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[12]: text=患者目前符合所有入选标准，不符合任一排除标准，嘱患者自今日起停用沙美特罗替卡松吸入粉雾剂, bbox=[181, 544, 948, 557]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[13]: text=|舒利迭(兴)(50ug/250ug)1泡/次 经口吸入 每日2次。IRT系统登记，筛选号；E1429021，并获得培训, bbox=[162, 560, 948, 573]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[14]: text=装置1瓶，药物编号：117165-EQ；获得导入期BFP1瓶，药物编号为；661331-BD。使用培训装置对患者进行, bbox=[162, 575, 948, 588]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[15]: text=吸入器使用培训及检查吸入装置技术，完成给药培训后当场回收；于11:08指导患者对导入期BFP进行, bbox=[162, 590, 948, 603]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[16]: text=预喷并给药2喷，给药结束时间为：11:10。发放急救药物万托林1瓶，嘱患者必要时使用。, bbox=[162, 605, 868, 618]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[17]: text=发放ePRO设备和峰流速仪，协助患者完成使用培训，同时发放白色吸入器使用指南，受试者参与卡。, bbox=[181, 620, 956, 633]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[18]: text=受试者感谢卡、哮喘监测仪AMS患者快速入门指南、峰流速计AM3使用指南，手持设备患者快速指南。, bbox=[162, 636, 948, 649]
2026-08-10 11:54:50,687 INFO     29 [qwen-vl-text] coord item[19]: text=预约患者下周一来院进行下次访视；, bbox=[181, 651, 452, 664]
2026-08-10 11:54:50,688 INFO     29 [qwen-vl-text] coord item[20]: text=嘱患者带上发放的峰速仪、ePRO以及导入期药物；, bbox=[181, 666, 561, 679]
2026-08-10 11:54:50,688 INFO     29 [qwen-vl-text] coord item[21]: text=嘱患者带上自上次访视以来的住院、门诊、急诊等病历记录；, bbox=[181, 681, 647, 694]
2026-08-10 11:54:50,688 INFO     29 [qwen-vl-text] coord item[22]: text=嘱患者下次访视前急救药物沙丁胺醇暂停≥6小时；, bbox=[181, 697, 570, 710]
2026-08-10 11:54:50,688 INFO     29 [qwen-vl-text] coord item[23]: text=嘱患者下次访视前早间剂量必须暂停，直至完成当此访视所有给药前评价；, bbox=[181, 712, 754, 725]
2026-08-10 11:54:50,688 INFO     29 [qwen-vl-text] coord item[24]: text=嘱患者按要求清洗给药装置；, bbox=[181, 727, 400, 740]
2026-08-10 11:54:50,688 INFO     29 [qwen-vl-text] coord item[25]: text=共4页，第3页, bbox=[445, 762, 564, 774]
2026-08-10 11:54:50,688 INFO     29 [qwen-vl-text] coord item[26]: text=13, bbox=[916, 980, 944, 993]
2026-08-10 11:54:50,689 INFO     29 [qwen-vl-text] page=12 — 27/27 coords, api_time=19.9s
2026-08-10 11:54:50,691 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=924713, prompt_len=831
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["四川省医学科学院·四川省人民医院", "门诊病历", "姓名：", "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "住址：四川省成都市邛崃市 联系电话：", "挂号流水号：49735667", "嘱患者用药期间如有任何不适，及时复诊。", "婚姻史：", "月经史：", "是否下转： 否", "是否外伤：否", "是否美容： 否", "医师签名： 燕海荣", "共4页，第4页"]

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
2026-08-10 11:55:02,352 INFO     29 [qwen-vl-text] coord API raw response (len=788):
[
	{"text": "四川省医学科学院·四川省人民医院", "bbox": [347, 323, 709, 341]},
	{"text": "门诊病历", "bbox": [419, 351, 569, 370]},
	{"text": "姓名：", "bbox": [41, 375, 84, 389]},
	{"text": "性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109", "bbox": [140, 375, 817, 389]},
	{"text": "住址：四川省成都市邛崃市 联系电话：", "bbox": [41, 393, 356, 407]},
	{"text": "挂号流水号：49735667", "bbox": [490, 393, 670, 407]},
	{"text": "嘱患者用药期间如有任何不适，及时复诊。", "bbox": [176, 413, 506, 426]},
	{"text": "婚姻史：", "bbox": [43, 449, 103, 462]},
	{"text": "月经史：", "bbox": [44, 467, 113, 480]},
	{"text": "是否下转： 否", "bbox": [44, 485, 168, 498]},
	{"text": "是否外伤：否", "bbox": [44, 503, 150, 516]},
	{"text": "是否美容： 否", "bbox": [204, 503, 321, 516]},
	{"text": "医师签名： 燕海荣", "bbox": [733, 521, 922, 544]},
	{"text": "共4页，第4页", "bbox": [443, 758, 561, 771]}
]
2026-08-10 11:55:02,352 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=11.7s
2026-08-10 11:55:02,352 INFO     29 [qwen-vl-text] coord item[0]: text=四川省医学科学院·四川省人民医院, bbox=[347, 323, 709, 341]
2026-08-10 11:55:02,352 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[419, 351, 569, 370]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[41, 375, 84, 389]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109, bbox=[140, 375, 817, 389]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[4]: text=住址：四川省成都市邛崃市 联系电话：, bbox=[41, 393, 356, 407]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[5]: text=挂号流水号：49735667, bbox=[490, 393, 670, 407]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[6]: text=嘱患者用药期间如有任何不适，及时复诊。, bbox=[176, 413, 506, 426]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻史：, bbox=[43, 449, 103, 462]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[8]: text=月经史：, bbox=[44, 467, 113, 480]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[9]: text=是否下转： 否, bbox=[44, 485, 168, 498]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[10]: text=是否外伤：否, bbox=[44, 503, 150, 516]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[11]: text=是否美容： 否, bbox=[204, 503, 321, 516]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[12]: text=医师签名： 燕海荣, bbox=[733, 521, 922, 544]
2026-08-10 11:55:02,354 INFO     29 [qwen-vl-text] coord item[13]: text=共4页，第4页, bbox=[443, 758, 561, 771]
2026-08-10 11:55:02,356 INFO     29 [qwen-vl-text] page=13 — 14/14 coords, api_time=11.7s
2026-08-10 11:55:02,356 INFO     29 [qwen-vl-text] new_positions (103):
[[10, 437.367, 882.1680000000001, 420.96, 454.286], [10, 526.575, 709.947, 471.826, 508.66], [10, 59.47200000000001, 112.74900000000001, 517.43, 540.232], [10, 182.133, 1017.219, 517.43, 540.232], [10, 59.47200000000001, 836.325, 549.002, 573.558], [10, 577.374, 680.211, 584.082, 610.392], [10, 66.906, 379.134, 620.916, 643.718], [10, 66.906, 815.2620000000001, 659.504, 682.306], [10, 66.906, 1179.528, 698.092, 722.648], [10, 203.19600000000003, 1179.528, 727.91, 750.712], [10, 203.19600000000003, 755.7900000000001, 754.22, 777.022], [10, 66.906, 789.243, 794.562, 817.364], [10, 203.19600000000003, 797.916, 820.872, 843.674], [10, 203.19600000000003, 810.306, 847.182, 869.984], [10, 66.906, 768.1800000000001, 885.77, 908.572], [10, 66.906, 1179.528, 920.85, 943.652], [10, 203.19600000000003, 1179.528, 945.406, 968.208], [10, 203.19600000000003, 1185.7230000000002, 969.962, 992.764], [10, 203.19600000000003, 1179.528, 994.518, 1017.32], [10, 203.19600000000003, 1179.528, 1019.074, 1041.876], [10, 203.19600000000003, 807.8280000000001, 1043.63, 1064.678], [10, 66.906, 1179.528, 1078.71, 1101.512], [10, 203.19600000000003, 1185.7230000000002, 1105.02, 1127.822], [10, 203.19600000000003, 1185.7230000000002, 1131.33, 1154.132], [10, 203.19600000000003, 1179.528, 1157.64, 1180.442], [10, 557.5500000000001, 704.9910000000001, 1210.26, 1233.062], [10, 437.367, 882.1680000000001, 1336.548, 1366.366], [10, 526.575, 709.947, 1385.66, 1420.74], [10, 59.47200000000001, 1014.7410000000001, 1433.018, 1455.82], [10, 59.47200000000001, 832.6080000000001, 1464.59, 1487.392], [11, 436.12800000000004, 882.1680000000001, 552.51, 585.836], [11, 524.0970000000001, 706.23, 603.376, 640.21], [11, 54.516000000000005, 109.03200000000001, 647.226, 670.028], [11, 179.655, 1014.7410000000001, 647.226, 670.028], [11, 54.516000000000005, 446.04, 678.798, 701.6], [11, 604.6320000000001, 833.8470000000001, 678.798, 701.6], [11, 200.71800000000002, 1186.962, 713.878, 736.68], [11, 200.71800000000002, 1177.0500000000002, 740.188, 764.744], [11, 200.71800000000002, 280.014, 768.252, 791.054], [11, 63.18900000000001, 159.83100000000002, 808.594, 831.396], [11, 200.71800000000002, 245.32200000000003, 808.594, 831.396], [11, 63.18900000000001, 84.25200000000001, 848.936, 871.738], [11, 128.85600000000002, 159.83100000000002, 848.936, 871.738], [11, 200.71800000000002, 1186.962, 845.428, 868.23], [11, 200.71800000000002, 1177.0500000000002, 871.738, 894.54], [11, 200.71800000000002, 1177.0500000000002, 898.048, 920.85], [11, 200.71800000000002, 1177.0500000000002, 924.358, 947.16], [11, 200.71800000000002, 1177.0500000000002, 950.668, 973.47], [11, 200.71800000000002, 1177.0500000000002, 976.978, 999.78], [11, 200.71800000000002, 1177.0500000000002, 1003.288, 1026.09], [11, 200.71800000000002, 1177.0500000000002, 1029.598, 1052.4], [11, 200.71800000000002, 1177.0500000000002, 1055.908, 1078.71], [11, 200.71800000000002, 1177.0500000000002, 1082.218, 1105.02], [11, 200.71800000000002, 1177.0500000000002, 1108.528, 1131.33], [11, 200.71800000000002, 499.31700000000006, 1136.592, 1159.394], [11, 200.71800000000002, 1014.7410000000001, 1164.656, 1187.458], [11, 200.71800000000002, 1186.962, 1190.966, 1213.768], [11, 200.71800000000002, 496.83900000000006, 1217.276, 1240.078], [11, 200.71800000000002, 1177.0500000000002, 1245.34, 1268.142], [11, 200.71800000000002, 298.59900000000005, 1271.65, 1294.452], [11, 551.355, 700.0350000000001, 1333.04, 1355.842], [11, 1134.9240000000002, 1169.616, 1718.92, 1741.722], [12, 433.65000000000003, 878.451, 554.264, 585.836], [12, 522.8580000000001, 704.9910000000001, 603.376, 638.456], [12, 55.755, 109.03200000000001, 647.226, 670.028], [12, 178.41600000000003, 1013.5020000000001, 647.226, 670.028], [12, 55.755, 830.1300000000001, 678.798, 701.6], [12, 200.71800000000002, 1174.5720000000001, 713.878, 736.68], [12, 200.71800000000002, 489.40500000000003, 768.252, 791.054], [12, 200.71800000000002, 1174.5720000000001, 796.316, 819.118], [12, 200.71800000000002, 390.285, 847.182, 869.984], [12, 224.25900000000001, 649.2360000000001, 875.246, 898.048], [12, 224.25900000000001, 934.2060000000001, 901.556, 924.358], [12, 224.25900000000001, 911.9040000000001, 927.866, 950.668], [12, 224.25900000000001, 1174.5720000000001, 954.176, 976.978], [12, 200.71800000000002, 1174.5720000000001, 982.24, 1005.042], [12, 200.71800000000002, 1174.5720000000001, 1008.55, 1031.352], [12, 200.71800000000002, 1174.5720000000001, 1034.86, 1057.662], [12, 200.71800000000002, 1075.452, 1061.17, 1083.972], [12, 224.25900000000001, 1184.4840000000002, 1087.48, 1110.282], [12, 200.71800000000002, 1174.5720000000001, 1115.544, 1138.346], [12, 224.25900000000001, 560.028, 1141.854, 1164.656], [12, 224.25900000000001, 695.0790000000001, 1168.164, 1190.966], [12, 224.25900000000001, 801.633, 1194.474, 1217.276], [12, 224.25900000000001, 706.23, 1222.538, 1245.34], [12, 224.25900000000001, 934.2060000000001, 1248.848, 1271.65], [12, 224.25900000000001, 495.6, 1275.158, 1297.96], [12, 551.355, 698.796, 1336.548, 1357.596], [12, 1134.9240000000002, 1169.616, 1718.92, 1741.722], [13, 429.93300000000005, 878.451, 566.542, 598.114], [13, 519.1410000000001, 704.9910000000001, 615.654, 648.98], [13, 50.79900000000001, 104.07600000000001, 657.75, 682.306], [13, 173.46, 1012.263, 657.75, 682.306], [13, 50.79900000000001, 441.08400000000006, 689.322, 713.878], [13, 607.11, 830.1300000000001, 689.322, 713.878], [13, 218.06400000000002, 626.9340000000001, 724.402, 747.204], [13, 53.277, 127.617, 787.546, 810.348], [13, 54.516000000000005, 140.007, 819.118, 841.92], [13, 54.516000000000005, 208.15200000000002, 850.69, 873.492], [13, 54.516000000000005, 185.85000000000002, 882.2620000000001, 905.064], [13, 252.75600000000003, 397.71900000000005, 882.2620000000001, 905.064], [13, 908.1870000000001, 1142.3580000000002, 913.834, 954.176], [13, 548.8770000000001, 695.0790000000001, 1329.532, 1352.334]]
2026-08-10 11:55:02,357 INFO     29 [qwen-vl-text] ═══ DONE ═══ 103 positions, pages=4, time=85.0s
2026-08-10 11:55:02,375 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 11:55:02,375 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:Clinical | outputs={"chunks": "6 items, types={'OutpatientRecord': 6}", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:55:02,375 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 11:55:02,376 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:55:02.375+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:55:02,385 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:02,386 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:55:03,666 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:03,675 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 11:55:03,676 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:55:03,676 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 11:55:03,682 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:55:03,683 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:55:03,683 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:55:03,683 INFO     29 [qwen-vl-text] positions(23): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:55:03,683 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [23]
2026-08-10 11:55:04,043 INFO     29 [qwen-vl-text] page=1, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:55:04,045 INFO     29 [qwen-vl-text] LLM extraction start, text_len=279
2026-08-10 11:55:04,045 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:04,045 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 50, \"bbox_end\": 72, \"encounter_dates\": [\"2026-02-24\"], \"department\": \"互联网医院门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "65753497\n就诊类型: 门诊\n就诊时间: 2026-02-24 21:35:00\n接诊年龄: 62岁\n闭环\n历web版\n2026年3月12日 12:21:13\n姓名:\n性别: 女\n年龄: 63岁\n门诊卡号: 0009922109\n科室: 互联网医院门诊\n主诊断: 支气管哮喘\n门诊医嘱\n门诊医嘱\n开立时间\n开立医生\n▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入\n2026/02/24 22:19\n燕海英\n集采7*甲泼尼龙片(兴)(基) 1盒 20mg 每日1次 口服\n2026/02/25 09:00\n燕海英",
    "role": "user"
  }
]
2026-08-10 11:55:06,616 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:06,616 INFO     29 [qwen-vl-text] LLM output (len=690):
{
  "encounter_date": "2026-02-25",
  "prescription_type": "门诊处方",
  "prescriber": "燕海英",
  "department": "互联网医院门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭(兴)",
      "drug_category": "西药",
      "dosage": "50/500",
      "frequency": "每日2次",
      "route": "经口吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": "1泡"
    },
    {
      "drug_generic_name": "甲泼尼龙片",
      "drug_trade_name": "甲泼尼龙片(兴)(基)",
      "drug_category": "西药",
      "dosage": "20mg",
      "frequency": "每日1次",
      "route": "口服",
      "duration_days": null,
      "quantity": "1盒",
      "notes": "集采"
    }
  ]
}
2026-08-10 11:55:06,616 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-25]
2026-08-10 11:55:06,621 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1545375, prompt_len=961
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["65753497", "就诊类型: 门诊", "就诊时间: 2026-02-24 21:35:00", "接诊年龄: 62岁", "闭环", "历web版", "2026年3月12日 12:21:13", "姓名:", "性别: 女", "年龄: 63岁", "门诊卡号: 0009922109", "科室: 互联网医院门诊", "主诊断: 支气管哮喘", "门诊医嘱", "门诊医嘱", "开立时间", "开立医生", "▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入", "2026/02/24 22:19", "燕海英", "集采7*甲泼尼龙片(兴)(基) 1盒 20mg 每日1次 口服", "2026/02/25 09:00", "燕海英"]

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
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord API raw response (len=1282):
[
	{"text": "65753497", "bbox": [8, 381, 55, 390]},
	{"text": "就诊类型: 门诊", "bbox": [68, 381, 140, 390]},
	{"text": "就诊时间: 2026-02-24 21:35:00", "bbox": [152, 381, 303, 390]},
	{"text": "接诊年龄: 62岁", "bbox": [315, 381, 389, 390]},
	{"text": "闭环", "bbox": [928, 378, 954, 392]},
	{"text": "历web版", "bbox": [8, 412, 67, 424]},
	{"text": "2026年3月12日 12:21:13", "bbox": [893, 413, 991, 421]},
	{"text": "姓名:", "bbox": [43, 435, 68, 444]},
	{"text": "性别: 女", "bbox": [113, 435, 155, 444]},
	{"text": "年龄: 63岁", "bbox": [173, 435, 227, 444]},
	{"text": "门诊卡号: 0009922109", "bbox": [247, 435, 361, 444]},
	{"text": "科室: 互联网医院门诊", "bbox": [378, 435, 478, 444]},
	{"text": "主诊断: 支气管哮喘", "bbox": [497, 435, 587, 444]},
	{"text": "门诊医嘱", "bbox": [82, 456, 129, 465]},
	{"text": "门诊医嘱", "bbox": [386, 482, 427, 490]},
	{"text": "开立时间", "bbox": [812, 482, 853, 490]},
	{"text": "开立医生", "bbox": [939, 482, 980, 490]},
	{"text": "▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入", "bbox": [68, 501, 405, 509]},
	{"text": "2026/02/24 22:19", "bbox": [790, 501, 874, 509]},
	{"text": "燕海英", "bbox": [943, 501, 975, 509]},
	{"text": "集采7*甲泼尼龙片(兴)(基) 1盒 20mg 每日1次 口服", "bbox": [67, 519, 293, 527]},
	{"text": "2026/02/25 09:00", "bbox": [790, 519, 874, 527]},
	{"text": "燕海英", "bbox": [943, 519, 975, 527]}
]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=15.0s
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[0]: text=65753497, bbox=[8, 381, 55, 390]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[1]: text=就诊类型: 门诊, bbox=[68, 381, 140, 390]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[2]: text=就诊时间: 2026-02-24 21:35:00, bbox=[152, 381, 303, 390]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[3]: text=接诊年龄: 62岁, bbox=[315, 381, 389, 390]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[4]: text=闭环, bbox=[928, 378, 954, 392]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[5]: text=历web版, bbox=[8, 412, 67, 424]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[6]: text=2026年3月12日 12:21:13, bbox=[893, 413, 991, 421]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[43, 435, 68, 444]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[8]: text=性别: 女, bbox=[113, 435, 155, 444]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[9]: text=年龄: 63岁, bbox=[173, 435, 227, 444]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[10]: text=门诊卡号: 0009922109, bbox=[247, 435, 361, 444]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[11]: text=科室: 互联网医院门诊, bbox=[378, 435, 478, 444]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[12]: text=主诊断: 支气管哮喘, bbox=[497, 435, 587, 444]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[13]: text=门诊医嘱, bbox=[82, 456, 129, 465]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[14]: text=门诊医嘱, bbox=[386, 482, 427, 490]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[15]: text=开立时间, bbox=[812, 482, 853, 490]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[16]: text=开立医生, bbox=[939, 482, 980, 490]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[17]: text=▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入, bbox=[68, 501, 405, 509]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[18]: text=2026/02/24 22:19, bbox=[790, 501, 874, 509]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[19]: text=燕海英, bbox=[943, 501, 975, 509]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[20]: text=集采7*甲泼尼龙片(兴)(基) 1盒 20mg 每日1次 口服, bbox=[67, 519, 293, 527]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[21]: text=2026/02/25 09:00, bbox=[790, 519, 874, 527]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] coord item[22]: text=燕海英, bbox=[943, 519, 975, 527]
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] page=1 — 23/23 coords, api_time=15.0s
2026-08-10 11:55:21,627 INFO     29 [qwen-vl-text] new_positions (23):
[[1, 9.912, 68.14500000000001, 668.274, 684.06], [1, 84.25200000000001, 173.46, 668.274, 684.06], [1, 188.328, 375.41700000000003, 668.274, 684.06], [1, 390.285, 481.97100000000006, 668.274, 684.06], [1, 1149.7920000000001, 1182.006, 663.0120000000001, 687.568], [1, 9.912, 83.013, 722.648, 743.696], [1, 1106.4270000000001, 1227.8490000000002, 724.402, 738.434], [1, 53.277, 84.25200000000001, 762.99, 778.776], [1, 140.007, 192.04500000000002, 762.99, 778.776], [1, 214.347, 281.25300000000004, 762.99, 778.776], [1, 306.033, 447.27900000000005, 762.99, 778.776], [1, 468.34200000000004, 592.2420000000001, 762.99, 778.776], [1, 615.783, 727.293, 762.99, 778.776], [1, 101.59800000000001, 159.83100000000002, 799.824, 815.61], [1, 478.254, 529.053, 845.428, 859.46], [1, 1006.0680000000001, 1056.8670000000002, 845.428, 859.46], [1, 1163.421, 1214.22, 845.428, 859.46], [1, 84.25200000000001, 501.795, 878.754, 892.7860000000001], [1, 978.8100000000001, 1082.8860000000002, 878.754, 892.7860000000001], [1, 1168.3770000000002, 1208.025, 878.754, 892.7860000000001], [1, 83.013, 363.02700000000004, 910.326, 924.358], [1, 978.8100000000001, 1082.8860000000002, 910.326, 924.358], [1, 1168.3770000000002, 1208.025, 910.326, 924.358]]
2026-08-10 11:55:21,628 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=17.9s
2026-08-10 11:55:21,628 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:55:21,628 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:55:21,629 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:55:21,629 INFO     29 [qwen-vl-text] positions(25): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:55:21,629 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [25]
2026-08-10 11:55:21,985 INFO     29 [qwen-vl-text] page=3, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:55:21,988 INFO     29 [qwen-vl-text] LLM extraction start, text_len=284
2026-08-10 11:55:21,988 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:21,989 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 110, \"bbox_end\": 134, \"encounter_dates\": [\"2026-01-23\"], \"department\": \"互联网医院门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "生日: 196****16\n过敏史: 否\n62岁\n身份证号: 510***********045\n更多\n005\n就诊类型: 门诊\n就诊时间: 2026-01-23 13:19:40\n接诊年龄: 62岁\n闭环\neb版\n2026年3月12日 12:22:03 注销\n姓名:\n性别: 女\n年龄: 63岁\n门诊卡号: 0009922109\n科室: 互联网医院门诊\n主诊断: 支气管哮喘\n门诊医嘱\n门诊医嘱\n开立时间\n开立医生\n259698508 ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入\n2026/01/23 13:48\n燕海英",
    "role": "user"
  }
]
2026-08-10 11:55:24,266 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:24,266 INFO     29 [qwen-vl-text] LLM output (len=427):
{
  "encounter_date": "2026-01-23",
  "prescription_type": "门诊处方",
  "prescriber": "燕海英",
  "department": "互联网医院门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭(兴)",
      "drug_category": "西药",
      "dosage": "50/500",
      "frequency": "每日2次",
      "route": "经口吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": "1泡"
    }
  ]
}
2026-08-10 11:55:24,266 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-23]
2026-08-10 11:55:24,269 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1595229, prompt_len=972
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["生日: 196****16", "过敏史: 否", "62岁", "身份证号: 510***********045", "更多", "005", "就诊类型: 门诊", "就诊时间: 2026-01-23 13:19:40", "接诊年龄: 62岁", "闭环", "eb版", "2026年3月12日 12:22:03 注销", "姓名:", "性别: 女", "年龄: 63岁", "门诊卡号: 0009922109", "科室: 互联网医院门诊", "主诊断: 支气管哮喘", "门诊医嘱", "门诊医嘱", "开立时间", "开立医生", "259698508 ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入", "2026/01/23 13:48", "燕海英"]

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
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord API raw response (len=1368):
[
	{"text": "生日: 196****16", "bbox": [7, 345, 88, 354]},
	{"text": "过敏史: 否", "bbox": [128, 345, 175, 354]},
	{"text": "62岁", "bbox": [19, 358, 42, 367]},
	{"text": "身份证号: 510***********045", "bbox": [84, 358, 206, 367]},
	{"text": "更多", "bbox": [265, 358, 284, 367]},
	{"text": "005", "bbox": [7, 375, 25, 383]},
	{"text": "就诊类型: 门诊", "bbox": [40, 375, 111, 383]},
	{"text": "就诊时间: 2026-01-23 13:19:40", "bbox": [125, 375, 274, 383]},
	{"text": "接诊年龄: 62岁", "bbox": [288, 375, 361, 383]},
	{"text": "闭环", "bbox": [911, 375, 932, 383]},
	{"text": "eb版", "bbox": [4, 407, 35, 417]},
	{"text": "2026年3月12日 12:22:03 注销", "bbox": [871, 407, 997, 415]},
	{"text": "姓名:", "bbox": [11, 430, 35, 438]},
	{"text": "性别: 女", "bbox": [85, 430, 123, 438]},
	{"text": "年龄: 63岁", "bbox": [142, 430, 195, 438]},
	{"text": "门诊卡号: 0009922109", "bbox": [215, 430, 331, 438]},
	{"text": "科室: 互联网医院门诊", "bbox": [350, 430, 451, 438]},
	{"text": "主诊断: 支气管哮喘", "bbox": [470, 430, 560, 438]},
	{"text": "门诊医嘱", "bbox": [50, 451, 97, 460]},
	{"text": "门诊医嘱", "bbox": [390, 478, 430, 487]},
	{"text": "开立时间", "bbox": [798, 478, 838, 487]},
	{"text": "开立医生", "bbox": [920, 478, 961, 487]},
	{"text": "259698508 ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入", "bbox": [28, 497, 425, 506]},
	{"text": "2026/01/23 13:48", "bbox": [774, 497, 860, 506]},
	{"text": "燕海英", "bbox": [924, 497, 955, 506]}
]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=15.0s
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[0]: text=生日: 196****16, bbox=[7, 345, 88, 354]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[1]: text=过敏史: 否, bbox=[128, 345, 175, 354]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[2]: text=62岁, bbox=[19, 358, 42, 367]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[3]: text=身份证号: 510***********045, bbox=[84, 358, 206, 367]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[4]: text=更多, bbox=[265, 358, 284, 367]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[5]: text=005, bbox=[7, 375, 25, 383]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[6]: text=就诊类型: 门诊, bbox=[40, 375, 111, 383]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[7]: text=就诊时间: 2026-01-23 13:19:40, bbox=[125, 375, 274, 383]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[8]: text=接诊年龄: 62岁, bbox=[288, 375, 361, 383]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[9]: text=闭环, bbox=[911, 375, 932, 383]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[10]: text=eb版, bbox=[4, 407, 35, 417]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[11]: text=2026年3月12日 12:22:03 注销, bbox=[871, 407, 997, 415]
2026-08-10 11:55:39,258 INFO     29 [qwen-vl-text] coord item[12]: text=姓名:, bbox=[11, 430, 35, 438]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[13]: text=性别: 女, bbox=[85, 430, 123, 438]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[14]: text=年龄: 63岁, bbox=[142, 430, 195, 438]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[15]: text=门诊卡号: 0009922109, bbox=[215, 430, 331, 438]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[16]: text=科室: 互联网医院门诊, bbox=[350, 430, 451, 438]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[17]: text=主诊断: 支气管哮喘, bbox=[470, 430, 560, 438]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[18]: text=门诊医嘱, bbox=[50, 451, 97, 460]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[19]: text=门诊医嘱, bbox=[390, 478, 430, 487]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[20]: text=开立时间, bbox=[798, 478, 838, 487]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[21]: text=开立医生, bbox=[920, 478, 961, 487]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[22]: text=259698508 ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入, bbox=[28, 497, 425, 506]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[23]: text=2026/01/23 13:48, bbox=[774, 497, 860, 506]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] coord item[24]: text=燕海英, bbox=[924, 497, 955, 506]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] page=3 — 25/25 coords, api_time=15.0s
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] new_positions (25):
[[3, 8.673, 109.03200000000001, 605.13, 620.916], [3, 158.592, 216.82500000000002, 605.13, 620.916], [3, 23.541, 52.038000000000004, 627.932, 643.718], [3, 104.07600000000001, 255.234, 627.932, 643.718], [3, 328.33500000000004, 351.87600000000003, 627.932, 643.718], [3, 8.673, 30.975, 657.75, 671.782], [3, 49.56, 137.52900000000002, 657.75, 671.782], [3, 154.875, 339.48600000000005, 657.75, 671.782], [3, 356.83200000000005, 447.27900000000005, 657.75, 671.782], [3, 1128.729, 1154.748, 657.75, 671.782], [3, 4.956, 43.365, 713.878, 731.418], [3, 1079.169, 1235.2830000000001, 713.878, 727.91], [3, 13.629000000000001, 43.365, 754.22, 768.252], [3, 105.31500000000001, 152.39700000000002, 754.22, 768.252], [3, 175.93800000000002, 241.60500000000002, 754.22, 768.252], [3, 266.38500000000005, 410.10900000000004, 754.22, 768.252], [3, 433.65000000000003, 558.7890000000001, 754.22, 768.252], [3, 582.33, 693.84, 754.22, 768.252], [3, 61.95, 120.183, 791.054, 806.84], [3, 483.21000000000004, 532.7700000000001, 838.412, 854.198], [3, 988.7220000000001, 1038.2820000000002, 838.412, 854.198], [3, 1139.88, 1190.679, 838.412, 854.198], [3, 34.692, 526.575, 871.738, 887.524], [3, 958.9860000000001, 1065.5400000000002, 871.738, 887.524], [3, 1144.836, 1183.2450000000001, 871.738, 887.524]]
2026-08-10 11:55:39,259 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=17.6s
2026-08-10 11:55:39,259 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:55:39,265 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:55:39,265 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:55:39,265 INFO     29 [qwen-vl-text] positions(22): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:55:39,265 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [22]
2026-08-10 11:55:39,654 INFO     29 [qwen-vl-text] page=9, rect=1239x1754, img=(3442x4873), dpi=200
2026-08-10 11:55:39,656 INFO     29 [qwen-vl-text] LLM extraction start, text_len=298
2026-08-10 11:55:39,656 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:39,656 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 318, \"bbox_end\": 339, \"encounter_dates\": [\"2025-09-02\"], \"department\": \"互联网医院门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "出生日期: 196******16\n过敏史: 无\n年龄: 62岁\n身份证号: 510***********045\n更多\n548559 就诊类型: 门诊 就诊时间: 2025-09-02 13:50:11 接诊年龄: 62岁\n闭环\nweb版\n2026年3月12日 12:26:27\n姓名\n性别: 女\n年龄: 63岁\n门诊卡号: 0009922109\n科室: 互联网医院门诊\n主诊断: 支气管哮喘\n门诊医嘱\n门诊医嘱\n开立时间\n开立医生\n244166554 省集11*▲布地奈德福莫特罗吸入粉雾剂(II)信必可都保(基)(兴) 2盒 2吸 每日2次 经口吸入\n2025/09/03 09:14\n燕海英",
    "role": "user"
  }
]
2026-08-10 11:55:39,658 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:55:39.657+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 25, "failed": 0, "current": {"4e7a239e94b111f1bd9827cf206dfa2d": {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:55:41,808 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:41,808 INFO     29 [qwen-vl-text] LLM output (len=427):
{
  "encounter_date": "2025-09-03",
  "prescription_type": "门诊处方",
  "prescriber": "燕海英",
  "department": "互联网医院门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "布地奈德福莫特罗吸入粉雾剂(II)",
      "drug_trade_name": "信必可都保",
      "drug_category": "西药",
      "dosage": "2吸",
      "frequency": "每日2次",
      "route": "经口吸入",
      "duration_days": null,
      "quantity": "2盒",
      "notes": null
    }
  ]
}
2026-08-10 11:55:41,809 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-03]
2026-08-10 11:55:41,813 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2049490, prompt_len=977
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["出生日期: 196******16", "过敏史: 无", "年龄: 62岁", "身份证号: 510***********045", "更多", "548559 就诊类型: 门诊 就诊时间: 2025-09-02 13:50:11 接诊年龄: 62岁", "闭环", "web版", "2026年3月12日 12:26:27", "姓名", "性别: 女", "年龄: 63岁", "门诊卡号: 0009922109", "科室: 互联网医院门诊", "主诊断: 支气管哮喘", "门诊医嘱", "门诊医嘱", "开立时间", "开立医生", "244166554 省集11*▲布地奈德福莫特罗吸入粉雾剂(II)信必可都保(基)(兴) 2盒 2吸 每日2次 经口吸入", "2025/09/03 09:14", "燕海英"]

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
2026-08-10 11:55:57,262 INFO     29 [qwen-vl-text] coord API raw response (len=1255):
[
	{"text": "出生日期: 196******16", "bbox": [10, 330, 102, 340]},
	{"text": "过敏史: 无", "bbox": [141, 330, 190, 340]},
	{"text": "年龄: 62岁", "bbox": [10, 343, 56, 352]},
	{"text": "身份证号: 510***********045", "bbox": [97, 343, 220, 352]},
	{"text": "更多", "bbox": [279, 343, 298, 352]},
	{"text": "548559 就诊类型: 门诊 就诊时间: 2025-09-02 13:50:11 接诊年龄: 62岁", "bbox": [2, 360, 376, 370]},
	{"text": "闭环", "bbox": [927, 360, 948, 370]},
	{"text": "web版", "bbox": [5, 393, 49, 403]},
	{"text": "2026年3月12日 12:26:27", "bbox": [888, 393, 987, 402]},
	{"text": "姓名", "bbox": [24, 414, 44, 423]},
	{"text": "性别: 女", "bbox": [95, 414, 136, 423]},
	{"text": "年龄: 63岁", "bbox": [155, 414, 208, 423]},
	{"text": "门诊卡号: 0009922109", "bbox": [228, 414, 345, 423]},
	{"text": "科室: 互联网医院门诊", "bbox": [363, 414, 465, 423]},
	{"text": "主诊断: 支气管哮喘", "bbox": [483, 414, 574, 423]},
	{"text": "门诊医嘱", "bbox": [62, 437, 109, 447]},
	{"text": "门诊医嘱", "bbox": [416, 464, 458, 473]},
	{"text": "开立时间", "bbox": [830, 464, 871, 473]},
	{"text": "开立医生", "bbox": [940, 464, 981, 473]},
	{"text": "244166554 省集11*▲布地奈德福莫特罗吸入粉雾剂(II)信必可都保(基)(兴) 2盒 2吸 每日2次 经口吸入", "bbox": [41, 483, 496, 492]},
	{"text": "2025/09/03 09:14", "bbox": [805, 483, 892, 492]},
	{"text": "燕海英", "bbox": [943, 483, 974, 492]}
]
2026-08-10 11:55:57,263 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=15.4s
2026-08-10 11:55:57,263 INFO     29 [qwen-vl-text] coord item[0]: text=出生日期: 196******16, bbox=[10, 330, 102, 340]
2026-08-10 11:55:57,263 INFO     29 [qwen-vl-text] coord item[1]: text=过敏史: 无, bbox=[141, 330, 190, 340]
2026-08-10 11:55:57,263 INFO     29 [qwen-vl-text] coord item[2]: text=年龄: 62岁, bbox=[10, 343, 56, 352]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[3]: text=身份证号: 510***********045, bbox=[97, 343, 220, 352]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[4]: text=更多, bbox=[279, 343, 298, 352]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[5]: text=548559 就诊类型: 门诊 就诊时间: 2025-09-02 13:50:11 接诊年龄: 62岁, bbox=[2, 360, 376, 370]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[6]: text=闭环, bbox=[927, 360, 948, 370]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[7]: text=web版, bbox=[5, 393, 49, 403]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[8]: text=2026年3月12日 12:26:27, bbox=[888, 393, 987, 402]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[9]: text=姓名, bbox=[24, 414, 44, 423]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[10]: text=性别: 女, bbox=[95, 414, 136, 423]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[11]: text=年龄: 63岁, bbox=[155, 414, 208, 423]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[12]: text=门诊卡号: 0009922109, bbox=[228, 414, 345, 423]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[13]: text=科室: 互联网医院门诊, bbox=[363, 414, 465, 423]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[14]: text=主诊断: 支气管哮喘, bbox=[483, 414, 574, 423]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[15]: text=门诊医嘱, bbox=[62, 437, 109, 447]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[16]: text=门诊医嘱, bbox=[416, 464, 458, 473]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[17]: text=开立时间, bbox=[830, 464, 871, 473]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[18]: text=开立医生, bbox=[940, 464, 981, 473]
2026-08-10 11:55:57,264 INFO     29 [qwen-vl-text] coord item[19]: text=244166554 省集11*▲布地奈德福莫特罗吸入粉雾剂(II)信必可都保(基)(兴) 2盒 2吸 每日2次 经口吸入, bbox=[41, 483, 496, 492]
2026-08-10 11:55:57,265 INFO     29 [qwen-vl-text] coord item[20]: text=2025/09/03 09:14, bbox=[805, 483, 892, 492]
2026-08-10 11:55:57,265 INFO     29 [qwen-vl-text] coord item[21]: text=燕海英, bbox=[943, 483, 974, 492]
2026-08-10 11:55:57,266 INFO     29 [qwen-vl-text] page=9 — 22/22 coords, api_time=15.4s
2026-08-10 11:55:57,266 INFO     29 [qwen-vl-text] new_positions (22):
[[9, 12.39, 126.37800000000001, 578.82, 596.36], [9, 174.699, 235.41000000000003, 578.82, 596.36], [9, 12.39, 69.384, 601.622, 617.408], [9, 120.183, 272.58000000000004, 601.622, 617.408], [9, 345.68100000000004, 369.22200000000004, 601.622, 617.408], [9, 2.478, 465.86400000000003, 631.44, 648.98], [9, 1148.553, 1174.5720000000001, 631.44, 648.98], [9, 6.195, 60.711000000000006, 689.322, 706.862], [9, 1100.2320000000002, 1222.893, 689.322, 705.108], [9, 29.736000000000004, 54.516000000000005, 726.156, 741.942], [9, 117.70500000000001, 168.50400000000002, 726.156, 741.942], [9, 192.04500000000002, 257.71200000000005, 726.156, 741.942], [9, 282.492, 427.45500000000004, 726.156, 741.942], [9, 449.75700000000006, 576.135, 726.156, 741.942], [9, 598.437, 711.186, 726.156, 741.942], [9, 76.81800000000001, 135.05100000000002, 766.498, 784.038], [9, 515.4240000000001, 567.4620000000001, 813.856, 829.642], [9, 1028.3700000000001, 1079.169, 813.856, 829.642], [9, 1164.66, 1215.459, 813.856, 829.642], [9, 50.79900000000001, 614.5440000000001, 847.182, 862.968], [9, 997.3950000000001, 1105.188, 847.182, 862.968], [9, 1168.3770000000002, 1206.786, 847.182, 862.968]]
2026-08-10 11:55:57,267 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=18.0s
2026-08-10 11:55:57,278 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:55:57,278 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:Prescription | outputs={"chunks": "3 items, types={'PrescriptionRecord': 3}", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:55:57,279 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:55:57,286 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:57,286 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:55:58,098 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:58,106 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:55:58,107 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:55:58,107 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:55:58,114 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:58,115 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:55:58,655 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:58,667 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:55:58,667 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:55:58,667 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:55:58,675 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:58,676 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:55:59,797 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:59,810 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:55:59,811 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:55:59,811 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:55:59,823 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:55:59,823 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:56:00,297 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:56:00,303 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:56:00,304 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "449 items", "markdown": "", "text": "", "name": "MARO-四川省人民.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Prescription\": 3, \"chunks_LabExam\": 1}"}
2026-08-10 11:56:00,304 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:56:00,305 INFO     29 [ChunkMerger] Merged 10 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 6, 'Extractor:Medication': 1, 'Extractor:Prescription': 3, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 11:56:00,320 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:56:00,320 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "10 items, types={'LabReport': 1, 'OutpatientRecord': 6, 'PrescriptionRecord': 3}", "name": "MARO-四川省人民.pdf"}
2026-08-10 11:56:00,320 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:56:00,497 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786362470177, 'update_date': datetime.datetime(2026, 8, 10, 11, 47, 50), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 945373, 'status': '1'}
2026-08-10 11:56:00,724 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   *白细胞计数  WBC  6.65  10^9/L  3.50--9.50  False    中性粒细胞数  NEUT#  4.47  10^9/L  1.80--6.30  False    淋巴细胞数  LYMPH#  1.41  10^9/L  1.10--3.20  False    单核细胞数  MONO#  0.33  10^9/L  0.10--0.60  False    嗜酸性粒细胞数  EOS#  0.40  10^9/L  0.02--0.52  False    嗜碱性粒细胞数  BASO#  0.04  10^9/L  0.00--0.06  False    中性粒细胞率  NEUT%  67.2  %  40.0--75.0  False    淋巴细胞率  LYMPH%  21.2  %  20.0--50.0  False    单核细胞率  MONO%  5.0  %  3.0--10.0  False    嗜酸性粒细胞率  EOS%  6.0  %  0.4--8.0  False    嗜碱性粒细胞率  BASO%  0.6  %  0--1.0  False    *红细胞计数  RBC  4.66  10^12/L  3.80--5.10  False    *血红蛋白量  HGB  131  g/L  115--150  False    *红细胞比积  HCT  42.5  %  35.0--45.0  False    *平均红细胞体积  MCV  91.1  fL  82.0--100.0  False    *平均红细胞血红蛋白量  MCH  28.1  pg  27.0--34.0  False    *平均红细胞血红蛋白浓度  MCHC  308  g/L  316--354  True    红细胞分布宽度  RDW-SD  48.5  fL  38.4--47.8  True    *血小板计数  PLT  178  10^9/L  101--320  False    中性粒细胞率  NEUT%  67.2  %  40.0--75.0  False    淋巴细胞率  LYMPH%  21.2  %  20.0--50.0  False    单核细胞率  MONO%  5.0  %  3.0--10.0  False    嗜酸性粒细胞率  EOS%  6.0  %  0.4--8.0  False    嗜碱性粒细胞率  BASO%  0.6  %  0--1.0  False    红细胞计数  RBC  4.66  10^12/L  3.80--5.10  False    血红蛋白量  HGB  131  g/L  115--150  False    红细胞比积  HCT  42.5  %  35.0--45.0  False    平均红细胞体积  MCV  91.1  fL  82.0--100.0  False    平均红细胞血红蛋白量  MCH  28.1  pg  27.0--34.0  False    平均红细胞血红蛋白浓度  MCHC  308  g/L  316--354  True    红细胞分布宽度  RDW-SD  48.5  fL  38.4--47.8  True    血小板计数  PLT  178  10^9/L  101--320  False   
---
门诊
就诊时间: 2026-03-10 19:04:14 接诊年龄: 62岁
闭环
病历详情
病历文档
四川省醫學科學院·四川省人民醫院
门诊病历
姓名:
别: 女年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109
住址: 四川省成都******* 联系电话: 133****6101 挂号流水号: 66150482
复诊记录
记录时间: 2026-03-10 19:04
主诉:
支气管哮喘复诊
简要病史:
支气管哮喘复诊, 目前哮喘症状稳定
既往病史:
阴性
过敏史:
阴性
流行病学
史:
阴性
体格检查:
阴性
门诊诊断:
支气管哮喘
处置:
继续使用舒利迭控制哮喘
婚姻史: 月经史:
是否下转: 否, 是否外伤: 否, 是否美容: 否
医师签名:
燕海荣
---
四川省医学科学院四川省人民医院
互联网门诊病历
姓名:
性别:女
年龄:62
门诊科室:互联网医院门诊
门诊病历号:0009922109
工作单位或住址:四川省成都市邛崃市临邛街道
联系电话:
复诊记录
记录时间:2026-02-24 22:18
主诉:咳嗽,喘息,加重3天
简要病史:咳嗽,喘息,加重3天,3天前受凉后出现喘息加重,无发热。
既往病史:
过敏史:
流行病学史:无
体格检查:无
门诊诊断:支气管哮喘,支气管哮喘急性发作
处理意见:无
是否下转:否
是否外伤:否
是否美容:否
是否体检:否
燕海荣
医师签名:
---
四川省医学科学院四川省人民医院
互联网门诊病历
姓名
性别：女
年龄：62
门诊科室：互联网医院门诊
门诊病历号：0009922109
工作单位或住址：四川省成都市邛崃市临邛街道
联系电话：
复诊记录
记录时间：2026-01-23 13:20
主诉：支气管哮喘
简要病史：支气管哮喘
既往病史：
过敏史：
流行病学史：无
体格检查：无
门诊诊断：支气管哮喘
处理意见：无
是否下转：否
是否外伤：否
是否美容：否
是否体检：否
燕海荣
医师签名：
---
流水号: 64363836 就诊类型: 门诊 就诊时间: 2025-12-29 10:01:20 接诊年龄: 62岁
闭环
病历详情
病历文档
四川省醫學科學院·四川省人民醫院
门诊病历
姓名:
性别: 女 年龄: 62岁 门诊科室: 呼吸与危重症医学科门诊 门诊病历号: 0009922109
住址: 四川省成都******** 联系电话: 133****6101 挂号流水号: 64363836
复诊记录
记录时间: 2025-12-29 10:38
主诉: 发作性喘息。
简要病史: 哮喘复诊, 1周前吼喘一次持续3天, 自觉呼吸困难
既往病史: 焦虑型抑郁症
过敏史: 有过敏源
流行病学
史: /
体格检查: 指尖氧饱和度95%, 心率78次/分
门诊诊断: 哮喘急性发作、失眠
处置: 血eos 0.4
集采7*甲泼尼龙片(兴)(基)20mg/次 口服 每日1次 6天
▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500)1泡/次 经口吸入 每日2次 31天
阿育吠陀片(精2)(基)0.4mg/次 口服 每晚1次 20天
血细胞分析(CBC+DIFF)
婚姻史: 月经史:
是否下转: 否, 是否外伤: 否, 是否美容: 否
医师签名: 燕海荣
---
就诊类型: 门诊
就诊时间: 2025-12-09 17:00:36
接诊年龄: 62岁
闭环
病历详情
病历文档
四川省醫學科學院·四川省人民醫院
门诊病历
姓名:
性别: 女年龄: 62岁门诊科室: 呼吸与危重症医学科门诊门诊病历号: 0009922109
住址: 四川省成都市邛崃市联系电话: 133****6101挂号流水号: 63931786
复诊记录
记录时间: 2025-12-09 17:00
主诉: 发作性喘息, 参加LOGOS (D5982C00008) 临床研究, 今日行电话回访。
简要病史: 哮喘病史
既往病史: 焦虑型抑郁症
过敏史: 有过敏源花粉过敏, 未见报告, 具体不详
流行病学史: /
体格检查: NA
门诊诊断: 哮喘
处置: 今日15:35对受试者行电话回访, 受试者电话: 133****6101, 感谢受试者参加有关布地奈德、格隆溴铵和富马酸福莫特罗吸入器 (也简称为BGFMDI或PT010) 的临床试验, 该临床试验是一项双盲研究, 在所有临床试验受试者的通力配合下, 研究人员正在查明此药物是否有助于治疗哮喘患者。试验开始时, 受试者已经知道会接受BGF MDI、布地奈德和富马酸福莫特罗 (也简称为BFF MDI) 或Symbicort, 接受BGF MDI或BFF MDI的参加者也接受了看起来像Symbicort的安慰剂吸入器。接受了Symbicort的参加者还接受了看起来BGF MDI和BFF MDI的安慰剂吸入器, 安慰剂外观像研究治疗药物, 但其中不含任何药物。患者也知道, 任何人 (包括研究者和试验工作人员在内) 在试验结束之前都不知道您接受的是哪种治疗。
告知受试者本试验已结束, 可告知患者接受的是布地奈德和富马酸福莫特罗定量吸入器 (BFF MDI), 受试者无疑问, 嘱受试者注意休息, 避免受凉感冒, 行肺功能锻炼, 病情加重时及时就诊。
告知受试者可以通过trialsunmaries.com网站在线查看总体研究结果的摘要, 可使用D5982C00008在上述网站搜索本试验, 此网站不会收集、储存或使用可用于识别受试者的身份信息, 该摘要将为受试者介绍本试验的总体结果。
婚烟史: 月经史:
是否下转: 否。是否外伤: 否。是否美容: 否
共2页, 第2页
医师签名: 张利
---
四川省医学科学院·四川省人民医院
门诊病历
姓名：
性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109
住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667
复诊记录
记录时间：2024-04-15 09:26
主诉：发作性喘息，参加LOGOS（D5982C00008）临床研究，行V1访视
简要病史：患者今日7:40到院，自诉：哮喘病史：于2022年5月UK日首次出现哮喘症状，于2022年5月16日首次
确诊为哮喘，2024年1月15日开始规范使用沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次
经口吸入 每日2次，控制症状，近一年未发生急性加重。
既往病史：焦虑型抑郁症：2021年2月UK日-至今，采取以下药物治疗：
草酸艾司西酞普兰片：2022年2月UK日-至今，20mg/次，qd；
枸橼酸坦度螺酮胶囊：2022年2月UK日-至今，10mg/次，tid。
过敏史：有过敏源花粉 因患者无法记得开始时间，故开始时间不详
流行病学史：此前3个月内，患者无可能相关的视力变化；否认青光眼史；患者不存在具有临床意义的症性前列腺肥大或膀胱颈梗阻
/尿潴留；患者在此前5年内不存在未完全缓解的不可切除的癌症，患者未在既往或当前在任何布地奈德和富马酸福莫特
罗研究(PT009)，布地奈德、格隆安和富马酸福莫特罗(PT010)或格隆安(PT001)中接受随机化；患者无计划研究期间住院，
患者否认访视前1个月内住过院，否认访视前4周内完成对呼吸道感染或哮喘急性发作的全身性激素治疗，否认有危机
生命的哮喘，否认访视1前12个月内已知有药物滥用或酗酒史，否认对β2-激动剂、激素、抗胆碱药或MDI或pMDI中的
任何组分发生超敏反应，否认既往或当前入组AEROSPHERE项目中的研究。
体格检查：神志清楚，精神尚可，呼吸平稳，全身皮肤无黄染，无瘀点、瘀斑，皮肤皮温不高，皮肤无汗湿。浅表淋巴结
未触及，头颅五官无畸形，眼球活动自如，睑结膜无充血苍白，球结膜无水肿，巩膜无黄染。口唇无发绀，
伸舌居中，咽无充血，双侧扁桃体无肿大。颈软，颈静脉充盈，气管居中，甲状腺未扪及肿大。桶状胸，
双肺呼吸音降低，双肺未闻及明显湿性啰音及哮鸣音。心界无明显增大，律齐，各瓣膜区未闻测量血
共4页，第1页
四川省医学科学院·四川省人民医院
门诊病历
姓名：马蓉 性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109
住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667
四川省医学科学院·四川省人民医院
门诊病历
姓名：
性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109
住址：四川省成都市邛崃市 联系电话：
挂号流水号：49735667
压）及病理性杂音。腹软，无压痛、反跳痛及肌紧张，肝脾肋下未触及，肝肾区无叩痛，肠鸣音不活跃。
双下肢对称无明显水肿，四肢肌力及肌张力正常。生命体征详见生命体征表（受试者已在休息5分钟后
取坐位）
门诊诊断：
哮喘
处
置：
知情过程：根据患者已有既往资料的情况，考虑受试者可能符合“一项随机、双盲、双模拟、平行分组、
多中心、24至52周可变时长的研究，评估布地奈德、格隆铵和富马酸福莫特罗定量吸入器（MDI）与布地
奈德和富马酸福莫特罗MDI以及信必可®加压MDI相比在哮喘未充分控制的成人和青少年受试者中的疗
效和安全性（LOGOS）”的临床试验，今日7时55分当面与患者本人及家属进行充分知情，详细讲解本研究
的目的、方法、流程及可能的获益及风险，并给予患者充分的时间考虑，患者仔细阅读无疑问，自愿同意
参加本项临床试验，于2024年4月15日8时15分与患者本人共同签署两份成人研究受试者主要信息
和知情同意书（研究信息和知情同意书）（研究中心版本号1429-2.0，研究中心版本日期：2023年10月
31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日当面与患者本人详细讲解中国个人
信息保护附录相关内容，患者表示无疑问并充分理解接受，于2024年4月15日8时18分签署两份中国
个人信息保护附录（中国个人信息保护附录）（研究中心版本号1429-2.0 研究中心版本日期2023年10
月31日），一份文件交由患者保存，一份原件保存在研究者文件夹。今日同时告知患者12小时PFT子研
究者相关内容，患者表示拒绝。
人口统计学信息：出生日期：1963年8月16日 性别：女 民族：汉族 种族：中国人
患者否认哮喘相关家族史，否认吸烟及饮酒，自诉无输血史及手术史，患者目前已绝经（经期：开始时间：
1978年，结束时间：2014年）。
疫苗接种史：目前已无法查询新冠疫苗接种史，患者自诉2021年-2022年期间接种三针（具体相关信息
无法提供）
共4页，第2页
12
四川省医学科学院·四川省人民医院
门诊病历
姓名：
性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109
住址：四川省成都市邛崃市 联系电话：13348966101 挂号流水号：49735667
询问患者最近一次进食时间，患者自诉19:10，今与患者确认测量前6小时内未使用SABA类药物，并确认前一晚吸入沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/250)1泡/次 经口吸入 每日2次 时间为
20:00，至今未使用任何药物。
患者静息10分钟后以仰卧位行12导联ECG检查，详见ECG报告。在肺功能测量前进行FoNO检测，检测一小时前无饮水及进食，随后行给药前-60min、-30min肺功能检查，患者者给药前FEV1%：78.85%。
检查结果详见报告。
完成ACQ-6及ACQ-7问卷，ACQ-7评分≥1.5。
患者性别：女，已绝经，故未使用中心试验室提供的试剂进行尿妊娠试验。
采集血样；完成血液标本采集后进行处理，并送往中心实验室进行检测。
患者目前符合所有入选标准，不符合任一排除标准，嘱患者自今日起停用沙美特罗替卡松吸入粉雾剂
|舒利迭(兴)(50ug/250ug)1泡/次 经口吸入 每日2次。IRT系统登记，筛选号；E1429021，并获得培训
装置1瓶，药物编号：117165-EQ；获得导入期BFP1瓶，药物编号为；661331-BD。使用培训装置对患者进行
吸入器使用培训及检查吸入装置技术，完成给药培训后当场回收；于11:08指导患者对导入期BFP进行
预喷并给药2喷，给药结束时间为：11:10。发放急救药物万托林1瓶，嘱患者必要时使用。
发放ePRO设备和峰流速仪，协助患者完成使用培训，同时发放白色吸入器使用指南，受试者参与卡。
受试者感谢卡、哮喘监测仪AMS患者快速入门指南、峰流速计AM3使用指南，手持设备患者快速指南。
预约患者下周一来院进行下次访视；
嘱患者带上发放的峰速仪、ePRO以及导入期药物；
嘱患者带上自上次访视以来的住院、门诊、急诊等病历记录；
嘱患者下次访视前急救药物沙丁胺醇暂停≥6小时；
嘱患者下次访视前早间剂量必须暂停，直至完成当此访视所有给药前评价；
嘱患者按要求清洗给药装置；
共4页，第3页
13
四川省医学科学院·四川省人民医院
门诊病历
姓名：
性别：女 年龄：60岁 门诊科室：呼吸与危重症医学科门诊 门诊病历号：0009922109
住址：四川省成都市邛崃市 联系电话：
挂号流水号：49735667
嘱患者用药期间如有任何不适，及时复诊。
婚姻史：
月经史：
是否下转： 否
是否外伤：否
是否美容： 否
医师签名： 燕海荣
共4页，第4页
---
65753497
就诊类型: 门诊
就诊时间: 2026-02-24 21:35:00
接诊年龄: 62岁
闭环
历web版
2026年3月12日 12:21:13
姓名:
性别: 女
年龄: 63岁
门诊卡号: 0009922109
科室: 互联网医院门诊
主诊断: 支气管哮喘
门诊医嘱
门诊医嘱
开立时间
开立医生
▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入
2026/02/24 22:19
燕海英
集采7*甲泼尼龙片(兴)(基) 1盒 20mg 每日1次 口服
2026/02/25 09:00
燕海英
---
生日: 196****16
过敏史: 否
62岁
身份证号: 510***********045
更多
005
就诊类型: 门诊
就诊时间: 2026-01-23 13:19:40
接诊年龄: 62岁
闭环
eb版
2026年3月12日 12:22:03 注销
姓名:
性别: 女
年龄: 63岁
门诊卡号: 0009922109
科室: 互联网医院门诊
主诊断: 支气管哮喘
门诊医嘱
门诊医嘱
开立时间
开立医生
259698508 ▲沙美特罗替卡松吸入粉雾剂|舒利迭(兴)(50/500) 1盒 1泡 每日2次 经口吸入
2026/01/23 13:48
燕海英
---
出生日期: 196******16
过敏史: 无
年龄: 62岁
身份证号: 510***********045
更多
548559 就诊类型: 门诊 就诊时间: 2025-09-02 13:50:11 接诊年龄: 62岁
闭环
web版
2026年3月12日 12:26:27
姓名
性别: 女
年龄: 63岁
门诊卡号: 0009922109
科室: 互联网医院门诊
主诊断: 支气管哮喘
门诊医嘱
门诊医嘱
开立时间
开立医生
244166554 省集11*▲布地奈德福莫特罗吸入粉雾剂(II)信必可都保(基)(兴) 2盒 2吸 每日2次 经口吸入
2025/09/03 09:14
燕海英
2026-08-10 11:56:01,376 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:56:01,376 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "10 items, types={'LabReport': 1, 'OutpatientRecord': 6, 'PrescriptionRecord': 3}", "name": "MARO-四川省人民.pdf", "embedding_token_consumption": 6003}
2026-08-10 11:56:01,377 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:56:01,627 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:56:01,627 INFO     29 [Trace] task=4e7a239e | doc=MARO-四川省人民.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":10,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 11:56:01,632 INFO     29 [DIAG-EXECUTOR] row_position_int len=32 row[0]=(7, 159, 271, 764, 789) row[-1]=(7, 161, 270, 1289, 1311)
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,633 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:56:01,640 INFO     29 set_progress(4e7a239e94b111f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:56:01 [DOC Engine]:
Start to index...
2026-08-10 11:56:01,668 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.022s]
2026-08-10 11:56:01,674 INFO     29 set_progress(4e7a239e94b111f1bd9827cf206dfa2d), progress: 0.81, progress_msg: 
2026-08-10 11:56:01,703 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.021s]
2026-08-10 11:56:01,731 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.019s]
2026-08-10 11:56:01,739 INFO     29 set_progress(4e7a239e94b111f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:56:01 Indexing done (0.10s). Task done (473.14s)
2026-08-10 11:56:01,746 INFO     29 [Done], chunks(10), token(6003), elapsed:473.14
2026-08-10 11:56:01,894 INFO     29 handle_task done for task {"id": "4e7a239e94b111f1bd9827cf206dfa2d", "doc_id": "4e16a27e94b111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "type": "pdf", "location": "MARO-\u56db\u5ddd\u7701\u4eba\u6c11.pdf", "size": 6177548, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786362467197, "task_type": "dataflow", "root_trace_id": "286793e46f274816aac4e99f4f88969c", "root_traceparent": "00-286793e46f274816aac4e99f4f88969c-0e15a5dfff02acd4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
