# 基准结果：lzga-哮喘-沈阳(1).pdf

## 基本信息

- 文件：`lzga-哮喘-沈阳(1).pdf`
- 大小：5899.8 KB
- PDF 总页数：5
- doc_id：`e1b14d16908a11f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:15  完成时间：2026-08-05T14:31:15  耗时：1.0s
- progress_msg：`05:05:35 Indexing done (0.06s). Task done (159.63s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 00f612c8 | 1 | 1-1 | 信4个月 医疗机构：凤城市中医院 (组织机构代码：46376203-6) 医疗付 |
| 2 | 4d136d9d | 1 | 2-2 | 凤城诚岳中医院 门诊 病 历 诊断专用章 编号：54474 姓名： 性别：男 年 |
| 3 | ae2a11aa | 1 | 3-3 | 凤城诚岳中医院 诊断专用笺 病 历 编号：104474 姓名： 性别： 男 年龄 |
| 4 | 28f899c0 | 1 | 4-4 | 欢迎光临健康大药房凤鸣分店 日期：2026-02-08 09:50:51 单号： |
| 5 | 93cb330a | 1 | 5-5 | 医疗保险定点药店收费明细 辽宁天士力大药房连锁有限公司 药店名称： 凤城石桥路店 |
| 6 | 8227fc6d | 1 | 5-5 | 医疗保险定点药店收费明细 辽宁天士力大药房连锁有限公司 药店名称： 凤城石桥路店 |

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
- ChunkMerger：`{"found": true, "merged": 6, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 3, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 05:05:33,540 INFO     29 [ChunkMerger] Merged 6 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 05:02:42,405 INFO     29 handle_task begin for task {"id": "e1e244a2908a11f1a3da71efcdd7cc1f", "doc_id": "e1b14d16908a11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 6041420, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906159481, "task_type": "dataflow", "root_trace_id": "ee648f5612474f2494cdafbea4ad365d", "root_traceparent": "00-ee648f5612474f2494cdafbea4ad365d-00889eb88a3b4664-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 05:02:42,624 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-05 05:02:42,668 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 05:02:42,683 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 05:02:42,683 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 05:02:42,688 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 05:02:42,688 INFO     29 ============================================================
2026-08-05 05:02:42,688 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 05:02:42,688 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 05:02:42,688 INFO     29 ============================================================
2026-08-05 05:02:42,688 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 05:02:42,688 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 05:02:42,690 INFO     29 No torch found.
2026-08-05 05:02:43,203 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-05 05:02:43,488 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1748129, prompt_len=644
2026-08-05 05:02:45,025 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:02:45,025 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-05 05:02:45,041 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1748129, prompt_len=401
2026-08-05 05:02:51,947 INFO     29 [qwen-vl-parser] text API response (len=1422):
["信4个月", "医疗机构：凤城市中医院", "(组织机构代码：46376203-6)", "医疗付费方式：城镇医保", "中医住院病案首页", "02410974", "健康卡号：", "第3次入院", "病案号：290510", "姓名：", "性别：1.男2.女出生日期：1958-12-09", "年龄：65岁", "国籍：中国", "(年龄不足一周岁的)年龄：", "新生儿出生体重：", "克", "新生儿入院体重：", "克", "出生地点：辽宁省凤城市", "籍贯：辽宁省", "民族：汉族", "身份证号：", "职业：退(离)休人", "婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他", "现地址：凤城市胜利委十组060644", "邮编：118100", "户口地址：凤城市胜利委十组060644", "邮编：118100", "工作单位：电业局", "邮编：118100", "联系人姓名：李治刚", "关系：本人或户", "地址：凤城市胜利委十组060644", "9", "入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他", "治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医", "入院时间：2024-10-08", "入院科别：内四科病房", "病房：11", "转科科别：", "出院时间：2024-10-15", "出院科别：内四科病房", "病房：", "实际住院：7 天", "门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)", "疾病编码：A04.04.04.02,A04.04.04.02", "门(急)诊诊断(西医诊断)：肺部感染", "疾病编码：J98.414", "实施临床路径：3 1.中医2.西医3否", "使用医疗机构中药制剂：2 1.是2.否", "使用中医诊疗设备：1 1.是2.否", "使用中医诊疗技术：1 1.是2.否", "辨证施护：1 1.是2.否", "出院中医诊断", "疾病编码", "入院", "病情", "出院西医诊断", "疾病编码", "入院", "病情", "主病：喘病(可选词：喘证)", "A04.04.04.02", "1", "主要诊断：支气管哮喘", "J45.900x001", "1", "主证：风寒袭肺证", "1", "其他诊断：冠状动脉粥样硬化性心脏", "I25.103", "1", "其他诊断：心功能II级(NYHA分级)", "I50.900x007", "1", "其他诊断：特应性神经性皮炎", "L20.803", "1", "入院病情：1.有，2.临床未确定，3.情况不明，4.无", "损伤、中毒的外部原因：", "疾病编码：", "病理诊断：", "疾病编码：", "病理号：", "药物过敏：1 1.无2.有过敏药物：", "死亡患者尸检：2 1.是2.否", "血型：1.A 2.B 3.0 4.AB 5.不详 6.未查", "Rh 4 1.阴2.阳3.不详4.未查", "科主任：李革", "主任(副主任)医师：李革", "主治医师：宋文平", "住院医师：刘", "责任护士：唐莹莹", "进修医师：", "实习医师：", "编码员：", "病案质量 1 1.甲2.乙3.丙质控医师：刘", "质控护士：杨", "质控日期：2024-10-17"]
2026-08-05 05:02:51,947 INFO     29 [qwen-vl-parser] page=1 text: 99 lines (bbox 0-98)
2026-08-05 05:02:51,947 INFO     29 [qwen-vl-parser] page=1 text: 99 sections
2026-08-05 05:02:52,170 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1375057, prompt_len=644
2026-08-05 05:02:53,515 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:02:53,516 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 05:02:53,530 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1375057, prompt_len=401
2026-08-05 05:02:57,311 INFO     29 [qwen-vl-parser] text API response (len=654):
["凤城诚岳中医院", "门诊 病 历", "诊断专用章", "编号：54474", "姓名：", "性别：男", "年龄：67.0岁", "地址：然机厂", "职业：退休", "联系电话", "99", "身份证号 21", "5", "就诊时间：2025年06月6日", "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白", "痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住", "院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1", "天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼", "吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。", "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，", "否认药物及食物过敏史、中毒史。", "体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82", "查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。", "辅助检查：", "初步诊断：支气管哮喘", "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "3、加重时及时就诊", "医师：梁明", "梁明"]
2026-08-05 05:02:57,312 INFO     29 [qwen-vl-parser] page=2 text: 31 lines (bbox 99-129)
2026-08-05 05:02:57,312 INFO     29 [qwen-vl-parser] page=2 text: 31 sections
2026-08-05 05:02:57,705 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2316883, prompt_len=644
2026-08-05 05:02:59,020 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:02:59,021 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 05:02:59,037 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2316883, prompt_len=401
2026-08-05 05:03:01,891 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:03:01.888+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 14, "failed": 0, "current": {"e1e244a2908a11f1a3da71efcdd7cc1f": {"id": "e1e244a2908a11f1a3da71efcdd7cc1f", "doc_id": "e1b14d16908a11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 6041420, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906159481, "task_type": "dataflow", "root_trace_id": "ee648f5612474f2494cdafbea4ad365d", "root_traceparent": "00-ee648f5612474f2494cdafbea4ad365d-00889eb88a3b4664-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:03:02,906 INFO     29 [qwen-vl-parser] text API response (len=653):
["凤城诚岳中医院", "诊断专用笺 病 历", "编号：104474", "姓名：", "性别： 男", "年龄： 67.0岁", "地址：", "职业： 退休", "联系电话", "身份证号", "就诊时间：2026年02月8日", "主 诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "现 病 史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。", "既 往 史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。", "体温(℃)： 36.8 脉搏(次/分)： 86 呼吸(次/分) 26 血压(mmHg) 140/80", "查 体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。", "辅助检查：", "初步诊断：支气管哮喘（急性发作期）", "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "3、加重时及时就诊。", "医师：梁明", "梁明"]
2026-08-05 05:03:02,908 INFO     29 [qwen-vl-parser] page=3 text: 23 lines (bbox 130-152)
2026-08-05 05:03:02,908 INFO     29 [qwen-vl-parser] page=3 text: 23 sections
2026-08-05 05:03:03,475 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2787579, prompt_len=644
2026-08-05 05:03:05,263 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:03:05,263 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-05 05:03:05,278 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2787579, prompt_len=401
2026-08-05 05:03:11,252 INFO     29 [qwen-vl-parser] text API response (len=441):
["欢迎光临健康大药房凤鸣分店", "日期：2026-02-08 09:50:51", "单号：2602080008000051", "会员号:73504会员姓名:李治刚", "收银员：050", "机号:01", "营业员：050", "编号:1440166", "名称:醋酸泼尼松片（强地松 4", "产地:浙江仙琚制药股份有限", "批号:LA24600", "规格:5mg*100p", "剂型:片剂", "单价:6.5 实价:6.5", "数量:1.金额:6.5", "收款方式:现金", "6.50", "数量合计:1.00", "应收额:6.50", "实收:6.50", "优惠额:0.00 找零:0.00", "本单为重打印小票!不作开票依据", "代金卡余额:0.00", "本单积分:1.7", "累计积分:27.7", "本单代金卡金额:0.0", "零钱包存入:0", "周六会员日", "满49返15,满99返30", "此票据为购货凭证,请妥善保管"]
2026-08-05 05:03:11,253 INFO     29 [qwen-vl-parser] page=4 text: 30 lines (bbox 153-182)
2026-08-05 05:03:11,253 INFO     29 [qwen-vl-parser] page=4 text: 30 sections
2026-08-05 05:03:11,816 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3573404, prompt_len=644
2026-08-05 05:03:13,495 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:03:13,498 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 05:03:13,516 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3573404, prompt_len=401
2026-08-05 05:03:18,803 INFO     29 [qwen-vl-parser] text API response (len=842):
["医疗保险定点药店收费明细", "辽宁天士力大药房连锁有限公司", "药店名称：", "凤城石桥路店", "购药人：", "鲁药单：1", "2106210151", "个人编号：0000001017 票据号：100189", "563862", "序号 药品名称 数量 金额", "1 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "2 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "总金额：392.40", "人民币叁佰玖拾贰", "圆肆角整", "现金支", "账户支付：0.00", "392.40", "付：", "共济支", "统筹支付：0.0", "0.0", "付：", "公补：0.0", "消费前账户余额：0.00", "消费后账户余额：0.00", "2025.12.02", "消费时间：", "10:22:36", "收款员：2103", "无购药人、个人编号、药品明细购药单无效", "医疗保险定点药店收费明细", "辽宁天士力大药房连锁有限公司", "药店名称：", "凤城石桥路店", "购药人：", "鲁药单：1", "2106210151", "个人编号：0000001017 票据号：100246", "563862", "序号 药品名称 数量 金额", "1 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "2 沙美特罗替卡 1.0 196.20", "松吸入粉雾剂", "总金额：392.40", "人民币叁佰玖拾贰", "圆肆角整", "现金支", "账户支付：0.00", "392.40", "付：", "共济支", "统筹支付：0.0", "0.0", "付：", "公补：0.0", "消费前账户余额：0.00", "消费后账户余额：0.00", "2026.02.01", "消费时间：", "19:49:51", "收款员：2103", "无购药人、个人编号、药品明细购药单无效"]
2026-08-05 05:03:18,805 INFO     29 [qwen-vl-parser] page=5 text: 66 lines (bbox 183-248)
2026-08-05 05:03:18,805 INFO     29 [qwen-vl-parser] page=5 text: 66 sections
2026-08-05 05:03:18,805 INFO     29 [qwen-vl-parser] parse_pdf done: 249 sections from 5 pages.
2026-08-05 05:03:18,815 INFO     29 Close text detector.
2026-08-05 05:03:19,157 INFO     29 Close text recognizer.
2026-08-05 05:03:19,465 INFO     29 Close recognizer.
2026-08-05 05:03:19,810 INFO     29 Close recognizer.
2026-08-05 05:03:20,190 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 05:03:20,191 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Parser:MedLink | outputs={"html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "json"}
2026-08-05 05:03:20,191 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 05:03:20,206 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:03:20,206 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 信4个月\n[BBOX-1] 医疗机构：凤城市中医院\n[BBOX-2] (组织机构代码：46376203-6)\n[BBOX-3] 医疗付费方式：城镇医保\n[BBOX-4] 中医住院病案首页\n[BBOX-5] 02410974\n[BBOX-6] 健康卡号：\n[BBOX-7] 第3次入院\n[BBOX-8] 病案号：290510\n[BBOX-9] 姓名：\n[BBOX-10] 性别：1.男2.女出生日期：1958-12-09\n[BBOX-11] 年龄：65岁\n[BBOX-12] 国籍：中国\n[BBOX-13] (年龄不足一周岁的)年龄：\n[BBOX-14] 新生儿出生体重：\n[BBOX-15] 克\n[BBOX-16] 新生儿入院体重：\n[BBOX-17] 克\n[BBOX-18] 出生地点：辽宁省凤城市\n[BBOX-19] 籍贯：辽宁省\n[BBOX-20] 民族：汉族\n[BBOX-21] 身份证号：\n[BBOX-22] 职业：退(离)休人\n[BBOX-23] 婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他\n[BBOX-24] 现地址：凤城市胜利委十组060644\n[BBOX-25] 邮编：118100\n[BBOX-26] 户口地址：凤城市胜利委十组060644\n[BBOX-27] 邮编：118100\n[BBOX-28] 工作单位：电业局\n[BBOX-29] 邮编：118100\n[BBOX-30] 联系人姓名：李治刚\n[BBOX-31] 关系：本人或户\n[BBOX-32] 地址：凤城市胜利委十组060644\n[BBOX-33] 9\n[BBOX-34] 入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他\n[BBOX-35] 治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医\n[BBOX-36] 入院时间：2024-10-08\n[BBOX-37] 入院科别：内四科病房\n[BBOX-38] 病房：11\n[BBOX-39] 转科科别：\n[BBOX-40] 出院时间：2024-10-15\n[BBOX-41] 出院科别：内四科病房\n[BBOX-42] 病房：\n[BBOX-43] 实际住院：7 天\n[BBOX-44] 门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)\n[BBOX-45] 疾病编码：A04.04.04.02,A04.04.04.02\n[BBOX-46] 门(急)诊诊断(西医诊断)：肺部感染\n[BBOX-47] 疾病编码：J98.414\n[BBOX-48] 实施临床路径：3 1.中医2.西医3否\n[BBOX-49] 使用医疗机构中药制剂：2 1.是2.否\n[BBOX-50] 使用中医诊疗设备：1 1.是2.否\n[BBOX-51] 使用中医诊疗技术：1 1.是2.否\n[BBOX-52] 辨证施护：1 1.是2.否\n[BBOX-53] 出院中医诊断\n[BBOX-54] 疾病编码\n[BBOX-55] 入院\n[BBOX-56] 病情\n[BBOX-57] 出院西医诊断\n[BBOX-58] 疾病编码\n[BBOX-59] 入院\n[BBOX-60] 病情\n[BBOX-61] 主病：喘病(可选词：喘证)\n[BBOX-62] A04.04.04.02\n[BBOX-63] 1\n[BBOX-64] 主要诊断：支气管哮喘\n[BBOX-65] J45.900x001\n[BBOX-66] 1\n[BBOX-67] 主证：风寒袭肺证\n[BBOX-68] 1\n[BBOX-69] 其他诊断：冠状动脉粥样硬化性心脏\n[BBOX-70] I25.103\n[BBOX-71] 1\n[BBOX-72] 其他诊断：心功能II级(NYHA分级)\n[BBOX-73] I50.900x007\n[BBOX-74] 1\n[BBOX-75] 其他诊断：特应性神经性皮炎\n[BBOX-76] L20.803\n[BBOX-77] 1\n[BBOX-78] 入院病情：1.有，2.临床未确定，3.情况不明，4.无\n[BBOX-79] 损伤、中毒的外部原因：\n[BBOX-80] 疾病编码：\n[BBOX-81] 病理诊断：\n[BBOX-82] 疾病编码：\n[BBOX-83] 病理号：\n[BBOX-84] 药物过敏：1 1.无2.有过敏药物：\n[BBOX-85] 死亡患者尸检：2 1.是2.否\n[BBOX-86] 血型：1.A 2.B 3.0 4.AB 5.不详 6.未查\n[BBOX-87] Rh 4 1.阴2.阳3.不详4.未查\n[BBOX-88] 科主任：李革\n[BBOX-89] 主任(副主任)医师：李革\n[BBOX-90] 主治医师：宋文平\n[BBOX-91] 住院医师：刘\n[BBOX-92] 责任护士：唐莹莹\n[BBOX-93] 进修医师：\n[BBOX-94] 实习医师：\n[BBOX-95] 编码员：\n[BBOX-96] 病案质量 1 1.甲2.乙3.丙质控医师：刘\n[BBOX-97] 质控护士：杨\n[BBOX-98] 质控日期：2024-10-17\n[BBOX-99] 凤城诚岳中医院\n[BBOX-100] 门诊 病 历\n[BBOX-101] 诊断专用章\n[BBOX-102] 编号：54474\n[BBOX-103] 姓名：\n[BBOX-104] 性别：男\n[BBOX-105] 年龄：67.0岁\n[BBOX-106] 地址：然机厂\n[BBOX-107] 职业：退休\n[BBOX-108] 联系电话\n[BBOX-109] 99\n[BBOX-110] 身份证号 21\n[BBOX-111] 5\n[BBOX-112] 就诊时间：2025年06月6日\n[BBOX-113] 主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。\n[BBOX-114] 现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白\n[BBOX-115] 痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住\n[BBOX-116] 院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1\n[BBOX-117] 天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼\n[BBOX-118] 吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。\n[BBOX-119] 既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，\n[BBOX-120] 否认药物及食物过敏史、中毒史。\n[BBOX-121] 体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82\n[BBOX-122] 查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。\n[BBOX-123] 辅助检查：\n[BBOX-124] 初步诊断：支气管哮喘\n[BBOX-125] 处置建议：1、舒利迭50/250ug/吸日二次吸入。\n[BBOX-126] 2、醋酸泼尼松（强的松）20mg日一次口服3-5天\n[BBOX-127] 3、加重时及时就诊\n[BBOX-128] 医师：梁明\n[BBOX-129] 梁明\n[BBOX-130] 凤城诚岳中医院\n[BBOX-131] 诊断专用笺 病 历\n[BBOX-132] 编号：104474\n[BBOX-133] 姓名：\n[BBOX-134] 性别： 男\n[BBOX-135] 年龄： 67.0岁\n[BBOX-136] 地址：\n[BBOX-137] 职业： 退休\n[BBOX-138] 联系电话\n[BBOX-139] 身份证号\n[BBOX-140] 就诊时间：2026年02月8日\n[BBOX-141] 主 诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。\n[BBOX-142] 现 病 史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。\n[BBOX-143] 既 往 史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。\n[BBOX-144] 体温(℃)： 36.8 脉搏(次/分)： 86 呼吸(次/分) 26 血压(mmHg) 140/80\n[BBOX-145] 查 体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。\n[BBOX-146] 辅助检查：\n[BBOX-147] 初步诊断：支气管哮喘（急性发作期）\n[BBOX-148] 处置建议：1、舒利迭50/250ug/吸日二次吸入。\n[BBOX-149] 2、醋酸泼尼松（强的松）20mg日一次口服3-5天\n[BBOX-150] 3、加重时及时就诊。\n[BBOX-151] 医师：梁明\n[BBOX-152] 梁明\n[BBOX-153] 欢迎光临健康大药房凤鸣分店\n[BBOX-154] 日期：2026-02-08 09:50:51\n[BBOX-155] 单号：2602080008000051\n[BBOX-156] 会员号:73504会员姓名:李治刚\n[BBOX-157] 收银员：050\n[BBOX-158] 机号:01\n[BBOX-159] 营业员：050\n[BBOX-160] 编号:1440166\n[BBOX-161] 名称:醋酸泼尼松片（强地松 4\n[BBOX-162] 产地:浙江仙琚制药股份有限\n[BBOX-163] 批号:LA24600\n[BBOX-164] 规格:5mg*100p\n[BBOX-165] 剂型:片剂\n[BBOX-166] 单价:6.5 实价:6.5\n[BBOX-167] 数量:1.金额:6.5\n[BBOX-168] 收款方式:现金\n[BBOX-169] 6.50\n[BBOX-170] 数量合计:1.00\n[BBOX-171] 应收额:6.50\n[BBOX-172] 实收:6.50\n[BBOX-173] 优惠额:0.00 找零:0.00\n[BBOX-174] 本单为重打印小票!不作开票依据\n[BBOX-175] 代金卡余额:0.00\n[BBOX-176] 本单积分:1.7\n[BBOX-177] 累计积分:27.7\n[BBOX-178] 本单代金卡金额:0.0\n[BBOX-179] 零钱包存入:0\n[BBOX-180] 周六会员日\n[BBOX-181] 满49返15,满99返30\n[BBOX-182] 此票据为购货凭证,请妥善保管\n[BBOX-183] 医疗保险定点药店收费明细\n[BBOX-184] 辽宁天士力大药房连锁有限公司\n[BBOX-185] 药店名称：\n[BBOX-186] 凤城石桥路店\n[BBOX-187] 购药人：\n[BBOX-188] 鲁药单：1\n[BBOX-189] 2106210151\n[BBOX-190] 个人编号：0000001017 票据号：100189\n[BBOX-191] 563862\n[BBOX-192] 序号 药品名称 数量 金额\n[BBOX-193] 1 沙美特罗替卡 1.0 196.20\n[BBOX-194] 松吸入粉雾剂\n[BBOX-195] 2 沙美特罗替卡 1.0 196.20\n[BBOX-196] 松吸入粉雾剂\n[BBOX-197] 总金额：392.40\n[BBOX-198] 人民币叁佰玖拾贰\n[BBOX-199] 圆肆角整\n[BBOX-200] 现金支\n[BBOX-201] 账户支付：0.00\n[BBOX-202] 392.40\n[BBOX-203] 付：\n[BBOX-204] 共济支\n[BBOX-205] 统筹支付：0.0\n[BBOX-206] 0.0\n[BBOX-207] 付：\n[BBOX-208] 公补：0.0\n[BBOX-209] 消费前账户余额：0.00\n[BBOX-210] 消费后账户余额：0.00\n[BBOX-211] 2025.12.02\n[BBOX-212] 消费时间：\n[BBOX-213] 10:22:36\n[BBOX-214] 收款员：2103\n[BBOX-215] 无购药人、个人编号、药品明细购药单无效\n[BBOX-216] 医疗保险定点药店收费明细\n[BBOX-217] 辽宁天士力大药房连锁有限公司\n[BBOX-218] 药店名称：\n[BBOX-219] 凤城石桥路店\n[BBOX-220] 购药人：\n[BBOX-221] 鲁药单：1\n[BBOX-222] 2106210151\n[BBOX-223] 个人编号：0000001017 票据号：100246\n[BBOX-224] 563862\n[BBOX-225] 序号 药品名称 数量 金额\n[BBOX-226] 1 沙美特罗替卡 1.0 196.20\n[BBOX-227] 松吸入粉雾剂\n[BBOX-228] 2 沙美特罗替卡 1.0 196.20\n[BBOX-229] 松吸入粉雾剂\n[BBOX-230] 总金额：392.40\n[BBOX-231] 人民币叁佰玖拾贰\n[BBOX-232] 圆肆角整\n[BBOX-233] 现金支\n[BBOX-234] 账户支付：0.00\n[BBOX-235] 392.40\n[BBOX-236] 付：\n[BBOX-237] 共济支\n[BBOX-238] 统筹支付：0.0\n[BBOX-239] 0.0\n[BBOX-240] 付：\n[BBOX-241] 公补：0.0\n[BBOX-242] 消费前账户余额：0.00\n[BBOX-243] 消费后账户余额：0.00\n[BBOX-244] 2026.02.01\n[BBOX-245] 消费时间：\n[BBOX-246] 19:49:51\n[BBOX-247] 收款员：2103\n[BBOX-248] 无购药人、个人编号、药品明细购药单无效"
  }
]
2026-08-05 05:03:27,549 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:03:27,562 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'DischargeRecord': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3}
2026-08-05 05:03:27,570 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 05:03:27,570 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks": "6 items, types={'DischargeRecord': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3}"}
2026-08-05 05:03:27,570 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 05:03:27,570 INFO     29 [ChunkRouter] Routed 6 chunks into 3 groups: {'chunks_Discharge': 1, 'chunks_Clinical': 2, 'chunks_Medication': 3}
2026-08-05 05:03:27,578 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 05:03:27,578 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks": "6 items, types={'DischargeRecord': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:03:27,578 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 05:03:27,582 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:03:27,582 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:03:27 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:27,583 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:28,259 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:03:28,267 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 05:03:28,268 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:03:28,268 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 05:03:28,273 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:03:28,273 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:03:28 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:28,274 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:29,292 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:03:29,296 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 05:03:29,297 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:03:29,297 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 05:03:29,301 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:03:29,302 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:03:29,302 INFO     29 [qwen-vl-text] positions(31): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:03:29,302 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [31]
2026-08-05 05:03:29,530 INFO     29 [qwen-vl-text] page=1, rect=595x794, img=(1654x2206), dpi=200
2026-08-05 05:03:29,531 INFO     29 [qwen-vl-text] LLM extraction start, text_len=560
2026-08-05 05:03:29,531 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:03:29,531 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 99, \"bbox_end\": 129, \"encounter_dates\": [\"2025-06-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "凤城诚岳中医院\n门诊 病 历\n诊断专用章\n编号：54474\n姓名：\n性别：男\n年龄：67.0岁\n地址：然机厂\n职业：退休\n联系电话\n99\n身份证号 21\n5\n就诊时间：2025年06月6日\n主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。\n现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白\n痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住\n院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1\n天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼\n吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。\n既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，\n否认药物及食物过敏史、中毒史。\n体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82\n查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。\n辅助检查：\n初步诊断：支气管哮喘\n处置建议：1、舒利迭50/250ug/吸日二次吸入。\n2、醋酸泼尼松（强的松）20mg日一次口服3-5天\n3、加重时及时就诊\n医师：梁明\n梁明",
    "role": "user"
  }
]
[92m05:03:29 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:29,533 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:33,132 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:03:33,132 INFO     29 [qwen-vl-text] LLM output (len=504):
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
2026-08-05 05:03:33,132 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-06-06]
2026-08-05 05:03:33,140 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1781561, prompt_len=1266
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["凤城诚岳中医院", "门诊 病 历", "诊断专用章", "编号：54474", "姓名：", "性别：男", "年龄：67.0岁", "地址：然机厂", "职业：退休", "联系电话", "99", "身份证号 21", "5", "就诊时间：2025年06月6日", "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白", "痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住", "院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1", "天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼", "吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。", "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，", "否认药物及食物过敏史、中毒史。", "体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82", "查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。", "辅助检查：", "初步诊断：支气管哮喘", "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "3、加重时及时就诊", "医师：梁明", "梁明"]

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
2026-08-05 05:03:43,384 INFO     29 [qwen-vl-text] coord API raw response (len=1910):
[
	{"text": "凤城诚岳中医院", "bbox": [397, 65, 579, 90]},
	{"text": "门诊 病 历", "bbox": [389, 90, 577, 110]},
	{"text": "诊断专用章", "bbox": [425, 107, 535, 125]},
	{"text": "编号：54474", "bbox": [752, 105, 888, 122]},
	{"text": "姓名：", "bbox": [107, 143, 152, 157]},
	{"text": "性别：男", "bbox": [370, 135, 467, 150]},
	{"text": "年龄：67.0岁", "bbox": [604, 130, 752, 145]},
	{"text": "地址：然机厂", "bbox": [105, 159, 348, 173]},
	{"text": "职业：退休", "bbox": [604, 148, 728, 163]},
	{"text": "联系电话", "bbox": [103, 176, 177, 190]},
	{"text": "99", "bbox": [300, 173, 318, 186]},
	{"text": "身份证号 21", "bbox": [584, 166, 707, 182]},
	{"text": "5", "bbox": [864, 164, 875, 176]},
	{"text": "就诊时间：2025年06月6日", "bbox": [98, 207, 344, 225]},
	{"text": "主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "bbox": [95, 222, 652, 244]},
	{"text": "现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白", "bbox": [86, 275, 900, 297]},
	{"text": "痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住", "bbox": [83, 295, 900, 317]},
	{"text": "院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1", "bbox": [82, 314, 900, 336]},
	{"text": "天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼", "bbox": [79, 334, 901, 356]},
	{"text": "吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。", "bbox": [77, 354, 903, 375]},
	{"text": "既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，", "bbox": [72, 395, 904, 415]},
	{"text": "否认药物及食物过敏史、中毒史。", "bbox": [71, 415, 366, 435]},
	{"text": "体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82", "bbox": [62, 476, 889, 500]},
	{"text": "查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。", "bbox": [56, 516, 813, 541]},
	{"text": "辅助检查：", "bbox": [48, 577, 137, 597]},
	{"text": "初步诊断：支气管哮喘", "bbox": [40, 643, 250, 667]},
	{"text": "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "bbox": [33, 685, 486, 715]},
	{"text": "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "bbox": [133, 710, 625, 744]},
	{"text": "3、加重时及时就诊", "bbox": [131, 733, 320, 758]},
	{"text": "医师：梁明", "bbox": [637, 821, 757, 847]},
	{"text": "梁明", "bbox": [687, 805, 736, 825]}
]
2026-08-05 05:03:43,384 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=10.2s
2026-08-05 05:03:43,384 INFO     29 [qwen-vl-text] coord item[0]: text=凤城诚岳中医院, bbox=[397, 65, 579, 90]
2026-08-05 05:03:43,384 INFO     29 [qwen-vl-text] coord item[1]: text=门诊 病 历, bbox=[389, 90, 577, 110]
2026-08-05 05:03:43,384 INFO     29 [qwen-vl-text] coord item[2]: text=诊断专用章, bbox=[425, 107, 535, 125]
2026-08-05 05:03:43,384 INFO     29 [qwen-vl-text] coord item[3]: text=编号：54474, bbox=[752, 105, 888, 122]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[107, 143, 152, 157]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[370, 135, 467, 150]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：67.0岁, bbox=[604, 130, 752, 145]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[7]: text=地址：然机厂, bbox=[105, 159, 348, 173]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[8]: text=职业：退休, bbox=[604, 148, 728, 163]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[9]: text=联系电话, bbox=[103, 176, 177, 190]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[10]: text=99, bbox=[300, 173, 318, 186]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号 21, bbox=[584, 166, 707, 182]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[12]: text=5, bbox=[864, 164, 875, 176]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[13]: text=就诊时间：2025年06月6日, bbox=[98, 207, 344, 225]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。, bbox=[95, 222, 652, 244]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：患者50余年前无明显诱因反复出现呼吸困难，胸闷、气促，偶有咳嗽，偶有白, bbox=[86, 275, 900, 297]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[16]: text=痰，常因感冒后或者着凉后加重，2年前于“凤城市人民医院”诊断为“支气管哮喘”，经住, bbox=[83, 295, 900, 317]
2026-08-05 05:03:43,385 INFO     29 [qwen-vl-text] coord item[17]: text=院治疗后好转，间断吸入万托林及沙美特罗替卡松（50/250ug）吸入治疗，控制情况尚可。1, bbox=[82, 314, 900, 336]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[18]: text=天前患者因着凉后出现呼吸困难加重，吸入万托林及舒利迭后未见好转来诊。目前时有呼, bbox=[79, 334, 901, 356]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[19]: text=吸困难，胸闷气短，活动后加重，偶有白痰，饮食、睡眠可，二便正常。体重无明显变化。, bbox=[77, 354, 903, 375]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[20]: text=既往史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，, bbox=[72, 395, 904, 415]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[21]: text=否认药物及食物过敏史、中毒史。, bbox=[71, 415, 366, 435]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[22]: text=体温(℃)：36.2 脉搏(次/分)：82 呼吸(次/分) 25 血压(mmHg) 135/82, bbox=[62, 476, 889, 500]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[23]: text=查体：舌胖大，苔薄白，脉滑。双肺散在闻及呼气相哮鸣音，未闻及湿啰音。, bbox=[56, 516, 813, 541]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[24]: text=辅助检查：, bbox=[48, 577, 137, 597]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[25]: text=初步诊断：支气管哮喘, bbox=[40, 643, 250, 667]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[26]: text=处置建议：1、舒利迭50/250ug/吸日二次吸入。, bbox=[33, 685, 486, 715]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[27]: text=2、醋酸泼尼松（强的松）20mg日一次口服3-5天, bbox=[133, 710, 625, 744]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[28]: text=3、加重时及时就诊, bbox=[131, 733, 320, 758]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[29]: text=医师：梁明, bbox=[637, 821, 757, 847]
2026-08-05 05:03:43,386 INFO     29 [qwen-vl-text] coord item[30]: text=梁明, bbox=[687, 805, 736, 825]
2026-08-05 05:03:43,388 INFO     29 [qwen-vl-text] page=1 — 31/31 coords, api_time=10.2s
2026-08-05 05:03:43,388 INFO     29 [qwen-vl-text] new_positions (31):
[[1, 236.3244270019531, 344.66459252929684, 51.610726013183594, 71.46100524902343], [1, 231.5622219238281, 343.4740412597656, 71.46100524902343, 87.34122863769531], [1, 252.9921447753906, 318.47246459960934, 84.95919512939453, 99.25139617919922], [1, 447.64727734375, 528.6047636718749, 83.37117279052734, 96.86936267089844], [1, 63.69449291992187, 90.481896484375, 113.54359722900391, 124.65975360107421], [1, 220.25198486328122, 277.99372143554683, 107.19150787353516, 119.10167541503905], [1, 359.5464833984375, 447.64727734375, 103.22145202636719, 115.1316195678711], [1, 62.50394165039062, 207.15592089843747, 126.2477759399414, 137.3639323120117], [1, 359.5464833984375, 433.36066210937497, 117.51365307617188, 129.42382061767577], [1, 61.31339038085937, 105.36378735351562, 139.7459658203125, 150.8621221923828], [1, 178.5826904296875, 189.29765185546873, 137.3639323120117, 147.68607751464845], [1, 347.640970703125, 420.85987377929683, 131.80585412597657, 144.51003283691406], [1, 514.3181484375, 520.8661804199219, 130.21783178710936, 139.7459658203125], [1, 58.33701220703124, 204.774818359375, 164.3603120727539, 178.6525131225586], [1, 56.55118530273437, 388.11971386718744, 176.2704796142578, 193.73872534179688], [1, 51.19370458984375, 535.7480712890624, 218.3530715942383, 235.82131732177734], [1, 49.40787768554687, 535.7480712890624, 234.23329498291014, 251.70154071044922], [1, 48.812602050781244, 535.7480712890624, 249.31950720214843, 266.7877529296875], [1, 47.02677514648437, 536.3433469238281, 265.1997305908203, 282.66797631835936], [1, 45.83622387695312, 537.5338981933593, 281.0799539794922, 297.75418853759766], [1, 42.859845703124996, 538.129173828125, 313.63441192626954, 329.5146353149414], [1, 42.26457006835937, 217.87088232421874, 329.5146353149414, 345.3948587036133], [1, 36.90708935546875, 529.2000393066406, 377.94931665039064, 397.0055847167969], [1, 33.335435546875, 483.9590910644531, 409.70976342773434, 429.5600426635742], [1, 28.573230468749998, 81.55276196289061, 458.14444476318357, 474.02466815185545], [1, 23.811025390624998, 148.81890869140625, 510.5491819458008, 529.605450012207], [1, 19.644095947265622, 289.30395849609374, 543.8976510620117, 567.7179861450195], [1, 79.17165942382812, 372.04727172851557, 563.7479302978516, 590.7443100585938], [1, 77.98110815429686, 190.48820312499998, 582.0101871948242, 601.860466430664], [1, 379.1905793457031, 450.6236555175781, 651.8831701049804, 672.527460510254], [1, 408.95436108398434, 438.1228671875, 639.178991394043, 655.0592147827148]]
2026-08-05 05:03:43,388 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=14.1s
2026-08-05 05:03:43,388 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:03:43,388 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:03:43,388 INFO     29 [qwen-vl-text] positions(23): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:03:43,388 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [23]
2026-08-05 05:03:43,687 INFO     29 [qwen-vl-text] page=2, rect=595x794, img=(1654x2206), dpi=200
2026-08-05 05:03:43,688 INFO     29 [qwen-vl-text] LLM extraction start, text_len=583
2026-08-05 05:03:43,689 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:03:43,689 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 130, \"bbox_end\": 152, \"encounter_dates\": [\"2026-02-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "凤城诚岳中医院\n诊断专用笺 病 历\n编号：104474\n姓名：\n性别： 男\n年龄： 67.0岁\n地址：\n职业： 退休\n联系电话\n身份证号\n就诊时间：2026年02月8日\n主 诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。\n现 病 史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。\n既 往 史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。\n体温(℃)： 36.8 脉搏(次/分)： 86 呼吸(次/分) 26 血压(mmHg) 140/80\n查 体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。\n辅助检查：\n初步诊断：支气管哮喘（急性发作期）\n处置建议：1、舒利迭50/250ug/吸日二次吸入。\n2、醋酸泼尼松（强的松）20mg日一次口服3-5天\n3、加重时及时就诊。\n医师：梁明\n梁明",
    "role": "user"
  }
]
[92m05:03:43 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:43,690 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:43,691 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:03:43.690+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 14, "failed": 0, "current": {"e1e244a2908a11f1a3da71efcdd7cc1f": {"id": "e1e244a2908a11f1a3da71efcdd7cc1f", "doc_id": "e1b14d16908a11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 6041420, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906159481, "task_type": "dataflow", "root_trace_id": "ee648f5612474f2494cdafbea4ad365d", "root_traceparent": "00-ee648f5612474f2494cdafbea4ad365d-00889eb88a3b4664-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:03:47,832 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:03:47,832 INFO     29 [qwen-vl-text] LLM output (len=543):
{
  "encounter_date": "2026-02-08",
  "chief_complaint": "反复发作喘息、气促50余年，加重伴呼吸困难1天。",
  "present_illness": "患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。",
  "past_history": "否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。",
  "diagnosis": "支气管哮喘（急性发作期）",
  "treatment_plan": [
    "舒利迭50/250ug/吸 日二次 吸入",
    "醋酸泼尼松（强的松）20mg 日一次 口服 3-5天",
    "加重时及时就诊"
  ]
}
2026-08-05 05:03:47,832 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-08]
2026-08-05 05:03:47,841 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3259303, prompt_len=1265
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["凤城诚岳中医院", "诊断专用笺 病 历", "编号：104474", "姓名：", "性别： 男", "年龄： 67.0岁", "地址：", "职业： 退休", "联系电话", "身份证号", "就诊时间：2026年02月8日", "主 诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "现 病 史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。", "既 往 史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。", "体温(℃)： 36.8 脉搏(次/分)： 86 呼吸(次/分) 26 血压(mmHg) 140/80", "查 体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。", "辅助检查：", "初步诊断：支气管哮喘（急性发作期）", "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "3、加重时及时就诊。", "医师：梁明", "梁明"]

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
2026-08-05 05:03:59,524 INFO     29 [qwen-vl-text] coord API raw response (len=1583):
[
	{"text": "凤城诚岳中医院", "bbox": [407, 48, 610, 72]},
	{"text": "诊断专用笺 病 历", "bbox": [380, 77, 604, 100]},
	{"text": "编号：104474", "bbox": [787, 104, 937, 122]},
	{"text": "姓名：", "bbox": [71, 130, 124, 148]},
	{"text": "性别： 男", "bbox": [381, 130, 490, 148]},
	{"text": "年龄： 67.0岁", "bbox": [641, 130, 798, 148]},
	{"text": "地址：", "bbox": [71, 151, 124, 169]},
	{"text": "职业： 退休", "bbox": [641, 151, 771, 169]},
	{"text": "联系电话", "bbox": [71, 172, 162, 190]},
	{"text": "身份证号", "bbox": [621, 172, 707, 190]},
	{"text": "就诊时间：2026年02月8日", "bbox": [71, 217, 358, 235]},
	{"text": "主 诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。", "bbox": [71, 238, 694, 256]},
	{"text": "现 病 史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。", "bbox": [73, 300, 946, 431]},
	{"text": "既 往 史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。", "bbox": [75, 470, 946, 519]},
	{"text": "体温(℃)： 36.8 脉搏(次/分)： 86 呼吸(次/分) 26 血压(mmHg) 140/80", "bbox": [77, 557, 928, 584]},
	{"text": "查 体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。", "bbox": [77, 601, 747, 627]},
	{"text": "辅助检查：", "bbox": [79, 677, 177, 695]},
	{"text": "初步诊断：支气管哮喘（急性发作期）", "bbox": [79, 738, 454, 763]},
	{"text": "处置建议：1、舒利迭50/250ug/吸日二次吸入。", "bbox": [77, 802, 548, 832]},
	{"text": "2、醋酸泼尼松（强的松）20mg日一次口服3-5天", "bbox": [191, 822, 684, 851]},
	{"text": "3、加重时及时就诊。", "bbox": [191, 850, 399, 873]},
	{"text": "医师：梁明", "bbox": [700, 917, 810, 954]},
	{"text": "梁明", "bbox": [747, 915, 795, 933]}
]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=11.7s
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[0]: text=凤城诚岳中医院, bbox=[407, 48, 610, 72]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[1]: text=诊断专用笺 病 历, bbox=[380, 77, 604, 100]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[2]: text=编号：104474, bbox=[787, 104, 937, 122]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[71, 130, 124, 148]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[4]: text=性别： 男, bbox=[381, 130, 490, 148]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[5]: text=年龄： 67.0岁, bbox=[641, 130, 798, 148]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[6]: text=地址：, bbox=[71, 151, 124, 169]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[7]: text=职业： 退休, bbox=[641, 151, 771, 169]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[8]: text=联系电话, bbox=[71, 172, 162, 190]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[9]: text=身份证号, bbox=[621, 172, 707, 190]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[10]: text=就诊时间：2026年02月8日, bbox=[71, 217, 358, 235]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[11]: text=主 诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。, bbox=[71, 238, 694, 256]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[12]: text=现 病 史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。, bbox=[73, 300, 946, 431]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[13]: text=既 往 史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。, bbox=[75, 470, 946, 519]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[14]: text=体温(℃)： 36.8 脉搏(次/分)： 86 呼吸(次/分) 26 血压(mmHg) 140/80, bbox=[77, 557, 928, 584]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[15]: text=查 体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。, bbox=[77, 601, 747, 627]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查：, bbox=[79, 677, 177, 695]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[17]: text=初步诊断：支气管哮喘（急性发作期）, bbox=[79, 738, 454, 763]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[18]: text=处置建议：1、舒利迭50/250ug/吸日二次吸入。, bbox=[77, 802, 548, 832]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[19]: text=2、醋酸泼尼松（强的松）20mg日一次口服3-5天, bbox=[191, 822, 684, 851]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[20]: text=3、加重时及时就诊。, bbox=[191, 850, 399, 873]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[21]: text=医师：梁明, bbox=[700, 917, 810, 954]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] coord item[22]: text=梁明, bbox=[747, 915, 795, 933]
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] page=2 — 23/23 coords, api_time=11.7s
2026-08-05 05:03:59,525 INFO     29 [qwen-vl-text] new_positions (23):
[[2, 242.27718334960934, 363.1181372070312, 38.1125361328125, 57.16880419921875], [2, 226.20474121093747, 359.5464833984375, 61.13886004638672, 79.40111694335937], [2, 468.4819245605468, 557.7732697753905, 82.57716162109375, 96.86936267089844], [2, 42.26457006835937, 73.8141787109375, 103.22145202636719, 117.51365307617188], [2, 226.8000168457031, 291.68506103515625, 103.22145202636719, 117.51365307617188], [2, 381.5716818847656, 475.0299565429687, 103.22145202636719, 117.51365307617188], [2, 42.26457006835937, 73.8141787109375, 119.89568658447266, 134.18788763427733], [2, 381.5716818847656, 458.95751440429683, 119.89568658447266, 134.18788763427733], [2, 42.26457006835937, 96.43465283203125, 136.56992114257812, 150.8621221923828], [2, 369.6661691894531, 420.85987377929683, 136.56992114257812, 150.8621221923828], [2, 42.26457006835937, 213.10867724609372, 172.30042376708985, 186.59262481689453], [2, 42.26457006835937, 413.1212905273437, 188.97465832519532, 203.266859375], [2, 43.455121337890624, 563.1307504882813, 238.2033508300781, 342.2188140258789], [2, 44.64567260742187, 563.1307504882813, 373.18524963378906, 412.09179693603517], [2, 45.83622387695312, 552.4157890624999, 442.2642213745117, 463.70252294921875], [2, 45.83622387695312, 444.6708991699218, 477.20071282958986, 497.84500323486327], [2, 47.02677514648437, 105.36378735351562, 537.5455617065429, 551.8377627563476], [2, 47.02677514648437, 270.2551381835937, 585.9802430419921, 605.8305222778321], [2, 45.83622387695312, 326.21104785156245, 636.7969578857421, 660.61729296875], [2, 113.69764624023436, 407.16853417968747, 652.677181274414, 675.7035051879883], [2, 113.69764624023436, 237.51497827148435, 674.9094940185547, 693.1717509155274], [2, 416.69294433593745, 482.17326416015624, 728.1082423706055, 757.4866556396485], [2, 444.6708991699218, 473.24412963867184, 726.5202200317383, 740.812421081543]]
2026-08-05 05:03:59,526 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=16.1s
2026-08-05 05:03:59,535 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 05:03:59,535 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:03:59,535 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 05:03:59,542 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:03:59,542 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:03:59,542 INFO     29 [qwen-vl-text] positions(30): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:03:59,542 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [30]
2026-08-05 05:03:59,827 INFO     29 [qwen-vl-text] page=3, rect=595x1058, img=(1654x2940), dpi=200
2026-08-05 05:03:59,828 INFO     29 [qwen-vl-text] LLM extraction start, text_len=350
2026-08-05 05:03:59,828 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:03:59,828 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 153, \"bbox_end\": 182, \"encounter_dates\": [\"2026-02-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "欢迎光临健康大药房凤鸣分店\n日期：2026-02-08 09:50:51\n单号：2602080008000051\n会员号:73504会员姓名:李治刚\n收银员：050\n机号:01\n营业员：050\n编号:1440166\n名称:醋酸泼尼松片（强地松 4\n产地:浙江仙琚制药股份有限\n批号:LA24600\n规格:5mg*100p\n剂型:片剂\n单价:6.5 实价:6.5\n数量:1.金额:6.5\n收款方式:现金\n6.50\n数量合计:1.00\n应收额:6.50\n实收:6.50\n优惠额:0.00 找零:0.00\n本单为重打印小票!不作开票依据\n代金卡余额:0.00\n本单积分:1.7\n累计积分:27.7\n本单代金卡金额:0.0\n零钱包存入:0\n周六会员日\n满49返15,满99返30\n此票据为购货凭证,请妥善保管",
    "role": "user"
  }
]
[92m05:03:59 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:03:59,829 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:02,489 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:04:02,489 INFO     29 [qwen-vl-text] LLM output (len=421):
{
  "encounter_date": "2026-02-08",
  "pharmacy": "健康大药房凤鸣分店",
  "medications": [
    {
      "name": "醋酸泼尼松片（强地松）",
      "specification": "5mg*100p",
      "dosage": null,
      "quantity": 1,
      "unit_price": 6.5,
      "total_price": 6.5,
      "frequency": null,
      "route": null,
      "manufacturer": "浙江仙琚制药股份有限公司",
      "approval_number": null
    }
  ],
  "payment_total": 6.5,
  "payment_method": "现金"
}
2026-08-05 05:04:02,489 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-08]
2026-08-05 05:04:02,502 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5040141, prompt_len=1053
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["欢迎光临健康大药房凤鸣分店", "日期：2026-02-08 09:50:51", "单号：2602080008000051", "会员号:73504会员姓名:李治刚", "收银员：050", "机号:01", "营业员：050", "编号:1440166", "名称:醋酸泼尼松片（强地松 4", "产地:浙江仙琚制药股份有限", "批号:LA24600", "规格:5mg*100p", "剂型:片剂", "单价:6.5 实价:6.5", "数量:1.金额:6.5", "收款方式:现金", "6.50", "数量合计:1.00", "应收额:6.50", "实收:6.50", "优惠额:0.00 找零:0.00", "本单为重打印小票!不作开票依据", "代金卡余额:0.00", "本单积分:1.7", "累计积分:27.7", "本单代金卡金额:0.0", "零钱包存入:0", "周六会员日", "满49返15,满99返30", "此票据为购货凭证,请妥善保管"]

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
2026-08-05 05:04:12,109 INFO     29 [qwen-vl-text] coord API raw response (len=1671):
[
	{"text": "欢迎光临健康大药房凤鸣分店", "bbox": [278, 225, 647, 255]},
	{"text": "日期：2026-02-08 09:50:51", "bbox": [277, 245, 620, 274]},
	{"text": "单号：2602080008000051", "bbox": [275, 265, 607, 294]},
	{"text": "会员号:73504会员姓名:李治刚", "bbox": [273, 287, 655, 317]},
	{"text": "收银员：050", "bbox": [270, 308, 436, 333]},
	{"text": "机号:01", "bbox": [473, 317, 568, 338]},
	{"text": "营业员：050", "bbox": [270, 344, 434, 367]},
	{"text": "编号:1440166", "bbox": [514, 354, 690, 371]},
	{"text": "名称:醋酸泼尼松片（强地松 4", "bbox": [270, 367, 658, 394]},
	{"text": "产地:浙江仙琚制药股份有限", "bbox": [266, 389, 624, 415],
	"text": "批号:LA24600", "bbox": [264, 411, 450, 433]},
	{"text": "规格:5mg*100p", "bbox": [263, 433, 467, 457]},
	{"text": "剂型:片剂", "bbox": [261, 456, 392, 478]},
	{"text": "单价:6.5 实价:6.5", "bbox": [261, 478, 506, 501]},
	{"text": "数量:1.金额:6.5", "bbox": [258, 501, 472, 522]},
	{"text": "收款方式:现金", "bbox": [254, 546, 463, 568]},
	{"text": "6.50", "bbox": [513, 551, 571, 568]},
	{"text": "数量合计:1.00", "bbox": [252, 569, 452, 590]},
	{"text": "应收额:6.50", "bbox": [250, 592, 434, 613]},
	{"text": "实收:6.50", "bbox": [467, 594, 612, 614]},
	{"text": "优惠额:0.00 找零:0.00", "bbox": [244, 641, 600, 664]},
	{"text": "本单为重打印小票!不作开票依据", "bbox": [241, 665, 708, 689]},
	{"text": "代金卡余额:0.00", "bbox": [238, 690, 490, 712]},
	{"text": "本单积分:1.7", "bbox": [236, 715, 441, 737]},
	{"text": "累计积分:27.7", "bbox": [235, 740, 456, 762]},
	{"text": "本单代金卡金额:0.0", "bbox": [233, 765, 533, 788]},
	{"text": "零钱包存入:0", "bbox": [230, 791, 420, 814]},
	{"text": "周六会员日", "bbox": [225, 845, 387, 867]},
	{"text": "满49返15,满99返30", "bbox": [223, 870, 528, 891]},
	{"text": "此票据为购货凭证,请妥善保管", "bbox": [222, 894, 675, 916]}
]
2026-08-05 05:04:12,109 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=9.6s
2026-08-05 05:04:12,109 INFO     29 [qwen-vl-text] coord item[0]: text=欢迎光临健康大药房凤鸣分店, bbox=[278, 225, 647, 255]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[1]: text=日期：2026-02-08 09:50:51, bbox=[277, 245, 620, 274]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[2]: text=单号：2602080008000051, bbox=[275, 265, 607, 294]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[3]: text=会员号:73504会员姓名:李治刚, bbox=[273, 287, 655, 317]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[4]: text=收银员：050, bbox=[270, 308, 436, 333]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[5]: text=机号:01, bbox=[473, 317, 568, 338]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[6]: text=营业员：050, bbox=[270, 344, 434, 367]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[7]: text=编号:1440166, bbox=[514, 354, 690, 371]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[8]: text=名称:醋酸泼尼松片（强地松 4, bbox=[270, 367, 658, 394]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[9]: text=批号:LA24600, bbox=[264, 411, 450, 433]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[10]: text=规格:5mg*100p, bbox=[263, 433, 467, 457]
2026-08-05 05:04:12,110 INFO     29 [qwen-vl-text] coord item[11]: text=剂型:片剂, bbox=[261, 456, 392, 478]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[12]: text=单价:6.5 实价:6.5, bbox=[261, 478, 506, 501]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[13]: text=数量:1.金额:6.5, bbox=[258, 501, 472, 522]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[14]: text=收款方式:现金, bbox=[254, 546, 463, 568]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[15]: text=6.50, bbox=[513, 551, 571, 568]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[16]: text=数量合计:1.00, bbox=[252, 569, 452, 590]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[17]: text=应收额:6.50, bbox=[250, 592, 434, 613]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[18]: text=实收:6.50, bbox=[467, 594, 612, 614]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[19]: text=优惠额:0.00 找零:0.00, bbox=[244, 641, 600, 664]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[20]: text=本单为重打印小票!不作开票依据, bbox=[241, 665, 708, 689]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[21]: text=代金卡余额:0.00, bbox=[238, 690, 490, 712]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[22]: text=本单积分:1.7, bbox=[236, 715, 441, 737]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[23]: text=累计积分:27.7, bbox=[235, 740, 456, 762]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[24]: text=本单代金卡金额:0.0, bbox=[233, 765, 533, 788]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[25]: text=零钱包存入:0, bbox=[230, 791, 420, 814]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[26]: text=周六会员日, bbox=[225, 845, 387, 867]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[27]: text=满49返15,满99返30, bbox=[223, 870, 528, 891]
2026-08-05 05:04:12,111 INFO     29 [qwen-vl-text] coord item[28]: text=此票据为购货凭证,请妥善保管, bbox=[222, 894, 675, 916]
2026-08-05 05:04:12,113 INFO     29 [qwen-vl-text] page=3 — 30/30 coords, api_time=9.6s
2026-08-05 05:04:12,113 INFO     29 [qwen-vl-text] new_positions (30):
[[3, 165.48662646484374, 385.14333569335935, 238.11026000976562, 269.85829467773436], [3, 164.89135083007812, 369.0708935546875, 259.27561645507814, 289.96538330078124], [3, 163.70079956054687, 361.33231030273436, 280.44097290039065, 311.13073974609375], [3, 162.5102482910156, 389.90554077148437, 303.72286499023437, 335.4708996582031], [3, 160.72442138671875, 259.5401767578125, 325.9464892578125, 352.40318481445314], [3, 281.5653752441406, 338.11656054687495, 335.4708996582031, 357.69452392578125], [3, 160.72442138671875, 258.3496254882812, 364.044130859375, 388.38429077148436], [3, 305.9716762695312, 410.7401879882812, 374.62680908203123, 392.6173620605469], [3, 160.72442138671875, 391.69136767578124, 388.38429077148436, 416.95752197265625], [3, 157.15276757812498, 267.8740356445312, 434.94807495117186, 458.22996704101564], [3, 156.55749194335937, 277.99372143554683, 458.22996704101564, 483.62839477539063], [3, 155.3669406738281, 233.34804882812497, 482.570126953125, 505.8520190429687], [3, 155.3669406738281, 301.20947119140624, 505.8520190429687, 530.1921789550781], [3, 153.58111376953124, 280.970099609375, 530.1921789550781, 552.4158032226562], [3, 151.20001123046873, 275.6126188964844, 577.8142309570312, 601.096123046875], [3, 305.3764006347656, 339.9023874511718, 583.1055700683594, 601.096123046875], [3, 150.00945996093748, 269.0645869140625, 602.1543908691406, 624.3780151367188], [3, 148.81890869140625, 258.3496254882812, 626.49455078125, 648.7181750488281], [3, 277.99372143554683, 364.30868847656245, 628.6110864257812, 649.7764428710938], [3, 145.24725488281248, 357.165380859375, 678.3496740722657, 702.689833984375], [3, 143.46142797851562, 421.4551494140625, 703.7481018066406, 729.1465295410156], [3, 141.67560107421875, 291.68506103515625, 730.2047973632813, 753.486689453125], [3, 140.4850498046875, 262.5165549316406, 756.6614929199219, 779.9433850097656], [3, 139.88977416992185, 271.445689453125, 783.1181884765625, 806.4000805664062], [3, 138.69922290039062, 317.2819133300781, 809.5748840332031, 833.9150439453125], [3, 136.91339599609373, 250.0157666015625, 837.0898474121094, 861.4300073242188], [3, 133.9370178222656, 230.37167065429685, 894.2363098144531, 917.5182019042969], [3, 132.74646655273438, 314.30553515624996, 920.6930053710937, 942.9166296386719], [3, 132.15119091796873, 401.81105346679686, 946.0914331054687, 969.3733251953125], [3, 132.15119091796873, 401.81105346679686, 946.0914331054687, 969.3733251953125]]
2026-08-05 05:04:12,113 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=12.6s
2026-08-05 05:04:12,113 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:04:12,114 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:04:12,114 INFO     29 [qwen-vl-text] positions(33): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:04:12,114 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [33]
2026-08-05 05:04:12,598 INFO     29 [qwen-vl-text] page=4, rect=595x794, img=(1654x2205), dpi=200
2026-08-05 05:04:12,599 INFO     29 [qwen-vl-text] LLM extraction start, text_len=321
2026-08-05 05:04:12,599 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:04:12,599 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 183, \"bbox_end\": 215, \"encounter_dates\": [\"2025-12-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "医疗保险定点药店收费明细\n辽宁天士力大药房连锁有限公司\n药店名称：\n凤城石桥路店\n购药人：\n鲁药单：1\n2106210151\n个人编号：0000001017 票据号：100189\n563862\n序号 药品名称 数量 金额\n1 沙美特罗替卡 1.0 196.20\n松吸入粉雾剂\n2 沙美特罗替卡 1.0 196.20\n松吸入粉雾剂\n总金额：392.40\n人民币叁佰玖拾贰\n圆肆角整\n现金支\n账户支付：0.00\n392.40\n付：\n共济支\n统筹支付：0.0\n0.0\n付：\n公补：0.0\n消费前账户余额：0.00\n消费后账户余额：0.00\n2025.12.02\n消费时间：\n10:22:36\n收款员：2103\n无购药人、个人编号、药品明细购药单无效",
    "role": "user"
  }
]
[92m05:04:12 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:12,601 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:16,234 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:04:16,234 INFO     29 [qwen-vl-text] LLM output (len=704):
{
  "encounter_date": "2025-12-02",
  "pharmacy": "辽宁天士力大药房连锁有限公司凤城石桥路店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 1.0,
      "unit_price": null,
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
      "unit_price": null,
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
2026-08-05 05:04:16,234 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-02]
2026-08-05 05:04:16,242 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4231832, prompt_len=1033
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
2026-08-05 05:04:25,932 INFO     29 [qwen-vl-text] coord API raw response (len=1793):
[
	{"text": "医疗保险定点药店收费明细", "bbox": [113, 240, 325, 271]},
	{"text": "辽宁天士力大药房连锁有限公司", "bbox": [147, 275, 325, 300],
	"bbox": [147, 275, 325, 300]},
	{"text": "药店名称：", "bbox": [60, 295, 139, 312]},
	{"text": "凤城石桥路店", "bbox": [147, 314, 242, 330]},
	{"text": "购药人：", "bbox": [68, 336, 139, 352]},
	{"text": "鲁药单：1", "bbox": [250, 338, 294, 354]},
	{"text": "2106210151", "bbox": [146, 363, 241, 378]},
	{"text": "个人编号：0000001017 票据号：100189", "bbox": [59, 385, 331, 402]},
	{"text": "563862", "bbox": [145, 417, 203, 431]},
	{"text": "序号 药品名称 数量 金额", "bbox": [74, 440, 339, 460]},
	{"text": "1 沙美特罗替卡 1.0 196.20", "bbox": [85, 465, 346, 494]},
	{"text": "松吸入粉雾剂", "bbox": [142, 480, 240, 496]},
	{"text": "2 沙美特罗替卡 1.0 196.20", "bbox": [85, 502, 348, 528]},
	{"text": "松吸入粉雾剂", "bbox": [142, 513, 240, 528]},
	{"text": "总金额：392.40", "bbox": [64, 552, 195, 567]},
	{"text": "人民币叁佰玖拾贰", "bbox": [252, 537, 348, 561]},
	{"text": "圆肆角整", "bbox": [252, 568, 314, 584]},
	{"text": "现金支", "bbox": [250, 598, 297, 613]},
	{"text": "账户支付：0.00", "bbox": [53, 615, 176, 629]},
	{"text": "392.40", "bbox": [310, 617, 348, 636]},
	{"text": "付：", "bbox": [264, 630, 288, 644]},
	{"text": "共济支", "bbox": [248, 660, 296, 675]},
	{"text": "统筹支付：0.0", "bbox": [55, 677, 166, 691]},
	{"text": "0.0", "bbox": [309, 679, 333, 692]},
	{"text": "付：", "bbox": [263, 691, 286, 705]},
	{"text": "公补：0.0", "bbox": [65, 722, 103, 736]},
	{"text": "消费前账户余额：0.00", "bbox": [74, 744, 193, 758]},
	{"text": "消费后账户余额：0.00", "bbox": [75, 774, 193, 789]},
	{"text": "2025.12.02", "bbox": [140, 797, 225, 812]},
	{"text": "消费时间：", "bbox": [57, 813, 135, 830]},
	{"text": "10:22:36", "bbox": [140, 827, 206, 843]},
	{"text": "收款员：2103", "bbox": [246, 812, 345, 830]},
	{"text": "无购药人、个人编号、药品明细购药单无效", "bbox": [60, 847, 348, 870]}
]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.7s
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[0]: text=医疗保险定点药店收费明细, bbox=[113, 240, 325, 271]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[1]: text=辽宁天士力大药房连锁有限公司, bbox=[147, 275, 325, 300]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[2]: text=药店名称：, bbox=[60, 295, 139, 312]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[3]: text=凤城石桥路店, bbox=[147, 314, 242, 330]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[4]: text=购药人：, bbox=[68, 336, 139, 352]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[5]: text=鲁药单：1, bbox=[250, 338, 294, 354]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[6]: text=2106210151, bbox=[146, 363, 241, 378]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[7]: text=个人编号：0000001017 票据号：100189, bbox=[59, 385, 331, 402]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[8]: text=563862, bbox=[145, 417, 203, 431]
2026-08-05 05:04:25,933 INFO     29 [qwen-vl-text] coord item[9]: text=序号 药品名称 数量 金额, bbox=[74, 440, 339, 460]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[10]: text=1 沙美特罗替卡 1.0 196.20, bbox=[85, 465, 346, 494]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[11]: text=松吸入粉雾剂, bbox=[142, 480, 240, 496]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[12]: text=2 沙美特罗替卡 1.0 196.20, bbox=[85, 502, 348, 528]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[13]: text=松吸入粉雾剂, bbox=[142, 513, 240, 528]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[14]: text=总金额：392.40, bbox=[64, 552, 195, 567]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[15]: text=人民币叁佰玖拾贰, bbox=[252, 537, 348, 561]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[16]: text=圆肆角整, bbox=[252, 568, 314, 584]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[17]: text=现金支, bbox=[250, 598, 297, 613]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[18]: text=账户支付：0.00, bbox=[53, 615, 176, 629]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[19]: text=392.40, bbox=[310, 617, 348, 636]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[20]: text=付：, bbox=[264, 630, 288, 644]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[21]: text=共济支, bbox=[248, 660, 296, 675]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[22]: text=统筹支付：0.0, bbox=[55, 677, 166, 691]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[23]: text=0.0, bbox=[309, 679, 333, 692]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[24]: text=付：, bbox=[263, 691, 286, 705]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[25]: text=公补：0.0, bbox=[65, 722, 103, 736]
2026-08-05 05:04:25,934 INFO     29 [qwen-vl-text] coord item[26]: text=消费前账户余额：0.00, bbox=[74, 744, 193, 758]
2026-08-05 05:04:25,935 INFO     29 [qwen-vl-text] coord item[27]: text=消费后账户余额：0.00, bbox=[75, 774, 193, 789]
2026-08-05 05:04:25,935 INFO     29 [qwen-vl-text] coord item[28]: text=2025.12.02, bbox=[140, 797, 225, 812]
2026-08-05 05:04:25,935 INFO     29 [qwen-vl-text] coord item[29]: text=消费时间：, bbox=[57, 813, 135, 830]
2026-08-05 05:04:25,935 INFO     29 [qwen-vl-text] coord item[30]: text=10:22:36, bbox=[140, 827, 206, 843]
2026-08-05 05:04:25,935 INFO     29 [qwen-vl-text] coord item[31]: text=收款员：2103, bbox=[246, 812, 345, 830]
2026-08-05 05:04:25,935 INFO     29 [qwen-vl-text] coord item[32]: text=无购药人、个人编号、药品明细购药单无效, bbox=[60, 847, 348, 870]
2026-08-05 05:04:25,936 INFO     29 [qwen-vl-text] page=4 — 33/33 coords, api_time=9.7s
2026-08-05 05:04:25,936 INFO     29 [qwen-vl-text] new_positions (33):
[[4, 67.26614672851562, 193.4645812988281, 190.48820800781252, 215.09293487548828], [4, 87.50551831054686, 193.4645812988281, 218.26773834228516, 238.11026000976565], [4, 35.7165380859375, 82.74331323242187, 234.14175567626955, 247.63467041015628], [4, 87.50551831054686, 144.05670361328123, 249.2220721435547, 261.9212860107422], [4, 40.47874316406249, 82.74331323242187, 266.6834912109375, 279.382705078125], [4, 148.81890869140625, 175.01103662109372, 268.27089294433597, 280.97010681152346], [4, 86.91024267578125, 143.46142797851562, 288.11341461181644, 300.0189276123047], [4, 35.12126245117187, 197.03623510742185, 305.57483367919923, 319.06774841308595], [4, 86.31496704101562, 120.84095385742187, 330.9732614135742, 342.0850735473633], [4, 44.050396972656245, 201.79844018554687, 349.2283813476563, 365.10239868164064], [4, 50.59842895507812, 205.96536962890625, 369.07090301513676, 392.0882281494141], [4, 84.52914013671874, 142.86615234375, 380.97641601562503, 393.67562988281253], [4, 50.59842895507812, 207.15592089843747, 398.4378350830078, 419.0740576171875], [4, 84.52914013671874, 142.86615234375, 407.16854461669925, 419.0740576171875], [4, 38.097640625, 116.07874877929686, 438.12287841796876, 450.02839141845703], [4, 150.00945996093748, 207.15592089843747, 426.2173654174805, 445.26618621826174], [4, 150.00945996093748, 186.91654931640625, 450.82209228515626, 463.52130615234375], [4, 148.81890869140625, 176.79686352539062, 474.63311828613286, 486.5386312866211], [4, 31.54960864257812, 104.76851171874999, 488.1260330200196, 499.2378451538086], [4, 184.53544677734374, 207.15592089843747, 489.71343475341797, 504.79375122070314], [4, 157.15276757812498, 171.43938281249999, 500.03154602050785, 511.1433581542969], [4, 147.628357421875, 176.20158789062498, 523.8425720214844, 535.7480850219727], [4, 32.74015991210937, 98.81575537109374, 537.3354867553711, 548.4472988891602], [4, 183.94017114257812, 198.2267863769531, 538.9228884887696, 549.2409997558594], [4, 156.55749194335937, 170.24883154296873, 548.4472988891602, 559.5591110229493], [4, 38.692916259765624, 61.31339038085937, 573.052025756836, 584.163837890625], [4, 44.050396972656245, 114.88819750976562, 590.5134448242188, 601.6252569580079], [4, 44.64567260742187, 114.88819750976562, 614.3244708251954, 626.2299838256836], [4, 83.3385888671875, 133.9370178222656, 632.5795907592774, 644.4851037597657], [4, 33.930711181640625, 80.36221069335937, 645.2788046264649, 658.7717193603517], [4, 83.3385888671875, 122.62678076171873, 656.3906167602539, 669.0898306274414], [4, 146.43780615234374, 205.3700939941406, 644.4851037597657, 658.7717193603517], [4, 35.7165380859375, 207.15592089843747, 672.2646340942383, 690.5197540283203]]
2026-08-05 05:04:25,936 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=13.8s
2026-08-05 05:04:25,936 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:04:25,936 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:04:25,936 INFO     29 [qwen-vl-text] positions(33): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:04:25,936 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [33]
2026-08-05 05:04:26,444 INFO     29 [qwen-vl-text] page=4, rect=595x794, img=(1654x2205), dpi=200
2026-08-05 05:04:26,445 INFO     29 [qwen-vl-text] LLM extraction start, text_len=321
2026-08-05 05:04:26,445 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:04:26,445 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 216, \"bbox_end\": 248, \"encounter_dates\": [\"2026-02-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "医疗保险定点药店收费明细\n辽宁天士力大药房连锁有限公司\n药店名称：\n凤城石桥路店\n购药人：\n鲁药单：1\n2106210151\n个人编号：0000001017 票据号：100246\n563862\n序号 药品名称 数量 金额\n1 沙美特罗替卡 1.0 196.20\n松吸入粉雾剂\n2 沙美特罗替卡 1.0 196.20\n松吸入粉雾剂\n总金额：392.40\n人民币叁佰玖拾贰\n圆肆角整\n现金支\n账户支付：0.00\n392.40\n付：\n共济支\n统筹支付：0.0\n0.0\n付：\n公补：0.0\n消费前账户余额：0.00\n消费后账户余额：0.00\n2026.02.01\n消费时间：\n19:49:51\n收款员：2103\n无购药人、个人编号、药品明细购药单无效",
    "role": "user"
  }
]
[92m05:04:26 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:26,446 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:26,447 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:04:26.445+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 14, "failed": 0, "current": {"e1e244a2908a11f1a3da71efcdd7cc1f": {"id": "e1e244a2908a11f1a3da71efcdd7cc1f", "doc_id": "e1b14d16908a11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 6041420, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906159481, "task_type": "dataflow", "root_trace_id": "ee648f5612474f2494cdafbea4ad365d", "root_traceparent": "00-ee648f5612474f2494cdafbea4ad365d-00889eb88a3b4664-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:04:32,580 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:04:32,580 INFO     29 [qwen-vl-text] LLM output (len=704):
{
  "encounter_date": "2026-02-01",
  "pharmacy": "辽宁天士力大药房连锁有限公司凤城石桥路店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 1.0,
      "unit_price": null,
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
      "unit_price": null,
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
2026-08-05 05:04:32,580 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-01]
2026-08-05 05:04:32,593 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4231832, prompt_len=1033
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
2026-08-05 05:04:41,336 INFO     29 [qwen-vl-text] coord API raw response (len=1762):
[
	{"text": "医疗保险定点药店收费明细", "bbox": [113, 240, 325, 270]},
	{"text": "辽宁天士力大药房连锁有限公司", "bbox": [147, 275, 325, 300]},
	{"text": "药店名称：", "bbox": [60, 295, 139, 312]},
	{"text": "凤城石桥路店", "bbox": [147, 314, 242, 330]},
	{"text": "购药人：", "bbox": [68, 336, 139, 352]},
	{"text": "鲁药单：1", "bbox": [250, 338, 294, 354]},
	{"text": "2106210151", "bbox": [146, 363, 241, 378]},
	{"text": "个人编号：0000001017 票据号：100189", "bbox": [59, 384, 331, 402]},
	{"text": "563862", "bbox": [145, 417, 203, 431]},
	{"text": "序号 药品名称 数量 金额", "bbox": [74, 440, 339, 460]},
	{"text": "1 沙美特罗替卡 1.0 196.20", "bbox": [85, 465, 346, 493]},
	{"text": "松吸入粉雾剂", "bbox": [142, 480, 240, 496]},
	{"text": "2 沙美特罗替卡 1.0 196.20", "bbox": [84, 502, 348, 528]},
	{"text": "松吸入粉雾剂", "bbox": [142, 513, 240, 528]},
	{"text": "总金额：392.40", "bbox": [64, 551, 195, 567]},
	{"text": "人民币叁佰玖拾贰", "bbox": [251, 537, 348, 560]},
	{"text": "圆肆角整", "bbox": [251, 568, 314, 584]},
	{"text": "现金支", "bbox": [250, 598, 297, 613]},
	{"text": "账户支付：0.00", "bbox": [53, 614, 176, 629]},
	{"text": "392.40", "bbox": [310, 616, 348, 636]},
	{"text": "付：", "bbox": [264, 630, 287, 644]},
	{"text": "共济支", "bbox": [248, 660, 296, 675]},
	{"text": "统筹支付：0.0", "bbox": [55, 677, 167, 691]},
	{"text": "0.0", "bbox": [308, 679, 333, 692]},
	{"text": "付：", "bbox": [263, 691, 285, 705]},
	{"text": "公补：0.0", "bbox": [65, 721, 103, 736]},
	{"text": "消费前账户余额：0.00", "bbox": [74, 743, 193, 758]},
	{"text": "消费后账户余额：0.00", "bbox": [75, 773, 193, 789]},
	{"text": "2026.02.01", "bbox": [548, 787, 634, 808]},
	{"text": "消费时间：", "bbox": [57, 813, 135, 830]},
	{"text": "19:49:51", "bbox": [546, 821, 611, 841]},
	{"text": "收款员：2103", "bbox": [658, 813, 768, 838]},
	{"text": "无购药人、个人编号、药品明细购药单无效", "bbox": [60, 847, 348, 870]}
]
2026-08-05 05:04:41,336 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=8.7s
2026-08-05 05:04:41,336 INFO     29 [qwen-vl-text] coord item[0]: text=医疗保险定点药店收费明细, bbox=[113, 240, 325, 270]
2026-08-05 05:04:41,336 INFO     29 [qwen-vl-text] coord item[1]: text=辽宁天士力大药房连锁有限公司, bbox=[147, 275, 325, 300]
2026-08-05 05:04:41,336 INFO     29 [qwen-vl-text] coord item[2]: text=药店名称：, bbox=[60, 295, 139, 312]
2026-08-05 05:04:41,336 INFO     29 [qwen-vl-text] coord item[3]: text=凤城石桥路店, bbox=[147, 314, 242, 330]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[4]: text=购药人：, bbox=[68, 336, 139, 352]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[5]: text=鲁药单：1, bbox=[250, 338, 294, 354]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[6]: text=2106210151, bbox=[146, 363, 241, 378]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[7]: text=个人编号：0000001017 票据号：100189, bbox=[59, 384, 331, 402]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[8]: text=563862, bbox=[145, 417, 203, 431]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[9]: text=序号 药品名称 数量 金额, bbox=[74, 440, 339, 460]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[10]: text=1 沙美特罗替卡 1.0 196.20, bbox=[85, 465, 346, 493]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[11]: text=松吸入粉雾剂, bbox=[142, 480, 240, 496]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[12]: text=2 沙美特罗替卡 1.0 196.20, bbox=[84, 502, 348, 528]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[13]: text=松吸入粉雾剂, bbox=[142, 513, 240, 528]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[14]: text=总金额：392.40, bbox=[64, 551, 195, 567]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[15]: text=人民币叁佰玖拾贰, bbox=[251, 537, 348, 560]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[16]: text=圆肆角整, bbox=[251, 568, 314, 584]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[17]: text=现金支, bbox=[250, 598, 297, 613]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[18]: text=账户支付：0.00, bbox=[53, 614, 176, 629]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[19]: text=392.40, bbox=[310, 616, 348, 636]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[20]: text=付：, bbox=[264, 630, 287, 644]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[21]: text=共济支, bbox=[248, 660, 296, 675]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[22]: text=统筹支付：0.0, bbox=[55, 677, 167, 691]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[23]: text=0.0, bbox=[308, 679, 333, 692]
2026-08-05 05:04:41,337 INFO     29 [qwen-vl-text] coord item[24]: text=付：, bbox=[263, 691, 285, 705]
2026-08-05 05:04:41,338 INFO     29 [qwen-vl-text] coord item[25]: text=公补：0.0, bbox=[65, 721, 103, 736]
2026-08-05 05:04:41,338 INFO     29 [qwen-vl-text] coord item[26]: text=消费前账户余额：0.00, bbox=[74, 743, 193, 758]
2026-08-05 05:04:41,338 INFO     29 [qwen-vl-text] coord item[27]: text=消费后账户余额：0.00, bbox=[75, 773, 193, 789]
2026-08-05 05:04:41,338 INFO     29 [qwen-vl-text] coord item[28]: text=2026.02.01, bbox=[548, 787, 634, 808]
2026-08-05 05:04:41,338 INFO     29 [qwen-vl-text] coord item[29]: text=消费时间：, bbox=[57, 813, 135, 830]
2026-08-05 05:04:41,338 INFO     29 [qwen-vl-text] coord item[30]: text=19:49:51, bbox=[546, 821, 611, 841]
2026-08-05 05:04:41,338 INFO     29 [qwen-vl-text] coord item[31]: text=收款员：2103, bbox=[658, 813, 768, 838]
2026-08-05 05:04:41,338 INFO     29 [qwen-vl-text] coord item[32]: text=无购药人、个人编号、药品明细购药单无效, bbox=[60, 847, 348, 870]
2026-08-05 05:04:41,339 INFO     29 [qwen-vl-text] page=4 — 33/33 coords, api_time=8.7s
2026-08-05 05:04:41,339 INFO     29 [qwen-vl-text] new_positions (33):
[[4, 67.26614672851562, 193.4645812988281, 190.48820800781252, 214.29923400878909], [4, 87.50551831054686, 193.4645812988281, 218.26773834228516, 238.11026000976565], [4, 35.7165380859375, 82.74331323242187, 234.14175567626955, 247.63467041015628], [4, 87.50551831054686, 144.05670361328123, 249.2220721435547, 261.9212860107422], [4, 40.47874316406249, 82.74331323242187, 266.6834912109375, 279.382705078125], [4, 148.81890869140625, 175.01103662109372, 268.27089294433597, 280.97010681152346], [4, 86.91024267578125, 143.46142797851562, 288.11341461181644, 300.0189276123047], [4, 35.12126245117187, 197.03623510742185, 304.7811328125, 319.06774841308595], [4, 86.31496704101562, 120.84095385742187, 330.9732614135742, 342.0850735473633], [4, 44.050396972656245, 201.79844018554687, 349.2283813476563, 365.10239868164064], [4, 50.59842895507812, 205.96536962890625, 369.07090301513676, 391.29452728271485], [4, 84.52914013671874, 142.86615234375, 380.97641601562503, 393.67562988281253], [4, 50.00315332031249, 207.15592089843747, 398.4378350830078, 419.0740576171875], [4, 84.52914013671874, 142.86615234375, 407.16854461669925, 419.0740576171875], [4, 38.097640625, 116.07874877929686, 437.32917755126954, 450.02839141845703], [4, 149.41418432617186, 207.15592089843747, 426.2173654174805, 444.4724853515625], [4, 149.41418432617186, 186.91654931640625, 450.82209228515626, 463.52130615234375], [4, 148.81890869140625, 176.79686352539062, 474.63311828613286, 486.5386312866211], [4, 31.54960864257812, 104.76851171874999, 487.33233215332035, 499.2378451538086], [4, 184.53544677734374, 207.15592089843747, 488.9197338867188, 504.79375122070314], [4, 157.15276757812498, 170.84410717773437, 500.03154602050785, 511.1433581542969], [4, 147.628357421875, 176.20158789062498, 523.8425720214844, 535.7480850219727], [4, 32.74015991210937, 99.41103100585937, 537.3354867553711, 548.4472988891602], [4, 183.34489550781248, 198.2267863769531, 538.9228884887696, 549.2409997558594], [4, 156.55749194335937, 169.65355590820312, 548.4472988891602, 559.5591110229493], [4, 38.692916259765624, 61.31339038085937, 572.2583248901368, 584.163837890625], [4, 44.050396972656245, 114.88819750976562, 589.7197439575195, 601.6252569580079], [4, 44.64567260742187, 114.88819750976562, 613.5307699584961, 626.2299838256836], [4, 326.21104785156245, 377.40475244140623, 624.6425820922852, 641.3103002929688], [4, 33.930711181640625, 80.36221069335937, 645.2788046264649, 658.7717193603517], [4, 325.0204965820312, 363.71341284179687, 651.6284115600587, 667.502428894043], [4, 391.69136767578124, 457.17168749999996, 645.2788046264649, 665.1213262939453], [4, 35.7165380859375, 207.15592089843747, 672.2646340942383, 690.5197540283203]]
2026-08-05 05:04:41,339 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=15.4s
2026-08-05 05:04:41,348 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 05:04:41,348 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Medication | outputs={"chunks": "3 items, types={'MedicationRecord': 3}", "html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:04:41,348 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 05:04:41,353 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:04:41,353 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:04:41 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:41,354 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:42,289 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:04:42,299 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 05:04:42,299 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:04:42,299 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 05:04:42,305 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:04:42,305 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-05 05:04:42,305 INFO     29 [qwen-vl-text] positions(99): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:04:42,305 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [99]
2026-08-05 05:04:42,536 INFO     29 [qwen-vl-text] page=0, rect=595x870, img=(1654x2418), dpi=200
2026-08-05 05:04:42,537 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1124
2026-08-05 05:04:42,537 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:04:42,537 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 0, \"bbox_end\": 98, \"encounter_dates\": [\"2024-10-08\", \"2024-10-15\"], \"department\": \"内四科病房\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "信4个月\n医疗机构：凤城市中医院\n(组织机构代码：46376203-6)\n医疗付费方式：城镇医保\n中医住院病案首页\n02410974\n健康卡号：\n第3次入院\n病案号：290510\n姓名：\n性别：1.男2.女出生日期：1958-12-09\n年龄：65岁\n国籍：中国\n(年龄不足一周岁的)年龄：\n新生儿出生体重：\n克\n新生儿入院体重：\n克\n出生地点：辽宁省凤城市\n籍贯：辽宁省\n民族：汉族\n身份证号：\n职业：退(离)休人\n婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他\n现地址：凤城市胜利委十组060644\n邮编：118100\n户口地址：凤城市胜利委十组060644\n邮编：118100\n工作单位：电业局\n邮编：118100\n联系人姓名：李治刚\n关系：本人或户\n地址：凤城市胜利委十组060644\n9\n入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他\n治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医\n入院时间：2024-10-08\n入院科别：内四科病房\n病房：11\n转科科别：\n出院时间：2024-10-15\n出院科别：内四科病房\n病房：\n实际住院：7 天\n门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)\n疾病编码：A04.04.04.02,A04.04.04.02\n门(急)诊诊断(西医诊断)：肺部感染\n疾病编码：J98.414\n实施临床路径：3 1.中医2.西医3否\n使用医疗机构中药制剂：2 1.是2.否\n使用中医诊疗设备：1 1.是2.否\n使用中医诊疗技术：1 1.是2.否\n辨证施护：1 1.是2.否\n出院中医诊断\n疾病编码\n入院\n病情\n出院西医诊断\n疾病编码\n入院\n病情\n主病：喘病(可选词：喘证)\nA04.04.04.02\n1\n主要诊断：支气管哮喘\nJ45.900x001\n1\n主证：风寒袭肺证\n1\n其他诊断：冠状动脉粥样硬化性心脏\nI25.103\n1\n其他诊断：心功能II级(NYHA分级)\nI50.900x007\n1\n其他诊断：特应性神经性皮炎\nL20.803\n1\n入院病情：1.有，2.临床未确定，3.情况不明，4.无\n损伤、中毒的外部原因：\n疾病编码：\n病理诊断：\n疾病编码：\n病理号：\n药物过敏：1 1.无2.有过敏药物：\n死亡患者尸检：2 1.是2.否\n血型：1.A 2.B 3.0 4.AB 5.不详 6.未查\nRh 4 1.阴2.阳3.不详4.未查\n科主任：李革\n主任(副主任)医师：李革\n主治医师：宋文平\n住院医师：刘\n责任护士：唐莹莹\n进修医师：\n实习医师：\n编码员：\n病案质量 1 1.甲2.乙3.丙质控医师：刘\n质控护士：杨\n质控日期：2024-10-17",
    "role": "user"
  }
]
[92m05:04:42 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:42,538 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:04:48,075 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:04:48,075 INFO     29 [qwen-vl-text] LLM output (len=1246):
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
      "name": "喘病(风寒袭肺证)",
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
      "name": "喘病(风寒袭肺证)",
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
2026-08-05 05:04:48,075 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-10-15]
2026-08-05 05:04:48,078 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2465600, prompt_len=2034
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共99行）
["信4个月", "医疗机构：凤城市中医院", "(组织机构代码：46376203-6)", "医疗付费方式：城镇医保", "中医住院病案首页", "02410974", "健康卡号：", "第3次入院", "病案号：290510", "姓名：", "性别：1.男2.女出生日期：1958-12-09", "年龄：65岁", "国籍：中国", "(年龄不足一周岁的)年龄：", "新生儿出生体重：", "克", "新生儿入院体重：", "克", "出生地点：辽宁省凤城市", "籍贯：辽宁省", "民族：汉族", "身份证号：", "职业：退(离)休人", "婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他", "现地址：凤城市胜利委十组060644", "邮编：118100", "户口地址：凤城市胜利委十组060644", "邮编：118100", "工作单位：电业局", "邮编：118100", "联系人姓名：李治刚", "关系：本人或户", "地址：凤城市胜利委十组060644", "9", "入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他", "治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医", "入院时间：2024-10-08", "入院科别：内四科病房", "病房：11", "转科科别：", "出院时间：2024-10-15", "出院科别：内四科病房", "病房：", "实际住院：7 天", "门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)", "疾病编码：A04.04.04.02,A04.04.04.02", "门(急)诊诊断(西医诊断)：肺部感染", "疾病编码：J98.414", "实施临床路径：3 1.中医2.西医3否", "使用医疗机构中药制剂：2 1.是2.否", "使用中医诊疗设备：1 1.是2.否", "使用中医诊疗技术：1 1.是2.否", "辨证施护：1 1.是2.否", "出院中医诊断", "疾病编码", "入院", "病情", "出院西医诊断", "疾病编码", "入院", "病情", "主病：喘病(可选词：喘证)", "A04.04.04.02", "1", "主要诊断：支气管哮喘", "J45.900x001", "1", "主证：风寒袭肺证", "1", "其他诊断：冠状动脉粥样硬化性心脏", "I25.103", "1", "其他诊断：心功能II级(NYHA分级)", "I50.900x007", "1", "其他诊断：特应性神经性皮炎", "L20.803", "1", "入院病情：1.有，2.临床未确定，3.情况不明，4.无", "损伤、中毒的外部原因：", "疾病编码：", "病理诊断：", "疾病编码：", "病理号：", "药物过敏：1 1.无2.有过敏药物：", "死亡患者尸检：2 1.是2.否", "血型：1.A 2.B 3.0 4.AB 5.不详 6.未查", "Rh 4 1.阴2.阳3.不详4.未查", "科主任：李革", "主任(副主任)医师：李革", "主治医师：宋文平", "住院医师：刘", "责任护士：唐莹莹", "进修医师：", "实习医师：", "编码员：", "病案质量 1 1.甲2.乙3.丙质控医师：刘", "质控护士：杨", "质控日期：2024-10-17"]

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
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord API raw response (len=8009):
[
	{"text": "信4个月", "bbox": [100, 33, 206, 67]},
	{"text": "医疗机构：凤城市中医院", "bbox": [277, 63, 466, 74]},
	{"text": "(组织机构代码：46376203-6)", "bbox": [617, 58, 848, 70]},
	{"text": "医疗付费方式：城镇医保", "bbox": [116, 85, 270, 98]},
	{"text": "中医住院病案首页", "bbox": [377, 82, 627, 97]},
	{"text": "02410974", "bbox": [721, 75, 863, 93]},
	{"text": "健康卡号：", "bbox": [113, 100, 174, 110]},
	{"text": "第3次入院", "bbox": [456, 105, 534, 115]},
	{"text": "病案号：290510", "bbox": [690, 104, 786, 113]},
	{"text": "姓名：", "bbox": [109, 117, 144, 127]},
	{"text": "性别：1.男2.女出生日期：1958-12-09", "bbox": [293, 119, 562, 130]},
	{"text": "年龄：65岁", "bbox": [632, 120, 695, 130]},
	{"text": "国籍：中国", "bbox": [737, 120, 804, 130]},
	{"text": "(年龄不足一周岁的)年龄：", "bbox": [148, 133, 320, 144], "bbox": [148, 133, 320, 144]},
	{"text": "新生儿出生体重：", "bbox": [413, 136, 517, 145], "bbox": [413, 136, 517, 145]},
	{"text": "克", "bbox": [595, 136, 610, 145], "bbox": [595, 136, 610, 145]},
	{"text": "新生儿入院体重：", "bbox": [634, 136, 736, 146], "bbox": [634, 136, 736, 146]},
	{"text": "克", "bbox": [838, 134, 853, 144], "bbox": [838, 134, 853, 144]},
	{"text": "出生地点：辽宁省凤城市", "bbox": [106, 147, 262, 158], "bbox": [106, 147, 262, 158]},
	{"text": "籍贯：辽宁省", "bbox": [532, 151, 610, 161], "bbox": [532, 151, 610, 161]},
	{"text": "民族：汉族", "bbox": [718, 152, 791, 161], "bbox": [718, 152, 791, 161]},
	{"text": "身份证号：", "bbox": [105, 161, 167, 171], "bbox": [105, 161, 167, 171]},
	{"text": "职业：退(离)休人", "bbox": [394, 164, 500, 174], "bbox": [394, 164, 500, 174]},
	{"text": "婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他", "bbox": [531, 165, 841, 176], "bbox": [531, 165, 841, 176]},
	{"text": "现地址：凤城市胜利委十组060644", "bbox": [101, 176, 318, 188], "bbox": [101, 176, 318, 188]},
	{"text": "邮编：118100", "bbox": [720, 181, 800, 190], "bbox": [720, 181, 800, 190]},
	{"text": "户口地址：凤城市胜利委十组060644", "bbox": [98, 190, 331, 201], "bbox": [98, 190, 331, 201]},
	{"text": "邮编：118100", "bbox": [720, 196, 804, 205], "bbox": [720, 196, 804, 205]},
	{"text": "工作单位：电业局", "bbox": [97, 204, 212, 214], "bbox": [97, 204, 212, 214]},
	{"text": "邮编：118100", "bbox": [721, 210, 804, 219], "bbox": [721, 210, 804, 219]},
	{"text": "联系人姓名：李治刚", "bbox": [93, 219, 223, 230], "bbox": [93, 219, 223, 230]},
	{"text": "关系：本人或户", "bbox": [338, 221, 437, 232], "bbox": [338, 221, 437, 232]},
	{"text": "地址：凤城市胜利委十组060644", "bbox": [470, 223, 675, 234], "bbox": [470, 223, 675, 234]},
	{"text": "9", "bbox": [827, 224, 841, 233], "bbox": [827, 224, 841, 233]},
	{"text": "入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他", "bbox": [90, 234, 477, 247], "bbox": [90, 234, 477, 247]},
	{"text": "治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医", "bbox": [505, 237, 882, 249], "bbox": [505, 237, 882, 249]},
	{"text": "入院时间：2024-10-08", "bbox": [87, 249, 235, 260], "bbox": [87, 249, 235, 260]},
	{"text": "入院科别：内四科病房", "bbox": [332, 252, 474, 263], "bbox": [332, 252, 474, 263]},
	{"text": "病房：11", "bbox": [553, 253, 604, 263], "bbox": [553, 253, 604, 263]},
	{"text": "转科科别：", "bbox": [721, 255, 810, 265], "bbox": [721, 255, 810, 265]},
	{"text": "出院时间：2024-10-15", "bbox": [85, 263, 235, 274], "bbox": [85, 263, 235, 274]},
	{"text": "出院科别：内四科病房", "bbox": [330, 266, 473, 277], "bbox": [330, 266, 473, 277]},
	{"text": "病房：", "bbox": [553, 266, 604, 277], "bbox": [553, 266, 604, 277]},
	{"text": "实际住院：7 天", "bbox": [722, 267, 878, 278], "bbox": [722, 267, 878, 278]},
	{"text": "门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证)", "bbox": [83, 276, 553, 289], "bbox": [83, 276, 553, 289]},
	{"text": "疾病编码：A04.04.04.02,A04.04.04.02", "bbox": [583, 281, 835, 292], "bbox": [583, 281, 835, 292]},
	{"text": "门(急)诊诊断(西医诊断)：肺部感染", "bbox": [81, 291, 322, 303], "bbox": [81, 291, 322, 303]},
	{"text": "疾病编码：J98.414", "bbox": [583, 295, 702, 306], "bbox": [583, 295, 702, 306]},
	{"text": "实施临床路径：3 1.中医2.西医3否", "bbox": [113, 309, 420, 322], "bbox": [113, 309, 420, 322]},
	{"text": "使用医疗机构中药制剂：2 1.是2.否", "bbox": [496, 312, 760, 325], "bbox": [496, 312, 760, 325]},
	{"text": "使用中医诊疗设备：1 1.是2.否", "bbox": [80, 326, 320, 339], "bbox": [80, 326, 320, 339]},
	{"text": "使用中医诊疗技术：1 1.是2.否", "bbox": [372, 328, 604, 341], "bbox": [372, 328, 604, 341]},
	{"text": "辨证施护：1 1.是2.否", "bbox": [715, 329, 888, 343], "bbox": [715, 329, 888, 343]},
	{"text": "出院中医诊断", "bbox": [162, 347, 254, 358], "bbox": [162, 347, 254, 358]},
	{"text": "疾病编码", "bbox": [374, 349, 437, 359], "bbox": [374, 349, 437, 359]},
	{"text": "入院", "bbox": [461, 344, 493, 355], "bbox": [461, 344, 493, 355]},
	{"text": "病情", "bbox": [461, 355, 493, 366], "bbox": [461, 355, 493, 366]},
	{"text": "出院西医诊断", "bbox": [579, 350, 668, 360], "bbox": [579, 350, 668, 360]},
	{"text": "疾病编码", "bbox": [768, 351, 829, 361], "bbox": [768, 351, 829, 361]},
	{"text": "入院", "bbox": [855, 347, 887, 358], "bbox": [855, 347, 887, 358]},
	{"text": "病情", "bbox": [855, 358, 887, 369], "bbox": [855, 358, 887, 369]},
	{"text": "主病：喘病(可选词：喘证)", "bbox": [62, 368, 249, 380], "bbox": [62, 368, 249, 380]},
	{"text": "A04.04.04.02", "bbox": [358, 371, 454, 381], "bbox": [358, 371, 454, 381]},
	{"text": "1", "bbox": [458, 371, 467, 381], "bbox": [458, 371, 467, 381]},
	{"text": "主要诊断：支气管哮喘", "bbox": [505, 371, 645, 382], "bbox": [505, 371, 645, 382]},
	{"text": "J45.900x001", "bbox": [754, 373, 839, 383], "bbox": [754, 373, 839, 383]},
	{"text": "1", "bbox": [857, 374, 866, 384], "bbox": [857, 374, 866, 384]},
	{"text": "主证：风寒袭肺证", "bbox": [60, 387, 176, 399], "bbox": [60, 387, 176, 399]},
	{"text": "1", "bbox": [458, 391, 467, 400], "bbox": [458, 391, 467, 400]},
	{"text": "其他诊断：冠状动脉粥样硬化性心脏", "bbox": [504, 390, 737, 402], "bbox": [504, 390, 737, 402]},
	{"text": "I25.103", "bbox": [755, 392, 810, 402], "bbox": [755, 392, 810, 402]},
	{"text": "1", "bbox": [858, 393, 867, 403], "bbox": [858, 393, 867, 403]},
	{"text": "其他诊断：心功能II级(NYHA分级)", "bbox": [504, 410, 721, 422], "bbox": [504, 410, 721, 422]},
	{"text": "I50.900x007", "bbox": [757, 412, 844, 422], "bbox": [757, 412, 844, 422]},
	{"text": "1", "bbox": [860, 413, 869, 423], "bbox": [860, 413, 869, 423]},
	{"text": "其他诊断：特应性神经性皮炎", "bbox": [504, 428, 694, 440], "bbox": [504, 428, 694, 440]},
	{"text": "L20.803", "bbox": [758, 431, 815, 441], "bbox": [758, 431, 815, 441]},
	{"text": "1", "bbox": [863, 432, 872, 442], "bbox": [863, 432, 872, 442]},
	{"text": "入院病情：1.有，2.临床未确定，3.情况不明，4.无", "bbox": [14, 601, 405, 614], "bbox": [14, 601, 405, 614]},
	{"text": "损伤、中毒的外部原因：", "bbox": [45, 627, 241, 641], "bbox": [45, 627, 241, 641]},
	{"text": "疾病编码：", "bbox": [701, 630, 796, 643], "bbox": [701, 630, 796, 643]},
	{"text": "病理诊断：", "bbox": [45, 653, 142, 667], "bbox": [45, 653, 142, 667]},
	{"text": "疾病编码：", "bbox": [39, 674, 138, 688], "bbox": [39, 674, 138, 688]},
	{"text": "病理号：", "bbox": [448, 675, 530, 689], "bbox": [448, 675, 530, 689]},
	{"text": "药物过敏：1 1.无2.有过敏药物：", "bbox": [32, 699, 347, 714], "bbox": [32, 699, 347, 714]},
	{"text": "死亡患者尸检：2 1.是2.否", "bbox": [710, 703, 938, 719], "bbox": [710, 703, 938, 719]},
	{"text": "血型：1.A 2.B 3.0 4.AB 5.不详 6.未查", "bbox": [27, 728, 437, 744], "bbox": [27, 728, 437, 744]},
	{"text": "Rh 4 1.阴2.阳3.不详4.未查", "bbox": [555, 727, 828, 746], "bbox": [555, 727, 828, 746]},
	{"text": "科主任：李革", "bbox": [22, 756, 122, 773], "bbox": [22, 756, 122, 773]},
	{"text": "主任(副主任)医师：李革", "bbox": [240, 756, 432, 773], "bbox": [240, 756, 432, 773]},
	{"text": "主治医师：宋文平", "bbox": [553, 756, 688, 773], "bbox": [553, 756, 688, 773]},
	{"text": "住院医师：刘", "bbox": [770, 756, 854, 775], "bbox": [770, 756, 854, 775]},
	{"text": "责任护士：唐莹莹", "bbox": [18, 781, 150, 798], "bbox": [18, 781, 150, 798]},
	{"text": "进修医师：", "bbox": [310, 783, 413, 800], "bbox": [310, 783, 413, 800]},
	{"text": "实习医师：", "bbox": [552, 783, 654, 800], "bbox": [552, 783, 654, 800]},
	{"text": "编码员：", "bbox": [789, 787, 851, 801], "bbox": [789, 787, 851, 801]},
	{"text": "病案质量 1 1.甲2.乙3.丙质控医师：刘", "bbox": [2, 811, 387, 832], "bbox": [2, 811, 387, 832]},
	{"text": "质控护士：杨", "bbox": [478, 814, 621, 832], "bbox": [478, 814, 621, 832]},
	{"text": "质控日期：2024-10-17", "bbox": [720, 817, 910, 833], "bbox": [720, 817, 910, 833]}
]
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord API: raw_items=99, valid_items=99, elapsed=42.9s
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord item[0]: text=信4个月, bbox=[100, 33, 206, 67]
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord item[1]: text=医疗机构：凤城市中医院, bbox=[277, 63, 466, 74]
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord item[2]: text=(组织机构代码：46376203-6), bbox=[617, 58, 848, 70]
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord item[3]: text=医疗付费方式：城镇医保, bbox=[116, 85, 270, 98]
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord item[4]: text=中医住院病案首页, bbox=[377, 82, 627, 97]
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord item[5]: text=02410974, bbox=[721, 75, 863, 93]
2026-08-05 05:05:30,936 INFO     29 [qwen-vl-text] coord item[6]: text=健康卡号：, bbox=[113, 100, 174, 110]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[7]: text=第3次入院, bbox=[456, 105, 534, 115]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[8]: text=病案号：290510, bbox=[690, 104, 786, 113]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[9]: text=姓名：, bbox=[109, 117, 144, 127]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[10]: text=性别：1.男2.女出生日期：1958-12-09, bbox=[293, 119, 562, 130]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[11]: text=年龄：65岁, bbox=[632, 120, 695, 130]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[12]: text=国籍：中国, bbox=[737, 120, 804, 130]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[13]: text=(年龄不足一周岁的)年龄：, bbox=[148, 133, 320, 144]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[14]: text=新生儿出生体重：, bbox=[413, 136, 517, 145]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[15]: text=克, bbox=[595, 136, 610, 145]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[16]: text=新生儿入院体重：, bbox=[634, 136, 736, 146]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[17]: text=克, bbox=[838, 134, 853, 144]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[18]: text=出生地点：辽宁省凤城市, bbox=[106, 147, 262, 158]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[19]: text=籍贯：辽宁省, bbox=[532, 151, 610, 161]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[20]: text=民族：汉族, bbox=[718, 152, 791, 161]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[21]: text=身份证号：, bbox=[105, 161, 167, 171]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[22]: text=职业：退(离)休人, bbox=[394, 164, 500, 174]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[23]: text=婚姻：9 1.未婚2.已婚3.丧偶4.离婚9.其他, bbox=[531, 165, 841, 176]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[24]: text=现地址：凤城市胜利委十组060644, bbox=[101, 176, 318, 188]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[25]: text=邮编：118100, bbox=[720, 181, 800, 190]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[26]: text=户口地址：凤城市胜利委十组060644, bbox=[98, 190, 331, 201]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[27]: text=邮编：118100, bbox=[720, 196, 804, 205]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[28]: text=工作单位：电业局, bbox=[97, 204, 212, 214]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[29]: text=邮编：118100, bbox=[721, 210, 804, 219]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[30]: text=联系人姓名：李治刚, bbox=[93, 219, 223, 230]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[31]: text=关系：本人或户, bbox=[338, 221, 437, 232]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[32]: text=地址：凤城市胜利委十组060644, bbox=[470, 223, 675, 234]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[33]: text=9, bbox=[827, 224, 841, 233]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[34]: text=入院途径：1 1.门诊2.急诊3.其他医疗机构转入9.其他, bbox=[90, 234, 477, 247]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[35]: text=治疗类别：2 1.中医(1.1中医1.2民族医)2.中西医3.西医, bbox=[505, 237, 882, 249]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[36]: text=入院时间：2024-10-08, bbox=[87, 249, 235, 260]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[37]: text=入院科别：内四科病房, bbox=[332, 252, 474, 263]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[38]: text=病房：11, bbox=[553, 253, 604, 263]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[39]: text=转科科别：, bbox=[721, 255, 810, 265]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[40]: text=出院时间：2024-10-15, bbox=[85, 263, 235, 274]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[41]: text=出院科别：内四科病房, bbox=[330, 266, 473, 277]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[42]: text=病房：, bbox=[553, 266, 604, 277]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[43]: text=实际住院：7 天, bbox=[722, 267, 878, 278]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[44]: text=门(急)诊诊断(中医诊断)：喘病(可选词：喘证),喘病(可选词：喘证), bbox=[83, 276, 553, 289]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[45]: text=疾病编码：A04.04.04.02,A04.04.04.02, bbox=[583, 281, 835, 292]
2026-08-05 05:05:30,937 INFO     29 [qwen-vl-text] coord item[46]: text=门(急)诊诊断(西医诊断)：肺部感染, bbox=[81, 291, 322, 303]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[47]: text=疾病编码：J98.414, bbox=[583, 295, 702, 306]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[48]: text=实施临床路径：3 1.中医2.西医3否, bbox=[113, 309, 420, 322]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[49]: text=使用医疗机构中药制剂：2 1.是2.否, bbox=[496, 312, 760, 325]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[50]: text=使用中医诊疗设备：1 1.是2.否, bbox=[80, 326, 320, 339]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[51]: text=使用中医诊疗技术：1 1.是2.否, bbox=[372, 328, 604, 341]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[52]: text=辨证施护：1 1.是2.否, bbox=[715, 329, 888, 343]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[53]: text=出院中医诊断, bbox=[162, 347, 254, 358]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[54]: text=疾病编码, bbox=[374, 349, 437, 359]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[55]: text=入院, bbox=[461, 344, 493, 355]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[56]: text=病情, bbox=[461, 355, 493, 366]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[57]: text=出院西医诊断, bbox=[579, 350, 668, 360]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[58]: text=疾病编码, bbox=[768, 351, 829, 361]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[59]: text=入院, bbox=[855, 347, 887, 358]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[60]: text=病情, bbox=[855, 358, 887, 369]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[61]: text=主病：喘病(可选词：喘证), bbox=[62, 368, 249, 380]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[62]: text=A04.04.04.02, bbox=[358, 371, 454, 381]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[63]: text=1, bbox=[458, 371, 467, 381]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[64]: text=主要诊断：支气管哮喘, bbox=[505, 371, 645, 382]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[65]: text=J45.900x001, bbox=[754, 373, 839, 383]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[66]: text=1, bbox=[857, 374, 866, 384]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[67]: text=主证：风寒袭肺证, bbox=[60, 387, 176, 399]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[68]: text=1, bbox=[458, 391, 467, 400]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[69]: text=其他诊断：冠状动脉粥样硬化性心脏, bbox=[504, 390, 737, 402]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[70]: text=I25.103, bbox=[755, 392, 810, 402]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[71]: text=1, bbox=[858, 393, 867, 403]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[72]: text=其他诊断：心功能II级(NYHA分级), bbox=[504, 410, 721, 422]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[73]: text=I50.900x007, bbox=[757, 412, 844, 422]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[74]: text=1, bbox=[860, 413, 869, 423]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[75]: text=其他诊断：特应性神经性皮炎, bbox=[504, 428, 694, 440]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[76]: text=L20.803, bbox=[758, 431, 815, 441]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[77]: text=1, bbox=[863, 432, 872, 442]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[78]: text=入院病情：1.有，2.临床未确定，3.情况不明，4.无, bbox=[14, 601, 405, 614]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[79]: text=损伤、中毒的外部原因：, bbox=[45, 627, 241, 641]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[80]: text=疾病编码：, bbox=[701, 630, 796, 643]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[81]: text=病理诊断：, bbox=[45, 653, 142, 667]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[82]: text=疾病编码：, bbox=[39, 674, 138, 688]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[83]: text=病理号：, bbox=[448, 675, 530, 689]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[84]: text=药物过敏：1 1.无2.有过敏药物：, bbox=[32, 699, 347, 714]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[85]: text=死亡患者尸检：2 1.是2.否, bbox=[710, 703, 938, 719]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[86]: text=血型：1.A 2.B 3.0 4.AB 5.不详 6.未查, bbox=[27, 728, 437, 744]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[87]: text=Rh 4 1.阴2.阳3.不详4.未查, bbox=[555, 727, 828, 746]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[88]: text=科主任：李革, bbox=[22, 756, 122, 773]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[89]: text=主任(副主任)医师：李革, bbox=[240, 756, 432, 773]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[90]: text=主治医师：宋文平, bbox=[553, 756, 688, 773]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[91]: text=住院医师：刘, bbox=[770, 756, 854, 775]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[92]: text=责任护士：唐莹莹, bbox=[18, 781, 150, 798]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[93]: text=进修医师：, bbox=[310, 783, 413, 800]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[94]: text=实习医师：, bbox=[552, 783, 654, 800]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[95]: text=编码员：, bbox=[789, 787, 851, 801]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[96]: text=病案质量 1 1.甲2.乙3.丙质控医师：刘, bbox=[2, 811, 387, 832]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[97]: text=质控护士：杨, bbox=[478, 814, 621, 832]
2026-08-05 05:05:30,938 INFO     29 [qwen-vl-text] coord item[98]: text=质控日期：2024-10-17, bbox=[720, 817, 910, 833]
2026-08-05 05:05:30,939 INFO     29 [qwen-vl-text] page=0 — 99/99 coords, api_time=42.9s
2026-08-05 05:05:30,940 INFO     29 [qwen-vl-text] new_positions (99):
[[0, 59.52756347656249, 122.62678076171873, 28.720397094726565, 58.31110925292969], [0, 164.89135083007812, 277.39844580078125, 54.82984899902344, 64.40331469726563], [0, 367.2850666503906, 504.79373828124994, 50.47827368164062, 60.92205444335938], [0, 69.05197363281249, 160.72442138671875, 73.97678039550782, 85.29087622070313], [0, 224.4189143066406, 373.23782299804685, 71.36583520507813, 84.42056115722656], [0, 429.1937326660156, 513.7228728027343, 65.27362976074218, 80.93930090332032], [0, 67.26614672851562, 103.57796044921874, 87.03150634765625, 95.73465698242188], [0, 271.445689453125, 317.8771889648437, 91.38308166503906, 100.08623229980469], [0, 410.7401879882812, 467.88664892578123, 90.5127666015625, 98.34560217285157], [0, 64.88504418945313, 85.71969140624999, 101.82686242675781, 110.53001306152343], [0, 174.4157609863281, 334.5449067382812, 103.56749255371093, 113.14095825195312], [0, 376.21420117187495, 413.71656616210936, 104.4378076171875, 113.14095825195312], [0, 438.7181428222656, 478.60161035156244, 104.4378076171875, 113.14095825195312], [0, 88.10079394531249, 190.48820312499998, 115.75190344238281, 125.325369140625], [0, 245.8488371582031, 307.7575031738281, 118.3628486328125, 126.19568420410157], [0, 354.1890026855468, 363.1181372070312, 118.3628486328125, 126.19568420410157], [0, 377.40475244140623, 438.1228671875, 118.3628486328125, 127.06599926757812], [0, 498.8409819335937, 507.7701164550781, 116.62221850585938, 125.325369140625], [0, 63.09921728515624, 155.96221630859372, 127.93631433105469, 137.50978002929688], [0, 316.68663769531247, 363.1181372070312, 131.41757458496093, 140.12072521972655], [0, 427.4079057617187, 470.8630270996093, 132.2878896484375, 140.12072521972655], [0, 62.50394165039062, 99.41103100585937, 140.12072521972655, 148.8238758544922], [0, 234.53860009765623, 297.6378173828125, 142.73167041015626, 151.43482104492188], [0, 316.0913620605468, 500.62680883789056, 143.60198547363282, 153.175451171875], [0, 60.12283911132812, 189.29765185546873, 153.175451171875, 163.61923193359374], [0, 428.59845703124995, 476.22050781249993, 157.52702648925782, 165.35986206054687], [0, 58.33701220703124, 197.03623510742185, 165.35986206054687, 174.93332775878906], [0, 428.59845703124995, 478.60161035156244, 170.58175244140625, 178.4145880126953], [0, 57.74173657226562, 126.19843457031249, 177.54427294921877, 186.24742358398439], [0, 429.1937326660156, 478.60161035156244, 182.76616333007811, 190.5989989013672], [0, 55.36063403320312, 132.74646655273438, 190.5989989013672, 200.17246459960938], [0, 201.20316455078122, 260.1354523925781, 192.3396290283203, 201.9130947265625], [0, 279.7795483398437, 401.81105346679686, 194.08025915527344, 203.65372485351563], [0, 492.2929499511718, 500.62680883789056, 194.95057421875, 202.78340979003906], [0, 53.574807128906244, 283.9464777832031, 203.65372485351563, 214.96782067871095], [0, 300.6141955566406, 525.0331098632812, 206.2646700439453, 216.70845080566406], [0, 51.78898022460937, 139.88977416992185, 216.70845080566406, 226.28191650390625], [0, 197.6315107421875, 282.1606508789062, 219.31939599609376, 228.89286169433595], [0, 329.1874260253906, 359.5464833984375, 220.18971105957033, 228.89286169433595], [0, 429.1937326660156, 482.17326416015624, 221.93034118652344, 230.63349182128906], [0, 50.59842895507812, 139.88977416992185, 228.89286169433595, 238.46632739257814], [0, 196.44095947265623, 281.5653752441406, 231.50380688476562, 241.0772725830078], [0, 329.1874260253906, 359.5464833984375, 231.50380688476562, 241.0772725830078], [0, 429.78900830078123, 522.6520073242187, 232.3741219482422, 241.94758764648438], [0, 49.40787768554687, 329.1874260253906, 240.20695751953124, 251.52105334472657], [0, 347.04569506835935, 497.0551550292968, 244.55853283691405, 254.13199853515624], [0, 48.217326416015624, 191.67875439453124, 253.2616834716797, 263.70546423339846], [0, 347.04569506835935, 417.88349560546874, 256.7429437255859, 266.31640942382813], [0, 67.26614672851562, 250.0157666015625, 268.9273546142578, 280.2414504394531], [0, 295.25671484375, 452.40948242187494, 271.5382998046875, 282.85239562988284], [0, 47.622050781249996, 190.48820312499998, 283.7227106933594, 295.03680651855467], [0, 221.44253613281248, 359.5464833984375, 285.4633408203125, 296.7774366455078], [0, 425.62207885742185, 528.6047636718749, 286.33365588378905, 298.51806677246094], [0, 96.43465283203125, 151.20001123046873, 301.9993270263672, 311.57279272460937], [0, 222.63308740234373, 260.1354523925781, 303.7399571533203, 312.44310778808597], [0, 274.4220676269531, 293.4708879394531, 299.3883818359375, 308.9618475341797], [0, 274.4220676269531, 293.4708879394531, 308.9618475341797, 318.53531323242186], [0, 344.66459252929684, 397.6441240234375, 304.6102722167969, 313.3134228515625], [0, 457.17168749999996, 493.4835012207031, 305.4805872802734, 314.18373791503905], [0, 508.9606677246093, 528.0094880371093, 301.9993270263672, 311.57279272460937], [0, 508.9606677246093, 528.0094880371093, 311.57279272460937, 321.1462584228516], [0, 36.90708935546875, 148.2236330566406, 320.275943359375, 330.71972412109375], [0, 213.10867724609372, 270.2551381835937, 322.88688854980467, 331.59003918457034], [0, 272.6362407226562, 277.99372143554683, 322.88688854980467, 331.59003918457034], [0, 300.6141955566406, 383.9527844238281, 322.88688854980467, 332.4603542480469], [0, 448.8378286132812, 499.43625756835934, 324.6275186767578, 333.3306693115234], [0, 510.1512189941406, 515.5086997070312, 325.4978337402344, 334.200984375], [0, 35.7165380859375, 104.76851171874999, 336.8119295654297, 347.25571032714845], [0, 272.6362407226562, 277.99372143554683, 340.29318981933596, 348.126025390625], [0, 300.01891992187495, 438.7181428222656, 339.42287475585937, 349.8666555175781], [0, 449.43310424804685, 482.17326416015624, 341.1635048828125, 349.8666555175781], [0, 510.7464946289062, 516.1039753417969, 342.03381994628904, 350.7369705810547], [0, 300.01891992187495, 429.1937326660156, 356.8291760253906, 367.27295678710936], [0, 450.6236555175781, 502.41263574218743, 358.56980615234374, 367.27295678710936], [0, 511.9370458984375, 517.2945266113281, 359.44012121582034, 368.14327185058596], [0, 300.01891992187495, 413.1212905273437, 372.49484716796877, 382.9386279296875], [0, 451.2189311523437, 485.14964233398433, 375.10579235839845, 383.80894299316407], [0, 513.7228728027343, 519.080353515625, 375.976107421875, 384.6792580566406], [0, 8.33385888671875, 241.08663208007812, 523.059353149414, 534.3734489746093], [0, 26.787403564453122, 143.46142797851562, 545.6875447998046, 557.8719556884765], [0, 417.2882199707031, 473.8394052734375, 548.2984899902344, 559.6125858154297], [0, 26.787403564453122, 84.52914013671874, 568.3157364501953, 580.5001473388672], [0, 23.215749755859374, 82.14803759765624, 586.5923527832032, 598.776763671875], [0, 266.683484375, 315.49608642578124, 587.4626678466797, 599.6470787353516], [0, 19.0488203125, 206.56064526367186, 608.3502293701172, 621.4049553222657], [0, 422.6457006835937, 558.3685454101562, 611.8314896240234, 625.7565306396484], [0, 16.072442138671875, 260.1354523925781, 633.5893662109376, 647.5144072265625], [0, 330.37797729492183, 492.88822558593745, 632.719051147461, 649.2550373535156], [0, 13.096063964843749, 72.62362744140624, 657.9581879882812, 672.7535440673828], [0, 142.86615234375, 257.15907421875, 657.9581879882812, 672.7535440673828], [0, 329.1874260253906, 409.54963671875, 657.9581879882812, 672.7535440673828], [0, 458.3622387695312, 508.3653920898437, 657.9581879882812, 674.494174194336], [0, 10.714961425781249, 89.29134521484374, 679.7160645751953, 694.5114206542969], [0, 184.53544677734374, 245.8488371582031, 681.4566947021484, 696.25205078125], [0, 328.59215039062497, 389.3102651367187, 681.4566947021484, 696.25205078125], [0, 469.6724758300781, 506.5795651855468, 684.9379549560547, 697.1223658447266], [0, 1.19055126953125, 230.37167065429685, 705.8255164794922, 724.1021328125], [0, 284.5417534179687, 369.6661691894531, 708.4364616699219, 724.1021328125], [0, 428.59845703124995, 541.7008276367187, 711.0474068603515, 724.9724478759766]]
2026-08-05 05:05:30,940 INFO     29 [qwen-vl-text] ═══ DONE ═══ 99 positions, pages=1, time=48.6s
2026-08-05 05:05:30,954 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 05:05:30,955 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:05:30,955 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 05:05:30,955 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:05:30.955+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 14, "failed": 0, "current": {"e1e244a2908a11f1a3da71efcdd7cc1f": {"id": "e1e244a2908a11f1a3da71efcdd7cc1f", "doc_id": "e1b14d16908a11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 6041420, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785906159481, "task_type": "dataflow", "root_trace_id": "ee648f5612474f2494cdafbea4ad365d", "root_traceparent": "00-ee648f5612474f2494cdafbea4ad365d-00889eb88a3b4664-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:05:30,961 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:05:30,962 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 05:05:31,913 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:05:31,922 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 05:05:31,923 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:05:31,923 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 05:05:31,928 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:05:31,928 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:05:31 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:05:31,929 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:05:33,529 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:05:33,539 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 05:05:33,539 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "249 items", "markdown": "", "text": "", "name": "lzga-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Clinical\": 2, \"chunks_Medication\": 3}"}
2026-08-05 05:05:33,540 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 05:05:33,540 INFO     29 [ChunkMerger] Merged 6 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 5 noise chunks)
2026-08-05 05:05:33,549 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 05:05:33,549 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 3, 'DischargeRecord': 1}", "name": "lzga-哮喘-沈阳(1).pdf"}
2026-08-05 05:05:33,549 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 05:05:33,633 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785906162618, 'update_date': datetime.datetime(2026, 8, 5, 5, 2, 42), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 178697, 'status': '1'}
2026-08-05 05:05:33,870 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=凤城诚岳中医院
门诊 病 历
诊断专用章
编号：54474
姓名：
性别：男
年龄：67.0岁
地址：然机厂
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
诊断专用笺 病 历
编号：104474
姓名：
性别： 男
年龄： 67.0岁
地址：
职业： 退休
联系电话
身份证号
就诊时间：2026年02月8日
主 诉：反复发作喘息、气促50余年，加重伴呼吸困难1天。
现 病 史：患者50余年前无明显诱因反复出现喘息、胸闷、气促，偶伴咳嗽，无咳痰/少量白痰，多于夜间、凌晨、受凉、接触过敏原、运动后诱发，3年前曾于凤城市人民医院诊断为支气管哮喘，经住院治疗后好转，2025年9月起规律使用沙美特罗替卡松（50/250ug）吸入治疗，控制情况一般。1天前因受凉出现症状加重，出现明显喘息、胸闷、呼吸困难，夜间不能平卧，伴咳嗽、咳痰，自行使用舒利迭50/250ug后无效，为求进一步诊治来我院门诊。饮食、睡眠、二便可，近期体重无明显变化。
既 往 史：否认有肝炎及结核病史，否认有高血压及糖尿病史，否认手术、外伤及输血史，否认药物及食物过敏史、中毒史。
体温(℃)： 36.8 脉搏(次/分)： 86 呼吸(次/分) 26 血压(mmHg) 140/80
查 体：双肺散在哮鸣音，未闻及湿啰音。舌胖大，苔白腻，脉滑。
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
满49返15,满99返30
此票据为购货凭证,请妥善保管
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
血型：1.A 2.B 3.0 4.AB 5.不详 6.未查
Rh 4 1.阴2.阳3.不详4.未查
科主任：李革
主任(副主任)医师：李革
主治医师：宋文平
住院医师：刘
责任护士：唐莹莹
进修医师：
实习医师：
编码员：
病案质量 1 1.甲2.乙3.丙质控医师：刘
质控护士：杨
质控日期：2024-10-17
2026-08-05 05:05:34,247 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 05:05:34,247 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 3, 'DischargeRecord': 1}", "name": "lzga-哮喘-沈阳(1).pdf", "embedding_token_consumption": 2699}
2026-08-05 05:05:34,247 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 05:05:35,423 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 05:05:35,424 INFO     29 [Trace] task=e1e244a2 | doc=lzga-哮喘-沈阳(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 05:05:35,427 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:05:35,427 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:05:35,427 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:05:35,427 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:05:35,427 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:05:35,427 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:05:35,431 INFO     29 set_progress(e1e244a2908a11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 05:05:35 [DOC Engine]:
Start to index...
2026-08-05 05:05:35,453 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.017s]
2026-08-05 05:05:35,458 INFO     29 set_progress(e1e244a2908a11f1a3da71efcdd7cc1f), progress: 0.8166666666666668, progress_msg: 
2026-08-05 05:05:35,479 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-05 05:05:35,494 INFO     29 set_progress(e1e244a2908a11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 05:05:35 Indexing done (0.06s). Task done (159.63s)
2026-08-05 05:05:35,502 INFO     29 [Done], chunks(6), token(2699), elapsed:159.63
2026-08-05 05:05:35,591 INFO     29 handle_task done for task {"id": "e1e244a2908a11f1a3da71efcdd7cc1f", "doc_id": "e1b14d16908a11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lzga-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 6041420, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785906159481, "task_type": "dataflow", "root_trace_id": "ee648f5612474f2494cdafbea4ad365d", "root_traceparent": "00-ee648f5612474f2494cdafbea4ad365d-00889eb88a3b4664-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
