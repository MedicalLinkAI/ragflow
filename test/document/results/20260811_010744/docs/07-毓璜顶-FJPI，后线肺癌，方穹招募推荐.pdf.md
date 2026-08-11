# 基准结果：07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf`
- 大小：4701.3 KB
- PDF 总页数：27
- doc_id：`cbc5ba5e94e111f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T01:34:51  完成时间：2026-08-11T01:49:08  耗时：856.4s
- progress_msg：`17:49:04 Indexing done (0.15s). Task done (794.95s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | d6a40eff | 3 | 1-3 | 第2次住院 入院记录 姓名： 姓名： 出生地： 性别：男 职业：其他 年龄：75 |
| 2 | 9671e680 | 2 | 4-5 | 出院记录 登记号: 住院号: 姓名 姓名： 性别：男 年龄：75岁 科室· 入院 |
| 3 | 6404e61a | 1 | 6-6 | 门（急）诊病历 初诊 科室 日期:2026-02-02 09:07 医学 性别: |
| 4 | 61f70a64 | 1 | 7-7 | 门诊号：- 姓名 性别 男 年龄 70岁 病人编号 病区 病案号 门诊号 送检科 |
| 5 | 218056c7 | 1 | 8-8 | 病理号 住院 门诊号 1-1] 姓名 70岁 病人编号 0007 病区 门诊号  |
| 6 | aacae8bc | 1 | 10-10 | 门楼号 姓名 病区 送检科室 标本名称 临床诊断 内眼所见 穿刺组织3条，合计长 |
| 7 | b75b7fb4 | 1 | 11-11 | 门诊号： 姓名 性别 75岁 病人编 病区 病区 病案号 门诊号 送检科室 送检 |
| 8 | f477a934 | 3 | 12-14 | 病历 姓名 病区 送检科室 标本名称 临床诊断 病理诊断 检查项目:肿瘤多基因检 |
| 9 | 8654b242 | 1 | 15-15 | 超声检查报告单 思者登 姓 性别：男 年龄：75岁 床号：A02 检查所见： 右 |
| 10 | 9206ece0 | 1 | 16-16 | 超声检查报告单 患者登记 姓名： 性别：男 年龄：75岁 号 1 2 检查所见： |
| 11 | 33e948ce | 1 | 17-17 | 影像学检查报告单 扫一扫查看云胶片（访问码）： 姓名： 性别：男 年龄：75岁  |
| 12 | af174946 | 1 | 18-18 | 影像学检查报告单 姓名： 性别：男 年龄：70岁 影像 检查日期：2020-12 |
| 13 | e3d99976 | 1 | 19-19 | 影像学检查报告单 扫码看电子胶片 姓 性别：男 年龄：70岁 影像 科 住院 检 |
| 14 | f2a12f19 | 1 | 20-20 | 超声检查报告单 患者 性别：男 年龄：75岁 检查所见： 甲状腺大小尚可，内回声 |
| 15 | c7afabe5 | 1 | 21-21 | 心电图报告单 性别：男 年龄：75岁 危重症医学科率：69 bpm P-R间期： |
| 16 | 6359c547 | 2 | 22-23 | \begin{tabular}{cccccccccc} 报告时间: 2020-0 |
| 17 | 65aa44ad | 1 | 23-23 | <table><tr><td>白细胞</td><td>None</td><td> |
| 18 | bbbadd59 | 1 | 25-25 | <table><tr><td>乙型肝炎表面抗原(化学发光法)</td><td>N |
| 19 | 117c2fb1 | 1 | 26-26 | <table><tr><td>癌胚抗原</td><td>None</td><td |
| 20 | f3ec24f4 | 1 | 24-24 | <table><tr><td>凝血酶原时间</td><td>None</td>< |

- chunks 总数：20
- 各 chunk 页数合计（含跨页重复）：26
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]`
- 覆盖页数：25 / 27；缺失页：`[9, 27]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 25/27 页，缺失 [9, 27]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 12 | 12 | 12 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 5 | 0 | 5 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "DischargeRecord": 1, "OutpatientRecord": 1, "ExaminationReport": 12, "LabReport": 5}`
- ChunkMerger：`{"found": true, "merged": 20, "sources": 9, "stats": {"Extractor:LabExam": 5, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 12, "Extractor:Progress": 1}, "filtered_noise": 4}`
- Extractor skip 证据：4 条
  - `[no_items_extracted] 2026-08-10 17:43:06,653 WARNING  29 [qwen-vl-table] page=21 no items extracted`
  - `[no_items_extracted] 2026-08-10 17:43:10,003 WARNING  29 [qwen-vl-table] page=22 no items extracted`
  - `[no_items_extracted] 2026-08-10 17:43:10,003 WARNING  29 [qwen-vl-table] No items extracted from any page`
  - `[no_text_noise] 2026-08-10 17:49:01,726 INFO     29 [ChunkMerger] Merged 20 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 17:34:55,487 INFO     29 handle_task begin for task {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 17:34:55,684 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 17:34:55,804 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 17:34:55,817 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:34:55,817 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 17:34:55,818 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 17:34:55,826 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 17:34:55,826 INFO     29 ============================================================
2026-08-10 17:34:55,826 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 17:34:55,826 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 17:34:55,826 INFO     29 ============================================================
2026-08-10 17:34:55,826 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 17:34:55,826 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 17:34:55,828 INFO     29 No torch found.
2026-08-10 17:34:57,349 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=27
2026-08-10 17:34:57,592 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2062587, prompt_len=764
2026-08-10 17:34:59,041 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 17:34:59,042 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 17:34:59,056 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2062587, prompt_len=401
2026-08-10 17:34:59,259 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:34:59.258+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:35:05,536 INFO     29 [qwen-vl-parser] text API response (len=1212):
["第2次住院", "入院记录", "姓名：", "姓名：", "出生地：", "性别：男", "职业：其他", "年龄：75岁", "入院时间：2026-01-26 10:12", "民族：汉族", "记录时间：2026-01-26 13:59", "婚姻：已婚", "病史陈述者：患者本人", "主诉：确诊肺癌5年，病情进展1月余", "现病史：患者因“胸闷2月，干咳1周”于2020年12月17日第一次入住我科，于2020-", "12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：", "CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），", "CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合", "免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞；（痰）", "涂片内发现少量可疑恶性肿瘤细胞，于2020-12-27给予培美曲塞800mgd1+卡铂", "400mgd2，并辅以止吐、保胃等治疗，化疗过程顺利，准予出院。出院诊断：左肺上叶恶", "性肿瘤（腺癌 T4N3M1 IV期）、为肿瘤化学治疗疗程、纵隔淋巴结继发恶性肿瘤、肺", "门淋巴结继发恶性肿瘤、阻塞性肺炎、肝囊肿、单纯性肾囊肿。出院后先后服用吉非", "替尼、泰瑞沙靶向治疗至今。", "1月余前患者就诊于外院，复查肺CT提示病灶增大，具体不详，无发热乏力，无咳", "嗽咳痰，无胸闷憋气等不适，为求进一步诊治就诊于我院门诊，为行二次活检收入我", "科，患者自发病以来，神志清，精神可，饮食睡眠可，大小便正常，体重近期未见明", "显变化。", "既往史：患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切", "接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术", "史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。", "个人史：生于山东省胶州市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿", "山、高氟区、低碘区居住史，无化学性物质、无放射性物质、无有毒物质接触史，无", "吸毒史，无吸烟史，无饮酒史，无特殊药物服用史，无冶游史。", "婚姻史：适龄结婚，配偶体健。", "家族史：父母已故（具体不详），父有糖尿病病史，1弟因白血病去世，一妹去世，2", "妹健在，否认家族中有遗传倾向性疾病及传染性疾病。", "体格检查", "T：36.3℃ P：69次/分 R：17次/分 BP：120/66mmHg H：160cm W：52kg BMI：20.", "31kg/m²", "一般情况：正常发育状态，营养良好，体型匀称型，自主体位，正常面容，神志清楚", "，正常步态，语言清晰，查体合作。", "第1页"]
2026-08-10 17:35:05,537 INFO     29 [qwen-vl-parser] page=1 text: 43 lines (bbox 0-42)
2026-08-10 17:35:05,537 INFO     29 [qwen-vl-parser] page=1 text: 43 sections
2026-08-10 17:35:05,815 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2484453, prompt_len=764
2026-08-10 17:35:07,258 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 17:35:07,259 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 17:35:07,274 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2484453, prompt_len=401
2026-08-10 17:35:14,582 INFO     29 [qwen-vl-parser] text API response (len=1275):
["另2次住院", "入院记录", "登记号:", "姓名:", "住院号", "皮肤、粘膜：皮肤黏膜无黄染 无皮疹、皮下出血，无皮下结节、瘢痕，皮下无水肿，", "毛发分布正常，无肝掌、蜘蛛痣。全身浅表淋巴结：全身浅表淋巴结无肿大。", "头部及其器官：头颅无畸形，毛发分布正常。眉毛正常，睫毛正常，无眼睑水肿，", "结膜无充血、苍白，眼球无震颤，巩膜无黄染，角膜正常，瞳孔等大等圆，对光调节", "反射正常。外耳道无畸形，无异常分泌物，乳突无压痛，听力正常。外鼻无畸形，无", "鼻翼扇动，无分泌物、出血、阻塞，鼻中隔基本居中，无穿孔，双侧鼻窦区无压痛。", "口唇无发绀，口腔粘膜无溃疡。伸舌无偏斜、震颤，齿龈无肿胀、出血。咽部粘膜无", "充血，扁桃体无肥大。喉咙发音清晰。", "颈部：颈部对称，软，颈动脉搏动正常，颈静脉无怒张，气管居中，肝颈静脉回流征", "阴性，甲状腺无肿大，无压痛，未扪及包块，未闻及血管杂音。", "胸部：胸廓对称、无畸形，乳房发育正常，胸骨无压痛，呼吸17次/分。", "肺部：呼吸运动正常，肋间隙无增宽、无变窄，呼吸规整，语颤无增强及减弱，无胸", "膜摩擦感、无皮下捻发感。叩诊清音，双肺呼吸音清晰，未闻及干、湿性啰音，语音", "传导正常，无胸膜摩擦音。", "心脏：心前区无隆起，心尖搏动未见增强及弥散，无震颤及心包摩擦感，心浊音界无", "扩大，心率69次/分，律齐，各瓣膜听诊区未闻及病理性杂音，无心包摩擦音。", "血管：桡动脉：脉率69次/分，脉律规整。无毛细血管搏动征，无股动脉枪击音。", "腹部：腹部平坦，对称，无腹壁静脉曲张，无胃肠型和蠕动波，腹部柔软，无压痛及", "反跳痛，未触及异常包块。肝、脾肋下未触及、质软、无压痛，Murphy氏征阴性。腹", "部叩诊：肝上界在右锁骨中线第五肋间，肝、肾区无叩击痛，无移动性浊音。肠鸣音", "正常，4次/分。未听到血管杂音。", "直肠肛门：肛门及直肠无异常。外生殖器无异常。", "脊柱、四肢：脊柱正常生理弯曲，无畸形、压痛、叩击痛，活动度正常，四肢无畸", "形，肌力、肌张力正常，关节活动度正常，双下肢无水肿，无静脉曲张。", "神经系统：痛、温、触觉正常，肌肉无萎缩、无瘫痪，无共济失调。腹壁反射正常，", "双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性、", "Gordon征阴性、Oppenheim征阴性、Hoffmann征阴性，脑膜刺激征阴性。", "专科检查", "辅助检查", "2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组", "化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），", "CK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合", "免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。", "第2页"]
2026-08-10 17:35:14,583 INFO     29 [qwen-vl-parser] page=2 text: 39 lines (bbox 43-81)
2026-08-10 17:35:14,583 INFO     29 [qwen-vl-parser] page=2 text: 39 sections
2026-08-10 17:35:14,652 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=314067, prompt_len=764
2026-08-10 17:35:15,861 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:35:15,861 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 17:35:15,872 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=314067, prompt_len=401
2026-08-10 17:35:16,777 INFO     29 [qwen-vl-parser] text API response (len=145):
["第2次住院", "入院记录", "登记号:", "姓名:", "住院号", "初步诊断", "肺部恶性肿瘤", "纵隔淋巴结继发恶性肿瘤", "肺门淋巴结继发恶性肿瘤", "医师签名", "项目内容", "患者（家属）签名", "以上患者所述内容及提供资料属实", "门诊病历已归还"]
2026-08-10 17:35:16,778 INFO     29 [qwen-vl-parser] page=3 text: 14 lines (bbox 82-95)
2026-08-10 17:35:16,778 INFO     29 [qwen-vl-parser] page=3 text: 14 sections
2026-08-10 17:35:17,088 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2562347, prompt_len=764
2026-08-10 17:35:18,432 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:35:18,435 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 17:35:18,453 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2562347, prompt_len=401
2026-08-10 17:35:28,757 INFO     29 [qwen-vl-parser] text API response (len=1518):
["出院记录", "登记号:", "住院号:", "姓名", "姓名：", "性别：男", "年龄：75岁", "科室·", "入院日期：2026-01-26", "出院日期：2026-01-31", "住院天数：5天", "入院情况：", "，男，75岁，因“确诊肺癌5年，病情进展1月余”于2026-01-", "26入院。患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切", "接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术", "史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。体检：T:", "36.3℃ P:69次/分 R:17次/分 BP:120/66mmHg。神志清，精神可，双肺呼吸音清，未", "闻及干湿性啰音。心脏各瓣膜听诊区未闻及异常杂音。腹软，无压痛，Murphy征阴", "性。双下肢无水肿。病理征阴性。辅助检查：2020-12-21行支气管镜检查，组织病理", "学示：(左侧隆突粘膜)非小细胞肺癌，免疫组化：CK7(+)，TTF-1(+)，", "NapsinA(+)，p40(部分+)，p63(部分+)，CK5/6(+)，ALK-D5F3(-)，ALK-", "D5F3-N(-)，S100(-)，Calponin(-)。结合免疫组化结果，符合腺癌；(左肺", "BALF)细胞蜡块内发现少量恶性肿瘤细胞。", "入院诊断：肺部恶性肿瘤纵隔淋巴结继发恶性肿瘤肺门淋巴结继发恶性肿瘤", "诊疗经过：入院后完善相关检验检查，【检验】血常规(无网红)+CRP：白细胞计数7.", "49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血", "小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原", "测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：", "22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4.", "820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆", "抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血", "试验、传染性标志物4项检测未见异常。【检查】十二通道常规心电图检查：大致正常", "心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性", "可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝", "囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超", "声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复", "查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随", "访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规", "整，请结合临床；【诊疗】入院后给予完善相关检查，排除禁忌后于2026-01-28行CT", "引导下经皮穿刺肺活检术，2026-01-30左肺组织穿刺活检示非小细胞肺癌伴大片坏", "死，结合形态学及免疫组化，符合腺癌。免疫组化示肿瘤细胞：CKpan(+)，", "CK7(+)，TTF-1(+)，p40(-)，CK5/6(-)；特殊染色：D-PAS(-)。现患者诊", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 17:35:28,760 INFO     29 [qwen-vl-parser] page=4 text: 45 lines (bbox 96-140)
2026-08-10 17:35:28,760 INFO     29 [qwen-vl-parser] page=4 text: 45 sections
2026-08-10 17:35:28,872 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=724214, prompt_len=764
2026-08-10 17:35:30,121 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:35:30,122 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 17:35:30,145 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=724214, prompt_len=401
2026-08-10 17:35:31,334 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:35:31.334+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:35:32,219 INFO     29 [qwen-vl-parser] text API response (len=374):
["出院记录", "登记号", "住院号", "姓名：", "断明确，拟出院后行基因检测治疗，准予办理出院。", "出院诊断：肺部恶性肿瘤（腺癌 rT4N3MO IVA期）", "纵隔淋巴结继发恶性肿瘤", "肺门淋巴结继发恶性肿瘤", "颈部淋巴结肿大", "脾术后", "慢性胆囊炎", "肝囊肿", "肾结节", "出院情况：患者一般情况可，查体：神志清，双肺呼吸音清，心律齐，腹软，无压痛", "及反跳痛，双下肢无水肿。", "出院医嘱：", "1.注意休息，避免感染、劳累；", "2.出院后分子病理科行基因检测，出院2周待结果回报后于呼吸与危重症医学科门诊就", "诊就诊制定进一步治疗方案；", "3.如有不适或复查指标异常，门急诊及时就诊。", "出院目的地：居家", "患者照护需求：注意休息，避免感染、劳累", "医师签名："]
2026-08-10 17:35:32,219 INFO     29 [qwen-vl-parser] page=5 text: 23 lines (bbox 141-163)
2026-08-10 17:35:32,219 INFO     29 [qwen-vl-parser] page=5 text: 23 sections
2026-08-10 17:35:32,352 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=959958, prompt_len=764
2026-08-10 17:35:33,597 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:35:33,599 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 17:35:33,614 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=959958, prompt_len=401
2026-08-10 17:35:37,310 INFO     29 [qwen-vl-parser] text API response (len=643):
["门（急）诊病历", "初诊", "科室", "日期:2026-02-02 09:07", "医学", "性别:男", "年龄:75岁", "出生日期:1950-09-13", "主诉:肺癌靶向治疗5年复查。", "现病史:肺癌吉非替尼治疗3个月,因肝功异常更换泰瑞沙靶向治疗至今5年,外院肺CT提示病灶增大", "既往史:无肺结核病史。", "个人史:无不良嗜好。", "家族史:无遗传病史。", "体 检:双肺呼吸音清,未闻及干湿性啰音。", "辅助检查:2026-01-30 组织病理学检查与诊断[免费用](左肺组织穿刺活检)非小细胞肺癌伴大片坏死,", "结合形态学及免疫组化,符合腺癌。免疫组化示肿瘤细胞:CKpan(+),CK7(+),TTF-", "1(+),p40(-),CK5/6(-);特殊染色:D-PAS(-)。", "初步诊断:肺恶性肿瘤", "诊疗计划:分子病理检测", "甲磺酸奥希替尼片(泰瑞沙2)(80mg*30),剂量:80MG,用法:口服,频率:每日1次,疗程:1天,", "温馨提示:此病历只打印一次,请妥善保管!", "第1页 共2页", "打印时间:2026-03-02 12:50:46", "门（急）诊病历", "初诊", "科", "日期:2026-02-02 09:07", "姓名", "性别:男", "年龄:75岁", "出生日期:1950-09-13", "医师签名：", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 17:35:37,311 INFO     29 [qwen-vl-parser] page=6 text: 34 lines (bbox 164-197)
2026-08-10 17:35:37,311 INFO     29 [qwen-vl-parser] page=6 text: 34 sections
2026-08-10 17:35:37,461 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=766959, prompt_len=764
2026-08-10 17:35:38,803 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2020-12-25"}
```
2026-08-10 17:35:38,803 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2020-12-25
2026-08-10 17:35:38,814 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=766959, prompt_len=401
2026-08-10 17:35:42,277 INFO     29 [qwen-vl-parser] text API response (len=655):
["报告状态", "收到日期", "数据来源", "床号", "图像", "1份已审核", "2026-01-30 14:10:13", "4.0", "无", "已审核", "2026-01-28 09:16:53", "4.0", "55", "无", "2审核", "2020-12-28 12:02", "2.0", "58床", "无", "2份已审核", "2020-12-21 14:02", "2.0", "58床", "无", "共1页，共4条记录", "门诊号：-", "姓名", "性别", "男", "年龄", "70岁", "病人编号", "病区", "病案号", "门诊号", "送检科室", "送检单位", "送检医生", "标本名称", "左侧隆突粘膜、左肺BALF等", "临床诊断", "肺部阴影", "病理诊断", "(左侧隆突粘膜)非小细胞肺癌，结合免疫组化结果，符合腺癌；", "(左肺BALF)细胞蜡块内发现少量恶性肿瘤细胞；", "(左肺BALF)涂片内未发现恶性肿瘤细胞；", "(痰)涂片内发现少量可疑恶性肿瘤细胞。", "免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。", "报告医生", "复诊医生", "报告时间", "2020-12-25", "12:51", "2026-03-02"]
2026-08-10 17:35:42,277 INFO     29 [qwen-vl-parser] page=7 text: 54 lines (bbox 198-251)
2026-08-10 17:35:42,277 INFO     29 [qwen-vl-parser] page=7 text: 54 sections


2026-08-10 17:35:42,396 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=550943, prompt_len=764
2026-08-10 17:35:43,728 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2020-12-29"}
```
2026-08-10 17:35:43,728 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2020-12-29
2026-08-10 17:35:43,736 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=550943, prompt_len=401
2026-08-10 17:35:46,436 INFO     29 [qwen-vl-parser] text API response (len=478):
["责任医生", "门诊号", "状态", "售到日期", "费用来源", "床号", "回路", "2020-01-30 14:10:13", "4.0", "无", "2020-01-28 09:10:53", "4.0", "55", "毛", "1费已审核", "2020-12-28 12:02", "2.0", "58床", "无", "2费已审核", "2020-12-21 14:02", "2.0", "58床", "无", "下一页", "显示", "共1页,共4条已查", "病理号", "住院", "门诊号", "1-1]", "姓名", "70岁", "病人编号", "0007", "病区", "门诊号", "送检科室", "送检医生", "标本名称", "左侧隆突粘膜、左肺BALF等", "临床诊断", "肺部阴影", "病理诊断", "2020.12.20加做免疫结果：PD-L1-22C3（+，TPS约30%）", "报告医生", "报告时间", "2020-12-29", "12:51", "2026-03-02"]
2026-08-10 17:35:46,437 INFO     29 [qwen-vl-parser] page=8 text: 50 lines (bbox 252-301)
2026-08-10 17:35:46,438 INFO     29 [qwen-vl-parser] page=8 text: 50 sections


2026-08-10 17:35:46,561 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=557447, prompt_len=764
2026-08-10 17:35:47,884 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2020-12-30"}
```
2026-08-10 17:35:47,885 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=2020-12-30
2026-08-10 17:35:47,894 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=557447, prompt_len=401
2026-08-10 17:36:02,148 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:36:02.147+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:36:35,449 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:36:35.449+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:37:07,549 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:37:07.546+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:37:39,558 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:37:39.555+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:37:57,272 INFO     29 [qwen-vl-parser] text API response (len=29393):
["性别：男", "年龄：70岁", "住院号：", "费", "报告状态：已审核", "登记日期：2020-01-30 14:10:13", "检验来源：1.0", "床号：", "图像：无", "报告状态：已审核", "登记日期：2020-01-28 08:10:53", "检验来源：1.0", "床号：55", "图像：无", "报告状态：已审核", "登记日期：2020-12-28 12:02", "检验来源：2.0", "床号：58床", "图像：无", "报告状态：已审核", "登记日期：2020-12-21 14:02", "检验来源：2.0", "床号：58床", "图像：无", "1 页 下一", "当前病人", "病理号", "门诊号：", "姓名：", "病区：", "住院科室：", "标本名称：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断���", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "病理诊断：", "
2026-08-10 17:37:57,287 INFO     29 [qwen-vl-parser] page=9 text: 3257 lines (bbox 302-3558)
2026-08-10 17:37:57,287 INFO     29 [qwen-vl-parser] page=9 text: 3257 sections
2026-08-10 17:37:57,411 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=537069, prompt_len=764
2026-08-10 17:37:58,721 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-28"}
```
2026-08-10 17:37:58,722 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2026-01-28
2026-08-10 17:37:58,751 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=537069, prompt_len=401
2026-08-10 17:38:01,348 INFO     29 [qwen-vl-parser] text API response (len=453):
["改检病查", "费尚增写", "报告状态", "咨询日期", "链签来源", "读号", "图像", "34", "巴油境", "2026-01-00 14:10:13", "4.0", "巴油境", "2026-01-28 00:10:53", "4.0", "55", "毛", "t巴油境", "2026-12-28 13:02", "2.0", "50", "毛", "5巴油境", "2026-12-21 14:02", "2.0", "50", "毛", "一页", "显示", "页", "门楼号", "姓名", "病区", "送检科室", "标本名称", "临床诊断", "内眼所见", "穿刺组织3条，合计长0.6cm。", "病理诊断", "(左肺组织穿刺活检）非小细胞肺癌伴大片坏死，待免疫组化。", "报告医生", "审核医生", "报告时间", "2026-01-28 14:53", "点击要返回的Pah:QC流程", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 17:38:01,348 INFO     29 [qwen-vl-parser] page=10 text: 46 lines (bbox 3559-3604)
2026-08-10 17:38:01,348 INFO     29 [qwen-vl-parser] page=10 text: 46 sections
2026-08-10 17:38:01,477 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=635054, prompt_len=764
2026-08-10 17:38:04,960 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-30"}
```
2026-08-10 17:38:04,961 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2026-01-30
2026-08-10 17:38:04,970 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=635054, prompt_len=401
2026-08-10 17:38:08,213 INFO     29 [qwen-vl-parser] text API response (len=598):
["门诊号", "病区", "送检科室", "原病理号", "报告状态", "收到日期", "数据来源", "床号", "图像", "审核", "2026-01-30 14:10:13", "4.0", "无", "已审核", "2026-01-28 09:16:53", "4.0", "55", "无", "2020-12-28 12:02", "2.0", "58床", "无", "2020-12-21 14:02", "2.0", "58床", "无", "共1页，共4条记录", "门诊号：", "姓名", "性别", "75岁", "病人编", "病区", "病区", "病案号", "门诊号", "送检科室", "送检单位", "送检医生", "丁晓倩", "标本名称", "左肺组织穿刺活检", "临床诊断", "1.肺恶性肿瘤2.肺恶性肿瘤", "病理诊断", "(左肺组织穿刺活检)肺小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合肺癌。", "免疫组化示肿瘤细胞：CKpan（+），CK7（+），TTF-1（+），p40（-），CK5/6（-）；", "特殊染色：D-PAS（-）。", "报告医生", "医生", "报告时间", "2026-01-30 11:19", "欢迎使用朗珈PathQC病理质控与资料管理系统！", "12:51", "2026-01-02"]
2026-08-10 17:38:08,214 INFO     29 [qwen-vl-parser] page=11 text: 55 lines (bbox 3605-3659)
2026-08-10 17:38:08,214 INFO     29 [qwen-vl-parser] page=11 text: 55 sections
2026-08-10 17:38:08,358 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=810423, prompt_len=764
2026-08-10 17:38:09,808 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-06"}
```
2026-08-10 17:38:09,808 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2026-02-06
2026-08-10 17:38:09,826 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=810423, prompt_len=401
2026-08-10 17:38:11,637 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:38:11.636+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:38:13,799 INFO     29 [qwen-vl-parser] text API response (len=790):
["病历", "姓名", "病区", "送检科室", "标本名称", "临床诊断", "病理诊断", "检查项目:肿瘤多基因检测(含MSI)", "检查方法:高通量测序(NGS)", "参考基因组:GRCh37/hg19", "临床数据库:1000 Genomes、ExAC、gnomAD、ClinVar、BRCA Exchange InSiGHT、DBSNP、Cancer Hotspots、COSMIC、JAX CKB、OncoKB等", "检测突变软件:ADXHS-Classic-H", "标本病理评估:肿瘤细胞占比30%。", "DNA质量评估:合格", "测序质量评估:合格", "表格结果:", "检测内容 检测结果 突变丰度 备注", "MSI MSS 0/55", "EGFR exon19 c.2235_2249del p.Glu746_Ala750del(E746_A750del) 29.59% I级,具有明确临床意义", "MET 扩增 3.97 I级,具有明确临床意义", "TP53 exon8 p.817C>T p.Arg273Cys(R273C) 6.35% II级,具有潜在临床意义", "检测结果备注:表格内未列出的为未检出。", "报告医生", "生", "报告时间", "2026-02-06 16:26", "住院号", "门诊号", "送检医生", "病人编号", "1份已审核", "2026-01-30 14:10:13", "4.0", "无", "2份已审核", "2026-01-28 09:16:53", "4.0", "55", "无", "1份已审核", "2020-12-28 12:02", "2.0", "58床", "无", "2020-12-21 14:02", "2.0", "58床", "无", ""]
2026-08-10 17:38:13,799 INFO     29 [qwen-vl-parser] page=12 text: 48 lines (bbox 3660-3707)
2026-08-10 17:38:13,799 INFO     29 [qwen-vl-parser] page=12 text: 48 sections
2026-08-10 17:38:13,948 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=966315, prompt_len=764
2026-08-10 17:38:15,295 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-06"
}
```
2026-08-10 17:38:15,296 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=2026-02-06
2026-08-10 17:38:15,313 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=966315, prompt_len=401
2026-08-10 17:38:19,002 INFO     29 [qwen-vl-parser] text API response (len=783):
["分子病理检查报告单", "编", "患者姓名", "性别：男", "年龄：75岁", "住院号：", "送检科室", "尿府理", "登记号：", "标本类型：石蜡组织", "病变部", "病理诊断：", "收到日期：2026-01-20", "检查项目：肿瘤多基因检测（含MSI）", "检查方法：高通量测序(NGS)", "参考基因组：GRCh37/hg19", "临床数据库：1000 Genomes、ExAC、gnomAD、ClinVar、BECA Exchange InSiGHT、DBSNP、", "Cancer Hotspots、COSMIC、JAX CXB、OncoKB等", "检测突变软件：ADXHS-Classic-H", "标本病理评估：肿瘤细胞占比30%。", "核酸质量评估：合格", "测序质量评估：合格", "检测结果：", "检测内容", "检测结果", "突变丰度", "备注", "MSI", "MSS", "0/55", "", "EGFR", "exon19 c.2235_2249del", "29.59%", "I级、具有明确临床意义", "p.Glu746_Ala750del (E746_A750del)", "MET", "3'端", "3.97", "I级、具有明确临床意义", "TP53", "exon6 c.817C>T p.Arg273Cys (R273C)", "6.35%", "II级、具有潜在临床意义", "备注：表格内未列出的为未检出。", "注：此报告仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与分子病理诊断科联系。", "报告.", "检测者", "报告日期：2026-02-06", "第1页/共16页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 17:38:19,002 INFO     29 [qwen-vl-parser] page=13 text: 51 lines (bbox 3708-3758)
2026-08-10 17:38:19,002 INFO     29 [qwen-vl-parser] page=13 text: 51 sections
2026-08-10 17:38:19,199 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1622180, prompt_len=764
2026-08-10 17:38:20,552 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:38:20,553 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-10 17:38:20,571 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1622180, prompt_len=401
2026-08-10 17:38:27,484 INFO     29 [qwen-vl-parser] text API response (len=1422):
["V2.0", "循环周期，调节转录，DNA 复", "制和诱导细胞程序死亡及抗血", "管生成。", "细胞瘤）和肾上腺皮质癌。TP53 突变还发生于包括 CML、", "ANLL、MDS 及 B-NHL。在内的多种恶性血液肿瘤以及", "黑色素瘤、基底细胞癌、鳞状细胞癌等皮肤癌等多种类型", "肝癌及恶性肿瘤。TP53 突变是多种癌症预后不良的标", "志，如乳腺癌。TP53 基因变异与肿瘤细胞对铂类化疗药", "物耐药性相关，但不影响氟杉醇类药物的敏感性；相关化", "疗药物还包括喜树碱、5-FU、顺铂、环磷酰胺等。FDA 已", "授予 IXC14586 快速通道资格，目前治疗具有 TP53 Y220C", "突变的局部晚期或转移性实体瘤患者。", "四、声明告知", "1. 本检测项目中使用的参考基因组版本为 hg19，报告中的变异命名遵从 HGVS 指南", "(http://varnomcn.hgvs.org)中的相关规定进行命名。", "2. 变异分类：综合变异在治疗、诊断和预后方面相关研究证据，将变异分为 4 级：I", "级为明确临床意义；II 级为潜在临床意义；III 类为临床意义未明；IV 级为良性/可能良", "性。本报告中仅列出 I-III 级变异。", "3. 检测结果与临床意义相关性的证据水平分为 4 个等级（A/B/C/D）。A 级：对应", "病种中 FDA/NMPA 批准或指南推荐的治疗、诊断和（或）预后的相关标志物；B 级：专家", "共识或 III/IV 期临床试验研究表明对患者肿瘤治疗有敏感或耐药、或具有诊断、预后意义", "的生物标志物；C 级：FDA/NMPA 批准或专业指南推荐的在其他癌种对某个治疗方案敏感", "或耐药的标志物；或者是作为临床试验入组标准的标志物；或者是多个小型研究结果证实", "具有诊断或预后意义的标志物；D 级：临床前研究表明具有潜在的治疗意义，或基于小型", "研究或多个案例报告可能作为辅助疾病诊断或预后的标志物（结论未形成共识）。", "4. 本检测的检测内容大部分基于仅限于 DNA 水平，部分基因涉及 RNA 水平，但", "不涉及蛋白水平的检测。", "5. 对于组织样品，如样本中肿瘤细胞含量低于 20%，可能影响检测结果的准确性；", "如未检出指定的基因变异，可能由于该样本中该突变的丰度低于本项目的检测下限。", "6. 对于组织样品，肿瘤存在异质性，即不同病灶甚至同一病灶内的组织的突变图谱可", "能也存在差异；另外，不同疾病发展或治疗阶段取出的样本中的突变可能不同；因此，本", "检测报告仅对此次送检的样本负责。并且，所检测的突变位点仅限于本检测试剂的检测范", "围，样品的基因组中可能存在的某些罕见或复杂突变，本项目不能完全检测。", "7. 本报告对于测序结果分析中核苷酸改变的位置信息是基于当前版本的基因组和转录", "本，随着人类基因组的更新，这些信息可能会有所不同；同时对于突变位点的解读，是基", "于当前已发表的文献、指南、公共数据库及临床研究结果，随着研究的发展，特定位点的", "解读可能发生变更。", "8. 本检测仅为临床治疗或诊断提供参考，具体的诊断结果及治疗决策应由临床医生综", "合患者的各种临床信息和检测结果进行判断。", "CS 扫描全能王", "3 亿人都在用的扫描 App"]
2026-08-10 17:38:27,484 INFO     29 [qwen-vl-parser] page=14 text: 42 lines (bbox 3759-3800)
2026-08-10 17:38:27,484 INFO     29 [qwen-vl-parser] page=14 text: 42 sections
2026-08-10 17:38:27,706 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1927079, prompt_len=764
2026-08-10 17:38:29,100 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-27"}
```
2026-08-10 17:38:29,101 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=2026-01-27
2026-08-10 17:38:29,118 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1927079, prompt_len=401
2026-08-10 17:38:35,197 INFO     29 [qwen-vl-parser] text API response (len=877):
["超声检查报告单", "思者登", "姓", "性别：男", "年龄：75岁", "床号：A02", "检查所见：", "右肝最大斜径12.8cm，左肝前后径6.4cm，上下径7.5cm，肝表面光滑，边缘规则，肝内", "呈细小点状回声，分布欠均匀，肝内见数个囊性回声，大者0.8x0.5cm，均透声可。", "空腹胆囊充盈差，胆囊区见胆囊祥回声，大小约3.4x1.4cm，腔内透声差，充满细密点", "状回声。", "胆总管内径0.5cm，未见明显异常回声，肝内胆管无明显扩张。", "胰腺大小形态可，表面光滑，内回声均匀，主胰管内径不宽。", "脾未探及。", "门静脉走行自然，呈入肝血流，门静脉主干内径1.0cm，入肝血流速度17.4cm/s，肝内", "门静脉血流充盈好，未见明显异常回声。", "肝静脉走行自然，各支内径不宽，腔内未见明显异常回声，血流速及频谱形态未见异", "常。", "双侧肾上腺区未见明显占位性病变。", "双肾大小形态正常，表面光滑，皮髓质分界清，左肾实质回声无明显异常，右肾中部实", "质内见1.5x1.2cm略高回声结节，边界清，双肾窦无分离扩张。", "双侧输尿管无明显扩张。", "膀胱充盈可，黏膜光滑，腔内未见明显占位。", "前列腺大小约4.0（左右径）×3.5（前后径）×3.2（上下径）cm，体积约23.3cm3，", "表面光滑，中叶略突，内部回声欠均匀。", "双侧精囊腺无肿大，内部回声均匀。", "双肾动脉主干血流通畅，肾内动脉血流分布好。", "左肾叶间动脉Vs 24.8cm/s，阻力指数（RI）0.66。", "右肾叶间动脉Vs 25.1cm/s，阻力指数（RI）0.65。", "超声提示：脾切除术后", "空腹胆囊充盈差、腔内透声差，慢性胆囊炎？请结合临床", "肝囊肿", "右肾略高回声结节，考虑良性（结合病史考虑复杂囊肿可能）", "前列腺增生并钙化", "报告日期：2026-01-27 08:35:35 记录人", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 17:38:35,199 INFO     29 [qwen-vl-parser] page=15 text: 37 lines (bbox 3801-3837)
2026-08-10 17:38:35,199 INFO     29 [qwen-vl-parser] page=15 text: 37 sections
2026-08-10 17:38:36,566 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=878226, prompt_len=764
2026-08-10 17:38:37,890 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-27"}
```
2026-08-10 17:38:37,891 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=2026-01-27
2026-08-10 17:38:37,909 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=878226, prompt_len=401
2026-08-10 17:38:40,103 INFO     29 [qwen-vl-parser] text API response (len=375):
["超声检查报告单", "患者登记", "姓名：", "性别：男", "年龄：75岁", "号", "1", "2", "检查所见：", "甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。", "甲状旁腺区未见明显异常回声。", "左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门", "髓结构不清，CDFI：内见条状血流信号。", "右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。", "超声提示：左侧颈部淋巴结肿大，考虑“M”性可能", "报告日期：2026-01-27 08:26:34 记", "名.", "注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 17:38:40,104 INFO     29 [qwen-vl-parser] page=16 text: 20 lines (bbox 3838-3857)
2026-08-10 17:38:40,104 INFO     29 [qwen-vl-parser] page=16 text: 20 sections
2026-08-10 17:38:40,239 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=979296, prompt_len=764
2026-08-10 17:38:41,566 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 17:38:41,567 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=None
2026-08-10 17:38:41,587 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=979296, prompt_len=401
2026-08-10 17:38:43,712 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:38:43.712+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:38:44,927 INFO     29 [qwen-vl-parser] text API response (len=584):
["影像学检查报告单", "扫一扫查看云胶片（访问码）：", "姓名：", "性别：男", "年龄：75岁", "影像", "住院号：", "登记号：", "检查名称：胸部CT增强成像（单独）", "检查方法：AXI+C", "图像所见：胸廓及胸腔容积基本正常。纵隔左偏。左肺可见软组织密度肿块，边界不", "清，大小约59mm*66mm，较前2024.09.03CT所示明显增大，呈不均匀强", "化。左主支气管及左肺上叶、下叶支气管狭窄，其远端肺组织实变，较前", "相仿。左肺下叶后基底段(6im53-54)见实性结节，大小约为11mm×8mm。", "双肺见多发小、微结节，较大者位于左肺下叶背段(6im39-41)，呈实性", "密度，大小约为9mm×7mm。双肺见多发斑片、索条影。气管未见狭窄或梗", "阻。纵隔及左肺门可见多发肿大淋巴结，较前相仿。心影未见明显增大。", "左侧部分肋骨局部形态不规整。", "印象：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床", "双肺多发结节，较前增多、增大，请结合临床随访", "双肺慢性炎症或纤维灶可能性大，请结合临床", "左侧部分肋骨局部形态不规整，请结合临床", "报告医师", "审核医", "该报告仅供临床医师参考；如需商榷，请通过临床医师与审核医师沟通", "流水号", ""]
2026-08-10 17:38:44,928 INFO     29 [qwen-vl-parser] page=17 text: 26 lines (bbox 3858-3883)
2026-08-10 17:38:44,928 INFO     29 [qwen-vl-parser] page=17 text: 26 sections
2026-08-10 17:38:45,039 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=694850, prompt_len=764
2026-08-10 17:38:46,431 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 17:38:46,432 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=None
2026-08-10 17:38:46,441 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=694850, prompt_len=401
2026-08-10 17:38:48,831 INFO     29 [qwen-vl-parser] text API response (len=405):
["影像学检查报告单", "姓名：", "性别：男", "年龄：70岁", "影像", "检查日期：2020-12-23", "报告日期：2020-12-23", "报告时间：10.00", "检查名称：全身骨显像", "检查方法：显像剂：99mTc-MDP", "图像所见：静脉注射显像剂2小时后行全身骨显像，图像清晰，对比度可。", "前位：双侧膝关节见显像剂浓聚灶。颅骨，锁骨，胸骨，前肋，骨盆显像", "剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。", "后位：脊椎见显像剂浓聚灶。颅骨，肩胛骨，后肋，骨盆显像剂分布基本", "左右对称，未见明显异常显像剂浓聚或稀疏区。", "印", "象：1，脊椎及双侧膝关节退行性变可能性大", "2，其余部位骨骼未见明显转移瘤，建议定期复查", "报告[", "审核医师：", "该报告反映受检者当时情况，仅供临床医师参考。", "流水号", "胶片"]
2026-08-10 17:38:48,832 INFO     29 [qwen-vl-parser] page=18 text: 23 lines (bbox 3884-3906)
2026-08-10 17:38:48,832 INFO     29 [qwen-vl-parser] page=18 text: 23 sections
2026-08-10 17:38:48,925 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=542144, prompt_len=764
2026-08-10 17:38:50,276 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 17:38:50,277 INFO     29 [qwen-vl-parser] page=19 classify=text report_date=None
2026-08-10 17:38:50,294 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=542144, prompt_len=401
2026-08-10 17:38:52,587 INFO     29 [qwen-vl-parser] text API response (len=415):
["影像学检查报告单", "扫码看电子胶片", "姓", "性别：男", "年龄：70岁", "影像", "科", "住院", "检查日期：2020-12-22", "报告日期：2020-12-23", "报告时间：14:22:52", "登记号", "40", "检查名称：颅脑MR平扫成像+DWI成像", "检查方法：AXI:FSE T1WI, T2WI, FLAIR, DWI", "SAG:FSE T1WI", "图像所见：双侧额顶叶白质可见散在斑点状等T1稍长T2信号影，FLAIR为高信号，", "DWI为等信号。脑室系统略扩大，脑沟、脑池明显加深，中线结构居中。", "印象：1. 血管性脱髓鞘（Fazekas 1级），请结合临床复查", "2. 老年性脑改变", "报告", "审核医师：", "该报告反映受检者当时情况，仅供临床医师参考。", "流水号", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 17:38:52,588 INFO     29 [qwen-vl-parser] page=19 text: 26 lines (bbox 3907-3932)
2026-08-10 17:38:52,589 INFO     29 [qwen-vl-parser] page=19 text: 26 sections
2026-08-10 17:38:52,754 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1040877, prompt_len=764
2026-08-10 17:38:54,177 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-27"}
```
2026-08-10 17:38:54,177 INFO     29 [qwen-vl-parser] page=20 classify=text report_date=2026-01-27
2026-08-10 17:38:54,190 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1040877, prompt_len=401
2026-08-10 17:38:56,167 INFO     29 [qwen-vl-parser] text API response (len=323):
["超声检查报告单", "患者", "性别：男", "年龄：75岁", "检查所见：", "甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。", "甲状旁腺区未见明显异常回声。", "左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门", "髓结构不清，CDFI：内见条状血流信号。", "右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。", "超声提示：左侧颈部淋巴结肿大，考虑“Ⅱ”性可能", "报告日期：2026-01-27 08:26:34 记录", "师", "注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。"]
2026-08-10 17:38:56,168 INFO     29 [qwen-vl-parser] page=20 text: 14 lines (bbox 3933-3946)
2026-08-10 17:38:56,168 INFO     29 [qwen-vl-parser] page=20 text: 14 sections
2026-08-10 17:38:56,557 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2943484, prompt_len=764
2026-08-10 17:38:58,107 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-01-26"
}
```
2026-08-10 17:38:58,108 INFO     29 [qwen-vl-parser] page=21 classify=text report_date=2026-01-26
2026-08-10 17:38:58,121 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2943484, prompt_len=401
2026-08-10 17:39:00,779 INFO     29 [qwen-vl-parser] text API response (len=375):
["心电图报告单", "性别：男", "年龄：75岁", "危重症医学科率：69 bpm", "P-R间期：139 ms", "QRS时间：90 ms", "QT/QTc : 414/445 ms", "P-R-T : 63/22/25 度", "SV1/RV5:0.49/1.35 mV", "RV5+SV1:1.84mV", "诊断：大致正常心电图", "检查时间：2026-01-26 10:31:55", "检查医生：", "I", "II", "III", "AVR", "AVL", "AVF", "V1", "V2", "V3", "V4", "V5", "V6", "检查者：", "25 mm/s 10 mm/mv", "报告审核", "时间：2026-01-26 10:35:22", "以上结果请结合临床及前图", "1/1"]
2026-08-10 17:39:00,780 INFO     29 [qwen-vl-parser] page=21 text: 31 lines (bbox 3947-3977)
2026-08-10 17:39:00,780 INFO     29 [qwen-vl-parser] page=21 text: 31 sections

2026-08-10 17:39:00,951 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=917232, prompt_len=764
2026-08-10 17:39:02,385 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2020-01-07"}
```
2026-08-10 17:39:02,386 INFO     29 [qwen-vl-parser] page=22 classify=table report_date=2020-01-07
2026-08-10 17:39:02,413 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=917232, prompt_len=756
2026-08-10 17:39:15,742 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:39:15.739+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:39:47,813 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:39:47.811+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:40:19,834 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:40:19.833+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:40:51,906 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:40:51.905+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:41:12,018 INFO     29 [qwen-vl-parser] table API response (len=28402):
\begin{tabular}{cccccccccc}
\hline
\multicolumn{10}{c}{\textbf{检验报告单 (血型尿常规)}} \\
\hline
\multicolumn{2}{c}{姓名} & \multicolumn{2}{c}{四四库呼呼与抗重球球学目} & \multicolumn{2}{c}{床 号:} & \multicolumn{2}{c}{号:} & \multicolumn{2}{c}{号:} \\
\multicolumn{2}{c}{性别} & \multicolumn{2}{c}{10001100101} & \multicolumn{2}{c}{标本种类:} & \multicolumn{2}{c}{李曲} & \multicolumn{2}{c}{标本状态:} \\
\multicolumn{2}{c}{年龄} & \multicolumn{2}{c}{1001000} & \multicolumn{2}{c}{临床诊断:} & \multicolumn{2}{c}{脑垂体肿瘤} & \multicolumn{2}{c}{} \\
\hline
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{生物参考区间} & \multicolumn{2}{c}{单位} & \multicolumn{2}{c}{日} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{生物参考区间} & \multicolumn{2}{c}{单位} \\
\hline
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{35} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \mult
2026-08-10 17:41:12,021 INFO     29 [qwen-vl-parser] page=22 table: 132 LaTeX lines (bbox 3978-4109)
2026-08-10 17:41:12,022 INFO     29 [qwen-vl-parser] page=22 table: 132 sections
2026-08-10 17:41:12,165 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=999262, prompt_len=764
2026-08-10 17:41:13,620 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-27"
}
```
2026-08-10 17:41:13,620 INFO     29 [qwen-vl-parser] page=23 classify=table report_date=2026-01-27
2026-08-10 17:41:13,636 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=999262, prompt_len=756
2026-08-10 17:41:23,962 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:41:23.961+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:41:24,194 INFO     29 [qwen-vl-parser] table API response (len=1927):
\begin{tabular}{llllllllll}
\hline
\multicolumn{2}{l}{质评合格,省内参考} & \multicolumn{4}{l}{} & \multicolumn{4}{l}{采集时间:} \\
\multicolumn{2}{l}{住院} & \multicolumn{4}{l}{} & \multicolumn{4}{l}{} \\
\multicolumn{2}{l}{尿干化学,尿有形成分分析} & \multicolumn{4}{l}{} & \multicolumn{4}{l}{采集人员:} \\
\multicolumn{2}{l}{} & \multicolumn{4}{l}{} & \multicolumn{4}{l}{} \\
\hline
\multicolumn{2}{l}{姓} & 科 & \multicolumn{2}{l}{.学科} & 床 & 气 & \multicolumn{2}{l}{样本编} & \\
\multicolumn{2}{l}{性} & 别: 男 & \multicolumn{2}{l}{病人} & \multicolumn{2}{l}{标本种类: 尿液} & \multicolumn{2}{l}{标本性状:} & \\
\multicolumn{2}{l}{年} & 龄: 75岁 & \multicolumn{2}{l}{住院} & \multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \multicolumn{2}{l}{} & \\
\hline
NO & 项 & 目 & 结果 & 生物参考区间 & 单位 & NO & 项 & 目 & 结果 \\
\hline
1 & 白细胞 & -- & 阴性 & 20 & 电导率 & 16.3 & 3.0-39.0 & mS/cm & \\
2 & 隐血 & -- & 阴性 & 21 & 红细胞信息 & -- & 阴性 & & \\
3 & 蛋白 & -- & 阴性 & & & & & & \\
4 & 葡萄糖 & -- & 阴性 & & & & & & \\
5 & PH & 6.5 & 4.5-8.0 & & & & & & \\
6 & 比重 & 1.016 & 1.003-1.030 & & & & & & \\
7 & 酮体 & -- & 阴性 & & & & & & \\
8 & 胆红素 & -- & 阴性 & & & & & & \\
9 & 尿胆原 & 正常 & 阴性-弱阳性 & & & & & & \\
10 & 亚硝酸盐 & -- & 阴性 & & & & & & \\
11 & 浊度 & 清亮 & & & & & & & \\
12 & 白细胞计数 & 2.4 & 0.0-25.0 & /uL & & & & & \\
13 & 红细胞计数 & 3.2 & 0.0-23.0 & /uL & & & & & \\
14 & 上皮细胞计数 & 0.4 & 0.0-31.0 & /uL & & & & & \\
15 & 管型计数 & 0.0 & 0.0-2.0 & /uL & & & & & \\
16 & 小圆上皮细胞 & 0.4 & 0.0-3.0 & /uL & & & & & \\
17 & 类酵母细胞 & -- & 0.0-0.0 & & & & & & \\
18 & 结晶检查 & 0.0 & 0.0-10.0 & /uL & & & & & \\
19 & 细菌计数 & 8.5 & 0.0-1200.0 & /uL & & & & & \\
\hline
\multicolumn{10}{l}{备注:} \\
\hline
\multicolumn{2}{l}{接收时间: 2026-01-27 08:37} & \multicolumn{2}{l}{报告时间:} & \multicolumn{2}{l}{2026-01-27 08:59} & \multicolumn{4}{l}{检验者:} \\
\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \multicolumn{2}{l}{送检医} & \multicolumn{6}{l}{} \\
\multicolumn{10}{l}{本报告仅对本次检验标本负责,如对检验结果有疑问,请与相关院区检验科联系!} \\
\multicolumn{10}{r}{第1页 共1页} \\
\hline
\end{tabular}
2026-08-10 17:41:24,196 INFO     29 [qwen-vl-parser] page=23 table: 42 LaTeX lines (bbox 4110-4151)
2026-08-10 17:41:24,197 INFO     29 [qwen-vl-parser] page=23 table: 42 sections
2026-08-10 17:41:24,324 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=822864, prompt_len=764
2026-08-10 17:41:25,779 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-27"
}
```
2026-08-10 17:41:25,779 INFO     29 [qwen-vl-parser] page=24 classify=table report_date=2026-01-27
2026-08-10 17:41:25,793 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=822864, prompt_len=756
2026-08-10 17:41:33,167 INFO     29 [qwen-vl-parser] table API response (len=1796):
\begin{tabular}{llllllll}
\hline
\multicolumn{2}{l}{质评合格,省内参考} & \multicolumn{4}{c}{\textbf{检验报告}} & \multicolumn{2}{r}{采集时间:} \\
\multicolumn{2}{l}{住院} & \multicolumn{4}{c}{} & \multicolumn{2}{r}{2026-01-27 05:46} \\
\multicolumn{2}{l}{D-二聚体,血浆抗凝血酶AT} & \multicolumn{4}{c}{} & \multicolumn{2}{r}{采集} \\
\hline
\multicolumn{1}{l}{姓} & \multicolumn{1}{l}{名} & \multicolumn{1}{l}{别} & \multicolumn{1}{l}{床} & \multicolumn{1}{l}{号.} & \multicolumn{1}{l}{样本编} & \multicolumn{2}{l}{} \\
\multicolumn{1}{l}{性} & \multicolumn{1}{l}{} & \multicolumn{1}{l}{ID:} & \multicolumn{1}{l}{标本种类:} & \multicolumn{1}{l}{血浆} & \multicolumn{1}{l}{标本性状.} & \multicolumn{2}{l}{} \\
\multicolumn{1}{l}{年} & \multicolumn{1}{l}{龄: 75岁} & \multicolumn{1}{l}{号} & \multicolumn{1}{l}{临床诊断:} & \multicolumn{1}{l}{肺恶性肿瘤} & \multicolumn{2}{l}{} & \multicolumn{1}{l}{} \\
\hline
\textbf{项} & \textbf{目} & \textbf{中} & \textbf{不} & \textbf{提示} & \textbf{生物参考区间} & \textbf{单位} & \\
\hline
1 & 凝血酶原时间 & 13.2 & & & 10.0-14.0 & sec & \\
2 & PT-国际标准化比值 & 1.13 & & & 0.80-1.20 & INR & \\
3 & PT百分活度 & 84 & & & 80-200 & \% & \\
4 & 活化部分凝血活酶时间 & 31.8 & & & 22.0-38.0 & sec & \\
5 & APTT比值 & 1.12 & & & 0.73-1.27 & R & \\
6 & 凝血酶时间 & 18.1 & & & 14.0-21.0 & sec & \\
7 & TT比值 & 1.06 & & & 0.82-1.23 & R & \\
8 & 纤维蛋白原 & 5.80 & $\uparrow$ & & 2.0-4.0 & g/L & \\
9 & 抗凝血酶III & 96 & & & 82-121 & \% & \\
10 & D-二聚体测定 & 550 & $\uparrow$ & & 0-500 & ng/ml & \\
\hline
\multicolumn{8}{l}{备注:} \\
\hline
\multicolumn{2}{l}{接收时间: 2026-01-27 07:13} & \multicolumn{2}{l}{报告时间: 2026-01-27 11:05} & \multicolumn{2}{l}{检验者:} & \multicolumn{2}{l}{审核者:} \\
\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \multicolumn{2}{l}{送检医} & \multicolumn{4}{l}{} \\
\multicolumn{8}{l}{本报告仅对本次检验标本负责,如对检验结} & \multicolumn{4}{l}{\textbf{第1页 共1页}} \\
\hline
\end{tabular}
2026-08-10 17:41:33,168 INFO     29 [qwen-vl-parser] page=24 table: 31 LaTeX lines (bbox 4152-4182)
2026-08-10 17:41:33,168 INFO     29 [qwen-vl-parser] page=24 table: 31 sections
2026-08-10 17:41:33,308 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038485, prompt_len=764
2026-08-10 17:41:34,793 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-27"
}
```
2026-08-10 17:41:34,794 INFO     29 [qwen-vl-parser] page=25 classify=table report_date=2026-01-27
2026-08-10 17:41:34,812 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038485, prompt_len=756
2026-08-10 17:41:36,452 INFO     29 [qwen-vl-parser] table API response (len=278):
\begin{tabular}{lllllll}
\hline
项 & 目 & 结果 & 提示 & 生物参考区间 & 单位 \\
\hline
1 & 乙型肝炎表面抗原(化学发光法) & 0.00 & 阴性 & $<$0.05 & IU/ml \\
2 & 丙型肝炎抗体 & 0.07 & 阴性 & $<$1 & S/CO \\
3 & HIV抗体/p24抗原 & 0.13 & 阴性 & $<$1.00 & S/CO \\
4 & 梅毒螺旋体抗体 & 0.08 & 无反应 & $<$1.00 & S/CO \\
\hline
\end{tabular}
2026-08-10 17:41:36,454 INFO     29 [qwen-vl-parser] page=25 table: 11 LaTeX lines (bbox 4183-4193)
2026-08-10 17:41:36,455 INFO     29 [qwen-vl-parser] page=25 table: 11 sections
2026-08-10 17:41:36,583 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=904056, prompt_len=764
2026-08-10 17:41:37,942 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-27"
}
```
2026-08-10 17:41:37,942 INFO     29 [qwen-vl-parser] page=26 classify=table report_date=2026-01-27
2026-08-10 17:41:37,952 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=904056, prompt_len=756
2026-08-10 17:41:45,219 INFO     29 [qwen-vl-parser] table API response (len=1686):
\begin{tabular}{llllllll}
\hline
\multicolumn{2}{l}{质评合格,省内参考} & \multicolumn{6}{r}{采集时间:} \\
\multicolumn{2}{l}{住院} & \multicolumn{6}{r}{2026-01-27 05:46} \\
\multicolumn{2}{l}{F-PSA, CA72-4, CA19-9, $\beta$-h} & \multicolumn{6}{r}{采} \\
\multicolumn{2}{l}{\textbf{检验报告}} & \multicolumn{6}{r}{} \\
\hline
\multicolumn{2}{l}{姓} & 男 & \multicolumn{2}{l}{床号: 55} & \multicolumn{3}{l}{样本} \\
\multicolumn{2}{l}{性} & 人 IP & \multicolumn{2}{l}{标本种类: 血清} & \multicolumn{3}{l}{标本} \\
\multicolumn{2}{l}{年} & 龄: 75岁 & \multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \multicolumn{3}{l}{} \\
\hline
\multicolumn{2}{l}{\textbf{项}} & \textbf{目} & \textbf{不} & \textbf{提示} & \textbf{生物参考区间} & \textbf{单位} \\
\hline
1 & 癌胚抗原 & 9.21 & $\uparrow$ & 0-5.0 & ng/ml & \\
2 & 甲胎蛋白 & 1.64 & & 0-7.00 & ng/ml & \\
3 & 糖类抗原72-4 & 2.08 & & 0-6.9 & U/ml & \\
4 & 神经元特异性烯醇化酶 & 22.47 & $\uparrow$ & 0-17 & ng/ml & \\
5 & 细胞角蛋白19片段 & 5.70 & $\uparrow$ & 0-3.3 & ng/ml & \\
6 & 鳞状细胞癌相关抗原 & 2.97 & $\uparrow$ & 0-2.5 & ng/ml & \\
7 & 胃泌素释放肽前体 & 37.68 & & 0-68.3 & pg/mL & \\
8 & 总前列腺特异性抗原 & 4.820 & $\uparrow$ & 0-4 & ng/ml & \\
9 & 游离前列腺特异性抗原 & 0.767 & & 0-0.93 & ng/ml & \\
10 & FPSA/TPSA & 0.159 & & $>$0.15 & & \\
11 & 特异$\beta$人绒毛膜促性腺激素 & 5.86 & $\uparrow$ & 0-2.6 & mIU/ml & \\
12 & 糖类抗原19-9 & 27.60 & & 0-30 & U/ml & \\
\hline
\multicolumn{8}{l}{备注:} \\
\hline
\multicolumn{2}{l}{接收时间: 2026-01-27 06:57} & \multicolumn{2}{l}{报告时间: 2026-01-27 10:21} & \multicolumn{2}{l}{检验者:} & \multicolumn{2}{l}{审核者:} \\
\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \multicolumn{2}{l}{送检医生:} & \multicolumn{4}{l}{} \\
\multicolumn{8}{l}{本报告仅对本次检验标本负责, 如对检验结果有疑问, 请在3个工作日内与相关院区检验科联系!} \\
\multicolumn{8}{r}{第1页 共1页} \\
\hline
\end{tabular}
2026-08-10 17:41:45,220 INFO     29 [qwen-vl-parser] page=26 table: 35 LaTeX lines (bbox 4194-4228)
2026-08-10 17:41:45,220 INFO     29 [qwen-vl-parser] page=26 table: 35 sections
2026-08-10 17:41:45,265 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=73607, prompt_len=764
2026-08-10 17:41:46,422 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 17:41:46,422 INFO     29 [qwen-vl-parser] page=27 classify=text report_date=None
2026-08-10 17:41:46,435 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=73607, prompt_len=401
2026-08-10 17:41:49,153 INFO     29 [qwen-vl-parser] text API response (len=68):
["20201221确诊 肺腺癌", "20201227培美+卡铂", "出院后吉非替尼3个月，后奥西", "替尼服用至202601"]
2026-08-10 17:41:49,154 INFO     29 [qwen-vl-parser] page=27 text: 4 lines (bbox 4229-4232)
2026-08-10 17:41:49,155 INFO     29 [qwen-vl-parser] page=27 text: 4 sections
2026-08-10 17:41:49,155 INFO     29 [qwen-vl-parser] parse_pdf done: 4233 sections from 27 pages.
2026-08-10 17:41:49,172 INFO     29 Close text detector.
2026-08-10 17:41:49,605 INFO     29 Close text recognizer.
2026-08-10 17:41:50,009 INFO     29 Close recognizer.
2026-08-10 17:41:50,384 INFO     29 Close recognizer.
2026-08-10 17:41:50,898 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 17:41:50,898 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Parser:MedLink | outputs={"html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "json"}
2026-08-10 17:41:50,899 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 17:41:50,933 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:41:50,934 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 第2次住院\n[BBOX-1] 入院记录\n[BBOX-2] 姓名：\n[BBOX-3] 姓名：\n[BBOX-4] 出生地：\n[BBOX-5] 性别：男\n[BBOX-6] 职业：其他\n[BBOX-7] 年龄：75岁\n[BBOX-8] 入院时间：2026-01-26 10:12\n[BBOX-9] 民族：汉族\n[BBOX-10] 记录时间：2026-01-26 13:59\n[BBOX-11] 婚姻：已婚\n[BBOX-12] 病史陈述者：患者本人\n[BBOX-13] 主诉：确诊肺癌5年，病情进展1月余\n[BBOX-14] 现病史：患者因“胸闷2月，干咳1周”于2020年12月17日第一次入住我科，于2020-\n[BBOX-15] 12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：\n[BBOX-16] CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），\n[BBOX-17] CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合\n[BBOX-18] 免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞；（痰）\n[BBOX-19] 涂片内发现少量可疑恶性肿瘤细胞，于2020-12-27给予培美曲塞800mgd1+卡铂\n[BBOX-20] 400mgd2，并辅以止吐、保胃等治疗，化疗过程顺利，准予出院。出院诊断：左肺上叶恶\n[BBOX-21] 性肿瘤（腺癌 T4N3M1 IV期）、为肿瘤化学治疗疗程、纵隔淋巴结继发恶性肿瘤、肺\n[BBOX-22] 门淋巴结继发恶性肿瘤、阻塞性肺炎、肝囊肿、单纯性肾囊肿。出院后先后服用吉非\n[BBOX-23] 替尼、泰瑞沙靶向治疗至今。\n[BBOX-24] 1月余前患者就诊于外院，复查肺CT提示病灶增大，具体不详，无发热乏力，无咳\n[BBOX-25] 嗽咳痰，无胸闷憋气等不适，为求进一步诊治就诊于我院门诊，为行二次活检收入我\n[BBOX-26] 科，患者自发病以来，神志清，精神可，饮食睡眠可，大小便正常，体重近期未见明\n[BBOX-27] 显变化。\n[BBOX-28] 既往史：患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切\n[BBOX-29] 接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术\n[BBOX-30] 史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。\n[BBOX-31] 个人史：生于山东省胶州市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿\n[BBOX-32] 山、高氟区、低碘区居住史，无化学性物质、无放射性物质、无有毒物质接触史，无\n[BBOX-33] 吸毒史，无吸烟史，无饮酒史，无特殊药物服用史，无冶游史。\n[BBOX-34] 婚姻史：适龄结婚，配偶体健。\n[BBOX-35] 家族史：父母已故（具体不详），父有糖尿病病史，1弟因白血病去世，一妹去世，2\n[BBOX-36] 妹健在，否认家族中有遗传倾向性疾病及传染性疾病。\n[BBOX-37] 体格检查\n[BBOX-38] T：36.3℃ P：69次/分 R：17次/分 BP：120/66mmHg H：160cm W：52kg BMI：20.\n[BBOX-39] 31kg/m²\n[BBOX-40] 一般情况：正常发育状态，营养良好，体型匀称型，自主体位，正常面容，神志清楚\n[BBOX-41] ，正常步态，语言清晰，查体合作。\n[BBOX-42] 第1页\n[BBOX-43] 另2次住院\n[BBOX-44] 入院记录\n[BBOX-45] 登记号:\n[BBOX-46] 姓名:\n[BBOX-47] 住院号\n[BBOX-48] 皮肤、粘膜：皮肤黏膜无黄染 无皮疹、皮下出血，无皮下结节、瘢痕，皮下无水肿，\n[BBOX-49] 毛发分布正常，无肝掌、蜘蛛痣。全身浅表淋巴结：全身浅表淋巴结无肿大。\n[BBOX-50] 头部及其器官：头颅无畸形，毛发分布正常。眉毛正常，睫毛正常，无眼睑水肿，\n[BBOX-51] 结膜无充血、苍白，眼球无震颤，巩膜无黄染，角膜正常，瞳孔等大等圆，对光调节\n[BBOX-52] 反射正常。外耳道无畸形，无异常分泌物，乳突无压痛，听力正常。外鼻无畸形，无\n[BBOX-53] 鼻翼扇动，无分泌物、出血、阻塞，鼻中隔基本居中，无穿孔，双侧鼻窦区无压痛。\n[BBOX-54] 口唇无发绀，口腔粘膜无溃疡。伸舌无偏斜、震颤，齿龈无肿胀、出血。咽部粘膜无\n[BBOX-55] 充血，扁桃体无肥大。喉咙发音清晰。\n[BBOX-56] 颈部：颈部对称，软，颈动脉搏动正常，颈静脉无怒张，气管居中，肝颈静脉回流征\n[BBOX-57] 阴性，甲状腺无肿大，无压痛，未扪及包块，未闻及血管杂音。\n[BBOX-58] 胸部：胸廓对称、无畸形，乳房发育正常，胸骨无压痛，呼吸17次/分。\n[BBOX-59] 肺部：呼吸运动正常，肋间隙无增宽、无变窄，呼吸规整，语颤无增强及减弱，无胸\n[BBOX-60] 膜摩擦感、无皮下捻发感。叩诊清音，双肺呼吸音清晰，未闻及干、湿性啰音，语音\n[BBOX-61] 传导正常，无胸膜摩擦音。\n[BBOX-62] 心脏：心前区无隆起，心尖搏动未见增强及弥散，无震颤及心包摩擦感，心浊音界无\n[BBOX-63] 扩大，心率69次/分，律齐，各瓣膜听诊区未闻及病理性杂音，无心包摩擦音。\n[BBOX-64] 血管：桡动脉：脉率69次/分，脉律规整。无毛细血管搏动征，无股动脉枪击音。\n[BBOX-65] 腹部：腹部平坦，对称，无腹壁静脉曲张，无胃肠型和蠕动波，腹部柔软，无压痛及\n[BBOX-66] 反跳痛，未触及异常包块。肝、脾肋下未触及、质软、无压痛，Murphy氏征阴性。腹\n[BBOX-67] 部叩诊：肝上界在右锁骨中线第五肋间，肝、肾区无叩击痛，无移动性浊音。肠鸣音\n[BBOX-68] 正常，4次/分。未听到血管杂音。\n[BBOX-69] 直肠肛门：肛门及直肠无异常。外生殖器无异常。\n[BBOX-70] 脊柱、四肢：脊柱正常生理弯曲，无畸形、压痛、叩击痛，活动度正常，四肢无畸\n[BBOX-71] 形，肌力、肌张力正常，关节活动度正常，双下肢无水肿，无静脉曲张。\n[BBOX-72] 神经系统：痛、温、触觉正常，肌肉无萎缩、无瘫痪，无共济失调。腹壁反射正常，\n[BBOX-73] 双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性、\n[BBOX-74] Gordon征阴性、Oppenheim征阴性、Hoffmann征阴性，脑膜刺激征阴性。\n[BBOX-75] 专科检查\n[BBOX-76] 辅助检查\n[BBOX-77] 2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组\n[BBOX-78] 化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），\n[BBOX-79] CK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合\n[BBOX-80] 免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。\n[BBOX-81] 第2页\n[BBOX-82] 第2次住院\n[BBOX-83] 入院记录\n[BBOX-84] 登记号:\n[BBOX-85] 姓名:\n[BBOX-86] 住院号\n[BBOX-87] 初步诊断\n[BBOX-88] 肺部恶性肿瘤\n[BBOX-89] 纵隔淋巴结继发恶性肿瘤\n[BBOX-90] 肺门淋巴结继发恶性肿瘤\n[BBOX-91] 医师签名\n[BBOX-92] 项目内容\n[BBOX-93] 患者（家属）签名\n[BBOX-94] 以上患者所述内容及提供资料属实\n[BBOX-95] 门诊病历已归还\n[BBOX-96] 出院记录\n[BBOX-97] 登记号:\n[BBOX-98] 住院号:\n[BBOX-99] 姓名\n[BBOX-100] 姓名：\n[BBOX-101] 性别：男\n[BBOX-102] 年龄：75岁\n[BBOX-103] 科室·\n[BBOX-104] 入院日期：2026-01-26\n[BBOX-105] 出院日期：2026-01-31\n[BBOX-106] 住院天数：5天\n[BBOX-107] 入院情况：\n[BBOX-108] ，男，75岁，因“确诊肺癌5年，病情进展1月余”于2026-01-\n[BBOX-109] 26入院。患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切\n[BBOX-110] 接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术\n[BBOX-111] 史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。体检：T:\n[BBOX-112] 36.3℃ P:69次/分 R:17次/分 BP:120/66mmHg。神志清，精神可，双肺呼吸音清，未\n[BBOX-113] 闻及干湿性啰音。心脏各瓣膜听诊区未闻及异常杂音。腹软，无压痛，Murphy征阴\n[BBOX-114] 性。双下肢无水肿。病理征阴性。辅助检查：2020-12-21行支气管镜检查，组织病理\n[BBOX-115] 学示：(左侧隆突粘膜)非小细胞肺癌，免疫组化：CK7(+)，TTF-1(+)，\n[BBOX-116] NapsinA(+)，p40(部分+)，p63(部分+)，CK5/6(+)，ALK-D5F3(-)，ALK-\n[BBOX-117] D5F3-N(-)，S100(-)，Calponin(-)。结合免疫组化结果，符合腺癌；(左肺\n[BBOX-118] BALF)细胞蜡块内发现少量恶性肿瘤细胞。\n[BBOX-119] 入院诊断：肺部恶性肿瘤纵隔淋巴结继发恶性肿瘤肺门淋巴结继发恶性肿瘤\n[BBOX-120] 诊疗经过：入院后完善相关检验检查，【检验】血常规(无网红)+CRP：白细胞计数7.\n[BBOX-121] 49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血\n[BBOX-122] 小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原\n[BBOX-123] 测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：\n[BBOX-124] 22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4.\n[BBOX-125] 820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆\n[BBOX-126] 抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血\n[BBOX-127] 试验、传染性标志物4项检测未见异常。【检查】十二通道常规心电图检查：大致正常\n[BBOX-128] 心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性\n[BBOX-129] 可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝\n[BBOX-130] 囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超\n[BBOX-131] 声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复\n[BBOX-132] 查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随\n[BBOX-133] 访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规\n[BBOX-134] 整，请结合临床；【诊疗】入院后给予完善相关检查，排除禁忌后于2026-01-28行CT\n[BBOX-135] 引导下经皮穿刺肺活检术，2026-01-30左肺组织穿刺活检示非小细胞肺癌伴大片坏\n[BBOX-136] 死，结合形态学及免疫组化，符合腺癌。免疫组化示肿瘤细胞：CKpan(+)，\n[BBOX-137] CK7(+)，TTF-1(+)，p40(-)，CK5/6(-)；特殊染色：D-PAS(-)。现患者诊\n[BBOX-138] 第1页\n[BBOX-139] CS 扫描全能王\n[BBOX-140] 3亿人都在用的扫描App\n[BBOX-141] 出院记录\n[BBOX-142] 登记号\n[BBOX-143] 住院号\n[BBOX-144] 姓名：\n[BBOX-145] 断明确，拟出院后行基因检测治疗，准予办理出院。\n[BBOX-146] 出院诊断：肺部恶性肿瘤（腺癌 rT4N3MO IVA期）\n[BBOX-147] 纵隔淋巴结继发恶性肿瘤\n[BBOX-148] 肺门淋巴结继发恶性肿瘤\n[BBOX-149] 颈部淋巴结肿大\n[BBOX-150] 脾术后\n[BBOX-151] 慢性胆囊炎\n[BBOX-152] 肝囊肿\n[BBOX-153] 肾结节\n[BBOX-154] 出院情况：患者一般情况可，查体：神志清，双肺呼吸音清，心律齐，腹软，无压痛\n[BBOX-155] 及反跳痛，双下肢无水肿。\n[BBOX-156] 出院医嘱：\n[BBOX-157] 1.注意休息，避免感染、劳累；\n[BBOX-158] 2.出院后分子病理科行基因检测，出院2周待结果回报后于呼吸与危重症医学科门诊就\n[BBOX-159] 诊就诊制定进一步治疗方案；\n[BBOX-160] 3.如有不适或复查指标异常，门急诊及时就诊。\n[BBOX-161] 出院目的地：居家\n[BBOX-162] 患者照护需求：注意休息，避免感染、劳累\n[BBOX-163] 医师签名：\n[BBOX-164] 门（急）诊病历\n[BBOX-165] 初诊\n[BBOX-166] 科室\n[BBOX-167] 日期:2026-02-02 09:07\n[BBOX-168] 医学\n[BBOX-169] 性别:男\n[BBOX-170] 年龄:75岁\n[BBOX-171] 出生日期:1950-09-13\n[BBOX-172] 主诉:肺癌靶向治疗5年复查。\n[BBOX-173] 现病史:肺癌吉非替尼治疗3个月,因肝功异常更换泰瑞沙靶向治疗至今5年,外院肺CT提示病灶增大\n[BBOX-174] 既往史:无肺结核病史。\n[BBOX-175] 个人史:无不良嗜好。\n[BBOX-176] 家族史:无遗传病史。\n[BBOX-177] 体 检:双肺呼吸音清,未闻及干湿性啰音。\n[BBOX-178] 辅助检查:2026-01-30 组织病理学检查与诊断[免费用](左肺组织穿刺活检)非小细胞肺癌伴大片坏死,\n[BBOX-179] 结合形态学及免疫组化,符合腺癌。免疫组化示肿瘤细胞:CKpan(+),CK7(+),TTF-\n[BBOX-180] 1(+),p40(-),CK5/6(-);特殊染色:D-PAS(-)。\n[BBOX-181] 初步诊断:肺恶性肿瘤\n[BBOX-182] 诊疗计划:分子病理检测\n[BBOX-183] 甲磺酸奥希替尼片(泰瑞沙2)(80mg*30),剂量:80MG,用法:口服,频率:每日1次,疗程:1天,\n[BBOX-184] 温馨提示:此病历只打印一次,请妥善保管!\n[BBOX-185] 第1页 共2页\n[BBOX-186] 打印时间:2026-03-02 12:50:46\n[BBOX-187] 门（急）诊病历\n[BBOX-188] 初诊\n[BBOX-189] 科\n[BBOX-190] 日期:2026-02-02 09:07\n[BBOX-191] 姓名\n[BBOX-192] 性别:男\n[BBOX-193] 年龄:75岁\n[BBOX-194] 出生日期:1950-09-13\n[BBOX-195] 医师签名：\n[BBOX-196] CS 扫描全能王\n[BBOX-197] 3亿人都在用的扫描App\n[BBOX-198] 报告状态\n[BBOX-199] 收到日期\n[BBOX-200] 数据来源\n[BBOX-201] 床号\n[BBOX-202] 图像\n[BBOX-203] 1份已审核\n[BBOX-204] 2026-01-30 14:10:13\n[BBOX-205] 4.0\n[BBOX-206] 无\n[BBOX-207] 已审核\n[BBOX-208] 2026-01-28 09:16:53\n[BBOX-209] 4.0\n[BBOX-210] 55\n[BBOX-211] 无\n[BBOX-212] 2审核\n[BBOX-213] 2020-12-28 12:02\n[BBOX-214] 2.0\n[BBOX-215] 58床\n[BBOX-216] 无\n[BBOX-217] 2份已审核\n[BBOX-218] 2020-12-21 14:02\n[BBOX-219] 2.0\n[BBOX-220] 58床\n[BBOX-221] 无\n[BBOX-222] 共1页，共4条记录\n[BBOX-223] 门诊号：-\n[BBOX-224] 姓名\n[BBOX-225] 性别\n[BBOX-226] 男\n[BBOX-227] 年龄\n[BBOX-228] 70岁\n[BBOX-229] 病人编号\n[BBOX-230] 病区\n[BBOX-231] 病案号\n[BBOX-232] 门诊号\n[BBOX-233] 送检科室\n[BBOX-234] 送检单位\n[BBOX-235] 送检医生\n[BBOX-236] 标本名称\n[BBOX-237] 左侧隆突粘膜、左肺BALF等\n[BBOX-238] 临床诊断\n[BBOX-239] 肺部阴影\n[BBOX-240] 病理诊断\n[BBOX-241] (左侧隆突粘膜)非小细胞肺癌，结合免疫组化结果，符合腺癌；\n[BBOX-242] (左肺BALF)细胞蜡块内发现少量恶性肿瘤细胞；\n[BBOX-243] (左肺BALF)涂片内未发现恶性肿瘤细胞；\n[BBOX-244] (痰)涂片内发现少量可疑恶性肿瘤细胞。\n[BBOX-245] 免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。\n[BBOX-246] 报告医生\n[BBOX-247] 复诊医生\n[BBOX-248] 报告时间\n[BBOX-249] 2020-12-25\n[BBOX-250] 12:51\n[BBOX-251] 2026-03-02\n[BBOX-252] 责任医生\n[BBOX-253] 门诊号\n[BBOX-254] 状态\n[BBOX-255] 售到日期\n[BBOX-256] 费用来源\n[BBOX-257] 床号\n[BBOX-258] 回路\n[BBOX-259] 2020-01-30 14:10:13\n[BBOX-260] 4.0\n[BBOX-261] 无\n[BBOX-262] 2020-01-28 09:10:53\n[BBOX-263] 4.0\n[BBOX-264] 55\n[BBOX-265] 毛\n[BBOX-266] 1费已审核\n[BBOX-267] 2020-12-28 12:02\n[BBOX-268] 2.0\n[BBOX-269] 58床\n[BBOX-270] 无\n[BBOX-271] 2费已审核\n[BBOX-272] 2020-12-21 14:02\n[BBOX-273] 2.0\n[BBOX-274] 58床\n[BBOX-275] 无\n[BBOX-276] 下一页\n[BBOX-277] 显示\n[BBOX-278] 共1页,共4条已查\n[BBOX-279] 病理号\n[BBOX-280] 住院\n[BBOX-281] 门诊号\n[BBOX-282] 1-1]\n[BBOX-283] 姓名\n[BBOX-284] 70岁\n[BBOX-285] 病人编号\n[BBOX-286] 0007\n[BBOX-287] 病区\n[BBOX-288] 门诊号\n[BBOX-289] 送检科室\n[BBOX-290] 送检医生\n[BBOX-291] 标本名称\n[BBOX-292] 左侧隆突粘膜、左肺BALF等\n[BBOX-293] 临床诊断\n[BBOX-294] 肺部阴影\n[BBOX-295] 病理诊断\n[BBOX-296] 2020.12.20加做免疫结果：PD-L1-22C3（+，TPS约30%）\n[BBOX-297] 报告医生\n[BBOX-298] 报告时间\n[BBOX-299] 2020-12-29\n[BBOX-300] 12:51\n[BBOX-301] 2026-03-02\n[BBOX-302] 性别：男\n[BBOX-303] 年龄：70岁\n[BBOX-304] 住院号：\n[BBOX-305] 费\n[BBOX-306] 报告状态：已审核\n[BBOX-307] 登记日期：2020-01-30 14:10:13\n[BBOX-308] 检验来源：1.0\n[BBOX-309] 床号：\n[BBOX-310] 图像：无\n[BBOX-311] 报告状态：已审核\n[BBOX-312] 登记日期：2020-01-28 08:10:53\n[BBOX-313] 检验来源：1.0\n[BBOX-314] 床号：55\n[BBOX-315] 图像：无\n[BBOX-316] 报告状态：已审核\n[BBOX-317] 登记日期：2020-12-28 12:02\n[BBOX-318] 检验来源：2.0\n[BBOX-319] 床号：58床\n[BBOX-320] 图像：无\n[BBOX-321] 报告状态：已审核\n[BBOX-322] 登记日期：2020-12-21 14:02\n[BBOX-323] 检验来源：2.0\n[BBOX-324] 床号：58床\n[BBOX-325] 图像：无\n[BBOX-326] 1 页 下一\n[BBOX-327] 当前病人\n[BBOX-328] 病理号\n[BBOX-329] 门诊号：\n[BBOX-330] 姓名：\n[BBOX-331] 病区：\n[BBOX-332] 住院科室：\n[BBOX-333] 标本名称：\n[BBOX-334] 病理诊断：\n[BBOX-335] 病理诊断：\n[BBOX-336] 病理诊断：\n[BBOX-337] 病理诊断：\n[BBOX-338] 病理诊断：\n[BBOX-339] 病理诊断：\n[BBOX-340] 病理诊断：\n[BBOX-341] 病理诊断：\n[BBOX-342] 病理诊断：\n[BBOX-343] 病理诊断：\n[BBOX-344] 病理诊断：\n[BBOX-345] 病理诊断：\n[BBOX-346] 病理诊断：\n[BBOX-347] 病理诊断：\n[BBOX-348] 病理诊断：\n[BBOX-349] 病理诊断：\n[BBOX-350] 病理诊断：\n[BBOX-351] 病理诊断：\n[BBOX-352] 病理诊断：\n[BBOX-353] 病理诊断：\n[BBOX-354] 病理诊断：\n[BBOX-355] 病理诊断：\n[BBOX-356] 病理诊断：\n[BBOX-357] 病理诊断：\n[BBOX-358] 病理诊断：\n[BBOX-359] 病理诊断：\n[BBOX-360] 病理诊断：\n[BBOX-361] 病理诊断：\n[BBOX-362] 病理诊断：\n[BBOX-363] 病理诊断：\n[BBOX-364] 病理诊断：\n[BBOX-365] 病理诊断：\n[BBOX-366] 病理诊断：\n[BBOX-367] 病理诊断：\n[BBOX-368] 病理诊断：\n[BBOX-369] 病理诊断：\n[BBOX-370] 病理诊断：\n[BBOX-371] 病理诊断：\n[BBOX-372] 病理诊断：\n[BBOX-373] 病理诊断：\n[BBOX-374] 病理诊断：\n[BBOX-375] 病理诊断：\n[BBOX-376] 病理诊断：\n[BBOX-377] 病理诊断：\n[BBOX-378] 病理诊断：\n[BBOX-379] 病理诊断：\n[BBOX-380] 病理诊断：\n[BBOX-381] 病理诊断：\n[BBOX-382] 病理诊断：\n[BBOX-383] 病理诊断：\n[BBOX-384] 病理诊断：\n[BBOX-385] 病理诊断：\n[BBOX-386] 病理诊断：\n[BBOX-387] 病理诊断：\n[BBOX-388] 病理诊断：\n[BBOX-389] 病理诊断：\n[BBOX-390] 病理诊断：\n[BBOX-391] 病理诊断：\n[BBOX-392] 病理诊断：\n[BBOX-393] 病理诊断：\n[BBOX-394] 病理诊断：\n[BBOX-395] 病理诊断：\n[BBOX-396] 病理诊断：\n[BBOX-397] 病理诊断：\n[BBOX-398] 病理诊断：\n[BBOX-399] 病理诊断：\n[BBOX-400] 病理诊断：\n[BBOX-401] 病理诊断：\n[BBOX-402] 病理诊断：\n[BBOX-403] 病理诊断：\n[BBOX-404] 病理诊断：\n[BBOX-405] 病理诊断：\n[BBOX-406] 病理诊断：\n[BBOX-407] 病理诊断：\n[BBOX-408] 病理诊断：\n[BBOX-409] 病理诊断：\n[BBOX-410] 病理诊断：\n[BBOX-411] 病理诊断：\n[BBOX-412] 病理诊断：\n[BBOX-413] 病理诊断：\n[BBOX-414] 病理诊断：\n[BBOX-415] 病理诊断：\n[BBOX-416] 病理诊断：\n[BBOX-417] 病理诊断：\n[BBOX-418] 病理诊断：\n[BBOX-419] 病理诊断：\n[BBOX-420] 病理诊断：\n[BBOX-421] 病理诊断：\n[BBOX-422] 病理诊断：\n[BBOX-423] 病理诊断：\n[BBOX-424] 病理诊断：\n[BBOX-425] 病理诊断：\n[BBOX-426] 病理诊断：\n[BBOX-427] 病理诊断：\n[BBOX-428] 病理诊断：\n[BBOX-429] 病理诊断：\n[BBOX-430] 病理诊断：\n[BBOX-431] 病理诊断：\n[BBOX-432] 病理诊断：\n[BBOX-433] 病理诊断：\n[BBOX-434] 病理诊断：\n[BBOX-435] 病理诊断：\n[BBOX-436] 病理诊断：\n[BBOX-437] 病理诊断：\n[BBOX-438] 病理诊断：\n[BBOX-439] 病理诊断：\n[BBOX-440] 病理诊断：\n[BBOX-441] 病理诊断：\n[BBOX-442] 病理诊断：\n[BBOX-443] 病理诊断：\n[BBOX-444] 病理诊断：\n[BBOX-445] 病理诊断：\n[BBOX-446] 病理诊断：\n[BBOX-447] 病理诊断：\n[BBOX-448] 病理诊断：\n[BBOX-449] 病理诊断：\n[BBOX-450] 病理诊断：\n[BBOX-451] 病理诊断：\n[BBOX-452] 病理诊断：\n[BBOX-453] 病理诊断：\n[BBOX-454] 病理诊断：\n[BBOX-455] 病理诊断：\n[BBOX-456] 病理诊断：\n[BBOX-457] 病理诊断：\n[BBOX-458] 病理诊断：\n[BBOX-459] 病理诊断：\n[BBOX-460] 病理诊断：\n[BBOX-461] 病理诊断：\n[BBOX-462] 病理诊断：\n[BBOX-463] 病理诊断：\n[BBOX-464] 病理诊断：\n[BBOX-465] 病理诊断：\n[BBOX-466] 病理诊断：\n[BBOX-467] 病理诊断：\n[BBOX-468] 病理诊断：\n[BBOX-469] 病理诊断：\n[BBOX-470] 病理诊断：\n[BBOX-471] 病理诊断：\n[BBOX-472] 病理诊断：\n[BBOX-473] 病理诊断：\n[BBOX-474] 病理诊断：\n[BBOX-475] 病理诊断：\n[BBOX-476] 病理诊断：\n[BBOX-477] 病理诊断：\n[BBOX-478] 病理诊断：\n[BBOX-479] 病理诊断：\n[BBOX-480] 病理诊断：\n[BBOX-481] 病理诊断：\n[BBOX-482] 病理诊断：\n[BBOX-483] 病理诊断：\n[BBOX-484] 病理诊断：\n[BBOX-485] 病理诊断：\n[BBOX-486] 病理诊断：\n[BBOX-487] 病理诊断：\n[BBOX-488] 病理诊断：\n[BBOX-489] 病理诊断：\n[BBOX-490] 病理诊断：\n[BBOX-491] 病理诊断：\n[BBOX-492] 病理诊断：\n[BBOX-493] 病理诊断：\n[BBOX-494] 病理诊断：\n[BBOX-495] 病理诊断：\n[BBOX-496] 病理诊断：\n[BBOX-497] 病理诊断：\n[BBOX-498] 病理诊断：\n[BBOX-499] 病理诊断：\n[BBOX-500] 病理诊断：\n[BBOX-501] 病理诊断：\n[BBOX-502] 病理诊断：\n[BBOX-503] 病理诊断：\n[BBOX-504] 病理诊断：\n[BBOX-505] 病理诊断：\n[BBOX-506] 病理诊断：\n[BBOX-507] 病理诊断：\n[BBOX-508] 病理诊断：\n[BBOX-509] 病理诊断：\n[BBOX-510] 病理诊断：\n[BBOX-511] 病理诊断：\n[BBOX-512] 病理诊断：\n[BBOX-513] 病理诊断：\n[BBOX-514] 病理诊断：\n[BBOX-515] 病理诊断：\n[BBOX-516] 病理诊断：\n[BBOX-517] 病理诊断：\n[BBOX-518] 病理诊断：\n[BBOX-519] 病理诊断：\n[BBOX-520] 病理诊断：\n[BBOX-521] 病理诊断：\n[BBOX-522] 病理诊断：\n[BBOX-523] 病理诊断：\n[BBOX-524] 病理诊断：\n[BBOX-525] 病理诊断：\n[BBOX-526] 病理诊断：\n[BBOX-527] 病理诊断：\n[BBOX-528] 病理诊断：\n[BBOX-529] 病理诊断：\n[BBOX-530] 病理诊断：\n[BBOX-531] 病理诊断：\n[BBOX-532] 病理诊断：\n[BBOX-533] 病理诊断：\n[BBOX-534] 病理诊断：\n[BBOX-535] 病理诊断：\n[BBOX-536] 病理诊断：\n[BBOX-537] 病理诊断：\n[BBOX-538] 病理诊断：\n[BBOX-539] 病理诊断：\n[BBOX-540] 病理诊断：\n[BBOX-541] 病理诊断：\n[BBOX-542] 病理诊断：\n[BBOX-543] 病理诊断：\n[BBOX-544] 病理诊断：\n[BBOX-545] 病理诊断：\n[BBOX-546] 病理诊断：\n[BBOX-547] 病理诊断：\n[BBOX-548] 病理诊断：\n[BBOX-549] 病理诊断：\n[BBOX-550] 病理诊断：\n[BBOX-551] 病理诊断：\n[BBOX-552] 病理诊断：\n[BBOX-553] 病理诊断：\n[BBOX-554] 病理诊断：\n[BBOX-555] 病理诊断：\n[BBOX-556] 病理诊断：\n[BBOX-557] 病理诊断：\n[BBOX-558] 病理诊断：\n[BBOX-559] 病理诊断：\n[BBOX-560] 病理诊断：\n[BBOX-561] 病理诊断：\n[BBOX-562] 病理诊断：\n[BBOX-563] 病理诊断：\n[BBOX-564] 病理诊断：\n[BBOX-565] 病理诊断：\n[BBOX-566] 病理诊断：\n[BBOX-567] 病理诊断：\n[BBOX-568] 病理诊断：\n[BBOX-569] 病理诊断：\n[BBOX-570] 病理诊断：\n[BBOX-571] 病理诊断：\n[BBOX-572] 病理诊断：\n[BBOX-573] 病理诊断：\n[BBOX-574] 病理诊断：\n[BBOX-575] 病理诊断：\n[BBOX-576] 病理诊断：\n[BBOX-577] 病理诊断：\n[BBOX-578] 病理诊断：\n[BBOX-579] 病理诊断：\n[BBOX-580] 病理诊断：\n[BBOX-581] 病理诊断：\n[BBOX-582] 病理诊断：\n[BBOX-583] 病理诊断：\n[BBOX-584] 病理诊断：\n[BBOX-585] 病理诊断：\n[BBOX-586] 病理诊断：\n[BBOX-587] 病理诊断：\n[BBOX-588] 病理诊断：\n[BBOX-589] 病理诊断：\n[BBOX-590] 病理诊断：\n[BBOX-591] 病理诊断：\n[BBOX-592] 病理诊断：\n[BBOX-593] 病理诊断：\n[BBOX-594] 病理诊断：\n[BBOX-595] 病理诊断：\n[BBOX-596] 病理诊断：\n[BBOX-597] 病理诊断：\n[BBOX-598] 病理诊断：\n[BBOX-599] 病理诊断：\n[BBOX-600] 病理诊断：\n[BBOX-601] 病理诊断：\n[BBOX-602] 病理诊断：\n[BBOX-603] 病理诊断：\n[BBOX-604] 病理诊断：\n[BBOX-605] 病理诊断：\n[BBOX-606] 病理诊断：\n[BBOX-607] 病理诊断：\n[BBOX-608] 病理诊断：\n[BBOX-609] 病理诊断：\n[BBOX-610] 病理诊断：\n[BBOX-611] 病理诊断：\n[BBOX-612] 病理诊断：\n[BBOX-613] 病理诊断：\n[BBOX-614] 病理诊断：\n[BBOX-615] 病理诊断：\n[BBOX-616] 病理诊断：\n[BBOX-617] 病理诊断：\n[BBOX-618] 病理诊断：\n[BBOX-619] 病理诊断：\n[BBOX-620] 病理诊断：\n[BBOX-621] 病理诊断：\n[BBOX-622] 病理诊断：\n[BBOX-623] 病理诊断：\n[BBOX-624] 病理诊断：\n[BBOX-625] 病理诊断：\n[BBOX-626] 病理诊断：\n[BBOX-627] 病理诊断：\n[BBOX-628] 病理诊断：\n[BBOX-629] 病理诊断：\n[BBOX-630] 病理诊断：\n[BBOX-631] 病理诊断：\n[BBOX-632] 病理诊断：\n[BBOX-633] 病理诊断：\n[BBOX-634] 病理诊断：\n[BBOX-635] 病理诊断：\n[BBOX-636] 病理诊断：\n[BBOX-637] 病理诊断：\n[BBOX-638] 病理诊断：\n[BBOX-639] 病理诊断：\n[BBOX-640] 病理诊断：\n[BBOX-641] 病理诊断：\n[BBOX-642] 病理诊断：\n[BBOX-643] 病理诊断：\n[BBOX-644] 病理诊断：\n[BBOX-645] 病理诊断：\n[BBOX-646] 病理诊断：\n[BBOX-647] 病理诊断：\n[BBOX-648] 病理诊断：\n[BBOX-649] 病理诊断：\n[BBOX-650] 病理诊断：\n[BBOX-651] 病理诊断：\n[BBOX-652] 病理诊断：\n[BBOX-653] 病理诊断：\n[BBOX-654] 病理诊断：\n[BBOX-655] 病理诊断：\n[BBOX-656] 病理诊断：\n[BBOX-657] 病理诊断：\n[BBOX-658] 病理诊断：\n[BBOX-659] 病理诊断：\n[BBOX-660] 病理诊断：\n[BBOX-661] 病理诊断：\n[BBOX-662] 病理诊断：\n[BBOX-663] 病理诊断：\n[BBOX-664] 病理诊断：\n[BBOX-665] 病理诊断：\n[BBOX-666] 病理诊断：\n[BBOX-667] 病理诊断：\n[BBOX-668] 病理诊断：\n[BBOX-669] 病理诊断：\n[BBOX-670] 病理诊断：\n[BBOX-671] 病理诊断：\n[BBOX-672] 病理诊断：\n[BBOX-673] 病理诊断：\n[BBOX-674] 病理诊断：\n[BBOX-675] 病理诊断：\n[BBOX-676] 病理诊断：\n[BBOX-677] 病理诊断：\n[BBOX-678] 病理诊断：\n[BBOX-679] 病理诊断：\n[BBOX-680] 病理诊断：\n[BBOX-681] 病理诊断：\n[BBOX-682] 病理诊断：\n[BBOX-683] 病理诊断：\n[BBOX-684] 病理诊断：\n[BBOX-685] 病理诊断：\n[BBOX-686] 病理诊断：\n[BBOX-687] 病理诊断：\n[BBOX-688] 病理诊断：\n[BBOX-689] 病理诊断：\n[BBOX-690] 病理诊断：\n[BBOX-691] 病理诊断：\n[BBOX-692] 病理诊断：\n[BBOX-693] 病理诊断：\n[BBOX-694] 病理诊断：\n[BBOX-695] 病理诊断：\n[BBOX-696] 病理诊断：\n[BBOX-697] 病理诊断：\n[BBOX-698] 病理诊断：\n[BBOX-699] 病理诊断：\n[BBOX-700] 病理诊断：\n[BBOX-701] 病理诊断：\n[BBOX-702] 病理诊断：\n[BBOX-703] 病理诊断：\n[BBOX-704] 病理诊断：\n[BBOX-705] 病理诊断：\n[BBOX-706] 病理诊断：\n[BBOX-707] 病理诊断：\n[BBOX-708] 病理诊断：\n[BBOX-709] 病理诊断：\n[BBOX-710] 病理诊断：\n[BBOX-711] 病理诊断：\n[BBOX-712] 病理诊断：\n[BBOX-713] 病理诊断：\n[BBOX-714] 病理诊断：\n[BBOX-715] 病理诊断：\n[BBOX-716] 病理诊断：\n[BBOX-717] 病理诊断：\n[BBOX-718] 病理诊断：\n[BBOX-719] 病理诊断：\n[BBOX-720] 病理诊断：\n[BBOX-721] 病理诊断：\n[BBOX-722] 病理诊断：\n[BBOX-723] 病理诊断：\n[BBOX-724] 病理诊断：\n[BBOX-725] 病理诊断：\n[BBOX-726] 病理诊断：\n[BBOX-727] 病理诊断：\n[BBOX-728] 病理诊断：\n[BBOX-729] 病理诊断：\n[BBOX-730] 病理诊断：\n[BBOX-731] 病理诊断：\n[BBOX-732] 病理诊断：\n[BBOX-733] 病理诊断：\n[BBOX-734] 病理诊断：\n[BBOX-735] 病理诊断：\n[BBOX-736] 病理诊断：\n[BBOX-737] 病理诊断：\n[BBOX-738] 病理诊断：\n[BBOX-739] 病理诊断：\n[BBOX-740] 病理诊断：\n[BBOX-741] 病理诊断：\n[BBOX-742] 病理诊断：\n[BBOX-743] 病理诊断：\n[BBOX-744] 病理诊断：\n[BBOX-745] 病理诊断：\n[BBOX-746] 病理诊断：\n[BBOX-747] 病理诊断：\n[BBOX-748] 病理诊断：\n[BBOX-749] 病理诊断：\n[BBOX-750] 病理诊断：\n[BBOX-751] 病理诊断：\n[BBOX-752] 病理诊断：\n[BBOX-753] 病理诊断：\n[BBOX-754] 病理诊断：\n[BBOX-755] 病理诊断：\n[BBOX-756] 病理诊断：\n[BBOX-757] 病理诊断：\n[BBOX-758] 病理诊断：\n[BBOX-759] 病理诊断：\n[BBOX-760] 病理诊断：\n[BBOX-761] 病理诊断：\n[BBOX-762] 病理诊断：\n[BBOX-763] 病理诊断：\n[BBOX-764] 病理诊断：\n[BBOX-765] 病理诊断：\n[BBOX-766] 病理诊断：\n[BBOX-767] 病理诊断：\n[BBOX-768] 病理诊断：\n[BBOX-769] 病理诊断：\n[BBOX-770] 病理诊断：\n[BBOX-771] 病理诊断：\n[BBOX-772] 病理诊断：\n[BBOX-773] 病理诊断：\n[BBOX-774] 病理诊断：\n[BBOX-775] 病理诊断：\n[BBOX-776] 病理诊断：\n[BBOX-777] 病理诊断：\n[BBOX-778] 病理诊断：\n[BBOX-779] 病理诊断：\n[BBOX-780] 病理诊断：\n[BBOX-781] 病理诊断：\n[BBOX-782] 病理诊断：\n[BBOX-783] 病理诊断：\n[BBOX-784] 病理诊断：\n[BBOX-785] 病理诊断：\n[BBOX-786] 病理诊断：\n[BBOX-787] 病理诊断：\n[BBOX-788] 病理诊断：\n[BBOX-789] 病理诊断：\n[BBOX-790] 病理诊断：\n[BBOX-791] 病理诊断：\n[BBOX-792] 病理诊断：\n[BBOX-793] 病理诊断：\n[BBOX-794] 病理诊断：\n[BBOX-795] 病理诊断：\n[BBOX-796] 病理诊断：\n[BBOX-797] 病理诊断：\n[BBOX-798] 病理诊断：\n[BBOX-799] 病理诊断：\n[BBOX-800] 病理诊断：\n[BBOX-801] 病理诊断：\n[BBOX-802] 病理诊断：\n[BBOX-803] 病理诊断：\n[BBOX-804] 病理诊断：\n[BBOX-805] 病理诊断：\n[BBOX-806] 病理诊断：\n[BBOX-807] 病理诊断：\n[BBOX-808] 病理诊断：\n[BBOX-809] 病理诊断：\n[BBOX-810] 病理诊断：\n[BBOX-811] 病理诊断：\n[BBOX-812] 病理诊断：\n[BBOX-813] 病理诊断：\n[BBOX-814] 病理诊断：\n[BBOX-815] 病理诊断：\n[BBOX-816] 病理诊断：\n[BBOX-817] 病理诊断：\n[BBOX-818] 病理诊断：\n[BBOX-819] 病理诊断：\n[BBOX-820] 病理诊断：\n[BBOX-821] 病理诊断：\n[BBOX-822] 病理诊断：\n[BBOX-823] 病理诊断：\n[BBOX-824] 病理诊断：\n[BBOX-825] 病理诊断：\n[BBOX-826] 病理诊断：\n[BBOX-827] 病理诊断：\n[BBOX-828] 病理诊断：\n[BBOX-829] 病理诊断：\n[BBOX-830] 病理诊断：\n[BBOX-831] 病理诊断：\n[BBOX-832] 病理诊断：\n[BBOX-833] 病理诊断：\n[BBOX-834] 病理诊断：\n[BBOX-835] 病理诊断：\n[BBOX-836] 病理诊断：\n[BBOX-837] 病理诊断：\n[BBOX-838] 病理诊断：\n[BBOX-839] 病理诊断：\n[BBOX-840] 病理诊断：\n[BBOX-841] 病理诊断：\n[BBOX-842] 病理诊断：\n[BBOX-843] 病理诊断：\n[BBOX-844] 病理诊断：\n[BBOX-845] 病理诊断：\n[BBOX-846] 病理诊断：\n[BBOX-847] 病理诊断：\n[BBOX-848] 病理诊断：\n[BBOX-849] 病理诊断：\n[BBOX-850] 病理诊断：\n[BBOX-851] 病理诊断：\n[BBOX-852] 病理诊断：\n[BBOX-853] 病理诊断：\n[BBOX-854] 病理诊断：\n[BBOX-855] 病理诊断：\n[BBOX-856] 病理诊断：\n[BBOX-857] 病理诊断：\n[BBOX-858] 病理诊断：\n[BBOX-859] 病理诊断：\n[BBOX-860] 病理诊断：\n[BBOX-861] 病理诊断：\n[BBOX-862] 病理诊断：\n[BBOX-863] 病理诊断：\n[BBOX-864] 病理诊断：\n[BBOX-865] 病理诊断：\n[BBOX-866] 病理诊断：\n[BBOX-867] 病理诊断：\n[BBOX-868] 病理诊断：\n[BBOX-869] 病理诊断：\n[BBOX-870] 病理诊断：\n[BBOX-871] 病理诊断：\n[BBOX-872] 病理诊断：\n[BBOX-873] 病理诊断：\n[BBOX-874] 病理诊断：\n[BBOX-875] 病理诊断：\n[BBOX-876] 病理诊断：\n[BBOX-877] 病理诊断：\n[BBOX-878] 病理诊断：\n[BBOX-879] 病理诊断：\n[BBOX-880] 病理诊断：\n[BBOX-881] 病理诊断：\n[BBOX-882] 病理诊断：\n[BBOX-883] 病理诊断：\n[BBOX-884] 病理诊断：\n[BBOX-885] ���理诊断：\n[BBOX-886] 病理诊断：\n[BBOX-887] 病理诊断：\n[BBOX-888] 病理诊断：\n[BBOX-889] 病理诊断：\n[BBOX-890] 病理诊断：\n[BBOX-891] 病理诊断：\n[BBOX-892] 病理诊断：\n[BBOX-893] 病理诊断：\n[BBOX-894] 病理诊断：\n[BBOX-895] 病理诊断：\n[BBOX-896] 病理诊断：\n[BBOX-897] 病理诊断：\n[BBOX-898] 病理诊断：\n[BBOX-899] 病理诊断：\n[BBOX-900] 病理诊断：\n[BBOX-901] 病理诊断：\n[BBOX-902] 病理诊断：\n[BBOX-903] 病理诊断：\n[BBOX-904] 病理诊断：\n[BBOX-905] 病理诊断：\n[BBOX-906] 病理诊断：\n[BBOX-907] 病理诊断：\n[BBOX-908] 病理诊断：\n[BBOX-909] 病理诊断：\n[BBOX-910] 病理诊断：\n[BBOX-911] 病理诊断：\n[BBOX-912] 病理诊断：\n[BBOX-913] 病理诊断：\n[BBOX-914] 病理诊断：\n[BBOX-915] 病理诊断：\n[BBOX-916] 病理诊断：\n[BBOX-917] 病理诊断：\n[BBOX-918] 病理诊断：\n[BBOX-919] 病理诊断：\n[BBOX-920] 病理诊断：\n[BBOX-921] 病理诊断：\n[BBOX-922] 病理诊断：\n[BBOX-923] 病理诊断：\n[BBOX-924] 病理诊断：\n[BBOX-925] 病理诊断：\n[BBOX-926] 病理诊断：\n[BBOX-927] 病理诊断：\n[BBOX-928] 病理诊断：\n[BBOX-929] 病理诊断：\n[BBOX-930] 病理诊断：\n[BBOX-931] 病理诊断：\n[BBOX-932] 病理诊断：\n[BBOX-933] 病理诊断：\n[BBOX-934] 病理诊断：\n[BBOX-935] 病理诊断：\n[BBOX-936] 病理诊断：\n[BBOX-937] 病理诊断：\n[BBOX-938] 病理诊断：\n[BBOX-939] 病理诊断：\n[BBOX-940] 病理诊断：\n[BBOX-941] 病理诊断：\n[BBOX-942] 病理诊断：\n[BBOX-943] 病理诊断：\n[BBOX-944] 病理诊断：\n[BBOX-945] 病理诊断：\n[BBOX-946] 病理诊断：\n[BBOX-947] 病理诊断：\n[BBOX-948] 病理诊断：\n[BBOX-949] 病理诊断：\n[BBOX-950] 病理诊断：\n[BBOX-951] 病理诊断：\n[BBOX-952] 病理诊断：\n[BBOX-953] 病理诊断：\n[BBOX-954] 病理诊断：\n[BBOX-955] 病理诊断：\n[BBOX-956] 病理诊断：\n[BBOX-957] 病理诊断：\n[BBOX-958] 病理诊断：\n[BBOX-959] 病理诊断：\n[BBOX-960] 病理诊断：\n[BBOX-961] 病理诊断：\n[BBOX-962] 病理诊断：\n[BBOX-963] 病理诊断：\n[BBOX-964] 病理诊断：\n[BBOX-965] 病理诊断：\n[BBOX-966] 病理诊断：\n[BBOX-967] 病理诊断：\n[BBOX-968] 病理诊断：\n[BBOX-969] 病理诊断：\n[BBOX-970] 病理诊断：\n[BBOX-971] 病理诊断：\n[BBOX-972] 病理诊断：\n[BBOX-973] 病理诊断：\n[BBOX-974] 病理诊断：\n[BBOX-975] 病理诊断：\n[BBOX-976] 病理诊断：\n[BBOX-977] 病理诊断：\n[BBOX-978] 病理诊断：\n[BBOX-979] 病理诊断：\n[BBOX-980] 病理诊断：\n[BBOX-981] 病理诊断：\n[BBOX-982] 病理诊断：\n[BBOX-983] 病理诊断：\n[BBOX-984] 病理诊断：\n[BBOX-985] 病理诊断：\n[BBOX-986] 病理诊断：\n[BBOX-987] 病理诊断：\n[BBOX-988] 病理诊断：\n[BBOX-989] 病理诊断：\n[BBOX-990] 病理诊断：\n[BBOX-991] 病理诊断：\n[BBOX-992] 病理诊断：\n[BBOX-993] 病理诊断：\n[BBOX-994] 病理诊断：\n[BBOX-995] 病理诊断：\n[BBOX-996] 病理诊断：\n[BBOX-997] 病理诊断：\n[BBOX-998] 病理诊断：\n[BBOX-999] 病理诊断：\n[BBOX-1000] 病理诊断：\n[BBOX-1001] 病理诊断：\n[BBOX-1002] 病理诊断：\n[BBOX-1003] 病理诊断：\n[BBOX-1004] 病理诊断：\n[BBOX-1005] 病理诊断：\n[BBOX-1006] 病理诊断：\n[BBOX-1007] 病理诊断：\n[BBOX-1008] 病理诊断：\n[BBOX-1009] 病理诊断：\n[BBOX-1010] 病理诊断：\n[BBOX-1011] 病理诊断：\n[BBOX-1012] 病理诊断：\n[BBOX-1013] 病理诊断：\n[BBOX-1014] 病理诊断：\n[BBOX-1015] 病理诊断：\n[BBOX-1016] 病理诊断：\n[BBOX-1017] 病理诊断：\n[BBOX-1018] 病理诊断：\n[BBOX-1019] 病理诊断：\n[BBOX-1020] 病理诊断：\n[BBOX-1021] 病理诊断：\n[BBOX-1022] 病理诊断：\n[BBOX-1023] 病理诊断：\n[BBOX-1024] 病理诊断：\n[BBOX-1025] 病理诊断：\n[BBOX-1026] 病理诊断：\n[BBOX-1027] 病理诊断：\n[BBOX-1028] 病理诊断：\n[BBOX-1029] 病理诊断：\n[BBOX-1030] 病理诊断：\n[BBOX-1031] 病理诊断：\n[BBOX-1032] 病理诊断：\n[BBOX-1033] 病理诊断：\n[BBOX-1034] 病理诊断：\n[BBOX-1035] 病理诊断：\n[BBOX-1036] 病理诊断：\n[BBOX-1037] 病理诊断：\n[BBOX-1038] 病理诊断：\n[BBOX-1039] 病理诊断：\n[BBOX-1040] 病理诊断：\n[BBOX-1041] 病理诊断：\n[BBOX-1042] 病理诊断：\n[BBOX-1043] 病理诊断：\n[BBOX-1044] 病理诊断：\n[BBOX-1045] 病理诊断：\n[BBOX-1046] 病理诊断：\n[BBOX-1047] 病理诊断：\n[BBOX-1048] 病理诊断：\n[BBOX-1049] 病理诊断：\n[BBOX-1050] 病理诊断：\n[BBOX-1051] 病理诊断：\n[BBOX-1052] 病理诊断：\n[BBOX-1053] 病理诊断：\n[BBOX-1054] 病理诊断：\n[BBOX-1055] 病理诊断：\n[BBOX-1056] 病理诊断：\n[BBOX-1057] 病理诊断：\n[BBOX-1058] 病理诊断：\n[BBOX-1059] 病理诊断：\n[BBOX-1060] 病理诊断：\n[BBOX-1061] 病理诊断：\n[BBOX-1062] 病理诊断：\n[BBOX-1063] 病理诊断：\n[BBOX-1064] 病理诊断：\n[BBOX-1065] 病理诊断：\n[BBOX-1066] 病理诊断：\n[BBOX-1067] 病理诊断：\n[BBOX-1068] 病理诊断：\n[BBOX-1069] 病理诊断：\n[BBOX-1070] 病理诊断：\n[BBOX-1071] 病理诊断：\n[BBOX-1072] 病理诊断：\n[BBOX-1073] 病理诊断：\n[BBOX-1074] 病理诊断：\n[BBOX-1075] 病理诊断：\n[BBOX-1076] 病理诊断：\n[BBOX-1077] 病理诊断：\n[BBOX-1078] 病理诊断：\n[BBOX-1079] 病理诊断：\n[BBOX-1080] 病理诊断：\n[BBOX-1081] 病理诊断：\n[BBOX-1082] 病理诊断：\n[BBOX-1083] 病理诊断：\n[BBOX-1084] 病理诊断：\n[BBOX-1085] 病理诊断：\n[BBOX-1086] 病理诊断：\n[BBOX-1087] 病理诊断：\n[BBOX-1088] 病理诊断：\n[BBOX-1089] 病理诊断：\n[BBOX-1090] 病理诊断：\n[BBOX-1091] 病理诊断：\n[BBOX-1092] 病理诊断：\n[BBOX-1093] 病理诊断：\n[BBOX-1094] 病理诊断：\n[BBOX-1095] 病理诊断：\n[BBOX-1096] 病理诊断：\n[BBOX-1097] 病理诊断：\n[BBOX-1098] 病理诊断：\n[BBOX-1099] 病理诊断：\n[BBOX-1100] 病理诊断：\n[BBOX-1101] 病理诊断：\n[BBOX-1102] 病理诊断：\n[BBOX-1103] 病理诊断：\n[BBOX-1104] 病理诊断：\n[BBOX-1105] 病理诊断：\n[BBOX-1106] 病理诊断：\n[BBOX-1107] 病理诊断：\n[BBOX-1108] 病理诊断：\n[BBOX-1109] 病理诊断：\n[BBOX-1110] 病理诊断：\n[BBOX-1111] 病理诊断：\n[BBOX-1112] 病理诊断：\n[BBOX-1113] 病理诊断：\n[BBOX-1114] 病理诊断：\n[BBOX-1115] 病理诊断：\n[BBOX-1116] 病理诊断：\n[BBOX-1117] 病理诊断：\n[BBOX-1118] 病理诊断：\n[BBOX-1119] 病理诊断：\n[BBOX-1120] 病理诊断：\n[BBOX-1121] 病理诊断：\n[BBOX-1122] 病理诊断：\n[BBOX-1123] 病理诊断：\n[BBOX-1124] 病理诊断：\n[BBOX-1125] 病理诊断：\n[BBOX-1126] 病理诊断：\n[BBOX-1127] 病理诊断：\n[BBOX-1128] 病理诊断：\n[BBOX-1129] 病理诊断：\n[BBOX-1130] 病理诊断：\n[BBOX-1131] 病理诊断：\n[BBOX-1132] 病理诊断：\n[BBOX-1133] 病理诊断：\n[BBOX-1134] 病理诊断：\n[BBOX-1135] 病理诊断：\n[BBOX-1136] 病理诊断：\n[BBOX-1137] 病理诊断：\n[BBOX-1138] 病理诊断：\n[BBOX-1139] 病理诊断：\n[BBOX-1140] 病理诊断：\n[BBOX-1141] 病理诊断：\n[BBOX-1142] 病理诊断：\n[BBOX-1143] 病理诊断：\n[BBOX-1144] 病理诊断：\n[BBOX-1145] 病理诊断：\n[BBOX-1146] 病理诊断：\n[BBOX-1147] 病理诊断：\n[BBOX-1148] 病理诊断：\n[BBOX-1149] 病理诊断：\n[BBOX-1150] 病理诊断：\n[BBOX-1151] 病理诊断：\n[BBOX-1152] 病理诊断：\n[BBOX-1153] 病理诊断：\n[BBOX-1154] 病理诊断：\n[BBOX-1155] 病理诊断：\n[BBOX-1156] 病理诊断：\n[BBOX-1157] 病理诊断：\n[BBOX-1158] 病理诊断：\n[BBOX-1159] 病理诊断：\n[BBOX-1160] 病理诊断：\n[BBOX-1161] 病理诊断：\n[BBOX-1162] 病理诊断：\n[BBOX-1163] 病理诊断：\n[BBOX-1164] 病理诊断：\n[BBOX-1165] 病理诊断：\n[BBOX-1166] 病理诊断：\n[BBOX-1167] 病理诊断：\n[BBOX-1168] 病理诊断：\n[BBOX-1169] 病理诊断：\n[BBOX-1170] 病理诊断：\n[BBOX-1171] 病理诊断：\n[BBOX-1172] 病理诊断：\n[BBOX-1173] 病理诊断：\n[BBOX-1174] 病理诊断：\n[BBOX-1175] 病理诊断：\n[BBOX-1176] 病理诊断：\n[BBOX-1177] 病理诊断：\n[BBOX-1178] 病理诊断：\n[BBOX-1179] 病理诊断：\n[BBOX-1180] 病理诊断：\n[BBOX-1181] 病理诊断：\n[BBOX-1182] 病理诊断：\n[BBOX-1183] 病理诊断：\n[BBOX-1184] 病理诊断：\n[BBOX-1185] 病理诊断：\n[BBOX-1186] 病理诊断：\n[BBOX-1187] 病理诊断：\n[BBOX-1188] 病理诊断：\n[BBOX-1189] 病理诊断：\n[BBOX-1190] 病理诊断：\n[BBOX-1191] 病理诊断：\n[BBOX-1192] 病理诊断：\n[BBOX-1193] 病理诊断：\n[BBOX-1194] 病理诊断：\n[BBOX-1195] 病理诊断：\n[BBOX-1196] 病理诊断：\n[BBOX-1197] 病理诊断：\n[BBOX-1198] 病理诊断：\n[BBOX-1199] 病理诊断：\n[BBOX-1200] 病理诊断：\n[BBOX-1201] 病理诊断：\n[BBOX-1202] 病理诊断：\n[BBOX-1203] 病理诊断：\n[BBOX-1204] 病理诊断：\n[BBOX-1205] 病理诊断：\n[BBOX-1206] 病理诊断：\n[BBOX-1207] 病理诊断：\n[BBOX-1208] 病理诊断：\n[BBOX-1209] 病理诊断：\n[BBOX-1210] 病理诊断：\n[BBOX-1211] 病理诊断：\n[BBOX-1212] 病理诊断：\n[BBOX-1213] 病理诊断：\n[BBOX-1214] 病理诊断：\n[BBOX-1215] 病理诊断：\n[BBOX-1216] 病理诊断：\n[BBOX-1217] 病理诊断：\n[BBOX-1218] 病理诊断：\n[BBOX-1219] 病理诊断：\n[BBOX-1220] 病理诊断：\n[BBOX-1221] 病理诊断：\n[BBOX-1222] 病理诊断：\n[BBOX-1223] 病理诊断：\n[BBOX-1224] 病理诊断：\n[BBOX-1225] 病理诊断：\n[BBOX-1226] 病理诊断：\n[BBOX-1227] 病理诊断：\n[BBOX-1228] 病理诊断：\n[BBOX-1229] 病理诊断：\n[BBOX-1230] 病理诊断：\n[BBOX-1231] 病理诊断：\n[BBOX-1232] 病理诊断：\n[BBOX-1233] 病理诊断：\n[BBOX-1234] 病理诊断：\n[BBOX-1235] 病理诊断：\n[BBOX-1236] 病理诊断：\n[BBOX-1237] 病理诊断：\n[BBOX-1238] 病理诊断：\n[BBOX-1239] 病理诊断：\n[BBOX-1240] 病理诊断：\n[BBOX-1241] 病理诊断：\n[BBOX-1242] 病理诊断：\n[BBOX-1243] 病理诊断：\n[BBOX-1244] 病理诊断：\n[BBOX-1245] 病理诊断：\n[BBOX-1246] 病理诊断：\n[BBOX-1247] 病理诊断：\n[BBOX-1248] 病理诊断：\n[BBOX-1249] 病理诊断：\n[BBOX-1250] 病理诊断：\n[BBOX-1251] 病理诊断：\n[BBOX-1252] 病理诊断：\n[BBOX-1253] 病理诊断：\n[BBOX-1254] 病理诊断：\n[BBOX-1255] 病理诊断：\n[BBOX-1256] 病理诊断：\n[BBOX-1257] 病理诊断：\n[BBOX-1258] 病理诊断：\n[BBOX-1259] 病理诊断：\n[BBOX-1260] 病理诊断：\n[BBOX-1261] 病理诊断：\n[BBOX-1262] 病理诊断：\n[BBOX-1263] 病理诊断：\n[BBOX-1264] 病理诊断：\n[BBOX-1265] 病理诊断：\n[BBOX-1266] 病理诊断：\n[BBOX-1267] 病理诊断：\n[BBOX-1268] 病理诊断：\n[BBOX-1269] 病理诊断：\n[BBOX-1270] 病理诊断：\n[BBOX-1271] 病理诊断：\n[BBOX-1272] 病理诊断：\n[BBOX-1273] 病理诊断：\n[BBOX-1274] 病理诊断：\n[BBOX-1275] 病理诊断：\n[BBOX-1276] 病理诊断：\n[BBOX-1277] 病理诊断：\n[BBOX-1278] 病理诊断：\n[BBOX-1279] 病理诊断：\n[BBOX-1280] 病理诊断：\n[BBOX-1281] 病理诊断：\n[BBOX-1282] 病理诊断：\n[BBOX-1283] 病理诊断：\n[BBOX-1284] 病理诊断：\n[BBOX-1285] 病理诊断：\n[BBOX-1286] 病理诊断：\n[BBOX-1287] 病理诊断：\n[BBOX-1288] 病理诊断：\n[BBOX-1289] 病理诊断：\n[BBOX-1290] 病理诊断：\n[BBOX-1291] 病理诊断：\n[BBOX-1292] 病理诊断：\n[BBOX-1293] 病理诊断：\n[BBOX-1294] 病理诊断：\n[BBOX-1295] 病理诊断：\n[BBOX-1296] 病理诊断：\n[BBOX-1297] 病理诊断：\n[BBOX-1298] 病理诊断：\n[BBOX-1299] 病理诊断：\n[BBOX-1300] 病理诊断：\n[BBOX-1301] 病理诊断：\n[BBOX-1302] 病理诊断：\n[BBOX-1303] 病理诊断：\n[BBOX-1304] 病理诊断：\n[BBOX-1305] 病理诊断：\n[BBOX-1306] 病理诊断：\n[BBOX-1307] 病理诊断：\n[BBOX-1308] 病理诊断：\n[BBOX-1309] 病理诊断：\n[BBOX-1310] 病理诊断：\n[BBOX-1311] 病理诊断：\n[BBOX-1312] 病理诊断：\n[BBOX-1313] 病理诊断：\n[BBOX-1314] 病理诊断：\n[BBOX-1315] 病理诊断：\n[BBOX-1316] 病理诊断：\n[BBOX-1317] 病理诊断：\n[BBOX-1318] 病理诊断：\n[BBOX-1319] 病理诊断：\n[BBOX-1320] 病理诊断：\n[BBOX-1321] 病理诊断：\n[BBOX-1322] 病理诊断：\n[BBOX-1323] 病理诊断：\n[BBOX-1324] 病理诊断：\n[BBOX-1325] 病理诊断：\n[BBOX-1326] 病理诊断：\n[BBOX-1327] 病理诊断：\n[BBOX-1328] 病理诊断：\n[BBOX-1329] 病理诊断：\n[BBOX-1330] 病理诊断：\n[BBOX-1331] 病理诊断：\n[BBOX-1332] 病理诊断：\n[BBOX-1333] 病理诊断：\n[BBOX-1334] 病理诊断：\n[BBOX-1335] 病理诊断：\n[BBOX-1336] 病理诊断：\n[BBOX-1337] 病理诊断：\n[BBOX-1338] 病理诊断：\n[BBOX-1339] 病理诊断：\n[BBOX-1340] 病理诊断：\n[BBOX-1341] 病理诊断：\n[BBOX-1342] 病理诊断：\n[BBOX-1343] 病理诊断：\n[BBOX-1344] 病理诊断：\n[BBOX-1345] 病理诊断：\n[BBOX-1346] 病理诊断：\n[BBOX-1347] 病理诊断：\n[BBOX-1348] 病理诊断：\n[BBOX-1349] 病理诊断：\n[BBOX-1350] 病理诊断：\n[BBOX-1351] 病理诊断：\n[BBOX-1352] 病理诊断：\n[BBOX-1353] 病理诊断：\n[BBOX-1354] 病理诊断：\n[BBOX-1355] 病理诊断：\n[BBOX-1356] 病理诊断：\n[BBOX-1357] 病理诊断：\n[BBOX-1358] 病理诊断：\n[BBOX-1359] 病理诊断：\n[BBOX-1360] 病理诊断：\n[BBOX-1361] 病理诊断：\n[BBOX-1362] 病理诊断：\n[BBOX-1363] 病理诊断：\n[BBOX-1364] 病理诊断：\n[BBOX-1365] 病理诊断：\n[BBOX-1366] 病理诊断：\n[BBOX-1367] 病理诊断：\n[BBOX-1368] 病理诊断：\n[BBOX-1369] 病理诊断：\n[BBOX-1370] 病理诊断：\n[BBOX-1371] 病理诊断：\n[BBOX-1372] 病理诊断：\n[BBOX-1373] 病理诊断：\n[BBOX-1374] 病理诊断：\n[BBOX-1375] 病理诊断：\n[BBOX-1376] 病理诊断：\n[BBOX-1377] 病理诊断：\n[BBOX-1378] 病理诊断：\n[BBOX-1379] 病理诊断：\n[BBOX-1380] 病理诊断：\n[BBOX-1381] 病理诊断：\n[BBOX-1382] 病理诊断：\n[BBOX-1383] 病理诊断：\n[BBOX-1384] 病理诊断：\n[BBOX-1385] 病理诊断：\n[BBOX-1386] 病理诊断：\n[BBOX-1387] 病理诊断：\n[BBOX-1388] 病理诊断：\n[BBOX-1389] 病理诊断：\n[BBOX-1390] 病理诊断：\n[BBOX-1391] 病理诊断：\n[BBOX-1392] 病理诊断：\n[BBOX-1393] 病理诊断：\n[BBOX-1394] 病理诊断：\n[BBOX-1395] 病理诊断：\n[BBOX-1396] 病理诊断：\n[BBOX-1397] 病理诊断：\n[BBOX-1398] 病理诊断：\n[BBOX-1399] 病理诊断：\n[BBOX-1400] 病理诊断：\n[BBOX-1401] 病理诊断：\n[BBOX-1402] 病理诊断：\n[BBOX-1403] 病理诊断：\n[BBOX-1404] 病理诊断：\n[BBOX-1405] 病理诊断：\n[BBOX-1406] 病理诊断：\n[BBOX-1407] 病理诊断：\n[BBOX-1408] 病理诊断：\n[BBOX-1409] 病理诊断：\n[BBOX-1410] 病理诊断：\n[BBOX-1411] 病理诊断：\n[BBOX-1412] 病理诊断：\n[BBOX-1413] 病理诊断：\n[BBOX-1414] 病理诊断：\n[BBOX-1415] 病理诊断：\n[BBOX-1416] 病理诊断：\n[BBOX-1417] 病理诊断：\n[BBOX-1418] 病理诊断：\n[BBOX-1419] 病理诊断：\n[BBOX-1420] 病理诊断：\n[BBOX-1421] 病理诊断：\n[BBOX-1422] 病理诊断：\n[BBOX-1423] 病理诊断：\n[BBOX-1424] 病理诊断：\n[BBOX-1425] 病理诊断：\n[BBOX-1426] 病理诊断：\n[BBOX-1427] 病理诊断：\n[BBOX-1428] 病理诊断：\n[BBOX-1429] 病理诊断：\n[BBOX-1430] 病理诊断：\n[BBOX-1431] 病理诊断：\n[BBOX-1432] 病理诊断：\n[BBOX-1433] 病理诊断：\n[BBOX-1434] 病理诊断：\n[BBOX-1435] 病理诊断：\n[BBOX-1436] 病理诊断：\n[BBOX-1437] 病理诊断：\n[BBOX-1438] 病理诊断：\n[BBOX-1439] 病理诊断：\n[BBOX-1440] 病理诊断：\n[BBOX-1441] 病理诊断：\n[BBOX-1442] 病理诊断：\n[BBOX-1443] 病理诊断：\n[BBOX-1444] 病理诊断：\n[BBOX-1445] 病理诊断：\n[BBOX-1446] 病理诊断：\n[BBOX-1447] 病理诊断：\n[BBOX-1448] 病理诊断：\n[BBOX-1449] 病理诊断：\n[BBOX-1450] 病理诊断：\n[BBOX-1451] 病理诊断：\n[BBOX-1452] 病理诊断：\n[BBOX-1453] 病理诊断：\n[BBOX-1454] 病理诊断：\n[BBOX-1455] 病理诊断：\n[BBOX-1456] 病理诊断：\n[BBOX-1457] 病理诊断：\n[BBOX-1458] 病理诊断：\n[BBOX-1459] 病理诊断：\n[BBOX-1460] 病理诊断：\n[BBOX-1461] 病理诊断：\n[BBOX-1462] 病理诊断：\n[BBOX-1463] 病理诊断：\n[BBOX-1464] 病理诊断：\n[BBOX-1465] 病理诊断：\n[BBOX-1466] 病理诊断：\n[BBOX-1467] 病理诊断：\n[BBOX-1468] 病理诊断：\n[BBOX-1469] 病理诊断：\n[BBOX-1470] 病理诊断：\n[BBOX-1471] 病理诊断：\n[BBOX-1472] 病理诊断：\n[BBOX-1473] 病理诊断：\n[BBOX-1474] 病理诊断：\n[BBOX-1475] 病理诊断：\n[BBOX-1476] 病理诊断：\n[BBOX-1477] 病理诊断：\n[BBOX-1478] 病理诊断：\n[BBOX-1479] 病理诊断：\n[BBOX-1480] 病理诊断：\n[BBOX-1481] 病理诊断：\n[BBOX-1482] 病理诊断：\n[BBOX-1483] 病理诊断：\n[BBOX-1484] 病理诊断：\n[BBOX-1485] 病理诊断：\n[BBOX-1486] 病理诊断：\n[BBOX-1487] 病理诊断：\n[BBOX-1488] 病理诊断：\n[BBOX-1489] 病理诊断：\n[BBOX-1490] 病理诊断：\n[BBOX-1491] 病理诊断：\n[BBOX-1492] 病理诊断：\n[BBOX-1493] 病理诊断：\n[BBOX-1494] 病理诊断：\n[BBOX-1495] 病理诊断：\n[BBOX-1496] 病理诊断：\n[BBOX-1497] 病理诊断：\n[BBOX-1498] 病理诊断：\n[BBOX-1499] 病理诊断：\n[BBOX-1500] 病理诊断：\n[BBOX-1501] 病理诊断：\n[BBOX-1502] 病理诊断：\n[BBOX-1503] 病理诊断：\n[BBOX-1504] 病理诊断：\n[BBOX-1505] 病理诊断：\n[BBOX-1506] 病理诊断：\n[BBOX-1507] 病理诊断：\n[BBOX-1508] 病理诊断：\n[BBOX-1509] 病理诊断：\n[BBOX-1510] 病理诊断：\n[BBOX-1511] 病理诊断：\n[BBOX-1512] 病理诊断：\n[BBOX-1513] 病理诊断：\n[BBOX-1514] 病理诊断：\n[BBOX-1515] 病理诊断：\n[BBOX-1516] 病理诊断：\n[BBOX-1517] 病理诊断：\n[BBOX-1518] 病理诊断：\n[BBOX-1519] 病理诊断：\n[BBOX-1520] 病理诊断：\n[BBOX-1521] 病理诊断：\n[BBOX-1522] 病理诊断：\n[BBOX-1523] 病理诊断：\n[BBOX-1524] 病理诊断：\n[BBOX-1525] 病理诊断：\n[BBOX-1526] 病理诊断：\n[BBOX-1527] 病理诊断：\n[BBOX-1528] 病理诊断：\n[BBOX-1529] 病理诊断：\n[BBOX-1530] 病理诊断：\n[BBOX-1531] 病理诊断：\n[BBOX-1532] 病理诊断：\n[BBOX-1533] 病理诊断：\n[BBOX-1534] 病理诊断：\n[BBOX-1535] 病理诊断：\n[BBOX-1536] 病理诊断：\n[BBOX-1537] 病理诊断：\n[BBOX-1538] 病理诊断：\n[BBOX-1539] 病理诊断：\n[BBOX-1540] 病理诊断：\n[BBOX-1541] 病理诊断：\n[BBOX-1542] 病理诊断：\n[BBOX-1543] 病理诊断：\n[BBOX-1544] 病理诊断：\n[BBOX-1545] 病理诊断：\n[BBOX-1546] 病理诊断：\n[BBOX-1547] 病理诊断：\n[BBOX-1548] 病理诊断：\n[BBOX-1549] 病理诊断：\n[BBOX-1550] 病理诊断：\n[BBOX-1551] 病理诊断：\n[BBOX-1552] 病理诊断：\n[BBOX-1553] 病理诊断：\n[BBOX-1554] 病理诊断：\n[BBOX-1555] 病理诊断：\n[BBOX-1556] 病理诊断：\n[BBOX-1557] 病理诊断：\n[BBOX-1558] 病理诊断：\n[BBOX-1559] 病理诊断：\n[BBOX-1560] 病理诊断：\n[BBOX-1561] 病理诊断：\n[BBOX-1562] 病理诊断：\n[BBOX-1563] 病理诊断：\n[BBOX-1564] 病理诊断：\n[BBOX-1565] 病理诊断：\n[BBOX-1566] 病理诊断：\n[BBOX-1567] 病理诊断：\n[BBOX-1568] 病理诊断：\n[BBOX-1569] 病理诊断：\n[BBOX-1570] 病理诊断：\n[BBOX-1571] 病理诊断：\n[BBOX-1572] 病理诊断：\n[BBOX-1573] 病理诊断：\n[BBOX-1574] 病理诊断：\n[BBOX-1575] 病理诊断：\n[BBOX-1576] 病理诊断：\n[BBOX-1577] 病理诊断：\n[BBOX-1578] 病理诊断：\n[BBOX-1579] 病理诊断：\n[BBOX-1580] 病理诊断：\n[BBOX-1581] 病理诊断：\n[BBOX-1582] 病理诊断：\n[BBOX-1583] 病理诊断：\n[BBOX-1584] 病理诊断：\n[BBOX-1585] 病理诊断：\n[BBOX-1586] 病理诊断：\n[BBOX-1587] 病理诊断：\n[BBOX-1588] 病理诊断：\n[BBOX-1589] 病理诊断：\n[BBOX-1590] 病理诊断：\n[BBOX-1591] 病理诊断：\n[BBOX-1592] 病理诊断：\n[BBOX-1593] 病理诊断：\n[BBOX-1594] 病理诊断：\n[BBOX-1595] 病理诊断：\n[BBOX-1596] 病理诊断：\n[BBOX-1597] 病理诊断：\n[BBOX-1598] 病理诊断：\n[BBOX-1599] 病理诊断：\n[BBOX-1600] 病理诊断：\n[BBOX-1601] 病理诊断：\n[BBOX-1602] 病理诊断：\n[BBOX-1603] 病理诊断：\n[BBOX-1604] 病理诊断：\n[BBOX-1605] 病理诊断：\n[BBOX-1606] 病理诊断：\n[BBOX-1607] 病理诊断：\n[BBOX-1608] 病理诊断：\n[BBOX-1609] 病理诊断：\n[BBOX-1610] 病理诊断：\n[BBOX-1611] 病理诊断：\n[BBOX-1612] 病理诊断：\n[BBOX-1613] 病理诊断：\n[BBOX-1614] 病理诊断：\n[BBOX-1615] 病理诊断：\n[BBOX-1616] 病理诊断：\n[BBOX-1617] 病理诊断：\n[BBOX-1618] 病理诊断：\n[BBOX-1619] 病理诊断：\n[BBOX-1620] 病理诊断：\n[BBOX-1621] 病理诊断：\n[BBOX-1622] 病理诊断：\n[BBOX-1623] 病理诊断：\n[BBOX-1624] 病理诊断：\n[BBOX-1625] 病理诊断：\n[BBOX-1626] 病理诊断：\n[BBOX-1627] 病理诊断：\n[BBOX-1628] 病理诊断：\n[BBOX-1629] 病理诊断：\n[BBOX-1630] 病理诊断：\n[BBOX-1631] 病理诊断：\n[BBOX-1632] 病理诊断：\n[BBOX-1633] 病理诊断：\n[BBOX-1634] 病理诊断：\n[BBOX-1635] 病理诊断：\n[BBOX-1636] 病理诊断：\n[BBOX-1637] 病理诊断：\n[BBOX-1638] 病理诊断：\n[BBOX-1639] 病理诊断：\n[BBOX-1640] 病理诊断：\n[BBOX-1641] 病理诊断：\n[BBOX-1642] 病理诊断：\n[BBOX-1643] 病理诊断：\n[BBOX-1644] 病理诊断：\n[BBOX-1645] 病理诊断：\n[BBOX-1646] 病理诊断：\n[BBOX-1647] 病理诊断：\n[BBOX-1648] 病理诊断：\n[BBOX-1649] 病理诊断：\n[BBOX-1650] 病理诊断：\n[BBOX-1651] 病理诊断：\n[BBOX-1652] 病理诊断：\n[BBOX-1653] 病理诊断：\n[BBOX-1654] 病理诊断：\n[BBOX-1655] 病理诊断：\n[BBOX-1656] 病理诊断：\n[BBOX-1657] 病理诊断：\n[BBOX-1658] 病理诊断：\n[BBOX-1659] 病理诊断：\n[BBOX-1660] 病理诊断：\n[BBOX-1661] 病理诊断：\n[BBOX-1662] 病理诊断：\n[BBOX-1663] 病理诊断：\n[BBOX-1664] 病理诊断：\n[BBOX-1665] 病理诊断：\n[BBOX-1666] 病理诊断：\n[BBOX-1667] 病理诊断：\n[BBOX-1668] 病理诊断：\n[BBOX-1669] 病理诊断：\n[BBOX-1670] 病理诊断：\n[BBOX-1671] 病理诊断：\n[BBOX-1672] 病理诊断：\n[BBOX-1673] 病理诊断：\n[BBOX-1674] 病理诊断：\n[BBOX-1675] 病理诊断：\n[BBOX-1676] 病理诊断：\n[BBOX-1677] 病理诊断：\n[BBOX-1678] 病理诊断：\n[BBOX-1679] 病理诊断：\n[BBOX-1680] 病理诊断：\n[BBOX-1681] 病理诊断：\n[BBOX-1682] 病理诊断：\n[BBOX-1683] 病理诊断：\n[BBOX-1684] 病理诊断：\n[BBOX-1685] 病理诊断：\n[BBOX-1686] 病理诊断：\n[BBOX-1687] 病理诊断：\n[BBOX-1688] 病理诊断：\n[BBOX-1689] 病理诊断：\n[BBOX-1690] 病理诊断：\n[BBOX-1691] 病理诊断：\n[BBOX-1692] 病理诊断：\n[BBOX-1693] 病理诊断：\n[BBOX-1694] 病理诊断：\n[BBOX-1695] 病理诊断：\n[BBOX-1696] 病理诊断：\n[BBOX-1697] 病理诊断：\n[BBOX-1698] 病理诊断：\n[BBOX-1699] 病理诊断：\n[BBOX-1700] 病理诊断：\n[BBOX-1701] 病理诊断：\n[BBOX-1702] 病理诊断：\n[BBOX-1703] 病理诊断：\n[BBOX-1704] 病理诊断：\n[BBOX-1705] 病理诊断：\n[BBOX-1706] 病理诊断：\n[BBOX-1707] 病理诊断：\n[BBOX-1708] 病理诊断：\n[BBOX-1709] 病理诊断：\n[BBOX-1710] 病理诊断：\n[BBOX-1711] 病理诊断：\n[BBOX-1712] 病理诊断：\n[BBOX-1713] 病理诊断：\n[BBOX-1714] 病理诊断：\n[BBOX-1715] 病理诊断：\n[BBOX-1716] 病理诊断：\n[BBOX-1717] 病理诊断：\n[BBOX-1718] 病理诊断：\n[BBOX-1719] 病理诊断：\n[BBOX-1720] 病理诊断：\n[BBOX-1721] 病理诊断：\n[BBOX-1722] 病理诊断：\n[BBOX-1723] 病理诊断：\n[BBOX-1724] 病理诊断：\n[BBOX-1725] 病理诊断：\n[BBOX-1726] 病理诊断：\n[BBOX-1727] 病理诊断：\n[BBOX-1728] 病理诊断：\n[BBOX-1729] 病理诊断：\n[BBOX-1730] 病理诊断：\n[BBOX-1731] 病理诊断：\n[BBOX-1732] 病理诊断：\n[BBOX-1733] 病理诊断：\n[BBOX-1734] 病理诊断：\n[BBOX-1735] 病理诊断：\n[BBOX-1736] 病理诊断：\n[BBOX-1737] 病理诊断：\n[BBOX-1738] 病理诊断：\n[BBOX-1739] 病理诊断：\n[BBOX-1740] 病理诊断：\n[BBOX-1741] 病理诊断：\n[BBOX-1742] 病理诊断：\n[BBOX-1743] 病理诊断：\n[BBOX-1744] 病理诊断：\n[BBOX-1745] 病理诊断：\n[BBOX-1746] 病理诊断：\n[BBOX-1747] 病理诊断：\n[BBOX-1748] 病理诊断：\n[BBOX-1749] 病理诊断：\n[BBOX-1750] 病理诊断：\n[BBOX-1751] 病理诊断：\n[BBOX-1752] 病理诊断：\n[BBOX-1753] 病理诊断：\n[BBOX-1754] 病理诊断：\n[BBOX-1755] 病理诊断：\n[BBOX-1756] 病理诊断：\n[BBOX-1757] 病理诊断：\n[BBOX-1758] 病理诊断：\n[BBOX-1759] 病理诊断：\n[BBOX-1760] 病理诊断：\n[BBOX-1761] 病理诊断：\n[BBOX-1762] 病理诊断：\n[BBOX-1763] 病理诊断：\n[BBOX-1764] 病理诊断：\n[BBOX-1765] 病理诊断：\n[BBOX-1766] 病理诊断：\n[BBOX-1767] 病理诊断：\n[BBOX-1768] 病理诊断：\n[BBOX-1769] 病理诊断：\n[BBOX-1770] 病理诊断：\n[BBOX-1771] 病理诊断：\n[BBOX-1772] 病理诊断：\n[BBOX-1773] 病理诊断：\n[BBOX-1774] 病理诊断：\n[BBOX-1775] 病理诊断：\n[BBOX-1776] 病理诊断：\n[BBOX-1777] 病理诊断：\n[BBOX-1778] 病理诊断：\n[BBOX-1779] 病理诊断：\n[BBOX-1780] 病理诊断：\n[BBOX-1781] 病理诊断：\n[BBOX-1782] 病理诊断：\n[BBOX-1783] 病理诊断：\n[BBOX-1784] 病理诊断：\n[BBOX-1785] 病理诊断：\n[BBOX-1786] 病理诊断：\n[BBOX-1787] 病理诊断：\n[BBOX-1788] 病理诊断：\n[BBOX-1789] 病理诊断：\n[BBOX-1790] 病理诊断：\n[BBOX-1791] 病理诊断：\n[BBOX-1792] 病理诊断：\n[BBOX-1793] 病理诊断：\n[BBOX-1794] 病理诊断：\n[BBOX-1795] 病理诊断：\n[BBOX-1796] 病理诊断：\n[BBOX-1797] 病理诊断：\n[BBOX-1798] 病理诊断：\n[BBOX-1799] 病理诊断：\n[BBOX-1800] 病理诊断：\n[BBOX-1801] 病理诊断：\n[BBOX-1802] 病理诊断：\n[BBOX-1803] 病理诊断：\n[BBOX-1804] 病理诊断：\n[BBOX-1805] 病理诊断：\n[BBOX-1806] 病理诊断：\n[BBOX-1807] 病理诊断：\n[BBOX-1808] 病理诊断：\n[BBOX-1809] 病理诊断：\n[BBOX-1810] 病理诊断：\n[BBOX-1811] 病理诊断：\n[BBOX-1812] 病理诊断：\n[BBOX-1813] 病理诊断：\n[BBOX-1814] 病理诊断：\n[BBOX-1815] 病理诊断：\n[BBOX-1816] 病理诊断：\n[BBOX-1817] 病理诊断：\n[BBOX-1818] 病理诊断：\n[BBOX-1819] 病理诊断：\n[BBOX-1820] 病理诊断：\n[BBOX-1821] 病理诊断：\n[BBOX-1822] 病理诊断：\n[BBOX-1823] 病理诊断：\n[BBOX-1824] 病理诊断：\n[BBOX-1825] 病理诊断：\n[BBOX-1826] 病理诊断：\n[BBOX-1827] 病理诊断：\n[BBOX-1828] 病理诊断：\n[BBOX-1829] 病理诊断：\n[BBOX-1830] 病理诊断：\n[BBOX-1831] 病理诊断：\n[BBOX-1832] 病理诊断：\n[BBOX-1833] 病理诊断：\n[BBOX-1834] 病理诊断：\n[BBOX-1835] 病理诊断：\n[BBOX-1836] 病理诊断：\n[BBOX-1837] 病理诊断：\n[BBOX-1838] 病理诊断：\n[BBOX-1839] 病理诊断：\n[BBOX-1840] 病理诊断：\n[BBOX-1841] 病理诊断：\n[BBOX-1842] 病理诊断：\n[BBOX-1843] 病理诊断：\n[BBOX-1844] 病理诊断：\n[BBOX-1845] 病理诊断：\n[BBOX-1846] 病理诊断：\n[BBOX-1847] 病理诊断：\n[BBOX-1848] 病理诊断：\n[BBOX-1849] 病理诊断：\n[BBOX-1850] 病理诊断：\n[BBOX-1851] 病理诊断：\n[BBOX-1852] 病理诊断：\n[BBOX-1853] 病理诊断：\n[BBOX-1854] 病理诊断：\n[BBOX-1855] 病理诊断：\n[BBOX-1856] 病理诊断：\n[BBOX-1857] 病理诊断：\n[BBOX-1858] 病理诊断：\n[BBOX-1859] 病理诊断：\n[BBOX-1860] 病理诊断：\n[BBOX-1861] 病理诊断：\n[BBOX-1862] 病理诊断：\n[BBOX-1863] 病理诊断：\n[BBOX-1864] 病理诊断：\n[BBOX-1865] 病理诊断：\n[BBOX-1866] 病理诊断：\n[BBOX-1867] 病理诊断：\n[BBOX-1868] 病理诊断：\n[BBOX-1869] 病理诊断：\n[BBOX-1870] 病理诊断：\n[BBOX-1871] 病理诊断：\n[BBOX-1872] 病理诊断：\n[BBOX-1873] 病理诊断：\n[BBOX-1874] 病理诊断：\n[BBOX-1875] 病理诊断：\n[BBOX-1876] 病理诊断：\n[BBOX-1877] 病理诊断：\n[BBOX-1878] 病理诊断：\n[BBOX-1879] 病理诊断：\n[BBOX-1880] 病理诊断：\n[BBOX-1881] 病理诊断：\n[BBOX-1882] 病理诊断：\n[BBOX-1883] 病理诊断：\n[BBOX-1884] 病理诊断：\n[BBOX-1885] 病理诊断：\n[BBOX-1886] 病理诊断：\n[BBOX-1887] 病理诊断：\n[BBOX-1888] 病理诊断：\n[BBOX-1889] 病理诊断：\n[BBOX-1890] 病理诊断：\n[BBOX-1891] 病理诊断：\n[BBOX-1892] 病理诊断：\n[BBOX-1893] 病理诊断：\n[BBOX-1894] 病理诊断：\n[BBOX-1895] 病理诊断：\n[BBOX-1896] 病理诊断：\n[BBOX-1897] 病理诊断：\n[BBOX-1898] 病理诊断：\n[BBOX-1899] 病理诊断：\n[BBOX-1900] 病理诊断：\n[BBOX-1901] 病理诊断：\n[BBOX-1902] 病理诊断：\n[BBOX-1903] 病理诊断：\n[BBOX-1904] 病理诊断：\n[BBOX-1905] 病理诊断：\n[BBOX-1906] 病理诊断：\n[BBOX-1907] 病理诊断：\n[BBOX-1908] 病理诊断：\n[BBOX-1909] 病理诊断：\n[BBOX-1910] 病理诊断：\n[BBOX-1911] 病理诊断：\n[BBOX-1912] 病理诊断：\n[BBOX-1913] 病理诊断：\n[BBOX-1914] 病理诊断：\n[BBOX-1915] 病理诊断：\n[BBOX-1916] 病理诊断：\n[BBOX-1917] 病理诊断：\n[BBOX-1918] 病理诊断：\n[BBOX-1919] 病理诊断：\n[BBOX-1920] 病理诊断：\n[BBOX-1921] 病理诊断：\n[BBOX-1922] 病理诊断：\n[BBOX-1923] 病理诊断：\n[BBOX-1924] 病理诊断：\n[BBOX-1925] 病理诊断：\n[BBOX-1926] 病理诊断：\n[BBOX-1927] 病理诊断：\n[BBOX-1928] 病理诊断：\n[BBOX-1929] 病理诊断：\n[BBOX-1930] 病理诊断：\n[BBOX-1931] 病理诊断：\n[BBOX-1932] 病理诊断：\n[BBOX-1933] 病理诊断：\n[BBOX-1934] 病理诊断：\n[BBOX-1935] 病理诊断：\n[BBOX-1936] 病理诊断：\n[BBOX-1937] 病理诊断：\n[BBOX-1938] 病理诊断：\n[BBOX-1939] 病理诊断：\n[BBOX-1940] 病理诊断：\n[BBOX-1941] 病理诊断：\n[BBOX-1942] 病理诊断：\n[BBOX-1943] 病理诊断：\n[BBOX-1944] 病理诊断：\n[BBOX-1945] 病理诊断：\n[BBOX-1946] 病理诊断：\n[BBOX-1947] 病理诊断：\n[BBOX-1948] 病理诊断：\n[BBOX-1949] 病理诊断：\n[BBOX-1950] 病理诊断：\n[BBOX-1951] 病理诊断：\n[BBOX-1952] 病理诊断：\n[BBOX-1953] 病理诊断：\n[BBOX-1954] 病理诊断：\n[BBOX-1955] 病理诊断：\n[BBOX-1956] 病理诊断：\n[BBOX-1957] 病理诊断：\n[BBOX-1958] 病理诊断：\n[BBOX-1959] 病理诊断：\n[BBOX-1960] 病理诊断：\n[BBOX-1961] 病理诊断：\n[BBOX-1962] 病理诊断：\n[BBOX-1963] 病理诊断：\n[BBOX-1964] 病理诊断：\n[BBOX-1965] 病理诊断：\n[BBOX-1966] 病理诊断：\n[BBOX-1967] 病理诊断：\n[BBOX-1968] 病理诊断：\n[BBOX-1969] 病理诊断：\n[BBOX-1970] 病理诊断：\n[BBOX-1971] 病理诊断：\n[BBOX-1972] 病理诊断：\n[BBOX-1973] 病理诊断：\n[BBOX-1974] 病理诊断：\n[BBOX-1975] 病理诊断：\n[BBOX-1976] 病理诊断：\n[BBOX-1977] 病理诊断：\n[BBOX-1978] 病理诊断：\n[BBOX-1979] 病理诊断：\n[BBOX-1980] 病理诊断：\n[BBOX-1981] 病理诊断：\n[BBOX-1982] 病理诊断：\n[BBOX-1983] 病理诊断：\n[BBOX-1984] 病理诊断：\n[BBOX-1985] 病理诊断：\n[BBOX-1986] 病理诊断：\n[BBOX-1987] 病理诊断：\n[BBOX-1988] 病理诊断：\n[BBOX-1989] 病理诊断：\n[BBOX-1990] 病理诊断：\n[BBOX-1991] 病理诊断：\n[BBOX-1992] 病理诊断：\n[BBOX-1993] 病理诊断：\n[BBOX-1994] 病理诊断：\n[BBOX-1995] 病理诊断：\n[BBOX-1996] 病理诊断：\n[BBOX-1997] 病理诊断：\n[BBOX-1998] 病理诊断：\n[BBOX-1999] 病理诊断：\n[BBOX-2000] 病理诊断：\n[BBOX-2001] 病理诊断：\n[BBOX-2002] 病理诊断：\n[BBOX-2003] 病理诊断：\n[BBOX-2004] 病理诊断：\n[BBOX-2005] 病理诊断：\n[BBOX-2006] 病理诊断：\n[BBOX-2007] 病理诊断：\n[BBOX-2008] 病理诊断：\n[BBOX-2009] 病理诊断：\n[BBOX-2010] 病理诊断：\n[BBOX-2011] 病理诊断：\n[BBOX-2012] 病理诊断：\n[BBOX-2013] 病理诊断：\n[BBOX-2014] 病理诊断：\n[BBOX-2015] 病理诊断：\n[BBOX-2016] 病理诊断：\n[BBOX-2017] 病理诊断：\n[BBOX-2018] 病理诊断：\n[BBOX-2019] 病理诊断：\n[BBOX-2020] 病理诊断：\n[BBOX-2021] 病理诊断：\n[BBOX-2022] 病理诊断：\n[BBOX-2023] 病理诊断：\n[BBOX-2024] 病理诊断：\n[BBOX-2025] 病理诊断：\n[BBOX-2026] 病理诊断：\n[BBOX-2027] 病理诊断：\n[BBOX-2028] 病理诊断：\n[BBOX-2029] 病理诊断：\n[BBOX-2030] 病理诊断：\n[BBOX-2031] 病理诊断：\n[BBOX-2032] 病理诊断：\n[BBOX-2033] 病理诊断：\n[BBOX-2034] 病理诊断：\n[BBOX-2035] 病理诊断：\n[BBOX-2036] 病理诊断：\n[BBOX-2037] 病理诊断：\n[BBOX-2038] 病理诊断：\n[BBOX-2039] 病理诊断：\n[BBOX-2040] 病理诊断：\n[BBOX-2041] 病理诊断：\n[BBOX-2042] 病理诊断：\n[BBOX-2043] 病理诊断：\n[BBOX-2044] 病理诊断：\n[BBOX-2045] 病理诊断：\n[BBOX-2046] 病理诊断：\n[BBOX-2047] 病理诊断：\n[BBOX-2048] 病理诊断：\n[BBOX-2049] 病理诊断：\n[BBOX-2050] 病理诊断：\n[BBOX-2051] 病理诊断：\n[BBOX-2052] 病理诊断：\n[BBOX-2053] 病理诊断：\n[BBOX-2054] 病理诊断：\n[BBOX-2055] 病理诊断：\n[BBOX-2056] 病理诊断：\n[BBOX-2057] 病理诊断：\n[BBOX-2058] 病理诊断：\n[BBOX-2059] 病理诊断：\n[BBOX-2060] 病理诊断：\n[BBOX-2061] 病理诊断：\n[BBOX-2062] 病理诊断：\n[BBOX-2063] 病理诊断：\n[BBOX-2064] 病理诊断：\n[BBOX-2065] 病理诊断：\n[BBOX-2066] 病理诊断：\n[BBOX-2067] 病理诊断：\n[BBOX-2068] 病理诊断：\n[BBOX-2069] 病理诊断：\n[BBOX-2070] 病理诊断：\n[BBOX-2071] 病理诊断：\n[BBOX-2072] 病理诊断：\n[BBOX-2073] 病理诊断：\n[BBOX-2074] 病理诊断：\n[BBOX-2075] 病理诊断：\n[BBOX-2076] 病理诊断：\n[BBOX-2077] 病理诊断：\n[BBOX-2078] 病理诊断：\n[BBOX-2079] 病理诊断：\n[BBOX-2080] 病理诊断：\n[BBOX-2081] 病理诊断：\n[BBOX-2082] 病理诊断：\n[BBOX-2083] 病理诊断：\n[BBOX-2084] 病理诊断：\n[BBOX-2085] 病理诊断：\n[BBOX-2086] 病理诊断：\n[BBOX-2087] 病理诊断：\n[BBOX-2088] 病理诊断：\n[BBOX-2089] 病理诊断：\n[BBOX-2090] 病理诊断：\n[BBOX-2091] 病理诊断：\n[BBOX-2092] 病理诊断：\n[BBOX-2093] 病理诊断：\n[BBOX-2094] 病理诊断：\n[BBOX-2095] 病理诊断：\n[BBOX-2096] 病理诊断：\n[BBOX-2097] 病理诊断：\n[BBOX-2098] 病理诊断：\n[BBOX-2099] 病理诊断：\n[BBOX-2100] 病理诊断：\n[BBOX-2101] 病理诊断：\n[BBOX-2102] 病理诊断：\n[BBOX-2103] 病理诊断：\n[BBOX-2104] 病理诊断：\n[BBOX-2105] 病理诊断：\n[BBOX-2106] 病理诊断：\n[BBOX-2107] 病理诊断：\n[BBOX-2108] 病理诊断：\n[BBOX-2109] 病理诊断：\n[BBOX-2110] 病理诊断：\n[BBOX-2111] 病理诊断：\n[BBOX-2112] 病理诊断：\n[BBOX-2113] 病理诊断：\n[BBOX-2114] 病理诊断：\n[BBOX-2115] 病理诊断：\n[BBOX-2116] 病理诊断：\n[BBOX-2117] 病理诊断：\n[BBOX-2118] 病理诊断：\n[BBOX-2119] 病理诊断：\n[BBOX-2120] 病理诊断：\n[BBOX-2121] 病理诊断：\n[BBOX-2122] 病理诊断：\n[BBOX-2123] 病理诊断：\n[BBOX-2124] 病理诊断：\n[BBOX-2125] 病理诊断：\n[BBOX-2126] 病理诊断：\n[BBOX-2127] 病理诊断：\n[BBOX-2128] 病理诊断：\n[BBOX-2129] 病理诊断：\n[BBOX-2130] 病理诊断：\n[BBOX-2131] 病理诊断：\n[BBOX-2132] 病理诊断：\n[BBOX-2133] 病理诊断：\n[BBOX-2134] 病理诊断：\n[BBOX-2135] 病理诊断：\n[BBOX-2136] 病理诊断：\n[BBOX-2137] 病理诊断：\n[BBOX-2138] 病理诊断：\n[BBOX-2139] 病理诊断：\n[BBOX-2140] 病理诊断：\n[BBOX-2141] 病理诊断：\n[BBOX-2142] 病理诊断：\n[BBOX-2143] 病理诊断：\n[BBOX-2144] 病理诊断：\n[BBOX-2145] 病理诊断：\n[BBOX-2146] 病理诊断：\n[BBOX-2147] 病理诊断：\n[BBOX-2148] 病理诊断：\n[BBOX-2149] 病理诊断：\n[BBOX-2150] 病理诊断：\n[BBOX-2151] 病理诊断：\n[BBOX-2152] 病理诊断：\n[BBOX-2153] 病理诊断：\n[BBOX-2154] 病理诊断：\n[BBOX-2155] 病理诊断：\n[BBOX-2156] 病理诊断：\n[BBOX-2157] 病理诊断：\n[BBOX-2158] 病理诊断：\n[BBOX-2159] 病理诊断：\n[BBOX-2160] 病理诊断：\n[BBOX-2161] 病理诊断：\n[BBOX-2162] 病理诊断：\n[BBOX-2163] 病理诊断：\n[BBOX-2164] 病理诊断：\n[BBOX-2165] 病理诊断：\n[BBOX-2166] 病理诊断：\n[BBOX-2167] 病理诊断：\n[BBOX-2168] 病理诊断：\n[BBOX-2169] 病理诊断：\n[BBOX-2170] 病理诊断：\n[BBOX-2171] 病理诊断：\n[BBOX-2172] 病理诊断：\n[BBOX-2173] 病理诊断：\n[BBOX-2174] 病理诊断：\n[BBOX-2175] 病理诊断：\n[BBOX-2176] 病理诊断：\n[BBOX-2177] 病理诊断：\n[BBOX-2178] 病理诊断：\n[BBOX-2179] 病理诊断：\n[BBOX-2180] 病理诊断：\n[BBOX-2181] 病理诊断：\n[BBOX-2182] 病理诊断：\n[BBOX-2183] 病理诊断：\n[BBOX-2184] 病理诊断：\n[BBOX-2185] 病理诊断：\n[BBOX-2186] 病理诊断：\n[BBOX-2187] 病理诊断：\n[BBOX-2188] 病理诊断：\n[BBOX-2189] 病理诊断：\n[BBOX-2190] 病理诊断：\n[BBOX-2191] 病理诊断：\n[BBOX-2192] 病理诊断：\n[BBOX-2193] 病理诊断：\n[BBOX-2194] 病理诊断：\n[BBOX-2195] 病理诊断：\n[BBOX-2196] 病理诊断：\n[BBOX-2197] 病理诊断：\n[BBOX-2198] 病理诊断：\n[BBOX-2199] 病理诊断：\n[BBOX-2200] 病理诊断：\n[BBOX-2201] 病理诊断：\n[BBOX-2202] 病理诊断：\n[BBOX-2203] 病理诊断：\n[BBOX-2204] 病理诊断：\n[BBOX-2205] 病理诊断：\n[BBOX-2206] 病理诊断：\n[BBOX-2207] 病理诊断：\n[BBOX-2208] 病理诊断：\n[BBOX-2209] 病理诊断：\n[BBOX-2210] 病理诊断：\n[BBOX-2211] 病理诊断：\n[BBOX-2212] 病理诊断：\n[BBOX-2213] 病理诊断：\n[BBOX-2214] 病理诊断：\n[BBOX-2215] 病理诊断：\n[BBOX-2216] 病理诊断：\n[BBOX-2217] 病理诊断：\n[BBOX-2218] 病理诊断：\n[BBOX-2219] 病理诊断：\n[BBOX-2220] 病理诊断：\n[BBOX-2221] 病理诊断：\n[BBOX-2222] 病理诊断：\n[BBOX-2223] 病理诊断：\n[BBOX-2224] 病理诊断：\n[BBOX-2225] 病理诊断：\n[BBOX-2226] 病理诊断：\n[BBOX-2227] 病理诊断：\n[BBOX-2228] 病理诊断：\n[BBOX-2229] 病理诊断：\n[BBOX-2230] 病理诊断：\n[BBOX-2231] 病理诊断：\n[BBOX-2232] 病理诊断：\n[BBOX-2233] 病理诊断：\n[BBOX-2234] 病理诊断：\n[BBOX-2235] 病理诊断：\n[BBOX-2236] 病理诊断：\n[BBOX-2237] 病理诊断：\n[BBOX-2238] 病理诊断：\n[BBOX-2239] 病理诊断：\n[BBOX-2240] 病理诊断：\n[BBOX-2241] 病理诊断：\n[BBOX-2242] 病理诊断：\n[BBOX-2243] 病理诊断：\n[BBOX-2244] 病理诊断：\n[BBOX-2245] 病理诊断：\n[BBOX-2246] 病理诊断：\n[BBOX-2247] 病理诊断：\n[BBOX-2248] 病理诊断：\n[BBOX-2249] 病理诊断：\n[BBOX-2250] 病理诊断：\n[BBOX-2251] 病理诊断：\n[BBOX-2252] 病理诊断：\n[BBOX-2253] 病理诊断：\n[BBOX-2254] 病理诊断：\n[BBOX-2255] 病理诊断：\n[BBOX-2256] 病理诊断：\n[BBOX-2257] 病理诊断：\n[BBOX-2258] 病理诊断：\n[BBOX-2259] 病理诊断：\n[BBOX-2260] 病理诊断：\n[BBOX-2261] 病理诊断：\n[BBOX-2262] 病理诊断：\n[BBOX-2263] 病理诊断：\n[BBOX-2264] 病理诊断：\n[BBOX-2265] 病理诊断：\n[BBOX-2266] 病理诊断：\n[BBOX-2267] 病理诊断：\n[BBOX-2268] 病理诊断：\n[BBOX-2269] 病理诊断：\n[BBOX-2270] 病理诊断：\n[BBOX-2271] 病理诊断：\n[BBOX-2272] 病理诊断：\n[BBOX-2273] 病理诊断：\n[BBOX-2274] 病理诊断：\n[BBOX-2275] 病理诊断：\n[BBOX-2276] 病理诊断：\n[BBOX-2277] 病理诊断：\n[BBOX-2278] 病理诊断：\n[BBOX-2279] 病理诊断：\n[BBOX-2280] 病理诊断：\n[BBOX-2281] 病理诊断：\n[BBOX-2282] 病理诊断：\n[BBOX-2283] 病理诊断：\n[BBOX-2284] 病理诊断：\n[BBOX-2285] 病理诊断：\n[BBOX-2286] 病理诊断：\n[BBOX-2287] 病理诊断：\n[BBOX-2288] 病理诊断：\n[BBOX-2289] 病理诊断：\n[BBOX-2290] 病理诊断：\n[BBOX-2291] 病理诊断：\n[BBOX-2292] 病理诊断：\n[BBOX-2293] 病理诊断：\n[BBOX-2294] 病理诊断：\n[BBOX-2295] 病理诊断：\n[BBOX-2296] 病理诊断：\n[BBOX-2297] 病理诊断：\n[BBOX-2298] 病理诊断：\n[BBOX-2299] 病理诊断：\n[BBOX-2300] 病理诊断：\n[BBOX-2301] 病理诊断：\n[BBOX-2302] 病理诊断：\n[BBOX-2303] 病理诊断：\n[BBOX-2304] 病理诊断：\n[BBOX-2305] 病理诊断：\n[BBOX-2306] 病理诊断：\n[BBOX-2307] 病理诊断：\n[BBOX-2308] 病理诊断：\n[BBOX-2309] 病理诊断：\n[BBOX-2310] 病理诊断：\n[BBOX-2311] 病理诊断：\n[BBOX-2312] 病理诊断：\n[BBOX-2313] 病理诊断：\n[BBOX-2314] 病理诊断：\n[BBOX-2315] 病理诊断：\n[BBOX-2316] 病理诊断：\n[BBOX-2317] 病理诊断：\n[BBOX-2318] 病理诊断：\n[BBOX-2319] 病理诊断：\n[BBOX-2320] 病理诊断：\n[BBOX-2321] 病理诊断：\n[BBOX-2322] 病理诊断：\n[BBOX-2323] 病理诊断：\n[BBOX-2324] 病理诊断：\n[BBOX-2325] 病理诊断：\n[BBOX-2326] 病理诊断：\n[BBOX-2327] 病理诊断：\n[BBOX-2328] 病理诊断：\n[BBOX-2329] 病理诊断：\n[BBOX-2330] 病理诊断：\n[BBOX-2331] 病理诊断：\n[BBOX-2332] 病理诊断：\n[BBOX-2333] 病理诊断：\n[BBOX-2334] 病理诊断：\n[BBOX-2335] 病理诊断：\n[BBOX-2336] 病理诊断：\n[BBOX-2337] 病理诊断：\n[BBOX-2338] 病理诊断：\n[BBOX-2339] 病理诊断：\n[BBOX-2340] 病理诊断：\n[BBOX-2341] 病理诊断：\n[BBOX-2342] 病理诊断：\n[BBOX-2343] 病理诊断：\n[BBOX-2344] 病理诊断：\n[BBOX-2345] 病理诊断：\n[BBOX-2346] 病理诊断：\n[BBOX-2347] 病理诊断：\n[BBOX-2348] 病理诊断：\n[BBOX-2349] 病理诊断：\n[BBOX-2350] 病理诊断：\n[BBOX-2351] 病理诊断：\n[BBOX-2352] 病理诊断：\n[BBOX-2353] 病理诊断：\n[BBOX-2354] 病理诊断：\n[BBOX-2355] 病理诊断：\n[BBOX-2356] 病理诊断：\n[BBOX-2357] 病理诊断：\n[BBOX-2358] 病理诊断：\n[BBOX-2359] 病理诊断：\n[BBOX-2360] 病理诊断：\n[BBOX-2361] 病理诊断：\n[BBOX-2362] 病理诊断：\n[BBOX-2363] 病理诊断：\n[BBOX-2364] 病理诊断：\n[BBOX-2365] 病理诊断：\n[BBOX-2366] 病理诊断：\n[BBOX-2367] 病理诊断：\n[BBOX-2368] 病理诊断：\n[BBOX-2369] 病理诊断：\n[BBOX-2370] 病理诊断：\n[BBOX-2371] 病理诊断：\n[BBOX-2372] 病理诊断：\n[BBOX-2373] 病理诊断：\n[BBOX-2374] 病理诊断：\n[BBOX-2375] 病理诊断：\n[BBOX-2376] 病理诊断：\n[BBOX-2377] 病理诊断：\n[BBOX-2378] 病理诊断：\n[BBOX-2379] 病理诊断：\n[BBOX-2380] 病理诊断：\n[BBOX-2381] 病理诊断：\n[BBOX-2382] 病理诊断：\n[BBOX-2383] 病理诊断：\n[BBOX-2384] 病理诊断：\n[BBOX-2385] 病理诊断：\n[BBOX-2386] 病理诊断：\n[BBOX-2387] 病理诊断：\n[BBOX-2388] 病理诊断：\n[BBOX-2389] 病理诊断：\n[BBOX-2390] 病理诊断：\n[BBOX-2391] 病理诊断：\n[BBOX-2392] 病理诊断：\n[BBOX-2393] 病理诊断：\n[BBOX-2394] 病理诊断：\n[BBOX-2395] 病理诊断：\n[BBOX-2396] 病理诊断：\n[BBOX-2397] 病理诊断：\n[BBOX-2398] 病理诊断：\n[BBOX-2399] 病理诊断：\n[BBOX-2400] 病理诊断：\n[BBOX-2401] 病理诊断：\n[BBOX-2402] 病理诊断：\n[BBOX-2403] 病理诊断：\n[BBOX-2404] 病理诊断：\n[BBOX-2405] 病理诊断：\n[BBOX-2406] 病理诊断：\n[BBOX-2407] 病理诊断：\n[BBOX-2408] 病理诊断：\n[BBOX-2409] 病理诊断：\n[BBOX-2410] 病理诊断：\n[BBOX-2411] 病理诊断：\n[BBOX-2412] 病理诊断：\n[BBOX-2413] 病理诊断：\n[BBOX-2414] 病理诊断：\n[BBOX-2415] 病理诊断：\n[BBOX-2416] 病理诊断：\n[BBOX-2417] 病理诊断：\n[BBOX-2418] 病理诊断：\n[BBOX-2419] 病理诊断：\n[BBOX-2420] 病理诊断：\n[BBOX-2421] 病理诊断：\n[BBOX-2422] 病理诊断：\n[BBOX-2423] 病理诊断：\n[BBOX-2424] 病理诊断：\n[BBOX-2425] 病理诊断：\n[BBOX-2426] 病理诊断：\n[BBOX-2427] 病理诊断：\n[BBOX-2428] 病理诊断：\n[BBOX-2429] 病理诊断：\n[BBOX-2430] 病理诊断：\n[BBOX-2431] 病理诊断：\n[BBOX-2432] 病理诊断：\n[BBOX-2433] 病理诊断：\n[BBOX-2434] 病理诊断：\n[BBOX-2435] 病理诊断：\n[BBOX-2436] 病理诊断：\n[BBOX-2437] 病理诊断：\n[BBOX-2438] 病理诊断：\n[BBOX-2439] 病理诊断：\n[BBOX-2440] 病理诊断：\n[BBOX-2441] 病理诊断：\n[BBOX-2442] 病理诊断：\n[BBOX-2443] 病理诊断：\n[BBOX-2444] 病理诊断：\n[BBOX-2445] 病理诊断：\n[BBOX-2446] 病理诊断：\n[BBOX-2447] 病理诊断：\n[BBOX-2448] 病理诊断：\n[BBOX-2449] 病理诊断：\n[BBOX-2450] 病理诊断：\n[BBOX-2451] 病理诊断：\n[BBOX-2452] 病理诊断：\n[BBOX-2453] 病理诊断：\n[BBOX-2454] 病理诊断：\n[BBOX-2455] 病理诊断：\n[BBOX-2456] 病理诊断：\n[BBOX-2457] 病理诊断：\n[BBOX-2458] 病理诊断：\n[BBOX-2459] 病理诊断：\n[BBOX-2460] 病理诊断：\n[BBOX-2461] 病理诊断：\n[BBOX-2462] 病理诊断：\n[BBOX-2463] 病理诊断：\n[BBOX-2464] 病理诊断：\n[BBOX-2465] 病理诊断：\n[BBOX-2466] 病理诊断：\n[BBOX-2467] 病理诊断：\n[BBOX-2468] 病理诊断：\n[BBOX-2469] 病理诊断：\n[BBOX-2470] 病理诊断：\n[BBOX-2471] 病理诊断：\n[BBOX-2472] 病理诊断：\n[BBOX-2473] 病理诊断：\n[BBOX-2474] 病理诊断：\n[BBOX-2475] 病理诊断：\n[BBOX-2476] 病理诊断：\n[BBOX-2477] 病理诊断：\n[BBOX-2478] 病理诊断：\n[BBOX-2479] 病理诊断：\n[BBOX-2480] 病理诊断：\n[BBOX-2481] 病理诊断：\n[BBOX-2482] 病理诊断：\n[BBOX-2483] 病理诊断：\n[BBOX-2484] 病理诊断：\n[BBOX-2485] 病理诊断：\n[BBOX-2486] 病理诊断：\n[BBOX-2487] 病理诊断：\n[BBOX-2488] 病理诊断：\n[BBOX-2489] 病理诊断：\n[BBOX-2490] 病理诊断：\n[BBOX-2491] 病理诊断：\n[BBOX-2492] 病理诊断：\n[BBOX-2493] 病理诊断：\n[BBOX-2494] 病理诊断：\n[BBOX-2495] 病理诊断：\n[BBOX-2496] 病理诊断：\n[BBOX-2497] 病理诊断：\n[BBOX-2498] 病理诊断：\n[BBOX-2499] 病理诊断：\n[BBOX-2500] 病理诊断：\n[BBOX-2501] 病理诊断：\n[BBOX-2502] 病理诊断：\n[BBOX-2503] 病理诊断：\n[BBOX-2504] 病理诊断：\n[BBOX-2505] 病理诊断：\n[BBOX-2506] 病理诊断：\n[BBOX-2507] 病理诊断：\n[BBOX-2508] 病理诊断：\n[BBOX-2509] 病理诊断：\n[BBOX-2510] 病理诊断：\n[BBOX-2511] 病理诊断：\n[BBOX-2512] 病理诊断：\n[BBOX-2513] 病理诊断：\n[BBOX-2514] 病理诊断：\n[BBOX-2515] 病理诊断：\n[BBOX-2516] 病理诊断：\n[BBOX-2517] 病理诊断：\n[BBOX-2518] 病理诊断：\n[BBOX-2519] 病理诊断：\n[BBOX-2520] 病理诊断：\n[BBOX-2521] 病理诊断：\n[BBOX-2522] 病理诊断：\n[BBOX-2523] 病理诊断：\n[BBOX-2524] 病理诊断：\n[BBOX-2525] 病理诊断：\n[BBOX-2526] 病理诊断：\n[BBOX-2527] 病理诊断：\n[BBOX-2528] 病理诊断：\n[BBOX-2529] 病理诊断：\n[BBOX-2530] 病理诊断：\n[BBOX-2531] 病理诊断：\n[BBOX-2532] 病理诊断：\n[BBOX-2533] 病理诊断：\n[BBOX-2534] 病理诊断：\n[BBOX-2535] 病理诊断：\n[BBOX-2536] 病理诊断：\n[BBOX-2537] 病理诊断：\n[BBOX-2538] 病理诊断：\n[BBOX-2539] 病理诊断：\n[BBOX-2540] 病理诊断：\n[BBOX-2541] 病理诊断：\n[BBOX-2542] 病理诊断：\n[BBOX-2543] 病理诊断：\n[BBOX-2544] 病理诊断：\n[BBOX-2545] 病理诊断：\n[BBOX-2546] 病理诊断：\n[BBOX-2547] 病理诊断：\n[BBOX-2548] 病理诊断：\n[BBOX-2549] 病理诊断：\n[BBOX-2550] 病理诊断：\n[BBOX-2551] 病理诊断：\n[BBOX-2552] 病理诊断：\n[BBOX-2553] 病理诊断：\n[BBOX-2554] 病理诊断：\n[BBOX-2555] 病理诊断：\n[BBOX-2556] 病理诊断：\n[BBOX-2557] 病理诊断：\n[BBOX-2558] 病理诊断：\n[BBOX-2559] 病理诊断：\n[BBOX-2560] 病理诊断：\n[BBOX-2561] 病理诊断：\n[BBOX-2562] 病理诊断：\n[BBOX-2563] 病理诊断：\n[BBOX-2564] 病理诊断：\n[BBOX-2565] 病理诊断：\n[BBOX-2566] 病理诊断：\n[BBOX-2567] 病理诊断：\n[BBOX-2568] 病理诊断：\n[BBOX-2569] 病理诊断：\n[BBOX-2570] 病理诊断：\n[BBOX-2571] 病理诊断：\n[BBOX-2572] 病理诊断：\n[BBOX-2573] 病理诊断：\n[BBOX-2574] 病理诊断：\n[BBOX-2575] 病理诊断：\n[BBOX-2576] 病理诊断：\n[BBOX-2577] 病理诊断：\n[BBOX-2578] 病理诊断：\n[BBOX-2579] 病理诊断：\n[BBOX-2580] 病理诊断：\n[BBOX-2581] 病理诊断：\n[BBOX-2582] 病理诊断：\n[BBOX-2583] 病理诊断：\n[BBOX-2584] 病理诊断：\n[BBOX-2585] 病理诊断：\n[BBOX-2586] 病理诊断：\n[BBOX-2587] 病理诊断：\n[BBOX-2588] 病理诊断：\n[BBOX-2589] 病理诊断：\n[BBOX-2590] 病理诊断：\n[BBOX-2591] 病理诊断：\n[BBOX-2592] 病理诊断：\n[BBOX-2593] 病理诊断：\n[BBOX-2594] 病理诊断：\n[BBOX-2595] 病理诊断：\n[BBOX-2596] 病理诊断：\n[BBOX-2597] 病理诊断：\n[BBOX-2598] 病理诊断：\n[BBOX-2599] 病理诊断：\n[BBOX-2600] 病理诊断：\n[BBOX-2601] 病理诊断：\n[BBOX-2602] 病理诊断：\n[BBOX-2603] 病理诊断：\n[BBOX-2604] 病理诊断：\n[BBOX-2605] 病理诊断：\n[BBOX-2606] 病理诊断：\n[BBOX-2607] 病理诊断：\n[BBOX-2608] 病理诊断：\n[BBOX-2609] 病理诊断：\n[BBOX-2610] 病理诊断：\n[BBOX-2611] 病理诊断：\n[BBOX-2612] 病理诊断：\n[BBOX-2613] 病理诊断：\n[BBOX-2614] 病理诊断：\n[BBOX-2615] 病理诊断：\n[BBOX-2616] 病理诊断：\n[BBOX-2617] 病理诊断：\n[BBOX-2618] 病理诊断：\n[BBOX-2619] 病理诊断：\n[BBOX-2620] 病理诊断：\n[BBOX-2621] 病理诊断：\n[BBOX-2622] 病理诊断：\n[BBOX-2623] 病理诊断：\n[BBOX-2624] 病理诊断：\n[BBOX-2625] 病理诊断：\n[BBOX-2626] 病理诊断：\n[BBOX-2627] 病理诊断：\n[BBOX-2628] 病理诊断：\n[BBOX-2629] 病理诊断：\n[BBOX-2630] 病理诊断：\n[BBOX-2631] 病理诊断：\n[BBOX-2632] 病理诊断：\n[BBOX-2633] 病理诊断：\n[BBOX-2634] 病理诊断：\n[BBOX-2635] 病理诊断：\n[BBOX-2636] 病理诊断：\n[BBOX-2637] 病理诊断：\n[BBOX-2638] 病理诊断：\n[BBOX-2639] 病理诊断：\n[BBOX-2640] 病理诊断：\n[BBOX-2641] 病理诊断：\n[BBOX-2642] 病理诊断：\n[BBOX-2643] 病理诊断：\n[BBOX-2644] 病理诊断：\n[BBOX-2645] 病理诊断：\n[BBOX-2646] 病理诊断：\n[BBOX-2647] 病理诊断：\n[BBOX-2648] 病理诊断：\n[BBOX-2649] 病理诊断：\n[BBOX-2650] 病理诊断：\n[BBOX-2651] 病理诊断：\n[BBOX-2652] 病理诊断：\n[BBOX-2653] 病理诊断：\n[BBOX-2654] 病理诊断：\n[BBOX-2655] 病理诊断：\n[BBOX-2656] 病理诊断：\n[BBOX-2657] 病理诊断：\n[BBOX-2658] 病理诊断：\n[BBOX-2659] 病理诊断：\n[BBOX-2660] 病理诊断：\n[BBOX-2661] 病理诊断：\n[BBOX-2662] 病理诊断：\n[BBOX-2663] 病理诊断：\n[BBOX-2664] 病理诊断：\n[BBOX-2665] 病理诊断：\n[BBOX-2666] 病理诊断：\n[BBOX-2667] 病理诊断：\n[BBOX-2668] 病理诊断：\n[BBOX-2669] 病理诊断：\n[BBOX-2670] 病理诊断：\n[BBOX-2671] 病理诊断：\n[BBOX-2672] 病理诊断：\n[BBOX-2673] 病理诊断：\n[BBOX-2674] 病理诊断：\n[BBOX-2675] 病理诊断：\n[BBOX-2676] 病理诊断：\n[BBOX-2677] 病理诊断：\n[BBOX-2678] 病理诊断：\n[BBOX-2679] 病理诊断：\n[BBOX-2680] 病理诊断：\n[BBOX-2681] 病理诊断：\n[BBOX-2682] 病理诊断：\n[BBOX-2683] 病理诊断：\n[BBOX-2684] 病理诊断：\n[BBOX-2685] 病理诊断：\n[BBOX-2686] 病理诊断：\n[BBOX-2687] 病理诊断：\n[BBOX-2688] 病理诊断：\n[BBOX-2689] 病理诊断：\n[BBOX-2690] 病理诊断：\n[BBOX-2691] 病理诊断：\n[BBOX-2692] 病理诊断：\n[BBOX-2693] 病理诊断：\n[BBOX-2694] 病理诊断：\n[BBOX-2695] 病理诊断：\n[BBOX-2696] 病理诊断：\n[BBOX-2697] 病理诊断：\n[BBOX-2698] 病理诊断：\n[BBOX-2699] 病理诊断：\n[BBOX-2700] 病理诊断：\n[BBOX-2701] 病理诊断：\n[BBOX-2702] 病理诊断：\n[BBOX-2703] 病理诊断：\n[BBOX-2704] 病理诊断：\n[BBOX-2705] 病理诊断：\n[BBOX-2706] 病理诊断：\n[BBOX-2707] 病理诊断：\n[BBOX-2708] 病理诊断：\n[BBOX-2709] 病理诊断：\n[BBOX-2710] 病理诊断：\n[BBOX-2711] 病理诊断：\n[BBOX-2712] 病理诊断：\n[BBOX-2713] 病理诊断：\n[BBOX-2714] 病理诊断：\n[BBOX-2715] 病理诊断：\n[BBOX-2716] 病理诊断：\n[BBOX-2717] 病理诊断：\n[BBOX-2718] 病理诊断：\n[BBOX-2719] 病理诊断：\n[BBOX-2720] 病理诊断：\n[BBOX-2721] 病理诊断：\n[BBOX-2722] 病理诊断：\n[BBOX-2723] 病理诊断：\n[BBOX-2724] 病理诊断：\n[BBOX-2725] 病理诊断：\n[BBOX-2726] 病理诊断：\n[BBOX-2727] 病理诊断：\n[BBOX-2728] 病理诊断：\n[BBOX-2729] 病理诊断：\n[BBOX-2730] 病理诊断：\n[BBOX-2731] 病理诊断：\n[BBOX-2732] 病理诊断：\n[BBOX-2733] 病理诊断：\n[BBOX-2734] 病理诊断：\n[BBOX-2735] 病理诊断：\n[BBOX-2736] 病理诊断：\n[BBOX-2737] 病理诊断：\n[BBOX-2738] 病理诊断：\n[BBOX-2739] 病理诊断：\n[BBOX-2740] 病理诊断：\n[BBOX-2741] 病理诊断：\n[BBOX-2742] 病理诊断：\n[BBOX-2743] 病理诊断：\n[BBOX-2744] 病理诊断：\n[BBOX-2745] 病理诊断：\n[BBOX-2746] 病理诊断：\n[BBOX-2747] 病理诊断：\n[BBOX-2748] 病理诊断：\n[BBOX-2749] 病理诊断：\n[BBOX-2750] 病理诊断：\n[BBOX-2751] 病理诊断：\n[BBOX-2752] 病理诊断：\n[BBOX-2753] 病理诊断：\n[BBOX-2754] 病理诊断：\n[BBOX-2755] 病理诊断：\n[BBOX-2756] 病理诊断：\n[BBOX-2757] 病理诊断：\n[BBOX-2758] 病理诊断：\n[BBOX-2759] 病理诊断：\n[BBOX-2760] 病理诊断：\n[BBOX-2761] 病理诊断：\n[BBOX-2762] 病理诊断：\n[BBOX-2763] 病理诊断：\n[BBOX-2764] 病理诊断：\n[BBOX-2765] 病理诊断：\n[BBOX-2766] 病理诊断：\n[BBOX-2767] 病理诊断：\n[BBOX-2768] 病理诊断：\n[BBOX-2769] 病理诊断：\n[BBOX-2770] 病理诊断：\n[BBOX-2771] 病理诊断：\n[BBOX-2772] 病理诊断：\n[BBOX-2773] 病理诊断：\n[BBOX-2774] 病理诊断：\n[BBOX-2775] 病理诊断：\n[BBOX-2776] 病理诊断：\n[BBOX-2777] 病理诊断：\n[BBOX-2778] 病理诊断：\n[BBOX-2779] 病理诊断：\n[BBOX-2780] 病理诊断：\n[BBOX-2781] 病理诊断：\n[BBOX-2782] 病理诊断：\n[BBOX-2783] 病理诊断：\n[BBOX-2784] 病理诊断：\n[BBOX-2785] 病理诊断：\n[BBOX-2786] 病理诊断：\n[BBOX-2787] 病理诊断：\n[BBOX-2788] 病理诊断：\n[BBOX-2789] 病理诊断：\n[BBOX-2790] 病理诊断：\n[BBOX-2791] 病理诊断：\n[BBOX-2792] 病理诊断：\n[BBOX-2793] 病理诊断：\n[BBOX-2794] 病理诊断：\n[BBOX-2795] 病理诊断：\n[BBOX-2796] 病理诊断：\n[BBOX-2797] 病理诊断：\n[BBOX-2798] 病理诊断：\n[BBOX-2799] 病理诊断：\n[BBOX-2800] 病理诊断：\n[BBOX-2801] 病理诊断：\n[BBOX-2802] 病理诊断：\n[BBOX-2803] 病理诊断：\n[BBOX-2804] 病理诊断：\n[BBOX-2805] 病理诊断：\n[BBOX-2806] 病理诊断：\n[BBOX-2807] 病理诊断：\n[BBOX-2808] 病理诊断：\n[BBOX-2809] 病理诊断：\n[BBOX-2810] 病理诊断：\n[BBOX-2811] 病理诊断：\n[BBOX-2812] 病理诊断：\n[BBOX-2813] 病理诊断：\n[BBOX-2814] 病理诊断：\n[BBOX-2815] 病理诊断：\n[BBOX-2816] 病理诊断：\n[BBOX-2817] 病理诊断：\n[BBOX-2818] 病理诊断：\n[BBOX-2819] 病理诊断：\n[BBOX-2820] 病理诊断：\n[BBOX-2821] 病理诊断：\n[BBOX-2822] 病理诊断：\n[BBOX-2823] 病理诊断：\n[BBOX-2824] 病理诊断：\n[BBOX-2825] 病理诊断：\n[BBOX-2826] 病理诊断：\n[BBOX-2827] 病理诊断：\n[BBOX-2828] 病理诊断：\n[BBOX-2829] 病理诊断：\n[BBOX-2830] 病理诊断：\n[BBOX-2831] 病理诊断：\n[BBOX-2832] 病理诊断：\n[BBOX-2833] 病理诊断：\n[BBOX-2834] 病理诊断：\n[BBOX-2835] 病理诊断：\n[BBOX-2836] 病理诊断：\n[BBOX-2837] 病理诊断：\n[BBOX-2838] 病理诊断：\n[BBOX-2839] 病理诊断：\n[BBOX-2840] 病理诊断：\n[BBOX-2841] 病理诊断：\n[BBOX-2842] 病理诊断：\n[BBOX-2843] 病理诊断：\n[BBOX-2844] 病理诊断：\n[BBOX-2845] 病理诊断：\n[BBOX-2846] 病理诊断：\n[BBOX-2847] 病理诊断：\n[BBOX-2848] 病理诊断：\n[BBOX-2849] 病理诊断：\n[BBOX-2850] 病理诊断：\n[BBOX-2851] 病理诊断：\n[BBOX-2852] 病理诊断：\n[BBOX-2853] 病理诊断：\n[BBOX-2854] 病理诊断：\n[BBOX-2855] 病理诊断：\n[BBOX-2856] 病理诊断：\n[BBOX-2857] 病理诊断：\n[BBOX-2858] 病理诊断：\n[BBOX-2859] 病理诊断：\n[BBOX-2860] 病理诊断：\n[BBOX-2861] 病理诊断：\n[BBOX-2862] 病理诊断：\n[BBOX-2863] 病理诊断：\n[BBOX-2864] 病理诊断：\n[BBOX-2865] 病理诊断：\n[BBOX-2866] 病理诊断：\n[BBOX-2867] 病理诊断：\n[BBOX-2868] 病理诊断：\n[BBOX-2869] 病理诊断：\n[BBOX-2870] 病理诊断：\n[BBOX-2871] 病理诊断：\n[BBOX-2872] 病理诊断：\n[BBOX-2873] 病理诊断：\n[BBOX-2874] 病理诊断：\n[BBOX-2875] 病理诊断：\n[BBOX-2876] 病理诊断：\n[BBOX-2877] 病理诊断：\n[BBOX-2878] 病理诊断：\n[BBOX-2879] 病理诊断：\n[BBOX-2880] 病理诊断：\n[BBOX-2881] 病理诊断：\n[BBOX-2882] 病理诊断：\n[BBOX-2883] 病理诊断：\n[BBOX-2884] 病理诊断：\n[BBOX-2885] 病理诊断：\n[BBOX-2886] 病理诊断：\n[BBOX-2887] 病理诊断：\n[BBOX-2888] 病理诊断：\n[BBOX-2889] 病理诊断：\n[BBOX-2890] 病理诊断：\n[BBOX-2891] 病理诊断：\n[BBOX-2892] 病理诊断：\n[BBOX-2893] 病理诊断：\n[BBOX-2894] 病理诊断：\n[BBOX-2895] 病理诊断：\n[BBOX-2896] 病理诊断：\n[BBOX-2897] 病理诊断：\n[BBOX-2898] 病理诊断：\n[BBOX-2899] 病理诊断：\n[BBOX-2900] 病理诊断：\n[BBOX-2901] 病理诊断：\n[BBOX-2902] 病理诊断：\n[BBOX-2903] 病理诊断：\n[BBOX-2904] 病理诊断：\n[BBOX-2905] 病理诊断：\n[BBOX-2906] 病理诊断：\n[BBOX-2907] 病理诊断：\n[BBOX-2908] 病理诊断：\n[BBOX-2909] 病理诊断：\n[BBOX-2910] 病理诊断：\n[BBOX-2911] 病理诊断：\n[BBOX-2912] 病理诊断：\n[BBOX-2913] 病理诊断：\n[BBOX-2914] 病理诊断：\n[BBOX-2915] 病理诊断：\n[BBOX-2916] 病理诊断：\n[BBOX-2917] 病理诊断：\n[BBOX-2918] 病理诊断：\n[BBOX-2919] 病理诊断：\n[BBOX-2920] 病理诊断：\n[BBOX-2921] 病理诊断：\n[BBOX-2922] 病理诊断：\n[BBOX-2923] 病理诊断：\n[BBOX-2924] 病理诊断：\n[BBOX-2925] 病理诊断：\n[BBOX-2926] 病理诊断：\n[BBOX-2927] 病理诊断：\n[BBOX-2928] 病理诊断：\n[BBOX-2929] 病理诊断：\n[BBOX-2930] 病理诊断：\n[BBOX-2931] 病理诊断：\n[BBOX-2932] 病理诊断：\n[BBOX-2933] 病理诊断：\n[BBOX-2934] 病理诊断：\n[BBOX-2935] 病理诊断：\n[BBOX-2936] 病理诊断：\n[BBOX-2937] 病理诊断：\n[BBOX-2938] 病理诊断：\n[BBOX-2939] 病理诊断：\n[BBOX-2940] 病理诊断：\n[BBOX-2941] 病理诊断：\n[BBOX-2942] 病理诊断：\n[BBOX-2943] 病理诊断：\n[BBOX-2944] 病理诊断：\n[BBOX-2945] 病理诊断：\n[BBOX-2946] 病理诊断：\n[BBOX-2947] 病理诊断：\n[BBOX-2948] 病理诊断：\n[BBOX-2949] 病理诊断：\n[BBOX-2950] 病理诊断：\n[BBOX-2951] 病理诊断：\n[BBOX-2952] 病理诊断：\n[BBOX-2953] 病理诊断：\n[BBOX-2954] 病理诊断：\n[BBOX-2955] 病理诊断：\n[BBOX-2956] 病理诊断：\n[BBOX-2957] 病理诊断：\n[BBOX-2958] 病理诊断：\n[BBOX-2959] 病理诊断：\n[BBOX-2960] 病理诊断：\n[BBOX-2961] 病理诊断：\n[BBOX-2962] 病理诊断：\n[BBOX-2963] 病理诊断：\n[BBOX-2964] 病理诊断：\n[BBOX-2965] 病理诊断：\n[BBOX-2966] 病理诊断：\n[BBOX-2967] 病理诊断：\n[BBOX-2968] 病理诊断：\n[BBOX-2969] 病理诊断：\n[BBOX-2970] 病理诊断：\n[BBOX-2971] 病理诊断：\n[BBOX-2972] 病理诊断：\n[BBOX-2973] 病理诊断：\n[BBOX-2974] 病理诊断：\n[BBOX-2975] 病理诊断：\n[BBOX-2976] 病理诊断：\n[BBOX-2977] 病理诊断：\n[BBOX-2978] 病理诊断：\n[BBOX-2979] 病理诊断：\n[BBOX-2980] 病理诊断：\n[BBOX-2981] 病理诊断：\n[BBOX-2982] 病理诊断：\n[BBOX-2983] 病理诊断：\n[BBOX-2984] 病理诊断：\n[BBOX-2985] 病理诊断：\n[BBOX-2986] 病理诊断：\n[BBOX-2987] 病理诊断：\n[BBOX-2988] 病理诊断：\n[BBOX-2989] 病理诊断：\n[BBOX-2990] 病理诊断：\n[BBOX-2991] 病理诊断：\n[BBOX-2992] 病理诊断：\n[BBOX-2993] 病理诊断：\n[BBOX-2994] 病理诊断：\n[BBOX-2995] 病理诊断：\n[BBOX-2996] 病理诊断：\n[BBOX-2997] 病理诊断：\n[BBOX-2998] 病理诊断：\n[BBOX-2999] 病理诊断：\n[BBOX-3000] 病理诊断：\n[BBOX-3001] 病理诊断：\n[BBOX-3002] 病理诊断：\n[BBOX-3003] 病理诊断：\n[BBOX-3004] 病理诊断：\n[BBOX-3005] 病理诊断：\n[BBOX-3006] 病理诊断：\n[BBOX-3007] 病理诊断：\n[BBOX-3008] 病理诊断：\n[BBOX-3009] 病理诊断：\n[BBOX-3010] 病理诊断：\n[BBOX-3011] 病理诊断：\n[BBOX-3012] 病理诊断：\n[BBOX-3013] 病理诊断：\n[BBOX-3014] 病理诊断：\n[BBOX-3015] 病理诊断：\n[BBOX-3016] 病理诊断：\n[BBOX-3017] 病理诊断：\n[BBOX-3018] 病理诊断：\n[BBOX-3019] 病理诊断：\n[BBOX-3020] 病理诊断：\n[BBOX-3021] 病理诊断：\n[BBOX-3022] 病理诊断：\n[BBOX-3023] 病理诊断：\n[BBOX-3024] 病理诊断：\n[BBOX-3025] 病理诊断：\n[BBOX-3026] 病理诊断：\n[BBOX-3027] 病理诊断：\n[BBOX-3028] 病理诊断：\n[BBOX-3029] 病理诊断：\n[BBOX-3030] 病理诊断：\n[BBOX-3031] 病理诊断：\n[BBOX-3032] 病理诊断：\n[BBOX-3033] 病理诊断：\n[BBOX-3034] 病理诊断：\n[BBOX-3035] 病理诊断：\n[BBOX-3036] 病理诊断：\n[BBOX-3037] 病理诊断：\n[BBOX-3038] 病理诊断：\n[BBOX-3039] 病理诊断：\n[BBOX-3040] 病理诊断：\n[BBOX-3041] 病理诊断：\n[BBOX-3042] 病理诊断：\n[BBOX-3043] 病理诊断：\n[BBOX-3044] 病理诊断：\n[BBOX-3045] 病理诊断：\n[BBOX-3046] 病理诊断：\n[BBOX-3047] 病理诊断：\n[BBOX-3048] 病理诊断：\n[BBOX-3049] 病理诊断：\n[BBOX-3050] 病理诊断：\n[BBOX-3051] 病理诊断：\n[BBOX-3052] 病理诊断：\n[BBOX-3053] 病理诊断：\n[BBOX-3054] 病理诊断：\n[BBOX-3055] 病理诊断：\n[BBOX-3056] 病理诊断：\n[BBOX-3057] 病理诊断：\n[BBOX-3058] 病理诊断：\n[BBOX-3059] 病理诊断：\n[BBOX-3060] 病理诊断：\n[BBOX-3061] 病理诊断：\n[BBOX-3062] 病理诊断：\n[BBOX-3063] 病理诊断：\n[BBOX-3064] 病理诊断：\n[BBOX-3065] 病理诊断：\n[BBOX-3066] 病理诊断：\n[BBOX-3067] 病理诊断：\n[BBOX-3068] 病理诊断：\n[BBOX-3069] 病理诊断：\n[BBOX-3070] 病理诊断：\n[BBOX-3071] 病理诊断：\n[BBOX-3072] 病理诊断：\n[BBOX-3073] 病理诊断：\n[BBOX-3074] 病理诊断：\n[BBOX-3075] 病理诊断：\n[BBOX-3076] 病理诊断：\n[BBOX-3077] 病理诊断：\n[BBOX-3078] 病理诊断：\n[BBOX-3079] 病理诊断：\n[BBOX-3080] 病理诊断：\n[BBOX-3081] 病理诊断：\n[BBOX-3082] 病理诊断：\n[BBOX-3083] 病理诊断：\n[BBOX-3084] 病理诊断：\n[BBOX-3085] 病理诊断：\n[BBOX-3086] 病理诊断：\n[BBOX-3087] 病理诊断：\n[BBOX-3088] 病理诊断：\n[BBOX-3089] 病理诊断：\n[BBOX-3090] 病理诊断：\n[BBOX-3091] 病理诊断：\n[BBOX-3092] 病理诊断：\n[BBOX-3093] 病理诊断：\n[BBOX-3094] 病理诊断：\n[BBOX-3095] 病理诊断：\n[BBOX-3096] 病理诊断：\n[BBOX-3097] 病理诊断：\n[BBOX-3098] 病理诊断：\n[BBOX-3099] 病理诊断：\n[BBOX-3100] 病理诊断：\n[BBOX-3101] 病理诊断：\n[BBOX-3102] 病理诊断：\n[BBOX-3103] 病理诊断：\n[BBOX-3104] 病理诊断：\n[BBOX-3105] 病理诊断：\n[BBOX-3106] 病理诊断：\n[BBOX-3107] 病理诊断：\n[BBOX-3108] 病理诊断：\n[BBOX-3109] 病理诊断：\n[BBOX-3110] 病理诊断：\n[BBOX-3111] 病理诊断：\n[BBOX-3112] 病理诊断：\n[BBOX-3113] 病理诊断：\n[BBOX-3114] 病理诊断：\n[BBOX-3115] 病理诊断：\n[BBOX-3116] 病理诊断：\n[BBOX-3117] 病理诊断：\n[BBOX-3118] 病理诊断：\n[BBOX-3119] 病理诊断：\n[BBOX-3120] 病理诊断：\n[BBOX-3121] 病理诊断：\n[BBOX-3122] 病理诊断：\n[BBOX-3123] 病理诊断：\n[BBOX-3124] 病理诊断：\n[BBOX-3125] 病理诊断：\n[BBOX-3126] 病理诊断：\n[BBOX-3127] 病理诊断：\n[BBOX-3128] 病理诊断：\n[BBOX-3129] 病理诊断：\n[BBOX-3130] 病理诊断：\n[BBOX-3131] 病理诊断：\n[BBOX-3132] 病理诊断：\n[BBOX-3133] 病理诊断：\n[BBOX-3134] 病理诊断：\n[BBOX-3135] 病理诊断：\n[BBOX-3136] 病理诊断：\n[BBOX-3137] 病理诊断：\n[BBOX-3138] 病理诊断：\n[BBOX-3139] 病理诊断：\n[BBOX-3140] 病理诊断：\n[BBOX-3141] 病理诊断：\n[BBOX-3142] 病理诊断：\n[BBOX-3143] 病理诊断：\n[BBOX-3144] 病理诊断：\n[BBOX-3145] 病理诊断：\n[BBOX-3146] 病理诊断：\n[BBOX-3147] 病理诊断：\n[BBOX-3148] 病理诊断：\n[BBOX-3149] 病理诊断：\n[BBOX-3150] 病理诊断：\n[BBOX-3151] 病理诊断：\n[BBOX-3152] 病理诊断：\n[BBOX-3153] 病理诊断：\n[BBOX-3154] 病理诊断：\n[BBOX-3155] 病理诊断：\n[BBOX-3156] 病理诊断：\n[BBOX-3157] 病理诊断：\n[BBOX-3158] 病理诊断：\n[BBOX-3159] 病理诊断：\n[BBOX-3160] 病理诊断：\n[BBOX-3161] 病理诊断：\n[BBOX-3162] 病理诊断：\n[BBOX-3163] 病理诊断：\n[BBOX-3164] 病理诊断：\n[BBOX-3165] 病理诊断：\n[BBOX-3166] 病理诊断：\n[BBOX-3167] 病理诊断：\n[BBOX-3168] 病理诊断：\n[BBOX-3169] 病理诊断：\n[BBOX-3170] 病理诊断：\n[BBOX-3171] 病理诊断：\n[BBOX-3172] 病理诊断：\n[BBOX-3173] 病理诊断：\n[BBOX-3174] 病理诊断：\n[BBOX-3175] 病理诊断：\n[BBOX-3176] 病理诊断：\n[BBOX-3177] 病理诊断：\n[BBOX-3178] 病理诊断：\n[BBOX-3179] 病理诊断：\n[BBOX-3180] 病理诊断：\n[BBOX-3181] 病理诊断：\n[BBOX-3182] 病理诊断：\n[BBOX-3183] 病理诊断：\n[BBOX-3184] 病理诊断：\n[BBOX-3185] 病理诊断：\n[BBOX-3186] 病理诊断：\n[BBOX-3187] 病理诊断：\n[BBOX-3188] 病理诊断：\n[BBOX-3189] 病理诊断：\n[BBOX-3190] 病理诊断：\n[BBOX-3191] 病理诊断：\n[BBOX-3192] 病理诊断：\n[BBOX-3193] 病理诊断：\n[BBOX-3194] 病理诊断：\n[BBOX-3195] 病理诊断：\n[BBOX-3196] 病理诊断：\n[BBOX-3197] 病理诊断：\n[BBOX-3198] 病理诊断：\n[BBOX-3199] 病理诊断：\n[BBOX-3200] 病理诊断：\n[BBOX-3201] 病理诊断：\n[BBOX-3202] 病理诊断：\n[BBOX-3203] 病理诊断：\n[BBOX-3204] 病理诊断：\n[BBOX-3205] 病理诊断：\n[BBOX-3206] 病理诊断：\n[BBOX-3207] 病理诊断：\n[BBOX-3208] 病理诊断：\n[BBOX-3209] 病理诊断：\n[BBOX-3210] 病理诊断：\n[BBOX-3211] 病理诊断：\n[BBOX-3212] 病理诊断：\n[BBOX-3213] 病理诊断：\n[BBOX-3214] 病理诊断：\n[BBOX-3215] 病理诊断：\n[BBOX-3216] 病理诊断：\n[BBOX-3217] 病理诊断：\n[BBOX-3218] 病理诊断：\n[BBOX-3219] 病理诊断：\n[BBOX-3220] 病理诊断：\n[BBOX-3221] 病理诊断：\n[BBOX-3222] 病理诊断：\n[BBOX-3223] 病理诊断：\n[BBOX-3224] 病理诊断：\n[BBOX-3225] 病理诊断：\n[BBOX-3226] 病理诊断：\n[BBOX-3227] 病理诊断：\n[BBOX-3228] 病理诊断：\n[BBOX-3229] 病理诊断：\n[BBOX-3230] 病理诊断：\n[BBOX-3231] 病理诊断：\n[BBOX-3232] 病理诊断：\n[BBOX-3233] 病理诊断：\n[BBOX-3234] 病理诊断：\n[BBOX-3235] 病理诊断：\n[BBOX-3236] 病理诊断：\n[BBOX-3237] 病理诊断：\n[BBOX-3238] 病理诊断：\n[BBOX-3239] 病理诊断：\n[BBOX-3240] 病理诊断：\n[BBOX-3241] 病理诊断：\n[BBOX-3242] 病理诊断：\n[BBOX-3243] 病理诊断：\n[BBOX-3244] 病理诊断：\n[BBOX-3245] 病理诊断：\n[BBOX-3246] 病理诊断：\n[BBOX-3247] 病理诊断：\n[BBOX-3248] 病理诊断：\n[BBOX-3249] 病理诊断：\n[BBOX-3250] 病理诊断：\n[BBOX-3251] 病理诊断：\n[BBOX-3252] 病理诊断：\n[BBOX-3253] 病理诊断：\n[BBOX-3254] 病理诊断：\n[BBOX-3255] 病理诊断：\n[BBOX-3256] 病理诊断：\n[BBOX-3257] 病理诊断：\n[BBOX-3258] 病理诊断：\n[BBOX-3259] 病理诊断：\n[BBOX-3260] 病理诊断：\n[BBOX-3261] 病理诊断：\n[BBOX-3262] 病理诊断：\n[BBOX-3263] 病理诊断：\n[BBOX-3264] 病理诊断：\n[BBOX-3265] 病理诊断：\n[BBOX-3266] 病理诊断：\n[BBOX-3267] 病理诊断：\n[BBOX-3268] 病理诊断：\n[BBOX-3269] 病理诊断：\n[BBOX-3270] 病理诊断：\n[BBOX-3271] 病理诊断：\n[BBOX-3272] 病理诊断：\n[BBOX-3273] 病理诊断：\n[BBOX-3274] 病理诊断：\n[BBOX-3275] 病理诊断：\n[BBOX-3276] 病理诊断：\n[BBOX-3277] 病理诊断：\n[BBOX-3278] 病理诊断：\n[BBOX-3279] 病理诊断：\n[BBOX-3280] 病理诊断：\n[BBOX-3281] 病理诊断：\n[BBOX-3282] 病理诊断：\n[BBOX-3283] 病理诊断：\n[BBOX-3284] 病理诊断：\n[BBOX-3285] 病理诊断：\n[BBOX-3286] 病理诊断：\n[BBOX-3287] 病理诊断：\n[BBOX-3288] 病理诊断：\n[BBOX-3289] 病理诊断：\n[BBOX-3290] 病理诊断：\n[BBOX-3291] 病理诊断：\n[BBOX-3292] 病理诊断：\n[BBOX-3293] 病理诊断：\n[BBOX-3294] 病理诊断：\n[BBOX-3295] 病理诊断：\n[BBOX-3296] 病理诊断：\n[BBOX-3297] 病理诊断：\n[BBOX-3298] 病理诊断：\n[BBOX-3299] 病理诊断：\n[BBOX-3300] 病理诊断：\n[BBOX-3301] 病理诊断：\n[BBOX-3302] 病理诊断：\n[BBOX-3303] 病理诊断：\n[BBOX-3304] 病理诊断：\n[BBOX-3305] 病理诊断：\n[BBOX-3306] 病理诊断：\n[BBOX-3307] 病理诊断：\n[BBOX-3308] 病理诊断：\n[BBOX-3309] 病理诊断：\n[BBOX-3310] 病理诊断：\n[BBOX-3311] 病理诊断：\n[BBOX-3312] 病理诊断：\n[BBOX-3313] 病理诊断：\n[BBOX-3314] 病理诊断：\n[BBOX-3315] 病理诊断：\n[BBOX-3316] 病理诊断：\n[BBOX-3317] 病理诊断：\n[BBOX-3318] 病理诊断：\n[BBOX-3319] 病理诊断：\n[BBOX-3320] 病理诊断：\n[BBOX-3321] 病理诊断：\n[BBOX-3322] 病理诊断：\n[BBOX-3323] 病理诊断：\n[BBOX-3324] 病理诊断：\n[BBOX-3325] 病理诊断：\n[BBOX-3326] 病理诊断：\n[BBOX-3327] 病理诊断：\n[BBOX-3328] 病理诊断：\n[BBOX-3329] 病理诊断：\n[BBOX-3330] 病理诊断：\n[BBOX-3331] 病理诊断：\n[BBOX-3332] 病理诊断：\n[BBOX-3333] 病理诊断：\n[BBOX-3334] 病理诊断：\n[BBOX-3335] 病理诊断：\n[BBOX-3336] 病理诊断：\n[BBOX-3337] 病理诊断：\n[BBOX-3338] 病理诊断：\n[BBOX-3339] 病理诊断：\n[BBOX-3340] 病理诊断：\n[BBOX-3341] 病理诊断：\n[BBOX-3342] 病理诊断：\n[BBOX-3343] 病理诊断：\n[BBOX-3344] 病理诊断：\n[BBOX-3345] 病理诊断：\n[BBOX-3346] 病理诊断：\n[BBOX-3347] 病理诊断：\n[BBOX-3348] 病理诊断：\n[BBOX-3349] 病理诊断：\n[BBOX-3350] 病理诊断：\n[BBOX-3351] 病理诊断：\n[BBOX-3352] 病理诊断：\n[BBOX-3353] 病理诊断：\n[BBOX-3354] 病理诊断：\n[BBOX-3355] 病理诊断：\n[BBOX-3356] 病理诊断：\n[BBOX-3357] 病理诊断：\n[BBOX-3358] 病理诊断：\n[BBOX-3359] 病理诊断：\n[BBOX-3360] 病理诊断：\n[BBOX-3361] 病理诊断：\n[BBOX-3362] 病理诊断：\n[BBOX-3363] 病理诊断：\n[BBOX-3364] 病理诊断：\n[BBOX-3365] 病理诊断：\n[BBOX-3366] 病理诊断：\n[BBOX-3367] 病理诊断：\n[BBOX-3368] 病理诊断：\n[BBOX-3369] 病理诊断：\n[BBOX-3370] 病理诊断：\n[BBOX-3371] 病理诊断：\n[BBOX-3372] 病理诊断：\n[BBOX-3373] 病理诊断：\n[BBOX-3374] 病理诊断：\n[BBOX-3375] 病理诊断：\n[BBOX-3376] 病理诊断：\n[BBOX-3377] 病理诊断：\n[BBOX-3378] 病理诊断：\n[BBOX-3379] 病理诊断：\n[BBOX-3380] 病理诊断：\n[BBOX-3381] 病理诊断：\n[BBOX-3382] 病理诊断：\n[BBOX-3383] 病理诊断：\n[BBOX-3384] 病理诊断：\n[BBOX-3385] 病理诊断：\n[BBOX-3386] 病理诊断：\n[BBOX-3387] 病理诊断：\n[BBOX-3388] 病理诊断：\n[BBOX-3389] 病理诊断：\n[BBOX-3390] 病理诊断：\n[BBOX-3391] 病理诊断：\n[BBOX-3392] 病理诊断：\n[BBOX-3393] 病理诊断：\n[BBOX-3394] 病理诊断：\n[BBOX-3395] 病理诊断：\n[BBOX-3396] 病理诊断：\n[BBOX-3397] 病理诊断：\n[BBOX-3398] 病理诊断：\n[BBOX-3399] 病理诊断：\n[BBOX-3400] 病理诊断：\n[BBOX-3401] 病理诊断：\n[BBOX-3402] 病理诊断：\n[BBOX-3403] 病理诊断：\n[BBOX-3404] 病理诊断：\n[BBOX-3405] 病理诊断：\n[BBOX-3406] 病理诊断：\n[BBOX-3407] 病理诊断：\n[BBOX-3408] 病理诊断：\n[BBOX-3409] 病理诊断：\n[BBOX-3410] 病理诊断：\n[BBOX-3411] 病理诊断：\n[BBOX-3412] 病理诊断：\n[BBOX-3413] 病理诊断：\n[BBOX-3414] 病理诊断：\n[BBOX-3415] 病理诊断：\n[BBOX-3416] 病理诊断：\n[BBOX-3417] 病理诊断：\n[BBOX-3418] 病理诊断：\n[BBOX-3419] 病理诊断：\n[BBOX-3420] 病理诊断：\n[BBOX-3421] 病理诊断：\n[BBOX-3422] 病理诊断：\n[BBOX-3423] 病理诊断：\n[BBOX-3424] 病理诊断：\n[BBOX-3425] 病理诊断：\n[BBOX-3426] 病理诊断：\n[BBOX-3427] 病理诊断：\n[BBOX-3428] 病理诊断：\n[BBOX-3429] 病理诊断：\n[BBOX-3430] 病理诊断：\n[BBOX-3431] 病理诊断：\n[BBOX-3432] 病理诊断：\n[BBOX-3433] 病理诊断：\n[BBOX-3434] 病理诊断：\n[BBOX-3435] 病理诊断：\n[BBOX-3436] 病理诊断：\n[BBOX-3437] 病理诊断：\n[BBOX-3438] 病理诊断：\n[BBOX-3439] 病理诊断：\n[BBOX-3440] 病理诊断：\n[BBOX-3441] 病理诊断：\n[BBOX-3442] 病理诊断：\n[BBOX-3443] 病理诊断：\n[BBOX-3444] 病理诊断：\n[BBOX-3445] 病理诊断：\n[BBOX-3446] 病理诊断：\n[BBOX-3447] 病理诊断：\n[BBOX-3448] 病理诊断：\n[BBOX-3449] 病理诊断：\n[BBOX-3450] 病理诊断：\n[BBOX-3451] 病理诊断：\n[BBOX-3452] 病理诊断：\n[BBOX-3453] 病理诊断：\n[BBOX-3454] 病理诊断：\n[BBOX-3455] 病理诊断：\n[BBOX-3456] 病理诊断：\n[BBOX-3457] 病理诊断：\n[BBOX-3458] 病理诊断：\n[BBOX-3459] 病理诊断：\n[BBOX-3460] 病理诊断：\n[BBOX-3461] 病理诊断：\n[BBOX-3462] 病理诊断：\n[BBOX-3463] 病理诊断：\n[BBOX-3464] 病理诊断：\n[BBOX-3465] 病理诊断：\n[BBOX-3466] 病理诊断：\n[BBOX-3467] 病理诊断：\n[BBOX-3468] 病理诊断：\n[BBOX-3469] 病理诊断：\n[BBOX-3470] 病理诊断：\n[BBOX-3471] 病理诊断：\n[BBOX-3472] 病理诊断：\n[BBOX-3473] 病理诊断：\n[BBOX-3474] 病理诊断：\n[BBOX-3475] 病理诊断：\n[BBOX-3476] 病理诊断：\n[BBOX-3477] 病理诊断：\n[BBOX-3478] 病理诊断：\n[BBOX-3479] 病理诊断：\n[BBOX-3480] 病理诊断：\n[BBOX-3481] 病理诊断：\n[BBOX-3482] 病理诊断：\n[BBOX-3483] 病理诊断：\n[BBOX-3484] 病理诊断：\n[BBOX-3485] 病理诊断：\n[BBOX-3486] 病理诊断：\n[BBOX-3487] 病理诊断：\n[BBOX-3488] 病理诊断：\n[BBOX-3489] 病理诊断：\n[BBOX-3490] 病理诊断：\n[BBOX-3491] 病理诊断：\n[BBOX-3492] 病理诊断：\n[BBOX-3493] 病理诊断：\n[BBOX-3494] 病理诊断：\n[BBOX-3495] 病理诊断：\n[BBOX-3496] 病理诊断：\n[BBOX-3497] 病理诊断：\n[BBOX-3498] 病理诊断：\n[BBOX-3499] 病理诊断：\n[BBOX-3500] 病理诊断：\n[BBOX-3501] 病理诊断：\n[BBOX-3502] 病理诊断：\n[BBOX-3503] 病理诊断：\n[BBOX-3504] 病理诊断：\n[BBOX-3505] 病理诊断：\n[BBOX-3506] 病理诊断：\n[BBOX-3507] 病理诊断：\n[BBOX-3508] 病理诊断：\n[BBOX-3509] 病理诊断：\n[BBOX-3510] 病理诊断：\n[BBOX-3511] 病理诊断：\n[BBOX-3512] 病理诊断：\n[BBOX-3513] 病理诊断：\n[BBOX-3514] 病理诊断：\n[BBOX-3515] 病理诊断：\n[BBOX-3516] 病理诊断：\n[BBOX-3517] 病理诊断：\n[BBOX-3518] 病理诊断：\n[BBOX-3519] 病理诊断：\n[BBOX-3520] 病理诊断：\n[BBOX-3521] 病理诊断：\n[BBOX-3522] 病理诊断：\n[BBOX-3523] 病理诊断：\n[BBOX-3524] 病理诊断：\n[BBOX-3525] 病理诊断：\n[BBOX-3526] 病理诊断：\n[BBOX-3527] 病理诊断：\n[BBOX-3528] 病理诊断：\n[BBOX-3529] 病理诊断：\n[BBOX-3530] 病理诊断：\n[BBOX-3531] 病理诊断：\n[BBOX-3532] 病理诊断：\n[BBOX-3533] 病理诊断：\n[BBOX-3534] 病理诊断：\n[BBOX-3535] 病理诊断：\n[BBOX-3536] 病理诊断：\n[BBOX-3537] 病理诊断：\n[BBOX-3538] 病理诊断：\n[BBOX-3539] 病理诊断：\n[BBOX-3540] 病理诊断：\n[BBOX-3541] 病理诊断：\n[BBOX-3542] 病理诊断：\n[BBOX-3543] 病理诊断：\n[BBOX-3544] 病理诊断：\n[BBOX-3545] 病理诊断：\n[BBOX-3546] 病理诊断：\n[BBOX-3547] 病理诊断：\n[BBOX-3548] 病理诊断：\n[BBOX-3549] 病理诊断：\n[BBOX-3550] 病理诊断：\n[BBOX-3551] 病理诊断：\n[BBOX-3552] 病理诊断：\n[BBOX-3553] 病理诊断：\n[BBOX-3554] 病理诊断：\n[BBOX-3555] 病理诊断：\n[BBOX-3556] 病理诊断：\n[BBOX-3557] 病理诊断：\n[BBOX-3558] 病理诊断：\n[BBOX-3559] 改检病查\n[BBOX-3560] 费尚增写\n[BBOX-3561] 报告状态\n[BBOX-3562] 咨询日期\n[BBOX-3563] 链签来源\n[BBOX-3564] 读号\n[BBOX-3565] 图像\n[BBOX-3566] 34\n[BBOX-3567] 巴油境\n[BBOX-3568] 2026-01-00 14:10:13\n[BBOX-3569] 4.0\n[BBOX-3570] 巴油境\n[BBOX-3571] 2026-01-28 00:10:53\n[BBOX-3572] 4.0\n[BBOX-3573] 55\n[BBOX-3574] 毛\n[BBOX-3575] t巴油境\n[BBOX-3576] 2026-12-28 13:02\n[BBOX-3577] 2.0\n[BBOX-3578] 50\n[BBOX-3579] 毛\n[BBOX-3580] 5巴油境\n[BBOX-3581] 2026-12-21 14:02\n[BBOX-3582] 2.0\n[BBOX-3583] 50\n[BBOX-3584] 毛\n[BBOX-3585] 一页\n[BBOX-3586] 显示\n[BBOX-3587] 页\n[BBOX-3588] 门楼号\n[BBOX-3589] 姓名\n[BBOX-3590] 病区\n[BBOX-3591] 送检科室\n[BBOX-3592] 标本名称\n[BBOX-3593] 临床诊断\n[BBOX-3594] 内眼所见\n[BBOX-3595] 穿刺组织3条，合计长0.6cm。\n[BBOX-3596] 病理诊断\n[BBOX-3597] (左肺组织穿刺活检）非小细胞肺癌伴大片坏死，待免疫组化。\n[BBOX-3598] 报告医生\n[BBOX-3599] 审核医生\n[BBOX-3600] 报告时间\n[BBOX-3601] 2026-01-28 14:53\n[BBOX-3602] 点击要返回的Pah:QC流程\n[BBOX-3603] CS 扫描全能王\n[BBOX-3604] 3亿人都在用的扫描App\n[BBOX-3605] 门诊号\n[BBOX-3606] 病区\n[BBOX-3607] 送检科室\n[BBOX-3608] 原病理号\n[BBOX-3609] 报告状态\n[BBOX-3610] 收到日期\n[BBOX-3611] 数据来源\n[BBOX-3612] 床号\n[BBOX-3613] 图像\n[BBOX-3614] 审核\n[BBOX-3615] 2026-01-30 14:10:13\n[BBOX-3616] 4.0\n[BBOX-3617] 无\n[BBOX-3618] 已审核\n[BBOX-3619] 2026-01-28 09:16:53\n[BBOX-3620] 4.0\n[BBOX-3621] 55\n[BBOX-3622] 无\n[BBOX-3623] 2020-12-28 12:02\n[BBOX-3624] 2.0\n[BBOX-3625] 58床\n[BBOX-3626] 无\n[BBOX-3627] 2020-12-21 14:02\n[BBOX-3628] 2.0\n[BBOX-3629] 58床\n[BBOX-3630] 无\n[BBOX-3631] 共1页，共4条记录\n[BBOX-3632] 门诊号：\n[BBOX-3633] 姓名\n[BBOX-3634] 性别\n[BBOX-3635] 75岁\n[BBOX-3636] 病人编\n[BBOX-3637] 病区\n[BBOX-3638] 病区\n[BBOX-3639] 病案号\n[BBOX-3640] 门诊号\n[BBOX-3641] 送检科室\n[BBOX-3642] 送检单位\n[BBOX-3643] 送检医生\n[BBOX-3644] 丁晓倩\n[BBOX-3645] 标本名称\n[BBOX-3646] 左肺组织穿刺活检\n[BBOX-3647] 临床诊断\n[BBOX-3648] 1.肺恶性肿瘤2.肺恶性肿瘤\n[BBOX-3649] 病理诊断\n[BBOX-3650] (左肺组织穿刺活检)肺小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合肺癌。\n[BBOX-3651] 免疫组化示肿瘤细胞：CKpan（+），CK7（+），TTF-1（+），p40（-），CK5/6（-）；\n[BBOX-3652] 特殊染色：D-PAS（-）。\n[BBOX-3653] 报告医生\n[BBOX-3654] 医生\n[BBOX-3655] 报告时间\n[BBOX-3656] 2026-01-30 11:19\n[BBOX-3657] 欢迎使用朗珈PathQC病理质控与资料管理系统！\n[BBOX-3658] 12:51\n[BBOX-3659] 2026-01-02\n[BBOX-3660] 病历\n[BBOX-3661] 姓名\n[BBOX-3662] 病区\n[BBOX-3663] 送检科室\n[BBOX-3664] 标本名称\n[BBOX-3665] 临床诊断\n[BBOX-3666] 病理诊断\n[BBOX-3667] 检查项目:肿瘤多基因检测(含MSI)\n[BBOX-3668] 检查方法:高通量测序(NGS)\n[BBOX-3669] 参考基因组:GRCh37/hg19\n[BBOX-3670] 临床数据库:1000 Genomes、ExAC、gnomAD、ClinVar、BRCA Exchange InSiGHT、DBSNP、Cancer Hotspots、COSMIC、JAX CKB、OncoKB等\n[BBOX-3671] 检测突变软件:ADXHS-Classic-H\n[BBOX-3672] 标本病理评估:肿瘤细胞占比30%。\n[BBOX-3673] DNA质量评估:合格\n[BBOX-3674] 测序质量评估:合格\n[BBOX-3675] 表格结果:\n[BBOX-3676] 检测内容 检测结果 突变丰度 备注\n[BBOX-3677] MSI MSS 0/55\n[BBOX-3678] EGFR exon19 c.2235_2249del p.Glu746_Ala750del(E746_A750del) 29.59% I级,具有明确临床意义\n[BBOX-3679] MET 扩增 3.97 I级,具有明确临床意义\n[BBOX-3680] TP53 exon8 p.817C>T p.Arg273Cys(R273C) 6.35% II级,具有潜在临床意义\n[BBOX-3681] 检测结果备注:表格内未列出的为未检出。\n[BBOX-3682] 报告医生\n[BBOX-3683] 生\n[BBOX-3684] 报告时间\n[BBOX-3685] 2026-02-06 16:26\n[BBOX-3686] 住院号\n[BBOX-3687] 门诊号\n[BBOX-3688] 送检医生\n[BBOX-3689] 病人编号\n[BBOX-3690] 1份已审核\n[BBOX-3691] 2026-01-30 14:10:13\n[BBOX-3692] 4.0\n[BBOX-3693] 无\n[BBOX-3694] 2份已审核\n[BBOX-3695] 2026-01-28 09:16:53\n[BBOX-3696] 4.0\n[BBOX-3697] 55\n[BBOX-3698] 无\n[BBOX-3699] 1份已审核\n[BBOX-3700] 2020-12-28 12:02\n[BBOX-3701] 2.0\n[BBOX-3702] 58床\n[BBOX-3703] 无\n[BBOX-3704] 2020-12-21 14:02\n[BBOX-3705] 2.0\n[BBOX-3706] 58床\n[BBOX-3707] 无\n[BBOX-3708] 分子病理检查报告单\n[BBOX-3709] 编\n[BBOX-3710] 患者姓名\n[BBOX-3711] 性别：男\n[BBOX-3712] 年龄：75岁\n[BBOX-3713] 住院号：\n[BBOX-3714] 送检科室\n[BBOX-3715] 尿府理\n[BBOX-3716] 登记号：\n[BBOX-3717] 标本类型：石蜡组织\n[BBOX-3718] 病变部\n[BBOX-3719] 病理诊断：\n[BBOX-3720] 收到日期：2026-01-20\n[BBOX-3721] 检查项目：肿瘤多基因检测（含MSI）\n[BBOX-3722] 检查方法：高通量测序(NGS)\n[BBOX-3723] 参考基因组：GRCh37/hg19\n[BBOX-3724] 临床数据库：1000 Genomes、ExAC、gnomAD、ClinVar、BECA Exchange InSiGHT、DBSNP、\n[BBOX-3725] Cancer Hotspots、COSMIC、JAX CXB、OncoKB等\n[BBOX-3726] 检测突变软件：ADXHS-Classic-H\n[BBOX-3727] 标本病理评估：肿瘤细胞占比30%。\n[BBOX-3728] 核酸质量评估：合格\n[BBOX-3729] 测序质量评估：合格\n[BBOX-3730] 检测结果：\n[BBOX-3731] 检测内容\n[BBOX-3732] 检测结果\n[BBOX-3733] 突变丰度\n[BBOX-3734] 备注\n[BBOX-3735] MSI\n[BBOX-3736] MSS\n[BBOX-3737] 0/55\n[BBOX-3738] EGFR\n[BBOX-3739] exon19 c.2235_2249del\n[BBOX-3740] 29.59%\n[BBOX-3741] I级、具有明确临床意义\n[BBOX-3742] p.Glu746_Ala750del (E746_A750del)\n[BBOX-3743] MET\n[BBOX-3744] 3'端\n[BBOX-3745] 3.97\n[BBOX-3746] I级、具有明确临床意义\n[BBOX-3747] TP53\n[BBOX-3748] exon6 c.817C>T p.Arg273Cys (R273C)\n[BBOX-3749] 6.35%\n[BBOX-3750] II级、具有潜在临床意义\n[BBOX-3751] 备注：表格内未列出的为未检出。\n[BBOX-3752] 注：此报告仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与分子病理诊断科联系。\n[BBOX-3753] 报告.\n[BBOX-3754] 检测者\n[BBOX-3755] 报告日期：2026-02-06\n[BBOX-3756] 第1页/共16页\n[BBOX-3757] CS 扫描全能王\n[BBOX-3758] 3亿人都在用的扫描App\n[BBOX-3759] V2.0\n[BBOX-3760] 循环周期，调节转录，DNA 复\n[BBOX-3761] 制和诱导细胞程序死亡及抗血\n[BBOX-3762] 管生成。\n[BBOX-3763] 细胞瘤）和肾上腺皮质癌。TP53 突变还发生于包括 CML、\n[BBOX-3764] ANLL、MDS 及 B-NHL。在内的多种恶性血液肿瘤以及\n[BBOX-3765] 黑色素瘤、基底细胞癌、鳞状细胞癌等皮肤癌等多种类型\n[BBOX-3766] 肝癌及恶性肿瘤。TP53 突变是多种癌症预后不良的标\n[BBOX-3767] 志，如乳腺癌。TP53 基因变异与肿瘤细胞对铂类化疗药\n[BBOX-3768] 物耐药性相关，但不影响氟杉醇类药物的敏感性；相关化\n[BBOX-3769] 疗药物还包括喜树碱、5-FU、顺铂、环磷酰胺等。FDA 已\n[BBOX-3770] 授予 IXC14586 快速通道资格，目前治疗具有 TP53 Y220C\n[BBOX-3771] 突变的局部晚期或转移性实体瘤患者。\n[BBOX-3772] 四、声明告知\n[BBOX-3773] 1. 本检测项目中使用的参考基因组版本为 hg19，报告中的变异命名遵从 HGVS 指南\n[BBOX-3774] (http://varnomcn.hgvs.org)中的相关规定进行命名。\n[BBOX-3775] 2. 变异分类：综合变异在治疗、诊断和预后方面相关研究证据，将变异分为 4 级：I\n[BBOX-3776] 级为明确临床意义；II 级为潜在临床意义；III 类为临床意义未明；IV 级为良性/可能良\n[BBOX-3777] 性。本报告中仅列出 I-III 级变异。\n[BBOX-3778] 3. 检测结果与临床意义相关性的证据水平分为 4 个等级（A/B/C/D）。A 级：对应\n[BBOX-3779] 病种中 FDA/NMPA 批准或指南推荐的治疗、诊断和（或）预后的相关标志物；B 级：专家\n[BBOX-3780] 共识或 III/IV 期临床试验研究表明对患者肿瘤治疗有敏感或耐药、或具有诊断、预后意义\n[BBOX-3781] 的生物标志物；C 级：FDA/NMPA 批准或专业指南推荐的在其他癌种对某个治疗方案敏感\n[BBOX-3782] 或耐药的标志物；或者是作为临床试验入组标准的标志物；或者是多个小型研究结果证实\n[BBOX-3783] 具有诊断或预后意义的标志物；D 级：临床前研究表明具有潜在的治疗意义，或基于小型\n[BBOX-3784] 研究或多个案例报告可能作为辅助疾病诊断或预后的标志物（结论未形成共识）。\n[BBOX-3785] 4. 本检测的检测内容大部分基于仅限于 DNA 水平，部分基因涉及 RNA 水平，但\n[BBOX-3786] 不涉及蛋白水平的检测。\n[BBOX-3787] 5. 对于组织样品，如样本中肿瘤细胞含量低于 20%，可能影响检测结果的准确性；\n[BBOX-3788] 如未检出指定的基因变异，可能由于该样本中该突变的丰度低于本项目的检测下限。\n[BBOX-3789] 6. 对于组织样品，肿瘤存在异质性，即不同病灶甚至同一病灶内的组织的突变图谱可\n[BBOX-3790] 能也存在差异；另外，不同疾病发展或治疗阶段取出的样本中的突变可能不同；因此，本\n[BBOX-3791] 检测报告仅对此次送检的样本负责。并且，所检测的突变位点仅限于本检测试剂的检测范\n[BBOX-3792] 围，样品的基因组中可能存在的某些罕见或复杂突变，本项目不能完全检测。\n[BBOX-3793] 7. 本报告对于测序结果分析中核苷酸改变的位置信息是基于当前版本的基因组和转录\n[BBOX-3794] 本，随着人类基因组的更新，这些信息可能会有所不同；同时对于突变位点的解读，是基\n[BBOX-3795] 于当前已发表的文献、指南、公共数据库及临床研究结果，随着研究的发展，特定位点的\n[BBOX-3796] 解读可能发生变更。\n[BBOX-3797] 8. 本检测仅为临床治疗或诊断提供参考，具体的诊断结果及治疗决策应由临床医生综\n[BBOX-3798] 合患者的各种临床信息和检测结果进行判断。\n[BBOX-3799] CS 扫描全能王\n[BBOX-3800] 3 亿人都在用的扫描 App\n[BBOX-3801] 超声检查报告单\n[BBOX-3802] 思者登\n[BBOX-3803] 姓\n[BBOX-3804] 性别：男\n[BBOX-3805] 年龄：75岁\n[BBOX-3806] 床号：A02\n[BBOX-3807] 检查所见：\n[BBOX-3808] 右肝最大斜径12.8cm，左肝前后径6.4cm，上下径7.5cm，肝表面光滑，边缘规则，肝内\n[BBOX-3809] 呈细小点状回声，分布欠均匀，肝内见数个囊性回声，大者0.8x0.5cm，均透声可。\n[BBOX-3810] 空腹胆囊充盈差，胆囊区见胆囊祥回声，大小约3.4x1.4cm，腔内透声差，充满细密点\n[BBOX-3811] 状回声。\n[BBOX-3812] 胆总管内径0.5cm，未见明显异常回声，肝内胆管无明显扩张。\n[BBOX-3813] 胰腺大小形态可，表面光滑，内回声均匀，主胰管内径不宽。\n[BBOX-3814] 脾未探及。\n[BBOX-3815] 门静脉走行自然，呈入肝血流，门静脉主干内径1.0cm，入肝血流速度17.4cm/s，肝内\n[BBOX-3816] 门静脉血流充盈好，未见明显异常回声。\n[BBOX-3817] 肝静脉走行自然，各支内径不宽，腔内未见明显异常回声，血流速及频谱形态未见异\n[BBOX-3818] 常。\n[BBOX-3819] 双侧肾上腺区未见明显占位性病变。\n[BBOX-3820] 双肾大小形态正常，表面光滑，皮髓质分界清，左肾实质回声无明显异常，右肾中部实\n[BBOX-3821] 质内见1.5x1.2cm略高回声结节，边界清，双肾窦无分离扩张。\n[BBOX-3822] 双侧输尿管无明显扩张。\n[BBOX-3823] 膀胱充盈可，黏膜光滑，腔内未见明显占位。\n[BBOX-3824] 前列腺大小约4.0（左右径）×3.5（前后径）×3.2（上下径）cm，体积约23.3cm3，\n[BBOX-3825] 表面光滑，中叶略突，内部回声欠均匀。\n[BBOX-3826] 双侧精囊腺无肿大，内部回声均匀。\n[BBOX-3827] 双肾动脉主干血流通畅，肾内动脉血流分布好。\n[BBOX-3828] 左肾叶间动脉Vs 24.8cm/s，阻力指数（RI）0.66。\n[BBOX-3829] 右肾叶间动脉Vs 25.1cm/s，阻力指数（RI）0.65。\n[BBOX-3830] 超声提示：脾切除术后\n[BBOX-3831] 空腹胆囊充盈差、腔内透声差，慢性胆囊炎？请结合临床\n[BBOX-3832] 肝囊肿\n[BBOX-3833] 右肾略高回声结节，考虑良性（结合病史考虑复杂囊肿可能）\n[BBOX-3834] 前列腺增生并钙化\n[BBOX-3835] 报告日期：2026-01-27 08:35:35 记录人\n[BBOX-3836] CS 扫描全能王\n[BBOX-3837] 3亿人都在用的扫描App\n[BBOX-3838] 超声检查报告单\n[BBOX-3839] 患者登记\n[BBOX-3840] 姓名：\n[BBOX-3841] 性别：男\n[BBOX-3842] 年龄：75岁\n[BBOX-3843] 号\n[BBOX-3844] 1\n[BBOX-3845] 2\n[BBOX-3846] 检查所见：\n[BBOX-3847] 甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。\n[BBOX-3848] 甲状旁腺区未见明显异常回声。\n[BBOX-3849] 左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门\n[BBOX-3850] 髓结构不清，CDFI：内见条状血流信号。\n[BBOX-3851] 右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。\n[BBOX-3852] 超声提示：左侧颈部淋巴结肿大，考虑“M”性可能\n[BBOX-3853] 报告日期：2026-01-27 08:26:34 记\n[BBOX-3854] 名.\n[BBOX-3855] 注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。\n[BBOX-3856] CS 扫描全能王\n[BBOX-3857] 3亿人都在用的扫描App\n[BBOX-3858] 影像学检查报告单\n[BBOX-3859] 扫一扫查看云胶片（访问码）：\n[BBOX-3860] 姓名：\n[BBOX-3861] 性别：男\n[BBOX-3862] 年龄：75岁\n[BBOX-3863] 影像\n[BBOX-3864] 住院号：\n[BBOX-3865] 登记号：\n[BBOX-3866] 检查名称：胸部CT增强成像（单独）\n[BBOX-3867] 检查方法：AXI+C\n[BBOX-3868] 图像所见：胸廓及胸腔容积基本正常。纵隔左偏。左肺可见软组织密度肿块，边界不\n[BBOX-3869] 清，大小约59mm*66mm，较前2024.09.03CT所示明显增大，呈不均匀强\n[BBOX-3870] 化。左主支气管及左肺上叶、下叶支气管狭窄，其远端肺组织实变，较前\n[BBOX-3871] 相仿。左肺下叶后基底段(6im53-54)见实性结节，大小约为11mm×8mm。\n[BBOX-3872] 双肺见多发小、微结节，较大者位于左肺下叶背段(6im39-41)，呈实性\n[BBOX-3873] 密度，大小约为9mm×7mm。双肺见多发斑片、索条影。气管未见狭窄或梗\n[BBOX-3874] 阻。纵隔及左肺门可见多发肿大淋巴结，较前相仿。心影未见明显增大。\n[BBOX-3875] 左侧部分肋骨局部形态不规整。\n[BBOX-3876] 印象：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床\n[BBOX-3877] 双肺多发结节，较前增多、增大，请结合临床随访\n[BBOX-3878] 双肺慢性炎症或纤维灶可能性大，请结合临床\n[BBOX-3879] 左侧部分肋骨局部形态不规整，请结合临床\n[BBOX-3880] 报告医师\n[BBOX-3881] 审核医\n[BBOX-3882] 该报告仅供临床医师参考；如需商榷，请通过临床医师与审核医师沟通\n[BBOX-3883] 流水号\n[BBOX-3884] 影像学检查报告单\n[BBOX-3885] 姓名：\n[BBOX-3886] 性别：男\n[BBOX-3887] 年龄：70岁\n[BBOX-3888] 影像\n[BBOX-3889] 检查日期：2020-12-23\n[BBOX-3890] 报告日期：2020-12-23\n[BBOX-3891] 报告时间：10.00\n[BBOX-3892] 检查名称：全身骨显像\n[BBOX-3893] 检查方法：显像剂：99mTc-MDP\n[BBOX-3894] 图像所见：静脉注射显像剂2小时后行全身骨显像，图像清晰，对比度可。\n[BBOX-3895] 前位：双侧膝关节见显像剂浓聚灶。颅骨，锁骨，胸骨，前肋，骨盆显像\n[BBOX-3896] 剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。\n[BBOX-3897] 后位：脊椎见显像剂浓聚灶。颅骨，肩胛骨，后肋，骨盆显像剂分布基本\n[BBOX-3898] 左右对称，未见明显异常显像剂浓聚或稀疏区。\n[BBOX-3899] 印\n[BBOX-3900] 象：1，脊椎及双侧膝关节退行性变可能性大\n[BBOX-3901] 2，其余部位骨骼未见明显转移瘤，建议定期复查\n[BBOX-3902] 报告[\n[BBOX-3903] 审核医师：\n[BBOX-3904] 该报告反映受检者当时情况，仅供临床医师参考。\n[BBOX-3905] 流水号\n[BBOX-3906] 胶片\n[BBOX-3907] 影像学检查报告单\n[BBOX-3908] 扫码看电子胶片\n[BBOX-3909] 姓\n[BBOX-3910] 性别：男\n[BBOX-3911] 年龄：70岁\n[BBOX-3912] 影像\n[BBOX-3913] 科\n[BBOX-3914] 住院\n[BBOX-3915] 检查日期：2020-12-22\n[BBOX-3916] 报告日期：2020-12-23\n[BBOX-3917] 报告时间：14:22:52\n[BBOX-3918] 登记号\n[BBOX-3919] 40\n[BBOX-3920] 检查名称：颅脑MR平扫成像+DWI成像\n[BBOX-3921] 检查方法：AXI:FSE T1WI, T2WI, FLAIR, DWI\n[BBOX-3922] SAG:FSE T1WI\n[BBOX-3923] 图像所见：双侧额顶叶白质可见散在斑点状等T1稍长T2信号影，FLAIR为高信号，\n[BBOX-3924] DWI为等信号。脑室系统略扩大，脑沟、脑池明显加深，中线结构居中。\n[BBOX-3925] 印象：1. 血管性脱髓鞘（Fazekas 1级），请结合临床复查\n[BBOX-3926] 2. 老年性脑改变\n[BBOX-3927] 报告\n[BBOX-3928] 审核医师：\n[BBOX-3929] 该报告反映受检者当时情况，仅供临床医师参考。\n[BBOX-3930] 流水号\n[BBOX-3931] CS 扫描全能王\n[BBOX-3932] 3亿人都在用的扫描App\n[BBOX-3933] 超声检查报告单\n[BBOX-3934] 患者\n[BBOX-3935] 性别：男\n[BBOX-3936] 年龄：75岁\n[BBOX-3937] 检查所见：\n[BBOX-3938] 甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。\n[BBOX-3939] 甲状旁腺区未见明显异常回声。\n[BBOX-3940] 左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门\n[BBOX-3941] 髓结构不清，CDFI：内见条状血流信号。\n[BBOX-3942] 右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。\n[BBOX-3943] 超声提示：左侧颈部淋巴结肿大，考虑“Ⅱ”性可能\n[BBOX-3944] 报告日期：2026-01-27 08:26:34 记录\n[BBOX-3945] 师\n[BBOX-3946] 注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。\n[BBOX-3947] 心电图报告单\n[BBOX-3948] 性别：男\n[BBOX-3949] 年龄：75岁\n[BBOX-3950] 危重症医学科率：69 bpm\n[BBOX-3951] P-R间期：139 ms\n[BBOX-3952] QRS时间：90 ms\n[BBOX-3953] QT/QTc : 414/445 ms\n[BBOX-3954] P-R-T : 63/22/25 度\n[BBOX-3955] SV1/RV5:0.49/1.35 mV\n[BBOX-3956] RV5+SV1:1.84mV\n[BBOX-3957] 诊断：大致正常心电图\n[BBOX-3958] 检查时间：2026-01-26 10:31:55\n[BBOX-3959] 检查医生：\n[BBOX-3960] I\n[BBOX-3961] II\n[BBOX-3962] III\n[BBOX-3963] AVR\n[BBOX-3964] AVL\n[BBOX-3965] AVF\n[BBOX-3966] V1\n[BBOX-3967] V2\n[BBOX-3968] V3\n[BBOX-3969] V4\n[BBOX-3970] V5\n[BBOX-3971] V6\n[BBOX-3972] 检查者：\n[BBOX-3973] 25 mm/s 10 mm/mv\n[BBOX-3974] 报告审核\n[BBOX-3975] 时间：2026-01-26 10:35:22\n[BBOX-3976] 以上结果请结合临床及前图\n[BBOX-3977] 1/1\n[BBOX-3978] \\begin{tabular}{cccccccccc}\n[BBOX-3979] 报告时间: 2020-01-07\n[BBOX-3980] \\hline\n[BBOX-3981] \\multicolumn{10}{c}{\\textbf{检验报告单 (血型尿常规)}} \\\\\n[BBOX-3982] \\hline\n[BBOX-3983] \\multicolumn{2}{c}{姓名} & \\multicolumn{2}{c}{四四库呼呼与抗重球球学目} & \\multicolumn{2}{c}{床 号:} & \\multicolumn{2}{c}{号:} & \\multicolumn{2}{c}{号:} \\\\\n[BBOX-3984] \\multicolumn{2}{c}{性别} & \\multicolumn{2}{c}{10001100101} & \\multicolumn{2}{c}{标本种类:} & \\multicolumn{2}{c}{李曲} & \\multicolumn{2}{c}{标本状态:} \\\\\n[BBOX-3985] \\multicolumn{2}{c}{年龄} & \\multicolumn{2}{c}{1001000} & \\multicolumn{2}{c}{临床诊断:} & \\multicolumn{2}{c}{脑垂体肿瘤} & \\multicolumn{2}{c}{} \\\\\n[BBOX-3986] \\hline\n[BBOX-3987] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{生物参考区间} & \\multicolumn{2}{c}{单位} & \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{生物参考区间} & \\multicolumn{2}{c}{单位} \\\\\n[BBOX-3988] \\hline\n[BBOX-3989] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{35} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} \\\\\n[BBOX-3990] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} \\\\\n[BBOX-3991] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} \\\\\n[BBOX-3992] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} \\\\\n[BBOX-3993] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-3994] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-3995] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-3996] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-3997] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-3998] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-3999] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4000] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4001] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4002] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4003] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4004] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4005] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4006] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4007] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4008] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4009] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4010] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4011] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4012] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4013] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4014] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4015] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4016] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4017] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4018] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4019] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4020] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4021] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4022] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4023] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4024] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4025] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4026] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4027] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4028] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4029] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4030] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4031] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4032] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4033] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4034] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4035] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4036] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4037] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4038] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4039] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4040] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4041] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4042] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4043] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4044] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4045] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4046] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4047] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4048] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4049] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4050] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4051] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4052] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4053] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4054] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4055] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4056] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4057] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4058] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4059] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4060] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4061] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4062] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4063] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4064] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4065] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4066] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4067] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4068] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4069] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4070] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4071] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4072] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4073] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4074] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4075] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4076] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4077] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4078] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4079] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4080] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4081] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4082] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4083] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4084] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4085] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4086] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4087] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4088] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4089] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4090] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4091] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4092] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4093] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4094] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4095] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4096] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4097] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4098] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4099] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4100] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4101] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4102] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4103] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4104] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4105] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4106] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4107] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4108] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n[BBOX-4109] \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\mult\n[BBOX-4110] \\begin{tabular}{llllllllll}\n[BBOX-4111] 报告时间: 2026-01-27\n[BBOX-4112] \\hline\n[BBOX-4113] \\multicolumn{2}{l}{质评合格,省内参考} & \\multicolumn{4}{l}{} & \\multicolumn{4}{l}{采集时间:} \\\\\n[BBOX-4114] \\multicolumn{2}{l}{住院} & \\multicolumn{4}{l}{} & \\multicolumn{4}{l}{} \\\\\n[BBOX-4115] \\multicolumn{2}{l}{尿干化学,尿有形成分分析} & \\multicolumn{4}{l}{} & \\multicolumn{4}{l}{采集人员:} \\\\\n[BBOX-4116] \\multicolumn{2}{l}{} & \\multicolumn{4}{l}{} & \\multicolumn{4}{l}{} \\\\\n[BBOX-4117] \\hline\n[BBOX-4118] \\multicolumn{2}{l}{姓} & 科 & \\multicolumn{2}{l}{.学科} & 床 & 气 & \\multicolumn{2}{l}{样本编} & \\\\\n[BBOX-4119] \\multicolumn{2}{l}{性} & 别: 男 & \\multicolumn{2}{l}{病人} & \\multicolumn{2}{l}{标本种类: 尿液} & \\multicolumn{2}{l}{标本性状:} & \\\\\n[BBOX-4120] \\multicolumn{2}{l}{年} & 龄: 75岁 & \\multicolumn{2}{l}{住院} & \\multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \\multicolumn{2}{l}{} & \\\\\n[BBOX-4121] \\hline\n[BBOX-4122] NO & 项 & 目 & 结果 & 生物参考区间 & 单位 & NO & 项 & 目 & 结果 \\\\\n[BBOX-4123] \\hline\n[BBOX-4124] 1 & 白细胞 & -- & 阴性 & 20 & 电导率 & 16.3 & 3.0-39.0 & mS/cm & \\\\\n[BBOX-4125] 2 & 隐血 & -- & 阴性 & 21 & 红细胞信息 & -- & 阴性 & & \\\\\n[BBOX-4126] 3 & 蛋白 & -- & 阴性 & & & & & & \\\\\n[BBOX-4127] 4 & 葡萄糖 & -- & 阴性 & & & & & & \\\\\n[BBOX-4128] 5 & PH & 6.5 & 4.5-8.0 & & & & & & \\\\\n[BBOX-4129] 6 & 比重 & 1.016 & 1.003-1.030 & & & & & & \\\\\n[BBOX-4130] 7 & 酮体 & -- & 阴性 & & & & & & \\\\\n[BBOX-4131] 8 & 胆红素 & -- & 阴性 & & & & & & \\\\\n[BBOX-4132] 9 & 尿胆原 & 正常 & 阴性-弱阳性 & & & & & & \\\\\n[BBOX-4133] 10 & 亚硝酸盐 & -- & 阴性 & & & & & & \\\\\n[BBOX-4134] 11 & 浊度 & 清亮 & & & & & & & \\\\\n[BBOX-4135] 12 & 白细胞计数 & 2.4 & 0.0-25.0 & /uL & & & & & \\\\\n[BBOX-4136] 13 & 红细胞计数 & 3.2 & 0.0-23.0 & /uL & & & & & \\\\\n[BBOX-4137] 14 & 上皮细胞计数 & 0.4 & 0.0-31.0 & /uL & & & & & \\\\\n[BBOX-4138] 15 & 管型计数 & 0.0 & 0.0-2.0 & /uL & & & & & \\\\\n[BBOX-4139] 16 & 小圆上皮细胞 & 0.4 & 0.0-3.0 & /uL & & & & & \\\\\n[BBOX-4140] 17 & 类酵母细胞 & -- & 0.0-0.0 & & & & & & \\\\\n[BBOX-4141] 18 & 结晶检查 & 0.0 & 0.0-10.0 & /uL & & & & & \\\\\n[BBOX-4142] 19 & 细菌计数 & 8.5 & 0.0-1200.0 & /uL & & & & & \\\\\n[BBOX-4143] \\hline\n[BBOX-4144] \\multicolumn{10}{l}{备注:} \\\\\n[BBOX-4145] \\hline\n[BBOX-4146] \\multicolumn{2}{l}{接收时间: 2026-01-27 08:37} & \\multicolumn{2}{l}{报告时间:} & \\multicolumn{2}{l}{2026-01-27 08:59} & \\multicolumn{4}{l}{检验者:} \\\\\n[BBOX-4147] \\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \\multicolumn{2}{l}{送检医} & \\multicolumn{6}{l}{} \\\\\n[BBOX-4148] \\multicolumn{10}{l}{本报告仅对本次检验标本负责,如对检验结果有疑问,请与相关院区检验科联系!} \\\\\n[BBOX-4149] \\multicolumn{10}{r}{第1页 共1页} \\\\\n[BBOX-4150] \\hline\n[BBOX-4151] \\end{tabular}\n[BBOX-4152] \\begin{tabular}{llllllll}\n[BBOX-4153] 报告时间: 2026-01-27\n[BBOX-4154] \\hline\n[BBOX-4155] \\multicolumn{2}{l}{质评合格,省内参考} & \\multicolumn{4}{c}{\\textbf{检验报告}} & \\multicolumn{2}{r}{采集时间:} \\\\\n[BBOX-4156] \\multicolumn{2}{l}{住院} & \\multicolumn{4}{c}{} & \\multicolumn{2}{r}{2026-01-27 05:46} \\\\\n[BBOX-4157] \\multicolumn{2}{l}{D-二聚体,血浆抗凝血酶AT} & \\multicolumn{4}{c}{} & \\multicolumn{2}{r}{采集} \\\\\n[BBOX-4158] \\hline\n[BBOX-4159] \\multicolumn{1}{l}{姓} & \\multicolumn{1}{l}{名} & \\multicolumn{1}{l}{别} & \\multicolumn{1}{l}{床} & \\multicolumn{1}{l}{号.} & \\multicolumn{1}{l}{样本编} & \\multicolumn{2}{l}{} \\\\\n[BBOX-4160] \\multicolumn{1}{l}{性} & \\multicolumn{1}{l}{} & \\multicolumn{1}{l}{ID:} & \\multicolumn{1}{l}{标本种类:} & \\multicolumn{1}{l}{血浆} & \\multicolumn{1}{l}{标本性状.} & \\multicolumn{2}{l}{} \\\\\n[BBOX-4161] \\multicolumn{1}{l}{年} & \\multicolumn{1}{l}{龄: 75岁} & \\multicolumn{1}{l}{号} & \\multicolumn{1}{l}{临床诊断:} & \\multicolumn{1}{l}{肺恶性肿瘤} & \\multicolumn{2}{l}{} & \\multicolumn{1}{l}{} \\\\\n[BBOX-4162] \\hline\n[BBOX-4163] \\textbf{项} & \\textbf{目} & \\textbf{中} & \\textbf{不} & \\textbf{提示} & \\textbf{生物参考区间} & \\textbf{单位} & \\\\\n[BBOX-4164] \\hline\n[BBOX-4165] 1 & 凝血酶原时间 & 13.2 & & & 10.0-14.0 & sec & \\\\\n[BBOX-4166] 2 & PT-国际标准化比值 & 1.13 & & & 0.80-1.20 & INR & \\\\\n[BBOX-4167] 3 & PT百分活度 & 84 & & & 80-200 & \\% & \\\\\n[BBOX-4168] 4 & 活化部分凝血活酶时间 & 31.8 & & & 22.0-38.0 & sec & \\\\\n[BBOX-4169] 5 & APTT比值 & 1.12 & & & 0.73-1.27 & R & \\\\\n[BBOX-4170] 6 & 凝血酶时间 & 18.1 & & & 14.0-21.0 & sec & \\\\\n[BBOX-4171] 7 & TT比值 & 1.06 & & & 0.82-1.23 & R & \\\\\n[BBOX-4172] 8 & 纤维蛋白原 & 5.80 & $\\uparrow$ & & 2.0-4.0 & g/L & \\\\\n[BBOX-4173] 9 & 抗凝血酶III & 96 & & & 82-121 & \\% & \\\\\n[BBOX-4174] 10 & D-二聚体测定 & 550 & $\\uparrow$ & & 0-500 & ng/ml & \\\\\n[BBOX-4175] \\hline\n[BBOX-4176] \\multicolumn{8}{l}{备注:} \\\\\n[BBOX-4177] \\hline\n[BBOX-4178] \\multicolumn{2}{l}{接收时间: 2026-01-27 07:13} & \\multicolumn{2}{l}{报告时间: 2026-01-27 11:05} & \\multicolumn{2}{l}{检验者:} & \\multicolumn{2}{l}{审核者:} \\\\\n[BBOX-4179] \\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \\multicolumn{2}{l}{送检医} & \\multicolumn{4}{l}{} \\\\\n[BBOX-4180] \\multicolumn{8}{l}{本报告仅对本次检验标本负责,如对检验结} & \\multicolumn{4}{l}{\\textbf{第1页 共1页}} \\\\\n[BBOX-4181] \\hline\n[BBOX-4182] \\end{tabular}\n[BBOX-4183] \\begin{tabular}{lllllll}\n[BBOX-4184] 报告时间: 2026-01-27\n[BBOX-4185] \\hline\n[BBOX-4186] 项 & 目 & 结果 & 提示 & 生物参考区间 & 单位 \\\\\n[BBOX-4187] \\hline\n[BBOX-4188] 1 & 乙型肝炎表面抗原(化学发光法) & 0.00 & 阴性 & $<$0.05 & IU/ml \\\\\n[BBOX-4189] 2 & 丙型肝炎抗体 & 0.07 & 阴性 & $<$1 & S/CO \\\\\n[BBOX-4190] 3 & HIV抗体/p24抗原 & 0.13 & 阴性 & $<$1.00 & S/CO \\\\\n[BBOX-4191] 4 & 梅毒螺旋体抗体 & 0.08 & 无反应 & $<$1.00 & S/CO \\\\\n[BBOX-4192] \\hline\n[BBOX-4193] \\end{tabular}\n[BBOX-4194] \\begin{tabular}{llllllll}\n[BBOX-4195] 报告时间: 2026-01-27\n[BBOX-4196] \\hline\n[BBOX-4197] \\multicolumn{2}{l}{质评合格,省内参考} & \\multicolumn{6}{r}{采集时间:} \\\\\n[BBOX-4198] \\multicolumn{2}{l}{住院} & \\multicolumn{6}{r}{2026-01-27 05:46} \\\\\n[BBOX-4199] \\multicolumn{2}{l}{F-PSA, CA72-4, CA19-9, $\\beta$-h} & \\multicolumn{6}{r}{采} \\\\\n[BBOX-4200] \\multicolumn{2}{l}{\\textbf{检验报告}} & \\multicolumn{6}{r}{} \\\\\n[BBOX-4201] \\hline\n[BBOX-4202] \\multicolumn{2}{l}{姓} & 男 & \\multicolumn{2}{l}{床号: 55} & \\multicolumn{3}{l}{样本} \\\\\n[BBOX-4203] \\multicolumn{2}{l}{性} & 人 IP & \\multicolumn{2}{l}{标本种类: 血清} & \\multicolumn{3}{l}{标本} \\\\\n[BBOX-4204] \\multicolumn{2}{l}{年} & 龄: 75岁 & \\multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \\multicolumn{3}{l}{} \\\\\n[BBOX-4205] \\hline\n[BBOX-4206] \\multicolumn{2}{l}{\\textbf{项}} & \\textbf{目} & \\textbf{不} & \\textbf{提示} & \\textbf{生物参考区间} & \\textbf{单位} \\\\\n[BBOX-4207] \\hline\n[BBOX-4208] 1 & 癌胚抗原 & 9.21 & $\\uparrow$ & 0-5.0 & ng/ml & \\\\\n[BBOX-4209] 2 & 甲胎蛋白 & 1.64 & & 0-7.00 & ng/ml & \\\\\n[BBOX-4210] 3 & 糖类抗原72-4 & 2.08 & & 0-6.9 & U/ml & \\\\\n[BBOX-4211] 4 & 神经元特异性烯醇化酶 & 22.47 & $\\uparrow$ & 0-17 & ng/ml & \\\\\n[BBOX-4212] 5 & 细胞角蛋白19片段 & 5.70 & $\\uparrow$ & 0-3.3 & ng/ml & \\\\\n[BBOX-4213] 6 & 鳞状细胞癌相关抗原 & 2.97 & $\\uparrow$ & 0-2.5 & ng/ml & \\\\\n[BBOX-4214] 7 & 胃泌素释放肽前体 & 37.68 & & 0-68.3 & pg/mL & \\\\\n[BBOX-4215] 8 & 总前列腺特异性抗原 & 4.820 & $\\uparrow$ & 0-4 & ng/ml & \\\\\n[BBOX-4216] 9 & 游离前列腺特异性抗原 & 0.767 & & 0-0.93 & ng/ml & \\\\\n[BBOX-4217] 10 & FPSA/TPSA & 0.159 & & $>$0.15 & & \\\\\n[BBOX-4218] 11 & 特异$\\beta$人绒毛膜促性腺激素 & 5.86 & $\\uparrow$ & 0-2.6 & mIU/ml & \\\\\n[BBOX-4219] 12 & 糖类抗原19-9 & 27.60 & & 0-30 & U/ml & \\\\\n[BBOX-4220] \\hline\n[BBOX-4221] \\multicolumn{8}{l}{备注:} \\\\\n[BBOX-4222] \\hline\n[BBOX-4223] \\multicolumn{2}{l}{接收时间: 2026-01-27 06:57} & \\multicolumn{2}{l}{报告时间: 2026-01-27 10:21} & \\multicolumn{2}{l}{检验者:} & \\multicolumn{2}{l}{审核者:} \\\\\n[BBOX-4224] \\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \\multicolumn{2}{l}{送检医生:} & \\multicolumn{4}{l}{} \\\\\n[BBOX-4225] \\multicolumn{8}{l}{本报告仅对本次检验标本负责, 如对检验结果有疑问, 请在3个工作日内与相关院区检验科联系!} \\\\\n[BBOX-4226] \\multicolumn{8}{r}{第1页 共1页} \\\\\n[BBOX-4227] \\hline\n[BBOX-4228] \\end{tabular}\n[BBOX-4229] 20201221确诊 肺腺癌\n[BBOX-4230] 20201227培美+卡铂\n[BBOX-4231] 出院后吉非替尼3个月，后奥西\n[BBOX-4232] 替尼服用至202601"
  }
]
2026-08-10 17:41:56,037 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:41:56.034+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:42:28,109 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:42:28.106+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:43:00,176 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:43:00.175+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:43:03,095 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:03,127 INFO     29 [SmartSplitter] SmartSplitter done: 20 chunks from 20 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 1, 'ExaminationReport': 12, 'LabReport': 5}
2026-08-10 17:43:03,144 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 17:43:03,145 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "20 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 1, 'ExaminationReport': 12, 'LabReport': 5}"}
2026-08-10 17:43:03,145 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 17:43:03,148 INFO     29 [ChunkRouter] Routed 20 chunks into 5 groups: {'chunks_Admission': 1, 'chunks_Discharge': 1, 'chunks_Clinical': 1, 'chunks_Examination': 12, 'chunks_LabExam': 5}
2026-08-10 17:43:03,163 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 17:43:03,164 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | ChunkRouter:Router | outputs={"html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks": "20 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 1, 'ExaminationReport': 12, 'LabReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:43:03,164 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 17:43:03,169 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:43:03,170 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:43:03,170 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[21, 22]
2026-08-10 17:43:03,170 INFO     29 [qwen-vl-table] positions ： [[21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:43:03,343 INFO     29 [qwen-vl-table] page=21, rect=842x595, img=(2339x1653)
2026-08-10 17:43:03,488 INFO     29 [qwen-vl-table] page=22, rect=842x595, img=(2339x1653)
2026-08-10 17:43:03,489 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:03,489 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 3978, \"bbox_end\": 4110, \"encounter_dates\": [\"2020-01-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccccc}\n报告时间: 2020-01-07\n\\hline\n\\multicolumn{10}{c}{\\textbf{检验报告单 (血型尿常规)}} \\\\\n\\hline\n\\multicolumn{2}{c}{姓名} & \\multicolumn{2}{c}{四四库呼呼与抗重球球学目} & \\multicolumn{2}{c}{床 号:} & \\multicolumn{2}{c}{号:} & \\multicolumn{2}{c}{号:} \\\\\n\\multicolumn{2}{c}{性别} & \\multicolumn{2}{c}{10001100101} & \\multicolumn{2}{c}{标本种类:} & \\multicolumn{2}{c}{李曲} & \\multicolumn{2}{c}{标本状态:} \\\\\n\\multicolumn{2}{c}{年龄} & \\multicolumn{2}{c}{1001000} & \\multicolumn{2}{c}{临床诊断:} & \\multicolumn{2}{c}{脑垂体肿瘤} & \\multicolumn{2}{c}{} \\\\\n\\hline\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{生物参考区间} & \\multicolumn{2}{c}{单位} & \\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{生物参考区间} & \\multicolumn{2}{c}{单位} \\\\\n\\hline\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{35} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} & \\multicolumn{2}{c}{10 0/1} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} & \\multicolumn{2}{c}{10 0 10 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} & \\multicolumn{2}{c}{00 0 00 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} & \\multicolumn{2}{c}{0 0 10 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\",
    "role": "user"
  }
]
2026-08-10 17:43:06,653 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:06,653 INFO     29 [qwen-vl-table] page=21 LLM output (len=48):
{
  "report_date": "2020-01-07",
  "items": []
}
2026-08-10 17:43:06,653 WARNING  29 [qwen-vl-table] page=21 no items extracted
2026-08-10 17:43:06,654 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:06,654 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 3978, \"bbox_end\": 4110, \"encounter_dates\": [\"2020-01-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} & \\multicolumn{2}{c}{0 0 0 0} \\\\\n\\multicolumn{2}{c}{日} & \\multicolumn{2}{c}{00} & \\mult\n\\begin{tabular}{llllllllll}",
    "role": "user"
  }
]
2026-08-10 17:43:10,002 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:10,002 INFO     29 [qwen-vl-table] page=22 LLM output (len=40):
{
  "report_date": null,
  "items": []
}
2026-08-10 17:43:10,003 WARNING  29 [qwen-vl-table] page=22 no items extracted
2026-08-10 17:43:10,003 INFO     29 [qwen-vl-table] coord grouping: {}
2026-08-10 17:43:10,003 INFO     29 [qwen-vl-table] new_positions (0):
[]
2026-08-10 17:43:10,003 WARNING  29 [qwen-vl-table] No items extracted from any page
2026-08-10 17:43:10,003 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:43:10,004 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:43:10,004 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[22]
2026-08-10 17:43:10,004 INFO     29 [qwen-vl-table] positions ： [[22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:43:10,154 INFO     29 [qwen-vl-table] page=22, rect=842x595, img=(2339x1653)
2026-08-10 17:43:10,154 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:10,155 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 4111, \"bbox_end\": 4151, \"encounter_dates\": [\"2026-01-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "报告时间: 2026-01-27\n\\hline\n\\multicolumn{2}{l}{质评合格,省内参考} & \\multicolumn{4}{l}{} & \\multicolumn{4}{l}{采集时间:} \\\\\n\\multicolumn{2}{l}{住院} & \\multicolumn{4}{l}{} & \\multicolumn{4}{l}{} \\\\\n\\multicolumn{2}{l}{尿干化学,尿有形成分分析} & \\multicolumn{4}{l}{} & \\multicolumn{4}{l}{采集人员:} \\\\\n\\multicolumn{2}{l}{} & \\multicolumn{4}{l}{} & \\multicolumn{4}{l}{} \\\\\n\\hline\n\\multicolumn{2}{l}{姓} & 科 & \\multicolumn{2}{l}{.学科} & 床 & 气 & \\multicolumn{2}{l}{样本编} & \\\\\n\\multicolumn{2}{l}{性} & 别: 男 & \\multicolumn{2}{l}{病人} & \\multicolumn{2}{l}{标本种类: 尿液} & \\multicolumn{2}{l}{标本性状:} & \\\\\n\\multicolumn{2}{l}{年} & 龄: 75岁 & \\multicolumn{2}{l}{住院} & \\multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \\multicolumn{2}{l}{} & \\\\\n\\hline\nNO & 项 & 目 & 结果 & 生物参考区间 & 单位 & NO & 项 & 目 & 结果 \\\\\n\\hline\n1 & 白细胞 & -- & 阴性 & 20 & 电导率 & 16.3 & 3.0-39.0 & mS/cm & \\\\\n2 & 隐血 & -- & 阴性 & 21 & 红细胞信息 & -- & 阴性 & & \\\\\n3 & 蛋白 & -- & 阴性 & & & & & & \\\\\n4 & 葡萄糖 & -- & 阴性 & & & & & & \\\\\n5 & PH & 6.5 & 4.5-8.0 & & & & & & \\\\\n6 & 比重 & 1.016 & 1.003-1.030 & & & & & & \\\\\n7 & 酮体 & -- & 阴性 & & & & & & \\\\\n8 & 胆红素 & -- & 阴性 & & & & & & \\\\\n9 & 尿胆原 & 正常 & 阴性-弱阳性 & & & & & & \\\\\n10 & 亚硝酸盐 & -- & 阴性 & & & & & & \\\\\n11 & 浊度 & 清亮 & & & & & & & \\\\\n12 & 白细胞计数 & 2.4 & 0.0-25.0 & /uL & & & & & \\\\\n13 & 红细胞计数 & 3.2 & 0.0-23.0 & /uL & & & & & \\\\\n14 & 上皮细胞计数 & 0.4 & 0.0-31.0 & /uL & & & & & \\\\\n15 & 管型计数 & 0.0 & 0.0-2.0 & /uL & & & & & \\\\\n16 & 小圆上皮细胞 & 0.4 & 0.0-3.0 & /uL & & & & & \\\\\n17 & 类酵母细胞 & -- & 0.0-0.0 & & & & & & \\\\\n18 & 结晶检查 & 0.0 & 0.0-10.0 & /uL & & & & & \\\\\n19 & 细菌计数 & 8.5 & 0.0-1200.0 & /uL & & & & & \\\\\n\\hline\n\\multicolumn{10}{l}{备注:} \\\\\n\\hline\n\\multicolumn{2}{l}{接收时间: 2026-01-27 08:37} & \\multicolumn{2}{l}{报告时间:} & \\multicolumn{2}{l}{2026-01-27 08:59} & \\multicolumn{4}{l}{检验者:} \\\\\n\\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \\multicolumn{2}{l}{送检医} & \\multicolumn{6}{l}{} \\\\\n\\multicolumn{10}{l}{本报告仅对本次检验标本负责,如对检验结果有疑问,请与相关院区检验科联系!} \\\\\n\\multicolumn{10}{r}{第1页 共1页} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 17:43:20,171 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:20,171 INFO     29 [qwen-vl-table] page=22 LLM output (len=3411):
{
  "report_date": "2026-01-27",
  "items": [
    {
      "name": "白细胞",
      "item_code": null,
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "隐血",
      "item_code": null,
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "蛋白",
      "item_code": null,
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": null,
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "PH",
      "item_code": null,
      "value": "6.5",
      "unit": null,
      "reference_range": "4.5-8.0",
      "abnormal": false
    },
    {
      "name": "比重",
      "item_code": null,
      "value": "1.016",
      "unit": null,
      "reference_range": "1.003-1.030",
      "abnormal": false
    },
    {
      "name": "酮体",
      "item_code": null,
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "胆红素",
      "item_code": null,
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿胆原",
      "item_code": null,
      "value": "正常",
      "unit": null,
      "reference_range": "阴性-弱阳性",
      "abnormal": false
    },
    {
      "name": "亚硝酸盐",
      "item_code": null,
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "浊度",
      "item_code": null,
      "value": "清亮",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "白细胞计数",
      "item_code": null,
      "value": "2.4",
      "unit": "/uL",
      "reference_range": "0.0-25.0",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": null,
      "value": "3.2",
      "unit": "/uL",
      "reference_range": "0.0-23.0",
      "abnormal": false
    },
    {
      "name": "上皮细胞计数",
      "item_code": null,
      "value": "0.4",
      "unit": "/uL",
      "reference_range": "0.0-31.0",
      "abnormal": false
    },
    {
      "name": "管型计数",
      "item_code": null,
      "value": "0.0",
      "unit": "/uL",
      "reference_range": "0.0-2.0",
      "abnormal": false
    },
    {
      "name": "小圆上皮细胞",
      "item_code": null,
      "value": "0.4",
      "unit": "/uL",
      "reference_range": "0.0-3.0",
      "abnormal": false
    },
    {
      "name": "类酵母细胞",
      "item_code": null,
      "value": "--",
      "unit": null,
      "reference_range": "0.0-0.0",
      "abnormal": false
    },
    {
      "name": "结晶检查",
      "item_code": null,
      "value": "0.0",
      "unit": "/uL",
      "reference_range": "0.0-10.0",
      "abnormal": false
    },
    {
      "name": "细菌计数",
      "item_code": null,
      "value": "8.5",
      "unit": "/uL",
      "reference_range": "0.0-1200.0",
      "abnormal": false
    },
    {
      "name": "电导率",
      "item_code": null,
      "value": "16.3",
      "unit": "mS/cm",
      "reference_range": "3.0-39.0",
      "abnormal": false
    },
    {
      "name": "红细胞信息",
      "item_code": null,
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 17:43:20,171 INFO     29 [qwen-vl-table] coord grouping: {22: 21}
2026-08-10 17:43:20,174 INFO     29 [qwen-vl-table] coord API call start, page=22, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1242997, prompt_len=602
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞、隐血、蛋白、葡萄糖、PH、比重、酮体、胆红素、尿胆原、亚硝酸盐、浊度、白细胞计数、红细胞计数、上皮细胞计数、管型计数、小圆上皮细胞、类酵母细胞、结晶检查、细菌计数、电导率、红细胞信息

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
2026-08-10 17:43:28,197 INFO     29 [qwen-vl-table] coord API raw response (len=1003):
[
	{"text": "白细胞", "bbox": [88, 240, 129, 259]},
	{"text": "隐血", "bbox": [88, 267, 115, 287]},
	{"text": "蛋白", "bbox": [88, 295, 115, 315]},
	{"text": "葡萄糖", "bbox": [88, 323, 129, 343]},
	{"text": "PH", "bbox": [88, 352, 102, 370]},
	{"text": "比重", "bbox": [88, 377, 115, 396]},
	{"text": "酮体", "bbox": [88, 403, 115, 423]},
	{"text": "胆红素", "bbox": [88, 431, 129, 450]},
	{"text": "尿胆原", "bbox": [88, 458, 129, 478]},
	{"text": "亚硝酸盐", "bbox": [88, 486, 142, 506]},
	{"text": "浊度", "bbox": [88, 513, 115, 533]},
	{"text": "白细胞计数", "bbox": [88, 540, 155, 560]},
	{"text": "红细胞计数", "bbox": [88, 566, 155, 586]},
	{"text": "上皮细胞计数", "bbox": [88, 593, 169, 613]},
	{"text": "管型计数", "bbox": [88, 619, 142, 639]},
	{"text": "小圆上皮细胞", "bbox": [88, 646, 169, 666]},
	{"text": "类酵母细胞", "bbox": [88, 673, 155, 693]},
	{"text": "结晶检查", "bbox": [88, 698, 142, 718]},
	{"text": "细菌计数", "bbox": [88, 724, 142, 744]},
	{"text": "电导率", "bbox": [497, 240, 538, 259]},
	{"text": "红细胞信息", "bbox": [497, 267, 566, 287]}
]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=8.0s
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[88, 240, 129, 259]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[1]: text=隐血, bbox=[88, 267, 115, 287]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[2]: text=蛋白, bbox=[88, 295, 115, 315]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[3]: text=葡萄糖, bbox=[88, 323, 129, 343]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[4]: text=PH, bbox=[88, 352, 102, 370]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[5]: text=比重, bbox=[88, 377, 115, 396]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[6]: text=酮体, bbox=[88, 403, 115, 423]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[7]: text=胆红素, bbox=[88, 431, 129, 450]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[8]: text=尿胆原, bbox=[88, 458, 129, 478]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[9]: text=亚硝酸盐, bbox=[88, 486, 142, 506]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[10]: text=浊度, bbox=[88, 513, 115, 533]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[11]: text=白细胞计数, bbox=[88, 540, 155, 560]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[12]: text=红细胞计数, bbox=[88, 566, 155, 586]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[13]: text=上皮细胞计数, bbox=[88, 593, 169, 613]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[14]: text=管型计数, bbox=[88, 619, 142, 639]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[15]: text=小圆上皮细胞, bbox=[88, 646, 169, 666]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[16]: text=类酵母细胞, bbox=[88, 673, 155, 693]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[17]: text=结晶检查, bbox=[88, 698, 142, 718]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[18]: text=细菌计数, bbox=[88, 724, 142, 744]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[19]: text=电导率, bbox=[497, 240, 538, 259]
2026-08-10 17:43:28,198 INFO     29 [qwen-vl-table] coord item[20]: text=红细胞信息, bbox=[497, 267, 566, 287]
2026-08-10 17:43:28,199 INFO     29 [qwen-vl-table] page=22 coord: matched 21/21, time=8.0s
2026-08-10 17:43:28,199 INFO     29 [qwen-vl-table] new_positions (21):
[[23, 74.096, 108.618, 142.79999999999998, 154.105], [23, 74.096, 96.83, 158.86499999999998, 170.765], [23, 74.096, 96.83, 175.525, 187.42499999999998], [23, 74.096, 108.618, 192.185, 204.08499999999998], [23, 74.096, 85.884, 209.44, 220.14999999999998], [23, 74.096, 96.83, 224.315, 235.61999999999998], [23, 74.096, 96.83, 239.785, 251.685], [23, 74.096, 108.618, 256.445, 267.75], [23, 74.096, 108.618, 272.51, 284.40999999999997], [23, 74.096, 119.564, 289.16999999999996, 301.07], [23, 74.096, 96.83, 305.235, 317.135], [23, 74.096, 130.51, 321.3, 333.2], [23, 74.096, 130.51, 336.77, 348.66999999999996], [23, 74.096, 142.298, 352.835, 364.73499999999996], [23, 74.096, 119.564, 368.305, 380.205], [23, 74.096, 142.298, 384.37, 396.27], [23, 74.096, 130.51, 400.435, 412.335], [23, 74.096, 119.564, 415.31, 427.21], [23, 74.096, 119.564, 430.78, 442.68], [23, 418.474, 452.996, 142.79999999999998, 154.105], [23, 418.474, 476.572, 158.86499999999998, 170.765]]
2026-08-10 17:43:28,199 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=18.2s
2026-08-10 17:43:28,200 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:43:28,202 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:43:28,202 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[23]
2026-08-10 17:43:28,202 INFO     29 [qwen-vl-table] positions ： [[23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:43:28,342 INFO     29 [qwen-vl-table] page=23, rect=842x595, img=(2339x1653)
2026-08-10 17:43:28,342 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:28,342 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 4152, \"bbox_end\": 4182, \"encounter_dates\": [\"2026-01-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-01-27\n\\hline\n\\multicolumn{2}{l}{质评合格,省内参考} & \\multicolumn{4}{c}{\\textbf{检验报告}} & \\multicolumn{2}{r}{采集时间:} \\\\\n\\multicolumn{2}{l}{住院} & \\multicolumn{4}{c}{} & \\multicolumn{2}{r}{2026-01-27 05:46} \\\\\n\\multicolumn{2}{l}{D-二聚体,血浆抗凝血酶AT} & \\multicolumn{4}{c}{} & \\multicolumn{2}{r}{采集} \\\\\n\\hline\n\\multicolumn{1}{l}{姓} & \\multicolumn{1}{l}{名} & \\multicolumn{1}{l}{别} & \\multicolumn{1}{l}{床} & \\multicolumn{1}{l}{号.} & \\multicolumn{1}{l}{样本编} & \\multicolumn{2}{l}{} \\\\\n\\multicolumn{1}{l}{性} & \\multicolumn{1}{l}{} & \\multicolumn{1}{l}{ID:} & \\multicolumn{1}{l}{标本种类:} & \\multicolumn{1}{l}{血浆} & \\multicolumn{1}{l}{标本性状.} & \\multicolumn{2}{l}{} \\\\\n\\multicolumn{1}{l}{年} & \\multicolumn{1}{l}{龄: 75岁} & \\multicolumn{1}{l}{号} & \\multicolumn{1}{l}{临床诊断:} & \\multicolumn{1}{l}{肺恶性肿瘤} & \\multicolumn{2}{l}{} & \\multicolumn{1}{l}{} \\\\\n\\hline\n\\textbf{项} & \\textbf{目} & \\textbf{中} & \\textbf{不} & \\textbf{提示} & \\textbf{生物参考区间} & \\textbf{单位} & \\\\\n\\hline\n1 & 凝血酶原时间 & 13.2 & & & 10.0-14.0 & sec & \\\\\n2 & PT-国际标准化比值 & 1.13 & & & 0.80-1.20 & INR & \\\\\n3 & PT百分活度 & 84 & & & 80-200 & \\% & \\\\\n4 & 活化部分凝血活酶时间 & 31.8 & & & 22.0-38.0 & sec & \\\\\n5 & APTT比值 & 1.12 & & & 0.73-1.27 & R & \\\\\n6 & 凝血酶时间 & 18.1 & & & 14.0-21.0 & sec & \\\\\n7 & TT比值 & 1.06 & & & 0.82-1.23 & R & \\\\\n8 & 纤维蛋白原 & 5.80 & $\\uparrow$ & & 2.0-4.0 & g/L & \\\\\n9 & 抗凝血酶III & 96 & & & 82-121 & \\% & \\\\\n10 & D-二聚体测定 & 550 & $\\uparrow$ & & 0-500 & ng/ml & \\\\\n\\hline\n\\multicolumn{8}{l}{备注:} \\\\\n\\hline\n\\multicolumn{2}{l}{接收时间: 2026-01-27 07:13} & \\multicolumn{2}{l}{报告时间: 2026-01-27 11:05} & \\multicolumn{2}{l}{检验者:} & \\multicolumn{2}{l}{审核者:} \\\\\n\\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \\multicolumn{2}{l}{送检医} & \\multicolumn{4}{l}{} \\\\\n\\multicolumn{8}{l}{本报告仅对本次检验标本负责,如对检验结} & \\multicolumn{4}{l}{\\textbf{第1页 共1页}} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 17:43:32,291 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:43:32.289+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:43:34,482 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:34,482 INFO     29 [qwen-vl-table] page=23 LLM output (len=1711):
{
  "report_date": "2026-01-27",
  "items": [
    {
      "name": "凝血酶原时间",
      "item_code": null,
      "value": "13.2",
      "unit": "sec",
      "reference_range": "10.0-14.0",
      "abnormal": false
    },
    {
      "name": "PT-国际标准化比值",
      "item_code": null,
      "value": "1.13",
      "unit": "INR",
      "reference_range": "0.80-1.20",
      "abnormal": false
    },
    {
      "name": "PT百分活度",
      "item_code": null,
      "value": "84",
      "unit": "%",
      "reference_range": "80-200",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间",
      "item_code": null,
      "value": "31.8",
      "unit": "sec",
      "reference_range": "22.0-38.0",
      "abnormal": false
    },
    {
      "name": "APTT比值",
      "item_code": null,
      "value": "1.12",
      "unit": "R",
      "reference_range": "0.73-1.27",
      "abnormal": false
    },
    {
      "name": "凝血酶时间",
      "item_code": null,
      "value": "18.1",
      "unit": "sec",
      "reference_range": "14.0-21.0",
      "abnormal": false
    },
    {
      "name": "TT比值",
      "item_code": null,
      "value": "1.06",
      "unit": "R",
      "reference_range": "0.82-1.23",
      "abnormal": false
    },
    {
      "name": "纤维蛋白原",
      "item_code": null,
      "value": "5.80",
      "unit": "g/L",
      "reference_range": "2.0-4.0",
      "abnormal": true
    },
    {
      "name": "抗凝血酶III",
      "item_code": null,
      "value": "96",
      "unit": "%",
      "reference_range": "82-121",
      "abnormal": false
    },
    {
      "name": "D-二聚体测定",
      "item_code": null,
      "value": "550",
      "unit": "ng/ml",
      "reference_range": "0-500",
      "abnormal": true
    }
  ]
}
2026-08-10 17:43:34,483 INFO     29 [qwen-vl-table] coord grouping: {23: 10}
2026-08-10 17:43:34,487 INFO     29 [qwen-vl-table] coord API call start, page=23, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=996641, prompt_len=582
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间、PT-国际标准化比值、PT百分活度、活化部分凝血活酶时间、APTT比值、凝血酶时间、TT比值、纤维蛋白原、抗凝血酶III、D-二聚体测定

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
2026-08-10 17:43:37,937 INFO     29 [qwen-vl-table] coord API raw response (len=520):
```json
[
	{"text": "凝血酶原时间", "bbox": [90, 250, 176, 270]},
	{"text": "PT-国际标准化比值", "bbox": [90, 277, 211, 298]},
	{"text": "PT百分活度", "bbox": [90, 305, 162, 325]},
	{"text": "活化部分凝血活酶时间", "bbox": [90, 332, 232, 352]},
	{"text": "APTT比值", "bbox": [90, 360, 148, 380]},
	{"text": "凝血酶时间", "bbox": [90, 387, 162, 407]},
	{"text": "TT比值", "bbox": [90, 413, 134, 433]},
	{"text": "纤维蛋白原", "bbox": [90, 440, 162, 460]},
	{"text": "抗凝血酶III", "bbox": [90, 467, 162, 487]},
	{"text": "D-二聚体测定", "bbox": [70, 494, 176, 514]}
]
```
2026-08-10 17:43:37,937 INFO     29 [qwen-vl-table] coord API: raw_items=10, valid_items=10, elapsed=3.5s
2026-08-10 17:43:37,937 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[90, 250, 176, 270]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[1]: text=PT-国际标准化比值, bbox=[90, 277, 211, 298]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[2]: text=PT百分活度, bbox=[90, 305, 162, 325]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间, bbox=[90, 332, 232, 352]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[4]: text=APTT比值, bbox=[90, 360, 148, 380]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[5]: text=凝血酶时间, bbox=[90, 387, 162, 407]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[6]: text=TT比值, bbox=[90, 413, 134, 433]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[7]: text=纤维蛋白原, bbox=[90, 440, 162, 460]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[8]: text=抗凝血酶III, bbox=[90, 467, 162, 487]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] coord item[9]: text=D-二聚体测定, bbox=[70, 494, 176, 514]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] page=23 coord: matched 10/10, time=3.5s
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] new_positions (10):
[[24, 75.78, 148.192, 148.75, 160.65], [24, 75.78, 177.662, 164.815, 177.31], [24, 75.78, 136.404, 181.475, 193.375], [24, 75.78, 195.344, 197.54, 209.44], [24, 75.78, 124.616, 214.2, 226.1], [24, 75.78, 136.404, 230.265, 242.165], [24, 75.78, 112.828, 245.73499999999999, 257.635], [24, 75.78, 136.404, 261.8, 273.7], [24, 75.78, 136.404, 277.865, 289.765], [24, 58.94, 148.192, 293.93, 305.83]]
2026-08-10 17:43:37,938 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=10, matched=10, pages=1, time=9.7s
2026-08-10 17:43:37,938 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:43:37,939 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:43:37,940 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[24]
2026-08-10 17:43:37,940 INFO     29 [qwen-vl-table] positions ： [[24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:43:38,091 INFO     29 [qwen-vl-table] page=24, rect=842x595, img=(2339x1653)
2026-08-10 17:43:38,092 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:38,092 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 4183, \"bbox_end\": 4193, \"encounter_dates\": [\"2026-01-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{lllllll}\n报告时间: 2026-01-27\n\\hline\n项 & 目 & 结果 & 提示 & 生物参考区间 & 单位 \\\\\n\\hline\n1 & 乙型肝炎表面抗原(化学发光法) & 0.00 & 阴性 & $<$0.05 & IU/ml \\\\\n2 & 丙型肝炎抗体 & 0.07 & 阴性 & $<$1 & S/CO \\\\\n3 & HIV抗体/p24抗原 & 0.13 & 阴性 & $<$1.00 & S/CO \\\\\n4 & 梅毒螺旋体抗体 & 0.08 & 无反应 & $<$1.00 & S/CO \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 17:43:40,531 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:40,531 INFO     29 [qwen-vl-table] page=24 LLM output (len=723):
{
  "report_date": "2026-01-27",
  "items": [
    {
      "name": "乙型肝炎表面抗原(化学发光法)",
      "item_code": null,
      "value": "0.00",
      "unit": "IU/ml",
      "reference_range": "<0.05",
      "abnormal": false
    },
    {
      "name": "丙型肝炎抗体",
      "item_code": null,
      "value": "0.07",
      "unit": "S/CO",
      "reference_range": "<1",
      "abnormal": false
    },
    {
      "name": "HIV抗体/p24抗原",
      "item_code": null,
      "value": "0.13",
      "unit": "S/CO",
      "reference_range": "<1.00",
      "abnormal": false
    },
    {
      "name": "梅毒螺旋体抗体",
      "item_code": null,
      "value": "0.08",
      "unit": "S/CO",
      "reference_range": "<1.00",
      "abnormal": false
    }
  ]
}
2026-08-10 17:43:40,531 INFO     29 [qwen-vl-table] coord grouping: {24: 4}
2026-08-10 17:43:40,533 INFO     29 [qwen-vl-table] coord API call start, page=24, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1200138, prompt_len=549
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
乙型肝炎表面抗原(化学发光法)、丙型肝炎抗体、HIV抗体/p24抗原、梅毒螺旋体抗体

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
2026-08-10 17:43:42,882 INFO     29 [qwen-vl-table] coord API raw response (len=264):
```json
[
	{"text": "乙型肝炎表面抗原(化学发光法)", "bbox": [100, 270, 295, 293]},
	{"text": "丙型肝炎抗体", "bbox": [100, 303, 185, 325],
	"bbox": [100, 334, 205, 356]},
	{"text": "HIV抗体/p24抗原", "bbox": [100, 367, 205, 389]},
	{"text": "梅毒螺旋体抗体", "bbox": [100, 399, 205, 421]}
]
```
2026-08-10 17:43:42,882 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=2.3s
2026-08-10 17:43:42,882 INFO     29 [qwen-vl-table] coord item[0]: text=乙型肝炎表面抗原(化学发光法), bbox=[100, 270, 295, 293]
2026-08-10 17:43:42,882 INFO     29 [qwen-vl-table] coord item[1]: text=丙型肝炎抗体, bbox=[100, 334, 205, 356]
2026-08-10 17:43:42,882 INFO     29 [qwen-vl-table] coord item[2]: text=HIV抗体/p24抗原, bbox=[100, 367, 205, 389]
2026-08-10 17:43:42,882 INFO     29 [qwen-vl-table] coord item[3]: text=梅毒螺旋体抗体, bbox=[100, 399, 205, 421]
2026-08-10 17:43:42,882 INFO     29 [qwen-vl-table] page=24 coord: matched 4/4, time=2.3s
2026-08-10 17:43:42,883 INFO     29 [qwen-vl-table] new_positions (4):
[[25, 84.2, 248.39, 160.65, 174.33499999999998], [25, 84.2, 172.60999999999999, 198.73, 211.82], [25, 84.2, 172.60999999999999, 218.36499999999998, 231.45499999999998], [25, 84.2, 172.60999999999999, 237.405, 250.49499999999998]]
2026-08-10 17:43:42,883 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=4, matched=4, pages=1, time=4.9s
2026-08-10 17:43:42,884 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:43:42,885 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:43:42,885 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[25]
2026-08-10 17:43:42,885 INFO     29 [qwen-vl-table] positions ： [[25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:43:43,026 INFO     29 [qwen-vl-table] page=25, rect=842x595, img=(2339x1653)
2026-08-10 17:43:43,026 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:43,027 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 4194, \"bbox_end\": 4228, \"encounter_dates\": [\"2026-01-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-01-27\n\\hline\n\\multicolumn{2}{l}{质评合格,省内参考} & \\multicolumn{6}{r}{采集时间:} \\\\\n\\multicolumn{2}{l}{住院} & \\multicolumn{6}{r}{2026-01-27 05:46} \\\\\n\\multicolumn{2}{l}{F-PSA, CA72-4, CA19-9, $\\beta$-h} & \\multicolumn{6}{r}{采} \\\\\n\\multicolumn{2}{l}{\\textbf{检验报告}} & \\multicolumn{6}{r}{} \\\\\n\\hline\n\\multicolumn{2}{l}{姓} & 男 & \\multicolumn{2}{l}{床号: 55} & \\multicolumn{3}{l}{样本} \\\\\n\\multicolumn{2}{l}{性} & 人 IP & \\multicolumn{2}{l}{标本种类: 血清} & \\multicolumn{3}{l}{标本} \\\\\n\\multicolumn{2}{l}{年} & 龄: 75岁 & \\multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \\multicolumn{3}{l}{} \\\\\n\\hline\n\\multicolumn{2}{l}{\\textbf{项}} & \\textbf{目} & \\textbf{不} & \\textbf{提示} & \\textbf{生物参考区间} & \\textbf{单位} \\\\\n\\hline\n1 & 癌胚抗原 & 9.21 & $\\uparrow$ & 0-5.0 & ng/ml & \\\\\n2 & 甲胎蛋白 & 1.64 & & 0-7.00 & ng/ml & \\\\\n3 & 糖类抗原72-4 & 2.08 & & 0-6.9 & U/ml & \\\\\n4 & 神经元特异性烯醇化酶 & 22.47 & $\\uparrow$ & 0-17 & ng/ml & \\\\\n5 & 细胞角蛋白19片段 & 5.70 & $\\uparrow$ & 0-3.3 & ng/ml & \\\\\n6 & 鳞状细胞癌相关抗原 & 2.97 & $\\uparrow$ & 0-2.5 & ng/ml & \\\\\n7 & 胃泌素释放肽前体 & 37.68 & & 0-68.3 & pg/mL & \\\\\n8 & 总前列腺特异性抗原 & 4.820 & $\\uparrow$ & 0-4 & ng/ml & \\\\\n9 & 游离前列腺特异性抗原 & 0.767 & & 0-0.93 & ng/ml & \\\\\n10 & FPSA/TPSA & 0.159 & & $>$0.15 & & \\\\\n11 & 特异$\\beta$人绒毛膜促性腺激素 & 5.86 & $\\uparrow$ & 0-2.6 & mIU/ml & \\\\\n12 & 糖类抗原19-9 & 27.60 & & 0-30 & U/ml & \\\\\n\\hline\n\\multicolumn{8}{l}{备注:} \\\\\n\\hline\n\\multicolumn{2}{l}{接收时间: 2026-01-27 06:57} & \\multicolumn{2}{l}{报告时间: 2026-01-27 10:21} & \\multicolumn{2}{l}{检验者:} & \\multicolumn{2}{l}{审核者:} \\\\\n\\multicolumn{2}{l}{开单时间: 2026-01-26 11:06} & \\multicolumn{2}{l}{送检医生:} & \\multicolumn{4}{l}{} \\\\\n\\multicolumn{8}{l}{本报告仅对本次检验标本负责, 如对检验结果有疑问, 请在3个工作日内与相关院区检验科联系!} \\\\\n\\multicolumn{8}{r}{第1页 共1页} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 17:43:49,743 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:49,743 INFO     29 [qwen-vl-table] page=25 LLM output (len=2065):
{
  "report_date": "2026-01-27",
  "items": [
    {
      "name": "癌胚抗原",
      "item_code": null,
      "value": "9.21",
      "unit": "ng/ml",
      "reference_range": "0-5.0",
      "abnormal": true
    },
    {
      "name": "甲胎蛋白",
      "item_code": null,
      "value": "1.64",
      "unit": "ng/ml",
      "reference_range": "0-7.00",
      "abnormal": false
    },
    {
      "name": "糖类抗原72-4",
      "item_code": null,
      "value": "2.08",
      "unit": "U/ml",
      "reference_range": "0-6.9",
      "abnormal": false
    },
    {
      "name": "神经元特异性烯醇化酶",
      "item_code": null,
      "value": "22.47",
      "unit": "ng/ml",
      "reference_range": "0-17",
      "abnormal": true
    },
    {
      "name": "细胞角蛋白19片段",
      "item_code": null,
      "value": "5.70",
      "unit": "ng/ml",
      "reference_range": "0-3.3",
      "abnormal": true
    },
    {
      "name": "鳞状细胞癌相关抗原",
      "item_code": null,
      "value": "2.97",
      "unit": "ng/ml",
      "reference_range": "0-2.5",
      "abnormal": true
    },
    {
      "name": "胃泌素释放肽前体",
      "item_code": null,
      "value": "37.68",
      "unit": "pg/mL",
      "reference_range": "0-68.3",
      "abnormal": false
    },
    {
      "name": "总前列腺特异性抗原",
      "item_code": null,
      "value": "4.820",
      "unit": "ng/ml",
      "reference_range": "0-4",
      "abnormal": true
    },
    {
      "name": "游离前列腺特异性抗原",
      "item_code": null,
      "value": "0.767",
      "unit": "ng/ml",
      "reference_range": "0-0.93",
      "abnormal": false
    },
    {
      "name": "FPSA/TPSA",
      "item_code": null,
      "value": "0.159",
      "unit": null,
      "reference_range": ">0.15",
      "abnormal": false
    },
    {
      "name": "特异β人绒毛膜促性腺激素",
      "item_code": null,
      "value": "5.86",
      "unit": "mIU/ml",
      "reference_range": "0-2.6",
      "abnormal": true
    },
    {
      "name": "糖类抗原19-9",
      "item_code": null,
      "value": "27.60",
      "unit": "U/ml",
      "reference_range": "0-30",
      "abnormal": false
    }
  ]
}
2026-08-10 17:43:49,743 INFO     29 [qwen-vl-table] coord grouping: {25: 12}
2026-08-10 17:43:49,748 INFO     29 [qwen-vl-table] coord API call start, page=25, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1055414, prompt_len=618
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
癌胚抗原、甲胎蛋白、糖类抗原72-4、神经元特异性烯醇化酶、细胞角蛋白19片段、鳞状细胞癌相关抗原、胃泌素释放肽前体、总前列腺特异性抗原、游离前列腺特异性抗原、FPSA/TPSA、特异β人绒毛膜促性腺激素、糖类抗原19-9

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
2026-08-10 17:43:53,886 INFO     29 [qwen-vl-table] coord API raw response (len=630):
[
	{"text": "癌胚抗原", "bbox": [95, 247, 151, 269]},
	{"text": "甲胎蛋白", "bbox": [95, 274, 151, 296]},
	{"text": "糖类抗原72-4", "bbox": [95, 302, 178, 323]},
	{"text": "神经元特异性烯醇化酶", "bbox": [95, 329, 233, 351]},
	{"text": "细胞角蛋白19片段", "bbox": [95, 357, 205, 378]},
	{"text": "鳞状细胞癌相关抗原", "bbox": [95, 384, 218, 405]},
	{"text": "胃泌素释放肽前体", "bbox": [95, 411, 205, 433]},
	{"text": "总前列腺特异性抗原", "bbox": [95, 439, 218, 460]},
	{"text": "游离前列腺特异性抗原", "bbox": [95, 466, 233, 487]},
	{"text": "FPSA/TPSA", "bbox": [95, 493, 157, 514]},
	{"text": "特异β人绒毛膜促性腺激素", "bbox": [95, 518, 261, 539]},
	{"text": "糖类抗原19-9", "bbox": [95, 545, 176, 566]}
]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord API: raw_items=12, valid_items=12, elapsed=4.1s
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[0]: text=癌胚抗原, bbox=[95, 247, 151, 269]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[1]: text=甲胎蛋白, bbox=[95, 274, 151, 296]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[2]: text=糖类抗原72-4, bbox=[95, 302, 178, 323]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[3]: text=神经元特异性烯醇化酶, bbox=[95, 329, 233, 351]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[4]: text=细胞角蛋白19片段, bbox=[95, 357, 205, 378]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[5]: text=鳞状细胞癌相关抗原, bbox=[95, 384, 218, 405]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[6]: text=胃泌素释放肽前体, bbox=[95, 411, 205, 433]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[7]: text=总前列腺特异性抗原, bbox=[95, 439, 218, 460]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[8]: text=游离前列腺特异性抗原, bbox=[95, 466, 233, 487]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[9]: text=FPSA/TPSA, bbox=[95, 493, 157, 514]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[10]: text=特异β人绒毛膜促性腺激素, bbox=[95, 518, 261, 539]
2026-08-10 17:43:53,887 INFO     29 [qwen-vl-table] coord item[11]: text=糖类抗原19-9, bbox=[95, 545, 176, 566]
2026-08-10 17:43:53,888 INFO     29 [qwen-vl-table] page=25 coord: matched 12/12, time=4.1s
2026-08-10 17:43:53,888 INFO     29 [qwen-vl-table] new_positions (12):
[[26, 79.99, 127.142, 146.965, 160.055], [26, 79.99, 127.142, 163.03, 176.12], [26, 79.99, 149.876, 179.69, 192.185], [26, 79.99, 196.186, 195.755, 208.845], [26, 79.99, 172.60999999999999, 212.415, 224.91], [26, 79.99, 183.55599999999998, 228.48, 240.975], [26, 79.99, 172.60999999999999, 244.545, 257.635], [26, 79.99, 183.55599999999998, 261.205, 273.7], [26, 79.99, 196.186, 277.27, 289.765], [26, 79.99, 132.194, 293.335, 305.83], [26, 79.99, 219.762, 308.21, 320.705], [26, 79.99, 148.192, 324.275, 336.77]]
2026-08-10 17:43:53,888 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=12, matched=12, pages=1, time=11.0s
2026-08-10 17:43:53,902 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 17:43:53,902 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:LabExam | outputs={"chunks": "5 items, types={'LabReport': 5}", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:43:53,902 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 17:43:53,909 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:53,910 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:43:54,728 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:54,737 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 17:43:54,738 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:43:54,738 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 17:43:54,747 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:43:54,748 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:43:54,748 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 17:43:54,748 INFO     29 [qwen-vl-text] positions(32): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:43:54,749 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [32]
2026-08-10 17:43:55,728 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:43:55,728 INFO     29 [qwen-vl-text] LLM extraction start, text_len=518
2026-08-10 17:43:55,729 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:55,730 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 164, \"bbox_end\": 195, \"encounter_dates\": [\"2026-02-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门（急）诊病历\n初诊\n科室\n日期:2026-02-02 09:07\n医学\n性别:男\n年龄:75岁\n出生日期:1950-09-13\n主诉:肺癌靶向治疗5年复查。\n现病史:肺癌吉非替尼治疗3个月,因肝功异常更换泰瑞沙靶向治疗至今5年,外院肺CT提示病灶增大\n既往史:无肺结核病史。\n个人史:无不良嗜好。\n家族史:无遗传病史。\n体 检:双肺呼吸音清,未闻及干湿性啰音。\n辅助检查:2026-01-30 组织病理学检查与诊断[免费用](左肺组织穿刺活检)非小细胞肺癌伴大片坏死,\n结合形态学及免疫组化,符合腺癌。免疫组化示肿瘤细胞:CKpan(+),CK7(+),TTF-\n1(+),p40(-),CK5/6(-);特殊染色:D-PAS(-)。\n初步诊断:肺恶性肿瘤\n诊疗计划:分子病理检测\n甲磺酸奥希替尼片(泰瑞沙2)(80mg*30),剂量:80MG,用法:口服,频率:每日1次,疗程:1天,\n温馨提示:此病历只打印一次,请妥善保管!\n第1页 共2页\n打印时间:2026-03-02 12:50:46\n门（急）诊病历\n初诊\n科\n日期:2026-02-02 09:07\n姓名\n性别:男\n年龄:75岁\n出生日期:1950-09-13\n医师签名：",
    "role": "user"
  }
]
2026-08-10 17:43:58,632 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:43:58,632 INFO     29 [qwen-vl-text] LLM output (len=275):
{
  "encounter_date": "2026-02-02",
  "chief_complaint": "肺癌靶向治疗5年复查。",
  "present_illness": "肺癌吉非替尼治疗3个月,因肝功异常更换泰瑞沙靶向治疗至今5年,外院肺CT提示病灶增大",
  "past_history": "无肺结核病史。",
  "diagnosis": "肺恶性肿瘤",
  "treatment_plan": "分子病理检测\n甲磺酸奥希替尼片(泰瑞沙2)(80mg*30),剂量:80MG,用法:口服,频率:每日1次,疗程:1天"
}
2026-08-10 17:43:58,633 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-02]
2026-08-10 17:43:58,634 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1119507, prompt_len=1227
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["门（急）诊病历", "初诊", "科室", "日期:2026-02-02 09:07", "医学", "性别:男", "年龄:75岁", "出生日期:1950-09-13", "主诉:肺癌靶向治疗5年复查。", "现病史:肺癌吉非替尼治疗3个月,因肝功异常更换泰瑞沙靶向治疗至今5年,外院肺CT提示病灶增大", "既往史:无肺结核病史。", "个人史:无不良嗜好。", "家族史:无遗传病史。", "体 检:双肺呼吸音清,未闻及干湿性啰音。", "辅助检查:2026-01-30 组织病理学检查与诊断[免费用](左肺组织穿刺活检)非小细胞肺癌伴大片坏死,", "结合形态学及免疫组化,符合腺癌。免疫组化示肿瘤细胞:CKpan(+),CK7(+),TTF-", "1(+),p40(-),CK5/6(-);特殊染色:D-PAS(-)。", "初步诊断:肺恶性肿瘤", "诊疗计划:分子病理检测", "甲磺酸奥希替尼片(泰瑞沙2)(80mg*30),剂量:80MG,用法:口服,频率:每日1次,疗程:1天,", "温馨提示:此病历只打印一次,请妥善保管!", "第1页 共2页", "打印时间:2026-03-02 12:50:46", "门（急）诊病历", "初诊", "科", "日期:2026-02-02 09:07", "姓名", "性别:男", "年龄:75岁", "出生日期:1950-09-13", "医师签名："]

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
2026-08-10 17:44:08,885 INFO     29 [qwen-vl-text] coord API raw response (len=1911):
[
	{"text": "门（急）诊病历", "bbox": [429, 100, 573, 116]},
	{"text": "初诊", "bbox": [667, 102, 699, 114]},
	{"text": "科室", "bbox": [26, 128, 67, 143]},
	{"text": "日期:2026-02-02 09:07", "bbox": [694, 128, 918, 143]},
	{"text": "医学", "bbox": [27, 150, 85, 165]},
	{"text": "性别:男", "bbox": [270, 172, 362, 188]},
	{"text": "年龄:75岁", "bbox": [463, 172, 553, 188]},
	{"text": "出生日期:1950-09-13", "bbox": [667, 172, 860, 188]},
	{"text": "主诉:肺癌靶向治疗5年复查。", "bbox": [25, 220, 328, 236]},
	{"text": "现病史:肺癌吉非替尼治疗3个月,因肝功异常更换泰瑞沙靶向治疗至今5年,外院肺CT提示病灶增大", "bbox": [25, 241, 933, 258]},
	{"text": "既往史:无肺结核病史。", "bbox": [25, 264, 257, 280]},
	{"text": "个人史:无不良嗜好。", "bbox": [25, 285, 239, 301]},
	{"text": "家族史:无遗传病史。", "bbox": [25, 307, 239, 323]},
	{"text": "体 检:双肺呼吸音清,未闻及干湿性啰音。", "bbox": [25, 329, 441, 345]},
	{"text": "辅助检查:2026-01-30 组织病理学检查与诊断[免费用](左肺组织穿刺活检)非小细胞肺癌伴大片坏死,", "bbox": [25, 350, 958, 367]},
	{"text": "结合形态学及免疫组化,符合腺癌。免疫组化示肿瘤细胞:CKpan(+),CK7(+),TTF-", "bbox": [125, 372, 967, 388]},
	{"text": "1(+),p40(-),CK5/6(-);特殊染色:D-PAS(-)。", "bbox": [125, 393, 640, 409]},
	{"text": "初步诊断:肺恶性肿瘤", "bbox": [25, 415, 223, 431]},
	{"text": "诊疗计划:分子病理检测", "bbox": [25, 437, 245, 453]},
	{"text": "甲磺酸奥希替尼片(泰瑞沙2)(80mg*30),剂量:80MG,用法:口服,频率:每日1次,疗程:1天,", "bbox": [125, 458, 964, 474]},
	{"text": "温馨提示:此病历只打印一次,请妥善保管!", "bbox": [98, 503, 401, 517]},
	{"text": "第1页 共2页", "bbox": [470, 501, 580, 517]},
	{"text": "打印时间:2026-03-02 12:50:46", "bbox": [651, 503, 947, 517]},
	{"text": "门（急）诊病历", "bbox": [427, 613, 569, 630]},
	{"text": "初诊", "bbox": [663, 615, 695, 627]},
	{"text": "科", "bbox": [25, 638, 55, 654]},
	{"text": "日期:2026-02-02 09:07", "bbox": [707, 640, 917, 656]},
	{"text": "姓名", "bbox": [25, 685, 67, 701]},
	{"text": "性别:男", "bbox": [267, 686, 359, 702]},
	{"text": "年龄:75岁", "bbox": [459, 686, 550, 702]},
	{"text": "出生日期:1950-09-13", "bbox": [663, 687, 858, 703]},
	{"text": "医师签名：", "bbox": [475, 784, 566, 800]}
]
2026-08-10 17:44:08,885 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=10.3s
2026-08-10 17:44:08,885 INFO     29 [qwen-vl-text] coord item[0]: text=门（急）诊病历, bbox=[429, 100, 573, 116]
2026-08-10 17:44:08,885 INFO     29 [qwen-vl-text] coord item[1]: text=初诊, bbox=[667, 102, 699, 114]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[2]: text=科室, bbox=[26, 128, 67, 143]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[3]: text=日期:2026-02-02 09:07, bbox=[694, 128, 918, 143]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[4]: text=医学, bbox=[27, 150, 85, 165]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[270, 172, 362, 188]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:75岁, bbox=[463, 172, 553, 188]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[7]: text=出生日期:1950-09-13, bbox=[667, 172, 860, 188]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[8]: text=主诉:肺癌靶向治疗5年复查。, bbox=[25, 220, 328, 236]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[9]: text=现病史:肺癌吉非替尼治疗3个月,因肝功异常更换泰瑞沙靶向治疗至今5年,外院肺CT提示病灶增大, bbox=[25, 241, 933, 258]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[10]: text=既往史:无肺结核病史。, bbox=[25, 264, 257, 280]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[11]: text=个人史:无不良嗜好。, bbox=[25, 285, 239, 301]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[12]: text=家族史:无遗传病史。, bbox=[25, 307, 239, 323]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[13]: text=体 检:双肺呼吸音清,未闻及干湿性啰音。, bbox=[25, 329, 441, 345]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[14]: text=辅助检查:2026-01-30 组织病理学检查与诊断[免费用](左肺组织穿刺活检)非小细胞肺癌伴大片坏死,, bbox=[25, 350, 958, 367]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[15]: text=结合形态学及免疫组化,符合腺癌。免疫组化示肿瘤细胞:CKpan(+),CK7(+),TTF-, bbox=[125, 372, 967, 388]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[16]: text=1(+),p40(-),CK5/6(-);特殊染色:D-PAS(-)。, bbox=[125, 393, 640, 409]
2026-08-10 17:44:08,886 INFO     29 [qwen-vl-text] coord item[17]: text=初步诊断:肺恶性肿瘤, bbox=[25, 415, 223, 431]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[18]: text=诊疗计划:分子病理检测, bbox=[25, 437, 245, 453]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[19]: text=甲磺酸奥希替尼片(泰瑞沙2)(80mg*30),剂量:80MG,用法:口服,频率:每日1次,疗程:1天,, bbox=[125, 458, 964, 474]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[20]: text=温馨提示:此病历只打印一次,请妥善保管!, bbox=[98, 503, 401, 517]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[21]: text=第1页 共2页, bbox=[470, 501, 580, 517]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[22]: text=打印时间:2026-03-02 12:50:46, bbox=[651, 503, 947, 517]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[23]: text=门（急）诊病历, bbox=[427, 613, 569, 630]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[24]: text=初诊, bbox=[663, 615, 695, 627]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[25]: text=科, bbox=[25, 638, 55, 654]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[26]: text=日期:2026-02-02 09:07, bbox=[707, 640, 917, 656]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[27]: text=姓名, bbox=[25, 685, 67, 701]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[28]: text=性别:男, bbox=[267, 686, 359, 702]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[29]: text=年龄:75岁, bbox=[459, 686, 550, 702]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[30]: text=出生日期:1950-09-13, bbox=[663, 687, 858, 703]
2026-08-10 17:44:08,887 INFO     29 [qwen-vl-text] coord item[31]: text=医师签名：, bbox=[475, 784, 566, 800]
2026-08-10 17:44:08,888 INFO     29 [qwen-vl-text] page=5 — 32/32 coords, api_time=10.3s
2026-08-10 17:44:08,888 INFO     29 [qwen-vl-text] new_positions (32):
[[5, 255.255, 340.935, 84.2, 97.672], [5, 396.865, 415.905, 85.884, 95.988], [5, 15.469999999999999, 39.864999999999995, 107.776, 120.40599999999999], [5, 412.93, 546.2099999999999, 107.776, 120.40599999999999], [5, 16.064999999999998, 50.574999999999996, 126.3, 138.93], [5, 160.65, 215.39, 144.82399999999998, 158.296], [5, 275.485, 329.03499999999997, 144.82399999999998, 158.296], [5, 396.865, 511.7, 144.82399999999998, 158.296], [5, 14.875, 195.16, 185.23999999999998, 198.712], [5, 14.875, 555.135, 202.922, 217.236], [5, 14.875, 152.915, 222.28799999999998, 235.76], [5, 14.875, 142.20499999999998, 239.97, 253.44199999999998], [5, 14.875, 142.20499999999998, 258.49399999999997, 271.966], [5, 14.875, 262.395, 277.018, 290.49], [5, 14.875, 570.01, 294.7, 309.014], [5, 74.375, 575.365, 313.224, 326.69599999999997], [5, 74.375, 380.79999999999995, 330.906, 344.378], [5, 14.875, 132.685, 349.43, 362.902], [5, 14.875, 145.775, 367.954, 381.426], [5, 74.375, 573.5799999999999, 385.63599999999997, 399.108], [5, 58.309999999999995, 238.595, 423.526, 435.31399999999996], [5, 279.65, 345.09999999999997, 421.842, 435.31399999999996], [5, 387.34499999999997, 563.4649999999999, 423.526, 435.31399999999996], [5, 254.065, 338.555, 516.146, 530.46], [5, 394.48499999999996, 413.525, 517.8299999999999, 527.934], [5, 14.875, 32.725, 537.196, 550.668], [5, 420.66499999999996, 545.615, 538.88, 552.352], [5, 14.875, 39.864999999999995, 576.77, 590.242], [5, 158.86499999999998, 213.605, 577.612, 591.084], [5, 273.10499999999996, 327.25, 577.612, 591.084], [5, 394.48499999999996, 510.51, 578.454, 591.9259999999999], [5, 282.625, 336.77, 660.1279999999999, 673.6]]
2026-08-10 17:44:08,888 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=14.1s
2026-08-10 17:44:08,905 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 17:44:08,905 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:44:08,905 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 17:44:08,906 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:44:08.906+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:44:08,915 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:44:08,916 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:44:10,038 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:44:10,047 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 17:44:10,048 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:44:10,048 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 17:44:10,055 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:44:10,055 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:44:10,476 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:44:10,482 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 17:44:10,482 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:44:10,482 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 17:44:10,489 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:44:10,489 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:44:10,489 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 17:44:10,489 INFO     29 [qwen-vl-text] positions(68): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:44:10,490 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [45, 23]
2026-08-10 17:44:10,785 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:44:10,909 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:44:10,909 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1687
2026-08-10 17:44:10,910 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:44:10,911 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 96, \"bbox_end\": 163, \"encounter_dates\": [\"2026-01-26\", \"2026-01-31\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n登记号:\n住院号:\n姓名\n姓名：\n性别：男\n年龄：75岁\n科室·\n入院日期：2026-01-26\n出院日期：2026-01-31\n住院天数：5天\n入院情况：\n，男，75岁，因“确诊肺癌5年，病情进展1月余”于2026-01-\n26入院。患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切\n接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术\n史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。体检：T:\n36.3℃ P:69次/分 R:17次/分 BP:120/66mmHg。神志清，精神可，双肺呼吸音清，未\n闻及干湿性啰音。心脏各瓣膜听诊区未闻及异常杂音。腹软，无压痛，Murphy征阴\n性。双下肢无水肿。病理征阴性。辅助检查：2020-12-21行支气管镜检查，组织病理\n学示：(左侧隆突粘膜)非小细胞肺癌，免疫组化：CK7(+)，TTF-1(+)，\nNapsinA(+)，p40(部分+)，p63(部分+)，CK5/6(+)，ALK-D5F3(-)，ALK-\nD5F3-N(-)，S100(-)，Calponin(-)。结合免疫组化结果，符合腺癌；(左肺\nBALF)细胞蜡块内发现少量恶性肿瘤细胞。\n入院诊断：肺部恶性肿瘤纵隔淋巴结继发恶性肿瘤肺门淋巴结继发恶性肿瘤\n诊疗经过：入院后完善相关检验检查，【检验】血常规(无网红)+CRP：白细胞计数7.\n49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血\n小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原\n测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：\n22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4.\n820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆\n抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血\n试验、传染性标志物4项检测未见异常。【检查】十二通道常规心电图检查：大致正常\n心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性\n可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝\n囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超\n声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复\n查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随\n访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规\n整，请结合临床；【诊疗】入院后给予完善相关检查，排除禁忌后于2026-01-28行CT\n引导下经皮穿刺肺活检术，2026-01-30左肺组织穿刺活检示非小细胞肺癌伴大片坏\n死，结合形态学及免疫组化，符合腺癌。免疫组化示肿瘤细胞：CKpan(+)，\nCK7(+)，TTF-1(+)，p40(-)，CK5/6(-)；特殊染色：D-PAS(-)。现患者诊\n第1页\nCS 扫描全能王\n3亿人都在用的扫描App\n出院记录\n登记号\n住院号\n姓名：\n断明确，拟出院后行基因检测治疗，准予办理出院。\n出院诊断：肺部恶性肿瘤（腺癌 rT4N3MO IVA期）\n纵隔淋巴结继发恶性肿瘤\n肺门淋巴结继发恶性肿瘤\n颈部淋巴结肿大\n脾术后\n慢性胆囊炎\n肝囊肿\n肾结节\n出院情况：患者一般情况可，查体：神志清，双肺呼吸音清，心律齐，腹软，无压痛\n及反跳痛，双下肢无水肿。\n出院医嘱：\n1.注意休息，避免感染、劳累；\n2.出院后分子病理科行基因检测，出院2周待结果回报后于呼吸与危重症医学科门诊就\n诊就诊制定进一步治疗方案；\n3.如有不适或复查指标异常，门急诊及时就诊。\n出院目的地：居家\n患者照护需求：注意休息，避免感染、劳累\n医师签名：",
    "role": "user"
  }
]
2026-08-10 17:44:25,320 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:44:25,320 INFO     29 [qwen-vl-text] LLM output (len=3333):
{
  "encounter_date": "2026-01-31",
  "admission_date": "2026-01-26",
  "discharge_date": "2026-01-31",
  "hospital_days": 5,
  "department": null,
  "bed_number": null,
  "admission_condition": "，男，75岁，因“确诊肺癌5年，病情进展1月余”于2026-01-26入院。患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。体检：T:36.3℃ P:69次/分 R:17次/分 BP:120/66mmHg。神志清，精神可，双肺呼吸音清，未闻及干湿性啰音。心脏各瓣膜听诊区未闻及异常杂音。腹软，无压痛，Murphy征阴性。双下肢无水肿。病理征阴性。",
  "admission_diagnoses": [
    {
      "name": "肺部恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "纵隔淋巴结继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺门淋巴结继发恶性肿瘤",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后完善相关检验检查，【检验】血常规(无网红)+CRP：白细胞计数7.49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4.820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血试验、传染性标志物4项检测未见异常。【检查】十二通道常规心电图检查：大致正常心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规整，请结合临床；【诊疗】入院后给予完善相关检查，排除禁忌后于2026-01-28行CT引导下经皮穿刺肺活检术，2026-01-30左肺组织穿刺活检示非小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合腺癌。免疫组化示肿瘤细胞：CKpan(+)，CK7(+)，TTF-1(+)，p40(-)，CK5/6(-)；特殊染色：D-PAS(-)。现患者诊断明确，拟出院后行基因检测治疗，准予办理出院。",
  "auxiliary_exams": "血常规(无网红)+CRP：白细胞计数7.49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4.820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血试验、传染性标志物4项检测未见异常。",
  "imaging_findings": "十二通道常规心电图检查：大致正常心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规整，请结合临床",
  "discharge_diagnoses": [
    {
      "name": "肺部恶性肿瘤（腺癌 rT4N3MO IVA期）",
      "diagnosis_type": "西医"
    },
    {
      "name": "纵隔淋巴结继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺门淋巴结继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "颈部淋巴结肿大",
      "diagnosis_type": "西医"
    },
    {
      "name": "脾术后",
      "diagnosis_type": "西医"
    },
    {
      "name": "慢性胆囊炎",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医"
    },
    {
      "name": "肾结节",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者一般情况可，查体：神志清，双肺呼吸音清，心律齐，腹软，无压痛及反跳痛，双下肢无水肿。",
  "outcome": null,
  "discharge_orders": "1.注意休息，避免感染、劳累；2.出院后分子病理科行基因检测，出院2周待结果回报后于呼吸与危重症医学科门诊就诊就诊制定进一步治疗方案；3.如有不适或复查指标异常，门急诊及时就诊。",
  "do_medications": [],
  "do_follow_up": "出院2周待结果回报后于呼吸与危重症医学科门诊就诊就诊制定进一步治疗方案",
  "do_precautions": [
    "注意休息，避免感染、劳累",
    "如有不适或复查指标异常，门急诊及时就诊"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": 36.3,
  "vs_pulse_bpm": 69,
  "vs_respiration_rpm": 17,
  "vs_systolic_bp_mmhg": 120,
  "vs_diastolic_bp_mmhg": 66
}
2026-08-10 17:44:25,320 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-31]
2026-08-10 17:44:25,327 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2977722, prompt_len=2130
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共45行）
["出院记录", "登记号:", "住院号:", "姓名", "姓名：", "性别：男", "年龄：75岁", "科室·", "入院日期：2026-01-26", "出院日期：2026-01-31", "住院天数：5天", "入院情况：", "，男，75岁，因“确诊肺癌5年，病情进展1月余”于2026-01-", "26入院。患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切", "接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术", "史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。体检：T:", "36.3℃ P:69次/分 R:17次/分 BP:120/66mmHg。神志清，精神可，双肺呼吸音清，未", "闻及干湿性啰音。心脏各瓣膜听诊区未闻及异常杂音。腹软，无压痛，Murphy征阴", "性。双下肢无水肿。病理征阴性。辅助检查：2020-12-21行支气管镜检查，组织病理", "学示：(左侧隆突粘膜)非小细胞肺癌，免疫组化：CK7(+)，TTF-1(+)，", "NapsinA(+)，p40(部分+)，p63(部分+)，CK5/6(+)，ALK-D5F3(-)，ALK-", "D5F3-N(-)，S100(-)，Calponin(-)。结合免疫组化结果，符合腺癌；(左肺", "BALF)细胞蜡块内发现少量恶性肿瘤细胞。", "入院诊断：肺部恶性肿瘤纵隔淋巴结继发恶性肿瘤肺门淋巴结继发恶性肿瘤", "诊疗经过：入院后完善相关检验检查，【检验】血常规(无网红)+CRP：白细胞计数7.", "49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血", "小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原", "测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：", "22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4.", "820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆", "抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血", "试验、传染性标志物4项检测未见异常。【检查】十二通道常规心电图检查：大致正常", "心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性", "可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝", "囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超", "声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复", "查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随", "访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规", "整，请结合临床；【诊疗】入院后给予完善相关检查，排除禁忌后于2026-01-28行CT", "引导下经皮穿刺肺活检术，2026-01-30左肺组织穿刺活检示非小细胞肺癌伴大片坏", "死，结合形态学及免疫组化，符合腺癌。免疫组化示肿瘤细胞：CKpan(+)，", "CK7(+)，TTF-1(+)，p40(-)，CK5/6(-)；特殊染色：D-PAS(-)。现患者诊", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord API raw response (len=3355):
[
	{"text": "出院记录", "bbox": [431, 33, 560, 57]},
	{"text": "登记号:", "bbox": [701, 32, 770, 50]},
	{"text": "住院号:", "bbox": [701, 57, 770, 75]},
	{"text": "姓名", "bbox": [114, 57, 148, 75]},
	{"text": "姓名：", "bbox": [202, 84, 254, 101]},
	{"text": "性别：男", "bbox": [202, 108, 325, 126]},
	{"text": "年龄：75岁", "bbox": [202, 133, 344, 150]},
	{"text": "科室·", "bbox": [202, 158, 252, 175]},
	{"text": "入院日期：2026-01-26", "bbox": [496, 84, 719, 101]},
	{"text": "出院日期：2026-01-31", "bbox": [496, 108, 717, 125]},
	{"text": "住院天数：5天", "bbox": [496, 133, 647, 150]},
	{"text": "入院情况：", "bbox": [110, 214, 204, 232]},
	{"text": "，男，75岁，因“确诊肺癌5年，病情进展1月余”于2026-01-", "bbox": [315, 214, 873, 232]},
	{"text": "26入院。患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切", "bbox": [110, 236, 873, 254]},
	{"text": "接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术", "bbox": [110, 258, 873, 276]},
	{"text": "史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。体检：T:", "bbox": [110, 279, 873, 297]},
	{"text": "36.3℃ P:69次/分 R:17次/分 BP:120/66mmHg。神志清，精神可，双肺呼吸音清，未", "bbox": [110, 300, 873, 318]},
	{"text": "闻及干湿性啰音。心脏各瓣膜听诊区未闻及异常杂音。腹软，无压痛，Murphy征阴", "bbox": [110, 322, 873, 340]},
	{"text": "性。双下肢无水肿。病理征阴性。辅助检查：2020-12-21行支气管镜检查，组织病理", "bbox": [110, 344, 873, 362]},
	{"text": "学示：(左侧隆突粘膜)非小细胞肺癌，免疫组化：CK7(+)，TTF-1(+)，", "bbox": [110, 365, 780, 383]},
	{"text": "NapsinA(+)，p40(部分+)，p63(部分+)，CK5/6(+)，ALK-D5F3(-)，ALK-", "bbox": [110, 387, 873, 405]},
	{"text": "D5F3-N(-)，S100(-)，Calponin(-)。结合免疫组化结果，符合腺癌；(左肺", "bbox": [110, 409, 873, 427]},
	{"text": "BALF)细胞蜡块内发现少量恶性肿瘤细胞。", "bbox": [110, 430, 489, 448]},
	{"text": "入院诊断：肺部恶性肿瘤纵隔淋巴结继发恶性肿瘤肺门淋巴结继发恶性肿瘤", "bbox": [110, 451, 790, 469]},
	{"text": "诊疗经过：入院后完善相关检验检查，【检验】血常规(无网红)+CRP：白细胞计数7.", "bbox": [110, 472, 870, 490]},
	{"text": "49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血", "bbox": [110, 494, 873, 512]},
	{"text": "小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原", "bbox": [110, 515, 873, 533]},
	{"text": "测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：", "bbox": [110, 537, 873, 555]},
	{"text": "22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4.", "bbox": [110, 558, 870, 576]},
	{"text": "820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆", "bbox": [110, 580, 873, 598]},
	{"text": "抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血", "bbox": [110, 601, 873, 619]},
	{"text": "试验、传染性标志物4项检测未见异常。【检查】十二通道常规心电图检查：大致正常", "bbox": [110, 623, 873, 641]},
	{"text": "心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性", "bbox": [110, 644, 873, 662]},
	{"text": "可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝", "bbox": [110, 666, 873, 684]},
	{"text": "囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超", "bbox": [110, 687, 873, 705]},
	{"text": "声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复", "bbox": [110, 709, 873, 727]},
	{"text": "查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随", "bbox": [110, 730, 873, 748]},
	{"text": "访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规", "bbox": [110, 752, 873, 770]},
	{"text": "整，请结合临床；【诊疗】入院后给予完善相关检查，排除禁忌后于2026-01-28行CT", "bbox": [110, 773, 873, 791]},
	{"text": "引导下经皮穿刺肺活检术，2026-01-30左肺组织穿刺活检示非小细胞肺癌伴大片坏", "bbox": [110, 795, 873, 813]},
	{"text": "死，结合形态学及免疫组化，符合腺癌。免疫组化示肿瘤细胞：CKpan(+)，", "bbox": [110, 816, 790, 834]},
	{"text": "CK7(+)，TTF-1(+)，p40(-)，CK5/6(-)；特殊染色：D-PAS(-)。现患者诊", "bbox": [110, 838, 873, 856]},
	{"text": "第1页", "bbox": [821, 870, 873, 887]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 977, 986]}
]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord API: raw_items=45, valid_items=45, elapsed=19.8s
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[431, 33, 560, 57]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[1]: text=登记号:, bbox=[701, 32, 770, 50]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[2]: text=住院号:, bbox=[701, 57, 770, 75]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[114, 57, 148, 75]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[202, 84, 254, 101]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[202, 108, 325, 126]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：75岁, bbox=[202, 133, 344, 150]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[7]: text=科室·, bbox=[202, 158, 252, 175]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[8]: text=入院日期：2026-01-26, bbox=[496, 84, 719, 101]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[9]: text=出院日期：2026-01-31, bbox=[496, 108, 717, 125]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[10]: text=住院天数：5天, bbox=[496, 133, 647, 150]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[11]: text=入院情况：, bbox=[110, 214, 204, 232]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[12]: text=，男，75岁，因“确诊肺癌5年，病情进展1月余”于2026-01-, bbox=[315, 214, 873, 232]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[13]: text=26入院。患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切, bbox=[110, 236, 873, 254]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[14]: text=接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术, bbox=[110, 258, 873, 276]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[15]: text=史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。体检：T:, bbox=[110, 279, 873, 297]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[16]: text=36.3℃ P:69次/分 R:17次/分 BP:120/66mmHg。神志清，精神可，双肺呼吸音清，未, bbox=[110, 300, 873, 318]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[17]: text=闻及干湿性啰音。心脏各瓣膜听诊区未闻及异常杂音。腹软，无压痛，Murphy征阴, bbox=[110, 322, 873, 340]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[18]: text=性。双下肢无水肿。病理征阴性。辅助检查：2020-12-21行支气管镜检查，组织病理, bbox=[110, 344, 873, 362]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[19]: text=学示：(左侧隆突粘膜)非小细胞肺癌，免疫组化：CK7(+)，TTF-1(+)，, bbox=[110, 365, 780, 383]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[20]: text=NapsinA(+)，p40(部分+)，p63(部分+)，CK5/6(+)，ALK-D5F3(-)，ALK-, bbox=[110, 387, 873, 405]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[21]: text=D5F3-N(-)，S100(-)，Calponin(-)。结合免疫组化结果，符合腺癌；(左肺, bbox=[110, 409, 873, 427]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[22]: text=BALF)细胞蜡块内发现少量恶性肿瘤细胞。, bbox=[110, 430, 489, 448]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[23]: text=入院诊断：肺部恶性肿瘤纵隔淋巴结继发恶性肿瘤肺门淋巴结继发恶性肿瘤, bbox=[110, 451, 790, 469]
2026-08-10 17:44:45,102 INFO     29 [qwen-vl-text] coord item[24]: text=诊疗经过：入院后完善相关检验检查，【检验】血常规(无网红)+CRP：白细胞计数7., bbox=[110, 472, 870, 490]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[25]: text=49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血, bbox=[110, 494, 873, 512]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[26]: text=小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原, bbox=[110, 515, 873, 533]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[27]: text=测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：, bbox=[110, 537, 873, 555]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[28]: text=22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4., bbox=[110, 558, 870, 576]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[29]: text=820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆, bbox=[110, 580, 873, 598]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[30]: text=抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血, bbox=[110, 601, 873, 619]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[31]: text=试验、传染性标志物4项检测未见异常。【检查】十二通道常规心电图检查：大致正常, bbox=[110, 623, 873, 641]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[32]: text=心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性, bbox=[110, 644, 873, 662]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[33]: text=可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝, bbox=[110, 666, 873, 684]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[34]: text=囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超, bbox=[110, 687, 873, 705]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[35]: text=声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复, bbox=[110, 709, 873, 727]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[36]: text=查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随, bbox=[110, 730, 873, 748]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[37]: text=访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规, bbox=[110, 752, 873, 770]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[38]: text=整，请结合临床；【诊疗】入院后给予完善相关检查，排除禁忌后于2026-01-28行CT, bbox=[110, 773, 873, 791]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[39]: text=引导下经皮穿刺肺活检术，2026-01-30左肺组织穿刺活检示非小细胞肺癌伴大片坏, bbox=[110, 795, 873, 813]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[40]: text=死，结合形态学及免疫组化，符合腺癌。免疫组化示肿瘤细胞：CKpan(+)，, bbox=[110, 816, 790, 834]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[41]: text=CK7(+)，TTF-1(+)，p40(-)，CK5/6(-)；特殊染色：D-PAS(-)。现患者诊, bbox=[110, 838, 873, 856]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[42]: text=第1页, bbox=[821, 870, 873, 887]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[43]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] coord item[44]: text=3亿人都在用的扫描App, bbox=[861, 977, 977, 986]
2026-08-10 17:44:45,103 INFO     29 [qwen-vl-text] page=3 — 45/45 coords, api_time=19.8s
2026-08-10 17:44:45,104 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=851225, prompt_len=986
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["出院记录", "登记号", "住院号", "姓名：", "断明确，拟出院后行基因检测治疗，准予办理出院。", "出院诊断：肺部恶性肿瘤（腺癌 rT4N3MO IVA期）", "纵隔淋巴结继发恶性肿瘤", "肺门淋巴结继发恶性肿瘤", "颈部淋巴结肿大", "脾术后", "慢性胆囊炎", "肝囊肿", "肾结节", "出院情况：患者一般情况可，查体：神志清，双肺呼吸音清，心律齐，腹软，无压痛", "及反跳痛，双下肢无水肿。", "出院医嘱：", "1.注意休息，避免感染、劳累；", "2.出院后分子病理科行基因检测，出院2周待结果回报后于呼吸与危重症医学科门诊就", "诊就诊制定进一步治疗方案；", "3.如有不适或复查指标异常，门急诊及时就诊。", "出院目的地：居家", "患者照护需求：注意休息，避免感染、劳累", "医师签名："]

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
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord API raw response (len=1319):
[
	{"text": "出院记录", "bbox": [432, 110, 561, 132]},
	{"text": "登记号", "bbox": [701, 110, 760, 126]},
	{"text": "住院号", "bbox": [701, 134, 760, 150]},
	{"text": "姓名：", "bbox": [113, 135, 154, 151]},
	{"text": "断明确，拟出院后行基因检测治疗，准予办理出院。", "bbox": [110, 160, 568, 177]},
	{"text": "出院诊断：肺部恶性肿瘤（腺癌 rT4N3MO IVA期）", "bbox": [110, 181, 548, 198]},
	{"text": "纵隔淋巴结继发恶性肿瘤", "bbox": [190, 203, 414, 220]},
	{"text": "肺门淋巴结继发恶性肿瘤", "bbox": [190, 224, 414, 241]},
	{"text": "颈部淋巴结肿大", "bbox": [190, 246, 334, 263]},
	{"text": "脾术后", "bbox": [190, 268, 252, 285]},
	{"text": "慢性胆囊炎", "bbox": [190, 290, 293, 307]},
	{"text": "肝囊肿", "bbox": [190, 312, 252, 329]},
	{"text": "肾结节", "bbox": [190, 334, 252, 350]},
	{"text": "出院情况：患者一般情况可，查体：神志清，双肺呼吸音清，心律齐，腹软，无压痛", "bbox": [109, 355, 873, 372]},
	{"text": "及反跳痛，双下肢无水肿。", "bbox": [109, 377, 348, 393]},
	{"text": "出院医嘱：", "bbox": [109, 398, 203, 414]},
	{"text": "1.注意休息，避免感染、劳累；", "bbox": [109, 419, 386, 436]},
	{"text": "2.出院后分子病理科行基因检测，出院2周待结果回报后于呼吸与危重症医学科门诊就", "bbox": [109, 441, 871, 458]},
	{"text": "诊就诊制定进一步治疗方案；", "bbox": [109, 463, 366, 479]},
	{"text": "3.如有不适或复查指标异常，门急诊及时就诊。", "bbox": [109, 484, 528, 501]},
	{"text": "出院目的地：居家", "bbox": [109, 506, 274, 522]},
	{"text": "患者照护需求：注意休息，避免感染、劳累", "bbox": [109, 527, 497, 544]},
	{"text": "医师签名：", "bbox": [672, 553, 760, 569]}
]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=7.2s
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[432, 110, 561, 132]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[1]: text=登记号, bbox=[701, 110, 760, 126]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[2]: text=住院号, bbox=[701, 134, 760, 150]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[113, 135, 154, 151]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[4]: text=断明确，拟出院后行基因检测治疗，准予办理出院。, bbox=[110, 160, 568, 177]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[5]: text=出院诊断：肺部恶性肿瘤（腺癌 rT4N3MO IVA期）, bbox=[110, 181, 548, 198]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[6]: text=纵隔淋巴结继发恶性肿瘤, bbox=[190, 203, 414, 220]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[7]: text=肺门淋巴结继发恶性肿瘤, bbox=[190, 224, 414, 241]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[8]: text=颈部淋巴结肿大, bbox=[190, 246, 334, 263]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[9]: text=脾术后, bbox=[190, 268, 252, 285]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[10]: text=慢性胆囊炎, bbox=[190, 290, 293, 307]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[11]: text=肝囊肿, bbox=[190, 312, 252, 329]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[12]: text=肾结节, bbox=[190, 334, 252, 350]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[13]: text=出院情况：患者一般情况可，查体：神志清，双肺呼吸音清，心律齐，腹软，无压痛, bbox=[109, 355, 873, 372]
2026-08-10 17:44:52,287 INFO     29 [qwen-vl-text] coord item[14]: text=及反跳痛，双下肢无水肿。, bbox=[109, 377, 348, 393]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] coord item[15]: text=出院医嘱：, bbox=[109, 398, 203, 414]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] coord item[16]: text=1.注意休息，避免感染、劳累；, bbox=[109, 419, 386, 436]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] coord item[17]: text=2.出院后分子病理科行基因检测，出院2周待结果回报后于呼吸与危重症医学科门诊就, bbox=[109, 441, 871, 458]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] coord item[18]: text=诊就诊制定进一步治疗方案；, bbox=[109, 463, 366, 479]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] coord item[19]: text=3.如有不适或复查指标异常，门急诊及时就诊。, bbox=[109, 484, 528, 501]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] coord item[20]: text=出院目的地：居家, bbox=[109, 506, 274, 522]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] coord item[21]: text=患者照护需求：注意休息，避免感染、劳累, bbox=[109, 527, 497, 544]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] coord item[22]: text=医师签名：, bbox=[672, 553, 760, 569]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] page=4 — 23/23 coords, api_time=7.2s
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] new_positions (68):
[[3, 256.445, 333.2, 27.785999999999998, 47.994], [3, 417.09499999999997, 458.15, 26.944, 42.1], [3, 417.09499999999997, 458.15, 47.994, 63.15], [3, 67.83, 88.06, 47.994, 63.15], [3, 120.19, 151.13, 70.728, 85.042], [3, 120.19, 193.375, 90.93599999999999, 106.092], [3, 120.19, 204.67999999999998, 111.98599999999999, 126.3], [3, 120.19, 149.94, 133.036, 147.35], [3, 295.12, 427.805, 70.728, 85.042], [3, 295.12, 426.615, 90.93599999999999, 105.25], [3, 295.12, 384.965, 111.98599999999999, 126.3], [3, 65.45, 121.38, 180.188, 195.344], [3, 187.42499999999998, 519.435, 180.188, 195.344], [3, 65.45, 519.435, 198.712, 213.868], [3, 65.45, 519.435, 217.236, 232.392], [3, 65.45, 519.435, 234.91799999999998, 250.07399999999998], [3, 65.45, 519.435, 252.6, 267.756], [3, 65.45, 519.435, 271.12399999999997, 286.28], [3, 65.45, 519.435, 289.64799999999997, 304.804], [3, 65.45, 464.09999999999997, 307.33, 322.486], [3, 65.45, 519.435, 325.854, 341.01], [3, 65.45, 519.435, 344.378, 359.534], [3, 65.45, 290.955, 362.06, 377.216], [3, 65.45, 470.04999999999995, 379.74199999999996, 394.89799999999997], [3, 65.45, 517.65, 397.424, 412.58], [3, 65.45, 519.435, 415.948, 431.104], [3, 65.45, 519.435, 433.63, 448.786], [3, 65.45, 519.435, 452.154, 467.31], [3, 65.45, 517.65, 469.83599999999996, 484.99199999999996], [3, 65.45, 519.435, 488.35999999999996, 503.51599999999996], [3, 65.45, 519.435, 506.042, 521.198], [3, 65.45, 519.435, 524.566, 539.722], [3, 65.45, 519.435, 542.2479999999999, 557.404], [3, 65.45, 519.435, 560.7719999999999, 575.928], [3, 65.45, 519.435, 578.454, 593.61], [3, 65.45, 519.435, 596.978, 612.134], [3, 65.45, 519.435, 614.66, 629.816], [3, 65.45, 519.435, 633.184, 648.34], [3, 65.45, 519.435, 650.866, 666.0219999999999], [3, 65.45, 519.435, 669.39, 684.5459999999999], [3, 65.45, 470.04999999999995, 687.072, 702.228], [3, 65.45, 519.435, 705.596, 720.752], [3, 488.495, 519.435, 732.54, 746.8539999999999], [3, 512.295, 581.3149999999999, 806.636, 820.108], [3, 512.295, 581.3149999999999, 822.634, 830.212], [4, 257.03999999999996, 333.79499999999996, 92.61999999999999, 111.14399999999999], [4, 417.09499999999997, 452.2, 92.61999999999999, 106.092], [4, 417.09499999999997, 452.2, 112.828, 126.3], [4, 67.235, 91.63, 113.67, 127.142], [4, 65.45, 337.96, 134.72, 149.034], [4, 65.45, 326.06, 152.402, 166.716], [4, 113.05, 246.32999999999998, 170.926, 185.23999999999998], [4, 113.05, 246.32999999999998, 188.608, 202.922], [4, 113.05, 198.73, 207.132, 221.446], [4, 113.05, 149.94, 225.656, 239.97], [4, 113.05, 174.33499999999998, 244.17999999999998, 258.49399999999997], [4, 113.05, 149.94, 262.704, 277.018], [4, 113.05, 149.94, 281.228, 294.7], [4, 64.855, 519.435, 298.90999999999997, 313.224], [4, 64.855, 207.06, 317.43399999999997, 330.906], [4, 64.855, 120.785, 335.116, 348.58799999999997], [4, 64.855, 229.67, 352.798, 367.11199999999997], [4, 64.855, 518.245, 371.322, 385.63599999999997], [4, 64.855, 217.76999999999998, 389.846, 403.318], [4, 64.855, 314.15999999999997, 407.52799999999996, 421.842], [4, 64.855, 163.03, 426.05199999999996, 439.524], [4, 64.855, 295.715, 443.734, 458.048], [4, 399.84, 452.2, 465.626, 479.09799999999996]]
2026-08-10 17:44:52,288 INFO     29 [qwen-vl-text] ═══ DONE ═══ 68 positions, pages=2, time=41.8s
2026-08-10 17:44:52,301 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 17:44:52,302 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:44:52,302 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 17:44:52,303 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:44:52.302+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:44:52,310 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:44:52,311 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:44:52,311 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 17:44:52,311 INFO     29 [qwen-vl-text] positions(96): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:44:52,311 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2], lines per page: [43, 39, 14]
2026-08-10 17:44:52,566 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:44:52,855 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:44:52,942 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:44:52,943 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2343
2026-08-10 17:44:52,943 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:44:52,943 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 95, \"encounter_dates\": [\"2026-01-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "第2次住院\n入院记录\n姓名：\n姓名：\n出生地：\n性别：男\n职业：其他\n年龄：75岁\n入院时间：2026-01-26 10:12\n民族：汉族\n记录时间：2026-01-26 13:59\n婚姻：已婚\n病史陈述者：患者本人\n主诉：确诊肺癌5年，病情进展1月余\n现病史：患者因“胸闷2月，干咳1周”于2020年12月17日第一次入住我科，于2020-\n12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：\nCK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），\nCK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合\n免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞；（痰）\n涂片内发现少量可疑恶性肿瘤细胞，于2020-12-27给予培美曲塞800mgd1+卡铂\n400mgd2，并辅以止吐、保胃等治疗，化疗过程顺利，准予出院。出院诊断：左肺上叶恶\n性肿瘤（腺癌 T4N3M1 IV期）、为肿瘤化学治疗疗程、纵隔淋巴结继发恶性肿瘤、肺\n门淋巴结继发恶性肿瘤、阻塞性肺炎、肝囊肿、单纯性肾囊肿。出院后先后服用吉非\n替尼、泰瑞沙靶向治疗至今。\n1月余前患者就诊于外院，复查肺CT提示病灶增大，具体不详，无发热乏力，无咳\n嗽咳痰，无胸闷憋气等不适，为求进一步诊治就诊于我院门诊，为行二次活检收入我\n科，患者自发病以来，神志清，精神可，饮食睡眠可，大小便正常，体重近期未见明\n显变化。\n既往史：患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切\n接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术\n史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。\n个人史：生于山东省胶州市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿\n山、高氟区、低碘区居住史，无化学性物质、无放射性物质、无有毒物质接触史，无\n吸毒史，无吸烟史，无饮酒史，无特殊药物服用史，无冶游史。\n婚姻史：适龄结婚，配偶体健。\n家族史：父母已故（具体不详），父有糖尿病病史，1弟因白血病去世，一妹去世，2\n妹健在，否认家族中有遗传倾向性疾病及传染性疾病。\n体格检查\nT：36.3℃ P：69次/分 R：17次/分 BP：120/66mmHg H：160cm W：52kg BMI：20.\n31kg/m²\n一般情况：正常发育状态，营养良好，体型匀称型，自主体位，正常面容，神志清楚\n，正常步态，语言清晰，查体合作。\n第1页\n另2次住院\n入院记录\n登记号:\n姓名:\n住院号\n皮肤、粘膜：皮肤黏膜无黄染 无皮疹、皮下出血，无皮下结节、瘢痕，皮下无水肿，\n毛发分布正常，无肝掌、蜘蛛痣。全身浅表淋巴结：全身浅表淋巴结无肿大。\n头部及其器官：头颅无畸形，毛发分布正常。眉毛正常，睫毛正常，无眼睑水肿，\n结膜无充血、苍白，眼球无震颤，巩膜无黄染，角膜正常，瞳孔等大等圆，对光调节\n反射正常。外耳道无畸形，无异常分泌物，乳突无压痛，听力正常。外鼻无畸形，无\n鼻翼扇动，无分泌物、出血、阻塞，鼻中隔基本居中，无穿孔，双侧鼻窦区无压痛。\n口唇无发绀，口腔粘膜无溃疡。伸舌无偏斜、震颤，齿龈无肿胀、出血。咽部粘膜无\n充血，扁桃体无肥大。喉咙发音清晰。\n颈部：颈部对称，软，颈动脉搏动正常，颈静脉无怒张，气管居中，肝颈静脉回流征\n阴性，甲状腺无肿大，无压痛，未扪及包块，未闻及血管杂音。\n胸部：胸廓对称、无畸形，乳房发育正常，胸骨无压痛，呼吸17次/分。\n肺部：呼吸运动正常，肋间隙无增宽、无变窄，呼吸规整，语颤无增强及减弱，无胸\n膜摩擦感、无皮下捻发感。叩诊清音，双肺呼吸音清晰，未闻及干、湿性啰音，语音\n传导正常，无胸膜摩擦音。\n心脏：心前区无隆起，心尖搏动未见增强及弥散，无震颤及心包摩擦感，心浊音界无\n扩大，心率69次/分，律齐，各瓣膜听诊区未闻及病理性杂音，无心包摩擦音。\n血管：桡动脉：脉率69次/分，脉律规整。无毛细血管搏动征，无股动脉枪击音。\n腹部：腹部平坦，对称，无腹壁静脉曲张，无胃肠型和蠕动波，腹部柔软，无压痛及\n反跳痛，未触及异常包块。肝、脾肋下未触及、质软、无压痛，Murphy氏征阴性。腹\n部叩诊：肝上界在右锁骨中线第五肋间，肝、肾区无叩击痛，无移动性浊音。肠鸣音\n正常，4次/分。未听到血管杂音。\n直肠肛门：肛门及直肠无异常。外生殖器无异常。\n脊柱、四肢：脊柱正常生理弯曲，无畸形、压痛、叩击痛，活动度正常，四肢无畸\n形，肌力、肌张力正常，关节活动度正常，双下肢无水肿，无静脉曲张。\n神经系统：痛、温、触觉正常，肌肉无萎缩、无瘫痪，无共济失调。腹壁反射正常，\n双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性、\nGordon征阴性、Oppenheim征阴性、Hoffmann征阴性，脑膜刺激征阴性。\n专科检查\n辅助检查\n2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组\n化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），\nCK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合\n免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。\n第2页\n第2次住院\n入院记录\n登记号:\n姓名:\n住院号\n初步诊断\n肺部恶性肿瘤\n纵隔淋巴结继发恶性肿瘤\n肺门淋巴结继发恶性肿瘤\n医师签名\n项目内容\n患者（家属）签名\n以上患者所述内容及提供资料属实\n门诊病历已归还",
    "role": "user"
  }
]
2026-08-10 17:45:09,736 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:45:09,736 INFO     29 [qwen-vl-text] LLM output (len=3096):
{
  "encounter_date": "2026-01-26",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": 75,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "其他",
  "dm_admission_time": "2026-01-26 10:12",
  "dm_record_time": "2026-01-26 13:59",
  "dm_history_provider": "患者本人",
  "cc_text": "确诊肺癌5年，病情进展1月余",
  "cc_main_symptoms": [
    "确诊肺癌",
    "病情进展"
  ],
  "cc_duration": "5年，1月余",
  "pi_text": "患者因“胸闷2月，干咳1周”于2020年12月17日第一次入住我科，于2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞；（痰）涂片内发现少量可疑恶性肿瘤细胞，于2020-12-27给予培美曲塞800mgd1+卡铂400mgd2，并辅以止吐、保胃等治疗，化疗过程顺利，准予出院。出院诊断：左肺上叶恶性肿瘤（腺癌 T4N3M1 IV期）、为肿瘤化学治疗疗程、纵隔淋巴结继发恶性肿瘤、肺门淋巴结继发恶性肿瘤、阻塞性肺炎、肝囊肿、单纯性肾囊肿。出院后先后服用吉非替尼、泰瑞沙靶向治疗至今。1月余前患者就诊于外院，复查肺CT提示病灶增大，具体不详，无发热乏力，无咳嗽咳痰，无胸闷憋气等不适，为求进一步诊治就诊于我院门诊，为行二次活检收入我科，患者自发病以来，神志清，精神可，饮食睡眠可，大小便正常，体重近期未见明显变化。",
  "pmh_disease_history": [
    "否认肝炎病史",
    "无结核病史",
    "否认疟疾病史",
    "否认高血压、心脏病史",
    "否认糖尿病、脑血管疾病、精神疾病史"
  ],
  "pmh_allergy_history": [
    "无药物、食物过敏史"
  ],
  "pmh_surgery_trauma_history": [
    "否认手术史",
    "无外伤史",
    "无输血史"
  ],
  "ph_smoking": "无吸烟史",
  "ph_drinking": "无饮酒史",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "父母已故（具体不详），父有糖尿病病史，1弟因白血病去世，一妹去世，2妹健在，否认家族中有遗传倾向性疾病及传染性疾病。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.3,
  "vs_pulse_bpm": 69,
  "vs_respiration_rpm": 17,
  "vs_systolic_bp_mmhg": 120,
  "vs_diastolic_bp_mmhg": 66,
  "pe_general_condition": "正常发育状态，营养良好，体型匀称型，自主体位，正常面容，神志清楚，正常步态，语言清晰，查体合作。",
  "pe_skin_mucosa": "皮肤黏膜无黄染 无皮疹、皮下出血，无皮下结节、瘢痕，皮下无水肿，毛发分布正常，无肝掌、蜘蛛痣。",
  "pe_lymph_nodes": "全身浅表淋巴结无肿大。",
  "pe_lungs": "呼吸运动正常，肋间隙无增宽、无变窄，呼吸规整，语颤无增强及减弱，无胸膜摩擦感、无皮下捻发感。叩诊清音，双肺呼吸音清晰，未闻及干、湿性啰音，语音传导正常，无胸膜摩擦音。",
  "pe_heart": "心前区无隆起，心尖搏动未见增强及弥散，无震颤及心包摩擦感，心浊音界无扩大，心率69次/分，律齐，各瓣膜听诊区未闻及病理性杂音，无心包摩擦音。",
  "pe_abdomen": "腹部平坦，对称，无腹壁静脉曲张，无胃肠型和蠕动波，腹部柔软，无压痛及反跳痛，未触及异常包块。肝、脾肋下未触及、质软、无压痛，Murphy氏征阴性。腹部叩诊：肝上界在右锁骨中线第五肋间，肝、肾区无叩击痛，无移动性浊音。肠鸣音正常，4次/分。未听到血管杂音。",
  "pe_extremities": "脊柱正常生理弯曲，无畸形、压痛、叩击痛，活动度正常，四肢无畸形，肌力、肌张力正常，关节活动度正常，双下肢无水肿，无静脉曲张。",
  "pe_nervous_system": "痛、温、触觉正常，肌肉无萎缩、无瘫痪，无共济失调。腹壁反射正常，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性、Gordon征阴性、Oppenheim征阴性、Hoffmann征阴性，脑膜刺激征阴性。",
  "pe_specialist_exam": null,
  "pe_ecog_score": null,
  "pat_text": "2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。",
  "pat_items": [
    "2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。"
  ],
  "preliminary_diagnoses": [
    {
      "name": "肺部恶性肿瘤",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "纵隔淋巴结继发恶性肿瘤",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肺门淋巴结继发恶性肿瘤",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 17:45:09,736 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-26]
2026-08-10 17:45:09,739 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2328242, prompt_len=1824
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["第2次住院", "入院记录", "姓名：", "姓名：", "出生地：", "性别：男", "职业：其他", "年龄：75岁", "入院时间：2026-01-26 10:12", "民族：汉族", "记录时间：2026-01-26 13:59", "婚姻：已婚", "病史陈述者：患者本人", "主诉：确诊肺癌5年，病情进展1月余", "现病史：患者因“胸闷2月，干咳1周”于2020年12月17日第一次入住我科，于2020-", "12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：", "CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），", "CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合", "免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞；（痰）", "涂片内发现少量可疑恶性肿瘤细胞，于2020-12-27给予培美曲塞800mgd1+卡铂", "400mgd2，并辅以止吐、保胃等治疗，化疗过程顺利，准予出院。出院诊断：左肺上叶恶", "性肿瘤（腺癌 T4N3M1 IV期）、为肿瘤化学治疗疗程、纵隔淋巴结继发恶性肿瘤、肺", "门淋巴结继发恶性肿瘤、阻塞性肺炎、肝囊肿、单纯性肾囊肿。出院后先后服用吉非", "替尼、泰瑞沙靶向治疗至今。", "1月余前患者就诊于外院，复查肺CT提示病灶增大，具体不详，无发热乏力，无咳", "嗽咳痰，无胸闷憋气等不适，为求进一步诊治就诊于我院门诊，为行二次活检收入我", "科，患者自发病以来，神志清，精神可，饮食睡眠可，大小便正常，体重近期未见明", "显变化。", "既往史：患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切", "接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术", "史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。", "个人史：生于山东省胶州市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿", "山、高氟区、低碘区居住史，无化学性物质、无放射性物质、无有毒物质接触史，无", "吸毒史，无吸烟史，无饮酒史，无特殊药物服用史，无冶游史。", "婚姻史：适龄结婚，配偶体健。", "家族史：父母已故（具体不详），父有糖尿病病史，1弟因白血病去世，一妹去世，2", "妹健在，否认家族中有遗传倾向性疾病及传染性疾病。", "体格检查", "T：36.3℃ P：69次/分 R：17次/分 BP：120/66mmHg H：160cm W：52kg BMI：20.", "31kg/m²", "一般情况：正常发育状态，营养良好，体型匀称型，自主体位，正常面容，神志清楚", "，正常步态，语言清晰，查体合作。", "第1页"]

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
2026-08-10 17:45:25,287 INFO     29 [qwen-vl-text] coord API raw response (len=2971):
[
	{"text": "第2次住院", "bbox": [187, 67, 244, 77]},
	{"text": "入院记录", "bbox": [414, 65, 545, 89]},
	{"text": "姓名：", "bbox": [99, 93, 148, 110]},
	{"text": "姓名：", "bbox": [217, 132, 267, 149]},
	{"text": "出生地：", "bbox": [481, 132, 551, 149]},
	{"text": "性别：男", "bbox": [217, 157, 311, 174]},
	{"text": "职业：其他", "bbox": [481, 157, 663, 174]},
	{"text": "年龄：75岁", "bbox": [217, 182, 331, 199]},
	{"text": "入院时间：2026-01-26 10:12", "bbox": [481, 182, 785, 199]},
	{"text": "民族：汉族", "bbox": [217, 207, 331, 224]},
	{"text": "记录时间：2026-01-26 13:59", "bbox": [620, 207, 785, 224]},
	{"text": "婚姻：已婚", "bbox": [217, 233, 331, 250]},
	{"text": "病史陈述者：患者本人", "bbox": [481, 233, 702, 250]},
	{"text": "主诉：确诊肺癌5年，病情进展1月余", "bbox": [107, 274, 433, 292]},
	{"text": "现病史：患者因“胸闷2月，干咳1周”于2020年12月17日第一次入住我科，于2020-", "bbox": [107, 297, 870, 314]},
	{"text": "12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：", "bbox": [107, 319, 860, 337]},
	{"text": "CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），", "bbox": [107, 341, 746, 359]},
	{"text": "CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合", "bbox": [107, 363, 870, 380]},
	{"text": "免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞；（痰）", "bbox": [107, 385, 860, 402]},
	{"text": "涂片内发现少量可疑恶性肿瘤细胞，于2020-12-27给予培美曲塞800mgd1+卡铂", "bbox": [107, 406, 798, 424]},
	{"text": "400mgd2，并辅以止吐、保胃等治疗，化疗过程顺利，准予出院。出院诊断：左肺上叶恶", "bbox": [107, 428, 870, 446]},
	{"text": "性肿瘤（腺癌 T4N3M1 IV期）、为肿瘤化学治疗疗程、纵隔淋巴结继发恶性肿瘤、肺", "bbox": [107, 450, 870, 468]},
	{"text": "门淋巴结继发恶性肿瘤、阻塞性肺炎、肝囊肿、单纯性肾囊肿。出院后先后服用吉非", "bbox": [107, 472, 870, 490]},
	{"text": "替尼、泰瑞沙靶向治疗至今。", "bbox": [107, 493, 367, 510]},
	{"text": "1月余前患者就诊于外院，复查肺CT提示病灶增大，具体不详，无发热乏力，无咳", "bbox": [107, 514, 870, 532]},
	{"text": "嗽咳痰，无胸闷憋气等不适，为求进一步诊治就诊于我院门诊，为行二次活检收入我", "bbox": [107, 536, 870, 554]},
	{"text": "科，患者自发病以来，神志清，精神可，饮食睡眠可，大小便正常，体重近期未见明", "bbox": [107, 557, 870, 575]},
	{"text": "显变化。", "bbox": [107, 579, 180, 596]},
	{"text": "既往史：患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切", "bbox": [107, 601, 864, 618]},
	{"text": "接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术", "bbox": [107, 623, 870, 640]},
	{"text": "史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。", "bbox": [107, 644, 760, 662]},
	{"text": "个人史：生于山东省胶州市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿", "bbox": [107, 666, 870, 684]},
	{"text": "山、高氟区、低碘区居住史，无化学性物质、无放射性物质、无有毒物质接触史，无", "bbox": [107, 688, 870, 705]},
	{"text": "吸毒史，无吸烟史，无饮酒史，无特殊药物服用史，无冶游史。", "bbox": [107, 710, 668, 727]},
	{"text": "婚姻史：适龄结婚，配偶体健。", "bbox": [107, 730, 384, 748]},
	{"text": "家族史：父母已故（具体不详），父有糖尿病病史，1弟因白血病去世，一妹去世，2", "bbox": [107, 752, 870, 770]},
	{"text": "妹健在，否认家族中有遗传倾向性疾病及传染性疾病。", "bbox": [107, 774, 588, 791]},
	{"text": "体格检查", "bbox": [449, 796, 531, 813]},
	{"text": "T：36.3℃ P：69次/分 R：17次/分 BP：120/66mmHg H：160cm W：52kg BMI：20.", "bbox": [130, 818, 865, 835]},
	{"text": "31kg/m²", "bbox": [111, 840, 178, 856]},
	{"text": "一般情况：正常发育状态，营养良好，体型匀称型，自主体位，正常面容，神志清楚", "bbox": [107, 859, 870, 877]},
	{"text": "，正常步态，语言清晰，查体合作。", "bbox": [111, 880, 425, 898]},
	{"text": "第1页", "bbox": [818, 909, 870, 925]}
]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=15.5s
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[0]: text=第2次住院, bbox=[187, 67, 244, 77]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[414, 65, 545, 89]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[99, 93, 148, 110]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[217, 132, 267, 149]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[4]: text=出生地：, bbox=[481, 132, 551, 149]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[217, 157, 311, 174]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[6]: text=职业：其他, bbox=[481, 157, 663, 174]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：75岁, bbox=[217, 182, 331, 199]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[8]: text=入院时间：2026-01-26 10:12, bbox=[481, 182, 785, 199]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[9]: text=民族：汉族, bbox=[217, 207, 331, 224]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[10]: text=记录时间：2026-01-26 13:59, bbox=[620, 207, 785, 224]
2026-08-10 17:45:25,288 INFO     29 [qwen-vl-text] coord item[11]: text=婚姻：已婚, bbox=[217, 233, 331, 250]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[12]: text=病史陈述者：患者本人, bbox=[481, 233, 702, 250]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[13]: text=主诉：确诊肺癌5年，病情进展1月余, bbox=[107, 274, 433, 292]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[14]: text=现病史：患者因“胸闷2月，干咳1周”于2020年12月17日第一次入住我科，于2020-, bbox=[107, 297, 870, 314]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[15]: text=12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：, bbox=[107, 319, 860, 337]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[16]: text=CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），, bbox=[107, 341, 746, 359]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[17]: text=CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合, bbox=[107, 363, 870, 380]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[18]: text=免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞；（痰）, bbox=[107, 385, 860, 402]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[19]: text=涂片内发现少量可疑恶性肿瘤细胞，于2020-12-27给予培美曲塞800mgd1+卡铂, bbox=[107, 406, 798, 424]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[20]: text=400mgd2，并辅以止吐、保胃等治疗，化疗过程顺利，准予出院。出院诊断：左肺上叶恶, bbox=[107, 428, 870, 446]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[21]: text=性肿瘤（腺癌 T4N3M1 IV期）、为肿瘤化学治疗疗程、纵隔淋巴结继发恶性肿瘤、肺, bbox=[107, 450, 870, 468]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[22]: text=门淋巴结继发恶性肿瘤、阻塞性肺炎、肝囊肿、单纯性肾囊肿。出院后先后服用吉非, bbox=[107, 472, 870, 490]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[23]: text=替尼、泰瑞沙靶向治疗至今。, bbox=[107, 493, 367, 510]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[24]: text=1月余前患者就诊于外院，复查肺CT提示病灶增大，具体不详，无发热乏力，无咳, bbox=[107, 514, 870, 532]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[25]: text=嗽咳痰，无胸闷憋气等不适，为求进一步诊治就诊于我院门诊，为行二次活检收入我, bbox=[107, 536, 870, 554]
2026-08-10 17:45:25,289 INFO     29 [qwen-vl-text] coord item[26]: text=科，患者自发病以来，神志清，精神可，饮食睡眠可，大小便正常，体重近期未见明, bbox=[107, 557, 870, 575]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[27]: text=显变化。, bbox=[107, 579, 180, 596]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[28]: text=既往史：患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切, bbox=[107, 601, 864, 618]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[29]: text=接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术, bbox=[107, 623, 870, 640]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[30]: text=史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。, bbox=[107, 644, 760, 662]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[31]: text=个人史：生于山东省胶州市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿, bbox=[107, 666, 870, 684]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[32]: text=山、高氟区、低碘区居住史，无化学性物质、无放射性物质、无有毒物质接触史，无, bbox=[107, 688, 870, 705]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[33]: text=吸毒史，无吸烟史，无饮酒史，无特殊药物服用史，无冶游史。, bbox=[107, 710, 668, 727]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[34]: text=婚姻史：适龄结婚，配偶体健。, bbox=[107, 730, 384, 748]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[35]: text=家族史：父母已故（具体不详），父有糖尿病病史，1弟因白血病去世，一妹去世，2, bbox=[107, 752, 870, 770]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[36]: text=妹健在，否认家族中有遗传倾向性疾病及传染性疾病。, bbox=[107, 774, 588, 791]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[37]: text=体格检查, bbox=[449, 796, 531, 813]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[38]: text=T：36.3℃ P：69次/分 R：17次/分 BP：120/66mmHg H：160cm W：52kg BMI：20., bbox=[130, 818, 865, 835]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[39]: text=31kg/m², bbox=[111, 840, 178, 856]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[40]: text=一般情况：正常发育状态，营养良好，体型匀称型，自主体位，正常面容，神志清楚, bbox=[107, 859, 870, 877]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[41]: text=，正常步态，语言清晰，查体合作。, bbox=[111, 880, 425, 898]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] coord item[42]: text=第1页, bbox=[818, 909, 870, 925]
2026-08-10 17:45:25,290 INFO     29 [qwen-vl-text] page=0 — 43/43 coords, api_time=15.5s
2026-08-10 17:45:25,296 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2937379, prompt_len=1887
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共39行）
["另2次住院", "入院记录", "登记号:", "姓名:", "住院号", "皮肤、粘膜：皮肤黏膜无黄染 无皮疹、皮下出血，无皮下结节、瘢痕，皮下无水肿，", "毛发分布正常，无肝掌、蜘蛛痣。全身浅表淋巴结：全身浅表淋巴结无肿大。", "头部及其器官：头颅无畸形，毛发分布正常。眉毛正常，睫毛正常，无眼睑水肿，", "结膜无充血、苍白，眼球无震颤，巩膜无黄染，角膜正常，瞳孔等大等圆，对光调节", "反射正常。外耳道无畸形，无异常分泌物，乳突无压痛，听力正常。外鼻无畸形，无", "鼻翼扇动，无分泌物、出血、阻塞，鼻中隔基本居中，无穿孔，双侧鼻窦区无压痛。", "口唇无发绀，口腔粘膜无溃疡。伸舌无偏斜、震颤，齿龈无肿胀、出血。咽部粘膜无", "充血，扁桃体无肥大。喉咙发音清晰。", "颈部：颈部对称，软，颈动脉搏动正常，颈静脉无怒张，气管居中，肝颈静脉回流征", "阴性，甲状腺无肿大，无压痛，未扪及包块，未闻及血管杂音。", "胸部：胸廓对称、无畸形，乳房发育正常，胸骨无压痛，呼吸17次/分。", "肺部：呼吸运动正常，肋间隙无增宽、无变窄，呼吸规整，语颤无增强及减弱，无胸", "膜摩擦感、无皮下捻发感。叩诊清音，双肺呼吸音清晰，未闻及干、湿性啰音，语音", "传导正常，无胸膜摩擦音。", "心脏：心前区无隆起，心尖搏动未见增强及弥散，无震颤及心包摩擦感，心浊音界无", "扩大，心率69次/分，律齐，各瓣膜听诊区未闻及病理性杂音，无心包摩擦音。", "血管：桡动脉：脉率69次/分，脉律规整。无毛细血管搏动征，无股动脉枪击音。", "腹部：腹部平坦，对称，无腹壁静脉曲张，无胃肠型和蠕动波，腹部柔软，无压痛及", "反跳痛，未触及异常包块。肝、脾肋下未触及、质软、无压痛，Murphy氏征阴性。腹", "部叩诊：肝上界在右锁骨中线第五肋间，肝、肾区无叩击痛，无移动性浊音。肠鸣音", "正常，4次/分。未听到血管杂音。", "直肠肛门：肛门及直肠无异常。外生殖器无异常。", "脊柱、四肢：脊柱正常生理弯曲，无畸形、压痛、叩击痛，活动度正常，四肢无畸", "形，肌力、肌张力正常，关节活动度正常，双下肢无水肿，无静脉曲张。", "神经系统：痛、温、触觉正常，肌肉无萎缩、无瘫痪，无共济失调。腹壁反射正常，", "双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性、", "Gordon征阴性、Oppenheim征阴性、Hoffmann征阴性，脑膜刺激征阴性。", "专科检查", "辅助检查", "2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组", "化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），", "CK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合", "免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。", "第2页"]

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
2026-08-10 17:45:42,719 INFO     29 [qwen-vl-text] coord API raw response (len=2865):
[
	{"text": "另2次住院", "bbox": [189, 26, 246, 36]},
	{"text": "入院记录", "bbox": [415, 26, 544, 49]},
	{"text": "登记号:", "bbox": [687, 25, 755, 41]},
	{"text": "姓名:", "bbox": [100, 53, 150, 69]},
	{"text": "住院号", "bbox": [687, 52, 745, 68]},
	{"text": "皮肤、粘膜：皮肤黏膜无黄染 无皮疹、皮下出血，无皮下结节、瘢痕，皮下无水肿，", "bbox": [109, 91, 860, 108]},
	{"text": "毛发分布正常，无肝掌、蜘蛛痣。全身浅表淋巴结：全身浅表淋巴结无肿大。", "bbox": [109, 112, 790, 128]},
	{"text": "头部及其器官：头颅无畸形，毛发分布正常。眉毛正常，睫毛正常，无眼睑水肿，", "bbox": [109, 133, 860, 149]},
	{"text": "结膜无充血、苍白，眼球无震颤，巩膜无黄染，角膜正常，瞳孔等大等圆，对光调节", "bbox": [109, 154, 869, 170]},
	{"text": "反射正常。外耳道无畸形，无异常分泌物，乳突无压痛，听力正常。外鼻无畸形，无", "bbox": [109, 174, 870, 191]},
	{"text": "鼻翼扇动，无分泌物、出血、阻塞，鼻中隔基本居中，无穿孔，双侧鼻窦区无压痛。", "bbox": [109, 195, 869, 212]},
	{"text": "口唇无发绀，口腔粘膜无溃疡。伸舌无偏斜、震颤，齿龈无肿胀、出血。咽部粘膜无", "bbox": [109, 216, 870, 233]},
	{"text": "充血，扁桃体无肥大。喉咙发音清晰。", "bbox": [109, 238, 454, 255]},
	{"text": "颈部：颈部对称，软，颈动脉搏动正常，颈静脉无怒张，气管居中，肝颈静脉回流征", "bbox": [109, 260, 870, 277]},
	{"text": "阴性，甲状腺无肿大，无压痛，未扪及包块，未闻及血管杂音。", "bbox": [109, 281, 668, 298]},
	{"text": "胸部：胸廓对称、无畸形，乳房发育正常，胸骨无压痛，呼吸17次/分。", "bbox": [109, 303, 738, 320]},
	{"text": "肺部：呼吸运动正常，肋间隙无增宽、无变窄，呼吸规整，语颤无增强及减弱，无胸", "bbox": [109, 325, 870, 342]},
	{"text": "膜摩擦感、无皮下捻发感。叩诊清音，双肺呼吸音清晰，未闻及干、湿性啰音，语音", "bbox": [109, 346, 870, 363]},
	{"text": "传导正常，无胸膜摩擦音。", "bbox": [109, 368, 354, 385]},
	{"text": "心脏：心前区无隆起，心尖搏动未见增强及弥散，无震颤及心包摩擦感，心浊音界无", "bbox": [109, 390, 870, 407]},
	{"text": "扩大，心率69次/分，律齐，各瓣膜听诊区未闻及病理性杂音，无心包摩擦音。", "bbox": [109, 411, 799, 428]},
	{"text": "血管：桡动脉：脉率69次/分，脉律规整。无毛细血管搏动征，无股动脉枪击音。", "bbox": [109, 433, 818, 450]},
	{"text": "腹部：腹部平坦，对称，无腹壁静脉曲张，无胃肠型和蠕动波，腹部柔软，无压痛及", "bbox": [109, 455, 869, 472]},
	{"text": "反跳痛，未触及异常包块。肝、脾肋下未触及、质软、无压痛，Murphy氏征阴性。腹", "bbox": [109, 476, 870, 493]},
	{"text": "部叩诊：肝上界在右锁骨中线第五肋间，肝、肾区无叩击痛，无移动性浊音。肠鸣音", "bbox": [109, 497, 869, 514]},
	{"text": "正常，4次/分。未听到血管杂音。", "bbox": [109, 518, 412, 535]},
	{"text": "直肠肛门：肛门及直肠无异常。外生殖器无异常。", "bbox": [109, 540, 545, 557]},
	{"text": "脊柱、四肢：脊柱正常生理弯曲，无畸形、压痛、叩击痛，活动度正常，四肢无畸", "bbox": [109, 562, 870, 579]},
	{"text": "形，肌力、肌张力正常，关节活动度正常，双下肢无水肿，无静脉曲张。", "bbox": [109, 583, 748, 600]},
	{"text": "神经系统：痛、温、触觉正常，肌肉无萎缩、无瘫痪，无共济失调。腹壁反射正常，", "bbox": [109, 605, 860, 622]},
	{"text": "双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性、", "bbox": [109, 626, 860, 643]},
	{"text": "Gordon征阴性、Oppenheim征阴性、Hoffmann征阴性，脑膜刺激征阴性。", "bbox": [109, 647, 740, 665]},
	{"text": "专科检查", "bbox": [448, 669, 530, 686]},
	{"text": "辅助检查", "bbox": [447, 735, 530, 752]},
	{"text": "2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组", "bbox": [109, 757, 870, 774]},
	{"text": "化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），", "bbox": [109, 778, 788, 795]},
	{"text": "CK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合", "bbox": [109, 800, 869, 817]},
	{"text": "免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。", "bbox": [109, 821, 788, 838]},
	{"text": "第2页", "bbox": [818, 861, 870, 877]}
]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord API: raw_items=39, valid_items=39, elapsed=17.4s
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[0]: text=另2次住院, bbox=[189, 26, 246, 36]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[415, 26, 544, 49]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[2]: text=登记号:, bbox=[687, 25, 755, 41]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[100, 53, 150, 69]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[4]: text=住院号, bbox=[687, 52, 745, 68]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[5]: text=皮肤、粘膜：皮肤黏膜无黄染 无皮疹、皮下出血，无皮下结节、瘢痕，皮下无水肿，, bbox=[109, 91, 860, 108]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[6]: text=毛发分布正常，无肝掌、蜘蛛痣。全身浅表淋巴结：全身浅表淋巴结无肿大。, bbox=[109, 112, 790, 128]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[7]: text=头部及其器官：头颅无畸形，毛发分布正常。眉毛正常，睫毛正常，无眼睑水肿，, bbox=[109, 133, 860, 149]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[8]: text=结膜无充血、苍白，眼球无震颤，巩膜无黄染，角膜正常，瞳孔等大等圆，对光调节, bbox=[109, 154, 869, 170]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[9]: text=反射正常。外耳道无畸形，无异常分泌物，乳突无压痛，听力正常。外鼻无畸形，无, bbox=[109, 174, 870, 191]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[10]: text=鼻翼扇动，无分泌物、出血、阻塞，鼻中隔基本居中，无穿孔，双侧鼻窦区无压痛。, bbox=[109, 195, 869, 212]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[11]: text=口唇无发绀，口腔粘膜无溃疡。伸舌无偏斜、震颤，齿龈无肿胀、出血。咽部粘膜无, bbox=[109, 216, 870, 233]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[12]: text=充血，扁桃体无肥大。喉咙发音清晰。, bbox=[109, 238, 454, 255]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[13]: text=颈部：颈部对称，软，颈动脉搏动正常，颈静脉无怒张，气管居中，肝颈静脉回流征, bbox=[109, 260, 870, 277]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[14]: text=阴性，甲状腺无肿大，无压痛，未扪及包块，未闻及血管杂音。, bbox=[109, 281, 668, 298]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[15]: text=胸部：胸廓对称、无畸形，乳房发育正常，胸骨无压痛，呼吸17次/分。, bbox=[109, 303, 738, 320]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[16]: text=肺部：呼吸运动正常，肋间隙无增宽、无变窄，呼吸规整，语颤无增强及减弱，无胸, bbox=[109, 325, 870, 342]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[17]: text=膜摩擦感、无皮下捻发感。叩诊清音，双肺呼吸音清晰，未闻及干、湿性啰音，语音, bbox=[109, 346, 870, 363]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[18]: text=传导正常，无胸膜摩擦音。, bbox=[109, 368, 354, 385]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[19]: text=心脏：心前区无隆起，心尖搏动未见增强及弥散，无震颤及心包摩擦感，心浊音界无, bbox=[109, 390, 870, 407]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[20]: text=扩大，心率69次/分，律齐，各瓣膜听诊区未闻及病理性杂音，无心包摩擦音。, bbox=[109, 411, 799, 428]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[21]: text=血管：桡动脉：脉率69次/分，脉律规整。无毛细血管搏动征，无股动脉枪击音。, bbox=[109, 433, 818, 450]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[22]: text=腹部：腹部平坦，对称，无腹壁静脉曲张，无胃肠型和蠕动波，腹部柔软，无压痛及, bbox=[109, 455, 869, 472]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[23]: text=反跳痛，未触及异常包块。肝、脾肋下未触及、质软、无压痛，Murphy氏征阴性。腹, bbox=[109, 476, 870, 493]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[24]: text=部叩诊：肝上界在右锁骨中线第五肋间，肝、肾区无叩击痛，无移动性浊音。肠鸣音, bbox=[109, 497, 869, 514]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[25]: text=正常，4次/分。未听到血管杂音。, bbox=[109, 518, 412, 535]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[26]: text=直肠肛门：肛门及直肠无异常。外生殖器无异常。, bbox=[109, 540, 545, 557]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[27]: text=脊柱、四肢：脊柱正常生理弯曲，无畸形、压痛、叩击痛，活动度正常，四肢无畸, bbox=[109, 562, 870, 579]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[28]: text=形，肌力、肌张力正常，关节活动度正常，双下肢无水肿，无静脉曲张。, bbox=[109, 583, 748, 600]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[29]: text=神经系统：痛、温、触觉正常，肌肉无萎缩、无瘫痪，无共济失调。腹壁反射正常，, bbox=[109, 605, 860, 622]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[30]: text=双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性、, bbox=[109, 626, 860, 643]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[31]: text=Gordon征阴性、Oppenheim征阴性、Hoffmann征阴性，脑膜刺激征阴性。, bbox=[109, 647, 740, 665]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[32]: text=专科检查, bbox=[448, 669, 530, 686]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[33]: text=辅助检查, bbox=[447, 735, 530, 752]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[34]: text=2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组, bbox=[109, 757, 870, 774]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[35]: text=化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），, bbox=[109, 778, 788, 795]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[36]: text=CK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合, bbox=[109, 800, 869, 817]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[37]: text=免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。, bbox=[109, 821, 788, 838]
2026-08-10 17:45:42,720 INFO     29 [qwen-vl-text] coord item[38]: text=第2页, bbox=[818, 861, 870, 877]
2026-08-10 17:45:42,721 INFO     29 [qwen-vl-text] page=1 — 39/39 coords, api_time=17.4s
2026-08-10 17:45:42,722 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=371552, prompt_len=757
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["第2次住院", "入院记录", "登记号:", "姓名:", "住院号", "初步诊断", "肺部恶性肿瘤", "纵隔淋巴结继发恶性肿瘤", "肺门淋巴结继发恶性肿瘤", "医师签名", "项目内容", "患者（家属）签名", "以上患者所述内容及提供资料属实", "门诊病历已归还"]

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
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord API raw response (len=719):
[
	{"text": "第2次住院", "bbox": [190, 170, 248, 180]},
	{"text": "入院记录", "bbox": [420, 170, 550, 193]},
	{"text": "登记号:", "bbox": [691, 169, 760, 186]},
	{"text": "姓名:", "bbox": [100, 195, 150, 211]},
	{"text": "住院号", "bbox": [691, 195, 750, 211]},
	{"text": "初步诊断", "bbox": [453, 257, 534, 274]},
	{"text": "肺部恶性肿瘤", "bbox": [471, 280, 591, 296]},
	{"text": "纵隔淋巴结继发恶性肿瘤", "bbox": [471, 300, 692, 317],
	"text": "肺门淋巴结继发恶性肿瘤", "bbox": [471, 322, 692, 339]},
	{"text": "医师签名", "bbox": [673, 349, 754, 365]},
	{"text": "项目内容", "bbox": [463, 394, 545, 411]},
	{"text": "患者（家属）签名", "bbox": [690, 394, 852, 411]},
	{"text": "以上患者所述内容及提供资料属实", "bbox": [320, 418, 622, 435]},
	{"text": "门诊病历已归还", "bbox": [320, 451, 463, 467]}
]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord API: raw_items=13, valid_items=13, elapsed=4.2s
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[0]: text=第2次住院, bbox=[190, 170, 248, 180]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[420, 170, 550, 193]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[2]: text=登记号:, bbox=[691, 169, 760, 186]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[100, 195, 150, 211]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[4]: text=住院号, bbox=[691, 195, 750, 211]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[5]: text=初步诊断, bbox=[453, 257, 534, 274]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[6]: text=肺部恶性肿瘤, bbox=[471, 280, 591, 296]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[7]: text=肺门淋巴结继发恶性肿瘤, bbox=[471, 322, 692, 339]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[8]: text=医师签名, bbox=[673, 349, 754, 365]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[9]: text=项目内容, bbox=[463, 394, 545, 411]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[10]: text=患者（家属）签名, bbox=[690, 394, 852, 411]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[11]: text=以上患者所述内容及提供资料属实, bbox=[320, 418, 622, 435]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] coord item[12]: text=门诊病历已归还, bbox=[320, 451, 463, 467]
2026-08-10 17:45:46,952 INFO     29 [qwen-vl-text] page=2 — 14/14 coords, api_time=4.2s
2026-08-10 17:45:46,953 INFO     29 [qwen-vl-text] new_positions (96):
[[0, 111.265, 145.18, 56.414, 64.834], [0, 246.32999999999998, 324.275, 54.73, 74.938], [0, 58.904999999999994, 88.06, 78.306, 92.61999999999999], [0, 129.11499999999998, 158.86499999999998, 111.14399999999999, 125.458], [0, 286.195, 327.84499999999997, 111.14399999999999, 125.458], [0, 129.11499999999998, 185.045, 132.194, 146.50799999999998], [0, 286.195, 394.48499999999996, 132.194, 146.50799999999998], [0, 129.11499999999998, 196.945, 153.244, 167.558], [0, 286.195, 467.075, 153.244, 167.558], [0, 129.11499999999998, 196.945, 174.29399999999998, 188.608], [0, 368.9, 467.075, 174.29399999999998, 188.608], [0, 129.11499999999998, 196.945, 196.186, 210.5], [0, 286.195, 417.69, 196.186, 210.5], [0, 63.665, 257.635, 230.708, 245.864], [0, 63.665, 517.65, 250.07399999999998, 264.388], [0, 63.665, 511.7, 268.598, 283.75399999999996], [0, 63.665, 443.87, 287.122, 302.27799999999996], [0, 63.665, 517.65, 305.646, 319.96], [0, 63.665, 511.7, 324.17, 338.484], [0, 63.665, 474.81, 341.852, 357.008], [0, 63.665, 517.65, 360.376, 375.532], [0, 63.665, 517.65, 378.9, 394.056], [0, 63.665, 517.65, 397.424, 412.58], [0, 63.665, 218.36499999999998, 415.106, 429.41999999999996], [0, 63.665, 517.65, 432.788, 447.94399999999996], [0, 63.665, 517.65, 451.312, 466.46799999999996], [0, 63.665, 517.65, 468.99399999999997, 484.15], [0, 63.665, 107.1, 487.518, 501.832], [0, 63.665, 514.0799999999999, 506.042, 520.356], [0, 63.665, 517.65, 524.566, 538.88], [0, 63.665, 452.2, 542.2479999999999, 557.404], [0, 63.665, 517.65, 560.7719999999999, 575.928], [0, 63.665, 517.65, 579.2959999999999, 593.61], [0, 63.665, 397.46, 597.8199999999999, 612.134], [0, 63.665, 228.48, 614.66, 629.816], [0, 63.665, 517.65, 633.184, 648.34], [0, 63.665, 349.85999999999996, 651.708, 666.0219999999999], [0, 267.155, 315.945, 670.232, 684.5459999999999], [0, 77.35, 514.675, 688.756, 703.0699999999999], [0, 66.045, 105.91, 707.28, 720.752], [0, 63.665, 517.65, 723.278, 738.434], [0, 66.045, 252.875, 740.9599999999999, 756.116], [0, 486.71, 517.65, 765.3779999999999, 778.85], [1, 112.455, 146.37, 21.892, 30.311999999999998], [1, 246.92499999999998, 323.68, 21.892, 41.257999999999996], [1, 408.765, 449.22499999999997, 21.05, 34.522], [1, 59.5, 89.25, 44.626, 58.098], [1, 408.765, 443.275, 43.784, 57.256], [1, 64.855, 511.7, 76.622, 90.93599999999999], [1, 64.855, 470.04999999999995, 94.304, 107.776], [1, 64.855, 511.7, 111.98599999999999, 125.458], [1, 64.855, 517.055, 129.668, 143.14], [1, 64.855, 517.65, 146.50799999999998, 160.822], [1, 64.855, 517.055, 164.19, 178.504], [1, 64.855, 517.65, 181.87199999999999, 196.186], [1, 64.855, 270.13, 200.396, 214.70999999999998], [1, 64.855, 517.65, 218.92, 233.23399999999998], [1, 64.855, 397.46, 236.602, 250.916], [1, 64.855, 439.10999999999996, 255.126, 269.44], [1, 64.855, 517.65, 273.65, 287.964], [1, 64.855, 517.65, 291.332, 305.646], [1, 64.855, 210.63, 309.856, 324.17], [1, 64.855, 517.65, 328.38, 342.69399999999996], [1, 64.855, 475.405, 346.062, 360.376], [1, 64.855, 486.71, 364.586, 378.9], [1, 64.855, 517.055, 383.11, 397.424], [1, 64.855, 517.65, 400.792, 415.106], [1, 64.855, 517.055, 418.474, 432.788], [1, 64.855, 245.14, 436.156, 450.46999999999997], [1, 64.855, 324.275, 454.68, 468.99399999999997], [1, 64.855, 517.65, 473.204, 487.518], [1, 64.855, 445.06, 490.88599999999997, 505.2], [1, 64.855, 511.7, 509.40999999999997, 523.7239999999999], [1, 64.855, 511.7, 527.092, 541.406], [1, 64.855, 440.29999999999995, 544.774, 559.93], [1, 266.56, 315.34999999999997, 563.298, 577.612], [1, 265.965, 315.34999999999997, 618.87, 633.184], [1, 64.855, 517.65, 637.394, 651.708], [1, 64.855, 468.85999999999996, 655.076, 669.39], [1, 64.855, 517.055, 673.6, 687.914], [1, 64.855, 468.85999999999996, 691.2819999999999, 705.596], [1, 486.71, 517.65, 724.962, 738.434], [2, 113.05, 147.56, 143.14, 151.56], [2, 249.89999999999998, 327.25, 143.14, 162.506], [2, 411.145, 452.2, 142.298, 156.612], [2, 59.5, 89.25, 164.19, 177.662], [2, 411.145, 446.25, 164.19, 177.662], [2, 269.53499999999997, 317.72999999999996, 216.394, 230.708], [2, 280.245, 351.645, 235.76, 249.232], [2, 280.245, 411.74, 271.12399999999997, 285.438], [2, 400.435, 448.63, 293.858, 307.33], [2, 275.485, 324.275, 331.748, 346.062], [2, 410.54999999999995, 506.94, 331.748, 346.062], [2, 190.39999999999998, 370.09, 351.95599999999996, 366.27], [2, 190.39999999999998, 275.485, 379.74199999999996, 393.214], [2, 190.39999999999998, 275.485, 379.74199999999996, 393.214]]
2026-08-10 17:45:46,953 INFO     29 [qwen-vl-text] ═══ DONE ═══ 96 positions, pages=3, time=54.6s
2026-08-10 17:45:46,972 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 17:45:46,973 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:45:46,973 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 17:45:46,973 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:45:46.973+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:45:46,980 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:45:46,981 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:45:46,981 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:45:46,981 INFO     29 [qwen-vl-text] positions(28): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:45:46,981 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [28]
2026-08-10 17:45:47,113 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 17:45:47,114 INFO     29 [qwen-vl-text] LLM extraction start, text_len=321
2026-08-10 17:45:47,114 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:45:47,115 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 223, \"bbox_end\": 250, \"encounter_dates\": [\"2020-12-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "门诊号：-\n姓名\n性别\n男\n年龄\n70岁\n病人编号\n病区\n病案号\n门诊号\n送检科室\n送检单位\n送检医生\n标本名称\n左侧隆突粘膜、左肺BALF等\n临床诊断\n肺部阴影\n病理诊断\n(左侧隆突粘膜)非小细胞肺癌，结合免疫组化结果，符合腺癌；\n(左肺BALF)细胞蜡块内发现少量恶性肿瘤细胞；\n(左肺BALF)涂片内未发现恶性肿瘤细胞；\n(痰)涂片内发现少量可疑恶性肿瘤细胞。\n免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。\n报告医生\n复诊医生\n报告时间\n2020-12-25\n12:51",
    "role": "user"
  }
]
2026-08-10 17:45:49,812 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:45:49,812 INFO     29 [qwen-vl-text] LLM output (len=522):
{
  "exam_date": null,
  "report_date": "2020-12-25",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "左侧隆突粘膜、左肺BALF等",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": null,
  "conclusion": "(左侧隆突粘膜)非小细胞肺癌，结合免疫组化结果，符合腺癌；\n(左肺BALF)细胞蜡块内发现少量恶性肿瘤细胞；\n(左肺BALF)涂片内未发现恶性肿瘤细胞；\n(痰)涂片内发现少量可疑恶性肿瘤细胞。\n免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:45:49,814 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1044595, prompt_len=1018
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["门诊号：-", "姓名", "性别", "男", "年龄", "70岁", "病人编号", "病区", "病案号", "门诊号", "送检科室", "送检单位", "送检医生", "标本名称", "左侧隆突粘膜、左肺BALF等", "临床诊断", "肺部阴影", "病理诊断", "(左侧隆突粘膜)非小细胞肺癌，结合免疫组化结果，符合腺癌；", "(左肺BALF)细胞蜡块内发现少量恶性肿瘤细胞；", "(左肺BALF)涂片内未发现恶性肿瘤细胞；", "(痰)涂片内发现少量可疑恶性肿瘤细胞。", "免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。", "报告医生", "复诊医生", "报告时间", "2020-12-25", "12:51"]

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
2026-08-10 17:46:02,580 INFO     29 [qwen-vl-text] coord API raw response (len=2366):
[
	{"text": "门诊号：-", "bbox": [818, 278, 866, 294]},
	{"text": "姓名", "bbox": [106, 337, 126, 351], "bbox": [106, 337, 126, 351]},
	{"text": "性别", "bbox": [325, 337, 347, 351], "bbox": [325, 337, 347, 351]},
	{"text": "男", "bbox": [410, 337, 420, 351], "bbox": [410, 337, 420, 351]},
	{"text": "年龄", "bbox": [545, 337, 565, 351], "bbox": [545, 337, 565, 351]},
	{"text": "70岁", "bbox": [630, 337, 648, 351], "bbox": [630, 337, 648, 351]},
	{"text": "病人编号", "bbox": [765, 337, 800, 351], "bbox": [765, 337, 800, 351]},
	{"text": "病区", "bbox": [106, 354, 126, 368], "bbox": [106, 354, 126, 368]},
	{"text": "病案号", "bbox": [325, 354, 358, 368], "bbox": [325, 354, 358, 368]},
	{"text": "门诊号", "bbox": [545, 354, 576, 368], "bbox": [545, 354, 576, 368]},
	{"text": "送检科室", "bbox": [106, 370, 140, 384], "bbox": [106, 370, 140, 384]},
	{"text": "送检单位", "bbox": [325, 370, 361, 384], "bbox": [325, 370, 361, 384]},
	{"text": "送检医生", "bbox": [545, 370, 579, 384], "bbox": [545, 370, 579, 384]},
	{"text": "标本名称", "bbox": [106, 387, 140, 400], "bbox": [106, 387, 140, 400]},
	{"text": "左侧隆突粘膜、左肺BALF等", "bbox": [189, 387, 295, 400], "bbox": [189, 387, 295, 400]},
	{"text": "临床诊断", "bbox": [106, 403, 140, 417], "bbox": [106, 403, 140, 417]},
	{"text": "肺部阴影", "bbox": [189, 403, 224, 417], "bbox": [189, 403, 224, 417]},
	{"text": "病理诊断", "bbox": [106, 424, 140, 437], "bbox": [106, 424, 140, 437]},
	{"text": "(左侧隆突粘膜)非小细胞肺癌，结合免疫组化结果，符合腺癌；", "bbox": [110, 440, 344, 454], "bbox": [110, 440, 344, 454]},
	{"text": "(左肺BALF)细胞蜡块内发现少量恶性肿瘤细胞；", "bbox": [110, 454, 290, 468], "bbox": [110, 454, 290, 468]},
	{"text": "(左肺BALF)涂片内未发现恶性肿瘤细胞；", "bbox": [110, 468, 264, 481], "bbox": [110, 468, 264, 481]},
	{"text": "(痰)涂片内发现少量可疑恶性肿瘤细胞。", "bbox": [110, 481, 261, 494], "bbox": [110, 481, 261, 494]},
	{"text": "免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。", "bbox": [106, 494, 726, 507], "bbox": [106, 494, 726, 507]},
	{"text": "报告医生", "bbox": [106, 522, 140, 535], "bbox": [106, 522, 140, 535]},
	{"text": "复诊医生", "bbox": [436, 522, 471, 535], "bbox": [436, 522, 471, 535]},
	{"text": "报告时间", "bbox": [600, 522, 634, 535], "bbox": [600, 522, 634, 535]},
	{"text": "2020-12-25", "bbox": [676, 524, 719, 535], "bbox": [676, 524, 719, 535]},
	{"text": "12:51", "bbox": [956, 874, 975, 885], "bbox": [956, 874, 975, 885]}
]
2026-08-10 17:46:02,580 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=12.8s
2026-08-10 17:46:02,580 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号：-, bbox=[818, 278, 866, 294]
2026-08-10 17:46:02,580 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[106, 337, 126, 351]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[2]: text=性别, bbox=[325, 337, 347, 351]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[3]: text=男, bbox=[410, 337, 420, 351]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[4]: text=年龄, bbox=[545, 337, 565, 351]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[5]: text=70岁, bbox=[630, 337, 648, 351]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[6]: text=病人编号, bbox=[765, 337, 800, 351]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[7]: text=病区, bbox=[106, 354, 126, 368]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[8]: text=病案号, bbox=[325, 354, 358, 368]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[9]: text=门诊号, bbox=[545, 354, 576, 368]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[10]: text=送检科室, bbox=[106, 370, 140, 384]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[11]: text=送检单位, bbox=[325, 370, 361, 384]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[12]: text=送检医生, bbox=[545, 370, 579, 384]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[13]: text=标本名称, bbox=[106, 387, 140, 400]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[14]: text=左侧隆突粘膜、左肺BALF等, bbox=[189, 387, 295, 400]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[15]: text=临床诊断, bbox=[106, 403, 140, 417]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[16]: text=肺部阴影, bbox=[189, 403, 224, 417]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[17]: text=病理诊断, bbox=[106, 424, 140, 437]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[18]: text=(左侧隆突粘膜)非小细胞肺癌，结合免疫组化结果，符合腺癌；, bbox=[110, 440, 344, 454]
2026-08-10 17:46:02,581 INFO     29 [qwen-vl-text] coord item[19]: text=(左肺BALF)细胞蜡块内发现少量恶性肿瘤细胞；, bbox=[110, 454, 290, 468]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] coord item[20]: text=(左肺BALF)涂片内未发现恶性肿瘤细胞；, bbox=[110, 468, 264, 481]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] coord item[21]: text=(痰)涂片内发现少量可疑恶性肿瘤细胞。, bbox=[110, 481, 261, 494]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] coord item[22]: text=免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。, bbox=[106, 494, 726, 507]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] coord item[23]: text=报告医生, bbox=[106, 522, 140, 535]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] coord item[24]: text=复诊医生, bbox=[436, 522, 471, 535]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] coord item[25]: text=报告时间, bbox=[600, 522, 634, 535]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] coord item[26]: text=2020-12-25, bbox=[676, 524, 719, 535]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] coord item[27]: text=12:51, bbox=[956, 874, 975, 885]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] page=6 — 28/28 coords, api_time=12.8s
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] new_positions (28):
[[6, 688.756, 729.172, 165.41, 174.92999999999998], [6, 89.252, 106.092, 200.515, 208.845], [6, 273.65, 292.174, 200.515, 208.845], [6, 345.21999999999997, 353.64, 200.515, 208.845], [6, 458.89, 475.72999999999996, 200.515, 208.845], [6, 530.46, 545.616, 200.515, 208.845], [6, 644.13, 673.6, 200.515, 208.845], [6, 89.252, 106.092, 210.63, 218.95999999999998], [6, 273.65, 301.436, 210.63, 218.95999999999998], [6, 458.89, 484.99199999999996, 210.63, 218.95999999999998], [6, 89.252, 117.88, 220.14999999999998, 228.48], [6, 273.65, 303.962, 220.14999999999998, 228.48], [6, 458.89, 487.518, 220.14999999999998, 228.48], [6, 89.252, 117.88, 230.265, 238.0], [6, 159.138, 248.39, 230.265, 238.0], [6, 89.252, 117.88, 239.785, 248.11499999999998], [6, 159.138, 188.608, 239.785, 248.11499999999998], [6, 89.252, 117.88, 252.28, 260.015], [6, 92.61999999999999, 289.64799999999997, 261.8, 270.13], [6, 92.61999999999999, 244.17999999999998, 270.13, 278.46], [6, 92.61999999999999, 222.28799999999998, 278.46, 286.195], [6, 92.61999999999999, 219.762, 286.195, 293.93], [6, 89.252, 611.292, 293.93, 301.66499999999996], [6, 89.252, 117.88, 310.59, 318.325], [6, 367.11199999999997, 396.582, 310.59, 318.325], [6, 505.2, 533.828, 310.59, 318.325], [6, 569.192, 605.398, 311.78, 318.325], [6, 804.952, 820.9499999999999, 520.03, 526.5749999999999]]
2026-08-10 17:46:02,582 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=15.6s
2026-08-10 17:46:02,583 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:46:02,584 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:46:02,584 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:46:02,584 INFO     29 [qwen-vl-text] positions(23): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:46:02,585 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [23]
2026-08-10 17:46:02,702 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 17:46:02,702 INFO     29 [qwen-vl-text] LLM extraction start, text_len=161
2026-08-10 17:46:02,703 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:46:02,703 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 279, \"bbox_end\": 301, \"encounter_dates\": [\"2020-12-29\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "病理号\n住院\n门诊号\n1-1]\n姓名\n70岁\n病人编号\n0007\n病区\n门诊号\n送检科室\n送检医生\n标本名称\n左侧隆突粘膜、左肺BALF等\n临床诊断\n肺部阴影\n病理诊断\n2020.12.20加做免疫结果：PD-L1-22C3（+，TPS约30%）\n报告医生\n报告时间\n2020-12-29\n12:51\n2026-03-02",
    "role": "user"
  }
]
2026-08-10 17:46:06,880 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:46:06,880 INFO     29 [qwen-vl-text] LLM output (len=363):
{
  "exam_date": "2020-12-20",
  "report_date": "2020-12-29",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "左侧隆突粘膜、左肺BALF等",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": null,
  "conclusion": "2020.12.20加做免疫结果：PD-L1-22C3（+，TPS约30%）",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:46:06,881 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=781833, prompt_len=843
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["病理号", "住院", "门诊号", "1-1]", "姓名", "70岁", "病人编号", "0007", "病区", "门诊号", "送检科室", "送检医生", "标本名称", "左侧隆突粘膜、左肺BALF等", "临床诊断", "肺部阴影", "病理诊断", "2020.12.20加做免疫结果：PD-L1-22C3（+，TPS约30%）", "报告医生", "报告时间", "2020-12-29", "12:51", "2026-03-02"]

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
2026-08-10 17:46:13,582 INFO     29 [qwen-vl-text] coord API raw response (len=1176):
[
	{"text": "病理号", "bbox": [246, 277, 280, 294]},
	{"text": "住院", "bbox": [524, 277, 548, 294]},
	{"text": "门诊号", "bbox": [816, 277, 852, 294]},
	{"text": "1-1]", "bbox": [614, 311, 635, 329]},
	{"text": "姓名", "bbox": [106, 336, 126, 350]},
	{"text": "70岁", "bbox": [628, 337, 647, 350]},
	{"text": "病人编号", "bbox": [764, 337, 799, 350]},
	{"text": "0007", "bbox": [848, 338, 870, 349]},
	{"text": "病区", "bbox": [106, 353, 126, 367]},
	{"text": "门诊号", "bbox": [544, 353, 575, 367]},
	{"text": "送检科室", "bbox": [106, 369, 138, 383]},
	{"text": "送检医生", "bbox": [544, 370, 578, 383]},
	{"text": "标本名称", "bbox": [106, 385, 139, 399]},
	{"text": "左侧隆突粘膜、左肺BALF等", "bbox": [189, 385, 294, 399]},
	{"text": "临床诊断", "bbox": [106, 401, 139, 415]},
	{"text": "肺部阴影", "bbox": [189, 401, 222, 415]},
	{"text": "病理诊断", "bbox": [106, 421, 139, 435]},
	{"text": "2020.12.20加做免疫结果：PD-L1-22C3（+，TPS约30%）", "bbox": [106, 438, 327, 452]},
	{"text": "报告医生", "bbox": [106, 466, 138, 480]},
	{"text": "报告时间", "bbox": [598, 467, 633, 480]},
	{"text": "2020-12-29", "bbox": [674, 470, 718, 480]},
	{"text": "12:51", "bbox": [956, 867, 975, 878]},
	{"text": "2026-03-02", "bbox": [945, 882, 986, 893]}
]
2026-08-10 17:46:13,583 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=6.7s
2026-08-10 17:46:13,583 INFO     29 [qwen-vl-text] coord item[0]: text=病理号, bbox=[246, 277, 280, 294]
2026-08-10 17:46:13,583 INFO     29 [qwen-vl-text] coord item[1]: text=住院, bbox=[524, 277, 548, 294]
2026-08-10 17:46:13,583 INFO     29 [qwen-vl-text] coord item[2]: text=门诊号, bbox=[816, 277, 852, 294]
2026-08-10 17:46:13,583 INFO     29 [qwen-vl-text] coord item[3]: text=1-1], bbox=[614, 311, 635, 329]
2026-08-10 17:46:13,583 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[106, 336, 126, 350]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[5]: text=70岁, bbox=[628, 337, 647, 350]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[6]: text=病人编号, bbox=[764, 337, 799, 350]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[7]: text=0007, bbox=[848, 338, 870, 349]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[8]: text=病区, bbox=[106, 353, 126, 367]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[9]: text=门诊号, bbox=[544, 353, 575, 367]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[10]: text=送检科室, bbox=[106, 369, 138, 383]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[11]: text=送检医生, bbox=[544, 370, 578, 383]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[12]: text=标本名称, bbox=[106, 385, 139, 399]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[13]: text=左侧隆突粘膜、左肺BALF等, bbox=[189, 385, 294, 399]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[14]: text=临床诊断, bbox=[106, 401, 139, 415]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[15]: text=肺部阴影, bbox=[189, 401, 222, 415]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[16]: text=病理诊断, bbox=[106, 421, 139, 435]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[17]: text=2020.12.20加做免疫结果：PD-L1-22C3（+，TPS约30%）, bbox=[106, 438, 327, 452]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[18]: text=报告医生, bbox=[106, 466, 138, 480]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[19]: text=报告时间, bbox=[598, 467, 633, 480]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[20]: text=2020-12-29, bbox=[674, 470, 718, 480]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[21]: text=12:51, bbox=[956, 867, 975, 878]
2026-08-10 17:46:13,584 INFO     29 [qwen-vl-text] coord item[22]: text=2026-03-02, bbox=[945, 882, 986, 893]
2026-08-10 17:46:13,585 INFO     29 [qwen-vl-text] page=7 — 23/23 coords, api_time=6.7s
2026-08-10 17:46:13,585 INFO     29 [qwen-vl-text] new_positions (23):
[[7, 207.132, 235.76, 164.815, 174.92999999999998], [7, 441.20799999999997, 461.416, 164.815, 174.92999999999998], [7, 687.072, 717.384, 164.815, 174.92999999999998], [7, 516.9879999999999, 534.67, 185.045, 195.755], [7, 89.252, 106.092, 199.92, 208.25], [7, 528.776, 544.774, 200.515, 208.25], [7, 643.288, 672.7579999999999, 200.515, 208.25], [7, 714.016, 732.54, 201.10999999999999, 207.655], [7, 89.252, 106.092, 210.035, 218.36499999999998], [7, 458.048, 484.15, 210.035, 218.36499999999998], [7, 89.252, 116.196, 219.55499999999998, 227.885], [7, 458.048, 486.676, 220.14999999999998, 227.885], [7, 89.252, 117.038, 229.075, 237.405], [7, 159.138, 247.548, 229.075, 237.405], [7, 89.252, 117.038, 238.595, 246.92499999999998], [7, 159.138, 186.924, 238.595, 246.92499999999998], [7, 89.252, 117.038, 250.49499999999998, 258.825], [7, 89.252, 275.334, 260.61, 268.94], [7, 89.252, 116.196, 277.27, 285.59999999999997], [7, 503.51599999999996, 532.986, 277.865, 285.59999999999997], [7, 567.5079999999999, 604.5559999999999, 279.65, 285.59999999999997], [7, 804.952, 820.9499999999999, 515.865, 522.41], [7, 795.6899999999999, 830.212, 524.79, 531.3349999999999]]
2026-08-10 17:46:13,585 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=11.0s
2026-08-10 17:46:13,585 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:46:13,587 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:46:13,587 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:46:13,587 INFO     29 [qwen-vl-text] positions(15): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:46:13,587 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [15]
2026-08-10 17:46:13,705 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 17:46:13,705 INFO     29 [qwen-vl-text] LLM extraction start, text_len=127
2026-08-10 17:46:13,706 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:46:13,706 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3588, \"bbox_end\": 3602, \"encounter_dates\": [\"2026-01-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "门楼号\n姓名\n病区\n送检科室\n标本名称\n临床诊断\n内眼所见\n穿刺组织3条，合计长0.6cm。\n病理诊断\n(左肺组织穿刺活检）非小细胞肺癌伴大片坏死，待免疫组化。\n报告医生\n审核医生\n报告时间\n2026-01-28 14:53\n点击要返回的Pah:QC流程",
    "role": "user"
  }
]
2026-08-10 17:46:15,674 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:46:15,675 INFO     29 [qwen-vl-text] LLM output (len=359):
{
  "exam_date": null,
  "report_date": "2026-01-28",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "内眼所见\n穿刺组织3条，合计长0.6cm。",
  "conclusion": "病理诊断\n(左肺组织穿刺活检）非小细胞肺癌伴大片坏死，待免疫组化。",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:46:15,676 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=825431, prompt_len=785
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共15行）
["门楼号", "姓名", "病区", "送检科室", "标本名称", "临床诊断", "内眼所见", "穿刺组织3条，合计长0.6cm。", "病理诊断", "(左肺组织穿刺活检）非小细胞肺癌伴大片坏死，待免疫组化。", "报告医生", "审核医生", "报告时间", "2026-01-28 14:53", "点击要返回的Pah:QC流程"]

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
2026-08-10 17:46:20,510 INFO     29 [qwen-vl-text] coord API raw response (len=780):
[
	{"text": "门楼号", "bbox": [812, 277, 850, 292]},
	{"text": "姓名", "bbox": [91, 335, 112, 348]},
	{"text": "病区", "bbox": [91, 352, 112, 365]},
	{"text": "送检科室", "bbox": [91, 368, 125, 381]},
	{"text": "标本名称", "bbox": [91, 384, 125, 397]},
	{"text": "临床诊断", "bbox": [91, 400, 125, 413]},
	{"text": "内眼所见", "bbox": [91, 420, 125, 433]},
	{"text": "穿刺组织3条，合计长0.6cm。", "bbox": [91, 438, 197, 451]},
	{"text": "病理诊断", "bbox": [91, 461, 125, 474]},
	{"text": "(左肺组织穿刺活检）非小细胞肺癌伴大片坏死，待免疫组化。", "bbox": [94, 477, 322, 491]},
	{"text": "报告医生", "bbox": [91, 507, 125, 520]},
	{"text": "审核医生", "bbox": [425, 507, 459, 520]},
	{"text": "报告时间", "bbox": [590, 507, 624, 520]},
	{"text": "2026-01-28 14:53", "bbox": [667, 510, 734, 520]},
	{"text": "点击要返回的Pah:QC流程", "bbox": [476, 845, 579, 859]}
]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord API: raw_items=15, valid_items=15, elapsed=4.8s
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[0]: text=门楼号, bbox=[812, 277, 850, 292]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[91, 335, 112, 348]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[2]: text=病区, bbox=[91, 352, 112, 365]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[3]: text=送检科室, bbox=[91, 368, 125, 381]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[4]: text=标本名称, bbox=[91, 384, 125, 397]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[5]: text=临床诊断, bbox=[91, 400, 125, 413]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[6]: text=内眼所见, bbox=[91, 420, 125, 433]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[7]: text=穿刺组织3条，合计长0.6cm。, bbox=[91, 438, 197, 451]
2026-08-10 17:46:20,511 INFO     29 [qwen-vl-text] coord item[8]: text=病理诊断, bbox=[91, 461, 125, 474]
2026-08-10 17:46:20,512 INFO     29 [qwen-vl-text] coord item[9]: text=(左肺组织穿刺活检）非小细胞肺癌伴大片坏死，待免疫组化。, bbox=[94, 477, 322, 491]
2026-08-10 17:46:20,512 INFO     29 [qwen-vl-text] coord item[10]: text=报告医生, bbox=[91, 507, 125, 520]
2026-08-10 17:46:20,512 INFO     29 [qwen-vl-text] coord item[11]: text=审核医生, bbox=[425, 507, 459, 520]
2026-08-10 17:46:20,512 INFO     29 [qwen-vl-text] coord item[12]: text=报告时间, bbox=[590, 507, 624, 520]
2026-08-10 17:46:20,512 INFO     29 [qwen-vl-text] coord item[13]: text=2026-01-28 14:53, bbox=[667, 510, 734, 520]
2026-08-10 17:46:20,512 INFO     29 [qwen-vl-text] coord item[14]: text=点击要返回的Pah:QC流程, bbox=[476, 845, 579, 859]
2026-08-10 17:46:20,512 INFO     29 [qwen-vl-text] page=9 — 15/15 coords, api_time=4.8s
2026-08-10 17:46:20,513 INFO     29 [qwen-vl-text] new_positions (15):
[[9, 683.704, 715.6999999999999, 164.815, 173.73999999999998], [9, 76.622, 94.304, 199.325, 207.06], [9, 76.622, 94.304, 209.44, 217.17499999999998], [9, 76.622, 105.25, 218.95999999999998, 226.695], [9, 76.622, 105.25, 228.48, 236.215], [9, 76.622, 105.25, 238.0, 245.73499999999999], [9, 76.622, 105.25, 249.89999999999998, 257.635], [9, 76.622, 165.874, 260.61, 268.34499999999997], [9, 76.622, 105.25, 274.295, 282.03], [9, 79.148, 271.12399999999997, 283.815, 292.145], [9, 76.622, 105.25, 301.66499999999996, 309.4], [9, 357.84999999999997, 386.478, 301.66499999999996, 309.4], [9, 496.78, 525.408, 301.66499999999996, 309.4], [9, 561.614, 618.028, 303.45, 309.4], [9, 400.792, 487.518, 502.775, 511.10499999999996]]
2026-08-10 17:46:20,513 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=1, time=6.9s
2026-08-10 17:46:20,513 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:46:20,520 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:46:20,521 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:46:20,521 INFO     29 [qwen-vl-text] positions(28): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:46:20,521 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [28]
2026-08-10 17:46:20,635 INFO     29 [qwen-vl-text] page=10, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 17:46:20,635 INFO     29 [qwen-vl-text] LLM extraction start, text_len=268
2026-08-10 17:46:20,636 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:46:20,636 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3632, \"bbox_end\": 3659, \"encounter_dates\": [\"2026-01-30\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "门诊号：\n姓名\n性别\n75岁\n病人编\n病区\n病区\n病案号\n门诊号\n送检科室\n送检单位\n送检医生\n丁晓倩\n标本名称\n左肺组织穿刺活检\n临床诊断\n1.肺恶性肿瘤2.肺恶性肿瘤\n病理诊断\n(左肺组织穿刺活检)肺小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合肺癌。\n免疫组化示肿瘤细胞：CKpan（+），CK7（+），TTF-1（+），p40（-），CK5/6（-）；\n特殊染色：D-PAS（-）。\n报告医生\n医生\n报告时间\n2026-01-30 11:19\n欢迎使用朗珈PathQC病理质控与资料管理系统！\n12:51\n2026-01-02",
    "role": "user"
  }
]
2026-08-10 17:46:20,638 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:46:20.637+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:46:22,522 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:46:22,522 INFO     29 [qwen-vl-text] LLM output (len=421):
{
  "exam_date": "2026-01-02",
  "report_date": "2026-01-30",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": null,
  "conclusion": "(左肺组织穿刺活检)肺小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合肺癌。\n免疫组化示肿瘤细胞：CKpan（+），CK7（+），TTF-1（+），p40（-），CK5/6（-）；\n特殊染色：D-PAS（-）。",
  "physician": "丁晓倩",
  "reviewer": null
}
2026-08-10 17:46:22,523 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871740, prompt_len=965
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["门诊号：", "姓名", "性别", "75岁", "病人编", "病区", "病区", "病案号", "门诊号", "送检科室", "送检单位", "送检医生", "丁晓倩", "标本名称", "左肺组织穿刺活检", "临床诊断", "1.肺恶性肿瘤2.肺恶性肿瘤", "病理诊断", "(左肺组织穿刺活检)肺小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合肺癌。", "免疫组化示肿瘤细胞：CKpan（+），CK7（+），TTF-1（+），p40（-），CK5/6（-）；", "特殊染色：D-PAS（-）。", "报告医生", "医生", "报告时间", "2026-01-30 11:19", "欢迎使用朗珈PathQC病理质控与资料管理系统！", "12:51", "2026-01-02"]

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
2026-08-10 17:46:35,026 INFO     29 [qwen-vl-text] coord API raw response (len=2325):
```json
[
	{"text": "门诊号：", "bbox": [823, 286, 871, 302]},
	{"text": "姓名", "bbox": [141, 341, 161, 355], "bbox": [141, 341, 161, 355]},
	{"text": "性别", "bbox": [353, 341, 374, 355], "bbox": [353, 341, 374, 355]},
	{"text": "75岁", "bbox": [645, 341, 662, 355], "bbox": [645, 341, 662, 355]},
	{"text": "病人编", "bbox": [774, 341, 800, 355], "bbox": [774, 341, 800, 355]},
	{"text": "病区", "bbox": [141, 357, 161, 370], "bbox": [141, 357, 161, 370]},
	{"text": "病区", "bbox": [321, 357, 337, 370], "bbox": [321, 357, 337, 370]},
	{"text": "病案号", "bbox": [353, 357, 384, 370], "bbox": [353, 357, 384, 370]},
	{"text": "门诊号", "bbox": [565, 357, 594, 370], "bbox": [565, 357, 594, 370]},
	{"text": "送检科室", "bbox": [141, 373, 173, 386], "bbox": [141, 373, 173, 386]},
	{"text": "送检单位", "bbox": [353, 373, 387, 386], "bbox": [353, 373, 387, 386]},
	{"text": "送检医生", "bbox": [565, 373, 597, 386], "bbox": [565, 373, 597, 386]},
	{"text": "丁晓倩", "bbox": [645, 373, 669, 386], "bbox": [645, 373, 669, 386]},
	{"text": "标本名称", "bbox": [141, 389, 173, 402], "bbox": [141, 389, 173, 402]},
	{"text": "左肺组织穿刺活检", "bbox": [222, 389, 288, 402], "bbox": [222, 389, 288, 402]},
	{"text": "临床诊断", "bbox": [141, 404, 173, 417], "bbox": [141, 404, 173, 417]},
	{"text": "1.肺恶性肿瘤2.肺恶性肿瘤", "bbox": [222, 404, 321, 417], "bbox": [222, 404, 321, 417]},
	{"text": "病理诊断", "bbox": [141, 423, 173, 436], "bbox": [141, 423, 173, 436]},
	{"text": "(左肺组织穿刺活检)肺小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合肺癌。", "bbox": [141, 439, 443, 452], "bbox": [141, 439, 443, 452]},
	{"text": "免疫组化示肿瘤细胞：CKpan（+），CK7（+），TTF-1（+），p40（-），CK5/6（-）；", "bbox": [141, 452, 455, 465], "bbox": [141, 452, 455, 465]},
	{"text": "特殊染色：D-PAS（-）。", "bbox": [141, 465, 227, 478], "bbox": [141, 465, 227, 478]},
	{"text": "报告医生", "bbox": [141, 491, 173, 504], "bbox": [141, 491, 173, 504]},
	{"text": "医生", "bbox": [475, 491, 492, 504], "bbox": [475, 491, 492, 504]},
	{"text": "报告时间", "bbox": [615, 491, 648, 504], "bbox": [615, 491, 648, 504]},
	{"text": "2026-01-30 11:19", "bbox": [688, 493, 752, 504], "bbox": [688, 493, 752, 504]},
	{"text": "欢迎使用朗珈PathQC病理质控与资料管理系统！", "bbox": [365, 829, 545, 843], "bbox": [365, 829, 545, 843]},
	{"text": "12:51", "bbox": [957, 851, 975, 862], "bbox": [957, 851, 975, 862]},
	{"text": "2026-01-02", "bbox": [947, 865, 986, 875], "bbox": [947, 865, 986, 875]}
]
```
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=12.5s
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号：, bbox=[823, 286, 871, 302]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[141, 341, 161, 355]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[2]: text=性别, bbox=[353, 341, 374, 355]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[3]: text=75岁, bbox=[645, 341, 662, 355]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[4]: text=病人编, bbox=[774, 341, 800, 355]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[5]: text=病区, bbox=[141, 357, 161, 370]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[6]: text=病区, bbox=[321, 357, 337, 370]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[7]: text=病案号, bbox=[353, 357, 384, 370]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[8]: text=门诊号, bbox=[565, 357, 594, 370]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[9]: text=送检科室, bbox=[141, 373, 173, 386]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[10]: text=送检单位, bbox=[353, 373, 387, 386]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[11]: text=送检医生, bbox=[565, 373, 597, 386]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[12]: text=丁晓倩, bbox=[645, 373, 669, 386]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[13]: text=标本名称, bbox=[141, 389, 173, 402]
2026-08-10 17:46:35,027 INFO     29 [qwen-vl-text] coord item[14]: text=左肺组织穿刺活检, bbox=[222, 389, 288, 402]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[15]: text=临床诊断, bbox=[141, 404, 173, 417]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[16]: text=1.肺恶性肿瘤2.肺恶性肿瘤, bbox=[222, 404, 321, 417]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[17]: text=病理诊断, bbox=[141, 423, 173, 436]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[18]: text=(左肺组织穿刺活检)肺小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合肺癌。, bbox=[141, 439, 443, 452]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[19]: text=免疫组化示肿瘤细胞：CKpan（+），CK7（+），TTF-1（+），p40（-），CK5/6（-）；, bbox=[141, 452, 455, 465]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[20]: text=特殊染色：D-PAS（-）。, bbox=[141, 465, 227, 478]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[21]: text=报告医生, bbox=[141, 491, 173, 504]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[22]: text=医生, bbox=[475, 491, 492, 504]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[23]: text=报告时间, bbox=[615, 491, 648, 504]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[24]: text=2026-01-30 11:19, bbox=[688, 493, 752, 504]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[25]: text=欢迎使用朗珈PathQC病理质控与资料管理系统！, bbox=[365, 829, 545, 843]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[26]: text=12:51, bbox=[957, 851, 975, 862]
2026-08-10 17:46:35,028 INFO     29 [qwen-vl-text] coord item[27]: text=2026-01-02, bbox=[947, 865, 986, 875]
2026-08-10 17:46:35,029 INFO     29 [qwen-vl-text] page=10 — 28/28 coords, api_time=12.5s
2026-08-10 17:46:35,029 INFO     29 [qwen-vl-text] new_positions (28):
[[10, 692.966, 733.382, 170.17, 179.69], [10, 118.722, 135.56199999999998, 202.89499999999998, 211.225], [10, 297.226, 314.908, 202.89499999999998, 211.225], [10, 543.09, 557.404, 202.89499999999998, 211.225], [10, 651.708, 673.6, 202.89499999999998, 211.225], [10, 118.722, 135.56199999999998, 212.415, 220.14999999999998], [10, 270.282, 283.75399999999996, 212.415, 220.14999999999998], [10, 297.226, 323.328, 212.415, 220.14999999999998], [10, 475.72999999999996, 500.14799999999997, 212.415, 220.14999999999998], [10, 118.722, 145.666, 221.935, 229.67], [10, 297.226, 325.854, 221.935, 229.67], [10, 475.72999999999996, 502.674, 221.935, 229.67], [10, 543.09, 563.298, 221.935, 229.67], [10, 118.722, 145.666, 231.45499999999998, 239.19], [10, 186.924, 242.49599999999998, 231.45499999999998, 239.19], [10, 118.722, 145.666, 240.38, 248.11499999999998], [10, 186.924, 270.282, 240.38, 248.11499999999998], [10, 118.722, 145.666, 251.685, 259.42], [10, 118.722, 373.006, 261.205, 268.94], [10, 118.722, 383.11, 268.94, 276.675], [10, 118.722, 191.134, 276.675, 284.40999999999997], [10, 118.722, 145.666, 292.145, 299.88], [10, 399.95, 414.264, 292.145, 299.88], [10, 517.8299999999999, 545.616, 292.145, 299.88], [10, 579.2959999999999, 633.184, 293.335, 299.88], [10, 307.33, 458.89, 493.255, 501.585], [10, 805.794, 820.9499999999999, 506.34499999999997, 512.89], [10, 797.374, 830.212, 514.675, 520.625]]
2026-08-10 17:46:35,029 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=14.5s
2026-08-10 17:46:35,029 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:46:35,031 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:46:35,031 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:46:35,032 INFO     29 [qwen-vl-text] positions(141): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:46:35,032 INFO     29 [qwen-vl-text] page grouping: [11, 12, 13], lines per page: [48, 51, 42]
2026-08-10 17:46:35,162 INFO     29 [qwen-vl-text] page=11, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 17:46:36,143 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:46:37,589 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:46:37,590 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2563
2026-08-10 17:46:37,590 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:46:37,590 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3660, \"bbox_end\": 3800, \"encounter_dates\": [\"2026-02-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "病历\n姓名\n病区\n送检科室\n标本名称\n临床诊断\n病理诊断\n检查项目:肿瘤多基因检测(含MSI)\n检查方法:高通量测序(NGS)\n参考基因组:GRCh37/hg19\n临床数据库:1000 Genomes、ExAC、gnomAD、ClinVar、BRCA Exchange InSiGHT、DBSNP、Cancer Hotspots、COSMIC、JAX CKB、OncoKB等\n检测突变软件:ADXHS-Classic-H\n标本病理评估:肿瘤细胞占比30%。\nDNA质量评估:合格\n测序质量评估:合格\n表格结果:\n检测内容 检测结果 突变丰度 备注\nMSI MSS 0/55\nEGFR exon19 c.2235_2249del p.Glu746_Ala750del(E746_A750del) 29.59% I级,具有明确临床意义\nMET 扩增 3.97 I级,具有明确临床意义\nTP53 exon8 p.817C>T p.Arg273Cys(R273C) 6.35% II级,具有潜在临床意义\n检测结果备注:表格内未列出的为未检出。\n报告医生\n生\n报告时间\n2026-02-06 16:26\n住院号\n门诊号\n送检医生\n病人编号\n1份已审核\n2026-01-30 14:10:13\n4.0\n无\n2份已审核\n2026-01-28 09:16:53\n4.0\n55\n无\n1份已审核\n2020-12-28 12:02\n2.0\n58床\n无\n2020-12-21 14:02\n2.0\n58床\n无\n分子病理检查报告单\n编\n患者姓名\n性别：男\n年龄：75岁\n住院号：\n送检科室\n尿府理\n登记号：\n标本类型：石蜡组织\n病变部\n病理诊断：\n收到日期：2026-01-20\n检查项目：肿瘤多基因检测（含MSI）\n检查方法：高通量测序(NGS)\n参考基因组：GRCh37/hg19\n临床数据库：1000 Genomes、ExAC、gnomAD、ClinVar、BECA Exchange InSiGHT、DBSNP、\nCancer Hotspots、COSMIC、JAX CXB、OncoKB等\n检测突变软件：ADXHS-Classic-H\n标本病理评估：肿瘤细胞占比30%。\n核酸质量评估：合格\n测序质量评估：合格\n检测结果：\n检测内容\n检测结果\n突变丰度\n备注\nMSI\nMSS\n0/55\nEGFR\nexon19 c.2235_2249del\n29.59%\nI级、具有明确临床意义\np.Glu746_Ala750del (E746_A750del)\nMET\n3'端\n3.97\nI级、具有明确临床意义\nTP53\nexon6 c.817C>T p.Arg273Cys (R273C)\n6.35%\nII级、具有潜在临床意义\n备注：表格内未列出的为未检出。\n注：此报告仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与分子病理诊断科联系。\n报告.\n检测者\n报告日期：2026-02-06\n第1页/共16页\nCS 扫描全能王\n3亿人都在用的扫描App\nV2.0\n循环周期，调节转录，DNA 复\n制和诱导细胞程序死亡及抗血\n管生成。\n细胞瘤）和肾上腺皮质癌。TP53 突变还发生于包括 CML、\nANLL、MDS 及 B-NHL。在内的多种恶性血液肿瘤以及\n黑色素瘤、基底细胞癌、鳞状细胞癌等皮肤癌等多种类型\n肝癌及恶性肿瘤。TP53 突变是多种癌症预后不良的标\n志，如乳腺癌。TP53 基因变异与肿瘤细胞对铂类化疗药\n物耐药性相关，但不影响氟杉醇类药物的敏感性；相关化\n疗药物还包括喜树碱、5-FU、顺铂、环磷酰胺等。FDA 已\n授予 IXC14586 快速通道资格，目前治疗具有 TP53 Y220C\n突变的局部晚期或转移性实体瘤患者。\n四、声明告知\n1. 本检测项目中使用的参考基因组版本为 hg19，报告中的变异命名遵从 HGVS 指南\n(http://varnomcn.hgvs.org)中的相关规定进行命名。\n2. 变异分类：综合变异在治疗、诊断和预后方面相关研究证据，将变异分为 4 级：I\n级为明确临床意义；II 级为潜在临床意义；III 类为临床意义未明；IV 级为良性/可能良\n性。本报告中仅列出 I-III 级变异。\n3. 检测结果与临床意义相关性的证据水平分为 4 个等级（A/B/C/D）。A 级：对应\n病种中 FDA/NMPA 批准或指南推荐的治疗、诊断和（或）预后的相关标志物；B 级：专家\n共识或 III/IV 期临床试验研究表明对患者肿瘤治疗有敏感或耐药、或具有诊断、预后意义\n的生物标志物；C 级：FDA/NMPA 批准或专业指南推荐的在其他癌种对某个治疗方案敏感\n或耐药的标志物；或者是作为临床试验入组标准的标志物；或者是多个小型研究结果证实\n具有诊断或预后意义的标志物；D 级：临床前研究表明具有潜在的治疗意义，或基于小型\n研究或多个案例报告可能作为辅助疾病诊断或预后的标志物（结论未形成共识）。\n4. 本检测的检测内容大部分基于仅限于 DNA 水平，部分基因涉及 RNA 水平，但\n不涉及蛋白水平的检测。\n5. 对于组织样品，如样本中肿瘤细胞含量低于 20%，可能影响检测结果的准确性；\n如未检出指定的基因变异，可能由于该样本中该突变的丰度低于本项目的检测下限。\n6. 对于组织样品，肿瘤存在异质性，即不同病灶甚至同一病灶内的组织的突变图谱可\n能也存在差异；另外，不同疾病发展或治疗阶段取出的样本中的突变可能不同；因此，本\n检测报告仅对此次送检的样本负责。并且，所检测的突变位点仅限于本检测试剂的检测范\n围，样品的基因组中可能存在的某些罕见或复杂突变，本项目不能完全检测。\n7. 本报告对于测序结果分析中核苷酸改变的位置信息是基于当前版本的基因组和转录\n本，随着人类基因组的更新，这些信息可能会有所不同；同时对于突变位点的解读，是基\n于当前已发表的文献、指南、公共数据库及临床研究结果，随着研究的发展，特定位点的\n解读可能发生变更。\n8. 本检测仅为临床治疗或诊断提供参考，具体的诊断结果及治疗决策应由临床医生综\n合患者的各种临床信息和检测结果进行判断。\nCS 扫描全能王\n3 亿人都在用的扫描 App",
    "role": "user"
  }
]
2026-08-10 17:46:41,711 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:46:41,711 INFO     29 [qwen-vl-text] LLM output (len=705):
{
  "exam_date": "2026-01-20",
  "report_date": "2026-02-06",
  "exam_name": "肿瘤多基因检测（含MSI）",
  "exam_category": "pathology",
  "body_part": "石蜡组织",
  "patient_name": null,
  "patient_gender": "男",
  "department": "尿府理",
  "bed_number": "58床",
  "findings": "标本病理评估：肿瘤细胞占比30%。\n核酸质量评估：合格\n测序质量评估：合格",
  "conclusion": "检测结果：\n| 检测内容 | 检测结果 | 突变丰度 | 备注 |\n|---|---|---|---|\n| MSI | MSS | 0/55 | |\n| EGFR | exon19 c.2235_2249del p.Glu746_Ala750del (E746_A750del) | 29.59% | I级、具有明确临床意义 |\n| MET | 3'端 | 3.97 | I级、具有明确临床意义 |\n| TP53 | exon6 c.817C>T p.Arg273Cys (R273C) | 6.35% | II级、具有潜在临床意义 |\n\n备注：表格内未列出的为未检出。\n注：此报告仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与分子病理诊断科联系。",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:46:41,714 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1041998, prompt_len=1398
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共48行）
["病历", "姓名", "病区", "送检科室", "标本名称", "临床诊断", "病理诊断", "检查项目:肿瘤多基因检测(含MSI)", "检查方法:高通量测序(NGS)", "参考基因组:GRCh37/hg19", "临床数据库:1000 Genomes、ExAC、gnomAD、ClinVar、BRCA Exchange InSiGHT、DBSNP、Cancer Hotspots、COSMIC、JAX CKB、OncoKB等", "检测突变软件:ADXHS-Classic-H", "标本病理评估:肿瘤细胞占比30%。", "DNA质量评估:合格", "测序质量评估:合格", "表格结果:", "检测内容 检测结果 突变丰度 备注", "MSI MSS 0/55", "EGFR exon19 c.2235_2249del p.Glu746_Ala750del(E746_A750del) 29.59% I级,具有明确临床意义", "MET 扩增 3.97 I级,具有明确临床意义", "TP53 exon8 p.817C>T p.Arg273Cys(R273C) 6.35% II级,具有潜在临床意义", "检测结果备注:表格内未列出的为未检出。", "报告医生", "生", "报告时间", "2026-02-06 16:26", "住院号", "门诊号", "送检医生", "病人编号", "1份已审核", "2026-01-30 14:10:13", "4.0", "无", "2份已审核", "2026-01-28 09:16:53", "4.0", "55", "无", "1份已审核", "2020-12-28 12:02", "2.0", "58床", "无", "2020-12-21 14:02", "2.0", "58床", "无"]

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
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord API raw response (len=3272):
[
	{"text": "病历", "bbox": [449, 339, 472, 357]},
	{"text": "姓名", "bbox": [73, 365, 94, 379]},
	{"text": "病区", "bbox": [73, 382, 94, 396]},
	{"text": "送检科室", "bbox": [73, 399, 108, 413]},
	{"text": "标本名称", "bbox": [73, 415, 108, 429]},
	{"text": "临床诊断", "bbox": [73, 432, 108, 446]},
	{"text": "病理诊断", "bbox": [73, 454, 108, 468]},
	{"text": "检查项目:肿瘤多基因检测(含MSI)", "bbox": [73, 471, 207, 485]},
	{"text": "检查方法:高通量测序(NGS)", "bbox": [73, 487, 177, 501]},
	{"text": "参考基因组:GRCh37/hg19", "bbox": [73, 501, 174, 515]},
	{"text": "临床数据库:1000 Genomes、ExAC、gnomAD、ClinVar、BRCA Exchange InSiGHT、DBSNP、Cancer Hotspots、COSMIC、JAX CKB、OncoKB等", "bbox": [73, 514, 644, 528]},
	{"text": "检测突变软件:ADXHS-Classic-H", "bbox": [73, 528, 197, 542]},
	{"text": "标本病理评估:肿瘤细胞占比30%。", "bbox": [73, 541, 200, 555]},
	{"text": "DNA质量评估:合格", "bbox": [73, 555, 145, 569]},
	{"text": "测序质量评估:合格", "bbox": [73, 568, 145, 582]},
	{"text": "表格结果:", "bbox": [73, 582, 113, 596]},
	{"text": "检测内容 检测结果 突变丰度 备注", "bbox": [73, 608, 200, 622]},
	{"text": "MSI MSS 0/55", "bbox": [73, 622, 130, 635]},
	{"text": "EGFR exon19 c.2235_2249del p.Glu746_Ala750del(E746_A750del) 29.59% I级,具有明确临床意义", "bbox": [73, 635, 459, 649]},
	{"text": "MET 扩增 3.97 I级,具有明确临床意义", "bbox": [73, 649, 221, 663]},
	{"text": "TP53 exon8 p.817C>T p.Arg273Cys(R273C) 6.35% II级,具有潜在临床意义", "bbox": [73, 663, 367, 677]},
	{"text": "检测结果备注:表格内未列出的为未检出。", "bbox": [73, 676, 234, 690]},
	{"text": "报告医生", "bbox": [73, 705, 108, 719]},
	{"text": "生", "bbox": [435, 705, 453, 719]},
	{"text": "报告时间", "bbox": [587, 705, 623, 719]},
	{"text": "2026-02-06 16:26", "bbox": [667, 707, 735, 718]},
	{"text": "住院号", "bbox": [529, 305, 568, 319]},
	{"text": "门诊号", "bbox": [531, 382, 563, 396]},
	{"text": "送检医生", "bbox": [531, 399, 566, 413]},
	{"text": "病人编号", "bbox": [759, 366, 795, 380]},
	{"text": "1份已审核", "bbox": [634, 121, 677, 135], "bbox": [634, 121, 677, 135]},
	{"text": "2026-01-30 14:10:13", "bbox": [732, 122, 818, 134], "bbox": [732, 122, 818, 134]},
	{"text": "4.0", "bbox": [829, 122, 844, 134], "bbox": [829, 122, 844, 134]},
	{"text": "无", "bbox": [945, 121, 957, 135], "bbox": [945, 121, 957, 135]},
	{"text": "2份已审核", "bbox": [634, 152, 677, 166], "bbox": [634, 152, 677, 166]},
	{"text": "2026-01-28 09:16:53", "bbox": [732, 153, 818, 165], "bbox": [732, 153, 818, 165]},
	{"text": "4.0", "bbox": [829, 153, 844, 165], "bbox": [829, 153, 844, 165]},
	{"text": "55", "bbox": [883, 153, 895, 165], "bbox": [883, 153, 895, 165]},
	{"text": "无", "bbox": [945, 152, 957, 166], "bbox": [945, 152, 957, 166]},
	{"text": "1份已审核", "bbox": [634, 183, 677, 196], "bbox": [634, 183, 677, 196]},
	{"text": "2020-12-28 12:02", "bbox": [732, 184, 805, 196], "bbox": [732, 184, 805, 196]},
	{"text": "2.0", "bbox": [830, 184, 844, 196], "bbox": [830, 184, 844, 196]},
	{"text": "58床", "bbox": [883, 184, 903, 196], "bbox": [883, 184, 903, 196]},
	{"text": "无", "bbox": [945, 183, 957, 196], "bbox": [945, 183, 957, 196]},
	{"text": "2020-12-21 14:02", "bbox": [732, 215, 805, 227], "bbox": [732, 215, 805, 227]},
	{"text": "2.0", "bbox": [830, 215, 844, 227], "bbox": [830, 215, 844, 227]},
	{"text": "58床", "bbox": [883, 215, 903, 227], "bbox": [883, 215, 903, 227]},
	{"text": "无", "bbox": [945, 214, 957, 227], "bbox": [945, 214, 957, 227]}
]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord API: raw_items=48, valid_items=48, elapsed=16.4s
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[0]: text=病历, bbox=[449, 339, 472, 357]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[73, 365, 94, 379]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[2]: text=病区, bbox=[73, 382, 94, 396]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[3]: text=送检科室, bbox=[73, 399, 108, 413]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[4]: text=标本名称, bbox=[73, 415, 108, 429]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[5]: text=临床诊断, bbox=[73, 432, 108, 446]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[6]: text=病理诊断, bbox=[73, 454, 108, 468]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[7]: text=检查项目:肿瘤多基因检测(含MSI), bbox=[73, 471, 207, 485]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[8]: text=检查方法:高通量测序(NGS), bbox=[73, 487, 177, 501]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[9]: text=参考基因组:GRCh37/hg19, bbox=[73, 501, 174, 515]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[10]: text=临床数据库:1000 Genomes、ExAC、gnomAD、ClinVar、BRCA Exchange InSiGHT、DBSNP、Cancer Hotspots、COSMIC、JAX CKB、OncoKB等, bbox=[73, 514, 644, 528]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[11]: text=检测突变软件:ADXHS-Classic-H, bbox=[73, 528, 197, 542]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[12]: text=标本病理评估:肿瘤细胞占比30%。, bbox=[73, 541, 200, 555]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[13]: text=DNA质量评估:合格, bbox=[73, 555, 145, 569]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[14]: text=测序质量评估:合格, bbox=[73, 568, 145, 582]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[15]: text=表格结果:, bbox=[73, 582, 113, 596]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[16]: text=检测内容 检测结果 突变丰度 备注, bbox=[73, 608, 200, 622]
2026-08-10 17:46:58,128 INFO     29 [qwen-vl-text] coord item[17]: text=MSI MSS 0/55, bbox=[73, 622, 130, 635]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[18]: text=EGFR exon19 c.2235_2249del p.Glu746_Ala750del(E746_A750del) 29.59% I级,具有明确临床意义, bbox=[73, 635, 459, 649]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[19]: text=MET 扩增 3.97 I级,具有明确临床意义, bbox=[73, 649, 221, 663]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[20]: text=TP53 exon8 p.817C>T p.Arg273Cys(R273C) 6.35% II级,具有潜在临床意义, bbox=[73, 663, 367, 677]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[21]: text=检测结果备注:表格内未列出的为未检出。, bbox=[73, 676, 234, 690]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[22]: text=报告医生, bbox=[73, 705, 108, 719]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[23]: text=生, bbox=[435, 705, 453, 719]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[24]: text=报告时间, bbox=[587, 705, 623, 719]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[25]: text=2026-02-06 16:26, bbox=[667, 707, 735, 718]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[26]: text=住院号, bbox=[529, 305, 568, 319]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[27]: text=门诊号, bbox=[531, 382, 563, 396]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[28]: text=送检医生, bbox=[531, 399, 566, 413]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[29]: text=病人编号, bbox=[759, 366, 795, 380]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[30]: text=1份已审核, bbox=[634, 121, 677, 135]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[31]: text=2026-01-30 14:10:13, bbox=[732, 122, 818, 134]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[32]: text=4.0, bbox=[829, 122, 844, 134]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[33]: text=无, bbox=[945, 121, 957, 135]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[34]: text=2份已审核, bbox=[634, 152, 677, 166]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[35]: text=2026-01-28 09:16:53, bbox=[732, 153, 818, 165]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[36]: text=4.0, bbox=[829, 153, 844, 165]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[37]: text=55, bbox=[883, 153, 895, 165]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[38]: text=无, bbox=[945, 152, 957, 166]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[39]: text=1份已审核, bbox=[634, 183, 677, 196]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[40]: text=2020-12-28 12:02, bbox=[732, 184, 805, 196]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[41]: text=2.0, bbox=[830, 184, 844, 196]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[42]: text=58床, bbox=[883, 184, 903, 196]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[43]: text=无, bbox=[945, 183, 957, 196]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[44]: text=2020-12-21 14:02, bbox=[732, 215, 805, 227]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[45]: text=2.0, bbox=[830, 215, 844, 227]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[46]: text=58床, bbox=[883, 215, 903, 227]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] coord item[47]: text=无, bbox=[945, 214, 957, 227]
2026-08-10 17:46:58,129 INFO     29 [qwen-vl-text] page=11 — 48/48 coords, api_time=16.4s
2026-08-10 17:46:58,132 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1201349, prompt_len=1391
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共51行）
["分子病理检查报告单", "编", "患者姓名", "性别：男", "年龄：75岁", "住院号：", "送检科室", "尿府理", "登记号：", "标本类型：石蜡组织", "病变部", "病理诊断：", "收到日期：2026-01-20", "检查项目：肿瘤多基因检测（含MSI）", "检查方法：高通量测序(NGS)", "参考基因组：GRCh37/hg19", "临床数据库：1000 Genomes、ExAC、gnomAD、ClinVar、BECA Exchange InSiGHT、DBSNP、", "Cancer Hotspots、COSMIC、JAX CXB、OncoKB等", "检测突变软件：ADXHS-Classic-H", "标本病理评估：肿瘤细胞占比30%。", "核酸质量评估：合格", "测序质量评估：合格", "检测结果：", "检测内容", "检测结果", "突变丰度", "备注", "MSI", "MSS", "0/55", "EGFR", "exon19 c.2235_2249del", "29.59%", "I级、具有明确临床意义", "p.Glu746_Ala750del (E746_A750del)", "MET", "3'端", "3.97", "I级、具有明确临床意义", "TP53", "exon6 c.817C>T p.Arg273Cys (R273C)", "6.35%", "II级、具有潜在临床意义", "备注：表格内未列出的为未检出。", "注：此报告仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与分子病理诊断科联系。", "报告.", "检测者", "报告日期：2026-02-06", "第1页/共16页", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 17:47:14,250 INFO     29 [qwen-vl-text] coord API raw response (len=2853):
[
	{"text": "分子病理检查报告单", "bbox": [364, 58, 650, 82]},
	{"text": "编", "bbox": [60, 90, 83, 106]},
	{"text": "患者姓名", "bbox": [62, 115, 136, 129]},
	{"text": "性别：男", "bbox": [366, 114, 453, 130]},
	{"text": "年龄：75岁", "bbox": [522, 114, 627, 130]},
	{"text": "住院号：", "bbox": [674, 115, 757, 130]},
	{"text": "送检科室", "bbox": [62, 134, 140, 148]},
	{"text": "尿府理", "bbox": [366, 134, 431, 148]},
	{"text": "登记号：", "bbox": [674, 134, 757, 149]},
	{"text": "标本类型：石蜡组织", "bbox": [62, 152, 228, 166]},
	{"text": "病变部", "bbox": [366, 152, 431, 166]},
	{"text": "病理诊断：", "bbox": [674, 152, 757, 166]},
	{"text": "收到日期：2026-01-20", "bbox": [62, 168, 254, 182]},
	{"text": "检查项目：肿瘤多基因检测（含MSI）", "bbox": [86, 189, 447, 203]},
	{"text": "检查方法：高通量测序(NGS)", "bbox": [86, 210, 376, 225]},
	{"text": "参考基因组：GRCh37/hg19", "bbox": [86, 234, 342, 250]},
	{"text": "临床数据库：1000 Genomes、ExAC、gnomAD、ClinVar、BECA Exchange InSiGHT、DBSNP、", "bbox": [86, 256, 866, 271]},
	{"text": "Cancer Hotspots、COSMIC、JAX CXB、OncoKB等", "bbox": [236, 273, 637, 288]},
	{"text": "检测突变软件：ADXHS-Classic-H", "bbox": [86, 298, 378, 312]},
	{"text": "标本病理评估：肿瘤细胞占比30%。", "bbox": [86, 333, 387, 348]},
	{"text": "核酸质量评估：合格", "bbox": [86, 357, 257, 372]},
	{"text": "测序质量评估：合格", "bbox": [447, 357, 622, 372]},
	{"text": "检测结果：", "bbox": [86, 388, 207, 403]},
	{"text": "检测内容", "bbox": [124, 439, 200, 453]},
	{"text": "检测结果", "bbox": [356, 439, 433, 453]},
	{"text": "突变丰度", "bbox": [592, 439, 668, 453]},
	{"text": "备注", "bbox": [797, 439, 835, 453]},
	{"text": "MSI", "bbox": [149, 466, 173, 477]},
	{"text": "MSS", "bbox": [380, 466, 407, 477]},
	{"text": "0/55", "bbox": [614, 466, 647, 477]},
	{"text": "EGFR", "bbox": [145, 496, 178, 507]},
	{"text": "exon19 c.2235_2249del", "bbox": [310, 490, 478, 500]},
	{"text": "29.59%", "bbox": [606, 496, 655, 507]},
	{"text": "I级、具有明确临床意义", "bbox": [732, 495, 899, 507]},
	{"text": "p.Glu746_Ala750del (E746_A750del)", "bbox": [265, 502, 520, 513]},
	{"text": "MET", "bbox": [149, 526, 174, 536]},
	{"text": "3'端", "bbox": [378, 525, 410, 537]},
	{"text": "3.97", "bbox": [614, 526, 647, 536]},
	{"text": "I级、具有明确临床意义", "bbox": [732, 525, 899, 537]},
	{"text": "TP53", "bbox": [145, 556, 178, 567]},
	{"text": "exon6 c.817C>T p.Arg273Cys (R273C)", "bbox": [263, 556, 523, 567]},
	{"text": "6.35%", "bbox": [610, 556, 651, 567]},
	{"text": "II级、具有潜在临床意义", "bbox": [727, 555, 902, 567]},
	{"text": "备注：表格内未列出的为未检出。", "bbox": [89, 588, 318, 601]},
	{"text": "注：此报告仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与分子病理诊断科联系。", "bbox": [102, 860, 835, 873]},
	{"text": "报告.", "bbox": [88, 899, 135, 914]},
	{"text": "检测者", "bbox": [361, 899, 416, 914]},
	{"text": "报告日期：2026-02-06", "bbox": [650, 900, 832, 914]},
	{"text": "第1页/共16页", "bbox": [441, 920, 566, 933]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 978, 977, 987]}
]
2026-08-10 17:47:14,250 INFO     29 [qwen-vl-text] coord API: raw_items=51, valid_items=51, elapsed=16.1s
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[0]: text=分子病理检查报告单, bbox=[364, 58, 650, 82]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[1]: text=编, bbox=[60, 90, 83, 106]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[2]: text=患者姓名, bbox=[62, 115, 136, 129]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[366, 114, 453, 130]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：75岁, bbox=[522, 114, 627, 130]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[674, 115, 757, 130]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[6]: text=送检科室, bbox=[62, 134, 140, 148]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[7]: text=尿府理, bbox=[366, 134, 431, 148]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[8]: text=登记号：, bbox=[674, 134, 757, 149]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[9]: text=标本类型：石蜡组织, bbox=[62, 152, 228, 166]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[10]: text=病变部, bbox=[366, 152, 431, 166]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[11]: text=病理诊断：, bbox=[674, 152, 757, 166]
2026-08-10 17:47:14,251 INFO     29 [qwen-vl-text] coord item[12]: text=收到日期：2026-01-20, bbox=[62, 168, 254, 182]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[13]: text=检查项目：肿瘤多基因检测（含MSI）, bbox=[86, 189, 447, 203]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[14]: text=检查方法：高通量测序(NGS), bbox=[86, 210, 376, 225]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[15]: text=参考基因组：GRCh37/hg19, bbox=[86, 234, 342, 250]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[16]: text=临床数据库：1000 Genomes、ExAC、gnomAD、ClinVar、BECA Exchange InSiGHT、DBSNP、, bbox=[86, 256, 866, 271]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[17]: text=Cancer Hotspots、COSMIC、JAX CXB、OncoKB等, bbox=[236, 273, 637, 288]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[18]: text=检测突变软件：ADXHS-Classic-H, bbox=[86, 298, 378, 312]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[19]: text=标本病理评估：肿瘤细胞占比30%。, bbox=[86, 333, 387, 348]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[20]: text=核酸质量评估：合格, bbox=[86, 357, 257, 372]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[21]: text=测序质量评估：合格, bbox=[447, 357, 622, 372]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[22]: text=检测结果：, bbox=[86, 388, 207, 403]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[23]: text=检测内容, bbox=[124, 439, 200, 453]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[24]: text=检测结果, bbox=[356, 439, 433, 453]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[25]: text=突变丰度, bbox=[592, 439, 668, 453]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[26]: text=备注, bbox=[797, 439, 835, 453]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[27]: text=MSI, bbox=[149, 466, 173, 477]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[28]: text=MSS, bbox=[380, 466, 407, 477]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[29]: text=0/55, bbox=[614, 466, 647, 477]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[30]: text=EGFR, bbox=[145, 496, 178, 507]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[31]: text=exon19 c.2235_2249del, bbox=[310, 490, 478, 500]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[32]: text=29.59%, bbox=[606, 496, 655, 507]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[33]: text=I级、具有明确临床意义, bbox=[732, 495, 899, 507]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[34]: text=p.Glu746_Ala750del (E746_A750del), bbox=[265, 502, 520, 513]
2026-08-10 17:47:14,252 INFO     29 [qwen-vl-text] coord item[35]: text=MET, bbox=[149, 526, 174, 536]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[36]: text=3'端, bbox=[378, 525, 410, 537]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[37]: text=3.97, bbox=[614, 526, 647, 536]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[38]: text=I级、具有明确临床意义, bbox=[732, 525, 899, 537]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[39]: text=TP53, bbox=[145, 556, 178, 567]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[40]: text=exon6 c.817C>T p.Arg273Cys (R273C), bbox=[263, 556, 523, 567]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[41]: text=6.35%, bbox=[610, 556, 651, 567]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[42]: text=II级、具有潜在临床意义, bbox=[727, 555, 902, 567]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[43]: text=备注：表格内未列出的为未检出。, bbox=[89, 588, 318, 601]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[44]: text=注：此报告仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与分子病理诊断科联系。, bbox=[102, 860, 835, 873]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[45]: text=报告., bbox=[88, 899, 135, 914]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[46]: text=检测者, bbox=[361, 899, 416, 914]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[47]: text=报告日期：2026-02-06, bbox=[650, 900, 832, 914]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[48]: text=第1页/共16页, bbox=[441, 920, 566, 933]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[49]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-10 17:47:14,253 INFO     29 [qwen-vl-text] coord item[50]: text=3亿人都在用的扫描App, bbox=[861, 978, 977, 987]
2026-08-10 17:47:14,254 INFO     29 [qwen-vl-text] page=12 — 51/51 coords, api_time=16.1s
2026-08-10 17:47:14,257 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1616496, prompt_len=2034
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共42行）
["V2.0", "循环周期，调节转录，DNA 复", "制和诱导细胞程序死亡及抗血", "管生成。", "细胞瘤）和肾上腺皮质癌。TP53 突变还发生于包括 CML、", "ANLL、MDS 及 B-NHL。在内的多种恶性血液肿瘤以及", "黑色素瘤、基底细胞癌、鳞状细胞癌等皮肤癌等多种类型", "肝癌及恶性肿瘤。TP53 突变是多种癌症预后不良的标", "志，如乳腺癌。TP53 基因变异与肿瘤细胞对铂类化疗药", "物耐药性相关，但不影响氟杉醇类药物的敏感性；相关化", "疗药物还包括喜树碱、5-FU、顺铂、环磷酰胺等。FDA 已", "授予 IXC14586 快速通道资格，目前治疗具有 TP53 Y220C", "突变的局部晚期或转移性实体瘤患者。", "四、声明告知", "1. 本检测项目中使用的参考基因组版本为 hg19，报告中的变异命名遵从 HGVS 指南", "(http://varnomcn.hgvs.org)中的相关规定进行命名。", "2. 变异分类：综合变异在治疗、诊断和预后方面相关研究证据，将变异分为 4 级：I", "级为明确临床意义；II 级为潜在临床意义；III 类为临床意义未明；IV 级为良性/可能良", "性。本报告中仅列出 I-III 级变异。", "3. 检测结果与临床意义相关性的证据水平分为 4 个等级（A/B/C/D）。A 级：对应", "病种中 FDA/NMPA 批准或指南推荐的治疗、诊断和（或）预后的相关标志物；B 级：专家", "共识或 III/IV 期临床试验研究表明对患者肿瘤治疗有敏感或耐药、或具有诊断、预后意义", "的生物标志物；C 级：FDA/NMPA 批准或专业指南推荐的在其他癌种对某个治疗方案敏感", "或耐药的标志物；或者是作为临床试验入组标准的标志物；或者是多个小型研究结果证实", "具有诊断或预后意义的标志物；D 级：临床前研究表明具有潜在的治疗意义，或基于小型", "研究或多个案例报告可能作为辅助疾病诊断或预后的标志物（结论未形成共识）。", "4. 本检测的检测内容大部分基于仅限于 DNA 水平，部分基因涉及 RNA 水平，但", "不涉及蛋白水平的检测。", "5. 对于组织样品，如样本中肿瘤细胞含量低于 20%，可能影响检测结果的准确性；", "如未检出指定的基因变异，可能由于该样本中该突变的丰度低于本项目的检测下限。", "6. 对于组织样品，肿瘤存在异质性，即不同病灶甚至同一病灶内的组织的突变图谱可", "能也存在差异；另外，不同疾病发展或治疗阶段取出的样本中的突变可能不同；因此，本", "检测报告仅对此次送检的样本负责。并且，所检测的突变位点仅限于本检测试剂的检测范", "围，样品的基因组中可能存在的某些罕见或复杂突变，本项目不能完全检测。", "7. 本报告对于测序结果分析中核苷酸改变的位置信息是基于当前版本的基因组和转录", "本，随着人类基因组的更新，这些信息可能会有所不同；同时对于突变位点的解读，是基", "于当前已发表的文献、指南、公共数据库及临床研究结果，随着研究的发展，特定位点的", "解读可能发生变更。", "8. 本检测仅为临床治疗或诊断提供参考，具体的诊断结果及治疗决策应由临床医生综", "合患者的各种临床信息和检测结果进行判断。", "CS 扫描全能王", "3 亿人都在用的扫描 App"]

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
2026-08-10 17:47:30,096 INFO     29 [qwen-vl-text] coord API raw response (len=3142):
[
	{"text": "V2.0", "bbox": [809, 58, 839, 67]},
	{"text": "循环周期，调节转录，DNA 复", "bbox": [232, 93, 424, 105]},
	{"text": "制和诱导细胞程序死亡及抗血", "bbox": [232, 110, 424, 122]},
	{"text": "管生成。", "bbox": [232, 127, 285, 138]},
	{"text": "细胞瘤）和肾上腺皮质癌。TP53 突变还发生于包括 CML、", "bbox": [552, 93, 900, 105]},
	{"text": "ANLL、MDS 及 B-NHL。在内的多种恶性血液肿瘤以及", "bbox": [552, 110, 900, 122]},
	{"text": "黑色素瘤、基底细胞癌、鳞状细胞癌等皮肤癌等多种类型", "bbox": [552, 127, 900, 138]},
	{"text": "肝癌及恶性肿瘤。TP53 突变是多种癌症预后不良的标", "bbox": [552, 144, 900, 156]},
	{"text": "志，如乳腺癌。TP53 基因变异与肿瘤细胞对铂类化疗药", "bbox": [552, 161, 900, 173]},
	{"text": "物耐药性相关，但不影响氟杉醇类药物的敏感性；相关化", "bbox": [552, 178, 900, 190]},
	{"text": "疗药物还包括喜树碱、5-FU、顺铂、环磷酰胺等。FDA 已", "bbox": [552, 195, 900, 207]},
	{"text": "授予 IXC14586 快速通道资格，目前治疗具有 TP53 Y220C", "bbox": [552, 212, 900, 224]},
	{"text": "突变的局部晚期或转移性实体瘤患者。", "bbox": [552, 229, 784, 241]},
	{"text": "四、声明告知", "bbox": [185, 254, 285, 267]},
	{"text": "1. 本检测项目中使用的参考基因组版本为 hg19，报告中的变异命名遵从 HGVS 指南", "bbox": [218, 277, 835, 290]},
	{"text": "(http://varnomcn.hgvs.org)中的相关规定进行命名。", "bbox": [182, 300, 534, 313]},
	{"text": "2. 变异分类：综合变异在治疗、诊断和预后方面相关研究证据，将变异分为 4 级：I", "bbox": [218, 324, 835, 337]},
	{"text": "级为明确临床意义；II 级为潜在临床意义；III 类为临床意义未明；IV 级为良性/可能良", "bbox": [185, 347, 805, 360]},
	{"text": "性。本报告中仅列出 I-III 级变异。", "bbox": [185, 369, 425, 382]},
	{"text": "3. 检测结果与临床意义相关性的证据水平分为 4 个等级（A/B/C/D）。A 级：对应", "bbox": [218, 392, 819, 405]},
	{"text": "病种中 FDA/NMPA 批准或指南推荐的治疗、诊断和（或）预后的相关标志物；B 级：专家", "bbox": [185, 414, 825, 427]},
	{"text": "共识或 III/IV 期临床试验研究表明对患者肿瘤治疗有敏感或耐药、或具有诊断、预后意义", "bbox": [185, 437, 822, 450]},
	{"text": "的生物标志物；C 级：FDA/NMPA 批准或专业指南推荐的在其他癌种对某个治疗方案敏感", "bbox": [185, 459, 822, 472]},
	{"text": "或耐药的标志物；或者是作为临床试验入组标准的标志物；或者是多个小型研究结果证实", "bbox": [185, 482, 825, 495]},
	{"text": "具有诊断或预后意义的标志物；D 级：临床前研究表明具有潜在的治疗意义，或基于小型", "bbox": [185, 504, 820, 517]},
	{"text": "研究或多个案例报告可能作为辅助疾病诊断或预后的标志物（结论未形成共识）。", "bbox": [185, 526, 769, 539]},
	{"text": "4. 本检测的检测内容大部分基于仅限于 DNA 水平，部分基因涉及 RNA 水平，但", "bbox": [218, 549, 822, 562]},
	{"text": "不涉及蛋白水平的检测。", "bbox": [185, 571, 355, 584]},
	{"text": "5. 对于组织样品，如样本中肿瘤细胞含量低于 20%，可能影响检测结果的准确性；", "bbox": [218, 594, 809, 607]},
	{"text": "如未检出指定的基因变异，可能由于该样本中该突变的丰度低于本项目的检测下限。", "bbox": [185, 617, 782, 629]},
	{"text": "6. 对于组织样品，肿瘤存在异质性，即不同病灶甚至同一病灶内的组织的突变图谱可", "bbox": [218, 640, 832, 653]},
	{"text": "能也存在差异；另外，不同疾病发展或治疗阶段取出的样本中的突变可能不同；因此，本", "bbox": [185, 662, 825, 675]},
	{"text": "检测报告仅对此次送检的样本负责。并且，所检测的突变位点仅限于本检测试剂的检测范", "bbox": [185, 685, 825, 698]},
	{"text": "围，样品的基因组中可能存在的某些罕见或复杂突变，本项目不能完全检测。", "bbox": [185, 707, 734, 720]},
	{"text": "7. 本报告对于测序结果分析中核苷酸改变的位置信息是基于当前版本的基因组和转录", "bbox": [218, 730, 832, 743]},
	{"text": "本，随着人类基因组的更新，这些信息可能会有所不同；同时对于突变位点的解读，是基", "bbox": [185, 753, 825, 766]},
	{"text": "于当前已发表的文献、指南、公共数据库及临床研究结果，随着研究的发展，特定位点的", "bbox": [185, 775, 825, 788]},
	{"text": "解读可能发生变更。", "bbox": [182, 798, 321, 811]},
	{"text": "8. 本检测仅为临床治疗或诊断提供参考，具体的诊断结果及治疗决策应由临床医生综", "bbox": [214, 822, 832, 835]},
	{"text": "合患者的各种临床信息和检测结果进行判断。", "bbox": [182, 844, 501, 857]},
	{"text": "CS 扫描全能王", "bbox": [862, 958, 977, 973]},
	{"text": "3 亿人都在用的扫描 App", "bbox": [862, 977, 977, 986]}
]
2026-08-10 17:47:30,096 INFO     29 [qwen-vl-text] coord API: raw_items=42, valid_items=42, elapsed=15.8s
2026-08-10 17:47:30,096 INFO     29 [qwen-vl-text] coord item[0]: text=V2.0, bbox=[809, 58, 839, 67]
2026-08-10 17:47:30,096 INFO     29 [qwen-vl-text] coord item[1]: text=循环周期，调节转录，DNA 复, bbox=[232, 93, 424, 105]
2026-08-10 17:47:30,096 INFO     29 [qwen-vl-text] coord item[2]: text=制和诱导细胞程序死亡及抗血, bbox=[232, 110, 424, 122]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[3]: text=管生成。, bbox=[232, 127, 285, 138]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[4]: text=细胞瘤）和肾上腺皮质癌。TP53 突变还发生于包括 CML、, bbox=[552, 93, 900, 105]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[5]: text=ANLL、MDS 及 B-NHL。在内的多种恶性血液肿瘤以及, bbox=[552, 110, 900, 122]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[6]: text=黑色素瘤、基底细胞癌、鳞状细胞癌等皮肤癌等多种类型, bbox=[552, 127, 900, 138]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[7]: text=肝癌及恶性肿瘤。TP53 突变是多种癌症预后不良的标, bbox=[552, 144, 900, 156]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[8]: text=志，如乳腺癌。TP53 基因变异与肿瘤细胞对铂类化疗药, bbox=[552, 161, 900, 173]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[9]: text=物耐药性相关，但不影响氟杉醇类药物的敏感性；相关化, bbox=[552, 178, 900, 190]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[10]: text=疗药物还包括喜树碱、5-FU、顺铂、环磷酰胺等。FDA 已, bbox=[552, 195, 900, 207]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[11]: text=授予 IXC14586 快速通道资格，目前治疗具有 TP53 Y220C, bbox=[552, 212, 900, 224]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[12]: text=突变的局部晚期或转移性实体瘤患者。, bbox=[552, 229, 784, 241]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[13]: text=四、声明告知, bbox=[185, 254, 285, 267]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[14]: text=1. 本检测项目中使用的参考基因组版本为 hg19，报告中的变异命名遵从 HGVS 指南, bbox=[218, 277, 835, 290]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[15]: text=(http://varnomcn.hgvs.org)中的相关规定进行命名。, bbox=[182, 300, 534, 313]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[16]: text=2. 变异分类：综合变异在治疗、诊断和预后方面相关研究证据，将变异分为 4 级：I, bbox=[218, 324, 835, 337]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[17]: text=级为明确临床意义；II 级为潜在临床意义；III 类为临床意义未明；IV 级为良性/可能良, bbox=[185, 347, 805, 360]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[18]: text=性。本报告中仅列出 I-III 级变异。, bbox=[185, 369, 425, 382]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[19]: text=3. 检测结果与临床意义相关性的证据水平分为 4 个等级（A/B/C/D）。A 级：对应, bbox=[218, 392, 819, 405]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[20]: text=病种中 FDA/NMPA 批准或指南推荐的治疗、诊断和（或）预后的相关标志物；B 级：专家, bbox=[185, 414, 825, 427]
2026-08-10 17:47:30,097 INFO     29 [qwen-vl-text] coord item[21]: text=共识或 III/IV 期临床试验研究表明对患者肿瘤治疗有敏感或耐药、或具有诊断、预后意义, bbox=[185, 437, 822, 450]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[22]: text=的生物标志物；C 级：FDA/NMPA 批准或专业指南推荐的在其他癌种对某个治疗方案敏感, bbox=[185, 459, 822, 472]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[23]: text=或耐药的标志物；或者是作为临床试验入组标准的标志物；或者是多个小型研究结果证实, bbox=[185, 482, 825, 495]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[24]: text=具有诊断或预后意义的标志物；D 级：临床前研究表明具有潜在的治疗意义，或基于小型, bbox=[185, 504, 820, 517]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[25]: text=研究或多个案例报告可能作为辅助疾病诊断或预后的标志物（结论未形成共识）。, bbox=[185, 526, 769, 539]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[26]: text=4. 本检测的检测内容大部分基于仅限于 DNA 水平，部分基因涉及 RNA 水平，但, bbox=[218, 549, 822, 562]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[27]: text=不涉及蛋白水平的检测。, bbox=[185, 571, 355, 584]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[28]: text=5. 对于组织样品，如样本中肿瘤细胞含量低于 20%，可能影响检测结果的准确性；, bbox=[218, 594, 809, 607]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[29]: text=如未检出指定的基因变异，可能由于该样本中该突变的丰度低于本项目的检测下限。, bbox=[185, 617, 782, 629]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[30]: text=6. 对于组织样品，肿瘤存在异质性，即不同病灶甚至同一病灶内的组织的突变图谱可, bbox=[218, 640, 832, 653]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[31]: text=能也存在差异；另外，不同疾病发展或治疗阶段取出的样本中的突变可能不同；因此，本, bbox=[185, 662, 825, 675]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[32]: text=检测报告仅对此次送检的样本负责。并且，所检测的突变位点仅限于本检测试剂的检测范, bbox=[185, 685, 825, 698]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[33]: text=围，样品的基因组中可能存在的某些罕见或复杂突变，本项目不能完全检测。, bbox=[185, 707, 734, 720]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[34]: text=7. 本报告对于测序结果分析中核苷酸改变的位置信息是基于当前版本的基因组和转录, bbox=[218, 730, 832, 743]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[35]: text=本，随着人类基因组的更新，这些信息可能会有所不同；同时对于突变位点的解读，是基, bbox=[185, 753, 825, 766]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[36]: text=于当前已发表的文献、指南、公共数据库及临床研究结果，随着研究的发展，特定位点的, bbox=[185, 775, 825, 788]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[37]: text=解读可能发生变更。, bbox=[182, 798, 321, 811]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[38]: text=8. 本检测仅为临床治疗或诊断提供参考，具体的诊断结果及治疗决策应由临床医生综, bbox=[214, 822, 832, 835]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[39]: text=合患者的各种临床信息和检测结果进行判断。, bbox=[182, 844, 501, 857]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[40]: text=CS 扫描全能王, bbox=[862, 958, 977, 973]
2026-08-10 17:47:30,098 INFO     29 [qwen-vl-text] coord item[41]: text=3 亿人都在用的扫描 App, bbox=[862, 977, 977, 986]
2026-08-10 17:47:30,099 INFO     29 [qwen-vl-text] page=13 — 42/42 coords, api_time=15.8s
2026-08-10 17:47:30,099 INFO     29 [qwen-vl-text] new_positions (141):
[[11, 378.058, 397.424, 201.70499999999998, 212.415], [11, 61.466, 79.148, 217.17499999999998, 225.505], [11, 61.466, 79.148, 227.29, 235.61999999999998], [11, 61.466, 90.93599999999999, 237.405, 245.73499999999999], [11, 61.466, 90.93599999999999, 246.92499999999998, 255.255], [11, 61.466, 90.93599999999999, 257.03999999999996, 265.37], [11, 61.466, 90.93599999999999, 270.13, 278.46], [11, 61.466, 174.29399999999998, 280.245, 288.575], [11, 61.466, 149.034, 289.765, 298.09499999999997], [11, 61.466, 146.50799999999998, 298.09499999999997, 306.425], [11, 61.466, 542.2479999999999, 305.83, 314.15999999999997], [11, 61.466, 165.874, 314.15999999999997, 322.49], [11, 61.466, 168.4, 321.895, 330.22499999999997], [11, 61.466, 122.08999999999999, 330.22499999999997, 338.555], [11, 61.466, 122.08999999999999, 337.96, 346.28999999999996], [11, 61.466, 95.146, 346.28999999999996, 354.62], [11, 61.466, 168.4, 361.76, 370.09], [11, 61.466, 109.46, 370.09, 377.825], [11, 61.466, 386.478, 377.825, 386.155], [11, 61.466, 186.082, 386.155, 394.48499999999996], [11, 61.466, 309.014, 394.48499999999996, 402.815], [11, 61.466, 197.028, 402.21999999999997, 410.54999999999995], [11, 61.466, 90.93599999999999, 419.47499999999997, 427.805], [11, 366.27, 381.426, 419.47499999999997, 427.805], [11, 494.25399999999996, 524.566, 419.47499999999997, 427.805], [11, 561.614, 618.87, 420.66499999999996, 427.21], [11, 445.418, 478.256, 181.475, 189.80499999999998], [11, 447.102, 474.046, 227.29, 235.61999999999998], [11, 447.102, 476.572, 237.405, 245.73499999999999], [11, 639.078, 669.39, 217.76999999999998, 226.1], [11, 533.828, 570.034, 71.99499999999999, 80.325], [11, 616.3439999999999, 688.756, 72.59, 79.72999999999999], [11, 698.018, 710.648, 72.59, 79.72999999999999], [11, 795.6899999999999, 805.794, 71.99499999999999, 80.325], [11, 533.828, 570.034, 90.44, 98.77], [11, 616.3439999999999, 688.756, 91.035, 98.175], [11, 698.018, 710.648, 91.035, 98.175], [11, 743.486, 753.5899999999999, 91.035, 98.175], [11, 795.6899999999999, 805.794, 90.44, 98.77], [11, 533.828, 570.034, 108.88499999999999, 116.61999999999999], [11, 616.3439999999999, 677.81, 109.47999999999999, 116.61999999999999], [11, 698.86, 710.648, 109.47999999999999, 116.61999999999999], [11, 743.486, 760.326, 109.47999999999999, 116.61999999999999], [11, 795.6899999999999, 805.794, 108.88499999999999, 116.61999999999999], [11, 616.3439999999999, 677.81, 127.925, 135.065], [11, 698.86, 710.648, 127.925, 135.065], [11, 743.486, 760.326, 127.925, 135.065], [11, 795.6899999999999, 805.794, 127.33, 135.065], [12, 216.57999999999998, 386.75, 48.836, 69.044], [12, 35.699999999999996, 49.385, 75.78, 89.252], [12, 36.89, 80.92, 96.83, 108.618], [12, 217.76999999999998, 269.53499999999997, 95.988, 109.46], [12, 310.59, 373.065, 95.988, 109.46], [12, 401.03, 450.41499999999996, 96.83, 109.46], [12, 36.89, 83.3, 112.828, 124.616], [12, 217.76999999999998, 256.445, 112.828, 124.616], [12, 401.03, 450.41499999999996, 112.828, 125.458], [12, 36.89, 135.66, 127.984, 139.772], [12, 217.76999999999998, 256.445, 127.984, 139.772], [12, 401.03, 450.41499999999996, 127.984, 139.772], [12, 36.89, 151.13, 141.456, 153.244], [12, 51.169999999999995, 265.965, 159.138, 170.926], [12, 51.169999999999995, 223.72, 176.82, 189.45], [12, 51.169999999999995, 203.48999999999998, 197.028, 210.5], [12, 51.169999999999995, 515.27, 215.552, 228.182], [12, 140.42, 379.015, 229.86599999999999, 242.49599999999998], [12, 51.169999999999995, 224.91, 250.916, 262.704], [12, 51.169999999999995, 230.265, 280.38599999999997, 293.01599999999996], [12, 51.169999999999995, 152.915, 300.594, 313.224], [12, 265.965, 370.09, 300.594, 313.224], [12, 51.169999999999995, 123.16499999999999, 326.69599999999997, 339.32599999999996], [12, 73.78, 119.0, 369.638, 381.426], [12, 211.82, 257.635, 369.638, 381.426], [12, 352.24, 397.46, 369.638, 381.426], [12, 474.215, 496.825, 369.638, 381.426], [12, 88.655, 102.935, 392.372, 401.63399999999996], [12, 226.1, 242.165, 392.372, 401.63399999999996], [12, 365.33, 384.965, 392.372, 401.63399999999996], [12, 86.27499999999999, 105.91, 417.632, 426.894], [12, 184.45, 284.40999999999997, 412.58, 421.0], [12, 360.57, 389.72499999999997, 417.632, 426.894], [12, 435.53999999999996, 534.905, 416.78999999999996, 426.894], [12, 157.67499999999998, 309.4, 422.68399999999997, 431.94599999999997], [12, 88.655, 103.53, 442.892, 451.312], [12, 224.91, 243.95, 442.05, 452.154], [12, 365.33, 384.965, 442.892, 451.312], [12, 435.53999999999996, 534.905, 442.05, 452.154], [12, 86.27499999999999, 105.91, 468.152, 477.414], [12, 156.48499999999999, 311.185, 468.152, 477.414], [12, 362.95, 387.34499999999997, 468.152, 477.414], [12, 432.565, 536.6899999999999, 467.31, 477.414], [12, 52.955, 189.20999999999998, 495.096, 506.042], [12, 60.69, 496.825, 724.12, 735.066], [12, 52.36, 80.325, 756.958, 769.588], [12, 214.795, 247.51999999999998, 756.958, 769.588], [12, 386.75, 495.03999999999996, 757.8, 769.588], [12, 262.395, 336.77, 774.64, 785.586], [12, 512.295, 581.3149999999999, 806.636, 820.108], [12, 512.295, 581.3149999999999, 823.476, 831.054], [13, 481.35499999999996, 499.205, 48.836, 56.414], [13, 138.04, 252.28, 78.306, 88.41], [13, 138.04, 252.28, 92.61999999999999, 102.72399999999999], [13, 138.04, 169.575, 106.934, 116.196], [13, 328.44, 535.5, 78.306, 88.41], [13, 328.44, 535.5, 92.61999999999999, 102.72399999999999], [13, 328.44, 535.5, 106.934, 116.196], [13, 328.44, 535.5, 121.24799999999999, 131.352], [13, 328.44, 535.5, 135.56199999999998, 145.666], [13, 328.44, 535.5, 149.876, 159.98], [13, 328.44, 535.5, 164.19, 174.29399999999998], [13, 328.44, 535.5, 178.504, 188.608], [13, 328.44, 466.47999999999996, 192.81799999999998, 202.922], [13, 110.07499999999999, 169.575, 213.868, 224.814], [13, 129.71, 496.825, 233.23399999999998, 244.17999999999998], [13, 108.28999999999999, 317.72999999999996, 252.6, 263.546], [13, 129.71, 496.825, 272.808, 283.75399999999996], [13, 110.07499999999999, 478.97499999999997, 292.174, 303.12], [13, 110.07499999999999, 252.875, 310.698, 321.644], [13, 129.71, 487.30499999999995, 330.06399999999996, 341.01], [13, 110.07499999999999, 490.875, 348.58799999999997, 359.534], [13, 110.07499999999999, 489.09, 367.954, 378.9], [13, 110.07499999999999, 489.09, 386.478, 397.424], [13, 110.07499999999999, 490.875, 405.844, 416.78999999999996], [13, 110.07499999999999, 487.9, 424.368, 435.31399999999996], [13, 110.07499999999999, 457.555, 442.892, 453.83799999999997], [13, 129.71, 489.09, 462.258, 473.204], [13, 110.07499999999999, 211.225, 480.782, 491.728], [13, 129.71, 481.35499999999996, 500.14799999999997, 511.094], [13, 110.07499999999999, 465.28999999999996, 519.514, 529.6179999999999], [13, 129.71, 495.03999999999996, 538.88, 549.826], [13, 110.07499999999999, 490.875, 557.404, 568.35], [13, 110.07499999999999, 490.875, 576.77, 587.716], [13, 110.07499999999999, 436.72999999999996, 595.294, 606.24], [13, 129.71, 495.03999999999996, 614.66, 625.606], [13, 110.07499999999999, 490.875, 634.026, 644.972], [13, 110.07499999999999, 490.875, 652.55, 663.496], [13, 108.28999999999999, 190.995, 671.9159999999999, 682.862], [13, 127.33, 495.03999999999996, 692.124, 703.0699999999999], [13, 108.28999999999999, 298.09499999999997, 710.648, 721.5939999999999], [13, 512.89, 581.3149999999999, 806.636, 819.266], [13, 512.89, 581.3149999999999, 822.634, 830.212]]
2026-08-10 17:47:30,100 INFO     29 [qwen-vl-text] ═══ DONE ═══ 141 positions, pages=3, time=55.1s
2026-08-10 17:47:30,100 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:47:30,108 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:47:30,108 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:47:30,108 INFO     29 [qwen-vl-text] positions(36): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:47:30,108 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [36]
2026-08-10 17:47:30,310 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:47:30,312 INFO     29 [qwen-vl-text] LLM extraction start, text_len=752
2026-08-10 17:47:30,312 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:47:30,312 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3801, \"bbox_end\": 3836, \"encounter_dates\": [\"2026-01-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "超声检查报告单\n思者登\n姓\n性别：男\n年龄：75岁\n床号：A02\n检查所见：\n右肝最大斜径12.8cm，左肝前后径6.4cm，上下径7.5cm，肝表面光滑，边缘规则，肝内\n呈细小点状回声，分布欠均匀，肝内见数个囊性回声，大者0.8x0.5cm，均透声可。\n空腹胆囊充盈差，胆囊区见胆囊祥回声，大小约3.4x1.4cm，腔内透声差，充满细密点\n状回声。\n胆总管内径0.5cm，未见明显异常回声，肝内胆管无明显扩张。\n胰腺大小形态可，表面光滑，内回声均匀，主胰管内径不宽。\n脾未探及。\n门静脉走行自然，呈入肝血流，门静脉主干内径1.0cm，入肝血流速度17.4cm/s，肝内\n门静脉血流充盈好，未见明显异常回声。\n肝静脉走行自然，各支内径不宽，腔内未见明显异常回声，血流速及频谱形态未见异\n常。\n双侧肾上腺区未见明显占位性病变。\n双肾大小形态正常，表面光滑，皮髓质分界清，左肾实质回声无明显异常，右肾中部实\n质内见1.5x1.2cm略高回声结节，边界清，双肾窦无分离扩张。\n双侧输尿管无明显扩张。\n膀胱充盈可，黏膜光滑，腔内未见明显占位。\n前列腺大小约4.0（左右径）×3.5（前后径）×3.2（上下径）cm，体积约23.3cm3，\n表面光滑，中叶略突，内部回声欠均匀。\n双侧精囊腺无肿大，内部回声均匀。\n双肾动脉主干血流通畅，肾内动脉血流分布好。\n左肾叶间动脉Vs 24.8cm/s，阻力指数（RI）0.66。\n右肾叶间动脉Vs 25.1cm/s，阻力指数（RI）0.65。\n超声提示：脾切除术后\n空腹胆囊充盈差、腔内透声差，慢性胆囊炎？请结合临床\n肝囊肿\n右肾略高回声结节，考虑良性（结合病史考虑复杂囊肿可能）\n前列腺增生并钙化\n报告日期：2026-01-27 08:35:35 记录人\nCS 扫描全能王",
    "role": "user"
  }
]
2026-08-10 17:47:30,314 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:47:30.313+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:47:35,861 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:47:35,861 INFO     29 [qwen-vl-text] LLM output (len=1009):
{
  "exam_date": "2026-01-27",
  "report_date": "2026-01-27",
  "exam_name": "超声检查",
  "exam_category": "imaging",
  "body_part": "腹部（肝胆胰脾肾肾上腺）、前列腺、精囊腺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": "A02",
  "findings": "右肝最大斜径12.8cm，左肝前后径6.4cm，上下径7.5cm，肝表面光滑，边缘规则，肝内呈细小点状回声，分布欠均匀，肝内见数个囊性回声，大者0.8x0.5cm，均透声可。\n空腹胆囊充盈差，胆囊区见胆囊祥回声，大小约3.4x1.4cm，腔内透声差，充满细密点状回声。\n胆总管内径0.5cm，未见明显异常回声，肝内胆管无明显扩张。\n胰腺大小形态可，表面光滑，内回声均匀，主胰管内径不宽。\n脾未探及。\n门静脉走行自然，呈入肝血流，门静脉主干内径1.0cm，入肝血流速度17.4cm/s，肝内门静脉血流充盈好，未见明显异常回声。\n肝静脉走行自然，各支内径不宽，腔内未见明显异常回声，血流速及频谱形态未见异常。\n双侧肾上腺区未见明显占位性病变。\n双肾大小形态正常，表面光滑，皮髓质分界清，左肾实质回声无明显异常，右肾中部实质内见1.5x1.2cm略高回声结节，边界清，双肾窦无分离扩张。\n双侧输尿管无明显扩张。\n膀胱充盈可，黏膜光滑，腔内未见明显占位。\n前列腺大小约4.0（左右径）×3.5（前后径）×3.2（上下径）cm，体积约23.3cm3，表面光滑，中叶略突，内部回声欠均匀。\n双侧精囊腺无肿大，内部回声均匀。\n双肾动脉主干血流通畅，肾内动脉血流分布好。\n左肾叶间动脉Vs 24.8cm/s，阻力指数（RI）0.66。\n右肾叶间动脉Vs 25.1cm/s，阻力指数（RI）0.65。",
  "conclusion": "脾切除术后\n空腹胆囊充盈差、腔内透声差，慢性胆囊炎？请结合临床\n肝囊肿\n右肾略高回声结节，考虑良性（结合病史考虑复杂囊肿可能）\n前列腺增生并钙化",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:47:35,868 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2501917, prompt_len=1473
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["超声检查报告单", "思者登", "姓", "性别：男", "年龄：75岁", "床号：A02", "检查所见：", "右肝最大斜径12.8cm，左肝前后径6.4cm，上下径7.5cm，肝表面光滑，边缘规则，肝内", "呈细小点状回声，分布欠均匀，肝内见数个囊性回声，大者0.8x0.5cm，均透声可。", "空腹胆囊充盈差，胆囊区见胆囊祥回声，大小约3.4x1.4cm，腔内透声差，充满细密点", "状回声。", "胆总管内径0.5cm，未见明显异常回声，肝内胆管无明显扩张。", "胰腺大小形态可，表面光滑，内回声均匀，主胰管内径不宽。", "脾未探及。", "门静脉走行自然，呈入肝血流，门静脉主干内径1.0cm，入肝血流速度17.4cm/s，肝内", "门静脉血流充盈好，未见明显异常回声。", "肝静脉走行自然，各支内径不宽，腔内未见明显异常回声，血流速及频谱形态未见异", "常。", "双侧肾上腺区未见明显占位性病变。", "双肾大小形态正常，表面光滑，皮髓质分界清，左肾实质回声无明显异常，右肾中部实", "质内见1.5x1.2cm略高回声结节，边界清，双肾窦无分离扩张。", "双侧输尿管无明显扩张。", "膀胱充盈可，黏膜光滑，腔内未见明显占位。", "前列腺大小约4.0（左右径）×3.5（前后径）×3.2（上下径）cm，体积约23.3cm3，", "表面光滑，中叶略突，内部回声欠均匀。", "双侧精囊腺无肿大，内部回声均匀。", "双肾动脉主干血流通畅，肾内动脉血流分布好。", "左肾叶间动脉Vs 24.8cm/s，阻力指数（RI）0.66。", "右肾叶间动脉Vs 25.1cm/s，阻力指数（RI）0.65。", "超声提示：脾切除术后", "空腹胆囊充盈差、腔内透声差，慢性胆囊炎？请结合临床", "肝囊肿", "右肾略高回声结节，考虑良性（结合病史考虑复杂囊肿可能）", "前列腺增生并钙化", "报告日期：2026-01-27 08:35:35 记录人", "CS 扫描全能王"]

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
2026-08-10 17:47:50,684 INFO     29 [qwen-vl-text] coord API raw response (len=2326):
[
	{"text": "超声检查报告单", "bbox": [335, 86, 652, 109]},
	{"text": "思者登", "bbox": [91, 121, 158, 137]},
	{"text": "姓", "bbox": [131, 151, 151, 165]},
	{"text": "性别：男", "bbox": [433, 151, 523, 167]},
	{"text": "年龄：75岁", "bbox": [655, 151, 763, 167]},
	{"text": "床号：A02", "bbox": [655, 180, 756, 196]},
	{"text": "检查所见：", "bbox": [91, 458, 180, 475]},
	{"text": "右肝最大斜径12.8cm，左肝前后径6.4cm，上下径7.5cm，肝表面光滑，边缘规则，肝内", "bbox": [91, 473, 895, 490]},
	{"text": "呈细小点状回声，分布欠均匀，肝内见数个囊性回声，大者0.8x0.5cm，均透声可。", "bbox": [91, 488, 814, 504]},
	{"text": "空腹胆囊充盈差，胆囊区见胆囊祥回声，大小约3.4x1.4cm，腔内透声差，充满细密点", "bbox": [91, 503, 884, 520]},
	{"text": "状回声。", "bbox": [91, 517, 162, 533]},
	{"text": "胆总管内径0.5cm，未见明显异常回声，肝内胆管无明显扩张。", "bbox": [133, 532, 673, 548]},
	{"text": "胰腺大小形态可，表面光滑，内回声均匀，主胰管内径不宽。", "bbox": [133, 547, 664, 563]},
	{"text": "脾未探及。", "bbox": [133, 562, 222, 578]},
	{"text": "门静脉走行自然，呈入肝血流，门静脉主干内径1.0cm，入肝血流速度17.4cm/s，肝内", "bbox": [133, 576, 884, 593]},
	{"text": "门静脉血流充盈好，未见明显异常回声。", "bbox": [91, 591, 444, 607]},
	{"text": "肝静脉走行自然，各支内径不宽，腔内未见明显异常回声，血流速及频谱形态未见异", "bbox": [133, 606, 874, 622]},
	{"text": "常。", "bbox": [91, 620, 123, 636]},
	{"text": "双侧肾上腺区未见明显占位性病变。", "bbox": [133, 635, 444, 651]},
	{"text": "双肾大小形态正常，表面光滑，皮髓质分界清，左肾实质回声无明显异常，右肾中部实", "bbox": [133, 650, 895, 666]},
	{"text": "质内见1.5x1.2cm略高回声结节，边界清，双肾窦无分离扩张。", "bbox": [91, 664, 634, 680]},
	{"text": "双侧输尿管无明显扩张。", "bbox": [133, 679, 343, 695]},
	{"text": "膀胱充盈可，黏膜光滑，腔内未见明显占位。", "bbox": [133, 694, 523, 710]},
	{"text": "前列腺大小约4.0（左右径）×3.5（前后径）×3.2（上下径）cm，体积约23.3cm3，", "bbox": [133, 708, 872, 725]},
	{"text": "表面光滑，中叶略突，内部回声欠均匀。", "bbox": [91, 723, 444, 739]},
	{"text": "双侧精囊腺无肿大，内部回声均匀。", "bbox": [133, 738, 444, 754]},
	{"text": "双肾动脉主干血流通畅，肾内动脉血流分布好。", "bbox": [133, 752, 544, 768]},
	{"text": "左肾叶间动脉Vs 24.8cm/s，阻力指数（RI）0.66。", "bbox": [133, 767, 573, 783]},
	{"text": "右肾叶间动脉Vs 25.1cm/s，阻力指数（RI）0.65。", "bbox": [133, 781, 573, 798]},
	{"text": "超声提示：脾切除术后", "bbox": [91, 811, 283, 828]},
	{"text": "空腹胆囊充盈差、腔内透声差，慢性胆囊炎？请结合临床", "bbox": [183, 827, 684, 843]},
	{"text": "肝囊肿", "bbox": [183, 842, 243, 858]},
	{"text": "右肾略高回声结节，考虑良性（结合病史考虑复杂囊肿可能）", "bbox": [183, 856, 713, 873]},
	{"text": "前列腺增生并钙化", "bbox": [183, 871, 345, 887]},
	{"text": "报告日期：2026-01-27 08:35:35 记录人", "bbox": [91, 901, 444, 917]},
	{"text": "CS 扫描全能王", "bbox": [862, 958, 977, 973]}
]
2026-08-10 17:47:50,684 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=14.8s
2026-08-10 17:47:50,684 INFO     29 [qwen-vl-text] coord item[0]: text=超声检查报告单, bbox=[335, 86, 652, 109]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[1]: text=思者登, bbox=[91, 121, 158, 137]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[2]: text=姓, bbox=[131, 151, 151, 165]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[433, 151, 523, 167]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：75岁, bbox=[655, 151, 763, 167]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[5]: text=床号：A02, bbox=[655, 180, 756, 196]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[6]: text=检查所见：, bbox=[91, 458, 180, 475]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[7]: text=右肝最大斜径12.8cm，左肝前后径6.4cm，上下径7.5cm，肝表面光滑，边缘规则，肝内, bbox=[91, 473, 895, 490]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[8]: text=呈细小点状回声，分布欠均匀，肝内见数个囊性回声，大者0.8x0.5cm，均透声可。, bbox=[91, 488, 814, 504]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[9]: text=空腹胆囊充盈差，胆囊区见胆囊祥回声，大小约3.4x1.4cm，腔内透声差，充满细密点, bbox=[91, 503, 884, 520]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[10]: text=状回声。, bbox=[91, 517, 162, 533]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[11]: text=胆总管内径0.5cm，未见明显异常回声，肝内胆管无明显扩张。, bbox=[133, 532, 673, 548]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[12]: text=胰腺大小形态可，表面光滑，内回声均匀，主胰管内径不宽。, bbox=[133, 547, 664, 563]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[13]: text=脾未探及。, bbox=[133, 562, 222, 578]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[14]: text=门静脉走行自然，呈入肝血流，门静脉主干内径1.0cm，入肝血流速度17.4cm/s，肝内, bbox=[133, 576, 884, 593]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[15]: text=门静脉血流充盈好，未见明显异常回声。, bbox=[91, 591, 444, 607]
2026-08-10 17:47:50,685 INFO     29 [qwen-vl-text] coord item[16]: text=肝静脉走行自然，各支内径不宽，腔内未见明显异常回声，血流速及频谱形态未见异, bbox=[133, 606, 874, 622]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[17]: text=常。, bbox=[91, 620, 123, 636]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[18]: text=双侧肾上腺区未见明显占位性病变。, bbox=[133, 635, 444, 651]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[19]: text=双肾大小形态正常，表面光滑，皮髓质分界清，左肾实质回声无明显异常，右肾中部实, bbox=[133, 650, 895, 666]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[20]: text=质内见1.5x1.2cm略高回声结节，边界清，双肾窦无分离扩张。, bbox=[91, 664, 634, 680]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[21]: text=双侧输尿管无明显扩张。, bbox=[133, 679, 343, 695]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[22]: text=膀胱充盈可，黏膜光滑，腔内未见明显占位。, bbox=[133, 694, 523, 710]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[23]: text=前列腺大小约4.0（左右径）×3.5（前后径）×3.2（上下径）cm，体积约23.3cm3，, bbox=[133, 708, 872, 725]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[24]: text=表面光滑，中叶略突，内部回声欠均匀。, bbox=[91, 723, 444, 739]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[25]: text=双侧精囊腺无肿大，内部回声均匀。, bbox=[133, 738, 444, 754]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[26]: text=双肾动脉主干血流通畅，肾内动脉血流分布好。, bbox=[133, 752, 544, 768]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[27]: text=左肾叶间动脉Vs 24.8cm/s，阻力指数（RI）0.66。, bbox=[133, 767, 573, 783]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[28]: text=右肾叶间动脉Vs 25.1cm/s，阻力指数（RI）0.65。, bbox=[133, 781, 573, 798]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[29]: text=超声提示：脾切除术后, bbox=[91, 811, 283, 828]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[30]: text=空腹胆囊充盈差、腔内透声差，慢性胆囊炎？请结合临床, bbox=[183, 827, 684, 843]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[31]: text=肝囊肿, bbox=[183, 842, 243, 858]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[32]: text=右肾略高回声结节，考虑良性（结合病史考虑复杂囊肿可能）, bbox=[183, 856, 713, 873]
2026-08-10 17:47:50,686 INFO     29 [qwen-vl-text] coord item[33]: text=前列腺增生并钙化, bbox=[183, 871, 345, 887]
2026-08-10 17:47:50,687 INFO     29 [qwen-vl-text] coord item[34]: text=报告日期：2026-01-27 08:35:35 记录人, bbox=[91, 901, 444, 917]
2026-08-10 17:47:50,687 INFO     29 [qwen-vl-text] coord item[35]: text=CS 扫描全能王, bbox=[862, 958, 977, 973]
2026-08-10 17:47:50,687 INFO     29 [qwen-vl-text] page=14 — 36/36 coords, api_time=14.8s
2026-08-10 17:47:50,687 INFO     29 [qwen-vl-text] new_positions (36):
[[14, 199.325, 387.94, 72.41199999999999, 91.77799999999999], [14, 54.144999999999996, 94.00999999999999, 101.88199999999999, 115.354], [14, 77.945, 89.845, 127.142, 138.93], [14, 257.635, 311.185, 127.142, 140.614], [14, 389.72499999999997, 453.98499999999996, 127.142, 140.614], [14, 389.72499999999997, 449.82, 151.56, 165.03199999999998], [14, 54.144999999999996, 107.1, 385.63599999999997, 399.95], [14, 54.144999999999996, 532.525, 398.26599999999996, 412.58], [14, 54.144999999999996, 484.33, 410.89599999999996, 424.368], [14, 54.144999999999996, 525.98, 423.526, 437.84], [14, 54.144999999999996, 96.39, 435.31399999999996, 448.786], [14, 79.13499999999999, 400.435, 447.94399999999996, 461.416], [14, 79.13499999999999, 395.08, 460.574, 474.046], [14, 79.13499999999999, 132.09, 473.204, 486.676], [14, 79.13499999999999, 525.98, 484.99199999999996, 499.306], [14, 54.144999999999996, 264.18, 497.62199999999996, 511.094], [14, 79.13499999999999, 520.03, 510.252, 523.7239999999999], [14, 54.144999999999996, 73.185, 522.04, 535.512], [14, 79.13499999999999, 264.18, 534.67, 548.1419999999999], [14, 79.13499999999999, 532.525, 547.3, 560.7719999999999], [14, 54.144999999999996, 377.22999999999996, 559.088, 572.56], [14, 79.13499999999999, 204.08499999999998, 571.718, 585.1899999999999], [14, 79.13499999999999, 311.185, 584.348, 597.8199999999999], [14, 79.13499999999999, 518.84, 596.136, 610.4499999999999], [14, 54.144999999999996, 264.18, 608.766, 622.2379999999999], [14, 79.13499999999999, 264.18, 621.396, 634.8679999999999], [14, 79.13499999999999, 323.68, 633.184, 646.656], [14, 79.13499999999999, 340.935, 645.814, 659.286], [14, 79.13499999999999, 340.935, 657.602, 671.9159999999999], [14, 54.144999999999996, 168.385, 682.862, 697.1759999999999], [14, 108.88499999999999, 406.97999999999996, 696.334, 709.8059999999999], [14, 108.88499999999999, 144.58499999999998, 708.9639999999999, 722.4359999999999], [14, 108.88499999999999, 424.23499999999996, 720.752, 735.066], [14, 108.88499999999999, 205.27499999999998, 733.382, 746.8539999999999], [14, 54.144999999999996, 264.18, 758.6419999999999, 772.1139999999999], [14, 512.89, 581.3149999999999, 806.636, 819.266]]
2026-08-10 17:47:50,687 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=1, time=20.6s
2026-08-10 17:47:50,688 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:47:50,690 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:47:50,690 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:47:50,690 INFO     29 [qwen-vl-text] positions(19): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:47:50,690 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [19]
2026-08-10 17:47:50,850 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:47:50,851 INFO     29 [qwen-vl-text] LLM extraction start, text_len=301
2026-08-10 17:47:50,851 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:47:50,851 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3838, \"bbox_end\": 3856, \"encounter_dates\": [\"2026-01-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "超声检查报告单\n患者登记\n姓名：\n性别：男\n年龄：75岁\n号\n1\n2\n检查所见：\n甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。\n甲状旁腺区未见明显异常回声。\n左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门\n髓结构不清，CDFI：内见条状血流信号。\n右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。\n超声提示：左侧颈部淋巴结肿大，考虑“M”性可能\n报告日期：2026-01-27 08:26:34 记\n名.\n注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。\nCS 扫描全能王",
    "role": "user"
  }
]
2026-08-10 17:47:53,430 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:47:53,430 INFO     29 [qwen-vl-text] LLM output (len=488):
{
  "exam_date": "2026-01-27",
  "report_date": "2026-01-27",
  "exam_name": "超声检查",
  "exam_category": "imaging",
  "body_part": "甲状腺、颈部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。\n甲状旁腺区未见明显异常回声。\n左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门髓结构不清，CDFI：内见条状血流信号。\n右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。",
  "conclusion": "左侧颈部淋巴结肿大，考虑“M”性可能",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:47:53,431 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1153055, prompt_len=971
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["超声检查报告单", "患者登记", "姓名：", "性别：男", "年龄：75岁", "号", "1", "2", "检查所见：", "甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。", "甲状旁腺区未见明显异常回声。", "左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门", "髓结构不清，CDFI：内见条状血流信号。", "右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。", "超声提示：左侧颈部淋巴结肿大，考虑“M”性可能", "报告日期：2026-01-27 08:26:34 记", "名.", "注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。", "CS 扫描全能王"]

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
2026-08-10 17:47:59,861 INFO     29 [qwen-vl-text] coord API raw response (len=1134):
[
	{"text": "超声检查报告单", "bbox": [326, 84, 657, 107]},
	{"text": "患者登记", "bbox": [77, 120, 160, 136]},
	{"text": "姓名：", "bbox": [118, 150, 172, 166]},	
	{"text": "性别：男", "bbox": [428, 150, 523, 167]},
	{"text": "年龄：75岁", "bbox": [659, 150, 773, 166]},
	{"text": "号", "bbox": [705, 180, 719, 195]},
	{"text": "1", "bbox": [103, 224, 120, 238]},
	{"text": "2", "bbox": [500, 224, 517, 238]},
	{"text": "检查所见：", "bbox": [77, 459, 167, 475]},
	{"text": "甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。", "bbox": [118, 480, 911, 497]},
	{"text": "甲状旁腺区未见明显异常回声。", "bbox": [118, 524, 398, 540]},
	{"text": "左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门", "bbox": [118, 546, 901, 564]},
	{"text": "髓结构不清，CDFI：内见条状血流信号。", "bbox": [77, 568, 440, 585]},
	{"text": "右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。", "bbox": [118, 590, 670, 608]},
	{"text": "超声提示：左侧颈部淋巴结肿大，考虑“M”性可能", "bbox": [77, 762, 535, 779]},
	{"text": "报告日期：2026-01-27 08:26:34 记", "bbox": [77, 792, 398, 809]},
	{"text": "名.", "bbox": [624, 792, 657, 809]},
	{"text": "注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。", "bbox": [77, 834, 797, 851]},
	{"text": "CS 扫描全能王", "bbox": [862, 958, 977, 974]}
]
2026-08-10 17:47:59,862 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=6.4s
2026-08-10 17:47:59,862 INFO     29 [qwen-vl-text] coord item[0]: text=超声检查报告单, bbox=[326, 84, 657, 107]
2026-08-10 17:47:59,862 INFO     29 [qwen-vl-text] coord item[1]: text=患者登记, bbox=[77, 120, 160, 136]
2026-08-10 17:47:59,862 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[118, 150, 172, 166]
2026-08-10 17:47:59,862 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[428, 150, 523, 167]
2026-08-10 17:47:59,862 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：75岁, bbox=[659, 150, 773, 166]
2026-08-10 17:47:59,862 INFO     29 [qwen-vl-text] coord item[5]: text=号, bbox=[705, 180, 719, 195]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[6]: text=1, bbox=[103, 224, 120, 238]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[7]: text=2, bbox=[500, 224, 517, 238]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[8]: text=检查所见：, bbox=[77, 459, 167, 475]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[9]: text=甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。, bbox=[118, 480, 911, 497]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[10]: text=甲状旁腺区未见明显异常回声。, bbox=[118, 524, 398, 540]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[11]: text=左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门, bbox=[118, 546, 901, 564]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[12]: text=髓结构不清，CDFI：内见条状血流信号。, bbox=[77, 568, 440, 585]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[13]: text=右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。, bbox=[118, 590, 670, 608]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[14]: text=超声提示：左侧颈部淋巴结肿大，考虑“M”性可能, bbox=[77, 762, 535, 779]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[15]: text=报告日期：2026-01-27 08:26:34 记, bbox=[77, 792, 398, 809]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[16]: text=名., bbox=[624, 792, 657, 809]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[17]: text=注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。, bbox=[77, 834, 797, 851]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] coord item[18]: text=CS 扫描全能王, bbox=[862, 958, 977, 974]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] page=15 — 19/19 coords, api_time=6.4s
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] new_positions (19):
[[15, 193.97, 390.91499999999996, 70.728, 90.094], [15, 45.815, 95.19999999999999, 101.03999999999999, 114.512], [15, 70.21, 102.33999999999999, 126.3, 139.772], [15, 254.66, 311.185, 126.3, 140.614], [15, 392.10499999999996, 459.935, 126.3, 139.772], [15, 419.47499999999997, 427.805, 151.56, 164.19], [15, 61.285, 71.39999999999999, 188.608, 200.396], [15, 297.5, 307.615, 188.608, 200.396], [15, 45.815, 99.365, 386.478, 399.95], [15, 70.21, 542.045, 404.15999999999997, 418.474], [15, 70.21, 236.81, 441.20799999999997, 454.68], [15, 70.21, 536.095, 459.73199999999997, 474.888], [15, 45.815, 261.8, 478.256, 492.57], [15, 70.21, 398.65, 496.78, 511.936], [15, 45.815, 318.325, 641.6039999999999, 655.918], [15, 45.815, 236.81, 666.864, 681.178], [15, 371.28, 390.91499999999996, 666.864, 681.178], [15, 45.815, 474.215, 702.228, 716.542], [15, 512.89, 581.3149999999999, 806.636, 820.108]]
2026-08-10 17:47:59,863 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=9.2s
2026-08-10 17:47:59,863 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:47:59,864 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:47:59,865 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:47:59,865 INFO     29 [qwen-vl-text] positions(26): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:47:59,865 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [26]
2026-08-10 17:48:00,015 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:48:00,015 INFO     29 [qwen-vl-text] LLM extraction start, text_len=501
2026-08-10 17:48:00,015 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:00,015 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3858, \"bbox_end\": 3883, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "影像学检查报告单\n扫一扫查看云胶片（访问码）：\n姓名：\n性别：男\n年龄：75岁\n影像\n住院号：\n登记号：\n检查名称：胸部CT增强成像（单独）\n检查方法：AXI+C\n图像所见：胸廓及胸腔容积基本正常。纵隔左偏。左肺可见软组织密度肿块，边界不\n清，大小约59mm*66mm，较前2024.09.03CT所示明显增大，呈不均匀强\n化。左主支气管及左肺上叶、下叶支气管狭窄，其远端肺组织实变，较前\n相仿。左肺下叶后基底段(6im53-54)见实性结节，大小约为11mm×8mm。\n双肺见多发小、微结节，较大者位于左肺下叶背段(6im39-41)，呈实性\n密度，大小约为9mm×7mm。双肺见多发斑片、索条影。气管未见狭窄或梗\n阻。纵隔及左肺门可见多发肿大淋巴结，较前相仿。心影未见明显增大。\n左侧部分肋骨局部形态不规整。\n印象：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床\n双肺多发结节，较前增多、增大，请结合临床随访\n双肺慢性炎症或纤维灶可能性大，请结合临床\n左侧部分肋骨局部形态不规整，请结合临床\n报告医师\n审核医\n该报告仅供临床医师参考；如需商榷，请通过临床医师与审核医师沟通\n流水号",
    "role": "user"
  }
]
2026-08-10 17:48:02,412 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:48:02.412+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:48:03,514 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:03,515 INFO     29 [qwen-vl-text] LLM output (len=661):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "胸部CT增强成像（单独）",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "胸廓及胸腔容积基本正常。纵隔左偏。左肺可见软组织密度肿块，边界不清，大小约59mm*66mm，较前2024.09.03CT所示明显增大，呈不均匀强化。左主支气管及左肺上叶、下叶支气管狭窄，其远端肺组织实变，较前相仿。左肺下叶后基底段(6im53-54)见实性结节，大小约为11mm×8mm。双肺见多发小、微结节，较大者位于左肺下叶背段(6im39-41)，呈实性密度，大小约为9mm×7mm。双肺见多发斑片、索条影。气管未见狭窄或梗阻。纵隔及左肺门可见多发肿大淋巴结，较前相仿。心影未见明显增大。左侧部分肋骨局部形态不规整。",
  "conclusion": "左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床\n双肺多发结节，较前增多、增大，请结合临床随访\n双肺慢性炎症或纤维灶可能性大，请结合临床\n左侧部分肋骨局部形态不规整，请结合临床",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:48:03,517 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1003705, prompt_len=1192
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["影像学检查报告单", "扫一扫查看云胶片（访问码）：", "姓名：", "性别：男", "年龄：75岁", "影像", "住院号：", "登记号：", "检查名称：胸部CT增强成像（单独）", "检查方法：AXI+C", "图像所见：胸廓及胸腔容积基本正常。纵隔左偏。左肺可见软组织密度肿块，边界不", "清，大小约59mm*66mm，较前2024.09.03CT所示明显增大，呈不均匀强", "化。左主支气管及左肺上叶、下叶支气管狭窄，其远端肺组织实变，较前", "相仿。左肺下叶后基底段(6im53-54)见实性结节，大小约为11mm×8mm。", "双肺见多发小、微结节，较大者位于左肺下叶背段(6im39-41)，呈实性", "密度，大小约为9mm×7mm。双肺见多发斑片、索条影。气管未见狭窄或梗", "阻。纵隔及左肺门可见多发肿大淋巴结，较前相仿。心影未见明显增大。", "左侧部分肋骨局部形态不规整。", "印象：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床", "双肺多发结节，较前增多、增大，请结合临床随访", "双肺慢性炎症或纤维灶可能性大，请结合临床", "左侧部分肋骨局部形态不规整，请结合临床", "报告医师", "审核医", "该报告仅供临床医师参考；如需商榷，请通过临床医师与审核医师沟通", "流水号"]

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
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord API raw response (len=1647):
[
	{"text": "影像学检查报告单", "bbox": [382, 89, 613, 110]},
	{"text": "扫一扫查看云胶片（访问码）：", "bbox": [422, 144, 638, 157]},
	{"text": "姓名：", "bbox": [103, 173, 144, 186]},
	{"text": "性别：男", "bbox": [285, 173, 360, 186]},
	{"text": "年龄：75岁", "bbox": [470, 173, 566, 186]},
	{"text": "影像", "bbox": [649, 173, 679, 186]},
	{"text": "住院号：", "bbox": [649, 200, 705, 212]},
	{"text": "登记号：", "bbox": [649, 227, 723, 240]},
	{"text": "检查名称：胸部CT增强成像（单独）", "bbox": [103, 269, 429, 285]},
	{"text": "检查方法：AXI+C", "bbox": [103, 304, 266, 319]},
	{"text": "图像所见：胸廓及胸腔容积基本正常。纵隔左偏。左肺可见软组织密度肿块，边界不", "bbox": [104, 360, 828, 376]},
	{"text": "清，大小约59mm*66mm，较前2024.09.03CT所示明显增大，呈不均匀强", "bbox": [216, 384, 813, 399]},
	{"text": "化。左主支气管及左肺上叶、下叶支气管狭窄，其远端肺组织实变，较前", "bbox": [216, 407, 826, 422]},
	{"text": "相仿。左肺下叶后基底段(6im53-54)见实性结节，大小约为11mm×8mm。", "bbox": [216, 430, 820, 445]},
	{"text": "双肺见多发小、微结节，较大者位于左肺下叶背段(6im39-41)，呈实性", "bbox": [216, 453, 816, 468]},
	{"text": "密度，大小约为9mm×7mm。双肺见多发斑片、索条影。气管未见狭窄或梗", "bbox": [216, 476, 831, 491]},
	{"text": "阻。纵隔及左肺门可见多发肿大淋巴结，较前相仿。心影未见明显增大。", "bbox": [216, 499, 816, 514]},
	{"text": "左侧部分肋骨局部形态不规整。", "bbox": [216, 521, 477, 536]},
	{"text": "印象：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床", "bbox": [104, 633, 826, 650]},
	{"text": "双肺多发结节，较前增多、增大，请结合临床随访", "bbox": [216, 657, 637, 672]},
	{"text": "双肺慢性炎症或纤维灶可能性大，请结合临床", "bbox": [216, 680, 600, 695]},
	{"text": "左侧部分肋骨局部形态不规整，请结合临床", "bbox": [216, 703, 581, 718]},
	{"text": "报告医师", "bbox": [198, 847, 261, 860]},
	{"text": "审核医", "bbox": [532, 847, 594, 860]},
	{"text": "该报告仅供临床医师参考；如需商榷，请通过临床医师与审核医师沟通", "bbox": [103, 869, 548, 881]},
	{"text": "流水号", "bbox": [103, 891, 145, 903]}
]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=11.2s
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[0]: text=影像学检查报告单, bbox=[382, 89, 613, 110]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[1]: text=扫一扫查看云胶片（访问码）：, bbox=[422, 144, 638, 157]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[103, 173, 144, 186]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[285, 173, 360, 186]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：75岁, bbox=[470, 173, 566, 186]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[5]: text=影像, bbox=[649, 173, 679, 186]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[6]: text=住院号：, bbox=[649, 200, 705, 212]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[7]: text=登记号：, bbox=[649, 227, 723, 240]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[8]: text=检查名称：胸部CT增强成像（单独）, bbox=[103, 269, 429, 285]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[9]: text=检查方法：AXI+C, bbox=[103, 304, 266, 319]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[10]: text=图像所见：胸廓及胸腔容积基本正常。纵隔左偏。左肺可见软组织密度肿块，边界不, bbox=[104, 360, 828, 376]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[11]: text=清，大小约59mm*66mm，较前2024.09.03CT所示明显增大，呈不均匀强, bbox=[216, 384, 813, 399]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[12]: text=化。左主支气管及左肺上叶、下叶支气管狭窄，其远端肺组织实变，较前, bbox=[216, 407, 826, 422]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[13]: text=相仿。左肺下叶后基底段(6im53-54)见实性结节，大小约为11mm×8mm。, bbox=[216, 430, 820, 445]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[14]: text=双肺见多发小、微结节，较大者位于左肺下叶背段(6im39-41)，呈实性, bbox=[216, 453, 816, 468]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[15]: text=密度，大小约为9mm×7mm。双肺见多发斑片、索条影。气管未见狭窄或梗, bbox=[216, 476, 831, 491]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[16]: text=阻。纵隔及左肺门可见多发肿大淋巴结，较前相仿。心影未见明显增大。, bbox=[216, 499, 816, 514]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[17]: text=左侧部分肋骨局部形态不规整。, bbox=[216, 521, 477, 536]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[18]: text=印象：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床, bbox=[104, 633, 826, 650]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[19]: text=双肺多发结节，较前增多、增大，请结合临床随访, bbox=[216, 657, 637, 672]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[20]: text=双肺慢性炎症或纤维灶可能性大，请结合临床, bbox=[216, 680, 600, 695]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[21]: text=左侧部分肋骨局部形态不规整，请结合临床, bbox=[216, 703, 581, 718]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[22]: text=报告医师, bbox=[198, 847, 261, 860]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[23]: text=审核医, bbox=[532, 847, 594, 860]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[24]: text=该报告仅供临床医师参考；如需商榷，请通过临床医师与审核医师沟通, bbox=[103, 869, 548, 881]
2026-08-10 17:48:14,733 INFO     29 [qwen-vl-text] coord item[25]: text=流水号, bbox=[103, 891, 145, 903]
2026-08-10 17:48:14,734 INFO     29 [qwen-vl-text] page=16 — 26/26 coords, api_time=11.2s
2026-08-10 17:48:14,734 INFO     29 [qwen-vl-text] new_positions (26):
[[16, 227.29, 364.73499999999996, 74.938, 92.61999999999999], [16, 251.08999999999997, 379.60999999999996, 121.24799999999999, 132.194], [16, 61.285, 85.67999999999999, 145.666, 156.612], [16, 169.575, 214.2, 145.666, 156.612], [16, 279.65, 336.77, 145.666, 156.612], [16, 386.155, 404.005, 145.666, 156.612], [16, 386.155, 419.47499999999997, 168.4, 178.504], [16, 386.155, 430.185, 191.134, 202.07999999999998], [16, 61.285, 255.255, 226.498, 239.97], [16, 61.285, 158.26999999999998, 255.968, 268.598], [16, 61.879999999999995, 492.65999999999997, 303.12, 316.592], [16, 128.51999999999998, 483.73499999999996, 323.328, 335.95799999999997], [16, 128.51999999999998, 491.46999999999997, 342.69399999999996, 355.324], [16, 128.51999999999998, 487.9, 362.06, 374.69], [16, 128.51999999999998, 485.52, 381.426, 394.056], [16, 128.51999999999998, 494.445, 400.792, 413.42199999999997], [16, 128.51999999999998, 485.52, 420.15799999999996, 432.788], [16, 128.51999999999998, 283.815, 438.68199999999996, 451.312], [16, 61.879999999999995, 491.46999999999997, 532.986, 547.3], [16, 128.51999999999998, 379.015, 553.194, 565.824], [16, 128.51999999999998, 357.0, 572.56, 585.1899999999999], [16, 128.51999999999998, 345.695, 591.9259999999999, 604.5559999999999], [16, 117.80999999999999, 155.295, 713.174, 724.12], [16, 316.53999999999996, 353.43, 713.174, 724.12], [16, 61.285, 326.06, 731.698, 741.802], [16, 61.285, 86.27499999999999, 750.222, 760.326]]
2026-08-10 17:48:14,734 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=14.9s
2026-08-10 17:48:14,734 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:48:14,735 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:48:14,735 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:48:14,735 INFO     29 [qwen-vl-text] positions(22): [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:48:14,735 INFO     29 [qwen-vl-text] page grouping: [17], lines per page: [22]
2026-08-10 17:48:14,869 INFO     29 [qwen-vl-text] page=17, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:48:14,870 INFO     29 [qwen-vl-text] LLM extraction start, text_len=332
2026-08-10 17:48:14,870 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:14,870 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3884, \"bbox_end\": 3905, \"encounter_dates\": [\"2020-12-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "影像学检查报告单\n姓名：\n性别：男\n年龄：70岁\n影像\n检查日期：2020-12-23\n报告日期：2020-12-23\n报告时间：10.00\n检查名称：全身骨显像\n检查方法：显像剂：99mTc-MDP\n图像所见：静脉注射显像剂2小时后行全身骨显像，图像清晰，对比度可。\n前位：双侧膝关节见显像剂浓聚灶。颅骨，锁骨，胸骨，前肋，骨盆显像\n剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。\n后位：脊椎见显像剂浓聚灶。颅骨，肩胛骨，后肋，骨盆显像剂分布基本\n左右对称，未见明显异常显像剂浓聚或稀疏区。\n印\n象：1，脊椎及双侧膝关节退行性变可能性大\n2，其余部位骨骼未见明显转移瘤，建议定期复查\n报告[\n审核医师：\n该报告反映受检者当时情况，仅供临床医师参考。\n流水号",
    "role": "user"
  }
]
2026-08-10 17:48:17,724 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:17,724 INFO     29 [qwen-vl-text] LLM output (len=504):
{
  "exam_date": "2020-12-23",
  "report_date": "2020-12-23",
  "exam_name": "全身骨显像",
  "exam_category": "imaging",
  "body_part": "全身骨骼",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "图像所见：静脉注射显像剂2小时后行全身骨显像，图像清晰，对比度可。\n前位：双侧膝关节见显像剂浓聚灶。颅骨，锁骨，胸骨，前肋，骨盆显像剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。\n后位：脊椎见显像剂浓聚灶。颅骨，肩胛骨，后肋，骨盆显像剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。",
  "conclusion": "印象：1，脊椎及双侧膝关节退行性变可能性大\n2，其余部位骨骼未见明显转移瘤，建议定期复查",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:48:17,725 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=731207, prompt_len=1011
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["影像学检查报告单", "姓名：", "性别：男", "年龄：70岁", "影像", "检查日期：2020-12-23", "报告日期：2020-12-23", "报告时间：10.00", "检查名称：全身骨显像", "检查方法：显像剂：99mTc-MDP", "图像所见：静脉注射显像剂2小时后行全身骨显像，图像清晰，对比度可。", "前位：双侧膝关节见显像剂浓聚灶。颅骨，锁骨，胸骨，前肋，骨盆显像", "剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。", "后位：脊椎见显像剂浓聚灶。颅骨，肩胛骨，后肋，骨盆显像剂分布基本", "左右对称，未见明显异常显像剂浓聚或稀疏区。", "印", "象：1，脊椎及双侧膝关节退行性变可能性大", "2，其余部位骨骼未见明显转移瘤，建议定期复查", "报告[", "审核医师：", "该报告反映受检者当时情况，仅供临床医师参考。", "流水号"]

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
2026-08-10 17:48:28,300 INFO     29 [qwen-vl-text] coord API raw response (len=1915):
[
	{"text": "影像学检查报告单", "bbox": [364, 68, 601, 90]},
	{"text": "姓名：", "bbox": [94, 113, 141, 126], "bbox": [94, 113, 141, 126]},
	{"text": "性别：男", "bbox": [278, 113, 357, 126], "bbox": [278, 113, 357, 126]},
	{"text": "年龄：70岁", "bbox": [469, 113, 567, 126], "bbox": [469, 113, 567, 126]},
	{"text": "影像", "bbox": [652, 113, 687, 126], "bbox": [652, 113, 687, 126]},
	{"text": "检查日期：2020-12-23", "bbox": [94, 157, 258, 169], "bbox": [94, 157, 258, 169]},
	{"text": "报告日期：2020-12-23", "bbox": [278, 157, 445, 169], "bbox": [278, 157, 445, 169]},
	{"text": "报告时间：10.00", "bbox": [469, 157, 615, 169], "bbox": [469, 157, 615, 169]},
	{"text": "检查名称：全身骨显像", "bbox": [94, 198, 308, 214], "bbox": [94, 198, 308, 214]},
	{"text": "检查方法：显像剂：99mTc-MDP", "bbox": [94, 232, 376, 248], "bbox": [94, 232, 376, 248]},
	{"text": "图像所见：静脉注射显像剂2小时后行全身骨显像，图像清晰，对比度可。", "bbox": [94, 286, 746, 302], "bbox": [94, 286, 746, 302]},
	{"text": "前位：双侧膝关节见显像剂浓聚灶。颅骨，锁骨，胸骨，前肋，骨盆显像", "bbox": [208, 310, 833, 326], "bbox": [208, 310, 833, 326]},
	{"text": "剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。", "bbox": [208, 334, 708, 349], "bbox": [208, 334, 708, 349]},
	{"text": "后位：脊椎见显像剂浓聚灶。颅骨，肩胛骨，后肋，骨盆显像剂分布基本", "bbox": [208, 357, 833, 373], "bbox": [208, 357, 833, 373]},
	{"text": "左右对称，未见明显异常显像剂浓聚或稀疏区。", "bbox": [208, 380, 611, 395], "bbox": [208, 380, 611, 395]},
	{"text": "印", "bbox": [94, 560, 115, 576], "bbox": [94, 560, 115, 576]},
	{"text": "象：1，脊椎及双侧膝关节退行性变可能性大", "bbox": [154, 561, 553, 577], "bbox": [154, 561, 553, 577]},
	{"text": "2，其余部位骨骼未见明显转移瘤，建议定期复查", "bbox": [208, 584, 630, 600], "bbox": [208, 584, 630, 600]},
	{"text": "报告[", "bbox": [193, 847, 234, 861], "bbox": [193, 847, 234, 861]},
	{"text": "审核医师：", "bbox": [534, 847, 608, 861], "bbox": [534, 847, 608, 861]},
	{"text": "该报告反映受检者当时情况，仅供临床医师参考。", "bbox": [98, 869, 412, 881], "bbox": [98, 869, 412, 881]},
	{"text": "流水号", "bbox": [98, 891, 141, 903], "bbox": [98, 891, 141, 903]}
]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=10.6s
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[0]: text=影像学检查报告单, bbox=[364, 68, 601, 90]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[94, 113, 141, 126]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[278, 113, 357, 126]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：70岁, bbox=[469, 113, 567, 126]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[4]: text=影像, bbox=[652, 113, 687, 126]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[5]: text=检查日期：2020-12-23, bbox=[94, 157, 258, 169]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[6]: text=报告日期：2020-12-23, bbox=[278, 157, 445, 169]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[7]: text=报告时间：10.00, bbox=[469, 157, 615, 169]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[8]: text=检查名称：全身骨显像, bbox=[94, 198, 308, 214]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[9]: text=检查方法：显像剂：99mTc-MDP, bbox=[94, 232, 376, 248]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[10]: text=图像所见：静脉注射显像剂2小时后行全身骨显像，图像清晰，对比度可。, bbox=[94, 286, 746, 302]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[11]: text=前位：双侧膝关节见显像剂浓聚灶。颅骨，锁骨，胸骨，前肋，骨盆显像, bbox=[208, 310, 833, 326]
2026-08-10 17:48:28,301 INFO     29 [qwen-vl-text] coord item[12]: text=剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。, bbox=[208, 334, 708, 349]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[13]: text=后位：脊椎见显像剂浓聚灶。颅骨，肩胛骨，后肋，骨盆显像剂分布基本, bbox=[208, 357, 833, 373]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[14]: text=左右对称，未见明显异常显像剂浓聚或稀疏区。, bbox=[208, 380, 611, 395]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[15]: text=印, bbox=[94, 560, 115, 576]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[16]: text=象：1，脊椎及双侧膝关节退行性变可能性大, bbox=[154, 561, 553, 577]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[17]: text=2，其余部位骨骼未见明显转移瘤，建议定期复查, bbox=[208, 584, 630, 600]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[18]: text=报告[, bbox=[193, 847, 234, 861]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[19]: text=审核医师：, bbox=[534, 847, 608, 861]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[20]: text=该报告反映受检者当时情况，仅供临床医师参考。, bbox=[98, 869, 412, 881]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] coord item[21]: text=流水号, bbox=[98, 891, 141, 903]
2026-08-10 17:48:28,302 INFO     29 [qwen-vl-text] page=17 — 22/22 coords, api_time=10.6s
2026-08-10 17:48:28,303 INFO     29 [qwen-vl-text] new_positions (22):
[[17, 216.57999999999998, 357.59499999999997, 57.256, 75.78], [17, 55.93, 83.895, 95.146, 106.092], [17, 165.41, 212.415, 95.146, 106.092], [17, 279.055, 337.365, 95.146, 106.092], [17, 387.94, 408.765, 95.146, 106.092], [17, 55.93, 153.51, 132.194, 142.298], [17, 165.41, 264.775, 132.194, 142.298], [17, 279.055, 365.925, 132.194, 142.298], [17, 55.93, 183.26, 166.716, 180.188], [17, 55.93, 223.72, 195.344, 208.816], [17, 55.93, 443.87, 240.81199999999998, 254.284], [17, 123.75999999999999, 495.635, 261.02, 274.492], [17, 123.75999999999999, 421.26, 281.228, 293.858], [17, 123.75999999999999, 495.635, 300.594, 314.066], [17, 123.75999999999999, 363.54499999999996, 319.96, 332.59], [17, 55.93, 68.425, 471.52, 484.99199999999996], [17, 91.63, 329.03499999999997, 472.36199999999997, 485.834], [17, 123.75999999999999, 374.84999999999997, 491.728, 505.2], [17, 114.835, 139.23, 713.174, 724.962], [17, 317.72999999999996, 361.76, 713.174, 724.962], [17, 58.309999999999995, 245.14, 731.698, 741.802], [17, 58.309999999999995, 83.895, 750.222, 760.326]]
2026-08-10 17:48:28,303 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=13.6s
2026-08-10 17:48:28,303 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:48:28,304 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:48:28,305 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:48:28,305 INFO     29 [qwen-vl-text] positions(25): [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:48:28,305 INFO     29 [qwen-vl-text] page grouping: [18], lines per page: [25]
2026-08-10 17:48:28,424 INFO     29 [qwen-vl-text] page=18, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:48:28,424 INFO     29 [qwen-vl-text] LLM extraction start, text_len=323
2026-08-10 17:48:28,424 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:28,425 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3907, \"bbox_end\": 3931, \"encounter_dates\": [\"2020-12-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "影像学检查报告单\n扫码看电子胶片\n姓\n性别：男\n年龄：70岁\n影像\n科\n住院\n检查日期：2020-12-22\n报告日期：2020-12-23\n报告时间：14:22:52\n登记号\n40\n检查名称：颅脑MR平扫成像+DWI成像\n检查方法：AXI:FSE T1WI, T2WI, FLAIR, DWI\nSAG:FSE T1WI\n图像所见：双侧额顶叶白质可见散在斑点状等T1稍长T2信号影，FLAIR为高信号，\nDWI为等信号。脑室系统略扩大，脑沟、脑池明显加深，中线结构居中。\n印象：1. 血管性脱髓鞘（Fazekas 1级），请结合临床复查\n2. 老年性脑改变\n报告\n审核医师：\n该报告反映受检者当时情况，仅供临床医师参考。\n流水号\nCS 扫描全能王",
    "role": "user"
  }
]
2026-08-10 17:48:30,875 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:30,875 INFO     29 [qwen-vl-text] LLM output (len=434):
{
  "exam_date": "2020-12-22",
  "report_date": "2020-12-23",
  "exam_name": "颅脑MR平扫成像+DWI成像",
  "exam_category": "imaging",
  "body_part": "颅脑",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "图像所见：双侧额顶叶白质可见散在斑点状等T1稍长T2信号影，FLAIR为高信号，DWI为等信号。脑室系统略扩大，脑沟、脑池明显加深，中线结构居中。",
  "conclusion": "印象：1. 血管性脱髓鞘（Fazekas 1级），请结合临床复查\n2. 老年性脑改变",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:48:30,878 INFO     29 [qwen-vl-text] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=576212, prompt_len=1011
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["影像学检查报告单", "扫码看电子胶片", "姓", "性别：男", "年龄：70岁", "影像", "科", "住院", "检查日期：2020-12-22", "报告日期：2020-12-23", "报告时间：14:22:52", "登记号", "40", "检查名称：颅脑MR平扫成像+DWI成像", "检查方法：AXI:FSE T1WI, T2WI, FLAIR, DWI", "SAG:FSE T1WI", "图像所见：双侧额顶叶白质可见散在斑点状等T1稍长T2信号影，FLAIR为高信号，", "DWI为等信号。脑室系统略扩大，脑沟、脑池明显加深，中线结构居中。", "印象：1. 血管性脱髓鞘（Fazekas 1级），请结合临床复查", "2. 老年性脑改变", "报告", "审核医师：", "该报告反映受检者当时情况，仅供临床医师参考。", "流水号", "CS 扫描全能王"]

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
2026-08-10 17:48:38,929 INFO     29 [qwen-vl-text] coord API raw response (len=1482):
```json
[
	{"text": "影像学检查报告单", "bbox": [365, 72, 599, 95]},
	{"text": "扫码看电子胶片", "bbox": [711, 84, 817, 96]},
	{"text": "姓", "bbox": [97, 117, 116, 129]},
	{"text": "性别：男", "bbox": [281, 117, 358, 129]},
	{"text": "年龄：70岁", "bbox": [469, 117, 565, 129]},
	{"text": "影像", "bbox": [649, 117, 682, 129]},
	{"text": "科", "bbox": [97, 136, 132, 148]},
	{"text": "住院", "bbox": [649, 139, 683, 151]},
	{"text": "检查日期：2020-12-22", "bbox": [97, 162, 261, 172]},
	{"text": "报告日期：2020-12-23", "bbox": [281, 162, 445, 172]},
	{"text": "报告时间：14:22:52", "bbox": [469, 162, 614, 172]},
	{"text": "登记号", "bbox": [649, 160, 699, 172]},
	{"text": "40", "bbox": [761, 160, 800, 172]},
	{"text": "检查名称：颅脑MR平扫成像+DWI成像", "bbox": [97, 202, 440, 217]},
	{"text": "检查方法：AXI:FSE T1WI, T2WI, FLAIR, DWI", "bbox": [97, 236, 473, 250]},
	{"text": "SAG:FSE T1WI", "bbox": [211, 253, 328, 266]},
	{"text": "图像所见：双侧额顶叶白质可见散在斑点状等T1稍长T2信号影，FLAIR为高信号，", "bbox": [97, 290, 811, 305]},
	{"text": "DWI为等信号。脑室系统略扩大，脑沟、脑池明显加深，中线结构居中。", "bbox": [211, 314, 813, 329]},
	{"text": "印象：1. 血管性脱髓鞘（Fazekas 1级），请结合临床复查", "bbox": [97, 563, 666, 579]},
	{"text": "2. 老年性脑改变", "bbox": [208, 587, 362, 602]},
	{"text": "报告", "bbox": [193, 847, 242, 861]},
	{"text": "审核医师：", "bbox": [535, 847, 609, 861]},
	{"text": "该报告反映受检者当时情况，仅供临床医师参考。", "bbox": [97, 870, 413, 881]},
	{"text": "流水号", "bbox": [97, 891, 141, 902]},
	{"text": "CS 扫描全能王", "bbox": [862, 958, 977, 973]},
	{"text": "3亿人都在用的扫描App", "bbox": [862, 978, 977, 986]}
]
```
2026-08-10 17:48:38,930 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=8.1s
2026-08-10 17:48:38,930 INFO     29 [qwen-vl-text] coord item[0]: text=影像学检查报告单, bbox=[365, 72, 599, 95]
2026-08-10 17:48:38,930 INFO     29 [qwen-vl-text] coord item[1]: text=扫码看电子胶片, bbox=[711, 84, 817, 96]
2026-08-10 17:48:38,930 INFO     29 [qwen-vl-text] coord item[2]: text=姓, bbox=[97, 117, 116, 129]
2026-08-10 17:48:38,930 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[281, 117, 358, 129]
2026-08-10 17:48:38,930 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：70岁, bbox=[469, 117, 565, 129]
2026-08-10 17:48:38,930 INFO     29 [qwen-vl-text] coord item[5]: text=影像, bbox=[649, 117, 682, 129]
2026-08-10 17:48:38,930 INFO     29 [qwen-vl-text] coord item[6]: text=科, bbox=[97, 136, 132, 148]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[7]: text=住院, bbox=[649, 139, 683, 151]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[8]: text=检查日期：2020-12-22, bbox=[97, 162, 261, 172]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[9]: text=报告日期：2020-12-23, bbox=[281, 162, 445, 172]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[10]: text=报告时间：14:22:52, bbox=[469, 162, 614, 172]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[11]: text=登记号, bbox=[649, 160, 699, 172]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[12]: text=40, bbox=[761, 160, 800, 172]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[13]: text=检查名称：颅脑MR平扫成像+DWI成像, bbox=[97, 202, 440, 217]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[14]: text=检查方法：AXI:FSE T1WI, T2WI, FLAIR, DWI, bbox=[97, 236, 473, 250]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[15]: text=SAG:FSE T1WI, bbox=[211, 253, 328, 266]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[16]: text=图像所见：双侧额顶叶白质可见散在斑点状等T1稍长T2信号影，FLAIR为高信号，, bbox=[97, 290, 811, 305]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[17]: text=DWI为等信号。脑室系统略扩大，脑沟、脑池明显加深，中线结构居中。, bbox=[211, 314, 813, 329]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[18]: text=印象：1. 血管性脱髓鞘（Fazekas 1级），请结合临床复查, bbox=[97, 563, 666, 579]
2026-08-10 17:48:38,931 INFO     29 [qwen-vl-text] coord item[19]: text=2. 老年性脑改变, bbox=[208, 587, 362, 602]
2026-08-10 17:48:38,932 INFO     29 [qwen-vl-text] coord item[20]: text=报告, bbox=[193, 847, 242, 861]
2026-08-10 17:48:38,932 INFO     29 [qwen-vl-text] coord item[21]: text=审核医师：, bbox=[535, 847, 609, 861]
2026-08-10 17:48:38,932 INFO     29 [qwen-vl-text] coord item[22]: text=该报告反映受检者当时情况，仅供临床医师参考。, bbox=[97, 870, 413, 881]
2026-08-10 17:48:38,932 INFO     29 [qwen-vl-text] coord item[23]: text=流水号, bbox=[97, 891, 141, 902]
2026-08-10 17:48:38,932 INFO     29 [qwen-vl-text] coord item[24]: text=CS 扫描全能王, bbox=[862, 958, 977, 973]
2026-08-10 17:48:38,932 INFO     29 [qwen-vl-text] coord item[25]: text=3亿人都在用的扫描App, bbox=[862, 978, 977, 986]
2026-08-10 17:48:38,932 INFO     29 [qwen-vl-text] page=18 — 25/25 coords, api_time=8.1s
2026-08-10 17:48:38,933 INFO     29 [qwen-vl-text] new_positions (25):
[[18, 217.17499999999998, 356.405, 60.623999999999995, 79.99], [18, 423.04499999999996, 486.11499999999995, 70.728, 80.832], [18, 57.714999999999996, 69.02, 98.514, 108.618], [18, 167.195, 213.01, 98.514, 108.618], [18, 279.055, 336.175, 98.514, 108.618], [18, 386.155, 405.78999999999996, 98.514, 108.618], [18, 57.714999999999996, 78.53999999999999, 114.512, 124.616], [18, 386.155, 406.385, 117.038, 127.142], [18, 57.714999999999996, 155.295, 136.404, 144.82399999999998], [18, 167.195, 264.775, 136.404, 144.82399999999998], [18, 279.055, 365.33, 136.404, 144.82399999999998], [18, 386.155, 415.905, 134.72, 144.82399999999998], [18, 452.79499999999996, 476.0, 134.72, 144.82399999999998], [18, 57.714999999999996, 261.8, 170.084, 182.714], [18, 57.714999999999996, 281.435, 198.712, 210.5], [18, 125.54499999999999, 195.16, 213.02599999999998, 223.97199999999998], [18, 57.714999999999996, 482.54499999999996, 244.17999999999998, 256.81], [18, 125.54499999999999, 483.73499999999996, 264.388, 277.018], [18, 57.714999999999996, 396.27, 474.046, 487.518], [18, 123.75999999999999, 215.39, 494.25399999999996, 506.88399999999996], [18, 114.835, 143.98999999999998, 713.174, 724.962], [18, 318.325, 362.35499999999996, 713.174, 724.962], [18, 57.714999999999996, 245.73499999999999, 732.54, 741.802], [18, 57.714999999999996, 83.895, 750.222, 759.4839999999999], [18, 512.89, 581.3149999999999, 806.636, 819.266]]
2026-08-10 17:48:38,933 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=10.6s
2026-08-10 17:48:38,933 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:48:38,944 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:48:38,945 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:48:38,945 INFO     29 [qwen-vl-text] positions(14): [[19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:48:38,945 INFO     29 [qwen-vl-text] page grouping: [19], lines per page: [14]
2026-08-10 17:48:39,109 INFO     29 [qwen-vl-text] page=19, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 17:48:39,110 INFO     29 [qwen-vl-text] LLM extraction start, text_len=280
2026-08-10 17:48:39,110 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:39,110 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3933, \"bbox_end\": 3946, \"encounter_dates\": [\"2026-01-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "超声检查报告单\n患者\n性别：男\n年龄：75岁\n检查所见：\n甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。\n甲状旁腺区未见明显异常回声。\n左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门\n髓结构不清，CDFI：内见条状血流信号。\n右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。\n超声提示：左侧颈部淋巴结肿大，考虑“Ⅱ”性可能\n报告日期：2026-01-27 08:26:34 记录\n师\n注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。",
    "role": "user"
  }
]
2026-08-10 17:48:39,112 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T17:48:39.111+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 82, "failed": 0, "current": {"cc093d2e94e111f1bd9827cf206dfa2d": {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 17:48:41,701 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:41,702 INFO     29 [qwen-vl-text] LLM output (len=488):
{
  "exam_date": "2026-01-27",
  "report_date": "2026-01-27",
  "exam_name": "超声检查",
  "exam_category": "imaging",
  "body_part": "甲状腺、颈部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。\n甲状旁腺区未见明显异常回声。\n左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门髓结构不清，CDFI：内见条状血流信号。\n右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。",
  "conclusion": "左侧颈部淋巴结肿大，考虑“Ⅱ”性可能",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:48:41,706 INFO     29 [qwen-vl-text] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1415428, prompt_len=935
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["超声检查报告单", "患者", "性别：男", "年龄：75岁", "检查所见：", "甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。", "甲状旁腺区未见明显异常回声。", "左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门", "髓结构不清，CDFI：内见条状血流信号。", "右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。", "超声提示：左侧颈部淋巴结肿大，考虑“Ⅱ”性可能", "报告日期：2026-01-27 08:26:34 记录", "师", "注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。"]

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
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord API raw response (len=892):
[
	{"text": "超声检查报告单", "bbox": [325, 84, 656, 108]},
	{"text": "患者", "bbox": [74, 122, 130, 138]},
	{"text": "性别：男", "bbox": [428, 150, 522, 167]},
	{"text": "年龄：75岁", "bbox": [658, 150, 772, 167]},
	{"text": "检查所见：", "bbox": [74, 457, 166, 473]},
	{"text": "甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。", "bbox": [116, 478, 908, 495]},
	{"text": "甲状旁腺区未见明显异常回声。", "bbox": [116, 522, 398, 538]},
	{"text": "左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门", "bbox": [116, 544, 898, 561]},
	{"text": "髓结构不清，CDFI：内见条状血流信号。", "bbox": [74, 566, 440, 582]},
	{"text": "右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。", "bbox": [114, 588, 668, 605]},
	{"text": "超声提示：左侧颈部淋巴结肿大，考虑“Ⅱ”性可能", "bbox": [74, 758, 535, 775]},
	{"text": "报告日期：2026-01-27 08:26:34 记录", "bbox": [74, 789, 410, 805]},
	{"text": "师", "bbox": [586, 789, 620, 805]},
	{"text": "注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。", "bbox": [74, 830, 797, 847]}
]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=7.6s
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[0]: text=超声检查报告单, bbox=[325, 84, 656, 108]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[1]: text=患者, bbox=[74, 122, 130, 138]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[428, 150, 522, 167]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：75岁, bbox=[658, 150, 772, 167]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[4]: text=检查所见：, bbox=[74, 457, 166, 473]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[5]: text=甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。, bbox=[116, 478, 908, 495]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[6]: text=甲状旁腺区未见明显异常回声。, bbox=[116, 522, 398, 538]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[7]: text=左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门, bbox=[116, 544, 898, 561]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[8]: text=髓结构不清，CDFI：内见条状血流信号。, bbox=[74, 566, 440, 582]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[9]: text=右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。, bbox=[114, 588, 668, 605]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[10]: text=超声提示：左侧颈部淋巴结肿大，考虑“Ⅱ”性可能, bbox=[74, 758, 535, 775]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[11]: text=报告日期：2026-01-27 08:26:34 记录, bbox=[74, 789, 410, 805]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[12]: text=师, bbox=[586, 789, 620, 805]
2026-08-10 17:48:49,352 INFO     29 [qwen-vl-text] coord item[13]: text=注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。, bbox=[74, 830, 797, 847]
2026-08-10 17:48:49,353 INFO     29 [qwen-vl-text] page=19 — 14/14 coords, api_time=7.6s
2026-08-10 17:48:49,353 INFO     29 [qwen-vl-text] new_positions (14):
[[19, 193.375, 390.32, 70.728, 90.93599999999999], [19, 44.03, 77.35, 102.72399999999999, 116.196], [19, 254.66, 310.59, 126.3, 140.614], [19, 391.51, 459.34, 126.3, 140.614], [19, 44.03, 98.77, 384.794, 398.26599999999996], [19, 69.02, 540.26, 402.476, 416.78999999999996], [19, 69.02, 236.81, 439.524, 452.996], [19, 69.02, 534.31, 458.048, 472.36199999999997], [19, 44.03, 261.8, 476.572, 490.044], [19, 67.83, 397.46, 495.096, 509.40999999999997], [19, 44.03, 318.325, 638.236, 652.55], [19, 44.03, 243.95, 664.338, 677.81], [19, 348.66999999999996, 368.9, 664.338, 677.81], [19, 44.03, 474.215, 698.86, 713.174]]
2026-08-10 17:48:49,353 INFO     29 [qwen-vl-text] ═══ DONE ═══ 14 positions, pages=1, time=10.4s
2026-08-10 17:48:49,353 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 17:48:49,354 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 17:48:49,354 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 17:48:49,354 INFO     29 [qwen-vl-text] positions(31): [[20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 17:48:49,354 INFO     29 [qwen-vl-text] page grouping: [20], lines per page: [31]
2026-08-10 17:48:49,625 INFO     29 [qwen-vl-text] page=20, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 17:48:49,626 INFO     29 [qwen-vl-text] LLM extraction start, text_len=281
2026-08-10 17:48:49,626 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:49,626 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3947, \"bbox_end\": 3977, \"encounter_dates\": [\"2026-01-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "心电图报告单\n性别：男\n年龄：75岁\n危重症医学科率：69 bpm\nP-R间期：139 ms\nQRS时间：90 ms\nQT/QTc : 414/445 ms\nP-R-T : 63/22/25 度\nSV1/RV5:0.49/1.35 mV\nRV5+SV1:1.84mV\n诊断：大致正常心电图\n检查时间：2026-01-26 10:31:55\n检查医生：\nI\nII\nIII\nAVR\nAVL\nAVF\nV1\nV2\nV3\nV4\nV5\nV6\n检查者：\n25 mm/s 10 mm/mv\n报告审核\n时间：2026-01-26 10:35:22\n以上结果请结合临床及前图\n1/1",
    "role": "user"
  }
]
2026-08-10 17:48:52,009 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:48:52,009 INFO     29 [qwen-vl-text] LLM output (len=434):
{
  "exam_date": "2026-01-26",
  "report_date": "2026-01-26",
  "exam_name": "心电图",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "男",
  "department": "危重症医学科",
  "bed_number": null,
  "findings": "心率：69 bpm\nP-R间期：139 ms\nQRS时间：90 ms\nQT/QTc : 414/445 ms\nP-R-T : 63/22/25 度\nSV1/RV5:0.49/1.35 mV\nRV5+SV1:1.84mV",
  "conclusion": "诊断：大致正常心电图",
  "physician": null,
  "reviewer": null
}
2026-08-10 17:48:52,015 INFO     29 [qwen-vl-text] coord API call start, page=20, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3650623, prompt_len=987
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["心电图报告单", "性别：男", "年龄：75岁", "危重症医学科率：69 bpm", "P-R间期：139 ms", "QRS时间：90 ms", "QT/QTc : 414/445 ms", "P-R-T : 63/22/25 度", "SV1/RV5:0.49/1.35 mV", "RV5+SV1:1.84mV", "诊断：大致正常心电图", "检查时间：2026-01-26 10:31:55", "检查医生：", "I", "II", "III", "AVR", "AVL", "AVF", "V1", "V2", "V3", "V4", "V5", "V6", "检查者：", "25 mm/s 10 mm/mv", "报告审核", "时间：2026-01-26 10:35:22", "以上结果请结合临床及前图", "1/1"]

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
2026-08-10 17:49:00,876 INFO     29 [qwen-vl-text] coord API raw response (len=1644):
[
	{"text": "心电图报告单", "bbox": [532, 64, 664, 94]},
	{"text": "性别：男", "bbox": [282, 154, 320, 169]},
	{"text": "年龄：75岁", "bbox": [282, 174, 330, 189]},
	{"text": "危重症医学科率：69 bpm", "bbox": [232, 195, 344, 209]},
	{"text": "P-R间期：139 ms", "bbox": [429, 134, 509, 148]},
	{"text": "QRS时间：90 ms", "bbox": [429, 154, 504, 169]},
	{"text": "QT/QTc : 414/445 ms", "bbox": [429, 175, 533, 189]},
	{"text": "P-R-T : 63/22/25 度", "bbox": [429, 195, 538, 209]},
	{"text": "SV1/RV5:0.49/1.35 mV", "bbox": [281, 217, 397, 230]},
	{"text": "RV5+SV1:1.84mV", "bbox": [429, 217, 511, 230]},
	{"text": "诊断：大致正常心电图", "bbox": [579, 132, 699, 149]},
	{"text": "检查时间：2026-01-26 10:31:55", "bbox": [133, 241, 296, 255]},
	{"text": "检查医生：", "bbox": [717, 241, 765, 255]},
	{"text": "I", "bbox": [139, 309, 146, 322]},
	{"text": "II", "bbox": [139, 391, 152, 404]},
	{"text": "III", "bbox": [139, 471, 157, 484]},
	{"text": "AVR", "bbox": [139, 552, 158, 565]},
	{"text": "AVL", "bbox": [139, 635, 158, 648]},
	{"text": "AVF", "bbox": [139, 717, 158, 730]},
	{"text": "V1", "bbox": [504, 309, 515, 322]},
	{"text": "V2", "bbox": [504, 391, 515, 404]},
	{"text": "V3", "bbox": [504, 471, 515, 484]},
	{"text": "V4", "bbox": [504, 552, 515, 565]},
	{"text": "V5", "bbox": [504, 635, 515, 648]},
	{"text": "V6", "bbox": [504, 717, 515, 730]},
	{"text": "检查者：", "bbox": [189, 838, 223, 853]},
	{"text": "25 mm/s 10 mm/mv", "bbox": [403, 841, 495, 854]},
	{"text": "报告审核", "bbox": [517, 838, 556, 853]},
	{"text": "时间：2026-01-26 10:35:22", "bbox": [700, 838, 844, 853]},
	{"text": "以上结果请结合临床及前图", "bbox": [722, 848, 927, 871]},
	{"text": "1/1", "bbox": [870, 21, 895, 42]}
]
2026-08-10 17:49:00,877 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=8.9s
2026-08-10 17:49:00,877 INFO     29 [qwen-vl-text] coord item[0]: text=心电图报告单, bbox=[532, 64, 664, 94]
2026-08-10 17:49:00,877 INFO     29 [qwen-vl-text] coord item[1]: text=性别：男, bbox=[282, 154, 320, 169]
2026-08-10 17:49:00,877 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：75岁, bbox=[282, 174, 330, 189]
2026-08-10 17:49:00,877 INFO     29 [qwen-vl-text] coord item[3]: text=危重症医学科率：69 bpm, bbox=[232, 195, 344, 209]
2026-08-10 17:49:00,877 INFO     29 [qwen-vl-text] coord item[4]: text=P-R间期：139 ms, bbox=[429, 134, 509, 148]
2026-08-10 17:49:00,877 INFO     29 [qwen-vl-text] coord item[5]: text=QRS时间：90 ms, bbox=[429, 154, 504, 169]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[6]: text=QT/QTc : 414/445 ms, bbox=[429, 175, 533, 189]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[7]: text=P-R-T : 63/22/25 度, bbox=[429, 195, 538, 209]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[8]: text=SV1/RV5:0.49/1.35 mV, bbox=[281, 217, 397, 230]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[9]: text=RV5+SV1:1.84mV, bbox=[429, 217, 511, 230]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[10]: text=诊断：大致正常心电图, bbox=[579, 132, 699, 149]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[11]: text=检查时间：2026-01-26 10:31:55, bbox=[133, 241, 296, 255]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[12]: text=检查医生：, bbox=[717, 241, 765, 255]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[13]: text=I, bbox=[139, 309, 146, 322]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[14]: text=II, bbox=[139, 391, 152, 404]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[15]: text=III, bbox=[139, 471, 157, 484]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[16]: text=AVR, bbox=[139, 552, 158, 565]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[17]: text=AVL, bbox=[139, 635, 158, 648]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[18]: text=AVF, bbox=[139, 717, 158, 730]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[19]: text=V1, bbox=[504, 309, 515, 322]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[20]: text=V2, bbox=[504, 391, 515, 404]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[21]: text=V3, bbox=[504, 471, 515, 484]
2026-08-10 17:49:00,878 INFO     29 [qwen-vl-text] coord item[22]: text=V4, bbox=[504, 552, 515, 565]
2026-08-10 17:49:00,879 INFO     29 [qwen-vl-text] coord item[23]: text=V5, bbox=[504, 635, 515, 648]
2026-08-10 17:49:00,879 INFO     29 [qwen-vl-text] coord item[24]: text=V6, bbox=[504, 717, 515, 730]
2026-08-10 17:49:00,879 INFO     29 [qwen-vl-text] coord item[25]: text=检查者：, bbox=[189, 838, 223, 853]
2026-08-10 17:49:00,879 INFO     29 [qwen-vl-text] coord item[26]: text=25 mm/s 10 mm/mv, bbox=[403, 841, 495, 854]
2026-08-10 17:49:00,879 INFO     29 [qwen-vl-text] coord item[27]: text=报告审核, bbox=[517, 838, 556, 853]
2026-08-10 17:49:00,879 INFO     29 [qwen-vl-text] coord item[28]: text=时间：2026-01-26 10:35:22, bbox=[700, 838, 844, 853]
2026-08-10 17:49:00,879 INFO     29 [qwen-vl-text] coord item[29]: text=以上结果请结合临床及前图, bbox=[722, 848, 927, 871]
2026-08-10 17:49:00,879 INFO     29 [qwen-vl-text] coord item[30]: text=1/1, bbox=[870, 21, 895, 42]
2026-08-10 17:49:00,880 INFO     29 [qwen-vl-text] page=20 — 31/31 coords, api_time=8.9s
2026-08-10 17:49:00,880 INFO     29 [qwen-vl-text] new_positions (31):
[[20, 447.94399999999996, 559.088, 38.08, 55.93], [20, 237.444, 269.44, 91.63, 100.55499999999999], [20, 237.444, 277.86, 103.53, 112.455], [20, 195.344, 289.64799999999997, 116.02499999999999, 124.35499999999999], [20, 361.21799999999996, 428.578, 79.72999999999999, 88.06], [20, 361.21799999999996, 424.368, 91.63, 100.55499999999999], [20, 361.21799999999996, 448.786, 104.125, 112.455], [20, 361.21799999999996, 452.996, 116.02499999999999, 124.35499999999999], [20, 236.602, 334.274, 129.11499999999998, 136.85], [20, 361.21799999999996, 430.262, 129.11499999999998, 136.85], [20, 487.518, 588.558, 78.53999999999999, 88.655], [20, 111.98599999999999, 249.232, 143.39499999999998, 151.725], [20, 603.7139999999999, 644.13, 143.39499999999998, 151.725], [20, 117.038, 122.932, 183.855, 191.59], [20, 117.038, 127.984, 232.64499999999998, 240.38], [20, 117.038, 132.194, 280.245, 287.97999999999996], [20, 117.038, 133.036, 328.44, 336.175], [20, 117.038, 133.036, 377.825, 385.56], [20, 117.038, 133.036, 426.615, 434.34999999999997], [20, 424.368, 433.63, 183.855, 191.59], [20, 424.368, 433.63, 232.64499999999998, 240.38], [20, 424.368, 433.63, 280.245, 287.97999999999996], [20, 424.368, 433.63, 328.44, 336.175], [20, 424.368, 433.63, 377.825, 385.56], [20, 424.368, 433.63, 426.615, 434.34999999999997], [20, 159.138, 187.766, 498.60999999999996, 507.53499999999997], [20, 339.32599999999996, 416.78999999999996, 500.395, 508.13], [20, 435.31399999999996, 468.152, 498.60999999999996, 507.53499999999997], [20, 589.4, 710.648, 498.60999999999996, 507.53499999999997], [20, 607.924, 780.534, 504.56, 518.245], [20, 732.54, 753.5899999999999, 12.495, 24.99]]
2026-08-10 17:49:00,880 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=11.5s
2026-08-10 17:49:00,898 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 17:49:00,900 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:ExaminationReport | outputs={"chunks": "12 items, types={'ExaminationReport': 12}", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:49:00,900 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 17:49:00,911 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:49:00,912 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 17:49:01,717 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 17:49:01,724 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 17:49:01,724 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "4233 items", "markdown": "", "text": "", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 1, \"chunks_Examination\": 12, \"chunks_LabExam\": 5}"}
2026-08-10 17:49:01,724 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 17:49:01,726 INFO     29 [ChunkMerger] Merged 20 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 12, 'Extractor:Progress': 1} (filtered 4 noise chunks)
2026-08-10 17:49:01,741 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 17:49:01,742 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "20 items, types={'LabReport': 5, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 12}", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf"}
2026-08-10 17:49:01,742 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 17:49:02,048 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786383295678, 'update_date': datetime.datetime(2026, 8, 10, 17, 34, 55), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1299137, 'status': '1'}
2026-08-10 17:49:02,283 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=\begin{tabular}{cccccccccc}
报告时间: 2020-01-07
\hline
\multicolumn{10}{c}{\textbf{检验报告单 (血型尿常规)}} \\
\hline
\multicolumn{2}{c}{姓名} & \multicolumn{2}{c}{四四库呼呼与抗重球球学目} & \multicolumn{2}{c}{床 号:} & \multicolumn{2}{c}{号:} & \multicolumn{2}{c}{号:} \\
\multicolumn{2}{c}{性别} & \multicolumn{2}{c}{10001100101} & \multicolumn{2}{c}{标本种类:} & \multicolumn{2}{c}{李曲} & \multicolumn{2}{c}{标本状态:} \\
\multicolumn{2}{c}{年龄} & \multicolumn{2}{c}{1001000} & \multicolumn{2}{c}{临床诊断:} & \multicolumn{2}{c}{脑垂体肿瘤} & \multicolumn{2}{c}{} \\
\hline
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{生物参考区间} & \multicolumn{2}{c}{单位} & \multicolumn{2}{c}{日} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{生物参考区间} & \multicolumn{2}{c}{单位} \\
\hline
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{35} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} & \multicolumn{2}{c}{10 0/1} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} & \multicolumn{2}{c}{10 0 10 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} & \multicolumn{2}{c}{00 0 00 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} & \multicolumn{2}{c}{0 0 10 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} & \multicolumn{2}{c}{0 0 0 0} \\
\multicolumn{2}{c}{日} & \multicolumn{2}{c}{00} & \mult
\begin{tabular}{llllllllll}
---
   白细胞  None  阴性  None  None  False    隐血  None  阴性  None  None  False    蛋白  None  阴性  None  None  False    葡萄糖  None  阴性  None  None  False    PH  None  6.5  None  4.5-8.0  False    比重  None  1.016  None  1.003-1.030  False    酮体  None  阴性  None  None  False    胆红素  None  阴性  None  None  False    尿胆原  None  正常  None  阴性-弱阳性  False    亚硝酸盐  None  阴性  None  None  False    浊度  None  清亮  None  None  False    白细胞计数  None  2.4  /uL  0.0-25.0  False    红细胞计数  None  3.2  /uL  0.0-23.0  False    上皮细胞计数  None  0.4  /uL  0.0-31.0  False    管型计数  None  0.0  /uL  0.0-2.0  False    小圆上皮细胞  None  0.4  /uL  0.0-3.0  False    类酵母细胞  None  --  None  0.0-0.0  False    结晶检查  None  0.0  /uL  0.0-10.0  False    细菌计数  None  8.5  /uL  0.0-1200.0  False    电导率  None  16.3  mS/cm  3.0-39.0  False    红细胞信息  None  阴性  None  None  False   
---
   凝血酶原时间  None  13.2  sec  10.0-14.0  False    PT-国际标准化比值  None  1.13  INR  0.80-1.20  False    PT百分活度  None  84  %  80-200  False    活化部分凝血活酶时间  None  31.8  sec  22.0-38.0  False    APTT比值  None  1.12  R  0.73-1.27  False    凝血酶时间  None  18.1  sec  14.0-21.0  False    TT比值  None  1.06  R  0.82-1.23  False    纤维蛋白原  None  5.80  g/L  2.0-4.0  True    抗凝血酶III  None  96  %  82-121  False    D-二聚体测定  None  550  ng/ml  0-500  True   
---
   乙型肝炎表面抗原(化学发光法)  None  0.00  IU/ml  <0.05  False    丙型肝炎抗体  None  0.07  S/CO  <1  False    HIV抗体/p24抗原  None  0.13  S/CO  <1.00  False    梅毒螺旋体抗体  None  0.08  S/CO  <1.00  False   
---
   癌胚抗原  None  9.21  ng/ml  0-5.0  True    甲胎蛋白  None  1.64  ng/ml  0-7.00  False    糖类抗原72-4  None  2.08  U/ml  0-6.9  False    神经元特异性烯醇化酶  None  22.47  ng/ml  0-17  True    细胞角蛋白19片段  None  5.70  ng/ml  0-3.3  True    鳞状细胞癌相关抗原  None  2.97  ng/ml  0-2.5  True    胃泌素释放肽前体  None  37.68  pg/mL  0-68.3  False    总前列腺特异性抗原  None  4.820  ng/ml  0-4  True    游离前列腺特异性抗原  None  0.767  ng/ml  0-0.93  False    FPSA/TPSA  None  0.159  None  >0.15  False    特异β人绒毛膜促性腺激素  None  5.86  mIU/ml  0-2.6  True    糖类抗原19-9  None  27.60  U/ml  0-30  False   
---
门（急）诊病历
初诊
科室
日期:2026-02-02 09:07
医学
性别:男
年龄:75岁
出生日期:1950-09-13
主诉:肺癌靶向治疗5年复查。
现病史:肺癌吉非替尼治疗3个月,因肝功异常更换泰瑞沙靶向治疗至今5年,外院肺CT提示病灶增大
既往史:无肺结核病史。
个人史:无不良嗜好。
家族史:无遗传病史。
体 检:双肺呼吸音清,未闻及干湿性啰音。
辅助检查:2026-01-30 组织病理学检查与诊断[免费用](左肺组织穿刺活检)非小细胞肺癌伴大片坏死,
结合形态学及免疫组化,符合腺癌。免疫组化示肿瘤细胞:CKpan(+),CK7(+),TTF-
1(+),p40(-),CK5/6(-);特殊染色:D-PAS(-)。
初步诊断:肺恶性肿瘤
诊疗计划:分子病理检测
甲磺酸奥希替尼片(泰瑞沙2)(80mg*30),剂量:80MG,用法:口服,频率:每日1次,疗程:1天,
温馨提示:此病历只打印一次,请妥善保管!
第1页 共2页
打印时间:2026-03-02 12:50:46
门（急）诊病历
初诊
科
日期:2026-02-02 09:07
姓名
性别:男
年龄:75岁
出生日期:1950-09-13
医师签名：
---
出院记录
登记号:
住院号:
姓名
姓名：
性别：男
年龄：75岁
科室·
入院日期：2026-01-26
出院日期：2026-01-31
住院天数：5天
入院情况：
，男，75岁，因“确诊肺癌5年，病情进展1月余”于2026-01-
26入院。患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切
接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术
史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。体检：T:
36.3℃ P:69次/分 R:17次/分 BP:120/66mmHg。神志清，精神可，双肺呼吸音清，未
闻及干湿性啰音。心脏各瓣膜听诊区未闻及异常杂音。腹软，无压痛，Murphy征阴
性。双下肢无水肿。病理征阴性。辅助检查：2020-12-21行支气管镜检查，组织病理
学示：(左侧隆突粘膜)非小细胞肺癌，免疫组化：CK7(+)，TTF-1(+)，
NapsinA(+)，p40(部分+)，p63(部分+)，CK5/6(+)，ALK-D5F3(-)，ALK-
D5F3-N(-)，S100(-)，Calponin(-)。结合免疫组化结果，符合腺癌；(左肺
BALF)细胞蜡块内发现少量恶性肿瘤细胞。
入院诊断：肺部恶性肿瘤纵隔淋巴结继发恶性肿瘤肺门淋巴结继发恶性肿瘤
诊疗经过：入院后完善相关检验检查，【检验】血常规(无网红)+CRP：白细胞计数7.
49×10⁹/L，中性粒细胞计数3.75×10⁹/L，红细胞计数3.67×10¹²/L，血红蛋白102g/L，血
小板计数488×10⁹/L，C反应蛋白38.40mg/l；血凝四项：纤维蛋白原5.80g/L；癌胚抗原
测定：9.21ng/ml；鳞状细胞癌相关抗原测定：2.97ng/ml；神经元特异性烯醇化酶测定：
22.47ng/ml；细胞角蛋白19片段测定：5.70ng/ml；总前列腺特异性抗原(TPSA)测定：4.
820ng/ml；β人绒毛膜促性腺激素测定：5.86mIU/ml；D-二聚体测定：550ng/ml；血浆
抗凝血酶活性(ATIII)测定、尿常规化学分析、尿有形成分分析、粪便常规分析+隐血
试验、传染性标志物4项检测未见异常。【检查】十二通道常规心电图检查：大致正常
心电图。甲状腺及体表肿物彩色多普勒超声检查：左侧颈部淋巴结肿大，考虑“M”性
可能。消化系统超声：脾切除术后，空腹胆囊充盈差、腔内透声差，慢性胆囊炎?肝
囊肿，右肾略高回声结节，考虑良性(结合病史考虑复杂囊肿可能)。泌尿系统超
声：前列腺增生并钙化。胸部CT增强成像：左肺癌并纵隔、左肺门肿大淋巴结转移复
查所见，较前进展，请结合临床，双肺多发结节，较前增多、增大，请结合临床随
访，双肺慢性炎症或纤维灶可能性大，请结合临床，左侧部分肋骨局部形态不规
整，请结合临床；【诊疗】入院后给予完善相关检查，排除禁忌后于2026-01-28行CT
引导下经皮穿刺肺活检术，2026-01-30左肺组织穿刺活检示非小细胞肺癌伴大片坏
死，结合形态学及免疫组化，符合腺癌。免疫组化示肿瘤细胞：CKpan(+)，
CK7(+)，TTF-1(+)，p40(-)，CK5/6(-)；特殊染色：D-PAS(-)。现患者诊
第1页
CS 扫描全能王
3亿人都在用的扫描App
出院记录
登记号
住院号
姓名：
断明确，拟出院后行基因检测治疗，准予办理出院。
出院诊断：肺部恶性肿瘤（腺癌 rT4N3MO IVA期）
纵隔淋巴结继发恶性肿瘤
肺门淋巴结继发恶性肿瘤
颈部淋巴结肿大
脾术后
慢性胆囊炎
肝囊肿
肾结节
出院情况：患者一般情况可，查体：神志清，双肺呼吸音清，心律齐，腹软，无压痛
及反跳痛，双下肢无水肿。
出院医嘱：
1.注意休息，避免感染、劳累；
2.出院后分子病理科行基因检测，出院2周待结果回报后于呼吸与危重症医学科门诊就
诊就诊制定进一步治疗方案；
3.如有不适或复查指标异常，门急诊及时就诊。
出院目的地：居家
患者照护需求：注意休息，避免感染、劳累
医师签名：
---
第2次住院
入院记录
姓名：
姓名：
出生地：
性别：男
职业：其他
年龄：75岁
入院时间：2026-01-26 10:12
民族：汉族
记录时间：2026-01-26 13:59
婚姻：已婚
病史陈述者：患者本人
主诉：确诊肺癌5年，病情进展1月余
现病史：患者因“胸闷2月，干咳1周”于2020年12月17日第一次入住我科，于2020-
12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组化：
CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），
CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合
免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞；（痰）
涂片内发现少量可疑恶性肿瘤细胞，于2020-12-27给予培美曲塞800mgd1+卡铂
400mgd2，并辅以止吐、保胃等治疗，化疗过程顺利，准予出院。出院诊断：左肺上叶恶
性肿瘤（腺癌 T4N3M1 IV期）、为肿瘤化学治疗疗程、纵隔淋巴结继发恶性肿瘤、肺
门淋巴结继发恶性肿瘤、阻塞性肺炎、肝囊肿、单纯性肾囊肿。出院后先后服用吉非
替尼、泰瑞沙靶向治疗至今。
1月余前患者就诊于外院，复查肺CT提示病灶增大，具体不详，无发热乏力，无咳
嗽咳痰，无胸闷憋气等不适，为求进一步诊治就诊于我院门诊，为行二次活检收入我
科，患者自发病以来，神志清，精神可，饮食睡眠可，大小便正常，体重近期未见明
显变化。
既往史：患者平素身体一般，否认肝炎病史，无结核病史，否认疟疾病史，否认密切
接触史，否认高血压、心脏病史，否认糖尿病、脑血管疾病、精神疾病史，否认手术
史，无外伤史，无输血史，无药物、食物过敏史，其他预防接种史不详。
个人史：生于山东省胶州市，久居本地，无疫区、疫情、疫水接触史，无牧区、矿
山、高氟区、低碘区居住史，无化学性物质、无放射性物质、无有毒物质接触史，无
吸毒史，无吸烟史，无饮酒史，无特殊药物服用史，无冶游史。
婚姻史：适龄结婚，配偶体健。
家族史：父母已故（具体不详），父有糖尿病病史，1弟因白血病去世，一妹去世，2
妹健在，否认家族中有遗传倾向性疾病及传染性疾病。
体格检查
T：36.3℃ P：69次/分 R：17次/分 BP：120/66mmHg H：160cm W：52kg BMI：20.
31kg/m²
一般情况：正常发育状态，营养良好，体型匀称型，自主体位，正常面容，神志清楚
，正常步态，语言清晰，查体合作。
第1页
另2次住院
入院记录
登记号:
姓名:
住院号
皮肤、粘膜：皮肤黏膜无黄染 无皮疹、皮下出血，无皮下结节、瘢痕，皮下无水肿，
毛发分布正常，无肝掌、蜘蛛痣。全身浅表淋巴结：全身浅表淋巴结无肿大。
头部及其器官：头颅无畸形，毛发分布正常。眉毛正常，睫毛正常，无眼睑水肿，
结膜无充血、苍白，眼球无震颤，巩膜无黄染，角膜正常，瞳孔等大等圆，对光调节
反射正常。外耳道无畸形，无异常分泌物，乳突无压痛，听力正常。外鼻无畸形，无
鼻翼扇动，无分泌物、出血、阻塞，鼻中隔基本居中，无穿孔，双侧鼻窦区无压痛。
口唇无发绀，口腔粘膜无溃疡。伸舌无偏斜、震颤，齿龈无肿胀、出血。咽部粘膜无
充血，扁桃体无肥大。喉咙发音清晰。
颈部：颈部对称，软，颈动脉搏动正常，颈静脉无怒张，气管居中，肝颈静脉回流征
阴性，甲状腺无肿大，无压痛，未扪及包块，未闻及血管杂音。
胸部：胸廓对称、无畸形，乳房发育正常，胸骨无压痛，呼吸17次/分。
肺部：呼吸运动正常，肋间隙无增宽、无变窄，呼吸规整，语颤无增强及减弱，无胸
膜摩擦感、无皮下捻发感。叩诊清音，双肺呼吸音清晰，未闻及干、湿性啰音，语音
传导正常，无胸膜摩擦音。
心脏：心前区无隆起，心尖搏动未见增强及弥散，无震颤及心包摩擦感，心浊音界无
扩大，心率69次/分，律齐，各瓣膜听诊区未闻及病理性杂音，无心包摩擦音。
血管：桡动脉：脉率69次/分，脉律规整。无毛细血管搏动征，无股动脉枪击音。
腹部：腹部平坦，对称，无腹壁静脉曲张，无胃肠型和蠕动波，腹部柔软，无压痛及
反跳痛，未触及异常包块。肝、脾肋下未触及、质软、无压痛，Murphy氏征阴性。腹
部叩诊：肝上界在右锁骨中线第五肋间，肝、肾区无叩击痛，无移动性浊音。肠鸣音
正常，4次/分。未听到血管杂音。
直肠肛门：肛门及直肠无异常。外生殖器无异常。
脊柱、四肢：脊柱正常生理弯曲，无畸形、压痛、叩击痛，活动度正常，四肢无畸
形，肌力、肌张力正常，关节活动度正常，双下肢无水肿，无静脉曲张。
神经系统：痛、温、触觉正常，肌肉无萎缩、无瘫痪，无共济失调。腹壁反射正常，
双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，双侧Babinski征阴性、
Gordon征阴性、Oppenheim征阴性、Hoffmann征阴性，脑膜刺激征阴性。
专科检查
辅助检查
2020-12-21行支气管镜检查，组织病理学示：（左侧隆突粘膜）非小细胞肺癌，免疫组
化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），
CK5/6（+）；ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。结合
免疫组化结果，符合腺癌；（左肺BALF）细胞蜡块内发现少量恶性肿瘤细胞。
第2页
第2次住院
入院记录
登记号:
姓名:
住院号
初步诊断
肺部恶性肿瘤
纵隔淋巴结继发恶性肿瘤
肺门淋巴结继发恶性肿瘤
医师签名
项目内容
患者（家属）签名
以上患者所述内容及提供资料属实
门诊病历已归还
---
门诊号：-
姓名
性别
男
年龄
70岁
病人编号
病区
病案号
门诊号
送检科室
送检单位
送检医生
标本名称
左侧隆突粘膜、左肺BALF等
临床诊断
肺部阴影
病理诊断
(左侧隆突粘膜)非小细胞肺癌，结合免疫组化结果，符合腺癌；
(左肺BALF)细胞蜡块内发现少量恶性肿瘤细胞；
(左肺BALF)涂片内未发现恶性肿瘤细胞；
(痰)涂片内发现少量可疑恶性肿瘤细胞。
免疫组化：CK7（+），TTF-1（+），NapsinA（+），p40（部分+），p63（部分+），CK5/6（+），ALK-D5F3（-），ALK-D5F3-N（-），S100（-），Calponin（-）。
报告医生
复诊医生
报告时间
2020-12-25
12:51
---
病理号
住院
门诊号
1-1]
姓名
70岁
病人编号
0007
病区
门诊号
送检科室
送检医生
标本名称
左侧隆突粘膜、左肺BALF等
临床诊断
肺部阴影
病理诊断
2020.12.20加做免疫结果：PD-L1-22C3（+，TPS约30%）
报告医生
报告时间
2020-12-29
12:51
2026-03-02
---
门楼号
姓名
病区
送检科室
标本名称
临床诊断
内眼所见
穿刺组织3条，合计长0.6cm。
病理诊断
(左肺组织穿刺活检）非小细胞肺癌伴大片坏死，待免疫组化。
报告医生
审核医生
报告时间
2026-01-28 14:53
点击要返回的Pah:QC流程
---
门诊号：
姓名
性别
75岁
病人编
病区
病区
病案号
门诊号
送检科室
送检单位
送检医生
丁晓倩
标本名称
左肺组织穿刺活检
临床诊断
1.肺恶性肿瘤2.肺恶性肿瘤
病理诊断
(左肺组织穿刺活检)肺小细胞肺癌伴大片坏死，结合形态学及免疫组化，符合肺癌。
免疫组化示肿瘤细胞：CKpan（+），CK7（+），TTF-1（+），p40（-），CK5/6（-）；
特殊染色：D-PAS（-）。
报告医生
医生
报告时间
2026-01-30 11:19
欢迎使用朗珈PathQC病理质控与资料管理系统！
12:51
2026-01-02
---
病历
姓名
病区
送检科室
标本名称
临床诊断
病理诊断
检查项目:肿瘤多基因检测(含MSI)
检查方法:高通量测序(NGS)
参考基因组:GRCh37/hg19
临床数据库:1000 Genomes、ExAC、gnomAD、ClinVar、BRCA Exchange InSiGHT、DBSNP、Cancer Hotspots、COSMIC、JAX CKB、OncoKB等
检测突变软件:ADXHS-Classic-H
标本病理评估:肿瘤细胞占比30%。
DNA质量评估:合格
测序质量评估:合格
表格结果:
检测内容 检测结果 突变丰度 备注
MSI MSS 0/55
EGFR exon19 c.2235_2249del p.Glu746_Ala750del(E746_A750del) 29.59% I级,具有明确临床意义
MET 扩增 3.97 I级,具有明确临床意义
TP53 exon8 p.817C>T p.Arg273Cys(R273C) 6.35% II级,具有潜在临床意义
检测结果备注:表格内未列出的为未检出。
报告医生
生
报告时间
2026-02-06 16:26
住院号
门诊号
送检医生
病人编号
1份已审核
2026-01-30 14:10:13
4.0
无
2份已审核
2026-01-28 09:16:53
4.0
55
无
1份已审核
2020-12-28 12:02
2.0
58床
无
2020-12-21 14:02
2.0
58床
无
分子病理检查报告单
编
患者姓名
性别：男
年龄：75岁
住院号：
送检科室
尿府理
登记号：
标本类型：石蜡组织
病变部
病理诊断：
收到日期：2026-01-20
检查项目：肿瘤多基因检测（含MSI）
检查方法：高通量测序(NGS)
参考基因组：GRCh37/hg19
临床数据库：1000 Genomes、ExAC、gnomAD、ClinVar、BECA Exchange InSiGHT、DBSNP、
Cancer Hotspots、COSMIC、JAX CXB、OncoKB等
检测突变软件：ADXHS-Classic-H
标本病理评估：肿瘤细胞占比30%。
核酸质量评估：合格
测序质量评估：合格
检测结果：
检测内容
检测结果
突变丰度
备注
MSI
MSS
0/55
EGFR
exon19 c.2235_2249del
29.59%
I级、具有明确临床意义
p.Glu746_Ala750del (E746_A750del)
MET
3'端
3.97
I级、具有明确临床意义
TP53
exon6 c.817C>T p.Arg273Cys (R273C)
6.35%
II级、具有潜在临床意义
备注：表格内未列出的为未检出。
注：此报告仅针对本次送检样本，仅供临床医生参考。如有疑问，请于7个工作日内与分子病理诊断科联系。
报告.
检测者
报告日期：2026-02-06
第1页/共16页
CS 扫描全能王
3亿人都在用的扫描App
V2.0
循环周期，调节转录，DNA 复
制和诱导细胞程序死亡及抗血
管生成。
细胞瘤）和肾上腺皮质癌。TP53 突变还发生于包括 CML、
ANLL、MDS 及 B-NHL。在内的多种恶性血液肿瘤以及
黑色素瘤、基底细胞癌、鳞状细胞癌等皮肤癌等多种类型
肝癌及恶性肿瘤。TP53 突变是多种癌症预后不良的标
志，如乳腺癌。TP53 基因变异与肿瘤细胞对铂类化疗药
物耐药性相关，但不影响氟杉醇类药物的敏感性；相关化
疗药物还包括喜树碱、5-FU、顺铂、环磷酰胺等。FDA 已
授予 IXC14586 快速通道资格，目前治疗具有 TP53 Y220C
突变的局部晚期或转移性实体瘤患者。
四、声明告知
1. 本检测项目中使用的参考基因组版本为 hg19，报告中的变异命名遵从 HGVS 指南
(http://varnomcn.hgvs.org)中的相关规定进行命名。
2. 变异分类：综合变异在治疗、诊断和预后方面相关研究证据，将变异分为 4 级：I
级为明确临床意义；II 级为潜在临床意义；III 类为临床意义未明；IV 级为良性/可能良
性。本报告中仅列出 I-III 级变异。
3. 检测结果与临床意义相关性的证据水平分为 4 个等级（A/B/C/D）。A 级：对应
病种中 FDA/NMPA 批准或指南推荐的治疗、诊断和（或）预后的相关标志物；B 级：专家
共识或 III/IV 期临床试验研究表明对患者肿瘤治疗有敏感或耐药、或具有诊断、预后意义
的生物标志物；C 级：FDA/NMPA 批准或专业指南推荐的在其他癌种对某个治疗方案敏感
或耐药的标志物；或者是作为临床试验入组标准的标志物；或者是多个小型研究结果证实
具有诊断或预后意义的标志物；D 级：临床前研究表明具有潜在的治疗意义，或基于小型
研究或多个案例报告可能作为辅助疾病诊断或预后的标志物（结论未形成共识）。
4. 本检测的检测内容大部分基于仅限于 DNA 水平，部分基因涉及 RNA 水平，但
不涉及蛋白水平的检测。
5. 对于组织样品，如样本中肿瘤细胞含量低于 20%，可能影响检测结果的准确性；
如未检出指定的基因变异，可能由于该样本中该突变的丰度低于本项目的检测下限。
6. 对于组织样品，肿瘤存在异质性，即不同病灶甚至同一病灶内的组织的突变图谱可
能也存在差异；另外，不同疾病发展或治疗阶段取出的样本中的突变可能不同；因此，本
检测报告仅对此次送检的样本负责。并且，所检测的突变位点仅限于本检测试剂的检测范
围，样品的基因组中可能存在的某些罕见或复杂突变，本项目不能完全检测。
7. 本报告对于测序结果分析中核苷酸改变的位置信息是基于当前版本的基因组和转录
本，随着人类基因组的更新，这些信息可能会有所不同；同时对于突变位点的解读，是基
于当前已发表的文献、指南、公共数据库及临床研究结果，随着研究的发展，特定位点的
解读可能发生变更。
8. 本检测仅为临床治疗或诊断提供参考，具体的诊断结果及治疗决策应由临床医生综
合患者的各种临床信息和检测结果进行判断。
CS 扫描全能王
3 亿人都在用的扫描 App
---
超声检查报告单
思者登
姓
性别：男
年龄：75岁
床号：A02
检查所见：
右肝最大斜径12.8cm，左肝前后径6.4cm，上下径7.5cm，肝表面光滑，边缘规则，肝内
呈细小点状回声，分布欠均匀，肝内见数个囊性回声，大者0.8x0.5cm，均透声可。
空腹胆囊充盈差，胆囊区见胆囊祥回声，大小约3.4x1.4cm，腔内透声差，充满细密点
状回声。
胆总管内径0.5cm，未见明显异常回声，肝内胆管无明显扩张。
胰腺大小形态可，表面光滑，内回声均匀，主胰管内径不宽。
脾未探及。
门静脉走行自然，呈入肝血流，门静脉主干内径1.0cm，入肝血流速度17.4cm/s，肝内
门静脉血流充盈好，未见明显异常回声。
肝静脉走行自然，各支内径不宽，腔内未见明显异常回声，血流速及频谱形态未见异
常。
双侧肾上腺区未见明显占位性病变。
双肾大小形态正常，表面光滑，皮髓质分界清，左肾实质回声无明显异常，右肾中部实
质内见1.5x1.2cm略高回声结节，边界清，双肾窦无分离扩张。
双侧输尿管无明显扩张。
膀胱充盈可，黏膜光滑，腔内未见明显占位。
前列腺大小约4.0（左右径）×3.5（前后径）×3.2（上下径）cm，体积约23.3cm3，
表面光滑，中叶略突，内部回声欠均匀。
双侧精囊腺无肿大，内部回声均匀。
双肾动脉主干血流通畅，肾内动脉血流分布好。
左肾叶间动脉Vs 24.8cm/s，阻力指数（RI）0.66。
右肾叶间动脉Vs 25.1cm/s，阻力指数（RI）0.65。
超声提示：脾切除术后
空腹胆囊充盈差、腔内透声差，慢性胆囊炎？请结合临床
肝囊肿
右肾略高回声结节，考虑良性（结合病史考虑复杂囊肿可能）
前列腺增生并钙化
报告日期：2026-01-27 08:35:35 记录人
CS 扫描全能王
---
超声检查报告单
患者登记
姓名：
性别：男
年龄：75岁
号
1
2
检查所见：
甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。
甲状旁腺区未见明显异常回声。
左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门
髓结构不清，CDFI：内见条状血流信号。
右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。
超声提示：左侧颈部淋巴结肿大，考虑“M”性可能
报告日期：2026-01-27 08:26:34 记
名.
注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。
CS 扫描全能王
---
影像学检查报告单
扫一扫查看云胶片（访问码）：
姓名：
性别：男
年龄：75岁
影像
住院号：
登记号：
检查名称：胸部CT增强成像（单独）
检查方法：AXI+C
图像所见：胸廓及胸腔容积基本正常。纵隔左偏。左肺可见软组织密度肿块，边界不
清，大小约59mm*66mm，较前2024.09.03CT所示明显增大，呈不均匀强
化。左主支气管及左肺上叶、下叶支气管狭窄，其远端肺组织实变，较前
相仿。左肺下叶后基底段(6im53-54)见实性结节，大小约为11mm×8mm。
双肺见多发小、微结节，较大者位于左肺下叶背段(6im39-41)，呈实性
密度，大小约为9mm×7mm。双肺见多发斑片、索条影。气管未见狭窄或梗
阻。纵隔及左肺门可见多发肿大淋巴结，较前相仿。心影未见明显增大。
左侧部分肋骨局部形态不规整。
印象：左肺癌并纵隔、左肺门肿大淋巴结转移复查所见，较前进展，请结合临床
双肺多发结节，较前增多、增大，请结合临床随访
双肺慢性炎症或纤维灶可能性大，请结合临床
左侧部分肋骨局部形态不规整，请结合临床
报告医师
审核医
该报告仅供临床医师参考；如需商榷，请通过临床医师与审核医师沟通
流水号
2026-08-10 17:49:03,503 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=影像学检查报告单
姓名：
性别：男
年龄：70岁
影像
检查日期：2020-12-23
报告日期：2020-12-23
报告时间：10.00
检查名称：全身骨显像
检查方法：显像剂：99mTc-MDP
图像所见：静脉注射显像剂2小时后行全身骨显像，图像清晰，对比度可。
前位：双侧膝关节见显像剂浓聚灶。颅骨，锁骨，胸骨，前肋，骨盆显像
剂分布基本左右对称，未见明显异常显像剂浓聚或稀疏区。
后位：脊椎见显像剂浓聚灶。颅骨，肩胛骨，后肋，骨盆显像剂分布基本
左右对称，未见明显异常显像剂浓聚或稀疏区。
印
象：1，脊椎及双侧膝关节退行性变可能性大
2，其余部位骨骼未见明显转移瘤，建议定期复查
报告[
审核医师：
该报告反映受检者当时情况，仅供临床医师参考。
流水号
---
影像学检查报告单
扫码看电子胶片
姓
性别：男
年龄：70岁
影像
科
住院
检查日期：2020-12-22
报告日期：2020-12-23
报告时间：14:22:52
登记号
40
检查名称：颅脑MR平扫成像+DWI成像
检查方法：AXI:FSE T1WI, T2WI, FLAIR, DWI
SAG:FSE T1WI
图像所见：双侧额顶叶白质可见散在斑点状等T1稍长T2信号影，FLAIR为高信号，
DWI为等信号。脑室系统略扩大，脑沟、脑池明显加深，中线结构居中。
印象：1. 血管性脱髓鞘（Fazekas 1级），请结合临床复查
2. 老年性脑改变
报告
审核医师：
该报告反映受检者当时情况，仅供临床医师参考。
流水号
CS 扫描全能王
---
超声检查报告单
患者
性别：男
年龄：75岁
检查所见：
甲状腺大小尚可，内回声欠均匀，未探及具体结节。CDFI：腺体内血流信号未见明显异常。
甲状旁腺区未见明显异常回声。
左侧颈部III区见1.7x0.8cm肿大淋巴结，左侧颈部IV区见2.3x1.6cm肿大淋巴结，均门
髓结构不清，CDFI：内见条状血流信号。
右侧颈部未见明显有意义肿大淋巴结，未见明显囊实性肿物。
超声提示：左侧颈部淋巴结肿大，考虑“Ⅱ”性可能
报告日期：2026-01-27 08:26:34 记录
师
注：该报告反映受检者当时情况，仅供临床医师参考。请结合临床及其他检查进一步诊断。
---
心电图报告单
性别：男
年龄：75岁
危重症医学科率：69 bpm
P-R间期：139 ms
QRS时间：90 ms
QT/QTc : 414/445 ms
P-R-T : 63/22/25 度
SV1/RV5:0.49/1.35 mV
RV5+SV1:1.84mV
诊断：大致正常心电图
检查时间：2026-01-26 10:31:55
检查医生：
I
II
III
AVR
AVL
AVF
V1
V2
V3
V4
V5
V6
检查者：
25 mm/s 10 mm/mv
报告审核
时间：2026-01-26 10:35:22
以上结果请结合临床及前图
1/1
2026-08-10 17:49:03,716 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 17:49:03,716 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "20 items, types={'LabReport': 5, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 12}", "name": "07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf", "embedding_token_consumption": 17646}
2026-08-10 17:49:03,716 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 17:49:04,083 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 17:49:04,084 INFO     29 [Trace] task=cc093d2e | doc=07-毓璜顶-FJPI，后线肺癌，方穹招募推荐.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":20,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 17:49:04,093 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(23, 74, 108, 142, 154) row[-1]=(23, 418, 476, 158, 170)
2026-08-10 17:49:04,094 INFO     29 [DIAG-EXECUTOR] row_position_int len=10 row[0]=(24, 75, 148, 148, 160) row[-1]=(24, 58, 148, 293, 305)
2026-08-10 17:49:04,094 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(25, 84, 248, 160, 174) row[-1]=(25, 84, 172, 237, 250)
2026-08-10 17:49:04,094 INFO     29 [DIAG-EXECUTOR] row_position_int len=12 row[0]=(26, 79, 127, 146, 160) row[-1]=(26, 79, 148, 324, 336)
2026-08-10 17:49:04,094 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,094 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,095 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,095 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,095 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,095 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,095 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,095 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,096 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,096 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,096 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,096 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,096 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,096 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,096 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 17:49:04,102 INFO     29 set_progress(cc093d2e94e111f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 17:49:04 [DOC Engine]:
Start to index...
2026-08-10 17:49:04,143 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.036s]
2026-08-10 17:49:04,148 INFO     29 set_progress(cc093d2e94e111f1bd9827cf206dfa2d), progress: 0.805, progress_msg: 
2026-08-10 17:49:04,173 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-10 17:49:04,198 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.017s]
2026-08-10 17:49:04,221 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-10 17:49:04,243 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 17:49:04,251 INFO     29 set_progress(cc093d2e94e111f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 17:49:04 Indexing done (0.15s). Task done (794.95s)
2026-08-10 17:49:04,254 INFO     29 [Done], chunks(20), token(17646), elapsed:794.95
2026-08-10 17:49:04,708 INFO     29 handle_task done for task {"id": "cc093d2e94e111f1bd9827cf206dfa2d", "doc_id": "cbc5ba5e94e111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "07-\u6bd3\u749c\u9876-FJPI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 4814116, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786383293693, "task_type": "dataflow", "root_trace_id": "26dd64836dd04f3fa19e8095283bd42a", "root_traceparent": "00-26dd64836dd04f3fa19e8095283bd42a-d9475622c9d0d2d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
