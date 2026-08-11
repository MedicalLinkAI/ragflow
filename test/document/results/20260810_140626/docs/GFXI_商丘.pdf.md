# 基准结果：GFXI 商丘.pdf

## 基本信息

- 文件：`GFXI 商丘.pdf`
- 大小：3218.5 KB
- PDF 总页数：4
- doc_id：`b40fb046948111f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T14:07:00  完成时间：2026-08-10T14:10:56  耗时：236.2s
- progress_msg：`06:10:24 Indexing done (0.21s). Task done (183.75s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

**该文档没有任何 chunk（文档级被过滤或解析失败）**

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
- ChunkMerger：`{"found": true, "merged": 2, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 06:10:21,721 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 06:07:19,878 INFO     29 handle_task begin for task {"id": "b531b82a948111f1bd9827cf206dfa2d", "doc_id": "b40fb046948111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342023691, "task_type": "dataflow", "root_trace_id": "5de32dcc1c9241298e4a586d264050c9", "root_traceparent": "00-5de32dcc1c9241298e4a586d264050c9-8ca896b124088c1e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 06:07:20,129 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 06:07:20,236 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 06:07:20,787 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:07:20,787 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 06:07:20,787 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 06:07:20,797 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 06:07:20,797 INFO     29 ============================================================
2026-08-10 06:07:20,797 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 06:07:20,797 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 06:07:20,797 INFO     29 ============================================================
2026-08-10 06:07:20,797 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 06:07:20,797 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 06:07:20,798 INFO     29 No torch found.
2026-08-10 06:07:21,517 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=4
2026-08-10 06:07:21,717 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1045252, prompt_len=764
2026-08-10 06:07:23,235 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 06:07:23,236 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 06:07:23,244 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1045252, prompt_len=401
2026-08-10 06:07:28,565 INFO     29 [qwen-vl-parser] text API response (len=836):
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：111", "住院号：", "体格检查", "T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg", "发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧", "虑，走入病房，检查合作。", "皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，", "无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。", "淋巴结：全身浅表淋巴结无肿大。", "头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔", "2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦", "无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、", "红肿，声音无嘶哑。", "颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流", "征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿", "大。", "胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、", "皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。", "肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发", "感。叩诊音呈清音。呼吸音异常干性啰音。", "心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所", "示。心率82次/分，心律齐。", "腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、", "条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。", "四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强", "直、畸形。", "肛门、直肠：未查。", "外生殖器：未查。", "专科检查", "第2页"]
2026-08-10 06:07:28,565 INFO     29 [qwen-vl-parser] page=1 text: 34 lines (bbox 0-33)
2026-08-10 06:07:28,566 INFO     29 [qwen-vl-parser] page=1 text: 34 sections
2026-08-10 06:07:28,803 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1363491, prompt_len=764
2026-08-10 06:07:30,343 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 06:07:30,344 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 06:07:30,362 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1363491, prompt_len=401
2026-08-10 06:07:36,259 INFO     29 [qwen-vl-parser] text API response (len=1001):
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：111", "住院号：", "科室：呼吸二病区", "第(1)次住院", "过敏史：无", "姓名：盖凤先", "性别：女", "年龄：67岁", "入院时间：2025-04-09 10:34", "职业：农民", "民族：回族", "婚姻：已婚", "记录时间：2025-04-09 10:34", "籍贯：河南省商丘市", "入院情况：有", "联系方式：15824782345", "现住址：河南省商丘市民权县伯党乡伯西村", "病史陈述者：本人", "可靠程度：供参", "委会", "考", "工作单位：-", "身份证号：412323195712211247", "联系人：白磊", "与患者关系：子", "联系人电话：15824782345", "主诉：胸闷、咳嗽、咳痰20余年，加重2天。", "现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，", "期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述", "症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动", "稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，", "门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠", "尚可，大小便无异常，体重无明显改变。", "既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血", "史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。", "个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟", "史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触", "史，无疫区接触史，无冶游史。", "婚姻史：25岁结婚，配偶健康。", "月经生育史：", "13", "3-5", "28-30", "50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，", "均健康。", "家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性", "疾病。", "第1页"]
2026-08-10 06:07:36,259 INFO     29 [qwen-vl-parser] page=2 text: 52 lines (bbox 34-85)
2026-08-10 06:07:36,260 INFO     29 [qwen-vl-parser] page=2 text: 52 sections
2026-08-10 06:07:36,391 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=440773, prompt_len=764
2026-08-10 06:07:36,933 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:36,933 INFO     29 [qwen-vl-text] LLM output (len=3999):
{
  "encounter_date": "2023-04-07",
  "prescription_type": "取药执行单",
  "prescriber": "陈音",
  "department": "呼吸危重三病区(门)",
  "diagnosis": null,
  "items": [
    {
      "drug_generic_name": "维生素AD滴剂",
      "drug_trade_name": "大伊可新",
      "drug_category": "西药",
      "dosage": "2000u",
      "frequency": "qd",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "头孢克肟颗粒",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "100mg",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "30",
      "notes": null
    },
    {
      "drug_generic_name": "阿奇霉素干混悬剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.25g",
      "frequency": "qd",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "三拗片",
      "drug_trade_name": null,
      "drug_category": "中成药",
      "dosage": "2片",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "富马酸酮替芬片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "1mg",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "6",
      "notes": null
    },
    {
      "drug_generic_name": "蒲地蓝消炎口服液",
      "drug_trade_name": null,
      "drug_category": "中成药",
      "dosage": "10ml",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "盐酸氨溴索口服溶液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "5ml",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "赖氨肌醇维B12口服溶液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10ml",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "3",
      "notes": null
    },
    {
      "drug_generic_name": "灭菌注射用水",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "20ml",
      "frequency": "bid",
      "route": "外用",
      "duration_days": null,
      "quantity": "4",
      "notes": null
    },
    {
      "drug_generic_name": "马来酸氯苯那敏注射液",
      "drug_trade_name": "扑尔敏针",
      "drug_category": "西药",
      "dosage": "20mg",
      "frequency": "bid",
      "route": "外用",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "地塞米松磷酸钠注射液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "bid",
      "route": "外用",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "消旋山莨菪碱注射液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "20mg",
      "frequency": "bid",
      "route": "外用",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "赖氨肌醇维B12口服溶液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10ml",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "复合维生素B片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "1片",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "100",
      "notes": null
    },
    {
      "drug_generic_name": "维生素",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": null,
      "frequency": null,
      "route": "口服",
      "duration_days": null,
      "quantity": "100",
      "notes": "OCR识别异常: 用维生素004/基"
    }
  ]
}
2026-08-10 06:07:36,933 INFO     29 [qwen-vl-text] Updated encounter_dates=[2023-04-07]
2026-08-10 06:07:36,935 INFO     29 [qwen-vl-text] coord API call start, page=35, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=920493, prompt_len=1608
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师", "药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音", "药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音", "药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音", "药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音", "药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音", "药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶", "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国", "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国", "药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚", "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚", "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚", "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚", "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚", "药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚", "药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚", "共70条 20条/页 < 1 2 3 4 > 前往 3 页"]

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
2026-08-10 06:07:37,826 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 06:07:37,827 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 06:07:37,833 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=440773, prompt_len=401
2026-08-10 06:07:39,786 INFO     29 [qwen-vl-parser] text API response (len=216):
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：", "住院号：", "肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、", "皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。", "辅助检查", "暂无。", "初步诊断", "1.哮喘（急性发作）", "2.慢性支气管炎", "住院医师：王贝贝", "主治医师：陈文宁", "主任医师：已签字", "第3页"]
2026-08-10 06:07:39,786 INFO     29 [qwen-vl-parser] page=3 text: 17 lines (bbox 86-102)
2026-08-10 06:07:39,787 INFO     29 [qwen-vl-parser] page=3 text: 17 sections
2026-08-10 06:07:40,077 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1369478, prompt_len=764
2026-08-10 06:07:41,713 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2023-08-15"
}
```
2026-08-10 06:07:41,713 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2023-08-15
2026-08-10 06:07:41,720 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1369478, prompt_len=401
2026-08-10 06:07:48,037 INFO     29 [qwen-vl-parser] text API response (len=1144):
["民权县人民医院", "肺功能检查报告", "病人ID:", "2023-08-1501", "性别：", "女", "高度：", "158 cm", "名：", "出生日期：", "1957/7/2", "体重：", "60 kg", "姓：", "年龄：", "66 years", "BMI：", "24.0 kg/m²", "体积", "流量", "体积", "时间[s]", "时间[s]", "单位", "预测值", "之前", "%预值", "沙丁胺醇", "(400", "%预值", "%变化", "ug)", "VC", "I", "(1)", "2.37", "1.66", "70%", "2.20", "93%", "+32.2%", "VC", "I", "(1)", "2.37", "1.66", "70%", "2.20", "93%", "+32.2%", "FEV1", "I", "(1)", "1.99", "0.88", "44%", "1.27", "64%", "+44.4%", "FEV1/FVC", "%", "(1)", "77", "53", "69%", "58", "75%", "+9.3%", "FEV1/VC", "%", "(1)", "77", "53", "69%", "58", "75%", "+9.3%", "PEF", "l/s", "(1)", "5.60", "2.06", "37%", "2.74", "49%", "+32.9%", "MEF75", "l/s", "(1)", "5.04", "0.97", "19%", "1.53", "30%", "+57.6%", "MEF50", "l/s", "(1)", "3.38", "0.49", "14%", "0.78", "23%", "+60.6%", "MEF25", "l/s", "(1)", "1.12", "0.22", "19%", "0.29", "26%", "+35.4%", "诊断意见：", "1.重度混合型通气功能障碍，小气道功能减低。", "2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。", "3.MVV:44%。建议定期复查。", "(1): ECCS 1993", "检测:2023/8/15", "-1-", "BTPS: 21.0 °C, 1013 hPa,", "50%", "医生：-", "Geratherm Respiratory GmbH", "www.geratherm-respiratory.com", "Blue Cherry V1.2.2.24"]
2026-08-10 06:07:48,038 INFO     29 [qwen-vl-parser] page=4 text: 126 lines (bbox 103-228)
2026-08-10 06:07:48,038 INFO     29 [qwen-vl-parser] page=4 text: 126 sections
2026-08-10 06:07:48,038 INFO     29 [qwen-vl-parser] parse_pdf done: 229 sections from 4 pages.
2026-08-10 06:07:48,056 INFO     29 Close text detector.
2026-08-10 06:07:48,537 INFO     29 Close text recognizer.
2026-08-10 06:07:48,967 INFO     29 Close recognizer.
2026-08-10 06:07:49,362 INFO     29 Close recognizer.
2026-08-10 06:07:50,270 INFO     29 [qwen-vl-text] coord API raw response (len=1800):
[
	{"text": "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "bbox": [18, 187, 600, 208]},
	{"text": "请输入药品内容,按回车键检索", "bbox": [18, 228, 137, 249]},
	{"text": "查询全部", "bbox": [215, 231, 267, 247]},
	{"text": "类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师", "bbox": [17, 261, 988, 284]},
	{"text": "药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音", "bbox": [17, 285, 988, 308]},
	{"text": "药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音", "bbox": [17, 309, 988, 332]},
	{"text": "药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音", "bbox": [17, 333, 988, 356]},
	{"text": "药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音", "bbox": [17, 357, 988, 380]},
	{"text": "药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音", "bbox": [17, 381, 988, 404]},
	{"text": "药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶", "bbox": [17, 405, 988, 428]},
	{"text": "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国", "bbox": [17, 429, 988, 452]},
	{"text": "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国", "bbox": [17, 453, 988, 476]},
	{"text": "药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚", "bbox": [17, 477, 988, 500]},
	{"text": "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚", "bbox": [17, 501, 988, 524]},
	{"text": "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚", "bbox": [17, 525, 988, 548]},
	{"text": "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚", "bbox": [17, 549, 988, 572]},
	{"text": "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚", "bbox": [17, 573, 988, 596]},
	{"text": "药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚", "bbox": [17, 597, 988, 620]},
	{"text": "药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚", "bbox": [17, 621, 988, 644]},
	{"text": "共70条 20条/页 < 1 2 3 4 > 前往 3 页", "bbox": [733, 651, 991, 670]}
]
2026-08-10 06:07:50,270 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=13.3s
2026-08-10 06:07:50,270 INFO     29 [qwen-vl-text] coord item[0]: text=集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告, bbox=[18, 187, 600, 208]
2026-08-10 06:07:50,270 INFO     29 [qwen-vl-text] coord item[1]: text=请输入药品内容,按回车键检索, bbox=[18, 228, 137, 249]
2026-08-10 06:07:50,270 INFO     29 [qwen-vl-text] coord item[2]: text=查询全部, bbox=[215, 231, 267, 247]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[3]: text=类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师, bbox=[17, 261, 988, 284]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[4]: text=药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音, bbox=[17, 285, 988, 308]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[5]: text=药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音, bbox=[17, 309, 988, 332]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[6]: text=药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音, bbox=[17, 333, 988, 356]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[7]: text=药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音, bbox=[17, 357, 988, 380]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[8]: text=药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音, bbox=[17, 381, 988, 404]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[9]: text=药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶, bbox=[17, 405, 988, 428]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[10]: text=药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国, bbox=[17, 429, 988, 452]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[11]: text=药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国, bbox=[17, 453, 988, 476]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[12]: text=药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚, bbox=[17, 477, 988, 500]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[13]: text=药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚, bbox=[17, 501, 988, 524]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[14]: text=药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚, bbox=[17, 525, 988, 548]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[15]: text=药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚, bbox=[17, 549, 988, 572]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[16]: text=药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚, bbox=[17, 573, 988, 596]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[17]: text=药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚, bbox=[17, 597, 988, 620]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[18]: text=药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚, bbox=[17, 621, 988, 644]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] coord item[19]: text=共70条 20条/页 < 1 2 3 4 > 前往 3 页, bbox=[733, 651, 991, 670]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] page=35 — 20/20 coords, api_time=13.3s
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] new_positions (20):
[[35, 15.155999999999999, 505.2, 111.265, 123.75999999999999], [35, 15.155999999999999, 115.354, 135.66, 148.155], [35, 181.03, 224.814, 137.445, 146.965], [35, 14.314, 831.896, 155.295, 168.98], [35, 14.314, 831.896, 169.575, 183.26], [35, 14.314, 831.896, 183.855, 197.54], [35, 14.314, 831.896, 198.135, 211.82], [35, 14.314, 831.896, 212.415, 226.1], [35, 14.314, 831.896, 226.695, 240.38], [35, 14.314, 831.896, 240.975, 254.66], [35, 14.314, 831.896, 255.255, 268.94], [35, 14.314, 831.896, 269.53499999999997, 283.21999999999997], [35, 14.314, 831.896, 283.815, 297.5], [35, 14.314, 831.896, 298.09499999999997, 311.78], [35, 14.314, 831.896, 312.375, 326.06], [35, 14.314, 831.896, 326.655, 340.34], [35, 14.314, 831.896, 340.935, 354.62], [35, 14.314, 831.896, 355.215, 368.9], [35, 14.314, 831.896, 369.495, 383.18], [35, 617.1859999999999, 834.422, 387.34499999999997, 398.65]]
2026-08-10 06:07:50,271 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=1, time=30.7s
2026-08-10 06:07:50,271 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:07:50,279 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:07:50,279 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 06:07:50,279 INFO     29 [qwen-vl-text] positions(19): [[36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:07:50,279 INFO     29 [qwen-vl-text] page grouping: [36], lines per page: [19]
2026-08-10 06:07:50,523 INFO     29 [qwen-vl-text] page=36, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 06:07:50,526 INFO     29 [qwen-vl-text] LLM extraction start, text_len=880
2026-08-10 06:07:50,526 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:50,526 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 1976, \"bbox_end\": 1994, \"encounter_dates\": [\"2026-02-12\"], \"department\": \"呼吸危重三病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n请输入药品内容，按回车键检索\n查询全部\n类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师\n药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国\n药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国\n药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚\n药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚\n药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚\n药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚\n药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚\n药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚\n药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚\n药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚\n药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚\n药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛\n药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛\n药品 乙1)美敏伪麻口服溶液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛\n共70条 20条/页 < 1 2 3 4 > 前往 3 页",
    "role": "user"
  }
]
2026-08-10 06:07:50,530 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:07:50.529+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "b531b82a948111f1bd9827cf206dfa2d": {"id": "b531b82a948111f1bd9827cf206dfa2d", "doc_id": "b40fb046948111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342023691, "task_type": "dataflow", "root_trace_id": "5de32dcc1c9241298e4a586d264050c9", "root_traceparent": "00-5de32dcc1c9241298e4a586d264050c9-8ca896b124088c1e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:07:51,130 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 06:07:51,130 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Parser:MedLink | outputs={"html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "json"}
2026-08-10 06:07:51,130 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 06:07:51,153 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:51,154 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 民权县人民医院\n[BBOX-1] 入院记录\n[BBOX-2] 姓名：\n[BBOX-3] 科室：呼吸二病区\n[BBOX-4] 床号：111\n[BBOX-5] 住院号：\n[BBOX-6] 体格检查\n[BBOX-7] T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg\n[BBOX-8] 发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧\n[BBOX-9] 虑，走入病房，检查合作。\n[BBOX-10] 皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，\n[BBOX-11] 无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。\n[BBOX-12] 淋巴结：全身浅表淋巴结无肿大。\n[BBOX-13] 头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔\n[BBOX-14] 2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦\n[BBOX-15] 无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、\n[BBOX-16] 红肿，声音无嘶哑。\n[BBOX-17] 颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流\n[BBOX-18] 征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿\n[BBOX-19] 大。\n[BBOX-20] 胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、\n[BBOX-21] 皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。\n[BBOX-22] 肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发\n[BBOX-23] 感。叩诊音呈清音。呼吸音异常干性啰音。\n[BBOX-24] 心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所\n[BBOX-25] 示。心率82次/分，心律齐。\n[BBOX-26] 腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、\n[BBOX-27] 条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。\n[BBOX-28] 四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强\n[BBOX-29] 直、畸形。\n[BBOX-30] 肛门、直肠：未查。\n[BBOX-31] 外生殖器：未查。\n[BBOX-32] 专科检查\n[BBOX-33] 第2页\n[BBOX-34] 民权县人民医院\n[BBOX-35] 入院记录\n[BBOX-36] 姓名：\n[BBOX-37] 科室：呼吸二病区\n[BBOX-38] 床号：111\n[BBOX-39] 住院号：\n[BBOX-40] 科室：呼吸二病区\n[BBOX-41] 第(1)次住院\n[BBOX-42] 过敏史：无\n[BBOX-43] 姓名：盖凤先\n[BBOX-44] 性别：女\n[BBOX-45] 年龄：67岁\n[BBOX-46] 入院时间：2025-04-09 10:34\n[BBOX-47] 职业：农民\n[BBOX-48] 民族：回族\n[BBOX-49] 婚姻：已婚\n[BBOX-50] 记录时间：2025-04-09 10:34\n[BBOX-51] 籍贯：河南省商丘市\n[BBOX-52] 入院情况：有\n[BBOX-53] 联系方式：15824782345\n[BBOX-54] 现住址：河南省商丘市民权县伯党乡伯西村\n[BBOX-55] 病史陈述者：本人\n[BBOX-56] 可靠程度：供参\n[BBOX-57] 委会\n[BBOX-58] 考\n[BBOX-59] 工作单位：-\n[BBOX-60] 身份证号：412323195712211247\n[BBOX-61] 联系人：白磊\n[BBOX-62] 与患者关系：子\n[BBOX-63] 联系人电话：15824782345\n[BBOX-64] 主诉：胸闷、咳嗽、咳痰20余年，加重2天。\n[BBOX-65] 现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，\n[BBOX-66] 期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述\n[BBOX-67] 症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动\n[BBOX-68] 稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，\n[BBOX-69] 门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠\n[BBOX-70] 尚可，大小便无异常，体重无明显改变。\n[BBOX-71] 既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血\n[BBOX-72] 史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。\n[BBOX-73] 个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟\n[BBOX-74] 史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触\n[BBOX-75] 史，无疫区接触史，无冶游史。\n[BBOX-76] 婚姻史：25岁结婚，配偶健康。\n[BBOX-77] 月经生育史：\n[BBOX-78] 13\n[BBOX-79] 3-5\n[BBOX-80] 28-30\n[BBOX-81] 50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，\n[BBOX-82] 均健康。\n[BBOX-83] 家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性\n[BBOX-84] 疾病。\n[BBOX-85] 第1页\n[BBOX-86] 民权县人民医院\n[BBOX-87] 入院记录\n[BBOX-88] 姓名：\n[BBOX-89] 科室：呼吸二病区\n[BBOX-90] 床号：\n[BBOX-91] 住院号：\n[BBOX-92] 肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、\n[BBOX-93] 皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。\n[BBOX-94] 辅助检查\n[BBOX-95] 暂无。\n[BBOX-96] 初步诊断\n[BBOX-97] 1.哮喘（急性发作）\n[BBOX-98] 2.慢性支气管炎\n[BBOX-99] 住院医师：王贝贝\n[BBOX-100] 主治医师：陈文宁\n[BBOX-101] 主任医师：已签字\n[BBOX-102] 第3页\n[BBOX-103] 民权县人民医院\n[BBOX-104] 肺功能检查报告\n[BBOX-105] 病人ID:\n[BBOX-106] 2023-08-1501\n[BBOX-107] 性别：\n[BBOX-108] 女\n[BBOX-109] 高度：\n[BBOX-110] 158 cm\n[BBOX-111] 名：\n[BBOX-112] 出生日期：\n[BBOX-113] 1957/7/2\n[BBOX-114] 体重：\n[BBOX-115] 60 kg\n[BBOX-116] 姓：\n[BBOX-117] 年龄：\n[BBOX-118] 66 years\n[BBOX-119] BMI：\n[BBOX-120] 24.0 kg/m²\n[BBOX-121] 体积\n[BBOX-122] 流量\n[BBOX-123] 体积\n[BBOX-124] 时间[s]\n[BBOX-125] 时间[s]\n[BBOX-126] 单位\n[BBOX-127] 预测值\n[BBOX-128] 之前\n[BBOX-129] %预值\n[BBOX-130] 沙丁胺醇\n[BBOX-131] (400\n[BBOX-132] %预值\n[BBOX-133] %变化\n[BBOX-134] ug)\n[BBOX-135] VC\n[BBOX-136] I\n[BBOX-137] (1)\n[BBOX-138] 2.37\n[BBOX-139] 1.66\n[BBOX-140] 70%\n[BBOX-141] 2.20\n[BBOX-142] 93%\n[BBOX-143] +32.2%\n[BBOX-144] VC\n[BBOX-145] I\n[BBOX-146] (1)\n[BBOX-147] 2.37\n[BBOX-148] 1.66\n[BBOX-149] 70%\n[BBOX-150] 2.20\n[BBOX-151] 93%\n[BBOX-152] +32.2%\n[BBOX-153] FEV1\n[BBOX-154] I\n[BBOX-155] (1)\n[BBOX-156] 1.99\n[BBOX-157] 0.88\n[BBOX-158] 44%\n[BBOX-159] 1.27\n[BBOX-160] 64%\n[BBOX-161] +44.4%\n[BBOX-162] FEV1/FVC\n[BBOX-163] %\n[BBOX-164] (1)\n[BBOX-165] 77\n[BBOX-166] 53\n[BBOX-167] 69%\n[BBOX-168] 58\n[BBOX-169] 75%\n[BBOX-170] +9.3%\n[BBOX-171] FEV1/VC\n[BBOX-172] %\n[BBOX-173] (1)\n[BBOX-174] 77\n[BBOX-175] 53\n[BBOX-176] 69%\n[BBOX-177] 58\n[BBOX-178] 75%\n[BBOX-179] +9.3%\n[BBOX-180] PEF\n[BBOX-181] l/s\n[BBOX-182] (1)\n[BBOX-183] 5.60\n[BBOX-184] 2.06\n[BBOX-185] 37%\n[BBOX-186] 2.74\n[BBOX-187] 49%\n[BBOX-188] +32.9%\n[BBOX-189] MEF75\n[BBOX-190] l/s\n[BBOX-191] (1)\n[BBOX-192] 5.04\n[BBOX-193] 0.97\n[BBOX-194] 19%\n[BBOX-195] 1.53\n[BBOX-196] 30%\n[BBOX-197] +57.6%\n[BBOX-198] MEF50\n[BBOX-199] l/s\n[BBOX-200] (1)\n[BBOX-201] 3.38\n[BBOX-202] 0.49\n[BBOX-203] 14%\n[BBOX-204] 0.78\n[BBOX-205] 23%\n[BBOX-206] +60.6%\n[BBOX-207] MEF25\n[BBOX-208] l/s\n[BBOX-209] (1)\n[BBOX-210] 1.12\n[BBOX-211] 0.22\n[BBOX-212] 19%\n[BBOX-213] 0.29\n[BBOX-214] 26%\n[BBOX-215] +35.4%\n[BBOX-216] 诊断意见：\n[BBOX-217] 1.重度混合型通气功能障碍，小气道功能减低。\n[BBOX-218] 2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。\n[BBOX-219] 3.MVV:44%。建议定期复查。\n[BBOX-220] (1): ECCS 1993\n[BBOX-221] 检测:2023/8/15\n[BBOX-222] -1-\n[BBOX-223] BTPS: 21.0 °C, 1013 hPa,\n[BBOX-224] 50%\n[BBOX-225] 医生：-\n[BBOX-226] Geratherm Respiratory GmbH\n[BBOX-227] www.geratherm-respiratory.com\n[BBOX-228] Blue Cherry V1.2.2.24"
  }
]
2026-08-10 06:07:55,243 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:55,274 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'ExaminationReport': 1}
2026-08-10 06:07:55,282 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 06:07:55,282 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks": "2 items, types={'AdmissionRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 06:07:55,282 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 06:07:55,283 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Admission': 1, 'chunks_Examination': 1}
2026-08-10 06:07:55,303 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 06:07:55,303 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | ChunkRouter:Router | outputs={"html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks": "2 items, types={'AdmissionRecord': 1, 'ExaminationReport': 1}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:07:55,303 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 06:07:55,310 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:55,310 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:07:56,113 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:56,121 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 06:07:56,121 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:07:56,121 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 06:07:56,126 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:56,126 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:07:56,718 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:56,723 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 06:07:56,723 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:07:56,723 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 06:07:56,727 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:56,727 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:07:57,319 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:57,323 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 06:07:57,324 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:07:57,324 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 06:07:57,329 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:57,329 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:07:58,159 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:58,166 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 06:07:58,166 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:07:58,166 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 06:07:58,172 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:58,172 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:07:58,717 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:58,722 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 06:07:58,722 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:07:58,722 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 06:07:58,728 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:58,728 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:07:59,224 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:59,230 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 06:07:59,230 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:07:59,230 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 06:07:59,236 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:07:59,237 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:07:59,237 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 06:07:59,237 INFO     29 [qwen-vl-text] positions(103): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:07:59,237 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2], lines per page: [34, 52, 17]
2026-08-10 06:07:59,426 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:07:59,632 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:07:59,770 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:07:59,771 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1743
2026-08-10 06:07:59,771 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:07:59,771 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 102, \"encounter_dates\": [\"2025-04-09\"], \"department\": \"呼吸二病区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "民权县人民医院\n入院记录\n姓名：\n科室：呼吸二病区\n床号：111\n住院号：\n体格检查\nT:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg\n发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧\n虑，走入病房，检查合作。\n皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，\n无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。\n淋巴结：全身浅表淋巴结无肿大。\n头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔\n2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦\n无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、\n红肿，声音无嘶哑。\n颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流\n征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿\n大。\n胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、\n皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。\n肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发\n感。叩诊音呈清音。呼吸音异常干性啰音。\n心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所\n示。心率82次/分，心律齐。\n腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、\n条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。\n四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强\n直、畸形。\n肛门、直肠：未查。\n外生殖器：未查。\n专科检查\n第2页\n民权县人民医院\n入院记录\n姓名：\n科室：呼吸二病区\n床号：111\n住院号：\n科室：呼吸二病区\n第(1)次住院\n过敏史：无\n姓名：盖凤先\n性别：女\n年龄：67岁\n入院时间：2025-04-09 10:34\n职业：农民\n民族：回族\n婚姻：已婚\n记录时间：2025-04-09 10:34\n籍贯：河南省商丘市\n入院情况：有\n联系方式：15824782345\n现住址：河南省商丘市民权县伯党乡伯西村\n病史陈述者：本人\n可靠程度：供参\n委会\n考\n工作单位：-\n身份证号：412323195712211247\n联系人：白磊\n与患者关系：子\n联系人电话：15824782345\n主诉：胸闷、咳嗽、咳痰20余年，加重2天。\n现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，\n期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述\n症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动\n稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，\n门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠\n尚可，大小便无异常，体重无明显改变。\n既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血\n史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。\n个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟\n史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触\n史，无疫区接触史，无冶游史。\n婚姻史：25岁结婚，配偶健康。\n月经生育史：\n13\n3-5\n28-30\n50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，\n均健康。\n家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性\n疾病。\n第1页\n民权县人民医院\n入院记录\n姓名：\n科室：呼吸二病区\n床号：\n住院号：\n肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、\n皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。\n辅助检查\n暂无。\n初步诊断\n1.哮喘（急性发作）\n2.慢性支气管炎\n住院医师：王贝贝\n主治医师：陈文宁\n主任医师：已签字\n第3页",
    "role": "user"
  }
]
2026-08-10 06:08:05,213 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:08:05,213 INFO     29 [qwen-vl-text] LLM output (len=3478):
{
  "encounter_date": "2022-05-09",
  "prescription_type": "取药执行单",
  "prescriber": null,
  "department": "呼吸危重三病区(门)",
  "diagnosis": null,
  "items": [
    {
      "drug_generic_name": "盐酸氨溴索口服溶液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10ml",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "3",
      "notes": null
    },
    {
      "drug_generic_name": "赖氨肌醇维B12口服溶液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "20ml",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "4",
      "notes": null
    },
    {
      "drug_generic_name": "灭菌注射用水",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "20mg",
      "frequency": "bid",
      "route": "外用",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "马来酸氯苯那敏注射液",
      "drug_trade_name": "扑尔敏针",
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "bid",
      "route": "外用",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "地塞米松磷酸钠注射液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "20mg",
      "frequency": "bid",
      "route": "外用",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "消旋山莨菪碱注射液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10ml",
      "frequency": "bid",
      "route": "外用",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "赖氨肌醇维B12口服溶液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "1片",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "100",
      "notes": null
    },
    {
      "drug_generic_name": "复合维生素B片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "5mg",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "100",
      "notes": null
    },
    {
      "drug_generic_name": "维生素B2片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "50mg",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "头孢克肟颗粒",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10ml",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "金振口服液",
      "drug_trade_name": null,
      "drug_category": "中成药",
      "dosage": "3g",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "小儿氨酚黄那敏颗粒",
      "drug_trade_name": "盖克",
      "drug_category": "西药",
      "dosage": "4ml",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "美敏伪麻口服溶液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "5ml",
      "frequency": "qid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    }
  ]
}
2026-08-10 06:08:05,213 INFO     29 [qwen-vl-text] Updated encounter_dates=[2022-05-09]
2026-08-10 06:08:05,216 INFO     29 [qwen-vl-text] coord API call start, page=36, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1030200, prompt_len=1550
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容，按回车键检索", "查询全部", "类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师", "药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国", "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国", "药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚", "药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚", "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚", "药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚", "药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚", "药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚", "药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚", "药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛", "药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛", "药品 乙1)美敏伪麻口服溶液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛", "共70条 20条/页 < 1 2 3 4 > 前往 3 页"]

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
2026-08-10 06:08:16,144 INFO     29 [qwen-vl-text] coord API raw response (len=1714):
```json
[
	{"text": "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "bbox": [19, 148, 587, 168]},
	{"text": "请输入药品内容，按回车键检索", "bbox": [19, 190, 135, 210]},
	{"text": "查询全部", "bbox": [214, 193, 262, 207]},
	{"text": "类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师", "bbox": [17, 224, 969, 246]},
	{"text": "药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国", "bbox": [17, 263, 969, 285]},
	{"text": "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国", "bbox": [17, 285, 969, 307]},
	{"text": "药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚", "bbox": [17, 307, 969, 329]},
	{"text": "药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "bbox": [17, 329, 969, 351]},
	{"text": "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚", "bbox": [17, 351, 969, 373]},
	{"text": "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "bbox": [17, 373, 969, 395]},
	{"text": "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚", "bbox": [17, 395, 969, 417]},
	{"text": "药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚", "bbox": [17, 417, 969, 439]},
	{"text": "药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚", "bbox": [17, 439, 969, 461]},
	{"text": "药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚", "bbox": [17, 461, 969, 483]},
	{"text": "药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚", "bbox": [17, 483, 969, 505]},
	{"text": "药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛", "bbox": [17, 505, 969, 527]},
	{"text": "药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛", "bbox": [17, 527, 969, 549]},
	{"text": "药品 乙1)美敏伪麻口服溶液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛", "bbox": [17, 549, 969, 571]},
	{"text": "共70条 20条/页 < 1 2 3 4 > 前往 3 页", "bbox": [719, 621, 979, 639]}
]
```
2026-08-10 06:08:16,144 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=10.9s
2026-08-10 06:08:16,144 INFO     29 [qwen-vl-text] coord item[0]: text=集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告, bbox=[19, 148, 587, 168]
2026-08-10 06:08:16,144 INFO     29 [qwen-vl-text] coord item[1]: text=请输入药品内容，按回车键检索, bbox=[19, 190, 135, 210]
2026-08-10 06:08:16,144 INFO     29 [qwen-vl-text] coord item[2]: text=查询全部, bbox=[214, 193, 262, 207]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[3]: text=类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师, bbox=[17, 224, 969, 246]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[4]: text=药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国, bbox=[17, 263, 969, 285]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[5]: text=药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国, bbox=[17, 285, 969, 307]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[6]: text=药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚, bbox=[17, 307, 969, 329]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[7]: text=药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚, bbox=[17, 329, 969, 351]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[8]: text=药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚, bbox=[17, 351, 969, 373]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[9]: text=药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚, bbox=[17, 373, 969, 395]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[10]: text=药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚, bbox=[17, 395, 969, 417]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[11]: text=药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚, bbox=[17, 417, 969, 439]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[12]: text=药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚, bbox=[17, 439, 969, 461]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[13]: text=药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚, bbox=[17, 461, 969, 483]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[14]: text=药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚, bbox=[17, 483, 969, 505]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[15]: text=药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛, bbox=[17, 505, 969, 527]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[16]: text=药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛, bbox=[17, 527, 969, 549]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[17]: text=药品 乙1)美敏伪麻口服溶液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛, bbox=[17, 549, 969, 571]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] coord item[18]: text=共70条 20条/页 < 1 2 3 4 > 前往 3 页, bbox=[719, 621, 979, 639]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] page=36 — 19/19 coords, api_time=10.9s
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] new_positions (19):
[[36, 15.998, 494.25399999999996, 88.06, 99.96], [36, 15.998, 113.67, 113.05, 124.94999999999999], [36, 180.188, 220.60399999999998, 114.835, 123.16499999999999], [36, 14.314, 815.898, 133.28, 146.37], [36, 14.314, 815.898, 156.48499999999999, 169.575], [36, 14.314, 815.898, 169.575, 182.665], [36, 14.314, 815.898, 182.665, 195.755], [36, 14.314, 815.898, 195.755, 208.845], [36, 14.314, 815.898, 208.845, 221.935], [36, 14.314, 815.898, 221.935, 235.02499999999998], [36, 14.314, 815.898, 235.02499999999998, 248.11499999999998], [36, 14.314, 815.898, 248.11499999999998, 261.205], [36, 14.314, 815.898, 261.205, 274.295], [36, 14.314, 815.898, 274.295, 287.385], [36, 14.314, 815.898, 287.385, 300.47499999999997], [36, 14.314, 815.898, 300.47499999999997, 313.565], [36, 14.314, 815.898, 313.565, 326.655], [36, 14.314, 815.898, 326.655, 339.745], [36, 605.398, 824.318, 369.495, 380.205]]
2026-08-10 06:08:16,145 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=25.9s
2026-08-10 06:08:16,145 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:08:16,146 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:08:16,147 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 06:08:16,147 INFO     29 [qwen-vl-text] positions(26): [[37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:08:16,147 INFO     29 [qwen-vl-text] page grouping: [37], lines per page: [26]
2026-08-10 06:08:16,363 INFO     29 [qwen-vl-text] page=37, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 06:08:16,365 INFO     29 [qwen-vl-text] LLM extraction start, text_len=718
2026-08-10 06:08:16,365 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:08:16,365 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 1998, \"bbox_end\": 2023, \"encounter_dates\": [\"2026-02-12\"], \"department\": \"呼吸危重三病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n请输入药品内容,按回车键检索\n查询全部\n类型 组 药品名称(规格)\n药品 甲)(小儿)双黄连口服液(基)\n药品 (盖克)小儿氨酚黄那敏颗粒\n药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)\n药品 蒲地蓝消炎口服液\n药品 复方氨酚甲麻口服液\n药品 (盖克)小儿氨酚黄那敏颗粒\n药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)\n药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)\n药品 右旋糖酐铁颗粒\n药品 盐酸氨卓斯丁滴眼液\n用法 频率 实际用量 总量 开立时间 开立医师\n口服 tid 10ml 1 2022-03-26 19:51:46 谭真真\n口服 tid 6g 2 2022-03-26 19:51:18 谭真真\n口服(继续 用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真\n口服 bid 10ml 1 2022-03-26 19:51:18 谭真真\n口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴\n口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴\n口服(继续 用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴\n压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅\n口服 tid 1袋 80 2021-09-28 15:12:34 党建华\n滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳\n共70条 20条/页 < 1 2 3 4 > 前往 4 页",
    "role": "user"
  }
]
2026-08-10 06:08:16,370 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:08:16,370 INFO     29 [qwen-vl-text] LLM output (len=2130):
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
2026-08-10 06:08:16,370 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-09]
2026-08-10 06:08:16,372 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1493212, prompt_len=1448
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
2026-08-10 06:08:30,211 INFO     29 [qwen-vl-text] coord API raw response (len=2228):
[
	{"text": "民权县人民医院", "bbox": [408, 45, 594, 65]},
	{"text": "入院记录", "bbox": [423, 79, 571, 99]},
	{"text": "姓名：", "bbox": [120, 121, 168, 137]},
	{"text": "科室：呼吸二病区", "bbox": [285, 117, 450, 134]},
	{"text": "床号：111", "bbox": [547, 114, 639, 130]},
	{"text": "住院号：", "bbox": [704, 113, 772, 128]},
	{"text": "体格检查", "bbox": [442, 157, 554, 173]},
	{"text": "T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg", "bbox": [162, 184, 607, 204]},
	{"text": "发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧", "bbox": [163, 207, 887, 235]},
	{"text": "虑，走入病房，检查合作。", "bbox": [117, 243, 350, 263]},
	{"text": "皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，", "bbox": [164, 261, 875, 290]},
	{"text": "无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。", "bbox": [119, 293, 702, 319]},
	{"text": "淋巴结：全身浅表淋巴结无肿大。", "bbox": [165, 326, 461, 346]},
	{"text": "头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔", "bbox": [166, 348, 887, 374]},
	{"text": "2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦", "bbox": [120, 376, 887, 402]},
	{"text": "无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、", "bbox": [122, 404, 893, 430]},
	{"text": "红肿，声音无嘶哑。", "bbox": [123, 441, 294, 458]},
	{"text": "颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流", "bbox": [170, 460, 884, 486]},
	{"text": "征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿", "bbox": [124, 487, 884, 513]},
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
	{"text": "外生殖器：未查。", "bbox": [176, 857, 328, 873]},
	{"text": "专科检查", "bbox": [457, 882, 567, 899]},
	{"text": "第2页", "bbox": [483, 933, 543, 946]}
]
2026-08-10 06:08:30,211 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=13.8s
2026-08-10 06:08:30,211 INFO     29 [qwen-vl-text] coord item[0]: text=民权县人民医院, bbox=[408, 45, 594, 65]
2026-08-10 06:08:30,211 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[423, 79, 571, 99]
2026-08-10 06:08:30,211 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[120, 121, 168, 137]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[3]: text=科室：呼吸二病区, bbox=[285, 117, 450, 134]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[4]: text=床号：111, bbox=[547, 114, 639, 130]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[704, 113, 772, 128]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[6]: text=体格检查, bbox=[442, 157, 554, 173]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[7]: text=T:36.4℃ P:82次/分 R:30次/分 BP:120/60mmHg, bbox=[162, 184, 607, 204]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[8]: text=发育正常，营养中等，神志清晰，精神差，体位主动，面容呈急性病容，表情忧, bbox=[163, 207, 887, 235]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[9]: text=虑，走入病房，检查合作。, bbox=[117, 243, 350, 263]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[10]: text=皮肤：色泽正常，温度和湿度正常，弹性正常，毛发分布正常。无水肿，无皮疹，, bbox=[164, 261, 875, 290]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[11]: text=无淤点、紫癜，无瘢痕，无溃疡，无皮下结节，无蜘蛛痣、肝掌。, bbox=[119, 293, 702, 319]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[12]: text=淋巴结：全身浅表淋巴结无肿大。, bbox=[165, 326, 461, 346]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[13]: text=头部：头颅正常，无压痛、异常隆起、肿块、凹陷，结膜正常巩膜无黄染。左眼瞳孔, bbox=[166, 348, 887, 374]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[14]: text=2.5mm，对光反射正常，右眼瞳孔2.5mm，对光反射正常，听力尚可。外鼻无畸形，鼻窦, bbox=[120, 376, 887, 402]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[15]: text=无压痛。口唇红润，舌苔正常，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充血、, bbox=[122, 404, 893, 430]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[16]: text=红肿，声音无嘶哑。, bbox=[123, 441, 294, 458]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[17]: text=颈部：两侧对称，无包块，无强直，颈静脉正常，无抵抗感。气管正中。肝颈静脉回流, bbox=[170, 460, 884, 486]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[18]: text=征阴性。颈动脉搏动左侧正常，右侧正常。双侧甲状腺正常对称，左侧无肿大，右侧无肿, bbox=[124, 487, 884, 513]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[19]: text=大。, bbox=[124, 525, 154, 540]
2026-08-10 06:08:30,212 INFO     29 [qwen-vl-text] coord item[20]: text=胸部：胸廓呈桶状胸。双侧乳房对称，左侧正常，右侧正常。胸壁无静脉曲张或充盈、, bbox=[172, 540, 895, 568]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[21]: text=皮下气肿、胸壁压痛、肋间隙回缩、肋间隙膨隆。, bbox=[125, 574, 555, 596]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[22]: text=肺：双侧呼吸运动正常，肋间隙增宽。双侧语颤正常。双侧无胸膜摩擦感、皮下捻发, bbox=[173, 597, 889, 623]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[23]: text=感。叩诊音呈清音。呼吸音异常干性啰音。, bbox=[126, 630, 502, 652]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[24]: text=心：心尖搏动不可明视。心尖搏动正常，无震颤，无心包摩擦感。相对浊音界如图所, bbox=[174, 653, 890, 679]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[25]: text=示。心率82次/分，心律齐。, bbox=[127, 688, 374, 707]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[26]: text=腹部：形状对称，平坦，无胃型、肠型，无胃蠕动波、肠蠕动波，无皮疹、色素、, bbox=[174, 708, 878, 734]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[27]: text=条纹、瘢痕、腹壁静脉曲张。腹柔软，无压痛、反跳痛。, bbox=[128, 740, 624, 762]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[28]: text=四肢：无畸形，双侧下肢对称无水肿。关节无红肿、疼痛、压痛、积液、脱臼、强, bbox=[175, 763, 892, 790]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[29]: text=直、畸形。, bbox=[130, 802, 217, 818]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[30]: text=肛门、直肠：未查。, bbox=[176, 829, 343, 847]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[31]: text=外生殖器：未查。, bbox=[176, 857, 328, 873]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[32]: text=专科检查, bbox=[457, 882, 567, 899]
2026-08-10 06:08:30,213 INFO     29 [qwen-vl-text] coord item[33]: text=第2页, bbox=[483, 933, 543, 946]
2026-08-10 06:08:30,214 INFO     29 [qwen-vl-text] page=0 — 34/34 coords, api_time=13.8s
2026-08-10 06:08:30,220 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1781058, prompt_len=1613
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共52行）
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：111", "住院号：", "科室：呼吸二病区", "第(1)次住院", "过敏史：无", "姓名：盖凤先", "性别：女", "年龄：67岁", "入院时间：2025-04-09 10:34", "职业：农民", "民族：回族", "婚姻：已婚", "记录时间：2025-04-09 10:34", "籍贯：河南省商丘市", "入院情况：有", "联系方式：15824782345", "现住址：河南省商丘市民权县伯党乡伯西村", "病史陈述者：本人", "可靠程度：供参", "委会", "考", "工作单位：-", "身份证号：412323195712211247", "联系人：白磊", "与患者关系：子", "联系人电话：15824782345", "主诉：胸闷、咳嗽、咳痰20余年，加重2天。", "现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，", "期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述", "症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动", "稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，", "门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠", "尚可，大小便无异常，体重无明显改变。", "既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血", "史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。", "个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟", "史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触", "史，无疫区接触史，无冶游史。", "婚姻史：25岁结婚，配偶健康。", "月经生育史：", "13", "3-5", "28-30", "50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，", "均健康。", "家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性", "疾病。", "第1页"]

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
2026-08-10 06:08:49,610 INFO     29 [qwen-vl-text] coord API raw response (len=3132):
[
	{"text": "民权县人民医院", "bbox": [407, 48, 593, 69]},
	{"text": "入院记录", "bbox": [421, 85, 569, 105]},
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
	{"text": "入院时间：2025-04-09 10:34", "bbox": [587, 189, 850, 204]},
	{"text": "职业：农民", "bbox": [117, 215, 217, 231]},
	{"text": "民族：回族", "bbox": [330, 214, 434, 230]},
	{"text": "婚姻：已婚", "bbox": [455, 214, 556, 230]},
	{"text": "记录时间：2025-04-09 10:34", "bbox": [587, 213, 850, 229]},
	{"text": "籍贯：河南省商丘市", "bbox": [117, 240, 294, 256]},
	{"text": "入院情况：有", "bbox": [434, 239, 555, 255]},
	{"text": "联系方式：15824782345", "bbox": [587, 238, 804, 254]},
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
	{"text": "期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述", "bbox": [117, 443, 876, 460]},
	{"text": "症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动", "bbox": [117, 470, 876, 487]},
	{"text": "稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，", "bbox": [117, 497, 884, 514]},
	{"text": "门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠", "bbox": [117, 524, 879, 541]},
	{"text": "尚可，大小便无异常，体重无明显改变。", "bbox": [117, 553, 472, 569]},
	{"text": "既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血", "bbox": [167, 580, 880, 597]},
	{"text": "史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。", "bbox": [117, 608, 742, 625]},
	{"text": "个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟", "bbox": [167, 636, 882, 653]},
	{"text": "史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触", "bbox": [117, 664, 882, 680]},
	{"text": "史，无疫区接触史，无冶游史。", "bbox": [117, 692, 395, 708]},
	{"text": "婚姻史：25岁结婚，配偶健康。", "bbox": [167, 720, 449, 736]},
	{"text": "月经生育史：", "bbox": [167, 756, 278, 772]},
	{"text": "13", "bbox": [320, 760, 338, 775]},
	{"text": "3-5", "bbox": [342, 757, 369, 770]},
	{"text": "28-30", "bbox": [334, 770, 377, 782]},
	{"text": "50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，", "bbox": [377, 754, 891, 772]},
	{"text": "均健康。", "bbox": [122, 805, 192, 821]},
	{"text": "家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性", "bbox": [162, 831, 886, 848]},
	{"text": "疾病。", "bbox": [122, 860, 173, 876]},
	{"text": "第1页", "bbox": [475, 935, 537, 948]}
]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord API: raw_items=52, valid_items=52, elapsed=19.4s
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[0]: text=民权县人民医院, bbox=[407, 48, 593, 69]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[421, 85, 569, 105]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[120, 122, 167, 138]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[3]: text=科室：呼吸二病区, bbox=[285, 122, 448, 138]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[4]: text=床号：111, bbox=[545, 122, 637, 137]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[702, 121, 770, 137]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[6]: text=科室：呼吸二病区, bbox=[117, 165, 278, 181]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[7]: text=第(1)次住院, bbox=[330, 165, 442, 181]
2026-08-10 06:08:49,611 INFO     29 [qwen-vl-text] coord item[8]: text=过敏史：无, bbox=[587, 164, 692, 180]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[9]: text=姓名：盖凤先, bbox=[117, 190, 227, 206]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[10]: text=性别：女, bbox=[330, 190, 413, 206]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[11]: text=年龄：67岁, bbox=[455, 190, 555, 206]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[12]: text=入院时间：2025-04-09 10:34, bbox=[587, 189, 850, 204]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[13]: text=职业：农民, bbox=[117, 215, 217, 231]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[14]: text=民族：回族, bbox=[330, 214, 434, 230]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[15]: text=婚姻：已婚, bbox=[455, 214, 556, 230]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[16]: text=记录时间：2025-04-09 10:34, bbox=[587, 213, 850, 229]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[17]: text=籍贯：河南省商丘市, bbox=[117, 240, 294, 256]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[18]: text=入院情况：有, bbox=[434, 239, 555, 255]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[19]: text=联系方式：15824782345, bbox=[587, 238, 804, 254]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[20]: text=现住址：河南省商丘市民权县伯党乡伯西村, bbox=[117, 265, 498, 281]
2026-08-10 06:08:49,612 INFO     29 [qwen-vl-text] coord item[21]: text=病史陈述者：本人, bbox=[509, 273, 670, 290]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[22]: text=可靠程度：供参, bbox=[717, 263, 876, 279]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[23]: text=委会, bbox=[117, 285, 157, 301]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[24]: text=考, bbox=[717, 282, 737, 298]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[25]: text=工作单位：-, bbox=[117, 309, 229, 325]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[26]: text=身份证号：412323195712211247, bbox=[509, 308, 794, 324]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[27]: text=联系人：白磊, bbox=[117, 335, 238, 351]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[28]: text=与患者关系：子, bbox=[334, 335, 475, 351]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[29]: text=联系人电话：15824782345, bbox=[619, 334, 855, 350]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[30]: text=主诉：胸闷、咳嗽、咳痰20余年，加重2天。, bbox=[167, 362, 575, 378]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[31]: text=现病史：20余年前受凉出现胸闷，伴阵发性干咳，偶有咳痰，多于活动后及闻及冷空气、刺激性气味后加重，无呼吸困难、大汗淋漓，无心悸、胸痛，无恶心、呕吐等症状，, bbox=[117, 389, 884, 405]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[32]: text=期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述, bbox=[117, 443, 876, 460]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[33]: text=症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动, bbox=[117, 470, 876, 487]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[34]: text=稍受限，活动耐受力较前明显下降，吸入药物控制控制欠佳，为求进一步治疗于我院就诊，, bbox=[117, 497, 884, 514]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[35]: text=门诊以“支气管哮喘合并感染、肺结节”收入我科。发病来，患者神志清，精神差，饮食睡眠, bbox=[117, 524, 879, 541]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[36]: text=尚可，大小便无异常，体重无明显改变。, bbox=[117, 553, 472, 569]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[37]: text=既往史：平素体健。，无肝炎、结核类传染病史，无手术史，无外伤史，无输血, bbox=[167, 580, 880, 597]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[38]: text=史，无献血史，无食物过敏史，无药物过敏史。预防接种随社会进行。, bbox=[117, 608, 742, 625]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[39]: text=个人史：生于河南省商丘市民权县，无长期外地居住史。无特殊生活习惯，无吸烟, bbox=[167, 636, 882, 653]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[40]: text=史。无饮酒嗜好，无药物嗜好，无工业毒物、粉尘、放射性物质接触史，无有毒性物质接触, bbox=[117, 664, 882, 680]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[41]: text=史，无疫区接触史，无冶游史。, bbox=[117, 692, 395, 708]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[42]: text=婚姻史：25岁结婚，配偶健康。, bbox=[167, 720, 449, 736]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[43]: text=月经生育史：, bbox=[167, 756, 278, 772]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[44]: text=13, bbox=[320, 760, 338, 775]
2026-08-10 06:08:49,613 INFO     29 [qwen-vl-text] coord item[45]: text=3-5, bbox=[342, 757, 369, 770]
2026-08-10 06:08:49,614 INFO     29 [qwen-vl-text] coord item[46]: text=28-30, bbox=[334, 770, 377, 782]
2026-08-10 06:08:49,614 INFO     29 [qwen-vl-text] coord item[47]: text=50，月经规律，量中等，色，无痛经。孕3产3，育1子2女，, bbox=[377, 754, 891, 772]
2026-08-10 06:08:49,614 INFO     29 [qwen-vl-text] coord item[48]: text=均健康。, bbox=[122, 805, 192, 821]
2026-08-10 06:08:49,614 INFO     29 [qwen-vl-text] coord item[49]: text=家族史：父母已故，1弟1姐2妹均体健。家族无类似患者疾病、传染性疾病、遗传性, bbox=[162, 831, 886, 848]
2026-08-10 06:08:49,614 INFO     29 [qwen-vl-text] coord item[50]: text=疾病。, bbox=[122, 860, 173, 876]
2026-08-10 06:08:49,614 INFO     29 [qwen-vl-text] coord item[51]: text=第1页, bbox=[475, 935, 537, 948]
2026-08-10 06:08:49,614 INFO     29 [qwen-vl-text] page=1 — 52/52 coords, api_time=19.4s
2026-08-10 06:08:49,615 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=649343, prompt_len=828
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["民权县人民医院", "入院记录", "姓名：", "科室：呼吸二病区", "床号：", "住院号：", "肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、", "皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。", "辅助检查", "暂无。", "初步诊断", "1.哮喘（急性发作）", "2.慢性支气管炎", "住院医师：王贝贝", "主治医师：陈文宁", "主任医师：已签字", "第3页"]

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
2026-08-10 06:08:55,626 INFO     29 [qwen-vl-text] coord API raw response (len=911):
[
	{"text": "民权县人民医院", "bbox": [407, 44, 592, 63]},
	{"text": "入院记录", "bbox": [420, 78, 568, 97]},
	{"text": "姓名：", "bbox": [119, 117, 165, 131]},
	{"text": "科室：呼吸二病区", "bbox": [282, 115, 445, 130]},
	{"text": "床号：", "bbox": [543, 115, 591, 130]},
	{"text": "住院号：", "bbox": [702, 115, 770, 130]},
	{"text": "肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、", "bbox": [123, 156, 890, 173]},
	{"text": "皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。", "bbox": [113, 183, 568, 200]},
	{"text": "辅助检查", "bbox": [436, 212, 548, 227]},
	{"text": "暂无。", "bbox": [131, 240, 178, 256]},
	{"text": "初步诊断", "bbox": [436, 268, 548, 284]},
	{"text": "1.哮喘（急性发作）", "bbox": [495, 296, 668, 312]},
	{"text": "2.慢性支气管炎", "bbox": [513, 325, 657, 341]},
	{"text": "住院医师：王贝贝", "bbox": [695, 350, 874, 375]},
	{"text": "主治医师：陈文宁", "bbox": [695, 388, 874, 414]},
	{"text": "主任医师：已签字", "bbox": [695, 425, 871, 453]},
	{"text": "第3页", "bbox": [461, 936, 521, 950]}
]
2026-08-10 06:08:55,626 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=6.0s
2026-08-10 06:08:55,626 INFO     29 [qwen-vl-text] coord item[0]: text=民权县人民医院, bbox=[407, 44, 592, 63]
2026-08-10 06:08:55,626 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[420, 78, 568, 97]
2026-08-10 06:08:55,626 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[119, 117, 165, 131]
2026-08-10 06:08:55,626 INFO     29 [qwen-vl-text] coord item[3]: text=科室：呼吸二病区, bbox=[282, 115, 445, 130]
2026-08-10 06:08:55,626 INFO     29 [qwen-vl-text] coord item[4]: text=床号：, bbox=[543, 115, 591, 130]
2026-08-10 06:08:55,626 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[702, 115, 770, 130]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[6]: text=肺：胸廓呈桶状胸，双侧呼吸运动正常，肋间隙正常。双侧语颤正常。双侧无胸膜摩擦感、, bbox=[123, 156, 890, 173]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[7]: text=皮下捻发感。叩诊音呈清音。呼吸音异常干性啰音。, bbox=[113, 183, 568, 200]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[8]: text=辅助检查, bbox=[436, 212, 548, 227]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[9]: text=暂无。, bbox=[131, 240, 178, 256]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[10]: text=初步诊断, bbox=[436, 268, 548, 284]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[11]: text=1.哮喘（急性发作）, bbox=[495, 296, 668, 312]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[12]: text=2.慢性支气管炎, bbox=[513, 325, 657, 341]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[13]: text=住院医师：王贝贝, bbox=[695, 350, 874, 375]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[14]: text=主治医师：陈文宁, bbox=[695, 388, 874, 414]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[15]: text=主任医师：已签字, bbox=[695, 425, 871, 453]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] coord item[16]: text=第3页, bbox=[461, 936, 521, 950]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] page=2 — 17/17 coords, api_time=6.0s
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] new_positions (103):
[[0, 242.76, 353.43, 37.89, 54.73], [0, 251.685, 339.745, 66.518, 83.358], [0, 71.39999999999999, 99.96, 101.88199999999999, 115.354], [0, 169.575, 267.75, 98.514, 112.828], [0, 325.465, 380.205, 95.988, 109.46], [0, 418.88, 459.34, 95.146, 107.776], [0, 262.99, 329.63, 132.194, 145.666], [0, 96.39, 361.16499999999996, 154.928, 171.768], [0, 96.985, 527.765, 174.29399999999998, 197.87], [0, 69.615, 208.25, 204.606, 221.446], [0, 97.58, 520.625, 219.762, 244.17999999999998], [0, 70.80499999999999, 417.69, 246.706, 268.598], [0, 98.175, 274.295, 274.492, 291.332], [0, 98.77, 527.765, 293.01599999999996, 314.908], [0, 71.39999999999999, 527.765, 316.592, 338.484], [0, 72.59, 531.3349999999999, 340.168, 362.06], [0, 73.185, 174.92999999999998, 371.322, 385.63599999999997], [0, 101.14999999999999, 525.98, 387.32, 409.212], [0, 73.78, 525.98, 410.054, 431.94599999999997], [0, 73.78, 91.63, 442.05, 454.68], [0, 102.33999999999999, 532.525, 454.68, 478.256], [0, 74.375, 330.22499999999997, 483.308, 501.832], [0, 102.935, 528.9549999999999, 502.674, 524.566], [0, 74.97, 298.69, 530.46, 548.984], [0, 103.53, 529.55, 549.826, 571.718], [0, 75.565, 222.53, 579.2959999999999, 595.294], [0, 103.53, 522.41, 596.136, 618.028], [0, 76.16, 371.28, 623.0799999999999, 641.6039999999999], [0, 104.125, 530.74, 642.446, 665.18], [0, 77.35, 129.11499999999998, 675.284, 688.756], [0, 104.72, 204.08499999999998, 698.018, 713.174], [0, 104.72, 195.16, 721.5939999999999, 735.066], [0, 271.91499999999996, 337.365, 742.644, 756.958], [0, 287.385, 323.085, 785.586, 796.5319999999999], [1, 242.165, 352.835, 40.416, 58.098], [1, 250.49499999999998, 338.555, 71.57, 88.41], [1, 71.39999999999999, 99.365, 102.72399999999999, 116.196], [1, 169.575, 266.56, 102.72399999999999, 116.196], [1, 324.275, 379.015, 102.72399999999999, 115.354], [1, 417.69, 458.15, 101.88199999999999, 115.354], [1, 69.615, 165.41, 138.93, 152.402], [1, 196.35, 262.99, 138.93, 152.402], [1, 349.265, 411.74, 138.088, 151.56], [1, 69.615, 135.065, 159.98, 173.452], [1, 196.35, 245.73499999999999, 159.98, 173.452], [1, 270.72499999999997, 330.22499999999997, 159.98, 173.452], [1, 349.265, 505.75, 159.138, 171.768], [1, 69.615, 129.11499999999998, 181.03, 194.50199999999998], [1, 196.35, 258.22999999999996, 180.188, 193.66], [1, 270.72499999999997, 330.82, 180.188, 193.66], [1, 349.265, 505.75, 179.346, 192.81799999999998], [1, 69.615, 174.92999999999998, 202.07999999999998, 215.552], [1, 258.22999999999996, 330.22499999999997, 201.238, 214.70999999999998], [1, 349.265, 478.38, 200.396, 213.868], [1, 69.615, 296.31, 223.13, 236.602], [1, 302.85499999999996, 398.65, 229.86599999999999, 244.17999999999998], [1, 426.615, 521.22, 221.446, 234.91799999999998], [1, 69.615, 93.41499999999999, 239.97, 253.44199999999998], [1, 426.615, 438.515, 237.444, 250.916], [1, 69.615, 136.255, 260.178, 273.65], [1, 302.85499999999996, 472.43, 259.336, 272.808], [1, 69.615, 141.60999999999999, 282.07, 295.542], [1, 198.73, 282.625, 282.07, 295.542], [1, 368.305, 508.72499999999997, 281.228, 294.7], [1, 99.365, 342.125, 304.804, 318.276], [1, 69.615, 525.98, 327.538, 341.01], [1, 69.615, 521.22, 373.006, 387.32], [1, 69.615, 521.22, 395.74, 410.054], [1, 69.615, 525.98, 418.474, 432.788], [1, 69.615, 523.005, 441.20799999999997, 455.522], [1, 69.615, 280.84, 465.626, 479.09799999999996], [1, 99.365, 523.6, 488.35999999999996, 502.674], [1, 69.615, 441.48999999999995, 511.936, 526.25], [1, 99.365, 524.79, 535.512, 549.826], [1, 69.615, 524.79, 559.088, 572.56], [1, 69.615, 235.02499999999998, 582.664, 596.136], [1, 99.365, 267.155, 606.24, 619.712], [1, 99.365, 165.41, 636.552, 650.024], [1, 190.39999999999998, 201.10999999999999, 639.92, 652.55], [1, 203.48999999999998, 219.55499999999998, 637.394, 648.34], [1, 198.73, 224.315, 648.34, 658.444], [1, 224.315, 530.145, 634.8679999999999, 650.024], [1, 72.59, 114.24, 677.81, 691.2819999999999], [1, 96.39, 527.17, 699.702, 714.016], [1, 72.59, 102.935, 724.12, 737.592], [1, 282.625, 319.515, 787.27, 798.216], [2, 242.165, 352.24, 37.048, 53.046], [2, 249.89999999999998, 337.96, 65.676, 81.67399999999999], [2, 70.80499999999999, 98.175, 98.514, 110.30199999999999], [2, 167.79, 264.775, 96.83, 109.46], [2, 323.085, 351.645, 96.83, 109.46], [2, 417.69, 458.15, 96.83, 109.46], [2, 73.185, 529.55, 131.352, 145.666], [2, 67.235, 337.96, 154.08599999999998, 168.4], [2, 259.42, 326.06, 178.504, 191.134], [2, 77.945, 105.91, 202.07999999999998, 215.552], [2, 259.42, 326.06, 225.656, 239.128], [2, 294.525, 397.46, 249.232, 262.704], [2, 305.235, 390.91499999999996, 273.65, 287.122], [2, 413.525, 520.03, 294.7, 315.75], [2, 413.525, 520.03, 326.69599999999997, 348.58799999999997], [2, 413.525, 518.245, 357.84999999999997, 381.426], [2, 274.295, 309.995, 788.112, 799.9]]
2026-08-10 06:08:55,627 INFO     29 [qwen-vl-text] ═══ DONE ═══ 103 positions, pages=3, time=56.4s
2026-08-10 06:08:56,200 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 06:08:56,201 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:08:56,202 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 06:08:56,204 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:08:56.202+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "b531b82a948111f1bd9827cf206dfa2d": {"id": "b531b82a948111f1bd9827cf206dfa2d", "doc_id": "b40fb046948111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342023691, "task_type": "dataflow", "root_trace_id": "5de32dcc1c9241298e4a586d264050c9", "root_traceparent": "00-5de32dcc1c9241298e4a586d264050c9-8ca896b124088c1e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:08:56,218 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:08:56,220 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:08:56,220 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:08:56,221 INFO     29 [qwen-vl-text] positions(126): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:08:56,221 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [126]
2026-08-10 06:08:56,407 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:08:56,408 INFO     29 [qwen-vl-text] LLM extraction start, text_len=765
2026-08-10 06:08:56,408 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:08:56,408 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 103, \"bbox_end\": 228, \"encounter_dates\": [\"2023-08-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "民权县人民医院\n肺功能检查报告\n病人ID:\n2023-08-1501\n性别：\n女\n高度：\n158 cm\n名：\n出生日期：\n1957/7/2\n体重：\n60 kg\n姓：\n年龄：\n66 years\nBMI：\n24.0 kg/m²\n体积\n流量\n体积\n时间[s]\n时间[s]\n单位\n预测值\n之前\n%预值\n沙丁胺醇\n(400\n%预值\n%变化\nug)\nVC\nI\n(1)\n2.37\n1.66\n70%\n2.20\n93%\n+32.2%\nVC\nI\n(1)\n2.37\n1.66\n70%\n2.20\n93%\n+32.2%\nFEV1\nI\n(1)\n1.99\n0.88\n44%\n1.27\n64%\n+44.4%\nFEV1/FVC\n%\n(1)\n77\n53\n69%\n58\n75%\n+9.3%\nFEV1/VC\n%\n(1)\n77\n53\n69%\n58\n75%\n+9.3%\nPEF\nl/s\n(1)\n5.60\n2.06\n37%\n2.74\n49%\n+32.9%\nMEF75\nl/s\n(1)\n5.04\n0.97\n19%\n1.53\n30%\n+57.6%\nMEF50\nl/s\n(1)\n3.38\n0.49\n14%\n0.78\n23%\n+60.6%\nMEF25\nl/s\n(1)\n1.12\n0.22\n19%\n0.29\n26%\n+35.4%\n诊断意见：\n1.重度混合型通气功能障碍，小气道功能减低。\n2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。\n3.MVV:44%。建议定期复查。\n(1): ECCS 1993\n检测:2023/8/15\n-1-\nBTPS: 21.0 °C, 1013 hPa,\n50%\n医生：-\nGeratherm Respiratory GmbH\nwww.geratherm-respiratory.com\nBlue Cherry V1.2.2.24",
    "role": "user"
  }
]
2026-08-10 06:09:04,807 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:09:04,807 INFO     29 [qwen-vl-text] LLM output (len=2742):
{
  "encounter_date": "2022-03-26",
  "prescription_type": "取药执行单",
  "prescriber": "谭真真",
  "department": "呼吸危重三病区(门)",
  "diagnosis": null,
  "items": [
    {
      "drug_generic_name": "双黄连口服液",
      "drug_trade_name": "小儿双黄连口服液",
      "drug_category": "中成药",
      "dosage": "10ml",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "小儿氨酚黄那敏颗粒",
      "drug_trade_name": "盖克",
      "drug_category": "西药",
      "dosage": "6g",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "阿莫西林克拉维酸钾干混悬剂",
      "drug_trade_name": "抗之膏",
      "drug_category": "西药",
      "dosage": "0.228g",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": "继续用药"
    },
    {
      "drug_generic_name": "蒲地蓝消炎口服液",
      "drug_trade_name": null,
      "drug_category": "中成药",
      "dosage": "10ml",
      "frequency": "bid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "复方氨酚甲麻口服液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10ml",
      "frequency": "q6h",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "小儿氨酚黄那敏颗粒",
      "drug_trade_name": "盖克",
      "drug_category": "西药",
      "dosage": "12g",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": null
    },
    {
      "drug_generic_name": "阿莫西林克拉维酸钾干混悬剂",
      "drug_trade_name": "抗之膏",
      "drug_category": "西药",
      "dosage": "0.45g",
      "frequency": "q12h",
      "route": "口服",
      "duration_days": null,
      "quantity": "2",
      "notes": "继续用药"
    },
    {
      "drug_generic_name": "吸入用布地奈德混悬液",
      "drug_trade_name": "普米克令舒",
      "drug_category": "西药",
      "dosage": "2ml",
      "frequency": "bid",
      "route": "压缩雾化",
      "duration_days": null,
      "quantity": "5",
      "notes": null
    },
    {
      "drug_generic_name": "右旋糖酐铁颗粒",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "1袋",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "80",
      "notes": null
    },
    {
      "drug_generic_name": "盐酸氨卓斯丁滴眼液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.1ml",
      "frequency": "bid",
      "route": "滴双眼",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    }
  ]
}
2026-08-10 06:09:04,807 INFO     29 [qwen-vl-text] Updated encounter_dates=[2022-03-26]
2026-08-10 06:09:04,808 INFO     29 [qwen-vl-text] coord API call start, page=37, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=772217, prompt_len=1409
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称(规格)", "药品 甲)(小儿)双黄连口服液(基)", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)", "药品 蒲地蓝消炎口服液", "药品 复方氨酚甲麻口服液", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)", "药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)", "药品 右旋糖酐铁颗粒", "药品 盐酸氨卓斯丁滴眼液", "用法 频率 实际用量 总量 开立时间 开立医师", "口服 tid 10ml 1 2022-03-26 19:51:46 谭真真", "口服 tid 6g 2 2022-03-26 19:51:18 谭真真", "口服(继续 用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真", "口服 bid 10ml 1 2022-03-26 19:51:18 谭真真", "口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴", "口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴", "口服(继续 用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴", "压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅", "口服 tid 1袋 80 2021-09-28 15:12:34 党建华", "滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳", "共70条 20条/页 < 1 2 3 4 > 前往 4 页"]

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
2026-08-10 06:09:17,248 INFO     29 [qwen-vl-text] coord API raw response (len=1864):
```json
[
	{"text": "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "bbox": [18, 195, 588, 215]},
	{"text": "请输入药品内容,按回车键检索", "bbox": [18, 237, 198, 259]},
	{"text": "查询全部", "bbox": [212, 240, 262, 255]},
	{"text": "类型 组 药品名称(规格)", "bbox": [17, 270, 164, 290]},
	{"text": "药品 甲)(小儿)双黄连口服液(基)", "bbox": [17, 294, 204, 314]},
	{"text": "药品 (盖克)小儿氨酚黄那敏颗粒", "bbox": [17, 319, 204, 338]},
	{"text": "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)", "bbox": [17, 351, 271, 371]},
	{"text": "药品 蒲地蓝消炎口服液", "bbox": [17, 385, 175, 404]},
	{"text": "药品 复方氨酚甲麻口服液", "bbox": [17, 409, 183, 428]},
	{"text": "药品 (盖克)小儿氨酚黄那敏颗粒", "bbox": [17, 434, 206, 453]},
	{"text": "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)", "bbox": [17, 466, 281, 486]},
	{"text": "药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)", "bbox": [17, 499, 277, 518]},
	{"text": "药品 右旋糖酐铁颗粒", "bbox": [17, 523, 168, 542]},
	{"text": "药品 盐酸氨卓斯丁滴眼液", "bbox": [17, 548, 184, 567]},
	{"text": "用法 频率 实际用量 总量 开立时间 开立医师", "bbox": [643, 270, 978, 290]},
	{"text": "口服 tid 10ml 1 2022-03-26 19:51:46 谭真真", "bbox": [643, 294, 978, 314]},
	{"text": "口服 tid 6g 2 2022-03-26 19:51:18 谭真真", "bbox": [643, 319, 978, 338]},
	{"text": "口服(继续 用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真", "bbox": [643, 343, 978, 371]},
	{"text": "口服 bid 10ml 1 2022-03-26 19:51:18 谭真真", "bbox": [643, 385, 978, 404]},
	{"text": "口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴", "bbox": [643, 409, 978, 428]},
	{"text": "口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴", "bbox": [643, 434, 978, 453]},
	{"text": "口服(继续 用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴", "bbox": [643, 466, 978, 486]},
	{"text": "压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅", "bbox": [643, 499, 978, 518]},
	{"text": "口服 tid 1袋 80 2021-09-28 15:12:34 党建华", "bbox": [643, 523, 978, 542]},
	{"text": "滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳", "bbox": [643, 548, 978, 567]},
	{"text": "共70条 20条/页 < 1 2 3 4 > 前往 4 页", "bbox": [723, 582, 987, 601]}
]
```
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=12.4s
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[0]: text=集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告, bbox=[18, 195, 588, 215]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[1]: text=请输入药品内容,按回车键检索, bbox=[18, 237, 198, 259]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[2]: text=查询全部, bbox=[212, 240, 262, 255]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[3]: text=类型 组 药品名称(规格), bbox=[17, 270, 164, 290]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[4]: text=药品 甲)(小儿)双黄连口服液(基), bbox=[17, 294, 204, 314]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[5]: text=药品 (盖克)小儿氨酚黄那敏颗粒, bbox=[17, 319, 204, 338]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[6]: text=药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基), bbox=[17, 351, 271, 371]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[7]: text=药品 蒲地蓝消炎口服液, bbox=[17, 385, 175, 404]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[8]: text=药品 复方氨酚甲麻口服液, bbox=[17, 409, 183, 428]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[9]: text=药品 (盖克)小儿氨酚黄那敏颗粒, bbox=[17, 434, 206, 453]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[10]: text=药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基), bbox=[17, 466, 281, 486]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[11]: text=药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基), bbox=[17, 499, 277, 518]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[12]: text=药品 右旋糖酐铁颗粒, bbox=[17, 523, 168, 542]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[13]: text=药品 盐酸氨卓斯丁滴眼液, bbox=[17, 548, 184, 567]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[14]: text=用法 频率 实际用量 总量 开立时间 开立医师, bbox=[643, 270, 978, 290]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[15]: text=口服 tid 10ml 1 2022-03-26 19:51:46 谭真真, bbox=[643, 294, 978, 314]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[16]: text=口服 tid 6g 2 2022-03-26 19:51:18 谭真真, bbox=[643, 319, 978, 338]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[17]: text=口服(继续 用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真, bbox=[643, 343, 978, 371]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[18]: text=口服 bid 10ml 1 2022-03-26 19:51:18 谭真真, bbox=[643, 385, 978, 404]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[19]: text=口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴, bbox=[643, 409, 978, 428]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[20]: text=口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴, bbox=[643, 434, 978, 453]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[21]: text=口服(继续 用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴, bbox=[643, 466, 978, 486]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[22]: text=压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅, bbox=[643, 499, 978, 518]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[23]: text=口服 tid 1袋 80 2021-09-28 15:12:34 党建华, bbox=[643, 523, 978, 542]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[24]: text=滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳, bbox=[643, 548, 978, 567]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] coord item[25]: text=共70条 20条/页 < 1 2 3 4 > 前往 4 页, bbox=[723, 582, 987, 601]
2026-08-10 06:09:17,249 INFO     29 [qwen-vl-text] page=37 — 26/26 coords, api_time=12.4s
2026-08-10 06:09:17,250 INFO     29 [qwen-vl-text] new_positions (26):
[[37, 15.155999999999999, 495.096, 116.02499999999999, 127.925], [37, 15.155999999999999, 166.716, 141.015, 154.105], [37, 178.504, 220.60399999999998, 142.79999999999998, 151.725], [37, 14.314, 138.088, 160.65, 172.54999999999998], [37, 14.314, 171.768, 174.92999999999998, 186.82999999999998], [37, 14.314, 171.768, 189.80499999999998, 201.10999999999999], [37, 14.314, 228.182, 208.845, 220.74499999999998], [37, 14.314, 147.35, 229.075, 240.38], [37, 14.314, 154.08599999999998, 243.355, 254.66], [37, 14.314, 173.452, 258.22999999999996, 269.53499999999997], [37, 14.314, 236.602, 277.27, 289.16999999999996], [37, 14.314, 233.23399999999998, 296.905, 308.21], [37, 14.314, 141.456, 311.185, 322.49], [37, 14.314, 154.928, 326.06, 337.365], [37, 541.406, 823.476, 160.65, 172.54999999999998], [37, 541.406, 823.476, 174.92999999999998, 186.82999999999998], [37, 541.406, 823.476, 189.80499999999998, 201.10999999999999], [37, 541.406, 823.476, 204.08499999999998, 220.74499999999998], [37, 541.406, 823.476, 229.075, 240.38], [37, 541.406, 823.476, 243.355, 254.66], [37, 541.406, 823.476, 258.22999999999996, 269.53499999999997], [37, 541.406, 823.476, 277.27, 289.16999999999996], [37, 541.406, 823.476, 296.905, 308.21], [37, 541.406, 823.476, 311.185, 322.49], [37, 541.406, 823.476, 326.06, 337.365], [37, 608.766, 831.054, 346.28999999999996, 357.59499999999997]]
2026-08-10 06:09:17,250 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=61.1s
2026-08-10 06:09:17,250 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:09:17,251 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:09:17,251 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 06:09:17,251 INFO     29 [qwen-vl-text] positions(12): [[51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:09:17,251 INFO     29 [qwen-vl-text] page grouping: [51], lines per page: [12]
2026-08-10 06:09:17,520 INFO     29 [qwen-vl-text] page=51, rect=842x1193, img=(2339x3313), dpi=200
2026-08-10 06:09:17,523 INFO     29 [qwen-vl-text] LLM extraction start, text_len=132
2026-08-10 06:09:17,523 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:09:17,523 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 2271, \"bbox_end\": 2282, \"encounter_dates\": [\"2021-02-16\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "处方笺\n4970401\n姓名：\n性别：□男 □女 年龄：60岁\n科别： 费别： 电话/住址：\n过敏史：无 开具日期：2021年2月16日\n临床诊断：支气管哮喘\nRp\n孟鲁司特钠片 10mg 2板\n用法：二天一次 1片\n审核： 调配： 医师：\n核对： 发药： 金额：",
    "role": "user"
  }
]
2026-08-10 06:09:17,527 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:09:17,527 INFO     29 [qwen-vl-text] LLM output (len=1021):
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
2026-08-10 06:09:17,531 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2160017, prompt_len=1757
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共126行）
["民权县人民医院", "肺功能检查报告", "病人ID:", "2023-08-1501", "性别：", "女", "高度：", "158 cm", "名：", "出生日期：", "1957/7/2", "体重：", "60 kg", "姓：", "年龄：", "66 years", "BMI：", "24.0 kg/m²", "体积", "流量", "体积", "时间[s]", "时间[s]", "单位", "预测值", "之前", "%预值", "沙丁胺醇", "(400", "%预值", "%变化", "ug)", "VC", "I", "(1)", "2.37", "1.66", "70%", "2.20", "93%", "+32.2%", "VC", "I", "(1)", "2.37", "1.66", "70%", "2.20", "93%", "+32.2%", "FEV1", "I", "(1)", "1.99", "0.88", "44%", "1.27", "64%", "+44.4%", "FEV1/FVC", "%", "(1)", "77", "53", "69%", "58", "75%", "+9.3%", "FEV1/VC", "%", "(1)", "77", "53", "69%", "58", "75%", "+9.3%", "PEF", "l/s", "(1)", "5.60", "2.06", "37%", "2.74", "49%", "+32.9%", "MEF75", "l/s", "(1)", "5.04", "0.97", "19%", "1.53", "30%", "+57.6%", "MEF50", "l/s", "(1)", "3.38", "0.49", "14%", "0.78", "23%", "+60.6%", "MEF25", "l/s", "(1)", "1.12", "0.22", "19%", "0.29", "26%", "+35.4%", "诊断意见：", "1.重度混合型通气功能障碍，小气道功能减低。", "2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。", "3.MVV:44%。建议定期复查。", "(1): ECCS 1993", "检测:2023/8/15", "-1-", "BTPS: 21.0 °C, 1013 hPa,", "50%", "医生：-", "Geratherm Respiratory GmbH", "www.geratherm-respiratory.com", "Blue Cherry V1.2.2.24"]

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
2026-08-10 06:10:21,093 INFO     29 [qwen-vl-text] coord API raw response (len=10387):
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
	{"text": "60 kg", "bbox": [767, 185, 795, 194], "bbox_2d": [767, 185, 795, 194]},
	{"text": "姓：", "bbox": [100, 187, 117, 196], "bbox_2d": [100, 187, 117, 196]},
	{"text": "年龄：", "bbox": [369, 191, 398, 200], "bbox_2d": [369, 191, 398, 200]},
	{"text": "66 years", "bbox": [502, 193, 545, 202], "bbox_2d": [502, 193, 545, 202]},
	{"text": "BMI：", "bbox": [634, 193, 657, 201], "bbox_2d": [634, 193, 657, 201]},
	{"text": "24.0 kg/m²", "bbox": [767, 195, 819, 204], "bbox_2d": [767, 195, 819, 204]},
	{"text": "体积", "bbox": [94, 223, 107, 240], "bbox_2d": [94, 223, 107, 240]},
	{"text": "流量", "bbox": [323, 231, 336, 262], "bbox_2d": [323, 231, 336, 262]},
	{"text": "体积", "bbox": [643, 228, 657, 245], "bbox_2d": [643, 228, 657, 245]},
	{"text": "时间[s]", "bbox": [265, 467, 307, 477], "bbox_2d": [265, 467, 307, 477]},
	{"text": "时间[s]", "bbox": [858, 470, 898, 480], "bbox_2d": [858, 470, 898, 480]},
	{"text": "单位", "bbox": [251, 512, 294, 527], "bbox_2d": [251, 512, 294, 527]},
	{"text": "预测值", "bbox": [335, 512, 397, 527], "bbox_2d": [335, 512, 397, 527]},
	{"text": "之前", "bbox": [419, 512, 461, 527], "bbox_2d": [419, 512, 461, 527]},
	{"text": "%预值", "bbox": [474, 512, 534, 527], "bbox_2d": [474, 512, 534, 527]},
	{"text": "沙丁胺醇", "bbox": [554, 500, 638, 515], "bbox_2d": [554, 500, 638, 515]},
	{"text": "(400", "bbox": [600, 516, 638, 530], "bbox_2d": [600, 516, 638, 530]},
	{"text": "%预值", "bbox": [653, 515, 714, 530], "bbox_2d": [653, 515, 714, 530]},
	{"text": "%变化", "bbox": [735, 515, 796, 530], "bbox_2d": [735, 515, 796, 530]},
	{"text": "ug)", "bbox": [609, 532, 638, 546], "bbox_2d": [609, 532, 638, 546]},
	{"text": "VC", "bbox": [204, 551, 232, 564], "bbox_2d": [204, 551, 232, 564]},
	{"text": "I", "bbox": [264, 551, 271, 564], "bbox_2d": [264, 551, 271, 564]},
	{"text": "(1)", "bbox": [300, 547, 315, 557], "bbox_2d": [300, 547, 315, 557]},
	{"text": "2.37", "bbox": [363, 551, 399, 564], "bbox_2d": [363, 551, 399, 564]},
	{"text": "1.66", "bbox": [428, 551, 464, 564], "bbox_2d": [428, 551, 464, 564]},
	{"text": "70%", "bbox": [502, 551, 536, 564], "bbox_2d": [502, 551, 536, 564]},
	{"text": "2.20", "bbox": [604, 551, 640, 564], "bbox_2d": [604, 551, 640, 564]},
	{"text": "93%", "bbox": [680, 551, 715, 564], "bbox_2d": [680, 551, 715, 564]},
	{"text": "+32.2%", "bbox": [737, 551, 797, 564], "bbox_2d": [737, 551, 797, 564]},
	{"text": "VC", "bbox": [204, 573, 232, 586], "bbox_2d": [204, 573, 232, 586]},
	{"text": "I", "bbox": [264, 573, 271, 586], "bbox_2d": [264, 573, 271, 586]},
	{"text": "(1)", "bbox": [300, 569, 315, 579], "bbox_2d": [300, 569, 315, 579]},
	{"text": "2.37", "bbox": [363, 573, 399, 586], "bbox_2d": [363, 573, 399, 586]},
	{"text": "1.66", "bbox": [428, 573, 464, 586], "bbox_2d": [428, 573, 464, 586]},
	{"text": "70%", "bbox": [502, 573, 536, 586], "bbox_2d": [502, 573, 536, 586]},
	{"text": "2.20", "bbox": [604, 573, 640, 586], "bbox_2d": [604, 573, 640, 586]},
	{"text": "93%", "bbox": [680, 573, 715, 586], "bbox_2d": [680, 573, 715, 586]},
	{"text": "+32.2%", "bbox": [737, 573, 797, 586], "bbox_2d": [737, 573, 797, 586]},
	{"text": "FEV1", "bbox": [181, 596, 228, 609], "bbox_2d": [181, 596, 228, 609]},
	{"text": "I", "bbox": [264, 596, 271, 609], "bbox_2d": [264, 596, 271, 609]},
	{"text": "(1)", "bbox": [300, 592, 315, 602], "bbox_2d": [300, 592, 315, 602]},
	{"text": "1.99", "bbox": [363, 596, 399, 609], "bbox_2d": [363, 596, 399, 609]},
	{"text": "0.88", "bbox": [426, 596, 463, 609], "bbox_2d": [426, 596, 463, 609]},
	{"text": "44%", "bbox": [501, 596, 536, 609], "bbox_2d": [501, 596, 536, 609]},
	{"text": "1.27", "bbox": [606, 596, 642, 609], "bbox_2d": [606, 596, 642, 609]},
	{"text": "64%", "bbox": [680, 596, 715, 609], "bbox_2d": [680, 596, 715, 609]},
	{"text": "+44.4%", "bbox": [737, 596, 797, 609], "bbox_2d": [737, 596, 797, 609]},
	{"text": "FEV1/FVC", "bbox": [138, 619, 230, 632], "bbox_2d": [138, 619, 230, 632]},
	{"text": "%", "bbox": [257, 619, 274, 632], "bbox_2d": [257, 619, 274, 632]},
	{"text": "(1)", "bbox": [298, 615, 313, 625], "bbox_2d": [298, 615, 313, 625]},
	{"text": "77", "bbox": [376, 619, 398, 632], "bbox_2d": [376, 619, 398, 632]},
	{"text": "53", "bbox": [441, 619, 463, 632], "bbox_2d": [441, 619, 463, 632]},
	{"text": "69%", "bbox": [501, 619, 536, 632], "bbox_2d": [501, 619, 536, 632]},
	{"text": "58", "bbox": [620, 619, 642, 632], "bbox_2d": [620, 619, 642, 632]},
	{"text": "75%", "bbox": [680, 619, 715, 632], "bbox_2d": [680, 619, 715, 632]},
	{"text": "+9.3%", "bbox": [747, 619, 797, 632], "bbox_2d": [747, 619, 797, 632]},
	{"text": "FEV1/VC", "bbox": [150, 642, 230, 655], "bbox_2d": [150, 642, 230, 655]},
	{"text": "%", "bbox": [257, 642, 274, 655], "bbox_2d": [257, 642, 274, 655]},
	{"text": "(1)", "bbox": [298, 638, 313, 648], "bbox_2d": [298, 638, 313, 648]},
	{"text": "77", "bbox": [376, 642, 398, 655], "bbox_2d": [376, 642, 398, 655]},
	{"text": "53", "bbox": [441, 642, 463, 655], "bbox_2d": [441, 642, 463, 655]},
	{"text": "69%", "bbox": [501, 642, 536, 655], "bbox_2d": [501, 642, 536, 655]},
	{"text": "58", "bbox": [620, 642, 642, 655], "bbox_2d": [620, 642, 642, 655]},
	{"text": "75%", "bbox": [680, 642, 715, 655], "bbox_2d": [680, 642, 715, 655]},
	{"text": "+9.3%", "bbox": [747, 642, 797, 655], "bbox_2d": [747, 642, 797, 655]},
	{"text": "PEF", "bbox": [192, 665, 230, 678], "bbox_2d": [192, 665, 230, 678]},
	{"text": "l/s", "bbox": [257, 665, 276, 678], "bbox_2d": [257, 665, 276, 678]},
	{"text": "(1)", "bbox": [298, 661, 313, 671], "bbox_2d": [298, 661, 313, 671]},
	{"text": "5.60", "bbox": [362, 665, 398, 678], "bbox_2d": [362, 665, 398, 678]},
	{"text": "2.06", "bbox": [425, 665, 462, 678], "bbox_2d": [425, 665, 462, 678]},
	{"text": "37%", "bbox": [501, 665, 536, 678], "bbox_2d": [501, 665, 536, 678]},
	{"text": "2.74", "bbox": [604, 665, 640, 678], "bbox_2d": [604, 665, 640, 678]},
	{"text": "49%", "bbox": [680, 665, 715, 678], "bbox_2d": [680, 665, 715, 678]},
	{"text": "+32.9%", "bbox": [737, 665, 797, 678], "bbox_2d": [737, 665, 797, 678]},
	{"text": "MEF75", "bbox": [168, 687, 230, 700], "bbox_2d": [168, 687, 230, 700]},
	{"text": "l/s", "bbox": [257, 687, 276, 700], "bbox_2d": [257, 687, 276, 700]},
	{"text": "(1)", "bbox": [298, 683, 313, 693], "bbox_2d": [298, 683, 313, 693]},
	{"text": "5.04", "bbox": [362, 687, 398, 700], "bbox_2d": [362, 687, 398, 700]},
	{"text": "0.97", "bbox": [425, 687, 462, 700], "bbox_2d": [425, 687, 462, 700]},
	{"text": "19%", "bbox": [502, 687, 536, 700], "bbox_2d": [502, 687, 536, 700]},
	{"text": "1.53", "bbox": [606, 687, 642, 700], "bbox_2d": [606, 687, 642, 700]},
	{"text": "30%", "bbox": [680, 687, 715, 700], "bbox_2d": [680, 687, 715, 700]},
	{"text": "+57.6%", "bbox": [737, 687, 797, 700], "bbox_2d": [737, 687, 797, 700]},
	{"text": "MEF50", "bbox": [167, 710, 230, 723], "bbox_2d": [167, 710, 230, 723]},
	{"text": "l/s", "bbox": [257, 710, 276, 723], "bbox_2d": [257, 710, 276, 723]},
	{"text": "(1)", "bbox": [298, 706, 313, 716], "bbox_2d": [298, 706, 313, 716]},
	{"text": "3.38", "bbox": [362, 710, 398, 723], "bbox_2d": [362, 710, 398, 723]},
	{"text": "0.49", "bbox": [425, 710, 462, 723], "bbox_2d": [425, 710, 462, 723]},
	{"text": "14%", "bbox": [502, 710, 536, 723], "bbox_2d": [502, 710, 536, 723]},
	{"text": "0.78", "bbox": [604, 710, 640, 723], "bbox_2d": [604, 710, 640, 723]},
	{"text": "23%", "bbox": [680, 710, 715, 723], "bbox_2d": [680, 710, 715, 723]},
	{"text": "+60.6%", "bbox": [737, 710, 797, 723], "bbox_2d": [737, 710, 797, 723]},
	{"text": "MEF25", "bbox": [165, 733, 230, 746], "bbox_2d": [165, 733, 230, 746]},
	{"text": "l/s", "bbox": [257, 733, 276, 746], "bbox_2d": [257, 733, 276, 746]},
	{"text": "(1)", "bbox": [298, 729, 313, 739], "bbox_2d": [298, 729, 313, 739]},
	{"text": "1.12", "bbox": [362, 733, 398, 746], "bbox_2d": [362, 733, 398, 746]},
	{"text": "0.22", "bbox": [425, 733, 462, 746], "bbox_2d": [425, 733, 462, 746]},
	{"text": "19%", "bbox": [502, 733, 536, 746], "bbox_2d": [502, 733, 536, 746]},
	{"text": "0.29", "bbox": [604, 733, 640, 746], "bbox_2d": [604, 733, 640, 746]},
	{"text": "26%", "bbox": [680, 733, 715, 746], "bbox_2d": [680, 733, 715, 746]},
	{"text": "+35.4%", "bbox": [737, 733, 797, 746], "bbox_2d": [737, 733, 797, 746]},
	{"text": "诊断意见：", "bbox": [85, 774, 170, 790], "bbox_2d": [85, 774, 170, 790]},
	{"text": "1.重度混合型通气功能障碍，小气道功能减低。", "bbox": [84, 797, 483, 818], "bbox_2d": [84, 797, 483, 818]},
	{"text": "2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。", "bbox": [83, 812, 658, 833], "bbox_2d": [83, 812, 658, 833]},
	{"text": "3.MVV:44%。建议定期复查。", "bbox": [83, 828, 332, 848], "bbox_2d": [83, 828, 332, 848]},
	{"text": "(1): ECCS 1993", "bbox": [80, 882, 175, 897], "bbox_2d": [80, 882, 175, 897]},
	{"text": "检测:2023/8/15", "bbox": [80, 903, 201, 920], "bbox_2d": [80, 903, 201, 920]},
	{"text": "-1-", "bbox": [383, 897, 413, 907], "bbox_2d": [383, 897, 413, 907]},
	{"text": "BTPS: 21.0 °C, 1013 hPa,", "bbox": [506, 894, 689, 909], "bbox_2d": [506, 894, 689, 909]},
	{"text": "50%", "bbox": [578, 909, 615, 920], "bbox_2d": [578, 909, 615, 920]},
	{"text": "医生：-", "bbox": [778, 900, 830, 913], "bbox_2d": [778, 900, 830, 913]},
	{"text": "Geratherm Respiratory GmbH", "bbox": [80, 933, 259, 950], "bbox_2d": [80, 933, 259, 950]},
	{"text": "www.geratherm-respiratory.com", "bbox": [407, 925, 588, 937], "bbox_2d": [407, 925, 588, 937]},
	{"text": "Blue Cherry V1.2.2.24", "bbox": [778, 930, 904, 939], "bbox_2d": [778, 930, 904, 939]}
]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord API: raw_items=126, valid_items=126, elapsed=63.6s
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[0]: text=民权县人民医院, bbox=[418, 98, 591, 113]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[458, 120, 557, 132]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[2]: text=病人ID:, bbox=[100, 166, 146, 176]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[3]: text=2023-08-1501, bbox=[234, 171, 304, 180]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[4]: text=性别：, bbox=[369, 171, 398, 180]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[5]: text=女, bbox=[502, 173, 514, 181]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[6]: text=高度：, bbox=[634, 172, 662, 181]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[7]: text=158 cm, bbox=[767, 175, 800, 184]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[8]: text=名：, bbox=[100, 177, 117, 186]
2026-08-10 06:10:21,094 INFO     29 [qwen-vl-text] coord item[9]: text=出生日期：, bbox=[369, 181, 418, 190]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[10]: text=1957/7/2, bbox=[502, 183, 545, 192]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[11]: text=体重：, bbox=[634, 182, 662, 191]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[12]: text=60 kg, bbox=[767, 185, 795, 194]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[13]: text=姓：, bbox=[100, 187, 117, 196]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[14]: text=年龄：, bbox=[369, 191, 398, 200]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[15]: text=66 years, bbox=[502, 193, 545, 202]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[16]: text=BMI：, bbox=[634, 193, 657, 201]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[17]: text=24.0 kg/m², bbox=[767, 195, 819, 204]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[18]: text=体积, bbox=[94, 223, 107, 240]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[19]: text=流量, bbox=[323, 231, 336, 262]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[20]: text=体积, bbox=[643, 228, 657, 245]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[21]: text=时间[s], bbox=[265, 467, 307, 477]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[22]: text=时间[s], bbox=[858, 470, 898, 480]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[23]: text=单位, bbox=[251, 512, 294, 527]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[24]: text=预测值, bbox=[335, 512, 397, 527]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[25]: text=之前, bbox=[419, 512, 461, 527]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[26]: text=%预值, bbox=[474, 512, 534, 527]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[27]: text=沙丁胺醇, bbox=[554, 500, 638, 515]
2026-08-10 06:10:21,095 INFO     29 [qwen-vl-text] coord item[28]: text=(400, bbox=[600, 516, 638, 530]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[29]: text=%预值, bbox=[653, 515, 714, 530]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[30]: text=%变化, bbox=[735, 515, 796, 530]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[31]: text=ug), bbox=[609, 532, 638, 546]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[32]: text=VC, bbox=[204, 551, 232, 564]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[33]: text=I, bbox=[264, 551, 271, 564]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[34]: text=(1), bbox=[300, 547, 315, 557]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[35]: text=2.37, bbox=[363, 551, 399, 564]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[36]: text=1.66, bbox=[428, 551, 464, 564]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[37]: text=70%, bbox=[502, 551, 536, 564]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[38]: text=2.20, bbox=[604, 551, 640, 564]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[39]: text=93%, bbox=[680, 551, 715, 564]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[40]: text=+32.2%, bbox=[737, 551, 797, 564]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[41]: text=VC, bbox=[204, 573, 232, 586]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[42]: text=I, bbox=[264, 573, 271, 586]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[43]: text=(1), bbox=[300, 569, 315, 579]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[44]: text=2.37, bbox=[363, 573, 399, 586]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[45]: text=1.66, bbox=[428, 573, 464, 586]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[46]: text=70%, bbox=[502, 573, 536, 586]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[47]: text=2.20, bbox=[604, 573, 640, 586]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[48]: text=93%, bbox=[680, 573, 715, 586]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[49]: text=+32.2%, bbox=[737, 573, 797, 586]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[50]: text=FEV1, bbox=[181, 596, 228, 609]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[51]: text=I, bbox=[264, 596, 271, 609]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[52]: text=(1), bbox=[300, 592, 315, 602]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[53]: text=1.99, bbox=[363, 596, 399, 609]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[54]: text=0.88, bbox=[426, 596, 463, 609]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[55]: text=44%, bbox=[501, 596, 536, 609]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[56]: text=1.27, bbox=[606, 596, 642, 609]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[57]: text=64%, bbox=[680, 596, 715, 609]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[58]: text=+44.4%, bbox=[737, 596, 797, 609]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[59]: text=FEV1/FVC, bbox=[138, 619, 230, 632]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[60]: text=%, bbox=[257, 619, 274, 632]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[61]: text=(1), bbox=[298, 615, 313, 625]
2026-08-10 06:10:21,096 INFO     29 [qwen-vl-text] coord item[62]: text=77, bbox=[376, 619, 398, 632]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[63]: text=53, bbox=[441, 619, 463, 632]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[64]: text=69%, bbox=[501, 619, 536, 632]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[65]: text=58, bbox=[620, 619, 642, 632]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[66]: text=75%, bbox=[680, 619, 715, 632]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[67]: text=+9.3%, bbox=[747, 619, 797, 632]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[68]: text=FEV1/VC, bbox=[150, 642, 230, 655]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[69]: text=%, bbox=[257, 642, 274, 655]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[70]: text=(1), bbox=[298, 638, 313, 648]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[71]: text=77, bbox=[376, 642, 398, 655]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[72]: text=53, bbox=[441, 642, 463, 655]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[73]: text=69%, bbox=[501, 642, 536, 655]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[74]: text=58, bbox=[620, 642, 642, 655]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[75]: text=75%, bbox=[680, 642, 715, 655]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[76]: text=+9.3%, bbox=[747, 642, 797, 655]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[77]: text=PEF, bbox=[192, 665, 230, 678]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[78]: text=l/s, bbox=[257, 665, 276, 678]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[79]: text=(1), bbox=[298, 661, 313, 671]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[80]: text=5.60, bbox=[362, 665, 398, 678]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[81]: text=2.06, bbox=[425, 665, 462, 678]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[82]: text=37%, bbox=[501, 665, 536, 678]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[83]: text=2.74, bbox=[604, 665, 640, 678]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[84]: text=49%, bbox=[680, 665, 715, 678]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[85]: text=+32.9%, bbox=[737, 665, 797, 678]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[86]: text=MEF75, bbox=[168, 687, 230, 700]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[87]: text=l/s, bbox=[257, 687, 276, 700]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[88]: text=(1), bbox=[298, 683, 313, 693]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[89]: text=5.04, bbox=[362, 687, 398, 700]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[90]: text=0.97, bbox=[425, 687, 462, 700]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[91]: text=19%, bbox=[502, 687, 536, 700]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[92]: text=1.53, bbox=[606, 687, 642, 700]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[93]: text=30%, bbox=[680, 687, 715, 700]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[94]: text=+57.6%, bbox=[737, 687, 797, 700]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[95]: text=MEF50, bbox=[167, 710, 230, 723]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[96]: text=l/s, bbox=[257, 710, 276, 723]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[97]: text=(1), bbox=[298, 706, 313, 716]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[98]: text=3.38, bbox=[362, 710, 398, 723]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[99]: text=0.49, bbox=[425, 710, 462, 723]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[100]: text=14%, bbox=[502, 710, 536, 723]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[101]: text=0.78, bbox=[604, 710, 640, 723]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[102]: text=23%, bbox=[680, 710, 715, 723]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[103]: text=+60.6%, bbox=[737, 710, 797, 723]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[104]: text=MEF25, bbox=[165, 733, 230, 746]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[105]: text=l/s, bbox=[257, 733, 276, 746]
2026-08-10 06:10:21,097 INFO     29 [qwen-vl-text] coord item[106]: text=(1), bbox=[298, 729, 313, 739]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[107]: text=1.12, bbox=[362, 733, 398, 746]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[108]: text=0.22, bbox=[425, 733, 462, 746]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[109]: text=19%, bbox=[502, 733, 536, 746]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[110]: text=0.29, bbox=[604, 733, 640, 746]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[111]: text=26%, bbox=[680, 733, 715, 746]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[112]: text=+35.4%, bbox=[737, 733, 797, 746]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[113]: text=诊断意见：, bbox=[85, 774, 170, 790]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[114]: text=1.重度混合型通气功能障碍，小气道功能减低。, bbox=[84, 797, 483, 818]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[115]: text=2.沙丁胺醇支气管舒张试验阳性，FEV1增加390ml，改善44.4%。, bbox=[83, 812, 658, 833]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[116]: text=3.MVV:44%。建议定期复查。, bbox=[83, 828, 332, 848]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[117]: text=(1): ECCS 1993, bbox=[80, 882, 175, 897]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[118]: text=检测:2023/8/15, bbox=[80, 903, 201, 920]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[119]: text=-1-, bbox=[383, 897, 413, 907]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[120]: text=BTPS: 21.0 °C, 1013 hPa,, bbox=[506, 894, 689, 909]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[121]: text=50%, bbox=[578, 909, 615, 920]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[122]: text=医生：-, bbox=[778, 900, 830, 913]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[123]: text=Geratherm Respiratory GmbH, bbox=[80, 933, 259, 950]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[124]: text=www.geratherm-respiratory.com, bbox=[407, 925, 588, 937]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] coord item[125]: text=Blue Cherry V1.2.2.24, bbox=[778, 930, 904, 939]
2026-08-10 06:10:21,098 INFO     29 [qwen-vl-text] page=3 — 126/126 coords, api_time=63.6s
2026-08-10 06:10:21,099 INFO     29 [qwen-vl-text] new_positions (126):
[[3, 248.70999999999998, 351.645, 82.51599999999999, 95.146], [3, 272.51, 331.41499999999996, 101.03999999999999, 111.14399999999999], [3, 59.5, 86.86999999999999, 139.772, 148.192], [3, 139.23, 180.88, 143.982, 151.56], [3, 219.55499999999998, 236.81, 143.982, 151.56], [3, 298.69, 305.83, 145.666, 152.402], [3, 377.22999999999996, 393.89, 144.82399999999998, 152.402], [3, 456.36499999999995, 476.0, 147.35, 154.928], [3, 59.5, 69.615, 149.034, 156.612], [3, 219.55499999999998, 248.70999999999998, 152.402, 159.98], [3, 298.69, 324.275, 154.08599999999998, 161.664], [3, 377.22999999999996, 393.89, 153.244, 160.822], [3, 456.36499999999995, 473.025, 155.76999999999998, 163.34799999999998], [3, 59.5, 69.615, 157.454, 165.03199999999998], [3, 219.55499999999998, 236.81, 160.822, 168.4], [3, 298.69, 324.275, 162.506, 170.084], [3, 377.22999999999996, 390.91499999999996, 162.506, 169.242], [3, 456.36499999999995, 487.30499999999995, 164.19, 171.768], [3, 55.93, 63.665, 187.766, 202.07999999999998], [3, 192.185, 199.92, 194.50199999999998, 220.60399999999998], [3, 382.585, 390.91499999999996, 191.976, 206.29], [3, 157.67499999999998, 182.665, 393.214, 401.63399999999996], [3, 510.51, 534.31, 395.74, 404.15999999999997], [3, 149.345, 174.92999999999998, 431.104, 443.734], [3, 199.325, 236.215, 431.104, 443.734], [3, 249.30499999999998, 274.295, 431.104, 443.734], [3, 282.03, 317.72999999999996, 431.104, 443.734], [3, 329.63, 379.60999999999996, 421.0, 433.63], [3, 357.0, 379.60999999999996, 434.472, 446.26], [3, 388.53499999999997, 424.83, 433.63, 446.26], [3, 437.325, 473.62, 433.63, 446.26], [3, 362.35499999999996, 379.60999999999996, 447.94399999999996, 459.73199999999997], [3, 121.38, 138.04, 463.942, 474.888], [3, 157.07999999999998, 161.245, 463.942, 474.888], [3, 178.5, 187.42499999999998, 460.574, 468.99399999999997], [3, 215.98499999999999, 237.405, 463.942, 474.888], [3, 254.66, 276.08, 463.942, 474.888], [3, 298.69, 318.91999999999996, 463.942, 474.888], [3, 359.38, 380.79999999999995, 463.942, 474.888], [3, 404.59999999999997, 425.42499999999995, 463.942, 474.888], [3, 438.515, 474.215, 463.942, 474.888], [3, 121.38, 138.04, 482.466, 493.412], [3, 157.07999999999998, 161.245, 482.466, 493.412], [3, 178.5, 187.42499999999998, 479.09799999999996, 487.518], [3, 215.98499999999999, 237.405, 482.466, 493.412], [3, 254.66, 276.08, 482.466, 493.412], [3, 298.69, 318.91999999999996, 482.466, 493.412], [3, 359.38, 380.79999999999995, 482.466, 493.412], [3, 404.59999999999997, 425.42499999999995, 482.466, 493.412], [3, 438.515, 474.215, 482.466, 493.412], [3, 107.695, 135.66, 501.832, 512.778], [3, 157.07999999999998, 161.245, 501.832, 512.778], [3, 178.5, 187.42499999999998, 498.464, 506.88399999999996], [3, 215.98499999999999, 237.405, 501.832, 512.778], [3, 253.47, 275.485, 501.832, 512.778], [3, 298.09499999999997, 318.91999999999996, 501.832, 512.778], [3, 360.57, 381.99, 501.832, 512.778], [3, 404.59999999999997, 425.42499999999995, 501.832, 512.778], [3, 438.515, 474.215, 501.832, 512.778], [3, 82.11, 136.85, 521.198, 532.144], [3, 152.915, 163.03, 521.198, 532.144], [3, 177.31, 186.23499999999999, 517.8299999999999, 526.25], [3, 223.72, 236.81, 521.198, 532.144], [3, 262.395, 275.485, 521.198, 532.144], [3, 298.09499999999997, 318.91999999999996, 521.198, 532.144], [3, 368.9, 381.99, 521.198, 532.144], [3, 404.59999999999997, 425.42499999999995, 521.198, 532.144], [3, 444.465, 474.215, 521.198, 532.144], [3, 89.25, 136.85, 540.564, 551.51], [3, 152.915, 163.03, 540.564, 551.51], [3, 177.31, 186.23499999999999, 537.196, 545.616], [3, 223.72, 236.81, 540.564, 551.51], [3, 262.395, 275.485, 540.564, 551.51], [3, 298.09499999999997, 318.91999999999996, 540.564, 551.51], [3, 368.9, 381.99, 540.564, 551.51], [3, 404.59999999999997, 425.42499999999995, 540.564, 551.51], [3, 444.465, 474.215, 540.564, 551.51], [3, 114.24, 136.85, 559.93, 570.876], [3, 152.915, 164.22, 559.93, 570.876], [3, 177.31, 186.23499999999999, 556.562, 564.982], [3, 215.39, 236.81, 559.93, 570.876], [3, 252.875, 274.89, 559.93, 570.876], [3, 298.09499999999997, 318.91999999999996, 559.93, 570.876], [3, 359.38, 380.79999999999995, 559.93, 570.876], [3, 404.59999999999997, 425.42499999999995, 559.93, 570.876], [3, 438.515, 474.215, 559.93, 570.876], [3, 99.96, 136.85, 578.454, 589.4], [3, 152.915, 164.22, 578.454, 589.4], [3, 177.31, 186.23499999999999, 575.086, 583.506], [3, 215.39, 236.81, 578.454, 589.4], [3, 252.875, 274.89, 578.454, 589.4], [3, 298.69, 318.91999999999996, 578.454, 589.4], [3, 360.57, 381.99, 578.454, 589.4], [3, 404.59999999999997, 425.42499999999995, 578.454, 589.4], [3, 438.515, 474.215, 578.454, 589.4], [3, 99.365, 136.85, 597.8199999999999, 608.766], [3, 152.915, 164.22, 597.8199999999999, 608.766], [3, 177.31, 186.23499999999999, 594.452, 602.872], [3, 215.39, 236.81, 597.8199999999999, 608.766], [3, 252.875, 274.89, 597.8199999999999, 608.766], [3, 298.69, 318.91999999999996, 597.8199999999999, 608.766], [3, 359.38, 380.79999999999995, 597.8199999999999, 608.766], [3, 404.59999999999997, 425.42499999999995, 597.8199999999999, 608.766], [3, 438.515, 474.215, 597.8199999999999, 608.766], [3, 98.175, 136.85, 617.1859999999999, 628.132], [3, 152.915, 164.22, 617.1859999999999, 628.132], [3, 177.31, 186.23499999999999, 613.818, 622.2379999999999], [3, 215.39, 236.81, 617.1859999999999, 628.132], [3, 252.875, 274.89, 617.1859999999999, 628.132], [3, 298.69, 318.91999999999996, 617.1859999999999, 628.132], [3, 359.38, 380.79999999999995, 617.1859999999999, 628.132], [3, 404.59999999999997, 425.42499999999995, 617.1859999999999, 628.132], [3, 438.515, 474.215, 617.1859999999999, 628.132], [3, 50.574999999999996, 101.14999999999999, 651.708, 665.18], [3, 49.98, 287.385, 671.074, 688.756], [3, 49.385, 391.51, 683.704, 701.386], [3, 49.385, 197.54, 697.1759999999999, 714.016], [3, 47.599999999999994, 104.125, 742.644, 755.274], [3, 47.599999999999994, 119.595, 760.326, 774.64], [3, 227.885, 245.73499999999999, 755.274, 763.694], [3, 301.07, 409.955, 752.7479999999999, 765.3779999999999], [3, 343.90999999999997, 365.925, 765.3779999999999, 774.64], [3, 462.90999999999997, 493.84999999999997, 757.8, 768.746], [3, 47.599999999999994, 154.105, 785.586, 799.9], [3, 242.165, 349.85999999999996, 778.85, 788.954], [3, 462.90999999999997, 537.88, 783.06, 790.6379999999999]]
2026-08-10 06:10:21,099 INFO     29 [qwen-vl-text] ═══ DONE ═══ 126 positions, pages=1, time=84.9s
2026-08-10 06:10:21,718 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 06:10:21,718 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "229 items", "markdown": "", "text": "", "name": "GFXI 商丘.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:10:21,718 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 06:10:21,719 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:10:21.718+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "b531b82a948111f1bd9827cf206dfa2d": {"id": "b531b82a948111f1bd9827cf206dfa2d", "doc_id": "b40fb046948111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342023691, "task_type": "dataflow", "root_trace_id": "5de32dcc1c9241298e4a586d264050c9", "root_traceparent": "00-5de32dcc1c9241298e4a586d264050c9-8ca896b124088c1e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:10:21,721 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-10 06:10:21,740 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 06:10:21,741 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'AdmissionRecord': 1, 'ExaminationReport': 1}", "name": "GFXI 商丘.pdf"}
2026-08-10 06:10:21,741 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 06:10:22,405 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786342040125, 'update_date': datetime.datetime(2026, 8, 10, 6, 7, 20), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 775111, 'status': '1'}
2026-08-10 06:10:22,661 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=民权县人民医院
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
期间多次就诊于我院考虑“哮喘”，积极予以“沙美特罗替卡松粉吸入剂”改善症状，上述
症状仍时有发生。2天前受凉后上述症状反复，胸闷，气急明显，发作频次增加，日常活动
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
第3页
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
检测:2023/8/15
-1-
BTPS: 21.0 °C, 1013 hPa,
50%
医生：-
Geratherm Respiratory GmbH
www.geratherm-respiratory.com
Blue Cherry V1.2.2.24
2026-08-10 06:10:23,134 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 06:10:23,134 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'AdmissionRecord': 1, 'ExaminationReport': 1}", "name": "GFXI 商丘.pdf", "embedding_token_consumption": 1979}
2026-08-10 06:10:23,134 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 06:10:23,853 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 06:10:23,853 INFO     29 [Trace] task=b531b82a | doc=GFXI 商丘.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 06:10:23,862 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:10:23,863 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:10:23,880 INFO     29 set_progress(b531b82a948111f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 06:10:23 [DOC Engine]:
Start to index...
2026-08-10 06:10:24,067 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.177s]
2026-08-10 06:10:24,072 INFO     29 set_progress(b531b82a948111f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 06:10:24,082 INFO     29 set_progress(b531b82a948111f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 06:10:24 Indexing done (0.21s). Task done (183.75s)
2026-08-10 06:10:24,089 INFO     29 [Done], chunks(2), token(1979), elapsed:183.75
2026-08-10 06:10:24,197 INFO     29 handle_task done for task {"id": "b531b82a948111f1bd9827cf206dfa2d", "doc_id": "b40fb046948111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GFXI \u5546\u4e18.pdf", "type": "pdf", "location": "GFXI \u5546\u4e18.pdf", "size": 3295700, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786342023691, "task_type": "dataflow", "root_trace_id": "5de32dcc1c9241298e4a586d264050c9", "root_traceparent": "00-5de32dcc1c9241298e4a586d264050c9-8ca896b124088c1e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
