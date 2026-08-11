# 基准结果：MEFE(1).pdf

## 基本信息

- 文件：`MEFE(1).pdf`
- 大小：5373.2 KB
- PDF 总页数：3
- doc_id：`e6e9ad0c948411f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T14:29:54  完成时间：2026-08-10T14:32:56  耗时：181.8s
- progress_msg：`06:32:23 Indexing done (0.07s). Task done (144.71s)`
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

- SmartSplitter Types 统计：`{"ExaminationReport": 1, "OutpatientRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 2, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 06:32:21,979 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 06:29:57,897 INFO     29 handle_task begin for task {"id": "e7b1979a948411f1bd9827cf206dfa2d", "doc_id": "e6e9ad0c948411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MEFE(1).pdf", "type": "pdf", "location": "MEFE(1).pdf", "size": 5502142, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343396901, "task_type": "dataflow", "root_trace_id": "5667f9593fa8497eabc7fd15b6ab98c0", "root_traceparent": "00-5667f9593fa8497eabc7fd15b6ab98c0-4a2925d1ccf16074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 06:29:58,239 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 06:29:58,363 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 06:29:58,381 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:29:58,381 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 06:29:58,381 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 06:29:58,392 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 06:29:58,392 INFO     29 ============================================================
2026-08-10 06:29:58,392 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 06:29:58,392 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 06:29:58,392 INFO     29 ============================================================
2026-08-10 06:29:58,393 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 06:29:58,393 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 06:29:58,395 INFO     29 No torch found.
2026-08-10 06:29:59,276 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=3
2026-08-10 06:29:59,726 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2367227, prompt_len=764
2026-08-10 06:30:02,169 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-05-28"
}
```
2026-08-10 06:30:02,170 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-05-28
2026-08-10 06:30:02,184 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2367227, prompt_len=401
2026-08-10 06:30:17,794 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:30:17.792+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 6, "failed": 0, "current": {"e7b1979a948411f1bd9827cf206dfa2d": {"id": "e7b1979a948411f1bd9827cf206dfa2d", "doc_id": "e6e9ad0c948411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MEFE(1).pdf", "type": "pdf", "location": "MEFE(1).pdf", "size": 5502142, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343396901, "task_type": "dataflow", "root_trace_id": "5667f9593fa8497eabc7fd15b6ab98c0", "root_traceparent": "00-5667f9593fa8497eabc7fd15b6ab98c0-4a2925d1ccf16074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:30:17,807 INFO     29 [qwen-vl-parser] text API response (len=1203):
["JAEGER TOENNIES", "徐州市中心医院", "东南大学医学院附属徐州医院", "肺功能检查报告", "姓名：", "门诊/住院号：5832", "身高：178 cm", "年龄：32 Years", "性别：男", "测试号：2025051412", "体重：68 kg", "科别：呼吸与危重症医学科", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "1", "2", "10", "F/V in", "日期", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "时间", "25/5/28", "25/5/28", "9:33:12", "10:00:0", "VC MAX", "[L]", "5.31", "4.00", "75.3", "4.63", "87.1", "15.62", "ERV", "[L]", "1.56", "IC", "[L]", "3.75", "FVC", "[L]", "5.08", "4.00", "78.7", "4.62", "91.0", "15.55", "FEV 1", "[L]", "4.24", "2.51", "59.2", "3.07", "72.5", "22.53", "FEV 1 % FVC", "[%]", "82.49", "62.65", "75.9", "66.43", "80.5", "6.05", "FEV 1 % VC MAX", "[%]", "81.45", "62.65", "76.9", "66.39", "81.5", "5.98", "PEF", "[L/s]", "9.70", "7.10", "73.1", "9.89", "101.9", "39.28", "MEF 75", "[L/s]", "8.32", "3.64", "43.8", "5.40", "64.8", "48.11", "MEF 50", "[L/s]", "5.40", "1.57", "29.1", "2.29", "42.4", "45.60", "MEF 25", "[L/s]", "2.47", "0.49", "19.7", "0.69", "28.1", "42.74", "MMEF 75/25", "[L/s]", "4.78", "1.24", "26.0", "1.72", "36.0", "38.55", "V backextrapol. % FVC", "[%]", "2.29", "2.55", "11.69", "结论：", "支气管舒张试验阳性", "医生签字：", "WPS Office", "快拍即存·WPS拍照扫描"]
2026-08-10 06:30:17,808 INFO     29 [qwen-vl-parser] page=1 text: 136 lines (bbox 0-135)
2026-08-10 06:30:17,808 INFO     29 [qwen-vl-parser] page=1 text: 136 sections
2026-08-10 06:30:18,086 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=917329, prompt_len=764
2026-08-10 06:30:21,305 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-02-20"}
```
2026-08-10 06:30:21,305 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2025-02-20
2026-08-10 06:30:21,318 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=917329, prompt_len=401
2026-08-10 06:30:25,912 INFO     29 [qwen-vl-parser] text API response (len=718):
["徐州市中心医院", "门（急）诊病历", "姓名：", "性别：男", "科室：呼吸与危重症门诊", "号别：普通号", "姓名", "证件类型", "居民身份证", "性别", "男", "证件号码", "3:", "出生日期", "1992年07月11日", "门诊编号", "0005832911", "婚姻", "就诊时间", "2025-02-20 13:22", "陪伴者姓名", "初诊/复诊/急诊", "复诊", "陪伴者与患者的关系", "过敏史", "否认(病史提供人)", "联系人电话", "主诉：支气管哮喘复诊。", "病史：现病史：哮喘，患者来院进行D5982C00008项目V15随访", "既往史：有既往疾病史，鼻炎。", "体格检查：", "体温：(℃)，脉搏：次/分，血压：/(mmHg)，呼吸：次/分，意识状态：清醒", "皮肤粘膜：颜色正常，无皮疹，无皮下出血，无水肿。", "胸部：外形正常，无胸壁压痛。肺脏及胸膜：呼吸音正常，未闻及啰音，未触及胸", "膜摩擦音。", "心脏：心律齐，未闻及杂音，未闻及心包摩擦音，周围血管征阴性。", "腹部：外形正常，无压痛，无反跳痛。未触及包块。肝脏未触及。无肾区叩击痛，", "移动性浊音阴性，肠鸣音正常。", "神经反射：浅反射正常，深反射正常，病理反射阴性，脑膜刺激征阴性。", "诊断：支气管哮喘", "处理措施：", "根据方案要求，患者今日来院进行V15随访，患者于今日08点", "00分左右到院随访，与患者核实上次访视至今未进行过任何", "疫苗接种", "第（1）页", "WPS Office", "快拍即存·WPS拍照扫描"]
2026-08-10 06:30:25,912 INFO     29 [qwen-vl-parser] page=2 text: 47 lines (bbox 136-182)
2026-08-10 06:30:25,912 INFO     29 [qwen-vl-parser] page=2 text: 47 sections
2026-08-10 06:30:26,099 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=925965, prompt_len=764
2026-08-10 06:30:28,590 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 06:30:28,590 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 06:30:28,604 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=925965, prompt_len=401
2026-08-10 06:30:33,974 INFO     29 [qwen-vl-parser] text API response (len=694):
["徐州市中心医院", "门（急）诊病历", "姓名", "性别：男", "科室：呼吸与危重症门诊", "号别：普通号", "患者万托林已停用大于6h，昨晚完成白色吸入剂的吸入时间是21：40，", "昨晚完成红色吸入剂的吸入时间是21：43。今晨未吸入研究药物，规律", "吸入研究药物中，未出现多服及漏服现象", "自上次访视至今，无不适，无新增合并用药，已和患者确认无其他门诊", "以及住院记录，无哮喘急性发作，已根据方案要求清洁吸入器装置", "查看患者电子日志，日志偶有漏做现象，进行两次给药前肺功能测定", "患者已空腹大于8小时，完成血样采集", "患者自行完成ACQ6问卷，AQLQ+12问卷，EQ-5D-5L问卷，PGIC问卷，患者", "于今日09点26分完成白色吸入剂2喷，09点28分完成红色吸入剂2喷，患", "者已掌握给药方法。进行给药后15min肺功能检查，进行给药后30min肺", "功能检查，进行给药后1h肺功能检查，进行给药后2h肺功能检查，进行", "给药后3h肺功能检查", "告知患者今日已完成试验，嘱后续治疗方案为信必可320ug bid 吸入，", "今日登记IRT系统进行完成试验登记，回收相关设备和药物。", "是否留观：否", "特别提醒：根据《传染病防治法》《治安管理处罚法》等法律规定，如果您隐", "瞒上述情况或者拒绝配合医务人员开展调查等处置措施的，将承担相应的法律责任。", "承诺以上情况均属实。", "医师签名：张敏浩", "患者签名：", "第（2）页", "WPS Office", "快拍即存·WPS拍照扫描"]
2026-08-10 06:30:33,974 INFO     29 [qwen-vl-parser] page=3 text: 29 lines (bbox 183-211)
2026-08-10 06:30:33,974 INFO     29 [qwen-vl-parser] page=3 text: 29 sections
2026-08-10 06:30:33,974 INFO     29 [qwen-vl-parser] parse_pdf done: 212 sections from 3 pages.
2026-08-10 06:30:33,981 INFO     29 Close text detector.
2026-08-10 06:30:34,477 INFO     29 Close text recognizer.
2026-08-10 06:30:35,044 INFO     29 Close recognizer.
2026-08-10 06:30:35,511 INFO     29 Close recognizer.
2026-08-10 06:30:36,019 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 06:30:36,019 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Parser:MedLink | outputs={"html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "json"}
2026-08-10 06:30:36,019 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 06:30:36,062 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:30:36,062 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] JAEGER TOENNIES\n[BBOX-1] 徐州市中心医院\n[BBOX-2] 东南大学医学院附属徐州医院\n[BBOX-3] 肺功能检查报告\n[BBOX-4] 姓名：\n[BBOX-5] 门诊/住院号：5832\n[BBOX-6] 身高：178 cm\n[BBOX-7] 年龄：32 Years\n[BBOX-8] 性别：男\n[BBOX-9] 测试号：2025051412\n[BBOX-10] 体重：68 kg\n[BBOX-11] 科别：呼吸与危重症医学科\n[BBOX-12] Flow [L/s]\n[BBOX-13] F/V ex\n[BBOX-14] 10\n[BBOX-15] 5\n[BBOX-16] 0\n[BBOX-17] 1\n[BBOX-18] 2\n[BBOX-19] 3\n[BBOX-20] 4\n[BBOX-21] 5\n[BBOX-22] 6\n[BBOX-23] 7\n[BBOX-24] 1\n[BBOX-25] 2\n[BBOX-26] 10\n[BBOX-27] F/V in\n[BBOX-28] 日期\n[BBOX-29] 预计值\n[BBOX-30] 前次\n[BBOX-31] 前/预\n[BBOX-32] 后次\n[BBOX-33] 后/预\n[BBOX-34] 改善率\n[BBOX-35] 时间\n[BBOX-36] 25/5/28\n[BBOX-37] 25/5/28\n[BBOX-38] 9:33:12\n[BBOX-39] 10:00:0\n[BBOX-40] VC MAX\n[BBOX-41] [L]\n[BBOX-42] 5.31\n[BBOX-43] 4.00\n[BBOX-44] 75.3\n[BBOX-45] 4.63\n[BBOX-46] 87.1\n[BBOX-47] 15.62\n[BBOX-48] ERV\n[BBOX-49] [L]\n[BBOX-50] 1.56\n[BBOX-51] IC\n[BBOX-52] [L]\n[BBOX-53] 3.75\n[BBOX-54] FVC\n[BBOX-55] [L]\n[BBOX-56] 5.08\n[BBOX-57] 4.00\n[BBOX-58] 78.7\n[BBOX-59] 4.62\n[BBOX-60] 91.0\n[BBOX-61] 15.55\n[BBOX-62] FEV 1\n[BBOX-63] [L]\n[BBOX-64] 4.24\n[BBOX-65] 2.51\n[BBOX-66] 59.2\n[BBOX-67] 3.07\n[BBOX-68] 72.5\n[BBOX-69] 22.53\n[BBOX-70] FEV 1 % FVC\n[BBOX-71] [%]\n[BBOX-72] 82.49\n[BBOX-73] 62.65\n[BBOX-74] 75.9\n[BBOX-75] 66.43\n[BBOX-76] 80.5\n[BBOX-77] 6.05\n[BBOX-78] FEV 1 % VC MAX\n[BBOX-79] [%]\n[BBOX-80] 81.45\n[BBOX-81] 62.65\n[BBOX-82] 76.9\n[BBOX-83] 66.39\n[BBOX-84] 81.5\n[BBOX-85] 5.98\n[BBOX-86] PEF\n[BBOX-87] [L/s]\n[BBOX-88] 9.70\n[BBOX-89] 7.10\n[BBOX-90] 73.1\n[BBOX-91] 9.89\n[BBOX-92] 101.9\n[BBOX-93] 39.28\n[BBOX-94] MEF 75\n[BBOX-95] [L/s]\n[BBOX-96] 8.32\n[BBOX-97] 3.64\n[BBOX-98] 43.8\n[BBOX-99] 5.40\n[BBOX-100] 64.8\n[BBOX-101] 48.11\n[BBOX-102] MEF 50\n[BBOX-103] [L/s]\n[BBOX-104] 5.40\n[BBOX-105] 1.57\n[BBOX-106] 29.1\n[BBOX-107] 2.29\n[BBOX-108] 42.4\n[BBOX-109] 45.60\n[BBOX-110] MEF 25\n[BBOX-111] [L/s]\n[BBOX-112] 2.47\n[BBOX-113] 0.49\n[BBOX-114] 19.7\n[BBOX-115] 0.69\n[BBOX-116] 28.1\n[BBOX-117] 42.74\n[BBOX-118] MMEF 75/25\n[BBOX-119] [L/s]\n[BBOX-120] 4.78\n[BBOX-121] 1.24\n[BBOX-122] 26.0\n[BBOX-123] 1.72\n[BBOX-124] 36.0\n[BBOX-125] 38.55\n[BBOX-126] V backextrapol. % FVC\n[BBOX-127] [%]\n[BBOX-128] 2.29\n[BBOX-129] 2.55\n[BBOX-130] 11.69\n[BBOX-131] 结论：\n[BBOX-132] 支气管舒张试验阳性\n[BBOX-133] 医生签字：\n[BBOX-134] WPS Office\n[BBOX-135] 快拍即存·WPS拍照扫描\n[BBOX-136] 徐州市中心医院\n[BBOX-137] 门（急）诊病历\n[BBOX-138] 姓名：\n[BBOX-139] 性别：男\n[BBOX-140] 科室：呼吸与危重症门诊\n[BBOX-141] 号别：普通号\n[BBOX-142] 姓名\n[BBOX-143] 证件类型\n[BBOX-144] 居民身份证\n[BBOX-145] 性别\n[BBOX-146] 男\n[BBOX-147] 证件号码\n[BBOX-148] 3:\n[BBOX-149] 出生日期\n[BBOX-150] 1992年07月11日\n[BBOX-151] 门诊编号\n[BBOX-152] 0005832911\n[BBOX-153] 婚姻\n[BBOX-154] 就诊时间\n[BBOX-155] 2025-02-20 13:22\n[BBOX-156] 陪伴者姓名\n[BBOX-157] 初诊/复诊/急诊\n[BBOX-158] 复诊\n[BBOX-159] 陪伴者与患者的关系\n[BBOX-160] 过敏史\n[BBOX-161] 否认(病史提供人)\n[BBOX-162] 联系人电话\n[BBOX-163] 主诉：支气管哮喘复诊。\n[BBOX-164] 病史：现病史：哮喘，患者来院进行D5982C00008项目V15随访\n[BBOX-165] 既往史：有既往疾病史，鼻炎。\n[BBOX-166] 体格检查：\n[BBOX-167] 体温：(℃)，脉搏：次/分，血压：/(mmHg)，呼吸：次/分，意识状态：清醒\n[BBOX-168] 皮肤粘膜：颜色正常，无皮疹，无皮下出血，无水肿。\n[BBOX-169] 胸部：外形正常，无胸壁压痛。肺脏及胸膜：呼吸音正常，未闻及啰音，未触及胸\n[BBOX-170] 膜摩擦音。\n[BBOX-171] 心脏：心律齐，未闻及杂音，未闻及心包摩擦音，周围血管征阴性。\n[BBOX-172] 腹部：外形正常，无压痛，无反跳痛。未触及包块。肝脏未触及。无肾区叩击痛，\n[BBOX-173] 移动性浊音阴性，肠鸣音正常。\n[BBOX-174] 神经反射：浅反射正常，深反射正常，病理反射阴性，脑膜刺激征阴性。\n[BBOX-175] 诊断：支气管哮喘\n[BBOX-176] 处理措施：\n[BBOX-177] 根据方案要求，患者今日来院进行V15随访，患者于今日08点\n[BBOX-178] 00分左右到院随访，与患者核实上次访视至今未进行过任何\n[BBOX-179] 疫苗接种\n[BBOX-180] 第（1）页\n[BBOX-181] WPS Office\n[BBOX-182] 快拍即存·WPS拍照扫描\n[BBOX-183] 徐州市中心医院\n[BBOX-184] 门（急）诊病历\n[BBOX-185] 姓名\n[BBOX-186] 性别：男\n[BBOX-187] 科室：呼吸与危重症门诊\n[BBOX-188] 号别：普通号\n[BBOX-189] 患者万托林已停用大于6h，昨晚完成白色吸入剂的吸入时间是21：40，\n[BBOX-190] 昨晚完成红色吸入剂的吸入时间是21：43。今晨未吸入研究药物，规律\n[BBOX-191] 吸入研究药物中，未出现多服及漏服现象\n[BBOX-192] 自上次访视至今，无不适，无新增合并用药，已和患者确认无其他门诊\n[BBOX-193] 以及住院记录，无哮喘急性发作，已根据方案要求清洁吸入器装置\n[BBOX-194] 查看患者电子日志，日志偶有漏做现象，进行两次给药前肺功能测定\n[BBOX-195] 患者已空腹大于8小时，完成血样采集\n[BBOX-196] 患者自行完成ACQ6问卷，AQLQ+12问卷，EQ-5D-5L问卷，PGIC问卷，患者\n[BBOX-197] 于今日09点26分完成白色吸入剂2喷，09点28分完成红色吸入剂2喷，患\n[BBOX-198] 者已掌握给药方法。进行给药后15min肺功能检查，进行给药后30min肺\n[BBOX-199] 功能检查，进行给药后1h肺功能检查，进行给药后2h肺功能检查，进行\n[BBOX-200] 给药后3h肺功能检查\n[BBOX-201] 告知患者今日已完成试验，嘱后续治疗方案为信必可320ug bid 吸入，\n[BBOX-202] 今日登记IRT系统进行完成试验登记，回收相关设备和药物。\n[BBOX-203] 是否留观：否\n[BBOX-204] 特别提醒：根据《传染病防治法》《治安管理处罚法》等法律规定，如果您隐\n[BBOX-205] 瞒上述情况或者拒绝配合医务人员开展调查等处置措施的，将承担相应的法律责任。\n[BBOX-206] 承诺以上情况均属实。\n[BBOX-207] 医师签名：张敏浩\n[BBOX-208] 患者签名：\n[BBOX-209] 第（2）页\n[BBOX-210] WPS Office\n[BBOX-211] 快拍即存·WPS拍照扫描"
  }
]
2026-08-10 06:30:43,052 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:30:43,084 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'ExaminationReport': 1, 'OutpatientRecord': 1}
2026-08-10 06:30:43,104 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 06:30:43,104 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks": "2 items, types={'ExaminationReport': 1, 'OutpatientRecord': 1}"}
2026-08-10 06:30:43,104 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 06:30:43,104 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Examination': 1, 'chunks_Clinical': 1}
2026-08-10 06:30:43,120 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 06:30:43,121 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks": "2 items, types={'ExaminationReport': 1, 'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:30:43,121 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 06:30:43,133 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:30:43,133 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:30:44,420 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:30:44,432 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 06:30:44,432 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:30:44,432 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 06:30:44,443 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:30:44,443 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:30:45,390 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:30:45,399 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 06:30:45,399 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:30:45,399 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 06:30:45,408 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:30:45,409 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:30:45,409 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 06:30:45,409 INFO     29 [qwen-vl-text] positions(74): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:30:45,409 INFO     29 [qwen-vl-text] page grouping: [1, 2], lines per page: [47, 27]
2026-08-10 06:30:45,607 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 06:30:45,804 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 06:30:45,805 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1159
2026-08-10 06:30:45,805 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:30:45,805 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 136, \"bbox_end\": 209, \"encounter_dates\": [\"2025-02-20\"], \"department\": \"呼吸与危重症门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "徐州市中心医院\n门（急）诊病历\n姓名：\n性别：男\n科室：呼吸与危重症门诊\n号别：普通号\n姓名\n证件类型\n居民身份证\n性别\n男\n证件号码\n3:\n出生日期\n1992年07月11日\n门诊编号\n0005832911\n婚姻\n就诊时间\n2025-02-20 13:22\n陪伴者姓名\n初诊/复诊/急诊\n复诊\n陪伴者与患者的关系\n过敏史\n否认(病史提供人)\n联系人电话\n主诉：支气管哮喘复诊。\n病史：现病史：哮喘，患者来院进行D5982C00008项目V15随访\n既往史：有既往疾病史，鼻炎。\n体格检查：\n体温：(℃)，脉搏：次/分，血压：/(mmHg)，呼吸：次/分，意识状态：清醒\n皮肤粘膜：颜色正常，无皮疹，无皮下出血，无水肿。\n胸部：外形正常，无胸壁压痛。肺脏及胸膜：呼吸音正常，未闻及啰音，未触及胸\n膜摩擦音。\n心脏：心律齐，未闻及杂音，未闻及心包摩擦音，周围血管征阴性。\n腹部：外形正常，无压痛，无反跳痛。未触及包块。肝脏未触及。无肾区叩击痛，\n移动性浊音阴性，肠鸣音正常。\n神经反射：浅反射正常，深反射正常，病理反射阴性，脑膜刺激征阴性。\n诊断：支气管哮喘\n处理措施：\n根据方案要求，患者今日来院进行V15随访，患者于今日08点\n00分左右到院随访，与患者核实上次访视至今未进行过任何\n疫苗接种\n第（1）页\nWPS Office\n快拍即存·WPS拍照扫描\n徐州市中心医院\n门（急）诊病历\n姓名\n性别：男\n科室：呼吸与危重症门诊\n号别：普通号\n患者万托林已停用大于6h，昨晚完成白色吸入剂的吸入时间是21：40，\n昨晚完成红色吸入剂的吸入时间是21：43。今晨未吸入研究药物，规律\n吸入研究药物中，未出现多服及漏服现象\n自上次访视至今，无不适，无新增合并用药，已和患者确认无其他门诊\n以及住院记录，无哮喘急性发作，已根据方案要求清洁吸入器装置\n查看患者电子日志，日志偶有漏做现象，进行两次给药前肺功能测定\n患者已空腹大于8小时，完成血样采集\n患者自行完成ACQ6问卷，AQLQ+12问卷，EQ-5D-5L问卷，PGIC问卷，患者\n于今日09点26分完成白色吸入剂2喷，09点28分完成红色吸入剂2喷，患\n者已掌握给药方法。进行给药后15min肺功能检查，进行给药后30min肺\n功能检查，进行给药后1h肺功能检查，进行给药后2h肺功能检查，进行\n给药后3h肺功能检查\n告知患者今日已完成试验，嘱后续治疗方案为信必可320ug bid 吸入，\n今日登记IRT系统进行完成试验登记，回收相关设备和药物。\n是否留观：否\n特别提醒：根据《传染病防治法》《治安管理处罚法》等法律规定，如果您隐\n瞒上述情况或者拒绝配合医务人员开展调查等处置措施的，将承担相应的法律责任。\n承诺以上情况均属实。\n医师签名：张敏浩\n患者签名：\n第（2）页",
    "role": "user"
  }
]
2026-08-10 06:30:47,836 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:30:47.833+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 6, "failed": 0, "current": {"e7b1979a948411f1bd9827cf206dfa2d": {"id": "e7b1979a948411f1bd9827cf206dfa2d", "doc_id": "e6e9ad0c948411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MEFE(1).pdf", "type": "pdf", "location": "MEFE(1).pdf", "size": 5502142, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343396901, "task_type": "dataflow", "root_trace_id": "5667f9593fa8497eabc7fd15b6ab98c0", "root_traceparent": "00-5667f9593fa8497eabc7fd15b6ab98c0-4a2925d1ccf16074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:30:49,488 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:30:49,488 INFO     29 [qwen-vl-text] LLM output (len=572):
{
  "encounter_date": "2025-02-20",
  "chief_complaint": "支气管哮喘复诊。",
  "present_illness": "哮喘，患者来院进行D5982C00008项目V15随访。患者万托林已停用大于6h，昨晚完成白色吸入剂的吸入时间是21：40，昨晚完成红色吸入剂的吸入时间是21：43。今晨未吸入研究药物，规律吸入研究药物中，未出现多服及漏服现象。自上次访视至今，无不适，无新增合并用药，已和患者确认无其他门诊以及住院记录，无哮喘急性发作，已根据方案要求清洁吸入器装置。查看患者电子日志，日志偶有漏做现象，进行两次给药前肺功能测定。患者已空腹大于8小时，完成血样采集。患者自行完成ACQ6问卷，AQLQ+12问卷，EQ-5D-5L问卷，PGIC问卷，患者于今日09点26分完成白色吸入剂2喷，09点28分完成红色吸入剂2喷，患者已掌握给药方法。进行给药后15min肺功能检查，进行给药后30min肺功能检查，进行给药后1h肺功能检查，进行给药后2h肺功能检查，进行给药后3h肺功能检查。",
  "past_history": "有既往疾病史，鼻炎。",
  "diagnosis": "支气管哮喘",
  "treatment_plan": "信必可320ug bid 吸入"
}
2026-08-10 06:30:49,488 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-20]
2026-08-10 06:30:49,491 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1097038, prompt_len=1330
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共47行）
["徐州市中心医院", "门（急）诊病历", "姓名：", "性别：男", "科室：呼吸与危重症门诊", "号别：普通号", "姓名", "证件类型", "居民身份证", "性别", "男", "证件号码", "3:", "出生日期", "1992年07月11日", "门诊编号", "0005832911", "婚姻", "就诊时间", "2025-02-20 13:22", "陪伴者姓名", "初诊/复诊/急诊", "复诊", "陪伴者与患者的关系", "过敏史", "否认(病史提供人)", "联系人电话", "主诉：支气管哮喘复诊。", "病史：现病史：哮喘，患者来院进行D5982C00008项目V15随访", "既往史：有既往疾病史，鼻炎。", "体格检查：", "体温：(℃)，脉搏：次/分，血压：/(mmHg)，呼吸：次/分，意识状态：清醒", "皮肤粘膜：颜色正常，无皮疹，无皮下出血，无水肿。", "胸部：外形正常，无胸壁压痛。肺脏及胸膜：呼吸音正常，未闻及啰音，未触及胸", "膜摩擦音。", "心脏：心律齐，未闻及杂音，未闻及心包摩擦音，周围血管征阴性。", "腹部：外形正常，无压痛，无反跳痛。未触及包块。肝脏未触及。无肾区叩击痛，", "移动性浊音阴性，肠鸣音正常。", "神经反射：浅反射正常，深反射正常，病理反射阴性，脑膜刺激征阴性。", "诊断：支气管哮喘", "处理措施：", "根据方案要求，患者今日来院进行V15随访，患者于今日08点", "00分左右到院随访，与患者核实上次访视至今未进行过任何", "疫苗接种", "第（1）页", "WPS Office", "快拍即存·WPS拍照扫描"]

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
2026-08-10 06:31:04,055 INFO     29 [qwen-vl-text] coord API raw response (len=2647):
[
	{"text": "徐州市中心医院", "bbox": [391, 185, 633, 204]},
	{"text": "门（急）诊病历", "bbox": [441, 205, 589, 223]},
	{"text": "姓名：", "bbox": [287, 226, 334, 238]},
	{"text": "性别：男", "bbox": [392, 225, 437, 237]},
	{"text": "科室：呼吸与危重症门诊", "bbox": [464, 224, 592, 236]},
	{"text": "号别：普通号", "bbox": [621, 221, 691, 233]},
	{"text": "姓名", "bbox": [329, 250, 355, 261]},
	{"text": "证件类型", "bbox": [548, 248, 598, 260]},
	{"text": "居民身份证", "bbox": [655, 244, 720, 255]},
	{"text": "性别", "bbox": [329, 267, 355, 278]},
	{"text": "男", "bbox": [458, 267, 472, 278]},
	{"text": "证件号码", "bbox": [548, 265, 598, 277]},
	{"text": "3:", "bbox": [628, 265, 640, 276]},
	{"text": "出生日期", "bbox": [318, 284, 368, 295]},
	{"text": "1992年07月11日", "bbox": [423, 284, 507, 294]},
	{"text": "门诊编号", "bbox": [548, 282, 598, 294]},
	{"text": "0005832911", "bbox": [654, 280, 720, 291]},
	{"text": "婚姻", "bbox": [329, 301, 355, 312]},
	{"text": "就诊时间", "bbox": [548, 300, 598, 311]},
	{"text": "2025-02-20 13:22", "bbox": [635, 297, 741, 308]},
	{"text": "陪伴者姓名", "bbox": [311, 318, 374, 329]},
	{"text": "初诊/复诊/急诊", "bbox": [530, 317, 617, 328]},
	{"text": "复诊", "bbox": [675, 315, 701, 326]},
	{"text": "陪伴者与患者的关系", "bbox": [287, 336, 399, 347]},
	{"text": "过敏史", "bbox": [554, 335, 592, 346]},
	{"text": "否认(病史提供人)", "bbox": [636, 333, 740, 344]},
	{"text": "联系人电话", "bbox": [311, 353, 374, 364]},
	{"text": "主诉：支气管哮喘复诊。", "bbox": [286, 369, 414, 380]},
	{"text": "病史：现病史：哮喘，患者来院进行D5982C00008项目V15随访", "bbox": [290, 387, 619, 398]},
	{"text": "既往史：有既往疾病史，鼻炎。", "bbox": [327, 404, 495, 415]},
	{"text": "体格检查：", "bbox": [290, 421, 345, 432]},
	{"text": "体温：(℃)，脉搏：次/分，血压：/(mmHg)，呼吸：次/分，意识状态：清醒", "bbox": [285, 439, 648, 451]},
	{"text": "皮肤粘膜：颜色正常，无皮疹，无皮下出血，无水肿。", "bbox": [290, 456, 577, 468]},
	{"text": "胸部：外形正常，无胸壁压痛。肺脏及胸膜：呼吸音正常，未闻及啰音，未触及胸", "bbox": [289, 473, 747, 488]},
	{"text": "膜摩擦音。", "bbox": [284, 489, 339, 501]},
	{"text": "心脏：心律齐，未闻及杂音，未闻及心包摩擦音，周围血管征阴性。", "bbox": [290, 507, 654, 522]},
	{"text": "腹部：外形正常，无压痛，无反跳痛。未触及包块。肝脏未触及。无肾区叩击痛，", "bbox": [289, 525, 736, 543]},
	{"text": "移动性浊音阴性，肠鸣音正常。", "bbox": [284, 542, 449, 556]},
	{"text": "神经反射：浅反射正常，深反射正常，病理反射阴性，脑膜刺激征阴性。", "bbox": [289, 559, 682, 580]},
	{"text": "诊断：支气管哮喘", "bbox": [289, 577, 412, 590]},
	{"text": "处理措施：", "bbox": [289, 595, 343, 607]},
	{"text": "根据方案要求，患者今日来院进行V15随访，患者于今日08点", "bbox": [353, 614, 752, 643]},
	{"text": "00分左右到院随访，与患者核实上次访视至今未进行过任何", "bbox": [352, 632, 752, 662]],
	{"text": "疫苗接种", "bbox": [352, 651, 411, 665]},
	{"text": "第（1）页", "bbox": [464, 694, 554, 711]},
	{"text": "WPS Office", "bbox": [604, 905, 817, 928]},
	{"text": "快拍即存·WPS拍照扫描", "bbox": [535, 940, 816, 958]}
]
2026-08-10 06:31:04,055 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord API: raw_items=47, valid_items=47, elapsed=14.6s
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[0]: text=徐州市中心医院, bbox=[391, 185, 633, 204]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[1]: text=门（急）诊病历, bbox=[441, 205, 589, 223]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[287, 226, 334, 238]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[392, 225, 437, 237]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重症门诊, bbox=[464, 224, 592, 236]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[5]: text=号别：普通号, bbox=[621, 221, 691, 233]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[6]: text=姓名, bbox=[329, 250, 355, 261]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[7]: text=证件类型, bbox=[548, 248, 598, 260]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[8]: text=居民身份证, bbox=[655, 244, 720, 255]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[9]: text=性别, bbox=[329, 267, 355, 278]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[10]: text=男, bbox=[458, 267, 472, 278]
2026-08-10 06:31:04,056 INFO     29 [qwen-vl-text] coord item[11]: text=证件号码, bbox=[548, 265, 598, 277]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[12]: text=3:, bbox=[628, 265, 640, 276]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[13]: text=出生日期, bbox=[318, 284, 368, 295]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[14]: text=1992年07月11日, bbox=[423, 284, 507, 294]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[15]: text=门诊编号, bbox=[548, 282, 598, 294]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[16]: text=0005832911, bbox=[654, 280, 720, 291]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[17]: text=婚姻, bbox=[329, 301, 355, 312]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[18]: text=就诊时间, bbox=[548, 300, 598, 311]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[19]: text=2025-02-20 13:22, bbox=[635, 297, 741, 308]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[20]: text=陪伴者姓名, bbox=[311, 318, 374, 329]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[21]: text=初诊/复诊/急诊, bbox=[530, 317, 617, 328]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[22]: text=复诊, bbox=[675, 315, 701, 326]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[23]: text=陪伴者与患者的关系, bbox=[287, 336, 399, 347]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[24]: text=过敏史, bbox=[554, 335, 592, 346]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[25]: text=否认(病史提供人), bbox=[636, 333, 740, 344]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[26]: text=联系人电话, bbox=[311, 353, 374, 364]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[27]: text=主诉：支气管哮喘复诊。, bbox=[286, 369, 414, 380]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[28]: text=病史：现病史：哮喘，患者来院进行D5982C00008项目V15随访, bbox=[290, 387, 619, 398]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[29]: text=既往史：有既往疾病史，鼻炎。, bbox=[327, 404, 495, 415]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[30]: text=体格检查：, bbox=[290, 421, 345, 432]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[31]: text=体温：(℃)，脉搏：次/分，血压：/(mmHg)，呼吸：次/分，意识状态：清醒, bbox=[285, 439, 648, 451]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[32]: text=皮肤粘膜：颜色正常，无皮疹，无皮下出血，无水肿。, bbox=[290, 456, 577, 468]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[33]: text=胸部：外形正常，无胸壁压痛。肺脏及胸膜：呼吸音正常，未闻及啰音，未触及胸, bbox=[289, 473, 747, 488]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[34]: text=膜摩擦音。, bbox=[284, 489, 339, 501]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[35]: text=心脏：心律齐，未闻及杂音，未闻及心包摩擦音，周围血管征阴性。, bbox=[290, 507, 654, 522]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[36]: text=腹部：外形正常，无压痛，无反跳痛。未触及包块。肝脏未触及。无肾区叩击痛，, bbox=[289, 525, 736, 543]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[37]: text=移动性浊音阴性，肠鸣音正常。, bbox=[284, 542, 449, 556]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[38]: text=神经反射：浅反射正常，深反射正常，病理反射阴性，脑膜刺激征阴性。, bbox=[289, 559, 682, 580]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[39]: text=诊断：支气管哮喘, bbox=[289, 577, 412, 590]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[40]: text=处理措施：, bbox=[289, 595, 343, 607]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[41]: text=根据方案要求，患者今日来院进行V15随访，患者于今日08点, bbox=[353, 614, 752, 643]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[42]: text=00分左右到院随访，与患者核实上次访视至今未进行过任何, bbox=[352, 632, 752, 662]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[43]: text=疫苗接种, bbox=[352, 651, 411, 665]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[44]: text=第（1）页, bbox=[464, 694, 554, 711]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[45]: text=WPS Office, bbox=[604, 905, 817, 928]
2026-08-10 06:31:04,057 INFO     29 [qwen-vl-text] coord item[46]: text=快拍即存·WPS拍照扫描, bbox=[535, 940, 816, 958]
2026-08-10 06:31:04,058 INFO     29 [qwen-vl-text] page=1 — 47/47 coords, api_time=14.6s
2026-08-10 06:31:04,059 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1101412, prompt_len=1276
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["徐州市中心医院", "门（急）诊病历", "姓名", "性别：男", "科室：呼吸与危重症门诊", "号别：普通号", "患者万托林已停用大于6h，昨晚完成白色吸入剂的吸入时间是21：40，", "昨晚完成红色吸入剂的吸入时间是21：43。今晨未吸入研究药物，规律", "吸入研究药物中，未出现多服及漏服现象", "自上次访视至今，无不适，无新增合并用药，已和患者确认无其他门诊", "以及住院记录，无哮喘急性发作，已根据方案要求清洁吸入器装置", "查看患者电子日志，日志偶有漏做现象，进行两次给药前肺功能测定", "患者已空腹大于8小时，完成血样采集", "患者自行完成ACQ6问卷，AQLQ+12问卷，EQ-5D-5L问卷，PGIC问卷，患者", "于今日09点26分完成白色吸入剂2喷，09点28分完成红色吸入剂2喷，患", "者已掌握给药方法。进行给药后15min肺功能检查，进行给药后30min肺", "功能检查，进行给药后1h肺功能检查，进行给药后2h肺功能检查，进行", "给药后3h肺功能检查", "告知患者今日已完成试验，嘱后续治疗方案为信必可320ug bid 吸入，", "今日登记IRT系统进行完成试验登记，回收相关设备和药物。", "是否留观：否", "特别提醒：根据《传染病防治法》《治安管理处罚法》等法律规定，如果您隐", "瞒上述情况或者拒绝配合医务人员开展调查等处置措施的，将承担相应的法律责任。", "承诺以上情况均属实。", "医师签名：张敏浩", "患者签名：", "第（2）页"]

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
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord API raw response (len=1773):
[
	{"text": "徐州市中心医院", "bbox": [379, 225, 612, 245]},
	{"text": "门（急）诊病历", "bbox": [427, 244, 568, 261]},
	{"text": "姓名", "bbox": [278, 263, 302, 273]},
	{"text": "性别：男", "bbox": [380, 263, 421, 273]},
	{"text": "科室：呼吸与危重症门诊", "bbox": [449, 261, 570, 272]},
	{"text": "号别：普通号", "bbox": [600, 258, 667, 269]},
	{"text": "患者万托林已停用大于6h，昨晚完成白色吸入剂的吸入时间是21：40，", "bbox": [276, 281, 707, 297]},
	{"text": "昨晚完成红色吸入剂的吸入时间是21：43。今晨未吸入研究药物，规律", "bbox": [276, 298, 716, 313]},
	{"text": "吸入研究药物中，未出现多服及漏服现象", "bbox": [276, 318, 519, 331]},
	{"text": "自上次访视至今，无不适，无新增合并用药，已和患者确认无其他门诊", "bbox": [276, 333, 716, 348]},
	{"text": "以及住院记录，无哮喘急性发作，已根据方案要求清洁吸入器装置", "bbox": [276, 350, 675, 364]},
	{"text": "查看患者电子日志，日志偶有漏做现象，进行两次给药前肺功能测定", "bbox": [276, 367, 690, 380]},
	{"text": "患者已空腹大于8小时，完成血样采集", "bbox": [274, 384, 498, 397]},
	{"text": "患者自行完成ACQ6问卷，AQLQ+12问卷，EQ-5D-5L问卷，PGIC问卷，患者", "bbox": [274, 400, 716, 414]},
	{"text": "于今日09点26分完成白色吸入剂2喷，09点28分完成红色吸入剂2喷，患", "bbox": [274, 417, 716, 430]},
	{"text": "者已掌握给药方法。进行给药后15min肺功能检查，进行给药后30min肺", "bbox": [274, 433, 716, 447]},
	{"text": "功能检查，进行给药后1h肺功能检查，进行给药后2h肺功能检查，进行", "bbox": [272, 450, 716, 464]},
	{"text": "给药后3h肺功能检查", "bbox": [270, 466, 395, 479]},
	{"text": "告知患者今日已完成试验，嘱后续治疗方案为信必可320ug bid 吸入，", "bbox": [270, 483, 709, 500]},
	{"text": "今日登记IRT系统进行完成试验登记，回收相关设备和药物。", "bbox": [270, 500, 629, 516]},
	{"text": "是否留观：否", "bbox": [274, 517, 346, 528]},
	{"text": "特别提醒：根据《传染病防治法》《治安管理处罚法》等法律规定，如果您隐", "bbox": [296, 534, 718, 555]},
	{"text": "瞒上述情况或者拒绝配合医务人员开展调查等处置措施的，将承担相应的法律责任。", "bbox": [268, 550, 709, 572]},
	{"text": "承诺以上情况均属实。", "bbox": [290, 568, 404, 580]},
	{"text": "医师签名：张敏浩", "bbox": [290, 586, 385, 598]},
	{"text": "患者签名：", "bbox": [516, 592, 569, 604]},
	{"text": "第（2）页", "bbox": [440, 715, 527, 730]}
]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=10.5s
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[0]: text=徐州市中心医院, bbox=[379, 225, 612, 245]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[1]: text=门（急）诊病历, bbox=[427, 244, 568, 261]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[278, 263, 302, 273]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[380, 263, 421, 273]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重症门诊, bbox=[449, 261, 570, 272]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[5]: text=号别：普通号, bbox=[600, 258, 667, 269]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[6]: text=患者万托林已停用大于6h，昨晚完成白色吸入剂的吸入时间是21：40，, bbox=[276, 281, 707, 297]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[7]: text=昨晚完成红色吸入剂的吸入时间是21：43。今晨未吸入研究药物，规律, bbox=[276, 298, 716, 313]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[8]: text=吸入研究药物中，未出现多服及漏服现象, bbox=[276, 318, 519, 331]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[9]: text=自上次访视至今，无不适，无新增合并用药，已和患者确认无其他门诊, bbox=[276, 333, 716, 348]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[10]: text=以及住院记录，无哮喘急性发作，已根据方案要求清洁吸入器装置, bbox=[276, 350, 675, 364]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[11]: text=查看患者电子日志，日志偶有漏做现象，进行两次给药前肺功能测定, bbox=[276, 367, 690, 380]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[12]: text=患者已空腹大于8小时，完成血样采集, bbox=[274, 384, 498, 397]
2026-08-10 06:31:14,580 INFO     29 [qwen-vl-text] coord item[13]: text=患者自行完成ACQ6问卷，AQLQ+12问卷，EQ-5D-5L问卷，PGIC问卷，患者, bbox=[274, 400, 716, 414]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[14]: text=于今日09点26分完成白色吸入剂2喷，09点28分完成红色吸入剂2喷，患, bbox=[274, 417, 716, 430]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[15]: text=者已掌握给药方法。进行给药后15min肺功能检查，进行给药后30min肺, bbox=[274, 433, 716, 447]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[16]: text=功能检查，进行给药后1h肺功能检查，进行给药后2h肺功能检查，进行, bbox=[272, 450, 716, 464]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[17]: text=给药后3h肺功能检查, bbox=[270, 466, 395, 479]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[18]: text=告知患者今日已完成试验，嘱后续治疗方案为信必可320ug bid 吸入，, bbox=[270, 483, 709, 500]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[19]: text=今日登记IRT系统进行完成试验登记，回收相关设备和药物。, bbox=[270, 500, 629, 516]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[20]: text=是否留观：否, bbox=[274, 517, 346, 528]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[21]: text=特别提醒：根据《传染病防治法》《治安管理处罚法》等法律规定，如果您隐, bbox=[296, 534, 718, 555]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[22]: text=瞒上述情况或者拒绝配合医务人员开展调查等处置措施的，将承担相应的法律责任。, bbox=[268, 550, 709, 572]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[23]: text=承诺以上情况均属实。, bbox=[290, 568, 404, 580]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[24]: text=医师签名：张敏浩, bbox=[290, 586, 385, 598]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[25]: text=患者签名：, bbox=[516, 592, 569, 604]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] coord item[26]: text=第（2）页, bbox=[440, 715, 527, 730]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] page=2 — 27/27 coords, api_time=10.5s
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] new_positions (74):
[[1, 232.75291638183595, 376.80970861816405, 155.74965270996094, 171.74556298828125], [1, 262.5167164306641, 350.61756457519533, 172.5874530029297, 187.74147326660156], [1, 170.84421228027344, 198.82218432617188, 190.26714331054689, 200.36982348632813], [1, 233.3481923828125, 260.1356124267578, 189.42525329589844, 199.5279334716797], [1, 276.208064453125, 352.403392578125, 188.58336328125, 198.68604345703125], [1, 369.66639660644535, 411.3357166748047, 186.05769323730468, 196.16037341308595], [1, 195.84580432128908, 211.32298034667969, 210.47250366210938, 219.73329382324218], [1, 326.21124853515624, 355.9750485839844, 208.7887236328125, 218.89140380859374], [1, 389.90578063964847, 428.598720703125, 205.42116357421875, 214.68195373535156], [1, 195.84580432128908, 211.32298034667969, 224.7846339111328, 234.04542407226563], [1, 272.63640844726564, 280.9702724609375, 224.7846339111328, 234.04542407226563], [1, 326.21124853515624, 355.9750485839844, 223.10085388183595, 233.2035340576172], [1, 373.83332861328125, 380.976640625, 223.10085388183595, 232.36164404296875], [1, 189.29776831054687, 219.061568359375, 239.09676416015625, 248.35755432128906], [1, 251.80174841308596, 301.8049324951172, 239.09676416015625, 247.51566430664062], [1, 326.21124853515624, 355.9750485839844, 237.41298413085937, 247.51566430664062], [1, 389.3105046386719, 428.598720703125, 235.7292041015625, 244.98999426269532], [1, 195.84580432128908, 211.32298034667969, 253.40889440917968, 262.6696845703125], [1, 326.21124853515624, 355.9750485839844, 252.56700439453124, 261.82779455566407], [1, 378.0002606201172, 441.0995167236328, 250.04133435058594, 259.3021245117188], [1, 185.13083630371094, 222.63322436523438, 267.72102465820313, 276.9818148193359], [1, 315.49628051757816, 367.2852926025391, 266.87913464355466, 276.1399248046875], [1, 401.8113006591797, 417.28847668457036, 265.19535461425784, 274.4561447753906], [1, 170.84421228027344, 237.51512438964843, 282.875044921875, 292.1358350830078], [1, 329.7829045410156, 352.403392578125, 282.03315490722656, 291.2939450683594], [1, 378.59553662109374, 440.5042407226563, 280.3493748779297, 289.6101650390625], [1, 185.13083630371094, 222.63322436523438, 297.18717517089846, 306.44796533203123], [1, 170.24893627929688, 246.4442644042969, 310.6574154052734, 319.91820556640624], [1, 172.63004028320313, 368.4758446044922, 325.8114356689453, 335.07222583007814], [1, 194.65525231933594, 294.66162048339845, 340.12356591796873, 349.38435607910156], [1, 172.63004028320313, 205.37022033691406, 354.43569616699216, 363.696486328125], [1, 169.65366027832033, 385.7388486328125, 369.58971643066405, 379.6923966064453], [1, 172.63004028320313, 343.47425256347657, 383.9018466796875, 394.0045268554687], [1, 172.03476428222658, 444.6711727294922, 398.2139769287109, 410.8423271484375], [1, 169.05838427734375, 201.7985643310547, 411.6842171630859, 421.78689733886716], [1, 172.63004028320313, 389.3105046386719, 426.8382374267578, 439.46658764648436], [1, 172.03476428222658, 438.12313671875, 441.9922576904297, 457.14627795410155], [1, 169.05838427734375, 267.27892443847657, 456.30438793945314, 468.09084814453126], [1, 172.03476428222658, 405.97823266601563, 470.61651818847656, 488.29620849609375], [1, 172.03476428222658, 245.25371240234375, 485.77053845214846, 496.7151086425781], [1, 172.03476428222658, 204.17966833496095, 500.9245587158203, 511.02723889160154], [1, 210.13242834472658, 447.64755273437504, 516.9204689941406, 541.3352794189453], [1, 209.53715234375, 447.64755273437504, 532.0744892578125, 557.3311896972656], [1, 209.53715234375, 244.6584364013672, 548.0703995361328, 559.8568597412109], [1, 276.208064453125, 329.7829045410156, 584.2716701660156, 598.583800415039], [1, 359.5467045898438, 486.3404927978516, 761.9104632568359, 781.27393359375], [1, 318.47266052246096, 485.745216796875, 791.3766137695312, 806.5306340332031], [2, 225.6096043701172, 364.3089125976563, 189.42525329589844, 206.2630535888672], [2, 254.1828524169922, 338.1167685546875, 205.42116357421875, 219.73329382324218], [2, 165.4867282714844, 179.7733522949219, 221.41707385253906, 229.83597399902342], [2, 226.20488037109376, 250.61119641113282, 221.41707385253906, 229.83597399902342], [2, 267.27892443847657, 339.30732055664066, 219.73329382324218, 228.994083984375], [2, 357.1656005859375, 397.04909265136723, 217.20762377929688, 226.46841394042968], [2, 164.29617626953126, 420.8601326904297, 236.57109411621093, 250.04133435058594], [2, 164.29617626953126, 426.21761669921875, 250.88322436523438, 263.51157458496095], [2, 164.29617626953126, 308.948244506836, 267.72102465820313, 278.6655948486328], [2, 164.29617626953126, 426.21761669921875, 280.3493748779297, 292.9777250976562], [2, 164.29617626953126, 401.8113006591797, 294.6615051269531, 306.44796533203123], [2, 164.29617626953126, 410.7404406738281, 308.9736353759766, 319.91820556640624], [2, 163.10562426757812, 296.44744848632814, 323.285765625, 334.23033581542967], [2, 163.10562426757812, 426.21761669921875, 336.756005859375, 348.5424660644531], [2, 163.10562426757812, 426.21761669921875, 351.06813610839845, 362.0127062988281], [2, 163.10562426757812, 426.21761669921875, 364.53837634277346, 376.32483654785153], [2, 161.915072265625, 426.21761669921875, 378.8505065917969, 390.636966796875], [2, 160.72452026367188, 235.1340203857422, 392.3207468261719, 403.26531701660156], [2, 160.72452026367188, 422.05068469238284, 406.6328770751953, 420.94500732421875], [2, 160.72452026367188, 374.42860461425784, 420.94500732421875, 434.41524755859376], [2, 163.10562426757812, 205.96549633789064, 435.2571375732422, 444.517927734375], [2, 176.2016962890625, 427.4081687011719, 449.5692678222656, 467.2489581298828], [2, 159.53396826171877, 422.05068469238284, 463.0395080566406, 481.5610883789062], [2, 172.63004028320313, 240.49150439453126, 478.1935283203125, 488.29620849609375], [2, 172.63004028320313, 229.18126037597656, 493.34754858398435, 503.4502287597656], [2, 307.1624165039063, 338.7120445556641, 498.398888671875, 508.50156884765624], [2, 261.9214404296875, 313.71045251464847, 601.9513604736328, 614.5797106933594]]
2026-08-10 06:31:14,581 INFO     29 [qwen-vl-text] ═══ DONE ═══ 74 positions, pages=2, time=29.2s
2026-08-10 06:31:14,595 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 06:31:14,595 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:31:14,595 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 06:31:14,605 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:14,605 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:31:16,778 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:16,790 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 06:31:16,790 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:31:16,790 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 06:31:16,799 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:16,800 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:31:17,291 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:17,303 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 06:31:17,303 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:31:17,303 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 06:31:17,315 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:17,315 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:31:17,775 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:17,794 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 06:31:17,794 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:31:17,794 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 06:31:17,803 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:17,803 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:31:17,889 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:31:17.888+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 6, "failed": 0, "current": {"e7b1979a948411f1bd9827cf206dfa2d": {"id": "e7b1979a948411f1bd9827cf206dfa2d", "doc_id": "e6e9ad0c948411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MEFE(1).pdf", "type": "pdf", "location": "MEFE(1).pdf", "size": 5502142, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343396901, "task_type": "dataflow", "root_trace_id": "5667f9593fa8497eabc7fd15b6ab98c0", "root_traceparent": "00-5667f9593fa8497eabc7fd15b6ab98c0-4a2925d1ccf16074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:31:18,632 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:18,643 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 06:31:18,643 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:31:18,644 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 06:31:18,654 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:31:18,655 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:31:18,655 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:31:18,655 INFO     29 [qwen-vl-text] positions(136): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:31:18,655 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [136]
2026-08-10 06:31:19,077 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 06:31:19,078 INFO     29 [qwen-vl-text] LLM extraction start, text_len=794
2026-08-10 06:31:19,078 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:19,078 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 135, \"encounter_dates\": [\"2025-05-28\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "JAEGER TOENNIES\n徐州市中心医院\n东南大学医学院附属徐州医院\n肺功能检查报告\n姓名：\n门诊/住院号：5832\n身高：178 cm\n年龄：32 Years\n性别：男\n测试号：2025051412\n体重：68 kg\n科别：呼吸与危重症医学科\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n1\n2\n10\nF/V in\n日期\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n时间\n25/5/28\n25/5/28\n9:33:12\n10:00:0\nVC MAX\n[L]\n5.31\n4.00\n75.3\n4.63\n87.1\n15.62\nERV\n[L]\n1.56\nIC\n[L]\n3.75\nFVC\n[L]\n5.08\n4.00\n78.7\n4.62\n91.0\n15.55\nFEV 1\n[L]\n4.24\n2.51\n59.2\n3.07\n72.5\n22.53\nFEV 1 % FVC\n[%]\n82.49\n62.65\n75.9\n66.43\n80.5\n6.05\nFEV 1 % VC MAX\n[%]\n81.45\n62.65\n76.9\n66.39\n81.5\n5.98\nPEF\n[L/s]\n9.70\n7.10\n73.1\n9.89\n101.9\n39.28\nMEF 75\n[L/s]\n8.32\n3.64\n43.8\n5.40\n64.8\n48.11\nMEF 50\n[L/s]\n5.40\n1.57\n29.1\n2.29\n42.4\n45.60\nMEF 25\n[L/s]\n2.47\n0.49\n19.7\n0.69\n28.1\n42.74\nMMEF 75/25\n[L/s]\n4.78\n1.24\n26.0\n1.72\n36.0\n38.55\nV backextrapol. % FVC\n[%]\n2.29\n2.55\n11.69\n结论：\n支气管舒张试验阳性\n医生签字：\nWPS Office\n快拍即存·WPS拍照扫描",
    "role": "user"
  }
]
2026-08-10 06:31:43,078 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:31:43,078 INFO     29 [qwen-vl-text] LLM output (len=1229):
{
  "exam_date": "2025-05-28",
  "report_date": "2025-05-28",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸与危重症医学科",
  "bed_number": null,
  "findings": "日期: 25/5/28\n预计值: 25/5/28\n前次: 9:33:12\n前/预: 10:00:0\n后次: \n后/预: \n改善率: \n时间: \n\n| 指标 | 预计值 | 前次 | 前/预 | 后次 | 后/预 | 改善率 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| VC MAX [L] | 5.31 | 4.00 | 75.3 | 4.63 | 87.1 | 15.62 |\n| ERV [L] | 1.56 | | | | | |\n| IC [L] | 3.75 | | | | | |\n| FVC [L] | 5.08 | 4.00 | 78.7 | 4.62 | 91.0 | 15.55 |\n| FEV 1 [L] | 4.24 | 2.51 | 59.2 | 3.07 | 72.5 | 22.53 |\n| FEV 1 % FVC [%] | 82.49 | 62.65 | 75.9 | 66.43 | 80.5 | 6.05 |\n| FEV 1 % VC MAX [%] | 81.45 | 62.65 | 76.9 | 66.39 | 81.5 | 5.98 |\n| PEF [L/s] | 9.70 | 7.10 | 73.1 | 9.89 | 101.9 | 39.28 |\n| MEF 75 [L/s] | 8.32 | 3.64 | 43.8 | 5.40 | 64.8 | 48.11 |\n| MEF 50 [L/s] | 5.40 | 1.57 | 29.1 | 2.29 | 42.4 | 45.60 |\n| MEF 25 [L/s] | 2.47 | 0.49 | 19.7 | 0.69 | 28.1 | 42.74 |\n| MMEF 75/25 [L/s] | 4.78 | 1.24 | 26.0 | 1.72 | 36.0 | 38.55 |\n| V backextrapol. % FVC [%] | 2.29 | 2.55 | 11.69 | | | |",
  "conclusion": "支气管舒张试验阳性",
  "physician": null,
  "reviewer": null
}
2026-08-10 06:31:43,090 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2902201, prompt_len=1816
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共136行）
["JAEGER TOENNIES", "徐州市中心医院", "东南大学医学院附属徐州医院", "肺功能检查报告", "姓名：", "门诊/住院号：5832", "身高：178 cm", "年龄：32 Years", "性别：男", "测试号：2025051412", "体重：68 kg", "科别：呼吸与危重症医学科", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "1", "2", "10", "F/V in", "日期", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "时间", "25/5/28", "25/5/28", "9:33:12", "10:00:0", "VC MAX", "[L]", "5.31", "4.00", "75.3", "4.63", "87.1", "15.62", "ERV", "[L]", "1.56", "IC", "[L]", "3.75", "FVC", "[L]", "5.08", "4.00", "78.7", "4.62", "91.0", "15.55", "FEV 1", "[L]", "4.24", "2.51", "59.2", "3.07", "72.5", "22.53", "FEV 1 % FVC", "[%]", "82.49", "62.65", "75.9", "66.43", "80.5", "6.05", "FEV 1 % VC MAX", "[%]", "81.45", "62.65", "76.9", "66.39", "81.5", "5.98", "PEF", "[L/s]", "9.70", "7.10", "73.1", "9.89", "101.9", "39.28", "MEF 75", "[L/s]", "8.32", "3.64", "43.8", "5.40", "64.8", "48.11", "MEF 50", "[L/s]", "5.40", "1.57", "29.1", "2.29", "42.4", "45.60", "MEF 25", "[L/s]", "2.47", "0.49", "19.7", "0.69", "28.1", "42.74", "MMEF 75/25", "[L/s]", "4.78", "1.24", "26.0", "1.72", "36.0", "38.55", "V backextrapol. % FVC", "[%]", "2.29", "2.55", "11.69", "结论：", "支气管舒张试验阳性", "医生签字：", "WPS Office", "快拍即存·WPS拍照扫描"]

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
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord API raw response (len=7141):
[
	{"text": "JAEGER TOENNIES", "bbox": [577, 97, 716, 108]},
	{"text": "徐州市中心医院", "bbox": [310, 112, 560, 127]},
	{"text": "东南大学医学院附属徐州医院", "bbox": [307, 127, 564, 141]},
	{"text": "肺功能检查报告", "bbox": [374, 145, 495, 158]},
	{"text": "姓名：", "bbox": [161, 167, 197, 177]},
	{"text": "门诊/住院号：", "bbox": [161, 176, 249, 186]},
	{"text": "5832", "bbox": [295, 177, 348, 186]},
	{"text": "身高：", "bbox": [161, 185, 197, 194]},
	{"text": "178 cm", "bbox": [295, 186, 342, 194]},
	{"text": "年龄：", "bbox": [161, 194, 197, 203]},
	{"text": "32 Years", "bbox": [295, 195, 355, 203]},
	{"text": "性别：", "bbox": [437, 167, 473, 177]},
	{"text": "男", "bbox": [570, 168, 583, 177]},
	{"text": "测试号：", "bbox": [437, 176, 488, 186]},
	{"text": "2025051412", "bbox": [570, 178, 642, 186]},
	{"text": "体重：", "bbox": [437, 185, 473, 194]},
	{"text": "68 kg", "bbox": [570, 187, 607, 195]},
	{"text": "科别：", "bbox": [437, 194, 473, 203]},
	{"text": "呼吸与危重症医学科", "bbox": [570, 195, 700, 204]},
	{"text": "Flow [L/s]", "bbox": [293, 219, 335, 227]},
	{"text": "F/V ex", "bbox": [480, 220, 507, 227]},
	{"text": "10", "bbox": [275, 232, 286, 239]},
	{"text": "5", "bbox": [279, 252, 286, 259]},
	{"text": "0", "bbox": [279, 271, 286, 278]},
	{"text": "1", "bbox": [325, 279, 332, 286]},
	{"text": "2", "bbox": [364, 279, 371, 286]},
	{"text": "3", "bbox": [403, 279, 409, 286]},
	{"text": "4", "bbox": [441, 279, 448, 286]},
	{"text": "5", "bbox": [478, 279, 485, 286]},
	{"text": "6", "bbox": [516, 279, 523, 286]},
	{"text": "7", "bbox": [553, 279, 560, 286]},
	{"text": "1", "bbox": [575, 268, 598, 276]},
	{"text": "2", "bbox": [575, 276, 598, 284]},
	{"text": "5", "bbox": [279, 292, 286, 300]},
	{"text": "10", "bbox": [275, 313, 286, 320]},
	{"text": "F/V in", "bbox": [482, 326, 507, 334]},
	{"text": "日期", "bbox": [151, 353, 182, 363]},
	{"text": "预计值", "bbox": [368, 343, 415, 353]},
	{"text": "前次", "bbox": [445, 343, 476, 353]},
	{"text": "前/预", "bbox": [497, 343, 534, 353]},
	{"text": "后次", "bbox": [563, 343, 594, 353]},
	{"text": "后/预", "bbox": [616, 343, 655, 353]},
	{"text": "改善率", "bbox": [667, 343, 713, 353]},
	{"text": "时间", "bbox": [151, 363, 182, 372]},
	{"text": "25/5/28", "bbox": [422, 355, 475, 363]},
	{"text": "25/5/28", "bbox": [542, 355, 594, 363]},
	{"text": "9:33:12", "bbox": [422, 364, 475, 372]},
	{"text": "10:00:0", "bbox": [542, 364, 594, 372]},
	{"text": "VC MAX", "bbox": [150, 384, 197, 392]},
	{"text": "[L]", "bbox": [332, 384, 352, 393]},
	{"text": "5.31", "bbox": [384, 384, 415, 392]},
	{"text": "4.00", "bbox": [445, 384, 476, 392]},
	{"text": "75.3", "bbox": [506, 384, 536, 392]},
	{"text": "4.63", "bbox": [564, 384, 594, 392]},
	{"text": "87.1", "bbox": [624, 384, 655, 392]},
	{"text": "15.62", "bbox": [678, 384, 715, 392]},
	{"text": "ERV", "bbox": [150, 394, 174, 402]},
	{"text": "[L]", "bbox": [332, 394, 352, 403]},
	{"text": "1.56", "bbox": [384, 394, 415, 402]},
	{"text": "IC", "bbox": [150, 404, 166, 412]},
	{"text": "[L]", "bbox": [332, 404, 352, 413]},
	{"text": "3.75", "bbox": [384, 404, 415, 412]},
	{"text": "FVC", "bbox": [150, 424, 172, 432]},
	{"text": "[L]", "bbox": [332, 424, 352, 433]},
	{"text": "5.08", "bbox": [384, 424, 415, 432]},
	{"text": "4.00", "bbox": [445, 424, 476, 432]},
	{"text": "78.7", "bbox": [506, 424, 536, 432]},
	{"text": "4.62", "bbox": [564, 424, 594, 432]},
	{"text": "91.0", "bbox": [626, 424, 657, 432]},
	{"text": "15.55", "bbox": [680, 424, 717, 432]},
	{"text": "FEV 1", "bbox": [150, 435, 185, 443]},
	{"text": "[L]", "bbox": [332, 435, 352, 444]},
	{"text": "4.24", "bbox": [384, 435, 415, 443]},
	{"text": "2.51", "bbox": [445, 435, 476, 443]},
	{"text": "59.2", "bbox": [506, 435, 536, 443]},
	{"text": "3.07", "bbox": [564, 435, 594, 443]},
	{"text": "72.5", "bbox": [626, 435, 657, 443]},
	{"text": "22.53", "bbox": [680, 435, 717, 443]},
	{"text": "FEV 1 % FVC", "bbox": [150, 445, 234, 453]},
	{"text": "[%]", "bbox": [332, 445, 352, 454]},
	{"text": "82.49", "bbox": [377, 445, 415, 453]},
	{"text": "62.65", "bbox": [440, 445, 476, 453]},
	{"text": "75.9", "bbox": [506, 445, 536, 453]},
	{"text": "66.43", "bbox": [558, 445, 596, 453]},
	{"text": "80.5", "bbox": [626, 445, 657, 453]},
	{"text": "6.05", "bbox": [689, 445, 717, 453]},
	{"text": "FEV 1 % VC MAX", "bbox": [150, 455, 258, 463]},
	{"text": "[%]", "bbox": [332, 455, 352, 464]},
	{"text": "81.45", "bbox": [377, 455, 415, 463]},
	{"text": "62.65", "bbox": [440, 455, 476, 463]},
	{"text": "76.9", "bbox": [506, 455, 536, 463]},
	{"text": "66.39", "bbox": [558, 455, 596, 463]},
	{"text": "81.5", "bbox": [626, 455, 657, 463]},
	{"text": "5.98", "bbox": [689, 455, 717, 463]},
	{"text": "PEF", "bbox": [147, 466, 170, 474]},
	{"text": "[L/s]", "bbox": [315, 466, 352, 475]},
	{"text": "9.70", "bbox": [384, 466, 415, 474]},
	{"text": "7.10", "bbox": [445, 466, 476, 474]},
	{"text": "73.1", "bbox": [506, 466, 536, 474]},
	{"text": "9.89", "bbox": [564, 466, 594, 474]},
	{"text": "101.9", "bbox": [620, 466, 657, 474]},
	{"text": "39.28", "bbox": [682, 466, 717, 474]},
	{"text": "MEF 75", "bbox": [145, 476, 193, 484]},
	{"text": "[L/s]", "bbox": [315, 476, 352, 485]},
	{"text": "8.32", "bbox": [384, 476, 415, 484]},
	{"text": "3.64", "bbox": [445, 476, 476, 484]},
	{"text": "43.8", "bbox": [506, 476, 536, 484]},
	{"text": "5.40", "bbox": [564, 476, 594, 484]},
	{"text": "64.8", "bbox": [626, 476, 657, 484]},
	{"text": "48.11", "bbox": [682, 476, 717, 484]},
	{"text": "MEF 50", "bbox": [145, 487, 193, 495]},
	{"text": "[L/s]", "bbox": [315, 487, 352, 496]},
	{"text": "5.40", "bbox": [384, 487, 415, 495]},
	{"text": "1.57", "bbox": [445, 487, 476, 495]},
	{"text": "29.1", "bbox": [506, 487, 536, 495]},
	{"text": "2.29", "bbox": [564, 487, 594, 495]},
	{"text": "42.4", "bbox": [626, 487, 657, 495]},
	{"text": "45.60", "bbox": [682, 487, 717, 495]},
	{"text": "MEF 25", "bbox": [145, 497, 193, 505]},
	{"text": "[L/s]", "bbox": [315, 497, 352, 506]},
	{"text": "2.47", "bbox": [384, 497, 415, 505]},
	{"text": "0.49", "bbox": [445, 497, 476, 505]},
	{"text": "19.7", "bbox": [506, 497, 536, 505]},
	{"text": "0.69", "bbox": [564, 497, 594, 505]},
	{"text": "28.1", "bbox": [626, 497, 657, 505]},
	{"text": "42.74", "bbox": [682, 497, 717, 505]},
	{"text": "MMEF 75/25", "bbox": [145, 507, 223, 515]},
	{"text": "[L/s]", "bbox": [315, 507, 352, 516]},
	{"text": "4.78", "bbox": [384, 507, 415, 515]},
	{"text": "1.24", "bbox": [445, 507, 476, 515]},
	{"text": "26.0", "bbox": [506, 507, 536, 515]},
	{"text": "1.72", "bbox": [564, 507, 594, 515]},
	{"text": "36.0", "bbox": [626, 507, 657, 515]},
	{"text": "38.55", "bbox": [682, 507, 717, 515]},
	{"text": "V backextrapol. % FVC", "bbox": [145, 517, 313, 525]},
	{"text": "[%]", "bbox": [330, 517, 351, 526]},
	{"text": "2.29", "bbox": [445, 517, 476, 525]},
	{"text": "2.55", "bbox": [564, 517, 594, 525]},
	{"text": "11.69", "bbox": [682, 517, 717, 525]},
	{"text": "结论：", "bbox": [161, 555, 206, 568]},
	{"text": "支气管舒张试验阳性", "bbox": [210, 580, 384, 593]},
	{"text": "医生签字：", "bbox": [579, 666, 661, 679]},
	{"text": "WPS Office", "bbox": [605, 905, 816, 927]},
	{"text": "快拍即存·WPS拍照扫描", "bbox": [535, 940, 815, 958]}
]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord API: raw_items=144, valid_items=144, elapsed=38.9s
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGER TOENNIES, bbox=[577, 97, 716, 108]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[1]: text=徐州市中心医院, bbox=[310, 112, 560, 127]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[2]: text=东南大学医学院附属徐州医院, bbox=[307, 127, 564, 141]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[3]: text=肺功能检查报告, bbox=[374, 145, 495, 158]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[161, 167, 197, 177]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[5]: text=门诊/住院号：, bbox=[161, 176, 249, 186]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[6]: text=5832, bbox=[295, 177, 348, 186]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[7]: text=身高：, bbox=[161, 185, 197, 194]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[8]: text=178 cm, bbox=[295, 186, 342, 194]
2026-08-10 06:32:21,956 INFO     29 [qwen-vl-text] coord item[9]: text=年龄：, bbox=[161, 194, 197, 203]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[10]: text=32 Years, bbox=[295, 195, 355, 203]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[11]: text=性别：, bbox=[437, 167, 473, 177]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[12]: text=男, bbox=[570, 168, 583, 177]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[13]: text=测试号：, bbox=[437, 176, 488, 186]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[14]: text=2025051412, bbox=[570, 178, 642, 186]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[15]: text=体重：, bbox=[437, 185, 473, 194]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[16]: text=68 kg, bbox=[570, 187, 607, 195]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[17]: text=科别：, bbox=[437, 194, 473, 203]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[18]: text=呼吸与危重症医学科, bbox=[570, 195, 700, 204]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[19]: text=Flow [L/s], bbox=[293, 219, 335, 227]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[20]: text=F/V ex, bbox=[480, 220, 507, 227]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[21]: text=10, bbox=[275, 232, 286, 239]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[22]: text=5, bbox=[279, 252, 286, 259]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[23]: text=0, bbox=[279, 271, 286, 278]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[24]: text=1, bbox=[325, 279, 332, 286]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[25]: text=2, bbox=[364, 279, 371, 286]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[26]: text=3, bbox=[403, 279, 409, 286]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[27]: text=4, bbox=[441, 279, 448, 286]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[28]: text=5, bbox=[478, 279, 485, 286]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[29]: text=6, bbox=[516, 279, 523, 286]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[30]: text=7, bbox=[553, 279, 560, 286]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[31]: text=1, bbox=[575, 268, 598, 276]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[32]: text=2, bbox=[575, 276, 598, 284]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[33]: text=5, bbox=[279, 292, 286, 300]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[34]: text=10, bbox=[275, 313, 286, 320]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[35]: text=F/V in, bbox=[482, 326, 507, 334]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[36]: text=日期, bbox=[151, 353, 182, 363]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[37]: text=预计值, bbox=[368, 343, 415, 353]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[38]: text=前次, bbox=[445, 343, 476, 353]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[39]: text=前/预, bbox=[497, 343, 534, 353]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[40]: text=后次, bbox=[563, 343, 594, 353]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[41]: text=后/预, bbox=[616, 343, 655, 353]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[42]: text=改善率, bbox=[667, 343, 713, 353]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[43]: text=时间, bbox=[151, 363, 182, 372]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[44]: text=25/5/28, bbox=[422, 355, 475, 363]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[45]: text=25/5/28, bbox=[542, 355, 594, 363]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[46]: text=9:33:12, bbox=[422, 364, 475, 372]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[47]: text=10:00:0, bbox=[542, 364, 594, 372]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[48]: text=VC MAX, bbox=[150, 384, 197, 392]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[49]: text=[L], bbox=[332, 384, 352, 393]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[50]: text=5.31, bbox=[384, 384, 415, 392]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[51]: text=4.00, bbox=[445, 384, 476, 392]
2026-08-10 06:32:21,957 INFO     29 [qwen-vl-text] coord item[52]: text=75.3, bbox=[506, 384, 536, 392]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[53]: text=4.63, bbox=[564, 384, 594, 392]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[54]: text=87.1, bbox=[624, 384, 655, 392]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[55]: text=15.62, bbox=[678, 384, 715, 392]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[56]: text=ERV, bbox=[150, 394, 174, 402]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[57]: text=[L], bbox=[332, 394, 352, 403]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[58]: text=1.56, bbox=[384, 394, 415, 402]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[59]: text=IC, bbox=[150, 404, 166, 412]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[60]: text=[L], bbox=[332, 404, 352, 413]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[61]: text=3.75, bbox=[384, 404, 415, 412]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[62]: text=FVC, bbox=[150, 424, 172, 432]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[63]: text=[L], bbox=[332, 424, 352, 433]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[64]: text=5.08, bbox=[384, 424, 415, 432]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[65]: text=4.00, bbox=[445, 424, 476, 432]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[66]: text=78.7, bbox=[506, 424, 536, 432]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[67]: text=4.62, bbox=[564, 424, 594, 432]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[68]: text=91.0, bbox=[626, 424, 657, 432]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[69]: text=15.55, bbox=[680, 424, 717, 432]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[70]: text=FEV 1, bbox=[150, 435, 185, 443]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[71]: text=[L], bbox=[332, 435, 352, 444]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[72]: text=4.24, bbox=[384, 435, 415, 443]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[73]: text=2.51, bbox=[445, 435, 476, 443]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[74]: text=59.2, bbox=[506, 435, 536, 443]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[75]: text=3.07, bbox=[564, 435, 594, 443]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[76]: text=72.5, bbox=[626, 435, 657, 443]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[77]: text=22.53, bbox=[680, 435, 717, 443]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[78]: text=FEV 1 % FVC, bbox=[150, 445, 234, 453]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[79]: text=[%], bbox=[332, 445, 352, 454]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[80]: text=82.49, bbox=[377, 445, 415, 453]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[81]: text=62.65, bbox=[440, 445, 476, 453]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[82]: text=75.9, bbox=[506, 445, 536, 453]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[83]: text=66.43, bbox=[558, 445, 596, 453]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[84]: text=80.5, bbox=[626, 445, 657, 453]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[85]: text=6.05, bbox=[689, 445, 717, 453]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[86]: text=FEV 1 % VC MAX, bbox=[150, 455, 258, 463]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[87]: text=[%], bbox=[332, 455, 352, 464]
2026-08-10 06:32:21,958 INFO     29 [qwen-vl-text] coord item[88]: text=81.45, bbox=[377, 455, 415, 463]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[89]: text=62.65, bbox=[440, 455, 476, 463]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[90]: text=76.9, bbox=[506, 455, 536, 463]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[91]: text=66.39, bbox=[558, 455, 596, 463]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[92]: text=81.5, bbox=[626, 455, 657, 463]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[93]: text=5.98, bbox=[689, 455, 717, 463]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[94]: text=PEF, bbox=[147, 466, 170, 474]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[95]: text=[L/s], bbox=[315, 466, 352, 475]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[96]: text=9.70, bbox=[384, 466, 415, 474]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[97]: text=7.10, bbox=[445, 466, 476, 474]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[98]: text=73.1, bbox=[506, 466, 536, 474]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[99]: text=9.89, bbox=[564, 466, 594, 474]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[100]: text=101.9, bbox=[620, 466, 657, 474]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[101]: text=39.28, bbox=[682, 466, 717, 474]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[102]: text=MEF 75, bbox=[145, 476, 193, 484]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[103]: text=[L/s], bbox=[315, 476, 352, 485]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[104]: text=8.32, bbox=[384, 476, 415, 484]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[105]: text=3.64, bbox=[445, 476, 476, 484]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[106]: text=43.8, bbox=[506, 476, 536, 484]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[107]: text=5.40, bbox=[564, 476, 594, 484]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[108]: text=64.8, bbox=[626, 476, 657, 484]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[109]: text=48.11, bbox=[682, 476, 717, 484]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[110]: text=MEF 50, bbox=[145, 487, 193, 495]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[111]: text=[L/s], bbox=[315, 487, 352, 496]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[112]: text=5.40, bbox=[384, 487, 415, 495]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[113]: text=1.57, bbox=[445, 487, 476, 495]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[114]: text=29.1, bbox=[506, 487, 536, 495]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[115]: text=2.29, bbox=[564, 487, 594, 495]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[116]: text=42.4, bbox=[626, 487, 657, 495]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[117]: text=45.60, bbox=[682, 487, 717, 495]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[118]: text=MEF 25, bbox=[145, 497, 193, 505]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[119]: text=[L/s], bbox=[315, 497, 352, 506]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[120]: text=2.47, bbox=[384, 497, 415, 505]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[121]: text=0.49, bbox=[445, 497, 476, 505]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[122]: text=19.7, bbox=[506, 497, 536, 505]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[123]: text=0.69, bbox=[564, 497, 594, 505]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[124]: text=28.1, bbox=[626, 497, 657, 505]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[125]: text=42.74, bbox=[682, 497, 717, 505]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[126]: text=MMEF 75/25, bbox=[145, 507, 223, 515]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[127]: text=[L/s], bbox=[315, 507, 352, 516]
2026-08-10 06:32:21,959 INFO     29 [qwen-vl-text] coord item[128]: text=4.78, bbox=[384, 507, 415, 515]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[129]: text=1.24, bbox=[445, 507, 476, 515]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[130]: text=26.0, bbox=[506, 507, 536, 515]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[131]: text=1.72, bbox=[564, 507, 594, 515]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[132]: text=36.0, bbox=[626, 507, 657, 515]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[133]: text=38.55, bbox=[682, 507, 717, 515]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[134]: text=V backextrapol. % FVC, bbox=[145, 517, 313, 525]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[135]: text=[%], bbox=[330, 517, 351, 526]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[136]: text=2.29, bbox=[445, 517, 476, 525]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[137]: text=2.55, bbox=[564, 517, 594, 525]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[138]: text=11.69, bbox=[682, 517, 717, 525]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[139]: text=结论：, bbox=[161, 555, 206, 568]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[140]: text=支气管舒张试验阳性, bbox=[210, 580, 384, 593]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[141]: text=医生签字：, bbox=[579, 666, 661, 679]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[142]: text=WPS Office, bbox=[605, 905, 816, 927]
2026-08-10 06:32:21,960 INFO     29 [qwen-vl-text] coord item[143]: text=快拍即存·WPS拍照扫描, bbox=[535, 940, 815, 958]
2026-08-10 06:32:21,961 INFO     29 [qwen-vl-text] page=0 — 136/136 coords, api_time=38.9s
2026-08-10 06:32:21,961 INFO     29 [qwen-vl-text] new_positions (136):
[[0, 343.47425256347657, 426.21761669921875, 81.66333142089843, 90.92412158203125], [0, 184.53556030273438, 333.354560546875, 94.291681640625, 106.92003186035156], [0, 182.7497322998047, 335.7356645507813, 106.92003186035156, 118.70649206542969], [0, 222.63322436523438, 294.66162048339845, 122.07405212402344, 133.01862231445313], [0, 95.83943615722657, 117.26937219238282, 140.59563244628907, 149.01453259277343], [0, 95.83943615722657, 148.22372424316407, 148.172642578125, 156.59154272460938], [0, 175.60642028808596, 207.15604833984375, 149.01453259277343, 156.59154272460938], [0, 95.83943615722657, 117.26937219238282, 155.74965270996094, 163.32666284179686], [0, 175.60642028808596, 203.5843923339844, 156.59154272460938, 163.32666284179686], [0, 95.83943615722657, 117.26937219238282, 163.32666284179686, 170.9036729736328], [0, 175.60642028808596, 211.32298034667969, 164.1685528564453, 170.9036729736328], [0, 260.1356124267578, 281.5655484619141, 140.59563244628907, 149.01453259277343], [0, 339.30732055664066, 347.04590856933595, 141.4375224609375, 149.01453259277343], [0, 260.1356124267578, 290.4946884765625, 148.172642578125, 156.59154272460938], [0, 339.30732055664066, 382.1671926269531, 149.85642260742188, 156.59154272460938], [0, 260.1356124267578, 281.5655484619141, 155.74965270996094, 163.32666284179686], [0, 339.30732055664066, 361.3325325927735, 157.43343273925782, 164.1685528564453], [0, 260.1356124267578, 281.5655484619141, 163.32666284179686, 170.9036729736328], [0, 339.30732055664066, 416.6932006835938, 164.1685528564453, 171.74556298828125], [0, 174.41586828613282, 199.41746032714843, 184.37391320800782, 191.1090333251953], [0, 285.73248046875, 301.8049324951172, 185.21580322265623, 191.1090333251953], [0, 163.7009002685547, 170.24893627929688, 195.3184833984375, 201.21171350097657], [0, 166.08200427246095, 170.24893627929688, 212.15628369140626, 218.04951379394532], [0, 166.08200427246095, 170.24893627929688, 228.15219396972657, 234.04542407226563], [0, 193.4647003173828, 197.63163232421877, 234.88731408691405, 240.7805441894531], [0, 216.68046435546876, 220.8473963623047, 234.88731408691405, 240.7805441894531], [0, 239.8962283935547, 243.46788439941406, 234.88731408691405, 240.7805441894531], [0, 262.5167164306641, 266.6836484375, 234.88731408691405, 240.7805441894531], [0, 284.5419284667969, 288.7088604736328, 234.88731408691405, 240.7805441894531], [0, 307.1624165039063, 311.3293485107422, 234.88731408691405, 240.7805441894531], [0, 329.1876285400391, 333.354560546875, 234.88731408691405, 240.7805441894531], [0, 342.28370056152346, 355.9750485839844, 225.62652392578124, 232.36164404296875], [0, 342.28370056152346, 355.9750485839844, 232.36164404296875, 239.09676416015625], [0, 166.08200427246095, 170.24893627929688, 245.83188427734376, 252.56700439453124], [0, 163.7009002685547, 170.24893627929688, 263.51157458496095, 269.4048046875], [0, 286.92303247070316, 301.8049324951172, 274.4561447753906, 281.19126489257815], [0, 89.88667614746095, 108.34023217773438, 297.18717517089846, 305.6060753173828], [0, 219.061568359375, 247.03954040527344, 288.76827502441404, 297.18717517089846], [0, 264.89782043457035, 283.3513764648438, 288.76827502441404, 297.18717517089846], [0, 295.85217248535156, 317.8773845214844, 288.76827502441404, 297.18717517089846], [0, 335.1403885498047, 353.59394458007813, 288.76827502441404, 297.18717517089846], [0, 366.6900166015625, 389.90578063964847, 288.76827502441404, 297.18717517089846], [0, 397.04909265136723, 424.43178869628906, 288.76827502441404, 297.18717517089846], [0, 89.88667614746095, 108.34023217773438, 305.6060753173828, 313.18308544921877], [0, 251.20647241210938, 282.7561004638672, 298.8709552001953, 305.6060753173828], [0, 322.63959252929686, 353.59394458007813, 298.8709552001953, 305.6060753173828], [0, 251.20647241210938, 282.7561004638672, 306.44796533203123, 313.18308544921877], [0, 322.63959252929686, 353.59394458007813, 306.44796533203123, 313.18308544921877], [0, 89.29140014648438, 117.26937219238282, 323.285765625, 330.0208857421875], [0, 197.63163232421877, 209.53715234375, 323.285765625, 330.86277575683596], [0, 228.585984375, 247.03954040527344, 323.285765625, 330.0208857421875], [0, 264.89782043457035, 283.3513764648438, 323.285765625, 330.0208857421875], [0, 301.20965649414063, 319.06793652343754, 323.285765625, 330.0208857421875], [0, 335.7356645507813, 353.59394458007813, 323.285765625, 330.0208857421875], [0, 371.45222460937504, 389.90578063964847, 323.285765625, 330.0208857421875], [0, 403.5971286621094, 425.6223406982422, 323.285765625, 330.0208857421875], [0, 89.29140014648438, 103.57802416992187, 331.7046657714844, 338.43978588867185], [0, 197.63163232421877, 209.53715234375, 331.7046657714844, 339.2816759033203], [0, 228.585984375, 247.03954040527344, 331.7046657714844, 338.43978588867185], [0, 89.29140014648438, 98.81581616210939, 340.12356591796873, 346.85868603515627], [0, 197.63163232421877, 209.53715234375, 340.12356591796873, 347.7005760498047], [0, 228.585984375, 247.03954040527344, 340.12356591796873, 346.85868603515627], [0, 89.29140014648438, 102.38747216796875, 356.9613662109375, 363.696486328125], [0, 197.63163232421877, 209.53715234375, 356.9613662109375, 364.53837634277346], [0, 228.585984375, 247.03954040527344, 356.9613662109375, 363.696486328125], [0, 264.89782043457035, 283.3513764648438, 356.9613662109375, 363.696486328125], [0, 301.20965649414063, 319.06793652343754, 356.9613662109375, 363.696486328125], [0, 335.7356645507813, 353.59394458007813, 356.9613662109375, 363.696486328125], [0, 372.64277661132815, 391.0963326416016, 356.9613662109375, 363.696486328125], [0, 404.7876806640625, 426.81289270019533, 356.9613662109375, 363.696486328125], [0, 89.29140014648438, 110.12606018066407, 366.2221563720703, 372.9572764892578], [0, 197.63163232421877, 209.53715234375, 366.2221563720703, 373.79916650390624], [0, 228.585984375, 247.03954040527344, 366.2221563720703, 372.9572764892578], [0, 264.89782043457035, 283.3513764648438, 366.2221563720703, 372.9572764892578], [0, 301.20965649414063, 319.06793652343754, 366.2221563720703, 372.9572764892578], [0, 335.7356645507813, 353.59394458007813, 366.2221563720703, 372.9572764892578], [0, 372.64277661132815, 391.0963326416016, 366.2221563720703, 372.9572764892578], [0, 404.7876806640625, 426.81289270019533, 366.2221563720703, 372.9572764892578], [0, 89.29140014648438, 139.29458422851562, 374.6410565185547, 381.3761766357422], [0, 197.63163232421877, 209.53715234375, 374.6410565185547, 382.2180666503906], [0, 224.41905236816407, 247.03954040527344, 374.6410565185547, 381.3761766357422], [0, 261.9214404296875, 283.3513764648438, 374.6410565185547, 381.3761766357422], [0, 301.20965649414063, 319.06793652343754, 374.6410565185547, 381.3761766357422], [0, 332.1640085449219, 354.78449658203124, 374.6410565185547, 381.3761766357422], [0, 372.64277661132815, 391.0963326416016, 374.6410565185547, 381.3761766357422], [0, 410.1451646728516, 426.81289270019533, 374.6410565185547, 381.3761766357422], [0, 89.29140014648438, 153.58120825195314, 383.05995666503907, 389.79507678222654], [0, 197.63163232421877, 209.53715234375, 383.05995666503907, 390.636966796875], [0, 224.41905236816407, 247.03954040527344, 383.05995666503907, 389.79507678222654], [0, 261.9214404296875, 283.3513764648438, 383.05995666503907, 389.79507678222654], [0, 301.20965649414063, 319.06793652343754, 383.05995666503907, 389.79507678222654], [0, 332.1640085449219, 354.78449658203124, 383.05995666503907, 389.79507678222654], [0, 372.64277661132815, 391.0963326416016, 383.05995666503907, 389.79507678222654], [0, 410.1451646728516, 426.81289270019533, 383.05995666503907, 389.79507678222654], [0, 87.50557214355469, 101.19692016601563, 392.3207468261719, 399.0558669433594], [0, 187.5119403076172, 209.53715234375, 392.3207468261719, 399.8977569580078], [0, 228.585984375, 247.03954040527344, 392.3207468261719, 399.0558669433594], [0, 264.89782043457035, 283.3513764648438, 392.3207468261719, 399.0558669433594], [0, 301.20965649414063, 319.06793652343754, 392.3207468261719, 399.0558669433594], [0, 335.7356645507813, 353.59394458007813, 392.3207468261719, 399.0558669433594], [0, 369.07112060546876, 391.0963326416016, 392.3207468261719, 399.0558669433594], [0, 405.97823266601563, 426.81289270019533, 392.3207468261719, 399.0558669433594], [0, 86.31502014160156, 114.88826818847657, 400.73964697265626, 407.47476708984374], [0, 187.5119403076172, 209.53715234375, 400.73964697265626, 408.3166571044922], [0, 228.585984375, 247.03954040527344, 400.73964697265626, 407.47476708984374], [0, 264.89782043457035, 283.3513764648438, 400.73964697265626, 407.47476708984374], [0, 301.20965649414063, 319.06793652343754, 400.73964697265626, 407.47476708984374], [0, 335.7356645507813, 353.59394458007813, 400.73964697265626, 407.47476708984374], [0, 372.64277661132815, 391.0963326416016, 400.73964697265626, 407.47476708984374], [0, 405.97823266601563, 426.81289270019533, 400.73964697265626, 407.47476708984374], [0, 86.31502014160156, 114.88826818847657, 410.00043713378903, 416.73555725097657], [0, 187.5119403076172, 209.53715234375, 410.00043713378903, 417.577447265625], [0, 228.585984375, 247.03954040527344, 410.00043713378903, 416.73555725097657], [0, 264.89782043457035, 283.3513764648438, 410.00043713378903, 416.73555725097657], [0, 301.20965649414063, 319.06793652343754, 410.00043713378903, 416.73555725097657], [0, 335.7356645507813, 353.59394458007813, 410.00043713378903, 416.73555725097657], [0, 372.64277661132815, 391.0963326416016, 410.00043713378903, 416.73555725097657], [0, 405.97823266601563, 426.81289270019533, 410.00043713378903, 416.73555725097657], [0, 86.31502014160156, 114.88826818847657, 418.41933728027345, 425.15445739746093], [0, 187.5119403076172, 209.53715234375, 418.41933728027345, 425.99634741210934], [0, 228.585984375, 247.03954040527344, 418.41933728027345, 425.15445739746093], [0, 264.89782043457035, 283.3513764648438, 418.41933728027345, 425.15445739746093], [0, 301.20965649414063, 319.06793652343754, 418.41933728027345, 425.15445739746093], [0, 335.7356645507813, 353.59394458007813, 418.41933728027345, 425.15445739746093], [0, 372.64277661132815, 391.0963326416016, 418.41933728027345, 425.15445739746093], [0, 405.97823266601563, 426.81289270019533, 418.41933728027345, 425.15445739746093], [0, 86.31502014160156, 132.74654821777344, 426.8382374267578, 433.5733575439453], [0, 187.5119403076172, 209.53715234375, 426.8382374267578, 434.41524755859376], [0, 228.585984375, 247.03954040527344, 426.8382374267578, 433.5733575439453], [0, 264.89782043457035, 283.3513764648438, 426.8382374267578, 433.5733575439453], [0, 301.20965649414063, 319.06793652343754, 426.8382374267578, 433.5733575439453], [0, 335.7356645507813, 353.59394458007813, 426.8382374267578, 433.5733575439453], [0, 372.64277661132815, 391.0963326416016, 426.8382374267578, 433.5733575439453], [0, 405.97823266601563, 426.81289270019533, 426.8382374267578, 433.5733575439453], [0, 86.31502014160156, 186.32138830566407, 435.2571375732422, 441.9922576904297], [0, 196.44108032226563, 208.94187634277344, 435.2571375732422, 442.8341477050781]]
2026-08-10 06:32:21,961 INFO     29 [qwen-vl-text] ═══ DONE ═══ 136 positions, pages=1, time=63.3s
2026-08-10 06:32:21,977 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 06:32:21,977 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "212 items", "markdown": "", "text": "", "name": "MEFE(1).pdf", "output_format": "chunks", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_Examination\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 06:32:21,977 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 06:32:21,978 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:32:21.977+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 6, "failed": 0, "current": {"e7b1979a948411f1bd9827cf206dfa2d": {"id": "e7b1979a948411f1bd9827cf206dfa2d", "doc_id": "e6e9ad0c948411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MEFE(1).pdf", "type": "pdf", "location": "MEFE(1).pdf", "size": 5502142, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786343396901, "task_type": "dataflow", "root_trace_id": "5667f9593fa8497eabc7fd15b6ab98c0", "root_traceparent": "00-5667f9593fa8497eabc7fd15b6ab98c0-4a2925d1ccf16074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:32:21,979 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-10 06:32:22,272 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 06:32:22,273 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "MEFE(1).pdf"}
2026-08-10 06:32:22,273 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 06:32:22,414 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786343398234, 'update_date': datetime.datetime(2026, 8, 10, 6, 29, 58), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 810640, 'status': '1'}
2026-08-10 06:32:22,636 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=徐州市中心医院
门（急）诊病历
姓名：
性别：男
科室：呼吸与危重症门诊
号别：普通号
姓名
证件类型
居民身份证
性别
男
证件号码
3:
出生日期
1992年07月11日
门诊编号
0005832911
婚姻
就诊时间
2025-02-20 13:22
陪伴者姓名
初诊/复诊/急诊
复诊
陪伴者与患者的关系
过敏史
否认(病史提供人)
联系人电话
主诉：支气管哮喘复诊。
病史：现病史：哮喘，患者来院进行D5982C00008项目V15随访
既往史：有既往疾病史，鼻炎。
体格检查：
体温：(℃)，脉搏：次/分，血压：/(mmHg)，呼吸：次/分，意识状态：清醒
皮肤粘膜：颜色正常，无皮疹，无皮下出血，无水肿。
胸部：外形正常，无胸壁压痛。肺脏及胸膜：呼吸音正常，未闻及啰音，未触及胸
膜摩擦音。
心脏：心律齐，未闻及杂音，未闻及心包摩擦音，周围血管征阴性。
腹部：外形正常，无压痛，无反跳痛。未触及包块。肝脏未触及。无肾区叩击痛，
移动性浊音阴性，肠鸣音正常。
神经反射：浅反射正常，深反射正常，病理反射阴性，脑膜刺激征阴性。
诊断：支气管哮喘
处理措施：
根据方案要求，患者今日来院进行V15随访，患者于今日08点
00分左右到院随访，与患者核实上次访视至今未进行过任何
疫苗接种
第（1）页
WPS Office
快拍即存·WPS拍照扫描
徐州市中心医院
门（急）诊病历
姓名
性别：男
科室：呼吸与危重症门诊
号别：普通号
患者万托林已停用大于6h，昨晚完成白色吸入剂的吸入时间是21：40，
昨晚完成红色吸入剂的吸入时间是21：43。今晨未吸入研究药物，规律
吸入研究药物中，未出现多服及漏服现象
自上次访视至今，无不适，无新增合并用药，已和患者确认无其他门诊
以及住院记录，无哮喘急性发作，已根据方案要求清洁吸入器装置
查看患者电子日志，日志偶有漏做现象，进行两次给药前肺功能测定
患者已空腹大于8小时，完成血样采集
患者自行完成ACQ6问卷，AQLQ+12问卷，EQ-5D-5L问卷，PGIC问卷，患者
于今日09点26分完成白色吸入剂2喷，09点28分完成红色吸入剂2喷，患
者已掌握给药方法。进行给药后15min肺功能检查，进行给药后30min肺
功能检查，进行给药后1h肺功能检查，进行给药后2h肺功能检查，进行
给药后3h肺功能检查
告知患者今日已完成试验，嘱后续治疗方案为信必可320ug bid 吸入，
今日登记IRT系统进行完成试验登记，回收相关设备和药物。
是否留观：否
特别提醒：根据《传染病防治法》《治安管理处罚法》等法律规定，如果您隐
瞒上述情况或者拒绝配合医务人员开展调查等处置措施的，将承担相应的法律责任。
承诺以上情况均属实。
医师签名：张敏浩
患者签名：
第（2）页
---
JAEGER TOENNIES
徐州市中心医院
东南大学医学院附属徐州医院
肺功能检查报告
姓名：
门诊/住院号：5832
身高：178 cm
年龄：32 Years
性别：男
测试号：2025051412
体重：68 kg
科别：呼吸与危重症医学科
Flow [L/s]
F/V ex
10
5
0
1
2
3
4
5
6
7
1
2
10
F/V in
日期
预计值
前次
前/预
后次
后/预
改善率
时间
25/5/28
25/5/28
9:33:12
10:00:0
VC MAX
[L]
5.31
4.00
75.3
4.63
87.1
15.62
ERV
[L]
1.56
IC
[L]
3.75
FVC
[L]
5.08
4.00
78.7
4.62
91.0
15.55
FEV 1
[L]
4.24
2.51
59.2
3.07
72.5
22.53
FEV 1 % FVC
[%]
82.49
62.65
75.9
66.43
80.5
6.05
FEV 1 % VC MAX
[%]
81.45
62.65
76.9
66.39
81.5
5.98
PEF
[L/s]
9.70
7.10
73.1
9.89
101.9
39.28
MEF 75
[L/s]
8.32
3.64
43.8
5.40
64.8
48.11
MEF 50
[L/s]
5.40
1.57
29.1
2.29
42.4
45.60
MEF 25
[L/s]
2.47
0.49
19.7
0.69
28.1
42.74
MMEF 75/25
[L/s]
4.78
1.24
26.0
1.72
36.0
38.55
V backextrapol. % FVC
[%]
2.29
2.55
11.69
结论：
支气管舒张试验阳性
医生签字：
WPS Office
快拍即存·WPS拍照扫描
2026-08-10 06:32:22,959 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 06:32:22,960 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "MEFE(1).pdf", "embedding_token_consumption": 1503}
2026-08-10 06:32:22,960 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 06:32:23,137 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 06:32:23,137 INFO     29 [Trace] task=e7b1979a | doc=MEFE(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 06:32:23,139 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:32:23,139 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:32:23,145 INFO     29 set_progress(e7b1979a948411f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 06:32:23 [DOC Engine]:
Start to index...
2026-08-10 06:32:23,203 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.054s]
2026-08-10 06:32:23,208 INFO     29 set_progress(e7b1979a948411f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 06:32:23,226 INFO     29 set_progress(e7b1979a948411f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 06:32:23 Indexing done (0.07s). Task done (144.71s)
2026-08-10 06:32:23,236 INFO     29 [Done], chunks(2), token(1503), elapsed:144.71
2026-08-10 06:32:23,315 INFO     29 handle_task done for task {"id": "e7b1979a948411f1bd9827cf206dfa2d", "doc_id": "e6e9ad0c948411f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "MEFE(1).pdf", "type": "pdf", "location": "MEFE(1).pdf", "size": 5502142, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786343396901, "task_type": "dataflow", "root_trace_id": "5667f9593fa8497eabc7fd15b6ab98c0", "root_traceparent": "00-5667f9593fa8497eabc7fd15b6ab98c0-4a2925d1ccf16074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
