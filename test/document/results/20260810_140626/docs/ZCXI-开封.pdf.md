# 基准结果：ZCXI-开封.pdf

## 基本信息

- 文件：`ZCXI-开封.pdf`
- 大小：3073.1 KB
- PDF 总页数：2
- doc_id：`534cda0a948511f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T14:32:56  完成时间：2026-08-10T14:35:06  耗时：130.4s
- progress_msg：`06:34:32 Indexing done (0.06s). Task done (92.62s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

**该文档没有任何 chunk（文档级被过滤或解析失败）**

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
- ChunkMerger：`{"found": true, "merged": 2, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 06:34:30,645 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 06:32:58,913 INFO     29 handle_task begin for task {"id": "53ddf620948511f1bd9827cf206dfa2d", "doc_id": "534cda0a948511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZCXI-\u5f00\u5c01.pdf", "type": "pdf", "location": "ZCXI-\u5f00\u5c01.pdf", "size": 3146880, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343578385, "task_type": "dataflow", "root_trace_id": "02484dfe91b54a019343dc11c0957c86", "root_traceparent": "00-02484dfe91b54a019343dc11c0957c86-3aa2f469fae54a9d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 06:32:59,123 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 06:32:59,243 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 06:32:59,256 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:32:59,256 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 06:32:59,256 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 06:32:59,271 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 06:32:59,271 INFO     29 ============================================================
2026-08-10 06:32:59,271 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 06:32:59,271 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 06:32:59,271 INFO     29 ============================================================
2026-08-10 06:32:59,272 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 06:32:59,272 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 06:32:59,277 INFO     29 No torch found.
2026-08-10 06:32:59,958 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=2
2026-08-10 06:33:00,330 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2201971, prompt_len=764
2026-08-10 06:33:01,984 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-29"}
```
2026-08-10 06:33:01,986 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-05-29
2026-08-10 06:33:02,006 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2201971, prompt_len=401
2026-08-10 06:33:08,271 INFO     29 [qwen-vl-parser] text API response (len=947):
["国家呼吸医疗质量控制中心标准化门诊病历", "哮喘复诊(简化版)", "门诊号:2505048587", "□复诊:□预约", "就诊日期:2025-05-2912:19:36", "就诊科室:呼吸与危重症医学科", "姓名", "性别:男", "年龄:58岁", "联系人:本人", "联系电话:", "T:36.5℃", "P:70次/分", "R:19次/分", "BP:120/60mmHg", "处方□检查□检验□医疗医嘱", "主诉:反复咳嗽、胸闷半年", "现病史:半年前反复发作咳嗽、胸闷,就诊于我院查肺功能结构提示支气管舒张实验阳性,考虑支气管", "哮喘,予以吸入ICS+LABA治疗后症状好转,仍反复发作。未规律用药,现为求复查入院。", "本次门诊距上次门诊间隔时间半年", "质控相关内容填写:", "症状控制情况:", "□良好控制(无勾选)√部分控制(勾线1-2项)□未控制(勾选3-4项)", "过去4周,患者:□夜间因哮喘憋醒;□日间哮喘症状>2次/周;", "√哮喘引起的活动受限□使用缓解药SABA次数>2次/周;", "吸入药物使用情况:□超量使用;□遵医嘱使用;□减量使用;√按需使用;□未使用;", "吸入装置使用情况:√正确□不正确", "急性发作情况:两次就诊期间急性发作:√否□是,发作次数", "过敏药物名称:无", "既往史:无", "既往检查检验:无", "个人史:", "吸烟史:无,年烟龄,支/天,戒烟,已戒年。", "查体:", "吸入ICS的患者检查口腔粘膜√是□否", "<西医诊断>", "1.支气管哮喘", "辅助检查:", "本次治疗方案:□升级√维持□降级□停药", "处方:", "质控相关内容填写:", "□吸入治疗:□按需ICS-福莫特罗□按需SABA□低剂量ICS□低剂量ICS+LABA", "□高剂量ICS+LABA√低剂量ICS+LABA□LAMA□其他", "□白三烯调节剂", "□茶碱", "□口服激素", "□靶向治疗:□抗IgE单抗□抗IL-5/5R单抗□抗TSLP单抗", "□其他", "□脱敏治疗", "□其他", "□吸入装置的评估和培训", "其他处理:", "医师签名:黄志昂"]
2026-08-10 06:33:08,272 INFO     29 [qwen-vl-parser] page=1 text: 53 lines (bbox 0-52)
2026-08-10 06:33:08,272 INFO     29 [qwen-vl-parser] page=1 text: 53 sections
2026-08-10 06:33:08,561 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1511639, prompt_len=764
2026-08-10 06:33:10,371 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-10-19"}
```
2026-08-10 06:33:10,372 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2024-10-19
2026-08-10 06:33:10,384 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1511639, prompt_len=401
2026-08-10 06:33:16,860 INFO     29 [qwen-vl-parser] text API response (len=992):
["河南大学第一附属医院", "肺功能测试", "姓名:", "体重: 64.00", "性别: Male", "ID: ", "身高: 166.00", "种族: Asian", "BSA: 1.71", "年龄: 58", "日期: 2024/10/19", "床号:", "结论: 中重度混合性通气功能障碍", "支气管舒张试验阳性", "签名: 王学会", "审核:", "Pre-Bronch", "Post-Bronch", "ctual Pred %Pred", "Actual %Pred %Chng", "---- 肺通气 ----", "FVC (L) 2.31 3.67 62 2.98 81 +29", "FEV1 (L) 1.49 2.92 51 1.89 64 +26", "FEV1/FVC (%) 65 79 81 63 80 -2", "FEF 25% (L/sec) 2.29 6.49 35 3.46 53 +50", "FEF 50% (L/sec) 1.07 4.26 25 1.93 45 +80", "FEF 75% (L/sec) 0.35 0.81 43 0.93 114 +166", "FEF 25-75% (L/s 0.83 2.61 31 1.72 66 +107", "FIF Max (L/sec) 2.46 1.90 -22", "FEF Max (L/sec) 3.70 4.03 +8", "Back Extrapol Vol 0.04 0.06 +37", "---- 肺活量 ----", "SVC (L) 2.21 3.67 60", "IC (L) 1.74 2.68 65", "ERV (L) 0.46 1.34 34", "6", "4", "2", "0", "-2", "-4", "-6", "6", "4", "2", "0", "-2", "-4", "-6", "1 2 3", "1 2 3", "08:44:26", "0", "5", "10", "15", "20", "25", "30", "6", "5", "4", "3", "2", "1", "0", "20", "15", "10", "5", "0", "0 1 2 3 4 5 6 7 8 9 10 11 12"]
2026-08-10 06:33:16,860 INFO     29 [qwen-vl-parser] page=2 text: 72 lines (bbox 53-124)
2026-08-10 06:33:16,860 INFO     29 [qwen-vl-parser] page=2 text: 72 sections
2026-08-10 06:33:16,861 INFO     29 [qwen-vl-parser] parse_pdf done: 125 sections from 2 pages.
2026-08-10 06:33:16,875 INFO     29 Close text detector.
2026-08-10 06:33:17,401 INFO     29 Close text recognizer.
2026-08-10 06:33:17,800 INFO     29 Close recognizer.
2026-08-10 06:33:18,190 INFO     29 Close recognizer.
2026-08-10 06:33:18,923 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 06:33:18,923 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Parser:MedLink | outputs={"html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "json"}
2026-08-10 06:33:18,923 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 06:33:18,958 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:18,958 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 国家呼吸医疗质量控制中心标准化门诊病历\n[BBOX-1] 哮喘复诊(简化版)\n[BBOX-2] 门诊号:2505048587\n[BBOX-3] □复诊:□预约\n[BBOX-4] 就诊日期:2025-05-2912:19:36\n[BBOX-5] 就诊科室:呼吸与危重症医学科\n[BBOX-6] 姓名\n[BBOX-7] 性别:男\n[BBOX-8] 年龄:58岁\n[BBOX-9] 联系人:本人\n[BBOX-10] 联系电话:\n[BBOX-11] T:36.5℃\n[BBOX-12] P:70次/分\n[BBOX-13] R:19次/分\n[BBOX-14] BP:120/60mmHg\n[BBOX-15] 处方□检查□检验□医疗医嘱\n[BBOX-16] 主诉:反复咳嗽、胸闷半年\n[BBOX-17] 现病史:半年前反复发作咳嗽、胸闷,就诊于我院查肺功能结构提示支气管舒张实验阳性,考虑支气管\n[BBOX-18] 哮喘,予以吸入ICS+LABA治疗后症状好转,仍反复发作。未规律用药,现为求复查入院。\n[BBOX-19] 本次门诊距上次门诊间隔时间半年\n[BBOX-20] 质控相关内容填写:\n[BBOX-21] 症状控制情况:\n[BBOX-22] □良好控制(无勾选)√部分控制(勾线1-2项)□未控制(勾选3-4项)\n[BBOX-23] 过去4周,患者:□夜间因哮喘憋醒;□日间哮喘症状>2次/周;\n[BBOX-24] √哮喘引起的活动受限□使用缓解药SABA次数>2次/周;\n[BBOX-25] 吸入药物使用情况:□超量使用;□遵医嘱使用;□减量使用;√按需使用;□未使用;\n[BBOX-26] 吸入装置使用情况:√正确□不正确\n[BBOX-27] 急性发作情况:两次就诊期间急性发作:√否□是,发作次数\n[BBOX-28] 过敏药物名称:无\n[BBOX-29] 既往史:无\n[BBOX-30] 既往检查检验:无\n[BBOX-31] 个人史:\n[BBOX-32] 吸烟史:无,年烟龄,支/天,戒烟,已戒年。\n[BBOX-33] 查体:\n[BBOX-34] 吸入ICS的患者检查口腔粘膜√是□否\n[BBOX-35] <西医诊断>\n[BBOX-36] 1.支气管哮喘\n[BBOX-37] 辅助检查:\n[BBOX-38] 本次治疗方案:□升级√维持□降级□停药\n[BBOX-39] 处方:\n[BBOX-40] 质控相关内容填写:\n[BBOX-41] □吸入治疗:□按需ICS-福莫特罗□按需SABA□低剂量ICS□低剂量ICS+LABA\n[BBOX-42] □高剂量ICS+LABA√低剂量ICS+LABA□LAMA□其他\n[BBOX-43] □白三烯调节剂\n[BBOX-44] □茶碱\n[BBOX-45] □口服激素\n[BBOX-46] □靶向治疗:□抗IgE单抗□抗IL-5/5R单抗□抗TSLP单抗\n[BBOX-47] □其他\n[BBOX-48] □脱敏治疗\n[BBOX-49] □其他\n[BBOX-50] □吸入装置的评估和培训\n[BBOX-51] 其他处理:\n[BBOX-52] 医师签名:黄志昂\n[BBOX-53] 河南大学第一附属医院\n[BBOX-54] 肺功能测试\n[BBOX-55] 姓名:\n[BBOX-56] 体重: 64.00\n[BBOX-57] 性别: Male\n[BBOX-58] ID:\n[BBOX-59] 身高: 166.00\n[BBOX-60] 种族: Asian\n[BBOX-61] BSA: 1.71\n[BBOX-62] 年龄: 58\n[BBOX-63] 日期: 2024/10/19\n[BBOX-64] 床号:\n[BBOX-65] 结论: 中重度混合性通气功能障碍\n[BBOX-66] 支气管舒张试验阳性\n[BBOX-67] 签名: 王学会\n[BBOX-68] 审核:\n[BBOX-69] Pre-Bronch\n[BBOX-70] Post-Bronch\n[BBOX-71] ctual Pred %Pred\n[BBOX-72] Actual %Pred %Chng\n[BBOX-73] ---- 肺通气 ----\n[BBOX-74] FVC (L) 2.31 3.67 62 2.98 81 +29\n[BBOX-75] FEV1 (L) 1.49 2.92 51 1.89 64 +26\n[BBOX-76] FEV1/FVC (%) 65 79 81 63 80 -2\n[BBOX-77] FEF 25% (L/sec) 2.29 6.49 35 3.46 53 +50\n[BBOX-78] FEF 50% (L/sec) 1.07 4.26 25 1.93 45 +80\n[BBOX-79] FEF 75% (L/sec) 0.35 0.81 43 0.93 114 +166\n[BBOX-80] FEF 25-75% (L/s 0.83 2.61 31 1.72 66 +107\n[BBOX-81] FIF Max (L/sec) 2.46 1.90 -22\n[BBOX-82] FEF Max (L/sec) 3.70 4.03 +8\n[BBOX-83] Back Extrapol Vol 0.04 0.06 +37\n[BBOX-84] ---- 肺活量 ----\n[BBOX-85] SVC (L) 2.21 3.67 60\n[BBOX-86] IC (L) 1.74 2.68 65\n[BBOX-87] ERV (L) 0.46 1.34 34\n[BBOX-88] 6\n[BBOX-89] 4\n[BBOX-90] 2\n[BBOX-91] 0\n[BBOX-92] -2\n[BBOX-93] -4\n[BBOX-94] -6\n[BBOX-95] 6\n[BBOX-96] 4\n[BBOX-97] 2\n[BBOX-98] 0\n[BBOX-99] -2\n[BBOX-100] -4\n[BBOX-101] -6\n[BBOX-102] 1 2 3\n[BBOX-103] 1 2 3\n[BBOX-104] 08:44:26\n[BBOX-105] 0\n[BBOX-106] 5\n[BBOX-107] 10\n[BBOX-108] 15\n[BBOX-109] 20\n[BBOX-110] 25\n[BBOX-111] 30\n[BBOX-112] 6\n[BBOX-113] 5\n[BBOX-114] 4\n[BBOX-115] 3\n[BBOX-116] 2\n[BBOX-117] 1\n[BBOX-118] 0\n[BBOX-119] 20\n[BBOX-120] 15\n[BBOX-121] 10\n[BBOX-122] 5\n[BBOX-123] 0\n[BBOX-124] 0 1 2 3 4 5 6 7 8 9 10 11 12"
  }
]
2026-08-10 06:33:22,229 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:33:22.227+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 7, "failed": 0, "current": {"53ddf620948511f1bd9827cf206dfa2d": {"id": "53ddf620948511f1bd9827cf206dfa2d", "doc_id": "534cda0a948511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZCXI-\u5f00\u5c01.pdf", "type": "pdf", "location": "ZCXI-\u5f00\u5c01.pdf", "size": 3146880, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343578385, "task_type": "dataflow", "root_trace_id": "02484dfe91b54a019343dc11c0957c86", "root_traceparent": "00-02484dfe91b54a019343dc11c0957c86-3aa2f469fae54a9d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:33:25,333 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:25,373 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 1}
2026-08-10 06:33:25,387 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 06:33:25,387 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 06:33:25,387 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 06:33:25,387 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 1}
2026-08-10 06:33:25,402 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 06:33:25,403 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | ChunkRouter:Router | outputs={"html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:33:25,403 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 06:33:25,409 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:25,409 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:33:26,678 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:26,684 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 06:33:26,685 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:33:26,685 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 06:33:26,690 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:26,690 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:33:27,737 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:27,747 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 06:33:27,747 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:33:27,748 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 06:33:27,757 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:33:27,758 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:33:27,758 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 06:33:27,758 INFO     29 [qwen-vl-text] positions(53): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:33:27,759 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [53]
2026-08-10 06:33:28,029 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:33:28,029 INFO     29 [qwen-vl-text] LLM extraction start, text_len=787
2026-08-10 06:33:28,030 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:28,030 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 52, \"encounter_dates\": [\"2025-05-29\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "国家呼吸医疗质量控制中心标准化门诊病历\n哮喘复诊(简化版)\n门诊号:2505048587\n□复诊:□预约\n就诊日期:2025-05-2912:19:36\n就诊科室:呼吸与危重症医学科\n姓名\n性别:男\n年龄:58岁\n联系人:本人\n联系电话:\nT:36.5℃\nP:70次/分\nR:19次/分\nBP:120/60mmHg\n处方□检查□检验□医疗医嘱\n主诉:反复咳嗽、胸闷半年\n现病史:半年前反复发作咳嗽、胸闷,就诊于我院查肺功能结构提示支气管舒张实验阳性,考虑支气管\n哮喘,予以吸入ICS+LABA治疗后症状好转,仍反复发作。未规律用药,现为求复查入院。\n本次门诊距上次门诊间隔时间半年\n质控相关内容填写:\n症状控制情况:\n□良好控制(无勾选)√部分控制(勾线1-2项)□未控制(勾选3-4项)\n过去4周,患者:□夜间因哮喘憋醒;□日间哮喘症状>2次/周;\n√哮喘引起的活动受限□使用缓解药SABA次数>2次/周;\n吸入药物使用情况:□超量使用;□遵医嘱使用;□减量使用;√按需使用;□未使用;\n吸入装置使用情况:√正确□不正确\n急性发作情况:两次就诊期间急性发作:√否□是,发作次数\n过敏药物名称:无\n既往史:无\n既往检查检验:无\n个人史:\n吸烟史:无,年烟龄,支/天,戒烟,已戒年。\n查体:\n吸入ICS的患者检查口腔粘膜√是□否\n<西医诊断>\n1.支气管哮喘\n辅助检查:\n本次治疗方案:□升级√维持□降级□停药\n处方:\n质控相关内容填写:\n□吸入治疗:□按需ICS-福莫特罗□按需SABA□低剂量ICS□低剂量ICS+LABA\n□高剂量ICS+LABA√低剂量ICS+LABA□LAMA□其他\n□白三烯调节剂\n□茶碱\n□口服激素\n□靶向治疗:□抗IgE单抗□抗IL-5/5R单抗□抗TSLP单抗\n□其他\n□脱敏治疗\n□其他\n□吸入装置的评估和培训\n其他处理:\n医师签名:黄志昂",
    "role": "user"
  }
]
2026-08-10 06:33:29,744 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:29,744 INFO     29 [qwen-vl-text] LLM output (len=263):
{
  "encounter_date": "2025-05-29",
  "chief_complaint": "反复咳嗽、胸闷半年",
  "present_illness": "半年前反复发作咳嗽、胸闷,就诊于我院查肺功能结构提示支气管舒张实验阳性,考虑支气管哮喘,予以吸入ICS+LABA治疗后症状好转,仍反复发作。未规律用药,现为求复查入院。",
  "past_history": "无",
  "diagnosis": "1.支气管哮喘",
  "treatment_plan": "低剂量ICS+LABA"
}
2026-08-10 06:33:29,744 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-29]
2026-08-10 06:33:29,749 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2876832, prompt_len=1559
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共53行）
["国家呼吸医疗质量控制中心标准化门诊病历", "哮喘复诊(简化版)", "门诊号:2505048587", "□复诊:□预约", "就诊日期:2025-05-2912:19:36", "就诊科室:呼吸与危重症医学科", "姓名", "性别:男", "年龄:58岁", "联系人:本人", "联系电话:", "T:36.5℃", "P:70次/分", "R:19次/分", "BP:120/60mmHg", "处方□检查□检验□医疗医嘱", "主诉:反复咳嗽、胸闷半年", "现病史:半年前反复发作咳嗽、胸闷,就诊于我院查肺功能结构提示支气管舒张实验阳性,考虑支气管", "哮喘,予以吸入ICS+LABA治疗后症状好转,仍反复发作。未规律用药,现为求复查入院。", "本次门诊距上次门诊间隔时间半年", "质控相关内容填写:", "症状控制情况:", "□良好控制(无勾选)√部分控制(勾线1-2项)□未控制(勾选3-4项)", "过去4周,患者:□夜间因哮喘憋醒;□日间哮喘症状>2次/周;", "√哮喘引起的活动受限□使用缓解药SABA次数>2次/周;", "吸入药物使用情况:□超量使用;□遵医嘱使用;□减量使用;√按需使用;□未使用;", "吸入装置使用情况:√正确□不正确", "急性发作情况:两次就诊期间急性发作:√否□是,发作次数", "过敏药物名称:无", "既往史:无", "既往检查检验:无", "个人史:", "吸烟史:无,年烟龄,支/天,戒烟,已戒年。", "查体:", "吸入ICS的患者检查口腔粘膜√是□否", "<西医诊断>", "1.支气管哮喘", "辅助检查:", "本次治疗方案:□升级√维持□降级□停药", "处方:", "质控相关内容填写:", "□吸入治疗:□按需ICS-福莫特罗□按需SABA□低剂量ICS□低剂量ICS+LABA", "□高剂量ICS+LABA√低剂量ICS+LABA□LAMA□其他", "□白三烯调节剂", "□茶碱", "□口服激素", "□靶向治疗:□抗IgE单抗□抗IL-5/5R单抗□抗TSLP单抗", "□其他", "□脱敏治疗", "□其他", "□吸入装置的评估和培训", "其他处理:", "医师签名:黄志昂"]

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
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord API raw response (len=3109):
[
	{"text": "国家呼吸医疗质量控制中心标准化门诊病历", "bbox": [309, 84, 716, 100]},
	{"text": "哮喘复诊(简化版)", "bbox": [430, 107, 598, 123]},
	{"text": "门诊号:2505048587", "bbox": [726, 108, 878, 120]},
	{"text": "□复诊:□预约", "bbox": [103, 139, 210, 152]},
	{"text": "就诊日期:2025-05-2912:19:36", "bbox": [283, 140, 527, 152]},
	{"text": "就诊科室:呼吸与危重症医学科", "bbox": [679, 139, 916, 152]},
	{"text": "姓名", "bbox": [107, 163, 140, 175]},
	{"text": "性别:男", "bbox": [283, 162, 350, 175]},
	{"text": "年龄:58岁", "bbox": [395, 162, 478, 175]},
	{"text": "联系人:本人", "bbox": [531, 162, 629, 175]},
	{"text": "联系电话:", "bbox": [714, 162, 789, 175]},
	{"text": "T:36.5℃", "bbox": [111, 187, 195, 200]},
	{"text": "P:70次/分", "bbox": [220, 187, 318, 200]},
	{"text": "R:19次/分", "bbox": [346, 187, 444, 200]},
	{"text": "BP:120/60mmHg", "bbox": [471, 187, 615, 201]},
	{"text": "处方□检查□检验□医疗医嘱", "bbox": [110, 207, 424, 221]},
	{"text": "主诉:反复咳嗽、胸闷半年", "bbox": [103, 227, 318, 240]},
	{"text": "现病史:半年前反复发作咳嗽、胸闷,就诊于我院查肺功能结构提示支气管舒张实验阳性,考虑支气管", "bbox": [103, 243, 935, 257]},
	{"text": "哮喘,予以吸入ICS+LABA治疗后症状好转,仍反复发作。未规律用药,现为求复查入院。", "bbox": [103, 259, 813, 273]},
	{"text": "本次门诊距上次门诊间隔时间半年", "bbox": [104, 277, 360, 290]},
	{"text": "质控相关内容填写:", "bbox": [138, 292, 278, 305]},
	{"text": "症状控制情况:", "bbox": [152, 307, 262, 320]},
	{"text": "□良好控制(无勾选)√部分控制(勾线1-2项)□未控制(勾选3-4项)", "bbox": [155, 324, 683, 338]},
	{"text": "过去4周,患者:□夜间因哮喘憋醒;□日间哮喘症状>2次/周;", "bbox": [177, 341, 717, 355]},
	{"text": "√哮喘引起的活动受限□使用缓解药SABA次数>2次/周;", "bbox": [323, 361, 769, 374]},
	{"text": "吸入药物使用情况:□超量使用;□遵医嘱使用;□减量使用;√按需使用;□未使用;", "bbox": [152, 379, 847, 393]},
	{"text": "吸入装置使用情况:√正确□不正确", "bbox": [152, 398, 487, 411]},
	{"text": "急性发作情况:两次就诊期间急性发作:√否□是,发作次数", "bbox": [152, 416, 656, 430]},
	{"text": "过敏药物名称:无", "bbox": [98, 437, 242, 450]},
	{"text": "既往史:无", "bbox": [98, 453, 188, 466]},
	{"text": "既往检查检验:无", "bbox": [98, 470, 238, 483]},
	{"text": "个人史:", "bbox": [98, 485, 159, 498]},
	{"text": "吸烟史:无,年烟龄,支/天,戒烟,已戒年。", "bbox": [128, 503, 497, 517]},
	{"text": "查体:", "bbox": [98, 520, 140, 532]},
	{"text": "吸入ICS的患者检查口腔粘膜√是□否", "bbox": [98, 537, 436, 551]},
	{"text": "<西医诊断>", "bbox": [96, 556, 186, 569]},
	{"text": "1.支气管哮喘", "bbox": [95, 573, 204, 587]},
	{"text": "辅助检查:", "bbox": [94, 589, 173, 602]},
	{"text": "本次治疗方案:□升级√维持□降级□停药", "bbox": [94, 658, 465, 673]},
	{"text": "处方:", "bbox": [91, 680, 135, 693]},
	{"text": "质控相关内容填写:", "bbox": [121, 697, 262, 710]},
	{"text": "□吸入治疗:□按需ICS-福莫特罗□按需SABA□低剂量ICS□低剂量ICS+LABA", "bbox": [138, 713, 784, 728]},
	{"text": "□高剂量ICS+LABA√低剂量ICS+LABA□LAMA□其他", "bbox": [246, 733, 697, 748]},
	{"text": "□白三烯调节剂", "bbox": [138, 748, 260, 762]},
	{"text": "□茶碱", "bbox": [138, 767, 191, 780]},
	{"text": "□口服激素", "bbox": [138, 788, 224, 801]},
	{"text": "□靶向治疗:□抗IgE单抗□抗IL-5/5R单抗□抗TSLP单抗", "bbox": [137, 810, 620, 825]},
	{"text": "□其他", "bbox": [244, 829, 300, 843]},
	{"text": "□脱敏治疗", "bbox": [135, 849, 222, 863]},
	{"text": "□其他", "bbox": [135, 870, 188, 884]},
	{"text": "□吸入装置的评估和培训", "bbox": [135, 892, 324, 907]},
	{"text": "其他处理:", "bbox": [84, 915, 163, 929]},
	{"text": "医师签名:黄志昂", "bbox": [671, 940, 875, 955]}
]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord API: raw_items=53, valid_items=53, elapsed=20.1s
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[0]: text=国家呼吸医疗质量控制中心标准化门诊病历, bbox=[309, 84, 716, 100]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[1]: text=哮喘复诊(简化版), bbox=[430, 107, 598, 123]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[2]: text=门诊号:2505048587, bbox=[726, 108, 878, 120]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[3]: text=□复诊:□预约, bbox=[103, 139, 210, 152]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[4]: text=就诊日期:2025-05-2912:19:36, bbox=[283, 140, 527, 152]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[5]: text=就诊科室:呼吸与危重症医学科, bbox=[679, 139, 916, 152]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[6]: text=姓名, bbox=[107, 163, 140, 175]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[7]: text=性别:男, bbox=[283, 162, 350, 175]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[8]: text=年龄:58岁, bbox=[395, 162, 478, 175]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[9]: text=联系人:本人, bbox=[531, 162, 629, 175]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[10]: text=联系电话:, bbox=[714, 162, 789, 175]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[11]: text=T:36.5℃, bbox=[111, 187, 195, 200]
2026-08-10 06:33:49,814 INFO     29 [qwen-vl-text] coord item[12]: text=P:70次/分, bbox=[220, 187, 318, 200]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[13]: text=R:19次/分, bbox=[346, 187, 444, 200]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[14]: text=BP:120/60mmHg, bbox=[471, 187, 615, 201]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[15]: text=处方□检查□检验□医疗医嘱, bbox=[110, 207, 424, 221]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[16]: text=主诉:反复咳嗽、胸闷半年, bbox=[103, 227, 318, 240]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[17]: text=现病史:半年前反复发作咳嗽、胸闷,就诊于我院查肺功能结构提示支气管舒张实验阳性,考虑支气管, bbox=[103, 243, 935, 257]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[18]: text=哮喘,予以吸入ICS+LABA治疗后症状好转,仍反复发作。未规律用药,现为求复查入院。, bbox=[103, 259, 813, 273]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[19]: text=本次门诊距上次门诊间隔时间半年, bbox=[104, 277, 360, 290]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[20]: text=质控相关内容填写:, bbox=[138, 292, 278, 305]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[21]: text=症状控制情况:, bbox=[152, 307, 262, 320]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[22]: text=□良好控制(无勾选)√部分控制(勾线1-2项)□未控制(勾选3-4项), bbox=[155, 324, 683, 338]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[23]: text=过去4周,患者:□夜间因哮喘憋醒;□日间哮喘症状>2次/周;, bbox=[177, 341, 717, 355]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[24]: text=√哮喘引起的活动受限□使用缓解药SABA次数>2次/周;, bbox=[323, 361, 769, 374]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[25]: text=吸入药物使用情况:□超量使用;□遵医嘱使用;□减量使用;√按需使用;□未使用;, bbox=[152, 379, 847, 393]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[26]: text=吸入装置使用情况:√正确□不正确, bbox=[152, 398, 487, 411]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[27]: text=急性发作情况:两次就诊期间急性发作:√否□是,发作次数, bbox=[152, 416, 656, 430]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[28]: text=过敏药物名称:无, bbox=[98, 437, 242, 450]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[29]: text=既往史:无, bbox=[98, 453, 188, 466]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[30]: text=既往检查检验:无, bbox=[98, 470, 238, 483]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[31]: text=个人史:, bbox=[98, 485, 159, 498]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[32]: text=吸烟史:无,年烟龄,支/天,戒烟,已戒年。, bbox=[128, 503, 497, 517]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[33]: text=查体:, bbox=[98, 520, 140, 532]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[34]: text=吸入ICS的患者检查口腔粘膜√是□否, bbox=[98, 537, 436, 551]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[35]: text=<西医诊断>, bbox=[96, 556, 186, 569]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[36]: text=1.支气管哮喘, bbox=[95, 573, 204, 587]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[37]: text=辅助检查:, bbox=[94, 589, 173, 602]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[38]: text=本次治疗方案:□升级√维持□降级□停药, bbox=[94, 658, 465, 673]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[39]: text=处方:, bbox=[91, 680, 135, 693]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[40]: text=质控相关内容填写:, bbox=[121, 697, 262, 710]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[41]: text=□吸入治疗:□按需ICS-福莫特罗□按需SABA□低剂量ICS□低剂量ICS+LABA, bbox=[138, 713, 784, 728]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[42]: text=□高剂量ICS+LABA√低剂量ICS+LABA□LAMA□其他, bbox=[246, 733, 697, 748]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[43]: text=□白三烯调节剂, bbox=[138, 748, 260, 762]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[44]: text=□茶碱, bbox=[138, 767, 191, 780]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[45]: text=□口服激素, bbox=[138, 788, 224, 801]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[46]: text=□靶向治疗:□抗IgE单抗□抗IL-5/5R单抗□抗TSLP单抗, bbox=[137, 810, 620, 825]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[47]: text=□其他, bbox=[244, 829, 300, 843]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[48]: text=□脱敏治疗, bbox=[135, 849, 222, 863]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[49]: text=□其他, bbox=[135, 870, 188, 884]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[50]: text=□吸入装置的评估和培训, bbox=[135, 892, 324, 907]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[51]: text=其他处理:, bbox=[84, 915, 163, 929]
2026-08-10 06:33:49,815 INFO     29 [qwen-vl-text] coord item[52]: text=医师签名:黄志昂, bbox=[671, 940, 875, 955]
2026-08-10 06:33:49,816 INFO     29 [qwen-vl-text] page=0 — 53/53 coords, api_time=20.1s
2026-08-10 06:33:49,816 INFO     29 [qwen-vl-text] new_positions (53):
[[0, 183.855, 426.02, 70.728, 84.2], [0, 255.85, 355.81, 90.094, 103.566], [0, 431.96999999999997, 522.41, 90.93599999999999, 101.03999999999999], [0, 61.285, 124.94999999999999, 117.038, 127.984], [0, 168.385, 313.565, 117.88, 127.984], [0, 404.005, 545.02, 117.038, 127.984], [0, 63.665, 83.3, 137.246, 147.35], [0, 168.385, 208.25, 136.404, 147.35], [0, 235.02499999999998, 284.40999999999997, 136.404, 147.35], [0, 315.945, 374.255, 136.404, 147.35], [0, 424.83, 469.455, 136.404, 147.35], [0, 66.045, 116.02499999999999, 157.454, 168.4], [0, 130.9, 189.20999999999998, 157.454, 168.4], [0, 205.87, 264.18, 157.454, 168.4], [0, 280.245, 365.925, 157.454, 169.242], [0, 65.45, 252.28, 174.29399999999998, 186.082], [0, 61.285, 189.20999999999998, 191.134, 202.07999999999998], [0, 61.285, 556.3249999999999, 204.606, 216.394], [0, 61.285, 483.73499999999996, 218.078, 229.86599999999999], [0, 61.879999999999995, 214.2, 233.23399999999998, 244.17999999999998], [0, 82.11, 165.41, 245.864, 256.81], [0, 90.44, 155.89, 258.49399999999997, 269.44], [0, 92.225, 406.385, 272.808, 284.596], [0, 105.315, 426.615, 287.122, 298.90999999999997], [0, 192.185, 457.555, 303.962, 314.908], [0, 90.44, 503.965, 319.118, 330.906], [0, 90.44, 289.765, 335.116, 346.062], [0, 90.44, 390.32, 350.272, 362.06], [0, 58.309999999999995, 143.98999999999998, 367.954, 378.9], [0, 58.309999999999995, 111.86, 381.426, 392.372], [0, 58.309999999999995, 141.60999999999999, 395.74, 406.686], [0, 58.309999999999995, 94.60499999999999, 408.37, 419.316], [0, 76.16, 295.715, 423.526, 435.31399999999996], [0, 58.309999999999995, 83.3, 437.84, 447.94399999999996], [0, 58.309999999999995, 259.42, 452.154, 463.942], [0, 57.12, 110.67, 468.152, 479.09799999999996], [0, 56.525, 121.38, 482.466, 494.25399999999996], [0, 55.93, 102.935, 495.938, 506.88399999999996], [0, 55.93, 276.675, 554.036, 566.6659999999999], [0, 54.144999999999996, 80.325, 572.56, 583.506], [0, 71.99499999999999, 155.89, 586.874, 597.8199999999999], [0, 82.11, 466.47999999999996, 600.346, 612.976], [0, 146.37, 414.715, 617.1859999999999, 629.816], [0, 82.11, 154.7, 629.816, 641.6039999999999], [0, 82.11, 113.645, 645.814, 656.76], [0, 82.11, 133.28, 663.496, 674.442], [0, 81.515, 368.9, 682.02, 694.65], [0, 145.18, 178.5, 698.018, 709.8059999999999], [0, 80.325, 132.09, 714.858, 726.646], [0, 80.325, 111.86, 732.54, 744.328], [0, 80.325, 192.78, 751.064, 763.694], [0, 49.98, 96.985, 770.43, 782.218], [0, 399.245, 520.625, 791.48, 804.11]]
2026-08-10 06:33:49,816 INFO     29 [qwen-vl-text] ═══ DONE ═══ 53 positions, pages=1, time=22.1s
2026-08-10 06:33:49,825 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 06:33:49,825 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:33:49,825 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 06:33:49,832 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:49,832 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:33:52,264 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:33:52.263+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 7, "failed": 0, "current": {"53ddf620948511f1bd9827cf206dfa2d": {"id": "53ddf620948511f1bd9827cf206dfa2d", "doc_id": "534cda0a948511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZCXI-\u5f00\u5c01.pdf", "type": "pdf", "location": "ZCXI-\u5f00\u5c01.pdf", "size": 3146880, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343578385, "task_type": "dataflow", "root_trace_id": "02484dfe91b54a019343dc11c0957c86", "root_traceparent": "00-02484dfe91b54a019343dc11c0957c86-3aa2f469fae54a9d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:33:58,992 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:59,005 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 06:33:59,005 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:33:59,005 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 06:33:59,013 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:59,014 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:33:59,772 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:59,781 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 06:33:59,781 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:33:59,781 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 06:33:59,791 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:33:59,791 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:34:00,586 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:34:00,599 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 06:34:00,599 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:34:00,600 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 06:34:00,610 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:34:00,610 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:34:01,183 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:34:01,201 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 06:34:01,201 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:34:01,201 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 06:34:01,217 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:34:01,218 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:34:01,218 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:34:01,219 INFO     29 [qwen-vl-text] positions(72): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:34:01,219 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [72]
2026-08-10 06:34:01,466 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:34:01,467 INFO     29 [qwen-vl-text] LLM extraction start, text_len=774
2026-08-10 06:34:01,467 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:34:01,467 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 53, \"bbox_end\": 124, \"encounter_dates\": [\"2024-10-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "河南大学第一附属医院\n肺功能测试\n姓名:\n体重: 64.00\n性别: Male\nID:\n身高: 166.00\n种族: Asian\nBSA: 1.71\n年龄: 58\n日期: 2024/10/19\n床号:\n结论: 中重度混合性通气功能障碍\n支气管舒张试验阳性\n签名: 王学会\n审核:\nPre-Bronch\nPost-Bronch\nctual Pred %Pred\nActual %Pred %Chng\n---- 肺通气 ----\nFVC (L) 2.31 3.67 62 2.98 81 +29\nFEV1 (L) 1.49 2.92 51 1.89 64 +26\nFEV1/FVC (%) 65 79 81 63 80 -2\nFEF 25% (L/sec) 2.29 6.49 35 3.46 53 +50\nFEF 50% (L/sec) 1.07 4.26 25 1.93 45 +80\nFEF 75% (L/sec) 0.35 0.81 43 0.93 114 +166\nFEF 25-75% (L/s 0.83 2.61 31 1.72 66 +107\nFIF Max (L/sec) 2.46 1.90 -22\nFEF Max (L/sec) 3.70 4.03 +8\nBack Extrapol Vol 0.04 0.06 +37\n---- 肺活量 ----\nSVC (L) 2.21 3.67 60\nIC (L) 1.74 2.68 65\nERV (L) 0.46 1.34 34\n6\n4\n2\n0\n-2\n-4\n-6\n6\n4\n2\n0\n-2\n-4\n-6\n1 2 3\n1 2 3\n08:44:26\n0\n5\n10\n15\n20\n25\n30\n6\n5\n4\n3\n2\n1\n0\n20\n15\n10\n5\n0\n0 1 2 3 4 5 6 7 8 9 10 11 12",
    "role": "user"
  }
]
2026-08-10 06:34:05,972 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:34:05,972 INFO     29 [qwen-vl-text] LLM output (len=837):
{
  "exam_date": "2024-10-19",
  "report_date": "2024-10-19",
  "exam_name": "肺功能测试",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "Male",
  "department": null,
  "bed_number": null,
  "findings": "Pre-Bronch Post-Bronch ctual Pred %Pred Actual %Pred %Chng ---- 肺通气 ---- FVC (L) 2.31 3.67 62 2.98 81 +29 FEV1 (L) 1.49 2.92 51 1.89 64 +26 FEV1/FVC (%) 65 79 81 63 80 -2 FEF 25% (L/sec) 2.29 6.49 35 3.46 53 +50 FEF 50% (L/sec) 1.07 4.26 25 1.93 45 +80 FEF 75% (L/sec) 0.35 0.81 43 0.93 114 +166 FEF 25-75% (L/s 0.83 2.61 31 1.72 66 +107 FIF Max (L/sec) 2.46 1.90 -22 FEF Max (L/sec) 3.70 4.03 +8 Back Extrapol Vol 0.04 0.06 +37 ---- 肺活量 ---- SVC (L) 2.21 3.67 60 IC (L) 1.74 2.68 65 ERV (L) 0.46 1.34 34",
  "conclusion": "中重度混合性通气功能障碍\n支气管舒张试验阳性",
  "physician": "王学会",
  "reviewer": null
}
2026-08-10 06:34:05,977 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2058451, prompt_len=1603
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共72行）
["河南大学第一附属医院", "肺功能测试", "姓名:", "体重: 64.00", "性别: Male", "ID:", "身高: 166.00", "种族: Asian", "BSA: 1.71", "年龄: 58", "日期: 2024/10/19", "床号:", "结论: 中重度混合性通气功能障碍", "支气管舒张试验阳性", "签名: 王学会", "审核:", "Pre-Bronch", "Post-Bronch", "ctual Pred %Pred", "Actual %Pred %Chng", "---- 肺通气 ----", "FVC (L) 2.31 3.67 62 2.98 81 +29", "FEV1 (L) 1.49 2.92 51 1.89 64 +26", "FEV1/FVC (%) 65 79 81 63 80 -2", "FEF 25% (L/sec) 2.29 6.49 35 3.46 53 +50", "FEF 50% (L/sec) 1.07 4.26 25 1.93 45 +80", "FEF 75% (L/sec) 0.35 0.81 43 0.93 114 +166", "FEF 25-75% (L/s 0.83 2.61 31 1.72 66 +107", "FIF Max (L/sec) 2.46 1.90 -22", "FEF Max (L/sec) 3.70 4.03 +8", "Back Extrapol Vol 0.04 0.06 +37", "---- 肺活量 ----", "SVC (L) 2.21 3.67 60", "IC (L) 1.74 2.68 65", "ERV (L) 0.46 1.34 34", "6", "4", "2", "0", "-2", "-4", "-6", "6", "4", "2", "0", "-2", "-4", "-6", "1 2 3", "1 2 3", "08:44:26", "0", "5", "10", "15", "20", "25", "30", "6", "5", "4", "3", "2", "1", "0", "20", "15", "10", "5", "0", "0 1 2 3 4 5 6 7 8 9 10 11 12"]

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
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord API raw response (len=3933):
[
	{"text": "河南大学第一附属医院", "bbox": [375, 95, 624, 114]},
	{"text": "肺功能测试", "bbox": [460, 117, 540, 130]},
	{"text": "姓名:", "bbox": [111, 131, 150, 144]},
	{"text": "体重: 64.00", "bbox": [111, 147, 214, 160]},
	{"text": "性别: Male", "bbox": [111, 160, 205, 173]},
	{"text": "ID:", "bbox": [402, 137, 424, 148]},
	{"text": "身高: 166.00", "bbox": [402, 149, 510, 162]},
	{"text": "种族: Asian", "bbox": [400, 164, 503, 178]},
	{"text": "BSA: 1.71", "bbox": [585, 139, 661, 150]},
	{"text": "年龄: 58", "bbox": [585, 151, 650, 164]},
	{"text": "日期: 2024/10/19", "bbox": [723, 139, 850, 151]},
	{"text": "床号:", "bbox": [723, 152, 760, 164]},
	{"text": "结论: 中重度混合性通气功能障碍", "bbox": [110, 182, 333, 195]},
	{"text": "支气管舒张试验阳性", "bbox": [160, 206, 289, 218]},
	{"text": "签名: 王学会", "bbox": [632, 233, 745, 257]},
	{"text": "审核:", "bbox": [633, 262, 668, 274]},
	{"text": "Pre-Bronch", "bbox": [243, 290, 324, 301]},
	{"text": "Post-Bronch", "bbox": [413, 292, 498, 304]},
	{"text": "ctual Pred %Pred", "bbox": [227, 305, 360, 318]},
	{"text": "Actual %Pred %Chng", "bbox": [381, 307, 543, 320]},
	{"text": "---- 肺通气 ----", "bbox": [102, 317, 204, 330]},
	{"text": "FVC (L) 2.31 3.67 62 2.98 81 +29", "bbox": [101, 333, 542, 349]},
	{"text": "FEV1 (L) 1.49 2.92 51 1.89 64 +26", "bbox": [100, 349, 542, 364]},
	{"text": "FEV1/FVC (%) 65 79 81 63 80 -2", "bbox": [100, 364, 542, 379]},
	{"text": "FEF 25% (L/sec) 2.29 6.49 35 3.46 53 +50", "bbox": [99, 379, 542, 394]},
	{"text": "FEF 50% (L/sec) 1.07 4.26 25 1.93 45 +80", "bbox": [99, 394, 542, 409]},
	{"text": "FEF 75% (L/sec) 0.35 0.81 43 0.93 114 +166", "bbox": [98, 409, 542, 424]},
	{"text": "FEF 25-75% (L/s 0.83 2.61 31 1.72 66 +107", "bbox": [97, 424, 542, 439]},
	{"text": "FIF Max (L/sec) 2.46 1.90 -22", "bbox": [96, 440, 541, 455]},
	{"text": "FEF Max (L/sec) 3.70 4.03 +8", "bbox": [95, 455, 541, 470]},
	{"text": "Back Extrapol Vol 0.04 0.06 +37", "bbox": [94, 470, 540, 485]},
	{"text": "---- 肺活量 ----", "bbox": [93, 502, 195, 515]},
	{"text": "SVC (L) 2.21 3.67 60", "bbox": [92, 518, 355, 532]},
	{"text": "IC (L) 1.74 2.68 65", "bbox": [91, 533, 354, 548]},
	{"text": "ERV (L) 0.46 1.34 34", "bbox": [90, 549, 354, 563]},
	{"text": "6", "bbox": [668, 319, 682, 333]},
	{"text": "4", "bbox": [668, 339, 682, 353]},
	{"text": "2", "bbox": [668, 358, 682, 373]},
	{"text": "0", "bbox": [668, 378, 682, 392]},
	{"text": "-2", "bbox": [662, 398, 682, 412]},
	{"text": "-4", "bbox": [662, 418, 682, 432]},
	{"text": "-6", "bbox": [662, 437, 682, 451]},
	{"text": "6", "bbox": [802, 320, 816, 334]},
	{"text": "4", "bbox": [802, 340, 816, 354]},
	{"text": "2", "bbox": [802, 359, 816, 373]},
	{"text": "0", "bbox": [802, 379, 816, 393]},
	{"text": "-2", "bbox": [797, 399, 816, 413]},
	{"text": "-4", "bbox": [797, 418, 816, 432]},
	{"text": "-6", "bbox": [797, 438, 816, 452]},
	{"text": "1 2 3", "bbox": [702, 394, 766, 408]},
	{"text": "1 2 3", "bbox": [837, 395, 902, 409]},
	{"text": "08:44:26", "bbox": [757, 481, 806, 490]},
	{"text": "0", "bbox": [668, 583, 677, 592]},
	{"text": "5", "bbox": [705, 584, 714, 593]},
	{"text": "10", "bbox": [741, 585, 754, 593]},
	{"text": "15", "bbox": [779, 585, 792, 593]},
	{"text": "20", "bbox": [814, 585, 828, 593]},
	{"text": "25", "bbox": [852, 585, 866, 593]},
	{"text": "30", "bbox": [889, 585, 902, 593]},
	{"text": "6", "bbox": [660, 715, 670, 724]},
	{"text": "5", "bbox": [660, 741, 670, 750]},
	{"text": "4", "bbox": [660, 768, 670, 777]},
	{"text": "3", "bbox": [660, 794, 670, 803]},
	{"text": "2", "bbox": [660, 821, 670, 830]},
	{"text": "1", "bbox": [660, 848, 670, 857]},
	{"text": "0", "bbox": [660, 875, 670, 884]},
	{"text": "20", "bbox": [895, 717, 911, 725]},
	{"text": "15", "bbox": [899, 757, 913, 766]},
	{"text": "10", "bbox": [900, 796, 914, 805]},
	{"text": "5", "bbox": [900, 837, 909, 846]},
	{"text": "0", "bbox": [900, 877, 909, 886]},
	{"text": "0 1 2 3 4 5 6 7 8 9 10 11 12", "bbox": [664, 884, 908, 894]}
]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord API: raw_items=72, valid_items=72, elapsed=24.6s
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[0]: text=河南大学第一附属医院, bbox=[375, 95, 624, 114]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能测试, bbox=[460, 117, 540, 130]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[111, 131, 150, 144]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[3]: text=体重: 64.00, bbox=[111, 147, 214, 160]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[4]: text=性别: Male, bbox=[111, 160, 205, 173]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[5]: text=ID:, bbox=[402, 137, 424, 148]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[6]: text=身高: 166.00, bbox=[402, 149, 510, 162]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[7]: text=种族: Asian, bbox=[400, 164, 503, 178]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[8]: text=BSA: 1.71, bbox=[585, 139, 661, 150]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[9]: text=年龄: 58, bbox=[585, 151, 650, 164]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[10]: text=日期: 2024/10/19, bbox=[723, 139, 850, 151]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[11]: text=床号:, bbox=[723, 152, 760, 164]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[12]: text=结论: 中重度混合性通气功能障碍, bbox=[110, 182, 333, 195]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[13]: text=支气管舒张试验阳性, bbox=[160, 206, 289, 218]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[14]: text=签名: 王学会, bbox=[632, 233, 745, 257]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[15]: text=审核:, bbox=[633, 262, 668, 274]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[16]: text=Pre-Bronch, bbox=[243, 290, 324, 301]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[17]: text=Post-Bronch, bbox=[413, 292, 498, 304]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[18]: text=ctual Pred %Pred, bbox=[227, 305, 360, 318]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[19]: text=Actual %Pred %Chng, bbox=[381, 307, 543, 320]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[20]: text=---- 肺通气 ----, bbox=[102, 317, 204, 330]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[21]: text=FVC (L) 2.31 3.67 62 2.98 81 +29, bbox=[101, 333, 542, 349]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[22]: text=FEV1 (L) 1.49 2.92 51 1.89 64 +26, bbox=[100, 349, 542, 364]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[23]: text=FEV1/FVC (%) 65 79 81 63 80 -2, bbox=[100, 364, 542, 379]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[24]: text=FEF 25% (L/sec) 2.29 6.49 35 3.46 53 +50, bbox=[99, 379, 542, 394]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[25]: text=FEF 50% (L/sec) 1.07 4.26 25 1.93 45 +80, bbox=[99, 394, 542, 409]
2026-08-10 06:34:30,623 INFO     29 [qwen-vl-text] coord item[26]: text=FEF 75% (L/sec) 0.35 0.81 43 0.93 114 +166, bbox=[98, 409, 542, 424]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[27]: text=FEF 25-75% (L/s 0.83 2.61 31 1.72 66 +107, bbox=[97, 424, 542, 439]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[28]: text=FIF Max (L/sec) 2.46 1.90 -22, bbox=[96, 440, 541, 455]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[29]: text=FEF Max (L/sec) 3.70 4.03 +8, bbox=[95, 455, 541, 470]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[30]: text=Back Extrapol Vol 0.04 0.06 +37, bbox=[94, 470, 540, 485]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[31]: text=---- 肺活量 ----, bbox=[93, 502, 195, 515]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[32]: text=SVC (L) 2.21 3.67 60, bbox=[92, 518, 355, 532]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[33]: text=IC (L) 1.74 2.68 65, bbox=[91, 533, 354, 548]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[34]: text=ERV (L) 0.46 1.34 34, bbox=[90, 549, 354, 563]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[35]: text=6, bbox=[668, 319, 682, 333]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[36]: text=4, bbox=[668, 339, 682, 353]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[37]: text=2, bbox=[668, 358, 682, 373]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[38]: text=0, bbox=[668, 378, 682, 392]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[39]: text=-2, bbox=[662, 398, 682, 412]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[40]: text=-4, bbox=[662, 418, 682, 432]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[41]: text=-6, bbox=[662, 437, 682, 451]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[42]: text=6, bbox=[802, 320, 816, 334]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[43]: text=4, bbox=[802, 340, 816, 354]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[44]: text=2, bbox=[802, 359, 816, 373]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[45]: text=0, bbox=[802, 379, 816, 393]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[46]: text=-2, bbox=[797, 399, 816, 413]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[47]: text=-4, bbox=[797, 418, 816, 432]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[48]: text=-6, bbox=[797, 438, 816, 452]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[49]: text=1 2 3, bbox=[702, 394, 766, 408]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[50]: text=1 2 3, bbox=[837, 395, 902, 409]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[51]: text=08:44:26, bbox=[757, 481, 806, 490]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[52]: text=0, bbox=[668, 583, 677, 592]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[53]: text=5, bbox=[705, 584, 714, 593]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[54]: text=10, bbox=[741, 585, 754, 593]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[55]: text=15, bbox=[779, 585, 792, 593]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[56]: text=20, bbox=[814, 585, 828, 593]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[57]: text=25, bbox=[852, 585, 866, 593]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[58]: text=30, bbox=[889, 585, 902, 593]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[59]: text=6, bbox=[660, 715, 670, 724]
2026-08-10 06:34:30,624 INFO     29 [qwen-vl-text] coord item[60]: text=5, bbox=[660, 741, 670, 750]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[61]: text=4, bbox=[660, 768, 670, 777]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[62]: text=3, bbox=[660, 794, 670, 803]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[63]: text=2, bbox=[660, 821, 670, 830]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[64]: text=1, bbox=[660, 848, 670, 857]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[65]: text=0, bbox=[660, 875, 670, 884]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[66]: text=20, bbox=[895, 717, 911, 725]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[67]: text=15, bbox=[899, 757, 913, 766]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[68]: text=10, bbox=[900, 796, 914, 805]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[69]: text=5, bbox=[900, 837, 909, 846]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[70]: text=0, bbox=[900, 877, 909, 886]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] coord item[71]: text=0 1 2 3 4 5 6 7 8 9 10 11 12, bbox=[664, 884, 908, 894]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] page=1 — 72/72 coords, api_time=24.6s
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] new_positions (72):
[[1, 223.125, 371.28, 79.99, 95.988], [1, 273.7, 321.3, 98.514, 109.46], [1, 66.045, 89.25, 110.30199999999999, 121.24799999999999], [1, 66.045, 127.33, 123.774, 134.72], [1, 66.045, 121.975, 134.72, 145.666], [1, 239.19, 252.28, 115.354, 124.616], [1, 239.19, 303.45, 125.458, 136.404], [1, 238.0, 299.28499999999997, 138.088, 149.876], [1, 348.075, 393.29499999999996, 117.038, 126.3], [1, 348.075, 386.75, 127.142, 138.088], [1, 430.185, 505.75, 117.038, 127.142], [1, 430.185, 452.2, 127.984, 138.088], [1, 65.45, 198.135, 153.244, 164.19], [1, 95.19999999999999, 171.95499999999998, 173.452, 183.55599999999998], [1, 376.03999999999996, 443.275, 196.186, 216.394], [1, 376.635, 397.46, 220.60399999999998, 230.708], [1, 144.58499999999998, 192.78, 244.17999999999998, 253.44199999999998], [1, 245.73499999999999, 296.31, 245.864, 255.968], [1, 135.065, 214.2, 256.81, 267.756], [1, 226.695, 323.085, 258.49399999999997, 269.44], [1, 60.69, 121.38, 266.914, 277.86], [1, 60.095, 322.49, 280.38599999999997, 293.858], [1, 59.5, 322.49, 293.858, 306.488], [1, 59.5, 322.49, 306.488, 319.118], [1, 58.904999999999994, 322.49, 319.118, 331.748], [1, 58.904999999999994, 322.49, 331.748, 344.378], [1, 58.309999999999995, 322.49, 344.378, 357.008], [1, 57.714999999999996, 322.49, 357.008, 369.638], [1, 57.12, 321.895, 370.47999999999996, 383.11], [1, 56.525, 321.895, 383.11, 395.74], [1, 55.93, 321.3, 395.74, 408.37], [1, 55.335, 116.02499999999999, 422.68399999999997, 433.63], [1, 54.739999999999995, 211.225, 436.156, 447.94399999999996], [1, 54.144999999999996, 210.63, 448.786, 461.416], [1, 53.55, 210.63, 462.258, 474.046], [1, 397.46, 405.78999999999996, 268.598, 280.38599999999997], [1, 397.46, 405.78999999999996, 285.438, 297.226], [1, 397.46, 405.78999999999996, 301.436, 314.066], [1, 397.46, 405.78999999999996, 318.276, 330.06399999999996], [1, 393.89, 405.78999999999996, 335.116, 346.904], [1, 393.89, 405.78999999999996, 351.95599999999996, 363.74399999999997], [1, 393.89, 405.78999999999996, 367.954, 379.74199999999996], [1, 477.19, 485.52, 269.44, 281.228], [1, 477.19, 485.52, 286.28, 298.068], [1, 477.19, 485.52, 302.27799999999996, 314.066], [1, 477.19, 485.52, 319.118, 330.906], [1, 474.215, 485.52, 335.95799999999997, 347.746], [1, 474.215, 485.52, 351.95599999999996, 363.74399999999997], [1, 474.215, 485.52, 368.796, 380.584], [1, 417.69, 455.77, 331.748, 343.536], [1, 498.015, 536.6899999999999, 332.59, 344.378], [1, 450.41499999999996, 479.57, 405.002, 412.58], [1, 397.46, 402.815, 490.88599999999997, 498.464], [1, 419.47499999999997, 424.83, 491.728, 499.306], [1, 440.895, 448.63, 492.57, 499.306], [1, 463.505, 471.23999999999995, 492.57, 499.306], [1, 484.33, 492.65999999999997, 492.57, 499.306], [1, 506.94, 515.27, 492.57, 499.306], [1, 528.9549999999999, 536.6899999999999, 492.57, 499.306], [1, 392.7, 398.65, 602.03, 609.608], [1, 392.7, 398.65, 623.922, 631.5], [1, 392.7, 398.65, 646.656, 654.2339999999999], [1, 392.7, 398.65, 668.548, 676.126], [1, 392.7, 398.65, 691.2819999999999, 698.86], [1, 392.7, 398.65, 714.016, 721.5939999999999], [1, 392.7, 398.65, 736.75, 744.328], [1, 532.525, 542.045, 603.7139999999999, 610.4499999999999], [1, 534.905, 543.235, 637.394, 644.972], [1, 535.5, 543.8299999999999, 670.232, 677.81], [1, 535.5, 540.855, 704.754, 712.332], [1, 535.5, 540.855, 738.434, 746.012], [1, 395.08, 540.26, 744.328, 752.7479999999999]]
2026-08-10 06:34:30,625 INFO     29 [qwen-vl-text] ═══ DONE ═══ 72 positions, pages=1, time=29.4s
2026-08-10 06:34:30,643 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 06:34:30,643 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "125 items", "markdown": "", "text": "", "name": "ZCXI-开封.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:34:30,643 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 06:34:30,644 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:34:30.643+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 7, "failed": 0, "current": {"53ddf620948511f1bd9827cf206dfa2d": {"id": "53ddf620948511f1bd9827cf206dfa2d", "doc_id": "534cda0a948511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZCXI-\u5f00\u5c01.pdf", "type": "pdf", "location": "ZCXI-\u5f00\u5c01.pdf", "size": 3146880, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343578385, "task_type": "dataflow", "root_trace_id": "02484dfe91b54a019343dc11c0957c86", "root_traceparent": "00-02484dfe91b54a019343dc11c0957c86-3aa2f469fae54a9d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:34:30,645 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-10 06:34:31,064 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 06:34:31,064 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "ZCXI-开封.pdf"}
2026-08-10 06:34:31,064 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 06:34:31,141 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786343579118, 'update_date': datetime.datetime(2026, 8, 10, 6, 32, 59), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 812145, 'status': '1'}
2026-08-10 06:34:31,352 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=国家呼吸医疗质量控制中心标准化门诊病历
哮喘复诊(简化版)
门诊号:2505048587
□复诊:□预约
就诊日期:2025-05-2912:19:36
就诊科室:呼吸与危重症医学科
姓名
性别:男
年龄:58岁
联系人:本人
联系电话:
T:36.5℃
P:70次/分
R:19次/分
BP:120/60mmHg
处方□检查□检验□医疗医嘱
主诉:反复咳嗽、胸闷半年
现病史:半年前反复发作咳嗽、胸闷,就诊于我院查肺功能结构提示支气管舒张实验阳性,考虑支气管
哮喘,予以吸入ICS+LABA治疗后症状好转,仍反复发作。未规律用药,现为求复查入院。
本次门诊距上次门诊间隔时间半年
质控相关内容填写:
症状控制情况:
□良好控制(无勾选)√部分控制(勾线1-2项)□未控制(勾选3-4项)
过去4周,患者:□夜间因哮喘憋醒;□日间哮喘症状>2次/周;
√哮喘引起的活动受限□使用缓解药SABA次数>2次/周;
吸入药物使用情况:□超量使用;□遵医嘱使用;□减量使用;√按需使用;□未使用;
吸入装置使用情况:√正确□不正确
急性发作情况:两次就诊期间急性发作:√否□是,发作次数
过敏药物名称:无
既往史:无
既往检查检验:无
个人史:
吸烟史:无,年烟龄,支/天,戒烟,已戒年。
查体:
吸入ICS的患者检查口腔粘膜√是□否
<西医诊断>
1.支气管哮喘
辅助检查:
本次治疗方案:□升级√维持□降级□停药
处方:
质控相关内容填写:
□吸入治疗:□按需ICS-福莫特罗□按需SABA□低剂量ICS□低剂量ICS+LABA
□高剂量ICS+LABA√低剂量ICS+LABA□LAMA□其他
□白三烯调节剂
□茶碱
□口服激素
□靶向治疗:□抗IgE单抗□抗IL-5/5R单抗□抗TSLP单抗
□其他
□脱敏治疗
□其他
□吸入装置的评估和培训
其他处理:
医师签名:黄志昂
---
河南大学第一附属医院
肺功能测试
姓名:
体重: 64.00
性别: Male
ID:
身高: 166.00
种族: Asian
BSA: 1.71
年龄: 58
日期: 2024/10/19
床号:
结论: 中重度混合性通气功能障碍
支气管舒张试验阳性
签名: 王学会
审核:
Pre-Bronch
Post-Bronch
ctual Pred %Pred
Actual %Pred %Chng
---- 肺通气 ----
FVC (L) 2.31 3.67 62 2.98 81 +29
FEV1 (L) 1.49 2.92 51 1.89 64 +26
FEV1/FVC (%) 65 79 81 63 80 -2
FEF 25% (L/sec) 2.29 6.49 35 3.46 53 +50
FEF 50% (L/sec) 1.07 4.26 25 1.93 45 +80
FEF 75% (L/sec) 0.35 0.81 43 0.93 114 +166
FEF 25-75% (L/s 0.83 2.61 31 1.72 66 +107
FIF Max (L/sec) 2.46 1.90 -22
FEF Max (L/sec) 3.70 4.03 +8
Back Extrapol Vol 0.04 0.06 +37
---- 肺活量 ----
SVC (L) 2.21 3.67 60
IC (L) 1.74 2.68 65
ERV (L) 0.46 1.34 34
6
4
2
0
-2
-4
-6
6
4
2
0
-2
-4
-6
1 2 3
1 2 3
08:44:26
0
5
10
15
20
25
30
6
5
4
3
2
1
0
20
15
10
5
0
0 1 2 3 4 5 6 7 8 9 10 11 12
2026-08-10 06:34:31,623 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 06:34:31,623 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "ZCXI-开封.pdf", "embedding_token_consumption": 1196}
2026-08-10 06:34:31,623 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 06:34:31,961 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 06:34:31,962 INFO     29 [Trace] task=53ddf620 | doc=ZCXI-开封.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 06:34:31,964 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:34:31,964 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:34:31,971 INFO     29 set_progress(53ddf620948511f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 06:34:31 [DOC Engine]:
Start to index...
2026-08-10 06:34:32,018 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.041s]
2026-08-10 06:34:32,023 INFO     29 set_progress(53ddf620948511f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 06:34:32,043 INFO     29 set_progress(53ddf620948511f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 06:34:32 Indexing done (0.06s). Task done (92.62s)
2026-08-10 06:34:32,054 INFO     29 [Done], chunks(2), token(1196), elapsed:92.62
2026-08-10 06:34:32,126 INFO     29 handle_task done for task {"id": "53ddf620948511f1bd9827cf206dfa2d", "doc_id": "534cda0a948511f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZCXI-\u5f00\u5c01.pdf", "type": "pdf", "location": "ZCXI-\u5f00\u5c01.pdf", "size": 3146880, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786343578385, "task_type": "dataflow", "root_trace_id": "02484dfe91b54a019343dc11c0957c86", "root_traceparent": "00-02484dfe91b54a019343dc11c0957c86-3aa2f469fae54a9d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
