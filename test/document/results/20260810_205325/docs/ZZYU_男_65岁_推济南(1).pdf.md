# 基准结果：ZZYU 男 65岁 推济南(1).pdf

## 基本信息

- 文件：`ZZYU 男 65岁 推济南(1).pdf`
- 大小：739.0 KB
- PDF 总页数：2
- doc_id：`e9284be494bd11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:17:59  完成时间：2026-08-10T21:19:27  耗时：87.9s
- progress_msg：`13:19:25 Indexing done (0.02s). Task done (77.50s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 1a72d813 | 1 | 1-1 | 邹城市人民医院 门诊病历 性别：男性 年龄：65岁 科室：呼吸与危重症医学科(千 |
| 2 | 893a36d0 | 2 | 1-2 | 708833003930 邹城市人民医院 肺功能检查报告单 姓名 温度：28℃  |

- chunks 总数：2
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
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "ExaminationReport": 1}`
- ChunkMerger：`{"found": true, "merged": 2, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:19:25,050 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:18:03,602 INFO     29 handle_task begin for task {"id": "e97265da94bd11f1bd9827cf206dfa2d", "doc_id": "e9284be494bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZZYU \u7537 65\u5c81 \u63a8\u6d4e\u5357(1).pdf", "type": "pdf", "location": "ZZYU \u7537 65\u5c81 \u63a8\u6d4e\u5357(1).pdf", "size": 756692, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367881156, "task_type": "dataflow", "root_trace_id": "7b4a5c76667c474a9c93698057034643", "root_traceparent": "00-7b4a5c76667c474a9c93698057034643-1740e57c2225b187-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:18:03,909 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:18:04,017 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:18:04,026 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:18:04,026 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:18:04,026 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:18:04,070 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:18:04,070 INFO     29 ============================================================
2026-08-10 13:18:04,070 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:18:04,070 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:18:04,070 INFO     29 ============================================================
2026-08-10 13:18:04,070 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:18:04,070 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:18:04,073 INFO     29 No torch found.
2026-08-10 13:18:04,482 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=2
2026-08-10 13:18:04,654 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=900248, prompt_len=764
2026-08-10 13:18:06,000 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:18:06,001 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:18:06,015 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=900248, prompt_len=401
2026-08-10 13:18:08,989 INFO     29 [qwen-vl-parser] text API response (len=510):
["邹城市人民医院", "门诊病历", "性别：男性", "年龄：65岁", "科室：呼吸与危重症医学科(千泉门诊)", "ID号", "就诊时间：2025-05-29 10:06", "主诉：阵发性憋喘60年。", "现病史：阵发性憋喘60年，遇冷空气时加重，时咳嗽、咳少量白痰，时有", "心慌、胸闷、气短，无胸痛，无恶心、呕吐，无腹痛、无腹泻，在院外未治疗，", "症状时好时坏，来诊。", "既往史：平素身体健康，否认高血压、冠心病、糖尿病史。否认病毒性肝", "炎、肺结核等传染病史及密切接触史。", "过敏史：否认药物过敏史。", "体格检查：神志清、精神可，胸廓无畸形，双肺呼吸音清，未闻及干湿", "啰音，心率75次/分，心律齐，无杂音，双下肢无水肿。", "辅助检查：", "诊断：喘憋（主诊断）", "诊疗意见：", "避免受凉感冒，避免过度劳累，如有不适，及时就诊。", "☑已向患者(家属)进行了关于患者病情、目前状况及诊疗方案的教育。", "☑已向患者(家属)交代了各种诊疗方案的效果和不遵从医嘱可能导致的后果。", "医生签名：", "门诊部", "(1)", "708833003930"]
2026-08-10 13:18:08,990 INFO     29 [qwen-vl-parser] page=1 text: 26 lines (bbox 0-25)
2026-08-10 13:18:08,990 INFO     29 [qwen-vl-parser] page=1 text: 26 sections
2026-08-10 13:18:09,129 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=555365, prompt_len=764
2026-08-10 13:18:10,480 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-05-29"
}
```
2026-08-10 13:18:10,480 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2025-05-29
2026-08-10 13:18:10,487 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=555365, prompt_len=401
2026-08-10 13:18:18,214 INFO     29 [qwen-vl-parser] text API response (len=1289):
["邹城市人民医院", "肺功能检查报告单", "姓名", "温度：28℃", "住院号：", "性别：男", "气压：745mmHg", "科室：呼吸与危重症医学科门", "年龄：65岁", "检查日期：05/29/25", "床位号：", "吸烟：无", "肺容积：", "(BTPS)", "用药前", "用药后", "预计值：", "实测值", "实/预%", "实测值", "实/预%改善率", "肺活量：", "VC", "L", "3.56", "潮气量：", "Vt", "L", "深吸气量：", "IC", "L", "补呼气量：", "ERV", "L", "残气：", "RV Sb", "L", "2.19", "功能残气量：", "FRC N2", "L", "3.39", "肺总量：", "TLC Sb", "L", "5.65", "残气/肺总量：", "RV/TLC Sb", "%", "39", "通气功能：", "用力肺活量：", "FVC", "L", "3.56", "2.90", "81", "3.24", "91", "12", "用力呼气一秒量：", "FEV1", "L", "2.77", "1.45", "52", "1.65", "60", "14", "用力呼气一秒率：", "FEV1/FVC", "%", "80", "50", "63", "51", "64", "2", "用力呼气中期流速：", "FEF25-75%L/sec", "2.85", "0.70", "25", "0.76", "27", "8", "25%用力呼气流速：", "FEF25%", "L/sec", "6.85", "1.58", "23", "2.00", "29", "27", "50%用力呼气流速：", "FEF50%", "L/sec", "3.57", "0.82", "23", "0.91", "25", "11", "75%用力呼气流速：", "FEF75%", "L/sec", "1.23", "0.34", "28", "0.39", "32", "13", "峰值流速", "PEF", "L/sec", "7.51", "2.72", "36", "2.71", "36", "-0", "每分静息通气量：", "VE", "L/min", "6.8", "最大自主通气量：", "MVV", "L/min", "121", "弥散功能", "CO弥散量：", "DLCO", "mL/mmHg/min8.3", "DLCOexh", "mL/mmHg/min8.3", "VA", "L", "VA exh", "L", "肺泡容积：", "DLCO/VA", "mL/mmHg/mi8.68", "弥散常数：", "DLexh/VA", "mL/mmHg/mi8.68", "结论：", "中重度阻塞性肺通气功能障碍。", "支气管舒张试验阳性。", "此报告仅供临床参考", "检查者："]
2026-08-10 13:18:18,214 INFO     29 [qwen-vl-parser] page=2 text: 151 lines (bbox 26-176)
2026-08-10 13:18:18,214 INFO     29 [qwen-vl-parser] page=2 text: 151 sections
2026-08-10 13:18:18,214 INFO     29 [qwen-vl-parser] parse_pdf done: 177 sections from 2 pages.
2026-08-10 13:18:18,220 INFO     29 Close text detector.
2026-08-10 13:18:18,611 INFO     29 Close text recognizer.
2026-08-10 13:18:19,019 INFO     29 Close recognizer.
2026-08-10 13:18:19,453 INFO     29 Close recognizer.
2026-08-10 13:18:19,910 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:18:19,910 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Parser:MedLink | outputs={"html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "json"}
2026-08-10 13:18:19,910 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:18:19,927 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:19,927 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 邹城市人民医院\n[BBOX-1] 门诊病历\n[BBOX-2] 性别：男性\n[BBOX-3] 年龄：65岁\n[BBOX-4] 科室：呼吸与危重症医学科(千泉门诊)\n[BBOX-5] ID号\n[BBOX-6] 就诊时间：2025-05-29 10:06\n[BBOX-7] 主诉：阵发性憋喘60年。\n[BBOX-8] 现病史：阵发性憋喘60年，遇冷空气时加重，时咳嗽、咳少量白痰，时有\n[BBOX-9] 心慌、胸闷、气短，无胸痛，无恶心、呕吐，无腹痛、无腹泻，在院外未治疗，\n[BBOX-10] 症状时好时坏，来诊。\n[BBOX-11] 既往史：平素身体健康，否认高血压、冠心病、糖尿病史。否认病毒性肝\n[BBOX-12] 炎、肺结核等传染病史及密切接触史。\n[BBOX-13] 过敏史：否认药物过敏史。\n[BBOX-14] 体格检查：神志清、精神可，胸廓无畸形，双肺呼吸音清，未闻及干湿\n[BBOX-15] 啰音，心率75次/分，心律齐，无杂音，双下肢无水肿。\n[BBOX-16] 辅助检查：\n[BBOX-17] 诊断：喘憋（主诊断）\n[BBOX-18] 诊疗意见：\n[BBOX-19] 避免受凉感冒，避免过度劳累，如有不适，及时就诊。\n[BBOX-20] ☑已向患者(家属)进行了关于患者病情、目前状况及诊疗方案的教育。\n[BBOX-21] ☑已向患者(家属)交代了各种诊疗方案的效果和不遵从医嘱可能导致的后果。\n[BBOX-22] 医生签名：\n[BBOX-23] 门诊部\n[BBOX-24] (1)\n[BBOX-25] 708833003930\n[BBOX-26] 邹城市人民医院\n[BBOX-27] 肺功能检查报告单\n[BBOX-28] 姓名\n[BBOX-29] 温度：28℃\n[BBOX-30] 住院号：\n[BBOX-31] 性别：男\n[BBOX-32] 气压：745mmHg\n[BBOX-33] 科室：呼吸与危重症医学科门\n[BBOX-34] 年龄：65岁\n[BBOX-35] 检查日期：05/29/25\n[BBOX-36] 床位号：\n[BBOX-37] 吸烟：无\n[BBOX-38] 肺容积：\n[BBOX-39] (BTPS)\n[BBOX-40] 用药前\n[BBOX-41] 用药后\n[BBOX-42] 预计值：\n[BBOX-43] 实测值\n[BBOX-44] 实/预%\n[BBOX-45] 实测值\n[BBOX-46] 实/预%改善率\n[BBOX-47] 肺活量：\n[BBOX-48] VC\n[BBOX-49] L\n[BBOX-50] 3.56\n[BBOX-51] 潮气量：\n[BBOX-52] Vt\n[BBOX-53] L\n[BBOX-54] 深吸气量：\n[BBOX-55] IC\n[BBOX-56] L\n[BBOX-57] 补呼气量：\n[BBOX-58] ERV\n[BBOX-59] L\n[BBOX-60] 残气：\n[BBOX-61] RV Sb\n[BBOX-62] L\n[BBOX-63] 2.19\n[BBOX-64] 功能残气量：\n[BBOX-65] FRC N2\n[BBOX-66] L\n[BBOX-67] 3.39\n[BBOX-68] 肺总量：\n[BBOX-69] TLC Sb\n[BBOX-70] L\n[BBOX-71] 5.65\n[BBOX-72] 残气/肺总量：\n[BBOX-73] RV/TLC Sb\n[BBOX-74] %\n[BBOX-75] 39\n[BBOX-76] 通气功能：\n[BBOX-77] 用力肺活量：\n[BBOX-78] FVC\n[BBOX-79] L\n[BBOX-80] 3.56\n[BBOX-81] 2.90\n[BBOX-82] 81\n[BBOX-83] 3.24\n[BBOX-84] 91\n[BBOX-85] 12\n[BBOX-86] 用力呼气一秒量：\n[BBOX-87] FEV1\n[BBOX-88] L\n[BBOX-89] 2.77\n[BBOX-90] 1.45\n[BBOX-91] 52\n[BBOX-92] 1.65\n[BBOX-93] 60\n[BBOX-94] 14\n[BBOX-95] 用力呼气一秒率：\n[BBOX-96] FEV1/FVC\n[BBOX-97] %\n[BBOX-98] 80\n[BBOX-99] 50\n[BBOX-100] 63\n[BBOX-101] 51\n[BBOX-102] 64\n[BBOX-103] 2\n[BBOX-104] 用力呼气中期流速：\n[BBOX-105] FEF25-75%L/sec\n[BBOX-106] 2.85\n[BBOX-107] 0.70\n[BBOX-108] 25\n[BBOX-109] 0.76\n[BBOX-110] 27\n[BBOX-111] 8\n[BBOX-112] 25%用力呼气流速：\n[BBOX-113] FEF25%\n[BBOX-114] L/sec\n[BBOX-115] 6.85\n[BBOX-116] 1.58\n[BBOX-117] 23\n[BBOX-118] 2.00\n[BBOX-119] 29\n[BBOX-120] 27\n[BBOX-121] 50%用力呼气流速：\n[BBOX-122] FEF50%\n[BBOX-123] L/sec\n[BBOX-124] 3.57\n[BBOX-125] 0.82\n[BBOX-126] 23\n[BBOX-127] 0.91\n[BBOX-128] 25\n[BBOX-129] 11\n[BBOX-130] 75%用力呼气流速：\n[BBOX-131] FEF75%\n[BBOX-132] L/sec\n[BBOX-133] 1.23\n[BBOX-134] 0.34\n[BBOX-135] 28\n[BBOX-136] 0.39\n[BBOX-137] 32\n[BBOX-138] 13\n[BBOX-139] 峰值流速\n[BBOX-140] PEF\n[BBOX-141] L/sec\n[BBOX-142] 7.51\n[BBOX-143] 2.72\n[BBOX-144] 36\n[BBOX-145] 2.71\n[BBOX-146] 36\n[BBOX-147] -0\n[BBOX-148] 每分静息通气量：\n[BBOX-149] VE\n[BBOX-150] L/min\n[BBOX-151] 6.8\n[BBOX-152] 最大自主通气量：\n[BBOX-153] MVV\n[BBOX-154] L/min\n[BBOX-155] 121\n[BBOX-156] 弥散功能\n[BBOX-157] CO弥散量：\n[BBOX-158] DLCO\n[BBOX-159] mL/mmHg/min8.3\n[BBOX-160] DLCOexh\n[BBOX-161] mL/mmHg/min8.3\n[BBOX-162] VA\n[BBOX-163] L\n[BBOX-164] VA exh\n[BBOX-165] L\n[BBOX-166] 肺泡容积：\n[BBOX-167] DLCO/VA\n[BBOX-168] mL/mmHg/mi8.68\n[BBOX-169] 弥散常数：\n[BBOX-170] DLexh/VA\n[BBOX-171] mL/mmHg/mi8.68\n[BBOX-172] 结论：\n[BBOX-173] 中重度阻塞性肺通气功能障碍。\n[BBOX-174] 支气管舒张试验阳性。\n[BBOX-175] 此报告仅供临床参考\n[BBOX-176] 检查者："
  }
]
2026-08-10 13:18:23,160 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:23,180 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 1}
2026-08-10 13:18:23,188 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:18:23,188 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 13:18:23,188 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:18:23,188 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 1}
2026-08-10 13:18:23,195 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:18:23,196 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:18:23,196 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:18:23,200 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:23,200 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:18:23,803 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:23,812 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:18:23,812 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:18:23,812 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:18:23,818 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:23,818 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:18:24,351 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:24,358 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:18:24,359 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:18:24,359 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:18:24,364 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:18:24,364 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:18:24,364 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:18:24,364 INFO     29 [qwen-vl-text] positions(25): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:18:24,364 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [25]
2026-08-10 13:18:24,564 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:18:24,565 INFO     29 [qwen-vl-text] LLM extraction start, text_len=418
2026-08-10 13:18:24,565 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:24,566 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 24, \"encounter_dates\": [\"2025-05-29\"], \"department\": \"呼吸与危重症医学科(千泉门诊)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "邹城市人民医院\n门诊病历\n性别：男性\n年龄：65岁\n科室：呼吸与危重症医学科(千泉门诊)\nID号\n就诊时间：2025-05-29 10:06\n主诉：阵发性憋喘60年。\n现病史：阵发性憋喘60年，遇冷空气时加重，时咳嗽、咳少量白痰，时有\n心慌、胸闷、气短，无胸痛，无恶心、呕吐，无腹痛、无腹泻，在院外未治疗，\n症状时好时坏，来诊。\n既往史：平素身体健康，否认高血压、冠心病、糖尿病史。否认病毒性肝\n炎、肺结核等传染病史及密切接触史。\n过敏史：否认药物过敏史。\n体格检查：神志清、精神可，胸廓无畸形，双肺呼吸音清，未闻及干湿\n啰音，心率75次/分，心律齐，无杂音，双下肢无水肿。\n辅助检查：\n诊断：喘憋（主诊断）\n诊疗意见：\n避免受凉感冒，避免过度劳累，如有不适，及时就诊。\n☑已向患者(家属)进行了关于患者病情、目前状况及诊疗方案的教育。\n☑已向患者(家属)交代了各种诊疗方案的效果和不遵从医嘱可能导致的后果。\n医生签名：\n门诊部\n(1)",
    "role": "user"
  }
]
2026-08-10 13:18:26,553 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:26,553 INFO     29 [qwen-vl-text] LLM output (len=316):
{
  "encounter_date": "2025-05-29",
  "chief_complaint": "阵发性憋喘60年。",
  "present_illness": "阵发性憋喘60年，遇冷空气时加重，时咳嗽、咳少量白痰，时有\n心慌、胸闷、气短，无胸痛，无恶心、呕吐，无腹痛、无腹泻，在院外未治疗，\n症状时好时坏，来诊。",
  "past_history": "平素身体健康，否认高血压、冠心病、糖尿病史。否认病毒性肝\n炎、肺结核等传染病史及密切接触史。",
  "diagnosis": "喘憋（主诊断）",
  "treatment_plan": "避免受凉感冒，避免过度劳累，如有不适，及时就诊。"
}
2026-08-10 13:18:26,553 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-29]
2026-08-10 13:18:26,556 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1313053, prompt_len=1106
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["邹城市人民医院", "门诊病历", "性别：男性", "年龄：65岁", "科室：呼吸与危重症医学科(千泉门诊)", "ID号", "就诊时间：2025-05-29 10:06", "主诉：阵发性憋喘60年。", "现病史：阵发性憋喘60年，遇冷空气时加重，时咳嗽、咳少量白痰，时有", "心慌、胸闷、气短，无胸痛，无恶心、呕吐，无腹痛、无腹泻，在院外未治疗，", "症状时好时坏，来诊。", "既往史：平素身体健康，否认高血压、冠心病、糖尿病史。否认病毒性肝", "炎、肺结核等传染病史及密切接触史。", "过敏史：否认药物过敏史。", "体格检查：神志清、精神可，胸廓无畸形，双肺呼吸音清，未闻及干湿", "啰音，心率75次/分，心律齐，无杂音，双下肢无水肿。", "辅助检查：", "诊断：喘憋（主诊断）", "诊疗意见：", "避免受凉感冒，避免过度劳累，如有不适，及时就诊。", "☑已向患者(家属)进行了关于患者病情、目前状况及诊疗方案的教育。", "☑已向患者(家属)交代了各种诊疗方案的效果和不遵从医嘱可能导致的后果。", "医生签名：", "门诊部", "(1)"]

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
2026-08-10 13:18:35,021 INFO     29 [qwen-vl-text] coord API raw response (len=1501):
[
	{"text": "邹城市人民医院", "bbox": [275, 40, 680, 69]},
	{"text": "门诊病历", "bbox": [374, 94, 580, 120]},
	{"text": "性别：男性", "bbox": [344, 140, 467, 161]},
	{"text": "年龄：65岁", "bbox": [595, 140, 747, 161]},
	{"text": "科室：呼吸与危重症医学科(千泉门诊)", "bbox": [52, 175, 475, 196]},
	{"text": "ID号", "bbox": [595, 175, 650, 196]},
	{"text": "就诊时间：2025-05-29 10:06", "bbox": [97, 208, 436, 228]},
	{"text": "主诉：阵发性憋喘60年。", "bbox": [97, 243, 370, 263]},
	{"text": "现病史：阵发性憋喘60年，遇冷空气时加重，时咳嗽、咳少量白痰，时有", "bbox": [97, 277, 914, 298]},
	{"text": "心慌、胸闷、气短，无胸痛，无恶心、呕吐，无腹痛、无腹泻，在院外未治疗，", "bbox": [41, 301, 913, 322]},
	{"text": "症状时好时坏，来诊。", "bbox": [40, 325, 282, 345]},
	{"text": "既往史：平素身体健康，否认高血压、冠心病、糖尿病史。否认病毒性肝", "bbox": [95, 362, 911, 382]},
	{"text": "炎、肺结核等传染病史及密切接触史。", "bbox": [40, 386, 457, 406]},
	{"text": "过敏史：否认药物过敏史。", "bbox": [91, 420, 393, 440]},
	{"text": "体格检查：神志清、精神可，胸廓无畸形，双肺呼吸音清，未闻及干湿", "bbox": [94, 457, 890, 477]},
	{"text": "啰音，心率75次/分，心律齐，无杂音，双下肢无水肿。", "bbox": [34, 480, 641, 501]},
	{"text": "辅助检查：", "bbox": [90, 516, 210, 536]},
	{"text": "诊断：喘憋（主诊断）", "bbox": [90, 550, 324, 570]},
	{"text": "诊疗意见：", "bbox": [90, 586, 208, 606]},
	{"text": "避免受凉感冒，避免过度劳累，如有不适，及时就诊。", "bbox": [90, 621, 680, 641]},
	{"text": "☑已向患者(家属)进行了关于患者病情、目前状况及诊疗方案的教育。", "bbox": [32, 659, 809, 680]},
	{"text": "☑已向患者(家属)交代了各种诊疗方案的效果和不遵从医嘱可能导致的后果。", "bbox": [32, 683, 888, 704]},
	{"text": "医生签名：", "bbox": [539, 728, 650, 749]},
	{"text": "门诊部", "bbox": [531, 772, 687, 802]},
	{"text": "(1)", "bbox": [588, 807, 630, 825]}
]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=8.5s
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[0]: text=邹城市人民医院, bbox=[275, 40, 680, 69]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[374, 94, 580, 120]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男性, bbox=[344, 140, 467, 161]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：65岁, bbox=[595, 140, 747, 161]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重症医学科(千泉门诊), bbox=[52, 175, 475, 196]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[5]: text=ID号, bbox=[595, 175, 650, 196]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[6]: text=就诊时间：2025-05-29 10:06, bbox=[97, 208, 436, 228]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[7]: text=主诉：阵发性憋喘60年。, bbox=[97, 243, 370, 263]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[8]: text=现病史：阵发性憋喘60年，遇冷空气时加重，时咳嗽、咳少量白痰，时有, bbox=[97, 277, 914, 298]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[9]: text=心慌、胸闷、气短，无胸痛，无恶心、呕吐，无腹痛、无腹泻，在院外未治疗，, bbox=[41, 301, 913, 322]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[10]: text=症状时好时坏，来诊。, bbox=[40, 325, 282, 345]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[11]: text=既往史：平素身体健康，否认高血压、冠心病、糖尿病史。否认病毒性肝, bbox=[95, 362, 911, 382]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[12]: text=炎、肺结核等传染病史及密切接触史。, bbox=[40, 386, 457, 406]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史：否认药物过敏史。, bbox=[91, 420, 393, 440]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[14]: text=体格检查：神志清、精神可，胸廓无畸形，双肺呼吸音清，未闻及干湿, bbox=[94, 457, 890, 477]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[15]: text=啰音，心率75次/分，心律齐，无杂音，双下肢无水肿。, bbox=[34, 480, 641, 501]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查：, bbox=[90, 516, 210, 536]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[17]: text=诊断：喘憋（主诊断）, bbox=[90, 550, 324, 570]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[18]: text=诊疗意见：, bbox=[90, 586, 208, 606]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[19]: text=避免受凉感冒，避免过度劳累，如有不适，及时就诊。, bbox=[90, 621, 680, 641]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[20]: text=☑已向患者(家属)进行了关于患者病情、目前状况及诊疗方案的教育。, bbox=[32, 659, 809, 680]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[21]: text=☑已向患者(家属)交代了各种诊疗方案的效果和不遵从医嘱可能导致的后果。, bbox=[32, 683, 888, 704]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[22]: text=医生签名：, bbox=[539, 728, 650, 749]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[23]: text=门诊部, bbox=[531, 772, 687, 802]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] coord item[24]: text=(1), bbox=[588, 807, 630, 825]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] page=0 — 25/25 coords, api_time=8.5s
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] new_positions (25):
[[0, 163.625, 404.59999999999997, 33.68, 58.098], [0, 222.53, 345.09999999999997, 79.148, 101.03999999999999], [0, 204.67999999999998, 277.865, 117.88, 135.56199999999998], [0, 354.025, 444.465, 117.88, 135.56199999999998], [0, 30.939999999999998, 282.625, 147.35, 165.03199999999998], [0, 354.025, 386.75, 147.35, 165.03199999999998], [0, 57.714999999999996, 259.42, 175.136, 191.976], [0, 57.714999999999996, 220.14999999999998, 204.606, 221.446], [0, 57.714999999999996, 543.8299999999999, 233.23399999999998, 250.916], [0, 24.395, 543.235, 253.44199999999998, 271.12399999999997], [0, 23.799999999999997, 167.79, 273.65, 290.49], [0, 56.525, 542.045, 304.804, 321.644], [0, 23.799999999999997, 271.91499999999996, 325.012, 341.852], [0, 54.144999999999996, 233.83499999999998, 353.64, 370.47999999999996], [0, 55.93, 529.55, 384.794, 401.63399999999996], [0, 20.23, 381.395, 404.15999999999997, 421.842], [0, 53.55, 124.94999999999999, 434.472, 451.312], [0, 53.55, 192.78, 463.09999999999997, 479.94], [0, 53.55, 123.75999999999999, 493.412, 510.252], [0, 53.55, 404.59999999999997, 522.882, 539.722], [0, 19.04, 481.35499999999996, 554.8779999999999, 572.56], [0, 19.04, 528.36, 575.086, 592.768], [0, 320.705, 386.75, 612.976, 630.658], [0, 315.945, 408.765, 650.024, 675.284], [0, 349.85999999999996, 374.84999999999997, 679.494, 694.65]]
2026-08-10 13:18:35,022 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=10.7s
2026-08-10 13:18:35,029 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:18:35,029 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:18:35,029 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:18:35,030 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:18:35.029+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 44, "failed": 0, "current": {"e97265da94bd11f1bd9827cf206dfa2d": {"id": "e97265da94bd11f1bd9827cf206dfa2d", "doc_id": "e9284be494bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZZYU \u7537 65\u5c81 \u63a8\u6d4e\u5357(1).pdf", "type": "pdf", "location": "ZZYU \u7537 65\u5c81 \u63a8\u6d4e\u5357(1).pdf", "size": 756692, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367881156, "task_type": "dataflow", "root_trace_id": "7b4a5c76667c474a9c93698057034643", "root_traceparent": "00-7b4a5c76667c474a9c93698057034643-1740e57c2225b187-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:18:35,035 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:35,035 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:18:36,146 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:36,154 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:18:36,154 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:18:36,154 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:18:36,159 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:36,160 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:18:36,618 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:36,623 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:18:36,623 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:18:36,623 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:18:36,628 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:36,628 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:18:37,093 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:37,099 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:18:37,100 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:18:37,100 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:18:37,103 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:37,104 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:18:37,593 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:37,597 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:18:37,598 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:18:37,598 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:18:37,602 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:18:37,603 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:18:37,603 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:18:37,603 INFO     29 [qwen-vl-text] positions(152): [[0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:18:37,603 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [1, 151]
2026-08-10 13:18:37,805 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:18:37,970 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:18:37,971 INFO     29 [qwen-vl-text] LLM extraction start, text_len=848
2026-08-10 13:18:37,971 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:37,971 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 25, \"bbox_end\": 176, \"encounter_dates\": [\"2025-05-29\"], \"department\": \"呼吸与危重症医学科门\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "708833003930\n邹城市人民医院\n肺功能检查报告单\n姓名\n温度：28℃\n住院号：\n性别：男\n气压：745mmHg\n科室：呼吸与危重症医学科门\n年龄：65岁\n检查日期：05/29/25\n床位号：\n吸烟：无\n肺容积：\n(BTPS)\n用药前\n用药后\n预计值：\n实测值\n实/预%\n实测值\n实/预%改善率\n肺活量：\nVC\nL\n3.56\n潮气量：\nVt\nL\n深吸气量：\nIC\nL\n补呼气量：\nERV\nL\n残气：\nRV Sb\nL\n2.19\n功能残气量：\nFRC N2\nL\n3.39\n肺总量：\nTLC Sb\nL\n5.65\n残气/肺总量：\nRV/TLC Sb\n%\n39\n通气功能：\n用力肺活量：\nFVC\nL\n3.56\n2.90\n81\n3.24\n91\n12\n用力呼气一秒量：\nFEV1\nL\n2.77\n1.45\n52\n1.65\n60\n14\n用力呼气一秒率：\nFEV1/FVC\n%\n80\n50\n63\n51\n64\n2\n用力呼气中期流速：\nFEF25-75%L/sec\n2.85\n0.70\n25\n0.76\n27\n8\n25%用力呼气流速：\nFEF25%\nL/sec\n6.85\n1.58\n23\n2.00\n29\n27\n50%用力呼气流速：\nFEF50%\nL/sec\n3.57\n0.82\n23\n0.91\n25\n11\n75%用力呼气流速：\nFEF75%\nL/sec\n1.23\n0.34\n28\n0.39\n32\n13\n峰值流速\nPEF\nL/sec\n7.51\n2.72\n36\n2.71\n36\n-0\n每分静息通气量：\nVE\nL/min\n6.8\n最大自主通气量：\nMVV\nL/min\n121\n弥散功能\nCO弥散量：\nDLCO\nmL/mmHg/min8.3\nDLCOexh\nmL/mmHg/min8.3\nVA\nL\nVA exh\nL\n肺泡容积：\nDLCO/VA\nmL/mmHg/mi8.68\n弥散常数：\nDLexh/VA\nmL/mmHg/mi8.68\n结论：\n中重度阻塞性肺通气功能障碍。\n支气管舒张试验阳性。\n此报告仅供临床参考\n检查者：",
    "role": "user"
  }
]
2026-08-10 13:18:43,880 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:18:43,880 INFO     29 [qwen-vl-text] LLM output (len=1162):
{
  "exam_date": "2025-05-29",
  "report_date": null,
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸与危重症医学科门",
  "bed_number": null,
  "findings": "肺容积：\n(BTPS)\n用药前\n用药后\n预计值：\n实测值\n实/预%\n实测值\n实/预%改善率\n肺活量：\nVC\nL\n3.56\n潮气量：\nVt\nL\n深吸气量：\nIC\nL\n补呼气量：\nERV\nL\n残气：\nRV Sb\nL\n2.19\n功能残气量：\nFRC N2\nL\n3.39\n肺总量：\nTLC Sb\nL\n5.65\n残气/肺总量：\nRV/TLC Sb\n%\n39\n通气功能：\n用力肺活量：\nFVC\nL\n3.56\n2.90\n81\n3.24\n91\n12\n用力呼气一秒量：\nFEV1\nL\n2.77\n1.45\n52\n1.65\n60\n14\n用力呼气一秒率：\nFEV1/FVC\n%\n80\n50\n63\n51\n64\n2\n用力呼气中期流速：\nFEF25-75%L/sec\n2.85\n0.70\n25\n0.76\n27\n8\n25%用力呼气流速：\nFEF25%\nL/sec\n6.85\n1.58\n23\n2.00\n29\n27\n50%用力呼气流速：\nFEF50%\nL/sec\n3.57\n0.82\n23\n0.91\n25\n11\n75%用力呼气流速：\nFEF75%\nL/sec\n1.23\n0.34\n28\n0.39\n32\n13\n峰值流速\nPEF\nL/sec\n7.51\n2.72\n36\n2.71\n36\n-0\n每分静息通气量：\nVE\nL/min\n6.8\n最大自主通气量：\nMVV\nL/min\n121\n弥散功能\nCO弥散量：\nDLCO\nmL/mmHg/min8.3\nDLCOexh\nmL/mmHg/min8.3\nVA\nL\nVA exh\nL\n肺泡容积：\nDLCO/VA\nmL/mmHg/mi8.68\n弥散常数：\nDLexh/VA\nmL/mmHg/mi8.68",
  "conclusion": "中重度阻塞性肺通气功能障碍。\n支气管舒张试验阳性。",
  "physician": null,
  "reviewer": null
}
2026-08-10 13:18:43,886 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1313053, prompt_len=627
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["708833003930"]

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
2026-08-10 13:18:46,036 INFO     29 [qwen-vl-text] coord API raw response (len=71):
```json
[
	{"text": "708833003930", "bbox": [537, 810, 687, 838]}
]
```
2026-08-10 13:18:46,037 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=2.2s
2026-08-10 13:18:46,037 INFO     29 [qwen-vl-text] coord item[0]: text=708833003930, bbox=[537, 810, 687, 838]
2026-08-10 13:18:46,037 INFO     29 [qwen-vl-text] page=0 — 1/1 coords, api_time=2.2s
2026-08-10 13:18:46,038 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=845206, prompt_len=1902
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共151行）
["邹城市人民医院", "肺功能检查报告单", "姓名", "温度：28℃", "住院号：", "性别：男", "气压：745mmHg", "科室：呼吸与危重症医学科门", "年龄：65岁", "检查日期：05/29/25", "床位号：", "吸烟：无", "肺容积：", "(BTPS)", "用药前", "用药后", "预计值：", "实测值", "实/预%", "实测值", "实/预%改善率", "肺活量：", "VC", "L", "3.56", "潮气量：", "Vt", "L", "深吸气量：", "IC", "L", "补呼气量：", "ERV", "L", "残气：", "RV Sb", "L", "2.19", "功能残气量：", "FRC N2", "L", "3.39", "肺总量：", "TLC Sb", "L", "5.65", "残气/肺总量：", "RV/TLC Sb", "%", "39", "通气功能：", "用力肺活量：", "FVC", "L", "3.56", "2.90", "81", "3.24", "91", "12", "用力呼气一秒量：", "FEV1", "L", "2.77", "1.45", "52", "1.65", "60", "14", "用力呼气一秒率：", "FEV1/FVC", "%", "80", "50", "63", "51", "64", "2", "用力呼气中期流速：", "FEF25-75%L/sec", "2.85", "0.70", "25", "0.76", "27", "8", "25%用力呼气流速：", "FEF25%", "L/sec", "6.85", "1.58", "23", "2.00", "29", "27", "50%用力呼气流速：", "FEF50%", "L/sec", "3.57", "0.82", "23", "0.91", "25", "11", "75%用力呼气流速：", "FEF75%", "L/sec", "1.23", "0.34", "28", "0.39", "32", "13", "峰值流速", "PEF", "L/sec", "7.51", "2.72", "36", "2.71", "36", "-0", "每分静息通气量：", "VE", "L/min", "6.8", "最大自主通气量：", "MVV", "L/min", "121", "弥散功能", "CO弥散量：", "DLCO", "mL/mmHg/min8.3", "DLCOexh", "mL/mmHg/min8.3", "VA", "L", "VA exh", "L", "肺泡容积：", "DLCO/VA", "mL/mmHg/mi8.68", "弥散常数：", "DLexh/VA", "mL/mmHg/mi8.68", "结论：", "中重度阻塞性肺通气功能障碍。", "支气管舒张试验阳性。", "此报告仅供临床参考", "检查者："]

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
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord API raw response (len=7478):
[
	{"text": "邹城市人民医院", "bbox": [375, 35, 623, 62]},
	{"text": "肺功能检查报告单", "bbox": [410, 67, 610, 89]},
	{"text": "姓名", "bbox": [414, 102, 448, 116]},
	{"text": "温度：28℃", "bbox": [672, 100, 754, 113]},
	{"text": "住院号：", "bbox": [178, 124, 234, 137]},
	{"text": "性别：男", "bbox": [414, 123, 473, 137]},
	{"text": "气压：745mmHg", "bbox": [672, 120, 795, 134]},
	{"text": "科室：呼吸与危重症医学科门", "bbox": [178, 144, 387, 157]},
	{"text": "年龄：65岁", "bbox": [414, 143, 500, 156]},
	{"text": "检查日期：05/29/25", "bbox": [672, 141, 808, 154]},
	{"text": "床位号：", "bbox": [178, 165, 234, 178]},
	{"text": "吸烟：无", "bbox": [414, 164, 473, 177]},
	{"text": "肺容积：", "bbox": [163, 195, 247, 215]},
	{"text": "(BTPS)", "bbox": [300, 195, 357, 208]},
	{"text": "用药前", "bbox": [638, 187, 688, 200]},
	{"text": "用药后", "bbox": [761, 182, 811, 195]},
	{"text": "预计值：", "bbox": [481, 201, 535, 214]},
	{"text": "实测值", "bbox": [607, 201, 656, 214]},
	{"text": "实/预%", "bbox": [675, 200, 725, 213]},
	{"text": "实测值", "bbox": [744, 200, 793, 213]},
	{"text": "实/预%改善率", "bbox": [814, 198, 912, 211]},
	{"text": "肺活量：", "bbox": [178, 223, 233, 236]},
	{"text": "VC", "bbox": [323, 222, 348, 235]},
	{"text": "L", "bbox": [412, 223, 424, 236]},
	{"text": "3.56", "bbox": [498, 222, 531, 235]},
	{"text": "潮气量：", "bbox": [178, 237, 233, 250]},
	{"text": "Vt", "bbox": [323, 237, 342, 250]},
	{"text": "L", "bbox": [412, 237, 424, 250]},
	{"text": "深吸气量：", "bbox": [178, 251, 249, 264]},
	{"text": "IC", "bbox": [323, 251, 342, 264]},
	{"text": "L", "bbox": [412, 251, 424, 264]},
	{"text": "补呼气量：", "bbox": [178, 265, 249, 278]},
	{"text": "ERV", "bbox": [323, 265, 359, 278]},
	{"text": "L", "bbox": [412, 265, 424, 278]},
	{"text": "残气：", "bbox": [178, 279, 215, 291]},
	{"text": "RV Sb", "bbox": [323, 279, 377, 292]},
	{"text": "L", "bbox": [412, 279, 424, 292]},
	{"text": "2.19", "bbox": [498, 279, 531, 292]},
	{"text": "功能残气量：", "bbox": [178, 292, 265, 305]},
	{"text": "FRC N2", "bbox": [323, 293, 385, 306]},
	{"text": "L", "bbox": [412, 293, 424, 306]},
	{"text": "3.39", "bbox": [498, 293, 531, 306]},
	{"text": "肺总量：", "bbox": [178, 306, 233, 319]},
	{"text": "TLC Sb", "bbox": [323, 307, 380, 320]},
	{"text": "L", "bbox": [412, 307, 424, 320]},
	{"text": "5.65", "bbox": [498, 307, 531, 320]},
	{"text": "残气/肺总量：", "bbox": [178, 319, 269, 332]},
	{"text": "RV/TLC Sb", "bbox": [323, 321, 408, 335]},
	{"text": "%", "bbox": [412, 320, 428, 333]},
	{"text": "39", "bbox": [512, 322, 531, 335]},
	{"text": "通气功能：", "bbox": [178, 351, 285, 370]},
	{"text": "用力肺活量：", "bbox": [178, 376, 265, 389]},
	{"text": "FVC", "bbox": [323, 376, 357, 389]},
	{"text": "L", "bbox": [412, 377, 424, 390]},
	{"text": "3.56", "bbox": [498, 376, 531, 389]},
	{"text": "2.90", "bbox": [615, 376, 649, 389]},
	{"text": "81", "bbox": [689, 376, 707, 389]},
	{"text": "3.24", "bbox": [735, 376, 768, 389]},
	{"text": "91", "bbox": [808, 376, 827, 389]},
	{"text": "12", "bbox": [870, 376, 889, 389]},
	{"text": "用力呼气一秒量：", "bbox": [178, 390, 299, 403]},
	{"text": "FEV1", "bbox": [323, 390, 364, 403]},
	{"text": "L", "bbox": [412, 391, 424, 404]},
	{"text": "2.77", "bbox": [498, 390, 531, 403]},
	{"text": "1.45", "bbox": [615, 390, 649, 403]},
	{"text": "52", "bbox": [689, 390, 707, 403]},
	{"text": "1.65", "bbox": [735, 390, 768, 403]},
	{"text": "60", "bbox": [808, 390, 827, 403]},
	{"text": "14", "bbox": [870, 390, 889, 403]},
	{"text": "用力呼气一秒率：", "bbox": [178, 404, 299, 417]},
	{"text": "FEV1/FVC", "bbox": [323, 404, 404, 417]},
	{"text": "%", "bbox": [412, 405, 428, 418]},
	{"text": "80", "bbox": [512, 404, 531, 417]},
	{"text": "50", "bbox": [628, 404, 649, 417]},
	{"text": "63", "bbox": [689, 404, 707, 417]},
	{"text": "51", "bbox": [747, 404, 768, 417]},
	{"text": "64", "bbox": [808, 404, 827, 417]},
	{"text": "2", "bbox": [877, 404, 889, 417]},
	{"text": "用力呼气中期流速：", "bbox": [178, 418, 317, 431]},
	{"text": "FEF25-75%L/sec", "bbox": [323, 418, 454, 431]},
	{"text": "2.85", "bbox": [498, 418, 531, 431]},
	{"text": "0.70", "bbox": [615, 418, 649, 431]},
	{"text": "25", "bbox": [689, 418, 707, 431]},
	{"text": "0.76", "bbox": [735, 418, 768, 431]},
	{"text": "27", "bbox": [808, 418, 827, 431]},
	{"text": "8", "bbox": [877, 418, 889, 431]},
	{"text": "25%用力呼气流速：", "bbox": [178, 432, 317, 445]},
	{"text": "FEF25%", "bbox": [323, 432, 387, 445]},
	{"text": "L/sec", "bbox": [412, 433, 454, 446]},
	{"text": "6.85", "bbox": [498, 432, 531, 445]},
	{"text": "1.58", "bbox": [615, 432, 649, 445]},
	{"text": "23", "bbox": [689, 432, 707, 445]},
	{"text": "2.00", "bbox": [735, 432, 768, 445]},
	{"text": "29", "bbox": [808, 432, 827, 445]},
	{"text": "27", "bbox": [868, 432, 889, 445]},
	{"text": "50%用力呼气流速：", "bbox": [178, 446, 317, 459]},
	{"text": "FEF50%", "bbox": [323, 446, 387, 459]},
	{"text": "L/sec", "bbox": [412, 447, 454, 460]},
	{"text": "3.57", "bbox": [498, 446, 531, 459]},
	{"text": "0.82", "bbox": [615, 446, 649, 459]},
	{"text": "23", "bbox": [689, 446, 707, 459]},
	{"text": "0.91", "bbox": [735, 446, 768, 459]},
	{"text": "25", "bbox": [808, 446, 827, 459]},
	{"text": "11", "bbox": [870, 446, 889, 459]},
	{"text": "75%用力呼气流速：", "bbox": [178, 460, 317, 473]},
	{"text": "FEF75%", "bbox": [323, 460, 387, 473]},
	{"text": "L/sec", "bbox": [412, 461, 454, 474]},
	{"text": "1.23", "bbox": [498, 460, 531, 473]},
	{"text": "0.34", "bbox": [615, 460, 649, 473]},
	{"text": "28", "bbox": [689, 460, 707, 473]},
	{"text": "0.39", "bbox": [735, 460, 768, 473]},
	{"text": "32", "bbox": [808, 460, 827, 473]},
	{"text": "13", "bbox": [870, 460, 889, 473]},
	{"text": "峰值流速", "bbox": [178, 473, 243, 486]},
	{"text": "PEF", "bbox": [323, 474, 356, 487]},
	{"text": "L/sec", "bbox": [412, 475, 454, 488]},
	{"text": "7.51", "bbox": [498, 474, 531, 487]},
	{"text": "2.72", "bbox": [615, 474, 649, 487]},
	{"text": "36", "bbox": [689, 474, 707, 487]},
	{"text": "2.71", "bbox": [735, 474, 768, 487]},
	{"text": "36", "bbox": [808, 474, 827, 487]},
	{"text": "-0", "bbox": [870, 474, 889, 487]},
	{"text": "每分静息通气量：", "bbox": [178, 487, 299, 500]},
	{"text": "VE", "bbox": [323, 488, 346, 501]},
	{"text": "L/min", "bbox": [412, 488, 454, 501]},
	{"text": "6.8", "bbox": [507, 488, 531, 501]},
	{"text": "最大自主通气量：", "bbox": [178, 500, 299, 513]},
	{"text": "MVV", "bbox": [323, 501, 360, 514]},
	{"text": "L/min", "bbox": [412, 501, 454, 514]},
	{"text": "121", "bbox": [505, 501, 531, 514]},
	{"text": "弥散功能", "bbox": [178, 532, 277, 551]},
	{"text": "CO弥散量：", "bbox": [178, 561, 257, 574]},
	{"text": "DLCO", "bbox": [323, 561, 370, 574]},
	{"text": "mL/mmHg/min8.3", "bbox": [412, 561, 531, 574]},
	{"text": "DLCOexh", "bbox": [323, 575, 396, 588]},
	{"text": "mL/mmHg/min8.3", "bbox": [412, 575, 531, 588]},
	{"text": "VA", "bbox": [323, 589, 346, 602]},
	{"text": "L", "bbox": [412, 589, 424, 602]},
	{"text": "VA exh", "bbox": [323, 603, 383, 616]},
	{"text": "L", "bbox": [412, 603, 424, 616]},
	{"text": "肺泡容积：", "bbox": [178, 615, 249, 628]},
	{"text": "DLCO/VA", "bbox": [323, 616, 396, 629]},
	{"text": "mL/mmHg/mi8.68", "bbox": [412, 616, 531, 629]},
	{"text": "弥散常数：", "bbox": [178, 632, 249, 645]},
	{"text": "DLexh/VA", "bbox": [323, 632, 399, 645]},
	{"text": "mL/mmHg/mi8.68", "bbox": [412, 632, 531, 645]},
	{"text": "结论：", "bbox": [180, 666, 231, 683]},
	{"text": "中重度阻塞性肺通气功能障碍。", "bbox": [178, 696, 400, 709]},
	{"text": "支气管舒张试验阳性。", "bbox": [178, 710, 339, 723]},
	{"text": "此报告仅供临床参考", "bbox": [178, 858, 314, 870]},
	{"text": "检查者：", "bbox": [370, 857, 428, 870]}
]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord API: raw_items=151, valid_items=151, elapsed=38.1s
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[0]: text=邹城市人民医院, bbox=[375, 35, 623, 62]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告单, bbox=[410, 67, 610, 89]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[414, 102, 448, 116]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[3]: text=温度：28℃, bbox=[672, 100, 754, 113]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[4]: text=住院号：, bbox=[178, 124, 234, 137]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[414, 123, 473, 137]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[6]: text=气压：745mmHg, bbox=[672, 120, 795, 134]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[7]: text=科室：呼吸与危重症医学科门, bbox=[178, 144, 387, 157]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：65岁, bbox=[414, 143, 500, 156]
2026-08-10 13:19:24,089 INFO     29 [qwen-vl-text] coord item[9]: text=检查日期：05/29/25, bbox=[672, 141, 808, 154]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[10]: text=床位号：, bbox=[178, 165, 234, 178]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[11]: text=吸烟：无, bbox=[414, 164, 473, 177]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[12]: text=肺容积：, bbox=[163, 195, 247, 215]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[13]: text=(BTPS), bbox=[300, 195, 357, 208]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[14]: text=用药前, bbox=[638, 187, 688, 200]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[15]: text=用药后, bbox=[761, 182, 811, 195]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[16]: text=预计值：, bbox=[481, 201, 535, 214]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[17]: text=实测值, bbox=[607, 201, 656, 214]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[18]: text=实/预%, bbox=[675, 200, 725, 213]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[19]: text=实测值, bbox=[744, 200, 793, 213]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[20]: text=实/预%改善率, bbox=[814, 198, 912, 211]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[21]: text=肺活量：, bbox=[178, 223, 233, 236]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[22]: text=VC, bbox=[323, 222, 348, 235]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[23]: text=L, bbox=[412, 223, 424, 236]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[24]: text=3.56, bbox=[498, 222, 531, 235]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[25]: text=潮气量：, bbox=[178, 237, 233, 250]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[26]: text=Vt, bbox=[323, 237, 342, 250]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[27]: text=L, bbox=[412, 237, 424, 250]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[28]: text=深吸气量：, bbox=[178, 251, 249, 264]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[29]: text=IC, bbox=[323, 251, 342, 264]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[30]: text=L, bbox=[412, 251, 424, 264]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[31]: text=补呼气量：, bbox=[178, 265, 249, 278]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[32]: text=ERV, bbox=[323, 265, 359, 278]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[33]: text=L, bbox=[412, 265, 424, 278]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[34]: text=残气：, bbox=[178, 279, 215, 291]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[35]: text=RV Sb, bbox=[323, 279, 377, 292]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[36]: text=L, bbox=[412, 279, 424, 292]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[37]: text=2.19, bbox=[498, 279, 531, 292]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[38]: text=功能残气量：, bbox=[178, 292, 265, 305]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[39]: text=FRC N2, bbox=[323, 293, 385, 306]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[40]: text=L, bbox=[412, 293, 424, 306]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[41]: text=3.39, bbox=[498, 293, 531, 306]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[42]: text=肺总量：, bbox=[178, 306, 233, 319]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[43]: text=TLC Sb, bbox=[323, 307, 380, 320]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[44]: text=L, bbox=[412, 307, 424, 320]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[45]: text=5.65, bbox=[498, 307, 531, 320]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[46]: text=残气/肺总量：, bbox=[178, 319, 269, 332]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[47]: text=RV/TLC Sb, bbox=[323, 321, 408, 335]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[48]: text=%, bbox=[412, 320, 428, 333]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[49]: text=39, bbox=[512, 322, 531, 335]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[50]: text=通气功能：, bbox=[178, 351, 285, 370]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[51]: text=用力肺活量：, bbox=[178, 376, 265, 389]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[52]: text=FVC, bbox=[323, 376, 357, 389]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[53]: text=L, bbox=[412, 377, 424, 390]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[54]: text=3.56, bbox=[498, 376, 531, 389]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[55]: text=2.90, bbox=[615, 376, 649, 389]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[56]: text=81, bbox=[689, 376, 707, 389]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[57]: text=3.24, bbox=[735, 376, 768, 389]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[58]: text=91, bbox=[808, 376, 827, 389]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[59]: text=12, bbox=[870, 376, 889, 389]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[60]: text=用力呼气一秒量：, bbox=[178, 390, 299, 403]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[61]: text=FEV1, bbox=[323, 390, 364, 403]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[62]: text=L, bbox=[412, 391, 424, 404]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[63]: text=2.77, bbox=[498, 390, 531, 403]
2026-08-10 13:19:24,090 INFO     29 [qwen-vl-text] coord item[64]: text=1.45, bbox=[615, 390, 649, 403]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[65]: text=52, bbox=[689, 390, 707, 403]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[66]: text=1.65, bbox=[735, 390, 768, 403]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[67]: text=60, bbox=[808, 390, 827, 403]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[68]: text=14, bbox=[870, 390, 889, 403]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[69]: text=用力呼气一秒率：, bbox=[178, 404, 299, 417]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[70]: text=FEV1/FVC, bbox=[323, 404, 404, 417]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[71]: text=%, bbox=[412, 405, 428, 418]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[72]: text=80, bbox=[512, 404, 531, 417]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[73]: text=50, bbox=[628, 404, 649, 417]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[74]: text=63, bbox=[689, 404, 707, 417]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[75]: text=51, bbox=[747, 404, 768, 417]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[76]: text=64, bbox=[808, 404, 827, 417]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[77]: text=2, bbox=[877, 404, 889, 417]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[78]: text=用力呼气中期流速：, bbox=[178, 418, 317, 431]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[79]: text=FEF25-75%L/sec, bbox=[323, 418, 454, 431]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[80]: text=2.85, bbox=[498, 418, 531, 431]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[81]: text=0.70, bbox=[615, 418, 649, 431]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[82]: text=25, bbox=[689, 418, 707, 431]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[83]: text=0.76, bbox=[735, 418, 768, 431]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[84]: text=27, bbox=[808, 418, 827, 431]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[85]: text=8, bbox=[877, 418, 889, 431]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[86]: text=25%用力呼气流速：, bbox=[178, 432, 317, 445]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[87]: text=FEF25%, bbox=[323, 432, 387, 445]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[88]: text=L/sec, bbox=[412, 433, 454, 446]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[89]: text=6.85, bbox=[498, 432, 531, 445]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[90]: text=1.58, bbox=[615, 432, 649, 445]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[91]: text=23, bbox=[689, 432, 707, 445]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[92]: text=2.00, bbox=[735, 432, 768, 445]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[93]: text=29, bbox=[808, 432, 827, 445]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[94]: text=27, bbox=[868, 432, 889, 445]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[95]: text=50%用力呼气流速：, bbox=[178, 446, 317, 459]
2026-08-10 13:19:24,091 INFO     29 [qwen-vl-text] coord item[96]: text=FEF50%, bbox=[323, 446, 387, 459]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[97]: text=L/sec, bbox=[412, 447, 454, 460]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[98]: text=3.57, bbox=[498, 446, 531, 459]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[99]: text=0.82, bbox=[615, 446, 649, 459]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[100]: text=23, bbox=[689, 446, 707, 459]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[101]: text=0.91, bbox=[735, 446, 768, 459]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[102]: text=25, bbox=[808, 446, 827, 459]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[103]: text=11, bbox=[870, 446, 889, 459]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[104]: text=75%用力呼气流速：, bbox=[178, 460, 317, 473]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[105]: text=FEF75%, bbox=[323, 460, 387, 473]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[106]: text=L/sec, bbox=[412, 461, 454, 474]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[107]: text=1.23, bbox=[498, 460, 531, 473]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[108]: text=0.34, bbox=[615, 460, 649, 473]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[109]: text=28, bbox=[689, 460, 707, 473]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[110]: text=0.39, bbox=[735, 460, 768, 473]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[111]: text=32, bbox=[808, 460, 827, 473]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[112]: text=13, bbox=[870, 460, 889, 473]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[113]: text=峰值流速, bbox=[178, 473, 243, 486]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[114]: text=PEF, bbox=[323, 474, 356, 487]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[115]: text=L/sec, bbox=[412, 475, 454, 488]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[116]: text=7.51, bbox=[498, 474, 531, 487]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[117]: text=2.72, bbox=[615, 474, 649, 487]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[118]: text=36, bbox=[689, 474, 707, 487]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[119]: text=2.71, bbox=[735, 474, 768, 487]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[120]: text=36, bbox=[808, 474, 827, 487]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[121]: text=-0, bbox=[870, 474, 889, 487]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[122]: text=每分静息通气量：, bbox=[178, 487, 299, 500]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[123]: text=VE, bbox=[323, 488, 346, 501]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[124]: text=L/min, bbox=[412, 488, 454, 501]
2026-08-10 13:19:24,092 INFO     29 [qwen-vl-text] coord item[125]: text=6.8, bbox=[507, 488, 531, 501]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[126]: text=最大自主通气量：, bbox=[178, 500, 299, 513]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[127]: text=MVV, bbox=[323, 501, 360, 514]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[128]: text=L/min, bbox=[412, 501, 454, 514]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[129]: text=121, bbox=[505, 501, 531, 514]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[130]: text=弥散功能, bbox=[178, 532, 277, 551]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[131]: text=CO弥散量：, bbox=[178, 561, 257, 574]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[132]: text=DLCO, bbox=[323, 561, 370, 574]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[133]: text=mL/mmHg/min8.3, bbox=[412, 561, 531, 574]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[134]: text=DLCOexh, bbox=[323, 575, 396, 588]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[135]: text=mL/mmHg/min8.3, bbox=[412, 575, 531, 588]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[136]: text=VA, bbox=[323, 589, 346, 602]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[137]: text=L, bbox=[412, 589, 424, 602]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[138]: text=VA exh, bbox=[323, 603, 383, 616]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[139]: text=L, bbox=[412, 603, 424, 616]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[140]: text=肺泡容积：, bbox=[178, 615, 249, 628]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[141]: text=DLCO/VA, bbox=[323, 616, 396, 629]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[142]: text=mL/mmHg/mi8.68, bbox=[412, 616, 531, 629]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[143]: text=弥散常数：, bbox=[178, 632, 249, 645]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[144]: text=DLexh/VA, bbox=[323, 632, 399, 645]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[145]: text=mL/mmHg/mi8.68, bbox=[412, 632, 531, 645]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[146]: text=结论：, bbox=[180, 666, 231, 683]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[147]: text=中重度阻塞性肺通气功能障碍。, bbox=[178, 696, 400, 709]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[148]: text=支气管舒张试验阳性。, bbox=[178, 710, 339, 723]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[149]: text=此报告仅供临床参考, bbox=[178, 858, 314, 870]
2026-08-10 13:19:24,093 INFO     29 [qwen-vl-text] coord item[150]: text=检查者：, bbox=[370, 857, 428, 870]
2026-08-10 13:19:24,094 INFO     29 [qwen-vl-text] page=1 — 151/151 coords, api_time=38.1s
2026-08-10 13:19:24,094 INFO     29 [qwen-vl-text] new_positions (152):
[[0, 319.515, 408.765, 682.02, 705.596], [1, 223.125, 370.685, 29.47, 52.204], [1, 243.95, 362.95, 56.414, 74.938], [1, 246.32999999999998, 266.56, 85.884, 97.672], [1, 399.84, 448.63, 84.2, 95.146], [1, 105.91, 139.23, 104.408, 115.354], [1, 246.32999999999998, 281.435, 103.566, 115.354], [1, 399.84, 473.025, 101.03999999999999, 112.828], [1, 105.91, 230.265, 121.24799999999999, 132.194], [1, 246.32999999999998, 297.5, 120.40599999999999, 131.352], [1, 399.84, 480.76, 118.722, 129.668], [1, 105.91, 139.23, 138.93, 149.876], [1, 246.32999999999998, 281.435, 138.088, 149.034], [1, 96.985, 146.965, 164.19, 181.03], [1, 178.5, 212.415, 164.19, 175.136], [1, 379.60999999999996, 409.35999999999996, 157.454, 168.4], [1, 452.79499999999996, 482.54499999999996, 153.244, 164.19], [1, 286.195, 318.325, 169.242, 180.188], [1, 361.16499999999996, 390.32, 169.242, 180.188], [1, 401.625, 431.375, 168.4, 179.346], [1, 442.68, 471.835, 168.4, 179.346], [1, 484.33, 542.64, 166.716, 177.662], [1, 105.91, 138.635, 187.766, 198.712], [1, 192.185, 207.06, 186.924, 197.87], [1, 245.14, 252.28, 187.766, 198.712], [1, 296.31, 315.945, 186.924, 197.87], [1, 105.91, 138.635, 199.554, 210.5], [1, 192.185, 203.48999999999998, 199.554, 210.5], [1, 245.14, 252.28, 199.554, 210.5], [1, 105.91, 148.155, 211.34199999999998, 222.28799999999998], [1, 192.185, 203.48999999999998, 211.34199999999998, 222.28799999999998], [1, 245.14, 252.28, 211.34199999999998, 222.28799999999998], [1, 105.91, 148.155, 223.13, 234.076], [1, 192.185, 213.605, 223.13, 234.076], [1, 245.14, 252.28, 223.13, 234.076], [1, 105.91, 127.925, 234.91799999999998, 245.022], [1, 192.185, 224.315, 234.91799999999998, 245.864], [1, 245.14, 252.28, 234.91799999999998, 245.864], [1, 296.31, 315.945, 234.91799999999998, 245.864], [1, 105.91, 157.67499999999998, 245.864, 256.81], [1, 192.185, 229.075, 246.706, 257.652], [1, 245.14, 252.28, 246.706, 257.652], [1, 296.31, 315.945, 246.706, 257.652], [1, 105.91, 138.635, 257.652, 268.598], [1, 192.185, 226.1, 258.49399999999997, 269.44], [1, 245.14, 252.28, 258.49399999999997, 269.44], [1, 296.31, 315.945, 258.49399999999997, 269.44], [1, 105.91, 160.055, 268.598, 279.544], [1, 192.185, 242.76, 270.282, 282.07], [1, 245.14, 254.66, 269.44, 280.38599999999997], [1, 304.64, 315.945, 271.12399999999997, 282.07], [1, 105.91, 169.575, 295.542, 311.53999999999996], [1, 105.91, 157.67499999999998, 316.592, 327.538], [1, 192.185, 212.415, 316.592, 327.538], [1, 245.14, 252.28, 317.43399999999997, 328.38], [1, 296.31, 315.945, 316.592, 327.538], [1, 365.925, 386.155, 316.592, 327.538], [1, 409.955, 420.66499999999996, 316.592, 327.538], [1, 437.325, 456.96, 316.592, 327.538], [1, 480.76, 492.065, 316.592, 327.538], [1, 517.65, 528.9549999999999, 316.592, 327.538], [1, 105.91, 177.905, 328.38, 339.32599999999996], [1, 192.185, 216.57999999999998, 328.38, 339.32599999999996], [1, 245.14, 252.28, 329.222, 340.168], [1, 296.31, 315.945, 328.38, 339.32599999999996], [1, 365.925, 386.155, 328.38, 339.32599999999996], [1, 409.955, 420.66499999999996, 328.38, 339.32599999999996], [1, 437.325, 456.96, 328.38, 339.32599999999996], [1, 480.76, 492.065, 328.38, 339.32599999999996], [1, 517.65, 528.9549999999999, 328.38, 339.32599999999996], [1, 105.91, 177.905, 340.168, 351.114], [1, 192.185, 240.38, 340.168, 351.114], [1, 245.14, 254.66, 341.01, 351.95599999999996], [1, 304.64, 315.945, 340.168, 351.114], [1, 373.65999999999997, 386.155, 340.168, 351.114], [1, 409.955, 420.66499999999996, 340.168, 351.114], [1, 444.465, 456.96, 340.168, 351.114], [1, 480.76, 492.065, 340.168, 351.114], [1, 521.8149999999999, 528.9549999999999, 340.168, 351.114], [1, 105.91, 188.61499999999998, 351.95599999999996, 362.902], [1, 192.185, 270.13, 351.95599999999996, 362.902], [1, 296.31, 315.945, 351.95599999999996, 362.902], [1, 365.925, 386.155, 351.95599999999996, 362.902], [1, 409.955, 420.66499999999996, 351.95599999999996, 362.902], [1, 437.325, 456.96, 351.95599999999996, 362.902], [1, 480.76, 492.065, 351.95599999999996, 362.902], [1, 521.8149999999999, 528.9549999999999, 351.95599999999996, 362.902], [1, 105.91, 188.61499999999998, 363.74399999999997, 374.69], [1, 192.185, 230.265, 363.74399999999997, 374.69], [1, 245.14, 270.13, 364.586, 375.532], [1, 296.31, 315.945, 363.74399999999997, 374.69], [1, 365.925, 386.155, 363.74399999999997, 374.69], [1, 409.955, 420.66499999999996, 363.74399999999997, 374.69], [1, 437.325, 456.96, 363.74399999999997, 374.69], [1, 480.76, 492.065, 363.74399999999997, 374.69], [1, 516.4599999999999, 528.9549999999999, 363.74399999999997, 374.69], [1, 105.91, 188.61499999999998, 375.532, 386.478], [1, 192.185, 230.265, 375.532, 386.478], [1, 245.14, 270.13, 376.37399999999997, 387.32], [1, 296.31, 315.945, 375.532, 386.478], [1, 365.925, 386.155, 375.532, 386.478], [1, 409.955, 420.66499999999996, 375.532, 386.478], [1, 437.325, 456.96, 375.532, 386.478], [1, 480.76, 492.065, 375.532, 386.478], [1, 517.65, 528.9549999999999, 375.532, 386.478], [1, 105.91, 188.61499999999998, 387.32, 398.26599999999996], [1, 192.185, 230.265, 387.32, 398.26599999999996], [1, 245.14, 270.13, 388.162, 399.108], [1, 296.31, 315.945, 387.32, 398.26599999999996], [1, 365.925, 386.155, 387.32, 398.26599999999996], [1, 409.955, 420.66499999999996, 387.32, 398.26599999999996], [1, 437.325, 456.96, 387.32, 398.26599999999996], [1, 480.76, 492.065, 387.32, 398.26599999999996], [1, 517.65, 528.9549999999999, 387.32, 398.26599999999996], [1, 105.91, 144.58499999999998, 398.26599999999996, 409.212], [1, 192.185, 211.82, 399.108, 410.054], [1, 245.14, 270.13, 399.95, 410.89599999999996], [1, 296.31, 315.945, 399.108, 410.054], [1, 365.925, 386.155, 399.108, 410.054], [1, 409.955, 420.66499999999996, 399.108, 410.054], [1, 437.325, 456.96, 399.108, 410.054], [1, 480.76, 492.065, 399.108, 410.054], [1, 517.65, 528.9549999999999, 399.108, 410.054], [1, 105.91, 177.905, 410.054, 421.0], [1, 192.185, 205.87, 410.89599999999996, 421.842], [1, 245.14, 270.13, 410.89599999999996, 421.842], [1, 301.66499999999996, 315.945, 410.89599999999996, 421.842], [1, 105.91, 177.905, 421.0, 431.94599999999997], [1, 192.185, 214.2, 421.842, 432.788], [1, 245.14, 270.13, 421.842, 432.788], [1, 300.47499999999997, 315.945, 421.842, 432.788], [1, 105.91, 164.815, 447.94399999999996, 463.942], [1, 105.91, 152.915, 472.36199999999997, 483.308], [1, 192.185, 220.14999999999998, 472.36199999999997, 483.308], [1, 245.14, 315.945, 472.36199999999997, 483.308], [1, 192.185, 235.61999999999998, 484.15, 495.096], [1, 245.14, 315.945, 484.15, 495.096], [1, 192.185, 205.87, 495.938, 506.88399999999996], [1, 245.14, 252.28, 495.938, 506.88399999999996], [1, 192.185, 227.885, 507.726, 518.672], [1, 245.14, 252.28, 507.726, 518.672], [1, 105.91, 148.155, 517.8299999999999, 528.776], [1, 192.185, 235.61999999999998, 518.672, 529.6179999999999], [1, 245.14, 315.945, 518.672, 529.6179999999999], [1, 105.91, 148.155, 532.144, 543.09], [1, 192.185, 237.405, 532.144, 543.09], [1, 245.14, 315.945, 532.144, 543.09], [1, 107.1, 137.445, 560.7719999999999, 575.086], [1, 105.91, 238.0, 586.0319999999999, 596.978], [1, 105.91, 201.70499999999998, 597.8199999999999, 608.766], [1, 105.91, 186.82999999999998, 722.4359999999999, 732.54], [1, 220.14999999999998, 254.66, 721.5939999999999, 732.54]]
2026-08-10 13:19:24,094 INFO     29 [qwen-vl-text] ═══ DONE ═══ 152 positions, pages=2, time=46.5s
2026-08-10 13:19:24,108 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:19:24,108 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:19:24,108 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:19:24,109 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:19:24.109+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 44, "failed": 0, "current": {"e97265da94bd11f1bd9827cf206dfa2d": {"id": "e97265da94bd11f1bd9827cf206dfa2d", "doc_id": "e9284be494bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZZYU \u7537 65\u5c81 \u63a8\u6d4e\u5357(1).pdf", "type": "pdf", "location": "ZZYU \u7537 65\u5c81 \u63a8\u6d4e\u5357(1).pdf", "size": 756692, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367881156, "task_type": "dataflow", "root_trace_id": "7b4a5c76667c474a9c93698057034643", "root_traceparent": "00-7b4a5c76667c474a9c93698057034643-1740e57c2225b187-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:19:24,118 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:19:24,119 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:19:25,038 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:19:25,049 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:19:25,049 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "177 items", "markdown": "", "text": "", "name": "ZZYU 男 65岁 推济南(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:19:25,049 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:19:25,050 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:19:25,061 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:19:25,061 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "ZZYU 男 65岁 推济南(1).pdf"}
2026-08-10 13:19:25,061 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:19:25,092 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786367883905, 'update_date': datetime.datetime(2026, 8, 10, 13, 18, 3), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1033549, 'status': '1'}
2026-08-10 13:19:25,317 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=邹城市人民医院
门诊病历
性别：男性
年龄：65岁
科室：呼吸与危重症医学科(千泉门诊)
ID号
就诊时间：2025-05-29 10:06
主诉：阵发性憋喘60年。
现病史：阵发性憋喘60年，遇冷空气时加重，时咳嗽、咳少量白痰，时有
心慌、胸闷、气短，无胸痛，无恶心、呕吐，无腹痛、无腹泻，在院外未治疗，
症状时好时坏，来诊。
既往史：平素身体健康，否认高血压、冠心病、糖尿病史。否认病毒性肝
炎、肺结核等传染病史及密切接触史。
过敏史：否认药物过敏史。
体格检查：神志清、精神可，胸廓无畸形，双肺呼吸音清，未闻及干湿
啰音，心率75次/分，心律齐，无杂音，双下肢无水肿。
辅助检查：
诊断：喘憋（主诊断）
诊疗意见：
避免受凉感冒，避免过度劳累，如有不适，及时就诊。
☑已向患者(家属)进行了关于患者病情、目前状况及诊疗方案的教育。
☑已向患者(家属)交代了各种诊疗方案的效果和不遵从医嘱可能导致的后果。
医生签名：
门诊部
(1)
---
708833003930
邹城市人民医院
肺功能检查报告单
姓名
温度：28℃
住院号：
性别：男
气压：745mmHg
科室：呼吸与危重症医学科门
年龄：65岁
检查日期：05/29/25
床位号：
吸烟：无
肺容积：
(BTPS)
用药前
用药后
预计值：
实测值
实/预%
实测值
实/预%改善率
肺活量：
VC
L
3.56
潮气量：
Vt
L
深吸气量：
IC
L
补呼气量：
ERV
L
残气：
RV Sb
L
2.19
功能残气量：
FRC N2
L
3.39
肺总量：
TLC Sb
L
5.65
残气/肺总量：
RV/TLC Sb
%
39
通气功能：
用力肺活量：
FVC
L
3.56
2.90
81
3.24
91
12
用力呼气一秒量：
FEV1
L
2.77
1.45
52
1.65
60
14
用力呼气一秒率：
FEV1/FVC
%
80
50
63
51
64
2
用力呼气中期流速：
FEF25-75%L/sec
2.85
0.70
25
0.76
27
8
25%用力呼气流速：
FEF25%
L/sec
6.85
1.58
23
2.00
29
27
50%用力呼气流速：
FEF50%
L/sec
3.57
0.82
23
0.91
25
11
75%用力呼气流速：
FEF75%
L/sec
1.23
0.34
28
0.39
32
13
峰值流速
PEF
L/sec
7.51
2.72
36
2.71
36
-0
每分静息通气量：
VE
L/min
6.8
最大自主通气量：
MVV
L/min
121
弥散功能
CO弥散量：
DLCO
mL/mmHg/min8.3
DLCOexh
mL/mmHg/min8.3
VA
L
VA exh
L
肺泡容积：
DLCO/VA
mL/mmHg/mi8.68
弥散常数：
DLexh/VA
mL/mmHg/mi8.68
结论：
中重度阻塞性肺通气功能障碍。
支气管舒张试验阳性。
此报告仅供临床参考
检查者：
2026-08-10 13:19:25,502 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:19:25,502 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "ZZYU 男 65岁 推济南(1).pdf", "embedding_token_consumption": 1009}
2026-08-10 13:19:25,502 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:19:25,601 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:19:25,601 INFO     29 [Trace] task=e97265da | doc=ZZYU 男 65岁 推济南(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:19:25,603 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:19:25,603 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:19:25,607 INFO     29 set_progress(e97265da94bd11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:19:25 [DOC Engine]:
Start to index...
2026-08-10 13:19:25,619 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 13:19:25,624 INFO     29 set_progress(e97265da94bd11f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 13:19:25,630 INFO     29 set_progress(e97265da94bd11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:19:25 Indexing done (0.02s). Task done (77.50s)
2026-08-10 13:19:25,633 INFO     29 [Done], chunks(2), token(1009), elapsed:77.50
2026-08-10 13:19:25,689 INFO     29 handle_task done for task {"id": "e97265da94bd11f1bd9827cf206dfa2d", "doc_id": "e9284be494bd11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZZYU \u7537 65\u5c81 \u63a8\u6d4e\u5357(1).pdf", "type": "pdf", "location": "ZZYU \u7537 65\u5c81 \u63a8\u6d4e\u5357(1).pdf", "size": 756692, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786367881156, "task_type": "dataflow", "root_trace_id": "7b4a5c76667c474a9c93698057034643", "root_traceparent": "00-7b4a5c76667c474a9c93698057034643-1740e57c2225b187-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
