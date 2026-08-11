# 基准结果：Bxli糖尿病 郑州中心.pdf

## 基本信息

- 文件：`Bxli糖尿病 郑州中心.pdf`
- 大小：1126.6 KB
- PDF 总页数：7
- doc_id：`1dee142694be11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:19:28  完成时间：2026-08-10T21:21:06  耗时：98.1s
- progress_msg：`13:21:03 Indexing done (0.05s). Task done (88.70s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 5edba32e | 1 | 1-1 | 中西医结合医院 病人门（急）诊病历 病人ID M024474 姓名 性别：女 出 |
| 2 | eddae4ea | 1 | 2-2 | 医结合医院处方笺 普通 性别：女 年龄：67岁 费别：自费 病人ID：M0244 |
| 3 | d54334e3 | 1 | 3-3 | 页中西医结合医院处方笺 普通 姓名 性别：女 年龄：66岁 费别：自费 病人ID |
| 4 | dc4085da | 1 | 6-6 | 百顺中西医结合医院 527836 自费 西药费 50.00 大额记账： 大病补充 |
| 5 | 2d74a5a0 | 1 | 7-7 | 20250507530576 新密佰顺中西医结合医院 530576 女 自费 西 |
| 6 | 7bee5e6e | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 7 | 8e1f5b58 | 1 | 5-5 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6, 7]`
- 覆盖页数：7 / 7；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 2 | 2 | 2 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 2 | 0 | 2 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "PrescriptionRecord": 2, "LabReport": 2, "MedicationRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 7, "sources": 9, "stats": {"Extractor:LabExam": 2, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 2, "Extractor:Prescription": 2, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:21:03,138 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:19:30,806 INFO     29 handle_task begin for task {"id": "1e2e962294be11f1bd9827cf206dfa2d", "doc_id": "1dee142694be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "type": "pdf", "location": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "size": 1153670, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367969629, "task_type": "dataflow", "root_trace_id": "c156a740bf4445608a67c6fa5390ecc5", "root_traceparent": "00-c156a740bf4445608a67c6fa5390ecc5-80117852a55b854d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:19:31,026 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:19:31,138 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:19:31,147 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:19:31,147 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:19:31,147 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:19:31,152 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:19:31,152 INFO     29 ============================================================
2026-08-10 13:19:31,152 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:19:31,152 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:19:31,152 INFO     29 ============================================================
2026-08-10 13:19:31,152 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:19:31,152 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:19:31,153 INFO     29 No torch found.
2026-08-10 13:19:31,860 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=7
2026-08-10 13:19:31,961 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=764421, prompt_len=764
2026-08-10 13:19:33,277 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:19:33,277 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:19:33,289 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=764421, prompt_len=401
2026-08-10 13:19:36,192 INFO     29 [qwen-vl-parser] text API response (len=480):
["中西医结合医院", "病人门（急）诊病历", "病人ID M024474 姓名", "性别：女 出生时间： 1958年8月27日", "籍贯：河南郑州市 民族：汉族 婚否：已婚 职业：无", "身份", "电话号码", "17", "工作单位： 常住地址：郑州市金水区花园路39号3号院", "门诊号： 74164 接诊时间： 2025年1月8日9时38分", "就诊时间：2025-1-8 09:41:09 体温：36.3℃", "主诉：尿里边带泡沫，去大药店门口测血糖买二甲双胍片。", "现病史：口干，喝水多，尿里带泡沫，来我院检查治疗。", "体格检查：", "西医诊断：1.糖尿病 中医诊断：", "建议： 1、糖尿病饮食；保持心情愉悦；", "2、适量运动；", "3、规律服药；", "4、定期监测血糖；", "5、不适随诊。", "过敏史：无", "家族史：无", "既往史：无", "处理：给予二甲双胍片口服，空腹血糖、糖化血红蛋白检测，以了解血糖控制情况", "备注：", "打印时间：2025-1-8 科室：内科门诊 医生：张建鹏"]
2026-08-10 13:19:36,192 INFO     29 [qwen-vl-parser] page=1 text: 26 lines (bbox 0-25)
2026-08-10 13:19:36,192 INFO     29 [qwen-vl-parser] page=1 text: 26 sections
2026-08-10 13:19:36,316 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=539324, prompt_len=764
2026-08-10 13:19:37,571 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:19:37,571 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:19:37,578 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=539324, prompt_len=401
2026-08-10 13:19:39,437 INFO     29 [qwen-vl-parser] text API response (len=304):
["医结合医院处方笺", "普通", "性别：女", "年龄：67岁", "费别：自费", "病人ID：M024474", "处方号：74164", "就诊序号：52849", "体重：/（kg）", "药物过敏史：无", "住址：郑州市金水区花园路39号院", "开方日期：2025-1-8 09:41", "就诊科室：内科门诊", "临床诊断：糖尿病", "Rp:", "盐酸二甲双胍片", "0.5g*60 X 5盒", "用法：每次0.5g 一日三次 口服", "备注：", "医师：张建鹏", "审核：", "核对：", "金额合计：50.00元", "调配：", "发药：", "药房：西药费"]
2026-08-10 13:19:39,438 INFO     29 [qwen-vl-parser] page=2 text: 26 lines (bbox 26-51)
2026-08-10 13:19:39,438 INFO     29 [qwen-vl-parser] page=2 text: 26 sections
2026-08-10 13:19:39,551 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=445725, prompt_len=764
2026-08-10 13:19:40,843 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:19:40,843 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 13:19:40,853 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=445725, prompt_len=401
2026-08-10 13:19:42,691 INFO     29 [qwen-vl-parser] text API response (len=301):
["页中西医结合医院处方笺", "普通", "姓名", "性别：女", "年龄：66岁", "费别：自费", "病人ID：M024474", "处方号：74165", "就诊序号：74164", "体重：/（kg）", "药物过敏史：无", "住址：", "开方日期：2025-05-07 09:39", "就诊科室：内科门诊", "临床诊断：糖尿病", "Rp：", "盐酸二甲双胍片", "0.5g", "X 5盒", "用法：每次0.5g TID 口服", "备注：", "医师：张建鹏", "审核：", "核对：", "金额合计：50.00元", "调配：", "发药：", "药房：西药房"]
2026-08-10 13:19:42,691 INFO     29 [qwen-vl-parser] page=3 text: 28 lines (bbox 52-79)
2026-08-10 13:19:42,692 INFO     29 [qwen-vl-parser] page=3 text: 28 sections
2026-08-10 13:19:42,827 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=677706, prompt_len=764
2026-08-10 13:19:44,297 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-01-08"
}
```
2026-08-10 13:19:44,298 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-01-08
2026-08-10 13:19:44,304 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=677706, prompt_len=756
2026-08-10 13:19:45,659 INFO     29 [qwen-vl-parser] table API response (len=199):
\begin{tabular}{cccccc}
\hline
姓名: & & 性别: 女 & 年龄: 67 & 送检科 & 标本状态: \\
\hline
& 项目名称 & 结果 & 参考范围 & 送检日期: & 标本类型: 静脉全血 \\
\hline
& 糖化血红蛋白 (HbA1c) & 8.6\% & 4-6\% & 2025-01-08 & \\
\hline
\end{tabular}
2026-08-10 13:19:45,660 INFO     29 [qwen-vl-parser] page=4 table: 10 LaTeX lines (bbox 80-89)
2026-08-10 13:19:45,660 INFO     29 [qwen-vl-parser] page=4 table: 10 sections
2026-08-10 13:19:45,787 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=644636, prompt_len=764
2026-08-10 13:19:48,673 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-05-07"
}
```
2026-08-10 13:19:48,673 INFO     29 [qwen-vl-parser] page=5 classify=table report_date=2025-05-07
2026-08-10 13:19:48,683 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=644636, prompt_len=756
2026-08-10 13:19:50,715 INFO     29 [qwen-vl-parser] table API response (len=407):
\begin{tabular}{ccccccccc}
\hline
\multicolumn{9}{c}{\textbf{顺中西医结合医院}} \\
\hline
姓名: & & & & & & & & \\
性别: 女 & 年龄: 67 & & & & & & & \\
送检科: & 室: 门诊 & & & & & & & \\
标本状态: 正常 & 标本类型: 静脉全血 & & & & & & & \\
送检日期: 2025-05-07 & & & & & & & & \\
\hline
项目名称 & & & & 结果 & & & & \\
\hline
糖化血红蛋白 (HbA1c) & & & & 11.2\% & & & & \\
\hline
& & & & & 参考范围 & & & \\
\hline
& & & & & 4-6\% & & & \\
\hline
\end{tabular}
2026-08-10 13:19:50,716 INFO     29 [qwen-vl-parser] page=5 table: 20 LaTeX lines (bbox 90-109)
2026-08-10 13:19:50,716 INFO     29 [qwen-vl-parser] page=5 table: 20 sections
2026-08-10 13:19:50,849 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=531357, prompt_len=764
2026-08-10 13:19:52,228 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:19:52,228 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 13:19:52,234 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=531357, prompt_len=401
2026-08-10 13:19:53,238 INFO     29 [qwen-vl-parser] text API response (len=128):
["百顺中西医结合医院", "527836", "自费", "西药费", "50.00", "大额记账：", "大病补充：", "原账户余额：", "现金支付：", "伍拾元整", "50.00", "27836", "0061", "2025-01-"]
2026-08-10 13:19:53,238 INFO     29 [qwen-vl-parser] page=6 text: 14 lines (bbox 110-123)
2026-08-10 13:19:53,238 INFO     29 [qwen-vl-parser] page=6 text: 14 sections
2026-08-10 13:19:53,427 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=776937, prompt_len=764
2026-08-10 13:19:54,812 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:19:54,813 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 13:19:54,828 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=776937, prompt_len=401
2026-08-10 13:19:55,508 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:19:55.507+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 45, "failed": 0, "current": {"1e2e962294be11f1bd9827cf206dfa2d": {"id": "1e2e962294be11f1bd9827cf206dfa2d", "doc_id": "1dee142694be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "type": "pdf", "location": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "size": 1153670, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367969629, "task_type": "dataflow", "root_trace_id": "c156a740bf4445608a67c6fa5390ecc5", "root_traceparent": "00-c156a740bf4445608a67c6fa5390ecc5-80117852a55b854d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:19:55,853 INFO     29 [qwen-vl-parser] text API response (len=124):
["20250507530576", "新密佰顺中西医结合医院", "530576", "女", "自费", "西药费", "50.00", "大额记账：", "大病补充：", "原帐户余额：", "现金支付：", "伍拾元整", "50.00"]
2026-08-10 13:19:55,854 INFO     29 [qwen-vl-parser] page=7 text: 13 lines (bbox 124-136)
2026-08-10 13:19:55,854 INFO     29 [qwen-vl-parser] page=7 text: 13 sections
2026-08-10 13:19:55,854 INFO     29 [qwen-vl-parser] parse_pdf done: 137 sections from 7 pages.
2026-08-10 13:19:55,867 INFO     29 Close text detector.
2026-08-10 13:19:56,320 INFO     29 Close text recognizer.
2026-08-10 13:19:56,707 INFO     29 Close recognizer.
2026-08-10 13:19:57,163 INFO     29 Close recognizer.
2026-08-10 13:19:57,838 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:19:57,838 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Parser:MedLink | outputs={"html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "json"}
2026-08-10 13:19:57,838 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:19:57,854 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:19:57,854 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 中西医结合医院\n[BBOX-1] 病人门（急）诊病历\n[BBOX-2] 病人ID M024474 姓名\n[BBOX-3] 性别：女 出生时间： 1958年8月27日\n[BBOX-4] 籍贯：河南郑州市 民族：汉族 婚否：已婚 职业：无\n[BBOX-5] 身份\n[BBOX-6] 电话号码\n[BBOX-7] 17\n[BBOX-8] 工作单位： 常住地址：郑州市金水区花园路39号3号院\n[BBOX-9] 门诊号： 74164 接诊时间： 2025年1月8日9时38分\n[BBOX-10] 就诊时间：2025-1-8 09:41:09 体温：36.3℃\n[BBOX-11] 主诉：尿里边带泡沫，去大药店门口测血糖买二甲双胍片。\n[BBOX-12] 现病史：口干，喝水多，尿里带泡沫，来我院检查治疗。\n[BBOX-13] 体格检查：\n[BBOX-14] 西医诊断：1.糖尿病 中医诊断：\n[BBOX-15] 建议： 1、糖尿病饮食；保持心情愉悦；\n[BBOX-16] 2、适量运动；\n[BBOX-17] 3、规律服药；\n[BBOX-18] 4、定期监测血糖；\n[BBOX-19] 5、不适随诊。\n[BBOX-20] 过敏史：无\n[BBOX-21] 家族史：无\n[BBOX-22] 既往史：无\n[BBOX-23] 处理：给予二甲双胍片口服，空腹血糖、糖化血红蛋白检测，以了解血糖控制情况\n[BBOX-24] 备注：\n[BBOX-25] 打印时间：2025-1-8 科室：内科门诊 医生：张建鹏\n[BBOX-26] 医结合医院处方笺\n[BBOX-27] 普通\n[BBOX-28] 性别：女\n[BBOX-29] 年龄：67岁\n[BBOX-30] 费别：自费\n[BBOX-31] 病人ID：M024474\n[BBOX-32] 处方号：74164\n[BBOX-33] 就诊序号：52849\n[BBOX-34] 体重：/（kg）\n[BBOX-35] 药物过敏史：无\n[BBOX-36] 住址：郑州市金水区花园路39号院\n[BBOX-37] 开方日期：2025-1-8 09:41\n[BBOX-38] 就诊科室：内科门诊\n[BBOX-39] 临床诊断：糖尿病\n[BBOX-40] Rp:\n[BBOX-41] 盐酸二甲双胍片\n[BBOX-42] 0.5g*60 X 5盒\n[BBOX-43] 用法：每次0.5g 一日三次 口服\n[BBOX-44] 备注：\n[BBOX-45] 医师：张建鹏\n[BBOX-46] 审核：\n[BBOX-47] 核对：\n[BBOX-48] 金额合计：50.00元\n[BBOX-49] 调配：\n[BBOX-50] 发药：\n[BBOX-51] 药房：西药费\n[BBOX-52] 页中西医结合医院处方笺\n[BBOX-53] 普通\n[BBOX-54] 姓名\n[BBOX-55] 性别：女\n[BBOX-56] 年龄：66岁\n[BBOX-57] 费别：自费\n[BBOX-58] 病人ID：M024474\n[BBOX-59] 处方号：74165\n[BBOX-60] 就诊序号：74164\n[BBOX-61] 体重：/（kg）\n[BBOX-62] 药物过敏史：无\n[BBOX-63] 住址：\n[BBOX-64] 开方日期：2025-05-07 09:39\n[BBOX-65] 就诊科室：内科门诊\n[BBOX-66] 临床诊断：糖尿病\n[BBOX-67] Rp：\n[BBOX-68] 盐酸二甲双胍片\n[BBOX-69] 0.5g\n[BBOX-70] X 5盒\n[BBOX-71] 用法：每次0.5g TID 口服\n[BBOX-72] 备注：\n[BBOX-73] 医师：张建鹏\n[BBOX-74] 审核：\n[BBOX-75] 核对：\n[BBOX-76] 金额合计：50.00元\n[BBOX-77] 调配：\n[BBOX-78] 发药：\n[BBOX-79] 药房：西药房\n[BBOX-80] \\begin{tabular}{cccccc}\n[BBOX-81] 报告时间: 2025-01-08\n[BBOX-82] \\hline\n[BBOX-83] 姓名: & & 性别: 女 & 年龄: 67 & 送检科 & 标本状态: \\\\\n[BBOX-84] \\hline\n[BBOX-85] & 项目名称 & 结果 & 参考范围 & 送检日期: & 标本类型: 静脉全血 \\\\\n[BBOX-86] \\hline\n[BBOX-87] & 糖化血红蛋白 (HbA1c) & 8.6\\% & 4-6\\% & 2025-01-08 & \\\\\n[BBOX-88] \\hline\n[BBOX-89] \\end{tabular}\n[BBOX-90] \\begin{tabular}{ccccccccc}\n[BBOX-91] 报告时间: 2025-05-07\n[BBOX-92] \\hline\n[BBOX-93] \\multicolumn{9}{c}{\\textbf{顺中西医结合医院}} \\\\\n[BBOX-94] \\hline\n[BBOX-95] 姓名: & & & & & & & & \\\\\n[BBOX-96] 性别: 女 & 年龄: 67 & & & & & & & \\\\\n[BBOX-97] 送检科: & 室: 门诊 & & & & & & & \\\\\n[BBOX-98] 标本状态: 正常 & 标本类型: 静脉全血 & & & & & & & \\\\\n[BBOX-99] 送检日期: 2025-05-07 & & & & & & & & \\\\\n[BBOX-100] \\hline\n[BBOX-101] 项目名称 & & & & 结果 & & & & \\\\\n[BBOX-102] \\hline\n[BBOX-103] 糖化血红蛋白 (HbA1c) & & & & 11.2\\% & & & & \\\\\n[BBOX-104] \\hline\n[BBOX-105] & & & & & 参考范围 & & & \\\\\n[BBOX-106] \\hline\n[BBOX-107] & & & & & 4-6\\% & & & \\\\\n[BBOX-108] \\hline\n[BBOX-109] \\end{tabular}\n[BBOX-110] 百顺中西医结合医院\n[BBOX-111] 527836\n[BBOX-112] 自费\n[BBOX-113] 西药费\n[BBOX-114] 50.00\n[BBOX-115] 大额记账：\n[BBOX-116] 大病补充：\n[BBOX-117] 原账户余额：\n[BBOX-118] 现金支付：\n[BBOX-119] 伍拾元整\n[BBOX-120] 50.00\n[BBOX-121] 27836\n[BBOX-122] 0061\n[BBOX-123] 2025-01-\n[BBOX-124] 20250507530576\n[BBOX-125] 新密佰顺中西医结合医院\n[BBOX-126] 530576\n[BBOX-127] 女\n[BBOX-128] 自费\n[BBOX-129] 西药费\n[BBOX-130] 50.00\n[BBOX-131] 大额记账：\n[BBOX-132] 大病补充：\n[BBOX-133] 原帐户余额：\n[BBOX-134] 现金支付：\n[BBOX-135] 伍拾元整\n[BBOX-136] 50.00"
  }
]
2026-08-10 13:20:03,917 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:03,932 INFO     29 [SmartSplitter] SmartSplitter done: 7 chunks from 7 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'PrescriptionRecord': 2, 'LabReport': 2, 'MedicationRecord': 2}
2026-08-10 13:20:03,939 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:20:03,939 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 1, 'PrescriptionRecord': 2, 'LabReport': 2, 'MedicationRecord': 2}"}
2026-08-10 13:20:03,939 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:20:03,939 INFO     29 [ChunkRouter] Routed 7 chunks into 4 groups: {'chunks_Clinical': 1, 'chunks_Prescription': 2, 'chunks_LabExam': 2, 'chunks_Medication': 2}
2026-08-10 13:20:03,946 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:20:03,946 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | ChunkRouter:Router | outputs={"html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks": "7 items, types={'OutpatientRecord': 1, 'PrescriptionRecord': 2, 'LabReport': 2, 'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:20:03,946 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:20:03,950 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:20:03,951 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:20:03,951 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:20:03,951 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:20:04,099 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 13:20:04,100 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:04,100 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 80, \"bbox_end\": 89, \"encounter_dates\": [\"2025-01-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2025-01-08\n\\hline\n姓名: & & 性别: 女 & 年龄: 67 & 送检科 & 标本状态: \\\\\n\\hline\n& 项目名称 & 结果 & 参考范围 & 送检日期: & 标本类型: 静脉全血 \\\\\n\\hline\n& 糖化血红蛋白 (HbA1c) & 8.6\\% & 4-6\\% & 2025-01-08 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:20:05,309 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:05,309 INFO     29 [qwen-vl-table] page=3 LLM output (len=213):
{
  "report_date": "2025-01-08",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1c",
      "value": "8.6%",
      "unit": "%",
      "reference_range": "4-6%",
      "abnormal": true
    }
  ]
}
2026-08-10 13:20:05,310 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:20:05,314 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1025743, prompt_len=513
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
2026-08-10 13:20:06,735 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [355, 100, 390, 255]}
]
```
2026-08-10 13:20:06,735 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.4s
2026-08-10 13:20:06,735 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[355, 100, 390, 255]
2026-08-10 13:20:06,736 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=1.4s
2026-08-10 13:20:06,736 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 211.225, 232.04999999999998, 84.2, 214.70999999999998]]
2026-08-10 13:20:06,736 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.8s
2026-08-10 13:20:06,736 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:20:06,737 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:20:06,737 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[4]
2026-08-10 13:20:06,737 INFO     29 [qwen-vl-table] positions ： [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:20:06,893 INFO     29 [qwen-vl-table] page=4, rect=595x842, img=(1653x2339)
2026-08-10 13:20:06,893 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:06,894 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 90, \"bbox_end\": 109, \"encounter_dates\": [\"2025-05-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2025-05-07\n\\hline\n\\multicolumn{9}{c}{\\textbf{顺中西医结合医院}} \\\\\n\\hline\n姓名: & & & & & & & & \\\\\n性别: 女 & 年龄: 67 & & & & & & & \\\\\n送检科: & 室: 门诊 & & & & & & & \\\\\n标本状态: 正常 & 标本类型: 静脉全血 & & & & & & & \\\\\n送检日期: 2025-05-07 & & & & & & & & \\\\\n\\hline\n项目名称 & & & & 结果 & & & & \\\\\n\\hline\n糖化血红蛋白 (HbA1c) & & & & 11.2\\% & & & & \\\\\n\\hline\n& & & & & 参考范围 & & & \\\\\n\\hline\n& & & & & 4-6\\% & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:20:08,050 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:08,050 INFO     29 [qwen-vl-table] page=4 LLM output (len=214):
{
  "report_date": "2025-05-07",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1c",
      "value": "11.2%",
      "unit": "%",
      "reference_range": "4-6%",
      "abnormal": true
    }
  ]
}
2026-08-10 13:20:08,050 INFO     29 [qwen-vl-table] coord grouping: {4: 1}
2026-08-10 13:20:08,053 INFO     29 [qwen-vl-table] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=974147, prompt_len=513
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
2026-08-10 13:20:09,547 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [355, 110, 390, 372]}
]
```
2026-08-10 13:20:09,547 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 13:20:09,547 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[355, 110, 390, 372]
2026-08-10 13:20:09,548 INFO     29 [qwen-vl-table] page=4 coord: matched 1/1, time=1.5s
2026-08-10 13:20:09,548 INFO     29 [qwen-vl-table] new_positions (1):
[[5, 211.225, 232.04999999999998, 92.61999999999999, 313.224]]
2026-08-10 13:20:09,548 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.8s
2026-08-10 13:20:09,557 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:20:09,558 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:LabExam | outputs={"chunks": "2 items, types={'LabReport': 2}", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:20:09,558 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:20:09,563 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:09,563 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:20:09,989 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:10,000 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:20:10,000 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:20:10,000 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:20:10,010 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:20:10,011 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:20:10,011 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:20:10,011 INFO     29 [qwen-vl-text] positions(26): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:20:10,011 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [26]
2026-08-10 13:20:10,166 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:20:10,167 INFO     29 [qwen-vl-text] LLM extraction start, text_len=401
2026-08-10 13:20:10,167 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:10,167 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 25, \"encounter_dates\": [\"2025-01-08\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "中西医结合医院\n病人门（急）诊病历\n病人ID M024474 姓名\n性别：女 出生时间： 1958年8月27日\n籍贯：河南郑州市 民族：汉族 婚否：已婚 职业：无\n身份\n电话号码\n17\n工作单位： 常住地址：郑州市金水区花园路39号3号院\n门诊号： 74164 接诊时间： 2025年1月8日9时38分\n就诊时间：2025-1-8 09:41:09 体温：36.3℃\n主诉：尿里边带泡沫，去大药店门口测血糖买二甲双胍片。\n现病史：口干，喝水多，尿里带泡沫，来我院检查治疗。\n体格检查：\n西医诊断：1.糖尿病 中医诊断：\n建议： 1、糖尿病饮食；保持心情愉悦；\n2、适量运动；\n3、规律服药；\n4、定期监测血糖；\n5、不适随诊。\n过敏史：无\n家族史：无\n既往史：无\n处理：给予二甲双胍片口服，空腹血糖、糖化血红蛋白检测，以了解血糖控制情况\n备注：\n打印时间：2025-1-8 科室：内科门诊 医生：张建鹏",
    "role": "user"
  }
]
2026-08-10 13:20:12,541 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:12,541 INFO     29 [qwen-vl-text] LLM output (len=482):
{
  "encounter_date": "2025-01-08",
  "chief_complaint": "尿里边带泡沫，去大药店门口测血糖买二甲双胍片。",
  "present_illness": "口干，喝水多，尿里带泡沫，来我院检查治疗。",
  "past_history": "无",
  "diagnosis": "西医：1.糖尿病 中医：",
  "treatment_plan": {
    "lifestyle_advice": [
      "糖尿病饮食",
      "保持心情愉悦",
      "适量运动",
      "规律服药",
      "定期监测血糖",
      "不适随诊"
    ],
    "medications": [
      {
        "name": "二甲双胍片",
        "route": "口服"
      }
    ],
    "examinations": [
      "空腹血糖",
      "糖化血红蛋白检测"
    ]
  }
}
2026-08-10 13:20:12,541 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-08]
2026-08-10 13:20:12,545 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=723555, prompt_len=1092
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["中西医结合医院", "病人门（急）诊病历", "病人ID M024474 姓名", "性别：女 出生时间： 1958年8月27日", "籍贯：河南郑州市 民族：汉族 婚否：已婚 职业：无", "身份", "电话号码", "17", "工作单位： 常住地址：郑州市金水区花园路39号3号院", "门诊号： 74164 接诊时间： 2025年1月8日9时38分", "就诊时间：2025-1-8 09:41:09 体温：36.3℃", "主诉：尿里边带泡沫，去大药店门口测血糖买二甲双胍片。", "现病史：口干，喝水多，尿里带泡沫，来我院检查治疗。", "体格检查：", "西医诊断：1.糖尿病 中医诊断：", "建议： 1、糖尿病饮食；保持心情愉悦；", "2、适量运动；", "3、规律服药；", "4、定期监测血糖；", "5、不适随诊。", "过敏史：无", "家族史：无", "既往史：无", "处理：给予二甲双胍片口服，空腹血糖、糖化血红蛋白检测，以了解血糖控制情况", "备注：", "打印时间：2025-1-8 科室：内科门诊 医生：张建鹏"]

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
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord API raw response (len=1529):
[
	{"text": "中西医结合医院", "bbox": [454, 28, 706, 57]},
	{"text": "病人门（急）诊病历", "bbox": [291, 74, 708, 108]},
	{"text": "病人ID M024474 姓名", "bbox": [86, 123, 313, 140]},
	{"text": "性别：女 出生时间： 1958年8月27日", "bbox": [454, 123, 847, 140]},
	{"text": "籍贯：河南郑州市 民族：汉族 婚否：已婚 职业：无", "bbox": [86, 151, 686, 169]},
	{"text": "身份", "bbox": [86, 181, 128, 198]},
	{"text": "电话号码", "bbox": [479, 181, 555, 198]},
	{"text": "17", "bbox": [691, 183, 713, 197]},
	{"text": "工作单位： 常住地址：郑州市金水区花园路39号3号院", "bbox": [86, 205, 815, 223]},
	{"text": "门诊号： 74164 接诊时间： 2025年1月8日9时38分", "bbox": [86, 232, 708, 250]},
	{"text": "就诊时间：2025-1-8 09:41:09 体温：36.3℃", "bbox": [86, 259, 672, 277]},
	{"text": "主诉：尿里边带泡沫，去大药店门口测血糖买二甲双胍片。", "bbox": [86, 292, 673, 310]},
	{"text": "现病史：口干，喝水多，尿里带泡沫，来我院检查治疗。", "bbox": [86, 352, 652, 370]},
	{"text": "体格检查：", "bbox": [86, 398, 185, 416]},
	{"text": "西医诊断：1.糖尿病 中医诊断：", "bbox": [86, 444, 509, 462]},
	{"text": "建议： 1、糖尿病饮食；保持心情愉悦；", "bbox": [86, 480, 497, 498]},
	{"text": "2、适量运动；", "bbox": [176, 498, 312, 515]},
	{"text": "3、规律服药；", "bbox": [176, 515, 312, 533]},
	{"text": "4、定期监测血糖；", "bbox": [176, 533, 359, 551]},
	{"text": "5、不适随诊。", "bbox": [176, 551, 316, 569]},
	{"text": "过敏史：无", "bbox": [86, 608, 202, 626]},
	{"text": "家族史：无", "bbox": [86, 644, 202, 662]},
	{"text": "既往史：无", "bbox": [86, 690, 202, 708]},
	{"text": "处理：给予二甲双胍片口服，空腹血糖、糖化血红蛋白检测，以了解血糖控制情况", "bbox": [96, 743, 914, 761]},
	{"text": "备注：", "bbox": [96, 783, 150, 801]},
	{"text": "打印时间：2025-1-8 科室：内科门诊 医生：张建鹏", "bbox": [114, 825, 727, 843]}
]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=10.1s
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[0]: text=中西医结合医院, bbox=[454, 28, 706, 57]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[1]: text=病人门（急）诊病历, bbox=[291, 74, 708, 108]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID M024474 姓名, bbox=[86, 123, 313, 140]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 出生时间： 1958年8月27日, bbox=[454, 123, 847, 140]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[4]: text=籍贯：河南郑州市 民族：汉族 婚否：已婚 职业：无, bbox=[86, 151, 686, 169]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[5]: text=身份, bbox=[86, 181, 128, 198]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[6]: text=电话号码, bbox=[479, 181, 555, 198]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[7]: text=17, bbox=[691, 183, 713, 197]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[8]: text=工作单位： 常住地址：郑州市金水区花园路39号3号院, bbox=[86, 205, 815, 223]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[9]: text=门诊号： 74164 接诊时间： 2025年1月8日9时38分, bbox=[86, 232, 708, 250]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[10]: text=就诊时间：2025-1-8 09:41:09 体温：36.3℃, bbox=[86, 259, 672, 277]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[11]: text=主诉：尿里边带泡沫，去大药店门口测血糖买二甲双胍片。, bbox=[86, 292, 673, 310]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[12]: text=现病史：口干，喝水多，尿里带泡沫，来我院检查治疗。, bbox=[86, 352, 652, 370]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查：, bbox=[86, 398, 185, 416]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[14]: text=西医诊断：1.糖尿病 中医诊断：, bbox=[86, 444, 509, 462]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[15]: text=建议： 1、糖尿病饮食；保持心情愉悦；, bbox=[86, 480, 497, 498]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[16]: text=2、适量运动；, bbox=[176, 498, 312, 515]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[17]: text=3、规律服药；, bbox=[176, 515, 312, 533]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[18]: text=4、定期监测血糖；, bbox=[176, 533, 359, 551]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[19]: text=5、不适随诊。, bbox=[176, 551, 316, 569]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[20]: text=过敏史：无, bbox=[86, 608, 202, 626]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[21]: text=家族史：无, bbox=[86, 644, 202, 662]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[22]: text=既往史：无, bbox=[86, 690, 202, 708]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[23]: text=处理：给予二甲双胍片口服，空腹血糖、糖化血红蛋白检测，以了解血糖控制情况, bbox=[96, 743, 914, 761]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[24]: text=备注：, bbox=[96, 783, 150, 801]
2026-08-10 13:20:22,664 INFO     29 [qwen-vl-text] coord item[25]: text=打印时间：2025-1-8 科室：内科门诊 医生：张建鹏, bbox=[114, 825, 727, 843]
2026-08-10 13:20:22,665 INFO     29 [qwen-vl-text] page=0 — 26/26 coords, api_time=10.1s
2026-08-10 13:20:22,665 INFO     29 [qwen-vl-text] new_positions (26):
[[0, 270.13, 420.07, 23.576, 47.994], [0, 173.14499999999998, 421.26, 62.308, 90.93599999999999], [0, 51.169999999999995, 186.23499999999999, 103.566, 117.88], [0, 270.13, 503.965, 103.566, 117.88], [0, 51.169999999999995, 408.16999999999996, 127.142, 142.298], [0, 51.169999999999995, 76.16, 152.402, 166.716], [0, 285.005, 330.22499999999997, 152.402, 166.716], [0, 411.145, 424.23499999999996, 154.08599999999998, 165.874], [0, 51.169999999999995, 484.92499999999995, 172.60999999999999, 187.766], [0, 51.169999999999995, 421.26, 195.344, 210.5], [0, 51.169999999999995, 399.84, 218.078, 233.23399999999998], [0, 51.169999999999995, 400.435, 245.864, 261.02], [0, 51.169999999999995, 387.94, 296.384, 311.53999999999996], [0, 51.169999999999995, 110.07499999999999, 335.116, 350.272], [0, 51.169999999999995, 302.85499999999996, 373.848, 389.00399999999996], [0, 51.169999999999995, 295.715, 404.15999999999997, 419.316], [0, 104.72, 185.64, 419.316, 433.63], [0, 104.72, 185.64, 433.63, 448.786], [0, 104.72, 213.605, 448.786, 463.942], [0, 104.72, 188.01999999999998, 463.942, 479.09799999999996], [0, 51.169999999999995, 120.19, 511.936, 527.092], [0, 51.169999999999995, 120.19, 542.2479999999999, 557.404], [0, 51.169999999999995, 120.19, 580.98, 596.136], [0, 57.12, 543.8299999999999, 625.606, 640.762], [0, 57.12, 89.25, 659.286, 674.442], [0, 67.83, 432.565, 694.65, 709.8059999999999]]
2026-08-10 13:20:22,665 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=12.7s
2026-08-10 13:20:22,671 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:20:22,672 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:20:22,672 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:20:22,676 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:20:22,677 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:20:22,677 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:20:22,677 INFO     29 [qwen-vl-text] positions(14): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:20:22,677 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [14]
2026-08-10 13:20:22,836 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:20:22,837 INFO     29 [qwen-vl-text] LLM extraction start, text_len=85
2026-08-10 13:20:22,837 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:22,837 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 110, \"bbox_end\": 123, \"encounter_dates\": [\"2025-01-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "百顺中西医结合医院\n527836\n自费\n西药费\n50.00\n大额记账：\n大病补充：\n原账户余额：\n现金支付：\n伍拾元整\n50.00\n27836\n0061\n2025-01-",
    "role": "user"
  }
]
2026-08-10 13:20:24,201 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:24,201 INFO     29 [qwen-vl-text] LLM output (len=138):
{
  "encounter_date": "2025-01-08",
  "pharmacy": "百顺中西医结合医院",
  "medications": [],
  "payment_total": 50.00,
  "payment_method": "现金支付"
}
2026-08-10 13:20:24,201 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-08]
2026-08-10 13:20:24,203 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=889029, prompt_len=740
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["百顺中西医结合医院", "527836", "自费", "西药费", "50.00", "大额记账：", "大病补充：", "原账户余额：", "现金支付：", "伍拾元整", "50.00", "27836", "0061", "2025-01-"]

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
2026-08-10 13:20:28,826 INFO     29 [qwen-vl-text] coord API raw response (len=716):
```json
[
	{"text": "百顺中西医结合医院", "bbox": [244, 214, 580, 245]},
	{"text": "527836", "bbox": [275, 252, 392, 275]},
	{"text": "自费", "bbox": [506, 317, 570, 343]},
	{"text": "西药费", "bbox": [191, 437, 300, 464]},
	{"text": "50.00", "bbox": [612, 443, 702, 466]},
	{"text": "大额记账：", "bbox": [137, 683, 300, 711]},
	{"text": "大病补充：", "bbox": [133, 725, 298, 753]},
	{"text": "原账户余额：", "bbox": [493, 645, 684, 673]},
	{"text": "现金支付：", "bbox": [525, 726, 684, 755]},
	{"text": "伍拾元整", "bbox": [319, 769, 472, 798]},
	{"text": "50.00", "bbox": [761, 773, 855, 797]},
	{"text": "27836", "bbox": [116, 921, 234, 945]},
	{"text": "0061", "bbox": [526, 921, 609, 945]},
	{"text": "2025-01-", "bbox": [730, 921, 882, 945]}
]
```
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=4.6s
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[0]: text=百顺中西医结合医院, bbox=[244, 214, 580, 245]
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[1]: text=527836, bbox=[275, 252, 392, 275]
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[2]: text=自费, bbox=[506, 317, 570, 343]
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[3]: text=西药费, bbox=[191, 437, 300, 464]
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[4]: text=50.00, bbox=[612, 443, 702, 466]
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[5]: text=大额记账：, bbox=[137, 683, 300, 711]
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[6]: text=大病补充：, bbox=[133, 725, 298, 753]
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[7]: text=原账户余额：, bbox=[493, 645, 684, 673]
2026-08-10 13:20:28,827 INFO     29 [qwen-vl-text] coord item[8]: text=现金支付：, bbox=[525, 726, 684, 755]
2026-08-10 13:20:28,828 INFO     29 [qwen-vl-text] coord item[9]: text=伍拾元整, bbox=[319, 769, 472, 798]
2026-08-10 13:20:28,828 INFO     29 [qwen-vl-text] coord item[10]: text=50.00, bbox=[761, 773, 855, 797]
2026-08-10 13:20:28,828 INFO     29 [qwen-vl-text] coord item[11]: text=27836, bbox=[116, 921, 234, 945]
2026-08-10 13:20:28,828 INFO     29 [qwen-vl-text] coord item[12]: text=0061, bbox=[526, 921, 609, 945]
2026-08-10 13:20:28,828 INFO     29 [qwen-vl-text] coord item[13]: text=2025-01-, bbox=[730, 921, 882, 945]
2026-08-10 13:20:28,828 INFO     29 [qwen-vl-text] page=5 — 14/14 coords, api_time=4.6s
2026-08-10 13:20:28,828 INFO     29 [qwen-vl-text] new_positions (14):
[[5, 145.18, 345.09999999999997, 180.188, 206.29], [5, 163.625, 233.23999999999998, 212.184, 231.54999999999998], [5, 301.07, 339.15, 266.914, 288.806], [5, 113.645, 178.5, 367.954, 390.688], [5, 364.14, 417.69, 373.006, 392.372], [5, 81.515, 178.5, 575.086, 598.662], [5, 79.13499999999999, 177.31, 610.4499999999999, 634.026], [5, 293.335, 406.97999999999996, 543.09, 566.6659999999999], [5, 312.375, 406.97999999999996, 611.292, 635.7099999999999], [5, 189.80499999999998, 280.84, 647.4979999999999, 671.9159999999999], [5, 452.79499999999996, 508.72499999999997, 650.866, 671.074], [5, 69.02, 139.23, 775.482, 795.6899999999999], [5, 312.96999999999997, 362.35499999999996, 775.482, 795.6899999999999], [5, 434.34999999999997, 524.79, 775.482, 795.6899999999999]]
2026-08-10 13:20:28,828 INFO     29 [qwen-vl-text] ═══ DONE ═══ 14 positions, pages=1, time=6.2s
2026-08-10 13:20:28,828 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:20:28,839 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:20:28,839 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:20:28,839 INFO     29 [qwen-vl-text] positions(13): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:20:28,839 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [13]
2026-08-10 13:20:29,041 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:20:29,042 INFO     29 [qwen-vl-text] LLM extraction start, text_len=84
2026-08-10 13:20:29,042 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:29,042 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 124, \"bbox_end\": 136, \"encounter_dates\": [\"2025-05-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "20250507530576\n新密佰顺中西医结合医院\n530576\n女\n自费\n西药费\n50.00\n大额记账：\n大病补充：\n原帐户余额：\n现金支付：\n伍拾元整\n50.00",
    "role": "user"
  }
]
2026-08-10 13:20:29,045 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:20:29.044+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 45, "failed": 0, "current": {"1e2e962294be11f1bd9827cf206dfa2d": {"id": "1e2e962294be11f1bd9827cf206dfa2d", "doc_id": "1dee142694be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "type": "pdf", "location": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "size": 1153670, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367969629, "task_type": "dataflow", "root_trace_id": "c156a740bf4445608a67c6fa5390ecc5", "root_traceparent": "00-c156a740bf4445608a67c6fa5390ecc5-80117852a55b854d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:20:29,887 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:29,887 INFO     29 [qwen-vl-text] LLM output (len=138):
{
  "encounter_date": "2025-05-07",
  "pharmacy": "新密佰顺中西医结合医院",
  "medications": [],
  "payment_total": 50.00,
  "payment_method": "自费"
}
2026-08-10 13:20:29,888 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-07]
2026-08-10 13:20:29,891 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1174595, prompt_len=736
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共13行）
["20250507530576", "新密佰顺中西医结合医院", "530576", "女", "自费", "西药费", "50.00", "大额记账：", "大病补充：", "原帐户余额：", "现金支付：", "伍拾元整", "50.00"]

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
2026-08-10 13:20:34,365 INFO     29 [qwen-vl-text] coord API raw response (len=659):
[
	{"text": "20250507530576", "bbox": [166, 265, 477, 293]},
	{"text": "新密佰顺中西医结合医院", "bbox": [171, 310, 591, 338]},
	{"text": "530576", "bbox": [283, 352, 391, 373]},
	{"text": "女", "bbox": [441, 387, 471, 409]},
	{"text": "自费", "bbox": [543, 388, 594, 408]},
	{"text": "西药费", "bbox": [207, 467, 308, 490]},
	{"text": "50.00", "bbox": [715, 468, 804, 489]},
	{"text": "大额记账：", "bbox": [126, 744, 280, 770]},
	{"text": "大病补充：", "bbox": [125, 780, 280, 808]},
	{"text": "原帐户余额：", "bbox": [523, 706, 710, 732]},
	{"text": "现金支付：", "bbox": [559, 780, 712, 809]},
	{"text": "伍拾元整", "bbox": [283, 835, 443, 865]},
	{"text": "50.00", "bbox": [764, 833, 867, 860]}
]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord API: raw_items=13, valid_items=13, elapsed=4.5s
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[0]: text=20250507530576, bbox=[166, 265, 477, 293]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[1]: text=新密佰顺中西医结合医院, bbox=[171, 310, 591, 338]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[2]: text=530576, bbox=[283, 352, 391, 373]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[3]: text=女, bbox=[441, 387, 471, 409]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[4]: text=自费, bbox=[543, 388, 594, 408]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[5]: text=西药费, bbox=[207, 467, 308, 490]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[6]: text=50.00, bbox=[715, 468, 804, 489]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[7]: text=大额记账：, bbox=[126, 744, 280, 770]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[8]: text=大病补充：, bbox=[125, 780, 280, 808]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[9]: text=原帐户余额：, bbox=[523, 706, 710, 732]
2026-08-10 13:20:34,366 INFO     29 [qwen-vl-text] coord item[10]: text=现金支付：, bbox=[559, 780, 712, 809]
2026-08-10 13:20:34,367 INFO     29 [qwen-vl-text] coord item[11]: text=伍拾元整, bbox=[283, 835, 443, 865]
2026-08-10 13:20:34,367 INFO     29 [qwen-vl-text] coord item[12]: text=50.00, bbox=[764, 833, 867, 860]
2026-08-10 13:20:34,367 INFO     29 [qwen-vl-text] page=6 — 13/13 coords, api_time=4.5s
2026-08-10 13:20:34,367 INFO     29 [qwen-vl-text] new_positions (13):
[[6, 98.77, 283.815, 223.13, 246.706], [6, 101.74499999999999, 351.645, 261.02, 284.596], [6, 168.385, 232.64499999999998, 296.384, 314.066], [6, 262.395, 280.245, 325.854, 344.378], [6, 323.085, 353.43, 326.69599999999997, 343.536], [6, 123.16499999999999, 183.26, 393.214, 412.58], [6, 425.42499999999995, 478.38, 394.056, 411.738], [6, 74.97, 166.6, 626.448, 648.34], [6, 74.375, 166.6, 656.76, 680.336], [6, 311.185, 422.45, 594.452, 616.3439999999999], [6, 332.60499999999996, 423.64, 656.76, 681.178], [6, 168.385, 263.585, 703.0699999999999, 728.3299999999999], [6, 454.58, 515.865, 701.386, 724.12]]
2026-08-10 13:20:34,367 INFO     29 [qwen-vl-text] ═══ DONE ═══ 13 positions, pages=1, time=5.5s
2026-08-10 13:20:34,381 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:20:34,381 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:20:34,381 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:20:34,389 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:20:34,389 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:20:34,389 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 13:20:34,390 INFO     29 [qwen-vl-text] positions(26): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:20:34,390 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [26]
2026-08-10 13:20:34,540 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:20:34,540 INFO     29 [qwen-vl-text] LLM extraction start, text_len=225
2026-08-10 13:20:34,540 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:34,541 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 26, \"bbox_end\": 51, \"encounter_dates\": [\"2025-01-08\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "医结合医院处方笺\n普通\n性别：女\n年龄：67岁\n费别：自费\n病人ID：M024474\n处方号：74164\n就诊序号：52849\n体重：/（kg）\n药物过敏史：无\n住址：郑州市金水区花园路39号院\n开方日期：2025-1-8 09:41\n就诊科室：内科门诊\n临床诊断：糖尿病\nRp:\n盐酸二甲双胍片\n0.5g*60 X 5盒\n用法：每次0.5g 一日三次 口服\n备注：\n医师：张建鹏\n审核：\n核对：\n金额合计：50.00元\n调配：\n发药：\n药房：西药费",
    "role": "user"
  }
]
2026-08-10 13:20:36,532 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:36,532 INFO     29 [qwen-vl-text] LLM output (len=409):
{
  "encounter_date": "2025-01-08",
  "prescription_type": "门诊处方",
  "prescriber": "张建鹏",
  "department": "内科门诊",
  "diagnosis": "糖尿病",
  "items": [
    {
      "drug_generic_name": "盐酸二甲双胍片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "一日三次",
      "route": "口服",
      "duration_days": null,
      "quantity": "5盒",
      "notes": null
    }
  ]
}
2026-08-10 13:20:36,532 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-08]
2026-08-10 13:20:36,535 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=744746, prompt_len=916
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["医结合医院处方笺", "普通", "性别：女", "年龄：67岁", "费别：自费", "病人ID：M024474", "处方号：74164", "就诊序号：52849", "体重：/（kg）", "药物过敏史：无", "住址：郑州市金水区花园路39号院", "开方日期：2025-1-8 09:41", "就诊科室：内科门诊", "临床诊断：糖尿病", "Rp:", "盐酸二甲双胍片", "0.5g*60 X 5盒", "用法：每次0.5g 一日三次 口服", "备注：", "医师：张建鹏", "审核：", "核对：", "金额合计：50.00元", "调配：", "发药：", "药房：西药费"]

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
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord API raw response (len=2092):
[
	{"text": "医结合医院处方笺", "bbox": [464, 133, 788, 161]},
	{"text": "普通", "bbox": [810, 103, 852, 120]},
	{"text": "性别：女", "bbox": [350, 190, 442, 207], "bbox": [350, 190, 442, 207]},
	{"text": "年龄：67岁", "bbox": [475, 190, 593, 207], "bbox": [475, 190, 593, 207]},
	{"text": "费别：自费", "bbox": [686, 191, 796, 208], "bbox": [686, 191, 796, 208]},
	{"text": "病人ID：M024474", "bbox": [158, 211, 320, 225], "bbox": [158, 211, 320, 225]},
	{"text": "处方号：74164", "bbox": [380, 209, 514, 224], "bbox": [380, 209, 514, 224]},
	{"text": "就诊序号：52849", "bbox": [544, 210, 707, 225], "bbox": [544, 210, 707, 225]},
	{"text": "体重：/（kg）", "bbox": [726, 211, 844, 228], "bbox": [726, 211, 844, 228]},
	{"text": "药物过敏史：无", "bbox": [158, 230, 315, 247], "bbox": [158, 230, 315, 247]},
	{"text": "住址：郑州市金水区花园路39号院", "bbox": [474, 230, 824, 248], "bbox": [474, 230, 824, 248]},
	{"text": "开方日期：2025-1-8 09:41", "bbox": [158, 255, 432, 272], "bbox": [158, 255, 432, 272]},
	{"text": "就诊科室：内科门诊", "bbox": [502, 254, 704, 271], "bbox": [502, 254, 704, 271]},
	{"text": "临床诊断：糖尿病", "bbox": [156, 287, 337, 304], "bbox": [156, 287, 337, 304]},
	{"text": "Rp:", "bbox": [152, 341, 207, 365], "bbox": [152, 341, 207, 365]},
	{"text": "盐酸二甲双胍片", "bbox": [195, 367, 356, 384], "bbox": [195, 367, 356, 384]},
	{"text": "0.5g*60 X 5盒", "bbox": [540, 367, 689, 384], "bbox": [540, 367, 689, 384]},
	{"text": "用法：每次0.5g 一日三次 口服", "bbox": [233, 398, 561, 416], "bbox": [233, 398, 561, 416]},
	{"text": "备注：", "bbox": [222, 806, 276, 823], "bbox": [222, 806, 276, 823]},
	{"text": "医师：张建鹏", "bbox": [713, 832, 852, 849], "bbox": [713, 832, 852, 849]},
	{"text": "审核：", "bbox": [208, 866, 262, 883], "bbox": [208, 866, 262, 883]},
	{"text": "核对：", "bbox": [431, 866, 486, 883], "bbox": [431, 866, 486, 883]},
	{"text": "金额合计：50.00元", "bbox": [632, 866, 837, 883], "bbox": [632, 866, 837, 883]},
	{"text": "调配：", "bbox": [208, 891, 262, 908], "bbox": [208, 891, 262, 908]},
	{"text": "发药：", "bbox": [431, 891, 486, 908], "bbox": [431, 891, 486, 908]},
	{"text": "药房：西药费", "bbox": [655, 891, 794, 908], "bbox": [655, 891, 794, 908]}
]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=11.6s
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[0]: text=医结合医院处方笺, bbox=[464, 133, 788, 161]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[810, 103, 852, 120]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[350, 190, 442, 207]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：67岁, bbox=[475, 190, 593, 207]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[4]: text=费别：自费, bbox=[686, 191, 796, 208]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[5]: text=病人ID：M024474, bbox=[158, 211, 320, 225]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[6]: text=处方号：74164, bbox=[380, 209, 514, 224]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[7]: text=就诊序号：52849, bbox=[544, 210, 707, 225]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[8]: text=体重：/（kg）, bbox=[726, 211, 844, 228]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[9]: text=药物过敏史：无, bbox=[158, 230, 315, 247]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[10]: text=住址：郑州市金水区花园路39号院, bbox=[474, 230, 824, 248]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[11]: text=开方日期：2025-1-8 09:41, bbox=[158, 255, 432, 272]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[12]: text=就诊科室：内科门诊, bbox=[502, 254, 704, 271]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[13]: text=临床诊断：糖尿病, bbox=[156, 287, 337, 304]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[14]: text=Rp:, bbox=[152, 341, 207, 365]
2026-08-10 13:20:48,129 INFO     29 [qwen-vl-text] coord item[15]: text=盐酸二甲双胍片, bbox=[195, 367, 356, 384]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[16]: text=0.5g*60 X 5盒, bbox=[540, 367, 689, 384]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[17]: text=用法：每次0.5g 一日三次 口服, bbox=[233, 398, 561, 416]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[18]: text=备注：, bbox=[222, 806, 276, 823]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[19]: text=医师：张建鹏, bbox=[713, 832, 852, 849]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[20]: text=审核：, bbox=[208, 866, 262, 883]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[21]: text=核对：, bbox=[431, 866, 486, 883]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[22]: text=金额合计：50.00元, bbox=[632, 866, 837, 883]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[23]: text=调配：, bbox=[208, 891, 262, 908]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[24]: text=发药：, bbox=[431, 891, 486, 908]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] coord item[25]: text=药房：西药费, bbox=[655, 891, 794, 908]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] page=1 — 26/26 coords, api_time=11.6s
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] new_positions (26):
[[1, 276.08, 468.85999999999996, 111.98599999999999, 135.56199999999998], [1, 481.95, 506.94, 86.726, 101.03999999999999], [1, 208.25, 262.99, 159.98, 174.29399999999998], [1, 282.625, 352.835, 159.98, 174.29399999999998], [1, 408.16999999999996, 473.62, 160.822, 175.136], [1, 94.00999999999999, 190.39999999999998, 177.662, 189.45], [1, 226.1, 305.83, 175.97799999999998, 188.608], [1, 323.68, 420.66499999999996, 176.82, 189.45], [1, 431.96999999999997, 502.17999999999995, 177.662, 191.976], [1, 94.00999999999999, 187.42499999999998, 193.66, 207.974], [1, 282.03, 490.28, 193.66, 208.816], [1, 94.00999999999999, 257.03999999999996, 214.70999999999998, 229.024], [1, 298.69, 418.88, 213.868, 228.182], [1, 92.82, 200.515, 241.654, 255.968], [1, 90.44, 123.16499999999999, 287.122, 307.33], [1, 116.02499999999999, 211.82, 309.014, 323.328], [1, 321.3, 409.955, 309.014, 323.328], [1, 138.635, 333.79499999999996, 335.116, 350.272], [1, 132.09, 164.22, 678.6519999999999, 692.966], [1, 424.23499999999996, 506.94, 700.544, 714.858], [1, 123.75999999999999, 155.89, 729.172, 743.486], [1, 256.445, 289.16999999999996, 729.172, 743.486], [1, 376.03999999999996, 498.015, 729.172, 743.486], [1, 123.75999999999999, 155.89, 750.222, 764.536], [1, 256.445, 289.16999999999996, 750.222, 764.536], [1, 389.72499999999997, 472.43, 750.222, 764.536]]
2026-08-10 13:20:48,130 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=13.7s
2026-08-10 13:20:48,130 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:20:48,131 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:20:48,131 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 13:20:48,131 INFO     29 [qwen-vl-text] positions(28): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:20:48,131 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [28]
2026-08-10 13:20:48,266 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:20:48,266 INFO     29 [qwen-vl-text] LLM extraction start, text_len=216
2026-08-10 13:20:48,267 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:48,267 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 52, \"bbox_end\": 79, \"encounter_dates\": [\"2025-05-07\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "页中西医结合医院处方笺\n普通\n姓名\n性别：女\n年龄：66岁\n费别：自费\n病人ID：M024474\n处方号：74165\n就诊序号：74164\n体重：/（kg）\n药物过敏史：无\n住址：\n开方日期：2025-05-07 09:39\n就诊科室：内科门诊\n临床诊断：糖尿病\nRp：\n盐酸二甲双胍片\n0.5g\nX 5盒\n用法：每次0.5g TID 口服\n备注：\n医师：张建鹏\n审核：\n核对：\n金额合计：50.00元\n调配：\n发药：\n药房：西药房",
    "role": "user"
  }
]
2026-08-10 13:20:51,758 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:51,758 INFO     29 [qwen-vl-text] LLM output (len=408):
{
  "encounter_date": "2025-05-07",
  "prescription_type": "门诊处方",
  "prescriber": "张建鹏",
  "department": "内科门诊",
  "diagnosis": "糖尿病",
  "items": [
    {
      "drug_generic_name": "盐酸二甲双胍片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "TID",
      "route": "口服",
      "duration_days": null,
      "quantity": "5盒",
      "notes": null
    }
  ]
}
2026-08-10 13:20:51,758 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-07]
2026-08-10 13:20:51,761 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=633179, prompt_len=913
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["页中西医结合医院处方笺", "普通", "姓名", "性别：女", "年龄：66岁", "费别：自费", "病人ID：M024474", "处方号：74165", "就诊序号：74164", "体重：/（kg）", "药物过敏史：无", "住址：", "开方日期：2025-05-07 09:39", "就诊科室：内科门诊", "临床诊断：糖尿病", "Rp：", "盐酸二甲双胍片", "0.5g", "X 5盒", "用法：每次0.5g TID 口服", "备注：", "医师：张建鹏", "审核：", "核对：", "金额合计：50.00元", "调配：", "发药：", "药房：西药房"]

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
2026-08-10 13:20:59,748 INFO     29 [qwen-vl-text] coord API raw response (len=1448):
[
	{"text": "页中西医结合医院处方笺", "bbox": [338, 96, 736, 129]},
	{"text": "普通", "bbox": [753, 72, 795, 89]},
	{"text": "姓名", "bbox": [138, 157, 182, 173]},
	{"text": "性别：女", "bbox": [343, 150, 420, 168]},
	{"text": "年龄：66岁", "bbox": [462, 152, 558, 169]},
	{"text": "费别：自费", "bbox": [654, 154, 743, 171]},
	{"text": "病人ID：M024474", "bbox": [137, 177, 294, 194]},
	{"text": "处方号：74165", "bbox": [361, 174, 485, 192]},
	{"text": "就诊序号：74164", "bbox": [508, 177, 655, 194]},
	{"text": "体重：/（kg）", "bbox": [687, 176, 813, 194]},
	{"text": "药物过敏史：无", "bbox": [137, 200, 283, 217]},
	{"text": "住址：", "bbox": [463, 200, 512, 216]},
	{"text": "开方日期：2025-05-07 09:39", "bbox": [137, 223, 417, 240]},
	{"text": "就诊科室：内科门诊", "bbox": [463, 222, 655, 239]},
	{"text": "临床诊断：糖尿病", "bbox": [138, 255, 316, 272]},
	{"text": "Rp：", "bbox": [138, 307, 194, 334]},
	{"text": "盐酸二甲双胍片", "bbox": [177, 335, 330, 352]},
	{"text": "0.5g", "bbox": [524, 334, 570, 350]},
	{"text": "X 5盒", "bbox": [633, 332, 689, 348]},
	{"text": "用法：每次0.5g TID 口服", "bbox": [221, 365, 494, 381]},
	{"text": "备注：", "bbox": [203, 790, 260, 808]},
	{"text": "医师：张建鹏", "bbox": [641, 814, 772, 832]},
	{"text": "审核：", "bbox": [188, 854, 243, 872]},
	{"text": "核对：", "bbox": [416, 853, 472, 871]},
	{"text": "金额合计：50.00元", "bbox": [617, 852, 813, 870]},
	{"text": "调配：", "bbox": [188, 883, 243, 900]},
	{"text": "发药：", "bbox": [416, 881, 472, 899]},
	{"text": "药房：西药房", "bbox": [665, 880, 797, 897]}
]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=8.0s
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[0]: text=页中西医结合医院处方笺, bbox=[338, 96, 736, 129]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[753, 72, 795, 89]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[138, 157, 182, 173]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[343, 150, 420, 168]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：66岁, bbox=[462, 152, 558, 169]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[5]: text=费别：自费, bbox=[654, 154, 743, 171]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[6]: text=病人ID：M024474, bbox=[137, 177, 294, 194]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[7]: text=处方号：74165, bbox=[361, 174, 485, 192]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[8]: text=就诊序号：74164, bbox=[508, 177, 655, 194]
2026-08-10 13:20:59,749 INFO     29 [qwen-vl-text] coord item[9]: text=体重：/（kg）, bbox=[687, 176, 813, 194]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[10]: text=药物过敏史：无, bbox=[137, 200, 283, 217]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[11]: text=住址：, bbox=[463, 200, 512, 216]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[12]: text=开方日期：2025-05-07 09:39, bbox=[137, 223, 417, 240]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[13]: text=就诊科室：内科门诊, bbox=[463, 222, 655, 239]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[14]: text=临床诊断：糖尿病, bbox=[138, 255, 316, 272]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[15]: text=Rp：, bbox=[138, 307, 194, 334]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[16]: text=盐酸二甲双胍片, bbox=[177, 335, 330, 352]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[17]: text=0.5g, bbox=[524, 334, 570, 350]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[18]: text=X 5盒, bbox=[633, 332, 689, 348]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[19]: text=用法：每次0.5g TID 口服, bbox=[221, 365, 494, 381]
2026-08-10 13:20:59,750 INFO     29 [qwen-vl-text] coord item[20]: text=备注：, bbox=[203, 790, 260, 808]
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] coord item[21]: text=医师：张建鹏, bbox=[641, 814, 772, 832]
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] coord item[22]: text=审核：, bbox=[188, 854, 243, 872]
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] coord item[23]: text=核对：, bbox=[416, 853, 472, 871]
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] coord item[24]: text=金额合计：50.00元, bbox=[617, 852, 813, 870]
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] coord item[25]: text=调配：, bbox=[188, 883, 243, 900]
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] coord item[26]: text=发药：, bbox=[416, 881, 472, 899]
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] coord item[27]: text=药房：西药房, bbox=[665, 880, 797, 897]
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] page=2 — 28/28 coords, api_time=8.0s
2026-08-10 13:20:59,751 INFO     29 [qwen-vl-text] new_positions (28):
[[2, 201.10999999999999, 437.91999999999996, 80.832, 108.618], [2, 448.03499999999997, 473.025, 60.623999999999995, 74.938], [2, 82.11, 108.28999999999999, 132.194, 145.666], [2, 204.08499999999998, 249.89999999999998, 126.3, 141.456], [2, 274.89, 332.01, 127.984, 142.298], [2, 389.13, 442.085, 129.668, 143.982], [2, 81.515, 174.92999999999998, 149.034, 163.34799999999998], [2, 214.795, 288.575, 146.50799999999998, 161.664], [2, 302.26, 389.72499999999997, 149.034, 163.34799999999998], [2, 408.765, 483.73499999999996, 148.192, 163.34799999999998], [2, 81.515, 168.385, 168.4, 182.714], [2, 275.485, 304.64, 168.4, 181.87199999999999], [2, 81.515, 248.11499999999998, 187.766, 202.07999999999998], [2, 275.485, 389.72499999999997, 186.924, 201.238], [2, 82.11, 188.01999999999998, 214.70999999999998, 229.024], [2, 82.11, 115.42999999999999, 258.49399999999997, 281.228], [2, 105.315, 196.35, 282.07, 296.384], [2, 311.78, 339.15, 281.228, 294.7], [2, 376.635, 409.955, 279.544, 293.01599999999996], [2, 131.495, 293.93, 307.33, 320.80199999999996], [2, 120.785, 154.7, 665.18, 680.336], [2, 381.395, 459.34, 685.3879999999999, 700.544], [2, 111.86, 144.58499999999998, 719.068, 734.2239999999999], [2, 247.51999999999998, 280.84, 718.226, 733.382], [2, 367.115, 483.73499999999996, 717.384, 732.54], [2, 111.86, 144.58499999999998, 743.486, 757.8], [2, 247.51999999999998, 280.84, 741.802, 756.958], [2, 395.67499999999995, 474.215, 740.9599999999999, 755.274]]
2026-08-10 13:20:59,752 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=11.6s
2026-08-10 13:20:59,766 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:20:59,766 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:Prescription | outputs={"chunks": "2 items, types={'PrescriptionRecord': 2}", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:20:59,766 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:20:59,770 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:20:59,771 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:21:00,548 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:21:00.548+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 45, "failed": 0, "current": {"1e2e962294be11f1bd9827cf206dfa2d": {"id": "1e2e962294be11f1bd9827cf206dfa2d", "doc_id": "1dee142694be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "type": "pdf", "location": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "size": 1153670, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367969629, "task_type": "dataflow", "root_trace_id": "c156a740bf4445608a67c6fa5390ecc5", "root_traceparent": "00-c156a740bf4445608a67c6fa5390ecc5-80117852a55b854d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:21:01,007 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:01,018 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:21:01,019 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:21:01,019 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:21:01,027 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:01,027 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:21:01,508 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:01,514 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:21:01,514 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:21:01,514 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:21:01,519 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:01,519 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:21:02,630 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:02,636 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:21:02,636 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:21:02,636 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:21:02,641 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:02,641 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:21:03,126 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:03,137 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:21:03,137 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "137 items", "markdown": "", "text": "", "name": "Bxli糖尿病 郑州中心.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Prescription": "2 items, types={'PrescriptionRecord': 2}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Prescription\": 2, \"chunks_LabExam\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:21:03,137 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:21:03,138 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 2, 'Extractor:Prescription': 2, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 13:21:03,150 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:21:03,150 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 2, 'OutpatientRecord': 1, 'MedicationRecord': 2, 'PrescriptionRecord': 2}", "name": "Bxli糖尿病 郑州中心.pdf"}
2026-08-10 13:21:03,150 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:21:03,189 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786367971021, 'update_date': datetime.datetime(2026, 8, 10, 13, 19, 31), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1034560, 'status': '1'}
2026-08-10 13:21:03,395 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白  HbA1c  8.6%  %  4-6%  True   
---
   糖化血红蛋白  HbA1c  11.2%  %  4-6%  True   
---
中西医结合医院
病人门（急）诊病历
病人ID M024474 姓名
性别：女 出生时间： 1958年8月27日
籍贯：河南郑州市 民族：汉族 婚否：已婚 职业：无
身份
电话号码
17
工作单位： 常住地址：郑州市金水区花园路39号3号院
门诊号： 74164 接诊时间： 2025年1月8日9时38分
就诊时间：2025-1-8 09:41:09 体温：36.3℃
主诉：尿里边带泡沫，去大药店门口测血糖买二甲双胍片。
现病史：口干，喝水多，尿里带泡沫，来我院检查治疗。
体格检查：
西医诊断：1.糖尿病 中医诊断：
建议： 1、糖尿病饮食；保持心情愉悦；
2、适量运动；
3、规律服药；
4、定期监测血糖；
5、不适随诊。
过敏史：无
家族史：无
既往史：无
处理：给予二甲双胍片口服，空腹血糖、糖化血红蛋白检测，以了解血糖控制情况
备注：
打印时间：2025-1-8 科室：内科门诊 医生：张建鹏
---
百顺中西医结合医院
527836
自费
西药费
50.00
大额记账：
大病补充：
原账户余额：
现金支付：
伍拾元整
50.00
27836
0061
2025-01-
---
20250507530576
新密佰顺中西医结合医院
530576
女
自费
西药费
50.00
大额记账：
大病补充：
原帐户余额：
现金支付：
伍拾元整
50.00
---
医结合医院处方笺
普通
性别：女
年龄：67岁
费别：自费
病人ID：M024474
处方号：74164
就诊序号：52849
体重：/（kg）
药物过敏史：无
住址：郑州市金水区花园路39号院
开方日期：2025-1-8 09:41
就诊科室：内科门诊
临床诊断：糖尿病
Rp:
盐酸二甲双胍片
0.5g*60 X 5盒
用法：每次0.5g 一日三次 口服
备注：
医师：张建鹏
审核：
核对：
金额合计：50.00元
调配：
发药：
药房：西药费
---
页中西医结合医院处方笺
普通
姓名
性别：女
年龄：66岁
费别：自费
病人ID：M024474
处方号：74165
就诊序号：74164
体重：/（kg）
药物过敏史：无
住址：
开方日期：2025-05-07 09:39
就诊科室：内科门诊
临床诊断：糖尿病
Rp：
盐酸二甲双胍片
0.5g
X 5盒
用法：每次0.5g TID 口服
备注：
医师：张建鹏
审核：
核对：
金额合计：50.00元
调配：
发药：
药房：西药房
2026-08-10 13:21:03,718 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:21:03,718 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 2, 'OutpatientRecord': 1, 'MedicationRecord': 2, 'PrescriptionRecord': 2}", "name": "Bxli糖尿病 郑州中心.pdf", "embedding_token_consumption": 900}
2026-08-10 13:21:03,718 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:21:03,948 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:21:03,948 INFO     29 [Trace] task=1e2e9622 | doc=Bxli糖尿病 郑州中心.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":7,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:21:03,951 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 211, 232, 84, 214) row[-1]=(4, 211, 232, 84, 214)
2026-08-10 13:21:03,951 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(5, 211, 232, 92, 313) row[-1]=(5, 211, 232, 92, 313)
2026-08-10 13:21:03,952 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:21:03,952 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:21:03,952 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:21:03,952 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:21:03,952 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:21:03,955 INFO     29 set_progress(1e2e962294be11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:21:03 [DOC Engine]:
Start to index...
2026-08-10 13:21:03,977 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 13:21:03,981 INFO     29 set_progress(1e2e962294be11f1bd9827cf206dfa2d), progress: 0.8142857142857143, progress_msg: 
2026-08-10 13:21:03,995 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-10 13:21:04,003 INFO     29 set_progress(1e2e962294be11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:21:03 Indexing done (0.05s). Task done (88.70s)
2026-08-10 13:21:04,008 INFO     29 [Done], chunks(7), token(900), elapsed:88.70
2026-08-10 13:21:04,090 INFO     29 handle_task done for task {"id": "1e2e962294be11f1bd9827cf206dfa2d", "doc_id": "1dee142694be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "type": "pdf", "location": "Bxli\u7cd6\u5c3f\u75c5 \u90d1\u5dde\u4e2d\u5fc3.pdf", "size": 1153670, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786367969629, "task_type": "dataflow", "root_trace_id": "c156a740bf4445608a67c6fa5390ecc5", "root_traceparent": "00-c156a740bf4445608a67c6fa5390ecc5-80117852a55b854d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
