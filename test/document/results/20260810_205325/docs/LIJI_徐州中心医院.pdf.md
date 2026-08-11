# 基准结果：LIJI 徐州中心医院.pdf

## 基本信息

- 文件：`LIJI 徐州中心医院.pdf`
- 大小：235.8 KB
- PDF 总页数：2
- doc_id：`4630c9da94bc11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:06:16  完成时间：2026-08-10T21:08:21  耗时：124.5s
- progress_msg：`13:08:18 Indexing done (0.02s). Task done (114.49s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 4cc26b00 | 1 | 1-1 | 徐州矿务集团总医院 徐州医科大学第二附属医院 间病房入、出院记录 ：十二病区护理 |
| 2 | bb290e50 | 1 | 2-2 | 徐州医科大学附属医院 肺功能检查报告 舒张试验 姓名： 科别： 性别： 身高：1 |

- chunks 总数：2
- 各 chunk 页数合计（含跨页重复）：2
- 页码并集：`[1, 2]`
- 覆盖页数：2 / 2；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"DischargeRecord": 1, "ExaminationReport": 1}`
- ChunkMerger：`{"found": true, "merged": 2, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:08:16,850 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:06:18,179 INFO     29 handle_task begin for task {"id": "465f3f9094bc11f1bd9827cf206dfa2d", "doc_id": "4630c9da94bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "type": "pdf", "location": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "size": 241486, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367178063, "task_type": "dataflow", "root_trace_id": "c90b5c4d512840ec92722025b8967e21", "root_traceparent": "00-c90b5c4d512840ec92722025b8967e21-6b6dbfd12195e555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:06:18,385 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:06:18,501 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:06:18,510 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:06:18,510 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:06:18,510 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:06:18,515 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:06:18,515 INFO     29 ============================================================
2026-08-10 13:06:18,515 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:06:18,516 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:06:18,516 INFO     29 ============================================================
2026-08-10 13:06:18,516 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:06:18,516 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:06:18,517 INFO     29 No torch found.
2026-08-10 13:06:18,764 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=2
2026-08-10 13:06:19,057 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1666518, prompt_len=764
2026-08-10 13:06:20,492 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:06:20,493 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:06:20,507 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1666518, prompt_len=401
2026-08-10 13:06:27,055 INFO     29 [qwen-vl-parser] text API response (len=1124):
["徐州矿务集团总医院", "徐州医科大学第二附属医院", "间病房入、出院记录", "：十二病区护理单元 床号：6 住院号：00214234", "工作单位：-", "性别：女", "年龄：49岁", "籍贯：江苏省徐州市泉山区", "民族：汉族", "婚姻：已婚", "职业：职工", "住址：江苏徐州市", "供史者与（患者关系）：本人", "入院日期：2025-04-23 09:05:08", "记录日期：2025年04月25日08时29分", "主诉：声音嘶哑10余天", "入院情况：患者因“声音嘶哑10余天”入院。查体：会厌无肿胀，杓会厌襞稍充血肿胀，室带无新生物，右侧声", "带边缘息肉样隆起，表面光滑，声门闭合不全。辅助检查：电子喉镜（2025-04-20本院）示：舌扁桃体增生，会", "厌无充血，声带稍肿胀，活动可，右侧声带边缘息肉样肿物，声门闭合欠佳，杓间区稍红肿。", "入院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。", "手术名称：1.内镜下声带病损切除术（内镜下声带病损切除术）", "年04月24日", "手术日期：2025", "诊疗经过：入院后完善血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十", "二通道）（20250423094755）：窦性心动过缓CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：", "左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶", "钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。手术指征明确，无明显手术禁忌，", "昨日全麻下行喉镜下声带病损切除术，手术顺利，术后予抗炎消肿、雾化等对症治疗，恢复可，要求今日出院。", "出院情况：（）治愈 口好转 口未愈 口未治 口转院 口自动出院）伤口愈合：-", "患者一般情况可，声音嘶哑，稍咽痛，无吞咽疼痛，无咽部出血，无发热，饮食睡眠可，大小便正常。查体：神", "志清，精神可，心肺无明显异常。咽喉部粘膜充血，会厌无充血肿胀，杓会厌襞粘膜无肿胀，双侧声带稍水肿，", "声门闭合良好。", "出院诊断：出院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。", "出院日期：2025-04-25", "出院医嘱：1.注意声休2周，禁食辛辣刺激，2.口服黄氏响声丸/西瓜霜含片，3.2-3周后复查喉镜；4.门诊随诊", "X光片号：", "CT号：", "MRI号：", "病理号：", "医师签名：", "门诊病历已交病人或家属，签收人：", "主治医师签名：", "第1页"]
2026-08-10 13:06:27,056 INFO     29 [qwen-vl-parser] page=1 text: 43 lines (bbox 0-42)
2026-08-10 13:06:27,056 INFO     29 [qwen-vl-parser] page=1 text: 43 sections
2026-08-10 13:06:27,250 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1092568, prompt_len=764
2026-08-10 13:06:28,584 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:06:28,584 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:06:28,592 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1092568, prompt_len=401
2026-08-10 13:06:37,830 INFO     29 [qwen-vl-parser] text API response (len=1910):
["徐州医科大学附属医院", "肺功能检查报告", "舒张试验", "姓名：", "科别：", "性别：", "身高：158 cm", "号：210254", "/住院号：门诊", "48 岁", "体重：49.6 kg", "Flow [L/s]", "F/V ex", "Volume [L]", "CO [%]", "0.30", "0.25", "0.20", "0.15", "0.10", "0.05", "0.00", "0", "10", "5", "0", "5", "10", "1", "2", "3", "4", "5", "6", "7", "F/V in", "Time [s]", "0", "10", "20", "30", "40", "50", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "日期", "24-11-29", "24-11-29", "时间", "10:51:30", "11:27:38", "VT", "[L]", "0.35", "0.42", "118.7", "BF", "[1/min]", "20.00", "19.20", "96.0", "MV", "[L/min]", "7.09", "8.07", "113.9", "VC MAX", "[L]", "2.93", "2.48", "84.6", "2.78", "94.9", "12.2", "ERV", "[L]", "0.96", "1.10", "115.1", "IC", "[L]", "1.97", "1.37", "69.7", "FVC", "[L]", "2.86", "2.48", "86.6", "2.73", "95.3", "10.0", "FEV 1", "[L]", "2.44", "1.64", "67.3", "1.86", "76.4", "13.5", "FEV 1 % FVC", "[%]", "82.57", "66.28", "80.3", "68.41", "82.9", "3.2", "FEV 1 % VC MAX", "[%]", "79.98", "66.28", "82.9", "67.06", "83.8", "1.2", "PEF", "[L/s]", "6.14", "4.14", "67.4", "4.24", "69.1", "2.5", "MEF 75", "[L/s]", "5.49", "2.43", "44.2", "3.22", "58.7", "32.8", "MEF 50", "[L/s]", "3.63", "1.22", "31.8", "1.38", "36.1", "13.6", "MEF 25", "[L/s]", "1.57", "0.38", "24.2", "0.41", "25.9", "7.4", "MMEF 75/25", "[L/s]", "3.26", "0.94", "28.7", "1.06", "32.4", "13.1", "V backextrapolation ex [L]", "0.07", "0.07", "0.2", "V backextrapol. % FVC [%]", "2.64", "2.40", "-9.0", "MVV", "[L/min]", "95.44", "64.07", "67.1", "55.95", "58.6", "13.5", "FEV 1*30", "[L/min]", "95.44", "49.27", "51.6", "TLC-SB", "[L]", "4.64", "4.76", "102.7", "FRC-SB", "[L]", "2.59", "3.27", "126.5", "RV-SB", "[L]", "1.63", "2.30", "141.5", "RV%TLC-SB", "[%]", "35.28", "48.35", "137.1", "DLCO SB", "[mmol/min/kPa]", "7.83", "5.92", "75.5", "DLCO/VA", "[mmol/min/kPa/L]", "1.69", "1.27", "75.3", "结论：", "中度阻塞性通气功能障碍", "残总比增高", "弥散功能轻度障碍", "可逆试验阳性（13.5%），绝对值增加220ml。", "医生：", "检查者：", "审核者："]
2026-08-10 13:06:37,831 INFO     29 [qwen-vl-parser] page=2 text: 219 lines (bbox 43-261)
2026-08-10 13:06:37,831 INFO     29 [qwen-vl-parser] page=2 text: 219 sections
2026-08-10 13:06:37,831 INFO     29 [qwen-vl-parser] parse_pdf done: 262 sections from 2 pages.
2026-08-10 13:06:37,839 INFO     29 Close text detector.
2026-08-10 13:06:38,266 INFO     29 Close text recognizer.
2026-08-10 13:06:38,645 INFO     29 Close recognizer.
2026-08-10 13:06:39,041 INFO     29 Close recognizer.
2026-08-10 13:06:39,490 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:06:39,490 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Parser:MedLink | outputs={"html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "json"}
2026-08-10 13:06:39,490 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:06:39,506 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:39,506 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 徐州矿务集团总医院\n[BBOX-1] 徐州医科大学第二附属医院\n[BBOX-2] 间病房入、出院记录\n[BBOX-3] ：十二病区护理单元 床号：6 住院号：00214234\n[BBOX-4] 工作单位：-\n[BBOX-5] 性别：女\n[BBOX-6] 年龄：49岁\n[BBOX-7] 籍贯：江苏省徐州市泉山区\n[BBOX-8] 民族：汉族\n[BBOX-9] 婚姻：已婚\n[BBOX-10] 职业：职工\n[BBOX-11] 住址：江苏徐州市\n[BBOX-12] 供史者与（患者关系）：本人\n[BBOX-13] 入院日期：2025-04-23 09:05:08\n[BBOX-14] 记录日期：2025年04月25日08时29分\n[BBOX-15] 主诉：声音嘶哑10余天\n[BBOX-16] 入院情况：患者因“声音嘶哑10余天”入院。查体：会厌无肿胀，杓会厌襞稍充血肿胀，室带无新生物，右侧声\n[BBOX-17] 带边缘息肉样隆起，表面光滑，声门闭合不全。辅助检查：电子喉镜（2025-04-20本院）示：舌扁桃体增生，会\n[BBOX-18] 厌无充血，声带稍肿胀，活动可，右侧声带边缘息肉样肿物，声门闭合欠佳，杓间区稍红肿。\n[BBOX-19] 入院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。\n[BBOX-20] 手术名称：1.内镜下声带病损切除术（内镜下声带病损切除术）\n[BBOX-21] 年04月24日\n[BBOX-22] 手术日期：2025\n[BBOX-23] 诊疗经过：入院后完善血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十\n[BBOX-24] 二通道）（20250423094755）：窦性心动过缓CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：\n[BBOX-25] 左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶\n[BBOX-26] 钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。手术指征明确，无明显手术禁忌，\n[BBOX-27] 昨日全麻下行喉镜下声带病损切除术，手术顺利，术后予抗炎消肿、雾化等对症治疗，恢复可，要求今日出院。\n[BBOX-28] 出院情况：（）治愈 口好转 口未愈 口未治 口转院 口自动出院）伤口愈合：-\n[BBOX-29] 患者一般情况可，声音嘶哑，稍咽痛，无吞咽疼痛，无咽部出血，无发热，饮食睡眠可，大小便正常。查体：神\n[BBOX-30] 志清，精神可，心肺无明显异常。咽喉部粘膜充血，会厌无充血肿胀，杓会厌襞粘膜无肿胀，双侧声带稍水肿，\n[BBOX-31] 声门闭合良好。\n[BBOX-32] 出院诊断：出院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。\n[BBOX-33] 出院日期：2025-04-25\n[BBOX-34] 出院医嘱：1.注意声休2周，禁食辛辣刺激，2.口服黄氏响声丸/西瓜霜含片，3.2-3周后复查喉镜；4.门诊随诊\n[BBOX-35] X光片号：\n[BBOX-36] CT号：\n[BBOX-37] MRI号：\n[BBOX-38] 病理号：\n[BBOX-39] 医师签名：\n[BBOX-40] 门诊病历已交病人或家属，签收人：\n[BBOX-41] 主治医师签名：\n[BBOX-42] 第1页\n[BBOX-43] 徐州医科大学附属医院\n[BBOX-44] 肺功能检查报告\n[BBOX-45] 舒张试验\n[BBOX-46] 姓名：\n[BBOX-47] 科别：\n[BBOX-48] 性别：\n[BBOX-49] 身高：158 cm\n[BBOX-50] 号：210254\n[BBOX-51] /住院号：门诊\n[BBOX-52] 48 岁\n[BBOX-53] 体重：49.6 kg\n[BBOX-54] Flow [L/s]\n[BBOX-55] F/V ex\n[BBOX-56] Volume [L]\n[BBOX-57] CO [%]\n[BBOX-58] 0.30\n[BBOX-59] 0.25\n[BBOX-60] 0.20\n[BBOX-61] 0.15\n[BBOX-62] 0.10\n[BBOX-63] 0.05\n[BBOX-64] 0.00\n[BBOX-65] 0\n[BBOX-66] 10\n[BBOX-67] 5\n[BBOX-68] 0\n[BBOX-69] 5\n[BBOX-70] 10\n[BBOX-71] 1\n[BBOX-72] 2\n[BBOX-73] 3\n[BBOX-74] 4\n[BBOX-75] 5\n[BBOX-76] 6\n[BBOX-77] 7\n[BBOX-78] F/V in\n[BBOX-79] Time [s]\n[BBOX-80] 0\n[BBOX-81] 10\n[BBOX-82] 20\n[BBOX-83] 30\n[BBOX-84] 40\n[BBOX-85] 50\n[BBOX-86] 预计值\n[BBOX-87] 前次\n[BBOX-88] 前/预\n[BBOX-89] 后次\n[BBOX-90] 后/预\n[BBOX-91] 改善率\n[BBOX-92] 日期\n[BBOX-93] 24-11-29\n[BBOX-94] 24-11-29\n[BBOX-95] 时间\n[BBOX-96] 10:51:30\n[BBOX-97] 11:27:38\n[BBOX-98] VT\n[BBOX-99] [L]\n[BBOX-100] 0.35\n[BBOX-101] 0.42\n[BBOX-102] 118.7\n[BBOX-103] BF\n[BBOX-104] [1/min]\n[BBOX-105] 20.00\n[BBOX-106] 19.20\n[BBOX-107] 96.0\n[BBOX-108] MV\n[BBOX-109] [L/min]\n[BBOX-110] 7.09\n[BBOX-111] 8.07\n[BBOX-112] 113.9\n[BBOX-113] VC MAX\n[BBOX-114] [L]\n[BBOX-115] 2.93\n[BBOX-116] 2.48\n[BBOX-117] 84.6\n[BBOX-118] 2.78\n[BBOX-119] 94.9\n[BBOX-120] 12.2\n[BBOX-121] ERV\n[BBOX-122] [L]\n[BBOX-123] 0.96\n[BBOX-124] 1.10\n[BBOX-125] 115.1\n[BBOX-126] IC\n[BBOX-127] [L]\n[BBOX-128] 1.97\n[BBOX-129] 1.37\n[BBOX-130] 69.7\n[BBOX-131] FVC\n[BBOX-132] [L]\n[BBOX-133] 2.86\n[BBOX-134] 2.48\n[BBOX-135] 86.6\n[BBOX-136] 2.73\n[BBOX-137] 95.3\n[BBOX-138] 10.0\n[BBOX-139] FEV 1\n[BBOX-140] [L]\n[BBOX-141] 2.44\n[BBOX-142] 1.64\n[BBOX-143] 67.3\n[BBOX-144] 1.86\n[BBOX-145] 76.4\n[BBOX-146] 13.5\n[BBOX-147] FEV 1 % FVC\n[BBOX-148] [%]\n[BBOX-149] 82.57\n[BBOX-150] 66.28\n[BBOX-151] 80.3\n[BBOX-152] 68.41\n[BBOX-153] 82.9\n[BBOX-154] 3.2\n[BBOX-155] FEV 1 % VC MAX\n[BBOX-156] [%]\n[BBOX-157] 79.98\n[BBOX-158] 66.28\n[BBOX-159] 82.9\n[BBOX-160] 67.06\n[BBOX-161] 83.8\n[BBOX-162] 1.2\n[BBOX-163] PEF\n[BBOX-164] [L/s]\n[BBOX-165] 6.14\n[BBOX-166] 4.14\n[BBOX-167] 67.4\n[BBOX-168] 4.24\n[BBOX-169] 69.1\n[BBOX-170] 2.5\n[BBOX-171] MEF 75\n[BBOX-172] [L/s]\n[BBOX-173] 5.49\n[BBOX-174] 2.43\n[BBOX-175] 44.2\n[BBOX-176] 3.22\n[BBOX-177] 58.7\n[BBOX-178] 32.8\n[BBOX-179] MEF 50\n[BBOX-180] [L/s]\n[BBOX-181] 3.63\n[BBOX-182] 1.22\n[BBOX-183] 31.8\n[BBOX-184] 1.38\n[BBOX-185] 36.1\n[BBOX-186] 13.6\n[BBOX-187] MEF 25\n[BBOX-188] [L/s]\n[BBOX-189] 1.57\n[BBOX-190] 0.38\n[BBOX-191] 24.2\n[BBOX-192] 0.41\n[BBOX-193] 25.9\n[BBOX-194] 7.4\n[BBOX-195] MMEF 75/25\n[BBOX-196] [L/s]\n[BBOX-197] 3.26\n[BBOX-198] 0.94\n[BBOX-199] 28.7\n[BBOX-200] 1.06\n[BBOX-201] 32.4\n[BBOX-202] 13.1\n[BBOX-203] V backextrapolation ex [L]\n[BBOX-204] 0.07\n[BBOX-205] 0.07\n[BBOX-206] 0.2\n[BBOX-207] V backextrapol. % FVC [%]\n[BBOX-208] 2.64\n[BBOX-209] 2.40\n[BBOX-210] -9.0\n[BBOX-211] MVV\n[BBOX-212] [L/min]\n[BBOX-213] 95.44\n[BBOX-214] 64.07\n[BBOX-215] 67.1\n[BBOX-216] 55.95\n[BBOX-217] 58.6\n[BBOX-218] 13.5\n[BBOX-219] FEV 1*30\n[BBOX-220] [L/min]\n[BBOX-221] 95.44\n[BBOX-222] 49.27\n[BBOX-223] 51.6\n[BBOX-224] TLC-SB\n[BBOX-225] [L]\n[BBOX-226] 4.64\n[BBOX-227] 4.76\n[BBOX-228] 102.7\n[BBOX-229] FRC-SB\n[BBOX-230] [L]\n[BBOX-231] 2.59\n[BBOX-232] 3.27\n[BBOX-233] 126.5\n[BBOX-234] RV-SB\n[BBOX-235] [L]\n[BBOX-236] 1.63\n[BBOX-237] 2.30\n[BBOX-238] 141.5\n[BBOX-239] RV%TLC-SB\n[BBOX-240] [%]\n[BBOX-241] 35.28\n[BBOX-242] 48.35\n[BBOX-243] 137.1\n[BBOX-244] DLCO SB\n[BBOX-245] [mmol/min/kPa]\n[BBOX-246] 7.83\n[BBOX-247] 5.92\n[BBOX-248] 75.5\n[BBOX-249] DLCO/VA\n[BBOX-250] [mmol/min/kPa/L]\n[BBOX-251] 1.69\n[BBOX-252] 1.27\n[BBOX-253] 75.3\n[BBOX-254] 结论：\n[BBOX-255] 中度阻塞性通气功能障碍\n[BBOX-256] 残总比增高\n[BBOX-257] 弥散功能轻度障碍\n[BBOX-258] 可逆试验阳性（13.5%），绝对值增加220ml。\n[BBOX-259] 医生：\n[BBOX-260] 检查者：\n[BBOX-261] 审核者："
  }
]
2026-08-10 13:06:41,013 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:06:41.012+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 39, "failed": 0, "current": {"465f3f9094bc11f1bd9827cf206dfa2d": {"id": "465f3f9094bc11f1bd9827cf206dfa2d", "doc_id": "4630c9da94bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "type": "pdf", "location": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "size": 241486, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367178063, "task_type": "dataflow", "root_trace_id": "c90b5c4d512840ec92722025b8967e21", "root_traceparent": "00-c90b5c4d512840ec92722025b8967e21-6b6dbfd12195e555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:06:44,659 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:44,677 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'DischargeRecord': 1, 'ExaminationReport': 1}
2026-08-10 13:06:44,688 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:06:44,688 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks": "2 items, types={'DischargeRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 13:06:44,688 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:06:44,689 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Discharge': 1, 'chunks_Examination': 1}
2026-08-10 13:06:44,698 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:06:44,698 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | ChunkRouter:Router | outputs={"html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks": "2 items, types={'DischargeRecord': 1, 'ExaminationReport': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:06:44,698 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:06:44,703 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:44,703 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:06:45,271 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:45,276 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:06:45,277 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:06:45,277 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:06:45,281 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:45,281 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:06:45,708 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:45,712 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:06:45,713 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:06:45,713 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:06:45,716 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:45,716 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:06:46,212 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:46,219 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:06:46,220 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:06:46,220 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:06:46,227 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:46,227 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:06:46,903 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:46,908 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:06:46,909 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:06:46,909 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:06:46,913 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:46,913 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:06:47,325 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:47,330 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:06:47,330 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:06:47,330 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:06:47,335 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:06:47,336 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:06:47,336 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 13:06:47,336 INFO     29 [qwen-vl-text] positions(43): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:06:47,336 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [43]
2026-08-10 13:06:47,545 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:06:47,546 INFO     29 [qwen-vl-text] LLM extraction start, text_len=994
2026-08-10 13:06:47,546 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:47,546 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 0, \"bbox_end\": 42, \"encounter_dates\": [\"2025-04-23\", \"2025-04-25\"], \"department\": \"十二病区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "徐州矿务集团总医院\n徐州医科大学第二附属医院\n间病房入、出院记录\n：十二病区护理单元 床号：6 住院号：00214234\n工作单位：-\n性别：女\n年龄：49岁\n籍贯：江苏省徐州市泉山区\n民族：汉族\n婚姻：已婚\n职业：职工\n住址：江苏徐州市\n供史者与（患者关系）：本人\n入院日期：2025-04-23 09:05:08\n记录日期：2025年04月25日08时29分\n主诉：声音嘶哑10余天\n入院情况：患者因“声音嘶哑10余天”入院。查体：会厌无肿胀，杓会厌襞稍充血肿胀，室带无新生物，右侧声\n带边缘息肉样隆起，表面光滑，声门闭合不全。辅助检查：电子喉镜（2025-04-20本院）示：舌扁桃体增生，会\n厌无充血，声带稍肿胀，活动可，右侧声带边缘息肉样肿物，声门闭合欠佳，杓间区稍红肿。\n入院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。\n手术名称：1.内镜下声带病损切除术（内镜下声带病损切除术）\n年04月24日\n手术日期：2025\n诊疗经过：入院后完善血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十\n二通道）（20250423094755）：窦性心动过缓CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：\n左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶\n钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。手术指征明确，无明显手术禁忌，\n昨日全麻下行喉镜下声带病损切除术，手术顺利，术后予抗炎消肿、雾化等对症治疗，恢复可，要求今日出院。\n出院情况：（）治愈 口好转 口未愈 口未治 口转院 口自动出院）伤口愈合：-\n患者一般情况可，声音嘶哑，稍咽痛，无吞咽疼痛，无咽部出血，无发热，饮食睡眠可，大小便正常。查体：神\n志清，精神可，心肺无明显异常。咽喉部粘膜充血，会厌无充血肿胀，杓会厌襞粘膜无肿胀，双侧声带稍水肿，\n声门闭合良好。\n出院诊断：出院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。\n出院日期：2025-04-25\n出院医嘱：1.注意声休2周，禁食辛辣刺激，2.口服黄氏响声丸/西瓜霜含片，3.2-3周后复查喉镜；4.门诊随诊\nX光片号：\nCT号：\nMRI号：\n病理号：\n医师签名：\n门诊病历已交病人或家属，签收人：\n主治医师签名：\n第1页",
    "role": "user"
  }
]
2026-08-10 13:06:55,942 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:06:55,942 INFO     29 [qwen-vl-text] LLM output (len=1942):
{
  "encounter_date": "2025-04-25",
  "admission_date": "2025-04-23",
  "discharge_date": "2025-04-25",
  "hospital_days": 2,
  "department": "十二病区",
  "bed_number": "6",
  "admission_condition": "患者因“声音嘶哑10余天”入院。查体：会厌无肿胀，杓会厌襞稍充血肿胀，室带无新生物，右侧声带边缘息肉样隆起，表面光滑，声门闭合不全。辅助检查：电子喉镜（2025-04-20本院）示：舌扁桃体增生，会厌无充血，声带稍肿胀，活动可，右侧声带边缘息肉样肿物，声门闭合欠佳，杓间区稍红肿。",
  "admission_diagnoses": [
    {
      "name": "声带息肉（右）",
      "diagnosis_type": "西医"
    },
    {
      "name": "喉咽反流",
      "diagnosis_type": "西医"
    },
    {
      "name": "急性咽喉炎",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后完善血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十二通道）（20250423094755）：窦性心动过缓CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。手术指征明确，无明显手术禁忌，昨日全麻下行喉镜下声带病损切除术，手术顺利，术后予抗炎消肿、雾化等对症治疗，恢复可，要求今日出院。",
  "auxiliary_exams": "血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十二通道）（20250423094755）：窦性心动过缓",
  "imaging_findings": "CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。",
  "discharge_diagnoses": [
    {
      "name": "声带息肉（右）",
      "diagnosis_type": "西医"
    },
    {
      "name": "喉咽反流",
      "diagnosis_type": "西医"
    },
    {
      "name": "急性咽喉炎",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者一般情况可，声音嘶哑，稍咽痛，无吞咽疼痛，无咽部出血，无发热，饮食睡眠可，大小便正常。查体：神志清，精神可，心肺无明显异常。咽喉部粘膜充血，会厌无充血肿胀，杓会厌襞粘膜无肿胀，双侧声带稍水肿，声门闭合良好。",
  "outcome": "治愈",
  "discharge_orders": "1.注意声休2周，禁食辛辣刺激，2.口服黄氏响声丸/西瓜霜含片，3.2-3周后复查喉镜；4.门诊随诊",
  "do_medications": [
    "黄氏响声丸",
    "西瓜霜含片"
  ],
  "do_follow_up": "2-3周后复查喉镜；门诊随诊",
  "do_precautions": [
    "注意声休2周",
    "禁食辛辣刺激"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 13:06:55,942 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-25]
2026-08-10 13:06:55,947 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2584115, prompt_len=1736
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["徐州矿务集团总医院", "徐州医科大学第二附属医院", "间病房入、出院记录", "：十二病区护理单元 床号：6 住院号：00214234", "工作单位：-", "性别：女", "年龄：49岁", "籍贯：江苏省徐州市泉山区", "民族：汉族", "婚姻：已婚", "职业：职工", "住址：江苏徐州市", "供史者与（患者关系）：本人", "入院日期：2025-04-23 09:05:08", "记录日期：2025年04月25日08时29分", "主诉：声音嘶哑10余天", "入院情况：患者因“声音嘶哑10余天”入院。查体：会厌无肿胀，杓会厌襞稍充血肿胀，室带无新生物，右侧声", "带边缘息肉样隆起，表面光滑，声门闭合不全。辅助检查：电子喉镜（2025-04-20本院）示：舌扁桃体增生，会", "厌无充血，声带稍肿胀，活动可，右侧声带边缘息肉样肿物，声门闭合欠佳，杓间区稍红肿。", "入院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。", "手术名称：1.内镜下声带病损切除术（内镜下声带病损切除术）", "年04月24日", "手术日期：2025", "诊疗经过：入院后完善血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十", "二通道）（20250423094755）：窦性心动过缓CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：", "左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶", "钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。手术指征明确，无明显手术禁忌，", "昨日全麻下行喉镜下声带病损切除术，手术顺利，术后予抗炎消肿、雾化等对症治疗，恢复可，要求今日出院。", "出院情况：（）治愈 口好转 口未愈 口未治 口转院 口自动出院）伤口愈合：-", "患者一般情况可，声音嘶哑，稍咽痛，无吞咽疼痛，无咽部出血，无发热，饮食睡眠可，大小便正常。查体：神", "志清，精神可，心肺无明显异常。咽喉部粘膜充血，会厌无充血肿胀，杓会厌襞粘膜无肿胀，双侧声带稍水肿，", "声门闭合良好。", "出院诊断：出院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。", "出院日期：2025-04-25", "出院医嘱：1.注意声休2周，禁食辛辣刺激，2.口服黄氏响声丸/西瓜霜含片，3.2-3周后复查喉镜；4.门诊随诊", "X光片号：", "CT号：", "MRI号：", "病理号：", "医师签名：", "门诊病历已交病人或家属，签收人：", "主治医师签名：", "第1页"]

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
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord API raw response (len=2879):
[
	{"text": "徐州矿务集团总医院", "bbox": [310, 95, 483, 116]},
	{"text": "徐州医科大学第二附属医院", "bbox": [288, 108, 508, 133]},
	{"text": "间病房入、出院记录", "bbox": [295, 120, 534, 150]},
	{"text": "：十二病区护理单元 床号：6 住院号：00214234", "bbox": [295, 138, 594, 166]},
	{"text": "工作单位：-", "bbox": [390, 158, 458, 172]},
	{"text": "性别：女", "bbox": [94, 195, 154, 207]},
	{"text": "年龄：49岁", "bbox": [94, 212, 154, 225]},
	{"text": "籍贯：江苏省徐州市泉山区", "bbox": [94, 224, 248, 244]},
	{"text": "民族：汉族", "bbox": [94, 249, 156, 263]},
	{"text": "婚姻：已婚", "bbox": [95, 268, 158, 282]},
	{"text": "职业：职工", "bbox": [391, 175, 454, 189]},
	{"text": "住址：江苏徐州市", "bbox": [394, 190, 494, 207]},
	{"text": "供史者与（患者关系）：本人", "bbox": [396, 206, 548, 225]},
	{"text": "入院日期：2025-04-23 09:05:08", "bbox": [398, 222, 580, 245]},
	{"text": "记录日期：2025年04月25日08时29分", "bbox": [401, 240, 609, 264]},
	{"text": "主诉：声音嘶哑10余天", "bbox": [94, 282, 223, 301]},
	{"text": "入院情况：患者因“声音嘶哑10余天”入院。查体：会厌无肿胀，杓会厌襞稍充血肿胀，室带无新生物，右侧声", "bbox": [96, 265, 748, 316]},
	{"text": "带边缘息肉样隆起，表面光滑，声门闭合不全。辅助检查：电子喉镜（2025-04-20本院）示：舌扁桃体增生，会", "bbox": [97, 280, 750, 332]},
	{"text": "厌无充血，声带稍肿胀，活动可，右侧声带边缘息肉样肿物，声门闭合欠佳，杓间区稍红肿。", "bbox": [98, 300, 641, 349]},
	{"text": "入院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。", "bbox": [100, 327, 511, 365]},
	{"text": "手术名称：1.内镜下声带病损切除术（内镜下声带病损切除术）", "bbox": [103, 347, 474, 380]},
	{"text": "年04月24日", "bbox": [106, 380, 176, 395]},
	{"text": "手术日期：2025", "bbox": [669, 328, 754, 344]},
	{"text": "诊疗经过：入院后完善血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十", "bbox": [108, 358, 755, 411]},
	{"text": "二通道）（20250423094755）：窦性心动过缓CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：", "bbox": [109, 374, 739, 427]},
	{"text": "左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶", "bbox": [110, 388, 761, 442]},
	{"text": "钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。手术指征明确，无明显手术禁忌，", "bbox": [111, 402, 756, 457]},
	{"text": "昨日全麻下行喉镜下声带病损切除术，手术顺利，术后予抗炎消肿、雾化等对症治疗，恢复可，要求今日出院。", "bbox": [112, 417, 757, 472]},
	{"text": "出院情况：（）治愈 口好转 口未愈 口未治 口转院 口自动出院）伤口愈合：-", "bbox": [114, 448, 574, 488]},
	{"text": "患者一般情况可，声音嘶哑，稍咽痛，无吞咽疼痛，无咽部出血，无发热，饮食睡眠可，大小便正常。查体：神", "bbox": [115, 448, 772, 502]},
	{"text": "志清，精神可，心肺无明显异常。咽喉部粘膜充血，会厌无充血肿胀，杓会厌襞粘膜无肿胀，双侧声带稍水肿，", "bbox": [115, 462, 770, 516]},
	{"text": "声门闭合良好。", "bbox": [115, 516, 207, 532]},
	{"text": "出院诊断：出院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。", "bbox": [115, 508, 538, 548]},
	{"text": "出院日期：2025-04-25", "bbox": [115, 544, 252, 563]},
	{"text": "出院医嘱：1.注意声休2周，禁食辛辣刺激，2.口服黄氏响声丸/西瓜霜含片，3.2-3周后复查喉镜；4.门诊随诊", "bbox": [115, 521, 764, 578]},
	{"text": "X光片号：", "bbox": [560, 550, 616, 565]},
	{"text": "CT号：", "bbox": [584, 569, 618, 582]},
	{"text": "MRI号：", "bbox": [581, 588, 622, 602]},
	{"text": "病理号：", "bbox": [578, 608, 626, 622]},
	{"text": "医师签名：", "bbox": [624, 627, 688, 644]},
	{"text": "门诊病历已交病人或家属，签收人：", "bbox": [118, 673, 354, 703]},
	{"text": "主治医师签名：", "bbox": [716, 651, 799, 669]},
	{"text": "第1页", "bbox": [463, 748, 513, 764]}
]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=15.7s
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[0]: text=徐州矿务集团总医院, bbox=[310, 95, 483, 116]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[1]: text=徐州医科大学第二附属医院, bbox=[288, 108, 508, 133]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[2]: text=间病房入、出院记录, bbox=[295, 120, 534, 150]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[3]: text=：十二病区护理单元 床号：6 住院号：00214234, bbox=[295, 138, 594, 166]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[4]: text=工作单位：-, bbox=[390, 158, 458, 172]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女, bbox=[94, 195, 154, 207]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：49岁, bbox=[94, 212, 154, 225]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[7]: text=籍贯：江苏省徐州市泉山区, bbox=[94, 224, 248, 244]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[8]: text=民族：汉族, bbox=[94, 249, 156, 263]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[9]: text=婚姻：已婚, bbox=[95, 268, 158, 282]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[10]: text=职业：职工, bbox=[391, 175, 454, 189]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[11]: text=住址：江苏徐州市, bbox=[394, 190, 494, 207]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[12]: text=供史者与（患者关系）：本人, bbox=[396, 206, 548, 225]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[13]: text=入院日期：2025-04-23 09:05:08, bbox=[398, 222, 580, 245]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[14]: text=记录日期：2025年04月25日08时29分, bbox=[401, 240, 609, 264]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：声音嘶哑10余天, bbox=[94, 282, 223, 301]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[16]: text=入院情况：患者因“声音嘶哑10余天”入院。查体：会厌无肿胀，杓会厌襞稍充血肿胀，室带无新生物，右侧声, bbox=[96, 265, 748, 316]
2026-08-10 13:07:11,681 INFO     29 [qwen-vl-text] coord item[17]: text=带边缘息肉样隆起，表面光滑，声门闭合不全。辅助检查：电子喉镜（2025-04-20本院）示：舌扁桃体增生，会, bbox=[97, 280, 750, 332]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[18]: text=厌无充血，声带稍肿胀，活动可，右侧声带边缘息肉样肿物，声门闭合欠佳，杓间区稍红肿。, bbox=[98, 300, 641, 349]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[19]: text=入院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。, bbox=[100, 327, 511, 365]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[20]: text=手术名称：1.内镜下声带病损切除术（内镜下声带病损切除术）, bbox=[103, 347, 474, 380]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[21]: text=年04月24日, bbox=[106, 380, 176, 395]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[22]: text=手术日期：2025, bbox=[669, 328, 754, 344]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[23]: text=诊疗经过：入院后完善血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十, bbox=[108, 358, 755, 411]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[24]: text=二通道）（20250423094755）：窦性心动过缓CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：, bbox=[109, 374, 739, 427]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[25]: text=左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶, bbox=[110, 388, 761, 442]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[26]: text=钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。手术指征明确，无明显手术禁忌，, bbox=[111, 402, 756, 457]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[27]: text=昨日全麻下行喉镜下声带病损切除术，手术顺利，术后予抗炎消肿、雾化等对症治疗，恢复可，要求今日出院。, bbox=[112, 417, 757, 472]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[28]: text=出院情况：（）治愈 口好转 口未愈 口未治 口转院 口自动出院）伤口愈合：-, bbox=[114, 448, 574, 488]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[29]: text=患者一般情况可，声音嘶哑，稍咽痛，无吞咽疼痛，无咽部出血，无发热，饮食睡眠可，大小便正常。查体：神, bbox=[115, 448, 772, 502]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[30]: text=志清，精神可，心肺无明显异常。咽喉部粘膜充血，会厌无充血肿胀，杓会厌襞粘膜无肿胀，双侧声带稍水肿，, bbox=[115, 462, 770, 516]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[31]: text=声门闭合良好。, bbox=[115, 516, 207, 532]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[32]: text=出院诊断：出院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。, bbox=[115, 508, 538, 548]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[33]: text=出院日期：2025-04-25, bbox=[115, 544, 252, 563]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[34]: text=出院医嘱：1.注意声休2周，禁食辛辣刺激，2.口服黄氏响声丸/西瓜霜含片，3.2-3周后复查喉镜；4.门诊随诊, bbox=[115, 521, 764, 578]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[35]: text=X光片号：, bbox=[560, 550, 616, 565]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[36]: text=CT号：, bbox=[584, 569, 618, 582]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[37]: text=MRI号：, bbox=[581, 588, 622, 602]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[38]: text=病理号：, bbox=[578, 608, 626, 622]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[39]: text=医师签名：, bbox=[624, 627, 688, 644]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[40]: text=门诊病历已交病人或家属，签收人：, bbox=[118, 673, 354, 703]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[41]: text=主治医师签名：, bbox=[716, 651, 799, 669]
2026-08-10 13:07:11,682 INFO     29 [qwen-vl-text] coord item[42]: text=第1页, bbox=[463, 748, 513, 764]
2026-08-10 13:07:11,683 INFO     29 [qwen-vl-text] page=0 — 43/43 coords, api_time=15.7s
2026-08-10 13:07:11,683 INFO     29 [qwen-vl-text] new_positions (43):
[[0, 184.45, 287.385, 79.99, 97.672], [0, 171.35999999999999, 302.26, 90.93599999999999, 111.98599999999999], [0, 175.525, 317.72999999999996, 101.03999999999999, 126.3], [0, 175.525, 353.43, 116.196, 139.772], [0, 232.04999999999998, 272.51, 133.036, 144.82399999999998], [0, 55.93, 91.63, 164.19, 174.29399999999998], [0, 55.93, 91.63, 178.504, 189.45], [0, 55.93, 147.56, 188.608, 205.44799999999998], [0, 55.93, 92.82, 209.658, 221.446], [0, 56.525, 94.00999999999999, 225.656, 237.444], [0, 232.64499999999998, 270.13, 147.35, 159.138], [0, 234.42999999999998, 293.93, 159.98, 174.29399999999998], [0, 235.61999999999998, 326.06, 173.452, 189.45], [0, 236.81, 345.09999999999997, 186.924, 206.29], [0, 238.595, 362.35499999999996, 202.07999999999998, 222.28799999999998], [0, 55.93, 132.685, 237.444, 253.44199999999998], [0, 57.12, 445.06, 223.13, 266.072], [0, 57.714999999999996, 446.25, 235.76, 279.544], [0, 58.309999999999995, 381.395, 252.6, 293.858], [0, 59.5, 304.04499999999996, 275.334, 307.33], [0, 61.285, 282.03, 292.174, 319.96], [0, 63.07, 104.72, 319.96, 332.59], [0, 398.055, 448.63, 276.176, 289.64799999999997], [0, 64.25999999999999, 449.22499999999997, 301.436, 346.062], [0, 64.855, 439.705, 314.908, 359.534], [0, 65.45, 452.79499999999996, 326.69599999999997, 372.164], [0, 66.045, 449.82, 338.484, 384.794], [0, 66.64, 450.41499999999996, 351.114, 397.424], [0, 67.83, 341.53, 377.216, 410.89599999999996], [0, 68.425, 459.34, 377.216, 422.68399999999997], [0, 68.425, 458.15, 389.00399999999996, 434.472], [0, 68.425, 123.16499999999999, 434.472, 447.94399999999996], [0, 68.425, 320.11, 427.736, 461.416], [0, 68.425, 149.94, 458.048, 474.046], [0, 68.425, 454.58, 438.68199999999996, 486.676], [0, 333.2, 366.52, 463.09999999999997, 475.72999999999996], [0, 347.47999999999996, 367.71, 479.09799999999996, 490.044], [0, 345.695, 370.09, 495.096, 506.88399999999996], [0, 343.90999999999997, 372.46999999999997, 511.936, 523.7239999999999], [0, 371.28, 409.35999999999996, 527.934, 542.2479999999999], [0, 70.21, 210.63, 566.6659999999999, 591.9259999999999], [0, 426.02, 475.405, 548.1419999999999, 563.298], [0, 275.485, 305.235, 629.816, 643.288]]
2026-08-10 13:07:11,683 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=24.3s
2026-08-10 13:07:11,689 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:07:11,689 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:07:11,689 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:07:11,694 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:07:11,694 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:07:12,467 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:07:12.465+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 39, "failed": 0, "current": {"465f3f9094bc11f1bd9827cf206dfa2d": {"id": "465f3f9094bc11f1bd9827cf206dfa2d", "doc_id": "4630c9da94bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "type": "pdf", "location": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "size": 241486, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367178063, "task_type": "dataflow", "root_trace_id": "c90b5c4d512840ec92722025b8967e21", "root_traceparent": "00-c90b5c4d512840ec92722025b8967e21-6b6dbfd12195e555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:07:12,663 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:07:12,667 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:07:12,668 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:07:12,668 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:07:12,672 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:07:12,672 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:07:12,673 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:07:12,673 INFO     29 [qwen-vl-text] positions(219): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:07:12,673 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [219]
2026-08-10 13:07:12,839 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:07:12,840 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1252
2026-08-10 13:07:12,840 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:07:12,840 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 43, \"bbox_end\": 261, \"encounter_dates\": [\"2024-11-29\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "徐州医科大学附属医院\n肺功能检查报告\n舒张试验\n姓名：\n科别：\n性别：\n身高：158 cm\n号：210254\n/住院号：门诊\n48 岁\n体重：49.6 kg\nFlow [L/s]\nF/V ex\nVolume [L]\nCO [%]\n0.30\n0.25\n0.20\n0.15\n0.10\n0.05\n0.00\n0\n10\n5\n0\n5\n10\n1\n2\n3\n4\n5\n6\n7\nF/V in\nTime [s]\n0\n10\n20\n30\n40\n50\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n日期\n24-11-29\n24-11-29\n时间\n10:51:30\n11:27:38\nVT\n[L]\n0.35\n0.42\n118.7\nBF\n[1/min]\n20.00\n19.20\n96.0\nMV\n[L/min]\n7.09\n8.07\n113.9\nVC MAX\n[L]\n2.93\n2.48\n84.6\n2.78\n94.9\n12.2\nERV\n[L]\n0.96\n1.10\n115.1\nIC\n[L]\n1.97\n1.37\n69.7\nFVC\n[L]\n2.86\n2.48\n86.6\n2.73\n95.3\n10.0\nFEV 1\n[L]\n2.44\n1.64\n67.3\n1.86\n76.4\n13.5\nFEV 1 % FVC\n[%]\n82.57\n66.28\n80.3\n68.41\n82.9\n3.2\nFEV 1 % VC MAX\n[%]\n79.98\n66.28\n82.9\n67.06\n83.8\n1.2\nPEF\n[L/s]\n6.14\n4.14\n67.4\n4.24\n69.1\n2.5\nMEF 75\n[L/s]\n5.49\n2.43\n44.2\n3.22\n58.7\n32.8\nMEF 50\n[L/s]\n3.63\n1.22\n31.8\n1.38\n36.1\n13.6\nMEF 25\n[L/s]\n1.57\n0.38\n24.2\n0.41\n25.9\n7.4\nMMEF 75/25\n[L/s]\n3.26\n0.94\n28.7\n1.06\n32.4\n13.1\nV backextrapolation ex [L]\n0.07\n0.07\n0.2\nV backextrapol. % FVC [%]\n2.64\n2.40\n-9.0\nMVV\n[L/min]\n95.44\n64.07\n67.1\n55.95\n58.6\n13.5\nFEV 1*30\n[L/min]\n95.44\n49.27\n51.6\nTLC-SB\n[L]\n4.64\n4.76\n102.7\nFRC-SB\n[L]\n2.59\n3.27\n126.5\nRV-SB\n[L]\n1.63\n2.30\n141.5\nRV%TLC-SB\n[%]\n35.28\n48.35\n137.1\nDLCO SB\n[mmol/min/kPa]\n7.83\n5.92\n75.5\nDLCO/VA\n[mmol/min/kPa/L]\n1.69\n1.27\n75.3\n结论：\n中度阻塞性通气功能障碍\n残总比增高\n弥散功能轻度障碍\n可逆试验阳性（13.5%），绝对值增加220ml。\n医生：\n检查者：\n审核者：",
    "role": "user"
  }
]
2026-08-10 13:07:23,248 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:07:23,249 INFO     29 [qwen-vl-text] LLM output (len=1670):
{
  "exam_date": "2024-11-29",
  "report_date": "2024-11-29",
  "exam_name": "肺功能检查报告",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "Flow [L/s]\nF/V ex\nVolume [L]\nCO [%]\n0.30\n0.25\n0.20\n0.15\n0.10\n0.05\n0.00\n0\n10\n5\n0\n5\n10\n1\n2\n3\n4\n5\n6\n7\nF/V in\nTime [s]\n0\n10\n20\n30\n40\n50\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n日期\n24-11-29\n24-11-29\n时间\n10:51:30\n11:27:38\nVT\n[L]\n0.35\n0.42\n118.7\nBF\n[1/min]\n20.00\n19.20\n96.0\nMV\n[L/min]\n7.09\n8.07\n113.9\nVC MAX\n[L]\n2.93\n2.48\n84.6\n2.78\n94.9\n12.2\nERV\n[L]\n0.96\n1.10\n115.1\nIC\n[L]\n1.97\n1.37\n69.7\nFVC\n[L]\n2.86\n2.48\n86.6\n2.73\n95.3\n10.0\nFEV 1\n[L]\n2.44\n1.64\n67.3\n1.86\n76.4\n13.5\nFEV 1 % FVC\n[%]\n82.57\n66.28\n80.3\n68.41\n82.9\n3.2\nFEV 1 % VC MAX\n[%]\n79.98\n66.28\n82.9\n67.06\n83.8\n1.2\nPEF\n[L/s]\n6.14\n4.14\n67.4\n4.24\n69.1\n2.5\nMEF 75\n[L/s]\n5.49\n2.43\n44.2\n3.22\n58.7\n32.8\nMEF 50\n[L/s]\n3.63\n1.22\n31.8\n1.38\n36.1\n13.6\nMEF 25\n[L/s]\n1.57\n0.38\n24.2\n0.41\n25.9\n7.4\nMMEF 75/25\n[L/s]\n3.26\n0.94\n28.7\n1.06\n32.4\n13.1\nV backextrapolation ex [L]\n0.07\n0.07\n0.2\nV backextrapol. % FVC [%]\n2.64\n2.40\n-9.0\nMVV\n[L/min]\n95.44\n64.07\n67.1\n55.95\n58.6\n13.5\nFEV 1*30\n[L/min]\n95.44\n49.27\n51.6\nTLC-SB\n[L]\n4.64\n4.76\n102.7\nFRC-SB\n[L]\n2.59\n3.27\n126.5\nRV-SB\n[L]\n1.63\n2.30\n141.5\nRV%TLC-SB\n[%]\n35.28\n48.35\n137.1\nDLCO SB\n[mmol/min/kPa]\n7.83\n5.92\n75.5\nDLCO/VA\n[mmol/min/kPa/L]\n1.69\n1.27\n75.3",
  "conclusion": "结论：\n中度阻塞性通气功能障碍\n残总比增高\n弥散功能轻度障碍\n可逆试验阳性（13.5%），绝对值增加220ml。",
  "physician": null,
  "reviewer": null
}
2026-08-10 13:07:23,252 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1645380, prompt_len=2523
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共219行）
["徐州医科大学附属医院", "肺功能检查报告", "舒张试验", "姓名：", "科别：", "性别：", "身高：158 cm", "号：210254", "/住院号：门诊", "48 岁", "体重：49.6 kg", "Flow [L/s]", "F/V ex", "Volume [L]", "CO [%]", "0.30", "0.25", "0.20", "0.15", "0.10", "0.05", "0.00", "0", "10", "5", "0", "5", "10", "1", "2", "3", "4", "5", "6", "7", "F/V in", "Time [s]", "0", "10", "20", "30", "40", "50", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "日期", "24-11-29", "24-11-29", "时间", "10:51:30", "11:27:38", "VT", "[L]", "0.35", "0.42", "118.7", "BF", "[1/min]", "20.00", "19.20", "96.0", "MV", "[L/min]", "7.09", "8.07", "113.9", "VC MAX", "[L]", "2.93", "2.48", "84.6", "2.78", "94.9", "12.2", "ERV", "[L]", "0.96", "1.10", "115.1", "IC", "[L]", "1.97", "1.37", "69.7", "FVC", "[L]", "2.86", "2.48", "86.6", "2.73", "95.3", "10.0", "FEV 1", "[L]", "2.44", "1.64", "67.3", "1.86", "76.4", "13.5", "FEV 1 % FVC", "[%]", "82.57", "66.28", "80.3", "68.41", "82.9", "3.2", "FEV 1 % VC MAX", "[%]", "79.98", "66.28", "82.9", "67.06", "83.8", "1.2", "PEF", "[L/s]", "6.14", "4.14", "67.4", "4.24", "69.1", "2.5", "MEF 75", "[L/s]", "5.49", "2.43", "44.2", "3.22", "58.7", "32.8", "MEF 50", "[L/s]", "3.63", "1.22", "31.8", "1.38", "36.1", "13.6", "MEF 25", "[L/s]", "1.57", "0.38", "24.2", "0.41", "25.9", "7.4", "MMEF 75/25", "[L/s]", "3.26", "0.94", "28.7", "1.06", "32.4", "13.1", "V backextrapolation ex [L]", "0.07", "0.07", "0.2", "V backextrapol. % FVC [%]", "2.64", "2.40", "-9.0", "MVV", "[L/min]", "95.44", "64.07", "67.1", "55.95", "58.6", "13.5", "FEV 1*30", "[L/min]", "95.44", "49.27", "51.6", "TLC-SB", "[L]", "4.64", "4.76", "102.7", "FRC-SB", "[L]", "2.59", "3.27", "126.5", "RV-SB", "[L]", "1.63", "2.30", "141.5", "RV%TLC-SB", "[%]", "35.28", "48.35", "137.1", "DLCO SB", "[mmol/min/kPa]", "7.83", "5.92", "75.5", "DLCO/VA", "[mmol/min/kPa/L]", "1.69", "1.27", "75.3", "结论：", "中度阻塞性通气功能障碍", "残总比增高", "弥散功能轻度障碍", "可逆试验阳性（13.5%），绝对值增加220ml。", "医生：", "检查者：", "审核者："]

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
2026-08-10 13:08:14,546 INFO     29 [qwen-vl-text] coord API raw response (len=10277):
[
	{"text": "徐州医科大学附属医院", "bbox": [320, 194, 553, 212]},
	{"text": "肺功能检查报告", "bbox": [355, 212, 518, 230]},
	{"text": "舒张试验", "bbox": [400, 232, 476, 247]},
	{"text": "姓名：", "bbox": [152, 252, 191, 264]},
	{"text": "科别：", "bbox": [152, 263, 191, 274]},
	{"text": "性别：", "bbox": [152, 274, 191, 285]},
	{"text": "身高：158 cm", "bbox": [152, 285, 344, 296]},
	{"text": "号：", "bbox": [468, 252, 496, 264]},
	{"text": "210254", "bbox": [581, 254, 628, 264]},
	{"text": "/住院号：", "bbox": [470, 264, 535, 275]},
	{"text": "门诊", "bbox": [581, 264, 614, 275]},
	{"text": "48 岁", "bbox": [581, 275, 619, 285]},
	{"text": "体重：49.6 kg", "bbox": [445, 285, 637, 296]},
	{"text": "Flow [L/s]", "bbox": [193, 302, 237, 311]},
	{"text": "F/V ex", "bbox": [337, 302, 365, 311]},
	{"text": "Volume [L]", "bbox": [474, 302, 520, 311]},
	{"text": "CO [%]", "bbox": [638, 300, 672, 309]},
	{"text": "0.30", "bbox": [680, 296, 699, 304]},
	{"text": "0.25", "bbox": [680, 314, 699, 321]},
	{"text": "0.20", "bbox": [680, 333, 699, 340]},
	{"text": "0.15", "bbox": [474, 352, 495, 359]},
	{"text": "0.10", "bbox": [474, 370, 495, 377]},
	{"text": "0.05", "bbox": [474, 388, 495, 395]},
	{"text": "0.00", "bbox": [680, 403, 699, 410]},
	{"text": "0", "bbox": [468, 413, 477, 420]},
	{"text": "10", "bbox": [508, 413, 520, 420]},
	{"text": "20", "bbox": [547, 413, 560, 420]},
	{"text": "30", "bbox": [588, 413, 600, 420]},
	{"text": "40", "bbox": [628, 413, 641, 420]},
	{"text": "50", "bbox": [670, 413, 682, 420]},
	{"text": "预计值", "bbox": [383, 421, 435, 433]},
	{"text": "前次", "bbox": [474, 421, 508, 433]},
	{"text": "前/预", "bbox": [530, 421, 571, 433]},
	{"text": "后次", "bbox": [611, 421, 646, 433]},
	{"text": "后/预", "bbox": [669, 421, 710, 433]},
	{"text": "改善率", "bbox": [725, 420, 775, 432]},
	{"text": "日期", "bbox": [152, 435, 187, 447]},
	{"text": "24-11-29", "bbox": [442, 435, 508, 445]},
	{"text": "24-11-29", "bbox": [579, 435, 646, 445]},
	{"text": "时间", "bbox": [152, 447, 187, 459]},
	{"text": "10:51:30", "bbox": [442, 446, 508, 456]},
	{"text": "11:27:38", "bbox": [579, 446, 646, 456]},
	{"text": "VT", "bbox": [152, 470, 170, 479]},
	{"text": "[L]", "bbox": [346, 469, 367, 479]},
	{"text": "0.35", "bbox": [401, 469, 435, 479]},
	{"text": "0.42", "bbox": [474, 469, 508, 479]},
	{"text": "118.7", "bbox": [532, 469, 571, 479]},
	{"text": "BF", "bbox": [152, 481, 170, 490]},
	{"text": "[1/min]", "bbox": [313, 480, 367, 490]},
	{"text": "20.00", "bbox": [393, 480, 435, 490]},
	{"text": "19.20", "bbox": [468, 480, 508, 490]},
	{"text": "96.0", "bbox": [540, 480, 571, 490]},
	{"text": "MV", "bbox": [152, 492, 170, 501]},
	{"text": "[L/min]", "bbox": [313, 491, 367, 501]},
	{"text": "7.09", "bbox": [401, 491, 435, 501]},
	{"text": "8.07", "bbox": [474, 491, 508, 501]},
	{"text": "113.9", "bbox": [532, 491, 571, 501]},
	{"text": "VC MAX", "bbox": [152, 514, 204, 523]},
	{"text": "[L]", "bbox": [346, 513, 367, 523]},
	{"text": "2.93", "bbox": [401, 513, 435, 523]},
	{"text": "2.48", "bbox": [474, 513, 508, 523]},
	{"text": "84.6", "bbox": [540, 513, 571, 523]},
	{"text": "2.78", "bbox": [613, 513, 646, 523]},
	{"text": "94.9", "bbox": [679, 513, 710, 523]},
	{"text": "12.2", "bbox": [745, 513, 775, 523]},
	{"text": "ERV", "bbox": [152, 526, 180, 535]},
	{"text": "[L]", "bbox": [346, 525, 367, 535]},
	{"text": "0.96", "bbox": [401, 525, 435, 535]},
	{"text": "1.10", "bbox": [474, 525, 508, 535]},
	{"text": "115.1", "bbox": [532, 525, 571, 535]},
	{"text": "IC", "bbox": [152, 537, 170, 546]},
	{"text": "[L]", "bbox": [346, 536, 367, 546]},
	{"text": "1.97", "bbox": [401, 536, 435, 546]},
	{"text": "1.37", "bbox": [474, 536, 508, 546]},
	{"text": "69.7", "bbox": [540, 536, 571, 546]},
	{"text": "FVC", "bbox": [152, 560, 180, 569]},
	{"text": "[L]", "bbox": [346, 559, 367, 569]},
	{"text": "2.86", "bbox": [401, 559, 435, 569]},
	{"text": "2.48", "bbox": [474, 559, 508, 569]},
	{"text": "86.6", "bbox": [540, 559, 571, 569]},
	{"text": "2.73", "bbox": [613, 559, 646, 569]},
	{"text": "95.3", "bbox": [679, 559, 710, 569]},
	{"text": "10.0", "bbox": [745, 559, 775, 569]},
	{"text": "FEV 1", "bbox": [152, 571, 195, 580]},
	{"text": "[L]", "bbox": [346, 570, 367, 580]},
	{"text": "2.44", "bbox": [401, 570, 435, 580]},
	{"text": "1.64", "bbox": [474, 570, 508, 580]},
	{"text": "67.3", "bbox": [540, 570, 571, 580]},
	{"text": "1.86", "bbox": [613, 570, 646, 580]},
	{"text": "76.4", "bbox": [679, 570, 710, 580]},
	{"text": "13.5", "bbox": [745, 570, 775, 580]},
	{"text": "FEV 1 % FVC", "bbox": [152, 583, 247, 592]},
	{"text": "[%]", "bbox": [346, 582, 367, 592]},
	{"text": "82.57", "bbox": [393, 582, 435, 592]},
	{"text": "66.28", "bbox": [468, 582, 508, 592]},
	{"text": "80.3", "bbox": [540, 582, 571, 592]},
	{"text": "68.41", "bbox": [606, 582, 646, 592]},
	{"text": "82.9", "bbox": [679, 582, 710, 592]},
	{"text": "3.2", "bbox": [753, 582, 775, 592]},
	{"text": "FEV 1 % VC MAX", "bbox": [152, 594, 272, 603]},
	{"text": "[%]", "bbox": [346, 593, 367, 603]},
	{"text": "79.98", "bbox": [393, 593, 435, 603]},
	{"text": "66.28", "bbox": [468, 593, 508, 603]},
	{"text": "82.9", "bbox": [540, 593, 571, 603]},
	{"text": "67.06", "bbox": [606, 593, 646, 603]},
	{"text": "83.8", "bbox": [679, 593, 710, 603]},
	{"text": "1.2", "bbox": [753, 593, 775, 603]},
	{"text": "PEF", "bbox": [152, 606, 180, 615]},
	{"text": "[L/s]", "bbox": [331, 605, 367, 615]},
	{"text": "6.14", "bbox": [401, 605, 435, 615]},
	{"text": "4.14", "bbox": [474, 605, 508, 615]},
	{"text": "67.4", "bbox": [540, 605, 571, 615]},
	{"text": "4.24", "bbox": [613, 605, 646, 615]},
	{"text": "69.1", "bbox": [679, 605, 710, 615]},
	{"text": "2.5", "bbox": [753, 605, 775, 615]},
	{"text": "MEF 75", "bbox": [152, 617, 205, 627]},
	{"text": "[L/s]", "bbox": [331, 617, 367, 627]},
	{"text": "5.49", "bbox": [401, 617, 435, 627]},
	{"text": "2.43", "bbox": [474, 617, 508, 627]},
	{"text": "44.2", "bbox": [540, 617, 571, 627]},
	{"text": "3.22", "bbox": [613, 617, 646, 627]},
	{"text": "58.7", "bbox": [679, 617, 710, 627]},
	{"text": "32.8", "bbox": [745, 617, 775, 627]},
	{"text": "MEF 50", "bbox": [152, 629, 205, 638]},
	{"text": "[L/s]", "bbox": [331, 628, 367, 638]},
	{"text": "3.63", "bbox": [401, 628, 435, 638]},
	{"text": "1.22", "bbox": [474, 628, 508, 638]},
	{"text": "31.8", "bbox": [540, 628, 571, 638]},
	{"text": "1.38", "bbox": [613, 628, 646, 638]},
	{"text": "36.1", "bbox": [679, 628, 710, 638]},
	{"text": "13.6", "bbox": [745, 628, 775, 638]},
	{"text": "MEF 25", "bbox": [152, 641, 205, 650]},
	{"text": "[L/s]", "bbox": [331, 640, 367, 650]},
	{"text": "1.57", "bbox": [401, 640, 435, 650]},
	{"text": "0.38", "bbox": [474, 640, 508, 650]},
	{"text": "24.2", "bbox": [540, 640, 571, 650]},
	{"text": "0.41", "bbox": [613, 640, 646, 650]},
	{"text": "25.9", "bbox": [679, 640, 710, 650]},
	{"text": "7.4", "bbox": [753, 640, 775, 650]},
	{"text": "MMEF 75/25", "bbox": [152, 652, 239, 662]},
	{"text": "[L/s]", "bbox": [331, 652, 367, 662]},
	{"text": "3.26", "bbox": [401, 652, 435, 662]},
	{"text": "0.94", "bbox": [474, 652, 508, 662]},
	{"text": "28.7", "bbox": [540, 652, 571, 662]},
	{"text": "1.06", "bbox": [613, 652, 646, 662]},
	{"text": "32.4", "bbox": [679, 652, 710, 662]},
	{"text": "13.1", "bbox": [745, 652, 775, 662]},
	{"text": "V backextrapolation ex [L]", "bbox": [152, 664, 367, 674]},
	{"text": "0.07", "bbox": [474, 663, 508, 673]},
	{"text": "0.07", "bbox": [613, 663, 646, 673]},
	{"text": "0.2", "bbox": [753, 663, 775, 673]},
	{"text": "V backextrapol. % FVC [%]", "bbox": [152, 675, 367, 685]},
	{"text": "2.64", "bbox": [474, 675, 508, 685]},
	{"text": "2.40", "bbox": [613, 675, 646, 685]},
	{"text": "-9.0", "bbox": [745, 675, 775, 685]},
	{"text": "MVV", "bbox": [152, 698, 182, 707]},
	{"text": "[L/min]", "bbox": [315, 697, 367, 707]},
	{"text": "95.44", "bbox": [393, 697, 435, 707]},
	{"text": "64.07", "bbox": [468, 697, 508, 707]},
	{"text": "67.1", "bbox": [540, 697, 571, 707]},
	{"text": "55.95", "bbox": [609, 705, 651, 714]},
	{"text": "58.6", "bbox": [684, 705, 716, 714]},
	{"text": "13.5", "bbox": [745, 705, 775, 714]},
	{"text": "FEV 1*30", "bbox": [152, 710, 221, 719]},
	{"text": "[L/min]", "bbox": [315, 709, 367, 719]},
	{"text": "95.44", "bbox": [393, 709, 435, 719]},
	{"text": "49.27", "bbox": [468, 709, 508, 719]},
	{"text": "51.6", "bbox": [540, 709, 571, 719]},
	{"text": "TLC-SB", "bbox": [152, 732, 207, 741]},
	{"text": "[L]", "bbox": [346, 731, 367, 741]},
	{"text": "4.64", "bbox": [401, 731, 435, 741]},
	{"text": "4.76", "bbox": [474, 731, 508, 741]},
	{"text": "102.7", "bbox": [532, 731, 571, 741]},
	{"text": "FRC-SB", "bbox": [152, 744, 207, 753]},
	{"text": "[L]", "bbox": [346, 743, 367, 753]},
	{"text": "2.59", "bbox": [401, 743, 435, 753]},
	{"text": "3.27", "bbox": [474, 743, 508, 753]},
	{"text": "126.5", "bbox": [532, 743, 571, 753]},
	{"text": "RV-SB", "bbox": [152, 755, 199, 764]},
	{"text": "[L]", "bbox": [346, 755, 367, 764]},
	{"text": "1.63", "bbox": [401, 755, 435, 764]},
	{"text": "2.30", "bbox": [474, 755, 508, 764]},
	{"text": "141.5", "bbox": [532, 755, 571, 764]},
	{"text": "RV%TLC-SB", "bbox": [152, 767, 232, 776]},
	{"text": "[%]", "bbox": [346, 766, 367, 776]},
	{"text": "35.28", "bbox": [393, 766, 435, 776]},
	{"text": "48.35", "bbox": [468, 766, 508, 776]},
	{"text": "137.1", "bbox": [532, 766, 571, 776]},
	{"text": "DLCO SB", "bbox": [152, 778, 216, 787]},
	{"text": "[mmol/min/kPa]", "bbox": [258, 777, 367, 787]},
	{"text": "7.83", "bbox": [401, 777, 435, 787]},
	{"text": "5.92", "bbox": [474, 777, 508, 787]},
	{"text": "75.5", "bbox": [540, 777, 571, 787]},
	{"text": "DLCO/VA", "bbox": [152, 790, 216, 799]},
	{"text": "[mmol/min/kPa/L]", "bbox": [242, 789, 367, 799]},
	{"text": "1.69", "bbox": [401, 789, 435, 799]},
	{"text": "1.27", "bbox": [474, 789, 508, 799]},
	{"text": "75.3", "bbox": [540, 789, 571, 799]},
	{"text": "结论：", "bbox": [155, 815, 205, 830]},
	{"text": "中度阻塞性通气功能障碍", "bbox": [160, 829, 423, 845]},
	{"text": "残总比增高", "bbox": [159, 845, 279, 861]},
	{"text": "弥散功能轻度障碍", "bbox": [160, 860, 352, 877]},
	{"text": "可逆试验阳性（13.5%），绝对值增加220ml。", "bbox": [160, 876, 624, 892]},
	{"text": "医生：", "bbox": [422, 895, 482, 910]},
	{"text": "检查者：", "bbox": [561, 895, 682, 914]},
	{"text": "审核者：", "bbox": [702, 892, 760, 907]}
]
2026-08-10 13:08:14,548 INFO     29 [qwen-vl-text] coord API: raw_items=206, valid_items=206, elapsed=51.3s
2026-08-10 13:08:14,548 INFO     29 [qwen-vl-text] coord item[0]: text=徐州医科大学附属医院, bbox=[320, 194, 553, 212]
2026-08-10 13:08:14,548 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[355, 212, 518, 230]
2026-08-10 13:08:14,548 INFO     29 [qwen-vl-text] coord item[2]: text=舒张试验, bbox=[400, 232, 476, 247]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[152, 252, 191, 264]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[4]: text=科别：, bbox=[152, 263, 191, 274]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[5]: text=性别：, bbox=[152, 274, 191, 285]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[6]: text=身高：158 cm, bbox=[152, 285, 344, 296]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[7]: text=号：, bbox=[468, 252, 496, 264]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[8]: text=210254, bbox=[581, 254, 628, 264]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[9]: text=/住院号：, bbox=[470, 264, 535, 275]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[10]: text=门诊, bbox=[581, 264, 614, 275]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[11]: text=48 岁, bbox=[581, 275, 619, 285]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[12]: text=体重：49.6 kg, bbox=[445, 285, 637, 296]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[13]: text=Flow [L/s], bbox=[193, 302, 237, 311]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[14]: text=F/V ex, bbox=[337, 302, 365, 311]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[15]: text=Volume [L], bbox=[474, 302, 520, 311]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[16]: text=CO [%], bbox=[638, 300, 672, 309]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[17]: text=0.30, bbox=[680, 296, 699, 304]
2026-08-10 13:08:14,549 INFO     29 [qwen-vl-text] coord item[18]: text=0.25, bbox=[680, 314, 699, 321]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[19]: text=0.20, bbox=[680, 333, 699, 340]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[20]: text=0.15, bbox=[474, 352, 495, 359]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[21]: text=0.10, bbox=[474, 370, 495, 377]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[22]: text=0.05, bbox=[474, 388, 495, 395]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[23]: text=0.00, bbox=[680, 403, 699, 410]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[24]: text=0, bbox=[468, 413, 477, 420]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[25]: text=10, bbox=[508, 413, 520, 420]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[26]: text=20, bbox=[547, 413, 560, 420]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[27]: text=30, bbox=[588, 413, 600, 420]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[28]: text=40, bbox=[628, 413, 641, 420]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[29]: text=50, bbox=[670, 413, 682, 420]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[30]: text=预计值, bbox=[383, 421, 435, 433]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[31]: text=前次, bbox=[474, 421, 508, 433]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[32]: text=前/预, bbox=[530, 421, 571, 433]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[33]: text=后次, bbox=[611, 421, 646, 433]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[34]: text=后/预, bbox=[669, 421, 710, 433]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[35]: text=改善率, bbox=[725, 420, 775, 432]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[36]: text=日期, bbox=[152, 435, 187, 447]
2026-08-10 13:08:14,550 INFO     29 [qwen-vl-text] coord item[37]: text=24-11-29, bbox=[442, 435, 508, 445]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[38]: text=24-11-29, bbox=[579, 435, 646, 445]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[39]: text=时间, bbox=[152, 447, 187, 459]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[40]: text=10:51:30, bbox=[442, 446, 508, 456]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[41]: text=11:27:38, bbox=[579, 446, 646, 456]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[42]: text=VT, bbox=[152, 470, 170, 479]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[43]: text=[L], bbox=[346, 469, 367, 479]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[44]: text=0.35, bbox=[401, 469, 435, 479]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[45]: text=0.42, bbox=[474, 469, 508, 479]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[46]: text=118.7, bbox=[532, 469, 571, 479]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[47]: text=BF, bbox=[152, 481, 170, 490]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[48]: text=[1/min], bbox=[313, 480, 367, 490]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[49]: text=20.00, bbox=[393, 480, 435, 490]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[50]: text=19.20, bbox=[468, 480, 508, 490]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[51]: text=96.0, bbox=[540, 480, 571, 490]
2026-08-10 13:08:14,551 INFO     29 [qwen-vl-text] coord item[52]: text=MV, bbox=[152, 492, 170, 501]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[53]: text=[L/min], bbox=[313, 491, 367, 501]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[54]: text=7.09, bbox=[401, 491, 435, 501]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[55]: text=8.07, bbox=[474, 491, 508, 501]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[56]: text=113.9, bbox=[532, 491, 571, 501]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[57]: text=VC MAX, bbox=[152, 514, 204, 523]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[58]: text=[L], bbox=[346, 513, 367, 523]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[59]: text=2.93, bbox=[401, 513, 435, 523]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[60]: text=2.48, bbox=[474, 513, 508, 523]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[61]: text=84.6, bbox=[540, 513, 571, 523]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[62]: text=2.78, bbox=[613, 513, 646, 523]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[63]: text=94.9, bbox=[679, 513, 710, 523]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[64]: text=12.2, bbox=[745, 513, 775, 523]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[65]: text=ERV, bbox=[152, 526, 180, 535]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[66]: text=[L], bbox=[346, 525, 367, 535]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[67]: text=0.96, bbox=[401, 525, 435, 535]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[68]: text=1.10, bbox=[474, 525, 508, 535]
2026-08-10 13:08:14,552 INFO     29 [qwen-vl-text] coord item[69]: text=115.1, bbox=[532, 525, 571, 535]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[70]: text=IC, bbox=[152, 537, 170, 546]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[71]: text=[L], bbox=[346, 536, 367, 546]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[72]: text=1.97, bbox=[401, 536, 435, 546]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[73]: text=1.37, bbox=[474, 536, 508, 546]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[74]: text=69.7, bbox=[540, 536, 571, 546]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[75]: text=FVC, bbox=[152, 560, 180, 569]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[76]: text=[L], bbox=[346, 559, 367, 569]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[77]: text=2.86, bbox=[401, 559, 435, 569]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[78]: text=2.48, bbox=[474, 559, 508, 569]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[79]: text=86.6, bbox=[540, 559, 571, 569]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[80]: text=2.73, bbox=[613, 559, 646, 569]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[81]: text=95.3, bbox=[679, 559, 710, 569]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[82]: text=10.0, bbox=[745, 559, 775, 569]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[83]: text=FEV 1, bbox=[152, 571, 195, 580]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[84]: text=[L], bbox=[346, 570, 367, 580]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[85]: text=2.44, bbox=[401, 570, 435, 580]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[86]: text=1.64, bbox=[474, 570, 508, 580]
2026-08-10 13:08:14,553 INFO     29 [qwen-vl-text] coord item[87]: text=67.3, bbox=[540, 570, 571, 580]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[88]: text=1.86, bbox=[613, 570, 646, 580]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[89]: text=76.4, bbox=[679, 570, 710, 580]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[90]: text=13.5, bbox=[745, 570, 775, 580]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[91]: text=FEV 1 % FVC, bbox=[152, 583, 247, 592]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[92]: text=[%], bbox=[346, 582, 367, 592]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[93]: text=82.57, bbox=[393, 582, 435, 592]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[94]: text=66.28, bbox=[468, 582, 508, 592]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[95]: text=80.3, bbox=[540, 582, 571, 592]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[96]: text=68.41, bbox=[606, 582, 646, 592]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[97]: text=82.9, bbox=[679, 582, 710, 592]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[98]: text=3.2, bbox=[753, 582, 775, 592]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[99]: text=FEV 1 % VC MAX, bbox=[152, 594, 272, 603]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[100]: text=[%], bbox=[346, 593, 367, 603]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[101]: text=79.98, bbox=[393, 593, 435, 603]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[102]: text=66.28, bbox=[468, 593, 508, 603]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[103]: text=82.9, bbox=[540, 593, 571, 603]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[104]: text=67.06, bbox=[606, 593, 646, 603]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[105]: text=83.8, bbox=[679, 593, 710, 603]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[106]: text=1.2, bbox=[753, 593, 775, 603]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[107]: text=PEF, bbox=[152, 606, 180, 615]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[108]: text=[L/s], bbox=[331, 605, 367, 615]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[109]: text=6.14, bbox=[401, 605, 435, 615]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[110]: text=4.14, bbox=[474, 605, 508, 615]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[111]: text=67.4, bbox=[540, 605, 571, 615]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[112]: text=4.24, bbox=[613, 605, 646, 615]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[113]: text=69.1, bbox=[679, 605, 710, 615]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[114]: text=2.5, bbox=[753, 605, 775, 615]
2026-08-10 13:08:14,554 INFO     29 [qwen-vl-text] coord item[115]: text=MEF 75, bbox=[152, 617, 205, 627]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[116]: text=[L/s], bbox=[331, 617, 367, 627]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[117]: text=5.49, bbox=[401, 617, 435, 627]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[118]: text=2.43, bbox=[474, 617, 508, 627]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[119]: text=44.2, bbox=[540, 617, 571, 627]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[120]: text=3.22, bbox=[613, 617, 646, 627]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[121]: text=58.7, bbox=[679, 617, 710, 627]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[122]: text=32.8, bbox=[745, 617, 775, 627]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[123]: text=MEF 50, bbox=[152, 629, 205, 638]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[124]: text=[L/s], bbox=[331, 628, 367, 638]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[125]: text=3.63, bbox=[401, 628, 435, 638]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[126]: text=1.22, bbox=[474, 628, 508, 638]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[127]: text=31.8, bbox=[540, 628, 571, 638]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[128]: text=1.38, bbox=[613, 628, 646, 638]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[129]: text=36.1, bbox=[679, 628, 710, 638]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[130]: text=13.6, bbox=[745, 628, 775, 638]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[131]: text=MEF 25, bbox=[152, 641, 205, 650]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[132]: text=[L/s], bbox=[331, 640, 367, 650]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[133]: text=1.57, bbox=[401, 640, 435, 650]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[134]: text=0.38, bbox=[474, 640, 508, 650]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[135]: text=24.2, bbox=[540, 640, 571, 650]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[136]: text=0.41, bbox=[613, 640, 646, 650]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[137]: text=25.9, bbox=[679, 640, 710, 650]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[138]: text=7.4, bbox=[753, 640, 775, 650]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[139]: text=MMEF 75/25, bbox=[152, 652, 239, 662]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[140]: text=[L/s], bbox=[331, 652, 367, 662]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[141]: text=3.26, bbox=[401, 652, 435, 662]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[142]: text=0.94, bbox=[474, 652, 508, 662]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[143]: text=28.7, bbox=[540, 652, 571, 662]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[144]: text=1.06, bbox=[613, 652, 646, 662]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[145]: text=32.4, bbox=[679, 652, 710, 662]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[146]: text=13.1, bbox=[745, 652, 775, 662]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[147]: text=V backextrapolation ex [L], bbox=[152, 664, 367, 674]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[148]: text=0.07, bbox=[474, 663, 508, 673]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[149]: text=0.07, bbox=[613, 663, 646, 673]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[150]: text=0.2, bbox=[753, 663, 775, 673]
2026-08-10 13:08:14,555 INFO     29 [qwen-vl-text] coord item[151]: text=V backextrapol. % FVC [%], bbox=[152, 675, 367, 685]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[152]: text=2.64, bbox=[474, 675, 508, 685]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[153]: text=2.40, bbox=[613, 675, 646, 685]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[154]: text=-9.0, bbox=[745, 675, 775, 685]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[155]: text=MVV, bbox=[152, 698, 182, 707]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[156]: text=[L/min], bbox=[315, 697, 367, 707]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[157]: text=95.44, bbox=[393, 697, 435, 707]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[158]: text=64.07, bbox=[468, 697, 508, 707]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[159]: text=67.1, bbox=[540, 697, 571, 707]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[160]: text=55.95, bbox=[609, 705, 651, 714]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[161]: text=58.6, bbox=[684, 705, 716, 714]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[162]: text=13.5, bbox=[745, 705, 775, 714]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[163]: text=FEV 1*30, bbox=[152, 710, 221, 719]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[164]: text=[L/min], bbox=[315, 709, 367, 719]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[165]: text=95.44, bbox=[393, 709, 435, 719]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[166]: text=49.27, bbox=[468, 709, 508, 719]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[167]: text=51.6, bbox=[540, 709, 571, 719]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[168]: text=TLC-SB, bbox=[152, 732, 207, 741]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[169]: text=[L], bbox=[346, 731, 367, 741]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[170]: text=4.64, bbox=[401, 731, 435, 741]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[171]: text=4.76, bbox=[474, 731, 508, 741]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[172]: text=102.7, bbox=[532, 731, 571, 741]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[173]: text=FRC-SB, bbox=[152, 744, 207, 753]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[174]: text=[L], bbox=[346, 743, 367, 753]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[175]: text=2.59, bbox=[401, 743, 435, 753]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[176]: text=3.27, bbox=[474, 743, 508, 753]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[177]: text=126.5, bbox=[532, 743, 571, 753]
2026-08-10 13:08:14,556 INFO     29 [qwen-vl-text] coord item[178]: text=RV-SB, bbox=[152, 755, 199, 764]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[179]: text=[L], bbox=[346, 755, 367, 764]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[180]: text=1.63, bbox=[401, 755, 435, 764]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[181]: text=2.30, bbox=[474, 755, 508, 764]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[182]: text=141.5, bbox=[532, 755, 571, 764]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[183]: text=RV%TLC-SB, bbox=[152, 767, 232, 776]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[184]: text=[%], bbox=[346, 766, 367, 776]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[185]: text=35.28, bbox=[393, 766, 435, 776]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[186]: text=48.35, bbox=[468, 766, 508, 776]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[187]: text=137.1, bbox=[532, 766, 571, 776]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[188]: text=DLCO SB, bbox=[152, 778, 216, 787]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[189]: text=[mmol/min/kPa], bbox=[258, 777, 367, 787]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[190]: text=7.83, bbox=[401, 777, 435, 787]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[191]: text=5.92, bbox=[474, 777, 508, 787]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[192]: text=75.5, bbox=[540, 777, 571, 787]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[193]: text=DLCO/VA, bbox=[152, 790, 216, 799]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[194]: text=[mmol/min/kPa/L], bbox=[242, 789, 367, 799]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[195]: text=1.69, bbox=[401, 789, 435, 799]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[196]: text=1.27, bbox=[474, 789, 508, 799]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[197]: text=75.3, bbox=[540, 789, 571, 799]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[198]: text=结论：, bbox=[155, 815, 205, 830]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[199]: text=中度阻塞性通气功能障碍, bbox=[160, 829, 423, 845]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[200]: text=残总比增高, bbox=[159, 845, 279, 861]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[201]: text=弥散功能轻度障碍, bbox=[160, 860, 352, 877]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[202]: text=可逆试验阳性（13.5%），绝对值增加220ml。, bbox=[160, 876, 624, 892]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[203]: text=医生：, bbox=[422, 895, 482, 910]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[204]: text=检查者：, bbox=[561, 895, 682, 914]
2026-08-10 13:08:14,557 INFO     29 [qwen-vl-text] coord item[205]: text=审核者：, bbox=[702, 892, 760, 907]
2026-08-10 13:08:14,559 INFO     29 [qwen-vl-text] page=1 — 219/219 coords, api_time=51.3s
2026-08-10 13:08:14,560 INFO     29 [qwen-vl-text] new_positions (219):
[[1, 190.39999999999998, 329.03499999999997, 163.34799999999998, 178.504], [1, 211.225, 308.21, 178.504, 193.66], [1, 238.0, 283.21999999999997, 195.344, 207.974], [1, 90.44, 113.645, 212.184, 222.28799999999998], [1, 90.44, 113.645, 221.446, 230.708], [1, 90.44, 113.645, 230.708, 239.97], [1, 90.44, 204.67999999999998, 239.97, 249.232], [1, 278.46, 295.12, 212.184, 222.28799999999998], [1, 345.695, 373.65999999999997, 213.868, 222.28799999999998], [1, 279.65, 318.325, 222.28799999999998, 231.54999999999998], [1, 345.695, 365.33, 222.28799999999998, 231.54999999999998], [1, 345.695, 368.305, 231.54999999999998, 239.97], [1, 264.775, 379.015, 239.97, 249.232], [1, 114.835, 141.015, 254.284, 261.86199999999997], [1, 200.515, 217.17499999999998, 254.284, 261.86199999999997], [1, 282.03, 309.4, 254.284, 261.86199999999997], [1, 379.60999999999996, 399.84, 252.6, 260.178], [1, 404.59999999999997, 415.905, 249.232, 255.968], [1, 404.59999999999997, 415.905, 264.388, 270.282], [1, 404.59999999999997, 415.905, 280.38599999999997, 286.28], [1, 282.03, 294.525, 296.384, 302.27799999999996], [1, 282.03, 294.525, 311.53999999999996, 317.43399999999997], [1, 282.03, 294.525, 326.69599999999997, 332.59], [1, 404.59999999999997, 415.905, 339.32599999999996, 345.21999999999997], [1, 278.46, 283.815, 347.746, 353.64], [1, 302.26, 309.4, 347.746, 353.64], [1, 325.465, 333.2, 347.746, 353.64], [1, 349.85999999999996, 357.0, 347.746, 353.64], [1, 373.65999999999997, 381.395, 347.746, 353.64], [1, 398.65, 405.78999999999996, 347.746, 353.64], [1, 227.885, 258.825, 354.48199999999997, 364.586], [1, 282.03, 302.26, 354.48199999999997, 364.586], [1, 315.34999999999997, 339.745, 354.48199999999997, 364.586], [1, 363.54499999999996, 384.37, 354.48199999999997, 364.586], [1, 398.055, 422.45, 354.48199999999997, 364.586], [1, 431.375, 461.125, 353.64, 363.74399999999997], [1, 90.44, 111.265, 366.27, 376.37399999999997], [1, 262.99, 302.26, 366.27, 374.69], [1, 344.505, 384.37, 366.27, 374.69], [1, 90.44, 111.265, 376.37399999999997, 386.478], [1, 262.99, 302.26, 375.532, 383.952], [1, 344.505, 384.37, 375.532, 383.952], [1, 90.44, 101.14999999999999, 395.74, 403.318], [1, 205.87, 218.36499999999998, 394.89799999999997, 403.318], [1, 238.595, 258.825, 394.89799999999997, 403.318], [1, 282.03, 302.26, 394.89799999999997, 403.318], [1, 316.53999999999996, 339.745, 394.89799999999997, 403.318], [1, 90.44, 101.14999999999999, 405.002, 412.58], [1, 186.23499999999999, 218.36499999999998, 404.15999999999997, 412.58], [1, 233.83499999999998, 258.825, 404.15999999999997, 412.58], [1, 278.46, 302.26, 404.15999999999997, 412.58], [1, 321.3, 339.745, 404.15999999999997, 412.58], [1, 90.44, 101.14999999999999, 414.264, 421.842], [1, 186.23499999999999, 218.36499999999998, 413.42199999999997, 421.842], [1, 238.595, 258.825, 413.42199999999997, 421.842], [1, 282.03, 302.26, 413.42199999999997, 421.842], [1, 316.53999999999996, 339.745, 413.42199999999997, 421.842], [1, 90.44, 121.38, 432.788, 440.366], [1, 205.87, 218.36499999999998, 431.94599999999997, 440.366], [1, 238.595, 258.825, 431.94599999999997, 440.366], [1, 282.03, 302.26, 431.94599999999997, 440.366], [1, 321.3, 339.745, 431.94599999999997, 440.366], [1, 364.73499999999996, 384.37, 431.94599999999997, 440.366], [1, 404.005, 422.45, 431.94599999999997, 440.366], [1, 443.275, 461.125, 431.94599999999997, 440.366], [1, 90.44, 107.1, 442.892, 450.46999999999997], [1, 205.87, 218.36499999999998, 442.05, 450.46999999999997], [1, 238.595, 258.825, 442.05, 450.46999999999997], [1, 282.03, 302.26, 442.05, 450.46999999999997], [1, 316.53999999999996, 339.745, 442.05, 450.46999999999997], [1, 90.44, 101.14999999999999, 452.154, 459.73199999999997], [1, 205.87, 218.36499999999998, 451.312, 459.73199999999997], [1, 238.595, 258.825, 451.312, 459.73199999999997], [1, 282.03, 302.26, 451.312, 459.73199999999997], [1, 321.3, 339.745, 451.312, 459.73199999999997], [1, 90.44, 107.1, 471.52, 479.09799999999996], [1, 205.87, 218.36499999999998, 470.678, 479.09799999999996], [1, 238.595, 258.825, 470.678, 479.09799999999996], [1, 282.03, 302.26, 470.678, 479.09799999999996], [1, 321.3, 339.745, 470.678, 479.09799999999996], [1, 364.73499999999996, 384.37, 470.678, 479.09799999999996], [1, 404.005, 422.45, 470.678, 479.09799999999996], [1, 443.275, 461.125, 470.678, 479.09799999999996], [1, 90.44, 116.02499999999999, 480.782, 488.35999999999996], [1, 205.87, 218.36499999999998, 479.94, 488.35999999999996], [1, 238.595, 258.825, 479.94, 488.35999999999996], [1, 282.03, 302.26, 479.94, 488.35999999999996], [1, 321.3, 339.745, 479.94, 488.35999999999996], [1, 364.73499999999996, 384.37, 479.94, 488.35999999999996], [1, 404.005, 422.45, 479.94, 488.35999999999996], [1, 443.275, 461.125, 479.94, 488.35999999999996], [1, 90.44, 146.965, 490.88599999999997, 498.464], [1, 205.87, 218.36499999999998, 490.044, 498.464], [1, 233.83499999999998, 258.825, 490.044, 498.464], [1, 278.46, 302.26, 490.044, 498.464], [1, 321.3, 339.745, 490.044, 498.464], [1, 360.57, 384.37, 490.044, 498.464], [1, 404.005, 422.45, 490.044, 498.464], [1, 448.03499999999997, 461.125, 490.044, 498.464], [1, 90.44, 161.84, 500.14799999999997, 507.726], [1, 205.87, 218.36499999999998, 499.306, 507.726], [1, 233.83499999999998, 258.825, 499.306, 507.726], [1, 278.46, 302.26, 499.306, 507.726], [1, 321.3, 339.745, 499.306, 507.726], [1, 360.57, 384.37, 499.306, 507.726], [1, 404.005, 422.45, 499.306, 507.726], [1, 448.03499999999997, 461.125, 499.306, 507.726], [1, 90.44, 107.1, 510.252, 517.8299999999999], [1, 196.945, 218.36499999999998, 509.40999999999997, 517.8299999999999], [1, 238.595, 258.825, 509.40999999999997, 517.8299999999999], [1, 282.03, 302.26, 509.40999999999997, 517.8299999999999], [1, 321.3, 339.745, 509.40999999999997, 517.8299999999999], [1, 364.73499999999996, 384.37, 509.40999999999997, 517.8299999999999], [1, 404.005, 422.45, 509.40999999999997, 517.8299999999999], [1, 448.03499999999997, 461.125, 509.40999999999997, 517.8299999999999], [1, 90.44, 121.975, 519.514, 527.934], [1, 196.945, 218.36499999999998, 519.514, 527.934], [1, 238.595, 258.825, 519.514, 527.934], [1, 282.03, 302.26, 519.514, 527.934], [1, 321.3, 339.745, 519.514, 527.934], [1, 364.73499999999996, 384.37, 519.514, 527.934], [1, 404.005, 422.45, 519.514, 527.934], [1, 443.275, 461.125, 519.514, 527.934], [1, 90.44, 121.975, 529.6179999999999, 537.196], [1, 196.945, 218.36499999999998, 528.776, 537.196], [1, 238.595, 258.825, 528.776, 537.196], [1, 282.03, 302.26, 528.776, 537.196], [1, 321.3, 339.745, 528.776, 537.196], [1, 364.73499999999996, 384.37, 528.776, 537.196], [1, 404.005, 422.45, 528.776, 537.196], [1, 443.275, 461.125, 528.776, 537.196], [1, 90.44, 121.975, 539.722, 547.3], [1, 196.945, 218.36499999999998, 538.88, 547.3], [1, 238.595, 258.825, 538.88, 547.3], [1, 282.03, 302.26, 538.88, 547.3], [1, 321.3, 339.745, 538.88, 547.3], [1, 364.73499999999996, 384.37, 538.88, 547.3], [1, 404.005, 422.45, 538.88, 547.3], [1, 448.03499999999997, 461.125, 538.88, 547.3], [1, 90.44, 142.20499999999998, 548.984, 557.404], [1, 196.945, 218.36499999999998, 548.984, 557.404], [1, 238.595, 258.825, 548.984, 557.404], [1, 282.03, 302.26, 548.984, 557.404], [1, 321.3, 339.745, 548.984, 557.404], [1, 364.73499999999996, 384.37, 548.984, 557.404], [1, 404.005, 422.45, 548.984, 557.404], [1, 443.275, 461.125, 548.984, 557.404], [1, 90.44, 218.36499999999998, 559.088, 567.5079999999999], [1, 282.03, 302.26, 558.246, 566.6659999999999], [1, 364.73499999999996, 384.37, 558.246, 566.6659999999999], [1, 448.03499999999997, 461.125, 558.246, 566.6659999999999], [1, 90.44, 218.36499999999998, 568.35, 576.77], [1, 282.03, 302.26, 568.35, 576.77], [1, 364.73499999999996, 384.37, 568.35, 576.77], [1, 443.275, 461.125, 568.35, 576.77], [1, 90.44, 108.28999999999999, 587.716, 595.294], [1, 187.42499999999998, 218.36499999999998, 586.874, 595.294], [1, 233.83499999999998, 258.825, 586.874, 595.294], [1, 278.46, 302.26, 586.874, 595.294], [1, 321.3, 339.745, 586.874, 595.294], [1, 362.35499999999996, 387.34499999999997, 593.61, 601.188], [1, 406.97999999999996, 426.02, 593.61, 601.188], [1, 443.275, 461.125, 593.61, 601.188], [1, 90.44, 131.495, 597.8199999999999, 605.398], [1, 187.42499999999998, 218.36499999999998, 596.978, 605.398], [1, 233.83499999999998, 258.825, 596.978, 605.398], [1, 278.46, 302.26, 596.978, 605.398], [1, 321.3, 339.745, 596.978, 605.398], [1, 90.44, 123.16499999999999, 616.3439999999999, 623.922], [1, 205.87, 218.36499999999998, 615.502, 623.922], [1, 238.595, 258.825, 615.502, 623.922], [1, 282.03, 302.26, 615.502, 623.922], [1, 316.53999999999996, 339.745, 615.502, 623.922], [1, 90.44, 123.16499999999999, 626.448, 634.026], [1, 205.87, 218.36499999999998, 625.606, 634.026], [1, 238.595, 258.825, 625.606, 634.026], [1, 282.03, 302.26, 625.606, 634.026], [1, 316.53999999999996, 339.745, 625.606, 634.026], [1, 90.44, 118.405, 635.7099999999999, 643.288], [1, 205.87, 218.36499999999998, 635.7099999999999, 643.288], [1, 238.595, 258.825, 635.7099999999999, 643.288], [1, 282.03, 302.26, 635.7099999999999, 643.288], [1, 316.53999999999996, 339.745, 635.7099999999999, 643.288], [1, 90.44, 138.04, 645.814, 653.3919999999999], [1, 205.87, 218.36499999999998, 644.972, 653.3919999999999], [1, 233.83499999999998, 258.825, 644.972, 653.3919999999999], [1, 278.46, 302.26, 644.972, 653.3919999999999], [1, 316.53999999999996, 339.745, 644.972, 653.3919999999999], [1, 90.44, 128.51999999999998, 655.076, 662.654], [1, 153.51, 218.36499999999998, 654.2339999999999, 662.654], [1, 238.595, 258.825, 654.2339999999999, 662.654], [1, 282.03, 302.26, 654.2339999999999, 662.654], [1, 321.3, 339.745, 654.2339999999999, 662.654], [1, 90.44, 128.51999999999998, 665.18, 672.7579999999999], [1, 143.98999999999998, 218.36499999999998, 664.338, 672.7579999999999], [1, 238.595, 258.825, 664.338, 672.7579999999999], [1, 282.03, 302.26, 664.338, 672.7579999999999], [1, 321.3, 339.745, 664.338, 672.7579999999999], [1, 92.225, 121.975, 686.23, 698.86], [1, 95.19999999999999, 251.685, 698.018, 711.49], [1, 94.60499999999999, 166.005, 711.49, 724.962], [1, 95.19999999999999, 209.44, 724.12, 738.434], [1, 95.19999999999999, 371.28, 737.592, 751.064], [1, 251.08999999999997, 286.78999999999996, 753.5899999999999, 766.22], [1, 333.79499999999996, 405.78999999999996, 753.5899999999999, 769.588], [1, 417.69, 452.2, 751.064, 763.694], [1, 90.44, 128.51999999999998, 665.18, 672.7579999999999], [1, 143.98999999999998, 218.36499999999998, 664.338, 672.7579999999999], [1, 238.595, 258.825, 664.338, 672.7579999999999], [1, 282.03, 302.26, 664.338, 672.7579999999999], [1, 321.3, 339.745, 664.338, 672.7579999999999], [1, 92.225, 121.975, 686.23, 698.86], [1, 95.19999999999999, 251.685, 698.018, 711.49], [1, 94.60499999999999, 166.005, 711.49, 724.962], [1, 95.19999999999999, 209.44, 724.12, 738.434], [1, 95.19999999999999, 371.28, 737.592, 751.064], [1, 251.08999999999997, 286.78999999999996, 753.5899999999999, 766.22], [1, 333.79499999999996, 405.78999999999996, 753.5899999999999, 769.588], [1, 417.69, 452.2, 751.064, 763.694]]
2026-08-10 13:08:14,560 INFO     29 [qwen-vl-text] ═══ DONE ═══ 219 positions, pages=1, time=61.9s
2026-08-10 13:08:14,575 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:08:14,575 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:08:14,575 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:08:14,576 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:08:14.576+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 39, "failed": 0, "current": {"465f3f9094bc11f1bd9827cf206dfa2d": {"id": "465f3f9094bc11f1bd9827cf206dfa2d", "doc_id": "4630c9da94bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "type": "pdf", "location": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "size": 241486, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367178063, "task_type": "dataflow", "root_trace_id": "c90b5c4d512840ec92722025b8967e21", "root_traceparent": "00-c90b5c4d512840ec92722025b8967e21-6b6dbfd12195e555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:08:14,581 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:08:14,581 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:08:16,839 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:08:16,848 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:08:16,848 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "262 items", "markdown": "", "text": "", "name": "LIJI 徐州中心医院.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:08:16,849 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:08:16,850 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:08:16,864 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:08:16,864 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'DischargeRecord': 1, 'ExaminationReport': 1}", "name": "LIJI 徐州中心医院.pdf"}
2026-08-10 13:08:16,864 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:08:16,905 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786367178382, 'update_date': datetime.datetime(2026, 8, 10, 13, 6, 18), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1023933, 'status': '1'}
2026-08-10 13:08:18,003 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=徐州矿务集团总医院
徐州医科大学第二附属医院
间病房入、出院记录
：十二病区护理单元 床号：6 住院号：00214234
工作单位：-
性别：女
年龄：49岁
籍贯：江苏省徐州市泉山区
民族：汉族
婚姻：已婚
职业：职工
住址：江苏徐州市
供史者与（患者关系）：本人
入院日期：2025-04-23 09:05:08
记录日期：2025年04月25日08时29分
主诉：声音嘶哑10余天
入院情况：患者因“声音嘶哑10余天”入院。查体：会厌无肿胀，杓会厌襞稍充血肿胀，室带无新生物，右侧声
带边缘息肉样隆起，表面光滑，声门闭合不全。辅助检查：电子喉镜（2025-04-20本院）示：舌扁桃体增生，会
厌无充血，声带稍肿胀，活动可，右侧声带边缘息肉样肿物，声门闭合欠佳，杓间区稍红肿。
入院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。
手术名称：1.内镜下声带病损切除术（内镜下声带病损切除术）
年04月24日
手术日期：2025
诊疗经过：入院后完善血常规、肝肾功能、电解质、血凝、病毒检查，回报未示明显异常。常规心电图检查（十
二通道）（20250423094755）：窦性心动过缓CT胸部平扫（多平面重建），CT咽喉平扫+二维重建（20250423）：
左侧杓会厌襞黏膜增厚；右侧声带局部稍增厚、隆起。建议结合喉镜检查。两肺多发实性微小结节。右肺上叶
钙化灶。甲状腺两侧叶密度不均。建议：结合超声检查。请结合临床随诊。手术指征明确，无明显手术禁忌，
昨日全麻下行喉镜下声带病损切除术，手术顺利，术后予抗炎消肿、雾化等对症治疗，恢复可，要求今日出院。
出院情况：（）治愈 口好转 口未愈 口未治 口转院 口自动出院）伤口愈合：-
患者一般情况可，声音嘶哑，稍咽痛，无吞咽疼痛，无咽部出血，无发热，饮食睡眠可，大小便正常。查体：神
志清，精神可，心肺无明显异常。咽喉部粘膜充血，会厌无充血肿胀，杓会厌襞粘膜无肿胀，双侧声带稍水肿，
声门闭合良好。
出院诊断：出院诊断：1.声带息肉（右），2.喉咽反流，3.急性咽喉炎。
出院日期：2025-04-25
出院医嘱：1.注意声休2周，禁食辛辣刺激，2.口服黄氏响声丸/西瓜霜含片，3.2-3周后复查喉镜；4.门诊随诊
X光片号：
CT号：
MRI号：
病理号：
医师签名：
门诊病历已交病人或家属，签收人：
主治医师签名：
第1页
---
徐州医科大学附属医院
肺功能检查报告
舒张试验
姓名：
科别：
性别：
身高：158 cm
号：210254
/住院号：门诊
48 岁
体重：49.6 kg
Flow [L/s]
F/V ex
Volume [L]
CO [%]
0.30
0.25
0.20
0.15
0.10
0.05
0.00
0
10
5
0
5
10
1
2
3
4
5
6
7
F/V in
Time [s]
0
10
20
30
40
50
预计值
前次
前/预
后次
后/预
改善率
日期
24-11-29
24-11-29
时间
10:51:30
11:27:38
VT
[L]
0.35
0.42
118.7
BF
[1/min]
20.00
19.20
96.0
MV
[L/min]
7.09
8.07
113.9
VC MAX
[L]
2.93
2.48
84.6
2.78
94.9
12.2
ERV
[L]
0.96
1.10
115.1
IC
[L]
1.97
1.37
69.7
FVC
[L]
2.86
2.48
86.6
2.73
95.3
10.0
FEV 1
[L]
2.44
1.64
67.3
1.86
76.4
13.5
FEV 1 % FVC
[%]
82.57
66.28
80.3
68.41
82.9
3.2
FEV 1 % VC MAX
[%]
79.98
66.28
82.9
67.06
83.8
1.2
PEF
[L/s]
6.14
4.14
67.4
4.24
69.1
2.5
MEF 75
[L/s]
5.49
2.43
44.2
3.22
58.7
32.8
MEF 50
[L/s]
3.63
1.22
31.8
1.38
36.1
13.6
MEF 25
[L/s]
1.57
0.38
24.2
0.41
25.9
7.4
MMEF 75/25
[L/s]
3.26
0.94
28.7
1.06
32.4
13.1
V backextrapolation ex [L]
0.07
0.07
0.2
V backextrapol. % FVC [%]
2.64
2.40
-9.0
MVV
[L/min]
95.44
64.07
67.1
55.95
58.6
13.5
FEV 1*30
[L/min]
95.44
49.27
51.6
TLC-SB
[L]
4.64
4.76
102.7
FRC-SB
[L]
2.59
3.27
126.5
RV-SB
[L]
1.63
2.30
141.5
RV%TLC-SB
[%]
35.28
48.35
137.1
DLCO SB
[mmol/min/kPa]
7.83
5.92
75.5
DLCO/VA
[mmol/min/kPa/L]
1.69
1.27
75.3
结论：
中度阻塞性通气功能障碍
残总比增高
弥散功能轻度障碍
可逆试验阳性（13.5%），绝对值增加220ml。
医生：
检查者：
审核者：
2026-08-10 13:08:18,259 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:08:18,259 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'DischargeRecord': 1, 'ExaminationReport': 1}", "name": "LIJI 徐州中心医院.pdf", "embedding_token_consumption": 1839}
2026-08-10 13:08:18,259 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:08:18,378 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:08:18,379 INFO     29 [Trace] task=465f3f90 | doc=LIJI 徐州中心医院.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:08:18,381 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:08:18,381 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:08:18,385 INFO     29 set_progress(465f3f9094bc11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:08:18 [DOC Engine]:
Start to index...
2026-08-10 13:08:18,398 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 13:08:18,402 INFO     29 set_progress(465f3f9094bc11f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 13:08:18,411 INFO     29 set_progress(465f3f9094bc11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:08:18 Indexing done (0.02s). Task done (114.49s)
2026-08-10 13:08:18,415 INFO     29 [Done], chunks(2), token(1839), elapsed:114.49
2026-08-10 13:08:18,482 INFO     29 handle_task done for task {"id": "465f3f9094bc11f1bd9827cf206dfa2d", "doc_id": "4630c9da94bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "type": "pdf", "location": "LIJI \u5f90\u5dde\u4e2d\u5fc3\u533b\u9662.pdf", "size": 241486, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786367178063, "task_type": "dataflow", "root_trace_id": "c90b5c4d512840ec92722025b8967e21", "root_traceparent": "00-c90b5c4d512840ec92722025b8967e21-6b6dbfd12195e555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
