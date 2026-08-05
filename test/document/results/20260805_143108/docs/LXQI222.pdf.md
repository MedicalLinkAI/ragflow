# 基准结果：LXQI222.pdf

## 基本信息

- 文件：`LXQI222.pdf`
- 大小：62937.7 KB
- PDF 总页数：10
- doc_id：`c9872b6c908911f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:14  完成时间：2026-08-05T14:31:14  耗时：0.9s
- progress_msg：`05:02:30 Indexing done (0.04s). Task done (423.34s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | a80da833 | 4 | 1-4 | 入院记录 姓名： 床号：23-03床 病历号：0 科室：呼吸与危重医学科医生 站 |
| 2 | b6c665d5 | 3 | 5-7 | 出院记录 姓名： 床号：23-03床 病历号：0 科室：呼吸与危重医学科医生站  |
| 3 | f5ee14b3 | 2 | 8-9 | 肺功能通气阻力检查报告 姓名： 性别：女 身高：151 cm 病历号： 年龄：7 |
| 4 | d62a0815 | 1 | 10-10 | 亦康互联网医院 普通 处方 已使用 已使用 已使用 联 处方笺 已使用 NO.: |

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
- ChunkMerger：`{"found": true, "merged": 4, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 4}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 05:02:29,237 INFO     29 [ChunkMerger] Merged 4 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 04:54:50,917 INFO     29 handle_task begin for task {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 04:54:51,159 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 04:54:51,201 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 04:54:51,241 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 04:54:51,241 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 04:54:51,252 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 04:54:51,252 INFO     29 ============================================================
2026-08-05 04:54:51,252 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 04:54:51,252 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 04:54:51,252 INFO     29 ============================================================
2026-08-05 04:54:51,252 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 04:54:51,252 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 04:54:51,258 INFO     29 No torch found.
2026-08-05 04:54:53,838 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=10
2026-08-05 04:54:53,957 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1110594, prompt_len=644
2026-08-05 04:54:55,087 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 04:54:55,087 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-05 04:54:55,094 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1110594, prompt_len=401
2026-08-05 04:55:00,033 INFO     29 [qwen-vl-parser] text API response (len=936):
["入院记录", "姓名：", "床号：23-03床", "病历号：0", "科室：呼吸与危重医学科医生", "站", "姓名：", "性别：女", "年龄：72岁", "出生地：贵州省贵阳市", "职业：退休人员", "民族：汉族", "婚姻：已婚", "联系地址：中国贵州省贵阳市", "入院时间：2025-10-30 14:34", "病史陈述者：本人", "主诉：咳嗽、咳痰5年，加重1周", "现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，", "不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管", "哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感", "和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治", "就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二", "便如常，近1年体重减少4kg。", "既往史：", "患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染", "病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫", "苗接种史不详", "个人史：", "出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长", "地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物", "质接触史。", "婚育史：", "已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。", "月经史：", "初潮年龄17岁 经期3-4天 绝经年龄53岁 月经及白带情况：正常", "月经周期30天", "家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否", "认二系三代有遗传病史。患者否认有遗传倾向的疾病。", "体格检查", "生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60"]
2026-08-05 04:55:00,034 INFO     29 [qwen-vl-parser] page=1 text: 40 lines (bbox 0-39)
2026-08-05 04:55:00,034 INFO     29 [qwen-vl-parser] page=1 text: 40 sections
2026-08-05 04:55:00,148 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935099, prompt_len=644
2026-08-05 04:55:02,082 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:55:02,083 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 04:55:02,098 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935099, prompt_len=401
2026-08-05 04:55:02,774 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:55:02.774+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:55:05,799 INFO     29 [qwen-vl-parser] text API response (len=683):
["体格检查", "生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体", "重：44kg，腰围：cm，BMI：18.8 kg/m²", "一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常", "表情：正常体位：自主体位步态：平稳配合检查：配合", "皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无", "皮疹：无紫癜：无", "1/3", "贵州醫科大學附属醫院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "入院记录", "姓名：", "床号：23-03床", "病历号", "科室：呼吸与危重医学科医生", "站", "水肿：无脱水现象：无松紧度：适中", "温度：适中出汗：无显性出汗瘢痕：无感染：无", "头颅：大小：正常畸形：无包块：无", "凹陷：无压痛：无", "眼：眼睑：无水肿结膜：无充血巩膜：无黄染", "眼球四个象限运动：左眼：正常右眼：正常", "眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆", "对光反射：左眼：灵敏右眼：灵敏", "鼻：外形：正常其他异常：无鼻旁窦压痛：无", "口：唇：无紫绀粘膜：无充血腮腺导管开口：正常", "舌：伸舌居中牙龈：无肿胀龋齿：无", "咽喉：扁桃体：正常咽：无充血声音：正常", "淋巴：淋巴结：全身浅表淋巴结未及肿大", "颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张", "气管：居中颈静脉回流征：无", "甲状腺：无肿大"]
2026-08-05 04:55:05,799 INFO     29 [qwen-vl-parser] page=2 text: 32 lines (bbox 40-71)
2026-08-05 04:55:05,799 INFO     29 [qwen-vl-parser] page=2 text: 32 sections
2026-08-05 04:55:05,909 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=753919, prompt_len=644
2026-08-05 04:55:06,937 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:55:06,938 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 04:55:06,949 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=753919, prompt_len=401
2026-08-05 04:55:10,460 INFO     29 [qwen-vl-parser] text API response (len=594):
["眼球四个象限运动：左眼：正常 右眼：正常", "眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆", "对光反射：左眼：灵敏 右眼：灵敏", "鼻：外形：正常 其他异常：无 鼻旁窦压痛：无", "口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常", "舌：伸舌居中 牙龈：无肿胀 龋齿：无", "咽 喉：扁桃体：正常 咽：无充血 声音：正常", "淋巴 巴：淋巴结：全身浅表淋巴结未及肿大", "颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张", "气管：居中 颈静脉回流征：无", "甲状腺：无肿大", "胸部 部：胸廓：无畸形 乳房：", "肺 部：视诊：呼吸运动", "触诊：", "叩诊：", "听诊：", "语音传导", "心 脏：视诊：", "触诊：心尖搏动：正常 振颤：无 心包摩擦感：无", "叩诊：", "第五肋间内0.5cm", "心界", "右(cm)", "肋间", "左(cm)", "2", "2", "2", "1", "3", "(左锁骨中线距胸骨线7.5cm)", "听诊：心率：92次/分 心律：齐 心音：未闻及异常心", "额外心音：无 杂音：无 心包摩擦音：", "周围血管：异常血管征：无", "腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出", "其他异常：无", "触诊：腹壁：柔软 压痛：无", "2/3"]
2026-08-05 04:55:10,461 INFO     29 [qwen-vl-parser] page=3 text: 38 lines (bbox 72-109)
2026-08-05 04:55:10,461 INFO     29 [qwen-vl-parser] page=3 text: 38 sections
2026-08-05 04:55:10,561 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=654032, prompt_len=644
2026-08-05 04:55:11,672 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-10-30"
}
```
2026-08-05 04:55:11,672 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-10-30
2026-08-05 04:55:11,680 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=654032, prompt_len=401
2026-08-05 04:55:15,643 INFO     29 [qwen-vl-parser] text API response (len=488):
["站", "反跳痛：无", "液波振颤：无 振水声：无", "腹部包块：无", "肝：肋下未及", "胆囊：未触及 Murphy征：阴性", "脾：未触及", "叩诊：肝浊音界：正常 移动性浊音：无", "肾区叩痛：无", "听诊：肠鸣音：正常 肠鸣音频率：4次/分", "气过水音：无 血管杂音：无", "肛门直肠：未检", "生殖器：未检", "脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限", "压痛，叩痛：无", "杵状指趾：无", "神经系统：腹壁反射：正常 肢体瘫痪：无", "肌张力：正常 肌力：V级", "肱二头肌反射：正常 Hoffman征：阴性", "膝腱反射：正常 Kernig征：阴性", "跟腱反射：正常Babinski征：阴性", "其他：无", "补充及专科情况", "双肺呼吸音清，未闻及干湿性啰音。", "辅助检查：暂无", "VTE评估：", "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "入院诊断：1.支气管哮喘急性发作期", "医师签名：", "日期：2025-10-30 16:38"]
2026-08-05 04:55:15,643 INFO     29 [qwen-vl-parser] page=4 text: 30 lines (bbox 110-139)
2026-08-05 04:55:15,643 INFO     29 [qwen-vl-parser] page=4 text: 30 sections
2026-08-05 04:55:15,879 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1934597, prompt_len=644
2026-08-05 04:55:17,147 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:55:17,148 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 04:55:17,156 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1934597, prompt_len=401
2026-08-05 04:55:24,516 INFO     29 [qwen-vl-parser] text API response (len=1305):
["出院记录", "姓名：", "床号：23-03床", "病历号：0", "科室：呼吸与危重医学科医生站", "姓名：", "性别：女", "年龄：72岁", "民族：汉族", "病历号：00", "科室：呼吸与危重医学科医生站", "入院日期：2025-10-30 14:34", "住院天数：8", "出院日期：2025-11-07 11:44", "籍贯：贵州省贵阳市", "职业：退休人员", "单位：贵阳供电局", "住址：中国贵州省贵阳", "入院情况：", "李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无", "明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯", "血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治", "疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1", "周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门", "诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体", "重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病", "史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无", "中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学", "历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗", "史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已", "故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患", "者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，", "血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。", "心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检", "查：暂无", "入院诊断：1.支气管哮喘急性发作期", "诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床", "检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1", "2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝", "功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中"]
2026-08-05 04:55:24,517 INFO     29 [qwen-vl-parser] page=5 text: 40 lines (bbox 140-179)
2026-08-05 04:55:24,517 INFO     29 [qwen-vl-parser] page=5 text: 40 sections
2026-08-05 04:55:24,933 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2975581, prompt_len=644
2026-08-05 04:55:26,182 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 04:55:26,183 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 04:55:26,194 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2975581, prompt_len=401
2026-08-05 04:55:36,622 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:55:36.621+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:55:37,012 INFO     29 [qwen-vl-parser] text API response (len=1405):
["心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心):钾(K)4.47mmol/L白介素-6(IL-6)2.10pg/ml", "肌酐(Cr)57.90μmol/L C反应蛋白(CRP)0.48mg/L丙氨酸氨基转移酶(ALT)17.50U/L天冬氨酸氨基转移", "酶(AST)25.40U/L。2025-10-3017:34 DIC全套(临床检验中心):纤维蛋白原(Fg)5.09g/L D-二聚体(DD)", "0.75μg/mLDDU。2025-10-3015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3", "015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3113:11 胸部CT平扫:1、考虑双肺新增少许感染灶,以左肺为著,请结合临床并复查。2、双肺尖多发结节灶、纤维化灶,邻近双侧", "1/3", "贵州醫科大學附屬醫院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "出院记录", "姓名:", "床号:23-03床", "病历号:", "科室:呼吸与危重医学科医生站", "胸膜局限性增厚,考虑陈旧性病变,建议随诊复查。3、左肺下叶外基底段局部间质性改变,其内支气管", "扩张;双肺支气管壁稍增厚,考虑慢性支气管炎,请结合临床并复查。4、左肺下叶微小结节,建议随诊", "复查。5、纵隔内淋巴结稍增大,建议随诊复查。6、主动脉及冠状动脉硬化;胸椎退变,左侧第2前肋走", "行欠佳。7、肝内囊性灶,建议超声随诊复查。2025-10-3114:35肺通气功能测定及支气管舒张试验:1.", "中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+)2025-10-3112:33。传染病筛查", "三项:阴性。2025-10-3113:12乙肝5项(定量):阴性。2025-10-3115:12大便常规(不含寄生虫)(临", "床检验中心):未见异常。2025-10-3115:10尿液检查(尿液分析+尿有形成分):未见异常。2025-10-31", "14:37痰液革兰氏染色+抗酸染色+真菌(临床检验中心):未见异常。2025-11-0210:41痰细菌培养及鉴", "定:未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染,痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "气管等对症支持治疗,先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "治疗,经我科治疗后,患者病情较前好转,目前一般情况可,请示上级医师盾予今日办理出院。", "出院诊断:1.支气管哮喘急性发作期;2.社区获得性肺炎,非重症;3.慢性阻塞性肺疾病;4.左肺下叶小", "结节;5.肝囊肿。", "出院情况:患者咳嗽、咳痰、胸闷、气促好转,无呼吸困难,无畏寒、发热,无恶心、呕吐等不适。查", "体:生命体征平稳。全身皮肤黏膜、巩膜无黄染,双肺呼吸音清,未闻及干湿性啰音。律齐,各瓣膜听诊", "区未闻及病理性杂音,腹软,全腹无压痛及反跳痛,肝脾肋下未及,肝脾肋下未及,双下肢无水肿。", "VTE评估:"]
2026-08-05 04:55:37,012 INFO     29 [qwen-vl-parser] page=6 text: 30 lines (bbox 180-209)
2026-08-05 04:55:37,012 INFO     29 [qwen-vl-parser] page=6 text: 30 sections
2026-08-05 04:55:37,134 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102115, prompt_len=644
2026-08-05 04:55:38,199 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 04:55:38,199 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 04:55:38,211 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102115, prompt_len=401
2026-08-05 04:55:43,257 INFO     29 [qwen-vl-parser] text API response (len=909):
["床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31", "14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴", "定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。", "出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小", "结节；5.肝囊肿。", "出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查", "体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊", "区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。", "VTE评估：", "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "出院医嘱：", "1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治", "疗，定期复查肺功能，呼吸科门诊随诊；", "2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。", "3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。", "4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。", "手术名称：", "无", "出院结果：好转", "医生签名：", "日期：2025-11-07 11:44", "温馨提示", "尊敬的患者，出院后如您需复印住院资料，请关注以下温馨小提示：", "一、操作流程", "【方法一】", "1.请先打开微信“扫一扫”，扫描二维码，根据提示进行操作完成网上预约申请并回家等待。", "2/3"]
2026-08-05 04:55:43,257 INFO     29 [qwen-vl-parser] page=7 text: 29 lines (bbox 210-238)
2026-08-05 04:55:43,257 INFO     29 [qwen-vl-parser] page=7 text: 29 sections
2026-08-05 04:55:43,392 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038939, prompt_len=644
2026-08-05 04:55:45,029 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 04:55:45,029 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-05 04:55:45,035 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038939, prompt_len=401
2026-08-05 04:55:53,246 INFO     29 [qwen-vl-parser] text API response (len=1606):
["贵州医科大学附属医院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "肺功能通气阻力检查报告", "姓名：", "性别：女", "身高：151 cm", "病历号：", "年龄：72 Years", "体重：46 kg", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "F/V in", "8", "Vol [L]", "6", "4", "1", "Vol%Vcmax", "100", "Vcmax", "20", "0", "Time [s]", "0", "1", "2", "3", "4", "5", "6", "2.0", "R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]", "1.5", "1.0", "1.0", "0.5", "0.0", "0.4", "0.2", "0.2", "0.4", "F [Hz]", "5", "10", "15", "20", "25", "30", "35", "日期", "时间", "预计值", "实测值", "实/预", "25/10/31", "14:29:33", "MV", "[L/min]", "6.57", "11.52", "175.3", "VT", "[L]", "0.33", "0.79", "239.6", "BF", "[1/min]", "20.00", "14.63", "73.1", "VC MAX", "[L]", "2.03", "1.48", "73.0", "ERV", "[L]", "0.57", "0.14", "25.5", "IC", "[L]", "1.46", "1.34", "91.6", "FVC", "[L]", "1.93", "1.44", "74.8", "FEV 1", "[L]", "1.56", "0.91", "58.4", "FEV 1 % FVC", "[%]", "63.38", "FEV 1 % VC MAX", "[%]", "75.42", "61.67", "81.8", "PEF", "[L/s]", "5.04", "2.51", "49.8", "MEF 75", "[L/s]", "4.66", "1.54", "33.1", "MEF 50", "[L/s]", "3.06", "0.56", "18.2", "MEF 25", "[L/s]", "0.90", "0.22", "24.6", "MEF 75/25", "[L/s]", "2.36", "0.50", "21.1", "FET", "[s]", "4.91", "LFV", "[L/min]", "73.10", "Z at 5 Hz", "[kPa/(L/s)]", "0.43", "0.58", "135.7", "Resonant frequency", "[1/s]", "30.00", "R at 5 Hz", "[kPa/(L/s)]", "0.41", "0.57", "137.2", "R nt 20 Hz", "[kPa/(L/s)]", "0.35", "0.34", "95.3", "R at 5 Hz", "[kPa/(L/s)]", "-0.11", "-0.12", "112.5", "Rcentral", "[kPa/(L/s)]", "0.12", "Rperipheral", "[kPa/(L/s)]", "0.40", "结论：", "1.中重度混合性肺通气功能障碍", "2.（阻力增加", "审核者专用章", "检查者：王美锦"]
2026-08-05 04:55:53,247 INFO     29 [qwen-vl-parser] page=8 text: 175 lines (bbox 239-413)
2026-08-05 04:55:53,247 INFO     29 [qwen-vl-parser] page=8 text: 175 sections
2026-08-05 04:55:53,359 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=849726, prompt_len=644
2026-08-05 04:55:54,776 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-05"
}
```
2026-08-05 04:55:54,776 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=2025-04-05
2026-08-05 04:55:54,783 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=849726, prompt_len=756
2026-08-05 04:56:01,725 INFO     29 [qwen-vl-parser] table API response (len=1530):
\begin{tabular}{lcccccc}
\hline
\multicolumn{1}{c}{} & \multicolumn{1}{c}{预计值} & \multicolumn{1}{c}{前次} & \multicolumn{1}{c}{前/预} & \multicolumn{1}{c}{后次} & \multicolumn{1}{c}{后/预} & \multicolumn{1}{c}{改善率} \\
\multicolumn{1}{c}{日期} & \multicolumn{1}{c}{} & \multicolumn{1}{c}{25/10/31} & \multicolumn{1}{c}{} & \multicolumn{1}{c}{25/10/31} & \multicolumn{1}{c}{} & \multicolumn{1}{c}{} \\
\multicolumn{1}{c}{时间} & \multicolumn{1}{c}{} & \multicolumn{1}{c}{14:29:33} & \multicolumn{1}{c}{} & \multicolumn{1}{c}{14:53:10} & \multicolumn{1}{c}{} & \multicolumn{1}{c}{} \\
\hline
VT & [L] & 0.33 & 0.79 & 239.6 & & \\
BF & [1/min] & 20.00 & 14.63 & 73.1 & & \\
MV & [L/min] & 6.57 & 11.52 & 175.3 & & \\
VC MAX & [L] & 2.03 & 1.48 & 73.0 & 1.66 & 81.9 & 12.2 \\
ERV & [L] & 0.57 & 0.14 & 25.5 & & \\
IC & [L] & 1.46 & 1.34 & 91.6 & & \\
FVC & [L] & 1.93 & 1.44 & 74.8 & 1.66 & 86.2 & 15.3 \\
FEV 1 & [L] & 1.56 & 0.91 & 58.4 & 1.08 & 68.8 & 17.8 \\
FEV 1 \% FVC & [\%] & & 63.38 & & 64.76 & & 2.2 \\
FEV 1 \% VC MAX & [\%] & 75.42 & 61.67 & 81.8 & 64.76 & 85.9 & 5.0 \\
PEF & [L/s] & 5.04 & 2.51 & 49.8 & 3.35 & 66.5 & 33.6 \\
MEF 75 & [L/s] & 4.66 & 1.54 & 33.1 & 1.72 & 36.8 & 11.3 \\
MEF 50 & [L/s] & 3.06 & 0.56 & 18.2 & 0.83 & 27.1 & 49.1 \\
MEF 25 & [L/s] & 0.90 & 0.22 & 24.6 & 0.36 & 39.8 & 62.1 \\
MMEF 75/25 & [L/s] & 2.36 & 0.50 & 21.1 & 0.47 & 20.0 & -4.9 \\
FET & [s] & & 4.91 & & 4.88 & & -0.6 \\
V backextrapol. \% FVC & [\%] & & 3.85 & & 4.39 & & 13.9 \\
\hline
MVV & [L/min] & 73.10 & & & & & \\
\hline
\end{tabular}
2026-08-05 04:56:01,728 INFO     29 [qwen-vl-parser] page=9 table: 28 LaTeX lines (bbox 414-441)
2026-08-05 04:56:01,729 INFO     29 [qwen-vl-parser] page=9 table: 28 sections
2026-08-05 04:56:01,847 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910218, prompt_len=644
2026-08-05 04:56:03,046 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-05"}
```
2026-08-05 04:56:03,047 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2025-12-05
2026-08-05 04:56:03,052 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910218, prompt_len=401
2026-08-05 04:56:07,948 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:56:07.948+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:56:41,023 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:56:41.020+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:57:13,796 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:57:13.795+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:57:46,439 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:57:46.436+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:58:12,116 INFO     29 [qwen-vl-parser] text API response (len=28633):
["亦康互联网医院", "普通", "处方", "已使用", "已使用", "已使用", "联", "处方笺", "已使用", "NO.:", "2025-12-05", "已使用", "姓名：", "性别：女处方专用章", "年龄：72岁", "已使用", "费别：自费", "科别：内科", "已使用", "临床诊断：支气管哮喘", "已使用", "Rp：", "已使用", "沙美特罗替卡松吸入粉雾剂", "已使用", "50μg:250μg*60泡", "x 3盒", "已使用", "用法用量：", "口腔吸入,一日两次,一次1.0揿;", "已使用", "补充说明：处方超7日为病情需要", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使���", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "���使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已使用", "已
2026-08-05 04:58:12,137 INFO     29 [qwen-vl-parser] page=10 text: 4080 lines (bbox 442-4521)
2026-08-05 04:58:12,137 INFO     29 [qwen-vl-parser] page=10 text: 4080 sections
2026-08-05 04:58:12,137 INFO     29 [qwen-vl-parser] parse_pdf done: 4522 sections from 10 pages.
2026-08-05 04:58:12,150 INFO     29 Close text detector.
2026-08-05 04:58:12,503 INFO     29 Close text recognizer.
2026-08-05 04:58:12,820 INFO     29 Close recognizer.
2026-08-05 04:58:13,168 INFO     29 Close recognizer.
2026-08-05 04:58:13,578 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 04:58:13,579 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Parser:MedLink | outputs={"html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "json"}
2026-08-05 04:58:13,579 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 04:58:13,600 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:58:13,600 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 入院记录\n[BBOX-1] 姓名：\n[BBOX-2] 床号：23-03床\n[BBOX-3] 病历号：0\n[BBOX-4] 科室：呼吸与危重医学科医生\n[BBOX-5] 站\n[BBOX-6] 姓名：\n[BBOX-7] 性别：女\n[BBOX-8] 年龄：72岁\n[BBOX-9] 出生地：贵州省贵阳市\n[BBOX-10] 职业：退休人员\n[BBOX-11] 民族：汉族\n[BBOX-12] 婚姻：已婚\n[BBOX-13] 联系地址：中国贵州省贵阳市\n[BBOX-14] 入院时间：2025-10-30 14:34\n[BBOX-15] 病史陈述者：本人\n[BBOX-16] 主诉：咳嗽、咳痰5年，加重1周\n[BBOX-17] 现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，\n[BBOX-18] 不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管\n[BBOX-19] 哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感\n[BBOX-20] 和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治\n[BBOX-21] 就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二\n[BBOX-22] 便如常，近1年体重减少4kg。\n[BBOX-23] 既往史：\n[BBOX-24] 患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染\n[BBOX-25] 病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫\n[BBOX-26] 苗接种史不详\n[BBOX-27] 个人史：\n[BBOX-28] 出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长\n[BBOX-29] 地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物\n[BBOX-30] 质接触史。\n[BBOX-31] 婚育史：\n[BBOX-32] 已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。\n[BBOX-33] 月经史：\n[BBOX-34] 初潮年龄17岁 经期3-4天 绝经年龄53岁 月经及白带情况：正常\n[BBOX-35] 月经周期30天\n[BBOX-36] 家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否\n[BBOX-37] 认二系三代有遗传病史。患者否认有遗传倾向的疾病。\n[BBOX-38] 体格检查\n[BBOX-39] 生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60\n[BBOX-40] 体格检查\n[BBOX-41] 生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体\n[BBOX-42] 重：44kg，腰围：cm，BMI：18.8 kg/m²\n[BBOX-43] 一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常\n[BBOX-44] 表情：正常体位：自主体位步态：平稳配合检查：配合\n[BBOX-45] 皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无\n[BBOX-46] 皮疹：无紫癜：无\n[BBOX-47] 1/3\n[BBOX-48] 贵州醫科大學附属醫院\n[BBOX-49] THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n[BBOX-50] 入院记录\n[BBOX-51] 姓名：\n[BBOX-52] 床号：23-03床\n[BBOX-53] 病历号\n[BBOX-54] 科室：呼吸与危重医学科医生\n[BBOX-55] 站\n[BBOX-56] 水肿：无脱水现象：无松紧度：适中\n[BBOX-57] 温度：适中出汗：无显性出汗瘢痕：无感染：无\n[BBOX-58] 头颅：大小：正常畸形：无包块：无\n[BBOX-59] 凹陷：无压痛：无\n[BBOX-60] 眼：眼睑：无水肿结膜：无充血巩膜：无黄染\n[BBOX-61] 眼球四个象限运动：左眼：正常右眼：正常\n[BBOX-62] 眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆\n[BBOX-63] 对光反射：左眼：灵敏右眼：灵敏\n[BBOX-64] 鼻：外形：正常其他异常：无鼻旁窦压痛：无\n[BBOX-65] 口：唇：无紫绀粘膜：无充血腮腺导管开口：正常\n[BBOX-66] 舌：伸舌居中牙龈：无肿胀龋齿：无\n[BBOX-67] 咽喉：扁桃体：正常咽：无充血声音：正常\n[BBOX-68] 淋巴：淋巴结：全身浅表淋巴结未及肿大\n[BBOX-69] 颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张\n[BBOX-70] 气管：居中颈静脉回流征：无\n[BBOX-71] 甲状腺：无肿大\n[BBOX-72] 眼球四个象限运动：左眼：正常 右眼：正常\n[BBOX-73] 眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆\n[BBOX-74] 对光反射：左眼：灵敏 右眼：灵敏\n[BBOX-75] 鼻：外形：正常 其他异常：无 鼻旁窦压痛：无\n[BBOX-76] 口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常\n[BBOX-77] 舌：伸舌居中 牙龈：无肿胀 龋齿：无\n[BBOX-78] 咽 喉：扁桃体：正常 咽：无充血 声音：正常\n[BBOX-79] 淋巴 巴：淋巴结：全身浅表淋巴结未及肿大\n[BBOX-80] 颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张\n[BBOX-81] 气管：居中 颈静脉回流征：无\n[BBOX-82] 甲状腺：无肿大\n[BBOX-83] 胸部 部：胸廓：无畸形 乳房：\n[BBOX-84] 肺 部：视诊：呼吸运动\n[BBOX-85] 触诊：\n[BBOX-86] 叩诊：\n[BBOX-87] 听诊：\n[BBOX-88] 语音传导\n[BBOX-89] 心 脏：视诊：\n[BBOX-90] 触诊：心尖搏动：正常 振颤：无 心包摩擦感：无\n[BBOX-91] 叩诊：\n[BBOX-92] 第五肋间内0.5cm\n[BBOX-93] 心界\n[BBOX-94] 右(cm)\n[BBOX-95] 肋间\n[BBOX-96] 左(cm)\n[BBOX-97] 2\n[BBOX-98] 2\n[BBOX-99] 2\n[BBOX-100] 1\n[BBOX-101] 3\n[BBOX-102] (左锁骨中线距胸骨线7.5cm)\n[BBOX-103] 听诊：心率：92次/分 心律：齐 心音：未闻及异常心\n[BBOX-104] 额外心音：无 杂音：无 心包摩擦音：\n[BBOX-105] 周围血管：异常血管征：无\n[BBOX-106] 腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出\n[BBOX-107] 其他异常：无\n[BBOX-108] 触诊：腹壁：柔软 压痛：无\n[BBOX-109] 2/3\n[BBOX-110] 站\n[BBOX-111] 反跳痛：无\n[BBOX-112] 液波振颤：无 振水声：无\n[BBOX-113] 腹部包块：无\n[BBOX-114] 肝：肋下未及\n[BBOX-115] 胆囊：未触及 Murphy征：阴性\n[BBOX-116] 脾：未触及\n[BBOX-117] 叩诊：肝浊音界：正常 移动性浊音：无\n[BBOX-118] 肾区叩痛：无\n[BBOX-119] 听诊：肠鸣音：正常 肠鸣音频率：4次/分\n[BBOX-120] 气过水音：无 血管杂音：无\n[BBOX-121] 肛门直肠：未检\n[BBOX-122] 生殖器：未检\n[BBOX-123] 脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限\n[BBOX-124] 压痛，叩痛：无\n[BBOX-125] 杵状指趾：无\n[BBOX-126] 神经系统：腹壁反射：正常 肢体瘫痪：无\n[BBOX-127] 肌张力：正常 肌力：V级\n[BBOX-128] 肱二头肌反射：正常 Hoffman征：阴性\n[BBOX-129] 膝腱反射：正常 Kernig征：阴性\n[BBOX-130] 跟腱反射：正常Babinski征：阴性\n[BBOX-131] 其他：无\n[BBOX-132] 补充及专科情况\n[BBOX-133] 双肺呼吸音清，未闻及干湿性啰音。\n[BBOX-134] 辅助检查：暂无\n[BBOX-135] VTE评估：\n[BBOX-136] Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：\n[BBOX-137] 入院诊断：1.支气管哮喘急性发作期\n[BBOX-138] 医师签名：\n[BBOX-139] 日期：2025-10-30 16:38\n[BBOX-140] 出院记录\n[BBOX-141] 姓名：\n[BBOX-142] 床号：23-03床\n[BBOX-143] 病历号：0\n[BBOX-144] 科室：呼吸与危重医学科医生站\n[BBOX-145] 姓名：\n[BBOX-146] 性别：女\n[BBOX-147] 年龄：72岁\n[BBOX-148] 民族：汉族\n[BBOX-149] 病历号：00\n[BBOX-150] 科室：呼吸与危重医学科医生站\n[BBOX-151] 入院日期：2025-10-30 14:34\n[BBOX-152] 住院天数：8\n[BBOX-153] 出院日期：2025-11-07 11:44\n[BBOX-154] 籍贯：贵州省贵阳市\n[BBOX-155] 职业：退休人员\n[BBOX-156] 单位：贵阳供电局\n[BBOX-157] 住址：中国贵州省贵阳\n[BBOX-158] 入院情况：\n[BBOX-159] 李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无\n[BBOX-160] 明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯\n[BBOX-161] 血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治\n[BBOX-162] 疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1\n[BBOX-163] 周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门\n[BBOX-164] 诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体\n[BBOX-165] 重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病\n[BBOX-166] 史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无\n[BBOX-167] 中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学\n[BBOX-168] 历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗\n[BBOX-169] 史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已\n[BBOX-170] 故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患\n[BBOX-171] 者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，\n[BBOX-172] 血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。\n[BBOX-173] 心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检\n[BBOX-174] 查：暂无\n[BBOX-175] 入院诊断：1.支气管哮喘急性发作期\n[BBOX-176] 诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床\n[BBOX-177] 检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1\n[BBOX-178] 2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝\n[BBOX-179] 功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中\n[BBOX-180] 心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心):钾(K)4.47mmol/L白介素-6(IL-6)2.10pg/ml\n[BBOX-181] 肌酐(Cr)57.90μmol/L C反应蛋白(CRP)0.48mg/L丙氨酸氨基转移酶(ALT)17.50U/L天冬氨酸氨基转移\n[BBOX-182] 酶(AST)25.40U/L。2025-10-3017:34 DIC全套(临床检验中心):纤维蛋白原(Fg)5.09g/L D-二聚体(DD)\n[BBOX-183] 0.75μg/mLDDU。2025-10-3015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3\n[BBOX-184] 015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3113:11 胸部CT平扫:1、考虑双肺新增少许感染灶,以左肺为著,请结合临床并复查。2、双肺尖多发结节灶、纤维化灶,邻近双侧\n[BBOX-185] 1/3\n[BBOX-186] 贵州醫科大學附屬醫院\n[BBOX-187] THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n[BBOX-188] 出院记录\n[BBOX-189] 姓名:\n[BBOX-190] 床号:23-03床\n[BBOX-191] 病历号:\n[BBOX-192] 科室:呼吸与危重医学科医生站\n[BBOX-193] 胸膜局限性增厚,考虑陈旧性病变,建议随诊复查。3、左肺下叶外基底段局部间质性改变,其内支气管\n[BBOX-194] 扩张;双肺支气管壁稍增厚,考虑慢性支气管炎,请结合临床并复查。4、左肺下叶微小结节,建议随诊\n[BBOX-195] 复查。5、纵隔内淋巴结稍增大,建议随诊复查。6、主动脉及冠状动脉硬化;胸椎退变,左侧第2前肋走\n[BBOX-196] 行欠佳。7、肝内囊性灶,建议超声随诊复查。2025-10-3114:35肺通气功能测定及支气管舒张试验:1.\n[BBOX-197] 中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+)2025-10-3112:33。传染病筛查\n[BBOX-198] 三项:阴性。2025-10-3113:12乙肝5项(定量):阴性。2025-10-3115:12大便常规(不含寄生虫)(临\n[BBOX-199] 床检验中心):未见异常。2025-10-3115:10尿液检查(尿液分析+尿有形成分):未见异常。2025-10-31\n[BBOX-200] 14:37痰液革兰氏染色+抗酸染色+真菌(临床检验中心):未见异常。2025-11-0210:41痰细菌培养及鉴\n[BBOX-201] 定:未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染,痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支\n[BBOX-202] 气管等对症支持治疗,先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症\n[BBOX-203] 治疗,经我科治疗后,患者病情较前好转,目前一般情况可,请示上级医师盾予今日办理出院。\n[BBOX-204] 出院诊断:1.支气管哮喘急性发作期;2.社区获得性肺炎,非重症;3.慢性阻塞性肺疾病;4.左肺下叶小\n[BBOX-205] 结节;5.肝囊肿。\n[BBOX-206] 出院情况:患者咳嗽、咳痰、胸闷、气促好转,无呼吸困难,无畏寒、发热,无恶心、呕吐等不适。查\n[BBOX-207] 体:生命体征平稳。全身皮肤黏膜、巩膜无黄染,双肺呼吸音清,未闻及干湿性啰音。律齐,各瓣膜听诊\n[BBOX-208] 区未闻及病理性杂音,腹软,全腹无压痛及反跳痛,肝脾肋下未及,肝脾肋下未及,双下肢无水肿。\n[BBOX-209] VTE评估:\n[BBOX-210] 床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31\n[BBOX-211] 14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴\n[BBOX-212] 定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支\n[BBOX-213] 气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症\n[BBOX-214] 治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。\n[BBOX-215] 出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小\n[BBOX-216] 结节；5.肝囊肿。\n[BBOX-217] 出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查\n[BBOX-218] 体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊\n[BBOX-219] 区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。\n[BBOX-220] VTE评估：\n[BBOX-221] Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：\n[BBOX-222] 出院医嘱：\n[BBOX-223] 1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治\n[BBOX-224] 疗，定期复查肺功能，呼吸科门诊随诊；\n[BBOX-225] 2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。\n[BBOX-226] 3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。\n[BBOX-227] 4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。\n[BBOX-228] 手术名称：\n[BBOX-229] 无\n[BBOX-230] 出院结果：好转\n[BBOX-231] 医生签名：\n[BBOX-232] 日期：2025-11-07 11:44\n[BBOX-233] 温馨提示\n[BBOX-234] 尊敬的患者，出院后如您需复印住院资料，请关注以下温馨小提示：\n[BBOX-235] 一、操作流程\n[BBOX-236] 【方法一】\n[BBOX-237] 1.请先打开微信“扫一扫”，扫描二维码，根据提示进行操作完成网上预约申请并回家等待。\n[BBOX-238] 2/3\n[BBOX-239] 贵州医科大学附属医院\n[BBOX-240] THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n[BBOX-241] 肺功能通气阻力检查报告\n[BBOX-242] 姓名：\n[BBOX-243] 性别：女\n[BBOX-244] 身高：151 cm\n[BBOX-245] 病历号：\n[BBOX-246] 年龄：72 Years\n[BBOX-247] 体重：46 kg\n[BBOX-248] Flow [L/s]\n[BBOX-249] F/V ex\n[BBOX-250] 10\n[BBOX-251] 5\n[BBOX-252] 0\n[BBOX-253] 2\n[BBOX-254] 4\n[BBOX-255] 6\n[BBOX-256] F/V in\n[BBOX-257] 8\n[BBOX-258] Vol [L]\n[BBOX-259] 6\n[BBOX-260] 4\n[BBOX-261] 1\n[BBOX-262] Vol%Vcmax\n[BBOX-263] 100\n[BBOX-264] Vcmax\n[BBOX-265] 20\n[BBOX-266] 0\n[BBOX-267] Time [s]\n[BBOX-268] 0\n[BBOX-269] 1\n[BBOX-270] 2\n[BBOX-271] 3\n[BBOX-272] 4\n[BBOX-273] 5\n[BBOX-274] 6\n[BBOX-275] 2.0\n[BBOX-276] R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]\n[BBOX-277] 1.5\n[BBOX-278] 1.0\n[BBOX-279] 1.0\n[BBOX-280] 0.5\n[BBOX-281] 0.0\n[BBOX-282] 0.4\n[BBOX-283] 0.2\n[BBOX-284] 0.2\n[BBOX-285] 0.4\n[BBOX-286] F [Hz]\n[BBOX-287] 5\n[BBOX-288] 10\n[BBOX-289] 15\n[BBOX-290] 20\n[BBOX-291] 25\n[BBOX-292] 30\n[BBOX-293] 35\n[BBOX-294] 日期\n[BBOX-295] 时间\n[BBOX-296] 预计值\n[BBOX-297] 实测值\n[BBOX-298] 实/预\n[BBOX-299] 25/10/31\n[BBOX-300] 14:29:33\n[BBOX-301] MV\n[BBOX-302] [L/min]\n[BBOX-303] 6.57\n[BBOX-304] 11.52\n[BBOX-305] 175.3\n[BBOX-306] VT\n[BBOX-307] [L]\n[BBOX-308] 0.33\n[BBOX-309] 0.79\n[BBOX-310] 239.6\n[BBOX-311] BF\n[BBOX-312] [1/min]\n[BBOX-313] 20.00\n[BBOX-314] 14.63\n[BBOX-315] 73.1\n[BBOX-316] VC MAX\n[BBOX-317] [L]\n[BBOX-318] 2.03\n[BBOX-319] 1.48\n[BBOX-320] 73.0\n[BBOX-321] ERV\n[BBOX-322] [L]\n[BBOX-323] 0.57\n[BBOX-324] 0.14\n[BBOX-325] 25.5\n[BBOX-326] IC\n[BBOX-327] [L]\n[BBOX-328] 1.46\n[BBOX-329] 1.34\n[BBOX-330] 91.6\n[BBOX-331] FVC\n[BBOX-332] [L]\n[BBOX-333] 1.93\n[BBOX-334] 1.44\n[BBOX-335] 74.8\n[BBOX-336] FEV 1\n[BBOX-337] [L]\n[BBOX-338] 1.56\n[BBOX-339] 0.91\n[BBOX-340] 58.4\n[BBOX-341] FEV 1 % FVC\n[BBOX-342] [%]\n[BBOX-343] 63.38\n[BBOX-344] FEV 1 % VC MAX\n[BBOX-345] [%]\n[BBOX-346] 75.42\n[BBOX-347] 61.67\n[BBOX-348] 81.8\n[BBOX-349] PEF\n[BBOX-350] [L/s]\n[BBOX-351] 5.04\n[BBOX-352] 2.51\n[BBOX-353] 49.8\n[BBOX-354] MEF 75\n[BBOX-355] [L/s]\n[BBOX-356] 4.66\n[BBOX-357] 1.54\n[BBOX-358] 33.1\n[BBOX-359] MEF 50\n[BBOX-360] [L/s]\n[BBOX-361] 3.06\n[BBOX-362] 0.56\n[BBOX-363] 18.2\n[BBOX-364] MEF 25\n[BBOX-365] [L/s]\n[BBOX-366] 0.90\n[BBOX-367] 0.22\n[BBOX-368] 24.6\n[BBOX-369] MEF 75/25\n[BBOX-370] [L/s]\n[BBOX-371] 2.36\n[BBOX-372] 0.50\n[BBOX-373] 21.1\n[BBOX-374] FET\n[BBOX-375] [s]\n[BBOX-376] 4.91\n[BBOX-377] LFV\n[BBOX-378] [L/min]\n[BBOX-379] 73.10\n[BBOX-380] Z at 5 Hz\n[BBOX-381] [kPa/(L/s)]\n[BBOX-382] 0.43\n[BBOX-383] 0.58\n[BBOX-384] 135.7\n[BBOX-385] Resonant frequency\n[BBOX-386] [1/s]\n[BBOX-387] 30.00\n[BBOX-388] R at 5 Hz\n[BBOX-389] [kPa/(L/s)]\n[BBOX-390] 0.41\n[BBOX-391] 0.57\n[BBOX-392] 137.2\n[BBOX-393] R nt 20 Hz\n[BBOX-394] [kPa/(L/s)]\n[BBOX-395] 0.35\n[BBOX-396] 0.34\n[BBOX-397] 95.3\n[BBOX-398] R at 5 Hz\n[BBOX-399] [kPa/(L/s)]\n[BBOX-400] -0.11\n[BBOX-401] -0.12\n[BBOX-402] 112.5\n[BBOX-403] Rcentral\n[BBOX-404] [kPa/(L/s)]\n[BBOX-405] 0.12\n[BBOX-406] Rperipheral\n[BBOX-407] [kPa/(L/s)]\n[BBOX-408] 0.40\n[BBOX-409] 结论：\n[BBOX-410] 1.中重度混合性肺通气功能障碍\n[BBOX-411] 2.（阻力增加\n[BBOX-412] 审核者专用章\n[BBOX-413] 检查者：王美锦\n[BBOX-414] \\begin{tabular}{lcccccc}\n[BBOX-415] 报告时间: 2025-04-05\n[BBOX-416] \\hline\n[BBOX-417] \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{预计值} & \\multicolumn{1}{c}{前次} & \\multicolumn{1}{c}{前/预} & \\multicolumn{1}{c}{后次} & \\multicolumn{1}{c}{后/预} & \\multicolumn{1}{c}{改善率} \\\\\n[BBOX-418] \\multicolumn{1}{c}{日期} & \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{25/10/31} & \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{25/10/31} & \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{} \\\\\n[BBOX-419] \\multicolumn{1}{c}{时间} & \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{14:29:33} & \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{14:53:10} & \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{} \\\\\n[BBOX-420] \\hline\n[BBOX-421] VT & [L] & 0.33 & 0.79 & 239.6 & & \\\\\n[BBOX-422] BF & [1/min] & 20.00 & 14.63 & 73.1 & & \\\\\n[BBOX-423] MV & [L/min] & 6.57 & 11.52 & 175.3 & & \\\\\n[BBOX-424] VC MAX & [L] & 2.03 & 1.48 & 73.0 & 1.66 & 81.9 & 12.2 \\\\\n[BBOX-425] ERV & [L] & 0.57 & 0.14 & 25.5 & & \\\\\n[BBOX-426] IC & [L] & 1.46 & 1.34 & 91.6 & & \\\\\n[BBOX-427] FVC & [L] & 1.93 & 1.44 & 74.8 & 1.66 & 86.2 & 15.3 \\\\\n[BBOX-428] FEV 1 & [L] & 1.56 & 0.91 & 58.4 & 1.08 & 68.8 & 17.8 \\\\\n[BBOX-429] FEV 1 \\% FVC & [\\%] & & 63.38 & & 64.76 & & 2.2 \\\\\n[BBOX-430] FEV 1 \\% VC MAX & [\\%] & 75.42 & 61.67 & 81.8 & 64.76 & 85.9 & 5.0 \\\\\n[BBOX-431] PEF & [L/s] & 5.04 & 2.51 & 49.8 & 3.35 & 66.5 & 33.6 \\\\\n[BBOX-432] MEF 75 & [L/s] & 4.66 & 1.54 & 33.1 & 1.72 & 36.8 & 11.3 \\\\\n[BBOX-433] MEF 50 & [L/s] & 3.06 & 0.56 & 18.2 & 0.83 & 27.1 & 49.1 \\\\\n[BBOX-434] MEF 25 & [L/s] & 0.90 & 0.22 & 24.6 & 0.36 & 39.8 & 62.1 \\\\\n[BBOX-435] MMEF 75/25 & [L/s] & 2.36 & 0.50 & 21.1 & 0.47 & 20.0 & -4.9 \\\\\n[BBOX-436] FET & [s] & & 4.91 & & 4.88 & & -0.6 \\\\\n[BBOX-437] V backextrapol. \\% FVC & [\\%] & & 3.85 & & 4.39 & & 13.9 \\\\\n[BBOX-438] \\hline\n[BBOX-439] MVV & [L/min] & 73.10 & & & & & \\\\\n[BBOX-440] \\hline\n[BBOX-441] \\end{tabular}\n[BBOX-442] 亦康互联网医院\n[BBOX-443] 普通\n[BBOX-444] 处方\n[BBOX-445] 已使用\n[BBOX-446] 已使用\n[BBOX-447] 已使用\n[BBOX-448] 联\n[BBOX-449] 处方笺\n[BBOX-450] 已使用\n[BBOX-451] NO.:\n[BBOX-452] 2025-12-05\n[BBOX-453] 已使用\n[BBOX-454] 姓名：\n[BBOX-455] 性别：女处方专用章\n[BBOX-456] 年龄：72岁\n[BBOX-457] 已使用\n[BBOX-458] 费别：自费\n[BBOX-459] 科别：内科\n[BBOX-460] 已使用\n[BBOX-461] 临床诊断：支气管哮喘\n[BBOX-462] 已使用\n[BBOX-463] Rp：\n[BBOX-464] 已使用\n[BBOX-465] 沙美特罗替卡松吸入粉雾剂\n[BBOX-466] 已使用\n[BBOX-467] 50μg:250μg*60泡\n[BBOX-468] x 3盒\n[BBOX-469] 已使用\n[BBOX-470] 用法用量：\n[BBOX-471] 口腔吸入,一日两次,一次1.0揿;\n[BBOX-472] 已使用\n[BBOX-473] 补充说明：处方超7日为病情需要\n[BBOX-474] 已使用\n[BBOX-475] 已使用\n[BBOX-476] 已使用\n[BBOX-477] 已使用\n[BBOX-478] 已使用\n[BBOX-479] 已使用\n[BBOX-480] 已使用\n[BBOX-481] 已使用\n[BBOX-482] 已使用\n[BBOX-483] 已使用\n[BBOX-484] 已使用\n[BBOX-485] 已使用\n[BBOX-486] 已使用\n[BBOX-487] 已使用\n[BBOX-488] 已使用\n[BBOX-489] 已使用\n[BBOX-490] 已使用\n[BBOX-491] 已使用\n[BBOX-492] 已使用\n[BBOX-493] 已使用\n[BBOX-494] 已使用\n[BBOX-495] 已使用\n[BBOX-496] 已使用\n[BBOX-497] 已使用\n[BBOX-498] 已使用\n[BBOX-499] 已使用\n[BBOX-500] 已使用\n[BBOX-501] 已使用\n[BBOX-502] 已使用\n[BBOX-503] 已使用\n[BBOX-504] 已使用\n[BBOX-505] 已使用\n[BBOX-506] 已使用\n[BBOX-507] 已使用\n[BBOX-508] 已使用\n[BBOX-509] 已使用\n[BBOX-510] 已使用\n[BBOX-511] 已使用\n[BBOX-512] 已使用\n[BBOX-513] 已使用\n[BBOX-514] 已使用\n[BBOX-515] 已使用\n[BBOX-516] 已使用\n[BBOX-517] 已使用\n[BBOX-518] 已使用\n[BBOX-519] 已使用\n[BBOX-520] 已使用\n[BBOX-521] 已使用\n[BBOX-522] 已使用\n[BBOX-523] 已使用\n[BBOX-524] 已使用\n[BBOX-525] 已使用\n[BBOX-526] 已使用\n[BBOX-527] 已使用\n[BBOX-528] 已使用\n[BBOX-529] 已使用\n[BBOX-530] 已使用\n[BBOX-531] 已使用\n[BBOX-532] 已使用\n[BBOX-533] 已使用\n[BBOX-534] 已使用\n[BBOX-535] 已使用\n[BBOX-536] 已使用\n[BBOX-537] 已使用\n[BBOX-538] 已使用\n[BBOX-539] 已使用\n[BBOX-540] 已使用\n[BBOX-541] 已使用\n[BBOX-542] 已使用\n[BBOX-543] 已使用\n[BBOX-544] 已使用\n[BBOX-545] 已使用\n[BBOX-546] 已使用\n[BBOX-547] 已使用\n[BBOX-548] 已使用\n[BBOX-549] 已使用\n[BBOX-550] 已使用\n[BBOX-551] 已使用\n[BBOX-552] 已使用\n[BBOX-553] 已使用\n[BBOX-554] 已使用\n[BBOX-555] 已使用\n[BBOX-556] 已使用\n[BBOX-557] 已使用\n[BBOX-558] 已使用\n[BBOX-559] 已使用\n[BBOX-560] 已使用\n[BBOX-561] 已使用\n[BBOX-562] 已使用\n[BBOX-563] 已使用\n[BBOX-564] 已使用\n[BBOX-565] 已使用\n[BBOX-566] 已使用\n[BBOX-567] 已使用\n[BBOX-568] 已使用\n[BBOX-569] 已使用\n[BBOX-570] 已使用\n[BBOX-571] 已使用\n[BBOX-572] 已使用\n[BBOX-573] 已使用\n[BBOX-574] 已使用\n[BBOX-575] 已使用\n[BBOX-576] 已使用\n[BBOX-577] 已使用\n[BBOX-578] 已使用\n[BBOX-579] 已使用\n[BBOX-580] 已使用\n[BBOX-581] 已使用\n[BBOX-582] 已使用\n[BBOX-583] 已使用\n[BBOX-584] 已使用\n[BBOX-585] 已使用\n[BBOX-586] 已使用\n[BBOX-587] 已使用\n[BBOX-588] 已使用\n[BBOX-589] 已使用\n[BBOX-590] 已使用\n[BBOX-591] 已使用\n[BBOX-592] 已使用\n[BBOX-593] 已使用\n[BBOX-594] 已使用\n[BBOX-595] 已使用\n[BBOX-596] 已使用\n[BBOX-597] 已使用\n[BBOX-598] 已使用\n[BBOX-599] 已使用\n[BBOX-600] 已使用\n[BBOX-601] 已使用\n[BBOX-602] 已使用\n[BBOX-603] 已使用\n[BBOX-604] 已使用\n[BBOX-605] 已使用\n[BBOX-606] 已使用\n[BBOX-607] 已使用\n[BBOX-608] 已使用\n[BBOX-609] 已使用\n[BBOX-610] 已使用\n[BBOX-611] 已使用\n[BBOX-612] 已使用\n[BBOX-613] 已使用\n[BBOX-614] 已使用\n[BBOX-615] 已使用\n[BBOX-616] 已使用\n[BBOX-617] 已使用\n[BBOX-618] 已使用\n[BBOX-619] 已使用\n[BBOX-620] 已使用\n[BBOX-621] 已使用\n[BBOX-622] 已使用\n[BBOX-623] 已使用\n[BBOX-624] 已使用\n[BBOX-625] 已使用\n[BBOX-626] 已使用\n[BBOX-627] 已使用\n[BBOX-628] 已使用\n[BBOX-629] 已使用\n[BBOX-630] 已使用\n[BBOX-631] 已使用\n[BBOX-632] 已使用\n[BBOX-633] 已使用\n[BBOX-634] 已使用\n[BBOX-635] 已使用\n[BBOX-636] 已使用\n[BBOX-637] 已使用\n[BBOX-638] 已使用\n[BBOX-639] 已使用\n[BBOX-640] 已使用\n[BBOX-641] 已使用\n[BBOX-642] 已使用\n[BBOX-643] 已使用\n[BBOX-644] 已使用\n[BBOX-645] 已使用\n[BBOX-646] 已使用\n[BBOX-647] 已使用\n[BBOX-648] 已使用\n[BBOX-649] 已使用\n[BBOX-650] 已使用\n[BBOX-651] 已使用\n[BBOX-652] 已使用\n[BBOX-653] 已使用\n[BBOX-654] 已使用\n[BBOX-655] 已使用\n[BBOX-656] 已使用\n[BBOX-657] 已使用\n[BBOX-658] 已使用\n[BBOX-659] 已使用\n[BBOX-660] 已使用\n[BBOX-661] 已使用\n[BBOX-662] 已使用\n[BBOX-663] 已使用\n[BBOX-664] 已使用\n[BBOX-665] 已使用\n[BBOX-666] 已使用\n[BBOX-667] 已使用\n[BBOX-668] 已使用\n[BBOX-669] 已使用\n[BBOX-670] 已使用\n[BBOX-671] 已使用\n[BBOX-672] 已使用\n[BBOX-673] 已使用\n[BBOX-674] 已使用\n[BBOX-675] 已使用\n[BBOX-676] 已使用\n[BBOX-677] 已使用\n[BBOX-678] 已使用\n[BBOX-679] 已使用\n[BBOX-680] 已使用\n[BBOX-681] 已使用\n[BBOX-682] 已使用\n[BBOX-683] 已使用\n[BBOX-684] 已使用\n[BBOX-685] 已使用\n[BBOX-686] 已使用\n[BBOX-687] 已使用\n[BBOX-688] 已使用\n[BBOX-689] 已使用\n[BBOX-690] 已使用\n[BBOX-691] 已使用\n[BBOX-692] 已使用\n[BBOX-693] 已使用\n[BBOX-694] 已使用\n[BBOX-695] 已使用\n[BBOX-696] 已使用\n[BBOX-697] 已使用\n[BBOX-698] 已使用\n[BBOX-699] 已使用\n[BBOX-700] 已使用\n[BBOX-701] 已使用\n[BBOX-702] 已使用\n[BBOX-703] 已使用\n[BBOX-704] 已使用\n[BBOX-705] 已使用\n[BBOX-706] 已使用\n[BBOX-707] 已使用\n[BBOX-708] 已使用\n[BBOX-709] 已使用\n[BBOX-710] 已使用\n[BBOX-711] 已使用\n[BBOX-712] 已使用\n[BBOX-713] 已使用\n[BBOX-714] 已使用\n[BBOX-715] 已使用\n[BBOX-716] 已使用\n[BBOX-717] 已使用\n[BBOX-718] 已使用\n[BBOX-719] 已使用\n[BBOX-720] 已使用\n[BBOX-721] 已使用\n[BBOX-722] 已使用\n[BBOX-723] 已使用\n[BBOX-724] 已使用\n[BBOX-725] 已使用\n[BBOX-726] 已使用\n[BBOX-727] 已使用\n[BBOX-728] 已使用\n[BBOX-729] 已使用\n[BBOX-730] 已使用\n[BBOX-731] 已使用\n[BBOX-732] 已使用\n[BBOX-733] 已使用\n[BBOX-734] 已使用\n[BBOX-735] 已使用\n[BBOX-736] 已使用\n[BBOX-737] 已使用\n[BBOX-738] 已使用\n[BBOX-739] 已使用\n[BBOX-740] 已使用\n[BBOX-741] 已使用\n[BBOX-742] 已使用\n[BBOX-743] 已使用\n[BBOX-744] 已使用\n[BBOX-745] 已使用\n[BBOX-746] 已使用\n[BBOX-747] 已使用\n[BBOX-748] 已使用\n[BBOX-749] 已使用\n[BBOX-750] 已使用\n[BBOX-751] 已使用\n[BBOX-752] 已使用\n[BBOX-753] 已使用\n[BBOX-754] 已使用\n[BBOX-755] 已使用\n[BBOX-756] 已使用\n[BBOX-757] 已使用\n[BBOX-758] 已使用\n[BBOX-759] 已使用\n[BBOX-760] 已使用\n[BBOX-761] 已使用\n[BBOX-762] 已使用\n[BBOX-763] 已使用\n[BBOX-764] 已使用\n[BBOX-765] 已使用\n[BBOX-766] 已使用\n[BBOX-767] 已使用\n[BBOX-768] 已使用\n[BBOX-769] 已使用\n[BBOX-770] 已使用\n[BBOX-771] 已使用\n[BBOX-772] 已使用\n[BBOX-773] 已使用\n[BBOX-774] 已使用\n[BBOX-775] 已使用\n[BBOX-776] 已使用\n[BBOX-777] 已使用\n[BBOX-778] 已使用\n[BBOX-779] 已使用\n[BBOX-780] 已使用\n[BBOX-781] 已使用\n[BBOX-782] 已使用\n[BBOX-783] 已使用\n[BBOX-784] 已使用\n[BBOX-785] 已使用\n[BBOX-786] 已使用\n[BBOX-787] 已使用\n[BBOX-788] 已使用\n[BBOX-789] 已使用\n[BBOX-790] 已使用\n[BBOX-791] 已使用\n[BBOX-792] 已使用\n[BBOX-793] 已使用\n[BBOX-794] 已使用\n[BBOX-795] 已使用\n[BBOX-796] 已使用\n[BBOX-797] 已使用\n[BBOX-798] 已使用\n[BBOX-799] 已使用\n[BBOX-800] 已使用\n[BBOX-801] 已使用\n[BBOX-802] 已使用\n[BBOX-803] 已使用\n[BBOX-804] 已使用\n[BBOX-805] 已使用\n[BBOX-806] 已使用\n[BBOX-807] 已使用\n[BBOX-808] 已使用\n[BBOX-809] 已使用\n[BBOX-810] 已使用\n[BBOX-811] 已使用\n[BBOX-812] 已使用\n[BBOX-813] 已使用\n[BBOX-814] 已使用\n[BBOX-815] 已使用\n[BBOX-816] 已使用\n[BBOX-817] 已使用\n[BBOX-818] 已使用\n[BBOX-819] 已使用\n[BBOX-820] 已使用\n[BBOX-821] 已使用\n[BBOX-822] 已使用\n[BBOX-823] 已使用\n[BBOX-824] 已使用\n[BBOX-825] 已使用\n[BBOX-826] 已使用\n[BBOX-827] 已使用\n[BBOX-828] 已使用\n[BBOX-829] 已使用\n[BBOX-830] 已使用\n[BBOX-831] 已使用\n[BBOX-832] 已使用\n[BBOX-833] 已使用\n[BBOX-834] 已使用\n[BBOX-835] 已使用\n[BBOX-836] 已使用\n[BBOX-837] 已使用\n[BBOX-838] 已使用\n[BBOX-839] 已使用\n[BBOX-840] 已使用\n[BBOX-841] 已使用\n[BBOX-842] 已使用\n[BBOX-843] 已使用\n[BBOX-844] 已使用\n[BBOX-845] 已使用\n[BBOX-846] 已使用\n[BBOX-847] 已使用\n[BBOX-848] 已使用\n[BBOX-849] 已使用\n[BBOX-850] 已使用\n[BBOX-851] 已使用\n[BBOX-852] 已使用\n[BBOX-853] 已使用\n[BBOX-854] 已使用\n[BBOX-855] 已使用\n[BBOX-856] 已使用\n[BBOX-857] 已使用\n[BBOX-858] 已使用\n[BBOX-859] 已使用\n[BBOX-860] 已使用\n[BBOX-861] 已使用\n[BBOX-862] 已使用\n[BBOX-863] 已使用\n[BBOX-864] 已使用\n[BBOX-865] 已使用\n[BBOX-866] 已使用\n[BBOX-867] 已使用\n[BBOX-868] 已使用\n[BBOX-869] 已使用\n[BBOX-870] 已使用\n[BBOX-871] 已使用\n[BBOX-872] 已使用\n[BBOX-873] 已使用\n[BBOX-874] 已使用\n[BBOX-875] 已使用\n[BBOX-876] 已使用\n[BBOX-877] 已使用\n[BBOX-878] 已使用\n[BBOX-879] 已使用\n[BBOX-880] 已使用\n[BBOX-881] 已使用\n[BBOX-882] 已使用\n[BBOX-883] 已使用\n[BBOX-884] 已使用\n[BBOX-885] 已使用\n[BBOX-886] 已使用\n[BBOX-887] 已使用\n[BBOX-888] 已使用\n[BBOX-889] 已使用\n[BBOX-890] 已使用\n[BBOX-891] 已使用\n[BBOX-892] 已使用\n[BBOX-893] 已使用\n[BBOX-894] 已使用\n[BBOX-895] 已使用\n[BBOX-896] 已使用\n[BBOX-897] 已使用\n[BBOX-898] 已使用\n[BBOX-899] 已使用\n[BBOX-900] 已使用\n[BBOX-901] 已使用\n[BBOX-902] 已使用\n[BBOX-903] 已使用\n[BBOX-904] 已使用\n[BBOX-905] 已使用\n[BBOX-906] 已使用\n[BBOX-907] 已使用\n[BBOX-908] 已使用\n[BBOX-909] 已使用\n[BBOX-910] 已使用\n[BBOX-911] 已使用\n[BBOX-912] 已使用\n[BBOX-913] 已使用\n[BBOX-914] 已使用\n[BBOX-915] 已使用\n[BBOX-916] 已使用\n[BBOX-917] 已使用\n[BBOX-918] 已使用\n[BBOX-919] 已使用\n[BBOX-920] 已使用\n[BBOX-921] 已使用\n[BBOX-922] 已使用\n[BBOX-923] 已使用\n[BBOX-924] 已使用\n[BBOX-925] 已使用\n[BBOX-926] 已使用\n[BBOX-927] 已使用\n[BBOX-928] 已使用\n[BBOX-929] 已使用\n[BBOX-930] 已使用\n[BBOX-931] 已使用\n[BBOX-932] 已使用\n[BBOX-933] 已使用\n[BBOX-934] 已使用\n[BBOX-935] 已使用\n[BBOX-936] 已使用\n[BBOX-937] 已使用\n[BBOX-938] 已使用\n[BBOX-939] 已使用\n[BBOX-940] 已使用\n[BBOX-941] 已使用\n[BBOX-942] 已使用\n[BBOX-943] 已使用\n[BBOX-944] 已使用\n[BBOX-945] 已使用\n[BBOX-946] 已使用\n[BBOX-947] 已使用\n[BBOX-948] 已使用\n[BBOX-949] 已使用\n[BBOX-950] 已使用\n[BBOX-951] 已使用\n[BBOX-952] 已使用\n[BBOX-953] 已使用\n[BBOX-954] 已使用\n[BBOX-955] 已使用\n[BBOX-956] 已使用\n[BBOX-957] 已使用\n[BBOX-958] 已使用\n[BBOX-959] 已使用\n[BBOX-960] 已使用\n[BBOX-961] 已使用\n[BBOX-962] 已使用\n[BBOX-963] 已使用\n[BBOX-964] 已使用\n[BBOX-965] 已使用\n[BBOX-966] 已使用\n[BBOX-967] 已使用\n[BBOX-968] 已使用\n[BBOX-969] 已使用\n[BBOX-970] 已使用\n[BBOX-971] 已使用\n[BBOX-972] 已使用\n[BBOX-973] 已使用\n[BBOX-974] 已使用\n[BBOX-975] 已使用\n[BBOX-976] 已使用\n[BBOX-977] 已使用\n[BBOX-978] 已使用\n[BBOX-979] 已使用\n[BBOX-980] 已使用\n[BBOX-981] 已使用\n[BBOX-982] 已使用\n[BBOX-983] 已使用\n[BBOX-984] 已使用\n[BBOX-985] 已使用\n[BBOX-986] 已使用\n[BBOX-987] 已使用\n[BBOX-988] 已使用\n[BBOX-989] 已使用\n[BBOX-990] 已使用\n[BBOX-991] 已使用\n[BBOX-992] 已使用\n[BBOX-993] 已使用\n[BBOX-994] 已使用\n[BBOX-995] 已使用\n[BBOX-996] 已使用\n[BBOX-997] 已使用\n[BBOX-998] 已使用\n[BBOX-999] 已使用\n[BBOX-1000] 已使用\n[BBOX-1001] 已使用\n[BBOX-1002] 已使用\n[BBOX-1003] 已使用\n[BBOX-1004] 已使用\n[BBOX-1005] 已使用\n[BBOX-1006] 已使用\n[BBOX-1007] 已使用\n[BBOX-1008] 已使用\n[BBOX-1009] 已使用\n[BBOX-1010] 已使用\n[BBOX-1011] 已使用\n[BBOX-1012] 已使用\n[BBOX-1013] 已使用\n[BBOX-1014] 已使用\n[BBOX-1015] 已使用\n[BBOX-1016] 已使用\n[BBOX-1017] 已使用\n[BBOX-1018] 已使用\n[BBOX-1019] 已使用\n[BBOX-1020] 已使用\n[BBOX-1021] 已使用\n[BBOX-1022] 已使用\n[BBOX-1023] 已使用\n[BBOX-1024] 已使用\n[BBOX-1025] 已使用\n[BBOX-1026] 已使用\n[BBOX-1027] 已使用\n[BBOX-1028] 已使用\n[BBOX-1029] 已使用\n[BBOX-1030] 已使用\n[BBOX-1031] 已使用\n[BBOX-1032] 已使用\n[BBOX-1033] 已使用\n[BBOX-1034] 已使用\n[BBOX-1035] 已使用\n[BBOX-1036] 已使用\n[BBOX-1037] 已使用\n[BBOX-1038] 已使用\n[BBOX-1039] 已使用\n[BBOX-1040] 已使用\n[BBOX-1041] 已使用\n[BBOX-1042] 已使用\n[BBOX-1043] 已使用\n[BBOX-1044] 已使用\n[BBOX-1045] 已使用\n[BBOX-1046] 已使用\n[BBOX-1047] 已使用\n[BBOX-1048] 已使用\n[BBOX-1049] 已使用\n[BBOX-1050] 已使用\n[BBOX-1051] 已使用\n[BBOX-1052] 已使用\n[BBOX-1053] 已使用\n[BBOX-1054] 已使用\n[BBOX-1055] 已使用\n[BBOX-1056] 已使用\n[BBOX-1057] 已使用\n[BBOX-1058] 已使用\n[BBOX-1059] 已使用\n[BBOX-1060] 已使用\n[BBOX-1061] 已使用\n[BBOX-1062] 已使用\n[BBOX-1063] 已使用\n[BBOX-1064] 已使用\n[BBOX-1065] 已使用\n[BBOX-1066] 已使用\n[BBOX-1067] 已使用\n[BBOX-1068] 已使用\n[BBOX-1069] 已使用\n[BBOX-1070] 已使用\n[BBOX-1071] 已使用\n[BBOX-1072] 已使用\n[BBOX-1073] 已使用\n[BBOX-1074] 已使用\n[BBOX-1075] 已使用\n[BBOX-1076] 已使用\n[BBOX-1077] 已使用\n[BBOX-1078] 已使用\n[BBOX-1079] 已使用\n[BBOX-1080] 已使用\n[BBOX-1081] 已使用\n[BBOX-1082] 已使用\n[BBOX-1083] 已使用\n[BBOX-1084] 已使用\n[BBOX-1085] 已使用\n[BBOX-1086] 已使用\n[BBOX-1087] 已使用\n[BBOX-1088] 已使用\n[BBOX-1089] 已使用\n[BBOX-1090] 已使用\n[BBOX-1091] 已使用\n[BBOX-1092] 已使用\n[BBOX-1093] 已使用\n[BBOX-1094] 已使用\n[BBOX-1095] 已使用\n[BBOX-1096] 已使用\n[BBOX-1097] 已使用\n[BBOX-1098] 已使用\n[BBOX-1099] 已使用\n[BBOX-1100] 已使用\n[BBOX-1101] 已使用\n[BBOX-1102] 已使用\n[BBOX-1103] 已使用\n[BBOX-1104] 已使用\n[BBOX-1105] 已使用\n[BBOX-1106] 已使用\n[BBOX-1107] 已使用\n[BBOX-1108] 已使用\n[BBOX-1109] 已使用\n[BBOX-1110] 已使用\n[BBOX-1111] 已使用\n[BBOX-1112] 已使用\n[BBOX-1113] 已使用\n[BBOX-1114] 已使用\n[BBOX-1115] 已使用\n[BBOX-1116] 已使用\n[BBOX-1117] 已使用\n[BBOX-1118] 已使用\n[BBOX-1119] 已使用\n[BBOX-1120] 已使用\n[BBOX-1121] 已使用\n[BBOX-1122] 已使用\n[BBOX-1123] 已使用\n[BBOX-1124] 已使用\n[BBOX-1125] 已使用\n[BBOX-1126] 已使用\n[BBOX-1127] 已使用\n[BBOX-1128] 已使用\n[BBOX-1129] 已使用\n[BBOX-1130] 已使用\n[BBOX-1131] 已使用\n[BBOX-1132] 已使用\n[BBOX-1133] 已使用\n[BBOX-1134] 已使用\n[BBOX-1135] 已使用\n[BBOX-1136] 已使用\n[BBOX-1137] 已使用\n[BBOX-1138] 已使用\n[BBOX-1139] 已使用\n[BBOX-1140] 已使用\n[BBOX-1141] 已使用\n[BBOX-1142] 已使用\n[BBOX-1143] 已使用\n[BBOX-1144] 已使用\n[BBOX-1145] 已使用\n[BBOX-1146] 已使用\n[BBOX-1147] 已使用\n[BBOX-1148] 已使用\n[BBOX-1149] 已使用\n[BBOX-1150] 已使用\n[BBOX-1151] 已使用\n[BBOX-1152] 已使用\n[BBOX-1153] 已使用\n[BBOX-1154] 已使用\n[BBOX-1155] 已使用\n[BBOX-1156] 已使用\n[BBOX-1157] 已使用\n[BBOX-1158] 已使用\n[BBOX-1159] 已使用\n[BBOX-1160] 已使用\n[BBOX-1161] 已使用\n[BBOX-1162] 已使用\n[BBOX-1163] 已使用\n[BBOX-1164] 已使用\n[BBOX-1165] 已使用\n[BBOX-1166] 已使用\n[BBOX-1167] 已使用\n[BBOX-1168] 已使用\n[BBOX-1169] 已使用\n[BBOX-1170] 已使用\n[BBOX-1171] 已使用\n[BBOX-1172] 已使用\n[BBOX-1173] 已使用\n[BBOX-1174] 已使用\n[BBOX-1175] 已使用\n[BBOX-1176] 已使用\n[BBOX-1177] 已使用\n[BBOX-1178] 已使用\n[BBOX-1179] 已使用\n[BBOX-1180] 已使用\n[BBOX-1181] 已使用\n[BBOX-1182] 已使用\n[BBOX-1183] 已使用\n[BBOX-1184] 已使用\n[BBOX-1185] 已使用\n[BBOX-1186] 已使用\n[BBOX-1187] 已使用\n[BBOX-1188] 已使用\n[BBOX-1189] 已使用\n[BBOX-1190] 已使用\n[BBOX-1191] 已使用\n[BBOX-1192] 已使用\n[BBOX-1193] 已使用\n[BBOX-1194] 已使用\n[BBOX-1195] 已使用\n[BBOX-1196] 已使用\n[BBOX-1197] 已使用\n[BBOX-1198] 已使用\n[BBOX-1199] 已使用\n[BBOX-1200] 已使用\n[BBOX-1201] 已使用\n[BBOX-1202] 已使用\n[BBOX-1203] 已使用\n[BBOX-1204] 已使用\n[BBOX-1205] 已使用\n[BBOX-1206] 已使用\n[BBOX-1207] 已使用\n[BBOX-1208] 已使用\n[BBOX-1209] 已使用\n[BBOX-1210] 已使用\n[BBOX-1211] 已使用\n[BBOX-1212] 已使用\n[BBOX-1213] 已使用\n[BBOX-1214] 已使用\n[BBOX-1215] 已使用\n[BBOX-1216] 已使用\n[BBOX-1217] 已使用\n[BBOX-1218] 已使用\n[BBOX-1219] 已使用\n[BBOX-1220] 已使用\n[BBOX-1221] 已使用\n[BBOX-1222] 已使用\n[BBOX-1223] 已使用\n[BBOX-1224] 已使用\n[BBOX-1225] 已使用\n[BBOX-1226] 已使用\n[BBOX-1227] 已使用\n[BBOX-1228] 已使用\n[BBOX-1229] 已使用\n[BBOX-1230] 已使用\n[BBOX-1231] 已使用\n[BBOX-1232] 已使用\n[BBOX-1233] 已使用\n[BBOX-1234] 已使用\n[BBOX-1235] 已使用\n[BBOX-1236] 已使用\n[BBOX-1237] 已使用\n[BBOX-1238] 已使用\n[BBOX-1239] 已使用\n[BBOX-1240] 已使用\n[BBOX-1241] 已使用\n[BBOX-1242] 已使用\n[BBOX-1243] 已使用\n[BBOX-1244] 已使用\n[BBOX-1245] 已使用\n[BBOX-1246] 已使用\n[BBOX-1247] 已使用\n[BBOX-1248] 已使用\n[BBOX-1249] 已使用\n[BBOX-1250] 已使用\n[BBOX-1251] 已使用\n[BBOX-1252] 已使用\n[BBOX-1253] 已使用\n[BBOX-1254] 已使用\n[BBOX-1255] 已使用\n[BBOX-1256] 已使用\n[BBOX-1257] 已使用\n[BBOX-1258] 已使用\n[BBOX-1259] 已使用\n[BBOX-1260] 已使用\n[BBOX-1261] 已使用\n[BBOX-1262] 已使用\n[BBOX-1263] 已使用\n[BBOX-1264] 已使用\n[BBOX-1265] 已使用\n[BBOX-1266] 已使用\n[BBOX-1267] 已使用\n[BBOX-1268] 已使用\n[BBOX-1269] 已使用\n[BBOX-1270] 已使用\n[BBOX-1271] 已使用\n[BBOX-1272] 已使用\n[BBOX-1273] 已使用\n[BBOX-1274] 已使用\n[BBOX-1275] 已使用\n[BBOX-1276] 已使用\n[BBOX-1277] 已使用\n[BBOX-1278] 已使用\n[BBOX-1279] 已使用\n[BBOX-1280] 已使用\n[BBOX-1281] 已使用\n[BBOX-1282] 已使用\n[BBOX-1283] 已使用\n[BBOX-1284] 已使用\n[BBOX-1285] 已使用\n[BBOX-1286] 已使用\n[BBOX-1287] 已使用\n[BBOX-1288] 已使用\n[BBOX-1289] 已使用\n[BBOX-1290] 已使用\n[BBOX-1291] 已使用\n[BBOX-1292] 已使用\n[BBOX-1293] 已使用\n[BBOX-1294] 已使用\n[BBOX-1295] 已使用\n[BBOX-1296] 已使用\n[BBOX-1297] 已使用\n[BBOX-1298] 已使用\n[BBOX-1299] 已使用\n[BBOX-1300] 已使用\n[BBOX-1301] 已使用\n[BBOX-1302] 已使用\n[BBOX-1303] 已使用\n[BBOX-1304] 已使用\n[BBOX-1305] 已使用\n[BBOX-1306] 已使用\n[BBOX-1307] 已使用\n[BBOX-1308] 已使用\n[BBOX-1309] 已使用\n[BBOX-1310] 已使用\n[BBOX-1311] 已使用\n[BBOX-1312] 已使用\n[BBOX-1313] 已使用\n[BBOX-1314] 已使用\n[BBOX-1315] 已使用\n[BBOX-1316] 已使用\n[BBOX-1317] 已使用\n[BBOX-1318] 已使用\n[BBOX-1319] 已使用\n[BBOX-1320] 已使用\n[BBOX-1321] 已使用\n[BBOX-1322] 已使用\n[BBOX-1323] 已使用\n[BBOX-1324] 已使用\n[BBOX-1325] 已使用\n[BBOX-1326] 已使用\n[BBOX-1327] 已使用\n[BBOX-1328] 已使用\n[BBOX-1329] 已使用\n[BBOX-1330] 已使用\n[BBOX-1331] 已使用\n[BBOX-1332] 已使用\n[BBOX-1333] 已使用\n[BBOX-1334] 已使用\n[BBOX-1335] 已使用\n[BBOX-1336] 已使用\n[BBOX-1337] 已使用\n[BBOX-1338] 已使用\n[BBOX-1339] 已使用\n[BBOX-1340] 已使用\n[BBOX-1341] 已使用\n[BBOX-1342] 已使用\n[BBOX-1343] 已使用\n[BBOX-1344] 已使用\n[BBOX-1345] 已使用\n[BBOX-1346] 已使用\n[BBOX-1347] 已使用\n[BBOX-1348] 已使用\n[BBOX-1349] 已使用\n[BBOX-1350] 已使用\n[BBOX-1351] 已使用\n[BBOX-1352] 已使用\n[BBOX-1353] 已使用\n[BBOX-1354] 已使用\n[BBOX-1355] 已使用\n[BBOX-1356] 已使用\n[BBOX-1357] 已使用\n[BBOX-1358] 已使用\n[BBOX-1359] 已使用\n[BBOX-1360] 已使用\n[BBOX-1361] 已使用\n[BBOX-1362] 已使用\n[BBOX-1363] 已使用\n[BBOX-1364] 已使用\n[BBOX-1365] 已使用\n[BBOX-1366] 已使用\n[BBOX-1367] 已使用\n[BBOX-1368] 已使用\n[BBOX-1369] 已使用\n[BBOX-1370] 已使用\n[BBOX-1371] 已使用\n[BBOX-1372] 已使用\n[BBOX-1373] 已使用\n[BBOX-1374] 已使用\n[BBOX-1375] 已使用\n[BBOX-1376] 已使用\n[BBOX-1377] 已使用\n[BBOX-1378] 已使用\n[BBOX-1379] 已使用\n[BBOX-1380] 已使用\n[BBOX-1381] 已使用\n[BBOX-1382] 已使用\n[BBOX-1383] 已使用\n[BBOX-1384] 已使用\n[BBOX-1385] 已使用\n[BBOX-1386] 已使用\n[BBOX-1387] 已使用\n[BBOX-1388] 已使用\n[BBOX-1389] 已使用\n[BBOX-1390] 已使用\n[BBOX-1391] 已使用\n[BBOX-1392] 已使用\n[BBOX-1393] 已使用\n[BBOX-1394] 已使用\n[BBOX-1395] 已使用\n[BBOX-1396] 已使用\n[BBOX-1397] 已使用\n[BBOX-1398] 已使用\n[BBOX-1399] 已使用\n[BBOX-1400] 已使用\n[BBOX-1401] 已使用\n[BBOX-1402] 已使用\n[BBOX-1403] 已使用\n[BBOX-1404] 已使用\n[BBOX-1405] 已使用\n[BBOX-1406] 已使用\n[BBOX-1407] 已使用\n[BBOX-1408] 已使用\n[BBOX-1409] 已使用\n[BBOX-1410] 已使用\n[BBOX-1411] 已使用\n[BBOX-1412] 已使用\n[BBOX-1413] 已使用\n[BBOX-1414] 已使用\n[BBOX-1415] 已使用\n[BBOX-1416] 已使用\n[BBOX-1417] 已使用\n[BBOX-1418] 已使用\n[BBOX-1419] 已使用\n[BBOX-1420] 已使用\n[BBOX-1421] 已使用\n[BBOX-1422] 已使用\n[BBOX-1423] 已使用\n[BBOX-1424] 已使用\n[BBOX-1425] 已使用\n[BBOX-1426] 已使用\n[BBOX-1427] 已使用\n[BBOX-1428] 已使用\n[BBOX-1429] 已使用\n[BBOX-1430] 已使用\n[BBOX-1431] 已使用\n[BBOX-1432] 已使用\n[BBOX-1433] 已使用\n[BBOX-1434] 已使用\n[BBOX-1435] 已使用\n[BBOX-1436] 已使用\n[BBOX-1437] 已使用\n[BBOX-1438] 已使用\n[BBOX-1439] 已使用\n[BBOX-1440] 已使用\n[BBOX-1441] 已使用\n[BBOX-1442] 已使用\n[BBOX-1443] 已使用\n[BBOX-1444] 已使用\n[BBOX-1445] 已使用\n[BBOX-1446] 已使用\n[BBOX-1447] 已使用\n[BBOX-1448] 已使用\n[BBOX-1449] 已使用\n[BBOX-1450] 已使用\n[BBOX-1451] 已使用\n[BBOX-1452] 已使用\n[BBOX-1453] 已使用\n[BBOX-1454] 已使用\n[BBOX-1455] 已使用\n[BBOX-1456] 已使用\n[BBOX-1457] 已使用\n[BBOX-1458] 已使用\n[BBOX-1459] 已使用\n[BBOX-1460] 已使用\n[BBOX-1461] 已使用\n[BBOX-1462] 已使用\n[BBOX-1463] 已使用\n[BBOX-1464] 已使用\n[BBOX-1465] 已使用\n[BBOX-1466] 已使用\n[BBOX-1467] 已使用\n[BBOX-1468] 已使用\n[BBOX-1469] 已使用\n[BBOX-1470] 已使用\n[BBOX-1471] 已使用\n[BBOX-1472] 已使用\n[BBOX-1473] 已使用\n[BBOX-1474] 已使用\n[BBOX-1475] 已使用\n[BBOX-1476] 已使用\n[BBOX-1477] 已使用\n[BBOX-1478] 已使用\n[BBOX-1479] 已使用\n[BBOX-1480] 已使用\n[BBOX-1481] 已使用\n[BBOX-1482] 已使用\n[BBOX-1483] 已使用\n[BBOX-1484] 已使用\n[BBOX-1485] 已使用\n[BBOX-1486] 已使用\n[BBOX-1487] 已使用\n[BBOX-1488] 已使用\n[BBOX-1489] 已使用\n[BBOX-1490] 已使用\n[BBOX-1491] 已使用\n[BBOX-1492] 已使用\n[BBOX-1493] 已使用\n[BBOX-1494] 已使用\n[BBOX-1495] 已使用\n[BBOX-1496] 已使用\n[BBOX-1497] 已使用\n[BBOX-1498] 已使用\n[BBOX-1499] 已使用\n[BBOX-1500] 已使用\n[BBOX-1501] 已使用\n[BBOX-1502] 已使用\n[BBOX-1503] 已使用\n[BBOX-1504] 已使用\n[BBOX-1505] 已使用\n[BBOX-1506] 已使用\n[BBOX-1507] 已使用\n[BBOX-1508] 已使用\n[BBOX-1509] 已使用\n[BBOX-1510] 已使用\n[BBOX-1511] 已使用\n[BBOX-1512] 已使用\n[BBOX-1513] 已使用\n[BBOX-1514] 已使用\n[BBOX-1515] 已使用\n[BBOX-1516] 已使用\n[BBOX-1517] 已使用\n[BBOX-1518] 已使用\n[BBOX-1519] 已使用\n[BBOX-1520] 已使用\n[BBOX-1521] 已使用\n[BBOX-1522] 已使用\n[BBOX-1523] 已使用\n[BBOX-1524] 已使用\n[BBOX-1525] 已使用\n[BBOX-1526] 已使用\n[BBOX-1527] 已使用\n[BBOX-1528] 已使用\n[BBOX-1529] 已使用\n[BBOX-1530] 已使用\n[BBOX-1531] 已使用\n[BBOX-1532] 已使用\n[BBOX-1533] 已使用\n[BBOX-1534] 已使用\n[BBOX-1535] 已使用\n[BBOX-1536] 已使用\n[BBOX-1537] 已使用\n[BBOX-1538] 已使用\n[BBOX-1539] 已使用\n[BBOX-1540] 已使用\n[BBOX-1541] 已使用\n[BBOX-1542] 已使用\n[BBOX-1543] 已使用\n[BBOX-1544] 已使用\n[BBOX-1545] 已使用\n[BBOX-1546] 已使用\n[BBOX-1547] 已使用\n[BBOX-1548] 已使用\n[BBOX-1549] 已使用\n[BBOX-1550] 已使用\n[BBOX-1551] 已使用\n[BBOX-1552] 已使用\n[BBOX-1553] 已使用\n[BBOX-1554] 已使用\n[BBOX-1555] 已使用\n[BBOX-1556] 已使用\n[BBOX-1557] 已使用\n[BBOX-1558] 已使用\n[BBOX-1559] 已使用\n[BBOX-1560] 已使用\n[BBOX-1561] 已使用\n[BBOX-1562] 已使用\n[BBOX-1563] 已使用\n[BBOX-1564] 已使用\n[BBOX-1565] 已使用\n[BBOX-1566] 已使用\n[BBOX-1567] 已使用\n[BBOX-1568] 已使用\n[BBOX-1569] 已使用\n[BBOX-1570] 已使用\n[BBOX-1571] 已使用\n[BBOX-1572] 已使用\n[BBOX-1573] 已使用\n[BBOX-1574] 已使用\n[BBOX-1575] 已使用\n[BBOX-1576] 已使用\n[BBOX-1577] 已使用\n[BBOX-1578] 已使用\n[BBOX-1579] 已使用\n[BBOX-1580] 已使用\n[BBOX-1581] 已使用\n[BBOX-1582] 已使用\n[BBOX-1583] 已使用\n[BBOX-1584] 已使用\n[BBOX-1585] 已使用\n[BBOX-1586] 已使用\n[BBOX-1587] 已使用\n[BBOX-1588] 已使用\n[BBOX-1589] 已使用\n[BBOX-1590] 已使用\n[BBOX-1591] 已使用\n[BBOX-1592] 已使用\n[BBOX-1593] 已使用\n[BBOX-1594] 已使用\n[BBOX-1595] 已使用\n[BBOX-1596] 已使用\n[BBOX-1597] 已使用\n[BBOX-1598] 已使用\n[BBOX-1599] 已使用\n[BBOX-1600] 已使用\n[BBOX-1601] 已使用\n[BBOX-1602] 已使用\n[BBOX-1603] 已使用\n[BBOX-1604] 已使用\n[BBOX-1605] 已使用\n[BBOX-1606] 已使用\n[BBOX-1607] 已使用\n[BBOX-1608] 已使用\n[BBOX-1609] 已使用\n[BBOX-1610] 已使用\n[BBOX-1611] 已使用\n[BBOX-1612] 已使用\n[BBOX-1613] 已使用\n[BBOX-1614] 已使用\n[BBOX-1615] 已使用\n[BBOX-1616] 已使用\n[BBOX-1617] 已使用\n[BBOX-1618] 已使用\n[BBOX-1619] 已使用\n[BBOX-1620] 已使用\n[BBOX-1621] 已使用\n[BBOX-1622] 已使用\n[BBOX-1623] 已使用\n[BBOX-1624] 已使用\n[BBOX-1625] 已使用\n[BBOX-1626] 已使用\n[BBOX-1627] 已使用\n[BBOX-1628] 已使用\n[BBOX-1629] 已使用\n[BBOX-1630] 已使用\n[BBOX-1631] 已使用\n[BBOX-1632] 已使用\n[BBOX-1633] 已使用\n[BBOX-1634] 已使用\n[BBOX-1635] 已使用\n[BBOX-1636] 已使用\n[BBOX-1637] 已使用\n[BBOX-1638] 已使用\n[BBOX-1639] 已使用\n[BBOX-1640] 已使用\n[BBOX-1641] 已使用\n[BBOX-1642] 已使用\n[BBOX-1643] 已使用\n[BBOX-1644] 已使用\n[BBOX-1645] 已使用\n[BBOX-1646] 已使用\n[BBOX-1647] 已使用\n[BBOX-1648] 已使用\n[BBOX-1649] 已使用\n[BBOX-1650] 已使用\n[BBOX-1651] 已使用\n[BBOX-1652] 已使用\n[BBOX-1653] 已使用\n[BBOX-1654] 已使用\n[BBOX-1655] 已使用\n[BBOX-1656] 已使用\n[BBOX-1657] 已使用\n[BBOX-1658] 已使用\n[BBOX-1659] 已使用\n[BBOX-1660] 已使用\n[BBOX-1661] 已使用\n[BBOX-1662] 已使用\n[BBOX-1663] 已使用\n[BBOX-1664] 已使用\n[BBOX-1665] 已使用\n[BBOX-1666] 已使用\n[BBOX-1667] 已使用\n[BBOX-1668] 已使用\n[BBOX-1669] 已使用\n[BBOX-1670] 已使用\n[BBOX-1671] 已使用\n[BBOX-1672] 已使用\n[BBOX-1673] 已使用\n[BBOX-1674] 已使用\n[BBOX-1675] 已使用\n[BBOX-1676] 已使用\n[BBOX-1677] 已使用\n[BBOX-1678] 已使用\n[BBOX-1679] 已使用\n[BBOX-1680] 已使用\n[BBOX-1681] 已使用\n[BBOX-1682] 已使用\n[BBOX-1683] 已使用\n[BBOX-1684] 已使用\n[BBOX-1685] 已使用\n[BBOX-1686] 已使用\n[BBOX-1687] 已使用\n[BBOX-1688] 已使用\n[BBOX-1689] 已使用\n[BBOX-1690] 已使用\n[BBOX-1691] 已使用\n[BBOX-1692] 已使用\n[BBOX-1693] 已使用\n[BBOX-1694] 已使用\n[BBOX-1695] 已使用\n[BBOX-1696] 已使用\n[BBOX-1697] 已使用\n[BBOX-1698] 已使用\n[BBOX-1699] 已使用\n[BBOX-1700] 已使用\n[BBOX-1701] 已使用\n[BBOX-1702] 已使用\n[BBOX-1703] 已使用\n[BBOX-1704] 已使用\n[BBOX-1705] 已使用\n[BBOX-1706] 已使用\n[BBOX-1707] 已使用\n[BBOX-1708] 已使用\n[BBOX-1709] 已使用\n[BBOX-1710] 已使用\n[BBOX-1711] 已使用\n[BBOX-1712] 已使用\n[BBOX-1713] 已使用\n[BBOX-1714] 已使用\n[BBOX-1715] 已使用\n[BBOX-1716] 已使用\n[BBOX-1717] 已使用\n[BBOX-1718] 已使用\n[BBOX-1719] 已使用\n[BBOX-1720] 已使用\n[BBOX-1721] 已使用\n[BBOX-1722] 已使用\n[BBOX-1723] 已使用\n[BBOX-1724] 已使用\n[BBOX-1725] 已使用\n[BBOX-1726] 已使用\n[BBOX-1727] 已使用\n[BBOX-1728] 已使用\n[BBOX-1729] 已使用\n[BBOX-1730] 已使用\n[BBOX-1731] 已使用\n[BBOX-1732] 已使用\n[BBOX-1733] 已使用\n[BBOX-1734] 已使用\n[BBOX-1735] 已使用\n[BBOX-1736] 已使用\n[BBOX-1737] 已使用\n[BBOX-1738] 已使用\n[BBOX-1739] 已使用\n[BBOX-1740] 已使用\n[BBOX-1741] 已使用\n[BBOX-1742] 已使用\n[BBOX-1743] 已使用\n[BBOX-1744] 已使用\n[BBOX-1745] 已使用\n[BBOX-1746] 已使用\n[BBOX-1747] 已使用\n[BBOX-1748] 已使用\n[BBOX-1749] 已使用\n[BBOX-1750] 已使用\n[BBOX-1751] 已使用\n[BBOX-1752] 已使用\n[BBOX-1753] 已使用\n[BBOX-1754] 已使用\n[BBOX-1755] 已使用\n[BBOX-1756] 已使用\n[BBOX-1757] 已使用\n[BBOX-1758] 已使用\n[BBOX-1759] 已使用\n[BBOX-1760] 已使用\n[BBOX-1761] 已使用\n[BBOX-1762] 已使用\n[BBOX-1763] 已使用\n[BBOX-1764] 已使用\n[BBOX-1765] 已使用\n[BBOX-1766] 已使用\n[BBOX-1767] 已使用\n[BBOX-1768] 已使用\n[BBOX-1769] 已使用\n[BBOX-1770] 已使用\n[BBOX-1771] 已使用\n[BBOX-1772] 已使用\n[BBOX-1773] 已使用\n[BBOX-1774] 已使用\n[BBOX-1775] 已使用\n[BBOX-1776] 已使用\n[BBOX-1777] 已使用\n[BBOX-1778] 已使用\n[BBOX-1779] 已使用\n[BBOX-1780] 已使用\n[BBOX-1781] 已使用\n[BBOX-1782] 已使用\n[BBOX-1783] 已使用\n[BBOX-1784] 已使用\n[BBOX-1785] 已使用\n[BBOX-1786] 已使用\n[BBOX-1787] 已使用\n[BBOX-1788] 已使用\n[BBOX-1789] 已使用\n[BBOX-1790] 已使用\n[BBOX-1791] 已使用\n[BBOX-1792] 已使用\n[BBOX-1793] 已使用\n[BBOX-1794] 已使用\n[BBOX-1795] 已使用\n[BBOX-1796] 已使用\n[BBOX-1797] 已使用\n[BBOX-1798] 已使用\n[BBOX-1799] 已使用\n[BBOX-1800] 已使用\n[BBOX-1801] 已使用\n[BBOX-1802] 已使用\n[BBOX-1803] 已使用\n[BBOX-1804] 已使用\n[BBOX-1805] 已使用\n[BBOX-1806] 已使用\n[BBOX-1807] 已使用\n[BBOX-1808] 已使用\n[BBOX-1809] 已使用\n[BBOX-1810] 已使用\n[BBOX-1811] 已使用\n[BBOX-1812] 已使用\n[BBOX-1813] 已使用\n[BBOX-1814] 已使用\n[BBOX-1815] 已使用\n[BBOX-1816] 已使用\n[BBOX-1817] 已使用\n[BBOX-1818] 已使用\n[BBOX-1819] 已使用\n[BBOX-1820] 已使用\n[BBOX-1821] 已使用\n[BBOX-1822] 已使用\n[BBOX-1823] 已使用\n[BBOX-1824] 已使用\n[BBOX-1825] 已使用\n[BBOX-1826] 已使用\n[BBOX-1827] 已使用\n[BBOX-1828] 已使用\n[BBOX-1829] 已使用\n[BBOX-1830] 已使用\n[BBOX-1831] 已使用\n[BBOX-1832] 已使用\n[BBOX-1833] 已使用\n[BBOX-1834] 已使用\n[BBOX-1835] 已使用\n[BBOX-1836] 已使用\n[BBOX-1837] 已使用\n[BBOX-1838] 已使用\n[BBOX-1839] 已使用\n[BBOX-1840] 已使用\n[BBOX-1841] 已使用\n[BBOX-1842] 已使用\n[BBOX-1843] 已使用\n[BBOX-1844] 已使用\n[BBOX-1845] 已使用\n[BBOX-1846] 已使用\n[BBOX-1847] 已使用\n[BBOX-1848] 已使用\n[BBOX-1849] 已使用\n[BBOX-1850] 已使用\n[BBOX-1851] 已使用\n[BBOX-1852] 已使用\n[BBOX-1853] 已使用\n[BBOX-1854] 已使用\n[BBOX-1855] 已使用\n[BBOX-1856] 已使用\n[BBOX-1857] 已使用\n[BBOX-1858] 已使用\n[BBOX-1859] 已使用\n[BBOX-1860] 已使用\n[BBOX-1861] 已使用\n[BBOX-1862] 已使用\n[BBOX-1863] 已使用\n[BBOX-1864] 已使用\n[BBOX-1865] 已使用\n[BBOX-1866] 已使用\n[BBOX-1867] 已使用\n[BBOX-1868] 已使用\n[BBOX-1869] 已使用\n[BBOX-1870] 已使用\n[BBOX-1871] 已使用\n[BBOX-1872] 已使用\n[BBOX-1873] 已使用\n[BBOX-1874] 已使用\n[BBOX-1875] 已使用\n[BBOX-1876] 已使用\n[BBOX-1877] 已使用\n[BBOX-1878] 已使用\n[BBOX-1879] 已使用\n[BBOX-1880] 已使用\n[BBOX-1881] 已使用\n[BBOX-1882] 已使用\n[BBOX-1883] 已使用\n[BBOX-1884] 已使用\n[BBOX-1885] 已使用\n[BBOX-1886] 已使用\n[BBOX-1887] 已使用\n[BBOX-1888] 已使用\n[BBOX-1889] 已使用\n[BBOX-1890] 已使用\n[BBOX-1891] 已使用\n[BBOX-1892] 已使用\n[BBOX-1893] 已使用\n[BBOX-1894] 已使用\n[BBOX-1895] 已使用\n[BBOX-1896] 已使用\n[BBOX-1897] 已使用\n[BBOX-1898] 已使用\n[BBOX-1899] 已使用\n[BBOX-1900] 已使用\n[BBOX-1901] 已使用\n[BBOX-1902] 已使用\n[BBOX-1903] 已使用\n[BBOX-1904] 已使用\n[BBOX-1905] 已使用\n[BBOX-1906] 已使用\n[BBOX-1907] 已使用\n[BBOX-1908] 已使用\n[BBOX-1909] 已使用\n[BBOX-1910] 已使用\n[BBOX-1911] 已使用\n[BBOX-1912] 已使用\n[BBOX-1913] 已使用\n[BBOX-1914] 已使用\n[BBOX-1915] 已使用\n[BBOX-1916] 已使用\n[BBOX-1917] 已使用\n[BBOX-1918] 已使用\n[BBOX-1919] 已使用\n[BBOX-1920] 已使用\n[BBOX-1921] 已使用\n[BBOX-1922] 已使用\n[BBOX-1923] 已使用\n[BBOX-1924] 已使用\n[BBOX-1925] 已使用\n[BBOX-1926] 已使用\n[BBOX-1927] 已使用\n[BBOX-1928] 已使用\n[BBOX-1929] 已使用\n[BBOX-1930] 已使用\n[BBOX-1931] 已使用\n[BBOX-1932] 已使用\n[BBOX-1933] 已使用\n[BBOX-1934] 已使用\n[BBOX-1935] 已使用\n[BBOX-1936] 已使用\n[BBOX-1937] 已使用\n[BBOX-1938] 已使用\n[BBOX-1939] 已使用\n[BBOX-1940] 已使用\n[BBOX-1941] 已使用\n[BBOX-1942] 已使用\n[BBOX-1943] 已使用\n[BBOX-1944] 已使用\n[BBOX-1945] 已使用\n[BBOX-1946] 已使用\n[BBOX-1947] 已使用\n[BBOX-1948] 已使用\n[BBOX-1949] 已使用\n[BBOX-1950] 已使用\n[BBOX-1951] 已使用\n[BBOX-1952] 已使用\n[BBOX-1953] 已使用\n[BBOX-1954] 已使用\n[BBOX-1955] 已使用\n[BBOX-1956] 已使用\n[BBOX-1957] 已使用\n[BBOX-1958] 已使用\n[BBOX-1959] 已使用\n[BBOX-1960] 已使用\n[BBOX-1961] 已使用\n[BBOX-1962] 已使用\n[BBOX-1963] 已使用\n[BBOX-1964] 已使用\n[BBOX-1965] 已使用\n[BBOX-1966] 已使用\n[BBOX-1967] 已使用\n[BBOX-1968] 已使用\n[BBOX-1969] 已使用\n[BBOX-1970] 已使用\n[BBOX-1971] 已使用\n[BBOX-1972] 已使用\n[BBOX-1973] 已使用\n[BBOX-1974] 已使用\n[BBOX-1975] 已使用\n[BBOX-1976] 已使用\n[BBOX-1977] 已使用\n[BBOX-1978] 已使用\n[BBOX-1979] 已使用\n[BBOX-1980] 已使用\n[BBOX-1981] 已使用\n[BBOX-1982] 已使用\n[BBOX-1983] 已使用\n[BBOX-1984] 已使用\n[BBOX-1985] 已使用\n[BBOX-1986] 已使用\n[BBOX-1987] 已使用\n[BBOX-1988] 已使用\n[BBOX-1989] 已使用\n[BBOX-1990] 已使用\n[BBOX-1991] 已使用\n[BBOX-1992] 已使用\n[BBOX-1993] 已使用\n[BBOX-1994] 已使用\n[BBOX-1995] 已使用\n[BBOX-1996] 已使用\n[BBOX-1997] 已使用\n[BBOX-1998] 已使用\n[BBOX-1999] 已使用\n[BBOX-2000] 已使用\n[BBOX-2001] 已使用\n[BBOX-2002] 已使用\n[BBOX-2003] 已使用\n[BBOX-2004] 已使用\n[BBOX-2005] 已使用\n[BBOX-2006] 已使用\n[BBOX-2007] 已使用\n[BBOX-2008] 已使用\n[BBOX-2009] 已使用\n[BBOX-2010] 已使用\n[BBOX-2011] 已使用\n[BBOX-2012] 已使用\n[BBOX-2013] 已使用\n[BBOX-2014] 已使用\n[BBOX-2015] 已使用\n[BBOX-2016] 已使用\n[BBOX-2017] 已使用\n[BBOX-2018] 已使用\n[BBOX-2019] 已使用\n[BBOX-2020] 已使用\n[BBOX-2021] 已使用\n[BBOX-2022] 已使用\n[BBOX-2023] 已使用\n[BBOX-2024] 已使用\n[BBOX-2025] 已使用\n[BBOX-2026] 已使用\n[BBOX-2027] 已使用\n[BBOX-2028] 已使用\n[BBOX-2029] 已使用\n[BBOX-2030] 已使用\n[BBOX-2031] 已使用\n[BBOX-2032] 已使用\n[BBOX-2033] 已使用\n[BBOX-2034] 已使用\n[BBOX-2035] 已使用\n[BBOX-2036] 已使用\n[BBOX-2037] 已使用\n[BBOX-2038] 已使用\n[BBOX-2039] 已使用\n[BBOX-2040] 已使用\n[BBOX-2041] 已使用\n[BBOX-2042] 已使用\n[BBOX-2043] 已使用\n[BBOX-2044] 已使用\n[BBOX-2045] 已使用\n[BBOX-2046] 已使用\n[BBOX-2047] 已使用\n[BBOX-2048] 已使用\n[BBOX-2049] 已使用\n[BBOX-2050] 已使用\n[BBOX-2051] 已使用\n[BBOX-2052] 已使用\n[BBOX-2053] 已使用\n[BBOX-2054] 已使用\n[BBOX-2055] 已使用\n[BBOX-2056] 已使用\n[BBOX-2057] 已使用\n[BBOX-2058] 已使用\n[BBOX-2059] 已使用\n[BBOX-2060] 已使用\n[BBOX-2061] 已使用\n[BBOX-2062] 已使用\n[BBOX-2063] 已使用\n[BBOX-2064] 已使用\n[BBOX-2065] 已使用\n[BBOX-2066] 已使用\n[BBOX-2067] 已使用\n[BBOX-2068] 已使用\n[BBOX-2069] 已使用\n[BBOX-2070] 已使用\n[BBOX-2071] 已使用\n[BBOX-2072] 已使用\n[BBOX-2073] 已使用\n[BBOX-2074] 已使用\n[BBOX-2075] 已使用\n[BBOX-2076] 已使用\n[BBOX-2077] 已使用\n[BBOX-2078] 已使用\n[BBOX-2079] 已使用\n[BBOX-2080] 已使用\n[BBOX-2081] 已使用\n[BBOX-2082] 已使用\n[BBOX-2083] 已使用\n[BBOX-2084] 已使用\n[BBOX-2085] 已使用\n[BBOX-2086] 已使用\n[BBOX-2087] 已使用\n[BBOX-2088] 已使用\n[BBOX-2089] 已使用\n[BBOX-2090] 已使用\n[BBOX-2091] 已使用\n[BBOX-2092] 已使用\n[BBOX-2093] 已使用\n[BBOX-2094] 已使用\n[BBOX-2095] 已使用\n[BBOX-2096] 已使用\n[BBOX-2097] 已使用\n[BBOX-2098] 已使用\n[BBOX-2099] 已使用\n[BBOX-2100] 已使用\n[BBOX-2101] 已使用\n[BBOX-2102] 已使用\n[BBOX-2103] 已使用\n[BBOX-2104] 已使用\n[BBOX-2105] 已使用\n[BBOX-2106] 已使用\n[BBOX-2107] 已使用\n[BBOX-2108] 已使用\n[BBOX-2109] 已使用\n[BBOX-2110] 已使用\n[BBOX-2111] 已使用\n[BBOX-2112] 已使用\n[BBOX-2113] 已使用\n[BBOX-2114] 已使用\n[BBOX-2115] 已使用\n[BBOX-2116] 已使用\n[BBOX-2117] 已使用\n[BBOX-2118] 已使用\n[BBOX-2119] 已使用\n[BBOX-2120] 已使用\n[BBOX-2121] 已使用\n[BBOX-2122] 已使用\n[BBOX-2123] 已使用\n[BBOX-2124] 已使用\n[BBOX-2125] 已使用\n[BBOX-2126] 已使用\n[BBOX-2127] 已使用\n[BBOX-2128] 已使用\n[BBOX-2129] 已使用\n[BBOX-2130] 已使用\n[BBOX-2131] 已使用\n[BBOX-2132] 已使用\n[BBOX-2133] 已使用\n[BBOX-2134] 已使用\n[BBOX-2135] 已使用\n[BBOX-2136] 已使用\n[BBOX-2137] 已使用\n[BBOX-2138] 已使用\n[BBOX-2139] 已使用\n[BBOX-2140] 已使用\n[BBOX-2141] 已使用\n[BBOX-2142] 已使用\n[BBOX-2143] 已使用\n[BBOX-2144] 已使用\n[BBOX-2145] 已使用\n[BBOX-2146] 已使用\n[BBOX-2147] 已使用\n[BBOX-2148] 已使用\n[BBOX-2149] 已使用\n[BBOX-2150] 已使用\n[BBOX-2151] 已使用\n[BBOX-2152] 已使用\n[BBOX-2153] 已使用\n[BBOX-2154] 已使用\n[BBOX-2155] 已使用\n[BBOX-2156] 已使用\n[BBOX-2157] 已使用\n[BBOX-2158] 已使用\n[BBOX-2159] 已使用\n[BBOX-2160] 已使用\n[BBOX-2161] 已使用\n[BBOX-2162] 已使用\n[BBOX-2163] 已使用\n[BBOX-2164] 已使用\n[BBOX-2165] 已使用\n[BBOX-2166] 已使用\n[BBOX-2167] 已使用\n[BBOX-2168] 已使用\n[BBOX-2169] 已使用\n[BBOX-2170] 已使用\n[BBOX-2171] 已使用\n[BBOX-2172] 已使用\n[BBOX-2173] 已使用\n[BBOX-2174] 已使用\n[BBOX-2175] 已使用\n[BBOX-2176] 已使用\n[BBOX-2177] 已使用\n[BBOX-2178] 已使用\n[BBOX-2179] 已使用\n[BBOX-2180] 已使用\n[BBOX-2181] 已使用\n[BBOX-2182] 已使用\n[BBOX-2183] 已使用\n[BBOX-2184] 已使用\n[BBOX-2185] 已使用\n[BBOX-2186] 已使用\n[BBOX-2187] 已使用\n[BBOX-2188] 已使用\n[BBOX-2189] 已使用\n[BBOX-2190] 已使用\n[BBOX-2191] 已使用\n[BBOX-2192] 已使用\n[BBOX-2193] 已使用\n[BBOX-2194] 已使用\n[BBOX-2195] 已使用\n[BBOX-2196] 已使用\n[BBOX-2197] 已使用\n[BBOX-2198] 已使用\n[BBOX-2199] 已使用\n[BBOX-2200] 已使用\n[BBOX-2201] 已使用\n[BBOX-2202] 已使用\n[BBOX-2203] 已使用\n[BBOX-2204] 已使用\n[BBOX-2205] 已使用\n[BBOX-2206] 已使用\n[BBOX-2207] 已使用\n[BBOX-2208] 已使用\n[BBOX-2209] 已使用\n[BBOX-2210] 已使用\n[BBOX-2211] 已使用\n[BBOX-2212] 已使用\n[BBOX-2213] 已使用\n[BBOX-2214] 已使用\n[BBOX-2215] 已使用\n[BBOX-2216] 已使用\n[BBOX-2217] 已使用\n[BBOX-2218] 已使用\n[BBOX-2219] 已使用\n[BBOX-2220] 已使用\n[BBOX-2221] 已使用\n[BBOX-2222] 已使用\n[BBOX-2223] 已使用\n[BBOX-2224] 已使用\n[BBOX-2225] 已使用\n[BBOX-2226] 已使用\n[BBOX-2227] 已使用\n[BBOX-2228] 已使用\n[BBOX-2229] 已使用\n[BBOX-2230] 已使用\n[BBOX-2231] 已使用\n[BBOX-2232] 已使用\n[BBOX-2233] 已使用\n[BBOX-2234] 已使用\n[BBOX-2235] 已使用\n[BBOX-2236] 已使用\n[BBOX-2237] 已使用\n[BBOX-2238] 已使用\n[BBOX-2239] 已使用\n[BBOX-2240] 已使用\n[BBOX-2241] 已使用\n[BBOX-2242] 已使用\n[BBOX-2243] 已使用\n[BBOX-2244] 已使用\n[BBOX-2245] 已使用\n[BBOX-2246] 已使用\n[BBOX-2247] 已使用\n[BBOX-2248] 已使用\n[BBOX-2249] 已使用\n[BBOX-2250] 已使用\n[BBOX-2251] 已使用\n[BBOX-2252] 已使用\n[BBOX-2253] 已使用\n[BBOX-2254] 已使用\n[BBOX-2255] 已使用\n[BBOX-2256] 已使用\n[BBOX-2257] 已使用\n[BBOX-2258] 已使用\n[BBOX-2259] 已使用\n[BBOX-2260] 已使用\n[BBOX-2261] 已使用\n[BBOX-2262] 已使用\n[BBOX-2263] 已使用\n[BBOX-2264] 已使用\n[BBOX-2265] 已使用\n[BBOX-2266] 已使用\n[BBOX-2267] 已使用\n[BBOX-2268] 已使用\n[BBOX-2269] 已使用\n[BBOX-2270] 已使用\n[BBOX-2271] 已使用\n[BBOX-2272] 已使用\n[BBOX-2273] 已使用\n[BBOX-2274] 已使用\n[BBOX-2275] 已使用\n[BBOX-2276] 已使用\n[BBOX-2277] 已使用\n[BBOX-2278] 已使用\n[BBOX-2279] 已使用\n[BBOX-2280] 已使用\n[BBOX-2281] 已使用\n[BBOX-2282] 已使用\n[BBOX-2283] 已使用\n[BBOX-2284] 已使用\n[BBOX-2285] 已使用\n[BBOX-2286] 已使用\n[BBOX-2287] 已使用\n[BBOX-2288] 已使用\n[BBOX-2289] 已使用\n[BBOX-2290] 已使用\n[BBOX-2291] 已使用\n[BBOX-2292] 已使用\n[BBOX-2293] 已使用\n[BBOX-2294] 已使用\n[BBOX-2295] 已使用\n[BBOX-2296] 已使用\n[BBOX-2297] 已使用\n[BBOX-2298] 已使用\n[BBOX-2299] 已使用\n[BBOX-2300] 已使用\n[BBOX-2301] 已使用\n[BBOX-2302] 已使用\n[BBOX-2303] 已使用\n[BBOX-2304] 已使用\n[BBOX-2305] 已使用\n[BBOX-2306] 已使用\n[BBOX-2307] 已使用\n[BBOX-2308] 已使用\n[BBOX-2309] 已使用\n[BBOX-2310] 已使用\n[BBOX-2311] 已使用\n[BBOX-2312] 已使用\n[BBOX-2313] 已使用\n[BBOX-2314] 已使用\n[BBOX-2315] 已使用\n[BBOX-2316] 已使用\n[BBOX-2317] 已使用\n[BBOX-2318] 已使用\n[BBOX-2319] 已使用\n[BBOX-2320] 已使用\n[BBOX-2321] 已使用\n[BBOX-2322] 已使用\n[BBOX-2323] 已使用\n[BBOX-2324] 已使用\n[BBOX-2325] 已使用\n[BBOX-2326] 已使用\n[BBOX-2327] 已使用\n[BBOX-2328] 已使用\n[BBOX-2329] 已使用\n[BBOX-2330] 已使用\n[BBOX-2331] 已使用\n[BBOX-2332] 已使用\n[BBOX-2333] 已使用\n[BBOX-2334] 已使用\n[BBOX-2335] 已使用\n[BBOX-2336] 已使用\n[BBOX-2337] 已使用\n[BBOX-2338] 已使用\n[BBOX-2339] 已使用\n[BBOX-2340] 已使用\n[BBOX-2341] 已使用\n[BBOX-2342] 已使用\n[BBOX-2343] 已使用\n[BBOX-2344] 已���用\n[BBOX-2345] 已使用\n[BBOX-2346] 已使用\n[BBOX-2347] 已使用\n[BBOX-2348] 已使用\n[BBOX-2349] 已使用\n[BBOX-2350] 已使用\n[BBOX-2351] 已使用\n[BBOX-2352] 已使用\n[BBOX-2353] 已使用\n[BBOX-2354] 已使用\n[BBOX-2355] 已使用\n[BBOX-2356] 已使用\n[BBOX-2357] 已使用\n[BBOX-2358] 已使用\n[BBOX-2359] 已使用\n[BBOX-2360] 已使用\n[BBOX-2361] 已使用\n[BBOX-2362] 已使用\n[BBOX-2363] 已使用\n[BBOX-2364] 已使用\n[BBOX-2365] 已使用\n[BBOX-2366] 已使用\n[BBOX-2367] 已使用\n[BBOX-2368] 已使用\n[BBOX-2369] 已使用\n[BBOX-2370] 已使用\n[BBOX-2371] 已使用\n[BBOX-2372] 已使用\n[BBOX-2373] 已使用\n[BBOX-2374] 已使用\n[BBOX-2375] 已使用\n[BBOX-2376] 已使用\n[BBOX-2377] 已使用\n[BBOX-2378] 已使用\n[BBOX-2379] 已使用\n[BBOX-2380] 已使用\n[BBOX-2381] 已使用\n[BBOX-2382] 已使用\n[BBOX-2383] 已使用\n[BBOX-2384] 已使用\n[BBOX-2385] 已使用\n[BBOX-2386] 已使用\n[BBOX-2387] 已使用\n[BBOX-2388] 已使用\n[BBOX-2389] 已使用\n[BBOX-2390] 已使用\n[BBOX-2391] 已使用\n[BBOX-2392] 已使用\n[BBOX-2393] 已使用\n[BBOX-2394] 已使用\n[BBOX-2395] 已使用\n[BBOX-2396] 已使用\n[BBOX-2397] 已使用\n[BBOX-2398] 已使用\n[BBOX-2399] 已使用\n[BBOX-2400] 已使用\n[BBOX-2401] 已使用\n[BBOX-2402] 已使用\n[BBOX-2403] 已使用\n[BBOX-2404] 已使用\n[BBOX-2405] 已使用\n[BBOX-2406] 已使用\n[BBOX-2407] 已使用\n[BBOX-2408] 已使用\n[BBOX-2409] 已使用\n[BBOX-2410] 已使用\n[BBOX-2411] 已使用\n[BBOX-2412] 已使用\n[BBOX-2413] 已使用\n[BBOX-2414] 已使用\n[BBOX-2415] 已使用\n[BBOX-2416] 已使用\n[BBOX-2417] 已使用\n[BBOX-2418] 已使用\n[BBOX-2419] 已使用\n[BBOX-2420] 已使用\n[BBOX-2421] 已使用\n[BBOX-2422] 已使用\n[BBOX-2423] 已使用\n[BBOX-2424] 已使用\n[BBOX-2425] 已使用\n[BBOX-2426] 已使用\n[BBOX-2427] 已使用\n[BBOX-2428] 已使用\n[BBOX-2429] 已使用\n[BBOX-2430] 已使用\n[BBOX-2431] 已使用\n[BBOX-2432] 已使用\n[BBOX-2433] 已使用\n[BBOX-2434] 已使用\n[BBOX-2435] 已使用\n[BBOX-2436] 已使用\n[BBOX-2437] 已使用\n[BBOX-2438] 已使用\n[BBOX-2439] 已使用\n[BBOX-2440] 已使用\n[BBOX-2441] 已使用\n[BBOX-2442] 已使用\n[BBOX-2443] 已使用\n[BBOX-2444] 已使用\n[BBOX-2445] 已使用\n[BBOX-2446] 已使用\n[BBOX-2447] 已使用\n[BBOX-2448] 已使用\n[BBOX-2449] 已使用\n[BBOX-2450] 已使用\n[BBOX-2451] 已使用\n[BBOX-2452] 已使用\n[BBOX-2453] 已使用\n[BBOX-2454] 已使用\n[BBOX-2455] 已使用\n[BBOX-2456] 已使用\n[BBOX-2457] 已使用\n[BBOX-2458] 已使用\n[BBOX-2459] 已使用\n[BBOX-2460] 已使用\n[BBOX-2461] 已使用\n[BBOX-2462] 已使用\n[BBOX-2463] 已使用\n[BBOX-2464] 已使用\n[BBOX-2465] 已使用\n[BBOX-2466] 已使用\n[BBOX-2467] 已使用\n[BBOX-2468] 已使用\n[BBOX-2469] 已使用\n[BBOX-2470] 已使用\n[BBOX-2471] 已使用\n[BBOX-2472] 已使用\n[BBOX-2473] 已使用\n[BBOX-2474] 已使用\n[BBOX-2475] 已使用\n[BBOX-2476] 已使用\n[BBOX-2477] 已使用\n[BBOX-2478] 已使用\n[BBOX-2479] 已使用\n[BBOX-2480] 已使用\n[BBOX-2481] 已使用\n[BBOX-2482] 已使用\n[BBOX-2483] 已使用\n[BBOX-2484] 已使用\n[BBOX-2485] 已使用\n[BBOX-2486] 已使用\n[BBOX-2487] 已使用\n[BBOX-2488] 已使用\n[BBOX-2489] 已使用\n[BBOX-2490] 已使用\n[BBOX-2491] 已使用\n[BBOX-2492] 已使用\n[BBOX-2493] 已使用\n[BBOX-2494] 已使用\n[BBOX-2495] 已使用\n[BBOX-2496] 已使用\n[BBOX-2497] 已使用\n[BBOX-2498] 已使用\n[BBOX-2499] 已使用\n[BBOX-2500] 已使用\n[BBOX-2501] 已使用\n[BBOX-2502] 已使用\n[BBOX-2503] 已使用\n[BBOX-2504] 已使用\n[BBOX-2505] 已使用\n[BBOX-2506] 已使用\n[BBOX-2507] 已使用\n[BBOX-2508] 已使用\n[BBOX-2509] 已使用\n[BBOX-2510] 已使用\n[BBOX-2511] 已使用\n[BBOX-2512] 已使用\n[BBOX-2513] 已使用\n[BBOX-2514] 已使用\n[BBOX-2515] 已使用\n[BBOX-2516] 已使用\n[BBOX-2517] 已使用\n[BBOX-2518] 已使用\n[BBOX-2519] 已使用\n[BBOX-2520] 已使用\n[BBOX-2521] 已使用\n[BBOX-2522] 已使用\n[BBOX-2523] 已使用\n[BBOX-2524] 已使用\n[BBOX-2525] 已使用\n[BBOX-2526] 已使用\n[BBOX-2527] 已使用\n[BBOX-2528] 已使用\n[BBOX-2529] 已使用\n[BBOX-2530] 已使用\n[BBOX-2531] 已使用\n[BBOX-2532] 已使用\n[BBOX-2533] 已使用\n[BBOX-2534] 已使用\n[BBOX-2535] 已使用\n[BBOX-2536] 已使用\n[BBOX-2537] 已使用\n[BBOX-2538] 已使用\n[BBOX-2539] 已使用\n[BBOX-2540] 已使用\n[BBOX-2541] 已使用\n[BBOX-2542] 已使用\n[BBOX-2543] 已使用\n[BBOX-2544] 已使用\n[BBOX-2545] 已使用\n[BBOX-2546] 已使用\n[BBOX-2547] 已使用\n[BBOX-2548] 已使用\n[BBOX-2549] 已使用\n[BBOX-2550] 已使用\n[BBOX-2551] 已使用\n[BBOX-2552] 已使用\n[BBOX-2553] 已使用\n[BBOX-2554] 已使用\n[BBOX-2555] 已使用\n[BBOX-2556] 已使用\n[BBOX-2557] 已使用\n[BBOX-2558] 已使用\n[BBOX-2559] 已使用\n[BBOX-2560] 已使用\n[BBOX-2561] 已使用\n[BBOX-2562] 已使用\n[BBOX-2563] 已使用\n[BBOX-2564] 已使用\n[BBOX-2565] 已使用\n[BBOX-2566] 已使用\n[BBOX-2567] 已使用\n[BBOX-2568] 已使用\n[BBOX-2569] 已使用\n[BBOX-2570] 已使用\n[BBOX-2571] 已使用\n[BBOX-2572] 已使用\n[BBOX-2573] 已使用\n[BBOX-2574] 已使用\n[BBOX-2575] 已使用\n[BBOX-2576] 已使用\n[BBOX-2577] 已使用\n[BBOX-2578] 已使用\n[BBOX-2579] 已使用\n[BBOX-2580] 已使用\n[BBOX-2581] 已使用\n[BBOX-2582] 已使用\n[BBOX-2583] 已使用\n[BBOX-2584] 已使用\n[BBOX-2585] 已使用\n[BBOX-2586] 已使用\n[BBOX-2587] 已使用\n[BBOX-2588] 已使用\n[BBOX-2589] 已使用\n[BBOX-2590] 已使用\n[BBOX-2591] 已使用\n[BBOX-2592] 已使用\n[BBOX-2593] 已使用\n[BBOX-2594] 已使用\n[BBOX-2595] 已使用\n[BBOX-2596] 已使用\n[BBOX-2597] 已使用\n[BBOX-2598] 已使用\n[BBOX-2599] 已使用\n[BBOX-2600] 已使用\n[BBOX-2601] 已使用\n[BBOX-2602] 已使用\n[BBOX-2603] 已使用\n[BBOX-2604] 已使用\n[BBOX-2605] 已使用\n[BBOX-2606] 已使用\n[BBOX-2607] 已使用\n[BBOX-2608] 已使用\n[BBOX-2609] 已使用\n[BBOX-2610] 已使用\n[BBOX-2611] 已使用\n[BBOX-2612] 已使用\n[BBOX-2613] 已使用\n[BBOX-2614] 已使用\n[BBOX-2615] 已使用\n[BBOX-2616] 已使用\n[BBOX-2617] 已使用\n[BBOX-2618] 已使用\n[BBOX-2619] 已使用\n[BBOX-2620] 已使用\n[BBOX-2621] 已使用\n[BBOX-2622] 已使用\n[BBOX-2623] 已使用\n[BBOX-2624] 已使用\n[BBOX-2625] 已使用\n[BBOX-2626] 已使用\n[BBOX-2627] 已使用\n[BBOX-2628] 已使用\n[BBOX-2629] 已使用\n[BBOX-2630] 已使用\n[BBOX-2631] 已使用\n[BBOX-2632] 已使用\n[BBOX-2633] 已使用\n[BBOX-2634] 已使用\n[BBOX-2635] 已使用\n[BBOX-2636] 已使用\n[BBOX-2637] 已使用\n[BBOX-2638] 已使用\n[BBOX-2639] 已使用\n[BBOX-2640] 已使用\n[BBOX-2641] 已使用\n[BBOX-2642] 已使用\n[BBOX-2643] 已使用\n[BBOX-2644] 已使用\n[BBOX-2645] 已使用\n[BBOX-2646] 已使用\n[BBOX-2647] 已使用\n[BBOX-2648] 已使用\n[BBOX-2649] 已使用\n[BBOX-2650] 已使用\n[BBOX-2651] 已使用\n[BBOX-2652] 已使用\n[BBOX-2653] 已使用\n[BBOX-2654] 已使用\n[BBOX-2655] 已使用\n[BBOX-2656] 已使用\n[BBOX-2657] 已使用\n[BBOX-2658] 已使用\n[BBOX-2659] 已使用\n[BBOX-2660] 已使用\n[BBOX-2661] 已使用\n[BBOX-2662] 已使用\n[BBOX-2663] 已使用\n[BBOX-2664] 已使用\n[BBOX-2665] 已使用\n[BBOX-2666] 已使用\n[BBOX-2667] 已使用\n[BBOX-2668] 已使用\n[BBOX-2669] 已使用\n[BBOX-2670] 已使用\n[BBOX-2671] 已使用\n[BBOX-2672] 已使用\n[BBOX-2673] 已使用\n[BBOX-2674] 已使用\n[BBOX-2675] 已使用\n[BBOX-2676] 已使用\n[BBOX-2677] 已使用\n[BBOX-2678] 已使用\n[BBOX-2679] 已使用\n[BBOX-2680] 已使用\n[BBOX-2681] 已使用\n[BBOX-2682] 已使用\n[BBOX-2683] 已使用\n[BBOX-2684] 已使用\n[BBOX-2685] 已使用\n[BBOX-2686] 已使用\n[BBOX-2687] 已使用\n[BBOX-2688] 已使用\n[BBOX-2689] 已使用\n[BBOX-2690] 已使用\n[BBOX-2691] 已使用\n[BBOX-2692] 已使用\n[BBOX-2693] 已使用\n[BBOX-2694] 已使用\n[BBOX-2695] 已使用\n[BBOX-2696] 已使用\n[BBOX-2697] 已使用\n[BBOX-2698] 已使用\n[BBOX-2699] 已使用\n[BBOX-2700] 已使用\n[BBOX-2701] 已使用\n[BBOX-2702] 已使用\n[BBOX-2703] 已使用\n[BBOX-2704] 已使用\n[BBOX-2705] 已使用\n[BBOX-2706] 已使用\n[BBOX-2707] 已使用\n[BBOX-2708] 已使用\n[BBOX-2709] 已使用\n[BBOX-2710] 已使用\n[BBOX-2711] 已使用\n[BBOX-2712] 已使用\n[BBOX-2713] 已使用\n[BBOX-2714] 已使用\n[BBOX-2715] 已使用\n[BBOX-2716] 已使用\n[BBOX-2717] 已使用\n[BBOX-2718] 已使用\n[BBOX-2719] 已使用\n[BBOX-2720] 已使用\n[BBOX-2721] 已使用\n[BBOX-2722] 已使用\n[BBOX-2723] 已使用\n[BBOX-2724] 已使用\n[BBOX-2725] 已使用\n[BBOX-2726] 已使用\n[BBOX-2727] 已使用\n[BBOX-2728] 已使用\n[BBOX-2729] 已使用\n[BBOX-2730] 已使用\n[BBOX-2731] 已使用\n[BBOX-2732] 已使用\n[BBOX-2733] 已使用\n[BBOX-2734] 已使用\n[BBOX-2735] 已使用\n[BBOX-2736] 已使用\n[BBOX-2737] 已使用\n[BBOX-2738] 已使用\n[BBOX-2739] 已使用\n[BBOX-2740] 已使用\n[BBOX-2741] 已使用\n[BBOX-2742] 已使用\n[BBOX-2743] 已使用\n[BBOX-2744] 已使用\n[BBOX-2745] 已使用\n[BBOX-2746] 已使用\n[BBOX-2747] 已使用\n[BBOX-2748] 已使用\n[BBOX-2749] 已使用\n[BBOX-2750] 已使用\n[BBOX-2751] 已使用\n[BBOX-2752] 已使用\n[BBOX-2753] 已使用\n[BBOX-2754] 已使用\n[BBOX-2755] 已使用\n[BBOX-2756] 已使用\n[BBOX-2757] 已使用\n[BBOX-2758] 已使用\n[BBOX-2759] 已使用\n[BBOX-2760] 已使用\n[BBOX-2761] 已使用\n[BBOX-2762] 已使用\n[BBOX-2763] 已使用\n[BBOX-2764] 已使用\n[BBOX-2765] 已使用\n[BBOX-2766] 已使用\n[BBOX-2767] 已使用\n[BBOX-2768] 已使用\n[BBOX-2769] 已使用\n[BBOX-2770] 已使用\n[BBOX-2771] 已使用\n[BBOX-2772] 已使用\n[BBOX-2773] 已使用\n[BBOX-2774] 已使用\n[BBOX-2775] 已使用\n[BBOX-2776] 已使用\n[BBOX-2777] 已使用\n[BBOX-2778] 已使用\n[BBOX-2779] 已使用\n[BBOX-2780] 已使用\n[BBOX-2781] 已使用\n[BBOX-2782] 已使用\n[BBOX-2783] 已使用\n[BBOX-2784] 已使用\n[BBOX-2785] 已使用\n[BBOX-2786] 已使用\n[BBOX-2787] 已使用\n[BBOX-2788] 已使用\n[BBOX-2789] 已使用\n[BBOX-2790] 已使用\n[BBOX-2791] 已使用\n[BBOX-2792] 已使用\n[BBOX-2793] 已使用\n[BBOX-2794] 已使用\n[BBOX-2795] 已使用\n[BBOX-2796] 已使用\n[BBOX-2797] 已使用\n[BBOX-2798] 已使用\n[BBOX-2799] 已使用\n[BBOX-2800] 已使用\n[BBOX-2801] 已使用\n[BBOX-2802] 已使用\n[BBOX-2803] 已使用\n[BBOX-2804] 已使用\n[BBOX-2805] 已使用\n[BBOX-2806] 已使用\n[BBOX-2807] 已使用\n[BBOX-2808] 已使用\n[BBOX-2809] 已使用\n[BBOX-2810] 已使用\n[BBOX-2811] 已使用\n[BBOX-2812] 已使用\n[BBOX-2813] 已使用\n[BBOX-2814] 已使用\n[BBOX-2815] 已使用\n[BBOX-2816] 已使用\n[BBOX-2817] 已使用\n[BBOX-2818] 已使用\n[BBOX-2819] 已使用\n[BBOX-2820] 已使用\n[BBOX-2821] 已使用\n[BBOX-2822] 已使用\n[BBOX-2823] 已使用\n[BBOX-2824] 已使用\n[BBOX-2825] 已使用\n[BBOX-2826] 已使用\n[BBOX-2827] 已使用\n[BBOX-2828] 已使用\n[BBOX-2829] 已使用\n[BBOX-2830] 已使用\n[BBOX-2831] 已使用\n[BBOX-2832] 已使用\n[BBOX-2833] 已使用\n[BBOX-2834] 已使用\n[BBOX-2835] 已使用\n[BBOX-2836] 已使用\n[BBOX-2837] 已使用\n[BBOX-2838] 已使用\n[BBOX-2839] 已使用\n[BBOX-2840] 已使用\n[BBOX-2841] 已使用\n[BBOX-2842] 已使用\n[BBOX-2843] 已使用\n[BBOX-2844] 已使用\n[BBOX-2845] 已使用\n[BBOX-2846] 已使用\n[BBOX-2847] 已使用\n[BBOX-2848] 已使用\n[BBOX-2849] 已使用\n[BBOX-2850] 已使用\n[BBOX-2851] 已使用\n[BBOX-2852] 已使用\n[BBOX-2853] 已使用\n[BBOX-2854] 已使用\n[BBOX-2855] 已使用\n[BBOX-2856] 已使用\n[BBOX-2857] 已使用\n[BBOX-2858] 已使用\n[BBOX-2859] 已使用\n[BBOX-2860] 已使用\n[BBOX-2861] 已使用\n[BBOX-2862] 已使用\n[BBOX-2863] 已使用\n[BBOX-2864] 已使用\n[BBOX-2865] 已使用\n[BBOX-2866] 已使用\n[BBOX-2867] 已使用\n[BBOX-2868] 已使用\n[BBOX-2869] 已使用\n[BBOX-2870] 已使用\n[BBOX-2871] 已使用\n[BBOX-2872] 已使用\n[BBOX-2873] 已使用\n[BBOX-2874] 已使用\n[BBOX-2875] 已使用\n[BBOX-2876] 已使用\n[BBOX-2877] 已使用\n[BBOX-2878] 已使用\n[BBOX-2879] 已使用\n[BBOX-2880] 已使用\n[BBOX-2881] 已使用\n[BBOX-2882] 已使用\n[BBOX-2883] 已使用\n[BBOX-2884] 已使用\n[BBOX-2885] 已使用\n[BBOX-2886] 已使用\n[BBOX-2887] 已使用\n[BBOX-2888] 已使用\n[BBOX-2889] 已使用\n[BBOX-2890] 已使用\n[BBOX-2891] 已使用\n[BBOX-2892] 已使用\n[BBOX-2893] 已使用\n[BBOX-2894] 已使用\n[BBOX-2895] 已使用\n[BBOX-2896] 已使用\n[BBOX-2897] 已使用\n[BBOX-2898] 已使用\n[BBOX-2899] 已使用\n[BBOX-2900] 已使用\n[BBOX-2901] 已使用\n[BBOX-2902] 已使用\n[BBOX-2903] 已使用\n[BBOX-2904] 已使用\n[BBOX-2905] 已使用\n[BBOX-2906] 已使用\n[BBOX-2907] 已使用\n[BBOX-2908] 已使用\n[BBOX-2909] 已使用\n[BBOX-2910] 已使用\n[BBOX-2911] 已使用\n[BBOX-2912] 已使用\n[BBOX-2913] 已使用\n[BBOX-2914] 已使用\n[BBOX-2915] 已使用\n[BBOX-2916] 已使用\n[BBOX-2917] 已使用\n[BBOX-2918] 已使用\n[BBOX-2919] 已使用\n[BBOX-2920] 已使用\n[BBOX-2921] 已使用\n[BBOX-2922] 已使用\n[BBOX-2923] 已使用\n[BBOX-2924] 已使用\n[BBOX-2925] 已使用\n[BBOX-2926] 已使用\n[BBOX-2927] 已使用\n[BBOX-2928] 已使用\n[BBOX-2929] 已使用\n[BBOX-2930] 已使用\n[BBOX-2931] 已使用\n[BBOX-2932] 已使用\n[BBOX-2933] 已使用\n[BBOX-2934] 已使用\n[BBOX-2935] 已使用\n[BBOX-2936] 已使用\n[BBOX-2937] 已使用\n[BBOX-2938] 已使用\n[BBOX-2939] 已使用\n[BBOX-2940] 已使用\n[BBOX-2941] 已使用\n[BBOX-2942] 已使用\n[BBOX-2943] 已使用\n[BBOX-2944] 已使用\n[BBOX-2945] 已使用\n[BBOX-2946] 已使用\n[BBOX-2947] 已使用\n[BBOX-2948] 已使用\n[BBOX-2949] 已使用\n[BBOX-2950] 已使用\n[BBOX-2951] 已使用\n[BBOX-2952] 已使用\n[BBOX-2953] 已使用\n[BBOX-2954] 已使用\n[BBOX-2955] 已使用\n[BBOX-2956] 已使用\n[BBOX-2957] 已使用\n[BBOX-2958] 已使用\n[BBOX-2959] 已使用\n[BBOX-2960] 已使用\n[BBOX-2961] 已使用\n[BBOX-2962] 已使用\n[BBOX-2963] 已使用\n[BBOX-2964] 已使用\n[BBOX-2965] 已使用\n[BBOX-2966] 已使用\n[BBOX-2967] 已使用\n[BBOX-2968] 已使用\n[BBOX-2969] 已使用\n[BBOX-2970] 已使用\n[BBOX-2971] 已使用\n[BBOX-2972] 已使用\n[BBOX-2973] 已使用\n[BBOX-2974] 已使用\n[BBOX-2975] 已使用\n[BBOX-2976] 已使用\n[BBOX-2977] 已使用\n[BBOX-2978] 已使用\n[BBOX-2979] 已使用\n[BBOX-2980] 已使用\n[BBOX-2981] 已使用\n[BBOX-2982] 已使用\n[BBOX-2983] 已使用\n[BBOX-2984] 已使用\n[BBOX-2985] 已使用\n[BBOX-2986] 已使用\n[BBOX-2987] 已使用\n[BBOX-2988] 已使用\n[BBOX-2989] 已使用\n[BBOX-2990] 已使用\n[BBOX-2991] 已使用\n[BBOX-2992] 已使用\n[BBOX-2993] 已使用\n[BBOX-2994] 已使用\n[BBOX-2995] 已使用\n[BBOX-2996] 已使用\n[BBOX-2997] 已使用\n[BBOX-2998] 已使用\n[BBOX-2999] 已使用\n[BBOX-3000] 已使用\n[BBOX-3001] 已使用\n[BBOX-3002] 已使用\n[BBOX-3003] 已使用\n[BBOX-3004] 已使用\n[BBOX-3005] 已使用\n[BBOX-3006] 已使用\n[BBOX-3007] 已使用\n[BBOX-3008] 已使用\n[BBOX-3009] 已使用\n[BBOX-3010] 已使用\n[BBOX-3011] 已使用\n[BBOX-3012] 已使用\n[BBOX-3013] 已使用\n[BBOX-3014] 已使用\n[BBOX-3015] 已使用\n[BBOX-3016] 已使用\n[BBOX-3017] 已使用\n[BBOX-3018] 已使用\n[BBOX-3019] 已使用\n[BBOX-3020] 已使用\n[BBOX-3021] 已使用\n[BBOX-3022] 已使用\n[BBOX-3023] 已使用\n[BBOX-3024] 已使用\n[BBOX-3025] 已使用\n[BBOX-3026] 已使用\n[BBOX-3027] 已使用\n[BBOX-3028] 已使用\n[BBOX-3029] 已使用\n[BBOX-3030] 已使用\n[BBOX-3031] 已使用\n[BBOX-3032] 已使用\n[BBOX-3033] 已使用\n[BBOX-3034] 已使用\n[BBOX-3035] 已使用\n[BBOX-3036] 已使用\n[BBOX-3037] 已使用\n[BBOX-3038] 已使用\n[BBOX-3039] 已使用\n[BBOX-3040] 已使用\n[BBOX-3041] 已使用\n[BBOX-3042] 已使用\n[BBOX-3043] 已使用\n[BBOX-3044] 已使用\n[BBOX-3045] 已使用\n[BBOX-3046] 已使用\n[BBOX-3047] 已使用\n[BBOX-3048] 已使用\n[BBOX-3049] 已使用\n[BBOX-3050] 已使用\n[BBOX-3051] 已使用\n[BBOX-3052] 已使用\n[BBOX-3053] 已使用\n[BBOX-3054] 已使用\n[BBOX-3055] 已使用\n[BBOX-3056] 已使用\n[BBOX-3057] 已使用\n[BBOX-3058] 已使用\n[BBOX-3059] 已使用\n[BBOX-3060] 已使用\n[BBOX-3061] 已使用\n[BBOX-3062] 已使用\n[BBOX-3063] 已使用\n[BBOX-3064] 已使用\n[BBOX-3065] 已使用\n[BBOX-3066] 已使用\n[BBOX-3067] 已使用\n[BBOX-3068] 已使用\n[BBOX-3069] 已使用\n[BBOX-3070] 已使用\n[BBOX-3071] 已使用\n[BBOX-3072] 已使用\n[BBOX-3073] 已使用\n[BBOX-3074] 已使用\n[BBOX-3075] 已使用\n[BBOX-3076] 已使用\n[BBOX-3077] 已使用\n[BBOX-3078] 已使用\n[BBOX-3079] 已使用\n[BBOX-3080] 已使用\n[BBOX-3081] 已使用\n[BBOX-3082] 已使用\n[BBOX-3083] 已使用\n[BBOX-3084] 已使用\n[BBOX-3085] 已使用\n[BBOX-3086] 已使用\n[BBOX-3087] 已使用\n[BBOX-3088] 已使用\n[BBOX-3089] 已使用\n[BBOX-3090] 已使用\n[BBOX-3091] 已使用\n[BBOX-3092] 已使用\n[BBOX-3093] 已使用\n[BBOX-3094] 已使用\n[BBOX-3095] 已使用\n[BBOX-3096] 已使用\n[BBOX-3097] 已使用\n[BBOX-3098] 已使用\n[BBOX-3099] 已使用\n[BBOX-3100] 已使用\n[BBOX-3101] 已使用\n[BBOX-3102] 已使用\n[BBOX-3103] 已使用\n[BBOX-3104] 已使用\n[BBOX-3105] 已使用\n[BBOX-3106] 已使用\n[BBOX-3107] 已使用\n[BBOX-3108] 已使用\n[BBOX-3109] 已使用\n[BBOX-3110] 已使用\n[BBOX-3111] 已使用\n[BBOX-3112] 已使用\n[BBOX-3113] 已使用\n[BBOX-3114] 已使用\n[BBOX-3115] 已使用\n[BBOX-3116] 已使用\n[BBOX-3117] 已使用\n[BBOX-3118] 已使用\n[BBOX-3119] 已使用\n[BBOX-3120] 已使用\n[BBOX-3121] 已使用\n[BBOX-3122] 已使用\n[BBOX-3123] 已使用\n[BBOX-3124] 已使用\n[BBOX-3125] 已使用\n[BBOX-3126] 已使用\n[BBOX-3127] 已使用\n[BBOX-3128] 已使用\n[BBOX-3129] 已使用\n[BBOX-3130] 已使用\n[BBOX-3131] 已使用\n[BBOX-3132] 已使用\n[BBOX-3133] 已使用\n[BBOX-3134] 已使用\n[BBOX-3135] 已使用\n[BBOX-3136] 已使用\n[BBOX-3137] 已使用\n[BBOX-3138] 已使用\n[BBOX-3139] 已使用\n[BBOX-3140] 已使用\n[BBOX-3141] 已使用\n[BBOX-3142] 已使用\n[BBOX-3143] 已使用\n[BBOX-3144] 已使用\n[BBOX-3145] 已使用\n[BBOX-3146] 已使用\n[BBOX-3147] 已使用\n[BBOX-3148] 已使用\n[BBOX-3149] 已使用\n[BBOX-3150] 已使用\n[BBOX-3151] 已使用\n[BBOX-3152] 已使用\n[BBOX-3153] 已使用\n[BBOX-3154] 已使用\n[BBOX-3155] 已使用\n[BBOX-3156] 已使用\n[BBOX-3157] 已使用\n[BBOX-3158] 已使用\n[BBOX-3159] 已使用\n[BBOX-3160] 已使用\n[BBOX-3161] 已使用\n[BBOX-3162] 已使用\n[BBOX-3163] 已使用\n[BBOX-3164] 已使用\n[BBOX-3165] 已使用\n[BBOX-3166] 已使用\n[BBOX-3167] 已使用\n[BBOX-3168] 已使用\n[BBOX-3169] 已使用\n[BBOX-3170] 已使用\n[BBOX-3171] 已使用\n[BBOX-3172] 已使用\n[BBOX-3173] 已使用\n[BBOX-3174] 已使用\n[BBOX-3175] 已使用\n[BBOX-3176] 已使用\n[BBOX-3177] 已使用\n[BBOX-3178] 已使用\n[BBOX-3179] 已使用\n[BBOX-3180] 已使用\n[BBOX-3181] 已使用\n[BBOX-3182] 已使用\n[BBOX-3183] 已使用\n[BBOX-3184] 已使用\n[BBOX-3185] 已使用\n[BBOX-3186] 已使用\n[BBOX-3187] 已使用\n[BBOX-3188] 已使用\n[BBOX-3189] 已使用\n[BBOX-3190] 已使用\n[BBOX-3191] 已使用\n[BBOX-3192] 已使用\n[BBOX-3193] 已使用\n[BBOX-3194] 已使用\n[BBOX-3195] 已使用\n[BBOX-3196] 已使用\n[BBOX-3197] 已使用\n[BBOX-3198] 已使用\n[BBOX-3199] 已使用\n[BBOX-3200] 已使用\n[BBOX-3201] 已使用\n[BBOX-3202] 已使用\n[BBOX-3203] 已使用\n[BBOX-3204] 已使用\n[BBOX-3205] 已使用\n[BBOX-3206] 已使用\n[BBOX-3207] 已使用\n[BBOX-3208] 已使用\n[BBOX-3209] 已使用\n[BBOX-3210] 已使用\n[BBOX-3211] 已使用\n[BBOX-3212] 已使用\n[BBOX-3213] 已使用\n[BBOX-3214] 已使用\n[BBOX-3215] 已使用\n[BBOX-3216] 已使用\n[BBOX-3217] 已使用\n[BBOX-3218] 已使用\n[BBOX-3219] 已使用\n[BBOX-3220] 已使用\n[BBOX-3221] 已使用\n[BBOX-3222] 已使用\n[BBOX-3223] 已使用\n[BBOX-3224] 已使用\n[BBOX-3225] 已使用\n[BBOX-3226] 已使用\n[BBOX-3227] 已使用\n[BBOX-3228] 已使用\n[BBOX-3229] 已使用\n[BBOX-3230] 已使用\n[BBOX-3231] 已使用\n[BBOX-3232] 已使用\n[BBOX-3233] 已使用\n[BBOX-3234] 已使用\n[BBOX-3235] 已使用\n[BBOX-3236] 已使用\n[BBOX-3237] 已使用\n[BBOX-3238] 已使用\n[BBOX-3239] 已使用\n[BBOX-3240] 已使用\n[BBOX-3241] 已使用\n[BBOX-3242] 已使用\n[BBOX-3243] 已使用\n[BBOX-3244] 已使用\n[BBOX-3245] 已使用\n[BBOX-3246] 已使用\n[BBOX-3247] 已使用\n[BBOX-3248] 已使用\n[BBOX-3249] 已使用\n[BBOX-3250] 已使用\n[BBOX-3251] 已使用\n[BBOX-3252] 已使用\n[BBOX-3253] 已使用\n[BBOX-3254] 已使用\n[BBOX-3255] 已使用\n[BBOX-3256] 已使用\n[BBOX-3257] 已使用\n[BBOX-3258] 已使用\n[BBOX-3259] 已使用\n[BBOX-3260] 已使用\n[BBOX-3261] 已使用\n[BBOX-3262] 已使用\n[BBOX-3263] 已使用\n[BBOX-3264] 已使用\n[BBOX-3265] 已使用\n[BBOX-3266] 已使用\n[BBOX-3267] 已使用\n[BBOX-3268] 已使用\n[BBOX-3269] 已使用\n[BBOX-3270] 已使用\n[BBOX-3271] 已使用\n[BBOX-3272] 已使用\n[BBOX-3273] 已使用\n[BBOX-3274] 已使用\n[BBOX-3275] 已使用\n[BBOX-3276] 已使用\n[BBOX-3277] 已使用\n[BBOX-3278] 已使用\n[BBOX-3279] 已使用\n[BBOX-3280] 已使用\n[BBOX-3281] 已使用\n[BBOX-3282] 已使用\n[BBOX-3283] 已使用\n[BBOX-3284] 已使用\n[BBOX-3285] 已使用\n[BBOX-3286] 已使用\n[BBOX-3287] 已使用\n[BBOX-3288] 已使用\n[BBOX-3289] 已使用\n[BBOX-3290] 已使用\n[BBOX-3291] 已使用\n[BBOX-3292] 已使用\n[BBOX-3293] 已使用\n[BBOX-3294] 已使用\n[BBOX-3295] 已使用\n[BBOX-3296] 已使用\n[BBOX-3297] 已使用\n[BBOX-3298] 已使用\n[BBOX-3299] 已使用\n[BBOX-3300] 已使用\n[BBOX-3301] 已使用\n[BBOX-3302] 已使用\n[BBOX-3303] 已使用\n[BBOX-3304] 已使用\n[BBOX-3305] 已使用\n[BBOX-3306] 已使用\n[BBOX-3307] 已使用\n[BBOX-3308] 已使用\n[BBOX-3309] 已使用\n[BBOX-3310] 已使用\n[BBOX-3311] 已使用\n[BBOX-3312] 已使用\n[BBOX-3313] 已使用\n[BBOX-3314] 已使用\n[BBOX-3315] 已使用\n[BBOX-3316] 已使用\n[BBOX-3317] 已使用\n[BBOX-3318] 已使用\n[BBOX-3319] 已使用\n[BBOX-3320] 已使用\n[BBOX-3321] 已使用\n[BBOX-3322] 已使用\n[BBOX-3323] 已使用\n[BBOX-3324] 已使用\n[BBOX-3325] 已使用\n[BBOX-3326] 已使用\n[BBOX-3327] 已使用\n[BBOX-3328] 已使用\n[BBOX-3329] 已使用\n[BBOX-3330] 已使用\n[BBOX-3331] 已使用\n[BBOX-3332] 已使用\n[BBOX-3333] 已使用\n[BBOX-3334] 已使用\n[BBOX-3335] 已使用\n[BBOX-3336] 已使用\n[BBOX-3337] 已使用\n[BBOX-3338] 已使用\n[BBOX-3339] 已使用\n[BBOX-3340] 已使用\n[BBOX-3341] 已使用\n[BBOX-3342] 已使用\n[BBOX-3343] 已使用\n[BBOX-3344] 已使用\n[BBOX-3345] 已使用\n[BBOX-3346] 已使用\n[BBOX-3347] 已使用\n[BBOX-3348] 已使用\n[BBOX-3349] 已使用\n[BBOX-3350] 已使用\n[BBOX-3351] 已使用\n[BBOX-3352] 已使用\n[BBOX-3353] 已使用\n[BBOX-3354] 已使用\n[BBOX-3355] 已使用\n[BBOX-3356] 已使用\n[BBOX-3357] 已使用\n[BBOX-3358] 已使用\n[BBOX-3359] 已使用\n[BBOX-3360] 已使用\n[BBOX-3361] 已使用\n[BBOX-3362] 已使用\n[BBOX-3363] 已使用\n[BBOX-3364] 已使用\n[BBOX-3365] 已使用\n[BBOX-3366] 已使用\n[BBOX-3367] 已使用\n[BBOX-3368] 已使用\n[BBOX-3369] 已使用\n[BBOX-3370] 已使用\n[BBOX-3371] 已使用\n[BBOX-3372] 已使用\n[BBOX-3373] 已使用\n[BBOX-3374] 已使用\n[BBOX-3375] 已使用\n[BBOX-3376] 已使用\n[BBOX-3377] 已使用\n[BBOX-3378] 已使用\n[BBOX-3379] 已使用\n[BBOX-3380] 已使用\n[BBOX-3381] 已使用\n[BBOX-3382] 已使用\n[BBOX-3383] 已使用\n[BBOX-3384] 已使用\n[BBOX-3385] 已使用\n[BBOX-3386] 已使用\n[BBOX-3387] 已使用\n[BBOX-3388] 已使用\n[BBOX-3389] 已使用\n[BBOX-3390] 已使用\n[BBOX-3391] 已使用\n[BBOX-3392] 已使用\n[BBOX-3393] 已使用\n[BBOX-3394] 已使用\n[BBOX-3395] 已使用\n[BBOX-3396] 已使用\n[BBOX-3397] 已使用\n[BBOX-3398] 已使用\n[BBOX-3399] 已使用\n[BBOX-3400] 已使用\n[BBOX-3401] 已使用\n[BBOX-3402] 已使用\n[BBOX-3403] 已使用\n[BBOX-3404] 已使用\n[BBOX-3405] 已使用\n[BBOX-3406] 已使用\n[BBOX-3407] 已使用\n[BBOX-3408] 已使用\n[BBOX-3409] 已使用\n[BBOX-3410] 已使用\n[BBOX-3411] 已使用\n[BBOX-3412] 已使用\n[BBOX-3413] 已使用\n[BBOX-3414] 已使用\n[BBOX-3415] 已使用\n[BBOX-3416] 已使用\n[BBOX-3417] 已使用\n[BBOX-3418] 已使用\n[BBOX-3419] 已使用\n[BBOX-3420] 已使用\n[BBOX-3421] 已使用\n[BBOX-3422] 已使用\n[BBOX-3423] 已使用\n[BBOX-3424] 已使用\n[BBOX-3425] 已使用\n[BBOX-3426] 已使用\n[BBOX-3427] 已使用\n[BBOX-3428] 已使用\n[BBOX-3429] 已使用\n[BBOX-3430] 已使用\n[BBOX-3431] 已使用\n[BBOX-3432] 已使用\n[BBOX-3433] 已使用\n[BBOX-3434] 已使用\n[BBOX-3435] 已使用\n[BBOX-3436] 已使用\n[BBOX-3437] 已使用\n[BBOX-3438] 已使用\n[BBOX-3439] 已使用\n[BBOX-3440] 已使用\n[BBOX-3441] 已使用\n[BBOX-3442] 已使用\n[BBOX-3443] 已使用\n[BBOX-3444] 已使用\n[BBOX-3445] 已使用\n[BBOX-3446] 已使用\n[BBOX-3447] 已使用\n[BBOX-3448] 已使用\n[BBOX-3449] 已使用\n[BBOX-3450] 已使用\n[BBOX-3451] 已使用\n[BBOX-3452] 已使用\n[BBOX-3453] 已使用\n[BBOX-3454] 已使用\n[BBOX-3455] 已使用\n[BBOX-3456] 已使用\n[BBOX-3457] 已使用\n[BBOX-3458] 已使用\n[BBOX-3459] 已使用\n[BBOX-3460] 已使用\n[BBOX-3461] 已使用\n[BBOX-3462] 已使用\n[BBOX-3463] 已使用\n[BBOX-3464] 已使用\n[BBOX-3465] 已使用\n[BBOX-3466] 已使用\n[BBOX-3467] 已使用\n[BBOX-3468] 已使用\n[BBOX-3469] 已使用\n[BBOX-3470] 已使用\n[BBOX-3471] 已使用\n[BBOX-3472] 已使用\n[BBOX-3473] 已使用\n[BBOX-3474] 已使用\n[BBOX-3475] 已使用\n[BBOX-3476] 已使用\n[BBOX-3477] 已使用\n[BBOX-3478] 已使用\n[BBOX-3479] 已使用\n[BBOX-3480] 已使用\n[BBOX-3481] 已使用\n[BBOX-3482] 已使用\n[BBOX-3483] 已使用\n[BBOX-3484] 已使用\n[BBOX-3485] 已使用\n[BBOX-3486] 已使用\n[BBOX-3487] 已使用\n[BBOX-3488] 已使用\n[BBOX-3489] 已使用\n[BBOX-3490] 已使用\n[BBOX-3491] 已使用\n[BBOX-3492] 已使用\n[BBOX-3493] 已使用\n[BBOX-3494] 已使用\n[BBOX-3495] 已使用\n[BBOX-3496] 已使用\n[BBOX-3497] 已使用\n[BBOX-3498] 已使用\n[BBOX-3499] 已使用\n[BBOX-3500] 已使用\n[BBOX-3501] 已使用\n[BBOX-3502] 已使用\n[BBOX-3503] 已使用\n[BBOX-3504] 已使用\n[BBOX-3505] 已使用\n[BBOX-3506] 已使用\n[BBOX-3507] 已使用\n[BBOX-3508] 已使用\n[BBOX-3509] 已使用\n[BBOX-3510] 已使用\n[BBOX-3511] 已使用\n[BBOX-3512] 已使用\n[BBOX-3513] 已使用\n[BBOX-3514] 已使用\n[BBOX-3515] 已使用\n[BBOX-3516] 已使用\n[BBOX-3517] 已使用\n[BBOX-3518] 已使用\n[BBOX-3519] 已使用\n[BBOX-3520] 已使用\n[BBOX-3521] 已使用\n[BBOX-3522] 已使用\n[BBOX-3523] 已使用\n[BBOX-3524] 已使用\n[BBOX-3525] 已使用\n[BBOX-3526] 已使用\n[BBOX-3527] 已使用\n[BBOX-3528] 已使用\n[BBOX-3529] 已使用\n[BBOX-3530] 已使用\n[BBOX-3531] 已使用\n[BBOX-3532] 已使用\n[BBOX-3533] 已使用\n[BBOX-3534] 已使用\n[BBOX-3535] 已使用\n[BBOX-3536] 已使用\n[BBOX-3537] 已使用\n[BBOX-3538] 已使用\n[BBOX-3539] 已使用\n[BBOX-3540] 已使用\n[BBOX-3541] 已使用\n[BBOX-3542] 已使用\n[BBOX-3543] 已使用\n[BBOX-3544] 已使用\n[BBOX-3545] 已使用\n[BBOX-3546] 已使用\n[BBOX-3547] 已使用\n[BBOX-3548] 已使用\n[BBOX-3549] 已使用\n[BBOX-3550] 已使用\n[BBOX-3551] 已使用\n[BBOX-3552] 已使用\n[BBOX-3553] 已使用\n[BBOX-3554] 已使用\n[BBOX-3555] 已使用\n[BBOX-3556] 已使用\n[BBOX-3557] 已使用\n[BBOX-3558] 已使用\n[BBOX-3559] 已使用\n[BBOX-3560] 已使用\n[BBOX-3561] 已使用\n[BBOX-3562] 已使用\n[BBOX-3563] 已使用\n[BBOX-3564] 已使用\n[BBOX-3565] 已使用\n[BBOX-3566] 已使用\n[BBOX-3567] 已使用\n[BBOX-3568] 已使用\n[BBOX-3569] 已使用\n[BBOX-3570] 已使用\n[BBOX-3571] 已使用\n[BBOX-3572] 已使用\n[BBOX-3573] 已使用\n[BBOX-3574] 已使用\n[BBOX-3575] 已使用\n[BBOX-3576] 已使用\n[BBOX-3577] 已使用\n[BBOX-3578] 已使用\n[BBOX-3579] 已使用\n[BBOX-3580] 已使用\n[BBOX-3581] 已使用\n[BBOX-3582] 已使用\n[BBOX-3583] 已使用\n[BBOX-3584] 已使用\n[BBOX-3585] 已使用\n[BBOX-3586] 已使用\n[BBOX-3587] 已使用\n[BBOX-3588] 已使用\n[BBOX-3589] 已使用\n[BBOX-3590] 已使用\n[BBOX-3591] 已使用\n[BBOX-3592] 已使用\n[BBOX-3593] 已使用\n[BBOX-3594] 已使用\n[BBOX-3595] 已使用\n[BBOX-3596] 已使用\n[BBOX-3597] 已使用\n[BBOX-3598] 已使用\n[BBOX-3599] 已使用\n[BBOX-3600] 已使用\n[BBOX-3601] 已使用\n[BBOX-3602] 已使用\n[BBOX-3603] 已使用\n[BBOX-3604] 已使用\n[BBOX-3605] 已使用\n[BBOX-3606] 已使用\n[BBOX-3607] 已使用\n[BBOX-3608] 已使用\n[BBOX-3609] 已使用\n[BBOX-3610] 已使用\n[BBOX-3611] 已使用\n[BBOX-3612] 已使用\n[BBOX-3613] 已使用\n[BBOX-3614] 已使用\n[BBOX-3615] 已使用\n[BBOX-3616] 已使用\n[BBOX-3617] 已使用\n[BBOX-3618] 已使用\n[BBOX-3619] 已使用\n[BBOX-3620] 已使用\n[BBOX-3621] 已使用\n[BBOX-3622] 已使用\n[BBOX-3623] 已使用\n[BBOX-3624] 已使用\n[BBOX-3625] 已使用\n[BBOX-3626] 已使用\n[BBOX-3627] 已使用\n[BBOX-3628] 已使用\n[BBOX-3629] 已使用\n[BBOX-3630] 已使用\n[BBOX-3631] 已使用\n[BBOX-3632] 已使用\n[BBOX-3633] 已使用\n[BBOX-3634] 已使用\n[BBOX-3635] 已使用\n[BBOX-3636] 已使用\n[BBOX-3637] 已使用\n[BBOX-3638] 已使用\n[BBOX-3639] 已使用\n[BBOX-3640] 已使用\n[BBOX-3641] 已使用\n[BBOX-3642] 已使用\n[BBOX-3643] 已使用\n[BBOX-3644] 已使用\n[BBOX-3645] 已使用\n[BBOX-3646] 已使用\n[BBOX-3647] 已使用\n[BBOX-3648] 已使用\n[BBOX-3649] 已使用\n[BBOX-3650] 已使用\n[BBOX-3651] 已使用\n[BBOX-3652] 已使用\n[BBOX-3653] 已使用\n[BBOX-3654] 已使用\n[BBOX-3655] 已使用\n[BBOX-3656] 已使用\n[BBOX-3657] 已使用\n[BBOX-3658] 已使用\n[BBOX-3659] 已使用\n[BBOX-3660] 已使用\n[BBOX-3661] 已使用\n[BBOX-3662] 已使用\n[BBOX-3663] 已使用\n[BBOX-3664] 已使用\n[BBOX-3665] 已使用\n[BBOX-3666] 已使用\n[BBOX-3667] 已使用\n[BBOX-3668] 已使用\n[BBOX-3669] 已使用\n[BBOX-3670] 已使用\n[BBOX-3671] 已使用\n[BBOX-3672] 已使用\n[BBOX-3673] 已使用\n[BBOX-3674] 已使用\n[BBOX-3675] 已使用\n[BBOX-3676] 已使用\n[BBOX-3677] 已使用\n[BBOX-3678] 已使用\n[BBOX-3679] 已使用\n[BBOX-3680] 已使用\n[BBOX-3681] 已使用\n[BBOX-3682] 已使用\n[BBOX-3683] 已使用\n[BBOX-3684] 已使用\n[BBOX-3685] 已使用\n[BBOX-3686] 已使用\n[BBOX-3687] 已使用\n[BBOX-3688] 已使用\n[BBOX-3689] 已使用\n[BBOX-3690] 已使用\n[BBOX-3691] 已使用\n[BBOX-3692] 已使用\n[BBOX-3693] 已使用\n[BBOX-3694] 已使用\n[BBOX-3695] 已使用\n[BBOX-3696] 已使用\n[BBOX-3697] 已使用\n[BBOX-3698] 已使用\n[BBOX-3699] 已使用\n[BBOX-3700] 已使用\n[BBOX-3701] 已使用\n[BBOX-3702] 已使用\n[BBOX-3703] 已使用\n[BBOX-3704] 已使用\n[BBOX-3705] 已使用\n[BBOX-3706] 已使用\n[BBOX-3707] 已使用\n[BBOX-3708] 已使用\n[BBOX-3709] 已使用\n[BBOX-3710] 已使用\n[BBOX-3711] 已使用\n[BBOX-3712] 已使用\n[BBOX-3713] 已使用\n[BBOX-3714] 已使用\n[BBOX-3715] 已使用\n[BBOX-3716] 已使用\n[BBOX-3717] 已使用\n[BBOX-3718] 已使用\n[BBOX-3719] 已使用\n[BBOX-3720] 已使用\n[BBOX-3721] 已使用\n[BBOX-3722] 已使用\n[BBOX-3723] 已使用\n[BBOX-3724] 已使用\n[BBOX-3725] 已使用\n[BBOX-3726] 已使用\n[BBOX-3727] 已使用\n[BBOX-3728] 已使用\n[BBOX-3729] 已使用\n[BBOX-3730] 已使用\n[BBOX-3731] 已使用\n[BBOX-3732] 已使用\n[BBOX-3733] 已使用\n[BBOX-3734] 已使用\n[BBOX-3735] 已使用\n[BBOX-3736] 已使用\n[BBOX-3737] 已使用\n[BBOX-3738] 已使用\n[BBOX-3739] 已使用\n[BBOX-3740] 已使用\n[BBOX-3741] 已使用\n[BBOX-3742] 已使用\n[BBOX-3743] 已使用\n[BBOX-3744] 已使用\n[BBOX-3745] 已使用\n[BBOX-3746] 已使用\n[BBOX-3747] 已使用\n[BBOX-3748] 已使用\n[BBOX-3749] 已使用\n[BBOX-3750] 已使用\n[BBOX-3751] 已使用\n[BBOX-3752] 已使用\n[BBOX-3753] 已使用\n[BBOX-3754] 已使用\n[BBOX-3755] 已使用\n[BBOX-3756] 已使用\n[BBOX-3757] 已使用\n[BBOX-3758] 已使用\n[BBOX-3759] 已使用\n[BBOX-3760] 已使用\n[BBOX-3761] 已使用\n[BBOX-3762] 已使用\n[BBOX-3763] 已使用\n[BBOX-3764] 已使用\n[BBOX-3765] 已使用\n[BBOX-3766] 已使用\n[BBOX-3767] 已使用\n[BBOX-3768] 已使用\n[BBOX-3769] 已使用\n[BBOX-3770] 已使用\n[BBOX-3771] 已使用\n[BBOX-3772] 已使用\n[BBOX-3773] 已使用\n[BBOX-3774] 已使用\n[BBOX-3775] 已使用\n[BBOX-3776] 已使用\n[BBOX-3777] 已使用\n[BBOX-3778] 已使用\n[BBOX-3779] 已使用\n[BBOX-3780] 已使用\n[BBOX-3781] 已使用\n[BBOX-3782] 已使用\n[BBOX-3783] 已使用\n[BBOX-3784] 已使用\n[BBOX-3785] 已使用\n[BBOX-3786] 已使用\n[BBOX-3787] 已使用\n[BBOX-3788] 已使用\n[BBOX-3789] 已使用\n[BBOX-3790] 已使用\n[BBOX-3791] 已使用\n[BBOX-3792] 已使用\n[BBOX-3793] 已使用\n[BBOX-3794] 已使用\n[BBOX-3795] 已使用\n[BBOX-3796] 已使用\n[BBOX-3797] 已使用\n[BBOX-3798] 已使用\n[BBOX-3799] 已使用\n[BBOX-3800] 已使用\n[BBOX-3801] 已使用\n[BBOX-3802] 已使用\n[BBOX-3803] 已使用\n[BBOX-3804] 已使用\n[BBOX-3805] 已使用\n[BBOX-3806] 已使用\n[BBOX-3807] 已使用\n[BBOX-3808] 已使用\n[BBOX-3809] 已使用\n[BBOX-3810] 已使用\n[BBOX-3811] 已使用\n[BBOX-3812] 已使用\n[BBOX-3813] 已使用\n[BBOX-3814] 已使用\n[BBOX-3815] 已使用\n[BBOX-3816] 已使用\n[BBOX-3817] 已使用\n[BBOX-3818] 已使用\n[BBOX-3819] 已使用\n[BBOX-3820] 已使用\n[BBOX-3821] 已使用\n[BBOX-3822] 已使用\n[BBOX-3823] 已使用\n[BBOX-3824] 已使用\n[BBOX-3825] 已使用\n[BBOX-3826] 已使用\n[BBOX-3827] 已使用\n[BBOX-3828] 已使用\n[BBOX-3829] 已使用\n[BBOX-3830] 已使用\n[BBOX-3831] 已使用\n[BBOX-3832] 已使用\n[BBOX-3833] 已使用\n[BBOX-3834] 已使用\n[BBOX-3835] 已使用\n[BBOX-3836] 已使用\n[BBOX-3837] 已使用\n[BBOX-3838] 已使用\n[BBOX-3839] 已使用\n[BBOX-3840] 已使用\n[BBOX-3841] 已使用\n[BBOX-3842] 已使用\n[BBOX-3843] 已使用\n[BBOX-3844] 已使用\n[BBOX-3845] 已使用\n[BBOX-3846] 已使用\n[BBOX-3847] 已使用\n[BBOX-3848] 已使用\n[BBOX-3849] 已使用\n[BBOX-3850] 已使用\n[BBOX-3851] 已使用\n[BBOX-3852] 已使用\n[BBOX-3853] 已使用\n[BBOX-3854] 已使用\n[BBOX-3855] 已使用\n[BBOX-3856] 已使用\n[BBOX-3857] 已使用\n[BBOX-3858] 已使用\n[BBOX-3859] 已使用\n[BBOX-3860] 已使用\n[BBOX-3861] 已使用\n[BBOX-3862] 已使用\n[BBOX-3863] 已使用\n[BBOX-3864] 已使用\n[BBOX-3865] 已使用\n[BBOX-3866] 已使用\n[BBOX-3867] 已使用\n[BBOX-3868] 已使用\n[BBOX-3869] 已使用\n[BBOX-3870] 已使用\n[BBOX-3871] 已使用\n[BBOX-3872] 已使用\n[BBOX-3873] 已使用\n[BBOX-3874] 已使用\n[BBOX-3875] 已使用\n[BBOX-3876] 已使用\n[BBOX-3877] 已使用\n[BBOX-3878] 已使用\n[BBOX-3879] 已使用\n[BBOX-3880] 已使用\n[BBOX-3881] 已使用\n[BBOX-3882] 已使用\n[BBOX-3883] 已使用\n[BBOX-3884] 已使用\n[BBOX-3885] 已使用\n[BBOX-3886] 已使用\n[BBOX-3887] 已使用\n[BBOX-3888] 已使用\n[BBOX-3889] 已使用\n[BBOX-3890] 已使用\n[BBOX-3891] 已使用\n[BBOX-3892] 已使用\n[BBOX-3893] 已使用\n[BBOX-3894] 已使用\n[BBOX-3895] 已使用\n[BBOX-3896] 已使用\n[BBOX-3897] 已使用\n[BBOX-3898] 已使用\n[BBOX-3899] 已使用\n[BBOX-3900] 已使用\n[BBOX-3901] 已使用\n[BBOX-3902] 已使用\n[BBOX-3903] 已使用\n[BBOX-3904] 已使用\n[BBOX-3905] 已使用\n[BBOX-3906] 已使用\n[BBOX-3907] 已使用\n[BBOX-3908] 已使用\n[BBOX-3909] 已使用\n[BBOX-3910] 已使用\n[BBOX-3911] 已使用\n[BBOX-3912] 已使用\n[BBOX-3913] 已使用\n[BBOX-3914] 已使用\n[BBOX-3915] 已使用\n[BBOX-3916] 已使用\n[BBOX-3917] 已使用\n[BBOX-3918] 已使用\n[BBOX-3919] 已使用\n[BBOX-3920] 已使用\n[BBOX-3921] 已使用\n[BBOX-3922] 已使用\n[BBOX-3923] 已使用\n[BBOX-3924] 已使用\n[BBOX-3925] 已使用\n[BBOX-3926] 已使用\n[BBOX-3927] 已使用\n[BBOX-3928] 已使用\n[BBOX-3929] 已使用\n[BBOX-3930] 已使用\n[BBOX-3931] 已使用\n[BBOX-3932] 已使用\n[BBOX-3933] 已使用\n[BBOX-3934] 已使用\n[BBOX-3935] 已使用\n[BBOX-3936] 已使用\n[BBOX-3937] 已使用\n[BBOX-3938] 已使用\n[BBOX-3939] 已使用\n[BBOX-3940] 已使用\n[BBOX-3941] 已使用\n[BBOX-3942] 已使用\n[BBOX-3943] 已使用\n[BBOX-3944] 已使用\n[BBOX-3945] 已使用\n[BBOX-3946] 已使用\n[BBOX-3947] 已使用\n[BBOX-3948] 已使用\n[BBOX-3949] 已使用\n[BBOX-3950] 已使用\n[BBOX-3951] 已使用\n[BBOX-3952] 已使用\n[BBOX-3953] 已使用\n[BBOX-3954] 已使用\n[BBOX-3955] 已使用\n[BBOX-3956] 已使用\n[BBOX-3957] 已使用\n[BBOX-3958] 已使用\n[BBOX-3959] 已使用\n[BBOX-3960] 已使用\n[BBOX-3961] 已使用\n[BBOX-3962] 已使用\n[BBOX-3963] 已使用\n[BBOX-3964] 已使用\n[BBOX-3965] 已使用\n[BBOX-3966] 已使用\n[BBOX-3967] 已使用\n[BBOX-3968] 已使用\n[BBOX-3969] 已使用\n[BBOX-3970] 已使用\n[BBOX-3971] 已使用\n[BBOX-3972] 已使用\n[BBOX-3973] 已使用\n[BBOX-3974] 已使用\n[BBOX-3975] 已使用\n[BBOX-3976] 已使用\n[BBOX-3977] 已使用\n[BBOX-3978] 已使用\n[BBOX-3979] 已使用\n[BBOX-3980] 已使用\n[BBOX-3981] 已使用\n[BBOX-3982] 已使用\n[BBOX-3983] 已使用\n[BBOX-3984] 已使用\n[BBOX-3985] 已使用\n[BBOX-3986] 已使用\n[BBOX-3987] 已使用\n[BBOX-3988] 已使用\n[BBOX-3989] 已使用\n[BBOX-3990] 已使用\n[BBOX-3991] 已使用\n[BBOX-3992] 已使用\n[BBOX-3993] 已使用\n[BBOX-3994] 已使用\n[BBOX-3995] 已使用\n[BBOX-3996] 已使用\n[BBOX-3997] 已使用\n[BBOX-3998] 已使用\n[BBOX-3999] 已使用\n[BBOX-4000] 已使用\n[BBOX-4001] 已使用\n[BBOX-4002] 已使用\n[BBOX-4003] 已使用\n[BBOX-4004] 已使用\n[BBOX-4005] 已使用\n[BBOX-4006] 已使用\n[BBOX-4007] 已使用\n[BBOX-4008] 已使用\n[BBOX-4009] 已使用\n[BBOX-4010] 已使用\n[BBOX-4011] 已使用\n[BBOX-4012] 已使用\n[BBOX-4013] 已使用\n[BBOX-4014] 已使用\n[BBOX-4015] 已使用\n[BBOX-4016] 已使用\n[BBOX-4017] 已使用\n[BBOX-4018] 已使用\n[BBOX-4019] 已使用\n[BBOX-4020] 已使用\n[BBOX-4021] 已使用\n[BBOX-4022] 已使用\n[BBOX-4023] 已使用\n[BBOX-4024] 已使用\n[BBOX-4025] 已使用\n[BBOX-4026] 已使用\n[BBOX-4027] 已使用\n[BBOX-4028] 已使用\n[BBOX-4029] 已使用\n[BBOX-4030] 已使用\n[BBOX-4031] 已使用\n[BBOX-4032] 已使用\n[BBOX-4033] 已使用\n[BBOX-4034] 已使用\n[BBOX-4035] 已使用\n[BBOX-4036] 已使用\n[BBOX-4037] 已使用\n[BBOX-4038] 已使用\n[BBOX-4039] 已使用\n[BBOX-4040] 已使用\n[BBOX-4041] 已使用\n[BBOX-4042] 已使用\n[BBOX-4043] 已使用\n[BBOX-4044] 已使用\n[BBOX-4045] 已使用\n[BBOX-4046] 已使用\n[BBOX-4047] 已使用\n[BBOX-4048] 已使用\n[BBOX-4049] 已使用\n[BBOX-4050] 已使用\n[BBOX-4051] 已使用\n[BBOX-4052] 已使用\n[BBOX-4053] 已使用\n[BBOX-4054] 已使用\n[BBOX-4055] 已使用\n[BBOX-4056] 已使用\n[BBOX-4057] 已使用\n[BBOX-4058] 已使用\n[BBOX-4059] 已使用\n[BBOX-4060] 已使用\n[BBOX-4061] 已使用\n[BBOX-4062] 已使用\n[BBOX-4063] 已使用\n[BBOX-4064] 已使用\n[BBOX-4065] 已使用\n[BBOX-4066] 已使用\n[BBOX-4067] 已使用\n[BBOX-4068] 已使用\n[BBOX-4069] 已使用\n[BBOX-4070] 已使用\n[BBOX-4071] 已使用\n[BBOX-4072] 已使用\n[BBOX-4073] 已使用\n[BBOX-4074] 已使用\n[BBOX-4075] 已使用\n[BBOX-4076] 已使用\n[BBOX-4077] 已使用\n[BBOX-4078] 已使用\n[BBOX-4079] 已使用\n[BBOX-4080] 已使用\n[BBOX-4081] 已使用\n[BBOX-4082] 已使用\n[BBOX-4083] 已使用\n[BBOX-4084] 已使用\n[BBOX-4085] 已使用\n[BBOX-4086] 已使用\n[BBOX-4087] 已使用\n[BBOX-4088] 已使用\n[BBOX-4089] 已使用\n[BBOX-4090] 已使用\n[BBOX-4091] 已使用\n[BBOX-4092] 已使用\n[BBOX-4093] 已使用\n[BBOX-4094] 已使用\n[BBOX-4095] 已使用\n[BBOX-4096] 已使用\n[BBOX-4097] 已使用\n[BBOX-4098] 已使用\n[BBOX-4099] 已使用\n[BBOX-4100] 已使用\n[BBOX-4101] 已使用\n[BBOX-4102] 已使用\n[BBOX-4103] 已使用\n[BBOX-4104] 已使用\n[BBOX-4105] 已使用\n[BBOX-4106] 已使用\n[BBOX-4107] 已使用\n[BBOX-4108] 已使用\n[BBOX-4109] 已使用\n[BBOX-4110] 已使用\n[BBOX-4111] 已使用\n[BBOX-4112] 已使用\n[BBOX-4113] 已使用\n[BBOX-4114] 已使用\n[BBOX-4115] 已使用\n[BBOX-4116] 已使用\n[BBOX-4117] 已使用\n[BBOX-4118] 已使用\n[BBOX-4119] 已使用\n[BBOX-4120] 已使用\n[BBOX-4121] 已使用\n[BBOX-4122] 已使用\n[BBOX-4123] 已使用\n[BBOX-4124] 已使用\n[BBOX-4125] 已使用\n[BBOX-4126] 已使用\n[BBOX-4127] 已使用\n[BBOX-4128] 已使用\n[BBOX-4129] 已使用\n[BBOX-4130] 已使用\n[BBOX-4131] 已使用\n[BBOX-4132] 已使用\n[BBOX-4133] 已使用\n[BBOX-4134] 已使用\n[BBOX-4135] 已使用\n[BBOX-4136] 已使用\n[BBOX-4137] 已使用\n[BBOX-4138] 已使用\n[BBOX-4139] 已使用\n[BBOX-4140] 已使用\n[BBOX-4141] 已使用\n[BBOX-4142] 已使用\n[BBOX-4143] 已使用\n[BBOX-4144] 已使用\n[BBOX-4145] 已使用\n[BBOX-4146] 已使用\n[BBOX-4147] 已使用\n[BBOX-4148] 已使用\n[BBOX-4149] 已使用\n[BBOX-4150] 已使用\n[BBOX-4151] 已使用\n[BBOX-4152] 已使用\n[BBOX-4153] 已使用\n[BBOX-4154] 已使用\n[BBOX-4155] 已使用\n[BBOX-4156] 已使用\n[BBOX-4157] 已使用\n[BBOX-4158] 已使用\n[BBOX-4159] 已使用\n[BBOX-4160] 已使用\n[BBOX-4161] 已使用\n[BBOX-4162] 已使用\n[BBOX-4163] 已使用\n[BBOX-4164] 已使用\n[BBOX-4165] 已使用\n[BBOX-4166] 已使用\n[BBOX-4167] 已使用\n[BBOX-4168] 已使用\n[BBOX-4169] 已使用\n[BBOX-4170] 已使用\n[BBOX-4171] 已使用\n[BBOX-4172] 已使用\n[BBOX-4173] 已使用\n[BBOX-4174] 已使用\n[BBOX-4175] 已使用\n[BBOX-4176] 已使用\n[BBOX-4177] 已使用\n[BBOX-4178] 已使用\n[BBOX-4179] 已使用\n[BBOX-4180] 已使用\n[BBOX-4181] 已使用\n[BBOX-4182] 已使用\n[BBOX-4183] 已使用\n[BBOX-4184] 已使用\n[BBOX-4185] 已使用\n[BBOX-4186] 已使用\n[BBOX-4187] 已使用\n[BBOX-4188] 已使用\n[BBOX-4189] 已使用\n[BBOX-4190] 已使用\n[BBOX-4191] 已使用\n[BBOX-4192] 已使用\n[BBOX-4193] 已使用\n[BBOX-4194] 已使用\n[BBOX-4195] 已使用\n[BBOX-4196] 已使用\n[BBOX-4197] 已使用\n[BBOX-4198] 已使用\n[BBOX-4199] 已使用\n[BBOX-4200] 已使用\n[BBOX-4201] 已使用\n[BBOX-4202] 已使用\n[BBOX-4203] 已使用\n[BBOX-4204] 已使用\n[BBOX-4205] 已使用\n[BBOX-4206] 已使用\n[BBOX-4207] 已使用\n[BBOX-4208] 已使用\n[BBOX-4209] 已使用\n[BBOX-4210] 已使用\n[BBOX-4211] 已使用\n[BBOX-4212] 已使用\n[BBOX-4213] 已使用\n[BBOX-4214] 已使用\n[BBOX-4215] 已使用\n[BBOX-4216] 已使用\n[BBOX-4217] 已使用\n[BBOX-4218] 已使用\n[BBOX-4219] 已使用\n[BBOX-4220] 已使用\n[BBOX-4221] 已使用\n[BBOX-4222] 已使用\n[BBOX-4223] 已使用\n[BBOX-4224] 已使用\n[BBOX-4225] 已使用\n[BBOX-4226] 已使用\n[BBOX-4227] 已使用\n[BBOX-4228] 已使用\n[BBOX-4229] 已使用\n[BBOX-4230] 已使用\n[BBOX-4231] 已使用\n[BBOX-4232] 已使用\n[BBOX-4233] 已使用\n[BBOX-4234] 已使用\n[BBOX-4235] 已使用\n[BBOX-4236] 已使用\n[BBOX-4237] 已使用\n[BBOX-4238] 已使用\n[BBOX-4239] 已使用\n[BBOX-4240] 已使用\n[BBOX-4241] 已使用\n[BBOX-4242] 已使用\n[BBOX-4243] 已使用\n[BBOX-4244] 已使用\n[BBOX-4245] 已使用\n[BBOX-4246] 已使用\n[BBOX-4247] 已使用\n[BBOX-4248] 已使用\n[BBOX-4249] 已使用\n[BBOX-4250] 已使用\n[BBOX-4251] 已使用\n[BBOX-4252] 已使用\n[BBOX-4253] 已使用\n[BBOX-4254] 已使用\n[BBOX-4255] 已使用\n[BBOX-4256] 已使用\n[BBOX-4257] 已使用\n[BBOX-4258] 已使用\n[BBOX-4259] 已使用\n[BBOX-4260] 已使用\n[BBOX-4261] 已使用\n[BBOX-4262] 已使用\n[BBOX-4263] 已使用\n[BBOX-4264] 已使用\n[BBOX-4265] 已使用\n[BBOX-4266] 已使用\n[BBOX-4267] 已使用\n[BBOX-4268] 已使用\n[BBOX-4269] 已使用\n[BBOX-4270] 已使用\n[BBOX-4271] 已使用\n[BBOX-4272] 已使用\n[BBOX-4273] 已使用\n[BBOX-4274] 已使用\n[BBOX-4275] 已使用\n[BBOX-4276] 已使用\n[BBOX-4277] 已使用\n[BBOX-4278] 已使用\n[BBOX-4279] 已使用\n[BBOX-4280] 已使用\n[BBOX-4281] 已使用\n[BBOX-4282] 已使用\n[BBOX-4283] 已使用\n[BBOX-4284] 已使用\n[BBOX-4285] 已使用\n[BBOX-4286] 已使用\n[BBOX-4287] 已使用\n[BBOX-4288] 已使用\n[BBOX-4289] 已使用\n[BBOX-4290] 已使用\n[BBOX-4291] 已使用\n[BBOX-4292] 已使用\n[BBOX-4293] 已使用\n[BBOX-4294] 已使用\n[BBOX-4295] 已使用\n[BBOX-4296] 已使用\n[BBOX-4297] 已使用\n[BBOX-4298] 已使用\n[BBOX-4299] 已使用\n[BBOX-4300] 已使用\n[BBOX-4301] 已使用\n[BBOX-4302] 已使用\n[BBOX-4303] 已使用\n[BBOX-4304] 已使用\n[BBOX-4305] 已使用\n[BBOX-4306] 已使用\n[BBOX-4307] 已使用\n[BBOX-4308] 已使用\n[BBOX-4309] 已使用\n[BBOX-4310] 已使用\n[BBOX-4311] 已使用\n[BBOX-4312] 已使用\n[BBOX-4313] 已使用\n[BBOX-4314] 已使用\n[BBOX-4315] 已使用\n[BBOX-4316] 已使用\n[BBOX-4317] 已使用\n[BBOX-4318] 已使用\n[BBOX-4319] 已使用\n[BBOX-4320] 已使用\n[BBOX-4321] 已使用\n[BBOX-4322] 已使用\n[BBOX-4323] 已使用\n[BBOX-4324] 已使用\n[BBOX-4325] 已使用\n[BBOX-4326] 已使用\n[BBOX-4327] 已使用\n[BBOX-4328] 已使用\n[BBOX-4329] 已使用\n[BBOX-4330] 已使用\n[BBOX-4331] 已使用\n[BBOX-4332] 已使用\n[BBOX-4333] 已使用\n[BBOX-4334] 已使用\n[BBOX-4335] 已使用\n[BBOX-4336] 已使用\n[BBOX-4337] 已使用\n[BBOX-4338] 已使用\n[BBOX-4339] 已使用\n[BBOX-4340] 已使用\n[BBOX-4341] 已使用\n[BBOX-4342] 已使用\n[BBOX-4343] 已使用\n[BBOX-4344] 已使用\n[BBOX-4345] 已使用\n[BBOX-4346] 已使用\n[BBOX-4347] 已使用\n[BBOX-4348] 已使用\n[BBOX-4349] 已使用\n[BBOX-4350] 已使用\n[BBOX-4351] 已使用\n[BBOX-4352] 已使用\n[BBOX-4353] 已使用\n[BBOX-4354] 已使用\n[BBOX-4355] 已使用\n[BBOX-4356] 已使用\n[BBOX-4357] 已使用\n[BBOX-4358] 已使用\n[BBOX-4359] 已使用\n[BBOX-4360] 已使用\n[BBOX-4361] 已使用\n[BBOX-4362] 已使用\n[BBOX-4363] 已使用\n[BBOX-4364] 已使用\n[BBOX-4365] 已使用\n[BBOX-4366] 已使用\n[BBOX-4367] 已使用\n[BBOX-4368] 已使用\n[BBOX-4369] 已使用\n[BBOX-4370] 已使用\n[BBOX-4371] 已使用\n[BBOX-4372] 已使用\n[BBOX-4373] 已使用\n[BBOX-4374] 已使用\n[BBOX-4375] 已使用\n[BBOX-4376] 已使用\n[BBOX-4377] 已使用\n[BBOX-4378] 已使用\n[BBOX-4379] 已使用\n[BBOX-4380] 已使用\n[BBOX-4381] 已使用\n[BBOX-4382] 已使用\n[BBOX-4383] 已使用\n[BBOX-4384] 已使用\n[BBOX-4385] 已使用\n[BBOX-4386] 已使用\n[BBOX-4387] 已使用\n[BBOX-4388] 已使用\n[BBOX-4389] 已使用\n[BBOX-4390] 已使用\n[BBOX-4391] 已使用\n[BBOX-4392] 已使用\n[BBOX-4393] 已使用\n[BBOX-4394] 已使用\n[BBOX-4395] 已使用\n[BBOX-4396] 已使用\n[BBOX-4397] 已使用\n[BBOX-4398] 已使用\n[BBOX-4399] 已使用\n[BBOX-4400] 已使用\n[BBOX-4401] 已使用\n[BBOX-4402] 已使用\n[BBOX-4403] 已使用\n[BBOX-4404] 已使用\n[BBOX-4405] 已使用\n[BBOX-4406] 已使用\n[BBOX-4407] 已使用\n[BBOX-4408] 已使用\n[BBOX-4409] 已使用\n[BBOX-4410] 已使用\n[BBOX-4411] 已使用\n[BBOX-4412] 已使用\n[BBOX-4413] 已使用\n[BBOX-4414] 已使用\n[BBOX-4415] 已使用\n[BBOX-4416] 已使用\n[BBOX-4417] 已使用\n[BBOX-4418] 已使用\n[BBOX-4419] 已使用\n[BBOX-4420] 已使用\n[BBOX-4421] 已使用\n[BBOX-4422] 已使用\n[BBOX-4423] 已使用\n[BBOX-4424] 已使用\n[BBOX-4425] 已使用\n[BBOX-4426] 已使用\n[BBOX-4427] 已使用\n[BBOX-4428] 已使用\n[BBOX-4429] 已使用\n[BBOX-4430] 已使用\n[BBOX-4431] 已使用\n[BBOX-4432] 已使用\n[BBOX-4433] 已使用\n[BBOX-4434] 已使用\n[BBOX-4435] 已使用\n[BBOX-4436] 已使用\n[BBOX-4437] 已使用\n[BBOX-4438] 已使用\n[BBOX-4439] 已使用\n[BBOX-4440] 已使用\n[BBOX-4441] 已使用\n[BBOX-4442] 已使用\n[BBOX-4443] 已使用\n[BBOX-4444] 已使用\n[BBOX-4445] 已使用\n[BBOX-4446] 已使用\n[BBOX-4447] 已使用\n[BBOX-4448] 已使用\n[BBOX-4449] 已使用\n[BBOX-4450] 已使用\n[BBOX-4451] 已使用\n[BBOX-4452] 已使用\n[BBOX-4453] 已使用\n[BBOX-4454] 已使用\n[BBOX-4455] 已使用\n[BBOX-4456] 已使用\n[BBOX-4457] 已使用\n[BBOX-4458] 已使用\n[BBOX-4459] 已使用\n[BBOX-4460] 已使用\n[BBOX-4461] 已使用\n[BBOX-4462] 已使用\n[BBOX-4463] 已使用\n[BBOX-4464] 已使用\n[BBOX-4465] 已使用\n[BBOX-4466] 已使用\n[BBOX-4467] 已使用\n[BBOX-4468] 已使用\n[BBOX-4469] 已使用\n[BBOX-4470] 已使用\n[BBOX-4471] 已使用\n[BBOX-4472] 已使用\n[BBOX-4473] 已使用\n[BBOX-4474] 已使用\n[BBOX-4475] 已使用\n[BBOX-4476] 已使用\n[BBOX-4477] 已使用\n[BBOX-4478] 已使用\n[BBOX-4479] 已使用\n[BBOX-4480] 已使用\n[BBOX-4481] 已使用\n[BBOX-4482] 已使用\n[BBOX-4483] 已使用\n[BBOX-4484] 已使用\n[BBOX-4485] 已使用\n[BBOX-4486] 已使用\n[BBOX-4487] 已使用\n[BBOX-4488] 已使用\n[BBOX-4489] 已使用\n[BBOX-4490] 已使用\n[BBOX-4491] 已使用\n[BBOX-4492] 已使用\n[BBOX-4493] 已使用\n[BBOX-4494] 已使用\n[BBOX-4495] 已使用\n[BBOX-4496] 已使用\n[BBOX-4497] 已使用\n[BBOX-4498] 已使用\n[BBOX-4499] 已使用\n[BBOX-4500] 已使用\n[BBOX-4501] 已使用\n[BBOX-4502] 已使用\n[BBOX-4503] 已使用\n[BBOX-4504] 已使用\n[BBOX-4505] 已使用\n[BBOX-4506] 已使用\n[BBOX-4507] 已使用\n[BBOX-4508] 已使用\n[BBOX-4509] 已使用\n[BBOX-4510] 已使用\n[BBOX-4511] 已使用\n[BBOX-4512] 已使用\n[BBOX-4513] 已使用\n[BBOX-4514] 已使用\n[BBOX-4515] 已使用\n[BBOX-4516] 已使用\n[BBOX-4517] 已使用\n[BBOX-4518] 已使用\n[BBOX-4519] 已使用\n[BBOX-4520] 已使用\n[BBOX-4521] 已"
  }
]
2026-08-05 04:58:19,151 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:58:19.150+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:58:45,092 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:58:45,107 INFO     29 [SmartSplitter] SmartSplitter done: 4 chunks from 4 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1}
2026-08-05 04:58:45,115 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 04:58:45,115 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks": "4 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1}"}
2026-08-05 04:58:45,115 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 04:58:45,116 INFO     29 [ChunkRouter] Routed 4 chunks into 4 groups: {'chunks_Admission': 1, 'chunks_Discharge': 1, 'chunks_Examination': 1, 'chunks_Prescription': 1}
2026-08-05 04:58:45,122 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 04:58:45,122 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | ChunkRouter:Router | outputs={"html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks": "4 items, types={'AdmissionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 04:58:45,122 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 04:58:45,126 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:58:45,126 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:58:45 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:45,127 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:45,820 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:58:45,829 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 04:58:45,830 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 04:58:45,830 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 04:58:45,835 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:58:45,835 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:58:45 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:45,836 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:46,419 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:58:46,424 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 04:58:46,425 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 04:58:46,425 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 04:58:46,430 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:58:46,430 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:58:46 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:46,431 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:47,438 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:58:47,448 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 04:58:47,449 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 04:58:47,449 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 04:58:47,456 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:58:47,456 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:58:47 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:47,457 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:47,952 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:58:47,963 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 04:58:47,964 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 04:58:47,964 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 04:58:47,971 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:58:47,971 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:58:47,971 INFO     29 [qwen-vl-text] positions(32): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:58:47,971 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [32]
2026-08-05 04:58:48,209 INFO     29 [qwen-vl-text] page=9, rect=612x733, img=(1700x2036), dpi=200
2026-08-05 04:58:48,211 INFO     29 [qwen-vl-text] LLM extraction start, text_len=204
2026-08-05 04:58:48,211 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:58:48,212 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 442, \"bbox_end\": 473, \"encounter_dates\": [\"2025-12-05\"], \"department\": \"内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "亦康互联网医院\n普通\n处方\n已使用\n已使用\n已使用\n联\n处方笺\n已使用\nNO.:\n2025-12-05\n已使用\n姓名：\n性别：女处方专用章\n年龄：72岁\n已使用\n费别：自费\n科别：内科\n已使用\n临床诊断：支气管哮喘\n已使用\nRp：\n已使用\n沙美特罗替卡松吸入粉雾剂\n已使用\n50μg:250μg*60泡\nx 3盒\n已使用\n用法用量：\n口腔吸入,一日两次,一次1.0揿;\n已使用\n补充说明：处方超7日为病情需要",
    "role": "user"
  }
]
[92m04:58:48 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:48,213 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:58:50,472 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:58:50,473 INFO     29 [qwen-vl-text] LLM output (len=437):
{
  "encounter_date": "2025-12-05",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "50μg:250μg",
      "frequency": "一日两次",
      "route": "口腔吸入",
      "duration_days": null,
      "quantity": "3盒",
      "notes": "一次1.0揿; 处方超7日为病情需要"
    }
  ]
}
2026-08-05 04:58:50,473 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-05]
2026-08-05 04:58:50,477 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=882388, prompt_len=913
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["亦康互联网医院", "普通", "处方", "已使用", "已使用", "已使用", "联", "处方笺", "已使用", "NO.:", "2025-12-05", "已使用", "姓名：", "性别：女处方专用章", "年龄：72岁", "已使用", "费别：自费", "科别：内科", "已使用", "临床诊断：支气管哮喘", "已使用", "Rp：", "已使用", "沙美特罗替卡松吸入粉雾剂", "已使用", "50μg:250μg*60泡", "x 3盒", "已使用", "用法用量：", "口腔吸入,一日两次,一次1.0揿;", "已使用", "补充说明：处方超7日为病情需要"]

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
2026-08-05 04:59:13,915 INFO     29 [qwen-vl-text] coord API raw response (len=4148):
[
	{"text": "亦康互联网医院", "bbox": [428, 29, 716, 66]},
	{"text": "普通", "bbox": [896, 33, 936, 50], "bbox": [896, 33, 936, 50]},
	{"text": "处方", "bbox": [896, 53, 936, 70], "bbox": [896, 53, 936, 70]},
	{"text": "已使用", "bbox": [20, 72, 90, 100], "bbox": [20, 72, 90, 100]},
	{"text": "已使用", "bbox": [182, 22, 248, 52], "bbox": [182, 22, 248, 52]},
	{"text": "已使用", "bbox": [361, 72, 427, 105], "bbox": [361, 72, 427, 105]},
	{"text": "联", "bbox": [550, 78, 575, 97], "bbox": [550, 78, 575, 97]},
	{"text": "处方笺", "bbox": [485, 95, 611, 130], "bbox": [485, 95, 611, 130]},
	{"text": "已使用", "bbox": [725, 95, 791, 127], "bbox": [725, 95, 791, 127]},
	{"text": "NO.:", "bbox": [100, 140, 170, 161], "bbox": [100, 140, 170, 161]},
	{"text": "2025-12-05", "bbox": [755, 136, 904, 157], "bbox": [755, 136, 904, 157]},
	{"text": "已使用", "bbox": [14, 189, 83, 220], "bbox": [14, 189, 83, 220]},
	{"text": "姓名：", "bbox": [98, 202, 200, 225], "bbox": [98, 202, 200, 225]},
	{"text": "性别：女处方专用章", "bbox": [411, 200, 622, 225], "bbox": [411, 200, 622, 225]},
	{"text": "年龄：72岁", "bbox": [695, 195, 836, 220], "bbox": [695, 195, 836, 220]},
	{"text": "已使用", "bbox": [371, 218, 418, 245], "bbox": [371, 218, 418, 245]},
	{"text": "费别：自费", "bbox": [97, 259, 244, 283], "bbox": [97, 259, 244, 283]},
	{"text": "科别：内科", "bbox": [411, 260, 557, 285], "bbox": [411, 260, 557, 285]},
	{"text": "已使用", "bbox": [539, 270, 604, 302], "bbox": [539, 270, 604, 302]},
	{"text": "临床诊断：支气管哮喘", "bbox": [97, 319, 376, 344], "bbox": [97, 319, 376, 344]},
	{"text": "已使用", "bbox": [909, 267, 977, 300], "bbox": [909, 267, 977, 300]},
	{"text": "Rp：", "bbox": [85, 389, 145, 418], "bbox": [85, 389, 145, 418]},
	{"text": "已使用", "bbox": [193, 386, 262, 418], "bbox": [193, 386, 262, 418]},
	{"text": "已使用", "bbox": [538, 383, 604, 417], "bbox": [538, 383, 604, 417]},
	{"text": "已使用", "bbox": [739, 323, 805, 356], "bbox": [739, 323, 805, 356]},
	{"text": "沙美特罗替卡松吸入粉雾剂", "bbox": [105, 443, 434, 468], "bbox": [105, 443, 434, 468]},
	{"text": "已使用", "bbox": [738, 442, 805, 475], "bbox": [738, 442, 805, 475]},
	{"text": "50μg:250μg*60泡", "bbox": [107, 483, 332, 508], "bbox": [107, 483, 332, 508]},
	{"text": "x 3盒", "bbox": [570, 480, 636, 503], "bbox": [570, 480, 636, 503]},
	{"text": "已使用", "bbox": [908, 382, 976, 416], "bbox": [908, 382, 976, 416]},
	{"text": "用法用量：", "bbox": [107, 527, 233, 551], "bbox": [107, 527, 233, 551]},
	{"text": "口腔吸入,一日两次,一次1.0揿;", "bbox": [277, 525, 623, 550], "bbox": [277, 525, 623, 550]},
	{"text": "已使用", "bbox": [908, 511, 976, 545], "bbox": [908, 511, 976, 545]},
	{"text": "补充说明：处方超7日为病情需要", "bbox": [82, 608, 512, 635], "bbox": [82, 608, 512, 635]},
	{"text": "已使用", "bbox": [193, 631, 260, 664], "bbox": [193, 631, 260, 664]},
	{"text": "已使用", "bbox": [549, 628, 615, 661], "bbox": [549, 628, 615, 661]},
	{"text": "已使用", "bbox": [908, 637, 976, 671], "bbox": [908, 637, 976, 671]},
	{"text": "已使用", "bbox": [0, 678, 69, 709], "bbox": [0, 678, 69, 709]},
	{"text": "已使用", "bbox": [378, 685, 446, 718], "bbox": [378, 685, 446, 718]},
	{"text": "已使用", "bbox": [738, 684, 805, 717], "bbox": [738, 684, 805, 717]},
	{"text": "已使用", "bbox": [183, 740, 255, 773], "bbox": [183, 740, 255, 773]},
	{"text": "已使用", "bbox": [555, 738, 622, 771], "bbox": [555, 738, 622, 771]},
	{"text": "已使用", "bbox": [908, 738, 976, 772], "bbox": [908, 738, 976, 772]},
	{"text": "已使用", "bbox": [0, 800, 58, 831], "bbox": [0, 800, 58, 831]},
	{"text": "医师：邢伟", "bbox": [67, 804, 250, 847], "bbox": [67, 804, 250, 847]},
	{"text": "审核：张艳梅", "bbox": [296, 807, 507, 835], "bbox": [296, 807, 507, 835]},
	{"text": "处方金额：", "bbox": [522, 805, 648, 830], "bbox": [522, 805, 648, 830]},
	{"text": "已使用", "bbox": [738, 800, 805, 833], "bbox": [738, 800, 805, 833]},
	{"text": "药房审核：", "bbox": [64, 865, 196, 890], "bbox": [64, 865, 196, 890]},
	{"text": "药房调配：", "bbox": [294, 866, 420, 890], "bbox": [294, 866, 420, 890]},
	{"text": "药房核对：", "bbox": [522, 865, 648, 890], "bbox": [522, 865, 648, 890]},
	{"text": "药房发药：", "bbox": [760, 866, 886, 890], "bbox": [760, 866, 886, 890]},
	{"text": "注：处方自开具日起3日内有效。", "bbox": [63, 957, 370, 978], "bbox": [63, 957, 370, 978]}
]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord API: raw_items=53, valid_items=53, elapsed=23.4s
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[0]: text=亦康互联网医院, bbox=[428, 29, 716, 66]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[896, 33, 936, 50]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[2]: text=处方, bbox=[896, 53, 936, 70]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[3]: text=已使用, bbox=[20, 72, 90, 100]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[4]: text=已使用, bbox=[182, 22, 248, 52]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[5]: text=已使用, bbox=[361, 72, 427, 105]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[6]: text=联, bbox=[550, 78, 575, 97]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[7]: text=处方笺, bbox=[485, 95, 611, 130]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[8]: text=已使用, bbox=[725, 95, 791, 127]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[9]: text=NO.:, bbox=[100, 140, 170, 161]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[10]: text=2025-12-05, bbox=[755, 136, 904, 157]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[11]: text=已使用, bbox=[14, 189, 83, 220]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[12]: text=姓名：, bbox=[98, 202, 200, 225]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[13]: text=性别：女处方专用章, bbox=[411, 200, 622, 225]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[14]: text=年龄：72岁, bbox=[695, 195, 836, 220]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[15]: text=已使用, bbox=[371, 218, 418, 245]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[16]: text=费别：自费, bbox=[97, 259, 244, 283]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[17]: text=科别：内科, bbox=[411, 260, 557, 285]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[18]: text=已使用, bbox=[539, 270, 604, 302]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[19]: text=临床诊断：支气管哮喘, bbox=[97, 319, 376, 344]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[20]: text=已使用, bbox=[909, 267, 977, 300]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[21]: text=Rp：, bbox=[85, 389, 145, 418]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[22]: text=已使用, bbox=[193, 386, 262, 418]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[23]: text=已使用, bbox=[538, 383, 604, 417]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[24]: text=已使用, bbox=[739, 323, 805, 356]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[25]: text=沙美特罗替卡松吸入粉雾剂, bbox=[105, 443, 434, 468]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[26]: text=已使用, bbox=[738, 442, 805, 475]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[27]: text=50μg:250μg*60泡, bbox=[107, 483, 332, 508]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[28]: text=x 3盒, bbox=[570, 480, 636, 503]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[29]: text=已使用, bbox=[908, 382, 976, 416]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[30]: text=用法用量：, bbox=[107, 527, 233, 551]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[31]: text=口腔吸入,一日两次,一次1.0揿;, bbox=[277, 525, 623, 550]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[32]: text=已使用, bbox=[908, 511, 976, 545]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[33]: text=补充说明：处方超7日为病情需要, bbox=[82, 608, 512, 635]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[34]: text=已使用, bbox=[193, 631, 260, 664]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[35]: text=已使用, bbox=[549, 628, 615, 661]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[36]: text=已使用, bbox=[908, 637, 976, 671]
2026-08-05 04:59:13,916 INFO     29 [qwen-vl-text] coord item[37]: text=已使用, bbox=[0, 678, 69, 709]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[38]: text=已使用, bbox=[378, 685, 446, 718]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[39]: text=已使用, bbox=[738, 684, 805, 717]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[40]: text=已使用, bbox=[183, 740, 255, 773]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[41]: text=已使用, bbox=[555, 738, 622, 771]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[42]: text=已使用, bbox=[908, 738, 976, 772]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[43]: text=已使用, bbox=[0, 800, 58, 831]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[44]: text=医师：邢伟, bbox=[67, 804, 250, 847]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[45]: text=审核：张艳梅, bbox=[296, 807, 507, 835]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[46]: text=处方金额：, bbox=[522, 805, 648, 830]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[47]: text=已使用, bbox=[738, 800, 805, 833]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[48]: text=药房审核：, bbox=[64, 865, 196, 890]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[49]: text=药房调配：, bbox=[294, 866, 420, 890]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[50]: text=药房核对：, bbox=[522, 865, 648, 890]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[51]: text=药房发药：, bbox=[760, 866, 886, 890]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] coord item[52]: text=注：处方自开具日起3日内有效。, bbox=[63, 957, 370, 978]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] page=9 — 32/32 coords, api_time=23.4s
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] new_positions (32):
[[9, 261.936, 438.192, 21.254792785644533, 48.37297668457031], [9, 548.352, 572.832, 24.186488342285156, 36.64619445800781], [9, 548.352, 572.832, 38.844966125488284, 51.30467224121094], [9, 12.24, 55.08, 52.770520019531254, 73.29238891601562], [9, 111.384, 151.776, 16.124325561523438, 38.11204223632813], [9, 220.932, 261.324, 52.770520019531254, 76.9570083618164], [9, 336.59999999999997, 351.9, 57.16806335449219, 71.09361724853515], [9, 296.82, 373.932, 69.62776947021484, 95.28010559082031], [9, 443.7, 484.092, 69.62776947021484, 93.08133392333984], [9, 61.199999999999996, 104.03999999999999, 102.60934448242188, 118.00074615478516], [9, 462.06, 553.2479999999999, 99.67764892578126, 115.06905059814453], [9, 8.568, 50.796, 138.52261505126953, 161.24325561523438], [9, 59.976, 122.39999999999999, 148.05062561035157, 164.90787506103516], [9, 251.53199999999998, 380.664, 146.58477783203125, 164.90787506103516], [9, 425.34, 511.632, 142.92015838623047, 161.24325561523438], [9, 227.052, 255.816, 159.77740783691408, 179.56635284423828], [9, 59.364, 149.328, 189.82728729248046, 207.41746063232424], [9, 251.53199999999998, 340.884, 190.56021118164062, 208.88330841064453], [9, 329.868, 369.64799999999997, 197.8894500732422, 221.3430145263672], [9, 59.364, 230.112, 233.80272064208984, 252.12581787109374], [9, 556.308, 597.924, 195.69067840576173, 219.87716674804688], [9, 52.019999999999996, 88.74, 285.1073928833008, 306.3621856689453], [9, 118.116, 160.344, 282.90862121582035, 306.3621856689453], [9, 329.256, 369.64799999999997, 280.70984954833983, 305.62926177978517], [9, 452.268, 492.65999999999997, 236.7344161987305, 260.92090454101566], [9, 64.26, 265.608, 324.6852828979492, 343.0083801269531], [9, 451.656, 492.65999999999997, 323.9523590087891, 348.1388473510742], [9, 65.484, 203.184, 354.00223846435546, 372.32533569335936], [9, 348.84, 389.23199999999997, 351.803466796875, 368.6607162475586], [9, 555.696, 597.312, 279.9769256591797, 304.89633789062503], [9, 65.484, 142.596, 386.25088958740236, 403.8410629272461], [9, 169.524, 381.276, 384.78504180908203, 403.10813903808594]]
2026-08-05 04:59:13,917 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=25.9s
2026-08-05 04:59:13,924 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 04:59:13,925 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Extractor:Prescription | outputs={"chunks": "1 items, types={'PrescriptionRecord': 1}", "html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 04:59:13,925 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 04:59:13,926 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:59:13.925+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:59:13,932 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:59:13,932 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-05 04:59:13,932 INFO     29 [qwen-vl-text] positions(93): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:59:13,932 INFO     29 [qwen-vl-text] page grouping: [4, 5, 6], lines per page: [40, 30, 23]
2026-08-05 04:59:14,346 INFO     29 [qwen-vl-text] page=4, rect=612x630, img=(1700x1750), dpi=200
2026-08-05 04:59:14,874 INFO     29 [qwen-vl-text] page=5, rect=612x634, img=(1700x1762), dpi=200
2026-08-05 04:59:15,224 INFO     29 [qwen-vl-text] page=6, rect=612x624, img=(1700x1733), dpi=200
2026-08-05 04:59:15,227 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3225
2026-08-05 04:59:15,227 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:59:15,227 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 140, \"bbox_end\": 232, \"encounter_dates\": [\"2025-10-30\", \"2025-11-07\"], \"department\": \"呼吸与危重医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n姓名：\n床号：23-03床\n病历号：0\n科室：呼吸与危重医学科医生站\n姓名：\n性别：女\n年龄：72岁\n民族：汉族\n病历号：00\n科室：呼吸与危重医学科医生站\n入院日期：2025-10-30 14:34\n住院天数：8\n出院日期：2025-11-07 11:44\n籍贯：贵州省贵阳市\n职业：退休人员\n单位：贵阳供电局\n住址：中国贵州省贵阳\n入院情况：\n李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无\n明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯\n血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治\n疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1\n周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门\n诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体\n重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病\n史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无\n中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学\n历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗\n史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已\n故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患\n者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，\n血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。\n心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检\n查：暂无\n入院诊断：1.支气管哮喘急性发作期\n诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床\n检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1\n2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝\n功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中\n心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心):钾(K)4.47mmol/L白介素-6(IL-6)2.10pg/ml\n肌酐(Cr)57.90μmol/L C反应蛋白(CRP)0.48mg/L丙氨酸氨基转移酶(ALT)17.50U/L天冬氨酸氨基转移\n酶(AST)25.40U/L。2025-10-3017:34 DIC全套(临床检验中心):纤维蛋白原(Fg)5.09g/L D-二聚体(DD)\n0.75μg/mLDDU。2025-10-3015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3\n015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3113:11 胸部CT平扫:1、考虑双肺新增少许感染灶,以左肺为著,请结合临床并复查。2、双肺尖多发结节灶、纤维化灶,邻近双侧\n1/3\n贵州醫科大學附屬醫院\nTHE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n出院记录\n姓名:\n床号:23-03床\n病历号:\n科室:呼吸与危重医学科医生站\n胸膜局限性增厚,考虑陈旧性病变,建议随诊复查。3、左肺下叶外基底段局部间质性改变,其内支气管\n扩张;双肺支气管壁稍增厚,考虑慢性支气管炎,请结合临床并复查。4、左肺下叶微小结节,建议随诊\n复查。5、纵隔内淋巴结稍增大,建议随诊复查。6、主动脉及冠状动脉硬化;胸椎退变,左侧第2前肋走\n行欠佳。7、肝内囊性灶,建议超声随诊复查。2025-10-3114:35肺通气功能测定及支气管舒张试验:1.\n中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+)2025-10-3112:33。传染病筛查\n三项:阴性。2025-10-3113:12乙肝5项(定量):阴性。2025-10-3115:12大便常规(不含寄生虫)(临\n床检验中心):未见异常。2025-10-3115:10尿液检查(尿液分析+尿有形成分):未见异常。2025-10-31\n14:37痰液革兰氏染色+抗酸染色+真菌(临床检验中心):未见异常。2025-11-0210:41痰细菌培养及鉴\n定:未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染,痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支\n气管等对症支持治疗,先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症\n治疗,经我科治疗后,患者病情较前好转,目前一般情况可,请示上级医师盾予今日办理出院。\n出院诊断:1.支气管哮喘急性发作期;2.社区获得性肺炎,非重症;3.慢性阻塞性肺疾病;4.左肺下叶小\n结节;5.肝囊肿。\n出院情况:患者咳嗽、咳痰、胸闷、气促好转,无呼吸困难,无畏寒、发热,无恶心、呕吐等不适。查\n体:生命体征平稳。全身皮肤黏膜、巩膜无黄染,双肺呼吸音清,未闻及干湿性啰音。律齐,各瓣膜听诊\n区未闻及病理性杂音,腹软,全腹无压痛及反跳痛,肝脾肋下未及,肝脾肋下未及,双下肢无水肿。\nVTE评估:\n床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31\n14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴\n定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支\n气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症\n治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。\n出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小\n结节；5.肝囊肿。\n出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查\n体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊\n区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。\nVTE评估：\nPadua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：\n出院医嘱：\n1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治\n疗，定期复查肺功能，呼吸科门诊随诊；\n2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。\n3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。\n4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。\n手术名称：\n无\n出院结果：好转\n医生签名：\n日期：2025-11-07 11:44",
    "role": "user"
  }
]
[92m04:59:15 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:59:15,228 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:59:44,901 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:59:44,901 INFO     29 [qwen-vl-text] LLM output (len=4003):
{
  "encounter_date": "2025-11-07",
  "admission_date": "2025-10-30",
  "discharge_date": "2025-11-07",
  "hospital_days": 8,
  "department": "呼吸与危重医学科",
  "bed_number": "23-03床",
  "admission_condition": "李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检查：暂无",
  "admission_diagnoses": [
    {
      "name": "支气管哮喘急性发作期",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 12.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心):钾(K)4.47mmol/L白介素-6(IL-6)2.10pg/ml 肌酐(Cr)57.90μmol/L C反应蛋白(CRP)0.48mg/L丙氨酸氨基转移酶(ALT)17.50U/L天冬氨酸氨基转移酶(AST)25.40U/L。2025-10-3017:34 DIC全套(临床检验中心):纤维蛋白原(Fg)5.09g/L D-二聚体(DD)0.75μg/mLDDU。2025-10-3015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3113:11 胸部CT平扫:1、考虑双肺新增少许感染灶,以左肺为著,请结合临床并复查。2、双肺尖多发结节灶、纤维化灶,邻近双侧胸膜局限性增厚,考虑陈旧性病变,建议随诊复查。3、左肺下叶外基底段局部间质性改变,其内支气管扩张;双肺支气管壁稍增厚,考虑慢性支气管炎,请结合临床并复查。4、左肺下叶微小结节,建议随诊复查。5、纵隔内淋巴结稍增大,建议随诊复查。6、主动脉及冠状动脉硬化;胸椎退变,左侧第2前肋走行欠佳。7、肝内囊性灶,建议超声随诊复查。2025-10-3114:35肺通气功能测定及支气管舒张试验:1.中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+)2025-10-3112:33。传染病筛查三项:阴性。2025-10-3113:12乙肝5项(定量):阴性。2025-10-3115:12大便常规(不含寄生虫)(临床检验中心):未见异常。2025-10-3115:10尿液检查(尿液分析+尿有形成分):未见异常。2025-10-3114:37痰液革兰氏染色+抗酸染色+真菌(临床检验中心):未见异常。2025-11-0210:41痰细菌培养及鉴定:未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染,痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支气管等对症支持治疗,先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症治疗,经我科治疗后,患者病情较前好转,目前一般情况可,请示上级医师后予今日办理出院。",
  "auxiliary_exams": "2025-10-30 血细胞分析：WBC 4.77×10^9/L，NEU% 43.60%，EOS% 12.60%，ESR 34.03mm/h，MCHC 313.00g/L；肝功能、肾功能、电解质、心肌酶、CRP、IL-6：K 4.47mmol/L，IL-6 2.10pg/ml，Cr 57.90μmol/L，CRP 0.48mg/L，ALT 17.50U/L，AST 25.40U/L；DIC全套：Fg 5.09g/L，DD 0.75μg/mL DDU；心电图：窦性心律 HR 69 bpm；肺通气功能测定及支气管舒张试验：中重度混合性肺通气功能障碍，气道阻力增加，支气管舒张试验阳性(+)；传染病筛查三项、乙肝5项、大便常规、尿液检查、痰涂片均未见异常；痰细菌培养：未检出流感嗜血杆菌。",
  "imaging_findings": "2025-10-31 胸部CT平扫：1、考虑双肺新增少许感染灶，以左肺为著；2、双肺尖多发结节灶、纤维化灶，邻近双侧胸膜局限性增厚，考虑陈旧性病变；3、左肺下叶外基底段局部间质性改变，其内支气管扩张；双肺支气管壁稍增厚，考虑慢性支气管炎；4、左肺下叶微小结节；5、纵隔内淋巴结稍增大；6、主动脉及冠状动脉硬化；胸椎退变，左侧第2前肋走行欠佳；7、肝内囊性灶。",
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
  "condition_at_discharge": "患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，双下肢无水肿。",
  "outcome": "好转",
  "discharge_orders": "1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治疗，定期复查肺功能，呼吸科门诊随诊；2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。",
  "do_medications": [
    "布地格福 每次2吸 每日2次"
  ],
  "do_follow_up": "呼吸科门诊随诊；1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊；半年后复查胸部CT，呼吸科及胸外科随诊；定期复查腹部超声，肝胆外科随诊；定期复查肺功能。",
  "do_precautions": [
    "吸药后漱口"
  ],
  "next_treatment_date": null,
  "attending_physician": "张先明",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": 36.2,
  "vs_pulse_bpm": 92,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 115,
  "vs_diastolic_bp_mmhg": 68
}
2026-08-05 04:59:44,901 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-07]
2026-08-05 04:59:44,906 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2186433, prompt_len=1917
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
2026-08-05 04:59:59,605 INFO     29 [qwen-vl-text] coord API raw response (len=2906):
[
	{"text": "出院记录", "bbox": [441, 8, 553, 34]},
	{"text": "姓名：", "bbox": [78, 70, 123, 90]},
	{"text": "床号：23-03床", "bbox": [248, 50, 371, 73]},
	{"text": "病历号：0", "bbox": [407, 45, 496, 64]},
	{"text": "科室：呼吸与危重医学科医生站", "bbox": [614, 44, 863, 60]},
	{"text": "姓名：", "bbox": [80, 144, 121, 163]},
	{"text": "性别：女", "bbox": [438, 122, 511, 140]},
	{"text": "年龄：72岁", "bbox": [717, 114, 803, 130]},
	{"text": "民族：汉族", "bbox": [82, 175, 168, 198]},
	{"text": "病历号：00", "bbox": [438, 162, 528, 181]},
	{"text": "科室：呼吸与危重医学科医生站", "bbox": [82, 204, 327, 235]},
	{"text": "入院日期：2025-10-30 14:34", "bbox": [439, 194, 678, 221]},
	{"text": "住院天数：8", "bbox": [83, 248, 178, 271]},
	{"text": "出院日期：2025-11-07 11:44", "bbox": [439, 234, 678, 262]},
	{"text": "籍贯：贵州省贵阳市", "bbox": [83, 283, 240, 307]},
	{"text": "职业：退休人员", "bbox": [439, 279, 563, 301]},
	{"text": "单位：贵阳供电局", "bbox": [84, 324, 223, 346]},
	{"text": "住址：中国贵州省贵阳", "bbox": [83, 362, 260, 384]},
	{"text": "入院情况：", "bbox": [83, 398, 164, 417]},
	{"text": "李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无", "bbox": [83, 412, 919, 452]},
	{"text": "明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯", "bbox": [83, 439, 919, 479]},
	{"text": "血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治", "bbox": [83, 467, 919, 507]},
	{"text": "疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1", "bbox": [83, 495, 910, 534]},
	{"text": "周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门", "bbox": [83, 523, 903, 562]},
	{"text": "诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体", "bbox": [83, 551, 909, 589]},
	{"text": "重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病", "bbox": [83, 579, 891, 617]},
	{"text": "史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无", "bbox": [83, 607, 907, 644]},
	{"text": "中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学", "bbox": [83, 634, 911, 672]},
	{"text": "历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗", "bbox": [85, 662, 909, 698]},
	{"text": "史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已", "bbox": [87, 689, 891, 724]},
	{"text": "故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患", "bbox": [87, 714, 905, 749]},
	{"text": "者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，", "bbox": [87, 739, 891, 774]},
	{"text": "血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。", "bbox": [87, 765, 884, 800]},
	{"text": "心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检", "bbox": [87, 790, 892, 826]},
	{"text": "查：暂无", "bbox": [87, 832, 157, 851]},
	{"text": "入院诊断：1.支气管哮喘急性发作期", "bbox": [85, 859, 366, 879]},
	{"text": "诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床", "bbox": [85, 874, 907, 907]},
	{"text": "检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1", "bbox": [85, 901, 909, 933]},
	{"text": "2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝", "bbox": [83, 928, 910, 960]},
	{"text": "功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中", "bbox": [83, 955, 903, 987]}
]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=14.7s
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[441, 8, 553, 34]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[78, 70, 123, 90]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[2]: text=床号：23-03床, bbox=[248, 50, 371, 73]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[3]: text=病历号：0, bbox=[407, 45, 496, 64]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重医学科医生站, bbox=[614, 44, 863, 60]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[5]: text=姓名：, bbox=[80, 144, 121, 163]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女, bbox=[438, 122, 511, 140]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：72岁, bbox=[717, 114, 803, 130]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[8]: text=民族：汉族, bbox=[82, 175, 168, 198]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[9]: text=病历号：00, bbox=[438, 162, 528, 181]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[10]: text=科室：呼吸与危重医学科医生站, bbox=[82, 204, 327, 235]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[11]: text=入院日期：2025-10-30 14:34, bbox=[439, 194, 678, 221]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[12]: text=住院天数：8, bbox=[83, 248, 178, 271]
2026-08-05 04:59:59,606 INFO     29 [qwen-vl-text] coord item[13]: text=出院日期：2025-11-07 11:44, bbox=[439, 234, 678, 262]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[14]: text=籍贯：贵州省贵阳市, bbox=[83, 283, 240, 307]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[15]: text=职业：退休人员, bbox=[439, 279, 563, 301]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[16]: text=单位：贵阳供电局, bbox=[84, 324, 223, 346]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[17]: text=住址：中国贵州省贵阳, bbox=[83, 362, 260, 384]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[18]: text=入院情况：, bbox=[83, 398, 164, 417]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[19]: text=李新秋，72岁，女，因“咳嗽、咳痰5年，加重1周”于2025-10-30 14:34:00入院。现病史：5年前患者无, bbox=[83, 412, 919, 452]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[20]: text=明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，不易咳出，无发热、咯, bbox=[83, 439, 919, 479]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[21]: text=血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管哮喘”，行对症支持治, bbox=[83, 467, 919, 507]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[22]: text=疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感和天气变化时加重。1, bbox=[83, 495, 910, 534]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[23]: text=周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治就诊于我院我科门, bbox=[83, 523, 903, 562]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[24]: text=诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二便如常，近1年体, bbox=[83, 551, 909, 589]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[25]: text=重减少4kg。既往史、个人史、家族史：患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病, bbox=[83, 579, 891, 617]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[26]: text=史；无肺结核；无病毒性肝炎；无其他传染病；食物、药物过敏无；无外伤史；无手术史；无输血史；无, bbox=[83, 607, 907, 644]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[27]: text=中毒史；无长期用药史；无可能成瘾药物。疫苗接种史不详；出生于贵州省贵阳市，职业：离退休人员，学, bbox=[83, 634, 911, 672]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[28]: text=历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长地：贵州省贵阳市，无疫区居留史。无治疗, bbox=[85, 662, 909, 698]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[29]: text=史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物质接触史。；家族史：父亲已故，母亲已, bbox=[87, 689, 891, 724]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[30]: text=故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否认二系三代有遗传病史。患, bbox=[87, 714, 905, 749]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[31]: text=者否认有遗传倾向的疾病。入院专科体查：生命体征：体温：36.2℃，脉搏：92次/分，呼吸：20次/分，, bbox=[87, 739, 891, 774]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[32]: text=血氧饱和度：93%，血压：上肢115/68mmHg。神志清楚，查体配合，双肺呼吸音清，未闻及干湿性啰音。, bbox=[87, 765, 884, 800]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[33]: text=心律齐，各瓣膜听诊区未闻及明显异常杂音，腹平软，无压痛、反跳痛及肌紧张，双下肢无水肿。辅助检, bbox=[87, 790, 892, 826]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[34]: text=查：暂无, bbox=[87, 832, 157, 851]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[35]: text=入院诊断：1.支气管哮喘急性发作期, bbox=[85, 859, 366, 879]
2026-08-05 04:59:59,607 INFO     29 [qwen-vl-text] coord item[36]: text=诊疗经过：入院积极完善相关检查：2025-10-30 16:53 血沉(临床检验中心)、血细胞分析(五分类)(临床, bbox=[85, 874, 907, 907]
2026-08-05 04:59:59,608 INFO     29 [qwen-vl-text] coord item[37]: text=检验中心)：白细胞计数(WBC) 4.7710~9/L 中性粒细胞百分比(NEU%) 43.60% 嗜酸性粒细胞百分比(EOS%) 1, bbox=[85, 901, 909, 933]
2026-08-05 04:59:59,608 INFO     29 [qwen-vl-text] coord item[38]: text=2.60% 红细胞沉降率(ESR) 34.03mm/h 平均红细胞血红蛋白浓度(MCHC) 313.00g/L。2025-10-30 17:10 肝, bbox=[83, 928, 910, 960]
2026-08-05 04:59:59,608 INFO     29 [qwen-vl-text] coord item[39]: text=功能半套(临床检验中心)、C-反应蛋白检测(CRP)(临床检验中心)、尿素(临床检验中心)、钾(临床检验中, bbox=[83, 955, 903, 987]
2026-08-05 04:59:59,608 INFO     29 [qwen-vl-text] page=4 — 40/40 coords, api_time=14.7s
2026-08-05 04:59:59,617 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3462031, prompt_len=2017
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心):钾(K)4.47mmol/L白介素-6(IL-6)2.10pg/ml", "肌酐(Cr)57.90μmol/L C反应蛋白(CRP)0.48mg/L丙氨酸氨基转移酶(ALT)17.50U/L天冬氨酸氨基转移", "酶(AST)25.40U/L。2025-10-3017:34 DIC全套(临床检验中心):纤维蛋白原(Fg)5.09g/L D-二聚体(DD)", "0.75μg/mLDDU。2025-10-3015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3", "015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3113:11 胸部CT平扫:1、考虑双肺新增少许感染灶,以左肺为著,请结合临床并复查。2、双肺尖多发结节灶、纤维化灶,邻近双侧", "1/3", "贵州醫科大學附屬醫院", "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "出院记录", "姓名:", "床号:23-03床", "病历号:", "科室:呼吸与危重医学科医生站", "胸膜局限性增厚,考虑陈旧性病变,建议随诊复查。3、左肺下叶外基底段局部间质性改变,其内支气管", "扩张;双肺支气管壁稍增厚,考虑慢性支气管炎,请结合临床并复查。4、左肺下叶微小结节,建议随诊", "复查。5、纵隔内淋巴结稍增大,建议随诊复查。6、主动脉及冠状动脉硬化;胸椎退变,左侧第2前肋走", "行欠佳。7、肝内囊性灶,建议超声随诊复查。2025-10-3114:35肺通气功能测定及支气管舒张试验:1.", "中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+)2025-10-3112:33。传染病筛查", "三项:阴性。2025-10-3113:12乙肝5项(定量):阴性。2025-10-3115:12大便常规(不含寄生虫)(临", "床检验中心):未见异常。2025-10-3115:10尿液检查(尿液分析+尿有形成分):未见异常。2025-10-31", "14:37痰液革兰氏染色+抗酸染色+真菌(临床检验中心):未见异常。2025-11-0210:41痰细菌培养及鉴", "定:未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染,痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "气管等对症支持治疗,先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "治疗,经我科治疗后,患者病情较前好转,目前一般情况可,请示上级医师盾予今日办理出院。", "出院诊断:1.支气管哮喘急性发作期;2.社区获得性肺炎,非重症;3.慢性阻塞性肺疾病;4.左肺下叶小", "结节;5.肝囊肿。", "出院情况:患者咳嗽、咳痰、胸闷、气促好转,无呼吸困难,无畏寒、发热,无恶心、呕吐等不适。查", "体:生命体征平稳。全身皮肤黏膜、巩膜无黄染,双肺呼吸音清,未闻及干湿性啰音。律齐,各瓣膜听诊", "区未闻及病理性杂音,腹软,全腹无压痛及反跳痛,肝脾肋下未及,肝脾肋下未及,双下肢无水肿。", "VTE评估:"]

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
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord API raw response (len=2609):
[
	{"text": "心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心):钾(K)4.47mmol/L白介素-6(IL-6)2.10pg/ml", "bbox": [68, 13, 898, 38]},
	{"text": "肌酐(Cr)57.90μmol/L C反应蛋白(CRP)0.48mg/L丙氨酸氨基转移酶(ALT)17.50U/L天冬氨酸氨基转移", "bbox": [68, 40, 904, 64]},
	{"text": "酶(AST)25.40U/L。2025-10-3017:34 DIC全套(临床检验中心):纤维蛋白原(Fg)5.09g/L D-二聚体(DD)", "bbox": [68, 65, 893, 110]},
	{"text": "0.75μg/mLDDU。2025-10-3015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3", "bbox": [68, 114, 904, 138]},
	{"text": "015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3113:11 胸部CT平扫:1、考虑双肺新增少许感染灶,以左肺为著,请结合临床并复查。2、双肺尖多发结节灶、纤维化灶,邻近双侧", "bbox": [68, 141, 904, 165]},
	{"text": "1/3", "bbox": [468, 220, 493, 236]},
	{"text": "贵州醫科大學附屬醫院", "bbox": [344, 359, 720, 398]},
	{"text": "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "bbox": [348, 405, 720, 420]},
	{"text": "出院记录", "bbox": [423, 440, 535, 466]},
	{"text": "姓名:", "bbox": [63, 478, 107, 496]},
	{"text": "床号:23-03床", "bbox": [232, 477, 354, 494]},
	{"text": "病历号:", "bbox": [390, 477, 457, 494]},
	{"text": "科室:呼吸与危重医学科医生站", "bbox": [598, 476, 855, 493]},
	{"text": "胸膜局限性增厚,考虑陈旧性病变,建议随诊复查。3、左肺下叶外基底段局部间质性改变,其内支气管", "bbox": [63, 517, 893, 538]},
	{"text": "扩张;双肺支气管壁稍增厚,考虑慢性支气管炎,请结合临床并复查。4、左肺下叶微小结节,建议随诊", "bbox": [63, 543, 893, 565]},
	{"text": "复查。5、纵隔内淋巴结稍增大,建议随诊复查。6、主动脉及冠状动脉硬化;胸椎退变,左侧第2前肋走", "bbox": [63, 570, 903, 591]},
	{"text": "行欠佳。7、肝内囊性灶,建议超声随诊复查。2025-10-3114:35肺通气功能测定及支气管舒张试验:1.", "bbox": [63, 597, 900, 618]},
	{"text": "中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+)2025-10-3112:33。传染病筛查", "bbox": [60, 624, 904, 646]},
	{"text": "三项:阴性。2025-10-3113:12乙肝5项(定量):阴性。2025-10-3115:12大便常规(不含寄生虫)(临", "bbox": [57, 651, 895, 673]},
	{"text": "床检验中心):未见异常。2025-10-3115:10尿液检查(尿液分析+尿有形成分):未见异常。2025-10-31", "bbox": [55, 678, 903, 700]},
	{"text": "14:37痰液革兰氏染色+抗酸染色+真菌(临床检验中心):未见异常。2025-11-0210:41痰细菌培养及鉴", "bbox": [53, 705, 887, 727]},
	{"text": "定:未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染,痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "bbox": [50, 732, 904, 754]},
	{"text": "气管等对症支持治疗,先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "bbox": [48, 759, 898, 781]},
	{"text": "治疗,经我科治疗后,患者病情较前好转,目前一般情况可,请示上级医师盾予今日办理出院。", "bbox": [47, 787, 813, 809]},
	{"text": "出院诊断:1.支气管哮喘急性发作期;2.社区获得性肺炎,非重症;3.慢性阻塞性肺疾病;4.左肺下叶小", "bbox": [47, 814, 904, 836]},
	{"text": "结节;5.肝囊肿。", "bbox": [45, 844, 187, 866]},
	{"text": "出院情况:患者咳嗽、咳痰、胸闷、气促好转,无呼吸困难,无畏寒、发热,无恶心、呕吐等不适。查", "bbox": [45, 870, 888, 893]},
	{"text": "体:生命体征平稳。全身皮肤黏膜、巩膜无黄染,双肺呼吸音清,未闻及干湿性啰音。律齐,各瓣膜听诊", "bbox": [44, 897, 898, 920]},
	{"text": "区未闻及病理性杂音,腹软,全腹无压痛及反跳痛,肝脾肋下未及,肝脾肋下未及,双下肢无水肿。", "bbox": [44, 925, 852, 948]},
	{"text": "VTE评估:", "bbox": [43, 960, 126, 980]}
]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=16.6s
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[0]: text=心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心):钾(K)4.47mmol/L白介素-6(IL-6)2.10pg/ml, bbox=[68, 13, 898, 38]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[1]: text=肌酐(Cr)57.90μmol/L C反应蛋白(CRP)0.48mg/L丙氨酸氨基转移酶(ALT)17.50U/L天冬氨酸氨基转移, bbox=[68, 40, 904, 64]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[2]: text=酶(AST)25.40U/L。2025-10-3017:34 DIC全套(临床检验中心):纤维蛋白原(Fg)5.09g/L D-二聚体(DD), bbox=[68, 65, 893, 110]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[3]: text=0.75μg/mLDDU。2025-10-3015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3, bbox=[68, 114, 904, 138]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[4]: text=015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3113:11 胸部CT平扫:1、考虑双肺新增少许感染灶,以左肺为著,请结合临床并复查。2、双肺尖多发结节灶、纤维化灶,邻近双侧, bbox=[68, 141, 904, 165]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[5]: text=1/3, bbox=[468, 220, 493, 236]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[6]: text=贵州醫科大學附屬醫院, bbox=[344, 359, 720, 398]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[7]: text=THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY, bbox=[348, 405, 720, 420]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[8]: text=出院记录, bbox=[423, 440, 535, 466]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[9]: text=姓名:, bbox=[63, 478, 107, 496]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[10]: text=床号:23-03床, bbox=[232, 477, 354, 494]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[11]: text=病历号:, bbox=[390, 477, 457, 494]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[12]: text=科室:呼吸与危重医学科医生站, bbox=[598, 476, 855, 493]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[13]: text=胸膜局限性增厚,考虑陈旧性病变,建议随诊复查。3、左肺下叶外基底段局部间质性改变,其内支气管, bbox=[63, 517, 893, 538]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[14]: text=扩张;双肺支气管壁稍增厚,考虑慢性支气管炎,请结合临床并复查。4、左肺下叶微小结节,建议随诊, bbox=[63, 543, 893, 565]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[15]: text=复查。5、纵隔内淋巴结稍增大,建议随诊复查。6、主动脉及冠状动脉硬化;胸椎退变,左侧第2前肋走, bbox=[63, 570, 903, 591]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[16]: text=行欠佳。7、肝内囊性灶,建议超声随诊复查。2025-10-3114:35肺通气功能测定及支气管舒张试验:1., bbox=[63, 597, 900, 618]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[17]: text=中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+)2025-10-3112:33。传染病筛查, bbox=[60, 624, 904, 646]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[18]: text=三项:阴性。2025-10-3113:12乙肝5项(定量):阴性。2025-10-3115:12大便常规(不含寄生虫)(临, bbox=[57, 651, 895, 673]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[19]: text=床检验中心):未见异常。2025-10-3115:10尿液检查(尿液分析+尿有形成分):未见异常。2025-10-31, bbox=[55, 678, 903, 700]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[20]: text=14:37痰液革兰氏染色+抗酸染色+真菌(临床检验中心):未见异常。2025-11-0210:41痰细菌培养及鉴, bbox=[53, 705, 887, 727]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[21]: text=定:未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染,痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支, bbox=[50, 732, 904, 754]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[22]: text=气管等对症支持治疗,先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症, bbox=[48, 759, 898, 781]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[23]: text=治疗,经我科治疗后,患者病情较前好转,目前一般情况可,请示上级医师盾予今日办理出院。, bbox=[47, 787, 813, 809]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[24]: text=出院诊断:1.支气管哮喘急性发作期;2.社区获得性肺炎,非重症;3.慢性阻塞性肺疾病;4.左肺下叶小, bbox=[47, 814, 904, 836]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[25]: text=结节;5.肝囊肿。, bbox=[45, 844, 187, 866]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[26]: text=出院情况:患者咳嗽、咳痰、胸闷、气促好转,无呼吸困难,无畏寒、发热,无恶心、呕吐等不适。查, bbox=[45, 870, 888, 893]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[27]: text=体:生命体征平稳。全身皮肤黏膜、巩膜无黄染,双肺呼吸音清,未闻及干湿性啰音。律齐,各瓣膜听诊, bbox=[44, 897, 898, 920]
2026-08-05 05:00:16,261 INFO     29 [qwen-vl-text] coord item[28]: text=区未闻及病理性杂音,腹软,全腹无压痛及反跳痛,肝脾肋下未及,肝脾肋下未及,双下肢无水肿。, bbox=[44, 925, 852, 948]
2026-08-05 05:00:16,262 INFO     29 [qwen-vl-text] coord item[29]: text=VTE评估:, bbox=[43, 960, 126, 980]
2026-08-05 05:00:16,262 INFO     29 [qwen-vl-text] page=5 — 30/30 coords, api_time=16.6s
2026-08-05 05:00:16,264 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1083764, prompt_len=1407
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
2026-08-05 05:00:25,414 INFO     29 [qwen-vl-text] coord API raw response (len=1710):
[
	{"text": "床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31", "bbox": [17, 7, 891, 31]},
	{"text": "14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴", "bbox": [18, 33, 874, 60]},
	{"text": "定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支", "bbox": [17, 60, 895, 89]},
	{"text": "气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症", "bbox": [17, 87, 888, 116]},
	{"text": "治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。", "bbox": [18, 113, 807, 139]},
	{"text": "出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小", "bbox": [20, 139, 898, 173]},
	{"text": "结节；5.肝囊肿。", "bbox": [20, 166, 164, 186]},
	{"text": "出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查", "bbox": [24, 192, 886, 230]},
	{"text": "体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊", "bbox": [24, 219, 900, 260]},
	{"text": "区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。", "bbox": [27, 247, 855, 282]},
	{"text": "VTE评估：", "bbox": [29, 273, 111, 291]},
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
2026-08-05 05:00:25,414 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=9.2s
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[0]: text=床检验中心）：未见异常。2025-10-31 15:10 尿液检查（尿液分析+尿有形成分）：未见异常。2025-10-31, bbox=[17, 7, 891, 31]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[1]: text=14:37 痰液革兰氏染色+抗酸染色+真菌(临床检验中心)：未见异常。2025-11-02 10:41 痰细菌培养及鉴, bbox=[18, 33, 874, 60]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[2]: text=定：未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染，痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支, bbox=[17, 60, 895, 89]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[3]: text=气管等对症支持治疗，先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症, bbox=[17, 87, 888, 116]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[4]: text=治疗，经我科治疗后，患者病情较前好转，目前一般情况可，请示上级医师后予今日办理出院。, bbox=[18, 113, 807, 139]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[5]: text=出院诊断：1.支气管哮喘急性发作期；2.社区获得性肺炎，非重症；3.慢性阻塞性肺疾病；4.左肺下叶小, bbox=[20, 139, 898, 173]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[6]: text=结节；5.肝囊肿。, bbox=[20, 166, 164, 186]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[7]: text=出院情况：患者咳嗽、咳痰、胸闷、气促好转，无呼吸困难，无畏寒、发热，无恶心、呕吐等不适。查, bbox=[24, 192, 886, 230]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[8]: text=体：生命体征平稳。全身皮肤黏膜、巩膜无黄染，双肺呼吸音清，未闻及干湿性啰音。律齐，各瓣膜听诊, bbox=[24, 219, 900, 260]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[9]: text=区未闻及病理性杂音，腹软，全腹无压痛及反跳痛，肝脾肋下未及，肝脾肋下未及，双下肢无水肿。, bbox=[27, 247, 855, 282]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[10]: text=VTE评估：, bbox=[29, 273, 111, 291]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[11]: text=Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：, bbox=[31, 300, 677, 331]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[12]: text=出院医嘱：, bbox=[40, 353, 127, 372]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[13]: text=1、针对患者支气管哮喘及慢性阻塞性肺疾病，继续予布地格福（每次2吸 每日2次，吸药后漱口）吸入治, bbox=[42, 379, 907, 440]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[14]: text=疗，定期复查肺功能，呼吸科门诊随诊；, bbox=[43, 407, 363, 434]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[15]: text=2、针对肺部感染，1月后复查胸部CT，于我科张先明主任医师特需专家门诊（每周二上午）复诊。, bbox=[44, 434, 842, 490]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[16]: text=3、针对左肺下叶小结节，半年后复查胸部CT，呼吸科及胸外科随诊。, bbox=[45, 460, 589, 491]
2026-08-05 05:00:25,415 INFO     29 [qwen-vl-text] coord item[17]: text=4、针对肝囊肿，定期复查腹部超声，肝胆外科随诊。, bbox=[47, 487, 460, 512]
2026-08-05 05:00:25,416 INFO     29 [qwen-vl-text] coord item[18]: text=手术名称：, bbox=[50, 512, 134, 530]
2026-08-05 05:00:25,416 INFO     29 [qwen-vl-text] coord item[19]: text=无, bbox=[55, 544, 74, 561]
2026-08-05 05:00:25,416 INFO     29 [qwen-vl-text] coord item[20]: text=出院结果：好转, bbox=[59, 574, 176, 594]
2026-08-05 05:00:25,416 INFO     29 [qwen-vl-text] coord item[21]: text=医生签名：, bbox=[688, 651, 772, 675]
2026-08-05 05:00:25,416 INFO     29 [qwen-vl-text] coord item[22]: text=日期：2025-11-07 11:44, bbox=[710, 693, 907, 721]
2026-08-05 05:00:25,416 INFO     29 [qwen-vl-text] page=6 — 23/23 coords, api_time=9.2s
2026-08-05 05:00:25,416 INFO     29 [qwen-vl-text] new_positions (93):
[[4, 269.892, 338.436, 5.03718408203125, 21.408032348632812], [4, 47.736, 75.276, 44.075360717773435, 56.668320922851564], [4, 151.776, 227.052, 31.482400512695314, 45.964304748535156], [4, 249.084, 303.552, 28.334160461425782, 40.29747265625], [4, 375.768, 528.156, 27.704512451171876, 37.77888061523438], [4, 48.96, 74.05199999999999, 90.66931347656251, 102.63262567138672], [4, 268.056, 312.73199999999997, 76.81705725097656, 88.15072143554687], [4, 438.804, 491.436, 71.77987316894531, 81.85424133300782], [4, 50.184, 102.816, 110.1884017944336, 124.67030603027344], [4, 268.056, 323.13599999999997, 102.00297766113282, 113.96628985595703], [4, 50.184, 200.124, 128.44819409179686, 147.96728240966797], [4, 268.668, 414.936, 122.15171398925781, 139.1522102661133], [4, 50.796, 108.93599999999999, 156.15270654296876, 170.6346107788086], [4, 268.668, 414.936, 147.33763439941407, 164.96777868652345], [4, 50.796, 146.88, 178.19038690185548, 193.3019391479492], [4, 268.668, 344.556, 175.67179486083984, 189.5240510864258], [4, 51.408, 136.476, 204.00595532226563, 217.85821154785157], [4, 50.796, 159.12, 227.93257971191406, 241.78483593750002], [4, 50.796, 100.368, 250.5999080810547, 262.5632202758789], [4, 50.796, 562.428, 259.4149802246094, 284.60090063476565], [4, 50.796, 562.428, 276.41547650146487, 301.6013969116211], [4, 50.796, 562.428, 294.04562078857424, 319.2315411987305], [4, 50.796, 556.92, 311.6757650756836, 336.23203747558597], [4, 50.796, 552.636, 329.305909362793, 353.86218176269534], [4, 50.796, 556.308, 346.93605364990236, 370.8626780395508], [4, 50.796, 545.292, 364.56619793701174, 388.4928223266602], [4, 50.796, 555.084, 382.1963422241211, 405.49331860351566], [4, 50.796, 557.532, 399.1968385009766, 423.12346289062504], [4, 52.019999999999996, 556.308, 416.82698278808596, 439.49431115722655], [4, 53.244, 545.292, 433.82747906494143, 455.8651594238281], [4, 53.244, 553.86, 449.5686793212891, 471.6063596801758], [4, 53.244, 545.292, 465.3098795776367, 487.34755993652345], [4, 53.244, 541.008, 481.6807278442383, 503.718408203125], [4, 53.244, 545.904, 497.42192810058594, 520.0892564697266], [4, 53.244, 96.084, 523.86714453125, 535.8304567260742], [4, 52.019999999999996, 223.992, 540.8676408081055, 553.4606010131836], [4, 52.019999999999996, 555.084, 550.3123609619141, 571.090745300293], [4, 52.019999999999996, 556.308, 567.3128572387695, 587.4615935668945], [4, 50.796, 556.92, 584.3133535156251, 604.46208984375], [4, 50.796, 552.636, 601.3138497924805, 621.4625861206055], [5, 41.616, 549.576, 8.243183044433593, 24.095458129882815], [5, 41.616, 553.2479999999999, 25.36364013671875, 40.58182421875], [5, 41.616, 546.516, 41.21591522216797, 69.75001037597656], [5, 41.616, 553.2479999999999, 72.28637438964844, 87.50455847167969], [5, 41.616, 553.2479999999999, 89.4068314819336, 104.62501556396485], [5, 286.416, 301.716, 139.50002075195312, 149.64547680664063], [5, 210.528, 440.64, 227.6386702270508, 252.36821936035156], [5, 212.976, 440.64, 256.80685638427735, 266.3182214355469], [5, 258.876, 327.42, 279.00004150390623, 295.48640759277345], [5, 38.556, 65.484, 303.0954996337891, 314.5091376953125], [5, 141.984, 216.648, 302.4614086303711, 313.24095568847656], [5, 238.68, 279.68399999999997, 302.4614086303711, 313.24095568847656], [5, 365.976, 523.26, 301.8273176269531, 312.6068646850586], [5, 38.556, 546.516, 327.82504876708987, 341.1409598388672], [5, 38.556, 546.516, 344.311414855957, 358.2614169311523], [5, 38.556, 552.636, 361.4318719482422, 374.74778302001954], [5, 38.556, 550.8, 378.55232904052735, 391.8682401123047], [5, 36.72, 553.2479999999999, 395.6727861328125, 409.6227882080078], [5, 34.884, 547.74, 412.7932432250977, 426.743245300293], [5, 33.66, 552.636, 429.9137003173828, 443.86370239257815], [5, 32.436, 542.8439999999999, 447.03415740966796, 460.9841594848633], [5, 30.599999999999998, 553.2479999999999, 464.1546145019531, 478.1046165771484], [5, 29.375999999999998, 549.576, 481.2750715942383, 495.2250736694336], [5, 28.764, 497.556, 499.0296196899414, 512.9796217651367], [5, 28.764, 553.2479999999999, 516.1500767822266, 530.1000788574219], [5, 27.54, 114.444, 535.1728068847656, 549.1228089599609], [5, 27.54, 543.456, 551.6591729736328, 566.2432660522461], [5, 26.928, 549.576, 568.779630065918, 583.3637231445313], [5, 26.928, 521.424, 586.5341781616211, 601.1182712402344], [5, 26.316, 77.112, 608.7273632812501, 621.4091833496094], [6, 10.404, 545.292, 4.364990051269531, 19.33067022705078], [6, 11.016, 534.888, 20.57781024169922, 37.414200439453126], [6, 10.404, 547.74, 37.414200439453126, 55.49773065185547], [6, 10.404, 543.456, 54.25059063720703, 72.33412084960938], [6, 11.016, 493.884, 70.46341082763672, 86.6762310180664], [6, 12.24, 549.576, 86.6762310180664, 107.87761126708985], [6, 12.24, 100.368, 103.51262121582032, 115.98402136230469], [6, 14.687999999999999, 542.232, 119.72544140625, 143.42110168457032], [6, 14.687999999999999, 550.8, 136.5618316040039, 162.12820190429687], [6, 16.524, 523.26, 154.02179180908203, 175.84674206542968], [6, 17.748, 67.932, 170.2346119995117, 181.45887213134765], [6, 18.972, 414.324, 187.0710021972656, 206.40167242431642], [6, 24.48, 77.724, 220.12021258544922, 231.96804272460938], [6, 25.704, 555.084, 236.3330327758789, 274.37080322265626], [6, 26.316, 222.156, 253.79299298095702, 270.62938317871095], [6, 26.928, 515.304, 270.62938317871095, 305.5493035888672], [6, 27.54, 360.468, 286.84220336914063, 306.1728735961914], [6, 28.764, 281.52, 303.6785935668945, 319.26784375], [6, 30.599999999999998, 82.008, 319.26784375, 330.49210388183593], [6, 33.66, 45.288, 339.222083984375, 349.82277410888673], [6, 36.108, 107.712, 357.92918420410155, 370.4005843505859], [6, 421.056, 472.464, 405.9440747680664, 420.90975494384764], [6, 434.52, 555.084, 432.1340150756836, 449.5939752807617]]
2026-08-05 05:00:25,416 INFO     29 [qwen-vl-text] ═══ DONE ═══ 93 positions, pages=3, time=71.5s
2026-08-05 05:00:25,430 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 05:00:25,431 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 05:00:25,431 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 05:00:25,431 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:00:25.431+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:00:25,437 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:00:25,437 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-05 05:00:25,437 INFO     29 [qwen-vl-text] positions(140): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:00:25,437 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [40, 32, 38, 30]
2026-08-05 05:00:25,784 INFO     29 [qwen-vl-text] page=0, rect=612x627, img=(1700x1741), dpi=200
2026-08-05 05:00:26,110 INFO     29 [qwen-vl-text] page=1, rect=612x620, img=(1700x1723), dpi=200
2026-08-05 05:00:26,437 INFO     29 [qwen-vl-text] page=2, rect=612x618, img=(1700x1718), dpi=200
2026-08-05 05:00:26,755 INFO     29 [qwen-vl-text] page=3, rect=612x628, img=(1700x1745), dpi=200
2026-08-05 05:00:26,757 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2280
2026-08-05 05:00:26,758 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:00:26,758 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 139, \"encounter_dates\": [\"2025-10-30\"], \"department\": \"呼吸与危重医学科\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "入院记录\n姓名：\n床号：23-03床\n病历号：0\n科室：呼吸与危重医学科医生\n站\n姓名：\n性别：女\n年龄：72岁\n出生地：贵州省贵阳市\n职业：退休人员\n民族：汉族\n婚姻：已婚\n联系地址：中国贵州省贵阳市\n入院时间：2025-10-30 14:34\n病史陈述者：本人\n主诉：咳嗽、咳痰5年，加重1周\n现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，\n不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管\n哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感\n和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治\n就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二\n便如常，近1年体重减少4kg。\n既往史：\n患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染\n病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫\n苗接种史不详\n个人史：\n出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长\n地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物\n质接触史。\n婚育史：\n已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。\n月经史：\n初潮年龄17岁 经期3-4天 绝经年龄53岁 月经及白带情况：正常\n月经周期30天\n家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否\n认二系三代有遗传病史。患者否认有遗传倾向的疾病。\n体格检查\n生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60\n体格检查\n生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体\n重：44kg，腰围：cm，BMI：18.8 kg/m²\n一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常\n表情：正常体位：自主体位步态：平稳配合检查：配合\n皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无\n皮疹：无紫癜：无\n1/3\n贵州醫科大學附属醫院\nTHE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY\n入院记录\n姓名：\n床号：23-03床\n病历号\n科室：呼吸与危重医学科医生\n站\n水肿：无脱水现象：无松紧度：适中\n温度：适中出汗：无显性出汗瘢痕：无感染：无\n头颅：大小：正常畸形：无包块：无\n凹陷：无压痛：无\n眼：眼睑：无水肿结膜：无充血巩膜：无黄染\n眼球四个象限运动：左眼：正常右眼：正常\n眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆\n对光反射：左眼：灵敏右眼：灵敏\n鼻：外形：正常其他异常：无鼻旁窦压痛：无\n口：唇：无紫绀粘膜：无充血腮腺导管开口：正常\n舌：伸舌居中牙龈：无肿胀龋齿：无\n咽喉：扁桃体：正常咽：无充血声音：正常\n淋巴：淋巴结：全身浅表淋巴结未及肿大\n颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张\n气管：居中颈静脉回流征：无\n甲状腺：无肿大\n眼球四个象限运动：左眼：正常 右眼：正常\n眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆\n对光反射：左眼：灵敏 右眼：灵敏\n鼻：外形：正常 其他异常：无 鼻旁窦压痛：无\n口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常\n舌：伸舌居中 牙龈：无肿胀 龋齿：无\n咽 喉：扁桃体：正常 咽：无充血 声音：正常\n淋巴 巴：淋巴结：全身浅表淋巴结未及肿大\n颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张\n气管：居中 颈静脉回流征：无\n甲状腺：无肿大\n胸部 部：胸廓：无畸形 乳房：\n肺 部：视诊：呼吸运动\n触诊：\n叩诊：\n听诊：\n语音传导\n心 脏：视诊：\n触诊：心尖搏动：正常 振颤：无 心包摩擦感：无\n叩诊：\n第五肋间内0.5cm\n心界\n右(cm)\n肋间\n左(cm)\n2\n2\n2\n1\n3\n(左锁骨中线距胸骨线7.5cm)\n听诊：心率：92次/分 心律：齐 心音：未闻及异常心\n额外心音：无 杂音：无 心包摩擦音：\n周围血管：异常血管征：无\n腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出\n其他异常：无\n触诊：腹壁：柔软 压痛：无\n2/3\n站\n反跳痛：无\n液波振颤：无 振水声：无\n腹部包块：无\n肝：肋下未及\n胆囊：未触及 Murphy征：阴性\n脾：未触及\n叩诊：肝浊音界：正常 移动性浊音：无\n肾区叩痛：无\n听诊：肠鸣音：正常 肠鸣音频率：4次/分\n气过水音：无 血管杂音：无\n肛门直肠：未检\n生殖器：未检\n脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限\n压痛，叩痛：无\n杵状指趾：无\n神经系统：腹壁反射：正常 肢体瘫痪：无\n肌张力：正常 肌力：V级\n肱二头肌反射：正常 Hoffman征：阴性\n膝腱反射：正常 Kernig征：阴性\n跟腱反射：正常Babinski征：阴性\n其他：无\n补充及专科情况\n双肺呼吸音清，未闻及干湿性啰音。\n辅助检查：暂无\nVTE评估：\nPadua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：\n入院诊断：1.支气管哮喘急性发作期\n医师签名：\n日期：2025-10-30 16:38",
    "role": "user"
  }
]
2026-08-05 05:00:38,506 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:00:38,506 INFO     29 [qwen-vl-text] LLM output (len=2291):
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
  "pe_heart": "心率：92次/分 心律：齐 心音：未闻及异常心 额外心音：无 杂音：无 心包摩擦音：无 心尖搏动：正常 振颤：无 心包摩擦感：无 心界：第五肋间内0.5cm 右(cm) 2 2 2 1 3 左(cm) (左锁骨中线距胸骨线7.5cm)",
  "pe_abdomen": "外形：平坦 腹式呼吸：存在 脐：无突出 其他异常：无 腹壁：柔软 压痛：无 反跳痛：无 液波振颤：无 振水声：无 腹部包块：无 肝：肋下未及 胆囊：未触及 Murphy征：阴性 脾：未触及 肝浊音界：正常 移动性浊音：无 肾区叩痛：无 肠鸣音：正常 肠鸣音频率：4次/分 气过水音：无 血管杂音：无",
  "pe_extremities": "脊柱：无畸形 四肢：正常 活动：不受限 压痛，叩痛：无 杵状指趾：无",
  "pe_nervous_system": "腹壁反射：正常 肢体瘫痪：无 肌张力：正常 肌力：V级 肱二头肌反射：正常 Hoffman征：阴性 膝腱反射：正常 Kernig征：阴性 跟腱反射：正常 Babinski征：阴性",
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
2026-08-05 05:00:38,506 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-30]
2026-08-05 05:00:38,508 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1116015, prompt_len=1548
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["入院记录", "姓名：", "床号：23-03床", "病历号：0", "科室：呼吸与危重医学科医生", "站", "姓名：", "性别：女", "年龄：72岁", "出生地：贵州省贵阳市", "职业：退休人员", "民族：汉族", "婚姻：已婚", "联系地址：中国贵州省贵阳市", "入院时间：2025-10-30 14:34", "病史陈述者：本人", "主诉：咳嗽、咳痰5年，加重1周", "现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，", "不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管", "哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感", "和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治", "就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二", "便如常，近1年体重减少4kg。", "既往史：", "患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染", "病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫", "苗接种史不详", "个人史：", "出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长", "地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物", "质接触史。", "婚育史：", "已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。", "月经史：", "初潮年龄17岁 经期3-4天 绝经年龄53岁 月经及白带情况：正常", "月经周期30天", "家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否", "认二系三代有遗传病史。患者否认有遗传倾向的疾病。", "体格检查", "生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60"]

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
2026-08-05 05:00:54,049 INFO     29 [qwen-vl-text] coord API raw response (len=2536):
[
	{"text": "入院记录", "bbox": [425, 0, 538, 24]},
	{"text": "姓名：", "bbox": [77, 37, 118, 56]},
	{"text": "床号：23-03床", "bbox": [241, 37, 359, 55]},
	{"text": "病历号：0", "bbox": [432, 35, 520, 53]},
	{"text": "科室：呼吸与危重医学科医生", "bbox": [655, 34, 895, 51]},
	{"text": "站", "bbox": [77, 64, 94, 81]},
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
	{"text": "和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治", "bbox": [83, 445, 908, 475]},
	{"text": "就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二", "bbox": [84, 472, 900, 501]},
	{"text": "便如常，近1年体重减少4kg。", "bbox": [84, 511, 300, 531]},
	{"text": "既往史：", "bbox": [85, 542, 148, 561]},
	{"text": "患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染", "bbox": [85, 558, 897, 587]},
	{"text": "病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫", "bbox": [85, 585, 905, 613]},
	{"text": "苗接种史不详", "bbox": [86, 620, 188, 639]},
	{"text": "个人史：", "bbox": [86, 648, 148, 667]},
	{"text": "出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长", "bbox": [86, 669, 896, 693]},
	{"text": "地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物", "bbox": [86, 695, 896, 719]},
	{"text": "质接触史。", "bbox": [86, 724, 164, 743]},
	{"text": "婚育史：", "bbox": [86, 751, 150, 770]},
	{"text": "已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。", "bbox": [87, 779, 584, 801]},
	{"text": "月经史：", "bbox": [87, 805, 151, 824]},
	{"text": "初潮年龄17岁 经期3-4天 绝经年龄53岁 月经及白带情况：正常", "bbox": [88, 845, 664, 877]},
	{"text": "月经周期30天", "bbox": [223, 880, 333, 900]},
	{"text": "家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否", "bbox": [90, 906, 904, 927]},
	{"text": "认二系三代有遗传病史。患者否认有遗传倾向的疾病。", "bbox": [90, 932, 502, 952]},
	{"text": "体格检查", "bbox": [461, 960, 534, 979]},
	{"text": "生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60", "bbox": [90, 984, 688, 1000]}
]
2026-08-05 05:00:54,049 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=15.5s
2026-08-05 05:00:54,049 INFO     29 [qwen-vl-text] coord item[0]: text=入院记录, bbox=[425, 0, 538, 24]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[77, 37, 118, 56]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[2]: text=床号：23-03床, bbox=[241, 37, 359, 55]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[3]: text=病历号：0, bbox=[432, 35, 520, 53]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重医学科医生, bbox=[655, 34, 895, 51]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[5]: text=站, bbox=[77, 64, 94, 81]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[6]: text=姓名：, bbox=[88, 143, 161, 162]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[7]: text=性别：女, bbox=[456, 137, 585, 156]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：72岁, bbox=[88, 180, 218, 200]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[9]: text=出生地：贵州省贵阳市, bbox=[456, 173, 676, 193]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[10]: text=职业：退休人员, bbox=[88, 220, 255, 240]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[11]: text=民族：汉族, bbox=[458, 211, 604, 231]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[12]: text=婚姻：已婚, bbox=[88, 258, 222, 278]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[13]: text=联系地址：中国贵州省贵阳市, bbox=[459, 247, 710, 267]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[14]: text=入院时间：2025-10-30 14:34, bbox=[90, 321, 333, 340]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[15]: text=病史陈述者：本人, bbox=[460, 310, 604, 331]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[16]: text=主诉：咳嗽、咳痰5年，加重1周, bbox=[83, 353, 332, 372]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[17]: text=现病史：5年前患者无明显诱因出现咳嗽咳痰，伴喘息气促，活动后气促症状加重，痰为脓痰，呈黄色，, bbox=[83, 367, 885, 397]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[18]: text=不易咳出，无发热、咯血、寒颤、胸闷、胸痛、腹痛、腹胀等不适，曾于外院完善相关检查诊断“支气管, bbox=[83, 393, 900, 422]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[19]: text=哮喘”，行对症支持治疗后好转，长期予以“沙罗特罗替卡松”吸入治疗。期间上述症状反复，每于上感, bbox=[83, 419, 900, 448]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[20]: text=和天气变化时加重。1周前患者感上述症状加重，偶伴头痛、胸闷、恶心、心慌等不适，今为求进一步诊治, bbox=[83, 445, 908, 475]
2026-08-05 05:00:54,050 INFO     29 [qwen-vl-text] coord item[21]: text=就诊于我院我科门诊，门诊以“支气管哮喘”收入我科。患者自病以来，精神、睡眠一般，饮食欠佳，二, bbox=[84, 472, 900, 501]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[22]: text=便如常，近1年体重减少4kg。, bbox=[84, 511, 300, 531]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[23]: text=既往史：, bbox=[85, 542, 148, 561]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[24]: text=患者过去体质一般。无高血压；无糖尿病；无心脏病；无肾病史；无肺结核；无病毒性肝炎；无其他传染, bbox=[85, 558, 897, 587]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[25]: text=病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫, bbox=[85, 585, 905, 613]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[26]: text=苗接种史不详, bbox=[86, 620, 188, 639]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[27]: text=个人史：, bbox=[86, 648, 148, 667]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[28]: text=出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长, bbox=[86, 669, 896, 693]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[29]: text=地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物, bbox=[86, 695, 896, 719]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[30]: text=质接触史。, bbox=[86, 724, 164, 743]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[31]: text=婚育史：, bbox=[86, 751, 150, 770]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[32]: text=已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。, bbox=[87, 779, 584, 801]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[33]: text=月经史：, bbox=[87, 805, 151, 824]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[34]: text=初潮年龄17岁 经期3-4天 绝经年龄53岁 月经及白带情况：正常, bbox=[88, 845, 664, 877]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[35]: text=月经周期30天, bbox=[223, 880, 333, 900]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[36]: text=家族史：父亲已故，母亲已故，具体死因不详。2个兄弟2个姐妹均体健，直系亲属无类似疾病项。患者否, bbox=[90, 906, 904, 927]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[37]: text=认二系三代有遗传病史。患者否认有遗传倾向的疾病。, bbox=[90, 932, 502, 952]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[38]: text=体格检查, bbox=[461, 960, 534, 979]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] coord item[39]: text=生命体征 体温：36.2℃ 脉搏：92次/分 呼吸：20次/分 血压：115/60, bbox=[90, 984, 688, 1000]
2026-08-05 05:00:54,051 INFO     29 [qwen-vl-text] page=0 — 40/40 coords, api_time=15.5s
2026-08-05 05:00:54,053 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1012941, prompt_len=1295
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
2026-08-05 05:01:04,170 INFO     29 [qwen-vl-text] coord API raw response (len=1978):
[
	{"text": "体格检查", "bbox": [434, 0, 505, 18]},
	{"text": "生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体", "bbox": [84, 20, 853, 52]},
	{"text": "重：44kg，腰围：cm，BMI：18.8 kg/m²", "bbox": [84, 55, 377, 85]},
	{"text": "一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常", "bbox": [84, 80, 687, 109]},
	{"text": "表情：正常体位：自主体位步态：平稳配合检查：配合", "bbox": [173, 106, 638, 133]},
	{"text": "皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无", "bbox": [84, 132, 608, 160]},
	{"text": "皮疹：无紫癜：无", "bbox": [173, 162, 331, 184]},
	{"text": "1/3", "bbox": [468, 219, 493, 236]},
	{"text": "贵州醫科大學附属醫院", "bbox": [360, 360, 723, 400]},
	{"text": "THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY", "bbox": [365, 407, 724, 422]},
	{"text": "入院记录", "bbox": [435, 440, 538, 467]},
	{"text": "姓名：", "bbox": [85, 471, 148, 491]},
	{"text": "床号：23-03床", "bbox": [257, 477, 376, 496]},
	{"text": "病历号", "bbox": [442, 476, 496, 495]},
	{"text": "科室：呼吸与危重医学科医生", "bbox": [654, 477, 907, 504]},
	{"text": "站", "bbox": [85, 500, 105, 518]},
	{"text": "水肿：无脱水现象：无松紧度：适中", "bbox": [185, 547, 500, 568]},
	{"text": "温度：适中出汗：无显性出汗瘢痕：无感染：无", "bbox": [185, 574, 608, 595]},
	{"text": "头颅：大小：正常畸形：无包块：无", "bbox": [88, 602, 448, 624]},
	{"text": "凹陷：无压痛：无", "bbox": [186, 631, 350, 652]},
	{"text": "眼：眼睑：无水肿结膜：无充血巩膜：无黄染", "bbox": [186, 660, 580, 681]},
	{"text": "眼球四个象限运动：左眼：正常右眼：正常", "bbox": [186, 687, 545, 708]},
	{"text": "眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆", "bbox": [90, 713, 659, 736]},
	{"text": "对光反射：左眼：灵敏右眼：灵敏", "bbox": [90, 741, 395, 763]},
	{"text": "鼻：外形：正常其他异常：无鼻旁窦压痛：无", "bbox": [195, 770, 595, 791]},
	{"text": "口：唇：无紫绀粘膜：无充血腮腺导管开口：正常", "bbox": [196, 798, 628, 820]},
	{"text": "舌：伸舌居中牙龈：无肿胀龋齿：无", "bbox": [196, 827, 518, 848]},
	{"text": "咽喉：扁桃体：正常咽：无充血声音：正常", "bbox": [91, 854, 514, 876]},
	{"text": "淋巴：淋巴结：全身浅表淋巴结未及肿大", "bbox": [91, 882, 462, 904]},
	{"text": "颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张", "bbox": [145, 911, 569, 932]},
	{"text": "气管：居中颈静脉回流征：无", "bbox": [187, 940, 443, 961]},
	{"text": "甲状腺：无肿大", "bbox": [187, 970, 322, 991]}
]
2026-08-05 05:01:04,170 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=10.1s
2026-08-05 05:01:04,170 INFO     29 [qwen-vl-text] coord item[0]: text=体格检查, bbox=[434, 0, 505, 18]
2026-08-05 05:01:04,170 INFO     29 [qwen-vl-text] coord item[1]: text=生命体征：体温:36.2℃，脉搏:92次/分，呼吸:20次/分，血压：115/68mmHg，身高：153cm，体, bbox=[84, 20, 853, 52]
2026-08-05 05:01:04,170 INFO     29 [qwen-vl-text] coord item[2]: text=重：44kg，腰围：cm，BMI：18.8 kg/m², bbox=[84, 55, 377, 85]
2026-08-05 05:01:04,170 INFO     29 [qwen-vl-text] coord item[3]: text=一般情况：发育：无畸形营养：良好神志：清晰呼吸：均匀面容：正常, bbox=[84, 80, 687, 109]
2026-08-05 05:01:04,170 INFO     29 [qwen-vl-text] coord item[4]: text=表情：正常体位：自主体位步态：平稳配合检查：配合, bbox=[173, 106, 638, 133]
2026-08-05 05:01:04,170 INFO     29 [qwen-vl-text] coord item[5]: text=皮肤：苍白：无潮红：无面颊潮红：无绀红：无黄色：无, bbox=[84, 132, 608, 160]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[6]: text=皮疹：无紫癜：无, bbox=[173, 162, 331, 184]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[7]: text=1/3, bbox=[468, 219, 493, 236]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[8]: text=贵州醫科大學附属醫院, bbox=[360, 360, 723, 400]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[9]: text=THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY, bbox=[365, 407, 724, 422]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[10]: text=入院记录, bbox=[435, 440, 538, 467]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[11]: text=姓名：, bbox=[85, 471, 148, 491]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[12]: text=床号：23-03床, bbox=[257, 477, 376, 496]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[13]: text=病历号, bbox=[442, 476, 496, 495]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[14]: text=科室：呼吸与危重医学科医生, bbox=[654, 477, 907, 504]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[15]: text=站, bbox=[85, 500, 105, 518]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[16]: text=水肿：无脱水现象：无松紧度：适中, bbox=[185, 547, 500, 568]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[17]: text=温度：适中出汗：无显性出汗瘢痕：无感染：无, bbox=[185, 574, 608, 595]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[18]: text=头颅：大小：正常畸形：无包块：无, bbox=[88, 602, 448, 624]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[19]: text=凹陷：无压痛：无, bbox=[186, 631, 350, 652]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[20]: text=眼：眼睑：无水肿结膜：无充血巩膜：无黄染, bbox=[186, 660, 580, 681]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[21]: text=眼球四个象限运动：左眼：正常右眼：正常, bbox=[186, 687, 545, 708]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[22]: text=眼球外形：左眼：正常右眼：正常角膜：无混浊瞳孔：等大等圆, bbox=[90, 713, 659, 736]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[23]: text=对光反射：左眼：灵敏右眼：灵敏, bbox=[90, 741, 395, 763]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[24]: text=鼻：外形：正常其他异常：无鼻旁窦压痛：无, bbox=[195, 770, 595, 791]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[25]: text=口：唇：无紫绀粘膜：无充血腮腺导管开口：正常, bbox=[196, 798, 628, 820]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[26]: text=舌：伸舌居中牙龈：无肿胀龋齿：无, bbox=[196, 827, 518, 848]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[27]: text=咽喉：扁桃体：正常咽：无充血声音：正常, bbox=[91, 854, 514, 876]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[28]: text=淋巴：淋巴结：全身浅表淋巴结未及肿大, bbox=[91, 882, 462, 904]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[29]: text=颈部：抵抗感：无颈动脉：搏动正常颈静脉：无怒张, bbox=[145, 911, 569, 932]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[30]: text=气管：居中颈静脉回流征：无, bbox=[187, 940, 443, 961]
2026-08-05 05:01:04,171 INFO     29 [qwen-vl-text] coord item[31]: text=甲状腺：无肿大, bbox=[187, 970, 322, 991]
2026-08-05 05:01:04,172 INFO     29 [qwen-vl-text] page=1 — 32/32 coords, api_time=10.1s
2026-08-05 05:01:04,176 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=886406, prompt_len=1206
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["眼球四个象限运动：左眼：正常 右眼：正常", "眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆", "对光反射：左眼：灵敏 右眼：灵敏", "鼻：外形：正常 其他异常：无 鼻旁窦压痛：无", "口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常", "舌：伸舌居中 牙龈：无肿胀 龋齿：无", "咽 喉：扁桃体：正常 咽：无充血 声音：正常", "淋巴 巴：淋巴结：全身浅表淋巴结未及肿大", "颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张", "气管：居中 颈静脉回流征：无", "甲状腺：无肿大", "胸部 部：胸廓：无畸形 乳房：", "肺 部：视诊：呼吸运动", "触诊：", "叩诊：", "听诊：", "语音传导", "心 脏：视诊：", "触诊：心尖搏动：正常 振颤：无 心包摩擦感：无", "叩诊：", "第五肋间内0.5cm", "心界", "右(cm)", "肋间", "左(cm)", "2", "2", "2", "1", "3", "(左锁骨中线距胸骨线7.5cm)", "听诊：心率：92次/分 心律：齐 心音：未闻及异常心", "额外心音：无 杂音：无 心包摩擦音：", "周围血管：异常血管征：无", "腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出", "其他异常：无", "触诊：腹壁：柔软 压痛：无", "2/3"]

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
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord API raw response (len=2136):
[
	{"text": "眼球四个象限运动：左眼：正常 右眼：正常", "bbox": [181, 0, 538, 19]},
	{"text": "眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆", "bbox": [85, 25, 649, 45]},
	{"text": "对光反射：左眼：灵敏 右眼：灵敏", "bbox": [85, 53, 384, 73]},
	{"text": "鼻：外形：正常 其他异常：无 鼻旁窦压痛：无", "bbox": [189, 80, 581, 100]},
	{"text": "口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常", "bbox": [189, 107, 616, 127]},
	{"text": "舌：伸舌居中 牙龈：无肿胀 龋齿：无", "bbox": [189, 134, 504, 154]},
	{"text": "咽 喉：扁桃体：正常 咽：无充血 声音：正常", "bbox": [85, 162, 498, 182]},
	{"text": "淋巴 巴：淋巴结：全身浅表淋巴结未及肿大", "bbox": [85, 189, 445, 209]},
	{"text": "颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张", "bbox": [85, 216, 551, 237]},
	{"text": "气管：居中 颈静脉回流征：无", "bbox": [178, 244, 423, 264]},
	{"text": "甲状腺：无肿大", "bbox": [178, 272, 302, 292]},
	{"text": "胸部 部：胸廓：无畸形 乳房：", "bbox": [85, 300, 330, 320]},
	{"text": "肺 部：视诊：呼吸运动", "bbox": [85, 328, 300, 348]},
	{"text": "触诊：", "bbox": [180, 359, 220, 377]},
	{"text": "叩诊：", "bbox": [180, 386, 220, 404]},
	{"text": "听诊：", "bbox": [180, 413, 220, 431]},
	{"text": "语音传导", "bbox": [181, 440, 250, 459]},
	{"text": "心 脏：视诊：", "bbox": [87, 467, 218, 487]},
	{"text": "触诊：心尖搏动：正常 振颤：无 心包摩擦感：无", "bbox": [181, 494, 735, 514]},
	{"text": "叩诊：", "bbox": [181, 521, 225, 540]},
	{"text": "第五肋间内0.5cm", "bbox": [420, 524, 563, 543]},
	{"text": "心界", "bbox": [397, 551, 440, 570]},
	{"text": "右(cm)", "bbox": [185, 605, 236, 624]},
	{"text": "肋间", "bbox": [371, 605, 406, 623]},
	{"text": "左(cm)", "bbox": [567, 605, 617, 624]},
	{"text": "2", "bbox": [185, 634, 195, 652]},
	{"text": "2", "bbox": [558, 634, 568, 652]},
	{"text": "2", "bbox": [185, 662, 195, 680]},
	{"text": "1", "bbox": [558, 662, 568, 680]},
	{"text": "3", "bbox": [185, 690, 195, 708]},
	{"text": "(左锁骨中线距胸骨线7.5cm)", "bbox": [267, 738, 482, 758]},
	{"text": "听诊：心率：92次/分 心律：齐 心音：未闻及异常心", "bbox": [166, 766, 617, 787]},
	{"text": "额外心音：无 杂音：无 心包摩擦音：", "bbox": [166, 793, 604, 814]},
	{"text": "周围血管：异常血管征：无", "bbox": [91, 823, 306, 844]},
	{"text": "腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出", "bbox": [91, 850, 549, 870]},
	{"text": "其他异常：无", "bbox": [178, 878, 282, 898]},
	{"text": "触诊：腹壁：柔软 压痛：无", "bbox": [178, 905, 416, 925]},
	{"text": "2/3", "bbox": [487, 948, 513, 965]}
]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=13.8s
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[0]: text=眼球四个象限运动：左眼：正常 右眼：正常, bbox=[181, 0, 538, 19]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[1]: text=眼球外形：左眼：正常 右眼：正常 角膜：无混浊 瞳孔：等大等圆, bbox=[85, 25, 649, 45]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[2]: text=对光反射：左眼：灵敏 右眼：灵敏, bbox=[85, 53, 384, 73]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[3]: text=鼻：外形：正常 其他异常：无 鼻旁窦压痛：无, bbox=[189, 80, 581, 100]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[4]: text=口：唇：无紫绀 粘膜：无充血 腮腺导管开口：正常, bbox=[189, 107, 616, 127]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[5]: text=舌：伸舌居中 牙龈：无肿胀 龋齿：无, bbox=[189, 134, 504, 154]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[6]: text=咽 喉：扁桃体：正常 咽：无充血 声音：正常, bbox=[85, 162, 498, 182]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[7]: text=淋巴 巴：淋巴结：全身浅表淋巴结未及肿大, bbox=[85, 189, 445, 209]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[8]: text=颈 部：抵抗感：无 颈动脉：搏动正常 颈静脉：无怒张, bbox=[85, 216, 551, 237]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[9]: text=气管：居中 颈静脉回流征：无, bbox=[178, 244, 423, 264]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[10]: text=甲状腺：无肿大, bbox=[178, 272, 302, 292]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[11]: text=胸部 部：胸廓：无畸形 乳房：, bbox=[85, 300, 330, 320]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[12]: text=肺 部：视诊：呼吸运动, bbox=[85, 328, 300, 348]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[13]: text=触诊：, bbox=[180, 359, 220, 377]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[14]: text=叩诊：, bbox=[180, 386, 220, 404]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[15]: text=听诊：, bbox=[180, 413, 220, 431]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[16]: text=语音传导, bbox=[181, 440, 250, 459]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[17]: text=心 脏：视诊：, bbox=[87, 467, 218, 487]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[18]: text=触诊：心尖搏动：正常 振颤：无 心包摩擦感：无, bbox=[181, 494, 735, 514]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[19]: text=叩诊：, bbox=[181, 521, 225, 540]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[20]: text=第五肋间内0.5cm, bbox=[420, 524, 563, 543]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[21]: text=心界, bbox=[397, 551, 440, 570]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[22]: text=右(cm), bbox=[185, 605, 236, 624]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[23]: text=肋间, bbox=[371, 605, 406, 623]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[24]: text=左(cm), bbox=[567, 605, 617, 624]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[25]: text=2, bbox=[185, 634, 195, 652]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[26]: text=2, bbox=[558, 634, 568, 652]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[27]: text=2, bbox=[185, 662, 195, 680]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[28]: text=1, bbox=[558, 662, 568, 680]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[29]: text=3, bbox=[185, 690, 195, 708]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[30]: text=(左锁骨中线距胸骨线7.5cm), bbox=[267, 738, 482, 758]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[31]: text=听诊：心率：92次/分 心律：齐 心音：未闻及异常心, bbox=[166, 766, 617, 787]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[32]: text=额外心音：无 杂音：无 心包摩擦音：, bbox=[166, 793, 604, 814]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[33]: text=周围血管：异常血管征：无, bbox=[91, 823, 306, 844]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[34]: text=腹部 部：视诊：外形：平坦 腹式呼吸：存在 脐：无突出, bbox=[91, 850, 549, 870]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[35]: text=其他异常：无, bbox=[178, 878, 282, 898]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[36]: text=触诊：腹壁：柔软 压痛：无, bbox=[178, 905, 416, 925]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] coord item[37]: text=2/3, bbox=[487, 948, 513, 965]
2026-08-05 05:01:18,004 INFO     29 [qwen-vl-text] page=2 — 38/38 coords, api_time=13.8s
2026-08-05 05:01:18,005 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=707672, prompt_len=1100
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["站", "反跳痛：无", "液波振颤：无 振水声：无", "腹部包块：无", "肝：肋下未及", "胆囊：未触及 Murphy征：阴性", "脾：未触及", "叩诊：肝浊音界：正常 移动性浊音：无", "肾区叩痛：无", "听诊：肠鸣音：正常 肠鸣音频率：4次/分", "气过水音：无 血管杂音：无", "肛门直肠：未检", "生殖器：未检", "脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限", "压痛，叩痛：无", "杵状指趾：无", "神经系统：腹壁反射：正常 肢体瘫痪：无", "肌张力：正常 肌力：V级", "肱二头肌反射：正常 Hoffman征：阴性", "膝腱反射：正常 Kernig征：阴性", "跟腱反射：正常Babinski征：阴性", "其他：无", "补充及专科情况", "双肺呼吸音清，未闻及干湿性啰音。", "辅助检查：暂无", "VTE评估：", "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "入院诊断：1.支气管哮喘急性发作期", "医师签名：", "日期：2025-10-30 16:38"]

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
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord API raw response (len=1701):
[
	{"text": "站", "bbox": [90, 0, 108, 14]},
	{"text": "反跳痛：无", "bbox": [176, 40, 266, 58]},
	{"text": "液波振颤：无 振水声：无", "bbox": [176, 66, 383, 85]},
	{"text": "腹部包块：无", "bbox": [176, 95, 283, 113]},
	{"text": "肝：肋下未及", "bbox": [176, 122, 283, 141]},
	{"text": "胆囊：未触及 Murphy征：阴性", "bbox": [176, 148, 419, 168]},
	{"text": "脾：未触及", "bbox": [176, 177, 264, 195]},
	{"text": "叩诊：肝浊音界：正常 移动性浊音：无", "bbox": [176, 203, 491, 222]},
	{"text": "肾区叩痛：无", "bbox": [176, 232, 283, 251]},
	{"text": "听诊：肠鸣音：正常 肠鸣音频率：4次/分", "bbox": [176, 258, 517, 278]},
	{"text": "气过水音：无 血管杂音：无", "bbox": [176, 287, 419, 307]},
	{"text": "肛门直肠：未检", "bbox": [90, 318, 216, 338]},
	{"text": "生殖器：未检", "bbox": [90, 347, 216, 366]},
	{"text": "脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限", "bbox": [90, 369, 505, 393]},
	{"text": "压痛，叩痛：无", "bbox": [183, 399, 308, 418]},
	{"text": "杵状指趾：无", "bbox": [90, 427, 199, 448]},
	{"text": "神经系统：腹壁反射：正常 肢体瘫痪：无", "bbox": [90, 453, 440, 474]},
	{"text": "肌张力：正常 肌力：V级", "bbox": [183, 480, 423, 500]},
	{"text": "肱二头肌反射：正常 Hoffman征：阴性", "bbox": [183, 507, 487, 527]},
	{"text": "膝腱反射：正常 Kernig征：阴性", "bbox": [183, 534, 442, 554]},
	{"text": "跟腱反射：正常Babinski征：阴性", "bbox": [183, 561, 450, 581]},
	{"text": "其他：无", "bbox": [90, 590, 195, 612]},
	{"text": "补充及专科情况", "bbox": [431, 643, 565, 663]},
	{"text": "双肺呼吸音清，未闻及干湿性啰音。", "bbox": [120, 672, 395, 692]},
	{"text": "辅助检查：暂无", "bbox": [87, 703, 214, 722]},
	{"text": "VTE评估：", "bbox": [87, 758, 158, 777]},
	{"text": "Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：", "bbox": [87, 777, 698, 801]},
	{"text": "入院诊断：1.支气管哮喘急性发作期", "bbox": [87, 837, 364, 859]},
	{"text": "医师签名：", "bbox": [700, 928, 780, 948]},
	{"text": "日期：2025-10-30 16:38", "bbox": [721, 972, 920, 990]}
]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=8.8s
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[0]: text=站, bbox=[90, 0, 108, 14]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[1]: text=反跳痛：无, bbox=[176, 40, 266, 58]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[2]: text=液波振颤：无 振水声：无, bbox=[176, 66, 383, 85]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[3]: text=腹部包块：无, bbox=[176, 95, 283, 113]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[4]: text=肝：肋下未及, bbox=[176, 122, 283, 141]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[5]: text=胆囊：未触及 Murphy征：阴性, bbox=[176, 148, 419, 168]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[6]: text=脾：未触及, bbox=[176, 177, 264, 195]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[7]: text=叩诊：肝浊音界：正常 移动性浊音：无, bbox=[176, 203, 491, 222]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[8]: text=肾区叩痛：无, bbox=[176, 232, 283, 251]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[9]: text=听诊：肠鸣音：正常 肠鸣音频率：4次/分, bbox=[176, 258, 517, 278]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[10]: text=气过水音：无 血管杂音：无, bbox=[176, 287, 419, 307]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[11]: text=肛门直肠：未检, bbox=[90, 318, 216, 338]
2026-08-05 05:01:26,830 INFO     29 [qwen-vl-text] coord item[12]: text=生殖器：未检, bbox=[90, 347, 216, 366]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[13]: text=脊柱四肢：脊柱：无畸形 四肢：正常 活动：不受限, bbox=[90, 369, 505, 393]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[14]: text=压痛，叩痛：无, bbox=[183, 399, 308, 418]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[15]: text=杵状指趾：无, bbox=[90, 427, 199, 448]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[16]: text=神经系统：腹壁反射：正常 肢体瘫痪：无, bbox=[90, 453, 440, 474]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[17]: text=肌张力：正常 肌力：V级, bbox=[183, 480, 423, 500]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[18]: text=肱二头肌反射：正常 Hoffman征：阴性, bbox=[183, 507, 487, 527]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[19]: text=膝腱反射：正常 Kernig征：阴性, bbox=[183, 534, 442, 554]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[20]: text=跟腱反射：正常Babinski征：阴性, bbox=[183, 561, 450, 581]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[21]: text=其他：无, bbox=[90, 590, 195, 612]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[22]: text=补充及专科情况, bbox=[431, 643, 565, 663]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[23]: text=双肺呼吸音清，未闻及干湿性啰音。, bbox=[120, 672, 395, 692]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[24]: text=辅助检查：暂无, bbox=[87, 703, 214, 722]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[25]: text=VTE评估：, bbox=[87, 758, 158, 777]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[26]: text=Padua评分：评估结果：低危，评估分数：1分，评估内容：高龄（≥70周岁）：, bbox=[87, 777, 698, 801]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[27]: text=入院诊断：1.支气管哮喘急性发作期, bbox=[87, 837, 364, 859]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[28]: text=医师签名：, bbox=[700, 928, 780, 948]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] coord item[29]: text=日期：2025-10-30 16:38, bbox=[721, 972, 920, 990]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] page=3 — 30/30 coords, api_time=8.8s
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] new_positions (140):
[[0, 260.1, 329.256, 0.0, 15.038255859374999], [0, 47.124, 72.216, 23.183977783203126, 35.089263671875], [0, 147.492, 219.708, 23.183977783203126, 34.462669677734375], [0, 264.384, 318.24, 21.930789794921875, 33.20948168945313], [0, 400.86, 547.74, 21.30419580078125, 31.956293701171877], [0, 47.124, 57.528, 40.102015625, 50.75411352539062], [0, 53.856, 98.532, 89.60294116210937, 101.50822705078124], [0, 279.072, 358.02, 85.84337719726562, 97.7486630859375], [0, 53.856, 133.416, 112.7869189453125, 125.318798828125], [0, 279.072, 413.712, 108.40076098632812, 120.93264086914063], [0, 53.856, 156.06, 137.8506787109375, 150.38255859375], [0, 280.296, 369.64799999999997, 132.21133276367186, 144.74321264648438], [0, 53.856, 135.864, 161.66125048828124, 174.19313037109376], [0, 280.908, 434.52, 154.76871655273436, 167.30059643554688], [0, 55.08, 203.796, 201.13667211914063, 213.0419580078125], [0, 281.52, 369.64799999999997, 194.24413818359375, 207.4026120605469], [0, 50.796, 203.184, 221.18767993164062, 233.0929658203125], [0, 50.796, 541.62, 229.95999584960938, 248.75781567382813], [0, 50.796, 550.8, 246.25143969726562, 264.4226655273437], [0, 50.796, 550.8, 262.5428835449219, 280.714109375], [0, 50.796, 555.696, 278.83432739257813, 297.63214721679685], [0, 51.408, 550.8, 295.752365234375, 313.92359106445315], [0, 51.408, 183.6, 320.18953100585935, 332.72141088867187], [0, 52.019999999999996, 90.576, 339.6139448242188, 351.51923071289065], [0, 52.019999999999996, 548.9639999999999, 349.63944873046876, 367.8106745605469], [0, 52.019999999999996, 553.86, 366.55748657226565, 384.1021184082031], [0, 52.632, 115.056, 388.4882763671875, 400.39356225585936], [0, 52.632, 90.576, 406.032908203125, 417.9381940917969], [0, 52.632, 548.352, 419.19138208007814, 434.22963793945314], [0, 52.632, 548.352, 435.4828259277344, 450.5210817871094], [0, 52.632, 100.368, 453.6540517578125, 465.5593376464844], [0, 52.632, 91.8, 470.5720895996094, 482.47737548828127], [0, 53.244, 357.408, 488.1167214355469, 501.90178930664064], [0, 53.244, 92.41199999999999, 504.4081652832031, 516.313451171875], [0, 53.856, 406.368, 529.4719250488281, 549.5229328613282], [0, 136.476, 203.796, 551.40271484375, 563.9345947265625], [0, 55.08, 553.2479999999999, 567.6941586914063, 580.8526325683594], [0, 55.08, 307.224, 583.9856025390625, 596.517482421875], [0, 282.132, 326.808, 601.530234375, 613.4355202636718], [0, 55.08, 421.056, 616.568490234375, 626.593994140625], [1, 265.608, 309.06, 0.0, 11.161241455078123], [1, 51.408, 522.036, 12.401379394531249, 32.243586425781245], [1, 51.408, 230.724, 34.10379333496093, 52.70586242675781], [1, 51.408, 420.444, 49.605517578124996, 67.5875177001953], [1, 105.876, 390.456, 65.72731079101563, 82.46917297363281], [1, 51.408, 372.096, 81.84910400390625, 99.21103515624999], [1, 105.876, 202.572, 100.45117309570311, 114.0926904296875], [1, 286.416, 301.716, 135.79510437011717, 146.33627685546872], [1, 220.32, 442.476, 223.22482910156248, 248.02758789062497], [1, 223.38, 443.08799999999997, 252.36807067871092, 261.6691052246093], [1, 266.21999999999997, 329.256, 272.83034667968747, 289.57220886230465], [1, 52.019999999999996, 90.576, 292.0524847412109, 304.45386413574215], [1, 157.284, 230.112, 295.7728985595703, 307.55420898437495], [1, 270.504, 303.552, 295.15282958984375, 306.9341400146484], [1, 400.248, 555.084, 295.7728985595703, 312.5147607421875], [1, 52.019999999999996, 64.26, 310.03448486328125, 321.19572631835933], [1, 113.22, 306.0, 339.17772644042964, 352.19917480468746], [1, 113.22, 372.096, 355.9195886230468, 368.94103698730464], [1, 53.856, 274.176, 373.2815197753906, 386.92303710937495], [1, 113.832, 214.2, 391.2635198974609, 404.2849682617187], [1, 113.832, 354.96, 409.2455200195312, 422.26696838378905], [1, 113.832, 333.54, 425.9873822021484, 439.00883056640623], [1, 55.08, 403.308, 442.10917541503903, 456.37076171875], [1, 55.08, 241.74, 459.4711065673828, 473.11262390136716], [1, 119.34, 364.14, 477.4531066894531, 490.4745550537109], [1, 119.952, 384.336, 494.8150378417968, 508.4565551757812], [1, 119.952, 317.016, 512.7970379638672, 525.818486328125], [1, 55.692, 314.568, 529.5389001464844, 543.1804174804687], [1, 55.692, 282.74399999999997, 546.900831298828, 560.5423486328125], [1, 88.74, 348.228, 564.8828314208984, 577.9042797851562], [1, 114.444, 271.116, 582.8648315429687, 595.8862799072265], [1, 114.444, 197.064, 601.4669006347656, 614.4883489990234], [2, 110.77199999999999, 329.256, 0.0, 11.75028466796875], [2, 52.019999999999996, 397.188, 15.46090087890625, 27.82962158203125], [2, 52.019999999999996, 235.00799999999998, 32.777109863281254, 45.145830566406254], [2, 115.66799999999999, 355.572, 49.4748828125, 61.843603515625], [2, 115.66799999999999, 376.992, 66.17265576171874, 78.54137646484375], [2, 115.66799999999999, 308.448, 82.8704287109375, 95.2391494140625], [2, 52.019999999999996, 304.776, 100.1866376953125, 112.5553583984375], [2, 52.019999999999996, 272.34, 116.88441064453126, 129.25313134765625], [2, 52.019999999999996, 337.212, 133.58218359375, 146.56934033203126], [2, 108.93599999999999, 258.876, 150.898392578125, 163.26711328125], [2, 108.93599999999999, 184.82399999999998, 168.2146015625, 180.58332226562501], [2, 52.019999999999996, 201.96, 185.530810546875, 197.89953125], [2, 52.019999999999996, 183.6, 202.84701953125, 215.215740234375], [2, 110.16, 134.64, 222.01853662109374, 233.15038525390625], [2, 110.16, 134.64, 238.7163095703125, 249.848158203125], [2, 110.16, 134.64, 255.41408251953126, 266.54593115234377], [2, 110.77199999999999, 153.0, 272.11185546875, 283.8621401367188], [2, 53.244, 133.416, 288.8096284179688, 301.17834912109373], [2, 110.77199999999999, 449.82, 305.5074013671875, 317.8761220703125], [2, 110.77199999999999, 137.7, 322.20517431640627, 333.955458984375], [2, 257.04, 344.556, 324.060482421875, 335.81076708984375], [2, 242.964, 269.28, 340.75825537109375, 352.5085400390625], [2, 113.22, 144.432, 374.15380126953124, 385.9040859375], [2, 227.052, 248.472, 374.15380126953124, 385.2856499023438], [2, 347.004, 377.604, 374.15380126953124, 385.9040859375], [2, 113.22, 119.34, 392.0884462890625, 403.220294921875], [2, 341.496, 347.616, 392.0884462890625, 403.220294921875], [2, 113.22, 119.34, 409.4046552734375, 420.53650390625], [2, 341.496, 347.616, 409.4046552734375, 420.53650390625], [2, 113.22, 119.34, 426.7208642578125, 437.852712890625], [2, 163.404, 294.984, 456.4057939453125, 468.7745146484375], [2, 101.592, 377.604, 473.7220029296875, 486.7091596679688], [2, 101.592, 369.64799999999997, 490.41977587890625, 503.4069326171875], [2, 55.692, 187.272, 508.97285693359373, 521.960013671875], [2, 55.692, 335.988, 525.6706298828125, 538.0393505859375], [2, 108.93599999999999, 172.584, 542.9868388671875, 555.3555595703125], [2, 108.93599999999999, 254.59199999999998, 559.6846118164062, 572.0533325195313], [2, 298.044, 313.956, 586.277361328125, 596.7907739257813], [3, 55.08, 66.096, 0.0, 8.791776123046875], [3, 107.712, 162.792, 25.1193603515625, 36.423072509765625], [3, 107.712, 234.396, 41.446944580078124, 53.37864074707031], [3, 107.712, 173.196, 59.65848083496093, 70.96219299316405], [3, 107.712, 173.196, 76.61404907226562, 88.54574523925781], [3, 107.712, 256.428, 92.94163330078125, 105.5013134765625], [3, 107.712, 161.56799999999998, 111.15316955566405, 122.45688171386718], [3, 107.712, 300.492, 127.48075378417968, 139.41244995117188], [3, 107.712, 173.196, 145.6922900390625, 157.62398620605467], [3, 107.712, 316.404, 162.0198742675781, 174.57955444335937], [3, 107.712, 256.428, 180.23141052246092, 192.7910906982422], [3, 55.08, 132.192, 199.69891479492188, 212.25859497070311], [3, 55.08, 132.192, 217.91045104980466, 229.84214721679686], [3, 55.08, 309.06, 231.72609924316404, 246.79771545410154], [3, 111.996, 188.496, 250.56561950683593, 262.4973156738281], [3, 55.08, 121.788, 268.14917175292965, 281.3368359375], [3, 55.08, 269.28, 284.4767559814453, 297.6644201660156], [3, 111.996, 258.876, 301.43232421874995, 313.99200439453125], [3, 111.996, 298.044, 318.38789245605466, 330.9475726318359], [3, 111.996, 270.504, 335.34346069335936, 347.9031408691406], [3, 111.996, 275.4, 352.29902893066406, 364.8587091064453], [3, 55.08, 119.34, 370.51056518554685, 384.32621337890623], [3, 263.772, 345.78, 403.79371765136716, 416.3533978271484], [3, 73.44, 241.74, 422.00525390625, 434.56493408203124], [3, 53.244, 130.968, 441.47275817871093, 453.4044543457031], [3, 53.244, 96.696, 476.0118786621093, 487.9435748291015], [3, 53.244, 427.176, 487.9435748291015, 503.01519104003904], [3, 53.244, 222.768, 525.6226153564453, 539.4382635498047], [3, 428.4, 477.36, 582.76916015625, 595.3288403320312], [3, 441.252, 563.04, 610.4004565429688, 621.7041687011719]]
2026-08-05 05:01:26,831 INFO     29 [qwen-vl-text] ═══ DONE ═══ 140 positions, pages=4, time=61.4s
2026-08-05 05:01:26,844 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 05:01:26,845 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 05:01:26,845 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 05:01:26,845 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:01:26.845+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:01:26,851 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:01:26,851 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:01:26,851 INFO     29 [qwen-vl-text] positions(201): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:01:26,852 INFO     29 [qwen-vl-text] page grouping: [7, 8], lines per page: [173, 22]
2026-08-05 05:01:27,130 INFO     29 [qwen-vl-text] page=7, rect=612x832, img=(1700x2312), dpi=200
2026-08-05 05:01:27,389 INFO     29 [qwen-vl-text] page=8, rect=612x818, img=(1700x2273), dpi=200
2026-08-05 05:01:27,391 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2149
2026-08-05 05:01:27,392 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:01:27,392 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 241, \"bbox_end\": 441, \"encounter_dates\": [\"2025-10-31\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能通气阻力检查报告\n姓名：\n性别：女\n身高：151 cm\n病历号：\n年龄：72 Years\n体重：46 kg\nFlow [L/s]\nF/V ex\n10\n5\n0\n2\n4\n6\nF/V in\n8\nVol [L]\n6\n4\n1\nVol%Vcmax\n100\nVcmax\n20\n0\nTime [s]\n0\n1\n2\n3\n4\n5\n6\n2.0\nR [kPa/(L/s)] Normal breathingX [kPa/(L/s)]\n1.5\n1.0\n1.0\n0.5\n0.0\n0.4\n0.2\n0.2\n0.4\nF [Hz]\n5\n10\n15\n20\n25\n30\n35\n日期\n时间\n预计值\n实测值\n实/预\n25/10/31\n14:29:33\nMV\n[L/min]\n6.57\n11.52\n175.3\nVT\n[L]\n0.33\n0.79\n239.6\nBF\n[1/min]\n20.00\n14.63\n73.1\nVC MAX\n[L]\n2.03\n1.48\n73.0\nERV\n[L]\n0.57\n0.14\n25.5\nIC\n[L]\n1.46\n1.34\n91.6\nFVC\n[L]\n1.93\n1.44\n74.8\nFEV 1\n[L]\n1.56\n0.91\n58.4\nFEV 1 % FVC\n[%]\n63.38\nFEV 1 % VC MAX\n[%]\n75.42\n61.67\n81.8\nPEF\n[L/s]\n5.04\n2.51\n49.8\nMEF 75\n[L/s]\n4.66\n1.54\n33.1\nMEF 50\n[L/s]\n3.06\n0.56\n18.2\nMEF 25\n[L/s]\n0.90\n0.22\n24.6\nMEF 75/25\n[L/s]\n2.36\n0.50\n21.1\nFET\n[s]\n4.91\nLFV\n[L/min]\n73.10\nZ at 5 Hz\n[kPa/(L/s)]\n0.43\n0.58\n135.7\nResonant frequency\n[1/s]\n30.00\nR at 5 Hz\n[kPa/(L/s)]\n0.41\n0.57\n137.2\nR nt 20 Hz\n[kPa/(L/s)]\n0.35\n0.34\n95.3\nR at 5 Hz\n[kPa/(L/s)]\n-0.11\n-0.12\n112.5\nRcentral\n[kPa/(L/s)]\n0.12\nRperipheral\n[kPa/(L/s)]\n0.40\n结论：\n1.中重度混合性肺通气功能障碍\n2.（阻力增加\n审核者专用章\n检查者：王美锦\n报告时间: 2025-04-05\n\\multicolumn{1}{c}{} \\multicolumn{1}{c}{预计值} \\multicolumn{1}{c}{前次} \\multicolumn{1}{c}{前/预} \\multicolumn{1}{c}{后次} \\multicolumn{1}{c}{后/预} \\multicolumn{1}{c}{改善率}\n\\multicolumn{1}{c}{日期} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{25/10/31} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{25/10/31} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{}\n\\multicolumn{1}{c}{时间} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{14:29:33} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{14:53:10} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{}\nVT [L] 0.33 0.79 239.6\nBF [1/min] 20.00 14.63 73.1\nMV [L/min] 6.57 11.52 175.3\nVC MAX [L] 2.03 1.48 73.0 1.66 81.9 12.2\nERV [L] 0.57 0.14 25.5\nIC [L] 1.46 1.34 91.6\nFVC [L] 1.93 1.44 74.8 1.66 86.2 15.3\nFEV 1 [L] 1.56 0.91 58.4 1.08 68.8 17.8\nFEV 1 % FVC [%] 63.38 64.76 2.2\nFEV 1 % VC MAX [%] 75.42 61.67 81.8 64.76 85.9 5.0\nPEF [L/s] 5.04 2.51 49.8 3.35 66.5 33.6\nMEF 75 [L/s] 4.66 1.54 33.1 1.72 36.8 11.3\nMEF 50 [L/s] 3.06 0.56 18.2 0.83 27.1 49.1\nMEF 25 [L/s] 0.90 0.22 24.6 0.36 39.8 62.1\nMMEF 75/25 [L/s] 2.36 0.50 21.1 0.47 20.0 -4.9\nFET [s] 4.91 4.88 -0.6\nV backextrapol. % FVC [%] 3.85 4.39 13.9\nMVV [L/min] 73.10",
    "role": "user"
  }
]
[92m05:01:27 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:01:27,393 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:01:45,111 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:01:45,111 INFO     29 [qwen-vl-text] LLM output (len=2464):
{
  "exam_date": "2025-10-31",
  "report_date": "2025-04-05",
  "exam_name": "肺功能通气阻力检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | 单位 | 预计值 | 实测值 | 实/预(%) |\n|---|---|---|---|---|\n| MV | L/min | 6.57 | 11.52 | 175.3 |\n| VT | L | 0.33 | 0.79 | 239.6 |\n| BF | 1/min | 20.00 | 14.63 | 73.1 |\n| VC MAX | L | 2.03 | 1.48 | 73.0 |\n| ERV | L | 0.57 | 0.14 | 25.5 |\n| IC | L | 1.46 | 1.34 | 91.6 |\n| FVC | L | 1.93 | 1.44 | 74.8 |\n| FEV 1 | L | 1.56 | 0.91 | 58.4 |\n| FEV 1 % FVC | % | - | 63.38 | - |\n| FEV 1 % VC MAX | % | 75.42 | 61.67 | 81.8 |\n| PEF | L/s | 5.04 | 2.51 | 49.8 |\n| MEF 75 | L/s | 4.66 | 1.54 | 33.1 |\n| MEF 50 | L/s | 3.06 | 0.56 | 18.2 |\n| MEF 25 | L/s | 0.90 | 0.22 | 24.6 |\n| MEF 75/25 | L/s | 2.36 | 0.50 | 21.1 |\n| FET | s | - | 4.91 | - |\n| LFV | L/min | - | 73.10 | - |\n| Z at 5 Hz | kPa/(L/s) | 0.43 | 0.58 | 135.7 |\n| Resonant frequency | 1/s | - | 30.00 | - |\n| R at 5 Hz | kPa/(L/s) | 0.41 | 0.57 | 137.2 |\n| R nt 20 Hz | kPa/(L/s) | 0.35 | 0.34 | 95.3 |\n| R at 5 Hz | kPa/(L/s) | -0.11 | -0.12 | 112.5 |\n| Rcentral | kPa/(L/s) | - | 0.12 | - |\n| Rperipheral | kPa/(L/s) | - | 0.40 | - |",
  "conclusion": "1.中重度混合性肺通气功能障碍\n2.（阻力增加\n\n| 指标 | 单位 | 预计值 | 前次(25/10/31 14:29:33) | 前/预(%) | 后次(25/10/31 14:53:10) | 后/预(%) | 改善率(%) |\n|---|---|---|---|---|---|---|---|\n| VT | L | 0.33 | 0.79 | 239.6 | - | - | - |\n| BF | 1/min | 20.00 | 14.63 | 73.1 | - | - | - |\n| MV | L/min | 6.57 | 11.52 | 175.3 | - | - | - |\n| VC MAX | L | 2.03 | 1.48 | 73.0 | 1.66 | 81.9 | 12.2 |\n| ERV | L | 0.57 | 0.14 | 25.5 | - | - | - |\n| IC | L | 1.46 | 1.34 | 91.6 | - | - | - |\n| FVC | L | 1.93 | 1.44 | 74.8 | 1.66 | 86.2 | 15.3 |\n| FEV 1 | L | 1.56 | 0.91 | 58.4 | 1.08 | 68.8 | 17.8 |\n| FEV 1 % FVC | % | - | 63.38 | - | 64.76 | - | 2.2 |\n| FEV 1 % VC MAX | % | 75.42 | 61.67 | 81.8 | 64.76 | 85.9 | 5.0 |\n| PEF | L/s | 5.04 | 2.51 | 49.8 | 3.35 | 66.5 | 33.6 |\n| MEF 75 | L/s | 4.66 | 1.54 | 33.1 | 1.72 | 36.8 | 11.3 |\n| MEF 50 | L/s | 3.06 | 0.56 | 18.2 | 0.83 | 27.1 | 49.1 |\n| MEF 25 | L/s | 0.90 | 0.22 | 24.6 | 0.36 | 39.8 | 62.1 |\n| MMEF 75/25 | L/s | 2.36 | 0.50 | 21.1 | 0.47 | 20.0 | -4.9 |\n| FET | s | - | 4.91 | - | 4.88 | - | -0.6 |\n| V backextrapol. % FVC | % | - | 3.85 | - | 4.39 | - | 13.9 |\n| MVV | L/min | - | 73.10 | - | - | - | - |",
  "physician": "王美锦",
  "reviewer": null
}
2026-08-05 05:01:45,113 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1024867, prompt_len=2148
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共173行）
["肺功能通气阻力检查报告", "姓名：", "性别：女", "身高：151 cm", "病历号：", "年龄：72 Years", "体重：46 kg", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "F/V in", "8", "Vol [L]", "6", "4", "1", "Vol%Vcmax", "100", "Vcmax", "20", "0", "Time [s]", "0", "1", "2", "3", "4", "5", "6", "2.0", "R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]", "1.5", "1.0", "1.0", "0.5", "0.0", "0.4", "0.2", "0.2", "0.4", "F [Hz]", "5", "10", "15", "20", "25", "30", "35", "日期", "时间", "预计值", "实测值", "实/预", "25/10/31", "14:29:33", "MV", "[L/min]", "6.57", "11.52", "175.3", "VT", "[L]", "0.33", "0.79", "239.6", "BF", "[1/min]", "20.00", "14.63", "73.1", "VC MAX", "[L]", "2.03", "1.48", "73.0", "ERV", "[L]", "0.57", "0.14", "25.5", "IC", "[L]", "1.46", "1.34", "91.6", "FVC", "[L]", "1.93", "1.44", "74.8", "FEV 1", "[L]", "1.56", "0.91", "58.4", "FEV 1 % FVC", "[%]", "63.38", "FEV 1 % VC MAX", "[%]", "75.42", "61.67", "81.8", "PEF", "[L/s]", "5.04", "2.51", "49.8", "MEF 75", "[L/s]", "4.66", "1.54", "33.1", "MEF 50", "[L/s]", "3.06", "0.56", "18.2", "MEF 25", "[L/s]", "0.90", "0.22", "24.6", "MEF 75/25", "[L/s]", "2.36", "0.50", "21.1", "FET", "[s]", "4.91", "LFV", "[L/min]", "73.10", "Z at 5 Hz", "[kPa/(L/s)]", "0.43", "0.58", "135.7", "Resonant frequency", "[1/s]", "30.00", "R at 5 Hz", "[kPa/(L/s)]", "0.41", "0.57", "137.2", "R nt 20 Hz", "[kPa/(L/s)]", "0.35", "0.34", "95.3", "R at 5 Hz", "[kPa/(L/s)]", "-0.11", "-0.12", "112.5", "Rcentral", "[kPa/(L/s)]", "0.12", "Rperipheral", "[kPa/(L/s)]", "0.40", "结论：", "1.中重度混合性肺通气功能障碍", "2.（阻力增加", "审核者专用章", "检查者：王美锦"]

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
2026-08-05 05:02:28,025 INFO     29 [qwen-vl-text] coord API raw response (len=8389):
[
	{"text": "肺功能通气阻力检查报告", "bbox": [375, 88, 634, 107]},
	{"text": "姓名：", "bbox": [154, 112, 202, 125]},
	{"text": "性别：女", "bbox": [154, 125, 347, 138]},
	{"text": "身高：151 cm", "bbox": [154, 138, 387, 149]},
	{"text": "病历号：", "bbox": [505, 110, 570, 123]},
	{"text": "年龄：72 Years", "bbox": [678, 121, 754, 133]},
	{"text": "体重：46 kg", "bbox": [678, 134, 725, 146]},
	{"text": "Flow [L/s]", "bbox": [121, 165, 173, 175]},
	{"text": "F/V ex", "bbox": [257, 165, 291, 173]},
	{"text": "10", "bbox": [102, 178, 115, 188]},
	{"text": "5", "bbox": [107, 199, 115, 208]},
	{"text": "0", "bbox": [107, 220, 115, 229]},
	{"text": "2", "bbox": [173, 230, 181, 238]},
	{"text": "4", "bbox": [231, 230, 240, 238]},
	{"text": "6", "bbox": [290, 230, 298, 238]},
	{"text": "F/V in", "bbox": [259, 274, 290, 283]},
	{"text": "8", "bbox": [408, 168, 416, 177]},
	{"text": "Vol [L]", "bbox": [422, 170, 457, 181]},
	{"text": "6", "bbox": [408, 193, 416, 201]},
	{"text": "4", "bbox": [408, 220, 416, 228]},
	{"text": "1", "bbox": [623, 218, 633, 227]},
	{"text": "Vol%Vcmax", "bbox": [375, 243, 438, 252]},
	{"text": "100", "bbox": [380, 254, 400, 264]},
	{"text": "Vcmax", "bbox": [435, 257, 472, 266]},
	{"text": "20", "bbox": [387, 266, 398, 275]},
	{"text": "0", "bbox": [408, 272, 416, 280]},
	{"text": "Time [s]", "bbox": [505, 262, 546, 272]},
	{"text": "0", "bbox": [417, 283, 425, 291]},
	{"text": "1", "bbox": [453, 283, 460, 291]},
	{"text": "2", "bbox": [487, 283, 495, 291]},
	{"text": "3", "bbox": [521, 283, 529, 291]},
	{"text": "4", "bbox": [555, 283, 563, 291]},
	{"text": "5", "bbox": [590, 283, 597, 291]},
	{"text": "6", "bbox": [623, 283, 631, 291]},
	{"text": "2.0", "bbox": [654, 161, 673, 170]},
	{"text": "R [kPa/(L/s)] Normal breathingX [kPa/(L/s)]", "bbox": [678, 163, 887, 175]},
	{"text": "1.5", "bbox": [654, 187, 673, 196]},
	{"text": "1.0", "bbox": [654, 215, 673, 224]},
	{"text": "0.5", "bbox": [654, 243, 673, 252]},
	{"text": "0.0", "bbox": [654, 271, 673, 280]},
	{"text": "F [Hz]", "bbox": [767, 261, 797, 271]},
	{"text": "5", "bbox": [673, 281, 681, 290]},
	{"text": "10", "bbox": [705, 281, 718, 290]},
	{"text": "15", "bbox": [739, 281, 751, 290]},
	{"text": "20", "bbox": [772, 281, 785, 290]},
	{"text": "25", "bbox": [808, 281, 822, 290]},
	{"text": "30", "bbox": [838, 281, 851, 290]},
	{"text": "35", "bbox": [872, 281, 885, 290]},
	{"text": "日期", "bbox": [105, 308, 142, 321]},
	{"text": "时间", "bbox": [105, 321, 142, 334]},
	{"text": "预计值", "bbox": [390, 296, 447, 309]},
	{"text": "实测值", "bbox": [483, 296, 540, 309]},
	{"text": "实/预", "bbox": [586, 295, 634, 308]},
	{"text": "25/10/31", "bbox": [466, 309, 540, 321]},
	{"text": "14:29:33", "bbox": [457, 323, 540, 335]},
	{"text": "MV", "bbox": [105, 349, 127, 358]},
	{"text": "[L/min]", "bbox": [287, 350, 350, 362]},
	{"text": "6.57", "bbox": [410, 350, 447, 362]},
	{"text": "11.52", "bbox": [495, 350, 540, 362]},
	{"text": "175.3", "bbox": [588, 349, 634, 360]},
	{"text": "VT", "bbox": [105, 362, 127, 371]},
	{"text": "[L]", "bbox": [326, 363, 350, 375]},
	{"text": "0.33", "bbox": [410, 363, 447, 375]},
	{"text": "0.79", "bbox": [503, 363, 540, 375]},
	{"text": "239.6", "bbox": [588, 362, 634, 374]},
	{"text": "BF", "bbox": [105, 375, 127, 384]},
	{"text": "[1/min]", "bbox": [287, 376, 350, 388]},
	{"text": "20.00", "bbox": [400, 376, 447, 388]},
	{"text": "14.63", "bbox": [495, 376, 540, 388]},
	{"text": "73.1", "bbox": [597, 375, 634, 387]},
	{"text": "VC MAX", "bbox": [105, 388, 165, 397]},
	{"text": "[L]", "bbox": [326, 389, 350, 401]},
	{"text": "2.03", "bbox": [410, 389, 447, 401]},
	{"text": "1.48", "bbox": [503, 389, 540, 401]},
	{"text": "73.0", "bbox": [597, 388, 634, 400]},
	{"text": "ERV", "bbox": [105, 401, 138, 410]},
	{"text": "[L]", "bbox": [326, 402, 350, 414]},
	{"text": "0.57", "bbox": [410, 402, 447, 414]},
	{"text": "0.14", "bbox": [503, 402, 540, 414]},
	{"text": "25.5", "bbox": [597, 401, 634, 413]},
	{"text": "IC", "bbox": [105, 414, 127, 423]},
	{"text": "[L]", "bbox": [326, 415, 350, 427]},
	{"text": "1.46", "bbox": [410, 415, 447, 427]},
	{"text": "1.34", "bbox": [503, 415, 540, 427]},
	{"text": "91.6", "bbox": [597, 414, 634, 426]},
	{"text": "FVC", "bbox": [105, 427, 138, 436]},
	{"text": "[L]", "bbox": [326, 428, 350, 440]},
	{"text": "1.93", "bbox": [410, 428, 447, 440]},
	{"text": "1.44", "bbox": [503, 428, 540, 440]},
	{"text": "74.8", "bbox": [597, 427, 634, 439]},
	{"text": "FEV 1", "bbox": [105, 439, 154, 449]},
	{"text": "[L]", "bbox": [326, 440, 350, 452]},
	{"text": "1.56", "bbox": [410, 440, 447, 452]},
	{"text": "0.91", "bbox": [503, 440, 540, 452]},
	{"text": "58.4", "bbox": [597, 439, 634, 451]},
	{"text": "FEV 1 % FVC", "bbox": [105, 452, 212, 462]},
	{"text": "[%]", "bbox": [326, 453, 350, 465]},
	{"text": "63.38", "bbox": [495, 453, 540, 465]},
	{"text": "FEV 1 % VC MAX", "bbox": [105, 465, 240, 474]},
	{"text": "[%]", "bbox": [326, 466, 350, 478]},
	{"text": "75.42", "bbox": [400, 466, 447, 478]},
	{"text": "61.67", "bbox": [495, 466, 540, 478]},
	{"text": "81.8", "bbox": [597, 465, 634, 477]},
	{"text": "PEF", "bbox": [105, 477, 138, 487]},
	{"text": "[L/s]", "bbox": [307, 478, 350, 490]},
	{"text": "5.04", "bbox": [410, 478, 447, 490]},
	{"text": "2.51", "bbox": [503, 478, 540, 490]},
	{"text": "49.8", "bbox": [597, 477, 634, 489]},
	{"text": "MEF 75", "bbox": [105, 489, 165, 499]},
	{"text": "[L/s]", "bbox": [307, 490, 350, 502]},
	{"text": "4.66", "bbox": [410, 490, 447, 502]},
	{"text": "1.54", "bbox": [503, 490, 540, 502]},
	{"text": "33.1", "bbox": [597, 489, 634, 501]},
	{"text": "MEF 50", "bbox": [105, 502, 165, 511]},
	{"text": "[L/s]", "bbox": [307, 503, 350, 515]},
	{"text": "3.06", "bbox": [410, 503, 447, 515]},
	{"text": "0.56", "bbox": [503, 503, 540, 515]},
	{"text": "18.2", "bbox": [597, 502, 634, 514]},
	{"text": "MEF 25", "bbox": [105, 514, 165, 524]},
	{"text": "[L/s]", "bbox": [307, 515, 350, 527]},
	{"text": "0.90", "bbox": [410, 515, 447, 527]},
	{"text": "0.22", "bbox": [503, 515, 540, 527]},
	{"text": "24.6", "bbox": [597, 514, 634, 526]},
	{"text": "MEF 75/25", "bbox": [105, 526, 202, 536]},
	{"text": "[L/s]", "bbox": [307, 527, 350, 539]},
	{"text": "2.36", "bbox": [410, 527, 447, 539]},
	{"text": "0.50", "bbox": [503, 527, 540, 539]},
	{"text": "21.1", "bbox": [597, 526, 634, 538]},
	{"text": "FET", "bbox": [105, 538, 138, 548]},
	{"text": "[s]", "bbox": [326, 539, 350, 551]},
	{"text": "4.91", "bbox": [503, 539, 540, 551]},
	{"text": "LFV", "bbox": [105, 551, 138, 560]},
	{"text": "[L/min]", "bbox": [287, 551, 350, 563]},
	{"text": "73.10", "bbox": [400, 551, 447, 563]},
	{"text": "Z at 5 Hz", "bbox": [105, 576, 194, 586]},
	{"text": "[kPa/(L/s)]", "bbox": [252, 576, 350, 588]},
	{"text": "0.43", "bbox": [410, 576, 447, 588]},
	{"text": "0.58", "bbox": [503, 576, 540, 588]},
	{"text": "135.7", "bbox": [588, 576, 634, 588]},
	{"text": "Resonant frequency", "bbox": [105, 589, 278, 600]},
	{"text": "[1/s]", "bbox": [307, 589, 350, 601]},
	{"text": "30.00", "bbox": [495, 589, 540, 601]},
	{"text": "R at 5 Hz", "bbox": [105, 602, 194, 612]},
	{"text": "[kPa/(L/s)]", "bbox": [252, 602, 350, 614]},
	{"text": "0.41", "bbox": [410, 602, 447, 614]},
	{"text": "0.57", "bbox": [503, 602, 540, 614]},
	{"text": "137.2", "bbox": [588, 602, 634, 614]},
	{"text": "R nt 20 Hz", "bbox": [105, 615, 202, 624]},
	{"text": "[kPa/(L/s)]", "bbox": [252, 615, 350, 627]},
	{"text": "0.35", "bbox": [410, 615, 447, 627]},
	{"text": "0.34", "bbox": [503, 615, 540, 627]},
	{"text": "95.3", "bbox": [597, 615, 634, 627]},
	{"text": "R at 5 Hz", "bbox": [105, 627, 194, 637]},
	{"text": "[kPa/(L/s)]", "bbox": [252, 627, 350, 639]},
	{"text": "-0.11", "bbox": [400, 627, 447, 639]},
	{"text": "-0.12", "bbox": [495, 627, 540, 639]},
	{"text": "112.5", "bbox": [588, 627, 634, 639]},
	{"text": "Rcentral", "bbox": [105, 640, 183, 650]},
	{"text": "[kPa/(L/s)]", "bbox": [252, 640, 350, 652]},
	{"text": "0.12", "bbox": [503, 640, 540, 652]},
	{"text": "Rperipheral", "bbox": [105, 652, 210, 663]},
	{"text": "[kPa/(L/s)]", "bbox": [252, 653, 350, 665]},
	{"text": "0.40", "bbox": [503, 653, 540, 665]},
	{"text": "结论：", "bbox": [107, 689, 160, 705]},
	{"text": "1.中重度混合性肺通气功能障碍", "bbox": [107, 716, 371, 729]},
	{"text": "2.（阻力增加", "bbox": [107, 728, 238, 741]},
	{"text": "审核者专用章", "bbox": [747, 878, 920, 901]},
	{"text": "检查者：王美锦", "bbox": [747, 911, 927, 948]}
]
2026-08-05 05:02:28,025 INFO     29 [qwen-vl-text] coord API: raw_items=168, valid_items=168, elapsed=42.9s
2026-08-05 05:02:28,025 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能通气阻力检查报告, bbox=[375, 88, 634, 107]
2026-08-05 05:02:28,025 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[154, 112, 202, 125]
2026-08-05 05:02:28,025 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[154, 125, 347, 138]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[3]: text=身高：151 cm, bbox=[154, 138, 387, 149]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[4]: text=病历号：, bbox=[505, 110, 570, 123]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：72 Years, bbox=[678, 121, 754, 133]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[6]: text=体重：46 kg, bbox=[678, 134, 725, 146]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[7]: text=Flow [L/s], bbox=[121, 165, 173, 175]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[8]: text=F/V ex, bbox=[257, 165, 291, 173]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[9]: text=10, bbox=[102, 178, 115, 188]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[10]: text=5, bbox=[107, 199, 115, 208]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[11]: text=0, bbox=[107, 220, 115, 229]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[12]: text=2, bbox=[173, 230, 181, 238]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[13]: text=4, bbox=[231, 230, 240, 238]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[14]: text=6, bbox=[290, 230, 298, 238]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[15]: text=F/V in, bbox=[259, 274, 290, 283]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[16]: text=8, bbox=[408, 168, 416, 177]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[17]: text=Vol [L], bbox=[422, 170, 457, 181]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[18]: text=6, bbox=[408, 193, 416, 201]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[19]: text=4, bbox=[408, 220, 416, 228]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[20]: text=1, bbox=[623, 218, 633, 227]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[21]: text=Vol%Vcmax, bbox=[375, 243, 438, 252]
2026-08-05 05:02:28,026 INFO     29 [qwen-vl-text] coord item[22]: text=100, bbox=[380, 254, 400, 264]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[23]: text=Vcmax, bbox=[435, 257, 472, 266]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[24]: text=20, bbox=[387, 266, 398, 275]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[25]: text=0, bbox=[408, 272, 416, 280]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[26]: text=Time [s], bbox=[505, 262, 546, 272]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[27]: text=0, bbox=[417, 283, 425, 291]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[28]: text=1, bbox=[453, 283, 460, 291]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[29]: text=2, bbox=[487, 283, 495, 291]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[30]: text=3, bbox=[521, 283, 529, 291]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[31]: text=4, bbox=[555, 283, 563, 291]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[32]: text=5, bbox=[590, 283, 597, 291]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[33]: text=6, bbox=[623, 283, 631, 291]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[34]: text=2.0, bbox=[654, 161, 673, 170]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[35]: text=R [kPa/(L/s)] Normal breathingX [kPa/(L/s)], bbox=[678, 163, 887, 175]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[36]: text=1.5, bbox=[654, 187, 673, 196]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[37]: text=1.0, bbox=[654, 215, 673, 224]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[38]: text=0.5, bbox=[654, 243, 673, 252]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[39]: text=0.0, bbox=[654, 271, 673, 280]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[40]: text=F [Hz], bbox=[767, 261, 797, 271]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[41]: text=5, bbox=[673, 281, 681, 290]
2026-08-05 05:02:28,027 INFO     29 [qwen-vl-text] coord item[42]: text=10, bbox=[705, 281, 718, 290]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[43]: text=15, bbox=[739, 281, 751, 290]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[44]: text=20, bbox=[772, 281, 785, 290]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[45]: text=25, bbox=[808, 281, 822, 290]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[46]: text=30, bbox=[838, 281, 851, 290]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[47]: text=35, bbox=[872, 281, 885, 290]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[48]: text=日期, bbox=[105, 308, 142, 321]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[49]: text=时间, bbox=[105, 321, 142, 334]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[50]: text=预计值, bbox=[390, 296, 447, 309]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[51]: text=实测值, bbox=[483, 296, 540, 309]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[52]: text=实/预, bbox=[586, 295, 634, 308]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[53]: text=25/10/31, bbox=[466, 309, 540, 321]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[54]: text=14:29:33, bbox=[457, 323, 540, 335]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[55]: text=MV, bbox=[105, 349, 127, 358]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[56]: text=[L/min], bbox=[287, 350, 350, 362]
2026-08-05 05:02:28,028 INFO     29 [qwen-vl-text] coord item[57]: text=6.57, bbox=[410, 350, 447, 362]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[58]: text=11.52, bbox=[495, 350, 540, 362]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[59]: text=175.3, bbox=[588, 349, 634, 360]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[60]: text=VT, bbox=[105, 362, 127, 371]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[61]: text=[L], bbox=[326, 363, 350, 375]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[62]: text=0.33, bbox=[410, 363, 447, 375]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[63]: text=0.79, bbox=[503, 363, 540, 375]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[64]: text=239.6, bbox=[588, 362, 634, 374]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[65]: text=BF, bbox=[105, 375, 127, 384]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[66]: text=[1/min], bbox=[287, 376, 350, 388]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[67]: text=20.00, bbox=[400, 376, 447, 388]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[68]: text=14.63, bbox=[495, 376, 540, 388]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[69]: text=73.1, bbox=[597, 375, 634, 387]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[70]: text=VC MAX, bbox=[105, 388, 165, 397]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[71]: text=[L], bbox=[326, 389, 350, 401]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[72]: text=2.03, bbox=[410, 389, 447, 401]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[73]: text=1.48, bbox=[503, 389, 540, 401]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[74]: text=73.0, bbox=[597, 388, 634, 400]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[75]: text=ERV, bbox=[105, 401, 138, 410]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[76]: text=[L], bbox=[326, 402, 350, 414]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[77]: text=0.57, bbox=[410, 402, 447, 414]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[78]: text=0.14, bbox=[503, 402, 540, 414]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[79]: text=25.5, bbox=[597, 401, 634, 413]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[80]: text=IC, bbox=[105, 414, 127, 423]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[81]: text=[L], bbox=[326, 415, 350, 427]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[82]: text=1.46, bbox=[410, 415, 447, 427]
2026-08-05 05:02:28,029 INFO     29 [qwen-vl-text] coord item[83]: text=1.34, bbox=[503, 415, 540, 427]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[84]: text=91.6, bbox=[597, 414, 634, 426]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[85]: text=FVC, bbox=[105, 427, 138, 436]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[86]: text=[L], bbox=[326, 428, 350, 440]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[87]: text=1.93, bbox=[410, 428, 447, 440]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[88]: text=1.44, bbox=[503, 428, 540, 440]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[89]: text=74.8, bbox=[597, 427, 634, 439]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[90]: text=FEV 1, bbox=[105, 439, 154, 449]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[91]: text=[L], bbox=[326, 440, 350, 452]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[92]: text=1.56, bbox=[410, 440, 447, 452]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[93]: text=0.91, bbox=[503, 440, 540, 452]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[94]: text=58.4, bbox=[597, 439, 634, 451]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[95]: text=FEV 1 % FVC, bbox=[105, 452, 212, 462]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[96]: text=[%], bbox=[326, 453, 350, 465]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[97]: text=63.38, bbox=[495, 453, 540, 465]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[98]: text=FEV 1 % VC MAX, bbox=[105, 465, 240, 474]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[99]: text=[%], bbox=[326, 466, 350, 478]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[100]: text=75.42, bbox=[400, 466, 447, 478]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[101]: text=61.67, bbox=[495, 466, 540, 478]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[102]: text=81.8, bbox=[597, 465, 634, 477]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[103]: text=PEF, bbox=[105, 477, 138, 487]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[104]: text=[L/s], bbox=[307, 478, 350, 490]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[105]: text=5.04, bbox=[410, 478, 447, 490]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[106]: text=2.51, bbox=[503, 478, 540, 490]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[107]: text=49.8, bbox=[597, 477, 634, 489]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[108]: text=MEF 75, bbox=[105, 489, 165, 499]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[109]: text=[L/s], bbox=[307, 490, 350, 502]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[110]: text=4.66, bbox=[410, 490, 447, 502]
2026-08-05 05:02:28,030 INFO     29 [qwen-vl-text] coord item[111]: text=1.54, bbox=[503, 490, 540, 502]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[112]: text=33.1, bbox=[597, 489, 634, 501]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[113]: text=MEF 50, bbox=[105, 502, 165, 511]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[114]: text=[L/s], bbox=[307, 503, 350, 515]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[115]: text=3.06, bbox=[410, 503, 447, 515]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[116]: text=0.56, bbox=[503, 503, 540, 515]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[117]: text=18.2, bbox=[597, 502, 634, 514]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[118]: text=MEF 25, bbox=[105, 514, 165, 524]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[119]: text=[L/s], bbox=[307, 515, 350, 527]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[120]: text=0.90, bbox=[410, 515, 447, 527]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[121]: text=0.22, bbox=[503, 515, 540, 527]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[122]: text=24.6, bbox=[597, 514, 634, 526]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[123]: text=MEF 75/25, bbox=[105, 526, 202, 536]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[124]: text=[L/s], bbox=[307, 527, 350, 539]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[125]: text=2.36, bbox=[410, 527, 447, 539]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[126]: text=0.50, bbox=[503, 527, 540, 539]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[127]: text=21.1, bbox=[597, 526, 634, 538]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[128]: text=FET, bbox=[105, 538, 138, 548]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[129]: text=[s], bbox=[326, 539, 350, 551]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[130]: text=4.91, bbox=[503, 539, 540, 551]
2026-08-05 05:02:28,031 INFO     29 [qwen-vl-text] coord item[131]: text=LFV, bbox=[105, 551, 138, 560]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[132]: text=[L/min], bbox=[287, 551, 350, 563]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[133]: text=73.10, bbox=[400, 551, 447, 563]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[134]: text=Z at 5 Hz, bbox=[105, 576, 194, 586]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[135]: text=[kPa/(L/s)], bbox=[252, 576, 350, 588]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[136]: text=0.43, bbox=[410, 576, 447, 588]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[137]: text=0.58, bbox=[503, 576, 540, 588]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[138]: text=135.7, bbox=[588, 576, 634, 588]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[139]: text=Resonant frequency, bbox=[105, 589, 278, 600]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[140]: text=[1/s], bbox=[307, 589, 350, 601]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[141]: text=30.00, bbox=[495, 589, 540, 601]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[142]: text=R at 5 Hz, bbox=[105, 602, 194, 612]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[143]: text=[kPa/(L/s)], bbox=[252, 602, 350, 614]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[144]: text=0.41, bbox=[410, 602, 447, 614]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[145]: text=0.57, bbox=[503, 602, 540, 614]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[146]: text=137.2, bbox=[588, 602, 634, 614]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[147]: text=R nt 20 Hz, bbox=[105, 615, 202, 624]
2026-08-05 05:02:28,032 INFO     29 [qwen-vl-text] coord item[148]: text=[kPa/(L/s)], bbox=[252, 615, 350, 627]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[149]: text=0.35, bbox=[410, 615, 447, 627]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[150]: text=0.34, bbox=[503, 615, 540, 627]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[151]: text=95.3, bbox=[597, 615, 634, 627]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[152]: text=R at 5 Hz, bbox=[105, 627, 194, 637]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[153]: text=[kPa/(L/s)], bbox=[252, 627, 350, 639]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[154]: text=-0.11, bbox=[400, 627, 447, 639]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[155]: text=-0.12, bbox=[495, 627, 540, 639]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[156]: text=112.5, bbox=[588, 627, 634, 639]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[157]: text=Rcentral, bbox=[105, 640, 183, 650]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[158]: text=[kPa/(L/s)], bbox=[252, 640, 350, 652]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[159]: text=0.12, bbox=[503, 640, 540, 652]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[160]: text=Rperipheral, bbox=[105, 652, 210, 663]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[161]: text=[kPa/(L/s)], bbox=[252, 653, 350, 665]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[162]: text=0.40, bbox=[503, 653, 540, 665]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[163]: text=结论：, bbox=[107, 689, 160, 705]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[164]: text=1.中重度混合性肺通气功能障碍, bbox=[107, 716, 371, 729]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[165]: text=2.（阻力增加, bbox=[107, 728, 238, 741]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[166]: text=审核者专用章, bbox=[747, 878, 920, 901]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] coord item[167]: text=检查者：王美锦, bbox=[747, 911, 927, 948]
2026-08-05 05:02:28,033 INFO     29 [qwen-vl-text] page=7 — 173/173 coords, api_time=42.9s
2026-08-05 05:02:28,035 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=851048, prompt_len=1833
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["报告时间: 2025-04-05", "\\multicolumn{1}{c}{} \\multicolumn{1}{c}{预计值} \\multicolumn{1}{c}{前次} \\multicolumn{1}{c}{前/预} \\multicolumn{1}{c}{后次} \\multicolumn{1}{c}{后/预} \\multicolumn{1}{c}{改善率}", "\\multicolumn{1}{c}{日期} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{25/10/31} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{25/10/31} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{}", "\\multicolumn{1}{c}{时间} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{14:29:33} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{14:53:10} \\multicolumn{1}{c}{} \\multicolumn{1}{c}{}", "VT [L] 0.33 0.79 239.6", "BF [1/min] 20.00 14.63 73.1", "MV [L/min] 6.57 11.52 175.3", "VC MAX [L] 2.03 1.48 73.0 1.66 81.9 12.2", "ERV [L] 0.57 0.14 25.5", "IC [L] 1.46 1.34 91.6", "FVC [L] 1.93 1.44 74.8 1.66 86.2 15.3", "FEV 1 [L] 1.56 0.91 58.4 1.08 68.8 17.8", "FEV 1 % FVC [%] 63.38 64.76 2.2", "FEV 1 % VC MAX [%] 75.42 61.67 81.8 64.76 85.9 5.0", "PEF [L/s] 5.04 2.51 49.8 3.35 66.5 33.6", "MEF 75 [L/s] 4.66 1.54 33.1 1.72 36.8 11.3", "MEF 50 [L/s] 3.06 0.56 18.2 0.83 27.1 49.1", "MEF 25 [L/s] 0.90 0.22 24.6 0.36 39.8 62.1", "MMEF 75/25 [L/s] 2.36 0.50 21.1 0.47 20.0 -4.9", "FET [s] 4.91 4.88 -0.6", "V backextrapol. % FVC [%] 3.85 4.39 13.9", "MVV [L/min] 73.10"]

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
2026-08-05 05:02:29,218 INFO     29 [qwen-vl-text] coord API raw response (len=2):
[]
2026-08-05 05:02:29,219 INFO     29 [qwen-vl-text] coord API: raw_items=0, valid_items=0, elapsed=1.2s
2026-08-05 05:02:29,219 WARNING  29 [qwen-vl-text] page=8 coord failed: ok, adding 22 placeholder(s)
2026-08-05 05:02:29,220 INFO     29 [qwen-vl-text] new_positions (195):
[[7, 229.5, 388.008, 73.21851904296875, 89.02706292724609], [7, 94.248, 123.624, 93.18720605468751, 104.00357818603516], [7, 94.248, 212.364, 104.00357818603516, 114.81995031738282], [7, 94.248, 236.844, 114.81995031738282, 123.97226519775391], [7, 309.06, 348.84, 91.52314880371094, 102.3395209350586], [7, 414.936, 461.448, 100.67546368408203, 110.6598071899414], [7, 414.936, 443.7, 111.4918358154297, 121.47617932128907], [7, 74.05199999999999, 105.876, 137.28472320556642, 145.60500946044922], [7, 157.284, 178.09199999999998, 137.28472320556642, 143.94095220947267], [7, 62.424, 70.38, 148.10109533691406, 156.4213815917969], [7, 65.484, 70.38, 165.57369647216797, 173.0619541015625], [7, 65.484, 70.38, 183.04629760742188, 190.5345552368164], [7, 105.876, 110.77199999999999, 191.36658386230468, 198.02281286621096], [7, 141.37199999999999, 146.88, 191.36658386230468, 198.02281286621096], [7, 177.48, 182.376, 191.36658386230468, 198.02281286621096], [7, 158.508, 177.48, 227.97584338378905, 235.4641010131836], [7, 249.696, 254.59199999999998, 139.78080908203125, 147.26906671142578], [7, 258.264, 279.68399999999997, 141.4448663330078, 150.59718121337892], [7, 249.696, 254.59199999999998, 160.58152471923827, 167.23775372314452], [7, 249.696, 254.59199999999998, 183.04629760742188, 189.70252661132812], [7, 381.276, 387.396, 181.38224035644532, 188.87049798583985], [7, 229.5, 268.056, 202.18295599365234, 209.67121362304687], [7, 232.56, 244.79999999999998, 211.33527087402345, 219.65555712890625], [7, 266.21999999999997, 288.864, 213.83135675048828, 221.3196143798828], [7, 236.844, 243.576, 221.3196143798828, 228.80787200927736], [7, 249.696, 254.59199999999998, 226.3117861328125, 232.96801513671875], [7, 309.06, 334.152, 217.9914998779297, 226.3117861328125], [7, 255.204, 260.1, 235.4641010131836, 242.12033001708986], [7, 277.236, 281.52, 235.4641010131836, 242.12033001708986], [7, 298.044, 302.94, 235.4641010131836, 242.12033001708986], [7, 318.852, 323.748, 235.4641010131836, 242.12033001708986], [7, 339.65999999999997, 344.556, 235.4641010131836, 242.12033001708986], [7, 361.08, 365.364, 235.4641010131836, 242.12033001708986], [7, 381.276, 386.17199999999997, 235.4641010131836, 242.12033001708986], [7, 400.248, 411.876, 133.95660870361328, 141.4448663330078], [7, 414.936, 542.8439999999999, 135.62066595458984, 145.60500946044922], [7, 400.248, 411.876, 155.5893529663086, 163.07761059570313], [7, 400.248, 411.876, 178.88615447998046, 186.37441210937502], [7, 400.248, 411.876, 202.18295599365234, 209.67121362304687], [7, 400.248, 411.876, 225.47975750732422, 232.96801513671875], [7, 469.404, 487.764, 217.15947125244142, 225.47975750732422], [7, 411.876, 416.772, 233.80004376220703, 241.28830139160158], [7, 431.46, 439.416, 233.80004376220703, 241.28830139160158], [7, 452.268, 459.61199999999997, 233.80004376220703, 241.28830139160158], [7, 472.464, 480.42, 233.80004376220703, 241.28830139160158], [7, 494.496, 503.06399999999996, 233.80004376220703, 241.28830139160158], [7, 512.856, 520.812, 233.80004376220703, 241.28830139160158], [7, 533.664, 541.62, 233.80004376220703, 241.28830139160158], [7, 64.26, 86.904, 256.2648166503906, 267.08118878173826], [7, 64.26, 86.904, 267.08118878173826, 277.89756091308595], [7, 238.68, 273.564, 246.28047314453124, 257.09684527587893], [7, 295.596, 330.48, 246.28047314453124, 257.09684527587893], [7, 358.632, 388.008, 245.44844451904297, 256.2648166503906], [7, 285.192, 330.48, 257.09684527587893, 267.08118878173826], [7, 279.68399999999997, 330.48, 268.7452460327149, 278.7295895385742], [7, 64.26, 77.724, 290.37799029541014, 297.86624792480467], [7, 175.644, 214.2, 291.21001892089845, 301.19436242675783], [7, 250.92, 273.564, 291.21001892089845, 301.19436242675783], [7, 302.94, 330.48, 291.21001892089845, 301.19436242675783], [7, 359.856, 388.008, 290.37799029541014, 299.5303051757813], [7, 64.26, 77.724, 301.19436242675783, 308.68262005615236], [7, 199.512, 214.2, 302.0263910522461, 312.01073455810547], [7, 250.92, 273.564, 302.0263910522461, 312.01073455810547], [7, 307.836, 330.48, 302.0263910522461, 312.01073455810547], [7, 359.856, 388.008, 301.19436242675783, 311.1787059326172], [7, 64.26, 77.724, 312.01073455810547, 319.4989921875], [7, 175.644, 214.2, 312.8427631835938, 322.82710668945316], [7, 244.79999999999998, 273.564, 312.8427631835938, 322.82710668945316], [7, 302.94, 330.48, 312.8427631835938, 322.82710668945316], [7, 365.364, 388.008, 312.01073455810547, 321.99507806396485], [7, 64.26, 100.98, 322.82710668945316, 330.3153643188477], [7, 199.512, 214.2, 323.6591353149414, 333.6434788208008], [7, 250.92, 273.564, 323.6591353149414, 333.6434788208008], [7, 307.836, 330.48, 323.6591353149414, 333.6434788208008], [7, 365.364, 388.008, 322.82710668945316, 332.8114501953125], [7, 64.26, 84.456, 333.6434788208008, 341.1317364501953], [7, 199.512, 214.2, 334.47550744628904, 344.45985095214843], [7, 250.92, 273.564, 334.47550744628904, 344.45985095214843], [7, 307.836, 330.48, 334.47550744628904, 344.45985095214843], [7, 365.364, 388.008, 333.6434788208008, 343.6278223266602], [7, 64.26, 77.724, 344.45985095214843, 351.94810858154295], [7, 199.512, 214.2, 345.29187957763673, 355.2762230834961], [7, 250.92, 273.564, 345.29187957763673, 355.2762230834961], [7, 307.836, 330.48, 345.29187957763673, 355.2762230834961], [7, 365.364, 388.008, 344.45985095214843, 354.4441944580078], [7, 64.26, 84.456, 355.2762230834961, 362.76448071289065], [7, 199.512, 214.2, 356.10825170898437, 366.09259521484375], [7, 250.92, 273.564, 356.10825170898437, 366.09259521484375], [7, 307.836, 330.48, 356.10825170898437, 366.09259521484375], [7, 365.364, 388.008, 355.2762230834961, 365.2605665893555], [7, 64.26, 94.248, 365.2605665893555, 373.5808528442383], [7, 199.512, 214.2, 366.09259521484375, 376.07693872070314], [7, 250.92, 273.564, 366.09259521484375, 376.07693872070314], [7, 307.836, 330.48, 366.09259521484375, 376.07693872070314], [7, 365.364, 388.008, 365.2605665893555, 375.24491009521483], [7, 64.26, 129.744, 376.07693872070314, 384.39722497558597], [7, 199.512, 214.2, 376.9089673461914, 386.8933108520508], [7, 302.94, 330.48, 376.9089673461914, 386.8933108520508], [7, 64.26, 146.88, 386.8933108520508, 394.3815684814453], [7, 199.512, 214.2, 387.7253394775391, 397.70968298339847], [7, 244.79999999999998, 273.564, 387.7253394775391, 397.70968298339847], [7, 302.94, 330.48, 387.7253394775391, 397.70968298339847], [7, 365.364, 388.008, 386.8933108520508, 396.87765435791016], [7, 64.26, 84.456, 396.87765435791016, 405.197940612793], [7, 187.884, 214.2, 397.70968298339847, 407.6940264892578], [7, 250.92, 273.564, 397.70968298339847, 407.6940264892578], [7, 307.836, 330.48, 397.70968298339847, 407.6940264892578], [7, 365.364, 388.008, 396.87765435791016, 406.86199786376955], [7, 64.26, 100.98, 406.86199786376955, 415.1822841186524], [7, 187.884, 214.2, 407.6940264892578, 417.6783699951172], [7, 250.92, 273.564, 407.6940264892578, 417.6783699951172], [7, 307.836, 330.48, 407.6940264892578, 417.6783699951172], [7, 365.364, 388.008, 406.86199786376955, 416.84634136962893], [7, 64.26, 100.98, 417.6783699951172, 425.1666276245117], [7, 187.884, 214.2, 418.5103986206055, 428.49474212646487], [7, 250.92, 273.564, 418.5103986206055, 428.49474212646487], [7, 307.836, 330.48, 418.5103986206055, 428.49474212646487], [7, 365.364, 388.008, 417.6783699951172, 427.66271350097657], [7, 64.26, 100.98, 427.66271350097657, 435.9829997558594], [7, 187.884, 214.2, 428.49474212646487, 438.47908563232426], [7, 250.92, 273.564, 428.49474212646487, 438.47908563232426], [7, 307.836, 330.48, 428.49474212646487, 438.47908563232426], [7, 365.364, 388.008, 427.66271350097657, 437.64705700683595], [7, 64.26, 123.624, 437.64705700683595, 445.9673432617188], [7, 187.884, 214.2, 438.47908563232426, 448.4634291381836], [7, 250.92, 273.564, 438.47908563232426, 448.4634291381836], [7, 307.836, 330.48, 438.47908563232426, 448.4634291381836], [7, 365.364, 388.008, 437.64705700683595, 447.63140051269534], [7, 64.26, 84.456, 447.63140051269534, 455.9516867675781], [7, 199.512, 214.2, 448.4634291381836, 458.44777264404297], [7, 307.836, 330.48, 448.4634291381836, 458.44777264404297], [7, 64.26, 84.456, 458.44777264404297, 465.9360302734375], [7, 175.644, 214.2, 458.44777264404297, 468.43211614990236], [7, 244.79999999999998, 273.564, 458.44777264404297, 468.43211614990236], [7, 64.26, 118.728, 479.24848828125, 487.5687745361328], [7, 154.224, 214.2, 479.24848828125, 489.2328317871094], [7, 250.92, 273.564, 479.24848828125, 489.2328317871094], [7, 307.836, 330.48, 479.24848828125, 489.2328317871094], [7, 359.856, 388.008, 479.24848828125, 489.2328317871094], [7, 64.26, 170.136, 490.0648604125977, 499.21717529296876], [7, 187.884, 214.2, 490.0648604125977, 500.04920391845707], [7, 302.94, 330.48, 490.0648604125977, 500.04920391845707], [7, 64.26, 118.728, 500.8812325439453, 509.20151879882815], [7, 154.224, 214.2, 500.8812325439453, 510.8655760498047], [7, 250.92, 273.564, 500.8812325439453, 510.8655760498047], [7, 307.836, 330.48, 500.8812325439453, 510.8655760498047], [7, 359.856, 388.008, 500.8812325439453, 510.8655760498047], [7, 64.26, 123.624, 511.697604675293, 519.1858623046875], [7, 154.224, 214.2, 511.697604675293, 521.6819481811524], [7, 250.92, 273.564, 511.697604675293, 521.6819481811524], [7, 307.836, 330.48, 511.697604675293, 521.6819481811524], [7, 365.364, 388.008, 511.697604675293, 521.6819481811524], [7, 64.26, 118.728, 521.6819481811524, 530.0022344360352], [7, 154.224, 214.2, 521.6819481811524, 531.6662916870117], [7, 244.79999999999998, 273.564, 521.6819481811524, 531.6662916870117], [7, 302.94, 330.48, 521.6819481811524, 531.6662916870117], [7, 359.856, 388.008, 521.6819481811524, 531.6662916870117], [7, 64.26, 111.996, 532.4983203125, 540.8186065673829], [7, 154.224, 214.2, 532.4983203125, 542.4826638183594], [7, 307.836, 330.48, 532.4983203125, 542.4826638183594], [7, 64.26, 128.52, 542.4826638183594, 551.6349786987305], [7, 154.224, 214.2, 543.3146924438477, 553.299035949707], [7, 307.836, 330.48, 543.3146924438477, 553.299035949707], [7, 65.484, 97.92, 573.2677229614258, 586.5801809692383], [7, 65.484, 227.052, 595.7324958496093, 606.5488679809571], [7, 65.484, 145.656, 605.7168393554688, 616.5332114868164], [7, 457.164, 563.04, 730.521133178711, 749.6577915649415], [7, 457.164, 567.324, 757.9780778198242, 788.7631369628906], [7, 65.484, 97.92, 573.2677229614258, 586.5801809692383], [7, 65.484, 227.052, 595.7324958496093, 606.5488679809571], [7, 65.484, 145.656, 605.7168393554688, 616.5332114868164], [7, 457.164, 563.04, 730.521133178711, 749.6577915649415], [7, 457.164, 567.324, 757.9780778198242, 788.7631369628906], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0], [8, 0, 0, 0, 0]]
2026-08-05 05:02:29,222 INFO     29 [qwen-vl-text] ═══ DONE ═══ 195 positions, pages=2, time=62.4s
2026-08-05 05:02:29,234 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 05:02:29,234 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "4522 items", "markdown": "", "text": "", "name": "LXQI222.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1}"}
2026-08-05 05:02:29,234 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 05:02:29,235 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:02:29.235+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 13, "failed": 0, "current": {"ca1be81a908911f1a3da71efcdd7cc1f": {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:02:29,237 INFO     29 [ChunkMerger] Merged 4 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 4 noise chunks)
2026-08-05 05:02:29,598 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 05:02:29,599 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "4 items, types={'PrescriptionRecord': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 1}", "name": "LXQI222.pdf"}
2026-08-05 05:02:29,599 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 05:02:29,751 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785905691155, 'update_date': datetime.datetime(2026, 8, 5, 4, 54, 51), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 172516, 'status': '1'}
2026-08-05 05:02:30,047 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=亦康互联网医院
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
已使用
用法用量：
口腔吸入,一日两次,一次1.0揿;
已使用
补充说明：处方超7日为病情需要
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
心)、心肌酶全套(临床检验中心)、氯(临床检验中心)、白细胞介素-6(临床检验中心)、钠(临床检验中心)、葡萄糖测定(临床检验中心)、肌酐(临床检验中心):钾(K)4.47mmol/L白介素-6(IL-6)2.10pg/ml
肌酐(Cr)57.90μmol/L C反应蛋白(CRP)0.48mg/L丙氨酸氨基转移酶(ALT)17.50U/L天冬氨酸氨基转移
酶(AST)25.40U/L。2025-10-3017:34 DIC全套(临床检验中心):纤维蛋白原(Fg)5.09g/L D-二聚体(DD)
0.75μg/mLDDU。2025-10-3015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3
015:46 静态心电图(含十二通道加收):窦性心律 HR 69 bpm。2025-10-3113:11 胸部CT平扫:1、考虑双肺新增少许感染灶,以左肺为著,请结合临床并复查。2、双肺尖多发结节灶、纤维化灶,邻近双侧
1/3
贵州醫科大學附屬醫院
THE AFFILIATED HOSPITAL OF GUIZHOU MEDICAL UNIVERSITY
出院记录
姓名:
床号:23-03床
病历号:
科室:呼吸与危重医学科医生站
胸膜局限性增厚,考虑陈旧性病变,建议随诊复查。3、左肺下叶外基底段局部间质性改变,其内支气管
扩张;双肺支气管壁稍增厚,考虑慢性支气管炎,请结合临床并复查。4、左肺下叶微小结节,建议随诊
复查。5、纵隔内淋巴结稍增大,建议随诊复查。6、主动脉及冠状动脉硬化;胸椎退变,左侧第2前肋走
行欠佳。7、肝内囊性灶,建议超声随诊复查。2025-10-3114:35肺通气功能测定及支气管舒张试验:1.
中重度混合性肺通气功能障碍2.气道阻力增加3.支气管舒张试验阳性(+)2025-10-3112:33。传染病筛查
三项:阴性。2025-10-3113:12乙肝5项(定量):阴性。2025-10-3115:12大便常规(不含寄生虫)(临
床检验中心):未见异常。2025-10-3115:10尿液检查(尿液分析+尿有形成分):未见异常。2025-10-31
14:37痰液革兰氏染色+抗酸染色+真菌(临床检验中心):未见异常。2025-11-0210:41痰细菌培养及鉴
定:未检出流感嗜血杆菌。治疗上予头孢美唑钠抗感染,痰热清祛痰、布地奈德+沙丁胺醇雾化抗炎扩张支
气管等对症支持治疗,先后予沙美特罗替卡松、布地格福、孟鲁司特钠片、氨茶碱抗炎舒张支气管等对症
治疗,经我科治疗后,患者病情较前好转,目前一般情况可,请示上级医师盾予今日办理出院。
出院诊断:1.支气管哮喘急性发作期;2.社区获得性肺炎,非重症;3.慢性阻塞性肺疾病;4.左肺下叶小
结节;5.肝囊肿。
出院情况:患者咳嗽、咳痰、胸闷、气促好转,无呼吸困难,无畏寒、发热,无恶心、呕吐等不适。查
体:生命体征平稳。全身皮肤黏膜、巩膜无黄染,双肺呼吸音清,未闻及干湿性啰音。律齐,各瓣膜听诊
区未闻及病理性杂音,腹软,全腹无压痛及反跳痛,肝脾肋下未及,肝脾肋下未及,双下肢无水肿。
VTE评估:
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
病；食物、药物过敏无；无外伤史；无手术史；无输血史；无中毒史；无长期用药史；无可能成瘾药物。疫
苗接种史不详
个人史：
出生于贵州省贵阳市，职业：离退人员，学历：其他，宗教：无，成长居住地：贵州省贵阳市，居住较长
地：贵州省贵阳市，无疫区居留史。无冶游史。无饮酒习惯。无吸烟习惯。无工业毒物、粉尘、放射性物
质接触史。
婚育史：
已婚已育，适龄结婚，配偶身体健康。育有1子1女，子女均体健。
月经史：
初潮年龄17岁 经期3-4天 绝经年龄53岁 月经及白带情况：正常
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
触诊：心尖搏动：正常 振颤：无 心包摩擦感：无
叩诊：
第五肋间内0.5cm
心界
右(cm)
肋间
左(cm)
2
2
2
1
3
(左锁骨中线距胸骨线7.5cm)
听诊：心率：92次/分 心律：齐 心音：未闻及异常心
额外心音：无 杂音：无 心包摩擦音：
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
跟腱反射：正常Babinski征：阴性
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
R at 5 Hz
[kPa/(L/s)]
-0.11
-0.12
112.5
Rcentral
[kPa/(L/s)]
0.12
Rperipheral
[kPa/(L/s)]
0.40
结论：
1.中重度混合性肺通气功能障碍
2.（阻力增加
审核者专用章
检查者：王美锦
报告时间: 2025-04-05
\multicolumn{1}{c}{} \multicolumn{1}{c}{预计值} \multicolumn{1}{c}{前次} \multicolumn{1}{c}{前/预} \multicolumn{1}{c}{后次} \multicolumn{1}{c}{后/预} \multicolumn{1}{c}{改善率}
\multicolumn{1}{c}{日期} \multicolumn{1}{c}{} \multicolumn{1}{c}{25/10/31} \multicolumn{1}{c}{} \multicolumn{1}{c}{25/10/31} \multicolumn{1}{c}{} \multicolumn{1}{c}{}
\multicolumn{1}{c}{时间} \multicolumn{1}{c}{} \multicolumn{1}{c}{14:29:33} \multicolumn{1}{c}{} \multicolumn{1}{c}{14:53:10} \multicolumn{1}{c}{} \multicolumn{1}{c}{}
VT [L] 0.33 0.79 239.6
BF [1/min] 20.00 14.63 73.1
MV [L/min] 6.57 11.52 175.3
VC MAX [L] 2.03 1.48 73.0 1.66 81.9 12.2
ERV [L] 0.57 0.14 25.5
IC [L] 1.46 1.34 91.6
FVC [L] 1.93 1.44 74.8 1.66 86.2 15.3
FEV 1 [L] 1.56 0.91 58.4 1.08 68.8 17.8
FEV 1 % FVC [%] 63.38 64.76 2.2
FEV 1 % VC MAX [%] 75.42 61.67 81.8 64.76 85.9 5.0
PEF [L/s] 5.04 2.51 49.8 3.35 66.5 33.6
MEF 75 [L/s] 4.66 1.54 33.1 1.72 36.8 11.3
MEF 50 [L/s] 3.06 0.56 18.2 0.83 27.1 49.1
MEF 25 [L/s] 0.90 0.22 24.6 0.36 39.8 62.1
MMEF 75/25 [L/s] 2.36 0.50 21.1 0.47 20.0 -4.9
FET [s] 4.91 4.88 -0.6
V backextrapol. % FVC [%] 3.85 4.39 13.9
MVV [L/min] 73.10
2026-08-05 05:02:30,563 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 05:02:30,563 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "4 items, types={'PrescriptionRecord': 1, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 1}", "name": "LXQI222.pdf", "embedding_token_consumption": 6179}
2026-08-05 05:02:30,563 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 05:02:30,666 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 05:02:30,667 INFO     29 [Trace] task=ca1be81a | doc=LXQI222.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":4,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 05:02:30,670 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:02:30,670 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:02:30,670 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:02:30,670 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:02:30,674 INFO     29 set_progress(ca1be81a908911f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 05:02:30 [DOC Engine]:
Start to index...
2026-08-05 05:02:30,696 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.017s]
2026-08-05 05:02:30,704 INFO     29 set_progress(ca1be81a908911f1a3da71efcdd7cc1f), progress: 0.8250000000000001, progress_msg: 
2026-08-05 05:02:30,711 INFO     29 set_progress(ca1be81a908911f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 05:02:30 Indexing done (0.04s). Task done (423.34s)
2026-08-05 05:02:30,716 INFO     29 [Done], chunks(4), token(6179), elapsed:423.34
2026-08-05 05:02:30,993 INFO     29 handle_task done for task {"id": "ca1be81a908911f1a3da71efcdd7cc1f", "doc_id": "c9872b6c908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LXQI222.pdf", "type": "pdf", "location": "LXQI222.pdf", "size": 64448220, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785905690096, "task_type": "dataflow", "root_trace_id": "015b64dddce34487955ec54cfaf98060", "root_traceparent": "00-015b64dddce34487955ec54cfaf98060-f0bc2e366e356d1b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
