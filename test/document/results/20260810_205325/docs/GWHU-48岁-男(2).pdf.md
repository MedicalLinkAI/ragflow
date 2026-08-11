# 基准结果：GWHU-48岁-男(2).pdf

## 基本信息

- 文件：`GWHU-48岁-男(2).pdf`
- 大小：1154.7 KB
- PDF 总页数：2
- doc_id：`bdc001e294bb11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:02:28  完成时间：2026-08-10T21:04:22  耗时：114.1s
- progress_msg：`13:04:16 Indexing done (0.02s). Task done (100.80s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 79f2a757 | 1 | 1-1 | 初诊病历 姓名： 病历号：00125638 科别：呼吸与危重症医学二科 门诊 性 |
| 2 | 6d8bbb1b | 1 | 2-2 | 鹤煤总医院肺功能报告单 ID号：4000 姓名： 性别：男 年龄：48 身高：1 |

- chunks 总数：2
- 各 chunk 页数合计（含跨页重复）：2
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
  - `[no_text_noise] 2026-08-10 13:04:16,007 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:02:30,378 INFO     29 handle_task begin for task {"id": "bdf0115294bb11f1bd9827cf206dfa2d", "doc_id": "bdc001e294bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366949164, "task_type": "dataflow", "root_trace_id": "ba607da6f8e14f3789343d8e8c76e702", "root_traceparent": "00-ba607da6f8e14f3789343d8e8c76e702-655c145a91d3c0d4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:02:30,583 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 13:02:30,699 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:02:30,709 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:02:30,709 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:02:30,710 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:02:30,782 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:02:30,783 INFO     29 ============================================================
2026-08-10 13:02:30,783 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:02:30,783 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:02:30,783 INFO     29 ============================================================
2026-08-10 13:02:30,783 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:02:30,783 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:02:30,797 INFO     29 No torch found.
2026-08-10 13:02:32,641 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=2
2026-08-10 13:02:32,774 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=990933, prompt_len=764
2026-08-10 13:02:34,125 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:02:34,126 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:02:34,138 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=990933, prompt_len=401
2026-08-10 13:02:36,503 INFO     29 [qwen-vl-parser] text API response (len=391):
["初诊病历", "姓名：", "病历号：00125638", "科别：呼吸与危重症医学二科", "门诊", "性别：男", "身份证号：", "出生日期：1975-12-14", "年龄：49岁", "就诊序号：113598", "就诊日期：2025-05-24 10:38", "民族：民族", "联系电话：", "医保费别：自费", "详细地址：地址", "主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "既往史：无", "过敏史：{否认食物、药物过敏史}。", "体格检查：{体温、脉搏、呼吸、血压未查}。", "辅助检查：无", "初步诊断：1、支气管哮喘", "处理意见：对症", "接诊医生：李志军", "签名时间：2025年05月24日10时38分"]
2026-08-10 13:02:36,503 INFO     29 [qwen-vl-parser] page=1 text: 25 lines (bbox 0-24)
2026-08-10 13:02:36,503 INFO     29 [qwen-vl-parser] page=1 text: 25 sections
2026-08-10 13:02:36,648 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1063452, prompt_len=764
2026-08-10 13:02:38,529 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2024-07-22"
}
```
2026-08-10 13:02:38,530 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2024-07-22
2026-08-10 13:02:38,545 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1063452, prompt_len=401
2026-08-10 13:02:48,295 INFO     29 [qwen-vl-parser] text API response (len=2163):
["鹤煤总医院肺功能报告单", "ID号：4000", "姓名：", "性别：男", "年龄：48", "身高：170 cm", "体重：95 kg", "B.S.A：2.06m²", "温度(℃)：22", "湿度(%)：50", "气压(mmHg)：1013.3", "科室：", "病区：", "预测公式：亚洲", "医生：李志军", "备注：", "SVC", "实测", "预测", "%预测", "BD后", "改进率", "VC", "L", "2.94", "3.78", "77.8", "", "", "IC", "L", "", "", "", "", "", "TV", "L", "", "", "", "", "", "ERV", "L", "", "", "", "", "", "IRV", "L", "", "", "", "", "", "FVC", "实测", "预测", "%预测", "BD后", "改进率", "FVC", "L", "2.94", "3.78", "77.8", "3.01", "2.4", "FEV0.5", "L", "1.26", "", "", "1.62", "28.6", "FEV1.0", "L", "1.88", "3.26", "57.7", "2.21", "17.6", "FEV3.0", "L", "2.74", "", "", "2.91", "6.2", "FEV1.0%(G)", "%", "63.95", "73.89", "86.5", "73.42", "14.8", "FEV1.0%(T)", "%", "63.95", "", "", "", "", "FEV1/VCpr", "%", "49.7", "", "", "58.5", "17.7", "MMF", "L/s", "1.17", "4.16", "28.1", "1.69", "44.4", "PEF", "L/s", "5.36", "8.7", "61.6", "4.37", "-18.5", "FEF25", "L/s", "2.3", "7.82", "29.4", "3.84", "67", "FEF50", "L/s", "1.45", "5.31", "27.3", "2.11", "45.5", "FEF75", "L/s", "0.61", "2.39", "25.5", "0.7", "14.8", "FEF90", "L/s", "0.23", "", "", "0.31", "34.8", "FEF50/FEF75", "", "2.38", "", "", "3.01", "26.5", "PEF/HT", "L/s/m", "3.15", "", "", "2.57", "-18.4", "FEF25/HT", "L/s/m", "1.35", "", "", "2.26", "67.4", "FEF75-85", "L/s", "0.47", "", "", "0.53", "12.8", "FEF0.2-1.2", "L/s", "2.37", "", "", "3.61", "52.3", "OI", "L/s", "5.21", "", "", "2.19", "-58", "ATI", "%", "", "", "", "", "", "PEFTIME", "Sec", "0.05", "", "", "0.08", "60", "FET", "Sec", "4.46", "", "", "3.72", "-16.6", "Vextrap", "L", "0.05", "", "", "0.09", "80", "Extrap V", "%", "1.7", "", "", "2.99", "75.9", "FIVC", "L", "2.93", "", "", "3.42", "16.7", "MVV", "实测", "预测", "%预测", "BD后", "改进率", "MVV", "L/min", "", "126.6", "", "", "", "RR", "C/min", "", "", "", "", "", "TV", "L", "", "", "", "", "", "MVV/BSA", "L/min/m²", "", "", "", "", "", "AVI", "", "", "", "", "", "", "诊断报告：", "FEV1% Restictive Normal", "SVC", "70", "Mixed", "Obstructive", "60", "%VC", "3", "0", "30", "50", "90 SEC", "12", "FVC", "8", "4", "0", "8 L", "-4", "-8", "-12", "4L", "MVV", "2", "0", "5", "10", "15 SEC", "检查技师：", "检查日期：2024-7-22", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 13:02:48,296 INFO     29 [qwen-vl-parser] page=2 text: 225 lines (bbox 25-249)
2026-08-10 13:02:48,296 INFO     29 [qwen-vl-parser] page=2 text: 225 sections
2026-08-10 13:02:48,296 INFO     29 [qwen-vl-parser] parse_pdf done: 250 sections from 2 pages.
2026-08-10 13:02:48,305 INFO     29 Close text detector.
2026-08-10 13:02:48,725 INFO     29 Close text recognizer.
2026-08-10 13:02:49,095 INFO     29 Close recognizer.
2026-08-10 13:02:49,548 INFO     29 Close recognizer.
2026-08-10 13:02:50,056 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:02:50,057 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Parser:MedLink | outputs={"html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "json"}
2026-08-10 13:02:50,057 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:02:50,076 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:50,076 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 初诊病历\n[BBOX-1] 姓名：\n[BBOX-2] 病历号：00125638\n[BBOX-3] 科别：呼吸与危重症医学二科\n[BBOX-4] 门诊\n[BBOX-5] 性别：男\n[BBOX-6] 身份证号：\n[BBOX-7] 出生日期：1975-12-14\n[BBOX-8] 年龄：49岁\n[BBOX-9] 就诊序号：113598\n[BBOX-10] 就诊日期：2025-05-24 10:38\n[BBOX-11] 民族：民族\n[BBOX-12] 联系电话：\n[BBOX-13] 医保费别：自费\n[BBOX-14] 详细地址：地址\n[BBOX-15] 主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。\n[BBOX-16] 现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。\n[BBOX-17] 既往史：无\n[BBOX-18] 过敏史：{否认食物、药物过敏史}。\n[BBOX-19] 体格检查：{体温、脉搏、呼吸、血压未查}。\n[BBOX-20] 辅助检查：无\n[BBOX-21] 初步诊断：1、支气管哮喘\n[BBOX-22] 处理意见：对症\n[BBOX-23] 接诊医生：李志军\n[BBOX-24] 签名时间：2025年05月24日10时38分\n[BBOX-25] 鹤煤总医院肺功能报告单\n[BBOX-26] ID号：4000\n[BBOX-27] 姓名：\n[BBOX-28] 性别：男\n[BBOX-29] 年龄：48\n[BBOX-30] 身高：170 cm\n[BBOX-31] 体重：95 kg\n[BBOX-32] B.S.A：2.06m²\n[BBOX-33] 温度(℃)：22\n[BBOX-34] 湿度(%)：50\n[BBOX-35] 气压(mmHg)：1013.3\n[BBOX-36] 科室：\n[BBOX-37] 病区：\n[BBOX-38] 预测公式：亚洲\n[BBOX-39] 医生：李志军\n[BBOX-40] 备注：\n[BBOX-41] SVC\n[BBOX-42] 实测\n[BBOX-43] 预测\n[BBOX-44] %预测\n[BBOX-45] BD后\n[BBOX-46] 改进率\n[BBOX-47] VC\n[BBOX-48] L\n[BBOX-49] 2.94\n[BBOX-50] 3.78\n[BBOX-51] 77.8\n[BBOX-52] IC\n[BBOX-53] L\n[BBOX-54] TV\n[BBOX-55] L\n[BBOX-56] ERV\n[BBOX-57] L\n[BBOX-58] IRV\n[BBOX-59] L\n[BBOX-60] FVC\n[BBOX-61] 实测\n[BBOX-62] 预测\n[BBOX-63] %预测\n[BBOX-64] BD后\n[BBOX-65] 改进率\n[BBOX-66] FVC\n[BBOX-67] L\n[BBOX-68] 2.94\n[BBOX-69] 3.78\n[BBOX-70] 77.8\n[BBOX-71] 3.01\n[BBOX-72] 2.4\n[BBOX-73] FEV0.5\n[BBOX-74] L\n[BBOX-75] 1.26\n[BBOX-76] 1.62\n[BBOX-77] 28.6\n[BBOX-78] FEV1.0\n[BBOX-79] L\n[BBOX-80] 1.88\n[BBOX-81] 3.26\n[BBOX-82] 57.7\n[BBOX-83] 2.21\n[BBOX-84] 17.6\n[BBOX-85] FEV3.0\n[BBOX-86] L\n[BBOX-87] 2.74\n[BBOX-88] 2.91\n[BBOX-89] 6.2\n[BBOX-90] FEV1.0%(G)\n[BBOX-91] %\n[BBOX-92] 63.95\n[BBOX-93] 73.89\n[BBOX-94] 86.5\n[BBOX-95] 73.42\n[BBOX-96] 14.8\n[BBOX-97] FEV1.0%(T)\n[BBOX-98] %\n[BBOX-99] 63.95\n[BBOX-100] FEV1/VCpr\n[BBOX-101] %\n[BBOX-102] 49.7\n[BBOX-103] 58.5\n[BBOX-104] 17.7\n[BBOX-105] MMF\n[BBOX-106] L/s\n[BBOX-107] 1.17\n[BBOX-108] 4.16\n[BBOX-109] 28.1\n[BBOX-110] 1.69\n[BBOX-111] 44.4\n[BBOX-112] PEF\n[BBOX-113] L/s\n[BBOX-114] 5.36\n[BBOX-115] 8.7\n[BBOX-116] 61.6\n[BBOX-117] 4.37\n[BBOX-118] -18.5\n[BBOX-119] FEF25\n[BBOX-120] L/s\n[BBOX-121] 2.3\n[BBOX-122] 7.82\n[BBOX-123] 29.4\n[BBOX-124] 3.84\n[BBOX-125] 67\n[BBOX-126] FEF50\n[BBOX-127] L/s\n[BBOX-128] 1.45\n[BBOX-129] 5.31\n[BBOX-130] 27.3\n[BBOX-131] 2.11\n[BBOX-132] 45.5\n[BBOX-133] FEF75\n[BBOX-134] L/s\n[BBOX-135] 0.61\n[BBOX-136] 2.39\n[BBOX-137] 25.5\n[BBOX-138] 0.7\n[BBOX-139] 14.8\n[BBOX-140] FEF90\n[BBOX-141] L/s\n[BBOX-142] 0.23\n[BBOX-143] 0.31\n[BBOX-144] 34.8\n[BBOX-145] FEF50/FEF75\n[BBOX-146] 2.38\n[BBOX-147] 3.01\n[BBOX-148] 26.5\n[BBOX-149] PEF/HT\n[BBOX-150] L/s/m\n[BBOX-151] 3.15\n[BBOX-152] 2.57\n[BBOX-153] -18.4\n[BBOX-154] FEF25/HT\n[BBOX-155] L/s/m\n[BBOX-156] 1.35\n[BBOX-157] 2.26\n[BBOX-158] 67.4\n[BBOX-159] FEF75-85\n[BBOX-160] L/s\n[BBOX-161] 0.47\n[BBOX-162] 0.53\n[BBOX-163] 12.8\n[BBOX-164] FEF0.2-1.2\n[BBOX-165] L/s\n[BBOX-166] 2.37\n[BBOX-167] 3.61\n[BBOX-168] 52.3\n[BBOX-169] OI\n[BBOX-170] L/s\n[BBOX-171] 5.21\n[BBOX-172] 2.19\n[BBOX-173] -58\n[BBOX-174] ATI\n[BBOX-175] %\n[BBOX-176] PEFTIME\n[BBOX-177] Sec\n[BBOX-178] 0.05\n[BBOX-179] 0.08\n[BBOX-180] 60\n[BBOX-181] FET\n[BBOX-182] Sec\n[BBOX-183] 4.46\n[BBOX-184] 3.72\n[BBOX-185] -16.6\n[BBOX-186] Vextrap\n[BBOX-187] L\n[BBOX-188] 0.05\n[BBOX-189] 0.09\n[BBOX-190] 80\n[BBOX-191] Extrap V\n[BBOX-192] %\n[BBOX-193] 1.7\n[BBOX-194] 2.99\n[BBOX-195] 75.9\n[BBOX-196] FIVC\n[BBOX-197] L\n[BBOX-198] 2.93\n[BBOX-199] 3.42\n[BBOX-200] 16.7\n[BBOX-201] MVV\n[BBOX-202] 实测\n[BBOX-203] 预测\n[BBOX-204] %预测\n[BBOX-205] BD后\n[BBOX-206] 改进率\n[BBOX-207] MVV\n[BBOX-208] L/min\n[BBOX-209] 126.6\n[BBOX-210] RR\n[BBOX-211] C/min\n[BBOX-212] TV\n[BBOX-213] L\n[BBOX-214] MVV/BSA\n[BBOX-215] L/min/m²\n[BBOX-216] AVI\n[BBOX-217] 诊断报告：\n[BBOX-218] FEV1% Restictive Normal\n[BBOX-219] SVC\n[BBOX-220] 70\n[BBOX-221] Mixed\n[BBOX-222] Obstructive\n[BBOX-223] 60\n[BBOX-224] %VC\n[BBOX-225] 3\n[BBOX-226] 0\n[BBOX-227] 30\n[BBOX-228] 50\n[BBOX-229] 90 SEC\n[BBOX-230] 12\n[BBOX-231] FVC\n[BBOX-232] 8\n[BBOX-233] 4\n[BBOX-234] 0\n[BBOX-235] 8 L\n[BBOX-236] -4\n[BBOX-237] -8\n[BBOX-238] -12\n[BBOX-239] 4L\n[BBOX-240] MVV\n[BBOX-241] 2\n[BBOX-242] 0\n[BBOX-243] 5\n[BBOX-244] 10\n[BBOX-245] 15 SEC\n[BBOX-246] 检查技师：\n[BBOX-247] 检查日期：2024-7-22\n[BBOX-248] CS 扫描全能王\n[BBOX-249] 3亿人都在用的扫描App"
  }
]
2026-08-10 13:02:53,417 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:53,433 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 1}
2026-08-10 13:02:53,441 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:02:53,441 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 13:02:53,441 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:02:53,442 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 1}
2026-08-10 13:02:53,449 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:02:53,449 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | ChunkRouter:Router | outputs={"html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:02:53,449 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:02:53,453 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:53,453 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:02:54,080 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:54,091 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:02:54,091 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:02:54,092 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:02:54,109 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:54,109 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:02:54,557 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:54,563 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:02:54,563 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:02:54,563 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:02:54,568 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:02:54,568 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:02:54,569 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:02:54,569 INFO     29 [qwen-vl-text] positions(25): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:02:54,569 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [25]
2026-08-10 13:02:54,711 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 13:02:54,711 INFO     29 [qwen-vl-text] LLM extraction start, text_len=315
2026-08-10 13:02:54,711 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:54,712 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 24, \"encounter_dates\": [\"2025-05-24\"], \"department\": \"呼吸与危重症医学二科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "初诊病历\n姓名：\n病历号：00125638\n科别：呼吸与危重症医学二科\n门诊\n性别：男\n身份证号：\n出生日期：1975-12-14\n年龄：49岁\n就诊序号：113598\n就诊日期：2025-05-24 10:38\n民族：民族\n联系电话：\n医保费别：自费\n详细地址：地址\n主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。\n现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。\n既往史：无\n过敏史：{否认食物、药物过敏史}。\n体格检查：{体温、脉搏、呼吸、血压未查}。\n辅助检查：无\n初步诊断：1、支气管哮喘\n处理意见：对症\n接诊医生：李志军\n签名时间：2025年05月24日10时38分",
    "role": "user"
  }
]
2026-08-10 13:02:56,103 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:56,103 INFO     29 [qwen-vl-text] LLM output (len=227):
{
  "encounter_date": "2025-05-24",
  "chief_complaint": "咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。",
  "present_illness": "咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。",
  "past_history": "无",
  "diagnosis": "1、支气管哮喘",
  "treatment_plan": "对症"
}
2026-08-10 13:02:56,103 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-24]
2026-08-10 13:02:56,105 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1124779, prompt_len=1003
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["初诊病历", "姓名：", "病历号：00125638", "科别：呼吸与危重症医学二科", "门诊", "性别：男", "身份证号：", "出生日期：1975-12-14", "年龄：49岁", "就诊序号：113598", "就诊日期：2025-05-24 10:38", "民族：民族", "联系电话：", "医保费别：自费", "详细地址：地址", "主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "既往史：无", "过敏史：{否认食物、药物过敏史}。", "体格检查：{体温、脉搏、呼吸、血压未查}。", "辅助检查：无", "初步诊断：1、支气管哮喘", "处理意见：对症", "接诊医生：李志军", "签名时间：2025年05月24日10时38分"]

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
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord API raw response (len=2012):
[
	{"text": "初诊病历", "bbox": [455, 13, 562, 48]},
	{"text": "姓名：", "bbox": [143, 73, 188, 100], "label": "姓名："},
	{"text": "病历号：00125638", "bbox": [326, 74, 479, 100], "label": "病历号：00125638"},
	{"text": "科别：呼吸与危重症医学二科", "bbox": [597, 73, 841, 100], "label": "科别：呼吸与危重症医学二科"},
	{"text": "门诊", "bbox": [589, 113, 636, 139], "label": "门诊"},
	{"text": "性别：男", "bbox": [144, 157, 227, 183], "label": "性别：男"},
	{"text": "身份证号：", "bbox": [328, 157, 407, 183], "label": "身份证号："},
	{"text": "出生日期：1975-12-14", "bbox": [596, 157, 784, 183], "label": "出生日期：1975-12-14"},
	{"text": "年龄：49岁", "bbox": [144, 197, 247, 223], "label": "年龄：49岁"},
	{"text": "就诊序号：113598", "bbox": [328, 197, 480, 223], "label": "就诊序号：113598"},
	{"text": "就诊日期：2025-05-24 10:38", "bbox": [596, 197, 836, 223], "label": "就诊日期：2025-05-24 10:38"},
	{"text": "民族：民族", "bbox": [145, 238, 247, 264], "label": "民族：民族"},
	{"text": "联系电话：", "bbox": [328, 238, 407, 264], "label": "联系电话："},
	{"text": "医保费别：自费", "bbox": [596, 238, 733, 264], "label": "医保费别：自费"},
	{"text": "详细地址：地址", "bbox": [144, 280, 274, 306], "label": "详细地址：地址"},
	{"text": "主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "bbox": [138, 321, 815, 348], "label": "主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。"},
	{"text": "现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "bbox": [138, 362, 834, 389], "label": "现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。"},
	{"text": "既往史：无", "bbox": [138, 403, 250, 429], "label": "既往史：无"},
	{"text": "过敏史：{否认食物、药物过敏史}。", "bbox": [138, 443, 443, 470], "label": "过敏史：{否认食物、药物过敏史}。"},
	{"text": "体格检查：{体温、脉搏、呼吸、血压未查}。", "bbox": [138, 483, 513, 510], "label": "体格检查：{体温、脉搏、呼吸、血压未查}。"},
	{"text": "辅助检查：无", "bbox": [138, 525, 270, 551], "label": "辅助检查：无"},
	{"text": "初步诊断：1、支气管哮喘", "bbox": [138, 566, 364, 593], "label": "初步诊断：1、支气管哮喘"},
	{"text": "处理意见：对症", "bbox": [138, 607, 285, 634], "label": "处理意见：对症"},
	{"text": "接诊医生：李志军", "bbox": [574, 689, 737, 715], "label": "接诊医生：李志军"},
	{"text": "签名时间：2025年05月24日10时38分", "bbox": [574, 730, 867, 756], "label": "签名时间：2025年05月24日10时38分"}
]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=11.8s
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[0]: text=初诊病历, bbox=[455, 13, 562, 48]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[143, 73, 188, 100]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[2]: text=病历号：00125638, bbox=[326, 74, 479, 100]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[3]: text=科别：呼吸与危重症医学二科, bbox=[597, 73, 841, 100]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[589, 113, 636, 139]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[144, 157, 227, 183]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[6]: text=身份证号：, bbox=[328, 157, 407, 183]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[7]: text=出生日期：1975-12-14, bbox=[596, 157, 784, 183]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：49岁, bbox=[144, 197, 247, 223]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[9]: text=就诊序号：113598, bbox=[328, 197, 480, 223]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[10]: text=就诊日期：2025-05-24 10:38, bbox=[596, 197, 836, 223]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[11]: text=民族：民族, bbox=[145, 238, 247, 264]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[12]: text=联系电话：, bbox=[328, 238, 407, 264]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[13]: text=医保费别：自费, bbox=[596, 238, 733, 264]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[14]: text=详细地址：地址, bbox=[144, 280, 274, 306]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。, bbox=[138, 321, 815, 348]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。, bbox=[138, 362, 834, 389]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：无, bbox=[138, 403, 250, 429]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[18]: text=过敏史：{否认食物、药物过敏史}。, bbox=[138, 443, 443, 470]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[19]: text=体格检查：{体温、脉搏、呼吸、血压未查}。, bbox=[138, 483, 513, 510]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查：无, bbox=[138, 525, 270, 551]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[21]: text=初步诊断：1、支气管哮喘, bbox=[138, 566, 364, 593]
2026-08-10 13:03:07,952 INFO     29 [qwen-vl-text] coord item[22]: text=处理意见：对症, bbox=[138, 607, 285, 634]
2026-08-10 13:03:07,953 INFO     29 [qwen-vl-text] coord item[23]: text=接诊医生：李志军, bbox=[574, 689, 737, 715]
2026-08-10 13:03:07,953 INFO     29 [qwen-vl-text] coord item[24]: text=签名时间：2025年05月24日10时38分, bbox=[574, 730, 867, 756]
2026-08-10 13:03:07,953 INFO     29 [qwen-vl-text] page=0 — 25/25 coords, api_time=11.8s
2026-08-10 13:03:07,953 INFO     29 [qwen-vl-text] new_positions (25):
[[0, 383.11, 473.204, 7.734999999999999, 28.56], [0, 120.40599999999999, 158.296, 43.434999999999995, 59.5], [0, 274.492, 403.318, 44.03, 59.5], [0, 502.674, 708.122, 43.434999999999995, 59.5], [0, 495.938, 535.512, 67.235, 82.705], [0, 121.24799999999999, 191.134, 93.41499999999999, 108.88499999999999], [0, 276.176, 342.69399999999996, 93.41499999999999, 108.88499999999999], [0, 501.832, 660.1279999999999, 93.41499999999999, 108.88499999999999], [0, 121.24799999999999, 207.974, 117.21499999999999, 132.685], [0, 276.176, 404.15999999999997, 117.21499999999999, 132.685], [0, 501.832, 703.9119999999999, 117.21499999999999, 132.685], [0, 122.08999999999999, 207.974, 141.60999999999999, 157.07999999999998], [0, 276.176, 342.69399999999996, 141.60999999999999, 157.07999999999998], [0, 501.832, 617.1859999999999, 141.60999999999999, 157.07999999999998], [0, 121.24799999999999, 230.708, 166.6, 182.07], [0, 116.196, 686.23, 190.995, 207.06], [0, 116.196, 702.228, 215.39, 231.45499999999998], [0, 116.196, 210.5, 239.785, 255.255], [0, 116.196, 373.006, 263.585, 279.65], [0, 116.196, 431.94599999999997, 287.385, 303.45], [0, 116.196, 227.34, 312.375, 327.84499999999997], [0, 116.196, 306.488, 336.77, 352.835], [0, 116.196, 239.97, 361.16499999999996, 377.22999999999996], [0, 483.308, 620.554, 409.955, 425.42499999999995], [0, 483.308, 730.014, 434.34999999999997, 449.82]]
2026-08-10 13:03:07,953 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=13.4s
2026-08-10 13:03:07,962 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:03:07,962 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:03:07,962 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:03:07,963 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:03:07.962+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 37, "failed": 0, "current": {"bdf0115294bb11f1bd9827cf206dfa2d": {"id": "bdf0115294bb11f1bd9827cf206dfa2d", "doc_id": "bdc001e294bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366949164, "task_type": "dataflow", "root_trace_id": "ba607da6f8e14f3789343d8e8c76e702", "root_traceparent": "00-ba607da6f8e14f3789343d8e8c76e702-655c145a91d3c0d4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:03:07,970 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:07,970 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:03:09,082 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:09,087 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:03:09,087 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:03:09,087 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:03:09,091 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:09,092 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:03:09,523 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:09,532 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:03:09,532 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:03:09,532 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:03:09,537 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:09,537 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:03:10,005 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:10,012 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:03:10,013 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:03:10,013 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:03:10,018 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:10,018 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:03:10,513 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:10,523 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:03:10,523 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:03:10,523 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:03:10,530 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:03:10,531 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:03:10,531 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:03:10,531 INFO     29 [qwen-vl-text] positions(223): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:03:10,531 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [223]
2026-08-10 13:03:10,731 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:03:10,732 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1117
2026-08-10 13:03:10,732 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:10,732 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 25, \"bbox_end\": 247, \"encounter_dates\": [\"2024-07-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "鹤煤总医院肺功能报告单\nID号：4000\n姓名：\n性别：男\n年龄：48\n身高：170 cm\n体重：95 kg\nB.S.A：2.06m²\n温度(℃)：22\n湿度(%)：50\n气压(mmHg)：1013.3\n科室：\n病区：\n预测公式：亚洲\n医生：李志军\n备注：\nSVC\n实测\n预测\n%预测\nBD后\n改进率\nVC\nL\n2.94\n3.78\n77.8\nIC\nL\nTV\nL\nERV\nL\nIRV\nL\nFVC\n实测\n预测\n%预测\nBD后\n改进率\nFVC\nL\n2.94\n3.78\n77.8\n3.01\n2.4\nFEV0.5\nL\n1.26\n1.62\n28.6\nFEV1.0\nL\n1.88\n3.26\n57.7\n2.21\n17.6\nFEV3.0\nL\n2.74\n2.91\n6.2\nFEV1.0%(G)\n%\n63.95\n73.89\n86.5\n73.42\n14.8\nFEV1.0%(T)\n%\n63.95\nFEV1/VCpr\n%\n49.7\n58.5\n17.7\nMMF\nL/s\n1.17\n4.16\n28.1\n1.69\n44.4\nPEF\nL/s\n5.36\n8.7\n61.6\n4.37\n-18.5\nFEF25\nL/s\n2.3\n7.82\n29.4\n3.84\n67\nFEF50\nL/s\n1.45\n5.31\n27.3\n2.11\n45.5\nFEF75\nL/s\n0.61\n2.39\n25.5\n0.7\n14.8\nFEF90\nL/s\n0.23\n0.31\n34.8\nFEF50/FEF75\n2.38\n3.01\n26.5\nPEF/HT\nL/s/m\n3.15\n2.57\n-18.4\nFEF25/HT\nL/s/m\n1.35\n2.26\n67.4\nFEF75-85\nL/s\n0.47\n0.53\n12.8\nFEF0.2-1.2\nL/s\n2.37\n3.61\n52.3\nOI\nL/s\n5.21\n2.19\n-58\nATI\n%\nPEFTIME\nSec\n0.05\n0.08\n60\nFET\nSec\n4.46\n3.72\n-16.6\nVextrap\nL\n0.05\n0.09\n80\nExtrap V\n%\n1.7\n2.99\n75.9\nFIVC\nL\n2.93\n3.42\n16.7\nMVV\n实测\n预测\n%预测\nBD后\n改进率\nMVV\nL/min\n126.6\nRR\nC/min\nTV\nL\nMVV/BSA\nL/min/m²\nAVI\n诊断报告：\nFEV1% Restictive Normal\nSVC\n70\nMixed\nObstructive\n60\n%VC\n3\n0\n30\n50\n90 SEC\n12\nFVC\n8\n4\n0\n8 L\n-4\n-8\n-12\n4L\nMVV\n2\n0\n5\n10\n15 SEC\n检查技师：\n检查日期：2024-7-22",
    "role": "user"
  }
]
2026-08-10 13:03:18,829 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:03:18,829 INFO     29 [qwen-vl-text] LLM output (len=1440):
{
  "exam_date": "2024-07-22",
  "report_date": null,
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "ID号：4000\n姓名：\n性别：男\n年龄：48\n身高：170 cm\n体重：95 kg\nB.S.A：2.06m²\n温度(℃)：22\n湿度(%)：50\n气压(mmHg)：1013.3\n科室：\n病区：\n预测公式：亚洲\n医生：李志军\n备注：\nSVC\n实测 预测 %预测 BD后 改进率\nVC L 2.94 3.78 77.8\nIC L\nTV L\nERV L\nIRV L\nFVC\n实测 预测 %预测 BD后 改进率\nFVC L 2.94 3.78 77.8 3.01 2.4\nFEV0.5 L 1.26 1.62 28.6\nFEV1.0 L 1.88 3.26 57.7 2.21 17.6\nFEV3.0 L 2.74 2.91 6.2\nFEV1.0%(G) % 63.95 73.89 86.5 73.42 14.8\nFEV1.0%(T) % 63.95\nFEV1/VCpr % 49.7 58.5 17.7\nMMF L/s 1.17 4.16 28.1 1.69 44.4\nPEF L/s 5.36 8.7 61.6 4.37 -18.5\nFEF25 L/s 2.3 7.82 29.4 3.84 67\nFEF50 L/s 1.45 5.31 27.3 2.11 45.5\nFEF75 L/s 0.61 2.39 25.5 0.7 14.8\nFEF90 L/s 0.23 0.31 34.8\nFEF50/FEF75 2.38 3.01 26.5\nPEF/HT L/s/m 3.15 2.57 -18.4\nFEF25/HT L/s/m 1.35 2.26 67.4\nFEF75-85 L/s 0.47 0.53 12.8\nFEF0.2-1.2 L/s 2.37 3.61 52.3\nOI L/s 5.21 2.19 -58\nATI %\nPEFTIME Sec 0.05 0.08 60\nFET Sec 4.46 3.72 -16.6\nVextrap L 0.05 0.09 80\nExtrap V % 1.7 2.99 75.9\nFIVC L 2.93 3.42 16.7\nMVV\n实测 预测 %预测 BD后 改进率\nMVV L/min 126.6\nRR C/min\nTV L\nMVV/BSA L/min/m²\nAVI",
  "conclusion": "诊断报告：\nFEV1% Restictive Normal\nSVC 70 Mixed Obstructive\n60 %VC 3 0 30 50 90 SEC 12 FVC 8 4 0 8 L -4 -8 -12 4L MVV 2 0 5 10 15 SEC",
  "physician": "李志军",
  "reviewer": null
}
2026-08-10 13:03:18,835 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1090086, prompt_len=2400
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共223行）
["鹤煤总医院肺功能报告单", "ID号：4000", "姓名：", "性别：男", "年龄：48", "身高：170 cm", "体重：95 kg", "B.S.A：2.06m²", "温度(℃)：22", "湿度(%)：50", "气压(mmHg)：1013.3", "科室：", "病区：", "预测公式：亚洲", "医生：李志军", "备注：", "SVC", "实测", "预测", "%预测", "BD后", "改进率", "VC", "L", "2.94", "3.78", "77.8", "IC", "L", "TV", "L", "ERV", "L", "IRV", "L", "FVC", "实测", "预测", "%预测", "BD后", "改进率", "FVC", "L", "2.94", "3.78", "77.8", "3.01", "2.4", "FEV0.5", "L", "1.26", "1.62", "28.6", "FEV1.0", "L", "1.88", "3.26", "57.7", "2.21", "17.6", "FEV3.0", "L", "2.74", "2.91", "6.2", "FEV1.0%(G)", "%", "63.95", "73.89", "86.5", "73.42", "14.8", "FEV1.0%(T)", "%", "63.95", "FEV1/VCpr", "%", "49.7", "58.5", "17.7", "MMF", "L/s", "1.17", "4.16", "28.1", "1.69", "44.4", "PEF", "L/s", "5.36", "8.7", "61.6", "4.37", "-18.5", "FEF25", "L/s", "2.3", "7.82", "29.4", "3.84", "67", "FEF50", "L/s", "1.45", "5.31", "27.3", "2.11", "45.5", "FEF75", "L/s", "0.61", "2.39", "25.5", "0.7", "14.8", "FEF90", "L/s", "0.23", "0.31", "34.8", "FEF50/FEF75", "2.38", "3.01", "26.5", "PEF/HT", "L/s/m", "3.15", "2.57", "-18.4", "FEF25/HT", "L/s/m", "1.35", "2.26", "67.4", "FEF75-85", "L/s", "0.47", "0.53", "12.8", "FEF0.2-1.2", "L/s", "2.37", "3.61", "52.3", "OI", "L/s", "5.21", "2.19", "-58", "ATI", "%", "PEFTIME", "Sec", "0.05", "0.08", "60", "FET", "Sec", "4.46", "3.72", "-16.6", "Vextrap", "L", "0.05", "0.09", "80", "Extrap V", "%", "1.7", "2.99", "75.9", "FIVC", "L", "2.93", "3.42", "16.7", "MVV", "实测", "预测", "%预测", "BD后", "改进率", "MVV", "L/min", "126.6", "RR", "C/min", "TV", "L", "MVV/BSA", "L/min/m²", "AVI", "诊断报告：", "FEV1% Restictive Normal", "SVC", "70", "Mixed", "Obstructive", "60", "%VC", "3", "0", "30", "50", "90 SEC", "12", "FVC", "8", "4", "0", "8 L", "-4", "-8", "-12", "4L", "MVV", "2", "0", "5", "10", "15 SEC", "检查技师：", "检查日期：2024-7-22"]

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
2026-08-10 13:04:14,871 INFO     29 [qwen-vl-text] coord API raw response (len=10796):
```json
[
	{"text": "鹤煤总医院肺功能报告单", "bbox": [327, 52, 613, 71]},
	{"text": "ID号：4000", "bbox": [64, 90, 145, 102]},
	{"text": "姓名：", "bbox": [226, 90, 266, 102]},
	{"text": "性别：男", "bbox": [392, 90, 457, 102]},
	{"text": "年龄：48", "bbox": [555, 88, 620, 100]},
	{"text": "身高：170 cm", "bbox": [721, 88, 819, 100]},
	{"text": "体重：95 kg", "bbox": [64, 110, 153, 123]},
	{"text": "B.S.A：2.06m²", "bbox": [226, 110, 335, 122]},
	{"text": "温度(℃)：22", "bbox": [392, 109, 490, 121]},
	{"text": "湿度(%)：50", "bbox": [555, 109, 645, 121]},
	{"text": "气压(mmHg)：1013.3", "bbox": [721, 108, 867, 120]},
	{"text": "科室：", "bbox": [64, 130, 102, 142]},
	{"text": "病区：", "bbox": [226, 130, 266, 142]},
	{"text": "预测公式：亚洲", "bbox": [392, 130, 506, 142]},
	{"text": "医生：李志军", "bbox": [555, 129, 652, 141]},
	{"text": "备注：", "bbox": [721, 129, 759, 141]},
	{"text": "SVC", "bbox": [117, 156, 144, 168]},
	{"text": "实测", "bbox": [231, 156, 264, 168]},
	{"text": "预测", "bbox": [302, 156, 335, 168]},
	{"text": "%预测", "bbox": [365, 156, 408, 168]},
	{"text": "BD后", "bbox": [440, 156, 473, 168]},
	{"text": "改进率", "bbox": [501, 156, 549, 168]},
	{"text": "VC", "bbox": [51, 171, 69, 183]},
	{"text": "L", "bbox": [201, 171, 210, 183]},
	{"text": "2.94", "bbox": [217, 171, 250, 183]},
	{"text": "3.78", "bbox": [286, 171, 320, 183]},
	{"text": "77.8", "bbox": [356, 171, 390, 183]},
	{"text": "IC", "bbox": [51, 187, 69, 199]},
	{"text": "L", "bbox": [201, 187, 210, 199]},
	{"text": "TV", "bbox": [51, 202, 67, 214]},
	{"text": "L", "bbox": [201, 202, 210, 214]},
	{"text": "ERV", "bbox": [51, 218, 76, 230]},
	{"text": "L", "bbox": [201, 218, 210, 230]},
	{"text": "IRV", "bbox": [51, 234, 76, 246]},
	{"text": "L", "bbox": [201, 234, 210, 246]},
	{"text": "FVC", "bbox": [117, 249, 145, 261]},
	{"text": "实测", "bbox": [231, 249, 264, 261]},
	{"text": "预测", "bbox": [302, 249, 335, 261]},
	{"text": "%预测", "bbox": [365, 249, 408, 261]},
	{"text": "BD后", "bbox": [440, 249, 473, 261]},
	{"text": "改进率", "bbox": [501, 249, 549, 261]},
	{"text": "FVC", "bbox": [51, 265, 78, 277]},
	{"text": "L", "bbox": [201, 265, 210, 277]},
	{"text": "2.94", "bbox": [217, 265, 250, 277]},
	{"text": "3.78", "bbox": [286, 265, 320, 277]},
	{"text": "77.8", "bbox": [356, 265, 390, 277]},
	{"text": "3.01", "bbox": [424, 265, 457, 277]},
	{"text": "2.4", "bbox": [493, 265, 519, 277]},
	{"text": "FEV0.5", "bbox": [51, 281, 102, 293]},
	{"text": "L", "bbox": [201, 281, 210, 293]},
	{"text": "1.26", "bbox": [217, 281, 250, 293]},
	{"text": "1.62", "bbox": [424, 281, 457, 293]},
	{"text": "28.6", "bbox": [493, 281, 526, 293]},
	{"text": "FEV1.0", "bbox": [51, 297, 102, 309]},
	{"text": "L", "bbox": [201, 297, 210, 309]},
	{"text": "1.88", "bbox": [217, 297, 250, 309]},
	{"text": "3.26", "bbox": [286, 297, 320, 309]},
	{"text": "57.7", "bbox": [356, 297, 390, 309]},
	{"text": "2.21", "bbox": [424, 297, 457, 309]},
	{"text": "17.6", "bbox": [493, 297, 526, 309]},
	{"text": "FEV3.0", "bbox": [51, 312, 102, 324]},
	{"text": "L", "bbox": [201, 312, 210, 324]},
	{"text": "2.74", "bbox": [217, 312, 250, 324]},
	{"text": "2.91", "bbox": [424, 312, 457, 324]},
	{"text": "6.2", "bbox": [493, 312, 519, 324]},
	{"text": "FEV1.0%(G)", "bbox": [51, 328, 132, 340]},
	{"text": "%", "bbox": [201, 328, 210, 340]},
	{"text": "63.95", "bbox": [217, 328, 259, 340]},
	{"text": "73.89", "bbox": [286, 328, 329, 340]},
	{"text": "86.5", "bbox": [356, 328, 390, 340]},
	{"text": "73.42", "bbox": [424, 328, 467, 340]},
	{"text": "14.8", "bbox": [493, 328, 526, 340]},
	{"text": "FEV1.0%(T)", "bbox": [51, 343, 132, 355]},
	{"text": "%", "bbox": [201, 343, 210, 355]},
	{"text": "63.95", "bbox": [217, 343, 259, 355]},
	{"text": "FEV1/VCpr", "bbox": [51, 359, 127, 371]},
	{"text": "%", "bbox": [201, 359, 210, 371]},
	{"text": "49.7", "bbox": [217, 359, 250, 371]},
	{"text": "58.5", "bbox": [424, 359, 457, 371]},
	{"text": "17.7", "bbox": [493, 359, 526, 371]},
	{"text": "MMF", "bbox": [51, 374, 79, 386]},
	{"text": "L/s", "bbox": [185, 374, 210, 386]},
	{"text": "1.17", "bbox": [217, 374, 250, 386]},
	{"text": "4.16", "bbox": [286, 374, 320, 386]},
	{"text": "28.1", "bbox": [356, 374, 390, 386]},
	{"text": "1.69", "bbox": [424, 374, 457, 386]},
	{"text": "44.4", "bbox": [493, 374, 526, 386]},
	{"text": "PEF", "bbox": [51, 389, 79, 401]},
	{"text": "L/s", "bbox": [185, 389, 210, 401]},
	{"text": "5.36", "bbox": [217, 389, 250, 401]},
	{"text": "8.7", "bbox": [286, 389, 312, 401]},
	{"text": "61.6", "bbox": [356, 389, 390, 401]},
	{"text": "4.37", "bbox": [424, 389, 457, 401]},
	{"text": "-18.5", "bbox": [493, 389, 535, 401]},
	{"text": "FEF25", "bbox": [51, 404, 95, 416]},
	{"text": "L/s", "bbox": [185, 404, 210, 416]},
	{"text": "2.3", "bbox": [217, 404, 242, 416]},
	{"text": "7.82", "bbox": [286, 404, 320, 416]},
	{"text": "29.4", "bbox": [356, 404, 390, 416]},
	{"text": "3.84", "bbox": [424, 404, 457, 416]},
	{"text": "67", "bbox": [493, 404, 511, 416]},
	{"text": "FEF50", "bbox": [51, 420, 95, 432]},
	{"text": "L/s", "bbox": 185, 420, 210, 432]},
	{"text": "1.45", "bbox": [217, 420, 250, 432]},
	{"text": "5.31", "bbox": [286, 420, 320, 432]},
	{"text": "27.3", "bbox": [356, 420, 390, 432]},
	{"text": "2.11", "bbox": [424, 420, 457, 432]},
	{"text": "45.5", "bbox": [493, 420, 526, 432]},
	{"text": "FEF75", "bbox": [51, 435, 95, 447]},
	{"text": "L/s", "bbox": 185, 435, 210, 447]},
	{"text": "0.61", "bbox": [217, 435, 250, 447]},
	{"text": "2.39", "bbox": 286, 435, 320, 447]},
	{"text": "25.5", "bbox": 356, 435, 390, 447]},
	{"text": "0.7", "bbox": 424, 435, 451, 447]},
	{"text": "14.8", "bbox": 493, 435, 526, 447]},
	{"text": "FEF90", "bbox": 51, 450, 95, 462]},
	{"text": "L/s", "bbox": 185, 450, 210, 462]},
	{"text": "0.23", "bbox": 217, 450, 250, 462]},
	{"text": "0.31", "bbox": 424, 450, 457, 462]},
	{"text": "34.8", "bbox": 493, 450, 526, 462]},
	{"text": "FEF50/FEF75", "bbox": 51, 465, 144, 477]},
	{"text": "2.38", "bbox": 217, 465, 250, 477]},
	{"text": "3.01", "bbox": 424, 465, 457, 477]},
	{"text": "26.5", "bbox": 493, 465, 526, 477]},
	{"text": "PEF/HT", "bbox": 51, 480, 104, 492]},
	{"text": "L/s/m", "bbox": 171, 480, 210, 492]},
	{"text": "3.15", "bbox": 217, 480, 250, 492]},
	{"text": "2.57", "bbox": 424, 480, 457, 492]},
	{"text": "-18.4", "bbox": 493, 480, 535, 492]},
	{"text": "FEF25/HT", "bbox": 51, 496, 119, 508]},
	{"text": "L/s/m", "bbox": 171, 496, 210, 508]},
	{"text": "1.35", "bbox": 217, 496, 250, 508]},
	{"text": "2.26", "bbox": 424, 496, 457, 508]},
	{"text": "67.4", "bbox": 493, 496, 526, 508]},
	{"text": "FEF75-85", "bbox": 51, 511, 119, 523]},
	{"text": "L/s", "bbox": 185, 511, 210, 523]},
	{"text": "0.47", "bbox": 217, 511, 250, 523]},
	{"text": "0.53", "bbox": 424, 511, 457, 523]},
	{"text": "12.8", "bbox": 493, 511, 526, 523]},
	{"text": "FEF0.2-1.2", "bbox": 51, 526, 136, 538]},
	{"text": "L/s", "bbox": 185, 526, 210, 538]},
	{"text": "2.37", "bbox": 217, 526, 250, 538]},
	{"text": "3.61", "bbox": 424, 526, 457, 538]},
	{"text": "52.3", "bbox": 493, 526, 526, 538]},
	{"text": "OI", "bbox": 51, 542, 69, 554]},
	{"text": "L/s", "bbox": 185, 542, 210, 554]},
	{"text": "5.21", "bbox": 217, 542, 250, 554]},
	{"text": "2.19", "bbox": 424, 542, 457, 554]},
	{"text": "-58", "bbox": 493, 542, 519, 554]},
	{"text": "ATI", "bbox": 51, 557, 79, 569]},
	{"text": "%", "bbox": 201, 557, 210, 569]},
	{"text": "PEFTIME", "bbox": 51, 572, 111, 584]},
	{"text": "Sec", "bbox": 185, 572, 210, 584]},
	{"text": "0.05", "bbox": 217, 572, 250, 584]},
	{"text": "0.08", "bbox": 424, 572, 457, 584]},
	{"text": "60", "bbox": 493, 572, 511, 584]},
	{"text": "FET", "bbox": 51, 588, 79, 600]},
	{"text": "Sec", "bbox": 185, 588, 210, 600]},
	{"text": "4.46", "bbox": 217, 588, 250, 600]},
	{"text": "3.72", "bbox": 424, 588, 457, 600]},
	{"text": "-16.6", "bbox": 493, 588, 535, 600]},
	{"text": "Vextrap", "bbox": 51, 603, 111, 615]},
	{"text": "L", "bbox": 201, 603, 210, 615]},
	{"text": "0.05", "bbox": 217, 603, 250, 615]},
	{"text": "0.09", "bbox": 424, 603, 457, 615]},
	{"text": "80", "bbox": 493, 603, 511, 615]},
	{"text": "Extrap V", "bbox": 51, 618, 119, 630]},
	{"text": "%", "bbox": 201, 618, 210, 630]},
	{"text": "1.7", "bbox": 217, 618, 242, 630]},
	{"text": "2.99", "bbox": 424, 618, 457, 630]},
	{"text": "75.9", "bbox": 493, 618, 526, 630]},
	{"text": "FIVC", "bbox": 51, 633, 89, 645]},
	{"text": "L", "bbox": 201, 633, 210, 645]},
	{"text": "2.93", "bbox": 217, 633, 250, 645]},
	{"text": "3.42", "bbox": 424, 633, 457, 645]},
	{"text": "16.7", "bbox": 493, 633, 526, 645]},
	{"text": "MVV", "bbox": [119, 649, 145, 661]},
	{"text": "实测", "bbox": [231, 649, 264, 661]},
	{"text": "预测", "bbox": 302, 649, 335, 661]},
	{"text": "%预测", "bbox": 365, 649, 408, 661]},
	{"text": "BD后", "bbox": 440, 649, 473, 661]},
	{"text": "改进率", "bbox": 501, 649, 549, 661]},
	{"text": "MVV", "bbox": 51, 664, 79, 676]},
	{"text": "L/min", "bbox": 171, 664, 210, 676]},
	{"text": "126.6", "bbox": 286, 664, 329, 676]},
	{"text": "RR", "bbox": 51, 680, 71, 692]},
	{"text": "C/min", "bbox": 171, 680, 210, 692]},
	{"text": "TV", "bbox": 51, 695, 71, 707]},
	{"text": "L", "bbox": 201, 695, 210, 707]},
	{"text": "MVV/BSA", "bbox": 51, 710, 111, 722]},
	{"text": "L/min/m²", "bbox": 145, 710, 210, 722]},
	{"text": "AVI", "bbox": 51, 726, 79, 738]},
	{"text": "诊断报告：", "bbox": [71, 740, 141, 752]},
	{"text": "FEV1% Restictive Normal", "bbox": [747, 164, 908, 173]},
	{"text": "SVC", "bbox": [698, 180, 724, 190]},
	{"text": "70", "bbox": [766, 189, 780, 198]},
	{"text": "Mixed", "bbox": [794, 221, 827, 229]},
	{"text": "Obstructive", "bbox": [865, 220, 935, 228]},
	{"text": "60", "bbox": [856, 234, 870, 242]},
	{"text": "%VC", "bbox": [893, 234, 913, 242]},
	{"text": "3", "bbox": [580, 245, 594, 255]},
	{"text": "0", "bbox": [590, 318, 600, 328]},
	{"text": "30", "bbox": [680, 317, 698, 327]},
	{"text": "50", "bbox": [774, 317, 792, 327]},
	{"text": "90 SEC", "bbox": [854, 316, 908, 327]},
	{"text": "12", "bbox": [575, 364, 594, 374]},
	{"text": "FVC", "bbox": [696, 363, 725, 373]},
	{"text": "8", "bbox": [584, 406, 594, 416]},
	{"text": "4", "bbox": [584, 447, 594, 457]},
	{"text": "0", "bbox": [584, 488, 594, 498]},
	{"text": "8 L", "bbox": [865, 494, 895, 505]},
	{"text": "-4", "bbox": [575, 529, 594, 539]},
	{"text": "-8", "bbox": [575, 570, 594, 580]},
	{"text": "-12", "bbox": [565, 611, 594, 621]},
	{"text": "4L", "bbox": [575, 690, 594, 700]},
	{"text": "MVV", "bbox": [699, 690, 725, 700]},
	{"text": "2", "bbox": [584, 752, 594, 762]},
	{"text": "0", "bbox": [590, 825, 600, 835]},
	{"text": "5", "bbox": [688, 825, 698, 835]},
	{"text": "10", "bbox": [781, 825, 799, 835]},
	{"text": "15 SEC", "bbox": [858, 825, 913, 835]},
	{"text": "检查技师：", "bbox": [53, 870, 122, 882]},
	{"text": "检查日期：2024-7-22", "bbox": [751, 870, 907, 882]}
]
```
2026-08-10 13:04:14,872 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord API: raw_items=223, valid_items=142, elapsed=56.0s
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[0]: text=鹤煤总医院肺功能报告单, bbox=[327, 52, 613, 71]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[1]: text=ID号：4000, bbox=[64, 90, 145, 102]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[226, 90, 266, 102]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[392, 90, 457, 102]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：48, bbox=[555, 88, 620, 100]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[5]: text=身高：170 cm, bbox=[721, 88, 819, 100]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[6]: text=体重：95 kg, bbox=[64, 110, 153, 123]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[7]: text=B.S.A：2.06m², bbox=[226, 110, 335, 122]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[8]: text=温度(℃)：22, bbox=[392, 109, 490, 121]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[9]: text=湿度(%)：50, bbox=[555, 109, 645, 121]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[10]: text=气压(mmHg)：1013.3, bbox=[721, 108, 867, 120]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[11]: text=科室：, bbox=[64, 130, 102, 142]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[12]: text=病区：, bbox=[226, 130, 266, 142]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[13]: text=预测公式：亚洲, bbox=[392, 130, 506, 142]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[14]: text=医生：李志军, bbox=[555, 129, 652, 141]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[15]: text=备注：, bbox=[721, 129, 759, 141]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[16]: text=SVC, bbox=[117, 156, 144, 168]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[17]: text=实测, bbox=[231, 156, 264, 168]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[18]: text=预测, bbox=[302, 156, 335, 168]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[19]: text=%预测, bbox=[365, 156, 408, 168]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[20]: text=BD后, bbox=[440, 156, 473, 168]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[21]: text=改进率, bbox=[501, 156, 549, 168]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[22]: text=VC, bbox=[51, 171, 69, 183]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[23]: text=L, bbox=[201, 171, 210, 183]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[24]: text=2.94, bbox=[217, 171, 250, 183]
2026-08-10 13:04:14,876 INFO     29 [qwen-vl-text] coord item[25]: text=3.78, bbox=[286, 171, 320, 183]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[26]: text=77.8, bbox=[356, 171, 390, 183]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[27]: text=IC, bbox=[51, 187, 69, 199]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[28]: text=L, bbox=[201, 187, 210, 199]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[29]: text=TV, bbox=[51, 202, 67, 214]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[30]: text=L, bbox=[201, 202, 210, 214]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[31]: text=ERV, bbox=[51, 218, 76, 230]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[32]: text=L, bbox=[201, 218, 210, 230]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[33]: text=IRV, bbox=[51, 234, 76, 246]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[34]: text=L, bbox=[201, 234, 210, 246]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[35]: text=FVC, bbox=[117, 249, 145, 261]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[36]: text=实测, bbox=[231, 249, 264, 261]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[37]: text=预测, bbox=[302, 249, 335, 261]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[38]: text=%预测, bbox=[365, 249, 408, 261]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[39]: text=BD后, bbox=[440, 249, 473, 261]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[40]: text=改进率, bbox=[501, 249, 549, 261]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[41]: text=FVC, bbox=[51, 265, 78, 277]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[42]: text=L, bbox=[201, 265, 210, 277]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[43]: text=2.94, bbox=[217, 265, 250, 277]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[44]: text=3.78, bbox=[286, 265, 320, 277]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[45]: text=77.8, bbox=[356, 265, 390, 277]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[46]: text=3.01, bbox=[424, 265, 457, 277]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[47]: text=2.4, bbox=[493, 265, 519, 277]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[48]: text=FEV0.5, bbox=[51, 281, 102, 293]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[49]: text=L, bbox=[201, 281, 210, 293]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[50]: text=1.26, bbox=[217, 281, 250, 293]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[51]: text=1.62, bbox=[424, 281, 457, 293]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[52]: text=28.6, bbox=[493, 281, 526, 293]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[53]: text=FEV1.0, bbox=[51, 297, 102, 309]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[54]: text=L, bbox=[201, 297, 210, 309]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[55]: text=1.88, bbox=[217, 297, 250, 309]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[56]: text=3.26, bbox=[286, 297, 320, 309]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[57]: text=57.7, bbox=[356, 297, 390, 309]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[58]: text=2.21, bbox=[424, 297, 457, 309]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[59]: text=17.6, bbox=[493, 297, 526, 309]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[60]: text=FEV3.0, bbox=[51, 312, 102, 324]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[61]: text=L, bbox=[201, 312, 210, 324]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[62]: text=2.74, bbox=[217, 312, 250, 324]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[63]: text=2.91, bbox=[424, 312, 457, 324]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[64]: text=6.2, bbox=[493, 312, 519, 324]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[65]: text=FEV1.0%(G), bbox=[51, 328, 132, 340]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[66]: text=%, bbox=[201, 328, 210, 340]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[67]: text=63.95, bbox=[217, 328, 259, 340]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[68]: text=73.89, bbox=[286, 328, 329, 340]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[69]: text=86.5, bbox=[356, 328, 390, 340]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[70]: text=73.42, bbox=[424, 328, 467, 340]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[71]: text=14.8, bbox=[493, 328, 526, 340]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[72]: text=FEV1.0%(T), bbox=[51, 343, 132, 355]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[73]: text=%, bbox=[201, 343, 210, 355]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[74]: text=63.95, bbox=[217, 343, 259, 355]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[75]: text=FEV1/VCpr, bbox=[51, 359, 127, 371]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[76]: text=%, bbox=[201, 359, 210, 371]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[77]: text=49.7, bbox=[217, 359, 250, 371]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[78]: text=58.5, bbox=[424, 359, 457, 371]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[79]: text=17.7, bbox=[493, 359, 526, 371]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[80]: text=MMF, bbox=[51, 374, 79, 386]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[81]: text=L/s, bbox=[185, 374, 210, 386]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[82]: text=1.17, bbox=[217, 374, 250, 386]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[83]: text=4.16, bbox=[286, 374, 320, 386]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[84]: text=28.1, bbox=[356, 374, 390, 386]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[85]: text=1.69, bbox=[424, 374, 457, 386]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[86]: text=44.4, bbox=[493, 374, 526, 386]
2026-08-10 13:04:14,877 INFO     29 [qwen-vl-text] coord item[87]: text=PEF, bbox=[51, 389, 79, 401]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[88]: text=L/s, bbox=[185, 389, 210, 401]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[89]: text=5.36, bbox=[217, 389, 250, 401]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[90]: text=8.7, bbox=[286, 389, 312, 401]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[91]: text=61.6, bbox=[356, 389, 390, 401]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[92]: text=4.37, bbox=[424, 389, 457, 401]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[93]: text=-18.5, bbox=[493, 389, 535, 401]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[94]: text=FEF25, bbox=[51, 404, 95, 416]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[95]: text=L/s, bbox=[185, 404, 210, 416]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[96]: text=2.3, bbox=[217, 404, 242, 416]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[97]: text=7.82, bbox=[286, 404, 320, 416]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[98]: text=29.4, bbox=[356, 404, 390, 416]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[99]: text=3.84, bbox=[424, 404, 457, 416]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[100]: text=67, bbox=[493, 404, 511, 416]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[101]: text=FEF50, bbox=[51, 420, 95, 432]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[102]: text=1.45, bbox=[217, 420, 250, 432]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[103]: text=5.31, bbox=[286, 420, 320, 432]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[104]: text=27.3, bbox=[356, 420, 390, 432]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[105]: text=2.11, bbox=[424, 420, 457, 432]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[106]: text=45.5, bbox=[493, 420, 526, 432]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[107]: text=FEF75, bbox=[51, 435, 95, 447]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[108]: text=0.61, bbox=[217, 435, 250, 447]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[109]: text=MVV, bbox=[119, 649, 145, 661]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[110]: text=实测, bbox=[231, 649, 264, 661]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[111]: text=诊断报告：, bbox=[71, 740, 141, 752]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[112]: text=FEV1% Restictive Normal, bbox=[747, 164, 908, 173]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[113]: text=SVC, bbox=[698, 180, 724, 190]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[114]: text=70, bbox=[766, 189, 780, 198]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[115]: text=Mixed, bbox=[794, 221, 827, 229]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[116]: text=Obstructive, bbox=[865, 220, 935, 228]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[117]: text=60, bbox=[856, 234, 870, 242]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[118]: text=%VC, bbox=[893, 234, 913, 242]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[119]: text=3, bbox=[580, 245, 594, 255]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[120]: text=0, bbox=[590, 318, 600, 328]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[121]: text=30, bbox=[680, 317, 698, 327]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[122]: text=50, bbox=[774, 317, 792, 327]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[123]: text=90 SEC, bbox=[854, 316, 908, 327]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[124]: text=12, bbox=[575, 364, 594, 374]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[125]: text=FVC, bbox=[696, 363, 725, 373]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[126]: text=8, bbox=[584, 406, 594, 416]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[127]: text=4, bbox=[584, 447, 594, 457]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[128]: text=0, bbox=[584, 488, 594, 498]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[129]: text=8 L, bbox=[865, 494, 895, 505]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[130]: text=-4, bbox=[575, 529, 594, 539]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[131]: text=-8, bbox=[575, 570, 594, 580]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[132]: text=-12, bbox=[565, 611, 594, 621]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[133]: text=4L, bbox=[575, 690, 594, 700]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[134]: text=MVV, bbox=[699, 690, 725, 700]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[135]: text=2, bbox=[584, 752, 594, 762]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[136]: text=0, bbox=[590, 825, 600, 835]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[137]: text=5, bbox=[688, 825, 698, 835]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[138]: text=10, bbox=[781, 825, 799, 835]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[139]: text=15 SEC, bbox=[858, 825, 913, 835]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[140]: text=检查技师：, bbox=[53, 870, 122, 882]
2026-08-10 13:04:14,878 INFO     29 [qwen-vl-text] coord item[141]: text=检查日期：2024-7-22, bbox=[751, 870, 907, 882]
2026-08-10 13:04:14,890 INFO     29 [qwen-vl-text] page=1 — 210/223 coords, api_time=56.0s
2026-08-10 13:04:14,890 INFO     29 [qwen-vl-text] new_positions (223):
[[1, 194.565, 364.73499999999996, 43.784, 59.782], [1, 38.08, 86.27499999999999, 75.78, 85.884], [1, 134.47, 158.26999999999998, 75.78, 85.884], [1, 233.23999999999998, 271.91499999999996, 75.78, 85.884], [1, 330.22499999999997, 368.9, 74.096, 84.2], [1, 428.995, 487.30499999999995, 74.096, 84.2], [1, 38.08, 91.035, 92.61999999999999, 103.566], [1, 134.47, 199.325, 92.61999999999999, 102.72399999999999], [1, 233.23999999999998, 291.55, 91.77799999999999, 101.88199999999999], [1, 330.22499999999997, 383.775, 91.77799999999999, 101.88199999999999], [1, 428.995, 515.865, 90.93599999999999, 101.03999999999999], [1, 38.08, 60.69, 109.46, 119.564], [1, 134.47, 158.26999999999998, 109.46, 119.564], [1, 233.23999999999998, 301.07, 109.46, 119.564], [1, 330.22499999999997, 387.94, 108.618, 118.722], [1, 428.995, 451.60499999999996, 108.618, 118.722], [1, 69.615, 85.67999999999999, 131.352, 141.456], [1, 137.445, 157.07999999999998, 131.352, 141.456], [1, 179.69, 199.325, 131.352, 141.456], [1, 217.17499999999998, 242.76, 131.352, 141.456], [1, 261.8, 281.435, 131.352, 141.456], [1, 298.09499999999997, 326.655, 131.352, 141.456], [1, 30.345, 41.055, 143.982, 154.08599999999998], [1, 119.595, 124.94999999999999, 143.982, 154.08599999999998], [1, 129.11499999999998, 148.75, 143.982, 154.08599999999998], [1, 170.17, 190.39999999999998, 143.982, 154.08599999999998], [1, 211.82, 232.04999999999998, 143.982, 154.08599999999998], [1, 30.345, 41.055, 157.454, 167.558], [1, 119.595, 124.94999999999999, 157.454, 167.558], [1, 30.345, 39.864999999999995, 170.084, 180.188], [1, 119.595, 124.94999999999999, 170.084, 180.188], [1, 30.345, 45.22, 183.55599999999998, 193.66], [1, 119.595, 124.94999999999999, 183.55599999999998, 193.66], [1, 30.345, 45.22, 197.028, 207.132], [1, 119.595, 124.94999999999999, 197.028, 207.132], [1, 69.615, 86.27499999999999, 209.658, 219.762], [1, 137.445, 157.07999999999998, 209.658, 219.762], [1, 179.69, 199.325, 209.658, 219.762], [1, 217.17499999999998, 242.76, 209.658, 219.762], [1, 261.8, 281.435, 209.658, 219.762], [1, 298.09499999999997, 326.655, 209.658, 219.762], [1, 30.345, 46.41, 223.13, 233.23399999999998], [1, 119.595, 124.94999999999999, 223.13, 233.23399999999998], [1, 129.11499999999998, 148.75, 223.13, 233.23399999999998], [1, 170.17, 190.39999999999998, 223.13, 233.23399999999998], [1, 211.82, 232.04999999999998, 223.13, 233.23399999999998], [1, 252.28, 271.91499999999996, 223.13, 233.23399999999998], [1, 293.335, 308.805, 223.13, 233.23399999999998], [1, 30.345, 60.69, 236.602, 246.706], [1, 119.595, 124.94999999999999, 236.602, 246.706], [1, 129.11499999999998, 148.75, 236.602, 246.706], [1, 252.28, 271.91499999999996, 236.602, 246.706], [1, 293.335, 312.96999999999997, 236.602, 246.706], [1, 30.345, 60.69, 250.07399999999998, 260.178], [1, 119.595, 124.94999999999999, 250.07399999999998, 260.178], [1, 129.11499999999998, 148.75, 250.07399999999998, 260.178], [1, 170.17, 190.39999999999998, 250.07399999999998, 260.178], [1, 211.82, 232.04999999999998, 250.07399999999998, 260.178], [1, 252.28, 271.91499999999996, 250.07399999999998, 260.178], [1, 293.335, 312.96999999999997, 250.07399999999998, 260.178], [1, 30.345, 60.69, 262.704, 272.808], [1, 119.595, 124.94999999999999, 262.704, 272.808], [1, 129.11499999999998, 148.75, 262.704, 272.808], [1, 252.28, 271.91499999999996, 262.704, 272.808], [1, 293.335, 308.805, 262.704, 272.808], [1, 30.345, 78.53999999999999, 276.176, 286.28], [1, 119.595, 124.94999999999999, 276.176, 286.28], [1, 129.11499999999998, 154.105, 276.176, 286.28], [1, 170.17, 195.755, 276.176, 286.28], [1, 211.82, 232.04999999999998, 276.176, 286.28], [1, 252.28, 277.865, 276.176, 286.28], [1, 293.335, 312.96999999999997, 276.176, 286.28], [1, 30.345, 78.53999999999999, 288.806, 298.90999999999997], [1, 119.595, 124.94999999999999, 288.806, 298.90999999999997], [1, 129.11499999999998, 154.105, 288.806, 298.90999999999997], [1, 30.345, 75.565, 302.27799999999996, 312.382], [1, 119.595, 124.94999999999999, 302.27799999999996, 312.382], [1, 129.11499999999998, 148.75, 302.27799999999996, 312.382], [1, 252.28, 271.91499999999996, 302.27799999999996, 312.382], [1, 293.335, 312.96999999999997, 302.27799999999996, 312.382], [1, 30.345, 47.004999999999995, 314.908, 325.012], [1, 110.07499999999999, 124.94999999999999, 314.908, 325.012], [1, 129.11499999999998, 148.75, 314.908, 325.012], [1, 170.17, 190.39999999999998, 314.908, 325.012], [1, 211.82, 232.04999999999998, 314.908, 325.012], [1, 252.28, 271.91499999999996, 314.908, 325.012], [1, 293.335, 312.96999999999997, 314.908, 325.012], [1, 30.345, 47.004999999999995, 327.538, 337.642], [1, 110.07499999999999, 124.94999999999999, 327.538, 337.642], [1, 129.11499999999998, 148.75, 327.538, 337.642], [1, 170.17, 185.64, 327.538, 337.642], [1, 211.82, 232.04999999999998, 327.538, 337.642], [1, 252.28, 271.91499999999996, 327.538, 337.642], [1, 293.335, 318.325, 327.538, 337.642], [1, 30.345, 56.525, 340.168, 350.272], [1, 110.07499999999999, 124.94999999999999, 340.168, 350.272], [1, 129.11499999999998, 143.98999999999998, 340.168, 350.272], [1, 170.17, 190.39999999999998, 340.168, 350.272], [1, 211.82, 232.04999999999998, 340.168, 350.272], [1, 252.28, 271.91499999999996, 340.168, 350.272], [1, 293.335, 304.04499999999996, 340.168, 350.272], [1, 30.345, 56.525, 353.64, 363.74399999999997], [1, 129.11499999999998, 148.75, 353.64, 363.74399999999997], [1, 170.17, 190.39999999999998, 353.64, 363.74399999999997], [1, 211.82, 232.04999999999998, 353.64, 363.74399999999997], [1, 252.28, 271.91499999999996, 353.64, 363.74399999999997], [1, 293.335, 312.96999999999997, 353.64, 363.74399999999997], [1, 30.345, 56.525, 366.27, 376.37399999999997], [1, 129.11499999999998, 148.75, 366.27, 376.37399999999997], [1, 70.80499999999999, 86.27499999999999, 546.458, 556.562], [1, 137.445, 157.07999999999998, 546.458, 556.562], [1, 42.245, 83.895, 623.0799999999999, 633.184], [1, 444.465, 540.26, 138.088, 145.666], [1, 415.31, 430.78, 151.56, 159.98], [1, 455.77, 464.09999999999997, 159.138, 166.716], [1, 472.43, 492.065, 186.082, 192.81799999999998], [1, 514.675, 556.3249999999999, 185.23999999999998, 191.976], [1, 509.32, 517.65, 197.028, 203.76399999999998], [1, 531.3349999999999, 543.235, 197.028, 203.76399999999998], [1, 345.09999999999997, 353.43, 206.29, 214.70999999999998], [1, 351.05, 357.0, 267.756, 276.176], [1, 404.59999999999997, 415.31, 266.914, 275.334], [1, 460.53, 471.23999999999995, 266.914, 275.334], [1, 508.13, 540.26, 266.072, 275.334], [1, 342.125, 353.43, 306.488, 314.908], [1, 414.12, 431.375, 305.646, 314.066], [1, 347.47999999999996, 353.43, 341.852, 350.272], [1, 347.47999999999996, 353.43, 376.37399999999997, 384.794], [1, 347.47999999999996, 353.43, 410.89599999999996, 419.316], [1, 514.675, 532.525, 415.948, 425.21], [1, 342.125, 353.43, 445.418, 453.83799999999997], [1, 342.125, 353.43, 479.94, 488.35999999999996], [1, 336.175, 353.43, 514.462, 522.882], [1, 342.125, 353.43, 580.98, 589.4], [1, 415.905, 431.375, 580.98, 589.4], [1, 347.47999999999996, 353.43, 633.184, 641.6039999999999], [1, 351.05, 357.0, 694.65, 703.0699999999999], [1, 409.35999999999996, 415.31, 694.65, 703.0699999999999], [1, 464.695, 475.405, 694.65, 703.0699999999999], [1, 510.51, 543.235, 694.65, 703.0699999999999], [1, 31.535, 72.59, 732.54, 742.644], [1, 446.84499999999997, 539.665, 732.54, 742.644], [1, 252.28, 271.91499999999996, 223.13, 233.23399999999998], [1, 129.11499999999998, 148.75, 327.538, 337.642], [1, 30.345, 41.055, 157.454, 167.558], [1, 110.07499999999999, 124.94999999999999, 340.168, 350.272], [1, 252.28, 271.91499999999996, 250.07399999999998, 260.178], [1, 129.11499999999998, 148.75, 223.13, 233.23399999999998], [1, 342.125, 353.43, 479.94, 488.35999999999996], [1, 0, 0, 0, 0], [1, 119.595, 124.94999999999999, 302.27799999999996, 312.382], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 252.28, 271.91499999999996, 223.13, 233.23399999999998], [1, 170.17, 190.39999999999998, 223.13, 233.23399999999998], [1, 509.32, 517.65, 197.028, 203.76399999999998], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 170.17, 190.39999999999998, 314.908, 325.012], [1, 170.17, 190.39999999999998, 223.13, 233.23399999999998], [1, 129.11499999999998, 148.75, 236.602, 246.706], [1, 0, 0, 0, 0], [1, 119.595, 124.94999999999999, 262.704, 272.808], [1, 252.28, 271.91499999999996, 223.13, 233.23399999999998], [1, 129.11499999999998, 148.75, 223.13, 233.23399999999998], [1, 455.77, 464.09999999999997, 159.138, 166.716], [1, 0, 0, 0, 0], [1, 119.595, 124.94999999999999, 302.27799999999996, 312.382], [1, 293.335, 312.96999999999997, 302.27799999999996, 312.382], [1, 129.11499999999998, 148.75, 223.13, 233.23399999999998], [1, 170.17, 195.755, 276.176, 286.28], [1, 414.12, 431.375, 305.646, 314.066], [1, 119.595, 124.94999999999999, 262.704, 272.808], [1, 129.11499999999998, 148.75, 223.13, 233.23399999999998], [1, 252.28, 277.865, 276.176, 286.28], [1, 293.335, 312.96999999999997, 302.27799999999996, 312.382], [1, 415.905, 431.375, 580.98, 589.4], [1, 137.445, 157.07999999999998, 546.458, 556.562], [1, 179.69, 199.325, 209.658, 219.762], [1, 217.17499999999998, 242.76, 209.658, 219.762], [1, 261.8, 281.435, 209.658, 219.762], [1, 298.09499999999997, 326.655, 209.658, 219.762], [1, 415.905, 431.375, 580.98, 589.4], [1, 0, 0, 0, 0], [1, 129.11499999999998, 148.75, 236.602, 246.706], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 30.345, 39.864999999999995, 170.084, 180.188], [1, 119.595, 124.94999999999999, 262.704, 272.808], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 42.245, 83.895, 623.0799999999999, 633.184], [1, 444.465, 540.26, 138.088, 145.666], [1, 415.31, 430.78, 151.56, 159.98], [1, 455.77, 464.09999999999997, 159.138, 166.716], [1, 472.43, 492.065, 186.082, 192.81799999999998], [1, 514.675, 556.3249999999999, 185.23999999999998, 191.976], [1, 509.32, 517.65, 197.028, 203.76399999999998], [1, 531.3349999999999, 543.235, 197.028, 203.76399999999998], [1, 345.09999999999997, 353.43, 206.29, 214.70999999999998], [1, 351.05, 357.0, 694.65, 703.0699999999999], [1, 404.59999999999997, 415.31, 266.914, 275.334], [1, 460.53, 471.23999999999995, 266.914, 275.334], [1, 508.13, 540.26, 266.072, 275.334], [1, 342.125, 353.43, 306.488, 314.908], [1, 414.12, 431.375, 305.646, 314.066], [1, 347.47999999999996, 353.43, 341.852, 350.272], [1, 347.47999999999996, 353.43, 376.37399999999997, 384.794], [1, 351.05, 357.0, 694.65, 703.0699999999999], [1, 514.675, 532.525, 415.948, 425.21], [1, 342.125, 353.43, 445.418, 453.83799999999997], [1, 342.125, 353.43, 479.94, 488.35999999999996], [1, 336.175, 353.43, 514.462, 522.882], [1, 342.125, 353.43, 580.98, 589.4], [1, 415.905, 431.375, 580.98, 589.4], [1, 347.47999999999996, 353.43, 633.184, 641.6039999999999], [1, 351.05, 357.0, 694.65, 703.0699999999999], [1, 409.35999999999996, 415.31, 694.65, 703.0699999999999], [1, 464.695, 475.405, 694.65, 703.0699999999999], [1, 510.51, 543.235, 694.65, 703.0699999999999], [1, 31.535, 72.59, 732.54, 742.644], [1, 446.84499999999997, 539.665, 732.54, 742.644]]
2026-08-10 13:04:14,891 INFO     29 [qwen-vl-text] ═══ DONE ═══ 223 positions, pages=1, time=64.4s
2026-08-10 13:04:14,903 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:04:14,903 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:04:14,904 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:04:14,904 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:04:14.904+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 37, "failed": 0, "current": {"bdf0115294bb11f1bd9827cf206dfa2d": {"id": "bdf0115294bb11f1bd9827cf206dfa2d", "doc_id": "bdc001e294bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366949164, "task_type": "dataflow", "root_trace_id": "ba607da6f8e14f3789343d8e8c76e702", "root_traceparent": "00-ba607da6f8e14f3789343d8e8c76e702-655c145a91d3c0d4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:04:14,909 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:14,909 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:04:15,994 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:04:16,006 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:04:16,006 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "250 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:04:16,006 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:04:16,007 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:04:16,021 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:04:16,021 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "GWHU-48岁-男(2).pdf"}
2026-08-10 13:04:16,021 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:04:16,051 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786366950578, 'update_date': datetime.datetime(2026, 8, 10, 13, 2, 30), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1021172, 'status': '1'}
2026-08-10 13:04:16,288 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=初诊病历
姓名：
病历号：00125638
科别：呼吸与危重症医学二科
门诊
性别：男
身份证号：
出生日期：1975-12-14
年龄：49岁
就诊序号：113598
就诊日期：2025-05-24 10:38
民族：民族
联系电话：
医保费别：自费
详细地址：地址
主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。
现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。
既往史：无
过敏史：{否认食物、药物过敏史}。
体格检查：{体温、脉搏、呼吸、血压未查}。
辅助检查：无
初步诊断：1、支气管哮喘
处理意见：对症
接诊医生：李志军
签名时间：2025年05月24日10时38分
---
鹤煤总医院肺功能报告单
ID号：4000
姓名：
性别：男
年龄：48
身高：170 cm
体重：95 kg
B.S.A：2.06m²
温度(℃)：22
湿度(%)：50
气压(mmHg)：1013.3
科室：
病区：
预测公式：亚洲
医生：李志军
备注：
SVC
实测
预测
%预测
BD后
改进率
VC
L
2.94
3.78
77.8
IC
L
TV
L
ERV
L
IRV
L
FVC
实测
预测
%预测
BD后
改进率
FVC
L
2.94
3.78
77.8
3.01
2.4
FEV0.5
L
1.26
1.62
28.6
FEV1.0
L
1.88
3.26
57.7
2.21
17.6
FEV3.0
L
2.74
2.91
6.2
FEV1.0%(G)
%
63.95
73.89
86.5
73.42
14.8
FEV1.0%(T)
%
63.95
FEV1/VCpr
%
49.7
58.5
17.7
MMF
L/s
1.17
4.16
28.1
1.69
44.4
PEF
L/s
5.36
8.7
61.6
4.37
-18.5
FEF25
L/s
2.3
7.82
29.4
3.84
67
FEF50
L/s
1.45
5.31
27.3
2.11
45.5
FEF75
L/s
0.61
2.39
25.5
0.7
14.8
FEF90
L/s
0.23
0.31
34.8
FEF50/FEF75
2.38
3.01
26.5
PEF/HT
L/s/m
3.15
2.57
-18.4
FEF25/HT
L/s/m
1.35
2.26
67.4
FEF75-85
L/s
0.47
0.53
12.8
FEF0.2-1.2
L/s
2.37
3.61
52.3
OI
L/s
5.21
2.19
-58
ATI
%
PEFTIME
Sec
0.05
0.08
60
FET
Sec
4.46
3.72
-16.6
Vextrap
L
0.05
0.09
80
Extrap V
%
1.7
2.99
75.9
FIVC
L
2.93
3.42
16.7
MVV
实测
预测
%预测
BD后
改进率
MVV
L/min
126.6
RR
C/min
TV
L
MVV/BSA
L/min/m²
AVI
诊断报告：
FEV1% Restictive Normal
SVC
70
Mixed
Obstructive
60
%VC
3
0
30
50
90 SEC
12
FVC
8
4
0
8 L
-4
-8
-12
4L
MVV
2
0
5
10
15 SEC
检查技师：
检查日期：2024-7-22
2026-08-10 13:04:16,503 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:04:16,503 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "GWHU-48岁-男(2).pdf", "embedding_token_consumption": 1198}
2026-08-10 13:04:16,504 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:04:16,801 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:04:16,801 INFO     29 [Trace] task=bdf01152 | doc=GWHU-48岁-男(2).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:04:16,803 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:04:16,803 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:04:16,807 INFO     29 set_progress(bdf0115294bb11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:04:16 [DOC Engine]:
Start to index...
2026-08-10 13:04:16,815 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.005s]
2026-08-10 13:04:16,819 INFO     29 set_progress(bdf0115294bb11f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 13:04:16,824 INFO     29 set_progress(bdf0115294bb11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:04:16 Indexing done (0.02s). Task done (100.80s)
2026-08-10 13:04:16,828 INFO     29 [Done], chunks(2), token(1198), elapsed:100.80
2026-08-10 13:04:16,891 INFO     29 handle_task done for task {"id": "bdf0115294bb11f1bd9827cf206dfa2d", "doc_id": "bdc001e294bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786366949164, "task_type": "dataflow", "root_trace_id": "ba607da6f8e14f3789343d8e8c76e702", "root_traceparent": "00-ba607da6f8e14f3789343d8e8c76e702-655c145a91d3c0d4-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
