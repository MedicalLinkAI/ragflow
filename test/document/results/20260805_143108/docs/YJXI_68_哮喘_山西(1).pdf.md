# 基准结果：YJXI 68 哮喘 山西(1).pdf

## 基本信息

- 文件：`YJXI 68 哮喘 山西(1).pdf`
- 大小：7775.6 KB
- PDF 总页数：11
- doc_id：`a0687fe6908f11f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:20  完成时间：2026-08-05T14:31:21  耗时：0.9s
- progress_msg：`05:41:45 Indexing done (0.07s). Task done (280.30s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 898e9f8d | 1 | 1-1 | 门诊电子病历（初诊） 姓名： 性别：女性 年龄：68岁 科室：呼吸与危重症医学门 |
| 2 | e68bd13f | 2 | 2-3 | 出院记录 姓名： 性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号： 住 |
| 3 | 981c92e9 | 1 | 4-4 | CT检查报告单 检查 病人姓名 性别：女 年龄：66岁 申请科室：呼吸与危重症二 |
| 4 | 6838963e | 1 | 5-5 | 【处方】导引单 ID: 姓名: 年龄：68岁 性别：女 费别：普通患者 诊断：支 |
| 5 | 5e8d6dce | 1 | 6-6 | [G532]  心草招县西人乡连锁 店 交易日期：2025-10-31 11:4 |
| 6 | 67dd6628 | 1 | 7-7 | 山西省医疗门诊收费票据（电子） 山西省 财政部监制 票据号码：004008195 |
| 7 | 09eb66f1 | 1 | 8-8 | 山西省医疗门诊收费票据（电子） 山西省 财政部监制 票据代码： 交款人话一社会信 |
| 8 | 28438611 | 1 | 9-9 | 山西省医疗门诊收费票据（电子） 山西省 财政部监制 票据代码:1/ 交款人统一社 |
| 9 | f2d04627 | 1 | 10-10 | 山西省医疗门诊收费票据（电子） 山西省 财政部监制 票据代码:14060124  |
| 10 | e9b095db | 1 | 11-11 | <table><tr><td>白细胞计数</td><td>WBC</td><td |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：11
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`
- 覆盖页数：11 / 11；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 5 | 5 | 5 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 1 | 1 | 1 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "DischargeRecord": 1, "ExaminationReport": 1, "PrescriptionRecord": 1, "MedicationRecord": 5, "LabReport": 1}`
- ChunkMerger：`{"found": true, "merged": 10, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 5, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 2}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 05:41:43,550 INFO     29 [ChunkMerger] Merged 10 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 5, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 05:36:39,026 INFO     29 handle_task begin for task {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 05:36:39,273 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-05 05:36:39,315 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 05:36:39,328 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 05:36:39,328 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 05:36:39,336 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 05:36:39,336 INFO     29 ============================================================
2026-08-05 05:36:39,336 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 05:36:39,336 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 05:36:39,336 INFO     29 ============================================================
2026-08-05 05:36:39,336 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 05:36:39,336 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 05:36:39,338 INFO     29 No torch found.
2026-08-05 05:36:40,819 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=11
2026-08-05 05:36:40,906 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=622373, prompt_len=644
2026-08-05 05:36:42,292 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 05:36:42,292 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-05 05:36:42,300 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=622373, prompt_len=401
2026-08-05 05:36:44,301 INFO     29 [qwen-vl-parser] text API response (len=343):
["门诊电子病历（初诊）", "姓名：", "性别：女性", "年龄：68岁", "科室：呼吸与危重症医学门诊科", "就诊时间：2026年01月19日16时48分", "主诉：咳嗽、气短40余年，近一周加重", "现病史：咳嗽、气短40余年，近一周加重，曾于当地医院诊断支气管哮喘，2024年3月因哮喘急性发作在", "山大二院住院治疗，规律使用布地格福吸入气雾剂，加重1周", "既往史：既往不详，未确认糖尿病病史，未确认高血压病史。", "过敏史：未确认药物过敏史，未确认食物过敏史。", "家族史：不详。", "门诊诊断：支气管哮喘(急性发作期)", "处理意见：醋酸泼尼松片、5mg*100片、15mg、口服、QD（每日一次）、1瓶；", "医师签", "第1页（共1页）"]
2026-08-05 05:36:44,302 INFO     29 [qwen-vl-parser] page=1 text: 16 lines (bbox 0-15)
2026-08-05 05:36:44,302 INFO     29 [qwen-vl-parser] page=1 text: 16 sections
2026-08-05 05:36:44,422 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1129938, prompt_len=644
2026-08-05 05:36:45,741 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 05:36:45,741 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 05:36:45,757 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1129938, prompt_len=401
2026-08-05 05:36:51,506 INFO     29 [qwen-vl-parser] text API response (len=1132):
["出院记录", "姓名：", "性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：", "住院号：", "姓名", "性别：女", "年龄：66岁", "职业：农民", "入院日期：2024年03月15日10时", "出院日期：2024年03月18日11时", "住院天数：3天", "入院时情况：发作性喘息10年，加重2月。", "入院诊断：1.支气管哮喘(急性发作期)", "2.低氧血症", "诊疗经过：完善相关化验及检查：", "血气分析：吸氧浓度21.0%，酸碱度7.414，二氧化碳分压35.3mmHg，氧分压67.9mmHg↓，", "实际碱剩余-1.4mmol/L，血浆碳酸氢盐浓度22.2mmol/L，乳酸浓度0.6mmol/", "L，氧合指数323mmHg↓，肺泡动脉氧分压差27.7mmHg↑。", "血常规：白细胞计数4.06*10^9/L，红细胞计数4.49*10^12/L，血红蛋白131g/L，血小板", "280*10^9/L。红细胞沉降率5mm/H。C反应蛋白2.43mg/L。", "肝+肾+离子：血清丙氨酸氨基转移酶10.80U/L，血清天门冬氨酸氨基转移酶15.60U/L，尿", "素4.40mmol/L，肌酐51.00umol/L，钾3.79mmol/L，钠143.00mmol/L，氯", "109.00mmol/L。", "免疫球蛋白：E128.00IU/mL↑。", "呼吸道病原体抗体：阴性；新型冠状病毒核酸：阴性；痰培养：阴性；", "尿常规：尿常规检验报告尿隐血-，尿白细胞3+，尿蛋白-，白细胞134个/uL↑。", "肿瘤标志物、心肺四项、凝血、便常规未见明显异常。", "腹部彩超：肝囊肿（多发）胆、胰、脾、双肾未见明显异常；", "心脏彩超：EF：68% 三尖瓣口少量返流 主动脉瓣口少量返流 左室舒张功能减低 左室收", "缩功能正常；", "胸部CT：双肺实性微结节，建议随诊 肝内低密度灶，考虑囊肿。", "肺功能：激发前：FEV1/FVC 86.86%，FEV1 96% FVC 90.2% 通气功能大致正常，吸入乙", "酰甲胆碱 32mg/ml（第5管）激发后FEV1/FVC 72.8%，FEV1下降20.82%，激发", "试验（+），DLCO 53.3% 肺弥散功能显著减退 RV/TLC 65.72%,残总比升高。", "呼出气一氧化氮测定：FENO50 25ppb 混合型气道炎症 FENO200 18ppb 小气道炎症 CaNO", "14.7ppb 肺泡炎症。FENO10 233。", "2.予以抗过敏、扩张气道、促进排痰、抗感染等对症治疗。", "第1页"]
2026-08-05 05:36:51,506 INFO     29 [qwen-vl-parser] page=2 text: 38 lines (bbox 16-53)
2026-08-05 05:36:51,506 INFO     29 [qwen-vl-parser] page=2 text: 38 sections
2026-08-05 05:36:51,591 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=598201, prompt_len=644
2026-08-05 05:36:52,946 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:36:52,946 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 05:36:52,959 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=598201, prompt_len=401
2026-08-05 05:36:56,052 INFO     29 [qwen-vl-parser] text API response (len=506):
["出院记录", "姓名：", "性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：", "床号：", "出院时情况：患者气短明显缓解，偶有咳嗽，无明显咳痰，精神可。查体：口唇暗紫", "色，咽部无充血，扁桃体无肿大；双肺未闻及干湿性啰音，心律齐，未闻及心脏瓣膜杂", "音；腹软，无压痛、反跳痛，双下肢无水肿。", "出院诊断：1.支气管哮喘(急性发作期)", "2.低氧血症", "3.肺部阴影(双肺结节性质待查)", "4.多发性肝囊肿", "出院医嘱：1、加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必", "要时吸氧。", "2、院外继续通药物治疗：", "氯雷他定片 10 mg/片 口服 睡前(1月)", "孟鲁司特片 10 mg/片 口服 睡前(1月)", "布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 (3月)", "茶碱缓释片 0.1g/片 口服 2次/日(长期)", "3、3月后复查胸部高分辨CT，总IgE、肺功能+扩张+弥散", "4、2周后呼吸科门诊复诊，不适随诊。", "签名：", "记录日期：2024年03月18日11时56分", "第2页"]
2026-08-05 05:36:56,052 INFO     29 [qwen-vl-parser] page=3 text: 23 lines (bbox 54-76)
2026-08-05 05:36:56,052 INFO     29 [qwen-vl-parser] page=3 text: 23 sections
2026-08-05 05:36:56,135 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=540762, prompt_len=644
2026-08-05 05:36:57,500 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-03-15"}
```
2026-08-05 05:36:57,500 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2024-03-15
2026-08-05 05:36:57,506 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=540762, prompt_len=401
2026-08-05 05:36:59,758 INFO     29 [qwen-vl-parser] text API response (len=379):
["CT检查报告单", "检查", "病人姓名", "性别：女", "年龄：66岁", "申请科室：呼吸与危重症二组", "住院号：", "门诊号：", "造影剂：", "检查部位：胸部高分辨平扫+矢冠状面重建", "影像学表现：", "双侧胸廓不对称，气管居中。双肺纹理清晰，走向自然，右肺下叶前基底段、", "左肺下叶外基底段、左肺下叶背段均可见结节影，较大者直径约0.4cm，所见各支", "气管腔通畅，纵隔内可肿大淋巴结，胸膜无增厚，胸腔内无积液。所扫肝内可见", "多个类圆形低密度影，密度均匀，边界尚清。", "初步诊断及建议：", "双肺实性微结节，建议随诊", "肝内低密度灶，考虑囊肿", "录入者：", "审核医", "报告日期：2024.03.15 18:52:06", "注：本报告仅供临床医师参考，本科室医师签字后有效。", ""]
2026-08-05 05:36:59,758 INFO     29 [qwen-vl-parser] page=4 text: 22 lines (bbox 77-98)
2026-08-05 05:36:59,758 INFO     29 [qwen-vl-parser] page=4 text: 22 sections
2026-08-05 05:36:59,843 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=586967, prompt_len=644
2026-08-05 05:37:01,148 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:37:01,149 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 05:37:01,161 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=586967, prompt_len=401
2026-08-05 05:37:06,649 INFO     29 [qwen-vl-parser] text API response (len=431):
["【处方】导引单", "ID:", "姓名:", "年龄：68岁", "性别：女", "费别：普通患者", "诊断：支气管哮喘(急性发作期)", "开单科室：呼吸与危重症医学科", "开单时间：2026-01-20 17:33:34", "取药排", "药品名称", "规格", "数量", "1.醋酸泼尼松片", "5mg*100片", "1瓶", "15.0mg", "口服", "每日一次", "微信/支付宝", "扫码支付", "金额：4.8元", "执行科室：门诊药房", "地点：门诊大厅一层西侧", "医生", "处方当日有效，补打导引单不可作为取药凭证", "【患者留存】", "ID:", "姓名:", "年龄：68岁", "性别：女", "药品名称", "规格", "数量", "1.醋酸泼尼松片", "5mg*100片", "1瓶", "15.0mg", "口服", "每日一次", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:37:06,649 INFO     29 [qwen-vl-parser] page=5 text: 42 lines (bbox 99-140)
2026-08-05 05:37:06,649 INFO     29 [qwen-vl-parser] page=5 text: 42 sections
2026-08-05 05:37:06,679 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:37:06.679+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"a0ac621a908f11f1a3da71efcdd7cc1f": {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:37:06,758 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=814407, prompt_len=644
2026-08-05 05:37:08,051 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:37:08,052 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 05:37:08,063 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=814407, prompt_len=401
2026-08-05 05:37:11,496 INFO     29 [qwen-vl-parser] text API response (len=574):
["[G532]  心草招县西人乡连锁", "店", "交易日期：2025-10-31 11:43:49", "销售单号：1325103100021472", "收银员：", "积分：543", "品名", "规格", "150027(兴)布地格福吸入", "气雾剂 倍择瑞_160ug:7.2u", "单价:233.00", "实价:233.00", "数量:2.00", "金额:466.00", "批号：6103904C00", "处方药", "国码：XRO3ALB240L028010179096", "AstraZeneca AB", "84471890087171843044", "84471890087171828685", "2、809245_一心堂卫生纸(原生", "木浆(纤维))_1000g(4层*1", "单价:11.80", "实价:0.01", "数量:1.00", "金额:0.01", "批号：20240825", "国码：Q01000000", "应收金额:477.8 优惠:11.8", "实收金额:466.01找零:0.00", "其中:收钱吧微信：", "466.01", "*药品除质量问题，概不退换", "*服务不满意，", "*地址-电话·", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:37:11,497 INFO     29 [qwen-vl-parser] page=6 text: 37 lines (bbox 141-177)
2026-08-05 05:37:11,497 INFO     29 [qwen-vl-parser] page=6 text: 37 sections
2026-08-05 05:37:11,613 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=781963, prompt_len=644
2026-08-05 05:37:12,939 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:37:12,940 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 05:37:12,953 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=781963, prompt_len=401
2026-08-05 05:37:16,016 INFO     29 [qwen-vl-parser] text API response (len=672):
["山西省医疗门诊收费票据（电子）", "山西省", "财政部监制", "票据号码：0040081955", "校验码：itykbi", "开票日期：2025-09-01", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "233.00", "", "", "", "", "", "G布地格福吸入气雾剂【每瓶12", "1.00", "盒", "233.00 限慢性阻", "", "", "", "", "0揿】", "", "", "塞性肺疾", "", "", "", "", "病。", "", "", "", "", "金额合计（大写）贰佰叁拾叁元整", "(小写)233.00", "", "", "业务流水号：07QIKH59659470P20250 门诊号：", "", "", "就诊日期：20250901", "901172144801", "", "", "", "（医", "型：综合医院", "医保类型：国家医保", "医保码", "", "", "", "医保统", "支付：154.95", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：78.05", "付：0.0", "", "", "", "z-方便", "", "", "", "费专用章", "", "", "", "复核人：程小磊", "收款", "", "", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:37:16,016 INFO     29 [qwen-vl-parser] page=7 text: 45 lines (bbox 178-222)
2026-08-05 05:37:16,016 INFO     29 [qwen-vl-parser] page=7 text: 45 sections
2026-08-05 05:37:16,121 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=752023, prompt_len=644
2026-08-05 05:37:17,363 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:37:17,364 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-05 05:37:17,375 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=752023, prompt_len=401
2026-08-05 05:37:20,102 INFO     29 [qwen-vl-parser] text API response (len=695):
["山西省医疗门诊收费票据（电子）", "山西省", "财政部监制", "票据代码：", "交款人话一社会信用代码：", "交款人", "票据号码：0039960248", "校验码：isI3ej", "开票日期：2025-07-08", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "466.00", "", "", "", "", "", "G布地格福吸入气雾剂【每瓶12", "2.00", "盒", "466.00 限慢性阻", "", "", "", "", "0揿】", "", "", "塞性肺疾", "", "", "", "", "病。", "", "", "", "", "金额合计（大写）肆佰陆拾陆元整", "(小写)466.00", "", "", "业务流水号：B7C8A658327630P20250 门诊号：", "就诊日期：20250708", "708113600815", "", "", "类型：综合医院", "医保类型：国家医保", "医保编", "", "", "医保.", "付：309.89", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：156.11", "信", "自付：", "", "", "息", "Z-方便", "靖号", "个人自费：156.11", "", "", "费专用", "", "", "复核人：程小蕊", "收款人：王丽", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:37:20,103 INFO     29 [qwen-vl-parser] page=8 text: 51 lines (bbox 223-273)
2026-08-05 05:37:20,103 INFO     29 [qwen-vl-parser] page=8 text: 51 sections
2026-08-05 05:37:20,239 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=974657, prompt_len=644
2026-08-05 05:37:21,510 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:37:21,510 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-05 05:37:21,520 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=974657, prompt_len=401
2026-08-05 05:37:24,639 INFO     29 [qwen-vl-parser] text API response (len=681):
["山西省医疗门诊收费票据（电子）", "山西省", "财政部监制", "票据代码:1/", "交款人统一社会信用代码:", "交款", "票据号码:0155140741", "校验码: ci4u59", "开票日期:2026-02-24", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1.00", "233.00", "", "", "", "", "", "G布地格福吸入气雾剂【每瓶12", "1.00", "盒", "233.00 限慢性阻", "", "", "", "", "0揿】", "", "", "塞性肺疾", "", "", "", "", "病。", "", "", "", "", "金额合计（大写）贰佰叁拾叁元整", "(小写)233.00", "", "业务流水号:2", "门诊号:", "就诊日期:20260224", "2", "", "", "", "类型:综合医院", "医保类型:国家医保", "医保编号", "0548 性别:女", "医保现", "付:154.95", "其他支付:0.00", "个人账户支付:0.00", "个人现金支付:78.05", "信", "自付:", "", "", "", "总", "Z-方便", "赵泽斌号", "个人自费:78.05", "费专用章", "", "", "", "复核人:程小蕊", "收款人:刘灵芝", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:37:24,639 INFO     29 [qwen-vl-parser] page=9 text: 53 lines (bbox 274-326)
2026-08-05 05:37:24,639 INFO     29 [qwen-vl-parser] page=9 text: 53 sections
2026-08-05 05:37:24,766 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=968664, prompt_len=644
2026-08-05 05:37:26,144 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:37:26,145 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-05 05:37:26,152 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=968664, prompt_len=401
2026-08-05 05:37:29,378 INFO     29 [qwen-vl-parser] text API response (len=647):
["山西省医疗门诊收费票据（电子）", "山西省", "财政部监制", "票据代码:14060124", "交款人统一社会信用代", "交款", "票据号码:0155032568", "校验码: pc2vph", "开票日期:2026-01-06", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1.00", "466.00", "", "", "", "", "", "G布地格福吸入气雾剂【每瓶12", "2.00", "盒", "466.00 限慢性阻", "", "", "", "", "0揿】", "", "", "塞性肺疾", "", "", "", "", "", "", "病。", "", "", "", "", "金额合计（大写）肆佰陆拾陆元整", "(小写)466.00", "", "业务流水号", "门", "就诊日期:20260106", "型:综合医院", "医保类型:国家医保", "医保编号:", "48 性别:女", "医", "其他支付:0.00", "个人账户支付:0.00", "个人现金支付:156.11", "信", "t:309.89", "个人自费:156.11", "息", "自付:", "Z-方便门诊", "必泽斌号", "费专用章", "复核人:程小蕊", "收款人:段国丽", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:37:29,378 INFO     29 [qwen-vl-parser] page=10 text: 52 lines (bbox 327-378)
2026-08-05 05:37:29,379 INFO     29 [qwen-vl-parser] page=10 text: 52 sections
2026-08-05 05:37:29,541 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1362852, prompt_len=644
2026-08-05 05:37:31,018 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-03-15"
}
```
2026-08-05 05:37:31,019 INFO     29 [qwen-vl-parser] page=11 classify=table report_date=2024-03-15
2026-08-05 05:37:31,036 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1362852, prompt_len=756
2026-08-05 05:37:39,392 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:37:39.390+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"a0ac621a908f11f1a3da71efcdd7cc1f": {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:37:41,572 INFO     29 [qwen-vl-parser] table API response (len=1440):
\begin{tabular}{ccccccccc}
\hline
编码 & 项目名称 & 结果 & 参考区间 & 单位 & 编码 & 项目名称 & 结果 & 参考区间 & 单位 \\
\hline
1 & WBC & ★白细胞计数 & 4.06 & 3.50~9.50 *10~9/L & 14 & PDW & 血小板体积分布宽度 & 8.90 $\downarrow$ & 9.60~15.20 & fL \\
2 & RBC & ★红细胞计数 & 4.49 & 3.80~5.10*10~12/L & 15 & LYM\# & 淋巴细胞绝对值 & 1.42 & 1.10~3.20 *10~9/L & \\
3 & HGB & ★血红蛋白 & 131 & 115~150 & g/L & 16 & MON\# & 单核细胞绝对值 & 0.18 & 0.10~0.60 *10~9/L & \\
4 & HCT & ★红细胞压积 & 0.405 & 0.350~0.450 & L/L & 17 & NEU\# & 中性粒细胞绝对值 & 2.42 & 1.80~6.30 *10~9/L & \\
5 & MCV & ★红细胞平均体积 & 90.2 & 82.0~100.0 & fL & 18 & EOS\# & 嗜酸性粒细胞绝对值 & 0.03 & 0.02~0.52 *10~9/L & \\
6 & MCH & ★红细胞平均血红蛋白含量 29.2 & 27.0~34.0 & pg & 19 & BASO\# & 嗜碱性粒细胞绝对值 & 0.01 & 0.00~0.06 *10~9/L & \\
7 & MCHC & ★红细胞平均血红蛋白浓度 323 & 316~354 & g/L & 20 & LYM\% & 淋巴细胞百分比 & 35.00 & 20.00~50.00 & \% \\
8 & RDW-SD & 红细胞体积分布宽度SD & 40.60 $\downarrow$ & 41.20~53.60 & fL & 21 & MON\% & 单核细胞百分比 & 4.40 & 3.00~10.00 & \% \\
9 & RDW-CV & 红细胞体积分布宽度CV & 12.20 & 12.20~14.80 & \% & 22 & NEU\% & 中性粒细胞百分比 & 59.70 & 40.00~75.00 & \% \\
10 & PLT & ★血小板 & 280 & 125~350 *10~9/L & 23 & EOS\% & 嗜酸性粒细胞百分比 & 0.70 & 0.40~8.00 & \% \\
11 & PCT & 血小板压积 & 0.24 & 0.19~0.39 & \% & 24 & BASO\% & 嗜碱性粒细胞百分比 & 0.20 & 0.00~1.00 & \% \\
12 & MPV & 平均血小板体积 & 8.70 $\downarrow$ & 9.20~12.00 & fL & 25 & NRBC\# & 有核红细胞绝对值 & 0.0 & & *10~12/L \\
13 & P-LCR & 大血小板比率 & 15.30 $\downarrow$ & 19.70~42.40 & \% & 26 & NRBC\% & 有核红细胞百分比 & 0.0 & & /100WBC \\
\hline
\end{tabular}
2026-08-05 05:37:41,574 INFO     29 [qwen-vl-parser] page=11 table: 20 LaTeX lines (bbox 379-398)
2026-08-05 05:37:41,575 INFO     29 [qwen-vl-parser] page=11 table: 20 sections
2026-08-05 05:37:41,575 INFO     29 [qwen-vl-parser] parse_pdf done: 399 sections from 11 pages.
2026-08-05 05:37:41,588 INFO     29 Close text detector.
2026-08-05 05:37:41,921 INFO     29 Close text recognizer.
2026-08-05 05:37:42,254 INFO     29 Close recognizer.
2026-08-05 05:37:42,607 INFO     29 Close recognizer.
2026-08-05 05:37:42,942 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 05:37:42,942 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Parser:MedLink | outputs={"html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "json"}
2026-08-05 05:37:42,942 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 05:37:42,961 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:37:42,961 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 门诊电子病历（初诊）\n[BBOX-1] 姓名：\n[BBOX-2] 性别：女性\n[BBOX-3] 年龄：68岁\n[BBOX-4] 科室：呼吸与危重症医学门诊科\n[BBOX-5] 就诊时间：2026年01月19日16时48分\n[BBOX-6] 主诉：咳嗽、气短40余年，近一周加重\n[BBOX-7] 现病史：咳嗽、气短40余年，近一周加重，曾于当地医院诊断支气管哮喘，2024年3月因哮喘急性发作在\n[BBOX-8] 山大二院住院治疗，规律使用布地格福吸入气雾剂，加重1周\n[BBOX-9] 既往史：既往不详，未确认糖尿病病史，未确认高血压病史。\n[BBOX-10] 过敏史：未确认药物过敏史，未确认食物过敏史。\n[BBOX-11] 家族史：不详。\n[BBOX-12] 门诊诊断：支气管哮喘(急性发作期)\n[BBOX-13] 处理意见：醋酸泼尼松片、5mg*100片、15mg、口服、QD（每日一次）、1瓶；\n[BBOX-14] 医师签\n[BBOX-15] 第1页（共1页）\n[BBOX-16] 出院记录\n[BBOX-17] 姓名：\n[BBOX-18] 性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：\n[BBOX-19] 住院号：\n[BBOX-20] 姓名\n[BBOX-21] 性别：女\n[BBOX-22] 年龄：66岁\n[BBOX-23] 职业：农民\n[BBOX-24] 入院日期：2024年03月15日10时\n[BBOX-25] 出院日期：2024年03月18日11时\n[BBOX-26] 住院天数：3天\n[BBOX-27] 入院时情况：发作性喘息10年，加重2月。\n[BBOX-28] 入院诊断：1.支气管哮喘(急性发作期)\n[BBOX-29] 2.低氧血症\n[BBOX-30] 诊疗经过：完善相关化验及检查：\n[BBOX-31] 血气分析：吸氧浓度21.0%，酸碱度7.414，二氧化碳分压35.3mmHg，氧分压67.9mmHg↓，\n[BBOX-32] 实际碱剩余-1.4mmol/L，血浆碳酸氢盐浓度22.2mmol/L，乳酸浓度0.6mmol/\n[BBOX-33] L，氧合指数323mmHg↓，肺泡动脉氧分压差27.7mmHg↑。\n[BBOX-34] 血常规：白细胞计数4.06*10^9/L，红细胞计数4.49*10^12/L，血红蛋白131g/L，血小板\n[BBOX-35] 280*10^9/L。红细胞沉降率5mm/H。C反应蛋白2.43mg/L。\n[BBOX-36] 肝+肾+离子：血清丙氨酸氨基转移酶10.80U/L，血清天门冬氨酸氨基转移酶15.60U/L，尿\n[BBOX-37] 素4.40mmol/L，肌酐51.00umol/L，钾3.79mmol/L，钠143.00mmol/L，氯\n[BBOX-38] 109.00mmol/L。\n[BBOX-39] 免疫球蛋白：E128.00IU/mL↑。\n[BBOX-40] 呼吸道病原体抗体：阴性；新型冠状病毒核酸：阴性；痰培养：阴性；\n[BBOX-41] 尿常规：尿常规检验报告尿隐血-，尿白细胞3+，尿蛋白-，白细胞134个/uL↑。\n[BBOX-42] 肿瘤标志物、心肺四项、凝血、便常规未见明显异常。\n[BBOX-43] 腹部彩超：肝囊肿（多发）胆、胰、脾、双肾未见明显异常；\n[BBOX-44] 心脏彩超：EF：68% 三尖瓣口少量返流 主动脉瓣口少量返流 左室舒张功能减低 左室收\n[BBOX-45] 缩功能正常；\n[BBOX-46] 胸部CT：双肺实性微结节，建议随诊 肝内低密度灶，考虑囊肿。\n[BBOX-47] 肺功能：激发前：FEV1/FVC 86.86%，FEV1 96% FVC 90.2% 通气功能大致正常，吸入乙\n[BBOX-48] 酰甲胆碱 32mg/ml（第5管）激发后FEV1/FVC 72.8%，FEV1下降20.82%，激发\n[BBOX-49] 试验（+），DLCO 53.3% 肺弥散功能显著减退 RV/TLC 65.72%,残总比升高。\n[BBOX-50] 呼出气一氧化氮测定：FENO50 25ppb 混合型气道炎症 FENO200 18ppb 小气道炎症 CaNO\n[BBOX-51] 14.7ppb 肺泡炎症。FENO10 233。\n[BBOX-52] 2.予以抗过敏、扩张气道、促进排痰、抗感染等对症治疗。\n[BBOX-53] 第1页\n[BBOX-54] 出院记录\n[BBOX-55] 姓名：\n[BBOX-56] 性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：\n[BBOX-57] 床号：\n[BBOX-58] 出院时情况：患者气短明显缓解，偶有咳嗽，无明显咳痰，精神可。查体：口唇暗紫\n[BBOX-59] 色，咽部无充血，扁桃体无肿大；双肺未闻及干湿性啰音，心律齐，未闻及心脏瓣膜杂\n[BBOX-60] 音；腹软，无压痛、反跳痛，双下肢无水肿。\n[BBOX-61] 出院诊断：1.支气管哮喘(急性发作期)\n[BBOX-62] 2.低氧血症\n[BBOX-63] 3.肺部阴影(双肺结节性质待查)\n[BBOX-64] 4.多发性肝囊肿\n[BBOX-65] 出院医嘱：1、加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必\n[BBOX-66] 要时吸氧。\n[BBOX-67] 2、院外继续通药物治疗：\n[BBOX-68] 氯雷他定片 10 mg/片 口服 睡前(1月)\n[BBOX-69] 孟鲁司特片 10 mg/片 口服 睡前(1月)\n[BBOX-70] 布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 (3月)\n[BBOX-71] 茶碱缓释片 0.1g/片 口服 2次/日(长期)\n[BBOX-72] 3、3月后复查胸部高分辨CT，总IgE、肺功能+扩张+弥散\n[BBOX-73] 4、2周后呼吸科门诊复诊，不适随诊。\n[BBOX-74] 签名：\n[BBOX-75] 记录日期：2024年03月18日11时56分\n[BBOX-76] 第2页\n[BBOX-77] CT检查报告单\n[BBOX-78] 检查\n[BBOX-79] 病人姓名\n[BBOX-80] 性别：女\n[BBOX-81] 年龄：66岁\n[BBOX-82] 申请科室：呼吸与危重症二组\n[BBOX-83] 住院号：\n[BBOX-84] 门诊号：\n[BBOX-85] 造影剂：\n[BBOX-86] 检查部位：胸部高分辨平扫+矢冠状面重建\n[BBOX-87] 影像学表现：\n[BBOX-88] 双侧胸廓不对称，气管居中。双肺纹理清晰，走向自然，右肺下叶前基底段、\n[BBOX-89] 左肺下叶外基底段、左肺下叶背段均可见结节影，较大者直径约0.4cm，所见各支\n[BBOX-90] 气管腔通畅，纵隔内可肿大淋巴结，胸膜无增厚，胸腔内无积液。所扫肝内可见\n[BBOX-91] 多个类圆形低密度影，密度均匀，边界尚清。\n[BBOX-92] 初步诊断及建议：\n[BBOX-93] 双肺实性微结节，建议随诊\n[BBOX-94] 肝内低密度灶，考虑囊肿\n[BBOX-95] 录入者：\n[BBOX-96] 审核医\n[BBOX-97] 报告日期：2024.03.15 18:52:06\n[BBOX-98] 注：本报告仅供临床医师参考，本科室医师签字后有效。\n[BBOX-99] 【处方】导引单\n[BBOX-100] ID:\n[BBOX-101] 姓名:\n[BBOX-102] 年龄：68岁\n[BBOX-103] 性别：女\n[BBOX-104] 费别：普通患者\n[BBOX-105] 诊断：支气管哮喘(急性发作期)\n[BBOX-106] 开单科室：呼吸与危重症医学科\n[BBOX-107] 开单时间：2026-01-20 17:33:34\n[BBOX-108] 取药排\n[BBOX-109] 药品名称\n[BBOX-110] 规格\n[BBOX-111] 数量\n[BBOX-112] 1.醋酸泼尼松片\n[BBOX-113] 5mg*100片\n[BBOX-114] 1瓶\n[BBOX-115] 15.0mg\n[BBOX-116] 口服\n[BBOX-117] 每日一次\n[BBOX-118] 微信/支付宝\n[BBOX-119] 扫码支付\n[BBOX-120] 金额：4.8元\n[BBOX-121] 执行科室：门诊药房\n[BBOX-122] 地点：门诊大厅一层西侧\n[BBOX-123] 医生\n[BBOX-124] 处方当日有效，补打导引单不可作为取药凭证\n[BBOX-125] 【患者留存】\n[BBOX-126] ID:\n[BBOX-127] 姓名:\n[BBOX-128] 年龄：68岁\n[BBOX-129] 性别：女\n[BBOX-130] 药品名称\n[BBOX-131] 规格\n[BBOX-132] 数量\n[BBOX-133] 1.醋酸泼尼松片\n[BBOX-134] 5mg*100片\n[BBOX-135] 1瓶\n[BBOX-136] 15.0mg\n[BBOX-137] 口服\n[BBOX-138] 每日一次\n[BBOX-139] CS 扫描全能王\n[BBOX-140] 3亿人都在用的扫描App\n[BBOX-141] [G532]  心草招县西人乡连锁\n[BBOX-142] 店\n[BBOX-143] 交易日期：2025-10-31 11:43:49\n[BBOX-144] 销售单号：1325103100021472\n[BBOX-145] 收银员：\n[BBOX-146] 积分：543\n[BBOX-147] 品名\n[BBOX-148] 规格\n[BBOX-149] 150027(兴)布地格福吸入\n[BBOX-150] 气雾剂 倍择瑞_160ug:7.2u\n[BBOX-151] 单价:233.00\n[BBOX-152] 实价:233.00\n[BBOX-153] 数量:2.00\n[BBOX-154] 金额:466.00\n[BBOX-155] 批号：6103904C00\n[BBOX-156] 处方药\n[BBOX-157] 国码：XRO3ALB240L028010179096\n[BBOX-158] AstraZeneca AB\n[BBOX-159] 84471890087171843044\n[BBOX-160] 84471890087171828685\n[BBOX-161] 2、809245_一心堂卫生纸(原生\n[BBOX-162] 木浆(纤维))_1000g(4层*1\n[BBOX-163] 单价:11.80\n[BBOX-164] 实价:0.01\n[BBOX-165] 数量:1.00\n[BBOX-166] 金额:0.01\n[BBOX-167] 批号：20240825\n[BBOX-168] 国码：Q01000000\n[BBOX-169] 应收金额:477.8 优惠:11.8\n[BBOX-170] 实收金额:466.01找零:0.00\n[BBOX-171] 其中:收钱吧微信：\n[BBOX-172] 466.01\n[BBOX-173] *药品除质量问题，概不退换\n[BBOX-174] *服务不满意，\n[BBOX-175] *地址-电话·\n[BBOX-176] CS 扫描全能王\n[BBOX-177] 3亿人都在用的扫描App\n[BBOX-178] 山西省医疗门诊收费票据（电子）\n[BBOX-179] 山西省\n[BBOX-180] 财政部监制\n[BBOX-181] 票据号码：0040081955\n[BBOX-182] 校验码：itykbi\n[BBOX-183] 开票日期：2025-09-01\n[BBOX-184] 项目名称\n[BBOX-185] 数量/单位\n[BBOX-186] 金额（元）\n[BBOX-187] 备注\n[BBOX-188] 项目名称\n[BBOX-189] 数量/单位\n[BBOX-190] 金额（元）\n[BBOX-191] 备注\n[BBOX-192] 西药费\n[BBOX-193] 1\n[BBOX-194] 233.00\n[BBOX-195] G布地格福吸入气雾剂【每瓶12\n[BBOX-196] 1.00\n[BBOX-197] 盒\n[BBOX-198] 233.00 限慢性阻\n[BBOX-199] 0揿】\n[BBOX-200] 塞性肺疾\n[BBOX-201] 病。\n[BBOX-202] 金额合计（大写）贰佰叁拾叁元整\n[BBOX-203] (小写)233.00\n[BBOX-204] 业务流水号：07QIKH59659470P20250 门诊号：\n[BBOX-205] 就诊日期：20250901\n[BBOX-206] 901172144801\n[BBOX-207] （医\n[BBOX-208] 型：综合医院\n[BBOX-209] 医保类型：国家医保\n[BBOX-210] 医保码\n[BBOX-211] 医保统\n[BBOX-212] 支付：154.95\n[BBOX-213] 其他支付：0.00\n[BBOX-214] 个人账户支付：0.00\n[BBOX-215] 个人现金支付：78.05\n[BBOX-216] 付：0.0\n[BBOX-217] z-方便\n[BBOX-218] 费专用章\n[BBOX-219] 复核人：程小磊\n[BBOX-220] 收款\n[BBOX-221] CS 扫描全能王\n[BBOX-222] 3亿人都在用的扫描App\n[BBOX-223] 山西省医疗门诊收费票据（电子）\n[BBOX-224] 山西省\n[BBOX-225] 财政部监制\n[BBOX-226] 票据代码：\n[BBOX-227] 交款人话一社会信用代码：\n[BBOX-228] 交款人\n[BBOX-229] 票据号码：0039960248\n[BBOX-230] 校验码：isI3ej\n[BBOX-231] 开票日期：2025-07-08\n[BBOX-232] 项目名称\n[BBOX-233] 数量/单位\n[BBOX-234] 金额（元）\n[BBOX-235] 备注\n[BBOX-236] 项目名称\n[BBOX-237] 数量/单位\n[BBOX-238] 金额（元）\n[BBOX-239] 备注\n[BBOX-240] 西药费\n[BBOX-241] 1\n[BBOX-242] 466.00\n[BBOX-243] G布地格福吸入气雾剂【每瓶12\n[BBOX-244] 2.00\n[BBOX-245] 盒\n[BBOX-246] 466.00 限慢性阻\n[BBOX-247] 0揿】\n[BBOX-248] 塞性肺疾\n[BBOX-249] 病。\n[BBOX-250] 金额合计（大写）肆佰陆拾陆元整\n[BBOX-251] (小写)466.00\n[BBOX-252] 业务流水号：B7C8A658327630P20250 门诊号：\n[BBOX-253] 就诊日期：20250708\n[BBOX-254] 708113600815\n[BBOX-255] 类型：综合医院\n[BBOX-256] 医保类型：国家医保\n[BBOX-257] 医保编\n[BBOX-258] 医保.\n[BBOX-259] 付：309.89\n[BBOX-260] 其他支付：0.00\n[BBOX-261] 个人账户支付：0.00\n[BBOX-262] 个人现金支付：156.11\n[BBOX-263] 信\n[BBOX-264] 自付：\n[BBOX-265] 息\n[BBOX-266] Z-方便\n[BBOX-267] 靖号\n[BBOX-268] 个人自费：156.11\n[BBOX-269] 费专用\n[BBOX-270] 复核人：程小蕊\n[BBOX-271] 收款人：王丽\n[BBOX-272] CS 扫描全能王\n[BBOX-273] 3亿人都在用的扫描App\n[BBOX-274] 山西省医疗门诊收费票据（电子）\n[BBOX-275] 山西省\n[BBOX-276] 财政部监制\n[BBOX-277] 票据代码:1/\n[BBOX-278] 交款人统一社会信用代码:\n[BBOX-279] 交款\n[BBOX-280] 票据号码:0155140741\n[BBOX-281] 校验码: ci4u59\n[BBOX-282] 开票日期:2026-02-24\n[BBOX-283] 项目名称\n[BBOX-284] 数量/单位\n[BBOX-285] 金额（元）\n[BBOX-286] 备注\n[BBOX-287] 项目名称\n[BBOX-288] 数量/单位\n[BBOX-289] 金额（元）\n[BBOX-290] 备注\n[BBOX-291] 西药费\n[BBOX-292] 1.00\n[BBOX-293] 233.00\n[BBOX-294] G布地格福吸入气雾剂【每瓶12\n[BBOX-295] 1.00\n[BBOX-296] 盒\n[BBOX-297] 233.00 限慢性阻\n[BBOX-298] 0揿】\n[BBOX-299] 塞性肺疾\n[BBOX-300] 病。\n[BBOX-301] 金额合计（大写）贰佰叁拾叁元整\n[BBOX-302] (小写)233.00\n[BBOX-303] 业务流水号:2\n[BBOX-304] 门诊号:\n[BBOX-305] 就诊日期:20260224\n[BBOX-306] 2\n[BBOX-307] 类型:综合医院\n[BBOX-308] 医保类型:国家医保\n[BBOX-309] 医保编号\n[BBOX-310] 0548 性别:女\n[BBOX-311] 医保现\n[BBOX-312] 付:154.95\n[BBOX-313] 其他支付:0.00\n[BBOX-314] 个人账户支付:0.00\n[BBOX-315] 个人现金支付:78.05\n[BBOX-316] 信\n[BBOX-317] 自付:\n[BBOX-318] 总\n[BBOX-319] Z-方便\n[BBOX-320] 赵泽斌号\n[BBOX-321] 个人自费:78.05\n[BBOX-322] 费专用章\n[BBOX-323] 复核人:程小蕊\n[BBOX-324] 收款人:刘灵芝\n[BBOX-325] CS 扫描全能王\n[BBOX-326] 3亿人都在用的扫描App\n[BBOX-327] 山西省医疗门诊收费票据（电子）\n[BBOX-328] 山西省\n[BBOX-329] 财政部监制\n[BBOX-330] 票据代码:14060124\n[BBOX-331] 交款人统一社会信用代\n[BBOX-332] 交款\n[BBOX-333] 票据号码:0155032568\n[BBOX-334] 校验码: pc2vph\n[BBOX-335] 开票日期:2026-01-06\n[BBOX-336] 项目名称\n[BBOX-337] 数量/单位\n[BBOX-338] 金额（元）\n[BBOX-339] 备注\n[BBOX-340] 项目名称\n[BBOX-341] 数量/单位\n[BBOX-342] 金额（元）\n[BBOX-343] 备注\n[BBOX-344] 西药费\n[BBOX-345] 1.00\n[BBOX-346] 466.00\n[BBOX-347] G布地格福吸入气雾剂【每瓶12\n[BBOX-348] 2.00\n[BBOX-349] 盒\n[BBOX-350] 466.00 限慢性阻\n[BBOX-351] 0揿】\n[BBOX-352] 塞性肺疾\n[BBOX-353] 病。\n[BBOX-354] 金额合计（大写）肆佰陆拾陆元整\n[BBOX-355] (小写)466.00\n[BBOX-356] 业务流水号\n[BBOX-357] 门\n[BBOX-358] 就诊日期:20260106\n[BBOX-359] 型:综合医院\n[BBOX-360] 医保类型:国家医保\n[BBOX-361] 医保编号:\n[BBOX-362] 48 性别:女\n[BBOX-363] 医\n[BBOX-364] 其他支付:0.00\n[BBOX-365] 个人账户支付:0.00\n[BBOX-366] 个人现金支付:156.11\n[BBOX-367] 信\n[BBOX-368] t:309.89\n[BBOX-369] 个人自费:156.11\n[BBOX-370] 息\n[BBOX-371] 自付:\n[BBOX-372] Z-方便门诊\n[BBOX-373] 必泽斌号\n[BBOX-374] 费专用章\n[BBOX-375] 复核人:程小蕊\n[BBOX-376] 收款人:段国丽\n[BBOX-377] CS 扫描全能王\n[BBOX-378] 3亿人都在用的扫描App\n[BBOX-379] \\begin{tabular}{ccccccccc}\n[BBOX-380] 报告时间: 2024-03-15\n[BBOX-381] \\hline\n[BBOX-382] 编码 & 项目名称 & 结果 & 参考区间 & 单位 & 编码 & 项目名称 & 结果 & 参考区间 & 单位 \\\\\n[BBOX-383] \\hline\n[BBOX-384] 1 & WBC & ★白细胞计数 & 4.06 & 3.50~9.50 *10~9/L & 14 & PDW & 血小板体积分布宽度 & 8.90 $\\downarrow$ & 9.60~15.20 & fL \\\\\n[BBOX-385] 2 & RBC & ★红细胞计数 & 4.49 & 3.80~5.10*10~12/L & 15 & LYM\\# & 淋巴细胞绝对值 & 1.42 & 1.10~3.20 *10~9/L & \\\\\n[BBOX-386] 3 & HGB & ★血红蛋白 & 131 & 115~150 & g/L & 16 & MON\\# & 单核细胞绝对值 & 0.18 & 0.10~0.60 *10~9/L & \\\\\n[BBOX-387] 4 & HCT & ★红细胞压积 & 0.405 & 0.350~0.450 & L/L & 17 & NEU\\# & 中性粒细胞绝对值 & 2.42 & 1.80~6.30 *10~9/L & \\\\\n[BBOX-388] 5 & MCV & ★红细胞平均体积 & 90.2 & 82.0~100.0 & fL & 18 & EOS\\# & 嗜酸性粒细胞绝对值 & 0.03 & 0.02~0.52 *10~9/L & \\\\\n[BBOX-389] 6 & MCH & ★红细胞平均血红蛋白含量 29.2 & 27.0~34.0 & pg & 19 & BASO\\# & 嗜碱性粒细胞绝对值 & 0.01 & 0.00~0.06 *10~9/L & \\\\\n[BBOX-390] 7 & MCHC & ★红细胞平均血红蛋白浓度 323 & 316~354 & g/L & 20 & LYM\\% & 淋巴细胞百分比 & 35.00 & 20.00~50.00 & \\% \\\\\n[BBOX-391] 8 & RDW-SD & 红细胞体积分布宽度SD & 40.60 $\\downarrow$ & 41.20~53.60 & fL & 21 & MON\\% & 单核细胞百分比 & 4.40 & 3.00~10.00 & \\% \\\\\n[BBOX-392] 9 & RDW-CV & 红细胞体积分布宽度CV & 12.20 & 12.20~14.80 & \\% & 22 & NEU\\% & 中性粒细胞百分比 & 59.70 & 40.00~75.00 & \\% \\\\\n[BBOX-393] 10 & PLT & ★血小板 & 280 & 125~350 *10~9/L & 23 & EOS\\% & 嗜酸性粒细胞百分比 & 0.70 & 0.40~8.00 & \\% \\\\\n[BBOX-394] 11 & PCT & 血小板压积 & 0.24 & 0.19~0.39 & \\% & 24 & BASO\\% & 嗜碱性粒细胞百分比 & 0.20 & 0.00~1.00 & \\% \\\\\n[BBOX-395] 12 & MPV & 平均血小板体积 & 8.70 $\\downarrow$ & 9.20~12.00 & fL & 25 & NRBC\\# & 有核红细胞绝对值 & 0.0 & & *10~12/L \\\\\n[BBOX-396] 13 & P-LCR & 大血小板比率 & 15.30 $\\downarrow$ & 19.70~42.40 & \\% & 26 & NRBC\\% & 有核红细胞百分比 & 0.0 & & /100WBC \\\\\n[BBOX-397] \\hline\n[BBOX-398] \\end{tabular}"
  }
]
2026-08-05 05:37:52,763 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:37:52,781 INFO     29 [SmartSplitter] SmartSplitter done: 10 chunks from 10 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1, 'MedicationRecord': 5, 'LabReport': 1}
2026-08-05 05:37:52,789 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 05:37:52,789 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks": "10 items, types={'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1, 'MedicationRecord': 5, 'LabReport': 1}"}
2026-08-05 05:37:52,789 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 05:37:52,789 INFO     29 [ChunkRouter] Routed 10 chunks into 6 groups: {'chunks_Clinical': 1, 'chunks_Discharge': 1, 'chunks_Examination': 1, 'chunks_Prescription': 1, 'chunks_Medication': 5, 'chunks_LabExam': 1}
2026-08-05 05:37:52,796 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 05:37:52,796 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks": "10 items, types={'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1, 'PrescriptionRecord': 1, 'MedicationRecord': 5, 'LabReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:37:52,796 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 05:37:52,800 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:37:52,800 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[10]
2026-08-05 05:37:52,800 INFO     29 [qwen-vl-table] positions ： [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:37:52,999 INFO     29 [qwen-vl-table] page=10, rect=842x595, img=(2339x1653)
2026-08-05 05:37:53,000 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:37:53,000 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 379, \"bbox_end\": 398, \"encounter_dates\": [\"2024-03-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2024-03-15\n\\hline\n编码 & 项目名称 & 结果 & 参考区间 & 单位 & 编码 & 项目名称 & 结果 & 参考区间 & 单位 \\\\\n\\hline\n1 & WBC & ★白细胞计数 & 4.06 & 3.50~9.50 *10~9/L & 14 & PDW & 血小板体积分布宽度 & 8.90 $\\downarrow$ & 9.60~15.20 & fL \\\\\n2 & RBC & ★红细胞计数 & 4.49 & 3.80~5.10*10~12/L & 15 & LYM\\# & 淋巴细胞绝对值 & 1.42 & 1.10~3.20 *10~9/L & \\\\\n3 & HGB & ★血红蛋白 & 131 & 115~150 & g/L & 16 & MON\\# & 单核细胞绝对值 & 0.18 & 0.10~0.60 *10~9/L & \\\\\n4 & HCT & ★红细胞压积 & 0.405 & 0.350~0.450 & L/L & 17 & NEU\\# & 中性粒细胞绝对值 & 2.42 & 1.80~6.30 *10~9/L & \\\\\n5 & MCV & ★红细胞平均体积 & 90.2 & 82.0~100.0 & fL & 18 & EOS\\# & 嗜酸性粒细胞绝对值 & 0.03 & 0.02~0.52 *10~9/L & \\\\\n6 & MCH & ★红细胞平均血红蛋白含量 29.2 & 27.0~34.0 & pg & 19 & BASO\\# & 嗜碱性粒细胞绝对值 & 0.01 & 0.00~0.06 *10~9/L & \\\\\n7 & MCHC & ★红细胞平均血红蛋白浓度 323 & 316~354 & g/L & 20 & LYM\\% & 淋巴细胞百分比 & 35.00 & 20.00~50.00 & \\% \\\\\n8 & RDW-SD & 红细胞体积分布宽度SD & 40.60 $\\downarrow$ & 41.20~53.60 & fL & 21 & MON\\% & 单核细胞百分比 & 4.40 & 3.00~10.00 & \\% \\\\\n9 & RDW-CV & 红细胞体积分布宽度CV & 12.20 & 12.20~14.80 & \\% & 22 & NEU\\% & 中性粒细胞百分比 & 59.70 & 40.00~75.00 & \\% \\\\\n10 & PLT & ★血小板 & 280 & 125~350 *10~9/L & 23 & EOS\\% & 嗜酸性粒细胞百分比 & 0.70 & 0.40~8.00 & \\% \\\\\n11 & PCT & 血小板压积 & 0.24 & 0.19~0.39 & \\% & 24 & BASO\\% & 嗜碱性粒细胞百分比 & 0.20 & 0.00~1.00 & \\% \\\\\n12 & MPV & 平均血小板体积 & 8.70 $\\downarrow$ & 9.20~12.00 & fL & 25 & NRBC\\# & 有核红细胞绝对值 & 0.0 & & *10~12/L \\\\\n13 & P-LCR & 大血小板比率 & 15.30 $\\downarrow$ & 19.70~42.40 & \\% & 26 & NRBC\\% & 有核红细胞百分比 & 0.0 & & /100WBC \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m05:37:53 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:37:53,001 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:38:12,190 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:38:12.189+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"a0ac621a908f11f1a3da71efcdd7cc1f": {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:38:27,050 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:38:27,050 INFO     29 [qwen-vl-table] page=10 LLM output (len=4523):
{
  "report_date": "2024-03-15",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "4.06",
      "unit": "*10~9/L",
      "reference_range": "3.50~9.50",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "4.49",
      "unit": "*10~12/L",
      "reference_range": "3.80~5.10",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "131",
      "unit": "g/L",
      "reference_range": "115~150",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "0.405",
      "unit": "L/L",
      "reference_range": "0.350~0.450",
      "abnormal": false
    },
    {
      "name": "红细胞平均体积",
      "item_code": "MCV",
      "value": "90.2",
      "unit": "fL",
      "reference_range": "82.0~100.0",
      "abnormal": false
    },
    {
      "name": "红细胞平均血红蛋白含量",
      "item_code": "MCH",
      "value": "29.2",
      "unit": "pg",
      "reference_range": "27.0~34.0",
      "abnormal": false
    },
    {
      "name": "红细胞平均血红蛋白浓度",
      "item_code": "MCHC",
      "value": "323",
      "unit": "g/L",
      "reference_range": "316~354",
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度SD",
      "item_code": "RDW-SD",
      "value": "40.60",
      "unit": "fL",
      "reference_range": "41.20~53.60",
      "abnormal": true
    },
    {
      "name": "红细胞体积分布宽度CV",
      "item_code": "RDW-CV",
      "value": "12.20",
      "unit": "%",
      "reference_range": "12.20~14.80",
      "abnormal": false
    },
    {
      "name": "血小板",
      "item_code": "PLT",
      "value": "280",
      "unit": "*10~9/L",
      "reference_range": "125~350",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.24",
      "unit": "%",
      "reference_range": "0.19~0.39",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "8.70",
      "unit": "fL",
      "reference_range": "9.20~12.00",
      "abnormal": true
    },
    {
      "name": "大血小板比率",
      "item_code": "P-LCR",
      "value": "15.30",
      "unit": "%",
      "reference_range": "19.70~42.40",
      "abnormal": true
    },
    {
      "name": "血小板体积分布宽度",
      "item_code": "PDW",
      "value": "8.90",
      "unit": "fL",
      "reference_range": "9.60~15.20",
      "abnormal": true
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LYM#",
      "value": "1.42",
      "unit": "*10~9/L",
      "reference_range": "1.10~3.20",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MON#",
      "value": "0.18",
      "unit": "*10~9/L",
      "reference_range": "0.10~0.60",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NEU#",
      "value": "2.42",
      "unit": "*10~9/L",
      "reference_range": "1.80~6.30",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": "EOS#",
      "value": "0.03",
      "unit": "*10~9/L",
      "reference_range": "0.02~0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": "BASO#",
      "value": "0.01",
      "unit": "*10~9/L",
      "reference_range": "0.00~0.06",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "LYM%",
      "value": "35.00",
      "unit": "%",
      "reference_range": "20.00~50.00",
      "abnormal": false
    },
    {
      "name": "单核细胞百分比",
      "item_code": "MON%",
      "value": "4.40",
      "unit": "%",
      "reference_range": "3.00~10.00",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "NEU%",
      "value": "59.70",
      "unit": "%",
      "reference_range": "40.00~75.00",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分比",
      "item_code": "EOS%",
      "value": "0.70",
      "unit": "%",
      "reference_range": "0.40~8.00",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分比",
      "item_code": "BASO%",
      "value": "0.20",
      "unit": "%",
      "reference_range": "0.00~1.00",
      "abnormal": false
    },
    {
      "name": "有核红细胞绝对值",
      "item_code": "NRBC#",
      "value": "0.0",
      "unit": "*10~12/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "有核红细胞百分比",
      "item_code": "NRBC%",
      "value": "0.0",
      "unit": "/100WBC",
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-05 05:38:27,050 INFO     29 [qwen-vl-table] coord grouping: {10: 26}
2026-08-05 05:38:27,055 INFO     29 [qwen-vl-table] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1226057, prompt_len=728
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、红细胞计数、血红蛋白、红细胞压积、红细胞平均体积、红细胞平均血红蛋白含量、红细胞平均血红蛋白浓度、红细胞体积分布宽度SD、红细胞体积分布宽度CV、血小板、血小板压积、平均血小板体积、大血小板比率、血小板体积分布宽度、淋巴细胞绝对值、单核细胞绝对值、中性粒细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、淋巴细胞百分比、单核细胞百分比、中性粒细胞百分比、嗜酸性粒细胞百分比、嗜碱性粒细胞百分比、有核红细胞绝对值、有核红细胞百分比

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
2026-08-05 05:38:34,524 INFO     29 [qwen-vl-table] coord API raw response (len=1366):
[
	{"text": "白细胞计数", "bbox": [103, 317, 192, 339]},
	{"text": "红细胞计数", "bbox": [103, 353, 192, 375]},
	{"text": "血红蛋白", "bbox": [103, 389, 176, 411]},
	{"text": "红细胞压积", "bbox": [103, 425, 192, 447]},
	{"text": "红细胞平均体积", "bbox": [103, 461, 221, 483]},
	{"text": "红细胞平均血红蛋白含量", "bbox": [103, 497, 285, 519]},
	{"text": "红细胞平均血红蛋白浓度", "bbox": [103, 533, 285, 555]},
	{"text": "红细胞体积分布宽度SD", "bbox": [60, 569, 255, 591]},
	{"text": "红细胞体积分布宽度CV", "bbox": [60, 605, 255, 627]},
	{"text": "血小板", "bbox": [103, 641, 160, 663]},
	{"text": "血小板压积", "bbox": [103, 677, 176, 699]},
	{"text": "平均血小板体积", "bbox": [103, 713, 204, 735]},
	{"text": "大血小板比率", "bbox": [103, 747, 190, 769]},
	{"text": "血小板体积分布宽度", "bbox": [581, 317, 715, 339]},
	{"text": "淋巴细胞绝对值", "bbox": [581, 353, 686, 375]},
	{"text": "单核细胞绝对值", "bbox": [581, 389, 686, 411]},
	{"text": "中性粒细胞绝对值", "bbox": [581, 425, 700, 447]},
	{"text": "嗜酸性粒细胞绝对值", "bbox": [581, 461, 715, 483]},
	{"text": "嗜碱性粒细胞绝对值", "bbox": [581, 497, 715, 519]},
	{"text": "淋巴细胞百分比", "bbox": [581, 533, 686, 555]},
	{"text": "单核细胞百分比", "bbox": [581, 569, 686, 591]},
	{"text": "中性粒细胞百分比", "bbox": [581, 605, 699, 627]},
	{"text": "嗜酸性粒细胞百分比", "bbox": [581, 641, 715, 663]},
	{"text": "嗜碱性粒细胞百分比", "bbox": [581, 677, 715, 699]},
	{"text": "有核红细胞绝对值", "bbox": [581, 713, 697, 735]},
	{"text": "有核红细胞百分比", "bbox": [581, 747, 697, 769]}
]
2026-08-05 05:38:34,524 INFO     29 [qwen-vl-table] coord API: raw_items=26, valid_items=26, elapsed=7.5s
2026-08-05 05:38:34,524 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[103, 317, 192, 339]
2026-08-05 05:38:34,524 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞计数, bbox=[103, 353, 192, 375]
2026-08-05 05:38:34,524 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白, bbox=[103, 389, 176, 411]
2026-08-05 05:38:34,524 INFO     29 [qwen-vl-table] coord item[3]: text=红细胞压积, bbox=[103, 425, 192, 447]
2026-08-05 05:38:34,524 INFO     29 [qwen-vl-table] coord item[4]: text=红细胞平均体积, bbox=[103, 461, 221, 483]
2026-08-05 05:38:34,524 INFO     29 [qwen-vl-table] coord item[5]: text=红细胞平均血红蛋白含量, bbox=[103, 497, 285, 519]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[6]: text=红细胞平均血红蛋白浓度, bbox=[103, 533, 285, 555]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[7]: text=红细胞体积分布宽度SD, bbox=[60, 569, 255, 591]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[8]: text=红细胞体积分布宽度CV, bbox=[60, 605, 255, 627]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[9]: text=血小板, bbox=[103, 641, 160, 663]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[10]: text=血小板压积, bbox=[103, 677, 176, 699]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[11]: text=平均血小板体积, bbox=[103, 713, 204, 735]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[12]: text=大血小板比率, bbox=[103, 747, 190, 769]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[13]: text=血小板体积分布宽度, bbox=[581, 317, 715, 339]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[14]: text=淋巴细胞绝对值, bbox=[581, 353, 686, 375]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[15]: text=单核细胞绝对值, bbox=[581, 389, 686, 411]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[16]: text=中性粒细胞绝对值, bbox=[581, 425, 700, 447]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[17]: text=嗜酸性粒细胞绝对值, bbox=[581, 461, 715, 483]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[18]: text=嗜碱性粒细胞绝对值, bbox=[581, 497, 715, 519]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[19]: text=淋巴细胞百分比, bbox=[581, 533, 686, 555]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[20]: text=单核细胞百分比, bbox=[581, 569, 686, 591]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[21]: text=中性粒细胞百分比, bbox=[581, 605, 699, 627]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[22]: text=嗜酸性粒细胞百分比, bbox=[581, 641, 715, 663]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[23]: text=嗜碱性粒细胞百分比, bbox=[581, 677, 715, 699]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[24]: text=有核红细胞绝对值, bbox=[581, 713, 697, 735]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] coord item[25]: text=有核红细胞百分比, bbox=[581, 747, 697, 769]
2026-08-05 05:38:34,525 INFO     29 [qwen-vl-table] page=10 coord: matched 26/26, time=7.5s
2026-08-05 05:38:34,526 INFO     29 [qwen-vl-table] new_positions (26):
[[11, 86.726, 161.664, 188.61499999999998, 201.70499999999998], [11, 86.726, 161.664, 210.035, 223.125], [11, 86.726, 148.192, 231.45499999999998, 244.545], [11, 86.726, 161.664, 252.875, 265.965], [11, 86.726, 186.082, 274.295, 287.385], [11, 86.726, 239.97, 295.715, 308.805], [11, 86.726, 239.97, 317.135, 330.22499999999997], [11, 50.519999999999996, 214.70999999999998, 338.555, 351.645], [11, 50.519999999999996, 214.70999999999998, 359.97499999999997, 373.065], [11, 86.726, 134.72, 381.395, 394.48499999999996], [11, 86.726, 148.192, 402.815, 415.905], [11, 86.726, 171.768, 424.23499999999996, 437.325], [11, 86.726, 159.98, 444.465, 457.555], [11, 489.202, 602.03, 188.61499999999998, 201.70499999999998], [11, 489.202, 577.612, 210.035, 223.125], [11, 489.202, 577.612, 231.45499999999998, 244.545], [11, 489.202, 589.4, 252.875, 265.965], [11, 489.202, 602.03, 274.295, 287.385], [11, 489.202, 602.03, 295.715, 308.805], [11, 489.202, 577.612, 317.135, 330.22499999999997], [11, 489.202, 577.612, 338.555, 351.645], [11, 489.202, 588.558, 359.97499999999997, 373.065], [11, 489.202, 602.03, 381.395, 394.48499999999996], [11, 489.202, 602.03, 402.815, 415.905], [11, 489.202, 586.874, 424.23499999999996, 437.325], [11, 489.202, 586.874, 444.465, 457.555]]
2026-08-05 05:38:34,526 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=26, matched=26, pages=1, time=41.7s
2026-08-05 05:38:34,534 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 05:38:34,534 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:38:34,534 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 05:38:34,538 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:38:34,538 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:38:34 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:38:34,539 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:38:35,518 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:38:35,523 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 05:38:35,523 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:38:35,523 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 05:38:35,527 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:38:35,527 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:38:35,527 INFO     29 [qwen-vl-text] positions(16): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:38:35,527 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [16]
2026-08-05 05:38:35,680 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:38:35,681 INFO     29 [qwen-vl-text] LLM extraction start, text_len=294
2026-08-05 05:38:35,681 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:38:35,682 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 15, \"encounter_dates\": [\"2026-01-19\"], \"department\": \"呼吸与危重症医学门诊科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊电子病历（初诊）\n姓名：\n性别：女性\n年龄：68岁\n科室：呼吸与危重症医学门诊科\n就诊时间：2026年01月19日16时48分\n主诉：咳嗽、气短40余年，近一周加重\n现病史：咳嗽、气短40余年，近一周加重，曾于当地医院诊断支气管哮喘，2024年3月因哮喘急性发作在\n山大二院住院治疗，规律使用布地格福吸入气雾剂，加重1周\n既往史：既往不详，未确认糖尿病病史，未确认高血压病史。\n过敏史：未确认药物过敏史，未确认食物过敏史。\n家族史：不详。\n门诊诊断：支气管哮喘(急性发作期)\n处理意见：醋酸泼尼松片、5mg*100片、15mg、口服、QD（每日一次）、1瓶；\n医师签\n第1页（共1页）",
    "role": "user"
  }
]
[92m05:38:35 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:38:35,683 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:38:38,185 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:38:38,185 INFO     29 [qwen-vl-text] LLM output (len=333):
{
  "encounter_date": "2026-01-19",
  "chief_complaint": "咳嗽、气短40余年，近一周加重",
  "present_illness": "咳嗽、气短40余年，近一周加重，曾于当地医院诊断支气管哮喘，2024年3月因哮喘急性发作在山大二院住院治疗，规律使用布地格福吸入气雾剂，加重1周",
  "past_history": "既往不详，未确认糖尿病病史，未确认高血压病史。未确认药物过敏史，未确认食物过敏史。家族史：不详。",
  "diagnosis": "支气管哮喘(急性发作期)",
  "treatment_plan": "醋酸泼尼松片 5mg*100片 15mg 口服 QD（每日一次） 1瓶"
}
2026-08-05 05:38:38,185 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-19]
2026-08-05 05:38:38,186 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=578991, prompt_len=955
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["门诊电子病历（初诊）", "姓名：", "性别：女性", "年龄：68岁", "科室：呼吸与危重症医学门诊科", "就诊时间：2026年01月19日16时48分", "主诉：咳嗽、气短40余年，近一周加重", "现病史：咳嗽、气短40余年，近一周加重，曾于当地医院诊断支气管哮喘，2024年3月因哮喘急性发作在", "山大二院住院治疗，规律使用布地格福吸入气雾剂，加重1周", "既往史：既往不详，未确认糖尿病病史，未确认高血压病史。", "过敏史：未确认药物过敏史，未确认食物过敏史。", "家族史：不详。", "门诊诊断：支气管哮喘(急性发作期)", "处理意见：醋酸泼尼松片、5mg*100片、15mg、口服、QD（每日一次）、1瓶；", "医师签", "第1页（共1页）"]

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
2026-08-05 05:38:43,773 INFO     29 [qwen-vl-text] coord API raw response (len=990):
[
	{"text": "门诊电子病历（初诊）", "bbox": [315, 139, 643, 187]},
	{"text": "姓名：", "bbox": [83, 206, 99, 228]},
	{"text": "性别：女性", "bbox": [238, 206, 311, 228]},
	{"text": "年龄：68岁", "bbox": [377, 206, 450, 228]},
	{"text": "科室：呼吸与危重症医学门诊科", "bbox": [500, 206, 721, 263]},
	{"text": "就诊时间：2026年01月19日16时48分", "bbox": [82, 296, 344, 319]},
	{"text": "主诉：咳嗽、气短40余年，近一周加重", "bbox": [82, 326, 408, 350]},
	{"text": "现病史：咳嗽、气短40余年，近一周加重，曾于当地医院诊断支气管哮喘，2024年3月因哮喘急性发作在", "bbox": [82, 357, 896, 381]},
	{"text": "山大二院住院治疗，规律使用布地格福吸入气雾剂，加重1周", "bbox": [82, 388, 540, 412]},
	{"text": "既往史：既往不详，未确认糖尿病病史，未确认高血压病史。", "bbox": [82, 418, 530, 442]},
	{"text": "过敏史：未确认药物过敏史，未确认食物过敏史。", "bbox": [82, 448, 450, 472]},
	{"text": "家族史：不详。", "bbox": [82, 478, 205, 502]},
	{"text": "门诊诊断：支气管哮喘(急性发作期)", "bbox": [82, 508, 342, 532]},
	{"text": "处理意见：醋酸泼尼松片、5mg*100片、15mg、口服、QD（每日一次）、1瓶；", "bbox": [82, 538, 626, 562]},
	{"text": "医师签", "bbox": [572, 610, 622, 634]},
	{"text": "第1页（共1页）", "bbox": [422, 867, 540, 890]}
]
2026-08-05 05:38:43,773 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.6s
2026-08-05 05:38:43,773 INFO     29 [qwen-vl-text] coord item[0]: text=门诊电子病历（初诊）, bbox=[315, 139, 643, 187]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[83, 206, 99, 228]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女性, bbox=[238, 206, 311, 228]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：68岁, bbox=[377, 206, 450, 228]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸与危重症医学门诊科, bbox=[500, 206, 721, 263]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[5]: text=就诊时间：2026年01月19日16时48分, bbox=[82, 296, 344, 319]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：咳嗽、气短40余年，近一周加重, bbox=[82, 326, 408, 350]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：咳嗽、气短40余年，近一周加重，曾于当地医院诊断支气管哮喘，2024年3月因哮喘急性发作在, bbox=[82, 357, 896, 381]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[8]: text=山大二院住院治疗，规律使用布地格福吸入气雾剂，加重1周, bbox=[82, 388, 540, 412]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：既往不详，未确认糖尿病病史，未确认高血压病史。, bbox=[82, 418, 530, 442]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[10]: text=过敏史：未确认药物过敏史，未确认食物过敏史。, bbox=[82, 448, 450, 472]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[11]: text=家族史：不详。, bbox=[82, 478, 205, 502]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[12]: text=门诊诊断：支气管哮喘(急性发作期), bbox=[82, 508, 342, 532]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[13]: text=处理意见：醋酸泼尼松片、5mg*100片、15mg、口服、QD（每日一次）、1瓶；, bbox=[82, 538, 626, 562]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[14]: text=医师签, bbox=[572, 610, 622, 634]
2026-08-05 05:38:43,774 INFO     29 [qwen-vl-text] coord item[15]: text=第1页（共1页）, bbox=[422, 867, 540, 890]
2026-08-05 05:38:43,775 INFO     29 [qwen-vl-text] page=0 — 16/16 coords, api_time=5.6s
2026-08-05 05:38:43,775 INFO     29 [qwen-vl-text] new_positions (16):
[[0, 265.23, 541.406, 82.705, 111.265], [0, 69.886, 83.358, 122.57, 135.66], [0, 200.396, 261.86199999999997, 122.57, 135.66], [0, 317.43399999999997, 378.9, 122.57, 135.66], [0, 421.0, 607.082, 122.57, 156.48499999999999], [0, 69.044, 289.64799999999997, 176.12, 189.80499999999998], [0, 69.044, 343.536, 193.97, 208.25], [0, 69.044, 754.432, 212.415, 226.695], [0, 69.044, 454.68, 230.85999999999999, 245.14], [0, 69.044, 446.26, 248.70999999999998, 262.99], [0, 69.044, 378.9, 266.56, 280.84], [0, 69.044, 172.60999999999999, 284.40999999999997, 298.69], [0, 69.044, 287.964, 302.26, 316.53999999999996], [0, 69.044, 527.092, 320.11, 334.39], [0, 481.62399999999997, 523.7239999999999, 362.95, 377.22999999999996], [0, 355.324, 454.68, 515.865, 529.55]]
2026-08-05 05:38:43,775 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=8.2s
2026-08-05 05:38:43,786 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 05:38:43,786 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:38:43,786 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 05:38:43,787 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:38:43.786+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"a0ac621a908f11f1a3da71efcdd7cc1f": {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:38:43,793 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:38:43,793 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:38:43,793 INFO     29 [qwen-vl-text] positions(35): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:38:43,793 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [35]
2026-08-05 05:38:43,930 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:38:43,931 INFO     29 [qwen-vl-text] LLM extraction start, text_len=440
2026-08-05 05:38:43,931 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:38:43,932 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 141, \"bbox_end\": 175, \"encounter_dates\": [\"2025-10-31\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "[G532]  心草招县西人乡连锁\n店\n交易日期：2025-10-31 11:43:49\n销售单号：1325103100021472\n收银员：\n积分：543\n品名\n规格\n150027(兴)布地格福吸入\n气雾剂 倍择瑞_160ug:7.2u\n单价:233.00\n实价:233.00\n数量:2.00\n金额:466.00\n批号：6103904C00\n处方药\n国码：XRO3ALB240L028010179096\nAstraZeneca AB\n84471890087171843044\n84471890087171828685\n2、809245_一心堂卫生纸(原生\n木浆(纤维))_1000g(4层*1\n单价:11.80\n实价:0.01\n数量:1.00\n金额:0.01\n批号：20240825\n国码：Q01000000\n应收金额:477.8 优惠:11.8\n实收金额:466.01找零:0.00\n其中:收钱吧微信：\n466.01\n*药品除质量问题，概不退换\n*服务不满意，\n*地址-电话·",
    "role": "user"
  }
]
[92m05:38:43 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:38:43,933 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:38:46,719 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:38:46,719 INFO     29 [qwen-vl-text] LLM output (len=440):
{
  "encounter_date": "2025-10-31",
  "pharmacy": "心草招县西人乡连锁店",
  "medications": [
    {
      "name": "布地格福吸入气雾剂(倍择瑞)",
      "specification": "160ug:7.2ug",
      "dosage": null,
      "quantity": 2,
      "unit_price": 233.0,
      "total_price": 466.0,
      "frequency": null,
      "route": null,
      "manufacturer": "AstraZeneca AB",
      "approval_number": null
    }
  ],
  "payment_total": 466.01,
  "payment_method": "收钱吧微信"
}
2026-08-05 05:38:46,719 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-31]
2026-08-05 05:38:46,721 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=881793, prompt_len=1158
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["[G532]  心草招县西人乡连锁", "店", "交易日期：2025-10-31 11:43:49", "销售单号：1325103100021472", "收银员：", "积分：543", "品名", "规格", "150027(兴)布地格福吸入", "气雾剂 倍择瑞_160ug:7.2u", "单价:233.00", "实价:233.00", "数量:2.00", "金额:466.00", "批号：6103904C00", "处方药", "国码：XRO3ALB240L028010179096", "AstraZeneca AB", "84471890087171843044", "84471890087171828685", "2、809245_一心堂卫生纸(原生", "木浆(纤维))_1000g(4层*1", "单价:11.80", "实价:0.01", "数量:1.00", "金额:0.01", "批号：20240825", "国码：Q01000000", "应收金额:477.8 优惠:11.8", "实收金额:466.01找零:0.00", "其中:收钱吧微信：", "466.01", "*药品除质量问题，概不退换", "*服务不满意，", "*地址-电话·"]

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
2026-08-05 05:38:58,484 INFO     29 [qwen-vl-text] coord API raw response (len=1993):
```json
[
	{"text": "[G532]  心草招县西人乡连锁", "bbox": [270, 68, 654, 91]},
	{"text": "店", "bbox": [269, 100, 295, 117]},
	{"text": "交易日期：2025-10-31 11:43:49", "bbox": [270, 122, 669, 144]},
	{"text": "销售单号：1325103100021472", "bbox": [270, 150, 613, 172]},
	{"text": "收银员：", "bbox": [270, 178, 364, 200]},
	{"text": "积分：543", "bbox": [546, 206, 671, 228]},
	{"text": "品名", "bbox": [382, 234, 435, 256]},
	{"text": "规格", "bbox": [545, 234, 601, 256]},
	{"text": "150027(兴)布地格福吸入", "bbox": [315, 289, 657, 312]},
	{"text": "气雾剂 倍择瑞_160ug:7.2u", "bbox": [272, 318, 603, 341]},
	{"text": "单价:233.00", "bbox": [270, 346, 423, 368]},
	{"text": "实价:233.00", "bbox": [480, 345, 631, 368]},
	{"text": "数量:2.00", "bbox": [270, 374, 396, 397]},
	{"text": "金额:466.00", "bbox": [452, 373, 605, 396]},
	{"text": "批号：6103904C00", "bbox": [270, 402, 495, 425]},
	{"text": "处方药", "bbox": [521, 402, 605, 424]},
	{"text": "国码：XRO3ALB240L028010179096", "bbox": [270, 430, 676, 453]},
	{"text": "AstraZeneca AB", "bbox": [270, 460, 466, 482]},
	{"text": "84471890087171843044", "bbox": [270, 488, 550, 511]},
	{"text": "84471890087171828685", "bbox": [270, 516, 550, 539]},
	{"text": "2、809245_一心堂卫生纸(原生", "bbox": [270, 545, 649, 568]},
	{"text": "木浆(纤维))_1000g(4层*1", "bbox": [270, 573, 590, 596]},
	{"text": "单价:11.80", "bbox": [270, 602, 410, 625]},
	{"text": "实价:0.01", "bbox": [467, 602, 590, 625]},
	{"text": "数量:1.00", "bbox": [270, 631, 396, 654]},
	{"text": "金额:0.01", "bbox": [454, 630, 576, 653]},
	{"text": "批号：20240825", "bbox": [270, 659, 467, 682]},
	{"text": "国码：Q01000000", "bbox": [270, 688, 480, 710]},
	{"text": "应收金额:477.8 优惠:11.8", "bbox": [270, 745, 606, 768]},
	{"text": "实收金额:466.01找零:0.00", "bbox": [272, 773, 605, 796]},
	{"text": "其中:收钱吧微信：", "bbox": [275, 802, 492, 825]},
	{"text": "466.01", "bbox": [535, 802, 616, 824]},
	{"text": "*药品除质量问题，概不退换", "bbox": [270, 858, 619, 880]},
	{"text": "*服务不满意，", "bbox": [270, 886, 470, 908]},
	{"text": "*地址-电话·", "bbox": [270, 914, 421, 936]}
]
```
2026-08-05 05:38:58,484 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=11.8s
2026-08-05 05:38:58,484 INFO     29 [qwen-vl-text] coord item[0]: text=[G532]  心草招县西人乡连锁, bbox=[270, 68, 654, 91]
2026-08-05 05:38:58,484 INFO     29 [qwen-vl-text] coord item[1]: text=店, bbox=[269, 100, 295, 117]
2026-08-05 05:38:58,484 INFO     29 [qwen-vl-text] coord item[2]: text=交易日期：2025-10-31 11:43:49, bbox=[270, 122, 669, 144]
2026-08-05 05:38:58,484 INFO     29 [qwen-vl-text] coord item[3]: text=销售单号：1325103100021472, bbox=[270, 150, 613, 172]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[4]: text=收银员：, bbox=[270, 178, 364, 200]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[5]: text=积分：543, bbox=[546, 206, 671, 228]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[6]: text=品名, bbox=[382, 234, 435, 256]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[7]: text=规格, bbox=[545, 234, 601, 256]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[8]: text=150027(兴)布地格福吸入, bbox=[315, 289, 657, 312]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[9]: text=气雾剂 倍择瑞_160ug:7.2u, bbox=[272, 318, 603, 341]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[10]: text=单价:233.00, bbox=[270, 346, 423, 368]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[11]: text=实价:233.00, bbox=[480, 345, 631, 368]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[12]: text=数量:2.00, bbox=[270, 374, 396, 397]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[13]: text=金额:466.00, bbox=[452, 373, 605, 396]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[14]: text=批号：6103904C00, bbox=[270, 402, 495, 425]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[15]: text=处方药, bbox=[521, 402, 605, 424]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[16]: text=国码：XRO3ALB240L028010179096, bbox=[270, 430, 676, 453]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[17]: text=AstraZeneca AB, bbox=[270, 460, 466, 482]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[18]: text=84471890087171843044, bbox=[270, 488, 550, 511]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[19]: text=84471890087171828685, bbox=[270, 516, 550, 539]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[20]: text=2、809245_一心堂卫生纸(原生, bbox=[270, 545, 649, 568]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[21]: text=木浆(纤维))_1000g(4层*1, bbox=[270, 573, 590, 596]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[22]: text=单价:11.80, bbox=[270, 602, 410, 625]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[23]: text=实价:0.01, bbox=[467, 602, 590, 625]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[24]: text=数量:1.00, bbox=[270, 631, 396, 654]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[25]: text=金额:0.01, bbox=[454, 630, 576, 653]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[26]: text=批号：20240825, bbox=[270, 659, 467, 682]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[27]: text=国码：Q01000000, bbox=[270, 688, 480, 710]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[28]: text=应收金额:477.8 优惠:11.8, bbox=[270, 745, 606, 768]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[29]: text=实收金额:466.01找零:0.00, bbox=[272, 773, 605, 796]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[30]: text=其中:收钱吧微信：, bbox=[275, 802, 492, 825]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[31]: text=466.01, bbox=[535, 802, 616, 824]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[32]: text=*药品除质量问题，概不退换, bbox=[270, 858, 619, 880]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[33]: text=*服务不满意，, bbox=[270, 886, 470, 908]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] coord item[34]: text=*地址-电话·, bbox=[270, 914, 421, 936]
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] page=5 — 35/35 coords, api_time=11.8s
2026-08-05 05:38:58,485 INFO     29 [qwen-vl-text] new_positions (35):
[[5, 160.65, 389.13, 57.256, 76.622], [5, 160.055, 175.525, 84.2, 98.514], [5, 160.65, 398.055, 102.72399999999999, 121.24799999999999], [5, 160.65, 364.73499999999996, 126.3, 144.82399999999998], [5, 160.65, 216.57999999999998, 149.876, 168.4], [5, 324.87, 399.245, 173.452, 191.976], [5, 227.29, 258.825, 197.028, 215.552], [5, 324.275, 357.59499999999997, 197.028, 215.552], [5, 187.42499999999998, 390.91499999999996, 243.338, 262.704], [5, 161.84, 358.78499999999997, 267.756, 287.122], [5, 160.65, 251.685, 291.332, 309.856], [5, 285.59999999999997, 375.445, 290.49, 309.856], [5, 160.65, 235.61999999999998, 314.908, 334.274], [5, 268.94, 359.97499999999997, 314.066, 333.432], [5, 160.65, 294.525, 338.484, 357.84999999999997], [5, 309.995, 359.97499999999997, 338.484, 357.008], [5, 160.65, 402.21999999999997, 362.06, 381.426], [5, 160.65, 277.27, 387.32, 405.844], [5, 160.65, 327.25, 410.89599999999996, 430.262], [5, 160.65, 327.25, 434.472, 453.83799999999997], [5, 160.65, 386.155, 458.89, 478.256], [5, 160.65, 351.05, 482.466, 501.832], [5, 160.65, 243.95, 506.88399999999996, 526.25], [5, 277.865, 351.05, 506.88399999999996, 526.25], [5, 160.65, 235.61999999999998, 531.302, 550.668], [5, 270.13, 342.71999999999997, 530.46, 549.826], [5, 160.65, 277.865, 554.8779999999999, 574.244], [5, 160.65, 285.59999999999997, 579.2959999999999, 597.8199999999999], [5, 160.65, 360.57, 627.29, 646.656], [5, 161.84, 359.97499999999997, 650.866, 670.232], [5, 163.625, 292.74, 675.284, 694.65], [5, 318.325, 366.52, 675.284, 693.808], [5, 160.65, 368.305, 722.4359999999999, 740.9599999999999], [5, 160.65, 279.65, 746.012, 764.536], [5, 160.65, 250.49499999999998, 769.588, 788.112]]
2026-08-05 05:38:58,486 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=14.7s
2026-08-05 05:38:58,486 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:38:58,486 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:38:58,486 INFO     29 [qwen-vl-text] positions(43): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:38:58,486 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [43]
2026-08-05 05:38:58,670 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:38:58,673 INFO     29 [qwen-vl-text] LLM extraction start, text_len=354
2026-08-05 05:38:58,673 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:38:58,673 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 178, \"bbox_end\": 220, \"encounter_dates\": [\"2025-09-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "山西省医疗门诊收费票据（电子）\n山西省\n财政部监制\n票据号码：0040081955\n校验码：itykbi\n开票日期：2025-09-01\n项目名称\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1\n233.00\nG布地格福吸入气雾剂【每瓶12\n1.00\n盒\n233.00 限慢性阻\n0揿】\n塞性肺疾\n病。\n金额合计（大写）贰佰叁拾叁元整\n(小写)233.00\n业务流水号：07QIKH59659470P20250 门诊号：\n就诊日期：20250901\n901172144801\n（医\n型：综合医院\n医保类型：国家医保\n医保码\n医保统\n支付：154.95\n其他支付：0.00\n个人账户支付：0.00\n个人现金支付：78.05\n付：0.0\nz-方便\n费专用章\n复核人：程小磊\n收款",
    "role": "user"
  }
]
[92m05:38:58 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:38:58,675 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:39:01,270 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:39:01,270 INFO     29 [qwen-vl-text] LLM output (len=407):
{
  "encounter_date": "2025-09-01",
  "pharmacy": null,
  "medications": [
    {
      "name": "布地格福吸入气雾剂",
      "specification": "每瓶120揿",
      "dosage": null,
      "quantity": 1,
      "unit_price": null,
      "total_price": 233.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 233.00,
  "payment_method": null
}
2026-08-05 05:39:01,270 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-01]
2026-08-05 05:39:01,273 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=723933, prompt_len=1096
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["山西省医疗门诊收费票据（电子）", "山西省", "财政部监制", "票据号码：0040081955", "校验码：itykbi", "开票日期：2025-09-01", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "233.00", "G布地格福吸入气雾剂【每瓶12", "1.00", "盒", "233.00 限慢性阻", "0揿】", "塞性肺疾", "病。", "金额合计（大写）贰佰叁拾叁元整", "(小写)233.00", "业务流水号：07QIKH59659470P20250 门诊号：", "就诊日期：20250901", "901172144801", "（医", "型：综合医院", "医保类型：国家医保", "医保码", "医保统", "支付：154.95", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：78.05", "付：0.0", "z-方便", "费专用章", "复核人：程小磊", "收款"]

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
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord API raw response (len=3579):
[
	{"text": "山西省医疗门诊收费票据（电子）", "bbox": [308, 68, 680, 104]},
	{"text": "山西省", "bbox": [477, 107, 522, 128], "bbox": [477, 107, 522, 128]},
	{"text": "财政部监制", "bbox": [463, 137, 536, 164], "bbox": [463, 137, 536, 164]},
	{"text": "票据号码：0040081955", "bbox": [631, 164, 764, 183], "bbox": [631, 164, 764, 183]},
	{"text": "校验码：itykbi", "bbox": [631, 190, 735, 209], "bbox": [631, 190, 735, 209]},
	{"text": "开票日期：2025-09-01", "bbox": [631, 216, 763, 234], "bbox": [631, 216, 763, 234]},
	{"text": "项目名称", "bbox": [157, 253, 210, 270], "bbox": [157, 253, 210, 270]},
	{"text": "数量/单位", "bbox": [293, 253, 353, 270], "bbox": [293, 253, 353, 270]},
	{"text": "金额（元）", "bbox": [382, 253, 438, 270], "bbox": [382, 253, 438, 270]},
	{"text": "备注", "bbox": [460, 253, 485, 270], "bbox": [460, 253, 485, 270]},
	{"text": "项目名称", "bbox": [560, 252, 612, 269], "bbox": [560, 252, 612, 269]},
	{"text": "数量/单位", "bbox": [696, 252, 758, 269], "bbox": [696, 252, 758, 269]},
	{"text": "金额（元）", "bbox": [792, 252, 852, 269], "bbox": [792, 252, 852, 269]},
	{"text": "备注", "bbox": [876, 252, 903, 269], "bbox": [876, 252, 903, 269]},
	{"text": "西药费", "bbox": [91, 289, 133, 307], "bbox": [91, 289, 133, 307]},
	{"text": "1", "bbox": [296, 290, 303, 306], "bbox": [296, 290, 303, 306]},
	{"text": "233.00", "bbox": [399, 289, 439, 306], "bbox": [399, 289, 439, 306]},
	{"text": "G布地格福吸入气雾剂【每瓶12", "bbox": [91, 316, 274, 335], "bbox": [91, 316, 274, 335]},
	{"text": "1.00", "bbox": [287, 317, 314, 334], "bbox": [287, 317, 314, 334]},
	{"text": "盒", "bbox": [337, 317, 351, 334], "bbox": [337, 317, 351, 334]},
	{"text": "233.00 限慢性阻", "bbox": [399, 316, 496, 334], "bbox": [399, 316, 496, 334]},
	{"text": "0揿】", "bbox": [91, 339, 119, 358], "bbox": [91, 339, 119, 358]},
	{"text": "塞性肺疾", "bbox": [444, 338, 496, 356], "bbox": [444, 338, 496, 356]},
	{"text": "病。", "bbox": [444, 360, 464, 378], "bbox": [444, 360, 464, 378]},
	{"text": "金额合计（大写）贰佰叁拾叁元整", "bbox": [96, 560, 297, 579], "bbox": [96, 560, 297, 579]},
	{"text": "(小写)233.00", "bbox": [559, 560, 639, 579], "bbox": [559, 560, 639, 579]},
	{"text": "业务流水号：07QIKH59659470P20250 门诊号：", "bbox": [124, 596, 399, 615], "bbox": [124, 596, 399, 615]},
	{"text": "就诊日期：20250901", "bbox": [733, 596, 850, 614], "bbox": [733, 596, 850, 614]},
	{"text": "901172144801", "bbox": [200, 619, 280, 637], "bbox": [200, 619, 280, 637]},
	{"text": "（医", "bbox": [119, 645, 145, 672], "bbox": [119, 645, 145, 672]},
	{"text": "型：综合医院", "bbox": [182, 643, 268, 661], "bbox": [182, 643, 268, 661]},
	{"text": "医保类型：国家医保", "bbox": [339, 641, 448, 660], "bbox": [339, 641, 448, 660]},
	{"text": "医保码", "bbox": [523, 645, 567, 662], "bbox": [523, 645, 567, 662]},
	{"text": "性别：女", "bbox": [733, 643, 783, 661], "bbox": [733, 643, 783, 661]},
	{"text": "医保统", "bbox": [124, 691, 178, 709], "bbox": [124, 691, 178, 709]},
	{"text": "支付：154.95", "bbox": [209, 690, 282, 708], "bbox": [209, 690, 282, 708]},
	{"text": "其他支付：0.00", "bbox": [339, 688, 422, 706], "bbox": [339, 688, 422, 706]},
	{"text": "个人账户支付：0.00", "bbox": [523, 689, 638, 708], "bbox": [523, 689, 638, 708]},
	{"text": "个人现金支付：78.05", "bbox": [734, 688, 858, 706], "bbox": [734, 688, 858, 706]},
	{"text": "付：0.0", "bbox": [154, 730, 216, 748], "bbox": [154, 730, 216, 748]},
	{"text": "z-方便", "bbox": [145, 752, 190, 772], "bbox": [145, 752, 190, 772]},
	{"text": "费专用章", "bbox": [105, 795, 185, 828], "bbox": [105, 795, 185, 828]},
	{"text": "复核人：程小磊", "bbox": [565, 809, 651, 827], "bbox": [565, 809, 651, 827]},
	{"text": "收款", "bbox": [738, 813, 768, 829], "bbox": [738, 813, 768, 829]}
]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=18.6s
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[0]: text=山西省医疗门诊收费票据（电子）, bbox=[308, 68, 680, 104]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[1]: text=山西省, bbox=[477, 107, 522, 128]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[2]: text=财政部监制, bbox=[463, 137, 536, 164]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[3]: text=票据号码：0040081955, bbox=[631, 164, 764, 183]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[4]: text=校验码：itykbi, bbox=[631, 190, 735, 209]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[5]: text=开票日期：2025-09-01, bbox=[631, 216, 763, 234]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[6]: text=项目名称, bbox=[157, 253, 210, 270]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[7]: text=数量/单位, bbox=[293, 253, 353, 270]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[8]: text=金额（元）, bbox=[382, 253, 438, 270]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[9]: text=备注, bbox=[460, 253, 485, 270]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[10]: text=项目名称, bbox=[560, 252, 612, 269]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[11]: text=数量/单位, bbox=[696, 252, 758, 269]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[12]: text=金额（元）, bbox=[792, 252, 852, 269]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[13]: text=备注, bbox=[876, 252, 903, 269]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[14]: text=西药费, bbox=[91, 289, 133, 307]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[15]: text=1, bbox=[296, 290, 303, 306]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[16]: text=233.00, bbox=[399, 289, 439, 306]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[17]: text=G布地格福吸入气雾剂【每瓶12, bbox=[91, 316, 274, 335]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[18]: text=1.00, bbox=[287, 317, 314, 334]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[19]: text=盒, bbox=[337, 317, 351, 334]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[20]: text=233.00 限慢性阻, bbox=[399, 316, 496, 334]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[21]: text=0揿】, bbox=[91, 339, 119, 358]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[22]: text=塞性肺疾, bbox=[444, 338, 496, 356]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[23]: text=病。, bbox=[444, 360, 464, 378]
2026-08-05 05:39:19,860 INFO     29 [qwen-vl-text] coord item[24]: text=金额合计（大写）贰佰叁拾叁元整, bbox=[96, 560, 297, 579]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[25]: text=(小写)233.00, bbox=[559, 560, 639, 579]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[26]: text=业务流水号：07QIKH59659470P20250 门诊号：, bbox=[124, 596, 399, 615]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[27]: text=就诊日期：20250901, bbox=[733, 596, 850, 614]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[28]: text=901172144801, bbox=[200, 619, 280, 637]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[29]: text=（医, bbox=[119, 645, 145, 672]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[30]: text=型：综合医院, bbox=[182, 643, 268, 661]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[31]: text=医保类型：国家医保, bbox=[339, 641, 448, 660]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[32]: text=医保码, bbox=[523, 645, 567, 662]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[33]: text=性别：女, bbox=[733, 643, 783, 661]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[34]: text=医保统, bbox=[124, 691, 178, 709]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[35]: text=支付：154.95, bbox=[209, 690, 282, 708]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[36]: text=其他支付：0.00, bbox=[339, 688, 422, 706]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[37]: text=个人账户支付：0.00, bbox=[523, 689, 638, 708]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[38]: text=个人现金支付：78.05, bbox=[734, 688, 858, 706]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[39]: text=付：0.0, bbox=[154, 730, 216, 748]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[40]: text=z-方便, bbox=[145, 752, 190, 772]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[41]: text=费专用章, bbox=[105, 795, 185, 828]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[42]: text=复核人：程小磊, bbox=[565, 809, 651, 827]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] coord item[43]: text=收款, bbox=[738, 813, 768, 829]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] page=6 — 43/43 coords, api_time=18.6s
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] new_positions (43):
[[6, 259.336, 572.56, 40.46, 61.879999999999995], [6, 401.63399999999996, 439.524, 63.665, 76.16], [6, 389.846, 451.312, 81.515, 97.58], [6, 531.302, 643.288, 97.58, 108.88499999999999], [6, 531.302, 618.87, 113.05, 124.35499999999999], [6, 531.302, 642.446, 128.51999999999998, 139.23], [6, 132.194, 176.82, 150.535, 160.65], [6, 246.706, 297.226, 150.535, 160.65], [6, 321.644, 368.796, 150.535, 160.65], [6, 387.32, 408.37, 150.535, 160.65], [6, 471.52, 515.304, 149.94, 160.055], [6, 586.0319999999999, 638.236, 149.94, 160.055], [6, 666.864, 717.384, 149.94, 160.055], [6, 737.592, 760.326, 149.94, 160.055], [6, 76.622, 111.98599999999999, 171.95499999999998, 182.665], [6, 249.232, 255.126, 172.54999999999998, 182.07], [6, 335.95799999999997, 369.638, 171.95499999999998, 182.07], [6, 76.622, 230.708, 188.01999999999998, 199.325], [6, 241.654, 264.388, 188.61499999999998, 198.73], [6, 283.75399999999996, 295.542, 188.61499999999998, 198.73], [6, 335.95799999999997, 417.632, 188.01999999999998, 198.73], [6, 76.622, 100.198, 201.70499999999998, 213.01], [6, 373.848, 417.632, 201.10999999999999, 211.82], [6, 373.848, 390.688, 214.2, 224.91], [6, 80.832, 250.07399999999998, 333.2, 344.505], [6, 470.678, 538.038, 333.2, 344.505], [6, 104.408, 335.95799999999997, 354.62, 365.925], [6, 617.1859999999999, 715.6999999999999, 354.62, 365.33], [6, 168.4, 235.76, 368.305, 379.015], [6, 100.198, 122.08999999999999, 383.775, 399.84], [6, 153.244, 225.656, 382.585, 393.29499999999996], [6, 285.438, 377.216, 381.395, 392.7], [6, 440.366, 477.414, 383.775, 393.89], [6, 617.1859999999999, 659.286, 382.585, 393.29499999999996], [6, 104.408, 149.876, 411.145, 421.85499999999996], [6, 175.97799999999998, 237.444, 410.54999999999995, 421.26], [6, 285.438, 355.324, 409.35999999999996, 420.07], [6, 440.366, 537.196, 409.955, 421.26], [6, 618.028, 722.4359999999999, 409.35999999999996, 420.07], [6, 129.668, 181.87199999999999, 434.34999999999997, 445.06], [6, 122.08999999999999, 159.98, 447.44, 459.34], [6, 88.41, 155.76999999999998, 473.025, 492.65999999999997], [6, 475.72999999999996, 548.1419999999999, 481.35499999999996, 492.065]]
2026-08-05 05:39:19,861 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=21.4s
2026-08-05 05:39:19,861 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:39:19,862 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:39:19,862 INFO     29 [qwen-vl-text] positions(49): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:39:19,862 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [49]
2026-08-05 05:39:20,025 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:39:20,026 INFO     29 [qwen-vl-text] LLM extraction start, text_len=395
2026-08-05 05:39:20,026 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:39:20,027 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 223, \"bbox_end\": 271, \"encounter_dates\": [\"2025-07-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "山西省医疗门诊收费票据（电子）\n山西省\n财政部监制\n票据代码：\n交款人话一社会信用代码：\n交款人\n票据号码：0039960248\n校验码：isI3ej\n开票日期：2025-07-08\n项目名称\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1\n466.00\nG布地格福吸入气雾剂【每瓶12\n2.00\n盒\n466.00 限慢性阻\n0揿】\n塞性肺疾\n病。\n金额合计（大写）肆佰陆拾陆元整\n(小写)466.00\n业务流水号：B7C8A658327630P20250 门诊号：\n就诊日期：20250708\n708113600815\n类型：综合医院\n医保类型：国家医保\n医保编\n医保.\n付：309.89\n其他支付：0.00\n个人账户支付：0.00\n个人现金支付：156.11\n信\n自付：\n息\nZ-方便\n靖号\n个人自费：156.11\n费专用\n复核人：程小蕊\n收款人：王丽",
    "role": "user"
  }
]
[92m05:39:20 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:39:20,028 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:39:20,029 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:39:20.027+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"a0ac621a908f11f1a3da71efcdd7cc1f": {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:39:22,454 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:39:22,454 INFO     29 [qwen-vl-text] LLM output (len=407):
{
  "encounter_date": "2025-07-08",
  "pharmacy": null,
  "medications": [
    {
      "name": "布地格福吸入气雾剂",
      "specification": "每瓶120揿",
      "dosage": null,
      "quantity": 2,
      "unit_price": null,
      "total_price": 466.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 466.00,
  "payment_method": null
}
2026-08-05 05:39:22,454 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-08]
2026-08-05 05:39:22,455 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=718847, prompt_len=1155
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共49行）
["山西省医疗门诊收费票据（电子）", "山西省", "财政部监制", "票据代码：", "交款人话一社会信用代码：", "交款人", "票据号码：0039960248", "校验码：isI3ej", "开票日期：2025-07-08", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "466.00", "G布地格福吸入气雾剂【每瓶12", "2.00", "盒", "466.00 限慢性阻", "0揿】", "塞性肺疾", "病。", "金额合计（大写）肆佰陆拾陆元整", "(小写)466.00", "业务流水号：B7C8A658327630P20250 门诊号：", "就诊日期：20250708", "708113600815", "类型：综合医院", "医保类型：国家医保", "医保编", "医保.", "付：309.89", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：156.11", "信", "自付：", "息", "Z-方便", "靖号", "个人自费：156.11", "费专用", "复核人：程小蕊", "收款人：王丽"]

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
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord API raw response (len=3596):
[
	{"text": "山西省医疗门诊收费票据（电子）", "bbox": [306, 68, 682, 114], "label": "山西省医疗门诊收费票据（电子）"},
	{"text": "山西省", "bbox": [474, 112, 521, 135], "label": "山西省"},
	{"text": "财政部监制", "bbox": [460, 143, 534, 174], "label": "财政部监制"},
	{"text": "票据代码：", "bbox": [95, 178, 158, 196], "label": "票据代码："},
	{"text": "交款人话一社会信用代码：", "bbox": [95, 202, 243, 220], "label": "交款人话一社会信用代码："},
	{"text": "交款人", "bbox": [95, 228, 134, 245], "label": "交款人"},
	{"text": "票据号码：0039960248", "bbox": [631, 167, 767, 189], "label": "票据号码：0039960248"},
	{"text": "校验码：isI3ej", "bbox": [631, 195, 738, 216], "label": "校验码：isI3ej"},
	{"text": "开票日期：2025-07-08", "bbox": [631, 222, 767, 242], "label": "开票日期：2025-07-08"},
	{"text": "项目名称", "bbox": [160, 262, 212, 279], "label": "项目名称"},
	{"text": "数量/单位", "bbox": [293, 262, 353, 279], "label": "数量/单位"},
	{"text": "金额（元）", "bbox": [382, 262, 438, 279], "label": "金额（元）"},
	{"text": "备注", "bbox": [460, 262, 485, 279], "label": "备注"},
	{"text": "项目名称", "bbox": [558, 260, 612, 277], "label": "项目名称"},
	{"text": "数量/单位", "bbox": [698, 259, 760, 277], "label": "数量/单位"},
	{"text": "金额（元）", "bbox": [790, 258, 854, 277], "label": "金额（元）"},
	{"text": "备注", "bbox": [868, 258, 894, 277], "label": "备注"},
	{"text": "西药费", "bbox": [96, 297, 136, 315], "label": "西药费"},
	{"text": "1", "bbox": [296, 298, 303, 314], "label": "1"},
	{"text": "466.00", "bbox": [400, 297, 439, 314], "label": "466.00"},
	{"text": "G布地格福吸入气雾剂【每瓶12", "bbox": [96, 325, 274, 344], "label": "G布地格福吸入气雾剂【每瓶12"},
	{"text": "2.00", "bbox": [286, 326, 314, 343], "label": "2.00"},
	{"text": "盒", "bbox": [337, 326, 352, 344], "label": "盒"},
	{"text": "466.00 限慢性阻", "bbox": [400, 326, 496, 344], "label": "466.00 限慢性阻"},
	{"text": "0揿】", "bbox": [96, 348, 124, 366], "label": "0揿】"},
	{"text": "塞性肺疾", "bbox": [444, 348, 496, 367], "label": "塞性肺疾"},
	{"text": "病。", "bbox": [444, 370, 464, 388], "label": "病。"},
	{"text": "金额合计（大写）肆佰陆拾陆元整", "bbox": [102, 571, 298, 590], "label": "金额合计（大写）肆佰陆拾陆元整"},
	{"text": "(小写)466.00", "bbox": [559, 570, 639, 589], "label": "(小写)466.00"},
	{"text": "业务流水号：B7C8A658327630P20250 门诊号：", "bbox": [127, 607, 385, 624], "label": "业务流水号：B7C8A658327630P20250 门诊号："},
	{"text": "就诊日期：20250708", "bbox": [736, 606, 845, 623], "label": "就诊日期：20250708"},
	{"text": "708113600815", "bbox": [199, 628, 281, 645], "label": "708113600815"},
	{"text": "类型：综合医院", "bbox": [181, 651, 267, 669], "label": "类型：综合医院"},
	{"text": "医保类型：国家医保", "bbox": [341, 649, 451, 667], "label": "医保类型：国家医保"},
	{"text": "医保编", "bbox": [524, 653, 562, 670], "label": "医保编"},
	{"text": "性别：女", "bbox": [724, 650, 784, 668], "label": "性别：女"},
	{"text": "医保.", "bbox": [127, 695, 157, 712], "label": "医保."},
	{"text": "付：309.89", "bbox": [218, 695, 282, 712], "label": "付：309.89"},
	{"text": "其他支付：0.00", "bbox": [341, 693, 425, 711], "label": "其他支付：0.00"},
	{"text": "个人账户支付：0.00", "bbox": [524, 695, 640, 712], "label": "个人账户支付：0.00"},
	{"text": "个人现金支付：156.11", "bbox": [738, 692, 858, 709], "label": "个人现金支付：156.11"},
	{"text": "信", "bbox": [105, 717, 116, 734], "label": "信"},
	{"text": "自付：", "bbox": [154, 734, 184, 752], "label": "自付："},
	{"text": "息", "bbox": [107, 752, 117, 769], "label": "息"},
	{"text": "Z-方便", "bbox": [145, 754, 190, 773], "label": "Z-方便"},
	{"text": "靖号", "bbox": [242, 756, 277, 774], "label": "靖号"},
	{"text": "个人自费：156.11", "bbox": [341, 731, 439, 749], "label": "个人自费：156.11"},
	{"text": "费专用", "bbox": [93, 794, 168, 828], "label": "费专用"},
	{"text": "复核人：程小蕊", "bbox": [572, 809, 656, 827], "label": "复核人：程小蕊"},
	{"text": "收款人：王丽", "bbox": [741, 809, 818, 827], "label": "收款人：王丽"}
]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord API: raw_items=50, valid_items=50, elapsed=21.1s
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[0]: text=山西省医疗门诊收费票据（电子）, bbox=[306, 68, 682, 114]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[1]: text=山西省, bbox=[474, 112, 521, 135]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[2]: text=财政部监制, bbox=[460, 143, 534, 174]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[3]: text=票据代码：, bbox=[95, 178, 158, 196]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[4]: text=交款人话一社会信用代码：, bbox=[95, 202, 243, 220]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[5]: text=交款人, bbox=[95, 228, 134, 245]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[6]: text=票据号码：0039960248, bbox=[631, 167, 767, 189]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[7]: text=校验码：isI3ej, bbox=[631, 195, 738, 216]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[8]: text=开票日期：2025-07-08, bbox=[631, 222, 767, 242]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[9]: text=项目名称, bbox=[160, 262, 212, 279]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[10]: text=数量/单位, bbox=[293, 262, 353, 279]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[11]: text=金额（元）, bbox=[382, 262, 438, 279]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[12]: text=备注, bbox=[460, 262, 485, 279]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[13]: text=项目名称, bbox=[558, 260, 612, 277]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[14]: text=数量/单位, bbox=[698, 259, 760, 277]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[15]: text=金额（元）, bbox=[790, 258, 854, 277]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[16]: text=备注, bbox=[868, 258, 894, 277]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[17]: text=西药费, bbox=[96, 297, 136, 315]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[18]: text=1, bbox=[296, 298, 303, 314]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[19]: text=466.00, bbox=[400, 297, 439, 314]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[20]: text=G布地格福吸入气雾剂【每瓶12, bbox=[96, 325, 274, 344]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[21]: text=2.00, bbox=[286, 326, 314, 343]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[22]: text=盒, bbox=[337, 326, 352, 344]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[23]: text=466.00 限慢性阻, bbox=[400, 326, 496, 344]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[24]: text=0揿】, bbox=[96, 348, 124, 366]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[25]: text=塞性肺疾, bbox=[444, 348, 496, 367]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[26]: text=病。, bbox=[444, 370, 464, 388]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[27]: text=金额合计（大写）肆佰陆拾陆元整, bbox=[102, 571, 298, 590]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[28]: text=(小写)466.00, bbox=[559, 570, 639, 589]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[29]: text=业务流水号：B7C8A658327630P20250 门诊号：, bbox=[127, 607, 385, 624]
2026-08-05 05:39:43,589 INFO     29 [qwen-vl-text] coord item[30]: text=就诊日期：20250708, bbox=[736, 606, 845, 623]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[31]: text=708113600815, bbox=[199, 628, 281, 645]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[32]: text=类型：综合医院, bbox=[181, 651, 267, 669]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[33]: text=医保类型：国家医保, bbox=[341, 649, 451, 667]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[34]: text=医保编, bbox=[524, 653, 562, 670]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[35]: text=性别：女, bbox=[724, 650, 784, 668]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[36]: text=医保., bbox=[127, 695, 157, 712]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[37]: text=付：309.89, bbox=[218, 695, 282, 712]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[38]: text=其他支付：0.00, bbox=[341, 693, 425, 711]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[39]: text=个人账户支付：0.00, bbox=[524, 695, 640, 712]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[40]: text=个人现金支付：156.11, bbox=[738, 692, 858, 709]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[41]: text=信, bbox=[105, 717, 116, 734]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[42]: text=自付：, bbox=[154, 734, 184, 752]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[43]: text=息, bbox=[107, 752, 117, 769]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[44]: text=Z-方便, bbox=[145, 754, 190, 773]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[45]: text=靖号, bbox=[242, 756, 277, 774]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[46]: text=个人自费：156.11, bbox=[341, 731, 439, 749]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[47]: text=费专用, bbox=[93, 794, 168, 828]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[48]: text=复核人：程小蕊, bbox=[572, 809, 656, 827]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] coord item[49]: text=收款人：王丽, bbox=[741, 809, 818, 827]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] page=7 — 49/49 coords, api_time=21.1s
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] new_positions (49):
[[7, 257.652, 574.244, 40.46, 67.83], [7, 399.108, 438.68199999999996, 66.64, 80.325], [7, 387.32, 449.628, 85.085, 103.53], [7, 79.99, 133.036, 105.91, 116.61999999999999], [7, 79.99, 204.606, 120.19, 130.9], [7, 79.99, 112.828, 135.66, 145.775], [7, 531.302, 645.814, 99.365, 112.455], [7, 531.302, 621.396, 116.02499999999999, 128.51999999999998], [7, 531.302, 645.814, 132.09, 143.98999999999998], [7, 134.72, 178.504, 155.89, 166.005], [7, 246.706, 297.226, 155.89, 166.005], [7, 321.644, 368.796, 155.89, 166.005], [7, 387.32, 408.37, 155.89, 166.005], [7, 469.83599999999996, 515.304, 154.7, 164.815], [7, 587.716, 639.92, 154.105, 164.815], [7, 665.18, 719.068, 153.51, 164.815], [7, 730.856, 752.7479999999999, 153.51, 164.815], [7, 80.832, 114.512, 176.715, 187.42499999999998], [7, 249.232, 255.126, 177.31, 186.82999999999998], [7, 336.8, 369.638, 176.715, 186.82999999999998], [7, 80.832, 230.708, 193.375, 204.67999999999998], [7, 240.81199999999998, 264.388, 193.97, 204.08499999999998], [7, 283.75399999999996, 296.384, 193.97, 204.67999999999998], [7, 336.8, 417.632, 193.97, 204.67999999999998], [7, 80.832, 104.408, 207.06, 217.76999999999998], [7, 373.848, 417.632, 207.06, 218.36499999999998], [7, 373.848, 390.688, 220.14999999999998, 230.85999999999999], [7, 85.884, 250.916, 339.745, 351.05], [7, 470.678, 538.038, 339.15, 350.455], [7, 106.934, 324.17, 361.16499999999996, 371.28], [7, 619.712, 711.49, 360.57, 370.685], [7, 167.558, 236.602, 373.65999999999997, 383.775], [7, 152.402, 224.814, 387.34499999999997, 398.055], [7, 287.122, 379.74199999999996, 386.155, 396.865], [7, 441.20799999999997, 473.204, 388.53499999999997, 398.65], [7, 609.608, 660.1279999999999, 386.75, 397.46], [7, 106.934, 132.194, 413.525, 423.64], [7, 183.55599999999998, 237.444, 413.525, 423.64], [7, 287.122, 357.84999999999997, 412.335, 423.04499999999996], [7, 441.20799999999997, 538.88, 413.525, 423.64], [7, 621.396, 722.4359999999999, 411.74, 421.85499999999996], [7, 88.41, 97.672, 426.615, 436.72999999999996], [7, 129.668, 154.928, 436.72999999999996, 447.44], [7, 90.094, 98.514, 447.44, 457.555], [7, 122.08999999999999, 159.98, 448.63, 459.935], [7, 203.76399999999998, 233.23399999999998, 449.82, 460.53], [7, 287.122, 369.638, 434.945, 445.655], [7, 78.306, 141.456, 472.43, 492.65999999999997], [7, 481.62399999999997, 552.352, 481.35499999999996, 492.065]]
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] ═══ DONE ═══ 49 positions, pages=1, time=23.7s
2026-08-05 05:39:43,590 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:39:43,590 INFO     29 [qwen-vl-text] positions(51): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:39:43,591 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [51]
2026-08-05 05:39:43,771 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:39:43,772 INFO     29 [qwen-vl-text] LLM extraction start, text_len=383
2026-08-05 05:39:43,772 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:39:43,772 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 274, \"bbox_end\": 324, \"encounter_dates\": [\"2026-02-24\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "山西省医疗门诊收费票据（电子）\n山西省\n财政部监制\n票据代码:1/\n交款人统一社会信用代码:\n交款\n票据号码:0155140741\n校验码: ci4u59\n开票日期:2026-02-24\n项目名称\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1.00\n233.00\nG布地格福吸入气雾剂【每瓶12\n1.00\n盒\n233.00 限慢性阻\n0揿】\n塞性肺疾\n病。\n金额合计（大写）贰佰叁拾叁元整\n(小写)233.00\n业务流水号:2\n门诊号:\n就诊日期:20260224\n2\n类型:综合医院\n医保类型:国家医保\n医保编号\n0548 性别:女\n医保现\n付:154.95\n其他支付:0.00\n个人账户支付:0.00\n个人现金支付:78.05\n信\n自付:\n总\nZ-方便\n赵泽斌号\n个人自费:78.05\n费专用章\n复核人:程小蕊\n收款人:刘灵芝",
    "role": "user"
  }
]
[92m05:39:43 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:39:43,773 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:39:46,173 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:39:46,173 INFO     29 [qwen-vl-text] LLM output (len=407):
{
  "encounter_date": "2026-02-24",
  "pharmacy": null,
  "medications": [
    {
      "name": "布地格福吸入气雾剂",
      "specification": "每瓶120揿",
      "dosage": null,
      "quantity": 1,
      "unit_price": null,
      "total_price": 233.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 233.00,
  "payment_method": null
}
2026-08-05 05:39:46,173 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-24]
2026-08-05 05:39:46,176 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1068916, prompt_len=1149
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共51行）
["山西省医疗门诊收费票据（电子）", "山西省", "财政部监制", "票据代码:1/", "交款人统一社会信用代码:", "交款", "票据号码:0155140741", "校验码: ci4u59", "开票日期:2026-02-24", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1.00", "233.00", "G布地格福吸入气雾剂【每瓶12", "1.00", "盒", "233.00 限慢性阻", "0揿】", "塞性肺疾", "病。", "金额合计（大写）贰佰叁拾叁元整", "(小写)233.00", "业务流水号:2", "门诊号:", "就诊日期:20260224", "2", "类型:综合医院", "医保类型:国家医保", "医保编号", "0548 性别:女", "医保现", "付:154.95", "其他支付:0.00", "个人账户支付:0.00", "个人现金支付:78.05", "信", "自付:", "总", "Z-方便", "赵泽斌号", "个人自费:78.05", "费专用章", "复核人:程小蕊", "收款人:刘灵芝"]

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
2026-08-05 05:40:09,862 INFO     29 [qwen-vl-text] coord API raw response (len=4100):
[
	{"text": "山西省医疗门诊收费票据（电子）", "bbox": [296, 44, 693, 80]},
	{"text": "山西省", "bbox": [477, 82, 529, 104], "bbox": [477, 82, 529, 104]},
	{"text": "财政部监制", "bbox": [462, 115, 544, 142], "bbox": [462, 115, 544, 142]},
	{"text": "票据代码:1/", "bbox": [73, 146, 146, 165], "bbox": [73, 146, 146, 165]},
	{"text": "交款人统一社会信用代码:", "bbox": [73, 172, 234, 191], "bbox": [73, 172, 234, 191]},
	{"text": "交款", "bbox": [73, 200, 98, 218], "bbox": [73, 200, 98, 218]},
	{"text": "票据号码:0155140741", "bbox": [645, 145, 775, 164], "bbox": [645, 145, 775, 164]},
	{"text": "校验码: ci4u59", "bbox": [645, 173, 748, 192], "bbox": [645, 173, 748, 192]},
	{"text": "开票日期:2026-02-24", "bbox": [645, 200, 776, 218], "bbox": [645, 200, 776, 218]},
	{"text": "项目名称", "bbox": [141, 238, 195, 255], "bbox": [141, 238, 195, 255]},
	{"text": "数量/单位", "bbox": [281, 238, 344, 255], "bbox": [281, 238, 344, 255]},
	{"text": "金额（元）", "bbox": [375, 238, 436, 256], "bbox": [375, 238, 436, 256]},
	{"text": "备注", "bbox": [460, 238, 486, 255], "bbox": [460, 238, 486, 255]},
	{"text": "项目名称", "bbox": [571, 238, 624, 255], "bbox": [571, 238, 624, 255]},
	{"text": "数量/单位", "bbox": [709, 238, 770, 255], "bbox": [709, 238, 770, 255]},
	{"text": "金额（元）", "bbox": [803, 238, 863, 256], "bbox": [803, 238, 863, 256]},
	{"text": "备注", "bbox": [886, 238, 911, 255], "bbox": [886, 238, 911, 255]},
	{"text": "西药费", "bbox": [75, 274, 116, 293], "bbox": [75, 274, 116, 293]},
	{"text": "1.00", "bbox": [274, 276, 302, 293], "bbox": [274, 276, 302, 293]},
	{"text": "233.00", "bbox": [393, 276, 436, 293], "bbox": [393, 276, 436, 293]},
	{"text": "G布地格福吸入气雾剂【每瓶12", "bbox": [75, 305, 261, 325], "bbox": [75, 305, 261, 325]},
	{"text": "1.00", "bbox": [274, 307, 302, 324], "bbox": [274, 307, 302, 324]},
	{"text": "盒", "bbox": [327, 307, 342, 325], "bbox": [327, 307, 342, 325]},
	{"text": "233.00 限慢性阻", "bbox": [393, 307, 497, 325], "bbox": [393, 307, 497, 325]},
	{"text": "0揿】", "bbox": [75, 329, 104, 348], "bbox": [75, 329, 104, 348]},
	{"text": "塞性肺疾", "bbox": [442, 329, 498, 348], "bbox": [442, 329, 498, 348]},
	{"text": "病。", "bbox": [442, 353, 464, 371], "bbox": [442, 353, 464, 371]},
	{"text": "金额合计（大写）贰佰叁拾叁元整", "bbox": [78, 563, 280, 582], "bbox": [78, 563, 280, 582]},
	{"text": "(小写)233.00", "bbox": [559, 564, 643, 582], "bbox": [559, 564, 643, 582]},
	{"text": "业务流水号:2", "bbox": [105, 603, 191, 621], "bbox": [105, 603, 191, 621]},
	{"text": "门诊号:", "bbox": [323, 603, 370, 621], "bbox": [323, 603, 370, 621]},
	{"text": "就诊日期:20260224", "bbox": [739, 603, 857, 621], "bbox": [739, 603, 857, 621]},
	{"text": "2", "bbox": [178, 627, 193, 644], "bbox": [178, 627, 193, 644]},
	{"text": "类型:综合医院", "bbox": [162, 651, 250, 670], "bbox": [162, 651, 250, 670]},
	{"text": "医保类型:国家医保", "bbox": [323, 651, 440, 670], "bbox": [323, 651, 440, 670]},
	{"text": "医保编号", "bbox": [519, 653, 572, 670], "bbox": [519, 653, 572, 670]},
	{"text": "0548 性别:女", "bbox": [700, 651, 788, 670], "bbox": [700, 651, 788, 670]},
	{"text": "医保现", "bbox": [105, 701, 149, 718], "bbox": [105, 701, 149, 718]},
	{"text": "付:154.95", "bbox": [193, 699, 264, 717], "bbox": [193, 699, 264, 717]},
	{"text": "其他支付:0.00", "bbox": [323, 699, 413, 717], "bbox": [323, 699, 413, 717]},
	{"text": "个人账户支付:0.00", "bbox": [519, 699, 638, 717], "bbox": [519, 699, 638, 717]},
	{"text": "个人现金支付:78.05", "bbox": [739, 699, 864, 717], "bbox": [739, 699, 864, 717]},
	{"text": "信", "bbox": [84, 723, 95, 740], "bbox": [84, 723, 95, 740]},
	{"text": "自付:", "bbox": [133, 743, 169, 761], "bbox": [133, 743, 169, 761]},
	{"text": "总", "bbox": [86, 762, 97, 780], "bbox": [86, 762, 97, 780]},
	{"text": "Z-方便", "bbox": [125, 767, 166, 785], "bbox": [125, 767, 166, 785]},
	{"text": "赵泽斌号", "bbox": [203, 767, 265, 785], "bbox": [203, 767, 265, 785]},
	{"text": "个人自费:78.05", "bbox": [323, 740, 420, 758], "bbox": [323, 740, 420, 758]},
	{"text": "费专用章", "bbox": [81, 809, 164, 845], "bbox": [81, 809, 164, 845]},
	{"text": "复核人:程小蕊", "bbox": [562, 827, 651, 847], "bbox": [562, 827, 651, 847]},
	{"text": "收款人:刘灵芝", "bbox": [741, 829, 833, 848], "bbox": [741, 829, 833, 848]}
]
2026-08-05 05:40:09,866 INFO     29 [qwen-vl-text] coord API: raw_items=51, valid_items=51, elapsed=23.7s
2026-08-05 05:40:09,866 INFO     29 [qwen-vl-text] coord item[0]: text=山西省医疗门诊收费票据（电子）, bbox=[296, 44, 693, 80]
2026-08-05 05:40:09,866 INFO     29 [qwen-vl-text] coord item[1]: text=山西省, bbox=[477, 82, 529, 104]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[2]: text=财政部监制, bbox=[462, 115, 544, 142]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[3]: text=票据代码:1/, bbox=[73, 146, 146, 165]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[4]: text=交款人统一社会信用代码:, bbox=[73, 172, 234, 191]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[5]: text=交款, bbox=[73, 200, 98, 218]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[6]: text=票据号码:0155140741, bbox=[645, 145, 775, 164]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[7]: text=校验码: ci4u59, bbox=[645, 173, 748, 192]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[8]: text=开票日期:2026-02-24, bbox=[645, 200, 776, 218]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[9]: text=项目名称, bbox=[141, 238, 195, 255]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[10]: text=数量/单位, bbox=[281, 238, 344, 255]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[11]: text=金额（元）, bbox=[375, 238, 436, 256]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[12]: text=备注, bbox=[460, 238, 486, 255]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[13]: text=项目名称, bbox=[571, 238, 624, 255]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[14]: text=数量/单位, bbox=[709, 238, 770, 255]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[15]: text=金额（元）, bbox=[803, 238, 863, 256]
2026-08-05 05:40:09,867 INFO     29 [qwen-vl-text] coord item[16]: text=备注, bbox=[886, 238, 911, 255]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[17]: text=西药费, bbox=[75, 274, 116, 293]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[18]: text=1.00, bbox=[274, 276, 302, 293]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[19]: text=233.00, bbox=[393, 276, 436, 293]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[20]: text=G布地格福吸入气雾剂【每瓶12, bbox=[75, 305, 261, 325]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[21]: text=1.00, bbox=[274, 307, 302, 324]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[22]: text=盒, bbox=[327, 307, 342, 325]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[23]: text=233.00 限慢性阻, bbox=[393, 307, 497, 325]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[24]: text=0揿】, bbox=[75, 329, 104, 348]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[25]: text=塞性肺疾, bbox=[442, 329, 498, 348]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[26]: text=病。, bbox=[442, 353, 464, 371]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[27]: text=金额合计（大写）贰佰叁拾叁元整, bbox=[78, 563, 280, 582]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[28]: text=(小写)233.00, bbox=[559, 564, 643, 582]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[29]: text=业务流水号:2, bbox=[105, 603, 191, 621]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[30]: text=门诊号:, bbox=[323, 603, 370, 621]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[31]: text=就诊日期:20260224, bbox=[739, 603, 857, 621]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[32]: text=2, bbox=[178, 627, 193, 644]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[33]: text=类型:综合医院, bbox=[162, 651, 250, 670]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[34]: text=医保类型:国家医保, bbox=[323, 651, 440, 670]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[35]: text=医保编号, bbox=[519, 653, 572, 670]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[36]: text=0548 性别:女, bbox=[700, 651, 788, 670]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[37]: text=医保现, bbox=[105, 701, 149, 718]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[38]: text=付:154.95, bbox=[193, 699, 264, 717]
2026-08-05 05:40:09,868 INFO     29 [qwen-vl-text] coord item[39]: text=其他支付:0.00, bbox=[323, 699, 413, 717]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[40]: text=个人账户支付:0.00, bbox=[519, 699, 638, 717]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[41]: text=个人现金支付:78.05, bbox=[739, 699, 864, 717]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[42]: text=信, bbox=[84, 723, 95, 740]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[43]: text=自付:, bbox=[133, 743, 169, 761]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[44]: text=总, bbox=[86, 762, 97, 780]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[45]: text=Z-方便, bbox=[125, 767, 166, 785]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[46]: text=赵泽斌号, bbox=[203, 767, 265, 785]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[47]: text=个人自费:78.05, bbox=[323, 740, 420, 758]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[48]: text=费专用章, bbox=[81, 809, 164, 845]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[49]: text=复核人:程小蕊, bbox=[562, 827, 651, 847]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] coord item[50]: text=收款人:刘灵芝, bbox=[741, 829, 833, 848]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] page=8 — 51/51 coords, api_time=23.7s
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] new_positions (51):
[[8, 249.232, 583.506, 26.18, 47.599999999999994], [8, 401.63399999999996, 445.418, 48.79, 61.879999999999995], [8, 389.00399999999996, 458.048, 68.425, 84.49], [8, 61.466, 122.932, 86.86999999999999, 98.175], [8, 61.466, 197.028, 102.33999999999999, 113.645], [8, 61.466, 82.51599999999999, 119.0, 129.71], [8, 543.09, 652.55, 86.27499999999999, 97.58], [8, 543.09, 629.816, 102.935, 114.24], [8, 543.09, 653.3919999999999, 119.0, 129.71], [8, 118.722, 164.19, 141.60999999999999, 151.725], [8, 236.602, 289.64799999999997, 141.60999999999999, 151.725], [8, 315.75, 367.11199999999997, 141.60999999999999, 152.32], [8, 387.32, 409.212, 141.60999999999999, 151.725], [8, 480.782, 525.408, 141.60999999999999, 151.725], [8, 596.978, 648.34, 141.60999999999999, 151.725], [8, 676.126, 726.646, 141.60999999999999, 152.32], [8, 746.012, 767.062, 141.60999999999999, 151.725], [8, 63.15, 97.672, 163.03, 174.33499999999998], [8, 230.708, 254.284, 164.22, 174.33499999999998], [8, 330.906, 367.11199999999997, 164.22, 174.33499999999998], [8, 63.15, 219.762, 181.475, 193.375], [8, 230.708, 254.284, 182.665, 192.78], [8, 275.334, 287.964, 182.665, 193.375], [8, 330.906, 418.474, 182.665, 193.375], [8, 63.15, 87.568, 195.755, 207.06], [8, 372.164, 419.316, 195.755, 207.06], [8, 372.164, 390.688, 210.035, 220.74499999999998], [8, 65.676, 235.76, 334.98499999999996, 346.28999999999996], [8, 470.678, 541.406, 335.58, 346.28999999999996], [8, 88.41, 160.822, 358.78499999999997, 369.495], [8, 271.966, 311.53999999999996, 358.78499999999997, 369.495], [8, 622.2379999999999, 721.5939999999999, 358.78499999999997, 369.495], [8, 149.876, 162.506, 373.065, 383.18], [8, 136.404, 210.5, 387.34499999999997, 398.65], [8, 271.966, 370.47999999999996, 387.34499999999997, 398.65], [8, 436.998, 481.62399999999997, 388.53499999999997, 398.65], [8, 589.4, 663.496, 387.34499999999997, 398.65], [8, 88.41, 125.458, 417.09499999999997, 427.21], [8, 162.506, 222.28799999999998, 415.905, 426.615], [8, 271.966, 347.746, 415.905, 426.615], [8, 436.998, 537.196, 415.905, 426.615], [8, 622.2379999999999, 727.4879999999999, 415.905, 426.615], [8, 70.728, 79.99, 430.185, 440.29999999999995], [8, 111.98599999999999, 142.298, 442.085, 452.79499999999996], [8, 72.41199999999999, 81.67399999999999, 453.39, 464.09999999999997], [8, 105.25, 139.772, 456.36499999999995, 467.075], [8, 170.926, 223.13, 456.36499999999995, 467.075], [8, 271.966, 353.64, 440.29999999999995, 451.01], [8, 68.202, 138.088, 481.35499999999996, 502.775], [8, 473.204, 548.1419999999999, 492.065, 503.965], [8, 623.922, 701.386, 493.255, 504.56]]
2026-08-05 05:40:09,869 INFO     29 [qwen-vl-text] ═══ DONE ═══ 51 positions, pages=1, time=26.3s
2026-08-05 05:40:09,870 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:40:09,870 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:40:09,870 INFO     29 [qwen-vl-text] positions(50): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:40:09,870 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [50]
2026-08-05 05:40:10,049 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:40:10,050 INFO     29 [qwen-vl-text] LLM extraction start, text_len=380
2026-08-05 05:40:10,050 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:40:10,051 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 327, \"bbox_end\": 376, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "山西省医疗门诊收费票据（电子）\n山西省\n财政部监制\n票据代码:14060124\n交款人统一社会信用代\n交款\n票据号码:0155032568\n校验码: pc2vph\n开票日期:2026-01-06\n项目名称\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1.00\n466.00\nG布地格福吸入气雾剂【每瓶12\n2.00\n盒\n466.00 限慢性阻\n0揿】\n塞性肺疾\n病。\n金额合计（大写）肆佰陆拾陆元整\n(小写)466.00\n业务流水号\n门\n就诊日期:20260106\n型:综合医院\n医保类型:国家医保\n医保编号:\n48 性别:女\n医\n其他支付:0.00\n个人账户支付:0.00\n个人现金支付:156.11\n信\nt:309.89\n个人自费:156.11\n息\n自付:\nZ-方便门诊\n必泽斌号\n费专用章\n复核人:程小蕊\n收款人:段国丽",
    "role": "user"
  }
]
[92m05:40:10 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:40:10,052 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:40:10,053 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:40:10.052+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"a0ac621a908f11f1a3da71efcdd7cc1f": {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:40:12,555 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:40:12,555 INFO     29 [qwen-vl-text] LLM output (len=407):
{
  "encounter_date": "2026-01-06",
  "pharmacy": null,
  "medications": [
    {
      "name": "布地格福吸入气雾剂",
      "specification": "每瓶120揿",
      "dosage": null,
      "quantity": 2,
      "unit_price": null,
      "total_price": 466.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 466.00,
  "payment_method": null
}
2026-08-05 05:40:12,555 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-06]
2026-08-05 05:40:12,560 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1070278, prompt_len=1143
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共50行）
["山西省医疗门诊收费票据（电子）", "山西省", "财政部监制", "票据代码:14060124", "交款人统一社会信用代", "交款", "票据号码:0155032568", "校验码: pc2vph", "开票日期:2026-01-06", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1.00", "466.00", "G布地格福吸入气雾剂【每瓶12", "2.00", "盒", "466.00 限慢性阻", "0揿】", "塞性肺疾", "病。", "金额合计（大写）肆佰陆拾陆元整", "(小写)466.00", "业务流水号", "门", "就诊日期:20260106", "型:综合医院", "医保类型:国家医保", "医保编号:", "48 性别:女", "医", "其他支付:0.00", "个人账户支付:0.00", "个人现金支付:156.11", "信", "t:309.89", "个人自费:156.11", "息", "自付:", "Z-方便门诊", "必泽斌号", "费专用章", "复核人:程小蕊", "收款人:段国丽"]

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
2026-08-05 05:40:32,131 INFO     29 [qwen-vl-text] coord API raw response (len=3850):
[
	{"text": "山西省医疗门诊收费票据（电子）", "bbox": [295, 37, 695, 73]},
	{"text": "山西省", "bbox": [477, 76, 529, 98]},
	{"text": "财政部监制", "bbox": [462, 108, 545, 137]},
	{"text": "票据代码:14060124", "bbox": [70, 138, 188, 158]},
	{"text": "交款人统一社会信用代", "bbox": [70, 167, 210, 186], "bbox": [70, 167, 210, 186]},
	{"text": "交款", "bbox": [70, 194, 100, 212], "bbox": [70, 194, 100, 212]},
	{"text": "票据号码:0155032568", "bbox": [646, 138, 779, 158], "bbox": [646, 138, 779, 158]},
	{"text": "校验码: pc2vph", "bbox": [646, 167, 750, 187], "bbox": [646, 167, 750, 187]},
	{"text": "开票日期:2026-01-06", "bbox": [646, 194, 779, 212], "bbox": [646, 194, 779, 212]},
	{"text": "项目名称", "bbox": [139, 233, 194, 250], "bbox": [139, 233, 194, 250]},
	{"text": "数量/单位", "bbox": [280, 233, 344, 250], "bbox": [280, 233, 344, 250]},
	{"text": "金额（元）", "bbox": [375, 233, 436, 250], "bbox": [375, 233, 436, 250]},
	{"text": "备注", "bbox": [460, 233, 487, 250], "bbox": [460, 233, 487, 250]},
	{"text": "项目名称", "bbox": [571, 233, 626, 250], "bbox": [571, 233, 626, 250]},
	{"text": "数量/单位", "bbox": [711, 233, 773, 250], "bbox": [711, 233, 773, 250]},
	{"text": "金额（元）", "bbox": [805, 233, 865, 250], "bbox": [805, 233, 865, 250]},
	{"text": "备注", "bbox": [889, 233, 915, 250], "bbox": [889, 233, 915, 250]},
	{"text": "西药费", "bbox": [72, 269, 114, 290], "bbox": [72, 269, 114, 290]},
	{"text": "1.00", "bbox": [273, 270, 302, 289], "bbox": [273, 270, 302, 289]},
	{"text": "466.00", "bbox": [393, 270, 437, 289], "bbox": [393, 270, 437, 289]},
	{"text": "G布地格福吸入气雾剂【每瓶12", "bbox": [72, 300, 260, 320], "bbox": [72, 300, 260, 320]},
	{"text": "2.00", "bbox": [272, 301, 302, 320], "bbox": [272, 301, 302, 320]},
	{"text": "盒", "bbox": [325, 301, 341, 320], "bbox": [325, 301, 341, 320]},
	{"text": "466.00 限慢性阻", "bbox": [393, 301, 498, 320], "bbox": [393, 301, 498, 320]},
	{"text": "0揿】", "bbox": [72, 324, 100, 345], "bbox": [72, 324, 100, 345]},
	{"text": "塞性肺疾", "bbox": [441, 324, 498, 345], "bbox": [441, 324, 498, 345]},
	{"text": "病。", "bbox": [441, 348, 463, 368], "bbox": [441, 348, 463, 368]},
	{"text": "金额合计（大写）肆佰陆拾陆元整", "bbox": [76, 560, 280, 580], "bbox": [76, 560, 280, 580]},
	{"text": "(小写)466.00", "bbox": [559, 560, 644, 580], "bbox": [559, 560, 644, 580]},
	{"text": "业务流水号", "bbox": [103, 598, 170, 617], "bbox": [103, 598, 170, 617]},
	{"text": "门", "bbox": [323, 598, 341, 617], "bbox": [323, 598, 341, 617]},
	{"text": "就诊日期:20260106", "bbox": [740, 598, 860, 617], "bbox": [740, 598, 860, 617]},
	{"text": "型:综合医院", "bbox": [164, 648, 249, 667], "bbox": [164, 648, 249, 667]},
	{"text": "医保类型:国家医保", "bbox": [323, 646, 441, 667], "bbox": [323, 646, 441, 667]},
	{"text": "医保编号:", "bbox": [520, 650, 580, 669], "bbox": [520, 650, 580, 669]},
	{"text": "48 性别:女", "bbox": [717, 648, 790, 667], "bbox": [717, 648, 790, 667]},
	{"text": "医", "bbox": [103, 702, 126, 716], "bbox": [103, 702, 126, 716]},
	{"text": "t:309.89", "bbox": [204, 695, 263, 714], "bbox": [204, 695, 263, 714]},
	{"text": "其他支付:0.00", "bbox": [323, 695, 413, 714], "bbox": [323, 695, 413, 714]},
	{"text": "个人账户支付:0.00", "bbox": [520, 695, 639, 714], "bbox": [520, 695, 639, 714]},
	{"text": "个人现金支付:156.11", "bbox": [740, 695, 873, 714], "bbox": [740, 695, 873, 714]},
	{"text": "信", "bbox": [81, 720, 94, 738], "bbox": [81, 720, 94, 738]},
	{"text": "自付:", "bbox": [130, 740, 167, 759], "bbox": [130, 740, 167, 759]},
	{"text": "息", "bbox": [81, 758, 94, 778], "bbox": [81, 758, 94, 778]},
	{"text": "Z-方便门诊", "bbox": [122, 764, 190, 784], "bbox": [122, 764, 190, 784]},
	{"text": "必泽斌号", "bbox": [200, 764, 264, 784], "bbox": [200, 764, 264, 784]},
	{"text": "费专用章", "bbox": [68, 808, 165, 844], "bbox": [68, 808, 165, 844]},
	{"text": "复核人:程小蕊", "bbox": [563, 825, 653, 846], "bbox": [563, 825, 653, 846]},
	{"text": "收款人:段国丽", "bbox": [743, 827, 835, 846], "bbox": [743, 827, 835, 846]}
]
2026-08-05 05:40:32,131 INFO     29 [qwen-vl-text] coord API: raw_items=49, valid_items=49, elapsed=19.6s
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[0]: text=山西省医疗门诊收费票据（电子）, bbox=[295, 37, 695, 73]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[1]: text=山西省, bbox=[477, 76, 529, 98]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[2]: text=财政部监制, bbox=[462, 108, 545, 137]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[3]: text=票据代码:14060124, bbox=[70, 138, 188, 158]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[4]: text=交款人统一社会信用代, bbox=[70, 167, 210, 186]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[5]: text=交款, bbox=[70, 194, 100, 212]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[6]: text=票据号码:0155032568, bbox=[646, 138, 779, 158]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[7]: text=校验码: pc2vph, bbox=[646, 167, 750, 187]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[8]: text=开票日期:2026-01-06, bbox=[646, 194, 779, 212]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[9]: text=项目名称, bbox=[139, 233, 194, 250]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[10]: text=数量/单位, bbox=[280, 233, 344, 250]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[11]: text=金额（元）, bbox=[375, 233, 436, 250]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[12]: text=备注, bbox=[460, 233, 487, 250]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[13]: text=项目名称, bbox=[571, 233, 626, 250]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[14]: text=数量/单位, bbox=[711, 233, 773, 250]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[15]: text=金额（元）, bbox=[805, 233, 865, 250]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[16]: text=备注, bbox=[889, 233, 915, 250]
2026-08-05 05:40:32,132 INFO     29 [qwen-vl-text] coord item[17]: text=西药费, bbox=[72, 269, 114, 290]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[18]: text=1.00, bbox=[273, 270, 302, 289]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[19]: text=466.00, bbox=[393, 270, 437, 289]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[20]: text=G布地格福吸入气雾剂【每瓶12, bbox=[72, 300, 260, 320]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[21]: text=2.00, bbox=[272, 301, 302, 320]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[22]: text=盒, bbox=[325, 301, 341, 320]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[23]: text=466.00 限慢性阻, bbox=[393, 301, 498, 320]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[24]: text=0揿】, bbox=[72, 324, 100, 345]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[25]: text=塞性肺疾, bbox=[441, 324, 498, 345]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[26]: text=病。, bbox=[441, 348, 463, 368]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[27]: text=金额合计（大写）肆佰陆拾陆元整, bbox=[76, 560, 280, 580]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[28]: text=(小写)466.00, bbox=[559, 560, 644, 580]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[29]: text=业务流水号, bbox=[103, 598, 170, 617]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[30]: text=门, bbox=[323, 598, 341, 617]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[31]: text=就诊日期:20260106, bbox=[740, 598, 860, 617]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[32]: text=型:综合医院, bbox=[164, 648, 249, 667]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[33]: text=医保类型:国家医保, bbox=[323, 646, 441, 667]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[34]: text=医保编号:, bbox=[520, 650, 580, 669]
2026-08-05 05:40:32,133 INFO     29 [qwen-vl-text] coord item[35]: text=48 性别:女, bbox=[717, 648, 790, 667]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[36]: text=医, bbox=[103, 702, 126, 716]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[37]: text=t:309.89, bbox=[204, 695, 263, 714]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[38]: text=其他支付:0.00, bbox=[323, 695, 413, 714]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[39]: text=个人账户支付:0.00, bbox=[520, 695, 639, 714]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[40]: text=个人现金支付:156.11, bbox=[740, 695, 873, 714]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[41]: text=信, bbox=[81, 720, 94, 738]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[42]: text=自付:, bbox=[130, 740, 167, 759]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[43]: text=息, bbox=[81, 758, 94, 778]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[44]: text=Z-方便门诊, bbox=[122, 764, 190, 784]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[45]: text=必泽斌号, bbox=[200, 764, 264, 784]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[46]: text=费专用章, bbox=[68, 808, 165, 844]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[47]: text=复核人:程小蕊, bbox=[563, 825, 653, 846]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] coord item[48]: text=收款人:段国丽, bbox=[743, 827, 835, 846]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] page=9 — 50/50 coords, api_time=19.6s
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] new_positions (50):
[[9, 248.39, 585.1899999999999, 22.015, 43.434999999999995], [9, 401.63399999999996, 445.418, 45.22, 58.309999999999995], [9, 389.00399999999996, 458.89, 64.25999999999999, 81.515], [9, 58.94, 158.296, 82.11, 94.00999999999999], [9, 58.94, 176.82, 99.365, 110.67], [9, 58.94, 84.2, 115.42999999999999, 126.14], [9, 543.932, 655.918, 82.11, 94.00999999999999], [9, 543.932, 631.5, 99.365, 111.265], [9, 543.932, 655.918, 115.42999999999999, 126.14], [9, 117.038, 163.34799999999998, 138.635, 148.75], [9, 235.76, 289.64799999999997, 138.635, 148.75], [9, 315.75, 367.11199999999997, 138.635, 148.75], [9, 387.32, 410.054, 138.635, 148.75], [9, 480.782, 527.092, 138.635, 148.75], [9, 598.662, 650.866, 138.635, 148.75], [9, 677.81, 728.3299999999999, 138.635, 148.75], [9, 748.538, 770.43, 138.635, 148.75], [9, 60.623999999999995, 95.988, 160.055, 172.54999999999998], [9, 229.86599999999999, 254.284, 160.65, 171.95499999999998], [9, 330.906, 367.954, 160.65, 171.95499999999998], [9, 60.623999999999995, 218.92, 178.5, 190.39999999999998], [9, 229.024, 254.284, 179.095, 190.39999999999998], [9, 273.65, 287.122, 179.095, 190.39999999999998], [9, 330.906, 419.316, 179.095, 190.39999999999998], [9, 60.623999999999995, 84.2, 192.78, 205.27499999999998], [9, 371.322, 419.316, 192.78, 205.27499999999998], [9, 371.322, 389.846, 207.06, 218.95999999999998], [9, 63.992, 235.76, 333.2, 345.09999999999997], [9, 470.678, 542.2479999999999, 333.2, 345.09999999999997], [9, 86.726, 143.14, 355.81, 367.115], [9, 271.966, 287.122, 355.81, 367.115], [9, 623.0799999999999, 724.12, 355.81, 367.115], [9, 138.088, 209.658, 385.56, 396.865], [9, 271.966, 371.322, 384.37, 396.865], [9, 437.84, 488.35999999999996, 386.75, 398.055], [9, 603.7139999999999, 665.18, 385.56, 396.865], [9, 86.726, 106.092, 417.69, 426.02], [9, 171.768, 221.446, 413.525, 424.83], [9, 271.966, 347.746, 413.525, 424.83], [9, 437.84, 538.038, 413.525, 424.83], [9, 623.0799999999999, 735.066, 413.525, 424.83], [9, 68.202, 79.148, 428.4, 439.10999999999996], [9, 109.46, 140.614, 440.29999999999995, 451.60499999999996], [9, 68.202, 79.148, 451.01, 462.90999999999997], [9, 102.72399999999999, 159.98, 454.58, 466.47999999999996], [9, 168.4, 222.28799999999998, 454.58, 466.47999999999996], [9, 57.256, 138.93, 480.76, 502.17999999999995], [9, 474.046, 549.826, 490.875, 503.37], [9, 625.606, 703.0699999999999, 492.065, 503.37], [9, 625.606, 703.0699999999999, 492.065, 503.37]]
2026-08-05 05:40:32,134 INFO     29 [qwen-vl-text] ═══ DONE ═══ 50 positions, pages=1, time=22.3s
2026-08-05 05:40:32,148 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 05:40:32,149 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Extractor:Medication | outputs={"chunks": "5 items, types={'MedicationRecord': 5}", "html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:40:32,149 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 05:40:32,154 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:40:32,154 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 05:40:32,154 INFO     29 [qwen-vl-text] positions(40): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:40:32,154 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [40]
2026-08-05 05:40:32,301 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:40:32,302 INFO     29 [qwen-vl-text] LLM extraction start, text_len=282
2026-08-05 05:40:32,302 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:40:32,302 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 99, \"bbox_end\": 138, \"encounter_dates\": [\"2026-01-20\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "【处方】导引单\nID:\n姓名:\n年龄：68岁\n性别：女\n费别：普通患者\n诊断：支气管哮喘(急性发作期)\n开单科室：呼吸与危重症医学科\n开单时间：2026-01-20 17:33:34\n取药排\n药品名称\n规格\n数量\n1.醋酸泼尼松片\n5mg*100片\n1瓶\n15.0mg\n口服\n每日一次\n微信/支付宝\n扫码支付\n金额：4.8元\n执行科室：门诊药房\n地点：门诊大厅一层西侧\n医生\n处方当日有效，补打导引单不可作为取药凭证\n【患者留存】\nID:\n姓名:\n年龄：68岁\n性别：女\n药品名称\n规格\n数量\n1.醋酸泼尼松片\n5mg*100片\n1瓶\n15.0mg\n口服\n每日一次",
    "role": "user"
  }
]
[92m05:40:32 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:40:32,304 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:40:37,266 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:40:37,266 INFO     29 [qwen-vl-text] LLM output (len=424):
{
  "encounter_date": "2026-01-20",
  "prescription_type": "取药执行单",
  "prescriber": null,
  "department": "呼吸与危重症医学科",
  "diagnosis": "支气管哮喘(急性发作期)",
  "items": [
    {
      "drug_generic_name": "醋酸泼尼松片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "15.0mg",
      "frequency": "每日一次",
      "route": "口服",
      "duration_days": null,
      "quantity": "1瓶",
      "notes": null
    }
  ]
}
2026-08-05 05:40:37,267 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-20]
2026-08-05 05:40:37,269 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=570528, prompt_len=1015
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["【处方】导引单", "ID:", "姓名:", "年龄：68岁", "性别：女", "费别：普通患者", "诊断：支气管哮喘(急性发作期)", "开单科室：呼吸与危重症医学科", "开单时间：2026-01-20 17:33:34", "取药排", "药品名称", "规格", "数量", "1.醋酸泼尼松片", "5mg*100片", "1瓶", "15.0mg", "口服", "每日一次", "微信/支付宝", "扫码支付", "金额：4.8元", "执行科室：门诊药房", "地点：门诊大厅一层西侧", "医生", "处方当日有效，补打导引单不可作为取药凭证", "【患者留存】", "ID:", "姓名:", "年龄：68岁", "性别：女", "药品名称", "规格", "数量", "1.醋酸泼尼松片", "5mg*100片", "1瓶", "15.0mg", "口服", "每日一次"]

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
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord API raw response (len=2043):
[
	{"text": "【处方】导引单", "bbox": [364, 67, 616, 94]},
	{"text": "ID:", "bbox": [312, 114, 340, 128]},
	{"text": "姓名:", "bbox": [561, 113, 612, 128]},
	{"text": "年龄：68岁", "bbox": [312, 136, 417, 151]},
	{"text": "性别：女", "bbox": [561, 136, 647, 151]},
	{"text": "费别：普通患者", "bbox": [312, 159, 459, 174]},
	{"text": "诊断：支气管哮喘(急性发作期)", "bbox": [312, 181, 605, 197]},
	{"text": "开单科室：呼吸与危重症医学科", "bbox": [312, 265, 607, 280]},
	{"text": "开单时间：2026-01-20 17:33:34", "bbox": [312, 289, 620, 304]},
	{"text": "取药排", "bbox": [677, 263, 700, 310]},
	{"text": "药品名称", "bbox": [312, 421, 398, 437]},
	{"text": "规格", "bbox": [512, 421, 553, 437]},
	{"text": "数量", "bbox": [610, 421, 653, 437]},
	{"text": "1.醋酸泼尼松片", "bbox": [312, 458, 457, 474]},
	{"text": "5mg*100片", "bbox": [478, 459, 572, 474]},
	{"text": "1瓶", "bbox": [594, 459, 626, 474]},
	{"text": "15.0mg", "bbox": [364, 484, 432, 499]},
	{"text": "口服", "bbox": [464, 484, 505, 499]},
	{"text": "每日一次", "bbox": [594, 484, 677, 499]},
	{"text": "微信/支付宝", "bbox": [336, 512, 452, 527]},
	{"text": "扫码支付", "bbox": [355, 528, 442, 543]},
	{"text": "金额：4.8元", "bbox": [496, 536, 600, 551]},
	{"text": "执行科室：门诊药房", "bbox": [496, 567, 681, 582]},
	{"text": "地点：门诊大厅一层西侧", "bbox": [496, 602, 722, 617]},
	{"text": "医生", "bbox": [496, 635, 534, 650]},
	{"text": "处方当日有效，补打导引单不可作为取药凭证", "bbox": [298, 673, 718, 688]},
	{"text": "【患者留存】", "bbox": [414, 745, 579, 767]},
	{"text": "ID:", "bbox": [319, 780, 346, 793]},
	{"text": "姓名:", "bbox": [560, 779, 609, 794]},
	{"text": "年龄：68岁", "bbox": [319, 801, 420, 816]},
	{"text": "性别：女", "bbox": [560, 801, 642, 816]},
	{"text": "药品名称", "bbox": [319, 828, 401, 843]},
	{"text": "规格", "bbox": [512, 828, 551, 843]},
	{"text": "数量", "bbox": [608, 828, 650, 843]},
	{"text": "1.醋酸泼尼松片", "bbox": [319, 866, 458, 881]},
	{"text": "5mg*100片", "bbox": [479, 867, 570, 881]},
	{"text": "1瓶", "bbox": [592, 867, 623, 881]},
	{"text": "15.0mg", "bbox": [368, 891, 434, 906]},
	{"text": "口服", "bbox": [465, 891, 504, 906]},
	{"text": "每日一次", "bbox": [591, 891, 672, 906]}
]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=10.4s
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[0]: text=【处方】导引单, bbox=[364, 67, 616, 94]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[1]: text=ID:, bbox=[312, 114, 340, 128]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[561, 113, 612, 128]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：68岁, bbox=[312, 136, 417, 151]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[561, 136, 647, 151]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[5]: text=费别：普通患者, bbox=[312, 159, 459, 174]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[6]: text=诊断：支气管哮喘(急性发作期), bbox=[312, 181, 605, 197]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[7]: text=开单科室：呼吸与危重症医学科, bbox=[312, 265, 607, 280]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[8]: text=开单时间：2026-01-20 17:33:34, bbox=[312, 289, 620, 304]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[9]: text=取药排, bbox=[677, 263, 700, 310]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[10]: text=药品名称, bbox=[312, 421, 398, 437]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[11]: text=规格, bbox=[512, 421, 553, 437]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[12]: text=数量, bbox=[610, 421, 653, 437]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[13]: text=1.醋酸泼尼松片, bbox=[312, 458, 457, 474]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[14]: text=5mg*100片, bbox=[478, 459, 572, 474]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[15]: text=1瓶, bbox=[594, 459, 626, 474]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[16]: text=15.0mg, bbox=[364, 484, 432, 499]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[17]: text=口服, bbox=[464, 484, 505, 499]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[18]: text=每日一次, bbox=[594, 484, 677, 499]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[19]: text=微信/支付宝, bbox=[336, 512, 452, 527]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[20]: text=扫码支付, bbox=[355, 528, 442, 543]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[21]: text=金额：4.8元, bbox=[496, 536, 600, 551]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[22]: text=执行科室：门诊药房, bbox=[496, 567, 681, 582]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[23]: text=地点：门诊大厅一层西侧, bbox=[496, 602, 722, 617]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[24]: text=医生, bbox=[496, 635, 534, 650]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[25]: text=处方当日有效，补打导引单不可作为取药凭证, bbox=[298, 673, 718, 688]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[26]: text=【患者留存】, bbox=[414, 745, 579, 767]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[27]: text=ID:, bbox=[319, 780, 346, 793]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[28]: text=姓名:, bbox=[560, 779, 609, 794]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[29]: text=年龄：68岁, bbox=[319, 801, 420, 816]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[30]: text=性别：女, bbox=[560, 801, 642, 816]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[31]: text=药品名称, bbox=[319, 828, 401, 843]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[32]: text=规格, bbox=[512, 828, 551, 843]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[33]: text=数量, bbox=[608, 828, 650, 843]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[34]: text=1.醋酸泼尼松片, bbox=[319, 866, 458, 881]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[35]: text=5mg*100片, bbox=[479, 867, 570, 881]
2026-08-05 05:40:47,669 INFO     29 [qwen-vl-text] coord item[36]: text=1瓶, bbox=[592, 867, 623, 881]
2026-08-05 05:40:47,670 INFO     29 [qwen-vl-text] coord item[37]: text=15.0mg, bbox=[368, 891, 434, 906]
2026-08-05 05:40:47,670 INFO     29 [qwen-vl-text] coord item[38]: text=口服, bbox=[465, 891, 504, 906]
2026-08-05 05:40:47,670 INFO     29 [qwen-vl-text] coord item[39]: text=每日一次, bbox=[591, 891, 672, 906]
2026-08-05 05:40:47,670 INFO     29 [qwen-vl-text] page=4 — 40/40 coords, api_time=10.4s
2026-08-05 05:40:47,670 INFO     29 [qwen-vl-text] new_positions (40):
[[4, 216.57999999999998, 366.52, 56.414, 79.148], [4, 185.64, 202.29999999999998, 95.988, 107.776], [4, 333.79499999999996, 364.14, 95.146, 107.776], [4, 185.64, 248.11499999999998, 114.512, 127.142], [4, 333.79499999999996, 384.965, 114.512, 127.142], [4, 185.64, 273.10499999999996, 133.878, 146.50799999999998], [4, 185.64, 359.97499999999997, 152.402, 165.874], [4, 185.64, 361.16499999999996, 223.13, 235.76], [4, 185.64, 368.9, 243.338, 255.968], [4, 402.815, 416.5, 221.446, 261.02], [4, 185.64, 236.81, 354.48199999999997, 367.954], [4, 304.64, 329.03499999999997, 354.48199999999997, 367.954], [4, 362.95, 388.53499999999997, 354.48199999999997, 367.954], [4, 185.64, 271.91499999999996, 385.63599999999997, 399.108], [4, 284.40999999999997, 340.34, 386.478, 399.108], [4, 353.43, 372.46999999999997, 386.478, 399.108], [4, 216.57999999999998, 257.03999999999996, 407.52799999999996, 420.15799999999996], [4, 276.08, 300.47499999999997, 407.52799999999996, 420.15799999999996], [4, 353.43, 402.815, 407.52799999999996, 420.15799999999996], [4, 199.92, 268.94, 431.104, 443.734], [4, 211.225, 262.99, 444.57599999999996, 457.20599999999996], [4, 295.12, 357.0, 451.312, 463.942], [4, 295.12, 405.195, 477.414, 490.044], [4, 295.12, 429.59, 506.88399999999996, 519.514], [4, 295.12, 317.72999999999996, 534.67, 547.3], [4, 177.31, 427.21, 566.6659999999999, 579.2959999999999], [4, 246.32999999999998, 344.505, 627.29, 645.814], [4, 189.80499999999998, 205.87, 656.76, 667.706], [4, 333.2, 362.35499999999996, 655.918, 668.548], [4, 189.80499999999998, 249.89999999999998, 674.442, 687.072], [4, 333.2, 381.99, 674.442, 687.072], [4, 189.80499999999998, 238.595, 697.1759999999999, 709.8059999999999], [4, 304.64, 327.84499999999997, 697.1759999999999, 709.8059999999999], [4, 361.76, 386.75, 697.1759999999999, 709.8059999999999], [4, 189.80499999999998, 272.51, 729.172, 741.802], [4, 285.005, 339.15, 730.014, 741.802], [4, 352.24, 370.685, 730.014, 741.802], [4, 218.95999999999998, 258.22999999999996, 750.222, 762.852], [4, 276.675, 299.88, 750.222, 762.852], [4, 351.645, 399.84, 750.222, 762.852]]
2026-08-05 05:40:47,670 INFO     29 [qwen-vl-text] ═══ DONE ═══ 40 positions, pages=1, time=15.5s
2026-08-05 05:40:47,676 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 05:40:47,677 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items, types={'PrescriptionRecord': 1}", "html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:40:47,677 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 05:40:47,678 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:40:47.677+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"a0ac621a908f11f1a3da71efcdd7cc1f": {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:40:47,683 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:40:47,683 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-05 05:40:47,684 INFO     29 [qwen-vl-text] positions(61): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:40:47,684 INFO     29 [qwen-vl-text] page grouping: [1, 2], lines per page: [38, 23]
2026-08-05 05:40:47,869 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:40:48,022 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:40:48,023 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1454
2026-08-05 05:40:48,023 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:40:48,023 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 16, \"bbox_end\": 76, \"encounter_dates\": [\"2024-03-15\", \"2024-03-18\"], \"department\": \"呼吸与危重症二组病区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n姓名：\n性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：\n住院号：\n姓名\n性别：女\n年龄：66岁\n职业：农民\n入院日期：2024年03月15日10时\n出院日期：2024年03月18日11时\n住院天数：3天\n入院时情况：发作性喘息10年，加重2月。\n入院诊断：1.支气管哮喘(急性发作期)\n2.低氧血症\n诊疗经过：完善相关化验及检查：\n血气分析：吸氧浓度21.0%，酸碱度7.414，二氧化碳分压35.3mmHg，氧分压67.9mmHg↓，\n实际碱剩余-1.4mmol/L，血浆碳酸氢盐浓度22.2mmol/L，乳酸浓度0.6mmol/\nL，氧合指数323mmHg↓，肺泡动脉氧分压差27.7mmHg↑。\n血常规：白细胞计数4.06*10^9/L，红细胞计数4.49*10^12/L，血红蛋白131g/L，血小板\n280*10^9/L。红细胞沉降率5mm/H。C反应蛋白2.43mg/L。\n肝+肾+离子：血清丙氨酸氨基转移酶10.80U/L，血清天门冬氨酸氨基转移酶15.60U/L，尿\n素4.40mmol/L，肌酐51.00umol/L，钾3.79mmol/L，钠143.00mmol/L，氯\n109.00mmol/L。\n免疫球蛋白：E128.00IU/mL↑。\n呼吸道病原体抗体：阴性；新型冠状病毒核酸：阴性；痰培养：阴性；\n尿常规：尿常规检验报告尿隐血-，尿白细胞3+，尿蛋白-，白细胞134个/uL↑。\n肿瘤标志物、心肺四项、凝血、便常规未见明显异常。\n腹部彩超：肝囊肿（多发）胆、胰、脾、双肾未见明显异常；\n心脏彩超：EF：68% 三尖瓣口少量返流 主动脉瓣口少量返流 左室舒张功能减低 左室收\n缩功能正常；\n胸部CT：双肺实性微结节，建议随诊 肝内低密度灶，考虑囊肿。\n肺功能：激发前：FEV1/FVC 86.86%，FEV1 96% FVC 90.2% 通气功能大致正常，吸入乙\n酰甲胆碱 32mg/ml（第5管）激发后FEV1/FVC 72.8%，FEV1下降20.82%，激发\n试验（+），DLCO 53.3% 肺弥散功能显著减退 RV/TLC 65.72%,残总比升高。\n呼出气一氧化氮测定：FENO50 25ppb 混合型气道炎症 FENO200 18ppb 小气道炎症 CaNO\n14.7ppb 肺泡炎症。FENO10 233。\n2.予以抗过敏、扩张气道、促进排痰、抗感染等对症治疗。\n第1页\n出院记录\n姓名：\n性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：\n床号：\n出院时情况：患者气短明显缓解，偶有咳嗽，无明显咳痰，精神可。查体：口唇暗紫\n色，咽部无充血，扁桃体无肿大；双肺未闻及干湿性啰音，心律齐，未闻及心脏瓣膜杂\n音；腹软，无压痛、反跳痛，双下肢无水肿。\n出院诊断：1.支气管哮喘(急性发作期)\n2.低氧血症\n3.肺部阴影(双肺结节性质待查)\n4.多发性肝囊肿\n出院医嘱：1、加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必\n要时吸氧。\n2、院外继续通药物治疗：\n氯雷他定片 10 mg/片 口服 睡前(1月)\n孟鲁司特片 10 mg/片 口服 睡前(1月)\n布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 (3月)\n茶碱缓释片 0.1g/片 口服 2次/日(长期)\n3、3月后复查胸部高分辨CT，总IgE、肺功能+扩张+弥散\n4、2周后呼吸科门诊复诊，不适随诊。\n签名：\n记录日期：2024年03月18日11时56分\n第2页",
    "role": "user"
  }
]
[92m05:40:48 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:40:48,024 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:41:04,081 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:41:04,081 INFO     29 [qwen-vl-text] LLM output (len=2576):
{
  "encounter_date": "2024-03-18",
  "admission_date": "2024-03-15",
  "discharge_date": "2024-03-18",
  "hospital_days": 3,
  "department": "呼吸与危重症二组病区",
  "bed_number": null,
  "admission_condition": "发作性喘息10年，加重2月。",
  "admission_diagnoses": [
    {
      "name": "支气管哮喘(急性发作期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "低氧血症",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "完善相关化验及检查：血气分析、血常规、肝肾功能离子、免疫球蛋白、呼吸道病原体抗体、新型冠状病毒核酸、痰培养、尿常规、肿瘤标志物、心肺四项、凝血、便常规、腹部彩超、心脏彩超、胸部CT、肺功能、呼出气一氧化氮测定。予以抗过敏、扩张气道、促进排痰、抗感染等对症治疗。",
  "auxiliary_exams": "血气分析：吸氧浓度21.0%，酸碱度7.414，二氧化碳分压35.3mmHg，氧分压67.9mmHg↓，实际碱剩余-1.4mmol/L，血浆碳酸氢盐浓度22.2mmol/L，乳酸浓度0.6mmol/L，氧合指数323mmHg↓，肺泡动脉氧分压差27.7mmHg↑。血常规：白细胞计数4.06*10^9/L，红细胞计数4.49*10^12/L，血红蛋白131g/L，血小板280*10^9/L。红细胞沉降率5mm/H。C反应蛋白2.43mg/L。肝+肾+离子：血清丙氨酸氨基转移酶10.80U/L，血清天门冬氨酸氨基转移酶15.60U/L，尿素4.40mmol/L，肌酐51.00umol/L，钾3.79mmol/L，钠143.00mmol/L，氯109.00mmol/L。免疫球蛋白：E128.00IU/mL↑。呼吸道病原体抗体：阴性；新型冠状病毒核酸：阴性；痰培养：阴性；尿常规：尿隐血-，尿白细胞3+，尿蛋白-，白细胞134个/uL↑。肿瘤标志物、心肺四项、凝血、便常规未见明显异常。肺功能：激发前：FEV1/FVC 86.86%，FEV1 96% FVC 90.2% 通气功能大致正常，吸入乙酰甲胆碱 32mg/ml（第5管）激发后FEV1/FVC 72.8%，FEV1下降20.82%，激发试验（+），DLCO 53.3% 肺弥散功能显著减退 RV/TLC 65.72%,残总比升高。呼出气一氧化氮测定：FENO50 25ppb 混合型气道炎症 FENO200 18ppb 小气道炎症 CaNO 14.7ppb 肺泡炎症。FENO10 233。",
  "imaging_findings": "腹部彩超：肝囊肿（多发）胆、胰、脾、双肾未见明显异常；心脏彩超：EF：68% 三尖瓣口少量返流 主动脉瓣口少量返流 左室舒张功能减低 左室收缩功能正常；胸部CT：双肺实性微结节，建议随诊 肝内低密度灶，考虑囊肿。",
  "discharge_diagnoses": [
    {
      "name": "支气管哮喘(急性发作期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "低氧血症",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺部阴影(双肺结节性质待查)",
      "diagnosis_type": "西医"
    },
    {
      "name": "多发性肝囊肿",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者气短明显缓解，偶有咳嗽，无明显咳痰，精神可。查体：口唇暗紫色，咽部无充血，扁桃体无肿大；双肺未闻及干湿性啰音，心律齐，未闻及心脏瓣膜杂音；腹软，无压痛、反跳痛，双下肢无水肿。",
  "outcome": "好转",
  "discharge_orders": "1、加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必要时吸氧。2、院外继续通药物治疗：氯雷他定片 10 mg/片 口服 睡前(1月)；孟鲁司特片 10 mg/片 口服 睡前(1月)；布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 (3月)；茶碱缓释片 0.1g/片 口服 2次/日(长期)。3、3月后复查胸部高分辨CT，总IgE、肺功能+扩张+弥散。4、2周后呼吸科门诊复诊，不适随诊。",
  "do_medications": [
    "氯雷他定片 10 mg/片 口服 睡前 1月",
    "孟鲁司特片 10 mg/片 口服 睡前 1月",
    "布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 3月",
    "茶碱缓释片 0.1g/片 口服 2次/日 长期"
  ],
  "do_follow_up": "2周后呼吸科门诊复诊，不适随诊。",
  "do_precautions": [
    "加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必要时吸氧"
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
2026-08-05 05:41:04,081 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-03-18]
2026-08-05 05:41:04,083 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=978660, prompt_len=1744
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["出院记录", "姓名：", "性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：", "住院号：", "姓名", "性别：女", "年龄：66岁", "职业：农民", "入院日期：2024年03月15日10时", "出院日期：2024年03月18日11时", "住院天数：3天", "入院时情况：发作性喘息10年，加重2月。", "入院诊断：1.支气管哮喘(急性发作期)", "2.低氧血症", "诊疗经过：完善相关化验及检查：", "血气分析：吸氧浓度21.0%，酸碱度7.414，二氧化碳分压35.3mmHg，氧分压67.9mmHg↓，", "实际碱剩余-1.4mmol/L，血浆碳酸氢盐浓度22.2mmol/L，乳酸浓度0.6mmol/", "L，氧合指数323mmHg↓，肺泡动脉氧分压差27.7mmHg↑。", "血常规：白细胞计数4.06*10^9/L，红细胞计数4.49*10^12/L，血红蛋白131g/L，血小板", "280*10^9/L。红细胞沉降率5mm/H。C反应蛋白2.43mg/L。", "肝+肾+离子：血清丙氨酸氨基转移酶10.80U/L，血清天门冬氨酸氨基转移酶15.60U/L，尿", "素4.40mmol/L，肌酐51.00umol/L，钾3.79mmol/L，钠143.00mmol/L，氯", "109.00mmol/L。", "免疫球蛋白：E128.00IU/mL↑。", "呼吸道病原体抗体：阴性；新型冠状病毒核酸：阴性；痰培养：阴性；", "尿常规：尿常规检验报告尿隐血-，尿白细胞3+，尿蛋白-，白细胞134个/uL↑。", "肿瘤标志物、心肺四项、凝血、便常规未见明显异常。", "腹部彩超：肝囊肿（多发）胆、胰、脾、双肾未见明显异常；", "心脏彩超：EF：68% 三尖瓣口少量返流 主动脉瓣口少量返流 左室舒张功能减低 左室收", "缩功能正常；", "胸部CT：双肺实性微结节，建议随诊 肝内低密度灶，考虑囊肿。", "肺功能：激发前：FEV1/FVC 86.86%，FEV1 96% FVC 90.2% 通气功能大致正常，吸入乙", "酰甲胆碱 32mg/ml（第5管）激发后FEV1/FVC 72.8%，FEV1下降20.82%，激发", "试验（+），DLCO 53.3% 肺弥散功能显著减退 RV/TLC 65.72%,残总比升高。", "呼出气一氧化氮测定：FENO50 25ppb 混合型气道炎症 FENO200 18ppb 小气道炎症 CaNO", "14.7ppb 肺泡炎症。FENO10 233。", "2.予以抗过敏、扩张气道、促进排痰、抗感染等对症治疗。", "第1页"]

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
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord API raw response (len=2692):
[
	{"text": "出院记录", "bbox": [465, 124, 556, 142]},
	{"text": "姓名：", "bbox": [169, 147, 189, 159]},
	{"text": "性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：", "bbox": [293, 147, 706, 159]},
	{"text": "住院号：", "bbox": [795, 147, 847, 159]},
	{"text": "姓名", "bbox": [169, 180, 203, 192]},
	{"text": "性别：女", "bbox": [356, 180, 418, 192]},
	{"text": "年龄：66岁", "bbox": [506, 180, 584, 192]},
	{"text": "职业：农民", "bbox": [677, 180, 758, 192]},
	{"text": "入院日期：2024年03月15日10时", "bbox": [173, 206, 421, 219]},
	{"text": "出院日期：2024年03月18日11时", "bbox": [447, 206, 694, 219]},
	{"text": "住院天数：3天", "bbox": [710, 206, 827, 219]},
	{"text": "入院时情况：发作性喘息10年，加重2月。", "bbox": [169, 233, 477, 246]},
	{"text": "入院诊断：1.支气管哮喘(急性发作期)", "bbox": [169, 256, 466, 270]},
	{"text": "2.低氧血症", "bbox": [256, 280, 346, 293]},
	{"text": "诊疗经过：完善相关化验及检查：", "bbox": [169, 303, 421, 316]},
	{"text": "血气分析：吸氧浓度21.0%，酸碱度7.414，二氧化碳分压35.3mmHg，氧分压67.9mmHg↓，", "bbox": [169, 327, 847, 340]},
	{"text": "实际碱剩余-1.4mmol/L，血浆碳酸氢盐浓度22.2mmol/L，乳酸浓度0.6mmol/", "bbox": [256, 350, 858, 364]},
	{"text": "L，氧合指数323mmHg↓，肺泡动脉氧分压差27.7mmHg↑。", "bbox": [256, 373, 688, 387]},
	{"text": "血常规：白细胞计数4.06*10^9/L，红细胞计数4.49*10^12/L，血红蛋白131g/L，血小板", "bbox": [169, 396, 858, 410]},
	{"text": "280*10^9/L。红细胞沉降率5mm/H。C反应蛋白2.43mg/L。", "bbox": [256, 419, 688, 433]},
	{"text": "肝+肾+离子：血清丙氨酸氨基转移酶10.80U/L，血清天门冬氨酸氨基转移酶15.60U/L，尿", "bbox": [169, 443, 858, 456]},
	{"text": "素4.40mmol/L，肌酐51.00umol/L，钾3.79mmol/L，钠143.00mmol/L，氯", "bbox": [256, 466, 858, 479]},
	{"text": "109.00mmol/L。", "bbox": [256, 489, 371, 502]},
	{"text": "免疫球蛋白：E128.00IU/mL↑。", "bbox": [169, 512, 407, 526]},
	{"text": "呼吸道病原体抗体：阴性；新型冠状病毒核酸：阴性；痰培养：阴性；", "bbox": [169, 535, 703, 549]},
	{"text": "尿常规：尿常规检验报告尿隐血-，尿白细胞3+，尿蛋白-，白细胞134个/uL↑。", "bbox": [169, 558, 786, 572]},
	{"text": "肿瘤标志物、心肺四项、凝血、便常规未见明显异常。", "bbox": [169, 581, 580, 595]},
	{"text": "腹部彩超：肝囊肿（多发）胆、胰、脾、双肾未见明显异常；", "bbox": [169, 605, 641, 618]},
	{"text": "心脏彩超：EF：68% 三尖瓣口少量返流 主动脉瓣口少量返流 左室舒张功能减低 左室收", "bbox": [169, 628, 858, 642]},
	{"text": "缩功能正常；", "bbox": [256, 652, 352, 665]},
	{"text": "胸部CT：双肺实性微结节，建议随诊 肝内低密度灶，考虑囊肿。", "bbox": [169, 675, 661, 688]},
	{"text": "肺功能：激发前：FEV1/FVC 86.86%，FEV1 96% FVC 90.2% 通气功能大致正常，吸入乙", "bbox": [169, 698, 856, 712]},
	{"text": "酰甲胆碱 32mg/ml（第5管）激发后FEV1/FVC 72.8%，FEV1下降20.82%，激发", "bbox": [256, 721, 856, 735]},
	{"text": "试验（+），DLCO 53.3% 肺弥散功能显著减退 RV/TLC 65.72%,残总比升高。", "bbox": [256, 744, 837, 758]},
	{"text": "呼出气一氧化氮测定：FENO50 25ppb 混合型气道炎症 FENO200 18ppb 小气道炎症 CaNO", "bbox": [169, 767, 856, 781]},
	{"text": "14.7ppb 肺泡炎症。FENO10 233。", "bbox": [266, 790, 527, 804]},
	{"text": "2.予以抗过敏、扩张气道、促进排痰、抗感染等对症治疗。", "bbox": [169, 814, 614, 827]},
	{"text": "第1页", "bbox": [489, 843, 528, 855]}
]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=15.2s
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[465, 124, 556, 142]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[169, 147, 189, 159]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：, bbox=[293, 147, 706, 159]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[3]: text=住院号：, bbox=[795, 147, 847, 159]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[169, 180, 203, 192]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女, bbox=[356, 180, 418, 192]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：66岁, bbox=[506, 180, 584, 192]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[7]: text=职业：农民, bbox=[677, 180, 758, 192]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[8]: text=入院日期：2024年03月15日10时, bbox=[173, 206, 421, 219]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[9]: text=出院日期：2024年03月18日11时, bbox=[447, 206, 694, 219]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[10]: text=住院天数：3天, bbox=[710, 206, 827, 219]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[11]: text=入院时情况：发作性喘息10年，加重2月。, bbox=[169, 233, 477, 246]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[12]: text=入院诊断：1.支气管哮喘(急性发作期), bbox=[169, 256, 466, 270]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[13]: text=2.低氧血症, bbox=[256, 280, 346, 293]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[14]: text=诊疗经过：完善相关化验及检查：, bbox=[169, 303, 421, 316]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[15]: text=血气分析：吸氧浓度21.0%，酸碱度7.414，二氧化碳分压35.3mmHg，氧分压67.9mmHg↓，, bbox=[169, 327, 847, 340]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[16]: text=实际碱剩余-1.4mmol/L，血浆碳酸氢盐浓度22.2mmol/L，乳酸浓度0.6mmol/, bbox=[256, 350, 858, 364]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[17]: text=L，氧合指数323mmHg↓，肺泡动脉氧分压差27.7mmHg↑。, bbox=[256, 373, 688, 387]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[18]: text=血常规：白细胞计数4.06*10^9/L，红细胞计数4.49*10^12/L，血红蛋白131g/L，血小板, bbox=[169, 396, 858, 410]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[19]: text=280*10^9/L。红细胞沉降率5mm/H。C反应蛋白2.43mg/L。, bbox=[256, 419, 688, 433]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[20]: text=肝+肾+离子：血清丙氨酸氨基转移酶10.80U/L，血清天门冬氨酸氨基转移酶15.60U/L，尿, bbox=[169, 443, 858, 456]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[21]: text=素4.40mmol/L，肌酐51.00umol/L，钾3.79mmol/L，钠143.00mmol/L，氯, bbox=[256, 466, 858, 479]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[22]: text=109.00mmol/L。, bbox=[256, 489, 371, 502]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[23]: text=免疫球蛋白：E128.00IU/mL↑。, bbox=[169, 512, 407, 526]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[24]: text=呼吸道病原体抗体：阴性；新型冠状病毒核酸：阴性；痰培养：阴性；, bbox=[169, 535, 703, 549]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[25]: text=尿常规：尿常规检验报告尿隐血-，尿白细胞3+，尿蛋白-，白细胞134个/uL↑。, bbox=[169, 558, 786, 572]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[26]: text=肿瘤标志物、心肺四项、凝血、便常规未见明显异常。, bbox=[169, 581, 580, 595]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[27]: text=腹部彩超：肝囊肿（多发）胆、胰、脾、双肾未见明显异常；, bbox=[169, 605, 641, 618]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[28]: text=心脏彩超：EF：68% 三尖瓣口少量返流 主动脉瓣口少量返流 左室舒张功能减低 左室收, bbox=[169, 628, 858, 642]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[29]: text=缩功能正常；, bbox=[256, 652, 352, 665]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[30]: text=胸部CT：双肺实性微结节，建议随诊 肝内低密度灶，考虑囊肿。, bbox=[169, 675, 661, 688]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[31]: text=肺功能：激发前：FEV1/FVC 86.86%，FEV1 96% FVC 90.2% 通气功能大致正常，吸入乙, bbox=[169, 698, 856, 712]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[32]: text=酰甲胆碱 32mg/ml（第5管）激发后FEV1/FVC 72.8%，FEV1下降20.82%，激发, bbox=[256, 721, 856, 735]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[33]: text=试验（+），DLCO 53.3% 肺弥散功能显著减退 RV/TLC 65.72%,残总比升高。, bbox=[256, 744, 837, 758]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[34]: text=呼出气一氧化氮测定：FENO50 25ppb 混合型气道炎症 FENO200 18ppb 小气道炎症 CaNO, bbox=[169, 767, 856, 781]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[35]: text=14.7ppb 肺泡炎症。FENO10 233。, bbox=[266, 790, 527, 804]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[36]: text=2.予以抗过敏、扩张气道、促进排痰、抗感染等对症治疗。, bbox=[169, 814, 614, 827]
2026-08-05 05:41:19,320 INFO     29 [qwen-vl-text] coord item[37]: text=第1页, bbox=[489, 843, 528, 855]
2026-08-05 05:41:19,321 INFO     29 [qwen-vl-text] page=1 — 38/38 coords, api_time=15.2s
2026-08-05 05:41:19,321 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=534303, prompt_len=1118
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["出院记录", "姓名：", "性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：", "床号：", "出院时情况：患者气短明显缓解，偶有咳嗽，无明显咳痰，精神可。查体：口唇暗紫", "色，咽部无充血，扁桃体无肿大；双肺未闻及干湿性啰音，心律齐，未闻及心脏瓣膜杂", "音；腹软，无压痛、反跳痛，双下肢无水肿。", "出院诊断：1.支气管哮喘(急性发作期)", "2.低氧血症", "3.肺部阴影(双肺结节性质待查)", "4.多发性肝囊肿", "出院医嘱：1、加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必", "要时吸氧。", "2、院外继续通药物治疗：", "氯雷他定片 10 mg/片 口服 睡前(1月)", "孟鲁司特片 10 mg/片 口服 睡前(1月)", "布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 (3月)", "茶碱缓释片 0.1g/片 口服 2次/日(长期)", "3、3月后复查胸部高分辨CT，总IgE、肺功能+扩张+弥散", "4、2周后呼吸科门诊复诊，不适随诊。", "签名：", "记录日期：2024年03月18日11时56分", "第2页"]

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
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord API raw response (len=1451):
[
	{"text": "出院记录", "bbox": [458, 129, 553, 147]},
	{"text": "姓名：", "bbox": [153, 151, 193, 164]},
	{"text": "性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：", "bbox": [270, 151, 703, 164]},
	{"text": "床号：", "bbox": [810, 151, 845, 164]},
	{"text": "出院时情况：患者气短明显缓解，偶有咳嗽，无明显咳痰，精神可。查体：口唇暗紫", "bbox": [154, 184, 855, 199]},
	{"text": "色，咽部无充血，扁桃体无肿大；双肺未闻及干湿性啰音，心律齐，未闻及心脏瓣膜杂", "bbox": [153, 207, 855, 222]},
	{"text": "音；腹软，无压痛、反跳痛，双下肢无水肿。", "bbox": [153, 231, 504, 246]},
	{"text": "出院诊断：1.支气管哮喘(急性发作期)", "bbox": [154, 254, 458, 269]},
	{"text": "2.低氧血症", "bbox": [243, 278, 335, 292]},
	{"text": "3.肺部阴影(双肺结节性质待查)", "bbox": [243, 301, 505, 316]},
	{"text": "4.多发性肝囊肿", "bbox": [243, 325, 370, 339]},
	{"text": "出院医嘱：1、加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必", "bbox": [153, 348, 855, 363]},
	{"text": "要时吸氧。", "bbox": [243, 371, 324, 385]},
	{"text": "2、院外继续通药物治疗：", "bbox": [242, 395, 440, 409]},
	{"text": "氯雷他定片 10 mg/片 口服 睡前(1月)", "bbox": [242, 418, 730, 433]},
	{"text": "孟鲁司特片 10 mg/片 口服 睡前(1月)", "bbox": [242, 441, 730, 456]},
	{"text": "布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 (3月)", "bbox": [242, 465, 738, 480]},
	{"text": "茶碱缓释片 0.1g/片 口服 2次/日(长期)", "bbox": [242, 488, 755, 503]},
	{"text": "3、3月后复查胸部高分辨CT，总IgE、肺功能+扩张+弥散", "bbox": [242, 511, 682, 526]},
	{"text": "4、2周后呼吸科门诊复诊，不适随诊。", "bbox": [242, 534, 538, 549]},
	{"text": "签名：", "bbox": [534, 557, 602, 572]},
	{"text": "记录日期：2024年03月18日11时56分", "bbox": [534, 582, 821, 597]},
	{"text": "第2页", "bbox": [477, 848, 517, 861]}
]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=11.4s
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[458, 129, 553, 147]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[153, 151, 193, 164]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：, bbox=[270, 151, 703, 164]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[3]: text=床号：, bbox=[810, 151, 845, 164]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[4]: text=出院时情况：患者气短明显缓解，偶有咳嗽，无明显咳痰，精神可。查体：口唇暗紫, bbox=[154, 184, 855, 199]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[5]: text=色，咽部无充血，扁桃体无肿大；双肺未闻及干湿性啰音，心律齐，未闻及心脏瓣膜杂, bbox=[153, 207, 855, 222]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[6]: text=音；腹软，无压痛、反跳痛，双下肢无水肿。, bbox=[153, 231, 504, 246]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[7]: text=出院诊断：1.支气管哮喘(急性发作期), bbox=[154, 254, 458, 269]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[8]: text=2.低氧血症, bbox=[243, 278, 335, 292]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[9]: text=3.肺部阴影(双肺结节性质待查), bbox=[243, 301, 505, 316]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[10]: text=4.多发性肝囊肿, bbox=[243, 325, 370, 339]
2026-08-05 05:41:30,747 INFO     29 [qwen-vl-text] coord item[11]: text=出院医嘱：1、加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必, bbox=[153, 348, 855, 363]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[12]: text=要时吸氧。, bbox=[243, 371, 324, 385]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[13]: text=2、院外继续通药物治疗：, bbox=[242, 395, 440, 409]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[14]: text=氯雷他定片 10 mg/片 口服 睡前(1月), bbox=[242, 418, 730, 433]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[15]: text=孟鲁司特片 10 mg/片 口服 睡前(1月), bbox=[242, 441, 730, 456]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[16]: text=布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 (3月), bbox=[242, 465, 738, 480]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[17]: text=茶碱缓释片 0.1g/片 口服 2次/日(长期), bbox=[242, 488, 755, 503]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[18]: text=3、3月后复查胸部高分辨CT，总IgE、肺功能+扩张+弥散, bbox=[242, 511, 682, 526]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[19]: text=4、2周后呼吸科门诊复诊，不适随诊。, bbox=[242, 534, 538, 549]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[20]: text=签名：, bbox=[534, 557, 602, 572]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[21]: text=记录日期：2024年03月18日11时56分, bbox=[534, 582, 821, 597]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] coord item[22]: text=第2页, bbox=[477, 848, 517, 861]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] page=2 — 23/23 coords, api_time=11.4s
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] new_positions (61):
[[1, 276.675, 330.82, 104.408, 119.564], [1, 100.55499999999999, 112.455, 123.774, 133.878], [1, 174.33499999999998, 420.07, 123.774, 133.878], [1, 473.025, 503.965, 123.774, 133.878], [1, 100.55499999999999, 120.785, 151.56, 161.664], [1, 211.82, 248.70999999999998, 151.56, 161.664], [1, 301.07, 347.47999999999996, 151.56, 161.664], [1, 402.815, 451.01, 151.56, 161.664], [1, 102.935, 250.49499999999998, 173.452, 184.398], [1, 265.965, 412.93, 173.452, 184.398], [1, 422.45, 492.065, 173.452, 184.398], [1, 100.55499999999999, 283.815, 196.186, 207.132], [1, 100.55499999999999, 277.27, 215.552, 227.34], [1, 152.32, 205.87, 235.76, 246.706], [1, 100.55499999999999, 250.49499999999998, 255.126, 266.072], [1, 100.55499999999999, 503.965, 275.334, 286.28], [1, 152.32, 510.51, 294.7, 306.488], [1, 152.32, 409.35999999999996, 314.066, 325.854], [1, 100.55499999999999, 510.51, 333.432, 345.21999999999997], [1, 152.32, 409.35999999999996, 352.798, 364.586], [1, 100.55499999999999, 510.51, 373.006, 383.952], [1, 152.32, 510.51, 392.372, 403.318], [1, 152.32, 220.74499999999998, 411.738, 422.68399999999997], [1, 100.55499999999999, 242.165, 431.104, 442.892], [1, 100.55499999999999, 418.28499999999997, 450.46999999999997, 462.258], [1, 100.55499999999999, 467.66999999999996, 469.83599999999996, 481.62399999999997], [1, 100.55499999999999, 345.09999999999997, 489.202, 500.99], [1, 100.55499999999999, 381.395, 509.40999999999997, 520.356], [1, 100.55499999999999, 510.51, 528.776, 540.564], [1, 152.32, 209.44, 548.984, 559.93], [1, 100.55499999999999, 393.29499999999996, 568.35, 579.2959999999999], [1, 100.55499999999999, 509.32, 587.716, 599.504], [1, 152.32, 509.32, 607.082, 618.87], [1, 152.32, 498.015, 626.448, 638.236], [1, 100.55499999999999, 509.32, 645.814, 657.602], [1, 158.26999999999998, 313.565, 665.18, 676.968], [1, 100.55499999999999, 365.33, 685.3879999999999, 696.334], [1, 290.955, 314.15999999999997, 709.8059999999999, 719.91], [2, 272.51, 329.03499999999997, 108.618, 123.774], [2, 91.035, 114.835, 127.142, 138.088], [2, 160.65, 418.28499999999997, 127.142, 138.088], [2, 481.95, 502.775, 127.142, 138.088], [2, 91.63, 508.72499999999997, 154.928, 167.558], [2, 91.035, 508.72499999999997, 174.29399999999998, 186.924], [2, 91.035, 299.88, 194.50199999999998, 207.132], [2, 91.63, 272.51, 213.868, 226.498], [2, 144.58499999999998, 199.325, 234.076, 245.864], [2, 144.58499999999998, 300.47499999999997, 253.44199999999998, 266.072], [2, 144.58499999999998, 220.14999999999998, 273.65, 285.438], [2, 91.035, 508.72499999999997, 293.01599999999996, 305.646], [2, 144.58499999999998, 192.78, 312.382, 324.17], [2, 143.98999999999998, 261.8, 332.59, 344.378], [2, 143.98999999999998, 434.34999999999997, 351.95599999999996, 364.586], [2, 143.98999999999998, 434.34999999999997, 371.322, 383.952], [2, 143.98999999999998, 439.10999999999996, 391.53, 404.15999999999997], [2, 143.98999999999998, 449.22499999999997, 410.89599999999996, 423.526], [2, 143.98999999999998, 405.78999999999996, 430.262, 442.892], [2, 143.98999999999998, 320.11, 449.628, 462.258], [2, 317.72999999999996, 358.19, 468.99399999999997, 481.62399999999997], [2, 317.72999999999996, 488.495, 490.044, 502.674], [2, 283.815, 307.615, 714.016, 724.962]]
2026-08-05 05:41:30,748 INFO     29 [qwen-vl-text] ═══ DONE ═══ 61 positions, pages=2, time=43.1s
2026-08-05 05:41:30,756 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 05:41:30,756 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:41:30,756 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 05:41:30,756 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:41:30.756+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 19, "failed": 0, "current": {"a0ac621a908f11f1a3da71efcdd7cc1f": {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:41:30,762 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:41:30,763 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 05:41:31,687 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:41:31,698 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 05:41:31,698 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:41:31,698 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 05:41:31,705 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:41:31,705 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 05:41:31,705 INFO     29 [qwen-vl-text] positions(22): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:41:31,705 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [22]
2026-08-05 05:41:31,860 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:41:31,862 INFO     29 [qwen-vl-text] LLM extraction start, text_len=308
2026-08-05 05:41:31,862 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:41:31,862 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 77, \"bbox_end\": 98, \"encounter_dates\": [\"2024-03-15\"], \"department\": \"呼吸与危重症二组\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CT检查报告单\n检查\n病人姓名\n性别：女\n年龄：66岁\n申请科室：呼吸与危重症二组\n住院号：\n门诊号：\n造影剂：\n检查部位：胸部高分辨平扫+矢冠状面重建\n影像学表现：\n双侧胸廓不对称，气管居中。双肺纹理清晰，走向自然，右肺下叶前基底段、\n左肺下叶外基底段、左肺下叶背段均可见结节影，较大者直径约0.4cm，所见各支\n气管腔通畅，纵隔内可肿大淋巴结，胸膜无增厚，胸腔内无积液。所扫肝内可见\n多个类圆形低密度影，密度均匀，边界尚清。\n初步诊断及建议：\n双肺实性微结节，建议随诊\n肝内低密度灶，考虑囊肿\n录入者：\n审核医\n报告日期：2024.03.15 18:52:06\n注：本报告仅供临床医师参考，本科室医师签字后有效。",
    "role": "user"
  }
]
[92m05:41:31 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:41:31,863 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:41:35,138 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:41:35,138 INFO     29 [qwen-vl-text] LLM output (len=494):
{
  "exam_date": "2024-03-15",
  "report_date": "2024-03-15",
  "exam_name": "胸部高分辨平扫+矢冠状面重建",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "呼吸与危重症二组",
  "bed_number": null,
  "findings": "影像学表现：\n双侧胸廓不对称，气管居中。双肺纹理清晰，走向自然，右肺下叶前基底段、左肺下叶外基底段、左肺下叶背段均可见结节影，较大者直径约0.4cm，所见各支气管腔通畅，纵隔内可肿大淋巴结，胸膜无增厚，胸腔内无积液。所扫肝内可见多个类圆形低密度影，密度均匀，边界尚清。",
  "conclusion": "初步诊断及建议：\n双肺实性微结节，建议随诊\n肝内低密度灶，考虑囊肿",
  "physician": null,
  "reviewer": null
}
2026-08-05 05:41:35,139 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=491451, prompt_len=987
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["CT检查报告单", "检查", "病人姓名", "性别：女", "年龄：66岁", "申请科室：呼吸与危重症二组", "住院号：", "门诊号：", "造影剂：", "检查部位：胸部高分辨平扫+矢冠状面重建", "影像学表现：", "双侧胸廓不对称，气管居中。双肺纹理清晰，走向自然，右肺下叶前基底段、", "左肺下叶外基底段、左肺下叶背段均可见结节影，较大者直径约0.4cm，所见各支", "气管腔通畅，纵隔内可肿大淋巴结，胸膜无增厚，胸腔内无积液。所扫肝内可见", "多个类圆形低密度影，密度均匀，边界尚清。", "初步诊断及建议：", "双肺实性微结节，建议随诊", "肝内低密度灶，考虑囊肿", "录入者：", "审核医", "报告日期：2024.03.15 18:52:06", "注：本报告仅供临床医师参考，本科室医师签字后有效。"]

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
2026-08-05 05:41:43,537 INFO     29 [qwen-vl-text] coord API raw response (len=1279):
[
	{"text": "CT检查报告单", "bbox": [445, 125, 632, 148]},
	{"text": "检查", "bbox": [134, 158, 183, 172]},
	{"text": "病人姓名", "bbox": [134, 185, 200, 199]},
	{"text": "性别：女", "bbox": [325, 185, 406, 199]},
	{"text": "年龄：66岁", "bbox": [491, 185, 595, 199]},
	{"text": "申请科室：呼吸与危重症二组", "bbox": [641, 185, 860, 199]},
	{"text": "住院号：", "bbox": [134, 205, 237, 219]},
	{"text": "门诊号：", "bbox": [325, 205, 384, 219]},
	{"text": "造影剂：", "bbox": [491, 205, 550, 219]},
	{"text": "检查部位：胸部高分辨平扫+矢冠状面重建", "bbox": [134, 227, 443, 241]},
	{"text": "影像学表现：", "bbox": [131, 272, 238, 288]},
	{"text": "双侧胸廓不对称，气管居中。双肺纹理清晰，走向自然，右肺下叶前基底段、", "bbox": [170, 296, 836, 311]},
	{"text": "左肺下叶外基底段、左肺下叶背段均可见结节影，较大者直径约0.4cm，所见各支", "bbox": [141, 315, 848, 331]},
	{"text": "气管腔通畅，纵隔内可肿大淋巴结，胸膜无增厚，胸腔内无积液。所扫肝内可见", "bbox": [141, 334, 837, 350]},
	{"text": "多个类圆形低密度影，密度均匀，边界尚清。", "bbox": [141, 353, 525, 369]},
	{"text": "初步诊断及建议：", "bbox": [131, 631, 275, 647]},
	{"text": "双肺实性微结节，建议随诊", "bbox": [141, 654, 376, 669]},
	{"text": "肝内低密度灶，考虑囊肿", "bbox": [141, 673, 356, 688]},
	{"text": "录入者：", "bbox": [148, 803, 206, 817]},
	{"text": "审核医", "bbox": [363, 803, 422, 817]},
	{"text": "报告日期：2024.03.15 18:52:06", "bbox": [609, 803, 824, 817]},
	{"text": "注：本报告仅供临床医师参考，本科室医师签字后有效。", "bbox": [125, 823, 470, 836]}
]
2026-08-05 05:41:43,537 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=8.4s
2026-08-05 05:41:43,537 INFO     29 [qwen-vl-text] coord item[0]: text=CT检查报告单, bbox=[445, 125, 632, 148]
2026-08-05 05:41:43,537 INFO     29 [qwen-vl-text] coord item[1]: text=检查, bbox=[134, 158, 183, 172]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[2]: text=病人姓名, bbox=[134, 185, 200, 199]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[325, 185, 406, 199]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：66岁, bbox=[491, 185, 595, 199]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[5]: text=申请科室：呼吸与危重症二组, bbox=[641, 185, 860, 199]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[6]: text=住院号：, bbox=[134, 205, 237, 219]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[7]: text=门诊号：, bbox=[325, 205, 384, 219]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[8]: text=造影剂：, bbox=[491, 205, 550, 219]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[9]: text=检查部位：胸部高分辨平扫+矢冠状面重建, bbox=[134, 227, 443, 241]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[10]: text=影像学表现：, bbox=[131, 272, 238, 288]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[11]: text=双侧胸廓不对称，气管居中。双肺纹理清晰，走向自然，右肺下叶前基底段、, bbox=[170, 296, 836, 311]
2026-08-05 05:41:43,538 INFO     29 [qwen-vl-text] coord item[12]: text=左肺下叶外基底段、左肺下叶背段均可见结节影，较大者直径约0.4cm，所见各支, bbox=[141, 315, 848, 331]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[13]: text=气管腔通畅，纵隔内可肿大淋巴结，胸膜无增厚，胸腔内无积液。所扫肝内可见, bbox=[141, 334, 837, 350]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[14]: text=多个类圆形低密度影，密度均匀，边界尚清。, bbox=[141, 353, 525, 369]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断及建议：, bbox=[131, 631, 275, 647]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[16]: text=双肺实性微结节，建议随诊, bbox=[141, 654, 376, 669]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[17]: text=肝内低密度灶，考虑囊肿, bbox=[141, 673, 356, 688]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[18]: text=录入者：, bbox=[148, 803, 206, 817]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[19]: text=审核医, bbox=[363, 803, 422, 817]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[20]: text=报告日期：2024.03.15 18:52:06, bbox=[609, 803, 824, 817]
2026-08-05 05:41:43,539 INFO     29 [qwen-vl-text] coord item[21]: text=注：本报告仅供临床医师参考，本科室医师签字后有效。, bbox=[125, 823, 470, 836]
2026-08-05 05:41:43,540 INFO     29 [qwen-vl-text] page=3 — 22/22 coords, api_time=8.4s
2026-08-05 05:41:43,540 INFO     29 [qwen-vl-text] new_positions (22):
[[3, 264.775, 376.03999999999996, 105.25, 124.616], [3, 79.72999999999999, 108.88499999999999, 133.036, 144.82399999999998], [3, 79.72999999999999, 119.0, 155.76999999999998, 167.558], [3, 193.375, 241.57, 155.76999999999998, 167.558], [3, 292.145, 354.025, 155.76999999999998, 167.558], [3, 381.395, 511.7, 155.76999999999998, 167.558], [3, 79.72999999999999, 141.015, 172.60999999999999, 184.398], [3, 193.375, 228.48, 172.60999999999999, 184.398], [3, 292.145, 327.25, 172.60999999999999, 184.398], [3, 79.72999999999999, 263.585, 191.134, 202.922], [3, 77.945, 141.60999999999999, 229.024, 242.49599999999998], [3, 101.14999999999999, 497.41999999999996, 249.232, 261.86199999999997], [3, 83.895, 504.56, 265.23, 278.702], [3, 83.895, 498.015, 281.228, 294.7], [3, 83.895, 312.375, 297.226, 310.698], [3, 77.945, 163.625, 531.302, 544.774], [3, 83.895, 223.72, 550.668, 563.298], [3, 83.895, 211.82, 566.6659999999999, 579.2959999999999], [3, 88.06, 122.57, 676.126, 687.914], [3, 215.98499999999999, 251.08999999999997, 676.126, 687.914], [3, 362.35499999999996, 490.28, 676.126, 687.914], [3, 74.375, 279.65, 692.966, 703.9119999999999]]
2026-08-05 05:41:43,540 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=11.8s
2026-08-05 05:41:43,548 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 05:41:43,549 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "399 items", "markdown": "", "text": "", "name": "YJXI 68 哮喘 山西(1).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Discharge\": 1, \"chunks_Examination\": 1, \"chunks_Prescription\": 1, \"chunks_Medication\": 5, \"chunks_LabExam\": 1}"}
2026-08-05 05:41:43,549 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 05:41:43,550 INFO     29 [ChunkMerger] Merged 10 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 5, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 2 noise chunks)
2026-08-05 05:41:43,881 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 05:41:43,881 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "10 items, types={'LabReport': 1, 'OutpatientRecord': 1, 'MedicationRecord': 5, 'PrescriptionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1}", "name": "YJXI 68 哮喘 山西(1).pdf"}
2026-08-05 05:41:43,881 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 05:41:43,989 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785908199267, 'update_date': datetime.datetime(2026, 8, 5, 5, 36, 39), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 219870, 'status': '1'}
2026-08-05 05:41:44,230 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞计数  WBC  4.06  *10~9/L  3.50~9.50  False    红细胞计数  RBC  4.49  *10~12/L  3.80~5.10  False    血红蛋白  HGB  131  g/L  115~150  False    红细胞压积  HCT  0.405  L/L  0.350~0.450  False    红细胞平均体积  MCV  90.2  fL  82.0~100.0  False    红细胞平均血红蛋白含量  MCH  29.2  pg  27.0~34.0  False    红细胞平均血红蛋白浓度  MCHC  323  g/L  316~354  False    红细胞体积分布宽度SD  RDW-SD  40.60  fL  41.20~53.60  True    红细胞体积分布宽度CV  RDW-CV  12.20  %  12.20~14.80  False    血小板  PLT  280  *10~9/L  125~350  False    血小板压积  PCT  0.24  %  0.19~0.39  False    平均血小板体积  MPV  8.70  fL  9.20~12.00  True    大血小板比率  P-LCR  15.30  %  19.70~42.40  True    血小板体积分布宽度  PDW  8.90  fL  9.60~15.20  True    淋巴细胞绝对值  LYM#  1.42  *10~9/L  1.10~3.20  False    单核细胞绝对值  MON#  0.18  *10~9/L  0.10~0.60  False    中性粒细胞绝对值  NEU#  2.42  *10~9/L  1.80~6.30  False    嗜酸性粒细胞绝对值  EOS#  0.03  *10~9/L  0.02~0.52  False    嗜碱性粒细胞绝对值  BASO#  0.01  *10~9/L  0.00~0.06  False    淋巴细胞百分比  LYM%  35.00  %  20.00~50.00  False    单核细胞百分比  MON%  4.40  %  3.00~10.00  False    中性粒细胞百分比  NEU%  59.70  %  40.00~75.00  False    嗜酸性粒细胞百分比  EOS%  0.70  %  0.40~8.00  False    嗜碱性粒细胞百分比  BASO%  0.20  %  0.00~1.00  False    有核红细胞绝对值  NRBC#  0.0  *10~12/L  None  False    有核红细胞百分比  NRBC%  0.0  /100WBC  None  False   
---
门诊电子病历（初诊）
姓名：
性别：女性
年龄：68岁
科室：呼吸与危重症医学门诊科
就诊时间：2026年01月19日16时48分
主诉：咳嗽、气短40余年，近一周加重
现病史：咳嗽、气短40余年，近一周加重，曾于当地医院诊断支气管哮喘，2024年3月因哮喘急性发作在
山大二院住院治疗，规律使用布地格福吸入气雾剂，加重1周
既往史：既往不详，未确认糖尿病病史，未确认高血压病史。
过敏史：未确认药物过敏史，未确认食物过敏史。
家族史：不详。
门诊诊断：支气管哮喘(急性发作期)
处理意见：醋酸泼尼松片、5mg*100片、15mg、口服、QD（每日一次）、1瓶；
医师签
第1页（共1页）
---
[G532]  心草招县西人乡连锁
店
交易日期：2025-10-31 11:43:49
销售单号：1325103100021472
收银员：
积分：543
品名
规格
150027(兴)布地格福吸入
气雾剂 倍择瑞_160ug:7.2u
单价:233.00
实价:233.00
数量:2.00
金额:466.00
批号：6103904C00
处方药
国码：XRO3ALB240L028010179096
AstraZeneca AB
84471890087171843044
84471890087171828685
2、809245_一心堂卫生纸(原生
木浆(纤维))_1000g(4层*1
单价:11.80
实价:0.01
数量:1.00
金额:0.01
批号：20240825
国码：Q01000000
应收金额:477.8 优惠:11.8
实收金额:466.01找零:0.00
其中:收钱吧微信：
466.01
*药品除质量问题，概不退换
*服务不满意，
*地址-电话·
---
山西省医疗门诊收费票据（电子）
山西省
财政部监制
票据号码：0040081955
校验码：itykbi
开票日期：2025-09-01
项目名称
数量/单位
金额（元）
备注
项目名称
数量/单位
金额（元）
备注
西药费
1
233.00
G布地格福吸入气雾剂【每瓶12
1.00
盒
233.00 限慢性阻
0揿】
塞性肺疾
病。
金额合计（大写）贰佰叁拾叁元整
(小写)233.00
业务流水号：07QIKH59659470P20250 门诊号：
就诊日期：20250901
901172144801
（医
型：综合医院
医保类型：国家医保
医保码
医保统
支付：154.95
其他支付：0.00
个人账户支付：0.00
个人现金支付：78.05
付：0.0
z-方便
费专用章
复核人：程小磊
收款
---
山西省医疗门诊收费票据（电子）
山西省
财政部监制
票据代码：
交款人话一社会信用代码：
交款人
票据号码：0039960248
校验码：isI3ej
开票日期：2025-07-08
项目名称
数量/单位
金额（元）
备注
项目名称
数量/单位
金额（元）
备注
西药费
1
466.00
G布地格福吸入气雾剂【每瓶12
2.00
盒
466.00 限慢性阻
0揿】
塞性肺疾
病。
金额合计（大写）肆佰陆拾陆元整
(小写)466.00
业务流水号：B7C8A658327630P20250 门诊号：
就诊日期：20250708
708113600815
类型：综合医院
医保类型：国家医保
医保编
医保.
付：309.89
其他支付：0.00
个人账户支付：0.00
个人现金支付：156.11
信
自付：
息
Z-方便
靖号
个人自费：156.11
费专用
复核人：程小蕊
收款人：王丽
---
山西省医疗门诊收费票据（电子）
山西省
财政部监制
票据代码:1/
交款人统一社会信用代码:
交款
票据号码:0155140741
校验码: ci4u59
开票日期:2026-02-24
项目名称
数量/单位
金额（元）
备注
项目名称
数量/单位
金额（元）
备注
西药费
1.00
233.00
G布地格福吸入气雾剂【每瓶12
1.00
盒
233.00 限慢性阻
0揿】
塞性肺疾
病。
金额合计（大写）贰佰叁拾叁元整
(小写)233.00
业务流水号:2
门诊号:
就诊日期:20260224
2
类型:综合医院
医保类型:国家医保
医保编号
0548 性别:女
医保现
付:154.95
其他支付:0.00
个人账户支付:0.00
个人现金支付:78.05
信
自付:
总
Z-方便
赵泽斌号
个人自费:78.05
费专用章
复核人:程小蕊
收款人:刘灵芝
---
山西省医疗门诊收费票据（电子）
山西省
财政部监制
票据代码:14060124
交款人统一社会信用代
交款
票据号码:0155032568
校验码: pc2vph
开票日期:2026-01-06
项目名称
数量/单位
金额（元）
备注
项目名称
数量/单位
金额（元）
备注
西药费
1.00
466.00
G布地格福吸入气雾剂【每瓶12
2.00
盒
466.00 限慢性阻
0揿】
塞性肺疾
病。
金额合计（大写）肆佰陆拾陆元整
(小写)466.00
业务流水号
门
就诊日期:20260106
型:综合医院
医保类型:国家医保
医保编号:
48 性别:女
医
其他支付:0.00
个人账户支付:0.00
个人现金支付:156.11
信
t:309.89
个人自费:156.11
息
自付:
Z-方便门诊
必泽斌号
费专用章
复核人:程小蕊
收款人:段国丽
---
【处方】导引单
ID:
姓名:
年龄：68岁
性别：女
费别：普通患者
诊断：支气管哮喘(急性发作期)
开单科室：呼吸与危重症医学科
开单时间：2026-01-20 17:33:34
取药排
药品名称
规格
数量
1.醋酸泼尼松片
5mg*100片
1瓶
15.0mg
口服
每日一次
微信/支付宝
扫码支付
金额：4.8元
执行科室：门诊药房
地点：门诊大厅一层西侧
医生
处方当日有效，补打导引单不可作为取药凭证
【患者留存】
ID:
姓名:
年龄：68岁
性别：女
药品名称
规格
数量
1.醋酸泼尼松片
5mg*100片
1瓶
15.0mg
口服
每日一次
---
出院记录
姓名：
性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：
住院号：
姓名
性别：女
年龄：66岁
职业：农民
入院日期：2024年03月15日10时
出院日期：2024年03月18日11时
住院天数：3天
入院时情况：发作性喘息10年，加重2月。
入院诊断：1.支气管哮喘(急性发作期)
2.低氧血症
诊疗经过：完善相关化验及检查：
血气分析：吸氧浓度21.0%，酸碱度7.414，二氧化碳分压35.3mmHg，氧分压67.9mmHg↓，
实际碱剩余-1.4mmol/L，血浆碳酸氢盐浓度22.2mmol/L，乳酸浓度0.6mmol/
L，氧合指数323mmHg↓，肺泡动脉氧分压差27.7mmHg↑。
血常规：白细胞计数4.06*10^9/L，红细胞计数4.49*10^12/L，血红蛋白131g/L，血小板
280*10^9/L。红细胞沉降率5mm/H。C反应蛋白2.43mg/L。
肝+肾+离子：血清丙氨酸氨基转移酶10.80U/L，血清天门冬氨酸氨基转移酶15.60U/L，尿
素4.40mmol/L，肌酐51.00umol/L，钾3.79mmol/L，钠143.00mmol/L，氯
109.00mmol/L。
免疫球蛋白：E128.00IU/mL↑。
呼吸道病原体抗体：阴性；新型冠状病毒核酸：阴性；痰培养：阴性；
尿常规：尿常规检验报告尿隐血-，尿白细胞3+，尿蛋白-，白细胞134个/uL↑。
肿瘤标志物、心肺四项、凝血、便常规未见明显异常。
腹部彩超：肝囊肿（多发）胆、胰、脾、双肾未见明显异常；
心脏彩超：EF：68% 三尖瓣口少量返流 主动脉瓣口少量返流 左室舒张功能减低 左室收
缩功能正常；
胸部CT：双肺实性微结节，建议随诊 肝内低密度灶，考虑囊肿。
肺功能：激发前：FEV1/FVC 86.86%，FEV1 96% FVC 90.2% 通气功能大致正常，吸入乙
酰甲胆碱 32mg/ml（第5管）激发后FEV1/FVC 72.8%，FEV1下降20.82%，激发
试验（+），DLCO 53.3% 肺弥散功能显著减退 RV/TLC 65.72%,残总比升高。
呼出气一氧化氮测定：FENO50 25ppb 混合型气道炎症 FENO200 18ppb 小气道炎症 CaNO
14.7ppb 肺泡炎症。FENO10 233。
2.予以抗过敏、扩张气道、促进排痰、抗感染等对症治疗。
第1页
出院记录
姓名：
性别：女 年龄：66岁 科室：呼吸与危重症二组病区 床号：
床号：
出院时情况：患者气短明显缓解，偶有咳嗽，无明显咳痰，精神可。查体：口唇暗紫
色，咽部无充血，扁桃体无肿大；双肺未闻及干湿性啰音，心律齐，未闻及心脏瓣膜杂
音；腹软，无压痛、反跳痛，双下肢无水肿。
出院诊断：1.支气管哮喘(急性发作期)
2.低氧血症
3.肺部阴影(双肺结节性质待查)
4.多发性肝囊肿
出院医嘱：1、加强营养，注意休息，避免劳累及受凉感冒，适当锻炼，自备制氧机，必
要时吸氧。
2、院外继续通药物治疗：
氯雷他定片 10 mg/片 口服 睡前(1月)
孟鲁司特片 10 mg/片 口服 睡前(1月)
布地格福吸入气雾剂 0.32 mg/吸 吸入 睡前 (3月)
茶碱缓释片 0.1g/片 口服 2次/日(长期)
3、3月后复查胸部高分辨CT，总IgE、肺功能+扩张+弥散
4、2周后呼吸科门诊复诊，不适随诊。
签名：
记录日期：2024年03月18日11时56分
第2页
---
CT检查报告单
检查
病人姓名
性别：女
年龄：66岁
申请科室：呼吸与危重症二组
住院号：
门诊号：
造影剂：
检查部位：胸部高分辨平扫+矢冠状面重建
影像学表现：
双侧胸廓不对称，气管居中。双肺纹理清晰，走向自然，右肺下叶前基底段、
左肺下叶外基底段、左肺下叶背段均可见结节影，较大者直径约0.4cm，所见各支
气管腔通畅，纵隔内可肿大淋巴结，胸膜无增厚，胸腔内无积液。所扫肝内可见
多个类圆形低密度影，密度均匀，边界尚清。
初步诊断及建议：
双肺实性微结节，建议随诊
肝内低密度灶，考虑囊肿
录入者：
审核医
报告日期：2024.03.15 18:52:06
注：本报告仅供临床医师参考，本科室医师签字后有效。
2026-08-05 05:41:44,825 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 05:41:44,825 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "10 items, types={'LabReport': 1, 'OutpatientRecord': 1, 'MedicationRecord': 5, 'PrescriptionRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 1}", "name": "YJXI 68 哮喘 山西(1).pdf", "embedding_token_consumption": 4407}
2026-08-05 05:41:44,825 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 05:41:44,969 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 05:41:44,969 INFO     29 [Trace] task=a0ac621a | doc=YJXI 68 哮喘 山西(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":10,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 05:41:44,974 INFO     29 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(11, 86, 161, 188, 201) row[-1]=(11, 489, 586, 444, 457)
2026-08-05 05:41:44,974 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,974 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,974 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,974 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,975 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,975 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,975 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,975 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,975 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:41:44,978 INFO     29 set_progress(a0ac621a908f11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 05:41:44 [DOC Engine]:
Start to index...
2026-08-05 05:41:45,003 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.019s]
2026-08-05 05:41:45,007 INFO     29 set_progress(a0ac621a908f11f1a3da71efcdd7cc1f), progress: 0.81, progress_msg: 
2026-08-05 05:41:45,027 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-05 05:41:45,043 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-05 05:41:45,052 INFO     29 set_progress(a0ac621a908f11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 05:41:45 Indexing done (0.07s). Task done (280.30s)
2026-08-05 05:41:45,056 INFO     29 [Done], chunks(10), token(4407), elapsed:280.30
2026-08-05 05:41:45,181 INFO     29 handle_task done for task {"id": "a0ac621a908f11f1a3da71efcdd7cc1f", "doc_id": "a0687fe6908f11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "type": "pdf", "location": "YJXI 68 \u54ee\u5598 \u5c71\u897f(1).pdf", "size": 7962206, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785908197559, "task_type": "dataflow", "root_trace_id": "8319cee6193e4da3880bde9a6f044605", "root_traceparent": "00-8319cee6193e4da3880bde9a6f044605-7ab441055f59bc6e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
