# 基准结果：LXQI222.pdf

## 基本信息

- 文件：`LXQI222.pdf`
- 大小：62937.7 KB
- PDF 总页数：10
- doc_id：`b9a7e47a94ad11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T19:22:06  完成时间：2026-08-10T19:28:02  耗时：355.9s
- progress_msg：`11:27:58 Indexing done (0.04s). Task done (333.01s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | d8562293 | 4 | 1-4 | 入院记录 姓名： 床号：23-03床 病历号：0 科室：呼吸与危重医学科医生 站 |
| 2 | c3b833e8 | 3 | 5-7 | 出院记录 姓名： 床号：23-03床 病历号：0 科室：呼吸与危重医学科医生站  |
| 3 | 3c28417d | 2 | 8-9 | 肺功能通气阻力检查报告 姓名： 性别：女 身高：151 cm 病历号： 年龄：7 |
| 4 | 160b4dac | 1 | 10-10 | 亦康互联网医院 普通 处方 已使用 已使用 已使用 联 处方笺 已使用 NO.: |

- chunks 总数：4
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- 覆盖页数：10 / 10；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 1 | 1 | 1 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "DischargeRecord": 1, "ExaminationReport": 1, "PrescriptionRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 4, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 11:27:57,607 INFO     29 [ChunkMerger] Merged 4 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 11:22:13,547 INFO     29 handle_task begin for task {"id": "ba5d751a94ad11f1bd9827cf206dfa2d", "doc_id": "b9a7e47a94ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360930217, "task_type": "dataflow", "root_trace_id": "2d4fcd13324b447999508dc50afac2e4", "root_traceparent": "00-2d4fcd13324b447999508dc50afac2e4-817dc24fdd0315e5-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:22:13,808 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 11:22:13,931 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 11:22:13,985 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:22:13,985 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 11:22:13,985 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 11:22:14,008 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 11:22:14,008 INFO     29 ============================================================
2026-08-10 11:22:14,008 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 11:22:14,008 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 11:22:14,008 INFO     29 ============================================================
2026-08-10 11:22:14,008 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 11:22:14,008 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 11:22:14,021 INFO     29 No torch found.
2026-08-10 11:22:16,490 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=10
2026-08-10 11:22:16,619 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1110594, prompt_len=764
2026-08-10 11:22:17,926 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:22:17,926 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 11:22:17,938 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1110594, prompt_len=401
2026-08-10 11:22:23,275 INFO     29 [qwen-vl-parser] text API response (len=942):
["入院记录", "姓名：", "床号：23-03床", "病历号：0", "科室：呼吸与危重医学科医生", "站", "姓名：", "性别：女", "年龄：72岁", "出生地：贵州省贵阳市", "职业：退休人员", "民族：汉族", "婚姻：已婚", "联系地址：中国贵州省贵阳市", "入院时间：2025-10-30 14:34", "病史陈述者：本人", "主诉：咳嗽、咳痰5年，加重1周", "现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，", "不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管", "哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感", "和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治", "就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二", "便如常，近1年体重减少4kg。", "既往史：", "患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染", "病；食物、药物过敏无；无外伤史：无手术史：无输血史：无中毒史：无长期用药史：无可能成瘾药物。疫", "苗接种史不详", "个人史：", "出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长", "地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物", "质接触史。", "婚育史：", "已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。", "月经史：", "初潮年龄17岁", "经期3-4天", "绝经年龄53岁 月经及白带情况：正常", "月经周期30天", "家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否", "认二系三代有遗传病史。患者否认有遗传倾向的疾病。", "体格检查", "生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60"]
2026-08-10 11:22:23,277 INFO     29 [qwen-vl-parser] page=1 text: 42 lines (bbox 0-41)
2026-08-10 11:22:23,277 INFO     29 [qwen-vl-parser] page=1 text: 42 sections
2026-08-10 11:22:23,408 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935099, prompt_len=764
2026-08-10 11:22:24,457 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:22:24,458 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 11:22:24,470 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935099, prompt_len=401
2026-08-10 11:22:28,359 INFO     29 [qwen-vl-parser] text API response (len=683):
["体格检查", "生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体", "重：44kg，腰围：cm，BMI：18.8 kg/m²", "一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常", "表情：正常体位：自主体位步态：平稳配合检查：配合", "皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无", "皮疹：无紫癜：无", "1/3", "贵州醫科大學附属醫院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "入院记录", "姓名：", "床号：23-03床", "病历号", "科室：呼吸与危重医学科医生", "站", "水肿：无脱水现象：无松紧度：适中", "温度：适中出汗：无显性出汗瘢痕：无感染：无", "头颅：大小：正常畸形：无包块：无", "凹陷：无压痛：无", "眼：眼睑：无水肿结膜：无充血巩膜：无黄染", "眼球四个象限运动：左眼：正常右眼：正常", "眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆", "对光反射：左眼：灵敏右眼：灵敏", "鼻：外形：正常其他异常：无鼻旁窦压痛：无", "口：唇：无紫绀粘膜：无充血腮腺导管开口：正常", "舌：伸舌居中牙龈：无肿胀龋齿：无", "咽喉：扁桃体：正常咽：无充血声音：正常", "淋巴：淋巴结：全身浅表淋巴结未及肿大", "颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张", "气管：居中颈静脉回流征：无", "甲状腺：无肿大"]
2026-08-10 11:22:28,360 INFO     29 [qwen-vl-parser] page=2 text: 32 lines (bbox 42-73)
2026-08-10 11:22:28,360 INFO     29 [qwen-vl-parser] page=2 text: 32 sections
2026-08-10 11:22:28,485 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=753919, prompt_len=764
2026-08-10 11:22:29,542 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:22:29,542 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 11:22:29,560 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=753919, prompt_len=401
2026-08-10 11:22:33,084 INFO     29 [qwen-vl-parser] text API response (len=559):
["眼球四个象限运动：左眼：正常 右眼：正常", "眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆", "对光反射：左眼：灵敏 右眼：灵敏", "鼻：外形：正常 其他异常：无 鼻旁窦压痛：无", "口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常", "舌：伸舌居中 牙龈：无肿胀 龋齿：无", "咽 喉：扁桃体：正常 咽：无充血 声音：正常", "淋巴 巴：淋巴结：全身浅表淋巴结未及肿大", "颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张", "气管：居中 颈静脉回流征：无", "甲状腺：无肿大", "胸部 部：胸廓：无畸形 乳房：", "肺 部：视诊：呼吸运动", "触诊：", "叩诊：", "听诊：", "语音传导", "心 脏：视诊：", "触诊：心尖搏动", "叩诊：", "心界", "右(cm)", "肋间", "左(cm)", "2", "2", "2", "3", "(左锁骨中线距胸骨线7.5cm)", "听诊：心率：92次/分 心律：齐 心音：未闻及异常心", "额外心音：无 杂音：无 心包摩擦感：", "周围血管：异常血管征：无", "腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出", "其他异常：无", "触诊：腹壁：柔软 压痛：无", "2/3"]
2026-08-10 11:22:33,085 INFO     29 [qwen-vl-parser] page=3 text: 36 lines (bbox 74-109)
2026-08-10 11:22:33,086 INFO     29 [qwen-vl-parser] page=3 text: 36 sections
2026-08-10 11:22:33,186 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=654032, prompt_len=764
2026-08-10 11:22:34,245 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:22:34,245 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 11:22:34,257 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=654032, prompt_len=401
2026-08-10 11:22:38,224 INFO     29 [qwen-vl-parser] text API response (len=489):
["站", "反跳痛：无", "液波振颤：无 振水声：无", "腹部包块：无", "肝：肋下未及", "胆囊：未触及 Murphy征：阴性", "脾：未触及", "叩诊：肝浊音界：正常 移动性浊音：无", "肾区叩痛：无", "听诊：肠鸣音：正常 肠鸣音频率：4次/分", "气过水音：无 血管杂音：无", "肛门直肠：未检", "生殖器：未检", "脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限", "压痛，叩痛：无", "杵状指趾：无", "神经系统：腹壁反射：正常 肢体瘫痪：无", "肌张力：正常 肌力：V级", "肱二头肌反射：正常 Hoffman征：阴性", "膝腱反射：正常 Kernig征：阴性", "跟腱反射：正常 Babinski征：阴性", "其他：无", "补充及专科情况", "双肺呼吸音清，未闻及干湿性啰音。", "辅助检查：暂无", "VTE评估：", "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "入院诊断：1.支气管哮喘急性发作期", "医师签名：", "日期：2025-10-30 16:38"]
2026-08-10 11:22:38,225 INFO     29 [qwen-vl-parser] page=4 text: 30 lines (bbox 110-139)
2026-08-10 11:22:38,225 INFO     29 [qwen-vl-parser] page=4 text: 30 sections
2026-08-10 11:22:38,474 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1934597, prompt_len=764
2026-08-10 11:22:39,716 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:22:39,717 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 11:22:39,727 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1934597, prompt_len=401
2026-08-10 11:22:42,617 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:22:42.616+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 21, "failed": 0, "current": {"ba5d751a94ad11f1bd9827cf206dfa2d": {"id": "ba5d751a94ad11f1bd9827cf206dfa2d", "doc_id": "b9a7e47a94ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360930217, "task_type": "dataflow", "root_trace_id": "2d4fcd13324b447999508dc50afac2e4", "root_traceparent": "00-2d4fcd13324b447999508dc50afac2e4-817dc24fdd0315e5-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:22:47,268 INFO     29 [qwen-vl-parser] text API response (len=1305):
["出院记录", "姓名：", "床号：23-03床", "病历号：0", "科室：呼吸与危重医学科医生站", "姓名：", "性别：女", "年龄：72岁", "民族：汉族", "病历号：00", "科室：呼吸与危重医学科医生站", "入院日期：2025-10-30 14:34", "住院天数：8", "出院日期：2025-11-07 11:44", "籍贯：贵州省贵阳市", "职业：退休人员", "单位：贵阳供电局", "住址：中国贵州省贵阳", "入院情况：", "李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无", "明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯", "血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治", "疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1", "周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门", "诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体", "重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病", "史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无", "中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学", "历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗", "史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已", "故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患", "者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，", "血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。", "心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检", "查：暂无", "入院诊断：1.支气管哮喘急性发作期", "诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床", "检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1", "2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝", "功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中"]
2026-08-10 11:22:47,269 INFO     29 [qwen-vl-parser] page=5 text: 40 lines (bbox 140-179)
2026-08-10 11:22:47,269 INFO     29 [qwen-vl-parser] page=5 text: 40 sections
2026-08-10 11:22:47,705 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2975581, prompt_len=764
2026-08-10 11:22:48,894 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:22:48,896 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 11:22:48,920 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2975581, prompt_len=401
2026-08-10 11:22:57,534 INFO     29 [qwen-vl-parser] text API response (len=1447):
["心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中", "心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml", "肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移", "酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD)", "0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-3", "0 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 13:11 胸部CT平扫：1、考", "虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧", "1/3", "贵州醫科大學附屬醫院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "出院记录", "姓名：", "床号：23-03床", "病历号：", "科室：呼吸与危重医学科医生站", "胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管", "扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊", "复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走", "行欠佳。 7、肝内囊性灶，建议超声随诊复查。2025-10-31 14:35 肺通气功能测定及支气管舒张试验：1.", "中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+) 2025-10-31 12:33。传染病筛查", "三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临", "床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31", "14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴", "定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。", "出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小", "结节；5.肝囊肿。", "出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查", "体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊", "区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。", "VTE评估："]
2026-08-10 11:22:57,537 INFO     29 [qwen-vl-parser] page=6 text: 32 lines (bbox 180-211)
2026-08-10 11:22:57,537 INFO     29 [qwen-vl-parser] page=6 text: 32 sections
2026-08-10 11:22:57,660 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102115, prompt_len=764
2026-08-10 11:22:58,750 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:22:58,750 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 11:22:58,764 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102115, prompt_len=401
2026-08-10 11:23:04,124 INFO     29 [qwen-vl-parser] text API response (len=909):
["床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31", "14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴", "定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。", "出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小", "结节；5.肝囊肿。", "出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查", "体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊", "区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。", "VTE评估：", "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "出院医嘱：", "1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治", "疗，定期复查肺功能，呼吸科门诊随诊；", "2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。", "3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。", "4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。", "手术名称：", "无", "出院结果：好转", "医生签名：", "日期：2025-11-07 11:44", "温馨提示", "尊敬的患者，出院后如您需复印住院资料，请关注以下温馨小提示：", "一、操作流程", "【方法一】", "1.请先打开微信“扫一扫”，扫描二维码，根据提示进行操作完成网上预约申请并回家等待。", "2/3"]
2026-08-10 11:23:04,125 INFO     29 [qwen-vl-parser] page=7 text: 29 lines (bbox 212-240)
2026-08-10 11:23:04,125 INFO     29 [qwen-vl-parser] page=7 text: 29 sections
2026-08-10 11:23:04,270 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038939, prompt_len=764
2026-08-10 11:23:06,646 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:23:06,646 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 11:23:06,658 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038939, prompt_len=401
2026-08-10 11:23:13,740 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:23:13.737+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 21, "failed": 0, "current": {"ba5d751a94ad11f1bd9827cf206dfa2d": {"id": "ba5d751a94ad11f1bd9827cf206dfa2d", "doc_id": "b9a7e47a94ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360930217, "task_type": "dataflow", "root_trace_id": "2d4fcd13324b447999508dc50afac2e4", "root_traceparent": "00-2d4fcd13324b447999508dc50afac2e4-817dc24fdd0315e5-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:23:15,063 INFO     29 [qwen-vl-parser] text API response (len=1598):
["贵州医科大学附属医院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "肺功能通气阻力检查报告", "姓名：", "性别：女", "身高：151 cm", "病历号：", "年龄：72 Years", "体重：46 kg", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "F/V in", "8", "Vol [L]", "6", "4", "1", "Vol%Vcmax", "100", "Vcmax", "20", "0", "Time [s]", "0", "1", "2", "3", "4", "5", "6", "2.0", "R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]", "1.5", "1.0", "0.5", "0.0", "0.4", "0.2", "0.2", "0.4", "F [Hz]", "5", "10", "15", "20", "25", "30", "35", "日期", "时间", "预计值", "实测值", "实/预", "25/10/31", "14:29:33", "MV", "[L/min]", "6.57", "11.52", "175.3", "VT", "[L]", "0.33", "0.79", "239.6", "BF", "[1/min]", "20.00", "14.63", "73.1", "VC MAX", "[L]", "2.03", "1.48", "73.0", "ERV", "[L]", "0.57", "0.14", "25.5", "IC", "[L]", "1.46", "1.34", "91.6", "FVC", "[L]", "1.93", "1.44", "74.8", "FEV 1", "[L]", "1.56", "0.91", "58.4", "FEV 1 % FVC", "[%]", "63.38", "FEV 1 % VC MAX", "[%]", "75.42", "61.67", "81.8", "PEF", "[L/s]", "5.04", "2.51", "49.8", "MEF 75", "[L/s]", "4.66", "1.54", "33.1", "MEF 50", "[L/s]", "3.06", "0.56", "18.2", "MEF 25", "[L/s]", "0.90", "0.22", "24.6", "MEF 75/25", "[L/s]", "2.36", "0.50", "21.1", "FET", "[s]", "4.91", "LFV", "[L/min]", "73.10", "Z at 5 Hz", "[kPa/(L/s)]", "0.43", "0.58", "135.7", "Resonant frequency", "[1/s]", "30.00", "R at 5 Hz", "[kPa/(L/s)]", "0.41", "0.57", "137.2", "R nt 20 Hz", "[kPa/(L/s)]", "0.35", "0.34", "95.3", "X at 5 Hz", "[kPa/(L/s)]", "-0.11", "-0.12", "112.5", "Rcentral", "[kPa/(L/s)]", "0.12", "Peripheral", "[kPa/(L/s)]", "0.40", "结论：", "1.中重度混合性肺通气功能障碍", "2.（阻力增加", "审核者专用章", "检查者：王美锦"]
2026-08-10 11:23:15,063 INFO     29 [qwen-vl-parser] page=8 text: 174 lines (bbox 241-414)
2026-08-10 11:23:15,063 INFO     29 [qwen-vl-parser] page=8 text: 174 sections
2026-08-10 11:23:15,186 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=849726, prompt_len=764
2026-08-10 11:23:16,493 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 11:23:16,494 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 11:23:16,511 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=849726, prompt_len=401
2026-08-10 11:23:23,908 INFO     29 [qwen-vl-parser] text API response (len=1541):
["贵州医科大学附属医院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "对比试验", "姓名：", "性别：女", "身高：151 cm", "病历号：", "年龄：72 Years", "体重：46 kg", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "3", "4", "5", "6", "7", "F/V in", "6", "Vol [L]", "4", "TLC", "ER,pleth2", "RV", "Time [min]", "Pred Act 0.0", "0.2", "0.4", "0.6", "0.8", "1.0", "日期", "时间", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "25/10/31", "14:29:33", "25/10/31", "14:53:10", "VT", "[L]", "0.33", "0.79", "239.6", "BF", "[1/min]", "20.00", "14.63", "73.1", "MV", "[L/min]", "6.57", "11.52", "175.3", "VC MAX", "[L]", "2.03", "1.48", "73.0", "1.66", "81.9", "12.2", "ERV", "[L]", "0.57", "0.14", "25.5", "IC", "[L]", "1.46", "1.34", "91.6", "FVC", "[L]", "1.93", "1.44", "74.8", "1.66", "86.2", "15.3", "FEV 1", "[L]", "1.56", "0.91", "58.4", "1.08", "68.8", "17.8", "FEV 1 % FVC", "[%]", "63.38", "64.76", "2.2", "FEV 1 % VC MAX", "[%]", "75.42", "61.67", "81.8", "64.76", "85.9", "5.0", "PEF", "[L/s]", "5.04", "2.51", "49.8", "3.35", "66.5", "33.6", "MEF 75", "[L/s]", "4.66", "1.54", "33.1", "1.72", "36.8", "11.3", "MEF 50", "[L/s]", "3.06", "0.56", "18.2", "0.83", "27.1", "49.1", "MEF 25", "[L/s]", "0.90", "0.22", "24.6", "0.36", "39.8", "62.1", "MMEF 75/25", "[L/s]", "2.36", "0.50", "21.1", "0.47", "20.0", "-4.9", "FET", "[s]", "4.91", "4.88", "-0.6", "V backextrapol. % FVC", "[%]", "3.85", "4.39", "13.9", "MVV", "[L/min]", "73.10", "结论：", "1.中重度混合性肺通气功能障碍", "2.气道阻力增加", "3.支气管舒张试验阳性 (+)", "吸入沙丁胺醇400μg", "FVC上升15.3%，增加220ml；", "审核者：", "检查者：", "贵州医科大学附属医院检查报告", "专用电子章"]
2026-08-10 11:23:23,910 INFO     29 [qwen-vl-parser] page=9 text: 171 lines (bbox 415-585)
2026-08-10 11:23:23,910 INFO     29 [qwen-vl-parser] page=9 text: 171 sections
2026-08-10 11:23:24,038 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910218, prompt_len=764
2026-08-10 11:23:25,350 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-05"}
```
2026-08-10 11:23:25,351 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2025-12-05
2026-08-10 11:23:25,379 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910218, prompt_len=401
2026-08-10 11:23:27,567 INFO     29 [qwen-vl-parser] text API response (len=384):
["亦康互联网医院", "普通", "处方", "已使用", "已使用", "已使用", "联", "处方笺", "已使用", "NO.:", "2025-12-05", "已使用", "姓名：", "性别：女处方专用章", "年龄：72岁", "已使用", "费别：自费", "科别：内科", "已使用", "临床诊断：支气管哮喘", "已使用", "Rp：", "已使用", "沙美特罗替卡松吸入粉雾剂", "已使用", "50μg:250μg*60泡", "x 3盒", "用法用量：", "口腔吸入,一日两次,一次1.0揿;", "已使用", "补充说明：处方超7日为病情需要", "已使用", "医师：邢伟", "审核：张艳梅", "处方金额：", "药房审核：", "药房调配：", "药房核对：", "药房发药：", "注：处方自开具日起3日内有效。"]
2026-08-10 11:23:27,567 INFO     29 [qwen-vl-parser] page=10 text: 40 lines (bbox 586-625)
2026-08-10 11:23:27,568 INFO     29 [qwen-vl-parser] page=10 text: 40 sections
2026-08-10 11:23:27,568 INFO     29 [qwen-vl-parser] parse_pdf done: 626 sections from 10 pages.
2026-08-10 11:23:27,576 INFO     29 Close text detector.
2026-08-10 11:23:28,026 INFO     29 Close text recognizer.
2026-08-10 11:23:28,431 INFO     29 Close recognizer.
2026-08-10 11:23:28,842 INFO     29 Close recognizer.
2026-08-10 11:23:29,291 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 11:23:29,292 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Parser:MedLink | outputs={"html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "json"}
2026-08-10 11:23:29,292 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 11:23:29,320 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:29,320 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 入院记录\n[BBOX-1] 姓名：\n[BBOX-2] 床号：23-03床\n[BBOX-3] 病历号：0\n[BBOX-4] 科室：呼吸与危重医学科医生\n[BBOX-5] 站\n[BBOX-6] 姓名：\n[BBOX-7] 性别：女\n[BBOX-8] 年龄：72岁\n[BBOX-9] 出生地：贵州省贵阳市\n[BBOX-10] 职业：退休人员\n[BBOX-11] 民族：汉族\n[BBOX-12] 婚姻：已婚\n[BBOX-13] 联系地址：中国贵州省贵阳市\n[BBOX-14] 入院时间：2025-10-30 14:34\n[BBOX-15] 病史陈述者：本人\n[BBOX-16] 主诉：咳嗽、咳痰5年，加重1周\n[BBOX-17] 现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，\n[BBOX-18] 不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管\n[BBOX-19] 哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感\n[BBOX-20] 和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治\n[BBOX-21] 就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二\n[BBOX-22] 便如常，近1年体重减少4kg。\n[BBOX-23] 既往史：\n[BBOX-24] 患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染\n[BBOX-25] 病；食物、药物过敏无；无外伤史：无手术史：无输血史：无中毒史：无长期用药史：无可能成瘾药物。疫\n[BBOX-26] 苗接种史不详\n[BBOX-27] 个人史：\n[BBOX-28] 出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长\n[BBOX-29] 地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物\n[BBOX-30] 质接触史。\n[BBOX-31] 婚育史：\n[BBOX-32] 已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。\n[BBOX-33] 月经史：\n[BBOX-34] 初潮年龄17岁\n[BBOX-35] 经期3-4天\n[BBOX-36] 绝经年龄53岁 月经及白带情况：正常\n[BBOX-37] 月经周期30天\n[BBOX-38] 家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否\n[BBOX-39] 认二系三代有遗传病史。患者否认有遗传倾向的疾病。\n[BBOX-40] 体格检查\n[BBOX-41] 生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60\n[BBOX-42] 体格检查\n[BBOX-43] 生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体\n[BBOX-44] 重：44kg，腰围：cm，BMI：18.8 kg/m²\n[BBOX-45] 一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常\n[BBOX-46] 表情：正常体位：自主体位步态：平稳配合检查：配合\n[BBOX-47] 皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无\n[BBOX-48] 皮疹：无紫癜：无\n[BBOX-49] 1/3\n[BBOX-50] 贵州醫科大學附属醫院\n[BBOX-51] THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n[BBOX-52] 入院记录\n[BBOX-53] 姓名：\n[BBOX-54] 床号：23-03床\n[BBOX-55] 病历号\n[BBOX-56] 科室：呼吸与危重医学科医生\n[BBOX-57] 站\n[BBOX-58] 水肿：无脱水现象：无松紧度：适中\n[BBOX-59] 温度：适中出汗：无显性出汗瘢痕：无感染：无\n[BBOX-60] 头颅：大小：正常畸形：无包块：无\n[BBOX-61] 凹陷：无压痛：无\n[BBOX-62] 眼：眼睑：无水肿结膜：无充血巩膜：无黄染\n[BBOX-63] 眼球四个象限运动：左眼：正常右眼：正常\n[BBOX-64] 眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆\n[BBOX-65] 对光反射：左眼：灵敏右眼：灵敏\n[BBOX-66] 鼻：外形：正常其他异常：无鼻旁窦压痛：无\n[BBOX-67] 口：唇：无紫绀粘膜：无充血腮腺导管开口：正常\n[BBOX-68] 舌：伸舌居中牙龈：无肿胀龋齿：无\n[BBOX-69] 咽喉：扁桃体：正常咽：无充血声音：正常\n[BBOX-70] 淋巴：淋巴结：全身浅表淋巴结未及肿大\n[BBOX-71] 颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张\n[BBOX-72] 气管：居中颈静脉回流征：无\n[BBOX-73] 甲状腺：无肿大\n[BBOX-74] 眼球四个象限运动：左眼：正常 右眼：正常\n[BBOX-75] 眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆\n[BBOX-76] 对光反射：左眼：灵敏 右眼：灵敏\n[BBOX-77] 鼻：外形：正常 其他异常：无 鼻旁窦压痛：无\n[BBOX-78] 口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常\n[BBOX-79] 舌：伸舌居中 牙龈：无肿胀 龋齿：无\n[BBOX-80] 咽 喉：扁桃体：正常 咽：无充血 声音：正常\n[BBOX-81] 淋巴 巴：淋巴结：全身浅表淋巴结未及肿大\n[BBOX-82] 颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张\n[BBOX-83] 气管：居中 颈静脉回流征：无\n[BBOX-84] 甲状腺：无肿大\n[BBOX-85] 胸部 部：胸廓：无畸形 乳房：\n[BBOX-86] 肺 部：视诊：呼吸运动\n[BBOX-87] 触诊：\n[BBOX-88] 叩诊：\n[BBOX-89] 听诊：\n[BBOX-90] 语音传导\n[BBOX-91] 心 脏：视诊：\n[BBOX-92] 触诊：心尖搏动\n[BBOX-93] 叩诊：\n[BBOX-94] 心界\n[BBOX-95] 右(cm)\n[BBOX-96] 肋间\n[BBOX-97] 左(cm)\n[BBOX-98] 2\n[BBOX-99] 2\n[BBOX-100] 2\n[BBOX-101] 3\n[BBOX-102] (左锁骨中线距胸骨线7.5cm)\n[BBOX-103] 听诊：心率：92次/分 心律：齐 心音：未闻及异常心\n[BBOX-104] 额外心音：无 杂音：无 心包摩擦感：\n[BBOX-105] 周围血管：异常血管征：无\n[BBOX-106] 腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出\n[BBOX-107] 其他异常：无\n[BBOX-108] 触诊：腹壁：柔软 压痛：无\n[BBOX-109] 2/3\n[BBOX-110] 站\n[BBOX-111] 反跳痛：无\n[BBOX-112] 液波振颤：无 振水声：无\n[BBOX-113] 腹部包块：无\n[BBOX-114] 肝：肋下未及\n[BBOX-115] 胆囊：未触及 Murphy征：阴性\n[BBOX-116] 脾：未触及\n[BBOX-117] 叩诊：肝浊音界：正常 移动性浊音：无\n[BBOX-118] 肾区叩痛：无\n[BBOX-119] 听诊：肠鸣音：正常 肠鸣音频率：4次/分\n[BBOX-120] 气过水音：无 血管杂音：无\n[BBOX-121] 肛门直肠：未检\n[BBOX-122] 生殖器：未检\n[BBOX-123] 脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限\n[BBOX-124] 压痛，叩痛：无\n[BBOX-125] 杵状指趾：无\n[BBOX-126] 神经系统：腹壁反射：正常 肢体瘫痪：无\n[BBOX-127] 肌张力：正常 肌力：V级\n[BBOX-128] 肱二头肌反射：正常 Hoffman征：阴性\n[BBOX-129] 膝腱反射：正常 Kernig征：阴性\n[BBOX-130] 跟腱反射：正常 Babinski征：阴性\n[BBOX-131] 其他：无\n[BBOX-132] 补充及专科情况\n[BBOX-133] 双肺呼吸音清，未闻及干湿性啰音。\n[BBOX-134] 辅助检查：暂无\n[BBOX-135] VTE评估：\n[BBOX-136] Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：\n[BBOX-137] 入院诊断：1.支气管哮喘急性发作期\n[BBOX-138] 医师签名：\n[BBOX-139] 日期：2025-10-30 16:38\n[BBOX-140] 出院记录\n[BBOX-141] 姓名：\n[BBOX-142] 床号：23-03床\n[BBOX-143] 病历号：0\n[BBOX-144] 科室：呼吸与危重医学科医生站\n[BBOX-145] 姓名：\n[BBOX-146] 性别：女\n[BBOX-147] 年龄：72岁\n[BBOX-148] 民族：汉族\n[BBOX-149] 病历号：00\n[BBOX-150] 科室：呼吸与危重医学科医生站\n[BBOX-151] 入院日期：2025-10-30 14:34\n[BBOX-152] 住院天数：8\n[BBOX-153] 出院日期：2025-11-07 11:44\n[BBOX-154] 籍贯：贵州省贵阳市\n[BBOX-155] 职业：退休人员\n[BBOX-156] 单位：贵阳供电局\n[BBOX-157] 住址：中国贵州省贵阳\n[BBOX-158] 入院情况：\n[BBOX-159] 李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无\n[BBOX-160] 明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯\n[BBOX-161] 血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治\n[BBOX-162] 疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1\n[BBOX-163] 周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门\n[BBOX-164] 诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体\n[BBOX-165] 重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病\n[BBOX-166] 史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无\n[BBOX-167] 中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学\n[BBOX-168] 历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗\n[BBOX-169] 史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已\n[BBOX-170] 故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患\n[BBOX-171] 者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，\n[BBOX-172] 血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。\n[BBOX-173] 心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检\n[BBOX-174] 查：暂无\n[BBOX-175] 入院诊断：1.支气管哮喘急性发作期\n[BBOX-176] 诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床\n[BBOX-177] 检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1\n[BBOX-178] 2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝\n[BBOX-179] 功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中\n[BBOX-180] 心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中\n[BBOX-181] 心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml\n[BBOX-182] 肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移\n[BBOX-183] 酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD)\n[BBOX-184] 0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-3\n[BBOX-185] 0 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 13:11 胸部CT平扫：1、考\n[BBOX-186] 虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧\n[BBOX-187] 1/3\n[BBOX-188] 贵州醫科大學附屬醫院\n[BBOX-189] THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n[BBOX-190] 出院记录\n[BBOX-191] 姓名：\n[BBOX-192] 床号：23-03床\n[BBOX-193] 病历号：\n[BBOX-194] 科室：呼吸与危重医学科医生站\n[BBOX-195] 胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管\n[BBOX-196] 扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊\n[BBOX-197] 复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走\n[BBOX-198] 行欠佳。 7、肝内囊性灶，建议超声随诊复查。2025-10-31 14:35 肺通气功能测定及支气管舒张试验：1.\n[BBOX-199] 中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+) 2025-10-31 12:33。传染病筛查\n[BBOX-200] 三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临\n[BBOX-201] 床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31\n[BBOX-202] 14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴\n[BBOX-203] 定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支\n[BBOX-204] 气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症\n[BBOX-205] 治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。\n[BBOX-206] 出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小\n[BBOX-207] 结节；5.肝囊肿。\n[BBOX-208] 出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查\n[BBOX-209] 体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊\n[BBOX-210] 区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。\n[BBOX-211] VTE评估：\n[BBOX-212] 床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31\n[BBOX-213] 14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴\n[BBOX-214] 定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支\n[BBOX-215] 气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症\n[BBOX-216] 治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。\n[BBOX-217] 出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小\n[BBOX-218] 结节；5.肝囊肿。\n[BBOX-219] 出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查\n[BBOX-220] 体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊\n[BBOX-221] 区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。\n[BBOX-222] VTE评估：\n[BBOX-223] Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：\n[BBOX-224] 出院医嘱：\n[BBOX-225] 1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治\n[BBOX-226] 疗，定期复查肺功能，呼吸科门诊随诊；\n[BBOX-227] 2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。\n[BBOX-228] 3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。\n[BBOX-229] 4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。\n[BBOX-230] 手术名称：\n[BBOX-231] 无\n[BBOX-232] 出院结果：好转\n[BBOX-233] 医生签名：\n[BBOX-234] 日期：2025-11-07 11:44\n[BBOX-235] 温馨提示\n[BBOX-236] 尊敬的患者，出院后如您需复印住院资料，请关注以下温馨小提示：\n[BBOX-237] 一、操作流程\n[BBOX-238] 【方法一】\n[BBOX-239] 1.请先打开微信“扫一扫”，扫描二维码，根据提示进行操作完成网上预约申请并回家等待。\n[BBOX-240] 2/3\n[BBOX-241] 贵州医科大学附属医院\n[BBOX-242] THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n[BBOX-243] 肺功能通气阻力检查报告\n[BBOX-244] 姓名：\n[BBOX-245] 性别：女\n[BBOX-246] 身高：151 cm\n[BBOX-247] 病历号：\n[BBOX-248] 年龄：72 Years\n[BBOX-249] 体重：46 kg\n[BBOX-250] Flow [L/s]\n[BBOX-251] F/V ex\n[BBOX-252] 10\n[BBOX-253] 5\n[BBOX-254] 0\n[BBOX-255] 2\n[BBOX-256] 4\n[BBOX-257] 6\n[BBOX-258] F/V in\n[BBOX-259] 8\n[BBOX-260] Vol [L]\n[BBOX-261] 6\n[BBOX-262] 4\n[BBOX-263] 1\n[BBOX-264] Vol%Vcmax\n[BBOX-265] 100\n[BBOX-266] Vcmax\n[BBOX-267] 20\n[BBOX-268] 0\n[BBOX-269] Time [s]\n[BBOX-270] 0\n[BBOX-271] 1\n[BBOX-272] 2\n[BBOX-273] 3\n[BBOX-274] 4\n[BBOX-275] 5\n[BBOX-276] 6\n[BBOX-277] 2.0\n[BBOX-278] R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]\n[BBOX-279] 1.5\n[BBOX-280] 1.0\n[BBOX-281] 0.5\n[BBOX-282] 0.0\n[BBOX-283] 0.4\n[BBOX-284] 0.2\n[BBOX-285] 0.2\n[BBOX-286] 0.4\n[BBOX-287] F [Hz]\n[BBOX-288] 5\n[BBOX-289] 10\n[BBOX-290] 15\n[BBOX-291] 20\n[BBOX-292] 25\n[BBOX-293] 30\n[BBOX-294] 35\n[BBOX-295] 日期\n[BBOX-296] 时间\n[BBOX-297] 预计值\n[BBOX-298] 实测值\n[BBOX-299] 实/预\n[BBOX-300] 25/10/31\n[BBOX-301] 14:29:33\n[BBOX-302] MV\n[BBOX-303] [L/min]\n[BBOX-304] 6.57\n[BBOX-305] 11.52\n[BBOX-306] 175.3\n[BBOX-307] VT\n[BBOX-308] [L]\n[BBOX-309] 0.33\n[BBOX-310] 0.79\n[BBOX-311] 239.6\n[BBOX-312] BF\n[BBOX-313] [1/min]\n[BBOX-314] 20.00\n[BBOX-315] 14.63\n[BBOX-316] 73.1\n[BBOX-317] VC MAX\n[BBOX-318] [L]\n[BBOX-319] 2.03\n[BBOX-320] 1.48\n[BBOX-321] 73.0\n[BBOX-322] ERV\n[BBOX-323] [L]\n[BBOX-324] 0.57\n[BBOX-325] 0.14\n[BBOX-326] 25.5\n[BBOX-327] IC\n[BBOX-328] [L]\n[BBOX-329] 1.46\n[BBOX-330] 1.34\n[BBOX-331] 91.6\n[BBOX-332] FVC\n[BBOX-333] [L]\n[BBOX-334] 1.93\n[BBOX-335] 1.44\n[BBOX-336] 74.8\n[BBOX-337] FEV 1\n[BBOX-338] [L]\n[BBOX-339] 1.56\n[BBOX-340] 0.91\n[BBOX-341] 58.4\n[BBOX-342] FEV 1 % FVC\n[BBOX-343] [%]\n[BBOX-344] 63.38\n[BBOX-345] FEV 1 % VC MAX\n[BBOX-346] [%]\n[BBOX-347] 75.42\n[BBOX-348] 61.67\n[BBOX-349] 81.8\n[BBOX-350] PEF\n[BBOX-351] [L/s]\n[BBOX-352] 5.04\n[BBOX-353] 2.51\n[BBOX-354] 49.8\n[BBOX-355] MEF 75\n[BBOX-356] [L/s]\n[BBOX-357] 4.66\n[BBOX-358] 1.54\n[BBOX-359] 33.1\n[BBOX-360] MEF 50\n[BBOX-361] [L/s]\n[BBOX-362] 3.06\n[BBOX-363] 0.56\n[BBOX-364] 18.2\n[BBOX-365] MEF 25\n[BBOX-366] [L/s]\n[BBOX-367] 0.90\n[BBOX-368] 0.22\n[BBOX-369] 24.6\n[BBOX-370] MEF 75/25\n[BBOX-371] [L/s]\n[BBOX-372] 2.36\n[BBOX-373] 0.50\n[BBOX-374] 21.1\n[BBOX-375] FET\n[BBOX-376] [s]\n[BBOX-377] 4.91\n[BBOX-378] LFV\n[BBOX-379] [L/min]\n[BBOX-380] 73.10\n[BBOX-381] Z at 5 Hz\n[BBOX-382] [kPa/(L/s)]\n[BBOX-383] 0.43\n[BBOX-384] 0.58\n[BBOX-385] 135.7\n[BBOX-386] Resonant frequency\n[BBOX-387] [1/s]\n[BBOX-388] 30.00\n[BBOX-389] R at 5 Hz\n[BBOX-390] [kPa/(L/s)]\n[BBOX-391] 0.41\n[BBOX-392] 0.57\n[BBOX-393] 137.2\n[BBOX-394] R nt 20 Hz\n[BBOX-395] [kPa/(L/s)]\n[BBOX-396] 0.35\n[BBOX-397] 0.34\n[BBOX-398] 95.3\n[BBOX-399] X at 5 Hz\n[BBOX-400] [kPa/(L/s)]\n[BBOX-401] -0.11\n[BBOX-402] -0.12\n[BBOX-403] 112.5\n[BBOX-404] Rcentral\n[BBOX-405] [kPa/(L/s)]\n[BBOX-406] 0.12\n[BBOX-407] Peripheral\n[BBOX-408] [kPa/(L/s)]\n[BBOX-409] 0.40\n[BBOX-410] 结论：\n[BBOX-411] 1.中重度混合性肺通气功能障碍\n[BBOX-412] 2.（阻力增加\n[BBOX-413] 审核者专用章\n[BBOX-414] 检查者：王美锦\n[BBOX-415] 贵州医科大学附属医院\n[BBOX-416] THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n[BBOX-417] 对比试验\n[BBOX-418] 姓名：\n[BBOX-419] 性别：女\n[BBOX-420] 身高：151 cm\n[BBOX-421] 病历号：\n[BBOX-422] 年龄：72 Years\n[BBOX-423] 体重：46 kg\n[BBOX-424] Flow [L/s]\n[BBOX-425] F/V ex\n[BBOX-426] 10\n[BBOX-427] 5\n[BBOX-428] 0\n[BBOX-429] 2\n[BBOX-430] 3\n[BBOX-431] 4\n[BBOX-432] 5\n[BBOX-433] 6\n[BBOX-434] 7\n[BBOX-435] F/V in\n[BBOX-436] 6\n[BBOX-437] Vol [L]\n[BBOX-438] 4\n[BBOX-439] TLC\n[BBOX-440] ER,pleth2\n[BBOX-441] RV\n[BBOX-442] Time [min]\n[BBOX-443] Pred Act 0.0\n[BBOX-444] 0.2\n[BBOX-445] 0.4\n[BBOX-446] 0.6\n[BBOX-447] 0.8\n[BBOX-448] 1.0\n[BBOX-449] 日期\n[BBOX-450] 时间\n[BBOX-451] 预计值\n[BBOX-452] 前次\n[BBOX-453] 前/预\n[BBOX-454] 后次\n[BBOX-455] 后/预\n[BBOX-456] 改善率\n[BBOX-457] 25/10/31\n[BBOX-458] 14:29:33\n[BBOX-459] 25/10/31\n[BBOX-460] 14:53:10\n[BBOX-461] VT\n[BBOX-462] [L]\n[BBOX-463] 0.33\n[BBOX-464] 0.79\n[BBOX-465] 239.6\n[BBOX-466] BF\n[BBOX-467] [1/min]\n[BBOX-468] 20.00\n[BBOX-469] 14.63\n[BBOX-470] 73.1\n[BBOX-471] MV\n[BBOX-472] [L/min]\n[BBOX-473] 6.57\n[BBOX-474] 11.52\n[BBOX-475] 175.3\n[BBOX-476] VC MAX\n[BBOX-477] [L]\n[BBOX-478] 2.03\n[BBOX-479] 1.48\n[BBOX-480] 73.0\n[BBOX-481] 1.66\n[BBOX-482] 81.9\n[BBOX-483] 12.2\n[BBOX-484] ERV\n[BBOX-485] [L]\n[BBOX-486] 0.57\n[BBOX-487] 0.14\n[BBOX-488] 25.5\n[BBOX-489] IC\n[BBOX-490] [L]\n[BBOX-491] 1.46\n[BBOX-492] 1.34\n[BBOX-493] 91.6\n[BBOX-494] FVC\n[BBOX-495] [L]\n[BBOX-496] 1.93\n[BBOX-497] 1.44\n[BBOX-498] 74.8\n[BBOX-499] 1.66\n[BBOX-500] 86.2\n[BBOX-501] 15.3\n[BBOX-502] FEV 1\n[BBOX-503] [L]\n[BBOX-504] 1.56\n[BBOX-505] 0.91\n[BBOX-506] 58.4\n[BBOX-507] 1.08\n[BBOX-508] 68.8\n[BBOX-509] 17.8\n[BBOX-510] FEV 1 % FVC\n[BBOX-511] [%]\n[BBOX-512] 63.38\n[BBOX-513] 64.76\n[BBOX-514] 2.2\n[BBOX-515] FEV 1 % VC MAX\n[BBOX-516] [%]\n[BBOX-517] 75.42\n[BBOX-518] 61.67\n[BBOX-519] 81.8\n[BBOX-520] 64.76\n[BBOX-521] 85.9\n[BBOX-522] 5.0\n[BBOX-523] PEF\n[BBOX-524] [L/s]\n[BBOX-525] 5.04\n[BBOX-526] 2.51\n[BBOX-527] 49.8\n[BBOX-528] 3.35\n[BBOX-529] 66.5\n[BBOX-530] 33.6\n[BBOX-531] MEF 75\n[BBOX-532] [L/s]\n[BBOX-533] 4.66\n[BBOX-534] 1.54\n[BBOX-535] 33.1\n[BBOX-536] 1.72\n[BBOX-537] 36.8\n[BBOX-538] 11.3\n[BBOX-539] MEF 50\n[BBOX-540] [L/s]\n[BBOX-541] 3.06\n[BBOX-542] 0.56\n[BBOX-543] 18.2\n[BBOX-544] 0.83\n[BBOX-545] 27.1\n[BBOX-546] 49.1\n[BBOX-547] MEF 25\n[BBOX-548] [L/s]\n[BBOX-549] 0.90\n[BBOX-550] 0.22\n[BBOX-551] 24.6\n[BBOX-552] 0.36\n[BBOX-553] 39.8\n[BBOX-554] 62.1\n[BBOX-555] MMEF 75/25\n[BBOX-556] [L/s]\n[BBOX-557] 2.36\n[BBOX-558] 0.50\n[BBOX-559] 21.1\n[BBOX-560] 0.47\n[BBOX-561] 20.0\n[BBOX-562] -4.9\n[BBOX-563] FET\n[BBOX-564] [s]\n[BBOX-565] 4.91\n[BBOX-566] 4.88\n[BBOX-567] -0.6\n[BBOX-568] V backextrapol. % FVC\n[BBOX-569] [%]\n[BBOX-570] 3.85\n[BBOX-571] 4.39\n[BBOX-572] 13.9\n[BBOX-573] MVV\n[BBOX-574] [L/min]\n[BBOX-575] 73.10\n[BBOX-576] 结论：\n[BBOX-577] 1.中重度混合性肺通气功能障碍\n[BBOX-578] 2.气道阻力增加\n[BBOX-579] 3.支气管舒张试验阳性 (+)\n[BBOX-580] 吸入沙丁胺醇400μg\n[BBOX-581] FVC上升15.3%，增加220ml；\n[BBOX-582] 审核者：\n[BBOX-583] 检查者：\n[BBOX-584] 贵州医科大学附属医院检查报告\n[BBOX-585] 专用电子章\n[BBOX-586] 亦康互联网医院\n[BBOX-587] 普通\n[BBOX-588] 处方\n[BBOX-589] 已使用\n[BBOX-590] 已使用\n[BBOX-591] 已使用\n[BBOX-592] 联\n[BBOX-593] 处方笺\n[BBOX-594] 已使用\n[BBOX-595] NO.:\n[BBOX-596] 2025-12-05\n[BBOX-597] 已使用\n[BBOX-598] 姓名：\n[BBOX-599] 性别：女处方专用章\n[BBOX-600] 年龄：72岁\n[BBOX-601] 已使用\n[BBOX-602] 费别：自费\n[BBOX-603] 科别：内科\n[BBOX-604] 已使用\n[BBOX-605] 临床诊断：支气管哮喘\n[BBOX-606] 已使用\n[BBOX-607] Rp：\n[BBOX-608] 已使用\n[BBOX-609] 沙美特罗替卡松吸入粉雾剂\n[BBOX-610] 已使用\n[BBOX-611] 50μg:250μg*60泡\n[BBOX-612] x 3盒\n[BBOX-613] 用法用量：\n[BBOX-614] 口腔吸入,一日两次,一次1.0揿;\n[BBOX-615] 已使用\n[BBOX-616] 补充说明：处方超7日为病情需要\n[BBOX-617] 已使用\n[BBOX-618] 医师：邢伟\n[BBOX-619] 审核：张艳梅\n[BBOX-620] 处方金额：\n[BBOX-621] 药房审核：\n[BBOX-622] 药房调配：\n[BBOX-623] 药房核对：\n[BBOX-624] 药房发药：\n[BBOX-625] 注：处方自开具日起3日内有效。"
  }
]
2026-08-10 11:23:37,317 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:37,348 INFO     29 [SmartSplitter] SmartSplitter done: 4 chunks from 4 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1}
2026-08-10 11:23:37,362 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 11:23:37,362 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks": "4 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1}"}
2026-08-10 11:23:37,362 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 11:23:37,363 INFO     29 [ChunkRouter] Routed 4 chunks into 4 groups: {'chunks_Admission': 1, 'chunks_Discharge': 1, 'chunks_Examination': 1, 'chunks_Prescription': 1}
2026-08-10 11:23:37,422 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 11:23:37,423 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | ChunkRouter:Router | outputs={"html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks": "4 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:23:37,423 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 11:23:37,436 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:37,436 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:23:39,220 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:39,228 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 11:23:39,229 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:23:39,229 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 11:23:39,238 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:39,238 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:23:39,662 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:39,676 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 11:23:39,677 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:23:39,677 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 11:23:39,687 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:39,688 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:23:40,203 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:40,211 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 11:23:40,211 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:23:40,211 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 11:23:40,218 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:40,219 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:23:40,898 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:40,905 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 11:23:40,905 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:23:40,905 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 11:23:40,911 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:23:40,911 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:23:40,912 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:23:40,912 INFO     29 [qwen-vl-text] positions(40): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:23:40,912 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [40]
2026-08-10 11:23:41,162 INFO     29 [qwen-vl-text] page=9, rect=612x733, img=(1700x2036), dpi=200
2026-08-10 11:23:41,165 INFO     29 [qwen-vl-text] LLM extraction start, text_len=263
2026-08-10 11:23:41,165 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:41,166 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 586, \"bbox_end\": 625, \"encounter_dates\": [\"2025-12-05\"], \"department\": \"内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "亦康互联网医院\n普通\n处方\n已使用\n已使用\n已使用\n联\n处方笺\n已使用\nNO.:\n2025-12-05\n已使用\n姓名：\n性别：女处方专用章\n年龄：72岁\n已使用\n费别：自费\n科别：内科\n已使用\n临床诊断：支气管哮喘\n已使用\nRp：\n已使用\n沙美特罗替卡松吸入粉雾剂\n已使用\n50μg:250μg*60泡\nx 3盒\n用法用量：\n口腔吸入,一日两次,一次1.0揿;\n已使用\n补充说明：处方超7日为病情需要\n已使用\n医师：邢伟\n审核：张艳梅\n处方金额：\n药房审核：\n药房调配：\n药房核对：\n药房发药：\n注：处方自开具日起3日内有效。",
    "role": "user"
  }
]
2026-08-10 11:23:43,069 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:23:43,070 INFO     29 [qwen-vl-text] LLM output (len=436):
{
  "encounter_date": "2025-12-05",
  "prescription_type": "门诊处方",
  "prescriber": "邢伟",
  "department": "内科",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "50μg:250μg",
      "frequency": "bid",
      "route": "口腔吸入",
      "duration_days": null,
      "quantity": "3盒",
      "notes": "一次1.0揿; 处方超7日为病情需要"
    }
  ]
}
2026-08-10 11:23:43,070 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-05]
2026-08-10 11:23:43,071 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=882388, prompt_len=996
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["亦康互联网医院", "普通", "处方", "已使用", "已使用", "已使用", "联", "处方笺", "已使用", "NO.:", "2025-12-05", "已使用", "姓名：", "性别：女处方专用章", "年龄：72岁", "已使用", "费别：自费", "科别：内科", "已使用", "临床诊断：支气管哮喘", "已使用", "Rp：", "已使用", "沙美特罗替卡松吸入粉雾剂", "已使用", "50μg:250μg*60泡", "x 3盒", "用法用量：", "口腔吸入,一日两次,一次1.0揿;", "已使用", "补充说明：处方超7日为病情需要", "已使用", "医师：邢伟", "审核：张艳梅", "处方金额：", "药房审核：", "药房调配：", "药房核对：", "药房发药：", "注：处方自开具日起3日内有效。"]

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
2026-08-10 11:24:04,148 INFO     29 [qwen-vl-text] coord API raw response (len=3996):
[
	{"text": "亦康互联网医院", "bbox": [428, 29, 716, 66]},
	{"text": "普通", "bbox": [896, 33, 936, 50], "bbox": [896, 33, 936, 50]},
	{"text": "处方", "bbox": [896, 53, 936, 70], "bbox": [896, 53, 936, 70]},
	{"text": "已使用", "bbox": [20, 72, 90, 100], "bbox": [20, 72, 90, 100]},
	{"text": "已使用", "bbox": [361, 72, 427, 106], "bbox": [361, 72, 427, 106]},
	{"text": "联", "bbox": [551, 78, 576, 97], "bbox": [551, 78, 576, 97]},
	{"text": "处方笺", "bbox": [485, 95, 611, 129], "bbox": [485, 95, 611, 129]},
	{"text": "已使用", "bbox": [725, 95, 791, 127], "bbox": [725, 95, 791, 127]},
	{"text": "NO.:", "bbox": [100, 140, 170, 161], "bbox": [100, 140, 170, 161]},
	{"text": "2025-12-05", "bbox": [755, 136, 904, 157], "bbox": [755, 136, 904, 157]},
	{"text": "已使用", "bbox": [14, 189, 83, 220], "bbox": [14, 189, 83, 220]},
	{"text": "姓名：", "bbox": [98, 201, 200, 226], "bbox": [98, 201, 200, 226]},
	{"text": "性别：女处方专用章", "bbox": [411, 200, 623, 226], "bbox": [411, 200, 623, 226]},
	{"text": "年龄：72岁", "bbox": [695, 195, 836, 220], "bbox": [695, 195, 836, 220]},
	{"text": "已使用", "bbox": [371, 218, 419, 245], "bbox": [371, 218, 419, 245]},
	{"text": "费别：自费", "bbox": [97, 258, 244, 284], "bbox": [97, 258, 244, 284]},
	{"text": "科别：内科", "bbox": [411, 260, 557, 286], "bbox": [411, 260, 557, 286]},
	{"text": "已使用", "bbox": [540, 270, 605, 302], "bbox": [540, 270, 605, 302]},
	{"text": "临床诊断：支气管哮喘", "bbox": [97, 318, 376, 344], "bbox": [97, 318, 376, 344]},
	{"text": "已使用", "bbox": [909, 267, 977, 300], "bbox": [909, 267, 977, 300]},
	{"text": "Rp：", "bbox": [85, 389, 145, 418], "bbox": [85, 389, 145, 418]},
	{"text": "已使用", "bbox": [194, 385, 262, 418], "bbox": [194, 385, 262, 418]},
	{"text": "已使用", "bbox": [538, 383, 605, 418], "bbox": [538, 383, 605, 418]},
	{"text": "已使用", "bbox": [908, 382, 976, 416], "bbox": [908, 382, 976, 416]},
	{"text": "沙美特罗替卡松吸入粉雾剂", "bbox": [105, 442, 434, 468], "bbox": [105, 442, 434, 468]},
	{"text": "已使用", "bbox": [738, 442, 805, 475], "bbox": [738, 442, 805, 475]},
	{"text": "50μg:250μg*60泡", "bbox": [107, 482, 332, 508], "bbox": [107, 482, 332, 508]},
	{"text": "x 3盒", "bbox": [570, 480, 636, 503], "bbox": [570, 480, 636, 503]},
	{"text": "用法用量：", "bbox": [107, 527, 233, 552], "bbox": [107, 527, 233, 552]},
	{"text": "口腔吸入,一日两次,一次1.0揿;", "bbox": [278, 525, 623, 551], "bbox": [278, 525, 623, 551]},
	{"text": "已使用", "bbox": [907, 511, 975, 545], "bbox": [907, 511, 975, 545]},
	{"text": "补充说明：处方超7日为病情需要", "bbox": [82, 608, 512, 635], "bbox": [82, 608, 512, 635]},
	{"text": "已使用", "bbox": [738, 560, 805, 593], "bbox": [738, 560, 805, 593]},
	{"text": "已使用", "bbox": [192, 631, 260, 664], "bbox": [192, 631, 260, 664]},
	{"text": "已使用", "bbox": [549, 628, 616, 661], "bbox": [549, 628, 616, 661]},
	{"text": "已使用", "bbox": [907, 637, 975, 671], "bbox": [907, 637, 975, 671]},
	{"text": "已使用", "bbox": [0, 678, 69, 710], "bbox": [0, 678, 69, 710]},
	{"text": "已使用", "bbox": [378, 685, 446, 718], "bbox": [378, 685, 446, 718]},
	{"text": "已使用", "bbox": [737, 685, 805, 718], "bbox": [737, 685, 805, 718]},
	{"text": "已使用", "bbox": [184, 740, 255, 773], "bbox": [184, 740, 255, 773]},
	{"text": "已使用", "bbox": [555, 738, 623, 772], "bbox": [555, 738, 623, 772]},
	{"text": "已使用", "bbox": [907, 738, 975, 772], "bbox": [907, 738, 975, 772]},
	{"text": "已使用", "bbox": [0, 800, 58, 831], "bbox": [0, 800, 58, 831]},
	{"text": "医师：邢伟", "bbox": [67, 804, 250, 847], "bbox": [67, 804, 250, 847]},
	{"text": "审核：张艳梅", "bbox": [296, 807, 508, 836], "bbox": [296, 807, 508, 836]},
	{"text": "处方金额：", "bbox": [522, 805, 648, 830], "bbox": [522, 805, 648, 830]},
	{"text": "药房审核：", "bbox": [64, 865, 196, 890], "bbox": [64, 865, 196, 890]},
	{"text": "药房调配：", "bbox": [294, 866, 420, 891], "bbox": [294, 866, 420, 891]},
	{"text": "药房核对：", "bbox": [522, 865, 648, 890], "bbox": [522, 865, 648, 890]},
	{"text": "药房发药：", "bbox": [759, 866, 885, 891], "bbox": [759, 866, 885, 891]},
	{"text": "注：处方自开具日起3日内有效。", "bbox": [63, 957, 370, 978], "bbox": [63, 957, 370, 978]}
]
2026-08-10 11:24:04,149 INFO     29 [qwen-vl-text] coord API: raw_items=51, valid_items=51, elapsed=21.1s
2026-08-10 11:24:04,149 INFO     29 [qwen-vl-text] coord item[0]: text=亦康互联网医院, bbox=[428, 29, 716, 66]
2026-08-10 11:24:04,149 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[896, 33, 936, 50]
2026-08-10 11:24:04,149 INFO     29 [qwen-vl-text] coord item[2]: text=处方, bbox=[896, 53, 936, 70]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[3]: text=已使用, bbox=[20, 72, 90, 100]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[4]: text=已使用, bbox=[361, 72, 427, 106]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[5]: text=联, bbox=[551, 78, 576, 97]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[6]: text=处方笺, bbox=[485, 95, 611, 129]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[7]: text=已使用, bbox=[725, 95, 791, 127]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[8]: text=NO.:, bbox=[100, 140, 170, 161]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[9]: text=2025-12-05, bbox=[755, 136, 904, 157]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[10]: text=已使用, bbox=[14, 189, 83, 220]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[11]: text=姓名：, bbox=[98, 201, 200, 226]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[12]: text=性别：女处方专用章, bbox=[411, 200, 623, 226]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[13]: text=年龄：72岁, bbox=[695, 195, 836, 220]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[14]: text=已使用, bbox=[371, 218, 419, 245]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[15]: text=费别：自费, bbox=[97, 258, 244, 284]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[16]: text=科别：内科, bbox=[411, 260, 557, 286]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[17]: text=已使用, bbox=[540, 270, 605, 302]
2026-08-10 11:24:04,150 INFO     29 [qwen-vl-text] coord item[18]: text=临床诊断：支气管哮喘, bbox=[97, 318, 376, 344]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[19]: text=已使用, bbox=[909, 267, 977, 300]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[20]: text=Rp：, bbox=[85, 389, 145, 418]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[21]: text=已使用, bbox=[194, 385, 262, 418]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[22]: text=已使用, bbox=[538, 383, 605, 418]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[23]: text=已使用, bbox=[908, 382, 976, 416]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[24]: text=沙美特罗替卡松吸入粉雾剂, bbox=[105, 442, 434, 468]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[25]: text=已使用, bbox=[738, 442, 805, 475]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[26]: text=50μg:250μg*60泡, bbox=[107, 482, 332, 508]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[27]: text=x 3盒, bbox=[570, 480, 636, 503]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[28]: text=用法用量：, bbox=[107, 527, 233, 552]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[29]: text=口腔吸入,一日两次,一次1.0揿;, bbox=[278, 525, 623, 551]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[30]: text=已使用, bbox=[907, 511, 975, 545]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[31]: text=补充说明：处方超7日为病情需要, bbox=[82, 608, 512, 635]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[32]: text=已使用, bbox=[738, 560, 805, 593]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[33]: text=已使用, bbox=[192, 631, 260, 664]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[34]: text=已使用, bbox=[549, 628, 616, 661]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[35]: text=已使用, bbox=[907, 637, 975, 671]
2026-08-10 11:24:04,151 INFO     29 [qwen-vl-text] coord item[36]: text=已使用, bbox=[0, 678, 69, 710]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[37]: text=已使用, bbox=[378, 685, 446, 718]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[38]: text=已使用, bbox=[737, 685, 805, 718]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[39]: text=已使用, bbox=[184, 740, 255, 773]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[40]: text=已使用, bbox=[555, 738, 623, 772]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[41]: text=已使用, bbox=[907, 738, 975, 772]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[42]: text=已使用, bbox=[0, 800, 58, 831]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[43]: text=医师：邢伟, bbox=[67, 804, 250, 847]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[44]: text=审核：张艳梅, bbox=[296, 807, 508, 836]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[45]: text=处方金额：, bbox=[522, 805, 648, 830]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[46]: text=药房审核：, bbox=[64, 865, 196, 890]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[47]: text=药房调配：, bbox=[294, 866, 420, 891]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[48]: text=药房核对：, bbox=[522, 865, 648, 890]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[49]: text=药房发药：, bbox=[759, 866, 885, 891]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] coord item[50]: text=注：处方自开具日起3日内有效。, bbox=[63, 957, 370, 978]
2026-08-10 11:24:04,152 INFO     29 [qwen-vl-text] page=9 — 40/40 coords, api_time=21.1s
2026-08-10 11:24:04,154 INFO     29 [qwen-vl-text] new_positions (40):
[[9, 261.936, 438.192, 21.254792785644533, 48.37297668457031], [9, 548.352, 572.832, 24.186488342285156, 36.64619445800781], [9, 548.352, 572.832, 38.844966125488284, 51.30467224121094], [9, 12.24, 55.08, 52.770520019531254, 73.29238891601562], [9, 220.932, 261.324, 52.770520019531254, 77.68993225097657], [9, 337.212, 352.512, 57.16806335449219, 71.09361724853515], [9, 296.82, 373.932, 69.62776947021484, 94.54718170166016], [9, 443.7, 484.092, 69.62776947021484, 93.08133392333984], [9, 61.199999999999996, 104.03999999999999, 102.60934448242188, 118.00074615478516], [9, 462.06, 553.2479999999999, 99.67764892578126, 115.06905059814453], [9, 8.568, 50.796, 138.52261505126953, 161.24325561523438], [9, 59.976, 122.39999999999999, 147.3177017211914, 165.64079895019532], [9, 251.53199999999998, 381.276, 146.58477783203125, 165.64079895019532], [9, 425.34, 511.632, 142.92015838623047, 161.24325561523438], [9, 227.052, 256.428, 159.77740783691408, 179.56635284423828], [9, 59.364, 149.328, 189.09436340332033, 208.15038452148437], [9, 251.53199999999998, 340.884, 190.56021118164062, 209.6162322998047], [9, 330.48, 370.26, 197.8894500732422, 221.3430145263672], [9, 59.364, 230.112, 233.0697967529297, 252.12581787109374], [9, 556.308, 597.924, 195.69067840576173, 219.87716674804688], [9, 52.019999999999996, 88.74, 285.1073928833008, 306.3621856689453], [9, 118.728, 160.344, 282.17569732666016, 306.3621856689453], [9, 329.256, 370.26, 280.70984954833983, 306.3621856689453], [9, 555.696, 597.312, 279.9769256591797, 304.89633789062503], [9, 64.26, 265.608, 323.9523590087891, 343.0083801269531], [9, 451.656, 492.65999999999997, 323.9523590087891, 348.1388473510742], [9, 65.484, 203.184, 353.2693145751953, 372.32533569335936], [9, 348.84, 389.23199999999997, 351.803466796875, 368.6607162475586], [9, 65.484, 142.596, 386.25088958740236, 404.57398681640626], [9, 170.136, 381.276, 384.78504180908203, 403.8410629272461], [9, 555.084, 596.7, 374.5241073608399, 399.44351959228516], [9, 50.184, 313.344, 445.617724609375, 465.4066696166992], [9, 451.656, 492.65999999999997, 410.4373779296875, 434.62386627197264], [9, 117.50399999999999, 159.12, 462.4749740600586, 486.6614624023438], [9, 335.988, 376.992, 460.2762023925781, 484.4626907348633], [9, 555.084, 596.7, 466.87251739501954, 491.7919296264649], [9, 0.0, 42.228, 496.9223968505859, 520.3759613037109], [9, 231.33599999999998, 272.952, 502.05286407470703, 526.2393524169922], [9, 451.044, 492.65999999999997, 502.05286407470703, 526.2393524169922], [9, 112.608, 156.06, 542.3636779785156, 566.5501663208008]]
2026-08-10 11:24:04,154 INFO     29 [qwen-vl-text] ═══ DONE ═══ 40 positions, pages=1, time=23.2s
2026-08-10 11:24:04,171 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:24:04,171 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:Prescription | outputs={"chunks": "1 items, types={'PrescriptionRecord': 1}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:24:04,171 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:24:04,172 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:24:04.171+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 21, "failed": 0, "current": {"ba5d751a94ad11f1bd9827cf206dfa2d": {"id": "ba5d751a94ad11f1bd9827cf206dfa2d", "doc_id": "b9a7e47a94ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360930217, "task_type": "dataflow", "root_trace_id": "2d4fcd13324b447999508dc50afac2e4", "root_traceparent": "00-2d4fcd13324b447999508dc50afac2e4-817dc24fdd0315e5-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:24:04,180 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:24:04,182 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:24:04,182 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 11:24:04,182 INFO     29 [qwen-vl-text] positions(95): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:24:04,182 INFO     29 [qwen-vl-text] page grouping: [4, 5, 6], lines per page: [40, 32, 23]
2026-08-10 11:24:04,617 INFO     29 [qwen-vl-text] page=4, rect=612x630, img=(1700x1750), dpi=200
2026-08-10 11:24:05,194 INFO     29 [qwen-vl-text] page=5, rect=612x634, img=(1700x1762), dpi=200
2026-08-10 11:24:05,568 INFO     29 [qwen-vl-text] page=6, rect=612x624, img=(1700x1733), dpi=200
2026-08-10 11:24:05,573 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3261
2026-08-10 11:24:05,573 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:24:05,573 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 140, \"bbox_end\": 234, \"encounter_dates\": [\"2025-10-30\", \"2025-11-07\"], \"department\": \"呼吸与危重医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n姓名：\n床号：23-03床\n病历号：0\n科室：呼吸与危重医学科医生站\n姓名：\n性别：女\n年龄：72岁\n民族：汉族\n病历号：00\n科室：呼吸与危重医学科医生站\n入院日期：2025-10-30 14:34\n住院天数：8\n出院日期：2025-11-07 11:44\n籍贯：贵州省贵阳市\n职业：退休人员\n单位：贵阳供电局\n住址：中国贵州省贵阳\n入院情况：\n李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无\n明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯\n血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治\n疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1\n周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门\n诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体\n重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病\n史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无\n中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学\n历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗\n史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已\n故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患\n者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，\n血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。\n心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检\n查：暂无\n入院诊断：1.支气管哮喘急性发作期\n诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床\n检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1\n2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝\n功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中\n心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中\n心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml\n肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移\n酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD)\n0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-3\n0 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 13:11 胸部CT平扫：1、考\n虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧\n1/3\n贵州醫科大學附屬醫院\nTHE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n出院记录\n姓名：\n床号：23-03床\n病历号：\n科室：呼吸与危重医学科医生站\n胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管\n扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊\n复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走\n行欠佳。 7、肝内囊性灶，建议超声随诊复查。2025-10-31 14:35 肺通气功能测定及支气管舒张试验：1.\n中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+) 2025-10-31 12:33。传染病筛查\n三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临\n床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31\n14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴\n定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支\n气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症\n治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。\n出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小\n结节；5.肝囊肿。\n出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查\n体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊\n区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。\nVTE评估：\n床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31\n14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴\n定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支\n气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症\n治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。\n出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小\n结节；5.肝囊肿。\n出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查\n体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊\n区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。\nVTE评估：\nPadua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：\n出院医嘱：\n1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治\n疗，定期复查肺功能，呼吸科门诊随诊；\n2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。\n3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。\n4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。\n手术名称：\n无\n出院结果：好转\n医生签名：\n日期：2025-11-07 11:44",
    "role": "user"
  }
]
2026-08-10 11:24:32,021 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:24:32,021 INFO     29 [qwen-vl-text] LLM output (len=4583):
{
  "encounter_date": "2025-11-07",
  "admission_date": "2025-10-30",
  "discharge_date": "2025-11-07",
  "hospital_days": 8,
  "department": "呼吸与危重医学科",
  "bed_number": "23-03床",
  "admission_condition": "李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检查：暂无",
  "admission_diagnoses": [
    {
      "name": "支气管哮喘急性发作期",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 12.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml 肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD) 0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 13:11 胸部CT平扫：1、考虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走行欠佳。 7、肝内囊性灶，建议超声随诊复查。2025-10-31 14:35 肺通气功能测定及支气管舒张试验：1.中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+) 2025-10-31 12:33。传染病筛查三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31 14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。",
  "auxiliary_exams": "2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 12.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml 肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD) 0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 12:33 传染病筛查三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31 14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴定：未检出流感嗜血杆菌。",
  "imaging_findings": "2025-10-31 13:11 胸部CT平扫：1、考虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走行欠佳。 7、肝内囊性灶，建议超声随诊复查。",
  "discharge_diagnoses": [
    {
      "name": "支气管哮喘急性发作期",
      "diagnosis_type": "西医"
    },
    {
      "name": "社区获得性肺炎，非重症",
      "diagnosis_type": "西医"
    },
    {
      "name": "慢性阻塞性肺疾病",
      "diagnosis_type": "西医"
    },
    {
      "name": "左肺下叶小结节",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。",
  "outcome": "好转",
  "discharge_orders": "1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治疗，定期复查肺功能，呼吸科门诊随诊；2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。",
  "do_medications": [
    "布地格福 每次2吸 每日2次"
  ],
  "do_follow_up": "1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。半年后复查胸部CT，呼吸科及胸外科随诊。定期复查腹部超声，肝胆外科随诊。定期复查肺功能，呼吸科门诊随诊。",
  "do_precautions": [
    "吸药后漱口"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": 36.2,
  "vs_pulse_bpm": 92,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 115,
  "vs_diastolic_bp_mmhg": 68
}
2026-08-10 11:24:32,022 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-07]
2026-08-10 11:24:32,030 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2186433, prompt_len=1917
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["出院记录", "姓名：", "床号：23-03床", "病历号：0", "科室：呼吸与危重医学科医生站", "姓名：", "性别：女", "年龄：72岁", "民族：汉族", "病历号：00", "科室：呼吸与危重医学科医生站", "入院日期：2025-10-30 14:34", "住院天数：8", "出院日期：2025-11-07 11:44", "籍贯：贵州省贵阳市", "职业：退休人员", "单位：贵阳供电局", "住址：中国贵州省贵阳", "入院情况：", "李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无", "明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯", "血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治", "疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1", "周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门", "诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体", "重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病", "史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无", "中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学", "历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗", "史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已", "故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患", "者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，", "血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。", "心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检", "查：暂无", "入院诊断：1.支气管哮喘急性发作期", "诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床", "检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1", "2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝", "功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中"]

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
2026-08-10 11:24:48,806 INFO     29 [qwen-vl-text] coord API raw response (len=2906):
[
	{"text": "出院记录", "bbox": [441, 8, 553, 34]},
	{"text": "姓名：", "bbox": [78, 70, 122, 90]},
	{"text": "床号：23-03床", "bbox": [248, 50, 371, 73]},
	{"text": "病历号：0", "bbox": [407, 45, 496, 64]},
	{"text": "科室：呼吸与危重医学科医生站", "bbox": [615, 44, 863, 60]},
	{"text": "姓名：", "bbox": [80, 144, 121, 163]},
	{"text": "性别：女", "bbox": [438, 122, 511, 141]},
	{"text": "年龄：72岁", "bbox": [718, 114, 803, 130]},
	{"text": "民族：汉族", "bbox": [82, 175, 168, 198]},
	{"text": "病历号：00", "bbox": [438, 162, 528, 181]},
	{"text": "科室：呼吸与危重医学科医生站", "bbox": [82, 204, 327, 235]},
	{"text": "入院日期：2025-10-30 14:34", "bbox": [439, 194, 678, 221]},
	{"text": "住院天数：8", "bbox": [83, 248, 178, 272]},
	{"text": "出院日期：2025-11-07 11:44", "bbox": [439, 235, 678, 262]},
	{"text": "籍贯：贵州省贵阳市", "bbox": [83, 284, 240, 308]},
	{"text": "职业：退休人员", "bbox": [439, 280, 563, 302]},
	{"text": "单位：贵阳供电局", "bbox": [84, 324, 223, 347]},
	{"text": "住址：中国贵州省贵阳", "bbox": [83, 362, 260, 384]},
	{"text": "入院情况：", "bbox": [83, 398, 164, 418]},
	{"text": "李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无", "bbox": [83, 412, 919, 452]},
	{"text": "明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯", "bbox": [83, 439, 919, 480]},
	{"text": "血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治", "bbox": [83, 467, 919, 507]},
	{"text": "疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1", "bbox": [83, 495, 910, 534]},
	{"text": "周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门", "bbox": [83, 523, 904, 562]},
	{"text": "诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体", "bbox": [83, 551, 909, 589]},
	{"text": "重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病", "bbox": [83, 580, 891, 616]},
	{"text": "史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无", "bbox": [83, 607, 907, 644]},
	{"text": "中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学", "bbox": [83, 635, 912, 671]},
	{"text": "历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗", "bbox": [85, 662, 909, 697]},
	{"text": "史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已", "bbox": [87, 689, 891, 723]},
	{"text": "故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患", "bbox": [87, 714, 906, 748]},
	{"text": "者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，", "bbox": [87, 740, 891, 773]},
	{"text": "血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。", "bbox": [87, 765, 884, 800]},
	{"text": "心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检", "bbox": [87, 790, 893, 825]},
	{"text": "查：暂无", "bbox": [87, 832, 157, 851]},
	{"text": "入院诊断：1.支气管哮喘急性发作期", "bbox": [85, 859, 366, 879]},
	{"text": "诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床", "bbox": [85, 874, 907, 906]},
	{"text": "检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1", "bbox": [85, 901, 909, 932]},
	{"text": "2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝", "bbox": [83, 928, 910, 959]},
	{"text": "功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中", "bbox": [83, 955, 903, 986]}
]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=16.8s
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[441, 8, 553, 34]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[78, 70, 122, 90]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[2]: text=床号：23-03床, bbox=[248, 50, 371, 73]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[3]: text=病历号：0, bbox=[407, 45, 496, 64]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重医学科医生站, bbox=[615, 44, 863, 60]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[5]: text=姓名：, bbox=[80, 144, 121, 163]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女, bbox=[438, 122, 511, 141]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：72岁, bbox=[718, 114, 803, 130]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[8]: text=民族：汉族, bbox=[82, 175, 168, 198]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[9]: text=病历号：00, bbox=[438, 162, 528, 181]
2026-08-10 11:24:48,807 INFO     29 [qwen-vl-text] coord item[10]: text=科室：呼吸与危重医学科医生站, bbox=[82, 204, 327, 235]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[11]: text=入院日期：2025-10-30 14:34, bbox=[439, 194, 678, 221]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[12]: text=住院天数：8, bbox=[83, 248, 178, 272]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[13]: text=出院日期：2025-11-07 11:44, bbox=[439, 235, 678, 262]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[14]: text=籍贯：贵州省贵阳市, bbox=[83, 284, 240, 308]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[15]: text=职业：退休人员, bbox=[439, 280, 563, 302]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[16]: text=单位：贵阳供电局, bbox=[84, 324, 223, 347]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[17]: text=住址：中国贵州省贵阳, bbox=[83, 362, 260, 384]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[18]: text=入院情况：, bbox=[83, 398, 164, 418]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[19]: text=李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无, bbox=[83, 412, 919, 452]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[20]: text=明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯, bbox=[83, 439, 919, 480]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[21]: text=血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治, bbox=[83, 467, 919, 507]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[22]: text=疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1, bbox=[83, 495, 910, 534]
2026-08-10 11:24:48,808 INFO     29 [qwen-vl-text] coord item[23]: text=周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门, bbox=[83, 523, 904, 562]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[24]: text=诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体, bbox=[83, 551, 909, 589]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[25]: text=重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病, bbox=[83, 580, 891, 616]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[26]: text=史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无, bbox=[83, 607, 907, 644]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[27]: text=中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学, bbox=[83, 635, 912, 671]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[28]: text=历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗, bbox=[85, 662, 909, 697]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[29]: text=史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已, bbox=[87, 689, 891, 723]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[30]: text=故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患, bbox=[87, 714, 906, 748]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[31]: text=者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，, bbox=[87, 740, 891, 773]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[32]: text=血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。, bbox=[87, 765, 884, 800]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[33]: text=心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检, bbox=[87, 790, 893, 825]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[34]: text=查：暂无, bbox=[87, 832, 157, 851]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[35]: text=入院诊断：1.支气管哮喘急性发作期, bbox=[85, 859, 366, 879]
2026-08-10 11:24:48,809 INFO     29 [qwen-vl-text] coord item[36]: text=诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床, bbox=[85, 874, 907, 906]
2026-08-10 11:24:48,810 INFO     29 [qwen-vl-text] coord item[37]: text=检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1, bbox=[85, 901, 909, 932]
2026-08-10 11:24:48,810 INFO     29 [qwen-vl-text] coord item[38]: text=2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝, bbox=[83, 928, 910, 959]
2026-08-10 11:24:48,810 INFO     29 [qwen-vl-text] coord item[39]: text=功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中, bbox=[83, 955, 903, 986]
2026-08-10 11:24:48,811 INFO     29 [qwen-vl-text] page=4 — 40/40 coords, api_time=16.8s
2026-08-10 11:24:48,822 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3462031, prompt_len=2059
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中", "心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml", "肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移", "酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD)", "0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-3", "0 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 13:11 胸部CT平扫：1、考", "虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧", "1/3", "贵州醫科大學附屬醫院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "出院记录", "姓名：", "床号：23-03床", "病历号：", "科室：呼吸与危重医学科医生站", "胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管", "扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊", "复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走", "行欠佳。 7、肝内囊性灶，建议超声随诊复查。2025-10-31 14:35 肺通气功能测定及支气管舒张试验：1.", "中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+) 2025-10-31 12:33。传染病筛查", "三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临", "床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31", "14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴", "定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。", "出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小", "结节；5.肝囊肿。", "出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查", "体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊", "区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。", "VTE评估："]

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
2026-08-10 11:25:04,154 INFO     29 [qwen-vl-text] coord API raw response (len=2729):
[
	{"text": "心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中", "bbox": [68, 14, 877, 35]},
	{"text": "心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml", "bbox": [68, 40, 903, 61]},
	{"text": "肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移", "bbox": [68, 65, 904, 87]},
	{"text": "酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD)", "bbox": [68, 91, 893, 112]},
	{"text": "0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-3", "bbox": [68, 117, 904, 138]},
	{"text": "0 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 13:11 胸部CT平扫：1、考", "bbox": [68, 143, 904, 164]},
	{"text": "虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧", "bbox": [68, 169, 896, 190]},
	{"text": "1/3", "bbox": [468, 220, 494, 236]},
	{"text": "贵州醫科大學附屬醫院", "bbox": [344, 360, 721, 398]},
	{"text": "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "bbox": [348, 406, 721, 420]},
	{"text": "出院记录", "bbox": [423, 440, 535, 466]},
	{"text": "姓名：", "bbox": [63, 478, 107, 497]},
	{"text": "床号：23-03床", "bbox": [232, 477, 354, 494]},
	{"text": "病历号：", "bbox": [390, 477, 457, 494]},
	{"text": "科室：呼吸与危重医学科医生站", "bbox": [598, 476, 856, 493]},
	{"text": "胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管", "bbox": [63, 517, 894, 538]},
	{"text": "扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊", "bbox": [63, 543, 894, 564]},
	{"text": "复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走", "bbox": [63, 569, 904, 590]},
	{"text": "行欠佳。 7、肝内囊性灶，建议超声随诊复查。2025-10-31 14:35 肺通气功能测定及支气管舒张试验：1.", "bbox": [63, 595, 900, 617]},
	{"text": "中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+) 2025-10-31 12:33。传染病筛查", "bbox": [60, 622, 904, 644]},
	{"text": "三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临", "bbox": [56, 649, 896, 671]},
	{"text": "床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31", "bbox": [54, 676, 904, 698]},
	{"text": "14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴", "bbox": [52, 703, 888, 725]},
	{"text": "定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "bbox": [50, 730, 906, 752]},
	{"text": "气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "bbox": [48, 757, 898, 779]},
	{"text": "治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。", "bbox": [47, 785, 814, 808]},
	{"text": "出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小", "bbox": [47, 813, 905, 836]},
	{"text": "结节；5.肝囊肿。", "bbox": [45, 844, 187, 866]},
	{"text": "出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查", "bbox": [45, 869, 889, 892]},
	{"text": "体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊", "bbox": [44, 897, 900, 919]},
	{"text": "区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。", "bbox": [44, 925, 853, 948]},
	{"text": "VTE评估：", "bbox": [43, 960, 126, 980]}
]
2026-08-10 11:25:04,154 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=15.3s
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[0]: text=心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中, bbox=[68, 14, 877, 35]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[1]: text=心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml, bbox=[68, 40, 903, 61]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[2]: text=肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移, bbox=[68, 65, 904, 87]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[3]: text=酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD), bbox=[68, 91, 893, 112]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[4]: text=0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-3, bbox=[68, 117, 904, 138]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[5]: text=0 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 13:11 胸部CT平扫：1、考, bbox=[68, 143, 904, 164]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[6]: text=虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧, bbox=[68, 169, 896, 190]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[7]: text=1/3, bbox=[468, 220, 494, 236]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[8]: text=贵州醫科大學附屬醫院, bbox=[344, 360, 721, 398]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[9]: text=THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY, bbox=[348, 406, 721, 420]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[10]: text=出院记录, bbox=[423, 440, 535, 466]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[11]: text=姓名：, bbox=[63, 478, 107, 497]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[12]: text=床号：23-03床, bbox=[232, 477, 354, 494]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[13]: text=病历号：, bbox=[390, 477, 457, 494]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[14]: text=科室：呼吸与危重医学科医生站, bbox=[598, 476, 856, 493]
2026-08-10 11:25:04,155 INFO     29 [qwen-vl-text] coord item[15]: text=胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管, bbox=[63, 517, 894, 538]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[16]: text=扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊, bbox=[63, 543, 894, 564]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[17]: text=复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走, bbox=[63, 569, 904, 590]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[18]: text=行欠佳。 7、肝内囊性灶，建议超声随诊复查。2025-10-31 14:35 肺通气功能测定及支气管舒张试验：1., bbox=[63, 595, 900, 617]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[19]: text=中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+) 2025-10-31 12:33。传染病筛查, bbox=[60, 622, 904, 644]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[20]: text=三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临, bbox=[56, 649, 896, 671]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[21]: text=床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31, bbox=[54, 676, 904, 698]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[22]: text=14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴, bbox=[52, 703, 888, 725]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[23]: text=定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支, bbox=[50, 730, 906, 752]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[24]: text=气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症, bbox=[48, 757, 898, 779]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[25]: text=治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。, bbox=[47, 785, 814, 808]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[26]: text=出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小, bbox=[47, 813, 905, 836]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[27]: text=结节；5.肝囊肿。, bbox=[45, 844, 187, 866]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[28]: text=出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查, bbox=[45, 869, 889, 892]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[29]: text=体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊, bbox=[44, 897, 900, 919]
2026-08-10 11:25:04,156 INFO     29 [qwen-vl-text] coord item[30]: text=区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。, bbox=[44, 925, 853, 948]
2026-08-10 11:25:04,157 INFO     29 [qwen-vl-text] coord item[31]: text=VTE评估：, bbox=[43, 960, 126, 980]
2026-08-10 11:25:04,158 INFO     29 [qwen-vl-text] page=5 — 32/32 coords, api_time=15.3s
2026-08-10 11:25:04,161 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1083764, prompt_len=1407
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31", "14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴", "定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。", "出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小", "结节；5.肝囊肿。", "出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查", "体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊", "区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。", "VTE评估：", "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "出院医嘱：", "1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治", "疗，定期复查肺功能，呼吸科门诊随诊；", "2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。", "3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。", "4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。", "手术名称：", "无", "出院结果：好转", "医生签名：", "日期：2025-11-07 11:44"]

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
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord API raw response (len=1710):
[
	{"text": "床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31", "bbox": [17, 7, 891, 31]},
	{"text": "14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴", "bbox": [18, 33, 874, 60]},
	{"text": "定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "bbox": [18, 60, 895, 89]},
	{"text": "气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "bbox": [18, 87, 888, 116]},
	{"text": "治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。", "bbox": [18, 113, 807, 140]},
	{"text": "出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小", "bbox": [20, 139, 898, 174]},
	{"text": "结节；5.肝囊肿。", "bbox": [20, 166, 164, 186]},
	{"text": "出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查", "bbox": [24, 192, 886, 230]},
	{"text": "体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊", "bbox": [24, 219, 900, 260]},
	{"text": "区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。", "bbox": [27, 247, 855, 282]},
	{"text": "VTE评估：", "bbox": [29, 273, 111, 292]},
	{"text": "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "bbox": [31, 300, 677, 331]},
	{"text": "出院医嘱：", "bbox": [40, 353, 127, 372]},
	{"text": "1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治", "bbox": [42, 379, 907, 440]},
	{"text": "疗，定期复查肺功能，呼吸科门诊随诊；", "bbox": [43, 407, 363, 434]},
	{"text": "2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。", "bbox": [44, 434, 842, 490]},
	{"text": "3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。", "bbox": [45, 460, 589, 491]},
	{"text": "4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。", "bbox": [47, 487, 460, 512]},
	{"text": "手术名称：", "bbox": [50, 512, 134, 530]},
	{"text": "无", "bbox": [55, 544, 74, 561]},
	{"text": "出院结果：好转", "bbox": [59, 574, 176, 594]},
	{"text": "医生签名：", "bbox": [688, 651, 772, 675]},
	{"text": "日期：2025-11-07 11:44", "bbox": [710, 693, 907, 721]}
]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=10.9s
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[0]: text=床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31, bbox=[17, 7, 891, 31]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[1]: text=14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴, bbox=[18, 33, 874, 60]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[2]: text=定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支, bbox=[18, 60, 895, 89]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[3]: text=气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症, bbox=[18, 87, 888, 116]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[4]: text=治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。, bbox=[18, 113, 807, 140]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[5]: text=出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小, bbox=[20, 139, 898, 174]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[6]: text=结节；5.肝囊肿。, bbox=[20, 166, 164, 186]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[7]: text=出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查, bbox=[24, 192, 886, 230]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[8]: text=体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊, bbox=[24, 219, 900, 260]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[9]: text=区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。, bbox=[27, 247, 855, 282]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[10]: text=VTE评估：, bbox=[29, 273, 111, 292]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[11]: text=Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：, bbox=[31, 300, 677, 331]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[12]: text=出院医嘱：, bbox=[40, 353, 127, 372]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[13]: text=1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治, bbox=[42, 379, 907, 440]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[14]: text=疗，定期复查肺功能，呼吸科门诊随诊；, bbox=[43, 407, 363, 434]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[15]: text=2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。, bbox=[44, 434, 842, 490]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[16]: text=3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。, bbox=[45, 460, 589, 491]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[17]: text=4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。, bbox=[47, 487, 460, 512]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[18]: text=手术名称：, bbox=[50, 512, 134, 530]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[19]: text=无, bbox=[55, 544, 74, 561]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[20]: text=出院结果：好转, bbox=[59, 574, 176, 594]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[21]: text=医生签名：, bbox=[688, 651, 772, 675]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] coord item[22]: text=日期：2025-11-07 11:44, bbox=[710, 693, 907, 721]
2026-08-10 11:25:15,032 INFO     29 [qwen-vl-text] page=6 — 23/23 coords, api_time=10.9s
2026-08-10 11:25:15,033 INFO     29 [qwen-vl-text] new_positions (95):
[[4, 269.892, 338.436, 5.03718408203125, 21.408032348632812], [4, 47.736, 74.664, 44.075360717773435, 56.668320922851564], [4, 151.776, 227.052, 31.482400512695314, 45.964304748535156], [4, 249.084, 303.552, 28.334160461425782, 40.29747265625], [4, 376.38, 528.156, 27.704512451171876, 37.77888061523438], [4, 48.96, 74.05199999999999, 90.66931347656251, 102.63262567138672], [4, 268.056, 312.73199999999997, 76.81705725097656, 88.78036944580079], [4, 439.416, 491.436, 71.77987316894531, 81.85424133300782], [4, 50.184, 102.816, 110.1884017944336, 124.67030603027344], [4, 268.056, 323.13599999999997, 102.00297766113282, 113.96628985595703], [4, 50.184, 200.124, 128.44819409179686, 147.96728240966797], [4, 268.668, 414.936, 122.15171398925781, 139.1522102661133], [4, 50.796, 108.93599999999999, 156.15270654296876, 171.2642587890625], [4, 268.668, 414.936, 147.96728240966797, 164.96777868652345], [4, 50.796, 146.88, 178.82003491210938, 193.93158715820314], [4, 268.668, 344.556, 176.30144287109374, 190.1536990966797], [4, 51.408, 136.476, 204.00595532226563, 218.48785955810547], [4, 50.796, 159.12, 227.93257971191406, 241.78483593750002], [4, 50.796, 100.368, 250.5999080810547, 263.1928682861328], [4, 50.796, 562.428, 259.4149802246094, 284.60090063476565], [4, 50.796, 562.428, 276.41547650146487, 302.231044921875], [4, 50.796, 562.428, 294.04562078857424, 319.2315411987305], [4, 50.796, 556.92, 311.6757650756836, 336.23203747558597], [4, 50.796, 553.2479999999999, 329.305909362793, 353.86218176269534], [4, 50.796, 556.308, 346.93605364990236, 370.8626780395508], [4, 50.796, 545.292, 365.19584594726564, 387.8631743164063], [4, 50.796, 555.084, 382.1963422241211, 405.49331860351566], [4, 50.796, 558.144, 399.8264865112305, 422.4938148803711], [4, 52.019999999999996, 556.308, 416.82698278808596, 438.86466314697265], [4, 53.244, 545.292, 433.82747906494143, 455.2355114135742], [4, 53.244, 554.472, 449.5686793212891, 470.9767116699219], [4, 53.244, 545.292, 465.9395275878906, 486.71791192626955], [4, 53.244, 541.008, 481.6807278442383, 503.718408203125], [4, 53.244, 546.516, 497.42192810058594, 519.4596084594726], [4, 53.244, 96.084, 523.86714453125, 535.8304567260742], [4, 52.019999999999996, 223.992, 540.8676408081055, 553.4606010131836], [4, 52.019999999999996, 555.084, 550.3123609619141, 570.4610972900391], [4, 52.019999999999996, 556.308, 567.3128572387695, 586.8319455566407], [4, 50.796, 556.92, 584.3133535156251, 603.8324418334961], [4, 50.796, 552.636, 601.3138497924805, 620.8329381103516], [5, 41.616, 536.724, 8.877274047851563, 22.193185119628907], [5, 41.616, 552.636, 25.36364013671875, 38.67955120849609], [5, 41.616, 553.2479999999999, 41.21591522216797, 55.16591729736328], [5, 41.616, 546.516, 57.70228131103516, 71.0181923828125], [5, 41.616, 553.2479999999999, 74.18864739990235, 87.50455847167969], [5, 41.616, 553.2479999999999, 90.67501348876954, 103.99092456054687], [5, 41.616, 548.352, 107.16137957763672, 120.47729064941406], [5, 286.416, 302.328, 139.50002075195312, 149.64547680664063], [5, 210.528, 441.252, 228.27276123046875, 252.36821936035156], [5, 212.976, 441.252, 257.4409473876953, 266.3182214355469], [5, 258.876, 327.42, 279.00004150390623, 295.48640759277345], [5, 38.556, 65.484, 303.0954996337891, 315.14322869873047], [5, 141.984, 216.648, 302.4614086303711, 313.24095568847656], [5, 238.68, 279.68399999999997, 302.4614086303711, 313.24095568847656], [5, 365.976, 523.872, 301.8273176269531, 312.6068646850586], [5, 38.556, 547.128, 327.82504876708987, 341.1409598388672], [5, 38.556, 547.128, 344.311414855957, 357.6273259277344], [5, 38.556, 553.2479999999999, 360.79778094482424, 374.1136920166016], [5, 38.556, 550.8, 377.2841470336914, 391.2341491088867], [5, 36.72, 553.2479999999999, 394.40460412597656, 408.35460620117186], [5, 34.272, 548.352, 411.5250612182617, 425.475063293457], [5, 33.048, 553.2479999999999, 428.6455183105469, 442.5955203857422], [5, 31.823999999999998, 543.456, 445.76597540283205, 459.71597747802736], [5, 30.599999999999998, 554.472, 462.8864324951172, 476.8364345703125], [5, 29.375999999999998, 549.576, 480.0068895874023, 493.9568916625977], [5, 28.764, 498.168, 497.7614376831055, 512.3455307617188], [5, 28.764, 553.86, 515.5159857788086, 530.1000788574219], [5, 27.54, 114.444, 535.1728068847656, 549.1228089599609], [5, 27.54, 544.068, 551.0250819702148, 565.6091750488281], [5, 26.928, 550.8, 568.779630065918, 582.7296321411133], [5, 26.928, 522.036, 586.5341781616211, 601.1182712402344], [5, 26.316, 77.112, 608.7273632812501, 621.4091833496094], [6, 10.404, 545.292, 4.364990051269531, 19.33067022705078], [6, 11.016, 534.888, 20.57781024169922, 37.414200439453126], [6, 11.016, 547.74, 37.414200439453126, 55.49773065185547], [6, 11.016, 543.456, 54.25059063720703, 72.33412084960938], [6, 11.016, 493.884, 70.46341082763672, 87.29980102539062], [6, 12.24, 549.576, 86.6762310180664, 108.50118127441407], [6, 12.24, 100.368, 103.51262121582032, 115.98402136230469], [6, 14.687999999999999, 542.232, 119.72544140625, 143.42110168457032], [6, 14.687999999999999, 550.8, 136.5618316040039, 162.12820190429687], [6, 16.524, 523.26, 154.02179180908203, 175.84674206542968], [6, 17.748, 67.932, 170.2346119995117, 182.08244213867187], [6, 18.972, 414.324, 187.0710021972656, 206.40167242431642], [6, 24.48, 77.724, 220.12021258544922, 231.96804272460938], [6, 25.704, 555.084, 236.3330327758789, 274.37080322265626], [6, 26.316, 222.156, 253.79299298095702, 270.62938317871095], [6, 26.928, 515.304, 270.62938317871095, 305.5493035888672], [6, 27.54, 360.468, 286.84220336914063, 306.1728735961914], [6, 28.764, 281.52, 303.6785935668945, 319.26784375], [6, 30.599999999999998, 82.008, 319.26784375, 330.49210388183593], [6, 33.66, 45.288, 339.222083984375, 349.82277410888673], [6, 36.108, 107.712, 357.92918420410155, 370.4005843505859], [6, 421.056, 472.464, 405.9440747680664, 420.90975494384764], [6, 434.52, 555.084, 432.1340150756836, 449.5939752807617]]
2026-08-10 11:25:15,033 INFO     29 [qwen-vl-text] ═══ DONE ═══ 95 positions, pages=3, time=70.9s
2026-08-10 11:25:15,052 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:25:15,052 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:25:15,053 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:25:15,053 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:25:15.053+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 21, "failed": 0, "current": {"ba5d751a94ad11f1bd9827cf206dfa2d": {"id": "ba5d751a94ad11f1bd9827cf206dfa2d", "doc_id": "b9a7e47a94ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360930217, "task_type": "dataflow", "root_trace_id": "2d4fcd13324b447999508dc50afac2e4", "root_traceparent": "00-2d4fcd13324b447999508dc50afac2e4-817dc24fdd0315e5-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:25:15,062 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:25:15,063 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:25:15,064 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 11:25:15,064 INFO     29 [qwen-vl-text] positions(140): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:25:15,064 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [42, 32, 36, 30]
2026-08-10 11:25:15,441 INFO     29 [qwen-vl-text] page=0, rect=612x627, img=(1700x1741), dpi=200
2026-08-10 11:25:15,792 INFO     29 [qwen-vl-text] page=1, rect=612x620, img=(1700x1723), dpi=200
2026-08-10 11:25:16,142 INFO     29 [qwen-vl-text] page=2, rect=612x618, img=(1700x1718), dpi=200
2026-08-10 11:25:16,490 INFO     29 [qwen-vl-text] page=3, rect=612x628, img=(1700x1745), dpi=200
2026-08-10 11:25:16,493 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2252
2026-08-10 11:25:16,493 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:25:16,493 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 139, \"encounter_dates\": [\"2025-10-30\"], \"department\": \"呼吸与危重医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "入院记录\n姓名：\n床号：23-03床\n病历号：0\n科室：呼吸与危重医学科医生\n站\n姓名：\n性别：女\n年龄：72岁\n出生地：贵州省贵阳市\n职业：退休人员\n民族：汉族\n婚姻：已婚\n联系地址：中国贵州省贵阳市\n入院时间：2025-10-30 14:34\n病史陈述者：本人\n主诉：咳嗽、咳痰5年，加重1周\n现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，\n不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管\n哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感\n和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治\n就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二\n便如常，近1年体重减少4kg。\n既往史：\n患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染\n病；食物、药物过敏无；无外伤史：无手术史：无输血史：无中毒史：无长期用药史：无可能成瘾药物。疫\n苗接种史不详\n个人史：\n出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长\n地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物\n质接触史。\n婚育史：\n已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。\n月经史：\n初潮年龄17岁\n经期3-4天\n绝经年龄53岁 月经及白带情况：正常\n月经周期30天\n家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否\n认二系三代有遗传病史。患者否认有遗传倾向的疾病。\n体格检查\n生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60\n体格检查\n生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体\n重：44kg，腰围：cm，BMI：18.8 kg/m²\n一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常\n表情：正常体位：自主体位步态：平稳配合检查：配合\n皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无\n皮疹：无紫癜：无\n1/3\n贵州醫科大學附属醫院\nTHE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n入院记录\n姓名：\n床号：23-03床\n病历号\n科室：呼吸与危重医学科医生\n站\n水肿：无脱水现象：无松紧度：适中\n温度：适中出汗：无显性出汗瘢痕：无感染：无\n头颅：大小：正常畸形：无包块：无\n凹陷：无压痛：无\n眼：眼睑：无水肿结膜：无充血巩膜：无黄染\n眼球四个象限运动：左眼：正常右眼：正常\n眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆\n对光反射：左眼：灵敏右眼：灵敏\n鼻：外形：正常其他异常：无鼻旁窦压痛：无\n口：唇：无紫绀粘膜：无充血腮腺导管开口：正常\n舌：伸舌居中牙龈：无肿胀龋齿：无\n咽喉：扁桃体：正常咽：无充血声音：正常\n淋巴：淋巴结：全身浅表淋巴结未及肿大\n颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张\n气管：居中颈静脉回流征：无\n甲状腺：无肿大\n眼球四个象限运动：左眼：正常 右眼：正常\n眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆\n对光反射：左眼：灵敏 右眼：灵敏\n鼻：外形：正常 其他异常：无 鼻旁窦压痛：无\n口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常\n舌：伸舌居中 牙龈：无肿胀 龋齿：无\n咽 喉：扁桃体：正常 咽：无充血 声音：正常\n淋巴 巴：淋巴结：全身浅表淋巴结未及肿大\n颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张\n气管：居中 颈静脉回流征：无\n甲状腺：无肿大\n胸部 部：胸廓：无畸形 乳房：\n肺 部：视诊：呼吸运动\n触诊：\n叩诊：\n听诊：\n语音传导\n心 脏：视诊：\n触诊：心尖搏动\n叩诊：\n心界\n右(cm)\n肋间\n左(cm)\n2\n2\n2\n3\n(左锁骨中线距胸骨线7.5cm)\n听诊：心率：92次/分 心律：齐 心音：未闻及异常心\n额外心音：无 杂音：无 心包摩擦感：\n周围血管：异常血管征：无\n腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出\n其他异常：无\n触诊：腹壁：柔软 压痛：无\n2/3\n站\n反跳痛：无\n液波振颤：无 振水声：无\n腹部包块：无\n肝：肋下未及\n胆囊：未触及 Murphy征：阴性\n脾：未触及\n叩诊：肝浊音界：正常 移动性浊音：无\n肾区叩痛：无\n听诊：肠鸣音：正常 肠鸣音频率：4次/分\n气过水音：无 血管杂音：无\n肛门直肠：未检\n生殖器：未检\n脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限\n压痛，叩痛：无\n杵状指趾：无\n神经系统：腹壁反射：正常 肢体瘫痪：无\n肌张力：正常 肌力：V级\n肱二头肌反射：正常 Hoffman征：阴性\n膝腱反射：正常 Kernig征：阴性\n跟腱反射：正常 Babinski征：阴性\n其他：无\n补充及专科情况\n双肺呼吸音清，未闻及干湿性啰音。\n辅助检查：暂无\nVTE评估：\nPadua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：\n入院诊断：1.支气管哮喘急性发作期\n医师签名：\n日期：2025-10-30 16:38",
    "role": "user"
  }
]
2026-08-10 11:25:27,972 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:25:27,972 INFO     29 [qwen-vl-text] LLM output (len=2247):
{
  "encounter_date": "2025-10-30",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 72,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "退休人员",
  "dm_admission_time": "2025-10-30 14:34",
  "dm_record_time": "2025-10-30 16:38",
  "dm_history_provider": "本人",
  "cc_text": "咳嗽、咳痰5年，加重1周",
  "cc_main_symptoms": [
    "咳嗽",
    "咳痰"
  ],
  "cc_duration": "5年，加重1周",
  "pi_text": "5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体重减少4kg。",
  "pmh_disease_history": [
    "无高血压",
    "无糖尿病",
    "无心脏病",
    "无肾病史",
    "无肺结核",
    "无病毒性肝炎",
    "无其他传染病"
  ],
  "pmh_allergy_history": [
    "食物、药物过敏无"
  ],
  "pmh_surgery_trauma_history": [
    "无外伤史",
    "无手术史",
    "无输血史",
    "无中毒史"
  ],
  "ph_smoking": "无吸烟习惯",
  "ph_drinking": "无饮酒习惯",
  "oh_menarche_age": 17,
  "oh_menopause_age": 53,
  "oh_pregnancies": "育有1子1女",
  "fh_text": "父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患者否认有遗传倾向的疾病。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.2,
  "vs_pulse_bpm": 92,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 115,
  "vs_diastolic_bp_mmhg": 68,
  "pe_general_condition": "发育：无畸形 营养：良好 神志：清晰 呼吸：均匀 面容：正常 表情：正常 体位：自主体位 步态：平稳 配合检查：配合",
  "pe_skin_mucosa": "苍白：无 潮红：无 面颊潮红：无 绀红：无 黄色：无 皮疹：无 紫癜：无 水肿：无 脱水现象：无 松紧度：适中 温度：适中 出汗：无显性出汗 瘢痕：无 感染：无",
  "pe_lymph_nodes": "全身浅表淋巴结未及肿大",
  "pe_lungs": "双肺呼吸音清，未闻及干湿性啰音。",
  "pe_heart": "心率：92次/分 心律：齐 心音：未闻及异常心 额外心音：无 杂音：无 心包摩擦感：无 周围血管：异常血管征：无",
  "pe_abdomen": "视诊：外形：平坦 腹式呼吸：存在 脐：无突出 其他异常：无 触诊：腹壁：柔软 压痛：无 反跳痛：无 液波振颤：无 振水声：无 腹部包块：无 肝：肋下未及 胆囊：未触及 Murphy征：阴性 脾：未触及 叩诊：肝浊音界：正常 移动性浊音：无 肾区叩痛：无 听诊：肠鸣音：正常 肠鸣音频率：4次/分 气过水音：无 血管杂音：无",
  "pe_extremities": "脊柱：无畸形 四肢：正常 活动：不受限 压痛，叩痛：无 杵状指趾：无",
  "pe_nervous_system": "腹壁反射：正常 肢体瘫痪：无 肌张力：正常 肌力：V级 肱二头肌反射：正常 Hoffman征：阴性 膝腱反射：正常 Kernig征：阴性 跟腱反射：正常 Babinski征：阴性 其他：无",
  "pe_specialist_exam": "双肺呼吸音清，未闻及干湿性啰音。",
  "pe_ecog_score": null,
  "pat_text": "暂无",
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "支气管哮喘急性发作期",
      "diagnosis_type": "西医",
      "is_primary": true
    }
  ],
  "department": "呼吸与危重医学科"
}
2026-08-10 11:25:27,972 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-30]
2026-08-10 11:25:27,974 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1116015, prompt_len=1554
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共42行）
["入院记录", "姓名：", "床号：23-03床", "病历号：0", "科室：呼吸与危重医学科医生", "站", "姓名：", "性别：女", "年龄：72岁", "出生地：贵州省贵阳市", "职业：退休人员", "民族：汉族", "婚姻：已婚", "联系地址：中国贵州省贵阳市", "入院时间：2025-10-30 14:34", "病史陈述者：本人", "主诉：咳嗽、咳痰5年，加重1周", "现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，", "不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管", "哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感", "和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治", "就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二", "便如常，近1年体重减少4kg。", "既往史：", "患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染", "病；食物、药物过敏无；无外伤史：无手术史：无输血史：无中毒史：无长期用药史：无可能成瘾药物。疫", "苗接种史不详", "个人史：", "出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长", "地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物", "质接触史。", "婚育史：", "已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。", "月经史：", "初潮年龄17岁", "经期3-4天", "绝经年龄53岁 月经及白带情况：正常", "月经周期30天", "家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否", "认二系三代有遗传病史。患者否认有遗传倾向的疾病。", "体格检查", "生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60"]

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
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord API raw response (len=2624):
[
	{"text": "入院记录", "bbox": [425, 0, 538, 24]},
	{"text": "姓名：", "bbox": [77, 37, 118, 56]},
	{"text": "床号：23-03床", "bbox": [240, 37, 359, 56]},
	{"text": "病历号：0", "bbox": [432, 35, 520, 53]},
	{"text": "科室：呼吸与危重医学科医生", "bbox": [655, 34, 895, 51]},
	{"text": "站", "bbox": [77, 64, 94, 82]},
	{"text": "姓名：", "bbox": [88, 143, 161, 162]},
	{"text": "性别：女", "bbox": [456, 137, 585, 156]},
	{"text": "年龄：72岁", "bbox": [88, 180, 218, 200]},
	{"text": "出生地：贵州省贵阳市", "bbox": [456, 173, 676, 193]},
	{"text": "职业：退休人员", "bbox": [88, 220, 255, 240]},
	{"text": "民族：汉族", "bbox": [458, 211, 604, 231]},
	{"text": "婚姻：已婚", "bbox": [88, 258, 222, 278]},
	{"text": "联系地址：中国贵州省贵阳市", "bbox": [459, 247, 710, 267]},
	{"text": "入院时间：2025-10-30 14:34", "bbox": [90, 321, 333, 340]},
	{"text": "病史陈述者：本人", "bbox": [460, 310, 604, 331]},
	{"text": "主诉：咳嗽、咳痰5年，加重1周", "bbox": [83, 353, 332, 372]},
	{"text": "现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，", "bbox": [83, 367, 885, 397]},
	{"text": "不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管", "bbox": [83, 393, 900, 422]},
	{"text": "哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感", "bbox": [83, 419, 900, 448]},
	{"text": "和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治", "bbox": [83, 445, 908, 474]},
	{"text": "就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二", "bbox": [83, 471, 900, 500]},
	{"text": "便如常，近1年体重减少4kg。", "bbox": [84, 511, 300, 531]},
	{"text": "既往史：", "bbox": [85, 542, 148, 561]},
	{"text": "患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染", "bbox": [85, 558, 897, 587]},
	{"text": "病；食物、药物过敏无；无外伤史：无手术史：无输血史：无中毒史：无长期用药史：无可能成瘾药物。疫", "bbox": [85, 584, 905, 613]},
	{"text": "苗接种史不详", "bbox": [86, 620, 188, 639]},
	{"text": "个人史：", "bbox": [86, 648, 148, 667]},
	{"text": "出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长", "bbox": [86, 669, 896, 693]},
	{"text": "地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物", "bbox": [86, 695, 896, 719]},
	{"text": "质接触史。", "bbox": [86, 724, 164, 743]},
	{"text": "婚育史：", "bbox": [86, 752, 149, 771]},
	{"text": "已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。", "bbox": [87, 779, 584, 801]},
	{"text": "月经史：", "bbox": [87, 805, 151, 824]},
	{"text": "初潮年龄17岁", "bbox": [89, 855, 195, 875]},
	{"text": "经期3-4天", "bbox": [239, 845, 318, 865]},
	{"text": "绝经年龄53岁 月经及白带情况：正常", "bbox": [367, 857, 664, 877]},
	{"text": "月经周期30天", "bbox": [223, 880, 332, 900]},
	{"text": "家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否", "bbox": [90, 906, 904, 927]},
	{"text": "认二系三代有遗传病史。患者否认有遗传倾向的疾病。", "bbox": [90, 932, 502, 952]},
	{"text": "体格检查", "bbox": [461, 960, 534, 979]},
	{"text": "生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60", "bbox": [90, 984, 687, 1000]}
]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord API: raw_items=42, valid_items=42, elapsed=13.9s
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[0]: text=入院记录, bbox=[425, 0, 538, 24]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[77, 37, 118, 56]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[2]: text=床号：23-03床, bbox=[240, 37, 359, 56]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[3]: text=病历号：0, bbox=[432, 35, 520, 53]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重医学科医生, bbox=[655, 34, 895, 51]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[5]: text=站, bbox=[77, 64, 94, 82]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[6]: text=姓名：, bbox=[88, 143, 161, 162]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[7]: text=性别：女, bbox=[456, 137, 585, 156]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：72岁, bbox=[88, 180, 218, 200]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[9]: text=出生地：贵州省贵阳市, bbox=[456, 173, 676, 193]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[10]: text=职业：退休人员, bbox=[88, 220, 255, 240]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[11]: text=民族：汉族, bbox=[458, 211, 604, 231]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[12]: text=婚姻：已婚, bbox=[88, 258, 222, 278]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[13]: text=联系地址：中国贵州省贵阳市, bbox=[459, 247, 710, 267]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[14]: text=入院时间：2025-10-30 14:34, bbox=[90, 321, 333, 340]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[15]: text=病史陈述者：本人, bbox=[460, 310, 604, 331]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[16]: text=主诉：咳嗽、咳痰5年，加重1周, bbox=[83, 353, 332, 372]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[17]: text=现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，, bbox=[83, 367, 885, 397]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[18]: text=不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管, bbox=[83, 393, 900, 422]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[19]: text=哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感, bbox=[83, 419, 900, 448]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[20]: text=和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治, bbox=[83, 445, 908, 474]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[21]: text=就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二, bbox=[83, 471, 900, 500]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[22]: text=便如常，近1年体重减少4kg。, bbox=[84, 511, 300, 531]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[23]: text=既往史：, bbox=[85, 542, 148, 561]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[24]: text=患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染, bbox=[85, 558, 897, 587]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[25]: text=病；食物、药物过敏无；无外伤史：无手术史：无输血史：无中毒史：无长期用药史：无可能成瘾药物。疫, bbox=[85, 584, 905, 613]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[26]: text=苗接种史不详, bbox=[86, 620, 188, 639]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[27]: text=个人史：, bbox=[86, 648, 148, 667]
2026-08-10 11:25:41,830 INFO     29 [qwen-vl-text] coord item[28]: text=出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长, bbox=[86, 669, 896, 693]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[29]: text=地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物, bbox=[86, 695, 896, 719]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[30]: text=质接触史。, bbox=[86, 724, 164, 743]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[31]: text=婚育史：, bbox=[86, 752, 149, 771]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[32]: text=已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。, bbox=[87, 779, 584, 801]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[33]: text=月经史：, bbox=[87, 805, 151, 824]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[34]: text=初潮年龄17岁, bbox=[89, 855, 195, 875]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[35]: text=经期3-4天, bbox=[239, 845, 318, 865]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[36]: text=绝经年龄53岁 月经及白带情况：正常, bbox=[367, 857, 664, 877]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[37]: text=月经周期30天, bbox=[223, 880, 332, 900]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[38]: text=家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否, bbox=[90, 906, 904, 927]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[39]: text=认二系三代有遗传病史。患者否认有遗传倾向的疾病。, bbox=[90, 932, 502, 952]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[40]: text=体格检查, bbox=[461, 960, 534, 979]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] coord item[41]: text=生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60, bbox=[90, 984, 687, 1000]
2026-08-10 11:25:41,831 INFO     29 [qwen-vl-text] page=0 — 42/42 coords, api_time=13.9s
2026-08-10 11:25:41,832 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1012941, prompt_len=1295
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["体格检查", "生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体", "重：44kg，腰围：cm，BMI：18.8 kg/m²", "一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常", "表情：正常体位：自主体位步态：平稳配合检查：配合", "皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无", "皮疹：无紫癜：无", "1/3", "贵州醫科大學附属醫院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "入院记录", "姓名：", "床号：23-03床", "病历号", "科室：呼吸与危重医学科医生", "站", "水肿：无脱水现象：无松紧度：适中", "温度：适中出汗：无显性出汗瘢痕：无感染：无", "头颅：大小：正常畸形：无包块：无", "凹陷：无压痛：无", "眼：眼睑：无水肿结膜：无充血巩膜：无黄染", "眼球四个象限运动：左眼：正常右眼：正常", "眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆", "对光反射：左眼：灵敏右眼：灵敏", "鼻：外形：正常其他异常：无鼻旁窦压痛：无", "口：唇：无紫绀粘膜：无充血腮腺导管开口：正常", "舌：伸舌居中牙龈：无肿胀龋齿：无", "咽喉：扁桃体：正常咽：无充血声音：正常", "淋巴：淋巴结：全身浅表淋巴结未及肿大", "颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张", "气管：居中颈静脉回流征：无", "甲状腺：无肿大"]

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
2026-08-10 11:25:53,523 INFO     29 [qwen-vl-text] coord API raw response (len=1978):
[
	{"text": "体格检查", "bbox": [434, 0, 505, 18]},
	{"text": "生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体", "bbox": [84, 20, 853, 52]},
	{"text": "重：44kg，腰围：cm，BMI：18.8 kg/m²", "bbox": [84, 55, 377, 85]},
	{"text": "一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常", "bbox": [84, 80, 687, 109]},
	{"text": "表情：正常体位：自主体位步态：平稳配合检查：配合", "bbox": [173, 106, 638, 133]},
	{"text": "皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无", "bbox": [84, 132, 609, 160]},
	{"text": "皮疹：无紫癜：无", "bbox": [173, 162, 330, 184]},
	{"text": "1/3", "bbox": [468, 219, 493, 236]},
	{"text": "贵州醫科大學附属醫院", "bbox": [360, 360, 723, 400]},
	{"text": "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "bbox": [365, 407, 724, 422]},
	{"text": "入院记录", "bbox": [435, 440, 539, 467]},
	{"text": "姓名：", "bbox": [85, 471, 148, 491]},
	{"text": "床号：23-03床", "bbox": [257, 477, 376, 496]},
	{"text": "病历号", "bbox": [442, 477, 496, 496]},
	{"text": "科室：呼吸与危重医学科医生", "bbox": [655, 477, 907, 504]},
	{"text": "站", "bbox": [85, 500, 105, 518]},
	{"text": "水肿：无脱水现象：无松紧度：适中", "bbox": [185, 547, 500, 567]},
	{"text": "温度：适中出汗：无显性出汗瘢痕：无感染：无", "bbox": [185, 574, 609, 595]},
	{"text": "头颅：大小：正常畸形：无包块：无", "bbox": [88, 602, 448, 624]},
	{"text": "凹陷：无压痛：无", "bbox": [186, 632, 350, 652]},
	{"text": "眼：眼睑：无水肿结膜：无充血巩膜：无黄染", "bbox": [186, 660, 580, 681]},
	{"text": "眼球四个象限运动：左眼：正常右眼：正常", "bbox": [186, 687, 546, 708]},
	{"text": "眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆", "bbox": [90, 713, 660, 736]},
	{"text": "对光反射：左眼：灵敏右眼：灵敏", "bbox": [90, 741, 395, 763]},
	{"text": "鼻：外形：正常其他异常：无鼻旁窦压痛：无", "bbox": [195, 770, 595, 791]},
	{"text": "口：唇：无紫绀粘膜：无充血腮腺导管开口：正常", "bbox": [196, 798, 629, 820]},
	{"text": "舌：伸舌居中牙龈：无肿胀龋齿：无", "bbox": [196, 827, 519, 848]},
	{"text": "咽喉：扁桃体：正常咽：无充血声音：正常", "bbox": [91, 854, 514, 876]},
	{"text": "淋巴：淋巴结：全身浅表淋巴结未及肿大", "bbox": [91, 882, 463, 904]},
	{"text": "颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张", "bbox": [145, 911, 569, 932]},
	{"text": "气管：居中颈静脉回流征：无", "bbox": [187, 940, 443, 961]},
	{"text": "甲状腺：无肿大", "bbox": [187, 970, 322, 991]}
]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=11.7s
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[0]: text=体格检查, bbox=[434, 0, 505, 18]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[1]: text=生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体, bbox=[84, 20, 853, 52]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[2]: text=重：44kg，腰围：cm，BMI：18.8 kg/m², bbox=[84, 55, 377, 85]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[3]: text=一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常, bbox=[84, 80, 687, 109]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[4]: text=表情：正常体位：自主体位步态：平稳配合检查：配合, bbox=[173, 106, 638, 133]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[5]: text=皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无, bbox=[84, 132, 609, 160]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[6]: text=皮疹：无紫癜：无, bbox=[173, 162, 330, 184]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[7]: text=1/3, bbox=[468, 219, 493, 236]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[8]: text=贵州醫科大學附属醫院, bbox=[360, 360, 723, 400]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[9]: text=THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY, bbox=[365, 407, 724, 422]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[10]: text=入院记录, bbox=[435, 440, 539, 467]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[11]: text=姓名：, bbox=[85, 471, 148, 491]
2026-08-10 11:25:53,524 INFO     29 [qwen-vl-text] coord item[12]: text=床号：23-03床, bbox=[257, 477, 376, 496]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[13]: text=病历号, bbox=[442, 477, 496, 496]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[14]: text=科室：呼吸与危重医学科医生, bbox=[655, 477, 907, 504]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[15]: text=站, bbox=[85, 500, 105, 518]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[16]: text=水肿：无脱水现象：无松紧度：适中, bbox=[185, 547, 500, 567]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[17]: text=温度：适中出汗：无显性出汗瘢痕：无感染：无, bbox=[185, 574, 609, 595]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[18]: text=头颅：大小：正常畸形：无包块：无, bbox=[88, 602, 448, 624]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[19]: text=凹陷：无压痛：无, bbox=[186, 632, 350, 652]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[20]: text=眼：眼睑：无水肿结膜：无充血巩膜：无黄染, bbox=[186, 660, 580, 681]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[21]: text=眼球四个象限运动：左眼：正常右眼：正常, bbox=[186, 687, 546, 708]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[22]: text=眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆, bbox=[90, 713, 660, 736]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[23]: text=对光反射：左眼：灵敏右眼：灵敏, bbox=[90, 741, 395, 763]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[24]: text=鼻：外形：正常其他异常：无鼻旁窦压痛：无, bbox=[195, 770, 595, 791]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[25]: text=口：唇：无紫绀粘膜：无充血腮腺导管开口：正常, bbox=[196, 798, 629, 820]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[26]: text=舌：伸舌居中牙龈：无肿胀龋齿：无, bbox=[196, 827, 519, 848]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[27]: text=咽喉：扁桃体：正常咽：无充血声音：正常, bbox=[91, 854, 514, 876]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[28]: text=淋巴：淋巴结：全身浅表淋巴结未及肿大, bbox=[91, 882, 463, 904]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[29]: text=颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张, bbox=[145, 911, 569, 932]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[30]: text=气管：居中颈静脉回流征：无, bbox=[187, 940, 443, 961]
2026-08-10 11:25:53,525 INFO     29 [qwen-vl-text] coord item[31]: text=甲状腺：无肿大, bbox=[187, 970, 322, 991]
2026-08-10 11:25:53,526 INFO     29 [qwen-vl-text] page=1 — 32/32 coords, api_time=11.7s
2026-08-10 11:25:53,528 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=886406, prompt_len=1171
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["眼球四个象限运动：左眼：正常 右眼：正常", "眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆", "对光反射：左眼：灵敏 右眼：灵敏", "鼻：外形：正常 其他异常：无 鼻旁窦压痛：无", "口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常", "舌：伸舌居中 牙龈：无肿胀 龋齿：无", "咽 喉：扁桃体：正常 咽：无充血 声音：正常", "淋巴 巴：淋巴结：全身浅表淋巴结未及肿大", "颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张", "气管：居中 颈静脉回流征：无", "甲状腺：无肿大", "胸部 部：胸廓：无畸形 乳房：", "肺 部：视诊：呼吸运动", "触诊：", "叩诊：", "听诊：", "语音传导", "心 脏：视诊：", "触诊：心尖搏动", "叩诊：", "心界", "右(cm)", "肋间", "左(cm)", "2", "2", "2", "3", "(左锁骨中线距胸骨线7.5cm)", "听诊：心率：92次/分 心律：齐 心音：未闻及异常心", "额外心音：无 杂音：无 心包摩擦感：", "周围血管：异常血管征：无", "腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出", "其他异常：无", "触诊：腹壁：柔软 压痛：无", "2/3"]

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
2026-08-10 11:26:04,533 INFO     29 [qwen-vl-text] coord API raw response (len=2019):
[
	{"text": "眼球四个象限运动：左眼：正常 右眼：正常", "bbox": [181, 0, 538, 18]},
	{"text": "眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆", "bbox": [85, 25, 649, 45]},
	{"text": "对光反射：左眼：灵敏 右眼：灵敏", "bbox": [85, 53, 384, 73]},
	{"text": "鼻：外形：正常 其他异常：无 鼻旁窦压痛：无", "bbox": [189, 80, 582, 100]},
	{"text": "口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常", "bbox": [189, 107, 616, 127]},
	{"text": "舌：伸舌居中 牙龈：无肿胀 龋齿：无", "bbox": [189, 134, 504, 154]},
	{"text": "咽 喉：扁桃体：正常 咽：无充血 声音：正常", "bbox": [85, 162, 498, 182]},
	{"text": "淋巴 巴：淋巴结：全身浅表淋巴结未及肿大", "bbox": [85, 189, 445, 209]},
	{"text": "颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张", "bbox": [85, 216, 551, 236]},
	{"text": "气管：居中 颈静脉回流征：无", "bbox": [178, 244, 423, 264]},
	{"text": "甲状腺：无肿大", "bbox": [178, 272, 302, 292]},
	{"text": "胸部 部：胸廓：无畸形 乳房：", "bbox": [85, 300, 330, 320]},
	{"text": "肺 部：视诊：呼吸运动", "bbox": [85, 328, 298, 348]},
	{"text": "触诊：", "bbox": [180, 359, 220, 377]},
	{"text": "叩诊：", "bbox": [180, 386, 220, 404]},
	{"text": "听诊：", "bbox": [180, 413, 220, 431]},
	{"text": "语音传导", "bbox": [181, 440, 250, 459]},
	{"text": "心 脏：视诊：", "bbox": [87, 467, 220, 487]},
	{"text": "触诊：心尖搏动", "bbox": [181, 494, 300, 514]},
	{"text": "叩诊：", "bbox": [181, 521, 224, 540]},
	{"text": "心界", "bbox": [398, 550, 440, 569]},
	{"text": "右(cm)", "bbox": [186, 605, 236, 624]},
	{"text": "肋间", "bbox": [371, 605, 406, 623]},
	{"text": "左(cm)", "bbox": [567, 605, 617, 624]},
	{"text": "2", "bbox": [184, 633, 195, 652]},
	{"text": "2", "bbox": [558, 633, 569, 652]},
	{"text": "2", "bbox": [184, 661, 195, 680]},
	{"text": "3", "bbox": [184, 689, 195, 708]},
	{"text": "(左锁骨中线距胸骨线7.5cm)", "bbox": [267, 738, 482, 758]},
	{"text": "听诊：心率：92次/分 心律：齐 心音：未闻及异常心", "bbox": [166, 766, 617, 787]},
	{"text": "额外心音：无 杂音：无 心包摩擦感：", "bbox": [166, 793, 604, 814]},
	{"text": "周围血管：异常血管征：无", "bbox": [91, 822, 306, 843]},
	{"text": "腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出", "bbox": [91, 849, 549, 870]},
	{"text": "其他异常：无", "bbox": [178, 877, 282, 897]},
	{"text": "触诊：腹壁：柔软 压痛：无", "bbox": [178, 905, 416, 925]},
	{"text": "2/3", "bbox": [487, 948, 513, 965]}
]
2026-08-10 11:26:04,534 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=11.0s
2026-08-10 11:26:04,534 INFO     29 [qwen-vl-text] coord item[0]: text=眼球四个象限运动：左眼：正常 右眼：正常, bbox=[181, 0, 538, 18]
2026-08-10 11:26:04,534 INFO     29 [qwen-vl-text] coord item[1]: text=眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆, bbox=[85, 25, 649, 45]
2026-08-10 11:26:04,534 INFO     29 [qwen-vl-text] coord item[2]: text=对光反射：左眼：灵敏 右眼：灵敏, bbox=[85, 53, 384, 73]
2026-08-10 11:26:04,534 INFO     29 [qwen-vl-text] coord item[3]: text=鼻：外形：正常 其他异常：无 鼻旁窦压痛：无, bbox=[189, 80, 582, 100]
2026-08-10 11:26:04,534 INFO     29 [qwen-vl-text] coord item[4]: text=口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常, bbox=[189, 107, 616, 127]
2026-08-10 11:26:04,534 INFO     29 [qwen-vl-text] coord item[5]: text=舌：伸舌居中 牙龈：无肿胀 龋齿：无, bbox=[189, 134, 504, 154]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[6]: text=咽 喉：扁桃体：正常 咽：无充血 声音：正常, bbox=[85, 162, 498, 182]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[7]: text=淋巴 巴：淋巴结：全身浅表淋巴结未及肿大, bbox=[85, 189, 445, 209]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[8]: text=颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张, bbox=[85, 216, 551, 236]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[9]: text=气管：居中 颈静脉回流征：无, bbox=[178, 244, 423, 264]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[10]: text=甲状腺：无肿大, bbox=[178, 272, 302, 292]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[11]: text=胸部 部：胸廓：无畸形 乳房：, bbox=[85, 300, 330, 320]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[12]: text=肺 部：视诊：呼吸运动, bbox=[85, 328, 298, 348]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[13]: text=触诊：, bbox=[180, 359, 220, 377]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[14]: text=叩诊：, bbox=[180, 386, 220, 404]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[15]: text=听诊：, bbox=[180, 413, 220, 431]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[16]: text=语音传导, bbox=[181, 440, 250, 459]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[17]: text=心 脏：视诊：, bbox=[87, 467, 220, 487]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[18]: text=触诊：心尖搏动, bbox=[181, 494, 300, 514]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[19]: text=叩诊：, bbox=[181, 521, 224, 540]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[20]: text=心界, bbox=[398, 550, 440, 569]
2026-08-10 11:26:04,535 INFO     29 [qwen-vl-text] coord item[21]: text=右(cm), bbox=[186, 605, 236, 624]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[22]: text=肋间, bbox=[371, 605, 406, 623]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[23]: text=左(cm), bbox=[567, 605, 617, 624]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[24]: text=2, bbox=[184, 633, 195, 652]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[25]: text=2, bbox=[558, 633, 569, 652]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[26]: text=2, bbox=[184, 661, 195, 680]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[27]: text=3, bbox=[184, 689, 195, 708]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[28]: text=(左锁骨中线距胸骨线7.5cm), bbox=[267, 738, 482, 758]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[29]: text=听诊：心率：92次/分 心律：齐 心音：未闻及异常心, bbox=[166, 766, 617, 787]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[30]: text=额外心音：无 杂音：无 心包摩擦感：, bbox=[166, 793, 604, 814]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[31]: text=周围血管：异常血管征：无, bbox=[91, 822, 306, 843]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[32]: text=腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出, bbox=[91, 849, 549, 870]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[33]: text=其他异常：无, bbox=[178, 877, 282, 897]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[34]: text=触诊：腹壁：柔软 压痛：无, bbox=[178, 905, 416, 925]
2026-08-10 11:26:04,536 INFO     29 [qwen-vl-text] coord item[35]: text=2/3, bbox=[487, 948, 513, 965]
2026-08-10 11:26:04,537 INFO     29 [qwen-vl-text] page=2 — 36/36 coords, api_time=11.0s
2026-08-10 11:26:04,540 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=707672, prompt_len=1101
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["站", "反跳痛：无", "液波振颤：无 振水声：无", "腹部包块：无", "肝：肋下未及", "胆囊：未触及 Murphy征：阴性", "脾：未触及", "叩诊：肝浊音界：正常 移动性浊音：无", "肾区叩痛：无", "听诊：肠鸣音：正常 肠鸣音频率：4次/分", "气过水音：无 血管杂音：无", "肛门直肠：未检", "生殖器：未检", "脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限", "压痛，叩痛：无", "杵状指趾：无", "神经系统：腹壁反射：正常 肢体瘫痪：无", "肌张力：正常 肌力：V级", "肱二头肌反射：正常 Hoffman征：阴性", "膝腱反射：正常 Kernig征：阴性", "跟腱反射：正常 Babinski征：阴性", "其他：无", "补充及专科情况", "双肺呼吸音清，未闻及干湿性啰音。", "辅助检查：暂无", "VTE评估：", "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "入院诊断：1.支气管哮喘急性发作期", "医师签名：", "日期：2025-10-30 16:38"]

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
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord API raw response (len=1702):
[
	{"text": "站", "bbox": [90, 0, 108, 15]},
	{"text": "反跳痛：无", "bbox": [176, 40, 266, 59]},
	{"text": "液波振颤：无 振水声：无", "bbox": [176, 66, 383, 86]},
	{"text": "腹部包块：无", "bbox": [176, 95, 283, 114]},
	{"text": "肝：肋下未及", "bbox": [176, 122, 283, 141]},
	{"text": "胆囊：未触及 Murphy征：阴性", "bbox": [176, 148, 419, 168]},
	{"text": "脾：未触及", "bbox": [176, 176, 264, 195]},
	{"text": "叩诊：肝浊音界：正常 移动性浊音：无", "bbox": [176, 202, 491, 222]},
	{"text": "肾区叩痛：无", "bbox": [176, 232, 283, 251]},
	{"text": "听诊：肠鸣音：正常 肠鸣音频率：4次/分", "bbox": [176, 258, 517, 278]},
	{"text": "气过水音：无 血管杂音：无", "bbox": [176, 287, 419, 307]},
	{"text": "肛门直肠：未检", "bbox": [90, 318, 216, 338]},
	{"text": "生殖器：未检", "bbox": [90, 346, 216, 366]},
	{"text": "脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限", "bbox": [90, 369, 505, 393]},
	{"text": "压痛，叩痛：无", "bbox": [183, 399, 308, 418]},
	{"text": "杵状指趾：无", "bbox": [90, 427, 199, 448]},
	{"text": "神经系统：腹壁反射：正常 肢体瘫痪：无", "bbox": [90, 453, 440, 474]},
	{"text": "肌张力：正常 肌力：V级", "bbox": [183, 480, 423, 500]},
	{"text": "肱二头肌反射：正常 Hoffman征：阴性", "bbox": [183, 507, 487, 527]},
	{"text": "膝腱反射：正常 Kernig征：阴性", "bbox": [183, 534, 441, 554]},
	{"text": "跟腱反射：正常 Babinski征：阴性", "bbox": [183, 561, 450, 581]},
	{"text": "其他：无", "bbox": [89, 590, 195, 612]},
	{"text": "补充及专科情况", "bbox": [431, 643, 565, 663]},
	{"text": "双肺呼吸音清，未闻及干湿性啰音。", "bbox": [120, 672, 395, 692]},
	{"text": "辅助检查：暂无", "bbox": [86, 703, 214, 722]},
	{"text": "VTE评估：", "bbox": [86, 758, 158, 777]},
	{"text": "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "bbox": [86, 777, 698, 801]},
	{"text": "入院诊断：1.支气管哮喘急性发作期", "bbox": [86, 837, 364, 859]},
	{"text": "医师签名：", "bbox": [700, 927, 780, 949]},
	{"text": "日期：2025-10-30 16:38", "bbox": [721, 971, 920, 990]}
]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=10.3s
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[0]: text=站, bbox=[90, 0, 108, 15]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[1]: text=反跳痛：无, bbox=[176, 40, 266, 59]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[2]: text=液波振颤：无 振水声：无, bbox=[176, 66, 383, 86]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[3]: text=腹部包块：无, bbox=[176, 95, 283, 114]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[4]: text=肝：肋下未及, bbox=[176, 122, 283, 141]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[5]: text=胆囊：未触及 Murphy征：阴性, bbox=[176, 148, 419, 168]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[6]: text=脾：未触及, bbox=[176, 176, 264, 195]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[7]: text=叩诊：肝浊音界：正常 移动性浊音：无, bbox=[176, 202, 491, 222]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[8]: text=肾区叩痛：无, bbox=[176, 232, 283, 251]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[9]: text=听诊：肠鸣音：正常 肠鸣音频率：4次/分, bbox=[176, 258, 517, 278]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[10]: text=气过水音：无 血管杂音：无, bbox=[176, 287, 419, 307]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[11]: text=肛门直肠：未检, bbox=[90, 318, 216, 338]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[12]: text=生殖器：未检, bbox=[90, 346, 216, 366]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[13]: text=脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限, bbox=[90, 369, 505, 393]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[14]: text=压痛，叩痛：无, bbox=[183, 399, 308, 418]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[15]: text=杵状指趾：无, bbox=[90, 427, 199, 448]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[16]: text=神经系统：腹壁反射：正常 肢体瘫痪：无, bbox=[90, 453, 440, 474]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[17]: text=肌张力：正常 肌力：V级, bbox=[183, 480, 423, 500]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[18]: text=肱二头肌反射：正常 Hoffman征：阴性, bbox=[183, 507, 487, 527]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[19]: text=膝腱反射：正常 Kernig征：阴性, bbox=[183, 534, 441, 554]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[20]: text=跟腱反射：正常 Babinski征：阴性, bbox=[183, 561, 450, 581]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[21]: text=其他：无, bbox=[89, 590, 195, 612]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[22]: text=补充及专科情况, bbox=[431, 643, 565, 663]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[23]: text=双肺呼吸音清，未闻及干湿性啰音。, bbox=[120, 672, 395, 692]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[24]: text=辅助检查：暂无, bbox=[86, 703, 214, 722]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[25]: text=VTE评估：, bbox=[86, 758, 158, 777]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[26]: text=Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：, bbox=[86, 777, 698, 801]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[27]: text=入院诊断：1.支气管哮喘急性发作期, bbox=[86, 837, 364, 859]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[28]: text=医师签名：, bbox=[700, 927, 780, 949]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] coord item[29]: text=日期：2025-10-30 16:38, bbox=[721, 971, 920, 990]
2026-08-10 11:26:14,807 INFO     29 [qwen-vl-text] page=3 — 30/30 coords, api_time=10.3s
2026-08-10 11:26:14,808 INFO     29 [qwen-vl-text] new_positions (140):
[[0, 260.1, 329.256, 0.0, 15.038255859374999], [0, 47.124, 72.216, 23.183977783203126, 35.089263671875], [0, 146.88, 219.708, 23.183977783203126, 35.089263671875], [0, 264.384, 318.24, 21.930789794921875, 33.20948168945313], [0, 400.86, 547.74, 21.30419580078125, 31.956293701171877], [0, 47.124, 57.528, 40.102015625, 51.38070751953125], [0, 53.856, 98.532, 89.60294116210937, 101.50822705078124], [0, 279.072, 358.02, 85.84337719726562, 97.7486630859375], [0, 53.856, 133.416, 112.7869189453125, 125.318798828125], [0, 279.072, 413.712, 108.40076098632812, 120.93264086914063], [0, 53.856, 156.06, 137.8506787109375, 150.38255859375], [0, 280.296, 369.64799999999997, 132.21133276367186, 144.74321264648438], [0, 53.856, 135.864, 161.66125048828124, 174.19313037109376], [0, 280.908, 434.52, 154.76871655273436, 167.30059643554688], [0, 55.08, 203.796, 201.13667211914063, 213.0419580078125], [0, 281.52, 369.64799999999997, 194.24413818359375, 207.4026120605469], [0, 50.796, 203.184, 221.18767993164062, 233.0929658203125], [0, 50.796, 541.62, 229.95999584960938, 248.75781567382813], [0, 50.796, 550.8, 246.25143969726562, 264.4226655273437], [0, 50.796, 550.8, 262.5428835449219, 280.714109375], [0, 50.796, 555.696, 278.83432739257813, 297.00555322265626], [0, 50.796, 550.8, 295.12577124023437, 313.2969970703125], [0, 51.408, 183.6, 320.18953100585935, 332.72141088867187], [0, 52.019999999999996, 90.576, 339.6139448242188, 351.51923071289065], [0, 52.019999999999996, 548.9639999999999, 349.63944873046876, 367.8106745605469], [0, 52.019999999999996, 553.86, 365.930892578125, 384.1021184082031], [0, 52.632, 115.056, 388.4882763671875, 400.39356225585936], [0, 52.632, 90.576, 406.032908203125, 417.9381940917969], [0, 52.632, 548.352, 419.19138208007814, 434.22963793945314], [0, 52.632, 548.352, 435.4828259277344, 450.5210817871094], [0, 52.632, 100.368, 453.6540517578125, 465.5593376464844], [0, 52.632, 91.188, 471.19868359375, 483.10396948242186], [0, 53.244, 357.408, 488.1167214355469, 501.90178930664064], [0, 53.244, 92.41199999999999, 504.4081652832031, 516.313451171875], [0, 54.467999999999996, 119.34, 535.7378649902344, 548.2697448730469], [0, 146.268, 194.61599999999999, 529.4719250488281, 542.0038049316406], [0, 224.60399999999998, 406.368, 536.9910529785157, 549.5229328613282], [0, 136.476, 203.184, 551.40271484375, 563.9345947265625], [0, 55.08, 553.2479999999999, 567.6941586914063, 580.8526325683594], [0, 55.08, 307.224, 583.9856025390625, 596.517482421875], [0, 282.132, 326.808, 601.530234375, 613.4355202636718], [0, 55.08, 420.444, 616.568490234375, 626.593994140625], [1, 265.608, 309.06, 0.0, 11.161241455078123], [1, 51.408, 522.036, 12.401379394531249, 32.243586425781245], [1, 51.408, 230.724, 34.10379333496093, 52.70586242675781], [1, 51.408, 420.444, 49.605517578124996, 67.5875177001953], [1, 105.876, 390.456, 65.72731079101563, 82.46917297363281], [1, 51.408, 372.70799999999997, 81.84910400390625, 99.21103515624999], [1, 105.876, 201.96, 100.45117309570311, 114.0926904296875], [1, 286.416, 301.716, 135.79510437011717, 146.33627685546872], [1, 220.32, 442.476, 223.22482910156248, 248.02758789062497], [1, 223.38, 443.08799999999997, 252.36807067871092, 261.6691052246093], [1, 266.21999999999997, 329.868, 272.83034667968747, 289.57220886230465], [1, 52.019999999999996, 90.576, 292.0524847412109, 304.45386413574215], [1, 157.284, 230.112, 295.7728985595703, 307.55420898437495], [1, 270.504, 303.552, 295.7728985595703, 307.55420898437495], [1, 400.86, 555.084, 295.7728985595703, 312.5147607421875], [1, 52.019999999999996, 64.26, 310.03448486328125, 321.19572631835933], [1, 113.22, 306.0, 339.17772644042964, 351.5791058349609], [1, 113.22, 372.70799999999997, 355.9195886230468, 368.94103698730464], [1, 53.856, 274.176, 373.2815197753906, 386.92303710937495], [1, 113.832, 214.2, 391.8835888671875, 404.2849682617187], [1, 113.832, 354.96, 409.2455200195312, 422.26696838378905], [1, 113.832, 334.152, 425.9873822021484, 439.00883056640623], [1, 55.08, 403.92, 442.10917541503903, 456.37076171875], [1, 55.08, 241.74, 459.4711065673828, 473.11262390136716], [1, 119.34, 364.14, 477.4531066894531, 490.4745550537109], [1, 119.952, 384.948, 494.8150378417968, 508.4565551757812], [1, 119.952, 317.628, 512.7970379638672, 525.818486328125], [1, 55.692, 314.568, 529.5389001464844, 543.1804174804687], [1, 55.692, 283.356, 546.900831298828, 560.5423486328125], [1, 88.74, 348.228, 564.8828314208984, 577.9042797851562], [1, 114.444, 271.116, 582.8648315429687, 595.8862799072265], [1, 114.444, 197.064, 601.4669006347656, 614.4883489990234], [2, 110.77199999999999, 329.256, 0.0, 11.1318486328125], [2, 52.019999999999996, 397.188, 15.46090087890625, 27.82962158203125], [2, 52.019999999999996, 235.00799999999998, 32.777109863281254, 45.145830566406254], [2, 115.66799999999999, 356.18399999999997, 49.4748828125, 61.843603515625], [2, 115.66799999999999, 376.992, 66.17265576171874, 78.54137646484375], [2, 115.66799999999999, 308.448, 82.8704287109375, 95.2391494140625], [2, 52.019999999999996, 304.776, 100.1866376953125, 112.5553583984375], [2, 52.019999999999996, 272.34, 116.88441064453126, 129.25313134765625], [2, 52.019999999999996, 337.212, 133.58218359375, 145.950904296875], [2, 108.93599999999999, 258.876, 150.898392578125, 163.26711328125], [2, 108.93599999999999, 184.82399999999998, 168.2146015625, 180.58332226562501], [2, 52.019999999999996, 201.96, 185.530810546875, 197.89953125], [2, 52.019999999999996, 182.376, 202.84701953125, 215.215740234375], [2, 110.16, 134.64, 222.01853662109374, 233.15038525390625], [2, 110.16, 134.64, 238.7163095703125, 249.848158203125], [2, 110.16, 134.64, 255.41408251953126, 266.54593115234377], [2, 110.77199999999999, 153.0, 272.11185546875, 283.8621401367188], [2, 53.244, 134.64, 288.8096284179688, 301.17834912109373], [2, 110.77199999999999, 183.6, 305.5074013671875, 317.8761220703125], [2, 110.77199999999999, 137.088, 322.20517431640627, 333.955458984375], [2, 243.576, 269.28, 340.1398193359375, 351.89010400390623], [2, 113.832, 144.432, 374.15380126953124, 385.9040859375], [2, 227.052, 248.472, 374.15380126953124, 385.2856499023438], [2, 347.004, 377.604, 374.15380126953124, 385.9040859375], [2, 112.608, 119.34, 391.47001025390625, 403.220294921875], [2, 341.496, 348.228, 391.47001025390625, 403.220294921875], [2, 112.608, 119.34, 408.78621923828126, 420.53650390625], [2, 112.608, 119.34, 426.1024282226563, 437.852712890625], [2, 163.404, 294.984, 456.4057939453125, 468.7745146484375], [2, 101.592, 377.604, 473.7220029296875, 486.7091596679688], [2, 101.592, 369.64799999999997, 490.41977587890625, 503.4069326171875], [2, 55.692, 187.272, 508.3544208984375, 521.3415776367187], [2, 55.692, 335.988, 525.0521938476562, 538.0393505859375], [2, 108.93599999999999, 172.584, 542.3684028320313, 554.7371235351562], [2, 108.93599999999999, 254.59199999999998, 559.6846118164062, 572.0533325195313], [2, 298.044, 313.956, 586.277361328125, 596.7907739257813], [3, 55.08, 66.096, 0.0, 9.419760131835936], [3, 107.712, 162.792, 25.1193603515625, 37.05105651855469], [3, 107.712, 234.396, 41.446944580078124, 54.00662475585937], [3, 107.712, 173.196, 59.65848083496093, 71.59017700195312], [3, 107.712, 173.196, 76.61404907226562, 88.54574523925781], [3, 107.712, 256.428, 92.94163330078125, 105.5013134765625], [3, 107.712, 161.56799999999998, 110.525185546875, 122.45688171386718], [3, 107.712, 300.492, 126.85276977539061, 139.41244995117188], [3, 107.712, 173.196, 145.6922900390625, 157.62398620605467], [3, 107.712, 316.404, 162.0198742675781, 174.57955444335937], [3, 107.712, 256.428, 180.23141052246092, 192.7910906982422], [3, 55.08, 132.192, 199.69891479492188, 212.25859497070311], [3, 55.08, 132.192, 217.28246704101562, 229.84214721679686], [3, 55.08, 309.06, 231.72609924316404, 246.79771545410154], [3, 111.996, 188.496, 250.56561950683593, 262.4973156738281], [3, 55.08, 121.788, 268.14917175292965, 281.3368359375], [3, 55.08, 269.28, 284.4767559814453, 297.6644201660156], [3, 111.996, 258.876, 301.43232421874995, 313.99200439453125], [3, 111.996, 298.044, 318.38789245605466, 330.9475726318359], [3, 111.996, 269.892, 335.34346069335936, 347.9031408691406], [3, 111.996, 275.4, 352.29902893066406, 364.8587091064453], [3, 54.467999999999996, 119.34, 370.51056518554685, 384.32621337890623], [3, 263.772, 345.78, 403.79371765136716, 416.3533978271484], [3, 73.44, 241.74, 422.00525390625, 434.56493408203124], [3, 52.632, 130.968, 441.47275817871093, 453.4044543457031], [3, 52.632, 96.696, 476.0118786621093, 487.9435748291015], [3, 52.632, 427.176, 487.9435748291015, 503.01519104003904], [3, 52.632, 222.768, 525.6226153564453, 539.4382635498047], [3, 428.4, 477.36, 582.1411761474609, 595.9568243408203], [3, 441.252, 563.04, 609.7724725341797, 621.7041687011719]]
2026-08-10 11:26:14,808 INFO     29 [qwen-vl-text] ═══ DONE ═══ 140 positions, pages=4, time=59.7s
2026-08-10 11:26:14,821 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:26:14,821 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:26:14,821 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:26:14,822 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:26:14.821+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 21, "failed": 0, "current": {"ba5d751a94ad11f1bd9827cf206dfa2d": {"id": "ba5d751a94ad11f1bd9827cf206dfa2d", "doc_id": "b9a7e47a94ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360930217, "task_type": "dataflow", "root_trace_id": "2d4fcd13324b447999508dc50afac2e4", "root_traceparent": "00-2d4fcd13324b447999508dc50afac2e4-817dc24fdd0315e5-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:26:14,832 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:26:14,833 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:26:14,834 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:26:14,834 INFO     29 [qwen-vl-text] positions(341): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:26:14,834 INFO     29 [qwen-vl-text] page grouping: [7, 8], lines per page: [172, 169]
2026-08-10 11:26:15,125 INFO     29 [qwen-vl-text] page=7, rect=612x832, img=(1700x2312), dpi=200
2026-08-10 11:26:15,408 INFO     29 [qwen-vl-text] page=8, rect=612x818, img=(1700x2273), dpi=200
2026-08-10 11:26:15,412 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2017
2026-08-10 11:26:15,412 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:26:15,412 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 243, \"bbox_end\": 583, \"encounter_dates\": [\"2025-10-31\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能通气阻力检查报告\n姓名：\n性别：女\n身高：151 cm\n病历号：\n年龄：72 Years\n体重：46 kg\nFlow [L/s]\nF/V ex\n10\n5\n0\n2\n4\n6\nF/V in\n8\nVol [L]\n6\n4\n1\nVol%Vcmax\n100\nVcmax\n20\n0\nTime [s]\n0\n1\n2\n3\n4\n5\n6\n2.0\nR [kPa/(L/s)] Normal breathingX [kPa/(L/s)]\n1.5\n1.0\n0.5\n0.0\n0.4\n0.2\n0.2\n0.4\nF [Hz]\n5\n10\n15\n20\n25\n30\n35\n日期\n时间\n预计值\n实测值\n实/预\n25/10/31\n14:29:33\nMV\n[L/min]\n6.57\n11.52\n175.3\nVT\n[L]\n0.33\n0.79\n239.6\nBF\n[1/min]\n20.00\n14.63\n73.1\nVC MAX\n[L]\n2.03\n1.48\n73.0\nERV\n[L]\n0.57\n0.14\n25.5\nIC\n[L]\n1.46\n1.34\n91.6\nFVC\n[L]\n1.93\n1.44\n74.8\nFEV 1\n[L]\n1.56\n0.91\n58.4\nFEV 1 % FVC\n[%]\n63.38\nFEV 1 % VC MAX\n[%]\n75.42\n61.67\n81.8\nPEF\n[L/s]\n5.04\n2.51\n49.8\nMEF 75\n[L/s]\n4.66\n1.54\n33.1\nMEF 50\n[L/s]\n3.06\n0.56\n18.2\nMEF 25\n[L/s]\n0.90\n0.22\n24.6\nMEF 75/25\n[L/s]\n2.36\n0.50\n21.1\nFET\n[s]\n4.91\nLFV\n[L/min]\n73.10\nZ at 5 Hz\n[kPa/(L/s)]\n0.43\n0.58\n135.7\nResonant frequency\n[1/s]\n30.00\nR at 5 Hz\n[kPa/(L/s)]\n0.41\n0.57\n137.2\nR nt 20 Hz\n[kPa/(L/s)]\n0.35\n0.34\n95.3\nX at 5 Hz\n[kPa/(L/s)]\n-0.11\n-0.12\n112.5\nRcentral\n[kPa/(L/s)]\n0.12\nPeripheral\n[kPa/(L/s)]\n0.40\n结论：\n1.中重度混合性肺通气功能障碍\n2.（阻力增加\n审核者专用章\n检查者：王美锦\n贵州医科大学附属医院\nTHE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n对比试验\n姓名：\n性别：女\n身高：151 cm\n病历号：\n年龄：72 Years\n体重：46 kg\nFlow [L/s]\nF/V ex\n10\n5\n0\n2\n3\n4\n5\n6\n7\nF/V in\n6\nVol [L]\n4\nTLC\nER,pleth2\nRV\nTime [min]\nPred Act 0.0\n0.2\n0.4\n0.6\n0.8\n1.0\n日期\n时间\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n25/10/31\n14:29:33\n25/10/31\n14:53:10\nVT\n[L]\n0.33\n0.79\n239.6\nBF\n[1/min]\n20.00\n14.63\n73.1\nMV\n[L/min]\n6.57\n11.52\n175.3\nVC MAX\n[L]\n2.03\n1.48\n73.0\n1.66\n81.9\n12.2\nERV\n[L]\n0.57\n0.14\n25.5\nIC\n[L]\n1.46\n1.34\n91.6\nFVC\n[L]\n1.93\n1.44\n74.8\n1.66\n86.2\n15.3\nFEV 1\n[L]\n1.56\n0.91\n58.4\n1.08\n68.8\n17.8\nFEV 1 % FVC\n[%]\n63.38\n64.76\n2.2\nFEV 1 % VC MAX\n[%]\n75.42\n61.67\n81.8\n64.76\n85.9\n5.0\nPEF\n[L/s]\n5.04\n2.51\n49.8\n3.35\n66.5\n33.6\nMEF 75\n[L/s]\n4.66\n1.54\n33.1\n1.72\n36.8\n11.3\nMEF 50\n[L/s]\n3.06\n0.56\n18.2\n0.83\n27.1\n49.1\nMEF 25\n[L/s]\n0.90\n0.22\n24.6\n0.36\n39.8\n62.1\nMMEF 75/25\n[L/s]\n2.36\n0.50\n21.1\n0.47\n20.0\n-4.9\nFET\n[s]\n4.91\n4.88\n-0.6\nV backextrapol. % FVC\n[%]\n3.85\n4.39\n13.9\nMVV\n[L/min]\n73.10\n结论：\n1.中重度混合性肺通气功能障碍\n2.气道阻力增加\n3.支气管舒张试验阳性 (+)\n吸入沙丁胺醇400μg\nFVC上升15.3%，增加220ml；\n审核者：\n检查者：",
    "role": "user"
  }
]
2026-08-10 11:26:28,742 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:26:28,742 INFO     29 [qwen-vl-text] LLM output (len=2257):
{
  "exam_date": "2025-10-31",
  "report_date": "2025-10-31",
  "exam_name": "肺功能通气阻力检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "贵州医科大学附属医院",
  "bed_number": null,
  "findings": "日期: 25/10/31\n时间: 14:29:33\n预计值 | 实测值 | 实/预\n---|---|---\nMV [L/min] | 6.57 | 11.52 | 175.3\nVT [L] | 0.33 | 0.79 | 239.6\nBF [1/min] | 20.00 | 14.63 | 73.1\nVC MAX [L] | 2.03 | 1.48 | 73.0\nERV [L] | 0.57 | 0.14 | 25.5\nIC [L] | 1.46 | 1.34 | 91.6\nFVC [L] | 1.93 | 1.44 | 74.8\nFEV 1 [L] | 1.56 | 0.91 | 58.4\nFEV 1 % FVC [%] | 63.38 | \nFEV 1 % VC MAX [%] | 75.42 | 61.67 | 81.8\nPEF [L/s] | 5.04 | 2.51 | 49.8\nMEF 75 [L/s] | 4.66 | 1.54 | 33.1\nMEF 50 [L/s] | 3.06 | 0.56 | 18.2\nMEF 25 [L/s] | 0.90 | 0.22 | 24.6\nMEF 75/25 [L/s] | 2.36 | 0.50 | 21.1\nFET [s] | 4.91 | \nLFV [L/min] | 73.10 | \nZ at 5 Hz [kPa/(L/s)] | 0.43 | 0.58 | 135.7\nResonant frequency [1/s] | 30.00 | \nR at 5 Hz [kPa/(L/s)] | 0.41 | 0.57 | 137.2\nR nt 20 Hz [kPa/(L/s)] | 0.35 | 0.34 | 95.3\nX at 5 Hz [kPa/(L/s)] | -0.11 | -0.12 | 112.5\nRcentral [kPa/(L/s)] | 0.12 | \nPeripheral [kPa/(L/s)] | 0.40 | \n\n对比试验\n日期: 25/10/31\n时间: 14:29:33 (前次), 14:53:10 (后次)\n预计值 | 前次 | 前/预 | 后次 | 后/预 | 改善率\n---|---|---|---|---|---\nVT [L] | 0.33 | 0.79 | 239.6 | | | \nBF [1/min] | 20.00 | 14.63 | 73.1 | | | \nMV [L/min] | 6.57 | 11.52 | 175.3 | | | \nVC MAX [L] | 2.03 | 1.48 | 73.0 | 1.66 | 81.9 | 12.2\nERV [L] | 0.57 | 0.14 | 25.5 | | | \nIC [L] | 1.46 | 1.34 | 91.6 | | | \nFVC [L] | 1.93 | 1.44 | 74.8 | 1.66 | 86.2 | 15.3\nFEV 1 [L] | 1.56 | 0.91 | 58.4 | 1.08 | 68.8 | 17.8\nFEV 1 % FVC [%] | 63.38 | | | 64.76 | | 2.2\nFEV 1 % VC MAX [%] | 75.42 | 61.67 | 81.8 | 64.76 | 85.9 | 5.0\nPEF [L/s] | 5.04 | 2.51 | 49.8 | 3.35 | 66.5 | 33.6\nMEF 75 [L/s] | 4.66 | 1.54 | 33.1 | 1.72 | 36.8 | 11.3\nMEF 50 [L/s] | 3.06 | 0.56 | 18.2 | 0.83 | 27.1 | 49.1\nMEF 25 [L/s] | 0.90 | 0.22 | 24.6 | 0.36 | 39.8 | 62.1\nMMEF 75/25 [L/s] | 2.36 | 0.50 | 21.1 | 0.47 | 20.0 | -4.9\nFET [s] | 4.91 | | | 4.88 | | -0.6\nV backextrapol. % FVC [%] | 3.85 | | | 4.39 | | 13.9\nMVV [L/min] | 73.10 | | | | | ",
  "conclusion": "1.中重度混合性肺通气功能障碍\n2.气道阻力增加\n3.支气管舒张试验阳性 (+)\n吸入沙丁胺醇400μg\nFVC上升15.3%，增加220ml；",
  "physician": "王美锦",
  "reviewer": null
}
2026-08-10 11:26:28,744 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1024867, prompt_len=2140
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共172行）
["肺功能通气阻力检查报告", "姓名：", "性别：女", "身高：151 cm", "病历号：", "年龄：72 Years", "体重：46 kg", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "F/V in", "8", "Vol [L]", "6", "4", "1", "Vol%Vcmax", "100", "Vcmax", "20", "0", "Time [s]", "0", "1", "2", "3", "4", "5", "6", "2.0", "R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]", "1.5", "1.0", "0.5", "0.0", "0.4", "0.2", "0.2", "0.4", "F [Hz]", "5", "10", "15", "20", "25", "30", "35", "日期", "时间", "预计值", "实测值", "实/预", "25/10/31", "14:29:33", "MV", "[L/min]", "6.57", "11.52", "175.3", "VT", "[L]", "0.33", "0.79", "239.6", "BF", "[1/min]", "20.00", "14.63", "73.1", "VC MAX", "[L]", "2.03", "1.48", "73.0", "ERV", "[L]", "0.57", "0.14", "25.5", "IC", "[L]", "1.46", "1.34", "91.6", "FVC", "[L]", "1.93", "1.44", "74.8", "FEV 1", "[L]", "1.56", "0.91", "58.4", "FEV 1 % FVC", "[%]", "63.38", "FEV 1 % VC MAX", "[%]", "75.42", "61.67", "81.8", "PEF", "[L/s]", "5.04", "2.51", "49.8", "MEF 75", "[L/s]", "4.66", "1.54", "33.1", "MEF 50", "[L/s]", "3.06", "0.56", "18.2", "MEF 25", "[L/s]", "0.90", "0.22", "24.6", "MEF 75/25", "[L/s]", "2.36", "0.50", "21.1", "FET", "[s]", "4.91", "LFV", "[L/min]", "73.10", "Z at 5 Hz", "[kPa/(L/s)]", "0.43", "0.58", "135.7", "Resonant frequency", "[1/s]", "30.00", "R at 5 Hz", "[kPa/(L/s)]", "0.41", "0.57", "137.2", "R nt 20 Hz", "[kPa/(L/s)]", "0.35", "0.34", "95.3", "X at 5 Hz", "[kPa/(L/s)]", "-0.11", "-0.12", "112.5", "Rcentral", "[kPa/(L/s)]", "0.12", "Peripheral", "[kPa/(L/s)]", "0.40", "结论：", "1.中重度混合性肺通气功能障碍", "2.（阻力增加", "审核者专用章", "检查者：王美锦"]

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
2026-08-10 11:27:12,355 INFO     29 [qwen-vl-text] coord API raw response (len=8672):
[
	{"text": "肺功能通气阻力检查报告", "bbox": [375, 88, 634, 107]},
	{"text": "姓名：", "bbox": [154, 112, 202, 125]},
	{"text": "性别：女", "bbox": [154, 125, 347, 138]},
	{"text": "身高：151 cm", "bbox": [154, 138, 387, 149]},
	{"text": "病历号：", "bbox": [505, 110, 570, 123]},
	{"text": "年龄：72 Years", "bbox": [678, 121, 754, 133]},
	{"text": "体重：46 kg", "bbox": [678, 134, 725, 146]},
	{"text": "Flow [L/s]", "bbox": [120, 165, 172, 175]},
	{"text": "F/V ex", "bbox": [257, 165, 291, 173]},
	{"text": "10", "bbox": [102, 178, 114, 187]},
	{"text": "5", "bbox": [107, 199, 114, 208]},
	{"text": "0", "bbox": [107, 220, 114, 229]},
	{"text": "2", "bbox": [173, 230, 181, 238]},
	{"text": "4", "bbox": [230, 230, 239, 238]},
	{"text": "6", "bbox": [290, 230, 298, 238]},
	{"text": "F/V in", "bbox": [259, 274, 290, 283]},
	{"text": "8", "bbox": [407, 168, 415, 176]},
	{"text": "Vol [L]", "bbox": [422, 170, 457, 181]},
	{"text": "6", "bbox": [407, 193, 415, 201]},
	{"text": "4", "bbox": [407, 220, 415, 228]},
	{"text": "1", "bbox": [624, 218, 633, 227]},
	{"text": "Vol%Vcmax", "bbox": [375, 243, 438, 252]},
	{"text": "100", "bbox": [380, 254, 400, 264]},
	{"text": "Vcmax", "bbox": [435, 257, 472, 266]},
	{"text": "20", "bbox": [385, 266, 398, 275]},
	{"text": "0", "bbox": [407, 272, 415, 280]},
	{"text": "Time [s]", "bbox": [505, 262, 546, 272]},
	{"text": "0", "bbox": [417, 283, 425, 291]},
	{"text": "1", "bbox": [453, 283, 460, 291]},
	{"text": "2", "bbox": [487, 283, 495, 291]},
	{"text": "3", "bbox": [521, 283, 528, 291]},
	{"text": "4", "bbox": [555, 283, 562, 291]},
	{"text": "5", "bbox": [590, 283, 597, 291]},
	{"text": "6", "bbox": [624, 283, 632, 291]},
	{"text": "2.0", "bbox": [654, 161, 672, 169]},
	{"text": "R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]", "bbox": [678, 163, 887, 174]},
	{"text": "1.5", "bbox": [654, 187, 672, 195]},
	{"text": "1.0", "bbox": [654, 215, 672, 223]},
	{"text": "0.5", "bbox": [654, 243, 672, 251]},
	{"text": "0.0", "bbox": [654, 271, 672, 279]},
	{"text": "0.4", "bbox": [892, 170, 909, 178]},
	{"text": "0.2", "bbox": [892, 193, 909, 201]},
	{"text": "R", "bbox": [892, 215, 908, 223]},
	{"text": "X", "bbox": [892, 226, 908, 234]},
	{"text": "0.2", "bbox": [892, 239, 909, 247]},
	{"text": "0.4", "bbox": [892, 260, 909, 268]},
	{"text": "F [Hz]", "bbox": [767, 261, 797, 271]},
	{"text": "5", "bbox": [674, 281, 681, 289]},
	{"text": "10", "bbox": [706, 281, 718, 289]},
	{"text": "15", "bbox": [740, 281, 751, 289]},
	{"text": "20", "bbox": [773, 281, 785, 289]},
	{"text": "25", "bbox": [810, 281, 823, 289]},
	{"text": "30", "bbox": [838, 281, 850, 289]},
	{"text": "35", "bbox": [873, 281, 885, 289]},
	{"text": "日期", "bbox": [105, 308, 142, 321]},
	{"text": "时间", "bbox": [105, 321, 142, 334]},
	{"text": "预计值", "bbox": [389, 296, 447, 309]},
	{"text": "实测值", "bbox": [483, 296, 541, 309]},
	{"text": "实/预", "bbox": [586, 295, 634, 308]},
	{"text": "25/10/31", "bbox": [466, 310, 540, 321]},
	{"text": "14:29:33", "bbox": [457, 323, 542, 335]},
	{"text": "MV", "bbox": [105, 349, 127, 358]},
	{"text": "[L/min]", "bbox": [287, 350, 350, 362]},
	{"text": "6.57", "bbox": [410, 351, 447, 361]},
	{"text": "11.52", "bbox": [495, 350, 541, 361]},
	{"text": "175.3", "bbox": [588, 349, 634, 359]},
	{"text": "VT", "bbox": [105, 362, 127, 371]},
	{"text": "[L]", "bbox": [326, 363, 350, 374]},
	{"text": "0.33", "bbox": [410, 364, 447, 374]},
	{"text": "0.79", "bbox": [503, 363, 541, 374]},
	{"text": "239.6", "bbox": [588, 362, 634, 373]},
	{"text": "BF", "bbox": [105, 375, 127, 384]},
	{"text": "[1/min]", "bbox": [287, 376, 350, 387]},
	{"text": "20.00", "bbox": [400, 376, 447, 387]},
	{"text": "14.63", "bbox": [495, 376, 541, 387]},
	{"text": "73.1", "bbox": [597, 375, 634, 385]},
	{"text": "VC MAX", "bbox": [105, 388, 165, 397]},
	{"text": "[L]", "bbox": [326, 389, 350, 400]},
	{"text": "2.03", "bbox": [410, 389, 447, 400]},
	{"text": "1.48", "bbox": [503, 389, 541, 400]},
	{"text": "73.0", "bbox": [597, 388, 634, 398]},
	{"text": "ERV", "bbox": [105, 400, 137, 410]},
	{"text": "[L]", "bbox": [326, 401, 350, 412]},
	{"text": "0.57", "bbox": [410, 401, 447, 412]},
	{"text": "0.14", "bbox": [503, 401, 541, 412]},
	{"text": "25.5", "bbox": [597, 400, 634, 410]},
	{"text": "IC", "bbox": [105, 413, 127, 422]},
	{"text": "[L]", "bbox": [326, 414, 350, 425]},
	{"text": "1.46", "bbox": [410, 414, 447, 425]},
	{"text": "1.34", "bbox": [503, 414, 541, 425]},
	{"text": "91.6", "bbox": [597, 413, 634, 423]},
	{"text": "FVC", "bbox": [105, 425, 137, 435]},
	{"text": "[L]", "bbox": [326, 426, 350, 437]},
	{"text": "1.93", "bbox": [410, 426, 447, 437]},
	{"text": "1.44", "bbox": [503, 426, 541, 437]},
	{"text": "74.8", "bbox": [597, 425, 634, 435]},
	{"text": "FEV 1", "bbox": [105, 438, 154, 448]},
	{"text": "[L]", "bbox": [326, 439, 350, 450]},
	{"text": "1.56", "bbox": [410, 439, 447, 450]},
	{"text": "0.91", "bbox": [503, 439, 541, 450]},
	{"text": "58.4", "bbox": [597, 438, 634, 448]},
	{"text": "FEV 1 % FVC", "bbox": [105, 451, 212, 461]},
	{"text": "[%]", "bbox": [326, 452, 350, 463]},
	{"text": "63.38", "bbox": [495, 451, 541, 461]},
	{"text": "FEV 1 % VC MAX", "bbox": [105, 463, 240, 473]},
	{"text": "[%]", "bbox": [326, 464, 350, 475]},
	{"text": "75.42", "bbox": [400, 464, 447, 475]},
	{"text": "61.67", "bbox": [495, 464, 541, 475]},
	{"text": "81.8", "bbox": [597, 463, 634, 473]},
	{"text": "PEF", "bbox": [105, 476, 137, 485]},
	{"text": "[L/s]", "bbox": [307, 477, 350, 488]},
	{"text": "5.04", "bbox": [410, 477, 447, 488]},
	{"text": "2.51", "bbox": [503, 477, 541, 488]},
	{"text": "49.8", "bbox": [597, 476, 634, 486]},
	{"text": "MEF 75", "bbox": [105, 488, 165, 498]},
	{"text": "[L/s]", "bbox": [307, 489, 350, 500]},
	{"text": "4.66", "bbox": [410, 489, 447, 500]},
	{"text": "1.54", "bbox": [503, 489, 541, 500]},
	{"text": "33.1", "bbox": [597, 488, 634, 498]},
	{"text": "MEF 50", "bbox": [105, 501, 165, 510]},
	{"text": "[L/s]", "bbox": [307, 502, 350, 513]},
	{"text": "3.06", "bbox": [410, 502, 447, 513]},
	{"text": "0.56", "bbox": [503, 502, 541, 513]},
	{"text": "18.2", "bbox": [597, 501, 634, 511]},
	{"text": "MEF 25", "bbox": [105, 513, 165, 523]},
	{"text": "[L/s]", "bbox": [307, 514, 350, 525]},
	{"text": "0.90", "bbox": [410, 514, 447, 525]},
	{"text": "0.22", "bbox": [503, 514, 541, 525]},
	{"text": "24.6", "bbox": [597, 513, 634, 523]},
	{"text": "MEF 75/25", "bbox": [105, 526, 202, 536]},
	{"text": "[L/s]", "bbox": [307, 527, 350, 538]},
	{"text": "2.36", "bbox": [410, 527, 447, 538]},
	{"text": "0.50", "bbox": [503, 527, 541, 538]},
	{"text": "21.1", "bbox": [597, 526, 634, 536]},
	{"text": "FET", "bbox": [105, 538, 137, 548]},
	{"text": "[s]", "bbox": [326, 539, 350, 550]},
	{"text": "4.91", "bbox": [503, 539, 541, 550]},
	{"text": "LFV", "bbox": [105, 551, 137, 560]},
	{"text": "[L/min]", "bbox": [287, 551, 350, 562]},
	{"text": "73.10", "bbox": [400, 551, 447, 562]},
	{"text": "Z at 5 Hz", "bbox": [105, 576, 194, 586]},
	{"text": "[kPa/(L/s)]", "bbox": [251, 576, 350, 587]},
	{"text": "0.43", "bbox": [410, 576, 447, 587]},
	{"text": "0.58", "bbox": [503, 576, 541, 587]},
	{"text": "135.7", "bbox": [588, 576, 634, 586]},
	{"text": "Resonant frequency", "bbox": [105, 589, 278, 600]},
	{"text": "[1/s]", "bbox": [307, 589, 350, 600]},
	{"text": "30.00", "bbox": [495, 589, 541, 600]},
	{"text": "R at 5 Hz", "bbox": [105, 602, 194, 612]},
	{"text": "[kPa/(L/s)]", "bbox": [251, 602, 350, 613]},
	{"text": "0.41", "bbox": [410, 602, 447, 613]},
	{"text": "0.57", "bbox": [503, 602, 541, 613]},
	{"text": "137.2", "bbox": [588, 602, 634, 612]},
	{"text": "R nt 20 Hz", "bbox": [105, 615, 202, 624]},
	{"text": "[kPa/(L/s)]", "bbox": [251, 615, 350, 626]},
	{"text": "0.35", "bbox": [410, 615, 447, 626]},
	{"text": "0.34", "bbox": [503, 615, 541, 626]},
	{"text": "95.3", "bbox": [597, 615, 634, 624]},
	{"text": "X at 5 Hz", "bbox": [105, 627, 194, 637]},
	{"text": "[kPa/(L/s)]", "bbox": [251, 627, 350, 638]},
	{"text": "-0.11", "bbox": [400, 627, 447, 638]},
	{"text": "-0.12", "bbox": [495, 627, 541, 638]},
	{"text": "112.5", "bbox": [588, 627, 634, 637]},
	{"text": "Rcentral", "bbox": [105, 640, 183, 650]},
	{"text": "[kPa/(L/s)]", "bbox": [251, 640, 350, 651]},
	{"text": "0.12", "bbox": [503, 640, 541, 651]},
	{"text": "Peripheral", "bbox": [105, 653, 211, 663]},
	{"text": "[kPa/(L/s)]", "bbox": [251, 653, 350, 664]},
	{"text": "0.40", "bbox": [503, 653, 541, 664]},
	{"text": "结论：", "bbox": [107, 689, 160, 705]},
	{"text": "1.中重度混合性肺通气功能障碍", "bbox": [107, 716, 371, 728]},
	{"text": "2.（阻力增加", "bbox": [107, 728, 238, 740]},
	{"text": "审核者专用章", "bbox": [748, 878, 920, 901]},
	{"text": "检查者：王美锦", "bbox": [748, 911, 927, 948]}
]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord API: raw_items=174, valid_items=174, elapsed=43.6s
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能通气阻力检查报告, bbox=[375, 88, 634, 107]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[154, 112, 202, 125]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[154, 125, 347, 138]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[3]: text=身高：151 cm, bbox=[154, 138, 387, 149]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[4]: text=病历号：, bbox=[505, 110, 570, 123]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：72 Years, bbox=[678, 121, 754, 133]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[6]: text=体重：46 kg, bbox=[678, 134, 725, 146]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[7]: text=Flow [L/s], bbox=[120, 165, 172, 175]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[8]: text=F/V ex, bbox=[257, 165, 291, 173]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[9]: text=10, bbox=[102, 178, 114, 187]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[10]: text=5, bbox=[107, 199, 114, 208]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[11]: text=0, bbox=[107, 220, 114, 229]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[12]: text=2, bbox=[173, 230, 181, 238]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[13]: text=4, bbox=[230, 230, 239, 238]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[14]: text=6, bbox=[290, 230, 298, 238]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[15]: text=F/V in, bbox=[259, 274, 290, 283]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[16]: text=8, bbox=[407, 168, 415, 176]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[17]: text=Vol [L], bbox=[422, 170, 457, 181]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[18]: text=6, bbox=[407, 193, 415, 201]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[19]: text=4, bbox=[407, 220, 415, 228]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[20]: text=1, bbox=[624, 218, 633, 227]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[21]: text=Vol%Vcmax, bbox=[375, 243, 438, 252]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[22]: text=100, bbox=[380, 254, 400, 264]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[23]: text=Vcmax, bbox=[435, 257, 472, 266]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[24]: text=20, bbox=[385, 266, 398, 275]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[25]: text=0, bbox=[407, 272, 415, 280]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[26]: text=Time [s], bbox=[505, 262, 546, 272]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[27]: text=0, bbox=[417, 283, 425, 291]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[28]: text=1, bbox=[453, 283, 460, 291]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[29]: text=2, bbox=[487, 283, 495, 291]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[30]: text=3, bbox=[521, 283, 528, 291]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[31]: text=4, bbox=[555, 283, 562, 291]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[32]: text=5, bbox=[590, 283, 597, 291]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[33]: text=6, bbox=[624, 283, 632, 291]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[34]: text=2.0, bbox=[654, 161, 672, 169]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[35]: text=R [kPa/(L/s)] Normal breathingX [kPa/(L/s)], bbox=[678, 163, 887, 174]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[36]: text=1.5, bbox=[654, 187, 672, 195]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[37]: text=1.0, bbox=[654, 215, 672, 223]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[38]: text=0.5, bbox=[654, 243, 672, 251]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[39]: text=0.0, bbox=[654, 271, 672, 279]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[40]: text=0.4, bbox=[892, 170, 909, 178]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[41]: text=0.2, bbox=[892, 193, 909, 201]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[42]: text=R, bbox=[892, 215, 908, 223]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[43]: text=X, bbox=[892, 226, 908, 234]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[44]: text=0.2, bbox=[892, 239, 909, 247]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[45]: text=0.4, bbox=[892, 260, 909, 268]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[46]: text=F [Hz], bbox=[767, 261, 797, 271]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[47]: text=5, bbox=[674, 281, 681, 289]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[48]: text=10, bbox=[706, 281, 718, 289]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[49]: text=15, bbox=[740, 281, 751, 289]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[50]: text=20, bbox=[773, 281, 785, 289]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[51]: text=25, bbox=[810, 281, 823, 289]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[52]: text=30, bbox=[838, 281, 850, 289]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[53]: text=35, bbox=[873, 281, 885, 289]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[54]: text=日期, bbox=[105, 308, 142, 321]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[55]: text=时间, bbox=[105, 321, 142, 334]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[56]: text=预计值, bbox=[389, 296, 447, 309]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[57]: text=实测值, bbox=[483, 296, 541, 309]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[58]: text=实/预, bbox=[586, 295, 634, 308]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[59]: text=25/10/31, bbox=[466, 310, 540, 321]
2026-08-10 11:27:12,356 INFO     29 [qwen-vl-text] coord item[60]: text=14:29:33, bbox=[457, 323, 542, 335]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[61]: text=MV, bbox=[105, 349, 127, 358]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[62]: text=[L/min], bbox=[287, 350, 350, 362]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[63]: text=6.57, bbox=[410, 351, 447, 361]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[64]: text=11.52, bbox=[495, 350, 541, 361]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[65]: text=175.3, bbox=[588, 349, 634, 359]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[66]: text=VT, bbox=[105, 362, 127, 371]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[67]: text=[L], bbox=[326, 363, 350, 374]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[68]: text=0.33, bbox=[410, 364, 447, 374]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[69]: text=0.79, bbox=[503, 363, 541, 374]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[70]: text=239.6, bbox=[588, 362, 634, 373]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[71]: text=BF, bbox=[105, 375, 127, 384]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[72]: text=[1/min], bbox=[287, 376, 350, 387]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[73]: text=20.00, bbox=[400, 376, 447, 387]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[74]: text=14.63, bbox=[495, 376, 541, 387]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[75]: text=73.1, bbox=[597, 375, 634, 385]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[76]: text=VC MAX, bbox=[105, 388, 165, 397]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[77]: text=[L], bbox=[326, 389, 350, 400]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[78]: text=2.03, bbox=[410, 389, 447, 400]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[79]: text=1.48, bbox=[503, 389, 541, 400]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[80]: text=73.0, bbox=[597, 388, 634, 398]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[81]: text=ERV, bbox=[105, 400, 137, 410]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[82]: text=[L], bbox=[326, 401, 350, 412]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[83]: text=0.57, bbox=[410, 401, 447, 412]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[84]: text=0.14, bbox=[503, 401, 541, 412]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[85]: text=25.5, bbox=[597, 400, 634, 410]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[86]: text=IC, bbox=[105, 413, 127, 422]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[87]: text=[L], bbox=[326, 414, 350, 425]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[88]: text=1.46, bbox=[410, 414, 447, 425]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[89]: text=1.34, bbox=[503, 414, 541, 425]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[90]: text=91.6, bbox=[597, 413, 634, 423]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[91]: text=FVC, bbox=[105, 425, 137, 435]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[92]: text=[L], bbox=[326, 426, 350, 437]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[93]: text=1.93, bbox=[410, 426, 447, 437]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[94]: text=1.44, bbox=[503, 426, 541, 437]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[95]: text=74.8, bbox=[597, 425, 634, 435]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[96]: text=FEV 1, bbox=[105, 438, 154, 448]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[97]: text=[L], bbox=[326, 439, 350, 450]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[98]: text=1.56, bbox=[410, 439, 447, 450]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[99]: text=0.91, bbox=[503, 439, 541, 450]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[100]: text=58.4, bbox=[597, 438, 634, 448]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[101]: text=FEV 1 % FVC, bbox=[105, 451, 212, 461]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[102]: text=[%], bbox=[326, 452, 350, 463]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[103]: text=63.38, bbox=[495, 451, 541, 461]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[104]: text=FEV 1 % VC MAX, bbox=[105, 463, 240, 473]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[105]: text=[%], bbox=[326, 464, 350, 475]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[106]: text=75.42, bbox=[400, 464, 447, 475]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[107]: text=61.67, bbox=[495, 464, 541, 475]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[108]: text=81.8, bbox=[597, 463, 634, 473]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[109]: text=PEF, bbox=[105, 476, 137, 485]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[110]: text=[L/s], bbox=[307, 477, 350, 488]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[111]: text=5.04, bbox=[410, 477, 447, 488]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[112]: text=2.51, bbox=[503, 477, 541, 488]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[113]: text=49.8, bbox=[597, 476, 634, 486]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[114]: text=MEF 75, bbox=[105, 488, 165, 498]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[115]: text=[L/s], bbox=[307, 489, 350, 500]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[116]: text=4.66, bbox=[410, 489, 447, 500]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[117]: text=1.54, bbox=[503, 489, 541, 500]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[118]: text=33.1, bbox=[597, 488, 634, 498]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[119]: text=MEF 50, bbox=[105, 501, 165, 510]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[120]: text=[L/s], bbox=[307, 502, 350, 513]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[121]: text=3.06, bbox=[410, 502, 447, 513]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[122]: text=0.56, bbox=[503, 502, 541, 513]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[123]: text=18.2, bbox=[597, 501, 634, 511]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[124]: text=MEF 25, bbox=[105, 513, 165, 523]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[125]: text=[L/s], bbox=[307, 514, 350, 525]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[126]: text=0.90, bbox=[410, 514, 447, 525]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[127]: text=0.22, bbox=[503, 514, 541, 525]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[128]: text=24.6, bbox=[597, 513, 634, 523]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[129]: text=MEF 75/25, bbox=[105, 526, 202, 536]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[130]: text=[L/s], bbox=[307, 527, 350, 538]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[131]: text=2.36, bbox=[410, 527, 447, 538]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[132]: text=0.50, bbox=[503, 527, 541, 538]
2026-08-10 11:27:12,357 INFO     29 [qwen-vl-text] coord item[133]: text=21.1, bbox=[597, 526, 634, 536]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[134]: text=FET, bbox=[105, 538, 137, 548]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[135]: text=[s], bbox=[326, 539, 350, 550]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[136]: text=4.91, bbox=[503, 539, 541, 550]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[137]: text=LFV, bbox=[105, 551, 137, 560]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[138]: text=[L/min], bbox=[287, 551, 350, 562]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[139]: text=73.10, bbox=[400, 551, 447, 562]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[140]: text=Z at 5 Hz, bbox=[105, 576, 194, 586]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[141]: text=[kPa/(L/s)], bbox=[251, 576, 350, 587]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[142]: text=0.43, bbox=[410, 576, 447, 587]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[143]: text=0.58, bbox=[503, 576, 541, 587]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[144]: text=135.7, bbox=[588, 576, 634, 586]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[145]: text=Resonant frequency, bbox=[105, 589, 278, 600]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[146]: text=[1/s], bbox=[307, 589, 350, 600]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[147]: text=30.00, bbox=[495, 589, 541, 600]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[148]: text=R at 5 Hz, bbox=[105, 602, 194, 612]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[149]: text=[kPa/(L/s)], bbox=[251, 602, 350, 613]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[150]: text=0.41, bbox=[410, 602, 447, 613]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[151]: text=0.57, bbox=[503, 602, 541, 613]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[152]: text=137.2, bbox=[588, 602, 634, 612]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[153]: text=R nt 20 Hz, bbox=[105, 615, 202, 624]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[154]: text=[kPa/(L/s)], bbox=[251, 615, 350, 626]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[155]: text=0.35, bbox=[410, 615, 447, 626]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[156]: text=0.34, bbox=[503, 615, 541, 626]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[157]: text=95.3, bbox=[597, 615, 634, 624]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[158]: text=X at 5 Hz, bbox=[105, 627, 194, 637]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[159]: text=[kPa/(L/s)], bbox=[251, 627, 350, 638]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[160]: text=-0.11, bbox=[400, 627, 447, 638]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[161]: text=-0.12, bbox=[495, 627, 541, 638]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[162]: text=112.5, bbox=[588, 627, 634, 637]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[163]: text=Rcentral, bbox=[105, 640, 183, 650]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[164]: text=[kPa/(L/s)], bbox=[251, 640, 350, 651]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[165]: text=0.12, bbox=[503, 640, 541, 651]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[166]: text=Peripheral, bbox=[105, 653, 211, 663]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[167]: text=[kPa/(L/s)], bbox=[251, 653, 350, 664]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[168]: text=0.40, bbox=[503, 653, 541, 664]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[169]: text=结论：, bbox=[107, 689, 160, 705]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[170]: text=1.中重度混合性肺通气功能障碍, bbox=[107, 716, 371, 728]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[171]: text=2.（阻力增加, bbox=[107, 728, 238, 740]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[172]: text=审核者专用章, bbox=[748, 878, 920, 901]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] coord item[173]: text=检查者：王美锦, bbox=[748, 911, 927, 948]
2026-08-10 11:27:12,358 INFO     29 [qwen-vl-text] page=7 — 172/172 coords, api_time=43.6s
2026-08-10 11:27:12,359 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=851048, prompt_len=2127
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共169行）
["贵州医科大学附属医院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "对比试验", "姓名：", "性别：女", "身高：151 cm", "病历号：", "年龄：72 Years", "体重：46 kg", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "3", "4", "5", "6", "7", "F/V in", "6", "Vol [L]", "4", "TLC", "ER,pleth2", "RV", "Time [min]", "Pred Act 0.0", "0.2", "0.4", "0.6", "0.8", "1.0", "日期", "时间", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "25/10/31", "14:29:33", "25/10/31", "14:53:10", "VT", "[L]", "0.33", "0.79", "239.6", "BF", "[1/min]", "20.00", "14.63", "73.1", "MV", "[L/min]", "6.57", "11.52", "175.3", "VC MAX", "[L]", "2.03", "1.48", "73.0", "1.66", "81.9", "12.2", "ERV", "[L]", "0.57", "0.14", "25.5", "IC", "[L]", "1.46", "1.34", "91.6", "FVC", "[L]", "1.93", "1.44", "74.8", "1.66", "86.2", "15.3", "FEV 1", "[L]", "1.56", "0.91", "58.4", "1.08", "68.8", "17.8", "FEV 1 % FVC", "[%]", "63.38", "64.76", "2.2", "FEV 1 % VC MAX", "[%]", "75.42", "61.67", "81.8", "64.76", "85.9", "5.0", "PEF", "[L/s]", "5.04", "2.51", "49.8", "3.35", "66.5", "33.6", "MEF 75", "[L/s]", "4.66", "1.54", "33.1", "1.72", "36.8", "11.3", "MEF 50", "[L/s]", "3.06", "0.56", "18.2", "0.83", "27.1", "49.1", "MEF 25", "[L/s]", "0.90", "0.22", "24.6", "0.36", "39.8", "62.1", "MMEF 75/25", "[L/s]", "2.36", "0.50", "21.1", "0.47", "20.0", "-4.9", "FET", "[s]", "4.91", "4.88", "-0.6", "V backextrapol. % FVC", "[%]", "3.85", "4.39", "13.9", "MVV", "[L/min]", "73.10", "结论：", "1.中重度混合性肺通气功能障碍", "2.气道阻力增加", "3.支气管舒张试验阳性 (+)", "吸入沙丁胺醇400μg", "FVC上升15.3%，增加220ml；", "审核者：", "检查者："]

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
2026-08-10 11:27:56,271 INFO     29 [qwen-vl-text] coord API raw response (len=8443):
[
	{"text": "贵州医科大学附属医院", "bbox": [378, 85, 687, 107]},
	{"text": "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "bbox": [378, 107, 687, 115]},
	{"text": "对比试验", "bbox": [440, 126, 538, 145]},
	{"text": "姓名：", "bbox": [137, 152, 183, 165]},
	{"text": "性别：女", "bbox": [137, 165, 328, 178]},
	{"text": "身高：151 cm", "bbox": [137, 178, 366, 190]},
	{"text": "病历号：", "bbox": [491, 148, 557, 161]},
	{"text": "年龄：72 Years", "bbox": [491, 161, 739, 173]},
	{"text": "体重：46 kg", "bbox": [491, 173, 711, 186]},
	{"text": "Flow [L/s]", "bbox": [180, 203, 235, 214]},
	{"text": "F/V ex", "bbox": [350, 203, 385, 213]},
	{"text": "10", "bbox": [161, 222, 175, 231]},
	{"text": "5", "bbox": [167, 247, 175, 256]},
	{"text": "0", "bbox": [167, 273, 175, 282]},
	{"text": "2", "bbox": [250, 280, 257, 289]},
	{"text": "3", "bbox": [285, 280, 292, 289]},
	{"text": "4", "bbox": [320, 280, 327, 289]},
	{"text": "5", "bbox": [355, 280, 362, 289]},
	{"text": "6", "bbox": [389, 280, 397, 289]},
	{"text": "7", "bbox": [424, 280, 431, 289]},
	{"text": "F/V in", "bbox": [357, 335, 387, 345]},
	{"text": "6", "bbox": [547, 197, 554, 206]},
	{"text": "Vol [L]", "bbox": [561, 200, 596, 211]},
	{"text": "4", "bbox": [547, 243, 555, 252]},
	{"text": "TLC", "bbox": [501, 248, 521, 258]},
	{"text": "ER,pleth2", "bbox": [501, 288, 554, 298]},
	{"text": "RV", "bbox": [501, 300, 518, 310]},
	{"text": "Time [min]", "bbox": [658, 321, 715, 332]},
	{"text": "Pred Act 0.0", "bbox": [501, 343, 568, 353]},
	{"text": "0.2", "bbox": [601, 342, 619, 351]},
	{"text": "0.4", "bbox": [652, 342, 670, 351]},
	{"text": "0.6", "bbox": [703, 342, 721, 351]},
	{"text": "0.8", "bbox": [753, 342, 772, 351]},
	{"text": "1.0", "bbox": [805, 342, 823, 351]},
	{"text": "日期", "bbox": [150, 375, 182, 386]},
	{"text": "时间", "bbox": [150, 387, 182, 398]},
	{"text": "预计值", "bbox": [396, 360, 448, 372]},
	{"text": "前次", "bbox": [489, 360, 524, 372]},
	{"text": "前/预", "bbox": [558, 360, 601, 372]},
	{"text": "后次", "bbox": [643, 360, 679, 372]},
	{"text": "后/预", "bbox": [713, 360, 756, 372]},
	{"text": "改善率", "bbox": [782, 360, 834, 372]},
	{"text": "25/10/31", "bbox": [456, 374, 524, 384]},
	{"text": "14:29:33", "bbox": [456, 387, 524, 396]},
	{"text": "25/10/31", "bbox": [609, 374, 678, 384]},
	{"text": "14:53:10", "bbox": [609, 387, 678, 396]},
	{"text": "VT", "bbox": [150, 412, 169, 421]},
	{"text": "[L]", "bbox": [351, 411, 372, 421]},
	{"text": "0.33", "bbox": [415, 411, 450, 421]},
	{"text": "0.79", "bbox": [490, 411, 525, 421]},
	{"text": "239.6", "bbox": [558, 411, 602, 421]},
	{"text": "BF", "bbox": [150, 424, 169, 433]},
	{"text": "[1/min]", "bbox": [316, 423, 372, 433]},
	{"text": "20.00", "bbox": [407, 423, 450, 433]},
	{"text": "14.63", "bbox": [483, 423, 525, 433]},
	{"text": "73.1", "bbox": [566, 423, 602, 433]},
	{"text": "MV", "bbox": [150, 436, 169, 445]},
	{"text": "[L/min]", "bbox": [316, 435, 372, 445]},
	{"text": "6.57", "bbox": [415, 435, 450, 445]},
	{"text": "11.52", "bbox": [483, 435, 525, 445]},
	{"text": "175.3", "bbox": [558, 435, 602, 445]},
	{"text": "VC MAX", "bbox": [150, 459, 204, 468]},
	{"text": "[L]", "bbox": [351, 458, 372, 468]},
	{"text": "2.03", "bbox": [415, 458, 450, 468]},
	{"text": "1.48", "bbox": [490, 458, 525, 468]},
	{"text": "73.0", "bbox": [566, 458, 602, 468]},
	{"text": "1.66", "bbox": [642, 458, 678, 468]},
	{"text": "81.9", "bbox": [720, 458, 756, 468]},
	{"text": "12.2", "bbox": [798, 458, 834, 468]},
	{"text": "ERV", "bbox": [150, 471, 179, 480]},
	{"text": "[L]", "bbox": [351, 470, 372, 480]},
	{"text": "0.57", "bbox": [415, 470, 450, 480]},
	{"text": "0.14", "bbox": [490, 470, 525, 480]},
	{"text": "25.5", "bbox": [566, 470, 602, 480]},
	{"text": "IC", "bbox": [150, 483, 170, 492]},
	{"text": "[L]", "bbox": [351, 482, 372, 492]},
	{"text": "1.46", "bbox": [415, 482, 450, 492]},
	{"text": "1.34", "bbox": [490, 482, 525, 492]},
	{"text": "91.6", "bbox": [566, 482, 602, 492]},
	{"text": "FVC", "bbox": [150, 506, 180, 515]},
	{"text": "[L]", "bbox": [351, 505, 372, 515]},
	{"text": "1.93", "bbox": [415, 505, 450, 515]},
	{"text": "1.44", "bbox": [490, 505, 525, 515]},
	{"text": "74.8", "bbox": [566, 505, 602, 515]},
	{"text": "1.66", "bbox": [642, 505, 678, 515]},
	{"text": "86.2", "bbox": [720, 505, 756, 515]},
	{"text": "15.3", "bbox": [798, 505, 834, 515]},
	{"text": "FEV 1", "bbox": [150, 518, 196, 527]},
	{"text": "[L]", "bbox": [351, 517, 372, 527]},
	{"text": "1.56", "bbox": [415, 517, 450, 527]},
	{"text": "0.91", "bbox": [490, 517, 525, 527]},
	{"text": "58.4", "bbox": [566, 517, 602, 527]},
	{"text": "1.08", "bbox": [642, 517, 678, 527]},
	{"text": "68.8", "bbox": [720, 517, 756, 527]},
	{"text": "17.8", "bbox": [798, 517, 834, 527]},
	{"text": "FEV 1 % FVC", "bbox": [150, 530, 249, 539]},
	{"text": "[%]", "bbox": [351, 529, 372, 539]},
	{"text": "63.38", "bbox": [483, 529, 525, 539]},
	{"text": "64.76", "bbox": [634, 529, 678, 539]},
	{"text": "2.2", "bbox": [806, 529, 834, 539]},
	{"text": "FEV 1 % VC MAX", "bbox": [150, 542, 274, 551]},
	{"text": "[%]", "bbox": [351, 541, 372, 551]},
	{"text": "75.42", "bbox": [407, 541, 450, 551]},
	{"text": "61.67", "bbox": [483, 541, 525, 551]},
	{"text": "81.8", "bbox": [566, 541, 602, 551]},
	{"text": "64.76", "bbox": [634, 541, 678, 551]},
	{"text": "85.9", "bbox": [720, 541, 756, 551]},
	{"text": "5.0", "bbox": [806, 541, 834, 551]},
	{"text": "PEF", "bbox": [150, 554, 180, 563]},
	{"text": "[L/s]", "bbox": [334, 553, 372, 563]},
	{"text": "5.04", "bbox": [415, 553, 450, 563]},
	{"text": "2.51", "bbox": [490, 553, 525, 563]},
	{"text": "49.8", "bbox": [566, 553, 602, 563]},
	{"text": "3.35", "bbox": [642, 553, 678, 563]},
	{"text": "66.5", "bbox": [720, 553, 756, 563]},
	{"text": "33.6", "bbox": [798, 553, 834, 563]},
	{"text": "MEF 75", "bbox": [150, 566, 204, 575]},
	{"text": "[L/s]", "bbox": [334, 565, 372, 575]},
	{"text": "4.66", "bbox": [415, 565, 450, 575]},
	{"text": "1.54", "bbox": [490, 565, 525, 575]},
	{"text": "33.1", "bbox": [566, 565, 602, 575]},
	{"text": "1.72", "bbox": [642, 565, 678, 575]},
	{"text": "36.8", "bbox": [720, 565, 756, 575]},
	{"text": "11.3", "bbox": [798, 565, 834, 575]},
	{"text": "MEF 50", "bbox": [150, 578, 204, 587]},
	{"text": "[L/s]", "bbox": [334, 577, 372, 587]},
	{"text": "3.06", "bbox": [415, 577, 450, 587]},
	{"text": "0.56", "bbox": [490, 577, 525, 587]},
	{"text": "18.2", "bbox": [566, 577, 602, 587]},
	{"text": "0.83", "bbox": [642, 577, 678, 587]},
	{"text": "27.1", "bbox": [720, 577, 756, 587]},
	{"text": "49.1", "bbox": [798, 577, 834, 587]},
	{"text": "MEF 25", "bbox": [150, 590, 204, 599]},
	{"text": "[L/s]", "bbox": [334, 589, 372, 599]},
	{"text": "0.90", "bbox": [415, 589, 450, 599]},
	{"text": "0.22", "bbox": [490, 589, 525, 599]},
	{"text": "24.6", "bbox": [566, 589, 602, 599]},
	{"text": "0.36", "bbox": [642, 589, 678, 599]},
	{"text": "39.8", "bbox": [720, 589, 756, 599]},
	{"text": "62.1", "bbox": [798, 589, 834, 599]},
	{"text": "MMEF 75/25", "bbox": [150, 602, 240, 611]},
	{"text": "[L/s]", "bbox": [334, 601, 372, 611]},
	{"text": "2.36", "bbox": [415, 601, 450, 611]},
	{"text": "0.50", "bbox": [490, 601, 525, 611]},
	{"text": "21.1", "bbox": [566, 601, 602, 611]},
	{"text": "0.47", "bbox": [642, 601, 678, 611]},
	{"text": "20.0", "bbox": [720, 601, 756, 611]},
	{"text": "-4.9", "bbox": [798, 601, 834, 611]},
	{"text": "FET", "bbox": [150, 614, 180, 623]},
	{"text": "[s]", "bbox": [351, 613, 372, 623]},
	{"text": "4.91", "bbox": [490, 613, 525, 623]},
	{"text": "4.88", "bbox": [642, 613, 678, 623]},
	{"text": "-0.6", "bbox": [798, 613, 834, 623]},
	{"text": "V backextrapol. % FVC", "bbox": [150, 625, 332, 635]},
	{"text": "[%]", "bbox": [351, 624, 372, 635]},
	{"text": "3.85", "bbox": [490, 624, 525, 635]},
	{"text": "4.39", "bbox": [642, 624, 678, 635]},
	{"text": "13.9", "bbox": [798, 624, 834, 635]},
	{"text": "MVV", "bbox": [152, 648, 180, 656]},
	{"text": "[L/min]", "bbox": [316, 647, 372, 657]},
	{"text": "73.10", "bbox": [407, 647, 450, 657]},
	{"text": "结论：", "bbox": [93, 684, 144, 700]},
	{"text": "1.中重度混合性肺通气功能障碍", "bbox": [104, 707, 415, 722]},
	{"text": "2.气道阻力增加", "bbox": [104, 722, 257, 737]},
	{"text": "3.支气管舒张试验阳性 (+)", "bbox": [104, 751, 370, 766]},
	{"text": "吸入沙丁胺醇400μg", "bbox": [104, 766, 293, 781]},
	{"text": "FVC上升15.3%，增加220ml；", "bbox": [104, 781, 368, 796]},
	{"text": "审核者：", "bbox": [687, 905, 764, 924]},
	{"text": "检查者：", "bbox": [687, 940, 764, 958]}
]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord API: raw_items=169, valid_items=169, elapsed=43.9s
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[0]: text=贵州医科大学附属医院, bbox=[378, 85, 687, 107]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[1]: text=THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY, bbox=[378, 107, 687, 115]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[2]: text=对比试验, bbox=[440, 126, 538, 145]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[137, 152, 183, 165]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[137, 165, 328, 178]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[5]: text=身高：151 cm, bbox=[137, 178, 366, 190]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[6]: text=病历号：, bbox=[491, 148, 557, 161]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：72 Years, bbox=[491, 161, 739, 173]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[8]: text=体重：46 kg, bbox=[491, 173, 711, 186]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[9]: text=Flow [L/s], bbox=[180, 203, 235, 214]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[10]: text=F/V ex, bbox=[350, 203, 385, 213]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[11]: text=10, bbox=[161, 222, 175, 231]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[12]: text=5, bbox=[167, 247, 175, 256]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[13]: text=0, bbox=[167, 273, 175, 282]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[14]: text=2, bbox=[250, 280, 257, 289]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[15]: text=3, bbox=[285, 280, 292, 289]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[16]: text=4, bbox=[320, 280, 327, 289]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[17]: text=5, bbox=[355, 280, 362, 289]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[18]: text=6, bbox=[389, 280, 397, 289]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[19]: text=7, bbox=[424, 280, 431, 289]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[20]: text=F/V in, bbox=[357, 335, 387, 345]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[21]: text=6, bbox=[547, 197, 554, 206]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[22]: text=Vol [L], bbox=[561, 200, 596, 211]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[23]: text=4, bbox=[547, 243, 555, 252]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[24]: text=TLC, bbox=[501, 248, 521, 258]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[25]: text=ER,pleth2, bbox=[501, 288, 554, 298]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[26]: text=RV, bbox=[501, 300, 518, 310]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[27]: text=Time [min], bbox=[658, 321, 715, 332]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[28]: text=Pred Act 0.0, bbox=[501, 343, 568, 353]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[29]: text=0.2, bbox=[601, 342, 619, 351]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[30]: text=0.4, bbox=[652, 342, 670, 351]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[31]: text=0.6, bbox=[703, 342, 721, 351]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[32]: text=0.8, bbox=[753, 342, 772, 351]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[33]: text=1.0, bbox=[805, 342, 823, 351]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[34]: text=日期, bbox=[150, 375, 182, 386]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[35]: text=时间, bbox=[150, 387, 182, 398]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[36]: text=预计值, bbox=[396, 360, 448, 372]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[37]: text=前次, bbox=[489, 360, 524, 372]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[38]: text=前/预, bbox=[558, 360, 601, 372]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[39]: text=后次, bbox=[643, 360, 679, 372]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[40]: text=后/预, bbox=[713, 360, 756, 372]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[41]: text=改善率, bbox=[782, 360, 834, 372]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[42]: text=25/10/31, bbox=[456, 374, 524, 384]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[43]: text=14:29:33, bbox=[456, 387, 524, 396]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[44]: text=25/10/31, bbox=[609, 374, 678, 384]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[45]: text=14:53:10, bbox=[609, 387, 678, 396]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[46]: text=VT, bbox=[150, 412, 169, 421]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[47]: text=[L], bbox=[351, 411, 372, 421]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[48]: text=0.33, bbox=[415, 411, 450, 421]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[49]: text=0.79, bbox=[490, 411, 525, 421]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[50]: text=239.6, bbox=[558, 411, 602, 421]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[51]: text=BF, bbox=[150, 424, 169, 433]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[52]: text=[1/min], bbox=[316, 423, 372, 433]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[53]: text=20.00, bbox=[407, 423, 450, 433]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[54]: text=14.63, bbox=[483, 423, 525, 433]
2026-08-10 11:27:56,272 INFO     29 [qwen-vl-text] coord item[55]: text=73.1, bbox=[566, 423, 602, 433]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[56]: text=MV, bbox=[150, 436, 169, 445]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[57]: text=[L/min], bbox=[316, 435, 372, 445]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[58]: text=6.57, bbox=[415, 435, 450, 445]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[59]: text=11.52, bbox=[483, 435, 525, 445]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[60]: text=175.3, bbox=[558, 435, 602, 445]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[61]: text=VC MAX, bbox=[150, 459, 204, 468]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[62]: text=[L], bbox=[351, 458, 372, 468]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[63]: text=2.03, bbox=[415, 458, 450, 468]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[64]: text=1.48, bbox=[490, 458, 525, 468]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[65]: text=73.0, bbox=[566, 458, 602, 468]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[66]: text=1.66, bbox=[642, 458, 678, 468]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[67]: text=81.9, bbox=[720, 458, 756, 468]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[68]: text=12.2, bbox=[798, 458, 834, 468]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[69]: text=ERV, bbox=[150, 471, 179, 480]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[70]: text=[L], bbox=[351, 470, 372, 480]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[71]: text=0.57, bbox=[415, 470, 450, 480]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[72]: text=0.14, bbox=[490, 470, 525, 480]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[73]: text=25.5, bbox=[566, 470, 602, 480]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[74]: text=IC, bbox=[150, 483, 170, 492]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[75]: text=[L], bbox=[351, 482, 372, 492]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[76]: text=1.46, bbox=[415, 482, 450, 492]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[77]: text=1.34, bbox=[490, 482, 525, 492]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[78]: text=91.6, bbox=[566, 482, 602, 492]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[79]: text=FVC, bbox=[150, 506, 180, 515]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[80]: text=[L], bbox=[351, 505, 372, 515]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[81]: text=1.93, bbox=[415, 505, 450, 515]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[82]: text=1.44, bbox=[490, 505, 525, 515]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[83]: text=74.8, bbox=[566, 505, 602, 515]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[84]: text=1.66, bbox=[642, 505, 678, 515]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[85]: text=86.2, bbox=[720, 505, 756, 515]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[86]: text=15.3, bbox=[798, 505, 834, 515]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[87]: text=FEV 1, bbox=[150, 518, 196, 527]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[88]: text=[L], bbox=[351, 517, 372, 527]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[89]: text=1.56, bbox=[415, 517, 450, 527]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[90]: text=0.91, bbox=[490, 517, 525, 527]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[91]: text=58.4, bbox=[566, 517, 602, 527]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[92]: text=1.08, bbox=[642, 517, 678, 527]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[93]: text=68.8, bbox=[720, 517, 756, 527]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[94]: text=17.8, bbox=[798, 517, 834, 527]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[95]: text=FEV 1 % FVC, bbox=[150, 530, 249, 539]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[96]: text=[%], bbox=[351, 529, 372, 539]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[97]: text=63.38, bbox=[483, 529, 525, 539]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[98]: text=64.76, bbox=[634, 529, 678, 539]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[99]: text=2.2, bbox=[806, 529, 834, 539]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[100]: text=FEV 1 % VC MAX, bbox=[150, 542, 274, 551]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[101]: text=[%], bbox=[351, 541, 372, 551]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[102]: text=75.42, bbox=[407, 541, 450, 551]
2026-08-10 11:27:56,273 INFO     29 [qwen-vl-text] coord item[103]: text=61.67, bbox=[483, 541, 525, 551]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[104]: text=81.8, bbox=[566, 541, 602, 551]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[105]: text=64.76, bbox=[634, 541, 678, 551]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[106]: text=85.9, bbox=[720, 541, 756, 551]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[107]: text=5.0, bbox=[806, 541, 834, 551]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[108]: text=PEF, bbox=[150, 554, 180, 563]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[109]: text=[L/s], bbox=[334, 553, 372, 563]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[110]: text=5.04, bbox=[415, 553, 450, 563]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[111]: text=2.51, bbox=[490, 553, 525, 563]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[112]: text=49.8, bbox=[566, 553, 602, 563]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[113]: text=3.35, bbox=[642, 553, 678, 563]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[114]: text=66.5, bbox=[720, 553, 756, 563]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[115]: text=33.6, bbox=[798, 553, 834, 563]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[116]: text=MEF 75, bbox=[150, 566, 204, 575]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[117]: text=[L/s], bbox=[334, 565, 372, 575]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[118]: text=4.66, bbox=[415, 565, 450, 575]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[119]: text=1.54, bbox=[490, 565, 525, 575]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[120]: text=33.1, bbox=[566, 565, 602, 575]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[121]: text=1.72, bbox=[642, 565, 678, 575]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[122]: text=36.8, bbox=[720, 565, 756, 575]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[123]: text=11.3, bbox=[798, 565, 834, 575]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[124]: text=MEF 50, bbox=[150, 578, 204, 587]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[125]: text=[L/s], bbox=[334, 577, 372, 587]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[126]: text=3.06, bbox=[415, 577, 450, 587]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[127]: text=0.56, bbox=[490, 577, 525, 587]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[128]: text=18.2, bbox=[566, 577, 602, 587]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[129]: text=0.83, bbox=[642, 577, 678, 587]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[130]: text=27.1, bbox=[720, 577, 756, 587]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[131]: text=49.1, bbox=[798, 577, 834, 587]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[132]: text=MEF 25, bbox=[150, 590, 204, 599]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[133]: text=[L/s], bbox=[334, 589, 372, 599]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[134]: text=0.90, bbox=[415, 589, 450, 599]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[135]: text=0.22, bbox=[490, 589, 525, 599]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[136]: text=24.6, bbox=[566, 589, 602, 599]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[137]: text=0.36, bbox=[642, 589, 678, 599]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[138]: text=39.8, bbox=[720, 589, 756, 599]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[139]: text=62.1, bbox=[798, 589, 834, 599]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[140]: text=MMEF 75/25, bbox=[150, 602, 240, 611]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[141]: text=[L/s], bbox=[334, 601, 372, 611]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[142]: text=2.36, bbox=[415, 601, 450, 611]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[143]: text=0.50, bbox=[490, 601, 525, 611]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[144]: text=21.1, bbox=[566, 601, 602, 611]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[145]: text=0.47, bbox=[642, 601, 678, 611]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[146]: text=20.0, bbox=[720, 601, 756, 611]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[147]: text=-4.9, bbox=[798, 601, 834, 611]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[148]: text=FET, bbox=[150, 614, 180, 623]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[149]: text=[s], bbox=[351, 613, 372, 623]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[150]: text=4.91, bbox=[490, 613, 525, 623]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[151]: text=4.88, bbox=[642, 613, 678, 623]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[152]: text=-0.6, bbox=[798, 613, 834, 623]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[153]: text=V backextrapol. % FVC, bbox=[150, 625, 332, 635]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[154]: text=[%], bbox=[351, 624, 372, 635]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[155]: text=3.85, bbox=[490, 624, 525, 635]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[156]: text=4.39, bbox=[642, 624, 678, 635]
2026-08-10 11:27:56,274 INFO     29 [qwen-vl-text] coord item[157]: text=13.9, bbox=[798, 624, 834, 635]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[158]: text=MVV, bbox=[152, 648, 180, 656]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[159]: text=[L/min], bbox=[316, 647, 372, 657]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[160]: text=73.10, bbox=[407, 647, 450, 657]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[161]: text=结论：, bbox=[93, 684, 144, 700]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[162]: text=1.中重度混合性肺通气功能障碍, bbox=[104, 707, 415, 722]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[163]: text=2.气道阻力增加, bbox=[104, 722, 257, 737]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[164]: text=3.支气管舒张试验阳性 (+), bbox=[104, 751, 370, 766]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[165]: text=吸入沙丁胺醇400μg, bbox=[104, 766, 293, 781]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[166]: text=FVC上升15.3%，增加220ml；, bbox=[104, 781, 368, 796]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[167]: text=审核者：, bbox=[687, 905, 764, 924]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] coord item[168]: text=检查者：, bbox=[687, 940, 764, 958]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] page=8 — 169/169 coords, api_time=43.9s
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] new_positions (341):
[[7, 229.5, 388.008, 73.21851904296875, 89.02706292724609], [7, 94.248, 123.624, 93.18720605468751, 104.00357818603516], [7, 94.248, 212.364, 104.00357818603516, 114.81995031738282], [7, 94.248, 236.844, 114.81995031738282, 123.97226519775391], [7, 309.06, 348.84, 91.52314880371094, 102.3395209350586], [7, 414.936, 461.448, 100.67546368408203, 110.6598071899414], [7, 414.936, 443.7, 111.4918358154297, 121.47617932128907], [7, 73.44, 105.264, 137.28472320556642, 145.60500946044922], [7, 157.284, 178.09199999999998, 137.28472320556642, 143.94095220947267], [7, 62.424, 69.768, 148.10109533691406, 155.5893529663086], [7, 65.484, 69.768, 165.57369647216797, 173.0619541015625], [7, 65.484, 69.768, 183.04629760742188, 190.5345552368164], [7, 105.876, 110.77199999999999, 191.36658386230468, 198.02281286621096], [7, 140.76, 146.268, 191.36658386230468, 198.02281286621096], [7, 177.48, 182.376, 191.36658386230468, 198.02281286621096], [7, 158.508, 177.48, 227.97584338378905, 235.4641010131836], [7, 249.084, 253.98, 139.78080908203125, 146.4370380859375], [7, 258.264, 279.68399999999997, 141.4448663330078, 150.59718121337892], [7, 249.084, 253.98, 160.58152471923827, 167.23775372314452], [7, 249.084, 253.98, 183.04629760742188, 189.70252661132812], [7, 381.888, 387.396, 181.38224035644532, 188.87049798583985], [7, 229.5, 268.056, 202.18295599365234, 209.67121362304687], [7, 232.56, 244.79999999999998, 211.33527087402345, 219.65555712890625], [7, 266.21999999999997, 288.864, 213.83135675048828, 221.3196143798828], [7, 235.62, 243.576, 221.3196143798828, 228.80787200927736], [7, 249.084, 253.98, 226.3117861328125, 232.96801513671875], [7, 309.06, 334.152, 217.9914998779297, 226.3117861328125], [7, 255.204, 260.1, 235.4641010131836, 242.12033001708986], [7, 277.236, 281.52, 235.4641010131836, 242.12033001708986], [7, 298.044, 302.94, 235.4641010131836, 242.12033001708986], [7, 318.852, 323.13599999999997, 235.4641010131836, 242.12033001708986], [7, 339.65999999999997, 343.944, 235.4641010131836, 242.12033001708986], [7, 361.08, 365.364, 235.4641010131836, 242.12033001708986], [7, 381.888, 386.784, 235.4641010131836, 242.12033001708986], [7, 400.248, 411.264, 133.95660870361328, 140.61283770751953], [7, 414.936, 542.8439999999999, 135.62066595458984, 144.77298083496095], [7, 400.248, 411.264, 155.5893529663086, 162.24558197021486], [7, 400.248, 411.264, 178.88615447998046, 185.5423834838867], [7, 400.248, 411.264, 202.18295599365234, 208.8391849975586], [7, 400.248, 411.264, 225.47975750732422, 232.13598651123047], [7, 545.904, 556.308, 141.4448663330078, 148.10109533691406], [7, 545.904, 556.308, 160.58152471923827, 167.23775372314452], [7, 545.904, 555.696, 178.88615447998046, 185.5423834838867], [7, 545.904, 555.696, 188.03846936035157, 194.69469836425782], [7, 545.904, 556.308, 198.85484149169923, 205.51107049560548], [7, 545.904, 556.308, 216.32744262695314, 222.9836716308594], [7, 469.404, 487.764, 217.15947125244142, 225.47975750732422], [7, 412.488, 416.772, 233.80004376220703, 240.4562727661133], [7, 432.072, 439.416, 233.80004376220703, 240.4562727661133], [7, 452.88, 459.61199999999997, 233.80004376220703, 240.4562727661133], [7, 473.07599999999996, 480.42, 233.80004376220703, 240.4562727661133], [7, 495.71999999999997, 503.676, 233.80004376220703, 240.4562727661133], [7, 512.856, 520.2, 233.80004376220703, 240.4562727661133], [7, 534.276, 541.62, 233.80004376220703, 240.4562727661133], [7, 64.26, 86.904, 256.2648166503906, 267.08118878173826], [7, 64.26, 86.904, 267.08118878173826, 277.89756091308595], [7, 238.06799999999998, 273.564, 246.28047314453124, 257.09684527587893], [7, 295.596, 331.092, 246.28047314453124, 257.09684527587893], [7, 358.632, 388.008, 245.44844451904297, 256.2648166503906], [7, 285.192, 330.48, 257.9288739013672, 267.08118878173826], [7, 279.68399999999997, 331.704, 268.7452460327149, 278.7295895385742], [7, 64.26, 77.724, 290.37799029541014, 297.86624792480467], [7, 175.644, 214.2, 291.21001892089845, 301.19436242675783], [7, 250.92, 273.564, 292.0420475463867, 300.36233380126953], [7, 302.94, 331.092, 291.21001892089845, 300.36233380126953], [7, 359.856, 388.008, 290.37799029541014, 298.698276550293], [7, 64.26, 77.724, 301.19436242675783, 308.68262005615236], [7, 199.512, 214.2, 302.0263910522461, 311.1787059326172], [7, 250.92, 273.564, 302.8584196777344, 311.1787059326172], [7, 307.836, 331.092, 302.0263910522461, 311.1787059326172], [7, 359.856, 388.008, 301.19436242675783, 310.3466773071289], [7, 64.26, 77.724, 312.01073455810547, 319.4989921875], [7, 175.644, 214.2, 312.8427631835938, 321.99507806396485], [7, 244.79999999999998, 273.564, 312.8427631835938, 321.99507806396485], [7, 302.94, 331.092, 312.8427631835938, 321.99507806396485], [7, 365.364, 388.008, 312.01073455810547, 320.3310208129883], [7, 64.26, 100.98, 322.82710668945316, 330.3153643188477], [7, 199.512, 214.2, 323.6591353149414, 332.8114501953125], [7, 250.92, 273.564, 323.6591353149414, 332.8114501953125], [7, 307.836, 331.092, 323.6591353149414, 332.8114501953125], [7, 365.364, 388.008, 322.82710668945316, 331.14739294433593], [7, 64.26, 83.844, 332.8114501953125, 341.1317364501953], [7, 199.512, 214.2, 333.6434788208008, 342.7957937011719], [7, 250.92, 273.564, 333.6434788208008, 342.7957937011719], [7, 307.836, 331.092, 333.6434788208008, 342.7957937011719], [7, 365.364, 388.008, 332.8114501953125, 341.1317364501953], [7, 64.26, 77.724, 343.6278223266602, 351.1160799560547], [7, 199.512, 214.2, 344.45985095214843, 353.61216583251957], [7, 250.92, 273.564, 344.45985095214843, 353.61216583251957], [7, 307.836, 331.092, 344.45985095214843, 353.61216583251957], [7, 365.364, 388.008, 343.6278223266602, 351.94810858154295], [7, 64.26, 83.844, 353.61216583251957, 361.93245208740234], [7, 199.512, 214.2, 354.4441944580078, 363.5965093383789], [7, 250.92, 273.564, 354.4441944580078, 363.5965093383789], [7, 307.836, 331.092, 354.4441944580078, 363.5965093383789], [7, 365.364, 388.008, 353.61216583251957, 361.93245208740234], [7, 64.26, 94.248, 364.4285379638672, 372.74882421875003], [7, 199.512, 214.2, 365.2605665893555, 374.4128814697266], [7, 250.92, 273.564, 365.2605665893555, 374.4128814697266], [7, 307.836, 331.092, 365.2605665893555, 374.4128814697266], [7, 365.364, 388.008, 364.4285379638672, 372.74882421875003], [7, 64.26, 129.744, 375.24491009521483, 383.56519635009766], [7, 199.512, 214.2, 376.07693872070314, 385.2292536010742], [7, 302.94, 331.092, 375.24491009521483, 383.56519635009766], [7, 64.26, 146.88, 385.2292536010742, 393.54953985595705], [7, 199.512, 214.2, 386.0612822265625, 395.2135971069336], [7, 244.79999999999998, 273.564, 386.0612822265625, 395.2135971069336], [7, 302.94, 331.092, 386.0612822265625, 395.2135971069336], [7, 365.364, 388.008, 385.2292536010742, 393.54953985595705], [7, 64.26, 83.844, 396.0456257324219, 403.53388336181644], [7, 187.884, 214.2, 396.87765435791016, 406.02996923828124], [7, 250.92, 273.564, 396.87765435791016, 406.02996923828124], [7, 307.836, 331.092, 396.87765435791016, 406.02996923828124], [7, 365.364, 388.008, 396.0456257324219, 404.3659119873047], [7, 64.26, 100.98, 406.02996923828124, 414.35025549316407], [7, 187.884, 214.2, 406.86199786376955, 416.0143127441406], [7, 250.92, 273.564, 406.86199786376955, 416.0143127441406], [7, 307.836, 331.092, 406.86199786376955, 416.0143127441406], [7, 365.364, 388.008, 406.02996923828124, 414.35025549316407], [7, 64.26, 100.98, 416.84634136962893, 424.33459899902346], [7, 187.884, 214.2, 417.6783699951172, 426.8306848754883], [7, 250.92, 273.564, 417.6783699951172, 426.8306848754883], [7, 307.836, 331.092, 417.6783699951172, 426.8306848754883], [7, 365.364, 388.008, 416.84634136962893, 425.1666276245117], [7, 64.26, 100.98, 426.8306848754883, 435.1509711303711], [7, 187.884, 214.2, 427.66271350097657, 436.81502838134764], [7, 250.92, 273.564, 427.66271350097657, 436.81502838134764], [7, 307.836, 331.092, 427.66271350097657, 436.81502838134764], [7, 365.364, 388.008, 426.8306848754883, 435.1509711303711], [7, 64.26, 123.624, 437.64705700683595, 445.9673432617188], [7, 187.884, 214.2, 438.47908563232426, 447.63140051269534], [7, 250.92, 273.564, 438.47908563232426, 447.63140051269534], [7, 307.836, 331.092, 438.47908563232426, 447.63140051269534], [7, 365.364, 388.008, 437.64705700683595, 445.9673432617188], [7, 64.26, 83.844, 447.63140051269534, 455.9516867675781], [7, 199.512, 214.2, 448.4634291381836, 457.6157440185547], [7, 307.836, 331.092, 448.4634291381836, 457.6157440185547], [7, 64.26, 83.844, 458.44777264404297, 465.9360302734375], [7, 175.644, 214.2, 458.44777264404297, 467.60008752441405], [7, 244.79999999999998, 273.564, 458.44777264404297, 467.60008752441405], [7, 64.26, 118.728, 479.24848828125, 487.5687745361328], [7, 153.612, 214.2, 479.24848828125, 488.4008031616211], [7, 250.92, 273.564, 479.24848828125, 488.4008031616211], [7, 307.836, 331.092, 479.24848828125, 488.4008031616211], [7, 359.856, 388.008, 479.24848828125, 487.5687745361328], [7, 64.26, 170.136, 490.0648604125977, 499.21717529296876], [7, 187.884, 214.2, 490.0648604125977, 499.21717529296876], [7, 302.94, 331.092, 490.0648604125977, 499.21717529296876], [7, 64.26, 118.728, 500.8812325439453, 509.20151879882815], [7, 153.612, 214.2, 500.8812325439453, 510.0335474243164], [7, 250.92, 273.564, 500.8812325439453, 510.0335474243164], [7, 307.836, 331.092, 500.8812325439453, 510.0335474243164], [7, 359.856, 388.008, 500.8812325439453, 509.20151879882815], [7, 64.26, 123.624, 511.697604675293, 519.1858623046875], [7, 153.612, 214.2, 511.697604675293, 520.8499195556641], [7, 250.92, 273.564, 511.697604675293, 520.8499195556641], [7, 307.836, 331.092, 511.697604675293, 520.8499195556641], [7, 365.364, 388.008, 511.697604675293, 519.1858623046875], [7, 64.26, 118.728, 521.6819481811524, 530.0022344360352], [7, 153.612, 214.2, 521.6819481811524, 530.8342630615234], [7, 244.79999999999998, 273.564, 521.6819481811524, 530.8342630615234], [7, 302.94, 331.092, 521.6819481811524, 530.8342630615234], [7, 359.856, 388.008, 521.6819481811524, 530.0022344360352], [7, 64.26, 111.996, 532.4983203125, 540.8186065673829], [7, 153.612, 214.2, 532.4983203125, 541.6506351928712], [7, 307.836, 331.092, 532.4983203125, 541.6506351928712], [7, 64.26, 129.132, 543.3146924438477, 551.6349786987305], [7, 153.612, 214.2, 543.3146924438477, 552.4670073242188], [7, 307.836, 331.092, 543.3146924438477, 552.4670073242188], [7, 65.484, 97.92, 573.2677229614258, 586.5801809692383], [7, 65.484, 227.052, 595.7324958496093, 605.7168393554688], [7, 65.484, 145.656, 605.7168393554688, 615.7011828613281], [8, 231.33599999999998, 420.444, 69.52553833007812, 87.52038354492188], [8, 231.33599999999998, 420.444, 87.52038354492188, 94.06396362304687], [8, 269.28, 329.256, 103.06138623046876, 118.60238891601563], [8, 83.844, 111.996, 124.328021484375, 134.96133911132813], [8, 83.844, 200.736, 134.96133911132813, 145.59465673828126], [8, 83.844, 223.992, 145.59465673828126, 155.41002685546874], [8, 300.492, 340.884, 121.0562314453125, 131.68954907226563], [8, 300.492, 452.268, 131.68954907226563, 141.50491918945312], [8, 300.492, 435.132, 141.50491918945312, 152.13823681640625], [8, 110.16, 143.82, 166.04334448242187, 175.04076708984377], [8, 214.2, 235.62, 166.04334448242187, 174.22281958007812], [8, 98.532, 107.1, 181.58434716796876, 188.9458747558594], [8, 102.204, 107.1, 202.03303491210937, 209.3945625], [8, 102.204, 107.1, 223.29967016601563, 230.66119775390627], [8, 153.0, 157.284, 229.025302734375, 236.38683032226564], [8, 174.42, 178.704, 229.025302734375, 236.38683032226564], [8, 195.84, 200.124, 229.025302734375, 236.38683032226564], [8, 217.26, 221.54399999999998, 229.025302734375, 236.38683032226564], [8, 238.06799999999998, 242.964, 229.025302734375, 236.38683032226564], [8, 259.488, 263.772, 229.025302734375, 236.38683032226564], [8, 218.484, 236.844, 274.01241577148437, 282.19189086914065], [8, 334.764, 339.048, 161.13565942382812, 168.49718701171875], [8, 343.332, 364.752, 163.589501953125, 172.5869245605469], [8, 334.764, 339.65999999999997, 198.76124487304688, 206.1227724609375], [8, 306.61199999999997, 318.852, 202.85098242187502, 211.03045751953127], [8, 306.61199999999997, 339.048, 235.56888281250002, 243.74835791015624], [8, 306.61199999999997, 317.016, 245.3842529296875, 253.56372802734376], [8, 402.69599999999997, 437.58, 262.5611506347656, 271.5585732421875], [8, 306.61199999999997, 347.616, 280.55599584960936, 288.73547094726564], [8, 367.812, 378.828, 279.7380483398438, 287.0995759277344], [8, 399.024, 410.04, 279.7380483398438, 287.0995759277344], [8, 430.236, 441.252, 279.7380483398438, 287.0995759277344], [8, 460.836, 472.464, 279.7380483398438, 287.0995759277344], [8, 492.65999999999997, 503.676, 279.7380483398438, 287.0995759277344], [8, 91.8, 111.384, 306.7303161621094, 315.72773876953124], [8, 91.8, 111.384, 316.5456862792969, 325.54310888671876], [8, 242.352, 274.176, 294.461103515625, 304.2764736328125], [8, 299.268, 320.688, 294.461103515625, 304.2764736328125], [8, 341.496, 367.812, 294.461103515625, 304.2764736328125], [8, 393.516, 415.548, 294.461103515625, 304.2764736328125], [8, 436.356, 462.67199999999997, 294.461103515625, 304.2764736328125], [8, 478.584, 510.408, 294.461103515625, 304.2764736328125], [8, 279.072, 320.688, 305.9123686523438, 314.09184375], [8, 279.072, 320.688, 316.5456862792969, 323.9072138671875], [8, 372.70799999999997, 414.936, 305.9123686523438, 314.09184375], [8, 372.70799999999997, 414.936, 316.5456862792969, 323.9072138671875], [8, 91.8, 103.428, 336.9943740234375, 344.35590161132814], [8, 214.81199999999998, 227.664, 336.1764265136719, 344.35590161132814], [8, 253.98, 275.4, 336.1764265136719, 344.35590161132814], [8, 299.88, 321.3, 336.1764265136719, 344.35590161132814], [8, 341.496, 368.424, 336.1764265136719, 344.35590161132814], [8, 91.8, 103.428, 346.809744140625, 354.17127172851565], [8, 193.392, 227.664, 345.99179663085937, 354.17127172851565], [8, 249.084, 275.4, 345.99179663085937, 354.17127172851565], [8, 295.596, 321.3, 345.99179663085937, 354.17127172851565], [8, 346.392, 368.424, 345.99179663085937, 354.17127172851565], [8, 91.8, 103.428, 356.6251142578125, 363.98664184570316], [8, 193.392, 227.664, 355.8071667480469, 363.98664184570316], [8, 253.98, 275.4, 355.8071667480469, 363.98664184570316], [8, 295.596, 321.3, 355.8071667480469, 363.98664184570316], [8, 341.496, 368.424, 355.8071667480469, 363.98664184570316], [8, 91.8, 124.848, 375.4379069824219, 382.7994345703125], [8, 214.81199999999998, 227.664, 374.61995947265626, 382.7994345703125], [8, 253.98, 275.4, 374.61995947265626, 382.7994345703125], [8, 299.88, 321.3, 374.61995947265626, 382.7994345703125], [8, 346.392, 368.424, 374.61995947265626, 382.7994345703125], [8, 392.904, 414.936, 374.61995947265626, 382.7994345703125], [8, 440.64, 462.67199999999997, 374.61995947265626, 382.7994345703125], [8, 488.376, 510.408, 374.61995947265626, 382.7994345703125], [8, 91.8, 109.548, 385.25327709960936, 392.6148046875], [8, 214.81199999999998, 227.664, 384.4353295898438, 392.6148046875], [8, 253.98, 275.4, 384.4353295898438, 392.6148046875], [8, 299.88, 321.3, 384.4353295898438, 392.6148046875], [8, 346.392, 368.424, 384.4353295898438, 392.6148046875], [8, 91.8, 104.03999999999999, 395.0686472167969, 402.4301748046875], [8, 214.81199999999998, 227.664, 394.2506997070313, 402.4301748046875], [8, 253.98, 275.4, 394.2506997070313, 402.4301748046875], [8, 299.88, 321.3, 394.2506997070313, 402.4301748046875], [8, 346.392, 368.424, 394.2506997070313, 402.4301748046875], [8, 91.8, 110.16, 413.88143994140626, 421.2429675292969], [8, 214.81199999999998, 227.664, 413.0634924316406, 421.2429675292969], [8, 253.98, 275.4, 413.0634924316406, 421.2429675292969], [8, 299.88, 321.3, 413.0634924316406, 421.2429675292969], [8, 346.392, 368.424, 413.0634924316406, 421.2429675292969], [8, 392.904, 414.936, 413.0634924316406, 421.2429675292969], [8, 440.64, 462.67199999999997, 413.0634924316406, 421.2429675292969], [8, 488.376, 510.408, 413.0634924316406, 421.2429675292969], [8, 91.8, 119.952, 423.69681005859377, 431.0583376464844], [8, 214.81199999999998, 227.664, 422.8788625488281, 431.0583376464844], [8, 253.98, 275.4, 422.8788625488281, 431.0583376464844], [8, 299.88, 321.3, 422.8788625488281, 431.0583376464844], [8, 346.392, 368.424, 422.8788625488281, 431.0583376464844], [8, 392.904, 414.936, 422.8788625488281, 431.0583376464844], [8, 440.64, 462.67199999999997, 422.8788625488281, 431.0583376464844], [8, 488.376, 510.408, 422.8788625488281, 431.0583376464844], [8, 91.8, 152.388, 433.5121801757813, 440.8737077636719], [8, 214.81199999999998, 227.664, 432.69423266601564, 440.8737077636719], [8, 295.596, 321.3, 432.69423266601564, 440.8737077636719], [8, 388.008, 414.936, 432.69423266601564, 440.8737077636719], [8, 493.272, 510.408, 432.69423266601564, 440.8737077636719], [8, 91.8, 167.688, 443.32755029296874, 450.6890778808594], [8, 214.81199999999998, 227.664, 442.50960278320315, 450.6890778808594], [8, 249.084, 275.4, 442.50960278320315, 450.6890778808594], [8, 295.596, 321.3, 442.50960278320315, 450.6890778808594], [8, 346.392, 368.424, 442.50960278320315, 450.6890778808594], [8, 388.008, 414.936, 442.50960278320315, 450.6890778808594], [8, 440.64, 462.67199999999997, 442.50960278320315, 450.6890778808594], [8, 493.272, 510.408, 442.50960278320315, 450.6890778808594], [8, 91.8, 110.16, 453.14292041015625, 460.5044479980469], [8, 204.408, 227.664, 452.32497290039066, 460.5044479980469], [8, 253.98, 275.4, 452.32497290039066, 460.5044479980469], [8, 299.88, 321.3, 452.32497290039066, 460.5044479980469], [8, 346.392, 368.424, 452.32497290039066, 460.5044479980469], [8, 392.904, 414.936, 452.32497290039066, 460.5044479980469], [8, 440.64, 462.67199999999997, 452.32497290039066, 460.5044479980469], [8, 488.376, 510.408, 452.32497290039066, 460.5044479980469], [8, 91.8, 124.848, 462.95829052734376, 470.3198181152344], [8, 204.408, 227.664, 462.1403430175781, 470.3198181152344], [8, 253.98, 275.4, 462.1403430175781, 470.3198181152344], [8, 299.88, 321.3, 462.1403430175781, 470.3198181152344], [8, 346.392, 368.424, 462.1403430175781, 470.3198181152344], [8, 392.904, 414.936, 462.1403430175781, 470.3198181152344], [8, 440.64, 462.67199999999997, 462.1403430175781, 470.3198181152344], [8, 488.376, 510.408, 462.1403430175781, 470.3198181152344], [8, 91.8, 124.848, 472.7736606445313, 480.1351882324219], [8, 204.408, 227.664, 471.95571313476563, 480.1351882324219], [8, 253.98, 275.4, 471.95571313476563, 480.1351882324219], [8, 299.88, 321.3, 471.95571313476563, 480.1351882324219], [8, 346.392, 368.424, 471.95571313476563, 480.1351882324219], [8, 392.904, 414.936, 471.95571313476563, 480.1351882324219], [8, 440.64, 462.67199999999997, 471.95571313476563, 480.1351882324219], [8, 488.376, 510.408, 471.95571313476563, 480.1351882324219], [8, 91.8, 124.848, 482.5890307617188, 489.95055834960937], [8, 204.408, 227.664, 481.77108325195314, 489.95055834960937], [8, 253.98, 275.4, 481.77108325195314, 489.95055834960937], [8, 299.88, 321.3, 481.77108325195314, 489.95055834960937], [8, 346.392, 368.424, 481.77108325195314, 489.95055834960937], [8, 392.904, 414.936, 481.77108325195314, 489.95055834960937], [8, 440.64, 462.67199999999997, 481.77108325195314, 489.95055834960937], [8, 488.376, 510.408, 481.77108325195314, 489.95055834960937], [8, 91.8, 146.88, 492.40440087890624, 499.7659284667969], [8, 204.408, 227.664, 491.58645336914066, 499.7659284667969], [8, 253.98, 275.4, 491.58645336914066, 499.7659284667969], [8, 299.88, 321.3, 491.58645336914066, 499.7659284667969], [8, 346.392, 368.424, 491.58645336914066, 499.7659284667969], [8, 392.904, 414.936, 491.58645336914066, 499.7659284667969], [8, 440.64, 462.67199999999997, 491.58645336914066, 499.7659284667969], [8, 488.376, 510.408, 491.58645336914066, 499.7659284667969], [8, 91.8, 110.16, 502.21977099609376, 509.5812985839844], [8, 214.81199999999998, 227.664, 501.4018234863281, 509.5812985839844], [8, 299.88, 321.3, 501.4018234863281, 509.5812985839844], [8, 392.904, 414.936, 501.4018234863281, 509.5812985839844], [8, 488.376, 510.408, 501.4018234863281, 509.5812985839844], [8, 91.8, 203.184, 511.2171936035156, 519.3966687011718], [8, 214.81199999999998, 227.664, 510.39924609375004, 519.3966687011718], [8, 299.88, 321.3, 510.39924609375004, 519.3966687011718], [8, 392.904, 414.936, 510.39924609375004, 519.3966687011718], [8, 488.376, 510.408, 510.39924609375004, 519.3966687011718], [8, 93.024, 110.16, 530.029986328125, 536.57356640625], [8, 193.392, 227.664, 529.2120388183594, 537.3915139160157], [8, 249.084, 275.4, 529.2120388183594, 537.3915139160157], [8, 56.916, 88.128, 559.4760966796875, 572.5632568359375], [8, 63.647999999999996, 253.98, 578.2888894042969, 590.5581020507813], [8, 63.647999999999996, 157.284, 590.5581020507813, 602.8273146972656], [8, 63.647999999999996, 226.44, 614.2785798339844, 626.5477924804687], [8, 63.647999999999996, 179.316, 626.5477924804687, 638.8170051269532], [8, 63.647999999999996, 225.216, 638.8170051269532, 651.0862177734375], [8, 420.444, 467.568, 740.2424963378907, 755.7834990234376], [8, 420.444, 467.568, 768.8706591796876, 783.5937143554688]]
2026-08-10 11:27:56,275 INFO     29 [qwen-vl-text] ═══ DONE ═══ 341 positions, pages=2, time=101.4s
2026-08-10 11:27:56,290 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:27:56,290 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:27:56,291 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:27:56,291 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:27:56.291+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 21, "failed": 0, "current": {"ba5d751a94ad11f1bd9827cf206dfa2d": {"id": "ba5d751a94ad11f1bd9827cf206dfa2d", "doc_id": "b9a7e47a94ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360930217, "task_type": "dataflow", "root_trace_id": "2d4fcd13324b447999508dc50afac2e4", "root_traceparent": "00-2d4fcd13324b447999508dc50afac2e4-817dc24fdd0315e5-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:27:56,301 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:27:56,301 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:27:57,595 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:27:57,605 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:27:57,605 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "626 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-10 11:27:57,605 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:27:57,607 INFO     29 [ChunkMerger] Merged 4 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 11:27:57,619 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:27:57,619 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "4 items, types={'PrescriptionRecord': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 1}", "name": "LXQI222.pdf"}
2026-08-10 11:27:57,619 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:27:57,779 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786360933803, 'update_date': datetime.datetime(2026, 8, 10, 11, 22, 13), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 918278, 'status': '1'}
2026-08-10 11:27:58,026 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=亦康互联网医院
普通
处方
已使用
已使用
已使用
联
处方笺
已使用
NO.:
2025-12-05
已使用
姓名：
性别：女处方专用章
年龄：72岁
已使用
费别：自费
科别：内科
已使用
临床诊断：支气管哮喘
已使用
Rp：
已使用
沙美特罗替卡松吸入粉雾剂
已使用
50μg:250μg*60泡
x 3盒
用法用量：
口腔吸入,一日两次,一次1.0揿;
已使用
补充说明：处方超7日为病情需要
已使用
医师：邢伟
审核：张艳梅
处方金额：
药房审核：
药房调配：
药房核对：
药房发药：
注：处方自开具日起3日内有效。
---
出院记录
姓名：
床号：23-03床
病历号：0
科室：呼吸与危重医学科医生站
姓名：
性别：女
年龄：72岁
民族：汉族
病历号：00
科室：呼吸与危重医学科医生站
入院日期：2025-10-30 14:34
住院天数：8
出院日期：2025-11-07 11:44
籍贯：贵州省贵阳市
职业：退休人员
单位：贵阳供电局
住址：中国贵州省贵阳
入院情况：
李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无
明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯
血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治
疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1
周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门
诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体
重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病
史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无
中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学
历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗
史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已
故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患
者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，
血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。
心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检
查：暂无
入院诊断：1.支气管哮喘急性发作期
诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床
检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1
2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝
功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中
心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中
心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心)：钾(K) 4.47mmol/L 白介素-6(IL-6) 2.10pg/ml
肌酐(Cr) 57.90μmol/L C反应蛋白(CRP) 0.48mg/L 丙氨酸氨基转移酶(ALT) 17.50U/L 天冬氨酸氨基转移
酶(AST) 25.40U/L。2025-10-30 17:34 DIC全套(临床检验中心)：纤维蛋白原(Fg) 5.09g/L D-二聚体(DD)
0.75μg/mL DDU。2025-10-30 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-3
0 15:46 静态心电图(含十二通道加收)：窦性心律 HR 69 bpm。2025-10-31 13:11 胸部CT平扫：1、考
虑双肺新增少许感染灶，以左肺为著，请结合临床并复查。 2、双肺尖多发结节灶、纤维化灶，邻近双侧
1/3
贵州醫科大學附屬醫院
THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY
出院记录
姓名：
床号：23-03床
病历号：
科室：呼吸与危重医学科医生站
胸膜局限性增厚，考虑陈旧性病变，建议随诊复查。 3、左肺下叶外基底段局部间质性改变，其内支气管
扩张；双肺支气管壁稍增厚，考虑慢性支气管炎，请结合临床并复查。 4、左肺下叶微小结节，建议随诊
复查。 5、纵隔内淋巴结稍增大，建议随诊复查。 6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走
行欠佳。 7、肝内囊性灶，建议超声随诊复查。2025-10-31 14:35 肺通气功能测定及支气管舒张试验：1.
中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+) 2025-10-31 12:33。传染病筛查
三项：阴性。2025-10-31 13:12 乙肝5项(定量)：阴性。2025-10-31 15:12 大便常规(不含寄生虫)(临
床检验中心)：未见异常。2025-10-31 15:10 尿液检查(尿液分析+尿有形成分)：未见异常。2025-10-31
14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴
定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支
气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症
治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。
出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小
结节；5.肝囊肿。
出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查
体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊
区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。
VTE评估：
床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31
14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴
定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支
气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症
治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。
出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小
结节；5.肝囊肿。
出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查
体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊
区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。
VTE评估：
Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：
出院医嘱：
1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治
疗，定期复查肺功能，呼吸科门诊随诊；
2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。
3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。
4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。
手术名称：
无
出院结果：好转
医生签名：
日期：2025-11-07 11:44
---
入院记录
姓名：
床号：23-03床
病历号：0
科室：呼吸与危重医学科医生
站
姓名：
性别：女
年龄：72岁
出生地：贵州省贵阳市
职业：退休人员
民族：汉族
婚姻：已婚
联系地址：中国贵州省贵阳市
入院时间：2025-10-30 14:34
病史陈述者：本人
主诉：咳嗽、咳痰5年，加重1周
现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，
不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管
哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感
和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治
就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二
便如常，近1年体重减少4kg。
既往史：
患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染
病；食物、药物过敏无；无外伤史：无手术史：无输血史：无中毒史：无长期用药史：无可能成瘾药物。疫
苗接种史不详
个人史：
出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长
地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物
质接触史。
婚育史：
已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。
月经史：
初潮年龄17岁
经期3-4天
绝经年龄53岁 月经及白带情况：正常
月经周期30天
家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否
认二系三代有遗传病史。患者否认有遗传倾向的疾病。
体格检查
生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60
体格检查
生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体
重：44kg，腰围：cm，BMI：18.8 kg/m²
一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常
表情：正常体位：自主体位步态：平稳配合检查：配合
皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无
皮疹：无紫癜：无
1/3
贵州醫科大學附属醫院
THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY
入院记录
姓名：
床号：23-03床
病历号
科室：呼吸与危重医学科医生
站
水肿：无脱水现象：无松紧度：适中
温度：适中出汗：无显性出汗瘢痕：无感染：无
头颅：大小：正常畸形：无包块：无
凹陷：无压痛：无
眼：眼睑：无水肿结膜：无充血巩膜：无黄染
眼球四个象限运动：左眼：正常右眼：正常
眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆
对光反射：左眼：灵敏右眼：灵敏
鼻：外形：正常其他异常：无鼻旁窦压痛：无
口：唇：无紫绀粘膜：无充血腮腺导管开口：正常
舌：伸舌居中牙龈：无肿胀龋齿：无
咽喉：扁桃体：正常咽：无充血声音：正常
淋巴：淋巴结：全身浅表淋巴结未及肿大
颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张
气管：居中颈静脉回流征：无
甲状腺：无肿大
眼球四个象限运动：左眼：正常 右眼：正常
眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆
对光反射：左眼：灵敏 右眼：灵敏
鼻：外形：正常 其他异常：无 鼻旁窦压痛：无
口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常
舌：伸舌居中 牙龈：无肿胀 龋齿：无
咽 喉：扁桃体：正常 咽：无充血 声音：正常
淋巴 巴：淋巴结：全身浅表淋巴结未及肿大
颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张
气管：居中 颈静脉回流征：无
甲状腺：无肿大
胸部 部：胸廓：无畸形 乳房：
肺 部：视诊：呼吸运动
触诊：
叩诊：
听诊：
语音传导
心 脏：视诊：
触诊：心尖搏动
叩诊：
心界
右(cm)
肋间
左(cm)
2
2
2
3
(左锁骨中线距胸骨线7.5cm)
听诊：心率：92次/分 心律：齐 心音：未闻及异常心
额外心音：无 杂音：无 心包摩擦感：
周围血管：异常血管征：无
腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出
其他异常：无
触诊：腹壁：柔软 压痛：无
2/3
站
反跳痛：无
液波振颤：无 振水声：无
腹部包块：无
肝：肋下未及
胆囊：未触及 Murphy征：阴性
脾：未触及
叩诊：肝浊音界：正常 移动性浊音：无
肾区叩痛：无
听诊：肠鸣音：正常 肠鸣音频率：4次/分
气过水音：无 血管杂音：无
肛门直肠：未检
生殖器：未检
脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限
压痛，叩痛：无
杵状指趾：无
神经系统：腹壁反射：正常 肢体瘫痪：无
肌张力：正常 肌力：V级
肱二头肌反射：正常 Hoffman征：阴性
膝腱反射：正常 Kernig征：阴性
跟腱反射：正常 Babinski征：阴性
其他：无
补充及专科情况
双肺呼吸音清，未闻及干湿性啰音。
辅助检查：暂无
VTE评估：
Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：
入院诊断：1.支气管哮喘急性发作期
医师签名：
日期：2025-10-30 16:38
---
肺功能通气阻力检查报告
姓名：
性别：女
身高：151 cm
病历号：
年龄：72 Years
体重：46 kg
Flow [L/s]
F/V ex
10
5
0
2
4
6
F/V in
8
Vol [L]
6
4
1
Vol%Vcmax
100
Vcmax
20
0
Time [s]
0
1
2
3
4
5
6
2.0
R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]
1.5
1.0
0.5
0.0
0.4
0.2
0.2
0.4
F [Hz]
5
10
15
20
25
30
35
日期
时间
预计值
实测值
实/预
25/10/31
14:29:33
MV
[L/min]
6.57
11.52
175.3
VT
[L]
0.33
0.79
239.6
BF
[1/min]
20.00
14.63
73.1
VC MAX
[L]
2.03
1.48
73.0
ERV
[L]
0.57
0.14
25.5
IC
[L]
1.46
1.34
91.6
FVC
[L]
1.93
1.44
74.8
FEV 1
[L]
1.56
0.91
58.4
FEV 1 % FVC
[%]
63.38
FEV 1 % VC MAX
[%]
75.42
61.67
81.8
PEF
[L/s]
5.04
2.51
49.8
MEF 75
[L/s]
4.66
1.54
33.1
MEF 50
[L/s]
3.06
0.56
18.2
MEF 25
[L/s]
0.90
0.22
24.6
MEF 75/25
[L/s]
2.36
0.50
21.1
FET
[s]
4.91
LFV
[L/min]
73.10
Z at 5 Hz
[kPa/(L/s)]
0.43
0.58
135.7
Resonant frequency
[1/s]
30.00
R at 5 Hz
[kPa/(L/s)]
0.41
0.57
137.2
R nt 20 Hz
[kPa/(L/s)]
0.35
0.34
95.3
X at 5 Hz
[kPa/(L/s)]
-0.11
-0.12
112.5
Rcentral
[kPa/(L/s)]
0.12
Peripheral
[kPa/(L/s)]
0.40
结论：
1.中重度混合性肺通气功能障碍
2.（阻力增加
审核者专用章
检查者：王美锦
贵州医科大学附属医院
THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY
对比试验
姓名：
性别：女
身高：151 cm
病历号：
年龄：72 Years
体重：46 kg
Flow [L/s]
F/V ex
10
5
0
2
3
4
5
6
7
F/V in
6
Vol [L]
4
TLC
ER,pleth2
RV
Time [min]
Pred Act 0.0
0.2
0.4
0.6
0.8
1.0
日期
时间
预计值
前次
前/预
后次
后/预
改善率
25/10/31
14:29:33
25/10/31
14:53:10
VT
[L]
0.33
0.79
239.6
BF
[1/min]
20.00
14.63
73.1
MV
[L/min]
6.57
11.52
175.3
VC MAX
[L]
2.03
1.48
73.0
1.66
81.9
12.2
ERV
[L]
0.57
0.14
25.5
IC
[L]
1.46
1.34
91.6
FVC
[L]
1.93
1.44
74.8
1.66
86.2
15.3
FEV 1
[L]
1.56
0.91
58.4
1.08
68.8
17.8
FEV 1 % FVC
[%]
63.38
64.76
2.2
FEV 1 % VC MAX
[%]
75.42
61.67
81.8
64.76
85.9
5.0
PEF
[L/s]
5.04
2.51
49.8
3.35
66.5
33.6
MEF 75
[L/s]
4.66
1.54
33.1
1.72
36.8
11.3
MEF 50
[L/s]
3.06
0.56
18.2
0.83
27.1
49.1
MEF 25
[L/s]
0.90
0.22
24.6
0.36
39.8
62.1
MMEF 75/25
[L/s]
2.36
0.50
21.1
0.47
20.0
-4.9
FET
[s]
4.91
4.88
-0.6
V backextrapol. % FVC
[%]
3.85
4.39
13.9
MVV
[L/min]
73.10
结论：
1.中重度混合性肺通气功能障碍
2.气道阻力增加
3.支气管舒张试验阳性 (+)
吸入沙丁胺醇400μg
FVC上升15.3%，增加220ml；
审核者：
检查者：
2026-08-10 11:27:58,592 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:27:58,592 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "4 items, types={'PrescriptionRecord': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 1}", "name": "LXQI222.pdf", "embedding_token_consumption": 6207}
2026-08-10 11:27:58,592 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:27:58,737 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:27:58,737 INFO     29 [Trace] task=ba5d751a | doc=LXQI222.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":4,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 11:27:58,740 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:27:58,740 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:27:58,740 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:27:58,740 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:27:58,747 INFO     29 set_progress(ba5d751a94ad11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:27:58 [DOC Engine]:
Start to index...
2026-08-10 11:27:58,771 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 11:27:58,775 INFO     29 set_progress(ba5d751a94ad11f1bd9827cf206dfa2d), progress: 0.8250000000000001, progress_msg: 
2026-08-10 11:27:58,786 INFO     29 set_progress(ba5d751a94ad11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:27:58 Indexing done (0.04s). Task done (333.01s)
2026-08-10 11:27:58,792 INFO     29 [Done], chunks(4), token(6207), elapsed:333.01
2026-08-10 11:27:58,934 INFO     29 handle_task done for task {"id": "ba5d751a94ad11f1bd9827cf206dfa2d", "doc_id": "b9a7e47a94ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786360930217, "task_type": "dataflow", "root_trace_id": "2d4fcd13324b447999508dc50afac2e4", "root_traceparent": "00-2d4fcd13324b447999508dc50afac2e4-817dc24fdd0315e5-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
