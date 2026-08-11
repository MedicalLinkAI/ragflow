# 基准结果：cji糖尿病.pdf

## 基本信息

- 文件：`cji糖尿病.pdf`
- 大小：702.6 KB
- PDF 总页数：5
- doc_id：`583d832894be11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:21:06  完成时间：2026-08-10T21:22:33  耗时：87.4s
- progress_msg：`13:22:30 Indexing done (0.04s). Task done (76.63s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 027e7141 | 1 | 1-1 | 河南省医疗门诊收费票据 河南省 票据代码：豫财410212 票据批次：0A[20 |
| 2 | 054b2c27 | 1 | 2-2 | 顺中西医结合医院处方笺 普通 姓名 性别：女 年龄：51岁 费别：自费 病人ID |
| 3 | 7134079d | 1 | 5-5 | 西医结合医院 病人门（急）诊病历 病人ID M0242896 姓名: 性别: 女 |
| 4 | 38bc8b55 | 1 | 3-3 | <table><tr><td>糖化血红蛋白测定</td><td>HbA1c</t |
| 5 | a9e6352a | 1 | 4-4 | <table><tr><td>糖化血红蛋白测定</td><td>HbA1c</t |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：5
- 页码并集：`[1, 2, 3, 4, 5]`
- 覆盖页数：5 / 5；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 1 | 1 | 1 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 1 | 1 | 1 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 2 | 0 | 2 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"MedicationRecord": 1, "PrescriptionRecord": 1, "LabReport": 2, "OutpatientRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 5, "sources": 9, "stats": {"Extractor:LabExam": 2, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:22:29,750 INFO     29 [ChunkMerger] Merged 5 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:21:09,309 INFO     29 handle_task begin for task {"id": "586b758094be11f1bd9827cf206dfa2d", "doc_id": "583d832894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "cji\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "cji\u7cd6\u5c3f\u75c5.pdf", "size": 719494, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368067335, "task_type": "dataflow", "root_trace_id": "d24053a1fe4d4cb6b28cd59a97da1a4b", "root_traceparent": "00-d24053a1fe4d4cb6b28cd59a97da1a4b-43fea21cae272936-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:21:09,536 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:21:09,650 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:21:09,658 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:21:09,658 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:21:09,658 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:21:09,663 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:21:09,663 INFO     29 ============================================================
2026-08-10 13:21:09,663 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:21:09,663 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:21:09,663 INFO     29 ============================================================
2026-08-10 13:21:09,663 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:21:09,663 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:21:09,664 INFO     29 No torch found.
2026-08-10 13:21:10,372 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-10 13:21:10,706 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1579492, prompt_len=764
2026-08-10 13:21:12,141 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:21:12,141 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:21:12,147 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1579492, prompt_len=401
2026-08-10 13:21:14,720 INFO     29 [qwen-vl-parser] text API response (len=463):
["河南省医疗门诊收费票据", "河南省", "票据代码：豫财410212", "票据批次：0A[2018]", "20241218527246", "新密佰顺中西医结合医院", "527245", "业务流水号：", "社会保障号码：", "姓名", "性别", "医保类型", "医疗机构类型", "项目", "数量", "金额", "自费", "付金额", "西药费", "80.00", "大额记账：", "大病补充：", "新密佰顺中西医结合", "5241018333000778", "发票专用章", "现金支付：", "合计(大写)：", "捌拾元整", "医保统筹支付：", "个人账户支付：", "其他医保支付：", "个人支付金额：", "收款单位(章)：", "收款人(签章)：", "527246", "0061", "80.00", "盖", "章", "有", "效", "遗", "失", "不", "补", "CS", "扫描全能王", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 13:21:14,721 INFO     29 [qwen-vl-parser] page=1 text: 49 lines (bbox 0-48)
2026-08-10 13:21:14,721 INFO     29 [qwen-vl-parser] page=1 text: 49 sections
2026-08-10 13:21:14,914 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1104917, prompt_len=764
2026-08-10 13:21:16,290 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:21:16,291 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:21:16,303 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1104917, prompt_len=401
2026-08-10 13:21:18,424 INFO     29 [qwen-vl-parser] text API response (len=350):
["顺中西医结合医院处方笺", "普通", "姓名", "性别：女", "年龄：51岁", "费别：自费", "病人ID：M045218", "处方号：67456", "就诊序号：69523", "体重：/（kg）", "药物过敏史：无", "住址：新密市", "开方日期：2024-12-18 10:37", "就诊科室：内科门诊", "临床诊断：2型糖尿病", "Rp:", "盐酸二甲双胍片", "0.5g*60 X 8盒", "用法：每次0.5g 一日三次 口服", "备注：", "医师：吴爱香", "审核：", "核对：", "金额合计：80.00元", "调配：", "发药：", "药房：西药费", "CS", "扫描全能王", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 13:21:18,425 INFO     29 [qwen-vl-parser] page=2 text: 31 lines (bbox 49-79)
2026-08-10 13:21:18,425 INFO     29 [qwen-vl-parser] page=2 text: 31 sections
2026-08-10 13:21:18,604 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1093560, prompt_len=764
2026-08-10 13:21:20,000 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-21"
}
```
2026-08-10 13:21:20,001 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2025-04-21
2026-08-10 13:21:20,014 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1093560, prompt_len=756
2026-08-10 13:21:23,922 INFO     29 [qwen-vl-parser] table API response (len=437):
\begin{tabular}{|c|c|c|c|c|c|c|c|}
\hline
\multicolumn{8}{|c|}{\textbf{新密佰顺中西医结合医院}} \\
\hline
姓名: & & 性别: 女 & 年龄: 51 & 送检科 & 室: 门诊 & 标本状态: 正常 & 标本类型: 静脉全血 \\
\hline
\multicolumn{8}{|c|}{送检日期: 2025-4-21} \\
\hline
项目名称 & & & & & & 结果 & 参考范围 \\
\hline
糖化血红蛋白测定 (HbA1c)) & & & & & & 8.1\% & 4-6\% \\
\hline
\multicolumn{8}{|c|}{送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2025-4-21} \\
\hline
\multicolumn{8}{|c|}{此结果仅对该标本负责} \\
\hline
\end{tabular}
2026-08-10 13:21:23,923 INFO     29 [qwen-vl-parser] page=3 table: 18 LaTeX lines (bbox 80-97)
2026-08-10 13:21:23,923 INFO     29 [qwen-vl-parser] page=3 table: 18 sections
2026-08-10 13:21:24,096 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1059019, prompt_len=764
2026-08-10 13:21:25,472 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-12-18"
}
```
2026-08-10 13:21:25,472 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2024-12-18
2026-08-10 13:21:25,488 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1059019, prompt_len=756
2026-08-10 13:21:29,138 INFO     29 [qwen-vl-parser] table API response (len=770):
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
\multicolumn{9}{|c|}{\textbf{新密佰顺中西医结合医院}} \\
\hline
\multicolumn{2}{|c|}{姓名:} & \multicolumn{2}{c|}{性别: 女} & \multicolumn{2}{c|}{年龄: 51} & \multicolumn{3}{c|}{送检科 室: 门诊} \\
\hline
\multicolumn{4}{|c|}{标本状态: 正常} & \multicolumn{5}{c|}{标本类型: 静脉全血} \\
\hline
\multicolumn{4}{|c|}{送检日期: 2024-12-18} & \multicolumn{5}{c|}{参考范围} \\
\hline
\multicolumn{4}{|c|}{} & \multicolumn{5}{c|}{4-6\%} \\
\hline
\multicolumn{4}{|c|}{项目名称} & \multicolumn{5}{c|}{结果} \\
\hline
\multicolumn{4}{|c|}{} & \multicolumn{5}{c|}{9.8\%} \\
\hline
\multicolumn{4}{|c|}{糖化血红蛋白测定 (HbA1c)} & \multicolumn{5}{c|}{} \\
\hline
\multicolumn{9}{|c|}{送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2024-12-18} \\
\hline
\multicolumn{9}{|c|}{此结果仅对该标本负责} \\
\hline
\end{tabular}
2026-08-10 13:21:29,139 INFO     29 [qwen-vl-parser] page=4 table: 24 LaTeX lines (bbox 98-121)
2026-08-10 13:21:29,139 INFO     29 [qwen-vl-parser] page=4 table: 24 sections
2026-08-10 13:21:29,340 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1290275, prompt_len=764
2026-08-10 13:21:30,774 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:21:30,775 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 13:21:30,792 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1290275, prompt_len=401
2026-08-10 13:21:31,979 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:21:31.978+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 46, "failed": 0, "current": {"586b758094be11f1bd9827cf206dfa2d": {"id": "586b758094be11f1bd9827cf206dfa2d", "doc_id": "583d832894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "cji\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "cji\u7cd6\u5c3f\u75c5.pdf", "size": 719494, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368067335, "task_type": "dataflow", "root_trace_id": "d24053a1fe4d4cb6b28cd59a97da1a4b", "root_traceparent": "00-d24053a1fe4d4cb6b28cd59a97da1a4b-43fea21cae272936-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:21:33,658 INFO     29 [qwen-vl-parser] text API response (len=468):
["西医结合医院", "病人门（急）诊病历", "病人ID M0242896 姓名:", "性别: 女 出生时间: 1974年12月28日", "籍贯: 河南省新密市城关镇 民族: 汉族 婚否: 已婚 职业: 无", "身份证号:", "电话号码:", "工作单位:", "常住地址: 新密市东大街百货大楼", "门诊号: 7253 接诊时间: 2024年12月18日 10时17分", "就诊时间: 2024-12-18 10:17:16 体温: 36.3℃", "主诉: 糖尿病2年", "现病史: 2年前感觉浑身乏力,来院检查发现血糖高。", "体格检查:", "西医诊断: 1.糖尿病 中医诊断:", "建议: 1、糖尿病饮食;保持心情愉悦;", "2、适量运动;", "3、规律服药;", "4、定期监测血糖;", "5、不适随诊。", "过敏史: 无", "族史: 有", "往史: 无", "理: 给予糖化血红蛋白检测,以了解血糖控制情况", "注:", "印时间: 2025.4.21 科室: 内科门诊 医生", ""]
2026-08-10 13:21:33,658 INFO     29 [qwen-vl-parser] page=5 text: 26 lines (bbox 122-147)
2026-08-10 13:21:33,658 INFO     29 [qwen-vl-parser] page=5 text: 26 sections
2026-08-10 13:21:33,658 INFO     29 [qwen-vl-parser] parse_pdf done: 148 sections from 5 pages.
2026-08-10 13:21:33,667 INFO     29 Close text detector.
2026-08-10 13:21:34,121 INFO     29 Close text recognizer.
2026-08-10 13:21:34,521 INFO     29 Close recognizer.
2026-08-10 13:21:34,901 INFO     29 Close recognizer.
2026-08-10 13:21:35,326 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:21:35,326 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Parser:MedLink | outputs={"html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "json"}
2026-08-10 13:21:35,326 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:21:35,345 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:35,345 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 河南省医疗门诊收费票据\n[BBOX-1] 河南省\n[BBOX-2] 票据代码：豫财410212\n[BBOX-3] 票据批次：0A[2018]\n[BBOX-4] 20241218527246\n[BBOX-5] 新密佰顺中西医结合医院\n[BBOX-6] 527245\n[BBOX-7] 业务流水号：\n[BBOX-8] 社会保障号码：\n[BBOX-9] 姓名\n[BBOX-10] 性别\n[BBOX-11] 医保类型\n[BBOX-12] 医疗机构类型\n[BBOX-13] 项目\n[BBOX-14] 数量\n[BBOX-15] 金额\n[BBOX-16] 自费\n[BBOX-17] 付金额\n[BBOX-18] 西药费\n[BBOX-19] 80.00\n[BBOX-20] 大额记账：\n[BBOX-21] 大病补充：\n[BBOX-22] 新密佰顺中西医结合\n[BBOX-23] 5241018333000778\n[BBOX-24] 发票专用章\n[BBOX-25] 现金支付：\n[BBOX-26] 合计(大写)：\n[BBOX-27] 捌拾元整\n[BBOX-28] 医保统筹支付：\n[BBOX-29] 个人账户支付：\n[BBOX-30] 其他医保支付：\n[BBOX-31] 个人支付金额：\n[BBOX-32] 收款单位(章)：\n[BBOX-33] 收款人(签章)：\n[BBOX-34] 527246\n[BBOX-35] 0061\n[BBOX-36] 80.00\n[BBOX-37] 盖\n[BBOX-38] 章\n[BBOX-39] 有\n[BBOX-40] 效\n[BBOX-41] 遗\n[BBOX-42] 失\n[BBOX-43] 不\n[BBOX-44] 补\n[BBOX-45] CS\n[BBOX-46] 扫描全能王\n[BBOX-47] CS 扫描全能王\n[BBOX-48] 3亿人都在用的扫描App\n[BBOX-49] 顺中西医结合医院处方笺\n[BBOX-50] 普通\n[BBOX-51] 姓名\n[BBOX-52] 性别：女\n[BBOX-53] 年龄：51岁\n[BBOX-54] 费别：自费\n[BBOX-55] 病人ID：M045218\n[BBOX-56] 处方号：67456\n[BBOX-57] 就诊序号：69523\n[BBOX-58] 体重：/（kg）\n[BBOX-59] 药物过敏史：无\n[BBOX-60] 住址：新密市\n[BBOX-61] 开方日期：2024-12-18 10:37\n[BBOX-62] 就诊科室：内科门诊\n[BBOX-63] 临床诊断：2型糖尿病\n[BBOX-64] Rp:\n[BBOX-65] 盐酸二甲双胍片\n[BBOX-66] 0.5g*60 X 8盒\n[BBOX-67] 用法：每次0.5g 一日三次 口服\n[BBOX-68] 备注：\n[BBOX-69] 医师：吴爱香\n[BBOX-70] 审核：\n[BBOX-71] 核对：\n[BBOX-72] 金额合计：80.00元\n[BBOX-73] 调配：\n[BBOX-74] 发药：\n[BBOX-75] 药房：西药费\n[BBOX-76] CS\n[BBOX-77] 扫描全能王\n[BBOX-78] CS 扫描全能王\n[BBOX-79] 3亿人都在用的扫描App\n[BBOX-80] \\begin{tabular}{|c|c|c|c|c|c|c|c|}\n[BBOX-81] 报告时间: 2025-04-21\n[BBOX-82] \\hline\n[BBOX-83] \\multicolumn{8}{|c|}{\\textbf{新密佰顺中西医结合医院}} \\\\\n[BBOX-84] \\hline\n[BBOX-85] 姓名: & & 性别: 女 & 年龄: 51 & 送检科 & 室: 门诊 & 标本状态: 正常 & 标本类型: 静脉全血 \\\\\n[BBOX-86] \\hline\n[BBOX-87] \\multicolumn{8}{|c|}{送检日期: 2025-4-21} \\\\\n[BBOX-88] \\hline\n[BBOX-89] 项目名称 & & & & & & 结果 & 参考范围 \\\\\n[BBOX-90] \\hline\n[BBOX-91] 糖化血红蛋白测定 (HbA1c)) & & & & & & 8.1\\% & 4-6\\% \\\\\n[BBOX-92] \\hline\n[BBOX-93] \\multicolumn{8}{|c|}{送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2025-4-21} \\\\\n[BBOX-94] \\hline\n[BBOX-95] \\multicolumn{8}{|c|}{此结果仅对该标本负责} \\\\\n[BBOX-96] \\hline\n[BBOX-97] \\end{tabular}\n[BBOX-98] \\begin{tabular}{|c|c|c|c|c|c|c|c|c|}\n[BBOX-99] 报告时间: 2024-12-18\n[BBOX-100] \\hline\n[BBOX-101] \\multicolumn{9}{|c|}{\\textbf{新密佰顺中西医结合医院}} \\\\\n[BBOX-102] \\hline\n[BBOX-103] \\multicolumn{2}{|c|}{姓名:} & \\multicolumn{2}{c|}{性别: 女} & \\multicolumn{2}{c|}{年龄: 51} & \\multicolumn{3}{c|}{送检科 室: 门诊} \\\\\n[BBOX-104] \\hline\n[BBOX-105] \\multicolumn{4}{|c|}{标本状态: 正常} & \\multicolumn{5}{c|}{标本类型: 静脉全血} \\\\\n[BBOX-106] \\hline\n[BBOX-107] \\multicolumn{4}{|c|}{送检日期: 2024-12-18} & \\multicolumn{5}{c|}{参考范围} \\\\\n[BBOX-108] \\hline\n[BBOX-109] \\multicolumn{4}{|c|}{} & \\multicolumn{5}{c|}{4-6\\%} \\\\\n[BBOX-110] \\hline\n[BBOX-111] \\multicolumn{4}{|c|}{项目名称} & \\multicolumn{5}{c|}{结果} \\\\\n[BBOX-112] \\hline\n[BBOX-113] \\multicolumn{4}{|c|}{} & \\multicolumn{5}{c|}{9.8\\%} \\\\\n[BBOX-114] \\hline\n[BBOX-115] \\multicolumn{4}{|c|}{糖化血红蛋白测定 (HbA1c)} & \\multicolumn{5}{c|}{} \\\\\n[BBOX-116] \\hline\n[BBOX-117] \\multicolumn{9}{|c|}{送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2024-12-18} \\\\\n[BBOX-118] \\hline\n[BBOX-119] \\multicolumn{9}{|c|}{此结果仅对该标本负责} \\\\\n[BBOX-120] \\hline\n[BBOX-121] \\end{tabular}\n[BBOX-122] 西医结合医院\n[BBOX-123] 病人门（急）诊病历\n[BBOX-124] 病人ID M0242896 姓名:\n[BBOX-125] 性别: 女 出生时间: 1974年12月28日\n[BBOX-126] 籍贯: 河南省新密市城关镇 民族: 汉族 婚否: 已婚 职业: 无\n[BBOX-127] 身份证号:\n[BBOX-128] 电话号码:\n[BBOX-129] 工作单位:\n[BBOX-130] 常住地址: 新密市东大街百货大楼\n[BBOX-131] 门诊号: 7253 接诊时间: 2024年12月18日 10时17分\n[BBOX-132] 就诊时间: 2024-12-18 10:17:16 体温: 36.3℃\n[BBOX-133] 主诉: 糖尿病2年\n[BBOX-134] 现病史: 2年前感觉浑身乏力,来院检查发现血糖高。\n[BBOX-135] 体格检查:\n[BBOX-136] 西医诊断: 1.糖尿病 中医诊断:\n[BBOX-137] 建议: 1、糖尿病饮食;保持心情愉悦;\n[BBOX-138] 2、适量运动;\n[BBOX-139] 3、规律服药;\n[BBOX-140] 4、定期监测血糖;\n[BBOX-141] 5、不适随诊。\n[BBOX-142] 过敏史: 无\n[BBOX-143] 族史: 有\n[BBOX-144] 往史: 无\n[BBOX-145] 理: 给予糖化血红蛋白检测,以了解血糖控制情况\n[BBOX-146] 注:\n[BBOX-147] 印时间: 2025.4.21 科室: 内科门诊 医生"
  }
]
2026-08-10 13:21:40,276 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:40,289 INFO     29 [SmartSplitter] SmartSplitter done: 5 chunks from 5 LLM segments (all bbox_id). Types: {'MedicationRecord': 1, 'PrescriptionRecord': 1, 'LabReport': 2, 'OutpatientRecord': 1}
2026-08-10 13:21:40,296 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:21:40,297 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks": "5 items, types={'MedicationRecord': 1, 'PrescriptionRecord': 1, 'LabReport': 2, 'OutpatientRecord': 1}"}
2026-08-10 13:21:40,297 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:21:40,297 INFO     29 [ChunkRouter] Routed 5 chunks into 4 groups: {'chunks_Medication': 1, 'chunks_Prescription': 1, 'chunks_LabExam': 2, 'chunks_Clinical': 1}
2026-08-10 13:21:40,305 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:21:40,305 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | ChunkRouter:Router | outputs={"html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks": "5 items, types={'MedicationRecord': 1, 'PrescriptionRecord': 1, 'LabReport': 2, 'OutpatientRecord': 1}", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:21:40,305 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:21:40,309 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:21:40,310 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:21:40,310 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[2]
2026-08-10 13:21:40,310 INFO     29 [qwen-vl-table] positions ： [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:21:40,458 INFO     29 [qwen-vl-table] page=2, rect=595x842, img=(1653x2339)
2026-08-10 13:21:40,459 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:40,459 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 80, \"bbox_end\": 97, \"encounter_dates\": [\"2025-04-21\"], \"department\": \"门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|c|c|c|c|c|c|c|c|}\n报告时间: 2025-04-21\n\\hline\n\\multicolumn{8}{|c|}{\\textbf{新密佰顺中西医结合医院}} \\\\\n\\hline\n姓名: & & 性别: 女 & 年龄: 51 & 送检科 & 室: 门诊 & 标本状态: 正常 & 标本类型: 静脉全血 \\\\\n\\hline\n\\multicolumn{8}{|c|}{送检日期: 2025-4-21} \\\\\n\\hline\n项目名称 & & & & & & 结果 & 参考范围 \\\\\n\\hline\n糖化血红蛋白测定 (HbA1c)) & & & & & & 8.1\\% & 4-6\\% \\\\\n\\hline\n\\multicolumn{8}{|c|}{送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2025-4-21} \\\\\n\\hline\n\\multicolumn{8}{|c|}{此结果仅对该标本负责} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:21:41,768 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:41,768 INFO     29 [qwen-vl-table] page=2 LLM output (len=215):
{
  "report_date": "2025-04-21",
  "items": [
    {
      "name": "糖化血红蛋白测定",
      "item_code": "HbA1c",
      "value": "8.1%",
      "unit": "%",
      "reference_range": "4-6%",
      "abnormal": true
    }
  ]
}
2026-08-10 13:21:41,768 INFO     29 [qwen-vl-table] coord grouping: {2: 1}
2026-08-10 13:21:41,773 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1716023, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白测定

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
2026-08-10 13:21:43,369 INFO     29 [qwen-vl-table] coord API raw response (len=67):
```json
[
	{"text": "糖化血红蛋白测定", "bbox": [608, 530, 647, 834]}
]
```
2026-08-10 13:21:43,369 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-10 13:21:43,369 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白测定, bbox=[608, 530, 647, 834]
2026-08-10 13:21:43,371 INFO     29 [qwen-vl-table] page=2 coord: matched 1/1, time=1.6s
2026-08-10 13:21:43,371 INFO     29 [qwen-vl-table] new_positions (1):
[[3, 361.76, 384.965, 446.26, 702.228]]
2026-08-10 13:21:43,371 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=3.1s
2026-08-10 13:21:43,372 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:21:43,374 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:21:43,374 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:21:43,374 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:21:43,531 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 13:21:43,532 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:43,532 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 98, \"bbox_end\": 121, \"encounter_dates\": [\"2024-12-18\"], \"department\": \"门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|c|c|c|c|c|c|c|c|c|}\n报告时间: 2024-12-18\n\\hline\n\\multicolumn{9}{|c|}{\\textbf{新密佰顺中西医结合医院}} \\\\\n\\hline\n\\multicolumn{2}{|c|}{姓名:} & \\multicolumn{2}{c|}{性别: 女} & \\multicolumn{2}{c|}{年龄: 51} & \\multicolumn{3}{c|}{送检科 室: 门诊} \\\\\n\\hline\n\\multicolumn{4}{|c|}{标本状态: 正常} & \\multicolumn{5}{c|}{标本类型: 静脉全血} \\\\\n\\hline\n\\multicolumn{4}{|c|}{送检日期: 2024-12-18} & \\multicolumn{5}{c|}{参考范围} \\\\\n\\hline\n\\multicolumn{4}{|c|}{} & \\multicolumn{5}{c|}{4-6\\%} \\\\\n\\hline\n\\multicolumn{4}{|c|}{项目名称} & \\multicolumn{5}{c|}{结果} \\\\\n\\hline\n\\multicolumn{4}{|c|}{} & \\multicolumn{5}{c|}{9.8\\%} \\\\\n\\hline\n\\multicolumn{4}{|c|}{糖化血红蛋白测定 (HbA1c)} & \\multicolumn{5}{c|}{} \\\\\n\\hline\n\\multicolumn{9}{|c|}{送检医师: 马中杰 检验师: 裴巧玲 审核者: 裴巧玲 报告时间: 2024-12-18} \\\\\n\\hline\n\\multicolumn{9}{|c|}{此结果仅对该标本负责} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:21:44,852 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:44,852 INFO     29 [qwen-vl-table] page=3 LLM output (len=215):
{
  "report_date": "2024-12-18",
  "items": [
    {
      "name": "糖化血红蛋白测定",
      "item_code": "HbA1c",
      "value": "9.8%",
      "unit": "%",
      "reference_range": "4-6%",
      "abnormal": true
    }
  ]
}
2026-08-10 13:21:44,852 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:21:44,855 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1635999, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白测定

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
2026-08-10 13:21:46,445 INFO     29 [qwen-vl-table] coord API raw response (len=67):
```json
[
	{"text": "糖化血红蛋白测定", "bbox": [565, 538, 608, 870]}
]
```
2026-08-10 13:21:46,445 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-10 13:21:46,445 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白测定, bbox=[565, 538, 608, 870]
2026-08-10 13:21:46,446 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=1.6s
2026-08-10 13:21:46,446 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 336.175, 361.76, 452.996, 732.54]]
2026-08-10 13:21:46,446 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=3.1s
2026-08-10 13:21:46,453 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:21:46,453 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:LabExam | outputs={"chunks": "2 items, types={'LabReport': 2}", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:21:46,453 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:21:46,458 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:46,458 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:21:46,871 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:46,879 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:21:46,879 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:21:46,879 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:21:46,885 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:21:46,886 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:21:46,886 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:21:46,886 INFO     29 [qwen-vl-text] positions(26): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:21:46,886 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [26]
2026-08-10 13:21:47,097 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:21:47,098 INFO     29 [qwen-vl-text] LLM extraction start, text_len=385
2026-08-10 13:21:47,098 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:47,100 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 122, \"bbox_end\": 147, \"encounter_dates\": [\"2024-12-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "西医结合医院\n病人门（急）诊病历\n病人ID M0242896 姓名:\n性别: 女 出生时间: 1974年12月28日\n籍贯: 河南省新密市城关镇 民族: 汉族 婚否: 已婚 职业: 无\n身份证号:\n电话号码:\n工作单位:\n常住地址: 新密市东大街百货大楼\n门诊号: 7253 接诊时间: 2024年12月18日 10时17分\n就诊时间: 2024-12-18 10:17:16 体温: 36.3℃\n主诉: 糖尿病2年\n现病史: 2年前感觉浑身乏力,来院检查发现血糖高。\n体格检查:\n西医诊断: 1.糖尿病 中医诊断:\n建议: 1、糖尿病饮食;保持心情愉悦;\n2、适量运动;\n3、规律服药;\n4、定期监测血糖;\n5、不适随诊。\n过敏史: 无\n族史: 有\n往史: 无\n理: 给予糖化血红蛋白检测,以了解血糖控制情况\n注:\n印时间: 2025.4.21 科室: 内科门诊 医生",
    "role": "user"
  }
]
2026-08-10 13:21:48,792 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:48,792 INFO     29 [qwen-vl-text] LLM output (len=258):
{
  "encounter_date": "2024-12-18",
  "chief_complaint": "糖尿病2年",
  "present_illness": "2年前感觉浑身乏力,来院检查发现血糖高。",
  "past_history": "无",
  "diagnosis": "西医诊断: 1.糖尿病",
  "treatment_plan": "1、糖尿病饮食;保持心情愉悦; 2、适量运动; 3、规律服药; 4、定期监测血糖; 5、不适随诊。 给予糖化血红蛋白检测,以了解血糖控制情况"
}
2026-08-10 13:21:48,792 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-18]
2026-08-10 13:21:48,797 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1641356, prompt_len=1076
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["西医结合医院", "病人门（急）诊病历", "病人ID M0242896 姓名:", "性别: 女 出生时间: 1974年12月28日", "籍贯: 河南省新密市城关镇 民族: 汉族 婚否: 已婚 职业: 无", "身份证号:", "电话号码:", "工作单位:", "常住地址: 新密市东大街百货大楼", "门诊号: 7253 接诊时间: 2024年12月18日 10时17分", "就诊时间: 2024-12-18 10:17:16 体温: 36.3℃", "主诉: 糖尿病2年", "现病史: 2年前感觉浑身乏力,来院检查发现血糖高。", "体格检查:", "西医诊断: 1.糖尿病 中医诊断:", "建议: 1、糖尿病饮食;保持心情愉悦;", "2、适量运动;", "3、规律服药;", "4、定期监测血糖;", "5、不适随诊。", "过敏史: 无", "族史: 有", "往史: 无", "理: 给予糖化血红蛋白检测,以了解血糖控制情况", "注:", "印时间: 2025.4.21 科室: 内科门诊 医生"]

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
2026-08-10 13:21:58,887 INFO     29 [qwen-vl-text] coord API raw response (len=1529):
[
	{"text": "西医结合医院", "bbox": [500, 29, 716, 58]},
	{"text": "病人门（急）诊病历", "bbox": [322, 78, 715, 113]},
	{"text": "病人ID M0242896 姓名:", "bbox": [135, 128, 373, 145]},
	{"text": "性别: 女 出生时间: 1974年12月28日", "bbox": [468, 128, 865, 146]},
	{"text": "籍贯: 河南省新密市城关镇 民族: 汉族 婚否: 已婚 职业: 无", "bbox": [140, 155, 778, 174]},
	{"text": "身份证号:", "bbox": [144, 183, 228, 200]},
	{"text": "电话号码:", "bbox": [512, 184, 600, 201]},
	{"text": "工作单位:", "bbox": [144, 206, 233, 223]},
	{"text": "常住地址: 新密市东大街百货大楼", "bbox": [530, 207, 833, 225]},
	{"text": "门诊号: 7253 接诊时间: 2024年12月18日 10时17分", "bbox": [144, 247, 753, 266]},
	{"text": "就诊时间: 2024-12-18 10:17:16 体温: 36.3℃", "bbox": [143, 271, 705, 290]},
	{"text": "主诉: 糖尿病2年", "bbox": [141, 300, 315, 317]},
	{"text": "现病史: 2年前感觉浑身乏力,来院检查发现血糖高。", "bbox": [136, 352, 652, 371]},
	{"text": "体格检查:", "bbox": [130, 393, 228, 409]},
	{"text": "西医诊断: 1.糖尿病 中医诊断:", "bbox": [124, 434, 540, 452]},
	{"text": "建议: 1、糖尿病饮食;保持心情愉悦;", "bbox": [117, 467, 530, 485]},
	{"text": "2、适量运动;", "bbox": [208, 484, 350, 501]},
	{"text": "3、规律服药;", "bbox": [207, 500, 349, 517]},
	{"text": "4、定期监测血糖;", "bbox": [204, 517, 394, 534]},
	{"text": "5、不适随诊。", "bbox": [202, 534, 348, 552]},
	{"text": "过敏史: 无", "bbox": [106, 591, 222, 610]},
	{"text": "族史: 有", "bbox": [106, 631, 215, 650]},
	{"text": "往史: 无", "bbox": [106, 682, 211, 702]},
	{"text": "理: 给予糖化血红蛋白检测,以了解血糖控制情况", "bbox": [108, 742, 687, 765]},
	{"text": "注:", "bbox": [106, 795, 138, 816]},
	{"text": "印时间: 2025.4.21 科室: 内科门诊 医生", "bbox": [108, 845, 600, 870]}
]
2026-08-10 13:21:58,888 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=10.1s
2026-08-10 13:21:58,888 INFO     29 [qwen-vl-text] coord item[0]: text=西医结合医院, bbox=[500, 29, 716, 58]
2026-08-10 13:21:58,888 INFO     29 [qwen-vl-text] coord item[1]: text=病人门（急）诊病历, bbox=[322, 78, 715, 113]
2026-08-10 13:21:58,888 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID M0242896 姓名:, bbox=[135, 128, 373, 145]
2026-08-10 13:21:58,888 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 女 出生时间: 1974年12月28日, bbox=[468, 128, 865, 146]
2026-08-10 13:21:58,888 INFO     29 [qwen-vl-text] coord item[4]: text=籍贯: 河南省新密市城关镇 民族: 汉族 婚否: 已婚 职业: 无, bbox=[140, 155, 778, 174]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[5]: text=身份证号:, bbox=[144, 183, 228, 200]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[6]: text=电话号码:, bbox=[512, 184, 600, 201]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[7]: text=工作单位:, bbox=[144, 206, 233, 223]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[8]: text=常住地址: 新密市东大街百货大楼, bbox=[530, 207, 833, 225]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[9]: text=门诊号: 7253 接诊时间: 2024年12月18日 10时17分, bbox=[144, 247, 753, 266]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[10]: text=就诊时间: 2024-12-18 10:17:16 体温: 36.3℃, bbox=[143, 271, 705, 290]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[11]: text=主诉: 糖尿病2年, bbox=[141, 300, 315, 317]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[12]: text=现病史: 2年前感觉浑身乏力,来院检查发现血糖高。, bbox=[136, 352, 652, 371]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查:, bbox=[130, 393, 228, 409]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[14]: text=西医诊断: 1.糖尿病 中医诊断:, bbox=[124, 434, 540, 452]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[15]: text=建议: 1、糖尿病饮食;保持心情愉悦;, bbox=[117, 467, 530, 485]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[16]: text=2、适量运动;, bbox=[208, 484, 350, 501]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[17]: text=3、规律服药;, bbox=[207, 500, 349, 517]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[18]: text=4、定期监测血糖;, bbox=[204, 517, 394, 534]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[19]: text=5、不适随诊。, bbox=[202, 534, 348, 552]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[20]: text=过敏史: 无, bbox=[106, 591, 222, 610]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[21]: text=族史: 有, bbox=[106, 631, 215, 650]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[22]: text=往史: 无, bbox=[106, 682, 211, 702]
2026-08-10 13:21:58,889 INFO     29 [qwen-vl-text] coord item[23]: text=理: 给予糖化血红蛋白检测,以了解血糖控制情况, bbox=[108, 742, 687, 765]
2026-08-10 13:21:58,890 INFO     29 [qwen-vl-text] coord item[24]: text=注:, bbox=[106, 795, 138, 816]
2026-08-10 13:21:58,890 INFO     29 [qwen-vl-text] coord item[25]: text=印时间: 2025.4.21 科室: 内科门诊 医生, bbox=[108, 845, 600, 870]
2026-08-10 13:21:58,891 INFO     29 [qwen-vl-text] page=4 — 26/26 coords, api_time=10.1s
2026-08-10 13:21:58,891 INFO     29 [qwen-vl-text] new_positions (26):
[[4, 297.5, 426.02, 24.418, 48.836], [4, 191.59, 425.42499999999995, 65.676, 95.146], [4, 80.325, 221.935, 107.776, 122.08999999999999], [4, 278.46, 514.675, 107.776, 122.932], [4, 83.3, 462.90999999999997, 130.51, 146.50799999999998], [4, 85.67999999999999, 135.66, 154.08599999999998, 168.4], [4, 304.64, 357.0, 154.928, 169.242], [4, 85.67999999999999, 138.635, 173.452, 187.766], [4, 315.34999999999997, 495.635, 174.29399999999998, 189.45], [4, 85.67999999999999, 448.03499999999997, 207.974, 223.97199999999998], [4, 85.085, 419.47499999999997, 228.182, 244.17999999999998], [4, 83.895, 187.42499999999998, 252.6, 266.914], [4, 80.92, 387.94, 296.384, 312.382], [4, 77.35, 135.66, 330.906, 344.378], [4, 73.78, 321.3, 365.428, 380.584], [4, 69.615, 315.34999999999997, 393.214, 408.37], [4, 123.75999999999999, 208.25, 407.52799999999996, 421.842], [4, 123.16499999999999, 207.655, 421.0, 435.31399999999996], [4, 121.38, 234.42999999999998, 435.31399999999996, 449.628], [4, 120.19, 207.06, 449.628, 464.784], [4, 63.07, 132.09, 497.62199999999996, 513.62], [4, 63.07, 127.925, 531.302, 547.3], [4, 63.07, 125.54499999999999, 574.244, 591.084], [4, 64.25999999999999, 408.765, 624.764, 644.13], [4, 63.07, 82.11, 669.39, 687.072], [4, 64.25999999999999, 357.0, 711.49, 732.54]]
2026-08-10 13:21:58,891 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=12.0s
2026-08-10 13:21:58,903 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:21:58,903 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:21:58,903 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:21:58,909 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:21:58,910 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:21:58,910 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:21:58,910 INFO     29 [qwen-vl-text] positions(45): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:21:58,910 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [45]
2026-08-10 13:21:59,125 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:21:59,126 INFO     29 [qwen-vl-text] LLM extraction start, text_len=284
2026-08-10 13:21:59,127 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:21:59,128 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 0, \"bbox_end\": 44, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "河南省医疗门诊收费票据\n河南省\n票据代码：豫财410212\n票据批次：0A[2018]\n20241218527246\n新密佰顺中西医结合医院\n527245\n业务流水号：\n社会保障号码：\n姓名\n性别\n医保类型\n医疗机构类型\n项目\n数量\n金额\n自费\n付金额\n西药费\n80.00\n大额记账：\n大病补充：\n新密佰顺中西医结合\n5241018333000778\n发票专用章\n现金支付：\n合计(大写)：\n捌拾元整\n医保统筹支付：\n个人账户支付：\n其他医保支付：\n个人支付金额：\n收款单位(章)：\n收款人(签章)：\n527246\n0061\n80.00\n盖\n章\n有\n效\n遗\n失\n不\n补",
    "role": "user"
  }
]
2026-08-10 13:22:00,628 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:00,628 INFO     29 [qwen-vl-text] LLM output (len=132):
{
  "encounter_date": null,
  "pharmacy": "新密佰顺中西医结合医院",
  "medications": [],
  "payment_total": 80.00,
  "payment_method": "现金支付"
}
2026-08-10 13:22:00,637 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3116536, prompt_len=1032
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共45行）
["河南省医疗门诊收费票据", "河南省", "票据代码：豫财410212", "票据批次：0A[2018]", "20241218527246", "新密佰顺中西医结合医院", "527245", "业务流水号：", "社会保障号码：", "姓名", "性别", "医保类型", "医疗机构类型", "项目", "数量", "金额", "自费", "付金额", "西药费", "80.00", "大额记账：", "大病补充：", "新密佰顺中西医结合", "5241018333000778", "发票专用章", "现金支付：", "合计(大写)：", "捌拾元整", "医保统筹支付：", "个人账户支付：", "其他医保支付：", "个人支付金额：", "收款单位(章)：", "收款人(签章)：", "527246", "0061", "80.00", "盖", "章", "有", "效", "遗", "失", "不", "补"]

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
2026-08-10 13:22:14,660 INFO     29 [qwen-vl-text] coord API raw response (len=2970):
[
	{"text": "河南省医疗门诊收费票据", "bbox": [148, 15, 775, 60]},
	{"text": "河南省", "bbox": [400, 54, 508, 76]},
	{"text": "票据代码：豫财410212", "bbox": [595, 65, 911, 90], "label": "票据代码"},
	{"text": "票据批次：0A[2018]", "bbox": [595, 92, 894, 115], "label": "票据批次"},
	{"text": "20241218527246", "bbox": [199, 87, 517, 117], "label": "票据编号"},
	{"text": "新密佰顺中西医结合医院", "bbox": [246, 135, 730, 168], "label": "医院名称"},
	{"text": "527245", "bbox": [248, 194, 376, 217], "label": "业务流水号"},
	{"text": "业务流水号：", "bbox": [16, 207, 164, 230], "label": "业务流水号"},
	{"text": "社会保障号码：", "bbox": [388, 207, 558, 228], "label": "社会保障号码"},
	{"text": "姓名", "bbox": [28, 244, 88, 265], "label": "姓名"},
	{"text": "性别", "bbox": [239, 247, 300, 267], "label": "性别"},
	{"text": "医保类型", "bbox": [388, 245, 505, 266], "label": "医保类型"},
	{"text": "医疗机构类型", "bbox": [604, 242, 775, 263], "label": "医疗机构类型"},
	{"text": "项目", "bbox": [28, 288, 88, 308], "label": "项目"},
	{"text": "数量", "bbox": [379, 288, 438, 308], "label": "数量"},
	{"text": "金额", "bbox": [537, 285, 596, 306], "label": "金额"},
	{"text": "自费", "bbox": [671, 273, 750, 302], "label": "自费"},
	{"text": "付金额", "bbox": [760, 280, 848, 301], "label": "付金额"},
	{"text": "西药费", "bbox": [119, 393, 244, 424], "label": "西药费"},
	{"text": "80.00", "bbox": [565, 389, 662, 412], "label": "金额"},
	{"text": "大额记账：", "bbox": [119, 673, 300, 703], "label": "大额记账"},
	{"text": "大病补充：", "bbox": [119, 717, 300, 747], "label": "大病补充"},
	{"text": "新密佰顺中西医结合", "bbox": [355, 555, 730, 655], "label": "医院名称"},
	{"text": "5241018333000778", "bbox": [415, 632, 770, 707], "label": "发票号码"},
	{"text": "发票专用章", "bbox": [442, 683, 638, 747], "label": "发票专用章"},
	{"text": "现金支付：", "bbox": [595, 717, 770, 756], "label": "现金支付"},
	{"text": "合计(大写)：", "bbox": [52, 756, 208, 784], "label": "合计(大写)"},
	{"text": "捌拾元整", "bbox": [355, 771, 510, 800], "label": "合计(大写)"},
	{"text": "医保统筹支付：", "bbox": [54, 805, 262, 834], "label": "医保统筹支付"},
	{"text": "个人账户支付：", "bbox": [445, 802, 648, 825], "label": "个人账户支付"},
	{"text": "其他医保支付：", "bbox": [58, 843, 262, 868], "label": "其他医保支付"},
	{"text": "个人支付金额：", "bbox": [447, 839, 648, 861], "label": "个人支付金额"},
	{"text": "收款单位(章)：", "bbox": [52, 887, 276, 911], "label": "收款单位(章)"},
	{"text": "收款人(签章)：", "bbox": [364, 882, 598, 905], "label": "收款人(签章)"},
	{"text": "527246", "bbox": [326, 910, 457, 934], "label": "收款人身份证号"},
	{"text": "0061", "bbox": [550, 915, 638, 940], "label": "收款人身份证号"},
	{"text": "80.00", "bbox": [837, 791, 940, 820], "label": "金额"},
	{"text": "盖", "bbox": [927, 382, 950, 403], "label": "盖"},
	{"text": "章", "bbox": [927, 424, 950, 446], "label": "章"},
	{"text": "有", "bbox": [927, 467, 950, 489], "label": "有"},
	{"text": "效", "bbox": [927, 510, 950, 532], "label": "效"},
	{"text": "遗", "bbox": [927, 613, 950, 635], "label": "遗"},
	{"text": "失", "bbox": [927, 657, 950, 679], "label": "失"},
	{"text": "不", "bbox": [927, 700, 950, 722], "label": "不"},
	{"text": "补", "bbox": [927, 742, 950, 764], "label": "补"}
]
2026-08-10 13:22:14,660 INFO     29 [qwen-vl-text] coord API: raw_items=45, valid_items=45, elapsed=14.0s
2026-08-10 13:22:14,660 INFO     29 [qwen-vl-text] coord item[0]: text=河南省医疗门诊收费票据, bbox=[148, 15, 775, 60]
2026-08-10 13:22:14,661 INFO     29 [qwen-vl-text] coord item[1]: text=河南省, bbox=[400, 54, 508, 76]
2026-08-10 13:22:14,661 INFO     29 [qwen-vl-text] coord item[2]: text=票据代码：豫财410212, bbox=[595, 65, 911, 90]
2026-08-10 13:22:14,661 INFO     29 [qwen-vl-text] coord item[3]: text=票据批次：0A[2018], bbox=[595, 92, 894, 115]
2026-08-10 13:22:14,661 INFO     29 [qwen-vl-text] coord item[4]: text=20241218527246, bbox=[199, 87, 517, 117]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[5]: text=新密佰顺中西医结合医院, bbox=[246, 135, 730, 168]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[6]: text=527245, bbox=[248, 194, 376, 217]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[7]: text=业务流水号：, bbox=[16, 207, 164, 230]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[8]: text=社会保障号码：, bbox=[388, 207, 558, 228]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[9]: text=姓名, bbox=[28, 244, 88, 265]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[10]: text=性别, bbox=[239, 247, 300, 267]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[11]: text=医保类型, bbox=[388, 245, 505, 266]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[12]: text=医疗机构类型, bbox=[604, 242, 775, 263]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[13]: text=项目, bbox=[28, 288, 88, 308]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[379, 288, 438, 308]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[15]: text=金额, bbox=[537, 285, 596, 306]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[16]: text=自费, bbox=[671, 273, 750, 302]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[17]: text=付金额, bbox=[760, 280, 848, 301]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[18]: text=西药费, bbox=[119, 393, 244, 424]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[19]: text=80.00, bbox=[565, 389, 662, 412]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[20]: text=大额记账：, bbox=[119, 673, 300, 703]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[21]: text=大病补充：, bbox=[119, 717, 300, 747]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[22]: text=新密佰顺中西医结合, bbox=[355, 555, 730, 655]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[23]: text=5241018333000778, bbox=[415, 632, 770, 707]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[24]: text=发票专用章, bbox=[442, 683, 638, 747]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[25]: text=现金支付：, bbox=[595, 717, 770, 756]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[26]: text=合计(大写)：, bbox=[52, 756, 208, 784]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[27]: text=捌拾元整, bbox=[355, 771, 510, 800]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[28]: text=医保统筹支付：, bbox=[54, 805, 262, 834]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[29]: text=个人账户支付：, bbox=[445, 802, 648, 825]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[30]: text=其他医保支付：, bbox=[58, 843, 262, 868]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[31]: text=个人支付金额：, bbox=[447, 839, 648, 861]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[32]: text=收款单位(章)：, bbox=[52, 887, 276, 911]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[33]: text=收款人(签章)：, bbox=[364, 882, 598, 905]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[34]: text=527246, bbox=[326, 910, 457, 934]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[35]: text=0061, bbox=[550, 915, 638, 940]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[36]: text=80.00, bbox=[837, 791, 940, 820]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[37]: text=盖, bbox=[927, 382, 950, 403]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[38]: text=章, bbox=[927, 424, 950, 446]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[39]: text=有, bbox=[927, 467, 950, 489]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[40]: text=效, bbox=[927, 510, 950, 532]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[41]: text=遗, bbox=[927, 613, 950, 635]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[42]: text=失, bbox=[927, 657, 950, 679]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[43]: text=不, bbox=[927, 700, 950, 722]
2026-08-10 13:22:14,662 INFO     29 [qwen-vl-text] coord item[44]: text=补, bbox=[927, 742, 950, 764]
2026-08-10 13:22:14,663 INFO     29 [qwen-vl-text] page=0 — 45/45 coords, api_time=14.0s
2026-08-10 13:22:14,663 INFO     29 [qwen-vl-text] new_positions (45):
[[0, 88.06, 461.125, 12.629999999999999, 50.519999999999996], [0, 238.0, 302.26, 45.467999999999996, 63.992], [0, 354.025, 542.045, 54.73, 75.78], [0, 354.025, 531.93, 77.464, 96.83], [0, 118.405, 307.615, 73.25399999999999, 98.514], [0, 146.37, 434.34999999999997, 113.67, 141.456], [0, 147.56, 223.72, 163.34799999999998, 182.714], [0, 9.52, 97.58, 174.29399999999998, 193.66], [0, 230.85999999999999, 332.01, 174.29399999999998, 191.976], [0, 16.66, 52.36, 205.44799999999998, 223.13], [0, 142.20499999999998, 178.5, 207.974, 224.814], [0, 230.85999999999999, 300.47499999999997, 206.29, 223.97199999999998], [0, 359.38, 461.125, 203.76399999999998, 221.446], [0, 16.66, 52.36, 242.49599999999998, 259.336], [0, 225.505, 260.61, 242.49599999999998, 259.336], [0, 319.515, 354.62, 239.97, 257.652], [0, 399.245, 446.25, 229.86599999999999, 254.284], [0, 452.2, 504.56, 235.76, 253.44199999999998], [0, 70.80499999999999, 145.18, 330.906, 357.008], [0, 336.175, 393.89, 327.538, 346.904], [0, 70.80499999999999, 178.5, 566.6659999999999, 591.9259999999999], [0, 70.80499999999999, 178.5, 603.7139999999999, 628.9739999999999], [0, 211.225, 434.34999999999997, 467.31, 551.51], [0, 246.92499999999998, 458.15, 532.144, 595.294], [0, 262.99, 379.60999999999996, 575.086, 628.9739999999999], [0, 354.025, 458.15, 603.7139999999999, 636.552], [0, 30.939999999999998, 123.75999999999999, 636.552, 660.1279999999999], [0, 211.225, 303.45, 649.182, 673.6], [0, 32.129999999999995, 155.89, 677.81, 702.228], [0, 264.775, 385.56, 675.284, 694.65], [0, 34.51, 155.89, 709.8059999999999, 730.856], [0, 265.965, 385.56, 706.438, 724.962], [0, 30.939999999999998, 164.22, 746.8539999999999, 767.062], [0, 216.57999999999998, 355.81, 742.644, 762.01], [0, 193.97, 271.91499999999996, 766.22, 786.428], [0, 327.25, 379.60999999999996, 770.43, 791.48], [0, 498.015, 559.3, 666.0219999999999, 690.4399999999999], [0, 551.5649999999999, 565.25, 321.644, 339.32599999999996], [0, 551.5649999999999, 565.25, 357.008, 375.532], [0, 551.5649999999999, 565.25, 393.214, 411.738], [0, 551.5649999999999, 565.25, 429.41999999999996, 447.94399999999996], [0, 551.5649999999999, 565.25, 516.146, 534.67], [0, 551.5649999999999, 565.25, 553.194, 571.718], [0, 551.5649999999999, 565.25, 589.4, 607.924], [0, 551.5649999999999, 565.25, 624.764, 643.288]]
2026-08-10 13:22:14,663 INFO     29 [qwen-vl-text] ═══ DONE ═══ 45 positions, pages=1, time=15.8s
2026-08-10 13:22:14,682 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:22:14,683 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:Medication | outputs={"chunks": "1 items, types={'MedicationRecord': 1}", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:22:14,683 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:22:14,684 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:22:14.683+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 46, "failed": 0, "current": {"586b758094be11f1bd9827cf206dfa2d": {"id": "586b758094be11f1bd9827cf206dfa2d", "doc_id": "583d832894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "cji\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "cji\u7cd6\u5c3f\u75c5.pdf", "size": 719494, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368067335, "task_type": "dataflow", "root_trace_id": "d24053a1fe4d4cb6b28cd59a97da1a4b", "root_traceparent": "00-d24053a1fe4d4cb6b28cd59a97da1a4b-43fea21cae272936-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:22:14,693 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:22:14,695 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:22:14,695 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 13:22:14,695 INFO     29 [qwen-vl-text] positions(27): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:22:14,696 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [27]
2026-08-10 13:22:14,853 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:22:14,854 INFO     29 [qwen-vl-text] LLM extraction start, text_len=225
2026-08-10 13:22:14,854 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:14,854 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 49, \"bbox_end\": 75, \"encounter_dates\": [\"2024-12-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "顺中西医结合医院处方笺\n普通\n姓名\n性别：女\n年龄：51岁\n费别：自费\n病人ID：M045218\n处方号：67456\n就诊序号：69523\n体重：/（kg）\n药物过敏史：无\n住址：新密市\n开方日期：2024-12-18 10:37\n就诊科室：内科门诊\n临床诊断：2型糖尿病\nRp:\n盐酸二甲双胍片\n0.5g*60 X 8盒\n用法：每次0.5g 一日三次 口服\n备注：\n医师：吴爱香\n审核：\n核对：\n金额合计：80.00元\n调配：\n发药：\n药房：西药费",
    "role": "user"
  }
]
2026-08-10 13:22:17,317 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:17,317 INFO     29 [qwen-vl-text] LLM output (len=411):
{
  "encounter_date": "2024-12-18",
  "prescription_type": "门诊处方",
  "prescriber": "吴爱香",
  "department": "内科门诊",
  "diagnosis": "2型糖尿病",
  "items": [
    {
      "drug_generic_name": "盐酸二甲双胍片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "一日三次",
      "route": "口服",
      "duration_days": null,
      "quantity": "8盒",
      "notes": null
    }
  ]
}
2026-08-10 13:22:17,317 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-18]
2026-08-10 13:22:17,319 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1581782, prompt_len=919
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["顺中西医结合医院处方笺", "普通", "姓名", "性别：女", "年龄：51岁", "费别：自费", "病人ID：M045218", "处方号：67456", "就诊序号：69523", "体重：/（kg）", "药物过敏史：无", "住址：新密市", "开方日期：2024-12-18 10:37", "就诊科室：内科门诊", "临床诊断：2型糖尿病", "Rp:", "盐酸二甲双胍片", "0.5g*60 X 8盒", "用法：每次0.5g 一日三次 口服", "备注：", "医师：吴爱香", "审核：", "核对：", "金额合计：80.00元", "调配：", "发药：", "药房：西药费"]

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
2026-08-10 13:22:26,716 INFO     29 [qwen-vl-text] coord API raw response (len=1405):
[
	{"text": "顺中西医结合医院处方笺", "bbox": [275, 30, 781, 64]},
	{"text": "普通", "bbox": [805, 0, 853, 18]},
	{"text": "姓名", "bbox": [60, 103, 103, 122]},
	{"text": "性别：女", "bbox": [265, 100, 372, 119]},
	{"text": "年龄：51岁", "bbox": [410, 100, 546, 119]},
	{"text": "费别：自费", "bbox": [652, 101, 779, 120]},
	{"text": "病人ID：M045218", "bbox": [60, 125, 246, 142]},
	{"text": "处方号：67456", "bbox": [316, 123, 470, 141]},
	{"text": "就诊序号：69523", "bbox": [504, 123, 691, 141]},
	{"text": "体重：/（kg）", "bbox": [713, 124, 848, 143]},
	{"text": "药物过敏史：无", "bbox": [60, 147, 242, 167]},
	{"text": "住址：新密市", "bbox": [450, 146, 604, 166]},
	{"text": "开方日期：2024-12-18 10:37", "bbox": [60, 177, 406, 196]},
	{"text": "就诊科室：内科门诊", "bbox": [443, 175, 675, 195]},
	{"text": "临床诊断：2型糖尿病", "bbox": [60, 214, 315, 235]},
	{"text": "Rp:", "bbox": [60, 275, 123, 304]},
	{"text": "盐酸二甲双胍片", "bbox": [112, 307, 295, 327]},
	{"text": "0.5g*60 X 8盒", "bbox": [502, 306, 671, 327]},
	{"text": "用法：每次0.5g 一日三次 口服", "bbox": [157, 344, 528, 365]},
	{"text": "备注：", "bbox": [157, 810, 218, 830]},
	{"text": "医师：吴爱香", "bbox": [714, 829, 871, 851]},
	{"text": "审核：", "bbox": [143, 878, 204, 899]},
	{"text": "核对：", "bbox": [398, 877, 461, 897]},
	{"text": "金额合计：80.00元", "bbox": [624, 871, 856, 892]},
	{"text": "调配：", "bbox": [143, 909, 204, 929]},
	{"text": "发药：", "bbox": [398, 907, 461, 927]},
	{"text": "药房：西药费", "bbox": [651, 902, 808, 923]}
]
2026-08-10 13:22:26,716 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=9.4s
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[0]: text=顺中西医结合医院处方笺, bbox=[275, 30, 781, 64]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[805, 0, 853, 18]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[60, 103, 103, 122]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[265, 100, 372, 119]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：51岁, bbox=[410, 100, 546, 119]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[5]: text=费别：自费, bbox=[652, 101, 779, 120]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[6]: text=病人ID：M045218, bbox=[60, 125, 246, 142]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[7]: text=处方号：67456, bbox=[316, 123, 470, 141]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[8]: text=就诊序号：69523, bbox=[504, 123, 691, 141]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[9]: text=体重：/（kg）, bbox=[713, 124, 848, 143]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[10]: text=药物过敏史：无, bbox=[60, 147, 242, 167]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[11]: text=住址：新密市, bbox=[450, 146, 604, 166]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[12]: text=开方日期：2024-12-18 10:37, bbox=[60, 177, 406, 196]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[13]: text=就诊科室：内科门诊, bbox=[443, 175, 675, 195]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[14]: text=临床诊断：2型糖尿病, bbox=[60, 214, 315, 235]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[15]: text=Rp:, bbox=[60, 275, 123, 304]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[16]: text=盐酸二甲双胍片, bbox=[112, 307, 295, 327]
2026-08-10 13:22:26,717 INFO     29 [qwen-vl-text] coord item[17]: text=0.5g*60 X 8盒, bbox=[502, 306, 671, 327]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[18]: text=用法：每次0.5g 一日三次 口服, bbox=[157, 344, 528, 365]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[19]: text=备注：, bbox=[157, 810, 218, 830]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[20]: text=医师：吴爱香, bbox=[714, 829, 871, 851]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[21]: text=审核：, bbox=[143, 878, 204, 899]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[22]: text=核对：, bbox=[398, 877, 461, 897]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[23]: text=金额合计：80.00元, bbox=[624, 871, 856, 892]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[24]: text=调配：, bbox=[143, 909, 204, 929]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[25]: text=发药：, bbox=[398, 907, 461, 927]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] coord item[26]: text=药房：西药费, bbox=[651, 902, 808, 923]
2026-08-10 13:22:26,718 INFO     29 [qwen-vl-text] page=1 — 27/27 coords, api_time=9.4s
2026-08-10 13:22:26,719 INFO     29 [qwen-vl-text] new_positions (27):
[[1, 163.625, 464.695, 25.259999999999998, 53.888], [1, 478.97499999999997, 507.53499999999997, 0.0, 15.155999999999999], [1, 35.699999999999996, 61.285, 86.726, 102.72399999999999], [1, 157.67499999999998, 221.34, 84.2, 100.198], [1, 243.95, 324.87, 84.2, 100.198], [1, 387.94, 463.505, 85.042, 101.03999999999999], [1, 35.699999999999996, 146.37, 105.25, 119.564], [1, 188.01999999999998, 279.65, 103.566, 118.722], [1, 299.88, 411.145, 103.566, 118.722], [1, 424.23499999999996, 504.56, 104.408, 120.40599999999999], [1, 35.699999999999996, 143.98999999999998, 123.774, 140.614], [1, 267.75, 359.38, 122.932, 139.772], [1, 35.699999999999996, 241.57, 149.034, 165.03199999999998], [1, 263.585, 401.625, 147.35, 164.19], [1, 35.699999999999996, 187.42499999999998, 180.188, 197.87], [1, 35.699999999999996, 73.185, 231.54999999999998, 255.968], [1, 66.64, 175.525, 258.49399999999997, 275.334], [1, 298.69, 399.245, 257.652, 275.334], [1, 93.41499999999999, 314.15999999999997, 289.64799999999997, 307.33], [1, 93.41499999999999, 129.71, 682.02, 698.86], [1, 424.83, 518.245, 698.018, 716.542], [1, 85.085, 121.38, 739.276, 756.958], [1, 236.81, 274.295, 738.434, 755.274], [1, 371.28, 509.32, 733.382, 751.064], [1, 85.085, 121.38, 765.3779999999999, 782.218], [1, 236.81, 274.295, 763.694, 780.534], [1, 387.34499999999997, 480.76, 759.4839999999999, 777.1659999999999]]
2026-08-10 13:22:26,719 INFO     29 [qwen-vl-text] ═══ DONE ═══ 27 positions, pages=1, time=12.0s
2026-08-10 13:22:26,729 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:22:26,730 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:Prescription | outputs={"chunks": "1 items, types={'PrescriptionRecord': 1}", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:22:26,730 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:22:26,736 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:26,737 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:22:27,619 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:27,624 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:22:27,624 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:22:27,624 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:22:27,628 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:27,629 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:22:28,131 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:28,136 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:22:28,136 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:22:28,136 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:22:28,140 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:28,140 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:22:29,236 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:29,240 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:22:29,241 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:22:29,241 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:22:29,245 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:29,245 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:22:29,741 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:22:29,749 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:22:29,749 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "148 items", "markdown": "", "text": "", "name": "cji糖尿病.pdf", "output_format": "chunks", "chunks_Medication": "1 items, types={'MedicationRecord': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Medication\": 1, \"chunks_Prescription\": 1, \"chunks_LabExam\": 2, \"chunks_Clinical\": 1}"}
2026-08-10 13:22:29,749 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:22:29,750 INFO     29 [ChunkMerger] Merged 5 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 13:22:29,759 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:22:29,759 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "5 items, types={'LabReport': 2, 'OutpatientRecord': 1, 'MedicationRecord': 1, 'PrescriptionRecord': 1}", "name": "cji糖尿病.pdf"}
2026-08-10 13:22:29,759 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:22:29,788 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786368069534, 'update_date': datetime.datetime(2026, 8, 10, 13, 21, 9), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1035462, 'status': '1'}
2026-08-10 13:22:29,988 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白测定  HbA1c  8.1%  %  4-6%  True   
---
   糖化血红蛋白测定  HbA1c  9.8%  %  4-6%  True   
---
西医结合医院
病人门（急）诊病历
病人ID M0242896 姓名:
性别: 女 出生时间: 1974年12月28日
籍贯: 河南省新密市城关镇 民族: 汉族 婚否: 已婚 职业: 无
身份证号:
电话号码:
工作单位:
常住地址: 新密市东大街百货大楼
门诊号: 7253 接诊时间: 2024年12月18日 10时17分
就诊时间: 2024-12-18 10:17:16 体温: 36.3℃
主诉: 糖尿病2年
现病史: 2年前感觉浑身乏力,来院检查发现血糖高。
体格检查:
西医诊断: 1.糖尿病 中医诊断:
建议: 1、糖尿病饮食;保持心情愉悦;
2、适量运动;
3、规律服药;
4、定期监测血糖;
5、不适随诊。
过敏史: 无
族史: 有
往史: 无
理: 给予糖化血红蛋白检测,以了解血糖控制情况
注:
印时间: 2025.4.21 科室: 内科门诊 医生
---
河南省医疗门诊收费票据
河南省
票据代码：豫财410212
票据批次：0A[2018]
20241218527246
新密佰顺中西医结合医院
527245
业务流水号：
社会保障号码：
姓名
性别
医保类型
医疗机构类型
项目
数量
金额
自费
付金额
西药费
80.00
大额记账：
大病补充：
新密佰顺中西医结合
5241018333000778
发票专用章
现金支付：
合计(大写)：
捌拾元整
医保统筹支付：
个人账户支付：
其他医保支付：
个人支付金额：
收款单位(章)：
收款人(签章)：
527246
0061
80.00
盖
章
有
效
遗
失
不
补
---
顺中西医结合医院处方笺
普通
姓名
性别：女
年龄：51岁
费别：自费
病人ID：M045218
处方号：67456
就诊序号：69523
体重：/（kg）
药物过敏史：无
住址：新密市
开方日期：2024-12-18 10:37
就诊科室：内科门诊
临床诊断：2型糖尿病
Rp:
盐酸二甲双胍片
0.5g*60 X 8盒
用法：每次0.5g 一日三次 口服
备注：
医师：吴爱香
审核：
核对：
金额合计：80.00元
调配：
发药：
药房：西药费
2026-08-10 13:22:30,225 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:22:30,225 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "5 items, types={'LabReport': 2, 'OutpatientRecord': 1, 'MedicationRecord': 1, 'PrescriptionRecord': 1}", "name": "cji糖尿病.pdf", "embedding_token_consumption": 786}
2026-08-10 13:22:30,225 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:22:30,385 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:22:30,385 INFO     29 [Trace] task=586b7580 | doc=cji糖尿病.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":5,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:22:30,388 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(3, 361, 384, 446, 702) row[-1]=(3, 361, 384, 446, 702)
2026-08-10 13:22:30,388 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 336, 361, 452, 732) row[-1]=(4, 336, 361, 452, 732)
2026-08-10 13:22:30,388 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:22:30,389 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:22:30,389 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:22:30,393 INFO     29 set_progress(586b758094be11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:22:30 [DOC Engine]:
Start to index...
2026-08-10 13:22:30,411 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 13:22:30,415 INFO     29 set_progress(586b758094be11f1bd9827cf206dfa2d), progress: 0.8200000000000001, progress_msg: 
2026-08-10 13:22:30,422 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.005s]
2026-08-10 13:22:30,430 INFO     29 set_progress(586b758094be11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:22:30 Indexing done (0.04s). Task done (76.63s)
2026-08-10 13:22:30,432 INFO     29 [Done], chunks(5), token(786), elapsed:76.63
2026-08-10 13:22:30,506 INFO     29 handle_task done for task {"id": "586b758094be11f1bd9827cf206dfa2d", "doc_id": "583d832894be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "cji\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "cji\u7cd6\u5c3f\u75c5.pdf", "size": 719494, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786368067335, "task_type": "dataflow", "root_trace_id": "d24053a1fe4d4cb6b28cd59a97da1a4b", "root_traceparent": "00-d24053a1fe4d4cb6b28cd59a97da1a4b-43fea21cae272936-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
