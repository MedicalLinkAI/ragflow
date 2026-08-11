# 基准结果：lzga-哮喘-沈阳(1).pdf

## 基本信息

- 文件：`lzga-哮喘-沈阳(1).pdf`
- 大小：5899.8 KB
- PDF 总页数：5
- doc_id：`8cb8165094ae11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T19:28:02  完成时间：2026-08-10T19:30:39  耗时：157.3s
- progress_msg：`11:30:38 Indexing done (0.07s). Task done (148.32s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 2fafa658 | 1 | 1-1 | 信4个月 医疗机构：凤城市中医院 (组织机构代码：46376203-6) 医疗付 |
| 2 | f9021ee8 | 1 | 2-2 | 凤城诚岳中医院 门诊病历 诊断专用章 编号：54474 姓名： 性别：男 年龄： |
| 3 | 389e624a | 1 | 3-3 | 凤城诚岳中医院 诊断专用章 病历 编号：104474 姓名： 性别：男 年龄：6 |
| 4 | 46c79d30 | 1 | 4-4 | 欢迎光临健康大药房凤鸣分店 日期：2026-02-08 09:50:51 单号： |
| 5 | 1908092f | 1 | 5-5 | 医疗保险定点药店收费明细 辽宁天士力大药房连锁有限公司 药店名称： 凤城石桥路店 |
| 6 | 9f9c175f | 1 | 5-5 | 医疗保险定点药店收费明细 辽宁天士力大药房连锁有限公司 药店名称： 凤城石桥路店 |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[1, 2, 3, 4, 5]`
- 覆盖页数：5 / 5；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 3 | 3 | 3 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"DischargeRecord": 1, "OutpatientRecord": 2, "MedicationRecord": 3}`
- ChunkMerger：`{"found": true, "merged": 6, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 3, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 11:30:37,062 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 11:28:04,079 INFO     29 handle_task begin for task {"id": "8d2d744a94ae11f1bd9827cf206dfa2d", "doc_id": "8cb8165094ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3256443, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361283901, "task_type": "dataflow", "root_trace_id": "a109a49aa4f54fb6bb962f0e0599fa22", "root_traceparent": "00-a109a49aa4f54fb6bb962f0e0599fa22-2306060947da7753-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:28:04,323 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 11:28:04,441 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 11:28:04,456 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:28:04,456 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 11:28:04,456 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 11:28:04,461 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 11:28:04,461 INFO     29 ============================================================
2026-08-10 11:28:04,461 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 11:28:04,461 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 11:28:04,461 INFO     29 ============================================================
2026-08-10 11:28:04,461 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 11:28:04,461 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 11:28:04,463 INFO     29 No torch found.
2026-08-10 11:28:04,988 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-10 11:28:05,297 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1748129, prompt_len=764
2026-08-10 11:28:06,908 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-10-17"}
```
2026-08-10 11:28:06,909 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2024-10-17
2026-08-10 11:28:06,925 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1748129, prompt_len=401
2026-08-10 11:28:14,681 INFO     29 [qwen-vl-parser] text API response (len=1426):
["信4个月", "医疗机构：凤城市中医院", "(组织机构代码：46376203-6)", "医疗付费方式：城镇医保", "中医住院病案首页", "02410974", "健康卡号：", "第3次入院", "病案号：290510", "姓名：", "性别：1.男2.女出生日期：1958-12-09", "年龄：65岁", "国籍：中国", "(年龄不足一周岁的)年龄：", "新生儿出生体重：", "克", "新生儿入院体重：", "克", "出生地点：辽宁省凤城市", "籍贯：辽宁省", "民族：汉族", "身份证号：", "职业：退(离)休人", "婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他", "现地址：凤城市胜利委十组060644", "邮编：118100", "户口地址：凤城市胜利委十组060644", "邮编：118100", "工作单位：电业局", "邮编：118100", "联系人姓名：李治刚", "关系：本人或户", "地址：凤城市胜利委十组060644", "9", "入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他", "治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医", "入院时间：2024-10-08", "入院科别：内四科病房", "病房：11", "转科科别：", "出院时间：2024-10-15", "出院科别：内四科病房", "病房：", "实际住院：7 天", "门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)", "疾病编码：A04.04.04.02,A04.04.04.02", "门(急)诊诊断(西医诊断)：肺部感染", "疾病编码：J98.414", "实施临床路径：3 1.中医2.西医3否", "使用医疗机构中药制剂：2 1.是2.否", "使用中医诊疗设备：1 1.是2.否", "使用中医诊疗技术：1 1.是2.否", "辨证施护：1 1.是2.否", "出院中医诊断", "疾病编码", "入院", "病情", "出院西医诊断", "疾病编码", "入院", "病情", "主病：喘病(可选词：喘证)", "A04.04.04.02", "1", "主要诊断：支气管哮喘", "J45.900x001", "1", "主证：风寒袭肺证", "1", "其他诊断：冠状动脉粥样硬化性心脏", "I25.103", "1", "其他诊断：心功能II级(NYHA分级)", "I50.900x007", "1", "其他诊断：特应性神经性皮炎", "L20.803", "1", "入院病情：1.有，2.临床未确定，3.情况不明，4.无", "损伤、中毒的外部原因：", "疾病编码：", "病理诊断：", "疾病编码：", "病理号：", "药物过敏：1 1.无2.有过敏药物：", "死亡患者尸检：2 1.是2.否", "血型：□ 1.A 2.B 3.O 4.AB 5.不详 6.未查", "Rh 4 1.阴2.阳3.不详4.未查", "科主任：李革", "主任(副主任)医师：李革", "主治医师：宋文平", "住院医师：刘彦", "责任护士：唐莹莹", "进修医师：", "实习医师：", "编码员：", "病案质量 1 1.甲2.乙3.丙质控医师：刘彦", "质控护士：杨", "质控日期：2024-10-17"]
2026-08-10 11:28:14,682 INFO     29 [qwen-vl-parser] page=1 text: 99 lines (bbox 0-98)
2026-08-10 11:28:14,682 INFO     29 [qwen-vl-parser] page=1 text: 99 sections
2026-08-10 11:28:14,920 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1374813, prompt_len=764
2026-08-10 11:28:16,182 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:28:16,182 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 11:28:16,194 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1374813, prompt_len=401
2026-08-10 11:28:21,224 INFO     29 [qwen-vl-parser] text API response (len=652):
["凤城诚岳中医院", "门诊病历", "诊断专用章", "编号：54474", "姓名：", "性别：男", "年龄：67.0岁", "地址：燃机厂", "职业：退休", "联系电话", "99", "身份证号 21", "5", "就诊时间：2025年06月6日", "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白", "痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住", "院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1", "天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼", "吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。", "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，", "否认药物及食物过敏史、中毒史。", "体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82", "查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。", "辅助检查：", "初步诊断：支气管哮喘", "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "3、加重时及时就诊", "医师：梁明", "梁明"]
2026-08-10 11:28:21,225 INFO     29 [qwen-vl-parser] page=2 text: 31 lines (bbox 99-129)
2026-08-10 11:28:21,225 INFO     29 [qwen-vl-parser] page=2 text: 31 sections
2026-08-10 11:28:21,630 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2316365, prompt_len=764
2026-08-10 11:28:22,993 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:28:22,993 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 11:28:23,010 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2316365, prompt_len=401
2026-08-10 11:28:26,931 INFO     29 [qwen-vl-parser] text API response (len=650):
["凤城诚岳中医院", "诊断专用章 病历", "编号：104474", "姓名：", "性别：男", "年龄：67.0岁", "地址：", "职业：退休", "联系电话", "身份证号", "就诊时间：2026年02月8日", "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "现病史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。", "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。", "体温(℃)：36.8", "脉搏(次/分)：86", "呼吸(次/分) 26", "血压(mmHg) 140/80", "查体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。", "辅助检查：", "初步诊断：支气管哮喘（急性发作期）", "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "3、加重时及时就诊。", "医师：梁明", "梁明"]
2026-08-10 11:28:26,932 INFO     29 [qwen-vl-parser] page=3 text: 26 lines (bbox 130-155)
2026-08-10 11:28:26,932 INFO     29 [qwen-vl-parser] page=3 text: 26 sections
2026-08-10 11:28:27,369 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:28:27.369+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 22, "failed": 0, "current": {"8d2d744a94ae11f1bd9827cf206dfa2d": {"id": "8d2d744a94ae11f1bd9827cf206dfa2d", "doc_id": "8cb8165094ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3256443, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361283901, "task_type": "dataflow", "root_trace_id": "a109a49aa4f54fb6bb962f0e0599fa22", "root_traceparent": "00-a109a49aa4f54fb6bb962f0e0599fa22-2306060947da7753-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:28:27,507 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2787579, prompt_len=764
2026-08-10 11:28:29,399 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:28:29,401 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 11:28:29,431 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2787579, prompt_len=401
2026-08-10 11:28:32,366 INFO     29 [qwen-vl-parser] text API response (len=441):
["欢迎光临健康大药房凤鸣分店", "日期：2026-02-08 09:50:51", "单号：2602080008000051", "会员号:73504会员姓名:李治刚", "收银员：050", "机号:01", "营业员：050", "编号:1440166", "名称:醋酸泼尼松片（强地松 4", "产地:浙江仙琚制药股份有限", "批号:LA24600", "规格:5mg*100p", "剂型:片剂", "单价:6.5 实价:6.5", "数量:1.金额:6.5", "收款方式:现金", "6.50", "数量合计:1.00", "应收额:6.50", "实收:6.50", "优惠额:0.00 找零:0.00", "本单为重打印小票!不作开票依据", "代金卡余额:0.00", "本单积分:1.7", "累计积分:27.7", "本单代金卡金额:0.0", "零钱包存入:0", "周六会员日", "满49返15，满99返30", "此票据为购货凭证，请妥善保管"]
2026-08-10 11:28:32,367 INFO     29 [qwen-vl-parser] page=4 text: 30 lines (bbox 156-185)
2026-08-10 11:28:32,367 INFO     29 [qwen-vl-parser] page=4 text: 30 sections
2026-08-10 11:28:32,969 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3466945, prompt_len=764
2026-08-10 11:28:34,448 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:28:34,450 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 11:28:34,467 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3466945, prompt_len=401
2026-08-10 11:28:40,202 INFO     29 [qwen-vl-parser] text API response (len=842):
["医疗保险定点药店收费明细", "辽宁天士力大药房连锁有限公司", "药店名称：", "凤城石桥路店", "购药人：", "鲁药单：1", "2106210151", "个人编号：0000001017 票据号：100189", "563862", "序号 药品名称 数量 金额", "1 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "2 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "总金额：392.40", "人民币叁佰玖拾贰", "圆肆角整", "现金支", "账户支付：0.00", "392.40", "付：", "共济支", "统筹支付：0.0", "0.0", "付：", "公补：0.0", "消费前账户余额：0.00", "消费后账户余额：0.00", "2025.12.02", "消费时间：", "10:22:36", "收款员：2103", "无购药人、个人编号、药品明细购药单无效", "医疗保险定点药店收费明细", "辽宁天士力大药房连锁有限公司", "药店名称：", "凤城石桥路店", "购药人：", "鲁药单：1", "2106210151", "个人编号：0000001017 票据号：100246", "563862", "序号 药品名称 数量 金额", "1 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "2 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "总金额：392.40", "人民币叁佰玖拾贰", "圆肆角整", "现金支", "账户支付：0.00", "392.40", "付：", "共济支", "统筹支付：0.0", "0.0", "付：", "公补：0.0", "消费前账户余额：0.00", "消费后账户余额：0.00", "2026.02.01", "消费时间：", "19:49:51", "收款员：2103", "无购药人、个人编号、药品明细购药单无效"]
2026-08-10 11:28:40,205 INFO     29 [qwen-vl-parser] page=5 text: 66 lines (bbox 186-251)
2026-08-10 11:28:40,205 INFO     29 [qwen-vl-parser] page=5 text: 66 sections
2026-08-10 11:28:40,205 INFO     29 [qwen-vl-parser] parse_pdf done: 252 sections from 5 pages.
2026-08-10 11:28:40,216 INFO     29 Close text detector.
2026-08-10 11:28:40,677 INFO     29 Close text recognizer.
2026-08-10 11:28:41,072 INFO     29 Close recognizer.
2026-08-10 11:28:41,462 INFO     29 Close recognizer.
2026-08-10 11:28:41,923 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 11:28:41,924 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Parser:MedLink | outputs={"html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "json"}
2026-08-10 11:28:41,924 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 11:28:41,964 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:28:41,965 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 信4个月\n[BBOX-1] 医疗机构：凤城市中医院\n[BBOX-2] (组织机构代码：46376203-6)\n[BBOX-3] 医疗付费方式：城镇医保\n[BBOX-4] 中医住院病案首页\n[BBOX-5] 02410974\n[BBOX-6] 健康卡号：\n[BBOX-7] 第3次入院\n[BBOX-8] 病案号：290510\n[BBOX-9] 姓名：\n[BBOX-10] 性别：1.男2.女出生日期：1958-12-09\n[BBOX-11] 年龄：65岁\n[BBOX-12] 国籍：中国\n[BBOX-13] (年龄不足一周岁的)年龄：\n[BBOX-14] 新生儿出生体重：\n[BBOX-15] 克\n[BBOX-16] 新生儿入院体重：\n[BBOX-17] 克\n[BBOX-18] 出生地点：辽宁省凤城市\n[BBOX-19] 籍贯：辽宁省\n[BBOX-20] 民族：汉族\n[BBOX-21] 身份证号：\n[BBOX-22] 职业：退(离)休人\n[BBOX-23] 婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他\n[BBOX-24] 现地址：凤城市胜利委十组060644\n[BBOX-25] 邮编：118100\n[BBOX-26] 户口地址：凤城市胜利委十组060644\n[BBOX-27] 邮编：118100\n[BBOX-28] 工作单位：电业局\n[BBOX-29] 邮编：118100\n[BBOX-30] 联系人姓名：李治刚\n[BBOX-31] 关系：本人或户\n[BBOX-32] 地址：凤城市胜利委十组060644\n[BBOX-33] 9\n[BBOX-34] 入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他\n[BBOX-35] 治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医\n[BBOX-36] 入院时间：2024-10-08\n[BBOX-37] 入院科别：内四科病房\n[BBOX-38] 病房：11\n[BBOX-39] 转科科别：\n[BBOX-40] 出院时间：2024-10-15\n[BBOX-41] 出院科别：内四科病房\n[BBOX-42] 病房：\n[BBOX-43] 实际住院：7 天\n[BBOX-44] 门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)\n[BBOX-45] 疾病编码：A04.04.04.02,A04.04.04.02\n[BBOX-46] 门(急)诊诊断(西医诊断)：肺部感染\n[BBOX-47] 疾病编码：J98.414\n[BBOX-48] 实施临床路径：3 1.中医2.西医3否\n[BBOX-49] 使用医疗机构中药制剂：2 1.是2.否\n[BBOX-50] 使用中医诊疗设备：1 1.是2.否\n[BBOX-51] 使用中医诊疗技术：1 1.是2.否\n[BBOX-52] 辨证施护：1 1.是2.否\n[BBOX-53] 出院中医诊断\n[BBOX-54] 疾病编码\n[BBOX-55] 入院\n[BBOX-56] 病情\n[BBOX-57] 出院西医诊断\n[BBOX-58] 疾病编码\n[BBOX-59] 入院\n[BBOX-60] 病情\n[BBOX-61] 主病：喘病(可选词：喘证)\n[BBOX-62] A04.04.04.02\n[BBOX-63] 1\n[BBOX-64] 主要诊断：支气管哮喘\n[BBOX-65] J45.900x001\n[BBOX-66] 1\n[BBOX-67] 主证：风寒袭肺证\n[BBOX-68] 1\n[BBOX-69] 其他诊断：冠状动脉粥样硬化性心脏\n[BBOX-70] I25.103\n[BBOX-71] 1\n[BBOX-72] 其他诊断：心功能II级(NYHA分级)\n[BBOX-73] I50.900x007\n[BBOX-74] 1\n[BBOX-75] 其他诊断：特应性神经性皮炎\n[BBOX-76] L20.803\n[BBOX-77] 1\n[BBOX-78] 入院病情：1.有，2.临床未确定，3.情况不明，4.无\n[BBOX-79] 损伤、中毒的外部原因：\n[BBOX-80] 疾病编码：\n[BBOX-81] 病理诊断：\n[BBOX-82] 疾病编码：\n[BBOX-83] 病理号：\n[BBOX-84] 药物过敏：1 1.无2.有过敏药物：\n[BBOX-85] 死亡患者尸检：2 1.是2.否\n[BBOX-86] 血型：□ 1.A 2.B 3.O 4.AB 5.不详 6.未查\n[BBOX-87] Rh 4 1.阴2.阳3.不详4.未查\n[BBOX-88] 科主任：李革\n[BBOX-89] 主任(副主任)医师：李革\n[BBOX-90] 主治医师：宋文平\n[BBOX-91] 住院医师：刘彦\n[BBOX-92] 责任护士：唐莹莹\n[BBOX-93] 进修医师：\n[BBOX-94] 实习医师：\n[BBOX-95] 编码员：\n[BBOX-96] 病案质量 1 1.甲2.乙3.丙质控医师：刘彦\n[BBOX-97] 质控护士：杨\n[BBOX-98] 质控日期：2024-10-17\n[BBOX-99] 凤城诚岳中医院\n[BBOX-100] 门诊病历\n[BBOX-101] 诊断专用章\n[BBOX-102] 编号：54474\n[BBOX-103] 姓名：\n[BBOX-104] 性别：男\n[BBOX-105] 年龄：67.0岁\n[BBOX-106] 地址：燃机厂\n[BBOX-107] 职业：退休\n[BBOX-108] 联系电话\n[BBOX-109] 99\n[BBOX-110] 身份证号 21\n[BBOX-111] 5\n[BBOX-112] 就诊时间：2025年06月6日\n[BBOX-113] 主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。\n[BBOX-114] 现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白\n[BBOX-115] 痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住\n[BBOX-116] 院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1\n[BBOX-117] 天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼\n[BBOX-118] 吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。\n[BBOX-119] 既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，\n[BBOX-120] 否认药物及食物过敏史、中毒史。\n[BBOX-121] 体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82\n[BBOX-122] 查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。\n[BBOX-123] 辅助检查：\n[BBOX-124] 初步诊断：支气管哮喘\n[BBOX-125] 处置建议：1、舒利迭50/250ug/吸日二次吸入。\n[BBOX-126] 2、醋酸泼尼松（强的松）20mg日一次口服3-5天\n[BBOX-127] 3、加重时及时就诊\n[BBOX-128] 医师：梁明\n[BBOX-129] 梁明\n[BBOX-130] 凤城诚岳中医院\n[BBOX-131] 诊断专用章 病历\n[BBOX-132] 编号：104474\n[BBOX-133] 姓名：\n[BBOX-134] 性别：男\n[BBOX-135] 年龄：67.0岁\n[BBOX-136] 地址：\n[BBOX-137] 职业：退休\n[BBOX-138] 联系电话\n[BBOX-139] 身份证号\n[BBOX-140] 就诊时间：2026年02月8日\n[BBOX-141] 主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。\n[BBOX-142] 现病史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。\n[BBOX-143] 既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。\n[BBOX-144] 体温(℃)：36.8\n[BBOX-145] 脉搏(次/分)：86\n[BBOX-146] 呼吸(次/分) 26\n[BBOX-147] 血压(mmHg) 140/80\n[BBOX-148] 查体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。\n[BBOX-149] 辅助检查：\n[BBOX-150] 初步诊断：支气管哮喘（急性发作期）\n[BBOX-151] 处置建议：1、舒利迭50/250ug/吸日二次吸入。\n[BBOX-152] 2、醋酸泼尼松（强的松）20mg日一次口服3-5天\n[BBOX-153] 3、加重时及时就诊。\n[BBOX-154] 医师：梁明\n[BBOX-155] 梁明\n[BBOX-156] 欢迎光临健康大药房凤鸣分店\n[BBOX-157] 日期：2026-02-08 09:50:51\n[BBOX-158] 单号：2602080008000051\n[BBOX-159] 会员号:73504会员姓名:李治刚\n[BBOX-160] 收银员：050\n[BBOX-161] 机号:01\n[BBOX-162] 营业员：050\n[BBOX-163] 编号:1440166\n[BBOX-164] 名称:醋酸泼尼松片（强地松 4\n[BBOX-165] 产地:浙江仙琚制药股份有限\n[BBOX-166] 批号:LA24600\n[BBOX-167] 规格:5mg*100p\n[BBOX-168] 剂型:片剂\n[BBOX-169] 单价:6.5 实价:6.5\n[BBOX-170] 数量:1.金额:6.5\n[BBOX-171] 收款方式:现金\n[BBOX-172] 6.50\n[BBOX-173] 数量合计:1.00\n[BBOX-174] 应收额:6.50\n[BBOX-175] 实收:6.50\n[BBOX-176] 优惠额:0.00 找零:0.00\n[BBOX-177] 本单为重打印小票!不作开票依据\n[BBOX-178] 代金卡余额:0.00\n[BBOX-179] 本单积分:1.7\n[BBOX-180] 累计积分:27.7\n[BBOX-181] 本单代金卡金额:0.0\n[BBOX-182] 零钱包存入:0\n[BBOX-183] 周六会员日\n[BBOX-184] 满49返15，满99返30\n[BBOX-185] 此票据为购货凭证，请妥善保管\n[BBOX-186] 医疗保险定点药店收费明细\n[BBOX-187] 辽宁天士力大药房连锁有限公司\n[BBOX-188] 药店名称：\n[BBOX-189] 凤城石桥路店\n[BBOX-190] 购药人：\n[BBOX-191] 鲁药单：1\n[BBOX-192] 2106210151\n[BBOX-193] 个人编号：0000001017 票据号：100189\n[BBOX-194] 563862\n[BBOX-195] 序号 药品名称 数量 金额\n[BBOX-196] 1 沙美特罗替卡 1.0 196.20\n[BBOX-197] 松吸入粉雾剂\n[BBOX-198] 2 沙美特罗替卡 1.0 196.20\n[BBOX-199] 松吸入粉雾剂\n[BBOX-200] 总金额：392.40\n[BBOX-201] 人民币叁佰玖拾贰\n[BBOX-202] 圆肆角整\n[BBOX-203] 现金支\n[BBOX-204] 账户支付：0.00\n[BBOX-205] 392.40\n[BBOX-206] 付：\n[BBOX-207] 共济支\n[BBOX-208] 统筹支付：0.0\n[BBOX-209] 0.0\n[BBOX-210] 付：\n[BBOX-211] 公补：0.0\n[BBOX-212] 消费前账户余额：0.00\n[BBOX-213] 消费后账户余额：0.00\n[BBOX-214] 2025.12.02\n[BBOX-215] 消费时间：\n[BBOX-216] 10:22:36\n[BBOX-217] 收款员：2103\n[BBOX-218] 无购药人、个人编号、药品明细购药单无效\n[BBOX-219] 医疗保险定点药店收费明细\n[BBOX-220] 辽宁天士力大药房连锁有限公司\n[BBOX-221] 药店名称：\n[BBOX-222] 凤城石桥路店\n[BBOX-223] 购药人：\n[BBOX-224] 鲁药单：1\n[BBOX-225] 2106210151\n[BBOX-226] 个人编号：0000001017 票据号：100246\n[BBOX-227] 563862\n[BBOX-228] 序号 药品名称 数量 金额\n[BBOX-229] 1 沙美特罗替卡 1.0 196.20\n[BBOX-230] 松吸入粉雾剂\n[BBOX-231] 2 沙美特罗替卡 1.0 196.20\n[BBOX-232] 松吸入粉雾剂\n[BBOX-233] 总金额：392.40\n[BBOX-234] 人民币叁佰玖拾贰\n[BBOX-235] 圆肆角整\n[BBOX-236] 现金支\n[BBOX-237] 账户支付：0.00\n[BBOX-238] 392.40\n[BBOX-239] 付：\n[BBOX-240] 共济支\n[BBOX-241] 统筹支付：0.0\n[BBOX-242] 0.0\n[BBOX-243] 付：\n[BBOX-244] 公补：0.0\n[BBOX-245] 消费前账户余额：0.00\n[BBOX-246] 消费后账户余额：0.00\n[BBOX-247] 2026.02.01\n[BBOX-248] 消费时间：\n[BBOX-249] 19:49:51\n[BBOX-250] 收款员：2103\n[BBOX-251] 无购药人、个人编号、药品明细购药单无效"
  }
]
2026-08-10 11:28:48,751 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:28:49,251 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'DischargeRecord': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3}
2026-08-10 11:28:49,263 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 11:28:49,264 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks": "6 items, types={'DischargeRecord': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3}"}
2026-08-10 11:28:49,264 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 11:28:49,264 INFO     29 [ChunkRouter] Routed 6 chunks into 3 groups: {'chunks_Discharge': 1, 'chunks_Clinical': 2, 'chunks_Medication': 3}
2026-08-10 11:28:49,280 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 11:28:49,280 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks": "6 items, types={'DischargeRecord': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:28:49,280 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 11:28:49,286 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:28:49,286 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:28:50,613 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:28:50,623 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 11:28:50,623 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:28:50,623 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 11:28:50,635 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:28:50,635 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:28:51,058 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:28:51,067 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 11:28:51,067 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:28:51,067 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 11:28:51,076 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:28:51,077 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:28:51,077 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:28:51,077 INFO     29 [qwen-vl-text] positions(31): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:28:51,077 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [31]
2026-08-10 11:28:51,316 INFO     29 [qwen-vl-text] page=1, rect=595x794, img=(1654x2206), dpi=200
2026-08-10 11:28:51,317 INFO     29 [qwen-vl-text] LLM extraction start, text_len=558
2026-08-10 11:28:51,317 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:28:51,318 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 99, \"bbox_end\": 129, \"encounter_dates\": [\"2025-06-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "凤城诚岳中医院\n门诊病历\n诊断专用章\n编号：54474\n姓名：\n性别：男\n年龄：67.0岁\n地址：燃机厂\n职业：退休\n联系电话\n99\n身份证号 21\n5\n就诊时间：2025年06月6日\n主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。\n现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白\n痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住\n院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1\n天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼\n吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。\n既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，\n否认药物及食物过敏史、中毒史。\n体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82\n查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。\n辅助检查：\n初步诊断：支气管哮喘\n处置建议：1、舒利迭50/250ug/吸日二次吸入。\n2、醋酸泼尼松（强的松）20mg日一次口服3-5天\n3、加重时及时就诊\n医师：梁明\n梁明",
    "role": "user"
  }
]
2026-08-10 11:28:54,153 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:28:54,153 INFO     29 [qwen-vl-text] LLM output (len=504):
{
  "encounter_date": "2025-06-06",
  "chief_complaint": "反复发作喘息、气促50余年，加重伴呼吸困难1天。",
  "present_illness": "患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。",
  "past_history": "否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。",
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "舒利迭50/250ug/吸日二次吸入",
    "醋酸泼尼松（强的松）20mg日一次口服3-5天",
    "加重时及时就诊"
  ]
}
2026-08-10 11:28:54,153 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-06-06]
2026-08-10 11:28:54,157 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1780559, prompt_len=1264
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["凤城诚岳中医院", "门诊病历", "诊断专用章", "编号：54474", "姓名：", "性别：男", "年龄：67.0岁", "地址：燃机厂", "职业：退休", "联系电话", "99", "身份证号 21", "5", "就诊时间：2025年06月6日", "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白", "痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住", "院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1", "天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼", "吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。", "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，", "否认药物及食物过敏史、中毒史。", "体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82", "查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。", "辅助检查：", "初步诊断：支气管哮喘", "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "3、加重时及时就诊", "医师：梁明", "梁明"]

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
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord API raw response (len=1908):
[
	{"text": "凤城诚岳中医院", "bbox": [397, 65, 579, 90]},
	{"text": "门诊病历", "bbox": [389, 90, 577, 110]},
	{"text": "诊断专用章", "bbox": [425, 107, 535, 125]},
	{"text": "编号：54474", "bbox": [752, 105, 888, 121]},
	{"text": "姓名：", "bbox": [107, 142, 152, 157]},
	{"text": "性别：男", "bbox": [370, 135, 467, 150]},
	{"text": "年龄：67.0岁", "bbox": [605, 130, 752, 145]},
	{"text": "地址：燃机厂", "bbox": [105, 158, 348, 173]},
	{"text": "职业：退休", "bbox": [605, 148, 727, 163]},
	{"text": "联系电话", "bbox": [103, 176, 177, 190]},
	{"text": "99", "bbox": [300, 173, 318, 186]},
	{"text": "身份证号 21", "bbox": [585, 166, 707, 182]},
	{"text": "5", "bbox": [864, 164, 875, 176]},
	{"text": "就诊时间：2025年06月6日", "bbox": [98, 207, 344, 225]},
	{"text": "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "bbox": [95, 222, 652, 243]},
	{"text": "现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白", "bbox": [87, 275, 900, 296]},
	{"text": "痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住", "bbox": [83, 294, 901, 316]},
	{"text": "院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1", "bbox": [82, 313, 901, 335]},
	{"text": "天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼", "bbox": [80, 333, 902, 355]},
	{"text": "吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。", "bbox": [77, 352, 904, 374]},
	{"text": "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，", "bbox": [72, 395, 905, 415]},
	{"text": "否认药物及食物过敏史、中毒史。", "bbox": [71, 415, 366, 434]},
	{"text": "体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82", "bbox": [62, 475, 890, 498]},
	{"text": "查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。", "bbox": [56, 516, 813, 540]},
	{"text": "辅助检查：", "bbox": [48, 577, 137, 596]},
	{"text": "初步诊断：支气管哮喘", "bbox": [40, 643, 250, 666]},
	{"text": "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "bbox": [33, 685, 486, 715]},
	{"text": "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "bbox": [133, 710, 625, 743]},
	{"text": "3、加重时及时就诊", "bbox": [131, 733, 320, 758]},
	{"text": "医师：梁明", "bbox": [637, 821, 757, 846]},
	{"text": "梁明", "bbox": [687, 805, 736, 824]}
]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=10.7s
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[0]: text=凤城诚岳中医院, bbox=[397, 65, 579, 90]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[389, 90, 577, 110]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[2]: text=诊断专用章, bbox=[425, 107, 535, 125]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[3]: text=编号：54474, bbox=[752, 105, 888, 121]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[107, 142, 152, 157]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[370, 135, 467, 150]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：67.0岁, bbox=[605, 130, 752, 145]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[7]: text=地址：燃机厂, bbox=[105, 158, 348, 173]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[8]: text=职业：退休, bbox=[605, 148, 727, 163]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[9]: text=联系电话, bbox=[103, 176, 177, 190]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[10]: text=99, bbox=[300, 173, 318, 186]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号 21, bbox=[585, 166, 707, 182]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[12]: text=5, bbox=[864, 164, 875, 176]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[13]: text=就诊时间：2025年06月6日, bbox=[98, 207, 344, 225]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。, bbox=[95, 222, 652, 243]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白, bbox=[87, 275, 900, 296]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[16]: text=痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住, bbox=[83, 294, 901, 316]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[17]: text=院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1, bbox=[82, 313, 901, 335]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[18]: text=天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼, bbox=[80, 333, 902, 355]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[19]: text=吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。, bbox=[77, 352, 904, 374]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[20]: text=既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，, bbox=[72, 395, 905, 415]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[21]: text=否认药物及食物过敏史、中毒史。, bbox=[71, 415, 366, 434]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[22]: text=体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82, bbox=[62, 475, 890, 498]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[23]: text=查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。, bbox=[56, 516, 813, 540]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[24]: text=辅助检查：, bbox=[48, 577, 137, 596]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[25]: text=初步诊断：支气管哮喘, bbox=[40, 643, 250, 666]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[26]: text=处置建议：1、舒利迭50/250ug/吸日二次吸入。, bbox=[33, 685, 486, 715]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[27]: text=2、醋酸泼尼松（强的松）20mg日一次口服3-5天, bbox=[133, 710, 625, 743]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[28]: text=3、加重时及时就诊, bbox=[131, 733, 320, 758]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[29]: text=医师：梁明, bbox=[637, 821, 757, 846]
2026-08-10 11:29:04,894 INFO     29 [qwen-vl-text] coord item[30]: text=梁明, bbox=[687, 805, 736, 824]
2026-08-10 11:29:04,895 INFO     29 [qwen-vl-text] page=1 — 31/31 coords, api_time=10.7s
2026-08-10 11:29:04,895 INFO     29 [qwen-vl-text] new_positions (31):
[[1, 236.32617163085936, 344.6671369628906, 51.610650634765626, 71.46090087890624], [1, 231.56393139648435, 343.47657690429685, 71.46090087890624, 87.34110107421874], [1, 252.99401245117187, 318.4748156738281, 84.95907104492187, 99.25125122070312], [1, 447.65058203125, 528.608666015625, 83.37105102539063, 96.07521118164063], [1, 63.69496313476562, 90.482564453125, 112.74942138671875, 124.65957153320312], [1, 220.25361083984373, 277.9957736816406, 107.19135131835937, 119.10150146484375], [1, 360.14441772460935, 447.65058203125, 103.22130126953125, 115.13145141601562], [1, 62.50440307617187, 207.1574501953125, 125.45358154296875, 137.36373168945312], [1, 360.14441772460935, 432.7685812988281, 117.5134814453125, 129.42363159179686], [1, 61.31384301757812, 105.36456518554687, 139.74576171875, 150.86190185546874], [1, 178.5840087890625, 189.29904931640624, 137.36373168945312, 147.68586181640623], [1, 348.23881713867183, 420.8629807128906, 131.80566162109375, 144.50982177734375], [1, 514.3219453125, 520.8700256347656, 130.2176416015625, 139.74576171875], [1, 58.33744287109374, 204.776330078125, 164.36007202148437, 178.65225219726562], [1, 56.55160278320312, 388.12257910156245, 176.27022216796874, 192.94443237304688], [1, 51.78936254882812, 535.7520263671875, 218.35275268554688, 235.026962890625], [1, 49.40824243164062, 536.3473063964843, 233.43894287109373, 250.9071630859375], [1, 48.81296240234374, 536.3473063964843, 248.5251330566406, 265.99335327148435], [1, 47.62240234375, 536.9425864257812, 264.4053332519531, 281.87355346679686], [1, 45.83656225585937, 538.133146484375, 279.4915234375, 296.9597436523437], [1, 42.860162109375, 538.7284265136718, 313.6339538574219, 329.51415405273434], [1, 42.264882080078124, 217.87249072265624, 329.51415405273434, 344.60034423828125], [1, 36.90736181640625, 529.7992260742187, 377.1547546386719, 395.41698486328124], [1, 33.335681640625, 483.9626638183593, 409.7091650390625, 428.76540527343747], [1, 28.573441406249998, 81.55336401367187, 458.14377563476563, 473.2299658203125], [1, 23.811201171875, 148.82000732421875, 510.5484362792969, 528.8106665039062], [1, 19.644240966796872, 289.3060942382812, 543.8968566894531, 567.7171569824219], [1, 79.17224389648437, 372.0500183105469, 563.7471069335937, 589.9494372558594], [1, 77.98168383789061, 190.489609375, 582.0093371582032, 601.8595874023438], [1, 379.19337866210935, 450.62698217773436, 651.8822180175781, 671.7324682617187], [1, 408.95738012695307, 438.12610156249997, 639.178057861328, 654.264248046875]]
2026-08-10 11:29:04,895 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=13.8s
2026-08-10 11:29:04,895 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:29:04,901 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:29:04,901 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:29:04,901 INFO     29 [qwen-vl-text] positions(26): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:29:04,901 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [26]
2026-08-10 11:29:05,208 INFO     29 [qwen-vl-text] page=2, rect=595x794, img=(1654x2206), dpi=200
2026-08-10 11:29:05,208 INFO     29 [qwen-vl-text] LLM extraction start, text_len=571
2026-08-10 11:29:05,209 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:05,209 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 130, \"bbox_end\": 155, \"encounter_dates\": [\"2026-02-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "凤城诚岳中医院\n诊断专用章 病历\n编号：104474\n姓名：\n性别：男\n年龄：67.0岁\n地址：\n职业：退休\n联系电话\n身份证号\n就诊时间：2026年02月8日\n主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。\n现病史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。\n既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。\n体温(℃)：36.8\n脉搏(次/分)：86\n呼吸(次/分) 26\n血压(mmHg) 140/80\n查体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。\n辅助检查：\n初步诊断：支气管哮喘（急性发作期）\n处置建议：1、舒利迭50/250ug/吸日二次吸入。\n2、醋酸泼尼松（强的松）20mg日一次口服3-5天\n3、加重时及时就诊。\n医师：梁明\n梁明",
    "role": "user"
  }
]
2026-08-10 11:29:05,212 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:29:05.211+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 22, "failed": 0, "current": {"8d2d744a94ae11f1bd9827cf206dfa2d": {"id": "8d2d744a94ae11f1bd9827cf206dfa2d", "doc_id": "8cb8165094ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3256443, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361283901, "task_type": "dataflow", "root_trace_id": "a109a49aa4f54fb6bb962f0e0599fa22", "root_traceparent": "00-a109a49aa4f54fb6bb962f0e0599fa22-2306060947da7753-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:29:08,778 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:08,778 INFO     29 [qwen-vl-text] LLM output (len=538):
{
  "encounter_date": "2026-02-08",
  "chief_complaint": "反复发作喘息、气促50余年，加重伴呼吸困难1天。",
  "present_illness": "患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。",
  "past_history": "否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。",
  "diagnosis": "支气管哮喘（急性发作期）",
  "treatment_plan": [
    "舒利迭50/250ug/吸日二次吸入",
    "醋酸泼尼松（强的松）20mg日一次口服3-5天",
    "加重时及时就诊"
  ]
}
2026-08-10 11:29:08,778 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-08]
2026-08-10 11:29:08,787 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3257554, prompt_len=1262
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["凤城诚岳中医院", "诊断专用章 病历", "编号：104474", "姓名：", "性别：男", "年龄：67.0岁", "地址：", "职业：退休", "联系电话", "身份证号", "就诊时间：2026年02月8日", "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "现病史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。", "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。", "体温(℃)：36.8", "脉搏(次/分)：86", "呼吸(次/分) 26", "血压(mmHg) 140/80", "查体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。", "辅助检查：", "初步诊断：支气管哮喘（急性发作期）", "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "3、加重时及时就诊。", "医师：梁明", "梁明"]

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
2026-08-10 11:29:18,982 INFO     29 [qwen-vl-text] coord API raw response (len=1703):
[
	{"text": "凤城诚岳中医院", "bbox": [407, 48, 610, 72]},
	{"text": "诊断专用章 病历", "bbox": [380, 77, 604, 100]},
	{"text": "编号：104474", "bbox": [787, 103, 937, 122]},
	{"text": "姓名：", "bbox": [71, 130, 124, 148]},
	{"text": "性别：男", "bbox": [381, 130, 490, 148]},
	{"text": "年龄：67.0岁", "bbox": [641, 130, 798, 148]},
	{"text": "地址：", "bbox": [71, 151, 124, 169]},
	{"text": "职业：退休", "bbox": [641, 151, 771, 169]},
	{"text": "联系电话", "bbox": [71, 172, 162, 190]},
	{"text": "身份证号", "bbox": [621, 172, 707, 190]},
	{"text": "就诊时间：2026年02月8日", "bbox": [71, 217, 358, 235]},
	{"text": "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "bbox": [71, 238, 694, 256]},
	{"text": "现病史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。", "bbox": [74, 300, 946, 430]},
	{"text": "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。", "bbox": [76, 470, 946, 518]},
	{"text": "体温(℃)：36.8", "bbox": [78, 565, 253, 584]},
	{"text": "脉搏(次/分)：86", "bbox": [288, 563, 471, 581]},
	{"text": "呼吸(次/分) 26", "bbox": [525, 559, 691, 577]},
	{"text": "血压(mmHg) 140/80", "bbox": [735, 557, 928, 575]},
	{"text": "查体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。", "bbox": [78, 602, 747, 627]},
	{"text": "辅助检查：", "bbox": [78, 677, 177, 695]},
	{"text": "初步诊断：支气管哮喘（急性发作期）", "bbox": [78, 738, 454, 762]},
	{"text": "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "bbox": [78, 803, 548, 831]},
	{"text": "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "bbox": [191, 822, 684, 850]},
	{"text": "3、加重时及时就诊。", "bbox": [191, 850, 398, 872]},
	{"text": "医师：梁明", "bbox": [700, 917, 810, 954]},
	{"text": "梁明", "bbox": [747, 915, 795, 933]}
]
2026-08-10 11:29:18,982 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=10.2s
2026-08-10 11:29:18,982 INFO     29 [qwen-vl-text] coord item[0]: text=凤城诚岳中医院, bbox=[407, 48, 610, 72]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[1]: text=诊断专用章 病历, bbox=[380, 77, 604, 100]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[2]: text=编号：104474, bbox=[787, 103, 937, 122]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[71, 130, 124, 148]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[381, 130, 490, 148]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：67.0岁, bbox=[641, 130, 798, 148]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[6]: text=地址：, bbox=[71, 151, 124, 169]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[7]: text=职业：退休, bbox=[641, 151, 771, 169]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[8]: text=联系电话, bbox=[71, 172, 162, 190]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[9]: text=身份证号, bbox=[621, 172, 707, 190]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[10]: text=就诊时间：2026年02月8日, bbox=[71, 217, 358, 235]
2026-08-10 11:29:18,983 INFO     29 [qwen-vl-text] coord item[11]: text=主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。, bbox=[71, 238, 694, 256]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[12]: text=现病史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。, bbox=[74, 300, 946, 430]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[13]: text=既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。, bbox=[76, 470, 946, 518]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[14]: text=体温(℃)：36.8, bbox=[78, 565, 253, 584]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[15]: text=脉搏(次/分)：86, bbox=[288, 563, 471, 581]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[16]: text=呼吸(次/分) 26, bbox=[525, 559, 691, 577]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[17]: text=血压(mmHg) 140/80, bbox=[735, 557, 928, 575]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[18]: text=查体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。, bbox=[78, 602, 747, 627]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[19]: text=辅助检查：, bbox=[78, 677, 177, 695]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[20]: text=初步诊断：支气管哮喘（急性发作期）, bbox=[78, 738, 454, 762]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[21]: text=处置建议：1、舒利迭50/250ug/吸日二次吸入。, bbox=[78, 803, 548, 831]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[22]: text=2、醋酸泼尼松（强的松）20mg日一次口服3-5天, bbox=[191, 822, 684, 850]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[23]: text=3、加重时及时就诊。, bbox=[191, 850, 398, 872]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[24]: text=医师：梁明, bbox=[700, 917, 810, 954]
2026-08-10 11:29:18,984 INFO     29 [qwen-vl-text] coord item[25]: text=梁明, bbox=[747, 915, 795, 933]
2026-08-10 11:29:18,985 INFO     29 [qwen-vl-text] page=2 — 26/26 coords, api_time=10.2s
2026-08-10 11:29:18,985 INFO     29 [qwen-vl-text] new_positions (26):
[[2, 242.2789719238281, 363.1208178710937, 38.11248046875, 57.168720703125], [2, 226.2064111328125, 359.5491376953125, 61.138770751953125, 79.4010009765625], [2, 468.4853830566406, 557.7773874511719, 81.78303100585937, 96.86922119140624], [2, 42.264882080078124, 73.8147236328125, 103.22130126953125, 117.5134814453125], [2, 226.80169116210936, 291.6872143554687, 103.22130126953125, 117.5134814453125], [2, 381.57449877929685, 475.0334633789062, 103.22130126953125, 117.5134814453125], [2, 42.264882080078124, 73.8147236328125, 119.89551147460936, 134.18769165039063], [2, 381.57449877929685, 458.9609025878906, 119.89551147460936, 134.18769165039063], [2, 42.264882080078124, 96.43536474609374, 136.5697216796875, 150.86190185546874], [2, 369.6688981933593, 420.8629807128906, 136.5697216796875, 150.86190185546874], [2, 42.264882080078124, 213.11025048828122, 172.30017211914063, 186.59235229492188], [2, 42.264882080078124, 413.12434033203124, 188.97438232421874, 203.2665625], [2, 44.05072216796874, 563.1349077148437, 238.2030029296875, 341.42430419921874], [2, 45.2412822265625, 563.1349077148437, 373.18470458984376, 411.29718505859375], [2, 46.43184228515625, 150.60584741210937, 448.6156555175781, 463.701845703125], [2, 171.4406484375, 280.3768937988281, 447.02763549804683, 461.3198156738281], [2, 312.52201538085933, 411.3385002441406, 443.8515954589844, 458.14377563476563], [2, 437.5308215332031, 552.4198671874999, 442.2635754394531, 456.5557556152344], [2, 46.43184228515625, 444.6741818847656, 477.99402587890626, 497.8442761230469], [2, 46.43184228515625, 105.36456518554687, 537.5447766113281, 551.8369567871093], [2, 46.43184228515625, 270.2571333007812, 585.9793872070312, 605.0356274414062], [2, 46.43184228515625, 326.21345605468747, 637.5900378417969, 659.8223181152343], [2, 113.69848559570312, 407.17154003906245, 652.6762280273438, 674.9085083007812], [2, 113.69848559570312, 236.92145166015624, 674.9085083007812, 692.376728515625], [2, 416.6960205078125, 482.1768237304687, 728.1071789550781, 757.4855493164063], [2, 444.6741818847656, 473.2476232910156, 726.5191589355469, 740.8113391113282]]
2026-08-10 11:29:18,985 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=14.1s
2026-08-10 11:29:18,998 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 11:29:18,998 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:29:18,999 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 11:29:19,010 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:29:19,011 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:29:19,011 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:29:19,011 INFO     29 [qwen-vl-text] positions(30): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:29:19,011 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [30]
2026-08-10 11:29:19,308 INFO     29 [qwen-vl-text] page=3, rect=595x1058, img=(1654x2940), dpi=200
2026-08-10 11:29:19,309 INFO     29 [qwen-vl-text] LLM extraction start, text_len=350
2026-08-10 11:29:19,311 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:19,311 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 156, \"bbox_end\": 185, \"encounter_dates\": [\"2026-02-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "欢迎光临健康大药房凤鸣分店\n日期：2026-02-08 09:50:51\n单号：2602080008000051\n会员号:73504会员姓名:李治刚\n收银员：050\n机号:01\n营业员：050\n编号:1440166\n名称:醋酸泼尼松片（强地松 4\n产地:浙江仙琚制药股份有限\n批号:LA24600\n规格:5mg*100p\n剂型:片剂\n单价:6.5 实价:6.5\n数量:1.金额:6.5\n收款方式:现金\n6.50\n数量合计:1.00\n应收额:6.50\n实收:6.50\n优惠额:0.00 找零:0.00\n本单为重打印小票!不作开票依据\n代金卡余额:0.00\n本单积分:1.7\n累计积分:27.7\n本单代金卡金额:0.0\n零钱包存入:0\n周六会员日\n满49返15，满99返30\n此票据为购货凭证，请妥善保管",
    "role": "user"
  }
]
2026-08-10 11:29:22,521 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:22,521 INFO     29 [qwen-vl-text] LLM output (len=414):
{
  "encounter_date": "2026-02-08",
  "pharmacy": "健康大药房凤鸣分店",
  "medications": [
    {
      "name": "醋酸泼尼松片",
      "specification": "5mg*100p",
      "dosage": null,
      "quantity": 1,
      "unit_price": 6.5,
      "total_price": 6.5,
      "frequency": null,
      "route": null,
      "manufacturer": "浙江仙琚制药股份有限",
      "approval_number": null
    }
  ],
  "payment_total": 6.5,
  "payment_method": "现金"
}
2026-08-10 11:29:22,521 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-08]
2026-08-10 11:29:22,536 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5040141, prompt_len=1053
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["欢迎光临健康大药房凤鸣分店", "日期：2026-02-08 09:50:51", "单号：2602080008000051", "会员号:73504会员姓名:李治刚", "收银员：050", "机号:01", "营业员：050", "编号:1440166", "名称:醋酸泼尼松片（强地松 4", "产地:浙江仙琚制药股份有限", "批号:LA24600", "规格:5mg*100p", "剂型:片剂", "单价:6.5 实价:6.5", "数量:1.金额:6.5", "收款方式:现金", "6.50", "数量合计:1.00", "应收额:6.50", "实收:6.50", "优惠额:0.00 找零:0.00", "本单为重打印小票!不作开票依据", "代金卡余额:0.00", "本单积分:1.7", "累计积分:27.7", "本单代金卡金额:0.0", "零钱包存入:0", "周六会员日", "满49返15，满99返30", "此票据为购货凭证，请妥善保管"]

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
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord API raw response (len=1671):
[
	{"text": "欢迎光临健康大药房凤鸣分店", "bbox": [278, 225, 646, 255]},
	{"text": "日期：2026-02-08 09:50:51", "bbox": [277, 245, 620, 274]},
	{"text": "单号：2602080008000051", "bbox": [275, 265, 607, 294]},
	{"text": "会员号:73504会员姓名:李治刚", "bbox": [273, 287, 654, 317]},
	{"text": "收银员：050", "bbox": [270, 308, 435, 332]},
	{"text": "机号:01", "bbox": [473, 317, 568, 337]},
	{"text": "营业员：050", "bbox": [270, 344, 434, 367]},
	{"text": "编号:1440166", "bbox": [513, 354, 690, 371]},
	{"text": "名称:醋酸泼尼松片（强地松 4", "bbox": [270, 367, 658, 394]},
	{"text": "产地:浙江仙琚制药股份有限", "bbox": [266, 389, 623, 415],
	"text": "批号:LA24600", "bbox": [264, 411, 450, 433]},
	{"text": "规格:5mg*100p", "bbox": [263, 433, 467, 456]},
	{"text": "剂型:片剂", "bbox": [261, 456, 392, 478]},
	{"text": "单价:6.5 实价:6.5", "bbox": [261, 478, 506, 501]},
	{"text": "数量:1.金额:6.5", "bbox": [258, 501, 472, 521]},
	{"text": "收款方式:现金", "bbox": [254, 546, 463, 568]},
	{"text": "6.50", "bbox": [513, 551, 571, 568]},
	{"text": "数量合计:1.00", "bbox": [253, 570, 452, 590]},
	{"text": "应收额:6.50", "bbox": [250, 593, 434, 613]},
	{"text": "实收:6.50", "bbox": [467, 595, 612, 614]},
	{"text": "优惠额:0.00 找零:0.00", "bbox": [244, 642, 600, 664]},
	{"text": "本单为重打印小票!不作开票依据", "bbox": [241, 666, 708, 689]},
	{"text": "代金卡余额:0.00", "bbox": [238, 690, 490, 712]},
	{"text": "本单积分:1.7", "bbox": [236, 716, 441, 737]},
	{"text": "累计积分:27.7", "bbox": [235, 741, 456, 762]},
	{"text": "本单代金卡金额:0.0", "bbox": [233, 766, 533, 788]},
	{"text": "零钱包存入:0", "bbox": [230, 792, 420, 814]},
	{"text": "周六会员日", "bbox": [225, 846, 387, 867]},
	{"text": "满49返15，满99返30", "bbox": [223, 870, 528, 891]},
	{"text": "此票据为购货凭证，请妥善保管", "bbox": [222, 895, 675, 916]}
]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=10.0s
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[0]: text=欢迎光临健康大药房凤鸣分店, bbox=[278, 225, 646, 255]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[1]: text=日期：2026-02-08 09:50:51, bbox=[277, 245, 620, 274]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[2]: text=单号：2602080008000051, bbox=[275, 265, 607, 294]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[3]: text=会员号:73504会员姓名:李治刚, bbox=[273, 287, 654, 317]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[4]: text=收银员：050, bbox=[270, 308, 435, 332]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[5]: text=机号:01, bbox=[473, 317, 568, 337]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[6]: text=营业员：050, bbox=[270, 344, 434, 367]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[7]: text=编号:1440166, bbox=[513, 354, 690, 371]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[8]: text=名称:醋酸泼尼松片（强地松 4, bbox=[270, 367, 658, 394]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[9]: text=批号:LA24600, bbox=[264, 411, 450, 433]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[10]: text=规格:5mg*100p, bbox=[263, 433, 467, 456]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[11]: text=剂型:片剂, bbox=[261, 456, 392, 478]
2026-08-10 11:29:32,527 INFO     29 [qwen-vl-text] coord item[12]: text=单价:6.5 实价:6.5, bbox=[261, 478, 506, 501]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[13]: text=数量:1.金额:6.5, bbox=[258, 501, 472, 521]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[14]: text=收款方式:现金, bbox=[254, 546, 463, 568]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[15]: text=6.50, bbox=[513, 551, 571, 568]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[16]: text=数量合计:1.00, bbox=[253, 570, 452, 590]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[17]: text=应收额:6.50, bbox=[250, 593, 434, 613]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[18]: text=实收:6.50, bbox=[467, 595, 612, 614]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[19]: text=优惠额:0.00 找零:0.00, bbox=[244, 642, 600, 664]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[20]: text=本单为重打印小票!不作开票依据, bbox=[241, 666, 708, 689]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[21]: text=代金卡余额:0.00, bbox=[238, 690, 490, 712]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[22]: text=本单积分:1.7, bbox=[236, 716, 441, 737]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[23]: text=累计积分:27.7, bbox=[235, 741, 456, 762]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[24]: text=本单代金卡金额:0.0, bbox=[233, 766, 533, 788]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[25]: text=零钱包存入:0, bbox=[230, 792, 420, 814]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[26]: text=周六会员日, bbox=[225, 846, 387, 867]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[27]: text=满49返15，满99返30, bbox=[223, 870, 528, 891]
2026-08-10 11:29:32,528 INFO     29 [qwen-vl-text] coord item[28]: text=此票据为购货凭证，请妥善保管, bbox=[222, 895, 675, 916]
2026-08-10 11:29:32,529 INFO     29 [qwen-vl-text] page=3 — 30/30 coords, api_time=10.0s
2026-08-10 11:29:32,529 INFO     29 [qwen-vl-text] new_positions (30):
[[3, 165.48784814453123, 384.5508989257812, 238.11075439453126, 269.8588549804687], [3, 164.89256811523435, 369.07361816406245, 259.2761547851562, 289.9659853515625], [3, 163.7020080566406, 361.3349777832031, 280.4415551757813, 311.1313857421875], [3, 162.51144799804686, 389.3131391601562, 303.72349560546877, 335.47159619140626], [3, 160.72560791015624, 258.94681274414063, 325.947166015625, 351.345646484375], [3, 281.56745385742187, 338.119056640625, 335.47159619140626, 356.63699658203126], [3, 160.72560791015624, 258.35153271484376, 364.04488671875, 388.38509716796875], [3, 305.37865502929685, 410.74322021484375, 374.6275869140625, 392.61817724609375], [3, 160.72560791015624, 391.69425927734375, 388.38509716796875, 416.9583876953125], [3, 157.15392773437497, 267.8760131835937, 434.94897802734374, 458.23091845703124], [3, 156.5586477050781, 277.9957736816406, 458.23091845703124, 482.57112890625], [3, 155.36808764648435, 233.34977148437497, 482.57112890625, 505.8530693359375], [3, 155.36808764648435, 301.21169482421874, 505.8530693359375, 530.1932797851563], [3, 153.58224755859374, 280.972173828125, 530.1932797851563, 551.3586801757813], [3, 151.20112744140624, 275.6146535644531, 577.8154306640625, 601.09737109375], [3, 305.37865502929685, 339.9048967285156, 583.1067807617187, 601.09737109375], [3, 150.60584741210937, 269.0665732421875, 603.2139111328125, 624.3793115234375], [3, 148.82000732421875, 258.35153271484376, 627.5541215820313, 648.7195219726563], [3, 277.9957736816406, 364.31137792968747, 629.6706616210937, 649.7777919921875], [3, 145.24832714843748, 357.168017578125, 679.4093525390625, 702.69129296875], [3, 143.46248706054686, 421.45826074218746, 704.8078330078125, 729.1480434570312], [3, 141.67664697265624, 291.6872143554687, 730.2063134765625, 753.48825390625], [3, 140.4860869140625, 262.51849291992187, 757.721333984375, 779.9450043945312], [3, 139.89080688476562, 271.44769335937497, 784.1780844726562, 806.4017548828125], [3, 138.70024682617188, 317.2842556152344, 810.6348349609375, 833.916775390625], [3, 136.91440673828123, 250.01761230468747, 838.14985546875, 861.4317958984375], [3, 133.93800659179686, 230.3733713378906, 895.2964365234375, 917.5201069335938], [3, 132.74744653320312, 314.30785546874995, 920.6949169921875, 942.9185874023437], [3, 132.15216650390624, 401.8140197753906, 947.1516674804687, 969.375337890625], [3, 132.15216650390624, 401.8140197753906, 947.1516674804687, 969.375337890625]]
2026-08-10 11:29:32,529 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=13.5s
2026-08-10 11:29:32,529 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:29:32,531 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:29:32,531 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:29:32,531 INFO     29 [qwen-vl-text] positions(33): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:29:32,531 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [33]
2026-08-10 11:29:33,016 INFO     29 [qwen-vl-text] page=4, rect=595x794, img=(1654x2205), dpi=200
2026-08-10 11:29:33,017 INFO     29 [qwen-vl-text] LLM extraction start, text_len=321
2026-08-10 11:29:33,017 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:33,017 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 186, \"bbox_end\": 218, \"encounter_dates\": [\"2025-12-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "医疗保险定点药店收费明细\n辽宁天士力大药房连锁有限公司\n药店名称：\n凤城石桥路店\n购药人：\n鲁药单：1\n2106210151\n个人编号：0000001017 票据号：100189\n563862\n序号 药品名称 数量 金额\n1 沙美特罗替卡 1.0 196.20\n松吸入粉雾剂\n2 沙美特罗替卡 1.0 196.20\n松吸入粉雾剂\n总金额：392.40\n人民币叁佰玖拾贰\n圆肆角整\n现金支\n账户支付：0.00\n392.40\n付：\n共济支\n统筹支付：0.0\n0.0\n付：\n公补：0.0\n消费前账户余额：0.00\n消费后账户余额：0.00\n2025.12.02\n消费时间：\n10:22:36\n收款员：2103\n无购药人、个人编号、药品明细购药单无效",
    "role": "user"
  }
]
2026-08-10 11:29:35,979 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:35,979 INFO     29 [qwen-vl-text] LLM output (len=708):
{
  "encounter_date": "2025-12-02",
  "pharmacy": "辽宁天士力大药房连锁有限公司凤城石桥路店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 1.0,
      "unit_price": 196.20,
      "total_price": 196.20,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    },
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 1.0,
      "unit_price": 196.20,
      "total_price": 196.20,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 392.40,
  "payment_method": "现金支付"
}
2026-08-10 11:29:35,979 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-02]
2026-08-10 11:29:35,988 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4182181, prompt_len=1033
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["医疗保险定点药店收费明细", "辽宁天士力大药房连锁有限公司", "药店名称：", "凤城石桥路店", "购药人：", "鲁药单：1", "2106210151", "个人编号：0000001017 票据号：100189", "563862", "序号 药品名称 数量 金额", "1 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "2 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "总金额：392.40", "人民币叁佰玖拾贰", "圆肆角整", "现金支", "账户支付：0.00", "392.40", "付：", "共济支", "统筹支付：0.0", "0.0", "付：", "公补：0.0", "消费前账户余额：0.00", "消费后账户余额：0.00", "2025.12.02", "消费时间：", "10:22:36", "收款员：2103", "无购药人、个人编号、药品明细购药单无效"]

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
2026-08-10 11:29:45,813 INFO     29 [qwen-vl-text] coord API raw response (len=1762):
[
	{"text": "医疗保险定点药店收费明细", "bbox": [113, 240, 325, 270]},
	{"text": "辽宁天士力大药房连锁有限公司", "bbox": [147, 275, 325, 300]},
	{"text": "药店名称：", "bbox": [60, 295, 139, 311]},
	{"text": "凤城石桥路店", "bbox": [147, 314, 242, 329]},
	{"text": "购药人：", "bbox": [68, 336, 138, 351]},
	{"text": "鲁药单：1", "bbox": [250, 338, 294, 353]},
	{"text": "2106210151", "bbox": [146, 363, 241, 377]},
	{"text": "个人编号：0000001017 票据号：100189", "bbox": [59, 384, 331, 402]},
	{"text": "563862", "bbox": [145, 417, 203, 430]},
	{"text": "序号 药品名称 数量 金额", "bbox": [74, 440, 339, 460]},
	{"text": "1 沙美特罗替卡 1.0 196.20", "bbox": [85, 465, 346, 493]},
	{"text": "松吸入粉雾剂", "bbox": [143, 480, 240, 495]},
	{"text": "2 沙美特罗替卡 1.0 196.20", "bbox": [85, 500, 348, 527]},
	{"text": "松吸入粉雾剂", "bbox": [142, 513, 240, 528]},
	{"text": "总金额：392.40", "bbox": [64, 551, 195, 567]},
	{"text": "人民币叁佰玖拾贰", "bbox": [252, 537, 348, 560]},
	{"text": "圆肆角整", "bbox": [252, 568, 314, 583]},
	{"text": "现金支", "bbox": [250, 598, 297, 613]},
	{"text": "账户支付：0.00", "bbox": [54, 614, 176, 629]},
	{"text": "392.40", "bbox": [310, 616, 348, 636]},
	{"text": "付：", "bbox": [264, 630, 288, 644]},
	{"text": "共济支", "bbox": [249, 660, 296, 675]},
	{"text": "统筹支付：0.0", "bbox": [55, 677, 167, 691]},
	{"text": "0.0", "bbox": [309, 679, 333, 692]},
	{"text": "付：", "bbox": [263, 691, 286, 705]},
	{"text": "公补：0.0", "bbox": [65, 721, 103, 736]},
	{"text": "消费前账户余额：0.00", "bbox": [74, 743, 193, 758]},
	{"text": "消费后账户余额：0.00", "bbox": [75, 773, 193, 789]},
	{"text": "2025.12.02", "bbox": [140, 797, 225, 812]},
	{"text": "消费时间：", "bbox": [57, 813, 135, 830]},
	{"text": "10:22:36", "bbox": [140, 827, 206, 843]},
	{"text": "收款员：2103", "bbox": [246, 812, 345, 830]},
	{"text": "无购药人、个人编号、药品明细购药单无效", "bbox": [60, 847, 348, 870]}
]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.8s
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[0]: text=医疗保险定点药店收费明细, bbox=[113, 240, 325, 270]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[1]: text=辽宁天士力大药房连锁有限公司, bbox=[147, 275, 325, 300]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[2]: text=药店名称：, bbox=[60, 295, 139, 311]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[3]: text=凤城石桥路店, bbox=[147, 314, 242, 329]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[4]: text=购药人：, bbox=[68, 336, 138, 351]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[5]: text=鲁药单：1, bbox=[250, 338, 294, 353]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[6]: text=2106210151, bbox=[146, 363, 241, 377]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[7]: text=个人编号：0000001017 票据号：100189, bbox=[59, 384, 331, 402]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[8]: text=563862, bbox=[145, 417, 203, 430]
2026-08-10 11:29:45,814 INFO     29 [qwen-vl-text] coord item[9]: text=序号 药品名称 数量 金额, bbox=[74, 440, 339, 460]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[10]: text=1 沙美特罗替卡 1.0 196.20, bbox=[85, 465, 346, 493]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[11]: text=松吸入粉雾剂, bbox=[143, 480, 240, 495]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[12]: text=2 沙美特罗替卡 1.0 196.20, bbox=[85, 500, 348, 527]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[13]: text=松吸入粉雾剂, bbox=[142, 513, 240, 528]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[14]: text=总金额：392.40, bbox=[64, 551, 195, 567]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[15]: text=人民币叁佰玖拾贰, bbox=[252, 537, 348, 560]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[16]: text=圆肆角整, bbox=[252, 568, 314, 583]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[17]: text=现金支, bbox=[250, 598, 297, 613]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[18]: text=账户支付：0.00, bbox=[54, 614, 176, 629]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[19]: text=392.40, bbox=[310, 616, 348, 636]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[20]: text=付：, bbox=[264, 630, 288, 644]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[21]: text=共济支, bbox=[249, 660, 296, 675]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[22]: text=统筹支付：0.0, bbox=[55, 677, 167, 691]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[23]: text=0.0, bbox=[309, 679, 333, 692]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[24]: text=付：, bbox=[263, 691, 286, 705]
2026-08-10 11:29:45,815 INFO     29 [qwen-vl-text] coord item[25]: text=公补：0.0, bbox=[65, 721, 103, 736]
2026-08-10 11:29:45,816 INFO     29 [qwen-vl-text] coord item[26]: text=消费前账户余额：0.00, bbox=[74, 743, 193, 758]
2026-08-10 11:29:45,816 INFO     29 [qwen-vl-text] coord item[27]: text=消费后账户余额：0.00, bbox=[75, 773, 193, 789]
2026-08-10 11:29:45,816 INFO     29 [qwen-vl-text] coord item[28]: text=2025.12.02, bbox=[140, 797, 225, 812]
2026-08-10 11:29:45,816 INFO     29 [qwen-vl-text] coord item[29]: text=消费时间：, bbox=[57, 813, 135, 830]
2026-08-10 11:29:45,816 INFO     29 [qwen-vl-text] coord item[30]: text=10:22:36, bbox=[140, 827, 206, 843]
2026-08-10 11:29:45,816 INFO     29 [qwen-vl-text] coord item[31]: text=收款员：2103, bbox=[246, 812, 345, 830]
2026-08-10 11:29:45,816 INFO     29 [qwen-vl-text] coord item[32]: text=无购药人、个人编号、药品明细购药单无效, bbox=[60, 847, 348, 870]
2026-08-10 11:29:45,818 INFO     29 [qwen-vl-text] page=4 — 33/33 coords, api_time=9.8s
2026-08-10 11:29:45,818 INFO     29 [qwen-vl-text] new_positions (33):
[[4, 67.26664331054687, 193.46600952148435, 190.4880029296875, 214.29900329589844], [4, 87.50616430664061, 193.46600952148435, 218.2675033569336, 238.11000366210936], [4, 35.7168017578125, 82.74392407226561, 234.14150360107422, 246.84070379638672], [4, 87.50616430664061, 144.05776708984374, 249.2218038330078, 261.12730401611327], [4, 40.4790419921875, 82.14864404296874, 266.6832041015625, 278.588704284668], [4, 148.82000732421875, 175.01232861328123, 268.27060412597655, 280.176104309082], [4, 86.91088427734374, 143.46248706054686, 288.11310443115235, 299.2249046020508], [4, 35.121521728515624, 197.03768969726562, 304.7808046875, 319.06740490722655], [4, 86.31560424804687, 120.84184594726561, 330.972905090332, 341.29100524902344], [4, 44.05072216796874, 201.7999299316406, 349.22800537109373, 365.10200561523436], [4, 50.59880249023437, 205.96689013671875, 369.07050567626953, 391.2941060180664], [4, 85.12504418945312, 142.86720703125, 380.976005859375, 392.88150604248045], [4, 50.59880249023437, 207.1574501953125, 396.8500061035156, 418.27990643310545], [4, 84.52976416015625, 142.86720703125, 407.168106262207, 419.0736064453125], [4, 38.097921875, 116.07960571289061, 437.3287067260742, 450.0279069213867], [4, 150.0105673828125, 207.1574501953125, 426.2169065551758, 444.47200683593746], [4, 150.0105673828125, 186.91792919921875, 450.8216069335937, 462.7271071166992], [4, 148.82000732421875, 176.79816870117187, 474.6326072998047, 486.53810748291016], [4, 32.14512158203125, 104.76928515624999, 487.3318074951172, 499.23730767822263], [4, 184.53680908203123, 207.1574501953125, 488.91920751953126, 504.7932077636719], [4, 157.15392773437497, 171.4406484375, 500.0310076904297, 511.1428078613281], [4, 148.22472729492188, 176.20288867187497, 523.8420080566406, 535.7475082397461], [4, 32.740401611328124, 99.41176489257812, 537.3349082641602, 548.4467084350586], [4, 183.94152905273435, 198.22824975585937, 538.9223082885742, 549.2404084472656], [4, 156.5586477050781, 170.25008837890624, 548.4467084350586, 559.5585086059571], [4, 38.69320190429687, 61.31384301757812, 572.2577088012695, 584.1632089843749], [4, 44.05072216796874, 114.88904565429686, 589.7191090698242, 601.6246092529296], [4, 44.646002197265624, 114.88904565429686, 613.5301094360351, 626.2293096313476], [4, 83.3392041015625, 133.93800659179686, 632.5789097290038, 644.4844099121094], [4, 33.93096166992187, 80.36280395507812, 645.2781099243164, 658.771010131836], [4, 83.3392041015625, 122.62768603515624, 656.3899100952149, 669.0891102905273], [4, 146.43888720703123, 205.37161010742187, 644.4844099121094, 658.771010131836], [4, 35.7168017578125, 207.1574501953125, 672.2639103393554, 690.5190106201172]]
2026-08-10 11:29:45,819 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=13.3s
2026-08-10 11:29:45,819 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:29:45,821 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:29:45,821 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:29:45,822 INFO     29 [qwen-vl-text] positions(33): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:29:45,822 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [33]
2026-08-10 11:29:46,311 INFO     29 [qwen-vl-text] page=4, rect=595x794, img=(1654x2205), dpi=200
2026-08-10 11:29:46,312 INFO     29 [qwen-vl-text] LLM extraction start, text_len=321
2026-08-10 11:29:46,312 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:46,312 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 219, \"bbox_end\": 251, \"encounter_dates\": [\"2026-02-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "医疗保险定点药店收费明细\n辽宁天士力大药房连锁有限公司\n药店名称：\n凤城石桥路店\n购药人：\n鲁药单：1\n2106210151\n个人编号：0000001017 票据号：100246\n563862\n序号 药品名称 数量 金额\n1 沙美特罗替卡 1.0 196.20\n松吸入粉雾剂\n2 沙美特罗替卡 1.0 196.20\n松吸入粉雾剂\n总金额：392.40\n人民币叁佰玖拾贰\n圆肆角整\n现金支\n账户支付：0.00\n392.40\n付：\n共济支\n统筹支付：0.0\n0.0\n付：\n公补：0.0\n消费前账户余额：0.00\n消费后账户余额：0.00\n2026.02.01\n消费时间：\n19:49:51\n收款员：2103\n无购药人、个人编号、药品明细购药单无效",
    "role": "user"
  }
]
2026-08-10 11:29:46,314 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:29:46.313+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 22, "failed": 0, "current": {"8d2d744a94ae11f1bd9827cf206dfa2d": {"id": "8d2d744a94ae11f1bd9827cf206dfa2d", "doc_id": "8cb8165094ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3256443, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361283901, "task_type": "dataflow", "root_trace_id": "a109a49aa4f54fb6bb962f0e0599fa22", "root_traceparent": "00-a109a49aa4f54fb6bb962f0e0599fa22-2306060947da7753-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:29:49,392 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:49,392 INFO     29 [qwen-vl-text] LLM output (len=708):
{
  "encounter_date": "2026-02-01",
  "pharmacy": "辽宁天士力大药房连锁有限公司凤城石桥路店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 1.0,
      "unit_price": 196.20,
      "total_price": 196.20,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    },
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 1.0,
      "unit_price": 196.20,
      "total_price": 196.20,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 392.40,
  "payment_method": "现金支付"
}
2026-08-10 11:29:49,393 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-01]
2026-08-10 11:29:49,407 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4182181, prompt_len=1033
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["医疗保险定点药店收费明细", "辽宁天士力大药房连锁有限公司", "药店名称：", "凤城石桥路店", "购药人：", "鲁药单：1", "2106210151", "个人编号：0000001017 票据号：100246", "563862", "序号 药品名称 数量 金额", "1 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "2 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "总金额：392.40", "人民币叁佰玖拾贰", "圆肆角整", "现金支", "账户支付：0.00", "392.40", "付：", "共济支", "统筹支付：0.0", "0.0", "付：", "公补：0.0", "消费前账户余额：0.00", "消费后账户余额：0.00", "2026.02.01", "消费时间：", "19:49:51", "收款员：2103", "无购药人、个人编号、药品明细购药单无效"]

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
2026-08-10 11:29:59,739 INFO     29 [qwen-vl-text] coord API raw response (len=1762):
[
	{"text": "医疗保险定点药店收费明细", "bbox": [113, 240, 325, 270]},
	{"text": "辽宁天士力大药房连锁有限公司", "bbox": [147, 275, 325, 300]},
	{"text": "药店名称：", "bbox": [60, 295, 139, 311]},
	{"text": "凤城石桥路店", "bbox": [147, 314, 242, 329]},
	{"text": "购药人：", "bbox": [68, 336, 138, 351]},
	{"text": "鲁药单：1", "bbox": [250, 338, 293, 353]},
	{"text": "2106210151", "bbox": [146, 363, 240, 377]},
	{"text": "个人编号：0000001017 票据号：100189", "bbox": [59, 385, 330, 402]},
	{"text": "563862", "bbox": [145, 418, 202, 430]},
	{"text": "序号 药品名称 数量 金额", "bbox": [74, 441, 338, 460]},
	{"text": "1 沙美特罗替卡 1.0 196.20", "bbox": [85, 465, 345, 493]},
	{"text": "松吸入粉雾剂", "bbox": [143, 480, 240, 495]},
	{"text": "2 沙美特罗替卡 1.0 196.20", "bbox": [85, 502, 348, 528]},
	{"text": "松吸入粉雾剂", "bbox": [143, 514, 240, 528]},
	{"text": "总金额：392.40", "bbox": [64, 552, 194, 567]},
	{"text": "人民币叁佰玖拾贰", "bbox": [252, 537, 347, 560]},
	{"text": "圆肆角整", "bbox": [252, 568, 313, 583]},
	{"text": "现金支", "bbox": [250, 598, 297, 613]},
	{"text": "账户支付：0.00", "bbox": [53, 615, 175, 629]},
	{"text": "392.40", "bbox": [310, 617, 347, 635]},
	{"text": "付：", "bbox": [264, 630, 287, 644]},
	{"text": "共济支", "bbox": [249, 660, 295, 675]},
	{"text": "统筹支付：0.0", "bbox": [55, 677, 166, 690]},
	{"text": "0.0", "bbox": [309, 679, 333, 691]},
	{"text": "付：", "bbox": [264, 691, 285, 705]},
	{"text": "公补：0.0", "bbox": [65, 722, 102, 735]},
	{"text": "消费前账户余额：0.00", "bbox": [74, 744, 192, 758]},
	{"text": "消费后账户余额：0.00", "bbox": [75, 774, 192, 788]},
	{"text": "2025.12.02", "bbox": [140, 797, 225, 811]},
	{"text": "消费时间：", "bbox": [57, 813, 135, 829]},
	{"text": "10:22:36", "bbox": [140, 828, 205, 842]},
	{"text": "收款员：2103", "bbox": [246, 813, 344, 829]},
	{"text": "无购药人、个人编号、药品明细购药单无效", "bbox": [60, 848, 348, 869]}
]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=10.3s
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[0]: text=医疗保险定点药店收费明细, bbox=[113, 240, 325, 270]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[1]: text=辽宁天士力大药房连锁有限公司, bbox=[147, 275, 325, 300]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[2]: text=药店名称：, bbox=[60, 295, 139, 311]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[3]: text=凤城石桥路店, bbox=[147, 314, 242, 329]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[4]: text=购药人：, bbox=[68, 336, 138, 351]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[5]: text=鲁药单：1, bbox=[250, 338, 293, 353]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[6]: text=2106210151, bbox=[146, 363, 240, 377]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[7]: text=个人编号：0000001017 票据号：100189, bbox=[59, 385, 330, 402]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[8]: text=563862, bbox=[145, 418, 202, 430]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[9]: text=序号 药品名称 数量 金额, bbox=[74, 441, 338, 460]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[10]: text=1 沙美特罗替卡 1.0 196.20, bbox=[85, 465, 345, 493]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[11]: text=松吸入粉雾剂, bbox=[143, 480, 240, 495]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[12]: text=2 沙美特罗替卡 1.0 196.20, bbox=[85, 502, 348, 528]
2026-08-10 11:29:59,740 INFO     29 [qwen-vl-text] coord item[13]: text=松吸入粉雾剂, bbox=[143, 514, 240, 528]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[14]: text=总金额：392.40, bbox=[64, 552, 194, 567]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[15]: text=人民币叁佰玖拾贰, bbox=[252, 537, 347, 560]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[16]: text=圆肆角整, bbox=[252, 568, 313, 583]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[17]: text=现金支, bbox=[250, 598, 297, 613]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[18]: text=账户支付：0.00, bbox=[53, 615, 175, 629]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[19]: text=392.40, bbox=[310, 617, 347, 635]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[20]: text=付：, bbox=[264, 630, 287, 644]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[21]: text=共济支, bbox=[249, 660, 295, 675]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[22]: text=统筹支付：0.0, bbox=[55, 677, 166, 690]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[23]: text=0.0, bbox=[309, 679, 333, 691]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[24]: text=付：, bbox=[264, 691, 285, 705]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[25]: text=公补：0.0, bbox=[65, 722, 102, 735]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[26]: text=消费前账户余额：0.00, bbox=[74, 744, 192, 758]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[27]: text=消费后账户余额：0.00, bbox=[75, 774, 192, 788]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[28]: text=2025.12.02, bbox=[140, 797, 225, 811]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[29]: text=消费时间：, bbox=[57, 813, 135, 829]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[30]: text=10:22:36, bbox=[140, 828, 205, 842]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[31]: text=收款员：2103, bbox=[246, 813, 344, 829]
2026-08-10 11:29:59,741 INFO     29 [qwen-vl-text] coord item[32]: text=无购药人、个人编号、药品明细购药单无效, bbox=[60, 848, 348, 869]
2026-08-10 11:29:59,743 INFO     29 [qwen-vl-text] page=4 — 33/33 coords, api_time=10.3s
2026-08-10 11:29:59,743 INFO     29 [qwen-vl-text] new_positions (33):
[[4, 67.26664331054687, 193.46600952148435, 190.4880029296875, 214.29900329589844], [4, 87.50616430664061, 193.46600952148435, 218.2675033569336, 238.11000366210936], [4, 35.7168017578125, 82.74392407226561, 234.14150360107422, 246.84070379638672], [4, 87.50616430664061, 144.05776708984374, 249.2218038330078, 261.12730401611327], [4, 40.4790419921875, 82.14864404296874, 266.6832041015625, 278.588704284668], [4, 148.82000732421875, 174.41704858398435, 268.27060412597655, 280.176104309082], [4, 86.91088427734374, 142.86720703125, 288.11310443115235, 299.2249046020508], [4, 35.121521728515624, 196.44240966796875, 305.574504699707, 319.06740490722655], [4, 86.31560424804687, 120.24656591796874, 331.7666051025391, 341.29100524902344], [4, 44.05072216796874, 201.20464990234373, 350.0217053833008, 365.10200561523436], [4, 50.59880249023437, 205.37161010742187, 369.07050567626953, 391.2941060180664], [4, 85.12504418945312, 142.86720703125, 380.976005859375, 392.88150604248045], [4, 50.59880249023437, 207.1574501953125, 398.4374061279297, 419.0736064453125], [4, 85.12504418945312, 142.86720703125, 407.9618062744141, 419.0736064453125], [4, 38.097921875, 115.48432568359374, 438.12240673828126, 450.0279069213867], [4, 150.0105673828125, 206.56217016601562, 426.2169065551758, 444.47200683593746], [4, 150.0105673828125, 186.32264916992187, 450.8216069335937, 462.7271071166992], [4, 148.82000732421875, 176.79816870117187, 474.6326072998047, 486.53810748291016], [4, 31.54984155273437, 104.17400512695312, 488.1255075073242, 499.23730767822263], [4, 184.53680908203123, 206.56217016601562, 489.71290753173827, 503.9995077514648], [4, 157.15392773437497, 170.84536840820311, 500.0310076904297, 511.1428078613281], [4, 148.22472729492188, 175.6076086425781, 523.8420080566406, 535.7475082397461], [4, 32.740401611328124, 98.81648486328125, 537.3349082641602, 547.6530084228516], [4, 183.94152905273435, 198.22824975585937, 538.9223082885742, 548.4467084350586], [4, 157.15392773437497, 169.65480834960937, 548.4467084350586, 559.5585086059571], [4, 38.69320190429687, 60.71856298828125, 573.0514088134765, 583.369508972168], [4, 44.05072216796874, 114.29376562499999, 590.5128090820313, 601.6246092529296], [4, 44.646002197265624, 114.29376562499999, 614.3238094482422, 625.4356096191406], [4, 83.3392041015625, 133.93800659179686, 632.5789097290038, 643.6907098999023], [4, 33.93096166992187, 80.36280395507812, 645.2781099243164, 657.9773101196289], [4, 83.3392041015625, 122.03240600585937, 657.1836101074218, 668.2954102783203], [4, 146.43888720703123, 204.776330078125, 645.2781099243164, 657.9773101196289], [4, 35.7168017578125, 207.1574501953125, 673.0576103515625, 689.7253106079102]]
2026-08-10 11:29:59,744 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=13.9s
2026-08-10 11:29:59,756 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 11:29:59,756 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Medication | outputs={"chunks": "3 items, types={'MedicationRecord': 3}", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:29:59,757 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 11:29:59,767 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:29:59,767 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:30:00,646 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:00,655 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:30:00,655 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:30:00,655 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:30:00,665 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:30:00,666 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:30:00,666 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 11:30:00,666 INFO     29 [qwen-vl-text] positions(99): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:30:00,666 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [99]
2026-08-10 11:30:00,913 INFO     29 [qwen-vl-text] page=0, rect=595x870, img=(1654x2418), dpi=200
2026-08-10 11:30:00,914 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1128
2026-08-10 11:30:00,914 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:00,914 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 0, \"bbox_end\": 98, \"encounter_dates\": [\"2024-10-08\", \"2024-10-15\"], \"department\": \"内四科病房\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "信4个月\n医疗机构：凤城市中医院\n(组织机构代码：46376203-6)\n医疗付费方式：城镇医保\n中医住院病案首页\n02410974\n健康卡号：\n第3次入院\n病案号：290510\n姓名：\n性别：1.男2.女出生日期：1958-12-09\n年龄：65岁\n国籍：中国\n(年龄不足一周岁的)年龄：\n新生儿出生体重：\n克\n新生儿入院体重：\n克\n出生地点：辽宁省凤城市\n籍贯：辽宁省\n民族：汉族\n身份证号：\n职业：退(离)休人\n婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他\n现地址：凤城市胜利委十组060644\n邮编：118100\n户口地址：凤城市胜利委十组060644\n邮编：118100\n工作单位：电业局\n邮编：118100\n联系人姓名：李治刚\n关系：本人或户\n地址：凤城市胜利委十组060644\n9\n入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他\n治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医\n入院时间：2024-10-08\n入院科别：内四科病房\n病房：11\n转科科别：\n出院时间：2024-10-15\n出院科别：内四科病房\n病房：\n实际住院：7 天\n门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)\n疾病编码：A04.04.04.02,A04.04.04.02\n门(急)诊诊断(西医诊断)：肺部感染\n疾病编码：J98.414\n实施临床路径：3 1.中医2.西医3否\n使用医疗机构中药制剂：2 1.是2.否\n使用中医诊疗设备：1 1.是2.否\n使用中医诊疗技术：1 1.是2.否\n辨证施护：1 1.是2.否\n出院中医诊断\n疾病编码\n入院\n病情\n出院西医诊断\n疾病编码\n入院\n病情\n主病：喘病(可选词：喘证)\nA04.04.04.02\n1\n主要诊断：支气管哮喘\nJ45.900x001\n1\n主证：风寒袭肺证\n1\n其他诊断：冠状动脉粥样硬化性心脏\nI25.103\n1\n其他诊断：心功能II级(NYHA分级)\nI50.900x007\n1\n其他诊断：特应性神经性皮炎\nL20.803\n1\n入院病情：1.有，2.临床未确定，3.情况不明，4.无\n损伤、中毒的外部原因：\n疾病编码：\n病理诊断：\n疾病编码：\n病理号：\n药物过敏：1 1.无2.有过敏药物：\n死亡患者尸检：2 1.是2.否\n血型：□ 1.A 2.B 3.O 4.AB 5.不详 6.未查\nRh 4 1.阴2.阳3.不详4.未查\n科主任：李革\n主任(副主任)医师：李革\n主治医师：宋文平\n住院医师：刘彦\n责任护士：唐莹莹\n进修医师：\n实习医师：\n编码员：\n病案质量 1 1.甲2.乙3.丙质控医师：刘彦\n质控护士：杨\n质控日期：2024-10-17",
    "role": "user"
  }
]
2026-08-10 11:30:05,467 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:05,467 INFO     29 [qwen-vl-text] LLM output (len=1297):
{
  "encounter_date": "2024-10-15",
  "admission_date": "2024-10-08",
  "discharge_date": "2024-10-15",
  "hospital_days": 7,
  "department": "内四科病房",
  "bed_number": "11",
  "admission_condition": null,
  "admission_diagnoses": [
    {
      "name": "喘病",
      "diagnosis_type": "中医"
    },
    {
      "name": "肺部感染",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": null,
  "auxiliary_exams": null,
  "imaging_findings": null,
  "discharge_diagnoses": [
    {
      "name": "喘病",
      "diagnosis_type": "中医"
    },
    {
      "name": "风寒袭肺证",
      "diagnosis_type": "中医"
    },
    {
      "name": "支气管哮喘",
      "diagnosis_type": "西医"
    },
    {
      "name": "冠状动脉粥样硬化性心脏病",
      "diagnosis_type": "西医"
    },
    {
      "name": "心功能II级(NYHA分级)",
      "diagnosis_type": "西医"
    },
    {
      "name": "特应性神经性皮炎",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": null,
  "outcome": null,
  "discharge_orders": null,
  "do_medications": [],
  "do_follow_up": null,
  "do_precautions": [],
  "next_treatment_date": null,
  "attending_physician": "宋文平",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 11:30:05,467 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-10-15]
2026-08-10 11:30:05,473 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2465600, prompt_len=2038
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共99行）
["信4个月", "医疗机构：凤城市中医院", "(组织机构代码：46376203-6)", "医疗付费方式：城镇医保", "中医住院病案首页", "02410974", "健康卡号：", "第3次入院", "病案号：290510", "姓名：", "性别：1.男2.女出生日期：1958-12-09", "年龄：65岁", "国籍：中国", "(年龄不足一周岁的)年龄：", "新生儿出生体重：", "克", "新生儿入院体重：", "克", "出生地点：辽宁省凤城市", "籍贯：辽宁省", "民族：汉族", "身份证号：", "职业：退(离)休人", "婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他", "现地址：凤城市胜利委十组060644", "邮编：118100", "户口地址：凤城市胜利委十组060644", "邮编：118100", "工作单位：电业局", "邮编：118100", "联系人姓名：李治刚", "关系：本人或户", "地址：凤城市胜利委十组060644", "9", "入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他", "治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医", "入院时间：2024-10-08", "入院科别：内四科病房", "病房：11", "转科科别：", "出院时间：2024-10-15", "出院科别：内四科病房", "病房：", "实际住院：7 天", "门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)", "疾病编码：A04.04.04.02,A04.04.04.02", "门(急)诊诊断(西医诊断)：肺部感染", "疾病编码：J98.414", "实施临床路径：3 1.中医2.西医3否", "使用医疗机构中药制剂：2 1.是2.否", "使用中医诊疗设备：1 1.是2.否", "使用中医诊疗技术：1 1.是2.否", "辨证施护：1 1.是2.否", "出院中医诊断", "疾病编码", "入院", "病情", "出院西医诊断", "疾病编码", "入院", "病情", "主病：喘病(可选词：喘证)", "A04.04.04.02", "1", "主要诊断：支气管哮喘", "J45.900x001", "1", "主证：风寒袭肺证", "1", "其他诊断：冠状动脉粥样硬化性心脏", "I25.103", "1", "其他诊断：心功能II级(NYHA分级)", "I50.900x007", "1", "其他诊断：特应性神经性皮炎", "L20.803", "1", "入院病情：1.有，2.临床未确定，3.情况不明，4.无", "损伤、中毒的外部原因：", "疾病编码：", "病理诊断：", "疾病编码：", "病理号：", "药物过敏：1 1.无2.有过敏药物：", "死亡患者尸检：2 1.是2.否", "血型：□ 1.A 2.B 3.O 4.AB 5.不详 6.未查", "Rh 4 1.阴2.阳3.不详4.未查", "科主任：李革", "主任(副主任)医师：李革", "主治医师：宋文平", "住院医师：刘彦", "责任护士：唐莹莹", "进修医师：", "实习医师：", "编码员：", "病案质量 1 1.甲2.乙3.丙质控医师：刘彦", "质控护士：杨", "质控日期：2024-10-17"]

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
2026-08-10 11:30:34,456 INFO     29 [qwen-vl-text] coord API raw response (len=5454):
[
	{"text": "信4个月", "bbox": [100, 33, 206, 67]},
	{"text": "医疗机构：凤城市中医院", "bbox": [277, 63, 466, 74]},
	{"text": "(组织机构代码：46376203-6)", "bbox": [617, 58, 848, 70]},
	{"text": "医疗付费方式：城镇医保", "bbox": [116, 84, 270, 98]},
	{"text": "中医住院病案首页", "bbox": [377, 82, 627, 96]},
	{"text": "02410974", "bbox": [721, 74, 863, 92]},
	{"text": "健康卡号：", "bbox": [112, 100, 174, 110]},
	{"text": "第3次入院", "bbox": [456, 104, 534, 114]},
	{"text": "病案号：290510", "bbox": [690, 103, 786, 113]},
	{"text": "姓名：", "bbox": [109, 117, 144, 127]},
	{"text": "性别：1.男2.女出生日期：1958-12-09", "bbox": [292, 119, 562, 130]},
	{"text": "年龄：65岁", "bbox": [631, 120, 695, 130]},
	{"text": "国籍：中国", "bbox": [736, 120, 804, 130]},
	{"text": "(年龄不足一周岁的)年龄：", "bbox": [148, 133, 320, 144]},
	{"text": "新生儿出生体重：", "bbox": [413, 136, 517, 145]},
	{"text": "克", "bbox": [594, 136, 610, 145]},
	{"text": "新生儿入院体重：", "bbox": [634, 136, 736, 146]},
	{"text": "克", "bbox": [838, 134, 853, 144]},
	{"text": "出生地点：辽宁省凤城市", "bbox": [106, 146, 262, 157]},
	{"text": "籍贯：辽宁省", "bbox": [532, 150, 610, 160]},
	{"text": "民族：汉族", "bbox": [718, 151, 791, 161]},
	{"text": "身份证号：", "bbox": [105, 161, 168, 171]},
	{"text": "职业：退(离)休人", "bbox": [394, 164, 500, 174]},
	{"text": "婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他", "bbox": [531, 165, 840, 176]},
	{"text": "现地址：凤城市胜利委十组060644", "bbox": [101, 176, 318, 188]},
	{"text": "邮编：118100", "bbox": [720, 181, 800, 190]},
	{"text": "户口地址：凤城市胜利委十组060644", "bbox": [98, 190, 331, 201]},
	{"text": "邮编：118100", "bbox": [720, 196, 804, 205]},
	{"text": "工作单位：电业局", "bbox": [97, 203, 213, 214]},
	{"text": "邮编：118100", "bbox": [721, 210, 804, 219]},
	{"text": "联系人姓名：李治刚", "bbox": [93, 218, 223, 230]},
	{"text": "关系：本人或户", "bbox": [338, 221, 437, 232]},
	{"text": "地址：凤城市胜利委十组060644", "bbox": [470, 222, 680, 233]},
	{"text": "9", "bbox": [827, 223, 841, 232]},
	{"text": "入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他", "bbox": [90, 233, 477, 247]},
	{"text": "治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医", "bbox": [505, 236, 882, 248]},
	{"text": "入院时间：2024-10-08", "bbox": [87, 248, 235, 260]},
	{"text": "入院科别：内四科病房", "bbox": [332, 251, 474, 262]},
	{"text": "病房：11", "bbox": [553, 252, 604, 263]},
	{"text": "转科科别：", "bbox": [721, 254, 810, 265]},
	{"text": "出院时间：2024-10-15", "bbox": [85, 262, 235, 274]},
	{"text": "出院科别：内四科病房", "bbox": [330, 265, 473, 276]},
	{"text": "病房：", "bbox": [553, 265, 604, 276]},
	{"text": "实际住院：7 天", "bbox": [722, 266, 878, 277]},
	{"text": "门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)", "bbox": [83, 275, 553, 288]},
	{"text": "疾病编码：A04.04.04.02,A04.04.04.02", "bbox": [583, 280, 835, 291]},
	{"text": "门(急)诊诊断(西医诊断)：肺部感染", "bbox": [80, 290, 322, 302]},
	{"text": "疾病编码：J98.414", "bbox": [583, 294, 702, 305]},
	{"text": "实施临床路径：3 1.中医2.西医3否", "bbox": [112, 307, 420, 321]},
	{"text": "使用医疗机构中药制剂：2 1.是2.否", "bbox": [496, 310, 760, 324]},
	{"text": "使用中医诊疗设备：1 1.是2.否", "bbox": [80, 325, 320, 339]},
	{"text": "使用中医诊疗技术：1 1.是2.否", "bbox": [371, 327, 604, 340]},
	{"text": "辨证施护：1 1.是2.否", "bbox": [715, 329, 888, 342]},
	{"text": "出院中医诊断", "bbox": [162, 346, 254, 358]},
	{"text": "疾病编码", "bbox": [374, 348, 437, 359]},
	{"text": "入院", "bbox": [461, 343, 493, 355]},
	{"text": "病情", "bbox": [461, 354, 493, 365]},
	{"text": "出院西医诊断", "bbox": [579, 349, 668, 360]},
	{"text": "疾病编码", "bbox": [768, 350, 829, 361]},
	{"text": "入院", "bbox": [855, 346, 887, 358]},
	{"text": "病情", "bbox": [855, 357, 887, 368]},
	{"text": "主病：喘病(可选词：喘证)", "bbox": [62, 367, 249, 380]},
	{"text": "A04.04.04.02", "bbox": [358, 370, 454, 381]},
	{"text": "1", "bbox": [458, 370, 468, 381]},
	{"text": "主要诊断：支气管哮喘", "bbox": [504, 370, 645, 382]},
	{"text": "J45.900x001", "bbox": [754, 372, 840, 383]},
	{"text": "1", "bbox": [857, 373, 866, 383]},
	{"text": "主证：风寒袭肺证", "bbox": [58, 387, 176, 399]},
	{"text": "1", "bbox": [458, 390, 468, 400]},
	{"text": "其他诊断：冠状动脉粥样硬化性心脏", "bbox": [504, 390, 738, 403]},
	{"text": "I25.103", "bbox": [755, 392, 810, 403]},
	{"text": "1", "bbox": [858, 393, 867, 403]},
	{"text": "其他诊断：心功能II级(NYHA分级)", "bbox": [504, 409, 722, 421]},
	{"text": "I50.900x007", "bbox": [757, 411, 844, 422]},
	{"text": "1", "bbox": [860, 412, 869, 422]},
	{"text": "其他诊断：特应性神经性皮炎", "bbox": [504, 428, 694, 440]},
	{"text": "L20.803", "bbox": [758, 430, 815, 441]},
	{"text": "1", "bbox": [863, 431, 872, 441]},
	{"text": "入院病情：1.有，2.临床未确定，3.情况不明，4.无", "bbox": [14, 600, 405, 614]},
	{"text": "损伤、中毒的外部原因：", "bbox": [45, 627, 241, 641]},
	{"text": "疾病编码：", "bbox": [701, 629, 796, 643]},
	{"text": "病理诊断：", "bbox": [45, 652, 142, 666]},
	{"text": "疾病编码：", "bbox": [39, 673, 138, 687]},
	{"text": "病理号：", "bbox": [448, 674, 530, 688]},
	{"text": "药物过敏：1 1.无2.有过敏药物：", "bbox": [32, 698, 347, 714]},
	{"text": "死亡患者尸检：2 1.是2.否", "bbox": [709, 702, 938, 719]},
	{"text": "血型：□ 1.A 2.B 3.O 4.AB 5.不详 6.未查", "bbox": [27, 727, 437, 744]},
	{"text": "Rh 4 1.阴2.阳3.不详4.未查", "bbox": [554, 727, 828, 745]},
	{"text": "科主任：李革", "bbox": [22, 755, 122, 772]},
	{"text": "主任(副主任)医师：李革", "bbox": [240, 756, 432, 773]},
	{"text": "主治医师：宋文平", "bbox": [552, 756, 688, 773]},
	{"text": "住院医师：刘彦", "bbox": [770, 756, 890, 775]},
	{"text": "责任护士：唐莹莹", "bbox": [18, 781, 150, 798]},
	{"text": "进修医师：", "bbox": [309, 783, 412, 800]},
	{"text": "实习医师：", "bbox": [552, 783, 654, 800]},
	{"text": "编码员：", "bbox": [789, 786, 851, 801]},
	{"text": "病案质量 1 1.甲2.乙3.丙质控医师：刘彦", "bbox": [2, 810, 387, 830]},
	{"text": "质控护士：杨", "bbox": [477, 813, 622, 832]},
	{"text": "质控日期：2024-10-17", "bbox": [720, 817, 910, 833]}
]
2026-08-10 11:30:34,457 INFO     29 [qwen-vl-text] coord API: raw_items=99, valid_items=99, elapsed=29.0s
2026-08-10 11:30:34,457 INFO     29 [qwen-vl-text] coord item[0]: text=信4个月, bbox=[100, 33, 206, 67]
2026-08-10 11:30:34,457 INFO     29 [qwen-vl-text] coord item[1]: text=医疗机构：凤城市中医院, bbox=[277, 63, 466, 74]
2026-08-10 11:30:34,457 INFO     29 [qwen-vl-text] coord item[2]: text=(组织机构代码：46376203-6), bbox=[617, 58, 848, 70]
2026-08-10 11:30:34,457 INFO     29 [qwen-vl-text] coord item[3]: text=医疗付费方式：城镇医保, bbox=[116, 84, 270, 98]
2026-08-10 11:30:34,457 INFO     29 [qwen-vl-text] coord item[4]: text=中医住院病案首页, bbox=[377, 82, 627, 96]
2026-08-10 11:30:34,457 INFO     29 [qwen-vl-text] coord item[5]: text=02410974, bbox=[721, 74, 863, 92]
2026-08-10 11:30:34,457 INFO     29 [qwen-vl-text] coord item[6]: text=健康卡号：, bbox=[112, 100, 174, 110]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[7]: text=第3次入院, bbox=[456, 104, 534, 114]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[8]: text=病案号：290510, bbox=[690, 103, 786, 113]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[9]: text=姓名：, bbox=[109, 117, 144, 127]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[10]: text=性别：1.男2.女出生日期：1958-12-09, bbox=[292, 119, 562, 130]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[11]: text=年龄：65岁, bbox=[631, 120, 695, 130]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[12]: text=国籍：中国, bbox=[736, 120, 804, 130]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[13]: text=(年龄不足一周岁的)年龄：, bbox=[148, 133, 320, 144]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[14]: text=新生儿出生体重：, bbox=[413, 136, 517, 145]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[15]: text=克, bbox=[594, 136, 610, 145]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[16]: text=新生儿入院体重：, bbox=[634, 136, 736, 146]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[17]: text=克, bbox=[838, 134, 853, 144]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[18]: text=出生地点：辽宁省凤城市, bbox=[106, 146, 262, 157]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[19]: text=籍贯：辽宁省, bbox=[532, 150, 610, 160]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[20]: text=民族：汉族, bbox=[718, 151, 791, 161]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[21]: text=身份证号：, bbox=[105, 161, 168, 171]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[22]: text=职业：退(离)休人, bbox=[394, 164, 500, 174]
2026-08-10 11:30:34,458 INFO     29 [qwen-vl-text] coord item[23]: text=婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他, bbox=[531, 165, 840, 176]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[24]: text=现地址：凤城市胜利委十组060644, bbox=[101, 176, 318, 188]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[25]: text=邮编：118100, bbox=[720, 181, 800, 190]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[26]: text=户口地址：凤城市胜利委十组060644, bbox=[98, 190, 331, 201]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[27]: text=邮编：118100, bbox=[720, 196, 804, 205]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[28]: text=工作单位：电业局, bbox=[97, 203, 213, 214]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[29]: text=邮编：118100, bbox=[721, 210, 804, 219]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[30]: text=联系人姓名：李治刚, bbox=[93, 218, 223, 230]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[31]: text=关系：本人或户, bbox=[338, 221, 437, 232]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[32]: text=地址：凤城市胜利委十组060644, bbox=[470, 222, 680, 233]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[33]: text=9, bbox=[827, 223, 841, 232]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[34]: text=入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他, bbox=[90, 233, 477, 247]
2026-08-10 11:30:34,459 INFO     29 [qwen-vl-text] coord item[35]: text=治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医, bbox=[505, 236, 882, 248]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[36]: text=入院时间：2024-10-08, bbox=[87, 248, 235, 260]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[37]: text=入院科别：内四科病房, bbox=[332, 251, 474, 262]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[38]: text=病房：11, bbox=[553, 252, 604, 263]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[39]: text=转科科别：, bbox=[721, 254, 810, 265]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[40]: text=出院时间：2024-10-15, bbox=[85, 262, 235, 274]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[41]: text=出院科别：内四科病房, bbox=[330, 265, 473, 276]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[42]: text=病房：, bbox=[553, 265, 604, 276]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[43]: text=实际住院：7 天, bbox=[722, 266, 878, 277]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[44]: text=门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证), bbox=[83, 275, 553, 288]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[45]: text=疾病编码：A04.04.04.02,A04.04.04.02, bbox=[583, 280, 835, 291]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[46]: text=门(急)诊诊断(西医诊断)：肺部感染, bbox=[80, 290, 322, 302]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[47]: text=疾病编码：J98.414, bbox=[583, 294, 702, 305]
2026-08-10 11:30:34,460 INFO     29 [qwen-vl-text] coord item[48]: text=实施临床路径：3 1.中医2.西医3否, bbox=[112, 307, 420, 321]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[49]: text=使用医疗机构中药制剂：2 1.是2.否, bbox=[496, 310, 760, 324]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[50]: text=使用中医诊疗设备：1 1.是2.否, bbox=[80, 325, 320, 339]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[51]: text=使用中医诊疗技术：1 1.是2.否, bbox=[371, 327, 604, 340]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[52]: text=辨证施护：1 1.是2.否, bbox=[715, 329, 888, 342]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[53]: text=出院中医诊断, bbox=[162, 346, 254, 358]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[54]: text=疾病编码, bbox=[374, 348, 437, 359]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[55]: text=入院, bbox=[461, 343, 493, 355]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[56]: text=病情, bbox=[461, 354, 493, 365]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[57]: text=出院西医诊断, bbox=[579, 349, 668, 360]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[58]: text=疾病编码, bbox=[768, 350, 829, 361]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[59]: text=入院, bbox=[855, 346, 887, 358]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[60]: text=病情, bbox=[855, 357, 887, 368]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[61]: text=主病：喘病(可选词：喘证), bbox=[62, 367, 249, 380]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[62]: text=A04.04.04.02, bbox=[358, 370, 454, 381]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[63]: text=1, bbox=[458, 370, 468, 381]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[64]: text=主要诊断：支气管哮喘, bbox=[504, 370, 645, 382]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[65]: text=J45.900x001, bbox=[754, 372, 840, 383]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[66]: text=1, bbox=[857, 373, 866, 383]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[67]: text=主证：风寒袭肺证, bbox=[58, 387, 176, 399]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[68]: text=1, bbox=[458, 390, 468, 400]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[69]: text=其他诊断：冠状动脉粥样硬化性心脏, bbox=[504, 390, 738, 403]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[70]: text=I25.103, bbox=[755, 392, 810, 403]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[71]: text=1, bbox=[858, 393, 867, 403]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[72]: text=其他诊断：心功能II级(NYHA分级), bbox=[504, 409, 722, 421]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[73]: text=I50.900x007, bbox=[757, 411, 844, 422]
2026-08-10 11:30:34,461 INFO     29 [qwen-vl-text] coord item[74]: text=1, bbox=[860, 412, 869, 422]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[75]: text=其他诊断：特应性神经性皮炎, bbox=[504, 428, 694, 440]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[76]: text=L20.803, bbox=[758, 430, 815, 441]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[77]: text=1, bbox=[863, 431, 872, 441]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[78]: text=入院病情：1.有，2.临床未确定，3.情况不明，4.无, bbox=[14, 600, 405, 614]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[79]: text=损伤、中毒的外部原因：, bbox=[45, 627, 241, 641]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[80]: text=疾病编码：, bbox=[701, 629, 796, 643]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[81]: text=病理诊断：, bbox=[45, 652, 142, 666]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[82]: text=疾病编码：, bbox=[39, 673, 138, 687]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[83]: text=病理号：, bbox=[448, 674, 530, 688]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[84]: text=药物过敏：1 1.无2.有过敏药物：, bbox=[32, 698, 347, 714]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[85]: text=死亡患者尸检：2 1.是2.否, bbox=[709, 702, 938, 719]
2026-08-10 11:30:34,462 INFO     29 [qwen-vl-text] coord item[86]: text=血型：□ 1.A 2.B 3.O 4.AB 5.不详 6.未查, bbox=[27, 727, 437, 744]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[87]: text=Rh 4 1.阴2.阳3.不详4.未查, bbox=[554, 727, 828, 745]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[88]: text=科主任：李革, bbox=[22, 755, 122, 772]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[89]: text=主任(副主任)医师：李革, bbox=[240, 756, 432, 773]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[90]: text=主治医师：宋文平, bbox=[552, 756, 688, 773]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[91]: text=住院医师：刘彦, bbox=[770, 756, 890, 775]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[92]: text=责任护士：唐莹莹, bbox=[18, 781, 150, 798]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[93]: text=进修医师：, bbox=[309, 783, 412, 800]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[94]: text=实习医师：, bbox=[552, 783, 654, 800]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[95]: text=编码员：, bbox=[789, 786, 851, 801]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[96]: text=病案质量 1 1.甲2.乙3.丙质控医师：刘彦, bbox=[2, 810, 387, 830]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[97]: text=质控护士：杨, bbox=[477, 813, 622, 832]
2026-08-10 11:30:34,463 INFO     29 [qwen-vl-text] coord item[98]: text=质控日期：2024-10-17, bbox=[720, 817, 910, 833]
2026-08-10 11:30:34,464 INFO     29 [qwen-vl-text] page=0 — 99/99 coords, api_time=29.0s
2026-08-10 11:30:34,465 INFO     29 [qwen-vl-text] new_positions (99):
[[0, 59.528002929687496, 122.62768603515624, 28.720560241699218, 58.31144049072266], [0, 164.89256811523435, 277.40049365234376, 54.830160461425784, 64.40368054199219], [0, 367.28777807617183, 504.79746484374994, 50.47856042480469, 60.92240051269531], [0, 69.05248339843749, 160.72560791015624, 73.10688061523437, 85.29136071777344], [0, 224.42057104492187, 373.2405783691406, 71.36624060058594, 83.550720703125], [0, 429.19690112304687, 513.726665283203, 64.40368054199219, 80.06944067382813], [0, 66.67136328125, 103.57872509765625, 87.03200073242188, 95.73520080566406], [0, 271.44769335937497, 317.87953564453124, 90.51328076171875, 99.21648083496093], [0, 410.74322021484375, 467.89010302734374, 89.64296075439454, 98.34616082763672], [0, 64.88552319335938, 85.72032421875, 101.82744085693359, 110.53064093017578], [0, 173.82176855468748, 334.54737646484375, 103.56808087158204, 113.14160095214844], [0, 375.6216984863281, 413.7196203613281, 104.43840087890625, 113.14160095214844], [0, 438.12610156249997, 478.60514355468746, 104.43840087890625, 113.14160095214844], [0, 88.10144433593749, 190.489609375, 115.7525609741211, 125.3260810546875], [0, 245.85065209960936, 307.75977514648434, 118.36352099609375, 126.19640106201172], [0, 353.59633740234375, 363.1208178710937, 118.36352099609375, 126.19640106201172], [0, 377.40753857421873, 438.12610156249997, 118.36352099609375, 127.06672106933594], [0, 498.8446645507812, 507.77386499023436, 116.62288098144532, 125.3260810546875], [0, 63.09968310546874, 155.96336767578123, 127.06672106933594, 136.64024114990235], [0, 316.6889755859375, 363.1208178710937, 130.54800109863282, 139.251201171875], [0, 427.4110610351562, 470.8665031738281, 131.41832110595703, 140.12152117919922], [0, 62.50440307617187, 100.00704492187499, 140.12152117919922, 148.8247212524414], [0, 234.54033154296874, 297.6400146484375, 142.73248120117188, 151.43568127441407], [0, 316.0936955566406, 500.03522460937495, 143.6028012084961, 153.1763212890625], [0, 60.12328295898437, 189.29904931640624, 153.1763212890625, 163.62016137695312], [0, 428.60162109374994, 476.22402343749997, 157.5279213256836, 165.36080139160157], [0, 58.33744287109374, 197.03768969726562, 165.36080139160157, 174.93432147216797], [0, 428.60162109374994, 478.60514355468746, 170.5827214355469, 178.41560150146483], [0, 57.74216284179687, 126.79464624023437, 176.67496148681641, 186.2484815673828], [0, 429.19690112304687, 478.60514355468746, 182.76720153808594, 190.60008160400392], [0, 55.36104272460937, 132.74744653320312, 189.72976159667968, 200.17360168457031], [0, 201.20464990234373, 260.1373728027344, 192.34072161865234, 201.91424169921876], [0, 279.78161376953125, 404.79041992187496, 193.21104162597658, 202.78456170654297], [0, 492.2965842285156, 500.6305046386718, 194.0813616333008, 201.91424169921876], [0, 53.57520263671874, 283.94857397460936, 202.78456170654297, 214.96904180908203], [0, 300.61641479492187, 525.0369858398437, 205.39552172851563, 215.83936181640627], [0, 51.78936254882812, 139.89080688476562, 215.83936181640627, 226.28320190429687], [0, 197.6329697265625, 282.16273388671874, 218.4503218383789, 228.02384191894532], [0, 329.18985620117184, 359.5491376953125, 219.32064184570314, 228.89416192626953], [0, 429.19690112304687, 482.1768237304687, 221.06128186035156, 230.63480194091798], [0, 50.59880249023437, 139.89080688476562, 228.02384191894532, 238.46768200683593], [0, 196.44240966796875, 281.56745385742187, 230.63480194091798, 240.20832202148438], [0, 329.18985620117184, 359.5491376953125, 230.63480194091798, 240.20832202148438], [0, 429.79218115234374, 522.6558657226562, 231.5051219482422, 241.0786420288086], [0, 49.40824243164062, 329.18985620117184, 239.33800201416017, 250.652162109375], [0, 347.0482570800781, 497.0588244628906, 243.68960205078125, 253.26312213134767], [0, 47.62240234375, 191.68016943359373, 252.39280212402343, 262.83664221191407], [0, 347.0482570800781, 417.8865805664062, 255.87408215332033, 265.4476022338867], [0, 66.67136328125, 250.01761230468747, 267.1882422485352, 279.37272235107423], [0, 295.25889453125, 452.412822265625, 269.7992022705078, 281.98368237304686], [0, 47.62240234375, 190.489609375, 282.8540023803711, 295.0384824829102], [0, 220.8488908691406, 359.5491376953125, 284.59464239501955, 295.9088024902344], [0, 425.6252209472656, 528.608666015625, 286.33528240966797, 297.6494425048828], [0, 96.43536474609374, 151.20112744140624, 301.1307225341797, 311.57456262207035], [0, 222.63473095703122, 260.1373728027344, 302.87136254882813, 312.44488262939456], [0, 274.42409350585933, 293.47305444335933, 298.519762512207, 308.96360260009766], [0, 274.42409350585933, 293.47305444335933, 308.09328259277345, 317.6668026733399], [0, 344.6671369628906, 397.6470595703125, 303.74168255615234, 313.31520263671877], [0, 457.17506249999997, 493.48714428710934, 304.61200256347655, 314.185522644043], [0, 508.9644250488281, 528.0133859863281, 301.1307225341797, 311.57456262207035], [0, 508.9644250488281, 528.0133859863281, 310.7042426147461, 320.2777626953125], [0, 36.90736181640625, 148.22472729492188, 319.4074426879883, 330.72160278320314], [0, 213.11025048828122, 270.2571333007812, 322.0184027099609, 331.59192279052735], [0, 272.6382534179687, 278.5910537109375, 322.0184027099609, 331.59192279052735], [0, 300.021134765625, 383.95561889648434, 322.0184027099609, 332.46224279785156], [0, 448.84114208984374, 500.03522460937495, 323.7590427246094, 333.33256280517577], [0, 510.15498510742185, 515.5125053710938, 324.6293627319336, 333.33256280517577], [0, 34.526241699218744, 104.76928515624999, 336.81384283447267, 347.2576829223633], [0, 272.6382534179687, 278.5910537109375, 339.4248028564453, 348.1280029296875], [0, 300.021134765625, 439.3166616210937, 339.4248028564453, 350.73896295166014], [0, 449.4364221191406, 482.1768237304687, 341.1654428710938, 350.73896295166014], [0, 510.7502651367187, 516.1077854003906, 342.035762878418, 350.73896295166014], [0, 300.021134765625, 429.79218115234374, 355.96088299560546, 366.4047230834961], [0, 450.62698217773436, 502.41634472656244, 357.70152301025394, 367.2750430908203], [0, 511.94082519531247, 517.2983454589844, 358.57184301757815, 367.2750430908203], [0, 300.021134765625, 413.12434033203124, 372.4969631347656, 382.94080322265626], [0, 451.22226220703124, 485.15322387695306, 374.2376031494141, 383.81112322998047], [0, 513.726665283203, 519.084185546875, 375.1079231567383, 383.81112322998047], [0, 8.33392041015625, 241.08841186523435, 522.1920043945313, 534.3764844970704], [0, 26.78760131835937, 143.46248706054686, 545.6906445922851, 557.8751246948242], [0, 417.29130053710935, 473.8429033203125, 547.4312846069336, 559.6157647094726], [0, 26.78760131835937, 84.52976416015625, 567.4486447753907, 579.6331248779297], [0, 23.215921142578125, 82.14864404296874, 585.7253649291993, 597.9098450317383], [0, 266.685453125, 315.49841552734375, 586.5956849365234, 598.7801650390625], [0, 19.0489609375, 206.56217016601562, 607.4833651123047, 621.4084852294922], [0, 422.05354077148434, 558.3726674804687, 610.9646451416015, 625.7600852661133], [0, 16.072560791015626, 260.1373728027344, 632.7226453247071, 647.5180854492188], [0, 329.7851362304687, 492.8918642578125, 632.7226453247071, 648.388405456543], [0, 13.096160644531249, 72.62416357421874, 657.0916055297852, 671.8870456542969], [0, 142.86720703125, 257.16097265625, 657.9619255371094, 672.7573656616211], [0, 328.59457617187496, 409.55266015625, 657.9619255371094, 672.7573656616211], [0, 458.3656225585937, 529.7992260742187, 657.9619255371094, 674.4980056762696], [0, 10.71504052734375, 89.29200439453125, 679.7199257202149, 694.5153658447266], [0, 183.94152905273435, 245.2553720703125, 681.4605657348633, 696.256005859375], [0, 328.59457617187496, 389.3131391601562, 681.4605657348633, 696.256005859375], [0, 469.67594311523436, 506.5833049316406, 684.071525756836, 697.1263258666993], [0, 1.19056005859375, 230.3733713378906, 704.9592059326172, 722.3656060791016], [0, 283.94857397460936, 370.2641782226562, 707.5701659545898, 724.10624609375], [0, 428.60162109374994, 541.7048266601562, 711.0514459838868, 724.9765661010742]]
2026-08-10 11:30:34,465 INFO     29 [qwen-vl-text] ═══ DONE ═══ 99 positions, pages=1, time=33.8s
2026-08-10 11:30:34,481 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:30:34,481 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:30:34,482 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:30:34,482 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:30:34.482+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 22, "failed": 0, "current": {"8d2d744a94ae11f1bd9827cf206dfa2d": {"id": "8d2d744a94ae11f1bd9827cf206dfa2d", "doc_id": "8cb8165094ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3256443, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786361283901, "task_type": "dataflow", "root_trace_id": "a109a49aa4f54fb6bb962f0e0599fa22", "root_traceparent": "00-a109a49aa4f54fb6bb962f0e0599fa22-2306060947da7753-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:30:34,491 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:34,491 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:30:35,402 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:35,407 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:30:35,407 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:30:35,407 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:30:35,414 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:35,414 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:30:36,563 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:36,569 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:30:36,570 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:30:36,570 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:30:36,576 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:36,576 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:30:37,045 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:30:37,060 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:30:37,061 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "252 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-10 11:30:37,061 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:30:37,062 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 11:30:37,081 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:30:37,081 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 3, 'DischargeRecord': 1}", "name": "lzga-哮喘-沈阳(1).pdf"}
2026-08-10 11:30:37,081 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:30:37,187 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786361284319, 'update_date': datetime.datetime(2026, 8, 10, 11, 28, 4), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 924487, 'status': '1'}
2026-08-10 11:30:37,445 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=凤城诚岳中医院
门诊病历
诊断专用章
编号：54474
姓名：
性别：男
年龄：67.0岁
地址：燃机厂
职业：退休
联系电话
99
身份证号 21
5
就诊时间：2025年06月6日
主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。
现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白
痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住
院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1
天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼
吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。
既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，
否认药物及食物过敏史、中毒史。
体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82
查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。
辅助检查：
初步诊断：支气管哮喘
处置建议：1、舒利迭50/250ug/吸日二次吸入。
2、醋酸泼尼松（强的松）20mg日一次口服3-5天
3、加重时及时就诊
医师：梁明
梁明
---
凤城诚岳中医院
诊断专用章 病历
编号：104474
姓名：
性别：男
年龄：67.0岁
地址：
职业：退休
联系电话
身份证号
就诊时间：2026年02月8日
主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。
现病史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。
既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。
体温(℃)：36.8
脉搏(次/分)：86
呼吸(次/分) 26
血压(mmHg) 140/80
查体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。
辅助检查：
初步诊断：支气管哮喘（急性发作期）
处置建议：1、舒利迭50/250ug/吸日二次吸入。
2、醋酸泼尼松（强的松）20mg日一次口服3-5天
3、加重时及时就诊。
医师：梁明
梁明
---
欢迎光临健康大药房凤鸣分店
日期：2026-02-08 09:50:51
单号：2602080008000051
会员号:73504会员姓名:李治刚
收银员：050
机号:01
营业员：050
编号:1440166
名称:醋酸泼尼松片（强地松 4
产地:浙江仙琚制药股份有限
批号:LA24600
规格:5mg*100p
剂型:片剂
单价:6.5 实价:6.5
数量:1.金额:6.5
收款方式:现金
6.50
数量合计:1.00
应收额:6.50
实收:6.50
优惠额:0.00 找零:0.00
本单为重打印小票!不作开票依据
代金卡余额:0.00
本单积分:1.7
累计积分:27.7
本单代金卡金额:0.0
零钱包存入:0
周六会员日
满49返15，满99返30
此票据为购货凭证，请妥善保管
---
医疗保险定点药店收费明细
辽宁天士力大药房连锁有限公司
药店名称：
凤城石桥路店
购药人：
鲁药单：1
2106210151
个人编号：0000001017 票据号：100189
563862
序号 药品名称 数量 金额
1 沙美特罗替卡 1.0 196.20
松吸入粉雾剂
2 沙美特罗替卡 1.0 196.20
松吸入粉雾剂
总金额：392.40
人民币叁佰玖拾贰
圆肆角整
现金支
账户支付：0.00
392.40
付：
共济支
统筹支付：0.0
0.0
付：
公补：0.0
消费前账户余额：0.00
消费后账户余额：0.00
2025.12.02
消费时间：
10:22:36
收款员：2103
无购药人、个人编号、药品明细购药单无效
---
医疗保险定点药店收费明细
辽宁天士力大药房连锁有限公司
药店名称：
凤城石桥路店
购药人：
鲁药单：1
2106210151
个人编号：0000001017 票据号：100246
563862
序号 药品名称 数量 金额
1 沙美特罗替卡 1.0 196.20
松吸入粉雾剂
2 沙美特罗替卡 1.0 196.20
松吸入粉雾剂
总金额：392.40
人民币叁佰玖拾贰
圆肆角整
现金支
账户支付：0.00
392.40
付：
共济支
统筹支付：0.0
0.0
付：
公补：0.0
消费前账户余额：0.00
消费后账户余额：0.00
2026.02.01
消费时间：
19:49:51
收款员：2103
无购药人、个人编号、药品明细购药单无效
---
信4个月
医疗机构：凤城市中医院
(组织机构代码：46376203-6)
医疗付费方式：城镇医保
中医住院病案首页
02410974
健康卡号：
第3次入院
病案号：290510
姓名：
性别：1.男2.女出生日期：1958-12-09
年龄：65岁
国籍：中国
(年龄不足一周岁的)年龄：
新生儿出生体重：
克
新生儿入院体重：
克
出生地点：辽宁省凤城市
籍贯：辽宁省
民族：汉族
身份证号：
职业：退(离)休人
婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他
现地址：凤城市胜利委十组060644
邮编：118100
户口地址：凤城市胜利委十组060644
邮编：118100
工作单位：电业局
邮编：118100
联系人姓名：李治刚
关系：本人或户
地址：凤城市胜利委十组060644
9
入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他
治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医
入院时间：2024-10-08
入院科别：内四科病房
病房：11
转科科别：
出院时间：2024-10-15
出院科别：内四科病房
病房：
实际住院：7 天
门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)
疾病编码：A04.04.04.02,A04.04.04.02
门(急)诊诊断(西医诊断)：肺部感染
疾病编码：J98.414
实施临床路径：3 1.中医2.西医3否
使用医疗机构中药制剂：2 1.是2.否
使用中医诊疗设备：1 1.是2.否
使用中医诊疗技术：1 1.是2.否
辨证施护：1 1.是2.否
出院中医诊断
疾病编码
入院
病情
出院西医诊断
疾病编码
入院
病情
主病：喘病(可选词：喘证)
A04.04.04.02
1
主要诊断：支气管哮喘
J45.900x001
1
主证：风寒袭肺证
1
其他诊断：冠状动脉粥样硬化性心脏
I25.103
1
其他诊断：心功能II级(NYHA分级)
I50.900x007
1
其他诊断：特应性神经性皮炎
L20.803
1
入院病情：1.有，2.临床未确定，3.情况不明，4.无
损伤、中毒的外部原因：
疾病编码：
病理诊断：
疾病编码：
病理号：
药物过敏：1 1.无2.有过敏药物：
死亡患者尸检：2 1.是2.否
血型：□ 1.A 2.B 3.O 4.AB 5.不详 6.未查
Rh 4 1.阴2.阳3.不详4.未查
科主任：李革
主任(副主任)医师：李革
主治医师：宋文平
住院医师：刘彦
责任护士：唐莹莹
进修医师：
实习医师：
编码员：
病案质量 1 1.甲2.乙3.丙质控医师：刘彦
质控护士：杨
质控日期：2024-10-17
2026-08-10 11:30:37,854 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:30:37,854 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 3, 'DischargeRecord': 1}", "name": "lzga-哮喘-沈阳(1).pdf", "embedding_token_consumption": 2679}
2026-08-10 11:30:37,854 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:30:38,022 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:30:38,022 INFO     29 [Trace] task=8d2d744a | doc=lzga-哮喘-沈阳(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 11:30:38,026 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:30:38,026 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:30:38,026 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:30:38,026 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:30:38,026 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:30:38,026 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:30:38,032 INFO     29 set_progress(8d2d744a94ae11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:30:38 [DOC Engine]:
Start to index...
2026-08-10 11:30:38,068 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.031s]
2026-08-10 11:30:38,073 INFO     29 set_progress(8d2d744a94ae11f1bd9827cf206dfa2d), progress: 0.8166666666666668, progress_msg: 
2026-08-10 11:30:38,093 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-10 11:30:38,105 INFO     29 set_progress(8d2d744a94ae11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:30:38 Indexing done (0.07s). Task done (148.32s)
2026-08-10 11:30:38,113 INFO     29 [Done], chunks(6), token(2679), elapsed:148.32
2026-08-10 11:30:38,210 INFO     29 handle_task done for task {"id": "8d2d744a94ae11f1bd9827cf206dfa2d", "doc_id": "8cb8165094ae11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3256443, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786361283901, "task_type": "dataflow", "root_trace_id": "a109a49aa4f54fb6bb962f0e0599fa22", "root_traceparent": "00-a109a49aa4f54fb6bb962f0e0599fa22-2306060947da7753-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
