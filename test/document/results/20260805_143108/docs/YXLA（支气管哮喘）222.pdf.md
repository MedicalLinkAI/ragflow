# 基准结果：YXLA（支气管哮喘）222.pdf

## 基本信息

- 文件：`YXLA（支气管哮喘）222.pdf`
- 大小：20976.6 KB
- PDF 总页数：19
- doc_id：`5986c9ec909011f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:21  完成时间：2026-08-05T14:31:21  耗时：0.9s
- progress_msg：`05:53:27 Indexing done (0.11s). Task done (639.15s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | d8ac5a18 | 1 | 1-1 | 人民医院 H43120200207, 院区: 燕城院区) 基本就诊信息 姓名:  |
| 2 | b99cdc31 | 1 | 2-2 | 基本就诊信息 姓名：杨 医生： 挂号单：26000068319 医保号：5200 |
| 3 | 89425ac4 | 2 | 3-4 | 报告时间: 2025-02-24 怀化市肿瘤医院 怀化市第二人民医院 鹤城院区  |
| 4 | 5487446b | 1 | 5-5 | 怀化市中心医院 HUAIHUA CENTRAL HOSPITAL 怀化市肿瘤医院 |
| 5 | 3932bac8 | 2 | 6-7 | HUAIHUA CENTRAL HOSPITAL 怀化市肿瘤医院 姓名： 性别： |
| 6 | bc15980b | 3 | 7-9 | 37岁 科室：呼吸与危重症医学科 床号：42 住院号： 出院记录 入院时间：20 |
| 7 | 5a0d477e | 1 | 9-9 | 第2次入院记录 姓名： 出生地：贵州省天柱县 性别：女 民族：苗族 年龄：37岁 |
| 8 | 73778cae | 2 | 10-11 | 出院记录 入院时间：2025-02-24 12:22 出院时间：2025-03- |
| 9 | cc03cf04 | 2 | 12-13 | 221028180 第2次入院记录 姓名： 性别：女 年龄：37岁 婚姻：已婚  |
| 10 | eece8415 | 1 | 14-14 | 姓名： 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：  |
| 11 | 5ac48b34 | 1 | 15-15 | 报告时间: 2026-02-09 Pred Bst % (B/Pd) A1 A2 |
| 12 | c60bcc42 | 1 | 16-16 | 呼出气一氧化氮检测报告单 姓名：杨 性别：女 出生日期：1987-12-01 年 |
| 13 | 229e2eea | 1 | 17-17 | 一口气法弥散功能报告 姓名： 年龄：38岁 性别：女 科别： 保险： 预计值模式 |
| 14 | b059b78b | 1 | 18-18 | Pred A1 A1/Pd P1 A2/Pd chg%l P2 A3/Pd ch |
| 15 | 94f3221e | 1 | 19-19 | 金城大药房 会员号: 积分: 112550 本次积分: 596.00 名称 规格 |

- chunks 总数：15
- 各 chunk 页数合计（含跨页重复）：21
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]`
- 覆盖页数：19 / 19；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 4 | 4 | 4 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 2 | 2 | 2 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 1 | 1 | 1 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 2 | 2 | 2 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 6 | 6 | 6 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"PrescriptionRecord": 2, "ExaminationReport": 6, "DischargeRecord": 2, "AdmissionRecord": 4, "MedicationRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 15, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 2, "Extractor:Discharge": 2, "Extractor:Admission": 4, "Extractor:ExaminationReport": 6}, "filtered_noise": 3}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 05:53:22,592 INFO     29 [ChunkMerger] Merged 15 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 05:41:48,606 INFO     29 handle_task begin for task {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 05:41:48,828 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 05:41:48,866 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 05:41:48,884 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 05:41:48,884 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 05:41:48,889 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 05:41:48,889 INFO     29 ============================================================
2026-08-05 05:41:48,889 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 05:41:48,889 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 05:41:48,889 INFO     29 ============================================================
2026-08-05 05:41:48,889 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 05:41:48,889 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 05:41:48,891 INFO     29 No torch found.
2026-08-05 05:41:50,780 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=19
2026-08-05 05:41:50,905 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=866058, prompt_len=644
2026-08-05 05:41:52,318 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-30"}
```
2026-08-05 05:41:52,319 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-09-30
2026-08-05 05:41:52,329 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=866058, prompt_len=401
2026-08-05 05:41:54,444 INFO     29 [qwen-vl-parser] text API response (len=346):
["人民医院", "H43120200207, 院区: 燕城院区)", "基本就诊信息", "姓名: 梳", "医生: 旅", "挂号单: 25000448502", "医保号: 5200002600000000600637839", "付款: 城乡居民基本医疗 费别: 普通", "门诊号: 2502240221", "社区号:", "门诊就诊:呼吸内科门诊,2025-09-30 14:50", "医嘱 | 报告", "已作废 | 全部", "处方 | 其他", "生效时间", "内容", "用法", "2025-09-30", "孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/", "睡前口服,每天一次,共30天", "14:51", "盒,共10盒,每次10mg", ""]
2026-08-05 05:41:54,445 INFO     29 [qwen-vl-parser] page=1 text: 22 lines (bbox 0-21)
2026-08-05 05:41:54,445 INFO     29 [qwen-vl-parser] page=1 text: 22 sections
2026-08-05 05:41:54,579 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=951375, prompt_len=644
2026-08-05 05:41:55,842 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-09"}
```
2026-08-05 05:41:55,843 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2026-02-09
2026-08-05 05:41:55,854 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=951375, prompt_len=401
2026-08-05 05:41:58,556 INFO     29 [qwen-vl-parser] text API response (len=474):
["基本就诊信息", "姓名：杨", "医生：", "挂号单：26000068319", "医保号：52000026000000006006378395", "付款：城乡居民基本医疗 费别：普通", "门诊号：2502240221", "社区号：", "门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04", "医嘱|报告|", "已作废|全部|处方|其他", "生效时间", "内容", "用法", "2026-02-09", "肺功能全套+支气管舒张试验,共1次", "", "2026-02-09", "(基)硫酸沙丁胺醇吸入气雾剂 (山东)", "吸入,一次,共1天", "11:08", "100ug*200揿/瓶,共1瓶,每次400ug", "", "2026-02-09", "呼出气一氧化氮测定,共1次", "", "2026-02-09", "沙美特罗替卡松粉吸入剂(法国GLAXO)", "吸入,每天二次,共1天", "12.33", "50ug/500ug*60吸/瓶,共1瓶,每次50ug", ""]
2026-08-05 05:41:58,557 INFO     29 [qwen-vl-parser] page=2 text: 28 lines (bbox 22-49)
2026-08-05 05:41:58,557 INFO     29 [qwen-vl-parser] page=2 text: 28 sections
2026-08-05 05:41:58,750 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1648211, prompt_len=644
2026-08-05 05:42:00,102 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2025-02-24"}
```
2026-08-05 05:42:00,103 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2025-02-24
2026-08-05 05:42:00,120 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1648211, prompt_len=756
2026-08-05 05:42:02,156 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:42:02.153+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:42:35,100 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:42:35.099+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:43:09,154 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:43:09.153+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:43:40,496 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:43:40.495+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:44:11,109 INFO     29 [qwen-vl-parser] table API response (len=16394):
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c
2026-08-05 05:44:11,111 INFO     29 [qwen-vl-parser] page=3 table: 2 LaTeX lines (bbox 50-51)
2026-08-05 05:44:11,111 INFO     29 [qwen-vl-parser] page=3 table: 2 sections
2026-08-05 05:44:11,206 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=713058, prompt_len=644
2026-08-05 05:44:12,488 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-02-25"}
```
2026-08-05 05:44:12,489 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-02-25
2026-08-05 05:44:12,503 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=713058, prompt_len=401
2026-08-05 05:44:14,538 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:44:14.537+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:44:15,080 INFO     29 [qwen-vl-parser] text API response (len=438):
["怀化市肿瘤医院", "怀化市第二人民医院", "鹤城院区", "湖南HR", "CT影像诊断报告单", "ID: 86562633", "检查号: CT00525514", "姓名:", "性别: 女", "年龄: 37岁", "住院号: 220999152", "床号: 46", "申请科室: 呼吸与危重症医学科", "申请医生: 易莹", "检查日期: 2025.02.25", "报告日期: 2025.02.25 09:45:16", "检查项目: CT成套:胸部(平扫(三维重建))", "检查所见:", "右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见", "条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主", "要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "意见:", "1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。", "2. 右肺中叶少许慢性炎症。"]
2026-08-05 05:44:15,081 INFO     29 [qwen-vl-parser] page=4 text: 24 lines (bbox 52-75)
2026-08-05 05:44:15,081 INFO     29 [qwen-vl-parser] page=4 text: 24 sections
2026-08-05 05:44:15,188 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=747519, prompt_len=644
2026-08-05 05:44:16,553 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-07-11"}
```
2026-08-05 05:44:16,554 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2025-07-11
2026-08-05 05:44:16,568 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=747519, prompt_len=401
2026-08-05 05:44:19,435 INFO     29 [qwen-vl-parser] text API response (len=503):
["怀化市中心医院", "HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "湖南HR", "CT影像诊断报告单", "ID: 93717786", "检查号: CT00568277", "姓名:", "性别: 女", "年龄: 37岁", "住院号: 221028180", "床号: 42", "申请科室: 呼吸与危重症医学科", "申请医生:", "检查日期: 2025.07.11", "报告日期: 2025.07.11 16:08:56", "检查项目: CT成套胸部平扫(三维重建)", "检查所见:", "与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。", "右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部", "分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "意见:", "1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。", "2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。"]
2026-08-05 05:44:19,435 INFO     29 [qwen-vl-parser] page=5 text: 24 lines (bbox 76-99)
2026-08-05 05:44:19,436 INFO     29 [qwen-vl-parser] page=5 text: 24 sections
2026-08-05 05:44:19,597 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1489979, prompt_len=644
2026-08-05 05:44:20,967 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:44:20,968 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 05:44:20,981 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1489979, prompt_len=401
2026-08-05 05:44:28,923 INFO     29 [qwen-vl-parser] text API response (len=1206):
["HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "221028180", "3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总", "神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓", "浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经", "(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞", "<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌", "(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支", "持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司", "特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前", "好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。", "出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发", "热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，", "BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。", "心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧", "段结节（LU-RADS 2类）。", "出院医嘱：", "1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生", "活习惯，增强体质，适当运动，加强营养；", "2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复", "查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；", "3.出院后继续服用中药。", "4.出院带药：", "舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱", "口，根据动态复查肺功能结果，调整用药）", "祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次", "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次", "5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；", "6.如有不适，随时医院就诊，我科随诊。", "科室护士办公室电话：0745-2329117。主管医师电话：13789357317", "医师签名：主治医师", ""]
2026-08-05 05:44:28,924 INFO     29 [qwen-vl-parser] page=6 text: 35 lines (bbox 100-134)
2026-08-05 05:44:28,924 INFO     29 [qwen-vl-parser] page=6 text: 35 sections
2026-08-05 05:44:29,106 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1724875, prompt_len=644
2026-08-05 05:44:30,499 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:44:30,500 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 05:44:30,515 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1724875, prompt_len=401
2026-08-05 05:44:39,224 INFO     29 [qwen-vl-parser] text API response (len=1523):
["zz1028180", "37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "出院记录", "入院时间：2025-07-11 08:57", "出院时间：2025-07-22 15:00", "住院天数：11天", "记录时间：2025-07-21 16:14", "入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；", "4.腹胀查因：功能性消化不良？反流性食管炎？其他。", "入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T", "36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面", "容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及", "少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，", "无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，", "LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功", "能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散", "功能在正常范围；肺总量在正常范围，残气量、残总比增高。", "诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分", "压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中", "性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；", "尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红", "细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；", "电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C", "蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链", "DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生", "虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：", "胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.", "支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气", "功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、", "MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重", "减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳", "性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，", "绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），", "2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO："]
2026-08-05 05:44:39,225 INFO     29 [qwen-vl-parser] page=7 text: 34 lines (bbox 135-168)
2026-08-05 05:44:39,225 INFO     29 [qwen-vl-parser] page=7 text: 34 sections
2026-08-05 05:44:39,341 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=959069, prompt_len=644
2026-08-05 05:44:40,666 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:44:40,666 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-05 05:44:40,673 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=959069, prompt_len=401
2026-08-05 05:44:44,218 INFO     29 [qwen-vl-parser] text API response (len=621):
["怀化市中心医院", "HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "221028180", "〔心前区无隆起〕，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，〔", "〔各瓣膜听诊区未闻及杂音〕。腹部平坦，〔腹壁静脉无曲张〕，无胃肠型和蠕动波，〔全", "腹柔软〕，〔腹部无压痛〕，〔腹部无反跳痛〕，〔肝脾肋下未扪及〕，Murphy征(-)，叩", "诊呈〔鼓音〕，移动性浊音(-)。肠鸣音正常，〔无气过水声〕。外生殖器〔未查〕，肛门", "直肠〔正常〕。脊柱四肢〔正常〕。 双下肢无浮肿 ，生理反射正常，病理反射阴性。", "辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复", "查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占", "预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量", "在正常范围，残气量、残总比增高。", "入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？", "3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其", "他。", "主治医师：", "副主任医师："]
2026-08-05 05:44:44,218 INFO     29 [qwen-vl-parser] page=8 text: 20 lines (bbox 169-188)
2026-08-05 05:44:44,218 INFO     29 [qwen-vl-parser] page=8 text: 20 sections
2026-08-05 05:44:44,381 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1557912, prompt_len=644
2026-08-05 05:44:45,706 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:44:45,706 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-05 05:44:45,719 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1557912, prompt_len=401
2026-08-05 05:44:45,943 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:44:45.942+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:44:52,146 INFO     29 [qwen-vl-parser] text API response (len=1149):
["221028180", "第2次入院记录", "姓名：", "出生地：贵州省天柱县", "性别：女", "民族：苗族", "年龄：37岁", "职业：农民", "婚姻：已婚", "住址：贵州省天柱县远口镇大祥村白蜡树脚组", "入院时间：2025-07-11 08:57", "记录时间：2025-07-11 14:36", "入院方式：步行", "主诉：反复胸闷、气促8年，加重1月。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "病史陈述者签名：", "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。", "眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，", "甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。", "叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。"]
2026-08-05 05:44:52,147 INFO     29 [qwen-vl-parser] page=9 text: 22 lines (bbox 189-210)
2026-08-05 05:44:52,147 INFO     29 [qwen-vl-parser] page=9 text: 22 sections
2026-08-05 05:44:52,436 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2682307, prompt_len=644
2026-08-05 05:44:53,734 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:44:53,734 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-05 05:44:53,749 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2682307, prompt_len=401
2026-08-05 05:45:04,463 INFO     29 [qwen-vl-parser] text API response (len=1311):
["出院记录", "入院时间：2025-02-24 12:22", "出院时间：2025-03-01 10:00", "住院天数：5天", "记录时间：2025-02-28 20:39", "入院诊断：胸闷、气促查因：支气管哮喘可能性大", "入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89", "次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。", "诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C", "+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、", "肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体", "测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。", "心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1", "0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范", "围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO", "2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球", "菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、", "两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，", "LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能", "结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、", "抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者", "及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。", "出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶", "心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，", "BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心", "率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：", "功能性消化不良？反流性食管炎？其他。", "出院医嘱：", "（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺", "激性烟雾及吸入二手烟；"]
2026-08-05 05:45:04,463 INFO     29 [qwen-vl-parser] page=10 text: 33 lines (bbox 211-243)
2026-08-05 05:45:04,463 INFO     29 [qwen-vl-parser] page=10 text: 33 sections
2026-08-05 05:45:04,579 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=845994, prompt_len=644
2026-08-05 05:45:05,945 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:45:05,946 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-05 05:45:05,955 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=845994, prompt_len=401
2026-08-05 05:45:08,732 INFO     29 [qwen-vl-parser] text API response (len=433):
["姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；", "(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；", "(4) 继续用药：", "舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服", "布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入", "(吸入后漱口，根据动态复查肺功能结果，调整用药)", "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服", "止咳祛痰：润肺膏 每次15g 每天2次，口服", "调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服", "(5) 如有不适，随时医院就诊，我科随诊。", "科室电话：0745-2329117 主管医师电话：13789357317", "医师签名：主治医师："]
2026-08-05 05:45:08,733 INFO     29 [qwen-vl-parser] page=11 text: 15 lines (bbox 244-258)
2026-08-05 05:45:08,733 INFO     29 [qwen-vl-parser] page=11 text: 15 sections
2026-08-05 05:45:08,910 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1540592, prompt_len=644
2026-08-05 05:45:10,274 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:45:10,274 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-05 05:45:10,286 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1540592, prompt_len=401
2026-08-05 05:45:16,781 INFO     29 [qwen-vl-parser] text API response (len=1149):
["221028180", "第2次入院记录", "姓名：", "性别：女", "年龄：37岁", "婚姻：已婚", "入院时间：2025-07-11 08:57", "入院方式：步行", "主诉：反复胸闷、气促8年，加重1月。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "病史陈述者签名：", "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。", "出生地：贵州省天柱县", "民族：苗族", "职业：农民", "住址：贵", "记录时间：2025-07-11 14:36", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:45:16,782 INFO     29 [qwen-vl-parser] page=12 text: 21 lines (bbox 259-279)
2026-08-05 05:45:16,782 INFO     29 [qwen-vl-parser] page=12 text: 21 sections
2026-08-05 05:45:16,924 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1153832, prompt_len=644
2026-08-05 05:45:18,268 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:45:18,269 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-05 05:45:18,290 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1153832, prompt_len=401
2026-08-05 05:45:18,770 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:45:18.770+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:45:22,171 INFO     29 [qwen-vl-parser] text API response (len=647):
["家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。", "病史陈述者签名：", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋", "姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:", "辅助检查结果：无", "入院初步诊断：胸闷、气促查因：支气管哮喘可能性大", "主治医师：", "主任医师："]
2026-08-05 05:45:22,172 INFO     29 [qwen-vl-parser] page=13 text: 10 lines (bbox 280-289)
2026-08-05 05:45:22,172 INFO     29 [qwen-vl-parser] page=13 text: 10 sections
2026-08-05 05:45:22,342 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1578095, prompt_len=644
2026-08-05 05:45:23,683 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:45:23,684 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-05 05:45:23,701 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1578095, prompt_len=401
2026-08-05 05:45:32,294 INFO     29 [qwen-vl-parser] text API response (len=1128):
["姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "入院记录", "姓名：", "出生地：贵州省天柱县远口镇大样村白蜡树脚组", "性别：女", "民族：苗族", "年龄：37岁", "职业：自由职业者", "婚姻：已婚", "住址：贵", "入院时间：2025-02-24 12:22", "记录时间：2025-02-24 14:28", "入院方式：步行", "主诉：反复胸闷、气促8年，加重半年。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳", "嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐", "渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，", "无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，", "约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，", "门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期", "体重无改变。", "既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病", "史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。", "个人史：[出生于原籍 ， 常住本地 ， 无粉尘放射性物质接触史 ， 否认疫区居住", "史]，[无吸烟史 ， 无饮酒史 ， 否认性病及治游史 。", "月经史：16 2~3 2025/2/21， 月经周期规律，色红，量少，无痛经。", "29~30", "婚育史：24岁结婚，育有1子1女，配偶及子女体健。", "家族史：家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。", "病史陈述者签名：", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜", "色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，", "巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常", "分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-", "颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤", "正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦", ""]
2026-08-05 05:45:32,295 INFO     29 [qwen-vl-parser] page=14 text: 39 lines (bbox 290-328)
2026-08-05 05:45:32,295 INFO     29 [qwen-vl-parser] page=14 text: 39 sections
2026-08-05 05:45:32,410 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=869774, prompt_len=644
2026-08-05 05:45:35,220 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-02-09"
}
```
2026-08-05 05:45:35,220 INFO     29 [qwen-vl-parser] page=15 classify=table report_date=2026-02-09
2026-08-05 05:45:35,230 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=869774, prompt_len=756
2026-08-05 05:45:41,941 INFO     29 [qwen-vl-parser] table API response (len=1313):
\begin{tabular}{lcccccc}
\hline
& Pred & Bst & \% (B/Pd) & A1 & A2 & A3 \\
\hline
FVC & [L] & 2.99 & 2.21 & 74.02 & 2.21 & 2.12 & 2.09 \\
FEV 1 & [L] & 2.67 & 1.26 & 48.56 & 1.26 & 1.13 & 1.18 \\
FEV6 & [L] & & 2.12 & & 2.12 & 2.05 & 2.02 \\
FEV 1 \% FVC & [\%] & 84.19 & 56.48 & 67.09 & 56.48 & 53.33 & 56.67 \\
FEV 1 \% VC MAX & [\%] & 81.88 & 55.26 & 67.48 & 55.26 & 50.10 & 52.31 \\
VC MAX & [L] & 3.03 & 2.26 & 74.60 & & & \\
PEF & [L/s] & 6.28 & 2.66 & 42.36 & 2.66 & 2.58 & 2.43 \\
MMEF 75/25 & [L/s] & 3.57 & 0.51 & 14.35 & 0.51 & 0.49 & 0.41 \\
MEF 75 & [L/s] & 5.64 & 1.47 & 26.14 & 1.47 & 0.80 & 1.21 \\
MEF 50 & [L/s] & 4.01 & 0.68 & 16.97 & 0.68 & 0.72 & 0.57 \\
MEF 25 & [L/s] & 1.79 & 0.19 & 10.52 & 0.19 & 0.18 & 0.15 \\
V backextrapolation ex & [L] & & & & 0.05 & 0.03 & 0.04 \\
V backextrapol. \% FVC & [\%] & & & & 2.07 & 1.50 & 1.81 \\
FET & [s] & & & & 7.63 & 7.35 & 7.55 \\
FEF 200-1200 & [L/s] & & & & 1.19 & 0.98 & 1.05 \\
FVC IN & [L] & 3.03 & 2.26 & 74.60 & 2.26 & 2.15 & 2.13 \\
FIV1 & [L] & & & & 2.21 & 2.12 & 2.09 \\
FIV1 \% FVC & [\%] & & & & 97.79 & 98.68 & 98.05 \\
FEF50 \% FIF50 & [\%] & & & & 22.86 & 25.05 & 19.46 \\
PIF & [L/s] & & & & 3.04 & 3.04 & 2.99 \\
MVV & [L/min] & 99.77 & 46.21 & 46.32 & 46.21 & & \\
BF MVV & [1/min] & & & & 75.55 & 75.55 & \\
\hline
\end{tabular}
2026-08-05 05:45:41,942 INFO     29 [qwen-vl-parser] page=15 table: 29 LaTeX lines (bbox 329-357)
2026-08-05 05:45:41,942 INFO     29 [qwen-vl-parser] page=15 table: 29 sections
2026-08-05 05:45:42,071 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1055456, prompt_len=644
2026-08-05 05:45:43,526 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-09"
}
```
2026-08-05 05:45:43,526 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=2026-02-09
2026-08-05 05:45:43,532 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1055456, prompt_len=401
2026-08-05 05:45:49,577 INFO     29 [qwen-vl-parser] text API response (len=1117):
["呼出气一氧化氮检测报告单", "姓名：杨", "性别：女", "出生日期：1987-12-01", "年龄：38岁2个月", "ID号：", "测试日期：2026-02-09", "科室：呼吸科门诊", "医生：张", "问卷调查：", "激素：正在使用口 三天内未使用口 从未使用口", "抗生素：正在使用口 三天内未使用口 从未使用口", "吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口", "症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：", "病史：过敏史口 其他：", "注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。", "检测信息：", "项目：在线", "呼气压力：8.8cmH2O 呼气流速：45ml/s", "呼气时间：5s 温度：21.8℃ 湿度：38.9%", "呼气浓度：10、11、12、11、11、11、10、10、10、", "10、10、10、11、10、11、11、11、11ppb", "项目：小气道", "呼气压力：11.3cmH2O 呼气流速：202ml/s", "呼气时间：3s 温度：22.0℃ 湿度：39.0%", "呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0", "0.0、0.0、0.0、0.0、1.0、1.0、1.0、", "1.0、1.0、0.0、0.0、0.0ppb", "参考意义：", "(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)", "测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型", "FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症", "25 - 50ppb 20 - 35ppb* 混合型气道炎症", "> 50ppb > 35ppb* 嗜酸性气道炎症", "CaNO ≤ 5ppb ≤ 3ppb 小气道正常", "> 5ppb > 3ppb 小气道炎症", "FaNO < 125ppb 考虑Kartagener综合征、PCD、CF或", "重度的鼻窦炎或鼻息肉", "125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉", "250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断", "> 500ppb 考虑过敏性鼻炎", "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "此结果仅对本次呼气检测负责", "测定结果：FeNO 60:11ppb CaNO :1.0ppb", "操作员：蒋细萍", "张日石", ""]
2026-08-05 05:45:49,578 INFO     29 [qwen-vl-parser] page=16 text: 46 lines (bbox 358-403)
2026-08-05 05:45:49,578 INFO     29 [qwen-vl-parser] page=16 text: 46 sections
2026-08-05 05:45:49,678 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=680206, prompt_len=644
2026-08-05 05:45:50,952 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-00"
}
```
2026-08-05 05:45:50,953 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=2026-02-00
2026-08-05 05:45:50,975 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=680206, prompt_len=401
2026-08-05 05:45:51,170 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:45:51.169+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:45:55,583 INFO     29 [qwen-vl-parser] text API response (len=1037):
["一口气法弥散功能报告", "姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-now", "测试号：2026020917", "身高：155 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "CO (%)", "Volume [L]", "CH4 [%]", "-0.25", "2-0.20", "0-0.15", "2-0.10", "0.05", "4", "Time [s]", "0", "5", "10", "15", "20", "25", "30", "Pred", "Best", "Best%", "Act1", "DLCO SB", "[mmol/min/kPa]", "8.08", "9.45", "116.9", "9.45", "DLCO/VA", "[mmol/min/kPa/L]", "1.82", "2.38", "130.8", "2.38", "VA", "[L]", "4.29", "3.97", "92.5", "3.97", "VC IN", "[L]", "3.03", "2.26", "74.6", "Discard vol", "[L]", "1.00", "Sample vol", "[L]", "0.53", "ERV", "[L]", "1.10", "IRV", "[L]", "IC", "[L]", "1.93", "VT", "[L]", "0.43", "VC MAX", "[L]", "3.03", "2.26", "74.6", "TLC-SB", "[L]", "4.44", "4.10", "92.4", "4.10", "RV-SB", "[L]", "1.41", "2.18", "154.5", "2.18", "RV%TLC-SB", "[%]", "31.88", "53.26", "167.1", "53.26", "FRC-SB", "[L]", "2.51", "2.39", "95.2", "2.39", "FRC%TLC-SB", "[%]", "51.18", "58.28", "113.9", "58.28", "测试日期", "26/2/0", "意见：", "1.弥散功能在正常范围。", "2.残气量、残总比增高，肺总量在正常范围。", "张"]
2026-08-05 05:45:55,584 INFO     29 [qwen-vl-parser] page=17 text: 115 lines (bbox 404-518)
2026-08-05 05:45:55,584 INFO     29 [qwen-vl-parser] page=17 text: 115 sections
2026-08-05 05:45:55,704 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=929802, prompt_len=644
2026-08-05 05:45:57,070 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-05 05:45:57,070 INFO     29 [qwen-vl-parser] page=18 classify=table report_date=None
2026-08-05 05:45:57,077 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=929802, prompt_len=756
2026-08-05 05:46:07,158 INFO     29 [qwen-vl-parser] table API response (len=1354):
\begin{tabular}{lcccccccccc}
\hline
& Pred & A1 A1/Pd & P1 A2/Pd & chg\%l & P2 A3/Pd & chg\%2 & P3 A4/Pd & chg\%3 & & \\
\hline
FVC & [L.] & 2.99 & 2.21 & 74.0 & 2.63 & 87.9 & 18.72 & 2.04 & 88.2 & 19.17 \\
FEV 1 & [L.] & 2.67 & 1.25 & 48.6 & 1.62 & 69.2 & 21.85 & 1.84 & 69.8 & 23.23 \\
FEV 1 \% FVC & [\%] & 84.19 & 56.48 & 67.1 & 67.97 & 68.9 & 2.64 & 58.40 & 69.4 & 3.41 \\
FEV 1 \% VC MAX & [\%] & 81.88 & 55.26 & 67.6 & 67.97 & 70.8 & 4.91 & 68.40 & 71.3 & 5.73 \\
VC MAX & [L.] & 3.03 & 2.26 & 74.6 & 2.63 & 86.6 & 16.14 & 2.64 & 87.0 & 16.59 \\
PEF & [L/s] & 6.28 & 2.66 & 42.4 & 2.90 & 46.2 & 9.17 & 3.37 & 53.7 & 26.79 \\
MMEF 75/25 & [L/s] & 3.57 & 0.61 & 14.4 & 0.67 & 18.8 & 31.03 & 0.73 & 20.4 & 42.01 \\
MEF 50 & [L/s] & 4.01 & 0.68 & 17.0 & 0.90 & 22.5 & 32.75 & 0.89 & 22.1 & 30.15 \\
MEF 25 & [L/s] & 1.79 & 0.19 & 10.5 & 0.27 & 15.2 & 44.16 & 0.33 & 18.7 & 77.66 \\
FET & [s] & 7.63 & & & 8.01 & & 4.99 & 7.79 & 2.14 & 7.43 \\
V backextrapolation ex [L] & & 0.05 & & 0.04 & & -11.67 & 0.04 & & -18.64 & 0.04 \\
PIF & [L/s] & 3.04 & & 3.37 & & 10.91 & 3.51 & & 15.70 & 3.60 \\
FIV1 & [L] & 2.21 & & 2.56 & & 15.71 & 2.56 & & 15.66 & 2.50 \\
PEF50 \% FIF50 & [\%] & 22.86 & & 28.15 & & 23.14 & 25.36 & & 10.95 & 27.28 \\
MVV & [L/min] & 99.77 & 46.21 & 46.3 & & & & & & \\
BF MVV & [1/min] & & 75.55 & & & & & & & \\
\hline
\end{tabular}
2026-08-05 05:46:07,159 INFO     29 [qwen-vl-parser] page=18 table: 22 LaTeX lines (bbox 519-540)
2026-08-05 05:46:07,159 INFO     29 [qwen-vl-parser] page=18 table: 22 sections
2026-08-05 05:46:07,316 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1413782, prompt_len=644
2026-08-05 05:46:08,810 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:46:08,810 INFO     29 [qwen-vl-parser] page=19 classify=text report_date=None
2026-08-05 05:46:08,818 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1413782, prompt_len=401
2026-08-05 05:46:10,977 INFO     29 [qwen-vl-parser] text API response (len=331):
["金城大药房", "会员号:", "积分: 112550", "本次积分: 596.00", "名称", "规格", "数量", "厂家", "批号", "单价", "金额", "1-布地奈德福莫特罗吸入粉雾剂", "320ug:9ug*60 吸/支", "2.00", "阿斯利康制药", "PKMR", "300.00", "596.00", "运动员慎用!!!", "****重打销售单****", "总计数量: 2.00", "应收: 600.00", "优惠: 4.00", "付款: 596.00", "找零: 0.00", "销售单号: 251210031062", "款台号: 2", "日期: 2025-12-10", "15:21:53"]
2026-08-05 05:46:10,977 INFO     29 [qwen-vl-parser] page=19 text: 29 lines (bbox 541-569)
2026-08-05 05:46:10,978 INFO     29 [qwen-vl-parser] page=19 text: 29 sections
2026-08-05 05:46:10,978 INFO     29 [qwen-vl-parser] parse_pdf done: 570 sections from 19 pages.
2026-08-05 05:46:10,990 INFO     29 Close text detector.
2026-08-05 05:46:11,373 INFO     29 Close text recognizer.
2026-08-05 05:46:11,731 INFO     29 Close recognizer.
2026-08-05 05:46:12,066 INFO     29 Close recognizer.
2026-08-05 05:46:12,430 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 05:46:12,430 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Parser:MedLink | outputs={"html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "json"}
2026-08-05 05:46:12,431 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 05:46:12,447 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:46:12,448 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 人民医院\n[BBOX-1] H43120200207, 院区: 燕城院区)\n[BBOX-2] 基本就诊信息\n[BBOX-3] 姓名: 梳\n[BBOX-4] 医生: 旅\n[BBOX-5] 挂号单: 25000448502\n[BBOX-6] 医保号: 5200002600000000600637839\n[BBOX-7] 付款: 城乡居民基本医疗 费别: 普通\n[BBOX-8] 门诊号: 2502240221\n[BBOX-9] 社区号:\n[BBOX-10] 门诊就诊:呼吸内科门诊,2025-09-30 14:50\n[BBOX-11] 医嘱 | 报告\n[BBOX-12] 已作废 | 全部\n[BBOX-13] 处方 | 其他\n[BBOX-14] 生效时间\n[BBOX-15] 内容\n[BBOX-16] 用法\n[BBOX-17] 2025-09-30\n[BBOX-18] 孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/\n[BBOX-19] 睡前口服,每天一次,共30天\n[BBOX-20] 14:51\n[BBOX-21] 盒,共10盒,每次10mg\n[BBOX-22] 基本就诊信息\n[BBOX-23] 姓名：杨\n[BBOX-24] 医生：\n[BBOX-25] 挂号单：26000068319\n[BBOX-26] 医保号：52000026000000006006378395\n[BBOX-27] 付款：城乡居民基本医疗 费别：普通\n[BBOX-28] 门诊号：2502240221\n[BBOX-29] 社区号：\n[BBOX-30] 门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04\n[BBOX-31] 医嘱|报告|\n[BBOX-32] 已作废|全部|处方|其他\n[BBOX-33] 生效时间\n[BBOX-34] 内容\n[BBOX-35] 用法\n[BBOX-36] 2026-02-09\n[BBOX-37] 肺功能全套+支气管舒张试验,共1次\n[BBOX-38] 2026-02-09\n[BBOX-39] (基)硫酸沙丁胺醇吸入气雾剂 (山东)\n[BBOX-40] 吸入,一次,共1天\n[BBOX-41] 11:08\n[BBOX-42] 100ug*200揿/瓶,共1瓶,每次400ug\n[BBOX-43] 2026-02-09\n[BBOX-44] 呼出气一氧化氮测定,共1次\n[BBOX-45] 2026-02-09\n[BBOX-46] 沙美特罗替卡松粉吸入剂(法国GLAXO)\n[BBOX-47] 吸入,每天二次,共1天\n[BBOX-48] 12.33\n[BBOX-49] 50ug/500ug*60吸/瓶,共1瓶,每次50ug\n[BBOX-50] \\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c\n[BBOX-51] 报告时间: 2025-02-24\n[BBOX-52] 怀化市肿瘤医院\n[BBOX-53] 怀化市第二人民医院\n[BBOX-54] 鹤城院区\n[BBOX-55] 湖南HR\n[BBOX-56] CT影像诊断报告单\n[BBOX-57] ID: 86562633\n[BBOX-58] 检查号: CT00525514\n[BBOX-59] 姓名:\n[BBOX-60] 性别: 女\n[BBOX-61] 年龄: 37岁\n[BBOX-62] 住院号: 220999152\n[BBOX-63] 床号: 46\n[BBOX-64] 申请科室: 呼吸与危重症医学科\n[BBOX-65] 申请医生: 易莹\n[BBOX-66] 检查日期: 2025.02.25\n[BBOX-67] 报告日期: 2025.02.25 09:45:16\n[BBOX-68] 检查项目: CT成套:胸部(平扫(三维重建))\n[BBOX-69] 检查所见:\n[BBOX-70] 右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见\n[BBOX-71] 条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主\n[BBOX-72] 要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。\n[BBOX-73] 意见:\n[BBOX-74] 1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。\n[BBOX-75] 2. 右肺中叶少许慢性炎症。\n[BBOX-76] 怀化市中心医院\n[BBOX-77] HUAIHUA CENTRAL HOSPITAL\n[BBOX-78] 怀化市肿瘤医院\n[BBOX-79] 湖南HR\n[BBOX-80] CT影像诊断报告单\n[BBOX-81] ID: 93717786\n[BBOX-82] 检查号: CT00568277\n[BBOX-83] 姓名:\n[BBOX-84] 性别: 女\n[BBOX-85] 年龄: 37岁\n[BBOX-86] 住院号: 221028180\n[BBOX-87] 床号: 42\n[BBOX-88] 申请科室: 呼吸与危重症医学科\n[BBOX-89] 申请医生:\n[BBOX-90] 检查日期: 2025.07.11\n[BBOX-91] 报告日期: 2025.07.11 16:08:56\n[BBOX-92] 检查项目: CT成套胸部平扫(三维重建)\n[BBOX-93] 检查所见:\n[BBOX-94] 与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。\n[BBOX-95] 右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部\n[BBOX-96] 分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。\n[BBOX-97] 意见:\n[BBOX-98] 1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。\n[BBOX-99] 2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。\n[BBOX-100] HUAIHUA CENTRAL HOSPITAL\n[BBOX-101] 怀化市肿瘤医院\n[BBOX-102] 姓名：\n[BBOX-103] 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n[BBOX-104] 221028180\n[BBOX-105] 3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总\n[BBOX-106] 神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓\n[BBOX-107] 浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经\n[BBOX-108] (感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞\n[BBOX-109] <10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌\n[BBOX-110] (TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支\n[BBOX-111] 持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司\n[BBOX-112] 特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前\n[BBOX-113] 好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。\n[BBOX-114] 出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发\n[BBOX-115] 热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，\n[BBOX-116] BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。\n[BBOX-117] 心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。\n[BBOX-118] 出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧\n[BBOX-119] 段结节（LU-RADS 2类）。\n[BBOX-120] 出院医嘱：\n[BBOX-121] 1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生\n[BBOX-122] 活习惯，增强体质，适当运动，加强营养；\n[BBOX-123] 2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复\n[BBOX-124] 查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；\n[BBOX-125] 3.出院后继续服用中药。\n[BBOX-126] 4.出院带药：\n[BBOX-127] 舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱\n[BBOX-128] 口，根据动态复查肺功能结果，调整用药）\n[BBOX-129] 祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次\n[BBOX-130] 抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次\n[BBOX-131] 5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；\n[BBOX-132] 6.如有不适，随时医院就诊，我科随诊。\n[BBOX-133] 科室护士办公室电话：0745-2329117。主管医师电话：13789357317\n[BBOX-134] 医师签名：主治医师\n[BBOX-135] zz1028180\n[BBOX-136] 37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n[BBOX-137] 出院记录\n[BBOX-138] 入院时间：2025-07-11 08:57\n[BBOX-139] 出院时间：2025-07-22 15:00\n[BBOX-140] 住院天数：11天\n[BBOX-141] 记录时间：2025-07-21 16:14\n[BBOX-142] 入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；\n[BBOX-143] 4.腹胀查因：功能性消化不良？反流性食管炎？其他。\n[BBOX-144] 入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T\n[BBOX-145] 36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面\n[BBOX-146] 容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及\n[BBOX-147] 少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，\n[BBOX-148] 无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，\n[BBOX-149] LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功\n[BBOX-150] 能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散\n[BBOX-151] 功能在正常范围；肺总量在正常范围，残气量、残总比增高。\n[BBOX-152] 诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分\n[BBOX-153] 压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中\n[BBOX-154] 性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；\n[BBOX-155] 尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红\n[BBOX-156] 细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；\n[BBOX-157] 电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C\n[BBOX-158] 蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链\n[BBOX-159] DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生\n[BBOX-160] 虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：\n[BBOX-161] 胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.\n[BBOX-162] 支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气\n[BBOX-163] 功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、\n[BBOX-164] MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重\n[BBOX-165] 减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳\n[BBOX-166] 性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，\n[BBOX-167] 绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），\n[BBOX-168] 2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：\n[BBOX-169] 怀化市中心医院\n[BBOX-170] HUAIHUA CENTRAL HOSPITAL\n[BBOX-171] 怀化市肿瘤医院\n[BBOX-172] 姓名：\n[BBOX-173] 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n[BBOX-174] 221028180\n[BBOX-175] 〔心前区无隆起〕，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，〔\n[BBOX-176] 〔各瓣膜听诊区未闻及杂音〕。腹部平坦，〔腹壁静脉无曲张〕，无胃肠型和蠕动波，〔全\n[BBOX-177] 腹柔软〕，〔腹部无压痛〕，〔腹部无反跳痛〕，〔肝脾肋下未扪及〕，Murphy征(-)，叩\n[BBOX-178] 诊呈〔鼓音〕，移动性浊音(-)。肠鸣音正常，〔无气过水声〕。外生殖器〔未查〕，肛门\n[BBOX-179] 直肠〔正常〕。脊柱四肢〔正常〕。 双下肢无浮肿 ，生理反射正常，病理反射阴性。\n[BBOX-180] 辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复\n[BBOX-181] 查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占\n[BBOX-182] 预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量\n[BBOX-183] 在正常范围，残气量、残总比增高。\n[BBOX-184] 入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？\n[BBOX-185] 3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其\n[BBOX-186] 他。\n[BBOX-187] 主治医师：\n[BBOX-188] 副主任医师：\n[BBOX-189] 221028180\n[BBOX-190] 第2次入院记录\n[BBOX-191] 姓名：\n[BBOX-192] 出生地：贵州省天柱县\n[BBOX-193] 性别：女\n[BBOX-194] 民族：苗族\n[BBOX-195] 年龄：37岁\n[BBOX-196] 职业：农民\n[BBOX-197] 婚姻：已婚\n[BBOX-198] 住址：贵州省天柱县远口镇大祥村白蜡树脚组\n[BBOX-199] 入院时间：2025-07-11 08:57\n[BBOX-200] 记录时间：2025-07-11 14:36\n[BBOX-201] 入院方式：步行\n[BBOX-202] 主诉：反复胸闷、气促8年，加重1月。\n[BBOX-203] 现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。\n[BBOX-204] 出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。\n[BBOX-205] 既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。\n[BBOX-206] 病史陈述者签名：\n[BBOX-207] 体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。\n[BBOX-208] 眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，\n[BBOX-209] 甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。\n[BBOX-210] 叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。\n[BBOX-211] 出院记录\n[BBOX-212] 入院时间：2025-02-24 12:22\n[BBOX-213] 出院时间：2025-03-01 10:00\n[BBOX-214] 住院天数：5天\n[BBOX-215] 记录时间：2025-02-28 20:39\n[BBOX-216] 入院诊断：胸闷、气促查因：支气管哮喘可能性大\n[BBOX-217] 入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。\n[BBOX-218] 体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸\n[BBOX-219] 氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89\n[BBOX-220] 次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。\n[BBOX-221] 诊疗经过：入院后完善检���：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C\n[BBOX-222] +3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、\n[BBOX-223] 肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体\n[BBOX-224] 测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。\n[BBOX-225] 心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1\n[BBOX-226] 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范\n[BBOX-227] 围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO\n[BBOX-228] 2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球\n[BBOX-229] 菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、\n[BBOX-230] 两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，\n[BBOX-231] LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能\n[BBOX-232] 结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、\n[BBOX-233] 抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者\n[BBOX-234] 及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。\n[BBOX-235] 出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶\n[BBOX-236] 心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，\n[BBOX-237] BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心\n[BBOX-238] 率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。\n[BBOX-239] 出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：\n[BBOX-240] 功能性消化不良？反流性食管炎？其他。\n[BBOX-241] 出院医嘱：\n[BBOX-242] （1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺\n[BBOX-243] 激性烟雾及吸入二手烟；\n[BBOX-244] 姓名：\n[BBOX-245] 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n[BBOX-246] 220999152\n[BBOX-247] (2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；\n[BBOX-248] (3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；\n[BBOX-249] (4) 继续用药：\n[BBOX-250] 舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服\n[BBOX-251] 布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入\n[BBOX-252] (吸入后漱口，根据动态复查肺功能结果，调整用药)\n[BBOX-253] 抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服\n[BBOX-254] 止咳祛痰：润肺膏 每次15g 每天2次，口服\n[BBOX-255] 调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服\n[BBOX-256] (5) 如有不适，随时医院就诊，我科随诊。\n[BBOX-257] 科室电话：0745-2329117 主管医师电话：13789357317\n[BBOX-258] 医师签名：主治医师：\n[BBOX-259] 221028180\n[BBOX-260] 第2次入院记录\n[BBOX-261] 姓名：\n[BBOX-262] 性别：女\n[BBOX-263] 年龄：37岁\n[BBOX-264] 婚姻：已婚\n[BBOX-265] 入院时间：2025-07-11 08:57\n[BBOX-266] 入院方式：步行\n[BBOX-267] 主诉：反复胸闷、气促8年，加重1月。\n[BBOX-268] 现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。\n[BBOX-269] 出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。\n[BBOX-270] 既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。\n[BBOX-271] 病史陈述者签名：\n[BBOX-272] 体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。\n[BBOX-273] 出生地：贵州省天柱县\n[BBOX-274] 民族：苗族\n[BBOX-275] 职业：农民\n[BBOX-276] 住址：贵\n[BBOX-277] 记录时间：2025-07-11 14:36\n[BBOX-278] CS 扫描全能王\n[BBOX-279] 3亿人都在用的扫描App\n[BBOX-280] 家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。\n[BBOX-281] 病史陈述者签名：\n[BBOX-282] 体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋\n[BBOX-283] 姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n[BBOX-284] 220999152\n[BBOX-285] 下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:\n[BBOX-286] 辅助检查结果：无\n[BBOX-287] 入院初步诊断：胸闷、气促查因：支气管哮喘可能性大\n[BBOX-288] 主治医师：\n[BBOX-289] 主任医师：\n[BBOX-290] 姓名：\n[BBOX-291] 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n[BBOX-292] 220999152\n[BBOX-293] 入院记录\n[BBOX-294] 姓名：\n[BBOX-295] 出生地：贵州省天柱县远口镇大样村白蜡树脚组\n[BBOX-296] 性别：女\n[BBOX-297] 民族：苗族\n[BBOX-298] 年龄：37岁\n[BBOX-299] 职业：自由职业者\n[BBOX-300] 婚姻：已婚\n[BBOX-301] 住址：贵\n[BBOX-302] 入院时间：2025-02-24 12:22\n[BBOX-303] 记录时间：2025-02-24 14:28\n[BBOX-304] 入院方式：步行\n[BBOX-305] 主诉：反复胸闷、气促8年，加重半年。\n[BBOX-306] 现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳\n[BBOX-307] 嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐\n[BBOX-308] 渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，\n[BBOX-309] 无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，\n[BBOX-310] 约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，\n[BBOX-311] 门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期\n[BBOX-312] 体重无改变。\n[BBOX-313] 既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病\n[BBOX-314] 史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。\n[BBOX-315] 个人史：[出生于原籍 ， 常住本地 ， 无粉尘放射性物质接触史 ， 否认疫区居住\n[BBOX-316] 史]，[无吸烟史 ， 无饮酒史 ， 否认性病及治游史 。\n[BBOX-317] 月经史：16 2~3 2025/2/21， 月经周期规律，色红，量少，无痛经。\n[BBOX-318] 29~30\n[BBOX-319] 婚育史：24岁结婚，育有1子1女，配偶及子女体健。\n[BBOX-320] 家族史：家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。\n[BBOX-321] 病史陈述者签名：\n[BBOX-322] 体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸\n[BBOX-323] 氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜\n[BBOX-324] 色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，\n[BBOX-325] 巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常\n[BBOX-326] 分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-\n[BBOX-327] 颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤\n[BBOX-328] 正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦\n[BBOX-329] \\begin{tabular}{lcccccc}\n[BBOX-330] 报告时间: 2026-02-09\n[BBOX-331] \\hline\n[BBOX-332] & Pred & Bst & \\% (B/Pd) & A1 & A2 & A3 \\\\\n[BBOX-333] \\hline\n[BBOX-334] FVC & [L] & 2.99 & 2.21 & 74.02 & 2.21 & 2.12 & 2.09 \\\\\n[BBOX-335] FEV 1 & [L] & 2.67 & 1.26 & 48.56 & 1.26 & 1.13 & 1.18 \\\\\n[BBOX-336] FEV6 & [L] & & 2.12 & & 2.12 & 2.05 & 2.02 \\\\\n[BBOX-337] FEV 1 \\% FVC & [\\%] & 84.19 & 56.48 & 67.09 & 56.48 & 53.33 & 56.67 \\\\\n[BBOX-338] FEV 1 \\% VC MAX & [\\%] & 81.88 & 55.26 & 67.48 & 55.26 & 50.10 & 52.31 \\\\\n[BBOX-339] VC MAX & [L] & 3.03 & 2.26 & 74.60 & & & \\\\\n[BBOX-340] PEF & [L/s] & 6.28 & 2.66 & 42.36 & 2.66 & 2.58 & 2.43 \\\\\n[BBOX-341] MMEF 75/25 & [L/s] & 3.57 & 0.51 & 14.35 & 0.51 & 0.49 & 0.41 \\\\\n[BBOX-342] MEF 75 & [L/s] & 5.64 & 1.47 & 26.14 & 1.47 & 0.80 & 1.21 \\\\\n[BBOX-343] MEF 50 & [L/s] & 4.01 & 0.68 & 16.97 & 0.68 & 0.72 & 0.57 \\\\\n[BBOX-344] MEF 25 & [L/s] & 1.79 & 0.19 & 10.52 & 0.19 & 0.18 & 0.15 \\\\\n[BBOX-345] V backextrapolation ex & [L] & & & & 0.05 & 0.03 & 0.04 \\\\\n[BBOX-346] V backextrapol. \\% FVC & [\\%] & & & & 2.07 & 1.50 & 1.81 \\\\\n[BBOX-347] FET & [s] & & & & 7.63 & 7.35 & 7.55 \\\\\n[BBOX-348] FEF 200-1200 & [L/s] & & & & 1.19 & 0.98 & 1.05 \\\\\n[BBOX-349] FVC IN & [L] & 3.03 & 2.26 & 74.60 & 2.26 & 2.15 & 2.13 \\\\\n[BBOX-350] FIV1 & [L] & & & & 2.21 & 2.12 & 2.09 \\\\\n[BBOX-351] FIV1 \\% FVC & [\\%] & & & & 97.79 & 98.68 & 98.05 \\\\\n[BBOX-352] FEF50 \\% FIF50 & [\\%] & & & & 22.86 & 25.05 & 19.46 \\\\\n[BBOX-353] PIF & [L/s] & & & & 3.04 & 3.04 & 2.99 \\\\\n[BBOX-354] MVV & [L/min] & 99.77 & 46.21 & 46.32 & 46.21 & & \\\\\n[BBOX-355] BF MVV & [1/min] & & & & 75.55 & 75.55 & \\\\\n[BBOX-356] \\hline\n[BBOX-357] \\end{tabular}\n[BBOX-358] 呼出气一氧化氮检测报告单\n[BBOX-359] 姓名：杨\n[BBOX-360] 性别：女\n[BBOX-361] 出生日期：1987-12-01\n[BBOX-362] 年龄：38岁2个月\n[BBOX-363] ID号：\n[BBOX-364] 测试日期：2026-02-09\n[BBOX-365] 科室：呼吸科门诊\n[BBOX-366] 医生：张\n[BBOX-367] 问卷调查：\n[BBOX-368] 激素：正在使用口 三天内未使用口 从未使用口\n[BBOX-369] 抗生素：正在使用口 三天内未使用口 从未使用口\n[BBOX-370] 吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口\n[BBOX-371] 症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：\n[BBOX-372] 病史：过敏史口 其他：\n[BBOX-373] 注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。\n[BBOX-374] 检测信息：\n[BBOX-375] 项目：在线\n[BBOX-376] 呼气压力：8.8cmH2O 呼气流速：45ml/s\n[BBOX-377] 呼气时间：5s 温度：21.8℃ 湿度：38.9%\n[BBOX-378] 呼气浓度：10、11、12、11、11、11、10、10、10、\n[BBOX-379] 10、10、10、11、10、11、11、11、11ppb\n[BBOX-380] 项目：小气道\n[BBOX-381] 呼气压力：11.3cmH2O 呼气流速：202ml/s\n[BBOX-382] 呼气时间：3s 温度：22.0℃ 湿度：39.0%\n[BBOX-383] 呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0\n[BBOX-384] 0.0、0.0、0.0、0.0、1.0、1.0、1.0、\n[BBOX-385] 1.0、1.0、0.0、0.0、0.0ppb\n[BBOX-386] 参考意义：\n[BBOX-387] (根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)\n[BBOX-388] 测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型\n[BBOX-389] FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症\n[BBOX-390] 25 - 50ppb 20 - 35ppb* 混合型气道炎症\n[BBOX-391] > 50ppb > 35ppb* 嗜酸性气道炎症\n[BBOX-392] CaNO ≤ 5ppb ≤ 3ppb 小气道正常\n[BBOX-393] > 5ppb > 3ppb 小气道炎症\n[BBOX-394] FaNO < 125ppb 考虑Kartagener综合征、PCD、CF或\n[BBOX-395] 重度的鼻窦炎或鼻息肉\n[BBOX-396] 125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉\n[BBOX-397] 250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断\n[BBOX-398] > 500ppb 考虑过敏性鼻炎\n[BBOX-399] (*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n[BBOX-400] 此结果仅对本次呼气检测负责\n[BBOX-401] 测定结果：FeNO 60:11ppb CaNO :1.0ppb\n[BBOX-402] 操作员：蒋细萍\n[BBOX-403] 张日石\n[BBOX-404] 一口气法弥散功能报告\n[BBOX-405] 姓名：\n[BBOX-406] 年龄：38岁\n[BBOX-407] 性别：女\n[BBOX-408] 科别：\n[BBOX-409] 保险：\n[BBOX-410] 预计值模式：Standard-now\n[BBOX-411] 测试号：2026020917\n[BBOX-412] 身高：155 cm\n[BBOX-413] 体重：60 kg\n[BBOX-414] 备注：\n[BBOX-415] ���系电话：\n[BBOX-416] 操作者：蒋细萍\n[BBOX-417] CO (%)\n[BBOX-418] Volume [L]\n[BBOX-419] CH4 [%]\n[BBOX-420] -0.25\n[BBOX-421] 2-0.20\n[BBOX-422] 0-0.15\n[BBOX-423] 2-0.10\n[BBOX-424] 0.05\n[BBOX-425] 4\n[BBOX-426] Time [s]\n[BBOX-427] 0\n[BBOX-428] 5\n[BBOX-429] 10\n[BBOX-430] 15\n[BBOX-431] 20\n[BBOX-432] 25\n[BBOX-433] 30\n[BBOX-434] Pred\n[BBOX-435] Best\n[BBOX-436] Best%\n[BBOX-437] Act1\n[BBOX-438] DLCO SB\n[BBOX-439] [mmol/min/kPa]\n[BBOX-440] 8.08\n[BBOX-441] 9.45\n[BBOX-442] 116.9\n[BBOX-443] 9.45\n[BBOX-444] DLCO/VA\n[BBOX-445] [mmol/min/kPa/L]\n[BBOX-446] 1.82\n[BBOX-447] 2.38\n[BBOX-448] 130.8\n[BBOX-449] 2.38\n[BBOX-450] VA\n[BBOX-451] [L]\n[BBOX-452] 4.29\n[BBOX-453] 3.97\n[BBOX-454] 92.5\n[BBOX-455] 3.97\n[BBOX-456] VC IN\n[BBOX-457] [L]\n[BBOX-458] 3.03\n[BBOX-459] 2.26\n[BBOX-460] 74.6\n[BBOX-461] Discard vol\n[BBOX-462] [L]\n[BBOX-463] 1.00\n[BBOX-464] Sample vol\n[BBOX-465] [L]\n[BBOX-466] 0.53\n[BBOX-467] ERV\n[BBOX-468] [L]\n[BBOX-469] 1.10\n[BBOX-470] IRV\n[BBOX-471] [L]\n[BBOX-472] IC\n[BBOX-473] [L]\n[BBOX-474] 1.93\n[BBOX-475] VT\n[BBOX-476] [L]\n[BBOX-477] 0.43\n[BBOX-478] VC MAX\n[BBOX-479] [L]\n[BBOX-480] 3.03\n[BBOX-481] 2.26\n[BBOX-482] 74.6\n[BBOX-483] TLC-SB\n[BBOX-484] [L]\n[BBOX-485] 4.44\n[BBOX-486] 4.10\n[BBOX-487] 92.4\n[BBOX-488] 4.10\n[BBOX-489] RV-SB\n[BBOX-490] [L]\n[BBOX-491] 1.41\n[BBOX-492] 2.18\n[BBOX-493] 154.5\n[BBOX-494] 2.18\n[BBOX-495] RV%TLC-SB\n[BBOX-496] [%]\n[BBOX-497] 31.88\n[BBOX-498] 53.26\n[BBOX-499] 167.1\n[BBOX-500] 53.26\n[BBOX-501] FRC-SB\n[BBOX-502] [L]\n[BBOX-503] 2.51\n[BBOX-504] 2.39\n[BBOX-505] 95.2\n[BBOX-506] 2.39\n[BBOX-507] FRC%TLC-SB\n[BBOX-508] [%]\n[BBOX-509] 51.18\n[BBOX-510] 58.28\n[BBOX-511] 113.9\n[BBOX-512] 58.28\n[BBOX-513] 测试日期\n[BBOX-514] 26/2/0\n[BBOX-515] 意见：\n[BBOX-516] 1.弥散功能在正常范围。\n[BBOX-517] 2.残气量、残总比增高，肺总量在正常范围。\n[BBOX-518] 张\n[BBOX-519] \\begin{tabular}{lcccccccccc}\n[BBOX-520] \\hline\n[BBOX-521] & Pred & A1 A1/Pd & P1 A2/Pd & chg\\%l & P2 A3/Pd & chg\\%2 & P3 A4/Pd & chg\\%3 & & \\\\\n[BBOX-522] \\hline\n[BBOX-523] FVC & [L.] & 2.99 & 2.21 & 74.0 & 2.63 & 87.9 & 18.72 & 2.04 & 88.2 & 19.17 \\\\\n[BBOX-524] FEV 1 & [L.] & 2.67 & 1.25 & 48.6 & 1.62 & 69.2 & 21.85 & 1.84 & 69.8 & 23.23 \\\\\n[BBOX-525] FEV 1 \\% FVC & [\\%] & 84.19 & 56.48 & 67.1 & 67.97 & 68.9 & 2.64 & 58.40 & 69.4 & 3.41 \\\\\n[BBOX-526] FEV 1 \\% VC MAX & [\\%] & 81.88 & 55.26 & 67.6 & 67.97 & 70.8 & 4.91 & 68.40 & 71.3 & 5.73 \\\\\n[BBOX-527] VC MAX & [L.] & 3.03 & 2.26 & 74.6 & 2.63 & 86.6 & 16.14 & 2.64 & 87.0 & 16.59 \\\\\n[BBOX-528] PEF & [L/s] & 6.28 & 2.66 & 42.4 & 2.90 & 46.2 & 9.17 & 3.37 & 53.7 & 26.79 \\\\\n[BBOX-529] MMEF 75/25 & [L/s] & 3.57 & 0.61 & 14.4 & 0.67 & 18.8 & 31.03 & 0.73 & 20.4 & 42.01 \\\\\n[BBOX-530] MEF 50 & [L/s] & 4.01 & 0.68 & 17.0 & 0.90 & 22.5 & 32.75 & 0.89 & 22.1 & 30.15 \\\\\n[BBOX-531] MEF 25 & [L/s] & 1.79 & 0.19 & 10.5 & 0.27 & 15.2 & 44.16 & 0.33 & 18.7 & 77.66 \\\\\n[BBOX-532] FET & [s] & 7.63 & & & 8.01 & & 4.99 & 7.79 & 2.14 & 7.43 \\\\\n[BBOX-533] V backextrapolation ex [L] & & 0.05 & & 0.04 & & -11.67 & 0.04 & & -18.64 & 0.04 \\\\\n[BBOX-534] PIF & [L/s] & 3.04 & & 3.37 & & 10.91 & 3.51 & & 15.70 & 3.60 \\\\\n[BBOX-535] FIV1 & [L] & 2.21 & & 2.56 & & 15.71 & 2.56 & & 15.66 & 2.50 \\\\\n[BBOX-536] PEF50 \\% FIF50 & [\\%] & 22.86 & & 28.15 & & 23.14 & 25.36 & & 10.95 & 27.28 \\\\\n[BBOX-537] MVV & [L/min] & 99.77 & 46.21 & 46.3 & & & & & & \\\\\n[BBOX-538] BF MVV & [1/min] & & 75.55 & & & & & & & \\\\\n[BBOX-539] \\hline\n[BBOX-540] \\end{tabular}\n[BBOX-541] 金城大药房\n[BBOX-542] 会员号:\n[BBOX-543] 积分: 112550\n[BBOX-544] 本次积分: 596.00\n[BBOX-545] 名称\n[BBOX-546] 规格\n[BBOX-547] 数量\n[BBOX-548] 厂家\n[BBOX-549] 批号\n[BBOX-550] 单价\n[BBOX-551] 金额\n[BBOX-552] 1-布地奈德福莫特罗吸入粉雾剂\n[BBOX-553] 320ug:9ug*60 吸/支\n[BBOX-554] 2.00\n[BBOX-555] 阿斯利康制药\n[BBOX-556] PKMR\n[BBOX-557] 300.00\n[BBOX-558] 596.00\n[BBOX-559] 运动员慎用!!!\n[BBOX-560] ****重打销售单****\n[BBOX-561] 总计数量: 2.00\n[BBOX-562] 应收: 600.00\n[BBOX-563] 优惠: 4.00\n[BBOX-564] 付款: 596.00\n[BBOX-565] 找零: 0.00\n[BBOX-566] 销售单号: 251210031062\n[BBOX-567] 款台号: 2\n[BBOX-568] 日期: 2025-12-10\n[BBOX-569] 15:21:53"
  }
]
2026-08-05 05:46:24,133 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:46:24.132+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:46:53,245 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:46:53,259 INFO     29 [SmartSplitter] SmartSplitter done: 15 chunks from 15 LLM segments (all bbox_id). Types: {'PrescriptionRecord': 2, 'ExaminationReport': 6, 'DischargeRecord': 2, 'AdmissionRecord': 4, 'MedicationRecord': 1}
2026-08-05 05:46:53,267 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 05:46:53,267 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks": "15 items, types={'PrescriptionRecord': 2, 'ExaminationReport': 6, 'DischargeRecord': 2, 'AdmissionRecord': 4, 'MedicationRecord': 1}"}
2026-08-05 05:46:53,267 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 05:46:53,268 INFO     29 [ChunkRouter] Routed 15 chunks into 5 groups: {'chunks_Prescription': 2, 'chunks_Examination': 6, 'chunks_Discharge': 2, 'chunks_Admission': 4, 'chunks_Medication': 1}
2026-08-05 05:46:53,276 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 05:46:53,276 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | ChunkRouter:Router | outputs={"html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks": "15 items, types={'PrescriptionRecord': 2, 'ExaminationReport': 6, 'DischargeRecord': 2, 'AdmissionRecord': 4, 'MedicationRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:46:53,276 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 05:46:53,279 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:46:53,280 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:46:53 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:46:53,281 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:46:54,087 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:46:54,096 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 05:46:54,096 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:46:54,096 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 05:46:54,102 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:46:54,102 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:46:54 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:46:54,103 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:46:54,805 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:46:54,814 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 05:46:54,815 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:46:54,815 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 05:46:54,821 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:46:54,821 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:46:54 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:46:54,822 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:46:55,751 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:46:55,756 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 05:46:55,756 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:46:55,756 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 05:46:55,760 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:46:55,760 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:46:55,761 INFO     29 [qwen-vl-text] positions(29): [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:46:55,761 INFO     29 [qwen-vl-text] page grouping: [18], lines per page: [29]
2026-08-05 05:46:55,896 INFO     29 [qwen-vl-text] page=18, rect=842x592, img=(2339x1646), dpi=200
2026-08-05 05:46:55,898 INFO     29 [qwen-vl-text] LLM extraction start, text_len=243
2026-08-05 05:46:55,898 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:46:55,899 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 541, \"bbox_end\": 569, \"encounter_dates\": [\"2025-12-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "金城大药房\n会员号:\n积分: 112550\n本次积分: 596.00\n名称\n规格\n数量\n厂家\n批号\n单价\n金额\n1-布地奈德福莫特罗吸入粉雾剂\n320ug:9ug*60 吸/支\n2.00\n阿斯利康制药\nPKMR\n300.00\n596.00\n运动员慎用!!!\n****重打销售单****\n总计数量: 2.00\n应收: 600.00\n优惠: 4.00\n付款: 596.00\n找零: 0.00\n销售单号: 251210031062\n款台号: 2\n日期: 2025-12-10\n15:21:53",
    "role": "user"
  }
]
[92m05:46:55 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:46:55,900 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:46:57,020 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:46:57.019+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:46:58,094 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:46:58,094 INFO     29 [qwen-vl-text] LLM output (len=429):
{
  "encounter_date": "2025-12-10",
  "pharmacy": "金城大药房",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": "320ug:9ug*60吸/支",
      "dosage": null,
      "quantity": 2,
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
2026-08-05 05:46:58,094 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-10]
2026-08-05 05:46:58,098 INFO     29 [qwen-vl-text] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1895666, prompt_len=943
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["金城大药房", "会员号:", "积分: 112550", "本次积分: 596.00", "名称", "规格", "数量", "厂家", "批号", "单价", "金额", "1-布地奈德福莫特罗吸入粉雾剂", "320ug:9ug*60 吸/支", "2.00", "阿斯利康制药", "PKMR", "300.00", "596.00", "运动员慎用!!!", "****重打销售单****", "总计数量: 2.00", "应收: 600.00", "优惠: 4.00", "付款: 596.00", "找零: 0.00", "销售单号: 251210031062", "款台号: 2", "日期: 2025-12-10", "15:21:53"]

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
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord API raw response (len=1521):
[
	{"text": "金城大药房", "bbox": [477, 74, 583, 108]},
	{"text": "会员号:", "bbox": [433, 138, 474, 162]},
	{"text": "积分: 112550", "bbox": [432, 170, 514, 194]},
	{"text": "本次积分: 596.00", "bbox": [432, 202, 532, 226]},
	{"text": "名称", "bbox": [430, 264, 458, 289]},
	{"text": "规格", "bbox": [429, 297, 457, 322]},
	{"text": "数量", "bbox": [569, 300, 596, 323]},
	{"text": "厂家", "bbox": [428, 332, 456, 357]},
	{"text": "批号", "bbox": [427, 365, 455, 390]},
	{"text": "单价", "bbox": [494, 368, 522, 393]},
	{"text": "金额", "bbox": [562, 367, 589, 390]},
	{"text": "1-布地奈德福莫特罗吸入粉雾剂", "bbox": [427, 434, 613, 461]},
	{"text": "320ug:9ug*60 吸/支", "bbox": [425, 471, 542, 498]},
	{"text": "2.00", "bbox": [575, 473, 600, 494]},
	{"text": "阿斯利康制药", "bbox": [425, 506, 507, 531]},
	{"text": "PKMR", "bbox": [424, 543, 462, 564]},
	{"text": "300.00", "bbox": [494, 543, 534, 564]},
	{"text": "596.00", "bbox": [562, 543, 601, 564]},
	{"text": "运动员慎用!!!", "bbox": [423, 575, 523, 600]},
	{"text": "****重打销售单****", "bbox": [469, 649, 573, 674]},
	{"text": "总计数量: 2.00", "bbox": [420, 685, 516, 712]},
	{"text": "应收: 600.00", "bbox": [419, 721, 503, 749]},
	{"text": "优惠: 4.00", "bbox": [532, 721, 602, 749]},
	{"text": "付款: 596.00", "bbox": [419, 760, 503, 788]},
	{"text": "找零: 0.00", "bbox": [532, 760, 602, 788]},
	{"text": "销售单号: 251210031062", "bbox": [418, 843, 580, 871]},
	{"text": "款台号: 2", "bbox": [417, 883, 482, 912]},
	{"text": "日期: 2025-12-10", "bbox": [417, 925, 537, 953]},
	{"text": "15:21:53", "bbox": [555, 927, 608, 951]}
]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=8.1s
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[0]: text=金城大药房, bbox=[477, 74, 583, 108]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[1]: text=会员号:, bbox=[433, 138, 474, 162]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[2]: text=积分: 112550, bbox=[432, 170, 514, 194]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[3]: text=本次积分: 596.00, bbox=[432, 202, 532, 226]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[4]: text=名称, bbox=[430, 264, 458, 289]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[5]: text=规格, bbox=[429, 297, 457, 322]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[6]: text=数量, bbox=[569, 300, 596, 323]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[7]: text=厂家, bbox=[428, 332, 456, 357]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[8]: text=批号, bbox=[427, 365, 455, 390]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[9]: text=单价, bbox=[494, 368, 522, 393]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[10]: text=金额, bbox=[562, 367, 589, 390]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[11]: text=1-布地奈德福莫特罗吸入粉雾剂, bbox=[427, 434, 613, 461]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[12]: text=320ug:9ug*60 吸/支, bbox=[425, 471, 542, 498]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[13]: text=2.00, bbox=[575, 473, 600, 494]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[14]: text=阿斯利康制药, bbox=[425, 506, 507, 531]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[15]: text=PKMR, bbox=[424, 543, 462, 564]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[16]: text=300.00, bbox=[494, 543, 534, 564]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[17]: text=596.00, bbox=[562, 543, 601, 564]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[18]: text=运动员慎用!!!, bbox=[423, 575, 523, 600]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[19]: text=****重打销售单****, bbox=[469, 649, 573, 674]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[20]: text=总计数量: 2.00, bbox=[420, 685, 516, 712]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[21]: text=应收: 600.00, bbox=[419, 721, 503, 749]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[22]: text=优惠: 4.00, bbox=[532, 721, 602, 749]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[23]: text=付款: 596.00, bbox=[419, 760, 503, 788]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[24]: text=找零: 0.00, bbox=[532, 760, 602, 788]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[25]: text=销售单号: 251210031062, bbox=[418, 843, 580, 871]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[26]: text=款台号: 2, bbox=[417, 883, 482, 912]
2026-08-05 05:47:06,235 INFO     29 [qwen-vl-text] coord item[27]: text=日期: 2025-12-10, bbox=[417, 925, 537, 953]
2026-08-05 05:47:06,236 INFO     29 [qwen-vl-text] coord item[28]: text=15:21:53, bbox=[555, 927, 608, 951]
2026-08-05 05:47:06,236 INFO     29 [qwen-vl-text] page=18 — 29/29 coords, api_time=8.1s
2026-08-05 05:47:06,236 INFO     29 [qwen-vl-text] new_positions (29):
[[18, 401.5815369873047, 490.82187854003905, 43.840632446289064, 63.98362573242187], [18, 364.53837634277346, 399.0558669433594, 81.75685510253906, 95.9754385986328], [18, 363.696486328125, 432.7314675292969, 100.71496643066406, 114.9335499267578], [18, 363.696486328125, 447.8854877929687, 119.67307775878906, 133.89166125488282], [18, 362.0127062988281, 385.58562670898436, 156.40441845703126, 171.2154429321289], [18, 361.1708162841797, 384.74373669433595, 175.95497076416015, 190.76599523925782], [18, 479.0354183349609, 501.76644873046877, 177.73229370117187, 191.35843621826172], [18, 360.3289262695312, 383.9018466796875, 196.69040502929687, 211.50142950439454], [18, 359.4870362548828, 383.05995666503907, 216.24095733642577, 231.05198181152343], [18, 415.8936672363281, 439.46658764648436, 218.01828027343748, 232.82930474853515], [18, 473.14218823242186, 495.8732186279297, 217.4258392944336, 231.05198181152343], [18, 359.4870362548828, 516.0785789794921, 257.11938488769533, 273.1152913208008], [18, 357.8032562255859, 456.30438793945314, 279.0397011108398, 295.03560754394533], [18, 484.0867584228516, 505.1340087890625, 280.22458306884766, 292.6658436279297], [18, 357.8032562255859, 426.8382374267578, 299.77513537597656, 314.5861598510742], [18, 356.9613662109375, 388.95318676757813, 321.6954515991211, 334.1367121582031], [18, 415.8936672363281, 449.5692678222656, 321.6954515991211, 334.1367121582031], [18, 473.14218823242186, 505.97589880371095, 321.6954515991211, 334.1367121582031], [18, 356.11947619628904, 440.3084776611328, 340.65356292724607, 355.46458740234374], [18, 394.8464168701172, 482.4029783935547, 384.49419537353515, 399.3052198486328], [18, 353.59380615234375, 434.41524755859376, 405.82207061767576, 421.8179770507812], [18, 352.75191613769533, 423.47067736816405, 427.1499458618164, 443.73829327392576], [18, 447.8854877929687, 506.81778881835936, 427.1499458618164, 443.73829327392576], [18, 352.75191613769533, 423.47067736816405, 450.25514404296877, 466.8434914550781], [18, 447.8854877929687, 506.81778881835936, 450.25514404296877, 466.8434914550781], [18, 351.91002612304686, 488.29620849609375, 499.42774530029294, 516.0160927124024], [18, 351.06813610839845, 405.79098706054685, 523.1253844604493, 540.3061728515625], [18, 351.06813610839845, 452.09493786621096, 548.0079055786133, 564.5962529907226], [18, 467.2489581298828, 511.86912890625, 549.192787536621, 563.4113710327148]]
2026-08-05 05:47:06,236 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=10.5s
2026-08-05 05:47:06,241 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 05:47:06,241 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Extractor:Medication | outputs={"chunks": "1 items, types={'MedicationRecord': 1}", "html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:47:06,241 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 05:47:06,246 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:47:06,246 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:47:06,246 INFO     29 [qwen-vl-text] positions(22): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:47:06,247 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [22]
2026-08-05 05:47:06,421 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:47:06,423 INFO     29 [qwen-vl-text] LLM extraction start, text_len=275
2026-08-05 05:47:06,423 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:47:06,423 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 0, \"bbox_end\": 21, \"encounter_dates\": [\"2025-09-30\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "人民医院\nH43120200207, 院区: 燕城院区)\n基本就诊信息\n姓名: 梳\n医生: 旅\n挂号单: 25000448502\n医保号: 5200002600000000600637839\n付款: 城乡居民基本医疗 费别: 普通\n门诊号: 2502240221\n社区号:\n门诊就诊:呼吸内科门诊,2025-09-30 14:50\n医嘱 | 报告\n已作废 | 全部\n处方 | 其他\n生效时间\n内容\n用法\n2025-09-30\n孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/\n睡前口服,每天一次,共30天\n14:51\n盒,共10盒,每次10mg",
    "role": "user"
  }
]
[92m05:47:06 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:47:06,424 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:47:12,173 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:47:12,173 INFO     29 [qwen-vl-text] LLM output (len=407):
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
      "notes": "睡前"
    }
  ]
}
2026-08-05 05:47:12,173 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-30]
2026-08-05 05:47:12,175 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1095422, prompt_len=954
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["人民医院", "H43120200207, 院区: 燕城院区)", "基本就诊信息", "姓名: 梳", "医生: 旅", "挂号单: 25000448502", "医保号: 5200002600000000600637839", "付款: 城乡居民基本医疗 费别: 普通", "门诊号: 2502240221", "社区号:", "门诊就诊:呼吸内科门诊,2025-09-30 14:50", "医嘱 | 报告", "已作废 | 全部", "处方 | 其他", "生效时间", "内容", "用法", "2025-09-30", "孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/", "睡前口服,每天一次,共30天", "14:51", "盒,共10盒,每次10mg"]

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
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord API raw response (len=1258):
[
	{"text": "人民医院", "bbox": [7, 45, 92, 68]},
	{"text": "H43120200207, 院区: 燕城院区)", "bbox": [288, 45, 642, 68]},
	{"text": "基本就诊信息", "bbox": [28, 90, 163, 113]},
	{"text": "姓名: 梳", "bbox": [30, 124, 107, 147]},
	{"text": "医生: 旅", "bbox": [270, 124, 347, 147]},
	{"text": "挂号单: 25000448502", "bbox": [432, 124, 632, 147], "bbox": [432, 124, 632, 147]},
	{"text": "医保号: 5200002600000000600637839", "bbox": [653, 124, 998, 147]},
	{"text": "付款: 城乡居民基本医疗 费别: 普通", "bbox": [31, 152, 370, 175]},
	{"text": "门诊号: 2502240221", "bbox": [432, 152, 618, 175]},
	{"text": "社区号:", "bbox": [652, 152, 725, 175]},
	{"text": "门诊就诊:呼吸内科门诊,2025-09-30 14:50", "bbox": [40, 212, 462, 235]},
	{"text": "医嘱 | 报告", "bbox": [14, 250, 170, 278]},
	{"text": "已作废 | 全部", "bbox": [37, 296, 104, 319]},
	{"text": "处方 | 其他", "bbox": [220, 296, 392, 319]},
	{"text": "生效时间", "bbox": [54, 334, 142, 357]},
	{"text": "内容", "bbox": [417, 334, 462, 357]},
	{"text": "用法", "bbox": [853, 334, 897, 357]},
	{"text": "2025-09-30", "bbox": [35, 364, 145, 382]},
	{"text": "孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/", "bbox": [195, 364, 673, 386]},
	{"text": "睡前口服,每天一次,共30天", "bbox": [731, 372, 985, 395]},
	{"text": "14:51", "bbox": [37, 385, 90, 403]},
	{"text": "盒,共10盒,每次10mg", "bbox": [195, 385, 401, 407]}
]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=7.2s
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[0]: text=人民医院, bbox=[7, 45, 92, 68]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[1]: text=H43120200207, 院区: 燕城院区), bbox=[288, 45, 642, 68]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[2]: text=基本就诊信息, bbox=[28, 90, 163, 113]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[3]: text=姓名: 梳, bbox=[30, 124, 107, 147]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[4]: text=医生: 旅, bbox=[270, 124, 347, 147]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[5]: text=挂号单: 25000448502, bbox=[432, 124, 632, 147]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[6]: text=医保号: 5200002600000000600637839, bbox=[653, 124, 998, 147]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[7]: text=付款: 城乡居民基本医疗 费别: 普通, bbox=[31, 152, 370, 175]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[8]: text=门诊号: 2502240221, bbox=[432, 152, 618, 175]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[9]: text=社区号:, bbox=[652, 152, 725, 175]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[10]: text=门诊就诊:呼吸内科门诊,2025-09-30 14:50, bbox=[40, 212, 462, 235]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[11]: text=医嘱 | 报告, bbox=[14, 250, 170, 278]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[12]: text=已作废 | 全部, bbox=[37, 296, 104, 319]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[13]: text=处方 | 其他, bbox=[220, 296, 392, 319]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[14]: text=生效时间, bbox=[54, 334, 142, 357]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[15]: text=内容, bbox=[417, 334, 462, 357]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[16]: text=用法, bbox=[853, 334, 897, 357]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[17]: text=2025-09-30, bbox=[35, 364, 145, 382]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[18]: text=孟鲁司特钠片(杭州默沙东) (默沙东)10mg*5s/, bbox=[195, 364, 673, 386]
2026-08-05 05:47:19,392 INFO     29 [qwen-vl-text] coord item[19]: text=睡前口服,每天一次,共30天, bbox=[731, 372, 985, 395]
2026-08-05 05:47:19,393 INFO     29 [qwen-vl-text] coord item[20]: text=14:51, bbox=[37, 385, 90, 403]
2026-08-05 05:47:19,393 INFO     29 [qwen-vl-text] coord item[21]: text=盒,共10盒,每次10mg, bbox=[195, 385, 401, 407]
2026-08-05 05:47:19,393 INFO     29 [qwen-vl-text] page=0 — 22/22 coords, api_time=7.2s
2026-08-05 05:47:19,393 INFO     29 [qwen-vl-text] new_positions (22):
[[0, 5.894, 77.464, 26.775, 40.46], [0, 242.49599999999998, 540.564, 26.775, 40.46], [0, 23.576, 137.246, 53.55, 67.235], [0, 25.259999999999998, 90.094, 73.78, 87.46499999999999], [0, 227.34, 292.174, 73.78, 87.46499999999999], [0, 363.74399999999997, 532.144, 73.78, 87.46499999999999], [0, 549.826, 840.3159999999999, 73.78, 87.46499999999999], [0, 26.102, 311.53999999999996, 90.44, 104.125], [0, 363.74399999999997, 520.356, 90.44, 104.125], [0, 548.984, 610.4499999999999, 90.44, 104.125], [0, 33.68, 389.00399999999996, 126.14, 139.825], [0, 11.788, 143.14, 148.75, 165.41], [0, 31.154, 87.568, 176.12, 189.80499999999998], [0, 185.23999999999998, 330.06399999999996, 176.12, 189.80499999999998], [0, 45.467999999999996, 119.564, 198.73, 212.415], [0, 351.114, 389.00399999999996, 198.73, 212.415], [0, 718.226, 755.274, 198.73, 212.415], [0, 29.47, 122.08999999999999, 216.57999999999998, 227.29], [0, 164.19, 566.6659999999999, 216.57999999999998, 229.67], [0, 615.502, 829.37, 221.34, 235.02499999999998], [0, 31.154, 75.78, 229.075, 239.785], [0, 164.19, 337.642, 229.075, 242.165]]
2026-08-05 05:47:19,393 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=13.1s
2026-08-05 05:47:19,393 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:47:19,393 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:47:19,393 INFO     29 [qwen-vl-text] positions(28): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:47:19,393 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [28]
2026-08-05 05:47:19,550 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:47:19,551 INFO     29 [qwen-vl-text] LLM extraction start, text_len=373
2026-08-05 05:47:19,551 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:47:19,551 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 22, \"bbox_end\": 49, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"怀化市刘仁水介入呼吸病学工作室\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "基本就诊信息\n姓名：杨\n医生：\n挂号单：26000068319\n医保号：52000026000000006006378395\n付款：城乡居民基本医疗 费别：普通\n门诊号：2502240221\n社区号：\n门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04\n医嘱|报告|\n已作废|全部|处方|其他\n生效时间\n内容\n用法\n2026-02-09\n肺功能全套+支气管舒张试验,共1次\n2026-02-09\n(基)硫酸沙丁胺醇吸入气雾剂 (山东)\n吸入,一次,共1天\n11:08\n100ug*200揿/瓶,共1瓶,每次400ug\n2026-02-09\n呼出气一氧化氮测定,共1次\n2026-02-09\n沙美特罗替卡松粉吸入剂(法国GLAXO)\n吸入,每天二次,共1天\n12.33\n50ug/500ug*60吸/瓶,共1瓶,每次50ug",
    "role": "user"
  }
]
[92m05:47:19 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:47:19,553 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:47:23,251 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:47:23,251 INFO     29 [qwen-vl-text] LLM output (len=675):
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
      "notes": null
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
      "notes": null
    }
  ]
}
2026-08-05 05:47:23,251 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-09]
2026-08-05 05:47:23,252 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1192752, prompt_len=1070
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
2026-08-05 05:47:32,767 INFO     29 [qwen-vl-text] coord API raw response (len=1595):
[
	{"text": "基本就诊信息", "bbox": [44, 284, 169, 306]},
	{"text": "姓名：杨", "bbox": [45, 315, 120, 337]},
	{"text": "医生：", "bbox": [270, 315, 335, 337]},
	{"text": "挂号单：26000068319", "bbox": [425, 315, 619, 337]},
	{"text": "医保号：52000026000000006006378395", "bbox": [639, 315, 994, 337]},
	{"text": "付款：城乡居民基本医疗 费别：普通", "bbox": [45, 341, 365, 363]},
	{"text": "门诊号：2502240221", "bbox": [424, 341, 606, 363]},
	{"text": "社区号：", "bbox": [638, 341, 712, 363]},
	{"text": "门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04", "bbox": [52, 392, 647, 413]},
	{"text": "医嘱|报告|", "bbox": [28, 426, 197, 449]},
	{"text": "已作废|全部|处方|其他", "bbox": [17, 463, 388, 486]},
	{"text": "生效时间", "bbox": [65, 498, 149, 519]},
	{"text": "内容", "bbox": [410, 498, 453, 519]},
	{"text": "用法", "bbox": [844, 498, 887, 519]},
	{"text": "2026-02-09", "bbox": [48, 525, 152, 541]},
	{"text": "肺功能全套+支气管舒张试验,共1次", "bbox": [200, 524, 530, 545]},
	{"text": "2026-02-09", "bbox": [48, 550, 152, 567]},
	{"text": "(基)硫酸沙丁胺醇吸入气雾剂 (山东)", "bbox": [200, 548, 571, 569]},
	{"text": "吸入,一次,共1天", "bbox": [720, 556, 883, 578]},
	{"text": "11:08", "bbox": [50, 568, 101, 584]},
	{"text": "100ug*200揿/瓶,共1瓶,每次400ug", "bbox": [200, 567, 521, 587]},
	{"text": "2026-02-09", "bbox": [48, 591, 152, 607]},
	{"text": "呼出气一氧化氮测定,共1次", "bbox": [200, 590, 457, 611]},
	{"text": "2026-02-09", "bbox": [48, 616, 152, 633]},
	{"text": "沙美特罗替卡松粉吸入剂(法国GLAXO)", "bbox": [200, 614, 551, 635]},
	{"text": "吸入,每天二次,共1天", "bbox": [720, 622, 924, 644]},
	{"text": "12.33", "bbox": [50, 634, 101, 650]},
	{"text": "50ug/500ug*60吸/瓶,共1瓶,每次50ug", "bbox": [200, 633, 553, 654]}
]
2026-08-05 05:47:32,767 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=9.5s
2026-08-05 05:47:32,767 INFO     29 [qwen-vl-text] coord item[0]: text=基本就诊信息, bbox=[44, 284, 169, 306]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：杨, bbox=[45, 315, 120, 337]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[2]: text=医生：, bbox=[270, 315, 335, 337]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[3]: text=挂号单：26000068319, bbox=[425, 315, 619, 337]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[4]: text=医保号：52000026000000006006378395, bbox=[639, 315, 994, 337]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[5]: text=付款：城乡居民基本医疗 费别：普通, bbox=[45, 341, 365, 363]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[6]: text=门诊号：2502240221, bbox=[424, 341, 606, 363]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[7]: text=社区号：, bbox=[638, 341, 712, 363]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[8]: text=门诊就诊：怀化市刘仁水介入呼吸病学工作室,2026-02-09 11:04, bbox=[52, 392, 647, 413]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[9]: text=医嘱|报告|, bbox=[28, 426, 197, 449]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[10]: text=已作废|全部|处方|其他, bbox=[17, 463, 388, 486]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[11]: text=生效时间, bbox=[65, 498, 149, 519]
2026-08-05 05:47:32,768 INFO     29 [qwen-vl-text] coord item[12]: text=内容, bbox=[410, 498, 453, 519]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[13]: text=用法, bbox=[844, 498, 887, 519]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[14]: text=2026-02-09, bbox=[48, 525, 152, 541]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[15]: text=肺功能全套+支气管舒张试验,共1次, bbox=[200, 524, 530, 545]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[16]: text=2026-02-09, bbox=[48, 550, 152, 567]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[17]: text=(基)硫酸沙丁胺醇吸入气雾剂 (山东), bbox=[200, 548, 571, 569]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[18]: text=吸入,一次,共1天, bbox=[720, 556, 883, 578]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[19]: text=11:08, bbox=[50, 568, 101, 584]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[20]: text=100ug*200揿/瓶,共1瓶,每次400ug, bbox=[200, 567, 521, 587]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[21]: text=2026-02-09, bbox=[48, 591, 152, 607]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[22]: text=呼出气一氧化氮测定,共1次, bbox=[200, 590, 457, 611]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[23]: text=2026-02-09, bbox=[48, 616, 152, 633]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[24]: text=沙美特罗替卡松粉吸入剂(法国GLAXO), bbox=[200, 614, 551, 635]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[25]: text=吸入,每天二次,共1天, bbox=[720, 622, 924, 644]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[26]: text=12.33, bbox=[50, 634, 101, 650]
2026-08-05 05:47:32,769 INFO     29 [qwen-vl-text] coord item[27]: text=50ug/500ug*60吸/瓶,共1瓶,每次50ug, bbox=[200, 633, 553, 654]
2026-08-05 05:47:32,770 INFO     29 [qwen-vl-text] page=1 — 28/28 coords, api_time=9.5s
2026-08-05 05:47:32,770 INFO     29 [qwen-vl-text] new_positions (28):
[[1, 37.048, 142.298, 168.98, 182.07], [1, 37.89, 101.03999999999999, 187.42499999999998, 200.515], [1, 227.34, 282.07, 187.42499999999998, 200.515], [1, 357.84999999999997, 521.198, 187.42499999999998, 200.515], [1, 538.038, 836.948, 187.42499999999998, 200.515], [1, 37.89, 307.33, 202.89499999999998, 215.98499999999999], [1, 357.008, 510.252, 202.89499999999998, 215.98499999999999], [1, 537.196, 599.504, 202.89499999999998, 215.98499999999999], [1, 43.784, 544.774, 233.23999999999998, 245.73499999999999], [1, 23.576, 165.874, 253.47, 267.155], [1, 14.314, 326.69599999999997, 275.485, 289.16999999999996], [1, 54.73, 125.458, 296.31, 308.805], [1, 345.21999999999997, 381.426, 296.31, 308.805], [1, 710.648, 746.8539999999999, 296.31, 308.805], [1, 40.416, 127.984, 312.375, 321.895], [1, 168.4, 446.26, 311.78, 324.275], [1, 40.416, 127.984, 327.25, 337.365], [1, 168.4, 480.782, 326.06, 338.555], [1, 606.24, 743.486, 330.82, 343.90999999999997], [1, 42.1, 85.042, 337.96, 347.47999999999996], [1, 168.4, 438.68199999999996, 337.365, 349.265], [1, 40.416, 127.984, 351.645, 361.16499999999996], [1, 168.4, 384.794, 351.05, 363.54499999999996], [1, 40.416, 127.984, 366.52, 376.635], [1, 168.4, 463.942, 365.33, 377.825], [1, 606.24, 778.0079999999999, 370.09, 383.18], [1, 42.1, 85.042, 377.22999999999996, 386.75], [1, 168.4, 465.626, 376.635, 389.13]]
2026-08-05 05:47:32,770 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=13.4s
2026-08-05 05:47:32,785 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 05:47:32,786 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Extractor:Prescription | outputs={"chunks": "2 items, types={'PrescriptionRecord': 2}", "html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:47:32,786 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 05:47:32,787 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:47:32.786+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:47:32,794 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:47:32,794 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-05 05:47:32,794 INFO     29 [qwen-vl-text] positions(36): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:47:32,795 INFO     29 [qwen-vl-text] page grouping: [5, 6], lines per page: [35, 1]
2026-08-05 05:47:33,035 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:47:33,298 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:47:33,300 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1106
2026-08-05 05:47:33,300 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:47:33,301 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 100, \"bbox_end\": 135, \"encounter_dates\": [\"2025-07-11\", \"2025-07-22\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "HUAIHUA CENTRAL HOSPITAL\n怀化市肿瘤医院\n姓名：\n性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n221028180\n3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总\n神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓\n浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经\n(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞\n<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌\n(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支\n持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司\n特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前\n好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。\n出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发\n热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，\nBP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。\n心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。\n出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧\n段结节（LU-RADS 2类）。\n出院医嘱：\n1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生\n活习惯，增强体质，适当运动，加强营养；\n2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复\n查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；\n3.出院后继续服用中药。\n4.出院带药：\n舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱\n口，根据动态复查肺功能结果，调整用药）\n祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次\n抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次\n5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；\n6.如有不适，随时医院就诊，我科随诊。\n科室护士办公室电话：0745-2329117。主管医师电话：13789357317\n医师签名：主治医师\nzz1028180",
    "role": "user"
  }
]
[92m05:47:33 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:47:33,302 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:47:48,823 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:47:48,823 INFO     29 [qwen-vl-text] LLM output (len=2111):
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
  "auxiliary_exams": "神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌(TB-DNA)定性、细菌及真菌培养均阴性。",
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
  "discharge_orders": "1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生活习惯，增强体质，适当运动，加强营养；\n2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；\n3.出院后继续服用中药。\n4.出院带药：\n舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱口，根据动态复查肺功能结果，调整用药）\n祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次\n抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次\n5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；\n6.如有不适，随时医院就诊，我科随诊。",
  "do_medications": [
    "布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次",
    "乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次",
    "孟鲁司特钠片 每次10mg（1片） 口服 每晚一次"
  ],
  "do_follow_up": "2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；如有不适，随时医院就诊，我科随诊。",
  "do_precautions": [
    "注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生活习惯，增强体质，适当运动，加强营养",
    "出院后继续服用中药"
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
2026-08-05 05:47:48,826 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1391013, prompt_len=1814
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
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord API raw response (len=2629):
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
	{"text": "<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌", "bbox": [188, 207, 798, 225]},
	{"text": "(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支", "bbox": [188, 233, 805, 252]},
	{"text": "持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司", "bbox": [188, 260, 798, 278]},
	{"text": "特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前", "bbox": [188, 286, 805, 304]},
	{"text": "好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。", "bbox": [188, 313, 646, 331]},
	{"text": "出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发", "bbox": [204, 340, 805, 358]},
	{"text": "热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，", "bbox": [188, 366, 744, 384]},
	{"text": "BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。", "bbox": [188, 392, 805, 410]},
	{"text": "心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "bbox": [188, 418, 776, 437]},
	{"text": "出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧", "bbox": [188, 445, 805, 463]},
	{"text": "段结节（LU-RADS 2类）。", "bbox": [188, 471, 361, 489]},
	{"text": "出院医嘱：", "bbox": [204, 498, 272, 516]},
	{"text": "1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生", "bbox": [212, 524, 800, 543]},
	{"text": "活习惯，增强体质，适当运动，加强营养；", "bbox": [188, 550, 475, 569]},
	{"text": "2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复", "bbox": [212, 577, 800, 595]},
	{"text": "查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；", "bbox": [188, 603, 660, 621]},
	{"text": "3.出院后继续服用中药。", "bbox": [212, 630, 376, 648]},
	{"text": "4.出院带药：", "bbox": [212, 656, 296, 674]},
	{"text": "舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱", "bbox": [212, 683, 807, 701]},
	{"text": "口，根据动态复查肺功能结果，调整用药）", "bbox": [188, 709, 477, 727]},
	{"text": "祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次", "bbox": [258, 735, 647, 754]},
	{"text": "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次", "bbox": [212, 761, 647, 780]},
	{"text": "5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；", "bbox": [212, 788, 622, 806]},
	{"text": "6.如有不适，随时医院就诊，我科随诊。", "bbox": [212, 814, 487, 833]},
	{"text": "科室护士办公室电话：0745-2329117。主管医师电话：13789357317", "bbox": [188, 841, 647, 859]},
	{"text": "医师签名：主治医师", "bbox": [518, 867, 660, 885]}
]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=13.7s
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[0]: text=HUAIHUA CENTRAL HOSPITAL, bbox=[282, 10, 444, 23]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[1]: text=怀化市肿瘤医院, bbox=[282, 24, 444, 39]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[188, 59, 226, 77]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：, bbox=[289, 60, 757, 78]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[4]: text=221028180, bbox=[188, 77, 259, 92]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[5]: text=3.0ppd。神经传导速度，结果：MCV 提示：双侧桡神经、尺神经、正中神经、胫神经、腓总, bbox=[188, 102, 805, 120]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[6]: text=神经波幅、潜伏期、传导速度在正常范围，SCV 提示：双侧桡神经、尺神经、腓肠神经、腓, bbox=[188, 128, 805, 146]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[7]: text=浅神经波幅、传导速度在正常范围；双侧正中神经传导速度减慢，结论：考虑双侧正中神经, bbox=[188, 154, 805, 172]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[8]: text=(感觉纤维)呈脱髓鞘病损。【痰液】革兰氏染色检查：上皮细胞 <10 /LP、白细胞, bbox=[194, 180, 759, 199]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[9]: text=<10 /LP、GS阳性杆菌 偶见、GS阳性链状排列球菌 1+，标本不合格；抗酸染色、结核杆菌, bbox=[188, 207, 798, 225]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[10]: text=(TB-DNA)定性、细菌及真菌培养均阴性。请相关科室会诊，结合病史查体及资料，目前不支, bbox=[188, 233, 805, 252]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[11]: text=持EGPA诊断。入院后予以甲泼尼龙40mg qd静滴抗炎、止咳祛痰、雾化舒张支气管、孟鲁司, bbox=[188, 260, 798, 278]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[12]: text=特钠片抗气道炎症、解痉平喘、补液、中药调理及中医外治等对症支持治疗，患者病情较前, bbox=[188, 286, 805, 304]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[13]: text=好转，今患者要求出院，请示张田慧副主任医师后，予以办理出院。, bbox=[188, 313, 646, 331]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[14]: text=出院情况：患者胸闷气促基本缓解，偶有咳嗽，少许白痰，无胸痛咯血、盗汗，无畏寒发, bbox=[204, 340, 805, 358]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[15]: text=热。精神、饮食、睡眠尚可，大小便正常。查体：T36.8℃，P68次/分，R20次/分，, bbox=[188, 366, 744, 384]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[16]: text=BP118/72mmHg，指脉氧饱和度96%。神志清楚，精神尚可。双肺呼吸音清，未闻及明显啰音。, bbox=[188, 392, 805, 410]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[17]: text=心率68次/分，律齐无杂音。腹部平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。, bbox=[188, 418, 776, 437]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[18]: text=出院诊断：1.支气管哮喘急性发作期 IgE介导；2.肺炎（CURB-65 0分） 3.右肺中叶内侧, bbox=[188, 445, 805, 463]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[19]: text=段结节（LU-RADS 2类）。, bbox=[188, 471, 361, 489]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[20]: text=出院医嘱：, bbox=[204, 498, 272, 516]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[21]: text=1.注意休息，避免着凉及感染，避免二手烟、厨房油烟及刺激性气体吸入，保持良好生, bbox=[212, 524, 800, 543]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[22]: text=活习惯，增强体质，适当运动，加强营养；, bbox=[188, 550, 475, 569]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[23]: text=2.2-3月后返院复查嗜酸性粒细胞、总IgE、肺功能、呼出气一氧化氮评估病情，定期复, bbox=[212, 577, 800, 595]
2026-08-05 05:48:02,487 INFO     29 [qwen-vl-text] coord item[24]: text=查尿常规、尿沉渣、电解质等检查，每年复查胸部CT评估肺结节变化；, bbox=[188, 603, 660, 621]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[25]: text=3.出院后继续服用中药。, bbox=[212, 630, 376, 648]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[26]: text=4.出院带药：, bbox=[212, 656, 296, 674]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[27]: text=舒张支气管：布地奈德福莫特罗吸入粉雾剂 每次320ug（1泡）吸入 每天2次（吸入后漱, bbox=[212, 683, 807, 701]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[28]: text=口，根据动态复查肺功能结果，调整用药）, bbox=[188, 709, 477, 727]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[29]: text=祛痰：乙酰半胱氨酸片 每天0.6g（1片） 口服 一天两次, bbox=[258, 735, 647, 754]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[30]: text=抗气道炎症：孟鲁司特钠片 每次10mg（1片） 口服 每晚一次, bbox=[212, 761, 647, 780]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[31]: text=5.定期复查神经传导速度，神经内科、风湿免疫科门诊随诊；, bbox=[212, 788, 622, 806]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[32]: text=6.如有不适，随时医院就诊，我科随诊。, bbox=[212, 814, 487, 833]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[33]: text=科室护士办公室电话：0745-2329117。主管医师电话：13789357317, bbox=[188, 841, 647, 859]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] coord item[34]: text=医师签名：主治医师, bbox=[518, 867, 660, 885]
2026-08-05 05:48:02,488 INFO     29 [qwen-vl-text] page=5 — 35/35 coords, api_time=13.7s
2026-08-05 05:48:02,490 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1584125, prompt_len=624
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
2026-08-05 05:48:04,070 INFO     29 [qwen-vl-text] coord API raw response (len=66):
```json
[
	{"text": "zz1028180", "bbox": [171, 33, 246, 52]}
]
```
2026-08-05 05:48:04,071 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-05 05:48:04,071 INFO     29 [qwen-vl-text] coord item[0]: text=zz1028180, bbox=[171, 33, 246, 52]
2026-08-05 05:48:04,071 INFO     29 [qwen-vl-text] page=6 — 1/1 coords, api_time=1.6s
2026-08-05 05:48:04,072 INFO     29 [qwen-vl-text] new_positions (36):
[[5, 237.444, 373.848, 5.949999999999999, 13.684999999999999], [5, 237.444, 373.848, 14.28, 23.205], [5, 158.296, 190.292, 35.105, 45.815], [5, 243.338, 637.394, 35.699999999999996, 46.41], [5, 158.296, 218.078, 45.815, 54.739999999999995], [5, 158.296, 677.81, 60.69, 71.39999999999999], [5, 158.296, 677.81, 76.16, 86.86999999999999], [5, 158.296, 677.81, 91.63, 102.33999999999999], [5, 163.34799999999998, 639.078, 107.1, 118.405], [5, 158.296, 671.9159999999999, 123.16499999999999, 133.875], [5, 158.296, 677.81, 138.635, 149.94], [5, 158.296, 671.9159999999999, 154.7, 165.41], [5, 158.296, 677.81, 170.17, 180.88], [5, 158.296, 543.932, 186.23499999999999, 196.945], [5, 171.768, 677.81, 202.29999999999998, 213.01], [5, 158.296, 626.448, 217.76999999999998, 228.48], [5, 158.296, 677.81, 233.23999999999998, 243.95], [5, 158.296, 653.3919999999999, 248.70999999999998, 260.015], [5, 158.296, 677.81, 264.775, 275.485], [5, 158.296, 303.962, 280.245, 290.955], [5, 171.768, 229.024, 296.31, 307.02], [5, 178.504, 673.6, 311.78, 323.085], [5, 158.296, 399.95, 327.25, 338.555], [5, 178.504, 673.6, 343.315, 354.025], [5, 158.296, 555.72, 358.78499999999997, 369.495], [5, 178.504, 316.592, 374.84999999999997, 385.56], [5, 178.504, 249.232, 390.32, 401.03], [5, 178.504, 679.494, 406.385, 417.09499999999997], [5, 158.296, 401.63399999999996, 421.85499999999996, 432.565], [5, 217.236, 544.774, 437.325, 448.63], [5, 178.504, 544.774, 452.79499999999996, 464.09999999999997], [5, 178.504, 523.7239999999999, 468.85999999999996, 479.57], [5, 178.504, 410.054, 484.33, 495.635], [5, 158.296, 544.774, 500.395, 511.10499999999996], [5, 436.156, 555.72, 515.865, 526.5749999999999], [6, 143.982, 207.132, 19.634999999999998, 30.939999999999998]]
2026-08-05 05:48:04,072 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=2, time=31.3s
2026-08-05 05:48:04,073 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:48:04,073 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-05 05:48:04,073 INFO     29 [qwen-vl-text] positions(48): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:48:04,074 INFO     29 [qwen-vl-text] page grouping: [9, 10], lines per page: [33, 15]
2026-08-05 05:48:04,397 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:48:04,578 INFO     29 [qwen-vl-text] page=10, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:48:04,580 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1599
2026-08-05 05:48:04,580 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:48:04,580 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 211, \"bbox_end\": 258, \"encounter_dates\": [\"2025-02-24\", \"2025-03-01\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n入院时间：2025-02-24 12:22\n出院时间：2025-03-01 10:00\n住院天数：5天\n记录时间：2025-02-28 20:39\n入院诊断：胸闷、气促查因：支气管哮喘可能性大\n入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。\n体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸\n氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89\n次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。\n诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C\n+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、\n肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体\n测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。\n心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1\n0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范\n围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO\n2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球\n菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、\n两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，\nLU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能\n结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、\n抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者\n及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。\n出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶\n心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，\nBP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心\n率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。\n出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：\n功能性消化不良？反流性食管炎？其他。\n出院医嘱：\n（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺\n激性烟雾及吸入二手烟；\n姓名：\n性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n220999152\n(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；\n(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；\n(4) 继续用药：\n舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服\n布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入\n(吸入后漱口，根据动态复查肺功能结果，调整用药)\n抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服\n止咳祛痰：润肺膏 每次15g 每天2次，口服\n调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服\n(5) 如有不适，随时医院就诊，我科随诊。\n科室电话：0745-2329117 主管医师电话：13789357317\n医师签名：主治医师：",
    "role": "user"
  }
]
[92m05:48:04 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:48:04,581 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:48:05,510 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:48:05.508+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:48:28,826 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:48:28,827 INFO     29 [qwen-vl-text] LLM output (len=3192):
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
  "auxiliary_exams": "尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C +3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO 2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、两次抗酸染色、TB-DNA均阴性。",
  "imaging_findings": "胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。",
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
  "discharge_orders": "（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺激性烟雾及吸入二手烟；(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；(4) 继续用药：舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服；布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入（吸入后漱口，根据动态复查肺功能结果，调整用药）；抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服；止咳祛痰：润肺膏 每次15g 每天2次，口服；调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服；(5) 如有不适，随时医院就诊，我科随诊。",
  "do_medications": [
    "复方甲氧那明胶囊 每次2粒 每天3次 口服",
    "布地奈德福莫特罗吸入粉雾剂 每次320ug（1包） 每天1次 吸入",
    "孟鲁司特钠片 每次10mg（1片） 每晚1次 口服",
    "润肺膏 每次15g 每天2次 口服",
    "马来酸曲美布汀片 每次0.1g（1片） 每天3次 口服"
  ],
  "do_follow_up": "3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；如有不适，随时医院就诊，我科随诊。",
  "do_precautions": [
    "避免接触一切可能过敏源",
    "注意保暖，避免感冒受凉",
    "避免剧烈运动",
    "避免接触刺激性烟雾及吸入二手烟",
    "吸入布地奈德福莫特罗吸入粉雾剂后漱口，根据动态复查肺功能结果调整用药"
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
2026-08-05 05:48:28,827 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-01]
2026-08-05 05:48:28,835 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2954195, prompt_len=1923
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
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord API raw response (len=2660):
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
	{"text": "结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、", "bbox": [194, 576, 814, 595]},
	{"text": "抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者", "bbox": [194, 602, 821, 622]},
	{"text": "及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。", "bbox": [194, 629, 625, 648]},
	{"text": "出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶", "bbox": [194, 655, 820, 674]},
	{"text": "心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，", "bbox": [194, 681, 755, 699]},
	{"text": "BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心", "bbox": [194, 707, 812, 726]},
	{"text": "率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。", "bbox": [194, 733, 757, 752]},
	{"text": "出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：", "bbox": [194, 759, 815, 778]},
	{"text": "功能性消化不良？反流性食管炎？其他。", "bbox": [194, 785, 466, 804]},
	{"text": "出院医嘱：", "bbox": [194, 811, 260, 829]},
	{"text": "（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺", "bbox": [223, 837, 815, 855]},
	{"text": "激性烟雾及吸入二手烟；", "bbox": [194, 862, 353, 880]}
]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=14.1s
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[476, 18, 557, 40]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[1]: text=入院时间：2025-02-24 12:22, bbox=[194, 50, 404, 69]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[2]: text=出院时间：2025-03-01 10:00, bbox=[194, 77, 404, 95]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[3]: text=住院天数：5天, bbox=[194, 103, 299, 121]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[4]: text=记录时间：2025-02-28 20:39, bbox=[194, 129, 403, 147]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[5]: text=入院诊断：胸闷、气促查因：支气管哮喘可能性大, bbox=[194, 155, 544, 174]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[6]: text=入院情况：青年女性，因“反复胸闷、气促8年，加重半年”入院。既往体质一般无特殊。, bbox=[194, 180, 814, 200]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[7]: text=体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸, bbox=[194, 207, 822, 226]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[8]: text=氧），急性面容，神志清晰，颈静脉无充盈，双肺呼吸音清，可闻及弥漫性哮鸣音。心率89, bbox=[194, 233, 831, 253]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[9]: text=次/分，心律齐，无杂音。腹部平软，无压痛及反跳痛。双下肢无浮肿。辅助检查：无。, bbox=[194, 260, 797, 279]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[10]: text=诊疗经过：入院后完善检查：尿常规：隐血 +2.00、PH 6.00、尿比重 1.02、维生素C, bbox=[194, 286, 790, 305]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[11]: text=+3.00。血清总IgE 221.59IU/ml。血气分析、血常规、大便常规、降钙素原、白介素6测定、, bbox=[194, 313, 829, 332]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[12]: text=肝功能、心肌酶谱、肾功能、葡萄糖测定、电解质、超敏C反应蛋白、凝血常规、D-二聚体, bbox=[194, 339, 820, 359]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[13]: text=测定、输血前常规、新冠肺炎病毒核酸检测、甲乙流感病毒抗原快速检测均未见明显异常。, bbox=[194, 366, 820, 385]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[14]: text=心电图：1.窦性心律 2.正常心电图。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1, bbox=[194, 392, 796, 411]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[15]: text=0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性；2.弥散功能在正常范, bbox=[194, 418, 819, 438]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[16]: text=围；肺总量在正常范围，残气量、残总比增高。呼出气一氧化氮试验：FeNO50 11ppd，CaNO, bbox=[194, 445, 816, 464]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[17]: text=2.0ppd。[痰液]革兰氏染色检查：上皮细胞 >25 /LP、白细胞 <10 /LP、GS阳性链状排列球, bbox=[194, 471, 825, 490]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[18]: text=菌 2+、GS阴性杆菌 少量、GS阴性双球菌 少量、GS阳性球菌 1+，痰标本不合格；细菌培养、, bbox=[194, 497, 832, 517]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[19]: text=两次抗酸染色、TB-DNA均阴性。心电图：正常心电图。胸部CT平扫：右肺中叶内侧段结节，, bbox=[194, 524, 814, 543]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[20]: text=LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。结合患者病史、临床表现及肺功能, bbox=[194, 550, 815, 569]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[21]: text=结果，可诊断“支气管哮喘急性发作期”，住院期间经抗炎平喘、舒张支气管、止咳化痰、, bbox=[194, 576, 814, 595]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[22]: text=抗气道炎症、护胃、促进胃肠动力、调节胃肠功能、补液等治疗后，症状较前好转，今患者, bbox=[194, 602, 821, 622]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[23]: text=及家属要求出院，请示刘仁水主任医师后，予以办理带药出院。, bbox=[194, 629, 625, 648]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[24]: text=出院情况：患者诉胸闷、气促明显好转，夜间稍有喘息，无发热、咳痰，无腹痛、腹胀、恶, bbox=[194, 655, 820, 674]
2026-08-05 05:48:42,919 INFO     29 [qwen-vl-text] coord item[25]: text=心，精神、食纳、睡眠尚可，大小便正常。查体：T36.6℃，P78次/分，R21次/分，, bbox=[194, 681, 755, 699]
2026-08-05 05:48:42,920 INFO     29 [qwen-vl-text] coord item[26]: text=BP126/78mmHg，血氧饱和度96%。神清，精神尚可。双肺呼吸音清，可闻及少许哮鸣音。心, bbox=[194, 707, 812, 726]
2026-08-05 05:48:42,920 INFO     29 [qwen-vl-text] coord item[27]: text=率78次/分，律齐无杂音。腹平软，无压痛及反跳痛，肠鸣音正常。双下肢无水肿。, bbox=[194, 733, 757, 752]
2026-08-05 05:48:42,920 INFO     29 [qwen-vl-text] coord item[28]: text=出院诊断：1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：, bbox=[194, 759, 815, 778]
2026-08-05 05:48:42,920 INFO     29 [qwen-vl-text] coord item[29]: text=功能性消化不良？反流性食管炎？其他。, bbox=[194, 785, 466, 804]
2026-08-05 05:48:42,920 INFO     29 [qwen-vl-text] coord item[30]: text=出院医嘱：, bbox=[194, 811, 260, 829]
2026-08-05 05:48:42,920 INFO     29 [qwen-vl-text] coord item[31]: text=（1）避免接触一切可能过敏源，注意保暖，避免感冒受凉，避免剧烈运动，避免接触刺, bbox=[223, 837, 815, 855]
2026-08-05 05:48:42,920 INFO     29 [qwen-vl-text] coord item[32]: text=激性烟雾及吸入二手烟；, bbox=[194, 862, 353, 880]
2026-08-05 05:48:42,920 INFO     29 [qwen-vl-text] page=9 — 33/33 coords, api_time=14.1s
2026-08-05 05:48:42,921 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=812427, prompt_len=1045
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
2026-08-05 05:48:50,271 INFO     29 [qwen-vl-text] coord API raw response (len=1050):
[
	{"text": "姓名：", "bbox": [114, 117, 187, 140]},
	{"text": "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "bbox": [250, 117, 871, 140]},
	{"text": "220999152", "bbox": [114, 140, 207, 159]},
	{"text": "(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；", "bbox": [145, 172, 940, 197]},
	{"text": "(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；", "bbox": [145, 206, 848, 231]},
	{"text": "(4) 继续用药：", "bbox": [145, 240, 275, 264]},
	{"text": "舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服", "bbox": [124, 274, 818, 299]},
	{"text": "布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入", "bbox": [245, 308, 817, 333]},
	{"text": "(吸入后漱口，根据动态复查肺功能结果，调整用药)", "bbox": [236, 342, 706, 367]},
	{"text": "抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服", "bbox": [123, 375, 815, 400]},
	{"text": "止咳祛痰：润肺膏 每次15g 每天2次，口服", "bbox": [144, 408, 814, 433]},
	{"text": "调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服", "bbox": [114, 442, 813, 467]},
	{"text": "(5) 如有不适，随时医院就诊，我科随诊。", "bbox": [145, 475, 517, 498]},
	{"text": "科室电话：0745-2329117 主管医师电话：13789357317", "bbox": [114, 507, 680, 529]},
	{"text": "医师签名：主治医师：", "bbox": [539, 530, 791, 560]}
]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord API: raw_items=15, valid_items=15, elapsed=7.4s
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[114, 117, 187, 140]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[1]: text=性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：, bbox=[250, 117, 871, 140]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[2]: text=220999152, bbox=[114, 140, 207, 159]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[3]: text=(2) 3月后返院复查肺功能、呼出气一氧化氮评估病情，每年复查胸部CT评估肺结节变化；, bbox=[145, 172, 940, 197]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[4]: text=(3) 哮喘控制稳定期，腹胀无缓解，建议消化内科就诊，进一步完善胃镜检查；, bbox=[145, 206, 848, 231]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[5]: text=(4) 继续用药：, bbox=[145, 240, 275, 264]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[6]: text=舒张支气管：复方甲氧那明胶囊 每次2粒 每天3次，口服, bbox=[124, 274, 818, 299]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[7]: text=布地奈德福莫特罗吸入粉雾剂 每次320ug（1包）每天1次，吸入, bbox=[245, 308, 817, 333]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[8]: text=(吸入后漱口，根据动态复查肺功能结果，调整用药), bbox=[236, 342, 706, 367]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[9]: text=抗气道炎症：孟鲁司特钠片 每次10mg（1片） 每晚1次，口服, bbox=[123, 375, 815, 400]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[10]: text=止咳祛痰：润肺膏 每次15g 每天2次，口服, bbox=[144, 408, 814, 433]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[11]: text=调节肠道功能：马来酸曲美布汀片 每次0.1g（1片） 每天3次，口服, bbox=[114, 442, 813, 467]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[12]: text=(5) 如有不适，随时医院就诊，我科随诊。, bbox=[145, 475, 517, 498]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[13]: text=科室电话：0745-2329117 主管医师电话：13789357317, bbox=[114, 507, 680, 529]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] coord item[14]: text=医师签名：主治医师：, bbox=[539, 530, 791, 560]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] page=10 — 15/15 coords, api_time=7.4s
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] new_positions (48):
[[9, 400.792, 468.99399999999997, 10.709999999999999, 23.799999999999997], [9, 163.34799999999998, 340.168, 29.75, 41.055], [9, 163.34799999999998, 340.168, 45.815, 56.525], [9, 163.34799999999998, 251.75799999999998, 61.285, 71.99499999999999], [9, 163.34799999999998, 339.32599999999996, 76.755, 87.46499999999999], [9, 163.34799999999998, 458.048, 92.225, 103.53], [9, 163.34799999999998, 685.3879999999999, 107.1, 119.0], [9, 163.34799999999998, 692.124, 123.16499999999999, 134.47], [9, 163.34799999999998, 699.702, 138.635, 150.535], [9, 163.34799999999998, 671.074, 154.7, 166.005], [9, 163.34799999999998, 665.18, 170.17, 181.475], [9, 163.34799999999998, 698.018, 186.23499999999999, 197.54], [9, 163.34799999999998, 690.4399999999999, 201.70499999999998, 213.605], [9, 163.34799999999998, 690.4399999999999, 217.76999999999998, 229.075], [9, 163.34799999999998, 670.232, 233.23999999999998, 244.545], [9, 163.34799999999998, 689.598, 248.70999999999998, 260.61], [9, 163.34799999999998, 687.072, 264.775, 276.08], [9, 163.34799999999998, 694.65, 280.245, 291.55], [9, 163.34799999999998, 700.544, 295.715, 307.615], [9, 163.34799999999998, 685.3879999999999, 311.78, 323.085], [9, 163.34799999999998, 686.23, 327.25, 338.555], [9, 163.34799999999998, 685.3879999999999, 342.71999999999997, 354.025], [9, 163.34799999999998, 691.2819999999999, 358.19, 370.09], [9, 163.34799999999998, 526.25, 374.255, 385.56], [9, 163.34799999999998, 690.4399999999999, 389.72499999999997, 401.03], [9, 163.34799999999998, 635.7099999999999, 405.195, 415.905], [9, 163.34799999999998, 683.704, 420.66499999999996, 431.96999999999997], [9, 163.34799999999998, 637.394, 436.135, 447.44], [9, 163.34799999999998, 686.23, 451.60499999999996, 462.90999999999997], [9, 163.34799999999998, 392.372, 467.075, 478.38], [9, 163.34799999999998, 218.92, 482.54499999999996, 493.255], [9, 187.766, 686.23, 498.015, 508.72499999999997], [9, 163.34799999999998, 297.226, 512.89, 523.6], [10, 95.988, 157.454, 69.615, 83.3], [10, 210.5, 733.382, 69.615, 83.3], [10, 95.988, 174.29399999999998, 83.3, 94.60499999999999], [10, 122.08999999999999, 791.48, 102.33999999999999, 117.21499999999999], [10, 122.08999999999999, 714.016, 122.57, 137.445], [10, 122.08999999999999, 231.54999999999998, 142.79999999999998, 157.07999999999998], [10, 104.408, 688.756, 163.03, 177.905], [10, 206.29, 687.914, 183.26, 198.135], [10, 198.712, 594.452, 203.48999999999998, 218.36499999999998], [10, 103.566, 686.23, 223.125, 238.0], [10, 121.24799999999999, 685.3879999999999, 242.76, 257.635], [10, 95.988, 684.5459999999999, 262.99, 277.865], [10, 122.08999999999999, 435.31399999999996, 282.625, 296.31], [10, 95.988, 572.56, 301.66499999999996, 314.755], [10, 453.83799999999997, 666.0219999999999, 315.34999999999997, 333.2]]
2026-08-05 05:48:50,272 INFO     29 [qwen-vl-text] ═══ DONE ═══ 48 positions, pages=2, time=46.2s
2026-08-05 05:48:50,285 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 05:48:50,286 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Extractor:Discharge | outputs={"chunks": "2 items, types={'DischargeRecord': 2}", "html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:48:50,286 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 05:48:50,286 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:48:50.286+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:48:50,291 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:48:50,292 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-05 05:48:50,292 INFO     29 [qwen-vl-text] positions(54): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:48:50,292 INFO     29 [qwen-vl-text] page grouping: [6, 7, 8], lines per page: [33, 20, 1]
2026-08-05 05:48:50,571 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:48:50,769 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:48:51,029 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:48:51,030 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1981
2026-08-05 05:48:51,030 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:48:51,031 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 136, \"bbox_end\": 189, \"encounter_dates\": [\"2025-07-11\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n出院记录\n入院时间：2025-07-11 08:57\n出院时间：2025-07-22 15:00\n住院天数：11天\n记录时间：2025-07-21 16:14\n入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；\n4.腹胀查因：功能性消化不良？反流性食管炎？其他。\n入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T\n36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面\n容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及\n少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，\n无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，\nLU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功\n能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散\n功能在正常范围；肺总量在正常范围，残气量、残总比增高。\n诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分\n压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中\n性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；\n尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红\n细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；\n电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C\n蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链\nDNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生\n虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：\n胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2.\n支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气\n功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、\nMEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重\n减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳\n性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，\n绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），\n2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：\n怀化市中心医院\nHUAIHUA CENTRAL HOSPITAL\n怀化市肿瘤医院\n姓名：\n性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：\n221028180\n〔心前区无隆起〕，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，〔\n〔各瓣膜听诊区未闻及杂音〕。腹部平坦，〔腹壁静脉无曲张〕，无胃肠型和蠕动波，〔全\n腹柔软〕，〔腹部无压痛〕，〔腹部无反跳痛〕，〔肝脾肋下未扪及〕，Murphy征(-)，叩\n诊呈〔鼓音〕，移动性浊音(-)。肠鸣音正常，〔无气过水声〕。外生殖器〔未查〕，肛门\n直肠〔正常〕。脊柱四肢〔正常〕。 双下肢无浮肿 ，生理反射正常，病理反射阴性。\n辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复\n查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占\n预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量\n在正常范围，残气量、残总比增高。\n入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？\n3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其\n他。\n主治医师：\n副主任医师：\n221028180",
    "role": "user"
  }
]
2026-08-05 05:49:13,207 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:49:13,207 INFO     29 [qwen-vl-text] LLM output (len=3916):
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
2026-08-05 05:49:13,209 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-11]
2026-08-05 05:49:13,213 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1584125, prompt_len=2122
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
2026-08-05 05:49:29,356 INFO     29 [qwen-vl-text] coord API raw response (len=2912):
[
	{"text": "zz1028180", "bbox": [171, 34, 246, 52]},
	{"text": "37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "bbox": [405, 18, 778, 37]},
	{"text": "出院记录", "bbox": [463, 68, 546, 90]},
	{"text": "入院时间：2025-07-11 08:57", "bbox": [170, 99, 387, 117]},
	{"text": "出院时间：2025-07-22 15:00", "bbox": [170, 125, 387, 143]},
	{"text": "住院天数：11天", "bbox": [170, 150, 289, 169]},
	{"text": "记录时间：2025-07-21 16:14", "bbox": [170, 178, 387, 196]},
	{"text": "入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；", "bbox": [186, 204, 835, 224]},
	{"text": "4.腹胀查因：功能性消化不良？反流性食管炎？其他。", "bbox": [170, 231, 559, 250]},
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
2026-08-05 05:49:29,357 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=16.1s
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[0]: text=zz1028180, bbox=[171, 34, 246, 52]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[1]: text=37岁 科室：呼吸与危重症医学科 床号：42 住院号：, bbox=[405, 18, 778, 37]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[2]: text=出院记录, bbox=[463, 68, 546, 90]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[3]: text=入院时间：2025-07-11 08:57, bbox=[170, 99, 387, 117]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[4]: text=出院时间：2025-07-22 15:00, bbox=[170, 125, 387, 143]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[5]: text=住院天数：11天, bbox=[170, 150, 289, 169]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[6]: text=记录时间：2025-07-21 16:14, bbox=[170, 178, 387, 196]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[7]: text=入院诊断：1.支气管哮喘急性发作期；2.肺炎？3.右肺中叶内侧段结节（LU-RADS 2类）；, bbox=[186, 204, 835, 224]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[8]: text=4.腹胀查因：功能性消化不良？反流性食管炎？其他。, bbox=[170, 231, 559, 250]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[9]: text=入院情况：患者女性，37岁，因“反复胸闷、气促8年，加重1月”入院。体格检查：T, bbox=[170, 258, 804, 277]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[10]: text=36.5℃，P70次/分，R24次/分钟，BP139/92mmHg，指脉氧氧饱和度95%（未吸氧），急性面, bbox=[170, 284, 819, 303]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[11]: text=容，神志清晰，精神欠佳，气促貌，球结膜无水肿，颈静脉无充盈，双肺呼吸音清，可闻及, bbox=[170, 311, 827, 330]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[12]: text=少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。心率70次/分，心律齐，无杂音。腹部平软，, bbox=[170, 337, 808, 356]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[13]: text=无压痛及反跳痛。双下肢无浮肿。辅助检查：2025-02-25胸部CT平扫，右肺中叶内侧段结节，, bbox=[170, 364, 834, 383]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[14]: text=LU-RADS 2类，建议年度复查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功, bbox=[170, 390, 827, 409]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[15]: text=能障碍（FEV1 0.99L，占预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散, bbox=[170, 416, 828, 435]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[16]: text=功能在正常范围；肺总量在正常范围，残气量、残总比增高。, bbox=[170, 443, 607, 462]
2026-08-05 05:49:29,358 INFO     29 [qwen-vl-text] coord item[17]: text=诊疗经过：入院后完善相关检查：血气分析：吸氧浓度 20.90 %、pH 7.42，m二氧化碳分, bbox=[186, 470, 828, 489]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[18]: text=压 34.50 mmHg ↓、二氧化碳总量 23.50 mmol/L ↓；血常规：白细胞 5.94×10^9/L、中, bbox=[170, 497, 819, 516]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[19]: text=性粒细胞比率 52.5%、嗜酸性粒细胞比率 8.1%↑、血红蛋白 139g/L、血小板 239×10^9/L；, bbox=[170, 523, 835, 542]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[20]: text=尿常规：白细胞 +--、葡萄糖 +1.00、隐血 +2.00、（镜检）白细胞 0-2 /HP、（镜检）红, bbox=[170, 550, 820, 569]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[21]: text=细胞 + /HP、（镜检）上皮细胞 + /LP；尿沉渣：草酸钙结晶 132个/ul、白细胞 +1.00；, bbox=[170, 576, 810, 595]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[22]: text=电解质：钾 3.48 mmol/L ↓；总IgE 261.95IU/ml；大便常规、肝肾功能、心肌酶、超敏C, bbox=[170, 603, 821, 622]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[23]: text=蛋白、凝血功能、D二聚体、PCT、白介素6、输血前四项、葡萄糖、乳酸、双链DNA、单链, bbox=[170, 629, 813, 648]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[24]: text=DNA、肺炎支原体IgM、肺炎衣原体IgG、过敏源综合14项、新冠肺炎病毒核酸检测、脑寄生, bbox=[170, 656, 820, 675]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[25]: text=虫全套、IgG4、血管炎四项均未见明显异常。心电图：1.窦性心律 2.正常心电图。CT成套：, bbox=[170, 682, 827, 701]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[26]: text=胸部(平扫(三维重建))：1.右肺中叶内侧段结节大致同前，LU-RADS 2类，建议年度复查。2., bbox=[170, 709, 833, 728]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[27]: text=支气管疾患并双肺少许炎性病变，病灶较前稍增多。肺功能常规通气：1.重度混合性肺通气, bbox=[170, 735, 828, 754]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[28]: text=功能障碍（FVC占预计值60.06%，FEV1占预计值36.5%，FEV1/FVC52.34%，MMEF75/25、MEF50、, bbox=[170, 762, 836, 781]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[29]: text=MEF25占预计值的比值分别为10.89%、12.13%、8.6%）；2、最大分钟通气量（MVV）：严重, bbox=[170, 788, 819, 807]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[30]: text=减退（占预计值39.61%）。舒张试验：1.重度混合性肺通气功能障碍，2.支气管舒张试验阳, bbox=[170, 815, 828, 834]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[31]: text=性（1.24h无支气管舒张药物使用史；2.吸入万托林气雾剂400ug15分钟后，FEV1/EVC≥12%，, bbox=[170, 841, 825, 860]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[32]: text=绝对值增加≥200ml）。一口气法弥散功能报告：弥散功能在正常范围（DLCO SB 102.9%），, bbox=[170, 868, 826, 887]
2026-08-05 05:49:29,359 INFO     29 [qwen-vl-text] coord item[33]: text=2.残气量上升、残总比上升 肺总量在正常范围。呼出气一氧化氮，FeNO50：20ppd，CaNO：, bbox=[170, 894, 820, 913]
2026-08-05 05:49:29,360 INFO     29 [qwen-vl-text] page=6 — 33/33 coords, api_time=16.1s
2026-08-05 05:49:29,363 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=921584, prompt_len=1233
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["怀化市中心医院", "HUAIHUA CENTRAL HOSPITAL", "怀化市肿瘤医院", "姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "221028180", "〔心前区无隆起〕，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，〔", "〔各瓣膜听诊区未闻及杂音〕。腹部平坦，〔腹壁静脉无曲张〕，无胃肠型和蠕动波，〔全", "腹柔软〕，〔腹部无压痛〕，〔腹部无反跳痛〕，〔肝脾肋下未扪及〕，Murphy征(-)，叩", "诊呈〔鼓音〕，移动性浊音(-)。肠鸣音正常，〔无气过水声〕。外生殖器〔未查〕，肛门", "直肠〔正常〕。脊柱四肢〔正常〕。 双下肢无浮肿 ，生理反射正常，病理反射阴性。", "辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复", "查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占", "预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量", "在正常范围，残气量、残总比增高。", "入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？", "3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其", "他。", "主治医师：", "副主任医师："]

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
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord API raw response (len=1437):
[
	{"text": "怀化市中心医院", "bbox": [248, 50, 438, 70]},
	{"text": "HUAIHUA CENTRAL HOSPITAL", "bbox": [248, 70, 438, 80]},
	{"text": "怀化市肿瘤医院", "bbox": [248, 84, 438, 98]},
	{"text": "姓名：", "bbox": [141, 127, 190, 147]},
	{"text": "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：", "bbox": [260, 127, 798, 147]},
	{"text": "221028180", "bbox": [141, 147, 222, 163]},
	{"text": "〔心前区无隆起〕，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，〔", "bbox": [145, 175, 855, 196]},
	{"text": "〔各瓣膜听诊区未闻及杂音〕。腹部平坦，〔腹壁静脉无曲张〕，无胃肠型和蠕动波，〔全", "bbox": [145, 204, 846, 225]},
	{"text": "腹柔软〕，〔腹部无压痛〕，〔腹部无反跳痛〕，〔肝脾肋下未扪及〕，Murphy征(-)，叩", "bbox": [141, 234, 846, 255]},
	{"text": "诊呈〔鼓音〕，移动性浊音(-)。肠鸣音正常，〔无气过水声〕。外生殖器〔未查〕，肛门", "bbox": [141, 264, 846, 285]},
	{"text": "直肠〔正常〕。脊柱四肢〔正常〕。 双下肢无浮肿 ，生理反射正常，病理反射阴性。", "bbox": [141, 294, 830, 315]},
	{"text": "辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复", "bbox": [141, 324, 848, 345]},
	{"text": "查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占", "bbox": [141, 354, 848, 375]},
	{"text": "预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量", "bbox": [141, 383, 855, 404]},
	{"text": "在正常范围，残气量、残总比增高。", "bbox": [141, 413, 420, 434]},
	{"text": "入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？", "bbox": [453, 443, 855, 464]},
	{"text": "3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其", "bbox": [141, 472, 860, 493]},
	{"text": "他。", "bbox": [141, 502, 167, 521]},
	{"text": "主治医师：", "bbox": [584, 530, 665, 551]},
	{"text": "副主任医师：", "bbox": [580, 560, 690, 580]}
]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=8.1s
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[0]: text=怀化市中心医院, bbox=[248, 50, 438, 70]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[1]: text=HUAIHUA CENTRAL HOSPITAL, bbox=[248, 70, 438, 80]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[2]: text=怀化市肿瘤医院, bbox=[248, 84, 438, 98]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[141, 127, 190, 147]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：42 住院号：, bbox=[260, 127, 798, 147]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[5]: text=221028180, bbox=[141, 147, 222, 163]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[6]: text=〔心前区无隆起〕，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，〔, bbox=[145, 175, 855, 196]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[7]: text=〔各瓣膜听诊区未闻及杂音〕。腹部平坦，〔腹壁静脉无曲张〕，无胃肠型和蠕动波，〔全, bbox=[145, 204, 846, 225]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[8]: text=腹柔软〕，〔腹部无压痛〕，〔腹部无反跳痛〕，〔肝脾肋下未扪及〕，Murphy征(-)，叩, bbox=[141, 234, 846, 255]
2026-08-05 05:49:37,511 INFO     29 [qwen-vl-text] coord item[9]: text=诊呈〔鼓音〕，移动性浊音(-)。肠鸣音正常，〔无气过水声〕。外生殖器〔未查〕，肛门, bbox=[141, 264, 846, 285]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[10]: text=直肠〔正常〕。脊柱四肢〔正常〕。 双下肢无浮肿 ，生理反射正常，病理反射阴性。, bbox=[141, 294, 830, 315]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[11]: text=辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复, bbox=[141, 324, 848, 345]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[12]: text=查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占, bbox=[141, 354, 848, 375]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[13]: text=预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量, bbox=[141, 383, 855, 404]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[14]: text=在正常范围，残气量、残总比增高。, bbox=[141, 413, 420, 434]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[15]: text=入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？, bbox=[453, 443, 855, 464]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[16]: text=3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其, bbox=[141, 472, 860, 493]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[17]: text=他。, bbox=[141, 502, 167, 521]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[18]: text=主治医师：, bbox=[584, 530, 665, 551]
2026-08-05 05:49:37,512 INFO     29 [qwen-vl-text] coord item[19]: text=副主任医师：, bbox=[580, 560, 690, 580]
2026-08-05 05:49:37,513 INFO     29 [qwen-vl-text] page=7 — 20/20 coords, api_time=8.1s
2026-08-05 05:49:37,518 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1474463, prompt_len=624
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["221028180"]

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
2026-08-05 05:49:38,930 INFO     29 [qwen-vl-text] coord API raw response (len=66):
```json
[
	{"text": "221028180", "bbox": [186, 17, 258, 32]}
]
```
2026-08-05 05:49:38,931 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.4s
2026-08-05 05:49:38,931 INFO     29 [qwen-vl-text] coord item[0]: text=221028180, bbox=[186, 17, 258, 32]
2026-08-05 05:49:38,932 INFO     29 [qwen-vl-text] page=8 — 1/1 coords, api_time=1.4s
2026-08-05 05:49:38,933 INFO     29 [qwen-vl-text] new_positions (54):
[[6, 143.982, 207.132, 20.23, 30.939999999999998], [6, 341.01, 655.076, 10.709999999999999, 22.015], [6, 389.846, 459.73199999999997, 40.46, 53.55], [6, 143.14, 325.854, 58.904999999999994, 69.615], [6, 143.14, 325.854, 74.375, 85.085], [6, 143.14, 243.338, 89.25, 100.55499999999999], [6, 143.14, 325.854, 105.91, 116.61999999999999], [6, 156.612, 703.0699999999999, 121.38, 133.28], [6, 143.14, 470.678, 137.445, 148.75], [6, 143.14, 676.968, 153.51, 164.815], [6, 143.14, 689.598, 168.98, 180.285], [6, 143.14, 696.334, 185.045, 196.35], [6, 143.14, 680.336, 200.515, 211.82], [6, 143.14, 702.228, 216.57999999999998, 227.885], [6, 143.14, 696.334, 232.04999999999998, 243.355], [6, 143.14, 697.1759999999999, 247.51999999999998, 258.825], [6, 143.14, 511.094, 263.585, 274.89], [6, 156.612, 697.1759999999999, 279.65, 290.955], [6, 143.14, 689.598, 295.715, 307.02], [6, 143.14, 703.0699999999999, 311.185, 322.49], [6, 143.14, 690.4399999999999, 327.25, 338.555], [6, 143.14, 682.02, 342.71999999999997, 354.025], [6, 143.14, 691.2819999999999, 358.78499999999997, 370.09], [6, 143.14, 684.5459999999999, 374.255, 385.56], [6, 143.14, 690.4399999999999, 390.32, 401.625], [6, 143.14, 696.334, 405.78999999999996, 417.09499999999997], [6, 143.14, 701.386, 421.85499999999996, 433.15999999999997], [6, 143.14, 697.1759999999999, 437.325, 448.63], [6, 143.14, 703.9119999999999, 453.39, 464.695], [6, 143.14, 689.598, 468.85999999999996, 480.16499999999996], [6, 143.14, 697.1759999999999, 484.92499999999995, 496.22999999999996], [6, 143.14, 694.65, 500.395, 511.7], [6, 143.14, 695.492, 516.4599999999999, 527.765], [7, 208.816, 368.796, 29.75, 41.65], [7, 208.816, 368.796, 41.65, 47.599999999999994], [7, 208.816, 368.796, 49.98, 58.309999999999995], [7, 118.722, 159.98, 75.565, 87.46499999999999], [7, 218.92, 671.9159999999999, 75.565, 87.46499999999999], [7, 118.722, 186.924, 87.46499999999999, 96.985], [7, 122.08999999999999, 719.91, 104.125, 116.61999999999999], [7, 122.08999999999999, 712.332, 121.38, 133.875], [7, 118.722, 712.332, 139.23, 151.725], [7, 118.722, 712.332, 157.07999999999998, 169.575], [7, 118.722, 698.86, 174.92999999999998, 187.42499999999998], [7, 118.722, 714.016, 192.78, 205.27499999999998], [7, 118.722, 714.016, 210.63, 223.125], [7, 118.722, 719.91, 227.885, 240.38], [7, 118.722, 353.64, 245.73499999999999, 258.22999999999996], [7, 381.426, 719.91, 263.585, 276.08], [7, 118.722, 724.12, 280.84, 293.335], [7, 118.722, 140.614, 298.69, 309.995], [7, 491.728, 559.93, 315.34999999999997, 327.84499999999997], [7, 488.35999999999996, 580.98, 333.2, 345.09999999999997], [8, 156.612, 217.236, 10.115, 19.04]]
2026-08-05 05:49:38,933 INFO     29 [qwen-vl-text] ═══ DONE ═══ 54 positions, pages=3, time=48.6s
2026-08-05 05:49:38,933 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:49:38,934 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-05 05:49:38,934 INFO     29 [qwen-vl-text] positions(21): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:49:38,934 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [21]
2026-08-05 05:49:39,202 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:49:39,203 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1072
2026-08-05 05:49:39,203 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:49:39,204 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 190, \"bbox_end\": 210, \"encounter_dates\": [\"2025-07-11\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "第2次入院记录\n姓名：\n出生地：贵州省天柱县\n性别：女\n民族：苗族\n年龄：37岁\n职业：农民\n婚姻：已婚\n住址：贵州省天柱县远口镇大祥村白蜡树脚组\n入院时间：2025-07-11 08:57\n记录时间：2025-07-11 14:36\n入院方式：步行\n主诉：反复胸闷、气促8年，加重1月。\n现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。\n出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。\n既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。\n病史陈述者签名：\n体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。\n眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，\n甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。\n叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。",
    "role": "user"
  }
]
2026-08-05 05:49:39,209 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:49:39.208+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:49:48,735 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:49:48,735 INFO     29 [qwen-vl-text] LLM output (len=1942):
{
  "encounter_date": "2025-07-11",
  "dm_name": null,
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
  "fh_text": null,
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 70,
  "vs_respiration_rpm": 24,
  "vs_systolic_bp_mmhg": 139,
  "vs_diastolic_bp_mmhg": 92,
  "pe_general_condition": "发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。",
  "pe_skin_mucosa": "全身皮肤黏膜色泽正常，无肝掌。无蜘蛛痣。",
  "pe_lymph_nodes": "全身浅表淋巴结未触及肿大。",
  "pe_lungs": "胸廓无畸形、双侧对称，呼吸动度两侧一致，无胸膜摩擦感。叩诊呈清音，双肺呼吸音粗，可闻及少许湿啰音及弥漫性哮鸣音，无胸膜摩擦音。",
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
      "name": "支气管哮喘急性发作期",
      "diagnosis_type": "西医",
      "is_primary": true
    }
  ],
  "department": "呼吸与危重症医学科"
}
2026-08-05 05:49:48,735 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-11]
2026-08-05 05:49:48,742 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1474463, prompt_len=1748
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["第2次入院记录", "姓名：", "出生地：贵州省天柱县", "性别：女", "民族：苗族", "年龄：37岁", "职业：农民", "婚姻：已婚", "住址：贵州省天柱县远口镇大祥村白蜡树脚组", "入院时间：2025-07-11 08:57", "记录时间：2025-07-11 14:36", "入院方式：步行", "主诉：反复胸闷、气促8年，加重1月。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "病史陈述者签名：", "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。", "眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，", "甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。", "叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。"]

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
2026-08-05 05:50:02,222 INFO     29 [qwen-vl-text] coord API raw response (len=1995):
[
	{"text": "第2次入院记录", "bbox": [439, 46, 568, 67]},
	{"text": "姓名：", "bbox": [184, 84, 235, 104]},
	{"text": "出生地：贵州省天柱县", "bbox": [455, 85, 613, 104]},
	{"text": "性别：女", "bbox": [184, 112, 250, 131]},
	{"text": "民族：苗族", "bbox": [455, 112, 535, 131]},
	{"text": "年龄：37岁", "bbox": [184, 138, 264, 157]},
	{"text": "职业：农民", "bbox": [455, 138, 535, 157]},
	{"text": "婚姻：已婚", "bbox": [184, 165, 266, 184]},
	{"text": "住址：贵州省天柱县远口镇大祥村白蜡树脚组", "bbox": [455, 165, 768, 184]},
	{"text": "入院时间：2025-07-11 08:57", "bbox": [184, 191, 392, 210]},
	{"text": "记录时间：2025-07-11 14:36", "bbox": [455, 191, 662, 210]},
	{"text": "入院方式：步行", "bbox": [184, 217, 298, 236]},
	{"text": "主诉：反复胸闷、气促8年，加重1月。", "bbox": [184, 243, 450, 262]},
	{"text": "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "bbox": [184, 270, 813, 471]},
	{"text": "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "bbox": [184, 479, 817, 630]},
	{"text": "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "bbox": [184, 637, 634, 656]},
	{"text": "病史陈述者签名：", "bbox": [184, 664, 303, 683]},
	{"text": "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。", "bbox": [184, 690, 817, 760]},
	{"text": "眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，", "bbox": [184, 767, 811, 840]},
	{"text": "甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。", "bbox": [193, 847, 798, 867]},
	{"text": "叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。", "bbox": [184, 873, 804, 893]}
]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=13.5s
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[0]: text=第2次入院记录, bbox=[439, 46, 568, 67]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[184, 84, 235, 104]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[2]: text=出生地：贵州省天柱县, bbox=[455, 85, 613, 104]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[184, 112, 250, 131]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[4]: text=民族：苗族, bbox=[455, 112, 535, 131]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：37岁, bbox=[184, 138, 264, 157]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[6]: text=职业：农民, bbox=[455, 138, 535, 157]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻：已婚, bbox=[184, 165, 266, 184]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[8]: text=住址：贵州省天柱县远口镇大祥村白蜡树脚组, bbox=[455, 165, 768, 184]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[9]: text=入院时间：2025-07-11 08:57, bbox=[184, 191, 392, 210]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[10]: text=记录时间：2025-07-11 14:36, bbox=[455, 191, 662, 210]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[11]: text=入院方式：步行, bbox=[184, 217, 298, 236]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[12]: text=主诉：反复胸闷、气促8年，加重1月。, bbox=[184, 243, 450, 262]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[13]: text=现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。, bbox=[184, 270, 813, 471]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[14]: text=出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。, bbox=[184, 479, 817, 630]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[15]: text=既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。, bbox=[184, 637, 634, 656]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[16]: text=病史陈述者签名：, bbox=[184, 664, 303, 683]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[17]: text=体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。, bbox=[184, 690, 817, 760]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[18]: text=眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，, bbox=[184, 767, 811, 840]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[19]: text=甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。, bbox=[193, 847, 798, 867]
2026-08-05 05:50:02,223 INFO     29 [qwen-vl-text] coord item[20]: text=叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。, bbox=[184, 873, 804, 893]
2026-08-05 05:50:02,224 INFO     29 [qwen-vl-text] page=8 — 21/21 coords, api_time=13.5s
2026-08-05 05:50:02,224 INFO     29 [qwen-vl-text] new_positions (21):
[[8, 369.638, 478.256, 27.369999999999997, 39.864999999999995], [8, 154.928, 197.87, 49.98, 61.879999999999995], [8, 383.11, 516.146, 50.574999999999996, 61.879999999999995], [8, 154.928, 210.5, 66.64, 77.945], [8, 383.11, 450.46999999999997, 66.64, 77.945], [8, 154.928, 222.28799999999998, 82.11, 93.41499999999999], [8, 383.11, 450.46999999999997, 82.11, 93.41499999999999], [8, 154.928, 223.97199999999998, 98.175, 109.47999999999999], [8, 383.11, 646.656, 98.175, 109.47999999999999], [8, 154.928, 330.06399999999996, 113.645, 124.94999999999999], [8, 383.11, 557.404, 113.645, 124.94999999999999], [8, 154.928, 250.916, 129.11499999999998, 140.42], [8, 154.928, 378.9, 144.58499999999998, 155.89], [8, 154.928, 684.5459999999999, 160.65, 280.245], [8, 154.928, 687.914, 285.005, 374.84999999999997], [8, 154.928, 533.828, 379.015, 390.32], [8, 154.928, 255.126, 395.08, 406.385], [8, 154.928, 687.914, 410.54999999999995, 452.2], [8, 154.928, 682.862, 456.36499999999995, 499.79999999999995], [8, 162.506, 671.9159999999999, 503.965, 515.865], [8, 154.928, 676.968, 519.435, 531.3349999999999]]
2026-08-05 05:50:02,224 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=23.3s
2026-08-05 05:50:02,224 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:50:02,224 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-05 05:50:02,224 INFO     29 [qwen-vl-text] positions(31): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:50:02,224 INFO     29 [qwen-vl-text] page grouping: [11, 12], lines per page: [21, 10]
2026-08-05 05:50:02,481 INFO     29 [qwen-vl-text] page=11, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:50:02,701 INFO     29 [qwen-vl-text] page=12, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:50:02,702 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1702
2026-08-05 05:50:02,703 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:50:02,703 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 259, \"bbox_end\": 289, \"encounter_dates\": [\"2025-07-11\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "221028180\n第2次入院记录\n姓名：\n性别：女\n年龄：37岁\n婚姻：已婚\n入院时间：2025-07-11 08:57\n入院方式：步行\n主诉：反复胸闷、气促8年，加重1月。\n现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。\n出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。\n既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。\n病史陈述者签名：\n体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。\n出生地：贵州省天柱县\n民族：苗族\n职业：农民\n住址：贵\n记录时间：2025-07-11 14:36\nCS 扫描全能王\n3亿人都在用的扫描App\n家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。\n病史陈述者签名：\n体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋\n姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n220999152\n下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:\n辅助检查结果：无\n入院初步诊断：胸闷、气促查因：支气管哮喘可能性大\n主治医师：\n主任医师：",
    "role": "user"
  }
]
2026-08-05 05:50:12,064 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:50:12.063+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:50:12,646 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:50:12,646 INFO     29 [qwen-vl-text] LLM output (len=2123):
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
      "diagnosis_type": "初步",
      "is_primary": true
    }
  ],
  "department": "呼吸与危重症医学科"
}
2026-08-05 05:50:12,646 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-11]
2026-08-05 05:50:12,649 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1451457, prompt_len=1761
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["221028180", "第2次入院记录", "姓名：", "性别：女", "年龄：37岁", "婚姻：已婚", "入院时间：2025-07-11 08:57", "入院方式：步行", "主诉：反复胸闷、气促8年，加重1月。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "病史陈述者签名：", "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。", "出生地：贵州省天柱县", "民族：苗族", "职业：农民", "住址：贵", "记录时间：2025-07-11 14:36", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:50:23,754 INFO     29 [qwen-vl-text] coord API raw response (len=2006):
[
	{"text": "221028180", "bbox": [186, 17, 258, 32]},
	{"text": "第2次入院记录", "bbox": [439, 47, 568, 67]},
	{"text": "姓名：", "bbox": [185, 85, 245, 105]},
	{"text": "性别：女", "bbox": [185, 113, 249, 132]},
	{"text": "年龄：37岁", "bbox": [185, 139, 263, 158]},
	{"text": "婚姻：已婚", "bbox": [185, 165, 266, 184]},
	{"text": "入院时间：2025-07-11 08:57", "bbox": [185, 192, 391, 210]},
	{"text": "入院方式：步行", "bbox": [185, 218, 298, 237]},
	{"text": "主诉：反复胸闷、气促8年，加重1月。", "bbox": [185, 244, 447, 263]},
	{"text": "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。", "bbox": [185, 270, 813, 471]},
	{"text": "出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。", "bbox": [185, 479, 815, 630]},
	{"text": "既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。", "bbox": [185, 637, 633, 656]},
	{"text": "病史陈述者签名：", "bbox": [185, 664, 303, 683]},
	{"text": "体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。", "bbox": [185, 690, 817, 894]},
	{"text": "出生地：贵州省天柱县", "bbox": [454, 85, 613, 105]},
	{"text": "民族：苗族", "bbox": [454, 113, 535, 132]},
	{"text": "职业：农民", "bbox": [454, 139, 535, 158]},
	{"text": "住址：贵", "bbox": [454, 165, 515, 184]},
	{"text": "记录时间：2025-07-11 14:36", "bbox": [454, 192, 662, 210]},
	{"text": "CS 扫描全能王", "bbox": [903, 942, 983, 963]},
	{"text": "3亿人都在用的扫描App", "bbox": [903, 970, 983, 981]}
]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=11.1s
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[0]: text=221028180, bbox=[186, 17, 258, 32]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[1]: text=第2次入院记录, bbox=[439, 47, 568, 67]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[185, 85, 245, 105]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[185, 113, 249, 132]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：37岁, bbox=[185, 139, 263, 158]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[5]: text=婚姻：已婚, bbox=[185, 165, 266, 184]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[6]: text=入院时间：2025-07-11 08:57, bbox=[185, 192, 391, 210]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[7]: text=入院方式：步行, bbox=[185, 218, 298, 237]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：反复胸闷、气促8年，加重1月。, bbox=[185, 244, 447, 263]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。2025年01月上述症状加重，每晚夜间可闻及喉鸣音，急性发作频率明显增加，约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，遂于2025.02.24-03.01日第一次我科住院治疗，完善相关检查后，诊断为“1.支气管哮喘急性发作期；2.右肺中叶内侧段结节，LU-RADS 2类；3.腹胀查因：功能性消化不良？反流性食管炎？其他”，治疗上予以甲泼尼龙静滴、布地奈德抗炎、平喘、舒张支气管、止咳化痰、护胃、促进胃肠动力、调节胃肠功能、补液等处理后，病情好转出院。, bbox=[185, 270, 813, 471]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[10]: text=出院后序贯并规律予以布地奈德福莫特罗吸入粉雾剂每次320ug BID吸入控制症状，病情尚稳定。1月前患者自觉受凉后出现上症加重，感胸闷不适，喘息气促明显，夜间及活动后为甚，平步慢走约200米即气喘明显，伴喉鸣音，咳嗽咳痰，痰量较平日增多，咳白色粘痰，无胸痛咯血，无畏寒发热，吸入信必可（都宝）、沙丁胺醇气雾剂（万托林）效果不佳，今为求进一步诊治，遂来我院门诊就诊，门诊以“支气管哮喘急性发作期”收入我科。患者自起病以来，睡眠、精神、食欲欠佳，大小便正常，体重未见明显改变。, bbox=[185, 479, 815, 630]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[11]: text=既往史、个人史、月经史、婚育史、家族史：见第一次入院记录。, bbox=[185, 637, 633, 656]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[12]: text=病史陈述者签名：, bbox=[185, 664, 303, 683]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查：T36.5℃，P70次/分，R24次/分钟，血压139/92mmHg，指脉氧氧饱和度：95%（未吸氧）。发育正常，营养良好，神志清醒，精神欠佳，急性面容，气促貌，自动体位，平车推入病房。全身皮肤黏膜色泽正常，无肝掌。 无蜘蛛痣 ， 全身浅表淋巴结未触及肿大。眼睑无浮肿，球结膜无水肿，巩膜 无黄染 ，双侧瞳孔 等大同圆，直径约2.5mm ，对光反射 灵敏 。 无鼻分泌物 ，外耳道 无异常分泌物 ，咽部 无充血 ， 扁桃体无肿大 ， 口唇无发绀 。颈软，气管 居中 ，颈静脉无充盈，肝-颈静脉回流征阴性，甲状腺无肿大 。胸廓无畸形、双侧对称，呼吸动度 两侧一致 ， 无胸膜摩擦感 。叩诊呈清音， 双肺呼吸音粗 ，可闻及少许湿啰音及弥漫性哮鸣音， 无胸膜摩擦音 。, bbox=[185, 690, 817, 894]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[14]: text=出生地：贵州省天柱县, bbox=[454, 85, 613, 105]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[15]: text=民族：苗族, bbox=[454, 113, 535, 132]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[16]: text=职业：农民, bbox=[454, 139, 535, 158]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[17]: text=住址：贵, bbox=[454, 165, 515, 184]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[18]: text=记录时间：2025-07-11 14:36, bbox=[454, 192, 662, 210]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[19]: text=CS 扫描全能王, bbox=[903, 942, 983, 963]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] coord item[20]: text=3亿人都在用的扫描App, bbox=[903, 970, 983, 981]
2026-08-05 05:50:23,755 INFO     29 [qwen-vl-text] page=11 — 21/21 coords, api_time=11.1s
2026-08-05 05:50:23,757 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1064952, prompt_len=1259
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
2026-08-05 05:50:33,114 INFO     29 [qwen-vl-text] coord API raw response (len=1054):
[
	{"text": "家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。", "bbox": [145, 27, 668, 50]},
	{"text": "病史陈述者签名：", "bbox": [145, 57, 277, 79]},
	{"text": "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋", "bbox": [145, 86, 853, 339]},
	{"text": "姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "bbox": [147, 574, 798, 595]},
	{"text": "220999152", "bbox": [147, 594, 228, 610]},
	{"text": "下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:", "bbox": [147, 620, 853, 697]},
	{"text": "辅助检查结果：无", "bbox": [147, 706, 290, 726]},
	{"text": "入院初步诊断：胸闷、气促查因：支气管哮喘可能性大", "bbox": [433, 734, 853, 754]},
	{"text": "主治医师：", "bbox": [649, 763, 772, 783]},
	{"text": "主任医师：", "bbox": [649, 791, 814, 811]}
]
2026-08-05 05:50:33,114 INFO     29 [qwen-vl-text] coord API: raw_items=10, valid_items=10, elapsed=9.4s
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[0]: text=家族史：家族中无同类病人。直系亲属体健。([无遗传倾向疾患])。, bbox=[145, 27, 668, 50]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[1]: text=病史陈述者签名：, bbox=[145, 57, 277, 79]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[2]: text=体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧饱和度：98%（未吸氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软，气管居中，颈静脉无怒张，肝-颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦音。心前区无隆起，无震颤，心率89次/分钟，心律齐，各瓣膜听诊区未闻及杂音。腹部平坦，腹壁静脉无曲张，无胃肠型和蠕动波，全腹柔软，腹部无压痛，腹部无反跳痛，肝脾肋, bbox=[145, 86, 853, 339]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：杨细兰 性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：, bbox=[147, 574, 798, 595]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[4]: text=220999152, bbox=[147, 594, 228, 610]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[5]: text=下未扪及，Murphy征(-)，叩诊呈鼓音，肝区无叩痛，肾区无叩痛，移动性浊音(-)。肠鸣音正常，无气过水声。外生殖器无异常，肛门直肠正常。脊柱四肢正常。生理反射正常，病理反射阴性。双下肢无浮肿。:, bbox=[147, 620, 853, 697]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[6]: text=辅助检查结果：无, bbox=[147, 706, 290, 726]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[7]: text=入院初步诊断：胸闷、气促查因：支气管哮喘可能性大, bbox=[433, 734, 853, 754]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[8]: text=主治医师：, bbox=[649, 763, 772, 783]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] coord item[9]: text=主任医师：, bbox=[649, 791, 814, 811]
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] page=12 — 10/10 coords, api_time=9.4s
2026-08-05 05:50:33,115 INFO     29 [qwen-vl-text] new_positions (31):
[[11, 156.612, 217.236, 10.115, 19.04], [11, 369.638, 478.256, 27.965, 39.864999999999995], [11, 155.76999999999998, 206.29, 50.574999999999996, 62.474999999999994], [11, 155.76999999999998, 209.658, 67.235, 78.53999999999999], [11, 155.76999999999998, 221.446, 82.705, 94.00999999999999], [11, 155.76999999999998, 223.97199999999998, 98.175, 109.47999999999999], [11, 155.76999999999998, 329.222, 114.24, 124.94999999999999], [11, 155.76999999999998, 250.916, 129.71, 141.015], [11, 155.76999999999998, 376.37399999999997, 145.18, 156.48499999999999], [11, 155.76999999999998, 684.5459999999999, 160.65, 280.245], [11, 155.76999999999998, 686.23, 285.005, 374.84999999999997], [11, 155.76999999999998, 532.986, 379.015, 390.32], [11, 155.76999999999998, 255.126, 395.08, 406.385], [11, 155.76999999999998, 687.914, 410.54999999999995, 531.93], [11, 382.268, 516.146, 50.574999999999996, 62.474999999999994], [11, 382.268, 450.46999999999997, 67.235, 78.53999999999999], [11, 382.268, 450.46999999999997, 82.705, 94.00999999999999], [11, 382.268, 433.63, 98.175, 109.47999999999999], [11, 382.268, 557.404, 114.24, 124.94999999999999], [11, 760.326, 827.6859999999999, 560.49, 572.985], [11, 760.326, 827.6859999999999, 577.15, 583.6949999999999], [12, 122.08999999999999, 562.456, 16.064999999999998, 29.75], [12, 122.08999999999999, 233.23399999999998, 33.915, 47.004999999999995], [12, 122.08999999999999, 718.226, 51.169999999999995, 201.70499999999998], [12, 123.774, 671.9159999999999, 341.53, 354.025], [12, 123.774, 191.976, 353.43, 362.95], [12, 123.774, 718.226, 368.9, 414.715], [12, 123.774, 244.17999999999998, 420.07, 431.96999999999997], [12, 364.586, 718.226, 436.72999999999996, 448.63], [12, 546.458, 650.024, 453.98499999999996, 465.885], [12, 546.458, 685.3879999999999, 470.645, 482.54499999999996]]
2026-08-05 05:50:33,116 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=2, time=30.9s
2026-08-05 05:50:33,116 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:50:33,116 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-05 05:50:33,116 INFO     29 [qwen-vl-text] positions(40): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:50:33,116 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [39]
2026-08-05 05:50:33,407 INFO     29 [qwen-vl-text] page=13, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:50:33,408 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1006
2026-08-05 05:50:33,408 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:50:33,408 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 290, \"bbox_end\": 329, \"encounter_dates\": [\"2025-02-24\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "姓名：\n性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：\n220999152\n入院记录\n姓名：\n出生地：贵州省天柱县远口镇大样村白蜡树脚组\n性别：女\n民族：苗族\n年龄：37岁\n职业：自由职业者\n婚姻：已婚\n住址：贵\n入院时间：2025-02-24 12:22\n记录时间：2025-02-24 14:28\n入院方式：步行\n主诉：反复胸闷、气促8年，加重半年。\n现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳\n嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐\n渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，\n无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，\n约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，\n门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期\n体重无改变。\n既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病\n史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。\n个人史：[出生于原籍 ， 常住本地 ， 无粉尘放射性物质接触史 ， 否认疫区居住\n史]，[无吸烟史 ， 无饮酒史 ， 否认性病及治游史 。\n月经史：16 2~3 2025/2/21， 月经周期规律，色红，量少，无痛经。\n29~30\n婚育史：24岁结婚，育有1子1女，配偶及子女体健。\n家族史：家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。\n病史陈述者签名：\n体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸\n氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜\n色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，\n巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常\n分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-\n颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤\n正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦",
    "role": "user"
  }
]
2026-08-05 05:50:41,354 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:50:41,354 INFO     29 [qwen-vl-text] LLM output (len=1795):
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
  "fh_text": "家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。",
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
2026-08-05 05:50:41,354 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-24]
2026-08-05 05:50:41,357 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1493729, prompt_len=1736
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共39行）
["姓名：", "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "220999152", "入院记录", "姓名：", "出生地：贵州省天柱县远口镇大样村白蜡树脚组", "性别：女", "民族：苗族", "年龄：37岁", "职业：自由职业者", "婚姻：已婚", "住址：贵", "入院时间：2025-02-24 12:22", "记录时间：2025-02-24 14:28", "入院方式：步行", "主诉：反复胸闷、气促8年，加重半年。", "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳", "嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐", "渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，", "无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，", "约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，", "门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期", "体重无改变。", "既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病", "史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。", "个人史：[出生于原籍 ， 常住本地 ， 无粉尘放射性物质接触史 ， 否认疫区居住", "史]，[无吸烟史 ， 无饮酒史 ， 否认性病及治游史 。", "月经史：16 2~3 2025/2/21， 月经周期规律，色红，量少，无痛经。", "29~30", "婚育史：24岁结婚，育有1子1女，配偶及子女体健。", "家族史：家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。", "病史陈述者签名：", "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜", "色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，", "巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常", "分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-", "颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤", "正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦"]

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
2026-08-05 05:50:55,496 INFO     29 [qwen-vl-text] coord API raw response (len=2718):
[
	{"text": "姓名：", "bbox": [173, 31, 218, 50]},
	{"text": "性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：", "bbox": [285, 31, 798, 50]},
	{"text": "220999152", "bbox": [173, 50, 250, 67]},
	{"text": "入院记录", "bbox": [477, 87, 547, 105]},
	{"text": "姓名：", "bbox": [173, 126, 218, 145]},
	{"text": "出生地：贵州省天柱县远口镇大样村白蜡树脚组", "bbox": [451, 126, 805, 145]},
	{"text": "性别：女", "bbox": [173, 154, 241, 173]},
	{"text": "民族：苗族", "bbox": [451, 154, 536, 173]},
	{"text": "年龄：37岁", "bbox": [173, 181, 257, 200]},
	{"text": "职业：自由职业者", "bbox": [451, 181, 585, 200]},
	{"text": "婚姻：已婚", "bbox": [173, 208, 257, 227]},
	{"text": "住址：贵", "bbox": [451, 208, 517, 227]},
	{"text": "入院时间：2025-02-24 12:22", "bbox": [173, 236, 394, 255]},
	{"text": "记录时间：2025-02-24 14:28", "bbox": [451, 236, 670, 255]},
	{"text": "入院方式：步行", "bbox": [173, 263, 292, 282]},
	{"text": "主诉：反复胸闷、气促8年，加重半年。", "bbox": [173, 290, 461, 309]},
	{"text": "现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳", "bbox": [173, 317, 837, 337]},
	{"text": "嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐", "bbox": [173, 345, 844, 364]},
	{"text": "渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，", "bbox": [173, 372, 833, 391]},
	{"text": "无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，", "bbox": [173, 399, 833, 418]},
	{"text": "约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，", "bbox": [173, 426, 850, 445]},
	{"text": "门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期", "bbox": [173, 453, 844, 472]},
	{"text": "体重无改变。", "bbox": [173, 480, 274, 499]},
	{"text": "既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病", "bbox": [173, 507, 844, 527]},
	{"text": "史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。", "bbox": [173, 535, 753, 554]},
	{"text": "个人史：[出生于原籍 ， 常住本地 ， 无粉尘放射性物质接触史 ， 否认疫区居住", "bbox": [173, 562, 845, 581]},
	{"text": "史]，[无吸烟史 ， 无饮酒史 ， 否认性病及治游史 。", "bbox": [173, 589, 636, 608]},
	{"text": "月经史：16 2~3 2025/2/21， 月经周期规律，色红，量少，无痛经。", "bbox": [173, 616, 676, 635]},
	{"text": "29~30", "bbox": [252, 612, 362, 630]},
	{"text": "婚育史：24岁结婚，育有1子1女，配偶及子女体健。", "bbox": [173, 644, 553, 663]},
	{"text": "家族史：家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。", "bbox": [173, 671, 671, 690]},
	{"text": "病史陈述者签名：", "bbox": [173, 698, 299, 717]},
	{"text": "体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸", "bbox": [173, 725, 845, 744]},
	{"text": "氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜", "bbox": [173, 752, 845, 771]},
	{"text": "色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，", "bbox": [173, 779, 835, 798]},
	{"text": "巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常", "bbox": [173, 806, 836, 825]},
	{"text": "分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-", "bbox": [173, 833, 836, 852]},
	{"text": "颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤", "bbox": [173, 860, 845, 879]},
	{"text": "正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦", "bbox": [173, 887, 845, 906]}
]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord API: raw_items=39, valid_items=39, elapsed=14.1s
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[173, 31, 218, 50]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[1]: text=性别：女 年龄：37岁 科室：呼吸与危重症医学科 床号：46 住院号：, bbox=[285, 31, 798, 50]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[2]: text=220999152, bbox=[173, 50, 250, 67]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[3]: text=入院记录, bbox=[477, 87, 547, 105]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[173, 126, 218, 145]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[5]: text=出生地：贵州省天柱县远口镇大样村白蜡树脚组, bbox=[451, 126, 805, 145]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女, bbox=[173, 154, 241, 173]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[7]: text=民族：苗族, bbox=[451, 154, 536, 173]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：37岁, bbox=[173, 181, 257, 200]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[9]: text=职业：自由职业者, bbox=[451, 181, 585, 200]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[10]: text=婚姻：已婚, bbox=[173, 208, 257, 227]
2026-08-05 05:50:55,497 INFO     29 [qwen-vl-text] coord item[11]: text=住址：贵, bbox=[451, 208, 517, 227]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[12]: text=入院时间：2025-02-24 12:22, bbox=[173, 236, 394, 255]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[13]: text=记录时间：2025-02-24 14:28, bbox=[451, 236, 670, 255]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[14]: text=入院方式：步行, bbox=[173, 263, 292, 282]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：反复胸闷、气促8年，加重半年。, bbox=[173, 290, 461, 309]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：患者自诉8年余前开始反复出现胸闷、气促，夜间及清晨时明显，伴喉鸣，偶有咳, bbox=[173, 317, 837, 337]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[17]: text=嗽，少许白色泡沫痰，吸入油烟等刺激后咳嗽、喘息加重，未系统诊治。半年前上述症状逐, bbox=[173, 345, 844, 364]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[18]: text=渐加重，夜间平卧后尤甚，每晚夜间可闻及喉鸣音，无端坐呼吸、夜间憋醒，无畏寒发热，, bbox=[173, 372, 833, 391]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[19]: text=无胸闷胸痛心悸，无恶心呕吐，无头痛头晕，无黑朦晕厥等不适，急性发作频率明显增加，, bbox=[173, 399, 833, 418]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[20]: text=约每1-2周急性发作1次，反复在诊所输液治疗可暂时缓解正常，但易反复，现为诊治来我院，, bbox=[173, 426, 850, 445]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[21]: text=门诊以“支气管哮喘”收入我科，自起病以来，患者精神食欲睡眠一般，大小便正常，近期, bbox=[173, 453, 844, 472]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[22]: text=体重无改变。, bbox=[173, 480, 274, 499]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[23]: text=既往史：平素身体一般。否认高血压病、糖尿病、心脏病病史。否认肝炎、结核等传染病病, bbox=[173, 507, 844, 527]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[24]: text=史，预防接种史不详。无手术史。无外伤史。无输血史。无食物、药物过敏史。, bbox=[173, 535, 753, 554]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[25]: text=个人史：[出生于原籍 ， 常住本地 ， 无粉尘放射性物质接触史 ， 否认疫区居住, bbox=[173, 562, 845, 581]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[26]: text=史]，[无吸烟史 ， 无饮酒史 ， 否认性病及治游史 。, bbox=[173, 589, 636, 608]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[27]: text=月经史：16 2~3 2025/2/21， 月经周期规律，色红，量少，无痛经。, bbox=[173, 616, 676, 635]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[28]: text=29~30, bbox=[252, 612, 362, 630]
2026-08-05 05:50:55,498 INFO     29 [qwen-vl-text] coord item[29]: text=婚育史：24岁结婚，育有1子1女，配偶及子女体健。, bbox=[173, 644, 553, 663]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[30]: text=家族史：家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。, bbox=[173, 671, 671, 690]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[31]: text=病史陈述者签名：, bbox=[173, 698, 299, 717]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[32]: text=体格检查：T36.6℃，P89次/分，R20次/分钟，BP129/90mmHg，指脉氧氧饱和度：98%（未吸, bbox=[173, 725, 845, 744]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[33]: text=氧），发育正常，营养良好，神志清楚，正常面容，步入病房，查体合作。全身皮肤黏膜颜, bbox=[173, 752, 845, 771]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[34]: text=色正常，无肝掌，无蜘蛛痣，全身浅表淋巴结未触及肿大。头颅五官无畸形，眼睑无水肿，, bbox=[173, 779, 835, 798]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[35]: text=巩膜无黄染，双侧瞳孔等大同圆，直径约3mm，对光反射灵敏。无鼻分泌物，外耳道无异常, bbox=[173, 806, 836, 825]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[36]: text=分泌物，咽部无充血，扁桃体无肿大，口唇无发绀。颈软、气管居中，颈静脉无怒张，肝-, bbox=[173, 833, 836, 852]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[37]: text=颈静脉回流征，甲状腺无肿大。胸廓对称、无畸形，呼吸动度两侧一致，肋间隙正常，语颤, bbox=[173, 860, 845, 879]
2026-08-05 05:50:55,499 INFO     29 [qwen-vl-text] coord item[38]: text=正常，无胸膜摩擦感。叩诊呈清音，双肺呼吸音清，双肺可闻及弥漫性哮鸣音，无胸膜摩擦, bbox=[173, 887, 845, 906]
2026-08-05 05:50:55,500 INFO     29 [qwen-vl-text] page=13 — 39/39 coords, api_time=14.1s
2026-08-05 05:50:55,500 INFO     29 [qwen-vl-text] new_positions (39):
[[13, 145.666, 183.55599999999998, 18.445, 29.75], [13, 239.97, 671.9159999999999, 18.445, 29.75], [13, 145.666, 210.5, 29.75, 39.864999999999995], [13, 401.63399999999996, 460.574, 51.765, 62.474999999999994], [13, 145.666, 183.55599999999998, 74.97, 86.27499999999999], [13, 379.74199999999996, 677.81, 74.97, 86.27499999999999], [13, 145.666, 202.922, 91.63, 102.935], [13, 379.74199999999996, 451.312, 91.63, 102.935], [13, 145.666, 216.394, 107.695, 119.0], [13, 379.74199999999996, 492.57, 107.695, 119.0], [13, 145.666, 216.394, 123.75999999999999, 135.065], [13, 379.74199999999996, 435.31399999999996, 123.75999999999999, 135.065], [13, 145.666, 331.748, 140.42, 151.725], [13, 379.74199999999996, 564.14, 140.42, 151.725], [13, 145.666, 245.864, 156.48499999999999, 167.79], [13, 145.666, 388.162, 172.54999999999998, 183.855], [13, 145.666, 704.754, 188.61499999999998, 200.515], [13, 145.666, 710.648, 205.27499999999998, 216.57999999999998], [13, 145.666, 701.386, 221.34, 232.64499999999998], [13, 145.666, 701.386, 237.405, 248.70999999999998], [13, 145.666, 715.6999999999999, 253.47, 264.775], [13, 145.666, 710.648, 269.53499999999997, 280.84], [13, 145.666, 230.708, 285.59999999999997, 296.905], [13, 145.666, 710.648, 301.66499999999996, 313.565], [13, 145.666, 634.026, 318.325, 329.63], [13, 145.666, 711.49, 334.39, 345.695], [13, 145.666, 535.512, 350.455, 361.76], [13, 145.666, 569.192, 366.52, 377.825], [13, 212.184, 304.804, 364.14, 374.84999999999997], [13, 145.666, 465.626, 383.18, 394.48499999999996], [13, 145.666, 564.982, 399.245, 410.54999999999995], [13, 145.666, 251.75799999999998, 415.31, 426.615], [13, 145.666, 711.49, 431.375, 442.68], [13, 145.666, 711.49, 447.44, 458.745], [13, 145.666, 703.0699999999999, 463.505, 474.81], [13, 145.666, 703.9119999999999, 479.57, 490.875], [13, 145.666, 703.9119999999999, 495.635, 506.94], [13, 145.666, 711.49, 511.7, 523.005], [13, 145.666, 711.49, 527.765, 539.0699999999999]]
2026-08-05 05:50:55,501 INFO     29 [qwen-vl-text] ═══ DONE ═══ 39 positions, pages=1, time=22.4s
2026-08-05 05:50:55,522 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 05:50:55,522 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Extractor:Admission | outputs={"chunks": "4 items, types={'AdmissionRecord': 4}", "html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:50:55,522 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 05:50:55,523 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:50:55.522+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:50:55,534 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:50:55,534 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:50:55,534 INFO     29 [qwen-vl-text] positions(25): [[2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:50:55,534 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [1, 24]
2026-08-05 05:50:55,809 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:50:55,994 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:50:55,995 INFO     29 [qwen-vl-text] LLM extraction start, text_len=382
2026-08-05 05:50:55,996 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:50:55,996 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 51, \"bbox_end\": 75, \"encounter_dates\": [\"2025-02-25\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告时间: 2025-02-24\n怀化市肿瘤医院\n怀化市第二人民医院\n鹤城院区\n湖南HR\nCT影像诊断报告单\nID: 86562633\n检查号: CT00525514\n姓名:\n性别: 女\n年龄: 37岁\n住院号: 220999152\n床号: 46\n申请科室: 呼吸与危重症医学科\n申请医生: 易莹\n检查日期: 2025.02.25\n报告日期: 2025.02.25 09:45:16\n检查项目: CT成套:胸部(平扫(三维重建))\n检查所见:\n右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见\n条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主\n要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。\n意见:\n1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。\n2. 右肺中叶少许慢性炎症。",
    "role": "user"
  }
]
[92m05:50:55 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:50:55,997 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:51:02,955 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:51:02,955 INFO     29 [qwen-vl-text] LLM output (len=486):
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
  "findings": "右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见\n条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主\n要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。",
  "conclusion": "1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。\n2. 右肺中叶少许慢性炎症。",
  "physician": null,
  "reviewer": null
}
2026-08-05 05:51:02,960 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1719494, prompt_len=631
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
2026-08-05 05:51:04,587 INFO     29 [qwen-vl-text] coord API raw response (len=75):
```json
[
	{"text": "报告时间: 2025-02-24", "bbox": [478, 152, 598, 166]}
]
```
2026-08-05 05:51:04,587 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-05 05:51:04,587 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间: 2025-02-24, bbox=[478, 152, 598, 166]
2026-08-05 05:51:04,587 INFO     29 [qwen-vl-text] page=2 — 1/1 coords, api_time=1.6s
2026-08-05 05:51:04,588 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=699247, prompt_len=1050
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
2026-08-05 05:51:12,318 INFO     29 [qwen-vl-text] coord API raw response (len=1415):
[
	{"text": "怀化市肿瘤医院", "bbox": [205, 35, 388, 57]},
	{"text": "怀化市第二人民医院", "bbox": [205, 62, 388, 83]},
	{"text": "鹤城院区", "bbox": [392, 46, 481, 67]},
	{"text": "湖南HR", "bbox": [630, 50, 712, 74]},
	{"text": "CT影像诊断报告单", "bbox": [399, 95, 620, 120]},
	{"text": "ID: 86562633", "bbox": [141, 132, 260, 147]},
	{"text": "检查号: CT00525514", "bbox": [482, 126, 631, 141]},
	{"text": "姓名:", "bbox": [140, 160, 182, 177]},
	{"text": "性别: 女", "bbox": [334, 160, 401, 177]},
	{"text": "年龄: 37岁", "bbox": [470, 160, 545, 177]},
	{"text": "住院号: 220999152", "bbox": [589, 160, 726, 177]},
	{"text": "床号: 46", "bbox": [764, 160, 824, 177]},
	{"text": "申请科室: 呼吸与危重症医学科", "bbox": [141, 184, 372, 202]},
	{"text": "申请医生: 易莹", "bbox": [471, 184, 587, 202]},
	{"text": "检查日期: 2025.02.25", "bbox": [140, 210, 307, 227]},
	{"text": "报告日期: 2025.02.25 09:45:16", "bbox": [470, 210, 710, 227]},
	{"text": "检查项目: CT成套:胸部(平扫(三维重建))", "bbox": [138, 239, 441, 257]},
	{"text": "检查所见:", "bbox": [140, 299, 212, 317]},
	{"text": "右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见", "bbox": [183, 326, 854, 345]},
	{"text": "条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主", "bbox": [147, 350, 854, 369]},
	{"text": "要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "bbox": [146, 375, 657, 394]},
	{"text": "意见:", "bbox": [136, 704, 174, 722]},
	{"text": "1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。", "bbox": [144, 727, 610, 746]},
	{"text": "2. 右肺中叶少许慢性炎症。", "bbox": [143, 748, 366, 767]}
]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=7.7s
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[0]: text=怀化市肿瘤医院, bbox=[205, 35, 388, 57]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[1]: text=怀化市第二人民医院, bbox=[205, 62, 388, 83]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[2]: text=鹤城院区, bbox=[392, 46, 481, 67]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[3]: text=湖南HR, bbox=[630, 50, 712, 74]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[4]: text=CT影像诊断报告单, bbox=[399, 95, 620, 120]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[5]: text=ID: 86562633, bbox=[141, 132, 260, 147]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[6]: text=检查号: CT00525514, bbox=[482, 126, 631, 141]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[140, 160, 182, 177]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[8]: text=性别: 女, bbox=[334, 160, 401, 177]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[9]: text=年龄: 37岁, bbox=[470, 160, 545, 177]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[10]: text=住院号: 220999152, bbox=[589, 160, 726, 177]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[11]: text=床号: 46, bbox=[764, 160, 824, 177]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[12]: text=申请科室: 呼吸与危重症医学科, bbox=[141, 184, 372, 202]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[13]: text=申请医生: 易莹, bbox=[471, 184, 587, 202]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[14]: text=检查日期: 2025.02.25, bbox=[140, 210, 307, 227]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[15]: text=报告日期: 2025.02.25 09:45:16, bbox=[470, 210, 710, 227]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[16]: text=检查项目: CT成套:胸部(平扫(三维重建)), bbox=[138, 239, 441, 257]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[17]: text=检查所见:, bbox=[140, 299, 212, 317]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[18]: text=右肺中叶内侧段叶间裂旁见结节影, 大小约5mm×3mm, 边界清楚。右肺中叶另见, bbox=[183, 326, 854, 345]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[19]: text=条片状高密度影与胸膜粘连。双肺血管支气管束清晰。两肺门结构清楚, 气管及其主, bbox=[147, 350, 854, 369]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[20]: text=要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。, bbox=[146, 375, 657, 394]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[21]: text=意见:, bbox=[136, 704, 174, 722]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[22]: text=1. 右肺中叶内侧段结节, LU-RADS 2类, 建议年度复查。, bbox=[144, 727, 610, 746]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] coord item[23]: text=2. 右肺中叶少许慢性炎症。, bbox=[143, 748, 366, 767]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] page=3 — 24/24 coords, api_time=7.7s
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] new_positions (25):
[[2, 402.476, 503.51599999999996, 90.44, 98.77], [3, 172.60999999999999, 326.69599999999997, 20.825, 33.915], [3, 172.60999999999999, 326.69599999999997, 36.89, 49.385], [3, 330.06399999999996, 405.002, 27.369999999999997, 39.864999999999995], [3, 530.46, 599.504, 29.75, 44.03], [3, 335.95799999999997, 522.04, 56.525, 71.39999999999999], [3, 118.722, 218.92, 78.53999999999999, 87.46499999999999], [3, 405.844, 531.302, 74.97, 83.895], [3, 117.88, 153.244, 95.19999999999999, 105.315], [3, 281.228, 337.642, 95.19999999999999, 105.315], [3, 395.74, 458.89, 95.19999999999999, 105.315], [3, 495.938, 611.292, 95.19999999999999, 105.315], [3, 643.288, 693.808, 95.19999999999999, 105.315], [3, 118.722, 313.224, 109.47999999999999, 120.19], [3, 396.582, 494.25399999999996, 109.47999999999999, 120.19], [3, 117.88, 258.49399999999997, 124.94999999999999, 135.065], [3, 395.74, 597.8199999999999, 124.94999999999999, 135.065], [3, 116.196, 371.322, 142.20499999999998, 152.915], [3, 117.88, 178.504, 177.905, 188.61499999999998], [3, 154.08599999999998, 719.068, 193.97, 205.27499999999998], [3, 123.774, 719.068, 208.25, 219.55499999999998], [3, 122.932, 553.194, 223.125, 234.42999999999998], [3, 114.512, 146.50799999999998, 418.88, 429.59], [3, 121.24799999999999, 513.62, 432.565, 443.87], [3, 120.40599999999999, 308.17199999999997, 445.06, 456.36499999999995]]
2026-08-05 05:51:12,319 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=2, time=16.8s
2026-08-05 05:51:12,320 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:51:12,320 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:51:12,320 INFO     29 [qwen-vl-text] positions(24): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:51:12,320 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [24]
2026-08-05 05:51:12,498 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:51:12,499 INFO     29 [qwen-vl-text] LLM extraction start, text_len=430
2026-08-05 05:51:12,499 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:51:12,500 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 76, \"bbox_end\": 99, \"encounter_dates\": [\"2025-07-11\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "怀化市中心医院\nHUAIHUA CENTRAL HOSPITAL\n怀化市肿瘤医院\n湖南HR\nCT影像诊断报告单\nID: 93717786\n检查号: CT00568277\n姓名:\n性别: 女\n年龄: 37岁\n住院号: 221028180\n床号: 42\n申请科室: 呼吸与危重症医学科\n申请医生:\n检查日期: 2025.07.11\n报告日期: 2025.07.11 16:08:56\n检查项目: CT成套胸部平扫(三维重建)\n检查所见:\n与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。\n右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部\n分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。\n意见:\n1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。\n2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。",
    "role": "user"
  }
]
[92m05:51:12 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:51:12,501 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:51:16,421 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:51:16,421 INFO     29 [qwen-vl-text] LLM output (len=536):
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
  "findings": "与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。\n右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部\n分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。",
  "conclusion": "1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。\n2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。",
  "physician": null,
  "reviewer": null
}
2026-08-05 05:51:16,425 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=724530, prompt_len=1115
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
2026-08-05 05:51:26,603 INFO     29 [qwen-vl-text] coord API raw response (len=1870):
[
	{"text": "怀化市中心医院", "bbox": [204, 27, 356, 48]},
	{"text": "HUAIHUA CENTRAL HOSPITAL", "bbox": [204, 49, 356, 60]},
	{"text": "怀化市肿瘤医院", "bbox": [204, 65, 356, 80]},
	{"text": "湖南HR", "bbox": [632, 43, 718, 69]},
	{"text": "CT影像诊断报告单", "bbox": [395, 89, 622, 116]},
	{"text": "ID: 93717786", "bbox": [137, 129, 255, 144]},
	{"text": "检查号: CT00568277", "bbox": [480, 122, 633, 138]},
	{"text": "姓名:", "bbox": [136, 157, 177, 175], "bbox": [136, 157, 177, 175]},
	{"text": "性别: 女", "bbox": [331, 157, 398, 175]},
	{"text": "年龄: 37岁", "bbox": [469, 157, 546, 175]},
	{"text": "住院号: 221028180", "bbox": [590, 157, 731, 175]},
	{"text": "床号: 42", "bbox": [770, 157, 833, 175]},
	{"text": "申请科室: 呼吸与危重症医学科", "bbox": [137, 182, 370, 200], "bbox": [137, 182, 370, 200]},
	{"text": "申请医生:", "bbox": [470, 182, 546, 200], "bbox": [470, 182, 546, 200]},
	{"text": "检查日期: 2025.07.11", "bbox": [136, 208, 304, 226], "bbox": [136, 208, 304, 226]},
	{"text": "报告日期: 2025.07.11 16:08:56", "bbox": [469, 208, 714, 226], "bbox": [469, 208, 714, 226]},
	{"text": "检查项目: CT成套胸部平扫(三维重建)", "bbox": [134, 237, 414, 255], "bbox": [134, 237, 414, 255]},
	{"text": "检查所见:", "bbox": [137, 296, 210, 313], "bbox": [137, 296, 210, 313]},
	{"text": "与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。", "bbox": [175, 323, 854, 339], "bbox": [175, 323, 854, 339]},
	{"text": "右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部", "bbox": [144, 342, 860, 359], "bbox": [144, 342, 860, 359]},
	{"text": "分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。", "bbox": [144, 361, 838, 377], "bbox": [144, 361, 838, 377]},
	{"text": "意见:", "bbox": [136, 704, 176, 721], "bbox": [136, 704, 176, 721]},
	{"text": "1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。", "bbox": [144, 727, 691, 745], "bbox": [144, 727, 691, 745]},
	{"text": "2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。", "bbox": [144, 746, 604, 765], "bbox": [144, 746, 604, 765]}
]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=10.2s
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[0]: text=怀化市中心医院, bbox=[204, 27, 356, 48]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[1]: text=HUAIHUA CENTRAL HOSPITAL, bbox=[204, 49, 356, 60]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[2]: text=怀化市肿瘤医院, bbox=[204, 65, 356, 80]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[3]: text=湖南HR, bbox=[632, 43, 718, 69]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[4]: text=CT影像诊断报告单, bbox=[395, 89, 622, 116]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[5]: text=ID: 93717786, bbox=[137, 129, 255, 144]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[6]: text=检查号: CT00568277, bbox=[480, 122, 633, 138]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[136, 157, 177, 175]
2026-08-05 05:51:26,604 INFO     29 [qwen-vl-text] coord item[8]: text=性别: 女, bbox=[331, 157, 398, 175]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[9]: text=年龄: 37岁, bbox=[469, 157, 546, 175]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[10]: text=住院号: 221028180, bbox=[590, 157, 731, 175]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[11]: text=床号: 42, bbox=[770, 157, 833, 175]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[12]: text=申请科室: 呼吸与危重症医学科, bbox=[137, 182, 370, 200]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[13]: text=申请医生:, bbox=[470, 182, 546, 200]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[14]: text=检查日期: 2025.07.11, bbox=[136, 208, 304, 226]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[15]: text=报告日期: 2025.07.11 16:08:56, bbox=[469, 208, 714, 226]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[16]: text=检查项目: CT成套胸部平扫(三维重建), bbox=[134, 237, 414, 255]
2026-08-05 05:51:26,605 INFO     29 [qwen-vl-text] coord item[17]: text=检查所见:, bbox=[137, 296, 210, 313]
2026-08-05 05:51:26,606 INFO     29 [qwen-vl-text] coord item[18]: text=与2025-02-25片对比,现:右肺中叶内侧段叶间裂旁见结节影大致同前,大小约5mm×3mm,边界清楚。, bbox=[175, 323, 854, 339]
2026-08-05 05:51:26,606 INFO     29 [qwen-vl-text] coord item[19]: text=右肺中叶见条片状高密度影与胸膜粘连较前无明显改变。双肺另见少许絮片状模糊影。双肺血管支气管束部, bbox=[144, 342, 860, 359]
2026-08-05 05:51:26,606 INFO     29 [qwen-vl-text] coord item[20]: text=分增多增粗。两肺门结构清楚,气管及其主要分支通畅。纵隔内未见明显肿大淋巴结。未见明显胸水征。, bbox=[144, 361, 838, 377]
2026-08-05 05:51:26,606 INFO     29 [qwen-vl-text] coord item[21]: text=意见:, bbox=[136, 704, 176, 721]
2026-08-05 05:51:26,606 INFO     29 [qwen-vl-text] coord item[22]: text=1.右肺中叶内侧段结节大致同前,LU-RADS 2类,建议年度复查。, bbox=[144, 727, 691, 745]
2026-08-05 05:51:26,606 INFO     29 [qwen-vl-text] coord item[23]: text=2.支气管疾患并双肺少许炎性病变,病灶较前稍增多。, bbox=[144, 746, 604, 765]
2026-08-05 05:51:26,606 INFO     29 [qwen-vl-text] page=4 — 24/24 coords, api_time=10.2s
2026-08-05 05:51:26,607 INFO     29 [qwen-vl-text] new_positions (24):
[[4, 171.768, 299.752, 16.064999999999998, 28.56], [4, 171.768, 299.752, 29.154999999999998, 35.699999999999996], [4, 171.768, 299.752, 38.675, 47.599999999999994], [4, 532.144, 604.5559999999999, 25.584999999999997, 41.055], [4, 332.59, 523.7239999999999, 52.955, 69.02], [4, 115.354, 214.70999999999998, 76.755, 85.67999999999999], [4, 404.15999999999997, 532.986, 72.59, 82.11], [4, 114.512, 149.034, 93.41499999999999, 104.125], [4, 278.702, 335.116, 93.41499999999999, 104.125], [4, 394.89799999999997, 459.73199999999997, 93.41499999999999, 104.125], [4, 496.78, 615.502, 93.41499999999999, 104.125], [4, 648.34, 701.386, 93.41499999999999, 104.125], [4, 115.354, 311.53999999999996, 108.28999999999999, 119.0], [4, 395.74, 459.73199999999997, 108.28999999999999, 119.0], [4, 114.512, 255.968, 123.75999999999999, 134.47], [4, 394.89799999999997, 601.188, 123.75999999999999, 134.47], [4, 112.828, 348.58799999999997, 141.015, 151.725], [4, 115.354, 176.82, 176.12, 186.23499999999999], [4, 147.35, 719.068, 192.185, 201.70499999999998], [4, 121.24799999999999, 724.12, 203.48999999999998, 213.605], [4, 121.24799999999999, 705.596, 214.795, 224.315], [4, 114.512, 148.192, 418.88, 428.995], [4, 121.24799999999999, 581.822, 432.565, 443.275], [4, 121.24799999999999, 508.568, 443.87, 455.17499999999995]]
2026-08-05 05:51:26,607 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=14.3s
2026-08-05 05:51:26,607 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:51:26,607 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:51:26,607 INFO     29 [qwen-vl-text] positions(28): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:51:26,608 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [24]
2026-08-05 05:51:26,787 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:51:26,789 INFO     29 [qwen-vl-text] LLM extraction start, text_len=870
2026-08-05 05:51:26,789 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:51:26,789 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 330, \"bbox_end\": 357, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"呼吸科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告时间: 2026-02-09\nPred Bst % (B/Pd) A1 A2 A3\nFVC [L] 2.99 2.21 74.02 2.21 2.12 2.09\nFEV 1 [L] 2.67 1.26 48.56 1.26 1.13 1.18\nFEV6 [L] 2.12 2.12 2.05 2.02\nFEV 1 % FVC [%] 84.19 56.48 67.09 56.48 53.33 56.67\nFEV 1 % VC MAX [%] 81.88 55.26 67.48 55.26 50.10 52.31\nVC MAX [L] 3.03 2.26 74.60\nPEF [L/s] 6.28 2.66 42.36 2.66 2.58 2.43\nMMEF 75/25 [L/s] 3.57 0.51 14.35 0.51 0.49 0.41\nMEF 75 [L/s] 5.64 1.47 26.14 1.47 0.80 1.21\nMEF 50 [L/s] 4.01 0.68 16.97 0.68 0.72 0.57\nMEF 25 [L/s] 1.79 0.19 10.52 0.19 0.18 0.15\nV backextrapolation ex [L] 0.05 0.03 0.04\nV backextrapol. % FVC [%] 2.07 1.50 1.81\nFET [s] 7.63 7.35 7.55\nFEF 200-1200 [L/s] 1.19 0.98 1.05\nFVC IN [L] 3.03 2.26 74.60 2.26 2.15 2.13\nFIV1 [L] 2.21 2.12 2.09\nFIV1 % FVC [%] 97.79 98.68 98.05\nFEF50 % FIF50 [%] 22.86 25.05 19.46\nPIF [L/s] 3.04 3.04 2.99\nMVV [L/min] 99.77 46.21 46.32 46.21\nBF MVV [1/min] 75.55 75.55",
    "role": "user"
  }
]
[92m05:51:26 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:51:26,791 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:51:28,573 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:51:28.572+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:51:41,598 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:51:41,598 INFO     29 [qwen-vl-text] LLM output (len=1590):
{
  "exam_date": "2026-02-09",
  "report_date": "2026-02-09",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": null,
  "department": "呼吸科门诊",
  "bed_number": null,
  "findings": "| 指标 | Pred | Bst | % (B/Pd) | A1 | A2 | A3 |\n|---|---|---|---|---|---|---|\n| FVC [L] | 2.99 | 2.21 | 74.02 | 2.21 | 2.12 | 2.09 |\n| FEV 1 [L] | 2.67 | 1.26 | 48.56 | 1.26 | 1.13 | 1.18 |\n| FEV6 [L] | | 2.12 | | 2.12 | 2.05 | 2.02 |\n| FEV 1 % FVC [%] | 84.19 | 56.48 | 67.09 | 56.48 | 53.33 | 56.67 |\n| FEV 1 % VC MAX [%] | 81.88 | 55.26 | 67.48 | 55.26 | 50.10 | 52.31 |\n| VC MAX [L] | 3.03 | 2.26 | 74.60 | | | |\n| PEF [L/s] | 6.28 | 2.66 | 42.36 | 2.66 | 2.58 | 2.43 |\n| MMEF 75/25 [L/s] | 3.57 | 0.51 | 14.35 | 0.51 | 0.49 | 0.41 |\n| MEF 75 [L/s] | 5.64 | 1.47 | 26.14 | 1.47 | 0.80 | 1.21 |\n| MEF 50 [L/s] | 4.01 | 0.68 | 16.97 | 0.68 | 0.72 | 0.57 |\n| MEF 25 [L/s] | 1.79 | 0.19 | 10.52 | 0.19 | 0.18 | 0.15 |\n| V backextrapolation ex [L] | | 0.05 | | 0.03 | 0.04 | |\n| V backextrapol. % FVC [%] | | 2.07 | | 1.50 | 1.81 | |\n| FET [s] | | 7.63 | | 7.35 | 7.55 | |\n| FEF 200-1200 [L/s] | | 1.19 | | 0.98 | 1.05 | |\n| FVC IN [L] | 3.03 | 2.26 | 74.60 | 2.26 | 2.15 | 2.13 |\n| FIV1 [L] | | 2.21 | | 2.12 | 2.09 | |\n| FIV1 % FVC [%] | | 97.79 | | 98.68 | 98.05 | |\n| FEF50 % FIF50 [%] | | 22.86 | | 25.05 | 19.46 | |\n| PIF [L/s] | | 3.04 | | 3.04 | 2.99 | |\n| MVV [L/min] | 99.77 | 46.21 | | 46.32 | 46.21 | |\n| BF MVV [1/min] | | 75.55 | | 75.55 | | |",
  "conclusion": null,
  "physician": null,
  "reviewer": null
}
2026-08-05 05:51:41,600 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=819324, prompt_len=1555
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["报告时间: 2026-02-09", "Pred Bst % (B/Pd) A1 A2 A3", "FVC [L] 2.99 2.21 74.02 2.21 2.12 2.09", "FEV 1 [L] 2.67 1.26 48.56 1.26 1.13 1.18", "FEV6 [L] 2.12 2.12 2.05 2.02", "FEV 1 % FVC [%] 84.19 56.48 67.09 56.48 53.33 56.67", "FEV 1 % VC MAX [%] 81.88 55.26 67.48 55.26 50.10 52.31", "VC MAX [L] 3.03 2.26 74.60", "PEF [L/s] 6.28 2.66 42.36 2.66 2.58 2.43", "MMEF 75/25 [L/s] 3.57 0.51 14.35 0.51 0.49 0.41", "MEF 75 [L/s] 5.64 1.47 26.14 1.47 0.80 1.21", "MEF 50 [L/s] 4.01 0.68 16.97 0.68 0.72 0.57", "MEF 25 [L/s] 1.79 0.19 10.52 0.19 0.18 0.15", "V backextrapolation ex [L] 0.05 0.03 0.04", "V backextrapol. % FVC [%] 2.07 1.50 1.81", "FET [s] 7.63 7.35 7.55", "FEF 200-1200 [L/s] 1.19 0.98 1.05", "FVC IN [L] 3.03 2.26 74.60 2.26 2.15 2.13", "FIV1 [L] 2.21 2.12 2.09", "FIV1 % FVC [%] 97.79 98.68 98.05", "FEF50 % FIF50 [%] 22.86 25.05 19.46", "PIF [L/s] 3.04 3.04 2.99", "MVV [L/min] 99.77 46.21 46.32 46.21", "BF MVV [1/min] 75.55 75.55"]

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
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord API raw response (len=1905):
[
	{"text": "报告时间: 2026-02-09", "bbox": [800, 36, 916, 58]},
	{"text": "Pred Bst % (B/Pd) A1 A2 A3", "bbox": [341, 160, 658, 174]},
	{"text": "FVC [L] 2.99 2.21 74.02 2.21 2.12 2.09", "bbox": [89, 187, 658, 201]},
	{"text": "FEV 1 [L] 2.67 1.26 48.56 1.26 1.13 1.18", "bbox": [89, 201, 658, 214]},
	{"text": "FEV6 [L] 2.12 2.12 2.05 2.02", "bbox": [89, 214, 658, 227]},
	{"text": "FEV 1 % FVC [%] 84.19 56.48 67.09 56.48 53.33 56.67", "bbox": [89, 227, 658, 240]},
	{"text": "FEV 1 % VC MAX [%] 81.88 55.26 67.48 55.26 50.10 52.31", "bbox": [89, 240, 658, 254]},
	{"text": "VC MAX [L] 3.03 2.26 74.60", "bbox": [89, 254, 488, 267]},
	{"text": "PEF [L/s] 6.28 2.66 42.36 2.66 2.58 2.43", "bbox": [89, 267, 658, 280]},
	{"text": "MMEF 75/25 [L/s] 3.57 0.51 14.35 0.51 0.49 0.41", "bbox": [89, 280, 658, 294]},
	{"text": "MEF 75 [L/s] 5.64 1.47 26.14 1.47 0.80 1.21", "bbox": [89, 294, 658, 307]},
	{"text": "MEF 50 [L/s] 4.01 0.68 16.97 0.68 0.72 0.57", "bbox": [89, 307, 658, 320]},
	{"text": "MEF 25 [L/s] 1.79 0.19 10.52 0.19 0.18 0.15", "bbox": [89, 320, 658, 334]},
	{"text": "V backextrapolation ex [L] 0.05 0.03 0.04", "bbox": [89, 334, 658, 347]},
	{"text": "V backextrapol. % FVC [%] 2.07 1.50 1.81", "bbox": [89, 347, 658, 360]},
	{"text": "FET [s] 7.63 7.35 7.55", "bbox": [89, 360, 658, 373]},
	{"text": "FEF 200-1200 [L/s] 1.19 0.98 1.05", "bbox": [89, 373, 658, 387]},
	{"text": "FVC IN [L] 3.03 2.26 74.60 2.26 2.15 2.13", "bbox": [89, 387, 658, 400]},
	{"text": "FIV1 [L] 2.21 2.12 2.09", "bbox": [89, 400, 658, 413]},
	{"text": "FIV1 % FVC [%] 97.79 98.68 98.05", "bbox": [89, 413, 658, 427]},
	{"text": "FEF50 % FIF50 [%] 22.86 25.05 19.46", "bbox": [89, 427, 658, 440]},
	{"text": "PIF [L/s] 3.04 3.04 2.99", "bbox": [89, 440, 658, 453]},
	{"text": "MVV [L/min] 99.77 46.21 46.32 46.21", "bbox": [89, 453, 544, 467]},
	{"text": "BF MVV [1/min] 75.55 75.55", "bbox": [89, 467, 544, 480]}
]
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=10.7s
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间: 2026-02-09, bbox=[800, 36, 916, 58]
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord item[1]: text=Pred Bst % (B/Pd) A1 A2 A3, bbox=[341, 160, 658, 174]
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord item[2]: text=FVC [L] 2.99 2.21 74.02 2.21 2.12 2.09, bbox=[89, 187, 658, 201]
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord item[3]: text=FEV 1 [L] 2.67 1.26 48.56 1.26 1.13 1.18, bbox=[89, 201, 658, 214]
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord item[4]: text=FEV6 [L] 2.12 2.12 2.05 2.02, bbox=[89, 214, 658, 227]
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord item[5]: text=FEV 1 % FVC [%] 84.19 56.48 67.09 56.48 53.33 56.67, bbox=[89, 227, 658, 240]
2026-08-05 05:51:52,320 INFO     29 [qwen-vl-text] coord item[6]: text=FEV 1 % VC MAX [%] 81.88 55.26 67.48 55.26 50.10 52.31, bbox=[89, 240, 658, 254]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[7]: text=VC MAX [L] 3.03 2.26 74.60, bbox=[89, 254, 488, 267]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[8]: text=PEF [L/s] 6.28 2.66 42.36 2.66 2.58 2.43, bbox=[89, 267, 658, 280]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[9]: text=MMEF 75/25 [L/s] 3.57 0.51 14.35 0.51 0.49 0.41, bbox=[89, 280, 658, 294]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[10]: text=MEF 75 [L/s] 5.64 1.47 26.14 1.47 0.80 1.21, bbox=[89, 294, 658, 307]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[11]: text=MEF 50 [L/s] 4.01 0.68 16.97 0.68 0.72 0.57, bbox=[89, 307, 658, 320]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[12]: text=MEF 25 [L/s] 1.79 0.19 10.52 0.19 0.18 0.15, bbox=[89, 320, 658, 334]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[13]: text=V backextrapolation ex [L] 0.05 0.03 0.04, bbox=[89, 334, 658, 347]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[14]: text=V backextrapol. % FVC [%] 2.07 1.50 1.81, bbox=[89, 347, 658, 360]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[15]: text=FET [s] 7.63 7.35 7.55, bbox=[89, 360, 658, 373]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[16]: text=FEF 200-1200 [L/s] 1.19 0.98 1.05, bbox=[89, 373, 658, 387]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[17]: text=FVC IN [L] 3.03 2.26 74.60 2.26 2.15 2.13, bbox=[89, 387, 658, 400]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[18]: text=FIV1 [L] 2.21 2.12 2.09, bbox=[89, 400, 658, 413]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[19]: text=FIV1 % FVC [%] 97.79 98.68 98.05, bbox=[89, 413, 658, 427]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[20]: text=FEF50 % FIF50 [%] 22.86 25.05 19.46, bbox=[89, 427, 658, 440]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[21]: text=PIF [L/s] 3.04 3.04 2.99, bbox=[89, 440, 658, 453]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[22]: text=MVV [L/min] 99.77 46.21 46.32 46.21, bbox=[89, 453, 544, 467]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] coord item[23]: text=BF MVV [1/min] 75.55 75.55, bbox=[89, 467, 544, 480]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] page=14 — 24/24 coords, api_time=10.7s
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] new_positions (24):
[[14, 476.0, 545.02, 30.311999999999998, 48.836], [14, 202.89499999999998, 391.51, 134.72, 146.50799999999998], [14, 52.955, 391.51, 157.454, 169.242], [14, 52.955, 391.51, 169.242, 180.188], [14, 52.955, 391.51, 180.188, 191.134], [14, 52.955, 391.51, 191.134, 202.07999999999998], [14, 52.955, 391.51, 202.07999999999998, 213.868], [14, 52.955, 290.36, 213.868, 224.814], [14, 52.955, 391.51, 224.814, 235.76], [14, 52.955, 391.51, 235.76, 247.548], [14, 52.955, 391.51, 247.548, 258.49399999999997], [14, 52.955, 391.51, 258.49399999999997, 269.44], [14, 52.955, 391.51, 269.44, 281.228], [14, 52.955, 391.51, 281.228, 292.174], [14, 52.955, 391.51, 292.174, 303.12], [14, 52.955, 391.51, 303.12, 314.066], [14, 52.955, 391.51, 314.066, 325.854], [14, 52.955, 391.51, 325.854, 336.8], [14, 52.955, 391.51, 336.8, 347.746], [14, 52.955, 391.51, 347.746, 359.534], [14, 52.955, 391.51, 359.534, 370.47999999999996], [14, 52.955, 391.51, 370.47999999999996, 381.426], [14, 52.955, 323.68, 381.426, 393.214], [14, 52.955, 323.68, 393.214, 404.15999999999997]]
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=25.7s
2026-08-05 05:51:52,321 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:51:52,321 INFO     29 [qwen-vl-text] positions(46): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:51:52,322 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [46]
2026-08-05 05:51:52,524 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:51:52,525 INFO     29 [qwen-vl-text] LLM extraction start, text_len=974
2026-08-05 05:51:52,525 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:51:52,525 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 358, \"bbox_end\": 403, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"呼吸科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "呼出气一氧化氮检测报告单\n姓名：杨\n性别：女\n出生日期：1987-12-01\n年龄：38岁2个月\nID号：\n测试日期：2026-02-09\n科室：呼吸科门诊\n医生：张\n问卷调查：\n激素：正在使用口 三天内未使用口 从未使用口\n抗生素：正在使用口 三天内未使用口 从未使用口\n吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口\n症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：\n病史：过敏史口 其他：\n注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。\n检测信息：\n项目：在线\n呼气压力：8.8cmH2O 呼气流速：45ml/s\n呼气时间：5s 温度：21.8℃ 湿度：38.9%\n呼气浓度：10、11、12、11、11、11、10、10、10、\n10、10、10、11、10、11、11、11、11ppb\n项目：小气道\n呼气压力：11.3cmH2O 呼气流速：202ml/s\n呼气时间：3s 温度：22.0℃ 湿度：39.0%\n呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0\n0.0、0.0、0.0、0.0、1.0、1.0、1.0、\n1.0、1.0、0.0、0.0、0.0ppb\n参考意义：\n(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)\n测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型\nFeNO < 25ppb < 20ppb* 非嗜酸性气道炎症\n25 - 50ppb 20 - 35ppb* 混合型气道炎症\n> 50ppb > 35ppb* 嗜酸性气道炎症\nCaNO ≤ 5ppb ≤ 3ppb 小气道正常\n> 5ppb > 3ppb 小气道炎症\nFaNO < 125ppb 考虑Kartagener综合征、PCD、CF或\n重度的鼻窦炎或鼻息肉\n125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉\n250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断\n> 500ppb 考虑过敏性鼻炎\n(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n此结果仅对本次呼气检测负责\n测定结果：FeNO 60:11ppb CaNO :1.0ppb\n操作员：蒋细萍\n张日石",
    "role": "user"
  }
]
[92m05:51:52 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:51:52,527 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:52:01,336 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:52:01.335+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:52:03,473 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:52:03,473 INFO     29 [qwen-vl-text] LLM output (len=1341):
{
  "exam_date": "2026-02-09",
  "report_date": null,
  "exam_name": "呼出气一氧化氮检测",
  "exam_category": "other",
  "body_part": "气道",
  "patient_name": "杨",
  "patient_gender": "女",
  "department": "呼吸科门诊",
  "bed_number": null,
  "findings": "问卷调查：\n激素：正在使用口 三天内未使用口 从未使用口\n抗生素：正在使用口 三天内未使用口 从未使用口\n吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口\n症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：\n病史：过敏史口 其他：\n注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。\n检测信息：\n项目：在线\n呼气压力：8.8cmH2O 呼气流速：45ml/s\n呼气时间：5s 温度：21.8℃ 湿度：38.9%\n呼气浓度：10、11、12、11、11、11、10、10、10、\n10、10、10、11、10、11、11、11、11ppb\n项目：小气道\n呼气压力：11.3cmH2O 呼气流速：202ml/s\n呼气时间：3s 温度：22.0℃ 湿度：39.0%\n呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0\n0.0、0.0、0.0、0.0、1.0、1.0、1.0、\n1.0、1.0、0.0、0.0、0.0ppb",
  "conclusion": "测定结果：FeNO 60:11ppb CaNO :1.0ppb\n参考意义：\n(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断)\n| 测试项目 | FeNO参考值（>12岁） | FeNO参考值（≤12岁） | 炎症鉴别类型 |\n| --- | --- | --- | --- |\n| FeNO | < 25ppb | < 20ppb* | 非嗜酸性气道炎症 |\n| | 25 - 50ppb | 20 - 35ppb* | 混合型气道炎症 |\n| | > 50ppb | > 35ppb* | 嗜酸性气道炎症 |\n| CaNO | ≤ 5ppb | ≤ 3ppb | 小气道正常 |\n| | > 5ppb | > 3ppb | 小气道炎症 |\n| FaNO | < 125ppb | | 考虑Kartagener综合征、PCD、CF或重度的鼻窦炎或鼻息肉 |\n| | 125 - 250ppb | | 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉 |\n| | 250 - 500ppb | | 非过敏性（嗜中性）炎症，考虑感染或其他诊断 |\n| | > 500ppb | | 考虑过敏性鼻炎 |\n(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n此结果仅对本次呼气检测负责",
  "physician": "张日石",
  "reviewer": null
}
2026-08-05 05:52:03,475 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1026194, prompt_len=1725
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
2026-08-05 05:52:22,191 INFO     29 [qwen-vl-text] coord API raw response (len=2994):
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
	{"text": "症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：", "bbox": [168, 233, 742, 250]},
	{"text": "病史：过敏史口 其他：", "bbox": [168, 253, 422, 270]},
	{"text": "注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。", "bbox": [175, 272, 768, 285]},
	{"text": "检测信息：", "bbox": [157, 288, 237, 302]},
	{"text": "项目：在线", "bbox": [172, 310, 236, 323]},
	{"text": "呼气压力：8.8cmH2O 呼气流速：45ml/s", "bbox": [172, 327, 445, 340]},
	{"text": "呼气时间：5s 温度：21.8℃ 湿度：38.9%", "bbox": [172, 344, 474, 357]},
	{"text": "呼气浓度：10、11、12、11、11、11、10、10、10、", "bbox": [172, 360, 486, 373]},
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
	{"text": "125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉", "bbox": [168, 738, 848, 755]},
	{"text": "250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断", "bbox": [168, 758, 848, 775]},
	{"text": "> 500ppb 考虑过敏性鼻炎", "bbox": [168, 778, 848, 795]},
	{"text": "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "bbox": [178, 797, 603, 809]},
	{"text": "此结果仅对本次呼气检测负责", "bbox": [178, 810, 343, 822]},
	{"text": "测定结果：FeNO 60:11ppb CaNO :1.0ppb", "bbox": [178, 833, 543, 847]},
	{"text": "操作员：蒋细萍", "bbox": [178, 852, 297, 866]},
	{"text": "张日石", "bbox": [718, 870, 786, 897]}
]
2026-08-05 05:52:22,192 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=18.7s
2026-08-05 05:52:22,192 INFO     29 [qwen-vl-text] coord item[0]: text=呼出气一氧化氮检测报告单, bbox=[386, 70, 603, 85]
2026-08-05 05:52:22,192 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：杨, bbox=[168, 100, 270, 114]
2026-08-05 05:52:22,192 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[413, 100, 498, 114]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[3]: text=出生日期：1987-12-01, bbox=[637, 100, 804, 114]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：38岁2个月, bbox=[168, 116, 294, 130]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[5]: text=ID号：, bbox=[413, 116, 472, 130]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[6]: text=测试日期：2026-02-09, bbox=[637, 116, 804, 130]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[7]: text=科室：呼吸科门诊, bbox=[168, 133, 303, 147]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[8]: text=医生：张, bbox=[413, 133, 555, 147]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[9]: text=问卷调查：, bbox=[157, 149, 237, 163]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[10]: text=激素：正在使用口 三天内未使用口 从未使用口, bbox=[168, 171, 742, 188]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[11]: text=抗生素：正在使用口 三天内未使用口 从未使用口, bbox=[168, 191, 742, 208]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[12]: text=吸烟史：已戒烟口 1h内未吸烟口 从未吸烟口, bbox=[168, 212, 742, 229]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[13]: text=症状：咳嗽口 咳痰口 喘息口 鼻塞口 喷嚏口 其他：, bbox=[168, 233, 742, 250]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[14]: text=病史：过敏史口 其他：, bbox=[168, 253, 422, 270]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[15]: text=注：检测前1小时内禁水禁食、禁止吸烟、避免剧烈运动；2小时内禁食含硝酸盐食物；4小时内禁酒。, bbox=[175, 272, 768, 285]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[16]: text=检测信息：, bbox=[157, 288, 237, 302]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[17]: text=项目：在线, bbox=[172, 310, 236, 323]
2026-08-05 05:52:22,193 INFO     29 [qwen-vl-text] coord item[18]: text=呼气压力：8.8cmH2O 呼气流速：45ml/s, bbox=[172, 327, 445, 340]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[19]: text=呼气时间：5s 温度：21.8℃ 湿度：38.9%, bbox=[172, 344, 474, 357]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[20]: text=呼气浓度：10、11、12、11、11、11、10、10、10、, bbox=[172, 360, 486, 373]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[21]: text=10、10、10、11、10、11、11、11、11ppb, bbox=[178, 377, 445, 389]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[22]: text=项目：小气道, bbox=[522, 310, 600, 323]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[23]: text=呼气压力：11.3cmH2O 呼气流速：202ml/s, bbox=[522, 327, 802, 340]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[24]: text=呼气时间：3s 温度：22.0℃ 湿度：39.0%, bbox=[522, 344, 825, 357]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[25]: text=呼气浓度：1.0、1.0、1.0、0.0、1.0、0.0, bbox=[522, 360, 790, 373]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[26]: text=0.0、0.0、0.0、0.0、1.0、1.0、1.0、, bbox=[527, 377, 774, 389]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[27]: text=1.0、1.0、0.0、0.0、0.0ppb, bbox=[527, 393, 718, 405]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[28]: text=参考意义：, bbox=[157, 540, 235, 554]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[29]: text=(根据ATS及ERS 2001及2004年eNO临床指南，结合NO呼气浓度的测定结果及症状判断), bbox=[184, 559, 655, 571]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[30]: text=测试项目 FeNO参考值（>12岁） FeNO参考值（≤12岁） 炎症鉴别类型, bbox=[168, 577, 848, 594]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[31]: text=FeNO < 25ppb < 20ppb* 非嗜酸性气道炎症, bbox=[168, 597, 848, 614]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[32]: text=25 - 50ppb 20 - 35ppb* 混合型气道炎症, bbox=[168, 617, 848, 634]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[33]: text=> 50ppb > 35ppb* 嗜酸性气道炎症, bbox=[168, 637, 848, 654]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[34]: text=CaNO ≤ 5ppb ≤ 3ppb 小气道正常, bbox=[168, 658, 848, 675]
2026-08-05 05:52:22,194 INFO     29 [qwen-vl-text] coord item[35]: text=> 5ppb > 3ppb 小气道炎症, bbox=[168, 678, 848, 695]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[36]: text=< 125ppb 考虑Kartagener综合征、PCD、CF或, bbox=[168, 700, 848, 717]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[37]: text=重度的鼻窦炎或鼻息肉, bbox=[617, 719, 745, 731]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[38]: text=125 - 250ppb 鼻窦口开放不佳，考虑鼻窦炎或鼻息肉, bbox=[168, 738, 848, 755]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[39]: text=250 - 500ppb 非过敏性（嗜中性）炎症，考虑感染或其他诊断, bbox=[168, 758, 848, 775]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[40]: text=> 500ppb 考虑过敏性鼻炎, bbox=[168, 778, 848, 795]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[41]: text=(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb), bbox=[178, 797, 603, 809]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[42]: text=此结果仅对本次呼气检测负责, bbox=[178, 810, 343, 822]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[43]: text=测定结果：FeNO 60:11ppb CaNO :1.0ppb, bbox=[178, 833, 543, 847]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[44]: text=操作员：蒋细萍, bbox=[178, 852, 297, 866]
2026-08-05 05:52:22,195 INFO     29 [qwen-vl-text] coord item[45]: text=张日石, bbox=[718, 870, 786, 897]
2026-08-05 05:52:22,196 INFO     29 [qwen-vl-text] page=15 — 46/46 coords, api_time=18.7s
2026-08-05 05:52:22,196 INFO     29 [qwen-vl-text] new_positions (46):
[[15, 229.67, 358.78499999999997, 58.94, 71.57], [15, 99.96, 160.65, 84.2, 95.988], [15, 245.73499999999999, 296.31, 84.2, 95.988], [15, 379.015, 478.38, 84.2, 95.988], [15, 99.96, 174.92999999999998, 97.672, 109.46], [15, 245.73499999999999, 280.84, 97.672, 109.46], [15, 379.015, 478.38, 97.672, 109.46], [15, 99.96, 180.285, 111.98599999999999, 123.774], [15, 245.73499999999999, 330.22499999999997, 111.98599999999999, 123.774], [15, 93.41499999999999, 141.015, 125.458, 137.246], [15, 99.96, 441.48999999999995, 143.982, 158.296], [15, 99.96, 441.48999999999995, 160.822, 175.136], [15, 99.96, 441.48999999999995, 178.504, 192.81799999999998], [15, 99.96, 441.48999999999995, 196.186, 210.5], [15, 99.96, 251.08999999999997, 213.02599999999998, 227.34], [15, 104.125, 456.96, 229.024, 239.97], [15, 93.41499999999999, 141.015, 242.49599999999998, 254.284], [15, 102.33999999999999, 140.42, 261.02, 271.966], [15, 102.33999999999999, 264.775, 275.334, 286.28], [15, 102.33999999999999, 282.03, 289.64799999999997, 300.594], [15, 102.33999999999999, 289.16999999999996, 303.12, 314.066], [15, 105.91, 264.775, 317.43399999999997, 327.538], [15, 310.59, 357.0, 261.02, 271.966], [15, 310.59, 477.19, 275.334, 286.28], [15, 310.59, 490.875, 289.64799999999997, 300.594], [15, 310.59, 470.04999999999995, 303.12, 314.066], [15, 313.565, 460.53, 317.43399999999997, 327.538], [15, 313.565, 427.21, 330.906, 341.01], [15, 93.41499999999999, 139.825, 454.68, 466.46799999999996], [15, 109.47999999999999, 389.72499999999997, 470.678, 480.782], [15, 99.96, 504.56, 485.834, 500.14799999999997], [15, 99.96, 504.56, 502.674, 516.9879999999999], [15, 99.96, 504.56, 519.514, 533.828], [15, 99.96, 504.56, 536.3539999999999, 550.668], [15, 99.96, 504.56, 554.036, 568.35], [15, 99.96, 504.56, 570.876, 585.1899999999999], [15, 99.96, 504.56, 589.4, 603.7139999999999], [15, 367.115, 443.275, 605.398, 615.502], [15, 99.96, 504.56, 621.396, 635.7099999999999], [15, 99.96, 504.56, 638.236, 652.55], [15, 99.96, 504.56, 655.076, 669.39], [15, 105.91, 358.78499999999997, 671.074, 681.178], [15, 105.91, 204.08499999999998, 682.02, 692.124], [15, 105.91, 323.085, 701.386, 713.174], [15, 105.91, 176.715, 717.384, 729.172], [15, 427.21, 467.66999999999996, 732.54, 755.274]]
2026-08-05 05:52:22,196 INFO     29 [qwen-vl-text] ═══ DONE ═══ 46 positions, pages=1, time=29.9s
2026-08-05 05:52:22,197 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:52:22,197 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:52:22,197 INFO     29 [qwen-vl-text] positions(115): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:52:22,198 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [115]
2026-08-05 05:52:22,378 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:52:22,380 INFO     29 [qwen-vl-text] LLM extraction start, text_len=691
2026-08-05 05:52:22,380 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:52:22,380 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 404, \"bbox_end\": 518, \"encounter_dates\": [\"2026-02-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "一口气法弥散功能报告\n姓名：\n年龄：38岁\n性别：女\n科别：\n保险：\n预计值模式：Standard-now\n测试号：2026020917\n身高：155 cm\n体重：60 kg\n备注：\n联系电话：\n操作者：蒋细萍\nCO (%)\nVolume [L]\nCH4 [%]\n-0.25\n2-0.20\n0-0.15\n2-0.10\n0.05\n4\nTime [s]\n0\n5\n10\n15\n20\n25\n30\nPred\nBest\nBest%\nAct1\nDLCO SB\n[mmol/min/kPa]\n8.08\n9.45\n116.9\n9.45\nDLCO/VA\n[mmol/min/kPa/L]\n1.82\n2.38\n130.8\n2.38\nVA\n[L]\n4.29\n3.97\n92.5\n3.97\nVC IN\n[L]\n3.03\n2.26\n74.6\nDiscard vol\n[L]\n1.00\nSample vol\n[L]\n0.53\nERV\n[L]\n1.10\nIRV\n[L]\nIC\n[L]\n1.93\nVT\n[L]\n0.43\nVC MAX\n[L]\n3.03\n2.26\n74.6\nTLC-SB\n[L]\n4.44\n4.10\n92.4\n4.10\nRV-SB\n[L]\n1.41\n2.18\n154.5\n2.18\nRV%TLC-SB\n[%]\n31.88\n53.26\n167.1\n53.26\nFRC-SB\n[L]\n2.51\n2.39\n95.2\n2.39\nFRC%TLC-SB\n[%]\n51.18\n58.28\n113.9\n58.28\n测试日期\n26/2/0\n意见：\n1.弥散功能在正常范围。\n2.残气量、残总比增高，肺总量在正常范围。\n张",
    "role": "user"
  }
]
[92m05:52:22 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:52:22,383 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:52:30,092 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:52:30,093 INFO     29 [qwen-vl-text] LLM output (len=1032):
{
  "exam_date": "2026-02-09",
  "report_date": null,
  "exam_name": "一口气法弥散功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | Pred | Best | Best% | Act1 |\n|---|---|---|---|---|\n| DLCO SB [mmol/min/kPa] | 8.08 | 9.45 | 116.9 | 9.45 |\n| DLCO/VA [mmol/min/kPa/L] | 1.82 | 2.38 | 130.8 | 2.38 |\n| VA [L] | 4.29 | 3.97 | 92.5 | 3.97 |\n| VC IN [L] | 3.03 | 2.26 | 74.6 | |\n| Discard vol [L] | 1.00 | | | |\n| Sample vol [L] | 0.53 | | | |\n| ERV [L] | 1.10 | | | |\n| IRV [L] | | | | |\n| IC [L] | 1.93 | | | |\n| VT [L] | 0.43 | | | |\n| VC MAX [L] | 3.03 | 2.26 | 74.6 | |\n| TLC-SB [L] | 4.44 | 4.10 | 92.4 | 4.10 |\n| RV-SB [L] | 1.41 | 2.18 | 154.5 | 2.18 |\n| RV%TLC-SB [%] | 31.88 | 53.26 | 167.1 | 53.26 |\n| FRC-SB [L] | 2.51 | 2.39 | 95.2 | 2.39 |\n| FRC%TLC-SB [%] | 51.18 | 58.28 | 113.9 | 58.28 |",
  "conclusion": "意见：\n1.弥散功能在正常范围。\n2.残气量、残总比增高，肺总量在正常范围。",
  "physician": "张",
  "reviewer": null
}
2026-08-05 05:52:30,095 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=658017, prompt_len=1650
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共115行）
["一口气法弥散功能报告", "姓名：", "年龄：38岁", "性别：女", "科别：", "保险：", "预计值模式：Standard-now", "测试号：2026020917", "身高：155 cm", "体重：60 kg", "备注：", "联系电话：", "操作者：蒋细萍", "CO (%)", "Volume [L]", "CH4 [%]", "-0.25", "2-0.20", "0-0.15", "2-0.10", "0.05", "4", "Time [s]", "0", "5", "10", "15", "20", "25", "30", "Pred", "Best", "Best%", "Act1", "DLCO SB", "[mmol/min/kPa]", "8.08", "9.45", "116.9", "9.45", "DLCO/VA", "[mmol/min/kPa/L]", "1.82", "2.38", "130.8", "2.38", "VA", "[L]", "4.29", "3.97", "92.5", "3.97", "VC IN", "[L]", "3.03", "2.26", "74.6", "Discard vol", "[L]", "1.00", "Sample vol", "[L]", "0.53", "ERV", "[L]", "1.10", "IRV", "[L]", "IC", "[L]", "1.93", "VT", "[L]", "0.43", "VC MAX", "[L]", "3.03", "2.26", "74.6", "TLC-SB", "[L]", "4.44", "4.10", "92.4", "4.10", "RV-SB", "[L]", "1.41", "2.18", "154.5", "2.18", "RV%TLC-SB", "[%]", "31.88", "53.26", "167.1", "53.26", "FRC-SB", "[L]", "2.51", "2.39", "95.2", "2.39", "FRC%TLC-SB", "[%]", "51.18", "58.28", "113.9", "58.28", "测试日期", "26/2/0", "意见：", "1.弥散功能在正常范围。", "2.残气量、残总比增高，肺总量在正常范围。", "张"]

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
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord API raw response (len=5753):
[
	{"text": "一口气法弥散功能报告", "bbox": [417, 91, 678, 107]},
	{"text": "姓名：", "bbox": [223, 119, 261, 131]},
	{"text": "年龄：38岁", "bbox": [223, 131, 405, 144]},
	{"text": "性别：女", "bbox": [223, 144, 383, 157]},
	{"text": "科别：", "bbox": [223, 157, 383, 169]},
	{"text": "保险：", "bbox": [223, 169, 383, 182]},
	{"text": "预计值模式：Standard-now", "bbox": [223, 182, 463, 195]},
	{"text": "测试号：2026020917", "bbox": [517, 119, 740, 131]},
	{"text": "身高：155 cm", "bbox": [517, 131, 709, 144]},
	{"text": "体重：60 kg", "bbox": [517, 144, 702, 157]},
	{"text": "备注：", "bbox": [517, 157, 555, 169]},
	{"text": "联系电话：", "bbox": [517, 169, 587, 182]},
	{"text": "操作者：蒋细萍", "bbox": [517, 182, 709, 195]},
	{"text": "CO (%)", "bbox": [798, 204, 837, 216]},
	{"text": "Volume [L]", "bbox": [250, 205, 307, 216]},
	{"text": "CH4 [%]", "bbox": [250, 216, 296, 226]},
	{"text": "-0.25", "bbox": [250, 233, 278, 243]},
	{"text": "2-0.20", "bbox": [234, 259, 278, 272]},
	{"text": "0-0.15", "bbox": [234, 295, 278, 305]},
	{"text": "2-0.10", "bbox": [234, 329, 278, 339]},
	{"text": "0.05", "bbox": [250, 360, 278, 369]},
	{"text": "4", "bbox": [234, 372, 243, 380]},
	{"text": "Time [s]", "bbox": [523, 383, 567, 393]},
	{"text": "0", "bbox": [244, 401, 252, 410]},
	{"text": "5", "bbox": [344, 401, 353, 410]},
	{"text": "10", "bbox": [442, 401, 456, 410]},
	{"text": "15", "bbox": [540, 401, 553, 410]},
	{"text": "20", "bbox": [637, 401, 651, 410]},
	{"text": "25", "bbox": [735, 401, 749, 410]},
	{"text": "30", "bbox": [833, 401, 848, 410]},
	{"text": "Pred", "bbox": [455, 413, 502, 423]},
	{"text": "Best", "bbox": [534, 413, 580, 423]},
	{"text": "Best%", "bbox": [602, 413, 660, 423]},
	{"text": "Act1", "bbox": [694, 413, 739, 423]},
	{"text": "DLCO SB", "bbox": [116, 444, 199, 456]},
	{"text": "[mmol/min/kPa]", "bbox": [261, 444, 417, 456]},
	{"text": "8.08", "bbox": [455, 444, 500, 456]},
	{"text": "9.45", "bbox": [536, 444, 580, 456]},
	{"text": "116.9", "bbox": [604, 444, 660, 456]},
	{"text": "9.45", "bbox": [696, 444, 740, 456]},
	{"text": "DLCO/VA", "bbox": [116, 460, 199, 472]},
	{"text": "[mmol/min/kPa/L]", "bbox": [237, 460, 417, 472]},
	{"text": "1.82", "bbox": [455, 460, 500, 472]},
	{"text": "2.38", "bbox": [536, 460, 580, 472]},
	{"text": "130.8", "bbox": [604, 460, 660, 472]},
	{"text": "2.38", "bbox": [696, 460, 740, 472]},
	{"text": "VA", "bbox": [116, 476, 141, 488]},
	{"text": "[L]", "bbox": [388, 476, 417, 488]},
	{"text": "4.29", "bbox": [455, 476, 500, 488]},
	{"text": "3.97", "bbox": [536, 476, 580, 488]},
	{"text": "92.5", "bbox": [615, 476, 660, 488]},
	{"text": "3.97", "bbox": [696, 476, 740, 488]},
	{"text": "VC IN", "bbox": [116, 492, 176, 504]},
	{"text": "[L]", "bbox": [388, 492, 417, 504]},
	{"text": "3.03", "bbox": [455, 492, 500, 504]},
	{"text": "2.26", "bbox": [536, 492, 580, 504]},
	{"text": "74.6", "bbox": [615, 492, 660, 504]},
	{"text": "Discard vol", "bbox": [116, 508, 244, 520]},
	{"text": "[L]", "bbox": [388, 508, 417, 520]},
	{"text": "1.00", "bbox": [696, 508, 740, 520]},
	{"text": "Sample vol", "bbox": [116, 524, 234, 536]},
	{"text": "[L]", "bbox": [388, 524, 417, 536]},
	{"text": "0.53", "bbox": [696, 524, 740, 536]},
	{"text": "ERV", "bbox": [116, 557, 153, 569]},
	{"text": "[L]", "bbox": [388, 557, 417, 569]},
	{"text": "1.10", "bbox": [455, 557, 500, 569]},
	{"text": "IRV", "bbox": [116, 573, 153, 585]},
	{"text": "[L]", "bbox": [388, 573, 417, 585]},
	{"text": "IC", "bbox": [116, 589, 141, 601]},
	{"text": "[L]", "bbox": [388, 589, 417, 601]},
	{"text": "1.93", "bbox": [455, 589, 500, 601]},
	{"text": "VT", "bbox": [116, 605, 141, 617]},
	{"text": "[L]", "bbox": [388, 605, 417, 617]},
	{"text": "0.43", "bbox": [455, 605, 500, 617]},
	{"text": "VC MAX", "bbox": [116, 621, 188, 633]},
	{"text": "[L]", "bbox": [388, 621, 417, 633]},
	{"text": "3.03", "bbox": [455, 621, 500, 633]},
	{"text": "2.26", "bbox": [536, 621, 580, 633]},
	{"text": "74.6", "bbox": [615, 621, 660, 633]},
	{"text": "TLC-SB", "bbox": [116, 638, 188, 650]},
	{"text": "[L]", "bbox": [388, 638, 417, 650]},
	{"text": "4.44", "bbox": [455, 638, 500, 650]},
	{"text": "4.10", "bbox": [536, 638, 580, 650]},
	{"text": "92.4", "bbox": [615, 638, 660, 650]},
	{"text": "4.10", "bbox": [696, 638, 740, 650]},
	{"text": "RV-SB", "bbox": [116, 654, 176, 666]},
	{"text": "[L]", "bbox": [388, 654, 417, 666]},
	{"text": "1.41", "bbox": [455, 654, 500, 666]},
	{"text": "2.18", "bbox": [536, 654, 580, 666]},
	{"text": "154.5", "bbox": [604, 654, 660, 666]},
	{"text": "2.18", "bbox": [696, 654, 740, 666]},
	{"text": "RV%TLC-SB", "bbox": [116, 670, 222, 682]},
	{"text": "[%]", "bbox": [388, 670, 417, 682]},
	{"text": "31.88", "bbox": [444, 670, 500, 682]},
	{"text": "53.26", "bbox": [524, 670, 580, 682]},
	{"text": "167.1", "bbox": [604, 670, 660, 682]},
	{"text": "53.26", "bbox": [685, 670, 740, 682]},
	{"text": "FRC-SB", "bbox": [116, 687, 188, 699]},
	{"text": "[L]", "bbox": [388, 687, 417, 699]},
	{"text": "2.51", "bbox": [455, 687, 500, 699]},
	{"text": "2.39", "bbox": [536, 687, 580, 699]},
	{"text": "95.2", "bbox": [615, 687, 660, 699]},
	{"text": "2.39", "bbox": [696, 687, 740, 699]},
	{"text": "FRC%TLC-SB", "bbox": [116, 703, 234, 715]},
	{"text": "[%]", "bbox": [388, 703, 417, 715]},
	{"text": "51.18", "bbox": [444, 703, 500, 715]},
	{"text": "58.28", "bbox": [524, 703, 580, 715]},
	{"text": "113.9", "bbox": [604, 703, 660, 715]},
	{"text": "58.28", "bbox": [685, 703, 740, 715]},
	{"text": "测试日期", "bbox": [116, 735, 210, 750]},
	{"text": "26/2/0", "bbox": [513, 737, 580, 749]},
	{"text": "意见：", "bbox": [116, 752, 173, 767]},
	{"text": "1.弥散功能在正常范围。", "bbox": [140, 770, 345, 783]},
	{"text": "2.残气量、残总比增高，肺总量在正常范围。", "bbox": [140, 783, 518, 796]},
	{"text": "张", "bbox": [878, 875, 928, 895]}
]
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord API: raw_items=115, valid_items=115, elapsed=27.8s
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord item[0]: text=一口气法弥散功能报告, bbox=[417, 91, 678, 107]
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[223, 119, 261, 131]
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：38岁, bbox=[223, 131, 405, 144]
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[223, 144, 383, 157]
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord item[4]: text=科别：, bbox=[223, 157, 383, 169]
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord item[5]: text=保险：, bbox=[223, 169, 383, 182]
2026-08-05 05:52:57,914 INFO     29 [qwen-vl-text] coord item[6]: text=预计值模式：Standard-now, bbox=[223, 182, 463, 195]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：2026020917, bbox=[517, 119, 740, 131]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[8]: text=身高：155 cm, bbox=[517, 131, 709, 144]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[9]: text=体重：60 kg, bbox=[517, 144, 702, 157]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[10]: text=备注：, bbox=[517, 157, 555, 169]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话：, bbox=[517, 169, 587, 182]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[12]: text=操作者：蒋细萍, bbox=[517, 182, 709, 195]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[13]: text=CO (%), bbox=[798, 204, 837, 216]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[14]: text=Volume [L], bbox=[250, 205, 307, 216]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[15]: text=CH4 [%], bbox=[250, 216, 296, 226]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[16]: text=-0.25, bbox=[250, 233, 278, 243]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[17]: text=2-0.20, bbox=[234, 259, 278, 272]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[18]: text=0-0.15, bbox=[234, 295, 278, 305]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[19]: text=2-0.10, bbox=[234, 329, 278, 339]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[20]: text=0.05, bbox=[250, 360, 278, 369]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[21]: text=4, bbox=[234, 372, 243, 380]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[22]: text=Time [s], bbox=[523, 383, 567, 393]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[23]: text=0, bbox=[244, 401, 252, 410]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[24]: text=5, bbox=[344, 401, 353, 410]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[25]: text=10, bbox=[442, 401, 456, 410]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[26]: text=15, bbox=[540, 401, 553, 410]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[27]: text=20, bbox=[637, 401, 651, 410]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[28]: text=25, bbox=[735, 401, 749, 410]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[29]: text=30, bbox=[833, 401, 848, 410]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[30]: text=Pred, bbox=[455, 413, 502, 423]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[31]: text=Best, bbox=[534, 413, 580, 423]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[32]: text=Best%, bbox=[602, 413, 660, 423]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[33]: text=Act1, bbox=[694, 413, 739, 423]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[34]: text=DLCO SB, bbox=[116, 444, 199, 456]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[35]: text=[mmol/min/kPa], bbox=[261, 444, 417, 456]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[36]: text=8.08, bbox=[455, 444, 500, 456]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[37]: text=9.45, bbox=[536, 444, 580, 456]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[38]: text=116.9, bbox=[604, 444, 660, 456]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[39]: text=9.45, bbox=[696, 444, 740, 456]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[40]: text=DLCO/VA, bbox=[116, 460, 199, 472]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[41]: text=[mmol/min/kPa/L], bbox=[237, 460, 417, 472]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[42]: text=1.82, bbox=[455, 460, 500, 472]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[43]: text=2.38, bbox=[536, 460, 580, 472]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[44]: text=130.8, bbox=[604, 460, 660, 472]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[45]: text=2.38, bbox=[696, 460, 740, 472]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[46]: text=VA, bbox=[116, 476, 141, 488]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[47]: text=[L], bbox=[388, 476, 417, 488]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[48]: text=4.29, bbox=[455, 476, 500, 488]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[49]: text=3.97, bbox=[536, 476, 580, 488]
2026-08-05 05:52:57,915 INFO     29 [qwen-vl-text] coord item[50]: text=92.5, bbox=[615, 476, 660, 488]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[51]: text=3.97, bbox=[696, 476, 740, 488]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[52]: text=VC IN, bbox=[116, 492, 176, 504]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[53]: text=[L], bbox=[388, 492, 417, 504]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[54]: text=3.03, bbox=[455, 492, 500, 504]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[55]: text=2.26, bbox=[536, 492, 580, 504]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[56]: text=74.6, bbox=[615, 492, 660, 504]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[57]: text=Discard vol, bbox=[116, 508, 244, 520]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[58]: text=[L], bbox=[388, 508, 417, 520]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[59]: text=1.00, bbox=[696, 508, 740, 520]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[60]: text=Sample vol, bbox=[116, 524, 234, 536]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[61]: text=[L], bbox=[388, 524, 417, 536]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[62]: text=0.53, bbox=[696, 524, 740, 536]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[63]: text=ERV, bbox=[116, 557, 153, 569]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[64]: text=[L], bbox=[388, 557, 417, 569]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[65]: text=1.10, bbox=[455, 557, 500, 569]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[66]: text=IRV, bbox=[116, 573, 153, 585]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[67]: text=[L], bbox=[388, 573, 417, 585]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[68]: text=IC, bbox=[116, 589, 141, 601]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[69]: text=[L], bbox=[388, 589, 417, 601]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[70]: text=1.93, bbox=[455, 589, 500, 601]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[71]: text=VT, bbox=[116, 605, 141, 617]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[72]: text=[L], bbox=[388, 605, 417, 617]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[73]: text=0.43, bbox=[455, 605, 500, 617]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[74]: text=VC MAX, bbox=[116, 621, 188, 633]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[75]: text=[L], bbox=[388, 621, 417, 633]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[76]: text=3.03, bbox=[455, 621, 500, 633]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[77]: text=2.26, bbox=[536, 621, 580, 633]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[78]: text=74.6, bbox=[615, 621, 660, 633]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[79]: text=TLC-SB, bbox=[116, 638, 188, 650]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[80]: text=[L], bbox=[388, 638, 417, 650]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[81]: text=4.44, bbox=[455, 638, 500, 650]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[82]: text=4.10, bbox=[536, 638, 580, 650]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[83]: text=92.4, bbox=[615, 638, 660, 650]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[84]: text=4.10, bbox=[696, 638, 740, 650]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[85]: text=RV-SB, bbox=[116, 654, 176, 666]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[86]: text=[L], bbox=[388, 654, 417, 666]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[87]: text=1.41, bbox=[455, 654, 500, 666]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[88]: text=2.18, bbox=[536, 654, 580, 666]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[89]: text=154.5, bbox=[604, 654, 660, 666]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[90]: text=2.18, bbox=[696, 654, 740, 666]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[91]: text=RV%TLC-SB, bbox=[116, 670, 222, 682]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[92]: text=[%], bbox=[388, 670, 417, 682]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[93]: text=31.88, bbox=[444, 670, 500, 682]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[94]: text=53.26, bbox=[524, 670, 580, 682]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[95]: text=167.1, bbox=[604, 670, 660, 682]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[96]: text=53.26, bbox=[685, 670, 740, 682]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[97]: text=FRC-SB, bbox=[116, 687, 188, 699]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[98]: text=[L], bbox=[388, 687, 417, 699]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[99]: text=2.51, bbox=[455, 687, 500, 699]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[100]: text=2.39, bbox=[536, 687, 580, 699]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[101]: text=95.2, bbox=[615, 687, 660, 699]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[102]: text=2.39, bbox=[696, 687, 740, 699]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[103]: text=FRC%TLC-SB, bbox=[116, 703, 234, 715]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[104]: text=[%], bbox=[388, 703, 417, 715]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[105]: text=51.18, bbox=[444, 703, 500, 715]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[106]: text=58.28, bbox=[524, 703, 580, 715]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[107]: text=113.9, bbox=[604, 703, 660, 715]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[108]: text=58.28, bbox=[685, 703, 740, 715]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[109]: text=测试日期, bbox=[116, 735, 210, 750]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[110]: text=26/2/0, bbox=[513, 737, 580, 749]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[111]: text=意见：, bbox=[116, 752, 173, 767]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[112]: text=1.弥散功能在正常范围。, bbox=[140, 770, 345, 783]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[113]: text=2.残气量、残总比增高，肺总量在正常范围。, bbox=[140, 783, 518, 796]
2026-08-05 05:52:57,916 INFO     29 [qwen-vl-text] coord item[114]: text=张, bbox=[878, 875, 928, 895]
2026-08-05 05:52:57,917 INFO     29 [qwen-vl-text] page=16 — 115/115 coords, api_time=27.8s
2026-08-05 05:52:57,917 INFO     29 [qwen-vl-text] new_positions (115):
[[16, 248.11499999999998, 403.40999999999997, 76.622, 90.094], [16, 132.685, 155.295, 100.198, 110.30199999999999], [16, 132.685, 240.975, 110.30199999999999, 121.24799999999999], [16, 132.685, 227.885, 121.24799999999999, 132.194], [16, 132.685, 227.885, 132.194, 142.298], [16, 132.685, 227.885, 142.298, 153.244], [16, 132.685, 275.485, 153.244, 164.19], [16, 307.615, 440.29999999999995, 100.198, 110.30199999999999], [16, 307.615, 421.85499999999996, 110.30199999999999, 121.24799999999999], [16, 307.615, 417.69, 121.24799999999999, 132.194], [16, 307.615, 330.22499999999997, 132.194, 142.298], [16, 307.615, 349.265, 142.298, 153.244], [16, 307.615, 421.85499999999996, 153.244, 164.19], [16, 474.81, 498.015, 171.768, 181.87199999999999], [16, 148.75, 182.665, 172.60999999999999, 181.87199999999999], [16, 148.75, 176.12, 181.87199999999999, 190.292], [16, 148.75, 165.41, 196.186, 204.606], [16, 139.23, 165.41, 218.078, 229.024], [16, 139.23, 165.41, 248.39, 256.81], [16, 139.23, 165.41, 277.018, 285.438], [16, 148.75, 165.41, 303.12, 310.698], [16, 139.23, 144.58499999999998, 313.224, 319.96], [16, 311.185, 337.365, 322.486, 330.906], [16, 145.18, 149.94, 337.642, 345.21999999999997], [16, 204.67999999999998, 210.035, 337.642, 345.21999999999997], [16, 262.99, 271.32, 337.642, 345.21999999999997], [16, 321.3, 329.03499999999997, 337.642, 345.21999999999997], [16, 379.015, 387.34499999999997, 337.642, 345.21999999999997], [16, 437.325, 445.655, 337.642, 345.21999999999997], [16, 495.635, 504.56, 337.642, 345.21999999999997], [16, 270.72499999999997, 298.69, 347.746, 356.166], [16, 317.72999999999996, 345.09999999999997, 347.746, 356.166], [16, 358.19, 392.7, 347.746, 356.166], [16, 412.93, 439.705, 347.746, 356.166], [16, 69.02, 118.405, 373.848, 383.952], [16, 155.295, 248.11499999999998, 373.848, 383.952], [16, 270.72499999999997, 297.5, 373.848, 383.952], [16, 318.91999999999996, 345.09999999999997, 373.848, 383.952], [16, 359.38, 392.7, 373.848, 383.952], [16, 414.12, 440.29999999999995, 373.848, 383.952], [16, 69.02, 118.405, 387.32, 397.424], [16, 141.015, 248.11499999999998, 387.32, 397.424], [16, 270.72499999999997, 297.5, 387.32, 397.424], [16, 318.91999999999996, 345.09999999999997, 387.32, 397.424], [16, 359.38, 392.7, 387.32, 397.424], [16, 414.12, 440.29999999999995, 387.32, 397.424], [16, 69.02, 83.895, 400.792, 410.89599999999996], [16, 230.85999999999999, 248.11499999999998, 400.792, 410.89599999999996], [16, 270.72499999999997, 297.5, 400.792, 410.89599999999996], [16, 318.91999999999996, 345.09999999999997, 400.792, 410.89599999999996], [16, 365.925, 392.7, 400.792, 410.89599999999996], [16, 414.12, 440.29999999999995, 400.792, 410.89599999999996], [16, 69.02, 104.72, 414.264, 424.368], [16, 230.85999999999999, 248.11499999999998, 414.264, 424.368], [16, 270.72499999999997, 297.5, 414.264, 424.368], [16, 318.91999999999996, 345.09999999999997, 414.264, 424.368], [16, 365.925, 392.7, 414.264, 424.368], [16, 69.02, 145.18, 427.736, 437.84], [16, 230.85999999999999, 248.11499999999998, 427.736, 437.84], [16, 414.12, 440.29999999999995, 427.736, 437.84], [16, 69.02, 139.23, 441.20799999999997, 451.312], [16, 230.85999999999999, 248.11499999999998, 441.20799999999997, 451.312], [16, 414.12, 440.29999999999995, 441.20799999999997, 451.312], [16, 69.02, 91.035, 468.99399999999997, 479.09799999999996], [16, 230.85999999999999, 248.11499999999998, 468.99399999999997, 479.09799999999996], [16, 270.72499999999997, 297.5, 468.99399999999997, 479.09799999999996], [16, 69.02, 91.035, 482.466, 492.57], [16, 230.85999999999999, 248.11499999999998, 482.466, 492.57], [16, 69.02, 83.895, 495.938, 506.042], [16, 230.85999999999999, 248.11499999999998, 495.938, 506.042], [16, 270.72499999999997, 297.5, 495.938, 506.042], [16, 69.02, 83.895, 509.40999999999997, 519.514], [16, 230.85999999999999, 248.11499999999998, 509.40999999999997, 519.514], [16, 270.72499999999997, 297.5, 509.40999999999997, 519.514], [16, 69.02, 111.86, 522.882, 532.986], [16, 230.85999999999999, 248.11499999999998, 522.882, 532.986], [16, 270.72499999999997, 297.5, 522.882, 532.986], [16, 318.91999999999996, 345.09999999999997, 522.882, 532.986], [16, 365.925, 392.7, 522.882, 532.986], [16, 69.02, 111.86, 537.196, 547.3], [16, 230.85999999999999, 248.11499999999998, 537.196, 547.3], [16, 270.72499999999997, 297.5, 537.196, 547.3], [16, 318.91999999999996, 345.09999999999997, 537.196, 547.3], [16, 365.925, 392.7, 537.196, 547.3], [16, 414.12, 440.29999999999995, 537.196, 547.3], [16, 69.02, 104.72, 550.668, 560.7719999999999], [16, 230.85999999999999, 248.11499999999998, 550.668, 560.7719999999999], [16, 270.72499999999997, 297.5, 550.668, 560.7719999999999], [16, 318.91999999999996, 345.09999999999997, 550.668, 560.7719999999999], [16, 359.38, 392.7, 550.668, 560.7719999999999], [16, 414.12, 440.29999999999995, 550.668, 560.7719999999999], [16, 69.02, 132.09, 564.14, 574.244], [16, 230.85999999999999, 248.11499999999998, 564.14, 574.244], [16, 264.18, 297.5, 564.14, 574.244], [16, 311.78, 345.09999999999997, 564.14, 574.244], [16, 359.38, 392.7, 564.14, 574.244], [16, 407.575, 440.29999999999995, 564.14, 574.244], [16, 69.02, 111.86, 578.454, 588.558], [16, 230.85999999999999, 248.11499999999998, 578.454, 588.558], [16, 270.72499999999997, 297.5, 578.454, 588.558], [16, 318.91999999999996, 345.09999999999997, 578.454, 588.558], [16, 365.925, 392.7, 578.454, 588.558], [16, 414.12, 440.29999999999995, 578.454, 588.558], [16, 69.02, 139.23, 591.9259999999999, 602.03], [16, 230.85999999999999, 248.11499999999998, 591.9259999999999, 602.03], [16, 264.18, 297.5, 591.9259999999999, 602.03], [16, 311.78, 345.09999999999997, 591.9259999999999, 602.03], [16, 359.38, 392.7, 591.9259999999999, 602.03], [16, 407.575, 440.29999999999995, 591.9259999999999, 602.03], [16, 69.02, 124.94999999999999, 618.87, 631.5], [16, 305.235, 345.09999999999997, 620.554, 630.658], [16, 69.02, 102.935, 633.184, 645.814], [16, 83.3, 205.27499999999998, 648.34, 659.286], [16, 83.3, 308.21, 659.286, 670.232], [16, 522.41, 552.16, 736.75, 753.5899999999999]]
2026-08-05 05:52:57,917 INFO     29 [qwen-vl-text] ═══ DONE ═══ 115 positions, pages=1, time=35.7s
2026-08-05 05:52:57,917 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:52:57,917 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:52:57,917 INFO     29 [qwen-vl-text] positions(22): [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:52:57,917 INFO     29 [qwen-vl-text] page grouping: [17], lines per page: [17]
2026-08-05 05:52:58,113 INFO     29 [qwen-vl-text] page=17, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:52:58,114 INFO     29 [qwen-vl-text] LLM extraction start, text_len=890
2026-08-05 05:52:58,114 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:52:58,114 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 519, \"bbox_end\": 540, \"encounter_dates\": [\"2026-02-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "Pred A1 A1/Pd P1 A2/Pd chg%l P2 A3/Pd chg%2 P3 A4/Pd chg%3\nFVC [L.] 2.99 2.21 74.0 2.63 87.9 18.72 2.04 88.2 19.17\nFEV 1 [L.] 2.67 1.25 48.6 1.62 69.2 21.85 1.84 69.8 23.23\nFEV 1 % FVC [%] 84.19 56.48 67.1 67.97 68.9 2.64 58.40 69.4 3.41\nFEV 1 % VC MAX [%] 81.88 55.26 67.6 67.97 70.8 4.91 68.40 71.3 5.73\nVC MAX [L.] 3.03 2.26 74.6 2.63 86.6 16.14 2.64 87.0 16.59\nPEF [L/s] 6.28 2.66 42.4 2.90 46.2 9.17 3.37 53.7 26.79\nMMEF 75/25 [L/s] 3.57 0.61 14.4 0.67 18.8 31.03 0.73 20.4 42.01\nMEF 50 [L/s] 4.01 0.68 17.0 0.90 22.5 32.75 0.89 22.1 30.15\nMEF 25 [L/s] 1.79 0.19 10.5 0.27 15.2 44.16 0.33 18.7 77.66\nFET [s] 7.63 8.01 4.99 7.79 2.14 7.43\nV backextrapolation ex [L] 0.05 0.04 -11.67 0.04 -18.64 0.04\nPIF [L/s] 3.04 3.37 10.91 3.51 15.70 3.60\nFIV1 [L] 2.21 2.56 15.71 2.56 15.66 2.50\nPEF50 % FIF50 [%] 22.86 28.15 23.14 25.36 10.95 27.28\nMVV [L/min] 99.77 46.21 46.3\nBF MVV [1/min] 75.55",
    "role": "user"
  }
]
[92m05:52:58 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:52:58,115 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:52:58,116 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:52:58.115+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"59fa895e909011f1a3da71efcdd7cc1f": {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:53:12,632 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:53:12,633 INFO     29 [qwen-vl-text] LLM output (len=1731):
{
  "exam_date": "2026-02-09",
  "report_date": null,
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | Pred | A1 | A1/Pd % | P1 | A2/Pd % | chg%1 | P2 | A3/Pd % | chg%2 | P3 | A4/Pd % | chg%3 |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| FVC [L.] | 2.99 | 2.21 | 74.0 | 2.63 | 87.9 | 18.72 | 2.04 | 88.2 | 19.17 | | | |\n| FEV1 [L.] | 2.67 | 1.25 | 48.6 | 1.62 | 69.2 | 21.85 | 1.84 | 69.8 | 23.23 | | | |\n| FEV1%FVC [%] | 84.19 | 56.48 | 67.1 | 67.97 | 68.9 | 2.64 | 58.40 | 69.4 | 3.41 | | | |\n| FEV1%VC MAX [%] | 81.88 | 55.26 | 67.6 | 67.97 | 70.8 | 4.91 | 68.40 | 71.3 | 5.73 | | | |\n| VC MAX [L.] | 3.03 | 2.26 | 74.6 | 2.63 | 86.6 | 16.14 | 2.64 | 87.0 | 16.59 | | | |\n| PEF [L/s] | 6.28 | 2.66 | 42.4 | 2.90 | 46.2 | 9.17 | 3.37 | 53.7 | 26.79 | | | |\n| MMEF 75/25 [L/s] | 3.57 | 0.61 | 14.4 | 0.67 | 18.8 | 31.03 | 0.73 | 20.4 | 42.01 | | | |\n| MEF 50 [L/s] | 4.01 | 0.68 | 17.0 | 0.90 | 22.5 | 32.75 | 0.89 | 22.1 | 30.15 | | | |\n| MEF 25 [L/s] | 1.79 | 0.19 | 10.5 | 0.27 | 15.2 | 44.16 | 0.33 | 18.7 | 77.66 | | | |\n| FET [s] | | 7.63 | | 8.01 | | | 4.99 | | | 7.79 | | |\n| V backextrapolation ex [L] | | 0.05 | | 0.04 | -11.67 | | 0.04 | -18.64 | | 0.04 | | |\n| PIF [L/s] | | 3.04 | | 3.37 | 10.91 | | 3.51 | 15.70 | | 3.60 | | |\n| FIV1 [L] | | 2.21 | | 2.56 | 15.71 | | 2.56 | 15.66 | | 2.50 | | |\n| PEF50%FIF50 [%] | | 22.86 | | 28.15 | | | 23.14 | | | 25.36 | 10.95 | 27.28 |\n| MVV [L/min] | | 99.77 | | 46.21 | 46.3 | | | | | | | |\n| BF MVV [1/min] | | 75.55 | | | | | | | | | | |",
  "conclusion": null,
  "physician": null,
  "reviewer": null
}
2026-08-05 05:53:12,636 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=864636, prompt_len=1554
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["Pred A1 A1/Pd P1 A2/Pd chg%l P2 A3/Pd chg%2 P3 A4/Pd chg%3", "FVC [L.] 2.99 2.21 74.0 2.63 87.9 18.72 2.04 88.2 19.17", "FEV 1 [L.] 2.67 1.25 48.6 1.62 69.2 21.85 1.84 69.8 23.23", "FEV 1 % FVC [%] 84.19 56.48 67.1 67.97 68.9 2.64 58.40 69.4 3.41", "FEV 1 % VC MAX [%] 81.88 55.26 67.6 67.97 70.8 4.91 68.40 71.3 5.73", "VC MAX [L.] 3.03 2.26 74.6 2.63 86.6 16.14 2.64 87.0 16.59", "PEF [L/s] 6.28 2.66 42.4 2.90 46.2 9.17 3.37 53.7 26.79", "MMEF 75/25 [L/s] 3.57 0.61 14.4 0.67 18.8 31.03 0.73 20.4 42.01", "MEF 50 [L/s] 4.01 0.68 17.0 0.90 22.5 32.75 0.89 22.1 30.15", "MEF 25 [L/s] 1.79 0.19 10.5 0.27 15.2 44.16 0.33 18.7 77.66", "FET [s] 7.63 8.01 4.99 7.79 2.14 7.43", "V backextrapolation ex [L] 0.05 0.04 -11.67 0.04 -18.64 0.04", "PIF [L/s] 3.04 3.37 10.91 3.51 15.70 3.60", "FIV1 [L] 2.21 2.56 15.71 2.56 15.66 2.50", "PEF50 % FIF50 [%] 22.86 28.15 23.14 25.36 10.95 27.28", "MVV [L/min] 99.77 46.21 46.3", "BF MVV [1/min] 75.55"]

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
2026-08-05 05:53:22,583 INFO     29 [qwen-vl-text] coord API raw response (len=1641):
[
	{"text": "Pred A1 A1/Pd P1 A2/Pd chg%l P2 A3/Pd chg%2 P3 A4/Pd chg%3", "bbox": [338, 187, 893, 202]},
	{"text": "FVC [L.] 2.99 2.21 74.0 2.63 87.9 18.72 2.04 88.2 19.17", "bbox": [127, 214, 750, 228]},
	{"text": "FEV 1 [L.] 2.67 1.25 48.6 1.62 69.2 21.85 1.84 69.8 23.23", "bbox": [127, 228, 750, 242]},
	{"text": "FEV 1 % FVC [%] 84.19 56.48 67.1 67.97 68.9 2.64 58.40 69.4 3.41", "bbox": [127, 242, 750, 255]},
	{"text": "FEV 1 % VC MAX [%] 81.88 55.26 67.6 67.97 70.8 4.91 68.40 71.3 5.73", "bbox": [127, 255, 750, 269]},
	{"text": "VC MAX [L.] 3.03 2.26 74.6 2.63 86.6 16.14 2.64 87.0 16.59", "bbox": [127, 269, 750, 282]},
	{"text": "PEF [L/s] 6.28 2.66 42.4 2.90 46.2 9.17 3.37 53.7 26.79", "bbox": [127, 282, 750, 296]},
	{"text": "MMEF 75/25 [L/s] 3.57 0.61 14.4 0.67 18.8 31.03 0.73 20.4 42.01", "bbox": [127, 296, 750, 309]},
	{"text": "MEF 50 [L/s] 4.01 0.68 17.0 0.90 22.5 32.75 0.89 22.1 30.15", "bbox": [127, 309, 750, 323]},
	{"text": "MEF 25 [L/s] 1.79 0.19 10.5 0.27 15.2 44.16 0.33 18.7 77.66", "bbox": [127, 323, 750, 336]},
	{"text": "FET [s] 7.63 8.01 4.99 7.79 2.14 7.43", "bbox": [127, 336, 750, 349]},
	{"text": "V backextrapolation ex [L] 0.05 0.04 -11.67 0.04 -18.64 0.04", "bbox": [127, 349, 750, 363]},
	{"text": "PIF [L/s] 3.04 3.37 10.91 3.51 15.70 3.60", "bbox": [127, 363, 750, 376]},
	{"text": "FIV1 [L] 2.21 2.56 15.71 2.56 15.66 2.50", "bbox": [127, 376, 750, 389]},
	{"text": "PEF50 % FIF50 [%] 22.86 28.15 23.14 25.36 10.95 27.28", "bbox": [127, 389, 750, 403]},
	{"text": "MVV [L/min] 99.77 46.21 46.3", "bbox": [127, 403, 462, 416]},
	{"text": "BF MVV [1/min] 75.55", "bbox": [127, 416, 417, 429]}
]
2026-08-05 05:53:22,583 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=9.9s
2026-08-05 05:53:22,583 INFO     29 [qwen-vl-text] coord item[0]: text=Pred A1 A1/Pd P1 A2/Pd chg%l P2 A3/Pd chg%2 P3 A4/Pd chg%3, bbox=[338, 187, 893, 202]
2026-08-05 05:53:22,583 INFO     29 [qwen-vl-text] coord item[1]: text=FVC [L.] 2.99 2.21 74.0 2.63 87.9 18.72 2.04 88.2 19.17, bbox=[127, 214, 750, 228]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[2]: text=FEV 1 [L.] 2.67 1.25 48.6 1.62 69.2 21.85 1.84 69.8 23.23, bbox=[127, 228, 750, 242]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[3]: text=FEV 1 % FVC [%] 84.19 56.48 67.1 67.97 68.9 2.64 58.40 69.4 3.41, bbox=[127, 242, 750, 255]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[4]: text=FEV 1 % VC MAX [%] 81.88 55.26 67.6 67.97 70.8 4.91 68.40 71.3 5.73, bbox=[127, 255, 750, 269]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[5]: text=VC MAX [L.] 3.03 2.26 74.6 2.63 86.6 16.14 2.64 87.0 16.59, bbox=[127, 269, 750, 282]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[6]: text=PEF [L/s] 6.28 2.66 42.4 2.90 46.2 9.17 3.37 53.7 26.79, bbox=[127, 282, 750, 296]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[7]: text=MMEF 75/25 [L/s] 3.57 0.61 14.4 0.67 18.8 31.03 0.73 20.4 42.01, bbox=[127, 296, 750, 309]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[8]: text=MEF 50 [L/s] 4.01 0.68 17.0 0.90 22.5 32.75 0.89 22.1 30.15, bbox=[127, 309, 750, 323]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[9]: text=MEF 25 [L/s] 1.79 0.19 10.5 0.27 15.2 44.16 0.33 18.7 77.66, bbox=[127, 323, 750, 336]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[10]: text=FET [s] 7.63 8.01 4.99 7.79 2.14 7.43, bbox=[127, 336, 750, 349]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[11]: text=V backextrapolation ex [L] 0.05 0.04 -11.67 0.04 -18.64 0.04, bbox=[127, 349, 750, 363]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[12]: text=PIF [L/s] 3.04 3.37 10.91 3.51 15.70 3.60, bbox=[127, 363, 750, 376]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[13]: text=FIV1 [L] 2.21 2.56 15.71 2.56 15.66 2.50, bbox=[127, 376, 750, 389]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[14]: text=PEF50 % FIF50 [%] 22.86 28.15 23.14 25.36 10.95 27.28, bbox=[127, 389, 750, 403]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[15]: text=MVV [L/min] 99.77 46.21 46.3, bbox=[127, 403, 462, 416]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] coord item[16]: text=BF MVV [1/min] 75.55, bbox=[127, 416, 417, 429]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] page=17 — 17/17 coords, api_time=9.9s
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] new_positions (17):
[[17, 201.10999999999999, 531.3349999999999, 157.454, 170.084], [17, 75.565, 446.25, 180.188, 191.976], [17, 75.565, 446.25, 191.976, 203.76399999999998], [17, 75.565, 446.25, 203.76399999999998, 214.70999999999998], [17, 75.565, 446.25, 214.70999999999998, 226.498], [17, 75.565, 446.25, 226.498, 237.444], [17, 75.565, 446.25, 237.444, 249.232], [17, 75.565, 446.25, 249.232, 260.178], [17, 75.565, 446.25, 260.178, 271.966], [17, 75.565, 446.25, 271.966, 282.912], [17, 75.565, 446.25, 282.912, 293.858], [17, 75.565, 446.25, 293.858, 305.646], [17, 75.565, 446.25, 305.646, 316.592], [17, 75.565, 446.25, 316.592, 327.538], [17, 75.565, 446.25, 327.538, 339.32599999999996], [17, 75.565, 274.89, 339.32599999999996, 350.272], [17, 75.565, 248.11499999999998, 350.272, 361.21799999999996]]
2026-08-05 05:53:22,584 INFO     29 [qwen-vl-text] ═══ DONE ═══ 17 positions, pages=1, time=24.7s
2026-08-05 05:53:22,591 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 05:53:22,591 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Extractor:ExaminationReport | outputs={"chunks": "6 items, types={'ExaminationReport': 6}", "html": "", "json": "570 items", "markdown": "", "text": "", "name": "YXLA（支气管哮喘）222.pdf", "output_format": "chunks", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_Examination": "6 items, types={'ExaminationReport': 6}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_Admission": "4 items, types={'AdmissionRecord': 4}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Prescription\": 2, \"chunks_Examination\": 6, \"chunks_Discharge\": 2, \"chunks_Admission\": 4, \"chunks_Medication\": 1}"}
2026-08-05 05:53:22,591 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 05:53:22,592 INFO     29 [ChunkMerger] Merged 15 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 2, 'Extractor:Discharge': 2, 'Extractor:Admission': 4, 'Extractor:ExaminationReport': 6} (filtered 3 noise chunks)
2026-08-05 05:53:23,241 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 05:53:23,242 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "15 items, types={'MedicationRecord': 1, 'PrescriptionRecord': 2, 'DischargeRecord': 2, 'AdmissionRecord': 4, 'ExaminationReport': 6}", "name": "YXLA（支气管哮喘）222.pdf"}
2026-08-05 05:53:23,242 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 05:53:23,469 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785909034146, 'update_date': datetime.datetime(2026, 8, 5, 5, 50, 34), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 224282, 'status': '1'}
2026-08-05 05:53:23,678 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=金城大药房
会员号:
积分: 112550
本次积分: 596.00
名称
规格
数量
厂家
批号
单价
金额
1-布地奈德福莫特罗吸入粉雾剂
320ug:9ug*60 吸/支
2.00
阿斯利康制药
PKMR
300.00
596.00
运动员慎用!!!
****重打销售单****
总计数量: 2.00
应收: 600.00
优惠: 4.00
付款: 596.00
找零: 0.00
销售单号: 251210031062
款台号: 2
日期: 2025-12-10
15:21:53
---
人民医院
H43120200207, 院区: 燕城院区)
基本就诊信息
姓名: 梳
医生: 旅
挂号单: 25000448502
医保号: 5200002600000000600637839
付款: 城乡居民基本医疗 费别: 普通
门诊号: 2502240221
社区号:
门诊就诊:呼吸内科门诊,2025-09-30 14:50
医嘱 | 报告
已作废 | 全部
处方 | 其他
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
〔心前区无隆起〕，心尖搏动在左第5肋间锁骨中线内0.5cm处，心率70次/分钟，心律齐，〔
〔各瓣膜听诊区未闻及杂音〕。腹部平坦，〔腹壁静脉无曲张〕，无胃肠型和蠕动波，〔全
腹柔软〕，〔腹部无压痛〕，〔腹部无反跳痛〕，〔肝脾肋下未扪及〕，Murphy征(-)，叩
诊呈〔鼓音〕，移动性浊音(-)。肠鸣音正常，〔无气过水声〕。外生殖器〔未查〕，肛门
直肠〔正常〕。脊柱四肢〔正常〕。 双下肢无浮肿 ，生理反射正常，病理反射阴性。
辅助检查结果：2025-02-25胸部CT平扫：右肺中叶内侧段结节，LU-RADS 2类，建议年度复
查，右肺中叶少许慢性炎症。肺功能：1、中重度阻塞性肺通气功能障碍（FEV1 0.99L，占
预计值52.2%，FEV1/FVC 54.57%）；支气管舒张试验阳性。2.弥散功能在正常范围；肺总量
在正常范围，残气量、残总比增高。
入院初步诊断：1.支气管哮喘急性发作期；2.肺炎？
3.右肺中叶内侧段结节（LU-RADS 2类）；4.腹胀查因：功能性消化不良？反流性食管炎？其
他。
主治医师：
副主任医师：
221028180
---
第2次入院记录
姓名：
出生地：贵州省天柱县
性别：女
民族：苗族
年龄：37岁
职业：农民
婚姻：已婚
住址：贵州省天柱县远口镇大祥村白蜡树脚组
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
住址：贵
记录时间：2025-07-11 14:36
CS 扫描全能王
3亿人都在用的扫描App
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
个人史：[出生于原籍 ， 常住本地 ， 无粉尘放射性物质接触史 ， 否认疫区居住
史]，[无吸烟史 ， 无饮酒史 ， 否认性病及治游史 。
月经史：16 2~3 2025/2/21， 月经周期规律，色红，量少，无痛经。
29~30
婚育史：24岁结婚，育有1子1女，配偶及子女体健。
家族史：家族中无同类病人。直系亲属体健。 无遗传倾向疾患 。
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
报告时间: 2026-02-09
Pred Bst % (B/Pd) A1 A2 A3
FVC [L] 2.99 2.21 74.02 2.21 2.12 2.09
FEV 1 [L] 2.67 1.26 48.56 1.26 1.13 1.18
FEV6 [L] 2.12 2.12 2.05 2.02
FEV 1 % FVC [%] 84.19 56.48 67.09 56.48 53.33 56.67
FEV 1 % VC MAX [%] 81.88 55.26 67.48 55.26 50.10 52.31
VC MAX [L] 3.03 2.26 74.60
PEF [L/s] 6.28 2.66 42.36 2.66 2.58 2.43
MMEF 75/25 [L/s] 3.57 0.51 14.35 0.51 0.49 0.41
MEF 75 [L/s] 5.64 1.47 26.14 1.47 0.80 1.21
MEF 50 [L/s] 4.01 0.68 16.97 0.68 0.72 0.57
MEF 25 [L/s] 1.79 0.19 10.52 0.19 0.18 0.15
V backextrapolation ex [L] 0.05 0.03 0.04
V backextrapol. % FVC [%] 2.07 1.50 1.81
FET [s] 7.63 7.35 7.55
FEF 200-1200 [L/s] 1.19 0.98 1.05
FVC IN [L] 3.03 2.26 74.60 2.26 2.15 2.13
FIV1 [L] 2.21 2.12 2.09
FIV1 % FVC [%] 97.79 98.68 98.05
FEF50 % FIF50 [%] 22.86 25.05 19.46
PIF [L/s] 3.04 3.04 2.99
MVV [L/min] 99.77 46.21 46.32 46.21
BF MVV [1/min] 75.55 75.55
---
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
-0.25
2-0.20
0-0.15
2-0.10
0.05
4
Time [s]
0
5
10
15
20
25
30
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
Pred A1 A1/Pd P1 A2/Pd chg%l P2 A3/Pd chg%2 P3 A4/Pd chg%3
FVC [L.] 2.99 2.21 74.0 2.63 87.9 18.72 2.04 88.2 19.17
FEV 1 [L.] 2.67 1.25 48.6 1.62 69.2 21.85 1.84 69.8 23.23
FEV 1 % FVC [%] 84.19 56.48 67.1 67.97 68.9 2.64 58.40 69.4 3.41
FEV 1 % VC MAX [%] 81.88 55.26 67.6 67.97 70.8 4.91 68.40 71.3 5.73
VC MAX [L.] 3.03 2.26 74.6 2.63 86.6 16.14 2.64 87.0 16.59
PEF [L/s] 6.28 2.66 42.4 2.90 46.2 9.17 3.37 53.7 26.79
MMEF 75/25 [L/s] 3.57 0.61 14.4 0.67 18.8 31.03 0.73 20.4 42.01
MEF 50 [L/s] 4.01 0.68 17.0 0.90 22.5 32.75 0.89 22.1 30.15
MEF 25 [L/s] 1.79 0.19 10.5 0.27 15.2 44.16 0.33 18.7 77.66
FET [s] 7.63 8.01 4.99 7.79 2.14 7.43
V backextrapolation ex [L] 0.05 0.04 -11.67 0.04 -18.64 0.04
PIF [L/s] 3.04 3.37 10.91 3.51 15.70 3.60
FIV1 [L] 2.21 2.56 15.71 2.56 15.66 2.50
PEF50 % FIF50 [%] 22.86 28.15 23.14 25.36 10.95 27.28
MVV [L/min] 99.77 46.21 46.3
BF MVV [1/min] 75.55
2026-08-05 05:53:27,687 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 05:53:27,688 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "15 items, types={'MedicationRecord': 1, 'PrescriptionRecord': 2, 'DischargeRecord': 2, 'AdmissionRecord': 4, 'ExaminationReport': 6}", "name": "YXLA（支气管哮喘）222.pdf", "embedding_token_consumption": 11090}
2026-08-05 05:53:27,688 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 05:53:27,880 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 05:53:27,880 INFO     29 [Trace] task=59fa895e | doc=YXLA（支气管哮喘）222.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":15,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,887 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:53:27,891 INFO     29 set_progress(59fa895e909011f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 05:53:27 [DOC Engine]:
Start to index...
2026-08-05 05:53:27,919 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.023s]
2026-08-05 05:53:27,924 INFO     29 set_progress(59fa895e909011f1a3da71efcdd7cc1f), progress: 0.8066666666666668, progress_msg: 
2026-08-05 05:53:27,952 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-05 05:53:27,977 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.017s]
2026-08-05 05:53:27,993 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-05 05:53:28,002 INFO     29 set_progress(59fa895e909011f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 05:53:27 Indexing done (0.11s). Task done (639.15s)
2026-08-05 05:53:28,006 INFO     29 [Done], chunks(15), token(11090), elapsed:639.15
2026-08-05 05:53:28,221 INFO     29 handle_task done for task {"id": "59fa895e909011f1a3da71efcdd7cc1f", "doc_id": "5986c9ec909011f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "type": "pdf", "location": "YXLA\uff08\u652f\u6c14\u7ba1\u54ee\u5598\uff09222.pdf", "size": 21480002, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785908508451, "task_type": "dataflow", "root_trace_id": "a750cf3b1204410ba521c8c324649cde", "root_traceparent": "00-a750cf3b1204410ba521c8c324649cde-5d606223adc1802e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
