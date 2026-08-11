# 基准结果：BJCA,男，49，肺鳞癌一线(1).pdf

## 基本信息

- 文件：`BJCA,男，49，肺鳞癌一线(1).pdf`
- 大小：14180.7 KB
- PDF 总页数：14
- doc_id：`14840e4e94f111f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T03:24:16  完成时间：2026-08-11T03:34:05  耗时：589.6s
- progress_msg：`19:34:04 Indexing done (0.07s). Task done (542.00s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 4fce37f2 | 3 | 1-3 | 姓名 住址：福建省三明市尤溪县 性别：男 工作单位：/ 年龄：49岁 入院日期： |
| 2 | 018628e9 | 1 | 4-4 | 测量结果: Lved:46.5 mm Lve5:28.9 mm La:26.6  |
| 3 | 49057c88 | 1 | 5-5 | 性别：男 年龄：49岁 门诊号： 检查部位：肺部 检查设备：GE-HD750 流 |
| 4 | 89841050 | 1 | 6-6 | 门诊号: 医院: 申请医生 申请科室 检查日期: 2026-03-17 10:5 |
| 5 | 453ee80c | 1 | 7-7 | 检查部位：头颅 检查设备：飞利浦MR9 流水号：0013240580 检查技术： |
| 6 | a2505c7f | 1 | 12-12 | 病案号: 11诊号:1K3392539b3 血型:FEI/CI独/业冰(111) |
| 7 | 53186590 | 1 | 13-13 | 福建医科大学附属协和医院 肺功能检查报告单 姓名： 性别：男 年龄：49 Yea |
| 8 | 533ca2fb | 1 | 14-14 | 姓 住院 性别：男 年龄：40岁 送检单位：本院 送检科室：呼吸与危重症医学科  |
| 9 | e973753a | 1 | 9-9 | <table><tr><td>总胆红素</td><td>TBIL</td><td |
| 10 | f651f2ea | 1 | 8-8 | <table><tr><td>乙肝病毒表面抗原</td><td>None</td |
| 11 | 1467a5fe | 1 | 9-9 | <table><tr><td>尿素</td><td>UREA</td><td>4 |
| 12 | 06ff8d75 | 1 | 10-10 | <table><tr><td>白细胞计数</td><td>None</td><t |
| 13 | fa1b16ce | 1 | 11-11 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |

- chunks 总数：13
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / 14；缺失页：`[]`
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
| ExaminationReport | 检查报告 | 7 | 7 | 7 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 5 | 0 | 5 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "ExaminationReport": 7, "LabReport": 5}`
- ChunkMerger：`{"found": true, "merged": 13, "sources": 9, "stats": {"Extractor:LabExam": 5, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 7, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：2 条
  - `[no_text_noise] 2026-08-10 19:28:45,254 INFO     29 [ChunkMerger] Merged 33 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 9, 'Extractor:Medication': 1, 'Extractor:Presc`
  - `[no_text_noise] 2026-08-10 19:34:02,687 INFO     29 [ChunkMerger] Merged 13 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 19:24:20,985 INFO     29 handle_task begin for task {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 19:24:21,206 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 19:24:21,355 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 19:24:21,657 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:24:21,657 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 19:24:21,657 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 19:24:21,663 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 19:24:21,663 INFO     29 ============================================================
2026-08-10 19:24:21,663 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 19:24:21,663 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 19:24:21,663 INFO     29 ============================================================
2026-08-10 19:24:21,663 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 19:24:21,663 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 19:24:21,665 INFO     29 No torch found.
2026-08-10 19:24:23,200 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=14
2026-08-10 19:24:23,353 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1290712, prompt_len=764
2026-08-10 19:24:24,655 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 19:24:24,656 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 19:24:24,663 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1290712, prompt_len=401
2026-08-10 19:24:29,913 INFO     29 [qwen-vl-parser] text API response (len=948):
["姓名", "住址：福建省三明市尤溪县", "性别：男", "工作单位：/", "年龄：49岁", "入院日期：2026.03.16 10:21:29", "婚姻：已婚", "记录时间：2026.03.16 10:21:29", "民族：汉族", "病史陈述者：患者及家属", "出生地：福建省三明市", "病史可靠程度：基本可靠", "职业(工种)：/", "过敏史：未发现", "主诉：确诊左下肺鳞癌4天。", "现病史：缘于2026.03.05以“咳嗽、咳痰1月”就诊于尤溪县总医院，查“2026.03.06胸部", "增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。”", "于2026.03.09行“支气管镜检查+支气管粘膜活检术”，术顺，术后病理示：（左肺下叶粘", "膜组织）浸润性鳞状细胞癌。", "予抗感染、止咳、化痰后咳嗽、咳痰好转，", "无头晕、头痛，无胸闷、胸痛，无畏冷、发热，无心悸、呼吸困难，无乏力、盗汗，无腹胀、腹痛，", "无恶心、呕吐，无声音嘶哑、吞咽困难等不适。今为进一步诊治就诊我科，门诊拟“左下肺腺", "癌”收治入院，自发病以来，精神、食欲、睡眠尚可，大、小便正常，体重近期未见明显增减。", "既往史：平素身体健康，否认高血压，否认糖尿病，否认冠心病，否认肝炎、结核、菌痢、伤寒", "等传染病史，否认其他手术史，否认输血史，否认外伤史，否认药物过敏史，预防接种按时完成。", "个人史：生于原籍，否认长期外地居住史，否认疫区居留史，否认特殊化学品及放射线接触", "史。有吸烟史20余年，否认饮酒。否认冶游史。", "婚育史：已婚已育，配偶及孩子均体健。", "家族史：父已故，母健在。其父有肺癌史。否认家族中有“肝炎、伤寒、结核”等传染病史，否", "认家族中有其他遗传性疾病史。", "体格检查", "T:36.5℃", "P:79次/分", "R:19次/分", "BP:112/69mmHg", "一般情况：神志清楚，发育正常，营养良好，体型正常，正常面容，表情安静，自动体位，查", "体合作，对答切题，步行入院。", "第1页"]
2026-08-10 19:24:29,914 INFO     29 [qwen-vl-parser] page=1 text: 38 lines (bbox 0-37)
2026-08-10 19:24:29,915 INFO     29 [qwen-vl-parser] page=1 text: 38 sections
2026-08-10 19:24:30,081 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1325777, prompt_len=764
2026-08-10 19:24:30,117 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:24:30,117 INFO     29 [qwen-vl-text] LLM output (len=698):
{
  "exam_date": "2024-06-19",
  "report_date": "2024-06-21",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "肺",
  "patient_name": "夕",
  "patient_gender": "女",
  "department": "胸外科",
  "bed_number": "1-",
  "findings": "肿瘤分级：低分化。\n肿瘤数量：1个。\n脉管内癌栓：脉管内见癌栓。\n神经侵犯：神经未见癌组织侵犯。\n沿气道播散STAS：查见STAS。\n胸膜侵犯：侵及壁层胸膜，PL3(改进Hammar分级)。\n切缘情况：支气管断端及肺切缘均未见癌。\n周围肺情况：周围肺组织示炭末沉积及细支气管化生。\n支气管周围淋巴结：查见支气管周围淋巴结（0/1）枚，未见癌组织转移。\n送检淋巴结：送检\"第7组\"淋巴结（0/1）枚，\"第10组\"淋巴结（0/1）枚，\"第11组\"淋巴结（0/1）枚，\"第12组\"淋巴结（0/1）枚，未见癌组织转移。",
  "conclusion": "免疫组化：1#TTF-1/弹力纤维（+）；\n3#TTF-1（+）；\n8#TTF-1（+），P40（+）；\n10#TTF-1/弹力纤维（+）；\n11#TTF-1/弹力纤维（+），P40（-）。\n特殊染色：8#六胺银染色（-）。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:24:30,118 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=880194, prompt_len=1167
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["病理诊断报告单", "病理号", "姓名：夕", "性别：女 年龄：67岁 科室病区", "送检医院：188.8.15", "病. 1067375 床号：1-", "收到日期：2024-06-19 门诊号：", "报告日期：2024-06-21", "肿瘤分级：低分化。", "肿瘤数量：1个。", "脉管内癌栓：脉管内见癌栓。", "神经侵犯：神经未见癌组织侵犯。", "沿气道播散STAS：查见STAS。", "胸膜侵犯：侵及壁层胸膜，PL3(改进Hammar分级)。", "切缘情况：支气管断端及肺切缘均未见癌。", "周围肺情况：周围肺组织示炭末沉积及细支气管化生。", "支气管周围淋巴结：查见支气管周围淋巴结（0/1）枚，未见癌组织转移。", "送检淋巴结：送检\"第7组\"淋巴结（0/1）枚，\"第10组\"淋巴结（0/1）枚，\"第11组\"淋巴", "结（0/1）枚，\"第12组\"淋巴结（0/1）枚，未见癌组织转移。", "免疫组化：1#TTF-1/弹力纤维（+）；", "3#TTF-1（+）；", "8#TTF-1（+），P40（+）；", "10#TTF-1/弹力纤维（+）；", "11#TTF-1/弹力纤维（+），P40（-）。", "特殊染色：8#六胺银染色（-）。"]

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
2026-08-10 19:24:32,012 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 19:24:32,013 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 19:24:32,032 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1325777, prompt_len=401
2026-08-10 19:24:38,951 INFO     29 [qwen-vl-parser] text API response (len=973):
["皮肤粘膜：色泽正常，未见黄染，未见紫绀，未见色素沉着，未见皮疹，未见皮下出血。皮温", "正常，湿度正常，弹性好，无水肿，未见肝掌，未见蜘蛛痣。", "淋巴结：全身浅表淋巴结未触及。", "头颅：大小正常，形状正常，头发分布正常，眼睑无浮肿，眼球无异常，巩膜无黄染，结膜正", "常，角膜透明，瞳孔等大等圆，直径3mm，对光反射灵敏。耳廓无畸形，外耳道正常，无异常分泌", "物，听力正常，无乳突压痛。双侧鼻唇沟对称，鼻中隔无偏曲，鼻腔通气畅，无副鼻窦区压痛。口", "唇无紫绀，口腔粘膜完整，口腔无异味，伸舌居中，咽无充血，扁桃体无肿大，无脓点。", "颈部：颈柔软，颈静脉无怒张，肝颈静脉回流征阴性，未见颈动脉异常搏动，气管居中，甲", "状腺无肿大，无血管杂音。", "胸部：胸廓无畸形，胸壁静脉未见，无皮下气肿，肋间隙正常。胸骨无压痛，胸廓挤压征阴", "性，无男乳女化。", "肺部：双侧呼吸运动匀称，双侧触觉语颤对称，叩诊音清，呼吸音清，未闻及干湿罗音，未", "闻及胸膜摩擦音。", "心脏：无心前区隆起，心尖搏动正常，位于第Ⅴ肋间，左锁骨中线内0.5cm处，未扪及震颤", "及抬举样搏动，心界叩诊无扩大，心音清晰，心率79次/分，节律整齐，A2>P2，无杂音。心浊音界", "大小如下图所示：", "右(CM) 肋间 左(CM)", "2 Ⅱ 2", "2 Ⅲ 3.5", "3 Ⅳ 5.5", "Ⅴ 8.0", "注：左锁骨中线距前正中线8.5CM。", "周围血管：脉率79次/分，节律整齐，无脉搏短绌，无奇脉，无交替脉，无毛细血管搏动征，", "无Duroziez二重杂音，无大血管枪击音，无水冲脉。双侧足背动脉及桡动脉搏动良好对称。", "腹部：腹平坦，呼吸运动自如，腹壁静脉未见怒张，腹壁皮肤无皮疹，无色素沉着，无腹纹，", "无疤痕，无疝，未见胃肠型及蠕动波，无上腹部搏动。全腹软，无肌紧张，无压痛及反跳痛，未触", "及包块，肝脏右肋下、剑突下未触及，胆囊未触及，莫菲氏征阴性，脾脏左肋下未触及，双肾未触", "及，双侧输尿管径路无压痛，无液波震颤。鼓音，肝上界位于右锁骨中线上第Ⅳ肋间，肝区无叩", "击痛，胃泡鼓音区存在，肾区无叩痛，移动性浊音阴性。肠鸣音正常，4次/分，未闻及振水音及血", "第2页"]
2026-08-10 19:24:38,952 INFO     29 [qwen-vl-parser] page=2 text: 30 lines (bbox 38-67)
2026-08-10 19:24:38,952 INFO     29 [qwen-vl-parser] page=2 text: 30 sections
2026-08-10 19:24:39,065 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=708246, prompt_len=764
2026-08-10 19:24:40,336 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 19:24:40,336 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 19:24:40,347 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=708246, prompt_len=401
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord API raw response (len=1578):
[
	{"text": "病理诊断报告单", "bbox": [345, 83, 655, 115]},
	{"text": "病理号", "bbox": [658, 121, 730, 139]},
	{"text": "姓名：夕", "bbox": [69, 153, 140, 169]},
	{"text": "性别：女 年龄：67岁 科室病区", "bbox": [343, 153, 641, 169]},
	{"text": "送检医院：188.8.15", "bbox": [69, 178, 340, 198]},
	{"text": "病. 1067375 床号：1-", "bbox": [561, 178, 877, 198]},
	{"text": "收到日期：2024-06-19 门诊号：", "bbox": [70, 204, 413, 220]},
	{"text": "报告日期：2024-06-21", "bbox": [561, 204, 768, 220]},
	{"text": "肿瘤分级：低分化。", "bbox": [132, 232, 315, 248]},
	{"text": "肿瘤数量：1个。", "bbox": [132, 248, 284, 264]},
	{"text": "脉管内癌栓：脉管内见癌栓。", "bbox": [132, 264, 396, 280]},
	{"text": "神经侵犯：神经未见癌组织侵犯。", "bbox": [132, 280, 437, 297]},
	{"text": "沿气道播散STAS：查见STAS。", "bbox": [132, 297, 396, 313]},
	{"text": "胸膜侵犯：侵及壁层胸膜，PL3(改进Hammar分级)。", "bbox": [132, 313, 585, 329]},
	{"text": "切缘情况：支气管断端及肺切缘均未见癌。", "bbox": [132, 330, 517, 347]},
	{"text": "周围肺情况：周围肺组织示炭末沉积及细支气管化生。", "bbox": [132, 347, 616, 363]},
	{"text": "支气管周围淋巴结：查见支气管周围淋巴结（0/1）枚，未见癌组织转移。", "bbox": [132, 363, 784, 379]},
	{"text": "送检淋巴结：送检\"第7组\"淋巴结（0/1）枚，\"第10组\"淋巴结（0/1）枚，\"第11组\"淋巴", "bbox": [132, 379, 914, 396]},
	{"text": "结（0/1）枚，\"第12组\"淋巴结（0/1）枚，未见癌组织转移。", "bbox": [132, 396, 666, 412]},
	{"text": "免疫组化：1#TTF-1/弹力纤维（+）；", "bbox": [132, 412, 465, 429]},
	{"text": "3#TTF-1（+）；", "bbox": [132, 429, 262, 445]},
	{"text": "8#TTF-1（+），P40（+）；", "bbox": [132, 445, 365, 462]},
	{"text": "10#TTF-1/弹力纤维（+）；", "bbox": [132, 462, 365, 478]},
	{"text": "11#TTF-1/弹力纤维（+），P40（-）。", "bbox": [132, 478, 467, 494]},
	{"text": "特殊染色：8#六胺银染色（-）。", "bbox": [132, 494, 418, 511]}
]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=10.9s
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[0]: text=病理诊断报告单, bbox=[345, 83, 655, 115]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[1]: text=病理号, bbox=[658, 121, 730, 139]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：夕, bbox=[69, 153, 140, 169]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 年龄：67岁 科室病区, bbox=[343, 153, 641, 169]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[4]: text=送检医院：188.8.15, bbox=[69, 178, 340, 198]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[5]: text=病. 1067375 床号：1-, bbox=[561, 178, 877, 198]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[6]: text=收到日期：2024-06-19 门诊号：, bbox=[70, 204, 413, 220]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[7]: text=报告日期：2024-06-21, bbox=[561, 204, 768, 220]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[8]: text=肿瘤分级：低分化。, bbox=[132, 232, 315, 248]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[9]: text=肿瘤数量：1个。, bbox=[132, 248, 284, 264]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[10]: text=脉管内癌栓：脉管内见癌栓。, bbox=[132, 264, 396, 280]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[11]: text=神经侵犯：神经未见癌组织侵犯。, bbox=[132, 280, 437, 297]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[12]: text=沿气道播散STAS：查见STAS。, bbox=[132, 297, 396, 313]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[13]: text=胸膜侵犯：侵及壁层胸膜，PL3(改进Hammar分级)。, bbox=[132, 313, 585, 329]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[14]: text=切缘情况：支气管断端及肺切缘均未见癌。, bbox=[132, 330, 517, 347]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[15]: text=周围肺情况：周围肺组织示炭末沉积及细支气管化生。, bbox=[132, 347, 616, 363]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[16]: text=支气管周围淋巴结：查见支气管周围淋巴结（0/1）枚，未见癌组织转移。, bbox=[132, 363, 784, 379]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[17]: text=送检淋巴结：送检"第7组"淋巴结（0/1）枚，"第10组"淋巴结（0/1）枚，"第11组"淋巴, bbox=[132, 379, 914, 396]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[18]: text=结（0/1）枚，"第12组"淋巴结（0/1）枚，未见癌组织转移。, bbox=[132, 396, 666, 412]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[19]: text=免疫组化：1#TTF-1/弹力纤维（+）；, bbox=[132, 412, 465, 429]
2026-08-10 19:24:41,004 INFO     29 [qwen-vl-text] coord item[20]: text=3#TTF-1（+）；, bbox=[132, 429, 262, 445]
2026-08-10 19:24:41,005 INFO     29 [qwen-vl-text] coord item[21]: text=8#TTF-1（+），P40（+）；, bbox=[132, 445, 365, 462]
2026-08-10 19:24:41,005 INFO     29 [qwen-vl-text] coord item[22]: text=10#TTF-1/弹力纤维（+）；, bbox=[132, 462, 365, 478]
2026-08-10 19:24:41,005 INFO     29 [qwen-vl-text] coord item[23]: text=11#TTF-1/弹力纤维（+），P40（-）。, bbox=[132, 478, 467, 494]
2026-08-10 19:24:41,005 INFO     29 [qwen-vl-text] coord item[24]: text=特殊染色：8#六胺银染色（-）。, bbox=[132, 494, 418, 511]
2026-08-10 19:24:41,005 INFO     29 [qwen-vl-text] page=6 — 25/25 coords, api_time=10.9s
2026-08-10 19:24:41,005 INFO     29 [qwen-vl-text] new_positions (25):
[[6, 205.27499999999998, 389.72499999999997, 69.886, 96.83], [6, 391.51, 434.34999999999997, 101.88199999999999, 117.038], [6, 41.055, 83.3, 128.826, 142.298], [6, 204.08499999999998, 381.395, 128.826, 142.298], [6, 41.055, 202.29999999999998, 149.876, 166.716], [6, 333.79499999999996, 521.8149999999999, 149.876, 166.716], [6, 41.65, 245.73499999999999, 171.768, 185.23999999999998], [6, 333.79499999999996, 456.96, 171.768, 185.23999999999998], [6, 78.53999999999999, 187.42499999999998, 195.344, 208.816], [6, 78.53999999999999, 168.98, 208.816, 222.28799999999998], [6, 78.53999999999999, 235.61999999999998, 222.28799999999998, 235.76], [6, 78.53999999999999, 260.015, 235.76, 250.07399999999998], [6, 78.53999999999999, 235.61999999999998, 250.07399999999998, 263.546], [6, 78.53999999999999, 348.075, 263.546, 277.018], [6, 78.53999999999999, 307.615, 277.86, 292.174], [6, 78.53999999999999, 366.52, 292.174, 305.646], [6, 78.53999999999999, 466.47999999999996, 305.646, 319.118], [6, 78.53999999999999, 543.8299999999999, 319.118, 333.432], [6, 78.53999999999999, 396.27, 333.432, 346.904], [6, 78.53999999999999, 276.675, 346.904, 361.21799999999996], [6, 78.53999999999999, 155.89, 361.21799999999996, 374.69], [6, 78.53999999999999, 217.17499999999998, 374.69, 389.00399999999996], [6, 78.53999999999999, 217.17499999999998, 389.00399999999996, 402.476], [6, 78.53999999999999, 277.865, 402.476, 415.948], [6, 78.53999999999999, 248.70999999999998, 415.948, 430.262]]
2026-08-10 19:24:41,005 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=20.2s
2026-08-10 19:24:41,005 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:24:41,006 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:24:41,006 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:24:41,006 INFO     29 [qwen-vl-text] positions(24): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:24:41,006 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [24]
2026-08-10 19:24:41,175 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:24:41,176 INFO     29 [qwen-vl-text] LLM extraction start, text_len=306
2026-08-10 19:24:41,176 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:24:41,176 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 265, \"bbox_end\": 288, \"encounter_dates\": [\"2024-06-16\"], \"department\": \"胸外科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "、心达院医子影像科\n影像诊断报告书\n取报告生\n可扫码查\n姓名\n性别：女\n年龄：67岁\n影像号\n523551\n病区：胸外科\n病床：1-18床\n病\n检查时间：2024-06-16 21:18:43\n设备：DISCOVERY MR750w2024061614049\n检查项目：颅脑MRI（平扫）\n影像表现：\n双侧基底节区、放射冠、半卵圆中心、额顶叶可见多发斑片状异\n常信号，T1WI、DWI呈等低信号，T2WI呈稍高信号，T2flair呈高信\n号。脑室系统扩张，侧脑室前后角旁白质对称性\nair高信号。中\n线结构居中。脑干、小脑形态信号未见异\n双侧基底节区、放射冠、半卵圆中心\n顶叶多发缺血灶\n2. 脑萎缩、脑白质疏松",
    "role": "user"
  }
]
2026-08-10 19:24:45,396 INFO     29 [qwen-vl-parser] text API response (len=426):
["管杂音。", "肛门生殖器：肛门及外生殖器未见异常。", "脊柱四肢：脊柱生理弯曲正常，活动度正常，脊柱无压痛，无叩击痛；各关节四肢形态正常。肢体无浮肿，无静脉曲张，无色素沉着，无溃疡。", "神经系统：四肢肌力正常，肌张力正常，角膜反射、腹壁反射、肱二头肌、肱三头肌、桡反射、膝反射、跟腱反射正常，巴彬斯基征未引出，脑膜刺激征阴性。", "专科情况", "生命征平稳，神志清楚，浅表淋巴结未触及淋巴结肿大。胸廓对称无畸形，胸壁未见静脉曲张，双肺触觉语颤对称，双肺叩诊呈清音，双肺呼吸音清，未闻及明显干湿性啰音及摩擦音。心前区无隆起，心脏触诊未及震颤，心界叩诊无扩大，心律齐，各瓣音区心音正常，未闻及病理性杂音。腹平软。未见胃肠型及蠕动波，肝脏肋下未触及，无压痛及反跳痛。双下肢无浮肿。", "辅助检查", "出院诊断：", "医生签名：", "初步诊断：肺结节性质待查：", "肺癌？", "炎性假瘤？", "医生签名：", "第3页", ""]
2026-08-10 19:24:45,396 INFO     29 [qwen-vl-parser] page=3 text: 14 lines (bbox 68-81)
2026-08-10 19:24:45,396 INFO     29 [qwen-vl-parser] page=3 text: 14 sections
2026-08-10 19:24:45,555 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1297056, prompt_len=764
2026-08-10 19:24:46,983 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 19:24:46,984 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 19:24:46,997 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1297056, prompt_len=401
2026-08-10 19:24:50,262 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:24:50,263 INFO     29 [qwen-vl-text] LLM output (len=459):
{
  "exam_date": "2024-06-16",
  "report_date": null,
  "exam_name": "颅脑MRI（平扫）",
  "exam_category": "imaging",
  "body_part": "颅脑",
  "patient_name": null,
  "patient_gender": "女",
  "department": "胸外科",
  "bed_number": "1-18床",
  "findings": "双侧基底节区、放射冠、半卵圆中心、额顶叶可见多发斑片状异常信号，T1WI、DWI呈等低信号，T2WI呈稍高信号，T2flair呈高信号。脑室系统扩张，侧脑室前后角旁白质对称性air高信号。中线结构居中。脑干、小脑形态信号未见异",
  "conclusion": "双侧基底节区、放射冠、半卵圆中心顶叶多发缺血灶\n2. 脑萎缩、脑白质疏松",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:24:50,264 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=787262, prompt_len=991
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["、心达院医子影像科", "影像诊断报告书", "取报告生", "可扫码查", "姓名", "性别：女", "年龄：67岁", "影像号", "523551", "病区：胸外科", "病床：1-18床", "病", "检查时间：2024-06-16 21:18:43", "设备：DISCOVERY MR750w2024061614049", "检查项目：颅脑MRI（平扫）", "影像表现：", "双侧基底节区、放射冠、半卵圆中心、额顶叶可见多发斑片状异", "常信号，T1WI、DWI呈等低信号，T2WI呈稍高信号，T2flair呈高信", "号。脑室系统扩张，侧脑室前后角旁白质对称性", "air高信号。中", "线结构居中。脑干、小脑形态信号未见异", "双侧基底节区、放射冠、半卵圆中心", "顶叶多发缺血灶", "2. 脑萎缩、脑白质疏松"]

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
2026-08-10 19:24:55,413 INFO     29 [qwen-vl-parser] text API response (len=1421):
["测量结果:", "Lved:46.5 mm", "Lve5:28.9 mm", "La:26.6 mm", "Ao:25.7 mm", "Lvpw:8.5 mm", "Ivs:9.5 mm", "Rv:20.1 mm", "Ra-L:34.8 mm", "Ra-M:25.5 mm", "Pa:17.6 mm", "E:0.46 m/s", "A:0.63 m/s", "Hr:90 bpm", "Fb:37.8 %", "Bf:68.0 %(Teich)", "EDV:99.8 ml", "Sv:67.8 ml", "Co:6.1 L/min", "Ci:4.0 L/min. m²", "H:166 cm", "W:52.5 kg", "BSA:1.5 m²", "LVM:140.2 g", "LVMI:93.4 g/m²", "B':0.08 m/s", "A':0.10 m/s", "RWT:0.38", "E/A:0.7", "E/E':5.7", "正常参考值(mm) 摘自中国成年人超声心动图检查测量指南《中华超声影像学杂志》2016.25(8):", "AO", "LA", "LV", "IVS", "RA", "RV", "PA", "LVMI", "EF(%)", "0-1岁", "8-15", "8-18", "17-31", "1.5-4", "17-32", "7-12", "6-12", "≥55", "1-6岁", "15-21", "14-21", "27-35", "3-5.5", "26-37", "8-14", "10-16", "≥55", "6-10岁", "17-23", "17-24", "30-38", "5-7", "30-39", "10-15", "14-18", "≥55", "10-14岁", "18-27", "19-30", "32-50", "5-10", "34-47", "11-17", "16-20", "≥55", "成人(男)", "27.7±5.7", "31.1±3.9", "46.2±4.0", "8.9±1.3", "44.4±4.7", "22.3±3.9", "20.1±3.2", "≥125", "≥55", "成人(女)", "25.9±3.5", "29.4±5.8", "43.2±3.3", "8.1±1.3", "41.5±4.7", "21.1±3.6", "19.2±3.1", "≥115", "≥55", "检查描述:", "二维及M型超声:", "静息时未见节段性室壁运动功能异常(见图)。各组瓣膜形态未见异常。心包腔正常。室间隔连", "续性完整，大血管位置关系正常，主一肺动脉无沟通。", "多普勒:", "三尖瓣反流最大压差17MMHG，估测肺动脉收缩压22MMHG。", "彩色多普勒:", "二尖瓣微量反流。三尖瓣轻度反流。主动脉瓣未见明显反流。肺动脉瓣轻度反流。", "超声提示:", "心脏结构及功能未见明显异常改变", "记录医生:袁瑄宸 报告录入:黄玉云 检查医生:刘文坤 复审医生:", "报告日期: 2026-03-17 16:38:04", "检查日期: 2026-03-17", "(本报告仅供临床参考,不做任何证明。)", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 19:24:55,413 INFO     29 [qwen-vl-parser] page=4 text: 112 lines (bbox 82-193)
2026-08-10 19:24:55,413 INFO     29 [qwen-vl-parser] page=4 text: 112 sections
2026-08-10 19:24:55,517 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=754925, prompt_len=764
2026-08-10 19:24:56,883 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-18"
}
```
2026-08-10 19:24:56,884 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2026-03-18
2026-08-10 19:24:56,897 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=754925, prompt_len=401
2026-08-10 19:25:00,350 INFO     29 [qwen-vl-parser] text API response (len=542):
["性别：男", "年龄：49岁", "门诊号：", "检查部位：肺部", "检查设备：GE-HD750", "流水号：0013240579", "检查技术：CT", "影像学所见：", "双肺纹理清晰，左肺下叶见团块软组织密度影，病灶内支气管闭塞，较大截面约7.6cm×", "8.3cm，增强扫描不均匀强化，周围散在条索斑片影。右肺散在小结节，大者右肺上叶尖段见一", "实性结节（Se4/Img46），大小约0.4cm×0.2cm。气管、余支气管通畅，纵隔及左肺门可见肿大", "淋巴结，大者短径约1.0cm，左侧胸腔少-中量积液，部分为包裹性。左侧胸膜结节状增厚。", "影像学诊断：", "1.左肺下叶肿块，考虑MT伴周围阻塞性肺炎，请结合临床。", "2.纵隔及左肺门肿大淋巴结，部分转移可能。", "3.左侧胸膜增厚，转移可能。", "4.右肺散在小结节，性质待定，建议随诊复查。", "5.左侧胸腔少-中量积液，部分为包裹性。", "报告医生：许志祥 /许志祥", "审核医生：沈东挥", "复核医生：", "此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。", "报告时间：2026-03-18", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 19:25:00,351 INFO     29 [qwen-vl-parser] page=5 text: 25 lines (bbox 194-218)
2026-08-10 19:25:00,351 INFO     29 [qwen-vl-parser] page=5 text: 25 sections
2026-08-10 19:25:00,654 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2196086, prompt_len=764
2026-08-10 19:25:01,338 INFO     29 [qwen-vl-text] coord API raw response (len=1912):
[
	{"text": "、心达院医子影像科", "bbox": [377, 205, 730, 232]},
	{"text": "影像诊断报告书", "bbox": [347, 235, 621, 263]},
	{"text": "取报告生", "bbox": [94, 232, 166, 245], "label": "取报告生"},
	{"text": "可扫码查", "bbox": [94, 247, 159, 260], "label": "可扫码查"},
	{"text": "姓名", "bbox": [94, 269, 115, 284], "label": "姓名"},
	{"text": "性别：女", "bbox": [296, 269, 379, 287], "label": "性别：女"},
	{"text": "年龄：67岁", "bbox": [496, 269, 603, 287], "label": "年龄：67岁"},
	{"text": "影像号", "bbox": [698, 269, 756, 287], "label": "影像号"},
	{"text": "523551", "bbox": [785, 270, 848, 284], "label": "523551"},
	{"text": "病区：胸外科", "bbox": [296, 292, 419, 309], "label": "病区：胸外科"},
	{"text": "病床：1-18床", "bbox": [496, 292, 624, 309], "label": "病床：1-18床"},
	{"text": "病", "bbox": [697, 292, 716, 309], "label": "病"},
	{"text": "检查时间：2024-06-16 21:18:43", "bbox": [94, 316, 391, 333], "label": "检查时间：2024-06-16 21:18:43"},
	{"text": "设备：DISCOVERY MR750w2024061614049", "bbox": [496, 316, 831, 333], "label": "设备：DISCOVERY MR750w2024061614049"},
	{"text": "检查项目：颅脑MRI（平扫）", "bbox": [94, 367, 373, 386], "label": "检查项目：颅脑MRI（平扫）"},
	{"text": "影像表现：", "bbox": [94, 410, 196, 428], "label": "影像表现："},
	{"text": "双侧基底节区、放射冠、半卵圆中心、额顶叶可见多发斑片状异", "bbox": [250, 410, 898, 428], "label": "双侧基底节区、放射冠、半卵圆中心、额顶叶可见多发斑片状异"},
	{"text": "常信号，T1WI、DWI呈等低信号，T2WI呈稍高信号，T2flair呈高信", "bbox": [203, 432, 895, 450], "label": "常信号，T1WI、DWI呈等低信号，T2WI呈稍高信号，T2flair呈高信"},
	{"text": "号。脑室系统扩张，侧脑室前后角旁白质对称性", "bbox": [203, 453, 690, 471], "label": "号。脑室系统扩张，侧脑室前后角旁白质对称性"},
	{"text": "air高信号。中", "bbox": [737, 453, 898, 471], "label": "air高信号。中"},
	{"text": "线结构居中。脑干、小脑形态信号未见异", "bbox": [203, 474, 639, 492], "label": "线结构居中。脑干、小脑形态信号未见异"},
	{"text": "双侧基底节区、放射冠、半卵圆中心", "bbox": [245, 705, 621, 723], "label": "双侧基底节区、放射冠、半卵圆中心"},
	{"text": "顶叶多发缺血灶", "bbox": [654, 705, 827, 723], "label": "顶叶多发缺血灶"},
	{"text": "2. 脑萎缩、脑白质疏松", "bbox": [203, 729, 455, 747], "label": "2. 脑萎缩、脑白质疏松"}
]
2026-08-10 19:25:01,339 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=11.1s
2026-08-10 19:25:01,339 INFO     29 [qwen-vl-text] coord item[0]: text=、心达院医子影像科, bbox=[377, 205, 730, 232]
2026-08-10 19:25:01,339 INFO     29 [qwen-vl-text] coord item[1]: text=影像诊断报告书, bbox=[347, 235, 621, 263]
2026-08-10 19:25:01,339 INFO     29 [qwen-vl-text] coord item[2]: text=取报告生, bbox=[94, 232, 166, 245]
2026-08-10 19:25:01,339 INFO     29 [qwen-vl-text] coord item[3]: text=可扫码查, bbox=[94, 247, 159, 260]
2026-08-10 19:25:01,339 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[94, 269, 115, 284]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女, bbox=[296, 269, 379, 287]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：67岁, bbox=[496, 269, 603, 287]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[7]: text=影像号, bbox=[698, 269, 756, 287]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[8]: text=523551, bbox=[785, 270, 848, 284]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[9]: text=病区：胸外科, bbox=[296, 292, 419, 309]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[10]: text=病床：1-18床, bbox=[496, 292, 624, 309]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[11]: text=病, bbox=[697, 292, 716, 309]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[12]: text=检查时间：2024-06-16 21:18:43, bbox=[94, 316, 391, 333]
2026-08-10 19:25:01,340 INFO     29 [qwen-vl-text] coord item[13]: text=设备：DISCOVERY MR750w2024061614049, bbox=[496, 316, 831, 333]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[14]: text=检查项目：颅脑MRI（平扫）, bbox=[94, 367, 373, 386]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[15]: text=影像表现：, bbox=[94, 410, 196, 428]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[16]: text=双侧基底节区、放射冠、半卵圆中心、额顶叶可见多发斑片状异, bbox=[250, 410, 898, 428]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[17]: text=常信号，T1WI、DWI呈等低信号，T2WI呈稍高信号，T2flair呈高信, bbox=[203, 432, 895, 450]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[18]: text=号。脑室系统扩张，侧脑室前后角旁白质对称性, bbox=[203, 453, 690, 471]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[19]: text=air高信号。中, bbox=[737, 453, 898, 471]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[20]: text=线结构居中。脑干、小脑形态信号未见异, bbox=[203, 474, 639, 492]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[21]: text=双侧基底节区、放射冠、半卵圆中心, bbox=[245, 705, 621, 723]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[22]: text=顶叶多发缺血灶, bbox=[654, 705, 827, 723]
2026-08-10 19:25:01,341 INFO     29 [qwen-vl-text] coord item[23]: text=2. 脑萎缩、脑白质疏松, bbox=[203, 729, 455, 747]
2026-08-10 19:25:01,343 INFO     29 [qwen-vl-text] page=7 — 24/24 coords, api_time=11.1s
2026-08-10 19:25:01,343 INFO     29 [qwen-vl-text] new_positions (24):
[[7, 224.315, 434.34999999999997, 172.60999999999999, 195.344], [7, 206.465, 369.495, 197.87, 221.446], [7, 55.93, 98.77, 195.344, 206.29], [7, 55.93, 94.60499999999999, 207.974, 218.92], [7, 55.93, 68.425, 226.498, 239.128], [7, 176.12, 225.505, 226.498, 241.654], [7, 295.12, 358.78499999999997, 226.498, 241.654], [7, 415.31, 449.82, 226.498, 241.654], [7, 467.075, 504.56, 227.34, 239.128], [7, 176.12, 249.30499999999998, 245.864, 260.178], [7, 295.12, 371.28, 245.864, 260.178], [7, 414.715, 426.02, 245.864, 260.178], [7, 55.93, 232.64499999999998, 266.072, 280.38599999999997], [7, 295.12, 494.445, 266.072, 280.38599999999997], [7, 55.93, 221.935, 309.014, 325.012], [7, 55.93, 116.61999999999999, 345.21999999999997, 360.376], [7, 148.75, 534.31, 345.21999999999997, 360.376], [7, 120.785, 532.525, 363.74399999999997, 378.9], [7, 120.785, 410.54999999999995, 381.426, 396.582], [7, 438.515, 534.31, 381.426, 396.582], [7, 120.785, 380.205, 399.108, 414.264], [7, 145.775, 369.495, 593.61, 608.766], [7, 389.13, 492.065, 593.61, 608.766], [7, 120.785, 270.72499999999997, 613.818, 628.9739999999999]]
2026-08-10 19:25:01,343 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=20.3s
2026-08-10 19:25:01,343 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:25:01,349 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:25:01,349 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:25:01,349 INFO     29 [qwen-vl-text] positions(34): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:25:01,350 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [34]
2026-08-10 19:25:01,533 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:25:01,534 INFO     29 [qwen-vl-text] LLM extraction start, text_len=476
2026-08-10 19:25:01,534 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:25:01,534 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 293, \"bbox_end\": 326, \"encounter_dates\": [\"2024-06-18\"], \"department\": \"胸外科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "住院\n取报告48小时后\n可扫码去二防山\n影像诊断报告书\n性别：女\n年龄：67岁\n影像号：450\n科_\n病区：胸外科\n病床：1-18床\n病...\n检查时间：2024-06-18 09:28:48\n设备：Revolution CT\n2\n检查项目：双肺CT（平扫+强化）\n影像表现：双侧胸廓对称，气管纵隔居中，右肺中叶外段（im34）见结节状密\n度增高影，大小约28×26mm，边界较清，示支气管截断征，邻近叶间\n胸膜轻度受牵拉，增强扫描团块呈轻-中度强化，其内穿行血管壁毛\n糙；双肺另见粟粒及微小结节，较大者位于右侧斜裂（im39），大小\n约5×3mm，边界清。双肺见条片状密度增高影。纵隔内见增大淋巴结。\n心脏未见异常，主动脉及冠脉见钙化影。右侧胸腔少量积液，胸膜未\n见增厚\n影像诊断：右肺中叶结节，考虑肺癌伴纵隔淋巴结增大，请结合临床，必要时细\n胞学检查\n双肺多发粟粒及微小结节，可随诊观察\n双肺条片影\n主动脉及冠脉钙化\n右侧胸腔少量积液\n报告医师：\n报告时间：\n2024-06-18\n14:41:25审核时间：\n2024-06-18\n15:24:02",
    "role": "user"
  }
]
2026-08-10 19:25:01,536 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:25:01.535+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 90, "failed": 0, "current": {"dbb9d9e294ee11f1bd9827cf206dfa2d": {"id": "dbb9d9e294ee11f1bd9827cf206dfa2d", "doc_id": "db844cb494ee11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 14828427, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388903475, "task_type": "dataflow", "root_trace_id": "9d9ed785184e435b9d8a5693cadbcf94", "root_traceparent": "00-9d9ed785184e435b9d8a5693cadbcf94-7ebd92d2185d496c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:25:02,017 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-17"}
```
2026-08-10 19:25:02,017 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2026-03-17
2026-08-10 19:25:02,024 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2196086, prompt_len=401
2026-08-10 19:25:06,336 INFO     29 [qwen-vl-parser] text API response (len=764):
["门诊号:", "医院:", "申请医生", "申请科室", "检查日期: 2026-03-17 10:58:32", "检查医生", "报告日期: 2026-03-17 11:11:03", "报告医生: 蔡平", "审核日期: 2026-03-17 11:11:03", "审核医生: 蔡平", "电轴(-30~90°): 29", "QRS时限(<120): 100", "P-R间期(120~200): 134", "Q-T间期(0~450): 344", "QTc(0~450): 444", "SV1: 1.26", "RV5(0~2.5): 2.02", "R+S: 3.28", "心率(60~100): 100", "临床诊断: 肺肿物", "描述:", "诊断: 窦性心律 ST段改变", "报告状态 已审核", "检查项目: 心电图(常规十二通道)", "当前状态", "走纸: 25mm/s", "增益:10mm/mv", "当前模式:普通模式", "572", "596", "600", "600", "596", "600", "604", "600", "596", "596", "604", "604", "596", "25mm/s 10mm/mv", "105", "101", "100", "100", "101", "100", "100", "100", "101", "101", "100", "100", "101", "100", "100", "102", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6", "2026-03-17 10:59:32", "版权所有 纳龙科技"]
2026-08-10 19:25:06,337 INFO     29 [qwen-vl-parser] page=6 text: 71 lines (bbox 219-289)
2026-08-10 19:25:06,338 INFO     29 [qwen-vl-parser] page=6 text: 71 sections
2026-08-10 19:25:06,432 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=526104, prompt_len=764
2026-08-10 19:25:07,797 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-19"
}
```
2026-08-10 19:25:07,797 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2026-03-19
2026-08-10 19:25:07,807 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=526104, prompt_len=401
2026-08-10 19:25:09,851 INFO     29 [qwen-vl-parser] text API response (len=339):
["检查部位：头颅", "检查设备：飞利浦MR9 流水号：0013240580", "检查技术：MR", "检查参数：", "影像学所见：", "双侧大脑半球对称，灰白质对比正常，实质内未见明显异常信号，DWI未见异常高信号，SW", "I未见异常低信号，各脑沟、脑池未见增宽、变深，脑室系统未见增宽，中线结构居中，幕下小", "脑、脑干未见异常信号，双侧桥小脑角区未见明显异常。颅骨骨质未见异常信号。增强后未见", "明显强化。", "影像学诊断：", "颅脑MRI平扫及增强未见明显异常。", "报告医生：林佳辉 /林佳辉", "审核医生：陈明宏", "复核医生：", "此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。", "报告时间：2026-03-19"]
2026-08-10 19:25:09,852 INFO     29 [qwen-vl-parser] page=7 text: 16 lines (bbox 290-305)
2026-08-10 19:25:09,852 INFO     29 [qwen-vl-parser] page=7 text: 16 sections
2026-08-10 19:25:09,990 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1030745, prompt_len=764
2026-08-10 19:25:10,795 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:25:10,795 INFO     29 [qwen-vl-text] LLM output (len=591):
{
  "exam_date": "2024-06-18",
  "report_date": "2024-06-18",
  "exam_name": "双肺CT（平扫+强化）",
  "exam_category": "imaging",
  "body_part": "双肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "胸外科",
  "bed_number": "1-18床",
  "findings": "双侧胸廓对称，气管纵隔居中，右肺中叶外段（im34）见结节状密度增高影，大小约28×26mm，边界较清，示支气管截断征，邻近叶间胸膜轻度受牵拉，增强扫描团块呈轻-中度强化，其内穿行血管壁毛糙；双肺另见粟粒及微小结节，较大者位于右侧斜裂（im39），大小约5×3mm，边界清。双肺见条片状密度增高影。纵隔内见增大淋巴结。心脏未见异常，主动脉及冠脉见钙化影。右侧胸腔少量积液，胸膜未见增厚",
  "conclusion": "右肺中叶结节，考虑肺癌伴纵隔淋巴结增大，请结合临床，必要时细胞学检查\n双肺多发粟粒及微小结节，可随诊观察\n双肺条片影\n主动脉及冠脉钙化\n右侧胸腔少量积液",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:25:10,797 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1034031, prompt_len=1191
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["住院", "取报告48小时后", "可扫码去二防山", "影像诊断报告书", "性别：女", "年龄：67岁", "影像号：450", "科_", "病区：胸外科", "病床：1-18床", "病...", "检查时间：2024-06-18 09:28:48", "设备：Revolution CT", "2", "检查项目：双肺CT（平扫+强化）", "影像表现：双侧胸廓对称，气管纵隔居中，右肺中叶外段（im34）见结节状密", "度增高影，大小约28×26mm，边界较清，示支气管截断征，邻近叶间", "胸膜轻度受牵拉，增强扫描团块呈轻-中度强化，其内穿行血管壁毛", "糙；双肺另见粟粒及微小结节，较大者位于右侧斜裂（im39），大小", "约5×3mm，边界清。双肺见条片状密度增高影。纵隔内见增大淋巴结。", "心脏未见异常，主动脉及冠脉见钙化影。右侧胸腔少量积液，胸膜未", "见增厚", "影像诊断：右肺中叶结节，考虑肺癌伴纵隔淋巴结增大，请结合临床，必要时细", "胞学检查", "双肺多发粟粒及微小结节，可随诊观察", "双肺条片影", "主动脉及冠脉钙化", "右侧胸腔少量积液", "报告医师：", "报告时间：", "2024-06-18", "14:41:25审核时间：", "2024-06-18", "15:24:02"]

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
2026-08-10 19:25:11,334 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-18"
}
```
2026-08-10 19:25:11,335 INFO     29 [qwen-vl-parser] page=8 classify=table report_date=2026-03-18
2026-08-10 19:25:11,341 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1030745, prompt_len=756
2026-08-10 19:25:14,982 INFO     29 [qwen-vl-parser] table API response (len=607):
\begin{tabular}{ccccccll}
\hline
\textbf{检验项目} & \textbf{结果} & \textbf{提示} & \textbf{参考区间} & \textbf{单位} & \textbf{方法} \\
\hline
1 & ★乙肝病毒表面抗原 & 0.00 & 阴性(-) & $<$0.05 & IU/ml & 学发光定量分析 \\
2 & ★乙肝病毒表面抗体 & 47.62 & 阳性(+) & $<$10 & mIU/ml & 学发光定量分析 \\
3 & ★乙肝病毒e抗原 & 0.41 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\
4 & ★乙肝病毒e抗体 & 1.29 & 阴性(-) & $>$1 & S/CO & 化学发光法YP \\
5 & ★乙肝病毒核心抗体 & 2.01 & 阳性(+) & $<$1 & S/CO & 化学发光法YP \\
6 & ★丙型肝炎病毒抗体 & 0.11 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\
7 & ★人免疫缺陷病毒抗原抗体 & 0.07 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\
8 & ★梅毒螺旋体特异抗体 & 0.11 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\
\hline
\end{tabular}
2026-08-10 19:25:14,986 INFO     29 [qwen-vl-parser] page=8 table: 15 LaTeX lines (bbox 306-320)
2026-08-10 19:25:14,986 INFO     29 [qwen-vl-parser] page=8 table: 15 sections
2026-08-10 19:25:16,111 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1691252, prompt_len=764
2026-08-10 19:25:19,068 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-18"
}
```
2026-08-10 19:25:19,068 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=2026-03-18
2026-08-10 19:25:19,084 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1691252, prompt_len=756
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord API raw response (len=2834):
[
	{"text": "住院", "bbox": [865, 35, 935, 60]},
	{"text": "取报告48小时后", "bbox": [97, 106, 235, 119], "label": "取报告48小时后"},
	{"text": "可扫码去二防山", "bbox": [97, 117, 236, 129], "label": "可扫码去二防山"},
	{"text": "影像诊断报告书", "bbox": [374, 108, 649, 133], "label": "影像诊断报告书"},
	{"text": "性别：女", "bbox": [300, 140, 383, 156], "label": "性别：女"},
	{"text": "年龄：67岁", "bbox": [502, 140, 607, 156], "label": "年龄：67岁"},
	{"text": "影像号：450", "bbox": [703, 140, 820, 156], "label": "影像号：450"},
	{"text": "科_", "bbox": [97, 165, 127, 180], "label": "科_"},
	{"text": "病区：胸外科", "bbox": [300, 165, 423, 180], "label": "病区：胸外科"},
	{"text": "病床：1-18床", "bbox": [502, 165, 629, 180], "label": "病床：1-18床"},
	{"text": "病...", "bbox": [703, 165, 770, 180], "label": "病..."},
	{"text": "检查时间：2024-06-18 09:28:48", "bbox": [97, 188, 396, 202], "label": "检查时间：2024-06-18 09:28:48"},
	{"text": "设备：Revolution CT", "bbox": [502, 188, 677, 202], "label": "设备：Revolution CT"},
	{"text": "2", "bbox": [703, 188, 720, 202], "label": "2"},
	{"text": "检查项目：双肺CT（平扫+强化）", "bbox": [97, 240, 422, 257], "label": "检查项目：双肺CT（平扫+强化）"},
	{"text": "影像表现：双侧胸廓对称，气管纵隔居中，右肺中叶外段（im34）见结节状密", "bbox": [97, 285, 893, 302], "label": "影像表现：双侧胸廓对称，气管纵隔居中，右肺中叶外段（im34）见结节状密"},
	{"text": "度增高影，大小约28×26mm，边界较清，示支气管截断征，邻近叶间", "bbox": [206, 307, 901, 324], "label": "度增高影，大小约28×26mm，边界较清，示支气管截断征，邻近叶间"},
	{"text": "胸膜轻度受牵拉，增强扫描团块呈轻-中度强化，其内穿行血管壁毛", "bbox": [206, 328, 893, 345], "label": "胸膜轻度受牵拉，增强扫描团块呈轻-中度强化，其内穿行血管壁毛"},
	{"text": "糙；双肺另见粟粒及微小结节，较大者位于右侧斜裂（im39），大小", "bbox": [206, 350, 893, 367], "label": "糙；双肺另见粟粒及微小结节，较大者位于右侧斜裂（im39），大小"},
	{"text": "约5×3mm，边界清。双肺见条片状密度增高影。纵隔内见增大淋巴结。", "bbox": [206, 371, 898, 388], "label": "约5×3mm，边界清。双肺见条片状密度增高影。纵隔内见增大淋巴结。"},
	{"text": "心脏未见异常，主动脉及冠脉见钙化影。右侧胸腔少量积液，胸膜未", "bbox": [206, 392, 902, 409], "label": "心脏未见异常，主动脉及冠脉见钙化影。右侧胸腔少量积液，胸膜未"},
	{"text": "见增厚", "bbox": [206, 413, 275, 430], "label": "见增厚"},
	{"text": "影像诊断：右肺中叶结节，考虑肺癌伴纵隔淋巴结增大，请结合临床，必要时细", "bbox": [97, 581, 901, 598], "label": "影像诊断：右肺中叶结节，考虑肺癌伴纵隔淋巴结增大，请结合临床，必要时细"},
	{"text": "胞学检查", "bbox": [206, 603, 300, 619], "label": "胞学检查"},
	{"text": "双肺多发粟粒及微小结节，可随诊观察", "bbox": [206, 625, 601, 642], "label": "双肺多发粟粒及微小结节，可随诊观察"},
	{"text": "双肺条片影", "bbox": [206, 650, 323, 667], "label": "双肺条片影"},
	{"text": "主动脉及冠脉钙化", "bbox": [206, 674, 393, 691], "label": "主动脉及冠脉钙化"},
	{"text": "右侧胸腔少量积液", "bbox": [206, 698, 393, 715], "label": "右侧胸腔少量积液"},
	{"text": "报告医师：", "bbox": [97, 852, 185, 868], "label": "报告医师："},
	{"text": "报告时间：", "bbox": [97, 893, 185, 908], "label": "报告时间："},
	{"text": "2024-06-18", "bbox": [275, 895, 378, 907], "label": "2024-06-18"},
	{"text": "14:41:25审核时间：", "bbox": [419, 895, 588, 907], "label": "14:41:25审核时间："},
	{"text": "2024-06-18", "bbox": [684, 895, 785, 907], "label": "2024-06-18"},
	{"text": "15:24:02", "bbox": [822, 895, 902, 907], "label": "15:24:02"}
]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=18.8s
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[0]: text=住院, bbox=[865, 35, 935, 60]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[1]: text=取报告48小时后, bbox=[97, 106, 235, 119]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[2]: text=可扫码去二防山, bbox=[97, 117, 236, 129]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[3]: text=影像诊断报告书, bbox=[374, 108, 649, 133]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[300, 140, 383, 156]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：67岁, bbox=[502, 140, 607, 156]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[6]: text=影像号：450, bbox=[703, 140, 820, 156]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[7]: text=科_, bbox=[97, 165, 127, 180]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[8]: text=病区：胸外科, bbox=[300, 165, 423, 180]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[9]: text=病床：1-18床, bbox=[502, 165, 629, 180]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[10]: text=病..., bbox=[703, 165, 770, 180]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[11]: text=检查时间：2024-06-18 09:28:48, bbox=[97, 188, 396, 202]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[12]: text=设备：Revolution CT, bbox=[502, 188, 677, 202]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[13]: text=2, bbox=[703, 188, 720, 202]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[14]: text=检查项目：双肺CT（平扫+强化）, bbox=[97, 240, 422, 257]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[15]: text=影像表现：双侧胸廓对称，气管纵隔居中，右肺中叶外段（im34）见结节状密, bbox=[97, 285, 893, 302]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[16]: text=度增高影，大小约28×26mm，边界较清，示支气管截断征，邻近叶间, bbox=[206, 307, 901, 324]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[17]: text=胸膜轻度受牵拉，增强扫描团块呈轻-中度强化，其内穿行血管壁毛, bbox=[206, 328, 893, 345]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[18]: text=糙；双肺另见粟粒及微小结节，较大者位于右侧斜裂（im39），大小, bbox=[206, 350, 893, 367]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[19]: text=约5×3mm，边界清。双肺见条片状密度增高影。纵隔内见增大淋巴结。, bbox=[206, 371, 898, 388]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[20]: text=心脏未见异常，主动脉及冠脉见钙化影。右侧胸腔少量积液，胸膜未, bbox=[206, 392, 902, 409]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[21]: text=见增厚, bbox=[206, 413, 275, 430]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[22]: text=影像诊断：右肺中叶结节，考虑肺癌伴纵隔淋巴结增大，请结合临床，必要时细, bbox=[97, 581, 901, 598]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[23]: text=胞学检查, bbox=[206, 603, 300, 619]
2026-08-10 19:25:29,556 INFO     29 [qwen-vl-text] coord item[24]: text=双肺多发粟粒及微小结节，可随诊观察, bbox=[206, 625, 601, 642]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[25]: text=双肺条片影, bbox=[206, 650, 323, 667]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[26]: text=主动脉及冠脉钙化, bbox=[206, 674, 393, 691]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[27]: text=右侧胸腔少量积液, bbox=[206, 698, 393, 715]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[28]: text=报告医师：, bbox=[97, 852, 185, 868]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[29]: text=报告时间：, bbox=[97, 893, 185, 908]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[30]: text=2024-06-18, bbox=[275, 895, 378, 907]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[31]: text=14:41:25审核时间：, bbox=[419, 895, 588, 907]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[32]: text=2024-06-18, bbox=[684, 895, 785, 907]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] coord item[33]: text=15:24:02, bbox=[822, 895, 902, 907]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] page=8 — 34/34 coords, api_time=18.8s
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] new_positions (34):
[[8, 514.675, 556.3249999999999, 29.47, 50.519999999999996], [8, 57.714999999999996, 139.825, 89.252, 100.198], [8, 57.714999999999996, 140.42, 98.514, 108.618], [8, 222.53, 386.155, 90.93599999999999, 111.98599999999999], [8, 178.5, 227.885, 117.88, 131.352], [8, 298.69, 361.16499999999996, 117.88, 131.352], [8, 418.28499999999997, 487.9, 117.88, 131.352], [8, 57.714999999999996, 75.565, 138.93, 151.56], [8, 178.5, 251.685, 138.93, 151.56], [8, 298.69, 374.255, 138.93, 151.56], [8, 418.28499999999997, 458.15, 138.93, 151.56], [8, 57.714999999999996, 235.61999999999998, 158.296, 170.084], [8, 298.69, 402.815, 158.296, 170.084], [8, 418.28499999999997, 428.4, 158.296, 170.084], [8, 57.714999999999996, 251.08999999999997, 202.07999999999998, 216.394], [8, 57.714999999999996, 531.3349999999999, 239.97, 254.284], [8, 122.57, 536.095, 258.49399999999997, 272.808], [8, 122.57, 531.3349999999999, 276.176, 290.49], [8, 122.57, 531.3349999999999, 294.7, 309.014], [8, 122.57, 534.31, 312.382, 326.69599999999997], [8, 122.57, 536.6899999999999, 330.06399999999996, 344.378], [8, 122.57, 163.625, 347.746, 362.06], [8, 57.714999999999996, 536.095, 489.202, 503.51599999999996], [8, 122.57, 178.5, 507.726, 521.198], [8, 122.57, 357.59499999999997, 526.25, 540.564], [8, 122.57, 192.185, 547.3, 561.614], [8, 122.57, 233.83499999999998, 567.5079999999999, 581.822], [8, 122.57, 233.83499999999998, 587.716, 602.03], [8, 57.714999999999996, 110.07499999999999, 717.384, 730.856], [8, 57.714999999999996, 110.07499999999999, 751.906, 764.536], [8, 163.625, 224.91, 753.5899999999999, 763.694], [8, 249.30499999999998, 349.85999999999996, 753.5899999999999, 763.694], [8, 406.97999999999996, 467.075, 753.5899999999999, 763.694], [8, 489.09, 536.6899999999999, 753.5899999999999, 763.694]]
2026-08-10 19:25:29,557 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=28.2s
2026-08-10 19:25:29,557 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:25:29,558 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:25:29,558 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:25:29,558 INFO     29 [qwen-vl-text] positions(22): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:25:29,558 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [22]
2026-08-10 19:25:29,721 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:25:29,722 INFO     29 [qwen-vl-text] LLM extraction start, text_len=257
2026-08-10 19:25:29,722 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:25:29,722 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 329, \"bbox_end\": 350, \"encounter_dates\": [\"2024-06-20\"], \"department\": \"胸外科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "住院\n取报告48小时\n可扫码查\n影像诊断报告书\n性别：女\n年龄：67岁\n病区：胸外科\n病床：1-33床\n病案号：80\n时间：2024-06-20 15:03:45\n检查项目：胸部正位片\n影像表现： 双侧胸廓对称，气管、纵隔居中，右肺纹理模糊，左肺野清晰，\n双肺纹理走行自然。心脏、大血管影未见异常。双侧膈面光滑，双侧\n肋膈角稍钝。右侧胸腔引流管，右侧胸壁软组织积气。\n影像诊断：右肺术后改变。\n双侧肋膈角稍钝。\n报告医师：\n审核医师：\n报告时间：\n17:26:30审核时间：\n2024-06-21\n07:53:41",
    "role": "user"
  }
]
2026-08-10 19:25:30,515 INFO     29 [qwen-vl-parser] table API response (len=2145):
\begin{tabular}{cccccc}
\hline
\multicolumn{2}{c}{检验项目} & 结果 & 参考区间 & 单位 & \\
\hline
1 & ★总胆红素[TBIL] & 10.6 & 0.0~23.0 & umol/L & \\
2 & ★直接胆红素[DBIL] & 1.4 & 0.0~8.0 & umol/L & \\
3 & 间接胆红素[IBIL] & 9.2 & 0.0~20.0 & umol/L & \\
4 & ★总蛋白[TP] & 81.8 & 65.0~85.0 & g/L & \\
5 & ★白蛋白[ALB] & 37.3 & 40.0~55.0 & g/L & \\
6 & 球蛋白[GLB] & 44.5 & 20.0~35.0 & g/L & \\
7 & 白球比例[A/G] & 0.84 & 1.09~2.50 & & \\
8 & ★丙氨酸氨基转移酶 & 39 & 9~50 & IU/L & \\
9 & ★天冬氨酸氨基转移酶 & 27 & 15~40 & IU/L & \\
10 & AST/ALT & 0.69 & & & \\
11 & ★γ-谷氨酰转肽酶 & 79 & 10~60 & IU/L & \\
12 & ★碱性磷酸酶[ALP] & 146 & 45~125 & IU/L & \\
13 & ★甘油三酯[TG] & 0.98 & 0.40~1.86 & mmol/L & \\
14 & ★总胆固醇[CHOL] & 4.73 & 3.40~6.10 & mmol/L & \\
15 & ★高密度脂蛋白胆固醇 & 0.77 & 0.90~1.90 & mmol/L & \\
16 & 非高密度脂蛋白胆固醇 & 3.96 & & & \\
17 & ★低密度脂蛋白胆固醇 & 3.37 & 1.10~3.50 & mmol/L & \\
18 & ★载脂蛋白A1[APOA1] & 0.76 & 1.00~1.60 & g/L & \\
19 & ★载脂蛋白B[APOB] & 1.09 & 0.60~1.10 & g/L & \\
20 & 载脂蛋白A1：B & 0.70 & & & \\
\hline
\multicolumn{6}{l}{※标本状态：符合检测要求} \\
\hline
\multicolumn{3}{l}{不件时间 2026-03-18 08:30} & \multicolumn{3}{l}{申请时间 2026-03-16 10:33} \\
\multicolumn{3}{l}{打印时间} & \multicolumn{3}{l}{接收时间 2026-03-18 10:05} \\
\multicolumn{3}{l}{带“★”者为省医疗单位互认项目。} & \multicolumn{3}{l}{接收者 \quad \quad \quad 检验者 \quad \quad \quad 审核者} \\
\hline
\end{tabular}

\begin{tabular}{cccccc}
\hline
\multicolumn{2}{c}{检验项目} & 结果 & 参考区间 & 单位 & \\
\hline
21 & ★尿素[UREA] & 4.1 & 3.1~7.4 & mmol/L & \\
22 & ★肌酐[CREA] & 68 & 57~97 & umol/L & \\
23 & UREA/CREA & 0.06 & & & \\
24 & ★尿酸[URIC] & 183 & 130~430 & umol/L & \\
25 & ★葡萄糖[GLU] & 5.21 & 3.90~6.10 & mmol/L & \\
26 & ★乳酸脱氢酶[LDH] & 162 & 120~250 & IU/L & \\
27 & ★肌酸激酶[CK] & 36 & 22~270 & IU/L & \\
28 & 肌酸激酶MB亚型 & 17.0 & 2.0~25.0 & IU/L & \\
29 & CKMB/CK & 0.47 & & & \\
30 & ★钾[K] & 4.50 & 3.50~5.50 & mmol/L & \\
31 & ★钠[NA] & 138.4 & 135.0~148.0 & mmol/L & \\
32 & ★氯[CL] & 96.3 & 96.0~112.0 & mmol/L & \\
33 & ★钙[CA] & 2.35 & 2.10~2.70 & mmol/L & \\
34 & 碳酸氢盐[HC03] & 27.3 & 20.1~29.0 & mmol/L & \\
35 & ★镁[MG] & 0.99 & 0.70~1.10 & mmol/L & \\
36 & ★无机磷酸盐[P] & 1.27 & 0.83~1.48 & mmol/L & \\
37 & 阴离子间隙[AG] & 19 & & & \\
38 & 渗透压[OSM] & 286 & & & \\
\hline
\end{tabular}
2026-08-10 19:25:30,517 INFO     29 [qwen-vl-parser] page=9 table: 58 LaTeX lines (bbox 321-378)
2026-08-10 19:25:30,517 INFO     29 [qwen-vl-parser] page=9 table: 58 sections
2026-08-10 19:25:30,703 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1607363, prompt_len=764
2026-08-10 19:25:32,063 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-18"
}
```
2026-08-10 19:25:32,064 INFO     29 [qwen-vl-parser] page=10 classify=table report_date=2026-03-18
2026-08-10 19:25:32,085 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1607363, prompt_len=756
2026-08-10 19:25:33,836 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:25:33.833+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 90, "failed": 0, "current": {"dbb9d9e294ee11f1bd9827cf206dfa2d": {"id": "dbb9d9e294ee11f1bd9827cf206dfa2d", "doc_id": "db844cb494ee11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 14828427, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388903475, "task_type": "dataflow", "root_trace_id": "9d9ed785184e435b9d8a5693cadbcf94", "root_traceparent": "00-9d9ed785184e435b9d8a5693cadbcf94-7ebd92d2185d496c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:25:35,740 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:25:35,740 INFO     29 [qwen-vl-text] LLM output (len=412):
{
  "exam_date": "2024-06-20",
  "report_date": "2024-06-21",
  "exam_name": "胸部正位片",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "胸外科",
  "bed_number": "1-33床",
  "findings": "双侧胸廓对称，气管、纵隔居中，右肺纹理模糊，左肺野清晰，双肺纹理走行自然。心脏、大血管影未见异常。双侧膈面光滑，双侧肋膈角稍钝。右侧胸腔引流管，右侧胸壁软组织积气。",
  "conclusion": "右肺术后改变。\n双侧肋膈角稍钝。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:25:35,743 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778727, prompt_len=936
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["住院", "取报告48小时", "可扫码查", "影像诊断报告书", "性别：女", "年龄：67岁", "病区：胸外科", "病床：1-33床", "病案号：80", "时间：2024-06-20 15:03:45", "检查项目：胸部正位片", "影像表现： 双侧胸廓对称，气管、纵隔居中，右肺纹理模糊，左肺野清晰，", "双肺纹理走行自然。心脏、大血管影未见异常。双侧膈面光滑，双侧", "肋膈角稍钝。右侧胸腔引流管，右侧胸壁软组织积气。", "影像诊断：右肺术后改变。", "双侧肋膈角稍钝。", "报告医师：", "审核医师：", "报告时间：", "17:26:30审核时间：", "2024-06-21", "07:53:41"]

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
2026-08-10 19:25:40,563 INFO     29 [qwen-vl-parser] table API response (len=1349):
\begin{tabular}{cccccc}
\hline
\textbf{检验项目} & \textbf{结果} & \textbf{参考区间} & \textbf{单位} & \textbf{检验项目} & \textbf{结果} & \textbf{参考区间} & \textbf{单位} \\
\hline
1 ★白细胞计数 & 6.58 & 4.00~10.00 & 10^9/L & 18红细胞体积分布宽度-CV & 13.4 & 11.0~16.0 & \% \\
2 中性粒细胞\% & 63.90 & 50.00~70.00 & \% & 19红细胞体积分布宽度-SD & 43.7 & 37.0~54.0 & f1 \\
3 淋巴细胞\% & 25.60 & 20.00~40.00 & \% & 20有核红细胞绝对计数 & 0.00 & 0.00~0.02 & 10^9/L \\
4 单核细胞\% & 9.70 $\uparrow$ & 3.00~8.00 & \% & 21有核红细胞/白细胞 & 0.00 & $<$1.00 & \% \\
5 嗜酸性粒细胞\% & 0.50 & 0.00~5.00 & \% & 22★血小板计数 & 378 $\uparrow$ & 100~300 & 10^9/L \\
6 嗜碱性粒细胞\% & 0.30 & 0.00~1.00 & \% & 23血小板比容 & 0.37 $\uparrow$ & 0.06~0.28 & \% \\
7 中性粒细胞绝对数 & 4.21 & 1.50~7.00 & 10^9/L & 24平均血小板体积 & 9.9 & 6.4~12.1 & f1 \\
8 淋巴细胞绝对数 & 1.68 & 0.80~4.00 & 10^9/L & 25血小板体积分布宽度 & 16.5 & 9.0~17.0 & \% \\
9 单核细胞绝对数 & 0.64 & 0.12~0.80 & 10^9/L & 26大血小板比率 & 24.80 & 13.00~43.00 & \% \\
10嗜酸性粒细胞绝对数 & 0.03 & 0.00~0.50 & 10^9/L & 27C-反应蛋白 & 97.64 $\uparrow$ & 0~8.00 & mg/L \\
11嗜碱性粒细胞绝对数 & 0.02 & 0.00~0.10 & 10^9/L & & & & \\
12★红细胞计数 & 4.55 & 3.50~6.00 & 10^12/L & & & & \\
13★血红蛋白 & 131.0 & 120.0~165.0 & g/L & & & & \\
14★红细胞比积 & 39.7 $\downarrow$ & 40.0~50.0 & \% & & & & \\
15★平均红细胞体积 & 87.2 & 80.0~100.0 & f1 & & & & \\
16平均红细胞血红蛋白含量 & 28.7 & 27.3~34.4 & pg & & & & \\
17平均红细胞血红蛋白浓度 & 330.0 & 320.0~360.0 & g/L & & & & \\
\hline
\end{tabular}
2026-08-10 19:25:40,565 INFO     29 [qwen-vl-parser] page=10 table: 24 LaTeX lines (bbox 379-402)
2026-08-10 19:25:40,566 INFO     29 [qwen-vl-parser] page=10 table: 24 sections
2026-08-10 19:25:40,710 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=901550, prompt_len=764
2026-08-10 19:25:42,106 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-18"
}
```
2026-08-10 19:25:42,107 INFO     29 [qwen-vl-parser] page=11 classify=table report_date=2026-03-18
2026-08-10 19:25:42,116 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=901550, prompt_len=756
2026-08-10 19:25:46,753 INFO     29 [qwen-vl-parser] table API response (len=872):
\begin{tabular}{l c c c c c}
\hline
\textbf{检验项目} & \textbf{结果} & \textbf{提示} & \textbf{参考区间} & \textbf{单位} \\
\hline
1 ★凝血酶原时间(PT) & 14.8 & & 11.0$\sim$15.0 & 秒 \\
2 国际标准化比值(INR) & 1.18 & & & \\
3 凝血酶原活动度 & 76.0 & & 70.0$\sim$150.0 & \% \\
4 ★活化部分凝血活酶时间(APTT) & 44.8 & $\uparrow$ & 28.0$\sim$42.0 & 秒 \\
5 活化部分凝血活酶时间比值 & 1.32 & & & \\
6 ★纤维蛋白原(FIB) & 9.79 & $\uparrow$ & 2.00$\sim$4.00 & g/L \\
7 ★凝血酶时间(TT) & 19.8 & & 14.0$\sim$21.0 & 秒 \\
8 ★D-二聚体(D-DI) & 7.28 & $\uparrow$ & 0.00$\sim$0.50 & ug/ml \\
\hline
\end{tabular}

\begin{tabular}{l l l l l l}
\hline
\multicolumn{2}{l}{申请时间 2026-03-16 10:33} & \multicolumn{4}{l}{采样者 杨美满} \\
\multicolumn{2}{l}{采样时间 2026-03-18 08:30} & \multicolumn{4}{l}{审核时间 2026-03-18 12:52} \\
\multicolumn{2}{l}{打印时间} & \multicolumn{2}{l}{接收者 赵俊} & \multicolumn{2}{l}{检验者 刘} \\
\multicolumn{6}{l}{带“★”者为省医疗单位互认项目。} \\
\hline
\end{tabular}
2026-08-10 19:25:46,756 INFO     29 [qwen-vl-parser] page=11 table: 24 LaTeX lines (bbox 403-426)
2026-08-10 19:25:46,756 INFO     29 [qwen-vl-parser] page=11 table: 24 sections
2026-08-10 19:25:46,968 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1755732, prompt_len=764
2026-08-10 19:25:47,225 INFO     29 [qwen-vl-text] coord API raw response (len=1752):
[
	{"text": "住院", "bbox": [860, 32, 930, 57]},
	{"text": "取报告48小时", "bbox": [93, 103, 230, 117]},
	{"text": "可扫码查", "bbox": [93, 119, 168, 133]},
	{"text": "影像诊断报告书", "bbox": [369, 109, 644, 135]},
	{"text": "性别：女", "bbox": [295, 145, 378, 160], "bbox": [295, 145, 378, 160]},
	{"text": "年龄：67岁", "bbox": [497, 145, 603, 160], "bbox": [497, 145, 603, 160]},
	{"text": "病区：胸外科", "bbox": [295, 168, 419, 183], "bbox": [295, 168, 419, 183]},
	{"text": "病床：1-33床", "bbox": [497, 168, 624, 183], "bbox": [497, 168, 624, 183]},
	{"text": "病案号：80", "bbox": [699, 168, 809, 183], "bbox": [699, 168, 809, 183]},
	{"text": "时间：2024-06-20 15:03:45", "bbox": [93, 192, 392, 207], "bbox": [93, 192, 392, 207]},
	{"text": "检查项目：胸部正位片", "bbox": [93, 243, 318, 262], "bbox": [93, 243, 318, 262]},
	{"text": "影像表现： 双侧胸廓对称，气管、纵隔居中，右肺纹理模糊，左肺野清晰，", "bbox": [93, 288, 876, 306], "bbox": [93, 288, 876, 306]},
	{"text": "双肺纹理走行自然。心脏、大血管影未见异常。双侧膈面光滑，双侧", "bbox": [202, 310, 900, 328], "bbox": [202, 310, 900, 328]},
	{"text": "肋膈角稍钝。右侧胸腔引流管，右侧胸壁软组织积气。", "bbox": [202, 332, 750, 350], "bbox": [202, 332, 750, 350]},
	{"text": "影像诊断：右肺术后改变。", "bbox": [94, 583, 355, 602], "bbox": [94, 583, 355, 602]},
	{"text": "双侧肋膈角稍钝。", "bbox": [203, 607, 378, 625], "bbox": [203, 607, 378, 625]},
	{"text": "报告医师：", "bbox": [95, 855, 185, 870], "bbox": [95, 855, 185, 870]},
	{"text": "审核医师：", "bbox": [504, 855, 589, 870], "bbox": [504, 855, 589, 870]},
	{"text": "报告时间：", "bbox": [95, 896, 185, 911], "bbox": [95, 896, 185, 911]},
	{"text": "17:26:30审核时间：", "bbox": [419, 896, 589, 911], "bbox": [419, 896, 589, 911]},
	{"text": "2024-06-21", "bbox": [684, 897, 784, 910], "bbox": [684, 897, 784, 910]},
	{"text": "07:53:41", "bbox": [822, 897, 902, 910], "bbox": [822, 897, 902, 910]}
]
2026-08-10 19:25:47,226 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=11.5s
2026-08-10 19:25:47,226 INFO     29 [qwen-vl-text] coord item[0]: text=住院, bbox=[860, 32, 930, 57]
2026-08-10 19:25:47,226 INFO     29 [qwen-vl-text] coord item[1]: text=取报告48小时, bbox=[93, 103, 230, 117]
2026-08-10 19:25:47,226 INFO     29 [qwen-vl-text] coord item[2]: text=可扫码查, bbox=[93, 119, 168, 133]
2026-08-10 19:25:47,226 INFO     29 [qwen-vl-text] coord item[3]: text=影像诊断报告书, bbox=[369, 109, 644, 135]
2026-08-10 19:25:47,226 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[295, 145, 378, 160]
2026-08-10 19:25:47,226 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：67岁, bbox=[497, 145, 603, 160]
2026-08-10 19:25:47,226 INFO     29 [qwen-vl-text] coord item[6]: text=病区：胸外科, bbox=[295, 168, 419, 183]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[7]: text=病床：1-33床, bbox=[497, 168, 624, 183]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[8]: text=病案号：80, bbox=[699, 168, 809, 183]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[9]: text=时间：2024-06-20 15:03:45, bbox=[93, 192, 392, 207]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[10]: text=检查项目：胸部正位片, bbox=[93, 243, 318, 262]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[11]: text=影像表现： 双侧胸廓对称，气管、纵隔居中，右肺纹理模糊，左肺野清晰，, bbox=[93, 288, 876, 306]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[12]: text=双肺纹理走行自然。心脏、大血管影未见异常。双侧膈面光滑，双侧, bbox=[202, 310, 900, 328]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[13]: text=肋膈角稍钝。右侧胸腔引流管，右侧胸壁软组织积气。, bbox=[202, 332, 750, 350]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[14]: text=影像诊断：右肺术后改变。, bbox=[94, 583, 355, 602]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[15]: text=双侧肋膈角稍钝。, bbox=[203, 607, 378, 625]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[16]: text=报告医师：, bbox=[95, 855, 185, 870]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[17]: text=审核医师：, bbox=[504, 855, 589, 870]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[18]: text=报告时间：, bbox=[95, 896, 185, 911]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[19]: text=17:26:30审核时间：, bbox=[419, 896, 589, 911]
2026-08-10 19:25:47,227 INFO     29 [qwen-vl-text] coord item[20]: text=2024-06-21, bbox=[684, 897, 784, 910]
2026-08-10 19:25:47,228 INFO     29 [qwen-vl-text] coord item[21]: text=07:53:41, bbox=[822, 897, 902, 910]
2026-08-10 19:25:47,228 INFO     29 [qwen-vl-text] page=9 — 22/22 coords, api_time=11.5s
2026-08-10 19:25:47,228 INFO     29 [qwen-vl-text] new_positions (22):
[[9, 511.7, 553.35, 26.944, 47.994], [9, 55.335, 136.85, 86.726, 98.514], [9, 55.335, 99.96, 100.198, 111.98599999999999], [9, 219.55499999999998, 383.18, 91.77799999999999, 113.67], [9, 175.525, 224.91, 122.08999999999999, 134.72], [9, 295.715, 358.78499999999997, 122.08999999999999, 134.72], [9, 175.525, 249.30499999999998, 141.456, 154.08599999999998], [9, 295.715, 371.28, 141.456, 154.08599999999998], [9, 415.905, 481.35499999999996, 141.456, 154.08599999999998], [9, 55.335, 233.23999999999998, 161.664, 174.29399999999998], [9, 55.335, 189.20999999999998, 204.606, 220.60399999999998], [9, 55.335, 521.22, 242.49599999999998, 257.652], [9, 120.19, 535.5, 261.02, 276.176], [9, 120.19, 446.25, 279.544, 294.7], [9, 55.93, 211.225, 490.88599999999997, 506.88399999999996], [9, 120.785, 224.91, 511.094, 526.25], [9, 56.525, 110.07499999999999, 719.91, 732.54], [9, 299.88, 350.455, 719.91, 732.54], [9, 56.525, 110.07499999999999, 754.432, 767.062], [9, 249.30499999999998, 350.455, 754.432, 767.062], [9, 406.97999999999996, 466.47999999999996, 755.274, 766.22], [9, 489.09, 536.6899999999999, 755.274, 766.22]]
2026-08-10 19:25:47,228 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=17.7s
2026-08-10 19:25:47,228 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:25:47,231 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:25:47,231 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:25:47,231 INFO     29 [qwen-vl-text] positions(20): [[19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:25:47,231 INFO     29 [qwen-vl-text] page grouping: [19], lines per page: [20]
2026-08-10 19:25:48,317 INFO     29 [qwen-vl-text] page=19, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 19:25:48,318 INFO     29 [qwen-vl-text] LLM extraction start, text_len=586
2026-08-10 19:25:48,318 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:25:48,318 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 624, \"bbox_end\": 643, \"encounter_dates\": [\"2026-02-27\"], \"department\": \"新区胸外科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "放射(1)\n报告时间↓\n项目\n02-27 16:23\n双肺CT（平扫）\n开单科室 新区胸外科门诊\n诊断 肺恶性肿瘤个人史\n检查F\n审核医\n开单时间 2026-02-27 09:17\n气肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。\n报告日期 2026-02-27 16:23\n检查科室 新区医院医学影像科\n检查项目\n双肺CT（平扫）\n检查描述\n双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。\n检查结论/诊断\n双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。\n右肺术后改变，术区团片影、索条影，较前2025.09.19片局部稍大饱满，建议复查，必要时增强检查 双肺粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前范围稍大 主动脉及冠脉钙化 右侧胸腔积液，部分包裹性积液，较前稍增多 甲状腺密度不均，请结合颈部检查 以上请结合临床及其它检查",
    "role": "user"
  }
]
2026-08-10 19:25:50,644 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-18"}
```
2026-08-10 19:25:50,645 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2026-03-18
2026-08-10 19:25:50,661 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1755732, prompt_len=401
2026-08-10 19:25:58,246 INFO     29 [qwen-vl-parser] text API response (len=1393):
["病案号:", "11诊号:1K3392539b3", "血型:FEI/CI独|业冰(111)", "显像剂:18F-FDG", "血糖:5.1mmol/l活", "度:7.22mci注射部位:右手背静脉", "注射/显像间隔时间:54分钟采集方式:断层采集3D厚", "度:3.75mm采集仪器:Discovery MI", "临床诊断:肺部阴影", "简要病史:", "肺部鳞癌基线评估。既往:2025.12肋骨骨折。", "图像所见:", "空腹4hr以上,口服适量温水,静脉注射显像剂,平静休息后行躯干PET及CT断层显像,PET图像行衰减校正及迭代", "法重建,PET、CT图像行多层面、多幅显示,影像清晰。", "颈部PET/CT示眼球、眼眶、鼻咽部、颈面部、喉咽部、甲状腺及颈部其它软组织结构、密度、代谢分布未见明显", "异常。", "胸部PET/CT示左肺下叶基底段近肺门部见高代谢结节,大小约2.0cm×1.9cm,边界不清,SUVmax约10.2。左肺", "下叶远端见散在片絮状高密度影。左侧胸腔积液,部分呈包裹性。左侧胸膜见不均匀增厚,伴代谢增高,SUVmax约", "4.0。右肺上叶胸膜下见微小结节,直径约0.2cm,代谢未见异常增高。主动脉、心脏生理性显像。", "腹盆部PET/CT示肝左内叶包膜下见高代谢结节,SUVmax约5.4,CT显示密度轻微减低,边界不清。左侧肾上腺见", "高代谢小结节,SUVmax约3.2,CT扫描局部稍增厚。胆囊、脾脏、胰腺大小正常,未见异常密度和异常代谢影。十二指", "肠、双肾、右肾上腺、双输尿管、膀胱、前列腺及双侧精囊腺未见异常显像。腹腔内见多个形态不一、条管状、浓淡不", "一的正常肠影。", "淋巴结PET/CT示左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧锁骨区见多发淋巴结增大伴代谢增", "高,较大者位于纵隔7组,大小约3.2×1.0cm,SUVmax约3.3。", "骨骼、软组织及周围神经走行区PET/CT示左侧第8、9、10、11肋骨、右侧第6肋骨见骨质中断,部分伴骨赘形", "成,伴代谢增高,SUVmax约3.8。左侧腹横肌见结节状增厚伴高代谢,SUVmax约2.9。全身其余骨骼、软组织及周围神", "经未见异常代谢影像,骨质和肌肉密度未见明显改变。", "I", "诊断意见:", "1.左肺下叶基底段近肺门部MT;左侧胸膜弥漫种植转移;左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧", "锁骨区多发淋巴结增大伴高代谢,考虑转移可能;肝S4包膜下转移瘤;左下叶远端阻塞性炎症;左胸腔癌性胸水可能", "大;", "2.左侧腹横肌转移瘤待除;左侧肾上腺转移待除,建议定期复查;", "3.右肺上叶胸膜下少许炎性小结节;肝右叶少许小钙化灶;", "4.双侧多根肋骨骨折伴骨赘区域炎性摄取;", "5.全身其它部位18F-FDG PET/CT显像未见明显异常。", "报告医师:林晓强", "审核医师:", "复核医师:", "报告日期:2026-03-18", "地址:福州市鼓楼区新权路29号电话:0591-833116130591-86218247", "此报告仅供临床医师参考,不做证明使用。", "CS扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 19:25:58,247 INFO     29 [qwen-vl-parser] page=12 text: 45 lines (bbox 427-471)
2026-08-10 19:25:58,247 INFO     29 [qwen-vl-parser] page=12 text: 45 sections
2026-08-10 19:25:58,361 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=810626, prompt_len=764
2026-08-10 19:25:58,842 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:25:58,843 INFO     29 [qwen-vl-text] LLM output (len=589):
{
  "exam_date": "2026-02-27",
  "report_date": "2026-02-27",
  "exam_name": "双肺CT（平扫）",
  "exam_category": "imaging",
  "body_part": "双肺",
  "patient_name": null,
  "patient_gender": null,
  "department": "新区胸外科门诊",
  "bed_number": null,
  "findings": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。",
  "conclusion": "右肺术后改变，术区团片影、索条影，较前2025.09.19片局部稍大饱满，建议复查，必要时增强检查 双肺粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前范围稍大 主动脉及冠脉钙化 右侧胸腔积液，部分包裹性积液，较前稍增多 甲状腺密度不均，请结合颈部检查 以上请结合临床及其它检查",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:25:58,847 INFO     29 [qwen-vl-text] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=985492, prompt_len=1259
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["放射(1)", "报告时间↓", "项目", "02-27 16:23", "双肺CT（平扫）", "开单科室 新区胸外科门诊", "诊断 肺恶性肿瘤个人史", "检查F", "审核医", "开单时间 2026-02-27 09:17", "气肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。", "报告日期 2026-02-27 16:23", "检查科室 新区医院医学影像科", "检查项目", "双肺CT（平扫）", "检查描述", "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。", "检查结论/诊断", "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。", "右肺术后改变，术区团片影、索条影，较前2025.09.19片局部稍大饱满，建议复查，必要时增强检查 双肺粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前范围稍大 主动脉及冠脉钙化 右侧胸腔积液，部分包裹性积液，较前稍增多 甲状腺密度不均，请结合颈部检查 以上请结合临床及其它检查"]

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
2026-08-10 19:25:59,802 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-20"
}
```
2026-08-10 19:25:59,803 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=2026-03-20
2026-08-10 19:25:59,817 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=810626, prompt_len=401
2026-08-10 19:26:04,946 INFO     29 [qwen-vl-parser] text API response (len=827):
["福建医科大学附属协和医院", "肺功能检查报告单", "姓名：", "性别：男", "年龄：49 Years", "病区床号：", "科室：", "病案号：", "身高：163 cm", "体重：61 kg", "测试号：Z0280275PF20280320", "预计值 实测值 实/预", "VC MAX [L] 3.92 2.48 63.3", "FVC [L] 3.77 2.48 65.8", "FEV 1 [L] 3.10 2.22 71.8", "FEV1%FVC [%] 81.86 89.56 109.4", "PEF [L/B] 8.05 6.38 79.3", "FIF25 [L/B] 7.01 6.16 87.9", "FIF50 [L/B] 4.31 2.76 64.1", "FIF75 [L/B] 1.64 1.29 78.4", "FIF25-75 [L/B] 3.76 2.58 68.7", "MVV [L/min] 116.58", "TLC-SB [L] 5.94 4.72 79.4", "FRC-SB [L] 3.17 3.74 118.1", "RV-SB [L] 1.98 2.18 110.0", "RV/TLC-SB [%] 33.07 46.21 139.7", "FRC/TLC-SB [%] 54.09 79.16 146.3", "DLCO SB [mmol/min/kPa] 8.85 5.98 67.6", "DLCOc SB [mmol/min/kPa] 8.86 5.98 67.6", "DLCO/VA [mmol/min/kPa/L] 1.49 1.30 87.1", "DLCOc/VA [mmol/min/kPa/L] 1.49 1.30 87.1", "1 本报告仅供临床参考，不作为任何诊断证明。", "检查者：", "审核者：", "报告日期：2026/3/20"]
2026-08-10 19:26:04,946 INFO     29 [qwen-vl-parser] page=13 text: 35 lines (bbox 472-506)
2026-08-10 19:26:04,946 INFO     29 [qwen-vl-parser] page=13 text: 35 sections
2026-08-10 19:26:05,136 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1132510, prompt_len=764
2026-08-10 19:26:06,537 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-12"
}
```
2026-08-10 19:26:06,538 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=2026-03-12
2026-08-10 19:26:06,557 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1132510, prompt_len=401
2026-08-10 19:26:08,858 INFO     29 [qwen-vl-parser] text API response (len=338):
["姓", "住院", "性别：男", "年龄：40岁", "送检单位：本院", "送检科室：呼吸与危重症医学科 送检医生：黄世霜", "送检日期：2026-03-10", "临床诊断：肺炎。", "送检材料：左肺下叶粘膜组织", "肉眼所见：", "灰白组织7块，直径0.05-0.2cm。（包全）", "镜下所见：", "病理诊断：", "（左肺下叶粘膜组织）浸润性鳞状细胞癌。", "诊断医师：廖荣娥", "医生签名：廖荣娥", "报告时间：2026年03月12", "备注：", "1 本报告仅作临床医师参考；若发现病理诊断与临床不相符时请立即与我科联系。", "2 此报告需医生签名方为有效。", "本报告仅作临床医师参考", "联系电话： 0598-63067"]
2026-08-10 19:26:08,859 INFO     29 [qwen-vl-parser] page=14 text: 22 lines (bbox 507-528)
2026-08-10 19:26:08,859 INFO     29 [qwen-vl-parser] page=14 text: 22 sections
2026-08-10 19:26:08,859 INFO     29 [qwen-vl-parser] parse_pdf done: 529 sections from 14 pages.
2026-08-10 19:26:08,871 INFO     29 Close text detector.
2026-08-10 19:26:09,447 INFO     29 Close text recognizer.
2026-08-10 19:26:09,850 INFO     29 Close recognizer.
2026-08-10 19:26:10,237 INFO     29 Close recognizer.
2026-08-10 19:26:11,338 INFO     29 [qwen-vl-text] coord API raw response (len=2060):
[
	{"text": "放射(1)", "bbox": [14, 11, 64, 26]},
	{"text": "报告时间↓", "bbox": [29, 47, 80, 61], "bbox_2d": [29, 47, 80, 61]},
	{"text": "项目", "bbox": [98, 47, 117, 61], "bbox_2d": [98, 47, 117, 61]},
	{"text": "02-27 16:23", "bbox": [29, 81, 82, 95], "bbox_2d": [29, 81, 82, 95]},
	{"text": "双肺CT（平扫）", "bbox": [97, 81, 164, 95], "bbox_2d": [97, 81, 164, 95]},
	{"text": "开单科室 新区胸外科门诊", "bbox": [230, 87, 345, 101], "bbox_2d": [230, 87, 345, 101]},
	{"text": "诊断 肺恶性肿瘤个人史", "bbox": [230, 110, 355, 124], "bbox_2d": [230, 110, 355, 124]},
	{"text": "检查F", "bbox": [230, 134, 257, 147], "bbox_2d": [230, 134, 257, 147]},
	{"text": "审核医", "bbox": [230, 164, 268, 177], "bbox_2d": [230, 164, 268, 177]},
	{"text": "开单时间 2026-02-27 09:17", "bbox": [609, 87, 732, 100], "bbox_2d": [609, 87, 732, 100]},
	{"text": "气肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。", "bbox": [491, 134, 838, 147], "bbox_2d": [491, 134, 838, 147]},
	{"text": "报告日期 2026-02-27 16:23", "bbox": [609, 164, 732, 177], "bbox_2d": [609, 164, 732, 177]},
	{"text": "检查科室 新区医院医学影像科", "bbox": [798, 164, 931, 177], "bbox_2d": [798, 164, 931, 177]},
	{"text": "检查项目", "bbox": [237, 205, 280, 219], "bbox_2d": [237, 205, 280, 219]},
	{"text": "双肺CT（平扫）", "bbox": [260, 248, 329, 262], "bbox_2d": [260, 248, 329, 262]},
	{"text": "检查描述", "bbox": [237, 290, 280, 304], "bbox_2d": [237, 290, 280, 304]},
	{"text": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。", "bbox": [240, 333, 974, 368], "bbox_2d": [240, 333, 974, 368]},
	{"text": "检查结论/诊断", "bbox": [237, 396, 305, 410], "bbox_2d": [237, 396, 305, 410]},
	{"text": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。", "bbox": [240, 438, 974, 474], "bbox_2d": [240, 438, 974, 474]},
	{"text": "右肺术后改变，术区团片影、索条影，较前2025.09.19片局部稍大饱满，建议复查，必要时增强检查 双肺粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前范围稍大 主动脉及冠脉钙化 右侧胸腔积液，部分包裹性积液，较前稍增多 甲状腺密度不均，请结合颈部检查 以上请结合临床及其它检查", "bbox": [240, 479, 974, 516], "bbox_2d": [240, 479, 974, 516]}
]
2026-08-10 19:26:11,338 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=12.5s
2026-08-10 19:26:11,338 INFO     29 [qwen-vl-text] coord item[0]: text=放射(1), bbox=[14, 11, 64, 26]
2026-08-10 19:26:11,338 INFO     29 [qwen-vl-text] coord item[1]: text=报告时间↓, bbox=[29, 47, 80, 61]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[2]: text=项目, bbox=[98, 47, 117, 61]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[3]: text=02-27 16:23, bbox=[29, 81, 82, 95]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[4]: text=双肺CT（平扫）, bbox=[97, 81, 164, 95]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[5]: text=开单科室 新区胸外科门诊, bbox=[230, 87, 345, 101]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[6]: text=诊断 肺恶性肿瘤个人史, bbox=[230, 110, 355, 124]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[7]: text=检查F, bbox=[230, 134, 257, 147]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[8]: text=审核医, bbox=[230, 164, 268, 177]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[9]: text=开单时间 2026-02-27 09:17, bbox=[609, 87, 732, 100]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[10]: text=气肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。, bbox=[491, 134, 838, 147]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[11]: text=报告日期 2026-02-27 16:23, bbox=[609, 164, 732, 177]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[12]: text=检查科室 新区医院医学影像科, bbox=[798, 164, 931, 177]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[13]: text=检查项目, bbox=[237, 205, 280, 219]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[14]: text=双肺CT（平扫）, bbox=[260, 248, 329, 262]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[15]: text=检查描述, bbox=[237, 290, 280, 304]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[16]: text=双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。, bbox=[240, 333, 974, 368]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[17]: text=检查结论/诊断, bbox=[237, 396, 305, 410]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[18]: text=双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。, bbox=[240, 438, 974, 474]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] coord item[19]: text=右肺术后改变，术区团片影、索条影，较前2025.09.19片局部稍大饱满，建议复查，必要时增强检查 双肺粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前范围稍大 主动脉及冠脉钙化 右侧胸腔积液，部分包裹性积液，较前稍增多 甲状腺密度不均，请结合颈部检查 以上请结合临床及其它检查, bbox=[240, 479, 974, 516]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] page=19 — 20/20 coords, api_time=12.5s
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] new_positions (20):
[[19, 11.788, 53.888, 6.545, 15.469999999999999], [19, 24.418, 67.36, 27.965, 36.295], [19, 82.51599999999999, 98.514, 27.965, 36.295], [19, 24.418, 69.044, 48.195, 56.525], [19, 81.67399999999999, 138.088, 48.195, 56.525], [19, 193.66, 290.49, 51.765, 60.095], [19, 193.66, 298.90999999999997, 65.45, 73.78], [19, 193.66, 216.394, 79.72999999999999, 87.46499999999999], [19, 193.66, 225.656, 97.58, 105.315], [19, 512.778, 616.3439999999999, 51.765, 59.5], [19, 413.42199999999997, 705.596, 79.72999999999999, 87.46499999999999], [19, 512.778, 616.3439999999999, 97.58, 105.315], [19, 671.9159999999999, 783.9019999999999, 97.58, 105.315], [19, 199.554, 235.76, 121.975, 130.305], [19, 218.92, 277.018, 147.56, 155.89], [19, 199.554, 235.76, 172.54999999999998, 180.88], [19, 202.07999999999998, 820.108, 198.135, 218.95999999999998], [19, 199.554, 256.81, 235.61999999999998, 243.95], [19, 202.07999999999998, 820.108, 260.61, 282.03], [19, 202.07999999999998, 820.108, 285.005, 307.02]]
2026-08-10 19:26:11,339 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=1, time=24.1s
2026-08-10 19:26:11,339 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:26:11,340 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:26:11,340 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:26:11,340 INFO     29 [qwen-vl-text] positions(22): [[26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:26:11,340 INFO     29 [qwen-vl-text] page grouping: [26], lines per page: [22]
2026-08-10 19:26:11,526 INFO     29 [qwen-vl-text] page=26, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 19:26:11,527 INFO     29 [qwen-vl-text] LLM extraction start, text_len=601
2026-08-10 19:26:11,527 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:26:11,528 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3196, \"bbox_end\": 3217, \"encounter_dates\": [\"2025-09-19\"], \"department\": \"新区胸外科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "放射(1)\n报告时间↓ 项目\n09-19 13:48 双肺CT（平扫）\n报告号 8810332\n原始报告 原始图像 申请单 对比报告 复制\n开单科室 新区胸外科门诊 开单医\n开单时间 2025-09-19 08:07\n诊断 肺恶性肿瘤个人史\n检查目的 体格检查：神志清，挂冲一\n八泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。\n日期 2025-09-19 13:48 检查科室\n学影像科\n检查项目\n双肺CT（平扫）\n检查描述\n双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双\n肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。\n检查结论/诊断\n双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双\n肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。\n右肺术后改变，术区团片影、索条影，较前2025.6.20片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前略减少、部分减\n小 主动脉及冠脉钙化 右侧胸腔少量积液，较前稍增多 甲状腺密度不均，请结合颈部检查",
    "role": "user"
  }
]
2026-08-10 19:26:11,533 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:26:11.532+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 90, "failed": 0, "current": {"dbb9d9e294ee11f1bd9827cf206dfa2d": {"id": "dbb9d9e294ee11f1bd9827cf206dfa2d", "doc_id": "db844cb494ee11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 14828427, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388903475, "task_type": "dataflow", "root_trace_id": "9d9ed785184e435b9d8a5693cadbcf94", "root_traceparent": "00-9d9ed785184e435b9d8a5693cadbcf94-7ebd92d2185d496c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:26:11,824 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 19:26:11,824 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Parser:MedLink | outputs={"html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "json"}
2026-08-10 19:26:11,824 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 19:26:11,845 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:26:11,845 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 姓名\n[BBOX-1] 住址：福建省三明市尤溪县\n[BBOX-2] 性别：男\n[BBOX-3] 工作单位：/\n[BBOX-4] 年龄：49岁\n[BBOX-5] 入院日期：2026.03.16 10:21:29\n[BBOX-6] 婚姻：已婚\n[BBOX-7] 记录时间：2026.03.16 10:21:29\n[BBOX-8] 民族：汉族\n[BBOX-9] 病史陈述者：患者及家属\n[BBOX-10] 出生地：福建省三明市\n[BBOX-11] 病史可靠程度：基本可靠\n[BBOX-12] 职业(工种)：/\n[BBOX-13] 过敏史：未发现\n[BBOX-14] 主诉：确诊左下肺鳞癌4天。\n[BBOX-15] 现病史：缘于2026.03.05以“咳嗽、咳痰1月”就诊于尤溪县总医院，查“2026.03.06胸部\n[BBOX-16] 增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。”\n[BBOX-17] 于2026.03.09行“支气管镜检查+支气管粘膜活检术”，术顺，术后病理示：（左肺下叶粘\n[BBOX-18] 膜组织）浸润性鳞状细胞癌。\n[BBOX-19] 予抗感染、止咳、化痰后咳嗽、咳痰好转，\n[BBOX-20] 无头晕、头痛，无胸闷、胸痛，无畏冷、发热，无心悸、呼吸困难，无乏力、盗汗，无腹胀、腹痛，\n[BBOX-21] 无恶心、呕吐，无声音嘶哑、吞咽困难等不适。今为进一步诊治就诊我科，门诊拟“左下肺腺\n[BBOX-22] 癌”收治入院，自发病以来，精神、食欲、睡眠尚可，大、小便正常，体重近期未见明显增减。\n[BBOX-23] 既往史：平素身体健康，否认高血压，否认糖尿病，否认冠心病，否认肝炎、结核、菌痢、伤寒\n[BBOX-24] 等传染病史，否认其他手术史，否认输血史，否认外伤史，否认药物过敏史，预防接种按时完成。\n[BBOX-25] 个人史：生于原籍，否认长期外地居住史，否认疫区居留史，否认特殊化学品及放射线接触\n[BBOX-26] 史。有吸烟史20余年，否认饮酒。否认冶游史。\n[BBOX-27] 婚育史：已婚已育，配偶及孩子均体健。\n[BBOX-28] 家族史：父已故，母健在。其父有肺癌史。否认家族中有“肝炎、伤寒、结核”等传染病史，否\n[BBOX-29] 认家族中有其他遗传性疾病史。\n[BBOX-30] 体格检查\n[BBOX-31] T:36.5℃\n[BBOX-32] P:79次/分\n[BBOX-33] R:19次/分\n[BBOX-34] BP:112/69mmHg\n[BBOX-35] 一般情况：神志清楚，发育正常，营养良好，体型正常，正常面容，表情安静，自动体位，查\n[BBOX-36] 体合作，对答切题，步行入院。\n[BBOX-37] 第1页\n[BBOX-38] 皮肤粘膜：色泽正常，未见黄染，未见紫绀，未见色素沉着，未见皮疹，未见皮下出血。皮温\n[BBOX-39] 正常，湿度正常，弹性好，无水肿，未见肝掌，未见蜘蛛痣。\n[BBOX-40] 淋巴结：全身浅表淋巴结未触及。\n[BBOX-41] 头颅：大小正常，形状正常，头发分布正常，眼睑无浮肿，眼球无异常，巩膜无黄染，结膜正\n[BBOX-42] 常，角膜透明，瞳孔等大等圆，直径3mm，对光反射灵敏。耳廓无畸形，外耳道正常，无异常分泌\n[BBOX-43] 物，听力正常，无乳突压痛。双侧鼻唇沟对称，鼻中隔无偏曲，鼻腔通气畅，无副鼻窦区压痛。口\n[BBOX-44] 唇无紫绀，口腔粘膜完整，口腔无异味，伸舌居中，咽无充血，扁桃体无肿大，无脓点。\n[BBOX-45] 颈部：颈柔软，颈静脉无怒张，肝颈静脉回流征阴性，未见颈动脉异常搏动，气管居中，甲\n[BBOX-46] 状腺无肿大，无血管杂音。\n[BBOX-47] 胸部：胸廓无畸形，胸壁静脉未见，无皮下气肿，肋间隙正常。胸骨无压痛，胸廓挤压征阴\n[BBOX-48] 性，无男乳女化。\n[BBOX-49] 肺部：双侧呼吸运动匀称，双侧触觉语颤对称，叩诊音清，呼吸音清，未闻及干湿罗音，未\n[BBOX-50] 闻及胸膜摩擦音。\n[BBOX-51] 心脏：无心前区隆起，心尖搏动正常，位于第Ⅴ肋间，左锁骨中线内0.5cm处，未扪及震颤\n[BBOX-52] 及抬举样搏动，心界叩诊无扩大，心音清晰，心率79次/分，节律整齐，A2>P2，无杂音。心浊音界\n[BBOX-53] 大小如下图所示：\n[BBOX-54] 右(CM) 肋间 左(CM)\n[BBOX-55] 2 Ⅱ 2\n[BBOX-56] 2 Ⅲ 3.5\n[BBOX-57] 3 Ⅳ 5.5\n[BBOX-58] Ⅴ 8.0\n[BBOX-59] 注：左锁骨中线距前正中线8.5CM。\n[BBOX-60] 周围血管：脉率79次/分，节律整齐，无脉搏短绌，无奇脉，无交替脉，无毛细血管搏动征，\n[BBOX-61] 无Duroziez二重杂音，无大血管枪击音，无水冲脉。双侧足背动脉及桡动脉搏动良好对称。\n[BBOX-62] 腹部：腹平坦，呼吸运动自如，腹壁静脉未见怒张，腹壁皮肤无皮疹，无色素沉着，无腹纹，\n[BBOX-63] 无疤痕，无疝，未见胃肠型及蠕动波，无上腹部搏动。全腹软，无肌紧张，无压痛及反跳痛，未触\n[BBOX-64] 及包块，肝脏右肋下、剑突下未触及，胆囊未触及，莫菲氏征阴性，脾脏左肋下未触及，双肾未触\n[BBOX-65] 及，双侧输尿管径路无压痛，无液波震颤。鼓音，肝上界位于右锁骨中线上第Ⅳ肋间，肝区无叩\n[BBOX-66] 击痛，胃泡鼓音区存在，肾区无叩痛，移动性浊音阴性。肠鸣音正常，4次/分，未闻及振水音及血\n[BBOX-67] 第2页\n[BBOX-68] 管杂音。\n[BBOX-69] 肛门生殖器：肛门及外生殖器未见异常。\n[BBOX-70] 脊柱四肢：脊柱生理弯曲正常，活动度正常，脊柱无压痛，无叩击痛；各关节四肢形态正常。肢体无浮肿，无静脉曲张，无色素沉着，无溃疡。\n[BBOX-71] 神经系统：四肢肌力正常，肌张力正常，角膜反射、腹壁反射、肱二头肌、肱三头肌、桡反射、膝反射、跟腱反射正常，巴彬斯基征未引出，脑膜刺激征阴性。\n[BBOX-72] 专科情况\n[BBOX-73] 生命征平稳，神志清楚，浅表淋巴结未触及淋巴结肿大。胸廓对称无畸形，胸壁未见静脉曲张，双肺触觉语颤对称，双肺叩诊呈清音，双肺呼吸音清，未闻及明显干湿性啰音及摩擦音。心前区无隆起，心脏触诊未及震颤，心界叩诊无扩大，心律齐，各瓣音区心音正常，未闻及病理性杂音。腹平软。未见胃肠型及蠕动波，肝脏肋下未触及，无压痛及反跳痛。双下肢无浮肿。\n[BBOX-74] 辅助检查\n[BBOX-75] 出院诊断：\n[BBOX-76] 医生签名：\n[BBOX-77] 初步诊断：肺结节性质待查：\n[BBOX-78] 肺癌？\n[BBOX-79] 炎性假瘤？\n[BBOX-80] 医生签名：\n[BBOX-81] 第3页\n[BBOX-82] 测量结果:\n[BBOX-83] Lved:46.5 mm\n[BBOX-84] Lve5:28.9 mm\n[BBOX-85] La:26.6 mm\n[BBOX-86] Ao:25.7 mm\n[BBOX-87] Lvpw:8.5 mm\n[BBOX-88] Ivs:9.5 mm\n[BBOX-89] Rv:20.1 mm\n[BBOX-90] Ra-L:34.8 mm\n[BBOX-91] Ra-M:25.5 mm\n[BBOX-92] Pa:17.6 mm\n[BBOX-93] E:0.46 m/s\n[BBOX-94] A:0.63 m/s\n[BBOX-95] Hr:90 bpm\n[BBOX-96] Fb:37.8 %\n[BBOX-97] Bf:68.0 %(Teich)\n[BBOX-98] EDV:99.8 ml\n[BBOX-99] Sv:67.8 ml\n[BBOX-100] Co:6.1 L/min\n[BBOX-101] Ci:4.0 L/min. m²\n[BBOX-102] H:166 cm\n[BBOX-103] W:52.5 kg\n[BBOX-104] BSA:1.5 m²\n[BBOX-105] LVM:140.2 g\n[BBOX-106] LVMI:93.4 g/m²\n[BBOX-107] B':0.08 m/s\n[BBOX-108] A':0.10 m/s\n[BBOX-109] RWT:0.38\n[BBOX-110] E/A:0.7\n[BBOX-111] E/E':5.7\n[BBOX-112] 正常参考值(mm) 摘自中国成年人超声心动图检查测量指南《中华超声影像学杂志》2016.25(8):\n[BBOX-113] AO\n[BBOX-114] LA\n[BBOX-115] LV\n[BBOX-116] IVS\n[BBOX-117] RA\n[BBOX-118] RV\n[BBOX-119] PA\n[BBOX-120] LVMI\n[BBOX-121] EF(%)\n[BBOX-122] 0-1岁\n[BBOX-123] 8-15\n[BBOX-124] 8-18\n[BBOX-125] 17-31\n[BBOX-126] 1.5-4\n[BBOX-127] 17-32\n[BBOX-128] 7-12\n[BBOX-129] 6-12\n[BBOX-130] ≥55\n[BBOX-131] 1-6岁\n[BBOX-132] 15-21\n[BBOX-133] 14-21\n[BBOX-134] 27-35\n[BBOX-135] 3-5.5\n[BBOX-136] 26-37\n[BBOX-137] 8-14\n[BBOX-138] 10-16\n[BBOX-139] ≥55\n[BBOX-140] 6-10岁\n[BBOX-141] 17-23\n[BBOX-142] 17-24\n[BBOX-143] 30-38\n[BBOX-144] 5-7\n[BBOX-145] 30-39\n[BBOX-146] 10-15\n[BBOX-147] 14-18\n[BBOX-148] ≥55\n[BBOX-149] 10-14岁\n[BBOX-150] 18-27\n[BBOX-151] 19-30\n[BBOX-152] 32-50\n[BBOX-153] 5-10\n[BBOX-154] 34-47\n[BBOX-155] 11-17\n[BBOX-156] 16-20\n[BBOX-157] ≥55\n[BBOX-158] 成人(男)\n[BBOX-159] 27.7±5.7\n[BBOX-160] 31.1±3.9\n[BBOX-161] 46.2±4.0\n[BBOX-162] 8.9±1.3\n[BBOX-163] 44.4±4.7\n[BBOX-164] 22.3±3.9\n[BBOX-165] 20.1±3.2\n[BBOX-166] ≥125\n[BBOX-167] ≥55\n[BBOX-168] 成人(女)\n[BBOX-169] 25.9±3.5\n[BBOX-170] 29.4±5.8\n[BBOX-171] 43.2±3.3\n[BBOX-172] 8.1±1.3\n[BBOX-173] 41.5±4.7\n[BBOX-174] 21.1±3.6\n[BBOX-175] 19.2±3.1\n[BBOX-176] ≥115\n[BBOX-177] ≥55\n[BBOX-178] 检查描述:\n[BBOX-179] 二维及M型超声:\n[BBOX-180] 静息时未见节段性室壁运动功能异常(见图)。各组瓣膜形态未见异常。心包腔正常。室间隔连\n[BBOX-181] 续性完整，大血管位置关系正常，主一肺动脉无沟通。\n[BBOX-182] 多普勒:\n[BBOX-183] 三尖瓣反流最大压差17MMHG，估测肺动脉收缩压22MMHG。\n[BBOX-184] 彩色多普勒:\n[BBOX-185] 二尖瓣微量反流。三尖瓣轻度反流。主动脉瓣未见明显反流。肺动脉瓣轻度反流。\n[BBOX-186] 超声提示:\n[BBOX-187] 心脏结构及功能未见明显异常改变\n[BBOX-188] 记录医生:袁瑄宸 报告录入:黄玉云 检查医生:刘文坤 复审医生:\n[BBOX-189] 报告日期: 2026-03-17 16:38:04\n[BBOX-190] 检查日期: 2026-03-17\n[BBOX-191] (本报告仅供临床参考,不做任何证明。)\n[BBOX-192] CS 扫描全能王\n[BBOX-193] 3亿人都在用的扫描App\n[BBOX-194] 性别：男\n[BBOX-195] 年龄：49岁\n[BBOX-196] 门诊号：\n[BBOX-197] 检查部位：肺部\n[BBOX-198] 检查设备：GE-HD750\n[BBOX-199] 流水号：0013240579\n[BBOX-200] 检查技术：CT\n[BBOX-201] 影像学所见：\n[BBOX-202] 双肺纹理清晰，左肺下叶见团块软组织密度影，病灶内支气管闭塞，较大截面约7.6cm×\n[BBOX-203] 8.3cm，增强扫描不均匀强化，周围散在条索斑片影。右肺散在小结节，大者右肺上叶尖段见一\n[BBOX-204] 实性结节（Se4/Img46），大小约0.4cm×0.2cm。气管、余支气管通畅，纵隔及左肺门可见肿大\n[BBOX-205] 淋巴结，大者短径约1.0cm，左侧胸腔少-中量积液，部分为包裹性。左侧胸膜结节状增厚。\n[BBOX-206] 影像学诊断：\n[BBOX-207] 1.左肺下叶肿块，考虑MT伴周围阻塞性肺炎，请结合临床。\n[BBOX-208] 2.纵隔及左肺门肿大淋巴结，部分转移可能。\n[BBOX-209] 3.左侧胸膜增厚，转移可能。\n[BBOX-210] 4.右肺散在小结节，性质待定，建议随诊复查。\n[BBOX-211] 5.左侧胸腔少-中量积液，部分为包裹性。\n[BBOX-212] 报告医生：许志祥 /许志祥\n[BBOX-213] 审核医生：沈东挥\n[BBOX-214] 复核医生：\n[BBOX-215] 此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。\n[BBOX-216] 报告时间：2026-03-18\n[BBOX-217] CS 扫描全能王\n[BBOX-218] 3亿人都在用的扫描App\n[BBOX-219] 门诊号:\n[BBOX-220] 医院:\n[BBOX-221] 申请医生\n[BBOX-222] 申请科室\n[BBOX-223] 检查日期: 2026-03-17 10:58:32\n[BBOX-224] 检查医生\n[BBOX-225] 报告日期: 2026-03-17 11:11:03\n[BBOX-226] 报告医生: 蔡平\n[BBOX-227] 审核日期: 2026-03-17 11:11:03\n[BBOX-228] 审核医生: 蔡平\n[BBOX-229] 电轴(-30~90°): 29\n[BBOX-230] QRS时限(<120): 100\n[BBOX-231] P-R间期(120~200): 134\n[BBOX-232] Q-T间期(0~450): 344\n[BBOX-233] QTc(0~450): 444\n[BBOX-234] SV1: 1.26\n[BBOX-235] RV5(0~2.5): 2.02\n[BBOX-236] R+S: 3.28\n[BBOX-237] 心率(60~100): 100\n[BBOX-238] 临床诊断: 肺肿物\n[BBOX-239] 描述:\n[BBOX-240] 诊断: 窦性心律 ST段改变\n[BBOX-241] 报告状态 已审核\n[BBOX-242] 检查项目: 心电图(常规十二通道)\n[BBOX-243] 当前状态\n[BBOX-244] 走纸: 25mm/s\n[BBOX-245] 增益:10mm/mv\n[BBOX-246] 当前模式:普通模式\n[BBOX-247] 572\n[BBOX-248] 596\n[BBOX-249] 600\n[BBOX-250] 600\n[BBOX-251] 596\n[BBOX-252] 600\n[BBOX-253] 604\n[BBOX-254] 600\n[BBOX-255] 596\n[BBOX-256] 596\n[BBOX-257] 604\n[BBOX-258] 604\n[BBOX-259] 596\n[BBOX-260] 25mm/s 10mm/mv\n[BBOX-261] 105\n[BBOX-262] 101\n[BBOX-263] 100\n[BBOX-264] 100\n[BBOX-265] 101\n[BBOX-266] 100\n[BBOX-267] 100\n[BBOX-268] 100\n[BBOX-269] 101\n[BBOX-270] 101\n[BBOX-271] 100\n[BBOX-272] 100\n[BBOX-273] 101\n[BBOX-274] 100\n[BBOX-275] 100\n[BBOX-276] 102\n[BBOX-277] II\n[BBOX-278] III\n[BBOX-279] aVR\n[BBOX-280] aVL\n[BBOX-281] aVF\n[BBOX-282] V1\n[BBOX-283] V2\n[BBOX-284] V3\n[BBOX-285] V4\n[BBOX-286] V5\n[BBOX-287] V6\n[BBOX-288] 2026-03-17 10:59:32\n[BBOX-289] 版权所有 纳龙科技\n[BBOX-290] 检查部位：头颅\n[BBOX-291] 检查设备：飞利浦MR9 流水号：0013240580\n[BBOX-292] 检查技术：MR\n[BBOX-293] 检查参数：\n[BBOX-294] 影像学所见：\n[BBOX-295] 双侧大脑半球对称，灰白质对比正常，实质内未见明显异常信号，DWI未见异常高信号，SW\n[BBOX-296] I未见异常低信号，各脑沟、脑池未见增宽、变深，脑室系统未见增宽，中线结构居中，幕下小\n[BBOX-297] 脑、脑干未见异常信号，双侧桥小脑角区未见明显异常。颅骨骨质未见异常信号。增强后未见\n[BBOX-298] 明显强化。\n[BBOX-299] 影像学诊断：\n[BBOX-300] 颅脑MRI平扫及增强未见明显异常。\n[BBOX-301] 报告医生：林佳辉 /林佳辉\n[BBOX-302] 审核医生：陈明宏\n[BBOX-303] 复核医生：\n[BBOX-304] 此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。\n[BBOX-305] 报告时间：2026-03-19\n[BBOX-306] \\begin{tabular}{ccccccll}\n[BBOX-307] 报告时间: 2026-03-18\n[BBOX-308] \\hline\n[BBOX-309] \\textbf{检验项目} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考区间} & \\textbf{单位} & \\textbf{方法} \\\\\n[BBOX-310] \\hline\n[BBOX-311] 1 & ★乙肝病毒表面抗原 & 0.00 & 阴性(-) & $<$0.05 & IU/ml & 学发光定量分析 \\\\\n[BBOX-312] 2 & ★乙肝病毒表面抗体 & 47.62 & 阳性(+) & $<$10 & mIU/ml & 学发光定量分析 \\\\\n[BBOX-313] 3 & ★乙肝病毒e抗原 & 0.41 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\\\\n[BBOX-314] 4 & ★乙肝病毒e抗体 & 1.29 & 阴性(-) & $>$1 & S/CO & 化学发光法YP \\\\\n[BBOX-315] 5 & ★乙肝病毒核心抗体 & 2.01 & 阳性(+) & $<$1 & S/CO & 化学发光法YP \\\\\n[BBOX-316] 6 & ★丙型肝炎病毒抗体 & 0.11 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\\\\n[BBOX-317] 7 & ★人免疫缺陷病毒抗原抗体 & 0.07 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\\\\n[BBOX-318] 8 & ★梅毒螺旋体特异抗体 & 0.11 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\\\\n[BBOX-319] \\hline\n[BBOX-320] \\end{tabular}\n[BBOX-321] \\begin{tabular}{cccccc}\n[BBOX-322] 报告时间: 2026-03-18\n[BBOX-323] \\hline\n[BBOX-324] \\multicolumn{2}{c}{检验项目} & 结果 & 参考区间 & 单位 & \\\\\n[BBOX-325] \\hline\n[BBOX-326] 1 & ★总胆红素[TBIL] & 10.6 & 0.0~23.0 & umol/L & \\\\\n[BBOX-327] 2 & ★直接胆红素[DBIL] & 1.4 & 0.0~8.0 & umol/L & \\\\\n[BBOX-328] 3 & 间接胆红素[IBIL] & 9.2 & 0.0~20.0 & umol/L & \\\\\n[BBOX-329] 4 & ★总蛋白[TP] & 81.8 & 65.0~85.0 & g/L & \\\\\n[BBOX-330] 5 & ★白蛋白[ALB] & 37.3 & 40.0~55.0 & g/L & \\\\\n[BBOX-331] 6 & 球蛋白[GLB] & 44.5 & 20.0~35.0 & g/L & \\\\\n[BBOX-332] 7 & 白球比例[A/G] & 0.84 & 1.09~2.50 & & \\\\\n[BBOX-333] 8 & ★丙氨酸氨基转移酶 & 39 & 9~50 & IU/L & \\\\\n[BBOX-334] 9 & ★天冬氨酸氨基转移酶 & 27 & 15~40 & IU/L & \\\\\n[BBOX-335] 10 & AST/ALT & 0.69 & & & \\\\\n[BBOX-336] 11 & ★γ-谷氨酰转肽酶 & 79 & 10~60 & IU/L & \\\\\n[BBOX-337] 12 & ★碱性磷酸酶[ALP] & 146 & 45~125 & IU/L & \\\\\n[BBOX-338] 13 & ★甘油三酯[TG] & 0.98 & 0.40~1.86 & mmol/L & \\\\\n[BBOX-339] 14 & ★总胆固醇[CHOL] & 4.73 & 3.40~6.10 & mmol/L & \\\\\n[BBOX-340] 15 & ★高密度脂蛋白胆固醇 & 0.77 & 0.90~1.90 & mmol/L & \\\\\n[BBOX-341] 16 & 非高密度脂蛋白胆固醇 & 3.96 & & & \\\\\n[BBOX-342] 17 & ★低密度脂蛋白胆固醇 & 3.37 & 1.10~3.50 & mmol/L & \\\\\n[BBOX-343] 18 & ★载脂蛋白A1[APOA1] & 0.76 & 1.00~1.60 & g/L & \\\\\n[BBOX-344] 19 & ★载脂蛋白B[APOB] & 1.09 & 0.60~1.10 & g/L & \\\\\n[BBOX-345] 20 & 载脂蛋白A1：B & 0.70 & & & \\\\\n[BBOX-346] \\hline\n[BBOX-347] \\multicolumn{6}{l}{※标本状态：符合检测要求} \\\\\n[BBOX-348] \\hline\n[BBOX-349] \\multicolumn{3}{l}{不件时间 2026-03-18 08:30} & \\multicolumn{3}{l}{申请时间 2026-03-16 10:33} \\\\\n[BBOX-350] \\multicolumn{3}{l}{打印时间} & \\multicolumn{3}{l}{接收时间 2026-03-18 10:05} \\\\\n[BBOX-351] \\multicolumn{3}{l}{带“★”者为省医疗单位互认项目。} & \\multicolumn{3}{l}{接收者 \\quad \\quad \\quad 检验者 \\quad \\quad \\quad 审核者} \\\\\n[BBOX-352] \\hline\n[BBOX-353] \\end{tabular}\n[BBOX-354] \\begin{tabular}{cccccc}\n[BBOX-355] 报告时间: 2026-03-18\n[BBOX-356] \\hline\n[BBOX-357] \\multicolumn{2}{c}{检验项目} & 结果 & 参考区间 & 单位 & \\\\\n[BBOX-358] \\hline\n[BBOX-359] 21 & ★尿素[UREA] & 4.1 & 3.1~7.4 & mmol/L & \\\\\n[BBOX-360] 22 & ★肌酐[CREA] & 68 & 57~97 & umol/L & \\\\\n[BBOX-361] 23 & UREA/CREA & 0.06 & & & \\\\\n[BBOX-362] 24 & ★尿酸[URIC] & 183 & 130~430 & umol/L & \\\\\n[BBOX-363] 25 & ★葡萄糖[GLU] & 5.21 & 3.90~6.10 & mmol/L & \\\\\n[BBOX-364] 26 & ★乳酸脱氢酶[LDH] & 162 & 120~250 & IU/L & \\\\\n[BBOX-365] 27 & ★肌酸激酶[CK] & 36 & 22~270 & IU/L & \\\\\n[BBOX-366] 28 & 肌酸激酶MB亚型 & 17.0 & 2.0~25.0 & IU/L & \\\\\n[BBOX-367] 29 & CKMB/CK & 0.47 & & & \\\\\n[BBOX-368] 30 & ★钾[K] & 4.50 & 3.50~5.50 & mmol/L & \\\\\n[BBOX-369] 31 & ★钠[NA] & 138.4 & 135.0~148.0 & mmol/L & \\\\\n[BBOX-370] 32 & ★氯[CL] & 96.3 & 96.0~112.0 & mmol/L & \\\\\n[BBOX-371] 33 & ★钙[CA] & 2.35 & 2.10~2.70 & mmol/L & \\\\\n[BBOX-372] 34 & 碳酸氢盐[HC03] & 27.3 & 20.1~29.0 & mmol/L & \\\\\n[BBOX-373] 35 & ★镁[MG] & 0.99 & 0.70~1.10 & mmol/L & \\\\\n[BBOX-374] 36 & ★无机磷酸盐[P] & 1.27 & 0.83~1.48 & mmol/L & \\\\\n[BBOX-375] 37 & 阴离子间隙[AG] & 19 & & & \\\\\n[BBOX-376] 38 & 渗透压[OSM] & 286 & & & \\\\\n[BBOX-377] \\hline\n[BBOX-378] \\end{tabular}\n[BBOX-379] \\begin{tabular}{cccccc}\n[BBOX-380] 报告时间: 2026-03-18\n[BBOX-381] \\hline\n[BBOX-382] \\textbf{检验项目} & \\textbf{结果} & \\textbf{参考区间} & \\textbf{单位} & \\textbf{检验项目} & \\textbf{结果} & \\textbf{参考区间} & \\textbf{单位} \\\\\n[BBOX-383] \\hline\n[BBOX-384] 1 ★白细胞计数 & 6.58 & 4.00~10.00 & 10^9/L & 18红细胞体积分布宽度-CV & 13.4 & 11.0~16.0 & \\% \\\\\n[BBOX-385] 2 中性粒细胞\\% & 63.90 & 50.00~70.00 & \\% & 19红细胞体积分布宽度-SD & 43.7 & 37.0~54.0 & f1 \\\\\n[BBOX-386] 3 淋巴细胞\\% & 25.60 & 20.00~40.00 & \\% & 20有核红细胞绝对计数 & 0.00 & 0.00~0.02 & 10^9/L \\\\\n[BBOX-387] 4 单核细胞\\% & 9.70 $\\uparrow$ & 3.00~8.00 & \\% & 21有核红细胞/白细胞 & 0.00 & $<$1.00 & \\% \\\\\n[BBOX-388] 5 嗜酸性粒细胞\\% & 0.50 & 0.00~5.00 & \\% & 22★血小板计数 & 378 $\\uparrow$ & 100~300 & 10^9/L \\\\\n[BBOX-389] 6 嗜碱性粒细胞\\% & 0.30 & 0.00~1.00 & \\% & 23血小板比容 & 0.37 $\\uparrow$ & 0.06~0.28 & \\% \\\\\n[BBOX-390] 7 中性粒细胞绝对数 & 4.21 & 1.50~7.00 & 10^9/L & 24平均血小板体积 & 9.9 & 6.4~12.1 & f1 \\\\\n[BBOX-391] 8 淋巴细胞绝对数 & 1.68 & 0.80~4.00 & 10^9/L & 25血小板体积分布宽度 & 16.5 & 9.0~17.0 & \\% \\\\\n[BBOX-392] 9 单核细胞绝对数 & 0.64 & 0.12~0.80 & 10^9/L & 26大血小板比率 & 24.80 & 13.00~43.00 & \\% \\\\\n[BBOX-393] 10嗜酸性粒细胞绝对数 & 0.03 & 0.00~0.50 & 10^9/L & 27C-反应蛋白 & 97.64 $\\uparrow$ & 0~8.00 & mg/L \\\\\n[BBOX-394] 11嗜碱性粒细胞绝对数 & 0.02 & 0.00~0.10 & 10^9/L & & & & \\\\\n[BBOX-395] 12★红细胞计数 & 4.55 & 3.50~6.00 & 10^12/L & & & & \\\\\n[BBOX-396] 13★血红蛋白 & 131.0 & 120.0~165.0 & g/L & & & & \\\\\n[BBOX-397] 14★红细胞比积 & 39.7 $\\downarrow$ & 40.0~50.0 & \\% & & & & \\\\\n[BBOX-398] 15★平均红细胞体积 & 87.2 & 80.0~100.0 & f1 & & & & \\\\\n[BBOX-399] 16平均红细胞血红蛋白含量 & 28.7 & 27.3~34.4 & pg & & & & \\\\\n[BBOX-400] 17平均红细胞血红蛋白浓度 & 330.0 & 320.0~360.0 & g/L & & & & \\\\\n[BBOX-401] \\hline\n[BBOX-402] \\end{tabular}\n[BBOX-403] \\begin{tabular}{l c c c c c}\n[BBOX-404] 报告时间: 2026-03-18\n[BBOX-405] \\hline\n[BBOX-406] \\textbf{检验项目} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考区间} & \\textbf{单位} \\\\\n[BBOX-407] \\hline\n[BBOX-408] 1 ★凝血酶原时间(PT) & 14.8 & & 11.0$\\sim$15.0 & 秒 \\\\\n[BBOX-409] 2 国际标准化比值(INR) & 1.18 & & & \\\\\n[BBOX-410] 3 凝血酶原活动度 & 76.0 & & 70.0$\\sim$150.0 & \\% \\\\\n[BBOX-411] 4 ★活化部分凝血活酶时间(APTT) & 44.8 & $\\uparrow$ & 28.0$\\sim$42.0 & 秒 \\\\\n[BBOX-412] 5 活化部分凝血活酶时间比值 & 1.32 & & & \\\\\n[BBOX-413] 6 ★纤维蛋白原(FIB) & 9.79 & $\\uparrow$ & 2.00$\\sim$4.00 & g/L \\\\\n[BBOX-414] 7 ★凝血酶时间(TT) & 19.8 & & 14.0$\\sim$21.0 & 秒 \\\\\n[BBOX-415] 8 ★D-二聚体(D-DI) & 7.28 & $\\uparrow$ & 0.00$\\sim$0.50 & ug/ml \\\\\n[BBOX-416] \\hline\n[BBOX-417] \\end{tabular}\n[BBOX-418] \\begin{tabular}{l l l l l l}\n[BBOX-419] 报告时间: 2026-03-18\n[BBOX-420] \\hline\n[BBOX-421] \\multicolumn{2}{l}{申请时间 2026-03-16 10:33} & \\multicolumn{4}{l}{采样者 杨美满} \\\\\n[BBOX-422] \\multicolumn{2}{l}{采样时间 2026-03-18 08:30} & \\multicolumn{4}{l}{审核时间 2026-03-18 12:52} \\\\\n[BBOX-423] \\multicolumn{2}{l}{打印时间} & \\multicolumn{2}{l}{接收者 赵俊} & \\multicolumn{2}{l}{检验者 刘} \\\\\n[BBOX-424] \\multicolumn{6}{l}{带“★”者为省医疗单位互认项目。} \\\\\n[BBOX-425] \\hline\n[BBOX-426] \\end{tabular}\n[BBOX-427] 病案号:\n[BBOX-428] 11诊号:1K3392539b3\n[BBOX-429] 血型:FEI/CI独|业冰(111)\n[BBOX-430] 显像剂:18F-FDG\n[BBOX-431] 血糖:5.1mmol/l活\n[BBOX-432] 度:7.22mci注射部位:右手背静脉\n[BBOX-433] 注射/显像间隔时间:54分钟采集方式:断层采集3D厚\n[BBOX-434] 度:3.75mm采集仪器:Discovery MI\n[BBOX-435] 临床诊断:肺部阴影\n[BBOX-436] 简要病史:\n[BBOX-437] 肺部鳞癌基线评估。既往:2025.12肋骨骨折。\n[BBOX-438] 图像所见:\n[BBOX-439] 空腹4hr以上,口服适量温水,静脉注射显像剂,平静休息后行躯干PET及CT断层显像,PET图像行衰减校正及迭代\n[BBOX-440] 法重建,PET、CT图像行多层面、多幅显示,影像清晰。\n[BBOX-441] 颈部PET/CT示眼球、眼眶、鼻咽部、颈面部、喉咽部、甲状腺及颈部其它软组织结构、密度、代谢分布未见明显\n[BBOX-442] 异常。\n[BBOX-443] 胸部PET/CT示左肺下叶基底段近肺门部见高代谢结节,大小约2.0cm×1.9cm,边界不清,SUVmax约10.2。左肺\n[BBOX-444] 下叶远端见散在片絮状高密度影。左侧胸腔积液,部分呈包裹性。左侧胸膜见不均匀增厚,伴代谢增高,SUVmax约\n[BBOX-445] 4.0。右肺上叶胸膜下见微小结节,直径约0.2cm,代谢未见异常增高。主动脉、心脏生理性显像。\n[BBOX-446] 腹盆部PET/CT示肝左内叶包膜下见高代谢结节,SUVmax约5.4,CT显示密度轻微减低,边界不清。左侧肾上腺见\n[BBOX-447] 高代谢小结节,SUVmax约3.2,CT扫描局部稍增厚。胆囊、脾脏、胰腺大小正常,未见异常密度和异常代谢影。十二指\n[BBOX-448] 肠、双肾、右肾上腺、双输尿管、膀胱、前列腺及双侧精囊腺未见异常显像。腹腔内见多个形态不一、条管状、浓淡不\n[BBOX-449] 一的正常肠影。\n[BBOX-450] 淋巴结PET/CT示左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧锁骨区见多发淋巴结增大伴代谢增\n[BBOX-451] 高,较大者位于纵隔7组,大小约3.2×1.0cm,SUVmax约3.3。\n[BBOX-452] 骨骼、软组织及周围神经走行区PET/CT示左侧第8、9、10、11肋骨、右侧第6肋骨见骨质中断,部分伴骨赘形\n[BBOX-453] 成,伴代谢增高,SUVmax约3.8。左侧腹横肌见结节状增厚伴高代谢,SUVmax约2.9。全身其余骨骼、软组织及周围神\n[BBOX-454] 经未见异常代谢影像,骨质和肌肉密度未见明显改变。\n[BBOX-455] I\n[BBOX-456] 诊断意见:\n[BBOX-457] 1.左肺下叶基底段近肺门部MT;左侧胸膜弥漫种植转移;左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧\n[BBOX-458] 锁骨区多发淋巴结增大伴高代谢,考虑转移可能;肝S4包膜下转移瘤;左下叶远端阻塞性炎症;左胸腔癌性胸水可能\n[BBOX-459] 大;\n[BBOX-460] 2.左侧腹横肌转移瘤待除;左侧肾上腺转移待除,建议定期复查;\n[BBOX-461] 3.右肺上叶胸膜下少许炎性小结节;肝右叶少许小钙化灶;\n[BBOX-462] 4.双侧多根肋骨骨折伴骨赘区域炎性摄取;\n[BBOX-463] 5.全身其它部位18F-FDG PET/CT显像未见明显异常。\n[BBOX-464] 报告医师:林晓强\n[BBOX-465] 审核医师:\n[BBOX-466] 复核医师:\n[BBOX-467] 报告日期:2026-03-18\n[BBOX-468] 地址:福州市鼓楼区新权路29号电话:0591-833116130591-86218247\n[BBOX-469] 此报告仅供临床医师参考,不做证明使用。\n[BBOX-470] CS扫描全能王\n[BBOX-471] 3亿人都在用的扫描App\n[BBOX-472] 福建医科大学附属协和医院\n[BBOX-473] 肺功能检查报告单\n[BBOX-474] 姓名：\n[BBOX-475] 性别：男\n[BBOX-476] 年龄：49 Years\n[BBOX-477] 病区床号：\n[BBOX-478] 科室：\n[BBOX-479] 病案号：\n[BBOX-480] 身高：163 cm\n[BBOX-481] 体重：61 kg\n[BBOX-482] 测试号：Z0280275PF20280320\n[BBOX-483] 预计值 实测值 实/预\n[BBOX-484] VC MAX [L] 3.92 2.48 63.3\n[BBOX-485] FVC [L] 3.77 2.48 65.8\n[BBOX-486] FEV 1 [L] 3.10 2.22 71.8\n[BBOX-487] FEV1%FVC [%] 81.86 89.56 109.4\n[BBOX-488] PEF [L/B] 8.05 6.38 79.3\n[BBOX-489] FIF25 [L/B] 7.01 6.16 87.9\n[BBOX-490] FIF50 [L/B] 4.31 2.76 64.1\n[BBOX-491] FIF75 [L/B] 1.64 1.29 78.4\n[BBOX-492] FIF25-75 [L/B] 3.76 2.58 68.7\n[BBOX-493] MVV [L/min] 116.58\n[BBOX-494] TLC-SB [L] 5.94 4.72 79.4\n[BBOX-495] FRC-SB [L] 3.17 3.74 118.1\n[BBOX-496] RV-SB [L] 1.98 2.18 110.0\n[BBOX-497] RV/TLC-SB [%] 33.07 46.21 139.7\n[BBOX-498] FRC/TLC-SB [%] 54.09 79.16 146.3\n[BBOX-499] DLCO SB [mmol/min/kPa] 8.85 5.98 67.6\n[BBOX-500] DLCOc SB [mmol/min/kPa] 8.86 5.98 67.6\n[BBOX-501] DLCO/VA [mmol/min/kPa/L] 1.49 1.30 87.1\n[BBOX-502] DLCOc/VA [mmol/min/kPa/L] 1.49 1.30 87.1\n[BBOX-503] 1 本报告仅供临床参考，不作为任何诊断证明。\n[BBOX-504] 检查者：\n[BBOX-505] 审核者：\n[BBOX-506] 报告日期：2026/3/20\n[BBOX-507] 姓\n[BBOX-508] 住院\n[BBOX-509] 性别：男\n[BBOX-510] 年龄：40岁\n[BBOX-511] 送检单位：本院\n[BBOX-512] 送检科室：呼吸与危重症医学科 送检医生：黄世霜\n[BBOX-513] 送检日期：2026-03-10\n[BBOX-514] 临床诊断：肺炎。\n[BBOX-515] 送检材料：左肺下叶粘膜组织\n[BBOX-516] 肉眼所见：\n[BBOX-517] 灰白组织7块，直径0.05-0.2cm。（包全）\n[BBOX-518] 镜下所见：\n[BBOX-519] 病理诊断：\n[BBOX-520] （左肺下叶粘膜组织）浸润性鳞状细胞癌。\n[BBOX-521] 诊断医师：廖荣娥\n[BBOX-522] 医生签名：廖荣娥\n[BBOX-523] 报告时间：2026年03月12\n[BBOX-524] 备注：\n[BBOX-525] 1 本报告仅作临床医师参考；若发现病理诊断与临床不相符时请立即与我科联系。\n[BBOX-526] 2 此报告需医生签名方为有效。\n[BBOX-527] 本报告仅作临床医师参考\n[BBOX-528] 联系电话： 0598-63067"
  }
]
2026-08-10 19:26:26,233 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:26:26,233 INFO     29 [qwen-vl-text] LLM output (len=563):
{
  "exam_date": "2025-09-19",
  "report_date": "2025-09-19",
  "exam_name": "双肺CT（平扫）",
  "exam_category": "imaging",
  "body_part": "双肺",
  "patient_name": null,
  "patient_gender": null,
  "department": "新区胸外科门诊",
  "bed_number": null,
  "findings": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。",
  "conclusion": "右肺术后改变，术区团片影、索条影，较前2025.6.20片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前略减少、部分减小 主动脉及冠脉钙化 右侧胸腔少量积液，较前稍增多 甲状腺密度不均，请结合颈部检查",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:26:26,235 INFO     29 [qwen-vl-text] coord API call start, page=26, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=854434, prompt_len=1280
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["放射(1)", "报告时间↓ 项目", "09-19 13:48 双肺CT（平扫）", "报告号 8810332", "原始报告 原始图像 申请单 对比报告 复制", "开单科室 新区胸外科门诊 开单医", "开单时间 2025-09-19 08:07", "诊断 肺恶性肿瘤个人史", "检查目的 体格检查：神志清，挂冲一", "八泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。", "日期 2025-09-19 13:48 检查科室", "学影像科", "检查项目", "双肺CT（平扫）", "检查描述", "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双", "肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。", "检查结论/诊断", "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双", "肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。", "右肺术后改变，术区团片影、索条影，较前2025.6.20片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前略减少、部分减", "小 主动脉及冠脉钙化 右侧胸腔少量积液，较前稍增多 甲状腺密度不均，请结合颈部检查"]

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
2026-08-10 19:26:39,170 INFO     29 [qwen-vl-text] coord API raw response (len=2314):
[
	{"text": "放射(1)", "bbox": [35, 10, 84, 26]},
	{"text": "报告时间↓ 项目", "bbox": [50, 45, 135, 61], "bbox_2d": [50, 45, 135, 61]},
	{"text": "09-19 13:48 双肺CT（平扫）", "bbox": [50, 78, 180, 94], "bbox_2d": [50, 78, 180, 94]},
	{"text": "报告号 8810332", "bbox": [248, 45, 341, 61], "bbox_2d": [248, 45, 341, 61]},
	{"text": "原始报告 原始图像 申请单 对比报告 复制", "bbox": [688, 45, 965, 61], "bbox_2d": [688, 45, 965, 61]},
	{"text": "开单科室 新区胸外科门诊 开单医", "bbox": [243, 85, 453, 100], "bbox_2d": [243, 85, 453, 100]},
	{"text": "开单时间 2025-09-19 08:07", "bbox": [608, 85, 727, 99], "bbox_2d": [608, 85, 727, 99]},
	{"text": "诊断 肺恶性肿瘤个人史", "bbox": [243, 107, 363, 122], "bbox_2d": [243, 107, 363, 122]},
	{"text": "检查目的 体格检查：神志清，挂冲一", "bbox": [243, 129, 400, 143], "bbox_2d": [243, 129, 400, 143]},
	{"text": "八泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。", "bbox": [535, 130, 830, 144], "bbox_2d": [535, 130, 830, 144]},
	{"text": "日期 2025-09-19 13:48 检查科室", "bbox": [625, 159, 838, 173], "bbox_2d": [625, 159, 838, 173]},
	{"text": "学影像科", "bbox": [877, 158, 919, 169], "bbox_2d": [877, 158, 919, 169]},
	{"text": "检查项目", "bbox": [250, 201, 291, 215], "bbox_2d": [250, 201, 291, 215]},
	{"text": "双肺CT（平扫）", "bbox": [271, 243, 337, 258], "bbox_2d": [271, 243, 337, 258]},
	{"text": "检查描述", "bbox": [250, 284, 291, 298], "bbox_2d": [250, 284, 291, 298]},
	{"text": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双", "bbox": [271, 326, 958, 341], "bbox_2d": [271, 326, 958, 341]},
	{"text": "肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。", "bbox": [253, 347, 727, 361], "bbox_2d": [253, 347, 727, 361]},
	{"text": "检查结论/诊断", "bbox": [250, 387, 314, 401], "bbox_2d": [250, 387, 314, 401]},
	{"text": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双", "bbox": [271, 428, 958, 443], "bbox_2d": [271, 428, 958, 443]},
	{"text": "肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。", "bbox": [253, 449, 727, 463], "bbox_2d": [253, 449, 727, 463]},
	{"text": "右肺术后改变，术区团片影、索条影，较前2025.6.20片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前略减少、部分减", "bbox": [271, 469, 958, 484], "bbox_2d": [271, 469, 958, 484]},
	{"text": "小 主动脉及冠脉钙化 右侧胸腔少量积液，较前稍增多 甲状腺密度不均，请结合颈部检查", "bbox": [253, 490, 616, 504], "bbox_2d": [253, 490, 616, 504]},
	{"text": "共 1 份", "bbox": [42, 892, 77, 906], "bbox_2d": [42, 892, 77, 906]}
]
2026-08-10 19:26:39,171 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=12.9s
2026-08-10 19:26:39,171 INFO     29 [qwen-vl-text] coord item[0]: text=放射(1), bbox=[35, 10, 84, 26]
2026-08-10 19:26:39,171 INFO     29 [qwen-vl-text] coord item[1]: text=报告时间↓ 项目, bbox=[50, 45, 135, 61]
2026-08-10 19:26:39,171 INFO     29 [qwen-vl-text] coord item[2]: text=09-19 13:48 双肺CT（平扫）, bbox=[50, 78, 180, 94]
2026-08-10 19:26:39,171 INFO     29 [qwen-vl-text] coord item[3]: text=报告号 8810332, bbox=[248, 45, 341, 61]
2026-08-10 19:26:39,171 INFO     29 [qwen-vl-text] coord item[4]: text=原始报告 原始图像 申请单 对比报告 复制, bbox=[688, 45, 965, 61]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[5]: text=开单科室 新区胸外科门诊 开单医, bbox=[243, 85, 453, 100]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[6]: text=开单时间 2025-09-19 08:07, bbox=[608, 85, 727, 99]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[7]: text=诊断 肺恶性肿瘤个人史, bbox=[243, 107, 363, 122]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[8]: text=检查目的 体格检查：神志清，挂冲一, bbox=[243, 129, 400, 143]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[9]: text=八泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。, bbox=[535, 130, 830, 144]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[10]: text=日期 2025-09-19 13:48 检查科室, bbox=[625, 159, 838, 173]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[11]: text=学影像科, bbox=[877, 158, 919, 169]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[12]: text=检查项目, bbox=[250, 201, 291, 215]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[13]: text=双肺CT（平扫）, bbox=[271, 243, 337, 258]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[14]: text=检查描述, bbox=[250, 284, 291, 298]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[15]: text=双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双, bbox=[271, 326, 958, 341]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[16]: text=肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。, bbox=[253, 347, 727, 361]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[17]: text=检查结论/诊断, bbox=[250, 387, 314, 401]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[18]: text=双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双, bbox=[271, 428, 958, 443]
2026-08-10 19:26:39,172 INFO     29 [qwen-vl-text] coord item[19]: text=肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。, bbox=[253, 449, 727, 463]
2026-08-10 19:26:39,173 INFO     29 [qwen-vl-text] coord item[20]: text=右肺术后改变，术区团片影、索条影，较前2025.6.20片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前略减少、部分减, bbox=[271, 469, 958, 484]
2026-08-10 19:26:39,173 INFO     29 [qwen-vl-text] coord item[21]: text=小 主动脉及冠脉钙化 右侧胸腔少量积液，较前稍增多 甲状腺密度不均，请结合颈部检查, bbox=[253, 490, 616, 504]
2026-08-10 19:26:39,173 INFO     29 [qwen-vl-text] coord item[22]: text=共 1 份, bbox=[42, 892, 77, 906]
2026-08-10 19:26:39,173 INFO     29 [qwen-vl-text] page=26 — 22/22 coords, api_time=12.9s
2026-08-10 19:26:39,173 INFO     29 [qwen-vl-text] new_positions (22):
[[26, 29.47, 70.728, 5.949999999999999, 15.469999999999999], [26, 42.1, 113.67, 26.775, 36.295], [26, 42.1, 151.56, 46.41, 55.93], [26, 208.816, 287.122, 26.775, 36.295], [26, 579.2959999999999, 812.53, 26.775, 36.295], [26, 204.606, 381.426, 50.574999999999996, 59.5], [26, 511.936, 612.134, 50.574999999999996, 58.904999999999994], [26, 204.606, 305.646, 63.665, 72.59], [26, 204.606, 336.8, 76.755, 85.085], [26, 450.46999999999997, 698.86, 77.35, 85.67999999999999], [26, 526.25, 705.596, 94.60499999999999, 102.935], [26, 738.434, 773.798, 94.00999999999999, 100.55499999999999], [26, 210.5, 245.022, 119.595, 127.925], [26, 228.182, 283.75399999999996, 144.58499999999998, 153.51], [26, 210.5, 245.022, 168.98, 177.31], [26, 228.182, 806.636, 193.97, 202.89499999999998], [26, 213.02599999999998, 612.134, 206.465, 214.795], [26, 210.5, 264.388, 230.265, 238.595], [26, 228.182, 806.636, 254.66, 263.585], [26, 213.02599999999998, 612.134, 267.155, 275.485], [26, 228.182, 806.636, 279.055, 287.97999999999996], [26, 213.02599999999998, 518.672, 291.55, 299.88]]
2026-08-10 19:26:39,173 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=27.8s
2026-08-10 19:26:39,173 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:26:39,182 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:26:39,182 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:26:39,182 INFO     29 [qwen-vl-text] positions(33): [[27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:26:39,182 INFO     29 [qwen-vl-text] page grouping: [27], lines per page: [33]
2026-08-10 19:26:39,374 INFO     29 [qwen-vl-text] page=27, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 19:26:39,377 INFO     29 [qwen-vl-text] LLM extraction start, text_len=710
2026-08-10 19:26:39,377 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:26:39,378 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3225, \"bbox_end\": 3257, \"encounter_dates\": [\"2025-09-19\"], \"department\": \"新区胸外科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告时间↓ 项目\n报告号 RMZZ_1001883808\n原始报告 原始图像 申请单 对比报告 复\n检验(5)\n检查(3)\n09-19 10:33 肝胆胰脾肾彩超\n开单科室 新区胸外科门诊 开单医\n龙\n开单时间 2025-09-19 08:07\n门诊病历\n诊断 肺恶性肿瘤^\\史\n检查目的\n清，精神可，手术切\n，无红肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。\n门急诊病历(2)\n报\n报告日期 2025-09-19 10:33 检查科室 -\n检查检验报告\n实验室(2)\n放射(1)\n超声(1)\n检查项目\n肝胆胰脾肾彩超\n检查描述\n超声显示:肝脏大小、形态可，被膜光整，肝左叶探及一个无回声区，大小约10×6mm，形态规则，边界清，壁薄、光滑，内透声可；余实质回声尚均匀，肝内管道纹\n理清晰，门静脉管腔通畅，血流信号未见明显异常。胆囊大小、形态正常，壁光滑，不厚，胆囊腔内透声清晰，未显示明确异常回声。超声切面图像可显示的胰腺大小、\n形态正常，轮廓清，受胃肠气体干扰，超声切面图像可显示的部分胰腺实质回声尚未见明显异常，主胰管无扩张，胰周区域动静脉血管走行正常。CDFI：胰腺及周围未见\n明显异常血流信号。脾脏大小、形态正常，被膜光滑，实质回声均匀，未见明显占位性病变，脾门部脾静脉内径正常。CDFI：脾动、静脉充盈良好，走行正常。双肾大\n小、形态正常，双肾被膜轮廓规整，实质呈低回声，皮髓质界限清晰，双肾集合系统回声未见明显异常。CDFI：双肾血流灌注在正常范围。双侧肾上腺区肠气干扰明显，\n可显示区域未探及明显异常回声包块。\n检查结论/诊断\n符合肝囊肿声像图。必要时结合临床或其他检查。\n共1份",
    "role": "user"
  }
]
2026-08-10 19:26:39,696 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:26:39,718 INFO     29 [SmartSplitter] SmartSplitter done: 13 chunks from 13 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'ExaminationReport': 7, 'LabReport': 5}
2026-08-10 19:26:39,728 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 19:26:39,728 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks": "13 items, types={'AdmissionRecord': 1, 'ExaminationReport': 7, 'LabReport': 5}"}
2026-08-10 19:26:39,728 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 19:26:39,729 INFO     29 [ChunkRouter] Routed 13 chunks into 3 groups: {'chunks_Admission': 1, 'chunks_Examination': 7, 'chunks_LabExam': 5}
2026-08-10 19:26:39,737 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 19:26:39,738 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks": "13 items, types={'AdmissionRecord': 1, 'ExaminationReport': 7, 'LabReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:26:39,738 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 19:26:39,744 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:26:39,745 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:26:39,745 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[7]
2026-08-10 19:26:39,745 INFO     29 [qwen-vl-table] positions ： [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:26:39,930 INFO     29 [qwen-vl-table] page=7, rect=842x595, img=(2339x1653)
2026-08-10 19:26:39,930 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:26:39,931 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 306, \"bbox_end\": 320, \"encounter_dates\": [\"2026-03-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccll}\n报告时间: 2026-03-18\n\\hline\n\\textbf{检验项目} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考区间} & \\textbf{单位} & \\textbf{方法} \\\\\n\\hline\n1 & ★乙肝病毒表面抗原 & 0.00 & 阴性(-) & $<$0.05 & IU/ml & 学发光定量分析 \\\\\n2 & ★乙肝病毒表面抗体 & 47.62 & 阳性(+) & $<$10 & mIU/ml & 学发光定量分析 \\\\\n3 & ★乙肝病毒e抗原 & 0.41 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\\\\n4 & ★乙肝病毒e抗体 & 1.29 & 阴性(-) & $>$1 & S/CO & 化学发光法YP \\\\\n5 & ★乙肝病毒核心抗体 & 2.01 & 阳性(+) & $<$1 & S/CO & 化学发光法YP \\\\\n6 & ★丙型肝炎病毒抗体 & 0.11 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\\\\n7 & ★人免疫缺陷病毒抗原抗体 & 0.07 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\\\\n8 & ★梅毒螺旋体特异抗体 & 0.11 & 阴性(-) & $<$1 & S/CO & 化学发光法YP \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:26:43,796 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:26:43.795+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 90, "failed": 0, "current": {"dbb9d9e294ee11f1bd9827cf206dfa2d": {"id": "dbb9d9e294ee11f1bd9827cf206dfa2d", "doc_id": "db844cb494ee11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 14828427, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388903475, "task_type": "dataflow", "root_trace_id": "9d9ed785184e435b9d8a5693cadbcf94", "root_traceparent": "00-9d9ed785184e435b9d8a5693cadbcf94-7ebd92d2185d496c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:26:49,416 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:26:49,416 INFO     29 [qwen-vl-text] LLM output (len=735):
{
  "exam_date": "2025-09-19",
  "report_date": "2025-09-19",
  "exam_name": "肝胆胰脾肾彩超",
  "exam_category": "imaging",
  "body_part": "肝胆胰脾肾",
  "patient_name": null,
  "patient_gender": null,
  "department": "新区胸外科门诊",
  "bed_number": null,
  "findings": "超声显示:肝脏大小、形态可，被膜光整，肝左叶探及一个无回声区，大小约10×6mm，形态规则，边界清，壁薄、光滑，内透声可；余实质回声尚均匀，肝内管道纹理清晰，门静脉管腔通畅，血流信号未见明显异常。胆囊大小、形态正常，壁光滑，不厚，胆囊腔内透声清晰，未显示明确异常回声。超声切面图像可显示的胰腺大小、形态正常，轮廓清，受胃肠气体干扰，超声切面图像可显示的部分胰腺实质回声尚未见明显异常，主胰管无扩张，胰周区域动静脉血管走行正常。CDFI：胰腺及周围未见明显异常血流信号。脾脏大小、形态正常，被膜光滑，实质回声均匀，未见明显占位性病变，脾门部脾静脉内径正常。CDFI：脾动、静脉充盈良好，走行正常。双肾大小、形态正常，双肾被膜轮廓规整，实质呈低回声，皮髓质界限清晰，双肾集合系统回声未见明显异常。CDFI：双肾血流灌注在正常范围。双侧肾上腺区肠气干扰明显，可显示区域未探及明显异常回声包块。",
  "conclusion": "符合肝囊肿声像图。必要时结合临床或其他检查。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:26:49,420 INFO     29 [qwen-vl-text] coord API call start, page=27, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1006039, prompt_len=1423
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["报告时间↓ 项目", "报告号 RMZZ_1001883808", "原始报告 原始图像 申请单 对比报告 复", "检验(5)", "检查(3)", "09-19 10:33 肝胆胰脾肾彩超", "开单科室 新区胸外科门诊 开单医", "龙", "开单时间 2025-09-19 08:07", "门诊病历", "诊断 肺恶性肿瘤^\\史", "检查目的", "清，精神可，手术切", "，无红肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。", "门急诊病历(2)", "报", "报告日期 2025-09-19 10:33 检查科室 -", "检查检验报告", "实验室(2)", "放射(1)", "超声(1)", "检查项目", "肝胆胰脾肾彩超", "检查描述", "超声显示:肝脏大小、形态可，被膜光整，肝左叶探及一个无回声区，大小约10×6mm，形态规则，边界清，壁薄、光滑，内透声可；余实质回声尚均匀，肝内管道纹", "理清晰，门静脉管腔通畅，血流信号未见明显异常。胆囊大小、形态正常，壁光滑，不厚，胆囊腔内透声清晰，未显示明确异常回声。超声切面图像可显示的胰腺大小、", "形态正常，轮廓清，受胃肠气体干扰，超声切面图像可显示的部分胰腺实质回声尚未见明显异常，主胰管无扩张，胰周区域动静脉血管走行正常。CDFI：胰腺及周围未见", "明显异常血流信号。脾脏大小、形态正常，被膜光滑，实质回声均匀，未见明显占位性病变，脾门部脾静脉内径正常。CDFI：脾动、静脉充盈良好，走行正常。双肾大", "小、形态正常，双肾被膜轮廓规整，实质呈低回声，皮髓质界限清晰，双肾集合系统回声未见明显异常。CDFI：双肾血流灌注在正常范围。双侧肾上腺区肠气干扰明显，", "可显示区域未探及明显异常回声包块。", "检查结论/诊断", "符合肝囊肿声像图。必要时结合临床或其他检查。", "共1份"]

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
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord API raw response (len=2144):
[
	{"text": "报告时间↓ 项目", "bbox": [114, 75, 204, 100]},
	{"text": "报告号 RMZZ_1001883808", "bbox": [304, 75, 445, 100]},
	{"text": "原始报告 原始图像 申请单 对比报告 复", "bbox": [722, 75, 984, 100]},
	{"text": "检验(5)", "bbox": [16, 96, 57, 114]},
	{"text": "检查(3)", "bbox": [16, 120, 57, 138]},
	{"text": "09-19 10:33 肝胆胰脾肾彩超", "bbox": [100, 108, 250, 132]},
	{"text": "开单科室 新区胸外科门诊 开单医", "bbox": [304, 114, 504, 134]},
	{"text": "龙", "bbox": [538, 114, 547, 134]},
	{"text": "开单时间 2025-09-19 08:07", "bbox": [650, 114, 762, 134]},
	{"text": "门诊病历", "bbox": [3, 145, 51, 163]},
	{"text": "诊断 肺恶性肿瘤^\\史", "bbox": [304, 134, 420, 154]},
	{"text": "检查目的", "bbox": [304, 154, 348, 174]},
	{"text": "清，精神可，手术切", "bbox": [409, 154, 494, 174]},
	{"text": "，无红肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。", "bbox": [535, 154, 856, 174]},
	{"text": "门急诊病历(2)", "bbox": [16, 170, 84, 188]},
	{"text": "报", "bbox": [477, 182, 488, 200]},
	{"text": "报告日期 2025-09-19 10:33 检查科室 -", "bbox": [649, 182, 865, 200]},
	{"text": "检查检验报告", "bbox": [3, 194, 68, 212]},
	{"text": "实验室(2)", "bbox": [16, 219, 65, 237]},
	{"text": "放射(1)", "bbox": [16, 244, 57, 262]},
	{"text": "超声(1)", "bbox": [16, 269, 57, 287]},
	{"text": "检查项目", "bbox": [312, 221, 351, 238]},
	{"text": "肝胆胰脾肾彩超", "bbox": [332, 260, 396, 277]},
	{"text": "检查描述", "bbox": [312, 297, 351, 313]},
	{"text": "超声显示:肝脏大小、形态可，被膜光整，肝左叶探及一个无回声区，大小约10×6mm，形态规则，边界清，壁薄、光滑，内透声可；余实质回声尚均匀，肝内管道纹", "bbox": [317, 335, 974, 352]},
	{"text": "理清晰，门静脉管腔通畅，血流信号未见明显异常。胆囊大小、形态正常，壁光滑，不厚，胆囊腔内透声清晰，未显示明确异常回声。超声切面图像可显示的胰腺大小、", "bbox": [315, 352, 970, 370]},
	{"text": "形态正常，轮廓清，受胃肠气体干扰，超声切面图像可显示的部分胰腺实质回声尚未见明显异常，主胰管无扩张，胰周区域动静脉血管走行正常。CDFI：胰腺及周围未见", "bbox": [315, 370, 971, 388]},
	{"text": "明显异常血流信号。脾脏大小、形态正常，被膜光滑，实质回声均匀，未见明显占位性病变，脾门部脾静脉内径正常。CDFI：脾动、静脉充盈良好，走行正常。双肾大", "bbox": [315, 388, 967, 406]},
	{"text": "小、形态正常，双肾被膜轮廓规整，实质呈低回声，皮髓质界限清晰，双肾集合系统回声未见明显异常。CDFI：双肾血流灌注在正常范围。双侧肾上腺区肠气干扰明显，", "bbox": [315, 406, 967, 424]},
	{"text": "可显示区域未探及明显异常回声包块。", "bbox": [315, 424, 461, 442]},
	{"text": "检查结论/诊断", "bbox": [312, 464, 372, 480]},
	{"text": "符合肝囊肿声像图。必要时结合临床或其他检查。", "bbox": [332, 502, 523, 518]},
	{"text": "共1份", "bbox": [114, 850, 147, 867]}
]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=13.6s
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间↓ 项目, bbox=[114, 75, 204, 100]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[1]: text=报告号 RMZZ_1001883808, bbox=[304, 75, 445, 100]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[2]: text=原始报告 原始图像 申请单 对比报告 复, bbox=[722, 75, 984, 100]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[3]: text=检验(5), bbox=[16, 96, 57, 114]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[4]: text=检查(3), bbox=[16, 120, 57, 138]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[5]: text=09-19 10:33 肝胆胰脾肾彩超, bbox=[100, 108, 250, 132]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[6]: text=开单科室 新区胸外科门诊 开单医, bbox=[304, 114, 504, 134]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[7]: text=龙, bbox=[538, 114, 547, 134]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[8]: text=开单时间 2025-09-19 08:07, bbox=[650, 114, 762, 134]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[9]: text=门诊病历, bbox=[3, 145, 51, 163]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[10]: text=诊断 肺恶性肿瘤^\史, bbox=[304, 134, 420, 154]
2026-08-10 19:27:03,040 INFO     29 [qwen-vl-text] coord item[11]: text=检查目的, bbox=[304, 154, 348, 174]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[12]: text=清，精神可，手术切, bbox=[409, 154, 494, 174]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[13]: text=，无红肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。, bbox=[535, 154, 856, 174]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[14]: text=门急诊病历(2), bbox=[16, 170, 84, 188]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[15]: text=报, bbox=[477, 182, 488, 200]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[16]: text=报告日期 2025-09-19 10:33 检查科室 -, bbox=[649, 182, 865, 200]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[17]: text=检查检验报告, bbox=[3, 194, 68, 212]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[18]: text=实验室(2), bbox=[16, 219, 65, 237]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[19]: text=放射(1), bbox=[16, 244, 57, 262]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[20]: text=超声(1), bbox=[16, 269, 57, 287]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[21]: text=检查项目, bbox=[312, 221, 351, 238]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[22]: text=肝胆胰脾肾彩超, bbox=[332, 260, 396, 277]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[23]: text=检查描述, bbox=[312, 297, 351, 313]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[24]: text=超声显示:肝脏大小、形态可，被膜光整，肝左叶探及一个无回声区，大小约10×6mm，形态规则，边界清，壁薄、光滑，内透声可；余实质回声尚均匀，肝内管道纹, bbox=[317, 335, 974, 352]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[25]: text=理清晰，门静脉管腔通畅，血流信号未见明显异常。胆囊大小、形态正常，壁光滑，不厚，胆囊腔内透声清晰，未显示明确异常回声。超声切面图像可显示的胰腺大小、, bbox=[315, 352, 970, 370]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[26]: text=形态正常，轮廓清，受胃肠气体干扰，超声切面图像可显示的部分胰腺实质回声尚未见明显异常，主胰管无扩张，胰周区域动静脉血管走行正常。CDFI：胰腺及周围未见, bbox=[315, 370, 971, 388]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[27]: text=明显异常血流信号。脾脏大小、形态正常，被膜光滑，实质回声均匀，未见明显占位性病变，脾门部脾静脉内径正常。CDFI：脾动、静脉充盈良好，走行正常。双肾大, bbox=[315, 388, 967, 406]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[28]: text=小、形态正常，双肾被膜轮廓规整，实质呈低回声，皮髓质界限清晰，双肾集合系统回声未见明显异常。CDFI：双肾血流灌注在正常范围。双侧肾上腺区肠气干扰明显，, bbox=[315, 406, 967, 424]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[29]: text=可显示区域未探及明显异常回声包块。, bbox=[315, 424, 461, 442]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[30]: text=检查结论/诊断, bbox=[312, 464, 372, 480]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[31]: text=符合肝囊肿声像图。必要时结合临床或其他检查。, bbox=[332, 502, 523, 518]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] coord item[32]: text=共1份, bbox=[114, 850, 147, 867]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] page=27 — 33/33 coords, api_time=13.6s
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] new_positions (33):
[[27, 95.988, 171.768, 44.625, 59.5], [27, 255.968, 374.69, 44.625, 59.5], [27, 607.924, 828.528, 44.625, 59.5], [27, 13.472, 47.994, 57.12, 67.83], [27, 13.472, 47.994, 71.39999999999999, 82.11], [27, 84.2, 210.5, 64.25999999999999, 78.53999999999999], [27, 255.968, 424.368, 67.83, 79.72999999999999], [27, 452.996, 460.574, 67.83, 79.72999999999999], [27, 547.3, 641.6039999999999, 67.83, 79.72999999999999], [27, 2.526, 42.942, 86.27499999999999, 96.985], [27, 255.968, 353.64, 79.72999999999999, 91.63], [27, 255.968, 293.01599999999996, 91.63, 103.53], [27, 344.378, 415.948, 91.63, 103.53], [27, 450.46999999999997, 720.752, 91.63, 103.53], [27, 13.472, 70.728, 101.14999999999999, 111.86], [27, 401.63399999999996, 410.89599999999996, 108.28999999999999, 119.0], [27, 546.458, 728.3299999999999, 108.28999999999999, 119.0], [27, 2.526, 57.256, 115.42999999999999, 126.14], [27, 13.472, 54.73, 130.305, 141.015], [27, 13.472, 47.994, 145.18, 155.89], [27, 13.472, 47.994, 160.055, 170.765], [27, 262.704, 295.542, 131.495, 141.60999999999999], [27, 279.544, 333.432, 154.7, 164.815], [27, 262.704, 295.542, 176.715, 186.23499999999999], [27, 266.914, 820.108, 199.325, 209.44], [27, 265.23, 816.74, 209.44, 220.14999999999998], [27, 265.23, 817.582, 220.14999999999998, 230.85999999999999], [27, 265.23, 814.2139999999999, 230.85999999999999, 241.57], [27, 265.23, 814.2139999999999, 241.57, 252.28], [27, 265.23, 388.162, 252.28, 262.99], [27, 262.704, 313.224, 276.08, 285.59999999999997], [27, 279.544, 440.366, 298.69, 308.21], [27, 95.988, 123.774, 505.75, 515.865]]
2026-08-10 19:27:03,041 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=23.9s
2026-08-10 19:27:03,041 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:27:03,042 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:27:03,042 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:27:03,043 INFO     29 [qwen-vl-text] positions(18): [[29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:27:03,043 INFO     29 [qwen-vl-text] page grouping: [29], lines per page: [18]
2026-08-10 19:27:03,378 INFO     29 [qwen-vl-text] page=29, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 19:27:03,379 INFO     29 [qwen-vl-text] LLM extraction start, text_len=220
2026-08-10 19:27:03,379 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:03,379 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3328, \"bbox_end\": 3345, \"encounter_dates\": [\"2025-06-20\"], \"department\": \"新区胸外科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "心电图检查报告单\n检查时间：2025/6/20 9:39:04\n女\n心率：75bpm\nP-R间期：138ms\n诊断：窦性心律\n性\nSV1：0.71mV\nQRS时限：95ms\n大致正常心电图\n年龄：68岁\nRV5：1.26mV\nQT/QTc：409/457ms\n科室：新区胸外科门诊\nRV5+SV1：1.97mV\n电轴：7°\n25mm/s 10mm/mV\n(本报告仅供临床医师结合临床参考，不作诊断证明之用) 报告日期：2025/6/20 9",
    "role": "user"
  }
]
2026-08-10 19:27:03,388 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:03,388 INFO     29 [qwen-vl-table] page=7 LLM output (len=1370):
{
  "report_date": "2026-03-18",
  "items": [
    {
      "name": "乙肝病毒表面抗原",
      "item_code": null,
      "value": "0.00",
      "unit": "IU/ml",
      "reference_range": "<0.05",
      "abnormal": false
    },
    {
      "name": "乙肝病毒表面抗体",
      "item_code": null,
      "value": "47.62",
      "unit": "mIU/ml",
      "reference_range": "<10",
      "abnormal": true
    },
    {
      "name": "乙肝病毒e抗原",
      "item_code": null,
      "value": "0.41",
      "unit": "S/CO",
      "reference_range": "<1",
      "abnormal": false
    },
    {
      "name": "乙肝病毒e抗体",
      "item_code": null,
      "value": "1.29",
      "unit": "S/CO",
      "reference_range": ">1",
      "abnormal": false
    },
    {
      "name": "乙肝病毒核心抗体",
      "item_code": null,
      "value": "2.01",
      "unit": "S/CO",
      "reference_range": "<1",
      "abnormal": true
    },
    {
      "name": "丙型肝炎病毒抗体",
      "item_code": null,
      "value": "0.11",
      "unit": "S/CO",
      "reference_range": "<1",
      "abnormal": false
    },
    {
      "name": "人免疫缺陷病毒抗原抗体",
      "item_code": null,
      "value": "0.07",
      "unit": "S/CO",
      "reference_range": "<1",
      "abnormal": false
    },
    {
      "name": "梅毒螺旋体特异抗体",
      "item_code": null,
      "value": "0.11",
      "unit": "S/CO",
      "reference_range": "<1",
      "abnormal": false
    }
  ]
}
2026-08-10 19:27:03,389 INFO     29 [qwen-vl-table] coord grouping: {7: 8}
2026-08-10 19:27:03,390 INFO     29 [qwen-vl-table] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1001561, prompt_len=580
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
乙肝病毒表面抗原、乙肝病毒表面抗体、乙肝病毒e抗原、乙肝病毒e抗体、乙肝病毒核心抗体、丙型肝炎病毒抗体、人免疫缺陷病毒抗原抗体、梅毒螺旋体特异抗体

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
2026-08-10 19:27:06,536 INFO     29 [qwen-vl-table] coord API raw response (len=428):
[
	{"text": "乙肝病毒表面抗原", "bbox": [120, 275, 274, 298]},
	{"text": "乙肝病毒表面抗体", "bbox": [120, 304, 274, 327]},
	{"text": "乙肝病毒e抗原", "bbox": [120, 335, 248, 358]},
	{"text": "乙肝病毒e抗体", "bbox": [120, 364, 248, 387]},
	{"text": "乙肝病毒核心抗体", "bbox": [120, 393, 274, 416]},
	{"text": "丙型肝炎病毒抗体", "bbox": [120, 422, 274, 445]},
	{"text": "人免疫缺陷病毒抗原抗体", "bbox": [120, 452, 327, 475]},
	{"text": "梅毒螺旋体特异抗体", "bbox": [120, 481, 292, 504]}
]
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=3.1s
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord item[0]: text=乙肝病毒表面抗原, bbox=[120, 275, 274, 298]
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord item[1]: text=乙肝病毒表面抗体, bbox=[120, 304, 274, 327]
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord item[2]: text=乙肝病毒e抗原, bbox=[120, 335, 248, 358]
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord item[3]: text=乙肝病毒e抗体, bbox=[120, 364, 248, 387]
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord item[4]: text=乙肝病毒核心抗体, bbox=[120, 393, 274, 416]
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord item[5]: text=丙型肝炎病毒抗体, bbox=[120, 422, 274, 445]
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord item[6]: text=人免疫缺陷病毒抗原抗体, bbox=[120, 452, 327, 475]
2026-08-10 19:27:06,537 INFO     29 [qwen-vl-table] coord item[7]: text=梅毒螺旋体特异抗体, bbox=[120, 481, 292, 504]
2026-08-10 19:27:06,538 INFO     29 [qwen-vl-table] page=7 coord: matched 8/8, time=3.1s
2026-08-10 19:27:06,538 INFO     29 [qwen-vl-table] new_positions (8):
[[8, 101.03999999999999, 230.708, 163.625, 177.31], [8, 101.03999999999999, 230.708, 180.88, 194.565], [8, 101.03999999999999, 208.816, 199.325, 213.01], [8, 101.03999999999999, 208.816, 216.57999999999998, 230.265], [8, 101.03999999999999, 230.708, 233.83499999999998, 247.51999999999998], [8, 101.03999999999999, 230.708, 251.08999999999997, 264.775], [8, 101.03999999999999, 275.334, 268.94, 282.625], [8, 101.03999999999999, 245.864, 286.195, 299.88]]
2026-08-10 19:27:06,538 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=8, matched=8, pages=1, time=26.8s
2026-08-10 19:27:06,540 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:27:06,542 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:27:06,542 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8]
2026-08-10 19:27:06,542 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:27:06,792 INFO     29 [qwen-vl-table] page=8, rect=842x595, img=(2339x1653)
2026-08-10 19:27:06,793 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:06,793 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 321, \"bbox_end\": 353, \"encounter_dates\": [\"2026-03-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-03-18\n\\hline\n\\multicolumn{2}{c}{检验项目} & 结果 & 参考区间 & 单位 & \\\\\n\\hline\n1 & ★总胆红素[TBIL] & 10.6 & 0.0~23.0 & umol/L & \\\\\n2 & ★直接胆红素[DBIL] & 1.4 & 0.0~8.0 & umol/L & \\\\\n3 & 间接胆红素[IBIL] & 9.2 & 0.0~20.0 & umol/L & \\\\\n4 & ★总蛋白[TP] & 81.8 & 65.0~85.0 & g/L & \\\\\n5 & ★白蛋白[ALB] & 37.3 & 40.0~55.0 & g/L & \\\\\n6 & 球蛋白[GLB] & 44.5 & 20.0~35.0 & g/L & \\\\\n7 & 白球比例[A/G] & 0.84 & 1.09~2.50 & & \\\\\n8 & ★丙氨酸氨基转移酶 & 39 & 9~50 & IU/L & \\\\\n9 & ★天冬氨酸氨基转移酶 & 27 & 15~40 & IU/L & \\\\\n10 & AST/ALT & 0.69 & & & \\\\\n11 & ★γ-谷氨酰转肽酶 & 79 & 10~60 & IU/L & \\\\\n12 & ★碱性磷酸酶[ALP] & 146 & 45~125 & IU/L & \\\\\n13 & ★甘油三酯[TG] & 0.98 & 0.40~1.86 & mmol/L & \\\\\n14 & ★总胆固醇[CHOL] & 4.73 & 3.40~6.10 & mmol/L & \\\\\n15 & ★高密度脂蛋白胆固醇 & 0.77 & 0.90~1.90 & mmol/L & \\\\\n16 & 非高密度脂蛋白胆固醇 & 3.96 & & & \\\\\n17 & ★低密度脂蛋白胆固醇 & 3.37 & 1.10~3.50 & mmol/L & \\\\\n18 & ★载脂蛋白A1[APOA1] & 0.76 & 1.00~1.60 & g/L & \\\\\n19 & ★载脂蛋白B[APOB] & 1.09 & 0.60~1.10 & g/L & \\\\\n20 & 载脂蛋白A1：B & 0.70 & & & \\\\\n\\hline\n\\multicolumn{6}{l}{※标本状态：符合检测要求} \\\\\n\\hline\n\\multicolumn{3}{l}{不件时间 2026-03-18 08:30} & \\multicolumn{3}{l}{申请时间 2026-03-16 10:33} \\\\\n\\multicolumn{3}{l}{打印时间} & \\multicolumn{3}{l}{接收时间 2026-03-18 10:05} \\\\\n\\multicolumn{3}{l}{带“★”者为省医疗单位互认项目。} & \\multicolumn{3}{l}{接收者 \\quad \\quad \\quad 检验者 \\quad \\quad \\quad 审核者} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:27:13,879 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:13,880 INFO     29 [qwen-vl-text] LLM output (len=442):
{
  "exam_date": "2025-06-20",
  "report_date": "2025-06-20",
  "exam_name": "心电图检查",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "女",
  "department": "新区胸外科门诊",
  "bed_number": null,
  "findings": "心率：75bpm\nP-R间期：138ms\nSV1：0.71mV\nQRS时限：95ms\nRV5：1.26mV\nQT/QTc：409/457ms\nRV5+SV1：1.97mV\n电轴：7°\n25mm/s 10mm/mV",
  "conclusion": "诊断：窦性心律\n大致正常心电图",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:27:13,891 INFO     29 [qwen-vl-text] coord API call start, page=29, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5221495, prompt_len=887
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["心电图检查报告单", "检查时间：2025/6/20 9:39:04", "女", "心率：75bpm", "P-R间期：138ms", "诊断：窦性心律", "性", "SV1：0.71mV", "QRS时限：95ms", "大致正常心电图", "年龄：68岁", "RV5：1.26mV", "QT/QTc：409/457ms", "科室：新区胸外科门诊", "RV5+SV1：1.97mV", "电轴：7°", "25mm/s 10mm/mV", "(本报告仅供临床医师结合临床参考，不作诊断证明之用) 报告日期：2025/6/20 9"]

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
2026-08-10 19:27:20,098 INFO     29 [qwen-vl-text] coord API raw response (len=996):
[
	{"text": "心电图检查报告单", "bbox": [452, 25, 614, 55]},
	{"text": "检查时间：2025/6/20 9:39:04", "bbox": [677, 47, 856, 65]},
	{"text": "女", "bbox": [56, 81, 66, 100]},
	{"text": "心率：75bpm", "bbox": [240, 77, 320, 95]},
	{"text": "P-R间期：138ms", "bbox": [420, 77, 505, 95]},
	{"text": "诊断：窦性心律", "bbox": [618, 74, 701, 92]},
	{"text": "性", "bbox": [56, 110, 70, 129]},
	{"text": "SV1：0.71mV", "bbox": [257, 107, 325, 124]},
	{"text": "QRS时限：95ms", "bbox": [420, 107, 498, 124]},
	{"text": "大致正常心电图", "bbox": [650, 93, 738, 111]},
	{"text": "年龄：68岁", "bbox": [56, 140, 134, 159]},
	{"text": "RV5：1.26mV", "bbox": [258, 137, 326, 154]},
	{"text": "QT/QTc：409/457ms", "bbox": [424, 137, 528, 154]},
	{"text": "科室：新区胸外科门诊", "bbox": [56, 170, 197, 189]},
	{"text": "RV5+SV1：1.97mV", "bbox": [234, 167, 325, 185]},
	{"text": "电轴：7°", "bbox": [425, 167, 484, 185]},
	{"text": "25mm/s 10mm/mV", "bbox": [828, 201, 953, 220]},
	{"text": "(本报告仅供临床医师结合临床参考，不作诊断证明之用) 报告日期：2025/6/20 9", "bbox": [49, 852, 504, 871]}
]
2026-08-10 19:27:20,098 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=6.2s
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[0]: text=心电图检查报告单, bbox=[452, 25, 614, 55]
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[1]: text=检查时间：2025/6/20 9:39:04, bbox=[677, 47, 856, 65]
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[2]: text=女, bbox=[56, 81, 66, 100]
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[3]: text=心率：75bpm, bbox=[240, 77, 320, 95]
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[4]: text=P-R间期：138ms, bbox=[420, 77, 505, 95]
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[5]: text=诊断：窦性心律, bbox=[618, 74, 701, 92]
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[6]: text=性, bbox=[56, 110, 70, 129]
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[7]: text=SV1：0.71mV, bbox=[257, 107, 325, 124]
2026-08-10 19:27:20,099 INFO     29 [qwen-vl-text] coord item[8]: text=QRS时限：95ms, bbox=[420, 107, 498, 124]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[9]: text=大致正常心电图, bbox=[650, 93, 738, 111]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[10]: text=年龄：68岁, bbox=[56, 140, 134, 159]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[11]: text=RV5：1.26mV, bbox=[258, 137, 326, 154]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[12]: text=QT/QTc：409/457ms, bbox=[424, 137, 528, 154]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[13]: text=科室：新区胸外科门诊, bbox=[56, 170, 197, 189]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[14]: text=RV5+SV1：1.97mV, bbox=[234, 167, 325, 185]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[15]: text=电轴：7°, bbox=[425, 167, 484, 185]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[16]: text=25mm/s 10mm/mV, bbox=[828, 201, 953, 220]
2026-08-10 19:27:20,100 INFO     29 [qwen-vl-text] coord item[17]: text=(本报告仅供临床医师结合临床参考，不作诊断证明之用) 报告日期：2025/6/20 9, bbox=[49, 852, 504, 871]
2026-08-10 19:27:20,102 INFO     29 [qwen-vl-text] page=29 — 18/18 coords, api_time=6.2s
2026-08-10 19:27:20,102 INFO     29 [qwen-vl-text] new_positions (18):
[[29, 380.584, 516.9879999999999, 14.875, 32.725], [29, 570.034, 720.752, 27.965, 38.675], [29, 47.152, 55.571999999999996, 48.195, 59.5], [29, 202.07999999999998, 269.44, 45.815, 56.525], [29, 353.64, 425.21, 45.815, 56.525], [29, 520.356, 590.242, 44.03, 54.739999999999995], [29, 47.152, 58.94, 65.45, 76.755], [29, 216.394, 273.65, 63.665, 73.78], [29, 353.64, 419.316, 63.665, 73.78], [29, 547.3, 621.396, 55.335, 66.045], [29, 47.152, 112.828, 83.3, 94.60499999999999], [29, 217.236, 274.492, 81.515, 91.63], [29, 357.008, 444.57599999999996, 81.515, 91.63], [29, 47.152, 165.874, 101.14999999999999, 112.455], [29, 197.028, 273.65, 99.365, 110.07499999999999], [29, 357.84999999999997, 407.52799999999996, 99.365, 110.07499999999999], [29, 697.1759999999999, 802.4259999999999, 119.595, 130.9], [29, 41.257999999999996, 424.368, 506.94, 518.245]]
2026-08-10 19:27:20,103 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=17.1s
2026-08-10 19:27:20,104 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:27:20,106 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:27:20,107 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:27:20,107 INFO     29 [qwen-vl-text] positions(19): [[30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:27:20,108 INFO     29 [qwen-vl-text] page grouping: [30], lines per page: [19]
2026-08-10 19:27:20,301 INFO     29 [qwen-vl-text] page=30, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 19:27:20,302 INFO     29 [qwen-vl-text] LLM extraction start, text_len=585
2026-08-10 19:27:20,302 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:20,302 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3348, \"bbox_end\": 3366, \"encounter_dates\": [\"2025-06-20\"], \"department\": \"肺癌门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "放射(1)\n报告时间↓ 项目\n06-20 14:53 双肺CT（平扫）\n报告\n原始报告 原始图像 申请单 对比报告 复制\n开单科室 肺癌 门诊 开单医生\n开单时间 2025-06-20 08:23\n诊断 肺恶性肿瘤个人史\n检查目的 体格检查 精神可，手术\n炎性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。\n报告日期 2025-06-20 14:53 检查科:\n检查项目\n双肺CT（平扫）\n检查描述\n双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。\n检查结论/诊断\n双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。\n右肺术后改变，术区团片影、索条影，较前2025.4.4片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前稍增多、部分范围增大 主动脉及冠脉钙化 右侧胸腔少量积液 甲状腺密度不均，请结合颈部检查\n共1份",
    "role": "user"
  }
]
2026-08-10 19:27:20,304 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:27:20.304+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 90, "failed": 0, "current": {"dbb9d9e294ee11f1bd9827cf206dfa2d": {"id": "dbb9d9e294ee11f1bd9827cf206dfa2d", "doc_id": "db844cb494ee11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 14828427, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388903475, "task_type": "dataflow", "root_trace_id": "9d9ed785184e435b9d8a5693cadbcf94", "root_traceparent": "00-9d9ed785184e435b9d8a5693cadbcf94-7ebd92d2185d496c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:27:29,912 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:29,912 INFO     29 [qwen-vl-text] LLM output (len=555):
{
  "exam_date": "2025-06-20",
  "report_date": "2025-06-20",
  "exam_name": "双肺CT（平扫）",
  "exam_category": "imaging",
  "body_part": "双肺",
  "patient_name": null,
  "patient_gender": null,
  "department": "肺癌门诊",
  "bed_number": null,
  "findings": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。",
  "conclusion": "右肺术后改变，术区团片影、索条影，较前2025.4.4片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前稍增多、部分范围增大 主动脉及冠脉钙化 右侧胸腔少量积液 甲状腺密度不均，请结合颈部检查",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:27:29,913 INFO     29 [qwen-vl-text] coord API call start, page=30, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=859681, prompt_len=1255
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["放射(1)", "报告时间↓ 项目", "06-20 14:53 双肺CT（平扫）", "报告", "原始报告 原始图像 申请单 对比报告 复制", "开单科室 肺癌 门诊 开单医生", "开单时间 2025-06-20 08:23", "诊断 肺恶性肿瘤个人史", "检查目的 体格检查 精神可，手术", "炎性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。", "报告日期 2025-06-20 14:53 检查科:", "检查项目", "双肺CT（平扫）", "检查描述", "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。", "检查结论/诊断", "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。", "右肺术后改变，术区团片影、索条影，较前2025.4.4片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前稍增多、部分范围增大 主动脉及冠脉钙化 右侧胸腔少量积液 甲状腺密度不均，请结合颈部检查", "共1份"]

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
2026-08-10 19:27:41,877 INFO     29 [qwen-vl-text] coord API raw response (len=2201):
[
	{"text": "放射(1)", "bbox": [23, 10, 72, 25]},
	{"text": "报告时间↓ 项目", "bbox": [38, 45, 124, 61], "label": "报告时间↓ 项目"},
	{"text": "06-20 14:53 双肺CT（平扫）", "bbox": [38, 78, 171, 94], "label": "06-20 14:53 双肺CT（平扫）"},
	{"text": "报告", "bbox": [240, 43, 276, 60], "label": "报告"},
	{"text": "原始报告 原始图像 申请单 对比报告 复制", "bbox": [689, 45, 972, 61], "label": "原始报告 原始图像 申请单 对比报告 复制"},
	{"text": "开单科室 肺癌 门诊 开单医生", "bbox": [235, 85, 458, 100], "label": "开单科室 肺癌 门诊 开单医生"},
	{"text": "开单时间 2025-06-20 08:23", "bbox": [608, 85, 729, 98], "label": "开单时间 2025-06-20 08:23"},
	{"text": "诊断 肺恶性肿瘤个人史", "bbox": [235, 107, 358, 122], "label": "诊断 肺恶性肿瘤个人史"},
	{"text": "检查目的 体格检查 精神可，手术", "bbox": [235, 129, 423, 144], "label": "检查目的 体格检查 精神可，手术"},
	{"text": "炎性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。", "bbox": [516, 130, 834, 144], "label": "炎性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。"},
	{"text": "报告日期 2025-06-20 14:53 检查科:", "bbox": [607, 158, 824, 172], "label": "报告日期 2025-06-20 14:53 检查科:"},
	{"text": "检查项目", "bbox": [242, 200, 284, 214], "label": "检查项目"},
	{"text": "双肺CT（平扫）", "bbox": [264, 242, 332, 257], "label": "双肺CT（平扫）"},
	{"text": "检查描述", "bbox": [242, 282, 284, 297], "label": "检查描述"},
	{"text": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。", "bbox": [245, 325, 965, 360], "label": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。"},
	{"text": "检查结论/诊断", "bbox": [242, 386, 308, 400], "label": "检查结论/诊断"},
	{"text": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。", "bbox": [245, 427, 965, 462], "label": "双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。"},
	{"text": "右肺术后改变，术区团片影、索条影，较前2025.4.4片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前稍增多、部分范围增大 主动脉及冠脉钙化 右侧胸腔少量积液 甲状腺密度不均，请结合颈部检查", "bbox": [245, 467, 962, 503], "label": "右肺术后改变，术区团片影、索条影，较前2025.4.4片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前稍增多、部分范围增大 主动脉及冠脉钙化 右侧胸腔少量积液 甲状腺密度不均，请结合颈部检查"},
	{"text": "共1份", "bbox": [30, 893, 65, 908], "label": "共1份"}
]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=12.0s
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[0]: text=放射(1), bbox=[23, 10, 72, 25]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[1]: text=报告时间↓ 项目, bbox=[38, 45, 124, 61]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[2]: text=06-20 14:53 双肺CT（平扫）, bbox=[38, 78, 171, 94]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[3]: text=报告, bbox=[240, 43, 276, 60]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[4]: text=原始报告 原始图像 申请单 对比报告 复制, bbox=[689, 45, 972, 61]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[5]: text=开单科室 肺癌 门诊 开单医生, bbox=[235, 85, 458, 100]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[6]: text=开单时间 2025-06-20 08:23, bbox=[608, 85, 729, 98]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[7]: text=诊断 肺恶性肿瘤个人史, bbox=[235, 107, 358, 122]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[8]: text=检查目的 体格检查 精神可，手术, bbox=[235, 129, 423, 144]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[9]: text=炎性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。, bbox=[516, 130, 834, 144]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[10]: text=报告日期 2025-06-20 14:53 检查科:, bbox=[607, 158, 824, 172]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[11]: text=检查项目, bbox=[242, 200, 284, 214]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[12]: text=双肺CT（平扫）, bbox=[264, 242, 332, 257]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[13]: text=检查描述, bbox=[242, 282, 284, 297]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[14]: text=双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。, bbox=[245, 325, 965, 360]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[15]: text=检查结论/诊断, bbox=[242, 386, 308, 400]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[16]: text=双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。, bbox=[245, 427, 965, 462]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[17]: text=右肺术后改变，术区团片影、索条影，较前2025.4.4片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前稍增多、部分范围增大 主动脉及冠脉钙化 右侧胸腔少量积液 甲状腺密度不均，请结合颈部检查, bbox=[245, 467, 962, 503]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] coord item[18]: text=共1份, bbox=[30, 893, 65, 908]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] page=30 — 19/19 coords, api_time=12.0s
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] new_positions (19):
[[30, 19.366, 60.623999999999995, 5.949999999999999, 14.875], [30, 31.996, 104.408, 26.775, 36.295], [30, 31.996, 143.982, 46.41, 55.93], [30, 202.07999999999998, 232.392, 25.584999999999997, 35.699999999999996], [30, 580.138, 818.424, 26.775, 36.295], [30, 197.87, 385.63599999999997, 50.574999999999996, 59.5], [30, 511.936, 613.818, 50.574999999999996, 58.309999999999995], [30, 197.87, 301.436, 63.665, 72.59], [30, 197.87, 356.166, 76.755, 85.67999999999999], [30, 434.472, 702.228, 77.35, 85.67999999999999], [30, 511.094, 693.808, 94.00999999999999, 102.33999999999999], [30, 203.76399999999998, 239.128, 119.0, 127.33], [30, 222.28799999999998, 279.544, 143.98999999999998, 152.915], [30, 203.76399999999998, 239.128, 167.79, 176.715], [30, 206.29, 812.53, 193.375, 214.2], [30, 203.76399999999998, 259.336, 229.67, 238.0], [30, 206.29, 812.53, 254.065, 274.89], [30, 206.29, 810.004, 277.865, 299.28499999999997], [30, 25.259999999999998, 54.73, 531.3349999999999, 540.26]]
2026-08-10 19:27:41,878 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=21.8s
2026-08-10 19:27:41,879 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:27:41,879 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:27:41,879 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:27:41,879 INFO     29 [qwen-vl-text] positions(20): [[34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:27:41,879 INFO     29 [qwen-vl-text] page grouping: [34], lines per page: [20]
2026-08-10 19:27:42,030 INFO     29 [qwen-vl-text] page=34, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:27:42,032 INFO     29 [qwen-vl-text] LLM extraction start, text_len=163
2026-08-10 19:27:42,032 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:42,032 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3399, \"bbox_end\": 3418, \"encounter_dates\": [\"2024-06-19\"], \"department\": \"胸外科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "临沂市人民医院\n术中冰冻病理报告单\n病理\n姓\n性别：女\n年龄：67岁\n收到日期：2024-06-19 14:28\n送检医院：\n送检科室\n病\n送检医生：5123\n病\n区.\n床号：1-18床\n冰冻诊断：\n(右肺中叶)浸润性腺癌。\n(脏层胸膜结节)查见腺癌。\n(壁层胸膜结节)查见腺癌。\n报告医生：\n2024-06-19 14:54",
    "role": "user"
  }
]
2026-08-10 19:27:44,333 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:44,334 INFO     29 [qwen-vl-table] page=8 LLM output (len=3390):
{
  "report_date": "2026-03-18",
  "items": [
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "10.6",
      "unit": "umol/L",
      "reference_range": "0.0~23.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "1.4",
      "unit": "umol/L",
      "reference_range": "0.0~8.0",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "9.2",
      "unit": "umol/L",
      "reference_range": "0.0~20.0",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "81.8",
      "unit": "g/L",
      "reference_range": "65.0~85.0",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "37.3",
      "unit": "g/L",
      "reference_range": "40.0~55.0",
      "abnormal": true
    },
    {
      "name": "球蛋白",
      "item_code": "GLB",
      "value": "44.5",
      "unit": "g/L",
      "reference_range": "20.0~35.0",
      "abnormal": true
    },
    {
      "name": "白球比例",
      "item_code": "A/G",
      "value": "0.84",
      "unit": null,
      "reference_range": "1.09~2.50",
      "abnormal": true
    },
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": null,
      "value": "39",
      "unit": "IU/L",
      "reference_range": "9~50",
      "abnormal": false
    },
    {
      "name": "天冬氨酸氨基转移酶",
      "item_code": null,
      "value": "27",
      "unit": "IU/L",
      "reference_range": "15~40",
      "abnormal": false
    },
    {
      "name": "AST/ALT",
      "item_code": null,
      "value": "0.69",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "γ-谷氨酰转肽酶",
      "item_code": null,
      "value": "79",
      "unit": "IU/L",
      "reference_range": "10~60",
      "abnormal": true
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "146",
      "unit": "IU/L",
      "reference_range": "45~125",
      "abnormal": true
    },
    {
      "name": "甘油三酯",
      "item_code": "TG",
      "value": "0.98",
      "unit": "mmol/L",
      "reference_range": "0.40~1.86",
      "abnormal": false
    },
    {
      "name": "总胆固醇",
      "item_code": "CHOL",
      "value": "4.73",
      "unit": "mmol/L",
      "reference_range": "3.40~6.10",
      "abnormal": false
    },
    {
      "name": "高密度脂蛋白胆固醇",
      "item_code": null,
      "value": "0.77",
      "unit": "mmol/L",
      "reference_range": "0.90~1.90",
      "abnormal": true
    },
    {
      "name": "非高密度脂蛋白胆固醇",
      "item_code": null,
      "value": "3.96",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "低密度脂蛋白胆固醇",
      "item_code": null,
      "value": "3.37",
      "unit": "mmol/L",
      "reference_range": "1.10~3.50",
      "abnormal": false
    },
    {
      "name": "载脂蛋白A1",
      "item_code": "APOA1",
      "value": "0.76",
      "unit": "g/L",
      "reference_range": "1.00~1.60",
      "abnormal": true
    },
    {
      "name": "载脂蛋白B",
      "item_code": "APOB",
      "value": "1.09",
      "unit": "g/L",
      "reference_range": "0.60~1.10",
      "abnormal": false
    },
    {
      "name": "载脂蛋白A1：B",
      "item_code": null,
      "value": "0.70",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 19:27:44,334 INFO     29 [qwen-vl-table] coord grouping: {8: 20}
2026-08-10 19:27:44,337 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1772162, prompt_len=645
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
总胆红素、直接胆红素、间接胆红素、总蛋白、白蛋白、球蛋白、白球比例、丙氨酸氨基转移酶、天冬氨酸氨基转移酶、AST/ALT、γ-谷氨酰转肽酶、碱性磷酸酶、甘油三酯、总胆固醇、高密度脂蛋白胆固醇、非高密度脂蛋白胆固醇、低密度脂蛋白胆固醇、载脂蛋白A1、载脂蛋白B、载脂蛋白A1：B

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
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord API raw response (len=1031):
```json
[
	{"text": "总胆红素", "bbox": [114, 233, 190, 253]},
	{"text": "直接胆红素", "bbox": [114, 253, 190, 273]},
	{"text": "间接胆红素", "bbox": [114, 275, 190, 295]},
	{"text": "总蛋白", "bbox": [114, 296, 190, 316]},
	{"text": "白蛋白", "bbox": [114, 318, 190, 338]},
	{"text": "球蛋白", "bbox": [114, 340, 190, 360]},
	{"text": "白球比例", "bbox": [114, 361, 190, 381]},
	{"text": "丙氨酸氨基转移酶", "bbox": [114, 383, 245, 403]},
	{"text": "天冬氨酸氨基转移酶", "bbox": [114, 405, 261, 425]},
	{"text": "AST/ALT", "bbox": [97, 427, 165, 447]},
	{"text": "γ-谷氨酰转肽酶", "bbox": [114, 449, 240, 469]},
	{"text": "碱性磷酸酶", "bbox": [114, 471, 190, 491]},
	{"text": "甘油三酯", "bbox": [114, 493, 190, 513]},
	{"text": "总胆固醇", "bbox": [114, 515, 190, 535]},
	{"text": "高密度脂蛋白胆固醇", "bbox": [114, 537, 261, 557]},
	{"text": "非高密度脂蛋白胆固醇", "bbox": [114, 558, 261, 578]},
	{"text": "低密度脂蛋白胆固醇", "bbox": [114, 580, 261, 600]},
	{"text": "载脂蛋白A1", "bbox": [114, 602, 190, 622]},
	{"text": "载脂蛋白B", "bbox": [114, 624, 190, 644]},
	{"text": "载脂蛋白A1：B", "bbox": [97, 646, 211, 666]}
]
```
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord API: raw_items=20, valid_items=20, elapsed=5.9s
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[0]: text=总胆红素, bbox=[114, 233, 190, 253]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[1]: text=直接胆红素, bbox=[114, 253, 190, 273]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[2]: text=间接胆红素, bbox=[114, 275, 190, 295]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[3]: text=总蛋白, bbox=[114, 296, 190, 316]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[4]: text=白蛋白, bbox=[114, 318, 190, 338]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[5]: text=球蛋白, bbox=[114, 340, 190, 360]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[6]: text=白球比例, bbox=[114, 361, 190, 381]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[7]: text=丙氨酸氨基转移酶, bbox=[114, 383, 245, 403]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[8]: text=天冬氨酸氨基转移酶, bbox=[114, 405, 261, 425]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[9]: text=AST/ALT, bbox=[97, 427, 165, 447]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[10]: text=γ-谷氨酰转肽酶, bbox=[114, 449, 240, 469]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[11]: text=碱性磷酸酶, bbox=[114, 471, 190, 491]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[12]: text=甘油三酯, bbox=[114, 493, 190, 513]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[13]: text=总胆固醇, bbox=[114, 515, 190, 535]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[14]: text=高密度脂蛋白胆固醇, bbox=[114, 537, 261, 557]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[15]: text=非高密度脂蛋白胆固醇, bbox=[114, 558, 261, 578]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[16]: text=低密度脂蛋白胆固醇, bbox=[114, 580, 261, 600]
2026-08-10 19:27:50,191 INFO     29 [qwen-vl-table] coord item[17]: text=载脂蛋白A1, bbox=[114, 602, 190, 622]
2026-08-10 19:27:50,192 INFO     29 [qwen-vl-table] coord item[18]: text=载脂蛋白B, bbox=[114, 624, 190, 644]
2026-08-10 19:27:50,192 INFO     29 [qwen-vl-table] coord item[19]: text=载脂蛋白A1：B, bbox=[97, 646, 211, 666]
2026-08-10 19:27:50,192 INFO     29 [qwen-vl-table] page=8 coord: matched 20/20, time=5.9s
2026-08-10 19:27:50,192 INFO     29 [qwen-vl-table] new_positions (20):
[[9, 95.988, 159.98, 138.635, 150.535], [9, 95.988, 159.98, 150.535, 162.435], [9, 95.988, 159.98, 163.625, 175.525], [9, 95.988, 159.98, 176.12, 188.01999999999998], [9, 95.988, 159.98, 189.20999999999998, 201.10999999999999], [9, 95.988, 159.98, 202.29999999999998, 214.2], [9, 95.988, 159.98, 214.795, 226.695], [9, 95.988, 206.29, 227.885, 239.785], [9, 95.988, 219.762, 240.975, 252.875], [9, 81.67399999999999, 138.93, 254.065, 265.965], [9, 95.988, 202.07999999999998, 267.155, 279.055], [9, 95.988, 159.98, 280.245, 292.145], [9, 95.988, 159.98, 293.335, 305.235], [9, 95.988, 159.98, 306.425, 318.325], [9, 95.988, 219.762, 319.515, 331.41499999999996], [9, 95.988, 219.762, 332.01, 343.90999999999997], [9, 95.988, 219.762, 345.09999999999997, 357.0], [9, 95.988, 159.98, 358.19, 370.09], [9, 95.988, 159.98, 371.28, 383.18], [9, 81.67399999999999, 177.662, 384.37, 396.27]]
2026-08-10 19:27:50,192 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=20, matched=20, pages=1, time=43.7s
2026-08-10 19:27:50,193 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:27:50,195 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:27:50,195 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8]
2026-08-10 19:27:50,195 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:27:50,447 INFO     29 [qwen-vl-table] page=8, rect=842x595, img=(2339x1653)
2026-08-10 19:27:50,448 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:50,449 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 354, \"bbox_end\": 378, \"encounter_dates\": [\"2026-03-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-03-18\n\\hline\n\\multicolumn{2}{c}{检验项目} & 结果 & 参考区间 & 单位 & \\\\\n\\hline\n21 & ★尿素[UREA] & 4.1 & 3.1~7.4 & mmol/L & \\\\\n22 & ★肌酐[CREA] & 68 & 57~97 & umol/L & \\\\\n23 & UREA/CREA & 0.06 & & & \\\\\n24 & ★尿酸[URIC] & 183 & 130~430 & umol/L & \\\\\n25 & ★葡萄糖[GLU] & 5.21 & 3.90~6.10 & mmol/L & \\\\\n26 & ★乳酸脱氢酶[LDH] & 162 & 120~250 & IU/L & \\\\\n27 & ★肌酸激酶[CK] & 36 & 22~270 & IU/L & \\\\\n28 & 肌酸激酶MB亚型 & 17.0 & 2.0~25.0 & IU/L & \\\\\n29 & CKMB/CK & 0.47 & & & \\\\\n30 & ★钾[K] & 4.50 & 3.50~5.50 & mmol/L & \\\\\n31 & ★钠[NA] & 138.4 & 135.0~148.0 & mmol/L & \\\\\n32 & ★氯[CL] & 96.3 & 96.0~112.0 & mmol/L & \\\\\n33 & ★钙[CA] & 2.35 & 2.10~2.70 & mmol/L & \\\\\n34 & 碳酸氢盐[HC03] & 27.3 & 20.1~29.0 & mmol/L & \\\\\n35 & ★镁[MG] & 0.99 & 0.70~1.10 & mmol/L & \\\\\n36 & ★无机磷酸盐[P] & 1.27 & 0.83~1.48 & mmol/L & \\\\\n37 & 阴离子间隙[AG] & 19 & & & \\\\\n38 & 渗透压[OSM] & 286 & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:27:50,456 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:50,456 INFO     29 [qwen-vl-text] LLM output (len=376):
{
  "exam_date": "2024-06-19",
  "report_date": "2024-06-19",
  "exam_name": "术中冰冻病理",
  "exam_category": "pathology",
  "body_part": "右肺中叶、脏层胸膜结节、壁层胸膜结节",
  "patient_name": null,
  "patient_gender": "女",
  "department": "胸外科",
  "bed_number": "1-18床",
  "findings": null,
  "conclusion": "(右肺中叶)浸润性腺癌。\n(脏层胸膜结节)查见腺癌。\n(壁层胸膜结节)查见腺癌。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:27:50,457 INFO     29 [qwen-vl-text] coord API call start, page=34, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=610388, prompt_len=836
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["临沂市人民医院", "术中冰冻病理报告单", "病理", "姓", "性别：女", "年龄：67岁", "收到日期：2024-06-19 14:28", "送检医院：", "送检科室", "病", "送检医生：5123", "病", "区.", "床号：1-18床", "冰冻诊断：", "(右肺中叶)浸润性腺癌。", "(脏层胸膜结节)查见腺癌。", "(壁层胸膜结节)查见腺癌。", "报告医生：", "2024-06-19 14:54"]

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
2026-08-10 19:27:57,472 INFO     29 [qwen-vl-text] coord API raw response (len=1040):
[
	{"text": "临沂市人民医院", "bbox": [373, 106, 625, 134]},
	{"text": "术中冰冻病理报告单", "bbox": [280, 144, 714, 181]},
	{"text": "病理", "bbox": [664, 192, 747, 211]},
	{"text": "姓", "bbox": [56, 232, 84, 251]},
	{"text": "性别：女", "bbox": [319, 232, 417, 251]},
	{"text": "年龄：67岁", "bbox": [464, 232, 580, 251]},
	{"text": "收到日期：2024-06-19 14:28", "bbox": [613, 232, 932, 251]},
	{"text": "送检医院：", "bbox": [56, 265, 163, 284]},
	{"text": "送检科室", "bbox": [319, 265, 417, 284]},
	{"text": "病", "bbox": [612, 265, 638, 284]},
	{"text": "送检医生：5123", "bbox": [56, 300, 225, 319]},
	{"text": "病", "bbox": [319, 300, 345, 319]},
	{"text": "区.", "bbox": [392, 300, 448, 319]},
	{"text": "床号：1-18床", "bbox": [612, 300, 758, 319]},
	{"text": "冰冻诊断：", "bbox": [56, 353, 163, 372]},
	{"text": "(右肺中叶)浸润性腺癌。", "bbox": [119, 374, 368, 393]},
	{"text": "(脏层胸膜结节)查见腺癌。", "bbox": [127, 394, 417, 413]},
	{"text": "(壁层胸膜结节)查见腺癌。", "bbox": [127, 413, 417, 432]},
	{"text": "报告医生：", "bbox": [56, 884, 163, 904]},
	{"text": "2024-06-19 14:54", "bbox": [723, 887, 917, 903]}
]
2026-08-10 19:27:57,473 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=7.0s
2026-08-10 19:27:57,473 INFO     29 [qwen-vl-text] coord item[0]: text=临沂市人民医院, bbox=[373, 106, 625, 134]
2026-08-10 19:27:57,473 INFO     29 [qwen-vl-text] coord item[1]: text=术中冰冻病理报告单, bbox=[280, 144, 714, 181]
2026-08-10 19:27:57,473 INFO     29 [qwen-vl-text] coord item[2]: text=病理, bbox=[664, 192, 747, 211]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[3]: text=姓, bbox=[56, 232, 84, 251]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[319, 232, 417, 251]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：67岁, bbox=[464, 232, 580, 251]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[6]: text=收到日期：2024-06-19 14:28, bbox=[613, 232, 932, 251]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[7]: text=送检医院：, bbox=[56, 265, 163, 284]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[8]: text=送检科室, bbox=[319, 265, 417, 284]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[9]: text=病, bbox=[612, 265, 638, 284]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[10]: text=送检医生：5123, bbox=[56, 300, 225, 319]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[11]: text=病, bbox=[319, 300, 345, 319]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[12]: text=区., bbox=[392, 300, 448, 319]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[13]: text=床号：1-18床, bbox=[612, 300, 758, 319]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[14]: text=冰冻诊断：, bbox=[56, 353, 163, 372]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[15]: text=(右肺中叶)浸润性腺癌。, bbox=[119, 374, 368, 393]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[16]: text=(脏层胸膜结节)查见腺癌。, bbox=[127, 394, 417, 413]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[17]: text=(壁层胸膜结节)查见腺癌。, bbox=[127, 413, 417, 432]
2026-08-10 19:27:57,474 INFO     29 [qwen-vl-text] coord item[18]: text=报告医生：, bbox=[56, 884, 163, 904]
2026-08-10 19:27:57,475 INFO     29 [qwen-vl-text] coord item[19]: text=2024-06-19 14:54, bbox=[723, 887, 917, 903]
2026-08-10 19:27:57,475 INFO     29 [qwen-vl-text] page=34 — 20/20 coords, api_time=7.0s
2026-08-10 19:27:57,475 INFO     29 [qwen-vl-text] new_positions (20):
[[34, 221.935, 371.875, 89.252, 112.828], [34, 166.6, 424.83, 121.24799999999999, 152.402], [34, 395.08, 444.465, 161.664, 177.662], [34, 33.32, 49.98, 195.344, 211.34199999999998], [34, 189.80499999999998, 248.11499999999998, 195.344, 211.34199999999998], [34, 276.08, 345.09999999999997, 195.344, 211.34199999999998], [34, 364.73499999999996, 554.54, 195.344, 211.34199999999998], [34, 33.32, 96.985, 223.13, 239.128], [34, 189.80499999999998, 248.11499999999998, 223.13, 239.128], [34, 364.14, 379.60999999999996, 223.13, 239.128], [34, 33.32, 133.875, 252.6, 268.598], [34, 189.80499999999998, 205.27499999999998, 252.6, 268.598], [34, 233.23999999999998, 266.56, 252.6, 268.598], [34, 364.14, 451.01, 252.6, 268.598], [34, 33.32, 96.985, 297.226, 313.224], [34, 70.80499999999999, 218.95999999999998, 314.908, 330.906], [34, 75.565, 248.11499999999998, 331.748, 347.746], [34, 75.565, 248.11499999999998, 347.746, 363.74399999999997], [34, 33.32, 96.985, 744.328, 761.168], [34, 430.185, 545.615, 746.8539999999999, 760.326]]
2026-08-10 19:27:57,475 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=1, time=15.6s
2026-08-10 19:27:57,475 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:27:57,477 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:27:57,478 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:27:57,478 INFO     29 [qwen-vl-text] positions(28): [[35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:27:57,478 INFO     29 [qwen-vl-text] page grouping: [35, 36], lines per page: [26, 2]
2026-08-10 19:27:59,059 INFO     29 [qwen-vl-text] page=35, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:27:59,109 INFO     29 [qwen-vl-text] page=36, rect=592x842, img=(1646x2339), dpi=200
2026-08-10 19:27:59,111 INFO     29 [qwen-vl-text] LLM extraction start, text_len=434
2026-08-10 19:27:59,111 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:27:59,112 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 3421, \"bbox_end\": 3448, \"encounter_dates\": [\"2026-03-12\"], \"department\": \"临床试验病房\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "影像学报告\n检查号\n姓名\n性别：女\n年龄：69岁\n科\n临床试验病房\n病房：702643\n病床：702643\n住院号：7122764316\n检查时间：2026-03-10 09:26 报告时间：2026-03-12 08:1\n检查部位：[胸部,增强]\n影像描述：\n原诊“肺癌靶向治疗后进展”复查：\n右肺局部术后，右肺下叶见条片状软组织影，局部结节影，强化欠均（\n图7-37）。左肺上叶见条片影。纵隔见肿大淋巴结，图7-24示大者短径\n约12mm。右侧叶间胸膜增厚，右侧胸膜多发结节样增厚，强化，右侧胸腔少\n量积液。甲状腺局部示低密度影，强化不均匀。扫及左肾上腺略增粗。\n影像诊断：\n1、肺癌靶向治疗后进展复查，右肺下叶局部强化欠均，随诊或结合基线\n片。\n2、左肺上叶局部不张。\n3、纵隔淋巴结肿大。\n4、右侧胸膜增厚，考虑转移所致。右侧胸腔少量积液。\n5、甲状腺结节，结合超声。\n6、左肾上腺略增粗，建议随诊。\n20240619手术\n202407奥西，202602停的药",
    "role": "user"
  }
]
2026-08-10 19:27:59,352 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:27:59.351+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 90, "failed": 0, "current": {"dbb9d9e294ee11f1bd9827cf206dfa2d": {"id": "dbb9d9e294ee11f1bd9827cf206dfa2d", "doc_id": "db844cb494ee11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 14828427, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388903475, "task_type": "dataflow", "root_trace_id": "9d9ed785184e435b9d8a5693cadbcf94", "root_traceparent": "00-9d9ed785184e435b9d8a5693cadbcf94-7ebd92d2185d496c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:28:07,659 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:28:07,659 INFO     29 [qwen-vl-text] LLM output (len=586):
{
  "exam_date": "2026-03-10",
  "report_date": "2026-03-12",
  "exam_name": "胸部增强CT",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "临床试验病房",
  "bed_number": "702643",
  "findings": "原诊“肺癌靶向治疗后进展”复查：\n右肺局部术后，右肺下叶见条片状软组织影，局部结节影，强化欠均（图7-37）。左肺上叶见条片影。纵隔见肿大淋巴结，图7-24示大者短径约12mm。右侧叶间胸膜增厚，右侧胸膜多发结节样增厚，强化，右侧胸腔少量积液。甲状腺局部示低密度影，强化不均匀。扫及左肾上腺略增粗。",
  "conclusion": "1、肺癌靶向治疗后进展复查，右肺下叶局部强化欠均，随诊或结合基线片。\n2、左肺上叶局部不张。\n3、纵隔淋巴结肿大。\n4、右侧胸膜增厚，考虑转移所致。右侧胸腔少量积液。\n5、甲状腺结节，结合超声。\n6、左肾上腺略增粗，建议随诊。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:28:07,662 INFO     29 [qwen-vl-text] coord API call start, page=35, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=821319, prompt_len=1095
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["影像学报告", "检查号", "姓名", "性别：女", "年龄：69岁", "科", "临床试验病房", "病房：702643", "病床：702643", "住院号：7122764316", "检查时间：2026-03-10 09:26 报告时间：2026-03-12 08:1", "检查部位：[胸部,增强]", "影像描述：", "原诊“肺癌靶向治疗后进展”复查：", "右肺局部术后，右肺下叶见条片状软组织影，局部结节影，强化欠均（", "图7-37）。左肺上叶见条片影。纵隔见肿大淋巴结，图7-24示大者短径", "约12mm。右侧叶间胸膜增厚，右侧胸膜多发结节样增厚，强化，右侧胸腔少", "量积液。甲状腺局部示低密度影，强化不均匀。扫及左肾上腺略增粗。", "影像诊断：", "1、肺癌靶向治疗后进展复查，右肺下叶局部强化欠均，随诊或结合基线", "片。", "2、左肺上叶局部不张。", "3、纵隔淋巴结肿大。", "4、右侧胸膜增厚，考虑转移所致。右侧胸腔少量积液。", "5、甲状腺结节，结合超声。", "6、左肾上腺略增粗，建议随诊。"]

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
2026-08-10 19:28:16,191 INFO     29 [qwen-vl-text] coord API raw response (len=1535):
[
	{"text": "影像学报告", "bbox": [375, 137, 621, 163]},
	{"text": "检查号", "bbox": [661, 171, 733, 189]},
	{"text": "姓名", "bbox": [66, 197, 113, 215]},
	{"text": "性别：女", "bbox": [380, 196, 498, 214]},
	{"text": "年龄：69岁", "bbox": [682, 197, 821, 215]},
	{"text": "科", "bbox": [67, 218, 106, 236]},
	{"text": "临床试验病房", "bbox": [158, 220, 290, 235]},
	{"text": "病房：702643", "bbox": [379, 218, 526, 236]},
	{"text": "病床：702643", "bbox": [681, 219, 837, 237]},
	{"text": "住院号：7122764316", "bbox": [67, 240, 289, 258]},
	{"text": "检查时间：2026-03-10 09:26 报告时间：2026-03-12 08:1", "bbox": [315, 240, 929, 258]},
	{"text": "检查部位：[胸部,增强]", "bbox": [61, 268, 327, 287]},
	{"text": "影像描述：", "bbox": [63, 289, 172, 307]},
	{"text": "原诊“肺癌靶向治疗后进展”复查：", "bbox": [120, 310, 507, 329]},
	{"text": "右肺局部术后，右肺下叶见条片状软组织影，局部结节影，强化欠均（", "bbox": [120, 328, 902, 347]},
	{"text": "图7-37）。左肺上叶见条片影。纵隔见肿大淋巴结，图7-24示大者短径", "bbox": [70, 347, 852, 366]},
	{"text": "约12mm。右侧叶间胸膜增厚，右侧胸膜多发结节样增厚，强化，右侧胸腔少", "bbox": [69, 365, 902, 384]},
	{"text": "量积液。甲状腺局部示低密度影，强化不均匀。扫及左肾上腺略增粗。", "bbox": [70, 383, 838, 402]},
	{"text": "影像诊断：", "bbox": [63, 701, 172, 719]},
	{"text": "1、肺癌靶向治疗后进展复查，右肺下叶局部强化欠均，随诊或结合基线", "bbox": [68, 724, 863, 742]},
	{"text": "片。", "bbox": [68, 742, 105, 760]},
	{"text": "2、左肺上叶局部不张。", "bbox": [67, 760, 318, 779]},
	{"text": "3、纵隔淋巴结肿大。", "bbox": [67, 779, 293, 797]},
	{"text": "4、右侧胸膜增厚，考虑转移所致。右侧胸腔少量积液。", "bbox": [67, 797, 672, 816]},
	{"text": "5、甲状腺结节，结合超声。", "bbox": [67, 816, 370, 834]},
	{"text": "6、左肾上腺略增粗，建议随诊。", "bbox": [67, 834, 420, 852]}
]
2026-08-10 19:28:16,191 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=8.5s
2026-08-10 19:28:16,191 INFO     29 [qwen-vl-text] coord item[0]: text=影像学报告, bbox=[375, 137, 621, 163]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[1]: text=检查号, bbox=[661, 171, 733, 189]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[66, 197, 113, 215]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[380, 196, 498, 214]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：69岁, bbox=[682, 197, 821, 215]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[5]: text=科, bbox=[67, 218, 106, 236]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[6]: text=临床试验病房, bbox=[158, 220, 290, 235]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[7]: text=病房：702643, bbox=[379, 218, 526, 236]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[8]: text=病床：702643, bbox=[681, 219, 837, 237]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[9]: text=住院号：7122764316, bbox=[67, 240, 289, 258]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[10]: text=检查时间：2026-03-10 09:26 报告时间：2026-03-12 08:1, bbox=[315, 240, 929, 258]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位：[胸部,增强], bbox=[61, 268, 327, 287]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[12]: text=影像描述：, bbox=[63, 289, 172, 307]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[13]: text=原诊“肺癌靶向治疗后进展”复查：, bbox=[120, 310, 507, 329]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[14]: text=右肺局部术后，右肺下叶见条片状软组织影，局部结节影，强化欠均（, bbox=[120, 328, 902, 347]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[15]: text=图7-37）。左肺上叶见条片影。纵隔见肿大淋巴结，图7-24示大者短径, bbox=[70, 347, 852, 366]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[16]: text=约12mm。右侧叶间胸膜增厚，右侧胸膜多发结节样增厚，强化，右侧胸腔少, bbox=[69, 365, 902, 384]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[17]: text=量积液。甲状腺局部示低密度影，强化不均匀。扫及左肾上腺略增粗。, bbox=[70, 383, 838, 402]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[18]: text=影像诊断：, bbox=[63, 701, 172, 719]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[19]: text=1、肺癌靶向治疗后进展复查，右肺下叶局部强化欠均，随诊或结合基线, bbox=[68, 724, 863, 742]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[20]: text=片。, bbox=[68, 742, 105, 760]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[21]: text=2、左肺上叶局部不张。, bbox=[67, 760, 318, 779]
2026-08-10 19:28:16,192 INFO     29 [qwen-vl-text] coord item[22]: text=3、纵隔淋巴结肿大。, bbox=[67, 779, 293, 797]
2026-08-10 19:28:16,193 INFO     29 [qwen-vl-text] coord item[23]: text=4、右侧胸膜增厚，考虑转移所致。右侧胸腔少量积液。, bbox=[67, 797, 672, 816]
2026-08-10 19:28:16,193 INFO     29 [qwen-vl-text] coord item[24]: text=5、甲状腺结节，结合超声。, bbox=[67, 816, 370, 834]
2026-08-10 19:28:16,193 INFO     29 [qwen-vl-text] coord item[25]: text=6、左肾上腺略增粗，建议随诊。, bbox=[67, 834, 420, 852]
2026-08-10 19:28:16,193 INFO     29 [qwen-vl-text] page=35 — 26/26 coords, api_time=8.5s
2026-08-10 19:28:16,193 INFO     29 [qwen-vl-text] coord API call start, page=36, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=35647, prompt_len=647
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["20240619手术", "202407奥西，202602停的药"]

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
2026-08-10 19:28:17,880 INFO     29 [qwen-vl-text] coord API raw response (len=120):
[
	{"text": "20240619手术", "bbox": [250, 460, 472, 485]},
	{"text": "202407奥西，202602停的药", "bbox": [250, 485, 695, 511]}
]
2026-08-10 19:28:17,880 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=1.7s
2026-08-10 19:28:17,880 INFO     29 [qwen-vl-text] coord item[0]: text=20240619手术, bbox=[250, 460, 472, 485]
2026-08-10 19:28:17,880 INFO     29 [qwen-vl-text] coord item[1]: text=202407奥西，202602停的药, bbox=[250, 485, 695, 511]
2026-08-10 19:28:17,881 INFO     29 [qwen-vl-text] page=36 — 2/2 coords, api_time=1.7s
2026-08-10 19:28:17,881 INFO     29 [qwen-vl-text] new_positions (28):
[[35, 223.125, 369.495, 115.354, 137.246], [35, 393.29499999999996, 436.135, 143.982, 159.138], [35, 39.269999999999996, 67.235, 165.874, 181.03], [35, 226.1, 296.31, 165.03199999999998, 180.188], [35, 405.78999999999996, 488.495, 165.874, 181.03], [35, 39.864999999999995, 63.07, 183.55599999999998, 198.712], [35, 94.00999999999999, 172.54999999999998, 185.23999999999998, 197.87], [35, 225.505, 312.96999999999997, 183.55599999999998, 198.712], [35, 405.195, 498.015, 184.398, 199.554], [35, 39.864999999999995, 171.95499999999998, 202.07999999999998, 217.236], [35, 187.42499999999998, 552.755, 202.07999999999998, 217.236], [35, 36.295, 194.565, 225.656, 241.654], [35, 37.485, 102.33999999999999, 243.338, 258.49399999999997], [35, 71.39999999999999, 301.66499999999996, 261.02, 277.018], [35, 71.39999999999999, 536.6899999999999, 276.176, 292.174], [35, 41.65, 506.94, 292.174, 308.17199999999997], [35, 41.055, 536.6899999999999, 307.33, 323.328], [35, 41.65, 498.60999999999996, 322.486, 338.484], [35, 37.485, 102.33999999999999, 590.242, 605.398], [35, 40.46, 513.485, 609.608, 624.764], [35, 40.46, 62.474999999999994, 624.764, 639.92], [35, 39.864999999999995, 189.20999999999998, 639.92, 655.918], [35, 39.864999999999995, 174.33499999999998, 655.918, 671.074], [35, 39.864999999999995, 399.84, 671.074, 687.072], [35, 39.864999999999995, 220.14999999999998, 687.072, 702.228], [35, 39.864999999999995, 249.89999999999998, 702.228, 717.384], [36, 148.11024475097656, 279.63214208984374, 387.26940673828125, 408.3166571044922], [36, 148.11024475097656, 411.74648040771484, 408.3166571044922, 430.2057974853516]]
2026-08-10 19:28:17,881 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=2, time=20.4s
2026-08-10 19:28:17,898 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 19:28:17,899 INFO     29 [Trace] task=dbb9d9e2 | doc=12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf | Extractor:ExaminationReport | outputs={"chunks": "16 items, types={'ExaminationReport': 16}", "html": "", "json": "3449 items", "markdown": "", "text": "", "name": "12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "16 items, types={'ExaminationReport': 16}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Progress": "1 items, types={'ProgressNote': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Clinical": "9 items, types={'OutpatientRecord': 9}", "route_summary": "{\"chunks_Examination\": 16, \"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Progress\": 1, \"chunks_LabExam\": 5, \"chunks_Clinical\": 9}"}
2026-08-10 19:28:17,899 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 19:28:17,904 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:28:17,906 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:28:17,906 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 19:28:17,906 INFO     29 [qwen-vl-text] positions(32): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:28:17,906 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [32]
2026-08-10 19:28:18,151 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:28:18,152 INFO     29 [qwen-vl-text] LLM extraction start, text_len=758
2026-08-10 19:28:18,152 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:28:18,152 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 465, \"bbox_end\": 496, \"encounter_dates\": [\"2024-06-19\"], \"department\": \"胸外科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "手术记录\n年龄：67岁\n病\n手术日期：2024-06-19\n手术时间：12:50~14:35\n才\n1.肺占位性病变2.腰椎间盘突出\n术中诊断：\n1.右肺中叶癌2.胸膜继发恶性肿瘤3.腰椎间盘突出\n手术名称：胸腔镜右肺中叶切除+脏层胸膜结节切除+壁层胸膜结节切除+淋巴结切除术\n麻醉方法：\n全身麻醉\n手术指导者：\n手术经过、术中发现的情况及处理：\n患者入室后，核查患者姓名、疾病名称、住院号、胸部CT姓名全部一致，患者平卧位行气管插管、全\n身麻醉后，取左侧卧位，左侧胸壁下垫海绵垫，固定患者，调整手术床呈折刀位。标记手术切口。常规碘伏\n消毒3遍，铺无菌巾，于右侧腋中线第5肋间切开皮肤约2.5cm，探查见右肺肺组织与胸壁无明显粘连，肿块\n位于右肺中叶，大小约3*3cm，脏层胸膜皱缩，脏层胸膜及壁层胸膜可见多发黄白色粟粒状结节，未见明显\n胸腔积液；用电钩游离出中叶动、静脉，用直线切割缝合器切断，清扫中叶支气管周围淋巴结后，夹闭支气\n管，麻醉师吸痰胀肺，确认为右肺中叶支气管后将中叶支气管用直线切割缝合器切断，继续将右肺水平裂用\n直线切割缝合器切断，将右肺中叶放入8号手套中，自胸腔内取出，于前纵隔壁层胸膜切除部分壁层胸膜结\n节，使用一次性直线切割缝合器于下叶背段切除部分脏层胸膜结节，送快速病理，半小时后病理示：右肺中\n叶浸润腺癌，脏层、壁层胸膜结节查见腺癌；遂用电刀行纵隔淋巴结采样，并充分止血，冲洗胸腔，麻醉师\n吸痰胀肺，检查无漏血漏气后，于右侧胸壁切口处置入26号胸腔闭式引流管，接水封瓶，用可吸收线缝合腋\n前线切口。手术程顺利，术中出血约20ml，未输血。病人清醒后拔除气管插管，安返病\n10\n58\n26.0\n188.8.155\n激活Winc\n转到\"设置\"以\n记录时间：2024-06-19 14:44:23",
    "role": "user"
  }
]
2026-08-10 19:28:26,095 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:28:26,095 INFO     29 [qwen-vl-table] page=8 LLM output (len=3023):
{
  "report_date": "2026-03-18",
  "items": [
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "4.1",
      "unit": "mmol/L",
      "reference_range": "3.1~7.4",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": "CREA",
      "value": "68",
      "unit": "umol/L",
      "reference_range": "57~97",
      "abnormal": false
    },
    {
      "name": "UREA/CREA",
      "item_code": null,
      "value": "0.06",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "URIC",
      "value": "183",
      "unit": "umol/L",
      "reference_range": "130~430",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "5.21",
      "unit": "mmol/L",
      "reference_range": "3.90~6.10",
      "abnormal": false
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": "LDH",
      "value": "162",
      "unit": "IU/L",
      "reference_range": "120~250",
      "abnormal": false
    },
    {
      "name": "肌酸激酶",
      "item_code": "CK",
      "value": "36",
      "unit": "IU/L",
      "reference_range": "22~270",
      "abnormal": false
    },
    {
      "name": "肌酸激酶MB亚型",
      "item_code": null,
      "value": "17.0",
      "unit": "IU/L",
      "reference_range": "2.0~25.0",
      "abnormal": false
    },
    {
      "name": "CKMB/CK",
      "item_code": null,
      "value": "0.47",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "4.50",
      "unit": "mmol/L",
      "reference_range": "3.50~5.50",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "NA",
      "value": "138.4",
      "unit": "mmol/L",
      "reference_range": "135.0~148.0",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "CL",
      "value": "96.3",
      "unit": "mmol/L",
      "reference_range": "96.0~112.0",
      "abnormal": false
    },
    {
      "name": "钙",
      "item_code": "CA",
      "value": "2.35",
      "unit": "mmol/L",
      "reference_range": "2.10~2.70",
      "abnormal": false
    },
    {
      "name": "碳酸氢盐",
      "item_code": "HC03",
      "value": "27.3",
      "unit": "mmol/L",
      "reference_range": "20.1~29.0",
      "abnormal": false
    },
    {
      "name": "镁",
      "item_code": "MG",
      "value": "0.99",
      "unit": "mmol/L",
      "reference_range": "0.70~1.10",
      "abnormal": false
    },
    {
      "name": "无机磷酸盐",
      "item_code": "P",
      "value": "1.27",
      "unit": "mmol/L",
      "reference_range": "0.83~1.48",
      "abnormal": false
    },
    {
      "name": "阴离子间隙",
      "item_code": "AG",
      "value": "19",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "渗透压",
      "item_code": "OSM",
      "value": "286",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 19:28:26,095 INFO     29 [qwen-vl-table] coord grouping: {8: 18}
2026-08-10 19:28:26,098 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1772162, prompt_len=588
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
尿素、肌酐、UREA/CREA、尿酸、葡萄糖、乳酸脱氢酶、肌酸激酶、肌酸激酶MB亚型、CKMB/CK、钾、钠、氯、钙、碳酸氢盐、镁、无机磷酸盐、阴离子间隙、渗透压

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
2026-08-10 19:28:32,841 INFO     29 [qwen-vl-table] coord API raw response (len=888):
```json
[
	{"text": "尿素", "bbox": [500, 233, 600, 253]},
	{"text": "肌酐", "bbox": [500, 253, 600, 273]},
	{"text": "UREA/CREA", "bbox": [500, 276, 581, 296]},
	{"text": "尿酸", "bbox": [500, 297, 600, 317]},
	{"text": "葡萄糖", "bbox": [500, 319, 608, 339]},
	{"text": "乳酸脱氢酶", "bbox": [500, 341, 638, 361]},
	{"text": "肌酸激酶", "bbox": [500, 363, 615, 383]},
	{"text": "肌酸激酶MB亚型", "bbox": [500, 385, 617, 405]},
	{"text": "CKMB/CK", "bbox": [500, 407, 567, 427]},
	{"text": "钾", "bbox": [500, 429, 564, 449]},
	{"text": "钠", "bbox": [500, 451, 570, 471]},
	{"text": "氯", "bbox": [500, 473, 570, 493]},
	{"text": "钙", "bbox": [500, 495, 570, 515]},
	{"text": "碳酸氢盐", "bbox": [500, 517, 615, 537]},
	{"text": "镁", "bbox": [500, 539, 570, 559]},
	{"text": "无机磷酸盐", "bbox": [500, 560, 622, 580]},
	{"text": "阴离子间隙", "bbox": [500, 582, 615, 602]},
	{"text": "渗透压", "bbox": [500, 604, 593, 624]}
]
```
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord API: raw_items=18, valid_items=18, elapsed=6.7s
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[0]: text=尿素, bbox=[500, 233, 600, 253]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[1]: text=肌酐, bbox=[500, 253, 600, 273]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[2]: text=UREA/CREA, bbox=[500, 276, 581, 296]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[3]: text=尿酸, bbox=[500, 297, 600, 317]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[4]: text=葡萄糖, bbox=[500, 319, 608, 339]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[5]: text=乳酸脱氢酶, bbox=[500, 341, 638, 361]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[6]: text=肌酸激酶, bbox=[500, 363, 615, 383]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[7]: text=肌酸激酶MB亚型, bbox=[500, 385, 617, 405]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[8]: text=CKMB/CK, bbox=[500, 407, 567, 427]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[9]: text=钾, bbox=[500, 429, 564, 449]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[10]: text=钠, bbox=[500, 451, 570, 471]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[11]: text=氯, bbox=[500, 473, 570, 493]
2026-08-10 19:28:32,842 INFO     29 [qwen-vl-table] coord item[12]: text=钙, bbox=[500, 495, 570, 515]
2026-08-10 19:28:32,843 INFO     29 [qwen-vl-table] coord item[13]: text=碳酸氢盐, bbox=[500, 517, 615, 537]
2026-08-10 19:28:32,843 INFO     29 [qwen-vl-table] coord item[14]: text=镁, bbox=[500, 539, 570, 559]
2026-08-10 19:28:32,843 INFO     29 [qwen-vl-table] coord item[15]: text=无机磷酸盐, bbox=[500, 560, 622, 580]
2026-08-10 19:28:32,843 INFO     29 [qwen-vl-table] coord item[16]: text=阴离子间隙, bbox=[500, 582, 615, 602]
2026-08-10 19:28:32,843 INFO     29 [qwen-vl-table] coord item[17]: text=渗透压, bbox=[500, 604, 593, 624]
2026-08-10 19:28:32,844 INFO     29 [qwen-vl-table] page=8 coord: matched 18/18, time=6.7s
2026-08-10 19:28:32,845 INFO     29 [qwen-vl-table] new_positions (18):
[[9, 421.0, 505.2, 138.635, 150.535], [9, 421.0, 505.2, 150.535, 162.435], [9, 421.0, 489.202, 164.22, 176.12], [9, 421.0, 505.2, 176.715, 188.61499999999998], [9, 421.0, 511.936, 189.80499999999998, 201.70499999999998], [9, 421.0, 537.196, 202.89499999999998, 214.795], [9, 421.0, 517.8299999999999, 215.98499999999999, 227.885], [9, 421.0, 519.514, 229.075, 240.975], [9, 421.0, 477.414, 242.165, 254.065], [9, 421.0, 474.888, 255.255, 267.155], [9, 421.0, 479.94, 268.34499999999997, 280.245], [9, 421.0, 479.94, 281.435, 293.335], [9, 421.0, 479.94, 294.525, 306.425], [9, 421.0, 517.8299999999999, 307.615, 319.515], [9, 421.0, 479.94, 320.705, 332.60499999999996], [9, 421.0, 523.7239999999999, 333.2, 345.09999999999997], [9, 421.0, 517.8299999999999, 346.28999999999996, 358.19], [9, 421.0, 499.306, 359.38, 371.28]]
2026-08-10 19:28:32,845 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=18, matched=18, pages=1, time=42.7s
2026-08-10 19:28:32,848 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:28:32,850 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:28:32,850 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-10 19:28:32,850 INFO     29 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:28:33,107 INFO     29 [qwen-vl-table] page=9, rect=842x595, img=(2339x1653)
2026-08-10 19:28:33,107 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:28:33,108 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 379, \"bbox_end\": 402, \"encounter_dates\": [\"2026-03-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-03-18\n\\hline\n\\textbf{检验项目} & \\textbf{结果} & \\textbf{参考区间} & \\textbf{单位} & \\textbf{检验项目} & \\textbf{结果} & \\textbf{参考区间} & \\textbf{单位} \\\\\n\\hline\n1 ★白细胞计数 & 6.58 & 4.00~10.00 & 10^9/L & 18红细胞体积分布宽度-CV & 13.4 & 11.0~16.0 & \\% \\\\\n2 中性粒细胞\\% & 63.90 & 50.00~70.00 & \\% & 19红细胞体积分布宽度-SD & 43.7 & 37.0~54.0 & f1 \\\\\n3 淋巴细胞\\% & 25.60 & 20.00~40.00 & \\% & 20有核红细胞绝对计数 & 0.00 & 0.00~0.02 & 10^9/L \\\\\n4 单核细胞\\% & 9.70 $\\uparrow$ & 3.00~8.00 & \\% & 21有核红细胞/白细胞 & 0.00 & $<$1.00 & \\% \\\\\n5 嗜酸性粒细胞\\% & 0.50 & 0.00~5.00 & \\% & 22★血小板计数 & 378 $\\uparrow$ & 100~300 & 10^9/L \\\\\n6 嗜碱性粒细胞\\% & 0.30 & 0.00~1.00 & \\% & 23血小板比容 & 0.37 $\\uparrow$ & 0.06~0.28 & \\% \\\\\n7 中性粒细胞绝对数 & 4.21 & 1.50~7.00 & 10^9/L & 24平均血小板体积 & 9.9 & 6.4~12.1 & f1 \\\\\n8 淋巴细胞绝对数 & 1.68 & 0.80~4.00 & 10^9/L & 25血小板体积分布宽度 & 16.5 & 9.0~17.0 & \\% \\\\\n9 单核细胞绝对数 & 0.64 & 0.12~0.80 & 10^9/L & 26大血小板比率 & 24.80 & 13.00~43.00 & \\% \\\\\n10嗜酸性粒细胞绝对数 & 0.03 & 0.00~0.50 & 10^9/L & 27C-反应蛋白 & 97.64 $\\uparrow$ & 0~8.00 & mg/L \\\\\n11嗜碱性粒细胞绝对数 & 0.02 & 0.00~0.10 & 10^9/L & & & & \\\\\n12★红细胞计数 & 4.55 & 3.50~6.00 & 10^12/L & & & & \\\\\n13★血红蛋白 & 131.0 & 120.0~165.0 & g/L & & & & \\\\\n14★红细胞比积 & 39.7 $\\downarrow$ & 40.0~50.0 & \\% & & & & \\\\\n15★平均红细胞体积 & 87.2 & 80.0~100.0 & f1 & & & & \\\\\n16平均红细胞血红蛋白含量 & 28.7 & 27.3~34.4 & pg & & & & \\\\\n17平均红细胞血红蛋白浓度 & 330.0 & 320.0~360.0 & g/L & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:28:33,110 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:28:33.110+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 90, "failed": 0, "current": {"dbb9d9e294ee11f1bd9827cf206dfa2d": {"id": "dbb9d9e294ee11f1bd9827cf206dfa2d", "doc_id": "db844cb494ee11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 14828427, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786388903475, "task_type": "dataflow", "root_trace_id": "9d9ed785184e435b9d8a5693cadbcf94", "root_traceparent": "00-9d9ed785184e435b9d8a5693cadbcf94-7ebd92d2185d496c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:28:34,406 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:28:34,406 INFO     29 [qwen-vl-text] LLM output (len=1170):
{
  "note_type": "其他",
  "record_time": "2024-06-19 14:44",
  "recorder": null,
  "reviewer": null,
  "reviewer_title": null,
  "cf_summary": null,
  "cf_positive_findings": [],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": null,
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": null,
  "tp_examinations": [],
  "tp_treatments": [],
  "tp_notes": null,
  "condition_changes": "患者入室后，核查患者姓名、疾病名称、住院号、胸部CT姓名全部一致，患者平卧位行气管插管、全身麻醉后，取左侧卧位，左侧胸壁下垫海绵垫，固定患者，调整手术床呈折刀位。标记手术切口。常规碘伏消毒3遍，铺无菌巾，于右侧腋中线第5肋间切开皮肤约2.5cm，探查见右肺肺组织与胸壁无明显粘连，肿块位于右肺中叶，大小约3*3cm，脏层胸膜皱缩，脏层胸膜及壁层胸膜可见多发黄白色粟粒状结节，未见明显胸腔积液；用电钩游离出中叶动、静脉，用直线切割缝合器切断，清扫中叶支气管周围淋巴结后，夹闭支气管，麻醉师吸痰胀肺，确认为右肺中叶支气管后将中叶支气管用直线切割缝合器切断，继续将右肺水平裂用直线切割缝合器切断，将右肺中叶放入8号手套中，自胸腔内取出，于前纵隔壁层胸膜切除部分壁层胸膜结节，使用一次性直线切割缝合器于下叶背段切除部分脏层胸膜结节，送快速病理，半小时后病理示：右肺中叶浸润腺癌，脏层、壁层胸膜结节查见腺癌；遂用电刀行纵隔淋巴结采样，并充分止血，冲洗胸腔，麻醉师吸痰胀肺，检查无漏血漏气后，于右侧胸壁切口处置入26号胸腔闭式引流管，接水封瓶，用可吸收线缝合腋前线切口。手术程顺利，术中出血约20ml，未输血。病人清醒后拔除气管插管，安返病",
  "test_results": null,
  "superior_opinion": null,
  "consultation_opinion": null,
  "measures_and_effects": null,
  "order_changes": null,
  "patient_notification": null,
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 19:28:34,413 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1996608, prompt_len=1469
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["手术记录", "年龄：67岁", "病", "手术日期：2024-06-19", "手术时间：12:50~14:35", "才", "1.肺占位性病变2.腰椎间盘突出", "术中诊断：", "1.右肺中叶癌2.胸膜继发恶性肿瘤3.腰椎间盘突出", "手术名称：胸腔镜右肺中叶切除+脏层胸膜结节切除+壁层胸膜结节切除+淋巴结切除术", "麻醉方法：", "全身麻醉", "手术指导者：", "手术经过、术中发现的情况及处理：", "患者入室后，核查患者姓名、疾病名称、住院号、胸部CT姓名全部一致，患者平卧位行气管插管、全", "身麻醉后，取左侧卧位，左侧胸壁下垫海绵垫，固定患者，调整手术床呈折刀位。标记手术切口。常规碘伏", "消毒3遍，铺无菌巾，于右侧腋中线第5肋间切开皮肤约2.5cm，探查见右肺肺组织与胸壁无明显粘连，肿块", "位于右肺中叶，大小约3*3cm，脏层胸膜皱缩，脏层胸膜及壁层胸膜可见多发黄白色粟粒状结节，未见明显", "胸腔积液；用电钩游离出中叶动、静脉，用直线切割缝合器切断，清扫中叶支气管周围淋巴结后，夹闭支气", "管，麻醉师吸痰胀肺，确认为右肺中叶支气管后将中叶支气管用直线切割缝合器切断，继续将右肺水平裂用", "直线切割缝合器切断，将右肺中叶放入8号手套中，自胸腔内取出，于前纵隔壁层胸膜切除部分壁层胸膜结", "节，使用一次性直线切割缝合器于下叶背段切除部分脏层胸膜结节，送快速病理，半小时后病理示：右肺中", "叶浸润腺癌，脏层、壁层胸膜结节查见腺癌；遂用电刀行纵隔淋巴结采样，并充分止血，冲洗胸腔，麻醉师", "吸痰胀肺，检查无漏血漏气后，于右侧胸壁切口处置入26号胸腔闭式引流管，接水封瓶，用可吸收线缝合腋", "前线切口。手术程顺利，术中出血约20ml，未输血。病人清醒后拔除气管插管，安返病", "10", "58", "26.0", "188.8.155", "激活Winc", "转到\"设置\"以", "记录时间：2024-06-19 14:44:23"]

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
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord API raw response (len=2149):
[
	{"text": "手术记录", "bbox": [440, 177, 535, 194]},
	{"text": "年龄：67岁", "bbox": [753, 149, 861, 164]},
	{"text": "病", "bbox": [753, 183, 787, 196]},
	{"text": "手术日期：2024-06-19", "bbox": [44, 220, 231, 236]},
	{"text": "手术时间：12:50~14:35", "bbox": [277, 220, 482, 236]},
	{"text": "才", "bbox": [43, 245, 61, 261]},
	{"text": "1.肺占位性病变2.腰椎间盘突出", "bbox": [44, 273, 333, 289]},
	{"text": "术中诊断：", "bbox": [44, 298, 137, 314]},
	{"text": "1.右肺中叶癌2.胸膜继发恶性肿瘤3.腰椎间盘突出", "bbox": [44, 326, 481, 342]},
	{"text": "手术名称：胸腔镜右肺中叶切除+脏层胸膜结节切除+壁层胸膜结节切除+淋巴结切除术", "bbox": [44, 351, 752, 367]},
	{"text": "麻醉方法：", "bbox": [816, 352, 897, 367]},
	{"text": "全身麻醉", "bbox": [44, 378, 128, 394]},
	{"text": "手术指导者：", "bbox": [44, 404, 144, 419]},
	{"text": "手术经过、术中发现的情况及处理：", "bbox": [44, 428, 370, 444]},
	{"text": "患者入室后，核查患者姓名、疾病名称、住院号、胸部CT姓名全部一致，患者平卧位行气管插管、全", "bbox": [44, 456, 906, 472]},
	{"text": "身麻醉后，取左侧卧位，左侧胸壁下垫海绵垫，固定患者，调整手术床呈折刀位。标记手术切口。常规碘伏", "bbox": [44, 481, 914, 498]},
	{"text": "消毒3遍，铺无菌巾，于右侧腋中线第5肋间切开皮肤约2.5cm，探查见右肺肺组织与胸壁无明显粘连，肿块", "bbox": [44, 507, 906, 523]},
	{"text": "位于右肺中叶，大小约3*3cm，脏层胸膜皱缩，脏层胸膜及壁层胸膜可见多发黄白色粟粒状结节，未见明显", "bbox": [44, 533, 905, 549]},
	{"text": "胸腔积液；用电钩游离出中叶动、静脉，用直线切割缝合器切断，清扫中叶支气管周围淋巴结后，夹闭支气", "bbox": [44, 559, 914, 575]},
	{"text": "管，麻醉师吸痰胀肺，确认为右肺中叶支气管后将中叶支气管用直线切割缝合器切断，继续将右肺水平裂用", "bbox": [44, 585, 914, 601]},
	{"text": "直线切割缝合器切断，将右肺中叶放入8号手套中，自胸腔内取出，于前纵隔壁层胸膜切除部分壁层胸膜结", "bbox": [44, 611, 905, 627]},
	{"text": "节，使用一次性直线切割缝合器于下叶背段切除部分脏层胸膜结节，送快速病理，半小时后病理示：右肺中", "bbox": [44, 638, 914, 654]},
	{"text": "叶浸润腺癌，脏层、壁层胸膜结节查见腺癌；遂用电刀行纵隔淋巴结采样，并充分止血，冲洗胸腔，麻醉师", "bbox": [44, 664, 914, 680]},
	{"text": "吸痰胀肺，检查无漏血漏气后，于右侧胸壁切口处置入26号胸腔闭式引流管，接水封瓶，用可吸收线缝合腋", "bbox": [44, 690, 914, 706]},
	{"text": "前线切口。手术程顺利，术中出血约20ml，未输血。病人清醒后拔除气管插管，安返病", "bbox": [44, 716, 767, 732]},
	{"text": "10", "bbox": [787, 708, 840, 732]},
	{"text": "58", "bbox": [84, 747, 124, 771]},
	{"text": "26.0", "bbox": [542, 747, 653, 789]},
	{"text": "188.8.155", "bbox": [574, 780, 771, 839]},
	{"text": "激活Winc", "bbox": [880, 815, 997, 835]},
	{"text": "转到\"设置\"以", "bbox": [880, 838, 997, 854]},
	{"text": "记录时间：2024-06-19 14:44:23", "bbox": [569, 850, 837, 864]}
]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=10.8s
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[0]: text=手术记录, bbox=[440, 177, 535, 194]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[1]: text=年龄：67岁, bbox=[753, 149, 861, 164]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[2]: text=病, bbox=[753, 183, 787, 196]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[3]: text=手术日期：2024-06-19, bbox=[44, 220, 231, 236]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[4]: text=手术时间：12:50~14:35, bbox=[277, 220, 482, 236]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[5]: text=才, bbox=[43, 245, 61, 261]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[6]: text=1.肺占位性病变2.腰椎间盘突出, bbox=[44, 273, 333, 289]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[7]: text=术中诊断：, bbox=[44, 298, 137, 314]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[8]: text=1.右肺中叶癌2.胸膜继发恶性肿瘤3.腰椎间盘突出, bbox=[44, 326, 481, 342]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[9]: text=手术名称：胸腔镜右肺中叶切除+脏层胸膜结节切除+壁层胸膜结节切除+淋巴结切除术, bbox=[44, 351, 752, 367]
2026-08-10 19:28:45,242 INFO     29 [qwen-vl-text] coord item[10]: text=麻醉方法：, bbox=[816, 352, 897, 367]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[11]: text=全身麻醉, bbox=[44, 378, 128, 394]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[12]: text=手术指导者：, bbox=[44, 404, 144, 419]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[13]: text=手术经过、术中发现的情况及处理：, bbox=[44, 428, 370, 444]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[14]: text=患者入室后，核查患者姓名、疾病名称、住院号、胸部CT姓名全部一致，患者平卧位行气管插管、全, bbox=[44, 456, 906, 472]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[15]: text=身麻醉后，取左侧卧位，左侧胸壁下垫海绵垫，固定患者，调整手术床呈折刀位。标记手术切口。常规碘伏, bbox=[44, 481, 914, 498]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[16]: text=消毒3遍，铺无菌巾，于右侧腋中线第5肋间切开皮肤约2.5cm，探查见右肺肺组织与胸壁无明显粘连，肿块, bbox=[44, 507, 906, 523]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[17]: text=位于右肺中叶，大小约3*3cm，脏层胸膜皱缩，脏层胸膜及壁层胸膜可见多发黄白色粟粒状结节，未见明显, bbox=[44, 533, 905, 549]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[18]: text=胸腔积液；用电钩游离出中叶动、静脉，用直线切割缝合器切断，清扫中叶支气管周围淋巴结后，夹闭支气, bbox=[44, 559, 914, 575]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[19]: text=管，麻醉师吸痰胀肺，确认为右肺中叶支气管后将中叶支气管用直线切割缝合器切断，继续将右肺水平裂用, bbox=[44, 585, 914, 601]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[20]: text=直线切割缝合器切断，将右肺中叶放入8号手套中，自胸腔内取出，于前纵隔壁层胸膜切除部分壁层胸膜结, bbox=[44, 611, 905, 627]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[21]: text=节，使用一次性直线切割缝合器于下叶背段切除部分脏层胸膜结节，送快速病理，半小时后病理示：右肺中, bbox=[44, 638, 914, 654]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[22]: text=叶浸润腺癌，脏层、壁层胸膜结节查见腺癌；遂用电刀行纵隔淋巴结采样，并充分止血，冲洗胸腔，麻醉师, bbox=[44, 664, 914, 680]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[23]: text=吸痰胀肺，检查无漏血漏气后，于右侧胸壁切口处置入26号胸腔闭式引流管，接水封瓶，用可吸收线缝合腋, bbox=[44, 690, 914, 706]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[24]: text=前线切口。手术程顺利，术中出血约20ml，未输血。病人清醒后拔除气管插管，安返病, bbox=[44, 716, 767, 732]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[25]: text=10, bbox=[787, 708, 840, 732]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[26]: text=58, bbox=[84, 747, 124, 771]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[27]: text=26.0, bbox=[542, 747, 653, 789]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[28]: text=188.8.155, bbox=[574, 780, 771, 839]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[29]: text=激活Winc, bbox=[880, 815, 997, 835]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[30]: text=转到"设置"以, bbox=[880, 838, 997, 854]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] coord item[31]: text=记录时间：2024-06-19 14:44:23, bbox=[569, 850, 837, 864]
2026-08-10 19:28:45,243 INFO     29 [qwen-vl-text] page=14 — 32/32 coords, api_time=10.8s
2026-08-10 19:28:45,244 INFO     29 [qwen-vl-text] new_positions (32):
[[14, 261.8, 318.325, 149.034, 163.34799999999998], [14, 448.03499999999997, 512.295, 125.458, 138.088], [14, 448.03499999999997, 468.265, 154.08599999999998, 165.03199999999998], [14, 26.18, 137.445, 185.23999999999998, 198.712], [14, 164.815, 286.78999999999996, 185.23999999999998, 198.712], [14, 25.584999999999997, 36.295, 206.29, 219.762], [14, 26.18, 198.135, 229.86599999999999, 243.338], [14, 26.18, 81.515, 250.916, 264.388], [14, 26.18, 286.195, 274.492, 287.964], [14, 26.18, 447.44, 295.542, 309.014], [14, 485.52, 533.715, 296.384, 309.014], [14, 26.18, 76.16, 318.276, 331.748], [14, 26.18, 85.67999999999999, 340.168, 352.798], [14, 26.18, 220.14999999999998, 360.376, 373.848], [14, 26.18, 539.0699999999999, 383.952, 397.424], [14, 26.18, 543.8299999999999, 405.002, 419.316], [14, 26.18, 539.0699999999999, 426.894, 440.366], [14, 26.18, 538.475, 448.786, 462.258], [14, 26.18, 543.8299999999999, 470.678, 484.15], [14, 26.18, 543.8299999999999, 492.57, 506.042], [14, 26.18, 538.475, 514.462, 527.934], [14, 26.18, 543.8299999999999, 537.196, 550.668], [14, 26.18, 543.8299999999999, 559.088, 572.56], [14, 26.18, 543.8299999999999, 580.98, 594.452], [14, 26.18, 456.36499999999995, 602.872, 616.3439999999999], [14, 468.265, 499.79999999999995, 596.136, 616.3439999999999], [14, 49.98, 73.78, 628.9739999999999, 649.182], [14, 322.49, 388.53499999999997, 628.9739999999999, 664.338], [14, 341.53, 458.745, 656.76, 706.438], [14, 523.6, 593.2149999999999, 686.23, 703.0699999999999], [14, 523.6, 593.2149999999999, 705.596, 719.068], [14, 338.555, 498.015, 715.6999999999999, 727.4879999999999]]
2026-08-10 19:28:45,246 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=27.3s
2026-08-10 19:28:45,252 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 19:28:45,253 INFO     29 [Trace] task=dbb9d9e2 | doc=12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf | Extractor:Progress | outputs={"chunks": "1 items, types={'ProgressNote': 1}", "html": "", "json": "3449 items", "markdown": "", "text": "", "name": "12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf", "output_format": "chunks", "chunks_Examination": "16 items, types={'ExaminationReport': 16}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Progress": "1 items, types={'ProgressNote': 1}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "chunks_Clinical": "9 items, types={'OutpatientRecord': 9}", "route_summary": "{\"chunks_Examination\": 16, \"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Progress\": 1, \"chunks_LabExam\": 5, \"chunks_Clinical\": 9}"}
2026-08-10 19:28:45,253 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 19:28:45,254 INFO     29 [ChunkMerger] Merged 33 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 9, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 16, 'Extractor:Progress': 1} (filtered 3 noise chunks)
2026-08-10 19:28:45,527 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 19:28:45,527 INFO     29 [Trace] task=dbb9d9e2 | doc=12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "33 items, types={'LabReport': 5, 'OutpatientRecord': 9, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 16, 'ProgressNote': 1}", "name": "12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf"}
2026-08-10 19:28:45,527 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 19:28:45,803 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786389861202, 'update_date': datetime.datetime(2026, 8, 10, 19, 24, 21), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1402087, 'status': '1'}
2026-08-10 19:28:46,015 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   癌胚抗原  None  19.80  ng/mL  0--5  True    糖类抗原125  None  15.700  u/ml  0--35  False    非小细胞肺癌相关抗原  None  1.330  ng/ml  0.1--3.3  False    鳞状细胞癌相关抗原  None  1.66  ng/ml  0.011--2.5  False   
---
   钾  None  4.06  mmol/L  3.5--5.3  False    钠  None  140.6  mmol/L  137--147  False    氯  None  106.5  mmol/L  99--110  False    二氧化碳  None  25.5  mmol/L  22--29  False    阴离子隙  None  12.66  mmol/L  8.00--16.00  False    钙  None  2.38  mmol/L  2.03--2.54  False    磷  None  1.20  mmol/L  0.9--1.34  False    镁  None  0.94  mmol/L  0.7--1.1  False    尿素  None  3.70  mmol/L  2.9--8.2  False    肌酐  None  54.0  μmol/L  53--97  False    尿酸  None  289.0  μmol/L  155--357  False    血糖  None  5.83  mmol/L  3.9--6.1  False    渗透压  None  280.05  mOsm/L  275--300  False    胆碱酯酶  None  9023  U/L  5000--12000  False    总蛋白  None  73.0  g/L  60--80  False    白蛋白  None  46.2  g/L  34--48  False    球蛋白  None  26.8  g/L  20.0--35.0  False    白蛋白/球蛋白  None  1.72  g/g  1.00--2.00  False    总胆红素  None  15.1  μmol/L  2--24  False    结合胆红素  None  5.4  μmol/L  0--5  True    非结合胆红素  None  9.7  μmol/L  1.7--20.6  False    天冬氨酸氨基转移酶  None  15.2  U/L  13--35  False    丙氨酸氨基转移酶  None  11.0  U/L  7--40  False   
---
   磷  None  1.20  mmol/L  0.9--1.34  False    镁  None  0.94  mmol/L  0.7--1.1  False    尿素  None  3.70  mmol/L  2.9--8.2  False    肌酐  None  54.0  µmol/L  53--97  False    尿酸  None  289.0  µmol/L  155--357  False    血糖  None  5.83  mmol/L  3.9--6.1  False    渗透压  None  280.05  mOsm/L  275-300  False    胆碱酯酶  None  9023  U/L  5000--12000  False    总蛋白  None  73.0  g/L  60--80  False    白蛋白  None  46.2  g/L  34--48  False    球蛋白  None  26.8  g/L  20.0--35.0  False    白蛋白/球蛋白  None  1.72  g/g  1.00--2.00  False    总胆红素  None  15.1  µmol/L  2--24  False    结合胆红素  None  5.4  µmol/L  0--5  True    非结合胆红素  None  9.7  µmol/L  1.7--20.6  False    天冬氨酸氨基转移酶  None  15.2  U/L  13--35  False    丙氨酸氨基转移酶  None  11.0  U/L  7--40  False    谷草酶/谷丙酶  None  1.38  U/U  1.00-2.00  False    碱性磷酸酶  None  85.0  U/L  40--150  False    r-谷氨酰转肽酶  None  17.0  U/L  7--45  False    甘油三酯  None  0.98  mmol/L  0.56--1.7  False    总胆固醇  None  4.93  mmol/L  2.33--5.17  False    高密度脂蛋白胆固醇  None  1.53  mmol/L  0.83--1.96  False    低密度脂蛋白胆固醇  None  3.20  mmol/L  2.07--3.1  True    脂蛋白(a)  None  109.8  mg/L  0--300  False    甘胆酸  None  1.0  mg/L  0--2.7  False    5'-核苷酸酶  None  6.0  U/L  2--11.4  False   
---
   白细胞  WBC  6.94  x10^9/L  3.5--9.5  False    红细胞  RBC  4.23  x10^12/L  3.8--5.1  False    血红蛋白  HGB  124.0  g/L  115--150  False    红细胞比积  HCT  38.80  %  35--45  False    平均红细胞体积  MCV  91.7  fl  82--100  False    平均红细胞血红蛋白含量  MCH  29.3  pg  27--34  False    平均红细胞血红蛋白浓度  MCHC  320.0  g/L  316--354  False    红细胞分布宽度  RDW  45.90  fl  37.0--54.0  False    红细胞变异系数  RDW-CV  13.90  %  11--16.5  False    血小板  PLT  159  x10^9/L  125--350  False    平均血小板体积  MPV  8.90  fl  6.5--17  False    血小板分布宽度  PDW  16.90  fl  9--17  False    大型血小板比率  P-LCR  20.9  %  13--43  False    血小板比积  PCT  0.14  %  0.17--0.35  True    中性粒细胞  NEUT#  5.38  x10^9/L  1.8--6.3  False    淋巴细胞  LYMPH#  1.11  x10^9/L  1.1--3.2  False    单核细胞  MONO#  0.38  x10^9/L  0.1--0.6  False    嗜酸性粒细胞  EO#  0.06  x10^9/L  0.02--0.52  False    嗜碱性粒细胞  BASO#  0.01  x10^9/L  0--0.06  False    中性粒细胞比率  NEUT%  77.5  %  40--75  True    淋巴细胞比率  LYMPH%  16.0  %  20--50  True    单核细胞比率  MONO%  5.5  %  3--10  False    嗜酸性粒细胞比率  EO%  0.9  %  0.4--8  False    嗜碱性粒细胞比率  BASO%  0.1  %  0--1  False   
---
   癌胚抗原  None  19.08  ng/mL  0--5  True    糖类抗原125  None  24.810  u/ml  0--35  False    非小细胞肺癌相关抗原  None  2.040  ng/ml  0.1--3.3  False    鳞状细胞癌相关抗原  None  1.43  ng/ml  0.011--2.5  False   
---
CDSS
主诉:肺占位术后1.5年余来诊。
现病史:患者于1.5年前因肺占位行手术治疗,术后病理示恶性肿瘤,术后恢复良好。
既往史:无
过敏史:无
体格检查:神志清,可,手术切口愈合良好,无红肿及脓性分泌物,呼吸音清,无明显干湿啰音,腹软,无压痛及反跳痛。
辅助检查:
门诊诊断:肺恶性肿瘤个人史
治疗计划:
26
---
主诉：肺占位术后1年余来诊。
现病史：患者于*年*月*日行*手术治疗，术后病理提示恶性肿瘤，术后恢复良好。
既往史：无
过敏史：无
体格检查：神志清，精神可，手术切口愈合良好，无红肿及脓性分泌物，无明显干湿啰音，腹软，无压痛及反跳痛。
辅助检查：
门诊诊断：
肺恶性肿瘤
治疗计划：继
---
主诉：肺占位术后1.5年余来诊。
现病史：患者于1.5年前因
术治疗，术后病理示恶性肿瘤，术后
体格检查：神志清，精神可，手术切口愈合良好，无红肿及脓性分泌
音，腹软，无压痛及反跳痛。
辅助检查：
门诊诊断：
肺恶性肿瘤个人史
治疗计划：继续服用奥
---
主诉: 肺占位术后1年余来诊。
现病史: 患者于1年前因
手术治疗, 术后病理示恶性肿瘤, 辅助靶向治疗,
既往史
过敏史:
体格检查: 神志清, 精神可, 手术切口愈合良好, 无红
音, 腹软, 无压痛及反跳痛。
辅助检查:
门诊诊断:
肺恶性肿瘤
治疗计划: 继续靶向治疗, 定
---
25-09-19 08:02
诊断证明
25-09-19 08:09
2025-09-19 08:02
初诊病历
主诉：肺占位术后1年余来诊。
现病史：患者于1年前因肺占位行手术治疗，术后病理示恶性肿瘤，术后恢复良好。
既往
体格检查：神志清，精神可，手术切口愈合良好，无红肿及脓性分泌
音，腹软，无压痛及反跳痛。
辅助检查：
门诊诊断：
肺恶性肿瘤个人史
治疗计划：继续服用奥希替尼治疗
---
2025-08-15 09:4
门诊初诊病历
主诉：肺占位术后1年余来诊。
现病史：患者于1年前因
术后病理示恶性肿瘤，术后恢复良好。
既往史：无
过敏史:无
体格检查：神...，精神可，手术切口愈合良好，无红肿及脓性分泌物，双肺呼吸音清，无明显干湿
音，腹软，无压痛及反跳痛。
辅助检查：
门诊诊断：
肺恶性肿瘤个人史
治疗计划：继续服用奥希替尼治疗。
---
主诉：肺占位术后3月余来诊。
现病史：患者于3月前因肺占位行手术治疗，术后病理示恶性肿瘤，术后恢复良好。
既往史：无
过敏史:无
体格检查：神志清，精神可，手术切口愈合良好，无红肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。
辅助检查：
门诊诊断：
肺恶性肿瘤个人史
治疗计划：肺癌术后辅助奥希替尼治疗。
---
主诉：肺占位术后4月余来诊。
现病史：患者于4月前因肺占位行手术治疗，术后病理示恶性肿瘤，术后恢复良好。
既往史：无
过敏史:无
体格检查：神志清，精神可，手术切口愈合良好，无红肿及脓性分泌物，叩及音清，无明显干湿啰音，腹软，无压痛及反跳痛。
辅助检查：
门诊诊断：
肺恶性肿瘤个人史
治疗计划：术后辅助奥希替尼靶向治疗
---
主诉：肺占位术后5月余来诊。
现病史：患者于5月前因肺占位行手术治疗，术后病理示恶性肿瘤，术后恢复良好。
既往史：无
过敏史:无
体格检查：神志清，精神可，手术切口愈合良好，无红肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。
辅助检查：
门诊诊断：
肺恶性肿瘤个人史
治疗计划：继续服用奥希替尼。
---
记录
姓名
性别：女
年龄：67岁
入院日期：2024-06-16 09:47:48
出院日期：2024-06-24 11:00:00
住院天数：8天
入院情
7岁。患者1天前查体行胸部CT示右肺中叶软组织密度肿块，最大截面约2.8*
2.4cm，可见浅分叶及毛刺，血管穿行，右肺中叶外侧段支气管狭窄闭塞，平素偶有胸闷、憋气，伴右侧胸
痛，无明显咳嗽、咳痰，无咳血，无声音嘶哑，无饮水呛咳，无明显头晕、头痛，无发热、盗汗，无明显恶
心、呕吐，无黑便、血便等症状，未行特殊治疗。现为行进一步治疗来我科就诊，门诊以“肺占位性病变”
为诊断收入院。患者自本次发病以来，饮食可，睡眠可，大便如常，小便如常，体重未见明显变化。
入院诊断：
1. 肺占位性病变
2. 腰椎间盘突出
诊疗经过：入院后完善相关检查，排除手术禁忌，2024.6.19在全麻下行胸腔镜右肺中叶切除+脏层胸膜结节
切除+壁层胸膜结节切除+淋巴结切除术，手术顺利，2024.06.21 17:05 冰冻病理申请单(新病理)术中冰冻
快速病理检查 检查诊断 标本名称： 右肺中叶切除+脏层胸膜结节切除+壁层胸膜结节切除+淋巴结切除标本
肿瘤病理诊断： （右肺中叶）浸润性非黏液腺癌（V：2.7x2.4x2.3cm），ICD-0编码（8140-3），贴壁型
约10%，腺泡型约20%，乳头型约20%，微乳头型约20%，复杂腺体及筛状型约30%，不伴肿瘤性坏死。（脏层胸
膜结节）查见腺癌（S1：0.2x0.1cm，S2：0.3x0.2cm）。（壁层胸膜结节）查见腺癌。肿瘤分级： 低分化。
肿瘤数量： 1个。脉管内癌栓： 脉管内见癌栓。神经侵犯： 神经未见癌组织侵犯，沿气道播散STAS： 查见
STAS。胸膜侵犯： 侵及壁层胸膜，PL3(改进Hammar分级)。切缘情况： 支气管断端及肺切缘均未见癌。周围
肺情况： 周围肺组织示炭末沉积及细支气管化生，支气管周围淋巴结： 查见支气管周围淋巴结（0/1）枚，
未见癌组织转移。送检淋巴结： 送检"第7组"淋巴结（0/1）枚，"第10组"淋巴结（0/1）枚，"第11组"淋巴
结（0/1）枚，"第12组"淋巴结（0/1）枚，未见癌组织转移。免疫组化： 1#TTF-1/弹力纤维（+）：3
#TTF-1（+）；8#TTF-1（+），P40（+）；10#TTF-1/弹力纤维（+）；11#TTF-1/弹力纤维（+），P40（-）。
特殊染色：8#六胺银染色（-）。术后对症支持治疗，好转出院。
出院诊断：
1. 肺恶性肿瘤(T3NOM0)
2. 胸膜继发性恶性肿瘤
3. 腰椎间盘突出
出院情况：一般情况可，生命体征平稳，无发热，辅料整洁干燥，听诊双肺呼吸音清，未闻及干湿啰音。
本页以下空白
出院记录
病案号：
出院医嘱：（注意事项）
1、注意休息，加强营养，注意活动双下肢预防血栓形成。添加下方二维码了解相关知识，保持网上随诊。
2、根据出院要求按时服药。出院带药：布地奈德福莫特罗粉吸入剂1吸吸入BID（共：1盒），酮咯酸氨丁
三醇胶囊（新时代）10mg口服TID（共：8粒），复方甲氧那明胶囊Δ2粒口服TID（共：1盒）
3、就近选择诊所、医院刀口换药，3天1次至刀口干燥结疤，无需拆线。
4、1周后（周日）返院胸外门诊复查，咨询基因检测，可微信搜索“临沂市人民医院”公众号预约挂号。
5、如果需要复印住院病历，可于出院后2周到1号楼3楼病案室复印。
6、门诊3楼慢特病门诊可办理慢特病备案。来院就诊，需到慢特病门诊窗口取号，然后到胸外科门诊就诊。
7、其他疾病定期复查，病情如有变化及时医院就诊。
家
签名：
床号：1-24床
0212:
---
八院记录
出生地
：
职
：
年
龄：67岁
入院日期：2024-06-16 09:47:48
民
族：汉族
记录日期：2024-06-16 15:24:34
婚
姻：已婚
病史陈述者：患者本人
主诉：查体发现肺结节1天。
现病史：患者1天前查体行胸部CT示右肺中叶软组织密度肿块，最大截面约2.8*2.4cm，可见浅分叶及毛
刺，血管穿行，右肺中叶外侧段支气管狭窄闭塞，平素偶有胸闷、憋气，伴右侧胸痛，无明显咳嗽、咳痰，
无咳血，无声音嘶哑，无饮水呛咳，无明显头晕、头痛，无发热、盗汗，无明显恶心、呕吐，无黑便、血便
等症状，未行特殊治疗。现为行进一步治疗来我科就诊，门诊以“肺占位性病变”为诊断收入院。患者自本
次发病以来，饮食可，睡眠可，大便如常，小便如常，体重未见明显变化。
既往史：平素健康状况良好。腰椎间盘突出病史10年，否认高血压病史。否认糖尿病病史。否认冠心病
病史。否认慢性支气管炎病史。否认胆结石病史。否认胆囊炎病史，否认传染病史，预防接种史不详。否认
手术外伤史，否认输血史。否认药物过敏史，否认食物过敏史。
个人史：出生于山东省临沂市。否认吸烟史；否认饮酒史，否认药物嗜好。否认疫区、疫水旅居史或接
触史，无工业毒物、粉尘、放射性物质接触史。无冶游史。
月经史：19
3-4
30
44
。经期规则，经量中等，无痛经。
婚育史：已婚，结婚年龄：27岁，已育1子1女，子女健康状况良好。
家族史：父母非近亲结婚；父：已故；母：已故。
似患者。否认家族遗传性病史。
以上病史记录我已确认，属实。患者/家属
体格检查
T
P 76次/分
R 18次/分
BP141/79mmHg
发育正常，营养良好，正常面容，表情自然，自主体位，神志清楚，言语清晰，查体合作。全身皮肤粘膜
无黄染，无水肿，无肝掌，无蜘蛛痣。全身浅表淋巴结无肿大。头颅无畸形，无压痛，无头部包块。眼睑正
常，结膜正常，巩膜无黄染，双瞳孔等大、等圆，双眼瞳孔对光反射灵敏。耳廓正常，无外耳道分泌物，无
乳突压痛，无听力粗试障碍。鼻外形正常，嗅觉正常。口唇红润，口腔粘膜正常，扁桃体无肿大。颈软，无
抵抗，颈动脉正常搏动，无颈静脉怒张，气管居中，双侧甲状腺无肿大，无压痛，无结节，未及震颤，颈静
脉回流征阴性。胸部查体见专科情况。心前区无隆起；心尖搏动正常，未触及震颤；心浊音界无明显扩
大，心律齐，无杂音，于心包摩擦音，腹部平田，于腹壁静脉曲张，腹壁柔软，紧张度适中，于压痛，于反
入院记录
病
胱无充盈，尿管压痛点无压痛；移动性浊音(-)，肠鸣音正常。生殖器：未查，肛门直肠：未查。脊柱
正常，活动度正常。四肢正常，运动正常，关节无红肿、无压痛，活动正常，双下肢无水肿，肌张力正常，
四肢肌力正常。腹壁反射存在，肱二头肌反射存在，肱三头肌反射存在，膝反射存在。巴氏征(右)：未引
出，巴氏征(左)：未引出；克氏征(右)：未引出，克氏征(左)：未引出；布氏征：未引出。生理反射存在，
病理反射未引出。
专科情况：胸廓对称，外形正常，无胸骨压痛，乳房正常对称。双侧呼吸运动对称，肋间隙正常；语颤
正常，无胸膜摩擦感；叩诊呈清音；双肺呼吸音稍粗，未闻及干湿啰音，无胸膜摩擦音。
辅助检查
双肺CT平扫 2024-6-15 蒙阴县高都镇卫生院 右肺中叶软组织密度肿块，最大截面约2.8*2.4cm，可见浅
分叶及毛刺，血管穿行，
支气管狭窄闭塞。
初步诊断：
1.肺占位性病变
2.腰椎间盘
2026-08-10 19:28:46,727 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=26-03-02 术中冰冻病理报告单
病理号：2
姓名
性别：女 年龄：67岁 收到日期：2024-06-19 14:28
送检医院： 送检科室：胸外科 病案号：8001067375
送检医生：5123 病 区：胸外科 床号：1-18床
冰冻诊断：
(右肺中叶)浸润性腺癌。
(脏层胸膜结节)查见腺癌。
(壁层胸膜结节)查见腺癌。
26-03
报告医生：
报告日期：2024-06-19 14:54
---
病理诊断报告单
姓名：
性别：女 年龄：67岁
送检医院：
病案
床号：1-18床
收到日期：2024-06-19
门诊号：
报告日期：2024-06-21
标本名称：1.肺切除标本，2.右肺中叶，3.临床诊断：
入院诊断：肺占位性病变,腰椎间盘突
壁层胸膜结节，4.脏层胸膜
出
巨检:右肺中叶：肺组织一块，V：9x6x2cm，上附钢钉长6cm，临床己切开，切面见一灰白结节，
V：2.7x2.4x2.3cm，切面灰白质脆，紧邻脏层胸膜，距钢钉侧切缘0.8cm，距支气管断端
1.5cm。支气管周围查见结节样物1枚，直径0.8cm。其余肺组织切面灰红灰黑质软。
脏层胸膜结节：肺组织一块，V：3.5x2x1cm，上附钢钉长3.5cm，表面见一系线1，临床己
切开，切面见一灰白结节，S1：0.2x0.1cm，切面灰白质脆，紧邻脏层胸膜，距钢钉侧切缘
1.2cm。距系线1约2cm，见系线2，切面见一灰白结节，S2：0.3x0.2cm，切面灰白质脆，紧
邻脏层胸膜。其余肺组织切面灰红灰黑质软。
壁层胸膜结节：灰黄不规则组织一块，V：1.3x0.5x0.3cm，未见明显结节。全取。冰冻1-4
号
（常规17-20号）送检4份：
1#第7组淋巴结：结节样物1枚，直径0.8cm。
2#第10组淋巴结：结节样物1枚，直径1.2cm。
3#第11组淋巴结：结节样物1枚，直径0.4cm。
4#第12组淋巴结：结节样物1枚，直径0.8cm。
镜下：癌细胞呈腺样排列
放大倍数：10X4 染色：HE
放大倍数：10X10 染色：HP
病理诊断：
标本名称 肺中叶切除+脏层胸膜结节切除+壁层胸膜结节切除+淋巴结切除标本
肿瘤病理诊断：
（右肺中叶）浸润性非黏液腺癌（V：2.7x2.4x2.3cm），ICD-0编码（8140-3），贴壁型
约10%，腺泡型约20%，乳头型约20%，微乳头型约20%，复杂腺体及筛状型约30%，不伴肿瘤
性坏死。
（脏层胸膜结节）查见腺癌（S1：0.2x0.1cm，S2：0.3x0.2cm）。
（壁层胸膜结节）查见腺癌。
报告医师：
---
基因检测报告单
标本编号：
姓
性别：女
年龄：67岁
科室病区：
送检医院：本院
病案号
床
号：1-33床
送检
门诊号：
送检日期：2024-06-20
病理诊断：浸润性非黏液腺癌
原病理号：202435432
标本类型：手术石蜡标本
检测方法：ARMS荧光定量PCR法
检测项目：五种突变基因检测（详见附表）
检测位点：详见附表
检测结果：EGFR基因第21号外显子序列L858R突变
检测可能的局限性：
1、肿瘤组织（细胞）可能存在较大异质性，即不同病灶甚至同一病灶内的组织的突变图
谱可能也存在差异。另外，不同疾病发展或治疗阶段取出的样本中的突变可能不同。
2. 基于肿瘤生物学机制的复杂性，阴性结果不能完全排除突变或融合基因的存在，样本
中肿瘤细胞过少，过度降解或者扩增反应体系中突变DNA浓度或融合RNA浓度低于检测限
亦可造成阴性结果。且不排除检测者带有以上基因的其他突变或融合类型。因此，本检
测报告仅对此次送检的样本负责。
3、本检测不是临床诊断报告，不具备医嘱性质，仅为临床治疗或诊断提供参考，具体的
诊断结果及治疗决策应由临床医生综合患者的
各种临床信息和检测结果
判断。
检测
报告日期：2024-06-25 15:46:21
---
病理诊断报告单
病理号
姓名：
性别：女
年龄：67岁
科室病区：
送检医院：
病案号：8001067375
床号：1-18床
收到日期：2024-06-19
门诊号：
报告日期：2024-06-26
标本名称：1.肺切除标本，2.右肺中
临床诊断：入院诊断：肺占位性病变,腰椎
叶，3.壁层胸膜结节，4.脏
间盘突出
层胸膜
巨检：右肺中叶：肺组织一块，V：9x6x2cm，上附钢钉长6cm，临床已切开，切面见一灰白结
节，V：2.7x2.4x2.3cm，切面灰白质脆，紧邻脏层胸膜，距钢钉侧切缘0.8cm，距支气管
断端1.5cm。支气管周围查见结节样物1枚，直径0.8cm。其余肺组织切面灰红灰黑质软。
脏层胸膜结节：肺组织一块，V：3.5x2x1cm，上附钢钉长3.5cm，表面见一系线1，临床已
切开，切面见一灰白结节，S1：0.2x0.1cm，切面灰白质脆，紧邻脏层胸膜，距钢钉侧切
缘1.2cm。距系线1约2cm，见系线2，切面见一灰白结节，S2：0.3x0.2cm，切面灰白质
脆，紧邻脏层胸膜。其余肺组织切面灰红灰黑质软。
壁层胸膜结节：灰黄不规则组织一块，V：1.3x0.5x0.3cm，未见明显结节。全取。冰冻1-
4号
（常规17-20号）送检4份：
1#第7组淋巴结：结节样物1枚，直径0.3cm。
2#第10组淋巴结：结节样物1枚，直径1.2cm。
3#第11组淋巴结：结节样物1枚，直径0.4cm。
4#第12组淋巴结：结节样物1枚，直径0.8cm。
镜下
放大倍数：10X4 染色：HE
放大倍数：10X10 染色：HP
病理
PD-L1检测结果：
肿瘤比例评分（TPS）（Dako 22C3）
A. 肿瘤比例评分范围：TPS≥50%；
补充报告
报告医师：
CS 扫描全能王
3亿人都在用的扫描App
病理诊断报告单
号：20
女
性别：女
年龄：67岁
科室病区：
送检医院：
病案号：8001067375
床号：1-18床
收到日期：2024-06-19
门诊号：
报告日期：2024-06-26
B. 肿瘤比例评分（TPS）：70%
补充报告
报告医师：
---
基因检测报告单
标本
姓名
性别：女
年龄：67岁
科室病区
送检医院：本院
病
床
号：1-33床
送检医
门诊号：
送检日期：2024-06-20
检测位点附表
检测项目
外显子/密码子
突变类型
EGFR基因
Exon-19
19-del
Exon-21
L858R
Exon-20
T790M
Exon-20
20-ins
Exon-18
G719X
Exon-20
S768I
Exon-21
L861Q
KRAS基因
Exon-2
G12D/S
G12A/V/R/C、G13C
BRAF基因
Exon-15
V600E1/E2/K/R/D1/D2
NRAS基因
Exon-3
Q61R/K/L/H
HER2基因
Exon-20
A775_G776insYVMA (1/2) M774_A775insAYVM / G776>VC (1)/
P780_Y781insGSP(1)
MET基因
Exon-13
Exon-14
Exon-15
跳跃突变
PIK3CA基因
Exon-20
H1047R
Exon-9
E545K
ALK融合基因
ALK-Exon-20
E13;A20,E6ins33;A20,E20;A20,E18;A20,E2;A20,
E17;ins68A20,E2;ins117A20,E13;ins69A20,E6;A20,
E6;A19,E6;ins18A20,E20;ins18A20,E17del58;ins39A20,
E17ins65;A20,E17;ins30A20,E17ins61;ins34A20,
E3;ins53A20,KI24;A20,KI17;A20,KL9;A20,T4;A20
ROS1融合基因
ROS1-Exon-32/34/35
SLC34A2 Exon-4/14、CD74 Exon-6、SDC4 Exon-2/4
SLC34A2 Exon-4/14、EZR Exon-10、CD74 Exon-6、SDC4 Exon-
4TPM3 Exon-8、LRIG3 Exon-16、GOPC Exon-8
RET融合基因
RET-Exon-12
CCDC6 exon 1;RET exon 12
NCOA4 exon 6;RET exon 12
KIF5B exon 15;RET exon 12
KIF5B exon 16;RET exon 12
KIF5B exon 23;RET exon 12
KIF5B exon 22;RET exon 12
检测
报告日期：2024-06-25 15:46:21
注：本报告仅对本标本负责，仅供临床医生参考。如有疑问，请于7个工作日内与病理科联系；8602621
---
病理诊断报告单
病理号
姓名：夕
性别：女 年龄：67岁 科室病区
送检医院：188.8.15
病. 1067375 床号：1-
收到日期：2024-06-19 门诊号：
报告日期：2024-06-21
肿瘤分级：低分化。
肿瘤数量：1个。
脉管内癌栓：脉管内见癌栓。
神经侵犯：神经未见癌组织侵犯。
沿气道播散STAS：查见STAS。
胸膜侵犯：侵及壁层胸膜，PL3(改进Hammar分级)。
切缘情况：支气管断端及肺切缘均未见癌。
周围肺情况：周围肺组织示炭末沉积及细支气管化生。
支气管周围淋巴结：查见支气管周围淋巴结（0/1）枚，未见癌组织转移。
送检淋巴结：送检"第7组"淋巴结（0/1）枚，"第10组"淋巴结（0/1）枚，"第11组"淋巴
结（0/1）枚，"第12组"淋巴结（0/1）枚，未见癌组织转移。
免疫组化：1#TTF-1/弹力纤维（+）；
3#TTF-1（+）；
8#TTF-1（+），P40（+）；
10#TTF-1/弹力纤维（+）；
11#TTF-1/弹力纤维（+），P40（-）。
特殊染色：8#六胺银染色（-）。
---
、心达院医子影像科
影像诊断报告书
取报告生
可扫码查
姓名
性别：女
年龄：67岁
影像号
523551
病区：胸外科
病床：1-18床
病
检查时间：2024-06-16 21:18:43
设备：DISCOVERY MR750w2024061614049
检查项目：颅脑MRI（平扫）
影像表现：
双侧基底节区、放射冠、半卵圆中心、额顶叶可见多发斑片状异
常信号，T1WI、DWI呈等低信号，T2WI呈稍高信号，T2flair呈高信
号。脑室系统扩张，侧脑室前后角旁白质对称性
air高信号。中
线结构居中。脑干、小脑形态信号未见异
双侧基底节区、放射冠、半卵圆中心
顶叶多发缺血灶
2. 脑萎缩、脑白质疏松
---
住院
取报告48小时后
可扫码去二防山
影像诊断报告书
性别：女
年龄：67岁
影像号：450
科_
病区：胸外科
病床：1-18床
病...
检查时间：2024-06-18 09:28:48
设备：Revolution CT
2
检查项目：双肺CT（平扫+强化）
影像表现：双侧胸廓对称，气管纵隔居中，右肺中叶外段（im34）见结节状密
度增高影，大小约28×26mm，边界较清，示支气管截断征，邻近叶间
胸膜轻度受牵拉，增强扫描团块呈轻-中度强化，其内穿行血管壁毛
糙；双肺另见粟粒及微小结节，较大者位于右侧斜裂（im39），大小
约5×3mm，边界清。双肺见条片状密度增高影。纵隔内见增大淋巴结。
心脏未见异常，主动脉及冠脉见钙化影。右侧胸腔少量积液，胸膜未
见增厚
影像诊断：右肺中叶结节，考虑肺癌伴纵隔淋巴结增大，请结合临床，必要时细
胞学检查
双肺多发粟粒及微小结节，可随诊观察
双肺条片影
主动脉及冠脉钙化
右侧胸腔少量积液
报告医师：
报告时间：
2024-06-18
14:41:25审核时间：
2024-06-18
15:24:02
---
住院
取报告48小时
可扫码查
影像诊断报告书
性别：女
年龄：67岁
病区：胸外科
病床：1-33床
病案号：80
时间：2024-06-20 15:03:45
检查项目：胸部正位片
影像表现： 双侧胸廓对称，气管、纵隔居中，右肺纹理模糊，左肺野清晰，
双肺纹理走行自然。心脏、大血管影未见异常。双侧膈面光滑，双侧
肋膈角稍钝。右侧胸腔引流管，右侧胸壁软组织积气。
影像诊断：右肺术后改变。
双侧肋膈角稍钝。
报告医师：
审核医师：
报告时间：
17:26:30审核时间：
2024-06-21
07:53:41
---
放射(1)
报告时间↓
项目
02-27 16:23
双肺CT（平扫）
开单科室 新区胸外科门诊
诊断 肺恶性肿瘤个人史
检查F
审核医
开单时间 2026-02-27 09:17
气肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。
报告日期 2026-02-27 16:23
检查科室 新区医院医学影像科
检查项目
双肺CT（平扫）
检查描述
双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。
检查结论/诊断
双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔积液。甲状腺密度不均。
右肺术后改变，术区团片影、索条影，较前2025.09.19片局部稍大饱满，建议复查，必要时增强检查 双肺粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前范围稍大 主动脉及冠脉钙化 右侧胸腔积液，部分包裹性积液，较前稍增多 甲状腺密度不均，请结合颈部检查 以上请结合临床及其它检查
---
放射(1)
报告时间↓ 项目
09-19 13:48 双肺CT（平扫）
报告号 8810332
原始报告 原始图像 申请单 对比报告 复制
开单科室 新区胸外科门诊 开单医
开单时间 2025-09-19 08:07
诊断 肺恶性肿瘤个人史
检查目的 体格检查：神志清，挂冲一
八泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。
日期 2025-09-19 13:48 检查科室
学影像科
检查项目
双肺CT（平扫）
检查描述
双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双
肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。
检查结论/诊断
双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双
肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。
右肺术后改变，术区团片影、索条影，较前2025.6.20片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前略减少、部分减
小 主动脉及冠脉钙化 右侧胸腔少量积液，较前稍增多 甲状腺密度不均，请结合颈部检查
---
报告时间↓ 项目
报告号 RMZZ_1001883808
原始报告 原始图像 申请单 对比报告 复
检验(5)
检查(3)
09-19 10:33 肝胆胰脾肾彩超
开单科室 新区胸外科门诊 开单医
龙
开单时间 2025-09-19 08:07
门诊病历
诊断 肺恶性肿瘤^\史
检查目的
清，精神可，手术切
，无红肿及脓性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。
门急诊病历(2)
报
报告日期 2025-09-19 10:33 检查科室 -
检查检验报告
实验室(2)
放射(1)
超声(1)
检查项目
肝胆胰脾肾彩超
检查描述
超声显示:肝脏大小、形态可，被膜光整，肝左叶探及一个无回声区，大小约10×6mm，形态规则，边界清，壁薄、光滑，内透声可；余实质回声尚均匀，肝内管道纹
理清晰，门静脉管腔通畅，血流信号未见明显异常。胆囊大小、形态正常，壁光滑，不厚，胆囊腔内透声清晰，未显示明确异常回声。超声切面图像可显示的胰腺大小、
形态正常，轮廓清，受胃肠气体干扰，超声切面图像可显示的部分胰腺实质回声尚未见明显异常，主胰管无扩张，胰周区域动静脉血管走行正常。CDFI：胰腺及周围未见
明显异常血流信号。脾脏大小、形态正常，被膜光滑，实质回声均匀，未见明显占位性病变，脾门部脾静脉内径正常。CDFI：脾动、静脉充盈良好，走行正常。双肾大
小、形态正常，双肾被膜轮廓规整，实质呈低回声，皮髓质界限清晰，双肾集合系统回声未见明显异常。CDFI：双肾血流灌注在正常范围。双侧肾上腺区肠气干扰明显，
可显示区域未探及明显异常回声包块。
检查结论/诊断
符合肝囊肿声像图。必要时结合临床或其他检查。
共1份
---
心电图检查报告单
检查时间：2025/6/20 9:39:04
女
心率：75bpm
P-R间期：138ms
诊断：窦性心律
性
SV1：0.71mV
QRS时限：95ms
大致正常心电图
年龄：68岁
RV5：1.26mV
QT/QTc：409/457ms
科室：新区胸外科门诊
RV5+SV1：1.97mV
电轴：7°
25mm/s 10mm/mV
(本报告仅供临床医师结合临床参考，不作诊断证明之用) 报告日期：2025/6/20 9
---
放射(1)
报告时间↓ 项目
06-20 14:53 双肺CT（平扫）
报告
原始报告 原始图像 申请单 对比报告 复制
开单科室 肺癌 门诊 开单医生
开单时间 2025-06-20 08:23
诊断 肺恶性肿瘤个人史
检查目的 体格检查 精神可，手术
炎性分泌物，双肺呼吸音清，无明显干湿啰音，腹软，无压痛及反跳痛。
报告日期 2025-06-20 14:53 检查科:
检查项目
双肺CT（平扫）
检查描述
双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。
检查结论/诊断
双侧胸廓对称，气管纵隔居中，右肺下叶术区局部见高密度缝合线及团片状软组织密度影、索条影，邻近胸膜增厚。双肺间质纹理增多。双肺见粟粒结节，边界清。双肺见条片状密度增高影。纵隔未见明显增大淋巴结。主动脉及冠脉见钙化影。右侧胸腔少量积液。甲状腺密度不均。
右肺术后改变，术区团片影、索条影，较前2025.4.4片无明显变化 双肺多发粟粒结节，较前相仿，建议随诊观察 双肺间质纹理增多 双肺条片影，较前稍增多、部分范围增大 主动脉及冠脉钙化 右侧胸腔少量积液 甲状腺密度不均，请结合颈部检查
共1份
---
临沂市人民医院
术中冰冻病理报告单
病理
姓
性别：女
年龄：67岁
收到日期：2024-06-19 14:28
送检医院：
送检科室
病
送检医生：5123
病
区.
床号：1-18床
冰冻诊断：
(右肺中叶)浸润性腺癌。
(脏层胸膜结节)查见腺癌。
(壁层胸膜结节)查见腺癌。
报告医生：
2024-06-19 14:54
---
影像学报告
检查号
姓名
性别：女
年龄：69岁
科
临床试验病房
病房：702643
病床：702643
住院号：7122764316
检查时间：2026-03-10 09:26 报告时间：2026-03-12 08:1
检查部位：[胸部,增强]
影像描述：
原诊“肺癌靶向治疗后进展”复查：
右肺局部术后，右肺下叶见条片状软组织影，局部结节影，强化欠均（
图7-37）。左肺上叶见条片影。纵隔见肿大淋巴结，图7-24示大者短径
约12mm。右侧叶间胸膜增厚，右侧胸膜多发结节样增厚，强化，右侧胸腔少
量积液。甲状腺局部示低密度影，强化不均匀。扫及左肾上腺略增粗。
影像诊断：
1、肺癌靶向治疗后进展复查，右肺下叶局部强化欠均，随诊或结合基线
片。
2、左肺上叶局部不张。
3、纵隔淋巴结肿大。
4、右侧胸膜增厚，考虑转移所致。右侧胸腔少量积液。
5、甲状腺结节，结合超声。
6、左肾上腺略增粗，建议随诊。
20240619手术
202407奥西，202602停的药
2026-08-10 19:28:47,450 INFO     29 [EMBED-PIPELINE] batch[32:48] text_for_embed=手术记录
年龄：67岁
病
手术日期：2024-06-19
手术时间：12:50~14:35
才
1.肺占位性病变2.腰椎间盘突出
术中诊断：
1.右肺中叶癌2.胸膜继发恶性肿瘤3.腰椎间盘突出
手术名称：胸腔镜右肺中叶切除+脏层胸膜结节切除+壁层胸膜结节切除+淋巴结切除术
麻醉方法：
全身麻醉
手术指导者：
手术经过、术中发现的情况及处理：
患者入室后，核查患者姓名、疾病名称、住院号、胸部CT姓名全部一致，患者平卧位行气管插管、全
身麻醉后，取左侧卧位，左侧胸壁下垫海绵垫，固定患者，调整手术床呈折刀位。标记手术切口。常规碘伏
消毒3遍，铺无菌巾，于右侧腋中线第5肋间切开皮肤约2.5cm，探查见右肺肺组织与胸壁无明显粘连，肿块
位于右肺中叶，大小约3*3cm，脏层胸膜皱缩，脏层胸膜及壁层胸膜可见多发黄白色粟粒状结节，未见明显
胸腔积液；用电钩游离出中叶动、静脉，用直线切割缝合器切断，清扫中叶支气管周围淋巴结后，夹闭支气
管，麻醉师吸痰胀肺，确认为右肺中叶支气管后将中叶支气管用直线切割缝合器切断，继续将右肺水平裂用
直线切割缝合器切断，将右肺中叶放入8号手套中，自胸腔内取出，于前纵隔壁层胸膜切除部分壁层胸膜结
节，使用一次性直线切割缝合器于下叶背段切除部分脏层胸膜结节，送快速病理，半小时后病理示：右肺中
叶浸润腺癌，脏层、壁层胸膜结节查见腺癌；遂用电刀行纵隔淋巴结采样，并充分止血，冲洗胸腔，麻醉师
吸痰胀肺，检查无漏血漏气后，于右侧胸壁切口处置入26号胸腔闭式引流管，接水封瓶，用可吸收线缝合腋
前线切口。手术程顺利，术中出血约20ml，未输血。病人清醒后拔除气管插管，安返病
10
58
26.0
188.8.155
激活Winc
转到"设置"以
记录时间：2024-06-19 14:44:23
2026-08-10 19:28:47,616 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 19:28:47,617 INFO     29 [Trace] task=dbb9d9e2 | doc=12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "33 items, types={'LabReport': 5, 'OutpatientRecord': 9, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 16, 'ProgressNote': 1}", "name": "12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf", "embedding_token_consumption": 13465}
2026-08-10 19:28:47,617 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 19:28:48,091 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 19:28:48,091 INFO     29 [Trace] task=dbb9d9e2 | doc=12-山肿-XXYI，后线肺癌，方穹招募推荐.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":33,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 19:28:48,104 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(16, 248, 292, 157, 166) row[-1]=(16, 248, 325, 210, 219)
2026-08-10 19:28:48,104 INFO     29 [DIAG-EXECUTOR] row_position_int len=23 row[0]=(17, 235, 254, 151, 160) row[-1]=(17, 235, 312, 523, 532)
2026-08-10 19:28:48,105 INFO     29 [DIAG-EXECUTOR] row_position_int len=27 row[0]=(18, 235, 253, 43, 52) row[-1]=(18, 235, 278, 484, 493)
2026-08-10 19:28:48,105 INFO     29 [DIAG-EXECUTOR] row_position_int len=24 row[0]=(19, 242, 275, 92, 102) row[-1]=(19, 242, 308, 484, 494)
2026-08-10 19:28:48,105 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(26, 307, 346, 151, 161) row[-1]=(26, 307, 376, 202, 211)
2026-08-10 19:28:48,105 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,105 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,105 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,105 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,106 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,106 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,106 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,106 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,106 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,106 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,106 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,106 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,107 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,107 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,107 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,107 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,107 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,107 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,107 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,108 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:28:48,119 INFO     29 set_progress(dbb9d9e294ee11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 19:28:48 [DOC Engine]:
Start to index...
2026-08-10 19:28:48,143 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.019s]
2026-08-10 19:28:48,146 INFO     29 set_progress(dbb9d9e294ee11f1bd9827cf206dfa2d), progress: 0.8030303030303031, progress_msg: 
2026-08-10 19:28:48,160 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:28:48,176 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 19:28:48,192 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 19:28:48,208 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:28:48,222 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:28:48,235 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:28:48,248 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.006s]
2026-08-10 19:28:48,256 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.005s]
2026-08-10 19:28:48,262 INFO     29 set_progress(dbb9d9e294ee11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 19:28:48 Indexing done (0.15s). Task done (1137.28s)
2026-08-10 19:28:48,265 INFO     29 [Done], chunks(33), token(13465), elapsed:1137.28
2026-08-10 19:28:48,780 INFO     29 handle_task done for task {"id": "dbb9d9e294ee11f1bd9827cf206dfa2d", "doc_id": "db844cb494ee11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "type": "pdf", "location": "12-\u5c71\u80bf-XXYI\uff0c\u540e\u7ebf\u80ba\u764c\uff0c\u65b9\u7a79\u62db\u52df\u63a8\u8350.pdf", "size": 14828427, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786388903475, "task_type": "dataflow", "root_trace_id": "9d9ed785184e435b9d8a5693cadbcf94", "root_traceparent": "00-9d9ed785184e435b9d8a5693cadbcf94-7ebd92d2185d496c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 19:29:05,399 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:29:05.397+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 91, "failed": 0, "current": {"14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:29:10,160 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:10,160 INFO     29 [qwen-vl-table] page=9 LLM output (len=4625):
{
  "report_date": "2026-03-18",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": null,
      "value": "6.58",
      "unit": "10^9/L",
      "reference_range": "4.00~10.00",
      "abnormal": false
    },
    {
      "name": "中性粒细胞%",
      "item_code": null,
      "value": "63.90",
      "unit": "%",
      "reference_range": "50.00~70.00",
      "abnormal": false
    },
    {
      "name": "淋巴细胞%",
      "item_code": null,
      "value": "25.60",
      "unit": "%",
      "reference_range": "20.00~40.00",
      "abnormal": false
    },
    {
      "name": "单核细胞%",
      "item_code": null,
      "value": "9.70",
      "unit": "%",
      "reference_range": "3.00~8.00",
      "abnormal": true
    },
    {
      "name": "嗜酸性粒细胞%",
      "item_code": null,
      "value": "0.50",
      "unit": "%",
      "reference_range": "0.00~5.00",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞%",
      "item_code": null,
      "value": "0.30",
      "unit": "%",
      "reference_range": "0.00~1.00",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对数",
      "item_code": null,
      "value": "4.21",
      "unit": "10^9/L",
      "reference_range": "1.50~7.00",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对数",
      "item_code": null,
      "value": "1.68",
      "unit": "10^9/L",
      "reference_range": "0.80~4.00",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对数",
      "item_code": null,
      "value": "0.64",
      "unit": "10^9/L",
      "reference_range": "0.12~0.80",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞绝对数",
      "item_code": null,
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0.00~0.50",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对数",
      "item_code": null,
      "value": "0.02",
      "unit": "10^9/L",
      "reference_range": "0.00~0.10",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": null,
      "value": "4.55",
      "unit": "10^12/L",
      "reference_range": "3.50~6.00",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": null,
      "value": "131.0",
      "unit": "g/L",
      "reference_range": "120.0~165.0",
      "abnormal": false
    },
    {
      "name": "红细胞比积",
      "item_code": null,
      "value": "39.7",
      "unit": "%",
      "reference_range": "40.0~50.0",
      "abnormal": true
    },
    {
      "name": "平均红细胞体积",
      "item_code": null,
      "value": "87.2",
      "unit": "f1",
      "reference_range": "80.0~100.0",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白含量",
      "item_code": null,
      "value": "28.7",
      "unit": "pg",
      "reference_range": "27.3~34.4",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": null,
      "value": "330.0",
      "unit": "g/L",
      "reference_range": "320.0~360.0",
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度-CV",
      "item_code": null,
      "value": "13.4",
      "unit": "%",
      "reference_range": "11.0~16.0",
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度-SD",
      "item_code": null,
      "value": "43.7",
      "unit": "f1",
      "reference_range": "37.0~54.0",
      "abnormal": false
    },
    {
      "name": "有核红细胞绝对计数",
      "item_code": null,
      "value": "0.00",
      "unit": "10^9/L",
      "reference_range": "0.00~0.02",
      "abnormal": false
    },
    {
      "name": "有核红细胞/白细胞",
      "item_code": null,
      "value": "0.00",
      "unit": "%",
      "reference_range": "<1.00",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": null,
      "value": "378",
      "unit": "10^9/L",
      "reference_range": "100~300",
      "abnormal": true
    },
    {
      "name": "血小板比容",
      "item_code": null,
      "value": "0.37",
      "unit": "%",
      "reference_range": "0.06~0.28",
      "abnormal": true
    },
    {
      "name": "平均血小板体积",
      "item_code": null,
      "value": "9.9",
      "unit": "f1",
      "reference_range": "6.4~12.1",
      "abnormal": false
    },
    {
      "name": "血小板体积分布宽度",
      "item_code": null,
      "value": "16.5",
      "unit": "%",
      "reference_range": "9.0~17.0",
      "abnormal": false
    },
    {
      "name": "大血小板比率",
      "item_code": null,
      "value": "24.80",
      "unit": "%",
      "reference_range": "13.00~43.00",
      "abnormal": false
    },
    {
      "name": "C-反应蛋白",
      "item_code": null,
      "value": "97.64",
      "unit": "mg/L",
      "reference_range": "0~8.00",
      "abnormal": true
    }
  ]
}
2026-08-10 19:29:10,160 INFO     29 [qwen-vl-table] coord grouping: {9: 27}
2026-08-10 19:29:10,163 INFO     29 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1657572, prompt_len=731
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、中性粒细胞%、淋巴细胞%、单核细胞%、嗜酸性粒细胞%、嗜碱性粒细胞%、中性粒细胞绝对数、淋巴细胞绝对数、单核细胞绝对数、嗜酸性粒细胞绝对数、嗜碱性粒细胞绝对数、红细胞计数、血红蛋白、红细胞比积、平均红细胞体积、平均红细胞血红蛋白含量、平均红细胞血红蛋白浓度、红细胞体积分布宽度-CV、红细胞体积分布宽度-SD、有核红细胞绝对计数、有核红细胞/白细胞、血小板计数、血小板比容、平均血小板体积、血小板体积分布宽度、大血小板比率、C-反应蛋白

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
2026-08-10 19:29:17,617 INFO     29 [qwen-vl-table] coord API raw response (len=1398):
[
	{"text": "白细胞计数", "bbox": [94, 170, 198, 192]},
	{"text": "中性粒细胞%", "bbox": [94, 195, 191, 216]},
	{"text": "淋巴细胞%", "bbox": [94, 218, 175, 239]},
	{"text": "单核细胞%", "bbox": [94, 242, 175, 263]},
	{"text": "嗜酸性粒细胞%", "bbox": [94, 265, 205, 286]},
	{"text": "嗜碱性粒细胞%", "bbox": [94, 289, 205, 310]},
	{"text": "中性粒细胞绝对数", "bbox": [94, 312, 228, 333]},
	{"text": "淋巴细胞绝对数", "bbox": [94, 336, 212, 357]},
	{"text": "单核细胞绝对数", "bbox": [94, 359, 212, 380]},
	{"text": "嗜酸性粒细胞绝对数", "bbox": [94, 382, 243, 403]},
	{"text": "嗜碱性粒细胞绝对数", "bbox": [94, 406, 243, 427]},
	{"text": "红细胞计数", "bbox": [94, 429, 198, 450]},
	{"text": "血红蛋白", "bbox": [94, 453, 183, 474]},
	{"text": "红细胞比积", "bbox": [94, 476, 198, 497]},
	{"text": "平均红细胞体积", "bbox": [94, 500, 228, 521]},
	{"text": "平均红细胞血红蛋白含量", "bbox": [94, 523, 285, 544]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [94, 547, 313, 568]},
	{"text": "红细胞体积分布宽度-CV", "bbox": [502, 170, 675, 192]},
	{"text": "红细胞体积分布宽度-SD", "bbox": [502, 195, 675, 216]},
	{"text": "有核红细胞绝对计数", "bbox": [502, 218, 652, 239]},
	{"text": "有核红细胞/白细胞", "bbox": [502, 242, 644, 263]},
	{"text": "血小板计数", "bbox": [502, 265, 607, 286]},
	{"text": "血小板比容", "bbox": [502, 289, 591, 310]},
	{"text": "平均血小板体积", "bbox": [502, 312, 621, 333]},
	{"text": "血小板体积分布宽度", "bbox": [502, 336, 652, 357]},
	{"text": "大血小板比率", "bbox": [502, 359, 607, 380]},
	{"text": "C-反应蛋白", "bbox": [502, 382, 591, 403]}
]
2026-08-10 19:29:17,618 INFO     29 [qwen-vl-table] coord API: raw_items=27, valid_items=27, elapsed=7.5s
2026-08-10 19:29:17,618 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[94, 170, 198, 192]
2026-08-10 19:29:17,618 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞%, bbox=[94, 195, 191, 216]
2026-08-10 19:29:17,618 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞%, bbox=[94, 218, 175, 239]
2026-08-10 19:29:17,619 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞%, bbox=[94, 242, 175, 263]
2026-08-10 19:29:17,619 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞%, bbox=[94, 265, 205, 286]
2026-08-10 19:29:17,619 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞%, bbox=[94, 289, 205, 310]
2026-08-10 19:29:17,619 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞绝对数, bbox=[94, 312, 228, 333]
2026-08-10 19:29:17,619 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞绝对数, bbox=[94, 336, 212, 357]
2026-08-10 19:29:17,620 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞绝对数, bbox=[94, 359, 212, 380]
2026-08-10 19:29:17,620 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞绝对数, bbox=[94, 382, 243, 403]
2026-08-10 19:29:17,620 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞绝对数, bbox=[94, 406, 243, 427]
2026-08-10 19:29:17,620 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞计数, bbox=[94, 429, 198, 450]
2026-08-10 19:29:17,620 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[94, 453, 183, 474]
2026-08-10 19:29:17,620 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞比积, bbox=[94, 476, 198, 497]
2026-08-10 19:29:17,620 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积, bbox=[94, 500, 228, 521]
2026-08-10 19:29:17,620 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞血红蛋白含量, bbox=[94, 523, 285, 544]
2026-08-10 19:29:17,621 INFO     29 [qwen-vl-table] coord item[16]: text=平均红细胞血红蛋白浓度, bbox=[94, 547, 313, 568]
2026-08-10 19:29:17,621 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞体积分布宽度-CV, bbox=[502, 170, 675, 192]
2026-08-10 19:29:17,621 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞体积分布宽度-SD, bbox=[502, 195, 675, 216]
2026-08-10 19:29:17,621 INFO     29 [qwen-vl-table] coord item[19]: text=有核红细胞绝对计数, bbox=[502, 218, 652, 239]
2026-08-10 19:29:17,621 INFO     29 [qwen-vl-table] coord item[20]: text=有核红细胞/白细胞, bbox=[502, 242, 644, 263]
2026-08-10 19:29:17,622 INFO     29 [qwen-vl-table] coord item[21]: text=血小板计数, bbox=[502, 265, 607, 286]
2026-08-10 19:29:17,622 INFO     29 [qwen-vl-table] coord item[22]: text=血小板比容, bbox=[502, 289, 591, 310]
2026-08-10 19:29:17,622 INFO     29 [qwen-vl-table] coord item[23]: text=平均血小板体积, bbox=[502, 312, 621, 333]
2026-08-10 19:29:17,622 INFO     29 [qwen-vl-table] coord item[24]: text=血小板体积分布宽度, bbox=[502, 336, 652, 357]
2026-08-10 19:29:17,622 INFO     29 [qwen-vl-table] coord item[25]: text=大血小板比率, bbox=[502, 359, 607, 380]
2026-08-10 19:29:17,622 INFO     29 [qwen-vl-table] coord item[26]: text=C-反应蛋白, bbox=[502, 382, 591, 403]
2026-08-10 19:29:17,623 INFO     29 [qwen-vl-table] page=9 coord: matched 27/27, time=7.5s
2026-08-10 19:29:17,623 INFO     29 [qwen-vl-table] new_positions (27):
[[10, 79.148, 166.716, 101.14999999999999, 114.24], [10, 79.148, 160.822, 116.02499999999999, 128.51999999999998], [10, 79.148, 147.35, 129.71, 142.20499999999998], [10, 79.148, 147.35, 143.98999999999998, 156.48499999999999], [10, 79.148, 172.60999999999999, 157.67499999999998, 170.17], [10, 79.148, 172.60999999999999, 171.95499999999998, 184.45], [10, 79.148, 191.976, 185.64, 198.135], [10, 79.148, 178.504, 199.92, 212.415], [10, 79.148, 178.504, 213.605, 226.1], [10, 79.148, 204.606, 227.29, 239.785], [10, 79.148, 204.606, 241.57, 254.065], [10, 79.148, 166.716, 255.255, 267.75], [10, 79.148, 154.08599999999998, 269.53499999999997, 282.03], [10, 79.148, 166.716, 283.21999999999997, 295.715], [10, 79.148, 191.976, 297.5, 309.995], [10, 79.148, 239.97, 311.185, 323.68], [10, 79.148, 263.546, 325.465, 337.96], [10, 422.68399999999997, 568.35, 101.14999999999999, 114.24], [10, 422.68399999999997, 568.35, 116.02499999999999, 128.51999999999998], [10, 422.68399999999997, 548.984, 129.71, 142.20499999999998], [10, 422.68399999999997, 542.2479999999999, 143.98999999999998, 156.48499999999999], [10, 422.68399999999997, 511.094, 157.67499999999998, 170.17], [10, 422.68399999999997, 497.62199999999996, 171.95499999999998, 184.45], [10, 422.68399999999997, 522.882, 185.64, 198.135], [10, 422.68399999999997, 548.984, 199.92, 212.415], [10, 422.68399999999997, 511.094, 213.605, 226.1], [10, 422.68399999999997, 497.62199999999996, 227.29, 239.785]]
2026-08-10 19:29:17,623 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=27, matched=27, pages=1, time=44.8s
2026-08-10 19:29:17,624 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:29:17,625 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:29:17,625 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[10]
2026-08-10 19:29:17,625 INFO     29 [qwen-vl-table] positions ： [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:29:17,803 INFO     29 [qwen-vl-table] page=10, rect=842x595, img=(2339x1653)
2026-08-10 19:29:17,803 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:17,804 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 403, \"bbox_end\": 426, \"encounter_dates\": [\"2026-03-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c c}\n报告时间: 2026-03-18\n\\hline\n\\textbf{检验项目} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考区间} & \\textbf{单位} \\\\\n\\hline\n1 ★凝血酶原时间(PT) & 14.8 & & 11.0$\\sim$15.0 & 秒 \\\\\n2 国际标准化比值(INR) & 1.18 & & & \\\\\n3 凝血酶原活动度 & 76.0 & & 70.0$\\sim$150.0 & \\% \\\\\n4 ★活化部分凝血活酶时间(APTT) & 44.8 & $\\uparrow$ & 28.0$\\sim$42.0 & 秒 \\\\\n5 活化部分凝血活酶时间比值 & 1.32 & & & \\\\\n6 ★纤维蛋白原(FIB) & 9.79 & $\\uparrow$ & 2.00$\\sim$4.00 & g/L \\\\\n7 ★凝血酶时间(TT) & 19.8 & & 14.0$\\sim$21.0 & 秒 \\\\\n8 ★D-二聚体(D-DI) & 7.28 & $\\uparrow$ & 0.00$\\sim$0.50 & ug/ml \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{l l l l l l}\n报告时间: 2026-03-18\n\\hline\n\\multicolumn{2}{l}{申请时间 2026-03-16 10:33} & \\multicolumn{4}{l}{采样者 杨美满} \\\\\n\\multicolumn{2}{l}{采样时间 2026-03-18 08:30} & \\multicolumn{4}{l}{审核时间 2026-03-18 12:52} \\\\\n\\multicolumn{2}{l}{打印时间} & \\multicolumn{2}{l}{接收者 赵俊} & \\multicolumn{2}{l}{检验者 刘} \\\\\n\\multicolumn{6}{l}{带“★”者为省医疗单位互认项目。} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:29:27,843 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:27,843 INFO     29 [qwen-vl-table] page=10 LLM output (len=1385):
{
  "report_date": "2026-03-18",
  "items": [
    {
      "name": "凝血酶原时间",
      "item_code": "PT",
      "value": "14.8",
      "unit": "秒",
      "reference_range": "11.0~15.0",
      "abnormal": false
    },
    {
      "name": "国际标准化比值",
      "item_code": "INR",
      "value": "1.18",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "凝血酶原活动度",
      "item_code": null,
      "value": "76.0",
      "unit": "%",
      "reference_range": "70.0~150.0",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间",
      "item_code": "APTT",
      "value": "44.8",
      "unit": "秒",
      "reference_range": "28.0~42.0",
      "abnormal": true
    },
    {
      "name": "活化部分凝血活酶时间比值",
      "item_code": null,
      "value": "1.32",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "纤维蛋白原",
      "item_code": "FIB",
      "value": "9.79",
      "unit": "g/L",
      "reference_range": "2.00~4.00",
      "abnormal": true
    },
    {
      "name": "凝血酶时间",
      "item_code": "TT",
      "value": "19.8",
      "unit": "秒",
      "reference_range": "14.0~21.0",
      "abnormal": false
    },
    {
      "name": "D-二聚体",
      "item_code": "D-DI",
      "value": "7.28",
      "unit": "ug/ml",
      "reference_range": "0.00~0.50",
      "abnormal": true
    }
  ]
}
2026-08-10 19:29:27,843 INFO     29 [qwen-vl-table] coord grouping: {10: 8}
2026-08-10 19:29:27,845 INFO     29 [qwen-vl-table] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1044736, prompt_len=571
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间、国际标准化比值、凝血酶原活动度、活化部分凝血活酶时间、活化部分凝血活酶时间比值、纤维蛋白原、凝血酶时间、D-二聚体

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
2026-08-10 19:29:31,040 INFO     29 [qwen-vl-table] coord API raw response (len=431):
```json
[
	{"text": "凝血酶原时间", "bbox": [100, 138, 234, 163]},
	{"text": "国际标准化比值", "bbox": [100, 167, 241, 192]},
	{"text": "凝血酶原活动度", "bbox": [100, 196, 204, 221]},
	{"text": "活化部分凝血活酶时间", "bbox": [100, 225, 314, 250]},
	{"text": "活化部分凝血活酶时间比值", "bbox": [100, 255, 285, 280]},
	{"text": "纤维蛋白原", "bbox": [100, 285, 225, 310]},
	{"text": "凝血酶时间", "bbox": [100, 314, 218, 339]},
	{"text": "D-二聚体", "bbox": [100, 344, 229, 369]}
]
```
2026-08-10 19:29:31,040 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=3.2s
2026-08-10 19:29:31,040 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[100, 138, 234, 163]
2026-08-10 19:29:31,040 INFO     29 [qwen-vl-table] coord item[1]: text=国际标准化比值, bbox=[100, 167, 241, 192]
2026-08-10 19:29:31,040 INFO     29 [qwen-vl-table] coord item[2]: text=凝血酶原活动度, bbox=[100, 196, 204, 221]
2026-08-10 19:29:31,040 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间, bbox=[100, 225, 314, 250]
2026-08-10 19:29:31,040 INFO     29 [qwen-vl-table] coord item[4]: text=活化部分凝血活酶时间比值, bbox=[100, 255, 285, 280]
2026-08-10 19:29:31,041 INFO     29 [qwen-vl-table] coord item[5]: text=纤维蛋白原, bbox=[100, 285, 225, 310]
2026-08-10 19:29:31,041 INFO     29 [qwen-vl-table] coord item[6]: text=凝血酶时间, bbox=[100, 314, 218, 339]
2026-08-10 19:29:31,041 INFO     29 [qwen-vl-table] coord item[7]: text=D-二聚体, bbox=[100, 344, 229, 369]
2026-08-10 19:29:31,041 INFO     29 [qwen-vl-table] page=10 coord: matched 8/8, time=3.2s
2026-08-10 19:29:31,041 INFO     29 [qwen-vl-table] new_positions (8):
[[11, 84.2, 197.028, 82.11, 96.985], [11, 84.2, 202.922, 99.365, 114.24], [11, 84.2, 171.768, 116.61999999999999, 131.495], [11, 84.2, 264.388, 133.875, 148.75], [11, 84.2, 239.97, 151.725, 166.6], [11, 84.2, 189.45, 169.575, 184.45], [11, 84.2, 183.55599999999998, 186.82999999999998, 201.70499999999998], [11, 84.2, 192.81799999999998, 204.67999999999998, 219.55499999999998]]
2026-08-10 19:29:31,041 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=8, matched=8, pages=1, time=13.4s
2026-08-10 19:29:31,050 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 19:29:31,050 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:LabExam | outputs={"chunks": "5 items, types={'LabReport': 5}", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:29:31,050 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 19:29:31,055 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:31,055 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:29:32,545 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:32,554 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 19:29:32,555 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:29:32,555 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 19:29:32,561 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:32,561 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:29:33,214 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:33,218 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 19:29:33,218 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:29:33,218 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 19:29:33,222 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:33,223 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:29:36,764 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:36,773 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 19:29:36,773 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:29:36,773 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 19:29:36,778 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:36,779 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:29:37,431 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:37,444 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 19:29:37,444 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:29:37,444 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 19:29:37,454 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:37,455 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:29:37,695 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:29:37.694+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 91, "failed": 0, "current": {"14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:29:38,124 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:38,134 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 19:29:38,135 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:29:38,135 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 19:29:38,145 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:29:38,146 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:29:38,146 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 19:29:38,146 INFO     29 [qwen-vl-text] positions(81): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:29:38,147 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2], lines per page: [38, 30, 13]
2026-08-10 19:29:38,390 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:29:38,628 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:29:38,818 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:29:38,819 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2092
2026-08-10 19:29:38,820 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:29:38,820 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 80, \"encounter_dates\": [\"2026-03-16\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "姓名\n住址：福建省三明市尤溪县\n性别：男\n工作单位：/\n年龄：49岁\n入院日期：2026.03.16 10:21:29\n婚姻：已婚\n记录时间：2026.03.16 10:21:29\n民族：汉族\n病史陈述者：患者及家属\n出生地：福建省三明市\n病史可靠程度：基本可靠\n职业(工种)：/\n过敏史：未发现\n主诉：确诊左下肺鳞癌4天。\n现病史：缘于2026.03.05以“咳嗽、咳痰1月”就诊于尤溪县总医院，查“2026.03.06胸部\n增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。”\n于2026.03.09行“支气管镜检查+支气管粘膜活检术”，术顺，术后病理示：（左肺下叶粘\n膜组织）浸润性鳞状细胞癌。\n予抗感染、止咳、化痰后咳嗽、咳痰好转，\n无头晕、头痛，无胸闷、胸痛，无畏冷、发热，无心悸、呼吸困难，无乏力、盗汗，无腹胀、腹痛，\n无恶心、呕吐，无声音嘶哑、吞咽困难等不适。今为进一步诊治就诊我科，门诊拟“左下肺腺\n癌”收治入院，自发病以来，精神、食欲、睡眠尚可，大、小便正常，体重近期未见明显增减。\n既往史：平素身体健康，否认高血压，否认糖尿病，否认冠心病，否认肝炎、结核、菌痢、伤寒\n等传染病史，否认其他手术史，否认输血史，否认外伤史，否认药物过敏史，预防接种按时完成。\n个人史：生于原籍，否认长期外地居住史，否认疫区居留史，否认特殊化学品及放射线接触\n史。有吸烟史20余年，否认饮酒。否认冶游史。\n婚育史：已婚已育，配偶及孩子均体健。\n家族史：父已故，母健在。其父有肺癌史。否认家族中有“肝炎、伤寒、结核”等传染病史，否\n认家族中有其他遗传性疾病史。\n体格检查\nT:36.5℃\nP:79次/分\nR:19次/分\nBP:112/69mmHg\n一般情况：神志清楚，发育正常，营养良好，体型正常，正常面容，表情安静，自动体位，查\n体合作，对答切题，步行入院。\n第1页\n皮肤粘膜：色泽正常，未见黄染，未见紫绀，未见色素沉着，未见皮疹，未见皮下出血。皮温\n正常，湿度正常，弹性好，无水肿，未见肝掌，未见蜘蛛痣。\n淋巴结：全身浅表淋巴结未触及。\n头颅：大小正常，形状正常，头发分布正常，眼睑无浮肿，眼球无异常，巩膜无黄染，结膜正\n常，角膜透明，瞳孔等大等圆，直径3mm，对光反射灵敏。耳廓无畸形，外耳道正常，无异常分泌\n物，听力正常，无乳突压痛。双侧鼻唇沟对称，鼻中隔无偏曲，鼻腔通气畅，无副鼻窦区压痛。口\n唇无紫绀，口腔粘膜完整，口腔无异味，伸舌居中，咽无充血，扁桃体无肿大，无脓点。\n颈部：颈柔软，颈静脉无怒张，肝颈静脉回流征阴性，未见颈动脉异常搏动，气管居中，甲\n状腺无肿大，无血管杂音。\n胸部：胸廓无畸形，胸壁静脉未见，无皮下气肿，肋间隙正常。胸骨无压痛，胸廓挤压征阴\n性，无男乳女化。\n肺部：双侧呼吸运动匀称，双侧触觉语颤对称，叩诊音清，呼吸音清，未闻及干湿罗音，未\n闻及胸膜摩擦音。\n心脏：无心前区隆起，心尖搏动正常，位于第Ⅴ肋间，左锁骨中线内0.5cm处，未扪及震颤\n及抬举样搏动，心界叩诊无扩大，心音清晰，心率79次/分，节律整齐，A2>P2，无杂音。心浊音界\n大小如下图所示：\n右(CM) 肋间 左(CM)\n2 Ⅱ 2\n2 Ⅲ 3.5\n3 Ⅳ 5.5\nⅤ 8.0\n注：左锁骨中线距前正中线8.5CM。\n周围血管：脉率79次/分，节律整齐，无脉搏短绌，无奇脉，无交替脉，无毛细血管搏动征，\n无Duroziez二重杂音，无大血管枪击音，无水冲脉。双侧足背动脉及桡动脉搏动良好对称。\n腹部：腹平坦，呼吸运动自如，腹壁静脉未见怒张，腹壁皮肤无皮疹，无色素沉着，无腹纹，\n无疤痕，无疝，未见胃肠型及蠕动波，无上腹部搏动。全腹软，无肌紧张，无压痛及反跳痛，未触\n及包块，肝脏右肋下、剑突下未触及，胆囊未触及，莫菲氏征阴性，脾脏左肋下未触及，双肾未触\n及，双侧输尿管径路无压痛，无液波震颤。鼓音，肝上界位于右锁骨中线上第Ⅳ肋间，肝区无叩\n击痛，胃泡鼓音区存在，肾区无叩痛，移动性浊音阴性。肠鸣音正常，4次/分，未闻及振水音及血\n第2页\n管杂音。\n肛门生殖器：肛门及外生殖器未见异常。\n脊柱四肢：脊柱生理弯曲正常，活动度正常，脊柱无压痛，无叩击痛；各关节四肢形态正常。肢体无浮肿，无静脉曲张，无色素沉着，无溃疡。\n神经系统：四肢肌力正常，肌张力正常，角膜反射、腹壁反射、肱二头肌、肱三头肌、桡反射、膝反射、跟腱反射正常，巴彬斯基征未引出，脑膜刺激征阴性。\n专科情况\n生命征平稳，神志清楚，浅表淋巴结未触及淋巴结肿大。胸廓对称无畸形，胸壁未见静脉曲张，双肺触觉语颤对称，双肺叩诊呈清音，双肺呼吸音清，未闻及明显干湿性啰音及摩擦音。心前区无隆起，心脏触诊未及震颤，心界叩诊无扩大，心律齐，各瓣音区心音正常，未闻及病理性杂音。腹平软。未见胃肠型及蠕动波，肝脏肋下未触及，无压痛及反跳痛。双下肢无浮肿。\n辅助检查\n出院诊断：\n医生签名：\n初步诊断：肺结节性质待查：\n肺癌？\n炎性假瘤？\n医生签名：",
    "role": "user"
  }
]
2026-08-10 19:30:09,983 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:30:09.980+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 91, "failed": 0, "current": {"14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:30:11,983 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:30:11,983 INFO     29 [qwen-vl-text] LLM output (len=3004):
{
  "encounter_date": "2026-03-16",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": 49,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "/",
  "dm_admission_time": "2026-03-16 10:21",
  "dm_record_time": "2026-03-16 10:21",
  "dm_history_provider": "患者及家属",
  "cc_text": "确诊左下肺鳞癌4天。",
  "cc_main_symptoms": [
    "确诊左下肺鳞癌"
  ],
  "cc_duration": "4天",
  "pi_text": "缘于2026.03.05以“咳嗽、咳痰1月”就诊于尤溪县总医院，查“2026.03.06胸部增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。”于2026.03.09行“支气管镜检查+支气管粘膜活检术”，术顺，术后病理示：（左肺下叶粘膜组织）浸润性鳞状细胞癌。予抗感染、止咳、化痰后咳嗽、咳痰好转，无头晕、头痛，无胸闷、胸痛，无畏冷、发热，无心悸、呼吸困难，无乏力、盗汗，无腹胀、腹痛，无恶心、呕吐，无声音嘶哑、吞咽困难等不适。今为进一步诊治就诊我科，门诊拟“左下肺腺癌”收治入院，自发病以来，精神、食欲、睡眠尚可，大、小便正常，体重近期未见明显增减。",
  "pmh_disease_history": [
    "平素身体健康",
    "否认高血压",
    "否认糖尿病",
    "否认冠心病",
    "否认肝炎、结核、菌痢、伤寒等传染病史"
  ],
  "pmh_allergy_history": [
    "未发现",
    "否认药物过敏史"
  ],
  "pmh_surgery_trauma_history": [
    "否认其他手术史",
    "否认输血史",
    "否认外伤史"
  ],
  "ph_smoking": "有吸烟史20余年",
  "ph_drinking": "否认饮酒",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "父已故，母健在。其父有肺癌史。否认家族中有“肝炎、伤寒、结核”等传染病史，否认家族中有其他遗传性疾病史。",
  "fh_hereditary_diseases": [
    "肺癌"
  ],
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 79,
  "vs_respiration_rpm": 19,
  "vs_systolic_bp_mmhg": 112,
  "vs_diastolic_bp_mmhg": 69,
  "pe_general_condition": "神志清楚，发育正常，营养良好，体型正常，正常面容，表情安静，自动体位，查体合作，对答切题，步行入院。",
  "pe_skin_mucosa": "色泽正常，未见黄染，未见紫绀，未见色素沉着，未见皮疹，未见皮下出血。皮温正常，湿度正常，弹性好，无水肿，未见肝掌，未见蜘蛛痣。",
  "pe_lymph_nodes": "全身浅表淋巴结未触及。",
  "pe_lungs": "双侧呼吸运动匀称，双侧触觉语颤对称，叩诊音清，呼吸音清，未闻及干湿罗音，未闻及胸膜摩擦音。",
  "pe_heart": "无心前区隆起，心尖搏动正常，位于第Ⅴ肋间，左锁骨中线内0.5cm处，未扪及震颤及抬举样搏动，心界叩诊无扩大，心音清晰，心率79次/分，节律整齐，A2>P2，无杂音。",
  "pe_abdomen": "腹平坦，呼吸运动自如，腹壁静脉未见怒张，腹壁皮肤无皮疹，无色素沉着，无腹纹，无疤痕，无疝，未见胃肠型及蠕动波，无上腹部搏动。全腹软，无肌紧张，无压痛及反跳痛，未触及包块，肝脏右肋下、剑突下未触及，胆囊未触及，莫菲氏征阴性，脾脏左肋下未触及，双肾未触及，双侧输尿管径路无压痛，无液波震颤。鼓音，肝上界位于右锁骨中线上第Ⅳ肋间，肝区无叩击痛，胃泡鼓音区存在，肾区无叩痛，移动性浊音阴性。肠鸣音正常，4次/分，未闻及振水音及血管杂音。",
  "pe_extremities": "脊柱生理弯曲正常，活动度正常，脊柱无压痛，无叩击痛；各关节四肢形态正常。肢体无浮肿，无静脉曲张，无色素沉着，无溃疡。",
  "pe_nervous_system": "四肢肌力正常，肌张力正常，角膜反射、腹壁反射、肱二头肌、肱三头肌、桡反射、膝反射、跟腱反射正常，巴彬斯基征未引出，脑膜刺激征阴性。",
  "pe_specialist_exam": "生命征平稳，神志清楚，浅表淋巴结未触及淋巴结肿大。胸廓对称无畸形，胸壁未见静脉曲张，双肺触觉语颤对称，双肺叩诊呈清音，双肺呼吸音清，未闻及明显干湿性啰音及摩擦音。心前区无隆起，心脏触诊未及震颤，心界叩诊无扩大，心律齐，各瓣音区心音正常，未闻及病理性杂音。腹平软。未见胃肠型及蠕动波，肝脏肋下未触及，无压痛及反跳痛。双下肢无浮肿。",
  "pe_ecog_score": null,
  "pat_text": "2026.03.06胸部增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。2026.03.09支气管镜检查+支气管粘膜活检术，术后病理示：（左肺下叶粘膜组织）浸润性鳞状细胞癌。",
  "pat_items": [
    "2026.03.06胸部增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm",
    "2026.03.09支气管镜检查+支气管粘膜活检术，术后病理示：（左肺下叶粘膜组织）浸润性鳞状细胞癌"
  ],
  "preliminary_diagnoses": [
    {
      "name": "肺结节性质待查",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "肺癌？",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "炎性假瘤？",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 19:30:11,983 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-16]
2026-08-10 19:30:11,987 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1169941, prompt_len=1560
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["姓名", "住址：福建省三明市尤溪县", "性别：男", "工作单位：/", "年龄：49岁", "入院日期：2026.03.16 10:21:29", "婚姻：已婚", "记录时间：2026.03.16 10:21:29", "民族：汉族", "病史陈述者：患者及家属", "出生地：福建省三明市", "病史可靠程度：基本可靠", "职业(工种)：/", "过敏史：未发现", "主诉：确诊左下肺鳞癌4天。", "现病史：缘于2026.03.05以“咳嗽、咳痰1月”就诊于尤溪县总医院，查“2026.03.06胸部", "增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。”", "于2026.03.09行“支气管镜检查+支气管粘膜活检术”，术顺，术后病理示：（左肺下叶粘", "膜组织）浸润性鳞状细胞癌。", "予抗感染、止咳、化痰后咳嗽、咳痰好转，", "无头晕、头痛，无胸闷、胸痛，无畏冷、发热，无心悸、呼吸困难，无乏力、盗汗，无腹胀、腹痛，", "无恶心、呕吐，无声音嘶哑、吞咽困难等不适。今为进一步诊治就诊我科，门诊拟“左下肺腺", "癌”收治入院，自发病以来，精神、食欲、睡眠尚可，大、小便正常，体重近期未见明显增减。", "既往史：平素身体健康，否认高血压，否认糖尿病，否认冠心病，否认肝炎、结核、菌痢、伤寒", "等传染病史，否认其他手术史，否认输血史，否认外伤史，否认药物过敏史，预防接种按时完成。", "个人史：生于原籍，否认长期外地居住史，否认疫区居留史，否认特殊化学品及放射线接触", "史。有吸烟史20余年，否认饮酒。否认冶游史。", "婚育史：已婚已育，配偶及孩子均体健。", "家族史：父已故，母健在。其父有肺癌史。否认家族中有“肝炎、伤寒、结核”等传染病史，否", "认家族中有其他遗传性疾病史。", "体格检查", "T:36.5℃", "P:79次/分", "R:19次/分", "BP:112/69mmHg", "一般情况：神志清楚，发育正常，营养良好，体型正常，正常面容，表情安静，自动体位，查", "体合作，对答切题，步行入院。", "第1页"]

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
2026-08-10 19:30:25,190 INFO     29 [qwen-vl-text] coord API raw response (len=2495):
[
	{"text": "姓名", "bbox": [109, 105, 150, 120]},
	{"text": "住址：福建省三明市尤溪县", "bbox": [405, 104, 648, 120]},
	{"text": "性别：男", "bbox": [109, 131, 190, 147]},
	{"text": "工作单位：/", "bbox": [405, 131, 539, 147]},
	{"text": "年龄：49岁", "bbox": [109, 158, 209, 173]},
	{"text": "入院日期：2026.03.16 10:21:29", "bbox": [405, 158, 700, 173]},
	{"text": "婚姻：已婚", "bbox": [109, 184, 210, 200]},
	{"text": "记录时间：2026.03.16 10:21:29", "bbox": [405, 184, 700, 200]},
	{"text": "民族：汉族", "bbox": [109, 210, 210, 226]},
	{"text": "病史陈述者：患者及家属", "bbox": [405, 210, 626, 226]},
	{"text": "出生地：福建省三明市", "bbox": [109, 237, 314, 252]},
	{"text": "病史可靠程度：基本可靠", "bbox": [405, 237, 626, 252]},
	{"text": "职业(工种)：/", "bbox": [109, 263, 244, 278]},
	{"text": "过敏史：未发现", "bbox": [405, 263, 547, 278]},
	{"text": "主诉：确诊左下肺鳞癌4天。", "bbox": [113, 291, 360, 307]},
	{"text": "现病史：缘于2026.03.05以“咳嗽、咳痰1月”就诊于尤溪县总医院，查“2026.03.06胸部", "bbox": [85, 314, 899, 330]},
	{"text": "增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。”", "bbox": [85, 338, 898, 375]},
	{"text": "于2026.03.09行“支气管镜检查+支气管粘膜活检术”，术顺，术后病理示：（左肺下叶粘", "bbox": [85, 384, 900, 400]},
	{"text": "膜组织）浸润性鳞状细胞癌。", "bbox": [85, 408, 344, 424]},
	{"text": "予抗感染、止咳、化痰后咳嗽、咳痰好转，", "bbox": [114, 432, 460, 448]},
	{"text": "无头晕、头痛，无胸闷、胸痛，无畏冷、发热，无心悸、呼吸困难，无乏力、盗汗，无腹胀、腹痛，", "bbox": [85, 456, 898, 472]},
	{"text": "无恶心、呕吐，无声音嘶哑、吞咽困难等不适。今为进一步诊治就诊我科，门诊拟“左下肺腺", "bbox": [85, 479, 899, 496]},
	{"text": "癌”收治入院，自发病以来，精神、食欲、睡眠尚可，大、小便正常，体重近期未见明显增减。", "bbox": [85, 503, 858, 519]},
	{"text": "既往史：平素身体健康，否认高血压，否认糖尿病，否认冠心病，否认肝炎、结核、菌痢、伤寒", "bbox": [85, 526, 902, 543]},
	{"text": "等传染病史，否认其他手术史，否认输血史，否认外伤史，否认药物过敏史，预防接种按时完成。", "bbox": [85, 550, 900, 567]},
	{"text": "个人史：生于原籍，否认长期外地居住史，否认疫区居留史，否认特殊化学品及放射线接触", "bbox": [114, 574, 902, 590]},
	{"text": "史。有吸烟史20余年，否认饮酒。否认冶游史。", "bbox": [85, 598, 473, 614]},
	{"text": "婚育史：已婚已育，配偶及孩子均体健。", "bbox": [114, 622, 452, 638]},
	{"text": "家族史：父已故，母健在。其父有肺癌史。否认家族中有“肝炎、伤寒、结核”等传染病史，否", "bbox": [114, 646, 902, 662]},
	{"text": "认家族中有其他遗传性疾病史。", "bbox": [85, 670, 364, 686]},
	{"text": "体格检查", "bbox": [458, 696, 570, 710]},
	{"text": "T:36.5℃", "bbox": [164, 719, 245, 734]},
	{"text": "P:79次/分", "bbox": [306, 719, 398, 734]},
	{"text": "R:19次/分", "bbox": [447, 719, 550, 734]},
	{"text": "BP:112/69mmHg", "bbox": [611, 719, 754, 734]},
	{"text": "一般情况：神志清楚，发育正常，营养良好，体型正常，正常面容，表情安静，自动体位，查", "bbox": [90, 743, 903, 759]},
	{"text": "体合作，对答切题，步行入院。", "bbox": [90, 766, 345, 782]},
	{"text": "第1页", "bbox": [467, 808, 528, 821]}
]
2026-08-10 19:30:25,190 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=13.2s
2026-08-10 19:30:25,190 INFO     29 [qwen-vl-text] coord item[0]: text=姓名, bbox=[109, 105, 150, 120]
2026-08-10 19:30:25,190 INFO     29 [qwen-vl-text] coord item[1]: text=住址：福建省三明市尤溪县, bbox=[405, 104, 648, 120]
2026-08-10 19:30:25,190 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[109, 131, 190, 147]
2026-08-10 19:30:25,190 INFO     29 [qwen-vl-text] coord item[3]: text=工作单位：/, bbox=[405, 131, 539, 147]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：49岁, bbox=[109, 158, 209, 173]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[5]: text=入院日期：2026.03.16 10:21:29, bbox=[405, 158, 700, 173]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻：已婚, bbox=[109, 184, 210, 200]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[7]: text=记录时间：2026.03.16 10:21:29, bbox=[405, 184, 700, 200]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[8]: text=民族：汉族, bbox=[109, 210, 210, 226]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[9]: text=病史陈述者：患者及家属, bbox=[405, 210, 626, 226]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[10]: text=出生地：福建省三明市, bbox=[109, 237, 314, 252]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[11]: text=病史可靠程度：基本可靠, bbox=[405, 237, 626, 252]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[12]: text=职业(工种)：/, bbox=[109, 263, 244, 278]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史：未发现, bbox=[405, 263, 547, 278]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：确诊左下肺鳞癌4天。, bbox=[113, 291, 360, 307]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：缘于2026.03.05以“咳嗽、咳痰1月”就诊于尤溪县总医院，查“2026.03.06胸部, bbox=[85, 314, 899, 330]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[16]: text=增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。”, bbox=[85, 338, 898, 375]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[17]: text=于2026.03.09行“支气管镜检查+支气管粘膜活检术”，术顺，术后病理示：（左肺下叶粘, bbox=[85, 384, 900, 400]
2026-08-10 19:30:25,191 INFO     29 [qwen-vl-text] coord item[18]: text=膜组织）浸润性鳞状细胞癌。, bbox=[85, 408, 344, 424]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[19]: text=予抗感染、止咳、化痰后咳嗽、咳痰好转，, bbox=[114, 432, 460, 448]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[20]: text=无头晕、头痛，无胸闷、胸痛，无畏冷、发热，无心悸、呼吸困难，无乏力、盗汗，无腹胀、腹痛，, bbox=[85, 456, 898, 472]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[21]: text=无恶心、呕吐，无声音嘶哑、吞咽困难等不适。今为进一步诊治就诊我科，门诊拟“左下肺腺, bbox=[85, 479, 899, 496]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[22]: text=癌”收治入院，自发病以来，精神、食欲、睡眠尚可，大、小便正常，体重近期未见明显增减。, bbox=[85, 503, 858, 519]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[23]: text=既往史：平素身体健康，否认高血压，否认糖尿病，否认冠心病，否认肝炎、结核、菌痢、伤寒, bbox=[85, 526, 902, 543]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[24]: text=等传染病史，否认其他手术史，否认输血史，否认外伤史，否认药物过敏史，预防接种按时完成。, bbox=[85, 550, 900, 567]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[25]: text=个人史：生于原籍，否认长期外地居住史，否认疫区居留史，否认特殊化学品及放射线接触, bbox=[114, 574, 902, 590]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[26]: text=史。有吸烟史20余年，否认饮酒。否认冶游史。, bbox=[85, 598, 473, 614]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[27]: text=婚育史：已婚已育，配偶及孩子均体健。, bbox=[114, 622, 452, 638]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[28]: text=家族史：父已故，母健在。其父有肺癌史。否认家族中有“肝炎、伤寒、结核”等传染病史，否, bbox=[114, 646, 902, 662]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[29]: text=认家族中有其他遗传性疾病史。, bbox=[85, 670, 364, 686]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[30]: text=体格检查, bbox=[458, 696, 570, 710]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[31]: text=T:36.5℃, bbox=[164, 719, 245, 734]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[32]: text=P:79次/分, bbox=[306, 719, 398, 734]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[33]: text=R:19次/分, bbox=[447, 719, 550, 734]
2026-08-10 19:30:25,192 INFO     29 [qwen-vl-text] coord item[34]: text=BP:112/69mmHg, bbox=[611, 719, 754, 734]
2026-08-10 19:30:25,193 INFO     29 [qwen-vl-text] coord item[35]: text=一般情况：神志清楚，发育正常，营养良好，体型正常，正常面容，表情安静，自动体位，查, bbox=[90, 743, 903, 759]
2026-08-10 19:30:25,193 INFO     29 [qwen-vl-text] coord item[36]: text=体合作，对答切题，步行入院。, bbox=[90, 766, 345, 782]
2026-08-10 19:30:25,193 INFO     29 [qwen-vl-text] coord item[37]: text=第1页, bbox=[467, 808, 528, 821]
2026-08-10 19:30:25,193 INFO     29 [qwen-vl-text] page=0 — 38/38 coords, api_time=13.2s
2026-08-10 19:30:25,196 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1194270, prompt_len=1585
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["皮肤粘膜：色泽正常，未见黄染，未见紫绀，未见色素沉着，未见皮疹，未见皮下出血。皮温", "正常，湿度正常，弹性好，无水肿，未见肝掌，未见蜘蛛痣。", "淋巴结：全身浅表淋巴结未触及。", "头颅：大小正常，形状正常，头发分布正常，眼睑无浮肿，眼球无异常，巩膜无黄染，结膜正", "常，角膜透明，瞳孔等大等圆，直径3mm，对光反射灵敏。耳廓无畸形，外耳道正常，无异常分泌", "物，听力正常，无乳突压痛。双侧鼻唇沟对称，鼻中隔无偏曲，鼻腔通气畅，无副鼻窦区压痛。口", "唇无紫绀，口腔粘膜完整，口腔无异味，伸舌居中，咽无充血，扁桃体无肿大，无脓点。", "颈部：颈柔软，颈静脉无怒张，肝颈静脉回流征阴性，未见颈动脉异常搏动，气管居中，甲", "状腺无肿大，无血管杂音。", "胸部：胸廓无畸形，胸壁静脉未见，无皮下气肿，肋间隙正常。胸骨无压痛，胸廓挤压征阴", "性，无男乳女化。", "肺部：双侧呼吸运动匀称，双侧触觉语颤对称，叩诊音清，呼吸音清，未闻及干湿罗音，未", "闻及胸膜摩擦音。", "心脏：无心前区隆起，心尖搏动正常，位于第Ⅴ肋间，左锁骨中线内0.5cm处，未扪及震颤", "及抬举样搏动，心界叩诊无扩大，心音清晰，心率79次/分，节律整齐，A2>P2，无杂音。心浊音界", "大小如下图所示：", "右(CM) 肋间 左(CM)", "2 Ⅱ 2", "2 Ⅲ 3.5", "3 Ⅳ 5.5", "Ⅴ 8.0", "注：左锁骨中线距前正中线8.5CM。", "周围血管：脉率79次/分，节律整齐，无脉搏短绌，无奇脉，无交替脉，无毛细血管搏动征，", "无Duroziez二重杂音，无大血管枪击音，无水冲脉。双侧足背动脉及桡动脉搏动良好对称。", "腹部：腹平坦，呼吸运动自如，腹壁静脉未见怒张，腹壁皮肤无皮疹，无色素沉着，无腹纹，", "无疤痕，无疝，未见胃肠型及蠕动波，无上腹部搏动。全腹软，无肌紧张，无压痛及反跳痛，未触", "及包块，肝脏右肋下、剑突下未触及，胆囊未触及，莫菲氏征阴性，脾脏左肋下未触及，双肾未触", "及，双侧输尿管径路无压痛，无液波震颤。鼓音，肝上界位于右锁骨中线上第Ⅳ肋间，肝区无叩", "击痛，胃泡鼓音区存在，肾区无叩痛，移动性浊音阴性。肠鸣音正常，4次/分，未闻及振水音及血", "第2页"]

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
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord API raw response (len=2187):
[
	{"text": "皮肤粘膜：色泽正常，未见黄染，未见紫绀，未见色素沉着，未见皮疹，未见皮下出血。皮温", "bbox": [75, 88, 903, 107]},
	{"text": "正常，湿度正常，弹性好，无水肿，未见肝掌，未见蜘蛛痣。", "bbox": [75, 113, 568, 131]},
	{"text": "淋巴结：全身浅表淋巴结未触及。", "bbox": [111, 140, 412, 157]},
	{"text": "头颅：大小正常，形状正常，头发分布正常，眼睑无浮肿，眼球无异常，巩膜无黄染，结膜正", "bbox": [75, 165, 903, 183]},
	{"text": "常，角膜透明，瞳孔等大等圆，直径3mm，对光反射灵敏。耳廓无畸形，外耳道正常，无异常分泌", "bbox": [75, 190, 902, 208]},
	{"text": "物，听力正常，无乳突压痛。双侧鼻唇沟对称，鼻中隔无偏曲，鼻腔通气畅，无副鼻窦区压痛。口", "bbox": [75, 215, 902, 233]},
	{"text": "唇无紫绀，口腔粘膜完整，口腔无异味，伸舌居中，咽无充血，扁桃体无肿大，无脓点。", "bbox": [75, 240, 808, 258]},
	{"text": "颈部：颈柔软，颈静脉无怒张，肝颈静脉回流征阴性，未见颈动脉异常搏动，气管居中，甲", "bbox": [111, 266, 902, 284]},
	{"text": "状腺无肿大，无血管杂音。", "bbox": [75, 291, 304, 309]},
	{"text": "胸部：胸廓无畸形，胸壁静脉未见，无皮下气肿，肋间隙正常。胸骨无压痛，胸廓挤压征阴", "bbox": [111, 317, 902, 335]},
	{"text": "性，无男乳女化。", "bbox": [75, 342, 220, 360]},
	{"text": "肺部：双侧呼吸运动匀称，双侧触觉语颤对称，叩诊音清，呼吸音清，未闻及干湿罗音，未", "bbox": [111, 368, 903, 386]},
	{"text": "闻及胸膜摩擦音。", "bbox": [75, 393, 234, 410]},
	{"text": "心脏：无心前区隆起，心尖搏动正常，位于第Ⅴ肋间，左锁骨中线内0.5cm处，未扪及震颤", "bbox": [111, 418, 903, 436]},
	{"text": "及抬举样搏动，心界叩诊无扩大，心音清晰，心率79次/分，节律整齐，A2>P2，无杂音。心浊音界", "bbox": [75, 443, 902, 461]},
	{"text": "大小如下图所示：", "bbox": [75, 468, 230, 485]},
	{"text": "右(CM) 肋间 左(CM)", "bbox": [607, 492, 885, 509]},
	{"text": "2 Ⅱ 2", "bbox": [648, 517, 838, 535]},
	{"text": "2 Ⅲ 3.5", "bbox": [648, 542, 856, 560]},
	{"text": "3 Ⅳ 5.5", "bbox": [648, 567, 856, 585]},
	{"text": "Ⅴ 8.0", "bbox": [733, 592, 856, 610]},
	{"text": "注：左锁骨中线距前正中线8.5CM。", "bbox": [556, 617, 865, 634]},
	{"text": "周围血管：脉率79次/分，节律整齐，无脉搏短绌，无奇脉，无交替脉，无毛细血管搏动征，", "bbox": [111, 642, 902, 660]},
	{"text": "无Duroziez二重杂音，无大血管枪击音，无水冲脉。双侧足背动脉及桡动脉搏动良好对称。", "bbox": [82, 667, 860, 685]},
	{"text": "腹部：腹平坦，呼吸运动自如，腹壁静脉未见怒张，腹壁皮肤无皮疹，无色素沉着，无腹纹，", "bbox": [82, 692, 902, 710]},
	{"text": "无疤痕，无疝，未见胃肠型及蠕动波，无上腹部搏动。全腹软，无肌紧张，无压痛及反跳痛，未触", "bbox": [82, 717, 902, 735]},
	{"text": "及包块，肝脏右肋下、剑突下未触及，胆囊未触及，莫菲氏征阴性，脾脏左肋下未触及，双肾未触", "bbox": [82, 742, 902, 760]},
	{"text": "及，双侧输尿管径路无压痛，无液波震颤。鼓音，肝上界位于右锁骨中线上第Ⅳ肋间，肝区无叩", "bbox": [82, 767, 902, 785]},
	{"text": "击痛，胃泡鼓音区存在，肾区无叩痛，移动性浊音阴性。肠鸣音正常，4次/分，未闻及振水音及血", "bbox": [82, 792, 902, 810]},
	{"text": "第2页", "bbox": [464, 826, 525, 841]}
]
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=12.4s
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord item[0]: text=皮肤粘膜：色泽正常，未见黄染，未见紫绀，未见色素沉着，未见皮疹，未见皮下出血。皮温, bbox=[75, 88, 903, 107]
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord item[1]: text=正常，湿度正常，弹性好，无水肿，未见肝掌，未见蜘蛛痣。, bbox=[75, 113, 568, 131]
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord item[2]: text=淋巴结：全身浅表淋巴结未触及。, bbox=[111, 140, 412, 157]
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord item[3]: text=头颅：大小正常，形状正常，头发分布正常，眼睑无浮肿，眼球无异常，巩膜无黄染，结膜正, bbox=[75, 165, 903, 183]
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord item[4]: text=常，角膜透明，瞳孔等大等圆，直径3mm，对光反射灵敏。耳廓无畸形，外耳道正常，无异常分泌, bbox=[75, 190, 902, 208]
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord item[5]: text=物，听力正常，无乳突压痛。双侧鼻唇沟对称，鼻中隔无偏曲，鼻腔通气畅，无副鼻窦区压痛。口, bbox=[75, 215, 902, 233]
2026-08-10 19:30:37,590 INFO     29 [qwen-vl-text] coord item[6]: text=唇无紫绀，口腔粘膜完整，口腔无异味，伸舌居中，咽无充血，扁桃体无肿大，无脓点。, bbox=[75, 240, 808, 258]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[7]: text=颈部：颈柔软，颈静脉无怒张，肝颈静脉回流征阴性，未见颈动脉异常搏动，气管居中，甲, bbox=[111, 266, 902, 284]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[8]: text=状腺无肿大，无血管杂音。, bbox=[75, 291, 304, 309]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[9]: text=胸部：胸廓无畸形，胸壁静脉未见，无皮下气肿，肋间隙正常。胸骨无压痛，胸廓挤压征阴, bbox=[111, 317, 902, 335]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[10]: text=性，无男乳女化。, bbox=[75, 342, 220, 360]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[11]: text=肺部：双侧呼吸运动匀称，双侧触觉语颤对称，叩诊音清，呼吸音清，未闻及干湿罗音，未, bbox=[111, 368, 903, 386]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[12]: text=闻及胸膜摩擦音。, bbox=[75, 393, 234, 410]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[13]: text=心脏：无心前区隆起，心尖搏动正常，位于第Ⅴ肋间，左锁骨中线内0.5cm处，未扪及震颤, bbox=[111, 418, 903, 436]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[14]: text=及抬举样搏动，心界叩诊无扩大，心音清晰，心率79次/分，节律整齐，A2>P2，无杂音。心浊音界, bbox=[75, 443, 902, 461]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[15]: text=大小如下图所示：, bbox=[75, 468, 230, 485]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[16]: text=右(CM) 肋间 左(CM), bbox=[607, 492, 885, 509]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[17]: text=2 Ⅱ 2, bbox=[648, 517, 838, 535]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[18]: text=2 Ⅲ 3.5, bbox=[648, 542, 856, 560]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[19]: text=3 Ⅳ 5.5, bbox=[648, 567, 856, 585]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[20]: text=Ⅴ 8.0, bbox=[733, 592, 856, 610]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[21]: text=注：左锁骨中线距前正中线8.5CM。, bbox=[556, 617, 865, 634]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[22]: text=周围血管：脉率79次/分，节律整齐，无脉搏短绌，无奇脉，无交替脉，无毛细血管搏动征，, bbox=[111, 642, 902, 660]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[23]: text=无Duroziez二重杂音，无大血管枪击音，无水冲脉。双侧足背动脉及桡动脉搏动良好对称。, bbox=[82, 667, 860, 685]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[24]: text=腹部：腹平坦，呼吸运动自如，腹壁静脉未见怒张，腹壁皮肤无皮疹，无色素沉着，无腹纹，, bbox=[82, 692, 902, 710]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[25]: text=无疤痕，无疝，未见胃肠型及蠕动波，无上腹部搏动。全腹软，无肌紧张，无压痛及反跳痛，未触, bbox=[82, 717, 902, 735]
2026-08-10 19:30:37,591 INFO     29 [qwen-vl-text] coord item[26]: text=及包块，肝脏右肋下、剑突下未触及，胆囊未触及，莫菲氏征阴性，脾脏左肋下未触及，双肾未触, bbox=[82, 742, 902, 760]
2026-08-10 19:30:37,592 INFO     29 [qwen-vl-text] coord item[27]: text=及，双侧输尿管径路无压痛，无液波震颤。鼓音，肝上界位于右锁骨中线上第Ⅳ肋间，肝区无叩, bbox=[82, 767, 902, 785]
2026-08-10 19:30:37,592 INFO     29 [qwen-vl-text] coord item[28]: text=击痛，胃泡鼓音区存在，肾区无叩痛，移动性浊音阴性。肠鸣音正常，4次/分，未闻及振水音及血, bbox=[82, 792, 902, 810]
2026-08-10 19:30:37,592 INFO     29 [qwen-vl-text] coord item[29]: text=第2页, bbox=[464, 826, 525, 841]
2026-08-10 19:30:37,592 INFO     29 [qwen-vl-text] page=1 — 30/30 coords, api_time=12.4s
2026-08-10 19:30:37,594 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=647268, prompt_len=1027
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共13行）
["管杂音。", "肛门生殖器：肛门及外生殖器未见异常。", "脊柱四肢：脊柱生理弯曲正常，活动度正常，脊柱无压痛，无叩击痛；各关节四肢形态正常。肢体无浮肿，无静脉曲张，无色素沉着，无溃疡。", "神经系统：四肢肌力正常，肌张力正常，角膜反射、腹壁反射、肱二头肌、肱三头肌、桡反射、膝反射、跟腱反射正常，巴彬斯基征未引出，脑膜刺激征阴性。", "专科情况", "生命征平稳，神志清楚，浅表淋巴结未触及淋巴结肿大。胸廓对称无畸形，胸壁未见静脉曲张，双肺触觉语颤对称，双肺叩诊呈清音，双肺呼吸音清，未闻及明显干湿性啰音及摩擦音。心前区无隆起，心脏触诊未及震颤，心界叩诊无扩大，心律齐，各瓣音区心音正常，未闻及病理性杂音。腹平软。未见胃肠型及蠕动波，肝脏肋下未触及，无压痛及反跳痛。双下肢无浮肿。", "辅助检查", "出院诊断：", "医生签名：", "初步诊断：肺结节性质待查：", "肺癌？", "炎性假瘤？", "医生签名："]

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
2026-08-10 19:30:45,740 INFO     29 [qwen-vl-text] coord API raw response (len=943):
[
	{"text": "管杂音。", "bbox": [90, 89, 161, 105]},
	{"text": "肛门生殖器：肛门及外生殖器未见异常。", "bbox": [136, 114, 492, 129]},
	{"text": "脊柱四肢：脊柱生理弯曲正常，活动度正常，脊柱无压痛，无叩击痛；各关节四肢形态正常。肢体无浮肿，无静脉曲张，无色素沉着，无溃疡。", "bbox": [90, 138, 901, 178]},
	{"text": "神经系统：四肢肌力正常，肌张力正常，角膜反射、腹壁反射、肱二头肌、肱三头肌、桡反射、膝反射、跟腱反射正常，巴彬斯基征未引出，脑膜刺激征阴性。", "bbox": [90, 187, 901, 228]},
	{"text": "专科情况", "bbox": [457, 233, 537, 248]},
	{"text": "生命征平稳，神志清楚，浅表淋巴结未触及淋巴结肿大。胸廓对称无畸形，胸壁未见静脉曲张，双肺触觉语颤对称，双肺叩诊呈清音，双肺呼吸音清，未闻及明显干湿性啰音及摩擦音。心前区无隆起，心脏触诊未及震颤，心界叩诊无扩大，心律齐，各瓣音区心音正常，未闻及病理性杂音。腹平软。未见胃肠型及蠕动波，肝脏肋下未触及，无压痛及反跳痛。双下肢无浮肿。", "bbox": [90, 252, 900, 343]},
	{"text": "辅助检查", "bbox": [459, 352, 569, 367]},
	{"text": "出院诊断：", "bbox": [92, 426, 183, 442]},
	{"text": "医生签名：", "bbox": [94, 573, 181, 589]},
	{"text": "初步诊断：肺结节性质待查：", "bbox": [478, 426, 745, 442]},
	{"text": "肺癌？", "bbox": [615, 452, 669, 467]},
	{"text": "炎性假瘤？", "bbox": [615, 475, 708, 490]},
	{"text": "医生签名：", "bbox": [469, 573, 555, 589]}
]
2026-08-10 19:30:45,740 INFO     29 [qwen-vl-text] coord API: raw_items=13, valid_items=13, elapsed=8.1s
2026-08-10 19:30:45,740 INFO     29 [qwen-vl-text] coord item[0]: text=管杂音。, bbox=[90, 89, 161, 105]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[1]: text=肛门生殖器：肛门及外生殖器未见异常。, bbox=[136, 114, 492, 129]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[2]: text=脊柱四肢：脊柱生理弯曲正常，活动度正常，脊柱无压痛，无叩击痛；各关节四肢形态正常。肢体无浮肿，无静脉曲张，无色素沉着，无溃疡。, bbox=[90, 138, 901, 178]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[3]: text=神经系统：四肢肌力正常，肌张力正常，角膜反射、腹壁反射、肱二头肌、肱三头肌、桡反射、膝反射、跟腱反射正常，巴彬斯基征未引出，脑膜刺激征阴性。, bbox=[90, 187, 901, 228]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[4]: text=专科情况, bbox=[457, 233, 537, 248]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[5]: text=生命征平稳，神志清楚，浅表淋巴结未触及淋巴结肿大。胸廓对称无畸形，胸壁未见静脉曲张，双肺触觉语颤对称，双肺叩诊呈清音，双肺呼吸音清，未闻及明显干湿性啰音及摩擦音。心前区无隆起，心脏触诊未及震颤，心界叩诊无扩大，心律齐，各瓣音区心音正常，未闻及病理性杂音。腹平软。未见胃肠型及蠕动波，肝脏肋下未触及，无压痛及反跳痛。双下肢无浮肿。, bbox=[90, 252, 900, 343]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[6]: text=辅助检查, bbox=[459, 352, 569, 367]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[7]: text=出院诊断：, bbox=[92, 426, 183, 442]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[8]: text=医生签名：, bbox=[94, 573, 181, 589]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[9]: text=初步诊断：肺结节性质待查：, bbox=[478, 426, 745, 442]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[10]: text=肺癌？, bbox=[615, 452, 669, 467]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[11]: text=炎性假瘤？, bbox=[615, 475, 708, 490]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] coord item[12]: text=医生签名：, bbox=[469, 573, 555, 589]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] page=2 — 13/13 coords, api_time=8.1s
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] new_positions (81):
[[0, 64.855, 89.25, 88.41, 101.03999999999999], [0, 240.975, 385.56, 87.568, 101.03999999999999], [0, 64.855, 113.05, 110.30199999999999, 123.774], [0, 240.975, 320.705, 110.30199999999999, 123.774], [0, 64.855, 124.35499999999999, 133.036, 145.666], [0, 240.975, 416.5, 133.036, 145.666], [0, 64.855, 124.94999999999999, 154.928, 168.4], [0, 240.975, 416.5, 154.928, 168.4], [0, 64.855, 124.94999999999999, 176.82, 190.292], [0, 240.975, 372.46999999999997, 176.82, 190.292], [0, 64.855, 186.82999999999998, 199.554, 212.184], [0, 240.975, 372.46999999999997, 199.554, 212.184], [0, 64.855, 145.18, 221.446, 234.076], [0, 240.975, 325.465, 221.446, 234.076], [0, 67.235, 214.2, 245.022, 258.49399999999997], [0, 50.574999999999996, 534.905, 264.388, 277.86], [0, 50.574999999999996, 534.31, 284.596, 315.75], [0, 50.574999999999996, 535.5, 323.328, 336.8], [0, 50.574999999999996, 204.67999999999998, 343.536, 357.008], [0, 67.83, 273.7, 363.74399999999997, 377.216], [0, 50.574999999999996, 534.31, 383.952, 397.424], [0, 50.574999999999996, 534.905, 403.318, 417.632], [0, 50.574999999999996, 510.51, 423.526, 436.998], [0, 50.574999999999996, 536.6899999999999, 442.892, 457.20599999999996], [0, 50.574999999999996, 535.5, 463.09999999999997, 477.414], [0, 67.83, 536.6899999999999, 483.308, 496.78], [0, 50.574999999999996, 281.435, 503.51599999999996, 516.9879999999999], [0, 67.83, 268.94, 523.7239999999999, 537.196], [0, 67.83, 536.6899999999999, 543.932, 557.404], [0, 50.574999999999996, 216.57999999999998, 564.14, 577.612], [0, 272.51, 339.15, 586.0319999999999, 597.8199999999999], [0, 97.58, 145.775, 605.398, 618.028], [0, 182.07, 236.81, 605.398, 618.028], [0, 265.965, 327.25, 605.398, 618.028], [0, 363.54499999999996, 448.63, 605.398, 618.028], [0, 53.55, 537.285, 625.606, 639.078], [0, 53.55, 205.27499999999998, 644.972, 658.444], [0, 277.865, 314.15999999999997, 680.336, 691.2819999999999], [1, 44.625, 537.285, 74.096, 90.094], [1, 44.625, 337.96, 95.146, 110.30199999999999], [1, 66.045, 245.14, 117.88, 132.194], [1, 44.625, 537.285, 138.93, 154.08599999999998], [1, 44.625, 536.6899999999999, 159.98, 175.136], [1, 44.625, 536.6899999999999, 181.03, 196.186], [1, 44.625, 480.76, 202.07999999999998, 217.236], [1, 66.045, 536.6899999999999, 223.97199999999998, 239.128], [1, 44.625, 180.88, 245.022, 260.178], [1, 66.045, 536.6899999999999, 266.914, 282.07], [1, 44.625, 130.9, 287.964, 303.12], [1, 66.045, 537.285, 309.856, 325.012], [1, 44.625, 139.23, 330.906, 345.21999999999997], [1, 66.045, 537.285, 351.95599999999996, 367.11199999999997], [1, 44.625, 536.6899999999999, 373.006, 388.162], [1, 44.625, 136.85, 394.056, 408.37], [1, 361.16499999999996, 526.5749999999999, 414.264, 428.578], [1, 385.56, 498.60999999999996, 435.31399999999996, 450.46999999999997], [1, 385.56, 509.32, 456.364, 471.52], [1, 385.56, 509.32, 477.414, 492.57], [1, 436.135, 509.32, 498.464, 513.62], [1, 330.82, 514.675, 519.514, 533.828], [1, 66.045, 536.6899999999999, 540.564, 555.72], [1, 48.79, 511.7, 561.614, 576.77], [1, 48.79, 536.6899999999999, 582.664, 597.8199999999999], [1, 48.79, 536.6899999999999, 603.7139999999999, 618.87], [1, 48.79, 536.6899999999999, 624.764, 639.92], [1, 48.79, 536.6899999999999, 645.814, 660.97], [1, 48.79, 536.6899999999999, 666.864, 682.02], [1, 276.08, 312.375, 695.492, 708.122], [2, 53.55, 95.795, 74.938, 88.41], [2, 80.92, 292.74, 95.988, 108.618], [2, 53.55, 536.095, 116.196, 149.876], [2, 53.55, 536.095, 157.454, 191.976], [2, 271.91499999999996, 319.515, 196.186, 208.816], [2, 53.55, 535.5, 212.184, 288.806], [2, 273.10499999999996, 338.555, 296.384, 309.014], [2, 54.739999999999995, 108.88499999999999, 358.692, 372.164], [2, 55.93, 107.695, 482.466, 495.938], [2, 284.40999999999997, 443.275, 358.692, 372.164], [2, 365.925, 398.055, 380.584, 393.214], [2, 365.925, 421.26, 399.95, 412.58], [2, 279.055, 330.22499999999997, 482.466, 495.938]]
2026-08-10 19:30:45,741 INFO     29 [qwen-vl-text] ═══ DONE ═══ 81 positions, pages=3, time=67.6s
2026-08-10 19:30:45,755 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 19:30:45,755 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:30:45,755 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 19:30:45,755 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:30:45.755+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 91, "failed": 0, "current": {"14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:30:45,761 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:30:45,762 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:30:45,762 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:30:45,762 INFO     29 [qwen-vl-text] positions(110): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:30:45,762 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [110]
2026-08-10 19:30:45,970 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:30:45,972 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1062
2026-08-10 19:30:45,972 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:30:45,972 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 82, \"bbox_end\": 191, \"encounter_dates\": [\"2026-03-17\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "测量结果:\nLved:46.5 mm\nLve5:28.9 mm\nLa:26.6 mm\nAo:25.7 mm\nLvpw:8.5 mm\nIvs:9.5 mm\nRv:20.1 mm\nRa-L:34.8 mm\nRa-M:25.5 mm\nPa:17.6 mm\nE:0.46 m/s\nA:0.63 m/s\nHr:90 bpm\nFb:37.8 %\nBf:68.0 %(Teich)\nEDV:99.8 ml\nSv:67.8 ml\nCo:6.1 L/min\nCi:4.0 L/min. m²\nH:166 cm\nW:52.5 kg\nBSA:1.5 m²\nLVM:140.2 g\nLVMI:93.4 g/m²\nB':0.08 m/s\nA':0.10 m/s\nRWT:0.38\nE/A:0.7\nE/E':5.7\n正常参考值(mm) 摘自中国成年人超声心动图检查测量指南《中华超声影像学杂志》2016.25(8):\nAO\nLA\nLV\nIVS\nRA\nRV\nPA\nLVMI\nEF(%)\n0-1岁\n8-15\n8-18\n17-31\n1.5-4\n17-32\n7-12\n6-12\n≥55\n1-6岁\n15-21\n14-21\n27-35\n3-5.5\n26-37\n8-14\n10-16\n≥55\n6-10岁\n17-23\n17-24\n30-38\n5-7\n30-39\n10-15\n14-18\n≥55\n10-14岁\n18-27\n19-30\n32-50\n5-10\n34-47\n11-17\n16-20\n≥55\n成人(男)\n27.7±5.7\n31.1±3.9\n46.2±4.0\n8.9±1.3\n44.4±4.7\n22.3±3.9\n20.1±3.2\n≥125\n≥55\n成人(女)\n25.9±3.5\n29.4±5.8\n43.2±3.3\n8.1±1.3\n41.5±4.7\n21.1±3.6\n19.2±3.1\n≥115\n≥55\n检查描述:\n二维及M型超声:\n静息时未见节段性室壁运动功能异常(见图)。各组瓣膜形态未见异常。心包腔正常。室间隔连\n续性完整，大血管位置关系正常，主一肺动脉无沟通。\n多普勒:\n三尖瓣反流最大压差17MMHG，估测肺动脉收缩压22MMHG。\n彩色多普勒:\n二尖瓣微量反流。三尖瓣轻度反流。主动脉瓣未见明显反流。肺动脉瓣轻度反流。\n超声提示:\n心脏结构及功能未见明显异常改变\n记录医生:袁瑄宸 报告录入:黄玉云 检查医生:刘文坤 复审医生:\n报告日期: 2026-03-17 16:38:04\n检查日期: 2026-03-17\n(本报告仅供临床参考,不做任何证明。)",
    "role": "user"
  }
]
2026-08-10 19:31:08,062 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:31:08,062 INFO     29 [qwen-vl-text] LLM output (len=1380):
{
  "exam_date": "2026-03-17",
  "report_date": "2026-03-17",
  "exam_name": "超声心动图",
  "exam_category": "imaging",
  "body_part": "心脏",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "测量结果:\nLved:46.5 mm\nLve5:28.9 mm\nLa:26.6 mm\nAo:25.7 mm\nLvpw:8.5 mm\nIvs:9.5 mm\nRv:20.1 mm\nRa-L:34.8 mm\nRa-M:25.5 mm\nPa:17.6 mm\nE:0.46 m/s\nA:0.63 m/s\nHr:90 bpm\nFb:37.8 %\nBf:68.0 %(Teich)\nEDV:99.8 ml\nSv:67.8 ml\nCo:6.1 L/min\nCi:4.0 L/min. m²\nH:166 cm\nW:52.5 kg\nBSA:1.5 m²\nLVM:140.2 g\nLVMI:93.4 g/m²\nB':0.08 m/s\nA':0.10 m/s\nRWT:0.38\nE/A:0.7\nE/E':5.7\n正常参考值(mm) 摘自中国成年人超声心动图检查测量指南《中华超声影像学杂志》2016.25(8):\nAO\nLA\nLV\nIVS\nRA\nRV\nPA\nLVMI\nEF(%)\n0-1岁\n8-15\n8-18\n17-31\n1.5-4\n17-32\n7-12\n6-12\n≥55\n1-6岁\n15-21\n14-21\n27-35\n3-5.5\n26-37\n8-14\n10-16\n≥55\n6-10岁\n17-23\n17-24\n30-38\n5-7\n30-39\n10-15\n14-18\n≥55\n10-14岁\n18-27\n19-30\n32-50\n5-10\n34-47\n11-17\n16-20\n≥55\n成人(男)\n27.7±5.7\n31.1±3.9\n46.2±4.0\n8.9±1.3\n44.4±4.7\n22.3±3.9\n20.1±3.2\n≥125\n≥55\n成人(女)\n25.9±3.5\n29.4±5.8\n43.2±3.3\n8.1±1.3\n41.5±4.7\n21.1±3.6\n19.2±3.1\n≥115\n≥55\n检查描述:\n二维及M型超声:\n静息时未见节段性室壁运动功能异常(见图)。各组瓣膜形态未见异常。心包腔正常。室间隔连\n续性完整，大血管位置关系正常，主一肺动脉无沟通。\n多普勒:\n三尖瓣反流最大压差17MMHG，估测肺动脉收缩压22MMHG。\n彩色多普勒:\n二尖瓣微量反流。三尖瓣轻度反流。主动脉瓣未见明显反流。肺动脉瓣轻度反流。",
  "conclusion": "超声提示:\n心脏结构及功能未见明显异常改变",
  "physician": "刘文坤",
  "reviewer": null
}
2026-08-10 19:31:08,064 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1392932, prompt_len=2006
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共110行）
["测量结果:", "Lved:46.5 mm", "Lve5:28.9 mm", "La:26.6 mm", "Ao:25.7 mm", "Lvpw:8.5 mm", "Ivs:9.5 mm", "Rv:20.1 mm", "Ra-L:34.8 mm", "Ra-M:25.5 mm", "Pa:17.6 mm", "E:0.46 m/s", "A:0.63 m/s", "Hr:90 bpm", "Fb:37.8 %", "Bf:68.0 %(Teich)", "EDV:99.8 ml", "Sv:67.8 ml", "Co:6.1 L/min", "Ci:4.0 L/min. m²", "H:166 cm", "W:52.5 kg", "BSA:1.5 m²", "LVM:140.2 g", "LVMI:93.4 g/m²", "B':0.08 m/s", "A':0.10 m/s", "RWT:0.38", "E/A:0.7", "E/E':5.7", "正常参考值(mm) 摘自中国成年人超声心动图检查测量指南《中华超声影像学杂志》2016.25(8):", "AO", "LA", "LV", "IVS", "RA", "RV", "PA", "LVMI", "EF(%)", "0-1岁", "8-15", "8-18", "17-31", "1.5-4", "17-32", "7-12", "6-12", "≥55", "1-6岁", "15-21", "14-21", "27-35", "3-5.5", "26-37", "8-14", "10-16", "≥55", "6-10岁", "17-23", "17-24", "30-38", "5-7", "30-39", "10-15", "14-18", "≥55", "10-14岁", "18-27", "19-30", "32-50", "5-10", "34-47", "11-17", "16-20", "≥55", "成人(男)", "27.7±5.7", "31.1±3.9", "46.2±4.0", "8.9±1.3", "44.4±4.7", "22.3±3.9", "20.1±3.2", "≥125", "≥55", "成人(女)", "25.9±3.5", "29.4±5.8", "43.2±3.3", "8.1±1.3", "41.5±4.7", "21.1±3.6", "19.2±3.1", "≥115", "≥55", "检查描述:", "二维及M型超声:", "静息时未见节段性室壁运动功能异常(见图)。各组瓣膜形态未见异常。心包腔正常。室间隔连", "续性完整，大血管位置关系正常，主一肺动脉无沟通。", "多普勒:", "三尖瓣反流最大压差17MMHG，估测肺动脉收缩压22MMHG。", "彩色多普勒:", "二尖瓣微量反流。三尖瓣轻度反流。主动脉瓣未见明显反流。肺动脉瓣轻度反流。", "超声提示:", "心脏结构及功能未见明显异常改变", "记录医生:袁瑄宸 报告录入:黄玉云 检查医生:刘文坤 复审医生:", "报告日期: 2026-03-17 16:38:04", "检查日期: 2026-03-17", "(本报告仅供临床参考,不做任何证明。)"]

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
2026-08-10 19:31:38,931 INFO     29 [qwen-vl-text] coord API raw response (len=5831):
[
	{"text": "测量结果:", "bbox": [49, 33, 140, 50]},
	{"text": "Lved:46.5 mm", "bbox": [52, 54, 157, 65]},
	{"text": "Lve5:28.9 mm", "bbox": [198, 54, 305, 65]},
	{"text": "La:26.6 mm", "bbox": [346, 54, 438, 65]},
	{"text": "Ao:25.7 mm", "bbox": [495, 54, 585, 65]},
	{"text": "Lvpw:8.5 mm", "bbox": [645, 54, 742, 65]},
	{"text": "Ivs:9.5 mm", "bbox": [795, 54, 882, 65]},
	{"text": "Rv:20.1 mm", "bbox": [52, 68, 140, 79]},
	{"text": "Ra-L:34.8 mm", "bbox": [198, 68, 305, 79]},
	{"text": "Ra-M:25.5 mm", "bbox": [346, 68, 454, 79]},
	{"text": "Pa:17.6 mm", "bbox": [495, 68, 585, 79]},
	{"text": "E:0.46 m/s", "bbox": [645, 68, 732, 79]},
	{"text": "A:0.63 m/s", "bbox": [795, 68, 882, 79]},
	{"text": "Hr:90 bpm", "bbox": [52, 82, 131, 93]},
	{"text": "Fb:37.8 %", "bbox": [198, 82, 279, 93]},
	{"text": "Bf:68.0 %(Teich)", "bbox": [346, 82, 485, 93]},
	{"text": "EDV:99.8 ml", "bbox": [495, 82, 592, 93]},
	{"text": "Sv:67.8 ml", "bbox": [645, 82, 732, 93]},
	{"text": "Co:6.1 L/min", "bbox": [795, 82, 899, 93]},
	{"text": "Ci:4.0 L/min. m²", "bbox": [52, 95, 180, 107]},
	{"text": "H:166 cm", "bbox": [198, 95, 269, 107]},
	{"text": "W:52.5 kg", "bbox": [346, 95, 426, 107]},
	{"text": "BSA:1.5 m²", "bbox": [512, 95, 598, 107]},
	{"text": "LVM:140.2 g", "bbox": [658, 95, 757, 107]},
	{"text": "LVMI:93.4 g/m²", "bbox": [808, 95, 929, 107]},
	{"text": "B':0.08 m/s", "bbox": [52, 109, 154, 120]},
	{"text": "A':0.10 m/s", "bbox": [198, 109, 301, 120]},
	{"text": "RWT:0.38", "bbox": [346, 109, 416, 120]},
	{"text": "E/A:0.7", "bbox": [502, 109, 563, 120]},
	{"text": "E/E':5.7", "bbox": [642, 109, 719, 120]},
	{"text": "正常参考值(mm) 摘自中国成年人超声心动图检查测量指南《中华超声影像学杂志》2016.25(8):", "bbox": [24, 140, 648, 152]},
	{"text": "AO", "bbox": [138, 153, 155, 164]},
	{"text": "LA", "bbox": [232, 153, 250, 164]},
	{"text": "LV", "bbox": [327, 153, 344, 164]},
	{"text": "IVS", "bbox": [416, 153, 438, 164]},
	{"text": "RA", "bbox": [517, 153, 534, 164]},
	{"text": "RV", "bbox": [612, 153, 629, 164]},
	{"text": "PA", "bbox": [707, 153, 724, 164]},
	{"text": "LVMI", "bbox": [789, 153, 817, 164]},
	{"text": "EF(%)", "bbox": [861, 153, 896, 164]},
	{"text": "0-1岁", "bbox": [37, 165, 73, 176]},
	{"text": "8-15", "bbox": [131, 165, 161, 176]},
	{"text": "8-18", "bbox": [225, 165, 255, 176]},
	{"text": "17-31", "bbox": [315, 165, 350, 176]},
	{"text": "1.5-4", "bbox": [410, 165, 446, 176]},
	{"text": "17-32", "bbox": [505, 165, 540, 176]},
	{"text": "7-12", "bbox": [606, 165, 635, 176]},
	{"text": "6-12", "bbox": [700, 165, 730, 176]},
	{"text": "≥55", "bbox": [861, 165, 891, 176]},
	{"text": "1-6岁", "bbox": [37, 177, 73, 188]},
	{"text": "15-21", "bbox": [125, 177, 161, 188]},
	{"text": "14-21", "bbox": [220, 177, 255, 188]},
	{"text": "27-35", "bbox": [315, 177, 350, 188]},
	{"text": "3-5.5", "bbox": [410, 177, 446, 188]},
	{"text": "26-37", "bbox": [505, 177, 540, 188]},
	{"text": "8-14", "bbox": [606, 177, 635, 188]},
	{"text": "10-16", "bbox": [694, 177, 730, 188]},
	{"text": "≥55", "bbox": [861, 177, 891, 188]},
	{"text": "6-10岁", "bbox": [37, 189, 80, 200]},
	{"text": "17-23", "bbox": [125, 189, 161, 200]},
	{"text": "17-24", "bbox": [220, 189, 255, 200]},
	{"text": "30-38", "bbox": [315, 189, 350, 200]},
	{"text": "5-7", "bbox": [417, 189, 441, 200]},
	{"text": "30-39", "bbox": [505, 189, 540, 200]},
	{"text": "10-15", "bbox": [600, 189, 635, 200]},
	{"text": "14-18", "bbox": [694, 189, 730, 200]},
	{"text": "≥55", "bbox": [861, 189, 891, 200]},
	{"text": "10-14岁", "bbox": [37, 201, 88, 212]},
	{"text": "18-27", "bbox": [125, 201, 161, 212]},
	{"text": "19-30", "bbox": [220, 201, 255, 212]},
	{"text": "32-50", "bbox": [315, 201, 350, 212]},
	{"text": "5-10", "bbox": [417, 201, 446, 212]},
	{"text": "34-47", "bbox": [505, 201, 540, 212]},
	{"text": "11-17", "bbox": [600, 201, 635, 212]},
	{"text": "16-20", "bbox": [694, 201, 730, 212]},
	{"text": "≥55", "bbox": [861, 201, 891, 212]},
	{"text": "成人(男)", "bbox": [37, 213, 93, 224]},
	{"text": "27.7±5.7", "bbox": [110, 213, 175, 224]},
	{"text": "31.1±3.9", "bbox": [205, 213, 270, 224]},
	{"text": "46.2±4.0", "bbox": [301, 213, 366, 224]},
	{"text": "8.9±1.3", "bbox": [403, 213, 461, 224]},
	{"text": "44.4±4.7", "bbox": [498, 213, 563, 224]},
	{"text": "22.3±3.9", "bbox": [592, 213, 657, 224]},
	{"text": "20.1±3.2", "bbox": [687, 213, 752, 224]},
	{"text": "≥125", "bbox": [790, 213, 825, 224]},
	{"text": "≥55", "bbox": [861, 213, 891, 224]},
	{"text": "成人(女)", "bbox": [37, 225, 93, 236]},
	{"text": "25.9±3.5", "bbox": [110, 225, 175, 236]},
	{"text": "29.4±5.8", "bbox": [205, 225, 270, 236]},
	{"text": "43.2±3.3", "bbox": [301, 225, 366, 236]},
	{"text": "8.1±1.3", "bbox": [403, 225, 461, 236]},
	{"text": "41.5±4.7", "bbox": [498, 225, 563, 236]},
	{"text": "21.1±3.6", "bbox": [592, 225, 657, 236]},
	{"text": "19.2±3.1", "bbox": [687, 225, 752, 236]},
	{"text": "≥115", "bbox": [790, 225, 825, 236]},
	{"text": "≥55", "bbox": [861, 225, 891, 236]},
	{"text": "检查描述:", "bbox": [50, 445, 158, 463]},
	{"text": "二维及M型超声:", "bbox": [93, 467, 237, 483]},
	{"text": "静息时未见节段性室壁运动功能异常(见图)。各组瓣膜形态未见异常。心包腔正常。室间隔连", "bbox": [93, 483, 952, 500]},
	{"text": "续性完整，大血管位置关系正常，主一肺动脉无沟通。", "bbox": [93, 500, 575, 517]},
	{"text": "多普勒:", "bbox": [93, 535, 164, 552]},
	{"text": "三尖瓣反流最大压差17MMHG，估测肺动脉收缩压22MMHG。", "bbox": [103, 552, 604, 569]},
	{"text": "彩色多普勒:", "bbox": [93, 586, 205, 603]},
	{"text": "二尖瓣微量反流。三尖瓣轻度反流。主动脉瓣未见明显反流。肺动脉瓣轻度反流。", "bbox": [93, 603, 818, 620]},
	{"text": "超声提示:", "bbox": [50, 699, 158, 717]},
	{"text": "心脏结构及功能未见明显异常改变", "bbox": [93, 717, 403, 735]},
	{"text": "记录医生:袁瑄宸 报告录入:黄玉云 检查医生:刘文坤 复审医生:", "bbox": [14, 857, 630, 874]},
	{"text": "报告日期: 2026-03-17 16:38:04", "bbox": [725, 857, 991, 870]},
	{"text": "检查日期: 2026-03-17", "bbox": [725, 885, 910, 898]},
	{"text": "(本报告仅供临床参考,不做任何证明。)", "bbox": [18, 903, 276, 915]}
]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord API: raw_items=110, valid_items=110, elapsed=30.9s
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[0]: text=测量结果:, bbox=[49, 33, 140, 50]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[1]: text=Lved:46.5 mm, bbox=[52, 54, 157, 65]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[2]: text=Lve5:28.9 mm, bbox=[198, 54, 305, 65]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[3]: text=La:26.6 mm, bbox=[346, 54, 438, 65]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[4]: text=Ao:25.7 mm, bbox=[495, 54, 585, 65]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[5]: text=Lvpw:8.5 mm, bbox=[645, 54, 742, 65]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[6]: text=Ivs:9.5 mm, bbox=[795, 54, 882, 65]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[7]: text=Rv:20.1 mm, bbox=[52, 68, 140, 79]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[8]: text=Ra-L:34.8 mm, bbox=[198, 68, 305, 79]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[9]: text=Ra-M:25.5 mm, bbox=[346, 68, 454, 79]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[10]: text=Pa:17.6 mm, bbox=[495, 68, 585, 79]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[11]: text=E:0.46 m/s, bbox=[645, 68, 732, 79]
2026-08-10 19:31:38,933 INFO     29 [qwen-vl-text] coord item[12]: text=A:0.63 m/s, bbox=[795, 68, 882, 79]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[13]: text=Hr:90 bpm, bbox=[52, 82, 131, 93]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[14]: text=Fb:37.8 %, bbox=[198, 82, 279, 93]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[15]: text=Bf:68.0 %(Teich), bbox=[346, 82, 485, 93]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[16]: text=EDV:99.8 ml, bbox=[495, 82, 592, 93]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[17]: text=Sv:67.8 ml, bbox=[645, 82, 732, 93]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[18]: text=Co:6.1 L/min, bbox=[795, 82, 899, 93]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[19]: text=Ci:4.0 L/min. m², bbox=[52, 95, 180, 107]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[20]: text=H:166 cm, bbox=[198, 95, 269, 107]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[21]: text=W:52.5 kg, bbox=[346, 95, 426, 107]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[22]: text=BSA:1.5 m², bbox=[512, 95, 598, 107]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[23]: text=LVM:140.2 g, bbox=[658, 95, 757, 107]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[24]: text=LVMI:93.4 g/m², bbox=[808, 95, 929, 107]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[25]: text=B':0.08 m/s, bbox=[52, 109, 154, 120]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[26]: text=A':0.10 m/s, bbox=[198, 109, 301, 120]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[27]: text=RWT:0.38, bbox=[346, 109, 416, 120]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[28]: text=E/A:0.7, bbox=[502, 109, 563, 120]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[29]: text=E/E':5.7, bbox=[642, 109, 719, 120]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[30]: text=正常参考值(mm) 摘自中国成年人超声心动图检查测量指南《中华超声影像学杂志》2016.25(8):, bbox=[24, 140, 648, 152]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[31]: text=AO, bbox=[138, 153, 155, 164]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[32]: text=LA, bbox=[232, 153, 250, 164]
2026-08-10 19:31:38,934 INFO     29 [qwen-vl-text] coord item[33]: text=LV, bbox=[327, 153, 344, 164]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[34]: text=IVS, bbox=[416, 153, 438, 164]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[35]: text=RA, bbox=[517, 153, 534, 164]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[36]: text=RV, bbox=[612, 153, 629, 164]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[37]: text=PA, bbox=[707, 153, 724, 164]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[38]: text=LVMI, bbox=[789, 153, 817, 164]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[39]: text=EF(%), bbox=[861, 153, 896, 164]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[40]: text=0-1岁, bbox=[37, 165, 73, 176]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[41]: text=8-15, bbox=[131, 165, 161, 176]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[42]: text=8-18, bbox=[225, 165, 255, 176]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[43]: text=17-31, bbox=[315, 165, 350, 176]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[44]: text=1.5-4, bbox=[410, 165, 446, 176]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[45]: text=17-32, bbox=[505, 165, 540, 176]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[46]: text=7-12, bbox=[606, 165, 635, 176]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[47]: text=6-12, bbox=[700, 165, 730, 176]
2026-08-10 19:31:38,935 INFO     29 [qwen-vl-text] coord item[48]: text=≥55, bbox=[861, 165, 891, 176]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[49]: text=1-6岁, bbox=[37, 177, 73, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[50]: text=15-21, bbox=[125, 177, 161, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[51]: text=14-21, bbox=[220, 177, 255, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[52]: text=27-35, bbox=[315, 177, 350, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[53]: text=3-5.5, bbox=[410, 177, 446, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[54]: text=26-37, bbox=[505, 177, 540, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[55]: text=8-14, bbox=[606, 177, 635, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[56]: text=10-16, bbox=[694, 177, 730, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[57]: text=≥55, bbox=[861, 177, 891, 188]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[58]: text=6-10岁, bbox=[37, 189, 80, 200]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[59]: text=17-23, bbox=[125, 189, 161, 200]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[60]: text=17-24, bbox=[220, 189, 255, 200]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[61]: text=30-38, bbox=[315, 189, 350, 200]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[62]: text=5-7, bbox=[417, 189, 441, 200]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[63]: text=30-39, bbox=[505, 189, 540, 200]
2026-08-10 19:31:38,936 INFO     29 [qwen-vl-text] coord item[64]: text=10-15, bbox=[600, 189, 635, 200]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[65]: text=14-18, bbox=[694, 189, 730, 200]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[66]: text=≥55, bbox=[861, 189, 891, 200]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[67]: text=10-14岁, bbox=[37, 201, 88, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[68]: text=18-27, bbox=[125, 201, 161, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[69]: text=19-30, bbox=[220, 201, 255, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[70]: text=32-50, bbox=[315, 201, 350, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[71]: text=5-10, bbox=[417, 201, 446, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[72]: text=34-47, bbox=[505, 201, 540, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[73]: text=11-17, bbox=[600, 201, 635, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[74]: text=16-20, bbox=[694, 201, 730, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[75]: text=≥55, bbox=[861, 201, 891, 212]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[76]: text=成人(男), bbox=[37, 213, 93, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[77]: text=27.7±5.7, bbox=[110, 213, 175, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[78]: text=31.1±3.9, bbox=[205, 213, 270, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[79]: text=46.2±4.0, bbox=[301, 213, 366, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[80]: text=8.9±1.3, bbox=[403, 213, 461, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[81]: text=44.4±4.7, bbox=[498, 213, 563, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[82]: text=22.3±3.9, bbox=[592, 213, 657, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[83]: text=20.1±3.2, bbox=[687, 213, 752, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[84]: text=≥125, bbox=[790, 213, 825, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[85]: text=≥55, bbox=[861, 213, 891, 224]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[86]: text=成人(女), bbox=[37, 225, 93, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[87]: text=25.9±3.5, bbox=[110, 225, 175, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[88]: text=29.4±5.8, bbox=[205, 225, 270, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[89]: text=43.2±3.3, bbox=[301, 225, 366, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[90]: text=8.1±1.3, bbox=[403, 225, 461, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[91]: text=41.5±4.7, bbox=[498, 225, 563, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[92]: text=21.1±3.6, bbox=[592, 225, 657, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[93]: text=19.2±3.1, bbox=[687, 225, 752, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[94]: text=≥115, bbox=[790, 225, 825, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[95]: text=≥55, bbox=[861, 225, 891, 236]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[96]: text=检查描述:, bbox=[50, 445, 158, 463]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[97]: text=二维及M型超声:, bbox=[93, 467, 237, 483]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[98]: text=静息时未见节段性室壁运动功能异常(见图)。各组瓣膜形态未见异常。心包腔正常。室间隔连, bbox=[93, 483, 952, 500]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[99]: text=续性完整，大血管位置关系正常，主一肺动脉无沟通。, bbox=[93, 500, 575, 517]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[100]: text=多普勒:, bbox=[93, 535, 164, 552]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[101]: text=三尖瓣反流最大压差17MMHG，估测肺动脉收缩压22MMHG。, bbox=[103, 552, 604, 569]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[102]: text=彩色多普勒:, bbox=[93, 586, 205, 603]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[103]: text=二尖瓣微量反流。三尖瓣轻度反流。主动脉瓣未见明显反流。肺动脉瓣轻度反流。, bbox=[93, 603, 818, 620]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[104]: text=超声提示:, bbox=[50, 699, 158, 717]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[105]: text=心脏结构及功能未见明显异常改变, bbox=[93, 717, 403, 735]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[106]: text=记录医生:袁瑄宸 报告录入:黄玉云 检查医生:刘文坤 复审医生:, bbox=[14, 857, 630, 874]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[107]: text=报告日期: 2026-03-17 16:38:04, bbox=[725, 857, 991, 870]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[108]: text=检查日期: 2026-03-17, bbox=[725, 885, 910, 898]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] coord item[109]: text=(本报告仅供临床参考,不做任何证明。), bbox=[18, 903, 276, 915]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] page=3 — 110/110 coords, api_time=30.9s
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] new_positions (110):
[[3, 29.154999999999998, 83.3, 27.785999999999998, 42.1], [3, 30.939999999999998, 93.41499999999999, 45.467999999999996, 54.73], [3, 117.80999999999999, 181.475, 45.467999999999996, 54.73], [3, 205.87, 260.61, 45.467999999999996, 54.73], [3, 294.525, 348.075, 45.467999999999996, 54.73], [3, 383.775, 441.48999999999995, 45.467999999999996, 54.73], [3, 473.025, 524.79, 45.467999999999996, 54.73], [3, 30.939999999999998, 83.3, 57.256, 66.518], [3, 117.80999999999999, 181.475, 57.256, 66.518], [3, 205.87, 270.13, 57.256, 66.518], [3, 294.525, 348.075, 57.256, 66.518], [3, 383.775, 435.53999999999996, 57.256, 66.518], [3, 473.025, 524.79, 57.256, 66.518], [3, 30.939999999999998, 77.945, 69.044, 78.306], [3, 117.80999999999999, 166.005, 69.044, 78.306], [3, 205.87, 288.575, 69.044, 78.306], [3, 294.525, 352.24, 69.044, 78.306], [3, 383.775, 435.53999999999996, 69.044, 78.306], [3, 473.025, 534.905, 69.044, 78.306], [3, 30.939999999999998, 107.1, 79.99, 90.094], [3, 117.80999999999999, 160.055, 79.99, 90.094], [3, 205.87, 253.47, 79.99, 90.094], [3, 304.64, 355.81, 79.99, 90.094], [3, 391.51, 450.41499999999996, 79.99, 90.094], [3, 480.76, 552.755, 79.99, 90.094], [3, 30.939999999999998, 91.63, 91.77799999999999, 101.03999999999999], [3, 117.80999999999999, 179.095, 91.77799999999999, 101.03999999999999], [3, 205.87, 247.51999999999998, 91.77799999999999, 101.03999999999999], [3, 298.69, 334.98499999999996, 91.77799999999999, 101.03999999999999], [3, 381.99, 427.805, 91.77799999999999, 101.03999999999999], [3, 14.28, 385.56, 117.88, 127.984], [3, 82.11, 92.225, 128.826, 138.088], [3, 138.04, 148.75, 128.826, 138.088], [3, 194.565, 204.67999999999998, 128.826, 138.088], [3, 247.51999999999998, 260.61, 128.826, 138.088], [3, 307.615, 317.72999999999996, 128.826, 138.088], [3, 364.14, 374.255, 128.826, 138.088], [3, 420.66499999999996, 430.78, 128.826, 138.088], [3, 469.455, 486.11499999999995, 128.826, 138.088], [3, 512.295, 533.12, 128.826, 138.088], [3, 22.015, 43.434999999999995, 138.93, 148.192], [3, 77.945, 95.795, 138.93, 148.192], [3, 133.875, 151.725, 138.93, 148.192], [3, 187.42499999999998, 208.25, 138.93, 148.192], [3, 243.95, 265.37, 138.93, 148.192], [3, 300.47499999999997, 321.3, 138.93, 148.192], [3, 360.57, 377.825, 138.93, 148.192], [3, 416.5, 434.34999999999997, 138.93, 148.192], [3, 512.295, 530.145, 138.93, 148.192], [3, 22.015, 43.434999999999995, 149.034, 158.296], [3, 74.375, 95.795, 149.034, 158.296], [3, 130.9, 151.725, 149.034, 158.296], [3, 187.42499999999998, 208.25, 149.034, 158.296], [3, 243.95, 265.37, 149.034, 158.296], [3, 300.47499999999997, 321.3, 149.034, 158.296], [3, 360.57, 377.825, 149.034, 158.296], [3, 412.93, 434.34999999999997, 149.034, 158.296], [3, 512.295, 530.145, 149.034, 158.296], [3, 22.015, 47.599999999999994, 159.138, 168.4], [3, 74.375, 95.795, 159.138, 168.4], [3, 130.9, 151.725, 159.138, 168.4], [3, 187.42499999999998, 208.25, 159.138, 168.4], [3, 248.11499999999998, 262.395, 159.138, 168.4], [3, 300.47499999999997, 321.3, 159.138, 168.4], [3, 357.0, 377.825, 159.138, 168.4], [3, 412.93, 434.34999999999997, 159.138, 168.4], [3, 512.295, 530.145, 159.138, 168.4], [3, 22.015, 52.36, 169.242, 178.504], [3, 74.375, 95.795, 169.242, 178.504], [3, 130.9, 151.725, 169.242, 178.504], [3, 187.42499999999998, 208.25, 169.242, 178.504], [3, 248.11499999999998, 265.37, 169.242, 178.504], [3, 300.47499999999997, 321.3, 169.242, 178.504], [3, 357.0, 377.825, 169.242, 178.504], [3, 412.93, 434.34999999999997, 169.242, 178.504], [3, 512.295, 530.145, 169.242, 178.504], [3, 22.015, 55.335, 179.346, 188.608], [3, 65.45, 104.125, 179.346, 188.608], [3, 121.975, 160.65, 179.346, 188.608], [3, 179.095, 217.76999999999998, 179.346, 188.608], [3, 239.785, 274.295, 179.346, 188.608], [3, 296.31, 334.98499999999996, 179.346, 188.608], [3, 352.24, 390.91499999999996, 179.346, 188.608], [3, 408.765, 447.44, 179.346, 188.608], [3, 470.04999999999995, 490.875, 179.346, 188.608], [3, 512.295, 530.145, 179.346, 188.608], [3, 22.015, 55.335, 189.45, 198.712], [3, 65.45, 104.125, 189.45, 198.712], [3, 121.975, 160.65, 189.45, 198.712], [3, 179.095, 217.76999999999998, 189.45, 198.712], [3, 239.785, 274.295, 189.45, 198.712], [3, 296.31, 334.98499999999996, 189.45, 198.712], [3, 352.24, 390.91499999999996, 189.45, 198.712], [3, 408.765, 447.44, 189.45, 198.712], [3, 470.04999999999995, 490.875, 189.45, 198.712], [3, 512.295, 530.145, 189.45, 198.712], [3, 29.75, 94.00999999999999, 374.69, 389.846], [3, 55.335, 141.015, 393.214, 406.686], [3, 55.335, 566.4399999999999, 406.686, 421.0], [3, 55.335, 342.125, 421.0, 435.31399999999996], [3, 55.335, 97.58, 450.46999999999997, 464.784], [3, 61.285, 359.38, 464.784, 479.09799999999996], [3, 55.335, 121.975, 493.412, 507.726], [3, 55.335, 486.71, 507.726, 522.04], [3, 29.75, 94.00999999999999, 588.558, 603.7139999999999], [3, 55.335, 239.785, 603.7139999999999, 618.87], [3, 8.33, 374.84999999999997, 721.5939999999999, 735.908], [3, 431.375, 589.645, 721.5939999999999, 732.54], [3, 431.375, 541.4499999999999, 745.17, 756.116], [3, 10.709999999999999, 164.22, 760.326, 770.43]]
2026-08-10 19:31:38,937 INFO     29 [qwen-vl-text] ═══ DONE ═══ 110 positions, pages=1, time=53.2s
2026-08-10 19:31:38,938 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:31:38,945 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:31:38,945 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:31:38,945 INFO     29 [qwen-vl-text] positions(23): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:31:38,945 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [23]
2026-08-10 19:31:39,129 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:31:39,130 INFO     29 [qwen-vl-text] LLM extraction start, text_len=444
2026-08-10 19:31:39,130 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:31:39,130 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 194, \"bbox_end\": 216, \"encounter_dates\": [\"2026-03-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "性别：男\n年龄：49岁\n门诊号：\n检查部位：肺部\n检查设备：GE-HD750\n流水号：0013240579\n检查技术：CT\n影像学所见：\n双肺纹理清晰，左肺下叶见团块软组织密度影，病灶内支气管闭塞，较大截面约7.6cm×\n8.3cm，增强扫描不均匀强化，周围散在条索斑片影。右肺散在小结节，大者右肺上叶尖段见一\n实性结节（Se4/Img46），大小约0.4cm×0.2cm。气管、余支气管通畅，纵隔及左肺门可见肿大\n淋巴结，大者短径约1.0cm，左侧胸腔少-中量积液，部分为包裹性。左侧胸膜结节状增厚。\n影像学诊断：\n1.左肺下叶肿块，考虑MT伴周围阻塞性肺炎，请结合临床。\n2.纵隔及左肺门肿大淋巴结，部分转移可能。\n3.左侧胸膜增厚，转移可能。\n4.右肺散在小结节，性质待定，建议随诊复查。\n5.左侧胸腔少-中量积液，部分为包裹性。\n报告医生：许志祥 /许志祥\n审核医生：沈东挥\n复核医生：\n此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。\n报告时间：2026-03-18",
    "role": "user"
  }
]
2026-08-10 19:31:39,132 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:31:39.131+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 91, "failed": 0, "current": {"14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:31:50,303 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:31:50,303 INFO     29 [qwen-vl-text] LLM output (len=600):
{
  "exam_date": "2026-03-18",
  "report_date": "2026-03-18",
  "exam_name": "CT",
  "exam_category": "imaging",
  "body_part": "肺部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "双肺纹理清晰，左肺下叶见团块软组织密度影，病灶内支气管闭塞，较大截面约7.6cm×8.3cm，增强扫描不均匀强化，周围散在条索斑片影。右肺散在小结节，大者右肺上叶尖段见一实性结节（Se4/Img46），大小约0.4cm×0.2cm。气管、余支气管通畅，纵隔及左肺门可见肿大淋巴结，大者短径约1.0cm，左侧胸腔少-中量积液，部分为包裹性。左侧胸膜结节状增厚。",
  "conclusion": "1.左肺下叶肿块，考虑MT伴周围阻塞性肺炎，请结合临床。\n2.纵隔及左肺门肿大淋巴结，部分转移可能。\n3.左侧胸膜增厚，转移可能。\n4.右肺散在小结节，性质待定，建议随诊复查。\n5.左侧胸腔少-中量积液，部分为包裹性。",
  "physician": "许志祥",
  "reviewer": "沈东挥"
}
2026-08-10 19:31:50,306 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=707617, prompt_len=1126
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["性别：男", "年龄：49岁", "门诊号：", "检查部位：肺部", "检查设备：GE-HD750", "流水号：0013240579", "检查技术：CT", "影像学所见：", "双肺纹理清晰，左肺下叶见团块软组织密度影，病灶内支气管闭塞，较大截面约7.6cm×", "8.3cm，增强扫描不均匀强化，周围散在条索斑片影。右肺散在小结节，大者右肺上叶尖段见一", "实性结节（Se4/Img46），大小约0.4cm×0.2cm。气管、余支气管通畅，纵隔及左肺门可见肿大", "淋巴结，大者短径约1.0cm，左侧胸腔少-中量积液，部分为包裹性。左侧胸膜结节状增厚。", "影像学诊断：", "1.左肺下叶肿块，考虑MT伴周围阻塞性肺炎，请结合临床。", "2.纵隔及左肺门肿大淋巴结，部分转移可能。", "3.左侧胸膜增厚，转移可能。", "4.右肺散在小结节，性质待定，建议随诊复查。", "5.左侧胸腔少-中量积液，部分为包裹性。", "报告医生：许志祥 /许志祥", "审核医生：沈东挥", "复核医生：", "此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。", "报告时间：2026-03-18"]

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
2026-08-10 19:31:58,514 INFO     29 [qwen-vl-text] coord API raw response (len=1465):
[
	{"text": "性别：男", "bbox": [286, 23, 380, 41]},
	{"text": "年龄：49岁", "bbox": [487, 23, 644, 41]},
	{"text": "门诊号：", "bbox": [717, 23, 793, 41]},
	{"text": "检查部位：肺部", "bbox": [48, 92, 203, 110]},
	{"text": "检查设备：GE-HD750", "bbox": [487, 92, 686, 110], "bbox": [487, 92, 686, 110]},
	{"text": "流水号：0013240579", "bbox": [717, 92, 914, 110]},
	{"text": "检查技术：CT", "bbox": [45, 134, 209, 152]},
	{"text": "影像学所见：", "bbox": [45, 162, 185, 181]},
	{"text": "双肺纹理清晰，左肺下叶见团块软组织密度影，病灶内支气管闭塞，较大截面约7.6cm×", "bbox": [135, 202, 918, 220]},
	{"text": "8.3cm，增强扫描不均匀强化，周围散在条索斑片影。右肺散在小结节，大者右肺上叶尖段见一", "bbox": [94, 220, 941, 238]},
	{"text": "实性结节（Se4/Img46），大小约0.4cm×0.2cm。气管、余支气管通畅，纵隔及左肺门可见肿大", "bbox": [94, 238, 941, 256]},
	{"text": "淋巴结，大者短径约1.0cm，左侧胸腔少-中量积液，部分为包裹性。左侧胸膜结节状增厚。", "bbox": [94, 255, 900, 273]},
	{"text": "影像学诊断：", "bbox": [45, 539, 188, 559]},
	{"text": "1.左肺下叶肿块，考虑MT伴周围阻塞性肺炎，请结合临床。", "bbox": [96, 572, 614, 590]},
	{"text": "2.纵隔及左肺门肿大淋巴结，部分转移可能。", "bbox": [96, 590, 494, 607]},
	{"text": "3.左侧胸膜增厚，转移可能。", "bbox": [96, 607, 354, 624]},
	{"text": "4.右肺散在小结节，性质待定，建议随诊复查。", "bbox": [96, 624, 514, 642]},
	{"text": "5.左侧胸腔少-中量积液，部分为包裹性。", "bbox": [96, 641, 465, 659]},
	{"text": "报告医生：许志祥 /许志祥", "bbox": [57, 828, 328, 847]},
	{"text": "审核医生：沈东挥", "bbox": [383, 828, 555, 847]},
	{"text": "复核医生：", "bbox": [687, 828, 785, 847]},
	{"text": "此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。", "bbox": [45, 875, 559, 889]},
	{"text": "报告时间：2026-03-18", "bbox": [688, 875, 903, 893]}
]
2026-08-10 19:31:58,514 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=8.2s
2026-08-10 19:31:58,514 INFO     29 [qwen-vl-text] coord item[0]: text=性别：男, bbox=[286, 23, 380, 41]
2026-08-10 19:31:58,514 INFO     29 [qwen-vl-text] coord item[1]: text=年龄：49岁, bbox=[487, 23, 644, 41]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[2]: text=门诊号：, bbox=[717, 23, 793, 41]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[3]: text=检查部位：肺部, bbox=[48, 92, 203, 110]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[4]: text=检查设备：GE-HD750, bbox=[487, 92, 686, 110]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[5]: text=流水号：0013240579, bbox=[717, 92, 914, 110]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[6]: text=检查技术：CT, bbox=[45, 134, 209, 152]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[7]: text=影像学所见：, bbox=[45, 162, 185, 181]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[8]: text=双肺纹理清晰，左肺下叶见团块软组织密度影，病灶内支气管闭塞，较大截面约7.6cm×, bbox=[135, 202, 918, 220]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[9]: text=8.3cm，增强扫描不均匀强化，周围散在条索斑片影。右肺散在小结节，大者右肺上叶尖段见一, bbox=[94, 220, 941, 238]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[10]: text=实性结节（Se4/Img46），大小约0.4cm×0.2cm。气管、余支气管通畅，纵隔及左肺门可见肿大, bbox=[94, 238, 941, 256]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[11]: text=淋巴结，大者短径约1.0cm，左侧胸腔少-中量积液，部分为包裹性。左侧胸膜结节状增厚。, bbox=[94, 255, 900, 273]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[12]: text=影像学诊断：, bbox=[45, 539, 188, 559]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[13]: text=1.左肺下叶肿块，考虑MT伴周围阻塞性肺炎，请结合临床。, bbox=[96, 572, 614, 590]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[14]: text=2.纵隔及左肺门肿大淋巴结，部分转移可能。, bbox=[96, 590, 494, 607]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[15]: text=3.左侧胸膜增厚，转移可能。, bbox=[96, 607, 354, 624]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[16]: text=4.右肺散在小结节，性质待定，建议随诊复查。, bbox=[96, 624, 514, 642]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[17]: text=5.左侧胸腔少-中量积液，部分为包裹性。, bbox=[96, 641, 465, 659]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[18]: text=报告医生：许志祥 /许志祥, bbox=[57, 828, 328, 847]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[19]: text=审核医生：沈东挥, bbox=[383, 828, 555, 847]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[20]: text=复核医生：, bbox=[687, 828, 785, 847]
2026-08-10 19:31:58,515 INFO     29 [qwen-vl-text] coord item[21]: text=此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。, bbox=[45, 875, 559, 889]
2026-08-10 19:31:58,516 INFO     29 [qwen-vl-text] coord item[22]: text=报告时间：2026-03-18, bbox=[688, 875, 903, 893]
2026-08-10 19:31:58,516 INFO     29 [qwen-vl-text] page=4 — 23/23 coords, api_time=8.2s
2026-08-10 19:31:58,516 INFO     29 [qwen-vl-text] new_positions (23):
[[4, 170.17, 226.1, 19.366, 34.522], [4, 289.765, 383.18, 19.366, 34.522], [4, 426.615, 471.835, 19.366, 34.522], [4, 28.56, 120.785, 77.464, 92.61999999999999], [4, 289.765, 408.16999999999996, 77.464, 92.61999999999999], [4, 426.615, 543.8299999999999, 77.464, 92.61999999999999], [4, 26.775, 124.35499999999999, 112.828, 127.984], [4, 26.775, 110.07499999999999, 136.404, 152.402], [4, 80.325, 546.2099999999999, 170.084, 185.23999999999998], [4, 55.93, 559.895, 185.23999999999998, 200.396], [4, 55.93, 559.895, 200.396, 215.552], [4, 55.93, 535.5, 214.70999999999998, 229.86599999999999], [4, 26.775, 111.86, 453.83799999999997, 470.678], [4, 57.12, 365.33, 481.62399999999997, 496.78], [4, 57.12, 293.93, 496.78, 511.094], [4, 57.12, 210.63, 511.094, 525.408], [4, 57.12, 305.83, 525.408, 540.564], [4, 57.12, 276.675, 539.722, 554.8779999999999], [4, 33.915, 195.16, 697.1759999999999, 713.174], [4, 227.885, 330.22499999999997, 697.1759999999999, 713.174], [4, 408.765, 467.075, 697.1759999999999, 713.174], [4, 26.775, 332.60499999999996, 736.75, 748.538], [4, 409.35999999999996, 537.285, 736.75, 751.906]]
2026-08-10 19:31:58,516 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=19.6s
2026-08-10 19:31:58,516 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:31:58,518 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:31:58,518 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:31:58,518 INFO     29 [qwen-vl-text] positions(71): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:31:58,518 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [71]
2026-08-10 19:31:58,850 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 19:31:58,851 INFO     29 [qwen-vl-text] LLM extraction start, text_len=550
2026-08-10 19:31:58,851 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:31:58,851 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 219, \"bbox_end\": 289, \"encounter_dates\": [\"2026-03-17\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "门诊号:\n医院:\n申请医生\n申请科室\n检查日期: 2026-03-17 10:58:32\n检查医生\n报告日期: 2026-03-17 11:11:03\n报告医生: 蔡平\n审核日期: 2026-03-17 11:11:03\n审核医生: 蔡平\n电轴(-30~90°): 29\nQRS时限(<120): 100\nP-R间期(120~200): 134\nQ-T间期(0~450): 344\nQTc(0~450): 444\nSV1: 1.26\nRV5(0~2.5): 2.02\nR+S: 3.28\n心率(60~100): 100\n临床诊断: 肺肿物\n描述:\n诊断: 窦性心律 ST段改变\n报告状态 已审核\n检查项目: 心电图(常规十二通道)\n当前状态\n走纸: 25mm/s\n增益:10mm/mv\n当前模式:普通模式\n572\n596\n600\n600\n596\n600\n604\n600\n596\n596\n604\n604\n596\n25mm/s 10mm/mv\n105\n101\n100\n100\n101\n100\n100\n100\n101\n101\n100\n100\n101\n100\n100\n102\nII\nIII\naVR\naVL\naVF\nV1\nV2\nV3\nV4\nV5\nV6\n2026-03-17 10:59:32\n版权所有 纳龙科技",
    "role": "user"
  }
]
2026-08-10 19:32:10,693 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:32:10,693 INFO     29 [qwen-vl-text] LLM output (len=756):
{
  "exam_date": "2026-03-17",
  "report_date": "2026-03-17",
  "exam_name": "心电图(常规十二通道)",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "电轴(-30~90°): 29\nQRS时限(<120): 100\nP-R间期(120~200): 134\nQ-T间期(0~450): 344\nQTc(0~450): 444\nSV1: 1.26\nRV5(0~2.5): 2.02\nR+S: 3.28\n心率(60~100): 100\n临床诊断: 肺肿物\n描述:\n走纸: 25mm/s\n增益:10mm/mv\n当前模式:普通模式\n572\n596\n600\n600\n596\n600\n604\n600\n596\n596\n604\n604\n596\n25mm/s 10mm/mv\n105\n101\n100\n100\n101\n100\n100\n100\n101\n101\n100\n100\n101\n100\n100\n102\nII\nIII\naVR\naVL\naVF\nV1\nV2\nV3\nV4\nV5\nV6\n2026-03-17 10:59:32",
  "conclusion": "诊断: 窦性心律 ST段改变",
  "physician": "蔡平",
  "reviewer": "蔡平"
}
2026-08-10 19:32:10,697 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2709903, prompt_len=1376
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共71行）
["门诊号:", "医院:", "申请医生", "申请科室", "检查日期: 2026-03-17 10:58:32", "检查医生", "报告日期: 2026-03-17 11:11:03", "报告医生: 蔡平", "审核日期: 2026-03-17 11:11:03", "审核医生: 蔡平", "电轴(-30~90°): 29", "QRS时限(<120): 100", "P-R间期(120~200): 134", "Q-T间期(0~450): 344", "QTc(0~450): 444", "SV1: 1.26", "RV5(0~2.5): 2.02", "R+S: 3.28", "心率(60~100): 100", "临床诊断: 肺肿物", "描述:", "诊断: 窦性心律 ST段改变", "报告状态 已审核", "检查项目: 心电图(常规十二通道)", "当前状态", "走纸: 25mm/s", "增益:10mm/mv", "当前模式:普通模式", "572", "596", "600", "600", "596", "600", "604", "600", "596", "596", "604", "604", "596", "25mm/s 10mm/mv", "105", "101", "100", "100", "101", "100", "100", "100", "101", "101", "100", "100", "101", "100", "100", "102", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6", "2026-03-17 10:59:32", "版权所有 纳龙科技"]

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
2026-08-10 19:32:32,720 INFO     29 [qwen-vl-text] coord API raw response (len=3651):
[
	{"text": "门诊号:", "bbox": [535, 3, 564, 15]},
	{"text": "医院:", "bbox": [698, 3, 727, 15]},
	{"text": "申请医生", "bbox": [200, 40, 230, 52]},
	{"text": "申请科室", "bbox": [371, 40, 402, 52]},
	{"text": "检查日期: 2026-03-17 10:58:32", "bbox": [528, 39, 647, 51]},
	{"text": "检查医生", "bbox": [698, 40, 727, 52]},
	{"text": "报告日期: 2026-03-17 11:11:03", "bbox": [200, 71, 319, 83]},
	{"text": "报告医生: 蔡平", "bbox": [371, 71, 433, 83]},
	{"text": "审核日期: 2026-03-17 11:11:03", "bbox": [528, 71, 647, 83]},
	{"text": "审核医生: 蔡平", "bbox": [698, 71, 759, 83]},
	{"text": "电轴(-30~90°): 29", "bbox": [183, 97, 255, 109]},
	{"text": "QRS时限(<120): 100", "bbox": [350, 97, 430, 109]},
	{"text": "P-R间期(120~200): 134", "bbox": [496, 97, 587, 109]},
	{"text": "Q-T间期(0~450): 344", "bbox": [674, 97, 756, 109]},
	{"text": "QTc(0~450): 444", "bbox": [190, 122, 259, 134]},
	{"text": "SV1: 1.26", "bbox": [387, 122, 433, 134]},
	{"text": "RV5(0~2.5): 2.02", "bbox": [520, 122, 590, 134]},
	{"text": "R+S: 3.28", "bbox": [714, 122, 759, 134]},
	{"text": "心率(60~100): 100", "bbox": [184, 148, 259, 160]},
	{"text": "临床诊断: 肺肿物", "bbox": [371, 148, 441, 160]},
	{"text": "描述:", "bbox": [196, 175, 215, 187]},
	{"text": "诊断: 窦性心律 ST段改变", "bbox": [448, 175, 550, 187]},
	{"text": "报告状态 已审核", "bbox": [186, 199, 253, 211]},
	{"text": "检查项目: 心电图(常规十二通道)", "bbox": [667, 199, 788, 211]},
	{"text": "当前状态", "bbox": [185, 258, 214, 270]},
	{"text": "走纸: 25mm/s", "bbox": [226, 258, 270, 270]},
	{"text": "增益:10mm/mv", "bbox": [282, 258, 334, 270]},
	{"text": "当前模式:普通模式", "bbox": [346, 258, 405, 270]},
	{"text": "572", "bbox": [211, 277, 227, 289]},
	{"text": "596", "bbox": [247, 277, 264, 289]},
	{"text": "600", "bbox": [285, 277, 301, 289]},
	{"text": "600", "bbox": [322, 277, 339, 289]},
	{"text": "596", "bbox": [360, 277, 377, 289]},
	{"text": "600", "bbox": [397, 277, 414, 289]},
	{"text": "604", "bbox": [435, 277, 452, 289]},
	{"text": "600", "bbox": [472, 277, 489, 289]},
	{"text": "596", "bbox": [509, 277, 526, 289]},
	{"text": "596", "bbox": [546, 277, 563, 289]},
	{"text": "604", "bbox": [583, 277, 599, 289]},
	{"text": "604", "bbox": [620, 277, 637, 289]},
	{"text": "596", "bbox": [657, 277, 674, 289]},
	{"text": "25mm/s 10mm/mv", "bbox": [707, 277, 785, 289]},
	{"text": "105", "bbox": [211, 292, 227, 304]},
	{"text": "101", "bbox": [247, 292, 264, 304]},
	{"text": "100", "bbox": [285, 292, 301, 304]},
	{"text": "100", "bbox": [322, 292, 339, 304]},
	{"text": "101", "bbox": [360, 292, 377, 304]},
	{"text": "100", "bbox": [397, 292, 414, 304]},
	{"text": "100", "bbox": [435, 292, 452, 304]},
	{"text": "100", "bbox": [472, 292, 489, 304]},
	{"text": "101", "bbox": [509, 292, 526, 304]},
	{"text": "101", "bbox": [546, 292, 563, 304]},
	{"text": "100", "bbox": [583, 292, 599, 304]},
	{"text": "100", "bbox": [620, 292, 637, 304]},
	{"text": "101", "bbox": [657, 292, 674, 304]},
	{"text": "100", "bbox": [695, 292, 711, 304]},
	{"text": "100", "bbox": [732, 292, 749, 304]},
	{"text": "102", "bbox": [769, 292, 785, 304]},
	{"text": "II", "bbox": [198, 369, 208, 381]},
	{"text": "III", "bbox": [198, 417, 210, 429]},
	{"text": "aVR", "bbox": [200, 467, 217, 479]},
	{"text": "aVL", "bbox": [200, 517, 216, 529]},
	{"text": "aVF", "bbox": [200, 567, 217, 579]},
	{"text": "V1", "bbox": [202, 617, 211, 629]},
	{"text": "V2", "bbox": [202, 667, 211, 679]},
	{"text": "V3", "bbox": [202, 717, 211, 729]},
	{"text": "V4", "bbox": [202, 767, 211, 779]},
	{"text": "V5", "bbox": [202, 817, 211, 829]},
	{"text": "V6", "bbox": [202, 867, 211, 879]},
	{"text": "2026-03-17 10:59:32", "bbox": [704, 857, 790, 869]},
	{"text": "版权所有 纳龙科技", "bbox": [174, 903, 240, 915]}
]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord API: raw_items=71, valid_items=71, elapsed=22.0s
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号:, bbox=[535, 3, 564, 15]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[1]: text=医院:, bbox=[698, 3, 727, 15]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[2]: text=申请医生, bbox=[200, 40, 230, 52]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[3]: text=申请科室, bbox=[371, 40, 402, 52]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[4]: text=检查日期: 2026-03-17 10:58:32, bbox=[528, 39, 647, 51]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[5]: text=检查医生, bbox=[698, 40, 727, 52]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[6]: text=报告日期: 2026-03-17 11:11:03, bbox=[200, 71, 319, 83]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[7]: text=报告医生: 蔡平, bbox=[371, 71, 433, 83]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[8]: text=审核日期: 2026-03-17 11:11:03, bbox=[528, 71, 647, 83]
2026-08-10 19:32:32,722 INFO     29 [qwen-vl-text] coord item[9]: text=审核医生: 蔡平, bbox=[698, 71, 759, 83]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[10]: text=电轴(-30~90°): 29, bbox=[183, 97, 255, 109]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[11]: text=QRS时限(<120): 100, bbox=[350, 97, 430, 109]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[12]: text=P-R间期(120~200): 134, bbox=[496, 97, 587, 109]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[13]: text=Q-T间期(0~450): 344, bbox=[674, 97, 756, 109]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[14]: text=QTc(0~450): 444, bbox=[190, 122, 259, 134]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[15]: text=SV1: 1.26, bbox=[387, 122, 433, 134]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[16]: text=RV5(0~2.5): 2.02, bbox=[520, 122, 590, 134]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[17]: text=R+S: 3.28, bbox=[714, 122, 759, 134]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[18]: text=心率(60~100): 100, bbox=[184, 148, 259, 160]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[19]: text=临床诊断: 肺肿物, bbox=[371, 148, 441, 160]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[20]: text=描述:, bbox=[196, 175, 215, 187]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[21]: text=诊断: 窦性心律 ST段改变, bbox=[448, 175, 550, 187]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[22]: text=报告状态 已审核, bbox=[186, 199, 253, 211]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[23]: text=检查项目: 心电图(常规十二通道), bbox=[667, 199, 788, 211]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[24]: text=当前状态, bbox=[185, 258, 214, 270]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[25]: text=走纸: 25mm/s, bbox=[226, 258, 270, 270]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[26]: text=增益:10mm/mv, bbox=[282, 258, 334, 270]
2026-08-10 19:32:32,723 INFO     29 [qwen-vl-text] coord item[27]: text=当前模式:普通模式, bbox=[346, 258, 405, 270]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[28]: text=572, bbox=[211, 277, 227, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[29]: text=596, bbox=[247, 277, 264, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[30]: text=600, bbox=[285, 277, 301, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[31]: text=600, bbox=[322, 277, 339, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[32]: text=596, bbox=[360, 277, 377, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[33]: text=600, bbox=[397, 277, 414, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[34]: text=604, bbox=[435, 277, 452, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[35]: text=600, bbox=[472, 277, 489, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[36]: text=596, bbox=[509, 277, 526, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[37]: text=596, bbox=[546, 277, 563, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[38]: text=604, bbox=[583, 277, 599, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[39]: text=604, bbox=[620, 277, 637, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[40]: text=596, bbox=[657, 277, 674, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[41]: text=25mm/s 10mm/mv, bbox=[707, 277, 785, 289]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[42]: text=105, bbox=[211, 292, 227, 304]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[43]: text=101, bbox=[247, 292, 264, 304]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[44]: text=100, bbox=[285, 292, 301, 304]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[45]: text=100, bbox=[322, 292, 339, 304]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[46]: text=101, bbox=[360, 292, 377, 304]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[47]: text=100, bbox=[397, 292, 414, 304]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[48]: text=100, bbox=[435, 292, 452, 304]
2026-08-10 19:32:32,724 INFO     29 [qwen-vl-text] coord item[49]: text=100, bbox=[472, 292, 489, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[50]: text=101, bbox=[509, 292, 526, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[51]: text=101, bbox=[546, 292, 563, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[52]: text=100, bbox=[583, 292, 599, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[53]: text=100, bbox=[620, 292, 637, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[54]: text=101, bbox=[657, 292, 674, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[55]: text=100, bbox=[695, 292, 711, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[56]: text=100, bbox=[732, 292, 749, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[57]: text=102, bbox=[769, 292, 785, 304]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[58]: text=II, bbox=[198, 369, 208, 381]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[59]: text=III, bbox=[198, 417, 210, 429]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[60]: text=aVR, bbox=[200, 467, 217, 479]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[61]: text=aVL, bbox=[200, 517, 216, 529]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[62]: text=aVF, bbox=[200, 567, 217, 579]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[63]: text=V1, bbox=[202, 617, 211, 629]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[64]: text=V2, bbox=[202, 667, 211, 679]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[65]: text=V3, bbox=[202, 717, 211, 729]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[66]: text=V4, bbox=[202, 767, 211, 779]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[67]: text=V5, bbox=[202, 817, 211, 829]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[68]: text=V6, bbox=[202, 867, 211, 879]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[69]: text=2026-03-17 10:59:32, bbox=[704, 857, 790, 869]
2026-08-10 19:32:32,725 INFO     29 [qwen-vl-text] coord item[70]: text=版权所有 纳龙科技, bbox=[174, 903, 240, 915]
2026-08-10 19:32:32,727 INFO     29 [qwen-vl-text] page=5 — 71/71 coords, api_time=22.0s
2026-08-10 19:32:32,727 INFO     29 [qwen-vl-text] new_positions (71):
[[5, 450.46999999999997, 474.888, 1.785, 8.924999999999999], [5, 587.716, 612.134, 1.785, 8.924999999999999], [5, 168.4, 193.66, 23.799999999999997, 30.939999999999998], [5, 312.382, 338.484, 23.799999999999997, 30.939999999999998], [5, 444.57599999999996, 544.774, 23.205, 30.345], [5, 587.716, 612.134, 23.799999999999997, 30.939999999999998], [5, 168.4, 268.598, 42.245, 49.385], [5, 312.382, 364.586, 42.245, 49.385], [5, 444.57599999999996, 544.774, 42.245, 49.385], [5, 587.716, 639.078, 42.245, 49.385], [5, 154.08599999999998, 214.70999999999998, 57.714999999999996, 64.855], [5, 294.7, 362.06, 57.714999999999996, 64.855], [5, 417.632, 494.25399999999996, 57.714999999999996, 64.855], [5, 567.5079999999999, 636.552, 57.714999999999996, 64.855], [5, 159.98, 218.078, 72.59, 79.72999999999999], [5, 325.854, 364.586, 72.59, 79.72999999999999], [5, 437.84, 496.78, 72.59, 79.72999999999999], [5, 601.188, 639.078, 72.59, 79.72999999999999], [5, 154.928, 218.078, 88.06, 95.19999999999999], [5, 312.382, 371.322, 88.06, 95.19999999999999], [5, 165.03199999999998, 181.03, 104.125, 111.265], [5, 377.216, 463.09999999999997, 104.125, 111.265], [5, 156.612, 213.02599999999998, 118.405, 125.54499999999999], [5, 561.614, 663.496, 118.405, 125.54499999999999], [5, 155.76999999999998, 180.188, 153.51, 160.65], [5, 190.292, 227.34, 153.51, 160.65], [5, 237.444, 281.228, 153.51, 160.65], [5, 291.332, 341.01, 153.51, 160.65], [5, 177.662, 191.134, 164.815, 171.95499999999998], [5, 207.974, 222.28799999999998, 164.815, 171.95499999999998], [5, 239.97, 253.44199999999998, 164.815, 171.95499999999998], [5, 271.12399999999997, 285.438, 164.815, 171.95499999999998], [5, 303.12, 317.43399999999997, 164.815, 171.95499999999998], [5, 334.274, 348.58799999999997, 164.815, 171.95499999999998], [5, 366.27, 380.584, 164.815, 171.95499999999998], [5, 397.424, 411.738, 164.815, 171.95499999999998], [5, 428.578, 442.892, 164.815, 171.95499999999998], [5, 459.73199999999997, 474.046, 164.815, 171.95499999999998], [5, 490.88599999999997, 504.358, 164.815, 171.95499999999998], [5, 522.04, 536.3539999999999, 164.815, 171.95499999999998], [5, 553.194, 567.5079999999999, 164.815, 171.95499999999998], [5, 595.294, 660.97, 164.815, 171.95499999999998], [5, 177.662, 191.134, 173.73999999999998, 180.88], [5, 207.974, 222.28799999999998, 173.73999999999998, 180.88], [5, 239.97, 253.44199999999998, 173.73999999999998, 180.88], [5, 271.12399999999997, 285.438, 173.73999999999998, 180.88], [5, 303.12, 317.43399999999997, 173.73999999999998, 180.88], [5, 334.274, 348.58799999999997, 173.73999999999998, 180.88], [5, 366.27, 380.584, 173.73999999999998, 180.88], [5, 397.424, 411.738, 173.73999999999998, 180.88], [5, 428.578, 442.892, 173.73999999999998, 180.88], [5, 459.73199999999997, 474.046, 173.73999999999998, 180.88], [5, 490.88599999999997, 504.358, 173.73999999999998, 180.88], [5, 522.04, 536.3539999999999, 173.73999999999998, 180.88], [5, 553.194, 567.5079999999999, 173.73999999999998, 180.88], [5, 585.1899999999999, 598.662, 173.73999999999998, 180.88], [5, 616.3439999999999, 630.658, 173.73999999999998, 180.88], [5, 647.4979999999999, 660.97, 173.73999999999998, 180.88], [5, 166.716, 175.136, 219.55499999999998, 226.695], [5, 166.716, 176.82, 248.11499999999998, 255.255], [5, 168.4, 182.714, 277.865, 285.005], [5, 168.4, 181.87199999999999, 307.615, 314.755], [5, 168.4, 182.714, 337.365, 344.505], [5, 170.084, 177.662, 367.115, 374.255], [5, 170.084, 177.662, 396.865, 404.005], [5, 170.084, 177.662, 426.615, 433.755], [5, 170.084, 177.662, 456.36499999999995, 463.505], [5, 170.084, 177.662, 486.11499999999995, 493.255], [5, 170.084, 177.662, 515.865, 523.005], [5, 592.768, 665.18, 509.91499999999996, 517.055], [5, 146.50799999999998, 202.07999999999998, 537.285, 544.425]]
2026-08-10 19:32:32,727 INFO     29 [qwen-vl-text] ═══ DONE ═══ 71 positions, pages=1, time=34.2s
2026-08-10 19:32:32,727 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:32:32,729 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:32:32,729 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:32:32,729 INFO     29 [qwen-vl-text] positions(16): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:32:32,729 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [16]
2026-08-10 19:32:32,900 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:32:32,901 INFO     29 [qwen-vl-text] LLM extraction start, text_len=290
2026-08-10 19:32:32,901 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:32:32,902 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 290, \"bbox_end\": 305, \"encounter_dates\": [\"2026-03-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "检查部位：头颅\n检查设备：飞利浦MR9 流水号：0013240580\n检查技术：MR\n检查参数：\n影像学所见：\n双侧大脑半球对称，灰白质对比正常，实质内未见明显异常信号，DWI未见异常高信号，SW\nI未见异常低信号，各脑沟、脑池未见增宽、变深，脑室系统未见增宽，中线结构居中，幕下小\n脑、脑干未见异常信号，双侧桥小脑角区未见明显异常。颅骨骨质未见异常信号。增强后未见\n明显强化。\n影像学诊断：\n颅脑MRI平扫及增强未见明显异常。\n报告医生：林佳辉 /林佳辉\n审核医生：陈明宏\n复核医生：\n此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。\n报告时间：2026-03-19",
    "role": "user"
  }
]
2026-08-10 19:32:32,904 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:32:32.903+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 91, "failed": 0, "current": {"14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:32:39,783 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:32:39,783 INFO     29 [qwen-vl-text] LLM output (len=464):
{
  "exam_date": "2026-03-19",
  "report_date": "2026-03-19",
  "exam_name": "颅脑MRI平扫及增强",
  "exam_category": "imaging",
  "body_part": "头颅",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "双侧大脑半球对称，灰白质对比正常，实质内未见明显异常信号，DWI未见异常高信号，SWI未见异常低信号，各脑沟、脑池未见增宽、变深，脑室系统未见增宽，中线结构居中，幕下小脑、脑干未见异常信号，双侧桥小脑角区未见明显异常。颅骨骨质未见异常信号。增强后未见明显强化。",
  "conclusion": "颅脑MRI平扫及增强未见明显异常。",
  "physician": "林佳辉",
  "reviewer": "陈明宏"
}
2026-08-10 19:32:39,784 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=489716, prompt_len=951
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["检查部位：头颅", "检查设备：飞利浦MR9 流水号：0013240580", "检查技术：MR", "检查参数：", "影像学所见：", "双侧大脑半球对称，灰白质对比正常，实质内未见明显异常信号，DWI未见异常高信号，SW", "I未见异常低信号，各脑沟、脑池未见增宽、变深，脑室系统未见增宽，中线结构居中，幕下小", "脑、脑干未见异常信号，双侧桥小脑角区未见明显异常。颅骨骨质未见异常信号。增强后未见", "明显强化。", "影像学诊断：", "颅脑MRI平扫及增强未见明显异常。", "报告医生：林佳辉 /林佳辉", "审核医生：陈明宏", "复核医生：", "此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。", "报告时间：2026-03-19"]

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
2026-08-10 19:32:45,663 INFO     29 [qwen-vl-text] coord API raw response (len=988):
[
	{"text": "检查部位：头颅", "bbox": [54, 83, 210, 102]},
	{"text": "检查设备：飞利浦MR9 流水号：0013240580", "bbox": [497, 83, 917, 100]},
	{"text": "检查技术：MR", "bbox": [53, 119, 217, 138]},
	{"text": "检查参数：", "bbox": [53, 151, 167, 171]},
	{"text": "影像学所见：", "bbox": [53, 181, 194, 201]},
	{"text": "双侧大脑半球对称，灰白质对比正常，实质内未见明显异常信号，DWI未见异常高信号，SW", "bbox": [140, 215, 947, 234]},
	{"text": "I未见异常低信号，各脑沟、脑池未见增宽、变深，脑室系统未见增宽，中线结构居中，幕下小", "bbox": [102, 233, 946, 252]},
	{"text": "脑、脑干未见异常信号，双侧桥小脑角区未见明显异常。颅骨骨质未见异常信号。增强后未见", "bbox": [102, 251, 936, 270]},
	{"text": "明显强化。", "bbox": [102, 268, 200, 287]},
	{"text": "影像学诊断：", "bbox": [53, 562, 195, 582]},
	{"text": "颅脑MRI平扫及增强未见明显异常。", "bbox": [103, 595, 412, 614]},
	{"text": "报告医生：林佳辉 /林佳辉", "bbox": [60, 819, 332, 838]},
	{"text": "审核医生：陈明宏", "bbox": [387, 819, 558, 838]},
	{"text": "复核医生：", "bbox": [690, 819, 788, 838]},
	{"text": "此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。", "bbox": [57, 867, 567, 880]},
	{"text": "报告时间：2026-03-19", "bbox": [690, 867, 906, 884]}
]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.9s
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[0]: text=检查部位：头颅, bbox=[54, 83, 210, 102]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[1]: text=检查设备：飞利浦MR9 流水号：0013240580, bbox=[497, 83, 917, 100]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[2]: text=检查技术：MR, bbox=[53, 119, 217, 138]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[3]: text=检查参数：, bbox=[53, 151, 167, 171]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[4]: text=影像学所见：, bbox=[53, 181, 194, 201]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[5]: text=双侧大脑半球对称，灰白质对比正常，实质内未见明显异常信号，DWI未见异常高信号，SW, bbox=[140, 215, 947, 234]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[6]: text=I未见异常低信号，各脑沟、脑池未见增宽、变深，脑室系统未见增宽，中线结构居中，幕下小, bbox=[102, 233, 946, 252]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[7]: text=脑、脑干未见异常信号，双侧桥小脑角区未见明显异常。颅骨骨质未见异常信号。增强后未见, bbox=[102, 251, 936, 270]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[8]: text=明显强化。, bbox=[102, 268, 200, 287]
2026-08-10 19:32:45,664 INFO     29 [qwen-vl-text] coord item[9]: text=影像学诊断：, bbox=[53, 562, 195, 582]
2026-08-10 19:32:45,665 INFO     29 [qwen-vl-text] coord item[10]: text=颅脑MRI平扫及增强未见明显异常。, bbox=[103, 595, 412, 614]
2026-08-10 19:32:45,665 INFO     29 [qwen-vl-text] coord item[11]: text=报告医生：林佳辉 /林佳辉, bbox=[60, 819, 332, 838]
2026-08-10 19:32:45,665 INFO     29 [qwen-vl-text] coord item[12]: text=审核医生：陈明宏, bbox=[387, 819, 558, 838]
2026-08-10 19:32:45,665 INFO     29 [qwen-vl-text] coord item[13]: text=复核医生：, bbox=[690, 819, 788, 838]
2026-08-10 19:32:45,665 INFO     29 [qwen-vl-text] coord item[14]: text=此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。, bbox=[57, 867, 567, 880]
2026-08-10 19:32:45,665 INFO     29 [qwen-vl-text] coord item[15]: text=报告时间：2026-03-19, bbox=[690, 867, 906, 884]
2026-08-10 19:32:45,665 INFO     29 [qwen-vl-text] page=6 — 16/16 coords, api_time=5.9s
2026-08-10 19:32:45,666 INFO     29 [qwen-vl-text] new_positions (16):
[[6, 32.129999999999995, 124.94999999999999, 69.886, 85.884], [6, 295.715, 545.615, 69.886, 84.2], [6, 31.535, 129.11499999999998, 100.198, 116.196], [6, 31.535, 99.365, 127.142, 143.982], [6, 31.535, 115.42999999999999, 152.402, 169.242], [6, 83.3, 563.4649999999999, 181.03, 197.028], [6, 60.69, 562.87, 196.186, 212.184], [6, 60.69, 556.92, 211.34199999999998, 227.34], [6, 60.69, 119.0, 225.656, 241.654], [6, 31.535, 116.02499999999999, 473.204, 490.044], [6, 61.285, 245.14, 500.99, 516.9879999999999], [6, 35.699999999999996, 197.54, 689.598, 705.596], [6, 230.265, 332.01, 689.598, 705.596], [6, 410.54999999999995, 468.85999999999996, 689.598, 705.596], [6, 33.915, 337.365, 730.014, 740.9599999999999], [6, 410.54999999999995, 539.0699999999999, 730.014, 744.328]]
2026-08-10 19:32:45,666 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=12.9s
2026-08-10 19:32:45,666 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:32:45,677 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:32:45,677 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:32:45,677 INFO     29 [qwen-vl-text] positions(43): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:32:45,677 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [43]
2026-08-10 19:32:45,943 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:32:45,945 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1236
2026-08-10 19:32:45,946 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:32:45,946 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 427, \"bbox_end\": 469, \"encounter_dates\": [\"2026-03-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "病案号:\n11诊号:1K3392539b3\n血型:FEI/CI独|业冰(111)\n显像剂:18F-FDG\n血糖:5.1mmol/l活\n度:7.22mci注射部位:右手背静脉\n注射/显像间隔时间:54分钟采集方式:断层采集3D厚\n度:3.75mm采集仪器:Discovery MI\n临床诊断:肺部阴影\n简要病史:\n肺部鳞癌基线评估。既往:2025.12肋骨骨折。\n图像所见:\n空腹4hr以上,口服适量温水,静脉注射显像剂,平静休息后行躯干PET及CT断层显像,PET图像行衰减校正及迭代\n法重建,PET、CT图像行多层面、多幅显示,影像清晰。\n颈部PET/CT示眼球、眼眶、鼻咽部、颈面部、喉咽部、甲状腺及颈部其它软组织结构、密度、代谢分布未见明显\n异常。\n胸部PET/CT示左肺下叶基底段近肺门部见高代谢结节,大小约2.0cm×1.9cm,边界不清,SUVmax约10.2。左肺\n下叶远端见散在片絮状高密度影。左侧胸腔积液,部分呈包裹性。左侧胸膜见不均匀增厚,伴代谢增高,SUVmax约\n4.0。右肺上叶胸膜下见微小结节,直径约0.2cm,代谢未见异常增高。主动脉、心脏生理性显像。\n腹盆部PET/CT示肝左内叶包膜下见高代谢结节,SUVmax约5.4,CT显示密度轻微减低,边界不清。左侧肾上腺见\n高代谢小结节,SUVmax约3.2,CT扫描局部稍增厚。胆囊、脾脏、胰腺大小正常,未见异常密度和异常代谢影。十二指\n肠、双肾、右肾上腺、双输尿管、膀胱、前列腺及双侧精囊腺未见异常显像。腹腔内见多个形态不一、条管状、浓淡不\n一的正常肠影。\n淋巴结PET/CT示左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧锁骨区见多发淋巴结增大伴代谢增\n高,较大者位于纵隔7组,大小约3.2×1.0cm,SUVmax约3.3。\n骨骼、软组织及周围神经走行区PET/CT示左侧第8、9、10、11肋骨、右侧第6肋骨见骨质中断,部分伴骨赘形\n成,伴代谢增高,SUVmax约3.8。左侧腹横肌见结节状增厚伴高代谢,SUVmax约2.9。全身其余骨骼、软组织及周围神\n经未见异常代谢影像,骨质和肌肉密度未见明显改变。\nI\n诊断意见:\n1.左肺下叶基底段近肺门部MT;左侧胸膜弥漫种植转移;左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧\n锁骨区多发淋巴结增大伴高代谢,考虑转移可能;肝S4包膜下转移瘤;左下叶远端阻塞性炎症;左胸腔癌性胸水可能\n大;\n2.左侧腹横肌转移瘤待除;左侧肾上腺转移待除,建议定期复查;\n3.右肺上叶胸膜下少许炎性小结节;肝右叶少许小钙化灶;\n4.双侧多根肋骨骨折伴骨赘区域炎性摄取;\n5.全身其它部位18F-FDG PET/CT显像未见明显异常。\n报告医师:林晓强\n审核医师:\n复核医师:\n报告日期:2026-03-18\n地址:福州市鼓楼区新权路29号电话:0591-833116130591-86218247\n此报告仅供临床医师参考,不做证明使用。",
    "role": "user"
  }
]
2026-08-10 19:33:03,948 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:33:03,948 INFO     29 [qwen-vl-text] LLM output (len=1285):
{
  "exam_date": "2026-03-18",
  "report_date": "2026-03-18",
  "exam_name": "PET/CT",
  "exam_category": "imaging",
  "body_part": "躯干",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "图像所见:\n空腹4hr以上,口服适量温水,静脉注射显像剂,平静休息后行躯干PET及CT断层显像,PET图像行衰减校正及迭代\n法重建,PET、CT图像行多层面、多幅显示,影像清晰。\n颈部PET/CT示眼球、眼眶、鼻咽部、颈面部、喉咽部、甲状腺及颈部其它软组织结构、密度、代谢分布未见明显\n异常。\n胸部PET/CT示左肺下叶基底段近肺门部见高代谢结节,大小约2.0cm×1.9cm,边界不清,SUVmax约10.2。左肺\n下叶远端见散在片絮状高密度影。左侧胸腔积液,部分呈包裹性。左侧胸膜见不均匀增厚,伴代谢增高,SUVmax约\n4.0。右肺上叶胸膜下见微小结节,直径约0.2cm,代谢未见异常增高。主动脉、心脏生理性显像。\n腹盆部PET/CT示肝左内叶包膜下见高代谢结节,SUVmax约5.4,CT显示密度轻微减低,边界不清。左侧肾上腺见\n高代谢小结节,SUVmax约3.2,CT扫描局部稍增厚。胆囊、脾脏、胰腺大小正常,未见异常密度和异常代谢影。十二指\n肠、双肾、右肾上腺、双输尿管、膀胱、前列腺及双侧精囊腺未见异常显像。腹腔内见多个形态不一、条管状、浓淡不\n一的正常肠影。\n淋巴结PET/CT示左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧锁骨区见多发淋巴结增大伴代谢增\n高,较大者位于纵隔7组,大小约3.2×1.0cm,SUVmax约3.3。\n骨骼、软组织及周围神经走行区PET/CT示左侧第8、9、10、11肋骨、右侧第6肋骨见骨质中断,部分伴骨赘形\n成,伴代谢增高,SUVmax约3.8。左侧腹横肌见结节状增厚伴高代谢,SUVmax约2.9。全身其余骨骼、软组织及周围神\n经未见异常代谢影像,骨质和肌肉密度未见明显改变。",
  "conclusion": "诊断意见:\n1.左肺下叶基底段近肺门部MT;左侧胸膜弥漫种植转移;左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧\n锁骨区多发淋巴结增大伴高代谢,考虑转移可能;肝S4包膜下转移瘤;左下叶远端阻塞性炎症;左胸腔癌性胸水可能\n大;\n2.左侧腹横肌转移瘤待除;左侧肾上腺转移待除,建议定期复查;\n3.右肺上叶胸膜下少许炎性小结节;肝右叶少许小钙化灶;\n4.双侧多根肋骨骨折伴骨赘区域炎性摄取;\n5.全身其它部位18F-FDG PET/CT显像未见明显异常。",
  "physician": "林晓强",
  "reviewer": null
}
2026-08-10 19:33:03,954 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1774828, prompt_len=1978
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["病案号:", "11诊号:1K3392539b3", "血型:FEI/CI独|业冰(111)", "显像剂:18F-FDG", "血糖:5.1mmol/l活", "度:7.22mci注射部位:右手背静脉", "注射/显像间隔时间:54分钟采集方式:断层采集3D厚", "度:3.75mm采集仪器:Discovery MI", "临床诊断:肺部阴影", "简要病史:", "肺部鳞癌基线评估。既往:2025.12肋骨骨折。", "图像所见:", "空腹4hr以上,口服适量温水,静脉注射显像剂,平静休息后行躯干PET及CT断层显像,PET图像行衰减校正及迭代", "法重建,PET、CT图像行多层面、多幅显示,影像清晰。", "颈部PET/CT示眼球、眼眶、鼻咽部、颈面部、喉咽部、甲状腺及颈部其它软组织结构、密度、代谢分布未见明显", "异常。", "胸部PET/CT示左肺下叶基底段近肺门部见高代谢结节,大小约2.0cm×1.9cm,边界不清,SUVmax约10.2。左肺", "下叶远端见散在片絮状高密度影。左侧胸腔积液,部分呈包裹性。左侧胸膜见不均匀增厚,伴代谢增高,SUVmax约", "4.0。右肺上叶胸膜下见微小结节,直径约0.2cm,代谢未见异常增高。主动脉、心脏生理性显像。", "腹盆部PET/CT示肝左内叶包膜下见高代谢结节,SUVmax约5.4,CT显示密度轻微减低,边界不清。左侧肾上腺见", "高代谢小结节,SUVmax约3.2,CT扫描局部稍增厚。胆囊、脾脏、胰腺大小正常,未见异常密度和异常代谢影。十二指", "肠、双肾、右肾上腺、双输尿管、膀胱、前列腺及双侧精囊腺未见异常显像。腹腔内见多个形态不一、条管状、浓淡不", "一的正常肠影。", "淋巴结PET/CT示左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧锁骨区见多发淋巴结增大伴代谢增", "高,较大者位于纵隔7组,大小约3.2×1.0cm,SUVmax约3.3。", "骨骼、软组织及周围神经走行区PET/CT示左侧第8、9、10、11肋骨、右侧第6肋骨见骨质中断,部分伴骨赘形", "成,伴代谢增高,SUVmax约3.8。左侧腹横肌见结节状增厚伴高代谢,SUVmax约2.9。全身其余骨骼、软组织及周围神", "经未见异常代谢影像,骨质和肌肉密度未见明显改变。", "I", "诊断意见:", "1.左肺下叶基底段近肺门部MT;左侧胸膜弥漫种植转移;左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧", "锁骨区多发淋巴结增大伴高代谢,考虑转移可能;肝S4包膜下转移瘤;左下叶远端阻塞性炎症;左胸腔癌性胸水可能", "大;", "2.左侧腹横肌转移瘤待除;左侧肾上腺转移待除,建议定期复查;", "3.右肺上叶胸膜下少许炎性小结节;肝右叶少许小钙化灶;", "4.双侧多根肋骨骨折伴骨赘区域炎性摄取;", "5.全身其它部位18F-FDG PET/CT显像未见明显异常。", "报告医师:林晓强", "审核医师:", "复核医师:", "报告日期:2026-03-18", "地址:福州市鼓楼区新权路29号电话:0591-833116130591-86218247", "此报告仅供临床医师参考,不做证明使用。"]

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
2026-08-10 19:33:22,372 INFO     29 [qwen-vl-text] coord API raw response (len=3084):
[
	{"text": "病案号:", "bbox": [40, 63, 115, 76]},
	{"text": "11诊号:1K3392539b3", "bbox": [304, 63, 494, 75]},
	{"text": "血型:FEI/CI独|业冰(111)", "bbox": [510, 64, 793, 75]},
	{"text": "显像剂:18F-FDG", "bbox": [40, 85, 200, 98]},
	{"text": "血糖:5.1mmol/l活", "bbox": [304, 84, 527, 98]},
	{"text": "度:7.22mci注射部位:右手背静脉", "bbox": [563, 84, 880, 98]},
	{"text": "注射/显像间隔时间:54分钟采集方式:断层采集3D厚", "bbox": [40, 106, 527, 120]},
	{"text": "度:3.75mm采集仪器:Discovery MI", "bbox": [563, 106, 910, 120]},
	{"text": "临床诊断:肺部阴影", "bbox": [40, 128, 196, 142]},
	{"text": "简要病史:", "bbox": [40, 162, 153, 180]},
	{"text": "肺部鳞癌基线评估。既往:2025.12肋骨骨折。", "bbox": [64, 188, 417, 202]},
	{"text": "图像所见:", "bbox": [40, 209, 153, 228]},
	{"text": "空腹4hr以上,口服适量温水,静脉注射显像剂,平静休息后行躯干PET及CT断层显像,PET图像行衰减校正及迭代", "bbox": [64, 235, 934, 249]},
	{"text": "法重建,PET、CT图像行多层面、多幅显示,影像清晰。", "bbox": [64, 250, 473, 264]},
	{"text": "颈部PET/CT示眼球、眼眶、鼻咽部、颈面部、喉咽部、甲状腺及颈部其它软组织结构、密度、代谢分布未见明显", "bbox": [64, 266, 932, 280]},
	{"text": "异常。", "bbox": [64, 281, 109, 295]},
	{"text": "胸部PET/CT示左肺下叶基底段近肺门部见高代谢结节,大小约2.0cm×1.9cm,边界不清,SUVmax约10.2。左肺", "bbox": [64, 297, 928, 311]},
	{"text": "下叶远端见散在片絮状高密度影。左侧胸腔积液,部分呈包裹性。左侧胸膜见不均匀增厚,伴代谢增高,SUVmax约", "bbox": [64, 312, 905, 326]},
	{"text": "4.0。右肺上叶胸膜下见微小结节,直径约0.2cm,代谢未见异常增高。主动脉、心脏生理性显像。", "bbox": [64, 328, 782, 342]},
	{"text": "腹盆部PET/CT示肝左内叶包膜下见高代谢结节,SUVmax约5.4,CT显示密度轻微减低,边界不清。左侧肾上腺见", "bbox": [64, 344, 930, 358]},
	{"text": "高代谢小结节,SUVmax约3.2,CT扫描局部稍增厚。胆囊、脾脏、胰腺大小正常,未见异常密度和异常代谢影。十二指", "bbox": [64, 359, 934, 373]},
	{"text": "肠、双肾、右肾上腺、双输尿管、膀胱、前列腺及双侧精囊腺未见异常显像。腹腔内见多个形态不一、条管状、浓淡不", "bbox": [64, 375, 934, 389]},
	{"text": "一的正常肠影。", "bbox": [64, 390, 174, 404]},
	{"text": "淋巴结PET/CT示左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧锁骨区见多发淋巴结增大伴代谢增", "bbox": [97, 406, 908, 420]},
	{"text": "高,较大者位于纵隔7组,大小约3.2×1.0cm,SUVmax约3.3。", "bbox": [64, 421, 520, 435]},
	{"text": "骨骼、软组织及周围神经走行区PET/CT示左侧第8、9、10、11肋骨、右侧第6肋骨见骨质中断,部分伴骨赘形", "bbox": [97, 437, 908, 451]},
	{"text": "成,伴代谢增高,SUVmax约3.8。左侧腹横肌见结节状增厚伴高代谢,SUVmax约2.9。全身其余骨骼、软组织及周围神", "bbox": [64, 452, 928, 466]},
	{"text": "经未见异常代谢影像,骨质和肌肉密度未见明显改变。", "bbox": [64, 468, 460, 481]},
	{"text": "I", "bbox": [765, 475, 777, 492]},
	{"text": "诊断意见:", "bbox": [40, 519, 153, 537]},
	{"text": "1.左肺下叶基底段近肺门部MT;左侧胸膜弥漫种植转移;左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧", "bbox": [64, 544, 922, 558]},
	{"text": "锁骨区多发淋巴结增大伴高代谢,考虑转移可能;肝S4包膜下转移瘤;左下叶远端阻塞性炎症;左胸腔癌性胸水可能", "bbox": [64, 559, 917, 573]},
	{"text": "大;", "bbox": [64, 575, 90, 589]},
	{"text": "2.左侧腹横肌转移瘤待除;左侧肾上腺转移待除,建议定期复查;", "bbox": [64, 590, 540, 604]},
	{"text": "3.右肺上叶胸膜下少许炎性小结节;肝右叶少许小钙化灶;", "bbox": [64, 606, 490, 620]},
	{"text": "4.双侧多根肋骨骨折伴骨赘区域炎性摄取;", "bbox": [64, 621, 373, 635]},
	{"text": "5.全身其它部位18F-FDG PET/CT显像未见明显异常。", "bbox": [64, 637, 452, 651]},
	{"text": "报告医师:林晓强", "bbox": [61, 789, 204, 803]},
	{"text": "审核医师:", "bbox": [269, 789, 342, 803]},
	{"text": "复核医师:", "bbox": [491, 789, 582, 806]},
	{"text": "报告日期:2026-03-18", "bbox": [729, 789, 909, 803]},
	{"text": "地址:福州市鼓楼区新权路29号电话:0591-833116130591-86218247", "bbox": [61, 816, 591, 830]},
	{"text": "此报告仅供临床医师参考,不做证明使用。", "bbox": [64, 838, 368, 852]}
]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=18.4s
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[0]: text=病案号:, bbox=[40, 63, 115, 76]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[1]: text=11诊号:1K3392539b3, bbox=[304, 63, 494, 75]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[2]: text=血型:FEI/CI独|业冰(111), bbox=[510, 64, 793, 75]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[3]: text=显像剂:18F-FDG, bbox=[40, 85, 200, 98]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[4]: text=血糖:5.1mmol/l活, bbox=[304, 84, 527, 98]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[5]: text=度:7.22mci注射部位:右手背静脉, bbox=[563, 84, 880, 98]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[6]: text=注射/显像间隔时间:54分钟采集方式:断层采集3D厚, bbox=[40, 106, 527, 120]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[7]: text=度:3.75mm采集仪器:Discovery MI, bbox=[563, 106, 910, 120]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[8]: text=临床诊断:肺部阴影, bbox=[40, 128, 196, 142]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[9]: text=简要病史:, bbox=[40, 162, 153, 180]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[10]: text=肺部鳞癌基线评估。既往:2025.12肋骨骨折。, bbox=[64, 188, 417, 202]
2026-08-10 19:33:22,373 INFO     29 [qwen-vl-text] coord item[11]: text=图像所见:, bbox=[40, 209, 153, 228]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[12]: text=空腹4hr以上,口服适量温水,静脉注射显像剂,平静休息后行躯干PET及CT断层显像,PET图像行衰减校正及迭代, bbox=[64, 235, 934, 249]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[13]: text=法重建,PET、CT图像行多层面、多幅显示,影像清晰。, bbox=[64, 250, 473, 264]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[14]: text=颈部PET/CT示眼球、眼眶、鼻咽部、颈面部、喉咽部、甲状腺及颈部其它软组织结构、密度、代谢分布未见明显, bbox=[64, 266, 932, 280]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[15]: text=异常。, bbox=[64, 281, 109, 295]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[16]: text=胸部PET/CT示左肺下叶基底段近肺门部见高代谢结节,大小约2.0cm×1.9cm,边界不清,SUVmax约10.2。左肺, bbox=[64, 297, 928, 311]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[17]: text=下叶远端见散在片絮状高密度影。左侧胸腔积液,部分呈包裹性。左侧胸膜见不均匀增厚,伴代谢增高,SUVmax约, bbox=[64, 312, 905, 326]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[18]: text=4.0。右肺上叶胸膜下见微小结节,直径约0.2cm,代谢未见异常增高。主动脉、心脏生理性显像。, bbox=[64, 328, 782, 342]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[19]: text=腹盆部PET/CT示肝左内叶包膜下见高代谢结节,SUVmax约5.4,CT显示密度轻微减低,边界不清。左侧肾上腺见, bbox=[64, 344, 930, 358]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[20]: text=高代谢小结节,SUVmax约3.2,CT扫描局部稍增厚。胆囊、脾脏、胰腺大小正常,未见异常密度和异常代谢影。十二指, bbox=[64, 359, 934, 373]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[21]: text=肠、双肾、右肾上腺、双输尿管、膀胱、前列腺及双侧精囊腺未见异常显像。腹腔内见多个形态不一、条管状、浓淡不, bbox=[64, 375, 934, 389]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[22]: text=一的正常肠影。, bbox=[64, 390, 174, 404]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[23]: text=淋巴结PET/CT示左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧锁骨区见多发淋巴结增大伴代谢增, bbox=[97, 406, 908, 420]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[24]: text=高,较大者位于纵隔7组,大小约3.2×1.0cm,SUVmax约3.3。, bbox=[64, 421, 520, 435]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[25]: text=骨骼、软组织及周围神经走行区PET/CT示左侧第8、9、10、11肋骨、右侧第6肋骨见骨质中断,部分伴骨赘形, bbox=[97, 437, 908, 451]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[26]: text=成,伴代谢增高,SUVmax约3.8。左侧腹横肌见结节状增厚伴高代谢,SUVmax约2.9。全身其余骨骼、软组织及周围神, bbox=[64, 452, 928, 466]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[27]: text=经未见异常代谢影像,骨质和肌肉密度未见明显改变。, bbox=[64, 468, 460, 481]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[28]: text=I, bbox=[765, 475, 777, 492]
2026-08-10 19:33:22,374 INFO     29 [qwen-vl-text] coord item[29]: text=诊断意见:, bbox=[40, 519, 153, 537]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[30]: text=1.左肺下叶基底段近肺门部MT;左侧胸膜弥漫种植转移;左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧, bbox=[64, 544, 922, 558]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[31]: text=锁骨区多发淋巴结增大伴高代谢,考虑转移可能;肝S4包膜下转移瘤;左下叶远端阻塞性炎症;左胸腔癌性胸水可能, bbox=[64, 559, 917, 573]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[32]: text=大;, bbox=[64, 575, 90, 589]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[33]: text=2.左侧腹横肌转移瘤待除;左侧肾上腺转移待除,建议定期复查;, bbox=[64, 590, 540, 604]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[34]: text=3.右肺上叶胸膜下少许炎性小结节;肝右叶少许小钙化灶;, bbox=[64, 606, 490, 620]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[35]: text=4.双侧多根肋骨骨折伴骨赘区域炎性摄取;, bbox=[64, 621, 373, 635]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[36]: text=5.全身其它部位18F-FDG PET/CT显像未见明显异常。, bbox=[64, 637, 452, 651]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[37]: text=报告医师:林晓强, bbox=[61, 789, 204, 803]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[38]: text=审核医师:, bbox=[269, 789, 342, 803]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[39]: text=复核医师:, bbox=[491, 789, 582, 806]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[40]: text=报告日期:2026-03-18, bbox=[729, 789, 909, 803]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[41]: text=地址:福州市鼓楼区新权路29号电话:0591-833116130591-86218247, bbox=[61, 816, 591, 830]
2026-08-10 19:33:22,375 INFO     29 [qwen-vl-text] coord item[42]: text=此报告仅供临床医师参考,不做证明使用。, bbox=[64, 838, 368, 852]
2026-08-10 19:33:22,376 INFO     29 [qwen-vl-text] page=11 — 43/43 coords, api_time=18.4s
2026-08-10 19:33:22,376 INFO     29 [qwen-vl-text] new_positions (43):
[[11, 23.799999999999997, 68.425, 53.046, 63.992], [11, 180.88, 293.93, 53.046, 63.15], [11, 303.45, 471.835, 53.888, 63.15], [11, 23.799999999999997, 119.0, 71.57, 82.51599999999999], [11, 180.88, 313.565, 70.728, 82.51599999999999], [11, 334.98499999999996, 523.6, 70.728, 82.51599999999999], [11, 23.799999999999997, 313.565, 89.252, 101.03999999999999], [11, 334.98499999999996, 541.4499999999999, 89.252, 101.03999999999999], [11, 23.799999999999997, 116.61999999999999, 107.776, 119.564], [11, 23.799999999999997, 91.035, 136.404, 151.56], [11, 38.08, 248.11499999999998, 158.296, 170.084], [11, 23.799999999999997, 91.035, 175.97799999999998, 191.976], [11, 38.08, 555.73, 197.87, 209.658], [11, 38.08, 281.435, 210.5, 222.28799999999998], [11, 38.08, 554.54, 223.97199999999998, 235.76], [11, 38.08, 64.855, 236.602, 248.39], [11, 38.08, 552.16, 250.07399999999998, 261.86199999999997], [11, 38.08, 538.475, 262.704, 274.492], [11, 38.08, 465.28999999999996, 276.176, 287.964], [11, 38.08, 553.35, 289.64799999999997, 301.436], [11, 38.08, 555.73, 302.27799999999996, 314.066], [11, 38.08, 555.73, 315.75, 327.538], [11, 38.08, 103.53, 328.38, 340.168], [11, 57.714999999999996, 540.26, 341.852, 353.64], [11, 38.08, 309.4, 354.48199999999997, 366.27], [11, 57.714999999999996, 540.26, 367.954, 379.74199999999996], [11, 38.08, 552.16, 380.584, 392.372], [11, 38.08, 273.7, 394.056, 405.002], [11, 455.17499999999995, 462.315, 399.95, 414.264], [11, 23.799999999999997, 91.035, 436.998, 452.154], [11, 38.08, 548.59, 458.048, 469.83599999999996], [11, 38.08, 545.615, 470.678, 482.466], [11, 38.08, 53.55, 484.15, 495.938], [11, 38.08, 321.3, 496.78, 508.568], [11, 38.08, 291.55, 510.252, 522.04], [11, 38.08, 221.935, 522.882, 534.67], [11, 38.08, 268.94, 536.3539999999999, 548.1419999999999], [11, 36.295, 121.38, 664.338, 676.126], [11, 160.055, 203.48999999999998, 664.338, 676.126], [11, 292.145, 346.28999999999996, 664.338, 678.6519999999999], [11, 433.755, 540.855, 664.338, 676.126], [11, 36.295, 351.645, 687.072, 698.86], [11, 38.08, 218.95999999999998, 705.596, 717.384]]
2026-08-10 19:33:22,377 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=36.7s
2026-08-10 19:33:22,377 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:33:22,384 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:33:22,384 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:33:22,384 INFO     29 [qwen-vl-text] positions(35): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:33:22,384 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [35]
2026-08-10 19:33:22,555 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:33:22,557 INFO     29 [qwen-vl-text] LLM extraction start, text_len=721
2026-08-10 19:33:22,557 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:33:22,557 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 472, \"bbox_end\": 506, \"encounter_dates\": [\"2026-03-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "福建医科大学附属协和医院\n肺功能检查报告单\n姓名：\n性别：男\n年龄：49 Years\n病区床号：\n科室：\n病案号：\n身高：163 cm\n体重：61 kg\n测试号：Z0280275PF20280320\n预计值 实测值 实/预\nVC MAX [L] 3.92 2.48 63.3\nFVC [L] 3.77 2.48 65.8\nFEV 1 [L] 3.10 2.22 71.8\nFEV1%FVC [%] 81.86 89.56 109.4\nPEF [L/B] 8.05 6.38 79.3\nFIF25 [L/B] 7.01 6.16 87.9\nFIF50 [L/B] 4.31 2.76 64.1\nFIF75 [L/B] 1.64 1.29 78.4\nFIF25-75 [L/B] 3.76 2.58 68.7\nMVV [L/min] 116.58\nTLC-SB [L] 5.94 4.72 79.4\nFRC-SB [L] 3.17 3.74 118.1\nRV-SB [L] 1.98 2.18 110.0\nRV/TLC-SB [%] 33.07 46.21 139.7\nFRC/TLC-SB [%] 54.09 79.16 146.3\nDLCO SB [mmol/min/kPa] 8.85 5.98 67.6\nDLCOc SB [mmol/min/kPa] 8.86 5.98 67.6\nDLCO/VA [mmol/min/kPa/L] 1.49 1.30 87.1\nDLCOc/VA [mmol/min/kPa/L] 1.49 1.30 87.1\n1 本报告仅供临床参考，不作为任何诊断证明。\n检查者：\n审核者：\n报告日期：2026/3/20",
    "role": "user"
  }
]
2026-08-10 19:33:22,559 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:33:22.558+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 91, "failed": 0, "current": {"14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:33:34,867 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:33:34,867 INFO     29 [qwen-vl-text] LLM output (len=921):
{
  "exam_date": "2026-03-20",
  "report_date": "2026-03-20",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "预计值 实测值 实/预\nVC MAX [L] 3.92 2.48 63.3\nFVC [L] 3.77 2.48 65.8\nFEV 1 [L] 3.10 2.22 71.8\nFEV1%FVC [%] 81.86 89.56 109.4\nPEF [L/B] 8.05 6.38 79.3\nFIF25 [L/B] 7.01 6.16 87.9\nFIF50 [L/B] 4.31 2.76 64.1\nFIF75 [L/B] 1.64 1.29 78.4\nFIF25-75 [L/B] 3.76 2.58 68.7\nMVV [L/min] 116.58\nTLC-SB [L] 5.94 4.72 79.4\nFRC-SB [L] 3.17 3.74 118.1\nRV-SB [L] 1.98 2.18 110.0\nRV/TLC-SB [%] 33.07 46.21 139.7\nFRC/TLC-SB [%] 54.09 79.16 146.3\nDLCO SB [mmol/min/kPa] 8.85 5.98 67.6\nDLCOc SB [mmol/min/kPa] 8.86 5.98 67.6\nDLCO/VA [mmol/min/kPa/L] 1.49 1.30 87.1\nDLCOc/VA [mmol/min/kPa/L] 1.49 1.30 87.1",
  "conclusion": "1 本报告仅供临床参考，不作为任何诊断证明。",
  "physician": null,
  "reviewer": null
}
2026-08-10 19:33:34,869 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=838896, prompt_len=1439
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["福建医科大学附属协和医院", "肺功能检查报告单", "姓名：", "性别：男", "年龄：49 Years", "病区床号：", "科室：", "病案号：", "身高：163 cm", "体重：61 kg", "测试号：Z0280275PF20280320", "预计值 实测值 实/预", "VC MAX [L] 3.92 2.48 63.3", "FVC [L] 3.77 2.48 65.8", "FEV 1 [L] 3.10 2.22 71.8", "FEV1%FVC [%] 81.86 89.56 109.4", "PEF [L/B] 8.05 6.38 79.3", "FIF25 [L/B] 7.01 6.16 87.9", "FIF50 [L/B] 4.31 2.76 64.1", "FIF75 [L/B] 1.64 1.29 78.4", "FIF25-75 [L/B] 3.76 2.58 68.7", "MVV [L/min] 116.58", "TLC-SB [L] 5.94 4.72 79.4", "FRC-SB [L] 3.17 3.74 118.1", "RV-SB [L] 1.98 2.18 110.0", "RV/TLC-SB [%] 33.07 46.21 139.7", "FRC/TLC-SB [%] 54.09 79.16 146.3", "DLCO SB [mmol/min/kPa] 8.85 5.98 67.6", "DLCOc SB [mmol/min/kPa] 8.86 5.98 67.6", "DLCO/VA [mmol/min/kPa/L] 1.49 1.30 87.1", "DLCOc/VA [mmol/min/kPa/L] 1.49 1.30 87.1", "1 本报告仅供临床参考，不作为任何诊断证明。", "检查者：", "审核者：", "报告日期：2026/3/20"]

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
2026-08-10 19:33:46,888 INFO     29 [qwen-vl-text] coord API raw response (len=2259):
[
	{"text": "福建医科大学附属协和医院", "bbox": [356, 45, 655, 65]},
	{"text": "肺功能检查报告单", "bbox": [406, 72, 605, 93]},
	{"text": "姓名：", "bbox": [209, 102, 248, 115]},
	{"text": "性别：男", "bbox": [506, 102, 664, 115]},
	{"text": "年龄：49 Years", "bbox": [209, 115, 417, 128]},
	{"text": "病区床号：", "bbox": [506, 115, 574, 128]},
	{"text": "科室：", "bbox": [209, 128, 248, 140]},
	{"text": "病案号：", "bbox": [506, 128, 558, 140]},
	{"text": "身高：163 cm", "bbox": [209, 140, 402, 153]},
	{"text": "体重：61 kg", "bbox": [506, 140, 689, 153]},
	{"text": "测试号：Z0280275PF20280320", "bbox": [209, 153, 493, 166]},
	{"text": "预计值 实测值 实/预", "bbox": [350, 196, 573, 209]},
	{"text": "VC MAX [L] 3.92 2.48 63.3", "bbox": [102, 223, 573, 237]},
	{"text": "FVC [L] 3.77 2.48 65.8", "bbox": [102, 250, 573, 264]},
	{"text": "FEV 1 [L] 3.10 2.22 71.8", "bbox": [102, 264, 573, 277]},
	{"text": "FEV1%FVC [%] 81.86 89.56 109.4", "bbox": [102, 277, 573, 290]},
	{"text": "PEF [L/B] 8.05 6.38 79.3", "bbox": [102, 290, 573, 303]},
	{"text": "FIF25 [L/B] 7.01 6.16 87.9", "bbox": [102, 303, 573, 316]},
	{"text": "FIF50 [L/B] 4.31 2.76 64.1", "bbox": [102, 316, 573, 329]},
	{"text": "FIF75 [L/B] 1.64 1.29 78.4", "bbox": [102, 329, 573, 342]},
	{"text": "FIF25-75 [L/B] 3.76 2.58 68.7", "bbox": [102, 342, 573, 355]},
	{"text": "MVV [L/min] 116.58", "bbox": [102, 367, 398, 380]},
	{"text": "TLC-SB [L] 5.94 4.72 79.4", "bbox": [102, 393, 573, 406]},
	{"text": "FRC-SB [L] 3.17 3.74 118.1", "bbox": [102, 406, 573, 419]},
	{"text": "RV-SB [L] 1.98 2.18 110.0", "bbox": [102, 419, 573, 432]},
	{"text": "RV/TLC-SB [%] 33.07 46.21 139.7", "bbox": [102, 432, 573, 445]},
	{"text": "FRC/TLC-SB [%] 54.09 79.16 146.3", "bbox": [102, 445, 573, 458]},
	{"text": "DLCO SB [mmol/min/kPa] 8.85 5.98 67.6", "bbox": [102, 469, 573, 482]},
	{"text": "DLCOc SB [mmol/min/kPa] 8.86 5.98 67.6", "bbox": [102, 482, 573, 495]},
	{"text": "DLCO/VA [mmol/min/kPa/L] 1.49 1.30 87.1", "bbox": [102, 495, 573, 508]},
	{"text": "DLCOc/VA [mmol/min/kPa/L] 1.49 1.30 87.1", "bbox": [102, 508, 573, 521]},
	{"text": "1 本报告仅供临床参考，不作为任何诊断证明。", "bbox": [91, 858, 448, 872]},
	{"text": "检查者：", "bbox": [367, 875, 426, 889]},
	{"text": "审核者：", "bbox": [575, 875, 633, 889]},
	{"text": "报告日期：2026/3/20", "bbox": [723, 875, 895, 889]}
]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=12.0s
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[0]: text=福建医科大学附属协和医院, bbox=[356, 45, 655, 65]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告单, bbox=[406, 72, 605, 93]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[209, 102, 248, 115]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[506, 102, 664, 115]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：49 Years, bbox=[209, 115, 417, 128]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[5]: text=病区床号：, bbox=[506, 115, 574, 128]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[6]: text=科室：, bbox=[209, 128, 248, 140]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[7]: text=病案号：, bbox=[506, 128, 558, 140]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[8]: text=身高：163 cm, bbox=[209, 140, 402, 153]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[9]: text=体重：61 kg, bbox=[506, 140, 689, 153]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[10]: text=测试号：Z0280275PF20280320, bbox=[209, 153, 493, 166]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[11]: text=预计值 实测值 实/预, bbox=[350, 196, 573, 209]
2026-08-10 19:33:46,889 INFO     29 [qwen-vl-text] coord item[12]: text=VC MAX [L] 3.92 2.48 63.3, bbox=[102, 223, 573, 237]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[13]: text=FVC [L] 3.77 2.48 65.8, bbox=[102, 250, 573, 264]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[14]: text=FEV 1 [L] 3.10 2.22 71.8, bbox=[102, 264, 573, 277]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[15]: text=FEV1%FVC [%] 81.86 89.56 109.4, bbox=[102, 277, 573, 290]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[16]: text=PEF [L/B] 8.05 6.38 79.3, bbox=[102, 290, 573, 303]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[17]: text=FIF25 [L/B] 7.01 6.16 87.9, bbox=[102, 303, 573, 316]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[18]: text=FIF50 [L/B] 4.31 2.76 64.1, bbox=[102, 316, 573, 329]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[19]: text=FIF75 [L/B] 1.64 1.29 78.4, bbox=[102, 329, 573, 342]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[20]: text=FIF25-75 [L/B] 3.76 2.58 68.7, bbox=[102, 342, 573, 355]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[21]: text=MVV [L/min] 116.58, bbox=[102, 367, 398, 380]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[22]: text=TLC-SB [L] 5.94 4.72 79.4, bbox=[102, 393, 573, 406]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[23]: text=FRC-SB [L] 3.17 3.74 118.1, bbox=[102, 406, 573, 419]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[24]: text=RV-SB [L] 1.98 2.18 110.0, bbox=[102, 419, 573, 432]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[25]: text=RV/TLC-SB [%] 33.07 46.21 139.7, bbox=[102, 432, 573, 445]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[26]: text=FRC/TLC-SB [%] 54.09 79.16 146.3, bbox=[102, 445, 573, 458]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[27]: text=DLCO SB [mmol/min/kPa] 8.85 5.98 67.6, bbox=[102, 469, 573, 482]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[28]: text=DLCOc SB [mmol/min/kPa] 8.86 5.98 67.6, bbox=[102, 482, 573, 495]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[29]: text=DLCO/VA [mmol/min/kPa/L] 1.49 1.30 87.1, bbox=[102, 495, 573, 508]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[30]: text=DLCOc/VA [mmol/min/kPa/L] 1.49 1.30 87.1, bbox=[102, 508, 573, 521]
2026-08-10 19:33:46,890 INFO     29 [qwen-vl-text] coord item[31]: text=1 本报告仅供临床参考，不作为任何诊断证明。, bbox=[91, 858, 448, 872]
2026-08-10 19:33:46,891 INFO     29 [qwen-vl-text] coord item[32]: text=检查者：, bbox=[367, 875, 426, 889]
2026-08-10 19:33:46,891 INFO     29 [qwen-vl-text] coord item[33]: text=审核者：, bbox=[575, 875, 633, 889]
2026-08-10 19:33:46,891 INFO     29 [qwen-vl-text] coord item[34]: text=报告日期：2026/3/20, bbox=[723, 875, 895, 889]
2026-08-10 19:33:46,891 INFO     29 [qwen-vl-text] page=12 — 35/35 coords, api_time=12.0s
2026-08-10 19:33:46,891 INFO     29 [qwen-vl-text] new_positions (35):
[[12, 211.82, 389.72499999999997, 37.89, 54.73], [12, 241.57, 359.97499999999997, 60.623999999999995, 78.306], [12, 124.35499999999999, 147.56, 85.884, 96.83], [12, 301.07, 395.08, 85.884, 96.83], [12, 124.35499999999999, 248.11499999999998, 96.83, 107.776], [12, 301.07, 341.53, 96.83, 107.776], [12, 124.35499999999999, 147.56, 107.776, 117.88], [12, 301.07, 332.01, 107.776, 117.88], [12, 124.35499999999999, 239.19, 117.88, 128.826], [12, 301.07, 409.955, 117.88, 128.826], [12, 124.35499999999999, 293.335, 128.826, 139.772], [12, 208.25, 340.935, 165.03199999999998, 175.97799999999998], [12, 60.69, 340.935, 187.766, 199.554], [12, 60.69, 340.935, 210.5, 222.28799999999998], [12, 60.69, 340.935, 222.28799999999998, 233.23399999999998], [12, 60.69, 340.935, 233.23399999999998, 244.17999999999998], [12, 60.69, 340.935, 244.17999999999998, 255.126], [12, 60.69, 340.935, 255.126, 266.072], [12, 60.69, 340.935, 266.072, 277.018], [12, 60.69, 340.935, 277.018, 287.964], [12, 60.69, 340.935, 287.964, 298.90999999999997], [12, 60.69, 236.81, 309.014, 319.96], [12, 60.69, 340.935, 330.906, 341.852], [12, 60.69, 340.935, 341.852, 352.798], [12, 60.69, 340.935, 352.798, 363.74399999999997], [12, 60.69, 340.935, 363.74399999999997, 374.69], [12, 60.69, 340.935, 374.69, 385.63599999999997], [12, 60.69, 340.935, 394.89799999999997, 405.844], [12, 60.69, 340.935, 405.844, 416.78999999999996], [12, 60.69, 340.935, 416.78999999999996, 427.736], [12, 60.69, 340.935, 427.736, 438.68199999999996], [12, 54.144999999999996, 266.56, 722.4359999999999, 734.2239999999999], [12, 218.36499999999998, 253.47, 736.75, 748.538], [12, 342.125, 376.635, 736.75, 748.538], [12, 430.185, 532.525, 736.75, 748.538]]
2026-08-10 19:33:46,891 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=24.5s
2026-08-10 19:33:46,891 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:33:46,893 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:33:46,893 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:33:46,894 INFO     29 [qwen-vl-text] positions(22): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:33:46,894 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [22]
2026-08-10 19:33:47,096 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:33:47,097 INFO     29 [qwen-vl-text] LLM extraction start, text_len=271
2026-08-10 19:33:47,097 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:33:47,097 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 507, \"bbox_end\": 528, \"encounter_dates\": [\"2026-03-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "姓\n住院\n性别：男\n年龄：40岁\n送检单位：本院\n送检科室：呼吸与危重症医学科 送检医生：黄世霜\n送检日期：2026-03-10\n临床诊断：肺炎。\n送检材料：左肺下叶粘膜组织\n肉眼所见：\n灰白组织7块，直径0.05-0.2cm。（包全）\n镜下所见：\n病理诊断：\n（左肺下叶粘膜组织）浸润性鳞状细胞癌。\n诊断医师：廖荣娥\n医生签名：廖荣娥\n报告时间：2026年03月12\n备注：\n1 本报告仅作临床医师参考；若发现病理诊断与临床不相符时请立即与我科联系。\n2 此报告需医生签名方为有效。\n本报告仅作临床医师参考\n联系电话： 0598-63067",
    "role": "user"
  }
]
2026-08-10 19:33:54,869 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:33:54.867+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 91, "failed": 0, "current": {"14e7373094f111f1bd9827cf206dfa2d": {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:33:54,935 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:33:54,935 INFO     29 [qwen-vl-text] LLM output (len=381):
{
  "exam_date": "2026-03-10",
  "report_date": "2026-03-12",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "左肺下叶粘膜组织",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸与危重症医学科",
  "bed_number": null,
  "findings": "肉眼所见：\n灰白组织7块，直径0.05-0.2cm。（包全）",
  "conclusion": "病理诊断：\n（左肺下叶粘膜组织）浸润性鳞状细胞癌。",
  "physician": "廖荣娥",
  "reviewer": null
}
2026-08-10 19:33:54,938 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1550840, prompt_len=950
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["姓", "住院", "性别：男", "年龄：40岁", "送检单位：本院", "送检科室：呼吸与危重症医学科 送检医生：黄世霜", "送检日期：2026-03-10", "临床诊断：肺炎。", "送检材料：左肺下叶粘膜组织", "肉眼所见：", "灰白组织7块，直径0.05-0.2cm。（包全）", "镜下所见：", "病理诊断：", "（左肺下叶粘膜组织）浸润性鳞状细胞癌。", "诊断医师：廖荣娥", "医生签名：廖荣娥", "报告时间：2026年03月12", "备注：", "1 本报告仅作临床医师参考；若发现病理诊断与临床不相符时请立即与我科联系。", "2 此报告需医生签名方为有效。", "本报告仅作临床医师参考", "联系电话： 0598-63067"]

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
2026-08-10 19:34:01,512 INFO     29 [qwen-vl-text] coord API raw response (len=1162):
[
	{"text": "姓", "bbox": [73, 67, 96, 83]},
	{"text": "住院", "bbox": [73, 90, 127, 106]},
	{"text": "性别：男", "bbox": [385, 67, 471, 84]},
	{"text": "年龄：40岁", "bbox": [508, 67, 610, 84]},
	{"text": "送检单位：本院", "bbox": [679, 67, 818, 84]},
	{"text": "送检科室：呼吸与危重症医学科 送检医生：黄世霜", "bbox": [73, 111, 555, 128]},
	{"text": "送检日期：2026-03-10", "bbox": [680, 90, 884, 107]},
	{"text": "临床诊断：肺炎。", "bbox": [680, 111, 832, 128]},
	{"text": "送检材料：左肺下叶粘膜组织", "bbox": [73, 133, 350, 150]},
	{"text": "肉眼所见：", "bbox": [73, 171, 170, 188]},
	{"text": "灰白组织7块，直径0.05-0.2cm。（包全）", "bbox": [73, 191, 462, 208]},
	{"text": "镜下所见：", "bbox": [66, 377, 165, 394]},
	{"text": "病理诊断：", "bbox": [65, 582, 163, 600]},
	{"text": "（左肺下叶粘膜组织）浸润性鳞状细胞癌。", "bbox": [75, 606, 478, 623]},
	{"text": "诊断医师：廖荣娥", "bbox": [66, 845, 239, 863]},
	{"text": "医生签名：廖荣娥", "bbox": [404, 845, 698, 878]},
	{"text": "报告时间：2026年03月12", "bbox": [756, 847, 998, 864]},
	{"text": "备注：", "bbox": [66, 878, 114, 895]},
	{"text": "1 本报告仅作临床医师参考；若发现病理诊断与临床不相符时请立即与我科联系。", "bbox": [66, 900, 739, 916]},
	{"text": "2 此报告需医生签名方为有效。", "bbox": [93, 915, 335, 930]},
	{"text": "联系电话： 0598-63067", "bbox": [785, 900, 998, 915]}
]
2026-08-10 19:34:01,513 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=6.6s
2026-08-10 19:34:01,513 INFO     29 [qwen-vl-text] coord item[0]: text=姓, bbox=[73, 67, 96, 83]
2026-08-10 19:34:01,513 INFO     29 [qwen-vl-text] coord item[1]: text=住院, bbox=[73, 90, 127, 106]
2026-08-10 19:34:01,513 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[385, 67, 471, 84]
2026-08-10 19:34:01,513 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：40岁, bbox=[508, 67, 610, 84]
2026-08-10 19:34:01,513 INFO     29 [qwen-vl-text] coord item[4]: text=送检单位：本院, bbox=[679, 67, 818, 84]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[5]: text=送检科室：呼吸与危重症医学科 送检医生：黄世霜, bbox=[73, 111, 555, 128]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[6]: text=送检日期：2026-03-10, bbox=[680, 90, 884, 107]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[7]: text=临床诊断：肺炎。, bbox=[680, 111, 832, 128]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[8]: text=送检材料：左肺下叶粘膜组织, bbox=[73, 133, 350, 150]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[9]: text=肉眼所见：, bbox=[73, 171, 170, 188]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[10]: text=灰白组织7块，直径0.05-0.2cm。（包全）, bbox=[73, 191, 462, 208]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[11]: text=镜下所见：, bbox=[66, 377, 165, 394]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[12]: text=病理诊断：, bbox=[65, 582, 163, 600]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[13]: text=（左肺下叶粘膜组织）浸润性鳞状细胞癌。, bbox=[75, 606, 478, 623]
2026-08-10 19:34:01,514 INFO     29 [qwen-vl-text] coord item[14]: text=诊断医师：廖荣娥, bbox=[66, 845, 239, 863]
2026-08-10 19:34:01,515 INFO     29 [qwen-vl-text] coord item[15]: text=医生签名：廖荣娥, bbox=[404, 845, 698, 878]
2026-08-10 19:34:01,515 INFO     29 [qwen-vl-text] coord item[16]: text=报告时间：2026年03月12, bbox=[756, 847, 998, 864]
2026-08-10 19:34:01,515 INFO     29 [qwen-vl-text] coord item[17]: text=备注：, bbox=[66, 878, 114, 895]
2026-08-10 19:34:01,515 INFO     29 [qwen-vl-text] coord item[18]: text=1 本报告仅作临床医师参考；若发现病理诊断与临床不相符时请立即与我科联系。, bbox=[66, 900, 739, 916]
2026-08-10 19:34:01,515 INFO     29 [qwen-vl-text] coord item[19]: text=2 此报告需医生签名方为有效。, bbox=[93, 915, 335, 930]
2026-08-10 19:34:01,515 INFO     29 [qwen-vl-text] coord item[20]: text=联系电话： 0598-63067, bbox=[785, 900, 998, 915]
2026-08-10 19:34:01,516 INFO     29 [qwen-vl-text] page=13 — 22/22 coords, api_time=6.6s
2026-08-10 19:34:01,517 INFO     29 [qwen-vl-text] new_positions (22):
[[13, 43.434999999999995, 57.12, 56.414, 69.886], [13, 43.434999999999995, 75.565, 75.78, 89.252], [13, 229.075, 280.245, 56.414, 70.728], [13, 302.26, 362.95, 56.414, 70.728], [13, 404.005, 486.71, 56.414, 70.728], [13, 43.434999999999995, 330.22499999999997, 93.462, 107.776], [13, 404.59999999999997, 525.98, 75.78, 90.094], [13, 404.59999999999997, 495.03999999999996, 93.462, 107.776], [13, 43.434999999999995, 208.25, 111.98599999999999, 126.3], [13, 43.434999999999995, 101.14999999999999, 143.982, 158.296], [13, 43.434999999999995, 274.89, 160.822, 175.136], [13, 39.269999999999996, 98.175, 317.43399999999997, 331.748], [13, 38.675, 96.985, 490.044, 505.2], [13, 44.625, 284.40999999999997, 510.252, 524.566], [13, 39.269999999999996, 142.20499999999998, 711.49, 726.646], [13, 240.38, 415.31, 711.49, 739.276], [13, 449.82, 593.81, 713.174, 727.4879999999999], [13, 39.269999999999996, 67.83, 739.276, 753.5899999999999], [13, 39.269999999999996, 439.705, 757.8, 771.2719999999999], [13, 55.335, 199.325, 770.43, 783.06], [13, 467.075, 593.81, 757.8, 770.43], [13, 467.075, 593.81, 757.8, 770.43]]
2026-08-10 19:34:01,517 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=14.6s
2026-08-10 19:34:01,530 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 19:34:01,530 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "7 items, types={'ExaminationReport': 7}", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:34:01,531 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 19:34:01,538 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:34:01,538 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:34:02,680 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:34:02,686 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 19:34:02,686 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "529 items", "markdown": "", "text": "", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "7 items, types={'ExaminationReport': 7}", "chunks_LabExam": "5 items, types={'LabReport': 5}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 7, \"chunks_LabExam\": 5}"}
2026-08-10 19:34:02,686 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 19:34:02,687 INFO     29 [ChunkMerger] Merged 13 chunks from 9 sources: {'Extractor:LabExam': 5, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 7, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 19:34:02,695 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 19:34:02,695 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "13 items, types={'LabReport': 5, 'AdmissionRecord': 1, 'ExaminationReport': 7}", "name": "BJCA,男，49，肺鳞癌一线(1).pdf"}
2026-08-10 19:34:02,696 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 19:34:02,862 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786390127585, 'update_date': datetime.datetime(2026, 8, 10, 19, 28, 47), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1415552, 'status': '1'}
2026-08-10 19:34:03,153 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   乙肝病毒表面抗原  None  0.00  IU/ml  <0.05  False    乙肝病毒表面抗体  None  47.62  mIU/ml  <10  True    乙肝病毒e抗原  None  0.41  S/CO  <1  False    乙肝病毒e抗体  None  1.29  S/CO  >1  False    乙肝病毒核心抗体  None  2.01  S/CO  <1  True    丙型肝炎病毒抗体  None  0.11  S/CO  <1  False    人免疫缺陷病毒抗原抗体  None  0.07  S/CO  <1  False    梅毒螺旋体特异抗体  None  0.11  S/CO  <1  False   
---
   总胆红素  TBIL  10.6  umol/L  0.0~23.0  False    直接胆红素  DBIL  1.4  umol/L  0.0~8.0  False    间接胆红素  IBIL  9.2  umol/L  0.0~20.0  False    总蛋白  TP  81.8  g/L  65.0~85.0  False    白蛋白  ALB  37.3  g/L  40.0~55.0  True    球蛋白  GLB  44.5  g/L  20.0~35.0  True    白球比例  A/G  0.84  None  1.09~2.50  True    丙氨酸氨基转移酶  None  39  IU/L  9~50  False    天冬氨酸氨基转移酶  None  27  IU/L  15~40  False    AST/ALT  None  0.69  None  None  False    γ-谷氨酰转肽酶  None  79  IU/L  10~60  True    碱性磷酸酶  ALP  146  IU/L  45~125  True    甘油三酯  TG  0.98  mmol/L  0.40~1.86  False    总胆固醇  CHOL  4.73  mmol/L  3.40~6.10  False    高密度脂蛋白胆固醇  None  0.77  mmol/L  0.90~1.90  True    非高密度脂蛋白胆固醇  None  3.96  None  None  False    低密度脂蛋白胆固醇  None  3.37  mmol/L  1.10~3.50  False    载脂蛋白A1  APOA1  0.76  g/L  1.00~1.60  True    载脂蛋白B  APOB  1.09  g/L  0.60~1.10  False    载脂蛋白A1：B  None  0.70  None  None  False   
---
   尿素  UREA  4.1  mmol/L  3.1~7.4  False    肌酐  CREA  68  umol/L  57~97  False    UREA/CREA  None  0.06  None  None  False    尿酸  URIC  183  umol/L  130~430  False    葡萄糖  GLU  5.21  mmol/L  3.90~6.10  False    乳酸脱氢酶  LDH  162  IU/L  120~250  False    肌酸激酶  CK  36  IU/L  22~270  False    肌酸激酶MB亚型  None  17.0  IU/L  2.0~25.0  False    CKMB/CK  None  0.47  None  None  False    钾  K  4.50  mmol/L  3.50~5.50  False    钠  NA  138.4  mmol/L  135.0~148.0  False    氯  CL  96.3  mmol/L  96.0~112.0  False    钙  CA  2.35  mmol/L  2.10~2.70  False    碳酸氢盐  HC03  27.3  mmol/L  20.1~29.0  False    镁  MG  0.99  mmol/L  0.70~1.10  False    无机磷酸盐  P  1.27  mmol/L  0.83~1.48  False    阴离子间隙  AG  19  None  None  False    渗透压  OSM  286  None  None  False   
---
   白细胞计数  None  6.58  10^9/L  4.00~10.00  False    中性粒细胞%  None  63.90  %  50.00~70.00  False    淋巴细胞%  None  25.60  %  20.00~40.00  False    单核细胞%  None  9.70  %  3.00~8.00  True    嗜酸性粒细胞%  None  0.50  %  0.00~5.00  False    嗜碱性粒细胞%  None  0.30  %  0.00~1.00  False    中性粒细胞绝对数  None  4.21  10^9/L  1.50~7.00  False    淋巴细胞绝对数  None  1.68  10^9/L  0.80~4.00  False    单核细胞绝对数  None  0.64  10^9/L  0.12~0.80  False    嗜酸性粒细胞绝对数  None  0.03  10^9/L  0.00~0.50  False    嗜碱性粒细胞绝对数  None  0.02  10^9/L  0.00~0.10  False    红细胞计数  None  4.55  10^12/L  3.50~6.00  False    血红蛋白  None  131.0  g/L  120.0~165.0  False    红细胞比积  None  39.7  %  40.0~50.0  True    平均红细胞体积  None  87.2  f1  80.0~100.0  False    平均红细胞血红蛋白含量  None  28.7  pg  27.3~34.4  False    平均红细胞血红蛋白浓度  None  330.0  g/L  320.0~360.0  False    红细胞体积分布宽度-CV  None  13.4  %  11.0~16.0  False    红细胞体积分布宽度-SD  None  43.7  f1  37.0~54.0  False    有核红细胞绝对计数  None  0.00  10^9/L  0.00~0.02  False    有核红细胞/白细胞  None  0.00  %  <1.00  False    血小板计数  None  378  10^9/L  100~300  True    血小板比容  None  0.37  %  0.06~0.28  True    平均血小板体积  None  9.9  f1  6.4~12.1  False    血小板体积分布宽度  None  16.5  %  9.0~17.0  False    大血小板比率  None  24.80  %  13.00~43.00  False    C-反应蛋白  None  97.64  mg/L  0~8.00  True   
---
   凝血酶原时间  PT  14.8  秒  11.0~15.0  False    国际标准化比值  INR  1.18  None  None  False    凝血酶原活动度  None  76.0  %  70.0~150.0  False    活化部分凝血活酶时间  APTT  44.8  秒  28.0~42.0  True    活化部分凝血活酶时间比值  None  1.32  None  None  False    纤维蛋白原  FIB  9.79  g/L  2.00~4.00  True    凝血酶时间  TT  19.8  秒  14.0~21.0  False    D-二聚体  D-DI  7.28  ug/ml  0.00~0.50  True   
---
姓名
住址：福建省三明市尤溪县
性别：男
工作单位：/
年龄：49岁
入院日期：2026.03.16 10:21:29
婚姻：已婚
记录时间：2026.03.16 10:21:29
民族：汉族
病史陈述者：患者及家属
出生地：福建省三明市
病史可靠程度：基本可靠
职业(工种)：/
过敏史：未发现
主诉：确诊左下肺鳞癌4天。
现病史：缘于2026.03.05以“咳嗽、咳痰1月”就诊于尤溪县总医院，查“2026.03.06胸部
增强CT：左肺下叶占位，大小约6.1cm×8.8cm；左肺下叶支气管部分闭塞，伴阻塞性肺不张、肺炎；双肺结节；左肺门及纵隔数枚淋巴结影，大者径约1cm。”
于2026.03.09行“支气管镜检查+支气管粘膜活检术”，术顺，术后病理示：（左肺下叶粘
膜组织）浸润性鳞状细胞癌。
予抗感染、止咳、化痰后咳嗽、咳痰好转，
无头晕、头痛，无胸闷、胸痛，无畏冷、发热，无心悸、呼吸困难，无乏力、盗汗，无腹胀、腹痛，
无恶心、呕吐，无声音嘶哑、吞咽困难等不适。今为进一步诊治就诊我科，门诊拟“左下肺腺
癌”收治入院，自发病以来，精神、食欲、睡眠尚可，大、小便正常，体重近期未见明显增减。
既往史：平素身体健康，否认高血压，否认糖尿病，否认冠心病，否认肝炎、结核、菌痢、伤寒
等传染病史，否认其他手术史，否认输血史，否认外伤史，否认药物过敏史，预防接种按时完成。
个人史：生于原籍，否认长期外地居住史，否认疫区居留史，否认特殊化学品及放射线接触
史。有吸烟史20余年，否认饮酒。否认冶游史。
婚育史：已婚已育，配偶及孩子均体健。
家族史：父已故，母健在。其父有肺癌史。否认家族中有“肝炎、伤寒、结核”等传染病史，否
认家族中有其他遗传性疾病史。
体格检查
T:36.5℃
P:79次/分
R:19次/分
BP:112/69mmHg
一般情况：神志清楚，发育正常，营养良好，体型正常，正常面容，表情安静，自动体位，查
体合作，对答切题，步行入院。
第1页
皮肤粘膜：色泽正常，未见黄染，未见紫绀，未见色素沉着，未见皮疹，未见皮下出血。皮温
正常，湿度正常，弹性好，无水肿，未见肝掌，未见蜘蛛痣。
淋巴结：全身浅表淋巴结未触及。
头颅：大小正常，形状正常，头发分布正常，眼睑无浮肿，眼球无异常，巩膜无黄染，结膜正
常，角膜透明，瞳孔等大等圆，直径3mm，对光反射灵敏。耳廓无畸形，外耳道正常，无异常分泌
物，听力正常，无乳突压痛。双侧鼻唇沟对称，鼻中隔无偏曲，鼻腔通气畅，无副鼻窦区压痛。口
唇无紫绀，口腔粘膜完整，口腔无异味，伸舌居中，咽无充血，扁桃体无肿大，无脓点。
颈部：颈柔软，颈静脉无怒张，肝颈静脉回流征阴性，未见颈动脉异常搏动，气管居中，甲
状腺无肿大，无血管杂音。
胸部：胸廓无畸形，胸壁静脉未见，无皮下气肿，肋间隙正常。胸骨无压痛，胸廓挤压征阴
性，无男乳女化。
肺部：双侧呼吸运动匀称，双侧触觉语颤对称，叩诊音清，呼吸音清，未闻及干湿罗音，未
闻及胸膜摩擦音。
心脏：无心前区隆起，心尖搏动正常，位于第Ⅴ肋间，左锁骨中线内0.5cm处，未扪及震颤
及抬举样搏动，心界叩诊无扩大，心音清晰，心率79次/分，节律整齐，A2>P2，无杂音。心浊音界
大小如下图所示：
右(CM) 肋间 左(CM)
2 Ⅱ 2
2 Ⅲ 3.5
3 Ⅳ 5.5
Ⅴ 8.0
注：左锁骨中线距前正中线8.5CM。
周围血管：脉率79次/分，节律整齐，无脉搏短绌，无奇脉，无交替脉，无毛细血管搏动征，
无Duroziez二重杂音，无大血管枪击音，无水冲脉。双侧足背动脉及桡动脉搏动良好对称。
腹部：腹平坦，呼吸运动自如，腹壁静脉未见怒张，腹壁皮肤无皮疹，无色素沉着，无腹纹，
无疤痕，无疝，未见胃肠型及蠕动波，无上腹部搏动。全腹软，无肌紧张，无压痛及反跳痛，未触
及包块，肝脏右肋下、剑突下未触及，胆囊未触及，莫菲氏征阴性，脾脏左肋下未触及，双肾未触
及，双侧输尿管径路无压痛，无液波震颤。鼓音，肝上界位于右锁骨中线上第Ⅳ肋间，肝区无叩
击痛，胃泡鼓音区存在，肾区无叩痛，移动性浊音阴性。肠鸣音正常，4次/分，未闻及振水音及血
第2页
管杂音。
肛门生殖器：肛门及外生殖器未见异常。
脊柱四肢：脊柱生理弯曲正常，活动度正常，脊柱无压痛，无叩击痛；各关节四肢形态正常。肢体无浮肿，无静脉曲张，无色素沉着，无溃疡。
神经系统：四肢肌力正常，肌张力正常，角膜反射、腹壁反射、肱二头肌、肱三头肌、桡反射、膝反射、跟腱反射正常，巴彬斯基征未引出，脑膜刺激征阴性。
专科情况
生命征平稳，神志清楚，浅表淋巴结未触及淋巴结肿大。胸廓对称无畸形，胸壁未见静脉曲张，双肺触觉语颤对称，双肺叩诊呈清音，双肺呼吸音清，未闻及明显干湿性啰音及摩擦音。心前区无隆起，心脏触诊未及震颤，心界叩诊无扩大，心律齐，各瓣音区心音正常，未闻及病理性杂音。腹平软。未见胃肠型及蠕动波，肝脏肋下未触及，无压痛及反跳痛。双下肢无浮肿。
辅助检查
出院诊断：
医生签名：
初步诊断：肺结节性质待查：
肺癌？
炎性假瘤？
医生签名：
---
测量结果:
Lved:46.5 mm
Lve5:28.9 mm
La:26.6 mm
Ao:25.7 mm
Lvpw:8.5 mm
Ivs:9.5 mm
Rv:20.1 mm
Ra-L:34.8 mm
Ra-M:25.5 mm
Pa:17.6 mm
E:0.46 m/s
A:0.63 m/s
Hr:90 bpm
Fb:37.8 %
Bf:68.0 %(Teich)
EDV:99.8 ml
Sv:67.8 ml
Co:6.1 L/min
Ci:4.0 L/min. m²
H:166 cm
W:52.5 kg
BSA:1.5 m²
LVM:140.2 g
LVMI:93.4 g/m²
B':0.08 m/s
A':0.10 m/s
RWT:0.38
E/A:0.7
E/E':5.7
正常参考值(mm) 摘自中国成年人超声心动图检查测量指南《中华超声影像学杂志》2016.25(8):
AO
LA
LV
IVS
RA
RV
PA
LVMI
EF(%)
0-1岁
8-15
8-18
17-31
1.5-4
17-32
7-12
6-12
≥55
1-6岁
15-21
14-21
27-35
3-5.5
26-37
8-14
10-16
≥55
6-10岁
17-23
17-24
30-38
5-7
30-39
10-15
14-18
≥55
10-14岁
18-27
19-30
32-50
5-10
34-47
11-17
16-20
≥55
成人(男)
27.7±5.7
31.1±3.9
46.2±4.0
8.9±1.3
44.4±4.7
22.3±3.9
20.1±3.2
≥125
≥55
成人(女)
25.9±3.5
29.4±5.8
43.2±3.3
8.1±1.3
41.5±4.7
21.1±3.6
19.2±3.1
≥115
≥55
检查描述:
二维及M型超声:
静息时未见节段性室壁运动功能异常(见图)。各组瓣膜形态未见异常。心包腔正常。室间隔连
续性完整，大血管位置关系正常，主一肺动脉无沟通。
多普勒:
三尖瓣反流最大压差17MMHG，估测肺动脉收缩压22MMHG。
彩色多普勒:
二尖瓣微量反流。三尖瓣轻度反流。主动脉瓣未见明显反流。肺动脉瓣轻度反流。
超声提示:
心脏结构及功能未见明显异常改变
记录医生:袁瑄宸 报告录入:黄玉云 检查医生:刘文坤 复审医生:
报告日期: 2026-03-17 16:38:04
检查日期: 2026-03-17
(本报告仅供临床参考,不做任何证明。)
---
性别：男
年龄：49岁
门诊号：
检查部位：肺部
检查设备：GE-HD750
流水号：0013240579
检查技术：CT
影像学所见：
双肺纹理清晰，左肺下叶见团块软组织密度影，病灶内支气管闭塞，较大截面约7.6cm×
8.3cm，增强扫描不均匀强化，周围散在条索斑片影。右肺散在小结节，大者右肺上叶尖段见一
实性结节（Se4/Img46），大小约0.4cm×0.2cm。气管、余支气管通畅，纵隔及左肺门可见肿大
淋巴结，大者短径约1.0cm，左侧胸腔少-中量积液，部分为包裹性。左侧胸膜结节状增厚。
影像学诊断：
1.左肺下叶肿块，考虑MT伴周围阻塞性肺炎，请结合临床。
2.纵隔及左肺门肿大淋巴结，部分转移可能。
3.左侧胸膜增厚，转移可能。
4.右肺散在小结节，性质待定，建议随诊复查。
5.左侧胸腔少-中量积液，部分为包裹性。
报告医生：许志祥 /许志祥
审核医生：沈东挥
复核医生：
此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。
报告时间：2026-03-18
---
门诊号:
医院:
申请医生
申请科室
检查日期: 2026-03-17 10:58:32
检查医生
报告日期: 2026-03-17 11:11:03
报告医生: 蔡平
审核日期: 2026-03-17 11:11:03
审核医生: 蔡平
电轴(-30~90°): 29
QRS时限(<120): 100
P-R间期(120~200): 134
Q-T间期(0~450): 344
QTc(0~450): 444
SV1: 1.26
RV5(0~2.5): 2.02
R+S: 3.28
心率(60~100): 100
临床诊断: 肺肿物
描述:
诊断: 窦性心律 ST段改变
报告状态 已审核
检查项目: 心电图(常规十二通道)
当前状态
走纸: 25mm/s
增益:10mm/mv
当前模式:普通模式
572
596
600
600
596
600
604
600
596
596
604
604
596
25mm/s 10mm/mv
105
101
100
100
101
100
100
100
101
101
100
100
101
100
100
102
II
III
aVR
aVL
aVF
V1
V2
V3
V4
V5
V6
2026-03-17 10:59:32
版权所有 纳龙科技
---
检查部位：头颅
检查设备：飞利浦MR9 流水号：0013240580
检查技术：MR
检查参数：
影像学所见：
双侧大脑半球对称，灰白质对比正常，实质内未见明显异常信号，DWI未见异常高信号，SW
I未见异常低信号，各脑沟、脑池未见增宽、变深，脑室系统未见增宽，中线结构居中，幕下小
脑、脑干未见异常信号，双侧桥小脑角区未见明显异常。颅骨骨质未见异常信号。增强后未见
明显强化。
影像学诊断：
颅脑MRI平扫及增强未见明显异常。
报告医生：林佳辉 /林佳辉
审核医生：陈明宏
复核医生：
此报告仅供本院医生参考，不做其它证明用，报告审核签字后生效。
报告时间：2026-03-19
---
病案号:
11诊号:1K3392539b3
血型:FEI/CI独|业冰(111)
显像剂:18F-FDG
血糖:5.1mmol/l活
度:7.22mci注射部位:右手背静脉
注射/显像间隔时间:54分钟采集方式:断层采集3D厚
度:3.75mm采集仪器:Discovery MI
临床诊断:肺部阴影
简要病史:
肺部鳞癌基线评估。既往:2025.12肋骨骨折。
图像所见:
空腹4hr以上,口服适量温水,静脉注射显像剂,平静休息后行躯干PET及CT断层显像,PET图像行衰减校正及迭代
法重建,PET、CT图像行多层面、多幅显示,影像清晰。
颈部PET/CT示眼球、眼眶、鼻咽部、颈面部、喉咽部、甲状腺及颈部其它软组织结构、密度、代谢分布未见明显
异常。
胸部PET/CT示左肺下叶基底段近肺门部见高代谢结节,大小约2.0cm×1.9cm,边界不清,SUVmax约10.2。左肺
下叶远端见散在片絮状高密度影。左侧胸腔积液,部分呈包裹性。左侧胸膜见不均匀增厚,伴代谢增高,SUVmax约
4.0。右肺上叶胸膜下见微小结节,直径约0.2cm,代谢未见异常增高。主动脉、心脏生理性显像。
腹盆部PET/CT示肝左内叶包膜下见高代谢结节,SUVmax约5.4,CT显示密度轻微减低,边界不清。左侧肾上腺见
高代谢小结节,SUVmax约3.2,CT扫描局部稍增厚。胆囊、脾脏、胰腺大小正常,未见异常密度和异常代谢影。十二指
肠、双肾、右肾上腺、双输尿管、膀胱、前列腺及双侧精囊腺未见异常显像。腹腔内见多个形态不一、条管状、浓淡不
一的正常肠影。
淋巴结PET/CT示左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧锁骨区见多发淋巴结增大伴代谢增
高,较大者位于纵隔7组,大小约3.2×1.0cm,SUVmax约3.3。
骨骼、软组织及周围神经走行区PET/CT示左侧第8、9、10、11肋骨、右侧第6肋骨见骨质中断,部分伴骨赘形
成,伴代谢增高,SUVmax约3.8。左侧腹横肌见结节状增厚伴高代谢,SUVmax约2.9。全身其余骨骼、软组织及周围神
经未见异常代谢影像,骨质和肌肉密度未见明显改变。
I
诊断意见:
1.左肺下叶基底段近肺门部MT;左侧胸膜弥漫种植转移;左侧肺门、纵隔7组、4L组、5组、2R组、左侧内乳区及双侧
锁骨区多发淋巴结增大伴高代谢,考虑转移可能;肝S4包膜下转移瘤;左下叶远端阻塞性炎症;左胸腔癌性胸水可能
大;
2.左侧腹横肌转移瘤待除;左侧肾上腺转移待除,建议定期复查;
3.右肺上叶胸膜下少许炎性小结节;肝右叶少许小钙化灶;
4.双侧多根肋骨骨折伴骨赘区域炎性摄取;
5.全身其它部位18F-FDG PET/CT显像未见明显异常。
报告医师:林晓强
审核医师:
复核医师:
报告日期:2026-03-18
地址:福州市鼓楼区新权路29号电话:0591-833116130591-86218247
此报告仅供临床医师参考,不做证明使用。
---
福建医科大学附属协和医院
肺功能检查报告单
姓名：
性别：男
年龄：49 Years
病区床号：
科室：
病案号：
身高：163 cm
体重：61 kg
测试号：Z0280275PF20280320
预计值 实测值 实/预
VC MAX [L] 3.92 2.48 63.3
FVC [L] 3.77 2.48 65.8
FEV 1 [L] 3.10 2.22 71.8
FEV1%FVC [%] 81.86 89.56 109.4
PEF [L/B] 8.05 6.38 79.3
FIF25 [L/B] 7.01 6.16 87.9
FIF50 [L/B] 4.31 2.76 64.1
FIF75 [L/B] 1.64 1.29 78.4
FIF25-75 [L/B] 3.76 2.58 68.7
MVV [L/min] 116.58
TLC-SB [L] 5.94 4.72 79.4
FRC-SB [L] 3.17 3.74 118.1
RV-SB [L] 1.98 2.18 110.0
RV/TLC-SB [%] 33.07 46.21 139.7
FRC/TLC-SB [%] 54.09 79.16 146.3
DLCO SB [mmol/min/kPa] 8.85 5.98 67.6
DLCOc SB [mmol/min/kPa] 8.86 5.98 67.6
DLCO/VA [mmol/min/kPa/L] 1.49 1.30 87.1
DLCOc/VA [mmol/min/kPa/L] 1.49 1.30 87.1
1 本报告仅供临床参考，不作为任何诊断证明。
检查者：
审核者：
报告日期：2026/3/20
---
姓
住院
性别：男
年龄：40岁
送检单位：本院
送检科室：呼吸与危重症医学科 送检医生：黄世霜
送检日期：2026-03-10
临床诊断：肺炎。
送检材料：左肺下叶粘膜组织
肉眼所见：
灰白组织7块，直径0.05-0.2cm。（包全）
镜下所见：
病理诊断：
（左肺下叶粘膜组织）浸润性鳞状细胞癌。
诊断医师：廖荣娥
医生签名：廖荣娥
报告时间：2026年03月12
备注：
1 本报告仅作临床医师参考；若发现病理诊断与临床不相符时请立即与我科联系。
2 此报告需医生签名方为有效。
本报告仅作临床医师参考
联系电话： 0598-63067
2026-08-10 19:34:03,883 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 19:34:03,883 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "13 items, types={'LabReport': 5, 'AdmissionRecord': 1, 'ExaminationReport': 7}", "name": "BJCA,男，49，肺鳞癌一线(1).pdf", "embedding_token_consumption": 7839}
2026-08-10 19:34:03,883 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 19:34:04,140 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 19:34:04,140 INFO     29 [Trace] task=14e73730 | doc=BJCA,男，49，肺鳞癌一线(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":13,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 19:34:04,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(8, 101, 230, 163, 177) row[-1]=(8, 101, 245, 286, 299)
2026-08-10 19:34:04,146 INFO     29 [DIAG-EXECUTOR] row_position_int len=20 row[0]=(9, 95, 159, 138, 150) row[-1]=(9, 81, 177, 384, 396)
2026-08-10 19:34:04,146 INFO     29 [DIAG-EXECUTOR] row_position_int len=18 row[0]=(9, 421, 505, 138, 150) row[-1]=(9, 421, 499, 359, 371)
2026-08-10 19:34:04,146 INFO     29 [DIAG-EXECUTOR] row_position_int len=27 row[0]=(10, 79, 166, 101, 114) row[-1]=(10, 422, 497, 227, 239)
2026-08-10 19:34:04,146 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(11, 84, 197, 82, 96) row[-1]=(11, 84, 192, 204, 219)
2026-08-10 19:34:04,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:34:04,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:34:04,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:34:04,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:34:04,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:34:04,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:34:04,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:34:04,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:34:04,151 INFO     29 set_progress(14e7373094f111f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 19:34:04 [DOC Engine]:
Start to index...
2026-08-10 19:34:04,163 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-10 19:34:04,167 INFO     29 set_progress(14e7373094f111f1bd9827cf206dfa2d), progress: 0.8076923076923077, progress_msg: 
2026-08-10 19:34:04,185 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 19:34:04,204 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.012s]
2026-08-10 19:34:04,211 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.005s]
2026-08-10 19:34:04,216 INFO     29 set_progress(14e7373094f111f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 19:34:04 Indexing done (0.07s). Task done (542.00s)
2026-08-10 19:34:04,219 INFO     29 [Done], chunks(13), token(7839), elapsed:542.00
2026-08-10 19:34:04,406 INFO     29 handle_task done for task {"id": "14e7373094f111f1bd9827cf206dfa2d", "doc_id": "14840e4e94f111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "BJCA,\u7537\uff0c49\uff0c\u80ba\u9cde\u764c\u4e00\u7ebf(1).pdf", "size": 14521028, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786389858396, "task_type": "dataflow", "root_trace_id": "7671b373137945908ca96c87c605ef71", "root_traceparent": "00-7671b373137945908ca96c87c605ef71-d115f4678a7d3047-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
