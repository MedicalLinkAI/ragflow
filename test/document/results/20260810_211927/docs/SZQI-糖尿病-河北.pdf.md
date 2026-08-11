# 基准结果：SZQI-糖尿病-河北.pdf

## 基本信息

- 文件：`SZQI-糖尿病-河北.pdf`
- 大小：350.2 KB
- PDF 总页数：2
- doc_id：`1d42193494c111f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:40:55  完成时间：2026-08-10T21:42:06  耗时：71.3s
- progress_msg：`13:42:00 Indexing done (0.02s). Task done (58.99s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 8d1094df | 1 | 1-1 | 门诊病历 姓名: 性别: 男 年龄: 60 ID号: 科室: 卫生室 日期: 2 |
| 2 | e0db0650 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HBA1C</td> |
| 3 | 60f1c7ab | 1 | 2-2 | <table><tr><td>葡萄糖</td><td>GL</td><td>9. |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：3
- 页码并集：`[1, 2]`
- 覆盖页数：2 / 2；缺失页：`[]`
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
| LabReport | 检验报告 | 2 | 0 | 2 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "LabReport": 2}`
- ChunkMerger：`{"found": true, "merged": 3, "sources": 9, "stats": {"Extractor:LabExam": 2, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:41:59,861 INFO     29 [ChunkMerger] Merged 3 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:40:58,694 INFO     29 handle_task begin for task {"id": "1d6f130894c111f1bd9827cf206dfa2d", "doc_id": "1d42193494c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SZQI-\u7cd6\u5c3f\u75c5-\u6cb3\u5317.pdf", "type": "pdf", "location": "SZQI-\u7cd6\u5c3f\u75c5-\u6cb3\u5317.pdf", "size": 358625, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369256863, "task_type": "dataflow", "root_trace_id": "46f5ace4ef7a4376b27794db03f19270", "root_traceparent": "00-46f5ace4ef7a4376b27794db03f19270-0a79aaff6c38124a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:40:58,932 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:40:59,048 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:40:59,057 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:40:59,057 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:40:59,057 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:40:59,063 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:40:59,063 INFO     29 ============================================================
2026-08-10 13:40:59,063 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:40:59,063 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:40:59,064 INFO     29 ============================================================
2026-08-10 13:40:59,064 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:40:59,064 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:40:59,066 INFO     29 No torch found.
2026-08-10 13:40:59,320 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=2
2026-08-10 13:40:59,443 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=628804, prompt_len=764
2026-08-10 13:41:01,097 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-09-30"}
```
2026-08-10 13:41:01,097 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2024-09-30
2026-08-10 13:41:01,111 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=628804, prompt_len=401
2026-08-10 13:41:03,144 INFO     29 [qwen-vl-parser] text API response (len=326):
["门诊病历", "姓名:", "性别: 男", "年龄: 60", "ID号:", "科室: 卫生室", "日期: 2024年9月30日", "主 诉 : 近日来体重下降, 尿量增多, 容易饥饿", "既往病史: 无", "检 查 : 指尖血血糖9.5mmol/L", "体温36.5℃", "体态正常", "心率齐72次/分", "双下肢无浮肿", "辅助检查: 糖化血红蛋白(静脉血)9.3%", "血糖(静脉血)9.2mmol/L", "主要诊断: 2型糖尿病", "处 置 : 1, 禁食高糖高油脂食物", "2, 适当增加运动", "3, 继续检测血糖", "4, 门诊随访", "医师签章: 李永利", "日期: 2024年9月30日"]
2026-08-10 13:41:03,144 INFO     29 [qwen-vl-parser] page=1 text: 23 lines (bbox 0-22)
2026-08-10 13:41:03,144 INFO     29 [qwen-vl-parser] page=1 text: 23 sections
2026-08-10 13:41:03,299 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=882570, prompt_len=764
2026-08-10 13:41:04,772 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-26"
}
```
2026-08-10 13:41:04,773 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2025-04-26
2026-08-10 13:41:04,786 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=882570, prompt_len=756
2026-08-10 13:41:12,041 INFO     29 [qwen-vl-parser] table API response (len=1450):
\begin{tabular}{cccccccccc}
\hline
代号 & 项目 & 结果 & 单位 & 参考值 & 代号 & 项目 & 结果 & 单位 & 参考值 \\
\hline
GL & 葡萄糖 & 9.80 & ↑ & mmol/L & 3.9-6.1 & ALP & 碱性磷酸酶 & 85 & U/L & 42-125 \\
BOL & 总胆固醇 & 5.51 & ↑ & mmol/L & 3.1-5.2 & CHE & 胆碱酯酶 & 7958 & U/L & 4600-12000 \\
TC & 甘油三酯 & 1.00 & & mmol/L & 0.56-1.7 & TBA & 总胆汁酸 & 3.6 & μmol/L & 0-15 \\
HDL-C & 高密度脂蛋白胆固醇 & 1.49 & & mmol/L & 1.04-1.55 & PA & 前白蛋白 & 258 & mg/L & 100-400 \\
LDL-C & 低密度脂蛋白胆固醇 & 2.92 & & mmol/L & 2.07-3.37 & 5'-NT & 血清5'核苷酸酶 & 3.00 & U/L & 0-11 \\
4POA1 & 载脂蛋白A1 & 1.56 & & g/L & 1.0-1.6 & UREA & 尿素 & 8.40 & mmol/L & 3.1-9.5 \\
4POB & 载脂蛋白B & 0.96 & & g/L & 0.6-1.1 & CREA & 肌酐（酶法） & 59.4 & μmol/L & 57-111 \\
UPa & 脂蛋白a & 185 & & mg/L & 0-300 & UA & 尿酸 & 237 & μmol/L & 208-428 \\
IBIL & 总胆红素 & 15.7 & & μmol/L & 3.4-20 & CO2 & 二氧化碳 & 26.5 & mmol/L & 20-30 \\
DBIL & 直接胆红素 & 4.5 & & μmol/L & 0-6.84 & CK & 肌酸激酶 & 68 & U/L & 50-310 \\
IBIL & 间接胆红素 & 11.2 & & μmol/L & 1.1-17 & LDH & 乳酸脱氢酶 & 134 & U/L & 120-250 \\
IP & 总蛋白 & 64.7 & ↓ & g/L & 65-85 & HBDH & α-羟丁酸脱氢酶 & 101 & U/L & 72-182 \\
ALB & 白蛋白(溴甲酚绿法) & 42.1 & & g/L & 35-55 & & & & & \\
GLB & 球蛋白 & 22.6 & & g/L & 20-40 & & & & & \\
ALI & 丙氨酸氨基转移酶 & 26 & & U/L & 9-50 & & & & & \\
4ST & 天门冬氨酸氨基转移酶 & 18 & & U/L & 15-40 & & & & & \\
I-GT & γ-谷氨酰基转移酶 & 23 & & U/L & 10-60 & & & & & \\
\hline
\end{tabular}

\begin{tabular}{cccccc}
\hline
项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\
\hline
HBA1C & 糖化血红蛋白 & 9.62 & ↑ & \% & 4-6 \\
\hline
\end{tabular}
2026-08-10 13:41:12,042 INFO     29 [qwen-vl-parser] page=2 table: 32 LaTeX lines (bbox 23-54)
2026-08-10 13:41:12,042 INFO     29 [qwen-vl-parser] page=2 table: 32 sections
2026-08-10 13:41:12,042 INFO     29 [qwen-vl-parser] parse_pdf done: 55 sections from 2 pages.
2026-08-10 13:41:12,050 INFO     29 Close text detector.
2026-08-10 13:41:12,443 INFO     29 Close text recognizer.
2026-08-10 13:41:12,830 INFO     29 Close recognizer.
2026-08-10 13:41:13,234 INFO     29 Close recognizer.
2026-08-10 13:41:13,653 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:41:13,653 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Parser:MedLink | outputs={"html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "json"}
2026-08-10 13:41:13,653 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:41:13,670 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:13,670 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 门诊病历\n[BBOX-1] 姓名:\n[BBOX-2] 性别: 男\n[BBOX-3] 年龄: 60\n[BBOX-4] ID号:\n[BBOX-5] 科室: 卫生室\n[BBOX-6] 日期: 2024年9月30日\n[BBOX-7] 主 诉 : 近日来体重下降, 尿量增多, 容易饥饿\n[BBOX-8] 既往病史: 无\n[BBOX-9] 检 查 : 指尖血血糖9.5mmol/L\n[BBOX-10] 体温36.5℃\n[BBOX-11] 体态正常\n[BBOX-12] 心率齐72次/分\n[BBOX-13] 双下肢无浮肿\n[BBOX-14] 辅助检查: 糖化血红蛋白(静脉血)9.3%\n[BBOX-15] 血糖(静脉血)9.2mmol/L\n[BBOX-16] 主要诊断: 2型糖尿病\n[BBOX-17] 处 置 : 1, 禁食高糖高油脂食物\n[BBOX-18] 2, 适当增加运动\n[BBOX-19] 3, 继续检测血糖\n[BBOX-20] 4, 门诊随访\n[BBOX-21] 医师签章: 李永利\n[BBOX-22] 日期: 2024年9月30日\n[BBOX-23] \\begin{tabular}{cccccccccc}\n[BBOX-24] 报告时间: 2025-04-26\n[BBOX-25] \\hline\n[BBOX-26] 代号 & 项目 & 结果 & 单位 & 参考值 & 代号 & 项目 & 结果 & 单位 & 参考值 \\\\\n[BBOX-27] \\hline\n[BBOX-28] GL & 葡萄糖 & 9.80 & ↑ & mmol/L & 3.9-6.1 & ALP & 碱性磷酸酶 & 85 & U/L & 42-125 \\\\\n[BBOX-29] BOL & 总胆固醇 & 5.51 & ↑ & mmol/L & 3.1-5.2 & CHE & 胆碱酯酶 & 7958 & U/L & 4600-12000 \\\\\n[BBOX-30] TC & 甘油三酯 & 1.00 & & mmol/L & 0.56-1.7 & TBA & 总胆汁酸 & 3.6 & μmol/L & 0-15 \\\\\n[BBOX-31] HDL-C & 高密度脂蛋白胆固醇 & 1.49 & & mmol/L & 1.04-1.55 & PA & 前白蛋白 & 258 & mg/L & 100-400 \\\\\n[BBOX-32] LDL-C & 低密度脂蛋白胆固醇 & 2.92 & & mmol/L & 2.07-3.37 & 5'-NT & 血清5'核苷酸酶 & 3.00 & U/L & 0-11 \\\\\n[BBOX-33] 4POA1 & 载脂蛋白A1 & 1.56 & & g/L & 1.0-1.6 & UREA & 尿素 & 8.40 & mmol/L & 3.1-9.5 \\\\\n[BBOX-34] 4POB & 载脂蛋白B & 0.96 & & g/L & 0.6-1.1 & CREA & 肌酐（酶法） & 59.4 & μmol/L & 57-111 \\\\\n[BBOX-35] UPa & 脂蛋白a & 185 & & mg/L & 0-300 & UA & 尿酸 & 237 & μmol/L & 208-428 \\\\\n[BBOX-36] IBIL & 总胆红素 & 15.7 & & μmol/L & 3.4-20 & CO2 & 二氧化碳 & 26.5 & mmol/L & 20-30 \\\\\n[BBOX-37] DBIL & 直接胆红素 & 4.5 & & μmol/L & 0-6.84 & CK & 肌酸激酶 & 68 & U/L & 50-310 \\\\\n[BBOX-38] IBIL & 间接胆红素 & 11.2 & & μmol/L & 1.1-17 & LDH & 乳酸脱氢酶 & 134 & U/L & 120-250 \\\\\n[BBOX-39] IP & 总蛋白 & 64.7 & ↓ & g/L & 65-85 & HBDH & α-羟丁酸脱氢酶 & 101 & U/L & 72-182 \\\\\n[BBOX-40] ALB & 白蛋白(溴甲酚绿法) & 42.1 & & g/L & 35-55 & & & & & \\\\\n[BBOX-41] GLB & 球蛋白 & 22.6 & & g/L & 20-40 & & & & & \\\\\n[BBOX-42] ALI & 丙氨酸氨基转移酶 & 26 & & U/L & 9-50 & & & & & \\\\\n[BBOX-43] 4ST & 天门冬氨酸氨基转移酶 & 18 & & U/L & 15-40 & & & & & \\\\\n[BBOX-44] I-GT & γ-谷氨酰基转移酶 & 23 & & U/L & 10-60 & & & & & \\\\\n[BBOX-45] \\hline\n[BBOX-46] \\end{tabular}\n[BBOX-47] \\begin{tabular}{cccccc}\n[BBOX-48] 报告时间: 2025-04-26\n[BBOX-49] \\hline\n[BBOX-50] 项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\\\\n[BBOX-51] \\hline\n[BBOX-52] HBA1C & 糖化血红蛋白 & 9.62 & ↑ & \\% & 4-6 \\\\\n[BBOX-53] \\hline\n[BBOX-54] \\end{tabular}"
  }
]
2026-08-10 13:41:16,969 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:16,982 INFO     29 [SmartSplitter] SmartSplitter done: 3 chunks from 3 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'LabReport': 2}
2026-08-10 13:41:16,989 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:41:16,989 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'LabReport': 2}"}
2026-08-10 13:41:16,989 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:41:16,989 INFO     29 [ChunkRouter] Routed 3 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_LabExam': 2}
2026-08-10 13:41:16,997 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:41:16,997 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | ChunkRouter:Router | outputs={"html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'LabReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:16,997 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:41:17,001 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:41:17,002 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:41:17,002 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[1]
2026-08-10 13:41:17,002 INFO     29 [qwen-vl-table] positions ： [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:41:17,150 INFO     29 [qwen-vl-table] page=1, rect=595x842, img=(1654x2339)
2026-08-10 13:41:17,151 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:17,151 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 23, \"bbox_end\": 46, \"encounter_dates\": [\"2025-04-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccccc}\n报告时间: 2025-04-26\n\\hline\n代号 & 项目 & 结果 & 单位 & 参考值 & 代号 & 项目 & 结果 & 单位 & 参考值 \\\\\n\\hline\nGL & 葡萄糖 & 9.80 & ↑ & mmol/L & 3.9-6.1 & ALP & 碱性磷酸酶 & 85 & U/L & 42-125 \\\\\nBOL & 总胆固醇 & 5.51 & ↑ & mmol/L & 3.1-5.2 & CHE & 胆碱酯酶 & 7958 & U/L & 4600-12000 \\\\\nTC & 甘油三酯 & 1.00 & & mmol/L & 0.56-1.7 & TBA & 总胆汁酸 & 3.6 & μmol/L & 0-15 \\\\\nHDL-C & 高密度脂蛋白胆固醇 & 1.49 & & mmol/L & 1.04-1.55 & PA & 前白蛋白 & 258 & mg/L & 100-400 \\\\\nLDL-C & 低密度脂蛋白胆固醇 & 2.92 & & mmol/L & 2.07-3.37 & 5'-NT & 血清5'核苷酸酶 & 3.00 & U/L & 0-11 \\\\\n4POA1 & 载脂蛋白A1 & 1.56 & & g/L & 1.0-1.6 & UREA & 尿素 & 8.40 & mmol/L & 3.1-9.5 \\\\\n4POB & 载脂蛋白B & 0.96 & & g/L & 0.6-1.1 & CREA & 肌酐（酶法） & 59.4 & μmol/L & 57-111 \\\\\nUPa & 脂蛋白a & 185 & & mg/L & 0-300 & UA & 尿酸 & 237 & μmol/L & 208-428 \\\\\nIBIL & 总胆红素 & 15.7 & & μmol/L & 3.4-20 & CO2 & 二氧化碳 & 26.5 & mmol/L & 20-30 \\\\\nDBIL & 直接胆红素 & 4.5 & & μmol/L & 0-6.84 & CK & 肌酸激酶 & 68 & U/L & 50-310 \\\\\nIBIL & 间接胆红素 & 11.2 & & μmol/L & 1.1-17 & LDH & 乳酸脱氢酶 & 134 & U/L & 120-250 \\\\\nIP & 总蛋白 & 64.7 & ↓ & g/L & 65-85 & HBDH & α-羟丁酸脱氢酶 & 101 & U/L & 72-182 \\\\\nALB & 白蛋白(溴甲酚绿法) & 42.1 & & g/L & 35-55 & & & & & \\\\\nGLB & 球蛋白 & 22.6 & & g/L & 20-40 & & & & & \\\\\nALI & 丙氨酸氨基转移酶 & 26 & & U/L & 9-50 & & & & & \\\\\n4ST & 天门冬氨酸氨基转移酶 & 18 & & U/L & 15-40 & & & & & \\\\\nI-GT & γ-谷氨酰基转移酶 & 23 & & U/L & 10-60 & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:41:28,249 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:41:28.248+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 54, "failed": 0, "current": {"1d6f130894c111f1bd9827cf206dfa2d": {"id": "1d6f130894c111f1bd9827cf206dfa2d", "doc_id": "1d42193494c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SZQI-\u7cd6\u5c3f\u75c5-\u6cb3\u5317.pdf", "type": "pdf", "location": "SZQI-\u7cd6\u5c3f\u75c5-\u6cb3\u5317.pdf", "size": 358625, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369256863, "task_type": "dataflow", "root_trace_id": "46f5ace4ef7a4376b27794db03f19270", "root_traceparent": "00-46f5ace4ef7a4376b27794db03f19270-0a79aaff6c38124a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:41:34,159 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:34,159 INFO     29 [qwen-vl-table] page=1 LLM output (len=4885):
{
  "report_date": "2025-04-26",
  "items": [
    {
      "name": "葡萄糖",
      "item_code": "GL",
      "value": "9.80",
      "unit": "mmol/L",
      "reference_range": "3.9-6.1",
      "abnormal": true
    },
    {
      "name": "总胆固醇",
      "item_code": "BOL",
      "value": "5.51",
      "unit": "mmol/L",
      "reference_range": "3.1-5.2",
      "abnormal": true
    },
    {
      "name": "甘油三酯",
      "item_code": "TC",
      "value": "1.00",
      "unit": "mmol/L",
      "reference_range": "0.56-1.7",
      "abnormal": false
    },
    {
      "name": "高密度脂蛋白胆固醇",
      "item_code": "HDL-C",
      "value": "1.49",
      "unit": "mmol/L",
      "reference_range": "1.04-1.55",
      "abnormal": false
    },
    {
      "name": "低密度脂蛋白胆固醇",
      "item_code": "LDL-C",
      "value": "2.92",
      "unit": "mmol/L",
      "reference_range": "2.07-3.37",
      "abnormal": false
    },
    {
      "name": "载脂蛋白A1",
      "item_code": "4POA1",
      "value": "1.56",
      "unit": "g/L",
      "reference_range": "1.0-1.6",
      "abnormal": false
    },
    {
      "name": "载脂蛋白B",
      "item_code": "4POB",
      "value": "0.96",
      "unit": "g/L",
      "reference_range": "0.6-1.1",
      "abnormal": false
    },
    {
      "name": "脂蛋白a",
      "item_code": "UPa",
      "value": "185",
      "unit": "mg/L",
      "reference_range": "0-300",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "IBIL",
      "value": "15.7",
      "unit": "μmol/L",
      "reference_range": "3.4-20",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "4.5",
      "unit": "μmol/L",
      "reference_range": "0-6.84",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "11.2",
      "unit": "μmol/L",
      "reference_range": "1.1-17",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": "IP",
      "value": "64.7",
      "unit": "g/L",
      "reference_range": "65-85",
      "abnormal": true
    },
    {
      "name": "白蛋白(溴甲酚绿法)",
      "item_code": "ALB",
      "value": "42.1",
      "unit": "g/L",
      "reference_range": "35-55",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLB",
      "value": "22.6",
      "unit": "g/L",
      "reference_range": "20-40",
      "abnormal": false
    },
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": "ALI",
      "value": "26",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": "4ST",
      "value": "18",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "γ-谷氨酰基转移酶",
      "item_code": "I-GT",
      "value": "23",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "85",
      "unit": "U/L",
      "reference_range": "42-125",
      "abnormal": false
    },
    {
      "name": "胆碱酯酶",
      "item_code": "CHE",
      "value": "7958",
      "unit": "U/L",
      "reference_range": "4600-12000",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": "TBA",
      "value": "3.6",
      "unit": "μmol/L",
      "reference_range": "0-15",
      "abnormal": false
    },
    {
      "name": "前白蛋白",
      "item_code": "PA",
      "value": "258",
      "unit": "mg/L",
      "reference_range": "100-400",
      "abnormal": false
    },
    {
      "name": "血清5'核苷酸酶",
      "item_code": "5'-NT",
      "value": "3.00",
      "unit": "U/L",
      "reference_range": "0-11",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "8.40",
      "unit": "mmol/L",
      "reference_range": "3.1-9.5",
      "abnormal": false
    },
    {
      "name": "肌酐（酶法）",
      "item_code": "CREA",
      "value": "59.4",
      "unit": "μmol/L",
      "reference_range": "57-111",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "UA",
      "value": "237",
      "unit": "μmol/L",
      "reference_range": "208-428",
      "abnormal": false
    },
    {
      "name": "二氧化碳",
      "item_code": "CO2",
      "value": "26.5",
      "unit": "mmol/L",
      "reference_range": "20-30",
      "abnormal": false
    },
    {
      "name": "肌酸激酶",
      "item_code": "CK",
      "value": "68",
      "unit": "U/L",
      "reference_range": "50-310",
      "abnormal": false
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": "LDH",
      "value": "134",
      "unit": "U/L",
      "reference_range": "120-250",
      "abnormal": false
    },
    {
      "name": "α-羟丁酸脱氢酶",
      "item_code": "HBDH",
      "value": "101",
      "unit": "U/L",
      "reference_range": "72-182",
      "abnormal": false
    }
  ]
}
2026-08-10 13:41:34,159 INFO     29 [qwen-vl-table] coord grouping: {1: 29}
2026-08-10 13:41:34,162 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1179511, prompt_len=692
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
葡萄糖、总胆固醇、甘油三酯、高密度脂蛋白胆固醇、低密度脂蛋白胆固醇、载脂蛋白A1、载脂蛋白B、脂蛋白a、总胆红素、直接胆红素、间接胆红素、总蛋白、白蛋白(溴甲酚绿法)、球蛋白、丙氨酸氨基转移酶、天门冬氨酸氨基转移酶、γ-谷氨酰基转移酶、碱性磷酸酶、胆碱酯酶、总胆汁酸、前白蛋白、血清5'核苷酸酶、尿素、肌酐（酶法）、尿酸、二氧化碳、肌酸激酶、乳酸脱氢酶、α-羟丁酸脱氢酶

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
2026-08-10 13:41:42,412 INFO     29 [qwen-vl-table] coord API raw response (len=1464):
[
	{"text": "葡萄糖", "bbox": [295, 170, 321, 177]},
	{"text": "总胆固醇", "bbox": [295, 180, 329, 187]},
	{"text": "甘油三酯", "bbox": [295, 190, 329, 197]},
	{"text": "高密度脂蛋白胆固醇", "bbox": [295, 199, 374, 206]},
	{"text": "低密度脂蛋白胆固醇", "bbox": [295, 209, 374, 216]},
	{"text": "载脂蛋白A1", "bbox": [295, 220, 336, 227]},
	{"text": "载脂蛋白B", "bbox": [295, 230, 333, 237]},
	{"text": "脂蛋白a", "bbox": [295, 240, 323, 247]},
	{"text": "总胆红素", "bbox": [295, 251, 327, 258]},
	{"text": "直接胆红素", "bbox": [295, 262, 336, 269]},
	{"text": "间接胆红素", "bbox": [295, 272, 336, 279]},
	{"text": "总蛋白", "bbox": [295, 283, 316, 290]},
	{"text": "白蛋白(溴甲酚绿法)", "bbox": [295, 293, 370, 300]},
	{"text": "球蛋白", "bbox": [295, 304, 314, 311]},
	{"text": "丙氨酸氨基转移酶", "bbox": [295, 315, 361, 322]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [295, 326, 379, 333]},
	{"text": "γ-谷氨酰基转移酶", "bbox": [295, 337, 366, 344]},
	{"text": "碱性磷酸酶", "bbox": [566, 159, 615, 166]},
	{"text": "胆碱酯酶", "bbox": [566, 169, 606, 176]},
	{"text": "总胆汁酸", "bbox": [566, 179, 606, 186]},
	{"text": "前白蛋白", "bbox": [566, 189, 606, 196]},
	{"text": "血清5'核苷酸酶", "bbox": [566, 199, 643, 206]},
	{"text": "尿素", "bbox": [566, 209, 587, 216]},
	{"text": "肌酐（酶法）", "bbox": [566, 219, 623, 226]},
	{"text": "尿酸", "bbox": [566, 229, 587, 236]},
	{"text": "二氧化碳", "bbox": [566, 239, 608, 246]},
	{"text": "肌酸激酶", "bbox": [566, 249, 608, 256]},
	{"text": "乳酸脱氢酶", "bbox": [566, 259, 620, 266]},
	{"text": "α-羟丁酸脱氢酶", "bbox": [566, 269, 648, 276]}
]
2026-08-10 13:41:42,412 INFO     29 [qwen-vl-table] coord API: raw_items=29, valid_items=29, elapsed=8.2s
2026-08-10 13:41:42,412 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖, bbox=[295, 170, 321, 177]
2026-08-10 13:41:42,412 INFO     29 [qwen-vl-table] coord item[1]: text=总胆固醇, bbox=[295, 180, 329, 187]
2026-08-10 13:41:42,412 INFO     29 [qwen-vl-table] coord item[2]: text=甘油三酯, bbox=[295, 190, 329, 197]
2026-08-10 13:41:42,412 INFO     29 [qwen-vl-table] coord item[3]: text=高密度脂蛋白胆固醇, bbox=[295, 199, 374, 206]
2026-08-10 13:41:42,412 INFO     29 [qwen-vl-table] coord item[4]: text=低密度脂蛋白胆固醇, bbox=[295, 209, 374, 216]
2026-08-10 13:41:42,412 INFO     29 [qwen-vl-table] coord item[5]: text=载脂蛋白A1, bbox=[295, 220, 336, 227]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[6]: text=载脂蛋白B, bbox=[295, 230, 333, 237]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[7]: text=脂蛋白a, bbox=[295, 240, 323, 247]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[8]: text=总胆红素, bbox=[295, 251, 327, 258]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[9]: text=直接胆红素, bbox=[295, 262, 336, 269]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[10]: text=间接胆红素, bbox=[295, 272, 336, 279]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[11]: text=总蛋白, bbox=[295, 283, 316, 290]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[12]: text=白蛋白(溴甲酚绿法), bbox=[295, 293, 370, 300]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[13]: text=球蛋白, bbox=[295, 304, 314, 311]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[14]: text=丙氨酸氨基转移酶, bbox=[295, 315, 361, 322]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[15]: text=天门冬氨酸氨基转移酶, bbox=[295, 326, 379, 333]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[16]: text=γ-谷氨酰基转移酶, bbox=[295, 337, 366, 344]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[17]: text=碱性磷酸酶, bbox=[566, 159, 615, 166]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[18]: text=胆碱酯酶, bbox=[566, 169, 606, 176]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[19]: text=总胆汁酸, bbox=[566, 179, 606, 186]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[20]: text=前白蛋白, bbox=[566, 189, 606, 196]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[21]: text=血清5'核苷酸酶, bbox=[566, 199, 643, 206]
2026-08-10 13:41:42,413 INFO     29 [qwen-vl-table] coord item[22]: text=尿素, bbox=[566, 209, 587, 216]
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] coord item[23]: text=肌酐（酶法）, bbox=[566, 219, 623, 226]
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] coord item[24]: text=尿酸, bbox=[566, 229, 587, 236]
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] coord item[25]: text=二氧化碳, bbox=[566, 239, 608, 246]
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] coord item[26]: text=肌酸激酶, bbox=[566, 249, 608, 256]
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] coord item[27]: text=乳酸脱氢酶, bbox=[566, 259, 620, 266]
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] coord item[28]: text=α-羟丁酸脱氢酶, bbox=[566, 269, 648, 276]
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] page=1 coord: matched 29/29, time=8.2s
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] new_positions (29):
[[2, 175.61349639892578, 191.09129608154296, 143.12300415039064, 149.01630432128906], [2, 175.61349639892578, 195.85369598388672, 151.54200439453126, 157.4353045654297], [2, 175.61349639892578, 195.85369598388672, 159.96100463867188, 165.85430480957032], [2, 175.61349639892578, 222.6421954345703, 167.53810485839844, 173.43140502929688], [2, 175.61349639892578, 222.6421954345703, 175.95710510253906, 181.8504052734375], [2, 175.61349639892578, 200.0207958984375, 185.21800537109377, 191.11130554199218], [2, 175.61349639892578, 198.2348959350586, 193.6370056152344, 199.53030578613283], [2, 175.61349639892578, 192.2818960571289, 202.056005859375, 207.94930603027345], [2, 175.61349639892578, 194.66309600830078, 211.31690612792968, 217.21020629882813], [2, 175.61349639892578, 200.0207958984375, 220.5778063964844, 226.47110656738283], [2, 175.61349639892578, 200.0207958984375, 228.996806640625, 234.89010681152345], [2, 175.61349639892578, 188.11479614257814, 238.2577069091797, 244.15100708007813], [2, 175.61349639892578, 220.26099548339846, 246.6767071533203, 252.57000732421875], [2, 175.61349639892578, 186.9241961669922, 255.93760742187501, 261.8309075927734], [2, 175.61349639892578, 214.90329559326173, 265.1985076904297, 271.0918078613281], [2, 175.61349639892578, 225.61869537353516, 274.4594079589844, 280.35270812988284], [2, 175.61349639892578, 217.87979553222658, 283.7203082275391, 289.6136083984375], [2, 336.93979309082033, 366.10949249267577, 133.86210388183594, 139.75540405273438], [2, 336.93979309082033, 360.75179260253907, 142.28110412597655, 148.174404296875], [2, 336.93979309082033, 360.75179260253907, 150.7001043701172, 156.59340454101564], [2, 336.93979309082033, 360.75179260253907, 159.11910461425782, 165.01240478515626], [2, 336.93979309082033, 382.7778921508789, 167.53810485839844, 173.43140502929688], [2, 336.93979309082033, 349.44109283447267, 175.95710510253906, 181.8504052734375], [2, 336.93979309082033, 370.87189239501953, 184.3761053466797, 190.26940551757812], [2, 336.93979309082033, 349.44109283447267, 192.79510559082033, 198.68840576171877], [2, 336.93979309082033, 361.942392578125, 201.21410583496095, 207.1074060058594], [2, 336.93979309082033, 361.942392578125, 209.63310607910157, 215.52640625], [2, 336.93979309082033, 369.08599243164065, 218.05210632324219, 223.94540649414063], [2, 336.93979309082033, 385.75439208984375, 226.47110656738283, 232.36440673828125]]
2026-08-10 13:41:42,414 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=29, matched=29, pages=1, time=25.4s
2026-08-10 13:41:42,415 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:41:42,416 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:41:42,417 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[1]
2026-08-10 13:41:42,417 INFO     29 [qwen-vl-table] positions ： [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:41:42,565 INFO     29 [qwen-vl-table] page=1, rect=595x842, img=(1654x2339)
2026-08-10 13:41:42,565 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:42,566 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 47, \"bbox_end\": 54, \"encounter_dates\": [\"2025-04-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2025-04-26\n\\hline\n项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\\\\n\\hline\nHBA1C & 糖化血红蛋白 & 9.62 & ↑ & \\% & 4-6 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:41:44,148 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:44,148 INFO     29 [qwen-vl-table] page=1 LLM output (len=212):
{
  "report_date": "2025-04-26",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HBA1C",
      "value": "9.62",
      "unit": "%",
      "reference_range": "4-6",
      "abnormal": true
    }
  ]
}
2026-08-10 13:41:44,148 INFO     29 [qwen-vl-table] coord grouping: {1: 1}
2026-08-10 13:41:44,150 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1179511, prompt_len=513
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
2026-08-10 13:41:44,835 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [333, 489, 386, 498]}
]
```
2026-08-10 13:41:44,836 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 13:41:44,836 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[333, 489, 386, 498]
2026-08-10 13:41:44,836 INFO     29 [qwen-vl-table] page=1 coord: matched 1/1, time=0.7s
2026-08-10 13:41:44,836 INFO     29 [qwen-vl-table] new_positions (1):
[[2, 198.2348959350586, 229.78579528808595, 411.6891119384766, 419.26621215820313]]
2026-08-10 13:41:44,837 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.4s
2026-08-10 13:41:44,846 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:41:44,846 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:LabExam | outputs={"chunks": "2 items, types={'LabReport': 2}", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:44,846 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:41:44,850 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:44,850 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:41:45,246 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:45,250 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:41:45,250 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:45,250 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:41:45,254 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:41:45,256 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:41:45,256 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:41:45,256 INFO     29 [qwen-vl-text] positions(23): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:41:45,256 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [23]
2026-08-10 13:41:45,372 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 13:41:45,373 INFO     29 [qwen-vl-text] LLM extraction start, text_len=256
2026-08-10 13:41:45,373 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:45,373 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 22, \"encounter_dates\": [\"2024-09-30\"], \"department\": \"卫生室\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n姓名:\n性别: 男\n年龄: 60\nID号:\n科室: 卫生室\n日期: 2024年9月30日\n主 诉 : 近日来体重下降, 尿量增多, 容易饥饿\n既往病史: 无\n检 查 : 指尖血血糖9.5mmol/L\n体温36.5℃\n体态正常\n心率齐72次/分\n双下肢无浮肿\n辅助检查: 糖化血红蛋白(静脉血)9.3%\n血糖(静脉血)9.2mmol/L\n主要诊断: 2型糖尿病\n处 置 : 1, 禁食高糖高油脂食物\n2, 适当增加运动\n3, 继续检测血糖\n4, 门诊随访\n医师签章: 李永利\n日期: 2024年9月30日",
    "role": "user"
  }
]
2026-08-10 13:41:46,766 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:46,766 INFO     29 [qwen-vl-text] LLM output (len=221):
{
  "encounter_date": "2024-09-30",
  "chief_complaint": "近日来体重下降, 尿量增多, 容易饥饿",
  "present_illness": null,
  "past_history": "无",
  "diagnosis": "2型糖尿病",
  "treatment_plan": "1, 禁食高糖高油脂食物\n2, 适当增加运动\n3, 继续检测血糖\n4, 门诊随访"
}
2026-08-10 13:41:46,766 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-09-30]
2026-08-10 13:41:46,768 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=923209, prompt_len=938
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["门诊病历", "姓名:", "性别: 男", "年龄: 60", "ID号:", "科室: 卫生室", "日期: 2024年9月30日", "主 诉 : 近日来体重下降, 尿量增多, 容易饥饿", "既往病史: 无", "检 查 : 指尖血血糖9.5mmol/L", "体温36.5℃", "体态正常", "心率齐72次/分", "双下肢无浮肿", "辅助检查: 糖化血红蛋白(静脉血)9.3%", "血糖(静脉血)9.2mmol/L", "主要诊断: 2型糖尿病", "处 置 : 1, 禁食高糖高油脂食物", "2, 适当增加运动", "3, 继续检测血糖", "4, 门诊随访", "医师签章: 李永利", "日期: 2024年9月30日"]

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
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord API raw response (len=1271):
[
	{"text": "门诊病历", "bbox": [423, 185, 530, 209]},
	{"text": "姓名:", "bbox": [163, 219, 206, 234]},
	{"text": "性别: 男", "bbox": [374, 225, 453, 241]},
	{"text": "年龄: 60", "bbox": [578, 232, 647, 246]},
	{"text": "ID号:", "bbox": [163, 247, 207, 261]},
	{"text": "科室: 卫生室", "bbox": [376, 252, 490, 269]},
	{"text": "日期: 2024年9月30日", "bbox": [573, 257, 759, 275]},
	{"text": "主 诉 : 近日来体重下降, 尿量增多, 容易饥饿", "bbox": [163, 274, 545, 297]},
	{"text": "既往病史: 无", "bbox": [162, 329, 269, 345]},
	{"text": "检 查 : 指尖血血糖9.5mmol/L", "bbox": [160, 384, 420, 402]},
	{"text": "体温36.5℃", "bbox": [461, 389, 546, 403]},
	{"text": "体态正常", "bbox": [597, 391, 665, 404]},
	{"text": "心率齐72次/分", "bbox": [250, 413, 370, 428]},
	{"text": "双下肢无浮肿", "bbox": [447, 416, 550, 430]},
	{"text": "辅助检查: 糖化血红蛋白(静脉血)9.3%", "bbox": [160, 467, 476, 483]},
	{"text": "血糖(静脉血)9.2mmol/L", "bbox": [534, 470, 728, 485]},
	{"text": "主要诊断: 2型糖尿病", "bbox": [160, 521, 333, 535]},
	{"text": "处 置 : 1, 禁食高糖高油脂食物", "bbox": [160, 575, 431, 590]},
	{"text": "2, 适当增加运动", "bbox": [247, 604, 379, 618]},
	{"text": "3, 继续检测血糖", "bbox": [247, 631, 379, 645]},
	{"text": "4, 门诊随访", "bbox": [246, 659, 344, 672]},
	{"text": "医师签章: 李永利", "bbox": [566, 743, 707, 758]},
	{"text": "日期: 2024年9月30日", "bbox": [567, 772, 755, 787]}
]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=8.9s
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[423, 185, 530, 209]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[1]: text=姓名:, bbox=[163, 219, 206, 234]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[2]: text=性别: 男, bbox=[374, 225, 453, 241]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[3]: text=年龄: 60, bbox=[578, 232, 647, 246]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[4]: text=ID号:, bbox=[163, 247, 207, 261]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[5]: text=科室: 卫生室, bbox=[376, 252, 490, 269]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[6]: text=日期: 2024年9月30日, bbox=[573, 257, 759, 275]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[7]: text=主 诉 : 近日来体重下降, 尿量增多, 容易饥饿, bbox=[163, 274, 545, 297]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[8]: text=既往病史: 无, bbox=[162, 329, 269, 345]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[9]: text=检 查 : 指尖血血糖9.5mmol/L, bbox=[160, 384, 420, 402]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[10]: text=体温36.5℃, bbox=[461, 389, 546, 403]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[11]: text=体态正常, bbox=[597, 391, 665, 404]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[12]: text=心率齐72次/分, bbox=[250, 413, 370, 428]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[13]: text=双下肢无浮肿, bbox=[447, 416, 550, 430]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[14]: text=辅助检查: 糖化血红蛋白(静脉血)9.3%, bbox=[160, 467, 476, 483]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[15]: text=血糖(静脉血)9.2mmol/L, bbox=[534, 470, 728, 485]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[16]: text=主要诊断: 2型糖尿病, bbox=[160, 521, 333, 535]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[17]: text=处 置 : 1, 禁食高糖高油脂食物, bbox=[160, 575, 431, 590]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[18]: text=2, 适当增加运动, bbox=[247, 604, 379, 618]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[19]: text=3, 继续检测血糖, bbox=[247, 631, 379, 645]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[20]: text=4, 门诊随访, bbox=[246, 659, 344, 672]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[21]: text=医师签章: 李永利, bbox=[566, 743, 707, 758]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] coord item[22]: text=日期: 2024年9月30日, bbox=[567, 772, 755, 787]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] page=0 — 23/23 coords, api_time=8.9s
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] new_positions (23):
[[0, 251.81189483642578, 315.5089935302735, 155.75150451660156, 175.95710510253906], [0, 97.0338980102539, 122.63179748535157, 184.3761053466797, 197.00460571289062], [0, 222.6421954345703, 269.6708944702149, 189.42750549316406, 202.89790588378906], [0, 344.08339294433597, 385.1590921020508, 195.3208056640625, 207.1074060058594], [0, 97.0338980102539, 123.22709747314454, 207.94930603027345, 219.73590637207033], [0, 223.83279541015625, 291.6969940185547, 212.15880615234377, 226.47110656738283], [0, 341.1068930053711, 451.8326907348633, 216.36830627441407, 231.5225067138672], [0, 97.0338980102539, 324.438493347168, 230.68060668945313, 250.04430725097657], [0, 96.43859802246094, 160.1356967163086, 276.98510803222655, 290.45550842285155], [0, 95.24799804687501, 250.0259948730469, 323.289609375, 338.4438098144531], [0, 274.4332943725586, 325.03379333496093, 327.4991094970703, 339.2857098388672], [0, 355.39409271240237, 395.87449188232426, 329.18290954589844, 340.12760986328124], [0, 148.8249969482422, 220.26099548339846, 347.70471008300785, 360.33321044921877], [0, 266.09909454345706, 327.4149932861328, 350.23041015625, 362.0170104980469], [0, 95.24799804687501, 283.36279418945315, 393.1673114013672, 406.6377117919922], [0, 317.89019348144535, 433.3783911132813, 395.69301147460936, 408.32151184082034], [0, 95.24799804687501, 198.2348959350586, 438.6299127197266, 450.41651306152346], [0, 95.24799804687501, 256.57429473876954, 484.09251403808594, 496.7210144042969], [0, 147.03909698486328, 225.61869537353516, 508.5076147460938, 520.2942150878906], [0, 147.03909698486328, 225.61869537353516, 531.2389154052735, 543.0255157470704], [0, 146.4437969970703, 204.78319580078127, 554.8121160888672, 565.75681640625], [0, 336.93979309082033, 420.87709136962894, 625.5317181396484, 638.1602185058593], [0, 337.5350930786133, 449.45149078369144, 649.9468188476562, 662.5753192138673]]
2026-08-10 13:41:55,661 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=10.4s
2026-08-10 13:41:55,674 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:41:55,674 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:55,675 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:41:55,680 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:55,681 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:41:56,796 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:56,807 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:41:56,808 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:56,808 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:41:56,815 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:56,815 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:41:57,278 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:57,290 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:41:57,290 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:57,290 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:41:57,300 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:57,300 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:41:57,740 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:57,751 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:41:57,751 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:57,751 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:41:57,759 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:57,759 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:41:58,238 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:58,243 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:41:58,244 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:58,244 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:41:58,248 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:58,249 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:41:59,341 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:59,351 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:41:59,351 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:59,351 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:41:59,360 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:59,360 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:41:59,793 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:41:59.790+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 54, "failed": 0, "current": {"1d6f130894c111f1bd9827cf206dfa2d": {"id": "1d6f130894c111f1bd9827cf206dfa2d", "doc_id": "1d42193494c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SZQI-\u7cd6\u5c3f\u75c5-\u6cb3\u5317.pdf", "type": "pdf", "location": "SZQI-\u7cd6\u5c3f\u75c5-\u6cb3\u5317.pdf", "size": 358625, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369256863, "task_type": "dataflow", "root_trace_id": "46f5ace4ef7a4376b27794db03f19270", "root_traceparent": "00-46f5ace4ef7a4376b27794db03f19270-0a79aaff6c38124a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:41:59,853 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:41:59,861 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:41:59,861 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "55 items", "markdown": "", "text": "", "name": "SZQI-糖尿病-河北.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-10 13:41:59,861 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:41:59,861 INFO     29 [ChunkMerger] Merged 3 chunks from 9 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:41:59,870 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:41:59,870 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "3 items, types={'LabReport': 2, 'OutpatientRecord': 1}", "name": "SZQI-糖尿病-河北.pdf"}
2026-08-10 13:41:59,870 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:41:59,906 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786369258927, 'update_date': datetime.datetime(2026, 8, 10, 13, 40, 58), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1046625, 'status': '1'}
2026-08-10 13:42:00,368 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   葡萄糖  GL  9.80  mmol/L  3.9-6.1  True    总胆固醇  BOL  5.51  mmol/L  3.1-5.2  True    甘油三酯  TC  1.00  mmol/L  0.56-1.7  False    高密度脂蛋白胆固醇  HDL-C  1.49  mmol/L  1.04-1.55  False    低密度脂蛋白胆固醇  LDL-C  2.92  mmol/L  2.07-3.37  False    载脂蛋白A1  4POA1  1.56  g/L  1.0-1.6  False    载脂蛋白B  4POB  0.96  g/L  0.6-1.1  False    脂蛋白a  UPa  185  mg/L  0-300  False    总胆红素  IBIL  15.7  μmol/L  3.4-20  False    直接胆红素  DBIL  4.5  μmol/L  0-6.84  False    间接胆红素  IBIL  11.2  μmol/L  1.1-17  False    总蛋白  IP  64.7  g/L  65-85  True    白蛋白(溴甲酚绿法)  ALB  42.1  g/L  35-55  False    球蛋白  GLB  22.6  g/L  20-40  False    丙氨酸氨基转移酶  ALI  26  U/L  9-50  False    天门冬氨酸氨基转移酶  4ST  18  U/L  15-40  False    γ-谷氨酰基转移酶  I-GT  23  U/L  10-60  False    碱性磷酸酶  ALP  85  U/L  42-125  False    胆碱酯酶  CHE  7958  U/L  4600-12000  False    总胆汁酸  TBA  3.6  μmol/L  0-15  False    前白蛋白  PA  258  mg/L  100-400  False    血清5'核苷酸酶  5'-NT  3.00  U/L  0-11  False    尿素  UREA  8.40  mmol/L  3.1-9.5  False    肌酐（酶法）  CREA  59.4  μmol/L  57-111  False    尿酸  UA  237  μmol/L  208-428  False    二氧化碳  CO2  26.5  mmol/L  20-30  False    肌酸激酶  CK  68  U/L  50-310  False    乳酸脱氢酶  LDH  134  U/L  120-250  False    α-羟丁酸脱氢酶  HBDH  101  U/L  72-182  False   
---
   糖化血红蛋白  HBA1C  9.62  %  4-6  True   
---
门诊病历
姓名:
性别: 男
年龄: 60
ID号:
科室: 卫生室
日期: 2024年9月30日
主 诉 : 近日来体重下降, 尿量增多, 容易饥饿
既往病史: 无
检 查 : 指尖血血糖9.5mmol/L
体温36.5℃
体态正常
心率齐72次/分
双下肢无浮肿
辅助检查: 糖化血红蛋白(静脉血)9.3%
血糖(静脉血)9.2mmol/L
主要诊断: 2型糖尿病
处 置 : 1, 禁食高糖高油脂食物
2, 适当增加运动
3, 继续检测血糖
4, 门诊随访
医师签章: 李永利
日期: 2024年9月30日
2026-08-10 13:42:00,617 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:42:00,617 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "3 items, types={'LabReport': 2, 'OutpatientRecord': 1}", "name": "SZQI-糖尿病-河北.pdf", "embedding_token_consumption": 1093}
2026-08-10 13:42:00,617 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:42:00,951 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:42:00,951 INFO     29 [Trace] task=1d6f1308 | doc=SZQI-糖尿病-河北.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":3,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:42:00,953 INFO     29 [DIAG-EXECUTOR] row_position_int len=29 row[0]=(2, 175, 191, 143, 149) row[-1]=(2, 336, 385, 226, 232)
2026-08-10 13:42:00,953 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(2, 198, 229, 411, 419) row[-1]=(2, 198, 229, 411, 419)
2026-08-10 13:42:00,953 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:42:00,957 INFO     29 set_progress(1d6f130894c111f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:42:00 [DOC Engine]:
Start to index...
2026-08-10 13:42:00,970 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 13:42:00,973 INFO     29 set_progress(1d6f130894c111f1bd9827cf206dfa2d), progress: 0.8333333333333334, progress_msg: 
2026-08-10 13:42:00,979 INFO     29 set_progress(1d6f130894c111f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:42:00 Indexing done (0.02s). Task done (58.99s)
2026-08-10 13:42:00,982 INFO     29 [Done], chunks(3), token(1093), elapsed:58.99
2026-08-10 13:42:01,038 INFO     29 handle_task done for task {"id": "1d6f130894c111f1bd9827cf206dfa2d", "doc_id": "1d42193494c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SZQI-\u7cd6\u5c3f\u75c5-\u6cb3\u5317.pdf", "type": "pdf", "location": "SZQI-\u7cd6\u5c3f\u75c5-\u6cb3\u5317.pdf", "size": 358625, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786369256863, "task_type": "dataflow", "root_trace_id": "46f5ace4ef7a4376b27794db03f19270", "root_traceparent": "00-46f5ace4ef7a4376b27794db03f19270-0a79aaff6c38124a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
