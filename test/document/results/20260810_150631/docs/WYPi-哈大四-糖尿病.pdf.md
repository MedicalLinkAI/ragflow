# 基准结果：WYPi-哈大四-糖尿病.pdf

## 基本信息

- 文件：`WYPi-哈大四-糖尿病.pdf`
- 大小：1843.8 KB
- PDF 总页数：6
- doc_id：`163668e2948b11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:14:11  完成时间：2026-08-10T15:15:50  耗时：98.6s
- progress_msg：`07:15:44 Indexing done (0.18s). Task done (91.98s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | ac9bb5df | 1 | 2-2 | 巴彦县太平社区卫生服务中心病历信息 门诊编号: 姓名: 性别: 女 科室: 门诊 |
| 2 | 3b72effa | 1 | 6-6 | 巴彦县太平社区卫生服务中 门诊缴费凭证 姓名： 就诊卡号： 性别：女 年龄：64 |
| 3 | d37c88f0 | 1 | 3-3 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 4 | 2e9ef25a | 1 | 4-4 | <table><tr><td>葡萄糖</td><td>GLU</td><td>8 |
| 5 | c7984f88 | 1 | 5-5 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：5
- 页码并集：`[2, 3, 4, 5, 6]`
- 覆盖页数：5 / 6；缺失页：`[1]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 5/6 页，缺失 [1]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 1 | 1 | 1 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 3 | 0 | 3 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "LabReport": 3, "MedicationRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 5, "sources": 8, "stats": {"Extractor:LabExam": 3, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 07:15:43,567 INFO     29 [ChunkMerger] Merged 5 chunks from 8 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 07:14:12,280 INFO     29 handle_task begin for task {"id": "166b6a2e948b11f1bd9827cf206dfa2d", "doc_id": "163668e2948b11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "size": 1888060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786346052273, "task_type": "dataflow", "root_trace_id": "d7cd678f6b6e421d965ddc3b62b23ca3", "root_traceparent": "00-d7cd678f6b6e421d965ddc3b62b23ca3-950bc6afdd8d5782-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 07:14:12,487 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 07:14:12,600 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 07:14:12,613 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:14:12,613 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 07:14:12,613 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 07:14:12,626 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 07:14:12,626 INFO     29 ============================================================
2026-08-10 07:14:12,626 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 07:14:12,626 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 07:14:12,627 INFO     29 ============================================================
2026-08-10 07:14:12,627 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 07:14:12,627 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 07:14:12,628 INFO     29 No torch found.
2026-08-10 07:14:13,578 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=6
2026-08-10 07:14:13,716 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=237378, prompt_len=764
2026-08-10 07:14:17,428 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-20"}
```
2026-08-10 07:14:17,429 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-04-20
2026-08-10 07:14:17,437 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=237378, prompt_len=401
2026-08-10 07:14:18,098 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:14:18.098+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 12, "failed": 0, "current": {"166b6a2e948b11f1bd9827cf206dfa2d": {"id": "166b6a2e948b11f1bd9827cf206dfa2d", "doc_id": "163668e2948b11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "size": 1888060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786346052273, "task_type": "dataflow", "root_trace_id": "d7cd678f6b6e421d965ddc3b62b23ca3", "root_traceparent": "00-d7cd678f6b6e421d965ddc3b62b23ca3-950bc6afdd8d5782-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:14:19,101 INFO     29 [qwen-vl-parser] text API response (len=230):
["受试者推荐情况汇总", "单药-联合？：联合", "姓名缩写：WYP", "年龄：65", "性别：女", "身高：155cm", "体重：63kg", "BMI：26.2", "首次诊断T2DM时间：2020", "最近血糖&糖化检测结果：8.6", "糖化-日期：2025.4.12", "遗传病学（乙肝、丙肝、梅毒、艾滋", "）是否阳性：否", "既往疾病：无", "推荐的中心：哈大四", "居住地：哈尔滨", "提报时间：2025.4.20"]
2026-08-10 07:14:19,102 INFO     29 [qwen-vl-parser] page=1 text: 17 lines (bbox 0-16)
2026-08-10 07:14:19,102 INFO     29 [qwen-vl-parser] page=1 text: 17 sections
2026-08-10 07:14:19,418 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1227633, prompt_len=764
2026-08-10 07:14:22,964 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-09-13"}
```
2026-08-10 07:14:22,964 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2024-09-13
2026-08-10 07:14:22,983 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1227633, prompt_len=401
2026-08-10 07:14:26,485 INFO     29 [qwen-vl-parser] text API response (len=525):
["巴彦县太平社区卫生服务中心病历信息", "门诊编号:", "姓名:", "性别: 女", "科室: 门诊", "年龄: 63岁", "过敏史: 无", "发病时间: 2024-09-13", "身高:", "体重:", "血压: 130/85mmHg", "血糖:", "体温: 36.5℃", "脉搏: 65次/min", "主诉: 诊断2型糖尿病4年", "既往史: 否认食物、药物过敏史。", "现病史: 诊断2型糖尿病4年。", "体格检查: 神清语利, 精神可。颈软, 无抵抗。两侧瞳孔正大等圆, 对光反射灵敏。", "双肺呼吸音清, 未闻及干、湿性啰音。心音可, 心律齐, 各瓣膜听诊区未闻及病理", "性杂音。腹软, 无压痛、反跳痛及肌紧张。", "辅助检查: 血糖、糖化血红蛋白", "健康评估: 慢病工程, 病情平稳, 一般情况可, 生命体征平稳。", "治疗意见: 二甲双胍片每日3次每次0.5g治疗。糖尿病健康知识宣教, 糖尿病饮食,", "监测血糖, 适当运动。注意复查。必要时上级医院诊疗。", "诊断: 2型糖尿病", "打印日期: 2024-09-13 13:24:15", "医生签名: 主治医师", "乔明磊"]
2026-08-10 07:14:26,486 INFO     29 [qwen-vl-parser] page=2 text: 28 lines (bbox 17-44)
2026-08-10 07:14:26,486 INFO     29 [qwen-vl-parser] page=2 text: 28 sections
2026-08-10 07:14:26,818 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=943112, prompt_len=764
2026-08-10 07:14:30,131 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2024-09-13"}
```
2026-08-10 07:14:30,132 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2024-09-13
2026-08-10 07:14:30,149 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=943112, prompt_len=756
2026-08-10 07:14:31,298 INFO     29 [qwen-vl-parser] table API response (len=148):
\begin{tabular}{ccccccc}
\hline
项目名称 & 英文 & 结果 & 标志 & 单位 & 参考值 \\
\hline
糖化血红蛋白 & HbA1c & 8.04 & $\uparrow$ & \% & 4.00-6.00 \\
\hline
\end{tabular}
2026-08-10 07:14:31,299 INFO     29 [qwen-vl-parser] page=3 table: 8 LaTeX lines (bbox 45-52)
2026-08-10 07:14:31,299 INFO     29 [qwen-vl-parser] page=3 table: 8 sections
2026-08-10 07:14:31,805 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2535529, prompt_len=764
2026-08-10 07:14:35,555 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-12"
}
```
2026-08-10 07:14:35,556 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-04-12
2026-08-10 07:14:35,576 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2535529, prompt_len=756
2026-08-10 07:14:37,011 INFO     29 [qwen-vl-parser] table API response (len=172):
\begin{tabular}{ccccccccc}
\hline
序号 & 项目代码 & 项目名称 & & & 检验结果 & 单位 & 生物参考区间 & 检验方法 \\
\hline
01 & GLU & ★葡萄糖 & & & 8.24 & mmol/L & 3.90-6.10 & 己糖激酶法 \\
\hline
\end{tabular}
2026-08-10 07:14:37,015 INFO     29 [qwen-vl-parser] page=4 table: 8 LaTeX lines (bbox 53-60)
2026-08-10 07:14:37,016 INFO     29 [qwen-vl-parser] page=4 table: 8 sections
2026-08-10 07:14:37,494 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2216113, prompt_len=764
2026-08-10 07:14:40,932 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-12"
}
```
2026-08-10 07:14:40,932 INFO     29 [qwen-vl-parser] page=5 classify=table report_date=2025-04-12
2026-08-10 07:14:40,945 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2216113, prompt_len=756
2026-08-10 07:14:42,329 INFO     29 [qwen-vl-parser] table API response (len=161):
\begin{tabular}{cccccccc}
\hline
序号 & 项目代码 & 项目名称 & 前回値 & 结果 & 异常标识 & 单位 & 参考区间 \\
\hline
01 & HbA1c & ★糖化血红蛋白 & & 8.6 & ↑ & \% & 3.6-6.0 \\
\hline
\end{tabular}
2026-08-10 07:14:42,330 INFO     29 [qwen-vl-parser] page=5 table: 8 LaTeX lines (bbox 61-68)
2026-08-10 07:14:42,330 INFO     29 [qwen-vl-parser] page=5 table: 8 sections
2026-08-10 07:14:42,712 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1367205, prompt_len=764
2026-08-10 07:14:46,340 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 07:14:46,340 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 07:14:46,361 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1367205, prompt_len=401
2026-08-10 07:14:48,134 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:14:48.133+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 12, "failed": 0, "current": {"166b6a2e948b11f1bd9827cf206dfa2d": {"id": "166b6a2e948b11f1bd9827cf206dfa2d", "doc_id": "163668e2948b11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "size": 1888060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786346052273, "task_type": "dataflow", "root_trace_id": "d7cd678f6b6e421d965ddc3b62b23ca3", "root_traceparent": "00-d7cd678f6b6e421d965ddc3b62b23ca3-950bc6afdd8d5782-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:14:48,522 INFO     29 [qwen-vl-parser] text API response (len=286):
["巴彦县太平社区卫生服务中", "门诊缴费凭证", "姓名：", "就诊卡号：", "性别：女", "年龄：64岁", "病人ID：", "缴费流水号：2025011900141", "医保类别：", "缴费方式：□公□自□保", "就诊科室：普通门诊", "接诊医生：刘璐璐", "收费项目", "数量", "金额", "盐酸二甲双胍缓释片/北京悦康", "0.5g×30片/盒", "20.0盒X 7.50元=150.00", "操作员：5556", "收款时间：2025-01-19 13:16:14", "温馨提示", "本凭条为本次缴款凭据，不做报销凭证。"]
2026-08-10 07:14:48,522 INFO     29 [qwen-vl-parser] page=6 text: 22 lines (bbox 69-90)
2026-08-10 07:14:48,522 INFO     29 [qwen-vl-parser] page=6 text: 22 sections
2026-08-10 07:14:48,522 INFO     29 [qwen-vl-parser] parse_pdf done: 91 sections from 6 pages.
2026-08-10 07:14:48,537 INFO     29 Close text detector.
2026-08-10 07:14:48,981 INFO     29 Close text recognizer.
2026-08-10 07:14:49,411 INFO     29 Close recognizer.
2026-08-10 07:14:49,895 INFO     29 Close recognizer.
2026-08-10 07:14:50,374 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 07:14:50,374 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Parser:MedLink | outputs={"html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "json"}
2026-08-10 07:14:50,374 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 07:14:50,407 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:14:50,407 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 受试者推荐情况汇总\n[BBOX-1] 单药-联合？：联合\n[BBOX-2] 姓名缩写：WYP\n[BBOX-3] 年龄：65\n[BBOX-4] 性别：女\n[BBOX-5] 身高：155cm\n[BBOX-6] 体重：63kg\n[BBOX-7] BMI：26.2\n[BBOX-8] 首次诊断T2DM时间：2020\n[BBOX-9] 最近血糖&糖化检测结果：8.6\n[BBOX-10] 糖化-日期：2025.4.12\n[BBOX-11] 遗传病学（乙肝、丙肝、梅毒、艾滋\n[BBOX-12] ）是否阳性：否\n[BBOX-13] 既往疾病：无\n[BBOX-14] 推荐的中心：哈大四\n[BBOX-15] 居住地：哈尔滨\n[BBOX-16] 提报时间：2025.4.20\n[BBOX-17] 巴彦县太平社区卫生服务中心病历信息\n[BBOX-18] 门诊编号:\n[BBOX-19] 姓名:\n[BBOX-20] 性别: 女\n[BBOX-21] 科室: 门诊\n[BBOX-22] 年龄: 63岁\n[BBOX-23] 过敏史: 无\n[BBOX-24] 发病时间: 2024-09-13\n[BBOX-25] 身高:\n[BBOX-26] 体重:\n[BBOX-27] 血压: 130/85mmHg\n[BBOX-28] 血糖:\n[BBOX-29] 体温: 36.5℃\n[BBOX-30] 脉搏: 65次/min\n[BBOX-31] 主诉: 诊断2型糖尿病4年\n[BBOX-32] 既往史: 否认食物、药物过敏史。\n[BBOX-33] 现病史: 诊断2型糖尿病4年。\n[BBOX-34] 体格检查: 神清语利, 精神可。颈软, 无抵抗。两侧瞳孔正大等圆, 对光反射灵敏。\n[BBOX-35] 双肺呼吸音清, 未闻及干、湿性啰音。心音可, 心律齐, 各瓣膜听诊区未闻及病理\n[BBOX-36] 性杂音。腹软, 无压痛、反跳痛及肌紧张。\n[BBOX-37] 辅助检查: 血糖、糖化血红蛋白\n[BBOX-38] 健康评估: 慢病工程, 病情平稳, 一般情况可, 生命体征平稳。\n[BBOX-39] 治疗意见: 二甲双胍片每日3次每次0.5g治疗。糖尿病健康知识宣教, 糖尿病饮食,\n[BBOX-40] 监测血糖, 适当运动。注意复查。必要时上级医院诊疗。\n[BBOX-41] 诊断: 2型糖尿病\n[BBOX-42] 打印日期: 2024-09-13 13:24:15\n[BBOX-43] 医生签名: 主治医师\n[BBOX-44] 乔明磊\n[BBOX-45] \\begin{tabular}{ccccccc}\n[BBOX-46] 报告时间: 2024-09-13\n[BBOX-47] \\hline\n[BBOX-48] 项目名称 & 英文 & 结果 & 标志 & 单位 & 参考值 \\\\\n[BBOX-49] \\hline\n[BBOX-50] 糖化血红蛋白 & HbA1c & 8.04 & $\\uparrow$ & \\% & 4.00-6.00 \\\\\n[BBOX-51] \\hline\n[BBOX-52] \\end{tabular}\n[BBOX-53] \\begin{tabular}{ccccccccc}\n[BBOX-54] 报告时间: 2025-04-12\n[BBOX-55] \\hline\n[BBOX-56] 序号 & 项目代码 & 项目名称 & & & 检验结果 & 单位 & 生物参考区间 & 检验方法 \\\\\n[BBOX-57] \\hline\n[BBOX-58] 01 & GLU & ★葡萄糖 & & & 8.24 & mmol/L & 3.90-6.10 & 己糖激酶法 \\\\\n[BBOX-59] \\hline\n[BBOX-60] \\end{tabular}\n[BBOX-61] \\begin{tabular}{cccccccc}\n[BBOX-62] 报告时间: 2025-04-12\n[BBOX-63] \\hline\n[BBOX-64] 序号 & 项目代码 & 项目名称 & 前回値 & 结果 & 异常标识 & 单位 & 参考区间 \\\\\n[BBOX-65] \\hline\n[BBOX-66] 01 & HbA1c & ★糖化血红蛋白 & & 8.6 & ↑ & \\% & 3.6-6.0 \\\\\n[BBOX-67] \\hline\n[BBOX-68] \\end{tabular}\n[BBOX-69] 巴彦县太平社区卫生服务中\n[BBOX-70] 门诊缴费凭证\n[BBOX-71] 姓名：\n[BBOX-72] 就诊卡号：\n[BBOX-73] 性别：女\n[BBOX-74] 年龄：64岁\n[BBOX-75] 病人ID：\n[BBOX-76] 缴费流水号：2025011900141\n[BBOX-77] 医保类别：\n[BBOX-78] 缴费方式：□公□自□保\n[BBOX-79] 就诊科室：普通门诊\n[BBOX-80] 接诊医生：刘璐璐\n[BBOX-81] 收费项目\n[BBOX-82] 数量\n[BBOX-83] 金额\n[BBOX-84] 盐酸二甲双胍缓释片/北京悦康\n[BBOX-85] 0.5g×30片/盒\n[BBOX-86] 20.0盒X 7.50元=150.00\n[BBOX-87] 操作员：5556\n[BBOX-88] 收款时间：2025-01-19 13:16:14\n[BBOX-89] 温馨提示\n[BBOX-90] 本凭条为本次缴款凭据，不做报销凭证。"
  }
]
2026-08-10 07:14:55,040 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:14:55,065 INFO     29 [SmartSplitter] SmartSplitter done: 5 chunks from 5 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'LabReport': 3, 'MedicationRecord': 1}
2026-08-10 07:14:55,080 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 07:14:55,080 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 1, 'LabReport': 3, 'MedicationRecord': 1}"}
2026-08-10 07:14:55,080 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 07:14:55,081 INFO     29 [ChunkRouter] Routed 5 chunks into 3 groups: {'chunks_Clinical': 1, 'chunks_LabExam': 3, 'chunks_Medication': 1}
2026-08-10 07:14:55,093 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 07:14:55,093 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | ChunkRouter:Router | outputs={"html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 1, 'LabReport': 3, 'MedicationRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:14:55,094 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 07:14:55,101 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:14:55,102 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:14:55,102 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[2]
2026-08-10 07:14:55,102 INFO     29 [qwen-vl-table] positions ： [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:14:55,404 INFO     29 [qwen-vl-table] page=2, rect=810x1440, img=(2250x4000)
2026-08-10 07:14:55,405 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:14:55,405 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 45, \"bbox_end\": 52, \"encounter_dates\": [\"2024-09-13\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2024-09-13\n\\hline\n项目名称 & 英文 & 结果 & 标志 & 单位 & 参考值 \\\\\n\\hline\n糖化血红蛋白 & HbA1c & 8.04 & $\\uparrow$ & \\% & 4.00-6.00 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:14:56,752 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:14:56,753 INFO     29 [qwen-vl-table] page=2 LLM output (len=218):
{
  "report_date": "2024-09-13",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1c",
      "value": "8.04",
      "unit": "%",
      "reference_range": "4.00-6.00",
      "abnormal": true
    }
  ]
}
2026-08-10 07:14:56,753 INFO     29 [qwen-vl-table] coord grouping: {2: 1}
2026-08-10 07:14:56,755 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1271580, prompt_len=513
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
2026-08-10 07:15:00,035 INFO     29 [qwen-vl-table] coord API raw response (len=64):
```json
[
	{"text": "糖化血红蛋白", "bbox": [63, 284, 201, 300]}
]
```
2026-08-10 07:15:00,035 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=3.3s
2026-08-10 07:15:00,035 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[63, 284, 201, 300]
2026-08-10 07:15:00,036 INFO     29 [qwen-vl-table] page=2 coord: matched 1/1, time=3.3s
2026-08-10 07:15:00,036 INFO     29 [qwen-vl-table] new_positions (1):
[[3, 51.03, 162.81, 408.96, 432.0]]
2026-08-10 07:15:00,036 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=4.9s
2026-08-10 07:15:00,037 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:15:00,038 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:15:00,038 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 07:15:00,038 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:15:00,357 INFO     29 [qwen-vl-table] page=3, rect=810x1440, img=(2250x4000)
2026-08-10 07:15:00,357 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:00,357 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 53, \"bbox_end\": 60, \"encounter_dates\": [\"2025-04-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2025-04-12\n\\hline\n序号 & 项目代码 & 项目名称 & & & 检验结果 & 单位 & 生物参考区间 & 检验方法 \\\\\n\\hline\n01 & GLU & ★葡萄糖 & & & 8.24 & mmol/L & 3.90-6.10 & 己糖激酶法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:15:02,035 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:02,036 INFO     29 [qwen-vl-table] page=3 LLM output (len=218):
{
  "report_date": "2025-04-12",
  "items": [
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "8.24",
      "unit": "mmol/L",
      "reference_range": "3.90-6.10",
      "abnormal": true
    }
  ]
}
2026-08-10 07:15:02,036 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 07:15:02,048 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3749078, prompt_len=510
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
葡萄糖

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
2026-08-10 07:15:05,760 INFO     29 [qwen-vl-table] coord API raw response (len=62):
```json
[
	{"text": "葡萄糖", "bbox": [117, 306, 163, 320]}
]
```
2026-08-10 07:15:05,760 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=3.7s
2026-08-10 07:15:05,761 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖, bbox=[117, 306, 163, 320]
2026-08-10 07:15:05,762 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=3.7s
2026-08-10 07:15:05,763 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 94.77000000000001, 132.03, 440.64, 460.79999999999995]]
2026-08-10 07:15:05,763 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=5.7s
2026-08-10 07:15:05,767 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:15:05,770 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:15:05,770 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[4]
2026-08-10 07:15:05,771 INFO     29 [qwen-vl-table] positions ： [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:15:06,092 INFO     29 [qwen-vl-table] page=4, rect=810x1440, img=(2250x4000)
2026-08-10 07:15:06,093 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:06,093 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 61, \"bbox_end\": 68, \"encounter_dates\": [\"2025-04-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccc}\n报告时间: 2025-04-12\n\\hline\n序号 & 项目代码 & 项目名称 & 前回値 & 结果 & 异常标识 & 单位 & 参考区间 \\\\\n\\hline\n01 & HbA1c & ★糖化血红蛋白 & & 8.6 & ↑ & \\% & 3.6-6.0 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:15:07,754 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:07,754 INFO     29 [qwen-vl-table] page=4 LLM output (len=215):
{
  "report_date": "2025-04-12",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1c",
      "value": "8.6",
      "unit": "%",
      "reference_range": "3.6-6.0",
      "abnormal": true
    }
  ]
}
2026-08-10 07:15:07,754 INFO     29 [qwen-vl-table] coord grouping: {4: 1}
2026-08-10 07:15:07,760 INFO     29 [qwen-vl-table] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3267842, prompt_len=513
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
2026-08-10 07:15:11,288 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [135, 307, 228, 318]}
]
```
2026-08-10 07:15:11,288 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=3.5s
2026-08-10 07:15:11,288 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[135, 307, 228, 318]
2026-08-10 07:15:11,289 INFO     29 [qwen-vl-table] page=4 coord: matched 1/1, time=3.5s
2026-08-10 07:15:11,289 INFO     29 [qwen-vl-table] new_positions (1):
[[5, 109.35000000000001, 184.68, 442.08, 457.91999999999996]]
2026-08-10 07:15:11,289 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=5.5s
2026-08-10 07:15:11,299 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 07:15:11,299 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Extractor:LabExam | outputs={"chunks": "3 items, types={'LabReport': 3}", "html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:15:11,299 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 07:15:11,307 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:11,307 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 07:15:12,622 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:12,629 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 07:15:12,630 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:15:12,630 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 07:15:12,636 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:15:12,637 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:15:12,637 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 07:15:12,637 INFO     29 [qwen-vl-text] positions(28): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:15:12,637 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [28]
2026-08-10 07:15:12,868 INFO     29 [qwen-vl-text] page=1, rect=1440x810, img=(4000x2250), dpi=200
2026-08-10 07:15:12,870 INFO     29 [qwen-vl-text] LLM extraction start, text_len=440
2026-08-10 07:15:12,870 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:12,870 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 17, \"bbox_end\": 44, \"encounter_dates\": [\"2024-09-13\"], \"department\": \"门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "巴彦县太平社区卫生服务中心病历信息\n门诊编号:\n姓名:\n性别: 女\n科室: 门诊\n年龄: 63岁\n过敏史: 无\n发病时间: 2024-09-13\n身高:\n体重:\n血压: 130/85mmHg\n血糖:\n体温: 36.5℃\n脉搏: 65次/min\n主诉: 诊断2型糖尿病4年\n既往史: 否认食物、药物过敏史。\n现病史: 诊断2型糖尿病4年。\n体格检查: 神清语利, 精神可。颈软, 无抵抗。两侧瞳孔正大等圆, 对光反射灵敏。\n双肺呼吸音清, 未闻及干、湿性啰音。心音可, 心律齐, 各瓣膜听诊区未闻及病理\n性杂音。腹软, 无压痛、反跳痛及肌紧张。\n辅助检查: 血糖、糖化血红蛋白\n健康评估: 慢病工程, 病情平稳, 一般情况可, 生命体征平稳。\n治疗意见: 二甲双胍片每日3次每次0.5g治疗。糖尿病健康知识宣教, 糖尿病饮食,\n监测血糖, 适当运动。注意复查。必要时上级医院诊疗。\n诊断: 2型糖尿病\n打印日期: 2024-09-13 13:24:15\n医生签名: 主治医师\n乔明磊",
    "role": "user"
  }
]
2026-08-10 07:15:14,510 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:14,510 INFO     29 [qwen-vl-text] LLM output (len=248):
{
  "encounter_date": "2024-09-13",
  "chief_complaint": "诊断2型糖尿病4年",
  "present_illness": "诊断2型糖尿病4年。",
  "past_history": "否认食物、药物过敏史。",
  "diagnosis": "2型糖尿病",
  "treatment_plan": "二甲双胍片每日3次每次0.5g治疗。糖尿病健康知识宣教, 糖尿病饮食, 监测血糖, 适当运动。注意复查。必要时上级医院诊疗。"
}
2026-08-10 07:15:14,510 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-09-13]
2026-08-10 07:15:14,513 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1883100, prompt_len=1137
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["巴彦县太平社区卫生服务中心病历信息", "门诊编号:", "姓名:", "性别: 女", "科室: 门诊", "年龄: 63岁", "过敏史: 无", "发病时间: 2024-09-13", "身高:", "体重:", "血压: 130/85mmHg", "血糖:", "体温: 36.5℃", "脉搏: 65次/min", "主诉: 诊断2型糖尿病4年", "既往史: 否认食物、药物过敏史。", "现病史: 诊断2型糖尿病4年。", "体格检查: 神清语利, 精神可。颈软, 无抵抗。两侧瞳孔正大等圆, 对光反射灵敏。", "双肺呼吸音清, 未闻及干、湿性啰音。心音可, 心律齐, 各瓣膜听诊区未闻及病理", "性杂音。腹软, 无压痛、反跳痛及肌紧张。", "辅助检查: 血糖、糖化血红蛋白", "健康评估: 慢病工程, 病情平稳, 一般情况可, 生命体征平稳。", "治疗意见: 二甲双胍片每日3次每次0.5g治疗。糖尿病健康知识宣教, 糖尿病饮食,", "监测血糖, 适当运动。注意复查。必要时上级医院诊疗。", "诊断: 2型糖尿病", "打印日期: 2024-09-13 13:24:15", "医生签名: 主治医师", "乔明磊"]

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
2026-08-10 07:15:26,770 INFO     29 [qwen-vl-text] coord API raw response (len=1675):
[
	{"text": "巴彦县太平社区卫生服务中心病历信息", "bbox": [328, 125, 603, 173]},
	{"text": "门诊编号:", "bbox": [228, 241, 284, 267]},
	{"text": "姓名:", "bbox": [378, 235, 410, 260]},
	{"text": "性别: 女", "bbox": [509, 224, 558, 250]},
	{"text": "科室: 门诊", "bbox": [608, 213, 674, 241]},
	{"text": "年龄: 63岁", "bbox": [228, 272, 295, 297]},
	{"text": "过敏史: 无", "bbox": [378, 264, 442, 290]},
	{"text": "发病时间: 2024-09-13", "bbox": [509, 252, 633, 280]},
	{"text": "身高:", "bbox": [228, 306, 260, 330]},
	{"text": "体重:", "bbox": [378, 298, 410, 323]},
	{"text": "血压: 130/85mmHg", "bbox": [510, 286, 621, 313]},
	{"text": "血糖:", "bbox": [228, 338, 260, 362]},
	{"text": "体温: 36.5℃", "bbox": [379, 329, 452, 355]},
	{"text": "脉搏: 65次/min", "bbox": [510, 320, 603, 346]},
	{"text": "主诉: 诊断2型糖尿病4年", "bbox": [229, 363, 382, 391]},
	{"text": "既往史: 否认食物、药物过敏史。", "bbox": [229, 393, 412, 421]},
	{"text": "现病史: 诊断2型糖尿病4年。", "bbox": [229, 424, 400, 453]},
	{"text": "体格检查: 神清语利, 精神可。颈软, 无抵抗。两侧瞳孔正大等圆, 对光反射灵敏。", "bbox": [229, 440, 693, 484]},
	{"text": "双肺呼吸音清, 未闻及干、湿性啰音。心音可, 心律齐, 各瓣膜听诊区未闻及病理", "bbox": [229, 471, 688, 515]},
	{"text": "性杂音。腹软, 无压痛、反跳痛及肌紧张。", "bbox": [229, 514, 462, 547]},
	{"text": "辅助检查: 血糖、糖化血红蛋白", "bbox": [229, 548, 407, 579]},
	{"text": "健康评估: 慢病工程, 病情平稳, 一般情况可, 生命体征平稳。", "bbox": [229, 573, 577, 611]},
	{"text": "治疗意见: 二甲双胍片每日3次每次0.5g治疗。糖尿病健康知识宣教, 糖尿病饮食,", "bbox": [229, 601, 699, 644]},
	{"text": "监测血糖, 适当运动。注意复查。必要时上级医院诊疗。", "bbox": [229, 640, 540, 675]},
	{"text": "诊断: 2型糖尿病", "bbox": [228, 682, 329, 709]},
	{"text": "打印日期: 2024-09-13 13:24:15", "bbox": [228, 745, 402, 773]},
	{"text": "医生签名: 主治医师", "bbox": [540, 735, 647, 766]},
	{"text": "乔明磊", "bbox": [600, 773, 647, 810]}
]
2026-08-10 07:15:26,770 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=12.3s
2026-08-10 07:15:26,770 INFO     29 [qwen-vl-text] coord item[0]: text=巴彦县太平社区卫生服务中心病历信息, bbox=[328, 125, 603, 173]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[1]: text=门诊编号:, bbox=[228, 241, 284, 267]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[378, 235, 410, 260]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 女, bbox=[509, 224, 558, 250]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[4]: text=科室: 门诊, bbox=[608, 213, 674, 241]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[5]: text=年龄: 63岁, bbox=[228, 272, 295, 297]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[6]: text=过敏史: 无, bbox=[378, 264, 442, 290]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[7]: text=发病时间: 2024-09-13, bbox=[509, 252, 633, 280]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[8]: text=身高:, bbox=[228, 306, 260, 330]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[9]: text=体重:, bbox=[378, 298, 410, 323]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[10]: text=血压: 130/85mmHg, bbox=[510, 286, 621, 313]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[11]: text=血糖:, bbox=[228, 338, 260, 362]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[12]: text=体温: 36.5℃, bbox=[379, 329, 452, 355]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[13]: text=脉搏: 65次/min, bbox=[510, 320, 603, 346]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[14]: text=主诉: 诊断2型糖尿病4年, bbox=[229, 363, 382, 391]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[15]: text=既往史: 否认食物、药物过敏史。, bbox=[229, 393, 412, 421]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[16]: text=现病史: 诊断2型糖尿病4年。, bbox=[229, 424, 400, 453]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[17]: text=体格检查: 神清语利, 精神可。颈软, 无抵抗。两侧瞳孔正大等圆, 对光反射灵敏。, bbox=[229, 440, 693, 484]
2026-08-10 07:15:26,771 INFO     29 [qwen-vl-text] coord item[18]: text=双肺呼吸音清, 未闻及干、湿性啰音。心音可, 心律齐, 各瓣膜听诊区未闻及病理, bbox=[229, 471, 688, 515]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[19]: text=性杂音。腹软, 无压痛、反跳痛及肌紧张。, bbox=[229, 514, 462, 547]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查: 血糖、糖化血红蛋白, bbox=[229, 548, 407, 579]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[21]: text=健康评估: 慢病工程, 病情平稳, 一般情况可, 生命体征平稳。, bbox=[229, 573, 577, 611]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[22]: text=治疗意见: 二甲双胍片每日3次每次0.5g治疗。糖尿病健康知识宣教, 糖尿病饮食,, bbox=[229, 601, 699, 644]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[23]: text=监测血糖, 适当运动。注意复查。必要时上级医院诊疗。, bbox=[229, 640, 540, 675]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[24]: text=诊断: 2型糖尿病, bbox=[228, 682, 329, 709]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[25]: text=打印日期: 2024-09-13 13:24:15, bbox=[228, 745, 402, 773]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[26]: text=医生签名: 主治医师, bbox=[540, 735, 647, 766]
2026-08-10 07:15:26,772 INFO     29 [qwen-vl-text] coord item[27]: text=乔明磊, bbox=[600, 773, 647, 810]
2026-08-10 07:15:26,773 INFO     29 [qwen-vl-text] page=1 — 28/28 coords, api_time=12.3s
2026-08-10 07:15:26,773 INFO     29 [qwen-vl-text] new_positions (28):
[[1, 472.32, 868.3199999999999, 101.25, 140.13], [1, 328.32, 408.96, 195.21, 216.27], [1, 544.3199999999999, 590.4, 190.35000000000002, 210.60000000000002], [1, 732.9599999999999, 803.52, 181.44, 202.5], [1, 875.52, 970.56, 172.53, 195.21], [1, 328.32, 424.8, 220.32000000000002, 240.57000000000002], [1, 544.3199999999999, 636.48, 213.84, 234.9], [1, 732.9599999999999, 911.52, 204.12, 226.8], [1, 328.32, 374.4, 247.86, 267.3], [1, 544.3199999999999, 590.4, 241.38000000000002, 261.63], [1, 734.4, 894.24, 231.66000000000003, 253.53000000000003], [1, 328.32, 374.4, 273.78000000000003, 293.22], [1, 545.76, 650.88, 266.49, 287.55], [1, 734.4, 868.3199999999999, 259.20000000000005, 280.26], [1, 329.76, 550.0799999999999, 294.03000000000003, 316.71000000000004], [1, 329.76, 593.28, 318.33000000000004, 341.01000000000005], [1, 329.76, 576.0, 343.44, 366.93], [1, 329.76, 997.92, 356.40000000000003, 392.04], [1, 329.76, 990.7199999999999, 381.51000000000005, 417.15000000000003], [1, 329.76, 665.28, 416.34000000000003, 443.07000000000005], [1, 329.76, 586.0799999999999, 443.88000000000005, 468.99], [1, 329.76, 830.88, 464.13000000000005, 494.91], [1, 329.76, 1006.56, 486.81000000000006, 521.64], [1, 329.76, 777.6, 518.4000000000001, 546.75], [1, 328.32, 473.76, 552.4200000000001, 574.2900000000001], [1, 328.32, 578.88, 603.45, 626.13], [1, 777.6, 931.68, 595.35, 620.46], [1, 864.0, 931.68, 626.13, 656.1]]
2026-08-10 07:15:26,773 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=14.1s
2026-08-10 07:15:26,790 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 07:15:26,791 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:15:26,791 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 07:15:26,791 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:15:26.791+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 12, "failed": 0, "current": {"166b6a2e948b11f1bd9827cf206dfa2d": {"id": "166b6a2e948b11f1bd9827cf206dfa2d", "doc_id": "163668e2948b11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "size": 1888060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786346052273, "task_type": "dataflow", "root_trace_id": "d7cd678f6b6e421d965ddc3b62b23ca3", "root_traceparent": "00-d7cd678f6b6e421d965ddc3b62b23ca3-950bc6afdd8d5782-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:15:26,798 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:15:26,799 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:15:26,799 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 07:15:26,800 INFO     29 [qwen-vl-text] positions(22): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:15:26,800 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [22]
2026-08-10 07:15:27,067 INFO     29 [qwen-vl-text] page=5, rect=810x1440, img=(2250x4000), dpi=200
2026-08-10 07:15:27,068 INFO     29 [qwen-vl-text] LLM extraction start, text_len=219
2026-08-10 07:15:27,068 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:27,069 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 69, \"bbox_end\": 90, \"encounter_dates\": [\"2025-01-19\"], \"department\": \"普通门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "巴彦县太平社区卫生服务中\n门诊缴费凭证\n姓名：\n就诊卡号：\n性别：女\n年龄：64岁\n病人ID：\n缴费流水号：2025011900141\n医保类别：\n缴费方式：□公□自□保\n就诊科室：普通门诊\n接诊医生：刘璐璐\n收费项目\n数量\n金额\n盐酸二甲双胍缓释片/北京悦康\n0.5g×30片/盒\n20.0盒X 7.50元=150.00\n操作员：5556\n收款时间：2025-01-19 13:16:14\n温馨提示\n本凭条为本次缴款凭据，不做报销凭证。",
    "role": "user"
  }
]
2026-08-10 07:15:29,641 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:29,641 INFO     29 [qwen-vl-text] LLM output (len=426):
{
  "encounter_date": "2025-01-19",
  "pharmacy": "巴彦县太平社区卫生服务中",
  "medications": [
    {
      "name": "盐酸二甲双胍缓释片",
      "specification": "0.5g×30片/盒",
      "dosage": null,
      "quantity": 20.0,
      "unit_price": 7.50,
      "total_price": 150.00,
      "frequency": null,
      "route": null,
      "manufacturer": "北京悦康",
      "approval_number": null
    }
  ],
  "payment_total": 150.00,
  "payment_method": null
}
2026-08-10 07:15:29,641 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-19]
2026-08-10 07:15:29,648 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2037973, prompt_len=898
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["巴彦县太平社区卫生服务中", "门诊缴费凭证", "姓名：", "就诊卡号：", "性别：女", "年龄：64岁", "病人ID：", "缴费流水号：2025011900141", "医保类别：", "缴费方式：□公□自□保", "就诊科室：普通门诊", "接诊医生：刘璐璐", "收费项目", "数量", "金额", "盐酸二甲双胍缓释片/北京悦康", "0.5g×30片/盒", "20.0盒X 7.50元=150.00", "操作员：5556", "收款时间：2025-01-19 13:16:14", "温馨提示", "本凭条为本次缴款凭据，不做报销凭证。"]

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
2026-08-10 07:15:39,004 INFO     29 [qwen-vl-text] coord API raw response (len=1190):
[
	{"text": "巴彦县太平社区卫生服务中", "bbox": [234, 144, 688, 178]},
	{"text": "门诊缴费凭证", "bbox": [369, 173, 603, 206]},
	{"text": "姓名：", "bbox": [196, 214, 360, 248]},
	{"text": "就诊卡号：", "bbox": [196, 243, 360, 276]},
	{"text": "性别：女", "bbox": [196, 273, 439, 310]},
	{"text": "年龄：64岁", "bbox": [196, 305, 484, 340]},
	{"text": "病人ID：", "bbox": [194, 333, 356, 365]},
	{"text": "缴费流水号：2025011900141", "bbox": [194, 363, 668, 398]},
	{"text": "医保类别：", "bbox": [194, 393, 360, 425]},
	{"text": "缴费方式：□公□自□保", "bbox": [194, 424, 632, 458]},
	{"text": "就诊科室：普通门诊", "bbox": [194, 456, 555, 489]},
	{"text": "接诊医生：刘璐璐", "bbox": [194, 487, 518, 518]},
	{"text": "收费项目", "bbox": [194, 542, 328, 567]},
	{"text": "数量", "bbox": [382, 546, 449, 569]},
	{"text": "金额", "bbox": [522, 544, 590, 568]},
	{"text": "盐酸二甲双胍缓释片/北京悦康", "bbox": [194, 575, 656, 601]},
	{"text": "0.5g×30片/盒", "bbox": [329, 610, 567, 634]},
	{"text": "20.0盒X 7.50元=150.00", "bbox": [190, 640, 690, 667]},
	{"text": "操作员：5556", "bbox": [187, 708, 411, 734]},
	{"text": "收款时间：2025-01-19 13:16:14", "bbox": [187, 740, 715, 767]},
	{"text": "温馨提示", "bbox": [387, 808, 535, 833]},
	{"text": "本凭条为本次缴款凭据，不做报销凭证。", "bbox": [185, 843, 693, 874]}
]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=9.4s
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[0]: text=巴彦县太平社区卫生服务中, bbox=[234, 144, 688, 178]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[1]: text=门诊缴费凭证, bbox=[369, 173, 603, 206]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[196, 214, 360, 248]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[3]: text=就诊卡号：, bbox=[196, 243, 360, 276]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[196, 273, 439, 310]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：64岁, bbox=[196, 305, 484, 340]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[6]: text=病人ID：, bbox=[194, 333, 356, 365]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[7]: text=缴费流水号：2025011900141, bbox=[194, 363, 668, 398]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[8]: text=医保类别：, bbox=[194, 393, 360, 425]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[9]: text=缴费方式：□公□自□保, bbox=[194, 424, 632, 458]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[10]: text=就诊科室：普通门诊, bbox=[194, 456, 555, 489]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[11]: text=接诊医生：刘璐璐, bbox=[194, 487, 518, 518]
2026-08-10 07:15:39,005 INFO     29 [qwen-vl-text] coord item[12]: text=收费项目, bbox=[194, 542, 328, 567]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[13]: text=数量, bbox=[382, 546, 449, 569]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[14]: text=金额, bbox=[522, 544, 590, 568]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[15]: text=盐酸二甲双胍缓释片/北京悦康, bbox=[194, 575, 656, 601]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[16]: text=0.5g×30片/盒, bbox=[329, 610, 567, 634]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[17]: text=20.0盒X 7.50元=150.00, bbox=[190, 640, 690, 667]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[18]: text=操作员：5556, bbox=[187, 708, 411, 734]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[19]: text=收款时间：2025-01-19 13:16:14, bbox=[187, 740, 715, 767]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[20]: text=温馨提示, bbox=[387, 808, 535, 833]
2026-08-10 07:15:39,006 INFO     29 [qwen-vl-text] coord item[21]: text=本凭条为本次缴款凭据，不做报销凭证。, bbox=[185, 843, 693, 874]
2026-08-10 07:15:39,007 INFO     29 [qwen-vl-text] page=5 — 22/22 coords, api_time=9.4s
2026-08-10 07:15:39,007 INFO     29 [qwen-vl-text] new_positions (22):
[[5, 189.54000000000002, 557.2800000000001, 207.35999999999999, 256.32], [5, 298.89000000000004, 488.43, 249.12, 296.64], [5, 158.76000000000002, 291.6, 308.15999999999997, 357.12], [5, 158.76000000000002, 291.6, 349.91999999999996, 397.44], [5, 158.76000000000002, 355.59000000000003, 393.12, 446.4], [5, 158.76000000000002, 392.04, 439.2, 489.59999999999997], [5, 157.14000000000001, 288.36, 479.52, 525.6], [5, 157.14000000000001, 541.08, 522.72, 573.12], [5, 157.14000000000001, 291.6, 565.92, 612.0], [5, 157.14000000000001, 511.92, 610.56, 659.52], [5, 157.14000000000001, 449.55, 656.64, 704.16], [5, 157.14000000000001, 419.58000000000004, 701.28, 745.92], [5, 157.14000000000001, 265.68, 780.48, 816.48], [5, 309.42, 363.69, 786.24, 819.36], [5, 422.82000000000005, 477.90000000000003, 783.36, 817.92], [5, 157.14000000000001, 531.36, 828.0, 865.4399999999999], [5, 266.49, 459.27000000000004, 878.4, 912.9599999999999], [5, 153.9, 558.9000000000001, 921.5999999999999, 960.48], [5, 151.47, 332.91, 1019.52, 1056.96], [5, 151.47, 579.1500000000001, 1065.6, 1104.48], [5, 313.47, 433.35, 1163.52, 1199.52], [5, 149.85000000000002, 561.33, 1213.9199999999998, 1258.56]]
2026-08-10 07:15:39,007 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=12.2s
2026-08-10 07:15:39,022 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 07:15:39,022 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Extractor:Medication | outputs={"chunks": "1 items, types={'MedicationRecord': 1}", "html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:15:39,022 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 07:15:39,034 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:39,034 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 07:15:40,344 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:40,356 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 07:15:40,356 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:15:40,356 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 07:15:40,366 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:40,367 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 07:15:41,047 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:41,058 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 07:15:41,059 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:15:41,059 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 07:15:41,070 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:41,070 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 07:15:41,702 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:41,709 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 07:15:41,709 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:15:41,710 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 07:15:41,716 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:41,716 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 07:15:43,556 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:15:43,566 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 07:15:43,567 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "91 items", "markdown": "", "text": "", "name": "WYPi-哈大四-糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 3, \"chunks_Medication\": 1}"}
2026-08-10 07:15:43,567 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 07:15:43,567 INFO     29 [ChunkMerger] Merged 5 chunks from 8 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 5 noise chunks)
2026-08-10 07:15:43,586 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 07:15:43,586 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "5 items, types={'LabReport': 3, 'OutpatientRecord': 1, 'MedicationRecord': 1}", "name": "WYPi-哈大四-糖尿病.pdf"}
2026-08-10 07:15:43,586 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 07:15:43,632 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786346052480, 'update_date': datetime.datetime(2026, 8, 10, 7, 14, 12), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 819092, 'status': '1'}
2026-08-10 07:15:43,897 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白  HbA1c  8.04  %  4.00-6.00  True   
---
   葡萄糖  GLU  8.24  mmol/L  3.90-6.10  True   
---
   糖化血红蛋白  HbA1c  8.6  %  3.6-6.0  True   
---
巴彦县太平社区卫生服务中心病历信息
门诊编号:
姓名:
性别: 女
科室: 门诊
年龄: 63岁
过敏史: 无
发病时间: 2024-09-13
身高:
体重:
血压: 130/85mmHg
血糖:
体温: 36.5℃
脉搏: 65次/min
主诉: 诊断2型糖尿病4年
既往史: 否认食物、药物过敏史。
现病史: 诊断2型糖尿病4年。
体格检查: 神清语利, 精神可。颈软, 无抵抗。两侧瞳孔正大等圆, 对光反射灵敏。
双肺呼吸音清, 未闻及干、湿性啰音。心音可, 心律齐, 各瓣膜听诊区未闻及病理
性杂音。腹软, 无压痛、反跳痛及肌紧张。
辅助检查: 血糖、糖化血红蛋白
健康评估: 慢病工程, 病情平稳, 一般情况可, 生命体征平稳。
治疗意见: 二甲双胍片每日3次每次0.5g治疗。糖尿病健康知识宣教, 糖尿病饮食,
监测血糖, 适当运动。注意复查。必要时上级医院诊疗。
诊断: 2型糖尿病
打印日期: 2024-09-13 13:24:15
医生签名: 主治医师
乔明磊
---
巴彦县太平社区卫生服务中
门诊缴费凭证
姓名：
就诊卡号：
性别：女
年龄：64岁
病人ID：
缴费流水号：2025011900141
医保类别：
缴费方式：□公□自□保
就诊科室：普通门诊
接诊医生：刘璐璐
收费项目
数量
金额
盐酸二甲双胍缓释片/北京悦康
0.5g×30片/盒
20.0盒X 7.50元=150.00
操作员：5556
收款时间：2025-01-19 13:16:14
温馨提示
本凭条为本次缴款凭据，不做报销凭证。
2026-08-10 07:15:44,169 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 07:15:44,169 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "5 items, types={'LabReport': 3, 'OutpatientRecord': 1, 'MedicationRecord': 1}", "name": "WYPi-哈大四-糖尿病.pdf", "embedding_token_consumption": 644}
2026-08-10 07:15:44,169 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 07:15:44,414 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 07:15:44,415 INFO     29 [Trace] task=166b6a2e | doc=WYPi-哈大四-糖尿病.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":5,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 07:15:44,419 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(3, 51, 162, 408, 432) row[-1]=(3, 51, 162, 408, 432)
2026-08-10 07:15:44,419 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 94, 132, 440, 460) row[-1]=(4, 94, 132, 440, 460)
2026-08-10 07:15:44,419 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(5, 109, 184, 442, 457) row[-1]=(5, 109, 184, 442, 457)
2026-08-10 07:15:44,419 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:15:44,419 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:15:44,428 INFO     29 set_progress(166b6a2e948b11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 07:15:44 [DOC Engine]:
Start to index...
2026-08-10 07:15:44,473 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.035s]
2026-08-10 07:15:44,566 INFO     29 set_progress(166b6a2e948b11f1bd9827cf206dfa2d), progress: 0.8200000000000001, progress_msg: 
2026-08-10 07:15:44,590 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.017s]
2026-08-10 07:15:44,602 INFO     29 set_progress(166b6a2e948b11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 07:15:44 Indexing done (0.18s). Task done (91.98s)
2026-08-10 07:15:44,607 INFO     29 [Done], chunks(5), token(644), elapsed:91.98
2026-08-10 07:15:44,676 INFO     29 handle_task done for task {"id": "166b6a2e948b11f1bd9827cf206dfa2d", "doc_id": "163668e2948b11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYPi-\u54c8\u5927\u56db-\u7cd6\u5c3f\u75c5.pdf", "size": 1888060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786346052273, "task_type": "dataflow", "root_trace_id": "d7cd678f6b6e421d965ddc3b62b23ca3", "root_traceparent": "00-d7cd678f6b6e421d965ddc3b62b23ca3-950bc6afdd8d5782-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
