# 基准结果：WYXI+糖尿病.pdf

## 基本信息

- 文件：`WYXI+糖尿病.pdf`
- 大小：231.7 KB
- PDF 总页数：3
- doc_id：`c996db3494c111f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:45:44  完成时间：2026-08-10T21:46:45  耗时：60.6s
- progress_msg：`13:46:42 Indexing done (0.02s). Task done (52.50s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 81c289a9 | 1 | 1-1 | Outpatient Patient Record 湖南旺旺医院 WantWan |
| 2 | 121abe55 | 2 | 2-3 | <table><tr><td>空腹血糖</td><td>GLU</td><td> |

- chunks 总数：2
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
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "LabReport": 1}`
- ChunkMerger：`{"found": true, "merged": 2, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：2 条
  - `[no_items_extracted] 2026-08-10 13:46:09,506 WARNING  29 [qwen-vl-table] page=0 no items extracted`
  - `[no_text_noise] 2026-08-10 13:46:41,814 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:45:46,684 INFO     29 handle_task begin for task {"id": "c9c3371a94c111f1bd9827cf206dfa2d", "doc_id": "c996db3494c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYXI+\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYXI+\u7cd6\u5c3f\u75c5.pdf", "size": 237287, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369545983, "task_type": "dataflow", "root_trace_id": "3de406fee81c49f9bc805cf32f9e9303", "root_traceparent": "00-3de406fee81c49f9bc805cf32f9e9303-9caf7738921ca49b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:45:46,903 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:45:47,006 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:45:47,015 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:45:47,015 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:45:47,015 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:45:47,020 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:45:47,020 INFO     29 ============================================================
2026-08-10 13:45:47,020 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:45:47,020 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:45:47,020 INFO     29 ============================================================
2026-08-10 13:45:47,020 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:45:47,020 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:45:47,021 INFO     29 No torch found.
2026-08-10 13:45:47,376 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=3
2026-08-10 13:45:47,657 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1261425, prompt_len=764
2026-08-10 13:45:49,764 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:45:49,765 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:45:49,774 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1261425, prompt_len=401
2026-08-10 13:45:55,244 INFO     29 [qwen-vl-parser] text API response (len=1025):
["Outpatient Patient Record", "湖南旺旺医院", "WantWant Hospital", "健康档案号:", "姓名:", "年龄: 50岁", "性别: 女", "婚姻:", "科别: 内分泌与代谢疾病专科", "职业: 不详", "籍贯: 湖南省常德市武陵区民族:", "地址/单位: 湖南省常德市武陵区不详", "过敏史: 无", "看诊时间: 2025/02/25 08:32", "疼痛评估: 0分", "跌倒风险: 无", "一般检查: 身高:156CM; 体重:61.5Kg; 体表面积:1.64m²; 身体质量指数:25.3", "体温:36.2℃(额温); 脉搏:92次/分; 呼吸:18次/分; 血压:128/80mmHg;", "血氧饱和度:98%", "意识:清醒", "主诉: 发现血糖高3+年。", "现病史: 自述没有怀孕。2021.10测空腹血糖: 6.9mmol/L, 注意饮食,", "未用药, 无特殊不适", "既往史: 无", "疫情或传染病史: -", "体格检查:", "无阳性体征", "辅助检查:", "葡萄糖测定一各种酶法(空腹): *空腹血糖 12.54mmol/L", "†: 糖化血红蛋白一高效液相法: *糖化血红蛋白A1c 9.2% †:", "初步诊断: 1、2型糖尿病", "处理措施:", "*处置:", "2025/02/25 08:33", "1.静脉采血: 1 次", "2.葡萄糖测定--各种酶法(空腹): 1 项", "3.一次性使用人体静脉血样采集容器(真空采血管-血清分离胶管): 1", "套(【自动产生】)", "4.糖化血红蛋白一高效液相法: 1 项", "5.一次性使用人体静脉血样采集容器(真空采血管): 1 套(【自动产生】)", "健康告知:", "建议完善尿常规、肝肾功能检查。建议用药降糖, 1、低糖、低脂、低盐饮食。2、", "适当运动, 每周3-5次,每次30分钟。3、监测血糖每周监测2-3天, 每日4", "医院地址:湖南省长沙市芙蓉区人民东路318号", "医院网址:http://www.wwhospital.com", "H01-06-YW-001", "联系电话:0731-82775411", "24小时急救电话:0731-82775120", "2020-03-A5", "页数: 1/2", "6"]
2026-08-10 13:45:55,245 INFO     29 [qwen-vl-parser] page=1 text: 51 lines (bbox 0-50)
2026-08-10 13:45:55,245 INFO     29 [qwen-vl-parser] page=1 text: 51 sections
2026-08-10 13:45:55,286 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:45:55.285+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 57, "failed": 0, "current": {"c9c3371a94c111f1bd9827cf206dfa2d": {"id": "c9c3371a94c111f1bd9827cf206dfa2d", "doc_id": "c996db3494c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYXI+\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYXI+\u7cd6\u5c3f\u75c5.pdf", "size": 237287, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369545983, "task_type": "dataflow", "root_trace_id": "3de406fee81c49f9bc805cf32f9e9303", "root_traceparent": "00-3de406fee81c49f9bc805cf32f9e9303-9caf7738921ca49b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:45:55,417 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=702904, prompt_len=764
2026-08-10 13:45:57,563 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-02-25"
}
```
2026-08-10 13:45:57,564 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2025-02-25
2026-08-10 13:45:57,584 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=702904, prompt_len=756
2026-08-10 13:45:58,584 INFO     29 [qwen-vl-parser] table API response (len=143):
\begin{tabular}{ccccccc}
\hline
代号 & 项目名称 & 结果 & 参考区间 & 单位 \\
\hline
GLU0 & *空腹血糖 & $\uparrow$ 12.54 & 3.9~6.1 & mmol/L \\
\hline
\end{tabular}
2026-08-10 13:45:58,585 INFO     29 [qwen-vl-parser] page=2 table: 8 LaTeX lines (bbox 51-58)
2026-08-10 13:45:58,585 INFO     29 [qwen-vl-parser] page=2 table: 8 sections
2026-08-10 13:45:58,761 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=713643, prompt_len=764
2026-08-10 13:46:00,933 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-02-25"
}
```
2026-08-10 13:46:00,934 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2025-02-25
2026-08-10 13:46:00,943 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=713643, prompt_len=756
2026-08-10 13:46:03,528 INFO     29 [qwen-vl-parser] table API response (len=151):
\begin{tabular}{l c c c c c c}
\hline
项目名称 & 结果 & 单位 & 参考区间 & & & \\
\hline
*糖化血红蛋白A1c & HbA1c $\uparrow$ 9.20 & \% & 4~6 & & & \\
\hline
\end{tabular}
2026-08-10 13:46:03,531 INFO     29 [qwen-vl-parser] page=3 table: 8 LaTeX lines (bbox 59-66)
2026-08-10 13:46:03,531 INFO     29 [qwen-vl-parser] page=3 table: 8 sections
2026-08-10 13:46:03,531 INFO     29 [qwen-vl-parser] parse_pdf done: 67 sections from 3 pages.
2026-08-10 13:46:03,538 INFO     29 Close text detector.
2026-08-10 13:46:03,952 INFO     29 Close text recognizer.
2026-08-10 13:46:04,335 INFO     29 Close recognizer.
2026-08-10 13:46:04,777 INFO     29 Close recognizer.
2026-08-10 13:46:05,391 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:46:05,391 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Parser:MedLink | outputs={"html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "json"}
2026-08-10 13:46:05,391 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:46:05,407 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:05,407 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] Outpatient Patient Record\n[BBOX-1] 湖南旺旺医院\n[BBOX-2] WantWant Hospital\n[BBOX-3] 健康档案号:\n[BBOX-4] 姓名:\n[BBOX-5] 年龄: 50岁\n[BBOX-6] 性别: 女\n[BBOX-7] 婚姻:\n[BBOX-8] 科别: 内分泌与代谢疾病专科\n[BBOX-9] 职业: 不详\n[BBOX-10] 籍贯: 湖南省常德市武陵区民族:\n[BBOX-11] 地址/单位: 湖南省常德市武陵区不详\n[BBOX-12] 过敏史: 无\n[BBOX-13] 看诊时间: 2025/02/25 08:32\n[BBOX-14] 疼痛评估: 0分\n[BBOX-15] 跌倒风险: 无\n[BBOX-16] 一般检查: 身高:156CM; 体重:61.5Kg; 体表面积:1.64m²; 身体质量指数:25.3\n[BBOX-17] 体温:36.2℃(额温); 脉搏:92次/分; 呼吸:18次/分; 血压:128/80mmHg;\n[BBOX-18] 血氧饱和度:98%\n[BBOX-19] 意识:清醒\n[BBOX-20] 主诉: 发现血糖高3+年。\n[BBOX-21] 现病史: 自述没有怀孕。2021.10测空腹血糖: 6.9mmol/L, 注意饮食,\n[BBOX-22] 未用药, 无特殊不适\n[BBOX-23] 既往史: 无\n[BBOX-24] 疫情或传染病史: -\n[BBOX-25] 体格检查:\n[BBOX-26] 无阳性体征\n[BBOX-27] 辅助检查:\n[BBOX-28] 葡萄糖测定一各种酶法(空腹): *空腹血糖 12.54mmol/L\n[BBOX-29] †: 糖化血红蛋白一高效液相法: *糖化血红蛋白A1c 9.2% †:\n[BBOX-30] 初步诊断: 1、2型糖尿病\n[BBOX-31] 处理措施:\n[BBOX-32] *处置:\n[BBOX-33] 2025/02/25 08:33\n[BBOX-34] 1.静脉采血: 1 次\n[BBOX-35] 2.葡萄糖测定--各种酶法(空腹): 1 项\n[BBOX-36] 3.一次性使用人体静脉血样采集容器(真空采血管-血清分离胶管): 1\n[BBOX-37] 套(【自动产生】)\n[BBOX-38] 4.糖化血红蛋白一高效液相法: 1 项\n[BBOX-39] 5.一次性使用人体静脉血样采集容器(真空采血管): 1 套(【自动产生】)\n[BBOX-40] 健康告知:\n[BBOX-41] 建议完善尿常规、肝肾功能检查。建议用药降糖, 1、低糖、低脂、低盐饮食。2、\n[BBOX-42] 适当运动, 每周3-5次,每次30分钟。3、监测血糖每周监测2-3天, 每日4\n[BBOX-43] 医院地址:湖南省长沙市芙蓉区人民东路318号\n[BBOX-44] 医院网址:http://www.wwhospital.com\n[BBOX-45] H01-06-YW-001\n[BBOX-46] 联系电话:0731-82775411\n[BBOX-47] 24小时急救电话:0731-82775120\n[BBOX-48] 2020-03-A5\n[BBOX-49] 页数: 1/2\n[BBOX-50] 6\n[BBOX-51] \\begin{tabular}{ccccccc}\n[BBOX-52] 报告时间: 2025-02-25\n[BBOX-53] \\hline\n[BBOX-54] 代号 & 项目名称 & 结果 & 参考区间 & 单位 \\\\\n[BBOX-55] \\hline\n[BBOX-56] GLU0 & *空腹血糖 & $\\uparrow$ 12.54 & 3.9~6.1 & mmol/L \\\\\n[BBOX-57] \\hline\n[BBOX-58] \\end{tabular}\n[BBOX-59] \\begin{tabular}{l c c c c c c}\n[BBOX-60] 报告时间: 2025-02-25\n[BBOX-61] \\hline\n[BBOX-62] 项目名称 & 结果 & 单位 & 参考区间 & & & \\\\\n[BBOX-63] \\hline\n[BBOX-64] *糖化血红蛋白A1c & HbA1c $\\uparrow$ 9.20 & \\% & 4~6 & & & \\\\\n[BBOX-65] \\hline\n[BBOX-66] \\end{tabular}"
  }
]
2026-08-10 13:46:08,094 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:08,111 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'LabReport': 1}
2026-08-10 13:46:08,121 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:46:08,121 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'LabReport': 1}"}
2026-08-10 13:46:08,121 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:46:08,121 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_LabExam': 1}
2026-08-10 13:46:08,131 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:46:08,131 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | ChunkRouter:Router | outputs={"html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'LabReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:08,131 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:46:08,135 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:46:08,136 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:46:08,136 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[0, 1, 2]
2026-08-10 13:46:08,136 INFO     29 [qwen-vl-table] positions ： [[0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:46:08,386 INFO     29 [qwen-vl-table] page=0, rect=718x1028, img=(1995x2856)
2026-08-10 13:46:08,595 INFO     29 [qwen-vl-table] page=1, rect=1048x776, img=(2912x2156)
2026-08-10 13:46:08,809 INFO     29 [qwen-vl-table] page=2, rect=1048x796, img=(2912x2212)
2026-08-10 13:46:08,810 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:08,810 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 50, \"bbox_end\": 66, \"encounter_dates\": [\"2025-02-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "6\n\\begin{tabular}{ccccccc}\n报告时间: 2025-02-25\n\\hline\n代号 & 项目名称 & 结果 & 参考区间 & 单位 \\\\",
    "role": "user"
  }
]
2026-08-10 13:46:09,505 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:09,505 INFO     29 [qwen-vl-table] page=0 LLM output (len=48):
{
  "report_date": "2025-02-25",
  "items": []
}
2026-08-10 13:46:09,506 WARNING  29 [qwen-vl-table] page=0 no items extracted
2026-08-10 13:46:09,506 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:09,506 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 50, \"bbox_end\": 66, \"encounter_dates\": [\"2025-02-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\hline\nGLU0 & *空腹血糖 & $\\uparrow$ 12.54 & 3.9~6.1 & mmol/L \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{l c c c c c c}",
    "role": "user"
  }
]
2026-08-10 13:46:10,645 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:10,645 INFO     29 [qwen-vl-table] page=1 LLM output (len=218):
{
  "report_date": "2025-02-25",
  "items": [
    {
      "name": "空腹血糖",
      "item_code": "GLU",
      "value": "12.54",
      "unit": "mmol/L",
      "reference_range": "3.9~6.1",
      "abnormal": true
    }
  ]
}
2026-08-10 13:46:10,645 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:10,645 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 50, \"bbox_end\": 66, \"encounter_dates\": [\"2025-02-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "报告时间: 2025-02-25\n\\hline\n项目名称 & 结果 & 单位 & 参考区间 & & & \\\\\n\\hline\n*糖化血红蛋白A1c & HbA1c $\\uparrow$ 9.20 & \\% & 4~6 & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:46:11,765 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:11,766 INFO     29 [qwen-vl-table] page=2 LLM output (len=215):
{
  "report_date": "2025-02-25",
  "items": [
    {
      "name": "糖化血红蛋白A1c",
      "item_code": "HbA1c",
      "value": "9.20",
      "unit": "%",
      "reference_range": "4~6",
      "abnormal": true
    }
  ]
}
2026-08-10 13:46:11,766 INFO     29 [qwen-vl-table] coord grouping: {1: 1, 2: 1}
2026-08-10 13:46:11,770 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1006884, prompt_len=511
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
空腹血糖

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
2026-08-10 13:46:14,067 INFO     29 [qwen-vl-table] coord API raw response (len=63):
```json
[
	{"text": "空腹血糖", "bbox": [140, 217, 216, 240]}
]
```
2026-08-10 13:46:14,068 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=2.3s
2026-08-10 13:46:14,068 INFO     29 [qwen-vl-table] coord item[0]: text=空腹血糖, bbox=[140, 217, 216, 240]
2026-08-10 13:46:14,068 INFO     29 [qwen-vl-table] page=1 coord: matched 1/1, time=2.3s
2026-08-10 13:46:14,072 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1023942, prompt_len=516
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白A1c

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
2026-08-10 13:46:16,440 INFO     29 [qwen-vl-table] coord API raw response (len=67):
```json
[
	{"text": "糖化血红蛋白A1c", "bbox": [17, 217, 160, 243]}
]
```
2026-08-10 13:46:16,440 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=2.4s
2026-08-10 13:46:16,440 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白A1c, bbox=[17, 217, 160, 243]
2026-08-10 13:46:16,440 INFO     29 [qwen-vl-table] page=2 coord: matched 1/1, time=2.4s
2026-08-10 13:46:16,441 INFO     29 [qwen-vl-table] new_positions (2):
[[2, 146.72, 226.368, 168.392, 186.24], [3, 17.816000000000003, 167.68, 172.732, 193.428]]
2026-08-10 13:46:16,441 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=3, time=8.3s
2026-08-10 13:46:16,458 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:46:16,459 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:16,459 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:46:16,466 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:16,467 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:46:17,689 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:17,694 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:46:17,694 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:17,694 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:46:17,699 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:46:17,699 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:46:17,699 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:46:17,699 INFO     29 [qwen-vl-text] positions(50): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:46:17,699 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [50]
2026-08-10 13:46:17,949 INFO     29 [qwen-vl-text] page=0, rect=718x1028, img=(1995x2856), dpi=200
2026-08-10 13:46:17,951 INFO     29 [qwen-vl-text] LLM extraction start, text_len=869
2026-08-10 13:46:17,951 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:17,952 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 49, \"encounter_dates\": [\"2025-02-25\"], \"department\": \"内分泌与代谢疾病专科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "Outpatient Patient Record\n湖南旺旺医院\nWantWant Hospital\n健康档案号:\n姓名:\n年龄: 50岁\n性别: 女\n婚姻:\n科别: 内分泌与代谢疾病专科\n职业: 不详\n籍贯: 湖南省常德市武陵区民族:\n地址/单位: 湖南省常德市武陵区不详\n过敏史: 无\n看诊时间: 2025/02/25 08:32\n疼痛评估: 0分\n跌倒风险: 无\n一般检查: 身高:156CM; 体重:61.5Kg; 体表面积:1.64m²; 身体质量指数:25.3\n体温:36.2℃(额温); 脉搏:92次/分; 呼吸:18次/分; 血压:128/80mmHg;\n血氧饱和度:98%\n意识:清醒\n主诉: 发现血糖高3+年。\n现病史: 自述没有怀孕。2021.10测空腹血糖: 6.9mmol/L, 注意饮食,\n未用药, 无特殊不适\n既往史: 无\n疫情或传染病史: -\n体格检查:\n无阳性体征\n辅助检查:\n葡萄糖测定一各种酶法(空腹): *空腹血糖 12.54mmol/L\n†: 糖化血红蛋白一高效液相法: *糖化血红蛋白A1c 9.2% †:\n初步诊断: 1、2型糖尿病\n处理措施:\n*处置:\n2025/02/25 08:33\n1.静脉采血: 1 次\n2.葡萄糖测定--各种酶法(空腹): 1 项\n3.一次性使用人体静脉血样采集容器(真空采血管-血清分离胶管): 1\n套(【自动产生】)\n4.糖化血红蛋白一高效液相法: 1 项\n5.一次性使用人体静脉血样采集容器(真空采血管): 1 套(【自动产生】)\n健康告知:\n建议完善尿常规、肝肾功能检查。建议用药降糖, 1、低糖、低脂、低盐饮食。2、\n适当运动, 每周3-5次,每次30分钟。3、监测血糖每周监测2-3天, 每日4\n医院地址:湖南省长沙市芙蓉区人民东路318号\n医院网址:http://www.wwhospital.com\nH01-06-YW-001\n联系电话:0731-82775411\n24小时急救电话:0731-82775120\n2020-03-A5\n页数: 1/2",
    "role": "user"
  }
]
2026-08-10 13:46:19,494 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:19,494 INFO     29 [qwen-vl-text] LLM output (len=218):
{
  "encounter_date": "2025-02-25",
  "chief_complaint": "发现血糖高3+年。",
  "present_illness": "自述没有怀孕。2021.10测空腹血糖: 6.9mmol/L, 注意饮食, 未用药, 无特殊不适",
  "past_history": "无",
  "diagnosis": "1、2型糖尿病",
  "treatment_plan": null
}
2026-08-10 13:46:19,494 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-25]
2026-08-10 13:46:19,502 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2153192, prompt_len=1632
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共50行）
["Outpatient Patient Record", "湖南旺旺医院", "WantWant Hospital", "健康档案号:", "姓名:", "年龄: 50岁", "性别: 女", "婚姻:", "科别: 内分泌与代谢疾病专科", "职业: 不详", "籍贯: 湖南省常德市武陵区民族:", "地址/单位: 湖南省常德市武陵区不详", "过敏史: 无", "看诊时间: 2025/02/25 08:32", "疼痛评估: 0分", "跌倒风险: 无", "一般检查: 身高:156CM; 体重:61.5Kg; 体表面积:1.64m²; 身体质量指数:25.3", "体温:36.2℃(额温); 脉搏:92次/分; 呼吸:18次/分; 血压:128/80mmHg;", "血氧饱和度:98%", "意识:清醒", "主诉: 发现血糖高3+年。", "现病史: 自述没有怀孕。2021.10测空腹血糖: 6.9mmol/L, 注意饮食,", "未用药, 无特殊不适", "既往史: 无", "疫情或传染病史: -", "体格检查:", "无阳性体征", "辅助检查:", "葡萄糖测定一各种酶法(空腹): *空腹血糖 12.54mmol/L", "†: 糖化血红蛋白一高效液相法: *糖化血红蛋白A1c 9.2% †:", "初步诊断: 1、2型糖尿病", "处理措施:", "*处置:", "2025/02/25 08:33", "1.静脉采血: 1 次", "2.葡萄糖测定--各种酶法(空腹): 1 项", "3.一次性使用人体静脉血样采集容器(真空采血管-血清分离胶管): 1", "套(【自动产生】)", "4.糖化血红蛋白一高效液相法: 1 项", "5.一次性使用人体静脉血样采集容器(真空采血管): 1 套(【自动产生】)", "健康告知:", "建议完善尿常规、肝肾功能检查。建议用药降糖, 1、低糖、低脂、低盐饮食。2、", "适当运动, 每周3-5次,每次30分钟。3、监测血糖每周监测2-3天, 每日4", "医院地址:湖南省长沙市芙蓉区人民东路318号", "医院网址:http://www.wwhospital.com", "H01-06-YW-001", "联系电话:0731-82775411", "24小时急救电话:0731-82775120", "2020-03-A5", "页数: 1/2"]

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
2026-08-10 13:46:37,513 INFO     29 [qwen-vl-text] coord API raw response (len=3027):
[
	{"text": "Outpatient Patient Record", "bbox": [348, 7, 647, 27]},
	{"text": "湖南旺旺医院", "bbox": [102, 30, 269, 50]},
	{"text": "WantWant Hospital", "bbox": [224, 55, 434, 73]},
	{"text": "健康档案号:", "bbox": [498, 52, 648, 72]},
	{"text": "姓名:", "bbox": [25, 78, 90, 98]},
	{"text": "年龄: 50岁", "bbox": [25, 100, 156, 118]},
	{"text": "性别: 女", "bbox": [348, 100, 454, 118]},
	{"text": "婚姻:", "bbox": [720, 100, 788, 118]},
	{"text": "科别: 内分泌与代谢疾病专科", "bbox": [25, 120, 378, 140]},
	{"text": "职业: 不详", "bbox": [734, 145, 870, 164]},
	{"text": "籍贯: 湖南省常德市武陵区民族:", "bbox": [25, 144, 413, 164]},
	{"text": "地址/单位: 湖南省常德市武陵区不详", "bbox": [25, 169, 479, 189]},
	{"text": "过敏史: 无", "bbox": [25, 194, 156, 214]},
	{"text": "看诊时间: 2025/02/25 08:32", "bbox": [631, 219, 935, 237]},
	{"text": "疼痛评估: 0分", "bbox": [25, 245, 175, 264]},
	{"text": "跌倒风险: 无", "bbox": [25, 269, 164, 288]},
	{"text": "一般检查: 身高:156CM; 体重:61.5Kg; 体表面积:1.64m²; 身体质量指数:25.3", "bbox": [25, 294, 852, 313]},
	{"text": "体温:36.2℃(额温); 脉搏:92次/分; 呼吸:18次/分; 血压:128/80mmHg;", "bbox": [77, 320, 824, 339]},
	{"text": "血氧饱和度:98%", "bbox": [77, 347, 240, 365]},
	{"text": "意识:清醒", "bbox": [313, 347, 421, 365]},
	{"text": "主诉: 发现血糖高3+年。", "bbox": [25, 379, 299, 398]},
	{"text": "现病史: 自述没有怀孕。2021.10测空腹血糖: 6.9mmol/L, 注意饮食,", "bbox": [25, 403, 739, 421]},
	{"text": "未用药, 无特殊不适", "bbox": [75, 427, 287, 445]},
	{"text": "既往史: 无", "bbox": [25, 452, 144, 470]},
	{"text": "疫情或传染病史: -", "bbox": [25, 476, 235, 494]},
	{"text": "体格检查:", "bbox": [25, 501, 126, 519]},
	{"text": "无阳性体征", "bbox": [74, 524, 189, 543]},
	{"text": "辅助检查:", "bbox": [25, 550, 126, 568]},
	{"text": "葡萄糖测定一各种酶法(空腹): *空腹血糖 12.54mmol/L", "bbox": [75, 574, 658, 592]},
	{"text": "†: 糖化血红蛋白一高效液相法: *糖化血红蛋白A1c 9.2% †:", "bbox": [77, 599, 725, 617]},
	{"text": "初步诊断: 1、2型糖尿病", "bbox": [25, 625, 284, 643]},
	{"text": "处理措施:", "bbox": [25, 650, 126, 668]},
	{"text": "*处置:", "bbox": [44, 670, 103, 686]},
	{"text": "2025/02/25 08:33", "bbox": [19, 691, 175, 707]},
	{"text": "1.静脉采血: 1 次", "bbox": [216, 691, 379, 707]},
	{"text": "2.葡萄糖测定--各种酶法(空腹): 1 项", "bbox": [216, 709, 559, 725]},
	{"text": "3.一次性使用人体静脉血样采集容器(真空采血管-血清分离胶管): 1", "bbox": [216, 727, 844, 743]},
	{"text": "套(【自动产生】)", "bbox": [216, 746, 375, 762]},
	{"text": "4.糖化血红蛋白一高效液相法: 1 项", "bbox": [216, 765, 539, 781]},
	{"text": "5.一次性使用人体静脉血样采集容器(真空采血管): 1 套(【自动产生】)", "bbox": [216, 784, 870, 800]},
	{"text": "健康告知:", "bbox": [25, 807, 126, 825]},
	{"text": "建议完善尿常规、肝肾功能检查。建议用药降糖, 1、低糖、低脂、低盐饮食。2、", "bbox": [72, 831, 915, 850]},
	{"text": "适当运动, 每周3-5次,每次30分钟。3、监测血糖每周监测2-3天, 每日4", "bbox": [72, 856, 820, 875]},
	{"text": "医院地址:湖南省长沙市芙蓉区人民东路318号", "bbox": [19, 877, 457, 894]},
	{"text": "医院网址:http://www.wwhospital.com", "bbox": [19, 894, 356, 910]},
	{"text": "H01-06-YW-001", "bbox": [19, 912, 170, 927]},
	{"text": "联系电话:0731-82775411", "bbox": [704, 878, 947, 894]},
	{"text": "24小时急救电话:0731-82775120", "bbox": [637, 896, 948, 912]},
	{"text": "2020-03-A5", "bbox": [820, 915, 935, 930]},
	{"text": "页数: 1/2", "bbox": [817, 24, 920, 37]}
]
2026-08-10 13:46:37,513 INFO     29 [qwen-vl-text] coord API: raw_items=50, valid_items=50, elapsed=18.0s
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[0]: text=Outpatient Patient Record, bbox=[348, 7, 647, 27]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[1]: text=湖南旺旺医院, bbox=[102, 30, 269, 50]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[2]: text=WantWant Hospital, bbox=[224, 55, 434, 73]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[3]: text=健康档案号:, bbox=[498, 52, 648, 72]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[25, 78, 90, 98]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[5]: text=年龄: 50岁, bbox=[25, 100, 156, 118]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[6]: text=性别: 女, bbox=[348, 100, 454, 118]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻:, bbox=[720, 100, 788, 118]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[8]: text=科别: 内分泌与代谢疾病专科, bbox=[25, 120, 378, 140]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[9]: text=职业: 不详, bbox=[734, 145, 870, 164]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[10]: text=籍贯: 湖南省常德市武陵区民族:, bbox=[25, 144, 413, 164]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[11]: text=地址/单位: 湖南省常德市武陵区不详, bbox=[25, 169, 479, 189]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[12]: text=过敏史: 无, bbox=[25, 194, 156, 214]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[13]: text=看诊时间: 2025/02/25 08:32, bbox=[631, 219, 935, 237]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[14]: text=疼痛评估: 0分, bbox=[25, 245, 175, 264]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[15]: text=跌倒风险: 无, bbox=[25, 269, 164, 288]
2026-08-10 13:46:37,514 INFO     29 [qwen-vl-text] coord item[16]: text=一般检查: 身高:156CM; 体重:61.5Kg; 体表面积:1.64m²; 身体质量指数:25.3, bbox=[25, 294, 852, 313]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[17]: text=体温:36.2℃(额温); 脉搏:92次/分; 呼吸:18次/分; 血压:128/80mmHg;, bbox=[77, 320, 824, 339]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[18]: text=血氧饱和度:98%, bbox=[77, 347, 240, 365]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[19]: text=意识:清醒, bbox=[313, 347, 421, 365]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[20]: text=主诉: 发现血糖高3+年。, bbox=[25, 379, 299, 398]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[21]: text=现病史: 自述没有怀孕。2021.10测空腹血糖: 6.9mmol/L, 注意饮食,, bbox=[25, 403, 739, 421]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[22]: text=未用药, 无特殊不适, bbox=[75, 427, 287, 445]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[23]: text=既往史: 无, bbox=[25, 452, 144, 470]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[24]: text=疫情或传染病史: -, bbox=[25, 476, 235, 494]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[25]: text=体格检查:, bbox=[25, 501, 126, 519]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[26]: text=无阳性体征, bbox=[74, 524, 189, 543]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[27]: text=辅助检查:, bbox=[25, 550, 126, 568]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[28]: text=葡萄糖测定一各种酶法(空腹): *空腹血糖 12.54mmol/L, bbox=[75, 574, 658, 592]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[29]: text=†: 糖化血红蛋白一高效液相法: *糖化血红蛋白A1c 9.2% †:, bbox=[77, 599, 725, 617]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[30]: text=初步诊断: 1、2型糖尿病, bbox=[25, 625, 284, 643]
2026-08-10 13:46:37,515 INFO     29 [qwen-vl-text] coord item[31]: text=处理措施:, bbox=[25, 650, 126, 668]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[32]: text=*处置:, bbox=[44, 670, 103, 686]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[33]: text=2025/02/25 08:33, bbox=[19, 691, 175, 707]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[34]: text=1.静脉采血: 1 次, bbox=[216, 691, 379, 707]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[35]: text=2.葡萄糖测定--各种酶法(空腹): 1 项, bbox=[216, 709, 559, 725]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[36]: text=3.一次性使用人体静脉血样采集容器(真空采血管-血清分离胶管): 1, bbox=[216, 727, 844, 743]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[37]: text=套(【自动产生】), bbox=[216, 746, 375, 762]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[38]: text=4.糖化血红蛋白一高效液相法: 1 项, bbox=[216, 765, 539, 781]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[39]: text=5.一次性使用人体静脉血样采集容器(真空采血管): 1 套(【自动产生】), bbox=[216, 784, 870, 800]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[40]: text=健康告知:, bbox=[25, 807, 126, 825]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[41]: text=建议完善尿常规、肝肾功能检查。建议用药降糖, 1、低糖、低脂、低盐饮食。2、, bbox=[72, 831, 915, 850]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[42]: text=适当运动, 每周3-5次,每次30分钟。3、监测血糖每周监测2-3天, 每日4, bbox=[72, 856, 820, 875]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[43]: text=医院地址:湖南省长沙市芙蓉区人民东路318号, bbox=[19, 877, 457, 894]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[44]: text=医院网址:http://www.wwhospital.com, bbox=[19, 894, 356, 910]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[45]: text=H01-06-YW-001, bbox=[19, 912, 170, 927]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[46]: text=联系电话:0731-82775411, bbox=[704, 878, 947, 894]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[47]: text=24小时急救电话:0731-82775120, bbox=[637, 896, 948, 912]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[48]: text=2020-03-A5, bbox=[820, 915, 935, 930]
2026-08-10 13:46:37,516 INFO     29 [qwen-vl-text] coord item[49]: text=页数: 1/2, bbox=[817, 24, 920, 37]
2026-08-10 13:46:37,517 INFO     29 [qwen-vl-text] page=0 — 50/50 coords, api_time=18.0s
2026-08-10 13:46:37,517 INFO     29 [qwen-vl-text] new_positions (50):
[[0, 249.86399999999998, 464.546, 7.196, 27.756], [0, 73.23599999999999, 193.142, 30.84, 51.4], [0, 160.832, 311.61199999999997, 56.54, 75.044], [0, 357.56399999999996, 465.264, 53.456, 74.016], [0, 17.95, 64.62, 80.184, 100.744], [0, 17.95, 112.008, 102.8, 121.304], [0, 249.86399999999998, 325.972, 102.8, 121.304], [0, 516.96, 565.784, 102.8, 121.304], [0, 17.95, 271.404, 123.36, 143.92000000000002], [0, 527.012, 624.66, 149.06, 168.592], [0, 17.95, 296.534, 148.032, 168.592], [0, 17.95, 343.92199999999997, 173.732, 194.292], [0, 17.95, 112.008, 199.43200000000002, 219.99200000000002], [0, 453.058, 671.3299999999999, 225.132, 243.636], [0, 17.95, 125.64999999999999, 251.86, 271.392], [0, 17.95, 117.752, 276.532, 296.064], [0, 17.95, 611.736, 302.232, 321.764], [0, 55.286, 591.632, 328.96000000000004, 348.492], [0, 55.286, 172.32, 356.716, 375.22], [0, 224.73399999999998, 302.27799999999996, 356.716, 375.22], [0, 17.95, 214.682, 389.612, 409.144], [0, 17.95, 530.602, 414.284, 432.788], [0, 53.849999999999994, 206.066, 438.956, 457.46000000000004], [0, 17.95, 103.392, 464.656, 483.16], [0, 17.95, 168.73, 489.32800000000003, 507.832], [0, 17.95, 90.46799999999999, 515.028, 533.532], [0, 53.132, 135.702, 538.672, 558.2040000000001], [0, 17.95, 90.46799999999999, 565.4, 583.904], [0, 53.849999999999994, 472.44399999999996, 590.072, 608.576], [0, 55.286, 520.55, 615.772, 634.2760000000001], [0, 17.95, 203.91199999999998, 642.5, 661.004], [0, 17.95, 90.46799999999999, 668.2, 686.7040000000001], [0, 31.592, 73.954, 688.76, 705.208], [0, 13.642, 125.64999999999999, 710.3480000000001, 726.796], [0, 155.088, 272.122, 710.3480000000001, 726.796], [0, 155.088, 401.36199999999997, 728.852, 745.3000000000001], [0, 155.088, 605.992, 747.356, 763.804], [0, 155.088, 269.25, 766.888, 783.336], [0, 155.088, 387.002, 786.4200000000001, 802.868], [0, 155.088, 624.66, 805.952, 822.4], [0, 17.95, 90.46799999999999, 829.596, 848.1], [0, 51.696, 656.97, 854.268, 873.8000000000001], [0, 51.696, 588.76, 879.9680000000001, 899.5], [0, 13.642, 328.126, 901.556, 919.032], [0, 13.642, 255.608, 919.032, 935.48], [0, 13.642, 122.06, 937.5360000000001, 952.956], [0, 505.472, 679.946, 902.5840000000001, 919.032], [0, 457.366, 680.664, 921.088, 937.5360000000001], [0, 588.76, 671.3299999999999, 940.62, 956.0400000000001], [0, 586.606, 660.56, 24.672, 38.036]]
2026-08-10 13:46:37,517 INFO     29 [qwen-vl-text] ═══ DONE ═══ 50 positions, pages=1, time=19.8s
2026-08-10 13:46:37,529 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:46:37,529 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:37,529 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:46:37,530 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:46:37.530+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 57, "failed": 0, "current": {"c9c3371a94c111f1bd9827cf206dfa2d": {"id": "c9c3371a94c111f1bd9827cf206dfa2d", "doc_id": "c996db3494c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYXI+\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYXI+\u7cd6\u5c3f\u75c5.pdf", "size": 237287, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369545983, "task_type": "dataflow", "root_trace_id": "3de406fee81c49f9bc805cf32f9e9303", "root_traceparent": "00-3de406fee81c49f9bc805cf32f9e9303-9caf7738921ca49b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:46:37,535 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:37,535 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:46:38,794 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:38,799 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:46:38,799 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:38,799 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:46:38,803 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:38,804 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:46:39,262 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:39,269 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:46:39,270 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:39,270 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:46:39,275 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:39,275 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:46:39,719 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:39,725 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:46:39,726 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:39,726 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:46:39,730 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:39,730 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:46:40,207 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:40,212 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:46:40,212 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:40,212 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:46:40,216 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:40,217 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:46:41,322 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:41,326 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:46:41,327 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:41,327 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:46:41,331 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:41,331 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:46:41,805 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:46:41,814 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:46:41,814 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "67 items", "markdown": "", "text": "", "name": "WYXI+糖尿病.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 13:46:41,814 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:46:41,814 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:46:41,823 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:46:41,823 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'LabReport': 1, 'OutpatientRecord': 1}", "name": "WYXI+糖尿病.pdf"}
2026-08-10 13:46:41,823 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:46:41,856 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786369546900, 'update_date': datetime.datetime(2026, 8, 10, 13, 45, 46), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1049374, 'status': '1'}
2026-08-10 13:46:42,067 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   空腹血糖  GLU  12.54  mmol/L  3.9~6.1  True    糖化血红蛋白A1c  HbA1c  9.20  %  4~6  True   
---
Outpatient Patient Record
湖南旺旺医院
WantWant Hospital
健康档案号:
姓名:
年龄: 50岁
性别: 女
婚姻:
科别: 内分泌与代谢疾病专科
职业: 不详
籍贯: 湖南省常德市武陵区民族:
地址/单位: 湖南省常德市武陵区不详
过敏史: 无
看诊时间: 2025/02/25 08:32
疼痛评估: 0分
跌倒风险: 无
一般检查: 身高:156CM; 体重:61.5Kg; 体表面积:1.64m²; 身体质量指数:25.3
体温:36.2℃(额温); 脉搏:92次/分; 呼吸:18次/分; 血压:128/80mmHg;
血氧饱和度:98%
意识:清醒
主诉: 发现血糖高3+年。
现病史: 自述没有怀孕。2021.10测空腹血糖: 6.9mmol/L, 注意饮食,
未用药, 无特殊不适
既往史: 无
疫情或传染病史: -
体格检查:
无阳性体征
辅助检查:
葡萄糖测定一各种酶法(空腹): *空腹血糖 12.54mmol/L
†: 糖化血红蛋白一高效液相法: *糖化血红蛋白A1c 9.2% †:
初步诊断: 1、2型糖尿病
处理措施:
*处置:
2025/02/25 08:33
1.静脉采血: 1 次
2.葡萄糖测定--各种酶法(空腹): 1 项
3.一次性使用人体静脉血样采集容器(真空采血管-血清分离胶管): 1
套(【自动产生】)
4.糖化血红蛋白一高效液相法: 1 项
5.一次性使用人体静脉血样采集容器(真空采血管): 1 套(【自动产生】)
健康告知:
建议完善尿常规、肝肾功能检查。建议用药降糖, 1、低糖、低脂、低盐饮食。2、
适当运动, 每周3-5次,每次30分钟。3、监测血糖每周监测2-3天, 每日4
医院地址:湖南省长沙市芙蓉区人民东路318号
医院网址:http://www.wwhospital.com
H01-06-YW-001
联系电话:0731-82775411
24小时急救电话:0731-82775120
2020-03-A5
页数: 1/2
2026-08-10 13:46:42,266 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:46:42,266 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'LabReport': 1, 'OutpatientRecord': 1}", "name": "WYXI+糖尿病.pdf", "embedding_token_consumption": 729}
2026-08-10 13:46:42,266 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:46:42,432 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:46:42,432 INFO     29 [Trace] task=c9c3371a | doc=WYXI+糖尿病.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:46:42,434 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(2, 146, 226, 168, 186) row[-1]=(3, 17, 167, 172, 193)
2026-08-10 13:46:42,434 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:46:42,437 INFO     29 set_progress(c9c3371a94c111f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:46:42 [DOC Engine]:
Start to index...
2026-08-10 13:46:42,446 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.006s]
2026-08-10 13:46:42,449 INFO     29 set_progress(c9c3371a94c111f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 13:46:42,453 INFO     29 set_progress(c9c3371a94c111f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:46:42 Indexing done (0.02s). Task done (52.50s)
2026-08-10 13:46:42,456 INFO     29 [Done], chunks(2), token(729), elapsed:52.50
2026-08-10 13:46:42,503 INFO     29 handle_task done for task {"id": "c9c3371a94c111f1bd9827cf206dfa2d", "doc_id": "c996db3494c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WYXI+\u7cd6\u5c3f\u75c5.pdf", "type": "pdf", "location": "WYXI+\u7cd6\u5c3f\u75c5.pdf", "size": 237287, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786369545983, "task_type": "dataflow", "root_trace_id": "3de406fee81c49f9bc805cf32f9e9303", "root_traceparent": "00-3de406fee81c49f9bc805cf32f9e9303-9caf7738921ca49b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
