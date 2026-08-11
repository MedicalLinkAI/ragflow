# 基准结果：腺癌TKI耐药ZHDO，39岁.pdf

## 基本信息

- 文件：`腺癌TKI耐药ZHDO，39岁.pdf`
- 大小：7763.4 KB
- PDF 总页数：22
- doc_id：`a144653494d011f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T23:31:59  完成时间：2026-08-10T23:43:28  耗时：689.5s
- progress_msg：`15:43:24 Indexing done (0.16s). Task done (643.37s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | f256e8ff | 2 | 1-2 | 入院记录 姓名： 性别：男 年龄：38岁 婚姻状况：已婚 出生地： 民族：汉族  |
| 2 | f67d202b | 1 | 3-3 | 出院证明书 (医院保存联) 姓名： 性别：男 年龄：38岁 入院时间：2025- |
| 3 | fbf23cdf | 2 | 4-5 | 医学影像检查报告单 住院 检查号： 患者姓名： 性别：男 患者年龄：38岁 申请 |
| 4 | 44fc4389 | 1 | 5-5 | 住院号 门诊号：- 病理号[ 姓名 性别 男 年龄 38岁 病人编号 病区 就诊 |
| 5 | 659ed1a4 | 2 | 6-7 | 检测概览 基本信息 受检者信息 样本信息 临床信息 姓名 样本编号： 临床/病理 |
| 6 | 10b35691 | 1 | 8-8 | 患者信息 姓名 性别 男 年龄 38岁 送检单位 样本信息 样本编号 样本类型  |
| 7 | 353e6708 | 1 | 9-9 | 出院证明书 (医院保存联) 住院证字 号 姓名 年龄：38岁 入院时间：2025 |
| 8 | 1b41afae | 1 | 10-10 | 出院证明书 (医院保存联) 住院证字 号 性别：男 年龄：39岁 入院时间：20 |
| 9 | 4f65b5ba | 1 | 11-11 | 出院证明书 (病人保存联) 住院证字 号 姓名： 性别：男 年龄：39岁 入院时 |
| 10 | 0596c335 | 1 | 12-12 | 民医院 出院证明书 (病人保存联) 住院证字 号 姓名： 性别：男 年龄：39岁 |
| 11 | 6965a23d | 2 | 13-14 | 入院记录 姓名： 性别：男 年龄： 婚姻状况：未婚 出生地： 民族：汉族 现住址 |
| 12 | 64bf3154 | 1 | 15-15 | 出院证明书 (病人保存联) 住院证字 号 性别：男 年龄：39岁 入院时间：20 |
| 13 | 92a016cf | 1 | 22-22 | 医学影像检查报告单 扫码查看影像 检查号: 患者姓名: 性别:男 年龄:39岁  |
| 14 | d9db015f | 1 | 19-19 | <table><tr><td>癌胚抗原</td><td>CEA</td><td> |
| 15 | 3ea7baa1 | 1 | 20-20 | <table><tr><td>凝血酶原时间</td><td>None</td>< |
| 16 | 0870dc64 | 1 | 21-21 | <table><tr><td>白细胞计数</td><td>None</td><t |
| 17 | 2a280739 | 1 | 16-16 | <table><tr><td>标本颜色</td><td>None</td><td |
| 18 | 88cc33b2 | 1 | 17-17 | <table><tr><td>颜色</td><td>None</td><td>淡 |
| 19 | 2a8207a2 | 1 | 18-18 | <table><tr><td>总蛋白</td><td>None</td><td> |

- chunks 总数：19
- 各 chunk 页数合计（含跨页重复）：23
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]`
- 覆盖页数：22 / 22；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 2 | 2 | 2 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 6 | 6 | 6 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 5 | 5 | 5 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 6 | 0 | 6 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 2, "DischargeRecord": 6, "ExaminationReport": 5, "LabReport": 6}`
- ChunkMerger：`{"found": true, "merged": 19, "sources": 9, "stats": {"Extractor:LabExam": 6, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 6, "Extractor:Admission": 2, "Extractor:ExaminationReport": 5, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 15:43:20,861 INFO     29 [ChunkMerger] Merged 19 chunks from 9 sources: {'Extractor:LabExam': 6, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 15:32:02,775 INFO     29 handle_task begin for task {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 15:32:02,980 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 15:32:03,095 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 15:32:03,112 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:32:03,112 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 15:32:03,112 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 15:32:03,117 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 15:32:03,117 INFO     29 ============================================================
2026-08-10 15:32:03,117 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 15:32:03,117 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 15:32:03,117 INFO     29 ============================================================
2026-08-10 15:32:03,117 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 15:32:03,117 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 15:32:03,119 INFO     29 No torch found.
2026-08-10 15:32:05,958 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=22
2026-08-10 15:32:06,536 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4944837, prompt_len=764
2026-08-10 15:32:08,030 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:32:08,032 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 15:32:08,059 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4944837, prompt_len=401
2026-08-10 15:32:14,627 INFO     29 [qwen-vl-parser] text API response (len=1134):
["入院记录", "姓名：", "性别：男", "年龄：38岁", "婚姻状况：已婚", "出生地：", "民族：汉族", "现住址：", "职业：自由职业者", "入院时间：2025-09-09 10:41", "记录时间：2025-09-09 11:01", "病史陈述者", "联系人姓名：", "联系人电话：", "病史真实性确认签字：", "主诉：咳嗽3+月，发现右上肺占位10+天", "现病史：入院前3+月，患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。10+天前，患", "民医院就诊，完善胸部CT", "提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑", "占位性病变，肺Ca可能性大。建议结合临床进一步检查。2.双肺散在点结影及条索影。3.纵隔内可见", "淋巴结显示，部分稍大。4.心脏形态大小未见异常。5.双侧胸腔未见确切积液征象。6.扫及肝右叶见", "片状密度低影，长径约2.7cm，性质?建议进一步检查。7.扫及胸椎多个椎体骨质密度减低破坏改", "变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+", "NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段", "测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺", "另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分", "稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，", "必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破", "坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.电轴左偏。建议完善经皮肺穿刺", "检查后纤支镜下肺活检明确，患方商议后表示拒绝，现患者为进一步明确占位性质，遂于我院门诊就", "诊，门诊以“右上肺占位”收入我科。", "自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。", "既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病", "史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。", "过敏史：否认食物、药物过敏史。", "个人史：出生原籍，长期居住生长于当地，否认疫区居住治游史，平素偶有饮酒，否认吸烟及"]
2026-08-10 15:32:14,628 INFO     29 [qwen-vl-parser] page=1 text: 36 lines (bbox 0-35)
2026-08-10 15:32:14,629 INFO     29 [qwen-vl-parser] page=1 text: 36 sections
2026-08-10 15:32:15,122 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4255547, prompt_len=764
2026-08-10 15:32:16,646 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:32:16,649 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 15:32:16,680 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4255547, prompt_len=401
2026-08-10 15:32:22,525 INFO     29 [qwen-vl-parser] text API response (len=956):
["人民医院", "入院记录", "家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。", "体格检查", "T36.1℃", "P92次/分", "R19次/分", "BP121/83mmHg", "一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮", "疹。背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部", "及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。", "颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊", "清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，HR92次/分，律齐，各", "瓣膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性", "浊音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经", "系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。", "专科情况", "背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。胸廓正常，双肺语颤正常，双肺叩诊清", "音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，HR92次/分，律齐，各瓣膜区未闻", "及病理性杂音。", "辅助检查", "2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇", "化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块,", "肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在", "斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低", "密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎", "体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦", "性心律 2.由缺血性"]
2026-08-10 15:32:22,526 INFO     29 [qwen-vl-parser] page=2 text: 28 lines (bbox 36-63)
2026-08-10 15:32:22,526 INFO     29 [qwen-vl-parser] page=2 text: 28 sections
2026-08-10 15:32:22,968 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5500961, prompt_len=764
2026-08-10 15:32:24,704 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:32:24,705 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 15:32:24,736 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5500961, prompt_len=401
2026-08-10 15:32:27,390 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:32:27.389+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:32:32,241 INFO     29 [qwen-vl-parser] text API response (len=973):
["出院证明书", "(医院保存联)", "姓名：", "性别：男", "年龄：38岁", "入院时间：2025-09-09 10:41", "住院证字", "号", "出院时间：2025-09-12", "病人单位或住址：", "出院诊断：1.右肺上叶腺癌cT4N1M1c IVB期（伴多发骨、肝脏、脑转移） 2.肝继发恶性肿瘤？ 3.", "多发骨继发恶性肿瘤？ 4.中脑继发恶性肿瘤？ 5.癌性疼痛", "诊疗小结：患者因“咳嗽3+月，发现右上肺占位10+天”入院。辅助检查：2025-09-01 [*胸部,增", "强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右", "肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸", "膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧", "部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨", "折可能。2025-09-11 [*头部,MRI平扫] [头部,DWI],1、中脑内异常信号影，占位性病变？脱髓鞘病", "变？缺血灶？其它？2、扫及右侧上颌窦囊肿可能。请结合临床及其它检查。2025-09-01 CYFRA21-1", "+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞", "角蛋白19片段测定 62.83(ng/ml)↑；2025-09-09 血常规(五分类):白细胞计数 10.51(10^9/L)↑，", "中性粒细胞百分率 80.40(%)↑，中性粒细胞计数 8.45(10^9/L)↑。心电图：1.窦性心律 2.电轴左", "偏。", "诊疗经过：[入院后完善相关辅助检查，于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病", "理科腺癌可能性大，报告未回，现患者要求院外等待结果，予以办理出院。]", "治疗结果：好转", "出院医嘱及建议：1、注意休息，避免受凉感冒及劳累；2、院外追踪免疫组化结果，待结果回示后", "及时呼吸内科门诊就诊；3、呼吸科、肿瘤科门诊随访，如有不适，请及时就医。"]
2026-08-10 15:32:32,242 INFO     29 [qwen-vl-parser] page=3 text: 28 lines (bbox 64-91)
2026-08-10 15:32:32,242 INFO     29 [qwen-vl-parser] page=3 text: 28 sections
2026-08-10 15:32:32,504 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1633917, prompt_len=764
2026-08-10 15:32:33,939 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-01"}
```
2026-08-10 15:32:33,939 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-09-01
2026-08-10 15:32:33,956 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1633917, prompt_len=401
2026-08-10 15:32:38,446 INFO     29 [qwen-vl-parser] text API response (len=768):
["人民医院", "川渝HR", "带*为川渝互认项目", "医学影像检查报告单", "住院", "检查号：", "患者姓名：", "性别：男", "患者年龄：38岁", "申请科室：", "床号：", "设备名称：CT1(联影CT)(1住)", "检查部位：[*胸部,增强]", "联系电话：", "检查技师：", "检查时间：2025-09-01 08:34:37", "报告时间：2025/9/1 9:31:33", "描述：", "右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截", "断，较大层面范围约7.9cm×6.9cm，增强扫描呈轻度不均匀强化，周围", "见斑条影及小结节影。双肺另见长径约0.4-0.6cm实性小结节。右肺中", "叶及双肺下叶见散在斑条影。纵膈见多发淋巴结显示，部分稍大。心脏", "不大，心包少量积液。左侧胸膜稍增厚。肝右叶见数个类圆形低密度", "影，较大者长径约2.5cm，增强扫描两期强化程度CT值相差25HU。扫及", "双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破", "坏，T2椎体见多发骨折线影。", "总结意见：", "1、右肺上叶团块，肿瘤占位性病变可能，其它待排。", "2、双肺另见小结节，必要时随诊。", "3、右肺中叶及双肺下叶见散在斑条影。", "4、纵膈见多发淋巴结显示，部分稍大。", "5、心包少量积液。左侧胸膜稍增厚。", "6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步", "检查。", "7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨", "性骨质破坏，转移灶可能，T2椎体病理性骨折可能。", "请结合临床及其它检查，必要时复查或进一步检查。", "报告者：申悦", "审核医师：马婉军"]
2026-08-10 15:32:38,447 INFO     29 [qwen-vl-parser] page=4 text: 39 lines (bbox 92-130)
2026-08-10 15:32:38,447 INFO     29 [qwen-vl-parser] page=4 text: 39 sections
2026-08-10 15:32:38,892 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2444089, prompt_len=764
2026-08-10 15:32:40,375 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-15"}
```
2026-08-10 15:32:40,377 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2025-09-15
2026-08-10 15:32:40,397 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2444089, prompt_len=401
2026-08-10 15:32:42,668 INFO     29 [qwen-vl-parser] text API response (len=377):
["页 尾页", "共1页,共1条记", "住院号", "门诊号：-", "病理号[", "姓名", "性别 男", "年龄 38岁", "病人编号", "病区", "就诊号", "收到日期 2025-09-10", "送检科室", "送检单位 本院", "送检医生", "标本名称 右肺包块", "临床诊断", "肉眼所见", "(右肺包块)灰白色组织多粒,直径0.4cm,点纸全", "病理诊断", "(右肺包块,穿刺活检)结合免疫组化结果:癌细胞CK(+),CK7(+),TTF-1(+),NapsinA(+),Ki67(+,约60%),CK20(-),SATB2(-),", "支持肺腺癌。", "报告医生 阙柳", "审核医生 阙柳", "复诊医生", "报告时间 2025-09-15", "欢迎使用朗珈PathQC病理质控与资料管理系统"]
2026-08-10 15:32:42,668 INFO     29 [qwen-vl-parser] page=5 text: 27 lines (bbox 131-157)
2026-08-10 15:32:42,668 INFO     29 [qwen-vl-parser] page=5 text: 27 sections
2026-08-10 15:32:42,786 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1028732, prompt_len=764
2026-08-10 15:32:44,193 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-21"}
```
2026-08-10 15:32:44,194 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2025-09-21
2026-08-10 15:32:44,206 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1028732, prompt_len=401
2026-08-10 15:32:50,761 INFO     29 [qwen-vl-parser] text API response (len=1390):
["检测概览", "基本信息", "受检者信息", "样本信息", "临床信息", "姓名", "样本编号：", "临床/病理诊断：肺癌怀疑骨转移肝转移", "性别：男", "样本类型：石蜡块", "手术史/用药史：/", "年龄：38岁", "采样部位：/", "既往基因检测结果：/", "送检单位", "家族史：/", "采集日期：", "接收日期：2025-09-18", "报告日期：2025-09-21", "本报告中的临床诊断等信息来自受检者送检时提供的信息，而非来自检测结果。", "项目简介", "项目名称", "肺癌靶向18基因检测", "检测方法", "目标区域探针捕获技术和二代测序技术(Next-Generation Sequencing,NGS)", "检测范围", "本检测基于非小细胞肺癌指南和专家共识，检测非小细胞肺癌靶向治疗和预后相关的18个基因(包括：EGFR、ALK、MET、ROS1、BRAF、RET、ERBB2(HER2)、KRAS、NTRK1/2/3、NRAS、PIK3CA、AKT1、FBXW7、DDR2、NRG1、TP53)，变异类型包含相应基因的点突变、插入/缺失，拷贝数变异和基因融合/重排。", "检测流程", "核酸提取、文库制备、高通量测序、生物信息分析及报告解读", "参考指南及数据库", "NCCN指南、CSCO指南、OncoKB、COSMIC、CKB、ClinVar等", "参考基因组", "GRCh37/hg19", "检测结果汇总", "基因变异结果（共5个）", "基因", "转录本/外显子", "cDNA改变", "氨基酸改变", "变异类型", "变异丰度/拷贝数", "变异分类", "EGFR", "NM_005228.5:exon21", "c.2573T>G", "p.L858R", "错义突变", "51.28%", "I类[重要临床意义]", "ERBB2(HER2)", "NM_004448.4", "/", "/", "拷贝数扩增", "拷贝数=3.6", "I类[重要临床意义]", "MET", "NM_000245.4", "/", "/", "拷贝数扩增", "拷贝数=3.1", "I类[重要临床意义]", "TP53", "NM_000546.6:exon6", "c.598_611del", "p.N200Vfs*4", "移码突变", "61.75%", "II类[潜在临床意义]", "第1页", "TP53", "NM_000546.6:exon6", "c.629A>C", "p.N210T", "错义突变", "62.88%", "III类[临床意义不明]", "注：", "《肿瘤二代测序临床报告解读共识》指出，基因变异按照其临床意义的重要性分为4类：", "I类：有重要的临床意义，与治疗、预后和诊断相关；", "II类：有潜在的临床意义，与治疗、预后和诊断相关；", "III类：临床意义不明(临床意义不明是指目前尚无充分证据证实这些基因变异与肿瘤的致病性关系，尚无相关用药提示，未来可能随着研究的深入而更新致病性及药物证据等级)；", "IV类变异，无害或可能无害。", "本报告只列出I、II、III类变异。", "靶向用药基因检测提示"]
2026-08-10 15:32:50,763 INFO     29 [qwen-vl-parser] page=6 text: 86 lines (bbox 158-243)
2026-08-10 15:32:50,763 INFO     29 [qwen-vl-parser] page=6 text: 86 sections
2026-08-10 15:32:50,855 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=733647, prompt_len=764
2026-08-10 15:32:52,090 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:32:52,090 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 15:32:52,104 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=733647, prompt_len=401
2026-08-10 15:32:59,111 INFO     29 [qwen-vl-parser] text API response (len=1678):
["靶向用药基因检测提示", "基因", "变异信息", "变异丰度/拷贝数", "(A级)", "FDA/NMPA", "指南推荐用药", "(B级)", "专家共识推荐用药", "(C级)", "跨适应症", "(C级)", "临床试验药物", "(D级)", "临床前研究", "奥希替尼", "(敏感)", "奥希替尼+", "化疗", "(敏感)", "埃万妥单抗+", "兰泽替尼", "(敏感)", "埃万妥单抗+", "化疗", "(敏感)", "阿美替尼", "(敏感)", "伏美替尼", "(敏感)", "达可替尼", "(敏感)", "吉非替尼", "(敏感)", "阿法替尼±", "西妥昔单抗", "(敏感)", "埃克替尼", "(敏感)", "贝福替尼", "(敏感)", "厄洛替尼±", "雷莫西尤单抗", "或贝伐珠单抗", "(敏感)", "瑞厄替尼", "(敏感)", "瑞齐替尼", "德达博妥单抗+", "奥希替尼", "(敏感)", "Patritumab", "Deruxtecan", "(敏感)", "BDTX-1535", "(敏感)", "WSD0922", "(敏感)", "HLX42", "(敏感)", "SHR-A2009", "(敏感)", "BL-B01D1", "(敏感)", "阿美替尼+", "化疗", "(敏感)", "EGFR", "c.2573T>G,", "p.L858R,", "Exon21", "51.28%", "/", "/", "/", "/", "第 2 页", "(敏感)", "佐利替尼", "(敏感)", "利厄替尼", "(敏感)", "德达博妥单抗", "(敏感)", "芦康沙妥珠单", "抗", "(敏感)", "依沃西单抗+", "培美曲塞+", "卡铂", "(敏感)", "奥希替尼+", "赛沃替尼", "(敏感)", "伯瑞替尼", "(敏感)", "克唑替尼", "(敏感)", "卡马替尼", "(敏感)", "特泊替尼", "(敏感)", "EGFR-TKIs", "(耐药)", "谷美替尼", "(敏感)", "EGFR-TKIs+", "MET-TKIs", "(敏感)", "/", "伯瑞替尼+", "PLB1004", "(敏感)", "SYM015", "(敏感)", "特泊替尼+", "吉非替尼", "(敏感)", "特泊替尼+", "奥希替尼", "(敏感)", "赛沃替尼", "(敏感)", "MET", "扩增", "拷贝数", "=3.1", "/", "德曲妥珠单", "抗", "(敏感)", "泽尼达妥单", "抗", "(敏感)", "帕博利珠单", "抗+", "曲妥珠单抗+", "化疗", "(敏感)", "帕妥珠单抗+", "曲妥珠单抗+", "化疗", "(敏感)", "恩美曲妥珠", "单抗", "(敏感)", "维迪西妥单", "抗", "(敏感)", "吡咯替尼", "(敏感)", "阿法替尼", "(敏感)", "帕妥珠单抗+", "曲妥珠单抗", "(敏感)", "吡咯替尼+", "阿帕替尼", "(敏感)", "维迪西妥单抗+", "替雷利珠单抗+", "贝伐珠单抗", "(敏感)", "维迪西妥单抗+", "安罗替尼", "(敏感)", "ERBB2", "(HER2)", "扩增", "拷贝数", "=3.6", "EGFR-TKIs", "(耐药)", "/", "Tarloxotinib", "(敏感)", "TAS0728", "(敏感)", "BDTX-189", "(敏感)", "c.598_611del", "p.N200Vfs*4", "Exon6", "61.75%", "/", "/", "/", "Adavosertib", "(敏感)", "CTX-1", "(敏感)", "CEP-8983", "(敏感)", "TP53"]
2026-08-10 15:32:59,112 INFO     29 [qwen-vl-parser] page=7 text: 194 lines (bbox 244-437)
2026-08-10 15:32:59,112 INFO     29 [qwen-vl-parser] page=7 text: 194 sections
2026-08-10 15:32:59,152 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:32:59.151+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:32:59,196 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=588745, prompt_len=764
2026-08-10 15:33:00,545 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-09-20"
}
```
2026-08-10 15:33:00,545 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-09-20
2026-08-10 15:33:00,560 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=588745, prompt_len=401
2026-08-10 15:33:04,225 INFO     29 [qwen-vl-parser] text API response (len=378):
["患者信息", "姓名", "性别", "男", "年龄", "38岁", "送检单位", "样本信息", "样本编号", "样本类型", "采样部位", "样本采集日期", "样本接收日期", "报告日期", "石蜡块", "—", "2025-09-18", "2025-09-20", "检测项目", "PD-L1蛋白表达检测", "抗体型号", "临床信息", "临床/病理诊断", "肺癌怀疑骨转移肝转移", "手术史/用药史", "—", "二、检测结果", "检测内容", "检测结果", "检测结果提示", "PD-L1蛋白", "TPS", "<1%", "PD-L1蛋白表达。", "表达水平", "CPS", "1", "TC", "<1%", "IC", "1%", "检测结果图示", "PDL1×200", "HE×200"]
2026-08-10 15:33:04,226 INFO     29 [qwen-vl-parser] page=8 text: 44 lines (bbox 438-481)
2026-08-10 15:33:04,226 INFO     29 [qwen-vl-parser] page=8 text: 44 sections
2026-08-10 15:33:04,512 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1762250, prompt_len=764
2026-08-10 15:33:05,876 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:33:05,877 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 15:33:05,894 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1762250, prompt_len=401
2026-08-10 15:33:14,026 INFO     29 [qwen-vl-parser] text API response (len=1382):
["出院证明书", "(医院保存联)", "住院证字", "号", "姓名", "年龄：38岁 入院时间：2025-12-04 09:00", "科", "床号：029 出院时间：2025-12-07", "病人单位或住址", "出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR", "L858R+）3.恶性肿瘤靶向治疗 4.肝继发恶性肿瘤 5.骨继发恶性肿瘤 6.化疗相关恶心和呕吐 7.", "化疗后骨髓抑制 8.轻度贫血", "诊疗小结：患者因“发现右肺上叶占位5+月，右肺上叶腺癌靶向治疗中。”入院。入院查体：", "T36.5℃，P75次/分，R20次/分，BP127/82mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语", "颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣", "膜区未闻及病理性杂音。]辅助检查：暂缺。", "诊疗经过：[入院完善相关检查2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋", "白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌", "素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。2025-12-04 胸腹部增", "强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较", "大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较", "CT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中", "叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边", "缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它", "病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约", "1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右", "肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前", "列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂", "骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理", "性骨折待排。病情评价好转，给于唑来磷酸预防骨相关事件。排除化疗禁忌于2025-12-5行第1周期AC", "方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼 110mg", "qd，化疗中给于抑酸、护胃、止吐等对症治疗，化疗顺利，患者无明显不适。化疗后复查血常规提", "示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。]", "治疗结果：好转", "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "第1页/共2页"]
2026-08-10 15:33:14,026 INFO     29 [qwen-vl-parser] page=9 text: 36 lines (bbox 482-517)
2026-08-10 15:33:14,026 INFO     29 [qwen-vl-parser] page=9 text: 36 sections
2026-08-10 15:33:14,283 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1646454, prompt_len=764
2026-08-10 15:33:15,613 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:33:15,613 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 15:33:15,631 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1646454, prompt_len=401
2026-08-10 15:33:22,031 INFO     29 [qwen-vl-parser] text API response (len=1114):
["出院证明书", "(医院保存联)", "住院证字", "号", "性别：男 年龄：39岁 入院时间：2025-12-29 09:54", "床号： 出院时间：2025-12-31", "病人单位或住址", "出院诊断：1.姑息性化疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）", "3.肝继发恶性肿瘤 4.骨继发恶性肿瘤 5.化疗相关性恶心和呕吐 6.化疗相关性吞咽困难 7.肝功", "能不全", "诊疗小结：患者因“发现右肺上叶占位6+月，右肺上叶腺癌1周期化疗后20+天。”入院。入院查", "体：T36.7℃；P85次/分；R18次/分；BP117/81mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺", "语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各", "瓣膜区未闻及病理性杂音。", "诊疗经过：患者入院后完善相关检查，2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，", "中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；", "2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急", "诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬", "氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。患者无化疗禁忌，于2025-12-30行第2周期AC方案化", "疗，具体方案为：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w，同时给予患者抑酸护胃、止", "痛等对症支持治疗，今日安排患者出院。", "治疗结果：好转", "出院医嘱及建议：1、注意休息，加强营养；2、每周复查血常规2次、肝肾功1次，如有异常，立即", "就诊。3、下周期化疗时间：2026-01-20，住院前请提前联系床位。4、出院用药：利可君片 1片 口", "服 每天3次，生血宝合剂 15ml 口服 每天3次。5、", "午", "6、我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午。", "备注（包括手术名称）：[手术记录手术名称]", "时间：2025年12月31日", "说明：1、此证明书未经我院加盖公章无效。 2、涂改未经加盖我院公章无效。", "3、此证明仅证明病人出院时病情。 4、请妥善保管，遗失不补。", "第1页/共2页"]
2026-08-10 15:33:22,031 INFO     29 [qwen-vl-parser] page=10 text: 32 lines (bbox 518-549)
2026-08-10 15:33:22,031 INFO     29 [qwen-vl-parser] page=10 text: 32 sections
2026-08-10 15:33:22,370 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2163050, prompt_len=764
2026-08-10 15:33:23,768 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:33:23,768 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 15:33:23,779 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2163050, prompt_len=401
2026-08-10 15:33:30,949 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:33:30.946+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:33:32,435 INFO     29 [qwen-vl-parser] text API response (len=1470):
["出院证明书", "(病人保存联)", "住院证字", "号", "姓名：", "性别：男", "年龄：39岁", "入院时间：2026-01-21 10:07", "出院时间：2026-01-24", "病人单位或住址", "出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR", "L858R+）", "3.恶性肿瘤靶向治疗", "4.肝继发恶性肿瘤", "5.骨继发恶性肿瘤", "6.化疗相关恶心和呕吐", "7.化疗后骨髓抑制", "8.白细胞减少", "9.恶性肿瘤的治疗后的随诊检查", "诊疗小结：患者因“发现右肺上叶占位7月，右肺上叶腺癌2周期化疗后20+天。”入院。入院查体：", "T36.6℃，P76次/分，R19次/分，BP113/75mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语", "颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣", "膜区未闻及病理性杂音。]辅助检查：暂缺。", "诊疗经过：[入院完善相关检查：2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红", "蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80", "(U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+", "ProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前", "体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。2026-01-22 胸腹部CT：1、“肺CA”复查，右", "肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，", "增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另", "见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺", "下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸", "膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大", "层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增", "粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前", "变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐", "骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。病情评价好转，排除于2026-1-23", "行第3周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w，同时给予", "患者抑酸护胃、止痛等对症支持治疗，现化疗已完成，于今出院回家乡休养。]", "治疗结果：好转", "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "诊。2、下周期治疗时间：2026年2月13日，请提前几天微信群预约床位，入院前尽量保持空腹状", "第1页/共2页"]
2026-08-10 15:33:32,436 INFO     29 [qwen-vl-parser] page=11 text: 43 lines (bbox 550-592)
2026-08-10 15:33:32,436 INFO     29 [qwen-vl-parser] page=11 text: 43 sections
2026-08-10 15:33:32,717 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1755195, prompt_len=764
2026-08-10 15:33:35,947 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:33:35,947 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-10 15:33:35,969 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1755195, prompt_len=401
2026-08-10 15:33:42,236 INFO     29 [qwen-vl-parser] text API response (len=1120):
["民医院", "出院证明书", "(病人保存联)", "住院证字", "号", "姓名：", "性别：男", "年龄：39岁", "入院时间：2026-02-24 09:09", "出院时间：2026-02-26", "病人单位或住址：", "出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）", "2.肝继发恶性肿", "瘤", "3.骨继发恶性肿瘤", "4.恶性肿瘤靶向治疗", "5.化疗后血小板减少", "6.姑息性化疗", "诊疗小结：患者因“右肺上叶腺癌3周期化疗后20+天。”入院。入院查体：T36.4℃；P93次/分；", "R18次/分；BP107/70mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，", "双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。", "诊疗经过：完善检查，2026-02-24", "血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24", "CEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；", "2026-02-24", "凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU)", "↑；2026-02-24", "急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急", "诊)：钠 136.00(mmol/L)↓；患者无化疗禁忌，2026-02-25开始行第4周期AC方案化疗，具体方案", "为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼110mg po qd，患者治疗结束，复", "查2026-02-26[左上肢静脉,血管彩超]，左上肢静脉未见明显异常。予以拔除PICC管后办理出院。", "治疗结果：好转", "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "诊。2、下周期治疗时间：2026年3月18日，肿瘤科门诊或日间放化疗门诊完成治疗。3、出院带", "药：-。4、", "5、加强营养，清淡饮食，避免着凉，预防感染，不适随诊。", "备注(包括手术名称)：[手术记录手术名称]", "时间：2026年02月26日", "说明：1、此证明书未经我院加盖公章无效。", "2、涂改未经加盖我院公章无效。", "3、此证明仅证明病人出院时病情。", "4、请妥善保管，遗失不补。"]
2026-08-10 15:33:42,236 INFO     29 [qwen-vl-parser] page=12 text: 42 lines (bbox 593-634)
2026-08-10 15:33:42,236 INFO     29 [qwen-vl-parser] page=12 text: 42 sections
2026-08-10 15:33:42,518 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1788666, prompt_len=764
2026-08-10 15:33:43,878 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:33:43,879 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 15:33:43,903 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1788666, prompt_len=401
2026-08-10 15:33:51,341 INFO     29 [qwen-vl-parser] text API response (len=1344):
["人民医院", "入院记录", "姓名：", "性别：男", "年龄：", "婚姻状况：未婚", "出生地：", "民族：汉族", "现住址：", "职业：自由职业者", "入院时间：2026-03-23 10:38", "记录时间：2026-03-23 10:46", "病史陈述者：", "联系人姓名：", "联系人电话：", "病史真实性确认签字：", "主诉：右肺上叶腺癌4周期化疗后1+月。", "现病史：2025-06患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未", "行治疗，病程中患者上述症状持续存在。", "民医院就诊，完善胸部CT提示“1.右上肺见", "团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca", "可能性大。3.纵隔内可见淋巴结显示，部分稍大。扫及肝右叶见片状密度低影，长径约2.7cm，性", "质？，扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住", "院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性", "烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑，行胸部增强CT检查示：右肺上", "叶团块，肿瘤占位性病变可能，其它待排。纵膈见多发淋巴结显示，部分稍大。肝右叶低密度结节，", "占位性病变可能，转移灶待排，扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性", "骨质破坏，转移灶可能，T2椎体病理性骨折可能。于2025-09-10行经皮肺穿刺活检，免疫组化结果电", "话询问病理科腺癌可能性大，2025-09-15报告回示：病理诊断（右肺包块，穿刺活检）结合免疫组化", "结果：癌细胞CK（+），CK7（+），TTF-1（+），NapsinA（+），Ki67（+，约60%），CK20（-），", "SATB2（-），支持肺腺癌。基因检查示：EGFR L858R+,MET 扩增，ERBB2 扩增，TP53突变，PD-L1<", "1%。于2025-09-24开始口服阿美替尼靶向治疗（110mg po qd）。2025-12-04复查胸腹部增强CT：病", "情评价好转。于2025-12-5、2025-12-30、2026-1-23、2026-02-05行4周期AC方案化疗联合靶向治", "疗，具体：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w+阿美替尼 110mg qd。现患者为进一", "步治疗于我院就诊，门诊以“右肺上叶腺癌”收入我科。", "自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。", "既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病", "史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。", "过敏史：否认食物、药物过敏史。", "个人史：出生原籍，长期居住生长于当地，否认疫区居住冶游史，平素偶有饮酒，否认吸烟及", "第1页"]
2026-08-10 15:33:51,342 INFO     29 [qwen-vl-parser] page=13 text: 41 lines (bbox 635-675)
2026-08-10 15:33:51,342 INFO     29 [qwen-vl-parser] page=13 text: 41 sections
2026-08-10 15:33:51,578 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1343385, prompt_len=764
2026-08-10 15:33:52,890 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:33:52,891 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-10 15:33:52,910 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1343385, prompt_len=401
2026-08-10 15:33:57,248 INFO     29 [qwen-vl-parser] text API response (len=712):
["入院记录", "其他不良嗜好。", "婚育史：适龄结婚，育有1子，家人均体健。", "家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。", "体格检查", "T36.4℃", "P95次/分", "R19次/分", "BP101/77mmHg", "一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮", "疹。背部可触及一大约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部", "及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。", "颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊", "清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，H95次/分，律齐，各瓣", "膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊", "音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经", "系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。", "专科情况", "ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰", "音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。", "辅助检查", "暂缺。", "初步诊断：", "1.右肺上叶腺癌伴肝脏、骨多发转移（", "cT4N2M1 IVB期 EGFR L858R+）", "2.肝继发恶性肿瘤", "3.骨继发恶性肿瘤", "医师签名", "第2页"]
2026-08-10 15:33:57,249 INFO     29 [qwen-vl-parser] page=14 text: 29 lines (bbox 676-704)
2026-08-10 15:33:57,249 INFO     29 [qwen-vl-parser] page=14 text: 29 sections
2026-08-10 15:33:57,525 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1772924, prompt_len=764
2026-08-10 15:33:58,892 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:33:58,893 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-10 15:33:58,902 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1772924, prompt_len=401
2026-08-10 15:34:02,721 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:34:02.720+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:34:08,579 INFO     29 [qwen-vl-parser] text API response (len=1369):
["出院证明书", "(病人保存联)", "住院证字", "号", "性别：男 年龄：39岁 入院时间：2026-03-23 10:38", "床号", "出院时间：2026-03-25", "病人单位或住址：", "出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+） 2.肝继发恶性肿", "瘤 3.骨继发恶性肿瘤 4.肝功能不全", "诊疗小结：患者因“右肺上叶腺癌4周期化疗后1+月。”入院。入院查体：T36.4℃ ;P93次/分；", "R18次/分;BP107/70mmHg", "诊疗经过：完善检查，2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急", "诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；", "2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml)", "↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L", "FEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L)", "↓。2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右", "肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，", "增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另", "见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右", "肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增", "厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范", "围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节", "状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、", "胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，", "增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠", "均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双", "侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。患者肝", "功能不全，予以保肝治疗，患者病情进展，考虑参加临床实验，予以办理出院。", "治疗结果：好转", "出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。 2、等待电话通", "知临床试验筛查。 3、出院带药：-。4、门诊随访：", "5、加强营养，清淡饮食，避免着凉，预防感", "第1页/共2页"]
2026-08-10 15:34:08,579 INFO     29 [qwen-vl-parser] page=15 text: 35 lines (bbox 705-739)
2026-08-10 15:34:08,580 INFO     29 [qwen-vl-parser] page=15 text: 35 sections
2026-08-10 15:34:08,793 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=964263, prompt_len=764
2026-08-10 15:34:10,074 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 15:34:10,075 INFO     29 [qwen-vl-parser] page=16 classify=table report_date=None
2026-08-10 15:34:10,102 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=964263, prompt_len=756
2026-08-10 15:34:12,159 INFO     29 [qwen-vl-parser] table API response (len=364):
\begin{tabular}{ccccccl}
\hline
NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 \\
\hline
1 & 标本颜色 & 黄色 & & & \\
2 & 标本性状 & 半稀便 & & & \\
3 & 红细胞 & 无 & /HP & 无 & 仪器法 \\
4 & 镜下白细胞 & 无 & /HP & 无 & 仪器法 \\
5 & 吞噬细胞 & 无 & /HP & 无 & 仪器法 \\
6 & 酵母样菌 & 无 & /HP & 无 & 仪器法 \\
7 & 脂肪球 & 无 & /HP & 无 & 仪器法 \\
8 & 脓细胞 & 无 & /HP & 无 & 仪器法 \\
9 & 淀粉样颗粒 & 无 & /HP & 无 & 仪器法 \\
\hline
\end{tabular}
2026-08-10 15:34:12,162 INFO     29 [qwen-vl-parser] page=16 table: 15 LaTeX lines (bbox 740-754)
2026-08-10 15:34:12,162 INFO     29 [qwen-vl-parser] page=16 table: 15 sections
2026-08-10 15:34:12,389 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102398, prompt_len=764
2026-08-10 15:34:13,883 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-10 15:34:13,883 INFO     29 [qwen-vl-parser] page=17 classify=table report_date=2026-03-23
2026-08-10 15:34:13,899 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102398, prompt_len=756
2026-08-10 15:34:16,711 INFO     29 [qwen-vl-parser] table API response (len=550):
\begin{tabular}{llllllll}
\hline
NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\
\hline
1 & 颜色 & 淡黄色 & & & & & \\
2 & 浊度 & 透明 & & & & & \\
\multicolumn{8}{l}{尿干化学分析} \\
3 & *尿胆原 & & & & 偶氮结合法 & & \\
4 & *胆红素 & & & & 偶氮偶合法 & & \\
5 & *酮体 & & & & 硝普化钠法 & & \\
6 & *尿潜血 & & & & 血红蛋白接触活性法 & & \\
7 & *尿蛋白 & & & & 蛋白质误差法 & & \\
9 & *亚硝酸盐 & & & & 硝酸盐还原法 & & \\
8 & 维生素C & & & & 干化学法 & & \\
10 & *白细胞 & & & & 酯酶法 & & \\
11 & *葡萄糖 & & & & 葡萄糖氧化酶法 & & \\
12 & *尿比重 & 1.025 & & 1.003-1.030 & 多聚电解质法 & & \\
13 & *PH值 & 5.00 & & 4.5-8.0 & 指示剂法 & & \\
\hline
\end{tabular}
2026-08-10 15:34:16,712 INFO     29 [qwen-vl-parser] page=17 table: 21 LaTeX lines (bbox 755-775)
2026-08-10 15:34:16,712 INFO     29 [qwen-vl-parser] page=17 table: 21 sections
2026-08-10 15:34:16,928 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1180802, prompt_len=764
2026-08-10 15:34:18,413 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-10 15:34:18,413 INFO     29 [qwen-vl-parser] page=18 classify=table report_date=2026-03-23
2026-08-10 15:34:18,424 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1180802, prompt_len=756
2026-08-10 15:34:23,486 INFO     29 [qwen-vl-parser] table API response (len=979):
\begin{tabular}{ccclllll}
\hline
NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\
\hline
1 & *总蛋白 & 81.60 & g/L & 65-85 & 比色法 & & \\
2 & *白蛋白 & 44.30 & g/L & 40-55 & 比色法 & & \\
3 & 球蛋白 & 37.30 & g/l & 20-40 & 计算法 & & \\
4 & *丙氨酸氨基转移酶 & 84.50 & U/L & 9-50 & 比色法 & & \\
5 & *天门冬氨酸氨基转移酶 & 47.40 & U/L & 15-40 & 比色法 & & \\
6 & *总胆红素 & 10.00 & umol/L & 0-26 & 重氮法 & & \\
7 & *直接胆红素 & 4.60 & umol/L & 0-8 & 重氮法 & & \\
8 & 间接胆红素 & 5.40 & umol/L & 0-13 & 计算法 & & \\
9 & 胆碱脂酶 & 8964.00 & U/L & 5320-12920 & 比色法 & & \\
10 & *葡萄糖 & 4.62 & mmol/L & 4.1-6.05 & 己糖激酶法 & & \\
11 & *钾 & 3.75 & mmol/L & 3.5-5.5 & 间接离子选择电极法 & & \\
12 & *钠 & 136.00 & mmol/L & 137-147 & 间接离子选择电极法 & & \\
13 & *氯 & 98.80 & mmol/L & 99-110 & 间接离子选择电极法 & & \\
14 & *钙 & 2.50 & mmol/L & 2.11-2.54 & 比色法 & & \\
15 & *肌酐 & 73.00 & umol/L & 59-104 & 酶法 & & \\
16 & *尿素 & 6.10 & mmol/L & 3.1-9.5 & 比色法 & & \\
17 & *尿酸 & 406.00 & umol/L & 202.3-416.5 & 比色法 & & \\
18 & 肾小球滤过率 & 111.07 & ml/min & >80 & 计算法 & & \\
\hline
\end{tabular}
2026-08-10 15:34:23,488 INFO     29 [qwen-vl-parser] page=18 table: 25 LaTeX lines (bbox 776-800)
2026-08-10 15:34:23,488 INFO     29 [qwen-vl-parser] page=18 table: 25 sections
2026-08-10 15:34:23,693 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=875002, prompt_len=764
2026-08-10 15:34:25,050 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 15:34:25,051 INFO     29 [qwen-vl-parser] page=19 classify=table report_date=None
2026-08-10 15:34:25,070 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=875002, prompt_len=756
2026-08-10 15:34:26,648 INFO     29 [qwen-vl-parser] table API response (len=263):
\begin{tabular}{ccccccc}
\hline
No. 英文名称 & 项 目 & 结果 & 单位 & 参考值 & 实验方法 \\
\hline
1 CEA & 癌胚抗原 & 163.87 & ng/ml & 0-4.5 & 化学发光法 \\
2 NSE & 神经元特异性烯醇化酶 & 49.25 & ng/ml & $<$16.5 & 化学发光法 \\
3 Pro-GRP & 胃泌素释放肽前体 & 55.98 & pg/ml & 0-78.62 & 化学发光法 \\
\hline
\end{tabular}
2026-08-10 15:34:26,650 INFO     29 [qwen-vl-parser] page=19 table: 9 LaTeX lines (bbox 801-809)
2026-08-10 15:34:26,651 INFO     29 [qwen-vl-parser] page=19 table: 9 sections
2026-08-10 15:34:26,863 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=981869, prompt_len=764
2026-08-10 15:34:28,302 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-03-23"}
```
2026-08-10 15:34:28,303 INFO     29 [qwen-vl-parser] page=20 classify=table report_date=2026-03-23
2026-08-10 15:34:28,313 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=981869, prompt_len=756
2026-08-10 15:34:30,769 INFO     29 [qwen-vl-parser] table API response (len=432):
\begin{tabular}{llllllll}
\hline
NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\
\hline
1 & *凝血酶原时间 & 11.40 & 秒 & 9-14 & 凝固法 & & \\
2 & *国际标准化比值(INR) & 0.99 & & 0.77-1.19 & 计算法 & & \\
3 & 凝血酶原活动度 & 87 & \% & 70-130 & 凝固法 & & \\
4 & *活化部分凝血活酶时间 & 28.00 & 秒 & 24.8-33.8 & 凝固法 & & \\
5 & *纤维蛋白原 & 4.04 & g/L & 2-4 & 凝固法 & & \\
6 & 凝血酶时间 & 17.10 & 秒 & 14-21 & 凝固法 & & \\
7 & D-二聚体 & 1.02 & mg/L FEU & 0-0.50 & 胶乳免疫比浊法 & & \\
\hline
\end{tabular}
2026-08-10 15:34:30,771 INFO     29 [qwen-vl-parser] page=20 table: 14 LaTeX lines (bbox 810-823)
2026-08-10 15:34:30,771 INFO     29 [qwen-vl-parser] page=20 table: 14 sections
2026-08-10 15:34:31,002 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1636466, prompt_len=764
2026-08-10 15:34:32,405 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-10 15:34:32,405 INFO     29 [qwen-vl-parser] page=21 classify=table report_date=2026-03-23
2026-08-10 15:34:32,420 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1636466, prompt_len=756
2026-08-10 15:34:34,515 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:34:34.512+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:34:41,798 INFO     29 [qwen-vl-parser] table API response (len=1375):
\begin{tabular}{cccccccc}
\hline
NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\
\hline
1 & *白细胞计数 & 6.77 & 10^9/L & 3.5-9.5 & 激光散射法 & & \\
2 & 中性粒细胞百分率 & 73.40 & \% & 40-75 & 激光散射法+荧光染色法 & & \\
3 & 淋巴细胞百分率 & 15.30 & \% & 20-50 & 激光散射法+荧光染色法 & & \\
4 & 单核细胞百分率 & 9.00 & \% & 3-10 & 激光散射法+荧光染色法 & & \\
5 & 嗜酸细胞百分率 & 1.80 & \% & 0.4-8.0 & 激光散射法+荧光染色法 & & \\
6 & 嗜碱细胞百分率 & 0.50 & \% & 0.00-1.0 & 计算法 & & \\
7 & 中性粒细胞计数 & 4.97 & 10^9/L & 1.8-6.3 & 计算法 & & \\
8 & 淋巴细胞计数 & 1.04 & 10^9/L & 1.1-3.2 & 计算法 & & \\
9 & 单核细胞计数 & 0.61 & 10^9/L & 0.10-0.60 & 计算法 & & \\
10 & 嗜酸细胞计数 & 0.12 & 10^9/L & 0.02-0.52 & 计算法 & & \\
11 & 嗜碱细胞计数 & 0.03 & 10^9/L & 0-0.06 & 激光散色+荧光染色法 & & \\
12 & *红细胞计数 & 4.81 & 10^12/L & 4.3-5.8 & 阻抗法 & & \\
13 & *血红蛋白浓度 & 131.00 & g/l & 130-175 & 比色法 & & \\
14 & *红细胞压积 & 39.50 & \% & 40-50 & 计算法 & & \\
15 & *平均红细胞体积 & 82.00 & fL & 82-100 & 阻抗法 & & \\
16 & 红细胞宽度-SD值 & 50.10 & fL & 37-50 & 阻抗法 & & \\
17 & 红细胞宽度-CV值 & 16.60 & \% & 10.9-15.4 & 阻抗法 & & \\
18 & *平均血红蛋白含量 & 27.20 & pg & 27-34 & 计算法 & & \\
19 & *平均血红蛋白浓度 & 332.00 & g/l & 316-354 & 计算法 & & \\
20 & *血小板计数 & 167.00 & 10^9/L & 125-350 & 阻抗法 & & \\
21 & 平均血小板体积 & 13.10 & fL & 9-13 & 阻抗法 & & \\
22 & 血小板压积 & 0.22 & \% & 0.108-0.282 & 计算法 & & \\
23 & 血小板分布宽度 & 16.80 & fL & 9-17 & 阻抗法 & & \\
24 & 大血小板比率 & 50.00 & \% & 16.9-46.7 & 阻抗法 & & \\
25 & 大血小板计数 & 83.00 & 10^9/L & 30-90 & 计算法 & & \\
\hline
\end{tabular}
2026-08-10 15:34:41,801 INFO     29 [qwen-vl-parser] page=21 table: 32 LaTeX lines (bbox 824-855)
2026-08-10 15:34:41,801 INFO     29 [qwen-vl-parser] page=21 table: 32 sections
2026-08-10 15:34:42,047 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1607894, prompt_len=764
2026-08-10 15:34:43,551 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-25"}
```
2026-08-10 15:34:43,551 INFO     29 [qwen-vl-parser] page=22 classify=text report_date=2026-03-25
2026-08-10 15:34:43,573 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1607894, prompt_len=401
2026-08-10 15:34:49,024 INFO     29 [qwen-vl-parser] text API response (len=965):
["人民醫院", "川渝HR", "带*为川渝互认项目", "医学影像检查报告单", "扫码查看影像", "检查号:", "患者姓名:", "性别:男", "年龄:39岁", "住院号:", "申请科室", "床号:023", "联系电话", "检查室:CT1(联影CT)(1住)", "检查技师:羊媛颖", "检查时间:2026-03-25 08:22:58", "检查部位:[*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强]", "检查技术:-", "描述:", "1、“肺CA”复查,右肺上叶见团块影,边缘呈分叶状,局部与胸膜粘连,见支气", "管截断,较大层面范围约5.6cm×5.3cm,增强扫描呈轻度不均匀强化,周围见斑条", "影及小结节影,较CT260121-240片病灶稍增大。", "2、双肺另见长径约0.4-0.7cm微小结节,较大者位于右肺上叶前段(IM37)较前片", "稍增大,必要时随诊。", "3、右肺中叶及双肺下叶见散在斑条影。", "4、心包少量积液。纵隔淋巴结显示,部分稍增大。双侧胸膜稍增厚。", "5、肝右后叶见稍低密度结节,边缘稍模糊,增强扫描轻中度强化,边缘强化明", "显,较大层面范围约1.2cm×0.9cm,转移灶可能,其它病变待排,较前稍缩小。", "6、左侧肾上腺内侧支增粗,见结节状稍低密度影,增强扫描强化稍欠均匀,长径", "约1.4cm,占位性病变或转移灶待排。较前稍增大。", "7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。", "8、右肾见稍低密度结节,较大者长径约1.3cm,增强扫描似见轻度强化,占位性病", "变或转移灶待排。较前变化不大。", "9、前列腺稍显丰满,强化稍欠均匀。", "10、扫及双侧部分肋骨,胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻", "骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏,转移灶可能,部分椎体", "变扁,病理性骨折待排。", "请结合临床及其它检查,必要时复查或进一步检查。", "总结意见:", "见上述。", "报告者:申悦", "审核医师:曹玉", "报告时间:2026/3/25 8:48:11", "审核时间:2026/3/25 9:26:23", "注:此报告审核"]
2026-08-10 15:34:49,024 INFO     29 [qwen-vl-parser] page=22 text: 45 lines (bbox 856-900)
2026-08-10 15:34:49,025 INFO     29 [qwen-vl-parser] page=22 text: 45 sections
2026-08-10 15:34:49,025 INFO     29 [qwen-vl-parser] parse_pdf done: 901 sections from 22 pages.
2026-08-10 15:34:49,033 INFO     29 Close text detector.
2026-08-10 15:34:49,499 INFO     29 Close text recognizer.
2026-08-10 15:34:49,905 INFO     29 Close recognizer.
2026-08-10 15:34:50,373 INFO     29 Close recognizer.
2026-08-10 15:34:50,997 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 15:34:50,998 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Parser:MedLink | outputs={"html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "json"}
2026-08-10 15:34:50,998 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 15:34:51,037 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:34:51,038 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 入院记录\n[BBOX-1] 姓名：\n[BBOX-2] 性别：男\n[BBOX-3] 年龄：38岁\n[BBOX-4] 婚姻状况：已婚\n[BBOX-5] 出生地：\n[BBOX-6] 民族：汉族\n[BBOX-7] 现住址：\n[BBOX-8] 职业：自由职业者\n[BBOX-9] 入院时间：2025-09-09 10:41\n[BBOX-10] 记录时间：2025-09-09 11:01\n[BBOX-11] 病史陈述者\n[BBOX-12] 联系人姓名：\n[BBOX-13] 联系人电话：\n[BBOX-14] 病史真实性确认签字：\n[BBOX-15] 主诉：咳嗽3+月，发现右上肺占位10+天\n[BBOX-16] 现病史：入院前3+月，患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。10+天前，患\n[BBOX-17] 民医院就诊，完善胸部CT\n[BBOX-18] 提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑\n[BBOX-19] 占位性病变，肺Ca可能性大。建议结合临床进一步检查。2.双肺散在点结影及条索影。3.纵隔内可见\n[BBOX-20] 淋巴结显示，部分稍大。4.心脏形态大小未见异常。5.双侧胸腔未见确切积液征象。6.扫及肝右叶见\n[BBOX-21] 片状密度低影，长径约2.7cm，性质?建议进一步检查。7.扫及胸椎多个椎体骨质密度减低破坏改\n[BBOX-22] 变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+\n[BBOX-23] NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段\n[BBOX-24] 测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺\n[BBOX-25] 另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分\n[BBOX-26] 稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，\n[BBOX-27] 必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破\n[BBOX-28] 坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.电轴左偏。建议完善经皮肺穿刺\n[BBOX-29] 检查后纤支镜下肺活检明确，患方商议后表示拒绝，现患者为进一步明确占位性质，遂于我院门诊就\n[BBOX-30] 诊，门诊以“右上肺占位”收入我科。\n[BBOX-31] 自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。\n[BBOX-32] 既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病\n[BBOX-33] 史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。\n[BBOX-34] 过敏史：否认食物、药物过敏史。\n[BBOX-35] 个人史：出生原籍，长期居住生长于当地，否认疫区居住治游史，平素偶有饮酒，否认吸烟及\n[BBOX-36] 人民医院\n[BBOX-37] 入院记录\n[BBOX-38] 家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。\n[BBOX-39] 体格检查\n[BBOX-40] T36.1℃\n[BBOX-41] P92次/分\n[BBOX-42] R19次/分\n[BBOX-43] BP121/83mmHg\n[BBOX-44] 一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮\n[BBOX-45] 疹。背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部\n[BBOX-46] 及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。\n[BBOX-47] 颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊\n[BBOX-48] 清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，HR92次/分，律齐，各\n[BBOX-49] 瓣膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性\n[BBOX-50] 浊音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经\n[BBOX-51] 系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。\n[BBOX-52] 专科情况\n[BBOX-53] 背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。胸廓正常，双肺语颤正常，双肺叩诊清\n[BBOX-54] 音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，HR92次/分，律齐，各瓣膜区未闻\n[BBOX-55] 及病理性杂音。\n[BBOX-56] 辅助检查\n[BBOX-57] 2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇\n[BBOX-58] 化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块,\n[BBOX-59] 肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在\n[BBOX-60] 斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低\n[BBOX-61] 密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎\n[BBOX-62] 体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦\n[BBOX-63] 性心律 2.由缺血性\n[BBOX-64] 出院证明书\n[BBOX-65] (医院保存联)\n[BBOX-66] 姓名：\n[BBOX-67] 性别：男\n[BBOX-68] 年龄：38岁\n[BBOX-69] 入院时间：2025-09-09 10:41\n[BBOX-70] 住院证字\n[BBOX-71] 号\n[BBOX-72] 出院时间：2025-09-12\n[BBOX-73] 病人单位或住址：\n[BBOX-74] 出院诊断：1.右肺上叶腺癌cT4N1M1c IVB期（伴多发骨、肝脏、脑转移） 2.肝继发恶性肿瘤？ 3.\n[BBOX-75] 多发骨继发恶性肿瘤？ 4.中脑继发恶性肿瘤？ 5.癌性疼痛\n[BBOX-76] 诊疗小结：患者因“咳嗽3+月，发现右上肺占位10+天”入院。辅助检查：2025-09-01 [*胸部,增\n[BBOX-77] 强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右\n[BBOX-78] 肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸\n[BBOX-79] 膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧\n[BBOX-80] 部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨\n[BBOX-81] 折可能。2025-09-11 [*头部,MRI平扫] [头部,DWI],1、中脑内异常信号影，占位性病变？脱髓鞘病\n[BBOX-82] 变？缺血灶？其它？2、扫及右侧上颌窦囊肿可能。请结合临床及其它检查。2025-09-01 CYFRA21-1\n[BBOX-83] +CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞\n[BBOX-84] 角蛋白19片段测定 62.83(ng/ml)↑；2025-09-09 血常规(五分类):白细胞计数 10.51(10^9/L)↑，\n[BBOX-85] 中性粒细胞百分率 80.40(%)↑，中性粒细胞计数 8.45(10^9/L)↑。心电图：1.窦性心律 2.电轴左\n[BBOX-86] 偏。\n[BBOX-87] 诊疗经过：[入院后完善相关辅助检查，于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病\n[BBOX-88] 理科腺癌可能性大，报告未回，现患者要求院外等待结果，予以办理出院。]\n[BBOX-89] 治疗结果：好转\n[BBOX-90] 出院医嘱及建议：1、注意休息，避免受凉感冒及劳累；2、院外追踪免疫组化结果，待结果回示后\n[BBOX-91] 及时呼吸内科门诊就诊；3、呼吸科、肿瘤科门诊随访，如有不适，请及时就医。\n[BBOX-92] 人民医院\n[BBOX-93] 川渝HR\n[BBOX-94] 带*为川渝互认项目\n[BBOX-95] 医学影像检查报告单\n[BBOX-96] 住院\n[BBOX-97] 检查号：\n[BBOX-98] 患者姓名：\n[BBOX-99] 性别：男\n[BBOX-100] 患者年龄：38岁\n[BBOX-101] 申请科室：\n[BBOX-102] 床号：\n[BBOX-103] 设备名称：CT1(联影CT)(1住)\n[BBOX-104] 检查部位：[*胸部,增强]\n[BBOX-105] 联系电话：\n[BBOX-106] 检查技师：\n[BBOX-107] 检查时间：2025-09-01 08:34:37\n[BBOX-108] 报告时间：2025/9/1 9:31:33\n[BBOX-109] 描述：\n[BBOX-110] 右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截\n[BBOX-111] 断，较大层面范围约7.9cm×6.9cm，增强扫描呈轻度不均匀强化，周围\n[BBOX-112] 见斑条影及小结节影。双肺另见长径约0.4-0.6cm实性小结节。右肺中\n[BBOX-113] 叶及双肺下叶见散在斑条影。纵膈见多发淋巴结显示，部分稍大。心脏\n[BBOX-114] 不大，心包少量积液。左侧胸膜稍增厚。肝右叶见数个类圆形低密度\n[BBOX-115] 影，较大者长径约2.5cm，增强扫描两期强化程度CT值相差25HU。扫及\n[BBOX-116] 双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破\n[BBOX-117] 坏，T2椎体见多发骨折线影。\n[BBOX-118] 总结意见：\n[BBOX-119] 1、右肺上叶团块，肿瘤占位性病变可能，其它待排。\n[BBOX-120] 2、双肺另见小结节，必要时随诊。\n[BBOX-121] 3、右肺中叶及双肺下叶见散在斑条影。\n[BBOX-122] 4、纵膈见多发淋巴结显示，部分稍大。\n[BBOX-123] 5、心包少量积液。左侧胸膜稍增厚。\n[BBOX-124] 6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步\n[BBOX-125] 检查。\n[BBOX-126] 7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨\n[BBOX-127] 性骨质破坏，转移灶可能，T2椎体病理性骨折可能。\n[BBOX-128] 请结合临床及其它检查，必要时复查或进一步检查。\n[BBOX-129] 报告者：申悦\n[BBOX-130] 审核医师：马婉军\n[BBOX-131] 页 尾页\n[BBOX-132] 共1页,共1条记\n[BBOX-133] 住院号\n[BBOX-134] 门诊号：-\n[BBOX-135] 病理号[\n[BBOX-136] 姓名\n[BBOX-137] 性别 男\n[BBOX-138] 年龄 38岁\n[BBOX-139] 病人编号\n[BBOX-140] 病区\n[BBOX-141] 就诊号\n[BBOX-142] 收到日期 2025-09-10\n[BBOX-143] 送检科室\n[BBOX-144] 送检单位 本院\n[BBOX-145] 送检医生\n[BBOX-146] 标本名称 右肺包块\n[BBOX-147] 临床诊断\n[BBOX-148] 肉眼所见\n[BBOX-149] (右肺包块)灰白色组织多粒,直径0.4cm,点纸全\n[BBOX-150] 病理诊断\n[BBOX-151] (右肺包块,穿刺活检)结合免疫组化结果:癌细胞CK(+),CK7(+),TTF-1(+),NapsinA(+),Ki67(+,约60%),CK20(-),SATB2(-),\n[BBOX-152] 支持肺腺癌。\n[BBOX-153] 报告医生 阙柳\n[BBOX-154] 审核医生 阙柳\n[BBOX-155] 复诊医生\n[BBOX-156] 报告时间 2025-09-15\n[BBOX-157] 欢迎使用朗珈PathQC病理质控与资料管理系统\n[BBOX-158] 检测概览\n[BBOX-159] 基本信息\n[BBOX-160] 受检者信息\n[BBOX-161] 样本信息\n[BBOX-162] 临床信息\n[BBOX-163] 姓名\n[BBOX-164] 样本编号：\n[BBOX-165] 临床/病理诊断：肺癌怀疑骨转移肝转移\n[BBOX-166] 性别：男\n[BBOX-167] 样本类型：石蜡块\n[BBOX-168] 手术史/用药史：/\n[BBOX-169] 年龄：38岁\n[BBOX-170] 采样部位：/\n[BBOX-171] 既往基因检测结果：/\n[BBOX-172] 送检单位\n[BBOX-173] 家族史：/\n[BBOX-174] 采集日期：\n[BBOX-175] 接收日期：2025-09-18\n[BBOX-176] 报告日期：2025-09-21\n[BBOX-177] 本报告中的临床诊断等信息来自受检者送检时提供的信息，而非来自检测结果。\n[BBOX-178] 项目简介\n[BBOX-179] 项目名称\n[BBOX-180] 肺癌靶向18基因检测\n[BBOX-181] 检测方法\n[BBOX-182] 目标区域探针捕获技术和二代测序技术(Next-Generation Sequencing,NGS)\n[BBOX-183] 检测范围\n[BBOX-184] 本检测基于非小细胞肺癌指南和专家共识，检测非小细胞肺癌靶向治疗和预后相关的18个基因(包括：EGFR、ALK、MET、ROS1、BRAF、RET、ERBB2(HER2)、KRAS、NTRK1/2/3、NRAS、PIK3CA、AKT1、FBXW7、DDR2、NRG1、TP53)，变异类型包含相应基因的点突变、插入/缺失，拷贝数变异和基因融合/重排。\n[BBOX-185] 检测流程\n[BBOX-186] 核酸提取、文库制备、高通量测序、生物信息分析及报告解读\n[BBOX-187] 参考指南及数据库\n[BBOX-188] NCCN指南、CSCO指南、OncoKB、COSMIC、CKB、ClinVar等\n[BBOX-189] 参考基因组\n[BBOX-190] GRCh37/hg19\n[BBOX-191] 检测结果汇总\n[BBOX-192] 基因变异结果（共5个）\n[BBOX-193] 基因\n[BBOX-194] 转录本/外显子\n[BBOX-195] cDNA改变\n[BBOX-196] 氨基酸改变\n[BBOX-197] 变异类型\n[BBOX-198] 变异丰度/拷贝数\n[BBOX-199] 变异分类\n[BBOX-200] EGFR\n[BBOX-201] NM_005228.5:exon21\n[BBOX-202] c.2573T>G\n[BBOX-203] p.L858R\n[BBOX-204] 错义突变\n[BBOX-205] 51.28%\n[BBOX-206] I类[重要临床意义]\n[BBOX-207] ERBB2(HER2)\n[BBOX-208] NM_004448.4\n[BBOX-209] /\n[BBOX-210] /\n[BBOX-211] 拷贝数扩增\n[BBOX-212] 拷贝数=3.6\n[BBOX-213] I类[重要临床意义]\n[BBOX-214] MET\n[BBOX-215] NM_000245.4\n[BBOX-216] /\n[BBOX-217] /\n[BBOX-218] 拷贝数扩增\n[BBOX-219] 拷贝数=3.1\n[BBOX-220] I类[重要临床意义]\n[BBOX-221] TP53\n[BBOX-222] NM_000546.6:exon6\n[BBOX-223] c.598_611del\n[BBOX-224] p.N200Vfs*4\n[BBOX-225] 移码突变\n[BBOX-226] 61.75%\n[BBOX-227] II类[潜在临床意义]\n[BBOX-228] 第1页\n[BBOX-229] TP53\n[BBOX-230] NM_000546.6:exon6\n[BBOX-231] c.629A>C\n[BBOX-232] p.N210T\n[BBOX-233] 错义突变\n[BBOX-234] 62.88%\n[BBOX-235] III类[临床意义不明]\n[BBOX-236] 注：\n[BBOX-237] 《肿瘤二代测序临床报告解读共识》指出，基因变异按照其临床意义的重要性分为4类：\n[BBOX-238] I类：有重要的临床意义，与治疗、预后和诊断相关；\n[BBOX-239] II类：有潜在的临床意义，与治疗、预后和诊断相关；\n[BBOX-240] III类：临床意义不明(临床意义不明是指目前尚无充分证据证实这些基因变异与肿瘤的致病性关系，尚无相关用药提示，未来可能随着研究的深入而更新致病性及药物证据等级)；\n[BBOX-241] IV类变异，无害或可能无害。\n[BBOX-242] 本报告只列出I、II、III类变异。\n[BBOX-243] 靶向用药基因检测提示\n[BBOX-244] 靶向用药基因检测提示\n[BBOX-245] 基因\n[BBOX-246] 变异信息\n[BBOX-247] 变异丰度/拷贝数\n[BBOX-248] (A级)\n[BBOX-249] FDA/NMPA\n[BBOX-250] 指南推荐用药\n[BBOX-251] (B级)\n[BBOX-252] 专家共识推荐用药\n[BBOX-253] (C级)\n[BBOX-254] 跨适应症\n[BBOX-255] (C级)\n[BBOX-256] 临床试验药物\n[BBOX-257] (D级)\n[BBOX-258] 临床前研究\n[BBOX-259] 奥希替尼\n[BBOX-260] (敏感)\n[BBOX-261] 奥希替尼+\n[BBOX-262] 化疗\n[BBOX-263] (敏感)\n[BBOX-264] 埃万妥单抗+\n[BBOX-265] 兰泽替尼\n[BBOX-266] (敏感)\n[BBOX-267] 埃万妥单抗+\n[BBOX-268] 化疗\n[BBOX-269] (敏感)\n[BBOX-270] 阿美替尼\n[BBOX-271] (敏感)\n[BBOX-272] 伏美替尼\n[BBOX-273] (敏感)\n[BBOX-274] 达可替尼\n[BBOX-275] (敏感)\n[BBOX-276] 吉非替尼\n[BBOX-277] (敏感)\n[BBOX-278] 阿法替尼±\n[BBOX-279] 西妥昔单抗\n[BBOX-280] (敏感)\n[BBOX-281] 埃克替尼\n[BBOX-282] (敏感)\n[BBOX-283] 贝福替尼\n[BBOX-284] (敏感)\n[BBOX-285] 厄洛替尼±\n[BBOX-286] 雷莫西尤单抗\n[BBOX-287] 或贝伐珠单抗\n[BBOX-288] (敏感)\n[BBOX-289] 瑞厄替尼\n[BBOX-290] (敏感)\n[BBOX-291] 瑞齐替尼\n[BBOX-292] 德达博妥单抗+\n[BBOX-293] 奥希替尼\n[BBOX-294] (敏感)\n[BBOX-295] Patritumab\n[BBOX-296] Deruxtecan\n[BBOX-297] (敏感)\n[BBOX-298] BDTX-1535\n[BBOX-299] (敏感)\n[BBOX-300] WSD0922\n[BBOX-301] (敏感)\n[BBOX-302] HLX42\n[BBOX-303] (敏感)\n[BBOX-304] SHR-A2009\n[BBOX-305] (敏感)\n[BBOX-306] BL-B01D1\n[BBOX-307] (敏感)\n[BBOX-308] 阿美替尼+\n[BBOX-309] 化疗\n[BBOX-310] (敏感)\n[BBOX-311] EGFR\n[BBOX-312] c.2573T>G,\n[BBOX-313] p.L858R,\n[BBOX-314] Exon21\n[BBOX-315] 51.28%\n[BBOX-316] /\n[BBOX-317] /\n[BBOX-318] /\n[BBOX-319] /\n[BBOX-320] 第 2 页\n[BBOX-321] (敏感)\n[BBOX-322] 佐利替尼\n[BBOX-323] (敏感)\n[BBOX-324] 利厄替尼\n[BBOX-325] (敏感)\n[BBOX-326] 德达博妥单抗\n[BBOX-327] (敏感)\n[BBOX-328] 芦康沙妥珠单\n[BBOX-329] 抗\n[BBOX-330] (敏感)\n[BBOX-331] 依沃西单抗+\n[BBOX-332] 培美曲塞+\n[BBOX-333] 卡铂\n[BBOX-334] (敏感)\n[BBOX-335] 奥希替尼+\n[BBOX-336] 赛沃替尼\n[BBOX-337] (敏感)\n[BBOX-338] 伯瑞替尼\n[BBOX-339] (敏感)\n[BBOX-340] 克唑替尼\n[BBOX-341] (敏感)\n[BBOX-342] 卡马替尼\n[BBOX-343] (敏感)\n[BBOX-344] 特泊替尼\n[BBOX-345] (敏感)\n[BBOX-346] EGFR-TKIs\n[BBOX-347] (耐药)\n[BBOX-348] 谷美替尼\n[BBOX-349] (敏感)\n[BBOX-350] EGFR-TKIs+\n[BBOX-351] MET-TKIs\n[BBOX-352] (敏感)\n[BBOX-353] /\n[BBOX-354] 伯瑞替尼+\n[BBOX-355] PLB1004\n[BBOX-356] (敏感)\n[BBOX-357] SYM015\n[BBOX-358] (敏感)\n[BBOX-359] 特泊替尼+\n[BBOX-360] 吉非替尼\n[BBOX-361] (敏感)\n[BBOX-362] 特泊替尼+\n[BBOX-363] 奥希替尼\n[BBOX-364] (敏感)\n[BBOX-365] 赛沃替尼\n[BBOX-366] (敏感)\n[BBOX-367] MET\n[BBOX-368] 扩增\n[BBOX-369] 拷贝数\n[BBOX-370] =3.1\n[BBOX-371] /\n[BBOX-372] 德曲妥珠单\n[BBOX-373] 抗\n[BBOX-374] (敏感)\n[BBOX-375] 泽尼达妥单\n[BBOX-376] 抗\n[BBOX-377] (敏感)\n[BBOX-378] 帕博利珠单\n[BBOX-379] 抗+\n[BBOX-380] 曲妥珠单抗+\n[BBOX-381] 化疗\n[BBOX-382] (敏感)\n[BBOX-383] 帕妥珠单抗+\n[BBOX-384] 曲妥珠单抗+\n[BBOX-385] 化疗\n[BBOX-386] (敏感)\n[BBOX-387] 恩美曲妥珠\n[BBOX-388] 单抗\n[BBOX-389] (敏感)\n[BBOX-390] 维迪西妥单\n[BBOX-391] 抗\n[BBOX-392] (敏感)\n[BBOX-393] 吡咯替尼\n[BBOX-394] (敏感)\n[BBOX-395] 阿法替尼\n[BBOX-396] (敏感)\n[BBOX-397] 帕妥珠单抗+\n[BBOX-398] 曲妥珠单抗\n[BBOX-399] (敏感)\n[BBOX-400] 吡咯替尼+\n[BBOX-401] 阿帕替尼\n[BBOX-402] (敏感)\n[BBOX-403] 维迪西妥单抗+\n[BBOX-404] 替雷利珠单抗+\n[BBOX-405] 贝伐珠单抗\n[BBOX-406] (敏感)\n[BBOX-407] 维迪西妥单抗+\n[BBOX-408] 安罗替尼\n[BBOX-409] (敏感)\n[BBOX-410] ERBB2\n[BBOX-411] (HER2)\n[BBOX-412] 扩增\n[BBOX-413] 拷贝数\n[BBOX-414] =3.6\n[BBOX-415] EGFR-TKIs\n[BBOX-416] (耐药)\n[BBOX-417] /\n[BBOX-418] Tarloxotinib\n[BBOX-419] (敏感)\n[BBOX-420] TAS0728\n[BBOX-421] (敏感)\n[BBOX-422] BDTX-189\n[BBOX-423] (敏感)\n[BBOX-424] c.598_611del\n[BBOX-425] p.N200Vfs*4\n[BBOX-426] Exon6\n[BBOX-427] 61.75%\n[BBOX-428] /\n[BBOX-429] /\n[BBOX-430] /\n[BBOX-431] Adavosertib\n[BBOX-432] (敏感)\n[BBOX-433] CTX-1\n[BBOX-434] (敏感)\n[BBOX-435] CEP-8983\n[BBOX-436] (敏感)\n[BBOX-437] TP53\n[BBOX-438] 患者信息\n[BBOX-439] 姓名\n[BBOX-440] 性别\n[BBOX-441] 男\n[BBOX-442] 年龄\n[BBOX-443] 38岁\n[BBOX-444] 送检单位\n[BBOX-445] 样本信息\n[BBOX-446] 样本编号\n[BBOX-447] 样本类型\n[BBOX-448] 采样部位\n[BBOX-449] 样本采集日期\n[BBOX-450] 样本接收日期\n[BBOX-451] 报告日期\n[BBOX-452] 石蜡块\n[BBOX-453] —\n[BBOX-454] 2025-09-18\n[BBOX-455] 2025-09-20\n[BBOX-456] 检测项目\n[BBOX-457] PD-L1蛋白表达检测\n[BBOX-458] 抗体型号\n[BBOX-459] 临床信息\n[BBOX-460] 临床/病理诊断\n[BBOX-461] 肺癌怀疑骨转移肝转移\n[BBOX-462] 手术史/用药史\n[BBOX-463] —\n[BBOX-464] 二、检测结果\n[BBOX-465] 检测内容\n[BBOX-466] 检测结果\n[BBOX-467] 检测结果提示\n[BBOX-468] PD-L1蛋白\n[BBOX-469] TPS\n[BBOX-470] <1%\n[BBOX-471] PD-L1蛋白表达。\n[BBOX-472] 表达水平\n[BBOX-473] CPS\n[BBOX-474] 1\n[BBOX-475] TC\n[BBOX-476] <1%\n[BBOX-477] IC\n[BBOX-478] 1%\n[BBOX-479] 检测结果图示\n[BBOX-480] PDL1×200\n[BBOX-481] HE×200\n[BBOX-482] 出院证明书\n[BBOX-483] (医院保存联)\n[BBOX-484] 住院证字\n[BBOX-485] 号\n[BBOX-486] 姓名\n[BBOX-487] 年龄：38岁 入院时间：2025-12-04 09:00\n[BBOX-488] 科\n[BBOX-489] 床号：029 出院时间：2025-12-07\n[BBOX-490] 病人单位或住址\n[BBOX-491] 出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR\n[BBOX-492] L858R+）3.恶性肿瘤靶向治疗 4.肝继发恶性肿瘤 5.骨继发恶性肿瘤 6.化疗相关恶心和呕吐 7.\n[BBOX-493] 化疗后骨髓抑制 8.轻度贫血\n[BBOX-494] 诊疗小结：患者因“发现右肺上叶占位5+月，右肺上叶腺癌靶向治疗中。”入院。入院查体：\n[BBOX-495] T36.5℃，P75次/分，R20次/分，BP127/82mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语\n[BBOX-496] 颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣\n[BBOX-497] 膜区未闻及病理性杂音。]辅助检查：暂缺。\n[BBOX-498] 诊疗经过：[入院完善相关检查2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋\n[BBOX-499] 白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌\n[BBOX-500] 素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。2025-12-04 胸腹部增\n[BBOX-501] 强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较\n[BBOX-502] 大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较\n[BBOX-503] CT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中\n[BBOX-504] 叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边\n[BBOX-505] 缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它\n[BBOX-506] 病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约\n[BBOX-507] 1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右\n[BBOX-508] 肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前\n[BBOX-509] 列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂\n[BBOX-510] 骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理\n[BBOX-511] 性骨折待排。病情评价好转，给于唑来磷酸预防骨相关事件。排除化疗禁忌于2025-12-5行第1周期AC\n[BBOX-512] 方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼 110mg\n[BBOX-513] qd，化疗中给于抑酸、护胃、止吐等对症治疗，化疗顺利，患者无明显不适。化疗后复查血常规提\n[BBOX-514] 示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。]\n[BBOX-515] 治疗结果：好转\n[BBOX-516] 出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就\n[BBOX-517] 第1页/共2页\n[BBOX-518] 出院证明书\n[BBOX-519] (医院保存联)\n[BBOX-520] 住院证字\n[BBOX-521] 号\n[BBOX-522] 性别：男 年龄：39岁 入院时间：2025-12-29 09:54\n[BBOX-523] 床号： 出院时间：2025-12-31\n[BBOX-524] 病人单位或住址\n[BBOX-525] 出院诊断：1.姑息性化疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）\n[BBOX-526] 3.肝继发恶性肿瘤 4.骨继发恶性肿瘤 5.化疗相关性恶心和呕吐 6.化疗相关性吞咽困难 7.肝功\n[BBOX-527] 能不全\n[BBOX-528] 诊疗小结：患者因“发现右肺上叶占位6+月，右肺上叶腺癌1周期化疗后20+天。”入院。入院查\n[BBOX-529] 体：T36.7℃；P85次/分；R18次/分；BP117/81mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺\n[BBOX-530] 语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各\n[BBOX-531] 瓣膜区未闻及病理性杂音。\n[BBOX-532] 诊疗经过：患者入院后完善相关检查，2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，\n[BBOX-533] 中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；\n[BBOX-534] 2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急\n[BBOX-535] 诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬\n[BBOX-536] 氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。患者无化疗禁忌，于2025-12-30行第2周期AC方案化\n[BBOX-537] 疗，具体方案为：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w，同时给予患者抑酸护胃、止\n[BBOX-538] 痛等对症支持治疗，今日安排患者出院。\n[BBOX-539] 治疗结果：好转\n[BBOX-540] 出院医嘱及建议：1、注意休息，加强营养；2、每周复查血常规2次、肝肾功1次，如有异常，立即\n[BBOX-541] 就诊。3、下周期化疗时间：2026-01-20，住院前请提前联系床位。4、出院用药：利可君片 1片 口\n[BBOX-542] 服 每天3次，生血宝合剂 15ml 口服 每天3次。5、\n[BBOX-543] 午\n[BBOX-544] 6、我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午。\n[BBOX-545] 备注（包括手术名称）：[手术记录手术名称]\n[BBOX-546] 时间：2025年12月31日\n[BBOX-547] 说明：1、此证明书未经我院加盖公章无效。 2、涂改未经加盖我院公章无效。\n[BBOX-548] 3、此证明仅证明病人出院时病情。 4、请妥善保管，遗失不补。\n[BBOX-549] 第1页/共2页\n[BBOX-550] 出院证明书\n[BBOX-551] (病人保存联)\n[BBOX-552] 住院证字\n[BBOX-553] 号\n[BBOX-554] 姓名：\n[BBOX-555] 性别：男\n[BBOX-556] 年龄：39岁\n[BBOX-557] 入院时间：2026-01-21 10:07\n[BBOX-558] 出院时间：2026-01-24\n[BBOX-559] 病人单位或住址\n[BBOX-560] 出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR\n[BBOX-561] L858R+）\n[BBOX-562] 3.恶性肿瘤靶向治疗\n[BBOX-563] 4.肝继发恶性肿瘤\n[BBOX-564] 5.骨继发恶性肿瘤\n[BBOX-565] 6.化疗相关恶心和呕吐\n[BBOX-566] 7.化疗后骨髓抑制\n[BBOX-567] 8.白细胞减少\n[BBOX-568] 9.恶性肿瘤的治疗后的随诊检查\n[BBOX-569] 诊疗小结：患者因“发现右肺上叶占位7月，右肺上叶腺癌2周期化疗后20+天。”入院。入院查体：\n[BBOX-570] T36.6℃，P76次/分，R19次/分，BP113/75mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语\n[BBOX-571] 颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣\n[BBOX-572] 膜区未闻及病理性杂音。]辅助检查：暂缺。\n[BBOX-573] 诊疗经过：[入院完善相关检查：2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红\n[BBOX-574] 蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80\n[BBOX-575] (U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+\n[BBOX-576] ProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前\n[BBOX-577] 体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。2026-01-22 胸腹部CT：1、“肺CA”复查，右\n[BBOX-578] 肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，\n[BBOX-579] 增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另\n[BBOX-580] 见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺\n[BBOX-581] 下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸\n[BBOX-582] 膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大\n[BBOX-583] 层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增\n[BBOX-584] 粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前\n[BBOX-585] 变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐\n[BBOX-586] 骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。病情评价好转，排除于2026-1-23\n[BBOX-587] 行第3周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w，同时给予\n[BBOX-588] 患者抑酸护胃、止痛等对症支持治疗，现化疗已完成，于今出院回家乡休养。]\n[BBOX-589] 治疗结果：好转\n[BBOX-590] 出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就\n[BBOX-591] 诊。2、下周期治疗时间：2026年2月13日，请提前几天微信群预约床位，入院前尽量保持空腹状\n[BBOX-592] 第1页/共2页\n[BBOX-593] 民医院\n[BBOX-594] 出院证明书\n[BBOX-595] (病人保存联)\n[BBOX-596] 住院证字\n[BBOX-597] 号\n[BBOX-598] 姓名：\n[BBOX-599] 性别：男\n[BBOX-600] 年龄：39岁\n[BBOX-601] 入院时间：2026-02-24 09:09\n[BBOX-602] 出院时间：2026-02-26\n[BBOX-603] 病人单位或住址：\n[BBOX-604] 出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）\n[BBOX-605] 2.肝继发恶性肿\n[BBOX-606] 瘤\n[BBOX-607] 3.骨继发恶性肿瘤\n[BBOX-608] 4.恶性肿瘤靶向治疗\n[BBOX-609] 5.化疗后血小板减少\n[BBOX-610] 6.姑息性化疗\n[BBOX-611] 诊疗小结：患者因“右肺上叶腺癌3周期化疗后20+天。”入院。入院查体：T36.4℃；P93次/分；\n[BBOX-612] R18次/分；BP107/70mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，\n[BBOX-613] 双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。\n[BBOX-614] 诊疗经过：完善检查，2026-02-24\n[BBOX-615] 血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24\n[BBOX-616] CEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；\n[BBOX-617] 2026-02-24\n[BBOX-618] 凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU)\n[BBOX-619] ↑；2026-02-24\n[BBOX-620] 急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急\n[BBOX-621] 诊)：钠 136.00(mmol/L)↓；患者无化疗禁忌，2026-02-25开始行第4周期AC方案化疗，具体方案\n[BBOX-622] 为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼110mg po qd，患者治疗结束，复\n[BBOX-623] 查2026-02-26[左上肢静脉,血管彩超]，左上肢静脉未见明显异常。予以拔除PICC管后办理出院。\n[BBOX-624] 治疗结果：好转\n[BBOX-625] 出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就\n[BBOX-626] 诊。2、下周期治疗时间：2026年3月18日，肿瘤科门诊或日间放化疗门诊完成治疗。3、出院带\n[BBOX-627] 药：-。4、\n[BBOX-628] 5、加强营养，清淡饮食，避免着凉，预防感染，不适随诊。\n[BBOX-629] 备注(包括手术名称)：[手术记录手术名称]\n[BBOX-630] 时间：2026年02月26日\n[BBOX-631] 说明：1、此证明书未经我院加盖公章无效。\n[BBOX-632] 2、涂改未经加盖我院公章无效。\n[BBOX-633] 3、此证明仅证明病人出院时病情。\n[BBOX-634] 4、请妥善保管，遗失不补。\n[BBOX-635] 人民医院\n[BBOX-636] 入院记录\n[BBOX-637] 姓名：\n[BBOX-638] 性别：男\n[BBOX-639] 年龄：\n[BBOX-640] 婚姻状况：未婚\n[BBOX-641] 出生地：\n[BBOX-642] 民族：汉族\n[BBOX-643] 现住址：\n[BBOX-644] 职业：自由职业者\n[BBOX-645] 入院时间：2026-03-23 10:38\n[BBOX-646] 记录时间：2026-03-23 10:46\n[BBOX-647] 病史陈述者：\n[BBOX-648] 联系人姓名：\n[BBOX-649] 联系人电话：\n[BBOX-650] 病史真实性确认签字：\n[BBOX-651] 主诉：右肺上叶腺癌4周期化疗后1+月。\n[BBOX-652] 现病史：2025-06患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未\n[BBOX-653] 行治疗，病程中患者上述症状持续存在。\n[BBOX-654] 民医院就诊，完善胸部CT提示“1.右上肺见\n[BBOX-655] 团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca\n[BBOX-656] 可能性大。3.纵隔内可见淋巴结显示，部分稍大。扫及肝右叶见片状密度低影，长径约2.7cm，性\n[BBOX-657] 质？，扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住\n[BBOX-658] 院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性\n[BBOX-659] 烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑，行胸部增强CT检查示：右肺上\n[BBOX-660] 叶团块，肿瘤占位性病变可能，其它待排。纵膈见多发淋巴结显示，部分稍大。肝右叶低密度结节，\n[BBOX-661] 占位性病变可能，转移灶待排，扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性\n[BBOX-662] 骨质破坏，转移灶可能，T2椎体病理性骨折可能。于2025-09-10行经皮肺穿刺活检，免疫组化结果电\n[BBOX-663] 话询问病理科腺癌可能性大，2025-09-15报告回示：病理诊断（右肺包块，穿刺活检）结合免疫组化\n[BBOX-664] 结果：癌细胞CK（+），CK7（+），TTF-1（+），NapsinA（+），Ki67（+，约60%），CK20（-），\n[BBOX-665] SATB2（-），支持肺腺癌。基因检查示：EGFR L858R+,MET 扩增，ERBB2 扩增，TP53突变，PD-L1<\n[BBOX-666] 1%。于2025-09-24开始口服阿美替尼靶向治疗（110mg po qd）。2025-12-04复查胸腹部增强CT：病\n[BBOX-667] 情评价好转。于2025-12-5、2025-12-30、2026-1-23、2026-02-05行4周期AC方案化疗联合靶向治\n[BBOX-668] 疗，具体：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w+阿美替尼 110mg qd。现患者为进一\n[BBOX-669] 步治疗于我院就诊，门诊以“右肺上叶腺癌”收入我科。\n[BBOX-670] 自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。\n[BBOX-671] 既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病\n[BBOX-672] 史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。\n[BBOX-673] 过敏史：否认食物、药物过敏史。\n[BBOX-674] 个人史：出生原籍，长期居住生长于当地，否认疫区居住冶游史，平素偶有饮酒，否认吸烟及\n[BBOX-675] 第1页\n[BBOX-676] 入院记录\n[BBOX-677] 其他不良嗜好。\n[BBOX-678] 婚育史：适龄结婚，育有1子，家人均体健。\n[BBOX-679] 家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。\n[BBOX-680] 体格检查\n[BBOX-681] T36.4℃\n[BBOX-682] P95次/分\n[BBOX-683] R19次/分\n[BBOX-684] BP101/77mmHg\n[BBOX-685] 一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮\n[BBOX-686] 疹。背部可触及一大约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部\n[BBOX-687] 及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。\n[BBOX-688] 颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊\n[BBOX-689] 清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，H95次/分，律齐，各瓣\n[BBOX-690] 膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊\n[BBOX-691] 音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经\n[BBOX-692] 系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。\n[BBOX-693] 专科情况\n[BBOX-694] ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰\n[BBOX-695] 音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。\n[BBOX-696] 辅助检查\n[BBOX-697] 暂缺。\n[BBOX-698] 初步诊断：\n[BBOX-699] 1.右肺上叶腺癌伴肝脏、骨多发转移（\n[BBOX-700] cT4N2M1 IVB期 EGFR L858R+）\n[BBOX-701] 2.肝继发恶性肿瘤\n[BBOX-702] 3.骨继发恶性肿瘤\n[BBOX-703] 医师签名\n[BBOX-704] 第2页\n[BBOX-705] 出院证明书\n[BBOX-706] (病人保存联)\n[BBOX-707] 住院证字\n[BBOX-708] 号\n[BBOX-709] 性别：男 年龄：39岁 入院时间：2026-03-23 10:38\n[BBOX-710] 床号\n[BBOX-711] 出院时间：2026-03-25\n[BBOX-712] 病人单位或住址：\n[BBOX-713] 出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+） 2.肝继发恶性肿\n[BBOX-714] 瘤 3.骨继发恶性肿瘤 4.肝功能不全\n[BBOX-715] 诊疗小结：患者因“右肺上叶腺癌4周期化疗后1+月。”入院。入院查体：T36.4℃ ;P93次/分；\n[BBOX-716] R18次/分;BP107/70mmHg\n[BBOX-717] 诊疗经过：完善检查，2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急\n[BBOX-718] 诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；\n[BBOX-719] 2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml)\n[BBOX-720] ↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L\n[BBOX-721] FEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L)\n[BBOX-722] ↓。2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右\n[BBOX-723] 肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，\n[BBOX-724] 增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另\n[BBOX-725] 见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右\n[BBOX-726] 肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增\n[BBOX-727] 厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范\n[BBOX-728] 围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节\n[BBOX-729] 状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、\n[BBOX-730] 胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，\n[BBOX-731] 增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠\n[BBOX-732] 均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双\n[BBOX-733] 侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。患者肝\n[BBOX-734] 功能不全，予以保肝治疗，患者病情进展，考虑参加临床实验，予以办理出院。\n[BBOX-735] 治疗结果：好转\n[BBOX-736] 出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。 2、等待电话通\n[BBOX-737] 知临床试验筛查。 3、出院带药：-。4、门诊随访：\n[BBOX-738] 5、加强营养，清淡饮食，避免着凉，预防感\n[BBOX-739] 第1页/共2页\n[BBOX-740] \\begin{tabular}{ccccccl}\n[BBOX-741] \\hline\n[BBOX-742] NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 \\\\\n[BBOX-743] \\hline\n[BBOX-744] 1 & 标本颜色 & 黄色 & & & \\\\\n[BBOX-745] 2 & 标本性状 & 半稀便 & & & \\\\\n[BBOX-746] 3 & 红细胞 & 无 & /HP & 无 & 仪器法 \\\\\n[BBOX-747] 4 & 镜下白细胞 & 无 & /HP & 无 & 仪器法 \\\\\n[BBOX-748] 5 & 吞噬细胞 & 无 & /HP & 无 & 仪器法 \\\\\n[BBOX-749] 6 & 酵母样菌 & 无 & /HP & 无 & 仪器法 \\\\\n[BBOX-750] 7 & 脂肪球 & 无 & /HP & 无 & 仪器法 \\\\\n[BBOX-751] 8 & 脓细胞 & 无 & /HP & 无 & 仪器法 \\\\\n[BBOX-752] 9 & 淀粉样颗粒 & 无 & /HP & 无 & 仪器法 \\\\\n[BBOX-753] \\hline\n[BBOX-754] \\end{tabular}\n[BBOX-755] \\begin{tabular}{llllllll}\n[BBOX-756] 报告时间: 2026-03-23\n[BBOX-757] \\hline\n[BBOX-758] NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\\\\n[BBOX-759] \\hline\n[BBOX-760] 1 & 颜色 & 淡黄色 & & & & & \\\\\n[BBOX-761] 2 & 浊度 & 透明 & & & & & \\\\\n[BBOX-762] \\multicolumn{8}{l}{尿干化学分析} \\\\\n[BBOX-763] 3 & *尿胆原 & & & & 偶氮结合法 & & \\\\\n[BBOX-764] 4 & *胆红素 & & & & 偶氮偶合法 & & \\\\\n[BBOX-765] 5 & *酮体 & & & & 硝普化钠法 & & \\\\\n[BBOX-766] 6 & *尿潜血 & & & & 血红蛋白接触活性法 & & \\\\\n[BBOX-767] 7 & *尿蛋白 & & & & 蛋白质误差法 & & \\\\\n[BBOX-768] 9 & *亚硝酸盐 & & & & 硝酸盐还原法 & & \\\\\n[BBOX-769] 8 & 维生素C & & & & 干化学法 & & \\\\\n[BBOX-770] 10 & *白细胞 & & & & 酯酶法 & & \\\\\n[BBOX-771] 11 & *葡萄糖 & & & & 葡萄糖氧化酶法 & & \\\\\n[BBOX-772] 12 & *尿比重 & 1.025 & & 1.003-1.030 & 多聚电解质法 & & \\\\\n[BBOX-773] 13 & *PH值 & 5.00 & & 4.5-8.0 & 指示剂法 & & \\\\\n[BBOX-774] \\hline\n[BBOX-775] \\end{tabular}\n[BBOX-776] \\begin{tabular}{ccclllll}\n[BBOX-777] 报告时间: 2026-03-23\n[BBOX-778] \\hline\n[BBOX-779] NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\\\\n[BBOX-780] \\hline\n[BBOX-781] 1 & *总蛋白 & 81.60 & g/L & 65-85 & 比色法 & & \\\\\n[BBOX-782] 2 & *白蛋白 & 44.30 & g/L & 40-55 & 比色法 & & \\\\\n[BBOX-783] 3 & 球蛋白 & 37.30 & g/l & 20-40 & 计算法 & & \\\\\n[BBOX-784] 4 & *丙氨酸氨基转移酶 & 84.50 & U/L & 9-50 & 比色法 & & \\\\\n[BBOX-785] 5 & *天门冬氨酸氨基转移酶 & 47.40 & U/L & 15-40 & 比色法 & & \\\\\n[BBOX-786] 6 & *总胆红素 & 10.00 & umol/L & 0-26 & 重氮法 & & \\\\\n[BBOX-787] 7 & *直接胆红素 & 4.60 & umol/L & 0-8 & 重氮法 & & \\\\\n[BBOX-788] 8 & 间接胆红素 & 5.40 & umol/L & 0-13 & 计算法 & & \\\\\n[BBOX-789] 9 & 胆碱脂酶 & 8964.00 & U/L & 5320-12920 & 比色法 & & \\\\\n[BBOX-790] 10 & *葡萄糖 & 4.62 & mmol/L & 4.1-6.05 & 己糖激酶法 & & \\\\\n[BBOX-791] 11 & *钾 & 3.75 & mmol/L & 3.5-5.5 & 间接离子选择电极法 & & \\\\\n[BBOX-792] 12 & *钠 & 136.00 & mmol/L & 137-147 & 间接离子选择电极法 & & \\\\\n[BBOX-793] 13 & *氯 & 98.80 & mmol/L & 99-110 & 间接离子选择电极法 & & \\\\\n[BBOX-794] 14 & *钙 & 2.50 & mmol/L & 2.11-2.54 & 比色法 & & \\\\\n[BBOX-795] 15 & *肌酐 & 73.00 & umol/L & 59-104 & 酶法 & & \\\\\n[BBOX-796] 16 & *尿素 & 6.10 & mmol/L & 3.1-9.5 & 比色法 & & \\\\\n[BBOX-797] 17 & *尿酸 & 406.00 & umol/L & 202.3-416.5 & 比色法 & & \\\\\n[BBOX-798] 18 & 肾小球滤过率 & 111.07 & ml/min & >80 & 计算法 & & \\\\\n[BBOX-799] \\hline\n[BBOX-800] \\end{tabular}\n[BBOX-801] \\begin{tabular}{ccccccc}\n[BBOX-802] \\hline\n[BBOX-803] No. 英文名称 & 项 目 & 结果 & 单位 & 参考值 & 实验方法 \\\\\n[BBOX-804] \\hline\n[BBOX-805] 1 CEA & 癌胚抗原 & 163.87 & ng/ml & 0-4.5 & 化学发光法 \\\\\n[BBOX-806] 2 NSE & 神经元特异性烯醇化酶 & 49.25 & ng/ml & $<$16.5 & 化学发光法 \\\\\n[BBOX-807] 3 Pro-GRP & 胃泌素释放肽前体 & 55.98 & pg/ml & 0-78.62 & 化学发光法 \\\\\n[BBOX-808] \\hline\n[BBOX-809] \\end{tabular}\n[BBOX-810] \\begin{tabular}{llllllll}\n[BBOX-811] 报告时间: 2026-03-23\n[BBOX-812] \\hline\n[BBOX-813] NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\\\\n[BBOX-814] \\hline\n[BBOX-815] 1 & *凝血酶原时间 & 11.40 & 秒 & 9-14 & 凝固法 & & \\\\\n[BBOX-816] 2 & *国际标准化比值(INR) & 0.99 & & 0.77-1.19 & 计算法 & & \\\\\n[BBOX-817] 3 & 凝血酶原活动度 & 87 & \\% & 70-130 & 凝固法 & & \\\\\n[BBOX-818] 4 & *活化部分凝血活酶时间 & 28.00 & 秒 & 24.8-33.8 & 凝固法 & & \\\\\n[BBOX-819] 5 & *纤维蛋白原 & 4.04 & g/L & 2-4 & 凝固法 & & \\\\\n[BBOX-820] 6 & 凝血酶时间 & 17.10 & 秒 & 14-21 & 凝固法 & & \\\\\n[BBOX-821] 7 & D-二聚体 & 1.02 & mg/L FEU & 0-0.50 & 胶乳免疫比浊法 & & \\\\\n[BBOX-822] \\hline\n[BBOX-823] \\end{tabular}\n[BBOX-824] \\begin{tabular}{cccccccc}\n[BBOX-825] 报告时间: 2026-03-23\n[BBOX-826] \\hline\n[BBOX-827] NO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\\\\n[BBOX-828] \\hline\n[BBOX-829] 1 & *白细胞计数 & 6.77 & 10^9/L & 3.5-9.5 & 激光散射法 & & \\\\\n[BBOX-830] 2 & 中性粒细胞百分率 & 73.40 & \\% & 40-75 & 激光散射法+荧光染色法 & & \\\\\n[BBOX-831] 3 & 淋巴细胞百分率 & 15.30 & \\% & 20-50 & 激光散射法+荧光染色法 & & \\\\\n[BBOX-832] 4 & 单核细胞百分率 & 9.00 & \\% & 3-10 & 激光散射法+荧光染色法 & & \\\\\n[BBOX-833] 5 & 嗜酸细胞百分率 & 1.80 & \\% & 0.4-8.0 & 激光散射法+荧光染色法 & & \\\\\n[BBOX-834] 6 & 嗜碱细胞百分率 & 0.50 & \\% & 0.00-1.0 & 计算法 & & \\\\\n[BBOX-835] 7 & 中性粒细胞计数 & 4.97 & 10^9/L & 1.8-6.3 & 计算法 & & \\\\\n[BBOX-836] 8 & 淋巴细胞计数 & 1.04 & 10^9/L & 1.1-3.2 & 计算法 & & \\\\\n[BBOX-837] 9 & 单核细胞计数 & 0.61 & 10^9/L & 0.10-0.60 & 计算法 & & \\\\\n[BBOX-838] 10 & 嗜酸细胞计数 & 0.12 & 10^9/L & 0.02-0.52 & 计算法 & & \\\\\n[BBOX-839] 11 & 嗜碱细胞计数 & 0.03 & 10^9/L & 0-0.06 & 激光散色+荧光染色法 & & \\\\\n[BBOX-840] 12 & *红细胞计数 & 4.81 & 10^12/L & 4.3-5.8 & 阻抗法 & & \\\\\n[BBOX-841] 13 & *血红蛋白浓度 & 131.00 & g/l & 130-175 & 比色法 & & \\\\\n[BBOX-842] 14 & *红细胞压积 & 39.50 & \\% & 40-50 & 计算法 & & \\\\\n[BBOX-843] 15 & *平均红细胞体积 & 82.00 & fL & 82-100 & 阻抗法 & & \\\\\n[BBOX-844] 16 & 红细胞宽度-SD值 & 50.10 & fL & 37-50 & 阻抗法 & & \\\\\n[BBOX-845] 17 & 红细胞宽度-CV值 & 16.60 & \\% & 10.9-15.4 & 阻抗法 & & \\\\\n[BBOX-846] 18 & *平均血红蛋白含量 & 27.20 & pg & 27-34 & 计算法 & & \\\\\n[BBOX-847] 19 & *平均血红蛋白浓度 & 332.00 & g/l & 316-354 & 计算法 & & \\\\\n[BBOX-848] 20 & *血小板计数 & 167.00 & 10^9/L & 125-350 & 阻抗法 & & \\\\\n[BBOX-849] 21 & 平均血小板体积 & 13.10 & fL & 9-13 & 阻抗法 & & \\\\\n[BBOX-850] 22 & 血小板压积 & 0.22 & \\% & 0.108-0.282 & 计算法 & & \\\\\n[BBOX-851] 23 & 血小板分布宽度 & 16.80 & fL & 9-17 & 阻抗法 & & \\\\\n[BBOX-852] 24 & 大血小板比率 & 50.00 & \\% & 16.9-46.7 & 阻抗法 & & \\\\\n[BBOX-853] 25 & 大血小板计数 & 83.00 & 10^9/L & 30-90 & 计算法 & & \\\\\n[BBOX-854] \\hline\n[BBOX-855] \\end{tabular}\n[BBOX-856] 人民醫院\n[BBOX-857] 川渝HR\n[BBOX-858] 带*为川渝互认项目\n[BBOX-859] 医学影像检查报告单\n[BBOX-860] 扫码查看影像\n[BBOX-861] 检查号:\n[BBOX-862] 患者姓名:\n[BBOX-863] 性别:男\n[BBOX-864] 年龄:39岁\n[BBOX-865] 住院号:\n[BBOX-866] 申请科室\n[BBOX-867] 床号:023\n[BBOX-868] 联系电话\n[BBOX-869] 检查室:CT1(联影CT)(1住)\n[BBOX-870] 检查技师:羊媛颖\n[BBOX-871] 检查时间:2026-03-25 08:22:58\n[BBOX-872] 检查部位:[*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强]\n[BBOX-873] 检查技术:-\n[BBOX-874] 描述:\n[BBOX-875] 1、“肺CA”复查,右肺上叶见团块影,边缘呈分叶状,局部与胸膜粘连,见支气\n[BBOX-876] 管截断,较大层面范围约5.6cm×5.3cm,增强扫描呈轻度不均匀强化,周围见斑条\n[BBOX-877] 影及小结节影,较CT260121-240片病灶稍增大。\n[BBOX-878] 2、双肺另见长径约0.4-0.7cm微小结节,较大者位于右肺上叶前段(IM37)较前片\n[BBOX-879] 稍增大,必要时随诊。\n[BBOX-880] 3、右肺中叶及双肺下叶见散在斑条影。\n[BBOX-881] 4、心包少量积液。纵隔淋巴结显示,部分稍增大。双侧胸膜稍增厚。\n[BBOX-882] 5、肝右后叶见稍低密度结节,边缘稍模糊,增强扫描轻中度强化,边缘强化明\n[BBOX-883] 显,较大层面范围约1.2cm×0.9cm,转移灶可能,其它病变待排,较前稍缩小。\n[BBOX-884] 6、左侧肾上腺内侧支增粗,见结节状稍低密度影,增强扫描强化稍欠均匀,长径\n[BBOX-885] 约1.4cm,占位性病变或转移灶待排。较前稍增大。\n[BBOX-886] 7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。\n[BBOX-887] 8、右肾见稍低密度结节,较大者长径约1.3cm,增强扫描似见轻度强化,占位性病\n[BBOX-888] 变或转移灶待排。较前变化不大。\n[BBOX-889] 9、前列腺稍显丰满,强化稍欠均匀。\n[BBOX-890] 10、扫及双侧部分肋骨,胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻\n[BBOX-891] 骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏,转移灶可能,部分椎体\n[BBOX-892] 变扁,病理性骨折待排。\n[BBOX-893] 请结合临床及其它检查,必要时复查或进一步检查。\n[BBOX-894] 总结意见:\n[BBOX-895] 见上述。\n[BBOX-896] 报告者:申悦\n[BBOX-897] 审核医师:曹玉\n[BBOX-898] 报告时间:2026/3/25 8:48:11\n[BBOX-899] 审核时间:2026/3/25 9:26:23\n[BBOX-900] 注:此报告审核"
  }
]
2026-08-10 15:35:06,316 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:35:06.315+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:35:19,125 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:19,152 INFO     29 [SmartSplitter] SmartSplitter done: 19 chunks from 19 LLM segments (all bbox_id). Types: {'AdmissionRecord': 2, 'DischargeRecord': 6, 'ExaminationReport': 5, 'LabReport': 6}
2026-08-10 15:35:19,164 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 15:35:19,164 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks": "19 items, types={'AdmissionRecord': 2, 'DischargeRecord': 6, 'ExaminationReport': 5, 'LabReport': 6}"}
2026-08-10 15:35:19,164 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 15:35:19,166 INFO     29 [ChunkRouter] Routed 19 chunks into 4 groups: {'chunks_Admission': 2, 'chunks_Discharge': 6, 'chunks_Examination': 5, 'chunks_LabExam': 6}
2026-08-10 15:35:19,180 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 15:35:19,181 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | ChunkRouter:Router | outputs={"html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks": "19 items, types={'AdmissionRecord': 2, 'DischargeRecord': 6, 'ExaminationReport': 5, 'LabReport': 6}", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:35:19,181 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 15:35:19,190 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:35:19,191 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:35:19,191 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[15]
2026-08-10 15:35:19,191 INFO     29 [qwen-vl-table] positions ： [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:35:19,450 INFO     29 [qwen-vl-table] page=15, rect=595x842, img=(1654x2339)
2026-08-10 15:35:19,451 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:19,452 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 740, \"bbox_end\": 754, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccl}\n\\hline\nNO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 \\\\\n\\hline\n1 & 标本颜色 & 黄色 & & & \\\\\n2 & 标本性状 & 半稀便 & & & \\\\\n3 & 红细胞 & 无 & /HP & 无 & 仪器法 \\\\\n4 & 镜下白细胞 & 无 & /HP & 无 & 仪器法 \\\\\n5 & 吞噬细胞 & 无 & /HP & 无 & 仪器法 \\\\\n6 & 酵母样菌 & 无 & /HP & 无 & 仪器法 \\\\\n7 & 脂肪球 & 无 & /HP & 无 & 仪器法 \\\\\n8 & 脓细胞 & 无 & /HP & 无 & 仪器法 \\\\\n9 & 淀粉样颗粒 & 无 & /HP & 无 & 仪器法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:35:23,863 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:23,863 INFO     29 [qwen-vl-table] page=15 LLM output (len=1447):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "标本颜色",
      "item_code": null,
      "value": "黄色",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "标本性状",
      "item_code": null,
      "value": "半稀便",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": null,
      "value": "无",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    },
    {
      "name": "镜下白细胞",
      "item_code": null,
      "value": "无",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    },
    {
      "name": "吞噬细胞",
      "item_code": null,
      "value": "无",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    },
    {
      "name": "酵母样菌",
      "item_code": null,
      "value": "无",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    },
    {
      "name": "脂肪球",
      "item_code": null,
      "value": "无",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    },
    {
      "name": "脓细胞",
      "item_code": null,
      "value": "无",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    },
    {
      "name": "淀粉样颗粒",
      "item_code": null,
      "value": "无",
      "unit": "/HP",
      "reference_range": "无",
      "abnormal": false
    }
  ]
}
2026-08-10 15:35:23,863 INFO     29 [qwen-vl-table] coord grouping: {15: 9}
2026-08-10 15:35:23,867 INFO     29 [qwen-vl-table] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1313474, prompt_len=550
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
标本颜色、标本性状、红细胞、镜下白细胞、吞噬细胞、酵母样菌、脂肪球、脓细胞、淀粉样颗粒

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
2026-08-10 15:35:27,002 INFO     29 [qwen-vl-table] coord API raw response (len=433):
[
	{"text": "标本颜色", "bbox": [69, 200, 138, 214]},
	{"text": "标本性状", "bbox": [69, 217, 138, 231]},
	{"text": "红细胞", "bbox": [69, 234, 121, 248]},
	{"text": "镜下白细胞", "bbox": [69, 250, 154, 264]},
	{"text": "吞噬细胞", "bbox": [69, 267, 138, 280]},
	{"text": "酵母样菌", "bbox": [69, 283, 138, 297]},
	{"text": "脂肪球", "bbox": [69, 299, 121, 313]},
	{"text": "脓细胞", "bbox": [69, 316, 121, 329]},
	{"text": "淀粉样颗粒", "bbox": [69, 331, 154, 345]}
]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord API: raw_items=9, valid_items=9, elapsed=3.1s
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[0]: text=标本颜色, bbox=[69, 200, 138, 214]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[1]: text=标本性状, bbox=[69, 217, 138, 231]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[2]: text=红细胞, bbox=[69, 234, 121, 248]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[3]: text=镜下白细胞, bbox=[69, 250, 154, 264]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[4]: text=吞噬细胞, bbox=[69, 267, 138, 280]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[5]: text=酵母样菌, bbox=[69, 283, 138, 297]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[6]: text=脂肪球, bbox=[69, 299, 121, 313]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[7]: text=脓细胞, bbox=[69, 316, 121, 329]
2026-08-10 15:35:27,003 INFO     29 [qwen-vl-table] coord item[8]: text=淀粉样颗粒, bbox=[69, 331, 154, 345]
2026-08-10 15:35:27,004 INFO     29 [qwen-vl-table] page=15 coord: matched 9/9, time=3.1s
2026-08-10 15:35:27,004 INFO     29 [qwen-vl-table] new_positions (9):
[[16, 41.074044067382815, 82.14808813476563, 168.3780029296875, 180.1644631347656], [16, 41.074044067382815, 82.14808813476563, 182.69013317871094, 194.47659338378907], [16, 41.074044067382815, 72.02839611816407, 197.00226342773436, 208.7887236328125], [16, 41.074044067382815, 91.67250415039062, 210.47250366210938, 222.2589638671875], [16, 41.074044067382815, 82.14808813476563, 224.7846339111328, 235.7292041015625], [16, 41.074044067382815, 82.14808813476563, 238.2548741455078, 250.04133435058594], [16, 41.074044067382815, 72.02839611816407, 251.7251143798828, 263.51157458496095], [16, 41.074044067382815, 72.02839611816407, 266.03724462890625, 276.9818148193359], [16, 41.074044067382815, 91.67250415039062, 278.6655948486328, 290.4520550537109]]
2026-08-10 15:35:27,004 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=9, matched=9, pages=1, time=7.8s
2026-08-10 15:35:27,005 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:35:27,006 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:35:27,006 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[16]
2026-08-10 15:35:27,006 INFO     29 [qwen-vl-table] positions ： [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:35:27,276 INFO     29 [qwen-vl-table] page=16, rect=595x842, img=(1654x2339)
2026-08-10 15:35:27,277 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:27,277 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 755, \"bbox_end\": 775, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-23\n\\hline\nNO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\\\\n\\hline\n1 & 颜色 & 淡黄色 & & & & & \\\\\n2 & 浊度 & 透明 & & & & & \\\\\n\\multicolumn{8}{l}{尿干化学分析} \\\\\n3 & *尿胆原 & & & & 偶氮结合法 & & \\\\\n4 & *胆红素 & & & & 偶氮偶合法 & & \\\\\n5 & *酮体 & & & & 硝普化钠法 & & \\\\\n6 & *尿潜血 & & & & 血红蛋白接触活性法 & & \\\\\n7 & *尿蛋白 & & & & 蛋白质误差法 & & \\\\\n9 & *亚硝酸盐 & & & & 硝酸盐还原法 & & \\\\\n8 & 维生素C & & & & 干化学法 & & \\\\\n10 & *白细胞 & & & & 酯酶法 & & \\\\\n11 & *葡萄糖 & & & & 葡萄糖氧化酶法 & & \\\\\n12 & *尿比重 & 1.025 & & 1.003-1.030 & 多聚电解质法 & & \\\\\n13 & *PH值 & 5.00 & & 4.5-8.0 & 指示剂法 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:35:33,377 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:33,378 INFO     29 [qwen-vl-table] page=16 LLM output (len=2084):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "颜色",
      "item_code": null,
      "value": "淡黄色",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "浊度",
      "item_code": null,
      "value": "透明",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿胆原",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "胆红素",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "酮体",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿潜血",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿蛋白",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "亚硝酸盐",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "维生素C",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿比重",
      "item_code": null,
      "value": "1.025",
      "unit": null,
      "reference_range": "1.003-1.030",
      "abnormal": false
    },
    {
      "name": "PH值",
      "item_code": null,
      "value": "5.00",
      "unit": null,
      "reference_range": "4.5-8.0",
      "abnormal": false
    }
  ]
}
2026-08-10 15:35:33,378 INFO     29 [qwen-vl-table] coord grouping: {16: 13}
2026-08-10 15:35:33,382 INFO     29 [qwen-vl-table] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1452065, prompt_len=557
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
颜色、浊度、尿胆原、胆红素、酮体、尿潜血、尿蛋白、亚硝酸盐、维生素C、白细胞、葡萄糖、尿比重、PH值

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
2026-08-10 15:35:37,324 INFO     29 [qwen-vl-table] coord API raw response (len=612):
[
	{"text": "颜色", "bbox": [75, 185, 110, 198]},
	{"text": "浊度", "bbox": [75, 204, 110, 217]},
	{"text": "尿胆原", "bbox": [75, 242, 135, 255]},
	{"text": "胆红素", "bbox": [75, 261, 135, 274]},
	{"text": "酮体", "bbox": [75, 279, 119, 292]},
	{"text": "尿潜血", "bbox": [75, 297, 135, 310]},
	{"text": "尿蛋白", "bbox": [75, 316, 135, 329]},
	{"text": "亚硝酸盐", "bbox": [75, 334, 150, 347]},
	{"text": "维生素C", "bbox": [75, 352, 140, 365]},
	{"text": "白细胞", "bbox": [75, 370, 133, 383]},
	{"text": "葡萄糖", "bbox": [75, 388, 133, 401]},
	{"text": "尿比重", "bbox": [75, 406, 131, 419]},
	{"text": "PH值", "bbox": [75, 424, 113, 437]}
]
2026-08-10 15:35:37,324 INFO     29 [qwen-vl-table] coord API: raw_items=13, valid_items=13, elapsed=3.9s
2026-08-10 15:35:37,324 INFO     29 [qwen-vl-table] coord item[0]: text=颜色, bbox=[75, 185, 110, 198]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[1]: text=浊度, bbox=[75, 204, 110, 217]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[2]: text=尿胆原, bbox=[75, 242, 135, 255]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[3]: text=胆红素, bbox=[75, 261, 135, 274]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[4]: text=酮体, bbox=[75, 279, 119, 292]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[5]: text=尿潜血, bbox=[75, 297, 135, 310]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[6]: text=尿蛋白, bbox=[75, 316, 135, 329]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[7]: text=亚硝酸盐, bbox=[75, 334, 150, 347]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[8]: text=维生素C, bbox=[75, 352, 140, 365]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[9]: text=白细胞, bbox=[75, 370, 133, 383]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[10]: text=葡萄糖, bbox=[75, 388, 133, 401]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[11]: text=尿比重, bbox=[75, 406, 131, 419]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] coord item[12]: text=PH值, bbox=[75, 424, 113, 437]
2026-08-10 15:35:37,325 INFO     29 [qwen-vl-table] page=16 coord: matched 13/13, time=3.9s
2026-08-10 15:35:37,326 INFO     29 [qwen-vl-table] new_positions (13):
[[17, 44.64570007324219, 65.48036010742187, 155.74965270996094, 166.69422290039063], [17, 44.64570007324219, 65.48036010742187, 171.74556298828125, 182.69013317871094], [17, 44.64570007324219, 80.36226013183594, 203.73738354492187, 214.68195373535156], [17, 44.64570007324219, 80.36226013183594, 219.73329382324218, 230.67786401367186], [17, 44.64570007324219, 70.83784411621095, 234.88731408691405, 245.83188427734376], [17, 44.64570007324219, 80.36226013183594, 250.04133435058594, 260.9859045410156], [17, 44.64570007324219, 80.36226013183594, 266.03724462890625, 276.9818148193359], [17, 44.64570007324219, 89.29140014648438, 281.19126489257815, 292.1358350830078], [17, 44.64570007324219, 83.33864013671875, 296.34528515625, 307.2898553466797], [17, 44.64570007324219, 79.17170812988282, 311.4993054199219, 322.44387561035154], [17, 44.64570007324219, 79.17170812988282, 326.6533256835937, 337.59789587402344], [17, 44.64570007324219, 77.9811561279297, 341.8073459472656, 352.75191613769533], [17, 44.64570007324219, 67.26618811035156, 356.9613662109375, 367.90593640136717]]
2026-08-10 15:35:37,326 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=13, matched=13, pages=1, time=10.3s
2026-08-10 15:35:37,328 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:35:37,330 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:35:37,330 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[17]
2026-08-10 15:35:37,330 INFO     29 [qwen-vl-table] positions ： [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:35:37,591 INFO     29 [qwen-vl-table] page=17, rect=595x842, img=(1654x2339)
2026-08-10 15:35:37,591 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:37,592 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 776, \"bbox_end\": 800, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccclllll}\n报告时间: 2026-03-23\n\\hline\nNO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\\\\n\\hline\n1 & *总蛋白 & 81.60 & g/L & 65-85 & 比色法 & & \\\\\n2 & *白蛋白 & 44.30 & g/L & 40-55 & 比色法 & & \\\\\n3 & 球蛋白 & 37.30 & g/l & 20-40 & 计算法 & & \\\\\n4 & *丙氨酸氨基转移酶 & 84.50 & U/L & 9-50 & 比色法 & & \\\\\n5 & *天门冬氨酸氨基转移酶 & 47.40 & U/L & 15-40 & 比色法 & & \\\\\n6 & *总胆红素 & 10.00 & umol/L & 0-26 & 重氮法 & & \\\\\n7 & *直接胆红素 & 4.60 & umol/L & 0-8 & 重氮法 & & \\\\\n8 & 间接胆红素 & 5.40 & umol/L & 0-13 & 计算法 & & \\\\\n9 & 胆碱脂酶 & 8964.00 & U/L & 5320-12920 & 比色法 & & \\\\\n10 & *葡萄糖 & 4.62 & mmol/L & 4.1-6.05 & 己糖激酶法 & & \\\\\n11 & *钾 & 3.75 & mmol/L & 3.5-5.5 & 间接离子选择电极法 & & \\\\\n12 & *钠 & 136.00 & mmol/L & 137-147 & 间接离子选择电极法 & & \\\\\n13 & *氯 & 98.80 & mmol/L & 99-110 & 间接离子选择电极法 & & \\\\\n14 & *钙 & 2.50 & mmol/L & 2.11-2.54 & 比色法 & & \\\\\n15 & *肌酐 & 73.00 & umol/L & 59-104 & 酶法 & & \\\\\n16 & *尿素 & 6.10 & mmol/L & 3.1-9.5 & 比色法 & & \\\\\n17 & *尿酸 & 406.00 & umol/L & 202.3-416.5 & 比色法 & & \\\\\n18 & 肾小球滤过率 & 111.07 & ml/min & >80 & 计算法 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:35:38,115 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:35:38.114+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:35:48,911 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:48,911 INFO     29 [qwen-vl-table] page=17 LLM output (len=3026):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "总蛋白",
      "item_code": null,
      "value": "81.60",
      "unit": "g/L",
      "reference_range": "65-85",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": null,
      "value": "44.30",
      "unit": "g/L",
      "reference_range": "40-55",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": null,
      "value": "37.30",
      "unit": "g/l",
      "reference_range": "20-40",
      "abnormal": false
    },
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": null,
      "value": "84.50",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": true
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": null,
      "value": "47.40",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": true
    },
    {
      "name": "总胆红素",
      "item_code": null,
      "value": "10.00",
      "unit": "umol/L",
      "reference_range": "0-26",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": null,
      "value": "4.60",
      "unit": "umol/L",
      "reference_range": "0-8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": null,
      "value": "5.40",
      "unit": "umol/L",
      "reference_range": "0-13",
      "abnormal": false
    },
    {
      "name": "胆碱脂酶",
      "item_code": null,
      "value": "8964.00",
      "unit": "U/L",
      "reference_range": "5320-12920",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": null,
      "value": "4.62",
      "unit": "mmol/L",
      "reference_range": "4.1-6.05",
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": null,
      "value": "3.75",
      "unit": "mmol/L",
      "reference_range": "3.5-5.5",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": null,
      "value": "136.00",
      "unit": "mmol/L",
      "reference_range": "137-147",
      "abnormal": true
    },
    {
      "name": "氯",
      "item_code": null,
      "value": "98.80",
      "unit": "mmol/L",
      "reference_range": "99-110",
      "abnormal": true
    },
    {
      "name": "钙",
      "item_code": null,
      "value": "2.50",
      "unit": "mmol/L",
      "reference_range": "2.11-2.54",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": null,
      "value": "73.00",
      "unit": "umol/L",
      "reference_range": "59-104",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": null,
      "value": "6.10",
      "unit": "mmol/L",
      "reference_range": "3.1-9.5",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": null,
      "value": "406.00",
      "unit": "umol/L",
      "reference_range": "202.3-416.5",
      "abnormal": false
    },
    {
      "name": "肾小球滤过率",
      "item_code": null,
      "value": "111.07",
      "unit": "ml/min",
      "reference_range": ">80",
      "abnormal": false
    }
  ]
}
2026-08-10 15:35:48,911 INFO     29 [qwen-vl-table] coord grouping: {17: 18}
2026-08-10 15:35:48,919 INFO     29 [qwen-vl-table] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1576583, prompt_len=588
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
总蛋白、白蛋白、球蛋白、丙氨酸氨基转移酶、天门冬氨酸氨基转移酶、总胆红素、直接胆红素、间接胆红素、胆碱脂酶、葡萄糖、钾、钠、氯、钙、肌酐、尿素、尿酸、肾小球滤过率

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
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord API raw response (len=855):
[
	{"text": "总蛋白", "bbox": [80, 194, 138, 207]},
	{"text": "白蛋白", "bbox": [80, 210, 138, 223]},
	{"text": "球蛋白", "bbox": [80, 226, 130, 239]},
	{"text": "丙氨酸氨基转移酶", "bbox": [80, 241, 219, 254]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [80, 257, 252, 270]},
	{"text": "总胆红素", "bbox": [80, 273, 152, 286]},
	{"text": "直接胆红素", "bbox": [80, 289, 167, 301]},
	{"text": "间接胆红素", "bbox": [80, 304, 159, 317]},
	{"text": "胆碱脂酶", "bbox": [77, 319, 142, 332]},
	{"text": "葡萄糖", "bbox": [77, 335, 134, 348]},
	{"text": "钾", "bbox": [77, 350, 100, 363]},
	{"text": "钠", "bbox": [77, 366, 99, 379]},
	{"text": "氯", "bbox": [77, 381, 99, 394]},
	{"text": "钙", "bbox": [77, 397, 99, 410]},
	{"text": "肌酐", "bbox": [77, 413, 114, 426]},
	{"text": "尿素", "bbox": [77, 429, 114, 442]},
	{"text": "尿酸", "bbox": [77, 444, 114, 457]},
	{"text": "肾小球滤过率", "bbox": [70, 460, 172, 473]}
]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord API: raw_items=18, valid_items=18, elapsed=5.0s
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[0]: text=总蛋白, bbox=[80, 194, 138, 207]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[1]: text=白蛋白, bbox=[80, 210, 138, 223]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[2]: text=球蛋白, bbox=[80, 226, 130, 239]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[3]: text=丙氨酸氨基转移酶, bbox=[80, 241, 219, 254]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[4]: text=天门冬氨酸氨基转移酶, bbox=[80, 257, 252, 270]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[5]: text=总胆红素, bbox=[80, 273, 152, 286]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[6]: text=直接胆红素, bbox=[80, 289, 167, 301]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[7]: text=间接胆红素, bbox=[80, 304, 159, 317]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[8]: text=胆碱脂酶, bbox=[77, 319, 142, 332]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[9]: text=葡萄糖, bbox=[77, 335, 134, 348]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[10]: text=钾, bbox=[77, 350, 100, 363]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[11]: text=钠, bbox=[77, 366, 99, 379]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[12]: text=氯, bbox=[77, 381, 99, 394]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[13]: text=钙, bbox=[77, 397, 99, 410]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[14]: text=肌酐, bbox=[77, 413, 114, 426]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[15]: text=尿素, bbox=[77, 429, 114, 442]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[16]: text=尿酸, bbox=[77, 444, 114, 457]
2026-08-10 15:35:53,968 INFO     29 [qwen-vl-table] coord item[17]: text=肾小球滤过率, bbox=[70, 460, 172, 473]
2026-08-10 15:35:53,969 INFO     29 [qwen-vl-table] page=17 coord: matched 18/18, time=5.0s
2026-08-10 15:35:53,969 INFO     29 [qwen-vl-table] new_positions (18):
[[18, 47.622080078125, 82.14808813476563, 163.32666284179686, 174.27123303222655], [18, 47.622080078125, 82.14808813476563, 176.79690307617187, 187.74147326660156], [18, 47.622080078125, 77.38588012695313, 190.26714331054689, 201.21171350097657], [18, 47.622080078125, 130.3654442138672, 202.89549353027343, 213.8400637207031], [18, 47.622080078125, 150.00955224609376, 216.36573376464844, 227.31030395507813], [18, 47.622080078125, 90.4819521484375, 229.83597399902342, 240.7805441894531], [18, 47.622080078125, 99.41109216308594, 243.30621423339844, 253.40889440917968], [18, 47.622080078125, 94.64888415527344, 255.934564453125, 266.87913464355466], [18, 45.83625207519531, 84.52919213867187, 268.56291467285155, 279.50748486328126], [18, 45.83625207519531, 79.76698413085938, 282.03315490722656, 292.9777250976562], [18, 45.83625207519531, 59.527600097656254, 294.6615051269531, 305.6060753173828], [18, 45.83625207519531, 58.93232409667969, 308.1317453613281, 319.07631555175783], [18, 45.83625207519531, 58.93232409667969, 320.76009558105466, 331.7046657714844], [18, 45.83625207519531, 58.93232409667969, 334.23033581542967, 345.1749060058594], [18, 45.83625207519531, 67.86146411132813, 347.7005760498047, 358.6451462402344], [18, 45.83625207519531, 67.86146411132813, 361.1708162841797, 372.11538647460935], [18, 45.83625207519531, 67.86146411132813, 373.79916650390624, 384.74373669433595], [18, 41.669320068359376, 102.38747216796875, 387.26940673828125, 398.2139769287109]]
2026-08-10 15:35:53,969 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=18, matched=18, pages=1, time=16.6s
2026-08-10 15:35:53,970 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:35:53,976 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:35:53,976 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[18]
2026-08-10 15:35:53,976 INFO     29 [qwen-vl-table] positions ： [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:35:54,223 INFO     29 [qwen-vl-table] page=18, rect=595x842, img=(1654x2339)
2026-08-10 15:35:54,224 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:54,224 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 801, \"bbox_end\": 809, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n\\hline\nNo. 英文名称 & 项 目 & 结果 & 单位 & 参考值 & 实验方法 \\\\\n\\hline\n1 CEA & 癌胚抗原 & 163.87 & ng/ml & 0-4.5 & 化学发光法 \\\\\n2 NSE & 神经元特异性烯醇化酶 & 49.25 & ng/ml & $<$16.5 & 化学发光法 \\\\\n3 Pro-GRP & 胃泌素释放肽前体 & 55.98 & pg/ml & 0-78.62 & 化学发光法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:35:56,820 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:56,821 INFO     29 [qwen-vl-table] page=18 LLM output (len=563):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "癌胚抗原",
      "item_code": "CEA",
      "value": "163.87",
      "unit": "ng/ml",
      "reference_range": "0-4.5",
      "abnormal": true
    },
    {
      "name": "神经元特异性烯醇化酶",
      "item_code": "NSE",
      "value": "49.25",
      "unit": "ng/ml",
      "reference_range": "<16.5",
      "abnormal": true
    },
    {
      "name": "胃泌素释放肽前体",
      "item_code": "Pro-GRP",
      "value": "55.98",
      "unit": "pg/ml",
      "reference_range": "0-78.62",
      "abnormal": false
    }
  ]
}
2026-08-10 15:35:56,821 INFO     29 [qwen-vl-table] coord grouping: {18: 3}
2026-08-10 15:35:56,824 INFO     29 [qwen-vl-table] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1145622, prompt_len=531
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
癌胚抗原、神经元特异性烯醇化酶、胃泌素释放肽前体

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
2026-08-10 15:35:58,796 INFO     29 [qwen-vl-table] coord API raw response (len=159):
[
	{"text": "癌胚抗原", "bbox": [181, 225, 250, 240]},
	{"text": "神经元特异性烯醇化酶", "bbox": [181, 242, 354, 257]},
	{"text": "胃泌素释放肽前体", "bbox": [181, 258, 320, 273]}
]
2026-08-10 15:35:58,796 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=2.0s
2026-08-10 15:35:58,797 INFO     29 [qwen-vl-table] coord item[0]: text=癌胚抗原, bbox=[181, 225, 250, 240]
2026-08-10 15:35:58,797 INFO     29 [qwen-vl-table] coord item[1]: text=神经元特异性烯醇化酶, bbox=[181, 242, 354, 257]
2026-08-10 15:35:58,797 INFO     29 [qwen-vl-table] coord item[2]: text=胃泌素释放肽前体, bbox=[181, 258, 320, 273]
2026-08-10 15:35:58,797 INFO     29 [qwen-vl-table] page=18 coord: matched 3/3, time=2.0s
2026-08-10 15:35:58,797 INFO     29 [qwen-vl-table] new_positions (3):
[[19, 107.74495617675781, 148.81900024414062, 189.42525329589844, 202.05360351562499], [19, 107.74495617675781, 210.72770434570313, 203.73738354492187, 216.36573376464844], [19, 107.74495617675781, 190.4883203125, 217.20762377929688, 229.83597399902342]]
2026-08-10 15:35:58,797 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=4.8s
2026-08-10 15:35:58,798 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:35:58,799 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:35:58,799 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[19]
2026-08-10 15:35:58,799 INFO     29 [qwen-vl-table] positions ： [[19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:35:59,054 INFO     29 [qwen-vl-table] page=19, rect=595x842, img=(1654x2339)
2026-08-10 15:35:59,054 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:35:59,054 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 810, \"bbox_end\": 823, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-23\n\\hline\nNO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\\\\n\\hline\n1 & *凝血酶原时间 & 11.40 & 秒 & 9-14 & 凝固法 & & \\\\\n2 & *国际标准化比值(INR) & 0.99 & & 0.77-1.19 & 计算法 & & \\\\\n3 & 凝血酶原活动度 & 87 & \\% & 70-130 & 凝固法 & & \\\\\n4 & *活化部分凝血活酶时间 & 28.00 & 秒 & 24.8-33.8 & 凝固法 & & \\\\\n5 & *纤维蛋白原 & 4.04 & g/L & 2-4 & 凝固法 & & \\\\\n6 & 凝血酶时间 & 17.10 & 秒 & 14-21 & 凝固法 & & \\\\\n7 & D-二聚体 & 1.02 & mg/L FEU & 0-0.50 & 胶乳免疫比浊法 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:36:03,108 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:03,108 INFO     29 [qwen-vl-table] page=19 LLM output (len=1204):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "凝血酶原时间",
      "item_code": null,
      "value": "11.40",
      "unit": "秒",
      "reference_range": "9-14",
      "abnormal": false
    },
    {
      "name": "国际标准化比值",
      "item_code": "INR",
      "value": "0.99",
      "unit": null,
      "reference_range": "0.77-1.19",
      "abnormal": false
    },
    {
      "name": "凝血酶原活动度",
      "item_code": null,
      "value": "87",
      "unit": "%",
      "reference_range": "70-130",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间",
      "item_code": null,
      "value": "28.00",
      "unit": "秒",
      "reference_range": "24.8-33.8",
      "abnormal": false
    },
    {
      "name": "纤维蛋白原",
      "item_code": null,
      "value": "4.04",
      "unit": "g/L",
      "reference_range": "2-4",
      "abnormal": true
    },
    {
      "name": "凝血酶时间",
      "item_code": null,
      "value": "17.10",
      "unit": "秒",
      "reference_range": "14-21",
      "abnormal": false
    },
    {
      "name": "D-二聚体",
      "item_code": null,
      "value": "1.02",
      "unit": "mg/L FEU",
      "reference_range": "0-0.50",
      "abnormal": true
    }
  ]
}
2026-08-10 15:36:03,108 INFO     29 [qwen-vl-table] coord grouping: {19: 7}
2026-08-10 15:36:03,111 INFO     29 [qwen-vl-table] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1322221, prompt_len=558
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间、国际标准化比值、凝血酶原活动度、活化部分凝血活酶时间、纤维蛋白原、凝血酶时间、D-二聚体

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
2026-08-10 15:36:06,040 INFO     29 [qwen-vl-table] coord API raw response (len=355):
[
	{"text": "凝血酶原时间", "bbox": [79, 191, 185, 204]},
	{"text": "国际标准化比值", "bbox": [80, 207, 238, 219]},
	{"text": "凝血酶原活动度", "bbox": [79, 222, 191, 234]},
	{"text": "活化部分凝血活酶时间", "bbox": [79, 238, 248, 250]},
	{"text": "纤维蛋白原", "bbox": [79, 252, 164, 264]},
	{"text": "凝血酶时间", "bbox": [77, 267, 155, 279]},
	{"text": "D-二聚体", "bbox": [74, 282, 139, 294]}
]
2026-08-10 15:36:06,040 INFO     29 [qwen-vl-table] coord API: raw_items=7, valid_items=7, elapsed=2.9s
2026-08-10 15:36:06,040 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[79, 191, 185, 204]
2026-08-10 15:36:06,040 INFO     29 [qwen-vl-table] coord item[1]: text=国际标准化比值, bbox=[80, 207, 238, 219]
2026-08-10 15:36:06,040 INFO     29 [qwen-vl-table] coord item[2]: text=凝血酶原活动度, bbox=[79, 222, 191, 234]
2026-08-10 15:36:06,040 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间, bbox=[79, 238, 248, 250]
2026-08-10 15:36:06,040 INFO     29 [qwen-vl-table] coord item[4]: text=纤维蛋白原, bbox=[79, 252, 164, 264]
2026-08-10 15:36:06,041 INFO     29 [qwen-vl-table] coord item[5]: text=凝血酶时间, bbox=[77, 267, 155, 279]
2026-08-10 15:36:06,041 INFO     29 [qwen-vl-table] coord item[6]: text=D-二聚体, bbox=[74, 282, 139, 294]
2026-08-10 15:36:06,041 INFO     29 [qwen-vl-table] page=19 coord: matched 7/7, time=2.9s
2026-08-10 15:36:06,041 INFO     29 [qwen-vl-table] new_positions (7):
[[20, 47.02680407714844, 110.12606018066407, 160.80099279785156, 171.74556298828125], [20, 47.622080078125, 141.6756882324219, 174.27123303222655, 184.37391320800782], [20, 47.02680407714844, 113.69771618652344, 186.89958325195312, 197.00226342773436], [20, 47.02680407714844, 147.62844824218752, 200.36982348632813, 210.47250366210938], [20, 47.02680407714844, 97.62526416015625, 212.15628369140626, 222.2589638671875], [20, 45.83625207519531, 92.26778015136719, 224.7846339111328, 234.88731408691405], [20, 44.05042407226563, 82.7433641357422, 237.41298413085937, 247.51566430664062]]
2026-08-10 15:36:06,041 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=7, matched=7, pages=1, time=7.2s
2026-08-10 15:36:06,043 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:36:06,045 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:36:06,045 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[20]
2026-08-10 15:36:06,045 INFO     29 [qwen-vl-table] positions ： [[20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:36:06,316 INFO     29 [qwen-vl-table] page=20, rect=595x842, img=(1654x2339)
2026-08-10 15:36:06,316 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:06,317 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 824, \"bbox_end\": 855, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccc}\n报告时间: 2026-03-23\n\\hline\nNO & 项 目 & 结果 & 单位 & 参考值 & 检测方法 & & \\\\\n\\hline\n1 & *白细胞计数 & 6.77 & 10^9/L & 3.5-9.5 & 激光散射法 & & \\\\\n2 & 中性粒细胞百分率 & 73.40 & \\% & 40-75 & 激光散射法+荧光染色法 & & \\\\\n3 & 淋巴细胞百分率 & 15.30 & \\% & 20-50 & 激光散射法+荧光染色法 & & \\\\\n4 & 单核细胞百分率 & 9.00 & \\% & 3-10 & 激光散射法+荧光染色法 & & \\\\\n5 & 嗜酸细胞百分率 & 1.80 & \\% & 0.4-8.0 & 激光散射法+荧光染色法 & & \\\\\n6 & 嗜碱细胞百分率 & 0.50 & \\% & 0.00-1.0 & 计算法 & & \\\\\n7 & 中性粒细胞计数 & 4.97 & 10^9/L & 1.8-6.3 & 计算法 & & \\\\\n8 & 淋巴细胞计数 & 1.04 & 10^9/L & 1.1-3.2 & 计算法 & & \\\\\n9 & 单核细胞计数 & 0.61 & 10^9/L & 0.10-0.60 & 计算法 & & \\\\\n10 & 嗜酸细胞计数 & 0.12 & 10^9/L & 0.02-0.52 & 计算法 & & \\\\\n11 & 嗜碱细胞计数 & 0.03 & 10^9/L & 0-0.06 & 激光散色+荧光染色法 & & \\\\\n12 & *红细胞计数 & 4.81 & 10^12/L & 4.3-5.8 & 阻抗法 & & \\\\\n13 & *血红蛋白浓度 & 131.00 & g/l & 130-175 & 比色法 & & \\\\\n14 & *红细胞压积 & 39.50 & \\% & 40-50 & 计算法 & & \\\\\n15 & *平均红细胞体积 & 82.00 & fL & 82-100 & 阻抗法 & & \\\\\n16 & 红细胞宽度-SD值 & 50.10 & fL & 37-50 & 阻抗法 & & \\\\\n17 & 红细胞宽度-CV值 & 16.60 & \\% & 10.9-15.4 & 阻抗法 & & \\\\\n18 & *平均血红蛋白含量 & 27.20 & pg & 27-34 & 计算法 & & \\\\\n19 & *平均血红蛋白浓度 & 332.00 & g/l & 316-354 & 计算法 & & \\\\\n20 & *血小板计数 & 167.00 & 10^9/L & 125-350 & 阻抗法 & & \\\\\n21 & 平均血小板体积 & 13.10 & fL & 9-13 & 阻抗法 & & \\\\\n22 & 血小板压积 & 0.22 & \\% & 0.108-0.282 & 计算法 & & \\\\\n23 & 血小板分布宽度 & 16.80 & fL & 9-17 & 阻抗法 & & \\\\\n24 & 大血小板比率 & 50.00 & \\% & 16.9-46.7 & 阻抗法 & & \\\\\n25 & 大血小板计数 & 83.00 & 10^9/L & 30-90 & 计算法 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:36:09,979 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:36:09.976+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:36:21,293 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:21,293 INFO     29 [qwen-vl-table] page=20 LLM output (len=4219):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": null,
      "value": "6.77",
      "unit": "10^9/L",
      "reference_range": "3.5-9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分率",
      "item_code": null,
      "value": "73.40",
      "unit": "%",
      "reference_range": "40-75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分率",
      "item_code": null,
      "value": "15.30",
      "unit": "%",
      "reference_range": "20-50",
      "abnormal": true
    },
    {
      "name": "单核细胞百分率",
      "item_code": null,
      "value": "9.00",
      "unit": "%",
      "reference_range": "3-10",
      "abnormal": false
    },
    {
      "name": "嗜酸细胞百分率",
      "item_code": null,
      "value": "1.80",
      "unit": "%",
      "reference_range": "0.4-8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱细胞百分率",
      "item_code": null,
      "value": "0.50",
      "unit": "%",
      "reference_range": "0.00-1.0",
      "abnormal": false
    },
    {
      "name": "中性粒细胞计数",
      "item_code": null,
      "value": "4.97",
      "unit": "10^9/L",
      "reference_range": "1.8-6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞计数",
      "item_code": null,
      "value": "1.04",
      "unit": "10^9/L",
      "reference_range": "1.1-3.2",
      "abnormal": true
    },
    {
      "name": "单核细胞计数",
      "item_code": null,
      "value": "0.61",
      "unit": "10^9/L",
      "reference_range": "0.10-0.60",
      "abnormal": true
    },
    {
      "name": "嗜酸细胞计数",
      "item_code": null,
      "value": "0.12",
      "unit": "10^9/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱细胞计数",
      "item_code": null,
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0-0.06",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": null,
      "value": "4.81",
      "unit": "10^12/L",
      "reference_range": "4.3-5.8",
      "abnormal": false
    },
    {
      "name": "血红蛋白浓度",
      "item_code": null,
      "value": "131.00",
      "unit": "g/l",
      "reference_range": "130-175",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": null,
      "value": "39.50",
      "unit": "%",
      "reference_range": "40-50",
      "abnormal": true
    },
    {
      "name": "平均红细胞体积",
      "item_code": null,
      "value": "82.00",
      "unit": "fL",
      "reference_range": "82-100",
      "abnormal": false
    },
    {
      "name": "红细胞宽度-SD值",
      "item_code": null,
      "value": "50.10",
      "unit": "fL",
      "reference_range": "37-50",
      "abnormal": true
    },
    {
      "name": "红细胞宽度-CV值",
      "item_code": null,
      "value": "16.60",
      "unit": "%",
      "reference_range": "10.9-15.4",
      "abnormal": true
    },
    {
      "name": "平均血红蛋白含量",
      "item_code": null,
      "value": "27.20",
      "unit": "pg",
      "reference_range": "27-34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": null,
      "value": "332.00",
      "unit": "g/l",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": null,
      "value": "167.00",
      "unit": "10^9/L",
      "reference_range": "125-350",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": null,
      "value": "13.10",
      "unit": "fL",
      "reference_range": "9-13",
      "abnormal": true
    },
    {
      "name": "血小板压积",
      "item_code": null,
      "value": "0.22",
      "unit": "%",
      "reference_range": "0.108-0.282",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": null,
      "value": "16.80",
      "unit": "fL",
      "reference_range": "9-17",
      "abnormal": false
    },
    {
      "name": "大血小板比率",
      "item_code": null,
      "value": "50.00",
      "unit": "%",
      "reference_range": "16.9-46.7",
      "abnormal": true
    },
    {
      "name": "大血小板计数",
      "item_code": null,
      "value": "83.00",
      "unit": "10^9/L",
      "reference_range": "30-90",
      "abnormal": false
    }
  ]
}
2026-08-10 15:36:21,293 INFO     29 [qwen-vl-table] coord grouping: {20: 25}
2026-08-10 15:36:21,297 INFO     29 [qwen-vl-table] coord API call start, page=20, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2001842, prompt_len=696
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、中性粒细胞百分率、淋巴细胞百分率、单核细胞百分率、嗜酸细胞百分率、嗜碱细胞百分率、中性粒细胞计数、淋巴细胞计数、单核细胞计数、嗜酸细胞计数、嗜碱细胞计数、红细胞计数、血红蛋白浓度、红细胞压积、平均红细胞体积、红细胞宽度-SD值、红细胞宽度-CV值、平均血红蛋白含量、平均血红蛋白浓度、血小板计数、平均血小板体积、血小板压积、血小板分布宽度、大血小板比率、大血小板计数

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
2026-08-10 15:36:28,380 INFO     29 [qwen-vl-table] coord API raw response (len=1267):
[
	{"text": "白细胞计数", "bbox": [67, 169, 160, 184]},
	{"text": "中性粒细胞百分率", "bbox": [67, 185, 200, 200]},
	{"text": "淋巴细胞百分率", "bbox": [67, 201, 183, 216]},
	{"text": "单核细胞百分率", "bbox": [67, 217, 183, 232]},
	{"text": "嗜酸细胞百分率", "bbox": [67, 233, 183, 248]},
	{"text": "嗜碱细胞百分率", "bbox": [67, 249, 183, 264]},
	{"text": "中性粒细胞计数", "bbox": [67, 265, 180, 280]},
	{"text": "淋巴细胞计数", "bbox": [64, 282, 162, 297]},
	{"text": "单核细胞计数", "bbox": [64, 298, 162, 313]},
	{"text": "嗜酸细胞计数", "bbox": [64, 315, 162, 330]},
	{"text": "嗜碱细胞计数", "bbox": [64, 331, 162, 346]},
	{"text": "红细胞计数", "bbox": [64, 348, 151, 363]},
	{"text": "血红蛋白浓度", "bbox": [64, 365, 167, 380]},
	{"text": "红细胞压积", "bbox": [64, 381, 151, 396]},
	{"text": "平均红细胞体积", "bbox": [64, 398, 183, 413]},
	{"text": "红细胞宽度-SD值", "bbox": [60, 414, 183, 429]},
	{"text": "红细胞宽度-CV值", "bbox": [60, 431, 183, 446]},
	{"text": "平均血红蛋白含量", "bbox": [60, 448, 198, 463]},
	{"text": "平均血红蛋白浓度", "bbox": [60, 465, 198, 480]},
	{"text": "血小板计数", "bbox": [60, 481, 146, 496]},
	{"text": "平均血小板体积", "bbox": [60, 498, 171, 513]},
	{"text": "血小板压积", "bbox": [57, 515, 137, 530]},
	{"text": "血小板分布宽度", "bbox": [57, 532, 170, 547]},
	{"text": "大血小板比率", "bbox": [57, 549, 152, 564]},
	{"text": "大血小板计数", "bbox": [57, 566, 152, 581]}
]
2026-08-10 15:36:28,380 INFO     29 [qwen-vl-table] coord API: raw_items=25, valid_items=25, elapsed=7.1s
2026-08-10 15:36:28,380 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[67, 169, 160, 184]
2026-08-10 15:36:28,380 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞百分率, bbox=[67, 185, 200, 200]
2026-08-10 15:36:28,380 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞百分率, bbox=[67, 201, 183, 216]
2026-08-10 15:36:28,380 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞百分率, bbox=[67, 217, 183, 232]
2026-08-10 15:36:28,380 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸细胞百分率, bbox=[67, 233, 183, 248]
2026-08-10 15:36:28,380 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱细胞百分率, bbox=[67, 249, 183, 264]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞计数, bbox=[67, 265, 180, 280]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞计数, bbox=[64, 282, 162, 297]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞计数, bbox=[64, 298, 162, 313]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸细胞计数, bbox=[64, 315, 162, 330]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱细胞计数, bbox=[64, 331, 162, 346]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞计数, bbox=[64, 348, 151, 363]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白浓度, bbox=[64, 365, 167, 380]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[64, 381, 151, 396]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积, bbox=[64, 398, 183, 413]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[15]: text=红细胞宽度-SD值, bbox=[60, 414, 183, 429]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[16]: text=红细胞宽度-CV值, bbox=[60, 431, 183, 446]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[17]: text=平均血红蛋白含量, bbox=[60, 448, 198, 463]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[18]: text=平均血红蛋白浓度, bbox=[60, 465, 198, 480]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[19]: text=血小板计数, bbox=[60, 481, 146, 496]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板体积, bbox=[60, 498, 171, 513]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[21]: text=血小板压积, bbox=[57, 515, 137, 530]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[22]: text=血小板分布宽度, bbox=[57, 532, 170, 547]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[23]: text=大血小板比率, bbox=[57, 549, 152, 564]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] coord item[24]: text=大血小板计数, bbox=[57, 566, 152, 581]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] page=20 coord: matched 25/25, time=7.1s
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] new_positions (25):
[[21, 39.88349206542969, 95.24416015625, 142.27941247558593, 154.9077626953125], [21, 39.88349206542969, 119.05520019531251, 155.74965270996094, 168.3780029296875], [21, 39.88349206542969, 108.93550817871095, 169.21989294433592, 181.8482431640625], [21, 39.88349206542969, 108.93550817871095, 182.69013317871094, 195.3184833984375], [21, 39.88349206542969, 108.93550817871095, 196.16037341308595, 208.7887236328125], [21, 39.88349206542969, 108.93550817871095, 209.63061364746093, 222.2589638671875], [21, 39.88349206542969, 107.14968017578126, 223.10085388183595, 235.7292041015625], [21, 38.0976640625, 96.43471215820313, 237.41298413085937, 250.04133435058594], [21, 38.0976640625, 96.43471215820313, 250.88322436523438, 263.51157458496095], [21, 38.0976640625, 96.43471215820313, 265.19535461425784, 277.8237048339844], [21, 38.0976640625, 96.43471215820313, 278.6655948486328, 291.2939450683594], [21, 38.0976640625, 89.88667614746095, 292.9777250976562, 305.6060753173828], [21, 38.0976640625, 99.41109216308594, 307.2898553466797, 319.91820556640624], [21, 38.0976640625, 89.88667614746095, 320.76009558105466, 333.38844580078126], [21, 38.0976640625, 108.93550817871095, 335.07222583007814, 347.7005760498047], [21, 35.71656005859375, 108.93550817871095, 348.5424660644531, 361.1708162841797], [21, 35.71656005859375, 108.93550817871095, 362.8545963134766, 375.4829465332031], [21, 35.71656005859375, 117.86464819335939, 377.1667265625, 389.79507678222654], [21, 35.71656005859375, 117.86464819335939, 391.4788568115234, 404.10720703124997], [21, 35.71656005859375, 86.91029614257813, 404.94909704589844, 417.577447265625], [21, 35.71656005859375, 101.7921961669922, 419.26122729492187, 431.8895775146484], [21, 33.930732055664066, 81.55281213378906, 433.5733575439453, 446.2017077636719], [21, 33.930732055664066, 101.19692016601563, 447.8854877929687, 460.5138380126953], [21, 33.930732055664066, 90.4819521484375, 462.1976180419922, 474.82596826171874], [21, 33.930732055664066, 90.4819521484375, 476.5097482910156, 489.13809851074217]]
2026-08-10 15:36:28,381 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=25, matched=25, pages=1, time=22.3s
2026-08-10 15:36:28,395 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 15:36:28,395 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:LabExam | outputs={"chunks": "6 items, types={'LabReport': 6}", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:36:28,395 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 15:36:28,402 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:28,402 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:36:29,219 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:29,233 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 15:36:29,234 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:36:29,234 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 15:36:29,241 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:29,242 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:36:29,756 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:29,763 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 15:36:29,763 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:36:29,764 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 15:36:29,772 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:29,772 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:36:30,471 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:30,481 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 15:36:30,482 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:36:30,482 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 15:36:30,491 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:30,491 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:36:30,929 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:30,942 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 15:36:30,942 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:36:30,942 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 15:36:30,954 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:36:30,956 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:36:30,956 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:36:30,956 INFO     29 [qwen-vl-text] positions(28): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:36:30,956 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [28]
2026-08-10 15:36:31,338 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:36:31,339 INFO     29 [qwen-vl-text] LLM extraction start, text_len=888
2026-08-10 15:36:31,339 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:31,339 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 64, \"bbox_end\": 91, \"encounter_dates\": [\"2025-09-09\", \"2025-09-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院证明书\n(医院保存联)\n姓名：\n性别：男\n年龄：38岁\n入院时间：2025-09-09 10:41\n住院证字\n号\n出院时间：2025-09-12\n病人单位或住址：\n出院诊断：1.右肺上叶腺癌cT4N1M1c IVB期（伴多发骨、肝脏、脑转移） 2.肝继发恶性肿瘤？ 3.\n多发骨继发恶性肿瘤？ 4.中脑继发恶性肿瘤？ 5.癌性疼痛\n诊疗小结：患者因“咳嗽3+月，发现右上肺占位10+天”入院。辅助检查：2025-09-01 [*胸部,增\n强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右\n肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸\n膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧\n部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨\n折可能。2025-09-11 [*头部,MRI平扫] [头部,DWI],1、中脑内异常信号影，占位性病变？脱髓鞘病\n变？缺血灶？其它？2、扫及右侧上颌窦囊肿可能。请结合临床及其它检查。2025-09-01 CYFRA21-1\n+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞\n角蛋白19片段测定 62.83(ng/ml)↑；2025-09-09 血常规(五分类):白细胞计数 10.51(10^9/L)↑，\n中性粒细胞百分率 80.40(%)↑，中性粒细胞计数 8.45(10^9/L)↑。心电图：1.窦性心律 2.电轴左\n偏。\n诊疗经过：[入院后完善相关辅助检查，于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病\n理科腺癌可能性大，报告未回，现患者要求院外等待结果，予以办理出院。]\n治疗结果：好转\n出院医嘱及建议：1、注意休息，避免受凉感冒及劳累；2、院外追踪免疫组化结果，待结果回示后\n及时呼吸内科门诊就诊；3、呼吸科、肿瘤科门诊随访，如有不适，请及时就医。",
    "role": "user"
  }
]
2026-08-10 15:36:39,261 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:39,261 INFO     29 [qwen-vl-text] LLM output (len=1867):
{
  "encounter_date": "2025-09-12",
  "admission_date": "2025-09-09",
  "discharge_date": "2025-09-12",
  "hospital_days": 3,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者因“咳嗽3+月，发现右上肺占位10+天”入院。",
  "admission_diagnoses": [],
  "treatment_summary": "[入院后完善相关辅助检查，于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病理科腺癌可能性大，报告未回，现患者要求院外等待结果，予以办理出院。]",
  "auxiliary_exams": "2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；2025-09-09 血常规(五分类):白细胞计数 10.51(10^9/L)↑，中性粒细胞百分率 80.40(%)↑，中性粒细胞计数 8.45(10^9/L)↑。心电图：1.窦性心律 2.电轴左偏。",
  "imaging_findings": "2025-09-01 [*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。2025-09-11 [*头部,MRI平扫] [头部,DWI],1、中脑内异常信号影，占位性病变？脱髓鞘病变？缺血灶？其它？2、扫及右侧上颌窦囊肿可能。请结合临床及其它检查。",
  "discharge_diagnoses": [
    {
      "name": "右肺上叶腺癌cT4N1M1c IVB期（伴多发骨、肝脏、脑转移）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝继发恶性肿瘤？",
      "diagnosis_type": "西医"
    },
    {
      "name": "多发骨继发恶性肿瘤？",
      "diagnosis_type": "西医"
    },
    {
      "name": "中脑继发恶性肿瘤？",
      "diagnosis_type": "西医"
    },
    {
      "name": "癌性疼痛",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": null,
  "outcome": "好转",
  "discharge_orders": "1、注意休息，避免受凉感冒及劳累；2、院外追踪免疫组化结果，待结果回示后及时呼吸内科门诊就诊；3、呼吸科、肿瘤科门诊随访，如有不适，请及时就医。",
  "do_medications": [],
  "do_follow_up": "呼吸科、肿瘤科门诊随访，如有不适，请及时就医。",
  "do_precautions": [
    "注意休息，避免受凉感冒及劳累",
    "院外追踪免疫组化结果，待结果回示后及时呼吸内科门诊就诊"
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
2026-08-10 15:36:39,261 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-12]
2026-08-10 15:36:39,277 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7097723, prompt_len=1585
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["出院证明书", "(医院保存联)", "姓名：", "性别：男", "年龄：38岁", "入院时间：2025-09-09 10:41", "住院证字", "号", "出院时间：2025-09-12", "病人单位或住址：", "出院诊断：1.右肺上叶腺癌cT4N1M1c IVB期（伴多发骨、肝脏、脑转移） 2.肝继发恶性肿瘤？ 3.", "多发骨继发恶性肿瘤？ 4.中脑继发恶性肿瘤？ 5.癌性疼痛", "诊疗小结：患者因“咳嗽3+月，发现右上肺占位10+天”入院。辅助检查：2025-09-01 [*胸部,增", "强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右", "肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸", "膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧", "部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨", "折可能。2025-09-11 [*头部,MRI平扫] [头部,DWI],1、中脑内异常信号影，占位性病变？脱髓鞘病", "变？缺血灶？其它？2、扫及右侧上颌窦囊肿可能。请结合临床及其它检查。2025-09-01 CYFRA21-1", "+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞", "角蛋白19片段测定 62.83(ng/ml)↑；2025-09-09 血常规(五分类):白细胞计数 10.51(10^9/L)↑，", "中性粒细胞百分率 80.40(%)↑，中性粒细胞计数 8.45(10^9/L)↑。心电图：1.窦性心律 2.电轴左", "偏。", "诊疗经过：[入院后完善相关辅助检查，于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病", "理科腺癌可能性大，报告未回，现患者要求院外等待结果，予以办理出院。]", "治疗结果：好转", "出院医嘱及建议：1、注意休息，避免受凉感冒及劳累；2、院外追踪免疫组化结果，待结果回示后", "及时呼吸内科门诊就诊；3、呼吸科、肿瘤科门诊随访，如有不适，请及时就医。"]

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
2026-08-10 15:36:53,002 INFO     29 [qwen-vl-text] coord API raw response (len=2129):
[
  {"text": "出院证明书", "bbox": [432, 143, 577, 159]},
  {"text": "(医院保存联)", "bbox": [36, 194, 159, 212]},
  {"text": "姓名：", "bbox": [34, 224, 100, 242]},
  {"text": "性别：男", "bbox": [164, 225, 247, 244]},
  {"text": "年龄：38岁", "bbox": [267, 226, 378, 244]},
  {"text": "入院时间：2025-09-09 10:41", "bbox": [389, 228, 669, 245]},
  {"text": "住院证字", "bbox": [545, 197, 631, 215]},
  {"text": "号", "bbox": [748, 197, 768, 214]},
  {"text": "出院时间：2025-09-12", "bbox": [468, 257, 687, 275]},
  {"text": "病人单位或住址：", "bbox": [36, 284, 214, 302]},
  {"text": "出院诊断：1.右肺上叶腺癌cT4N1M1c IVB期（伴多发骨、肝脏、脑转移） 2.肝继发恶性肿瘤？ 3.", "bbox": [38, 314, 947, 335]},
  {"text": "多发骨继发恶性肿瘤？ 4.中脑继发恶性肿瘤？ 5.癌性疼痛", "bbox": [38, 343, 586, 363]},
  {"text": "诊疗小结：患者因“咳嗽3+月，发现右上肺占位10+天”入院。辅助检查：2025-09-01 [*胸部,增", "bbox": [38, 372, 938, 392]},
  {"text": "强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右", "bbox": [40, 401, 951, 421]},
  {"text": "肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸", "bbox": [41, 430, 961, 450]},
  {"text": "膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧", "bbox": [41, 458, 959, 478]},
  {"text": "部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨", "bbox": [42, 487, 958, 507]},
  {"text": "折可能。2025-09-11 [*头部,MRI平扫] [头部,DWI],1、中脑内异常信号影，占位性病变？脱髓鞘病", "bbox": [43, 515, 947, 535]},
  {"text": "变？缺血灶？其它？2、扫及右侧上颌窦囊肿可能。请结合临床及其它检查。2025-09-01 CYFRA21-1", "bbox": [44, 544, 955, 563]},
  {"text": "+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞", "bbox": [45, 572, 945, 591]},
  {"text": "角蛋白19片段测定 62.83(ng/ml)↑；2025-09-09 血常规(五分类):白细胞计数 10.51(10^9/L)↑，", "bbox": [45, 600, 941, 620]},
  {"text": "中性粒细胞百分率 80.40(%)↑，中性粒细胞计数 8.45(10^9/L)↑。心电图：1.窦性心律 2.电轴左", "bbox": [47, 628, 943, 648]},
  {"text": "偏。", "bbox": [47, 657, 80, 674]},
  {"text": "诊疗经过：[入院后完善相关辅助检查，于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病", "bbox": [47, 683, 948, 703]},
  {"text": "理科腺癌可能性大，报告未回，现患者要求院外等待结果，予以办理出院。]", "bbox": [48, 711, 733, 730]},
  {"text": "治疗结果：好转", "bbox": [48, 739, 200, 757]},
  {"text": "出院医嘱及建议：1、注意休息，避免受凉感冒及劳累；2、院外追踪免疫组化结果，待结果回示后", "bbox": [49, 767, 939, 786]},
  {"text": "及时呼吸内科门诊就诊；3、呼吸科、肿瘤科门诊随访，如有不适，请及时就医。", "bbox": [50, 794, 764, 813]}
]
2026-08-10 15:36:53,002 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=13.7s
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[0]: text=出院证明书, bbox=[432, 143, 577, 159]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[1]: text=(医院保存联), bbox=[36, 194, 159, 212]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[34, 224, 100, 242]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[164, 225, 247, 244]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：38岁, bbox=[267, 226, 378, 244]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[5]: text=入院时间：2025-09-09 10:41, bbox=[389, 228, 669, 245]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[6]: text=住院证字, bbox=[545, 197, 631, 215]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[7]: text=号, bbox=[748, 197, 768, 214]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[8]: text=出院时间：2025-09-12, bbox=[468, 257, 687, 275]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[9]: text=病人单位或住址：, bbox=[36, 284, 214, 302]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[10]: text=出院诊断：1.右肺上叶腺癌cT4N1M1c IVB期（伴多发骨、肝脏、脑转移） 2.肝继发恶性肿瘤？ 3., bbox=[38, 314, 947, 335]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[11]: text=多发骨继发恶性肿瘤？ 4.中脑继发恶性肿瘤？ 5.癌性疼痛, bbox=[38, 343, 586, 363]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[12]: text=诊疗小结：患者因“咳嗽3+月，发现右上肺占位10+天”入院。辅助检查：2025-09-01 [*胸部,增, bbox=[38, 372, 938, 392]
2026-08-10 15:36:53,003 INFO     29 [qwen-vl-text] coord item[13]: text=强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右, bbox=[40, 401, 951, 421]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[14]: text=肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸, bbox=[41, 430, 961, 450]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[15]: text=膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧, bbox=[41, 458, 959, 478]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[16]: text=部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨, bbox=[42, 487, 958, 507]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[17]: text=折可能。2025-09-11 [*头部,MRI平扫] [头部,DWI],1、中脑内异常信号影，占位性病变？脱髓鞘病, bbox=[43, 515, 947, 535]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[18]: text=变？缺血灶？其它？2、扫及右侧上颌窦囊肿可能。请结合临床及其它检查。2025-09-01 CYFRA21-1, bbox=[44, 544, 955, 563]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[19]: text=+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞, bbox=[45, 572, 945, 591]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[20]: text=角蛋白19片段测定 62.83(ng/ml)↑；2025-09-09 血常规(五分类):白细胞计数 10.51(10^9/L)↑，, bbox=[45, 600, 941, 620]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[21]: text=中性粒细胞百分率 80.40(%)↑，中性粒细胞计数 8.45(10^9/L)↑。心电图：1.窦性心律 2.电轴左, bbox=[47, 628, 943, 648]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[22]: text=偏。, bbox=[47, 657, 80, 674]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[23]: text=诊疗经过：[入院后完善相关辅助检查，于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病, bbox=[47, 683, 948, 703]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[24]: text=理科腺癌可能性大，报告未回，现患者要求院外等待结果，予以办理出院。], bbox=[48, 711, 733, 730]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[25]: text=治疗结果：好转, bbox=[48, 739, 200, 757]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[26]: text=出院医嘱及建议：1、注意休息，避免受凉感冒及劳累；2、院外追踪免疫组化结果，待结果回示后, bbox=[49, 767, 939, 786]
2026-08-10 15:36:53,004 INFO     29 [qwen-vl-text] coord item[27]: text=及时呼吸内科门诊就诊；3、呼吸科、肿瘤科门诊随访，如有不适，请及时就医。, bbox=[50, 794, 764, 813]
2026-08-10 15:36:53,007 INFO     29 [qwen-vl-text] page=2 — 28/28 coords, api_time=13.7s
2026-08-10 15:36:53,007 INFO     29 [qwen-vl-text] new_positions (28):
[[2, 257.159232421875, 343.47425256347657, 120.39027209472655, 133.86051232910157], [2, 21.429936035156253, 94.64888415527344, 163.32666284179686, 178.48068310546876], [2, 20.239384033203127, 59.527600097656254, 188.58336328125, 203.73738354492187], [2, 97.62526416015625, 147.03317224121093, 189.42525329589844, 205.42116357421875], [2, 158.9386922607422, 225.01432836914063, 190.26714331054689, 205.42116357421875], [2, 231.5623643798828, 398.23964465332034, 191.95092333984374, 206.2630535888672], [2, 324.42542053222655, 375.61915661621094, 165.8523328857422, 181.00635314941405], [2, 445.26644873046877, 457.17196875, 165.8523328857422, 180.1644631347656], [2, 278.58916845703123, 408.9546126708984, 216.36573376464844, 231.5197540283203], [2, 21.429936035156253, 127.38906420898438, 239.09676416015625, 254.25078442382812], [2, 22.620488037109375, 563.7263729248048, 264.35346459960937, 282.03315490722656], [2, 22.620488037109375, 348.83173657226564, 288.76827502441404, 305.6060753173828], [2, 22.620488037109375, 558.3688889160156, 313.18308544921877, 330.0208857421875], [2, 23.8110400390625, 566.107476928711, 337.59789587402344, 354.43569616699216], [2, 24.406316040039062, 572.0602369384766, 362.0127062988281, 378.8505065917969], [2, 24.406316040039062, 570.8696849365234, 385.58562670898436, 402.42342700195314], [2, 25.001592041015627, 570.274408935547, 410.00043713378903, 426.8382374267578], [2, 25.596868041992188, 563.7263729248048, 433.5733575439453, 450.4111578369141], [2, 26.19214404296875, 568.4885809326172, 457.98816796875, 473.98407824707033], [2, 26.787420043945314, 562.5358209228516, 481.5610883789062, 497.55699865722653], [2, 26.787420043945314, 560.1547169189454, 505.1340087890625, 521.9718090820312], [2, 27.97797204589844, 561.3452689208984, 528.7069291992187, 545.5447294921875], [2, 27.97797204589844, 47.622080078125, 553.1217396240235, 567.4338698730469], [2, 27.97797204589844, 564.3216489257812, 575.0108800048828, 591.8486802978515], [2, 28.573248046875, 436.3373087158203, 598.583800415039, 614.5797106933594], [2, 28.573248046875, 119.05520019531251, 622.1567208251953, 637.3107410888672], [2, 29.168524047851562, 558.9641649169922, 645.7296412353516, 661.7255515136719], [2, 29.763800048828127, 454.79086474609375, 668.4606716308593, 684.4565819091797]]
2026-08-10 15:36:53,007 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=22.1s
2026-08-10 15:36:53,008 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:36:53,009 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:36:53,009 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:36:53,009 INFO     29 [qwen-vl-text] positions(36): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:36:53,010 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [36]
2026-08-10 15:36:53,300 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:36:53,301 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1273
2026-08-10 15:36:53,301 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:36:53,301 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 482, \"bbox_end\": 517, \"encounter_dates\": [\"2025-12-04\", \"2025-12-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院证明书\n(医院保存联)\n住院证字\n号\n姓名\n年龄：38岁 入院时间：2025-12-04 09:00\n科\n床号：029 出院时间：2025-12-07\n病人单位或住址\n出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR\nL858R+）3.恶性肿瘤靶向治疗 4.肝继发恶性肿瘤 5.骨继发恶性肿瘤 6.化疗相关恶心和呕吐 7.\n化疗后骨髓抑制 8.轻度贫血\n诊疗小结：患者因“发现右肺上叶占位5+月，右肺上叶腺癌靶向治疗中。”入院。入院查体：\nT36.5℃，P75次/分，R20次/分，BP127/82mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语\n颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣\n膜区未闻及病理性杂音。]辅助检查：暂缺。\n诊疗经过：[入院完善相关检查2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋\n白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌\n素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。2025-12-04 胸腹部增\n强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较\n大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较\nCT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中\n叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边\n缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它\n病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约\n1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右\n肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前\n列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂\n骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理\n性骨折待排。病情评价好转，给于唑来磷酸预防骨相关事件。排除化疗禁忌于2025-12-5行第1周期AC\n方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼 110mg\nqd，化疗中给于抑酸、护胃、止吐等对症治疗，化疗顺利，患者无明显不适。化疗后复查血常规提\n示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。]\n治疗结果：好转\n出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就\n第1页/共2页",
    "role": "user"
  }
]
2026-08-10 15:36:53,303 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:36:53.303+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:37:07,789 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:37:07,789 INFO     29 [qwen-vl-text] LLM output (len=2994):
{
  "encounter_date": "2025-12-07",
  "admission_date": "2025-12-04",
  "discharge_date": "2025-12-07",
  "hospital_days": 3,
  "department": null,
  "bed_number": "029",
  "admission_condition": "T36.5℃，P75次/分，R20次/分，BP127/82mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。]",
  "admission_diagnoses": [],
  "treatment_summary": "入院完善相关检查2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。2025-12-04 胸腹部增强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。病情评价好转，给于唑来磷酸预防骨相关事件。排除化疗禁忌于2025-12-5行第1周期AC方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼 110mg qd，化疗中给于抑酸、护胃、止吐等对症治疗，化疗顺利，患者无明显不适。化疗后复查血常规提示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。",
  "auxiliary_exams": "2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。",
  "imaging_findings": "2025-12-04 胸腹部增强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。",
  "discharge_diagnoses": [
    {
      "name": "恶性肿瘤化学治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶向治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "骨继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗相关恶心和呕吐",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗后骨髓抑制",
      "diagnosis_type": "西医"
    },
    {
      "name": "轻度贫血",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "化疗顺利，患者无明显不适。化疗后复查血常规提示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。",
  "outcome": "好转",
  "discharge_orders": "1、每周复查血常规，每2周复查肝肾功，如有异常，及时就",
  "do_medications": [],
  "do_follow_up": null,
  "do_precautions": [
    "每周复查血常规",
    "每2周复查肝肾功",
    "如有异常，及时就"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": 1,
  "body_surface_area": null,
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 75,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 127,
  "vs_diastolic_bp_mmhg": 82
}
2026-08-10 15:37:07,789 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-07]
2026-08-10 15:37:07,793 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2234552, prompt_len=1994
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["出院证明书", "(医院保存联)", "住院证字", "号", "姓名", "年龄：38岁 入院时间：2025-12-04 09:00", "科", "床号：029 出院时间：2025-12-07", "病人单位或住址", "出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR", "L858R+）3.恶性肿瘤靶向治疗 4.肝继发恶性肿瘤 5.骨继发恶性肿瘤 6.化疗相关恶心和呕吐 7.", "化疗后骨髓抑制 8.轻度贫血", "诊疗小结：患者因“发现右肺上叶占位5+月，右肺上叶腺癌靶向治疗中。”入院。入院查体：", "T36.5℃，P75次/分，R20次/分，BP127/82mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语", "颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣", "膜区未闻及病理性杂音。]辅助检查：暂缺。", "诊疗经过：[入院完善相关检查2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋", "白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌", "素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。2025-12-04 胸腹部增", "强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较", "大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较", "CT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中", "叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边", "缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它", "病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约", "1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右", "肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前", "列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂", "骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理", "性骨折待排。病情评价好转，给于唑来磷酸预防骨相关事件。排除化疗禁忌于2025-12-5行第1周期AC", "方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼 110mg", "qd，化疗中给于抑酸、护胃、止吐等对症治疗，化疗顺利，患者无明显不适。化疗后复查血常规提", "示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。]", "治疗结果：好转", "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "第1页/共2页"]

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
2026-08-10 15:37:25,253 INFO     29 [qwen-vl-text] coord API raw response (len=2828):
[
	{"text": "出院证明书", "bbox": [423, 53, 550, 74]},
	{"text": "(医院保存联)", "bbox": [77, 113, 182, 130]},
	{"text": "住院证字", "bbox": [527, 110, 603, 126]},
	{"text": "号", "bbox": [708, 110, 726, 126]},
	{"text": "姓名", "bbox": [78, 141, 114, 157]},
	{"text": "年龄：38岁 入院时间：2025-12-04 09:00", "bbox": [273, 138, 624, 154]},
	{"text": "科", "bbox": [80, 168, 100, 184]},
	{"text": "床号：029 出院时间：2025-12-07", "bbox": [227, 166, 519, 181]},
	{"text": "病人单位或住址", "bbox": [82, 193, 208, 209]},
	{"text": "出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR", "bbox": [85, 217, 846, 234]},
	{"text": "L858R+）3.恶性肿瘤靶向治疗 4.肝继发恶性肿瘤 5.骨继发恶性肿瘤 6.化疗相关恶心和呕吐 7.", "bbox": [85, 243, 896, 260]},
	{"text": "化疗后骨髓抑制 8.轻度贫血", "bbox": [86, 270, 323, 285]},
	{"text": "诊疗小结：患者因“发现右肺上叶占位5+月，右肺上叶腺癌靶向治疗中。”入院。入院查体：", "bbox": [85, 295, 832, 310]},
	{"text": "T36.5℃，P75次/分，R20次/分，BP127/82mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语", "bbox": [84, 320, 898, 336]},
	{"text": "颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣", "bbox": [82, 345, 898, 361]},
	{"text": "膜区未闻及病理性杂音。]辅助检查：暂缺。", "bbox": [80, 369, 435, 385]},
	{"text": "诊疗经过：[入院完善相关检查2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋", "bbox": [78, 394, 883, 410]},
	{"text": "白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌", "bbox": [77, 419, 891, 435]},
	{"text": "素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。2025-12-04 胸腹部增", "bbox": [75, 444, 901, 460]},
	{"text": "强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较", "bbox": [74, 469, 894, 485]},
	{"text": "大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较", "bbox": [73, 494, 807, 510]},
	{"text": "CT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中", "bbox": [71, 520, 893, 536]},
	{"text": "叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边", "bbox": [70, 545, 903, 561]},
	{"text": "缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它", "bbox": [70, 570, 903, 587]},
	{"text": "病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约", "bbox": [70, 596, 856, 612]},
	{"text": "1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右", "bbox": [70, 622, 894, 638]},
	{"text": "肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前", "bbox": [70, 648, 903, 664]},
	{"text": "列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂", "bbox": [70, 674, 885, 690]},
	{"text": "骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理", "bbox": [70, 700, 903, 717]},
	{"text": "性骨折待排。病情评价好转，给于唑来磷酸预防骨相关事件。排除化疗禁忌于2025-12-5行第1周期AC", "bbox": [70, 727, 905, 743]},
	{"text": "方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼 110mg", "bbox": [68, 753, 908, 770]},
	{"text": "qd，化疗中给于抑酸、护胃、止吐等对症治疗，化疗顺利，患者无明显不适。化疗后复查血常规提", "bbox": [74, 780, 903, 797]},
	{"text": "示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。]", "bbox": [63, 811, 577, 829]},
	{"text": "治疗结果：好转", "bbox": [60, 840, 196, 857]},
	{"text": "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "bbox": [57, 868, 892, 887]},
	{"text": "第1页/共2页", "bbox": [420, 900, 570, 916]}
]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=17.5s
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[0]: text=出院证明书, bbox=[423, 53, 550, 74]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[1]: text=(医院保存联), bbox=[77, 113, 182, 130]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[2]: text=住院证字, bbox=[527, 110, 603, 126]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[3]: text=号, bbox=[708, 110, 726, 126]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[78, 141, 114, 157]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：38岁 入院时间：2025-12-04 09:00, bbox=[273, 138, 624, 154]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[6]: text=科, bbox=[80, 168, 100, 184]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[7]: text=床号：029 出院时间：2025-12-07, bbox=[227, 166, 519, 181]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[8]: text=病人单位或住址, bbox=[82, 193, 208, 209]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[9]: text=出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR, bbox=[85, 217, 846, 234]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[10]: text=L858R+）3.恶性肿瘤靶向治疗 4.肝继发恶性肿瘤 5.骨继发恶性肿瘤 6.化疗相关恶心和呕吐 7., bbox=[85, 243, 896, 260]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[11]: text=化疗后骨髓抑制 8.轻度贫血, bbox=[86, 270, 323, 285]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[12]: text=诊疗小结：患者因“发现右肺上叶占位5+月，右肺上叶腺癌靶向治疗中。”入院。入院查体：, bbox=[85, 295, 832, 310]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[13]: text=T36.5℃，P75次/分，R20次/分，BP127/82mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语, bbox=[84, 320, 898, 336]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[14]: text=颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣, bbox=[82, 345, 898, 361]
2026-08-10 15:37:25,254 INFO     29 [qwen-vl-text] coord item[15]: text=膜区未闻及病理性杂音。]辅助检查：暂缺。, bbox=[80, 369, 435, 385]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[16]: text=诊疗经过：[入院完善相关检查2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋, bbox=[78, 394, 883, 410]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[17]: text=白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌, bbox=[77, 419, 891, 435]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[18]: text=素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。2025-12-04 胸腹部增, bbox=[75, 444, 901, 460]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[19]: text=强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较, bbox=[74, 469, 894, 485]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[20]: text=大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较, bbox=[73, 494, 807, 510]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[21]: text=CT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中, bbox=[71, 520, 893, 536]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[22]: text=叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边, bbox=[70, 545, 903, 561]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[23]: text=缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它, bbox=[70, 570, 903, 587]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[24]: text=病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约, bbox=[70, 596, 856, 612]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[25]: text=1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右, bbox=[70, 622, 894, 638]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[26]: text=肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前, bbox=[70, 648, 903, 664]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[27]: text=列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂, bbox=[70, 674, 885, 690]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[28]: text=骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理, bbox=[70, 700, 903, 717]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[29]: text=性骨折待排。病情评价好转，给于唑来磷酸预防骨相关事件。排除化疗禁忌于2025-12-5行第1周期AC, bbox=[70, 727, 905, 743]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[30]: text=方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼 110mg, bbox=[68, 753, 908, 770]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[31]: text=qd，化疗中给于抑酸、护胃、止吐等对症治疗，化疗顺利，患者无明显不适。化疗后复查血常规提, bbox=[74, 780, 903, 797]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[32]: text=示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。], bbox=[63, 811, 577, 829]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[33]: text=治疗结果：好转, bbox=[60, 840, 196, 857]
2026-08-10 15:37:25,255 INFO     29 [qwen-vl-text] coord item[34]: text=出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就, bbox=[57, 868, 892, 887]
2026-08-10 15:37:25,256 INFO     29 [qwen-vl-text] coord item[35]: text=第1页/共2页, bbox=[420, 900, 570, 916]
2026-08-10 15:37:25,256 INFO     29 [qwen-vl-text] page=8 — 36/36 coords, api_time=17.5s
2026-08-10 15:37:25,256 INFO     29 [qwen-vl-text] new_positions (36):
[[8, 251.80174841308596, 327.4018005371094, 44.62017077636719, 62.299861083984375], [8, 45.83625207519531, 108.34023217773438, 95.13357165527344, 109.44570190429687], [8, 313.71045251464847, 358.9514285888672, 92.60790161132812, 106.07814184570313], [8, 421.45540869140626, 432.1703767089844, 92.60790161132812, 106.07814184570313], [8, 46.43152807617188, 67.86146411132813, 118.70649206542969, 132.17673229980468], [8, 162.51034826660157, 371.45222460937504, 116.18082202148437, 129.6510622558594], [8, 47.622080078125, 59.527600097656254, 141.4375224609375, 154.9077626953125], [8, 135.12765222167968, 308.948244506836, 139.75374243164063, 152.38209265136717], [8, 48.812632080078124, 123.81740820312501, 162.48477282714845, 175.95501306152343], [8, 50.598460083007815, 503.6034968261719, 182.69013317871094, 197.00226342773436], [8, 50.598460083007815, 533.367296875, 204.5792735595703, 218.89140380859374], [8, 51.193736083984376, 192.2741483154297, 227.31030395507813, 239.9386541748047], [8, 50.598460083007815, 495.26963281250005, 248.35755432128906, 260.9859045410156], [8, 50.003184082031254, 534.5578488769531, 269.4048046875, 282.875044921875], [8, 48.812632080078124, 534.5578488769531, 290.4520550537109, 303.92229528808593], [8, 47.622080078125, 258.9450604248047, 310.6574154052734, 324.1276556396484], [8, 46.43152807617188, 525.6287088623047, 331.7046657714844, 345.1749060058594], [8, 45.83625207519531, 530.3909168701172, 352.75191613769533, 366.2221563720703], [8, 44.64570007324219, 536.3436768798829, 373.79916650390624, 387.26940673828125], [8, 44.05042407226563, 532.1767448730469, 394.8464168701172, 408.3166571044922], [8, 43.45514807128907, 480.38773278808594, 415.8936672363281, 429.3639074707031], [8, 42.26459606933594, 531.5814688720703, 437.7828076171875, 451.2530478515625], [8, 41.669320068359376, 537.5342288818359, 458.83005798339843, 472.30029821777345], [8, 41.669320068359376, 537.5342288818359, 479.8773083496094, 494.1894385986328], [8, 41.669320068359376, 509.5562568359375, 501.76644873046877, 515.2366889648438], [8, 41.669320068359376, 532.1767448730469, 523.6555891113281, 537.1258293457031], [8, 41.669320068359376, 537.5342288818359, 545.5447294921875, 559.0149697265625], [8, 41.669320068359376, 526.8192608642578, 567.4338698730469, 580.9041101074218], [8, 41.669320068359376, 537.5342288818359, 589.3230102539062, 603.6351405029296], [8, 41.669320068359376, 538.7247808837891, 612.0540406494141, 625.5242808837891], [8, 40.47876806640625, 540.5106088867187, 633.9431810302734, 648.2553112792968], [8, 44.05042407226563, 537.5342288818359, 656.6742114257812, 670.9863416748046], [8, 37.50238806152344, 343.47425256347657, 682.7728018798828, 697.9268221435547], [8, 35.71656005859375, 116.67409619140625, 707.1876123046875, 721.4997425537109], [8, 33.930732055664066, 530.9861928710937, 730.7605327148437, 746.756442993164], [8, 250.01592041015627, 339.30732055664066, 757.7010131835938, 771.1712534179687]]
2026-08-10 15:37:25,256 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=1, time=32.2s
2026-08-10 15:37:25,256 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:37:25,258 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:37:25,258 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:37:25,258 INFO     29 [qwen-vl-text] positions(32): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:37:25,258 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [32]
2026-08-10 15:37:25,592 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:37:25,594 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1017
2026-08-10 15:37:25,594 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:37:25,594 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 518, \"bbox_end\": 549, \"encounter_dates\": [\"2025-12-29\", \"2025-12-31\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院证明书\n(医院保存联)\n住院证字\n号\n性别：男 年龄：39岁 入院时间：2025-12-29 09:54\n床号： 出院时间：2025-12-31\n病人单位或住址\n出院诊断：1.姑息性化疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）\n3.肝继发恶性肿瘤 4.骨继发恶性肿瘤 5.化疗相关性恶心和呕吐 6.化疗相关性吞咽困难 7.肝功\n能不全\n诊疗小结：患者因“发现右肺上叶占位6+月，右肺上叶腺癌1周期化疗后20+天。”入院。入院查\n体：T36.7℃；P85次/分；R18次/分；BP117/81mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺\n语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各\n瓣膜区未闻及病理性杂音。\n诊疗经过：患者入院后完善相关检查，2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，\n中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；\n2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急\n诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬\n氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。患者无化疗禁忌，于2025-12-30行第2周期AC方案化\n疗，具体方案为：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w，同时给予患者抑酸护胃、止\n痛等对症支持治疗，今日安排患者出院。\n治疗结果：好转\n出院医嘱及建议：1、注意休息，加强营养；2、每周复查血常规2次、肝肾功1次，如有异常，立即\n就诊。3、下周期化疗时间：2026-01-20，住院前请提前联系床位。4、出院用药：利可君片 1片 口\n服 每天3次，生血宝合剂 15ml 口服 每天3次。5、\n午\n6、我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午。\n备注（包括手术名称）：[手术记录手术名称]\n时间：2025年12月31日\n说明：1、此证明书未经我院加盖公章无效。 2、涂改未经加盖我院公章无效。\n3、此证明仅证明病人出院时病情。 4、请妥善保管，遗失不补。\n第1页/共2页",
    "role": "user"
  }
]
2026-08-10 15:37:25,596 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:37:25.595+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:37:36,271 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:37:36,271 INFO     29 [qwen-vl-text] LLM output (len=2336):
{
  "encounter_date": "2025-12-31",
  "admission_date": "2025-12-29",
  "discharge_date": "2025-12-31",
  "hospital_days": 2,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者因“发现右肺上叶占位6+月，右肺上叶腺癌1周期化疗后20+天。”入院。入院查体：T36.7℃；P85次/分；R18次/分；BP117/81mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。",
  "admission_diagnoses": [],
  "treatment_summary": "患者入院后完善相关检查，2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。患者无化疗禁忌，于2025-12-30行第2周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w，同时给予患者抑酸护胃、止痛等对症支持治疗，今日安排患者出院。",
  "auxiliary_exams": "2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。",
  "imaging_findings": null,
  "discharge_diagnoses": [
    {
      "name": "姑息性化疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "骨继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗相关性恶心和呕吐",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗相关性吞咽困难",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝功能不全",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": null,
  "outcome": "好转",
  "discharge_orders": "1、注意休息，加强营养；2、每周复查血常规2次、肝肾功1次，如有异常，立即就诊。3、下周期化疗时间：2026-01-20，住院前请提前联系床位。4、出院用药：利可君片 1片 口服 每天3次，生血宝合剂 15ml 口服 每天3次。5、午 6、我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午。",
  "do_medications": [
    "利可君片 1片 口服 每天3次",
    "生血宝合剂 15ml 口服 每天3次"
  ],
  "do_follow_up": "每周复查血常规2次、肝肾功1次，如有异常，立即就诊。",
  "do_precautions": [
    "注意休息，加强营养",
    "如有异常，立即就诊",
    "住院前请提前联系床位",
    "我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午"
  ],
  "next_treatment_date": "2026-01-20",
  "attending_physician": null,
  "pe_ecog_score": 1,
  "body_surface_area": null,
  "vs_temperature_c": 36.7,
  "vs_pulse_bpm": 85,
  "vs_respiration_rpm": 18,
  "vs_systolic_bp_mmhg": 117,
  "vs_diastolic_bp_mmhg": 81
}
2026-08-10 15:37:36,272 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-31]
2026-08-10 15:37:36,280 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2124882, prompt_len=1726
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["出院证明书", "(医院保存联)", "住院证字", "号", "性别：男 年龄：39岁 入院时间：2025-12-29 09:54", "床号： 出院时间：2025-12-31", "病人单位或住址", "出院诊断：1.姑息性化疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）", "3.肝继发恶性肿瘤 4.骨继发恶性肿瘤 5.化疗相关性恶心和呕吐 6.化疗相关性吞咽困难 7.肝功", "能不全", "诊疗小结：患者因“发现右肺上叶占位6+月，右肺上叶腺癌1周期化疗后20+天。”入院。入院查", "体：T36.7℃；P85次/分；R18次/分；BP117/81mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺", "语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各", "瓣膜区未闻及病理性杂音。", "诊疗经过：患者入院后完善相关检查，2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，", "中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；", "2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急", "诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬", "氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。患者无化疗禁忌，于2025-12-30行第2周期AC方案化", "疗，具体方案为：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w，同时给予患者抑酸护胃、止", "痛等对症支持治疗，今日安排患者出院。", "治疗结果：好转", "出院医嘱及建议：1、注意休息，加强营养；2、每周复查血常规2次、肝肾功1次，如有异常，立即", "就诊。3、下周期化疗时间：2026-01-20，住院前请提前联系床位。4、出院用药：利可君片 1片 口", "服 每天3次，生血宝合剂 15ml 口服 每天3次。5、", "午", "6、我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午。", "备注（包括手术名称）：[手术记录手术名称]", "时间：2025年12月31日", "说明：1、此证明书未经我院加盖公章无效。 2、涂改未经加盖我院公章无效。", "3、此证明仅证明病人出院时病情。 4、请妥善保管，遗失不补。", "第1页/共2页"]

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
2026-08-10 15:37:50,200 INFO     29 [qwen-vl-text] coord API raw response (len=2401):
[
	{"text": "出院证明书", "bbox": [447, 36, 584, 60]},
	{"text": "(医院保存联)", "bbox": [70, 96, 184, 113]},
	{"text": "住院证字", "bbox": [557, 100, 640, 116]},
	{"text": "号", "bbox": [752, 102, 771, 118]},
	{"text": "性别：男 年龄：39岁 入院时间：2025-12-29 09:54", "bbox": [187, 126, 661, 144]},
	{"text": "床号： 出院时间：2025-12-31", "bbox": [233, 156, 547, 173]},
	{"text": "病人单位或住址", "bbox": [76, 184, 208, 200]},
	{"text": "出院诊断：1.姑息性化疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）", "bbox": [79, 213, 915, 232]},
	{"text": "3.肝继发恶性肿瘤 4.骨继发恶性肿瘤 5.化疗相关性恶心和呕吐 6.化疗相关性吞咽困难 7.肝功", "bbox": [79, 241, 952, 261]},
	{"text": "能不全", "bbox": [80, 268, 138, 284]},
	{"text": "诊疗小结：患者因“发现右肺上叶占位6+月，右肺上叶腺癌1周期化疗后20+天。”入院。入院查", "bbox": [80, 295, 912, 314]},
	{"text": "体：T36.7℃；P85次/分；R18次/分；BP117/81mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺", "bbox": [79, 322, 941, 342]},
	{"text": "语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各", "bbox": [77, 349, 951, 369]},
	{"text": "瓣膜区未闻及病理性杂音。", "bbox": [75, 375, 305, 391]},
	{"text": "诊疗经过：患者入院后完善相关检查，2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，", "bbox": [72, 401, 931, 421]},
	{"text": "中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；", "bbox": [71, 428, 900, 448]},
	{"text": "2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急", "bbox": [68, 455, 952, 476]},
	{"text": "诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬", "bbox": [67, 482, 942, 503]},
	{"text": "氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。患者无化疗禁忌，于2025-12-30行第2周期AC方案化", "bbox": [66, 509, 932, 530]},
	{"text": "疗，具体方案为：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w，同时给予患者抑酸护胃、止", "bbox": [64, 537, 942, 558]},
	{"text": "痛等对症支持治疗，今日安排患者出院。", "bbox": [63, 564, 420, 581]},
	{"text": "治疗结果：好转", "bbox": [62, 592, 206, 609]},
	{"text": "出院医嘱及建议：1、注意休息，加强营养；2、每周复查血常规2次、肝肾功1次，如有异常，立即", "bbox": [62, 620, 931, 640]},
	{"text": "就诊。3、下周期化疗时间：2026-01-20，住院前请提前联系床位。4、出院用药：利可君片 1片 口", "bbox": [61, 648, 938, 668]},
	{"text": "服 每天3次，生血宝合剂 15ml 口服 每天3次。5、", "bbox": [60, 675, 508, 694]},
	{"text": "午", "bbox": [60, 705, 80, 720]},
	{"text": "6、我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午。", "bbox": [323, 734, 920, 752]},
	{"text": "备注（包括手术名称）：[手术记录手术名称]", "bbox": [60, 760, 468, 779]},
	{"text": "时间：2025年12月31日", "bbox": [667, 794, 870, 811]},
	{"text": "说明：1、此证明书未经我院加盖公章无效。 2、涂改未经加盖我院公章无效。", "bbox": [57, 818, 776, 841]},
	{"text": "3、此证明仅证明病人出院时病情。 4、请妥善保管，遗失不补。", "bbox": [113, 848, 736, 871]},
	{"text": "第1页/共2页", "bbox": [430, 945, 591, 966]}
]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=13.9s
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[0]: text=出院证明书, bbox=[447, 36, 584, 60]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[1]: text=(医院保存联), bbox=[70, 96, 184, 113]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[2]: text=住院证字, bbox=[557, 100, 640, 116]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[3]: text=号, bbox=[752, 102, 771, 118]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男 年龄：39岁 入院时间：2025-12-29 09:54, bbox=[187, 126, 661, 144]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[5]: text=床号： 出院时间：2025-12-31, bbox=[233, 156, 547, 173]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[6]: text=病人单位或住址, bbox=[76, 184, 208, 200]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[7]: text=出院诊断：1.姑息性化疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）, bbox=[79, 213, 915, 232]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[8]: text=3.肝继发恶性肿瘤 4.骨继发恶性肿瘤 5.化疗相关性恶心和呕吐 6.化疗相关性吞咽困难 7.肝功, bbox=[79, 241, 952, 261]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[9]: text=能不全, bbox=[80, 268, 138, 284]
2026-08-10 15:37:50,201 INFO     29 [qwen-vl-text] coord item[10]: text=诊疗小结：患者因“发现右肺上叶占位6+月，右肺上叶腺癌1周期化疗后20+天。”入院。入院查, bbox=[80, 295, 912, 314]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[11]: text=体：T36.7℃；P85次/分；R18次/分；BP117/81mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺, bbox=[79, 322, 941, 342]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[12]: text=语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各, bbox=[77, 349, 951, 369]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[13]: text=瓣膜区未闻及病理性杂音。, bbox=[75, 375, 305, 391]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[14]: text=诊疗经过：患者入院后完善相关检查，2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，, bbox=[72, 401, 931, 421]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[15]: text=中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；, bbox=[71, 428, 900, 448]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[16]: text=2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急, bbox=[68, 455, 952, 476]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[17]: text=诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬, bbox=[67, 482, 942, 503]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[18]: text=氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。患者无化疗禁忌，于2025-12-30行第2周期AC方案化, bbox=[66, 509, 932, 530]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[19]: text=疗，具体方案为：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w，同时给予患者抑酸护胃、止, bbox=[64, 537, 942, 558]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[20]: text=痛等对症支持治疗，今日安排患者出院。, bbox=[63, 564, 420, 581]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[21]: text=治疗结果：好转, bbox=[62, 592, 206, 609]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[22]: text=出院医嘱及建议：1、注意休息，加强营养；2、每周复查血常规2次、肝肾功1次，如有异常，立即, bbox=[62, 620, 931, 640]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[23]: text=就诊。3、下周期化疗时间：2026-01-20，住院前请提前联系床位。4、出院用药：利可君片 1片 口, bbox=[61, 648, 938, 668]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[24]: text=服 每天3次，生血宝合剂 15ml 口服 每天3次。5、, bbox=[60, 675, 508, 694]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[25]: text=午, bbox=[60, 705, 80, 720]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[26]: text=6、我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午。, bbox=[323, 734, 920, 752]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[27]: text=备注（包括手术名称）：[手术记录手术名称], bbox=[60, 760, 468, 779]
2026-08-10 15:37:50,202 INFO     29 [qwen-vl-text] coord item[28]: text=时间：2025年12月31日, bbox=[667, 794, 870, 811]
2026-08-10 15:37:50,203 INFO     29 [qwen-vl-text] coord item[29]: text=说明：1、此证明书未经我院加盖公章无效。 2、涂改未经加盖我院公章无效。, bbox=[57, 818, 776, 841]
2026-08-10 15:37:50,203 INFO     29 [qwen-vl-text] coord item[30]: text=3、此证明仅证明病人出院时病情。 4、请妥善保管，遗失不补。, bbox=[113, 848, 736, 871]
2026-08-10 15:37:50,203 INFO     29 [qwen-vl-text] coord item[31]: text=第1页/共2页, bbox=[430, 945, 591, 966]
2026-08-10 15:37:50,204 INFO     29 [qwen-vl-text] page=9 — 32/32 coords, api_time=13.9s
2026-08-10 15:37:50,206 INFO     29 [qwen-vl-text] new_positions (32):
[[9, 266.08837243652346, 347.64118457031253, 30.30804052734375, 50.513400878906246], [9, 41.669320068359376, 109.5307841796875, 80.82144140625, 95.13357165527344], [9, 331.5687325439453, 380.976640625, 84.18900146484376, 97.65924169921875], [9, 447.64755273437504, 458.9577967529297, 85.87278149414063, 99.34302172851562], [9, 111.31661218261719, 393.47743664550785, 106.07814184570313, 121.232162109375], [9, 138.69930822753906, 325.6159725341797, 131.33484228515624, 145.6469725341797], [9, 45.24097607421875, 123.81740820312501, 154.9077626953125, 168.3780029296875], [9, 47.02680407714844, 544.6775408935547, 179.3225731201172, 195.3184833984375], [9, 47.02680407714844, 566.7027529296876, 202.89549353027343, 219.73329382324218], [9, 47.622080078125, 82.14808813476563, 225.62652392578124, 239.09676416015625], [9, 47.622080078125, 542.8917128906251, 248.35755432128906, 264.35346459960937], [9, 47.02680407714844, 560.1547169189454, 271.08858471679684, 287.9263850097656], [9, 45.83625207519531, 566.107476928711, 293.8196151123047, 310.6574154052734], [9, 44.64570007324219, 181.55918029785158, 315.70875549316406, 329.1789957275391], [9, 42.859872070312505, 554.2019569091797, 337.59789587402344, 354.43569616699216], [9, 42.26459606933594, 535.7484008789063, 360.3289262695312, 377.1667265625], [9, 40.47876806640625, 566.7027529296876, 383.05995666503907, 400.73964697265626], [9, 39.88349206542969, 560.7499929199219, 405.79098706054685, 423.47067736816405], [9, 39.288216064453124, 554.7972329101563, 428.5220174560547, 446.2017077636719], [9, 38.0976640625, 560.7499929199219, 452.09493786621096, 469.7746281738281], [9, 37.50238806152344, 250.01592041015627, 474.82596826171874, 489.13809851074217], [9, 36.90711206054688, 122.62685620117188, 498.398888671875, 512.7110189208985], [9, 36.90711206054688, 554.2019569091797, 521.9718090820312, 538.809609375], [9, 36.31183605957031, 558.3688889160156, 545.5447294921875, 562.3825297851563], [9, 35.71656005859375, 302.40020849609374, 568.2757598876954, 584.2716701660156], [9, 35.71656005859375, 47.622080078125, 593.5324603271484, 606.160810546875], [9, 192.2741483154297, 547.6539208984375, 617.9472707519532, 633.101291015625], [9, 35.71656005859375, 278.58916845703123, 639.8364111328125, 655.8323214111329], [9, 397.04909265136723, 517.8901208496094, 668.4606716308593, 682.7728018798828], [9, 33.930732055664066, 461.9341767578125, 688.6660319824218, 708.029502319336], [9, 67.26618811035156, 438.12313671875, 713.922732421875, 733.286202758789], [9, 255.9686804199219, 351.80811657714844, 795.5860638427735, 813.2657541503906]]
2026-08-10 15:37:50,206 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=24.9s
2026-08-10 15:37:50,207 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:37:50,215 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:37:50,215 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:37:50,216 INFO     29 [qwen-vl-text] positions(43): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:37:50,216 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [43]
2026-08-10 15:37:50,551 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:37:50,553 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1340
2026-08-10 15:37:50,553 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:37:50,553 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 550, \"bbox_end\": 592, \"encounter_dates\": [\"2026-01-21\", \"2026-01-24\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院证明书\n(病人保存联)\n住院证字\n号\n姓名：\n性别：男\n年龄：39岁\n入院时间：2026-01-21 10:07\n出院时间：2026-01-24\n病人单位或住址\n出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR\nL858R+）\n3.恶性肿瘤靶向治疗\n4.肝继发恶性肿瘤\n5.骨继发恶性肿瘤\n6.化疗相关恶心和呕吐\n7.化疗后骨髓抑制\n8.白细胞减少\n9.恶性肿瘤的治疗后的随诊检查\n诊疗小结：患者因“发现右肺上叶占位7月，右肺上叶腺癌2周期化疗后20+天。”入院。入院查体：\nT36.6℃，P76次/分，R19次/分，BP113/75mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语\n颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣\n膜区未闻及病理性杂音。]辅助检查：暂缺。\n诊疗经过：[入院完善相关检查：2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红\n蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80\n(U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+\nProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前\n体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。2026-01-22 胸腹部CT：1、“肺CA”复查，右\n肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，\n增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另\n见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺\n下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸\n膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大\n层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增\n粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前\n变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐\n骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。病情评价好转，排除于2026-1-23\n行第3周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w，同时给予\n患者抑酸护胃、止痛等对症支持治疗，现化疗已完成，于今出院回家乡休养。]\n治疗结果：好转\n出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就\n诊。2、下周期治疗时间：2026年2月13日，请提前几天微信群预约床位，入院前尽量保持空腹状\n第1页/共2页",
    "role": "user"
  }
]
2026-08-10 15:37:56,423 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:37:56.421+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:38:08,230 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:38:08,230 INFO     29 [qwen-vl-text] LLM output (len=3213):
{
  "encounter_date": "2026-01-24",
  "admission_date": "2026-01-21",
  "discharge_date": "2026-01-24",
  "hospital_days": 3,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者因“发现右肺上叶占位7月，右肺上叶腺癌2周期化疗后20+天。”入院。入院查体：T36.6℃，P76次/分，R19次/分，BP113/75mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。]",
  "admission_diagnoses": [],
  "treatment_summary": "入院完善相关检查：2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80 (U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+ ProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。2026-01-22 胸腹部CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。病情评价好转，排除于2026-1-23行第3周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w，同时给予患者抑酸护胃、止痛等对症支持治疗，现化疗已完成，于今出院回家乡休养。",
  "auxiliary_exams": "2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80 (U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+ ProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。",
  "imaging_findings": "2026-01-22 胸腹部CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。",
  "discharge_diagnoses": [
    {
      "name": "恶性肿瘤化学治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶向治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "骨继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗相关恶心和呕吐",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗后骨髓抑制",
      "diagnosis_type": "西医"
    },
    {
      "name": "白细胞减少",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤的治疗后的随诊检查",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "化疗已完成，于今出院回家乡休养",
  "outcome": "好转",
  "discharge_orders": "1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。2、下周期治疗时间：2026年2月13日，请提前几天微信群预约床位，入院前尽量保持空腹状",
  "do_medications": [],
  "do_follow_up": "每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。",
  "do_precautions": [
    "如有异常，及时就诊",
    "入院前尽量保持空腹状"
  ],
  "next_treatment_date": "2026-02-13",
  "attending_physician": null,
  "pe_ecog_score": 1,
  "body_surface_area": null,
  "vs_temperature_c": 36.6,
  "vs_pulse_bpm": 76,
  "vs_respiration_rpm": 19,
  "vs_systolic_bp_mmhg": 113,
  "vs_diastolic_bp_mmhg": 75
}
2026-08-10 15:38:08,230 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-24]
2026-08-10 15:38:08,237 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2756451, prompt_len=2082
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["出院证明书", "(病人保存联)", "住院证字", "号", "姓名：", "性别：男", "年龄：39岁", "入院时间：2026-01-21 10:07", "出院时间：2026-01-24", "病人单位或住址", "出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR", "L858R+）", "3.恶性肿瘤靶向治疗", "4.肝继发恶性肿瘤", "5.骨继发恶性肿瘤", "6.化疗相关恶心和呕吐", "7.化疗后骨髓抑制", "8.白细胞减少", "9.恶性肿瘤的治疗后的随诊检查", "诊疗小结：患者因“发现右肺上叶占位7月，右肺上叶腺癌2周期化疗后20+天。”入院。入院查体：", "T36.6℃，P76次/分，R19次/分，BP113/75mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语", "颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣", "膜区未闻及病理性杂音。]辅助检查：暂缺。", "诊疗经过：[入院完善相关检查：2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红", "蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80", "(U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+", "ProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前", "体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。2026-01-22 胸腹部CT：1、“肺CA”复查，右", "肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，", "增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另", "见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺", "下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸", "膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大", "层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增", "粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前", "变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐", "骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。病情评价好转，排除于2026-1-23", "行第3周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w，同时给予", "患者抑酸护胃、止痛等对症支持治疗，现化疗已完成，于今出院回家乡休养。]", "治疗结果：好转", "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "诊。2、下周期治疗时间：2026年2月13日，请提前几天微信群预约床位，入院前尽量保持空腹状", "第1页/共2页"]

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
2026-08-10 15:38:26,488 INFO     29 [qwen-vl-text] coord API raw response (len=3199):
[
	{"text": "出院证明书", "bbox": [428, 18, 568, 40]},
	{"text": "(病人保存联)", "bbox": [50, 85, 166, 104]},
	{"text": "住院证字", "bbox": [543, 80, 626, 98]},
	{"text": "号", "bbox": [741, 80, 761, 98]},
	{"text": "姓名：", "bbox": [52, 116, 100, 134]},
	{"text": "性别：男", "bbox": [178, 114, 245, 132]},
	{"text": "年龄：39岁", "bbox": [265, 114, 371, 131]},
	{"text": "入院时间：2026-01-21 10:07", "bbox": [382, 112, 649, 129]},
	{"text": "出院时间：2026-01-24", "bbox": [331, 142, 536, 159]},
	{"text": "病人单位或住址", "bbox": [58, 175, 198, 192]},
	{"text": "出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR", "bbox": [62, 200, 888, 219]},
	{"text": "L858R+）", "bbox": [62, 232, 133, 248]},
	{"text": "3.恶性肿瘤靶向治疗", "bbox": [160, 230, 343, 247]},
	{"text": "4.肝继发恶性肿瘤", "bbox": [363, 229, 524, 246]},
	{"text": "5.骨继发恶性肿瘤", "bbox": [543, 228, 704, 245]},
	{"text": "6.化疗相关恶心和呕吐", "bbox": [723, 227, 923, 244]},
	{"text": "7.化疗后骨髓抑制", "bbox": [63, 258, 221, 275]},
	{"text": "8.白细胞减少", "bbox": [240, 257, 364, 274]},
	{"text": "9.恶性肿瘤的治疗后的随诊检查", "bbox": [383, 256, 664, 273]},
	{"text": "诊疗小结：患者因“发现右肺上叶占位7月，右肺上叶腺癌2周期化疗后20+天。”入院。入院查体：", "bbox": [63, 283, 919, 301]},
	{"text": "T36.6℃，P76次/分，R19次/分，BP113/75mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语", "bbox": [62, 311, 940, 329]},
	{"text": "颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣", "bbox": [61, 338, 940, 356]},
	{"text": "膜区未闻及病理性杂音。]辅助检查：暂缺。", "bbox": [58, 367, 437, 384]},
	{"text": "诊疗经过：[入院完善相关检查：2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红", "bbox": [57, 393, 935, 411]},
	{"text": "蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80", "bbox": [56, 420, 945, 438]},
	{"text": "(U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+", "bbox": [56, 447, 897, 465]},
	{"text": "ProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前", "bbox": [52, 473, 948, 491]},
	{"text": "体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。2026-01-22 胸腹部CT：1、“肺CA”复查，右", "bbox": [52, 500, 940, 519]},
	{"text": "肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，", "bbox": [50, 527, 939, 546]},
	{"text": "增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另", "bbox": [49, 554, 942, 573]},
	{"text": "见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺", "bbox": [49, 581, 955, 601]},
	{"text": "下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸", "bbox": [49, 608, 946, 630]},
	{"text": "膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大", "bbox": [48, 637, 948, 660]},
	{"text": "层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增", "bbox": [48, 665, 927, 690]},
	{"text": "粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前", "bbox": [47, 693, 949, 720]},
	{"text": "变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐", "bbox": [47, 722, 931, 750]},
	{"text": "骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。病情评价好转，排除于2026-1-23", "bbox": [47, 750, 952, 780]},
	{"text": "行第3周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w，同时给予", "bbox": [47, 778, 963, 809]},
	{"text": "患者抑酸护胃、止痛等对症支持治疗，现化疗已完成，于今出院回家乡休养。]", "bbox": [46, 813, 776, 842]},
	{"text": "治疗结果：好转", "bbox": [43, 855, 195, 873]},
	{"text": "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "bbox": [41, 868, 939, 905]},
	{"text": "诊。2、下周期治疗时间：2026年2月13日，请提前几天微信群预约床位，入院前尽量保持空腹状", "bbox": [38, 898, 955, 938]},
	{"text": "第1页/共2页", "bbox": [444, 941, 609, 962]}
]
2026-08-10 15:38:26,488 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=18.3s
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[0]: text=出院证明书, bbox=[428, 18, 568, 40]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[1]: text=(病人保存联), bbox=[50, 85, 166, 104]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[2]: text=住院证字, bbox=[543, 80, 626, 98]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[3]: text=号, bbox=[741, 80, 761, 98]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[52, 116, 100, 134]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[178, 114, 245, 132]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：39岁, bbox=[265, 114, 371, 131]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[7]: text=入院时间：2026-01-21 10:07, bbox=[382, 112, 649, 129]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[8]: text=出院时间：2026-01-24, bbox=[331, 142, 536, 159]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[9]: text=病人单位或住址, bbox=[58, 175, 198, 192]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[10]: text=出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR, bbox=[62, 200, 888, 219]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[11]: text=L858R+）, bbox=[62, 232, 133, 248]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[12]: text=3.恶性肿瘤靶向治疗, bbox=[160, 230, 343, 247]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[13]: text=4.肝继发恶性肿瘤, bbox=[363, 229, 524, 246]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[14]: text=5.骨继发恶性肿瘤, bbox=[543, 228, 704, 245]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[15]: text=6.化疗相关恶心和呕吐, bbox=[723, 227, 923, 244]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[16]: text=7.化疗后骨髓抑制, bbox=[63, 258, 221, 275]
2026-08-10 15:38:26,489 INFO     29 [qwen-vl-text] coord item[17]: text=8.白细胞减少, bbox=[240, 257, 364, 274]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[18]: text=9.恶性肿瘤的治疗后的随诊检查, bbox=[383, 256, 664, 273]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[19]: text=诊疗小结：患者因“发现右肺上叶占位7月，右肺上叶腺癌2周期化疗后20+天。”入院。入院查体：, bbox=[63, 283, 919, 301]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[20]: text=T36.6℃，P76次/分，R19次/分，BP113/75mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语, bbox=[62, 311, 940, 329]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[21]: text=颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣, bbox=[61, 338, 940, 356]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[22]: text=膜区未闻及病理性杂音。]辅助检查：暂缺。, bbox=[58, 367, 437, 384]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[23]: text=诊疗经过：[入院完善相关检查：2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红, bbox=[57, 393, 935, 411]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[24]: text=蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80, bbox=[56, 420, 945, 438]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[25]: text=(U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+, bbox=[56, 447, 897, 465]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[26]: text=ProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前, bbox=[52, 473, 948, 491]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[27]: text=体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。2026-01-22 胸腹部CT：1、“肺CA”复查，右, bbox=[52, 500, 940, 519]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[28]: text=肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，, bbox=[50, 527, 939, 546]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[29]: text=增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另, bbox=[49, 554, 942, 573]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[30]: text=见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺, bbox=[49, 581, 955, 601]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[31]: text=下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸, bbox=[49, 608, 946, 630]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[32]: text=膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大, bbox=[48, 637, 948, 660]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[33]: text=层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增, bbox=[48, 665, 927, 690]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[34]: text=粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前, bbox=[47, 693, 949, 720]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[35]: text=变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐, bbox=[47, 722, 931, 750]
2026-08-10 15:38:26,490 INFO     29 [qwen-vl-text] coord item[36]: text=骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。病情评价好转，排除于2026-1-23, bbox=[47, 750, 952, 780]
2026-08-10 15:38:26,491 INFO     29 [qwen-vl-text] coord item[37]: text=行第3周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w，同时给予, bbox=[47, 778, 963, 809]
2026-08-10 15:38:26,491 INFO     29 [qwen-vl-text] coord item[38]: text=患者抑酸护胃、止痛等对症支持治疗，现化疗已完成，于今出院回家乡休养。], bbox=[46, 813, 776, 842]
2026-08-10 15:38:26,491 INFO     29 [qwen-vl-text] coord item[39]: text=治疗结果：好转, bbox=[43, 855, 195, 873]
2026-08-10 15:38:26,491 INFO     29 [qwen-vl-text] coord item[40]: text=出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就, bbox=[41, 868, 939, 905]
2026-08-10 15:38:26,491 INFO     29 [qwen-vl-text] coord item[41]: text=诊。2、下周期治疗时间：2026年2月13日，请提前几天微信群预约床位，入院前尽量保持空腹状, bbox=[38, 898, 955, 938]
2026-08-10 15:38:26,491 INFO     29 [qwen-vl-text] coord item[42]: text=第1页/共2页, bbox=[444, 941, 609, 962]
2026-08-10 15:38:26,492 INFO     29 [qwen-vl-text] page=10 — 43/43 coords, api_time=18.3s
2026-08-10 15:38:26,492 INFO     29 [qwen-vl-text] new_positions (43):
[[10, 254.77812841796876, 338.1167685546875, 15.154020263671875, 33.6756005859375], [10, 29.763800048828127, 98.81581616210939, 71.56065124511719, 87.5565615234375], [10, 323.23486853027345, 372.64277661132815, 67.351201171875, 82.50522143554687], [10, 441.0995167236328, 453.00503674316406, 67.351201171875, 82.50522143554687], [10, 30.954352050781253, 59.527600097656254, 97.65924169921875, 112.81326196289062], [10, 105.95912817382813, 145.84262023925783, 95.97546166992187, 111.12948193359375], [10, 157.74814025878908, 220.8473963623047, 95.97546166992187, 110.28759191894531], [10, 227.39543237304687, 386.3341246337891, 94.291681640625, 108.60381188964844], [10, 197.0363563232422, 319.06793652343754, 119.54838208007813, 133.86051232910157], [10, 34.52600805664063, 117.86464819335939, 147.33075256347655, 161.6428828125], [10, 36.90711206054688, 528.6050888671875, 168.3780029296875, 184.37391320800782], [10, 36.90711206054688, 79.17170812988282, 195.3184833984375, 208.7887236328125], [10, 95.24416015625, 204.17966833496095, 193.63470336914062, 207.94683361816405], [10, 216.0851883544922, 311.9246245117188, 192.79281335449218, 207.10494360351564], [10, 323.23486853027345, 419.0743046875, 191.95092333984374, 206.2630535888672], [10, 430.3845487060547, 549.4397489013672, 191.1090333251953, 205.42116357421875], [10, 37.50238806152344, 131.55599621582033, 217.20762377929688, 231.5197540283203], [10, 142.866240234375, 216.68046435546876, 216.36573376464844, 230.67786401367186], [10, 227.99070837402346, 395.26326464843754, 215.52384375, 229.83597399902342], [10, 37.50238806152344, 547.0586448974609, 238.2548741455078, 253.40889440917968], [10, 36.90711206054688, 559.5594409179688, 261.82779455566407, 276.9818148193359], [10, 36.31183605957031, 559.5594409179688, 284.55882495117186, 299.71284521484375], [10, 34.52600805664063, 260.1356124267578, 308.9736353759766, 323.285765625], [10, 33.930732055664066, 556.583060913086, 330.86277575683596, 346.0167960205078], [10, 33.3354560546875, 562.5358209228516, 353.59380615234375, 368.74782641601564], [10, 33.3354560546875, 533.9625728759765, 376.32483654785153, 391.4788568115234], [10, 30.954352050781253, 564.3216489257812, 398.2139769287109, 413.3679971923828], [10, 30.954352050781253, 559.5594409179688, 420.94500732421875, 436.94091760253906], [10, 29.763800048828127, 558.9641649169922, 443.67603771972654, 459.67194799804685], [10, 29.168524047851562, 560.7499929199219, 466.4070681152344, 482.4029783935547], [10, 29.168524047851562, 568.4885809326172, 489.13809851074217, 505.97589880371095], [10, 29.168524047851562, 563.1310969238282, 511.86912890625, 530.3907092285157], [10, 28.573248046875, 564.3216489257812, 536.2839393310546, 555.6474096679688], [10, 28.573248046875, 551.8208529052735, 559.8568597412109, 580.9041101074218], [10, 27.97797204589844, 564.9169249267578, 583.4297801513671, 606.160810546875], [10, 27.97797204589844, 554.2019569091797, 607.8445905761719, 631.4175109863281], [10, 27.97797204589844, 566.7027529296876, 631.4175109863281, 656.6742114257812], [10, 27.97797204589844, 573.2507889404297, 654.9904313964844, 681.0890218505859], [10, 27.382696044921875, 461.9341767578125, 684.4565819091797, 708.8713923339843], [10, 25.596868041992188, 116.0788201904297, 719.8159625244141, 734.969982788086], [10, 24.406316040039062, 558.9641649169922, 730.7605327148437, 761.9104632568359], [10, 22.620488037109375, 568.4885809326172, 756.0172331542968, 789.6928337402344], [10, 264.30254443359377, 362.5230845947266, 792.2185037841797, 809.8981940917969]]
2026-08-10 15:38:26,493 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=36.3s
2026-08-10 15:38:26,493 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:38:26,502 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:38:26,502 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:38:26,502 INFO     29 [qwen-vl-text] positions(42): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:38:26,502 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [42]
2026-08-10 15:38:26,868 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:38:26,869 INFO     29 [qwen-vl-text] LLM extraction start, text_len=993
2026-08-10 15:38:26,869 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:38:26,869 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 593, \"bbox_end\": 634, \"encounter_dates\": [\"2026-02-24\", \"2026-02-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "民医院\n出院证明书\n(病人保存联)\n住院证字\n号\n姓名：\n性别：男\n年龄：39岁\n入院时间：2026-02-24 09:09\n出院时间：2026-02-26\n病人单位或住址：\n出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）\n2.肝继发恶性肿\n瘤\n3.骨继发恶性肿瘤\n4.恶性肿瘤靶向治疗\n5.化疗后血小板减少\n6.姑息性化疗\n诊疗小结：患者因“右肺上叶腺癌3周期化疗后20+天。”入院。入院查体：T36.4℃；P93次/分；\nR18次/分；BP107/70mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，\n双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。\n诊疗经过：完善检查，2026-02-24\n血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24\nCEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；\n2026-02-24\n凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU)\n↑；2026-02-24\n急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急\n诊)：钠 136.00(mmol/L)↓；患者无化疗禁忌，2026-02-25开始行第4周期AC方案化疗，具体方案\n为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼110mg po qd，患者治疗结束，复\n查2026-02-26[左上肢静脉,血管彩超]，左上肢静脉未见明显异常。予以拔除PICC管后办理出院。\n治疗结果：好转\n出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就\n诊。2、下周期治疗时间：2026年3月18日，肿瘤科门诊或日间放化疗门诊完成治疗。3、出院带\n药：-。4、\n5、加强营养，清淡饮食，避免着凉，预防感染，不适随诊。\n备注(包括手术名称)：[手术记录手术名称]\n时间：2026年02月26日\n说明：1、此证明书未经我院加盖公章无效。\n2、涂改未经加盖我院公章无效。\n3、此证明仅证明病人出院时病情。\n4、请妥善保管，遗失不补。",
    "role": "user"
  }
]
2026-08-10 15:38:29,153 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:38:29.152+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:38:36,931 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:38:36,932 INFO     29 [qwen-vl-text] LLM output (len=2172):
{
  "encounter_date": "2026-02-26",
  "admission_date": "2026-02-24",
  "discharge_date": "2026-02-26",
  "hospital_days": 2,
  "department": "肿瘤科",
  "bed_number": null,
  "admission_condition": "患者因“右肺上叶腺癌3周期化疗后20+天。”入院。入院查体：T36.4℃；P93次/分；R18次/分；BP107/70mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。",
  "admission_diagnoses": [],
  "treatment_summary": "完善检查，2026-02-24血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24CEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；2026-02-24凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU)↑；2026-02-24急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：钠 136.00(mmol/L)↓；患者无化疗禁忌，2026-02-25开始行第4周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼110mg po qd，患者治疗结束，复查2026-02-26[左上肢静脉,血管彩超]，左上肢静脉未见明显异常。予以拔除PICC管后办理出院。",
  "auxiliary_exams": "2026-02-24血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24CEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；2026-02-24凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU)↑；2026-02-24急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：钠 136.00(mmol/L)↓",
  "imaging_findings": "2026-02-26[左上肢静脉,血管彩超]，左上肢静脉未见明显异常。",
  "discharge_diagnoses": [
    {
      "name": "右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "骨继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶向治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗后血小板减少",
      "diagnosis_type": "西医"
    },
    {
      "name": "姑息性化疗",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": null,
  "outcome": "好转",
  "discharge_orders": "1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。2、下周期治疗时间：2026年3月18日，肿瘤科门诊或日间放化疗门诊完成治疗。3、出院带药：-。4、5、加强营养，清淡饮食，避免着凉，预防感染，不适随诊。",
  "do_medications": [],
  "do_follow_up": "每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。",
  "do_precautions": [
    "加强营养，清淡饮食，避免着凉，预防感染，不适随诊。"
  ],
  "next_treatment_date": "2026-03-18",
  "attending_physician": null,
  "pe_ecog_score": 1,
  "body_surface_area": null,
  "vs_temperature_c": 36.4,
  "vs_pulse_bpm": 93,
  "vs_respiration_rpm": 18,
  "vs_systolic_bp_mmhg": 107,
  "vs_diastolic_bp_mmhg": 70
}
2026-08-10 15:38:36,932 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-26]
2026-08-10 15:38:36,936 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2252680, prompt_len=1732
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共42行）
["民医院", "出院证明书", "(病人保存联)", "住院证字", "号", "姓名：", "性别：男", "年龄：39岁", "入院时间：2026-02-24 09:09", "出院时间：2026-02-26", "病人单位或住址：", "出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）", "2.肝继发恶性肿", "瘤", "3.骨继发恶性肿瘤", "4.恶性肿瘤靶向治疗", "5.化疗后血小板减少", "6.姑息性化疗", "诊疗小结：患者因“右肺上叶腺癌3周期化疗后20+天。”入院。入院查体：T36.4℃；P93次/分；", "R18次/分；BP107/70mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，", "双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。", "诊疗经过：完善检查，2026-02-24", "血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24", "CEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；", "2026-02-24", "凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU)", "↑；2026-02-24", "急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急", "诊)：钠 136.00(mmol/L)↓；患者无化疗禁忌，2026-02-25开始行第4周期AC方案化疗，具体方案", "为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼110mg po qd，患者治疗结束，复", "查2026-02-26[左上肢静脉,血管彩超]，左上肢静脉未见明显异常。予以拔除PICC管后办理出院。", "治疗结果：好转", "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "诊。2、下周期治疗时间：2026年3月18日，肿瘤科门诊或日间放化疗门诊完成治疗。3、出院带", "药：-。4、", "5、加强营养，清淡饮食，避免着凉，预防感染，不适随诊。", "备注(包括手术名称)：[手术记录手术名称]", "时间：2026年02月26日", "说明：1、此证明书未经我院加盖公章无效。", "2、涂改未经加盖我院公章无效。", "3、此证明仅证明病人出院时病情。", "4、请妥善保管，遗失不补。"]

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
2026-08-10 15:38:53,792 INFO     29 [qwen-vl-text] coord API raw response (len=2819):
[
	{"text": "民医院", "bbox": [530, 15, 625, 43]},
	{"text": "出院证明书", "bbox": [442, 63, 582, 87]},
	{"text": "(病人保存联)", "bbox": [54, 125, 173, 144]},
	{"text": "住院证字", "bbox": [556, 125, 641, 143]},
	{"text": "号", "bbox": [757, 126, 777, 143]},
	{"text": "姓名：", "bbox": [54, 156, 107, 174]},
	{"text": "性别：男", "bbox": [195, 156, 253, 174]},
	{"text": "年龄：39岁", "bbox": [274, 156, 381, 174]},
	{"text": "入院时间：2026-02-24 09:09", "bbox": [391, 156, 664, 173]},
	{"text": "出院时间：2026-02-26", "bbox": [348, 185, 549, 202]},
	{"text": "病人单位或住址：", "bbox": [58, 215, 213, 233]},
	{"text": "出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）", "bbox": [62, 244, 785, 261]},
	{"text": "2.肝继发恶性肿", "bbox": [813, 244, 954, 261]},
	{"text": "瘤", "bbox": [60, 273, 83, 290]},
	{"text": "3.骨继发恶性肿瘤", "bbox": [102, 273, 266, 290]},
	{"text": "4.恶性肿瘤靶向治疗", "bbox": [287, 273, 474, 290]},
	{"text": "5.化疗后血小板减少", "bbox": [494, 273, 681, 290]},
	{"text": "6.姑息性化疗", "bbox": [691, 273, 812, 290]},
	{"text": "诊疗小结：患者因“右肺上叶腺癌3周期化疗后20+天。”入院。入院查体：T36.4℃；P93次/分；", "bbox": [60, 300, 933, 318]},
	{"text": "R18次/分；BP107/70mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，", "bbox": [60, 328, 953, 346]},
	{"text": "双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。", "bbox": [60, 356, 957, 373]},
	{"text": "诊疗经过：完善检查，2026-02-24", "bbox": [57, 384, 375, 401]},
	{"text": "血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24", "bbox": [395, 384, 952, 401]},
	{"text": "CEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；", "bbox": [64, 411, 867, 429]},
	{"text": "2026-02-24", "bbox": [52, 440, 160, 457]},
	{"text": "凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU)", "bbox": [180, 439, 950, 457]},
	{"text": "↑；2026-02-24", "bbox": [57, 468, 201, 485]},
	{"text": "急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急", "bbox": [221, 467, 934, 485]},
	{"text": "诊)：钠 136.00(mmol/L)↓；患者无化疗禁忌，2026-02-25开始行第4周期AC方案化疗，具体方案", "bbox": [48, 495, 946, 513]},
	{"text": "为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼110mg po qd，患者治疗结束，复", "bbox": [47, 523, 970, 541]},
	{"text": "查2026-02-26 [左上肢静脉,血管彩超]，左上肢静脉未见明显异常。予以拔除PICC管后办理出院。", "bbox": [45, 551, 938, 569]},
	{"text": "治疗结果：好转", "bbox": [43, 583, 196, 600]},
	{"text": "出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就", "bbox": [43, 610, 944, 628]},
	{"text": "诊。2、下周期治疗时间：2026年3月18日，肿瘤科门诊或日间放化疗门诊完成治疗。3、出院带", "bbox": [41, 638, 953, 657]},
	{"text": "药：-。4、", "bbox": [39, 674, 137, 692]},
	{"text": "5、加强营养，清淡饮食，避免着凉，预防感染，不适随诊。", "bbox": [268, 698, 829, 718]},
	{"text": "备注(包括手术名称)：[手术记录手术名称]", "bbox": [37, 731, 478, 752]},
	{"text": "时间：2026年02月26日", "bbox": [689, 756, 899, 776]},
	{"text": "说明：1、此证明书未经我院加盖公章无效。", "bbox": [36, 794, 455, 814]},
	{"text": "2、涂改未经加盖我院公章无效。", "bbox": [498, 789, 800, 809]},
	{"text": "3、此证明仅证明病人出院时病情。", "bbox": [100, 826, 434, 846]},
	{"text": "4、请妥善保管，遗失不补。", "bbox": [498, 821, 760, 841]}
]
2026-08-10 15:38:53,792 INFO     29 [qwen-vl-text] coord API: raw_items=42, valid_items=42, elapsed=16.9s
2026-08-10 15:38:53,792 INFO     29 [qwen-vl-text] coord item[0]: text=民医院, bbox=[530, 15, 625, 43]
2026-08-10 15:38:53,792 INFO     29 [qwen-vl-text] coord item[1]: text=出院证明书, bbox=[442, 63, 582, 87]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[2]: text=(病人保存联), bbox=[54, 125, 173, 144]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[3]: text=住院证字, bbox=[556, 125, 641, 143]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[4]: text=号, bbox=[757, 126, 777, 143]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[5]: text=姓名：, bbox=[54, 156, 107, 174]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[6]: text=性别：男, bbox=[195, 156, 253, 174]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：39岁, bbox=[274, 156, 381, 174]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[8]: text=入院时间：2026-02-24 09:09, bbox=[391, 156, 664, 173]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[9]: text=出院时间：2026-02-26, bbox=[348, 185, 549, 202]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[10]: text=病人单位或住址：, bbox=[58, 215, 213, 233]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[11]: text=出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）, bbox=[62, 244, 785, 261]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[12]: text=2.肝继发恶性肿, bbox=[813, 244, 954, 261]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[13]: text=瘤, bbox=[60, 273, 83, 290]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[14]: text=3.骨继发恶性肿瘤, bbox=[102, 273, 266, 290]
2026-08-10 15:38:53,793 INFO     29 [qwen-vl-text] coord item[15]: text=4.恶性肿瘤靶向治疗, bbox=[287, 273, 474, 290]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[16]: text=5.化疗后血小板减少, bbox=[494, 273, 681, 290]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[17]: text=6.姑息性化疗, bbox=[691, 273, 812, 290]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[18]: text=诊疗小结：患者因“右肺上叶腺癌3周期化疗后20+天。”入院。入院查体：T36.4℃；P93次/分；, bbox=[60, 300, 933, 318]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[19]: text=R18次/分；BP107/70mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，, bbox=[60, 328, 953, 346]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[20]: text=双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。, bbox=[60, 356, 957, 373]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[21]: text=诊疗经过：完善检查，2026-02-24, bbox=[57, 384, 375, 401]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[22]: text=血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24, bbox=[395, 384, 952, 401]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[23]: text=CEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；, bbox=[64, 411, 867, 429]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[24]: text=2026-02-24, bbox=[52, 440, 160, 457]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[25]: text=凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU), bbox=[180, 439, 950, 457]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[26]: text=↑；2026-02-24, bbox=[57, 468, 201, 485]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[27]: text=急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急, bbox=[221, 467, 934, 485]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[28]: text=诊)：钠 136.00(mmol/L)↓；患者无化疗禁忌，2026-02-25开始行第4周期AC方案化疗，具体方案, bbox=[48, 495, 946, 513]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[29]: text=为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼110mg po qd，患者治疗结束，复, bbox=[47, 523, 970, 541]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[30]: text=查2026-02-26 [左上肢静脉,血管彩超]，左上肢静脉未见明显异常。予以拔除PICC管后办理出院。, bbox=[45, 551, 938, 569]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[31]: text=治疗结果：好转, bbox=[43, 583, 196, 600]
2026-08-10 15:38:53,794 INFO     29 [qwen-vl-text] coord item[32]: text=出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就, bbox=[43, 610, 944, 628]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[33]: text=诊。2、下周期治疗时间：2026年3月18日，肿瘤科门诊或日间放化疗门诊完成治疗。3、出院带, bbox=[41, 638, 953, 657]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[34]: text=药：-。4、, bbox=[39, 674, 137, 692]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[35]: text=5、加强营养，清淡饮食，避免着凉，预防感染，不适随诊。, bbox=[268, 698, 829, 718]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[36]: text=备注(包括手术名称)：[手术记录手术名称], bbox=[37, 731, 478, 752]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[37]: text=时间：2026年02月26日, bbox=[689, 756, 899, 776]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[38]: text=说明：1、此证明书未经我院加盖公章无效。, bbox=[36, 794, 455, 814]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[39]: text=2、涂改未经加盖我院公章无效。, bbox=[498, 789, 800, 809]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[40]: text=3、此证明仅证明病人出院时病情。, bbox=[100, 826, 434, 846]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] coord item[41]: text=4、请妥善保管，遗失不补。, bbox=[498, 821, 760, 841]
2026-08-10 15:38:53,795 INFO     29 [qwen-vl-text] page=11 — 42/42 coords, api_time=16.9s
2026-08-10 15:38:53,796 INFO     29 [qwen-vl-text] new_positions (42):
[[11, 315.49628051757816, 372.04750061035156, 12.628350219726562, 36.20127062988281], [11, 263.11199243164066, 346.45063256835937, 53.039070922851565, 73.24443127441405], [11, 32.144904052734375, 102.98274816894532, 105.23625183105469, 121.232162109375], [11, 330.9734565429688, 381.5719166259766, 105.23625183105469, 120.39027209472655], [11, 450.62393273925784, 462.5294527587891, 106.07814184570313, 120.39027209472655], [11, 32.144904052734375, 63.69453210449219, 131.33484228515624, 146.4888625488281], [11, 116.0788201904297, 150.60482824707032, 131.33484228515624, 146.4888625488281], [11, 163.10562426757812, 226.80015637207032, 131.33484228515624, 146.4888625488281], [11, 232.75291638183595, 395.26326464843754, 131.33484228515624, 145.6469725341797], [11, 207.15604833984375, 326.8065245361328, 155.74965270996094, 170.06178295898437], [11, 34.52600805664063, 126.79378820800781, 181.00635314941405, 196.16037341308595], [11, 36.90711206054688, 467.2916607666016, 205.42116357421875, 219.73329382324218], [11, 483.9593887939453, 567.8933049316406, 205.42116357421875, 219.73329382324218], [11, 35.71656005859375, 49.40790808105469, 229.83597399902342, 244.14810424804688], [11, 60.71815209960938, 158.34341625976563, 229.83597399902342, 244.14810424804688], [11, 170.84421228027344, 282.1608244628906, 229.83597399902342, 244.14810424804688], [11, 294.06634448242187, 405.3829566650391, 229.83597399902342, 244.14810424804688], [11, 411.3357166748047, 483.3641127929688, 229.83597399902342, 244.14810424804688], [11, 35.71656005859375, 555.3925089111328, 252.56700439453124, 267.72102465820313], [11, 35.71656005859375, 567.298028930664, 276.1399248046875, 291.2939450683594], [11, 35.71656005859375, 569.6791329345704, 299.71284521484375, 314.0249754638672], [11, 33.930732055664066, 223.22850036621094, 323.285765625, 337.59789587402344], [11, 235.1340203857422, 566.7027529296876, 323.285765625, 337.59789587402344], [11, 38.0976640625, 516.1042928466798, 346.0167960205078, 361.1708162841797], [11, 30.954352050781253, 95.24416015625, 370.43160644531247, 384.74373669433595], [11, 107.14968017578126, 565.5122009277344, 369.58971643066405, 384.74373669433595], [11, 33.930732055664066, 119.65047619628906, 394.0045268554687, 408.3166571044922], [11, 131.55599621582033, 555.9877849121094, 393.1626368408203, 408.3166571044922], [11, 28.573248046875, 563.1310969238282, 416.73555725097657, 431.8895775146484], [11, 27.97797204589844, 577.4177209472656, 440.3084776611328, 455.46249792480467], [11, 26.787420043945314, 558.3688889160156, 463.8813980712891, 479.0354183349609], [11, 25.596868041992188, 116.67409619140625, 490.82187854003905, 505.1340087890625], [11, 25.596868041992188, 561.940544921875, 513.5529089355468, 528.7069291992187], [11, 24.406316040039062, 567.298028930664, 537.1258293457031, 553.1217396240235], [11, 23.21576403808594, 81.55281213378906, 567.4338698730469, 582.5878901367188], [11, 159.53396826171877, 493.48380480957036, 587.6392302246094, 604.4770305175781], [11, 22.025212036132814, 284.5419284667969, 615.4216007080078, 633.101291015625], [11, 410.1451646728516, 535.1531248779297, 636.4688510742187, 653.3066513671874], [11, 21.429936035156253, 270.85058044433595, 668.4606716308593, 685.2984719238281], [11, 296.44744848632814, 476.22080078125003, 664.2512215576172, 681.0890218505859], [11, 59.527600097656254, 258.3497844238281, 695.4011520996094, 712.2389523925781], [11, 296.44744848632814, 452.40976074218753, 691.1917020263671, 708.029502319336]]
2026-08-10 15:38:53,796 INFO     29 [qwen-vl-text] ═══ DONE ═══ 42 positions, pages=1, time=27.3s
2026-08-10 15:38:53,796 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:38:53,798 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:38:53,798 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:38:53,798 INFO     29 [qwen-vl-text] positions(35): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:38:53,799 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [35]
2026-08-10 15:38:54,107 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:38:54,109 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1263
2026-08-10 15:38:54,109 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:38:54,109 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 705, \"bbox_end\": 739, \"encounter_dates\": [\"2026-03-23\", \"2026-03-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院证明书\n(病人保存联)\n住院证字\n号\n性别：男 年龄：39岁 入院时间：2026-03-23 10:38\n床号\n出院时间：2026-03-25\n病人单位或住址：\n出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+） 2.肝继发恶性肿\n瘤 3.骨继发恶性肿瘤 4.肝功能不全\n诊疗小结：患者因“右肺上叶腺癌4周期化疗后1+月。”入院。入院查体：T36.4℃ ;P93次/分；\nR18次/分;BP107/70mmHg\n诊疗经过：完善检查，2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急\n诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；\n2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml)\n↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L\nFEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L)\n↓。2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右\n肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，\n增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另\n见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右\n肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增\n厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范\n围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节\n状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、\n胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，\n增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠\n均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双\n侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。患者肝\n功能不全，予以保肝治疗，患者病情进展，考虑参加临床实验，予以办理出院。\n治疗结果：好转\n出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。 2、等待电话通\n知临床试验筛查。 3、出院带药：-。4、门诊随访：\n5、加强营养，清淡饮食，避免着凉，预防感\n第1页/共2页",
    "role": "user"
  }
]
2026-08-10 15:39:00,982 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:39:00.982+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:39:09,564 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:39:09,564 INFO     29 [qwen-vl-text] LLM output (len=3034):
{
  "encounter_date": "2026-03-25",
  "admission_date": "2026-03-23",
  "discharge_date": "2026-03-25",
  "hospital_days": 2,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者因“右肺上叶腺癌4周期化疗后1+月。”入院。入院查体：T36.4℃ ;P93次/分；R18次/分;BP107/70mmHg",
  "admission_diagnoses": [],
  "treatment_summary": "完善检查，2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml)↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L FEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L)↓。2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。患者肝功能不全，予以保肝治疗，患者病情进展，考虑参加临床实验，予以办理出院。",
  "auxiliary_exams": "2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml)↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L FEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L)↓。",
  "imaging_findings": "2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。",
  "discharge_diagnoses": [
    {
      "name": "右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "骨继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝功能不全",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": null,
  "outcome": "好转",
  "discharge_orders": "1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。 2、等待电话通知临床试验筛查。 3、出院带药：-。4、门诊随访： 5、加强营养，清淡饮食，避免着凉，预防感",
  "do_medications": [],
  "do_follow_up": "门诊随访：",
  "do_precautions": [
    "每周复查血常规，每2周复查肝肾功，如有异常，及时就诊",
    "等待电话通知临床试验筛查",
    "加强营养，清淡饮食，避免着凉，预防感"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": 36.4,
  "vs_pulse_bpm": 93,
  "vs_respiration_rpm": 18,
  "vs_systolic_bp_mmhg": 107,
  "vs_diastolic_bp_mmhg": 70
}
2026-08-10 15:39:09,564 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-25]
2026-08-10 15:39:09,569 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2154760, prompt_len=1981
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["出院证明书", "(病人保存联)", "住院证字", "号", "性别：男 年龄：39岁 入院时间：2026-03-23 10:38", "床号", "出院时间：2026-03-25", "病人单位或住址：", "出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+） 2.肝继发恶性肿", "瘤 3.骨继发恶性肿瘤 4.肝功能不全", "诊疗小结：患者因“右肺上叶腺癌4周期化疗后1+月。”入院。入院查体：T36.4℃ ;P93次/分；", "R18次/分;BP107/70mmHg", "诊疗经过：完善检查，2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急", "诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；", "2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml)", "↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L", "FEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L)", "↓。2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右", "肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，", "增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另", "见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右", "肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增", "厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范", "围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节", "状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、", "胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，", "增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠", "均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双", "侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。患者肝", "功能不全，予以保肝治疗，患者病情进展，考虑参加临床实验，予以办理出院。", "治疗结果：好转", "出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。 2、等待电话通", "知临床试验筛查。 3、出院带药：-。4、门诊随访：", "5、加强营养，清淡饮食，避免着凉，预防感", "第1页/共2页"]

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
2026-08-10 15:39:26,820 INFO     29 [qwen-vl-text] coord API raw response (len=2775):
[
	{"text": "出院证明书", "bbox": [427, 46, 552, 66]},
	{"text": "(病人保存联)", "bbox": [75, 97, 184, 112]},
	{"text": "住院证字", "bbox": [530, 100, 605, 114]},
	{"text": "号", "bbox": [708, 101, 726, 115]},
	{"text": "性别：男 年龄：39岁 入院时间：2026-03-23 10:38", "bbox": [74, 122, 627, 138]},
	{"text": "床号", "bbox": [227, 148, 264, 163]},
	{"text": "出院时间：2026-03-25", "bbox": [333, 149, 523, 164]},
	{"text": "病人单位或住址：", "bbox": [74, 174, 216, 189]},
	{"text": "出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+） 2.肝继发恶性肿", "bbox": [75, 200, 896, 216]},
	{"text": "瘤 3.骨继发恶性肿瘤 4.肝功能不全", "bbox": [75, 225, 390, 241]},
	{"text": "诊疗小结：患者因“右肺上叶腺癌4周期化疗后1+月。”入院。入院查体：T36.4℃ ;P93次/分；", "bbox": [75, 251, 867, 267]},
	{"text": "R18次/分;BP107/70mmHg", "bbox": [75, 278, 287, 294]},
	{"text": "诊疗经过：完善检查，2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急", "bbox": [77, 303, 878, 319]},
	{"text": "诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；", "bbox": [79, 329, 876, 345]},
	{"text": "2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml)", "bbox": [79, 355, 884, 371]},
	{"text": "↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L", "bbox": [85, 380, 880, 397]},
	{"text": "FEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L)", "bbox": [80, 406, 896, 422]},
	{"text": "↓。2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右", "bbox": [85, 431, 900, 447]},
	{"text": "肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，", "bbox": [80, 457, 900, 473]},
	{"text": "增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另", "bbox": [79, 482, 904, 498]},
	{"text": "见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右", "bbox": [79, 507, 916, 523]},
	{"text": "肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增", "bbox": [75, 532, 908, 549]},
	{"text": "厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范", "bbox": [75, 558, 911, 574]},
	{"text": "围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节", "bbox": [73, 583, 912, 600]},
	{"text": "状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、", "bbox": [70, 609, 914, 626]},
	{"text": "胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，", "bbox": [68, 636, 914, 655]},
	{"text": "增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠", "bbox": [67, 664, 918, 682]},
	{"text": "均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双", "bbox": [65, 691, 930, 710]},
	{"text": "侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。患者肝", "bbox": [63, 718, 931, 738]},
	{"text": "功能不全，予以保肝治疗，患者病情进展，考虑参加临床实验，予以办理出院。", "bbox": [62, 748, 748, 767]},
	{"text": "治疗结果：好转", "bbox": [60, 780, 201, 796]},
	{"text": "出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。 2、等待电话通", "bbox": [59, 806, 926, 825]},
	{"text": "知临床试验筛查。 3、出院带药：-。4、门诊随访：", "bbox": [57, 837, 512, 855]},
	{"text": "5、加强营养，清淡饮食，避免着凉，预防感", "bbox": [531, 865, 937, 884]},
	{"text": "第1页/共2页", "bbox": [430, 895, 584, 912]}
]
2026-08-10 15:39:26,821 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=17.3s
2026-08-10 15:39:26,821 INFO     29 [qwen-vl-text] coord item[0]: text=出院证明书, bbox=[427, 46, 552, 66]
2026-08-10 15:39:26,821 INFO     29 [qwen-vl-text] coord item[1]: text=(病人保存联), bbox=[75, 97, 184, 112]
2026-08-10 15:39:26,821 INFO     29 [qwen-vl-text] coord item[2]: text=住院证字, bbox=[530, 100, 605, 114]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[3]: text=号, bbox=[708, 101, 726, 115]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男 年龄：39岁 入院时间：2026-03-23 10:38, bbox=[74, 122, 627, 138]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[5]: text=床号, bbox=[227, 148, 264, 163]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[6]: text=出院时间：2026-03-25, bbox=[333, 149, 523, 164]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[7]: text=病人单位或住址：, bbox=[74, 174, 216, 189]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[8]: text=出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+） 2.肝继发恶性肿, bbox=[75, 200, 896, 216]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[9]: text=瘤 3.骨继发恶性肿瘤 4.肝功能不全, bbox=[75, 225, 390, 241]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[10]: text=诊疗小结：患者因“右肺上叶腺癌4周期化疗后1+月。”入院。入院查体：T36.4℃ ;P93次/分；, bbox=[75, 251, 867, 267]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[11]: text=R18次/分;BP107/70mmHg, bbox=[75, 278, 287, 294]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[12]: text=诊疗经过：完善检查，2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急, bbox=[77, 303, 878, 319]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[13]: text=诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；, bbox=[79, 329, 876, 345]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[14]: text=2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml), bbox=[79, 355, 884, 371]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[15]: text=↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L, bbox=[85, 380, 880, 397]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[16]: text=FEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L), bbox=[80, 406, 896, 422]
2026-08-10 15:39:26,822 INFO     29 [qwen-vl-text] coord item[17]: text=↓。2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右, bbox=[85, 431, 900, 447]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[18]: text=肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，, bbox=[80, 457, 900, 473]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[19]: text=增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另, bbox=[79, 482, 904, 498]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[20]: text=见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右, bbox=[79, 507, 916, 523]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[21]: text=肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增, bbox=[75, 532, 908, 549]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[22]: text=厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范, bbox=[75, 558, 911, 574]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[23]: text=围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节, bbox=[73, 583, 912, 600]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[24]: text=状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、, bbox=[70, 609, 914, 626]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[25]: text=胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，, bbox=[68, 636, 914, 655]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[26]: text=增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠, bbox=[67, 664, 918, 682]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[27]: text=均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双, bbox=[65, 691, 930, 710]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[28]: text=侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。患者肝, bbox=[63, 718, 931, 738]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[29]: text=功能不全，予以保肝治疗，患者病情进展，考虑参加临床实验，予以办理出院。, bbox=[62, 748, 748, 767]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[30]: text=治疗结果：好转, bbox=[60, 780, 201, 796]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[31]: text=出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。 2、等待电话通, bbox=[59, 806, 926, 825]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[32]: text=知临床试验筛查。 3、出院带药：-。4、门诊随访：, bbox=[57, 837, 512, 855]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[33]: text=5、加强营养，清淡饮食，避免着凉，预防感, bbox=[531, 865, 937, 884]
2026-08-10 15:39:26,823 INFO     29 [qwen-vl-text] coord item[34]: text=第1页/共2页, bbox=[430, 895, 584, 912]
2026-08-10 15:39:26,824 INFO     29 [qwen-vl-text] page=14 — 35/35 coords, api_time=17.3s
2026-08-10 15:39:26,825 INFO     29 [qwen-vl-text] new_positions (35):
[[14, 254.1828524169922, 328.5923525390625, 38.726940673828125, 55.564740966796876], [14, 44.64570007324219, 109.5307841796875, 81.66333142089843, 94.291681640625], [14, 315.49628051757816, 360.1419805908203, 84.18900146484376, 95.97546166992187], [14, 421.45540869140626, 432.1703767089844, 85.03089147949218, 96.81735168457031], [14, 44.05042407226563, 373.2380526123047, 102.71058178710938, 116.18082202148437], [14, 135.12765222167968, 157.1528642578125, 124.59972216796875, 137.2280723876953], [14, 198.22690832519532, 311.3293485107422, 125.44161218261719, 138.06996240234375], [14, 44.05042407226563, 128.5796162109375, 146.4888625488281, 159.11721276855468], [14, 44.64570007324219, 533.367296875, 168.3780029296875, 181.8482431640625], [14, 44.64570007324219, 232.1576403808594, 189.42525329589844, 202.89549353027343], [14, 44.64570007324219, 516.1042928466798, 211.31439367675782, 224.7846339111328], [14, 44.64570007324219, 170.84421228027344, 234.04542407226563, 247.51566430664062], [14, 45.83625207519531, 522.6523288574219, 255.09267443847656, 268.56291467285155], [14, 47.02680407714844, 521.4617768554688, 276.9818148193359, 290.4520550537109], [14, 47.02680407714844, 526.2239848632813, 298.8709552001953, 312.3411954345703], [14, 50.598460083007815, 523.842880859375, 319.91820556640624, 334.23033581542967], [14, 47.622080078125, 533.367296875, 341.8073459472656, 355.27758618164063], [14, 50.598460083007815, 535.7484008789063, 362.8545963134766, 376.32483654785153], [14, 47.622080078125, 535.7484008789063, 384.74373669433595, 398.2139769287109], [14, 47.02680407714844, 538.1295048828125, 405.79098706054685, 419.26122729492187], [14, 47.02680407714844, 545.2728168945313, 426.8382374267578, 440.3084776611328], [14, 44.64570007324219, 540.5106088867187, 447.8854877929687, 462.1976180419922], [14, 44.64570007324219, 542.2964368896485, 469.7746281738281, 483.2448684082031], [14, 43.45514807128907, 542.8917128906251, 490.82187854003905, 505.1340087890625], [14, 41.669320068359376, 544.0822648925781, 512.7110189208985, 527.0231491699219], [14, 40.47876806640625, 544.0822648925781, 535.4420493164063, 551.4379595947265], [14, 39.88349206542969, 546.4633688964844, 559.0149697265625, 574.1689899902344], [14, 38.69294006347656, 553.6066809082032, 581.7460001220703, 597.7419104003906], [14, 37.50238806152344, 554.2019569091797, 604.4770305175781, 621.3148308105468], [14, 36.90711206054688, 445.26644873046877, 629.7337309570313, 645.7296412353516], [14, 35.71656005859375, 119.65047619628906, 656.6742114257812, 670.1444516601563], [14, 35.12128405761719, 551.2255769042969, 678.5633518066406, 694.5592620849609], [14, 33.930732055664066, 304.7813125, 704.6619422607422, 719.8159625244141], [14, 316.0915565185547, 557.773612915039, 728.2348626708985, 744.2307729492187], [14, 255.9686804199219, 347.64118457031253, 753.4915631103515, 767.803693359375]]
2026-08-10 15:39:26,825 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=33.0s
2026-08-10 15:39:26,836 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 15:39:26,837 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:Discharge | outputs={"chunks": "6 items, types={'DischargeRecord': 6}", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:39:26,837 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 15:39:26,844 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:39:26,845 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:39:26,845 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 15:39:26,845 INFO     29 [qwen-vl-text] positions(64): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:39:26,845 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [36, 28]
2026-08-10 15:39:27,292 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:39:27,667 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:39:27,668 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1897
2026-08-10 15:39:27,668 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:39:27,669 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 63, \"encounter_dates\": [\"2025-09-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "入院记录\n姓名：\n性别：男\n年龄：38岁\n婚姻状况：已婚\n出生地：\n民族：汉族\n现住址：\n职业：自由职业者\n入院时间：2025-09-09 10:41\n记录时间：2025-09-09 11:01\n病史陈述者\n联系人姓名：\n联系人电话：\n病史真实性确认签字：\n主诉：咳嗽3+月，发现右上肺占位10+天\n现病史：入院前3+月，患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。10+天前，患\n民医院就诊，完善胸部CT\n提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑\n占位性病变，肺Ca可能性大。建议结合临床进一步检查。2.双肺散在点结影及条索影。3.纵隔内可见\n淋巴结显示，部分稍大。4.心脏形态大小未见异常。5.双侧胸腔未见确切积液征象。6.扫及肝右叶见\n片状密度低影，长径约2.7cm，性质?建议进一步检查。7.扫及胸椎多个椎体骨质密度减低破坏改\n变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+\nNSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段\n测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺\n另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分\n稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，\n必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破\n坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.电轴左偏。建议完善经皮肺穿刺\n检查后纤支镜下肺活检明确，患方商议后表示拒绝，现患者为进一步明确占位性质，遂于我院门诊就\n诊，门诊以“右上肺占位”收入我科。\n自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。\n既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病\n史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。\n过敏史：否认食物、药物过敏史。\n个人史：出生原籍，长期居住生长于当地，否认疫区居住治游史，平素偶有饮酒，否认吸烟及\n人民医院\n入院记录\n家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。\n体格检查\nT36.1℃\nP92次/分\nR19次/分\nBP121/83mmHg\n一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮\n疹。背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部\n及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。\n颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊\n清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，HR92次/分，律齐，各\n瓣膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性\n浊音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经\n系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。\n专科情况\n背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。胸廓正常，双肺语颤正常，双肺叩诊清\n音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，HR92次/分，律齐，各瓣膜区未闻\n及病理性杂音。\n辅助检查\n2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇\n化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块,\n肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在\n斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低\n密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎\n体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦\n性心律 2.由缺血性",
    "role": "user"
  }
]
2026-08-10 15:39:32,765 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:39:32.765+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:39:44,106 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:39:44,106 INFO     29 [qwen-vl-text] LLM output (len=3207):
{
  "encounter_date": "2025-09-09",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": 38,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "自由职业者",
  "dm_admission_time": "2025-09-09 10:41",
  "dm_record_time": "2025-09-09 11:01",
  "dm_history_provider": null,
  "cc_text": "咳嗽3+月，发现右上肺占位10+天",
  "cc_main_symptoms": [
    "咳嗽",
    "右上肺占位"
  ],
  "cc_duration": "3+月",
  "pi_text": "入院前3+月，患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。10+天前，患民医院就诊，完善胸部CT提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca可能性大。建议结合临床进一步检查。2.双肺散在点结影及条索影。3.纵隔内可见淋巴结显示，部分稍大。4.心脏形态大小未见异常。5.双侧胸腔未见确切积液征象。6.扫及肝右叶见片状密度低影，长径约2.7cm，性质?建议进一步检查。7.扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.电轴左偏。建议完善经皮肺穿刺检查后纤支镜下肺活检明确，患方商议后表示拒绝，现患者为进一步明确占位性质，遂于我院门诊就诊，门诊以“右上肺占位”收入我科。自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。",
  "pmh_disease_history": [
    "否认糖尿病",
    "否认高血压",
    "否认高血脂",
    "否认结核",
    "否认肝炎",
    "否认精神病史"
  ],
  "pmh_allergy_history": [
    "否认食物过敏",
    "否认药物过敏"
  ],
  "pmh_surgery_trauma_history": [
    "否认重大外伤史",
    "否认手术史",
    "无输血及血液制品史"
  ],
  "ph_smoking": "否认吸烟",
  "ph_drinking": "平素偶有饮酒",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "否认家族性遗传病、精神病史，否认家族性肿瘤病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.1,
  "vs_pulse_bpm": 92,
  "vs_respiration_rpm": 19,
  "vs_systolic_bp_mmhg": 121,
  "vs_diastolic_bp_mmhg": 83,
  "pe_general_condition": "发育正常，体型消瘦，步入病房，神志清醒，查体合作。",
  "pe_skin_mucosa": "无黄染皮疹。背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。",
  "pe_lymph_nodes": "浅表淋巴结未扪及肿大。",
  "pe_lungs": "胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。",
  "pe_heart": "心界不大，HR92次/分，律齐，各瓣膜区未闻及病理性杂音。",
  "pe_abdomen": "腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊音，肠鸣音正常。",
  "pe_extremities": "脊柱、四肢无异常。双下肢不肿。",
  "pe_nervous_system": "腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。",
  "pe_specialist_exam": "背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，HR92次/分，律齐，各瓣膜区未闻及病理性杂音。",
  "pe_ecog_score": null,
  "pat_text": "2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块,肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.由缺血性",
  "pat_items": [
    "癌胚抗原 94.90(ng/ml)↑",
    "神经元特异性烯醇化酶 58.93(ng/ml)↑",
    "细胞角蛋白19片段测定 62.83(ng/ml)↑",
    "胸部增强CT: 右肺上叶团块,肿瘤占位性病变可能",
    "胸部增强CT: 双肺另见小结节",
    "胸部增强CT: 右肺中叶及双肺下叶见散在斑条影",
    "胸部增强CT: 纵膈见多发淋巴结显示，部分稍大",
    "胸部增强CT: 心包少量积液",
    "胸部增强CT: 左侧胸膜稍增厚",
    "胸部增强CT: 肝右叶低密度结节，占位性病变可能，转移灶待排",
    "胸部增强CT: 双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能",
    "胸部增强CT: T2椎体病理性骨折可能",
    "心电图: 窦性心律",
    "心电图: 由缺血性"
  ],
  "preliminary_diagnoses": [
    {
      "name": "右上肺占位",
      "diagnosis_type": "西医",
      "is_primary": true
    }
  ],
  "department": null
}
2026-08-10 15:39:44,106 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-09]
2026-08-10 15:39:44,121 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6449770, prompt_len=1746
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["入院记录", "姓名：", "性别：男", "年龄：38岁", "婚姻状况：已婚", "出生地：", "民族：汉族", "现住址：", "职业：自由职业者", "入院时间：2025-09-09 10:41", "记录时间：2025-09-09 11:01", "病史陈述者", "联系人姓名：", "联系人电话：", "病史真实性确认签字：", "主诉：咳嗽3+月，发现右上肺占位10+天", "现病史：入院前3+月，患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。10+天前，患", "民医院就诊，完善胸部CT", "提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑", "占位性病变，肺Ca可能性大。建议结合临床进一步检查。2.双肺散在点结影及条索影。3.纵隔内可见", "淋巴结显示，部分稍大。4.心脏形态大小未见异常。5.双侧胸腔未见确切积液征象。6.扫及肝右叶见", "片状密度低影，长径约2.7cm，性质?建议进一步检查。7.扫及胸椎多个椎体骨质密度减低破坏改", "变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+", "NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段", "测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺", "另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分", "稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，", "必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破", "坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.电轴左偏。建议完善经皮肺穿刺", "检查后纤支镜下肺活检明确，患方商议后表示拒绝，现患者为进一步明确占位性质，遂于我院门诊就", "诊，门诊以“右上肺占位”收入我科。", "自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。", "既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病", "史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。", "过敏史：否认食物、药物过敏史。", "个人史：出生原籍，长期居住生长于当地，否认疫区居住治游史，平素偶有饮酒，否认吸烟及"]

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
2026-08-10 15:40:00,154 INFO     29 [qwen-vl-text] coord API raw response (len=2596):
[
	{"text": "入院记录", "bbox": [433, 93, 590, 113]},
	{"text": "姓名：", "bbox": [177, 146, 275, 165]},
	{"text": "性别：男", "bbox": [177, 174, 308, 193]},
	{"text": "年龄：38岁", "bbox": [177, 202, 327, 221]},
	{"text": "婚姻状况：已婚", "bbox": [177, 230, 327, 249]},
	{"text": "出生地：", "bbox": [177, 258, 275, 277]},
	{"text": "民族：汉族", "bbox": [177, 286, 329, 305]},
	{"text": "现住址：", "bbox": [177, 314, 275, 333]},
	{"text": "职业：自由职业者", "bbox": [582, 149, 795, 167]},
	{"text": "入院时间：2025-09-09 10:41", "bbox": [582, 177, 851, 195]},
	{"text": "记录时间：2025-09-09 11:01", "bbox": [582, 205, 851, 223]},
	{"text": "病史陈述者", "bbox": [580, 234, 688, 252]},
	{"text": "联系人姓名：", "bbox": [580, 261, 696, 280]},
	{"text": "联系人电话：", "bbox": [580, 289, 696, 308]},
	{"text": "病史真实性确认签字：", "bbox": [575, 317, 776, 336]},
	{"text": "主诉：咳嗽3+月，发现右上肺占位10+天", "bbox": [107, 342, 484, 362]},
	{"text": "现病史：入院前3+月，患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。10+天前，患", "bbox": [68, 369, 598, 415]},
	{"text": "民医院就诊，完善胸部CT", "bbox": [728, 401, 947, 419]},
	{"text": "提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑", "bbox": [68, 423, 945, 446]},
	{"text": "占位性病变，肺Ca可能性大。建议结合临床进一步检查。2.双肺散在点结影及条索影。3.纵隔内可见", "bbox": [68, 450, 945, 473]},
	{"text": "淋巴结显示，部分稍大。4.心脏形态大小未见异常。5.双侧胸腔未见确切积液征象。6.扫及肝右叶见", "bbox": [68, 477, 945, 500]},
	{"text": "片状密度低影，长径约2.7cm，性质?建议进一步检查。7.扫及胸椎多个椎体骨质密度减低破坏改", "bbox": [68, 505, 945, 528]},
	{"text": "变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+", "bbox": [68, 532, 942, 555]},
	{"text": "NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段", "bbox": [68, 559, 942, 582]},
	{"text": "测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺", "bbox": [68, 586, 942, 609]},
	{"text": "另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分", "bbox": [68, 613, 940, 636]},
	{"text": "稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，", "bbox": [68, 640, 925, 663]},
	{"text": "必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破", "bbox": [68, 667, 940, 690]},
	{"text": "坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.电轴左偏。建议完善经皮肺穿刺", "bbox": [68, 694, 938, 717]},
	{"text": "检查后纤支镜下肺活检明确，患方商议后表示拒绝，现患者为进一步明确占位性质，遂于我院门诊就", "bbox": [68, 721, 938, 744]},
	{"text": "诊，门诊以“右上肺占位”收入我科。", "bbox": [68, 748, 394, 767]},
	{"text": "自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。", "bbox": [107, 775, 805, 795]},
	{"text": "既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病", "bbox": [107, 802, 935, 825]},
	{"text": "史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。", "bbox": [68, 829, 705, 850]},
	{"text": "过敏史：否认食物、药物过敏史。", "bbox": [107, 856, 396, 875]},
	{"text": "个人史：出生原籍，长期居住生长于当地，否认疫区居住治游史，平素偶有饮酒，否认吸烟及", "bbox": [107, 883, 933, 905]}
]
2026-08-10 15:40:00,155 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=16.0s
2026-08-10 15:40:00,155 INFO     29 [qwen-vl-text] coord item[0]: text=入院记录, bbox=[433, 93, 590, 113]
2026-08-10 15:40:00,155 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[177, 146, 275, 165]
2026-08-10 15:40:00,155 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[177, 174, 308, 193]
2026-08-10 15:40:00,155 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：38岁, bbox=[177, 202, 327, 221]
2026-08-10 15:40:00,155 INFO     29 [qwen-vl-text] coord item[4]: text=婚姻状况：已婚, bbox=[177, 230, 327, 249]
2026-08-10 15:40:00,155 INFO     29 [qwen-vl-text] coord item[5]: text=出生地：, bbox=[177, 258, 275, 277]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[6]: text=民族：汉族, bbox=[177, 286, 329, 305]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[7]: text=现住址：, bbox=[177, 314, 275, 333]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[8]: text=职业：自由职业者, bbox=[582, 149, 795, 167]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[9]: text=入院时间：2025-09-09 10:41, bbox=[582, 177, 851, 195]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[10]: text=记录时间：2025-09-09 11:01, bbox=[582, 205, 851, 223]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[11]: text=病史陈述者, bbox=[580, 234, 688, 252]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[12]: text=联系人姓名：, bbox=[580, 261, 696, 280]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[13]: text=联系人电话：, bbox=[580, 289, 696, 308]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[14]: text=病史真实性确认签字：, bbox=[575, 317, 776, 336]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：咳嗽3+月，发现右上肺占位10+天, bbox=[107, 342, 484, 362]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：入院前3+月，患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。10+天前，患, bbox=[68, 369, 598, 415]
2026-08-10 15:40:00,156 INFO     29 [qwen-vl-text] coord item[17]: text=民医院就诊，完善胸部CT, bbox=[728, 401, 947, 419]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[18]: text=提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑, bbox=[68, 423, 945, 446]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[19]: text=占位性病变，肺Ca可能性大。建议结合临床进一步检查。2.双肺散在点结影及条索影。3.纵隔内可见, bbox=[68, 450, 945, 473]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[20]: text=淋巴结显示，部分稍大。4.心脏形态大小未见异常。5.双侧胸腔未见确切积液征象。6.扫及肝右叶见, bbox=[68, 477, 945, 500]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[21]: text=片状密度低影，长径约2.7cm，性质?建议进一步检查。7.扫及胸椎多个椎体骨质密度减低破坏改, bbox=[68, 505, 945, 528]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[22]: text=变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+, bbox=[68, 532, 942, 555]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[23]: text=NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段, bbox=[68, 559, 942, 582]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[24]: text=测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺, bbox=[68, 586, 942, 609]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[25]: text=另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分, bbox=[68, 613, 940, 636]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[26]: text=稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，, bbox=[68, 640, 925, 663]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[27]: text=必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破, bbox=[68, 667, 940, 690]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[28]: text=坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.电轴左偏。建议完善经皮肺穿刺, bbox=[68, 694, 938, 717]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[29]: text=检查后纤支镜下肺活检明确，患方商议后表示拒绝，现患者为进一步明确占位性质，遂于我院门诊就, bbox=[68, 721, 938, 744]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[30]: text=诊，门诊以“右上肺占位”收入我科。, bbox=[68, 748, 394, 767]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[31]: text=自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。, bbox=[107, 775, 805, 795]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[32]: text=既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病, bbox=[107, 802, 935, 825]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[33]: text=史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。, bbox=[68, 829, 705, 850]
2026-08-10 15:40:00,157 INFO     29 [qwen-vl-text] coord item[34]: text=过敏史：否认食物、药物过敏史。, bbox=[107, 856, 396, 875]
2026-08-10 15:40:00,158 INFO     29 [qwen-vl-text] coord item[35]: text=个人史：出生原籍，长期居住生长于当地，否认疫区居住治游史，平素偶有饮酒，否认吸烟及, bbox=[107, 883, 933, 905]
2026-08-10 15:40:00,160 INFO     29 [qwen-vl-text] page=0 — 36/36 coords, api_time=16.0s
2026-08-10 15:40:00,175 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5544723, prompt_len=1568
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["人民医院", "入院记录", "家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。", "体格检查", "T36.1℃", "P92次/分", "R19次/分", "BP121/83mmHg", "一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮", "疹。背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部", "及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。", "颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊", "清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，HR92次/分，律齐，各", "瓣膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性", "浊音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经", "系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。", "专科情况", "背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。胸廓正常，双肺语颤正常，双肺叩诊清", "音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，HR92次/分，律齐，各瓣膜区未闻", "及病理性杂音。", "辅助检查", "2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇", "化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块,", "肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在", "斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低", "密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎", "体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦", "性心律 2.由缺血性"]

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
2026-08-10 15:40:12,022 INFO     29 [qwen-vl-text] coord API raw response (len=2091):
[
	{"text": "人民医院", "bbox": [508, 161, 621, 183]},
	{"text": "入院记录", "bbox": [443, 198, 591, 218]},
	{"text": "家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。", "bbox": [128, 247, 664, 267]},
	{"text": "体格检查", "bbox": [410, 277, 621, 294]},
	{"text": "T36.1℃", "bbox": [187, 302, 257, 318]},
	{"text": "P92次/分", "bbox": [366, 304, 454, 320]},
	{"text": "R19次/分", "bbox": [576, 305, 663, 321]},
	{"text": "BP121/83mmHg", "bbox": [771, 306, 887, 321]},
	{"text": "一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮", "bbox": [146, 329, 933, 349]},
	{"text": "疹。背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部", "bbox": [91, 356, 932, 375]},
	{"text": "及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。", "bbox": [92, 382, 918, 401]},
	{"text": "颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊", "bbox": [92, 408, 930, 427]},
	{"text": "清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，HR92次/分，律齐，各", "bbox": [92, 435, 930, 454]},
	{"text": "瓣膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性", "bbox": [93, 461, 930, 480]},
	{"text": "浊音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经", "bbox": [93, 488, 930, 506]},
	{"text": "系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。", "bbox": [95, 514, 895, 532]},
	{"text": "专科情况", "bbox": [415, 540, 621, 557]},
	{"text": "背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。胸廓正常，双肺语颤正常，双肺叩诊清", "bbox": [135, 566, 927, 584]},
	{"text": "音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，HR92次/分，律齐，各瓣膜区未闻", "bbox": [96, 591, 927, 609]},
	{"text": "及病理性杂音。", "bbox": [96, 618, 222, 635]},
	{"text": "辅助检查", "bbox": [411, 644, 619, 660]},
	{"text": "2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇", "bbox": [145, 669, 927, 687]},
	{"text": "化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块,", "bbox": [97, 695, 914, 713]},
	{"text": "肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在", "bbox": [97, 720, 925, 738]},
	{"text": "斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低", "bbox": [97, 746, 917, 764]},
	{"text": "密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎", "bbox": [97, 772, 916, 790]},
	{"text": "体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦", "bbox": [97, 797, 926, 815]},
	{"text": "性心律 2.由缺血性", "bbox": [97, 825, 261, 838]}
]
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=11.8s
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord item[0]: text=人民医院, bbox=[508, 161, 621, 183]
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[443, 198, 591, 218]
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord item[2]: text=家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。, bbox=[128, 247, 664, 267]
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord item[3]: text=体格检查, bbox=[410, 277, 621, 294]
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord item[4]: text=T36.1℃, bbox=[187, 302, 257, 318]
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord item[5]: text=P92次/分, bbox=[366, 304, 454, 320]
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord item[6]: text=R19次/分, bbox=[576, 305, 663, 321]
2026-08-10 15:40:12,023 INFO     29 [qwen-vl-text] coord item[7]: text=BP121/83mmHg, bbox=[771, 306, 887, 321]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[8]: text=一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮, bbox=[146, 329, 933, 349]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[9]: text=疹。背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部, bbox=[91, 356, 932, 375]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[10]: text=及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。, bbox=[92, 382, 918, 401]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[11]: text=颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊, bbox=[92, 408, 930, 427]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[12]: text=清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，HR92次/分，律齐，各, bbox=[92, 435, 930, 454]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[13]: text=瓣膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性, bbox=[93, 461, 930, 480]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[14]: text=浊音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经, bbox=[93, 488, 930, 506]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[15]: text=系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。, bbox=[95, 514, 895, 532]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[16]: text=专科情况, bbox=[415, 540, 621, 557]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[17]: text=背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。胸廓正常，双肺语颤正常，双肺叩诊清, bbox=[135, 566, 927, 584]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[18]: text=音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，HR92次/分，律齐，各瓣膜区未闻, bbox=[96, 591, 927, 609]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[19]: text=及病理性杂音。, bbox=[96, 618, 222, 635]
2026-08-10 15:40:12,024 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查, bbox=[411, 644, 619, 660]
2026-08-10 15:40:12,025 INFO     29 [qwen-vl-text] coord item[21]: text=2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇, bbox=[145, 669, 927, 687]
2026-08-10 15:40:12,025 INFO     29 [qwen-vl-text] coord item[22]: text=化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块,, bbox=[97, 695, 914, 713]
2026-08-10 15:40:12,025 INFO     29 [qwen-vl-text] coord item[23]: text=肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在, bbox=[97, 720, 925, 738]
2026-08-10 15:40:12,025 INFO     29 [qwen-vl-text] coord item[24]: text=斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低, bbox=[97, 746, 917, 764]
2026-08-10 15:40:12,025 INFO     29 [qwen-vl-text] coord item[25]: text=密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎, bbox=[97, 772, 916, 790]
2026-08-10 15:40:12,025 INFO     29 [qwen-vl-text] coord item[26]: text=体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦, bbox=[97, 797, 926, 815]
2026-08-10 15:40:12,025 INFO     29 [qwen-vl-text] coord item[27]: text=性心律 2.由缺血性, bbox=[97, 825, 261, 838]
2026-08-10 15:40:12,027 INFO     29 [qwen-vl-text] page=1 — 28/28 coords, api_time=11.8s
2026-08-10 15:40:12,027 INFO     29 [qwen-vl-text] new_positions (64):
[[0, 257.7545084228516, 351.2128405761719, 78.29577136230469, 95.13357165527344], [0, 105.36385217285157, 163.7009002685547, 122.91594213867188, 138.9118524169922], [0, 105.36385217285157, 183.34500830078125, 146.4888625488281, 162.48477282714845], [0, 105.36385217285157, 194.65525231933594, 170.06178295898437, 186.05769323730468], [0, 105.36385217285157, 194.65525231933594, 193.63470336914062, 209.63061364746093], [0, 105.36385217285157, 163.7009002685547, 217.20762377929688, 233.2035340576172], [0, 105.36385217285157, 195.84580432128908, 240.7805441894531, 256.7764544677734], [0, 105.36385217285157, 163.7009002685547, 264.35346459960937, 280.3493748779297], [0, 346.45063256835937, 473.24442077636724, 125.44161218261719, 140.59563244628907], [0, 346.45063256835937, 506.5798768310547, 149.01453259277343, 164.1685528564453], [0, 346.45063256835937, 506.5798768310547, 172.5874530029297, 187.74147326660156], [0, 345.26008056640626, 409.549888671875, 197.00226342773436, 212.15628369140626], [0, 345.26008056640626, 414.3120966796875, 219.73329382324218, 235.7292041015625], [0, 345.26008056640626, 414.3120966796875, 243.30621423339844, 259.3021245117188], [0, 342.28370056152346, 461.9341767578125, 266.87913464355466, 282.875044921875], [0, 63.69453210449219, 288.11358447265627, 287.9263850097656, 304.76418530273435], [0, 40.47876806640625, 355.9750485839844, 310.6574154052734, 349.38435607910156], [0, 433.3609287109375, 563.7263729248048, 337.59789587402344, 352.75191613769533], [0, 40.47876806640625, 562.5358209228516, 356.11947619628904, 375.4829465332031], [0, 40.47876806640625, 562.5358209228516, 378.8505065917969, 398.2139769287109], [0, 40.47876806640625, 562.5358209228516, 401.5815369873047, 420.94500732421875], [0, 40.47876806640625, 562.5358209228516, 425.15445739746093, 444.517927734375], [0, 40.47876806640625, 560.7499929199219, 447.8854877929687, 467.2489581298828], [0, 40.47876806640625, 560.7499929199219, 470.61651818847656, 489.97998852539064], [0, 40.47876806640625, 560.7499929199219, 493.34754858398435, 512.7110189208985], [0, 40.47876806640625, 559.5594409179688, 516.0785789794921, 535.4420493164063], [0, 40.47876806640625, 550.6303009033203, 538.809609375, 558.173079711914], [0, 40.47876806640625, 559.5594409179688, 561.5406397705078, 580.9041101074218], [0, 40.47876806640625, 558.3688889160156, 584.2716701660156, 603.6351405029296], [0, 40.47876806640625, 558.3688889160156, 607.0027005615234, 626.3661708984375], [0, 40.47876806640625, 234.53874438476564, 629.7337309570313, 645.7296412353516], [0, 63.69453210449219, 479.19718078613283, 652.4647613525391, 669.3025616455078], [0, 63.69453210449219, 556.583060913086, 675.1957917480469, 694.5592620849609], [0, 40.47876806640625, 419.6695806884766, 697.9268221435547, 715.6065124511719], [0, 63.69453210449219, 235.72929638671877, 720.6578525390624, 736.6537628173828], [0, 63.69453210449219, 555.3925089111328, 743.3888829345703, 761.9104632568359], [1, 302.40020849609374, 369.66639660644535, 135.54429235839842, 154.06587268066406], [1, 263.7072684326172, 351.80811657714844, 166.69422290039063, 183.53202319335938], [1, 76.195328125, 395.26326464843754, 207.94683361816405, 224.7846339111328], [1, 244.06316040039064, 369.66639660644535, 233.2035340576172, 247.51566430664062], [1, 111.31661218261719, 152.98593225097656, 254.25078442382812, 267.72102465820313], [1, 217.8710163574219, 270.25530444335936, 255.934564453125, 269.4048046875], [1, 342.87897656250004, 394.66798864746096, 256.7764544677734, 270.24669470214843], [1, 458.9577967529297, 528.009812866211, 257.6183444824219, 270.24669470214843], [1, 86.91029614257813, 555.3925089111328, 276.9818148193359, 293.8196151123047], [1, 54.17011608886719, 554.7972329101563, 299.71284521484375, 315.70875549316406], [1, 54.76539208984375, 546.4633688964844, 321.6019855957031, 337.59789587402344], [1, 54.76539208984375, 553.6066809082032, 343.4911259765625, 359.4870362548828], [1, 54.76539208984375, 553.6066809082032, 366.2221563720703, 382.2180666503906], [1, 55.36066809082031, 553.6066809082032, 388.11129675292966, 404.10720703124997], [1, 55.36066809082031, 553.6066809082032, 410.8423271484375, 425.99634741210934], [1, 56.55122009277344, 532.7720208740235, 432.7314675292969, 447.8854877929687], [1, 247.03954040527344, 369.66639660644535, 454.62060791015625, 468.9327381591797], [1, 80.36226013183594, 551.8208529052735, 476.5097482910156, 491.6637685546875], [1, 57.14649609375, 551.8208529052735, 497.55699865722653, 512.7110189208985], [1, 57.14649609375, 132.15127221679688, 520.2880290527344, 534.6001593017578], [1, 244.6584364013672, 368.4758446044922, 542.1771694335937, 555.6474096679688], [1, 86.31502014160156, 551.8208529052735, 563.2244197998047, 578.3784400634765], [1, 57.741772094726564, 544.0822648925781, 585.1135601806641, 600.267580444336], [1, 57.741772094726564, 550.6303009033203, 606.160810546875, 621.3148308105468], [1, 57.741772094726564, 545.8680928955079, 628.0499509277344, 643.2039711914063], [1, 57.741772094726564, 545.2728168945313, 649.9390913085938, 665.0931115722656], [1, 57.741772094726564, 551.2255769042969, 670.9863416748046, 686.1403619384765], [1, 57.741772094726564, 155.3670362548828, 694.5592620849609, 705.5038322753907]]
2026-08-10 15:40:12,028 INFO     29 [qwen-vl-text] ═══ DONE ═══ 64 positions, pages=2, time=45.2s
2026-08-10 15:40:12,028 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:40:12,030 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:40:12,030 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 15:40:12,030 INFO     29 [qwen-vl-text] positions(69): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:40:12,030 INFO     29 [qwen-vl-text] page grouping: [12, 13], lines per page: [40, 29]
2026-08-10 15:40:12,326 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:40:12,608 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:40:12,609 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1840
2026-08-10 15:40:12,609 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:40:12,609 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 636, \"bbox_end\": 704, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "入院记录\n姓名：\n性别：男\n年龄：\n婚姻状况：未婚\n出生地：\n民族：汉族\n现住址：\n职业：自由职业者\n入院时间：2026-03-23 10:38\n记录时间：2026-03-23 10:46\n病史陈述者：\n联系人姓名：\n联系人电话：\n病史真实性确认签字：\n主诉：右肺上叶腺癌4周期化疗后1+月。\n现病史：2025-06患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未\n行治疗，病程中患者上述症状持续存在。\n民医院就诊，完善胸部CT提示“1.右上肺见\n团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca\n可能性大。3.纵隔内可见淋巴结显示，部分稍大。扫及肝右叶见片状密度低影，长径约2.7cm，性\n质？，扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住\n院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性\n烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑，行胸部增强CT检查示：右肺上\n叶团块，肿瘤占位性病变可能，其它待排。纵膈见多发淋巴结显示，部分稍大。肝右叶低密度结节，\n占位性病变可能，转移灶待排，扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性\n骨质破坏，转移灶可能，T2椎体病理性骨折可能。于2025-09-10行经皮肺穿刺活检，免疫组化结果电\n话询问病理科腺癌可能性大，2025-09-15报告回示：病理诊断（右肺包块，穿刺活检）结合免疫组化\n结果：癌细胞CK（+），CK7（+），TTF-1（+），NapsinA（+），Ki67（+，约60%），CK20（-），\nSATB2（-），支持肺腺癌。基因检查示：EGFR L858R+,MET 扩增，ERBB2 扩增，TP53突变，PD-L1<\n1%。于2025-09-24开始口服阿美替尼靶向治疗（110mg po qd）。2025-12-04复查胸腹部增强CT：病\n情评价好转。于2025-12-5、2025-12-30、2026-1-23、2026-02-05行4周期AC方案化疗联合靶向治\n疗，具体：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w+阿美替尼 110mg qd。现患者为进一\n步治疗于我院就诊，门诊以“右肺上叶腺癌”收入我科。\n自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。\n既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病\n史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。\n过敏史：否认食物、药物过敏史。\n个人史：出生原籍，长期居住生长于当地，否认疫区居住冶游史，平素偶有饮酒，否认吸烟及\n第1页\n入院记录\n其他不良嗜好。\n婚育史：适龄结婚，育有1子，家人均体健。\n家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。\n体格检查\nT36.4℃\nP95次/分\nR19次/分\nBP101/77mmHg\n一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮\n疹。背部可触及一大约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部\n及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。\n颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊\n清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，H95次/分，律齐，各瓣\n膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊\n音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经\n系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。\n专科情况\nECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰\n音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。\n辅助检查\n暂缺。\n初步诊断：\n1.右肺上叶腺癌伴肝脏、骨多发转移（\ncT4N2M1 IVB期 EGFR L858R+）\n2.肝继发恶性肿瘤\n3.骨继发恶性肿瘤\n医师签名\n第2页",
    "role": "user"
  }
]
2026-08-10 15:40:12,611 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:40:12.611+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:40:27,321 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:40:27,321 INFO     29 [qwen-vl-text] LLM output (len=2857):
{
  "encounter_date": "2026-03-23",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": null,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "未婚",
  "dm_occupation": "自由职业者",
  "dm_admission_time": "2026-03-23 10:38",
  "dm_record_time": "2026-03-23 10:46",
  "dm_history_provider": null,
  "cc_text": "右肺上叶腺癌4周期化疗后1+月。",
  "cc_main_symptoms": [
    "右肺上叶腺癌"
  ],
  "cc_duration": "4周期化疗后1+月",
  "pi_text": "2025-06患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。民医院就诊，完善胸部CT提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca可能性大。3.纵隔内可见淋巴结显示，部分稍大。扫及肝右叶见片状密度低影，长径约2.7cm，性质？，扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑，行胸部增强CT检查示：右肺上叶团块，肿瘤占位性病变可能，其它待排。纵膈见多发淋巴结显示，部分稍大。肝右叶低密度结节，占位性病变可能，转移灶待排，扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病理科腺癌可能性大，2025-09-15报告回示：病理诊断（右肺包块，穿刺活检）结合免疫组化结果：癌细胞CK（+），CK7（+），TTF-1（+），NapsinA（+），Ki67（+，约60%），CK20（-），SATB2（-），支持肺腺癌。基因检查示：EGFR L858R+,MET 扩增，ERBB2 扩增，TP53突变，PD-L1<1%。于2025-09-24开始口服阿美替尼靶向治疗（110mg po qd）。2025-12-04复查胸腹部增强CT：病情评价好转。于2025-12-5、2025-12-30、2026-1-23、2026-02-05行4周期AC方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w+阿美替尼 110mg qd。现患者为进一步治疗于我院就诊，门诊以“右肺上叶腺癌”收入我科。自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。",
  "pmh_disease_history": [
    "否认糖尿病病史",
    "否认高血压病史",
    "否认高血脂病史",
    "否认结核病史",
    "否认肝炎病史",
    "否认精神病史"
  ],
  "pmh_allergy_history": [
    "否认食物过敏史",
    "否认药物过敏史"
  ],
  "pmh_surgery_trauma_history": [
    "否认重大外伤史",
    "否认手术史"
  ],
  "ph_smoking": "否认吸烟",
  "ph_drinking": "平素偶有饮酒",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": "育有1子",
  "fh_text": "否认家族性遗传病、精神病史，否认家族性肿瘤病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.4,
  "vs_pulse_bpm": 95,
  "vs_respiration_rpm": 19,
  "vs_systolic_bp_mmhg": 101,
  "vs_diastolic_bp_mmhg": 77,
  "pe_general_condition": "发育正常，体型消瘦，步入病房，神志清醒，查体合作。",
  "pe_skin_mucosa": "无黄染皮疹。背部可触及一大约2cm*1cm包块，质稍硬，活动度差。",
  "pe_lymph_nodes": "浅表淋巴结未扪及肿大。",
  "pe_lungs": "胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。",
  "pe_heart": "心界不大，H95次/分，律齐，各瓣膜区未闻及病理性杂音。",
  "pe_abdomen": "腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊音，肠鸣音正常。",
  "pe_extremities": "脊柱、四肢无异常。双下肢不肿。",
  "pe_nervous_system": "腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。",
  "pe_specialist_exam": "ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。",
  "pe_ecog_score": 1,
  "pat_text": "暂缺。",
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "肝继发恶性肿瘤",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "骨继发恶性肿瘤",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 15:40:27,321 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-23]
2026-08-10 15:40:27,326 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2265397, prompt_len=1948
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["入院记录", "姓名：", "性别：男", "年龄：", "婚姻状况：未婚", "出生地：", "民族：汉族", "现住址：", "职业：自由职业者", "入院时间：2026-03-23 10:38", "记录时间：2026-03-23 10:46", "病史陈述者：", "联系人姓名：", "联系人电话：", "病史真实性确认签字：", "主诉：右肺上叶腺癌4周期化疗后1+月。", "现病史：2025-06患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未", "行治疗，病程中患者上述症状持续存在。", "民医院就诊，完善胸部CT提示“1.右上肺见", "团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca", "可能性大。3.纵隔内可见淋巴结显示，部分稍大。扫及肝右叶见片状密度低影，长径约2.7cm，性", "质？，扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住", "院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性", "烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑，行胸部增强CT检查示：右肺上", "叶团块，肿瘤占位性病变可能，其它待排。纵膈见多发淋巴结显示，部分稍大。肝右叶低密度结节，", "占位性病变可能，转移灶待排，扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性", "骨质破坏，转移灶可能，T2椎体病理性骨折可能。于2025-09-10行经皮肺穿刺活检，免疫组化结果电", "话询问病理科腺癌可能性大，2025-09-15报告回示：病理诊断（右肺包块，穿刺活检）结合免疫组化", "结果：癌细胞CK（+），CK7（+），TTF-1（+），NapsinA（+），Ki67（+，约60%），CK20（-），", "SATB2（-），支持肺腺癌。基因检查示：EGFR L858R+,MET 扩增，ERBB2 扩增，TP53突变，PD-L1<", "1%。于2025-09-24开始口服阿美替尼靶向治疗（110mg po qd）。2025-12-04复查胸腹部增强CT：病", "情评价好转。于2025-12-5、2025-12-30、2026-1-23、2026-02-05行4周期AC方案化疗联合靶向治", "疗，具体：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w+阿美替尼 110mg qd。现患者为进一", "步治疗于我院就诊，门诊以“右肺上叶腺癌”收入我科。", "自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。", "既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病", "史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。", "过敏史：否认食物、药物过敏史。", "个人史：出生原籍，长期居住生长于当地，否认疫区居住冶游史，平素偶有饮酒，否认吸烟及", "第1页"]

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
2026-08-10 15:40:44,293 INFO     29 [qwen-vl-text] coord API raw response (len=2960):
[
	{"text": "入院记录", "bbox": [435, 85, 577, 106]},
	{"text": "姓名：", "bbox": [187, 141, 273, 157]},
	{"text": "性别：男", "bbox": [187, 165, 303, 181]},
	{"text": "年龄：", "bbox": [187, 190, 273, 206]},
	{"text": "婚姻状况：未婚", "bbox": [187, 215, 323, 231]},
	{"text": "出生地：", "bbox": [187, 240, 273, 257]},
	{"text": "民族：汉族", "bbox": [187, 265, 323, 281]},
	{"text": "现住址：", "bbox": [183, 290, 273, 306]},
	{"text": "职业：自由职业者", "bbox": [600, 135, 775, 151]},
	{"text": "入院时间：2026-03-23 10:38", "bbox": [580, 160, 834, 176]},
	{"text": "记录时间：2026-03-23 10:46", "bbox": [580, 185, 834, 201]},
	{"text": "病史陈述者：", "bbox": [580, 210, 688, 227]},
	{"text": "联系人姓名：", "bbox": [580, 236, 688, 252]},
	{"text": "联系人电话：", "bbox": [580, 261, 688, 277]},
	{"text": "病史真实性确认签字：", "bbox": [562, 287, 748, 303]},
	{"text": "主诉：右肺上叶腺癌4周期化疗后1+月。", "bbox": [123, 315, 475, 331]},
	{"text": "现病史：2025-06患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未", "bbox": [118, 338, 942, 355]},
	{"text": "行治疗，病程中患者上述症状持续存在。", "bbox": [76, 364, 424, 380]},
	{"text": "民医院就诊，完善胸部CT提示“1.右上肺见", "bbox": [570, 363, 951, 379]},
	{"text": "团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca", "bbox": [70, 388, 955, 404]},
	{"text": "可能性大。3.纵隔内可见淋巴结显示，部分稍大。扫及肝右叶见片状密度低影，长径约2.7cm，性", "bbox": [64, 413, 959, 429]},
	{"text": "质？，扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住", "bbox": [58, 438, 960, 455]},
	{"text": "院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性", "bbox": [55, 464, 960, 481]},
	{"text": "烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑，行胸部增强CT检查示：右肺上", "bbox": [54, 490, 959, 507]},
	{"text": "叶团块，肿瘤占位性病变可能，其它待排。纵膈见多发淋巴结显示，部分稍大。肝右叶低密度结节，", "bbox": [55, 516, 946, 533]},
	{"text": "占位性病变可能，转移灶待排，扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性", "bbox": [60, 544, 957, 563]},
	{"text": "骨质破坏，转移灶可能，T2椎体病理性骨折可能。于2025-09-10行经皮肺穿刺活检，免疫组化结果电", "bbox": [62, 572, 955, 590]},
	{"text": "话询问病理科腺癌可能性大，2025-09-15报告回示：病理诊断（右肺包块，穿刺活检）结合免疫组化", "bbox": [65, 599, 954, 617]},
	{"text": "结果：癌细胞CK（+），CK7（+），TTF-1（+），NapsinA（+），Ki67（+，约60%），CK20（-），", "bbox": [67, 627, 940, 645]},
	{"text": "SATB2（-），支持肺腺癌。基因检查示：EGFR L858R+,MET 扩增，ERBB2 扩增，TP53突变，PD-L1<", "bbox": [67, 655, 950, 673]},
	{"text": "1%。于2025-09-24开始口服阿美替尼靶向治疗（110mg po qd）。2025-12-04复查胸腹部增强CT：病", "bbox": [70, 682, 950, 701]},
	{"text": "情评价好转。于2025-12-5、2025-12-30、2026-1-23、2026-02-05行4周期AC方案化疗联合靶向治", "bbox": [70, 710, 949, 728]},
	{"text": "疗，具体：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w+阿美替尼 110mg qd。现患者为进一", "bbox": [70, 737, 949, 756]},
	{"text": "步治疗于我院就诊，门诊以“右肺上叶腺癌”收入我科。", "bbox": [72, 763, 559, 781]},
	{"text": "自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。", "bbox": [113, 790, 819, 809]},
	{"text": "既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病", "bbox": [111, 817, 944, 837]},
	{"text": "史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。", "bbox": [74, 844, 718, 864]},
	{"text": "过敏史：否认食物、药物过敏史。", "bbox": [111, 869, 400, 888]},
	{"text": "个人史：出生原籍，长期居住生长于当地，否认疫区居住冶游史，平素偶有饮酒，否认吸烟及", "bbox": [111, 897, 947, 918]},
	{"text": "第1页", "bbox": [477, 928, 548, 944]}
]
2026-08-10 15:40:44,294 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=17.0s
2026-08-10 15:40:44,294 INFO     29 [qwen-vl-text] coord item[0]: text=入院记录, bbox=[435, 85, 577, 106]
2026-08-10 15:40:44,294 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[187, 141, 273, 157]
2026-08-10 15:40:44,294 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[187, 165, 303, 181]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：, bbox=[187, 190, 273, 206]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[4]: text=婚姻状况：未婚, bbox=[187, 215, 323, 231]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[5]: text=出生地：, bbox=[187, 240, 273, 257]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[6]: text=民族：汉族, bbox=[187, 265, 323, 281]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[7]: text=现住址：, bbox=[183, 290, 273, 306]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[8]: text=职业：自由职业者, bbox=[600, 135, 775, 151]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[9]: text=入院时间：2026-03-23 10:38, bbox=[580, 160, 834, 176]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[10]: text=记录时间：2026-03-23 10:46, bbox=[580, 185, 834, 201]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[11]: text=病史陈述者：, bbox=[580, 210, 688, 227]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[12]: text=联系人姓名：, bbox=[580, 236, 688, 252]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[13]: text=联系人电话：, bbox=[580, 261, 688, 277]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[14]: text=病史真实性确认签字：, bbox=[562, 287, 748, 303]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：右肺上叶腺癌4周期化疗后1+月。, bbox=[123, 315, 475, 331]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：2025-06患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未, bbox=[118, 338, 942, 355]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[17]: text=行治疗，病程中患者上述症状持续存在。, bbox=[76, 364, 424, 380]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[18]: text=民医院就诊，完善胸部CT提示“1.右上肺见, bbox=[570, 363, 951, 379]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[19]: text=团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca, bbox=[70, 388, 955, 404]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[20]: text=可能性大。3.纵隔内可见淋巴结显示，部分稍大。扫及肝右叶见片状密度低影，长径约2.7cm，性, bbox=[64, 413, 959, 429]
2026-08-10 15:40:44,295 INFO     29 [qwen-vl-text] coord item[21]: text=质？，扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住, bbox=[58, 438, 960, 455]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[22]: text=院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性, bbox=[55, 464, 960, 481]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[23]: text=烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑，行胸部增强CT检查示：右肺上, bbox=[54, 490, 959, 507]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[24]: text=叶团块，肿瘤占位性病变可能，其它待排。纵膈见多发淋巴结显示，部分稍大。肝右叶低密度结节，, bbox=[55, 516, 946, 533]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[25]: text=占位性病变可能，转移灶待排，扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性, bbox=[60, 544, 957, 563]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[26]: text=骨质破坏，转移灶可能，T2椎体病理性骨折可能。于2025-09-10行经皮肺穿刺活检，免疫组化结果电, bbox=[62, 572, 955, 590]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[27]: text=话询问病理科腺癌可能性大，2025-09-15报告回示：病理诊断（右肺包块，穿刺活检）结合免疫组化, bbox=[65, 599, 954, 617]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[28]: text=结果：癌细胞CK（+），CK7（+），TTF-1（+），NapsinA（+），Ki67（+，约60%），CK20（-），, bbox=[67, 627, 940, 645]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[29]: text=SATB2（-），支持肺腺癌。基因检查示：EGFR L858R+,MET 扩增，ERBB2 扩增，TP53突变，PD-L1<, bbox=[67, 655, 950, 673]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[30]: text=1%。于2025-09-24开始口服阿美替尼靶向治疗（110mg po qd）。2025-12-04复查胸腹部增强CT：病, bbox=[70, 682, 950, 701]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[31]: text=情评价好转。于2025-12-5、2025-12-30、2026-1-23、2026-02-05行4周期AC方案化疗联合靶向治, bbox=[70, 710, 949, 728]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[32]: text=疗，具体：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w+阿美替尼 110mg qd。现患者为进一, bbox=[70, 737, 949, 756]
2026-08-10 15:40:44,296 INFO     29 [qwen-vl-text] coord item[33]: text=步治疗于我院就诊，门诊以“右肺上叶腺癌”收入我科。, bbox=[72, 763, 559, 781]
2026-08-10 15:40:44,297 INFO     29 [qwen-vl-text] coord item[34]: text=自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。, bbox=[113, 790, 819, 809]
2026-08-10 15:40:44,297 INFO     29 [qwen-vl-text] coord item[35]: text=既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病, bbox=[111, 817, 944, 837]
2026-08-10 15:40:44,297 INFO     29 [qwen-vl-text] coord item[36]: text=史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。, bbox=[74, 844, 718, 864]
2026-08-10 15:40:44,297 INFO     29 [qwen-vl-text] coord item[37]: text=过敏史：否认食物、药物过敏史。, bbox=[111, 869, 400, 888]
2026-08-10 15:40:44,297 INFO     29 [qwen-vl-text] coord item[38]: text=个人史：出生原籍，长期居住生长于当地，否认疫区居住冶游史，平素偶有饮酒，否认吸烟及, bbox=[111, 897, 947, 918]
2026-08-10 15:40:44,297 INFO     29 [qwen-vl-text] coord item[39]: text=第1页, bbox=[477, 928, 548, 944]
2026-08-10 15:40:44,297 INFO     29 [qwen-vl-text] page=12 — 40/40 coords, api_time=17.0s
2026-08-10 15:40:44,303 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1738372, prompt_len=1324
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["入院记录", "其他不良嗜好。", "婚育史：适龄结婚，育有1子，家人均体健。", "家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。", "体格检查", "T36.4℃", "P95次/分", "R19次/分", "BP101/77mmHg", "一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮", "疹。背部可触及一大约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部", "及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。", "颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊", "清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，H95次/分，律齐，各瓣", "膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊", "音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经", "系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。", "专科情况", "ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰", "音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。", "辅助检查", "暂缺。", "初步诊断：", "1.右肺上叶腺癌伴肝脏、骨多发转移（", "cT4N2M1 IVB期 EGFR L858R+）", "2.肝继发恶性肿瘤", "3.骨继发恶性肿瘤", "医师签名", "第2页"]

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
2026-08-10 15:40:54,775 INFO     29 [qwen-vl-text] coord API raw response (len=1892):
[
	{"text": "入院记录", "bbox": [425, 55, 571, 76]},
	{"text": "其他不良嗜好。", "bbox": [65, 108, 193, 124]},
	{"text": "婚育史：适龄结婚，育有1子，家人均体健。", "bbox": [106, 136, 484, 152]},
	{"text": "家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。", "bbox": [107, 163, 652, 179]},
	{"text": "体格检查", "bbox": [393, 190, 594, 206]},
	{"text": "T36.4℃", "bbox": [167, 219, 235, 234]},
	{"text": "P95次/分", "bbox": [349, 218, 439, 234]},
	{"text": "R19次/分", "bbox": [566, 218, 656, 234]},
	{"text": "BP101/77mmHg", "bbox": [770, 219, 888, 235]},
	{"text": "一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮", "bbox": [126, 245, 925, 262]},
	{"text": "疹。背部可触及一大约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部", "bbox": [72, 272, 928, 289]},
	{"text": "及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。", "bbox": [73, 299, 915, 316]},
	{"text": "颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊", "bbox": [72, 326, 930, 343]},
	{"text": "清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，H95次/分，律齐，各瓣", "bbox": [72, 353, 935, 370]},
	{"text": "膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊", "bbox": [72, 380, 937, 397]},
	{"text": "音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经", "bbox": [70, 407, 925, 423]},
	{"text": "系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。", "bbox": [69, 434, 904, 450]},
	{"text": "专科情况", "bbox": [370, 461, 570, 477]},
	{"text": "ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰", "bbox": [103, 487, 948, 504]},
	{"text": "音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。", "bbox": [64, 514, 630, 530]},
	{"text": "辅助检查", "bbox": [393, 541, 594, 557]},
	{"text": "暂缺。", "bbox": [111, 568, 160, 584]},
	{"text": "初步诊断：", "bbox": [481, 622, 570, 638]},
	{"text": "1.右肺上叶腺癌伴肝脏、骨多发转移（", "bbox": [521, 651, 872, 668]},
	{"text": "cT4N2M1 IVB期 EGFR L858R+）", "bbox": [480, 678, 748, 695]},
	{"text": "2.肝继发恶性肿瘤", "bbox": [520, 707, 685, 724]},
	{"text": "3.骨继发恶性肿瘤", "bbox": [520, 735, 685, 752]},
	{"text": "医师签名", "bbox": [480, 763, 560, 779]},
	{"text": "第2页", "bbox": [471, 932, 542, 950]}
]
2026-08-10 15:40:54,775 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=10.5s
2026-08-10 15:40:54,775 INFO     29 [qwen-vl-text] coord item[0]: text=入院记录, bbox=[425, 55, 571, 76]
2026-08-10 15:40:54,775 INFO     29 [qwen-vl-text] coord item[1]: text=其他不良嗜好。, bbox=[65, 108, 193, 124]
2026-08-10 15:40:54,775 INFO     29 [qwen-vl-text] coord item[2]: text=婚育史：适龄结婚，育有1子，家人均体健。, bbox=[106, 136, 484, 152]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[3]: text=家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。, bbox=[107, 163, 652, 179]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[4]: text=体格检查, bbox=[393, 190, 594, 206]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[5]: text=T36.4℃, bbox=[167, 219, 235, 234]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[6]: text=P95次/分, bbox=[349, 218, 439, 234]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[7]: text=R19次/分, bbox=[566, 218, 656, 234]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[8]: text=BP101/77mmHg, bbox=[770, 219, 888, 235]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[9]: text=一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮, bbox=[126, 245, 925, 262]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[10]: text=疹。背部可触及一大约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部, bbox=[72, 272, 928, 289]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[11]: text=及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。, bbox=[73, 299, 915, 316]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[12]: text=颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊, bbox=[72, 326, 930, 343]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[13]: text=清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，H95次/分，律齐，各瓣, bbox=[72, 353, 935, 370]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[14]: text=膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊, bbox=[72, 380, 937, 397]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[15]: text=音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经, bbox=[70, 407, 925, 423]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[16]: text=系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。, bbox=[69, 434, 904, 450]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[17]: text=专科情况, bbox=[370, 461, 570, 477]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[18]: text=ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰, bbox=[103, 487, 948, 504]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[19]: text=音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。, bbox=[64, 514, 630, 530]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查, bbox=[393, 541, 594, 557]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[21]: text=暂缺。, bbox=[111, 568, 160, 584]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[22]: text=初步诊断：, bbox=[481, 622, 570, 638]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[23]: text=1.右肺上叶腺癌伴肝脏、骨多发转移（, bbox=[521, 651, 872, 668]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[24]: text=cT4N2M1 IVB期 EGFR L858R+）, bbox=[480, 678, 748, 695]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[25]: text=2.肝继发恶性肿瘤, bbox=[520, 707, 685, 724]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[26]: text=3.骨继发恶性肿瘤, bbox=[520, 735, 685, 752]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[27]: text=医师签名, bbox=[480, 763, 560, 779]
2026-08-10 15:40:54,776 INFO     29 [qwen-vl-text] coord item[28]: text=第2页, bbox=[471, 932, 542, 950]
2026-08-10 15:40:54,777 INFO     29 [qwen-vl-text] page=13 — 29/29 coords, api_time=10.5s
2026-08-10 15:40:54,777 INFO     29 [qwen-vl-text] new_positions (69):
[[12, 258.9450604248047, 343.47425256347657, 71.56065124511719, 89.24034155273438], [12, 111.31661218261719, 162.51034826660157, 118.70649206542969, 132.17673229980468], [12, 111.31661218261719, 180.36862829589845, 138.9118524169922, 152.38209265136717], [12, 111.31661218261719, 162.51034826660157, 159.95910278320312, 173.42934301757813], [12, 111.31661218261719, 192.2741483154297, 181.00635314941405, 194.47659338378907], [12, 111.31661218261719, 162.51034826660157, 202.05360351562499, 216.36573376464844], [12, 111.31661218261719, 192.2741483154297, 223.10085388183595, 236.57109411621093], [12, 108.93550817871095, 162.51034826660157, 244.14810424804688, 257.6183444824219], [12, 357.1656005859375, 461.338900756836, 113.65515197753906, 127.12539221191406], [12, 345.26008056640626, 496.46018481445316, 134.70240234375, 148.172642578125], [12, 345.26008056640626, 496.46018481445316, 155.74965270996094, 169.21989294433592], [12, 345.26008056640626, 409.549888671875, 176.79690307617187, 191.1090333251953], [12, 345.26008056640626, 409.549888671875, 198.68604345703125, 212.15628369140626], [12, 345.26008056640626, 409.549888671875, 219.73329382324218, 233.2035340576172], [12, 334.5451125488281, 445.26644873046877, 241.62243420410155, 255.09267443847656], [12, 73.21894812011719, 282.7561004638672, 265.19535461425784, 278.6655948486328], [12, 70.24256811523438, 560.7499929199219, 284.55882495117186, 298.8709552001953], [12, 45.24097607421875, 252.3970244140625, 306.44796533203123, 319.91820556640624], [12, 339.30732055664066, 566.107476928711, 305.6060753173828, 319.07631555175783], [12, 41.669320068359376, 568.4885809326172, 326.6533256835937, 340.12356591796873], [12, 38.0976640625, 570.8696849365234, 347.7005760498047, 361.1708162841797], [12, 34.52600805664063, 571.4649609375, 368.74782641601564, 383.05995666503907], [12, 32.74018005371094, 571.4649609375, 390.636966796875, 404.94909704589844], [12, 32.144904052734375, 570.8696849365234, 412.5261071777344, 426.8382374267578], [12, 32.74018005371094, 563.1310969238282, 434.41524755859376, 448.7273778076172], [12, 35.71656005859375, 569.6791329345704, 457.98816796875, 473.98407824707033], [12, 36.90711206054688, 568.4885809326172, 481.5610883789062, 496.7151086425781], [12, 38.69294006347656, 567.8933049316406, 504.29211877441406, 519.4461390380859], [12, 39.88349206542969, 559.5594409179688, 527.8650391845703, 543.0190594482422], [12, 39.88349206542969, 565.5122009277344, 551.4379595947265, 566.5919798583984], [12, 41.669320068359376, 565.5122009277344, 574.1689899902344, 590.1649002685547], [12, 41.669320068359376, 564.9169249267578, 597.7419104003906, 612.8959306640625], [12, 41.669320068359376, 564.9169249267578, 620.4729407958985, 636.4688510742187], [12, 42.859872070312505, 332.7592845458984, 642.3620811767578, 657.5161014404297], [12, 67.26618811035156, 487.5310447998047, 665.0931115722656, 681.0890218505859], [12, 66.07563610839844, 561.940544921875, 687.8241419677735, 704.6619422607422], [12, 44.05042407226563, 427.4081687011719, 710.5551723632813, 727.39297265625], [12, 66.07563610839844, 238.11040039062502, 731.6024227294922, 747.5983330078125], [12, 66.07563610839844, 563.7263729248048, 755.1753431396485, 772.8550334472657], [12, 283.9466524658203, 326.21124853515624, 781.27393359375, 794.744173828125], [13, 252.99230041503907, 339.9025965576172, 46.30395080566406, 63.98364111328125], [13, 38.69294006347656, 114.88826818847657, 90.92412158203125, 104.39436181640625], [13, 63.09925610351563, 288.11358447265627, 114.4970419921875, 127.9672822265625], [13, 63.69453210449219, 388.1199526367188, 137.2280723876953, 150.69831262207032], [13, 233.94346838378908, 353.59394458007813, 159.95910278320312, 173.42934301757813], [13, 99.41109216308594, 139.8898602294922, 184.37391320800782, 197.00226342773436], [13, 207.75132434082033, 261.32616442871097, 183.53202319335938, 197.00226342773436], [13, 336.9262165527344, 390.501056640625, 183.53202319335938, 197.00226342773436], [13, 458.3625207519531, 528.6050888671875, 184.37391320800782, 197.8441534423828], [13, 75.00477612304688, 550.6303009033203, 206.2630535888672, 220.57518383789062], [13, 42.859872070312505, 552.41612890625, 228.994083984375, 243.30621423339844], [13, 43.45514807128907, 544.6775408935547, 251.7251143798828, 266.03724462890625], [13, 42.859872070312505, 553.6066809082032, 274.4561447753906, 288.76827502441404], [13, 42.859872070312505, 556.583060913086, 297.18717517089846, 311.4993054199219], [13, 42.859872070312505, 557.773612915039, 319.91820556640624, 334.23033581542967], [13, 41.669320068359376, 550.6303009033203, 342.64923596191403, 356.11947619628904], [13, 41.074044067382815, 538.1295048828125, 365.3802663574219, 378.8505065917969], [13, 220.25212036132814, 339.30732055664066, 388.11129675292966, 401.5815369873047], [13, 61.31342810058594, 564.3216489257812, 410.00043713378903, 424.3125673828125], [13, 38.0976640625, 375.0238806152344, 432.7314675292969, 446.2017077636719], [13, 233.94346838378908, 353.59394458007813, 455.46249792480467, 468.9327381591797], [13, 66.07563610839844, 95.24416015625, 478.1935283203125, 491.6637685546875], [13, 286.3277564697266, 339.30732055664066, 523.6555891113281, 537.1258293457031], [13, 310.1387965087891, 519.0806728515626, 548.0703995361328, 562.3825297851563], [13, 285.73248046875, 445.26644873046877, 570.8014299316407, 585.1135601806641], [13, 309.5435205078125, 407.7640606689453, 595.2162403564453, 609.5283706054687], [13, 309.5435205078125, 407.7640606689453, 618.7891607666015, 633.101291015625], [13, 285.73248046875, 333.354560546875, 642.3620811767578, 655.8323214111329], [13, 280.3749964599609, 322.63959252929686, 784.6414936523438, 799.7955139160156]]
2026-08-10 15:40:54,777 INFO     29 [qwen-vl-text] ═══ DONE ═══ 69 positions, pages=2, time=42.7s
2026-08-10 15:40:54,789 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 15:40:54,789 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:Admission | outputs={"chunks": "2 items, types={'AdmissionRecord': 2}", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:40:54,790 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 15:40:54,791 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:40:54.790+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:40:54,798 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:40:54,799 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:40:54,800 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:40:54,800 INFO     29 [qwen-vl-text] positions(37): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:40:54,800 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [36, 1]
2026-08-10 15:40:55,093 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:40:55,320 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:40:55,321 INFO     29 [qwen-vl-text] LLM extraction start, text_len=635
2026-08-10 15:40:55,321 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:40:55,321 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 95, \"bbox_end\": 131, \"encounter_dates\": [\"2025-09-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "医学影像检查报告单\n住院\n检查号：\n患者姓名：\n性别：男\n患者年龄：38岁\n申请科室：\n床号：\n设备名称：CT1(联影CT)(1住)\n检查部位：[*胸部,增强]\n联系电话：\n检查技师：\n检查时间：2025-09-01 08:34:37\n报告时间：2025/9/1 9:31:33\n描述：\n右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截\n断，较大层面范围约7.9cm×6.9cm，增强扫描呈轻度不均匀强化，周围\n见斑条影及小结节影。双肺另见长径约0.4-0.6cm实性小结节。右肺中\n叶及双肺下叶见散在斑条影。纵膈见多发淋巴结显示，部分稍大。心脏\n不大，心包少量积液。左侧胸膜稍增厚。肝右叶见数个类圆形低密度\n影，较大者长径约2.5cm，增强扫描两期强化程度CT值相差25HU。扫及\n双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破\n坏，T2椎体见多发骨折线影。\n总结意见：\n1、右肺上叶团块，肿瘤占位性病变可能，其它待排。\n2、双肺另见小结节，必要时随诊。\n3、右肺中叶及双肺下叶见散在斑条影。\n4、纵膈见多发淋巴结显示，部分稍大。\n5、心包少量积液。左侧胸膜稍增厚。\n6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步\n检查。\n7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨\n性骨质破坏，转移灶可能，T2椎体病理性骨折可能。\n请结合临床及其它检查，必要时复查或进一步检查。\n报告者：申悦\n审核医师：马婉军\n页 尾页",
    "role": "user"
  }
]
2026-08-10 15:41:00,456 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:41:00,457 INFO     29 [qwen-vl-text] LLM output (len=772):
{
  "exam_date": "2025-09-01",
  "report_date": "2025-09-01",
  "exam_name": "胸部CT增强",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约7.9cm×6.9cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影。双肺另见长径约0.4-0.6cm实性小结节。右肺中叶及双肺下叶见散在斑条影。纵膈见多发淋巴结显示，部分稍大。心脏不大，心包少量积液。左侧胸膜稍增厚。肝右叶见数个类圆形低密度影，较大者长径约2.5cm，增强扫描两期强化程度CT值相差25HU。扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，T2椎体见多发骨折线影。",
  "conclusion": "1、右肺上叶团块，肿瘤占位性病变可能，其它待排。\n2、双肺另见小结节，必要时随诊。\n3、右肺中叶及双肺下叶见散在斑条影。\n4、纵膈见多发淋巴结显示，部分稍大。\n5、心包少量积液。左侧胸膜稍增厚。\n6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。\n7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。\n请结合临床及其它检查，必要时复查或进一步检查。",
  "physician": "申悦",
  "reviewer": "马婉军"
}
2026-08-10 15:41:00,460 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2148001, prompt_len=1351
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["医学影像检查报告单", "住院", "检查号：", "患者姓名：", "性别：男", "患者年龄：38岁", "申请科室：", "床号：", "设备名称：CT1(联影CT)(1住)", "检查部位：[*胸部,增强]", "联系电话：", "检查技师：", "检查时间：2025-09-01 08:34:37", "报告时间：2025/9/1 9:31:33", "描述：", "右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截", "断，较大层面范围约7.9cm×6.9cm，增强扫描呈轻度不均匀强化，周围", "见斑条影及小结节影。双肺另见长径约0.4-0.6cm实性小结节。右肺中", "叶及双肺下叶见散在斑条影。纵膈见多发淋巴结显示，部分稍大。心脏", "不大，心包少量积液。左侧胸膜稍增厚。肝右叶见数个类圆形低密度", "影，较大者长径约2.5cm，增强扫描两期强化程度CT值相差25HU。扫及", "双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破", "坏，T2椎体见多发骨折线影。", "总结意见：", "1、右肺上叶团块，肿瘤占位性病变可能，其它待排。", "2、双肺另见小结节，必要时随诊。", "3、右肺中叶及双肺下叶见散在斑条影。", "4、纵膈见多发淋巴结显示，部分稍大。", "5、心包少量积液。左侧胸膜稍增厚。", "6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步", "检查。", "7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨", "性骨质破坏，转移灶可能，T2椎体病理性骨折可能。", "请结合临床及其它检查，必要时复查或进一步检查。", "报告者：申悦", "审核医师：马婉军"]

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
2026-08-10 15:41:12,625 INFO     29 [qwen-vl-text] coord API raw response (len=2221):
[
	{"text": "医学影像检查报告单", "bbox": [300, 100, 632, 129]},
	{"text": "住院", "bbox": [71, 132, 110, 148]},
	{"text": "检查号：", "bbox": [615, 135, 680, 151], "bbox": [615, 135, 680, 151]},
	{"text": "患者姓名：", "bbox": [82, 156, 156, 171]},
	{"text": "性别：男", "bbox": [379, 154, 474, 170]},
	{"text": "患者年龄：38岁", "bbox": [592, 156, 761, 172]},
	{"text": "申请科室：", "bbox": [84, 173, 164, 188]},
	{"text": "床号：", "bbox": [379, 173, 425, 188]},
	{"text": "设备名称：CT1(联影CT)(1住)", "bbox": [592, 175, 855, 192]},
	{"text": "检查部位：[*胸部,增强]", "bbox": [84, 190, 302, 207]},
	{"text": "联系电话：", "bbox": [84, 210, 165, 225]},
	{"text": "检查技师：", "bbox": [591, 210, 674, 225]},
	{"text": "检查时间：2025-09-01 08:34:37", "bbox": [84, 238, 384, 254]},
	{"text": "报告时间：2025/9/1 9:31:33", "bbox": [544, 241, 804, 257]},
	{"text": "描述：", "bbox": [87, 273, 136, 289]},
	{"text": "右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截", "bbox": [132, 302, 846, 320]},
	{"text": "断，较大层面范围约7.9cm×6.9cm，增强扫描呈轻度不均匀强化，周围", "bbox": [84, 320, 845, 338]},
	{"text": "见斑条影及小结节影。双肺另见长径约0.4-0.6cm实性小结节。右肺中", "bbox": [84, 338, 832, 356]},
	{"text": "叶及双肺下叶见散在斑条影。纵膈见多发淋巴结显示，部分稍大。心脏", "bbox": [81, 355, 848, 373]},
	{"text": "不大，心包少量积液。左侧胸膜稍增厚。肝右叶见数个类圆形低密度", "bbox": [82, 372, 822, 390]},
	{"text": "影，较大者长径约2.5cm，增强扫描两期强化程度CT值相差25HU。扫及", "bbox": [80, 389, 837, 407]},
	{"text": "双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破", "bbox": [80, 406, 850, 424]},
	{"text": "坏，T2椎体见多发骨折线影。", "bbox": [79, 423, 389, 441]},
	{"text": "总结意见：", "bbox": [71, 553, 164, 570]},
	{"text": "1、右肺上叶团块，肿瘤占位性病变可能，其它待排。", "bbox": [71, 596, 647, 614]},
	{"text": "2、双肺另见小结节，必要时随诊。", "bbox": [71, 613, 450, 631]},
	{"text": "3、右肺中叶及双肺下叶见散在斑条影。", "bbox": [71, 630, 498, 649]},
	{"text": "4、纵膈见多发淋巴结显示，部分稍大。", "bbox": [71, 648, 498, 666]},
	{"text": "5、心包少量积液。左侧胸膜稍增厚。", "bbox": [71, 666, 474, 684]},
	{"text": "6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步", "bbox": [69, 684, 848, 704]},
	{"text": "检查。", "bbox": [68, 703, 128, 720]},
	{"text": "7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨", "bbox": [68, 720, 848, 741]},
	{"text": "性骨质破坏，转移灶可能，T2椎体病理性骨折可能。", "bbox": [68, 738, 638, 758]},
	{"text": "请结合临床及其它检查，必要时复查或进一步检查。", "bbox": [65, 774, 637, 794]},
	{"text": "报告者：申悦", "bbox": [62, 840, 197, 857]},
	{"text": "审核医师：马婉军", "bbox": [553, 838, 716, 858]}
]
2026-08-10 15:41:12,625 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=12.2s
2026-08-10 15:41:12,625 INFO     29 [qwen-vl-text] coord item[0]: text=医学影像检查报告单, bbox=[300, 100, 632, 129]
2026-08-10 15:41:12,625 INFO     29 [qwen-vl-text] coord item[1]: text=住院, bbox=[71, 132, 110, 148]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[2]: text=检查号：, bbox=[615, 135, 680, 151]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[3]: text=患者姓名：, bbox=[82, 156, 156, 171]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[379, 154, 474, 170]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[5]: text=患者年龄：38岁, bbox=[592, 156, 761, 172]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[6]: text=申请科室：, bbox=[84, 173, 164, 188]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[7]: text=床号：, bbox=[379, 173, 425, 188]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[8]: text=设备名称：CT1(联影CT)(1住), bbox=[592, 175, 855, 192]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[9]: text=检查部位：[*胸部,增强], bbox=[84, 190, 302, 207]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[10]: text=联系电话：, bbox=[84, 210, 165, 225]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[11]: text=检查技师：, bbox=[591, 210, 674, 225]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[12]: text=检查时间：2025-09-01 08:34:37, bbox=[84, 238, 384, 254]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[13]: text=报告时间：2025/9/1 9:31:33, bbox=[544, 241, 804, 257]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[14]: text=描述：, bbox=[87, 273, 136, 289]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[15]: text=右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截, bbox=[132, 302, 846, 320]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[16]: text=断，较大层面范围约7.9cm×6.9cm，增强扫描呈轻度不均匀强化，周围, bbox=[84, 320, 845, 338]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[17]: text=见斑条影及小结节影。双肺另见长径约0.4-0.6cm实性小结节。右肺中, bbox=[84, 338, 832, 356]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[18]: text=叶及双肺下叶见散在斑条影。纵膈见多发淋巴结显示，部分稍大。心脏, bbox=[81, 355, 848, 373]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[19]: text=不大，心包少量积液。左侧胸膜稍增厚。肝右叶见数个类圆形低密度, bbox=[82, 372, 822, 390]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[20]: text=影，较大者长径约2.5cm，增强扫描两期强化程度CT值相差25HU。扫及, bbox=[80, 389, 837, 407]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[21]: text=双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破, bbox=[80, 406, 850, 424]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[22]: text=坏，T2椎体见多发骨折线影。, bbox=[79, 423, 389, 441]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[23]: text=总结意见：, bbox=[71, 553, 164, 570]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[24]: text=1、右肺上叶团块，肿瘤占位性病变可能，其它待排。, bbox=[71, 596, 647, 614]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[25]: text=2、双肺另见小结节，必要时随诊。, bbox=[71, 613, 450, 631]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[26]: text=3、右肺中叶及双肺下叶见散在斑条影。, bbox=[71, 630, 498, 649]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[27]: text=4、纵膈见多发淋巴结显示，部分稍大。, bbox=[71, 648, 498, 666]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[28]: text=5、心包少量积液。左侧胸膜稍增厚。, bbox=[71, 666, 474, 684]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[29]: text=6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步, bbox=[69, 684, 848, 704]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[30]: text=检查。, bbox=[68, 703, 128, 720]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[31]: text=7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨, bbox=[68, 720, 848, 741]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[32]: text=性骨质破坏，转移灶可能，T2椎体病理性骨折可能。, bbox=[68, 738, 638, 758]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[33]: text=请结合临床及其它检查，必要时复查或进一步检查。, bbox=[65, 774, 637, 794]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[34]: text=报告者：申悦, bbox=[62, 840, 197, 857]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] coord item[35]: text=审核医师：马婉军, bbox=[553, 838, 716, 858]
2026-08-10 15:41:12,626 INFO     29 [qwen-vl-text] page=3 — 36/36 coords, api_time=12.2s
2026-08-10 15:41:12,634 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3878881, prompt_len=619
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["页 尾页"]

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
2026-08-10 15:41:14,175 INFO     29 [qwen-vl-text] coord API raw response (len=60):
```json
[
	{"text": "页 尾页", "bbox": [0, 255, 60, 270]}
]
```
2026-08-10 15:41:14,175 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 15:41:14,175 INFO     29 [qwen-vl-text] coord item[0]: text=页 尾页, bbox=[0, 255, 60, 270]
2026-08-10 15:41:14,176 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=1.5s
2026-08-10 15:41:14,177 INFO     29 [qwen-vl-text] new_positions (37):
[[3, 178.58280029296876, 376.2144326171875, 84.18900146484376, 108.60381188964844], [3, 42.26459606933594, 65.48036010742187, 111.12948193359375, 124.59972216796875], [3, 366.09474060058596, 404.7876806640625, 113.65515197753906, 127.12539221191406], [3, 48.812632080078124, 92.86305615234376, 131.33484228515624, 143.9631925048828], [3, 225.6096043701172, 282.1608244628906, 129.6510622558594, 143.12130249023437], [3, 352.403392578125, 453.00503674316406, 131.33484228515624, 144.80508251953125], [3, 50.003184082031254, 97.62526416015625, 145.6469725341797, 158.27532275390624], [3, 225.6096043701172, 252.99230041503907, 145.6469725341797, 158.27532275390624], [3, 352.403392578125, 508.96098083496094, 147.33075256347655, 161.6428828125], [3, 50.003184082031254, 179.7733522949219, 159.95910278320312, 174.27123303222655], [3, 50.003184082031254, 98.22054016113282, 176.79690307617187, 189.42525329589844], [3, 351.80811657714844, 401.21602465820314, 176.79690307617187, 189.42525329589844], [3, 50.003184082031254, 228.585984375, 200.36982348632813, 213.8400637207031], [3, 323.83014453125, 478.60190478515625, 202.89549353027343, 216.36573376464844], [3, 51.78901208496094, 80.9575361328125, 229.83597399902342, 243.30621423339844], [3, 78.57643212890625, 503.6034968261719, 254.25078442382812, 269.4048046875], [3, 50.003184082031254, 503.00822082519534, 269.4048046875, 284.55882495117186], [3, 50.003184082031254, 495.26963281250005, 284.55882495117186, 299.71284521484375], [3, 48.21735607910156, 504.794048828125, 298.8709552001953, 314.0249754638672], [3, 48.812632080078124, 489.3168728027344, 313.18308544921877, 328.3371057128906], [3, 47.622080078125, 498.24601281738285, 327.4952156982422, 342.64923596191403], [3, 47.622080078125, 505.98460083007814, 341.8073459472656, 356.9613662109375], [3, 47.02680407714844, 231.5623643798828, 356.11947619628904, 371.27349645996094], [3, 42.26459606933594, 97.62526416015625, 465.5651781005859, 479.8773083496094], [3, 42.26459606933594, 385.143572631836, 501.76644873046877, 516.9204689941406], [3, 42.26459606933594, 267.87420043945315, 516.0785789794921, 531.232599243164], [3, 42.26459606933594, 296.44744848632814, 530.3907092285157, 546.3866195068359], [3, 42.26459606933594, 296.44744848632814, 545.5447294921875, 560.6987497558594], [3, 42.26459606933594, 282.1608244628906, 560.6987497558594, 575.8527700195312], [3, 41.074044067382815, 504.794048828125, 575.8527700195312, 592.6905703125], [3, 40.47876806640625, 76.195328125, 591.8486802978515, 606.160810546875], [3, 40.47876806640625, 504.794048828125, 606.160810546875, 623.8405008544922], [3, 40.47876806640625, 379.7860886230469, 621.3148308105468, 638.1526311035157], [3, 38.69294006347656, 379.1908126220703, 651.6228713378906, 668.4606716308593], [3, 36.90711206054688, 117.26937219238282, 707.1876123046875, 721.4997425537109], [3, 329.1876285400391, 426.21761669921875, 705.5038322753907, 722.3416325683594], [4, 0.0, 35.71656005859375, 214.68195373535156, 227.31030395507813]]
2026-08-10 15:41:14,177 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=2, time=19.4s
2026-08-10 15:41:14,177 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:41:14,178 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:41:14,178 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:41:14,178 INFO     29 [qwen-vl-text] positions(24): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:41:14,179 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [24]
2026-08-10 15:41:14,402 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:41:14,404 INFO     29 [qwen-vl-text] LLM extraction start, text_len=257
2026-08-10 15:41:14,404 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:41:14,404 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 133, \"bbox_end\": 156, \"encounter_dates\": [\"2025-09-10\", \"2025-09-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "住院号\n门诊号：-\n病理号[\n姓名\n性别 男\n年龄 38岁\n病人编号\n病区\n就诊号\n收到日期 2025-09-10\n送检科室\n送检单位 本院\n送检医生\n标本名称 右肺包块\n临床诊断\n肉眼所见\n(右肺包块)灰白色组织多粒,直径0.4cm,点纸全\n病理诊断\n(右肺包块,穿刺活检)结合免疫组化结果:癌细胞CK(+),CK7(+),TTF-1(+),NapsinA(+),Ki67(+,约60%),CK20(-),SATB2(-),\n支持肺腺癌。\n报告医生 阙柳\n审核医生 阙柳\n复诊医生\n报告时间 2025-09-15",
    "role": "user"
  }
]
2026-08-10 15:41:18,800 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:41:18,800 INFO     29 [qwen-vl-text] LLM output (len=443):
{
  "exam_date": "2025-09-10",
  "report_date": "2025-09-15",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "右肺包块",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "肉眼所见\n(右肺包块)灰白色组织多粒,直径0.4cm,点纸全",
  "conclusion": "病理诊断\n(右肺包块,穿刺活检)结合免疫组化结果:癌细胞CK(+),CK7(+),TTF-1(+),NapsinA(+),Ki67(+,约60%),CK20(-),SATB2(-),\n支持肺腺癌。",
  "physician": "阙柳",
  "reviewer": "阙柳"
}
2026-08-10 15:41:18,809 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3878881, prompt_len=942
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["住院号", "门诊号：-", "病理号[", "姓名", "性别 男", "年龄 38岁", "病人编号", "病区", "就诊号", "收到日期 2025-09-10", "送检科室", "送检单位 本院", "送检医生", "标本名称 右肺包块", "临床诊断", "肉眼所见", "(右肺包块)灰白色组织多粒,直径0.4cm,点纸全", "病理诊断", "(右肺包块,穿刺活检)结合免疫组化结果:癌细胞CK(+),CK7(+),TTF-1(+),NapsinA(+),Ki67(+,约60%),CK20(-),SATB2(-),", "支持肺腺癌。", "报告医生 阙柳", "审核医生 阙柳", "复诊医生", "报告时间 2025-09-15"]

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
2026-08-10 15:41:27,956 INFO     29 [qwen-vl-text] coord API raw response (len=1790):
[
	{"text": "住院号", "bbox": [304, 278, 357, 295]},
	{"text": "门诊号：-", "bbox": [800, 281, 875, 298]},
	{"text": "病理号[", "bbox": [395, 307, 469, 326]},
	{"text": "姓名", "bbox": [10, 325, 25, 338], "bbox": [10, 325, 25, 338]},
	{"text": "性别 男", "bbox": [260, 328, 319, 342]},
	{"text": "年龄 38岁", "bbox": [508, 330, 637, 344]},
	{"text": "病人编号", "bbox": [752, 330, 809, 343]},
	{"text": "病区", "bbox": [10, 344, 25, 357], "bbox": [10, 344, 25, 357]},
	{"text": "就诊号", "bbox": [260, 346, 305, 359], "bbox": [260, 346, 305, 359]},
	{"text": "收到日期 2025-09-10", "bbox": [508, 348, 680, 361]},
	{"text": "送检科室", "bbox": [10, 361, 70, 373], "bbox": [10, 361, 70, 373]},
	{"text": "送检单位 本院", "bbox": [260, 363, 392, 376], "bbox": [260, 363, 392, 376]},
	{"text": "送检医生", "bbox": [508, 365, 564, 377], "bbox": [508, 365, 564, 377]},
	{"text": "标本名称 右肺包块", "bbox": [10, 373, 171, 386], "bbox": [10, 373, 171, 386]},
	{"text": "临床诊断", "bbox": [10, 385, 70, 397], "bbox": [10, 385, 70, 397]},
	{"text": "肉眼所见", "bbox": [10, 401, 70, 413], "bbox": [10, 401, 70, 413]},
	{"text": "(右肺包块)灰白色组织多粒,直径0.4cm,点纸全", "bbox": [17, 416, 338, 429], "bbox": [17, 416, 338, 429]},
	{"text": "病理诊断", "bbox": [10, 437, 70, 449], "bbox": [10, 437, 70, 449]},
	{"text": "(右肺包块,穿刺活检)结合免疫组化结果:癌细胞CK(+),CK7(+),TTF-1(+),NapsinA(+),Ki67(+,约60%),CK20(-),SATB2(-),", "bbox": [17, 452, 972, 465], "bbox": [17, 452, 972, 465]},
	{"text": "支持肺腺癌。", "bbox": [14, 463, 92, 475], "bbox": [14, 463, 92, 475]},
	{"text": "报告医生 阙柳", "bbox": [14, 485, 135, 498], "bbox": [14, 485, 135, 498]},
	{"text": "审核医生 阙柳", "bbox": [204, 486, 322, 499], "bbox": [204, 486, 322, 499]},
	{"text": "复诊医生", "bbox": [389, 487, 446, 499], "bbox": [389, 487, 446, 499]},
	{"text": "报告时间 2025-09-15", "bbox": [571, 487, 729, 499], "bbox": [571, 487, 729, 499]}
]
2026-08-10 15:41:27,957 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=9.1s
2026-08-10 15:41:27,957 INFO     29 [qwen-vl-text] coord item[0]: text=住院号, bbox=[304, 278, 357, 295]
2026-08-10 15:41:27,957 INFO     29 [qwen-vl-text] coord item[1]: text=门诊号：-, bbox=[800, 281, 875, 298]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[2]: text=病理号[, bbox=[395, 307, 469, 326]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[10, 325, 25, 338]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[4]: text=性别 男, bbox=[260, 328, 319, 342]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[5]: text=年龄 38岁, bbox=[508, 330, 637, 344]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[6]: text=病人编号, bbox=[752, 330, 809, 343]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[7]: text=病区, bbox=[10, 344, 25, 357]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[8]: text=就诊号, bbox=[260, 346, 305, 359]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[9]: text=收到日期 2025-09-10, bbox=[508, 348, 680, 361]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[10]: text=送检科室, bbox=[10, 361, 70, 373]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[11]: text=送检单位 本院, bbox=[260, 363, 392, 376]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[12]: text=送检医生, bbox=[508, 365, 564, 377]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[13]: text=标本名称 右肺包块, bbox=[10, 373, 171, 386]
2026-08-10 15:41:27,958 INFO     29 [qwen-vl-text] coord item[14]: text=临床诊断, bbox=[10, 385, 70, 397]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[15]: text=肉眼所见, bbox=[10, 401, 70, 413]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[16]: text=(右肺包块)灰白色组织多粒,直径0.4cm,点纸全, bbox=[17, 416, 338, 429]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[17]: text=病理诊断, bbox=[10, 437, 70, 449]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[18]: text=(右肺包块,穿刺活检)结合免疫组化结果:癌细胞CK(+),CK7(+),TTF-1(+),NapsinA(+),Ki67(+,约60%),CK20(-),SATB2(-),, bbox=[17, 452, 972, 465]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[19]: text=支持肺腺癌。, bbox=[14, 463, 92, 475]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[20]: text=报告医生 阙柳, bbox=[14, 485, 135, 498]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[21]: text=审核医生 阙柳, bbox=[204, 486, 322, 499]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[22]: text=复诊医生, bbox=[389, 487, 446, 499]
2026-08-10 15:41:27,959 INFO     29 [qwen-vl-text] coord item[23]: text=报告时间 2025-09-15, bbox=[571, 487, 729, 499]
2026-08-10 15:41:27,960 INFO     29 [qwen-vl-text] page=4 — 24/24 coords, api_time=9.1s
2026-08-10 15:41:27,961 INFO     29 [qwen-vl-text] new_positions (24):
[[4, 180.963904296875, 212.51353234863282, 234.04542407226563, 248.35755432128906], [4, 476.22080078125003, 520.8665008544922, 236.57109411621093, 250.88322436523438], [4, 235.1340203857422, 279.1844444580078, 258.4602344970703, 274.4561447753906], [4, 5.952760009765625, 14.881900024414064, 273.6142547607422, 284.55882495117186], [4, 154.77176025390625, 189.89304431152345, 276.1399248046875, 287.9263850097656], [4, 302.40020849609374, 379.1908126220703, 277.8237048339844, 289.6101650390625], [4, 447.64755273437504, 481.5782847900391, 277.8237048339844, 288.76827502441404], [4, 5.952760009765625, 14.881900024414064, 289.6101650390625, 300.55473522949217], [4, 154.77176025390625, 181.55918029785158, 291.2939450683594, 302.23851525878905], [4, 302.40020849609374, 404.7876806640625, 292.9777250976562, 303.92229528808593], [4, 5.952760009765625, 41.669320068359376, 303.92229528808593, 314.0249754638672], [4, 154.77176025390625, 233.3481923828125, 305.6060753173828, 316.5506455078125], [4, 302.40020849609374, 335.7356645507813, 307.2898553466797, 317.39253552246095], [4, 5.952760009765625, 101.7921961669922, 314.0249754638672, 324.9695456542969], [4, 5.952760009765625, 41.669320068359376, 324.1276556396484, 334.23033581542967], [4, 5.952760009765625, 41.669320068359376, 337.59789587402344, 347.7005760498047], [4, 10.119692016601563, 201.20328833007812, 350.22624609375, 361.1708162841797], [4, 5.952760009765625, 41.669320068359376, 367.90593640136717, 378.0086165771484], [4, 10.119692016601563, 578.6082729492188, 380.53428662109377, 391.4788568115234], [4, 8.333864013671874, 54.76539208984375, 389.79507678222654, 399.8977569580078], [4, 8.333864013671874, 80.36226013183594, 408.3166571044922, 419.26122729492187], [4, 121.43630419921875, 191.67887231445314, 409.1585471191406, 420.1031173095703], [4, 231.5623643798828, 265.4930964355469, 410.00043713378903, 420.1031173095703], [4, 339.9025965576172, 433.9562047119141, 410.00043713378903, 420.1031173095703]]
2026-08-10 15:41:27,961 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=13.8s
2026-08-10 15:41:27,961 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:41:27,963 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:41:27,963 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:41:27,963 INFO     29 [qwen-vl-text] positions(280): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:41:27,964 INFO     29 [qwen-vl-text] page grouping: [5, 6], lines per page: [86, 194]
2026-08-10 15:41:28,138 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:41:28,291 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:41:28,294 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2227
2026-08-10 15:41:28,294 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:41:28,295 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 158, \"bbox_end\": 437, \"encounter_dates\": [\"2025-09-18\", \"2025-09-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "检测概览\n基本信息\n受检者信息\n样本信息\n临床信息\n姓名\n样本编号：\n临床/病理诊断：肺癌怀疑骨转移肝转移\n性别：男\n样本类型：石蜡块\n手术史/用药史：/\n年龄：38岁\n采样部位：/\n既往基因检测结果：/\n送检单位\n家族史：/\n采集日期：\n接收日期：2025-09-18\n报告日期：2025-09-21\n本报告中的临床诊断等信息来自受检者送检时提供的信息，而非来自检测结果。\n项目简介\n项目名称\n肺癌靶向18基因检测\n检测方法\n目标区域探针捕获技术和二代测序技术(Next-Generation Sequencing,NGS)\n检测范围\n本检测基于非小细胞肺癌指南和专家共识，检测非小细胞肺癌靶向治疗和预后相关的18个基因(包括：EGFR、ALK、MET、ROS1、BRAF、RET、ERBB2(HER2)、KRAS、NTRK1/2/3、NRAS、PIK3CA、AKT1、FBXW7、DDR2、NRG1、TP53)，变异类型包含相应基因的点突变、插入/缺失，拷贝数变异和基因融合/重排。\n检测流程\n核酸提取、文库制备、高通量测序、生物信息分析及报告解读\n参考指南及数据库\nNCCN指南、CSCO指南、OncoKB、COSMIC、CKB、ClinVar等\n参考基因组\nGRCh37/hg19\n检测结果汇总\n基因变异结果（共5个）\n基因\n转录本/外显子\ncDNA改变\n氨基酸改变\n变异类型\n变异丰度/拷贝数\n变异分类\nEGFR\nNM_005228.5:exon21\nc.2573T>G\np.L858R\n错义突变\n51.28%\nI类[重要临床意义]\nERBB2(HER2)\nNM_004448.4\n/\n/\n拷贝数扩增\n拷贝数=3.6\nI类[重要临床意义]\nMET\nNM_000245.4\n/\n/\n拷贝数扩增\n拷贝数=3.1\nI类[重要临床意义]\nTP53\nNM_000546.6:exon6\nc.598_611del\np.N200Vfs*4\n移码突变\n61.75%\nII类[潜在临床意义]\n第1页\nTP53\nNM_000546.6:exon6\nc.629A>C\np.N210T\n错义突变\n62.88%\nIII类[临床意义不明]\n注：\n《肿瘤二代测序临床报告解读共识》指出，基因变异按照其临床意义的重要性分为4类：\nI类：有重要的临床意义，与治疗、预后和诊断相关；\nII类：有潜在的临床意义，与治疗、预后和诊断相关；\nIII类：临床意义不明(临床意义不明是指目前尚无充分证据证实这些基因变异与肿瘤的致病性关系，尚无相关用药提示，未来可能随着研究的深入而更新致病性及药物证据等级)；\nIV类变异，无害或可能无害。\n本报告只列出I、II、III类变异。\n靶向用药基因检测提示\n靶向用药基因检测提示\n基因\n变异信息\n变异丰度/拷贝数\n(A级)\nFDA/NMPA\n指南推荐用药\n(B级)\n专家共识推荐用药\n(C级)\n跨适应症\n(C级)\n临床试验药物\n(D级)\n临床前研究\n奥希替尼\n(敏感)\n奥希替尼+\n化疗\n(敏感)\n埃万妥单抗+\n兰泽替尼\n(敏感)\n埃万妥单抗+\n化疗\n(敏感)\n阿美替尼\n(敏感)\n伏美替尼\n(敏感)\n达可替尼\n(敏感)\n吉非替尼\n(敏感)\n阿法替尼±\n西妥昔单抗\n(敏感)\n埃克替尼\n(敏感)\n贝福替尼\n(敏感)\n厄洛替尼±\n雷莫西尤单抗\n或贝伐珠单抗\n(敏感)\n瑞厄替尼\n(敏感)\n瑞齐替尼\n德达博妥单抗+\n奥希替尼\n(敏感)\nPatritumab\nDeruxtecan\n(敏感)\nBDTX-1535\n(敏感)\nWSD0922\n(敏感)\nHLX42\n(敏感)\nSHR-A2009\n(敏感)\nBL-B01D1\n(敏感)\n阿美替尼+\n化疗\n(敏感)\nEGFR\nc.2573T>G,\np.L858R,\nExon21\n51.28%\n/\n/\n/\n/\n第 2 页\n(敏感)\n佐利替尼\n(敏感)\n利厄替尼\n(敏感)\n德达博妥单抗\n(敏感)\n芦康沙妥珠单\n抗\n(敏感)\n依沃西单抗+\n培美曲塞+\n卡铂\n(敏感)\n奥希替尼+\n赛沃替尼\n(敏感)\n伯瑞替尼\n(敏感)\n克唑替尼\n(敏感)\n卡马替尼\n(敏感)\n特泊替尼\n(敏感)\nEGFR-TKIs\n(耐药)\n谷美替尼\n(敏感)\nEGFR-TKIs+\nMET-TKIs\n(敏感)\n/\n伯瑞替尼+\nPLB1004\n(敏感)\nSYM015\n(敏感)\n特泊替尼+\n吉非替尼\n(敏感)\n特泊替尼+\n奥希替尼\n(敏感)\n赛沃替尼\n(敏感)\nMET\n扩增\n拷贝数\n=3.1\n/\n德曲妥珠单\n抗\n(敏感)\n泽尼达妥单\n抗\n(敏感)\n帕博利珠单\n抗+\n曲妥珠单抗+\n化疗\n(敏感)\n帕妥珠单抗+\n曲妥珠单抗+\n化疗\n(敏感)\n恩美曲妥珠\n单抗\n(敏感)\n维迪西妥单\n抗\n(敏感)\n吡咯替尼\n(敏感)\n阿法替尼\n(敏感)\n帕妥珠单抗+\n曲妥珠单抗\n(敏感)\n吡咯替尼+\n阿帕替尼\n(敏感)\n维迪西妥单抗+\n替雷利珠单抗+\n贝伐珠单抗\n(敏感)\n维迪西妥单抗+\n安罗替尼\n(敏感)\nERBB2\n(HER2)\n扩增\n拷贝数\n=3.6\nEGFR-TKIs\n(耐药)\n/\nTarloxotinib\n(敏感)\nTAS0728\n(敏感)\nBDTX-189\n(敏感)\nc.598_611del\np.N200Vfs*4\nExon6\n61.75%\n/\n/\n/\nAdavosertib\n(敏感)\nCTX-1\n(敏感)\nCEP-8983\n(敏感)\nTP53",
    "role": "user"
  }
]
2026-08-10 15:41:28,297 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:41:28.296+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:41:41,153 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:41:41,153 INFO     29 [qwen-vl-text] LLM output (len=2346):
{
  "exam_date": "2025-09-18",
  "report_date": "2025-09-21",
  "exam_name": "肺癌靶向18基因检测",
  "exam_category": "pathology",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "基因变异结果（共5个）\n\n| 基因 | 转录本/外显子 | cDNA改变 | 氨基酸改变 | 变异类型 | 变异丰度/拷贝数 | 变异分类 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| EGFR | NM_005228.5:exon21 | c.2573T>G | p.L858R | 错义突变 | 51.28% | I类[重要临床意义] |\n| ERBB2(HER2) | NM_004448.4 | / | / | 拷贝数扩增 | 拷贝数=3.6 | I类[重要临床意义] |\n| MET | NM_000245.4 | / | / | 拷贝数扩增 | 拷贝数=3.1 | I类[重要临床意义] |\n| TP53 | NM_000546.6:exon6 | c.598_611del | p.N200Vfs*4 | 移码突变 | 61.75% | II类[潜在临床意义] |\n| TP53 | NM_000546.6:exon6 | c.629A>C | p.N210T | 错义突变 | 62.88% | III类[临床意义不明] |\n\n注：\n《肿瘤二代测序临床报告解读共识》指出，基因变异按照其临床意义的重要性分为4类：\nI类：有重要的临床意义，与治疗、预后和诊断相关；\nII类：有潜在的临床意义，与治疗、预后和诊断相关；\nIII类：临床意义不明(临床意义不明是指目前尚无充分证据证实这些基因变异与肿瘤的致病性关系，尚无相关用药提示，未来可能随着研究的深入而更新致病性及药物证据等级)；\nIV类变异，无害或可能无害。\n本报告只列出I、II、III类变异。",
  "conclusion": "靶向用药基因检测提示\n\n| 基因 | 变异信息 | 变异丰度/拷贝数 | (A级) | FDA/NMPA 指南推荐用药 (B级) | 专家共识推荐用药 (C级) | 跨适应症 (C级) | 临床试验药物 (D级) | 临床前研究 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| EGFR | c.2573T>G, p.L858R, Exon21 | 51.28% | / | / | 奥希替尼 (敏感), 奥希替尼+化疗 (敏感), 埃万妥单抗+兰泽替尼 (敏感), 埃万妥单抗+化疗 (敏感), 阿美替尼 (敏感), 伏美替尼 (敏感), 达可替尼 (敏感), 吉非替尼 (敏感), 阿法替尼±西妥昔单抗 (敏感), 埃克替尼 (敏感), 贝福替尼 (敏感), 厄洛替尼±雷莫西尤单抗或贝伐珠单抗 (敏感), 瑞厄替尼 (敏感), 瑞齐替尼, 德达博妥单抗+奥希替尼 (敏感), Patritumab Deruxtecan (敏感), BDTX-1535 (敏感), WSD0922 (敏感), HLX42 (敏感), SHR-A2009 (敏感), BL-B01D1 (敏感), 阿美替尼+化疗 (敏感), 佐利替尼 (敏感), 利厄替尼 (敏感), 德达博妥单抗 (敏感), 芦康沙妥珠单抗 (敏感), 依沃西单抗+培美曲塞+卡铂 (敏感) | / | / | / |\n| MET | 扩增 拷贝数=3.1 | / | / | / | 奥希替尼+赛沃替尼 (敏感), 伯瑞替尼 (敏感), 克唑替尼 (敏感), 卡马替尼 (敏感), 特泊替尼 (敏感), EGFR-TKIs (耐药), 谷美替尼 (敏感), EGFR-TKIs+MET-TKIs (敏感), 伯瑞替尼+PLB1004 (敏感), SYM015 (敏感), 特泊替尼+吉非替尼 (敏感), 特泊替尼+奥希替尼 (敏感), 赛沃替尼 (敏感) | / | / | / |\n| ERBB2 (HER2) | 扩增 拷贝数=3.6 | / | / | / | 德曲妥珠单抗 (敏感), 泽尼达妥单抗 (敏感), 帕博利珠单抗+曲妥珠单抗+化疗 (敏感), 帕妥珠单抗+曲妥珠单抗+化疗 (敏感), 恩美曲妥珠单抗 (敏感), 维迪西妥单抗 (敏感), 吡咯替尼 (敏感), 阿法替尼 (敏感), 帕妥珠单抗+曲妥珠单抗 (敏感), 吡咯替尼+阿帕替尼 (敏感), 维迪西妥单抗+替雷利珠单抗+贝伐珠单抗 (敏感), 维迪西妥单抗+安罗替尼 (敏感), EGFR-TKIs (耐药) | / | Tarloxotinib (敏感), TAS0728 (敏感), BDTX-189 (敏感) | / |\n| TP53 | c.598_611del p.N200Vfs*4 Exon6 | 61.75% | / | / | / | / | Adavosertib (敏感), CTX-1 (敏感), CEP-8983 (敏感) | / |",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:41:41,155 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1015928, prompt_len=2002
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共86行）
["检测概览", "基本信息", "受检者信息", "样本信息", "临床信息", "姓名", "样本编号：", "临床/病理诊断：肺癌怀疑骨转移肝转移", "性别：男", "样本类型：石蜡块", "手术史/用药史：/", "年龄：38岁", "采样部位：/", "既往基因检测结果：/", "送检单位", "家族史：/", "采集日期：", "接收日期：2025-09-18", "报告日期：2025-09-21", "本报告中的临床诊断等信息来自受检者送检时提供的信息，而非来自检测结果。", "项目简介", "项目名称", "肺癌靶向18基因检测", "检测方法", "目标区域探针捕获技术和二代测序技术(Next-Generation Sequencing,NGS)", "检测范围", "本检测基于非小细胞肺癌指南和专家共识，检测非小细胞肺癌靶向治疗和预后相关的18个基因(包括：EGFR、ALK、MET、ROS1、BRAF、RET、ERBB2(HER2)、KRAS、NTRK1/2/3、NRAS、PIK3CA、AKT1、FBXW7、DDR2、NRG1、TP53)，变异类型包含相应基因的点突变、插入/缺失，拷贝数变异和基因融合/重排。", "检测流程", "核酸提取、文库制备、高通量测序、生物信息分析及报告解读", "参考指南及数据库", "NCCN指南、CSCO指南、OncoKB、COSMIC、CKB、ClinVar等", "参考基因组", "GRCh37/hg19", "检测结果汇总", "基因变异结果（共5个）", "基因", "转录本/外显子", "cDNA改变", "氨基酸改变", "变异类型", "变异丰度/拷贝数", "变异分类", "EGFR", "NM_005228.5:exon21", "c.2573T>G", "p.L858R", "错义突变", "51.28%", "I类[重要临床意义]", "ERBB2(HER2)", "NM_004448.4", "/", "/", "拷贝数扩增", "拷贝数=3.6", "I类[重要临床意义]", "MET", "NM_000245.4", "/", "/", "拷贝数扩增", "拷贝数=3.1", "I类[重要临床意义]", "TP53", "NM_000546.6:exon6", "c.598_611del", "p.N200Vfs*4", "移码突变", "61.75%", "II类[潜在临床意义]", "第1页", "TP53", "NM_000546.6:exon6", "c.629A>C", "p.N210T", "错义突变", "62.88%", "III类[临床意义不明]", "注：", "《肿瘤二代测序临床报告解读共识》指出，基因变异按照其临床意义的重要性分为4类：", "I类：有重要的临床意义，与治疗、预后和诊断相关；", "II类：有潜在的临床意义，与治疗、预后和诊断相关；", "III类：临床意义不明(临床意义不明是指目前尚无充分证据证实这些基因变异与肿瘤的致病性关系，尚无相关用药提示，未来可能随着研究的深入而更新致病性及药物证据等级)；", "IV类变异，无害或可能无害。", "本报告只列出I、II、III类变异。", "靶向用药基因检测提示"]

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
2026-08-10 15:42:06,704 INFO     29 [qwen-vl-text] coord API raw response (len=4905):
[
	{"text": "检测概览", "bbox": [705, 17, 765, 28]},
	{"text": "基本信息", "bbox": [160, 51, 227, 63]},
	{"text": "受检者信息", "bbox": [168, 75, 230, 86]},
	{"text": "样本信息", "bbox": [370, 75, 420, 86]},
	{"text": "临床信息", "bbox": [601, 75, 651, 86]},
	{"text": "姓名", "bbox": [168, 93, 195, 104]},
	{"text": "样本编号：", "bbox": [370, 93, 426, 104]},
	{"text": "临床/病理诊断：肺癌怀疑骨转移肝转移", "bbox": [601, 93, 817, 104]},
	{"text": "性别：男", "bbox": [168, 110, 217, 120]},
	{"text": "样本类型：石蜡块", "bbox": [370, 110, 472, 120]},
	{"text": "手术史/用药史：/", "bbox": [601, 110, 698, 120]},
	{"text": "年龄：38岁", "bbox": [168, 126, 235, 137]},
	{"text": "采样部位：/", "bbox": [370, 126, 439, 137]},
	{"text": "既往基因检测结果：/", "bbox": [601, 126, 718, 137]},
	{"text": "送检单位", "bbox": [168, 144, 217, 155]},
	{"text": "家族史：/", "bbox": [601, 144, 656, 155]},
	{"text": "采集日期：", "bbox": [168, 162, 224, 173]},
	{"text": "接收日期：2025-09-18", "bbox": [370, 162, 498, 173]},
	{"text": "报告日期：2025-09-21", "bbox": [601, 162, 726, 173]},
	{"text": "本报告中的临床诊断等信息来自受检者送检时提供的信息，而非来自检测结果。", "bbox": [160, 178, 548, 188]},
	{"text": "项目简介", "bbox": [160, 221, 227, 233]},
	{"text": "项目名称", "bbox": [168, 247, 217, 258]},
	{"text": "肺癌靶向18基因检测", "bbox": [282, 247, 403, 258]},
	{"text": "检测方法", "bbox": [168, 267, 217, 278]},
	{"text": "目标区域探针捕获技术和二代测序技术(Next-Generation Sequencing,NGS)", "bbox": [282, 267, 698, 278]},
	{"text": "检测范围", "bbox": [168, 307, 217, 318]},
	{"text": "本检测基于非小细胞肺癌指南和专家共识，检测非小细胞肺癌靶向治疗和预后相关的18个基因(包括：EGFR、ALK、MET、ROS1、BRAF、RET、ERBB2(HER2)、KRAS、NTRK1/2/3、NRAS、PIK3CA、AKT1、FBXW7、DDR2、NRG1、TP53)，变异类型包含相应基因的点突变、插入/缺失，拷贝数变异和基因融合/重排。", "bbox": [282, 284, 817, 343]},
	{"text": "检测流程", "bbox": [168, 349, 217, 360]},
	{"text": "核酸提取、文库制备、高通量测序、生物信息分析及报告解读", "bbox": [282, 349, 618, 360]},
	{"text": "参考指南及数据库", "bbox": [168, 365, 268, 376]},
	{"text": "NCCN指南、CSCO指南、OncoKB、COSMIC、CKB、ClinVar等", "bbox": [282, 365, 642, 376]},
	{"text": "参考基因组", "bbox": [168, 381, 230, 392]},
	{"text": "GRCh37/hg19", "bbox": [282, 381, 362, 392]},
	{"text": "检测结果汇总", "bbox": [160, 430, 257, 442]},
	{"text": "基因变异结果（共5个）", "bbox": [427, 457, 558, 468]},
	{"text": "基因", "bbox": [175, 485, 200, 496]},
	{"text": "转录本/外显子", "bbox": [262, 477, 300, 488]},
	{"text": "cDNA改变", "bbox": [374, 485, 434, 496]},
	{"text": "氨基酸改变", "bbox": [498, 485, 560, 496]},
	{"text": "变异类型", "bbox": [611, 485, 661, 496]},
	{"text": "变异丰度/拷贝数", "bbox": [694, 477, 743, 488]},
	{"text": "变异分类", "bbox": [773, 485, 823, 496]},
	{"text": "EGFR", "bbox": [172, 517, 204, 527]},
	{"text": "NM_005228.5:exon21", "bbox": [240, 510, 323, 535]},
	{"text": "c.2573T>G", "bbox": [372, 517, 436, 527]},
	{"text": "p.L858R", "bbox": [505, 517, 554, 527]},
	{"text": "错义突变", "bbox": [611, 517, 661, 527]},
	{"text": "51.28%", "bbox": [697, 517, 740, 527]},
	{"text": "I类[重要临床意义]", "bbox": [767, 510, 829, 535]},
	{"text": "ERBB2(HER2)", "bbox": [168, 541, 208, 568]},
	{"text": "NM_004448.4", "bbox": [241, 550, 322, 561]},
	{"text": "/", "bbox": [400, 550, 407, 561]},
	{"text": "/", "bbox": [526, 550, 533, 561]},
	{"text": "拷贝数扩增", "bbox": [604, 550, 667, 561]},
	{"text": "拷贝数=3.6", "bbox": [700, 543, 732, 568]},
	{"text": "I类[重要临床意义]", "bbox": [767, 541, 829, 568]},
	{"text": "MET", "bbox": [175, 582, 200, 592]},
	{"text": "NM_000245.4", "bbox": [241, 582, 322, 592]},
	{"text": "/", "bbox": [400, 582, 407, 592]},
	{"text": "/", "bbox": [526, 582, 533, 592]},
	{"text": "拷贝数扩增", "bbox": [604, 582, 667, 592]},
	{"text": "拷贝数=3.1", "bbox": [700, 574, 732, 599]},
	{"text": "I类[重要临床意义]", "bbox": [767, 574, 829, 599]},
	{"text": "TP53", "bbox": [172, 615, 204, 625]},
	{"text": "NM_000546.6:exon6", "bbox": [240, 607, 323, 633]},
	{"text": "c.598_611del", "bbox": [364, 615, 444, 625]},
	{"text": "p.N200Vfs*4", "bbox": [492, 615, 565, 625]},
	{"text": "移码突变", "bbox": [611, 615, 661, 625]},
	{"text": "61.75%", "bbox": [697, 615, 740, 625]},
	{"text": "II类[潜在临床意义]", "bbox": [767, 607, 830, 633]},
	{"text": "第1页", "bbox": [478, 674, 518, 684]},
	{"text": "TP53", "bbox": [172, 793, 204, 803]},
	{"text": "NM_000546.6:exon6", "bbox": [240, 785, 323, 810]},
	{"text": "c.629A>C", "bbox": [377, 793, 431, 803]},
	{"text": "p.N210T", "bbox": [505, 793, 554, 803]},
	{"text": "错义突变", "bbox": [611, 793, 661, 803]},
	{"text": "62.88%", "bbox": [697, 793, 740, 803]},
	{"text": "III类[临床意义不明]", "bbox": [764, 785, 832, 810]},
	{"text": "注：", "bbox": [160, 824, 180, 835]},
	{"text": "《肿瘤二代测序临床报告解读共识》指出，基因变异按照其临床意义的重要性分为4类：", "bbox": [168, 840, 634, 851]},
	{"text": "I类：有重要的临床意义，与治疗、预后和诊断相关；", "bbox": [160, 856, 445, 867]},
	{"text": "II类：有潜在的临床意义，与治疗、预后和诊断相关；", "bbox": [160, 871, 449, 882]},
	{"text": "III类：临床意义不明(临床意义不明是指目前尚无充分证据证实这些基因变异与肿瘤的致病性关系，尚无相关用药提示，未来可能随着研究的深入而更新致病性及药物证据等级)；", "bbox": [160, 888, 832, 914]},
	{"text": "IV类变异，无害或可能无害。", "bbox": [160, 920, 316, 931]},
	{"text": "本报告只列出I、II、III类变异。", "bbox": [160, 936, 327, 947]},
	{"text": "靶向用药基因检测提示", "bbox": [435, 981, 559, 991]}
]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord API: raw_items=86, valid_items=86, elapsed=25.5s
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[0]: text=检测概览, bbox=[705, 17, 765, 28]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[1]: text=基本信息, bbox=[160, 51, 227, 63]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[2]: text=受检者信息, bbox=[168, 75, 230, 86]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[3]: text=样本信息, bbox=[370, 75, 420, 86]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[4]: text=临床信息, bbox=[601, 75, 651, 86]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[168, 93, 195, 104]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[6]: text=样本编号：, bbox=[370, 93, 426, 104]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[7]: text=临床/病理诊断：肺癌怀疑骨转移肝转移, bbox=[601, 93, 817, 104]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[8]: text=性别：男, bbox=[168, 110, 217, 120]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[9]: text=样本类型：石蜡块, bbox=[370, 110, 472, 120]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[10]: text=手术史/用药史：/, bbox=[601, 110, 698, 120]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[11]: text=年龄：38岁, bbox=[168, 126, 235, 137]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[12]: text=采样部位：/, bbox=[370, 126, 439, 137]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[13]: text=既往基因检测结果：/, bbox=[601, 126, 718, 137]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[14]: text=送检单位, bbox=[168, 144, 217, 155]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[15]: text=家族史：/, bbox=[601, 144, 656, 155]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[16]: text=采集日期：, bbox=[168, 162, 224, 173]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[17]: text=接收日期：2025-09-18, bbox=[370, 162, 498, 173]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[18]: text=报告日期：2025-09-21, bbox=[601, 162, 726, 173]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[19]: text=本报告中的临床诊断等信息来自受检者送检时提供的信息，而非来自检测结果。, bbox=[160, 178, 548, 188]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[20]: text=项目简介, bbox=[160, 221, 227, 233]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[21]: text=项目名称, bbox=[168, 247, 217, 258]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[22]: text=肺癌靶向18基因检测, bbox=[282, 247, 403, 258]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[23]: text=检测方法, bbox=[168, 267, 217, 278]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[24]: text=目标区域探针捕获技术和二代测序技术(Next-Generation Sequencing,NGS), bbox=[282, 267, 698, 278]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[25]: text=检测范围, bbox=[168, 307, 217, 318]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[26]: text=本检测基于非小细胞肺癌指南和专家共识，检测非小细胞肺癌靶向治疗和预后相关的18个基因(包括：EGFR、ALK、MET、ROS1、BRAF、RET、ERBB2(HER2)、KRAS、NTRK1/2/3、NRAS、PIK3CA、AKT1、FBXW7、DDR2、NRG1、TP53)，变异类型包含相应基因的点突变、插入/缺失，拷贝数变异和基因融合/重排。, bbox=[282, 284, 817, 343]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[27]: text=检测流程, bbox=[168, 349, 217, 360]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[28]: text=核酸提取、文库制备、高通量测序、生物信息分析及报告解读, bbox=[282, 349, 618, 360]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[29]: text=参考指南及数据库, bbox=[168, 365, 268, 376]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[30]: text=NCCN指南、CSCO指南、OncoKB、COSMIC、CKB、ClinVar等, bbox=[282, 365, 642, 376]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[31]: text=参考基因组, bbox=[168, 381, 230, 392]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[32]: text=GRCh37/hg19, bbox=[282, 381, 362, 392]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[33]: text=检测结果汇总, bbox=[160, 430, 257, 442]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[34]: text=基因变异结果（共5个）, bbox=[427, 457, 558, 468]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[35]: text=基因, bbox=[175, 485, 200, 496]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[36]: text=转录本/外显子, bbox=[262, 477, 300, 488]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[37]: text=cDNA改变, bbox=[374, 485, 434, 496]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[38]: text=氨基酸改变, bbox=[498, 485, 560, 496]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[39]: text=变异类型, bbox=[611, 485, 661, 496]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[40]: text=变异丰度/拷贝数, bbox=[694, 477, 743, 488]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[41]: text=变异分类, bbox=[773, 485, 823, 496]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[42]: text=EGFR, bbox=[172, 517, 204, 527]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[43]: text=NM_005228.5:exon21, bbox=[240, 510, 323, 535]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[44]: text=c.2573T>G, bbox=[372, 517, 436, 527]
2026-08-10 15:42:06,705 INFO     29 [qwen-vl-text] coord item[45]: text=p.L858R, bbox=[505, 517, 554, 527]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[46]: text=错义突变, bbox=[611, 517, 661, 527]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[47]: text=51.28%, bbox=[697, 517, 740, 527]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[48]: text=I类[重要临床意义], bbox=[767, 510, 829, 535]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[49]: text=ERBB2(HER2), bbox=[168, 541, 208, 568]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[50]: text=NM_004448.4, bbox=[241, 550, 322, 561]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[51]: text=/, bbox=[400, 550, 407, 561]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[52]: text=/, bbox=[526, 550, 533, 561]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[53]: text=拷贝数扩增, bbox=[604, 550, 667, 561]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[54]: text=拷贝数=3.6, bbox=[700, 543, 732, 568]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[55]: text=I类[重要临床意义], bbox=[767, 541, 829, 568]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[56]: text=MET, bbox=[175, 582, 200, 592]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[57]: text=NM_000245.4, bbox=[241, 582, 322, 592]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[58]: text=/, bbox=[400, 582, 407, 592]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[59]: text=/, bbox=[526, 582, 533, 592]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[60]: text=拷贝数扩增, bbox=[604, 582, 667, 592]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[61]: text=拷贝数=3.1, bbox=[700, 574, 732, 599]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[62]: text=I类[重要临床意义], bbox=[767, 574, 829, 599]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[63]: text=TP53, bbox=[172, 615, 204, 625]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[64]: text=NM_000546.6:exon6, bbox=[240, 607, 323, 633]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[65]: text=c.598_611del, bbox=[364, 615, 444, 625]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[66]: text=p.N200Vfs*4, bbox=[492, 615, 565, 625]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[67]: text=移码突变, bbox=[611, 615, 661, 625]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[68]: text=61.75%, bbox=[697, 615, 740, 625]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[69]: text=II类[潜在临床意义], bbox=[767, 607, 830, 633]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[70]: text=第1页, bbox=[478, 674, 518, 684]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[71]: text=TP53, bbox=[172, 793, 204, 803]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[72]: text=NM_000546.6:exon6, bbox=[240, 785, 323, 810]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[73]: text=c.629A>C, bbox=[377, 793, 431, 803]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[74]: text=p.N210T, bbox=[505, 793, 554, 803]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[75]: text=错义突变, bbox=[611, 793, 661, 803]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[76]: text=62.88%, bbox=[697, 793, 740, 803]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[77]: text=III类[临床意义不明], bbox=[764, 785, 832, 810]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[78]: text=注：, bbox=[160, 824, 180, 835]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[79]: text=《肿瘤二代测序临床报告解读共识》指出，基因变异按照其临床意义的重要性分为4类：, bbox=[168, 840, 634, 851]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[80]: text=I类：有重要的临床意义，与治疗、预后和诊断相关；, bbox=[160, 856, 445, 867]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[81]: text=II类：有潜在的临床意义，与治疗、预后和诊断相关；, bbox=[160, 871, 449, 882]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[82]: text=III类：临床意义不明(临床意义不明是指目前尚无充分证据证实这些基因变异与肿瘤的致病性关系，尚无相关用药提示，未来可能随着研究的深入而更新致病性及药物证据等级)；, bbox=[160, 888, 832, 914]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[83]: text=IV类变异，无害或可能无害。, bbox=[160, 920, 316, 931]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[84]: text=本报告只列出I、II、III类变异。, bbox=[160, 936, 327, 947]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] coord item[85]: text=靶向用药基因检测提示, bbox=[435, 981, 559, 991]
2026-08-10 15:42:06,706 INFO     29 [qwen-vl-text] page=5 — 86/86 coords, api_time=25.5s
2026-08-10 15:42:06,707 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=737357, prompt_len=2291
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共194行）
["靶向用药基因检测提示", "基因", "变异信息", "变异丰度/拷贝数", "(A级)", "FDA/NMPA", "指南推荐用药", "(B级)", "专家共识推荐用药", "(C级)", "跨适应症", "(C级)", "临床试验药物", "(D级)", "临床前研究", "奥希替尼", "(敏感)", "奥希替尼+", "化疗", "(敏感)", "埃万妥单抗+", "兰泽替尼", "(敏感)", "埃万妥单抗+", "化疗", "(敏感)", "阿美替尼", "(敏感)", "伏美替尼", "(敏感)", "达可替尼", "(敏感)", "吉非替尼", "(敏感)", "阿法替尼±", "西妥昔单抗", "(敏感)", "埃克替尼", "(敏感)", "贝福替尼", "(敏感)", "厄洛替尼±", "雷莫西尤单抗", "或贝伐珠单抗", "(敏感)", "瑞厄替尼", "(敏感)", "瑞齐替尼", "德达博妥单抗+", "奥希替尼", "(敏感)", "Patritumab", "Deruxtecan", "(敏感)", "BDTX-1535", "(敏感)", "WSD0922", "(敏感)", "HLX42", "(敏感)", "SHR-A2009", "(敏感)", "BL-B01D1", "(敏感)", "阿美替尼+", "化疗", "(敏感)", "EGFR", "c.2573T>G,", "p.L858R,", "Exon21", "51.28%", "/", "/", "/", "/", "第 2 页", "(敏感)", "佐利替尼", "(敏感)", "利厄替尼", "(敏感)", "德达博妥单抗", "(敏感)", "芦康沙妥珠单", "抗", "(敏感)", "依沃西单抗+", "培美曲塞+", "卡铂", "(敏感)", "奥希替尼+", "赛沃替尼", "(敏感)", "伯瑞替尼", "(敏感)", "克唑替尼", "(敏感)", "卡马替尼", "(敏感)", "特泊替尼", "(敏感)", "EGFR-TKIs", "(耐药)", "谷美替尼", "(敏感)", "EGFR-TKIs+", "MET-TKIs", "(敏感)", "/", "伯瑞替尼+", "PLB1004", "(敏感)", "SYM015", "(敏感)", "特泊替尼+", "吉非替尼", "(敏感)", "特泊替尼+", "奥希替尼", "(敏感)", "赛沃替尼", "(敏感)", "MET", "扩增", "拷贝数", "=3.1", "/", "德曲妥珠单", "抗", "(敏感)", "泽尼达妥单", "抗", "(敏感)", "帕博利珠单", "抗+", "曲妥珠单抗+", "化疗", "(敏感)", "帕妥珠单抗+", "曲妥珠单抗+", "化疗", "(敏感)", "恩美曲妥珠", "单抗", "(敏感)", "维迪西妥单", "抗", "(敏感)", "吡咯替尼", "(敏感)", "阿法替尼", "(敏感)", "帕妥珠单抗+", "曲妥珠单抗", "(敏感)", "吡咯替尼+", "阿帕替尼", "(敏感)", "维迪西妥单抗+", "替雷利珠单抗+", "贝伐珠单抗", "(敏感)", "维迪西妥单抗+", "安罗替尼", "(敏感)", "ERBB2", "(HER2)", "扩增", "拷贝数", "=3.6", "EGFR-TKIs", "(耐药)", "/", "Tarloxotinib", "(敏感)", "TAS0728", "(敏感)", "BDTX-189", "(敏感)", "c.598_611del", "p.N200Vfs*4", "Exon6", "61.75%", "/", "/", "/", "Adavosertib", "(敏感)", "CTX-1", "(敏感)", "CEP-8983", "(敏感)", "TP53"]

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
2026-08-10 15:42:42,476 INFO     29 [qwen-vl-text] coord API raw response (len=6169):
[
	{"text": "靶向用药基因检测提示", "bbox": [443, 17, 553, 26]},
	{"text": "基因", "bbox": [217, 44, 240, 53],
	"bbox": [281, 44, 325, 53],
	"bbox": [351, 40, 400, 49],
	"bbox": [357, 49, 393, 58],
	"bbox": [435, 35, 464, 44],
	"bbox": [420, 44, 478, 53],
	"bbox": [415, 53, 483, 62],
	"bbox": [517, 35, 544, 44],
	"bbox": [503, 44, 557, 53],
	"bbox": [513, 53, 546, 62],
	"bbox": [588, 39, 617, 48],
	"bbox": [582, 48, 624, 57],
	"bbox": [671, 39, 697, 48],
	"bbox": [651, 48, 715, 57],
	"bbox": [750, 39, 777, 48],
	"bbox": [735, 48, 790, 57],
	"bbox": [428, 67, 472, 76],
	"bbox": [435, 76, 467, 85],
	"bbox": [425, 85, 475, 94],
	"bbox": [438, 94, 464, 103],
	"bbox": [435, 103, 467, 112],
	"bbox": [419, 112, 480, 121],
	"bbox": [428, 121, 472, 130],
	"bbox": [435, 130, 467, 139],
	"bbox": [419, 139, 480, 148],
	"bbox": [438, 148, 464, 157],
	"bbox": [435, 157, 467, 166],
	"bbox": [428, 166, 472, 175],
	"bbox": [435, 175, 467, 184],
	"bbox": [428, 184, 472, 193],
	"bbox": [435, 193, 467, 202],
	"bbox": [428, 202, 472, 211],
	"bbox": [435, 211, 467, 220],
	"bbox": [428, 220, 472, 229],
	"bbox": [435, 229, 467, 238],
	"bbox": [422, 238, 477, 247],
	"bbox": [422, 247, 477, 256],
	"bbox": [435, 256, 467, 265],
	"bbox": [428, 265, 472, 274],
	"bbox": [435, 274, 467, 283],
	"bbox": [428, 283, 472, 292],
	"bbox": [435, 292, 467, 301],
	"bbox": [422, 301, 477, 310],
	"bbox": [417, 310, 482, 319],
	"bbox": [417, 319, 482, 328],
	"bbox": [435, 328, 467, 337],
	"bbox": [428, 337, 472, 346],
	"bbox": [435, 346, 467, 355],
	"bbox": [428, 355, 472, 364],
	"bbox": [647, 131, 718, 140],
	"bbox": [660, 140, 704, 149],
	"bbox": [668, 149, 696, 158],
	"bbox": [654, 158, 711, 167],
	"bbox": [654, 167, 711, 176],
	"bbox": [668, 176, 696, 185],
	"bbox": [655, 185, 710, 194],
	"bbox": [668, 194, 696, 203],
	"bbox": [659, 203, 707, 212],
	"bbox": [668, 212, 696, 221],
	"bbox": [660, 221, 698, 230],
	"bbox": [668, 230, 696, 239],
	"bbox": [655, 239, 710, 248],
	"bbox": [668, 248, 696, 257],
	"bbox": [659, 257, 707, 266],
	"bbox": [668, 266, 696, 275],
	"bbox": [659, 275, 707, 284],
	"bbox": [659, 284, 707, 293],
	"bbox": [671, 293, 693, 302],
	"bbox": [668, 302, 696, 311],
	"bbox": [217, 215, 243, 224],
	"bbox": [272, 206, 329, 215],
	"bbox": [278, 215, 324, 224],
	"bbox": [285, 224, 323, 233],
	"bbox": [357, 215, 395, 224],
	"bbox": [525, 215, 534, 224],
	"bbox": [599, 215, 607, 224],
	"bbox": [760, 215, 767, 224],
	"bbox": [481, 405, 517, 414],
	"bbox": [435, 500, 467, 509],
	"bbox": [428, 509, 472, 518],
	"bbox": [435, 518, 467, 527],
	"bbox": [428, 527, 472, 536],
	"bbox": [435, 536, 467, 545],
	"bbox": [417, 545, 482, 554],
	"bbox": [435, 554, 467, 563],
	"bbox": [417, 563, 482, 572],
	"bbox": [443, 572, 459, 581],
	"bbox": [435, 581, 467, 590],
	"bbox": [419, 590, 480, 600],
	"bbox": [425, 600, 475, 609],
	"bbox": [438, 609, 464, 618],
	"bbox": [435, 618, 467, 627],
	"bbox": [425, 627, 475, 636],
	"bbox": [428, 636, 472, 645],
	"bbox": [435, 645, 467, 654],
	"bbox": [428, 654, 472, 663],
	"bbox": [435, 663, 467, 672],
	"bbox": [428, 672, 472, 681],
	"bbox": [425, 681, 475, 690],
	"bbox": [438, 690, 464, 699],
	"bbox": [428, 699, 472, 708],
	"bbox": [435, 708, 467, 717],
	"bbox": [422, 717, 477, 726],
	"bbox": [435, 726, 467, 735],
	"bbox": [435, 735, 467, 744],
	"bbox": [657, 628, 707, 637],
	"bbox": [660, 637, 704, 646],
	"bbox": [668, 646, 696, 655],
	"bbox": [664, 655, 701, 664],
	"bbox": [657, 664, 707, 673],
	"bbox": [660, 673, 704, 682],
	"bbox": [668, 682, 696, 691],
	"bbox": [660, 691, 704, 700],
	"bbox": [668, 700, 696, 709],
	"bbox": [660, 709, 704, 718],
	"bbox": [668, 718, 696, 727],
	"bbox": [660, 727, 704, 736],
	"bbox": [668, 736, 696, 745],
	"bbox": [217, 685, 240, 694],
	"bbox": [292, 685, 315, 694],
	"bbox": [357, 681, 393, 690],
	"bbox": [364, 690, 387, 699],
	"bbox": [500, 668, 551, 677],
	"bbox": [513, 677, 546, 686],
	"bbox": [500, 686, 557, 695],
	"bbox": [505, 695, 552, 704],
	"bbox": [513, 704, 546, 713],
	"bbox": [599, 685, 607, 694],
	"bbox": [760, 685, 767, 694],
	"bbox": [576, 750, 631, 759],
	"bbox": [594, 759, 610, 768],
	"bbox": [588, 768, 617, 777],
	"bbox": [576, 777, 631, 786],
	"bbox": [594, 786, 610, 795],
	"bbox": [588, 795, 617, 804],
	"bbox": [576, 804, 631, 813],
	"bbox": [594, 813, 610, 822],
	"bbox": [572, 822, 634, 831],
	"bbox": [594, 831, 610, 840],
	"bbox": [572, 840, 634, 849],
	"bbox": [594, 849, 610, 858],
	"bbox": [572, 858, 634, 867],
	"bbox": [594, 867, 610, 876],
	"bbox": [588, 876, 617, 885],
	"bbox": [576, 885, 631, 894],
	"bbox": [594, 894, 610, 903],
	"bbox": [576, 903, 631, 912],
	"bbox": [594, 912, 610, 921],
	"bbox": [576, 921, 631, 930],
	"bbox": [594, 930, 610, 939],
	"bbox": [660, 770, 704, 779],
	"bbox": [668, 779, 696, 788],
	"bbox": [660, 788, 704, 797],
	"bbox": [668, 797, 696, 806],
	"bbox": [654, 806, 711, 815],
	"bbox": [654, 815, 711, 824],
	"bbox": [668, 824, 696, 833],
	"bbox": [660, 833, 704, 842],
	"bbox": [668, 842, 696, 851],
	"bbox": [654, 851, 711, 860],
	"bbox": [668, 860, 696, 869],
	"bbox": [654, 869, 711, 878],
	"bbox": [668, 878, 696, 887],
	"bbox": [668, 887, 696, 896],
	"bbox": [647, 896, 718, 905],
	"bbox": [660, 905, 704, 914],
	"bbox": [668, 914, 696, 923],
	"bbox": [668, 923, 696, 932],
	"bbox": [730, 821, 794, 830],
	"bbox": [750, 830, 777, 839],
	"bbox": [740, 839, 785, 848],
	"bbox": [750, 848, 777, 857],
	"bbox": [737, 857, 788, 866],
	"bbox": [750, 866, 777, 875],
	"bbox": [212, 840, 246, 849],
	"bbox": [212, 849, 246, 858],
	"bbox": [292, 844, 315, 853],
	"bbox": [357, 839, 393, 848],
	"bbox": [364, 848, 387, 857],
	"bbox": [422, 840, 477, 849],
	"bbox": [435, 849, 467, 858],
	"bbox": [525, 844, 534, 853],
	"bbox": [272, 947, 339, 956],
	"bbox": [298, 956, 304, 965],
	"bbox": [272, 965, 337, 974],
	"bbox": [357, 965, 395, 974],
	"bbox": [446, 965, 454, 974],
	"bbox": [525, 965, 534, 974],
	"bbox": [599, 965, 607, 974],
	"bbox": [652, 960, 713, 969],
	"bbox": [668, 969, 696, 978],
	"bbox": [748, 951, 779, 960],
	"bbox": [750, 960, 777, 969],
	"bbox": [739, 969, 787, 978],
	"bbox": [750, 978, 777, 987],
	"bbox": [217, 965, 240, 974],
	"bbox": [292, 983, 320, 992],
	"bbox": [272, 974, 298, 983]
]
2026-08-10 15:42:42,476 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 15:42:42,482 INFO     29 [qwen-vl-text] coord API: raw_items=199, valid_items=2, elapsed=35.8s
2026-08-10 15:42:42,482 INFO     29 [qwen-vl-text] coord item[0]: text=靶向用药基因检测提示, bbox=[443, 17, 553, 26]
2026-08-10 15:42:42,482 INFO     29 [qwen-vl-text] coord item[1]: text=基因, bbox=[217, 44, 240, 53]
2026-08-10 15:42:42,485 INFO     29 [qwen-vl-text] page=6 — 2/194 coords, api_time=35.8s
2026-08-10 15:42:42,486 INFO     29 [qwen-vl-text] new_positions (280):
[[5, 419.6695806884766, 455.3861407470703, 14.312130249023438, 23.57292041015625], [5, 95.24416015625, 135.12765222167968, 42.93639074707031, 53.039070922851565], [5, 100.00636816406251, 136.91348022460937, 63.14175109863281, 72.40254125976563], [5, 220.25212036132814, 250.01592041015627, 63.14175109863281, 72.40254125976563], [5, 357.7608765869141, 387.5246766357422, 63.14175109863281, 72.40254125976563], [5, 100.00636816406251, 116.0788201904297, 78.29577136230469, 87.5565615234375], [5, 220.25212036132814, 253.58757641601562, 78.29577136230469, 87.5565615234375], [5, 357.7608765869141, 486.3404927978516, 78.29577136230469, 87.5565615234375], [5, 100.00636816406251, 129.17489221191406, 92.60790161132812, 101.02680175781249], [5, 220.25212036132814, 280.9702724609375, 92.60790161132812, 101.02680175781249], [5, 357.7608765869141, 415.50264868164066, 92.60790161132812, 101.02680175781249], [5, 100.00636816406251, 139.8898602294922, 106.07814184570313, 115.33893200683593], [5, 220.25212036132814, 261.32616442871097, 106.07814184570313, 115.33893200683593], [5, 357.7608765869141, 427.4081687011719, 106.07814184570313, 115.33893200683593], [5, 100.00636816406251, 129.17489221191406, 121.232162109375, 130.4929522705078], [5, 357.7608765869141, 390.501056640625, 121.232162109375, 130.4929522705078], [5, 100.00636816406251, 133.34182421875, 136.38618237304686, 145.6469725341797], [5, 220.25212036132814, 296.44744848632814, 136.38618237304686, 145.6469725341797], [5, 357.7608765869141, 432.1703767089844, 136.38618237304686, 145.6469725341797], [5, 95.24416015625, 326.21124853515624, 149.85642260742188, 158.27532275390624], [5, 95.24416015625, 135.12765222167968, 186.05769323730468, 196.16037341308595], [5, 100.00636816406251, 129.17489221191406, 207.94683361816405, 217.20762377929688], [5, 167.86783227539064, 239.8962283935547, 207.94683361816405, 217.20762377929688], [5, 100.00636816406251, 129.17489221191406, 224.7846339111328, 234.04542407226563], [5, 167.86783227539064, 415.50264868164066, 224.7846339111328, 234.04542407226563], [5, 100.00636816406251, 129.17489221191406, 258.4602344970703, 267.72102465820313], [5, 167.86783227539064, 486.3404927978516, 239.09676416015625, 288.76827502441404], [5, 100.00636816406251, 129.17489221191406, 293.8196151123047, 303.0804052734375], [5, 167.86783227539064, 367.88056860351566, 293.8196151123047, 303.0804052734375], [5, 100.00636816406251, 159.53396826171877, 307.2898553466797, 316.5506455078125], [5, 167.86783227539064, 382.1671926269531, 307.2898553466797, 316.5506455078125], [5, 100.00636816406251, 136.91348022460937, 320.76009558105466, 330.0208857421875], [5, 167.86783227539064, 215.48991235351562, 320.76009558105466, 330.0208857421875], [5, 95.24416015625, 152.98593225097656, 362.0127062988281, 372.11538647460935], [5, 254.1828524169922, 332.1640085449219, 384.74373669433595, 394.0045268554687], [5, 104.17330017089844, 119.05520019531251, 408.3166571044922, 417.577447265625], [5, 155.9623122558594, 178.58280029296876, 401.5815369873047, 410.8423271484375], [5, 222.63322436523438, 258.3497844238281, 408.3166571044922, 417.577447265625], [5, 296.44744848632814, 333.354560546875, 408.3166571044922, 417.577447265625], [5, 363.7136365966797, 393.47743664550785, 408.3166571044922, 417.577447265625], [5, 413.1215446777344, 442.29006872558597, 401.5815369873047, 410.8423271484375], [5, 460.1483487548828, 489.912148803711, 408.3166571044922, 417.577447265625], [5, 102.38747216796875, 121.43630419921875, 435.2571375732422, 443.67603771972654], [5, 142.866240234375, 192.2741483154297, 429.3639074707031, 450.4111578369141], [5, 221.44267236328125, 259.5403364257813, 435.2571375732422, 443.67603771972654], [5, 300.61438049316405, 329.7829045410156, 435.2571375732422, 443.67603771972654], [5, 363.7136365966797, 393.47743664550785, 435.2571375732422, 443.67603771972654], [5, 414.9073726806641, 440.5042407226563, 435.2571375732422, 443.67603771972654], [5, 456.57669274902344, 493.48380480957036, 429.3639074707031, 450.4111578369141], [5, 100.00636816406251, 123.81740820312501, 455.46249792480467, 478.1935283203125], [5, 143.46151623535158, 191.67887231445314, 463.0395080566406, 472.30029821777345], [5, 238.11040039062502, 242.27733239746095, 463.0395080566406, 472.30029821777345], [5, 313.1151765136719, 317.28210852050785, 463.0395080566406, 472.30029821777345], [5, 359.5467045898438, 397.04909265136723, 463.0395080566406, 472.30029821777345], [5, 416.6932006835938, 435.7420327148438, 457.14627795410155, 478.1935283203125], [5, 456.57669274902344, 493.48380480957036, 455.46249792480467, 478.1935283203125], [5, 104.17330017089844, 119.05520019531251, 489.97998852539064, 498.398888671875], [5, 143.46151623535158, 191.67887231445314, 489.97998852539064, 498.398888671875], [5, 238.11040039062502, 242.27733239746095, 489.97998852539064, 498.398888671875], [5, 313.1151765136719, 317.28210852050785, 489.97998852539064, 498.398888671875], [5, 359.5467045898438, 397.04909265136723, 489.97998852539064, 498.398888671875], [5, 416.6932006835938, 435.7420327148438, 483.2448684082031, 504.29211877441406], [5, 456.57669274902344, 493.48380480957036, 483.2448684082031, 504.29211877441406], [5, 102.38747216796875, 121.43630419921875, 517.7623590087891, 526.1812591552734], [5, 142.866240234375, 192.2741483154297, 511.02723889160154, 532.916379272461], [5, 216.68046435546876, 264.30254443359377, 517.7623590087891, 526.1812591552734], [5, 292.87579248046876, 336.3309405517578, 517.7623590087891, 526.1812591552734], [5, 363.7136365966797, 393.47743664550785, 517.7623590087891, 526.1812591552734], [5, 414.9073726806641, 440.5042407226563, 517.7623590087891, 526.1812591552734], [5, 456.57669274902344, 494.0790808105469, 511.02723889160154, 532.916379272461], [5, 284.5419284667969, 308.3529685058594, 567.4338698730469, 575.8527700195312], [5, 102.38747216796875, 121.43630419921875, 667.618781616211, 676.0376817626953], [5, 142.866240234375, 192.2741483154297, 660.8836614990234, 681.9309118652344], [5, 224.41905236816407, 256.5639564208984, 667.618781616211, 676.0376817626953], [5, 300.61438049316405, 329.7829045410156, 667.618781616211, 676.0376817626953], [5, 363.7136365966797, 393.47743664550785, 667.618781616211, 676.0376817626953], [5, 414.9073726806641, 440.5042407226563, 667.618781616211, 676.0376817626953], [5, 454.79086474609375, 495.26963281250005, 660.8836614990234, 681.9309118652344], [5, 95.24416015625, 107.14968017578126, 693.7173720703125, 702.9781622314453], [5, 100.00636816406251, 377.40498461914063, 707.1876123046875, 716.4484024658203], [5, 95.24416015625, 264.89782043457035, 720.6578525390624, 729.9186427001953], [5, 95.24416015625, 267.27892443847657, 733.286202758789, 742.5469929199219], [5, 95.24416015625, 495.26963281250005, 747.5983330078125, 769.4874733886719], [5, 95.24416015625, 188.10721630859376, 774.5388134765625, 783.7996036376953], [5, 95.24416015625, 194.65525231933594, 788.0090537109375, 797.2698438720703], [5, 258.9450604248047, 332.7592845458984, 825.8941043701171, 834.3130045166016], [6, 263.7072684326172, 329.1876285400391, 14.312130249023438, 21.889140380859374], [6, 129.17489221191406, 142.866240234375, 37.04316064453125, 44.62017077636719], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0], [6, 0, 0, 0, 0]]
2026-08-10 15:42:42,486 INFO     29 [qwen-vl-text] ═══ DONE ═══ 280 positions, pages=2, time=74.5s
2026-08-10 15:42:42,486 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:42:42,493 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:42:42,493 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:42:42,493 INFO     29 [qwen-vl-text] positions(44): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:42:42,493 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [44]
2026-08-10 15:42:42,652 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:42:42,653 INFO     29 [qwen-vl-text] LLM extraction start, text_len=245
2026-08-10 15:42:42,653 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:42:42,653 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 438, \"bbox_end\": 481, \"encounter_dates\": [\"2025-09-18\", \"2025-09-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "患者信息\n姓名\n性别\n男\n年龄\n38岁\n送检单位\n样本信息\n样本编号\n样本类型\n采样部位\n样本采集日期\n样本接收日期\n报告日期\n石蜡块\n—\n2025-09-18\n2025-09-20\n检测项目\nPD-L1蛋白表达检测\n抗体型号\n临床信息\n临床/病理诊断\n肺癌怀疑骨转移肝转移\n手术史/用药史\n—\n二、检测结果\n检测内容\n检测结果\n检测结果提示\nPD-L1蛋白\nTPS\n<1%\nPD-L1蛋白表达。\n表达水平\nCPS\n1\nTC\n<1%\nIC\n1%\n检测结果图示\nPDL1×200\nHE×200",
    "role": "user"
  }
]
2026-08-10 15:42:42,655 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:42:42.655+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:42:44,998 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:42:44,999 INFO     29 [qwen-vl-text] LLM output (len=435):
{
  "exam_date": "2025-09-18",
  "report_date": "2025-09-20",
  "exam_name": "PD-L1蛋白表达检测",
  "exam_category": "pathology",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": null,
  "conclusion": "检测结果\n检测内容\t检测结果\t检测结果提示\nPD-L1蛋白\tTPS\t<1%\tPD-L1蛋白表达。\n表达水平\tCPS\t1\n\tTC\t<1%\n\tIC\t1%\n检测结果图示\nPDL1×200\nHE×200",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:42:45,001 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=675132, prompt_len=990
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["患者信息", "姓名", "性别", "男", "年龄", "38岁", "送检单位", "样本信息", "样本编号", "样本类型", "采样部位", "样本采集日期", "样本接收日期", "报告日期", "石蜡块", "—", "2025-09-18", "2025-09-20", "检测项目", "PD-L1蛋白表达检测", "抗体型号", "临床信息", "临床/病理诊断", "肺癌怀疑骨转移肝转移", "手术史/用药史", "—", "二、检测结果", "检测内容", "检测结果", "检测结果提示", "PD-L1蛋白", "TPS", "<1%", "PD-L1蛋白表达。", "表达水平", "CPS", "1", "TC", "<1%", "IC", "1%", "检测结果图示", "PDL1×200", "HE×200"]

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
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord API raw response (len=2170):
[
	{"text": "患者信息", "bbox": [235, 32, 298, 45]},
	{"text": "姓名", "bbox": [252, 56, 277, 66]},
	{"text": "性别", "bbox": [520, 56, 545, 66]},
	{"text": "男", "bbox": [673, 56, 685, 66]},
	{"text": "年龄", "bbox": [252, 78, 277, 88]},
	{"text": "38岁", "bbox": [387, 78, 411, 88]},
	{"text": "送检单位", "bbox": [511, 78, 554, 88]},
	{"text": "样本信息", "bbox": [235, 126, 298, 139]},
	{"text": "样本编号", "bbox": [243, 152, 287, 162]},
	{"text": "样本类型", "bbox": [342, 152, 387, 162]},
	{"text": "采样部位", "bbox": [432, 152, 477, 162]},
	{"text": "样本采集日期", "bbox": [497, 152, 559, 162]},
	{"text": "样本接收日期", "bbox": [591, 152, 657, 162]},
	{"text": "报告日期", "bbox": [700, 152, 745, 162]},
	{"text": "石蜡块", "bbox": [348, 179, 381, 188]},
	{"text": "—", "bbox": [447, 179, 458, 188]},
	{"text": "2025-09-18", "bbox": [595, 179, 653, 188]},
	{"text": "2025-09-20", "bbox": [696, 179, 751, 188]},
	{"text": "检测项目", "bbox": [243, 204, 287, 214]},
	{"text": "PD-L1蛋白表达检测", "bbox": [351, 204, 448, 214]},
	{"text": "抗体型号", "bbox": [510, 204, 554, 214]},
	{"text": "临床信息", "bbox": [235, 257, 298, 270]},
	{"text": "临床/病理诊断", "bbox": [227, 282, 298, 291]},
	{"text": "肺癌怀疑骨转移肝转移", "bbox": [488, 282, 596, 291]},
	{"text": "手术史/用药史", "bbox": [227, 307, 298, 316]},
	{"text": "—", "bbox": [537, 307, 548, 316]},
	{"text": "二、检测结果", "bbox": [218, 639, 324, 653]},
	{"text": "检测内容", "bbox": [234, 687, 279, 696]},
	{"text": "检测结果", "bbox": [348, 687, 390, 696]},
	{"text": "检测结果提示", "bbox": [577, 687, 643, 696]},
	{"text": "PD-L1蛋白", "bbox": [230, 720, 282, 729]},
	{"text": "TPS", "bbox": [319, 707, 339, 716]},
	{"text": "<1%", "bbox": [392, 707, 415, 716]},
	{"text": "PD-L1蛋白表达。", "bbox": [567, 723, 647, 732]},
	{"text": "表达水平", "bbox": [234, 735, 278, 744]},
	{"text": "CPS", "bbox": [319, 721, 340, 730]},
	{"text": "1", "bbox": [401, 721, 407, 730]},
	{"text": "TC", "bbox": [322, 736, 337, 745]},
	{"text": "<1%", "bbox": [392, 736, 415, 745]},
	{"text": "IC", "bbox": [324, 750, 335, 759]},
	{"text": "1%", "bbox": [395, 750, 412, 759]},
	{"text": "检测结果图示", "bbox": [461, 780, 535, 790]},
	{"text": "PDL1×200", "bbox": [367, 893, 422, 902]},
	{"text": "HE×200", "bbox": [579, 893, 622, 902]}
]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=13.0s
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[0]: text=患者信息, bbox=[235, 32, 298, 45]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[252, 56, 277, 66]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[2]: text=性别, bbox=[520, 56, 545, 66]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[3]: text=男, bbox=[673, 56, 685, 66]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[4]: text=年龄, bbox=[252, 78, 277, 88]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[5]: text=38岁, bbox=[387, 78, 411, 88]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[6]: text=送检单位, bbox=[511, 78, 554, 88]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[7]: text=样本信息, bbox=[235, 126, 298, 139]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[8]: text=样本编号, bbox=[243, 152, 287, 162]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[9]: text=样本类型, bbox=[342, 152, 387, 162]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[10]: text=采样部位, bbox=[432, 152, 477, 162]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[11]: text=样本采集日期, bbox=[497, 152, 559, 162]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[12]: text=样本接收日期, bbox=[591, 152, 657, 162]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[13]: text=报告日期, bbox=[700, 152, 745, 162]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[14]: text=石蜡块, bbox=[348, 179, 381, 188]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[15]: text=—, bbox=[447, 179, 458, 188]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[16]: text=2025-09-18, bbox=[595, 179, 653, 188]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[17]: text=2025-09-20, bbox=[696, 179, 751, 188]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[18]: text=检测项目, bbox=[243, 204, 287, 214]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[19]: text=PD-L1蛋白表达检测, bbox=[351, 204, 448, 214]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[20]: text=抗体型号, bbox=[510, 204, 554, 214]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[21]: text=临床信息, bbox=[235, 257, 298, 270]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[22]: text=临床/病理诊断, bbox=[227, 282, 298, 291]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[23]: text=肺癌怀疑骨转移肝转移, bbox=[488, 282, 596, 291]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[24]: text=手术史/用药史, bbox=[227, 307, 298, 316]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[25]: text=—, bbox=[537, 307, 548, 316]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[26]: text=二、检测结果, bbox=[218, 639, 324, 653]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[27]: text=检测内容, bbox=[234, 687, 279, 696]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[28]: text=检测结果, bbox=[348, 687, 390, 696]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[29]: text=检测结果提示, bbox=[577, 687, 643, 696]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[30]: text=PD-L1蛋白, bbox=[230, 720, 282, 729]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[31]: text=TPS, bbox=[319, 707, 339, 716]
2026-08-10 15:42:57,993 INFO     29 [qwen-vl-text] coord item[32]: text=<1%, bbox=[392, 707, 415, 716]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[33]: text=PD-L1蛋白表达。, bbox=[567, 723, 647, 732]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[34]: text=表达水平, bbox=[234, 735, 278, 744]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[35]: text=CPS, bbox=[319, 721, 340, 730]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[36]: text=1, bbox=[401, 721, 407, 730]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[37]: text=TC, bbox=[322, 736, 337, 745]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[38]: text=<1%, bbox=[392, 736, 415, 745]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[39]: text=IC, bbox=[324, 750, 335, 759]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[40]: text=1%, bbox=[395, 750, 412, 759]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[41]: text=检测结果图示, bbox=[461, 780, 535, 790]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[42]: text=PDL1×200, bbox=[367, 893, 422, 902]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] coord item[43]: text=HE×200, bbox=[579, 893, 622, 902]
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] page=7 — 44/44 coords, api_time=13.0s
2026-08-10 15:42:57,994 INFO     29 [qwen-vl-text] new_positions (44):
[[7, 139.8898602294922, 177.39224829101562, 26.94048046875, 37.88505065917969], [7, 150.00955224609376, 164.8914522705078, 47.1458408203125, 55.564740966796876], [7, 309.5435205078125, 324.42542053222655, 47.1458408203125, 55.564740966796876], [7, 400.62074865722656, 407.7640606689453, 47.1458408203125, 55.564740966796876], [7, 150.00955224609376, 164.8914522705078, 65.66742114257812, 74.0863212890625], [7, 230.3718123779297, 244.6584364013672, 65.66742114257812, 74.0863212890625], [7, 304.18603649902343, 329.7829045410156, 65.66742114257812, 74.0863212890625], [7, 139.8898602294922, 177.39224829101562, 106.07814184570313, 117.02271203613282], [7, 144.6520682373047, 170.84421228027344, 127.9672822265625, 136.38618237304686], [7, 203.5843923339844, 230.3718123779297, 127.9672822265625, 136.38618237304686], [7, 257.159232421875, 283.9466524658203, 127.9672822265625, 136.38618237304686], [7, 295.85217248535156, 332.7592845458984, 127.9672822265625, 136.38618237304686], [7, 351.80811657714844, 391.0963326416016, 127.9672822265625, 136.38618237304686], [7, 416.6932006835938, 443.4806207275391, 127.9672822265625, 136.38618237304686], [7, 207.15604833984375, 226.80015637207032, 150.69831262207032, 158.27532275390624], [7, 266.08837243652346, 272.63640844726564, 150.69831262207032, 158.27532275390624], [7, 354.1892205810547, 388.7152286376953, 150.69831262207032, 158.27532275390624], [7, 414.3120966796875, 447.05227673339846, 150.69831262207032, 158.27532275390624], [7, 144.6520682373047, 170.84421228027344, 171.74556298828125, 180.1644631347656], [7, 208.94187634277344, 266.6836484375, 171.74556298828125, 180.1644631347656], [7, 303.5907604980469, 329.7829045410156, 171.74556298828125, 180.1644631347656], [7, 139.8898602294922, 177.39224829101562, 216.36573376464844, 227.31030395507813], [7, 135.12765222167968, 177.39224829101562, 237.41298413085937, 244.98999426269532], [7, 290.4946884765625, 354.78449658203124, 237.41298413085937, 244.98999426269532], [7, 135.12765222167968, 177.39224829101562, 258.4602344970703, 266.03724462890625], [7, 319.66321252441406, 326.21124853515624, 258.4602344970703, 266.03724462890625], [7, 129.77016821289064, 192.86942431640625, 537.9677193603516, 549.7541795654297], [7, 139.29458422851562, 166.08200427246095, 578.3784400634765, 585.9554501953124], [7, 207.15604833984375, 232.1576403808594, 578.3784400634765, 585.9554501953124], [7, 343.47425256347657, 382.7624686279297, 578.3784400634765, 585.9554501953124], [7, 136.91348022460937, 167.86783227539064, 606.160810546875, 613.7378206787109], [7, 189.89304431152345, 201.7985643310547, 595.2162403564453, 602.7932504882813], [7, 233.3481923828125, 247.03954040527344, 595.2162403564453, 602.7932504882813], [7, 337.52149255371097, 385.143572631836, 608.6864805908203, 616.2634907226562], [7, 139.29458422851562, 165.4867282714844, 618.7891607666015, 626.3661708984375], [7, 189.89304431152345, 202.39384033203126, 607.0027005615234, 614.5797106933594], [7, 238.70567639160157, 242.27733239746095, 607.0027005615234, 614.5797106933594], [7, 191.67887231445314, 200.60801232910157, 619.63105078125, 627.2080609130859], [7, 233.3481923828125, 247.03954040527344, 619.63105078125, 627.2080609130859], [7, 192.86942431640625, 199.41746032714843, 631.4175109863281, 638.994521118164], [7, 235.1340203857422, 245.25371240234375, 631.4175109863281, 638.994521118164], [7, 274.4222364501953, 318.47266052246096, 656.6742114257812, 665.0931115722656], [7, 218.46629235839845, 251.20647241210938, 751.8077830810547, 759.3847932128906], [7, 344.6648045654297, 370.2616726074219, 751.8077830810547, 759.3847932128906]]
2026-08-10 15:42:57,995 INFO     29 [qwen-vl-text] ═══ DONE ═══ 44 positions, pages=1, time=15.5s
2026-08-10 15:42:57,995 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:42:57,995 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:42:57,996 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:42:57,996 INFO     29 [qwen-vl-text] positions(42): [[21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:42:57,996 INFO     29 [qwen-vl-text] page grouping: [21], lines per page: [42]
2026-08-10 15:42:58,292 INFO     29 [qwen-vl-text] page=21, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:42:58,294 INFO     29 [qwen-vl-text] LLM extraction start, text_len=809
2026-08-10 15:42:58,295 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:42:58,295 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 859, \"bbox_end\": 900, \"encounter_dates\": [\"2026-03-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "医学影像检查报告单\n扫码查看影像\n检查号:\n患者姓名:\n性别:男\n年龄:39岁\n住院号:\n申请科室\n床号:023\n联系电话\n检查室:CT1(联影CT)(1住)\n检查技师:羊媛颖\n检查时间:2026-03-25 08:22:58\n检查部位:[*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强]\n检查技术:-\n描述:\n1、“肺CA”复查,右肺上叶见团块影,边缘呈分叶状,局部与胸膜粘连,见支气\n管截断,较大层面范围约5.6cm×5.3cm,增强扫描呈轻度不均匀强化,周围见斑条\n影及小结节影,较CT260121-240片病灶稍增大。\n2、双肺另见长径约0.4-0.7cm微小结节,较大者位于右肺上叶前段(IM37)较前片\n稍增大,必要时随诊。\n3、右肺中叶及双肺下叶见散在斑条影。\n4、心包少量积液。纵隔淋巴结显示,部分稍增大。双侧胸膜稍增厚。\n5、肝右后叶见稍低密度结节,边缘稍模糊,增强扫描轻中度强化,边缘强化明\n显,较大层面范围约1.2cm×0.9cm,转移灶可能,其它病变待排,较前稍缩小。\n6、左侧肾上腺内侧支增粗,见结节状稍低密度影,增强扫描强化稍欠均匀,长径\n约1.4cm,占位性病变或转移灶待排。较前稍增大。\n7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。\n8、右肾见稍低密度结节,较大者长径约1.3cm,增强扫描似见轻度强化,占位性病\n变或转移灶待排。较前变化不大。\n9、前列腺稍显丰满,强化稍欠均匀。\n10、扫及双侧部分肋骨,胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻\n骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏,转移灶可能,部分椎体\n变扁,病理性骨折待排。\n请结合临床及其它检查,必要时复查或进一步检查。\n总结意见:\n见上述。\n报告者:申悦\n审核医师:曹玉\n报告时间:2026/3/25 8:48:11\n审核时间:2026/3/25 9:26:23\n注:此报告审核",
    "role": "user"
  }
]
2026-08-10 15:43:03,578 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:43:03,578 INFO     29 [qwen-vl-text] LLM output (len=903):
{
  "exam_date": "2026-03-25",
  "report_date": "2026-03-25",
  "exam_name": "胸部、上腹部、下腹部、盆腔CT增强",
  "exam_category": "imaging",
  "body_part": "盆腔,上腹部,下腹部,胸部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": "023",
  "findings": "1、“肺CA”复查,右肺上叶见团块影,边缘呈分叶状,局部与胸膜粘连,见支气管截断,较大层面范围约5.6cm×5.3cm,增强扫描呈轻度不均匀强化,周围见斑条影及小结节影,较CT260121-240片病灶稍增大。\n2、双肺另见长径约0.4-0.7cm微小结节,较大者位于右肺上叶前段(IM37)较前片稍增大,必要时随诊。\n3、右肺中叶及双肺下叶见散在斑条影。\n4、心包少量积液。纵隔淋巴结显示,部分稍增大。双侧胸膜稍增厚。\n5、肝右后叶见稍低密度结节,边缘稍模糊,增强扫描轻中度强化,边缘强化明显,较大层面范围约1.2cm×0.9cm,转移灶可能,其它病变待排,较前稍缩小。\n6、左侧肾上腺内侧支增粗,见结节状稍低密度影,增强扫描强化稍欠均匀,长径约1.4cm,占位性病变或转移灶待排。较前稍增大。\n7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。\n8、右肾见稍低密度结节,较大者长径约1.3cm,增强扫描似见轻度强化,占位性病变或转移灶待排。较前变化不大。\n9、前列腺稍显丰满,强化稍欠均匀。\n10、扫及双侧部分肋骨,胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏,转移灶可能,部分椎体变扁,病理性骨折待排。\n请结合临床及其它检查,必要时复查或进一步检查。",
  "conclusion": "见上述。",
  "physician": "申悦",
  "reviewer": "曹玉"
}
2026-08-10 15:43:03,587 INFO     29 [qwen-vl-text] coord API call start, page=21, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2111514, prompt_len=1548
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共42行）
["医学影像检查报告单", "扫码查看影像", "检查号:", "患者姓名:", "性别:男", "年龄:39岁", "住院号:", "申请科室", "床号:023", "联系电话", "检查室:CT1(联影CT)(1住)", "检查技师:羊媛颖", "检查时间:2026-03-25 08:22:58", "检查部位:[*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强]", "检查技术:-", "描述:", "1、“肺CA”复查,右肺上叶见团块影,边缘呈分叶状,局部与胸膜粘连,见支气", "管截断,较大层面范围约5.6cm×5.3cm,增强扫描呈轻度不均匀强化,周围见斑条", "影及小结节影,较CT260121-240片病灶稍增大。", "2、双肺另见长径约0.4-0.7cm微小结节,较大者位于右肺上叶前段(IM37)较前片", "稍增大,必要时随诊。", "3、右肺中叶及双肺下叶见散在斑条影。", "4、心包少量积液。纵隔淋巴结显示,部分稍增大。双侧胸膜稍增厚。", "5、肝右后叶见稍低密度结节,边缘稍模糊,增强扫描轻中度强化,边缘强化明", "显,较大层面范围约1.2cm×0.9cm,转移灶可能,其它病变待排,较前稍缩小。", "6、左侧肾上腺内侧支增粗,见结节状稍低密度影,增强扫描强化稍欠均匀,长径", "约1.4cm,占位性病变或转移灶待排。较前稍增大。", "7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。", "8、右肾见稍低密度结节,较大者长径约1.3cm,增强扫描似见轻度强化,占位性病", "变或转移灶待排。较前变化不大。", "9、前列腺稍显丰满,强化稍欠均匀。", "10、扫及双侧部分肋骨,胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻", "骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏,转移灶可能,部分椎体", "变扁,病理性骨折待排。", "请结合临床及其它检查,必要时复查或进一步检查。", "总结意见:", "见上述。", "报告者:申悦", "审核医师:曹玉", "报告时间:2026/3/25 8:48:11", "审核时间:2026/3/25 9:26:23", "注:此报告审核"]

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
2026-08-10 15:43:19,691 INFO     29 [qwen-vl-text] coord API raw response (len=3379):
[
	{"text": "人民醫院", "bbox": [480, 50, 642, 84]},
	{"text": "川渝HR", "bbox": [840, 55, 916, 73]},
	{"text": "带*为川渝互认项目", "bbox": [825, 75, 930, 86]},
	{"text": "医学影像检查报告单", "bbox": [386, 90, 654, 111]},
	{"text": "检查号:", "bbox": [714, 107, 785, 122], "label": "检查号"},
	{"text": "患者姓名:", "bbox": [78, 124, 158, 140], "label": "患者姓名"},
	{"text": "性别:男", "bbox": [391, 127, 465, 142], "label": "性别"},
	{"text": "年龄:39岁", "bbox": [529, 128, 627, 143], "label": "年龄"},
	{"text": "住院号:", "bbox": [714, 131, 785, 146], "label": "住院号"},
	{"text": "申请科室", "bbox": [78, 146, 155, 161], "label": "申请科室"},
	{"text": "床号:023", "bbox": [390, 148, 476, 163], "label": "床号"},
	{"text": "联系电话", "bbox": [714, 151, 798, 167], "label": "联系电话"},
	{"text": "检查室:CT1(联影CT)(1住)", "bbox": [76, 170, 323, 186], "label": "检查室"},
	{"text": "检查技师:羊媛颖", "bbox": [390, 172, 544, 188], "label": "检查技师"},
	{"text": "检查时间:2026-03-25 08:22:58", "bbox": [628, 175, 904, 190], "label": "检查时间"},
	{"text": "检查部位:[*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强]", "bbox": [75, 193, 673, 213], "label": "检查部位"},
	{"text": "检查技术:-", "bbox": [71, 228, 180, 244], "label": "检查技术"},
	{"text": "描述:", "bbox": [70, 249, 122, 265], "label": "描述"},
	{"text": "1、“肺CA”复查,右肺上叶见团块影,边缘呈分叶状,局部与胸膜粘连,见支气", "bbox": [92, 275, 904, 294], "label": "描述"},
	{"text": "管截断,较大层面范围约5.6cm×5.3cm,增强扫描呈轻度不均匀强化,周围见斑条", "bbox": [92, 291, 914, 310], "label": "描述"},
	{"text": "影及小结节影,较CT260121-240片病灶稍增大。", "bbox": [91, 306, 557, 325], "label": "描述"},
	{"text": "2、双肺另见长径约0.4-0.7cm微小结节,较大者位于右肺上叶前段(IM37)较前片", "bbox": [87, 322, 913, 343], "label": "描述"},
	{"text": "稍增大,必要时随诊。", "bbox": [87, 337, 304, 355], "label": "描述"},
	{"text": "3、右肺中叶及双肺下叶见散在斑条影。", "bbox": [84, 352, 476, 371], "label": "描述"},
	{"text": "4、心包少量积液。纵隔淋巴结显示,部分稍增大。双侧胸膜稍增厚。", "bbox": [83, 368, 776, 389], "label": "描述"},
	{"text": "5、肝右后叶见稍低密度结节,边缘稍模糊,增强扫描轻中度强化,边缘强化明", "bbox": [82, 384, 883, 405], "label": "描述"},
	{"text": "显,较大层面范围约1.2cm×0.9cm,转移灶可能,其它病变待排,较前稍缩小。", "bbox": [82, 400, 883, 421], "label": "描述"},
	{"text": "6、左侧肾上腺内侧支增粗,见结节状稍低密度影,增强扫描强化稍欠均匀,长径", "bbox": [79, 415, 907, 438], "label": "描述"},
	{"text": "约1.4cm,占位性病变或转移灶待排。较前稍增大。", "bbox": [79, 431, 588, 452], "label": "描述"},
	{"text": "7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。", "bbox": [77, 447, 656, 468], "label": "描述"},
	{"text": "8、右肾见稍低密度结节,较大者长径约1.3cm,增强扫描似见轻度强化,占位性病", "bbox": [76, 463, 918, 485], "label": "描述"},
	{"text": "变或转移灶待排。较前变化不大。", "bbox": [76, 479, 416, 498], "label": "描述"},
	{"text": "9、前列腺稍显丰满,强化稍欠均匀。", "bbox": [74, 494, 450, 514], "label": "描述"},
	{"text": "10、扫及双侧部分肋骨,胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻", "bbox": [74, 510, 895, 532], "label": "描述"},
	{"text": "骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏,转移灶可能,部分椎体", "bbox": [73, 526, 918, 548], "label": "描述"},
	{"text": "变扁,病理性骨折待排。", "bbox": [73, 542, 320, 561], "label": "描述"},
	{"text": "请结合临床及其它检查,必要时复查或进一步检查。", "bbox": [70, 575, 595, 596], "label": "请结合临床及其它检查,必要时复查或进一步检查。"},
	{"text": "总结意见:", "bbox": [28, 805, 134, 824], "label": "总结意见"},
	{"text": "见上述。", "bbox": [57, 840, 138, 858], "label": "见上述。"},
	{"text": "报告者:申悦", "bbox": [34, 896, 154, 914], "label": "报告者"},
	{"text": "审核医师:曹玉", "bbox": [547, 893, 685, 914], "label": "审核医师"},
	{"text": "报告时间:2026/3/25 8:48:11", "bbox": [33, 917, 308, 935], "label": "报告时间"},
	{"text": "审核时间:2026/3/25 9:26:23", "bbox": [547, 914, 821, 946], "label": "审核时间"},
	{"text": "注:此报告审核", "bbox": [617, 956, 764, 972], "label": "注:此报告审核"}
]
2026-08-10 15:43:19,691 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=16.1s
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[0]: text=人民醫院, bbox=[480, 50, 642, 84]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[1]: text=川渝HR, bbox=[840, 55, 916, 73]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[2]: text=带*为川渝互认项目, bbox=[825, 75, 930, 86]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[3]: text=医学影像检查报告单, bbox=[386, 90, 654, 111]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[4]: text=检查号:, bbox=[714, 107, 785, 122]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[5]: text=患者姓名:, bbox=[78, 124, 158, 140]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[6]: text=性别:男, bbox=[391, 127, 465, 142]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[7]: text=年龄:39岁, bbox=[529, 128, 627, 143]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[8]: text=住院号:, bbox=[714, 131, 785, 146]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[9]: text=申请科室, bbox=[78, 146, 155, 161]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[10]: text=床号:023, bbox=[390, 148, 476, 163]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话, bbox=[714, 151, 798, 167]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[12]: text=检查室:CT1(联影CT)(1住), bbox=[76, 170, 323, 186]
2026-08-10 15:43:19,692 INFO     29 [qwen-vl-text] coord item[13]: text=检查技师:羊媛颖, bbox=[390, 172, 544, 188]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[14]: text=检查时间:2026-03-25 08:22:58, bbox=[628, 175, 904, 190]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[15]: text=检查部位:[*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强], bbox=[75, 193, 673, 213]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[16]: text=检查技术:-, bbox=[71, 228, 180, 244]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[17]: text=描述:, bbox=[70, 249, 122, 265]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[18]: text=1、“肺CA”复查,右肺上叶见团块影,边缘呈分叶状,局部与胸膜粘连,见支气, bbox=[92, 275, 904, 294]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[19]: text=管截断,较大层面范围约5.6cm×5.3cm,增强扫描呈轻度不均匀强化,周围见斑条, bbox=[92, 291, 914, 310]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[20]: text=影及小结节影,较CT260121-240片病灶稍增大。, bbox=[91, 306, 557, 325]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[21]: text=2、双肺另见长径约0.4-0.7cm微小结节,较大者位于右肺上叶前段(IM37)较前片, bbox=[87, 322, 913, 343]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[22]: text=稍增大,必要时随诊。, bbox=[87, 337, 304, 355]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[23]: text=3、右肺中叶及双肺下叶见散在斑条影。, bbox=[84, 352, 476, 371]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[24]: text=4、心包少量积液。纵隔淋巴结显示,部分稍增大。双侧胸膜稍增厚。, bbox=[83, 368, 776, 389]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[25]: text=5、肝右后叶见稍低密度结节,边缘稍模糊,增强扫描轻中度强化,边缘强化明, bbox=[82, 384, 883, 405]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[26]: text=显,较大层面范围约1.2cm×0.9cm,转移灶可能,其它病变待排,较前稍缩小。, bbox=[82, 400, 883, 421]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[27]: text=6、左侧肾上腺内侧支增粗,见结节状稍低密度影,增强扫描强化稍欠均匀,长径, bbox=[79, 415, 907, 438]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[28]: text=约1.4cm,占位性病变或转移灶待排。较前稍增大。, bbox=[79, 431, 588, 452]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[29]: text=7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。, bbox=[77, 447, 656, 468]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[30]: text=8、右肾见稍低密度结节,较大者长径约1.3cm,增强扫描似见轻度强化,占位性病, bbox=[76, 463, 918, 485]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[31]: text=变或转移灶待排。较前变化不大。, bbox=[76, 479, 416, 498]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[32]: text=9、前列腺稍显丰满,强化稍欠均匀。, bbox=[74, 494, 450, 514]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[33]: text=10、扫及双侧部分肋骨,胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻, bbox=[74, 510, 895, 532]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[34]: text=骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏,转移灶可能,部分椎体, bbox=[73, 526, 918, 548]
2026-08-10 15:43:19,693 INFO     29 [qwen-vl-text] coord item[35]: text=变扁,病理性骨折待排。, bbox=[73, 542, 320, 561]
2026-08-10 15:43:19,694 INFO     29 [qwen-vl-text] coord item[36]: text=请结合临床及其它检查,必要时复查或进一步检查。, bbox=[70, 575, 595, 596]
2026-08-10 15:43:19,694 INFO     29 [qwen-vl-text] coord item[37]: text=总结意见:, bbox=[28, 805, 134, 824]
2026-08-10 15:43:19,694 INFO     29 [qwen-vl-text] coord item[38]: text=见上述。, bbox=[57, 840, 138, 858]
2026-08-10 15:43:19,694 INFO     29 [qwen-vl-text] coord item[39]: text=报告者:申悦, bbox=[34, 896, 154, 914]
2026-08-10 15:43:19,694 INFO     29 [qwen-vl-text] coord item[40]: text=审核医师:曹玉, bbox=[547, 893, 685, 914]
2026-08-10 15:43:19,694 INFO     29 [qwen-vl-text] coord item[41]: text=报告时间:2026/3/25 8:48:11, bbox=[33, 917, 308, 935]
2026-08-10 15:43:19,694 INFO     29 [qwen-vl-text] coord item[42]: text=审核时间:2026/3/25 9:26:23, bbox=[547, 914, 821, 946]
2026-08-10 15:43:19,694 INFO     29 [qwen-vl-text] coord item[43]: text=注:此报告审核, bbox=[617, 956, 764, 972]
2026-08-10 15:43:19,695 INFO     29 [qwen-vl-text] page=21 — 42/42 coords, api_time=16.1s
2026-08-10 15:43:19,695 INFO     29 [qwen-vl-text] new_positions (42):
[[21, 285.73248046875, 382.1671926269531, 42.09450073242188, 70.71876123046874], [21, 500.03184082031254, 545.2728168945313, 46.30395080566406, 61.45797106933594], [21, 491.1027008056641, 553.6066809082032, 63.14175109863281, 72.40254125976563], [21, 229.77653637695315, 389.3105046386719, 75.77010131835938, 93.44979162597656], [21, 425.02706469726564, 467.2916607666016, 90.0822315673828, 102.71058178710938], [21, 46.43152807617188, 94.05360815429688, 104.39436181640625, 117.86460205078124], [21, 232.75291638183595, 276.8033404541016, 106.92003186035156, 119.54838208007813], [21, 314.9010045166016, 373.2380526123047, 107.761921875, 120.39027209472655], [21, 425.02706469726564, 467.2916607666016, 110.28759191894531, 122.91594213867188], [21, 46.43152807617188, 92.26778015136719, 122.91594213867188, 135.54429235839842], [21, 232.1576403808594, 283.3513764648438, 124.59972216796875, 137.2280723876953], [21, 425.02706469726564, 475.03024877929687, 127.12539221191406, 140.59563244628907], [21, 45.24097607421875, 192.2741483154297, 143.12130249023437, 156.59154272460938], [21, 232.1576403808594, 323.83014453125, 144.80508251953125, 158.27532275390624], [21, 373.83332861328125, 538.1295048828125, 147.33075256347655, 159.95910278320312], [21, 44.64570007324219, 400.62074865722656, 162.48477282714845, 179.3225731201172], [21, 42.26459606933594, 107.14968017578126, 191.95092333984374, 205.42116357421875], [21, 41.669320068359376, 72.62367211914062, 209.63061364746093, 223.10085388183595], [21, 54.76539208984375, 538.1295048828125, 231.5197540283203, 247.51566430664062], [21, 54.76539208984375, 544.0822648925781, 244.98999426269532, 260.9859045410156], [21, 54.17011608886719, 331.5687325439453, 257.6183444824219, 273.6142547607422], [21, 51.78901208496094, 543.4869888916016, 271.08858471679684, 288.76827502441404], [21, 51.78901208496094, 180.963904296875, 283.71693493652344, 298.8709552001953], [21, 50.003184082031254, 283.3513764648438, 296.34528515625, 312.3411954345703], [21, 49.40790808105469, 461.9341767578125, 309.815525390625, 327.4952156982422], [21, 48.812632080078124, 525.6287088623047, 323.285765625, 340.9654559326172], [21, 48.812632080078124, 525.6287088623047, 336.756005859375, 354.43569616699216], [21, 47.02680407714844, 539.9153328857423, 349.38435607910156, 368.74782641601564], [21, 47.02680407714844, 350.02228857421875, 362.8545963134766, 380.53428662109377], [21, 45.83625207519531, 390.501056640625, 376.32483654785153, 394.0045268554687], [21, 45.24097607421875, 546.4633688964844, 389.79507678222654, 408.3166571044922], [21, 45.24097607421875, 247.63481640625002, 403.26531701660156, 419.26122729492187], [21, 44.05042407226563, 267.87420043945315, 415.8936672363281, 432.7314675292969], [21, 44.05042407226563, 532.7720208740235, 429.3639074707031, 447.8854877929687], [21, 43.45514807128907, 546.4633688964844, 442.8341477050781, 461.35572802734373], [21, 43.45514807128907, 190.4883203125, 456.30438793945314, 472.30029821777345], [21, 41.669320068359376, 354.1892205810547, 484.0867584228516, 501.76644873046877], [21, 16.66772802734375, 79.76698413085938, 677.7214617919922, 693.7173720703125], [21, 33.930732055664066, 82.14808813476563, 707.1876123046875, 722.3416325683594], [21, 20.239384033203127, 91.67250415039062, 754.333453125, 769.4874733886719], [21, 325.6159725341797, 407.7640606689453, 751.8077830810547, 769.4874733886719], [21, 19.644108032226562, 183.34500830078125, 772.0131434326172, 787.1671636962891]]
2026-08-10 15:43:19,695 INFO     29 [qwen-vl-text] ═══ DONE ═══ 42 positions, pages=1, time=21.7s
2026-08-10 15:43:19,791 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 15:43:19,792 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:ExaminationReport | outputs={"chunks": "5 items, types={'ExaminationReport': 5}", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:43:19,792 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 15:43:19,795 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:43:19.793+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 68, "failed": 0, "current": {"a18ddf0c94d011f1bd9827cf206dfa2d": {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:43:19,811 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:43:19,811 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:43:20,843 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:43:20,857 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 15:43:20,857 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "901 items", "markdown": "", "text": "", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "output_format": "chunks", "chunks_Admission": "2 items, types={'AdmissionRecord': 2}", "chunks_Discharge": "6 items, types={'DischargeRecord': 6}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Admission\": 2, \"chunks_Discharge\": 6, \"chunks_Examination\": 5, \"chunks_LabExam\": 6}"}
2026-08-10 15:43:20,857 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 15:43:20,861 INFO     29 [ChunkMerger] Merged 19 chunks from 9 sources: {'Extractor:LabExam': 6, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 6, 'Extractor:Admission': 2, 'Extractor:ExaminationReport': 5, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 15:43:20,877 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 15:43:20,877 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "19 items, types={'LabReport': 6, 'DischargeRecord': 6, 'AdmissionRecord': 2, 'ExaminationReport': 5}", "name": "腺癌TKI耐药ZHDO，39岁.pdf"}
2026-08-10 15:43:20,877 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 15:43:21,107 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786375922974, 'update_date': datetime.datetime(2026, 8, 10, 15, 32, 2), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1167304, 'status': '1'}
2026-08-10 15:43:21,305 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   标本颜色  None  黄色  None  None  False    标本性状  None  半稀便  None  None  False    红细胞  None  无  /HP  无  False    镜下白细胞  None  无  /HP  无  False    吞噬细胞  None  无  /HP  无  False    酵母样菌  None  无  /HP  无  False    脂肪球  None  无  /HP  无  False    脓细胞  None  无  /HP  无  False    淀粉样颗粒  None  无  /HP  无  False   
---
   颜色  None  淡黄色  None  None  False    浊度  None  透明  None  None  False    尿胆原  None  None  None  None  False    胆红素  None  None  None  None  False    酮体  None  None  None  None  False    尿潜血  None  None  None  None  False    尿蛋白  None  None  None  None  False    亚硝酸盐  None  None  None  None  False    维生素C  None  None  None  None  False    白细胞  None  None  None  None  False    葡萄糖  None  None  None  None  False    尿比重  None  1.025  None  1.003-1.030  False    PH值  None  5.00  None  4.5-8.0  False   
---
   总蛋白  None  81.60  g/L  65-85  False    白蛋白  None  44.30  g/L  40-55  False    球蛋白  None  37.30  g/l  20-40  False    丙氨酸氨基转移酶  None  84.50  U/L  9-50  True    天门冬氨酸氨基转移酶  None  47.40  U/L  15-40  True    总胆红素  None  10.00  umol/L  0-26  False    直接胆红素  None  4.60  umol/L  0-8  False    间接胆红素  None  5.40  umol/L  0-13  False    胆碱脂酶  None  8964.00  U/L  5320-12920  False    葡萄糖  None  4.62  mmol/L  4.1-6.05  False    钾  None  3.75  mmol/L  3.5-5.5  False    钠  None  136.00  mmol/L  137-147  True    氯  None  98.80  mmol/L  99-110  True    钙  None  2.50  mmol/L  2.11-2.54  False    肌酐  None  73.00  umol/L  59-104  False    尿素  None  6.10  mmol/L  3.1-9.5  False    尿酸  None  406.00  umol/L  202.3-416.5  False    肾小球滤过率  None  111.07  ml/min  >80  False   
---
   癌胚抗原  CEA  163.87  ng/ml  0-4.5  True    神经元特异性烯醇化酶  NSE  49.25  ng/ml  <16.5  True    胃泌素释放肽前体  Pro-GRP  55.98  pg/ml  0-78.62  False   
---
   凝血酶原时间  None  11.40  秒  9-14  False    国际标准化比值  INR  0.99  None  0.77-1.19  False    凝血酶原活动度  None  87  %  70-130  False    活化部分凝血活酶时间  None  28.00  秒  24.8-33.8  False    纤维蛋白原  None  4.04  g/L  2-4  True    凝血酶时间  None  17.10  秒  14-21  False    D-二聚体  None  1.02  mg/L FEU  0-0.50  True   
---
   白细胞计数  None  6.77  10^9/L  3.5-9.5  False    中性粒细胞百分率  None  73.40  %  40-75  False    淋巴细胞百分率  None  15.30  %  20-50  True    单核细胞百分率  None  9.00  %  3-10  False    嗜酸细胞百分率  None  1.80  %  0.4-8.0  False    嗜碱细胞百分率  None  0.50  %  0.00-1.0  False    中性粒细胞计数  None  4.97  10^9/L  1.8-6.3  False    淋巴细胞计数  None  1.04  10^9/L  1.1-3.2  True    单核细胞计数  None  0.61  10^9/L  0.10-0.60  True    嗜酸细胞计数  None  0.12  10^9/L  0.02-0.52  False    嗜碱细胞计数  None  0.03  10^9/L  0-0.06  False    红细胞计数  None  4.81  10^12/L  4.3-5.8  False    血红蛋白浓度  None  131.00  g/l  130-175  False    红细胞压积  None  39.50  %  40-50  True    平均红细胞体积  None  82.00  fL  82-100  False    红细胞宽度-SD值  None  50.10  fL  37-50  True    红细胞宽度-CV值  None  16.60  %  10.9-15.4  True    平均血红蛋白含量  None  27.20  pg  27-34  False    平均血红蛋白浓度  None  332.00  g/l  316-354  False    血小板计数  None  167.00  10^9/L  125-350  False    平均血小板体积  None  13.10  fL  9-13  True    血小板压积  None  0.22  %  0.108-0.282  False    血小板分布宽度  None  16.80  fL  9-17  False    大血小板比率  None  50.00  %  16.9-46.7  True    大血小板计数  None  83.00  10^9/L  30-90  False   
---
出院证明书
(医院保存联)
姓名：
性别：男
年龄：38岁
入院时间：2025-09-09 10:41
住院证字
号
出院时间：2025-09-12
病人单位或住址：
出院诊断：1.右肺上叶腺癌cT4N1M1c IVB期（伴多发骨、肝脏、脑转移） 2.肝继发恶性肿瘤？ 3.
多发骨继发恶性肿瘤？ 4.中脑继发恶性肿瘤？ 5.癌性疼痛
诊疗小结：患者因“咳嗽3+月，发现右上肺占位10+天”入院。辅助检查：2025-09-01 [*胸部,增
强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右
肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸
膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧
部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨
折可能。2025-09-11 [*头部,MRI平扫] [头部,DWI],1、中脑内异常信号影，占位性病变？脱髓鞘病
变？缺血灶？其它？2、扫及右侧上颌窦囊肿可能。请结合临床及其它检查。2025-09-01 CYFRA21-1
+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞
角蛋白19片段测定 62.83(ng/ml)↑；2025-09-09 血常规(五分类):白细胞计数 10.51(10^9/L)↑，
中性粒细胞百分率 80.40(%)↑，中性粒细胞计数 8.45(10^9/L)↑。心电图：1.窦性心律 2.电轴左
偏。
诊疗经过：[入院后完善相关辅助检查，于2025-09-10行经皮肺穿刺活检，免疫组化结果电话询问病
理科腺癌可能性大，报告未回，现患者要求院外等待结果，予以办理出院。]
治疗结果：好转
出院医嘱及建议：1、注意休息，避免受凉感冒及劳累；2、院外追踪免疫组化结果，待结果回示后
及时呼吸内科门诊就诊；3、呼吸科、肿瘤科门诊随访，如有不适，请及时就医。
---
出院证明书
(医院保存联)
住院证字
号
姓名
年龄：38岁 入院时间：2025-12-04 09:00
科
床号：029 出院时间：2025-12-07
病人单位或住址
出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR
L858R+）3.恶性肿瘤靶向治疗 4.肝继发恶性肿瘤 5.骨继发恶性肿瘤 6.化疗相关恶心和呕吐 7.
化疗后骨髓抑制 8.轻度贫血
诊疗小结：患者因“发现右肺上叶占位5+月，右肺上叶腺癌靶向治疗中。”入院。入院查体：
T36.5℃，P75次/分，R20次/分，BP127/82mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语
颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣
膜区未闻及病理性杂音。]辅助检查：暂缺。
诊疗经过：[入院完善相关检查2025-12-04 血常规(五分类)：白细胞计数 5.47(10^9/L)，血红蛋
白浓度 140.00(g/l)；癌胚抗原 136.41(ng/ml)↑，神经元特异性烯醇化酶 20.11(ng/ml)↑，胃泌
素释放肽前体 46.83(pg/ml)；凝血、肝肾功、电解质、钙测定未见明显异常。2025-12-04 胸腹部增
强CT：1、“肺CA”复查，右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较
大层面范围约5.7cm×5.3cm，增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较
CT250830-152前片病灶范围缩小。2、双肺另见长径约0.4-0.5cm微小结节，必要时随诊。3、右肺中
叶及双肺下叶见散在斑条影。4、心包少量积液。双侧胸膜稍增厚。5、肝右后叶见稍低密度结节，边
缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范围约1.7cm×1.5cm，转移灶可能，其它
病变待排。6、左侧肾上腺内侧支增粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约
1.2cm，占位性病变或转移灶待排。7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右
肾见稍低密度结节，较大者长径约1.3cm，增强扫描似见轻度强化，占位性病变或转移灶待排。9、前
列腺强化稍欠均匀。直肠壁稍显增厚。10、扫及双侧部分肋骨，胸腰骶椎多个椎体、胸骨、双侧髂
骨、耻骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理
性骨折待排。病情评价好转，给于唑来磷酸预防骨相关事件。排除化疗禁忌于2025-12-5行第1周期AC
方案化疗联合靶向治疗，具体：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼 110mg
qd，化疗中给于抑酸、护胃、止吐等对症治疗，化疗顺利，患者无明显不适。化疗后复查血常规提
示轻度贫血，给与纠正贫血对症治疗，于今出院回家休养。]
治疗结果：好转
出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就
第1页/共2页
---
出院证明书
(医院保存联)
住院证字
号
性别：男 年龄：39岁 入院时间：2025-12-29 09:54
床号： 出院时间：2025-12-31
病人单位或住址
出院诊断：1.姑息性化疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）
3.肝继发恶性肿瘤 4.骨继发恶性肿瘤 5.化疗相关性恶心和呕吐 6.化疗相关性吞咽困难 7.肝功
能不全
诊疗小结：患者因“发现右肺上叶占位6+月，右肺上叶腺癌1周期化疗后20+天。”入院。入院查
体：T36.7℃；P85次/分；R18次/分；BP117/81mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺
语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各
瓣膜区未闻及病理性杂音。
诊疗经过：患者入院后完善相关检查，2025-12-29 血常规(五分类)：白细胞计数 5.25(10^9/L)，
中性粒细胞百分率 72.90(%)，血红蛋白浓度 145.00(g/l)，血小板计数 117.00(10^9/L)↓；
2025-12-29 NSE+CEA+ProGRP：癌胚抗原 100.58(ng/ml)↑；2025-12-29 急诊肾功(无二氧化碳)+急
诊肝功(无ADA)+电解质三项(急诊)+钙测定(急诊)：丙氨酸氨基转移酶 80.90(U/L)↑，天门冬
氨酸氨基转移酶 46.30(U/L)↑；凝血无特殊。患者无化疗禁忌，于2025-12-30行第2周期AC方案化
疗，具体方案为：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w，同时给予患者抑酸护胃、止
痛等对症支持治疗，今日安排患者出院。
治疗结果：好转
出院医嘱及建议：1、注意休息，加强营养；2、每周复查血常规2次、肝肾功1次，如有异常，立即
就诊。3、下周期化疗时间：2026-01-20，住院前请提前联系床位。4、出院用药：利可君片 1片 口
服 每天3次，生血宝合剂 15ml 口服 每天3次。5、
午
6、我院PICC导管维护时间：静脉导管维护门诊 每周一、周四上午。
备注（包括手术名称）：[手术记录手术名称]
时间：2025年12月31日
说明：1、此证明书未经我院加盖公章无效。 2、涂改未经加盖我院公章无效。
3、此证明仅证明病人出院时病情。 4、请妥善保管，遗失不补。
第1页/共2页
---
出院证明书
(病人保存联)
住院证字
号
姓名：
性别：男
年龄：39岁
入院时间：2026-01-21 10:07
出院时间：2026-01-24
病人单位或住址
出院诊断：1.恶性肿瘤化学治疗 2.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR
L858R+）
3.恶性肿瘤靶向治疗
4.肝继发恶性肿瘤
5.骨继发恶性肿瘤
6.化疗相关恶心和呕吐
7.化疗后骨髓抑制
8.白细胞减少
9.恶性肿瘤的治疗后的随诊检查
诊疗小结：患者因“发现右肺上叶占位7月，右肺上叶腺癌2周期化疗后20+天。”入院。入院查体：
T36.6℃，P76次/分，R19次/分，BP113/75mmHg，专科检查：[ECOG评分：1分，胸廓正常，双肺语
颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣
膜区未闻及病理性杂音。]辅助检查：暂缺。
诊疗经过：[入院完善相关检查：2026-01-21 血常规(五分类)：白细胞计数 3.28(10^9/L)↓，血红
蛋白浓度 137.00(g/l)，血小板计数 95.00(10^9/L)↓；2026-01-21生化：丙氨酸氨基转移酶 56.80
(U/L)↑，天门冬氨酸氨基转移酶 47.50(U/L)↑，尿酸 435.00(umol/L)↑；2026-01-21 NSE+
ProGRP+CEA：癌胚抗原 114.34(ng/ml)↑，神经元特异性烯醇化酶 22.32(ng/ml)↑，胃泌素释放肽前
体 41.37(pg/ml)；凝血无特殊。心电图无明显异常。2026-01-22 胸腹部CT：1、“肺CA”复查，右
肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.4cm×4.8cm，
增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较2025-12-04片病灶略显缩小。2、双肺另
见长径约0.4-0.5cm微小结节，较大者位于右肺上叶后段（IM70），必要时随诊。3、右肺中叶及双肺
下叶见散在斑条影。上腔静脉见置管影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸
膜稍增厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大
层面范围约1.7cm×1.5cm，转移灶可能，其它病变待排。较前变化不大。6、左侧肾上腺内侧支增
粗，见结节状稍低密度影，增强扫描强化稍欠均匀，长径约1.2cm，占位性病变或转移灶待排。较前
变化不大。7、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐
骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能。病情评价好转，排除于2026-1-23
行第3周期AC方案化疗，具体方案为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w，同时给予
患者抑酸护胃、止痛等对症支持治疗，现化疗已完成，于今出院回家乡休养。]
治疗结果：好转
出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就
诊。2、下周期治疗时间：2026年2月13日，请提前几天微信群预约床位，入院前尽量保持空腹状
第1页/共2页
---
民医院
出院证明书
(病人保存联)
住院证字
号
姓名：
性别：男
年龄：39岁
入院时间：2026-02-24 09:09
出院时间：2026-02-26
病人单位或住址：
出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+）
2.肝继发恶性肿
瘤
3.骨继发恶性肿瘤
4.恶性肿瘤靶向治疗
5.化疗后血小板减少
6.姑息性化疗
诊疗小结：患者因“右肺上叶腺癌3周期化疗后20+天。”入院。入院查体：T36.4℃；P93次/分；
R18次/分；BP107/70mmHg，专科检查：ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，
双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。
诊疗经过：完善检查，2026-02-24
血常规(五分类)：血小板计数 106.00(10^9/L)↓；2026-02-24
CEA+ProGRP+NSE：癌胚抗原 150.61(ng/ml)↑，神经元特异性烯醇化酶 31.31(ng/ml)↑；
2026-02-24
凝血四项+血浆D一二聚体测定：纤维蛋白原 4.81(g/L)↑，D-二聚体 0.60(mg/L FEU)
↑；2026-02-24
急诊肾功(无二氧化碳)+急诊肝功(无ADA)+电解质三项(急诊)+钙测定(急
诊)：钠 136.00(mmol/L)↓；患者无化疗禁忌，2026-02-25开始行第4周期AC方案化疗，具体方案
为：培美曲塞 0.8g ivgtt dl+卡铂 0.5g ivgtt dl q3w+阿美替尼110mg po qd，患者治疗结束，复
查2026-02-26[左上肢静脉,血管彩超]，左上肢静脉未见明显异常。予以拔除PICC管后办理出院。
治疗结果：好转
出院医嘱及建议：出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就
诊。2、下周期治疗时间：2026年3月18日，肿瘤科门诊或日间放化疗门诊完成治疗。3、出院带
药：-。4、
5、加强营养，清淡饮食，避免着凉，预防感染，不适随诊。
备注(包括手术名称)：[手术记录手术名称]
时间：2026年02月26日
说明：1、此证明书未经我院加盖公章无效。
2、涂改未经加盖我院公章无效。
3、此证明仅证明病人出院时病情。
4、请妥善保管，遗失不补。
---
出院证明书
(病人保存联)
住院证字
号
性别：男 年龄：39岁 入院时间：2026-03-23 10:38
床号
出院时间：2026-03-25
病人单位或住址：
出院诊断：1.右肺上叶腺癌伴肝脏、骨多发转移（cT4N2M1 IVB期 EGFR L858R+） 2.肝继发恶性肿
瘤 3.骨继发恶性肿瘤 4.肝功能不全
诊疗小结：患者因“右肺上叶腺癌4周期化疗后1+月。”入院。入院查体：T36.4℃ ;P93次/分；
R18次/分;BP107/70mmHg
诊疗经过：完善检查，2026-03-23 急诊肾功(无二氧化碳)+急诊肝功（无ADA）+电解质三项（急
诊）+钙测定（急诊）:丙氨酸氨基转移酶 84.50(U/L)↑，天门冬氨酸氨基转移酶 47.40(U/L)↑；
2026-03-23 CEA+ProGRP+NSE:癌胚抗原 163.87(ng/ml)↑，神经元特异性烯醇化酶 49.25(ng/ml)
↑；2026-03-23 凝血四项+血浆D-二聚体测定:纤维蛋白原 4.04(g/L)↑，D-二聚体 1.02(mg/L
FEU)↑；2026-03-23 血常规(五分类)：淋巴细胞百分率 15.30(%)↓，淋巴细胞计数 1.04(10^9/L)
↓。2026-03-25 [*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强],1、“肺CA”复查，右
肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截断，较大层面范围约5.6cm×5.3cm，
增强扫描呈轻度不均匀强化，周围见斑条影及小结节影，较CT260121-240片病灶稍增大。2、双肺另
见长径约0.4-0.7cm微小结节，较大者位于右肺上叶前段（IM37）较前片稍增大，必要时随诊。3、右
肺中叶及双肺下叶见散在斑条影。4、心包少量积液。纵隔淋巴结显示，部分稍增大。双侧胸膜稍增
厚。5、肝右后叶见稍低密度结节，边缘稍模糊，增强扫描轻中度强化，边缘强化明显，较大层面范
围约1.2cm×0.9cm，转移灶可能，其它病变待排，较前稍缩小。6、左侧肾上腺内侧支增粗，见结节
状稍低密度影，增强扫描强化稍欠均匀，长径约1.4cm，占位性病变或转移灶待排。较前稍增大。7、
胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。8、右肾见稍低密度结节，较大者长径1.3cm，
增强扫描似见轻度强化，占位性病变或转移灶待排。较前变化不大。9、前列腺稍显丰满，强化稍欠
均匀。10、扫及双侧部分肋骨，胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻骨、坐骨、双
侧股骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，部分椎体变扁，病理性骨折待排。患者肝
功能不全，予以保肝治疗，患者病情进展，考虑参加临床实验，予以办理出院。
治疗结果：好转
出院医嘱及建议：1、每周复查血常规，每2周复查肝肾功，如有异常，及时就诊。 2、等待电话通
知临床试验筛查。 3、出院带药：-。4、门诊随访：
5、加强营养，清淡饮食，避免着凉，预防感
第1页/共2页
---
入院记录
姓名：
性别：男
年龄：38岁
婚姻状况：已婚
出生地：
民族：汉族
现住址：
职业：自由职业者
入院时间：2025-09-09 10:41
记录时间：2025-09-09 11:01
病史陈述者
联系人姓名：
联系人电话：
病史真实性确认签字：
主诉：咳嗽3+月，发现右上肺占位10+天
现病史：入院前3+月，患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未行治疗，病程中患者上述症状持续存在。10+天前，患
民医院就诊，完善胸部CT
提示“1.右上肺见团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑
占位性病变，肺Ca可能性大。建议结合临床进一步检查。2.双肺散在点结影及条索影。3.纵隔内可见
淋巴结显示，部分稍大。4.心脏形态大小未见异常。5.双侧胸腔未见确切积液征象。6.扫及肝右叶见
片状密度低影，长径约2.7cm，性质?建议进一步检查。7.扫及胸椎多个椎体骨质密度减低破坏改
变，考虑转移可能”，患者为进一步治疗遂于我科住院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+
NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段
测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块，肿瘤占位性病变可能，其它待排。2、双肺
另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在斑条影。4、纵膈见多发淋巴结显示，部分
稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低密度结节，占位性病变可能，转移灶待排，
必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破
坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦性心律 2.电轴左偏。建议完善经皮肺穿刺
检查后纤支镜下肺活检明确，患方商议后表示拒绝，现患者为进一步明确占位性质，遂于我院门诊就
诊，门诊以“右上肺占位”收入我科。
自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。
既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病
史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。
过敏史：否认食物、药物过敏史。
个人史：出生原籍，长期居住生长于当地，否认疫区居住治游史，平素偶有饮酒，否认吸烟及
人民医院
入院记录
家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。
体格检查
T36.1℃
P92次/分
R19次/分
BP121/83mmHg
一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮
疹。背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部
及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。
颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊
清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，HR92次/分，律齐，各
瓣膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性
浊音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经
系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。
专科情况
背部可触及一大小约2cm*1cm包块，质稍硬，活动度差。胸廓正常，双肺语颤正常，双肺叩诊清
音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心界不大，HR92次/分，律齐，各瓣膜区未闻
及病理性杂音。
辅助检查
2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性烯醇
化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑；[*胸部,增强],1、右肺上叶团块,
肿瘤占位性病变可能，其它待排。2、双肺另见小结节，必要时随诊。3、右肺中叶及双肺下叶见散在
斑条影。4、纵膈见多发淋巴结显示，部分稍大。5、心包少量积液。左侧胸膜稍增厚。6、肝右叶低
密度结节，占位性病变可能，转移灶待排，必要时进一步检查。7、扫及双侧部分肋骨，胸椎多个椎
体、胸骨多发结节状、斑片状溶骨性骨质破坏，转移灶可能，T2椎体病理性骨折可能。心电图：1.窦
性心律 2.由缺血性
---
入院记录
姓名：
性别：男
年龄：
婚姻状况：未婚
出生地：
民族：汉族
现住址：
职业：自由职业者
入院时间：2026-03-23 10:38
记录时间：2026-03-23 10:46
病史陈述者：
联系人姓名：
联系人电话：
病史真实性确认签字：
主诉：右肺上叶腺癌4周期化疗后1+月。
现病史：2025-06患者无明显诱因出现咳嗽、咳痰等不适，为白色粘痰，量少，患者未重视，未
行治疗，病程中患者上述症状持续存在。
民医院就诊，完善胸部CT提示“1.右上肺见
团块影，形态不规则，内密度欠均，相应气管受压变窄，大小约6.4cm*8.2cm,考虑占位性病变，肺Ca
可能性大。3.纵隔内可见淋巴结显示，部分稍大。扫及肝右叶见片状密度低影，长径约2.7cm，性
质？，扫及胸椎多个椎体骨质密度减低破坏改变，考虑转移可能”，患者为进一步治疗遂于我科住
院，完善2025-09-01 CYFRA21-1+CEA+ProGRP+NSE+SCCA:癌胚抗原 94.90(ng/ml)↑，神经元特异性
烯醇化酶 58.93(ng/ml)↑，细胞角蛋白19片段测定 62.83(ng/ml)↑，行胸部增强CT检查示：右肺上
叶团块，肿瘤占位性病变可能，其它待排。纵膈见多发淋巴结显示，部分稍大。肝右叶低密度结节，
占位性病变可能，转移灶待排，扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性
骨质破坏，转移灶可能，T2椎体病理性骨折可能。于2025-09-10行经皮肺穿刺活检，免疫组化结果电
话询问病理科腺癌可能性大，2025-09-15报告回示：病理诊断（右肺包块，穿刺活检）结合免疫组化
结果：癌细胞CK（+），CK7（+），TTF-1（+），NapsinA（+），Ki67（+，约60%），CK20（-），
SATB2（-），支持肺腺癌。基因检查示：EGFR L858R+,MET 扩增，ERBB2 扩增，TP53突变，PD-L1<
1%。于2025-09-24开始口服阿美替尼靶向治疗（110mg po qd）。2025-12-04复查胸腹部增强CT：病
情评价好转。于2025-12-5、2025-12-30、2026-1-23、2026-02-05行4周期AC方案化疗联合靶向治
疗，具体：培美曲塞 0.8g ivgtt d1+卡铂 0.5g ivgtt d1 q3w+阿美替尼 110mg qd。现患者为进一
步治疗于我院就诊，门诊以“右肺上叶腺癌”收入我科。
自患病以来，患者精神食欲、睡眠、精神一般，大小便正常，近期体重变化不详。
既往史：否认“糖尿病、高血压、高血脂”病史，预防接种史不详，否认结核、肝炎等传染病
史，否认重大外伤史，否认手术史，否认精神病史。无输血及血液制品史。
过敏史：否认食物、药物过敏史。
个人史：出生原籍，长期居住生长于当地，否认疫区居住冶游史，平素偶有饮酒，否认吸烟及
第1页
入院记录
其他不良嗜好。
婚育史：适龄结婚，育有1子，家人均体健。
家族史：否认家族性遗传病、精神病史，否认家族性肿瘤病史。
体格检查
T36.4℃
P95次/分
R19次/分
BP101/77mmHg
一般情况：发育正常，体型消瘦，步入病房，神志清醒，查体合作。皮肤黏膜：无黄染皮
疹。背部可触及一大约2cm*1cm包块，质稍硬，活动度差。淋巴结：浅表淋巴结未扪及肿大。头部
及其器官：头颅五官形态无畸形，双瞳等大，形圆，光敏。口唇无发绀，咽不充血，扁桃体不大。
颈部：颈软，气管居中，颈静脉无怒张，甲状腺无肿大。胸部：胸廓正常，双肺语颤正常，双肺叩诊
清音，双肺呼吸音清，未闻及明显干湿啰音及胸膜摩擦音。心脏：心界不大，H95次/分，律齐，各瓣
膜区未闻及病理性杂音。腹部：腹平软，无压痛、无反跳痛、肌紧张，肝肾区无叩痛，无移动性浊
音，肠鸣音正常。直肠肛门外生殖器：未查。脊柱四肢：脊柱、四肢无异常。双下肢不肿。神经
系统：腹壁反射、肱二头肌、肱三头肌、跟腱、膝腱反射正常，巴彬斯基征，、脑膜刺激征阴性。
专科情况
ECOG评分：1分，胸廓正常，双肺语颤正常，双肺叩诊清音，双肺呼吸音清，未闻及明显干湿啰
音及胸膜摩擦音。心界不大，律齐，各瓣膜区未闻及病理性杂音。
辅助检查
暂缺。
初步诊断：
1.右肺上叶腺癌伴肝脏、骨多发转移（
cT4N2M1 IVB期 EGFR L858R+）
2.肝继发恶性肿瘤
3.骨继发恶性肿瘤
医师签名
第2页
---
医学影像检查报告单
住院
检查号：
患者姓名：
性别：男
患者年龄：38岁
申请科室：
床号：
设备名称：CT1(联影CT)(1住)
检查部位：[*胸部,增强]
联系电话：
检查技师：
检查时间：2025-09-01 08:34:37
报告时间：2025/9/1 9:31:33
描述：
右肺上叶见团块影，边缘呈分叶状，局部与胸膜粘连，见支气管截
断，较大层面范围约7.9cm×6.9cm，增强扫描呈轻度不均匀强化，周围
见斑条影及小结节影。双肺另见长径约0.4-0.6cm实性小结节。右肺中
叶及双肺下叶见散在斑条影。纵膈见多发淋巴结显示，部分稍大。心脏
不大，心包少量积液。左侧胸膜稍增厚。肝右叶见数个类圆形低密度
影，较大者长径约2.5cm，增强扫描两期强化程度CT值相差25HU。扫及
双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨性骨质破
坏，T2椎体见多发骨折线影。
总结意见：
1、右肺上叶团块，肿瘤占位性病变可能，其它待排。
2、双肺另见小结节，必要时随诊。
3、右肺中叶及双肺下叶见散在斑条影。
4、纵膈见多发淋巴结显示，部分稍大。
5、心包少量积液。左侧胸膜稍增厚。
6、肝右叶低密度结节，占位性病变可能，转移灶待排，必要时进一步
检查。
7、扫及双侧部分肋骨，胸椎多个椎体、胸骨多发结节状、斑片状溶骨
性骨质破坏，转移灶可能，T2椎体病理性骨折可能。
请结合临床及其它检查，必要时复查或进一步检查。
报告者：申悦
审核医师：马婉军
页 尾页
---
住院号
门诊号：-
病理号[
姓名
性别 男
年龄 38岁
病人编号
病区
就诊号
收到日期 2025-09-10
送检科室
送检单位 本院
送检医生
标本名称 右肺包块
临床诊断
肉眼所见
(右肺包块)灰白色组织多粒,直径0.4cm,点纸全
病理诊断
(右肺包块,穿刺活检)结合免疫组化结果:癌细胞CK(+),CK7(+),TTF-1(+),NapsinA(+),Ki67(+,约60%),CK20(-),SATB2(-),
支持肺腺癌。
报告医生 阙柳
审核医生 阙柳
复诊医生
报告时间 2025-09-15
2026-08-10 15:43:24,159 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=检测概览
基本信息
受检者信息
样本信息
临床信息
姓名
样本编号：
临床/病理诊断：肺癌怀疑骨转移肝转移
性别：男
样本类型：石蜡块
手术史/用药史：/
年龄：38岁
采样部位：/
既往基因检测结果：/
送检单位
家族史：/
采集日期：
接收日期：2025-09-18
报告日期：2025-09-21
本报告中的临床诊断等信息来自受检者送检时提供的信息，而非来自检测结果。
项目简介
项目名称
肺癌靶向18基因检测
检测方法
目标区域探针捕获技术和二代测序技术(Next-Generation Sequencing,NGS)
检测范围
本检测基于非小细胞肺癌指南和专家共识，检测非小细胞肺癌靶向治疗和预后相关的18个基因(包括：EGFR、ALK、MET、ROS1、BRAF、RET、ERBB2(HER2)、KRAS、NTRK1/2/3、NRAS、PIK3CA、AKT1、FBXW7、DDR2、NRG1、TP53)，变异类型包含相应基因的点突变、插入/缺失，拷贝数变异和基因融合/重排。
检测流程
核酸提取、文库制备、高通量测序、生物信息分析及报告解读
参考指南及数据库
NCCN指南、CSCO指南、OncoKB、COSMIC、CKB、ClinVar等
参考基因组
GRCh37/hg19
检测结果汇总
基因变异结果（共5个）
基因
转录本/外显子
cDNA改变
氨基酸改变
变异类型
变异丰度/拷贝数
变异分类
EGFR
NM_005228.5:exon21
c.2573T>G
p.L858R
错义突变
51.28%
I类[重要临床意义]
ERBB2(HER2)
NM_004448.4
/
/
拷贝数扩增
拷贝数=3.6
I类[重要临床意义]
MET
NM_000245.4
/
/
拷贝数扩增
拷贝数=3.1
I类[重要临床意义]
TP53
NM_000546.6:exon6
c.598_611del
p.N200Vfs*4
移码突变
61.75%
II类[潜在临床意义]
第1页
TP53
NM_000546.6:exon6
c.629A>C
p.N210T
错义突变
62.88%
III类[临床意义不明]
注：
《肿瘤二代测序临床报告解读共识》指出，基因变异按照其临床意义的重要性分为4类：
I类：有重要的临床意义，与治疗、预后和诊断相关；
II类：有潜在的临床意义，与治疗、预后和诊断相关；
III类：临床意义不明(临床意义不明是指目前尚无充分证据证实这些基因变异与肿瘤的致病性关系，尚无相关用药提示，未来可能随着研究的深入而更新致病性及药物证据等级)；
IV类变异，无害或可能无害。
本报告只列出I、II、III类变异。
靶向用药基因检测提示
靶向用药基因检测提示
基因
变异信息
变异丰度/拷贝数
(A级)
FDA/NMPA
指南推荐用药
(B级)
专家共识推荐用药
(C级)
跨适应症
(C级)
临床试验药物
(D级)
临床前研究
奥希替尼
(敏感)
奥希替尼+
化疗
(敏感)
埃万妥单抗+
兰泽替尼
(敏感)
埃万妥单抗+
化疗
(敏感)
阿美替尼
(敏感)
伏美替尼
(敏感)
达可替尼
(敏感)
吉非替尼
(敏感)
阿法替尼±
西妥昔单抗
(敏感)
埃克替尼
(敏感)
贝福替尼
(敏感)
厄洛替尼±
雷莫西尤单抗
或贝伐珠单抗
(敏感)
瑞厄替尼
(敏感)
瑞齐替尼
德达博妥单抗+
奥希替尼
(敏感)
Patritumab
Deruxtecan
(敏感)
BDTX-1535
(敏感)
WSD0922
(敏感)
HLX42
(敏感)
SHR-A2009
(敏感)
BL-B01D1
(敏感)
阿美替尼+
化疗
(敏感)
EGFR
c.2573T>G,
p.L858R,
Exon21
51.28%
/
/
/
/
第 2 页
(敏感)
佐利替尼
(敏感)
利厄替尼
(敏感)
德达博妥单抗
(敏感)
芦康沙妥珠单
抗
(敏感)
依沃西单抗+
培美曲塞+
卡铂
(敏感)
奥希替尼+
赛沃替尼
(敏感)
伯瑞替尼
(敏感)
克唑替尼
(敏感)
卡马替尼
(敏感)
特泊替尼
(敏感)
EGFR-TKIs
(耐药)
谷美替尼
(敏感)
EGFR-TKIs+
MET-TKIs
(敏感)
/
伯瑞替尼+
PLB1004
(敏感)
SYM015
(敏感)
特泊替尼+
吉非替尼
(敏感)
特泊替尼+
奥希替尼
(敏感)
赛沃替尼
(敏感)
MET
扩增
拷贝数
=3.1
/
德曲妥珠单
抗
(敏感)
泽尼达妥单
抗
(敏感)
帕博利珠单
抗+
曲妥珠单抗+
化疗
(敏感)
帕妥珠单抗+
曲妥珠单抗+
化疗
(敏感)
恩美曲妥珠
单抗
(敏感)
维迪西妥单
抗
(敏感)
吡咯替尼
(敏感)
阿法替尼
(敏感)
帕妥珠单抗+
曲妥珠单抗
(敏感)
吡咯替尼+
阿帕替尼
(敏感)
维迪西妥单抗+
替雷利珠单抗+
贝伐珠单抗
(敏感)
维迪西妥单抗+
安罗替尼
(敏感)
ERBB2
(HER2)
扩增
拷贝数
=3.6
EGFR-TKIs
(耐药)
/
Tarloxotinib
(敏感)
TAS0728
(敏感)
BDTX-189
(敏感)
c.598_611del
p.N200Vfs*4
Exon6
61.75%
/
/
/
Adavosertib
(敏感)
CTX-1
(敏感)
CEP-8983
(敏感)
TP53
---
患者信息
姓名
性别
男
年龄
38岁
送检单位
样本信息
样本编号
样本类型
采样部位
样本采集日期
样本接收日期
报告日期
石蜡块
—
2025-09-18
2025-09-20
检测项目
PD-L1蛋白表达检测
抗体型号
临床信息
临床/病理诊断
肺癌怀疑骨转移肝转移
手术史/用药史
—
二、检测结果
检测内容
检测结果
检测结果提示
PD-L1蛋白
TPS
<1%
PD-L1蛋白表达。
表达水平
CPS
1
TC
<1%
IC
1%
检测结果图示
PDL1×200
HE×200
---
医学影像检查报告单
扫码查看影像
检查号:
患者姓名:
性别:男
年龄:39岁
住院号:
申请科室
床号:023
联系电话
检查室:CT1(联影CT)(1住)
检查技师:羊媛颖
检查时间:2026-03-25 08:22:58
检查部位:[*盆腔,增强][*上腹部,增强][*下腹部,增强][*胸部,增强]
检查技术:-
描述:
1、“肺CA”复查,右肺上叶见团块影,边缘呈分叶状,局部与胸膜粘连,见支气
管截断,较大层面范围约5.6cm×5.3cm,增强扫描呈轻度不均匀强化,周围见斑条
影及小结节影,较CT260121-240片病灶稍增大。
2、双肺另见长径约0.4-0.7cm微小结节,较大者位于右肺上叶前段(IM37)较前片
稍增大,必要时随诊。
3、右肺中叶及双肺下叶见散在斑条影。
4、心包少量积液。纵隔淋巴结显示,部分稍增大。双侧胸膜稍增厚。
5、肝右后叶见稍低密度结节,边缘稍模糊,增强扫描轻中度强化,边缘强化明
显,较大层面范围约1.2cm×0.9cm,转移灶可能,其它病变待排,较前稍缩小。
6、左侧肾上腺内侧支增粗,见结节状稍低密度影,增强扫描强化稍欠均匀,长径
约1.4cm,占位性病变或转移灶待排。较前稍增大。
7、胆囊、胰腺、脾脏、左肾、膀胱未见确切异常强化影。
8、右肾见稍低密度结节,较大者长径约1.3cm,增强扫描似见轻度强化,占位性病
变或转移灶待排。较前变化不大。
9、前列腺稍显丰满,强化稍欠均匀。
10、扫及双侧部分肋骨,胸腰骶椎多个椎体及附件、胸骨、双侧肱骨、髂骨、耻
骨、坐骨、双侧股骨多发结节状、斑片状溶骨性骨质破坏,转移灶可能,部分椎体
变扁,病理性骨折待排。
请结合临床及其它检查,必要时复查或进一步检查。
总结意见:
见上述。
报告者:申悦
审核医师:曹玉
报告时间:2026/3/25 8:48:11
审核时间:2026/3/25 9:26:23
注:此报告审核
2026-08-10 15:43:24,427 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 15:43:24,427 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "19 items, types={'LabReport': 6, 'DischargeRecord': 6, 'AdmissionRecord': 2, 'ExaminationReport': 5}", "name": "腺癌TKI耐药ZHDO，39岁.pdf", "embedding_token_consumption": 13576}
2026-08-10 15:43:24,427 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 15:43:24,786 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 15:43:24,786 INFO     29 [Trace] task=a18ddf0c | doc=腺癌TKI耐药ZHDO，39岁.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":19,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int len=9 row[0]=(16, 41, 82, 168, 180) row[-1]=(16, 41, 91, 278, 290)
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int len=13 row[0]=(17, 44, 65, 155, 166) row[-1]=(17, 44, 67, 356, 367)
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int len=18 row[0]=(18, 47, 82, 163, 174) row[-1]=(18, 41, 102, 387, 398)
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(19, 107, 148, 189, 202) row[-1]=(19, 107, 190, 217, 229)
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int len=7 row[0]=(20, 47, 110, 160, 171) row[-1]=(20, 44, 82, 237, 247)
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int len=25 row[0]=(21, 39, 95, 142, 154) row[-1]=(21, 33, 90, 476, 489)
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,796 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,797 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,797 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,797 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:43:24,804 INFO     29 set_progress(a18ddf0c94d011f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 15:43:24 [DOC Engine]:
Start to index...
2026-08-10 15:43:24,842 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.032s]
2026-08-10 15:43:24,846 INFO     29 set_progress(a18ddf0c94d011f1bd9827cf206dfa2d), progress: 0.8052631578947369, progress_msg: 
2026-08-10 15:43:24,874 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.020s]
2026-08-10 15:43:24,908 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.022s]
2026-08-10 15:43:24,937 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 15:43:24,953 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 15:43:24,960 INFO     29 set_progress(a18ddf0c94d011f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 15:43:24 Indexing done (0.16s). Task done (643.37s)
2026-08-10 15:43:24,966 INFO     29 [Done], chunks(19), token(13576), elapsed:643.37
2026-08-10 15:43:25,283 INFO     29 handle_task done for task {"id": "a18ddf0c94d011f1bd9827cf206dfa2d", "doc_id": "a144653494d011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "type": "pdf", "location": "\u817a\u764cTKI\u8010\u836fZHDO\uff0c39\u5c81.pdf", "size": 7949713, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786375920977, "task_type": "dataflow", "root_trace_id": "fc2f2d0d6f6743e8bdd3d39db33f19f0", "root_traceparent": "00-fc2f2d0d6f6743e8bdd3d39db33f19f0-fdc03106ebb553e0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
