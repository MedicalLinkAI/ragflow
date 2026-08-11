# 基准结果：ZHFE 女(1).pdf

## 基本信息

- 文件：`ZHFE 女(1).pdf`
- 大小：2307.1 KB
- PDF 总页数：9
- doc_id：`5739903094cc11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T23:01:17  完成时间：2026-08-10T23:08:25  耗时：428.3s
- progress_msg：`15:08:21 Indexing done (0.06s). Task done (399.68s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 9fda1e48 | 3 | 1-3 | 姓名： 性别：女 年龄：41岁 婚 姻：已婚 联系电话： 出生 民族：汉族 职业 |
| 2 | 7de3a457 | 2 | 4-5 | 入院时间:2026年03月04日09时20分 出院时间:2026年03月07日1 |
| 3 | 632817dc | 1 | 5-5 | 5G 85 < 详情 JIX日时间· 2020 00 04 10.00.07 检 |
| 4 | 62bfa54f | 2 | 5-6 | 3亿人都在用的扫描App 患者处 性 别: 女 年 龄: 41 岁 登记时间:  |
| 5 | 0c7b07fe | 3 | 7-9 | <table><tr><td>谷丙转氨酶</td><td>ALT</td><td |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：11
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：9 / 9；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "DischargeRecord": 1, "ExaminationReport": 2, "LabReport": 1}`
- ChunkMerger：`{"found": true, "merged": 5, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：2 条
  - `[no_items_extracted] 2026-08-10 15:05:20,882 WARNING  29 [qwen-vl-table] page=7 no items extracted`
  - `[no_text_noise] 2026-08-10 15:08:20,190 INFO     29 [ChunkMerger] Merged 5 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 15:01:18,940 INFO     29 handle_task begin for task {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 15:01:19,149 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 15:01:19,279 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 15:01:19,290 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:01:19,290 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 15:01:19,291 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 15:01:19,297 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 15:01:19,297 INFO     29 ============================================================
2026-08-10 15:01:19,297 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 15:01:19,297 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 15:01:19,297 INFO     29 ============================================================
2026-08-10 15:01:19,297 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 15:01:19,297 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 15:01:19,299 INFO     29 No torch found.
2026-08-10 15:01:20,174 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=9
2026-08-10 15:01:20,493 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1689316, prompt_len=764
2026-08-10 15:01:21,998 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:01:21,999 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 15:01:22,011 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1689316, prompt_len=401
2026-08-10 15:01:31,347 INFO     29 [qwen-vl-parser] text API response (len=1623):
["姓名：", "性别：女", "年龄：41岁", "婚 姻：已婚", "联系电话：", "出生", "民族：汉族", "职业：职工", "住址", "电子邮件(E_mail)：无", "入院时间：2026年03月04日 09时20分", "记录时间：2026年03月04日 10时56分", "病史陈述者：患者本人", "入院方式：步行", "主诉：确诊肺腺癌8个月余。", "现病史：患者自诉2025年6月开始无明显诱因出现活动后气促，为求治疗在", "就诊，完善检查：（左侧颈部淋巴结）HE结合免疫组化符合转移性腺癌，倾向肺来源可能性大，", "请完善相关检查后综合考虑。IHC：GATA-3(-)，P16(-)，CK7(+)，ER(-).PR(-)，CK20(-)，Pax-", "8(-)，TTF-1(+)，NapsinA(+)，CerbB-2(1+)，Villin(+)，Ki-67(热点区约50%+)。PETCT：1.双肺", "散在斑片影及磨玻璃影，糖代谢增高，双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹", "主动脉旁多发肿大淋巴结，糖代谢增高，脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增", "高，上述考虑恶性肿瘤（肺CA？）并淋巴结、骨转移可能，建议结合病理。2.双侧胸腔积液，双下", "肺膨胀不全。3.心包积液，盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶，糖代谢增高，考虑生", "理性改变。诊断考虑为“左上肺腺癌广泛转移”，行化疗前准备（叶酸+维生素B12），于6月13日", "出院。", "2025年6月14日为求治疗入我科，于6月16日完善基因检测，于6月18日予以PCb+贝伐珠单抗", "联合治疗第1周期（培美曲塞785mg+卡铂600mg+贝伐珠单抗800mg），同时予以护胃、止呕等对症", "治疗，患者治疗完成予以办理出院。", "出院后患者诉气促好转，基因检测报告：BRAF（p.K601E），MET扩增，PDL1 TPS表达55%。", "2025年7月9日再入院，予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂", "650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，于7月12日予以地", "舒单抗120mg护骨治疗，复查血常规正常于7月12日出院。", "出院后患者气促明显缓解，2025年7月30日为求治疗再入院，完善检查：肝肾功能、电解质、", "心肌酶、血常规正常。纵隔及心脏平扫及增强|肺部平扫及增强|上腹部平扫及增强|下腹部平扫", "及增强|盆腔平扫及增强CT：肺部炎症，合并多发占位可能；心包积液；双侧部分肋骨、腰椎多发骨", "质病变，腹膜后多发小淋巴结，结合病史考虑转移。疗效评估为PR，于7月31日、8月23日、9月9日、", "10月02日予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单", "抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，期间规律予以地舒单抗护骨治疗，", "患者治疗完成10月05日出院。", "2025年10月23日为求治疗再入院，完善相关检查：胸部平扫及增强|上腹部平扫及增强|下", "腹部平扫及增强|盆腔平扫及增强：与07-30老片相比：肺部炎症较前吸收，考虑肺内转移病灶，", "较前大致相仿；心包积液，较前稍吸收；双肾结石。双侧部分肋骨、腰椎多发骨质病变，似较前稍微", "增多；腹膜后多发小淋巴结，较前相仿；结合病史考虑转移。评估为SD，继续予以贝伐珠单抗", "800mg+替雷利珠单抗200mg维持治疗，同时予以降血脂治疗，2025年10月25日予以办理出院。", "2025年11月14日、12月4日返院继续治疗，因患者偶有痰中带血，停贝伐珠单抗，予以替雷禾", "第 1 页"]
2026-08-10 15:01:31,348 INFO     29 [qwen-vl-parser] page=1 text: 46 lines (bbox 0-45)
2026-08-10 15:01:31,348 INFO     29 [qwen-vl-parser] page=1 text: 46 sections
2026-08-10 15:01:31,649 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1800149, prompt_len=764
2026-08-10 15:01:32,960 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:01:32,961 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 15:01:32,970 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1800149, prompt_len=401
2026-08-10 15:01:38,520 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:01:38.518+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:01:42,710 INFO     29 [qwen-vl-parser] text API response (len=1704):
["珠单抗200mg维持治疗。", "2025年12月25日为求治疗再入院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部", "平扫及增强|盆腔平扫及增强：与10-23老片相比：肺部炎症较前稍进展，考虑肺内转移病灶，较", "前大致相仿；心包积液，较前稍增多；双肾结石。双侧部分肋骨、腰椎多发骨质病变，较前相仿；腹", "膜后多发小淋巴结，较前稍微增大；左侧腋窝稍大淋巴结；结合病史考虑转移。评估为SD，免疫性", "肺炎不排除，参考中科院专家会诊意见，于2025年12月27日予以贝伐珠单抗联合PCb化疗联合治", "疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成12月", "30日办理出院。", "2026年1月17日为求治疗再入院，完善检查，于2026年1月19日予以贝伐珠单抗联合PCb化疗", "联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完", "成1月20日办理出院。", "2026年2月8日再次返院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增", "强|盆腔平扫及增强CT：与2025-10-23日老片相比：肺部炎症较前增多；肺内多发结节（右下肺", "后基底段新增10mm小结节，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可", "能。心包积液，大致同前；双肾结石。双侧部分肋骨、腰椎、骨盆多发骨质病变，大致同前。本次复查", "增强CT，对比2025-12片，疗效评价SD，建议继续贝伐珠单抗+培美曲塞+卡铂联合治疗，患者因过", "年要求暂缓化疗，于2026-02-12予以贝伐珠单抗800mg靶向治疗。治疗上予以抗感染、清热解毒、", "化痰止咳等对症治疗后于2月14日出院。", "今患者为求继续治疗在我院门诊就诊，门诊以“肺恶性肿瘤”收住我科，此次发病期间，患", "者精神食欲睡眠可，大小便正常，体重无明显变化。", "既往史：个人史、月经及婚育史、家族史见第一次入院记录。", "体格检查", "T：36.5℃ P：85次/分 R：19次/分 BP：100/78mmHg", "发育正常，营养中等，自主体位，神志清楚，查体合作。粘膜无发绀、黄染、苍白，无皮疹。未见", "皮下出血。皮肤湿度正常，弹性正常，无肝掌，未见蜘蛛痣。左侧腋下可触及大小约1*1cm的肿大淋", "巴结，活动度差，质地韧，无明显压痛，边界不清晰。头颅外形正常。眼：眼睑正常，眼球无凸出及", "凹陷，结膜正常。巩膜无黄染，双侧瞳孔等大等圆，瞳孔直径3.0mm，对光反射及调节均灵敏。耳：", "双耳耳廓外形正常，无畸形，双侧无乳突压痛，外耳道通畅，无分泌物。鼻外形正常，鼻中隔无偏", "曲，上颌窦与额窦无压痛，无鼻塞，无分泌物。口腔：口唇红润，伸舌居中，双侧扁桃体无肿大，表", "面未见脓点，咽无充血，声音嘶哑。颈软，无抵抗感，气管居中，颈静脉充盈正常，肝颈静脉回流征", "阴性，颈动脉搏动正常，甲状腺未触及肿大。胸廓正常，肋间隙正常，胸壁无压痛，无胸骨叩痛。呼", "吸节律正常，语颤正常，双肺未触及胸膜摩擦感，未触及皮下捻发感。胸廓对称，双肺语颤正常，叩", "诊双肺呈清音，听诊双肺呼吸音低，未闻及明显罗音。心前区无隆起，可见心尖搏动，心尖搏动位", "于第5肋间左锁骨中线内0.5cm，心前区无异常搏动。心尖搏动触不清，未触及震颤，无心包摩擦", "感。心界不大。心率：85次/分，律齐，心音清。各瓣膜听诊区未闻及病理性杂音，不可闻及额外心", "音，未闻及心包摩擦音。周围血管征阴性。腹部平坦，未见胃肠型及蠕动波。未见静脉曲张，脐部正", "常。腹部柔软，无液波震颤，未触及腹部肿块。全腹无压痛、无反跳痛，无肌紧张。肝、脾脏未触及", "肾未触及。肝浊音界存在，肝上界位于右锁骨中线第5肋间，移动性浊音阴性，双肾区无叩痛。肠", "音正常，无气过水声，无震水音，未闻及腹部血管杂音。肛门、直肠及外生殖器：正常。脊柱正常", "第 2 页"]
2026-08-10 15:01:42,711 INFO     29 [qwen-vl-parser] page=2 text: 40 lines (bbox 46-85)
2026-08-10 15:01:42,711 INFO     29 [qwen-vl-parser] page=2 text: 40 sections
2026-08-10 15:01:42,994 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1335517, prompt_len=764
2026-08-10 15:01:44,257 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:01:44,257 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 15:01:44,274 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1335517, prompt_len=401
2026-08-10 15:01:49,901 INFO     29 [qwen-vl-parser] text API response (len=706):
["号 A1687966", "理弯曲,活动自如,无压痛及叩击痛。四肢活动自如,关节无红肿,活动自如,皮温正常。无杵状指、", "趾,双下肢无水肿。腹壁反射存在,双侧跟腱反射正常,四肢肌力及肌张力正常,双侧巴彬斯征、", "布鲁金斯基征、克匿格征阴性。", "辅助检查结果:2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增", "高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢", "增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并", "淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积", "液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。", "2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾", "向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-).", "PR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约", "50%+)。", "心肌酶正常,CA125 372U/ml。", "2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。", "入院诊断:1.肺腺癌 cTxNxM1 IVb期 骨转移、双", "肺、心包转移2.胸腔积液3.心包积液4.肺部感染?", "医生签名"]
2026-08-10 15:01:49,902 INFO     29 [qwen-vl-parser] page=3 text: 18 lines (bbox 86-103)
2026-08-10 15:01:49,902 INFO     29 [qwen-vl-parser] page=3 text: 18 sections
2026-08-10 15:01:50,197 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1463112, prompt_len=764
2026-08-10 15:01:51,805 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:01:51,806 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 15:01:51,821 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1463112, prompt_len=401
2026-08-10 15:01:57,914 INFO     29 [qwen-vl-parser] text API response (len=1036):
["入院时间:2026年03月04日09时20分 出院时间:2026年03月07日10时00分 住院天数:3天", "X线号:-", "CT号:-", "MRI号:-", "入院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸", "腔积液 4.肺部感染?", "入院情况:确诊肺腺癌8个月余。体格检查:四测正常,神志清楚,自动体位,慢性病容。皮肤", "巩膜无黄染,全身未扪及明显肿大淋巴结,气管居中。颈软,胸廓对称,双肺语颤正常,叩诊双肺呈", "清音,听诊双肺呼吸音低,未闻及明显罗音。心音清晰,心律齐无杂音。腹平软,全腹无压痛反跳", "痛,肝脾肋下未扪及,肝肾区无叩痛,移动性浊音阴性,肠鸣音正常。双下肢无浮肿。四肢肌力、肌", "张力正常。生理反射正常,病理征阴性。", "诊治经过:完善相关检查:CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器)", "23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇", "7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。胸部平扫:与2026.02.08日老片", "相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,", "余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧", "胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。评估为PD,部分进展,与家属商榷后于3月6", "日继续予以贝伐珠单抗联合PCb化疗联合治疗(贝伐珠单抗800mg+培美曲塞860mg+卡铂", "600mg),现治疗完成予以办理出院。", "出院情况:患者偶有干咳。", "出院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸", "腔积液", "出院医嘱:1、注意休息,加强营养,多饮白开水。", "2、定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复", "查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射", "200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,", "遵医嘱用药;", "3、院外巩固治疗,不适随诊。"]
2026-08-10 15:01:57,914 INFO     29 [qwen-vl-parser] page=4 text: 28 lines (bbox 104-131)
2026-08-10 15:01:57,915 INFO     29 [qwen-vl-parser] page=4 text: 28 sections
2026-08-10 15:01:58,051 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935582, prompt_len=764
2026-08-10 15:01:59,461 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:01:59,461 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 15:01:59,475 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935582, prompt_len=401
2026-08-10 15:02:02,346 INFO     29 [qwen-vl-parser] text API response (len=471):
["11:25", "5G 85", "< 详情", "JIX日时间· 2020 00 04 10.00.07", "检查医院:", "影像所见", "审核医生", "肺Ca患者复查：双肺支气管-血管束增", "多，双肺散在多发斑片状、小结节状磨玻璃密度影，气管及叶段支气管通畅。纵隔", "未见明显肿大淋巴结，双侧胸腔少许积液。心包见环形积液征象。左侧腋窝见肿", "大淋巴结，大者短径约17mm。双侧部分", "肋骨、胸椎见斑片状、结节状骨质密度增", "高影。", "影像诊断", "与2026.02.08日老片相比：肺部炎症较", "前稍增多；肺内多发结节（右下肺后基底", "段结节较前稍增大，现直径约13mm，余", "同前相仿），不排除转移瘤；左侧腋窝淋", "巴结较前增大，转移瘤可能。心包积液，", "大致同前；双侧胸腔新见少许积液。双侧", "部分肋骨、胸椎多发骨质病变，大致同", "前。", "相关检查(6)", "查看全部>", "图文报告", "影像浏览", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 15:02:02,346 INFO     29 [qwen-vl-parser] page=5 text: 28 lines (bbox 132-159)
2026-08-10 15:02:02,346 INFO     29 [qwen-vl-parser] page=5 text: 28 sections
2026-08-10 15:02:02,574 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1601505, prompt_len=764
2026-08-10 15:02:04,002 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-08"
}
```
2026-08-10 15:02:04,003 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2026-02-08
2026-08-10 15:02:04,024 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1601505, prompt_len=401
2026-08-10 15:02:10,159 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:02:10.158+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:02:10,209 INFO     29 [qwen-vl-parser] text API response (len=1001):
["患者处", "性 别: 女 年 龄: 41 岁 登记时间: 2026-02-08 10:17:51", "患者编", "检查号: ZX-1401650 科 别: 肿瘤血液科一病区 床 号: 12034", "检查部位: 胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强", "影像表现:", "肺Ca患者复查: 经肘静脉注入造影剂行增强扫描(造影剂: 碘海醇; 浓度:", "35g/100ml; 速率: 3.0-4.0ml/s; 用量: 1-1.2ml/kg):", "双肺支气管-血管束增多, 双肺散在多发斑片状、小结节状磨玻璃密度影,", "增强扫描强化不明显, 气管及叶段支气管通畅。", "纵隔未见明显肿大淋巴结, 双侧胸腔未见明显积液征象。心包见环形积液征", "象。增强后未见异常强化。左侧腋窝见肿大淋巴结, 大者短径约12mm。", "肝脏形态大小未见异常, 表面光滑, 肝叶比例协调, 肝裂不宽, 肝实质内未", "见异常密度灶, 增强后未见异常强化, 肝内血管走形自然。肝内外胆管无扩张。", "胆囊不大, 壁不厚, 内未见高密度灶, 胰腺大小形态未见异常, 均匀强化。脾不", "大, 质均匀, 增强后均匀强化。双肾形态大小未见异常, 实质密度均匀, 双肾内", "可见结节状高密度影, 肾盂肾盏无扩张, 肾周脂肪间隙清晰, 增强后未见异常强", "化。腹膜后见多发小淋巴结, 增强扫描强化较明显。", "膀胱充盈良好, 壁光整, 未见结节或肿块, 其内未见异常密度影及异常强化", "灶。盆腔未见积液征象, 未见明确肿大淋巴结。", "双侧部分肋骨、腰椎、骨盆见斑片状、结节状骨质密度增高影。", "意见:", "与2025-10-23日老片相比:", "肺部炎症较前增多; 肺内多发结节(右下肺后基底段新增10mm小结节, 余同前相", "仿), 不排除转移瘤; 左侧腋窝淋巴结较前增大, 转移瘤可能。", "心包积液, 大致同前;", "双肾结石。", "双侧部分肋骨、腰椎、骨盆多发骨质病变, 大致同前; 腹膜后多发小淋巴结, 较前相", "报告医师: 常利霞", "审核医师:", "报告时间: 2026-02-08 16:26:10", ") . 出诊时间: 每周六(8:30-12:0", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 15:02:10,210 INFO     29 [qwen-vl-parser] page=6 text: 34 lines (bbox 160-193)
2026-08-10 15:02:10,210 INFO     29 [qwen-vl-parser] page=6 text: 34 sections
2026-08-10 15:02:10,664 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2658616, prompt_len=764
2026-08-10 15:02:12,279 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-04"
}
```
2026-08-10 15:02:12,281 INFO     29 [qwen-vl-parser] page=7 classify=table report_date=2026-03-04
2026-08-10 15:02:12,310 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2658616, prompt_len=756
2026-08-10 15:02:41,685 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:02:41.684+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:03:13,601 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:03:13.598+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:03:45,383 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:03:45.381+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:04:17,791 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:04:17.790+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:04:22,735 INFO     29 [qwen-vl-parser] table API response (len=34178):
\begin{tabular}{ccccccccc}
\hline
& & & & & & & & \\
\hline
1 & ALT & *谷丙转氨酶 & 26.0 & 0~40.0 & U/L & 24 LDH & *乳酸脱氢酶 & 217 \\
2 & AST & *谷草转氨酶 & 35.0 & 0~40.0 & U/L & 25 MYO & 肌红蛋白 & 45 \\
3 & AST/ALT & 谷草谷丙比 & 1.35 & 0.80~1.68 & & 26 K & *钾 & 4.25 \\
4 & GGT & *谷氨酰氨基转 & 52.0 & ↑0.0~50.0 & U/L & 27 Na & *钠 & 141.0 \\
5 & TP & *总蛋白 & 69.5 & 60~83 & g/L & 28 CL & *氯 & 102.0 \\
6 & ALB & *白蛋白 & 42.4 & 35~55.0 & g/L & 29 Ca & *钙 & 2.51 \\
7 & GLD & 球蛋白 & 27.1 & 20.0~35.0 & g/L & & & \\
8 & A/G & 白/球蛋白 & 1.56 & 1.00~2.50 & & & & \\
9 & TBA & 总胆汁酸 & 2.8 & 0.0~12.0 & umol/L & & & \\
10 & TBIL & *总胆红素 & 7.4 & 3.4~17.1 & umol/L & & & \\
11 & DBIL & *直接胆红素 & 1.9 & 0.0~7.1 & umol/L & & & \\
12 & IBIL & 间接胆红素 & 5.5 & 0.0~16.0 & umol/L & & & \\
13 & *尿素氮 & & 4.04 & 2.90~7.10 & mmol/L & & & \\
14 & *肌酐 & & 66.0 & 40~79.6 & umol/L & & & \\
15 & UA & *尿酸 & 314.7 & 90.0~423.0 & umol/L & & & \\
16 & GLU & *葡萄糖 & 5.60 & 3.90~6.10 & mmol/L & & & \\
17 & TG & *甘油三酯 & 3.18 & ↑0.23~1.69 & mmol/L & & & \\
18 & CHOL & *总胆固醇 & 7.37 & ↑2.8~5.50 & mmol/L & & & \\
19 & *低密度脂蛋白胆固醇 & & 5.30 & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & & & & & \\
& & & & &
2026-08-10 15:04:22,738 INFO     29 [qwen-vl-parser] page=7 table: 1766 LaTeX lines (bbox 194-1959)
2026-08-10 15:04:22,738 INFO     29 [qwen-vl-parser] page=7 table: 1766 sections
2026-08-10 15:04:23,392 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2501825, prompt_len=764
2026-08-10 15:04:24,825 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-04"
}
```
2026-08-10 15:04:24,826 INFO     29 [qwen-vl-parser] page=8 classify=table report_date=2026-03-04
2026-08-10 15:04:24,847 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2501825, prompt_len=756
2026-08-10 15:04:32,162 INFO     29 [qwen-vl-parser] table API response (len=1194):
\begin{tabular}{ccccccccc}
\hline
\multicolumn{2}{c}{检验项目} & 结果 & 参考范围 & 单位 & \multicolumn{2}{c}{检验项目} & 结果 & 参考范围 & 单位 \\
\hline
*超敏C反应蛋白 & & 1.48 & 0.0~10.0 & mg/L & HCT & *红细胞压积 & 37.70 & 35~45 & \% \\
WBC & *白细胞 & 4.7 & 3.5~9.5 & 10^9/L & MCV & *红细胞平均体积 & 101.9 & 82.0~100 & fL \\
RBC & *红细胞 & 3.70 & 3.8~5.1 & 10^12/L & MCH & *平均血红蛋白量 & 32.4 & 27.0~34 & pg \\
HGB & *血红蛋白 & 120.0 & 115~150 & g/L & MCHC & *平均血红蛋白浓度 & 318 & 316~354 & g/L \\
PLT & *血小板 & 207.0 & 125~350 & 10^9/L & PCT & 血小板比积 & 0.210 & 0.108~0.272 & \\
NEU & 中性细胞数 & 2.4 & 1.8~6.3 & 10^9/L & MPV & 平均血小板体积 & 9.90 & 9.00~13.00 & fL \\
EOS & 嗜酸性粒细胞 & 0.070 & 0.02~0.52 & 10^9/L & PDW & 血小板分布宽度 & 10.8 & 15.0~18.0 & \\
BASO & 嗜碱性粒细胞 & 0.010 & 0.000~0.06 & 10^9/L & RDW-SD & RBC分布宽度 & 56.80 & 37.00~50.00 & fL \\
LYM & 淋巴细胞数 & 1.54 & 1.1~3.2 & 10^9/L & P-LCR & 大型PLT比率 & 24.20 & 13.00~43.00 & \% \\
MONO & 单核细胞 & 0.63 & 0.1~0.6 & 10^9/L & 红细胞分布宽度系数 & 15 & & & \% \\
NEU\% & 中性细胞比率 & 51.8 & 40~75 & \% & & & & & \\
LYM\% & 淋巴细胞比率 & 33 & 20~50 & \% & & & & & \\
MONO\% & 单核细胞比率 & 13.5 & 3.0~10 & \% & & & & & \\
BASO\% & 嗜碱细胞比率 & 0.2 & 0.0~1.0 & \% & & & & & \\
EOS\% & 嗜酸细胞比率 & 1.5 & 0.4~8 & \% & & & & & \\
\hline
\end{tabular}
2026-08-10 15:04:32,165 INFO     29 [qwen-vl-parser] page=8 table: 22 LaTeX lines (bbox 1960-1981)
2026-08-10 15:04:32,165 INFO     29 [qwen-vl-parser] page=8 table: 22 sections
2026-08-10 15:04:32,523 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1606322, prompt_len=764
2026-08-10 15:04:33,954 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 15:04:33,955 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=None
2026-08-10 15:04:33,971 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1606322, prompt_len=756
2026-08-10 15:04:35,366 INFO     29 [qwen-vl-parser] table API response (len=217):
\begin{tabular}{llll}
\hline
检验项目 & 结果 & & 提示 \\
\hline
1*癌胚抗原(新仪器) & 23.75 & & $\uparrow$ \\
2*糖类抗原125(新仪器) & 240.15 & & $\uparrow$ \\
3*糖类抗原153(新仪器) & 16.42 & & \\
4 细胞角蛋白19片段(新仪器) & 3.39 & & \\
\hline
\end{tabular}
2026-08-10 15:04:35,368 INFO     29 [qwen-vl-parser] page=9 table: 10 LaTeX lines (bbox 1982-1991)
2026-08-10 15:04:35,368 INFO     29 [qwen-vl-parser] page=9 table: 10 sections
2026-08-10 15:04:35,368 INFO     29 [qwen-vl-parser] parse_pdf done: 1992 sections from 9 pages.
2026-08-10 15:04:35,388 INFO     29 Close text detector.
2026-08-10 15:04:35,817 INFO     29 Close text recognizer.
2026-08-10 15:04:36,188 INFO     29 Close recognizer.
2026-08-10 15:04:36,605 INFO     29 Close recognizer.
2026-08-10 15:04:37,013 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 15:04:37,013 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Parser:MedLink | outputs={"html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "json"}
2026-08-10 15:04:37,013 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 15:04:37,044 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:04:37,044 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 姓名：\n[BBOX-1] 性别：女\n[BBOX-2] 年龄：41岁\n[BBOX-3] 婚 姻：已婚\n[BBOX-4] 联系电话：\n[BBOX-5] 出生\n[BBOX-6] 民族：汉族\n[BBOX-7] 职业：职工\n[BBOX-8] 住址\n[BBOX-9] 电子邮件(E_mail)：无\n[BBOX-10] 入院时间：2026年03月04日 09时20分\n[BBOX-11] 记录时间：2026年03月04日 10时56分\n[BBOX-12] 病史陈述者：患者本人\n[BBOX-13] 入院方式：步行\n[BBOX-14] 主诉：确诊肺腺癌8个月余。\n[BBOX-15] 现病史：患者自诉2025年6月开始无明显诱因出现活动后气促，为求治疗在\n[BBOX-16] 就诊，完善检查：（左侧颈部淋巴结）HE结合免疫组化符合转移性腺癌，倾向肺来源可能性大，\n[BBOX-17] 请完善相关检查后综合考虑。IHC：GATA-3(-)，P16(-)，CK7(+)，ER(-).PR(-)，CK20(-)，Pax-\n[BBOX-18] 8(-)，TTF-1(+)，NapsinA(+)，CerbB-2(1+)，Villin(+)，Ki-67(热点区约50%+)。PETCT：1.双肺\n[BBOX-19] 散在斑片影及磨玻璃影，糖代谢增高，双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹\n[BBOX-20] 主动脉旁多发肿大淋巴结，糖代谢增高，脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增\n[BBOX-21] 高，上述考虑恶性肿瘤（肺CA？）并淋巴结、骨转移可能，建议结合病理。2.双侧胸腔积液，双下\n[BBOX-22] 肺膨胀不全。3.心包积液，盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶，糖代谢增高，考虑生\n[BBOX-23] 理性改变。诊断考虑为“左上肺腺癌广泛转移”，行化疗前准备（叶酸+维生素B12），于6月13日\n[BBOX-24] 出院。\n[BBOX-25] 2025年6月14日为求治疗入我科，于6月16日完善基因检测，于6月18日予以PCb+贝伐珠单抗\n[BBOX-26] 联合治疗第1周期（培美曲塞785mg+卡铂600mg+贝伐珠单抗800mg），同时予以护胃、止呕等对症\n[BBOX-27] 治疗，患者治疗完成予以办理出院。\n[BBOX-28] 出院后患者诉气促好转，基因检测报告：BRAF（p.K601E），MET扩增，PDL1 TPS表达55%。\n[BBOX-29] 2025年7月9日再入院，予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂\n[BBOX-30] 650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，于7月12日予以地\n[BBOX-31] 舒单抗120mg护骨治疗，复查血常规正常于7月12日出院。\n[BBOX-32] 出院后患者气促明显缓解，2025年7月30日为求治疗再入院，完善检查：肝肾功能、电解质、\n[BBOX-33] 心肌酶、血常规正常。纵隔及心脏平扫及增强|肺部平扫及增强|上腹部平扫及增强|下腹部平扫\n[BBOX-34] 及增强|盆腔平扫及增强CT：肺部炎症，合并多发占位可能；心包积液；双侧部分肋骨、腰椎多发骨\n[BBOX-35] 质病变，腹膜后多发小淋巴结，结合病史考虑转移。疗效评估为PR，于7月31日、8月23日、9月9日、\n[BBOX-36] 10月02日予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单\n[BBOX-37] 抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，期间规律予以地舒单抗护骨治疗，\n[BBOX-38] 患者治疗完成10月05日出院。\n[BBOX-39] 2025年10月23日为求治疗再入院，完善相关检查：胸部平扫及增强|上腹部平扫及增强|下\n[BBOX-40] 腹部平扫及增强|盆腔平扫及增强：与07-30老片相比：肺部炎症较前吸收，考虑肺内转移病灶，\n[BBOX-41] 较前大致相仿；心包积液，较前稍吸收；双肾结石。双侧部分肋骨、腰椎多发骨质病变，似较前稍微\n[BBOX-42] 增多；腹膜后多发小淋巴结，较前相仿；结合病史考虑转移。评估为SD，继续予以贝伐珠单抗\n[BBOX-43] 800mg+替雷利珠单抗200mg维持治疗，同时予以降血脂治疗，2025年10月25日予以办理出院。\n[BBOX-44] 2025年11月14日、12月4日返院继续治疗，因患者偶有痰中带血，停贝伐珠单抗，予以替雷禾\n[BBOX-45] 第 1 页\n[BBOX-46] 珠单抗200mg维持治疗。\n[BBOX-47] 2025年12月25日为求治疗再入院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部\n[BBOX-48] 平扫及增强|盆腔平扫及增强：与10-23老片相比：肺部炎症较前稍进展，考虑肺内转移病灶，较\n[BBOX-49] 前大致相仿；心包积液，较前稍增多；双肾结石。双侧部分肋骨、腰椎多发骨质病变，较前相仿；腹\n[BBOX-50] 膜后多发小淋巴结，较前稍微增大；左侧腋窝稍大淋巴结；结合病史考虑转移。评估为SD，免疫性\n[BBOX-51] 肺炎不排除，参考中科院专家会诊意见，于2025年12月27日予以贝伐珠单抗联合PCb化疗联合治\n[BBOX-52] 疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成12月\n[BBOX-53] 30日办理出院。\n[BBOX-54] 2026年1月17日为求治疗再入院，完善检查，于2026年1月19日予以贝伐珠单抗联合PCb化疗\n[BBOX-55] 联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完\n[BBOX-56] 成1月20日办理出院。\n[BBOX-57] 2026年2月8日再次返院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增\n[BBOX-58] 强|盆腔平扫及增强CT：与2025-10-23日老片相比：肺部炎症较前增多；肺内多发结节（右下肺\n[BBOX-59] 后基底段新增10mm小结节，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可\n[BBOX-60] 能。心包积液，大致同前；双肾结石。双侧部分肋骨、腰椎、骨盆多发骨质病变，大致同前。本次复查\n[BBOX-61] 增强CT，对比2025-12片，疗效评价SD，建议继续贝伐珠单抗+培美曲塞+卡铂联合治疗，患者因过\n[BBOX-62] 年要求暂缓化疗，于2026-02-12予以贝伐珠单抗800mg靶向治疗。治疗上予以抗感染、清热解毒、\n[BBOX-63] 化痰止咳等对症治疗后于2月14日出院。\n[BBOX-64] 今患者为求继续治疗在我院门诊就诊，门诊以“肺恶性肿瘤”收住我科，此次发病期间，患\n[BBOX-65] 者精神食欲睡眠可，大小便正常，体重无明显变化。\n[BBOX-66] 既往史：个人史、月经及婚育史、家族史见第一次入院记录。\n[BBOX-67] 体格检查\n[BBOX-68] T：36.5℃ P：85次/分 R：19次/分 BP：100/78mmHg\n[BBOX-69] 发育正常，营养中等，自主体位，神志清楚，查体合作。粘膜无发绀、黄染、苍白，无皮疹。未见\n[BBOX-70] 皮下出血。皮肤湿度正常，弹性正常，无肝掌，未见蜘蛛痣。左侧腋下可触及大小约1*1cm的肿大淋\n[BBOX-71] 巴结，活动度差，质地韧，无明显压痛，边界不清晰。头颅外形正常。眼：眼睑正常，眼球无凸出及\n[BBOX-72] 凹陷，结膜正常。巩膜无黄染，双侧瞳孔等大等圆，瞳孔直径3.0mm，对光反射及调节均灵敏。耳：\n[BBOX-73] 双耳耳廓外形正常，无畸形，双侧无乳突压痛，外耳道通畅，无分泌物。鼻外形正常，鼻中隔无偏\n[BBOX-74] 曲，上颌窦与额窦无压痛，无鼻塞，无分泌物。口腔：口唇红润，伸舌居中，双侧扁桃体无肿大，表\n[BBOX-75] 面未见脓点，咽无充血，声音嘶哑。颈软，无抵抗感，气管居中，颈静脉充盈正常，肝颈静脉回流征\n[BBOX-76] 阴性，颈动脉搏动正常，甲状腺未触及肿大。胸廓正常，肋间隙正常，胸壁无压痛，无胸骨叩痛。呼\n[BBOX-77] 吸节律正常，语颤正常，双肺未触及胸膜摩擦感，未触及皮下捻发感。胸廓对称，双肺语颤正常，叩\n[BBOX-78] 诊双肺呈清音，听诊双肺呼吸音低，未闻及明显罗音。心前区无隆起，可见心尖搏动，心尖搏动位\n[BBOX-79] 于第5肋间左锁骨中线内0.5cm，心前区无异常搏动。心尖搏动触不清，未触及震颤，无心包摩擦\n[BBOX-80] 感。心界不大。心率：85次/分，律齐，心音清。各瓣膜听诊区未闻及病理性杂音，不可闻及额外心\n[BBOX-81] 音，未闻及心包摩擦音。周围血管征阴性。腹部平坦，未见胃肠型及蠕动波。未见静脉曲张，脐部正\n[BBOX-82] 常。腹部柔软，无液波震颤，未触及腹部肿块。全腹无压痛、无反跳痛，无肌紧张。肝、脾脏未触及\n[BBOX-83] 肾未触及。肝浊音界存在，肝上界位于右锁骨中线第5肋间，移动性浊音阴性，双肾区无叩痛。肠\n[BBOX-84] 音正常，无气过水声，无震水音，未闻及腹部血管杂音。肛门、直肠及外生殖器：正常。脊柱正常\n[BBOX-85] 第 2 页\n[BBOX-86] 号 A1687966\n[BBOX-87] 理弯曲,活动自如,无压痛及叩击痛。四肢活动自如,关节无红肿,活动自如,皮温正常。无杵状指、\n[BBOX-88] 趾,双下肢无水肿。腹壁反射存在,双侧跟腱反射正常,四肢肌力及肌张力正常,双侧巴彬斯征、\n[BBOX-89] 布鲁金斯基征、克匿格征阴性。\n[BBOX-90] 辅助检查结果:2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增\n[BBOX-91] 高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢\n[BBOX-92] 增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并\n[BBOX-93] 淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积\n[BBOX-94] 液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。\n[BBOX-95] 2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾\n[BBOX-96] 向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-).\n[BBOX-97] PR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约\n[BBOX-98] 50%+)。\n[BBOX-99] 心肌酶正常,CA125 372U/ml。\n[BBOX-100] 2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。\n[BBOX-101] 入院诊断:1.肺腺癌 cTxNxM1 IVb期 骨转移、双\n[BBOX-102] 肺、心包转移2.胸腔积液3.心包积液4.肺部感染?\n[BBOX-103] 医生签名\n[BBOX-104] 入院时间:2026年03月04日09时20分 出院时间:2026年03月07日10时00分 住院天数:3天\n[BBOX-105] X线号:-\n[BBOX-106] CT号:-\n[BBOX-107] MRI号:-\n[BBOX-108] 入院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸\n[BBOX-109] 腔积液 4.肺部感染?\n[BBOX-110] 入院情况:确诊肺腺癌8个月余。体格检查:四测正常,神志清楚,自动体位,慢性病容。皮肤\n[BBOX-111] 巩膜无黄染,全身未扪及明显肿大淋巴结,气管居中。颈软,胸廓对称,双肺语颤正常,叩诊双肺呈\n[BBOX-112] 清音,听诊双肺呼吸音低,未闻及明显罗音。心音清晰,心律齐无杂音。腹平软,全腹无压痛反跳\n[BBOX-113] 痛,肝脾肋下未扪及,肝肾区无叩痛,移动性浊音阴性,肠鸣音正常。双下肢无浮肿。四肢肌力、肌\n[BBOX-114] 张力正常。生理反射正常,病理征阴性。\n[BBOX-115] 诊治经过:完善相关检查:CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器)\n[BBOX-116] 23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇\n[BBOX-117] 7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。胸部平扫:与2026.02.08日老片\n[BBOX-118] 相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,\n[BBOX-119] 余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧\n[BBOX-120] 胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。评估为PD,部分进展,与家属商榷后于3月6\n[BBOX-121] 日继续予以贝伐珠单抗联合PCb化疗联合治疗(贝伐珠单抗800mg+培美曲塞860mg+卡铂\n[BBOX-122] 600mg),现治疗完成予以办理出院。\n[BBOX-123] 出院情况:患者偶有干咳。\n[BBOX-124] 出院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸\n[BBOX-125] 腔积液\n[BBOX-126] 出院医嘱:1、注意休息,加强营养,多饮白开水。\n[BBOX-127] 2、定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复\n[BBOX-128] 查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射\n[BBOX-129] 200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,\n[BBOX-130] 遵医嘱用药;\n[BBOX-131] 3、院外巩固治疗,不适随诊。\n[BBOX-132] 11:25\n[BBOX-133] 5G 85\n[BBOX-134] < 详情\n[BBOX-135] JIX日时间· 2020 00 04 10.00.07\n[BBOX-136] 检查医院:\n[BBOX-137] 影像所见\n[BBOX-138] 审核医生\n[BBOX-139] 肺Ca患者复查：双肺支气管-血管束增\n[BBOX-140] 多，双肺散在多发斑片状、小结节状磨玻璃密度影，气管及叶段支气管通畅。纵隔\n[BBOX-141] 未见明显肿大淋巴结，双侧胸腔少许积液。心包见环形积液征象。左侧腋窝见肿\n[BBOX-142] 大淋巴结，大者短径约17mm。双侧部分\n[BBOX-143] 肋骨、胸椎见斑片状、结节状骨质密度增\n[BBOX-144] 高影。\n[BBOX-145] 影像诊断\n[BBOX-146] 与2026.02.08日老片相比：肺部炎症较\n[BBOX-147] 前稍增多；肺内多发结节（右下肺后基底\n[BBOX-148] 段结节较前稍增大，现直径约13mm，余\n[BBOX-149] 同前相仿），不排除转移瘤；左侧腋窝淋\n[BBOX-150] 巴结较前增大，转移瘤可能。心包积液，\n[BBOX-151] 大致同前；双侧胸腔新见少许积液。双侧\n[BBOX-152] 部分肋骨、胸椎多发骨质病变，大致同\n[BBOX-153] 前。\n[BBOX-154] 相关检查(6)\n[BBOX-155] 查看全部>\n[BBOX-156] 图文报告\n[BBOX-157] 影像浏览\n[BBOX-158] CS 扫描全能王\n[BBOX-159] 3亿人都在用的扫描App\n[BBOX-160] 患者处\n[BBOX-161] 性 别: 女 年 龄: 41 岁 登记时间: 2026-02-08 10:17:51\n[BBOX-162] 患者编\n[BBOX-163] 检查号: ZX-1401650 科 别: 肿瘤血液科一病区 床 号: 12034\n[BBOX-164] 检查部位: 胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强\n[BBOX-165] 影像表现:\n[BBOX-166] 肺Ca患者复查: 经肘静脉注入造影剂行增强扫描(造影剂: 碘海醇; 浓度:\n[BBOX-167] 35g/100ml; 速率: 3.0-4.0ml/s; 用量: 1-1.2ml/kg):\n[BBOX-168] 双肺支气管-血管束增多, 双肺散在多发斑片状、小结节状磨玻璃密度影,\n[BBOX-169] 增强扫描强化不明显, 气管及叶段支气管通畅。\n[BBOX-170] 纵隔未见明显肿大淋巴结, 双侧胸腔未见明显积液征象。心包见环形积液征\n[BBOX-171] 象。增强后未见异常强化。左侧腋窝见肿大淋巴结, 大者短径约12mm。\n[BBOX-172] 肝脏形态大小未见异常, 表面光滑, 肝叶比例协调, 肝裂不宽, 肝实质内未\n[BBOX-173] 见异常密度灶, 增强后未见异常强化, 肝内血管走形自然。肝内外胆管无扩张。\n[BBOX-174] 胆囊不大, 壁不厚, 内未见高密度灶, 胰腺大小形态未见异常, 均匀强化。脾不\n[BBOX-175] 大, 质均匀, 增强后均匀强化。双肾形态大小未见异常, 实质密度均匀, 双肾内\n[BBOX-176] 可见结节状高密度影, 肾盂肾盏无扩张, 肾周脂肪间隙清晰, 增强后未见异常强\n[BBOX-177] 化。腹膜后见多发小淋巴结, 增强扫描强化较明显。\n[BBOX-178] 膀胱充盈良好, 壁光整, 未见结节或肿块, 其内未见异常密度影及异常强化\n[BBOX-179] 灶。盆腔未见积液征象, 未见明确肿大淋巴结。\n[BBOX-180] 双侧部分肋骨、腰椎、骨盆见斑片状、结节状骨质密度增高影。\n[BBOX-181] 意见:\n[BBOX-182] 与2025-10-23日老片相比:\n[BBOX-183] 肺部炎症较前增多; 肺内多发结节(右下肺后基底段新增10mm小结节, 余同前相\n[BBOX-184] 仿), 不排除转移瘤; 左侧腋窝淋巴结较前增大, 转���瘤可能。\n[BBOX-185] 心包积液, 大致同前;\n[BBOX-186] 双肾结石。\n[BBOX-187] 双侧部分肋骨、腰椎、骨盆多发骨质病变, 大致同前; 腹膜后多发小淋巴结, 较前相\n[BBOX-188] 报告医师: 常利霞\n[BBOX-189] 审核医师:\n[BBOX-190] 报告时间: 2026-02-08 16:26:10\n[BBOX-191] ) . 出诊时间: 每周六(8:30-12:0\n[BBOX-192] CS 扫描全能王\n[BBOX-193] 3亿人都在用的扫描App\n[BBOX-194] \\begin{tabular}{ccccccccc}\n[BBOX-195] 报告时间: 2026-03-04\n[BBOX-196] \\hline\n[BBOX-197] & & & & & & & & \\\\\n[BBOX-198] \\hline\n[BBOX-199] 1 & ALT & *谷丙转氨酶 & 26.0 & 0~40.0 & U/L & 24 LDH & *乳酸脱氢酶 & 217 \\\\\n[BBOX-200] 2 & AST & *谷草转氨酶 & 35.0 & 0~40.0 & U/L & 25 MYO & 肌红蛋白 & 45 \\\\\n[BBOX-201] 3 & AST/ALT & 谷草谷丙比 & 1.35 & 0.80~1.68 & & 26 K & *钾 & 4.25 \\\\\n[BBOX-202] 4 & GGT & *谷氨酰氨基转 & 52.0 & ↑0.0~50.0 & U/L & 27 Na & *钠 & 141.0 \\\\\n[BBOX-203] 5 & TP & *总蛋白 & 69.5 & 60~83 & g/L & 28 CL & *氯 & 102.0 \\\\\n[BBOX-204] 6 & ALB & *白蛋白 & 42.4 & 35~55.0 & g/L & 29 Ca & *钙 & 2.51 \\\\\n[BBOX-205] 7 & GLD & 球蛋白 & 27.1 & 20.0~35.0 & g/L & & & \\\\\n[BBOX-206] 8 & A/G & 白/球蛋白 & 1.56 & 1.00~2.50 & & & & \\\\\n[BBOX-207] 9 & TBA & 总胆汁酸 & 2.8 & 0.0~12.0 & umol/L & & & \\\\\n[BBOX-208] 10 & TBIL & *总胆红素 & 7.4 & 3.4~17.1 & umol/L & & & \\\\\n[BBOX-209] 11 & DBIL & *直接胆红素 & 1.9 & 0.0~7.1 & umol/L & & & \\\\\n[BBOX-210] 12 & IBIL & 间接胆红素 & 5.5 & 0.0~16.0 & umol/L & & & \\\\\n[BBOX-211] 13 & *尿素氮 & & 4.04 & 2.90~7.10 & mmol/L & & & \\\\\n[BBOX-212] 14 & *肌酐 & & 66.0 & 40~79.6 & umol/L & & & \\\\\n[BBOX-213] 15 & UA & *尿酸 & 314.7 & 90.0~423.0 & umol/L & & & \\\\\n[BBOX-214] 16 & GLU & *葡萄糖 & 5.60 & 3.90~6.10 & mmol/L & & & \\\\\n[BBOX-215] 17 & TG & *甘油三酯 & 3.18 & ↑0.23~1.69 & mmol/L & & & \\\\\n[BBOX-216] 18 & CHOL & *总胆固醇 & 7.37 & ↑2.8~5.50 & mmol/L & & & \\\\\n[BBOX-217] 19 & *低密度脂蛋白胆固醇 & & 5.30 & & & & & \\\\\n[BBOX-218] & & & & & & & & \\\\\n[BBOX-219] & & & & & & & & \\\\\n[BBOX-220] & & & & & & & & \\\\\n[BBOX-221] & & & & & & & & \\\\\n[BBOX-222] & & & & & & & & \\\\\n[BBOX-223] & & & & & & & & \\\\\n[BBOX-224] & & & & & & & & \\\\\n[BBOX-225] & & & & & & & & \\\\\n[BBOX-226] & & & & & & & & \\\\\n[BBOX-227] & & & & & & & & \\\\\n[BBOX-228] & & & & & & & & \\\\\n[BBOX-229] & & & & & & & & \\\\\n[BBOX-230] & & & & & & & & \\\\\n[BBOX-231] & & & & & & & & \\\\\n[BBOX-232] & & & & & & & & \\\\\n[BBOX-233] & & & & & & & & \\\\\n[BBOX-234] & & & & & & & & \\\\\n[BBOX-235] & & & & & & & & \\\\\n[BBOX-236] & & & & & & & & \\\\\n[BBOX-237] & & & & & & & & \\\\\n[BBOX-238] & & & & & & & & \\\\\n[BBOX-239] & & & & & & & & \\\\\n[BBOX-240] & & & & & & & & \\\\\n[BBOX-241] & & & & & & & & \\\\\n[BBOX-242] & & & & & & & & \\\\\n[BBOX-243] & & & & & & & & \\\\\n[BBOX-244] & & & & & & & & \\\\\n[BBOX-245] & & & & & & & & \\\\\n[BBOX-246] & & & & & & & & \\\\\n[BBOX-247] & & & & & & & & \\\\\n[BBOX-248] & & & & & & & & \\\\\n[BBOX-249] & & & & & & & & \\\\\n[BBOX-250] & & & & & & & & \\\\\n[BBOX-251] & & & & & & & & \\\\\n[BBOX-252] & & & & & & & & \\\\\n[BBOX-253] & & & & & & & & \\\\\n[BBOX-254] & & & & & & & & \\\\\n[BBOX-255] & & & & & & & & \\\\\n[BBOX-256] & & & & & & & & \\\\\n[BBOX-257] & & & & & & & & \\\\\n[BBOX-258] & & & & & & & & \\\\\n[BBOX-259] & & & & & & & & \\\\\n[BBOX-260] & & & & & & & & \\\\\n[BBOX-261] & & & & & & & & \\\\\n[BBOX-262] & & & & & & & & \\\\\n[BBOX-263] & & & & & & & & \\\\\n[BBOX-264] & & & & & & & & \\\\\n[BBOX-265] & & & & & & & & \\\\\n[BBOX-266] & & & & & & & & \\\\\n[BBOX-267] & & & & & & & & \\\\\n[BBOX-268] & & & & & & & & \\\\\n[BBOX-269] & & & & & & & & \\\\\n[BBOX-270] & & & & & & & & \\\\\n[BBOX-271] & & & & & & & & \\\\\n[BBOX-272] & & & & & & & & \\\\\n[BBOX-273] & & & & & & & & \\\\\n[BBOX-274] & & & & & & & & \\\\\n[BBOX-275] & & & & & & & & \\\\\n[BBOX-276] & & & & & & & & \\\\\n[BBOX-277] & & & & & & & & \\\\\n[BBOX-278] & & & & & & & & \\\\\n[BBOX-279] & & & & & & & & \\\\\n[BBOX-280] & & & & & & & & \\\\\n[BBOX-281] & & & & & & & & \\\\\n[BBOX-282] & & & & & & & & \\\\\n[BBOX-283] & & & & & & & & \\\\\n[BBOX-284] & & & & & & & & \\\\\n[BBOX-285] & & & & & & & & \\\\\n[BBOX-286] & & & & & & & & \\\\\n[BBOX-287] & & & & & & & & \\\\\n[BBOX-288] & & & & & & & & \\\\\n[BBOX-289] & & & & & & & & \\\\\n[BBOX-290] & & & & & & & & \\\\\n[BBOX-291] & & & & & & & & \\\\\n[BBOX-292] & & & & & & & & \\\\\n[BBOX-293] & & & & & & & & \\\\\n[BBOX-294] & & & & & & & & \\\\\n[BBOX-295] & & & & & & & & \\\\\n[BBOX-296] & & & & & & & & \\\\\n[BBOX-297] & & & & & & & & \\\\\n[BBOX-298] & & & & & & & & \\\\\n[BBOX-299] & & & & & & & & \\\\\n[BBOX-300] & & & & & & & & \\\\\n[BBOX-301] & & & & & & & & \\\\\n[BBOX-302] & & & & & & & & \\\\\n[BBOX-303] & & & & & & & & \\\\\n[BBOX-304] & & & & & & & & \\\\\n[BBOX-305] & & & & & & & & \\\\\n[BBOX-306] & & & & & & & & \\\\\n[BBOX-307] & & & & & & & & \\\\\n[BBOX-308] & & & & & & & & \\\\\n[BBOX-309] & & & & & & & & \\\\\n[BBOX-310] & & & & & & & & \\\\\n[BBOX-311] & & & & & & & & \\\\\n[BBOX-312] & & & & & & & & \\\\\n[BBOX-313] & & & & & & & & \\\\\n[BBOX-314] & & & & & & & & \\\\\n[BBOX-315] & & & & & & & & \\\\\n[BBOX-316] & & & & & & & & \\\\\n[BBOX-317] & & & & & & & & \\\\\n[BBOX-318] & & & & & & & & \\\\\n[BBOX-319] & & & & & & & & \\\\\n[BBOX-320] & & & & & & & & \\\\\n[BBOX-321] & & & & & & & & \\\\\n[BBOX-322] & & & & & & & & \\\\\n[BBOX-323] & & & & & & & & \\\\\n[BBOX-324] & & & & & & & & \\\\\n[BBOX-325] & & & & & & & & \\\\\n[BBOX-326] & & & & & & & & \\\\\n[BBOX-327] & & & & & & & & \\\\\n[BBOX-328] & & & & & & & & \\\\\n[BBOX-329] & & & & & & & & \\\\\n[BBOX-330] & & & & & & & & \\\\\n[BBOX-331] & & & & & & & & \\\\\n[BBOX-332] & & & & & & & & \\\\\n[BBOX-333] & & & & & & & & \\\\\n[BBOX-334] & & & & & & & & \\\\\n[BBOX-335] & & & & & & & & \\\\\n[BBOX-336] & & & & & & & & \\\\\n[BBOX-337] & & & & & & & & \\\\\n[BBOX-338] & & & & & & & & \\\\\n[BBOX-339] & & & & & & & & \\\\\n[BBOX-340] & & & & & & & & \\\\\n[BBOX-341] & & & & & & & & \\\\\n[BBOX-342] & & & & & & & & \\\\\n[BBOX-343] & & & & & & & & \\\\\n[BBOX-344] & & & & & & & & \\\\\n[BBOX-345] & & & & & & & & \\\\\n[BBOX-346] & & & & & & & & \\\\\n[BBOX-347] & & & & & & & & \\\\\n[BBOX-348] & & & & & & & & \\\\\n[BBOX-349] & & & & & & & & \\\\\n[BBOX-350] & & & & & & & & \\\\\n[BBOX-351] & & & & & & & & \\\\\n[BBOX-352] & & & & & & & & \\\\\n[BBOX-353] & & & & & & & & \\\\\n[BBOX-354] & & & & & & & & \\\\\n[BBOX-355] & & & & & & & & \\\\\n[BBOX-356] & & & & & & & & \\\\\n[BBOX-357] & & & & & & & & \\\\\n[BBOX-358] & & & & & & & & \\\\\n[BBOX-359] & & & & & & & & \\\\\n[BBOX-360] & & & & & & & & \\\\\n[BBOX-361] & & & & & & & & \\\\\n[BBOX-362] & & & & & & & & \\\\\n[BBOX-363] & & & & & & & & \\\\\n[BBOX-364] & & & & & & & & \\\\\n[BBOX-365] & & & & & & & & \\\\\n[BBOX-366] & & & & & & & & \\\\\n[BBOX-367] & & & & & & & & \\\\\n[BBOX-368] & & & & & & & & \\\\\n[BBOX-369] & & & & & & & & \\\\\n[BBOX-370] & & & & & & & & \\\\\n[BBOX-371] & & & & & & & & \\\\\n[BBOX-372] & & & & & & & & \\\\\n[BBOX-373] & & & & & & & & \\\\\n[BBOX-374] & & & & & & & & \\\\\n[BBOX-375] & & & & & & & & \\\\\n[BBOX-376] & & & & & & & & \\\\\n[BBOX-377] & & & & & & & & \\\\\n[BBOX-378] & & & & & & & & \\\\\n[BBOX-379] & & & & & & & & \\\\\n[BBOX-380] & & & & & & & & \\\\\n[BBOX-381] & & & & & & & & \\\\\n[BBOX-382] & & & & & & & & \\\\\n[BBOX-383] & & & & & & & & \\\\\n[BBOX-384] & & & & & & & & \\\\\n[BBOX-385] & & & & & & & & \\\\\n[BBOX-386] & & & & & & & & \\\\\n[BBOX-387] & & & & & & & & \\\\\n[BBOX-388] & & & & & & & & \\\\\n[BBOX-389] & & & & & & & & \\\\\n[BBOX-390] & & & & & & & & \\\\\n[BBOX-391] & & & & & & & & \\\\\n[BBOX-392] & & & & & & & & \\\\\n[BBOX-393] & & & & & & & & \\\\\n[BBOX-394] & & & & & & & & \\\\\n[BBOX-395] & & & & & & & & \\\\\n[BBOX-396] & & & & & & & & \\\\\n[BBOX-397] & & & & & & & & \\\\\n[BBOX-398] & & & & & & & & \\\\\n[BBOX-399] & & & & & & & & \\\\\n[BBOX-400] & & & & & & & & \\\\\n[BBOX-401] & & & & & & & & \\\\\n[BBOX-402] & & & & & & & & \\\\\n[BBOX-403] & & & & & & & & \\\\\n[BBOX-404] & & & & & & & & \\\\\n[BBOX-405] & & & & & & & & \\\\\n[BBOX-406] & & & & & & & & \\\\\n[BBOX-407] & & & & & & & & \\\\\n[BBOX-408] & & & & & & & & \\\\\n[BBOX-409] & & & & & & & & \\\\\n[BBOX-410] & & & & & & & & \\\\\n[BBOX-411] & & & & & & & & \\\\\n[BBOX-412] & & & & & & & & \\\\\n[BBOX-413] & & & & & & & & \\\\\n[BBOX-414] & & & & & & & & \\\\\n[BBOX-415] & & & & & & & & \\\\\n[BBOX-416] & & & & & & & & \\\\\n[BBOX-417] & & & & & & & & \\\\\n[BBOX-418] & & & & & & & & \\\\\n[BBOX-419] & & & & & & & & \\\\\n[BBOX-420] & & & & & & & & \\\\\n[BBOX-421] & & & & & & & & \\\\\n[BBOX-422] & & & & & & & & \\\\\n[BBOX-423] & & & & & & & & \\\\\n[BBOX-424] & & & & & & & & \\\\\n[BBOX-425] & & & & & & & & \\\\\n[BBOX-426] & & & & & & & & \\\\\n[BBOX-427] & & & & & & & & \\\\\n[BBOX-428] & & & & & & & & \\\\\n[BBOX-429] & & & & & & & & \\\\\n[BBOX-430] & & & & & & & & \\\\\n[BBOX-431] & & & & & & & & \\\\\n[BBOX-432] & & & & & & & & \\\\\n[BBOX-433] & & & & & & & & \\\\\n[BBOX-434] & & & & & & & & \\\\\n[BBOX-435] & & & & & & & & \\\\\n[BBOX-436] & & & & & & & & \\\\\n[BBOX-437] & & & & & & & & \\\\\n[BBOX-438] & & & & & & & & \\\\\n[BBOX-439] & & & & & & & & \\\\\n[BBOX-440] & & & & & & & & \\\\\n[BBOX-441] & & & & & & & & \\\\\n[BBOX-442] & & & & & & & & \\\\\n[BBOX-443] & & & & & & & & \\\\\n[BBOX-444] & & & & & & & & \\\\\n[BBOX-445] & & & & & & & & \\\\\n[BBOX-446] & & & & & & & & \\\\\n[BBOX-447] & & & & & & & & \\\\\n[BBOX-448] & & & & & & & & \\\\\n[BBOX-449] & & & & & & & & \\\\\n[BBOX-450] & & & & & & & & \\\\\n[BBOX-451] & & & & & & & & \\\\\n[BBOX-452] & & & & & & & & \\\\\n[BBOX-453] & & & & & & & & \\\\\n[BBOX-454] & & & & & & & & \\\\\n[BBOX-455] & & & & & & & & \\\\\n[BBOX-456] & & & & & & & & \\\\\n[BBOX-457] & & & & & & & & \\\\\n[BBOX-458] & & & & & & & & \\\\\n[BBOX-459] & & & & & & & & \\\\\n[BBOX-460] & & & & & & & & \\\\\n[BBOX-461] & & & & & & & & \\\\\n[BBOX-462] & & & & & & & & \\\\\n[BBOX-463] & & & & & & & & \\\\\n[BBOX-464] & & & & & & & & \\\\\n[BBOX-465] & & & & & & & & \\\\\n[BBOX-466] & & & & & & & & \\\\\n[BBOX-467] & & & & & & & & \\\\\n[BBOX-468] & & & & & & & & \\\\\n[BBOX-469] & & & & & & & & \\\\\n[BBOX-470] & & & & & & & & \\\\\n[BBOX-471] & & & & & & & & \\\\\n[BBOX-472] & & & & & & & & \\\\\n[BBOX-473] & & & & & & & & \\\\\n[BBOX-474] & & & & & & & & \\\\\n[BBOX-475] & & & & & & & & \\\\\n[BBOX-476] & & & & & & & & \\\\\n[BBOX-477] & & & & & & & & \\\\\n[BBOX-478] & & & & & & & & \\\\\n[BBOX-479] & & & & & & & & \\\\\n[BBOX-480] & & & & & & & & \\\\\n[BBOX-481] & & & & & & & & \\\\\n[BBOX-482] & & & & & & & & \\\\\n[BBOX-483] & & & & & & & & \\\\\n[BBOX-484] & & & & & & & & \\\\\n[BBOX-485] & & & & & & & & \\\\\n[BBOX-486] & & & & & & & & \\\\\n[BBOX-487] & & & & & & & & \\\\\n[BBOX-488] & & & & & & & & \\\\\n[BBOX-489] & & & & & & & & \\\\\n[BBOX-490] & & & & & & & & \\\\\n[BBOX-491] & & & & & & & & \\\\\n[BBOX-492] & & & & & & & & \\\\\n[BBOX-493] & & & & & & & & \\\\\n[BBOX-494] & & & & & & & & \\\\\n[BBOX-495] & & & & & & & & \\\\\n[BBOX-496] & & & & & & & & \\\\\n[BBOX-497] & & & & & & & & \\\\\n[BBOX-498] & & & & & & & & \\\\\n[BBOX-499] & & & & & & & & \\\\\n[BBOX-500] & & & & & & & & \\\\\n[BBOX-501] & & & & & & & & \\\\\n[BBOX-502] & & & & & & & & \\\\\n[BBOX-503] & & & & & & & & \\\\\n[BBOX-504] & & & & & & & & \\\\\n[BBOX-505] & & & & & & & & \\\\\n[BBOX-506] & & & & & & & & \\\\\n[BBOX-507] & & & & & & & & \\\\\n[BBOX-508] & & & & & & & & \\\\\n[BBOX-509] & & & & & & & & \\\\\n[BBOX-510] & & & & & & & & \\\\\n[BBOX-511] & & & & & & & & \\\\\n[BBOX-512] & & & & & & & & \\\\\n[BBOX-513] & & & & & & & & \\\\\n[BBOX-514] & & & & & & & & \\\\\n[BBOX-515] & & & & & & & & \\\\\n[BBOX-516] & & & & & & & & \\\\\n[BBOX-517] & & & & & & & & \\\\\n[BBOX-518] & & & & & & & & \\\\\n[BBOX-519] & & & & & & & & \\\\\n[BBOX-520] & & & & & & & & \\\\\n[BBOX-521] & & & & & & & & \\\\\n[BBOX-522] & & & & & & & & \\\\\n[BBOX-523] & & & & & & & & \\\\\n[BBOX-524] & & & & & & & & \\\\\n[BBOX-525] & & & & & & & & \\\\\n[BBOX-526] & & & & & & & & \\\\\n[BBOX-527] & & & & & & & & \\\\\n[BBOX-528] & & & & & & & & \\\\\n[BBOX-529] & & & & & & & & \\\\\n[BBOX-530] & & & & & & & & \\\\\n[BBOX-531] & & & & & & & & \\\\\n[BBOX-532] & & & & & & & & \\\\\n[BBOX-533] & & & & & & & & \\\\\n[BBOX-534] & & & & & & & & \\\\\n[BBOX-535] & & & & & & & & \\\\\n[BBOX-536] & & & & & & & & \\\\\n[BBOX-537] & & & & & & & & \\\\\n[BBOX-538] & & & & & & & & \\\\\n[BBOX-539] & & & & & & & & \\\\\n[BBOX-540] & & & & & & & & \\\\\n[BBOX-541] & & & & & & & & \\\\\n[BBOX-542] & & & & & & & & \\\\\n[BBOX-543] & & & & & & & & \\\\\n[BBOX-544] & & & & & & & & \\\\\n[BBOX-545] & & & & & & & & \\\\\n[BBOX-546] & & & & & & & & \\\\\n[BBOX-547] & & & & & & & & \\\\\n[BBOX-548] & & & & & & & & \\\\\n[BBOX-549] & & & & & & & & \\\\\n[BBOX-550] & & & & & & & & \\\\\n[BBOX-551] & & & & & & & & \\\\\n[BBOX-552] & & & & & & & & \\\\\n[BBOX-553] & & & & & & & & \\\\\n[BBOX-554] & & & & & & & & \\\\\n[BBOX-555] & & & & & & & & \\\\\n[BBOX-556] & & & & & & & & \\\\\n[BBOX-557] & & & & & & & & \\\\\n[BBOX-558] & & & & & & & & \\\\\n[BBOX-559] & & & & & & & & \\\\\n[BBOX-560] & & & & & & & & \\\\\n[BBOX-561] & & & & & & & & \\\\\n[BBOX-562] & & & & & & & & \\\\\n[BBOX-563] & & & & & & & & \\\\\n[BBOX-564] & & & & & & & & \\\\\n[BBOX-565] & & & & & & & & \\\\\n[BBOX-566] & & & & & & & & \\\\\n[BBOX-567] & & & & & & & & \\\\\n[BBOX-568] & & & & & & & & \\\\\n[BBOX-569] & & & & & & & & \\\\\n[BBOX-570] & & & & & & & & \\\\\n[BBOX-571] & & & & & & & & \\\\\n[BBOX-572] & & & & & & & & \\\\\n[BBOX-573] & & & & & & & & \\\\\n[BBOX-574] & & & & & & & & \\\\\n[BBOX-575] & & & & & & & & \\\\\n[BBOX-576] & & & & & & & & \\\\\n[BBOX-577] & & & & & & & & \\\\\n[BBOX-578] & & & & & & & & \\\\\n[BBOX-579] & & & & & & & & \\\\\n[BBOX-580] & & & & & & & & \\\\\n[BBOX-581] & & & & & & & & \\\\\n[BBOX-582] & & & & & & & & \\\\\n[BBOX-583] & & & & & & & & \\\\\n[BBOX-584] & & & & & & & & \\\\\n[BBOX-585] & & & & & & & & \\\\\n[BBOX-586] & & & & & & & & \\\\\n[BBOX-587] & & & & & & & & \\\\\n[BBOX-588] & & & & & & & & \\\\\n[BBOX-589] & & & & & & & & \\\\\n[BBOX-590] & & & & & & & & \\\\\n[BBOX-591] & & & & & & & & \\\\\n[BBOX-592] & & & & & & & & \\\\\n[BBOX-593] & & & & & & & & \\\\\n[BBOX-594] & & & & & & & & \\\\\n[BBOX-595] & & & & & & & & \\\\\n[BBOX-596] & & & & & & & & \\\\\n[BBOX-597] & & & & & & & & \\\\\n[BBOX-598] & & & & & & & & \\\\\n[BBOX-599] & & & & & & & & \\\\\n[BBOX-600] & & & & & & & & \\\\\n[BBOX-601] & & & & & & & & \\\\\n[BBOX-602] & & & & & & & & \\\\\n[BBOX-603] & & & & & & & & \\\\\n[BBOX-604] & & & & & & & & \\\\\n[BBOX-605] & & & & & & & & \\\\\n[BBOX-606] & & & & & & & & \\\\\n[BBOX-607] & & & & & & & & \\\\\n[BBOX-608] & & & & & & & & \\\\\n[BBOX-609] & & & & & & & & \\\\\n[BBOX-610] & & & & & & & & \\\\\n[BBOX-611] & & & & & & & & \\\\\n[BBOX-612] & & & & & & & & \\\\\n[BBOX-613] & & & & & & & & \\\\\n[BBOX-614] & & & & & & & & \\\\\n[BBOX-615] & & & & & & & & \\\\\n[BBOX-616] & & & & & & & & \\\\\n[BBOX-617] & & & & & & & & \\\\\n[BBOX-618] & & & & & & & & \\\\\n[BBOX-619] & & & & & & & & \\\\\n[BBOX-620] & & & & & & & & \\\\\n[BBOX-621] & & & & & & & & \\\\\n[BBOX-622] & & & & & & & & \\\\\n[BBOX-623] & & & & & & & & \\\\\n[BBOX-624] & & & & & & & & \\\\\n[BBOX-625] & & & & & & & & \\\\\n[BBOX-626] & & & & & & & & \\\\\n[BBOX-627] & & & & & & & & \\\\\n[BBOX-628] & & & & & & & & \\\\\n[BBOX-629] & & & & & & & & \\\\\n[BBOX-630] & & & & & & & & \\\\\n[BBOX-631] & & & & & & & & \\\\\n[BBOX-632] & & & & & & & & \\\\\n[BBOX-633] & & & & & & & & \\\\\n[BBOX-634] & & & & & & & & \\\\\n[BBOX-635] & & & & & & & & \\\\\n[BBOX-636] & & & & & & & & \\\\\n[BBOX-637] & & & & & & & & \\\\\n[BBOX-638] & & & & & & & & \\\\\n[BBOX-639] & & & & & & & & \\\\\n[BBOX-640] & & & & & & & & \\\\\n[BBOX-641] & & & & & & & & \\\\\n[BBOX-642] & & & & & & & & \\\\\n[BBOX-643] & & & & & & & & \\\\\n[BBOX-644] & & & & & & & & \\\\\n[BBOX-645] & & & & & & & & \\\\\n[BBOX-646] & & & & & & & & \\\\\n[BBOX-647] & & & & & & & & \\\\\n[BBOX-648] & & & & & & & & \\\\\n[BBOX-649] & & & & & & & & \\\\\n[BBOX-650] & & & & & & & & \\\\\n[BBOX-651] & & & & & & & & \\\\\n[BBOX-652] & & & & & & & & \\\\\n[BBOX-653] & & & & & & & & \\\\\n[BBOX-654] & & & & & & & & \\\\\n[BBOX-655] & & & & & & & & \\\\\n[BBOX-656] & & & & & & & & \\\\\n[BBOX-657] & & & & & & & & \\\\\n[BBOX-658] & & & & & & & & \\\\\n[BBOX-659] & & & & & & & & \\\\\n[BBOX-660] & & & & & & & & \\\\\n[BBOX-661] & & & & & & & & \\\\\n[BBOX-662] & & & & & & & & \\\\\n[BBOX-663] & & & & & & & & \\\\\n[BBOX-664] & & & & & & & & \\\\\n[BBOX-665] & & & & & & & & \\\\\n[BBOX-666] & & & & & & & & \\\\\n[BBOX-667] & & & & & & & & \\\\\n[BBOX-668] & & & & & & & & \\\\\n[BBOX-669] & & & & & & & & \\\\\n[BBOX-670] & & & & & & & & \\\\\n[BBOX-671] & & & & & & & & \\\\\n[BBOX-672] & & & & & & & & \\\\\n[BBOX-673] & & & & & & & & \\\\\n[BBOX-674] & & & & & & & & \\\\\n[BBOX-675] & & & & & & & & \\\\\n[BBOX-676] & & & & & & & & \\\\\n[BBOX-677] & & & & & & & & \\\\\n[BBOX-678] & & & & & & & & \\\\\n[BBOX-679] & & & & & & & & \\\\\n[BBOX-680] & & & & & & & & \\\\\n[BBOX-681] & & & & & & & & \\\\\n[BBOX-682] & & & & & & & & \\\\\n[BBOX-683] & & & & & & & & \\\\\n[BBOX-684] & & & & & & & & \\\\\n[BBOX-685] & & & & & & & & \\\\\n[BBOX-686] & & & & & & & & \\\\\n[BBOX-687] & & & & & & & & \\\\\n[BBOX-688] & & & & & & & & \\\\\n[BBOX-689] & & & & & & & & \\\\\n[BBOX-690] & & & & & & & & \\\\\n[BBOX-691] & & & & & & & & \\\\\n[BBOX-692] & & & & & & & & \\\\\n[BBOX-693] & & & & & & & & \\\\\n[BBOX-694] & & & & & & & & \\\\\n[BBOX-695] & & & & & & & & \\\\\n[BBOX-696] & & & & & & & & \\\\\n[BBOX-697] & & & & & & & & \\\\\n[BBOX-698] & & & & & & & & \\\\\n[BBOX-699] & & & & & & & & \\\\\n[BBOX-700] & & & & & & & & \\\\\n[BBOX-701] & & & & & & & & \\\\\n[BBOX-702] & & & & & & & & \\\\\n[BBOX-703] & & & & & & & & \\\\\n[BBOX-704] & & & & & & & & \\\\\n[BBOX-705] & & & & & & & & \\\\\n[BBOX-706] & & & & & & & & \\\\\n[BBOX-707] & & & & & & & & \\\\\n[BBOX-708] & & & & & & & & \\\\\n[BBOX-709] & & & & & & & & \\\\\n[BBOX-710] & & & & & & & & \\\\\n[BBOX-711] & & & & & & & & \\\\\n[BBOX-712] & & & & & & & & \\\\\n[BBOX-713] & & & & & & & & \\\\\n[BBOX-714] & & & & & & & & \\\\\n[BBOX-715] & & & & & & & & \\\\\n[BBOX-716] & & & & & & & & \\\\\n[BBOX-717] & & & & & & & & \\\\\n[BBOX-718] & & & & & & & & \\\\\n[BBOX-719] & & & & & & & & \\\\\n[BBOX-720] & & & & & & & & \\\\\n[BBOX-721] & & & & & & & & \\\\\n[BBOX-722] & & & & & & & & \\\\\n[BBOX-723] & & & & & & & & \\\\\n[BBOX-724] & & & & & & & & \\\\\n[BBOX-725] & & & & & & & & \\\\\n[BBOX-726] & & & & & & & & \\\\\n[BBOX-727] & & & & & & & & \\\\\n[BBOX-728] & & & & & & & & \\\\\n[BBOX-729] & & & & & & & & \\\\\n[BBOX-730] & & & & & & & & \\\\\n[BBOX-731] & & & & & & & & \\\\\n[BBOX-732] & & & & & & & & \\\\\n[BBOX-733] & & & & & & & & \\\\\n[BBOX-734] & & & & & & & & \\\\\n[BBOX-735] & & & & & & & & \\\\\n[BBOX-736] & & & & & & & & \\\\\n[BBOX-737] & & & & & & & & \\\\\n[BBOX-738] & & & & & & & & \\\\\n[BBOX-739] & & & & & & & & \\\\\n[BBOX-740] & & & & & & & & \\\\\n[BBOX-741] & & & & & & & & \\\\\n[BBOX-742] & & & & & & & & \\\\\n[BBOX-743] & & & & & & & & \\\\\n[BBOX-744] & & & & & & & & \\\\\n[BBOX-745] & & & & & & & & \\\\\n[BBOX-746] & & & & & & & & \\\\\n[BBOX-747] & & & & & & & & \\\\\n[BBOX-748] & & & & & & & & \\\\\n[BBOX-749] & & & & & & & & \\\\\n[BBOX-750] & & & & & & & & \\\\\n[BBOX-751] & & & & & & & & \\\\\n[BBOX-752] & & & & & & & & \\\\\n[BBOX-753] & & & & & & & & \\\\\n[BBOX-754] & & & & & & & & \\\\\n[BBOX-755] & & & & & & & & \\\\\n[BBOX-756] & & & & & & & & \\\\\n[BBOX-757] & & & & & & & & \\\\\n[BBOX-758] & & & & & & & & \\\\\n[BBOX-759] & & & & & & & & \\\\\n[BBOX-760] & & & & & & & & \\\\\n[BBOX-761] & & & & & & & & \\\\\n[BBOX-762] & & & & & & & & \\\\\n[BBOX-763] & & & & & & & & \\\\\n[BBOX-764] & & & & & & & & \\\\\n[BBOX-765] & & & & & & & & \\\\\n[BBOX-766] & & & & & & & & \\\\\n[BBOX-767] & & & & & & & & \\\\\n[BBOX-768] & & & & & & & & \\\\\n[BBOX-769] & & & & & & & & \\\\\n[BBOX-770] & & & & & & & & \\\\\n[BBOX-771] & & & & & & & & \\\\\n[BBOX-772] & & & & & & & & \\\\\n[BBOX-773] & & & & & & & & \\\\\n[BBOX-774] & & & & & & & & \\\\\n[BBOX-775] & & & & & & & & \\\\\n[BBOX-776] & & & & & & & & \\\\\n[BBOX-777] & & & & & & & & \\\\\n[BBOX-778] & & & & & & & & \\\\\n[BBOX-779] & & & & & & & & \\\\\n[BBOX-780] & & & & & & & & \\\\\n[BBOX-781] & & & & & & & & \\\\\n[BBOX-782] & & & & & & & & \\\\\n[BBOX-783] & & & & & & & & \\\\\n[BBOX-784] & & & & & & & & \\\\\n[BBOX-785] & & & & & & & & \\\\\n[BBOX-786] & & & & & & & & \\\\\n[BBOX-787] & & & & & & & & \\\\\n[BBOX-788] & & & & & & & & \\\\\n[BBOX-789] & & & & & & & & \\\\\n[BBOX-790] & & & & & & & & \\\\\n[BBOX-791] & & & & & & & & \\\\\n[BBOX-792] & & & & & & & & \\\\\n[BBOX-793] & & & & & & & & \\\\\n[BBOX-794] & & & & & & & & \\\\\n[BBOX-795] & & & & & & & & \\\\\n[BBOX-796] & & & & & & & & \\\\\n[BBOX-797] & & & & & & & & \\\\\n[BBOX-798] & & & & & & & & \\\\\n[BBOX-799] & & & & & & & & \\\\\n[BBOX-800] & & & & & & & & \\\\\n[BBOX-801] & & & & & & & & \\\\\n[BBOX-802] & & & & & & & & \\\\\n[BBOX-803] & & & & & & & & \\\\\n[BBOX-804] & & & & & & & & \\\\\n[BBOX-805] & & & & & & & & \\\\\n[BBOX-806] & & & & & & & & \\\\\n[BBOX-807] & & & & & & & & \\\\\n[BBOX-808] & & & & & & & & \\\\\n[BBOX-809] & & & & & & & & \\\\\n[BBOX-810] & & & & & & & & \\\\\n[BBOX-811] & & & & & & & & \\\\\n[BBOX-812] & & & & & & & & \\\\\n[BBOX-813] & & & & & & & & \\\\\n[BBOX-814] & & & & & & & & \\\\\n[BBOX-815] & & & & & & & & \\\\\n[BBOX-816] & & & & & & & & \\\\\n[BBOX-817] & & & & & & & & \\\\\n[BBOX-818] & & & & & & & & \\\\\n[BBOX-819] & & & & & & & & \\\\\n[BBOX-820] & & & & & & & & \\\\\n[BBOX-821] & & & & & & & & \\\\\n[BBOX-822] & & & & & & & & \\\\\n[BBOX-823] & & & & & & & & \\\\\n[BBOX-824] & & & & & & & & \\\\\n[BBOX-825] & & & & & & & & \\\\\n[BBOX-826] & & & & & & & & \\\\\n[BBOX-827] & & & & & & & & \\\\\n[BBOX-828] & & & & & & & & \\\\\n[BBOX-829] & & & & & & & & \\\\\n[BBOX-830] & & & & & & & & \\\\\n[BBOX-831] & & & & & & & & \\\\\n[BBOX-832] & & & & & & & & \\\\\n[BBOX-833] & & & & & & & & \\\\\n[BBOX-834] & & & & & & & & \\\\\n[BBOX-835] & & & & & & & & \\\\\n[BBOX-836] & & & & & & & & \\\\\n[BBOX-837] & & & & & & & & \\\\\n[BBOX-838] & & & & & & & & \\\\\n[BBOX-839] & & & & & & & & \\\\\n[BBOX-840] & & & & & & & & \\\\\n[BBOX-841] & & & & & & & & \\\\\n[BBOX-842] & & & & & & & & \\\\\n[BBOX-843] & & & & & & & & \\\\\n[BBOX-844] & & & & & & & & \\\\\n[BBOX-845] & & & & & & & & \\\\\n[BBOX-846] & & & & & & & & \\\\\n[BBOX-847] & & & & & & & & \\\\\n[BBOX-848] & & & & & & & & \\\\\n[BBOX-849] & & & & & & & & \\\\\n[BBOX-850] & & & & & & & & \\\\\n[BBOX-851] & & & & & & & & \\\\\n[BBOX-852] & & & & & & & & \\\\\n[BBOX-853] & & & & & & & & \\\\\n[BBOX-854] & & & & & & & & \\\\\n[BBOX-855] & & & & & & & & \\\\\n[BBOX-856] & & & & & & & & \\\\\n[BBOX-857] & & & & & & & & \\\\\n[BBOX-858] & & & & & & & & \\\\\n[BBOX-859] & & & & & & & & \\\\\n[BBOX-860] & & & & & & & & \\\\\n[BBOX-861] & & & & & & & & \\\\\n[BBOX-862] & & & & & & & & \\\\\n[BBOX-863] & & & & & & & & \\\\\n[BBOX-864] & & & & & & & & \\\\\n[BBOX-865] & & & & & & & & \\\\\n[BBOX-866] & & & & & & & & \\\\\n[BBOX-867] & & & & & & & & \\\\\n[BBOX-868] & & & & & & & & \\\\\n[BBOX-869] & & & & & & & & \\\\\n[BBOX-870] & & & & & & & & \\\\\n[BBOX-871] & & & & & & & & \\\\\n[BBOX-872] & & & & & & & & \\\\\n[BBOX-873] & & & & & & & & \\\\\n[BBOX-874] & & & & & & & & \\\\\n[BBOX-875] & & & & & & & & \\\\\n[BBOX-876] & & & & & & & & \\\\\n[BBOX-877] & & & & & & & & \\\\\n[BBOX-878] & & & & & & & & \\\\\n[BBOX-879] & & & & & & & & \\\\\n[BBOX-880] & & & & & & & & \\\\\n[BBOX-881] & & & & & & & & \\\\\n[BBOX-882] & & & & & & & & \\\\\n[BBOX-883] & & & & & & & & \\\\\n[BBOX-884] & & & & & & & & \\\\\n[BBOX-885] & & & & & & & & \\\\\n[BBOX-886] & & & & & & & & \\\\\n[BBOX-887] & & & & & & & & \\\\\n[BBOX-888] & & & & & & & & \\\\\n[BBOX-889] & & & & & & & & \\\\\n[BBOX-890] & & & & & & & & \\\\\n[BBOX-891] & & & & & & & & \\\\\n[BBOX-892] & & & & & & & & \\\\\n[BBOX-893] & & & & & & & & \\\\\n[BBOX-894] & & & & & & & & \\\\\n[BBOX-895] & & & & & & & & \\\\\n[BBOX-896] & & & & & & & & \\\\\n[BBOX-897] & & & & & & & & \\\\\n[BBOX-898] & & & & & & & & \\\\\n[BBOX-899] & & & & & & & & \\\\\n[BBOX-900] & & & & & & & & \\\\\n[BBOX-901] & & & & & & & & \\\\\n[BBOX-902] & & & & & & & & \\\\\n[BBOX-903] & & & & & & & & \\\\\n[BBOX-904] & & & & & & & & \\\\\n[BBOX-905] & & & & & & & & \\\\\n[BBOX-906] & & & & & & & & \\\\\n[BBOX-907] & & & & & & & & \\\\\n[BBOX-908] & & & & & & & & \\\\\n[BBOX-909] & & & & & & & & \\\\\n[BBOX-910] & & & & & & & & \\\\\n[BBOX-911] & & & & & & & & \\\\\n[BBOX-912] & & & & & & & & \\\\\n[BBOX-913] & & & & & & & & \\\\\n[BBOX-914] & & & & & & & & \\\\\n[BBOX-915] & & & & & & & & \\\\\n[BBOX-916] & & & & & & & & \\\\\n[BBOX-917] & & & & & & & & \\\\\n[BBOX-918] & & & & & & & & \\\\\n[BBOX-919] & & & & & & & & \\\\\n[BBOX-920] & & & & & & & & \\\\\n[BBOX-921] & & & & & & & & \\\\\n[BBOX-922] & & & & & & & & \\\\\n[BBOX-923] & & & & & & & & \\\\\n[BBOX-924] & & & & & & & & \\\\\n[BBOX-925] & & & & & & & & \\\\\n[BBOX-926] & & & & & & & & \\\\\n[BBOX-927] & & & & & & & & \\\\\n[BBOX-928] & & & & & & & & \\\\\n[BBOX-929] & & & & & & & & \\\\\n[BBOX-930] & & & & & & & & \\\\\n[BBOX-931] & & & & & & & & \\\\\n[BBOX-932] & & & & & & & & \\\\\n[BBOX-933] & & & & & & & & \\\\\n[BBOX-934] & & & & & & & & \\\\\n[BBOX-935] & & & & & & & & \\\\\n[BBOX-936] & & & & & & & & \\\\\n[BBOX-937] & & & & & & & & \\\\\n[BBOX-938] & & & & & & & & \\\\\n[BBOX-939] & & & & & & & & \\\\\n[BBOX-940] & & & & & & & & \\\\\n[BBOX-941] & & & & & & & & \\\\\n[BBOX-942] & & & & & & & & \\\\\n[BBOX-943] & & & & & & & & \\\\\n[BBOX-944] & & & & & & & & \\\\\n[BBOX-945] & & & & & & & & \\\\\n[BBOX-946] & & & & & & & & \\\\\n[BBOX-947] & & & & & & & & \\\\\n[BBOX-948] & & & & & & & & \\\\\n[BBOX-949] & & & & & & & & \\\\\n[BBOX-950] & & & & & & & & \\\\\n[BBOX-951] & & & & & & & & \\\\\n[BBOX-952] & & & & & & & & \\\\\n[BBOX-953] & & & & & & & & \\\\\n[BBOX-954] & & & & & & & & \\\\\n[BBOX-955] & & & & & & & & \\\\\n[BBOX-956] & & & & & & & & \\\\\n[BBOX-957] & & & & & & & & \\\\\n[BBOX-958] & & & & & & & & \\\\\n[BBOX-959] & & & & & & & & \\\\\n[BBOX-960] & & & & & & & & \\\\\n[BBOX-961] & & & & & & & & \\\\\n[BBOX-962] & & & & & & & & \\\\\n[BBOX-963] & & & & & & & & \\\\\n[BBOX-964] & & & & & & & & \\\\\n[BBOX-965] & & & & & & & & \\\\\n[BBOX-966] & & & & & & & & \\\\\n[BBOX-967] & & & & & & & & \\\\\n[BBOX-968] & & & & & & & & \\\\\n[BBOX-969] & & & & & & & & \\\\\n[BBOX-970] & & & & & & & & \\\\\n[BBOX-971] & & & & & & & & \\\\\n[BBOX-972] & & & & & & & & \\\\\n[BBOX-973] & & & & & & & & \\\\\n[BBOX-974] & & & & & & & & \\\\\n[BBOX-975] & & & & & & & & \\\\\n[BBOX-976] & & & & & & & & \\\\\n[BBOX-977] & & & & & & & & \\\\\n[BBOX-978] & & & & & & & & \\\\\n[BBOX-979] & & & & & & & & \\\\\n[BBOX-980] & & & & & & & & \\\\\n[BBOX-981] & & & & & & & & \\\\\n[BBOX-982] & & & & & & & & \\\\\n[BBOX-983] & & & & & & & & \\\\\n[BBOX-984] & & & & & & & & \\\\\n[BBOX-985] & & & & & & & & \\\\\n[BBOX-986] & & & & & & & & \\\\\n[BBOX-987] & & & & & & & & \\\\\n[BBOX-988] & & & & & & & & \\\\\n[BBOX-989] & & & & & & & & \\\\\n[BBOX-990] & & & & & & & & \\\\\n[BBOX-991] & & & & & & & & \\\\\n[BBOX-992] & & & & & & & & \\\\\n[BBOX-993] & & & & & & & & \\\\\n[BBOX-994] & & & & & & & & \\\\\n[BBOX-995] & & & & & & & & \\\\\n[BBOX-996] & & & & & & & & \\\\\n[BBOX-997] & & & & & & & & \\\\\n[BBOX-998] & & & & & & & & \\\\\n[BBOX-999] & & & & & & & & \\\\\n[BBOX-1000] & & & & & & & & \\\\\n[BBOX-1001] & & & & & & & & \\\\\n[BBOX-1002] & & & & & & & & \\\\\n[BBOX-1003] & & & & & & & & \\\\\n[BBOX-1004] & & & & & & & & \\\\\n[BBOX-1005] & & & & & & & & \\\\\n[BBOX-1006] & & & & & & & & \\\\\n[BBOX-1007] & & & & & & & & \\\\\n[BBOX-1008] & & & & & & & & \\\\\n[BBOX-1009] & & & & & & & & \\\\\n[BBOX-1010] & & & & & & & & \\\\\n[BBOX-1011] & & & & & & & & \\\\\n[BBOX-1012] & & & & & & & & \\\\\n[BBOX-1013] & & & & & & & & \\\\\n[BBOX-1014] & & & & & & & & \\\\\n[BBOX-1015] & & & & & & & & \\\\\n[BBOX-1016] & & & & & & & & \\\\\n[BBOX-1017] & & & & & & & & \\\\\n[BBOX-1018] & & & & & & & & \\\\\n[BBOX-1019] & & & & & & & & \\\\\n[BBOX-1020] & & & & & & & & \\\\\n[BBOX-1021] & & & & & & & & \\\\\n[BBOX-1022] & & & & & & & & \\\\\n[BBOX-1023] & & & & & & & & \\\\\n[BBOX-1024] & & & & & & & & \\\\\n[BBOX-1025] & & & & & & & & \\\\\n[BBOX-1026] & & & & & & & & \\\\\n[BBOX-1027] & & & & & & & & \\\\\n[BBOX-1028] & & & & & & & & \\\\\n[BBOX-1029] & & & & & & & & \\\\\n[BBOX-1030] & & & & & & & & \\\\\n[BBOX-1031] & & & & & & & & \\\\\n[BBOX-1032] & & & & & & & & \\\\\n[BBOX-1033] & & & & & & & & \\\\\n[BBOX-1034] & & & & & & & & \\\\\n[BBOX-1035] & & & & & & & & \\\\\n[BBOX-1036] & & & & & & & & \\\\\n[BBOX-1037] & & & & & & & & \\\\\n[BBOX-1038] & & & & & & & & \\\\\n[BBOX-1039] & & & & & & & & \\\\\n[BBOX-1040] & & & & & & & & \\\\\n[BBOX-1041] & & & & & & & & \\\\\n[BBOX-1042] & & & & & & & & \\\\\n[BBOX-1043] & & & & & & & & \\\\\n[BBOX-1044] & & & & & & & & \\\\\n[BBOX-1045] & & & & & & & & \\\\\n[BBOX-1046] & & & & & & & & \\\\\n[BBOX-1047] & & & & & & & & \\\\\n[BBOX-1048] & & & & & & & & \\\\\n[BBOX-1049] & & & & & & & & \\\\\n[BBOX-1050] & & & & & & & & \\\\\n[BBOX-1051] & & & & & & & & \\\\\n[BBOX-1052] & & & & & & & & \\\\\n[BBOX-1053] & & & & & & & & \\\\\n[BBOX-1054] & & & & & & & & \\\\\n[BBOX-1055] & & & & & & & & \\\\\n[BBOX-1056] & & & & & & & & \\\\\n[BBOX-1057] & & & & & & & & \\\\\n[BBOX-1058] & & & & & & & & \\\\\n[BBOX-1059] & & & & & & & & \\\\\n[BBOX-1060] & & & & & & & & \\\\\n[BBOX-1061] & & & & & & & & \\\\\n[BBOX-1062] & & & & & & & & \\\\\n[BBOX-1063] & & & & & & & & \\\\\n[BBOX-1064] & & & & & & & & \\\\\n[BBOX-1065] & & & & & & & & \\\\\n[BBOX-1066] & & & & & & & & \\\\\n[BBOX-1067] & & & & & & & & \\\\\n[BBOX-1068] & & & & & & & & \\\\\n[BBOX-1069] & & & & & & & & \\\\\n[BBOX-1070] & & & & & & & & \\\\\n[BBOX-1071] & & & & & & & & \\\\\n[BBOX-1072] & & & & & & & & \\\\\n[BBOX-1073] & & & & & & & & \\\\\n[BBOX-1074] & & & & & & & & \\\\\n[BBOX-1075] & & & & & & & & \\\\\n[BBOX-1076] & & & & & & & & \\\\\n[BBOX-1077] & & & & & & & & \\\\\n[BBOX-1078] & & & & & & & & \\\\\n[BBOX-1079] & & & & & & & & \\\\\n[BBOX-1080] & & & & & & & & \\\\\n[BBOX-1081] & & & & & & & & \\\\\n[BBOX-1082] & & & & & & & & \\\\\n[BBOX-1083] & & & & & & & & \\\\\n[BBOX-1084] & & & & & & & & \\\\\n[BBOX-1085] & & & & & & & & \\\\\n[BBOX-1086] & & & & & & & & \\\\\n[BBOX-1087] & & & & & & & & \\\\\n[BBOX-1088] & & & & & & & & \\\\\n[BBOX-1089] & & & & & & & & \\\\\n[BBOX-1090] & & & & & & & & \\\\\n[BBOX-1091] & & & & & & & & \\\\\n[BBOX-1092] & & & & & & & & \\\\\n[BBOX-1093] & & & & & & & & \\\\\n[BBOX-1094] & & & & & & & & \\\\\n[BBOX-1095] & & & & & & & & \\\\\n[BBOX-1096] & & & & & & & & \\\\\n[BBOX-1097] & & & & & & & & \\\\\n[BBOX-1098] & & & & & & & & \\\\\n[BBOX-1099] & & & & & & & & \\\\\n[BBOX-1100] & & & & & & & & \\\\\n[BBOX-1101] & & & & & & & & \\\\\n[BBOX-1102] & & & & & & & & \\\\\n[BBOX-1103] & & & & & & & & \\\\\n[BBOX-1104] & & & & & & & & \\\\\n[BBOX-1105] & & & & & & & & \\\\\n[BBOX-1106] & & & & & & & & \\\\\n[BBOX-1107] & & & & & & & & \\\\\n[BBOX-1108] & & & & & & & & \\\\\n[BBOX-1109] & & & & & & & & \\\\\n[BBOX-1110] & & & & & & & & \\\\\n[BBOX-1111] & & & & & & & & \\\\\n[BBOX-1112] & & & & & & & & \\\\\n[BBOX-1113] & & & & & & & & \\\\\n[BBOX-1114] & & & & & & & & \\\\\n[BBOX-1115] & & & & & & & & \\\\\n[BBOX-1116] & & & & & & & & \\\\\n[BBOX-1117] & & & & & & & & \\\\\n[BBOX-1118] & & & & & & & & \\\\\n[BBOX-1119] & & & & & & & & \\\\\n[BBOX-1120] & & & & & & & & \\\\\n[BBOX-1121] & & & & & & & & \\\\\n[BBOX-1122] & & & & & & & & \\\\\n[BBOX-1123] & & & & & & & & \\\\\n[BBOX-1124] & & & & & & & & \\\\\n[BBOX-1125] & & & & & & & & \\\\\n[BBOX-1126] & & & & & & & & \\\\\n[BBOX-1127] & & & & & & & & \\\\\n[BBOX-1128] & & & & & & & & \\\\\n[BBOX-1129] & & & & & & & & \\\\\n[BBOX-1130] & & & & & & & & \\\\\n[BBOX-1131] & & & & & & & & \\\\\n[BBOX-1132] & & & & & & & & \\\\\n[BBOX-1133] & & & & & & & & \\\\\n[BBOX-1134] & & & & & & & & \\\\\n[BBOX-1135] & & & & & & & & \\\\\n[BBOX-1136] & & & & & & & & \\\\\n[BBOX-1137] & & & & & & & & \\\\\n[BBOX-1138] & & & & & & & & \\\\\n[BBOX-1139] & & & & & & & & \\\\\n[BBOX-1140] & & & & & & & & \\\\\n[BBOX-1141] & & & & & & & & \\\\\n[BBOX-1142] & & & & & & & & \\\\\n[BBOX-1143] & & & & & & & & \\\\\n[BBOX-1144] & & & & & & & & \\\\\n[BBOX-1145] & & & & & & & & \\\\\n[BBOX-1146] & & & & & & & & \\\\\n[BBOX-1147] & & & & & & & & \\\\\n[BBOX-1148] & & & & & & & & \\\\\n[BBOX-1149] & & & & & & & & \\\\\n[BBOX-1150] & & & & & & & & \\\\\n[BBOX-1151] & & & & & & & & \\\\\n[BBOX-1152] & & & & & & & & \\\\\n[BBOX-1153] & & & & & & & & \\\\\n[BBOX-1154] & & & & & & & & \\\\\n[BBOX-1155] & & & & & & & & \\\\\n[BBOX-1156] & & & & & & & & \\\\\n[BBOX-1157] & & & & & & & & \\\\\n[BBOX-1158] & & & & & & & & \\\\\n[BBOX-1159] & & & & & & & & \\\\\n[BBOX-1160] & & & & & & & & \\\\\n[BBOX-1161] & & & & & & & & \\\\\n[BBOX-1162] & & & & & & & & \\\\\n[BBOX-1163] & & & & & & & & \\\\\n[BBOX-1164] & & & & & & & & \\\\\n[BBOX-1165] & & & & & & & & \\\\\n[BBOX-1166] & & & & & & & & \\\\\n[BBOX-1167] & & & & & & & & \\\\\n[BBOX-1168] & & & & & & & & \\\\\n[BBOX-1169] & & & & & & & & \\\\\n[BBOX-1170] & & & & & & & & \\\\\n[BBOX-1171] & & & & & & & & \\\\\n[BBOX-1172] & & & & & & & & \\\\\n[BBOX-1173] & & & & & & & & \\\\\n[BBOX-1174] & & & & & & & & \\\\\n[BBOX-1175] & & & & & & & & \\\\\n[BBOX-1176] & & & & & & & & \\\\\n[BBOX-1177] & & & & & & & & \\\\\n[BBOX-1178] & & & & & & & & \\\\\n[BBOX-1179] & & & & & & & & \\\\\n[BBOX-1180] & & & & & & & & \\\\\n[BBOX-1181] & & & & & & & & \\\\\n[BBOX-1182] & & & & & & & & \\\\\n[BBOX-1183] & & & & & & & & \\\\\n[BBOX-1184] & & & & & & & & \\\\\n[BBOX-1185] & & & & & & & & \\\\\n[BBOX-1186] & & & & & & & & \\\\\n[BBOX-1187] & & & & & & & & \\\\\n[BBOX-1188] & & & & & & & & \\\\\n[BBOX-1189] & & & & & & & & \\\\\n[BBOX-1190] & & & & & & & & \\\\\n[BBOX-1191] & & & & & & & & \\\\\n[BBOX-1192] & & & & & & & & \\\\\n[BBOX-1193] & & & & & & & & \\\\\n[BBOX-1194] & & & & & & & & \\\\\n[BBOX-1195] & & & & & & & & \\\\\n[BBOX-1196] & & & & & & & & \\\\\n[BBOX-1197] & & & & & & & & \\\\\n[BBOX-1198] & & & & & & & & \\\\\n[BBOX-1199] & & & & & & & & \\\\\n[BBOX-1200] & & & & & & & & \\\\\n[BBOX-1201] & & & & & & & & \\\\\n[BBOX-1202] & & & & & & & & \\\\\n[BBOX-1203] & & & & & & & & \\\\\n[BBOX-1204] & & & & & & & & \\\\\n[BBOX-1205] & & & & & & & & \\\\\n[BBOX-1206] & & & & & & & & \\\\\n[BBOX-1207] & & & & & & & & \\\\\n[BBOX-1208] & & & & & & & & \\\\\n[BBOX-1209] & & & & & & & & \\\\\n[BBOX-1210] & & & & & & & & \\\\\n[BBOX-1211] & & & & & & & & \\\\\n[BBOX-1212] & & & & & & & & \\\\\n[BBOX-1213] & & & & & & & & \\\\\n[BBOX-1214] & & & & & & & & \\\\\n[BBOX-1215] & & & & & & & & \\\\\n[BBOX-1216] & & & & & & & & \\\\\n[BBOX-1217] & & & & & & & & \\\\\n[BBOX-1218] & & & & & & & & \\\\\n[BBOX-1219] & & & & & & & & \\\\\n[BBOX-1220] & & & & & & & & \\\\\n[BBOX-1221] & & & & & & & & \\\\\n[BBOX-1222] & & & & & & & & \\\\\n[BBOX-1223] & & & & & & & & \\\\\n[BBOX-1224] & & & & & & & & \\\\\n[BBOX-1225] & & & & & & & & \\\\\n[BBOX-1226] & & & & & & & & \\\\\n[BBOX-1227] & & & & & & & & \\\\\n[BBOX-1228] & & & & & & & & \\\\\n[BBOX-1229] & & & & & & & & \\\\\n[BBOX-1230] & & & & & & & & \\\\\n[BBOX-1231] & & & & & & & & \\\\\n[BBOX-1232] & & & & & & & & \\\\\n[BBOX-1233] & & & & & & & & \\\\\n[BBOX-1234] & & & & & & & & \\\\\n[BBOX-1235] & & & & & & & & \\\\\n[BBOX-1236] & & & & & & & & \\\\\n[BBOX-1237] & & & & & & & & \\\\\n[BBOX-1238] & & & & & & & & \\\\\n[BBOX-1239] & & & & & & & & \\\\\n[BBOX-1240] & & & & & & & & \\\\\n[BBOX-1241] & & & & & & & & \\\\\n[BBOX-1242] & & & & & & & & \\\\\n[BBOX-1243] & & & & & & & & \\\\\n[BBOX-1244] & & & & & & & & \\\\\n[BBOX-1245] & & & & & & & & \\\\\n[BBOX-1246] & & & & & & & & \\\\\n[BBOX-1247] & & & & & & & & \\\\\n[BBOX-1248] & & & & & & & & \\\\\n[BBOX-1249] & & & & & & & & \\\\\n[BBOX-1250] & & & & & & & & \\\\\n[BBOX-1251] & & & & & & & & \\\\\n[BBOX-1252] & & & & & & & & \\\\\n[BBOX-1253] & & & & & & & & \\\\\n[BBOX-1254] & & & & & & & & \\\\\n[BBOX-1255] & & & & & & & & \\\\\n[BBOX-1256] & & & & & & & & \\\\\n[BBOX-1257] & & & & & & & & \\\\\n[BBOX-1258] & & & & & & & & \\\\\n[BBOX-1259] & & & & & & & & \\\\\n[BBOX-1260] & & & & & & & & \\\\\n[BBOX-1261] & & & & & & & & \\\\\n[BBOX-1262] & & & & & & & & \\\\\n[BBOX-1263] & & & & & & & & \\\\\n[BBOX-1264] & & & & & & & & \\\\\n[BBOX-1265] & & & & & & & & \\\\\n[BBOX-1266] & & & & & & & & \\\\\n[BBOX-1267] & & & & & & & & \\\\\n[BBOX-1268] & & & & & & & & \\\\\n[BBOX-1269] & & & & & & & & \\\\\n[BBOX-1270] & & & & & & & & \\\\\n[BBOX-1271] & & & & & & & & \\\\\n[BBOX-1272] & & & & & & & & \\\\\n[BBOX-1273] & & & & & & & & \\\\\n[BBOX-1274] & & & & & & & & \\\\\n[BBOX-1275] & & & & & & & & \\\\\n[BBOX-1276] & & & & & & & & \\\\\n[BBOX-1277] & & & & & & & & \\\\\n[BBOX-1278] & & & & & & & & \\\\\n[BBOX-1279] & & & & & & & & \\\\\n[BBOX-1280] & & & & & & & & \\\\\n[BBOX-1281] & & & & & & & & \\\\\n[BBOX-1282] & & & & & & & & \\\\\n[BBOX-1283] & & & & & & & & \\\\\n[BBOX-1284] & & & & & & & & \\\\\n[BBOX-1285] & & & & & & & & \\\\\n[BBOX-1286] & & & & & & & & \\\\\n[BBOX-1287] & & & & & & & & \\\\\n[BBOX-1288] & & & & & & & & \\\\\n[BBOX-1289] & & & & & & & & \\\\\n[BBOX-1290] & & & & & & & & \\\\\n[BBOX-1291] & & & & & & & & \\\\\n[BBOX-1292] & & & & & & & & \\\\\n[BBOX-1293] & & & & & & & & \\\\\n[BBOX-1294] & & & & & & & & \\\\\n[BBOX-1295] & & & & & & & & \\\\\n[BBOX-1296] & & & & & & & & \\\\\n[BBOX-1297] & & & & & & & & \\\\\n[BBOX-1298] & & & & & & & & \\\\\n[BBOX-1299] & & & & & & & & \\\\\n[BBOX-1300] & & & & & & & & \\\\\n[BBOX-1301] & & & & & & & & \\\\\n[BBOX-1302] & & & & & & & & \\\\\n[BBOX-1303] & & & & & & & & \\\\\n[BBOX-1304] & & & & & & & & \\\\\n[BBOX-1305] & & & & & & & & \\\\\n[BBOX-1306] & & & & & & & & \\\\\n[BBOX-1307] & & & & & & & & \\\\\n[BBOX-1308] & & & & & & & & \\\\\n[BBOX-1309] & & & & & & & & \\\\\n[BBOX-1310] & & & & & & & & \\\\\n[BBOX-1311] & & & & & & & & \\\\\n[BBOX-1312] & & & & & & & & \\\\\n[BBOX-1313] & & & & & & & & \\\\\n[BBOX-1314] & & & & & & & & \\\\\n[BBOX-1315] & & & & & & & & \\\\\n[BBOX-1316] & & & & & & & & \\\\\n[BBOX-1317] & & & & & & & & \\\\\n[BBOX-1318] & & & & & & & & \\\\\n[BBOX-1319] & & & & & & & & \\\\\n[BBOX-1320] & & & & & & & & \\\\\n[BBOX-1321] & & & & & & & & \\\\\n[BBOX-1322] & & & & & & & & \\\\\n[BBOX-1323] & & & & & & & & \\\\\n[BBOX-1324] & & & & & & & & \\\\\n[BBOX-1325] & & & & & & & & \\\\\n[BBOX-1326] & & & & & & & & \\\\\n[BBOX-1327] & & & & & & & & \\\\\n[BBOX-1328] & & & & & & & & \\\\\n[BBOX-1329] & & & & & & & & \\\\\n[BBOX-1330] & & & & & & & & \\\\\n[BBOX-1331] & & & & & & & & \\\\\n[BBOX-1332] & & & & & & & & \\\\\n[BBOX-1333] & & & & & & & & \\\\\n[BBOX-1334] & & & & & & & & \\\\\n[BBOX-1335] & & & & & & & & \\\\\n[BBOX-1336] & & & & & & & & \\\\\n[BBOX-1337] & & & & & & & & \\\\\n[BBOX-1338] & & & & & & & & \\\\\n[BBOX-1339] & & & & & & & & \\\\\n[BBOX-1340] & & & & & & & & \\\\\n[BBOX-1341] & & & & & & & & \\\\\n[BBOX-1342] & & & & & & & & \\\\\n[BBOX-1343] & & & & & & & & \\\\\n[BBOX-1344] & & & & & & & & \\\\\n[BBOX-1345] & & & & & & & & \\\\\n[BBOX-1346] & & & & & & & & \\\\\n[BBOX-1347] & & & & & & & & \\\\\n[BBOX-1348] & & & & & & & & \\\\\n[BBOX-1349] & & & & & & & & \\\\\n[BBOX-1350] & & & & & & & & \\\\\n[BBOX-1351] & & & & & & & & \\\\\n[BBOX-1352] & & & & & & & & \\\\\n[BBOX-1353] & & & & & & & & \\\\\n[BBOX-1354] & & & & & & & & \\\\\n[BBOX-1355] & & & & & & & & \\\\\n[BBOX-1356] & & & & & & & & \\\\\n[BBOX-1357] & & & & & & & & \\\\\n[BBOX-1358] & & & & & & & & \\\\\n[BBOX-1359] & & & & & & & & \\\\\n[BBOX-1360] & & & & & & & & \\\\\n[BBOX-1361] & & & & & & & & \\\\\n[BBOX-1362] & & & & & & & & \\\\\n[BBOX-1363] & & & & & & & & \\\\\n[BBOX-1364] & & & & & & & & \\\\\n[BBOX-1365] & & & & & & & & \\\\\n[BBOX-1366] & & & & & & & & \\\\\n[BBOX-1367] & & & & & & & & \\\\\n[BBOX-1368] & & & & & & & & \\\\\n[BBOX-1369] & & & & & & & & \\\\\n[BBOX-1370] & & & & & & & & \\\\\n[BBOX-1371] & & & & & & & & \\\\\n[BBOX-1372] & & & & & & & & \\\\\n[BBOX-1373] & & & & & & & & \\\\\n[BBOX-1374] & & & & & & & & \\\\\n[BBOX-1375] & & & & & & & & \\\\\n[BBOX-1376] & & & & & & & & \\\\\n[BBOX-1377] & & & & & & & & \\\\\n[BBOX-1378] & & & & & & & & \\\\\n[BBOX-1379] & & & & & & & & \\\\\n[BBOX-1380] & & & & & & & & \\\\\n[BBOX-1381] & & & & & & & & \\\\\n[BBOX-1382] & & & & & & & & \\\\\n[BBOX-1383] & & & & & & & & \\\\\n[BBOX-1384] & & & & & & & & \\\\\n[BBOX-1385] & & & & & & & & \\\\\n[BBOX-1386] & & & & & & & & \\\\\n[BBOX-1387] & & & & & & & & \\\\\n[BBOX-1388] & & & & & & & & \\\\\n[BBOX-1389] & & & & & & & & \\\\\n[BBOX-1390] & & & & & & & & \\\\\n[BBOX-1391] & & & & & & & & \\\\\n[BBOX-1392] & & & & & & & & \\\\\n[BBOX-1393] & & & & & & & & \\\\\n[BBOX-1394] & & & & & & & & \\\\\n[BBOX-1395] & & & & & & & & \\\\\n[BBOX-1396] & & & & & & & & \\\\\n[BBOX-1397] & & & & & & & & \\\\\n[BBOX-1398] & & & & & & & & \\\\\n[BBOX-1399] & & & & & & & & \\\\\n[BBOX-1400] & & & & & & & & \\\\\n[BBOX-1401] & & & & & & & & \\\\\n[BBOX-1402] & & & & & & & & \\\\\n[BBOX-1403] & & & & & & & & \\\\\n[BBOX-1404] & & & & & & & & \\\\\n[BBOX-1405] & & & & & & & & \\\\\n[BBOX-1406] & & & & & & & & \\\\\n[BBOX-1407] & & & & & & & & \\\\\n[BBOX-1408] & & & & & & & & \\\\\n[BBOX-1409] & & & & & & & & \\\\\n[BBOX-1410] & & & & & & & & \\\\\n[BBOX-1411] & & & & & & & & \\\\\n[BBOX-1412] & & & & & & & & \\\\\n[BBOX-1413] & & & & & & & & \\\\\n[BBOX-1414] & & & & & & & & \\\\\n[BBOX-1415] & & & & & & & & \\\\\n[BBOX-1416] & & & & & & & & \\\\\n[BBOX-1417] & & & & & & & & \\\\\n[BBOX-1418] & & & & & & & & \\\\\n[BBOX-1419] & & & & & & & & \\\\\n[BBOX-1420] & & & & & & & & \\\\\n[BBOX-1421] & & & & & & & & \\\\\n[BBOX-1422] & & & & & & & & \\\\\n[BBOX-1423] & & & & & & & & \\\\\n[BBOX-1424] & & & & & & & & \\\\\n[BBOX-1425] & & & & & & & & \\\\\n[BBOX-1426] & & & & & & & & \\\\\n[BBOX-1427] & & & & & & & & \\\\\n[BBOX-1428] & & & & & & & & \\\\\n[BBOX-1429] & & & & & & & & \\\\\n[BBOX-1430] & & & & & & & & \\\\\n[BBOX-1431] & & & & & & & & \\\\\n[BBOX-1432] & & & & & & & & \\\\\n[BBOX-1433] & & & & & & & & \\\\\n[BBOX-1434] & & & & & & & & \\\\\n[BBOX-1435] & & & & & & & & \\\\\n[BBOX-1436] & & & & & & & & \\\\\n[BBOX-1437] & & & & & & & & \\\\\n[BBOX-1438] & & & & & & & & \\\\\n[BBOX-1439] & & & & & & & & \\\\\n[BBOX-1440] & & & & & & & & \\\\\n[BBOX-1441] & & & & & & & & \\\\\n[BBOX-1442] & & & & & & & & \\\\\n[BBOX-1443] & & & & & & & & \\\\\n[BBOX-1444] & & & & & & & & \\\\\n[BBOX-1445] & & & & & & & & \\\\\n[BBOX-1446] & & & & & & & & \\\\\n[BBOX-1447] & & & & & & & & \\\\\n[BBOX-1448] & & & & & & & & \\\\\n[BBOX-1449] & & & & & & & & \\\\\n[BBOX-1450] & & & & & & & & \\\\\n[BBOX-1451] & & & & & & & & \\\\\n[BBOX-1452] & & & & & & & & \\\\\n[BBOX-1453] & & & & & & & & \\\\\n[BBOX-1454] & & & & & & & & \\\\\n[BBOX-1455] & & & & & & & & \\\\\n[BBOX-1456] & & & & & & & & \\\\\n[BBOX-1457] & & & & & & & & \\\\\n[BBOX-1458] & & & & & & & & \\\\\n[BBOX-1459] & & & & & & & & \\\\\n[BBOX-1460] & & & & & & & & \\\\\n[BBOX-1461] & & & & & & & & \\\\\n[BBOX-1462] & & & & & & & & \\\\\n[BBOX-1463] & & & & & & & & \\\\\n[BBOX-1464] & & & & & & & & \\\\\n[BBOX-1465] & & & & & & & & \\\\\n[BBOX-1466] & & & & & & & & \\\\\n[BBOX-1467] & & & & & & & & \\\\\n[BBOX-1468] & & & & & & & & \\\\\n[BBOX-1469] & & & & & & & & \\\\\n[BBOX-1470] & & & & & & & & \\\\\n[BBOX-1471] & & & & & & & & \\\\\n[BBOX-1472] & & & & & & & & \\\\\n[BBOX-1473] & & & & & & & & \\\\\n[BBOX-1474] & & & & & & & & \\\\\n[BBOX-1475] & & & & & & & & \\\\\n[BBOX-1476] & & & & & & & & \\\\\n[BBOX-1477] & & & & & & & & \\\\\n[BBOX-1478] & & & & & & & & \\\\\n[BBOX-1479] & & & & & & & & \\\\\n[BBOX-1480] & & & & & & & & \\\\\n[BBOX-1481] & & & & & & & & \\\\\n[BBOX-1482] & & & & & & & & \\\\\n[BBOX-1483] & & & & & & & & \\\\\n[BBOX-1484] & & & & & & & & \\\\\n[BBOX-1485] & & & & & & & & \\\\\n[BBOX-1486] & & & & & & & & \\\\\n[BBOX-1487] & & & & & & & & \\\\\n[BBOX-1488] & & & & & & & & \\\\\n[BBOX-1489] & & & & & & & & \\\\\n[BBOX-1490] & & & & & & & & \\\\\n[BBOX-1491] & & & & & & & & \\\\\n[BBOX-1492] & & & & & & & & \\\\\n[BBOX-1493] & & & & & & & & \\\\\n[BBOX-1494] & & & & & & & & \\\\\n[BBOX-1495] & & & & & & & & \\\\\n[BBOX-1496] & & & & & & & & \\\\\n[BBOX-1497] & & & & & & & & \\\\\n[BBOX-1498] & & & & & & & & \\\\\n[BBOX-1499] & & & & & & & & \\\\\n[BBOX-1500] & & & & & & & & \\\\\n[BBOX-1501] & & & & & & & & \\\\\n[BBOX-1502] & & & & & & & & \\\\\n[BBOX-1503] & & & & & & & & \\\\\n[BBOX-1504] & & & & & & & & \\\\\n[BBOX-1505] & & & & & & & & \\\\\n[BBOX-1506] & & & & & & & & \\\\\n[BBOX-1507] & & & & & & & & \\\\\n[BBOX-1508] & & & & & & & & \\\\\n[BBOX-1509] & & & & & & & & \\\\\n[BBOX-1510] & & & & & & & & \\\\\n[BBOX-1511] & & & & & & & & \\\\\n[BBOX-1512] & & & & & & & & \\\\\n[BBOX-1513] & & & & & & & & \\\\\n[BBOX-1514] & & & & & & & & \\\\\n[BBOX-1515] & & & & & & & & \\\\\n[BBOX-1516] & & & & & & & & \\\\\n[BBOX-1517] & & & & & & & & \\\\\n[BBOX-1518] & & & & & & & & \\\\\n[BBOX-1519] & & & & & & & & \\\\\n[BBOX-1520] & & & & & & & & \\\\\n[BBOX-1521] & & & & & & & & \\\\\n[BBOX-1522] & & & & & & & & \\\\\n[BBOX-1523] & & & & & & & & \\\\\n[BBOX-1524] & & & & & & & & \\\\\n[BBOX-1525] & & & & & & & & \\\\\n[BBOX-1526] & & & & & & & & \\\\\n[BBOX-1527] & & & & & & & & \\\\\n[BBOX-1528] & & & & & & & & \\\\\n[BBOX-1529] & & & & & & & & \\\\\n[BBOX-1530] & & & & & & & & \\\\\n[BBOX-1531] & & & & & & & & \\\\\n[BBOX-1532] & & & & & & & & \\\\\n[BBOX-1533] & & & & & & & & \\\\\n[BBOX-1534] & & & & & & & & \\\\\n[BBOX-1535] & & & & & & & & \\\\\n[BBOX-1536] & & & & & & & & \\\\\n[BBOX-1537] & & & & & & & & \\\\\n[BBOX-1538] & & & & & & & & \\\\\n[BBOX-1539] & & & & & & & & \\\\\n[BBOX-1540] & & & & & & & & \\\\\n[BBOX-1541] & & & & & & & & \\\\\n[BBOX-1542] & & & & & & & & \\\\\n[BBOX-1543] & & & & & & & & \\\\\n[BBOX-1544] & & & & & & & & \\\\\n[BBOX-1545] & & & & & & & & \\\\\n[BBOX-1546] & & & & & & & & \\\\\n[BBOX-1547] & & & & & & & & \\\\\n[BBOX-1548] & & & & & & & & \\\\\n[BBOX-1549] & & & & & & & & \\\\\n[BBOX-1550] & & & & & & & & \\\\\n[BBOX-1551] & & & & & & & & \\\\\n[BBOX-1552] & & & & & & & & \\\\\n[BBOX-1553] & & & & & & & & \\\\\n[BBOX-1554] & & & & & & & & \\\\\n[BBOX-1555] & & & & & & & & \\\\\n[BBOX-1556] & & & & & & & & \\\\\n[BBOX-1557] & & & & & & & & \\\\\n[BBOX-1558] & & & & & & & & \\\\\n[BBOX-1559] & & & & & & & & \\\\\n[BBOX-1560] & & & & & & & & \\\\\n[BBOX-1561] & & & & & & & & \\\\\n[BBOX-1562] & & & & & & & & \\\\\n[BBOX-1563] & & & & & & & & \\\\\n[BBOX-1564] & & & & & & & & \\\\\n[BBOX-1565] & & & & & & & & \\\\\n[BBOX-1566] & & & & & & & & \\\\\n[BBOX-1567] & & & & & & & & \\\\\n[BBOX-1568] & & & & & & & & \\\\\n[BBOX-1569] & & & & & & & & \\\\\n[BBOX-1570] & & & & & & & & \\\\\n[BBOX-1571] & & & & & & & & \\\\\n[BBOX-1572] & & & & & & & & \\\\\n[BBOX-1573] & & & & & & & & \\\\\n[BBOX-1574] & & & & & & & & \\\\\n[BBOX-1575] & & & & & & & & \\\\\n[BBOX-1576] & & & & & & & & \\\\\n[BBOX-1577] & & & & & & & & \\\\\n[BBOX-1578] & & & & & & & & \\\\\n[BBOX-1579] & & & & & & & & \\\\\n[BBOX-1580] & & & & & & & & \\\\\n[BBOX-1581] & & & & & & & & \\\\\n[BBOX-1582] & & & & & & & & \\\\\n[BBOX-1583] & & & & & & & & \\\\\n[BBOX-1584] & & & & & & & & \\\\\n[BBOX-1585] & & & & & & & & \\\\\n[BBOX-1586] & & & & & & & & \\\\\n[BBOX-1587] & & & & & & & & \\\\\n[BBOX-1588] & & & & & & & & \\\\\n[BBOX-1589] & & & & & & & & \\\\\n[BBOX-1590] & & & & & & & & \\\\\n[BBOX-1591] & & & & & & & & \\\\\n[BBOX-1592] & & & & & & & & \\\\\n[BBOX-1593] & & & & & & & & \\\\\n[BBOX-1594] & & & & & & & & \\\\\n[BBOX-1595] & & & & & & & & \\\\\n[BBOX-1596] & & & & & & & & \\\\\n[BBOX-1597] & & & & & & & & \\\\\n[BBOX-1598] & & & & & & & & \\\\\n[BBOX-1599] & & & & & & & & \\\\\n[BBOX-1600] & & & & & & & & \\\\\n[BBOX-1601] & & & & & & & & \\\\\n[BBOX-1602] & & & & & & & & \\\\\n[BBOX-1603] & & & & & & & & \\\\\n[BBOX-1604] & & & & & & & & \\\\\n[BBOX-1605] & & & & & & & & \\\\\n[BBOX-1606] & & & & & & & & \\\\\n[BBOX-1607] & & & & & & & & \\\\\n[BBOX-1608] & & & & & & & & \\\\\n[BBOX-1609] & & & & & & & & \\\\\n[BBOX-1610] & & & & & & & & \\\\\n[BBOX-1611] & & & & & & & & \\\\\n[BBOX-1612] & & & & & & & & \\\\\n[BBOX-1613] & & & & & & & & \\\\\n[BBOX-1614] & & & & & & & & \\\\\n[BBOX-1615] & & & & & & & & \\\\\n[BBOX-1616] & & & & & & & & \\\\\n[BBOX-1617] & & & & & & & & \\\\\n[BBOX-1618] & & & & & & & & \\\\\n[BBOX-1619] & & & & & & & & \\\\\n[BBOX-1620] & & & & & & & & \\\\\n[BBOX-1621] & & & & & & & & \\\\\n[BBOX-1622] & & & & & & & & \\\\\n[BBOX-1623] & & & & & & & & \\\\\n[BBOX-1624] & & & & & & & & \\\\\n[BBOX-1625] & & & & & & & & \\\\\n[BBOX-1626] & & & & & & & & \\\\\n[BBOX-1627] & & & & & & & & \\\\\n[BBOX-1628] & & & & & & & & \\\\\n[BBOX-1629] & & & & & & & & \\\\\n[BBOX-1630] & & & & & & & & \\\\\n[BBOX-1631] & & & & & & & & \\\\\n[BBOX-1632] & & & & & & & & \\\\\n[BBOX-1633] & & & & & & & & \\\\\n[BBOX-1634] & & & & & & & & \\\\\n[BBOX-1635] & & & & & & & & \\\\\n[BBOX-1636] & & & & & & & & \\\\\n[BBOX-1637] & & & & & & & & \\\\\n[BBOX-1638] & & & & & & & & \\\\\n[BBOX-1639] & & & & & & & & \\\\\n[BBOX-1640] & & & & & & & & \\\\\n[BBOX-1641] & & & & & & & & \\\\\n[BBOX-1642] & & & & & & & & \\\\\n[BBOX-1643] & & & & & & & & \\\\\n[BBOX-1644] & & & & & & & & \\\\\n[BBOX-1645] & & & & & & & & \\\\\n[BBOX-1646] & & & & & & & & \\\\\n[BBOX-1647] & & & & & & & & \\\\\n[BBOX-1648] & & & & & & & & \\\\\n[BBOX-1649] & & & & & & & & \\\\\n[BBOX-1650] & & & & & & & & \\\\\n[BBOX-1651] & & & & & & & & \\\\\n[BBOX-1652] & & & & & & & & \\\\\n[BBOX-1653] & & & & & & & & \\\\\n[BBOX-1654] & & & & & & & & \\\\\n[BBOX-1655] & & & & & & & & \\\\\n[BBOX-1656] & & & & & & & & \\\\\n[BBOX-1657] & & & & & & & & \\\\\n[BBOX-1658] & & & & & & & & \\\\\n[BBOX-1659] & & & & & & & & \\\\\n[BBOX-1660] & & & & & & & & \\\\\n[BBOX-1661] & & & & & & & & \\\\\n[BBOX-1662] & & & & & & & & \\\\\n[BBOX-1663] & & & & & & & & \\\\\n[BBOX-1664] & & & & & & & & \\\\\n[BBOX-1665] & & & & & & & & \\\\\n[BBOX-1666] & & & & & & & & \\\\\n[BBOX-1667] & & & & & & & & \\\\\n[BBOX-1668] & & & & & & & & \\\\\n[BBOX-1669] & & & & & & & & \\\\\n[BBOX-1670] & & & & & & & & \\\\\n[BBOX-1671] & & & & & & & & \\\\\n[BBOX-1672] & & & & & & & & \\\\\n[BBOX-1673] & & & & & & & & \\\\\n[BBOX-1674] & & & & & & & & \\\\\n[BBOX-1675] & & & & & & & & \\\\\n[BBOX-1676] & & & & & & & & \\\\\n[BBOX-1677] & & & & & & & & \\\\\n[BBOX-1678] & & & & & & & & \\\\\n[BBOX-1679] & & & & & & & & \\\\\n[BBOX-1680] & & & & & & & & \\\\\n[BBOX-1681] & & & & & & & & \\\\\n[BBOX-1682] & & & & & & & & \\\\\n[BBOX-1683] & & & & & & & & \\\\\n[BBOX-1684] & & & & & & & & \\\\\n[BBOX-1685] & & & & & & & & \\\\\n[BBOX-1686] & & & & & & & & \\\\\n[BBOX-1687] & & & & & & & & \\\\\n[BBOX-1688] & & & & & & & & \\\\\n[BBOX-1689] & & & & & & & & \\\\\n[BBOX-1690] & & & & & & & & \\\\\n[BBOX-1691] & & & & & & & & \\\\\n[BBOX-1692] & & & & & & & & \\\\\n[BBOX-1693] & & & & & & & & \\\\\n[BBOX-1694] & & & & & & & & \\\\\n[BBOX-1695] & & & & & & & & \\\\\n[BBOX-1696] & & & & & & & & \\\\\n[BBOX-1697] & & & & & & & & \\\\\n[BBOX-1698] & & & & & & & & \\\\\n[BBOX-1699] & & & & & & & & \\\\\n[BBOX-1700] & & & & & & & & \\\\\n[BBOX-1701] & & & & & & & & \\\\\n[BBOX-1702] & & & & & & & & \\\\\n[BBOX-1703] & & & & & & & & \\\\\n[BBOX-1704] & & & & & & & & \\\\\n[BBOX-1705] & & & & & & & & \\\\\n[BBOX-1706] & & & & & & & & \\\\\n[BBOX-1707] & & & & & & & & \\\\\n[BBOX-1708] & & & & & & & & \\\\\n[BBOX-1709] & & & & & & & & \\\\\n[BBOX-1710] & & & & & & & & \\\\\n[BBOX-1711] & & & & & & & & \\\\\n[BBOX-1712] & & & & & & & & \\\\\n[BBOX-1713] & & & & & & & & \\\\\n[BBOX-1714] & & & & & & & & \\\\\n[BBOX-1715] & & & & & & & & \\\\\n[BBOX-1716] & & & & & & & & \\\\\n[BBOX-1717] & & & & & & & & \\\\\n[BBOX-1718] & & & & & & & & \\\\\n[BBOX-1719] & & & & & & & & \\\\\n[BBOX-1720] & & & & & & & & \\\\\n[BBOX-1721] & & & & & & & & \\\\\n[BBOX-1722] & & & & & & & & \\\\\n[BBOX-1723] & & & & & & & & \\\\\n[BBOX-1724] & & & & & & & & \\\\\n[BBOX-1725] & & & & & & & & \\\\\n[BBOX-1726] & & & & & & & & \\\\\n[BBOX-1727] & & & & & & & & \\\\\n[BBOX-1728] & & & & & & & & \\\\\n[BBOX-1729] & & & & & & & & \\\\\n[BBOX-1730] & & & & & & & & \\\\\n[BBOX-1731] & & & & & & & & \\\\\n[BBOX-1732] & & & & & & & & \\\\\n[BBOX-1733] & & & & & & & & \\\\\n[BBOX-1734] & & & & & & & & \\\\\n[BBOX-1735] & & & & & & & & \\\\\n[BBOX-1736] & & & & & & & & \\\\\n[BBOX-1737] & & & & & & & & \\\\\n[BBOX-1738] & & & & & & & & \\\\\n[BBOX-1739] & & & & & & & & \\\\\n[BBOX-1740] & & & & & & & & \\\\\n[BBOX-1741] & & & & & & & & \\\\\n[BBOX-1742] & & & & & & & & \\\\\n[BBOX-1743] & & & & & & & & \\\\\n[BBOX-1744] & & & & & & & & \\\\\n[BBOX-1745] & & & & & & & & \\\\\n[BBOX-1746] & & & & & & & & \\\\\n[BBOX-1747] & & & & & & & & \\\\\n[BBOX-1748] & & & & & & & & \\\\\n[BBOX-1749] & & & & & & & & \\\\\n[BBOX-1750] & & & & & & & & \\\\\n[BBOX-1751] & & & & & & & & \\\\\n[BBOX-1752] & & & & & & & & \\\\\n[BBOX-1753] & & & & & & & & \\\\\n[BBOX-1754] & & & & & & & & \\\\\n[BBOX-1755] & & & & & & & & \\\\\n[BBOX-1756] & & & & & & & & \\\\\n[BBOX-1757] & & & & & & & & \\\\\n[BBOX-1758] & & & & & & & & \\\\\n[BBOX-1759] & & & & & & & & \\\\\n[BBOX-1760] & & & & & & & & \\\\\n[BBOX-1761] & & & & & & & & \\\\\n[BBOX-1762] & & & & & & & & \\\\\n[BBOX-1763] & & & & & & & & \\\\\n[BBOX-1764] & & & & & & & & \\\\\n[BBOX-1765] & & & & & & & & \\\\\n[BBOX-1766] & & & & & & & & \\\\\n[BBOX-1767] & & & & & & & & \\\\\n[BBOX-1768] & & & & & & & & \\\\\n[BBOX-1769] & & & & & & & & \\\\\n[BBOX-1770] & & & & & & & & \\\\\n[BBOX-1771] & & & & & & & & \\\\\n[BBOX-1772] & & & & & & & & \\\\\n[BBOX-1773] & & & & & & & & \\\\\n[BBOX-1774] & & & & & & & & \\\\\n[BBOX-1775] & & & & & & & & \\\\\n[BBOX-1776] & & & & & & & & \\\\\n[BBOX-1777] & & & & & & & & \\\\\n[BBOX-1778] & & & & & & & & \\\\\n[BBOX-1779] & & & & & & & & \\\\\n[BBOX-1780] & & & & & & & & \\\\\n[BBOX-1781] & & & & & & & & \\\\\n[BBOX-1782] & & & & & & & & \\\\\n[BBOX-1783] & & & & & & & & \\\\\n[BBOX-1784] & & & & & & & & \\\\\n[BBOX-1785] & & & & & & & & \\\\\n[BBOX-1786] & & & & & & & & \\\\\n[BBOX-1787] & & & & & & & & \\\\\n[BBOX-1788] & & & & & & & & \\\\\n[BBOX-1789] & & & & & & & & \\\\\n[BBOX-1790] & & & & & & & & \\\\\n[BBOX-1791] & & & & & & & & \\\\\n[BBOX-1792] & & & & & & & & \\\\\n[BBOX-1793] & & & & & & & & \\\\\n[BBOX-1794] & & & & & & & & \\\\\n[BBOX-1795] & & & & & & & & \\\\\n[BBOX-1796] & & & & & & & & \\\\\n[BBOX-1797] & & & & & & & & \\\\\n[BBOX-1798] & & & & & & & & \\\\\n[BBOX-1799] & & & & & & & & \\\\\n[BBOX-1800] & & & & & & & & \\\\\n[BBOX-1801] & & & & & & & & \\\\\n[BBOX-1802] & & & & & & & & \\\\\n[BBOX-1803] & & & & & & & & \\\\\n[BBOX-1804] & & & & & & & & \\\\\n[BBOX-1805] & & & & & & & & \\\\\n[BBOX-1806] & & & & & & & & \\\\\n[BBOX-1807] & & & & & & & & \\\\\n[BBOX-1808] & & & & & & & & \\\\\n[BBOX-1809] & & & & & & & & \\\\\n[BBOX-1810] & & & & & & & & \\\\\n[BBOX-1811] & & & & & & & & \\\\\n[BBOX-1812] & & & & & & & & \\\\\n[BBOX-1813] & & & & & & & & \\\\\n[BBOX-1814] & & & & & & & & \\\\\n[BBOX-1815] & & & & & & & & \\\\\n[BBOX-1816] & & & & & & & & \\\\\n[BBOX-1817] & & & & & & & & \\\\\n[BBOX-1818] & & & & & & & & \\\\\n[BBOX-1819] & & & & & & & & \\\\\n[BBOX-1820] & & & & & & & & \\\\\n[BBOX-1821] & & & & & & & & \\\\\n[BBOX-1822] & & & & & & & & \\\\\n[BBOX-1823] & & & & & & & & \\\\\n[BBOX-1824] & & & & & & & & \\\\\n[BBOX-1825] & & & & & & & & \\\\\n[BBOX-1826] & & & & & & & & \\\\\n[BBOX-1827] & & & & & & & & \\\\\n[BBOX-1828] & & & & & & & & \\\\\n[BBOX-1829] & & & & & & & & \\\\\n[BBOX-1830] & & & & & & & & \\\\\n[BBOX-1831] & & & & & & & & \\\\\n[BBOX-1832] & & & & & & & & \\\\\n[BBOX-1833] & & & & & & & & \\\\\n[BBOX-1834] & & & & & & & & \\\\\n[BBOX-1835] & & & & & & & & \\\\\n[BBOX-1836] & & & & & & & & \\\\\n[BBOX-1837] & & & & & & & & \\\\\n[BBOX-1838] & & & & & & & & \\\\\n[BBOX-1839] & & & & & & & & \\\\\n[BBOX-1840] & & & & & & & & \\\\\n[BBOX-1841] & & & & & & & & \\\\\n[BBOX-1842] & & & & & & & & \\\\\n[BBOX-1843] & & & & & & & & \\\\\n[BBOX-1844] & & & & & & & & \\\\\n[BBOX-1845] & & & & & & & & \\\\\n[BBOX-1846] & & & & & & & & \\\\\n[BBOX-1847] & & & & & & & & \\\\\n[BBOX-1848] & & & & & & & & \\\\\n[BBOX-1849] & & & & & & & & \\\\\n[BBOX-1850] & & & & & & & & \\\\\n[BBOX-1851] & & & & & & & & \\\\\n[BBOX-1852] & & & & & & & & \\\\\n[BBOX-1853] & & & & & & & & \\\\\n[BBOX-1854] & & & & & & & & \\\\\n[BBOX-1855] & & & & & & & & \\\\\n[BBOX-1856] & & & & & & & & \\\\\n[BBOX-1857] & & & & & & & & \\\\\n[BBOX-1858] & & & & & & & & \\\\\n[BBOX-1859] & & & & & & & & \\\\\n[BBOX-1860] & & & & & & & & \\\\\n[BBOX-1861] & & & & & & & & \\\\\n[BBOX-1862] & & & & & & & & \\\\\n[BBOX-1863] & & & & & & & & \\\\\n[BBOX-1864] & & & & & & & & \\\\\n[BBOX-1865] & & & & & & & & \\\\\n[BBOX-1866] & & & & & & & & \\\\\n[BBOX-1867] & & & & & & & & \\\\\n[BBOX-1868] & & & & & & & & \\\\\n[BBOX-1869] & & & & & & & & \\\\\n[BBOX-1870] & & & & & & & & \\\\\n[BBOX-1871] & & & & & & & & \\\\\n[BBOX-1872] & & & & & & & & \\\\\n[BBOX-1873] & & & & & & & & \\\\\n[BBOX-1874] & & & & & & & & \\\\\n[BBOX-1875] & & & & & & & & \\\\\n[BBOX-1876] & & & & & & & & \\\\\n[BBOX-1877] & & & & & & & & \\\\\n[BBOX-1878] & & & & & & & & \\\\\n[BBOX-1879] & & & & & & & & \\\\\n[BBOX-1880] & & & & & & & & \\\\\n[BBOX-1881] & & & & & & & & \\\\\n[BBOX-1882] & & & & & & & & \\\\\n[BBOX-1883] & & & & & & & & \\\\\n[BBOX-1884] & & & & & & & & \\\\\n[BBOX-1885] & & & & & & & & \\\\\n[BBOX-1886] & & & & & & & & \\\\\n[BBOX-1887] & & & & & & & & \\\\\n[BBOX-1888] & & & & & & & & \\\\\n[BBOX-1889] & & & & & & & & \\\\\n[BBOX-1890] & & & & & & & & \\\\\n[BBOX-1891] & & & & & & & & \\\\\n[BBOX-1892] & & & & & & & & \\\\\n[BBOX-1893] & & & & & & & & \\\\\n[BBOX-1894] & & & & & & & & \\\\\n[BBOX-1895] & & & & & & & & \\\\\n[BBOX-1896] & & & & & & & & \\\\\n[BBOX-1897] & & & & & & & & \\\\\n[BBOX-1898] & & & & & & & & \\\\\n[BBOX-1899] & & & & & & & & \\\\\n[BBOX-1900] & & & & & & & & \\\\\n[BBOX-1901] & & & & & & & & \\\\\n[BBOX-1902] & & & & & & & & \\\\\n[BBOX-1903] & & & & & & & & \\\\\n[BBOX-1904] & & & & & & & & \\\\\n[BBOX-1905] & & & & & & & & \\\\\n[BBOX-1906] & & & & & & & & \\\\\n[BBOX-1907] & & & & & & & & \\\\\n[BBOX-1908] & & & & & & & & \\\\\n[BBOX-1909] & & & & & & & & \\\\\n[BBOX-1910] & & & & & & & & \\\\\n[BBOX-1911] & & & & & & & & \\\\\n[BBOX-1912] & & & & & & & & \\\\\n[BBOX-1913] & & & & & & & & \\\\\n[BBOX-1914] & & & & & & & & \\\\\n[BBOX-1915] & & & & & & & & \\\\\n[BBOX-1916] & & & & & & & & \\\\\n[BBOX-1917] & & & & & & & & \\\\\n[BBOX-1918] & & & & & & & & \\\\\n[BBOX-1919] & & & & & & & & \\\\\n[BBOX-1920] & & & & & & & & \\\\\n[BBOX-1921] & & & & & & & & \\\\\n[BBOX-1922] & & & & & & & & \\\\\n[BBOX-1923] & & & & & & & & \\\\\n[BBOX-1924] & & & & & & & & \\\\\n[BBOX-1925] & & & & & & & & \\\\\n[BBOX-1926] & & & & & & & & \\\\\n[BBOX-1927] & & & & & & & & \\\\\n[BBOX-1928] & & & & & & & & \\\\\n[BBOX-1929] & & & & & & & & \\\\\n[BBOX-1930] & & & & & & & & \\\\\n[BBOX-1931] & & & & & & & & \\\\\n[BBOX-1932] & & & & & & & & \\\\\n[BBOX-1933] & & & & & & & & \\\\\n[BBOX-1934] & & & & & & & & \\\\\n[BBOX-1935] & & & & & & & & \\\\\n[BBOX-1936] & & & & & & & & \\\\\n[BBOX-1937] & & & & & & & & \\\\\n[BBOX-1938] & & & & & & & & \\\\\n[BBOX-1939] & & & & & & & & \\\\\n[BBOX-1940] & & & & & & & & \\\\\n[BBOX-1941] & & & & & & & & \\\\\n[BBOX-1942] & & & & & & & & \\\\\n[BBOX-1943] & & & & & & & & \\\\\n[BBOX-1944] & & & & & & & & \\\\\n[BBOX-1945] & & & & & & & & \\\\\n[BBOX-1946] & & & & & & & & \\\\\n[BBOX-1947] & & & & & & & & \\\\\n[BBOX-1948] & & & & & & & & \\\\\n[BBOX-1949] & & & & & & & & \\\\\n[BBOX-1950] & & & & & & & & \\\\\n[BBOX-1951] & & & & & & & & \\\\\n[BBOX-1952] & & & & & & & & \\\\\n[BBOX-1953] & & & & & & & & \\\\\n[BBOX-1954] & & & & & & & & \\\\\n[BBOX-1955] & & & & & & & & \\\\\n[BBOX-1956] & & & & & & & & \\\\\n[BBOX-1957] & & & & & & & & \\\\\n[BBOX-1958] & & & & & & & & \\\\\n[BBOX-1959] & & & & &\n[BBOX-1960] \\begin{tabular}{ccccccccc}\n[BBOX-1961] 报告时间: 2026-03-04\n[BBOX-1962] \\hline\n[BBOX-1963] \\multicolumn{2}{c}{检验项目} & 结果 & 参考范围 & 单位 & \\multicolumn{2}{c}{检验项目} & 结果 & 参考范围 & 单位 \\\\\n[BBOX-1964] \\hline\n[BBOX-1965] *超敏C反应蛋白 & & 1.48 & 0.0~10.0 & mg/L & HCT & *红细胞压积 & 37.70 & 35~45 & \\% \\\\\n[BBOX-1966] WBC & *白细胞 & 4.7 & 3.5~9.5 & 10^9/L & MCV & *红细胞平均体积 & 101.9 & 82.0~100 & fL \\\\\n[BBOX-1967] RBC & *红细胞 & 3.70 & 3.8~5.1 & 10^12/L & MCH & *平均血红蛋白量 & 32.4 & 27.0~34 & pg \\\\\n[BBOX-1968] HGB & *血红蛋白 & 120.0 & 115~150 & g/L & MCHC & *平均血红蛋白浓度 & 318 & 316~354 & g/L \\\\\n[BBOX-1969] PLT & *血小板 & 207.0 & 125~350 & 10^9/L & PCT & 血小板比积 & 0.210 & 0.108~0.272 & \\\\\n[BBOX-1970] NEU & 中性细胞数 & 2.4 & 1.8~6.3 & 10^9/L & MPV & 平均血小板体积 & 9.90 & 9.00~13.00 & fL \\\\\n[BBOX-1971] EOS & 嗜酸性粒细胞 & 0.070 & 0.02~0.52 & 10^9/L & PDW & 血小板分布宽度 & 10.8 & 15.0~18.0 & \\\\\n[BBOX-1972] BASO & 嗜碱性粒细胞 & 0.010 & 0.000~0.06 & 10^9/L & RDW-SD & RBC分布宽度 & 56.80 & 37.00~50.00 & fL \\\\\n[BBOX-1973] LYM & 淋巴细胞数 & 1.54 & 1.1~3.2 & 10^9/L & P-LCR & 大型PLT比率 & 24.20 & 13.00~43.00 & \\% \\\\\n[BBOX-1974] MONO & 单核细胞 & 0.63 & 0.1~0.6 & 10^9/L & 红细胞分布宽度系数 & 15 & & & \\% \\\\\n[BBOX-1975] NEU\\% & 中性细胞比率 & 51.8 & 40~75 & \\% & & & & & \\\\\n[BBOX-1976] LYM\\% & 淋巴细胞比率 & 33 & 20~50 & \\% & & & & & \\\\\n[BBOX-1977] MONO\\% & 单核细胞比率 & 13.5 & 3.0~10 & \\% & & & & & \\\\\n[BBOX-1978] BASO\\% & 嗜碱细胞比率 & 0.2 & 0.0~1.0 & \\% & & & & & \\\\\n[BBOX-1979] EOS\\% & 嗜酸细胞比率 & 1.5 & 0.4~8 & \\% & & & & & \\\\\n[BBOX-1980] \\hline\n[BBOX-1981] \\end{tabular}\n[BBOX-1982] \\begin{tabular}{llll}\n[BBOX-1983] \\hline\n[BBOX-1984] 检验项目 & 结果 & & 提示 \\\\\n[BBOX-1985] \\hline\n[BBOX-1986] 1*癌胚抗原(新仪器) & 23.75 & & $\\uparrow$ \\\\\n[BBOX-1987] 2*糖类抗原125(新仪器) & 240.15 & & $\\uparrow$ \\\\\n[BBOX-1988] 3*糖类抗原153(新仪器) & 16.42 & & \\\\\n[BBOX-1989] 4 细胞角蛋白19片段(新仪器) & 3.39 & & \\\\\n[BBOX-1990] \\hline\n[BBOX-1991] \\end{tabular}"
  }
]
2026-08-10 15:04:48,841 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:04:48.838+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:05:01,326 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:01,352 WARNING  29 [SmartSplitter] Segment 4 type=LabReport bbox_end=1999 out of range (len(sections)=1992), truncated to 1991
2026-08-10 15:05:01,363 WARNING  29 [SmartSplitter] Segment 4 missing first_line: {'type': 'LabReport', 'bbox_start': 194, 'bbox_end': 1999, 'encounter_dates': ['2026-03-04'], 'department': None, 'record_count': 1}
2026-08-10 15:05:01,363 WARNING  29 [SmartSplitter] Segment 5 missing first_line: {'type': 'LabReport', 'bbox_start': 2000, 'bbox_end': 1991, 'encounter_dates': ['2026-03-04'], 'department': None, 'record_count': 1}
2026-08-10 15:05:01,363 INFO     29 [SmartSplitter] No first_line segments located, but 5 chunks already created via bbox_id.
2026-08-10 15:05:01,371 INFO     29 [SmartSplitter] SmartSplitter done: 5 chunks from 6 LLM segments (5 bbox_id, 0 first_line). Types: {'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 2, 'LabReport': 1}
2026-08-10 15:05:01,383 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 15:05:01,383 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks": "5 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 2, 'LabReport': 1}"}
2026-08-10 15:05:01,383 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 15:05:01,386 INFO     29 [ChunkRouter] Routed 5 chunks into 4 groups: {'chunks_Admission': 1, 'chunks_Discharge': 1, 'chunks_Examination': 2, 'chunks_LabExam': 1}
2026-08-10 15:05:01,398 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 15:05:01,398 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks": "5 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 2, 'LabReport': 1}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:05:01,398 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 15:05:01,409 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:05:01,409 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:05:01,410 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[6, 7, 8]
2026-08-10 15:05:01,410 INFO     29 [qwen-vl-table] positions ： [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:05:01,650 INFO     29 [qwen-vl-table] page=6, rect=842x595, img=(2339x1653)
2026-08-10 15:05:01,866 INFO     29 [qwen-vl-table] page=7, rect=842x595, img=(2339x1653)
2026-08-10 15:05:02,061 INFO     29 [qwen-vl-table] page=8, rect=842x595, img=(2339x1653)
2026-08-10 15:05:02,064 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:02,064 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 194, \"bbox_end\": 1999, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-03-04\n\\hline\n& & & & & & & & \\\\\n\\hline\n1 & ALT & *谷丙转氨酶 & 26.0 & 0~40.0 & U/L & 24 LDH & *乳酸脱氢酶 & 217 \\\\\n2 & AST & *谷草转氨酶 & 35.0 & 0~40.0 & U/L & 25 MYO & 肌红蛋白 & 45 \\\\\n3 & AST/ALT & 谷草谷丙比 & 1.35 & 0.80~1.68 & & 26 K & *钾 & 4.25 \\\\\n4 & GGT & *谷氨酰氨基转 & 52.0 & ↑0.0~50.0 & U/L & 27 Na & *钠 & 141.0 \\\\\n5 & TP & *总蛋白 & 69.5 & 60~83 & g/L & 28 CL & *氯 & 102.0 \\\\\n6 & ALB & *白蛋白 & 42.4 & 35~55.0 & g/L & 29 Ca & *钙 & 2.51 \\\\\n7 & GLD & 球蛋白 & 27.1 & 20.0~35.0 & g/L & & & \\\\\n8 & A/G & 白/球蛋白 & 1.56 & 1.00~2.50 & & & & \\\\\n9 & TBA & 总胆汁酸 & 2.8 & 0.0~12.0 & umol/L & & & \\\\\n10 & TBIL & *总胆红素 & 7.4 & 3.4~17.1 & umol/L & & & \\\\\n11 & DBIL & *直接胆红素 & 1.9 & 0.0~7.1 & umol/L & & & \\\\\n12 & IBIL & 间接胆红素 & 5.5 & 0.0~16.0 & umol/L & & & \\\\\n13 & *尿素氮 & & 4.04 & 2.90~7.10 & mmol/L & & & \\\\\n14 & *肌酐 & & 66.0 & 40~79.6 & umol/L & & & \\\\\n15 & UA & *尿酸 & 314.7 & 90.0~423.0 & umol/L & & & \\\\\n16 & GLU & *葡萄糖 & 5.60 & 3.90~6.10 & mmol/L & & & \\\\\n17 & TG & *甘油三酯 & 3.18 & ↑0.23~1.69 & mmol/L & & & \\\\\n18 & CHOL & *总胆固醇 & 7.37 & ↑2.8~5.50 & mmol/L & & & \\\\\n19 & *低密度脂蛋白胆固醇 & & 5.30 & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\",
    "role": "user"
  }
]
2026-08-10 15:05:18,437 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:18,437 INFO     29 [qwen-vl-table] page=6 LLM output (len=4160):
{
  "report_date": "2026-03-04",
  "items": [
    {
      "name": "谷丙转氨酶",
      "item_code": "ALT",
      "value": "26.0",
      "unit": "U/L",
      "reference_range": "0~40.0",
      "abnormal": false
    },
    {
      "name": "谷草转氨酶",
      "item_code": "AST",
      "value": "35.0",
      "unit": "U/L",
      "reference_range": "0~40.0",
      "abnormal": false
    },
    {
      "name": "谷草谷丙比",
      "item_code": "AST/ALT",
      "value": "1.35",
      "unit": null,
      "reference_range": "0.80~1.68",
      "abnormal": false
    },
    {
      "name": "谷氨酰氨基转",
      "item_code": "GGT",
      "value": "52.0",
      "unit": "U/L",
      "reference_range": "0.0~50.0",
      "abnormal": true
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "69.5",
      "unit": "g/L",
      "reference_range": "60~83",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "42.4",
      "unit": "g/L",
      "reference_range": "35~55.0",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLD",
      "value": "27.1",
      "unit": "g/L",
      "reference_range": "20.0~35.0",
      "abnormal": false
    },
    {
      "name": "白/球蛋白",
      "item_code": "A/G",
      "value": "1.56",
      "unit": null,
      "reference_range": "1.00~2.50",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": "TBA",
      "value": "2.8",
      "unit": "umol/L",
      "reference_range": "0.0~12.0",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "7.4",
      "unit": "umol/L",
      "reference_range": "3.4~17.1",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "1.9",
      "unit": "umol/L",
      "reference_range": "0.0~7.1",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "5.5",
      "unit": "umol/L",
      "reference_range": "0.0~16.0",
      "abnormal": false
    },
    {
      "name": "尿素氮",
      "item_code": null,
      "value": "4.04",
      "unit": "mmol/L",
      "reference_range": "2.90~7.10",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": null,
      "value": "66.0",
      "unit": "umol/L",
      "reference_range": "40~79.6",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "UA",
      "value": "314.7",
      "unit": "umol/L",
      "reference_range": "90.0~423.0",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "5.60",
      "unit": "mmol/L",
      "reference_range": "3.90~6.10",
      "abnormal": false
    },
    {
      "name": "甘油三酯",
      "item_code": "TG",
      "value": "3.18",
      "unit": "mmol/L",
      "reference_range": "0.23~1.69",
      "abnormal": true
    },
    {
      "name": "总胆固醇",
      "item_code": "CHOL",
      "value": "7.37",
      "unit": "mmol/L",
      "reference_range": "2.8~5.50",
      "abnormal": true
    },
    {
      "name": "低密度脂蛋白胆固醇",
      "item_code": null,
      "value": "5.30",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": "LDH",
      "value": "217",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "肌红蛋白",
      "item_code": "MYO",
      "value": "45",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "4.25",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "Na",
      "value": "141.0",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "CL",
      "value": "102.0",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "钙",
      "item_code": "Ca",
      "value": "2.51",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 15:05:18,438 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:18,439 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 194, \"bbox_end\": 1999, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\",
    "role": "user"
  }
]
2026-08-10 15:05:20,750 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:05:20.749+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:05:20,881 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:20,882 INFO     29 [qwen-vl-table] page=7 LLM output (len=40):
{
  "report_date": null,
  "items": []
}
2026-08-10 15:05:20,882 WARNING  29 [qwen-vl-table] page=7 no items extracted
2026-08-10 15:05:20,883 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:20,884 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 194, \"bbox_end\": 1999, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & & & & & \\\\\n& & & & &\n\\begin{tabular}{ccccccccc}\n报告时间: 2026-03-04\n\\hline\n\\multicolumn{2}{c}{检验项目} & 结果 & 参考范围 & 单位 & \\multicolumn{2}{c}{检验项目} & 结果 & 参考范围 & 单位 \\\\\n\\hline\n*超敏C反应蛋白 & & 1.48 & 0.0~10.0 & mg/L & HCT & *红细胞压积 & 37.70 & 35~45 & \\% \\\\\nWBC & *白细胞 & 4.7 & 3.5~9.5 & 10^9/L & MCV & *红细胞平均体积 & 101.9 & 82.0~100 & fL \\\\\nRBC & *红细胞 & 3.70 & 3.8~5.1 & 10^12/L & MCH & *平均血红蛋白量 & 32.4 & 27.0~34 & pg \\\\\nHGB & *血红蛋白 & 120.0 & 115~150 & g/L & MCHC & *平均血红蛋白浓度 & 318 & 316~354 & g/L \\\\\nPLT & *血小板 & 207.0 & 125~350 & 10^9/L & PCT & 血小板比积 & 0.210 & 0.108~0.272 & \\\\\nNEU & 中性细胞数 & 2.4 & 1.8~6.3 & 10^9/L & MPV & 平均血小板体积 & 9.90 & 9.00~13.00 & fL \\\\\nEOS & 嗜酸性粒细胞 & 0.070 & 0.02~0.52 & 10^9/L & PDW & 血小板分布宽度 & 10.8 & 15.0~18.0 & \\\\\nBASO & 嗜碱性粒细胞 & 0.010 & 0.000~0.06 & 10^9/L & RDW-SD & RBC分布宽度 & 56.80 & 37.00~50.00 & fL \\\\\nLYM & 淋巴细胞数 & 1.54 & 1.1~3.2 & 10^9/L & P-LCR & 大型PLT比率 & 24.20 & 13.00~43.00 & \\% \\\\\nMONO & 单核细胞 & 0.63 & 0.1~0.6 & 10^9/L & 红细胞分布宽度系数 & 15 & & & \\% \\\\\nNEU\\% & 中性细胞比率 & 51.8 & 40~75 & \\% & & & & & \\\\\nLYM\\% & 淋巴细胞比率 & 33 & 20~50 & \\% & & & & & \\\\\nMONO\\% & 单核细胞比率 & 13.5 & 3.0~10 & \\% & & & & & \\\\\nBASO\\% & 嗜碱细胞比率 & 0.2 & 0.0~1.0 & \\% & & & & & \\\\\nEOS\\% & 嗜酸细胞比率 & 1.5 & 0.4~8 & \\% & & & & & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{llll}\n\\hline\n检验项目 & 结果 & & 提示 \\\\\n\\hline\n1*癌胚抗原(新仪器) & 23.75 & & $\\uparrow$ \\\\\n2*糖类抗原125(新仪器) & 240.15 & & $\\uparrow$ \\\\\n3*糖类抗原153(新仪器) & 16.42 & & \\\\\n4 细胞角蛋白19片段(新仪器) & 3.39 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:05:41,737 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:41,737 INFO     29 [qwen-vl-table] page=8 LLM output (len=4906):
{
  "report_date": "2026-03-04",
  "items": [
    {
      "name": "超敏C反应蛋白",
      "item_code": null,
      "value": "1.48",
      "unit": "mg/L",
      "reference_range": "0.0~10.0",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "4.7",
      "unit": "10^9/L",
      "reference_range": "3.5~9.5",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "3.70",
      "unit": "10^12/L",
      "reference_range": "3.8~5.1",
      "abnormal": true
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "120.0",
      "unit": "g/L",
      "reference_range": "115~150",
      "abnormal": false
    },
    {
      "name": "血小板",
      "item_code": "PLT",
      "value": "207.0",
      "unit": "10^9/L",
      "reference_range": "125~350",
      "abnormal": false
    },
    {
      "name": "中性细胞数",
      "item_code": "NEU",
      "value": "2.4",
      "unit": "10^9/L",
      "reference_range": "1.8~6.3",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞",
      "item_code": "EOS",
      "value": "0.070",
      "unit": "10^9/L",
      "reference_range": "0.02~0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞",
      "item_code": "BASO",
      "value": "0.010",
      "unit": "10^9/L",
      "reference_range": "0.000~0.06",
      "abnormal": false
    },
    {
      "name": "淋巴细胞数",
      "item_code": "LYM",
      "value": "1.54",
      "unit": "10^9/L",
      "reference_range": "1.1~3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞",
      "item_code": "MONO",
      "value": "0.63",
      "unit": "10^9/L",
      "reference_range": "0.1~0.6",
      "abnormal": true
    },
    {
      "name": "中性细胞比率",
      "item_code": "NEU%",
      "value": "51.8",
      "unit": "%",
      "reference_range": "40~75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞比率",
      "item_code": "LYM%",
      "value": "33",
      "unit": "%",
      "reference_range": "20~50",
      "abnormal": false
    },
    {
      "name": "单核细胞比率",
      "item_code": "MONO%",
      "value": "13.5",
      "unit": "%",
      "reference_range": "3.0~10",
      "abnormal": true
    },
    {
      "name": "嗜碱细胞比率",
      "item_code": "BASO%",
      "value": "0.2",
      "unit": "%",
      "reference_range": "0.0~1.0",
      "abnormal": false
    },
    {
      "name": "嗜酸细胞比率",
      "item_code": "EOS%",
      "value": "1.5",
      "unit": "%",
      "reference_range": "0.4~8",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "37.70",
      "unit": "%",
      "reference_range": "35~45",
      "abnormal": false
    },
    {
      "name": "红细胞平均体积",
      "item_code": "MCV",
      "value": "101.9",
      "unit": "fL",
      "reference_range": "82.0~100",
      "abnormal": true
    },
    {
      "name": "平均血红蛋白量",
      "item_code": "MCH",
      "value": "32.4",
      "unit": "pg",
      "reference_range": "27.0~34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": "MCHC",
      "value": "318",
      "unit": "g/L",
      "reference_range": "316~354",
      "abnormal": false
    },
    {
      "name": "血小板比积",
      "item_code": "PCT",
      "value": "0.210",
      "unit": null,
      "reference_range": "0.108~0.272",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "9.90",
      "unit": "fL",
      "reference_range": "9.00~13.00",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "10.8",
      "unit": null,
      "reference_range": "15.0~18.0",
      "abnormal": true
    },
    {
      "name": "RBC分布宽度",
      "item_code": "RDW-SD",
      "value": "56.80",
      "unit": "fL",
      "reference_range": "37.00~50.00",
      "abnormal": true
    },
    {
      "name": "大型PLT比率",
      "item_code": "P-LCR",
      "value": "24.20",
      "unit": "%",
      "reference_range": "13.00~43.00",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度系数",
      "item_code": null,
      "value": "15",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "癌胚抗原(新仪器)",
      "item_code": null,
      "value": "23.75",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "糖类抗原125(新仪器)",
      "item_code": null,
      "value": "240.15",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "糖类抗原153(新仪器)",
      "item_code": null,
      "value": "16.42",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "细胞角蛋白19片段(新仪器)",
      "item_code": null,
      "value": "3.39",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 15:05:41,738 INFO     29 [qwen-vl-table] coord grouping: {6: 25, 7: 25, 8: 4}
2026-08-10 15:05:41,750 INFO     29 [qwen-vl-table] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5267807, prompt_len=624
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
谷丙转氨酶、谷草转氨酶、谷草谷丙比、谷氨酰氨基转、总蛋白、白蛋白、球蛋白、白/球蛋白、总胆汁酸、总胆红素、直接胆红素、间接胆红素、尿素氮、肌酐、尿酸、葡萄糖、甘油三酯、总胆固醇、低密度脂蛋白胆固醇、乳酸脱氢酶、肌红蛋白、钾、钠、氯、钙

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
2026-08-10 15:05:48,804 INFO     29 [qwen-vl-table] coord API raw response (len=1218):
[
	{"text": "谷丙转氨酶", "bbox": [225, 83, 317, 109]},
	{"text": "谷草转氨酶", "bbox": [225, 111, 317, 137]},
	{"text": "谷草谷丙比", "bbox": [225, 137, 324, 163]},
	{"text": "谷氨酰氨基转", "bbox": [225, 163, 324, 190]},
	{"text": "总蛋白", "bbox": [225, 190, 280, 216]},
	{"text": "白蛋白", "bbox": [225, 216, 280, 243]},
	{"text": "球蛋白", "bbox": [220, 243, 271, 270]},
	{"text": "白/球蛋白", "bbox": [220, 270, 296, 297]},
	{"text": "总胆汁酸", "bbox": [220, 297, 289, 324]},
	{"text": "总胆红素", "bbox": [225, 324, 296, 351]},
	{"text": "直接胆红素", "bbox": [225, 351, 314, 378]},
	{"text": "间接胆红素", "bbox": [225, 378, 305, 405]},
	{"text": "尿素氮", "bbox": [180, 405, 235, 432]},
	{"text": "肌酐", "bbox": [180, 432, 217, 459]},
	{"text": "尿酸", "bbox": [220, 460, 261, 487]},
	{"text": "葡萄糖", "bbox": [220, 487, 278, 514]},
	{"text": "甘油三酯", "bbox": [220, 514, 296, 540]},
	{"text": "总胆固醇", "bbox": [220, 540, 296, 567]},
	{"text": "低密度脂蛋白胆固醇", "bbox": [180, 567, 324, 594]},
	{"text": "乳酸脱氢酶", "bbox": [712, 87, 807, 114]},
	{"text": "肌红蛋白", "bbox": [712, 114, 781, 140]},
	{"text": "钾", "bbox": [712, 140, 738, 167]},
	{"text": "钠", "bbox": [712, 167, 738, 194]},
	{"text": "氯", "bbox": [712, 194, 738, 220]},
	{"text": "钙", "bbox": [712, 220, 738, 247]}
]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord API: raw_items=25, valid_items=25, elapsed=7.1s
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[0]: text=谷丙转氨酶, bbox=[225, 83, 317, 109]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[1]: text=谷草转氨酶, bbox=[225, 111, 317, 137]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[2]: text=谷草谷丙比, bbox=[225, 137, 324, 163]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[3]: text=谷氨酰氨基转, bbox=[225, 163, 324, 190]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[4]: text=总蛋白, bbox=[225, 190, 280, 216]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[5]: text=白蛋白, bbox=[225, 216, 280, 243]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[6]: text=球蛋白, bbox=[220, 243, 271, 270]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[7]: text=白/球蛋白, bbox=[220, 270, 296, 297]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[8]: text=总胆汁酸, bbox=[220, 297, 289, 324]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[9]: text=总胆红素, bbox=[225, 324, 296, 351]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[10]: text=直接胆红素, bbox=[225, 351, 314, 378]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[11]: text=间接胆红素, bbox=[225, 378, 305, 405]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[12]: text=尿素氮, bbox=[180, 405, 235, 432]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[13]: text=肌酐, bbox=[180, 432, 217, 459]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[14]: text=尿酸, bbox=[220, 460, 261, 487]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[15]: text=葡萄糖, bbox=[220, 487, 278, 514]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[16]: text=甘油三酯, bbox=[220, 514, 296, 540]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[17]: text=总胆固醇, bbox=[220, 540, 296, 567]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[18]: text=低密度脂蛋白胆固醇, bbox=[180, 567, 324, 594]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[19]: text=乳酸脱氢酶, bbox=[712, 87, 807, 114]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[20]: text=肌红蛋白, bbox=[712, 114, 781, 140]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[21]: text=钾, bbox=[712, 140, 738, 167]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[22]: text=钠, bbox=[712, 167, 738, 194]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[23]: text=氯, bbox=[712, 194, 738, 220]
2026-08-10 15:05:48,805 INFO     29 [qwen-vl-table] coord item[24]: text=钙, bbox=[712, 220, 738, 247]
2026-08-10 15:05:48,806 INFO     29 [qwen-vl-table] page=6 coord: matched 25/25, time=7.1s
2026-08-10 15:05:48,814 INFO     29 [qwen-vl-table] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4777327, prompt_len=676
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
超敏C反应蛋白、白细胞、红细胞、血红蛋白、血小板、中性细胞数、嗜酸性粒细胞、嗜碱性粒细胞、淋巴细胞数、单核细胞、中性细胞比率、淋巴细胞比率、单核细胞比率、嗜碱细胞比率、嗜酸细胞比率、红细胞压积、红细胞平均体积、平均血红蛋白量、平均血红蛋白浓度、血小板比积、平均血小板体积、血小板分布宽度、RBC分布宽度、大型PLT比率、红细胞分布宽度系数

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
2026-08-10 15:05:55,825 INFO     29 [qwen-vl-table] coord API raw response (len=1271):
[
	{"text": "超敏C反应蛋白", "bbox": [77, 205, 177, 230]},
	{"text": "白细胞", "bbox": [111, 232, 164, 255]},
	{"text": "红细胞", "bbox": [111, 257, 164, 280]},
	{"text": "血红蛋白", "bbox": [111, 282, 177, 305]},
	{"text": "血小板", "bbox": [111, 308, 164, 331]},
	{"text": "中性细胞数", "bbox": [111, 333, 185, 356]},
	{"text": "嗜酸性粒细胞", "bbox": [111, 358, 200, 381]},
	{"text": "嗜碱性粒细胞", "bbox": [111, 383, 200, 406]},
	{"text": "淋巴细胞数", "bbox": [111, 408, 185, 431]},
	{"text": "单核细胞", "bbox": [111, 433, 171, 456]},
	{"text": "中性细胞比率", "bbox": [111, 458, 200, 481]},
	{"text": "淋巴细胞比率", "bbox": [111, 483, 200, 506]},
	{"text": "单核细胞比率", "bbox": [111, 508, 200, 531]},
	{"text": "嗜碱细胞比率", "bbox": [111, 533, 200, 556]},
	{"text": "嗜酸细胞比率", "bbox": [111, 558, 200, 581]},
	{"text": "红细胞压积", "bbox": [529, 205, 611, 230]},
	{"text": "红细胞平均体积", "bbox": [524, 232, 633, 255]},
	{"text": "平均血红蛋白量", "bbox": [524, 257, 633, 280]},
	{"text": "平均血红蛋白浓度", "bbox": [524, 282, 655, 305]},
	{"text": "血小板比积", "bbox": [529, 308, 604, 331]},
	{"text": "平均血小板体积", "bbox": [524, 333, 625, 356]},
	{"text": "血小板分布宽度", "bbox": [530, 358, 633, 381]},
	{"text": "RBC分布宽度", "bbox": [518, 383, 625, 406]},
	{"text": "大型PLT比率", "bbox": [530, 408, 618, 431]},
	{"text": "红细胞分布宽度系数", "bbox": [494, 433, 625, 456]}
]
2026-08-10 15:05:55,826 INFO     29 [qwen-vl-table] coord API: raw_items=25, valid_items=25, elapsed=7.0s
2026-08-10 15:05:55,826 INFO     29 [qwen-vl-table] coord item[0]: text=超敏C反应蛋白, bbox=[77, 205, 177, 230]
2026-08-10 15:05:55,826 INFO     29 [qwen-vl-table] coord item[1]: text=白细胞, bbox=[111, 232, 164, 255]
2026-08-10 15:05:55,826 INFO     29 [qwen-vl-table] coord item[2]: text=红细胞, bbox=[111, 257, 164, 280]
2026-08-10 15:05:55,826 INFO     29 [qwen-vl-table] coord item[3]: text=血红蛋白, bbox=[111, 282, 177, 305]
2026-08-10 15:05:55,826 INFO     29 [qwen-vl-table] coord item[4]: text=血小板, bbox=[111, 308, 164, 331]
2026-08-10 15:05:55,826 INFO     29 [qwen-vl-table] coord item[5]: text=中性细胞数, bbox=[111, 333, 185, 356]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[6]: text=嗜酸性粒细胞, bbox=[111, 358, 200, 381]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[7]: text=嗜碱性粒细胞, bbox=[111, 383, 200, 406]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[8]: text=淋巴细胞数, bbox=[111, 408, 185, 431]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[9]: text=单核细胞, bbox=[111, 433, 171, 456]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[10]: text=中性细胞比率, bbox=[111, 458, 200, 481]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[11]: text=淋巴细胞比率, bbox=[111, 483, 200, 506]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[12]: text=单核细胞比率, bbox=[111, 508, 200, 531]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[13]: text=嗜碱细胞比率, bbox=[111, 533, 200, 556]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[14]: text=嗜酸细胞比率, bbox=[111, 558, 200, 581]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[15]: text=红细胞压积, bbox=[529, 205, 611, 230]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[16]: text=红细胞平均体积, bbox=[524, 232, 633, 255]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[17]: text=平均血红蛋白量, bbox=[524, 257, 633, 280]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[18]: text=平均血红蛋白浓度, bbox=[524, 282, 655, 305]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[19]: text=血小板比积, bbox=[529, 308, 604, 331]
2026-08-10 15:05:55,827 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板体积, bbox=[524, 333, 625, 356]
2026-08-10 15:05:55,828 INFO     29 [qwen-vl-table] coord item[21]: text=血小板分布宽度, bbox=[530, 358, 633, 381]
2026-08-10 15:05:55,828 INFO     29 [qwen-vl-table] coord item[22]: text=RBC分布宽度, bbox=[518, 383, 625, 406]
2026-08-10 15:05:55,828 INFO     29 [qwen-vl-table] coord item[23]: text=大型PLT比率, bbox=[530, 408, 618, 431]
2026-08-10 15:05:55,828 INFO     29 [qwen-vl-table] coord item[24]: text=红细胞分布宽度系数, bbox=[494, 433, 625, 456]
2026-08-10 15:05:55,830 INFO     29 [qwen-vl-table] page=7 coord: matched 25/25, time=7.0s
2026-08-10 15:05:55,839 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3503524, prompt_len=557
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
癌胚抗原(新仪器)、糖类抗原125(新仪器)、糖类抗原153(新仪器)、细胞角蛋白19片段(新仪器)

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
2026-08-10 15:05:58,133 INFO     29 [qwen-vl-table] coord API raw response (len=225):
[
	{"text": "癌胚抗原(新仪器)", "bbox": [52, 212, 284, 256]},
	{"text": "糖类抗原125(新仪器)", "bbox": [52, 270, 351, 313]},
	{"text": "糖类抗原153(新仪器)", "bbox": [52, 331, 331, 374]},
	{"text": "细胞角蛋白19片段(新仪器)", "bbox": [36, 391, 408, 434]}
]
2026-08-10 15:05:58,133 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=2.3s
2026-08-10 15:05:58,133 INFO     29 [qwen-vl-table] coord item[0]: text=癌胚抗原(新仪器), bbox=[52, 212, 284, 256]
2026-08-10 15:05:58,133 INFO     29 [qwen-vl-table] coord item[1]: text=糖类抗原125(新仪器), bbox=[52, 270, 351, 313]
2026-08-10 15:05:58,134 INFO     29 [qwen-vl-table] coord item[2]: text=糖类抗原153(新仪器), bbox=[52, 331, 331, 374]
2026-08-10 15:05:58,134 INFO     29 [qwen-vl-table] coord item[3]: text=细胞角蛋白19片段(新仪器), bbox=[36, 391, 408, 434]
2026-08-10 15:05:58,135 INFO     29 [qwen-vl-table] page=8 coord: matched 4/4, time=2.3s
2026-08-10 15:05:58,136 INFO     29 [qwen-vl-table] new_positions (54):
[[7, 189.45, 266.914, 49.385, 64.855], [7, 189.45, 266.914, 66.045, 81.515], [7, 189.45, 272.808, 81.515, 96.985], [7, 189.45, 272.808, 96.985, 113.05], [7, 189.45, 235.76, 113.05, 128.51999999999998], [7, 189.45, 235.76, 128.51999999999998, 144.58499999999998], [7, 185.23999999999998, 228.182, 144.58499999999998, 160.65], [7, 185.23999999999998, 249.232, 160.65, 176.715], [7, 185.23999999999998, 243.338, 176.715, 192.78], [7, 189.45, 249.232, 192.78, 208.845], [7, 189.45, 264.388, 208.845, 224.91], [7, 189.45, 256.81, 224.91, 240.975], [7, 151.56, 197.87, 240.975, 257.03999999999996], [7, 151.56, 182.714, 257.03999999999996, 273.10499999999996], [7, 185.23999999999998, 219.762, 273.7, 289.765], [7, 185.23999999999998, 234.076, 289.765, 305.83], [7, 185.23999999999998, 249.232, 305.83, 321.3], [7, 185.23999999999998, 249.232, 321.3, 337.365], [7, 151.56, 272.808, 337.365, 353.43], [7, 599.504, 679.494, 51.765, 67.83], [7, 599.504, 657.602, 67.83, 83.3], [7, 599.504, 621.396, 83.3, 99.365], [7, 599.504, 621.396, 99.365, 115.42999999999999], [7, 599.504, 621.396, 115.42999999999999, 130.9], [7, 599.504, 621.396, 130.9, 146.965], [8, 64.834, 149.034, 121.975, 136.85], [8, 93.462, 138.088, 138.04, 151.725], [8, 93.462, 138.088, 152.915, 166.6], [8, 93.462, 149.034, 167.79, 181.475], [8, 93.462, 138.088, 183.26, 196.945], [8, 93.462, 155.76999999999998, 198.135, 211.82], [8, 93.462, 168.4, 213.01, 226.695], [8, 93.462, 168.4, 227.885, 241.57], [8, 93.462, 155.76999999999998, 242.76, 256.445], [8, 93.462, 143.982, 257.635, 271.32], [8, 93.462, 168.4, 272.51, 286.195], [8, 93.462, 168.4, 287.385, 301.07], [8, 93.462, 168.4, 302.26, 315.945], [8, 93.462, 168.4, 317.135, 330.82], [8, 93.462, 168.4, 332.01, 345.695], [8, 445.418, 514.462, 121.975, 136.85], [8, 441.20799999999997, 532.986, 138.04, 151.725], [8, 441.20799999999997, 532.986, 152.915, 166.6], [8, 441.20799999999997, 551.51, 167.79, 181.475], [8, 445.418, 508.568, 183.26, 196.945], [8, 441.20799999999997, 526.25, 198.135, 211.82], [8, 446.26, 532.986, 213.01, 226.695], [8, 436.156, 526.25, 227.885, 241.57], [8, 446.26, 520.356, 242.76, 256.445], [8, 415.948, 526.25, 257.635, 271.32], [9, 43.784, 239.128, 126.14, 152.32], [9, 43.784, 295.542, 160.65, 186.23499999999999], [9, 43.784, 278.702, 196.945, 222.53], [9, 30.311999999999998, 343.536, 232.64499999999998, 258.22999999999996]]
2026-08-10 15:05:58,136 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=54, matched=54, pages=3, time=56.7s
2026-08-10 15:05:58,212 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 15:05:58,212 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:05:58,212 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 15:05:58,213 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:05:58.212+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:05:58,230 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:58,230 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:05:58,925 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:58,933 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 15:05:58,933 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:05:58,933 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 15:05:58,942 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:58,942 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:05:59,492 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:59,497 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 15:05:59,498 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:05:59,498 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 15:05:59,504 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:05:59,505 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:06:00,174 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:06:00,185 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 15:06:00,185 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:06:00,186 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 15:06:00,193 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:06:00,193 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:06:00,610 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:06:00,619 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 15:06:00,620 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:06:00,620 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 15:06:00,630 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:06:00,631 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:06:00,632 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:06:00,632 INFO     29 [qwen-vl-text] positions(29): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:06:00,632 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [28, 1]
2026-08-10 15:06:00,925 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:06:01,112 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:06:01,112 INFO     29 [qwen-vl-text] LLM extraction start, text_len=957
2026-08-10 15:06:01,113 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:06:01,113 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 104, \"bbox_end\": 132, \"encounter_dates\": [\"2026-03-04\", \"2026-03-07\"], \"department\": \"肿瘤内科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "入院时间:2026年03月04日09时20分 出院时间:2026年03月07日10时00分 住院天数:3天\nX线号:-\nCT号:-\nMRI号:-\n入院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸\n腔积液 4.肺部感染?\n入院情况:确诊肺腺癌8个月余。体格检查:四测正常,神志清楚,自动体位,慢性病容。皮肤\n巩膜无黄染,全身未扪及明显肿大淋巴结,气管居中。颈软,胸廓对称,双肺语颤正常,叩诊双肺呈\n清音,听诊双肺呼吸音低,未闻及明显罗音。心音清晰,心律齐无杂音。腹平软,全腹无压痛反跳\n痛,肝脾肋下未扪及,肝肾区无叩痛,移动性浊音阴性,肠鸣音正常。双下肢无浮肿。四肢肌力、肌\n张力正常。生理反射正常,病理征阴性。\n诊治经过:完善相关检查:CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器)\n23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇\n7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。胸部平扫:与2026.02.08日老片\n相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,\n余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧\n胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。评估为PD,部分进展,与家属商榷后于3月6\n日继续予以贝伐珠单抗联合PCb化疗联合治疗(贝伐珠单抗800mg+培美曲塞860mg+卡铂\n600mg),现治疗完成予以办理出院。\n出院情况:患者偶有干咳。\n出院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸\n腔积液\n出院医嘱:1、注意休息,加强营养,多饮白开水。\n2、定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复\n查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射\n200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,\n遵医嘱用药;\n3、院外巩固治疗,不适随诊。\n11:25",
    "role": "user"
  }
]
2026-08-10 15:06:13,494 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:06:13,494 INFO     29 [qwen-vl-text] LLM output (len=2421):
{
  "encounter_date": "2026-03-07",
  "admission_date": "2026-03-04",
  "discharge_date": "2026-03-07",
  "hospital_days": 3,
  "department": "肿瘤内科",
  "bed_number": null,
  "admission_condition": "确诊肺腺癌8个月余。体格检查:四测正常,神志清楚,自动体位,慢性病容。皮肤巩膜无黄染,全身未扪及明显肿大淋巴结,气管居中。颈软,胸廓对称,双肺语颤正常,叩诊双肺呈清音,听诊双肺呼吸音低,未闻及明显罗音。心音清晰,心律齐无杂音。腹平软,全腹无压痛反跳痛,肝脾肋下未扪及,肝肾区无叩痛,移动性浊音阴性,肠鸣音正常。双下肢无浮肿。四肢肌力、肌张力正常。生理反射正常,病理征阴性。",
  "admission_diagnoses": [
    {
      "name": "原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移",
      "diagnosis_type": "西医"
    },
    {
      "name": "心包积液",
      "diagnosis_type": "西医"
    },
    {
      "name": "胸腔积液",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺部感染?",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "完善相关检查:CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器) 23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇 7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。胸部平扫:与2026.02.08日老片相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。评估为PD,部分进展,与家属商榷后于3月6日继续予以贝伐珠单抗联合PCb化疗联合治疗(贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg),现治疗完成予以办理出院。",
  "auxiliary_exams": "CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器) 23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇 7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。",
  "imaging_findings": "胸部平扫:与2026.02.08日老片相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。",
  "discharge_diagnoses": [
    {
      "name": "原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移",
      "diagnosis_type": "西医"
    },
    {
      "name": "心包积液",
      "diagnosis_type": "西医"
    },
    {
      "name": "胸腔积液",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者偶有干咳。",
  "outcome": null,
  "discharge_orders": "1、注意休息,加强营养,多饮白开水。\n2、定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,遵医嘱用药;\n3、院外巩固治疗,不适随诊。",
  "do_medications": [],
  "do_follow_up": "定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,遵医嘱用药;院外巩固治疗,不适随诊。",
  "do_precautions": [
    "注意休息,加强营养,多饮白开水。"
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
2026-08-10 15:06:13,494 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-07]
2026-08-10 15:06:13,500 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1845039, prompt_len=1648
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["入院时间:2026年03月04日09时20分 出院时间:2026年03月07日10时00分 住院天数:3天", "X线号:-", "CT号:-", "MRI号:-", "入院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸", "腔积液 4.肺部感染?", "入院情况:确诊肺腺癌8个月余。体格检查:四测正常,神志清楚,自动体位,慢性病容。皮肤", "巩膜无黄染,全身未扪及明显肿大淋巴结,气管居中。颈软,胸廓对称,双肺语颤正常,叩诊双肺呈", "清音,听诊双肺呼吸音低,未闻及明显罗音。心音清晰,心律齐无杂音。腹平软,全腹无压痛反跳", "痛,肝脾肋下未扪及,肝肾区无叩痛,移动性浊音阴性,肠鸣音正常。双下肢无浮肿。四肢肌力、肌", "张力正常。生理反射正常,病理征阴性。", "诊治经过:完善相关检查:CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器)", "23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇", "7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。胸部平扫:与2026.02.08日老片", "相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,", "余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧", "胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。评估为PD,部分进展,与家属商榷后于3月6", "日继续予以贝伐珠单抗联合PCb化疗联合治疗(贝伐珠单抗800mg+培美曲塞860mg+卡铂", "600mg),现治疗完成予以办理出院。", "出院情况:患者偶有干咳。", "出院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸", "腔积液", "出院医嘱:1、注意休息,加强营养,多饮白开水。", "2、定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复", "查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射", "200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,", "遵医嘱用药;", "3、院外巩固治疗,不适随诊。"]

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
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord API raw response (len=2186):
[
	{"text": "入院时间:2026年03月04日09时20分 出院时间:2026年03月07日10时00分 住院天数:3天", "bbox": [100, 174, 858, 193]},
	{"text": "X线号:-", "bbox": [100, 197, 168, 212]},
	{"text": "CT号:-", "bbox": [233, 197, 295, 212]},
	{"text": "MRI号:-", "bbox": [322, 197, 394, 212]},
	{"text": "入院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸", "bbox": [100, 216, 909, 234]},
	{"text": "腔积液 4.肺部感染?", "bbox": [100, 238, 275, 253]},
	{"text": "入院情况:确诊肺腺癌8个月余。体格检查:四测正常,神志清楚,自动体位,慢性病容。皮肤", "bbox": [100, 257, 910, 274]},
	{"text": "巩膜无黄染,全身未扪及明显肿大淋巴结,气管居中。颈软,胸廓对称,双肺语颤正常,叩诊双肺呈", "bbox": [100, 278, 909, 294]},
	{"text": "清音,听诊双肺呼吸音低,未闻及明显罗音。心音清晰,心律齐无杂音。腹平软,全腹无压痛反跳", "bbox": [100, 298, 910, 314]},
	{"text": "痛,肝脾肋下未扪及,肝肾区无叩痛,移动性浊音阴性,肠鸣音正常。双下肢无浮肿。四肢肌力、肌", "bbox": [100, 318, 910, 334]},
	{"text": "张力正常。生理反射正常,病理征阴性。", "bbox": [100, 339, 422, 355]},
	{"text": "诊治经过:完善相关检查:CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器)", "bbox": [140, 360, 896, 375]},
	{"text": "23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇", "bbox": [100, 380, 902, 396]},
	{"text": "7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。胸部平扫:与2026.02.08日老片", "bbox": [100, 400, 909, 416]},
	{"text": "相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,", "bbox": [100, 420, 908, 437]},
	{"text": "余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧", "bbox": [100, 440, 908, 457]},
	{"text": "胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。评估为PD,部分进展,与家属商榷后于3月6", "bbox": [100, 460, 909, 477]},
	{"text": "日继续予以贝伐珠单抗联合PCb化疗联合治疗(贝伐珠单抗800mg+培美曲塞860mg+卡铂", "bbox": [100, 480, 908, 497]},
	{"text": "600mg),现治疗完成予以办理出院。", "bbox": [100, 500, 405, 517]},
	{"text": "出院情况:患者偶有干咳。", "bbox": [141, 521, 356, 537]},
	{"text": "出院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸", "bbox": [141, 541, 909, 558]},
	{"text": "腔积液", "bbox": [100, 561, 159, 577]},
	{"text": "出院医嘱:1、注意休息,加强营养,多饮白开水。", "bbox": [141, 581, 531, 598]},
	{"text": "2、定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复", "bbox": [227, 602, 909, 618]},
	{"text": "查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射", "bbox": [100, 622, 899, 638]},
	{"text": "200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,", "bbox": [100, 642, 907, 659]},
	{"text": "遵医嘱用药;", "bbox": [100, 663, 204, 679]},
	{"text": "3、院外巩固治疗,不适随诊。", "bbox": [227, 683, 464, 699]}
]
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=12.4s
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord item[0]: text=入院时间:2026年03月04日09时20分 出院时间:2026年03月07日10时00分 住院天数:3天, bbox=[100, 174, 858, 193]
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord item[1]: text=X线号:-, bbox=[100, 197, 168, 212]
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord item[2]: text=CT号:-, bbox=[233, 197, 295, 212]
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord item[3]: text=MRI号:-, bbox=[322, 197, 394, 212]
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord item[4]: text=入院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸, bbox=[100, 216, 909, 234]
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord item[5]: text=腔积液 4.肺部感染?, bbox=[100, 238, 275, 253]
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord item[6]: text=入院情况:确诊肺腺癌8个月余。体格检查:四测正常,神志清楚,自动体位,慢性病容。皮肤, bbox=[100, 257, 910, 274]
2026-08-10 15:06:25,860 INFO     29 [qwen-vl-text] coord item[7]: text=巩膜无黄染,全身未扪及明显肿大淋巴结,气管居中。颈软,胸廓对称,双肺语颤正常,叩诊双肺呈, bbox=[100, 278, 909, 294]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[8]: text=清音,听诊双肺呼吸音低,未闻及明显罗音。心音清晰,心律齐无杂音。腹平软,全腹无压痛反跳, bbox=[100, 298, 910, 314]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[9]: text=痛,肝脾肋下未扪及,肝肾区无叩痛,移动性浊音阴性,肠鸣音正常。双下肢无浮肿。四肢肌力、肌, bbox=[100, 318, 910, 334]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[10]: text=张力正常。生理反射正常,病理征阴性。, bbox=[100, 339, 422, 355]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[11]: text=诊治经过:完善相关检查:CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器), bbox=[140, 360, 896, 375]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[12]: text=23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇, bbox=[100, 380, 902, 396]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[13]: text=7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。胸部平扫:与2026.02.08日老片, bbox=[100, 400, 909, 416]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[14]: text=相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,, bbox=[100, 420, 908, 437]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[15]: text=余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧, bbox=[100, 440, 908, 457]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[16]: text=胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。评估为PD,部分进展,与家属商榷后于3月6, bbox=[100, 460, 909, 477]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[17]: text=日继续予以贝伐珠单抗联合PCb化疗联合治疗(贝伐珠单抗800mg+培美曲塞860mg+卡铂, bbox=[100, 480, 908, 497]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[18]: text=600mg),现治疗完成予以办理出院。, bbox=[100, 500, 405, 517]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[19]: text=出院情况:患者偶有干咳。, bbox=[141, 521, 356, 537]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[20]: text=出院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸, bbox=[141, 541, 909, 558]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[21]: text=腔积液, bbox=[100, 561, 159, 577]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[22]: text=出院医嘱:1、注意休息,加强营养,多饮白开水。, bbox=[141, 581, 531, 598]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[23]: text=2、定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复, bbox=[227, 602, 909, 618]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[24]: text=查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射, bbox=[100, 622, 899, 638]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[25]: text=200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,, bbox=[100, 642, 907, 659]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[26]: text=遵医嘱用药;, bbox=[100, 663, 204, 679]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] coord item[27]: text=3、院外巩固治疗,不适随诊。, bbox=[227, 683, 464, 699]
2026-08-10 15:06:25,861 INFO     29 [qwen-vl-text] page=3 — 28/28 coords, api_time=12.4s
2026-08-10 15:06:25,862 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1029259, prompt_len=620
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["11:25"]

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
2026-08-10 15:06:27,376 INFO     29 [qwen-vl-text] coord API raw response (len=62):
```json
[
	{"text": "11:25", "bbox": [273, 26, 339, 44]}
]
```
2026-08-10 15:06:27,376 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 15:06:27,376 INFO     29 [qwen-vl-text] coord item[0]: text=11:25, bbox=[273, 26, 339, 44]
2026-08-10 15:06:27,376 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=1.5s
2026-08-10 15:06:27,377 INFO     29 [qwen-vl-text] new_positions (29):
[[3, 59.5, 510.51, 146.50799999999998, 162.506], [3, 59.5, 99.96, 165.874, 178.504], [3, 138.635, 175.525, 165.874, 178.504], [3, 191.59, 234.42999999999998, 165.874, 178.504], [3, 59.5, 540.855, 181.87199999999999, 197.028], [3, 59.5, 163.625, 200.396, 213.02599999999998], [3, 59.5, 541.4499999999999, 216.394, 230.708], [3, 59.5, 540.855, 234.076, 247.548], [3, 59.5, 541.4499999999999, 250.916, 264.388], [3, 59.5, 541.4499999999999, 267.756, 281.228], [3, 59.5, 251.08999999999997, 285.438, 298.90999999999997], [3, 83.3, 533.12, 303.12, 315.75], [3, 59.5, 536.6899999999999, 319.96, 333.432], [3, 59.5, 540.855, 336.8, 350.272], [3, 59.5, 540.26, 353.64, 367.954], [3, 59.5, 540.26, 370.47999999999996, 384.794], [3, 59.5, 540.855, 387.32, 401.63399999999996], [3, 59.5, 540.26, 404.15999999999997, 418.474], [3, 59.5, 240.975, 421.0, 435.31399999999996], [3, 83.895, 211.82, 438.68199999999996, 452.154], [3, 83.895, 540.855, 455.522, 469.83599999999996], [3, 59.5, 94.60499999999999, 472.36199999999997, 485.834], [3, 83.895, 315.945, 489.202, 503.51599999999996], [3, 135.065, 540.855, 506.88399999999996, 520.356], [3, 59.5, 534.905, 523.7239999999999, 537.196], [3, 59.5, 539.665, 540.564, 554.8779999999999], [3, 59.5, 121.38, 558.246, 571.718], [3, 135.065, 276.08, 575.086, 588.558], [4, 162.435, 201.70499999999998, 21.892, 37.048]]
2026-08-10 15:06:27,377 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=2, time=26.7s
2026-08-10 15:06:27,387 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 15:06:27,388 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:06:27,388 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 15:06:27,393 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:06:27,394 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:06:27,394 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 15:06:27,394 INFO     29 [qwen-vl-text] positions(104): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:06:27,394 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2], lines per page: [46, 40, 18]
2026-08-10 15:06:27,678 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:06:27,967 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:06:28,244 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:06:28,245 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3720
2026-08-10 15:06:28,245 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:06:28,245 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 103, \"encounter_dates\": [\"2026-03-04\"], \"department\": \"肿瘤内科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "姓名：\n性别：女\n年龄：41岁\n婚 姻：已婚\n联系电话：\n出生\n民族：汉族\n职业：职工\n住址\n电子邮件(E_mail)：无\n入院时间：2026年03月04日 09时20分\n记录时间：2026年03月04日 10时56分\n病史陈述者：患者本人\n入院方式：步行\n主诉：确诊肺腺癌8个月余。\n现病史：患者自诉2025年6月开始无明显诱因出现活动后气促，为求治疗在\n就诊，完善检查：（左侧颈部淋巴结）HE结合免疫组化符合转移性腺癌，倾向肺来源可能性大，\n请完善相关检查后综合考虑。IHC：GATA-3(-)，P16(-)，CK7(+)，ER(-).PR(-)，CK20(-)，Pax-\n8(-)，TTF-1(+)，NapsinA(+)，CerbB-2(1+)，Villin(+)，Ki-67(热点区约50%+)。PETCT：1.双肺\n散在斑片影及磨玻璃影，糖代谢增高，双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹\n主动脉旁多发肿大淋巴结，糖代谢增高，脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增\n高，上述考虑恶性肿瘤（肺CA？）并淋巴结、骨转移可能，建议结合病理。2.双侧胸腔积液，双下\n肺膨胀不全。3.心包积液，盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶，糖代谢增高，考虑生\n理性改变。诊断考虑为“左上肺腺癌广泛转移”，行化疗前准备（叶酸+维生素B12），于6月13日\n出院。\n2025年6月14日为求治疗入我科，于6月16日完善基因检测，于6月18日予以PCb+贝伐珠单抗\n联合治疗第1周期（培美曲塞785mg+卡铂600mg+贝伐珠单抗800mg），同时予以护胃、止呕等对症\n治疗，患者治疗完成予以办理出院。\n出院后患者诉气促好转，基因检测报告：BRAF（p.K601E），MET扩增，PDL1 TPS表达55%。\n2025年7月9日再入院，予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂\n650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，于7月12日予以地\n舒单抗120mg护骨治疗，复查血常规正常于7月12日出院。\n出院后患者气促明显缓解，2025年7月30日为求治疗再入院，完善检查：肝肾功能、电解质、\n心肌酶、血常规正常。纵隔及心脏平扫及增强|肺部平扫及增强|上腹部平扫及增强|下腹部平扫\n及增强|盆腔平扫及增强CT：肺部炎症，合并多发占位可能；心包积液；双侧部分肋骨、腰椎多发骨\n质病变，腹膜后多发小淋巴结，结合病史考虑转移。疗效评估为PR，于7月31日、8月23日、9月9日、\n10月02日予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单\n抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，期间规律予以地舒单抗护骨治疗，\n患者治疗完成10月05日出院。\n2025年10月23日为求治疗再入院，完善相关检查：胸部平扫及增强|上腹部平扫及增强|下\n腹部平扫及增强|盆腔平扫及增强：与07-30老片相比：肺部炎症较前吸收，考虑肺内转移病灶，\n较前大致相仿；心包积液，较前稍吸收；双肾结石。双侧部分肋骨、腰椎多发骨质病变，似较前稍微\n增多；腹膜后多发小淋巴结，较前相仿；结合病史考虑转移。评估为SD，继续予以贝伐珠单抗\n800mg+替雷利珠单抗200mg维持治疗，同时予以降血脂治疗，2025年10月25日予以办理出院。\n2025年11月14日、12月4日返院继续治疗，因患者偶有痰中带血，停贝伐珠单抗，予以替雷禾\n第 1 页\n珠单抗200mg维持治疗。\n2025年12月25日为求治疗再入院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部\n平扫及增强|盆腔平扫及增强：与10-23老片相比：肺部炎症较前稍进展，考虑肺内转移病灶，较\n前大致相仿；心包积液，较前稍增多；双肾结石。双侧部分肋骨、腰椎多发骨质病变，较前相仿；腹\n膜后多发小淋巴结，较前稍微增大；左侧腋窝稍大淋巴结；结合病史考虑转移。评估为SD，免疫性\n肺炎不排除，参考中科院专家会诊意见，于2025年12月27日予以贝伐珠单抗联合PCb化疗联合治\n疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成12月\n30日办理出院。\n2026年1月17日为求治疗再入院，完善检查，于2026年1月19日予以贝伐珠单抗联合PCb化疗\n联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完\n成1月20日办理出院。\n2026年2月8日再次返院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增\n强|盆腔平扫及增强CT：与2025-10-23日老片相比：肺部炎症较前增多；肺内多发结节（右下肺\n后基底段新增10mm小结节，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可\n能。心包积液，大致同前；双肾结石。双侧部分肋骨、腰椎、骨盆多发骨质病变，大致同前。本次复查\n增强CT，对比2025-12片，疗效评价SD，建议继续贝伐珠单抗+培美曲塞+卡铂联合治疗，患者因过\n年要求暂缓化疗，于2026-02-12予以贝伐珠单抗800mg靶向治疗。治疗上予以抗感染、清热解毒、\n化痰止咳等对症治疗后于2月14日出院。\n今患者为求继续治疗在我院门诊就诊，门诊以“肺恶性肿瘤”收住我科，此次发病期间，患\n者精神食欲睡眠可，大小便正常，体重无明显变化。\n既往史：个人史、月经及婚育史、家族史见第一次入院记录。\n体格检查\nT：36.5℃ P：85次/分 R：19次/分 BP：100/78mmHg\n发育正常，营养中等，自主体位，神志清楚，查体合作。粘膜无发绀、黄染、苍白，无皮疹。未见\n皮下出血。皮肤湿度正常，弹性正常，无肝掌，未见蜘蛛痣。左侧腋下可触及大小约1*1cm的肿大淋\n巴结，活动度差，质地韧，无明显压痛，边界不清晰。头颅外形正常。眼：眼睑正常，眼球无凸出及\n凹陷，结膜正常。巩膜无黄染，双侧瞳孔等大等圆，瞳孔直径3.0mm，对光反射及调节均灵敏。耳：\n双耳耳廓外形正常，无畸形，双侧无乳突压痛，外耳道通畅，无分泌物。鼻外形正常，鼻中隔无偏\n曲，上颌窦与额窦无压痛，无鼻塞，无分泌物。口腔：口唇红润，伸舌居中，双侧扁桃体无肿大，表\n面未见脓点，咽无充血，声音嘶哑。颈软，无抵抗感，气管居中，颈静脉充盈正常，肝颈静脉回流征\n阴性，颈动脉搏动正常，甲状腺未触及肿大。胸廓正常，肋间隙正常，胸壁无压痛，无胸骨叩痛。呼\n吸节律正常，语颤正常，双肺未触及胸膜摩擦感，未触及皮下捻发感。胸廓对称，双肺语颤正常，叩\n诊双肺呈清音，听诊双肺呼吸音低，未闻及明显罗音。心前区无隆起，可见心尖搏动，心尖搏动位\n于第5肋间左锁骨中线内0.5cm，心前区无异常搏动。心尖搏动触不清，未触及震颤，无心包摩擦\n感。心界不大。心率：85次/分，律齐，心音清。各瓣膜听诊区未闻及病理性杂音，不可闻及额外心\n音，未闻及心包摩擦音。周围血管征阴性。腹部平坦，未见胃肠型及蠕动波。未见静脉曲张，脐部正\n常。腹部柔软，无液波震颤，未触及腹部肿块。全腹无压痛、无反跳痛，无肌紧张。肝、脾脏未触及\n肾未触及。肝浊音界存在，肝上界位于右锁骨中线第5肋间，移动性浊音阴性，双肾区无叩痛。肠\n音正常，无气过水声，无震水音，未闻及腹部血管杂音。肛门、直肠及外生殖器：正常。脊柱正常\n第 2 页\n号 A1687966\n理弯曲,活动自如,无压痛及叩击痛。四肢活动自如,关节无红肿,活动自如,皮温正常。无杵状指、\n趾,双下肢无水肿。腹壁反射存在,双侧跟腱反射正常,四肢肌力及肌张力正常,双侧巴彬斯征、\n布鲁金斯基征、克匿格征阴性。\n辅助检查结果:2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增\n高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢\n增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并\n淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积\n液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。\n2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾\n向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-).\nPR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约\n50%+)。\n心肌酶正常,CA125 372U/ml。\n2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。\n入院诊断:1.肺腺癌 cTxNxM1 IVb期 骨转移、双\n肺、心包转移2.胸腔积液3.心包积液4.肺部感染?\n医生签名",
    "role": "user"
  }
]
2026-08-10 15:06:29,990 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:06:29.990+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:06:56,483 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:06:56,483 INFO     29 [qwen-vl-text] LLM output (len=5042):
{
  "encounter_date": "2026-03-04",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 41,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "职工",
  "dm_admission_time": "2026-03-04 09:20",
  "dm_record_time": "2026-03-04 10:56",
  "dm_history_provider": "患者本人",
  "cc_text": "确诊肺腺癌8个月余。",
  "cc_main_symptoms": [
    "确诊肺腺癌"
  ],
  "cc_duration": "8个月余",
  "pi_text": "患者自诉2025年6月开始无明显诱因出现活动后气促，为求治疗在就诊，完善检查：（左侧颈部淋巴结）HE结合免疫组化符合转移性腺癌，倾向肺来源可能性大，请完善相关检查后综合考虑。IHC：GATA-3(-)，P16(-)，CK7(+)，ER(-).PR(-)，CK20(-)，Pax-8(-)，TTF-1(+)，NapsinA(+)，CerbB-2(1+)，Villin(+)，Ki-67(热点区约50%+)。PETCT：1.双肺散在斑片影及磨玻璃影，糖代谢增高，双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结，糖代谢增高，脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高，上述考虑恶性肿瘤（肺CA？）并淋巴结、骨转移可能，建议结合病理。2.双侧胸腔积液，双下肺膨胀不全。3.心包积液，盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶，糖代谢增高，考虑生理性改变。诊断考虑为“左上肺腺癌广泛转移”，行化疗前准备（叶酸+维生素B12），于6月13日出院。2025年6月14日为求治疗入我科，于6月16日完善基因检测，于6月18日予以PCb+贝伐珠单抗联合治疗第1周期（培美曲塞785mg+卡铂600mg+贝伐珠单抗800mg），同时予以护胃、止呕等对症治疗，患者治疗完成予以办理出院。出院后患者诉气促好转，基因检测报告：BRAF（p.K601E），MET扩增，PDL1 TPS表达55%。2025年7月9日再入院，予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，于7月12日予以地舒单抗120mg护骨治疗，复查血常规正常于7月12日出院。出院后患者气促明显缓解，2025年7月30日为求治疗再入院，完善检查：肝肾功能、电解质、心肌酶、血常规正常。纵隔及心脏平扫及增强|肺部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强CT：肺部炎症，合并多发占位可能；心包积液；双侧部分肋骨、腰椎多发骨质病变，腹膜后多发小淋巴结，结合病史考虑转移。疗效评估为PR，于7月31日、8月23日、9月9日、10月02日予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，期间规律予以地舒单抗护骨治疗，患者治疗完成10月05日出院。2025年10月23日为求治疗再入院，完善相关检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强：与07-30老片相比：肺部炎症较前吸收，考虑肺内转移病灶，较前大致相仿；心包积液，较前稍吸收；双肾结石。双侧部分肋骨、腰椎多发骨质病变，似较前稍微增多；腹膜后多发小淋巴结，较前相仿；结合病史考虑转移。评估为SD，继续予以贝伐珠单抗800mg+替雷利珠单抗200mg维持治疗，同时予以降血脂治疗，2025年10月25日予以办理出院。2025年11月14日、12月4日返院继续治疗，因患者偶有痰中带血，停贝伐珠单抗，予以替雷禾珠单抗200mg维持治疗。2025年12月25日为求治疗再入院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强：与10-23老片相比：肺部炎症较前稍进展，考虑肺内转移病灶，较前大致相仿；心包积液，较前稍增多；双肾结石。双侧部分肋骨、腰椎多发骨质病变，较前相仿；腹膜后多发小淋巴结，较前稍微增大；左侧腋窝稍大淋巴结；结合病史考虑转移。评估为SD，免疫性肺炎不排除，参考中科院专家会诊意见，于2025年12月27日予以贝伐珠单抗联合PCb化疗联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成12月30日办理出院。2026年1月17日为求治疗再入院，完善检查，于2026年1月19日予以贝伐珠单抗联合PCb化疗联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成1月20日办理出院。2026年2月8日再次返院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强CT：与2025-10-23日老片相比：肺部炎症较前增多；肺内多发结节（右下肺后基底段新增10mm小结节，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可能。心包积液，大致同前；双肾结石。双侧部分肋骨、腰椎、骨盆多发骨质病变，大致同前。本次复查增强CT，对比2025-12片，疗效评价SD，建议继续贝伐珠单抗+培美曲塞+卡铂联合治疗，患者因过年要求暂缓化疗，于2026-02-12予以贝伐珠单抗800mg靶向治疗。治疗上予以抗感染、清热解毒、化痰止咳等对症治疗后于2月14日出院。今患者为求继续治疗在我院门诊就诊，门诊以“肺恶性肿瘤”收住我科，此次发病期间，患者精神食欲睡眠可，大小便正常，体重无明显变化。",
  "pmh_disease_history": [],
  "pmh_allergy_history": [],
  "pmh_surgery_trauma_history": [],
  "ph_smoking": null,
  "ph_drinking": null,
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": null,
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 85,
  "vs_respiration_rpm": 19,
  "vs_systolic_bp_mmhg": 100,
  "vs_diastolic_bp_mmhg": 78,
  "pe_general_condition": "发育正常，营养中等，自主体位，神志清楚，查体合作。",
  "pe_skin_mucosa": "粘膜无发绀、黄染、苍白，无皮疹。未见皮下出血。皮肤湿度正常，弹性正常，无肝掌，未见蜘蛛痣。",
  "pe_lymph_nodes": "左侧腋下可触及大小约1*1cm的肿大淋巴结，活动度差，质地韧，无明显压痛，边界不清晰。",
  "pe_lungs": "胸廓对称，双肺语颤正常，叩诊双肺呈清音，听诊双肺呼吸音低，未闻及明显罗音。",
  "pe_heart": "心前区无隆起，可见心尖搏动，心尖搏动位于第5肋间左锁骨中线内0.5cm，心前区无异常搏动。心尖搏动触不清，未触及震颤，无心包摩擦感。心界不大。心率：85次/分，律齐，心音清。各瓣膜听诊区未闻及病理性杂音，不可闻及额外心音，未闻及心包摩擦音。周围血管征阴性。",
  "pe_abdomen": "腹部平坦，未见胃肠型及蠕动波。未见静脉曲张，脐部正常。腹部柔软，无液波震颤，未触及腹部肿块。全腹无压痛、无反跳痛，无肌紧张。肝、脾脏未触及肾未触及。肝浊音界存在，肝上界位于右锁骨中线第5肋间，移动性浊音阴性，双肾区无叩痛。肠音正常，无气过水声，无震水音，未闻及腹部血管杂音。",
  "pe_extremities": "四肢活动自如,关节无红肿,活动自如,皮温正常。无杵状指、趾,双下肢无水肿。",
  "pe_nervous_system": "腹壁反射存在,双侧跟腱反射正常,四肢肌力及肌张力正常,双侧巴彬斯征、布鲁金斯基征、克匿格征阴性。",
  "pe_specialist_exam": null,
  "pe_ecog_score": null,
  "pat_text": "2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-).PR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约50%+)。心肌酶正常,CA125 372U/ml。2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。",
  "pat_items": [
    "2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。",
    "2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-).PR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约50%+)。",
    "心肌酶正常,CA125 372U/ml。",
    "2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。"
  ],
  "preliminary_diagnoses": [
    {
      "name": "肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "胸腔积液",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "心包积液",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肺部感染?",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": "肿瘤内科"
}
2026-08-10 15:06:56,484 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-04]
2026-08-10 15:06:56,487 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2229107, prompt_len=2235
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共46行）
["姓名：", "性别：女", "年龄：41岁", "婚 姻：已婚", "联系电话：", "出生", "民族：汉族", "职业：职工", "住址", "电子邮件(E_mail)：无", "入院时间：2026年03月04日 09时20分", "记录时间：2026年03月04日 10时56分", "病史陈述者：患者本人", "入院方式：步行", "主诉：确诊肺腺癌8个月余。", "现病史：患者自诉2025年6月开始无明显诱因出现活动后气促，为求治疗在", "就诊，完善检查：（左侧颈部淋巴结）HE结合免疫组化符合转移性腺癌，倾向肺来源可能性大，", "请完善相关检查后综合考虑。IHC：GATA-3(-)，P16(-)，CK7(+)，ER(-).PR(-)，CK20(-)，Pax-", "8(-)，TTF-1(+)，NapsinA(+)，CerbB-2(1+)，Villin(+)，Ki-67(热点区约50%+)。PETCT：1.双肺", "散在斑片影及磨玻璃影，糖代谢增高，双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹", "主动脉旁多发肿大淋巴结，糖代谢增高，脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增", "高，上述考虑恶性肿瘤（肺CA？）并淋巴结、骨转移可能，建议结合病理。2.双侧胸腔积液，双下", "肺膨胀不全。3.心包积液，盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶，糖代谢增高，考虑生", "理性改变。诊断考虑为“左上肺腺癌广泛转移”，行化疗前准备（叶酸+维生素B12），于6月13日", "出院。", "2025年6月14日为求治疗入我科，于6月16日完善基因检测，于6月18日予以PCb+贝伐珠单抗", "联合治疗第1周期（培美曲塞785mg+卡铂600mg+贝伐珠单抗800mg），同时予以护胃、止呕等对症", "治疗，患者治疗完成予以办理出院。", "出院后患者诉气促好转，基因检测报告：BRAF（p.K601E），MET扩增，PDL1 TPS表达55%。", "2025年7月9日再入院，予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂", "650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，于7月12日予以地", "舒单抗120mg护骨治疗，复查血常规正常于7月12日出院。", "出院后患者气促明显缓解，2025年7月30日为求治疗再入院，完善检查：肝肾功能、电解质、", "心肌酶、血常规正常。纵隔及心脏平扫及增强|肺部平扫及增强|上腹部平扫及增强|下腹部平扫", "及增强|盆腔平扫及增强CT：肺部炎症，合并多发占位可能；心包积液；双侧部分肋骨、腰椎多发骨", "质病变，腹膜后多发小淋巴结，结合病史考虑转移。疗效评估为PR，于7月31日、8月23日、9月9日、", "10月02日予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单", "抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，期间规律予以地舒单抗护骨治疗，", "患者治疗完成10月05日出院。", "2025年10月23日为求治疗再入院，完善相关检查：胸部平扫及增强|上腹部平扫及增强|下", "腹部平扫及增强|盆腔平扫及增强：与07-30老片相比：肺部炎症较前吸收，考虑肺内转移病灶，", "较前大致相仿；心包积液，较前稍吸收；双肾结石。双侧部分肋骨、腰椎多发骨质病变，似较前稍微", "增多；腹膜后多发小淋巴结，较前相仿；结合病史考虑转移。评估为SD，继续予以贝伐珠单抗", "800mg+替雷利珠单抗200mg维持治疗，同时予以降血脂治疗，2025年10月25日予以办理出院。", "2025年11月14日、12月4日返院继续治疗，因患者偶有痰中带血，停贝伐珠单抗，予以替雷禾", "第 1 页"]

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
2026-08-10 15:07:17,397 INFO     29 [qwen-vl-text] coord API raw response (len=3511):
[
	{"text": "姓名：", "bbox": [111, 100, 132, 116]},
	{"text": "性别：女", "bbox": [170, 122, 228, 138]},
	{"text": "年龄：41岁", "bbox": [170, 144, 247, 160]},
	{"text": "婚 姻：已婚", "bbox": [111, 166, 247, 182]},
	{"text": "联系电话：", "bbox": [111, 188, 197, 204]},
	{"text": "出生", "bbox": [481, 100, 528, 116]},
	{"text": "民族：汉族", "bbox": [540, 122, 618, 138]},
	{"text": "职业：职工", "bbox": [540, 144, 618, 160]},
	{"text": "住址", "bbox": [481, 166, 502, 182]},
	{"text": "电子邮件(E_mail)：无", "bbox": [481, 188, 678, 204]},
	{"text": "入院时间：2026年03月04日 09时20分", "bbox": [111, 210, 435, 226]},
	{"text": "记录时间：2026年03月04日 10时56分", "bbox": [481, 210, 805, 226]},
	{"text": "病史陈述者：患者本人", "bbox": [111, 233, 307, 249]},
	{"text": "入院方式：步行", "bbox": [481, 233, 617, 249]},
	{"text": "主诉：确诊肺腺癌8个月余。", "bbox": [150, 259, 374, 275]},
	{"text": "现病史：患者自诉2025年6月开始无明显诱因出现活动后气促，为求治疗在", "bbox": [150, 280, 772, 297]},
	{"text": "就诊，完善检查：（左侧颈部淋巴结）HE结合免疫组化符合转移性腺癌，倾向肺来源可能性大，", "bbox": [111, 302, 912, 318]},
	{"text": "请完善相关检查后综合考虑。IHC：GATA-3(-)，P16(-)，CK7(+)，ER(-).PR(-)，CK20(-)，Pax-", "bbox": [111, 324, 912, 340]},
	{"text": "8(-)，TTF-1(+)，NapsinA(+)，CerbB-2(1+)，Villin(+)，Ki-67(热点区约50%+)。PETCT：1.双肺", "bbox": [111, 345, 912, 362]},
	{"text": "散在斑片影及磨玻璃影，糖代谢增高，双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹", "bbox": [111, 366, 914, 383]},
	{"text": "主动脉旁多发肿大淋巴结，糖代谢增高，脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增", "bbox": [111, 388, 914, 404]},
	{"text": "高，上述考虑恶性肿瘤（肺CA？）并淋巴结、骨转移可能，建议结合病理。2.双侧胸腔积液，双下", "bbox": [111, 409, 914, 425]},
	{"text": "肺膨胀不全。3.心包积液，盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶，糖代谢增高，考虑生", "bbox": [111, 430, 914, 447]},
	{"text": "理性改变。诊断考虑为“左上肺腺癌广泛转移”，行化疗前准备（叶酸+维生素B12），于6月13日", "bbox": [111, 451, 914, 468]},
	{"text": "出院。", "bbox": [111, 470, 158, 484]},
	{"text": "2025年6月14日为求治疗入我科，于6月16日完善基因检测，于6月18日予以PCb+贝伐珠单抗", "bbox": [150, 490, 914, 506]},
	{"text": "联合治疗第1周期（培美曲塞785mg+卡铂600mg+贝伐珠单抗800mg），同时予以护胃、止呕等对症", "bbox": [111, 510, 914, 527]},
	{"text": "治疗，患者治疗完成予以办理出院。", "bbox": [111, 530, 404, 546]},
	{"text": "出院后患者诉气促好转，基因检测报告：BRAF（p.K601E），MET扩增，PDL1 TPS表达55%。", "bbox": [150, 551, 914, 568]},
	{"text": "2025年7月9日再入院，予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂", "bbox": [111, 572, 914, 589]},
	{"text": "650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，于7月12日予以地", "bbox": [111, 593, 914, 610]},
	{"text": "舒单抗120mg护骨治疗，复查血常规正常于7月12日出院。", "bbox": [111, 614, 579, 630]},
	{"text": "出院后患者气促明显缓解，2025年7月30日为求治疗再入院，完善检查：肝肾功能、电解质、", "bbox": [150, 635, 914, 652]},
	{"text": "心肌酶、血常规正常。纵隔及心脏平扫及增强|肺部平扫及增强|上腹部平扫及增强|下腹部平扫", "bbox": [111, 656, 914, 673]},
	{"text": "及增强|盆腔平扫及增强CT：肺部炎症，合并多发占位可能；心包积液；双侧部分肋骨、腰椎多发骨", "bbox": [111, 677, 914, 694]},
	{"text": "质病变，腹膜后多发小淋巴结，结合病史考虑转移。疗效评估为PR，于7月31日、8月23日、9月9日、", "bbox": [111, 698, 914, 715]},
	{"text": "10月02日予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单", "bbox": [111, 719, 914, 736]},
	{"text": "抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，期间规律予以地舒单抗护骨治疗，", "bbox": [111, 740, 914, 757]},
	{"text": "患者治疗完成10月05日出院。", "bbox": [111, 760, 355, 777]},
	{"text": "2025年10月23日为求治疗再入院，完善相关检查：胸部平扫及增强|上腹部平扫及增强|下", "bbox": [150, 781, 914, 798]},
	{"text": "腹部平扫及增强|盆腔平扫及增强：与07-30老片相比：肺部炎症较前吸收，考虑肺内转移病灶，", "bbox": [111, 802, 914, 819]},
	{"text": "较前大致相仿；心包积液，较前稍吸收；双肾结石。双侧部分肋骨、腰椎多发骨质病变，似较前稍微", "bbox": [111, 823, 914, 840]},
	{"text": "增多；腹膜后多发小淋巴结，较前相仿；结合病史考虑转移。评估为SD，继续予以贝伐珠单抗", "bbox": [111, 844, 914, 861]},
	{"text": "800mg+替雷利珠单抗200mg维持治疗，同时予以降血脂治疗，2025年10月25日予以办理出院。", "bbox": [111, 865, 871, 881]},
	{"text": "2025年11月14日、12月4日返院继续治疗，因患者偶有痰中带血，停贝伐珠单抗，予以替雷禾", "bbox": [150, 885, 912, 901]},
	{"text": "第 1 页", "bbox": [478, 918, 554, 932]}
]
2026-08-10 15:07:17,397 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=20.9s
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[111, 100, 132, 116]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[1]: text=性别：女, bbox=[170, 122, 228, 138]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：41岁, bbox=[170, 144, 247, 160]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[3]: text=婚 姻：已婚, bbox=[111, 166, 247, 182]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[4]: text=联系电话：, bbox=[111, 188, 197, 204]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[5]: text=出生, bbox=[481, 100, 528, 116]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[6]: text=民族：汉族, bbox=[540, 122, 618, 138]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[7]: text=职业：职工, bbox=[540, 144, 618, 160]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[8]: text=住址, bbox=[481, 166, 502, 182]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[9]: text=电子邮件(E_mail)：无, bbox=[481, 188, 678, 204]
2026-08-10 15:07:17,398 INFO     29 [qwen-vl-text] coord item[10]: text=入院时间：2026年03月04日 09时20分, bbox=[111, 210, 435, 226]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[11]: text=记录时间：2026年03月04日 10时56分, bbox=[481, 210, 805, 226]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[12]: text=病史陈述者：患者本人, bbox=[111, 233, 307, 249]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[13]: text=入院方式：步行, bbox=[481, 233, 617, 249]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：确诊肺腺癌8个月余。, bbox=[150, 259, 374, 275]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：患者自诉2025年6月开始无明显诱因出现活动后气促，为求治疗在, bbox=[150, 280, 772, 297]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[16]: text=就诊，完善检查：（左侧颈部淋巴结）HE结合免疫组化符合转移性腺癌，倾向肺来源可能性大，, bbox=[111, 302, 912, 318]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[17]: text=请完善相关检查后综合考虑。IHC：GATA-3(-)，P16(-)，CK7(+)，ER(-).PR(-)，CK20(-)，Pax-, bbox=[111, 324, 912, 340]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[18]: text=8(-)，TTF-1(+)，NapsinA(+)，CerbB-2(1+)，Villin(+)，Ki-67(热点区约50%+)。PETCT：1.双肺, bbox=[111, 345, 912, 362]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[19]: text=散在斑片影及磨玻璃影，糖代谢增高，双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹, bbox=[111, 366, 914, 383]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[20]: text=主动脉旁多发肿大淋巴结，糖代谢增高，脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增, bbox=[111, 388, 914, 404]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[21]: text=高，上述考虑恶性肿瘤（肺CA？）并淋巴结、骨转移可能，建议结合病理。2.双侧胸腔积液，双下, bbox=[111, 409, 914, 425]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[22]: text=肺膨胀不全。3.心包积液，盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶，糖代谢增高，考虑生, bbox=[111, 430, 914, 447]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[23]: text=理性改变。诊断考虑为“左上肺腺癌广泛转移”，行化疗前准备（叶酸+维生素B12），于6月13日, bbox=[111, 451, 914, 468]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[24]: text=出院。, bbox=[111, 470, 158, 484]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[25]: text=2025年6月14日为求治疗入我科，于6月16日完善基因检测，于6月18日予以PCb+贝伐珠单抗, bbox=[150, 490, 914, 506]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[26]: text=联合治疗第1周期（培美曲塞785mg+卡铂600mg+贝伐珠单抗800mg），同时予以护胃、止呕等对症, bbox=[111, 510, 914, 527]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[27]: text=治疗，患者治疗完成予以办理出院。, bbox=[111, 530, 404, 546]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[28]: text=出院后患者诉气促好转，基因检测报告：BRAF（p.K601E），MET扩增，PDL1 TPS表达55%。, bbox=[150, 551, 914, 568]
2026-08-10 15:07:17,399 INFO     29 [qwen-vl-text] coord item[29]: text=2025年7月9日再入院，予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂, bbox=[111, 572, 914, 589]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[30]: text=650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，于7月12日予以地, bbox=[111, 593, 914, 610]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[31]: text=舒单抗120mg护骨治疗，复查血常规正常于7月12日出院。, bbox=[111, 614, 579, 630]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[32]: text=出院后患者气促明显缓解，2025年7月30日为求治疗再入院，完善检查：肝肾功能、电解质、, bbox=[150, 635, 914, 652]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[33]: text=心肌酶、血常规正常。纵隔及心脏平扫及增强|肺部平扫及增强|上腹部平扫及增强|下腹部平扫, bbox=[111, 656, 914, 673]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[34]: text=及增强|盆腔平扫及增强CT：肺部炎症，合并多发占位可能；心包积液；双侧部分肋骨、腰椎多发骨, bbox=[111, 677, 914, 694]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[35]: text=质病变，腹膜后多发小淋巴结，结合病史考虑转移。疗效评估为PR，于7月31日、8月23日、9月9日、, bbox=[111, 698, 914, 715]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[36]: text=10月02日予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单, bbox=[111, 719, 914, 736]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[37]: text=抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，期间规律予以地舒单抗护骨治疗，, bbox=[111, 740, 914, 757]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[38]: text=患者治疗完成10月05日出院。, bbox=[111, 760, 355, 777]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[39]: text=2025年10月23日为求治疗再入院，完善相关检查：胸部平扫及增强|上腹部平扫及增强|下, bbox=[150, 781, 914, 798]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[40]: text=腹部平扫及增强|盆腔平扫及增强：与07-30老片相比：肺部炎症较前吸收，考虑肺内转移病灶，, bbox=[111, 802, 914, 819]
2026-08-10 15:07:17,400 INFO     29 [qwen-vl-text] coord item[41]: text=较前大致相仿；心包积液，较前稍吸收；双肾结石。双侧部分肋骨、腰椎多发骨质病变，似较前稍微, bbox=[111, 823, 914, 840]
2026-08-10 15:07:17,401 INFO     29 [qwen-vl-text] coord item[42]: text=增多；腹膜后多发小淋巴结，较前相仿；结合病史考虑转移。评估为SD，继续予以贝伐珠单抗, bbox=[111, 844, 914, 861]
2026-08-10 15:07:17,401 INFO     29 [qwen-vl-text] coord item[43]: text=800mg+替雷利珠单抗200mg维持治疗，同时予以降血脂治疗，2025年10月25日予以办理出院。, bbox=[111, 865, 871, 881]
2026-08-10 15:07:17,401 INFO     29 [qwen-vl-text] coord item[44]: text=2025年11月14日、12月4日返院继续治疗，因患者偶有痰中带血，停贝伐珠单抗，予以替雷禾, bbox=[150, 885, 912, 901]
2026-08-10 15:07:17,401 INFO     29 [qwen-vl-text] coord item[45]: text=第 1 页, bbox=[478, 918, 554, 932]
2026-08-10 15:07:17,401 INFO     29 [qwen-vl-text] page=0 — 46/46 coords, api_time=20.9s
2026-08-10 15:07:17,407 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2378696, prompt_len=2316
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["珠单抗200mg维持治疗。", "2025年12月25日为求治疗再入院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部", "平扫及增强|盆腔平扫及增强：与10-23老片相比：肺部炎症较前稍进展，考虑肺内转移病灶，较", "前大致相仿；心包积液，较前稍增多；双肾结石。双侧部分肋骨、腰椎多发骨质病变，较前相仿；腹", "膜后多发小淋巴结，较前稍微增大；左侧腋窝稍大淋巴结；结合病史考虑转移。评估为SD，免疫性", "肺炎不排除，参考中科院专家会诊意见，于2025年12月27日予以贝伐珠单抗联合PCb化疗联合治", "疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成12月", "30日办理出院。", "2026年1月17日为求治疗再入院，完善检查，于2026年1月19日予以贝伐珠单抗联合PCb化疗", "联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完", "成1月20日办理出院。", "2026年2月8日再次返院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增", "强|盆腔平扫及增强CT：与2025-10-23日老片相比：肺部炎症较前增多；肺内多发结节（右下肺", "后基底段新增10mm小结节，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可", "能。心包积液，大致同前；双肾结石。双侧部分肋骨、腰椎、骨盆多发骨质病变，大致同前。本次复查", "增强CT，对比2025-12片，疗效评价SD，建议继续贝伐珠单抗+培美曲塞+卡铂联合治疗，患者因过", "年要求暂缓化疗，于2026-02-12予以贝伐珠单抗800mg靶向治疗。治疗上予以抗感染、清热解毒、", "化痰止咳等对症治疗后于2月14日出院。", "今患者为求继续治疗在我院门诊就诊，门诊以“肺恶性肿瘤”收住我科，此次发病期间，患", "者精神食欲睡眠可，大小便正常，体重无明显变化。", "既往史：个人史、月经及婚育史、家族史见第一次入院记录。", "体格检查", "T：36.5℃ P：85次/分 R：19次/分 BP：100/78mmHg", "发育正常，营养中等，自主体位，神志清楚，查体合作。粘膜无发绀、黄染、苍白，无皮疹。未见", "皮下出血。皮肤湿度正常，弹性正常，无肝掌，未见蜘蛛痣。左侧腋下可触及大小约1*1cm的肿大淋", "巴结，活动度差，质地韧，无明显压痛，边界不清晰。头颅外形正常。眼：眼睑正常，眼球无凸出及", "凹陷，结膜正常。巩膜无黄染，双侧瞳孔等大等圆，瞳孔直径3.0mm，对光反射及调节均灵敏。耳：", "双耳耳廓外形正常，无畸形，双侧无乳突压痛，外耳道通畅，无分泌物。鼻外形正常，鼻中隔无偏", "曲，上颌窦与额窦无压痛，无鼻塞，无分泌物。口腔：口唇红润，伸舌居中，双侧扁桃体无肿大，表", "面未见脓点，咽无充血，声音嘶哑。颈软，无抵抗感，气管居中，颈静脉充盈正常，肝颈静脉回流征", "阴性，颈动脉搏动正常，甲状腺未触及肿大。胸廓正常，肋间隙正常，胸壁无压痛，无胸骨叩痛。呼", "吸节律正常，语颤正常，双肺未触及胸膜摩擦感，未触及皮下捻发感。胸廓对称，双肺语颤正常，叩", "诊双肺呈清音，听诊双肺呼吸音低，未闻及明显罗音。心前区无隆起，可见心尖搏动，心尖搏动位", "于第5肋间左锁骨中线内0.5cm，心前区无异常搏动。心尖搏动触不清，未触及震颤，无心包摩擦", "感。心界不大。心率：85次/分，律齐，心音清。各瓣膜听诊区未闻及病理性杂音，不可闻及额外心", "音，未闻及心包摩擦音。周围血管征阴性。腹部平坦，未见胃肠型及蠕动波。未见静脉曲张，脐部正", "常。腹部柔软，无液波震颤，未触及腹部肿块。全腹无压痛、无反跳痛，无肌紧张。肝、脾脏未触及", "肾未触及。肝浊音界存在，肝上界位于右锁骨中线第5肋间，移动性浊音阴性，双肾区无叩痛。肠", "音正常，无气过水声，无震水音，未闻及腹部血管杂音。肛门、直肠及外生殖器：正常。脊柱正常", "第 2 页"]

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
2026-08-10 15:07:36,118 INFO     29 [qwen-vl-text] coord API raw response (len=3346):
[
	{"text": "珠单抗200mg维持治疗。", "bbox": [124, 122, 310, 139]},
	{"text": "2025年12月25日为求治疗再入院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部", "bbox": [124, 143, 898, 160]},
	{"text": "平扫及增强|盆腔平扫及增强：与10-23老片相比：肺部炎症较前稍进展，考虑肺内转移病灶，较", "bbox": [124, 162, 898, 180]},
	{"text": "前大致相仿；心包积液，较前稍增多；双肾结石。双侧部分肋骨、腰椎多发骨质病变，较前相仿；腹", "bbox": [124, 182, 898, 199]},
	{"text": "膜后多发小淋巴结，较前稍微增大；左侧腋窝稍大淋巴结；结合病史考虑转移。评估为SD，免疫性", "bbox": [124, 201, 898, 218]},
	{"text": "肺炎不排除，参考中科院专家会诊意见，于2025年12月27日予以贝伐珠单抗联合PCb化疗联合治", "bbox": [124, 220, 898, 238]},
	{"text": "疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成12月", "bbox": [124, 240, 895, 258]},
	{"text": "30日办理出院。", "bbox": [124, 260, 245, 277]},
	{"text": "2026年1月17日为求治疗再入院，完善检查，于2026年1月19日予以贝伐珠单抗联合PCb化疗", "bbox": [161, 280, 898, 297]},
	{"text": "联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完", "bbox": [124, 300, 900, 317]},
	{"text": "成1月20日办理出院。", "bbox": [124, 320, 292, 337]},
	{"text": "2026年2月8日再次返院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增", "bbox": [161, 340, 900, 357]},
	{"text": "强|盆腔平扫及增强CT：与2025-10-23日老片相比：肺部炎症较前增多；肺内多发结节（右下肺", "bbox": [124, 360, 900, 377]},
	{"text": "后基底段新增10mm小结节，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可", "bbox": [124, 379, 900, 397]},
	{"text": "能。心包积液，大致同前；双肾结石。双侧部分肋骨、腰椎、骨盆多发骨质病变，大致同前。本次复查", "bbox": [124, 399, 900, 416]},
	{"text": "增强CT，对比2025-12片，疗效评价SD，建议继续贝伐珠单抗+培美曲塞+卡铂联合治疗，患者因过", "bbox": [124, 418, 900, 436]},
	{"text": "年要求暂缓化疗，于2026-02-12予以贝伐珠单抗800mg靶向治疗。治疗上予以抗感染、清热解毒、", "bbox": [124, 438, 900, 455]},
	{"text": "化痰止咳等对症治疗后于2月14日出院。", "bbox": [124, 458, 444, 475]},
	{"text": "今患者为求继续治疗在我院门诊就诊，门诊以“肺恶性肿瘤”收住我科，此次发病期间，患", "bbox": [161, 478, 900, 495]},
	{"text": "者精神食欲睡眠可，大小便正常，体重无明显变化。", "bbox": [124, 497, 527, 514]},
	{"text": "既往史：个人史、月经及婚育史、家族史见第一次入院记录。", "bbox": [161, 517, 631, 534]},
	{"text": "体格检查", "bbox": [475, 537, 550, 554]},
	{"text": "T：36.5℃ P：85次/分 R：19次/分 BP：100/78mmHg", "bbox": [280, 557, 746, 574]},
	{"text": "发育正常，营养中等，自主体位，神志清楚，查体合作。粘膜无发绀、黄染、苍白，无皮疹。未见", "bbox": [161, 577, 904, 594]},
	{"text": "皮下出血。皮肤湿度正常，弹性正常，无肝掌，未见蜘蛛痣。左侧腋下可触及大小约1*1cm的肿大淋", "bbox": [124, 597, 902, 614]},
	{"text": "巴结，活动度差，质地韧，无明显压痛，边界不清晰。头颅外形正常。眼：眼睑正常，眼球无凸出及", "bbox": [124, 616, 902, 634]},
	{"text": "凹陷，结膜正常。巩膜无黄染，双侧瞳孔等大等圆，瞳孔直径3.0mm，对光反射及调节均灵敏。耳：", "bbox": [124, 636, 892, 654]},
	{"text": "双耳耳廓外形正常，无畸形，双侧无乳突压痛，外耳道通畅，无分泌物。鼻外形正常，鼻中隔无偏", "bbox": [124, 656, 904, 673]},
	{"text": "曲，上颌窦与额窦无压痛，无鼻塞，无分泌物。口腔：口唇红润，伸舌居中，双侧扁桃体无肿大，表", "bbox": [124, 676, 904, 693]},
	{"text": "面未见脓点，咽无充血，声音嘶哑。颈软，无抵抗感，气管居中，颈静脉充盈正常，肝颈静脉回流征", "bbox": [124, 695, 904, 713]},
	{"text": "阴性，颈动脉搏动正常，甲状腺未触及肿大。胸廓正常，肋间隙正常，胸壁无压痛，无胸骨叩痛。呼", "bbox": [124, 715, 902, 732]},
	{"text": "吸节律正常，语颤正常，双肺未触及胸膜摩擦感，未触及皮下捻发感。胸廓对称，双肺语颤正常，叩", "bbox": [124, 735, 902, 752]},
	{"text": "诊双肺呈清音，听诊双肺呼吸音低，未闻及明显罗音。心前区无隆起，可见心尖搏动，心尖搏动位", "bbox": [124, 754, 900, 772]},
	{"text": "于第5肋间左锁骨中线内0.5cm，心前区无异常搏动。心尖搏动触不清，未触及震颤，无心包摩擦", "bbox": [124, 774, 900, 791]},
	{"text": "感。心界不大。心率：85次/分，律齐，心音清。各瓣膜听诊区未闻及病理性杂音，不可闻及额外心", "bbox": [124, 794, 900, 811]},
	{"text": "音，未闻及心包摩擦音。周围血管征阴性。腹部平坦，未见胃肠型及蠕动波。未见静脉曲张，脐部正", "bbox": [124, 813, 900, 831]},
	{"text": "常。腹部柔软，无液波震颤，未触及腹部肿块。全腹无压痛、无反跳痛，无肌紧张。肝、脾脏未触及", "bbox": [124, 833, 895, 850]},
	{"text": "肾未触及。肝浊音界存在，肝上界位于右锁骨中线第5肋间，移动性浊音阴性，双肾区无叩痛。肠", "bbox": [124, 853, 892, 870]},
	{"text": "音正常，无气过水声，无震水音，未闻及腹部血管杂音。肛门、直肠及外生殖器：正常。脊柱正常", "bbox": [120, 873, 892, 891]},
	{"text": "第 2 页", "bbox": [475, 912, 551, 928]}
]
2026-08-10 15:07:36,118 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=18.7s
2026-08-10 15:07:36,118 INFO     29 [qwen-vl-text] coord item[0]: text=珠单抗200mg维持治疗。, bbox=[124, 122, 310, 139]
2026-08-10 15:07:36,118 INFO     29 [qwen-vl-text] coord item[1]: text=2025年12月25日为求治疗再入院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部, bbox=[124, 143, 898, 160]
2026-08-10 15:07:36,118 INFO     29 [qwen-vl-text] coord item[2]: text=平扫及增强|盆腔平扫及增强：与10-23老片相比：肺部炎症较前稍进展，考虑肺内转移病灶，较, bbox=[124, 162, 898, 180]
2026-08-10 15:07:36,118 INFO     29 [qwen-vl-text] coord item[3]: text=前大致相仿；心包积液，较前稍增多；双肾结石。双侧部分肋骨、腰椎多发骨质病变，较前相仿；腹, bbox=[124, 182, 898, 199]
2026-08-10 15:07:36,118 INFO     29 [qwen-vl-text] coord item[4]: text=膜后多发小淋巴结，较前稍微增大；左侧腋窝稍大淋巴结；结合病史考虑转移。评估为SD，免疫性, bbox=[124, 201, 898, 218]
2026-08-10 15:07:36,118 INFO     29 [qwen-vl-text] coord item[5]: text=肺炎不排除，参考中科院专家会诊意见，于2025年12月27日予以贝伐珠单抗联合PCb化疗联合治, bbox=[124, 220, 898, 238]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[6]: text=疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成12月, bbox=[124, 240, 895, 258]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[7]: text=30日办理出院。, bbox=[124, 260, 245, 277]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[8]: text=2026年1月17日为求治疗再入院，完善检查，于2026年1月19日予以贝伐珠单抗联合PCb化疗, bbox=[161, 280, 898, 297]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[9]: text=联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完, bbox=[124, 300, 900, 317]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[10]: text=成1月20日办理出院。, bbox=[124, 320, 292, 337]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[11]: text=2026年2月8日再次返院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增, bbox=[161, 340, 900, 357]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[12]: text=强|盆腔平扫及增强CT：与2025-10-23日老片相比：肺部炎症较前增多；肺内多发结节（右下肺, bbox=[124, 360, 900, 377]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[13]: text=后基底段新增10mm小结节，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可, bbox=[124, 379, 900, 397]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[14]: text=能。心包积液，大致同前；双肾结石。双侧部分肋骨、腰椎、骨盆多发骨质病变，大致同前。本次复查, bbox=[124, 399, 900, 416]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[15]: text=增强CT，对比2025-12片，疗效评价SD，建议继续贝伐珠单抗+培美曲塞+卡铂联合治疗，患者因过, bbox=[124, 418, 900, 436]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[16]: text=年要求暂缓化疗，于2026-02-12予以贝伐珠单抗800mg靶向治疗。治疗上予以抗感染、清热解毒、, bbox=[124, 438, 900, 455]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[17]: text=化痰止咳等对症治疗后于2月14日出院。, bbox=[124, 458, 444, 475]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[18]: text=今患者为求继续治疗在我院门诊就诊，门诊以“肺恶性肿瘤”收住我科，此次发病期间，患, bbox=[161, 478, 900, 495]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[19]: text=者精神食欲睡眠可，大小便正常，体重无明显变化。, bbox=[124, 497, 527, 514]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[20]: text=既往史：个人史、月经及婚育史、家族史见第一次入院记录。, bbox=[161, 517, 631, 534]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[21]: text=体格检查, bbox=[475, 537, 550, 554]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[22]: text=T：36.5℃ P：85次/分 R：19次/分 BP：100/78mmHg, bbox=[280, 557, 746, 574]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[23]: text=发育正常，营养中等，自主体位，神志清楚，查体合作。粘膜无发绀、黄染、苍白，无皮疹。未见, bbox=[161, 577, 904, 594]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[24]: text=皮下出血。皮肤湿度正常，弹性正常，无肝掌，未见蜘蛛痣。左侧腋下可触及大小约1*1cm的肿大淋, bbox=[124, 597, 902, 614]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[25]: text=巴结，活动度差，质地韧，无明显压痛，边界不清晰。头颅外形正常。眼：眼睑正常，眼球无凸出及, bbox=[124, 616, 902, 634]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[26]: text=凹陷，结膜正常。巩膜无黄染，双侧瞳孔等大等圆，瞳孔直径3.0mm，对光反射及调节均灵敏。耳：, bbox=[124, 636, 892, 654]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[27]: text=双耳耳廓外形正常，无畸形，双侧无乳突压痛，外耳道通畅，无分泌物。鼻外形正常，鼻中隔无偏, bbox=[124, 656, 904, 673]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[28]: text=曲，上颌窦与额窦无压痛，无鼻塞，无分泌物。口腔：口唇红润，伸舌居中，双侧扁桃体无肿大，表, bbox=[124, 676, 904, 693]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[29]: text=面未见脓点，咽无充血，声音嘶哑。颈软，无抵抗感，气管居中，颈静脉充盈正常，肝颈静脉回流征, bbox=[124, 695, 904, 713]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[30]: text=阴性，颈动脉搏动正常，甲状腺未触及肿大。胸廓正常，肋间隙正常，胸壁无压痛，无胸骨叩痛。呼, bbox=[124, 715, 902, 732]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[31]: text=吸节律正常，语颤正常，双肺未触及胸膜摩擦感，未触及皮下捻发感。胸廓对称，双肺语颤正常，叩, bbox=[124, 735, 902, 752]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[32]: text=诊双肺呈清音，听诊双肺呼吸音低，未闻及明显罗音。心前区无隆起，可见心尖搏动，心尖搏动位, bbox=[124, 754, 900, 772]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[33]: text=于第5肋间左锁骨中线内0.5cm，心前区无异常搏动。心尖搏动触不清，未触及震颤，无心包摩擦, bbox=[124, 774, 900, 791]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[34]: text=感。心界不大。心率：85次/分，律齐，心音清。各瓣膜听诊区未闻及病理性杂音，不可闻及额外心, bbox=[124, 794, 900, 811]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[35]: text=音，未闻及心包摩擦音。周围血管征阴性。腹部平坦，未见胃肠型及蠕动波。未见静脉曲张，脐部正, bbox=[124, 813, 900, 831]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[36]: text=常。腹部柔软，无液波震颤，未触及腹部肿块。全腹无压痛、无反跳痛，无肌紧张。肝、脾脏未触及, bbox=[124, 833, 895, 850]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[37]: text=肾未触及。肝浊音界存在，肝上界位于右锁骨中线第5肋间，移动性浊音阴性，双肾区无叩痛。肠, bbox=[124, 853, 892, 870]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[38]: text=音正常，无气过水声，无震水音，未闻及腹部血管杂音。肛门、直肠及外生殖器：正常。脊柱正常, bbox=[120, 873, 892, 891]
2026-08-10 15:07:36,119 INFO     29 [qwen-vl-text] coord item[39]: text=第 2 页, bbox=[475, 912, 551, 928]
2026-08-10 15:07:36,120 INFO     29 [qwen-vl-text] page=1 — 40/40 coords, api_time=18.7s
2026-08-10 15:07:36,123 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1768543, prompt_len=1318
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["号 A1687966", "理弯曲,活动自如,无压痛及叩击痛。四肢活动自如,关节无红肿,活动自如,皮温正常。无杵状指、", "趾,双下肢无水肿。腹壁反射存在,双侧跟腱反射正常,四肢肌力及肌张力正常,双侧巴彬斯征、", "布鲁金斯基征、克匿格征阴性。", "辅助检查结果:2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增", "高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢", "增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并", "淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积", "液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。", "2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾", "向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-).", "PR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约", "50%+)。", "心肌酶正常,CA125 372U/ml。", "2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。", "入院诊断:1.肺腺癌 cTxNxM1 IVb期 骨转移、双", "肺、心包转移2.胸腔积液3.心包积液4.肺部感染?", "医生签名"]

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
2026-08-10 15:07:46,125 INFO     29 [qwen-vl-text] coord API raw response (len=1432):
[
	{"text": "号 A1687966", "bbox": [734, 74, 848, 89]},
	{"text": "理弯曲,活动自如,无压痛及叩击痛。四肢活动自如,关节无红肿,活动自如,皮温正常。无杵状指、", "bbox": [98, 103, 919, 120]},
	{"text": "趾,双下肢无水肿。腹壁反射存在,双侧跟腱反射正常,四肢肌力及肌张力正常,双侧巴彬斯征、", "bbox": [98, 123, 919, 140]},
	{"text": "布鲁金斯基征、克匿格征阴性。", "bbox": [98, 145, 357, 161]},
	{"text": "辅助检查结果:2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增", "bbox": [98, 166, 919, 184]},
	{"text": "高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢", "bbox": [98, 187, 919, 204]},
	{"text": "增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并", "bbox": [98, 208, 919, 225]},
	{"text": "淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积", "bbox": [98, 230, 919, 247]},
	{"text": "液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。", "bbox": [98, 251, 686, 268]},
	{"text": "2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾", "bbox": [133, 272, 919, 290]},
	{"text": "向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-).", "bbox": [98, 294, 915, 311]},
	{"text": "PR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约", "bbox": [98, 315, 915, 333]},
	{"text": "50%+)。", "bbox": [98, 337, 158, 352]},
	{"text": "心肌酶正常,CA125 372U/ml。", "bbox": [372, 358, 620, 374]},
	{"text": "2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。", "bbox": [137, 379, 765, 396]},
	{"text": "入院诊断:1.肺腺癌 cTxNxM1 IVb期 骨转移、双", "bbox": [499, 403, 917, 419]},
	{"text": "肺、心包转移2.胸腔积液3.心包积液4.肺部感染?", "bbox": [96, 430, 527, 447]},
	{"text": "医生签名", "bbox": [565, 459, 644, 474]}
]
2026-08-10 15:07:46,126 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=10.0s
2026-08-10 15:07:46,126 INFO     29 [qwen-vl-text] coord item[0]: text=号 A1687966, bbox=[734, 74, 848, 89]
2026-08-10 15:07:46,126 INFO     29 [qwen-vl-text] coord item[1]: text=理弯曲,活动自如,无压痛及叩击痛。四肢活动自如,关节无红肿,活动自如,皮温正常。无杵状指、, bbox=[98, 103, 919, 120]
2026-08-10 15:07:46,126 INFO     29 [qwen-vl-text] coord item[2]: text=趾,双下肢无水肿。腹壁反射存在,双侧跟腱反射正常,四肢肌力及肌张力正常,双侧巴彬斯征、, bbox=[98, 123, 919, 140]
2026-08-10 15:07:46,126 INFO     29 [qwen-vl-text] coord item[3]: text=布鲁金斯基征、克匿格征阴性。, bbox=[98, 145, 357, 161]
2026-08-10 15:07:46,126 INFO     29 [qwen-vl-text] coord item[4]: text=辅助检查结果:2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增, bbox=[98, 166, 919, 184]
2026-08-10 15:07:46,126 INFO     29 [qwen-vl-text] coord item[5]: text=高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢, bbox=[98, 187, 919, 204]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[6]: text=增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并, bbox=[98, 208, 919, 225]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[7]: text=淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积, bbox=[98, 230, 919, 247]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[8]: text=液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。, bbox=[98, 251, 686, 268]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[9]: text=2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾, bbox=[133, 272, 919, 290]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[10]: text=向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-)., bbox=[98, 294, 915, 311]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[11]: text=PR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约, bbox=[98, 315, 915, 333]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[12]: text=50%+)。, bbox=[98, 337, 158, 352]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[13]: text=心肌酶正常,CA125 372U/ml。, bbox=[372, 358, 620, 374]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[14]: text=2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。, bbox=[137, 379, 765, 396]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[15]: text=入院诊断:1.肺腺癌 cTxNxM1 IVb期 骨转移、双, bbox=[499, 403, 917, 419]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[16]: text=肺、心包转移2.胸腔积液3.心包积液4.肺部感染?, bbox=[96, 430, 527, 447]
2026-08-10 15:07:46,127 INFO     29 [qwen-vl-text] coord item[17]: text=医生签名, bbox=[565, 459, 644, 474]
2026-08-10 15:07:46,128 INFO     29 [qwen-vl-text] page=2 — 18/18 coords, api_time=10.0s
2026-08-10 15:07:46,128 INFO     29 [qwen-vl-text] new_positions (104):
[[0, 66.045, 78.53999999999999, 84.2, 97.672], [0, 101.14999999999999, 135.66, 102.72399999999999, 116.196], [0, 101.14999999999999, 146.965, 121.24799999999999, 134.72], [0, 66.045, 146.965, 139.772, 153.244], [0, 66.045, 117.21499999999999, 158.296, 171.768], [0, 286.195, 314.15999999999997, 84.2, 97.672], [0, 321.3, 367.71, 102.72399999999999, 116.196], [0, 321.3, 367.71, 121.24799999999999, 134.72], [0, 286.195, 298.69, 139.772, 153.244], [0, 286.195, 403.40999999999997, 158.296, 171.768], [0, 66.045, 258.825, 176.82, 190.292], [0, 286.195, 478.97499999999997, 176.82, 190.292], [0, 66.045, 182.665, 196.186, 209.658], [0, 286.195, 367.115, 196.186, 209.658], [0, 89.25, 222.53, 218.078, 231.54999999999998], [0, 89.25, 459.34, 235.76, 250.07399999999998], [0, 66.045, 542.64, 254.284, 267.756], [0, 66.045, 542.64, 272.808, 286.28], [0, 66.045, 542.64, 290.49, 304.804], [0, 66.045, 543.8299999999999, 308.17199999999997, 322.486], [0, 66.045, 543.8299999999999, 326.69599999999997, 340.168], [0, 66.045, 543.8299999999999, 344.378, 357.84999999999997], [0, 66.045, 543.8299999999999, 362.06, 376.37399999999997], [0, 66.045, 543.8299999999999, 379.74199999999996, 394.056], [0, 66.045, 94.00999999999999, 395.74, 407.52799999999996], [0, 89.25, 543.8299999999999, 412.58, 426.05199999999996], [0, 66.045, 543.8299999999999, 429.41999999999996, 443.734], [0, 66.045, 240.38, 446.26, 459.73199999999997], [0, 89.25, 543.8299999999999, 463.942, 478.256], [0, 66.045, 543.8299999999999, 481.62399999999997, 495.938], [0, 66.045, 543.8299999999999, 499.306, 513.62], [0, 66.045, 344.505, 516.9879999999999, 530.46], [0, 89.25, 543.8299999999999, 534.67, 548.984], [0, 66.045, 543.8299999999999, 552.352, 566.6659999999999], [0, 66.045, 543.8299999999999, 570.034, 584.348], [0, 66.045, 543.8299999999999, 587.716, 602.03], [0, 66.045, 543.8299999999999, 605.398, 619.712], [0, 66.045, 543.8299999999999, 623.0799999999999, 637.394], [0, 66.045, 211.225, 639.92, 654.2339999999999], [0, 89.25, 543.8299999999999, 657.602, 671.9159999999999], [0, 66.045, 543.8299999999999, 675.284, 689.598], [0, 66.045, 543.8299999999999, 692.966, 707.28], [0, 66.045, 543.8299999999999, 710.648, 724.962], [0, 66.045, 518.245, 728.3299999999999, 741.802], [0, 89.25, 542.64, 745.17, 758.6419999999999], [0, 284.40999999999997, 329.63, 772.956, 784.744], [1, 73.78, 184.45, 102.72399999999999, 117.038], [1, 73.78, 534.31, 120.40599999999999, 134.72], [1, 73.78, 534.31, 136.404, 151.56], [1, 73.78, 534.31, 153.244, 167.558], [1, 73.78, 534.31, 169.242, 183.55599999999998], [1, 73.78, 534.31, 185.23999999999998, 200.396], [1, 73.78, 532.525, 202.07999999999998, 217.236], [1, 73.78, 145.775, 218.92, 233.23399999999998], [1, 95.795, 534.31, 235.76, 250.07399999999998], [1, 73.78, 535.5, 252.6, 266.914], [1, 73.78, 173.73999999999998, 269.44, 283.75399999999996], [1, 95.795, 535.5, 286.28, 300.594], [1, 73.78, 535.5, 303.12, 317.43399999999997], [1, 73.78, 535.5, 319.118, 334.274], [1, 73.78, 535.5, 335.95799999999997, 350.272], [1, 73.78, 535.5, 351.95599999999996, 367.11199999999997], [1, 73.78, 535.5, 368.796, 383.11], [1, 73.78, 264.18, 385.63599999999997, 399.95], [1, 95.795, 535.5, 402.476, 416.78999999999996], [1, 73.78, 313.565, 418.474, 432.788], [1, 95.795, 375.445, 435.31399999999996, 449.628], [1, 282.625, 327.25, 452.154, 466.46799999999996], [1, 166.6, 443.87, 468.99399999999997, 483.308], [1, 95.795, 537.88, 485.834, 500.14799999999997], [1, 73.78, 536.6899999999999, 502.674, 516.9879999999999], [1, 73.78, 536.6899999999999, 518.672, 533.828], [1, 73.78, 530.74, 535.512, 550.668], [1, 73.78, 537.88, 552.352, 566.6659999999999], [1, 73.78, 537.88, 569.192, 583.506], [1, 73.78, 537.88, 585.1899999999999, 600.346], [1, 73.78, 536.6899999999999, 602.03, 616.3439999999999], [1, 73.78, 536.6899999999999, 618.87, 633.184], [1, 73.78, 535.5, 634.8679999999999, 650.024], [1, 73.78, 535.5, 651.708, 666.0219999999999], [1, 73.78, 535.5, 668.548, 682.862], [1, 73.78, 535.5, 684.5459999999999, 699.702], [1, 73.78, 532.525, 701.386, 715.6999999999999], [1, 73.78, 530.74, 718.226, 732.54], [1, 71.39999999999999, 530.74, 735.066, 750.222], [1, 282.625, 327.84499999999997, 767.904, 781.376], [2, 436.72999999999996, 504.56, 62.308, 74.938], [2, 58.309999999999995, 546.805, 86.726, 101.03999999999999], [2, 58.309999999999995, 546.805, 103.566, 117.88], [2, 58.309999999999995, 212.415, 122.08999999999999, 135.56199999999998], [2, 58.309999999999995, 546.805, 139.772, 154.928], [2, 58.309999999999995, 546.805, 157.454, 171.768], [2, 58.309999999999995, 546.805, 175.136, 189.45], [2, 58.309999999999995, 546.805, 193.66, 207.974], [2, 58.309999999999995, 408.16999999999996, 211.34199999999998, 225.656], [2, 79.13499999999999, 546.805, 229.024, 244.17999999999998], [2, 58.309999999999995, 544.425, 247.548, 261.86199999999997], [2, 58.309999999999995, 544.425, 265.23, 280.38599999999997], [2, 58.309999999999995, 94.00999999999999, 283.75399999999996, 296.384], [2, 221.34, 368.9, 301.436, 314.908], [2, 81.515, 455.17499999999995, 319.118, 333.432], [2, 296.905, 545.615, 339.32599999999996, 352.798], [2, 57.12, 313.565, 362.06, 376.37399999999997], [2, 336.175, 383.18, 386.478, 399.108]]
2026-08-10 15:07:46,128 INFO     29 [qwen-vl-text] ═══ DONE ═══ 104 positions, pages=3, time=78.7s
2026-08-10 15:07:46,147 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 15:07:46,147 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:07:46,148 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 15:07:46,149 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:07:46.148+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:07:46,160 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:07:46,162 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:07:46,162 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:07:46,162 INFO     29 [qwen-vl-text] positions(26): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:07:46,162 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [26]
2026-08-10 15:07:46,344 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:07:46,345 INFO     29 [qwen-vl-text] LLM extraction start, text_len=367
2026-08-10 15:07:46,345 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:07:46,345 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 133, \"bbox_end\": 158, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "5G 85\n< 详情\nJIX日时间· 2020 00 04 10.00.07\n检查医院:\n影像所见\n审核医生\n肺Ca患者复查：双肺支气管-血管束增\n多，双肺散在多发斑片状、小结节状磨玻璃密度影，气管及叶段支气管通畅。纵隔\n未见明显肿大淋巴结，双侧胸腔少许积液。心包见环形积液征象。左侧腋窝见肿\n大淋巴结，大者短径约17mm。双侧部分\n肋骨、胸椎见斑片状、结节状骨质密度增\n高影。\n影像诊断\n与2026.02.08日老片相比：肺部炎症较\n前稍增多；肺内多发结节（右下肺后基底\n段结节较前稍增大，现直径约13mm，余\n同前相仿），不排除转移瘤；左侧腋窝淋\n巴结较前增大，转移瘤可能。心包积液，\n大致同前；双侧胸腔新见少许积液。双侧\n部分肋骨、胸椎多发骨质病变，大致同\n前。\n相关检查(6)\n查看全部>\n图文报告\n影像浏览\nCS 扫描全能王",
    "role": "user"
  }
]
2026-08-10 15:07:49,482 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:07:49,482 INFO     29 [qwen-vl-text] LLM output (len=570):
{
  "exam_date": "2026-03-04",
  "report_date": "2026-03-04",
  "exam_name": "胸部CT",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "肺Ca患者复查：双肺支气管-血管束增多，双肺散在多发斑片状、小结节状磨玻璃密度影，气管及叶段支气管通畅。纵隔未见明显肿大淋巴结，双侧胸腔少许积液。心包见环形积液征象。左侧腋窝见肿大淋巴结，大者短径约17mm。双侧部分肋骨、胸椎见斑片状、结节状骨质密度增高影。",
  "conclusion": "与2026.02.08日老片相比：肺部炎症较前稍增多；肺内多发结节（右下肺后基底段结节较前稍增大，现直径约13mm，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可能。心包积液，大致同前；双侧胸腔新见少许积液。双侧部分肋骨、胸椎多发骨质病变，大致同前。",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:07:49,484 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1029259, prompt_len=1058
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["5G 85", "< 详情", "JIX日时间· 2020 00 04 10.00.07", "检查医院:", "影像所见", "审核医生", "肺Ca患者复查：双肺支气管-血管束增", "多，双肺散在多发斑片状、小结节状磨玻璃密度影，气管及叶段支气管通畅。纵隔", "未见明显肿大淋巴结，双侧胸腔少许积液。心包见环形积液征象。左侧腋窝见肿", "大淋巴结，大者短径约17mm。双侧部分", "肋骨、胸椎见斑片状、结节状骨质密度增", "高影。", "影像诊断", "与2026.02.08日老片相比：肺部炎症较", "前稍增多；肺内多发结节（右下肺后基底", "段结节较前稍增大，现直径约13mm，余", "同前相仿），不排除转移瘤；左侧腋窝淋", "巴结较前增大，转移瘤可能。心包积液，", "大致同前；双侧胸腔新见少许积液。双侧", "部分肋骨、胸椎多发骨质病变，大致同", "前。", "相关检查(6)", "查看全部>", "图文报告", "影像浏览", "CS 扫描全能王"]

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
2026-08-10 15:07:57,685 INFO     29 [qwen-vl-text] coord API raw response (len=1632):
```json
[
	{"text": "11:25", "bbox": [273, 27, 338, 44]},
	{"text": ".ll 5G 85", "bbox": [631, 27, 745, 44]},
	{"text": "< 详情", "bbox": [242, 80, 534, 107]},
	{"text": "JIX日时间· 2020 00 04 10.00.07", "bbox": [217, 117, 671, 128]},
	{"text": "检查医院:", "bbox": [217, 148, 351, 170]},
	{"text": "影像所见", "bbox": [217, 212, 360, 235]},
	{"text": "审核医生", "bbox": [555, 212, 668, 235]},
	{"text": "肺Ca患者复查：双肺支气管-血管束增", "bbox": [217, 263, 736, 286]},
	{"text": "多，双肺散在多发斑片状、小结节状磨玻璃密度影，气管及叶段支气管通畅。纵隔", "bbox": [217, 289, 770, 313]},
	{"text": "未见明显肿大淋巴结，双侧胸腔少许积液。心包见环形积液征象。左侧腋窝见肿", "bbox": [217, 342, 770, 365]},
	{"text": "大淋巴结，大者短径约17mm。双侧部分", "bbox": [217, 392, 764, 415]},
	{"text": "肋骨、胸椎见斑片状、结节状骨质密度增", "bbox": [217, 419, 770, 442]},
	{"text": "高影。", "bbox": [217, 445, 292, 468]},
	{"text": "影像诊断", "bbox": [217, 494, 360, 517]},
	{"text": "与2026.02.08日老片相比：肺部炎症较", "bbox": [217, 545, 751, 568]},
	{"text": "前稍增多；肺内多发结节（右下肺后基底", "bbox": [217, 571, 760, 594]},
	{"text": "段结节较前稍增大，现直径约13mm，余", "bbox": [217, 597, 765, 620]},
	{"text": "同前相仿），不排除转移瘤；左侧腋窝淋", "bbox": [217, 623, 751, 646]},
	{"text": "巴结较前增大，转移瘤可能。心包积液，", "bbox": [217, 649, 751, 672]},
	{"text": "大致同前；双侧胸腔新见少许积液。双侧", "bbox": [217, 675, 770, 698]},
	{"text": "部分肋骨、胸椎多发骨质病变，大致同", "bbox": [217, 701, 739, 724]},
	{"text": "前。", "bbox": [217, 727, 260, 750]},
	{"text": "相关检查(6)", "bbox": [229, 790, 410, 814]},
	{"text": "查看全部>", "bbox": [626, 790, 777, 814]},
	{"text": "图文报告", "bbox": [275, 873, 417, 900]},
	{"text": "影像浏览", "bbox": [580, 873, 722, 900]},
	{"text": "CS 扫描全能王", "bbox": [858, 955, 972, 971]},
	{"text": "3亿人都在用的扫描App", "bbox": [858, 974, 972, 984]}
]
```
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=8.2s
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[0]: text=11:25, bbox=[273, 27, 338, 44]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[1]: text=.ll 5G 85, bbox=[631, 27, 745, 44]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[2]: text=< 详情, bbox=[242, 80, 534, 107]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[3]: text=JIX日时间· 2020 00 04 10.00.07, bbox=[217, 117, 671, 128]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[4]: text=检查医院:, bbox=[217, 148, 351, 170]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[5]: text=影像所见, bbox=[217, 212, 360, 235]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[6]: text=审核医生, bbox=[555, 212, 668, 235]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[7]: text=肺Ca患者复查：双肺支气管-血管束增, bbox=[217, 263, 736, 286]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[8]: text=多，双肺散在多发斑片状、小结节状磨玻璃密度影，气管及叶段支气管通畅。纵隔, bbox=[217, 289, 770, 313]
2026-08-10 15:07:57,686 INFO     29 [qwen-vl-text] coord item[9]: text=未见明显肿大淋巴结，双侧胸腔少许积液。心包见环形积液征象。左侧腋窝见肿, bbox=[217, 342, 770, 365]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[10]: text=大淋巴结，大者短径约17mm。双侧部分, bbox=[217, 392, 764, 415]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[11]: text=肋骨、胸椎见斑片状、结节状骨质密度增, bbox=[217, 419, 770, 442]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[12]: text=高影。, bbox=[217, 445, 292, 468]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[13]: text=影像诊断, bbox=[217, 494, 360, 517]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[14]: text=与2026.02.08日老片相比：肺部炎症较, bbox=[217, 545, 751, 568]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[15]: text=前稍增多；肺内多发结节（右下肺后基底, bbox=[217, 571, 760, 594]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[16]: text=段结节较前稍增大，现直径约13mm，余, bbox=[217, 597, 765, 620]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[17]: text=同前相仿），不排除转移瘤；左侧腋窝淋, bbox=[217, 623, 751, 646]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[18]: text=巴结较前增大，转移瘤可能。心包积液，, bbox=[217, 649, 751, 672]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[19]: text=大致同前；双侧胸腔新见少许积液。双侧, bbox=[217, 675, 770, 698]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[20]: text=部分肋骨、胸椎多发骨质病变，大致同, bbox=[217, 701, 739, 724]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[21]: text=前。, bbox=[217, 727, 260, 750]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[22]: text=相关检查(6), bbox=[229, 790, 410, 814]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[23]: text=查看全部>, bbox=[626, 790, 777, 814]
2026-08-10 15:07:57,687 INFO     29 [qwen-vl-text] coord item[24]: text=图文报告, bbox=[275, 873, 417, 900]
2026-08-10 15:07:57,688 INFO     29 [qwen-vl-text] coord item[25]: text=影像浏览, bbox=[580, 873, 722, 900]
2026-08-10 15:07:57,688 INFO     29 [qwen-vl-text] coord item[26]: text=CS 扫描全能王, bbox=[858, 955, 972, 971]
2026-08-10 15:07:57,688 INFO     29 [qwen-vl-text] coord item[27]: text=3亿人都在用的扫描App, bbox=[858, 974, 972, 984]
2026-08-10 15:07:57,688 INFO     29 [qwen-vl-text] page=4 — 26/26 coords, api_time=8.2s
2026-08-10 15:07:57,688 INFO     29 [qwen-vl-text] new_positions (26):
[[4, 162.435, 201.10999999999999, 22.733999999999998, 37.048], [4, 375.445, 443.275, 22.733999999999998, 37.048], [4, 143.98999999999998, 317.72999999999996, 67.36, 90.094], [4, 129.11499999999998, 399.245, 98.514, 107.776], [4, 129.11499999999998, 208.845, 124.616, 143.14], [4, 129.11499999999998, 214.2, 178.504, 197.87], [4, 330.22499999999997, 397.46, 178.504, 197.87], [4, 129.11499999999998, 437.91999999999996, 221.446, 240.81199999999998], [4, 129.11499999999998, 458.15, 243.338, 263.546], [4, 129.11499999999998, 458.15, 287.964, 307.33], [4, 129.11499999999998, 454.58, 330.06399999999996, 349.43], [4, 129.11499999999998, 458.15, 352.798, 372.164], [4, 129.11499999999998, 173.73999999999998, 374.69, 394.056], [4, 129.11499999999998, 214.2, 415.948, 435.31399999999996], [4, 129.11499999999998, 446.84499999999997, 458.89, 478.256], [4, 129.11499999999998, 452.2, 480.782, 500.14799999999997], [4, 129.11499999999998, 455.17499999999995, 502.674, 522.04], [4, 129.11499999999998, 446.84499999999997, 524.566, 543.932], [4, 129.11499999999998, 446.84499999999997, 546.458, 565.824], [4, 129.11499999999998, 458.15, 568.35, 587.716], [4, 129.11499999999998, 439.705, 590.242, 609.608], [4, 129.11499999999998, 154.7, 612.134, 631.5], [4, 136.255, 243.95, 665.18, 685.3879999999999], [4, 372.46999999999997, 462.315, 665.18, 685.3879999999999], [4, 163.625, 248.11499999999998, 735.066, 757.8], [4, 345.09999999999997, 429.59, 735.066, 757.8]]
2026-08-10 15:07:57,689 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=11.5s
2026-08-10 15:07:57,689 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:07:57,691 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:07:57,691 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:07:57,691 INFO     29 [qwen-vl-text] positions(32): [[4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:07:57,691 INFO     29 [qwen-vl-text] page grouping: [4, 5], lines per page: [1, 31]
2026-08-10 15:07:57,872 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:07:58,114 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:07:58,115 INFO     29 [qwen-vl-text] LLM extraction start, text_len=865
2026-08-10 15:07:58,115 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:07:58,115 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 159, \"bbox_end\": 190, \"encounter_dates\": [\"2026-02-08\"], \"department\": \"肿瘤血液科一病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "3亿人都在用的扫描App\n患者处\n性 别: 女 年 龄: 41 岁 登记时间: 2026-02-08 10:17:51\n患者编\n检查号: ZX-1401650 科 别: 肿瘤血液科一病区 床 号: 12034\n检查部位: 胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强\n影像表现:\n肺Ca患者复查: 经肘静脉注入造影剂行增强扫描(造影剂: 碘海醇; 浓度:\n35g/100ml; 速率: 3.0-4.0ml/s; 用量: 1-1.2ml/kg):\n双肺支气管-血管束增多, 双肺散在多发斑片状、小结节状磨玻璃密度影,\n增强扫描强化不明显, 气管及叶段支气管通畅。\n纵隔未见明显肿大淋巴结, 双侧胸腔未见明显积液征象。心包见环形积液征\n象。增强后未见异常强化。左侧腋窝见肿大淋巴结, 大者短径约12mm。\n肝脏形态大小未见异常, 表面光滑, 肝叶比例协调, 肝裂不宽, 肝实质内未\n见异常密度灶, 增强后未见异常强化, 肝内血管走形自然。肝内外胆管无扩张。\n胆囊不大, 壁不厚, 内未见高密度灶, 胰腺大小形态未见异常, 均匀强化。脾不\n大, 质均匀, 增强后均匀强化。双肾形态大小未见异常, 实质密度均匀, 双肾内\n可见结节状高密度影, 肾盂肾盏无扩张, 肾周脂肪间隙清晰, 增强后未见异常强\n化。腹膜后见多发小淋巴结, 增强扫描强化较明显。\n膀胱充盈良好, 壁光整, 未见结节或肿块, 其内未见异常密度影及异常强化\n灶。盆腔未见积液征象, 未见明确肿大淋巴结。\n双侧部分肋骨、腰椎、骨盆见斑片状、结节状骨质密度增高影。\n意见:\n与2025-10-23日老片相比:\n肺部炎症较前增多; 肺内多发结节(右下肺后基底段新增10mm小结节, 余同前相\n仿), 不排除转移瘤; 左侧腋窝淋巴结较前增大, 转移瘤可能。\n心包积液, 大致同前;\n双肾结石。\n双侧部分肋骨、腰椎、骨盆多发骨质病变, 大致同前; 腹膜后多发小淋巴结, 较前相\n报告医师: 常利霞\n审核医师:\n报告时间: 2026-02-08 16:26:10",
    "role": "user"
  }
]
2026-08-10 15:08:04,055 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:08:04,056 INFO     29 [qwen-vl-text] LLM output (len=1048):
{
  "exam_date": "2026-02-08",
  "report_date": "2026-02-08",
  "exam_name": "胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强",
  "exam_category": "imaging",
  "body_part": "胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强",
  "patient_name": null,
  "patient_gender": "女",
  "department": "肿瘤血液科一病区",
  "bed_number": "12034",
  "findings": "肺Ca患者复查: 经肘静脉注入造影剂行增强扫描(造影剂: 碘海醇; 浓度: 35g/100ml; 速率: 3.0-4.0ml/s; 用量: 1-1.2ml/kg):\n双肺支气管-血管束增多, 双肺散在多发斑片状、小结节状磨玻璃密度影, 增强扫描强化不明显, 气管及叶段支气管通畅。\n纵隔未见明显肿大淋巴结, 双侧胸腔未见明显积液征象。心包见环形积液征象。增强后未见异常强化。左侧腋窝见肿大淋巴结, 大者短径约12mm。\n肝脏形态大小未见异常, 表面光滑, 肝叶比例协调, 肝裂不宽, 肝实质内未见异常密度灶, 增强后未见异常强化, 肝内血管走形自然。肝内外胆管无扩张。\n胆囊不大, 壁不厚, 内未见高密度灶, 胰腺大小形态未见异常, 均匀强化。脾不大, 质均匀, 增强后均匀强化。双肾形态大小未见异常, 实质密度均匀, 双肾内可见结节状高密度影, 肾盂肾盏无扩张, 肾周脂肪间隙清晰, 增强后未见异常强化。腹膜后见多发小淋巴结, 增强扫描强化较明显。\n膀胱充盈良好, 壁光整, 未见结节或肿块, 其内未见异常密度影及异常强化灶。盆腔未见积液征象, 未见明确肿大淋巴结。\n双侧部分肋骨、腰椎、骨盆见斑片状、结节状骨质密度增高影。",
  "conclusion": "与2025-10-23日老片相比:\n肺部炎症较前增多; 肺内多发结节(右下肺后基底段新增10mm小结节, 余同前相仿), 不排除转移瘤; 左侧腋窝淋巴结较前增大, 转移瘤可能。\n心包积液, 大致同前;\n双肾结石。\n双侧部分肋骨、腰椎、骨盆多发骨质病变, 大致同前; 腹膜后多发小淋巴结, 较前相",
  "physician": "常利霞",
  "reviewer": null
}
2026-08-10 15:08:04,060 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1029259, prompt_len=627
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["3亿人都在用的扫描App"]

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
2026-08-10 15:08:04,905 INFO     29 [qwen-vl-text] coord API raw response (len=71):
```json
[
	{"text": "3亿人都在用的扫描App", "bbox": [857, 975, 973, 985]}
]
```
2026-08-10 15:08:04,905 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.8s
2026-08-10 15:08:04,906 INFO     29 [qwen-vl-text] coord item[0]: text=3亿人都在用的扫描App, bbox=[857, 975, 973, 985]
2026-08-10 15:08:04,906 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=0.8s
2026-08-10 15:08:04,908 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2053433, prompt_len=1558
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["患者处", "性 别: 女 年 龄: 41 岁 登记时间: 2026-02-08 10:17:51", "患者编", "检查号: ZX-1401650 科 别: 肿瘤血液科一病区 床 号: 12034", "检查部位: 胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强", "影像表现:", "肺Ca患者复查: 经肘静脉注入造影剂行增强扫描(造影剂: 碘海醇; 浓度:", "35g/100ml; 速率: 3.0-4.0ml/s; 用量: 1-1.2ml/kg):", "双肺支气管-血管束增多, 双肺散在多发斑片状、小结节状磨玻璃密度影,", "增强扫描强化不明显, 气管及叶段支气管通畅。", "纵隔未见明显肿大淋巴结, 双侧胸腔未见明显积液征象。心包见环形积液征", "象。增强后未见异常强化。左侧腋窝见肿大淋巴结, 大者短径约12mm。", "肝脏形态大小未见异常, 表面光滑, 肝叶比例协调, 肝裂不宽, 肝实质内未", "见异常密度灶, 增强后未见异常强化, 肝内血管走形自然。肝内外胆管无扩张。", "胆囊不大, 壁不厚, 内未见高密度灶, 胰腺大小形态未见异常, 均匀强化。脾不", "大, 质均匀, 增强后均匀强化。双肾形态大小未见异常, 实质密度均匀, 双肾内", "可见结节状高密度影, 肾盂肾盏无扩张, 肾周脂肪间隙清晰, 增强后未见异常强", "化。腹膜后见多发小淋巴结, 增强扫描强化较明显。", "膀胱充盈良好, 壁光整, 未见结节或肿块, 其内未见异常密度影及异常强化", "灶。盆腔未见积液征象, 未见明确肿大淋巴结。", "双侧部分肋骨、腰椎、骨盆见斑片状、结节状骨质密度增高影。", "意见:", "与2025-10-23日老片相比:", "肺部炎症较前增多; 肺内多发结节(右下肺后基底段新增10mm小结节, 余同前相", "仿), 不排除转移瘤; 左侧腋窝淋巴结较前增大, 转移瘤可能。", "心包积液, 大致同前;", "双肾结石。", "双侧部分肋骨、腰椎、骨盆多发骨质病变, 大致同前; 腹膜后多发小淋巴结, 较前相", "报告医师: 常利霞", "审核医师:", "报告时间: 2026-02-08 16:26:10"]

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
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord API raw response (len=2201):
[
	{"text": "患者处", "bbox": [72, 115, 146, 134]},
	{"text": "性 别: 女 年 龄: 41 岁 登记时间: 2026-02-08 10:17:51", "bbox": [311, 116, 946, 135]},
	{"text": "患者编", "bbox": [72, 151, 146, 169]},
	{"text": "检查号: ZX-1401650 科 别: 肿瘤血液科一病区 床 号: 12034", "bbox": [311, 151, 962, 169]},
	{"text": "检查部位: 胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强", "bbox": [72, 185, 804, 202]},
	{"text": "影像表现:", "bbox": [72, 213, 181, 231]},
	{"text": "肺Ca患者复查: 经肘静脉注入造影剂行增强扫描(造影剂: 碘海醇; 浓度:", "bbox": [125, 235, 930, 254]},
	{"text": "35g/100ml; 速率: 3.0-4.0ml/s; 用量: 1-1.2ml/kg):", "bbox": [72, 257, 699, 276]},
	{"text": "双肺支气管-血管束增多, 双肺散在多发斑片状、小结节状磨玻璃密度影,", "bbox": [125, 279, 918, 298]},
	{"text": "增强扫描强化不明显, 气管及叶段支气管通畅。", "bbox": [72, 301, 583, 320]},
	{"text": "纵隔未见明显肿大淋巴结, 双侧胸腔未见明显积液征象。心包见环形积液征", "bbox": [72, 325, 945, 344]},
	{"text": "象。增强后未见异常强化。左侧腋窝见肿大淋巴结, 大者短径约12mm。", "bbox": [72, 348, 834, 366]},
	{"text": "肝脏形态大小未见异常, 表面光滑, 肝叶比例协调, 肝裂不宽, 肝实质内未", "bbox": [72, 370, 934, 389]},
	{"text": "见异常密度灶, 增强后未见异常强化, 肝内血管走形自然。肝内外胆管无扩张。", "bbox": [72, 392, 930, 411]},
	{"text": "胆囊不大, 壁不厚, 内未见高密度灶, 胰腺大小形态未见异常, 均匀强化。脾不", "bbox": [72, 415, 944, 434]},
	{"text": "大, 质均匀, 增强后均匀强化。双肾形态大小未见异常, 实质密度均匀, 双肾内", "bbox": [72, 438, 942, 457]},
	{"text": "可见结节状高密度影, 肾盂肾盏无扩张, 肾周脂肪间隙清晰, 增强后未见异常强", "bbox": [72, 460, 944, 479]},
	{"text": "化。腹膜后见多发小淋巴结, 增强扫描强化较明显。", "bbox": [72, 483, 633, 502]},
	{"text": "膀胱充盈良好, 壁光整, 未见结节或肿块, 其内未见异常密度影及异常强化", "bbox": [125, 507, 946, 525]},
	{"text": "灶。盆腔未见积液征象, 未见明确肿大淋巴结。", "bbox": [72, 529, 583, 548]},
	{"text": "双侧部分肋骨、腰椎、骨盆见斑片状、结节状骨质密度增高影。", "bbox": [125, 552, 808, 571]},
	{"text": "意见:", "bbox": [72, 657, 131, 675]},
	{"text": "与2025-10-23日老片相比:", "bbox": [119, 680, 379, 698]},
	{"text": "肺部炎症较前增多; 肺内多发结节(右下肺后基底段新增10mm小结节, 余同前相", "bbox": [119, 702, 903, 721]},
	{"text": "仿), 不排除转移瘤; 左侧腋窝淋巴结较前增大, 转移瘤可能。", "bbox": [72, 723, 685, 741]},
	{"text": "心包积液, 大致同前;", "bbox": [119, 744, 329, 762]},
	{"text": "双肾结石。", "bbox": [119, 765, 219, 783]},
	{"text": "双侧部分肋骨、腰椎、骨盆多发骨质病变, 大致同前; 腹膜后多发小淋巴结, 较前相", "bbox": [119, 787, 947, 805]},
	{"text": "报告医师: 常利霞", "bbox": [69, 841, 280, 871]},
	{"text": "审核医师:", "bbox": [373, 843, 594, 870]},
	{"text": "报告时间: 2026-02-08 16:26:10", "bbox": [651, 851, 968, 870]}
]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=14.4s
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[0]: text=患者处, bbox=[72, 115, 146, 134]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[1]: text=性 别: 女 年 龄: 41 岁 登记时间: 2026-02-08 10:17:51, bbox=[311, 116, 946, 135]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[2]: text=患者编, bbox=[72, 151, 146, 169]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[3]: text=检查号: ZX-1401650 科 别: 肿瘤血液科一病区 床 号: 12034, bbox=[311, 151, 962, 169]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[4]: text=检查部位: 胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强, bbox=[72, 185, 804, 202]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[5]: text=影像表现:, bbox=[72, 213, 181, 231]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[6]: text=肺Ca患者复查: 经肘静脉注入造影剂行增强扫描(造影剂: 碘海醇; 浓度:, bbox=[125, 235, 930, 254]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[7]: text=35g/100ml; 速率: 3.0-4.0ml/s; 用量: 1-1.2ml/kg):, bbox=[72, 257, 699, 276]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[8]: text=双肺支气管-血管束增多, 双肺散在多发斑片状、小结节状磨玻璃密度影,, bbox=[125, 279, 918, 298]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[9]: text=增强扫描强化不明显, 气管及叶段支气管通畅。, bbox=[72, 301, 583, 320]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[10]: text=纵隔未见明显肿大淋巴结, 双侧胸腔未见明显积液征象。心包见环形积液征, bbox=[72, 325, 945, 344]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[11]: text=象。增强后未见异常强化。左侧腋窝见肿大淋巴结, 大者短径约12mm。, bbox=[72, 348, 834, 366]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[12]: text=肝脏形态大小未见异常, 表面光滑, 肝叶比例协调, 肝裂不宽, 肝实质内未, bbox=[72, 370, 934, 389]
2026-08-10 15:08:19,303 INFO     29 [qwen-vl-text] coord item[13]: text=见异常密度灶, 增强后未见异常强化, 肝内血管走形自然。肝内外胆管无扩张。, bbox=[72, 392, 930, 411]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[14]: text=胆囊不大, 壁不厚, 内未见高密度灶, 胰腺大小形态未见异常, 均匀强化。脾不, bbox=[72, 415, 944, 434]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[15]: text=大, 质均匀, 增强后均匀强化。双肾形态大小未见异常, 实质密度均匀, 双肾内, bbox=[72, 438, 942, 457]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[16]: text=可见结节状高密度影, 肾盂肾盏无扩张, 肾周脂肪间隙清晰, 增强后未见异常强, bbox=[72, 460, 944, 479]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[17]: text=化。腹膜后见多发小淋巴结, 增强扫描强化较明显。, bbox=[72, 483, 633, 502]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[18]: text=膀胱充盈良好, 壁光整, 未见结节或肿块, 其内未见异常密度影及异常强化, bbox=[125, 507, 946, 525]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[19]: text=灶。盆腔未见积液征象, 未见明确肿大淋巴结。, bbox=[72, 529, 583, 548]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[20]: text=双侧部分肋骨、腰椎、骨盆见斑片状、结节状骨质密度增高影。, bbox=[125, 552, 808, 571]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[21]: text=意见:, bbox=[72, 657, 131, 675]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[22]: text=与2025-10-23日老片相比:, bbox=[119, 680, 379, 698]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[23]: text=肺部炎症较前增多; 肺内多发结节(右下肺后基底段新增10mm小结节, 余同前相, bbox=[119, 702, 903, 721]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[24]: text=仿), 不排除转移瘤; 左侧腋窝淋巴结较前增大, 转移瘤可能。, bbox=[72, 723, 685, 741]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[25]: text=心包积液, 大致同前;, bbox=[119, 744, 329, 762]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[26]: text=双肾结石。, bbox=[119, 765, 219, 783]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[27]: text=双侧部分肋骨、腰椎、骨盆多发骨质病变, 大致同前; 腹膜后多发小淋巴结, 较前相, bbox=[119, 787, 947, 805]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[28]: text=报告医师: 常利霞, bbox=[69, 841, 280, 871]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[29]: text=审核医师:, bbox=[373, 843, 594, 870]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] coord item[30]: text=报告时间: 2026-02-08 16:26:10, bbox=[651, 851, 968, 870]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] page=5 — 31/31 coords, api_time=14.4s
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] new_positions (32):
[[4, 509.91499999999996, 578.935, 820.9499999999999, 829.37], [5, 42.839999999999996, 86.86999999999999, 96.83, 112.828], [5, 185.045, 562.87, 97.672, 113.67], [5, 42.839999999999996, 86.86999999999999, 127.142, 142.298], [5, 185.045, 572.39, 127.142, 142.298], [5, 42.839999999999996, 478.38, 155.76999999999998, 170.084], [5, 42.839999999999996, 107.695, 179.346, 194.50199999999998], [5, 74.375, 553.35, 197.87, 213.868], [5, 42.839999999999996, 415.905, 216.394, 232.392], [5, 74.375, 546.2099999999999, 234.91799999999998, 250.916], [5, 42.839999999999996, 346.885, 253.44199999999998, 269.44], [5, 42.839999999999996, 562.275, 273.65, 289.64799999999997], [5, 42.839999999999996, 496.22999999999996, 293.01599999999996, 308.17199999999997], [5, 42.839999999999996, 555.73, 311.53999999999996, 327.538], [5, 42.839999999999996, 553.35, 330.06399999999996, 346.062], [5, 42.839999999999996, 561.68, 349.43, 365.428], [5, 42.839999999999996, 560.49, 368.796, 384.794], [5, 42.839999999999996, 561.68, 387.32, 403.318], [5, 42.839999999999996, 376.635, 406.686, 422.68399999999997], [5, 74.375, 562.87, 426.894, 442.05], [5, 42.839999999999996, 346.885, 445.418, 461.416], [5, 74.375, 480.76, 464.784, 480.782], [5, 42.839999999999996, 77.945, 553.194, 568.35], [5, 70.80499999999999, 225.505, 572.56, 587.716], [5, 70.80499999999999, 537.285, 591.084, 607.082], [5, 42.839999999999996, 407.575, 608.766, 623.922], [5, 70.80499999999999, 195.755, 626.448, 641.6039999999999], [5, 70.80499999999999, 130.305, 644.13, 659.286], [5, 70.80499999999999, 563.4649999999999, 662.654, 677.81], [5, 41.055, 166.6, 708.122, 733.382], [5, 221.935, 353.43, 709.8059999999999, 732.54], [5, 387.34499999999997, 575.9599999999999, 716.542, 732.54]]
2026-08-10 15:08:19,304 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=2, time=21.6s
2026-08-10 15:08:19,322 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 15:08:19,323 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:08:19,323 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 15:08:19,324 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:08:19.323+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 65, "failed": 0, "current": {"577f370294cc11f1bd9827cf206dfa2d": {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:08:19,336 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:08:19,336 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:08:20,182 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:08:20,189 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 15:08:20,189 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "1992 items", "markdown": "", "text": "", "name": "ZHFE 女(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 2, \"chunks_LabExam\": 1}"}
2026-08-10 15:08:20,189 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 15:08:20,190 INFO     29 [ChunkMerger] Merged 5 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 15:08:20,204 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 15:08:20,204 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "5 items, types={'LabReport': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 2}", "name": "ZHFE 女(1).pdf"}
2026-08-10 15:08:20,204 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 15:08:20,337 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786374079144, 'update_date': datetime.datetime(2026, 8, 10, 15, 1, 19), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1129542, 'status': '1'}
2026-08-10 15:08:20,557 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   谷丙转氨酶  ALT  26.0  U/L  0~40.0  False    谷草转氨酶  AST  35.0  U/L  0~40.0  False    谷草谷丙比  AST/ALT  1.35  None  0.80~1.68  False    谷氨酰氨基转  GGT  52.0  U/L  0.0~50.0  True    总蛋白  TP  69.5  g/L  60~83  False    白蛋白  ALB  42.4  g/L  35~55.0  False    球蛋白  GLD  27.1  g/L  20.0~35.0  False    白/球蛋白  A/G  1.56  None  1.00~2.50  False    总胆汁酸  TBA  2.8  umol/L  0.0~12.0  False    总胆红素  TBIL  7.4  umol/L  3.4~17.1  False    直接胆红素  DBIL  1.9  umol/L  0.0~7.1  False    间接胆红素  IBIL  5.5  umol/L  0.0~16.0  False    尿素氮  None  4.04  mmol/L  2.90~7.10  False    肌酐  None  66.0  umol/L  40~79.6  False    尿酸  UA  314.7  umol/L  90.0~423.0  False    葡萄糖  GLU  5.60  mmol/L  3.90~6.10  False    甘油三酯  TG  3.18  mmol/L  0.23~1.69  True    总胆固醇  CHOL  7.37  mmol/L  2.8~5.50  True    低密度脂蛋白胆固醇  None  5.30  None  None  False    乳酸脱氢酶  LDH  217  None  None  False    肌红蛋白  MYO  45  None  None  False    钾  K  4.25  None  None  False    钠  Na  141.0  None  None  False    氯  CL  102.0  None  None  False    钙  Ca  2.51  None  None  False    超敏C反应蛋白  None  1.48  mg/L  0.0~10.0  False    白细胞  WBC  4.7  10^9/L  3.5~9.5  False    红细胞  RBC  3.70  10^12/L  3.8~5.1  True    血红蛋白  HGB  120.0  g/L  115~150  False    血小板  PLT  207.0  10^9/L  125~350  False    中性细胞数  NEU  2.4  10^9/L  1.8~6.3  False    嗜酸性粒细胞  EOS  0.070  10^9/L  0.02~0.52  False    嗜碱性粒细胞  BASO  0.010  10^9/L  0.000~0.06  False    淋巴细胞数  LYM  1.54  10^9/L  1.1~3.2  False    单核细胞  MONO  0.63  10^9/L  0.1~0.6  True    中性细胞比率  NEU%  51.8  %  40~75  False    淋巴细胞比率  LYM%  33  %  20~50  False    单核细胞比率  MONO%  13.5  %  3.0~10  True    嗜碱细胞比率  BASO%  0.2  %  0.0~1.0  False    嗜酸细胞比率  EOS%  1.5  %  0.4~8  False    红细胞压积  HCT  37.70  %  35~45  False    红细胞平均体积  MCV  101.9  fL  82.0~100  True    平均血红蛋白量  MCH  32.4  pg  27.0~34  False    平均血红蛋白浓度  MCHC  318  g/L  316~354  False    血小板比积  PCT  0.210  None  0.108~0.272  False    平均血小板体积  MPV  9.90  fL  9.00~13.00  False    血小板分布宽度  PDW  10.8  None  15.0~18.0  True    RBC分布宽度  RDW-SD  56.80  fL  37.00~50.00  True    大型PLT比率  P-LCR  24.20  %  13.00~43.00  False    红细胞分布宽度系数  None  15  %  None  False    癌胚抗原(新仪器)  None  23.75  None  None  True    糖类抗原125(新仪器)  None  240.15  None  None  True    糖类抗原153(新仪器)  None  16.42  None  None  False    细胞角蛋白19片段(新仪器)  None  3.39  None  None  False   
---
入院时间:2026年03月04日09时20分 出院时间:2026年03月07日10时00分 住院天数:3天
X线号:-
CT号:-
MRI号:-
入院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸
腔积液 4.肺部感染?
入院情况:确诊肺腺癌8个月余。体格检查:四测正常,神志清楚,自动体位,慢性病容。皮肤
巩膜无黄染,全身未扪及明显肿大淋巴结,气管居中。颈软,胸廓对称,双肺语颤正常,叩诊双肺呈
清音,听诊双肺呼吸音低,未闻及明显罗音。心音清晰,心律齐无杂音。腹平软,全腹无压痛反跳
痛,肝脾肋下未扪及,肝肾区无叩痛,移动性浊音阴性,肠鸣音正常。双下肢无浮肿。四肢肌力、肌
张力正常。生理反射正常,病理征阴性。
诊治经过:完善相关检查:CA125+CEA+3CA153+4CYFRA211:*癌胚抗原(新仪器)
23.75ng/ml,*糖类抗原125(新仪器) 240.15U/ml;血脂:甘油三酯3.18mmol/L,总胆固醇
7.37mmol/L;肝肾功能、电解质、空腹血糖、心肌酶、血常规正常。胸部平扫:与2026.02.08日老片
相比:肺部炎症较前稍增多;肺内多发结节(右下肺后基底段结节较前稍增大,现直径约13mm,
余同前相仿),不排除转移瘤;左侧腋窝淋巴结较前增大,转移瘤可能。心包积液,大致同前;双侧
胸腔新见少许积液。双侧部分肋骨、胸椎多发骨转移。评估为PD,部分进展,与家属商榷后于3月6
日继续予以贝伐珠单抗联合PCb化疗联合治疗(贝伐珠单抗800mg+培美曲塞860mg+卡铂
600mg),现治疗完成予以办理出院。
出院情况:患者偶有干咳。
出院诊断:1.原发支气管肺腺癌 cTxNxM1 IVb期 骨转移、双肺、心包转移 2.心包积液 3.胸
腔积液
出院医嘱:1、注意休息,加强营养,多饮白开水。
2、定期于肿瘤内科门诊(门诊3楼)复查血常规,出院后3天内复查,以后每5-7天复
查至少一次,如果血常规白细胞低于4*10^9/L,立即返院予以重组人粒细胞集落刺激因子注射
200ug/次皮下注射1次/天,用药后隔天复查;如果血常规血小板低于75*109/L,立即返院就诊,
遵医嘱用药;
3、院外巩固治疗,不适随诊。
11:25
---
姓名：
性别：女
年龄：41岁
婚 姻：已婚
联系电话：
出生
民族：汉族
职业：职工
住址
电子邮件(E_mail)：无
入院时间：2026年03月04日 09时20分
记录时间：2026年03月04日 10时56分
病史陈述者：患者本人
入院方式：步行
主诉：确诊肺腺癌8个月余。
现病史：患者自诉2025年6月开始无明显诱因出现活动后气促，为求治疗在
就诊，完善检查：（左侧颈部淋巴结）HE结合免疫组化符合转移性腺癌，倾向肺来源可能性大，
请完善相关检查后综合考虑。IHC：GATA-3(-)，P16(-)，CK7(+)，ER(-).PR(-)，CK20(-)，Pax-
8(-)，TTF-1(+)，NapsinA(+)，CerbB-2(1+)，Villin(+)，Ki-67(热点区约50%+)。PETCT：1.双肺
散在斑片影及磨玻璃影，糖代谢增高，双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹
主动脉旁多发肿大淋巴结，糖代谢增高，脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增
高，上述考虑恶性肿瘤（肺CA？）并淋巴结、骨转移可能，建议结合病理。2.双侧胸腔积液，双下
肺膨胀不全。3.心包积液，盆腔少量积液。4.双肾小结石。5.双侧卵巢囊性灶，糖代谢增高，考虑生
理性改变。诊断考虑为“左上肺腺癌广泛转移”，行化疗前准备（叶酸+维生素B12），于6月13日
出院。
2025年6月14日为求治疗入我科，于6月16日完善基因检测，于6月18日予以PCb+贝伐珠单抗
联合治疗第1周期（培美曲塞785mg+卡铂600mg+贝伐珠单抗800mg），同时予以护胃、止呕等对症
治疗，患者治疗完成予以办理出院。
出院后患者诉气促好转，基因检测报告：BRAF（p.K601E），MET扩增，PDL1 TPS表达55%。
2025年7月9日再入院，予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂
650mg+贝伐珠单抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，于7月12日予以地
舒单抗120mg护骨治疗，复查血常规正常于7月12日出院。
出院后患者气促明显缓解，2025年7月30日为求治疗再入院，完善检查：肝肾功能、电解质、
心肌酶、血常规正常。纵隔及心脏平扫及增强|肺部平扫及增强|上腹部平扫及增强|下腹部平扫
及增强|盆腔平扫及增强CT：肺部炎症，合并多发占位可能；心包积液；双侧部分肋骨、腰椎多发骨
质病变，腹膜后多发小淋巴结，结合病史考虑转移。疗效评估为PR，于7月31日、8月23日、9月9日、
10月02日予以PCb+贝伐珠单抗+替雷利珠单抗联合治疗（培美曲塞785mg+卡铂650mg+贝伐珠单
抗800mg+替雷利珠200mg），同时予以护胃、止呕等对症治疗，期间规律予以地舒单抗护骨治疗，
患者治疗完成10月05日出院。
2025年10月23日为求治疗再入院，完善相关检查：胸部平扫及增强|上腹部平扫及增强|下
腹部平扫及增强|盆腔平扫及增强：与07-30老片相比：肺部炎症较前吸收，考虑肺内转移病灶，
较前大致相仿；心包积液，较前稍吸收；双肾结石。双侧部分肋骨、腰椎多发骨质病变，似较前稍微
增多；腹膜后多发小淋巴结，较前相仿；结合病史考虑转移。评估为SD，继续予以贝伐珠单抗
800mg+替雷利珠单抗200mg维持治疗，同时予以降血脂治疗，2025年10月25日予以办理出院。
2025年11月14日、12月4日返院继续治疗，因患者偶有痰中带血，停贝伐珠单抗，予以替雷禾
第 1 页
珠单抗200mg维持治疗。
2025年12月25日为求治疗再入院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部
平扫及增强|盆腔平扫及增强：与10-23老片相比：肺部炎症较前稍进展，考虑肺内转移病灶，较
前大致相仿；心包积液，较前稍增多；双肾结石。双侧部分肋骨、腰椎多发骨质病变，较前相仿；腹
膜后多发小淋巴结，较前稍微增大；左侧腋窝稍大淋巴结；结合病史考虑转移。评估为SD，免疫性
肺炎不排除，参考中科院专家会诊意见，于2025年12月27日予以贝伐珠单抗联合PCb化疗联合治
疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完成12月
30日办理出院。
2026年1月17日为求治疗再入院，完善检查，于2026年1月19日予以贝伐珠单抗联合PCb化疗
联合治疗（贝伐珠单抗800mg+培美曲塞860mg+卡铂600mg），同时予以地舒单抗护骨，现治疗完
成1月20日办理出院。
2026年2月8日再次返院，完善检查：胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增
强|盆腔平扫及增强CT：与2025-10-23日老片相比：肺部炎症较前增多；肺内多发结节（右下肺
后基底段新增10mm小结节，余同前相仿），不排除转移瘤；左侧腋窝淋巴结较前增大，转移瘤可
能。心包积液，大致同前；双肾结石。双侧部分肋骨、腰椎、骨盆多发骨质病变，大致同前。本次复查
增强CT，对比2025-12片，疗效评价SD，建议继续贝伐珠单抗+培美曲塞+卡铂联合治疗，患者因过
年要求暂缓化疗，于2026-02-12予以贝伐珠单抗800mg靶向治疗。治疗上予以抗感染、清热解毒、
化痰止咳等对症治疗后于2月14日出院。
今患者为求继续治疗在我院门诊就诊，门诊以“肺恶性肿瘤”收住我科，此次发病期间，患
者精神食欲睡眠可，大小便正常，体重无明显变化。
既往史：个人史、月经及婚育史、家族史见第一次入院记录。
体格检查
T：36.5℃ P：85次/分 R：19次/分 BP：100/78mmHg
发育正常，营养中等，自主体位，神志清楚，查体合作。粘膜无发绀、黄染、苍白，无皮疹。未见
皮下出血。皮肤湿度正常，弹性正常，无肝掌，未见蜘蛛痣。左侧腋下可触及大小约1*1cm的肿大淋
巴结，活动度差，质地韧，无明显压痛，边界不清晰。头颅外形正常。眼：眼睑正常，眼球无凸出及
凹陷，结膜正常。巩膜无黄染，双侧瞳孔等大等圆，瞳孔直径3.0mm，对光反射及调节均灵敏。耳：
双耳耳廓外形正常，无畸形，双侧无乳突压痛，外耳道通畅，无分泌物。鼻外形正常，鼻中隔无偏
曲，上颌窦与额窦无压痛，无鼻塞，无分泌物。口腔：口唇红润，伸舌居中，双侧扁桃体无肿大，表
面未见脓点，咽无充血，声音嘶哑。颈软，无抵抗感，气管居中，颈静脉充盈正常，肝颈静脉回流征
阴性，颈动脉搏动正常，甲状腺未触及肿大。胸廓正常，肋间隙正常，胸壁无压痛，无胸骨叩痛。呼
吸节律正常，语颤正常，双肺未触及胸膜摩擦感，未触及皮下捻发感。胸廓对称，双肺语颤正常，叩
诊双肺呈清音，听诊双肺呼吸音低，未闻及明显罗音。心前区无隆起，可见心尖搏动，心尖搏动位
于第5肋间左锁骨中线内0.5cm，心前区无异常搏动。心尖搏动触不清，未触及震颤，无心包摩擦
感。心界不大。心率：85次/分，律齐，心音清。各瓣膜听诊区未闻及病理性杂音，不可闻及额外心
音，未闻及心包摩擦音。周围血管征阴性。腹部平坦，未见胃肠型及蠕动波。未见静脉曲张，脐部正
常。腹部柔软，无液波震颤，未触及腹部肿块。全腹无压痛、无反跳痛，无肌紧张。肝、脾脏未触及
肾未触及。肝浊音界存在，肝上界位于右锁骨中线第5肋间，移动性浊音阴性，双肾区无叩痛。肠
音正常，无气过水声，无震水音，未闻及腹部血管杂音。肛门、直肠及外生殖器：正常。脊柱正常
第 2 页
号 A1687966
理弯曲,活动自如,无压痛及叩击痛。四肢活动自如,关节无红肿,活动自如,皮温正常。无杵状指、
趾,双下肢无水肿。腹壁反射存在,双侧跟腱反射正常,四肢肌力及肌张力正常,双侧巴彬斯征、
布鲁金斯基征、克匿格征阴性。
辅助检查结果:2025年6月湘潭市中心医院PETCT:1.双肺散在斑片影及磨玻璃影,糖代谢增
高,双侧锁骨区、双侧腋窝、心膈角、纵膈、双侧肺门、胰腺后、腹主动脉旁多发肿大淋巴结,糖代谢
增高,脊柱多个椎体及附件、部分肋骨、骨盆骨糖代谢局部增高,上述考虑恶性肿瘤(肺CA?)并
淋巴结、骨转移可能,建议结合病理。2.双侧胸腔积液,双下肺膨胀不全。3.心包积液,盆腔少量积
液。4.双肾小结石。5.双侧卵巢囊性灶,糖代谢增高,考虑生理性改变。
2025年6月湘潭市中心医院病理:(左侧颈部淋巴结)HE结合免疫组化符合转移性腺癌,倾
向肺来源可能性大,请完善相关检查后综合考虑。IHC:GATA-3(-),P16(-),CK7(+),ER(-).
PR(-),CK20(-),Pax-8(-),TTF-1(+),NapsinA(+),CerbB-2(1+),Villin(+),Ki-67(热点区约
50%+)。
心肌酶正常,CA125 372U/ml。
2025年7月基因检测报告: BRAF(p.K601E),MET扩增,PDL1 TPS表达55%。
入院诊断:1.肺腺癌 cTxNxM1 IVb期 骨转移、双
肺、心包转移2.胸腔积液3.心包积液4.肺部感染?
医生签名
---
5G 85
< 详情
JIX日时间· 2020 00 04 10.00.07
检查医院:
影像所见
审核医生
肺Ca患者复查：双肺支气管-血管束增
多，双肺散在多发斑片状、小结节状磨玻璃密度影，气管及叶段支气管通畅。纵隔
未见明显肿大淋巴结，双侧胸腔少许积液。心包见环形积液征象。左侧腋窝见肿
大淋巴结，大者短径约17mm。双侧部分
肋骨、胸椎见斑片状、结节状骨质密度增
高影。
影像诊断
与2026.02.08日老片相比：肺部炎症较
前稍增多；肺内多发结节（右下肺后基底
段结节较前稍增大，现直径约13mm，余
同前相仿），不排除转移瘤；左侧腋窝淋
巴结较前增大，转移瘤可能。心包积液，
大致同前；双侧胸腔新见少许积液。双侧
部分肋骨、胸椎多发骨质病变，大致同
前。
相关检查(6)
查看全部>
图文报告
影像浏览
CS 扫描全能王
---
3亿人都在用的扫描App
患者处
性 别: 女 年 龄: 41 岁 登记时间: 2026-02-08 10:17:51
患者编
检查号: ZX-1401650 科 别: 肿瘤血液科一病区 床 号: 12034
检查部位: 胸部平扫及增强|上腹部平扫及增强|下腹部平扫及增强|盆腔平扫及增强
影像表现:
肺Ca患者复查: 经肘静脉注入造影剂行增强扫描(造影剂: 碘海醇; 浓度:
35g/100ml; 速率: 3.0-4.0ml/s; 用量: 1-1.2ml/kg):
双肺支气管-血管束增多, 双肺散在多发斑片状、小结节状磨玻璃密度影,
增强扫描强化不明显, 气管及叶段支气管通畅。
纵隔未见明显肿大淋巴结, 双侧胸腔未见明显积液征象。心包见环形积液征
象。增强后未见异常强化。左侧腋窝见肿大淋巴结, 大者短径约12mm。
肝脏形态大小未见异常, 表面光滑, 肝叶比例协调, 肝裂不宽, 肝实质内未
见异常密度灶, 增强后未见异常强化, 肝内血管走形自然。肝内外胆管无扩张。
胆囊不大, 壁不厚, 内未见高密度灶, 胰腺大小形态未见异常, 均匀强化。脾不
大, 质均匀, 增强后均匀强化。双肾形态大小未见异常, 实质密度均匀, 双肾内
可见结节状高密度影, 肾盂肾盏无扩张, 肾周脂肪间隙清晰, 增强后未见异常强
化。腹膜后见多发小淋巴结, 增强扫描强化较明显。
膀胱充盈良好, 壁光整, 未见结节或肿块, 其内未见异常密度影及异常强化
灶。盆腔未见积液征象, 未见明确肿大淋巴结。
双侧部分肋骨、腰椎、骨盆见斑片状、结节状骨质密度增高影。
意见:
与2025-10-23日老片相比:
肺部炎症较前增多; 肺内多发结节(右下肺后基底段新增10mm小结节, 余同前相
仿), 不排除转移瘤; 左侧腋窝淋巴结较前增大, 转移瘤可能。
心包积液, 大致同前;
双肾结石。
双侧部分肋骨、腰椎、骨盆多发骨质病变, 大致同前; 腹膜后多发小淋巴结, 较前相
报告医师: 常利霞
审核医师:
报告时间: 2026-02-08 16:26:10
2026-08-10 15:08:21,170 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 15:08:21,171 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "5 items, types={'LabReport': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 2}", "name": "ZHFE 女(1).pdf", "embedding_token_consumption": 6387}
2026-08-10 15:08:21,171 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 15:08:21,343 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 15:08:21,343 INFO     29 [Trace] task=577f3702 | doc=ZHFE 女(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":5,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 15:08:21,346 INFO     29 [DIAG-EXECUTOR] row_position_int len=54 row[0]=(7, 189, 266, 49, 64) row[-1]=(9, 30, 343, 232, 258)
2026-08-10 15:08:21,346 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:08:21,346 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:08:21,346 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:08:21,347 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:08:21,353 INFO     29 set_progress(577f370294cc11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 15:08:21 [DOC Engine]:
Start to index...
2026-08-10 15:08:21,375 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 15:08:21,379 INFO     29 set_progress(577f370294cc11f1bd9827cf206dfa2d), progress: 0.8200000000000001, progress_msg: 
2026-08-10 15:08:21,400 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-10 15:08:21,407 INFO     29 set_progress(577f370294cc11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 15:08:21 Indexing done (0.06s). Task done (399.68s)
2026-08-10 15:08:21,414 INFO     29 [Done], chunks(5), token(6387), elapsed:399.68
2026-08-10 15:08:21,654 INFO     29 handle_task done for task {"id": "577f370294cc11f1bd9827cf206dfa2d", "doc_id": "5739903094cc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "ZHFE \u5973(1).pdf", "type": "pdf", "location": "ZHFE \u5973(1).pdf", "size": 2362516, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786374078743, "task_type": "dataflow", "root_trace_id": "c620a8a58f2a4074a8683018c17588f5", "root_traceparent": "00-c620a8a58f2a4074a8683018c17588f5-c936535a5900f4d3-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
