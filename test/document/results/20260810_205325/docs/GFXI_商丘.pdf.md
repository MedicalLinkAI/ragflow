# 基准结果：GFXI 商丘.pdf

## 基本信息

- 文件：`GFXI 商丘.pdf`
- 大小：3218.5 KB
- PDF 总页数：4
- doc_id：`6067e0fa94bb11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T20:59:51  完成时间：2026-08-10T21:02:28  耗时：156.7s
- progress_msg：`13:02:26 Indexing done (0.03s). Task done (147.02s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | f69d93bd | 3 | 1-3 | 民权县人民医院 入院记录 姓名： 科室：呼吸二病区 床号：111 住院号： 体格 |
| 2 | b1ba7a71 | 1 | 4-4 | 民权县人民医院 肺功能检查报告 病人ID: 2023-08-1501 性别： 女 |

- chunks 总数：2
- 各 chunk 页数合计（含跨页重复）：4
- 页码并集：`[1, 2, 3, 4]`
- 覆盖页数：4 / 4；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "ExaminationReport": 1}`
- ChunkMerger：`{"found": true, "merged": 2, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:02:26,172 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 12:59:52,659 INFO     29 handle_task begin for task {"id": "60a23a7a94bb11f1bd9827cf206dfa2d", "doc_id": "6067e0fa94bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366792626, "task_type": "dataflow", "root_trace_id": "94d1339f4db64958b3764c87ea29c5c0", "root_traceparent": "00-94d1339f4db64958b3764c87ea29c5c0-51b0d67fb5a77038-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 12:59:52,854 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 12:59:52,977 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 12:59:52,989 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:59:52,989 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 12:59:52,989 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 12:59:53,002 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 12:59:53,003 INFO     29 ============================================================
2026-08-10 12:59:53,003 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 12:59:53,003 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 12:59:53,003 INFO     29 ============================================================
2026-08-10 12:59:53,003 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 12:59:53,003 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 12:59:53,017 INFO     29 No torch found.
2026-08-10 12:59:53,489 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=4
2026-08-10 12:59:53,680 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1045252, prompt_len=764
2026-08-10 12:59:56,539 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:59:56,540 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 12:59:56,551 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1045252, prompt_len=401
2026-08-10 13:00:01,641 INFO     29 [qwen-vl-parser] text API response (len=836):
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：111", "住院号：", "体格检查", "T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg", "发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧", "虑，走入病房，检查合作。", "皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，", "无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。", "淋巴结：全身浅表淋巴结无肿大。", "头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔", "2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦", "无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、", "红肿，声音无嘶哑。", "颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流", "征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿", "大。", "胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、", "皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。", "肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发", "感。叩诊音呈清音。呼吸音异常干性啰音。", "心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所", "示。心率82次/分，心律齐。", "腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、", "条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。", "四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强", "直、畸形。", "肛门、直肠：未查。", "外生殖器：未查。", "专科检查", "第2页"]
2026-08-10 13:00:01,641 INFO     29 [qwen-vl-parser] page=1 text: 34 lines (bbox 0-33)
2026-08-10 13:00:01,641 INFO     29 [qwen-vl-parser] page=1 text: 34 sections
2026-08-10 13:00:01,870 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1363491, prompt_len=764
2026-08-10 13:00:03,276 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:00:03,277 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:00:03,292 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1363491, prompt_len=401
2026-08-10 13:00:09,486 INFO     29 [qwen-vl-parser] text API response (len=997):
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：111", "住院号：", "科室：呼吸二病区", "第(1)次住院", "过敏史：无", "姓名：盖凤先", "性别：女", "年龄：67岁", "入院时间：2025-04-09 10:34", "职业：农民", "民族：回族", "婚姻：已婚", "记录时间：2025-04-09 10:34", "籍贯：河南省商丘市", "入院情况：有", "联系方式：15824782345", "现住址：河南省商丘市民权县伯党乡伯西村", "病史陈述者：本人", "可靠程度：供参", "委会", "考", "工作单位：-", "身份证号：412323195712211247", "联系人：白磊", "与患者关系：子", "联系人电话：15824782345", "主诉：胸闷、咳嗽、咳痰20余年，加重2天。", "现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，", "期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动", "稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，", "门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠", "尚可，大小便无异常，体重无明显改变。", "既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血", "史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。", "个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟", "史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触", "史，无疫区接触史，无冶游史。", "婚姻史：25岁结婚，配偶健康。", "月经生育史：", "13", "3-5", "28-30", "50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，", "均健康。", "家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性", "疾病。", "第1页"]
2026-08-10 13:00:09,486 INFO     29 [qwen-vl-parser] page=2 text: 51 lines (bbox 34-84)
2026-08-10 13:00:09,487 INFO     29 [qwen-vl-parser] page=2 text: 51 sections
2026-08-10 13:00:09,602 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=440773, prompt_len=764
2026-08-10 13:00:10,841 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:00:10,841 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 13:00:10,852 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=440773, prompt_len=401
2026-08-10 13:00:12,260 INFO     29 [qwen-vl-parser] text API response (len=216):
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：", "住院号：", "肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、", "皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。", "辅助检查", "暂无。", "初步诊断", "1.哮喘（急性发作）", "2.慢性支气管炎", "住院医师：王贝贝", "主治医师：陈文宁", "主任医师：已签字", "第3页"]
2026-08-10 13:00:12,260 INFO     29 [qwen-vl-parser] page=3 text: 17 lines (bbox 85-101)
2026-08-10 13:00:12,260 INFO     29 [qwen-vl-parser] page=3 text: 17 sections
2026-08-10 13:00:12,492 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1369478, prompt_len=764
2026-08-10 13:00:13,888 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2023-08-15"
}
```
2026-08-10 13:00:13,889 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2023-08-15
2026-08-10 13:00:13,896 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1369478, prompt_len=401
2026-08-10 13:00:18,935 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:00:18.934+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 36, "failed": 0, "current": {"60a23a7a94bb11f1bd9827cf206dfa2d": {"id": "60a23a7a94bb11f1bd9827cf206dfa2d", "doc_id": "6067e0fa94bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366792626, "task_type": "dataflow", "root_trace_id": "94d1339f4db64958b3764c87ea29c5c0", "root_traceparent": "00-94d1339f4db64958b3764c87ea29c5c0-51b0d67fb5a77038-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:00:19,200 INFO     29 [qwen-vl-parser] text API response (len=1145):
["民权县人民医院", "肺功能检查报告", "病人ID:", "2023-08-1501", "性别：", "女", "高度：", "158 cm", "名：", "出生日期：", "1957/7/2", "体重：", "60 kg", "姓：", "年龄：", "66 years", "BMI：", "24.0 kg/m²", "体积", "流量", "体积", "时间[s]", "时间[s]", "单位", "预测值", "之前", "%预值", "沙丁胺醇", "(400", "%预值", "%变化", "ug)", "VC", "I", "(1)", "2.37", "1.66", "70%", "2.20", "93%", "+32.2%", "VC", "I", "(1)", "2.37", "1.66", "70%", "2.20", "93%", "+32.2%", "FEV1", "I", "(1)", "1.99", "0.88", "44%", "1.27", "64%", "+44.4%", "FEV1/FVC", "%", "(1)", "77", "53", "69%", "58", "75%", "+9.3%", "FEV1/VC", "%", "(1)", "77", "53", "69%", "58", "75%", "+9.3%", "PEF", "l/s", "(1)", "5.60", "2.06", "37%", "2.74", "49%", "+32.9%", "MEF75", "l/s", "(1)", "5.04", "0.97", "19%", "1.53", "30%", "+57.6%", "MEF50", "l/s", "(1)", "3.38", "0.49", "14%", "0.78", "23%", "+60.6%", "MEF25", "l/s", "(1)", "1.12", "0.22", "19%", "0.29", "26%", "+35.4%", "诊断意见：", "1.重度混合型通气功能障碍，小气道功能减低。", "2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。", "3.MVV:44%。建议定期复查。", "(1): ECCS 1993", "-1-", "BTPS: 21.0 °C, 1013 hPa,", "检测: 2023/8/15", "50%", "医生:-", "Geratherm Respiratory GmbH", "www.geratherm-respiratory.com", "Blue Cherry V1.2.2.24"]
2026-08-10 13:00:19,201 INFO     29 [qwen-vl-parser] page=4 text: 126 lines (bbox 102-227)
2026-08-10 13:00:19,202 INFO     29 [qwen-vl-parser] page=4 text: 126 sections
2026-08-10 13:00:19,202 INFO     29 [qwen-vl-parser] parse_pdf done: 228 sections from 4 pages.
2026-08-10 13:00:19,223 INFO     29 Close text detector.
2026-08-10 13:00:19,733 INFO     29 Close text recognizer.
2026-08-10 13:00:20,127 INFO     29 Close recognizer.
2026-08-10 13:00:20,510 INFO     29 Close recognizer.
2026-08-10 13:00:21,203 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:00:21,203 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Parser:MedLink | outputs={"html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "json"}
2026-08-10 13:00:21,205 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:00:21,226 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:21,226 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 民权县人民医院\n[BBOX-1] 入院记录\n[BBOX-2] 姓名：\n[BBOX-3] 科室：呼吸二病区\n[BBOX-4] 床号：111\n[BBOX-5] 住院号：\n[BBOX-6] 体格检查\n[BBOX-7] T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg\n[BBOX-8] 发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧\n[BBOX-9] 虑，走入病房，检查合作。\n[BBOX-10] 皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，\n[BBOX-11] 无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。\n[BBOX-12] 淋巴结：全身浅表淋巴结无肿大。\n[BBOX-13] 头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔\n[BBOX-14] 2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦\n[BBOX-15] 无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、\n[BBOX-16] 红肿，声音无嘶哑。\n[BBOX-17] 颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流\n[BBOX-18] 征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿\n[BBOX-19] 大。\n[BBOX-20] 胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、\n[BBOX-21] 皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。\n[BBOX-22] 肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发\n[BBOX-23] 感。叩诊音呈清音。呼吸音异常干性啰音。\n[BBOX-24] 心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所\n[BBOX-25] 示。心率82次/分，心律齐。\n[BBOX-26] 腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、\n[BBOX-27] 条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。\n[BBOX-28] 四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强\n[BBOX-29] 直、畸形。\n[BBOX-30] 肛门、直肠：未查。\n[BBOX-31] 外生殖器：未查。\n[BBOX-32] 专科检查\n[BBOX-33] 第2页\n[BBOX-34] 民权县人民医院\n[BBOX-35] 入院记录\n[BBOX-36] 姓名：\n[BBOX-37] 科室：呼吸二病区\n[BBOX-38] 床号：111\n[BBOX-39] 住院号：\n[BBOX-40] 科室：呼吸二病区\n[BBOX-41] 第(1)次住院\n[BBOX-42] 过敏史：无\n[BBOX-43] 姓名：盖凤先\n[BBOX-44] 性别：女\n[BBOX-45] 年龄：67岁\n[BBOX-46] 入院时间：2025-04-09 10:34\n[BBOX-47] 职业：农民\n[BBOX-48] 民族：回族\n[BBOX-49] 婚姻：已婚\n[BBOX-50] 记录时间：2025-04-09 10:34\n[BBOX-51] 籍贯：河南省商丘市\n[BBOX-52] 入院情况：有\n[BBOX-53] 联系方式：15824782345\n[BBOX-54] 现住址：河南省商丘市民权县伯党乡伯西村\n[BBOX-55] 病史陈述者：本人\n[BBOX-56] 可靠程度：供参\n[BBOX-57] 委会\n[BBOX-58] 考\n[BBOX-59] 工作单位：-\n[BBOX-60] 身份证号：412323195712211247\n[BBOX-61] 联系人：白磊\n[BBOX-62] 与患者关系：子\n[BBOX-63] 联系人电话：15824782345\n[BBOX-64] 主诉：胸闷、咳嗽、咳痰20余年，加重2天。\n[BBOX-65] 现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，\n[BBOX-66] 期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动\n[BBOX-67] 稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，\n[BBOX-68] 门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠\n[BBOX-69] 尚可，大小便无异常，体重无明显改变。\n[BBOX-70] 既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血\n[BBOX-71] 史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。\n[BBOX-72] 个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟\n[BBOX-73] 史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触\n[BBOX-74] 史，无疫区接触史，无冶游史。\n[BBOX-75] 婚姻史：25岁结婚，配偶健康。\n[BBOX-76] 月经生育史：\n[BBOX-77] 13\n[BBOX-78] 3-5\n[BBOX-79] 28-30\n[BBOX-80] 50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，\n[BBOX-81] 均健康。\n[BBOX-82] 家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性\n[BBOX-83] 疾病。\n[BBOX-84] 第1页\n[BBOX-85] 民权县人民医院\n[BBOX-86] 入院记录\n[BBOX-87] 姓名：\n[BBOX-88] 科室：呼吸二病区\n[BBOX-89] 床号：\n[BBOX-90] 住院号：\n[BBOX-91] 肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、\n[BBOX-92] 皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。\n[BBOX-93] 辅助检查\n[BBOX-94] 暂无。\n[BBOX-95] 初步诊断\n[BBOX-96] 1.哮喘（急性发作）\n[BBOX-97] 2.慢性支气管炎\n[BBOX-98] 住院医师：王贝贝\n[BBOX-99] 主治医师：陈文宁\n[BBOX-100] 主任医师：已签字\n[BBOX-101] 第3页\n[BBOX-102] 民权县人民医院\n[BBOX-103] 肺功能检查报告\n[BBOX-104] 病人ID:\n[BBOX-105] 2023-08-1501\n[BBOX-106] 性别：\n[BBOX-107] 女\n[BBOX-108] 高度：\n[BBOX-109] 158 cm\n[BBOX-110] 名：\n[BBOX-111] 出生日期：\n[BBOX-112] 1957/7/2\n[BBOX-113] 体重：\n[BBOX-114] 60 kg\n[BBOX-115] 姓：\n[BBOX-116] 年龄：\n[BBOX-117] 66 years\n[BBOX-118] BMI：\n[BBOX-119] 24.0 kg/m²\n[BBOX-120] 体积\n[BBOX-121] 流量\n[BBOX-122] 体积\n[BBOX-123] 时间[s]\n[BBOX-124] 时间[s]\n[BBOX-125] 单位\n[BBOX-126] 预测值\n[BBOX-127] 之前\n[BBOX-128] %预值\n[BBOX-129] 沙丁胺醇\n[BBOX-130] (400\n[BBOX-131] %预值\n[BBOX-132] %变化\n[BBOX-133] ug)\n[BBOX-134] VC\n[BBOX-135] I\n[BBOX-136] (1)\n[BBOX-137] 2.37\n[BBOX-138] 1.66\n[BBOX-139] 70%\n[BBOX-140] 2.20\n[BBOX-141] 93%\n[BBOX-142] +32.2%\n[BBOX-143] VC\n[BBOX-144] I\n[BBOX-145] (1)\n[BBOX-146] 2.37\n[BBOX-147] 1.66\n[BBOX-148] 70%\n[BBOX-149] 2.20\n[BBOX-150] 93%\n[BBOX-151] +32.2%\n[BBOX-152] FEV1\n[BBOX-153] I\n[BBOX-154] (1)\n[BBOX-155] 1.99\n[BBOX-156] 0.88\n[BBOX-157] 44%\n[BBOX-158] 1.27\n[BBOX-159] 64%\n[BBOX-160] +44.4%\n[BBOX-161] FEV1/FVC\n[BBOX-162] %\n[BBOX-163] (1)\n[BBOX-164] 77\n[BBOX-165] 53\n[BBOX-166] 69%\n[BBOX-167] 58\n[BBOX-168] 75%\n[BBOX-169] +9.3%\n[BBOX-170] FEV1/VC\n[BBOX-171] %\n[BBOX-172] (1)\n[BBOX-173] 77\n[BBOX-174] 53\n[BBOX-175] 69%\n[BBOX-176] 58\n[BBOX-177] 75%\n[BBOX-178] +9.3%\n[BBOX-179] PEF\n[BBOX-180] l/s\n[BBOX-181] (1)\n[BBOX-182] 5.60\n[BBOX-183] 2.06\n[BBOX-184] 37%\n[BBOX-185] 2.74\n[BBOX-186] 49%\n[BBOX-187] +32.9%\n[BBOX-188] MEF75\n[BBOX-189] l/s\n[BBOX-190] (1)\n[BBOX-191] 5.04\n[BBOX-192] 0.97\n[BBOX-193] 19%\n[BBOX-194] 1.53\n[BBOX-195] 30%\n[BBOX-196] +57.6%\n[BBOX-197] MEF50\n[BBOX-198] l/s\n[BBOX-199] (1)\n[BBOX-200] 3.38\n[BBOX-201] 0.49\n[BBOX-202] 14%\n[BBOX-203] 0.78\n[BBOX-204] 23%\n[BBOX-205] +60.6%\n[BBOX-206] MEF25\n[BBOX-207] l/s\n[BBOX-208] (1)\n[BBOX-209] 1.12\n[BBOX-210] 0.22\n[BBOX-211] 19%\n[BBOX-212] 0.29\n[BBOX-213] 26%\n[BBOX-214] +35.4%\n[BBOX-215] 诊断意见：\n[BBOX-216] 1.重度混合型通气功能障碍，小气道功能减低。\n[BBOX-217] 2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。\n[BBOX-218] 3.MVV:44%。建议定期复查。\n[BBOX-219] (1): ECCS 1993\n[BBOX-220] -1-\n[BBOX-221] BTPS: 21.0 °C, 1013 hPa,\n[BBOX-222] 检测: 2023/8/15\n[BBOX-223] 50%\n[BBOX-224] 医生:-\n[BBOX-225] Geratherm Respiratory GmbH\n[BBOX-226] www.geratherm-respiratory.com\n[BBOX-227] Blue Cherry V1.2.2.24"
  }
]
2026-08-10 13:00:24,819 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:24,846 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'ExaminationReport': 1}
2026-08-10 13:00:24,853 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:00:24,854 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks": "2 items, types={'AdmissionRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 13:00:24,854 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:00:24,854 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Admission': 1, 'chunks_Examination': 1}
2026-08-10 13:00:24,863 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:00:24,863 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | ChunkRouter:Router | outputs={"html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks": "2 items, types={'AdmissionRecord': 1, 'ExaminationReport': 1}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:00:24,863 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:00:24,867 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:24,867 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:00:26,044 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:26,050 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:00:26,050 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:00:26,050 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:00:26,055 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:26,055 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:00:27,252 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:27,259 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:00:27,260 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:00:27,260 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:00:27,265 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:27,265 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:00:27,769 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:27,779 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:00:27,779 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:00:27,779 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:00:27,786 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:27,787 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:00:28,494 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:28,499 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:00:28,499 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:00:28,499 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:00:28,504 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:28,504 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:00:28,921 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:28,927 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:00:28,927 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:00:28,927 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:00:28,932 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:28,932 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:00:29,405 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:29,417 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:00:29,417 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:00:29,417 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:00:29,424 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:00:29,425 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:00:29,425 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 13:00:29,425 INFO     29 [qwen-vl-text] positions(101): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:00:29,425 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2], lines per page: [34, 51, 16]
2026-08-10 13:00:29,600 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:00:29,817 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:00:29,952 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:00:29,953 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1738
2026-08-10 13:00:29,953 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:29,954 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 100, \"encounter_dates\": [\"2025-04-09\"], \"department\": \"呼吸二病区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "民权县人民医院\n入院记录\n姓名：\n科室：呼吸二病区\n床号：111\n住院号：\n体格检查\nT:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg\n发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧\n虑，走入病房，检查合作。\n皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，\n无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。\n淋巴结：全身浅表淋巴结无肿大。\n头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔\n2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦\n无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、\n红肿，声音无嘶哑。\n颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流\n征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿\n大。\n胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、\n皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。\n肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发\n感。叩诊音呈清音。呼吸音异常干性啰音。\n心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所\n示。心率82次/分，心律齐。\n腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、\n条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。\n四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强\n直、畸形。\n肛门、直肠：未查。\n外生殖器：未查。\n专科检查\n第2页\n民权县人民医院\n入院记录\n姓名：\n科室：呼吸二病区\n床号：111\n住院号：\n科室：呼吸二病区\n第(1)次住院\n过敏史：无\n姓名：盖凤先\n性别：女\n年龄：67岁\n入院时间：2025-04-09 10:34\n职业：农民\n民族：回族\n婚姻：已婚\n记录时间：2025-04-09 10:34\n籍贯：河南省商丘市\n入院情况：有\n联系方式：15824782345\n现住址：河南省商丘市民权县伯党乡伯西村\n病史陈述者：本人\n可靠程度：供参\n委会\n考\n工作单位：-\n身份证号：412323195712211247\n联系人：白磊\n与患者关系：子\n联系人电话：15824782345\n主诉：胸闷、咳嗽、咳痰20余年，加重2天。\n现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，\n期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动\n稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，\n门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠\n尚可，大小便无异常，体重无明显改变。\n既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血\n史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。\n个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟\n史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触\n史，无疫区接触史，无冶游史。\n婚姻史：25岁结婚，配偶健康。\n月经生育史：\n13\n3-5\n28-30\n50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，\n均健康。\n家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性\n疾病。\n第1页\n民权县人民医院\n入院记录\n姓名：\n科室：呼吸二病区\n床号：\n住院号：\n肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、\n皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。\n辅助检查\n暂无。\n初步诊断\n1.哮喘（急性发作）\n2.慢性支气管炎\n住院医师：王贝贝\n主治医师：陈文宁\n主任医师：已签字",
    "role": "user"
  }
]
2026-08-10 13:00:39,677 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:00:39,677 INFO     29 [qwen-vl-text] LLM output (len=2130):
{
  "encounter_date": "2025-04-09",
  "dm_name": "盖凤先",
  "dm_gender": "女",
  "dm_age": 67,
  "dm_ethnicity": "回族",
  "dm_marital_status": "已婚",
  "dm_occupation": "农民",
  "dm_admission_time": "2025-04-09 10:34",
  "dm_record_time": "2025-04-09 10:34",
  "dm_history_provider": "本人",
  "cc_text": "胸闷、咳嗽、咳痰20余年，加重2天。",
  "cc_main_symptoms": [
    "胸闷",
    "咳嗽",
    "咳痰"
  ],
  "cc_duration": "20余年，加重2天",
  "pi_text": "20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠尚可，大小便无异常，体重无明显改变。",
  "pmh_disease_history": [
    "平素体健",
    "无肝炎、结核类传染病史"
  ],
  "pmh_allergy_history": [
    "无食物过敏史",
    "无药物过敏史"
  ],
  "pmh_surgery_trauma_history": [
    "无手术史",
    "无外伤史"
  ],
  "ph_smoking": "无吸烟史",
  "ph_drinking": "无饮酒嗜好",
  "oh_menarche_age": 13,
  "oh_menopause_age": 50,
  "oh_pregnancies": "孕3产3，育1子2女",
  "fh_text": "父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性疾病。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.4,
  "vs_pulse_bpm": 82,
  "vs_respiration_rpm": 30,
  "vs_systolic_bp_mmhg": 120,
  "vs_diastolic_bp_mmhg": 60,
  "pe_general_condition": "发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧虑，走入病房，检查合作。",
  "pe_skin_mucosa": "色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。",
  "pe_lymph_nodes": "全身浅表淋巴结无肿大。",
  "pe_lungs": "胸廓呈桶状胸。双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。",
  "pe_heart": "心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所示。心率82次/分，心律齐。",
  "pe_abdomen": "形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。",
  "pe_extremities": "无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强直、畸形。",
  "pe_nervous_system": null,
  "pe_specialist_exam": "胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。",
  "pe_ecog_score": null,
  "pat_text": "暂无。",
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "哮喘（急性发作）",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "慢性支气管炎",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": "呼吸二病区"
}
2026-08-10 13:00:39,677 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-09]
2026-08-10 13:00:39,680 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1493212, prompt_len=1448
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：111", "住院号：", "体格检查", "T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg", "发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧", "虑，走入病房，检查合作。", "皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，", "无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。", "淋巴结：全身浅表淋巴结无肿大。", "头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔", "2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦", "无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、", "红肿，声音无嘶哑。", "颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流", "征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿", "大。", "胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、", "皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。", "肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发", "感。叩诊音呈清音。呼吸音异常干性啰音。", "心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所", "示。心率82次/分，心律齐。", "腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、", "条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。", "四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强", "直、畸形。", "肛门、直肠：未查。", "外生殖器：未查。", "专科检查", "第2页"]

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
2026-08-10 13:00:52,090 INFO     29 [qwen-vl-text] coord API raw response (len=2228):
[
	{"text": "民权县人民医院", "bbox": [408, 45, 594, 65]},
	{"text": "入院记录", "bbox": [422, 79, 571, 99]},
	{"text": "姓名：", "bbox": [120, 121, 167, 137]},
	{"text": "科室：呼吸二病区", "bbox": [285, 117, 450, 134]},
	{"text": "床号：111", "bbox": [547, 114, 640, 130]},
	{"text": "住院号：", "bbox": [704, 113, 773, 128]},
	{"text": "体格检查", "bbox": [442, 157, 554, 173]},
	{"text": "T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg", "bbox": [162, 184, 607, 204]},
	{"text": "发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧", "bbox": [164, 207, 887, 235]},
	{"text": "虑，走入病房，检查合作。", "bbox": [117, 243, 350, 263]},
	{"text": "皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，", "bbox": [164, 261, 875, 290]},
	{"text": "无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。", "bbox": [119, 293, 702, 319]},
	{"text": "淋巴结：全身浅表淋巴结无肿大。", "bbox": [165, 326, 461, 346]},
	{"text": "头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔", "bbox": [166, 348, 888, 374]},
	{"text": "2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦", "bbox": [120, 376, 887, 402]},
	{"text": "无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、", "bbox": [122, 404, 893, 430]},
	{"text": "红肿，声音无嘶哑。", "bbox": [123, 441, 294, 458]},
	{"text": "颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流", "bbox": [170, 460, 884, 486]},
	{"text": "征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿", "bbox": [125, 487, 884, 513]},
	{"text": "大。", "bbox": [124, 525, 154, 540]},
	{"text": "胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、", "bbox": [172, 540, 895, 568]},
	{"text": "皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。", "bbox": [125, 574, 555, 596]},
	{"text": "肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发", "bbox": [173, 597, 889, 623]},
	{"text": "感。叩诊音呈清音。呼吸音异常干性啰音。", "bbox": [126, 630, 502, 652]},
	{"text": "心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所", "bbox": [174, 653, 890, 679]},
	{"text": "示。心率82次/分，心律齐。", "bbox": [127, 688, 374, 707]},
	{"text": "腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、", "bbox": [174, 708, 878, 734]},
	{"text": "条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。", "bbox": [128, 740, 624, 762]},
	{"text": "四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强", "bbox": [175, 763, 892, 790]},
	{"text": "直、畸形。", "bbox": [130, 802, 217, 818]},
	{"text": "肛门、直肠：未查。", "bbox": [176, 829, 343, 847]},
	{"text": "外生殖器：未查。", "bbox": [177, 857, 328, 873]},
	{"text": "专科检查", "bbox": [457, 882, 567, 899]},
	{"text": "第2页", "bbox": [483, 933, 543, 946]}
]
2026-08-10 13:00:52,090 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=12.4s
2026-08-10 13:00:52,090 INFO     29 [qwen-vl-text] coord item[0]: text=民权县人民医院, bbox=[408, 45, 594, 65]
2026-08-10 13:00:52,090 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[422, 79, 571, 99]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[120, 121, 167, 137]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[3]: text=科室：呼吸二病区, bbox=[285, 117, 450, 134]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[4]: text=床号：111, bbox=[547, 114, 640, 130]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[704, 113, 773, 128]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[6]: text=体格检查, bbox=[442, 157, 554, 173]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[7]: text=T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg, bbox=[162, 184, 607, 204]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[8]: text=发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧, bbox=[164, 207, 887, 235]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[9]: text=虑，走入病房，检查合作。, bbox=[117, 243, 350, 263]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[10]: text=皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，, bbox=[164, 261, 875, 290]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[11]: text=无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。, bbox=[119, 293, 702, 319]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[12]: text=淋巴结：全身浅表淋巴结无肿大。, bbox=[165, 326, 461, 346]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[13]: text=头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔, bbox=[166, 348, 888, 374]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[14]: text=2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦, bbox=[120, 376, 887, 402]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[15]: text=无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、, bbox=[122, 404, 893, 430]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[16]: text=红肿，声音无嘶哑。, bbox=[123, 441, 294, 458]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[17]: text=颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流, bbox=[170, 460, 884, 486]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[18]: text=征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿, bbox=[125, 487, 884, 513]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[19]: text=大。, bbox=[124, 525, 154, 540]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[20]: text=胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、, bbox=[172, 540, 895, 568]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[21]: text=皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。, bbox=[125, 574, 555, 596]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[22]: text=肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发, bbox=[173, 597, 889, 623]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[23]: text=感。叩诊音呈清音。呼吸音异常干性啰音。, bbox=[126, 630, 502, 652]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[24]: text=心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所, bbox=[174, 653, 890, 679]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[25]: text=示。心率82次/分，心律齐。, bbox=[127, 688, 374, 707]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[26]: text=腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、, bbox=[174, 708, 878, 734]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[27]: text=条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。, bbox=[128, 740, 624, 762]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[28]: text=四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强, bbox=[175, 763, 892, 790]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[29]: text=直、畸形。, bbox=[130, 802, 217, 818]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[30]: text=肛门、直肠：未查。, bbox=[176, 829, 343, 847]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[31]: text=外生殖器：未查。, bbox=[177, 857, 328, 873]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[32]: text=专科检查, bbox=[457, 882, 567, 899]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] coord item[33]: text=第2页, bbox=[483, 933, 543, 946]
2026-08-10 13:00:52,091 INFO     29 [qwen-vl-text] page=0 — 34/34 coords, api_time=12.4s
2026-08-10 13:00:52,093 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1781058, prompt_len=1609
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共51行）
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：111", "住院号：", "科室：呼吸二病区", "第(1)次住院", "过敏史：无", "姓名：盖凤先", "性别：女", "年龄：67岁", "入院时间：2025-04-09 10:34", "职业：农民", "民族：回族", "婚姻：已婚", "记录时间：2025-04-09 10:34", "籍贯：河南省商丘市", "入院情况：有", "联系方式：15824782345", "现住址：河南省商丘市民权县伯党乡伯西村", "病史陈述者：本人", "可靠程度：供参", "委会", "考", "工作单位：-", "身份证号：412323195712211247", "联系人：白磊", "与患者关系：子", "联系人电话：15824782345", "主诉：胸闷、咳嗽、咳痰20余年，加重2天。", "现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，", "期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动", "稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，", "门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠", "尚可，大小便无异常，体重无明显改变。", "既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血", "史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。", "个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟", "史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触", "史，无疫区接触史，无冶游史。", "婚姻史：25岁结婚，配偶健康。", "月经生育史：", "13", "3-5", "28-30", "50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，", "均健康。", "家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性", "疾病。", "第1页"]

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
2026-08-10 13:01:08,979 INFO     29 [qwen-vl-text] coord API raw response (len=3087):
[
	{"text": "民权县人民医院", "bbox": [407, 48, 593, 69]},
	{"text": "入院记录", "bbox": [421, 85, 570, 105]},
	{"text": "姓名：", "bbox": [120, 122, 167, 138]},
	{"text": "科室：呼吸二病区", "bbox": [285, 122, 448, 138]},
	{"text": "床号：111", "bbox": [545, 122, 637, 137]},
	{"text": "住院号：", "bbox": [702, 121, 770, 137]},
	{"text": "科室：呼吸二病区", "bbox": [117, 165, 278, 181]},
	{"text": "第(1)次住院", "bbox": [330, 165, 442, 181]},
	{"text": "过敏史：无", "bbox": [587, 164, 692, 180]},
	{"text": "姓名：盖凤先", "bbox": [117, 190, 227, 206]},
	{"text": "性别：女", "bbox": [330, 190, 413, 206]},
	{"text": "年龄：67岁", "bbox": [455, 190, 555, 206]},
	{"text": "入院时间：2025-04-09 10:34", "bbox": [588, 189, 850, 204]},
	{"text": "职业：农民", "bbox": [117, 215, 217, 231]},
	{"text": "民族：回族", "bbox": [330, 214, 434, 231]},
	{"text": "婚姻：已婚", "bbox": [455, 214, 557, 231]},
	{"text": "记录时间：2025-04-09 10:34", "bbox": [588, 213, 850, 229]},
	{"text": "籍贯：河南省商丘市", "bbox": [117, 240, 294, 256]},
	{"text": "入院情况：有", "bbox": [434, 239, 555, 255]},
	{"text": "联系方式：15824782345", "bbox": [588, 238, 804, 254]},
	{"text": "现住址：河南省商丘市民权县伯党乡伯西村", "bbox": [117, 265, 498, 281]},
	{"text": "病史陈述者：本人", "bbox": [509, 273, 670, 290]},
	{"text": "可靠程度：供参", "bbox": [717, 263, 876, 279]},
	{"text": "委会", "bbox": [117, 285, 157, 301]},
	{"text": "考", "bbox": [717, 282, 737, 298]},
	{"text": "工作单位：-", "bbox": [117, 309, 229, 325]},
	{"text": "身份证号：412323195712211247", "bbox": [509, 308, 794, 324]},
	{"text": "联系人：白磊", "bbox": [117, 335, 238, 351]},
	{"text": "与患者关系：子", "bbox": [334, 335, 475, 351]},
	{"text": "联系人电话：15824782345", "bbox": [619, 334, 855, 350]},
	{"text": "主诉：胸闷、咳嗽、咳痰20余年，加重2天。", "bbox": [167, 362, 575, 378]},
	{"text": "现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，", "bbox": [117, 389, 884, 405]},
	{"text": "期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动", "bbox": [117, 444, 876, 460]},
	{"text": "稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，", "bbox": [117, 470, 876, 486]},
	{"text": "门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠", "bbox": [117, 496, 884, 512]},
	{"text": "尚可，大小便无异常，体重无明显改变。", "bbox": [120, 553, 472, 569]},
	{"text": "既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血", "bbox": [167, 580, 880, 596]},
	{"text": "史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。", "bbox": [120, 608, 742, 624]},
	{"text": "个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟", "bbox": [167, 636, 882, 652]},
	{"text": "史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触", "bbox": [120, 664, 882, 680]},
	{"text": "史，无疫区接触史，无冶游史。", "bbox": [120, 692, 395, 708]},
	{"text": "婚姻史：25岁结婚，配偶健康。", "bbox": [167, 720, 449, 736]},
	{"text": "月经生育史：", "bbox": [167, 756, 278, 772]},
	{"text": "13", "bbox": [320, 760, 338, 774]},
	{"text": "3-5", "bbox": [342, 757, 369, 770]},
	{"text": "28-30", "bbox": [334, 770, 377, 782]},
	{"text": "50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，", "bbox": [404, 754, 891, 770]},
	{"text": "均健康。", "bbox": [122, 805, 192, 821]},
	{"text": "家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性", "bbox": [162, 832, 886, 848]},
	{"text": "疾病。", "bbox": [122, 860, 173, 876]},
	{"text": "第1页", "bbox": [475, 935, 537, 948]}
]
2026-08-10 13:01:08,980 INFO     29 [qwen-vl-text] coord API: raw_items=51, valid_items=51, elapsed=16.9s
2026-08-10 13:01:08,980 INFO     29 [qwen-vl-text] coord item[0]: text=民权县人民医院, bbox=[407, 48, 593, 69]
2026-08-10 13:01:08,980 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[421, 85, 570, 105]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[120, 122, 167, 138]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[3]: text=科室：呼吸二病区, bbox=[285, 122, 448, 138]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[4]: text=床号：111, bbox=[545, 122, 637, 137]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[702, 121, 770, 137]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[6]: text=科室：呼吸二病区, bbox=[117, 165, 278, 181]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[7]: text=第(1)次住院, bbox=[330, 165, 442, 181]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[8]: text=过敏史：无, bbox=[587, 164, 692, 180]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[9]: text=姓名：盖凤先, bbox=[117, 190, 227, 206]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[10]: text=性别：女, bbox=[330, 190, 413, 206]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[11]: text=年龄：67岁, bbox=[455, 190, 555, 206]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[12]: text=入院时间：2025-04-09 10:34, bbox=[588, 189, 850, 204]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[13]: text=职业：农民, bbox=[117, 215, 217, 231]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[14]: text=民族：回族, bbox=[330, 214, 434, 231]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[15]: text=婚姻：已婚, bbox=[455, 214, 557, 231]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[16]: text=记录时间：2025-04-09 10:34, bbox=[588, 213, 850, 229]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[17]: text=籍贯：河南省商丘市, bbox=[117, 240, 294, 256]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[18]: text=入院情况：有, bbox=[434, 239, 555, 255]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[19]: text=联系方式：15824782345, bbox=[588, 238, 804, 254]
2026-08-10 13:01:08,981 INFO     29 [qwen-vl-text] coord item[20]: text=现住址：河南省商丘市民权县伯党乡伯西村, bbox=[117, 265, 498, 281]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[21]: text=病史陈述者：本人, bbox=[509, 273, 670, 290]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[22]: text=可靠程度：供参, bbox=[717, 263, 876, 279]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[23]: text=委会, bbox=[117, 285, 157, 301]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[24]: text=考, bbox=[717, 282, 737, 298]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[25]: text=工作单位：-, bbox=[117, 309, 229, 325]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[26]: text=身份证号：412323195712211247, bbox=[509, 308, 794, 324]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[27]: text=联系人：白磊, bbox=[117, 335, 238, 351]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[28]: text=与患者关系：子, bbox=[334, 335, 475, 351]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[29]: text=联系人电话：15824782345, bbox=[619, 334, 855, 350]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[30]: text=主诉：胸闷、咳嗽、咳痰20余年，加重2天。, bbox=[167, 362, 575, 378]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[31]: text=现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，, bbox=[117, 389, 884, 405]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[32]: text=期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动, bbox=[117, 444, 876, 460]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[33]: text=稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，, bbox=[117, 470, 876, 486]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[34]: text=门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠, bbox=[117, 496, 884, 512]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[35]: text=尚可，大小便无异常，体重无明显改变。, bbox=[120, 553, 472, 569]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[36]: text=既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血, bbox=[167, 580, 880, 596]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[37]: text=史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。, bbox=[120, 608, 742, 624]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[38]: text=个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟, bbox=[167, 636, 882, 652]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[39]: text=史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触, bbox=[120, 664, 882, 680]
2026-08-10 13:01:08,982 INFO     29 [qwen-vl-text] coord item[40]: text=史，无疫区接触史，无冶游史。, bbox=[120, 692, 395, 708]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[41]: text=婚姻史：25岁结婚，配偶健康。, bbox=[167, 720, 449, 736]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[42]: text=月经生育史：, bbox=[167, 756, 278, 772]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[43]: text=13, bbox=[320, 760, 338, 774]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[44]: text=3-5, bbox=[342, 757, 369, 770]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[45]: text=28-30, bbox=[334, 770, 377, 782]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[46]: text=50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，, bbox=[404, 754, 891, 770]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[47]: text=均健康。, bbox=[122, 805, 192, 821]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[48]: text=家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性, bbox=[162, 832, 886, 848]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[49]: text=疾病。, bbox=[122, 860, 173, 876]
2026-08-10 13:01:08,983 INFO     29 [qwen-vl-text] coord item[50]: text=第1页, bbox=[475, 935, 537, 948]
2026-08-10 13:01:08,984 INFO     29 [qwen-vl-text] page=1 — 51/51 coords, api_time=16.9s
2026-08-10 13:01:08,986 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=649343, prompt_len=821
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：", "住院号：", "肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、", "皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。", "辅助检查", "暂无。", "初步诊断", "1.哮喘（急性发作）", "2.慢性支气管炎", "住院医师：王贝贝", "主治医师：陈文宁", "主任医师：已签字"]

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
2026-08-10 13:01:15,876 INFO     29 [qwen-vl-text] coord API raw response (len=911):
[
	{"text": "民权县人民医院", "bbox": [407, 44, 592, 63]},
	{"text": "入院记录", "bbox": [420, 78, 568, 97]},
	{"text": "姓名：", "bbox": [119, 117, 165, 131]},
	{"text": "科室：呼吸二病区", "bbox": [282, 115, 445, 130]},
	{"text": "床号：", "bbox": [543, 115, 591, 130]},
	{"text": "住院号：", "bbox": [702, 115, 770, 130]},
	{"text": "肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、", "bbox": [123, 156, 890, 173]},
	{"text": "皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。", "bbox": [112, 183, 568, 200]},
	{"text": "辅助检查", "bbox": [436, 212, 548, 227]},
	{"text": "暂无。", "bbox": [131, 240, 178, 255]},
	{"text": "初步诊断", "bbox": [436, 268, 548, 284]},
	{"text": "1.哮喘（急性发作）", "bbox": [495, 296, 668, 312]},
	{"text": "2.慢性支气管炎", "bbox": [513, 325, 657, 340]},
	{"text": "住院医师：王贝贝", "bbox": [695, 350, 874, 374]},
	{"text": "主治医师：陈文宁", "bbox": [695, 388, 874, 413]},
	{"text": "主任医师：已签字", "bbox": [695, 425, 871, 452]},
	{"text": "第3页", "bbox": [460, 936, 522, 950]}
]
2026-08-10 13:01:15,876 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=6.9s
2026-08-10 13:01:15,876 INFO     29 [qwen-vl-text] coord item[0]: text=民权县人民医院, bbox=[407, 44, 592, 63]
2026-08-10 13:01:15,876 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[420, 78, 568, 97]
2026-08-10 13:01:15,876 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[119, 117, 165, 131]
2026-08-10 13:01:15,876 INFO     29 [qwen-vl-text] coord item[3]: text=科室：呼吸二病区, bbox=[282, 115, 445, 130]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[4]: text=床号：, bbox=[543, 115, 591, 130]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[702, 115, 770, 130]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[6]: text=肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、, bbox=[123, 156, 890, 173]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[7]: text=皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。, bbox=[112, 183, 568, 200]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[8]: text=辅助检查, bbox=[436, 212, 548, 227]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[9]: text=暂无。, bbox=[131, 240, 178, 255]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[10]: text=初步诊断, bbox=[436, 268, 548, 284]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[11]: text=1.哮喘（急性发作）, bbox=[495, 296, 668, 312]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[12]: text=2.慢性支气管炎, bbox=[513, 325, 657, 340]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[13]: text=住院医师：王贝贝, bbox=[695, 350, 874, 374]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[14]: text=主治医师：陈文宁, bbox=[695, 388, 874, 413]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[15]: text=主任医师：已签字, bbox=[695, 425, 871, 452]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] coord item[16]: text=第3页, bbox=[460, 936, 522, 950]
2026-08-10 13:01:15,877 INFO     29 [qwen-vl-text] page=2 — 16/16 coords, api_time=6.9s
2026-08-10 13:01:15,878 INFO     29 [qwen-vl-text] new_positions (101):
[[0, 242.76, 353.43, 37.89, 54.73], [0, 251.08999999999997, 339.745, 66.518, 83.358], [0, 71.39999999999999, 99.365, 101.88199999999999, 115.354], [0, 169.575, 267.75, 98.514, 112.828], [0, 325.465, 380.79999999999995, 95.988, 109.46], [0, 418.88, 459.935, 95.146, 107.776], [0, 262.99, 329.63, 132.194, 145.666], [0, 96.39, 361.16499999999996, 154.928, 171.768], [0, 97.58, 527.765, 174.29399999999998, 197.87], [0, 69.615, 208.25, 204.606, 221.446], [0, 97.58, 520.625, 219.762, 244.17999999999998], [0, 70.80499999999999, 417.69, 246.706, 268.598], [0, 98.175, 274.295, 274.492, 291.332], [0, 98.77, 528.36, 293.01599999999996, 314.908], [0, 71.39999999999999, 527.765, 316.592, 338.484], [0, 72.59, 531.3349999999999, 340.168, 362.06], [0, 73.185, 174.92999999999998, 371.322, 385.63599999999997], [0, 101.14999999999999, 525.98, 387.32, 409.212], [0, 74.375, 525.98, 410.054, 431.94599999999997], [0, 73.78, 91.63, 442.05, 454.68], [0, 102.33999999999999, 532.525, 454.68, 478.256], [0, 74.375, 330.22499999999997, 483.308, 501.832], [0, 102.935, 528.9549999999999, 502.674, 524.566], [0, 74.97, 298.69, 530.46, 548.984], [0, 103.53, 529.55, 549.826, 571.718], [0, 75.565, 222.53, 579.2959999999999, 595.294], [0, 103.53, 522.41, 596.136, 618.028], [0, 76.16, 371.28, 623.0799999999999, 641.6039999999999], [0, 104.125, 530.74, 642.446, 665.18], [0, 77.35, 129.11499999999998, 675.284, 688.756], [0, 104.72, 204.08499999999998, 698.018, 713.174], [0, 105.315, 195.16, 721.5939999999999, 735.066], [0, 271.91499999999996, 337.365, 742.644, 756.958], [0, 287.385, 323.085, 785.586, 796.5319999999999], [1, 242.165, 352.835, 40.416, 58.098], [1, 250.49499999999998, 339.15, 71.57, 88.41], [1, 71.39999999999999, 99.365, 102.72399999999999, 116.196], [1, 169.575, 266.56, 102.72399999999999, 116.196], [1, 324.275, 379.015, 102.72399999999999, 115.354], [1, 417.69, 458.15, 101.88199999999999, 115.354], [1, 69.615, 165.41, 138.93, 152.402], [1, 196.35, 262.99, 138.93, 152.402], [1, 349.265, 411.74, 138.088, 151.56], [1, 69.615, 135.065, 159.98, 173.452], [1, 196.35, 245.73499999999999, 159.98, 173.452], [1, 270.72499999999997, 330.22499999999997, 159.98, 173.452], [1, 349.85999999999996, 505.75, 159.138, 171.768], [1, 69.615, 129.11499999999998, 181.03, 194.50199999999998], [1, 196.35, 258.22999999999996, 180.188, 194.50199999999998], [1, 270.72499999999997, 331.41499999999996, 180.188, 194.50199999999998], [1, 349.85999999999996, 505.75, 179.346, 192.81799999999998], [1, 69.615, 174.92999999999998, 202.07999999999998, 215.552], [1, 258.22999999999996, 330.22499999999997, 201.238, 214.70999999999998], [1, 349.85999999999996, 478.38, 200.396, 213.868], [1, 69.615, 296.31, 223.13, 236.602], [1, 302.85499999999996, 398.65, 229.86599999999999, 244.17999999999998], [1, 426.615, 521.22, 221.446, 234.91799999999998], [1, 69.615, 93.41499999999999, 239.97, 253.44199999999998], [1, 426.615, 438.515, 237.444, 250.916], [1, 69.615, 136.255, 260.178, 273.65], [1, 302.85499999999996, 472.43, 259.336, 272.808], [1, 69.615, 141.60999999999999, 282.07, 295.542], [1, 198.73, 282.625, 282.07, 295.542], [1, 368.305, 508.72499999999997, 281.228, 294.7], [1, 99.365, 342.125, 304.804, 318.276], [1, 69.615, 525.98, 327.538, 341.01], [1, 69.615, 521.22, 373.848, 387.32], [1, 69.615, 521.22, 395.74, 409.212], [1, 69.615, 525.98, 417.632, 431.104], [1, 71.39999999999999, 280.84, 465.626, 479.09799999999996], [1, 99.365, 523.6, 488.35999999999996, 501.832], [1, 71.39999999999999, 441.48999999999995, 511.936, 525.408], [1, 99.365, 524.79, 535.512, 548.984], [1, 71.39999999999999, 524.79, 559.088, 572.56], [1, 71.39999999999999, 235.02499999999998, 582.664, 596.136], [1, 99.365, 267.155, 606.24, 619.712], [1, 99.365, 165.41, 636.552, 650.024], [1, 190.39999999999998, 201.10999999999999, 639.92, 651.708], [1, 203.48999999999998, 219.55499999999998, 637.394, 648.34], [1, 198.73, 224.315, 648.34, 658.444], [1, 240.38, 530.145, 634.8679999999999, 648.34], [1, 72.59, 114.24, 677.81, 691.2819999999999], [1, 96.39, 527.17, 700.544, 714.016], [1, 72.59, 102.935, 724.12, 737.592], [1, 282.625, 319.515, 787.27, 798.216], [2, 242.165, 352.24, 37.048, 53.046], [2, 249.89999999999998, 337.96, 65.676, 81.67399999999999], [2, 70.80499999999999, 98.175, 98.514, 110.30199999999999], [2, 167.79, 264.775, 96.83, 109.46], [2, 323.085, 351.645, 96.83, 109.46], [2, 417.69, 458.15, 96.83, 109.46], [2, 73.185, 529.55, 131.352, 145.666], [2, 66.64, 337.96, 154.08599999999998, 168.4], [2, 259.42, 326.06, 178.504, 191.134], [2, 77.945, 105.91, 202.07999999999998, 214.70999999999998], [2, 259.42, 326.06, 225.656, 239.128], [2, 294.525, 397.46, 249.232, 262.704], [2, 305.235, 390.91499999999996, 273.65, 286.28], [2, 413.525, 520.03, 294.7, 314.908], [2, 413.525, 520.03, 326.69599999999997, 347.746], [2, 413.525, 518.245, 357.84999999999997, 380.584]]
2026-08-10 13:01:15,878 INFO     29 [qwen-vl-text] ═══ DONE ═══ 101 positions, pages=3, time=46.5s
2026-08-10 13:01:15,900 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:01:15,901 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:01:15,901 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:01:15,902 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:01:15.901+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 36, "failed": 0, "current": {"60a23a7a94bb11f1bd9827cf206dfa2d": {"id": "60a23a7a94bb11f1bd9827cf206dfa2d", "doc_id": "6067e0fa94bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366792626, "task_type": "dataflow", "root_trace_id": "94d1339f4db64958b3764c87ea29c5c0", "root_traceparent": "00-94d1339f4db64958b3764c87ea29c5c0-51b0d67fb5a77038-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:01:15,910 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:01:15,911 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:01:15,911 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:01:15,911 INFO     29 [qwen-vl-text] positions(126): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:01:15,911 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [126]
2026-08-10 13:01:16,090 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:01:16,091 INFO     29 [qwen-vl-text] LLM extraction start, text_len=766
2026-08-10 13:01:16,091 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:01:16,092 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 102, \"bbox_end\": 227, \"encounter_dates\": [\"2023-08-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "民权县人民医院\n肺功能检查报告\n病人ID:\n2023-08-1501\n性别：\n女\n高度：\n158 cm\n名：\n出生日期：\n1957/7/2\n体重：\n60 kg\n姓：\n年龄：\n66 years\nBMI：\n24.0 kg/m²\n体积\n流量\n体积\n时间[s]\n时间[s]\n单位\n预测值\n之前\n%预值\n沙丁胺醇\n(400\n%预值\n%变化\nug)\nVC\nI\n(1)\n2.37\n1.66\n70%\n2.20\n93%\n+32.2%\nVC\nI\n(1)\n2.37\n1.66\n70%\n2.20\n93%\n+32.2%\nFEV1\nI\n(1)\n1.99\n0.88\n44%\n1.27\n64%\n+44.4%\nFEV1/FVC\n%\n(1)\n77\n53\n69%\n58\n75%\n+9.3%\nFEV1/VC\n%\n(1)\n77\n53\n69%\n58\n75%\n+9.3%\nPEF\nl/s\n(1)\n5.60\n2.06\n37%\n2.74\n49%\n+32.9%\nMEF75\nl/s\n(1)\n5.04\n0.97\n19%\n1.53\n30%\n+57.6%\nMEF50\nl/s\n(1)\n3.38\n0.49\n14%\n0.78\n23%\n+60.6%\nMEF25\nl/s\n(1)\n1.12\n0.22\n19%\n0.29\n26%\n+35.4%\n诊断意见：\n1.重度混合型通气功能障碍，小气道功能减低。\n2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。\n3.MVV:44%。建议定期复查。\n(1): ECCS 1993\n-1-\nBTPS: 21.0 °C, 1013 hPa,\n检测: 2023/8/15\n50%\n医生:-\nGeratherm Respiratory GmbH\nwww.geratherm-respiratory.com\nBlue Cherry V1.2.2.24",
    "role": "user"
  }
]
2026-08-10 13:01:21,910 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:01:21,911 INFO     29 [qwen-vl-text] LLM output (len=1021):
{
  "exam_date": "2023-08-15",
  "report_date": "2023-08-15",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | 单位 | 预测值 | 之前 | %预值 | 沙丁胺醇 (400ug) | %预值 | %变化 |\n|---|---|---|---|---|---|---|---|\n| VC I (1) | | 2.37 | 1.66 | 70% | 2.20 | 93% | +32.2% |\n| VC I (1) | | 2.37 | 1.66 | 70% | 2.20 | 93% | +32.2% |\n| FEV1 I (1) | | 1.99 | 0.88 | 44% | 1.27 | 64% | +44.4% |\n| FEV1/FVC % (1) | | 77 | 53 | 69% | 58 | 75% | +9.3% |\n| FEV1/VC % (1) | | 77 | 53 | 69% | 58 | 75% | +9.3% |\n| PEF l/s (1) | | 5.60 | 2.06 | 37% | 2.74 | 49% | +32.9% |\n| MEF75 l/s (1) | | 5.04 | 0.97 | 19% | 1.53 | 30% | +57.6% |\n| MEF50 l/s (1) | | 3.38 | 0.49 | 14% | 0.78 | 23% | +60.6% |\n| MEF25 l/s (1) | | 1.12 | 0.22 | 19% | 0.29 | 26% | +35.4% |",
  "conclusion": "诊断意见：\n1.重度混合型通气功能障碍，小气道功能减低。\n2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。\n3.MVV:44%。建议定期复查。",
  "physician": null,
  "reviewer": null
}
2026-08-10 13:01:21,918 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2160017, prompt_len=1758
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共126行）
["民权县人民医院", "肺功能检查报告", "病人ID:", "2023-08-1501", "性别：", "女", "高度：", "158 cm", "名：", "出生日期：", "1957/7/2", "体重：", "60 kg", "姓：", "年龄：", "66 years", "BMI：", "24.0 kg/m²", "体积", "流量", "体积", "时间[s]", "时间[s]", "单位", "预测值", "之前", "%预值", "沙丁胺醇", "(400", "%预值", "%变化", "ug)", "VC", "I", "(1)", "2.37", "1.66", "70%", "2.20", "93%", "+32.2%", "VC", "I", "(1)", "2.37", "1.66", "70%", "2.20", "93%", "+32.2%", "FEV1", "I", "(1)", "1.99", "0.88", "44%", "1.27", "64%", "+44.4%", "FEV1/FVC", "%", "(1)", "77", "53", "69%", "58", "75%", "+9.3%", "FEV1/VC", "%", "(1)", "77", "53", "69%", "58", "75%", "+9.3%", "PEF", "l/s", "(1)", "5.60", "2.06", "37%", "2.74", "49%", "+32.9%", "MEF75", "l/s", "(1)", "5.04", "0.97", "19%", "1.53", "30%", "+57.6%", "MEF50", "l/s", "(1)", "3.38", "0.49", "14%", "0.78", "23%", "+60.6%", "MEF25", "l/s", "(1)", "1.12", "0.22", "19%", "0.29", "26%", "+35.4%", "诊断意见：", "1.重度混合型通气功能障碍，小气道功能减低。", "2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。", "3.MVV:44%。建议定期复查。", "(1): ECCS 1993", "-1-", "BTPS: 21.0 °C, 1013 hPa,", "检测: 2023/8/15", "50%", "医生:-", "Geratherm Respiratory GmbH", "www.geratherm-respiratory.com", "Blue Cherry V1.2.2.24"]

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
2026-08-10 13:02:25,230 INFO     29 [qwen-vl-text] coord API raw response (len=11603):
[
	{"text": "民权县人民医院", "bbox": [418, 98, 591, 113]},
	{"text": "肺功能检查报告", "bbox": [458, 120, 557, 132]},
	{"text": "病人ID:", "bbox": [100, 166, 146, 176], "bbox_2d": [100, 166, 146, 176]},
	{"text": "2023-08-1501", "bbox": [234, 171, 304, 180], "bbox_2d": [234, 171, 304, 180]},
	{"text": "性别：", "bbox": [369, 171, 398, 180], "bbox_2d": [369, 171, 398, 180]},
	{"text": "女", "bbox": [502, 173, 514, 181], "bbox_2d": [502, 173, 514, 181]},
	{"text": "高度：", "bbox": [634, 172, 662, 181], "bbox_2d": [634, 172, 662, 181]},
	{"text": "158 cm", "bbox": [767, 175, 800, 184], "bbox_2d": [767, 175, 800, 184]},
	{"text": "名：", "bbox": [100, 177, 117, 186], "bbox_2d": [100, 177, 117, 186]},
	{"text": "出生日期：", "bbox": [369, 181, 418, 190], "bbox_2d": [369, 181, 418, 190]},
	{"text": "1957/7/2", "bbox": [502, 183, 545, 192], "bbox_2d": [502, 183, 545, 192]},
	{"text": "体重：", "bbox": [634, 182, 662, 191], "bbox_2d": [634, 182, 662, 191]},
	{"text": "60 kg", "bbox": [767, 185, 796, 194], "bbox_2d": [767, 185, 796, 194]},
	{"text": "姓：", "bbox": [100, 187, 117, 196], "bbox_2d": [100, 187, 117, 196]},
	{"text": "年龄：", "bbox": [369, 191, 398, 200], "bbox_2d": [369, 191, 398, 200]},
	{"text": "66 years", "bbox": [502, 193, 545, 202], "bbox_2d": [502, 193, 545, 202]},
	{"text": "BMI：", "bbox": [634, 193, 657, 201], "bbox_2d": [634, 193, 657, 201]},
	{"text": "24.0 kg/m²", "bbox": [767, 195, 820, 204], "bbox_2d": [767, 195, 820, 204]},
	{"text": "体积", "bbox": [94, 223, 107, 234], "bbox_2d": [94, 223, 107, 234]},
	{"text": "0.0", "bbox": [107, 223, 120, 230], "bbox_2d": [107, 223, 120, 230]},
	{"text": "三", "bbox": [92, 241, 104, 250], "bbox_2d": [92, 241, 104, 250]},
	{"text": "流量", "bbox": [324, 231, 337, 262], "bbox_2d": [324, 231, 337, 262]},
	{"text": "6", "bbox": [341, 231, 348, 237], "bbox_2d": [341, 231, 348, 237]},
	{"text": "体积", "bbox": [643, 228, 657, 240], "bbox_2d": [643, 228, 657, 240]},
	{"text": "0", "bbox": [657, 228, 664, 234], "bbox_2d": [657, 228, 664, 234]},
	{"text": "三", "bbox": [642, 245, 655, 254], "bbox_2d": [642, 245, 655, 254]},
	{"text": "1.0", "bbox": [106, 276, 117, 283], "bbox_2d": [106, 276, 117, 283]},
	{"text": "4", "bbox": [340, 275, 347, 282], "bbox_2d": [340, 275, 347, 282]},
	{"text": "2.0", "bbox": [105, 334, 117, 341], "bbox_2d": [105, 334, 117, 341]},
	{"text": "2", "bbox": [340, 324, 347, 331], "bbox_2d": [340, 324, 347, 331]},
	{"text": "2", "bbox": [655, 316, 662, 323], "bbox_2d": [655, 316, 662, 323]},
	{"text": "3", "bbox": [655, 360, 662, 367], "bbox_2d": [655, 360, 662, 367]},
	{"text": "0", "bbox": [340, 372, 347, 379], "bbox_2d": [340, 372, 347, 379]},
	{"text": "1.0", "bbox": [420, 385, 432, 392], "bbox_2d": [420, 385, 432, 392]},
	{"text": "2.0", "bbox": [485, 385, 498, 392], "bbox_2d": [485, 385, 498, 392]},
	{"text": "3.0", "bbox": [553, 385, 565, 392], "bbox_2d": [553, 385, 565, 392]},
	{"text": "4.0", "bbox": [620, 385, 632, 392], "bbox_2d": [620, 385, 632, 392]},
	{"text": "体积[l]", "bbox": [595, 392, 633, 403], "bbox_2d": [595, 392, 633, 403]},
	{"text": "3.0", "bbox": [104, 389, 117, 396], "bbox_2d": [104, 389, 117, 396]},
	{"text": "4", "bbox": [655, 405, 662, 412], "bbox_2d": [655, 405, 662, 412]},
	{"text": "-2", "bbox": [337, 418, 348, 425], "bbox_2d": [337, 418, 348, 425]},
	{"text": "4.0", "bbox": [104, 446, 117, 453], "bbox_2d": [104, 446, 117, 453]},
	{"text": "0", "bbox": [128, 459, 135, 466], "bbox_2d": [128, 459, 135, 466]},
	{"text": "15", "bbox": [182, 459, 192, 466], "bbox_2d": [182, 459, 192, 466]},
	{"text": "30", "bbox": [239, 459, 250, 466], "bbox_2d": [239, 459, 250, 466]},
	{"text": "45", "bbox": [296, 459, 307, 466], "bbox_2d": [296, 459, 307, 466]},
	{"text": "5", "bbox": [653, 450, 659, 457], "bbox_2d": [653, 450, 659, 457]},
	{"text": "0", "bbox": [669, 462, 675, 469], "bbox_2d": [669, 462, 675, 469]},
	{"text": "5", "bbox": [724, 462, 730, 469], "bbox_2d": [724, 462, 730, 469]},
	{"text": "10", "bbox": [780, 462, 788, 469], "bbox_2d": [780, 462, 788, 469]},
	{"text": "15", "bbox": [836, 462, 844, 469], "bbox_2d": [836, 462, 844, 469]},
	{"text": "20", "bbox": [889, 462, 898, 469], "bbox_2d": [889, 462, 898, 469]},
	{"text": "时间[s]", "bbox": [265, 467, 307, 477], "bbox_2d": [265, 467, 307, 477]},
	{"text": "时间[s]", "bbox": [858, 470, 898, 480], "bbox_2d": [858, 470, 898, 480]},
	{"text": "单位", "bbox": [251, 512, 294, 527], "bbox_2d": [251, 512, 294, 527]},
	{"text": "预测值", "bbox": [335, 512, 397, 527], "bbox_2d": [335, 512, 397, 527]},
	{"text": "之前", "bbox": [420, 512, 461, 527], "bbox_2d": [420, 512, 461, 527]},
	{"text": "%预值", "bbox": [474, 512, 534, 527], "bbox_2d": [474, 512, 534, 527]},
	{"text": "沙丁胺醇", "bbox": [554, 499, 638, 514], "bbox_2d": [554, 499, 638, 514]},
	{"text": "(400", "bbox": [600, 515, 638, 530], "bbox_2d": [600, 515, 638, 530]},
	{"text": "%预值", "bbox": [653, 515, 714, 530], "bbox_2d": [653, 515, 714, 530]},
	{"text": "%变化", "bbox": [735, 515, 796, 530], "bbox_2d": [735, 515, 796, 530]},
	{"text": "ug)", "bbox": [609, 532, 638, 547], "bbox_2d": [609, 532, 638, 547]},
	{"text": "VC", "bbox": [204, 551, 232, 564], "bbox_2d": [204, 551, 232, 564]},
	{"text": "I", "bbox": [264, 551, 271, 564], "bbox_2d": [264, 551, 271, 564]},
	{"text": "(1)", "bbox": [300, 547, 315, 558], "bbox_2d": [300, 547, 315, 558]},
	{"text": "2.37", "bbox": [364, 551, 399, 564], "bbox_2d": [364, 551, 399, 564]},
	{"text": "1.66", "bbox": [429, 551, 464, 564], "bbox_2d": [429, 551, 464, 564]},
	{"text": "70%", "bbox": [502, 551, 536, 564], "bbox_2d": [502, 551, 536, 564]},
	{"text": "2.20", "bbox": [604, 551, 640, 564], "bbox_2d": [604, 551, 640, 564]},
	{"text": "93%", "bbox": [680, 551, 715, 564], "bbox_2d": [680, 551, 715, 564]},
	{"text": "+32.2%", "bbox": [737, 551, 797, 564], "bbox_2d": [737, 551, 797, 564]},
	{"text": "VC", "bbox": [204, 573, 232, 586], "bbox_2d": [204, 573, 232, 586]},
	{"text": "I", "bbox": [264, 573, 271, 586], "bbox_2d": [264, 573, 271, 586]},
	{"text": "(1)", "bbox": [300, 569, 315, 580], "bbox_2d": [300, 569, 315, 580]},
	{"text": "2.37", "bbox": [364, 573, 399, 586], "bbox_2d": [364, 573, 399, 586]},
	{"text": "1.66", "bbox": [429, 573, 464, 586], "bbox_2d": [429, 573, 464, 586]},
	{"text": "70%", "bbox": [502, 573, 536, 586], "bbox_2d": [502, 573, 536, 586]},
	{"text": "2.20", "bbox": [604, 573, 640, 586], "bbox_2d": [604, 573, 640, 586]},
	{"text": "93%", "bbox": [680, 573, 715, 586], "bbox_2d": [680, 573, 715, 586]},
	{"text": "+32.2%", "bbox": [737, 573, 797, 586], "bbox_2d": [737, 573, 797, 586]},
	{"text": "FEV1", "bbox": [181, 595, 229, 609], "bbox_2d": [181, 595, 229, 609]},
	{"text": "I", "bbox": [264, 595, 271, 609], "bbox_2d": [264, 595, 271, 609]},
	{"text": "(1)", "bbox": [300, 591, 315, 603], "bbox_2d": [300, 591, 315, 603]},
	{"text": "1.99", "bbox": [364, 595, 399, 609], "bbox_2d": [364, 595, 399, 609]},
	{"text": "0.88", "bbox": [426, 595, 463, 609], "bbox_2d": [426, 595, 463, 609]},
	{"text": "44%", "bbox": [502, 595, 536, 609], "bbox_2d": [502, 595, 536, 609]},
	{"text": "5", "bbox": [538, 584, 565, 608], "bbox_2d": [538, 584, 565, 608]},
	{"text": "1.27", "bbox": [606, 595, 642, 609], "bbox_2d": [606, 595, 642, 609]},
	{"text": "64%", "bbox": [680, 595, 715, 609], "bbox_2d": [680, 595, 715, 609]},
	{"text": "+44.4%", "bbox": [737, 595, 797, 609], "bbox_2d": [737, 595, 797, 609]},
	{"text": "FEV1/FVC", "bbox": [138, 618, 230, 632], "bbox_2d": [138, 618, 230, 632]},
	{"text": "%", "bbox": [257, 618, 274, 632], "bbox_2d": [257, 618, 274, 632]},
	{"text": "(1)", "bbox": [298, 614, 313, 625], "bbox_2d": [298, 614, 313, 625]},
	{"text": "77", "bbox": [377, 618, 398, 632], "bbox_2d": [377, 618, 398, 632]},
	{"text": "53", "bbox": [442, 618, 463, 632], "bbox_2d": [442, 618, 463, 632]},
	{"text": "69%", "bbox": [502, 618, 536, 632], "bbox_2d": [502, 618, 536, 632]},
	{"text": "58", "bbox": [620, 618, 642, 632], "bbox_2d": [620, 618, 642, 632]},
	{"text": "75%", "bbox": [680, 618, 715, 632], "bbox_2d": [680, 618, 715, 632]},
	{"text": "+9.3%", "bbox": [747, 618, 797, 632], "bbox_2d": [747, 618, 797, 632]},
	{"text": "FEV1/VC", "bbox": [150, 641, 230, 655], "bbox_2d": [150, 641, 230, 655]},
	{"text": "%", "bbox": [257, 641, 274, 655], "bbox_2d": [257, 641, 274, 655]},
	{"text": "(1)", "bbox": [298, 637, 313, 648], "bbox_2d": [298, 637, 313, 648]},
	{"text": "77", "bbox": [377, 641, 398, 655], "bbox_2d": [377, 641, 398, 655]},
	{"text": "53", "bbox": [442, 641, 463, 655], "bbox_2d": [442, 641, 463, 655]},
	{"text": "69%", "bbox": [502, 641, 536, 655], "bbox_2d": [502, 641, 536, 655]},
	{"text": "58", "bbox": [620, 641, 642, 655], "bbox_2d": [620, 641, 642, 655]},
	{"text": "75%", "bbox": [680, 641, 715, 655], "bbox_2d": [680, 641, 715, 655]},
	{"text": "+9.3%", "bbox": [747, 641, 797, 655], "bbox_2d": [747, 641, 797, 655]},
	{"text": "PEF", "bbox": [192, 664, 230, 677], "bbox_2d": [192, 664, 230, 677]},
	{"text": "l/s", "bbox": [257, 664, 276, 677], "bbox_2d": [257, 664, 276, 677]},
	{"text": "(1)", "bbox": [298, 660, 313, 671], "bbox_2d": [298, 660, 313, 671]},
	{"text": "5.60", "bbox": [362, 664, 398, 677], "bbox_2d": [362, 664, 398, 677]},
	{"text": "2.06", "bbox": [425, 664, 463, 677], "bbox_2d": [425, 664, 463, 677]},
	{"text": "37%", "bbox": [502, 664, 536, 677], "bbox_2d": [502, 664, 536, 677]},
	{"text": "2.74", "bbox": [604, 664, 642, 677], "bbox_2d": [604, 664, 642, 677]},
	{"text": "49%", "bbox": [680, 664, 715, 677], "bbox_2d": [680, 664, 715, 677]},
	{"text": "+32.9%", "bbox": [737, 664, 797, 677], "bbox_2d": [737, 664, 797, 677]},
	{"text": "MEF75", "bbox": [168, 686, 230, 700], "bbox_2d": [168, 686, 230, 700]},
	{"text": "l/s", "bbox": [257, 686, 276, 700], "bbox_2d": [257, 686, 276, 700]},
	{"text": "(1)", "bbox": [298, 682, 313, 693], "bbox_2d": [298, 682, 313, 693]},
	{"text": "5.04", "bbox": [362, 686, 398, 700], "bbox_2d": [362, 686, 398, 700]},
	{"text": "0.97", "bbox": [425, 686, 463, 700], "bbox_2d": [425, 686, 463, 700]},
	{"text": "19%", "bbox": [502, 686, 536, 700], "bbox_2d": [502, 686, 536, 700]},
	{"text": "1.53", "bbox": [606, 686, 642, 700], "bbox_2d": [606, 686, 642, 700]},
	{"text": "30%", "bbox": [680, 686, 715, 700], "bbox_2d": [680, 686, 715, 700]},
	{"text": "+57.6%", "bbox": [737, 686, 797, 700], "bbox_2d": [737, 686, 797, 700]},
	{"text": "MEF50", "bbox": [167, 709, 230, 723], "bbox_2d": [167, 709, 230, 723]},
	{"text": "l/s", "bbox": [257, 709, 276, 723], "bbox_2d": [257, 709, 276, 723]},
	{"text": "(1)", "bbox": [298, 705, 313, 716], "bbox_2d": [298, 705, 313, 716]},
	{"text": "3.38", "bbox": [362, 709, 398, 723], "bbox_2d": [362, 709, 398, 723]},
	{"text": "0.49", "bbox": [425, 709, 463, 723], "bbox_2d": [425, 709, 463, 723]},
	{"text": "14%", "bbox": [502, 709, 536, 723], "bbox_2d": [502, 709, 536, 723]},
	{"text": "0.78", "bbox": [604, 709, 642, 723], "bbox_2d": [604, 709, 642, 723]},
	{"text": "23%", "bbox": [680, 709, 715, 723], "bbox_2d": [680, 709, 715, 723]},
	{"text": "+60.6%", "bbox": [737, 709, 797, 723], "bbox_2d": [737, 709, 797, 723]},
	{"text": "MEF25", "bbox": [165, 732, 230, 746], "bbox_2d": [165, 732, 230, 746]},
	{"text": "l/s", "bbox": [257, 732, 276, 746], "bbox_2d": [257, 732, 276, 746]},
	{"text": "(1)", "bbox": [298, 728, 313, 739], "bbox_2d": [298, 728, 313, 739]},
	{"text": "1.12", "bbox": [362, 732, 398, 746], "bbox_2d": [362, 732, 398, 746]},
	{"text": "0.22", "bbox": [425, 732, 463, 746], "bbox_2d": [425, 732, 463, 746]},
	{"text": "19%", "bbox": [502, 732, 536, 746], "bbox_2d": [502, 732, 536, 746]},
	{"text": "0.29", "bbox": [604, 732, 642, 746], "bbox_2d": [604, 732, 642, 746]},
	{"text": "26%", "bbox": [680, 732, 715, 7
2026-08-10 13:02:25,231 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord API: raw_items=144, valid_items=144, elapsed=63.3s
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[0]: text=民权县人民医院, bbox=[418, 98, 591, 113]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[458, 120, 557, 132]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID:, bbox=[100, 166, 146, 176]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[3]: text=2023-08-1501, bbox=[234, 171, 304, 180]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[4]: text=性别：, bbox=[369, 171, 398, 180]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[5]: text=女, bbox=[502, 173, 514, 181]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[6]: text=高度：, bbox=[634, 172, 662, 181]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[7]: text=158 cm, bbox=[767, 175, 800, 184]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[8]: text=名：, bbox=[100, 177, 117, 186]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[9]: text=出生日期：, bbox=[369, 181, 418, 190]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[10]: text=1957/7/2, bbox=[502, 183, 545, 192]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[11]: text=体重：, bbox=[634, 182, 662, 191]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[12]: text=60 kg, bbox=[767, 185, 796, 194]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[13]: text=姓：, bbox=[100, 187, 117, 196]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[14]: text=年龄：, bbox=[369, 191, 398, 200]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[15]: text=66 years, bbox=[502, 193, 545, 202]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[16]: text=BMI：, bbox=[634, 193, 657, 201]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[17]: text=24.0 kg/m², bbox=[767, 195, 820, 204]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[18]: text=体积, bbox=[94, 223, 107, 234]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[19]: text=0.0, bbox=[107, 223, 120, 230]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[20]: text=三, bbox=[92, 241, 104, 250]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[21]: text=流量, bbox=[324, 231, 337, 262]
2026-08-10 13:02:25,234 INFO     29 [qwen-vl-text] coord item[22]: text=6, bbox=[341, 231, 348, 237]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[23]: text=体积, bbox=[643, 228, 657, 240]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[24]: text=0, bbox=[657, 228, 664, 234]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[25]: text=三, bbox=[642, 245, 655, 254]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[26]: text=1.0, bbox=[106, 276, 117, 283]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[27]: text=4, bbox=[340, 275, 347, 282]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[28]: text=2.0, bbox=[105, 334, 117, 341]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[29]: text=2, bbox=[340, 324, 347, 331]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[30]: text=2, bbox=[655, 316, 662, 323]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[31]: text=3, bbox=[655, 360, 662, 367]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[32]: text=0, bbox=[340, 372, 347, 379]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[33]: text=1.0, bbox=[420, 385, 432, 392]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[34]: text=2.0, bbox=[485, 385, 498, 392]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[35]: text=3.0, bbox=[553, 385, 565, 392]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[36]: text=4.0, bbox=[620, 385, 632, 392]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[37]: text=体积[l], bbox=[595, 392, 633, 403]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[38]: text=3.0, bbox=[104, 389, 117, 396]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[39]: text=4, bbox=[655, 405, 662, 412]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[40]: text=-2, bbox=[337, 418, 348, 425]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[41]: text=4.0, bbox=[104, 446, 117, 453]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[42]: text=0, bbox=[128, 459, 135, 466]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[43]: text=15, bbox=[182, 459, 192, 466]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[44]: text=30, bbox=[239, 459, 250, 466]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[45]: text=45, bbox=[296, 459, 307, 466]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[46]: text=5, bbox=[653, 450, 659, 457]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[47]: text=0, bbox=[669, 462, 675, 469]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[48]: text=5, bbox=[724, 462, 730, 469]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[49]: text=10, bbox=[780, 462, 788, 469]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[50]: text=15, bbox=[836, 462, 844, 469]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[51]: text=20, bbox=[889, 462, 898, 469]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[52]: text=时间[s], bbox=[265, 467, 307, 477]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[53]: text=时间[s], bbox=[858, 470, 898, 480]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[54]: text=单位, bbox=[251, 512, 294, 527]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[55]: text=预测值, bbox=[335, 512, 397, 527]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[56]: text=之前, bbox=[420, 512, 461, 527]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[57]: text=%预值, bbox=[474, 512, 534, 527]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[58]: text=沙丁胺醇, bbox=[554, 499, 638, 514]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[59]: text=(400, bbox=[600, 515, 638, 530]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[60]: text=%预值, bbox=[653, 515, 714, 530]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[61]: text=%变化, bbox=[735, 515, 796, 530]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[62]: text=ug), bbox=[609, 532, 638, 547]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[63]: text=VC, bbox=[204, 551, 232, 564]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[64]: text=I, bbox=[264, 551, 271, 564]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[65]: text=(1), bbox=[300, 547, 315, 558]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[66]: text=2.37, bbox=[364, 551, 399, 564]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[67]: text=1.66, bbox=[429, 551, 464, 564]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[68]: text=70%, bbox=[502, 551, 536, 564]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[69]: text=2.20, bbox=[604, 551, 640, 564]
2026-08-10 13:02:25,235 INFO     29 [qwen-vl-text] coord item[70]: text=93%, bbox=[680, 551, 715, 564]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[71]: text=+32.2%, bbox=[737, 551, 797, 564]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[72]: text=VC, bbox=[204, 573, 232, 586]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[73]: text=I, bbox=[264, 573, 271, 586]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[74]: text=(1), bbox=[300, 569, 315, 580]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[75]: text=2.37, bbox=[364, 573, 399, 586]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[76]: text=1.66, bbox=[429, 573, 464, 586]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[77]: text=70%, bbox=[502, 573, 536, 586]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[78]: text=2.20, bbox=[604, 573, 640, 586]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[79]: text=93%, bbox=[680, 573, 715, 586]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[80]: text=+32.2%, bbox=[737, 573, 797, 586]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[81]: text=FEV1, bbox=[181, 595, 229, 609]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[82]: text=I, bbox=[264, 595, 271, 609]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[83]: text=(1), bbox=[300, 591, 315, 603]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[84]: text=1.99, bbox=[364, 595, 399, 609]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[85]: text=0.88, bbox=[426, 595, 463, 609]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[86]: text=44%, bbox=[502, 595, 536, 609]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[87]: text=5, bbox=[538, 584, 565, 608]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[88]: text=1.27, bbox=[606, 595, 642, 609]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[89]: text=64%, bbox=[680, 595, 715, 609]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[90]: text=+44.4%, bbox=[737, 595, 797, 609]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[91]: text=FEV1/FVC, bbox=[138, 618, 230, 632]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[92]: text=%, bbox=[257, 618, 274, 632]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[93]: text=(1), bbox=[298, 614, 313, 625]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[94]: text=77, bbox=[377, 618, 398, 632]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[95]: text=53, bbox=[442, 618, 463, 632]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[96]: text=69%, bbox=[502, 618, 536, 632]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[97]: text=58, bbox=[620, 618, 642, 632]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[98]: text=75%, bbox=[680, 618, 715, 632]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[99]: text=+9.3%, bbox=[747, 618, 797, 632]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[100]: text=FEV1/VC, bbox=[150, 641, 230, 655]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[101]: text=%, bbox=[257, 641, 274, 655]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[102]: text=(1), bbox=[298, 637, 313, 648]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[103]: text=77, bbox=[377, 641, 398, 655]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[104]: text=53, bbox=[442, 641, 463, 655]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[105]: text=69%, bbox=[502, 641, 536, 655]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[106]: text=58, bbox=[620, 641, 642, 655]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[107]: text=75%, bbox=[680, 641, 715, 655]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[108]: text=+9.3%, bbox=[747, 641, 797, 655]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[109]: text=PEF, bbox=[192, 664, 230, 677]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[110]: text=l/s, bbox=[257, 664, 276, 677]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[111]: text=(1), bbox=[298, 660, 313, 671]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[112]: text=5.60, bbox=[362, 664, 398, 677]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[113]: text=2.06, bbox=[425, 664, 463, 677]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[114]: text=37%, bbox=[502, 664, 536, 677]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[115]: text=2.74, bbox=[604, 664, 642, 677]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[116]: text=49%, bbox=[680, 664, 715, 677]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[117]: text=+32.9%, bbox=[737, 664, 797, 677]
2026-08-10 13:02:25,236 INFO     29 [qwen-vl-text] coord item[118]: text=MEF75, bbox=[168, 686, 230, 700]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[119]: text=l/s, bbox=[257, 686, 276, 700]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[120]: text=(1), bbox=[298, 682, 313, 693]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[121]: text=5.04, bbox=[362, 686, 398, 700]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[122]: text=0.97, bbox=[425, 686, 463, 700]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[123]: text=19%, bbox=[502, 686, 536, 700]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[124]: text=1.53, bbox=[606, 686, 642, 700]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[125]: text=30%, bbox=[680, 686, 715, 700]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[126]: text=+57.6%, bbox=[737, 686, 797, 700]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[127]: text=MEF50, bbox=[167, 709, 230, 723]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[128]: text=l/s, bbox=[257, 709, 276, 723]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[129]: text=(1), bbox=[298, 705, 313, 716]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[130]: text=3.38, bbox=[362, 709, 398, 723]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[131]: text=0.49, bbox=[425, 709, 463, 723]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[132]: text=14%, bbox=[502, 709, 536, 723]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[133]: text=0.78, bbox=[604, 709, 642, 723]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[134]: text=23%, bbox=[680, 709, 715, 723]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[135]: text=+60.6%, bbox=[737, 709, 797, 723]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[136]: text=MEF25, bbox=[165, 732, 230, 746]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[137]: text=l/s, bbox=[257, 732, 276, 746]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[138]: text=(1), bbox=[298, 728, 313, 739]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[139]: text=1.12, bbox=[362, 732, 398, 746]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[140]: text=0.22, bbox=[425, 732, 463, 746]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[141]: text=19%, bbox=[502, 732, 536, 746]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[142]: text=0.29, bbox=[604, 732, 642, 746]
2026-08-10 13:02:25,237 INFO     29 [qwen-vl-text] coord item[143]: text=26%, bbox=[680, 732, 715, 7]
2026-08-10 13:02:25,238 INFO     29 [qwen-vl-text] page=3 — 126/126 coords, api_time=63.3s
2026-08-10 13:02:25,238 INFO     29 [qwen-vl-text] new_positions (126):
[[3, 248.70999999999998, 351.645, 82.51599999999999, 95.146], [3, 272.51, 331.41499999999996, 101.03999999999999, 111.14399999999999], [3, 59.5, 86.86999999999999, 139.772, 148.192], [3, 139.23, 180.88, 143.982, 151.56], [3, 219.55499999999998, 236.81, 143.982, 151.56], [3, 298.69, 305.83, 145.666, 152.402], [3, 377.22999999999996, 393.89, 144.82399999999998, 152.402], [3, 456.36499999999995, 476.0, 147.35, 154.928], [3, 59.5, 69.615, 149.034, 156.612], [3, 219.55499999999998, 248.70999999999998, 152.402, 159.98], [3, 298.69, 324.275, 154.08599999999998, 161.664], [3, 377.22999999999996, 393.89, 153.244, 160.822], [3, 456.36499999999995, 473.62, 155.76999999999998, 163.34799999999998], [3, 59.5, 69.615, 157.454, 165.03199999999998], [3, 219.55499999999998, 236.81, 160.822, 168.4], [3, 298.69, 324.275, 162.506, 170.084], [3, 377.22999999999996, 390.91499999999996, 162.506, 169.242], [3, 456.36499999999995, 487.9, 164.19, 171.768], [3, 55.93, 63.665, 187.766, 197.028], [3, 63.665, 71.39999999999999, 187.766, 193.66], [3, 54.739999999999995, 61.879999999999995, 202.922, 210.5], [3, 192.78, 200.515, 194.50199999999998, 220.60399999999998], [3, 202.89499999999998, 207.06, 194.50199999999998, 199.554], [3, 382.585, 390.91499999999996, 191.976, 202.07999999999998], [3, 390.91499999999996, 395.08, 191.976, 197.028], [3, 381.99, 389.72499999999997, 206.29, 213.868], [3, 63.07, 69.615, 232.392, 238.286], [3, 202.29999999999998, 206.465, 231.54999999999998, 237.444], [3, 62.474999999999994, 69.615, 281.228, 287.122], [3, 202.29999999999998, 206.465, 272.808, 278.702], [3, 389.72499999999997, 393.89, 266.072, 271.966], [3, 389.72499999999997, 393.89, 303.12, 309.014], [3, 202.29999999999998, 206.465, 313.224, 319.118], [3, 249.89999999999998, 257.03999999999996, 324.17, 330.06399999999996], [3, 288.575, 296.31, 324.17, 330.06399999999996], [3, 329.03499999999997, 336.175, 324.17, 330.06399999999996], [3, 368.9, 376.03999999999996, 324.17, 330.06399999999996], [3, 354.025, 376.635, 330.06399999999996, 339.32599999999996], [3, 61.879999999999995, 69.615, 327.538, 333.432], [3, 389.72499999999997, 393.89, 341.01, 346.904], [3, 200.515, 207.06, 351.95599999999996, 357.84999999999997], [3, 61.879999999999995, 69.615, 375.532, 381.426], [3, 76.16, 80.325, 386.478, 392.372], [3, 108.28999999999999, 114.24, 386.478, 392.372], [3, 142.20499999999998, 148.75, 386.478, 392.372], [3, 176.12, 182.665, 386.478, 392.372], [3, 388.53499999999997, 392.10499999999996, 378.9, 384.794], [3, 398.055, 401.625, 389.00399999999996, 394.89799999999997], [3, 430.78, 434.34999999999997, 389.00399999999996, 394.89799999999997], [3, 464.09999999999997, 468.85999999999996, 389.00399999999996, 394.89799999999997], [3, 497.41999999999996, 502.17999999999995, 389.00399999999996, 394.89799999999997], [3, 528.9549999999999, 534.31, 389.00399999999996, 394.89799999999997], [3, 157.67499999999998, 182.665, 393.214, 401.63399999999996], [3, 510.51, 534.31, 395.74, 404.15999999999997], [3, 149.345, 174.92999999999998, 431.104, 443.734], [3, 199.325, 236.215, 431.104, 443.734], [3, 249.89999999999998, 274.295, 431.104, 443.734], [3, 282.03, 317.72999999999996, 431.104, 443.734], [3, 329.63, 379.60999999999996, 420.15799999999996, 432.788], [3, 357.0, 379.60999999999996, 433.63, 446.26], [3, 388.53499999999997, 424.83, 433.63, 446.26], [3, 437.325, 473.62, 433.63, 446.26], [3, 362.35499999999996, 379.60999999999996, 447.94399999999996, 460.574], [3, 121.38, 138.04, 463.942, 474.888], [3, 157.07999999999998, 161.245, 463.942, 474.888], [3, 178.5, 187.42499999999998, 460.574, 469.83599999999996], [3, 216.57999999999998, 237.405, 463.942, 474.888], [3, 255.255, 276.08, 463.942, 474.888], [3, 298.69, 318.91999999999996, 463.942, 474.888], [3, 359.38, 380.79999999999995, 463.942, 474.888], [3, 404.59999999999997, 425.42499999999995, 463.942, 474.888], [3, 438.515, 474.215, 463.942, 474.888], [3, 121.38, 138.04, 482.466, 493.412], [3, 157.07999999999998, 161.245, 482.466, 493.412], [3, 178.5, 187.42499999999998, 479.09799999999996, 488.35999999999996], [3, 216.57999999999998, 237.405, 482.466, 493.412], [3, 255.255, 276.08, 482.466, 493.412], [3, 298.69, 318.91999999999996, 482.466, 493.412], [3, 359.38, 380.79999999999995, 482.466, 493.412], [3, 404.59999999999997, 425.42499999999995, 482.466, 493.412], [3, 438.515, 474.215, 482.466, 493.412], [3, 107.695, 136.255, 500.99, 512.778], [3, 157.07999999999998, 161.245, 500.99, 512.778], [3, 178.5, 187.42499999999998, 497.62199999999996, 507.726], [3, 216.57999999999998, 237.405, 500.99, 512.778], [3, 253.47, 275.485, 500.99, 512.778], [3, 298.69, 318.91999999999996, 500.99, 512.778], [3, 320.11, 336.175, 491.728, 511.936], [3, 360.57, 381.99, 500.99, 512.778], [3, 404.59999999999997, 425.42499999999995, 500.99, 512.778], [3, 438.515, 474.215, 500.99, 512.778], [3, 82.11, 136.85, 520.356, 532.144], [3, 152.915, 163.03, 520.356, 532.144], [3, 177.31, 186.23499999999999, 516.9879999999999, 526.25], [3, 224.315, 236.81, 520.356, 532.144], [3, 262.99, 275.485, 520.356, 532.144], [3, 298.69, 318.91999999999996, 520.356, 532.144], [3, 368.9, 381.99, 520.356, 532.144], [3, 404.59999999999997, 425.42499999999995, 520.356, 532.144], [3, 444.465, 474.215, 520.356, 532.144], [3, 89.25, 136.85, 539.722, 551.51], [3, 152.915, 163.03, 539.722, 551.51], [3, 177.31, 186.23499999999999, 536.3539999999999, 545.616], [3, 224.315, 236.81, 539.722, 551.51], [3, 262.99, 275.485, 539.722, 551.51], [3, 298.69, 318.91999999999996, 539.722, 551.51], [3, 368.9, 381.99, 539.722, 551.51], [3, 404.59999999999997, 425.42499999999995, 539.722, 551.51], [3, 444.465, 474.215, 539.722, 551.51], [3, 114.24, 136.85, 559.088, 570.034], [3, 152.915, 164.22, 559.088, 570.034], [3, 177.31, 186.23499999999999, 555.72, 564.982], [3, 215.39, 236.81, 559.088, 570.034], [3, 252.875, 275.485, 559.088, 570.034], [3, 298.69, 318.91999999999996, 559.088, 570.034], [3, 359.38, 381.99, 559.088, 570.034], [3, 404.59999999999997, 425.42499999999995, 559.088, 570.034], [3, 438.515, 474.215, 559.088, 570.034], [3, 99.96, 136.85, 577.612, 589.4], [3, 152.915, 164.22, 577.612, 589.4], [3, 177.31, 186.23499999999999, 574.244, 583.506], [3, 215.39, 236.81, 577.612, 589.4], [3, 252.875, 275.485, 577.612, 589.4], [3, 298.69, 318.91999999999996, 577.612, 589.4], [3, 360.57, 381.99, 577.612, 589.4], [3, 404.59999999999997, 425.42499999999995, 577.612, 589.4]]
2026-08-10 13:02:25,238 INFO     29 [qwen-vl-text] ═══ DONE ═══ 126 positions, pages=1, time=69.3s
2026-08-10 13:02:25,249 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:02:25,249 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:02:25,250 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:02:25,250 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:02:25.250+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 36, "failed": 0, "current": {"60a23a7a94bb11f1bd9827cf206dfa2d": {"id": "60a23a7a94bb11f1bd9827cf206dfa2d", "doc_id": "6067e0fa94bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366792626, "task_type": "dataflow", "root_trace_id": "94d1339f4db64958b3764c87ea29c5c0", "root_traceparent": "00-94d1339f4db64958b3764c87ea29c5c0-51b0d67fb5a77038-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:02:25,255 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:25,255 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:02:26,158 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:02:26,170 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:02:26,170 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "228 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:02:26,170 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:02:26,172 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:02:26,189 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:02:26,189 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'AdmissionRecord': 1, 'ExaminationReport': 1}", "name": "GFXI 商丘.pdf"}
2026-08-10 13:02:26,189 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:02:26,236 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786366792850, 'update_date': datetime.datetime(2026, 8, 10, 12, 59, 52), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1019195, 'status': '1'}
2026-08-10 13:02:26,453 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=民权县人民医院
入院记录
姓名：
科室：呼吸二病区
床号：111
住院号：
体格检查
T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg
发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧
虑，走入病房，检查合作。
皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，
无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。
淋巴结：全身浅表淋巴结无肿大。
头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔
2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦
无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、
红肿，声音无嘶哑。
颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流
征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿
大。
胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、
皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。
肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发
感。叩诊音呈清音。呼吸音异常干性啰音。
心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所
示。心率82次/分，心律齐。
腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、
条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。
四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强
直、畸形。
肛门、直肠：未查。
外生殖器：未查。
专科检查
第2页
民权县人民医院
入院记录
姓名：
科室：呼吸二病区
床号：111
住院号：
科室：呼吸二病区
第(1)次住院
过敏史：无
姓名：盖凤先
性别：女
年龄：67岁
入院时间：2025-04-09 10:34
职业：农民
民族：回族
婚姻：已婚
记录时间：2025-04-09 10:34
籍贯：河南省商丘市
入院情况：有
联系方式：15824782345
现住址：河南省商丘市民权县伯党乡伯西村
病史陈述者：本人
可靠程度：供参
委会
考
工作单位：-
身份证号：412323195712211247
联系人：白磊
与患者关系：子
联系人电话：15824782345
主诉：胸闷、咳嗽、咳痰20余年，加重2天。
现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，
期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动
稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，
门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠
尚可，大小便无异常，体重无明显改变。
既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血
史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。
个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟
史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触
史，无疫区接触史，无冶游史。
婚姻史：25岁结婚，配偶健康。
月经生育史：
13
3-5
28-30
50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，
均健康。
家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性
疾病。
第1页
民权县人民医院
入院记录
姓名：
科室：呼吸二病区
床号：
住院号：
肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、
皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。
辅助检查
暂无。
初步诊断
1.哮喘（急性发作）
2.慢性支气管炎
住院医师：王贝贝
主治医师：陈文宁
主任医师：已签字
---
民权县人民医院
肺功能检查报告
病人ID:
2023-08-1501
性别：
女
高度：
158 cm
名：
出生日期：
1957/7/2
体重：
60 kg
姓：
年龄：
66 years
BMI：
24.0 kg/m²
体积
流量
体积
时间[s]
时间[s]
单位
预测值
之前
%预值
沙丁胺醇
(400
%预值
%变化
ug)
VC
I
(1)
2.37
1.66
70%
2.20
93%
+32.2%
VC
I
(1)
2.37
1.66
70%
2.20
93%
+32.2%
FEV1
I
(1)
1.99
0.88
44%
1.27
64%
+44.4%
FEV1/FVC
%
(1)
77
53
69%
58
75%
+9.3%
FEV1/VC
%
(1)
77
53
69%
58
75%
+9.3%
PEF
l/s
(1)
5.60
2.06
37%
2.74
49%
+32.9%
MEF75
l/s
(1)
5.04
0.97
19%
1.53
30%
+57.6%
MEF50
l/s
(1)
3.38
0.49
14%
0.78
23%
+60.6%
MEF25
l/s
(1)
1.12
0.22
19%
0.29
26%
+35.4%
诊断意见：
1.重度混合型通气功能障碍，小气道功能减低。
2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。
3.MVV:44%。建议定期复查。
(1): ECCS 1993
-1-
BTPS: 21.0 °C, 1013 hPa,
检测: 2023/8/15
50%
医生:-
Geratherm Respiratory GmbH
www.geratherm-respiratory.com
Blue Cherry V1.2.2.24
2026-08-10 13:02:26,699 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:02:26,699 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'AdmissionRecord': 1, 'ExaminationReport': 1}", "name": "GFXI 商丘.pdf", "embedding_token_consumption": 1975}
2026-08-10 13:02:26,699 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:02:26,833 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:02:26,833 INFO     29 [Trace] task=60a23a7a | doc=GFXI 商丘.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:02:26,835 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:02:26,835 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:02:26,840 INFO     29 set_progress(60a23a7a94bb11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:02:26 [DOC Engine]:
Start to index...
2026-08-10 13:02:26,859 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-10 13:02:26,865 INFO     29 set_progress(60a23a7a94bb11f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 13:02:26,874 INFO     29 set_progress(60a23a7a94bb11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:02:26 Indexing done (0.03s). Task done (147.02s)
2026-08-10 13:02:26,877 INFO     29 [Done], chunks(2), token(1975), elapsed:147.02
2026-08-10 13:02:26,974 INFO     29 handle_task done for task {"id": "60a23a7a94bb11f1bd9827cf206dfa2d", "doc_id": "6067e0fa94bb11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786366792626, "task_type": "dataflow", "root_trace_id": "94d1339f4db64958b3764c87ea29c5c0", "root_traceparent": "00-94d1339f4db64958b3764c87ea29c5c0-51b0d67fb5a77038-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
