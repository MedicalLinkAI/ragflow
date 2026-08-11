# 基准结果：LHPI+单药+司美医大一院.pdf

## 基本信息

- 文件：`LHPI+单药+司美医大一院.pdf`
- 大小：3490.2 KB
- PDF 总页数：7
- doc_id：`a85a827494bf11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:30:29  完成时间：2026-08-10T21:35:04  耗时：274.5s
- progress_msg：`13:34:57 Indexing done (0.06s). Task done (253.27s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 8168c76a | 1 | 1-1 | 石家庄真仁中医钩活术总医院 姓名：刘 性别：男 年龄：56 科室：中西医结合 主 |
| 2 | 815939b9 | 1 | 2-2 | 石家庄明瀚医院门诊病历 姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊 过 |
| 3 | a51a89e0 | 1 | 5-5 | 世纪康大药房 流水单号：20250329032 会员姓名：刘会平 商品名称    |
| 4 | 59140751 | 1 | 6-6 | 世纪康大药房 流水单号：20250102026 会员姓名： 商品名称 单价 折后 |
| 5 | caff89e7 | 1 | 7-7 | mm W A29216 DOL Diagnosis: - Exam.: 2025 |
| 6 | 873a583d | 1 | 3-3 | <table><tr><td>糖化血红蛋白</td><td>HbA1C</td> |
| 7 | eeaaf0c9 | 1 | 4-4 | <table><tr><td>葡萄糖</td><td>GLU</td><td>8 |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6, 7]`
- 覆盖页数：7 / 7；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 2 | 0 | 2 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "LabReport": 2, "MedicationRecord": 2, "ExaminationReport": 1}`
- ChunkMerger：`{"found": true, "merged": 7, "sources": 9, "stats": {"Extractor:LabExam": 2, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 2, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:34:56,733 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:30:32,611 INFO     29 handle_task begin for task {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:30:32,803 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 13:30:32,914 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:30:32,924 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:30:32,924 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:30:32,924 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:30:32,932 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:30:32,932 INFO     29 ============================================================
2026-08-10 13:30:32,932 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:30:32,932 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:30:32,932 INFO     29 ============================================================
2026-08-10 13:30:32,932 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:30:32,932 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:30:32,940 INFO     29 No torch found.
2026-08-10 13:30:37,528 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=7
2026-08-10 13:30:40,031 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9195547, prompt_len=764
2026-08-10 13:30:51,561 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:30:51,565 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:30:51,595 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9195547, prompt_len=401
2026-08-10 13:30:54,567 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:30:54.565+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 51, "failed": 0, "current": {"a8bf32fa94bf11f1bd9827cf206dfa2d": {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:30:54,795 INFO     29 [qwen-vl-parser] text API response (len=263):
["石家庄真仁中医钩活术总医院", "姓名：刘", "性别：男", "年龄：56", "科室：中西医结合", "主诉：血糖控制不佳2天", "现病史：2天前血糖控制不佳，无口干、多饮、多尿。无头晕、头痛、无恶心、呕吐。", "既往史：糖尿病病史10年", "体格检查：查体未见异常", "辅助检查：", "处理与建议：建议按时按量口服盐酸二甲双胍缓释片0.5g，口服1.0g 2/日，注意饮食", "习惯，适当运动，注意休息。", "初步诊断：2型糖尿病", "医师签字：张宇鹏", "2025年01月02日", "张宇鹏"]
2026-08-10 13:30:54,799 INFO     29 [qwen-vl-parser] page=1 text: 16 lines (bbox 0-15)
2026-08-10 13:30:54,799 INFO     29 [qwen-vl-parser] page=1 text: 16 sections
2026-08-10 13:30:58,636 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=15065193, prompt_len=764
2026-08-10 13:31:08,381 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:31:08,386 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:31:08,437 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=15065193, prompt_len=401
2026-08-10 13:31:13,083 INFO     29 [qwen-vl-parser] text API response (len=345):
["石家庄明瀚医院门诊病历", "姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊", "过敏史:无", "主诉:2型糖尿病10年,血糖控制不佳1个月,复查、定期取药", "现病史:2型糖尿病10年,血糖控制不佳1个月。", "既往史:2型糖尿病", "体格检查:咽无充血,扁桃体无肿大,双肺呼吸音清,未闻及", "干、湿性啰音,心音正常,心律齐,腹软,无压痛。", "辅助检查:", "印象/IMP:2型糖尿病", "处理与建议:", "血糖(空腹)1项", "血脂四项1项", "糖化血红蛋白1项", "普通门诊诊察费1次", "[基]★(TM)盐酸二甲双胍缓释片0.5g口服1.0g2/日", "初步诊断:2型糖尿病", "医师签字:王会兰 玲兰", "2025年03月29日"]
2026-08-10 13:31:13,088 INFO     29 [qwen-vl-parser] page=2 text: 19 lines (bbox 16-34)
2026-08-10 13:31:13,088 INFO     29 [qwen-vl-parser] page=2 text: 19 sections
2026-08-10 13:31:14,148 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3166142, prompt_len=764
2026-08-10 13:31:23,028 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-03-29"
}
```
2026-08-10 13:31:23,029 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2025-03-29
2026-08-10 13:31:23,049 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3166142, prompt_len=756
2026-08-10 13:31:24,863 INFO     29 [qwen-vl-parser] table API response (len=154):
\begin{tabular}{ccccccll}
\hline
项目名称 & 英文名称 & 结果 & 单位 & 参考区间 & 方法学 \\
\hline
1 & 糖化血红蛋白 & HbA1C & 9.10 & \% & ↑ 4.0-6.0 & 荧光免疫层析法 \\
\hline
\end{tabular}
2026-08-10 13:31:24,865 INFO     29 [qwen-vl-parser] page=3 table: 8 LaTeX lines (bbox 35-42)
2026-08-10 13:31:24,865 INFO     29 [qwen-vl-parser] page=3 table: 8 sections
2026-08-10 13:31:25,190 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:31:25.189+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 51, "failed": 0, "current": {"a8bf32fa94bf11f1bd9827cf206dfa2d": {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:31:25,878 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4075160, prompt_len=764
2026-08-10 13:31:34,330 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-03-29"
}
```
2026-08-10 13:31:34,331 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-03-29
2026-08-10 13:31:34,350 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4075160, prompt_len=756
2026-08-10 13:31:39,069 INFO     29 [qwen-vl-parser] table API response (len=348):
\begin{tabular}{cccllcccl}
\hline
1 & 葡萄糖 & GLU & 8.96 & mmol/L & $\uparrow$ & 3.9-6.1 & 己糖激酶法 \\
2 & 甘油三酯 & TG & 2.02 & mmol/L & & 0-2.3 & 氧化酶法 \\
3 & 总胆固醇 & TC & 4.39 & mmol/L & & 0-5.6 & 氧化酶法 \\
4 & 高密度脂蛋白胆固醇 & HDL-C & 1.05 & mmol/L & $\downarrow$ & 1.2-2.0 & 直接法 \\
5 & 低密度脂蛋白胆固醇 & LDL-C & 3.09 & mmol/L & & 0-4.11 & 直接法 \\
\hline
\end{tabular}
2026-08-10 13:31:39,072 INFO     29 [qwen-vl-parser] page=4 table: 10 LaTeX lines (bbox 43-52)
2026-08-10 13:31:39,072 INFO     29 [qwen-vl-parser] page=4 table: 10 sections
2026-08-10 13:31:41,472 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7427847, prompt_len=764
2026-08-10 13:31:50,996 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:31:50,997 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 13:31:51,024 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7427847, prompt_len=401
2026-08-10 13:31:54,277 INFO     29 [qwen-vl-parser] text API response (len=250):
["世纪康大药房", "流水单号：20250329032", "会员姓名：刘会平", "商品名称    单价    折后价    数量    合计", "(德源)盐酸二甲双胍缓释片0.5g*30片", "8.00    8.00    10    80.00", "消费备注：", "消费1项，合计:￥80.00 本次积分:0", "实付金额:￥80.00  找零:￥0.00", "积分:0", "操作员:admin", "出单时间:2025-03-29", "地址：石家庄市新华区誉兴路88号"]
2026-08-10 13:31:54,281 INFO     29 [qwen-vl-parser] page=5 text: 13 lines (bbox 53-65)
2026-08-10 13:31:54,281 INFO     29 [qwen-vl-parser] page=5 text: 13 sections
2026-08-10 13:31:56,605 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:31:56.604+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 51, "failed": 0, "current": {"a8bf32fa94bf11f1bd9827cf206dfa2d": {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:31:56,866 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8801166, prompt_len=764
2026-08-10 13:32:05,843 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:32:05,845 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 13:32:05,868 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8801166, prompt_len=401
2026-08-10 13:32:10,865 INFO     29 [qwen-vl-parser] text API response (len=252):
["世纪康大药房", "流水单号：20250102026", "会员姓名：", "商品名称", "单价", "折后价", "数量", "合计", "(德源)盐酸二甲双胍缓释片0.5g*30片", "8.00", "8.00", "12", "96.00", "消费备注：", "消费1项，合计:￥96.00", "本次积分:0", "实付金额:￥96.00", "找零:￥0.00", "积分:0", "操作员:admin", "出单时间:2025-01-02", "地址：石家庄市新华区誉兴路88号"]
2026-08-10 13:32:10,869 INFO     29 [qwen-vl-parser] page=6 text: 22 lines (bbox 66-87)
2026-08-10 13:32:10,869 INFO     29 [qwen-vl-parser] page=6 text: 22 sections
2026-08-10 13:32:13,639 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=14232861, prompt_len=764
2026-08-10 13:32:23,812 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-21"}
```
2026-08-10 13:32:23,817 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2025-04-21
2026-08-10 13:32:23,861 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=14232861, prompt_len=401
2026-08-10 13:32:28,908 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:32:28.905+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 51, "failed": 0, "current": {"a8bf32fa94bf11f1bd9827cf206dfa2d": {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:32:29,355 INFO     29 [qwen-vl-parser] text API response (len=681):
["mm W A29216", "DOL", "Diagnosis: -", "Exam.: 2025/四月/21", "Comment: -", "OD, vk004D16", "OB, vk004D17", "OD, FA 0:13.17 65° [HS]", "OD, FA 0:27.10 65° ART [HS]", "OD, FA 1:10.60 65° ART [HS]", "OD, FA 1:17.70 65° ART [HS]", "OD, FA 1:23.73 65° ART [HS]", "OD, FA 1:29.21 66° ART [HS]", "OD, FA 1:35.26 65° ART [HS]", "OD, FA 5:19.08 65° ART [HS]", "OS, FA 0:41.48 65° ART [HS]", "OS, FA 0:47.76 65° ART [HS]", "OB, FA 0:53.38 65° ART [HS]", "OS, FA 0:58.04 65° ART [HS]", "OS, FA 1:04.09 65° ART [HS]", "OS, FA 9:00.99 65° ART [HS]", "Notes:", "The SN PDR.", "2025/4/21", "Signature:", "Dun", "www.HeidelbergEngineering.com", "Software Version: 6.9.5", "Overview Report, Page 1"]
2026-08-10 13:32:29,361 INFO     29 [qwen-vl-parser] page=7 text: 29 lines (bbox 88-116)
2026-08-10 13:32:29,361 INFO     29 [qwen-vl-parser] page=7 text: 29 sections
2026-08-10 13:32:29,361 INFO     29 [qwen-vl-parser] parse_pdf done: 117 sections from 7 pages.
2026-08-10 13:32:29,371 INFO     29 Close text detector.
2026-08-10 13:32:29,960 INFO     29 Close text recognizer.
2026-08-10 13:32:30,354 INFO     29 Close recognizer.
2026-08-10 13:32:30,760 INFO     29 Close recognizer.
2026-08-10 13:32:31,553 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:32:31,554 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Parser:MedLink | outputs={"html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "json"}
2026-08-10 13:32:31,554 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:32:31,578 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:32:31,579 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 石家庄真仁中医钩活术总医院\n[BBOX-1] 姓名：刘\n[BBOX-2] 性别：男\n[BBOX-3] 年龄：56\n[BBOX-4] 科室：中西医结合\n[BBOX-5] 主诉：血糖控制不佳2天\n[BBOX-6] 现病史：2天前血糖控制不佳，无口干、多饮、多尿。无头晕、头痛、无恶心、呕吐。\n[BBOX-7] 既往史：糖尿病病史10年\n[BBOX-8] 体格检查：查体未见异常\n[BBOX-9] 辅助检查：\n[BBOX-10] 处理与建议：建议按时按量口服盐酸二甲双胍缓释片0.5g，口服1.0g 2/日，注意饮食\n[BBOX-11] 习惯，适当运动，注意休息。\n[BBOX-12] 初步诊断：2型糖尿病\n[BBOX-13] 医师签字：张宇鹏\n[BBOX-14] 2025年01月02日\n[BBOX-15] 张宇鹏\n[BBOX-16] 石家庄明瀚医院门诊病历\n[BBOX-17] 姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊\n[BBOX-18] 过敏史:无\n[BBOX-19] 主诉:2型糖尿病10年,血糖控制不佳1个月,复查、定期取药\n[BBOX-20] 现病史:2型糖尿病10年,血糖控制不佳1个月。\n[BBOX-21] 既往史:2型糖尿病\n[BBOX-22] 体格检查:咽无充血,扁桃体无肿大,双肺呼吸音清,未闻及\n[BBOX-23] 干、湿性啰音,心音正常,心律齐,腹软,无压痛。\n[BBOX-24] 辅助检查:\n[BBOX-25] 印象/IMP:2型糖尿病\n[BBOX-26] 处理与建议:\n[BBOX-27] 血糖(空腹)1项\n[BBOX-28] 血脂四项1项\n[BBOX-29] 糖化血红蛋白1项\n[BBOX-30] 普通门诊诊察费1次\n[BBOX-31] [基]★(TM)盐酸二甲双胍缓释片0.5g口服1.0g2/日\n[BBOX-32] 初步诊断:2型糖尿病\n[BBOX-33] 医师签字:王会兰 玲兰\n[BBOX-34] 2025年03月29日\n[BBOX-35] \\begin{tabular}{ccccccll}\n[BBOX-36] 报告时间: 2025-03-29\n[BBOX-37] \\hline\n[BBOX-38] 项目名称 & 英文名称 & 结果 & 单位 & 参考区间 & 方法学 \\\\\n[BBOX-39] \\hline\n[BBOX-40] 1 & 糖化血红蛋白 & HbA1C & 9.10 & \\% & ↑ 4.0-6.0 & 荧光免疫层析法 \\\\\n[BBOX-41] \\hline\n[BBOX-42] \\end{tabular}\n[BBOX-43] \\begin{tabular}{cccllcccl}\n[BBOX-44] 报告时间: 2025-03-29\n[BBOX-45] \\hline\n[BBOX-46] 1 & 葡萄糖 & GLU & 8.96 & mmol/L & $\\uparrow$ & 3.9-6.1 & 己糖激酶法 \\\\\n[BBOX-47] 2 & 甘油三酯 & TG & 2.02 & mmol/L & & 0-2.3 & 氧化酶法 \\\\\n[BBOX-48] 3 & 总胆固醇 & TC & 4.39 & mmol/L & & 0-5.6 & 氧化酶法 \\\\\n[BBOX-49] 4 & 高密度脂蛋白胆固醇 & HDL-C & 1.05 & mmol/L & $\\downarrow$ & 1.2-2.0 & 直接法 \\\\\n[BBOX-50] 5 & 低密度脂蛋白胆固醇 & LDL-C & 3.09 & mmol/L & & 0-4.11 & 直接法 \\\\\n[BBOX-51] \\hline\n[BBOX-52] \\end{tabular}\n[BBOX-53] 世纪康大药房\n[BBOX-54] 流水单号：20250329032\n[BBOX-55] 会员姓名：刘会平\n[BBOX-56] 商品名称    单价    折后价    数量    合计\n[BBOX-57] (德源)盐酸二甲双胍缓释片0.5g*30片\n[BBOX-58] 8.00    8.00    10    80.00\n[BBOX-59] 消费备注：\n[BBOX-60] 消费1项，合计:￥80.00 本次积分:0\n[BBOX-61] 实付金额:￥80.00  找零:￥0.00\n[BBOX-62] 积分:0\n[BBOX-63] 操作员:admin\n[BBOX-64] 出单时间:2025-03-29\n[BBOX-65] 地址：石家庄市新华区誉兴路88号\n[BBOX-66] 世纪康大药房\n[BBOX-67] 流水单号：20250102026\n[BBOX-68] 会员姓名：\n[BBOX-69] 商品名称\n[BBOX-70] 单价\n[BBOX-71] 折后价\n[BBOX-72] 数量\n[BBOX-73] 合计\n[BBOX-74] (德源)盐酸二甲双胍缓释片0.5g*30片\n[BBOX-75] 8.00\n[BBOX-76] 8.00\n[BBOX-77] 12\n[BBOX-78] 96.00\n[BBOX-79] 消费备注：\n[BBOX-80] 消费1项，合计:￥96.00\n[BBOX-81] 本次积分:0\n[BBOX-82] 实付金额:￥96.00\n[BBOX-83] 找零:￥0.00\n[BBOX-84] 积分:0\n[BBOX-85] 操作员:admin\n[BBOX-86] 出单时间:2025-01-02\n[BBOX-87] 地址：石家庄市新华区誉兴路88号\n[BBOX-88] mm W A29216\n[BBOX-89] DOL\n[BBOX-90] Diagnosis: -\n[BBOX-91] Exam.: 2025/四月/21\n[BBOX-92] Comment: -\n[BBOX-93] OD, vk004D16\n[BBOX-94] OB, vk004D17\n[BBOX-95] OD, FA 0:13.17 65° [HS]\n[BBOX-96] OD, FA 0:27.10 65° ART [HS]\n[BBOX-97] OD, FA 1:10.60 65° ART [HS]\n[BBOX-98] OD, FA 1:17.70 65° ART [HS]\n[BBOX-99] OD, FA 1:23.73 65° ART [HS]\n[BBOX-100] OD, FA 1:29.21 66° ART [HS]\n[BBOX-101] OD, FA 1:35.26 65° ART [HS]\n[BBOX-102] OD, FA 5:19.08 65° ART [HS]\n[BBOX-103] OS, FA 0:41.48 65° ART [HS]\n[BBOX-104] OS, FA 0:47.76 65° ART [HS]\n[BBOX-105] OB, FA 0:53.38 65° ART [HS]\n[BBOX-106] OS, FA 0:58.04 65° ART [HS]\n[BBOX-107] OS, FA 1:04.09 65° ART [HS]\n[BBOX-108] OS, FA 9:00.99 65° ART [HS]\n[BBOX-109] Notes:\n[BBOX-110] The SN PDR.\n[BBOX-111] 2025/4/21\n[BBOX-112] Signature:\n[BBOX-113] Dun\n[BBOX-114] www.HeidelbergEngineering.com\n[BBOX-115] Software Version: 6.9.5\n[BBOX-116] Overview Report, Page 1"
  }
]
2026-08-10 13:32:37,603 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:32:37,624 INFO     29 [SmartSplitter] SmartSplitter done: 7 chunks from 7 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'LabReport': 2, 'MedicationRecord': 2, 'ExaminationReport': 1}
2026-08-10 13:32:37,632 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:32:37,632 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 2, 'LabReport': 2, 'MedicationRecord': 2, 'ExaminationReport': 1}"}
2026-08-10 13:32:37,632 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:32:37,633 INFO     29 [ChunkRouter] Routed 7 chunks into 4 groups: {'chunks_Clinical': 2, 'chunks_LabExam': 2, 'chunks_Medication': 2, 'chunks_Examination': 1}
2026-08-10 13:32:37,642 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:32:37,642 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | ChunkRouter:Router | outputs={"html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 2, 'LabReport': 2, 'MedicationRecord': 2, 'ExaminationReport': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:32:37,642 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:32:37,646 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:32:37,647 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:32:37,647 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[2]
2026-08-10 13:32:37,647 INFO     29 [qwen-vl-table] positions ： [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:32:38,671 INFO     29 [qwen-vl-table] page=2, rect=2528x1840, img=(7023x5112)
2026-08-10 13:32:38,671 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:32:38,671 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 35, \"bbox_end\": 42, \"encounter_dates\": [\"2025-03-29\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccll}\n报告时间: 2025-03-29\n\\hline\n项目名称 & 英文名称 & 结果 & 单位 & 参考区间 & 方法学 \\\\\n\\hline\n1 & 糖化血红蛋白 & HbA1C & 9.10 & \\% & ↑ 4.0-6.0 & 荧光免疫层析法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:32:39,919 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:32:39,919 INFO     29 [qwen-vl-table] page=2 LLM output (len=216):
{
  "report_date": "2025-03-29",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1C",
      "value": "9.10",
      "unit": "%",
      "reference_range": "4.0-6.0",
      "abnormal": true
    }
  ]
}
2026-08-10 13:32:39,919 INFO     29 [qwen-vl-table] coord grouping: {2: 1}
2026-08-10 13:32:39,933 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5776147, prompt_len=513
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白

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
2026-08-10 13:32:48,383 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [118, 227, 202, 248]}
]
```
2026-08-10 13:32:48,384 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=8.5s
2026-08-10 13:32:48,384 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[118, 227, 202, 248]
2026-08-10 13:32:48,387 INFO     29 [qwen-vl-table] page=2 coord: matched 1/1, time=8.5s
2026-08-10 13:32:48,387 INFO     29 [qwen-vl-table] new_positions (1):
[[3, 298.30400000000003, 510.656, 417.68, 456.32]]
2026-08-10 13:32:48,387 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=10.7s
2026-08-10 13:32:48,395 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:32:48,396 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:32:48,396 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:32:48,396 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:32:49,532 INFO     29 [qwen-vl-table] page=3, rect=2528x1840, img=(7023x5112)
2026-08-10 13:32:49,532 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:32:49,533 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 43, \"bbox_end\": 52, \"encounter_dates\": [\"2025-03-29\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccllcccl}\n报告时间: 2025-03-29\n\\hline\n1 & 葡萄糖 & GLU & 8.96 & mmol/L & $\\uparrow$ & 3.9-6.1 & 己糖激酶法 \\\\\n2 & 甘油三酯 & TG & 2.02 & mmol/L & & 0-2.3 & 氧化酶法 \\\\\n3 & 总胆固醇 & TC & 4.39 & mmol/L & & 0-5.6 & 氧化酶法 \\\\\n4 & 高密度脂蛋白胆固醇 & HDL-C & 1.05 & mmol/L & $\\downarrow$ & 1.2-2.0 & 直接法 \\\\\n5 & 低密度脂蛋白胆固醇 & LDL-C & 3.09 & mmol/L & & 0-4.11 & 直接法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:32:53,130 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:32:53,130 INFO     29 [qwen-vl-table] page=3 LLM output (len=894):
{
  "report_date": "2025-03-29",
  "items": [
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "8.96",
      "unit": "mmol/L",
      "reference_range": "3.9-6.1",
      "abnormal": true
    },
    {
      "name": "甘油三酯",
      "item_code": "TG",
      "value": "2.02",
      "unit": "mmol/L",
      "reference_range": "0-2.3",
      "abnormal": false
    },
    {
      "name": "总胆固醇",
      "item_code": "TC",
      "value": "4.39",
      "unit": "mmol/L",
      "reference_range": "0-5.6",
      "abnormal": false
    },
    {
      "name": "高密度脂蛋白胆固醇",
      "item_code": "HDL-C",
      "value": "1.05",
      "unit": "mmol/L",
      "reference_range": "1.2-2.0",
      "abnormal": true
    },
    {
      "name": "低密度脂蛋白胆固醇",
      "item_code": "LDL-C",
      "value": "3.09",
      "unit": "mmol/L",
      "reference_range": "0-4.11",
      "abnormal": false
    }
  ]
}
2026-08-10 13:32:53,130 INFO     29 [qwen-vl-table] coord grouping: {3: 5}
2026-08-10 13:32:53,145 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7196940, prompt_len=540
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
葡萄糖、甘油三酯、总胆固醇、高密度脂蛋白胆固醇、低密度脂蛋白胆固醇

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
2026-08-10 13:33:03,438 INFO     29 [qwen-vl-table] coord API raw response (len=268):
```json
[
	{"text": "葡萄糖", "bbox": [130, 205, 173, 226]},
	{"text": "甘油三酯", "bbox": [130, 232, 187, 253]},
	{"text": "总胆固醇", "bbox": [130, 258, 187, 280]},
	{"text": "高密度脂蛋白胆固醇", "bbox": [130, 287, 258, 309]},
	{"text": "低密度脂蛋白胆固醇", "bbox": [130, 313, 258, 336]}
]
```
2026-08-10 13:33:03,438 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=10.3s
2026-08-10 13:33:03,438 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖, bbox=[130, 205, 173, 226]
2026-08-10 13:33:03,438 INFO     29 [qwen-vl-table] coord item[1]: text=甘油三酯, bbox=[130, 232, 187, 253]
2026-08-10 13:33:03,438 INFO     29 [qwen-vl-table] coord item[2]: text=总胆固醇, bbox=[130, 258, 187, 280]
2026-08-10 13:33:03,438 INFO     29 [qwen-vl-table] coord item[3]: text=高密度脂蛋白胆固醇, bbox=[130, 287, 258, 309]
2026-08-10 13:33:03,438 INFO     29 [qwen-vl-table] coord item[4]: text=低密度脂蛋白胆固醇, bbox=[130, 313, 258, 336]
2026-08-10 13:33:03,440 INFO     29 [qwen-vl-table] page=3 coord: matched 5/5, time=10.3s
2026-08-10 13:33:03,440 INFO     29 [qwen-vl-table] new_positions (5):
[[4, 328.64, 437.344, 377.2, 415.84000000000003], [4, 328.64, 472.736, 426.88, 465.52000000000004], [4, 328.64, 472.736, 474.72, 515.2], [4, 328.64, 652.224, 528.08, 568.5600000000001], [4, 328.64, 652.224, 575.9200000000001, 618.24]]
2026-08-10 13:33:03,440 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=5, matched=5, pages=1, time=15.0s
2026-08-10 13:33:03,455 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:33:03,455 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:LabExam | outputs={"chunks": "2 items, types={'LabReport': 2}", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:33:03,455 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:33:03,456 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:33:03.456+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 51, "failed": 0, "current": {"a8bf32fa94bf11f1bd9827cf206dfa2d": {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:33:03,462 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:33:03,462 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:33:04,273 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:33:04,282 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:33:04,283 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:33:04,283 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:33:04,289 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:33:04,290 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:33:04,290 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:33:04,290 INFO     29 [qwen-vl-text] positions(15): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:33:04,290 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [15]
2026-08-10 13:33:06,393 INFO     29 [qwen-vl-text] page=0, rect=2308x3316, img=(6412x9212), dpi=200
2026-08-10 13:33:06,400 INFO     29 [qwen-vl-text] LLM extraction start, text_len=210
2026-08-10 13:33:06,400 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:33:06,401 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 14, \"encounter_dates\": [\"2025-01-02\"], \"department\": \"中西医结合\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "石家庄真仁中医钩活术总医院\n姓名：刘\n性别：男\n年龄：56\n科室：中西医结合\n主诉：血糖控制不佳2天\n现病史：2天前血糖控制不佳，无口干、多饮、多尿。无头晕、头痛、无恶心、呕吐。\n既往史：糖尿病病史10年\n体格检查：查体未见异常\n辅助检查：\n处理与建议：建议按时按量口服盐酸二甲双胍缓释片0.5g，口服1.0g 2/日，注意饮食\n习惯，适当运动，注意休息。\n初步诊断：2型糖尿病\n医师签字：张宇鹏\n2025年01月02日",
    "role": "user"
  }
]
2026-08-10 13:33:08,017 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:33:08,017 INFO     29 [qwen-vl-text] LLM output (len=232):
{
  "encounter_date": "2025-01-02",
  "chief_complaint": "血糖控制不佳2天",
  "present_illness": "2天前血糖控制不佳，无口干、多饮、多尿。无头晕、头痛、无恶心、呕吐。",
  "past_history": "糖尿病病史10年",
  "diagnosis": "2型糖尿病",
  "treatment_plan": "盐酸二甲双胍缓释片 0.5g 口服 1.0g 2/日"
}
2026-08-10 13:33:08,017 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-02]
2026-08-10 13:33:08,058 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=18010822, prompt_len=868
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共15行）
["石家庄真仁中医钩活术总医院", "姓名：刘", "性别：男", "年龄：56", "科室：中西医结合", "主诉：血糖控制不佳2天", "现病史：2天前血糖控制不佳，无口干、多饮、多尿。无头晕、头痛、无恶心、呕吐。", "既往史：糖尿病病史10年", "体格检查：查体未见异常", "辅助检查：", "处理与建议：建议按时按量口服盐酸二甲双胍缓释片0.5g，口服1.0g 2/日，注意饮食", "习惯，适当运动，注意休息。", "初步诊断：2型糖尿病", "医师签字：张宇鹏", "2025年01月02日"]

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
2026-08-10 13:33:24,089 INFO     29 [qwen-vl-text] coord API raw response (len=862):
[
	{"text": "石家庄真仁中医钩活术总医院", "bbox": [32, 160, 604, 207]},
	{"text": "姓名：刘", "bbox": [45, 228, 125, 249]},
	{"text": "性别：男", "bbox": [230, 231, 317, 253]},
	{"text": "年龄：56", "bbox": [366, 235, 457, 255]},
	{"text": "科室：中西医结合", "bbox": [498, 237, 672, 258]},
	{"text": "主诉：血糖控制不佳2天", "bbox": [38, 298, 283, 319]},
	{"text": "现病史：2天前血糖控制不佳，无口干、多饮、多尿。无头晕、头痛、无恶心、呕吐。", "bbox": [28, 327, 833, 351]},
	{"text": "既往史：糖尿病病史10年", "bbox": [22, 357, 284, 375],
	"text": "体格检查：查体未见异常", "bbox": [22, 390, 279, 409]},
	{"text": "辅助检查：", "bbox": [24, 426, 132, 445]},
	{"text": "处理与建议：建议按时按量口服盐酸二甲双胍缓释片0.5g，口服1.0g 2/日，注意饮食", "bbox": [25, 460, 903, 479]},
	{"text": "习惯，适当运动，注意休息。", "bbox": [170, 492, 453, 510]},
	{"text": "初步诊断：2型糖尿病", "bbox": [25, 527, 250, 546]},
	{"text": "医师签字：张宇鹏", "bbox": [671, 731, 868, 750]},
	{"text": "2025年01月02日", "bbox": [667, 754, 871, 773]}
]
2026-08-10 13:33:24,090 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=16.0s
2026-08-10 13:33:24,090 INFO     29 [qwen-vl-text] coord item[0]: text=石家庄真仁中医钩活术总医院, bbox=[32, 160, 604, 207]
2026-08-10 13:33:24,090 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：刘, bbox=[45, 228, 125, 249]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[230, 231, 317, 253]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：56, bbox=[366, 235, 457, 255]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[4]: text=科室：中西医结合, bbox=[498, 237, 672, 258]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[5]: text=主诉：血糖控制不佳2天, bbox=[38, 298, 283, 319]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[6]: text=现病史：2天前血糖控制不佳，无口干、多饮、多尿。无头晕、头痛、无恶心、呕吐。, bbox=[28, 327, 833, 351]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[7]: text=体格检查：查体未见异常, bbox=[22, 390, 279, 409]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[8]: text=辅助检查：, bbox=[24, 426, 132, 445]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[9]: text=处理与建议：建议按时按量口服盐酸二甲双胍缓释片0.5g，口服1.0g 2/日，注意饮食, bbox=[25, 460, 903, 479]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[10]: text=习惯，适当运动，注意休息。, bbox=[170, 492, 453, 510]
2026-08-10 13:33:24,091 INFO     29 [qwen-vl-text] coord item[11]: text=初步诊断：2型糖尿病, bbox=[25, 527, 250, 546]
2026-08-10 13:33:24,092 INFO     29 [qwen-vl-text] coord item[12]: text=医师签字：张宇鹏, bbox=[671, 731, 868, 750]
2026-08-10 13:33:24,092 INFO     29 [qwen-vl-text] coord item[13]: text=2025年01月02日, bbox=[667, 754, 871, 773]
2026-08-10 13:33:24,097 INFO     29 [qwen-vl-text] page=0 — 15/15 coords, api_time=16.0s
2026-08-10 13:33:24,098 INFO     29 [qwen-vl-text] new_positions (15):
[[0, 73.856, 1394.032, 530.56, 686.4119999999999], [0, 103.85999999999999, 288.5, 756.048, 825.684], [0, 530.8399999999999, 731.636, 765.996, 838.948], [0, 844.728, 1054.7559999999999, 779.26, 845.5799999999999], [0, 1149.384, 1550.9759999999999, 785.8919999999999, 855.5279999999999], [0, 87.704, 653.164, 988.168, 1057.8039999999999], [0, 64.624, 1922.5639999999999, 1084.3319999999999, 1163.916], [0, 50.775999999999996, 643.9319999999999, 1293.24, 1356.244], [0, 55.391999999999996, 304.65599999999995, 1412.616, 1475.62], [0, 57.699999999999996, 2084.124, 1525.36, 1588.364], [0, 392.35999999999996, 1045.524, 1631.472, 1691.1599999999999], [0, 57.699999999999996, 577.0, 1747.532, 1810.5359999999998], [0, 1548.668, 2003.3439999999998, 2423.996, 2487.0], [0, 1539.436, 2010.2679999999998, 2500.2639999999997, 2563.268], [0, 1539.436, 2010.2679999999998, 2500.2639999999997, 2563.268]]
2026-08-10 13:33:24,098 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=1, time=19.8s
2026-08-10 13:33:24,099 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:33:24,101 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:33:24,101 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:33:24,101 INFO     29 [qwen-vl-text] positions(19): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:33:24,101 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [19]
2026-08-10 13:33:27,914 INFO     29 [qwen-vl-text] page=1, rect=2308x3316, img=(6412x9212), dpi=200
2026-08-10 13:33:27,921 INFO     29 [qwen-vl-text] LLM extraction start, text_len=287
2026-08-10 13:33:27,921 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:33:27,922 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 16, \"bbox_end\": 34, \"encounter_dates\": [\"2025-03-29\"], \"department\": \"内二门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "石家庄明瀚医院门诊病历\n姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊\n过敏史:无\n主诉:2型糖尿病10年,血糖控制不佳1个月,复查、定期取药\n现病史:2型糖尿病10年,血糖控制不佳1个月。\n既往史:2型糖尿病\n体格检查:咽无充血,扁桃体无肿大,双肺呼吸音清,未闻及\n干、湿性啰音,心音正常,心律齐,腹软,无压痛。\n辅助检查:\n印象/IMP:2型糖尿病\n处理与建议:\n血糖(空腹)1项\n血脂四项1项\n糖化血红蛋白1项\n普通门诊诊察费1次\n[基]★(TM)盐酸二甲双胍缓释片0.5g口服1.0g2/日\n初步诊断:2型糖尿病\n医师签字:王会兰 玲兰\n2025年03月29日",
    "role": "user"
  }
]
2026-08-10 13:33:29,793 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:33:29,793 INFO     29 [qwen-vl-text] LLM output (len=232):
{
  "encounter_date": "2025-03-29",
  "chief_complaint": "2型糖尿病10年,血糖控制不佳1个月,复查、定期取药",
  "present_illness": "2型糖尿病10年,血糖控制不佳1个月。",
  "past_history": "2型糖尿病",
  "diagnosis": "2型糖尿病",
  "treatment_plan": "盐酸二甲双胍缓释片 0.5g 口服 1.0g 2/日"
}
2026-08-10 13:33:29,793 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-29]
2026-08-10 13:33:29,860 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=30837430, prompt_len=957
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["石家庄明瀚医院门诊病历", "姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊", "过敏史:无", "主诉:2型糖尿病10年,血糖控制不佳1个月,复查、定期取药", "现病史:2型糖尿病10年,血糖控制不佳1个月。", "既往史:2型糖尿病", "体格检查:咽无充血,扁桃体无肿大,双肺呼吸音清,未闻及", "干、湿性啰音,心音正常,心律齐,腹软,无压痛。", "辅助检查:", "印象/IMP:2型糖尿病", "处理与建议:", "血糖(空腹)1项", "血脂四项1项", "糖化血红蛋白1项", "普通门诊诊察费1次", "[基]★(TM)盐酸二甲双胍缓释片0.5g口服1.0g2/日", "初步诊断:2型糖尿病", "医师签字:王会兰 玲兰", "2025年03月29日"]

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
2026-08-10 13:33:47,157 INFO     29 [qwen-vl-text] coord API raw response (len=1107):
[
	{"text": "石家庄明瀚医院门诊病历", "bbox": [140, 56, 740, 97]},
	{"text": "姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊", "bbox": [66, 123, 762, 144]},
	{"text": "过敏史:无", "bbox": [60, 158, 176, 177]},
	{"text": "主诉:2型糖尿病10年,血糖控制不佳1个月,复查、定期取药", "bbox": [60, 222, 847, 250]},
	{"text": "现病史:2型糖尿病10年,血糖控制不佳1个月。", "bbox": [54, 268, 653, 292]},
	{"text": "既往史:2型糖尿病", "bbox": [54, 293, 296, 315]},
	{"text": "体格检查:咽无充血,扁桃体无肿大,双肺呼吸音清,未闻及", "bbox": [52, 315, 844, 339]},
	{"text": "干、湿性啰音,心音正常,心律齐,腹软,无压痛。", "bbox": [52, 340, 708, 363]},
	{"text": "辅助检查:", "bbox": [52, 363, 176, 385]},
	{"text": "印象/IMP:2型糖尿病", "bbox": [52, 386, 328, 408]},
	{"text": "处理与建议:", "bbox": [52, 410, 206, 431]},
	{"text": "血糖(空腹)1项", "bbox": [52, 432, 249, 455]},
	{"text": "血脂四项1项", "bbox": [54, 455, 231, 477]},
	{"text": "糖化血红蛋白1项", "bbox": [54, 477, 291, 499]},
	{"text": "普通门诊诊察费1次", "bbox": [54, 500, 319, 521]},
	{"text": "[基]★(TM)盐酸二甲双胍缓释片0.5g口服1.0g2/日", "bbox": [48, 521, 712, 545]},
	{"text": "初步诊断:2型糖尿病", "bbox": [40, 567, 334, 590]},
	{"text": "医师签字:王会兰 玲兰", "bbox": [16, 738, 398, 773]},
	{"text": "2025年03月29日", "bbox": [160, 780, 394, 804]}
]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=17.3s
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[0]: text=石家庄明瀚医院门诊病历, bbox=[140, 56, 740, 97]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[1]: text=姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊, bbox=[66, 123, 762, 144]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[2]: text=过敏史:无, bbox=[60, 158, 176, 177]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[3]: text=主诉:2型糖尿病10年,血糖控制不佳1个月,复查、定期取药, bbox=[60, 222, 847, 250]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[4]: text=现病史:2型糖尿病10年,血糖控制不佳1个月。, bbox=[54, 268, 653, 292]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[5]: text=既往史:2型糖尿病, bbox=[54, 293, 296, 315]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[6]: text=体格检查:咽无充血,扁桃体无肿大,双肺呼吸音清,未闻及, bbox=[52, 315, 844, 339]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[7]: text=干、湿性啰音,心音正常,心律齐,腹软,无压痛。, bbox=[52, 340, 708, 363]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[8]: text=辅助检查:, bbox=[52, 363, 176, 385]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[9]: text=印象/IMP:2型糖尿病, bbox=[52, 386, 328, 408]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[10]: text=处理与建议:, bbox=[52, 410, 206, 431]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[11]: text=血糖(空腹)1项, bbox=[52, 432, 249, 455]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[12]: text=血脂四项1项, bbox=[54, 455, 231, 477]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[13]: text=糖化血红蛋白1项, bbox=[54, 477, 291, 499]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[14]: text=普通门诊诊察费1次, bbox=[54, 500, 319, 521]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[15]: text=[基]★(TM)盐酸二甲双胍缓释片0.5g口服1.0g2/日, bbox=[48, 521, 712, 545]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[16]: text=初步诊断:2型糖尿病, bbox=[40, 567, 334, 590]
2026-08-10 13:33:47,160 INFO     29 [qwen-vl-text] coord item[17]: text=医师签字:王会兰 玲兰, bbox=[16, 738, 398, 773]
2026-08-10 13:33:47,161 INFO     29 [qwen-vl-text] coord item[18]: text=2025年03月29日, bbox=[160, 780, 394, 804]
2026-08-10 13:33:47,169 INFO     29 [qwen-vl-text] page=1 — 19/19 coords, api_time=17.3s
2026-08-10 13:33:47,169 INFO     29 [qwen-vl-text] new_positions (19):
[[1, 323.12, 1707.9199999999998, 185.696, 321.652], [1, 152.32799999999997, 1758.696, 407.868, 477.50399999999996], [1, 138.48, 406.20799999999997, 523.928, 586.932], [1, 138.48, 1954.8759999999997, 736.1519999999999, 829.0], [1, 124.63199999999999, 1507.1239999999998, 888.688, 968.2719999999999], [1, 124.63199999999999, 683.1679999999999, 971.588, 1044.54], [1, 120.01599999999999, 1947.9519999999998, 1044.54, 1124.124], [1, 120.01599999999999, 1634.0639999999999, 1127.44, 1203.7079999999999], [1, 120.01599999999999, 406.20799999999997, 1203.7079999999999, 1276.6599999999999], [1, 120.01599999999999, 757.0239999999999, 1279.9759999999999, 1352.9279999999999], [1, 120.01599999999999, 475.448, 1359.56, 1429.196], [1, 120.01599999999999, 574.692, 1432.512, 1508.78], [1, 124.63199999999999, 533.1479999999999, 1508.78, 1581.732], [1, 124.63199999999999, 671.6279999999999, 1581.732, 1654.684], [1, 124.63199999999999, 736.252, 1658.0, 1727.636], [1, 110.78399999999999, 1643.2959999999998, 1727.636, 1807.2199999999998], [1, 92.32, 770.872, 1880.1719999999998, 1956.4399999999998], [1, 36.928, 918.584, 2447.208, 2563.268], [1, 369.28, 909.352, 2586.48, 2666.064]]
2026-08-10 13:33:47,169 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=23.1s
2026-08-10 13:33:47,185 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:33:47,185 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:33:47,185 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:33:47,186 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:33:47.186+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 51, "failed": 0, "current": {"a8bf32fa94bf11f1bd9827cf206dfa2d": {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:33:47,193 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:33:47,193 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:33:47,193 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:33:47,194 INFO     29 [qwen-vl-text] positions(13): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:33:47,194 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [13]
2026-08-10 13:33:49,005 INFO     29 [qwen-vl-text] page=4, rect=2308x3316, img=(6412x9212), dpi=200
2026-08-10 13:33:49,011 INFO     29 [qwen-vl-text] LLM extraction start, text_len=210
2026-08-10 13:33:49,012 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:33:49,012 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 53, \"bbox_end\": 65, \"encounter_dates\": [\"2025-03-29\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "世纪康大药房\n流水单号：20250329032\n会员姓名：刘会平\n商品名称    单价    折后价    数量    合计\n(德源)盐酸二甲双胍缓释片0.5g*30片\n8.00    8.00    10    80.00\n消费备注：\n消费1项，合计:￥80.00 本次积分:0\n实付金额:￥80.00  找零:￥0.00\n积分:0\n操作员:admin\n出单时间:2025-03-29\n地址：石家庄市新华区誉兴路88号",
    "role": "user"
  }
]
2026-08-10 13:33:51,187 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:33:51,187 INFO     29 [qwen-vl-text] LLM output (len=416):
{
  "encounter_date": "2025-03-29",
  "pharmacy": "世纪康大药房",
  "medications": [
    {
      "name": "(德源)盐酸二甲双胍缓释片",
      "specification": "0.5g*30片",
      "dosage": null,
      "quantity": 10,
      "unit_price": 8.00,
      "total_price": 80.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 80.00,
  "payment_method": null
}
2026-08-10 13:33:51,188 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-29]
2026-08-10 13:33:51,230 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=16238611, prompt_len=862
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共13行）
["世纪康大药房", "流水单号：20250329032", "会员姓名：刘会平", "商品名称    单价    折后价    数量    合计", "(德源)盐酸二甲双胍缓释片0.5g*30片", "8.00    8.00    10    80.00", "消费备注：", "消费1项，合计:￥80.00 本次积分:0", "实付金额:￥80.00  找零:￥0.00", "积分:0", "操作员:admin", "出单时间:2025-03-29", "地址：石家庄市新华区誉兴路88号"]

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
2026-08-10 13:34:06,228 INFO     29 [qwen-vl-text] coord API raw response (len=783):
[
	{"text": "世纪康大药房", "bbox": [367, 63, 660, 98]},
	{"text": "流水单号：20250329032", "bbox": [106, 147, 673, 183]},
	{"text": "会员姓名：刘会平", "bbox": [108, 188, 508, 224]},
	{"text": "商品名称    单价    折后价    数量    合计", "bbox": [108, 270, 891, 309]},
	{"text": "(德源)盐酸二甲双胍缓释片0.5g*30片", "bbox": [131, 346, 860, 383]},
	{"text": "8.00    8.00    10    80.00", "bbox": [344, 418, 890, 447]},
	{"text": "消费备注：", "bbox": [111, 460, 307, 493]},
	{"text": "消费1项，合计:￥80.00 本次积分:0", "bbox": [110, 518, 847, 564]},
	{"text": "实付金额:￥80.00  找零:￥0.00", "bbox": [110, 559, 878, 599]},
	{"text": "积分:0", "bbox": [111, 614, 250, 651]},
	{"text": "操作员:admin", "bbox": [111, 649, 407, 693]},
	{"text": "出单时间:2025-03-29", "bbox": [113, 684, 575, 734]},
	{"text": "地址：石家庄市新华区誉兴路88号", "bbox": [115, 764, 794, 817]}
]
2026-08-10 13:34:06,229 INFO     29 [qwen-vl-text] coord API: raw_items=13, valid_items=13, elapsed=15.0s
2026-08-10 13:34:06,229 INFO     29 [qwen-vl-text] coord item[0]: text=世纪康大药房, bbox=[367, 63, 660, 98]
2026-08-10 13:34:06,229 INFO     29 [qwen-vl-text] coord item[1]: text=流水单号：20250329032, bbox=[106, 147, 673, 183]
2026-08-10 13:34:06,229 INFO     29 [qwen-vl-text] coord item[2]: text=会员姓名：刘会平, bbox=[108, 188, 508, 224]
2026-08-10 13:34:06,229 INFO     29 [qwen-vl-text] coord item[3]: text=商品名称    单价    折后价    数量    合计, bbox=[108, 270, 891, 309]
2026-08-10 13:34:06,229 INFO     29 [qwen-vl-text] coord item[4]: text=(德源)盐酸二甲双胍缓释片0.5g*30片, bbox=[131, 346, 860, 383]
2026-08-10 13:34:06,229 INFO     29 [qwen-vl-text] coord item[5]: text=8.00    8.00    10    80.00, bbox=[344, 418, 890, 447]
2026-08-10 13:34:06,229 INFO     29 [qwen-vl-text] coord item[6]: text=消费备注：, bbox=[111, 460, 307, 493]
2026-08-10 13:34:06,230 INFO     29 [qwen-vl-text] coord item[7]: text=消费1项，合计:￥80.00 本次积分:0, bbox=[110, 518, 847, 564]
2026-08-10 13:34:06,230 INFO     29 [qwen-vl-text] coord item[8]: text=实付金额:￥80.00  找零:￥0.00, bbox=[110, 559, 878, 599]
2026-08-10 13:34:06,230 INFO     29 [qwen-vl-text] coord item[9]: text=积分:0, bbox=[111, 614, 250, 651]
2026-08-10 13:34:06,230 INFO     29 [qwen-vl-text] coord item[10]: text=操作员:admin, bbox=[111, 649, 407, 693]
2026-08-10 13:34:06,230 INFO     29 [qwen-vl-text] coord item[11]: text=出单时间:2025-03-29, bbox=[113, 684, 575, 734]
2026-08-10 13:34:06,230 INFO     29 [qwen-vl-text] coord item[12]: text=地址：石家庄市新华区誉兴路88号, bbox=[115, 764, 794, 817]
2026-08-10 13:34:06,235 INFO     29 [qwen-vl-text] page=4 — 13/13 coords, api_time=15.0s
2026-08-10 13:34:06,236 INFO     29 [qwen-vl-text] new_positions (13):
[[4, 847.036, 1523.28, 208.908, 324.96799999999996], [4, 244.64799999999997, 1553.2839999999999, 487.452, 606.828], [4, 249.26399999999998, 1172.464, 623.408, 742.784], [4, 249.26399999999998, 2056.428, 895.3199999999999, 1024.644], [4, 302.34799999999996, 1984.8799999999999, 1147.336, 1270.028], [4, 793.952, 2054.12, 1386.088, 1482.252], [4, 256.188, 708.5559999999999, 1525.36, 1634.788], [4, 253.88, 1954.8759999999997, 1717.6879999999999, 1870.224], [4, 253.88, 2026.4239999999998, 1853.644, 1986.2839999999999], [4, 256.188, 577.0, 2036.024, 2158.716], [4, 256.188, 939.3559999999999, 2152.084, 2297.988], [4, 260.804, 1327.1, 2268.144, 2433.944], [4, 265.41999999999996, 1832.552, 2533.424, 2709.172]]
2026-08-10 13:34:06,236 INFO     29 [qwen-vl-text] ═══ DONE ═══ 13 positions, pages=1, time=19.0s
2026-08-10 13:34:06,237 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:34:06,238 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:34:06,238 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:34:06,238 INFO     29 [qwen-vl-text] positions(22): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:34:06,238 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [22]
2026-08-10 13:34:08,293 INFO     29 [qwen-vl-text] page=5, rect=2308x3316, img=(6412x9212), dpi=200
2026-08-10 13:34:08,300 INFO     29 [qwen-vl-text] LLM extraction start, text_len=185
2026-08-10 13:34:08,300 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:08,300 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 66, \"bbox_end\": 87, \"encounter_dates\": [\"2025-01-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "世纪康大药房\n流水单号：20250102026\n会员姓名：\n商品名称\n单价\n折后价\n数量\n合计\n(德源)盐酸二甲双胍缓释片0.5g*30片\n8.00\n8.00\n12\n96.00\n消费备注：\n消费1项，合计:￥96.00\n本次积分:0\n实付金额:￥96.00\n找零:￥0.00\n积分:0\n操作员:admin\n出单时间:2025-01-02\n地址：石家庄市新华区誉兴路88号",
    "role": "user"
  }
]
2026-08-10 13:34:10,402 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:10,402 INFO     29 [qwen-vl-text] LLM output (len=416):
{
  "encounter_date": "2025-01-02",
  "pharmacy": "世纪康大药房",
  "medications": [
    {
      "name": "(德源)盐酸二甲双胍缓释片",
      "specification": "0.5g*30片",
      "dosage": null,
      "quantity": 12,
      "unit_price": 8.00,
      "total_price": 96.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 96.00,
  "payment_method": null
}
2026-08-10 13:34:10,402 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-02]
2026-08-10 13:34:10,448 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=19047823, prompt_len=864
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["世纪康大药房", "流水单号：20250102026", "会员姓名：", "商品名称", "单价", "折后价", "数量", "合计", "(德源)盐酸二甲双胍缓释片0.5g*30片", "8.00", "8.00", "12", "96.00", "消费备注：", "消费1项，合计:￥96.00", "本次积分:0", "实付金额:￥96.00", "找零:￥0.00", "积分:0", "操作员:admin", "出单时间:2025-01-02", "地址：石家庄市新华区誉兴路88号"]

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
2026-08-10 13:34:27,575 INFO     29 [qwen-vl-text] coord API raw response (len=1154):
[
	{"text": "世纪康大药房", "bbox": [370, 50, 652, 85]},
	{"text": "流水单号：20250102026", "bbox": [122, 119, 662, 167]},
	{"text": "会员姓名：", "bbox": [125, 160, 338, 200]},
	{"text": "商品名称", "bbox": [128, 247, 298, 286]},
	{"text": "单价", "bbox": [351, 255, 425, 290]},
	{"text": "折后价", "bbox": [476, 254, 597, 290]},
	{"text": "数量", "bbox": [655, 252, 738, 286]},
	{"text": "合计", "bbox": [784, 250, 868, 284]},
	{"text": "(德源)盐酸二甲双胍缓释片0.5g*30片", "bbox": [152, 328, 835, 360]},
	{"text": "8.00", "bbox": [348, 396, 418, 419]},
	{"text": "8.00", "bbox": [467, 396, 541, 419]},
	{"text": "12", "bbox": [647, 396, 690, 419]},
	{"text": "96.00", "bbox": [752, 395, 858, 419]},
	{"text": "消费备注：", "bbox": [136, 428, 314, 461]},
	{"text": "消费1项，合计:￥96.00", "bbox": [136, 485, 571, 528]},
	{"text": "本次积分:0", "bbox": [600, 485, 808, 518]},
	{"text": "实付金额:￥96.00", "bbox": [137, 521, 467, 570]},
	{"text": "找零:￥0.00", "bbox": [600, 523, 838, 557]},
	{"text": "积分:0", "bbox": [138, 572, 263, 609]},
	{"text": "操作员:admin", "bbox": [138, 602, 401, 652]},
	{"text": "出单时间:2025-01-02", "bbox": [141, 633, 550, 690]},
	{"text": "地址：石家庄市新华区誉兴路88号", "bbox": [142, 705, 750, 767]}
]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=17.1s
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[0]: text=世纪康大药房, bbox=[370, 50, 652, 85]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[1]: text=流水单号：20250102026, bbox=[122, 119, 662, 167]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[2]: text=会员姓名：, bbox=[125, 160, 338, 200]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[3]: text=商品名称, bbox=[128, 247, 298, 286]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[4]: text=单价, bbox=[351, 255, 425, 290]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[5]: text=折后价, bbox=[476, 254, 597, 290]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[6]: text=数量, bbox=[655, 252, 738, 286]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[7]: text=合计, bbox=[784, 250, 868, 284]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[8]: text=(德源)盐酸二甲双胍缓释片0.5g*30片, bbox=[152, 328, 835, 360]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[9]: text=8.00, bbox=[348, 396, 418, 419]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[10]: text=8.00, bbox=[467, 396, 541, 419]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[11]: text=12, bbox=[647, 396, 690, 419]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[12]: text=96.00, bbox=[752, 395, 858, 419]
2026-08-10 13:34:27,576 INFO     29 [qwen-vl-text] coord item[13]: text=消费备注：, bbox=[136, 428, 314, 461]
2026-08-10 13:34:27,577 INFO     29 [qwen-vl-text] coord item[14]: text=消费1项，合计:￥96.00, bbox=[136, 485, 571, 528]
2026-08-10 13:34:27,577 INFO     29 [qwen-vl-text] coord item[15]: text=本次积分:0, bbox=[600, 485, 808, 518]
2026-08-10 13:34:27,577 INFO     29 [qwen-vl-text] coord item[16]: text=实付金额:￥96.00, bbox=[137, 521, 467, 570]
2026-08-10 13:34:27,577 INFO     29 [qwen-vl-text] coord item[17]: text=找零:￥0.00, bbox=[600, 523, 838, 557]
2026-08-10 13:34:27,577 INFO     29 [qwen-vl-text] coord item[18]: text=积分:0, bbox=[138, 572, 263, 609]
2026-08-10 13:34:27,577 INFO     29 [qwen-vl-text] coord item[19]: text=操作员:admin, bbox=[138, 602, 401, 652]
2026-08-10 13:34:27,577 INFO     29 [qwen-vl-text] coord item[20]: text=出单时间:2025-01-02, bbox=[141, 633, 550, 690]
2026-08-10 13:34:27,577 INFO     29 [qwen-vl-text] coord item[21]: text=地址：石家庄市新华区誉兴路88号, bbox=[142, 705, 750, 767]
2026-08-10 13:34:27,582 INFO     29 [qwen-vl-text] page=5 — 22/22 coords, api_time=17.1s
2026-08-10 13:34:27,583 INFO     29 [qwen-vl-text] new_positions (22):
[[5, 853.9599999999999, 1504.8159999999998, 165.79999999999998, 281.86], [5, 281.57599999999996, 1527.896, 394.604, 553.7719999999999], [5, 288.5, 780.1039999999999, 530.56, 663.1999999999999], [5, 295.424, 687.784, 819.0519999999999, 948.376], [5, 810.108, 980.9, 845.5799999999999, 961.64], [5, 1098.608, 1377.876, 842.264, 961.64], [5, 1511.7399999999998, 1703.3039999999999, 835.632, 948.376], [5, 1809.4719999999998, 2003.3439999999998, 829.0, 941.7439999999999], [5, 350.816, 1927.1799999999998, 1087.648, 1193.76], [5, 803.184, 964.7439999999999, 1313.136, 1389.404], [5, 1077.836, 1248.628, 1313.136, 1389.404], [5, 1493.2759999999998, 1592.52, 1313.136, 1389.404], [5, 1735.616, 1980.264, 1309.82, 1389.404], [5, 313.888, 724.712, 1419.2479999999998, 1528.676], [5, 313.888, 1317.868, 1608.26, 1750.848], [5, 1384.8, 1864.8639999999998, 1608.26, 1717.6879999999999], [5, 316.19599999999997, 1077.836, 1727.636, 1890.12], [5, 1384.8, 1934.1039999999998, 1734.2679999999998, 1847.012], [5, 318.50399999999996, 607.0039999999999, 1896.752, 2019.444], [5, 318.50399999999996, 925.5079999999999, 1996.232, 2162.0319999999997], [5, 325.428, 1269.3999999999999, 2099.028, 2288.04], [5, 327.736, 1730.9999999999998, 2337.7799999999997, 2543.372]]
2026-08-10 13:34:27,583 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=21.3s
2026-08-10 13:34:27,598 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:34:27,598 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:34:27,598 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:34:27,599 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:34:27.599+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 51, "failed": 0, "current": {"a8bf32fa94bf11f1bd9827cf206dfa2d": {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:34:27,605 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:27,605 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:34:28,435 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:28,445 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:34:28,445 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:34:28,446 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:34:28,452 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:28,452 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:34:29,649 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:29,659 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:34:29,660 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:34:29,660 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:34:29,668 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:29,668 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:34:30,185 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:30,192 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:34:30,192 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:34:30,192 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:34:30,197 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:34:30,198 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:34:30,198 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:34:30,198 INFO     29 [qwen-vl-text] positions(29): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:34:30,198 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [29]
2026-08-10 13:34:31,748 INFO     29 [qwen-vl-text] page=6, rect=1766x2426, img=(4906x6739), dpi=200
2026-08-10 13:34:31,753 INFO     29 [qwen-vl-text] LLM extraction start, text_len=593
2026-08-10 13:34:31,753 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:31,753 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 88, \"bbox_end\": 116, \"encounter_dates\": [\"2025-04-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "mm W A29216\nDOL\nDiagnosis: -\nExam.: 2025/四月/21\nComment: -\nOD, vk004D16\nOB, vk004D17\nOD, FA 0:13.17 65° [HS]\nOD, FA 0:27.10 65° ART [HS]\nOD, FA 1:10.60 65° ART [HS]\nOD, FA 1:17.70 65° ART [HS]\nOD, FA 1:23.73 65° ART [HS]\nOD, FA 1:29.21 66° ART [HS]\nOD, FA 1:35.26 65° ART [HS]\nOD, FA 5:19.08 65° ART [HS]\nOS, FA 0:41.48 65° ART [HS]\nOS, FA 0:47.76 65° ART [HS]\nOB, FA 0:53.38 65° ART [HS]\nOS, FA 0:58.04 65° ART [HS]\nOS, FA 1:04.09 65° ART [HS]\nOS, FA 9:00.99 65° ART [HS]\nNotes:\nThe SN PDR.\n2025/4/21\nSignature:\nDun\nwww.HeidelbergEngineering.com\nSoftware Version: 6.9.5\nOverview Report, Page 1",
    "role": "user"
  }
]
2026-08-10 13:34:35,399 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:35,399 INFO     29 [qwen-vl-text] LLM output (len=762):
{
  "exam_date": "2025-04-21",
  "report_date": "2025-04-21",
  "exam_name": "OCT Angiography",
  "exam_category": "other",
  "body_part": "OD, OS",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "OD, vk004D16\nOB, vk004D17\nOD, FA 0:13.17 65° [HS]\nOD, FA 0:27.10 65° ART [HS]\nOD, FA 1:10.60 65° ART [HS]\nOD, FA 1:17.70 65° ART [HS]\nOD, FA 1:23.73 65° ART [HS]\nOD, FA 1:29.21 66° ART [HS]\nOD, FA 1:35.26 65° ART [HS]\nOD, FA 5:19.08 65° ART [HS]\nOS, FA 0:41.48 65° ART [HS]\nOS, FA 0:47.76 65° ART [HS]\nOB, FA 0:53.38 65° ART [HS]\nOS, FA 0:58.04 65° ART [HS]\nOS, FA 1:04.09 65° ART [HS]\nOS, FA 9:00.99 65° ART [HS]",
  "conclusion": "The SN PDR.",
  "physician": "Dun",
  "reviewer": null
}
2026-08-10 13:34:35,461 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=29120362, prompt_len=1293
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["mm W A29216", "DOL", "Diagnosis: -", "Exam.: 2025/四月/21", "Comment: -", "OD, vk004D16", "OB, vk004D17", "OD, FA 0:13.17 65° [HS]", "OD, FA 0:27.10 65° ART [HS]", "OD, FA 1:10.60 65° ART [HS]", "OD, FA 1:17.70 65° ART [HS]", "OD, FA 1:23.73 65° ART [HS]", "OD, FA 1:29.21 66° ART [HS]", "OD, FA 1:35.26 65° ART [HS]", "OD, FA 5:19.08 65° ART [HS]", "OS, FA 0:41.48 65° ART [HS]", "OS, FA 0:47.76 65° ART [HS]", "OB, FA 0:53.38 65° ART [HS]", "OS, FA 0:58.04 65° ART [HS]", "OS, FA 1:04.09 65° ART [HS]", "OS, FA 9:00.99 65° ART [HS]", "Notes:", "The SN PDR.", "2025/4/21", "Signature:", "Dun", "www.HeidelbergEngineering.com", "Software Version: 6.9.5", "Overview Report, Page 1"]

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
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord API raw response (len=1845):
[
	{"text": "mm W A29216", "bbox": [87, 7, 208, 22]},
	{"text": "DOL", "bbox": [450, 0, 487, 8]},
	{"text": "Diagnosis: -", "bbox": [52, 22, 168, 38]},
	{"text": "Exam.: 2025/四月/21", "bbox": [450, 10, 653, 22]},
	{"text": "Comment: -", "bbox": [450, 25, 531, 36]},
	{"text": "OD, vk004D16", "bbox": [52, 93, 129, 102]},
	{"text": "OB, vk004D17", "bbox": [280, 93, 354, 102]},
	{"text": "OD, FA 0:13.17 65° [HS]", "bbox": [505, 67, 630, 77]},
	{"text": "OD, FA 0:27.10 65° ART [HS]", "bbox": [731, 67, 884, 77]},
	{"text": "OD, FA 1:10.60 65° ART [HS]", "bbox": [52, 272, 204, 282]},
	{"text": "OD, FA 1:17.70 65° ART [HS]", "bbox": [280, 272, 428, 282]},
	{"text": "OD, FA 1:23.73 65° ART [HS]", "bbox": [505, 272, 653, 282]},
	{"text": "OD, FA 1:29.21 66° ART [HS]", "bbox": [731, 272, 884, 282]},
	{"text": "OD, FA 1:35.26 65° ART [HS]", "bbox": [52, 478, 204, 488]},
	{"text": "OD, FA 5:19.08 65° ART [HS]", "bbox": [280, 478, 428, 488]},
	{"text": "OS, FA 0:41.48 65° ART [HS]", "bbox": [505, 478, 653, 488]},
	{"text": "OS, FA 0:47.76 65° ART [HS]", "bbox": [731, 478, 884, 488]},
	{"text": "OB, FA 0:53.38 65° ART [HS]", "bbox": [52, 685, 202, 695]},
	{"text": "OS, FA 0:58.04 65° ART [HS]", "bbox": [280, 685, 428, 695]},
	{"text": "OS, FA 1:04.09 65° ART [HS]", "bbox": [505, 685, 653, 695]},
	{"text": "OS, FA 9:00.99 65° ART [HS]", "bbox": [731, 685, 884, 695]},
	{"text": "Notes:", "bbox": [57, 892, 108, 905]},
	{"text": "The SN PDR.", "bbox": [132, 897, 305, 919]},
	{"text": "2025/4/21", "bbox": [104, 922, 180, 933]},
	{"text": "Signature:", "bbox": [275, 922, 353, 935]},
	{"text": "Dun", "bbox": [370, 901, 417, 915]},
	{"text": "www.HeidelbergEngineering.com", "bbox": [414, 944, 594, 955]},
	{"text": "Software Version: 6.9.5", "bbox": [52, 948, 181, 963]},
	{"text": "Overview Report, Page 1", "bbox": [816, 945, 973, 957]}
]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=20.0s
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[0]: text=mm W A29216, bbox=[87, 7, 208, 22]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[1]: text=DOL, bbox=[450, 0, 487, 8]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[2]: text=Diagnosis: -, bbox=[52, 22, 168, 38]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[3]: text=Exam.: 2025/四月/21, bbox=[450, 10, 653, 22]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[4]: text=Comment: -, bbox=[450, 25, 531, 36]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[5]: text=OD, vk004D16, bbox=[52, 93, 129, 102]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[6]: text=OB, vk004D17, bbox=[280, 93, 354, 102]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[7]: text=OD, FA 0:13.17 65° [HS], bbox=[505, 67, 630, 77]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[8]: text=OD, FA 0:27.10 65° ART [HS], bbox=[731, 67, 884, 77]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[9]: text=OD, FA 1:10.60 65° ART [HS], bbox=[52, 272, 204, 282]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[10]: text=OD, FA 1:17.70 65° ART [HS], bbox=[280, 272, 428, 282]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[11]: text=OD, FA 1:23.73 65° ART [HS], bbox=[505, 272, 653, 282]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[12]: text=OD, FA 1:29.21 66° ART [HS], bbox=[731, 272, 884, 282]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[13]: text=OD, FA 1:35.26 65° ART [HS], bbox=[52, 478, 204, 488]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[14]: text=OD, FA 5:19.08 65° ART [HS], bbox=[280, 478, 428, 488]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[15]: text=OS, FA 0:41.48 65° ART [HS], bbox=[505, 478, 653, 488]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[16]: text=OS, FA 0:47.76 65° ART [HS], bbox=[731, 478, 884, 488]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[17]: text=OB, FA 0:53.38 65° ART [HS], bbox=[52, 685, 202, 695]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[18]: text=OS, FA 0:58.04 65° ART [HS], bbox=[280, 685, 428, 695]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[19]: text=OS, FA 1:04.09 65° ART [HS], bbox=[505, 685, 653, 695]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[20]: text=OS, FA 9:00.99 65° ART [HS], bbox=[731, 685, 884, 695]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[21]: text=Notes:, bbox=[57, 892, 108, 905]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[22]: text=The SN PDR., bbox=[132, 897, 305, 919]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[23]: text=2025/4/21, bbox=[104, 922, 180, 933]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[24]: text=Signature:, bbox=[275, 922, 353, 935]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[25]: text=Dun, bbox=[370, 901, 417, 915]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[26]: text=www.HeidelbergEngineering.com, bbox=[414, 944, 594, 955]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[27]: text=Software Version: 6.9.5, bbox=[52, 948, 181, 963]
2026-08-10 13:34:55,491 INFO     29 [qwen-vl-text] coord item[28]: text=Overview Report, Page 1, bbox=[816, 945, 973, 957]
2026-08-10 13:34:55,496 INFO     29 [qwen-vl-text] page=6 — 29/29 coords, api_time=20.0s
2026-08-10 13:34:55,496 INFO     29 [qwen-vl-text] new_positions (29):
[[6, 153.642, 367.328, 16.982, 53.372], [6, 794.7, 860.042, 0.0, 19.408], [6, 91.832, 296.688, 53.372, 92.188], [6, 794.7, 1153.198, 24.26, 53.372], [6, 794.7, 937.746, 60.650000000000006, 87.33600000000001], [6, 91.832, 227.814, 225.61800000000002, 247.45200000000003], [6, 494.48, 625.164, 225.61800000000002, 247.45200000000003], [6, 891.83, 1112.58, 162.542, 186.80200000000002], [6, 1290.946, 1561.144, 162.542, 186.80200000000002], [6, 91.832, 360.264, 659.8720000000001, 684.1320000000001], [6, 494.48, 755.848, 659.8720000000001, 684.1320000000001], [6, 891.83, 1153.198, 659.8720000000001, 684.1320000000001], [6, 1290.946, 1561.144, 659.8720000000001, 684.1320000000001], [6, 91.832, 360.264, 1159.6280000000002, 1183.8880000000001], [6, 494.48, 755.848, 1159.6280000000002, 1183.8880000000001], [6, 891.83, 1153.198, 1159.6280000000002, 1183.8880000000001], [6, 1290.946, 1561.144, 1159.6280000000002, 1183.8880000000001], [6, 91.832, 356.732, 1661.8100000000002, 1686.0700000000002], [6, 494.48, 755.848, 1661.8100000000002, 1686.0700000000002], [6, 891.83, 1153.198, 1661.8100000000002, 1686.0700000000002], [6, 1290.946, 1561.144, 1661.8100000000002, 1686.0700000000002], [6, 100.662, 190.728, 2163.992, 2195.53], [6, 233.112, 538.63, 2176.1220000000003, 2229.494], [6, 183.664, 317.88, 2236.772, 2263.458], [6, 485.65, 623.398, 2236.772, 2268.31], [6, 653.42, 736.422, 2185.826, 2219.79], [6, 731.124, 1049.004, 2290.1440000000002, 2316.83], [6, 91.832, 319.646, 2299.848, 2336.2380000000003], [6, 1441.056, 1718.318, 2292.57, 2321.6820000000002]]
2026-08-10 13:34:55,496 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=25.3s
2026-08-10 13:34:55,502 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:34:55,503 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:34:55,503 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:34:55,507 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:55,507 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:34:56,726 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:34:56,732 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:34:56,732 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "117 items", "markdown": "", "text": "", "name": "LHPI+单药+司美医大一院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2, \"chunks_Examination\": 1}"}
2026-08-10 13:34:56,732 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:34:56,733 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 2, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 13:34:56,740 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:34:56,740 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 2, 'OutpatientRecord': 2, 'MedicationRecord': 2, 'ExaminationReport': 1}", "name": "LHPI+单药+司美医大一院.pdf"}
2026-08-10 13:34:56,740 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:34:56,781 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786368632797, 'update_date': datetime.datetime(2026, 8, 10, 13, 30, 32), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1041598, 'status': '1'}
2026-08-10 13:34:56,997 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白  HbA1C  9.10  %  4.0-6.0  True   
---
   葡萄糖  GLU  8.96  mmol/L  3.9-6.1  True    甘油三酯  TG  2.02  mmol/L  0-2.3  False    总胆固醇  TC  4.39  mmol/L  0-5.6  False    高密度脂蛋白胆固醇  HDL-C  1.05  mmol/L  1.2-2.0  True    低密度脂蛋白胆固醇  LDL-C  3.09  mmol/L  0-4.11  False   
---
石家庄真仁中医钩活术总医院
姓名：刘
性别：男
年龄：56
科室：中西医结合
主诉：血糖控制不佳2天
现病史：2天前血糖控制不佳，无口干、多饮、多尿。无头晕、头痛、无恶心、呕吐。
既往史：糖尿病病史10年
体格检查：查体未见异常
辅助检查：
处理与建议：建议按时按量口服盐酸二甲双胍缓释片0.5g，口服1.0g 2/日，注意饮食
习惯，适当运动，注意休息。
初步诊断：2型糖尿病
医师签字：张宇鹏
2025年01月02日
---
石家庄明瀚医院门诊病历
姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊
过敏史:无
主诉:2型糖尿病10年,血糖控制不佳1个月,复查、定期取药
现病史:2型糖尿病10年,血糖控制不佳1个月。
既往史:2型糖尿病
体格检查:咽无充血,扁桃体无肿大,双肺呼吸音清,未闻及
干、湿性啰音,心音正常,心律齐,腹软,无压痛。
辅助检查:
印象/IMP:2型糖尿病
处理与建议:
血糖(空腹)1项
血脂四项1项
糖化血红蛋白1项
普通门诊诊察费1次
[基]★(TM)盐酸二甲双胍缓释片0.5g口服1.0g2/日
初步诊断:2型糖尿病
医师签字:王会兰 玲兰
2025年03月29日
---
世纪康大药房
流水单号：20250329032
会员姓名：刘会平
商品名称    单价    折后价    数量    合计
(德源)盐酸二甲双胍缓释片0.5g*30片
8.00    8.00    10    80.00
消费备注：
消费1项，合计:￥80.00 本次积分:0
实付金额:￥80.00  找零:￥0.00
积分:0
操作员:admin
出单时间:2025-03-29
地址：石家庄市新华区誉兴路88号
---
世纪康大药房
流水单号：20250102026
会员姓名：
商品名称
单价
折后价
数量
合计
(德源)盐酸二甲双胍缓释片0.5g*30片
8.00
8.00
12
96.00
消费备注：
消费1项，合计:￥96.00
本次积分:0
实付金额:￥96.00
找零:￥0.00
积分:0
操作员:admin
出单时间:2025-01-02
地址：石家庄市新华区誉兴路88号
---
mm W A29216
DOL
Diagnosis: -
Exam.: 2025/四月/21
Comment: -
OD, vk004D16
OB, vk004D17
OD, FA 0:13.17 65° [HS]
OD, FA 0:27.10 65° ART [HS]
OD, FA 1:10.60 65° ART [HS]
OD, FA 1:17.70 65° ART [HS]
OD, FA 1:23.73 65° ART [HS]
OD, FA 1:29.21 66° ART [HS]
OD, FA 1:35.26 65° ART [HS]
OD, FA 5:19.08 65° ART [HS]
OS, FA 0:41.48 65° ART [HS]
OS, FA 0:47.76 65° ART [HS]
OB, FA 0:53.38 65° ART [HS]
OS, FA 0:58.04 65° ART [HS]
OS, FA 1:04.09 65° ART [HS]
OS, FA 9:00.99 65° ART [HS]
Notes:
The SN PDR.
2025/4/21
Signature:
Dun
www.HeidelbergEngineering.com
Software Version: 6.9.5
Overview Report, Page 1
2026-08-10 13:34:57,331 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:34:57,331 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 2, 'OutpatientRecord': 2, 'MedicationRecord': 2, 'ExaminationReport': 1}", "name": "LHPI+单药+司美医大一院.pdf", "embedding_token_consumption": 1286}
2026-08-10 13:34:57,331 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:34:57,713 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:34:57,713 INFO     29 [Trace] task=a8bf32fa | doc=LHPI+单药+司美医大一院.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":7,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:34:57,717 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(3, 298, 510, 417, 456) row[-1]=(3, 298, 510, 417, 456)
2026-08-10 13:34:57,717 INFO     29 [DIAG-EXECUTOR] row_position_int len=5 row[0]=(4, 328, 437, 377, 415) row[-1]=(4, 328, 652, 575, 618)
2026-08-10 13:34:57,717 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:34:57,717 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:34:57,717 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:34:57,717 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:34:57,717 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:34:57,726 INFO     29 set_progress(a8bf32fa94bf11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:34:57 [DOC Engine]:
Start to index...
2026-08-10 13:34:57,759 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 13:34:57,763 INFO     29 set_progress(a8bf32fa94bf11f1bd9827cf206dfa2d), progress: 0.8142857142857143, progress_msg: 
2026-08-10 13:34:57,778 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 13:34:57,785 INFO     29 set_progress(a8bf32fa94bf11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:34:57 Indexing done (0.06s). Task done (253.27s)
2026-08-10 13:34:57,789 INFO     29 [Done], chunks(7), token(1286), elapsed:253.27
2026-08-10 13:34:57,865 INFO     29 handle_task done for task {"id": "a8bf32fa94bf11f1bd9827cf206dfa2d", "doc_id": "a85a827494bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "type": "pdf", "location": "LHPI+\u5355\u836f+\u53f8\u7f8e\u533b\u5927\u4e00\u9662.pdf", "size": 3573996, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786368631598, "task_type": "dataflow", "root_trace_id": "056381f36a04484bb2a14af068181806", "root_traceparent": "00-056381f36a04484bb2a14af068181806-1bb42d9e6390ba71-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
