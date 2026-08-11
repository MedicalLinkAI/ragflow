# 基准结果：Wlge-肝癌-男-57岁.pdf

## 基本信息

- 文件：`Wlge-肝癌-男-57岁.pdf`
- 大小：7702.0 KB
- PDF 总页数：16
- doc_id：`3d4248b094d211f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T23:43:30  完成时间：2026-08-10T23:50:30  耗时：420.3s
- progress_msg：`15:50:27 Indexing done (0.11s). Task done (389.75s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | b18d263c | 1 | 1-1 | 族:汉族 婚姻:已婚 出生地:江西省南昌市湾里区 业:其他 现住址:江西省南昌市 |
| 2 | dfccc477 | 1 | 2-2 | 工作单位或地址:湾里区 就诊科室:红角洲肝胆外科门诊 就诊时间:2025年12月 |
| 3 | af9302e6 | 1 | 3-3 | 就诊科室:红角洲肝胆外科门诊 就诊时间:2026年03月05日 09:51 药物 |
| 4 | f42d2238 | 1 | 4-4 | 职业： 出生日期：1968年01月06日 工作单位或地址：湾里区 就诊科室：红角 |
| 5 | fec5bfeb | 2 | 5-6 | 入院日期：2025年08月02日 出院日期：2025年08月06日 住院天数：4 |
| 6 | ff2d9746 | 1 | 7-7 | 肝区介入术后复查所见。 入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期 |
| 7 | c7b7fda9 | 2 | 7-8 | 第1页 入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结 |
| 8 | 0f71d6c1 | 3 | 8-10 | 第1页 入院日期：2025年03月18日 出院日期：2025年03月24日 住院 |
| 9 | 2f2ef597 | 1 | 10-10 | 向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗 检查项目:上腹部薄层CT平扫+增 |
| 10 | f6a1b440 | 2 | 10-11 | 红角洲影像科咨询电话:0791-86257676( 临床诊断:1.肝细胞癌(BC |
| 11 | 5c443294 | 2 | 11-12 | 第1页 共1页 临床诊断:1.肝癌介入治疗,2.原发性肝癌 检查项目:胸部CT平 |
| 12 | b860533b | 1 | 13-13 | 临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期), |
| 13 | 7da9c2a1 | 1 | 14-14 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 14 | f9262ba2 | 1 | 15-15 | <table><tr><td>总蛋白</td><td>TP</td><td>77 |
| 15 | 608a87f1 | 1 | 16-16 | <table><tr><td>甲胎蛋白测定</td><td>AFP</td><t |

- chunks 总数：15
- 各 chunk 页数合计（含跨页重复）：21
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- 覆盖页数：16 / 16；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 3 | 0 | 3 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 4 | 4 | 4 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 4 | 4 | 4 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 3 | 0 | 3 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "OutpatientRecord": 3, "DischargeRecord": 4, "ExaminationReport": 4, "LabReport": 3}`
- ChunkMerger：`{"found": true, "merged": 15, "sources": 9, "stats": {"Extractor:LabExam": 3, "Extractor:Imaging": 1, "Extractor:Clinical": 3, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 4, "Extractor:Admission": 1, "Extractor:ExaminationReport": 4, "Extractor:Progress": 1}, "filtered_noise": 4}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 15:50:26,075 INFO     29 [ChunkMerger] Merged 15 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 15:43:35,487 INFO     29 handle_task begin for task {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 15:43:35,724 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 15:43:35,884 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 15:43:35,902 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:43:35,902 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 15:43:35,902 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 15:43:35,909 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 15:43:35,909 INFO     29 ============================================================
2026-08-10 15:43:35,910 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 15:43:35,910 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 15:43:35,910 INFO     29 ============================================================
2026-08-10 15:43:35,910 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 15:43:35,910 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 15:43:35,911 INFO     29 No torch found.
2026-08-10 15:43:37,301 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=16
2026-08-10 15:43:37,477 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1769209, prompt_len=764
2026-08-10 15:43:39,795 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:43:39,796 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 15:43:39,811 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1769209, prompt_len=401
2026-08-10 15:43:44,938 INFO     29 [qwen-vl-parser] text API response (len=843):
["族:汉族", "婚姻:已婚", "出生地:江西省南昌市湾里区", "业:其他", "现住址:江西省南昌市湾里区", "史陈述者:本人及家属", "与患者关系:其他", "可靠程度:基本可靠", "院时间:2025年09月16日 14:33", "记录时间:2025年09月16日 15:59", "诉:肝癌综合治疗5月余。", "病史:患者5月余前开始因肝癌于我院行综合治疗(介入+靶向+免疫:TACE+仑伐替尼+信迪利单", "), 后于2025年04月27日、2025年06月03日、2025年08月04日行肝动脉栓塞术。现患者为求下一周", "治疗来我院就诊。门诊拟\"肝癌介入治疗\"收入我科。患者自起病来, 饮食睡眠一般, 大小便如常,", "睡无明显变化。", "注史:患者既往身体较差。否认高血压病史。否认糖尿病史。否认冠心病史。否认肾病史。有肝炎", "史慢性乙型病毒性肝炎。否认结核病史。有手术史2025年03月20日、4月27日、06月03日、08月04日", "行肝动脉栓塞术, 肝局部灌注术, 肝动脉造影术, 动脉注射化疗药物, 肝动脉置管术手术。否认外伤史", "否认输血史。否认药物、食物过敏史。", "人史:生于原籍, 久居本地, 否认疫区、疫水接触史。否认毒物、放射性物质接触史。否认烟酒嗜好", "育史:已婚,[结婚年龄]适龄结婚, 配偶体健, 夫妻关系和睦。育有[育子数量]男、[育女数量]", "均体健。", "史:否认家族及遗传病史。", "体格检查", "体温:36.8℃ 脉搏:82次/分 呼吸:20次/分 血压:115/87mmHg", "正常, 营养中等, 表情自然, 无贫血貌, 自主体位, 步入病房, 步态正常, 神志清楚, 查体合作", "身皮肤黏膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣。全身浅表淋巴结未触及", "。头颅无畸形, 双眼睑无水肿, 眼球无突出及震颤, 结膜无苍白、无充血、无出血、无水肿, 巩"]
2026-08-10 15:43:44,940 INFO     29 [qwen-vl-parser] page=1 text: 28 lines (bbox 0-27)
2026-08-10 15:43:44,940 INFO     29 [qwen-vl-parser] page=1 text: 28 sections
2026-08-10 15:43:45,062 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=920899, prompt_len=764
2026-08-10 15:43:46,449 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-12-07"
}
```
2026-08-10 15:43:46,449 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2025-12-07
2026-08-10 15:43:46,465 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=920899, prompt_len=401
2026-08-10 15:43:49,074 INFO     29 [qwen-vl-parser] text API response (len=451):
["工作单位或地址:湾里区", "就诊科室:红角洲肝胆外科门诊", "就诊时间:2025年12月07日 08:46", "药物过敏史:无", "主诉:肝Ca综合治疗后半年返院复查。", "病史:肝Ca综合治疗后半年复查。未诉特殊不适。", "既往史和其他病史:既往半年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。", "体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。", "助检查:暂缺。", "诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿", "靶向治疗;4.恶性肿瘤免疫治疗", "理:1.胸部CT平扫", "上腹部薄层CT平扫+增强扫描", "肝癌三项:肝功能八项+白蛋白;血常规(五分类法);肾功能3项", "碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶", "用法:每次30g即时造影用1天", "CT静脉注药(留置针置管)每次1项", "转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院", "医生签名:"]
2026-08-10 15:43:49,075 INFO     29 [qwen-vl-parser] page=2 text: 19 lines (bbox 28-46)
2026-08-10 15:43:49,075 INFO     29 [qwen-vl-parser] page=2 text: 19 sections
2026-08-10 15:43:49,201 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=958226, prompt_len=764
2026-08-10 15:43:50,541 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-05"
}
```
2026-08-10 15:43:50,542 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2026-03-05
2026-08-10 15:43:50,563 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=958226, prompt_len=401
2026-08-10 15:43:52,654 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:43:52.653+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:43:53,298 INFO     29 [qwen-vl-parser] text API response (len=473):
["就诊科室:红角洲肝胆外科门诊", "就诊时间:2026年03月05日 09:51", "药物过敏史:无", "主诉:肝Ca综合治疗后1年返院评估介入治疗。", "现病史:肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。", "既往史和其他病史:既往1年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。", "查体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。", "辅助检查:暂缺。", "诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿", "瘤靶向治疗;4.恶性肿瘤免疫治疗;5.肝癌介入治疗", "处理:1.胸部CT平扫", "2.上腹部薄层CT平扫+增强扫描", "3.肝癌三项;肝功能八项+白蛋白:血常规(五分类法);肾功能3项", "4.碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶", "用法:每次30g即时造影用1天", "5.CT静脉注药(留置针置管)每次1项", "下转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院", "医生签名:", ""]
2026-08-10 15:43:53,299 INFO     29 [qwen-vl-parser] page=3 text: 18 lines (bbox 47-64)
2026-08-10 15:43:53,299 INFO     29 [qwen-vl-parser] page=3 text: 18 sections
2026-08-10 15:43:53,431 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1062138, prompt_len=764
2026-08-10 15:43:54,818 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:43:54,819 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 15:43:54,836 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1062138, prompt_len=401
2026-08-10 15:43:57,736 INFO     29 [qwen-vl-parser] text API response (len=498):
["职业：", "出生日期：1968年01月06日", "工作单位或地址：湾里区", "就诊科室：红角洲肝胆外科门诊", "就诊时间：2026年03月07日 14:40", "药物过敏史：无", "主诉：肝Ca综合治疗后1年返院评估介入治疗。", "现病史：肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。", "既往史和其他病史：既往1年前诊断肝CA，行介入+抗肿瘤靶向+免疫治疗。", "查体：血压：/mmHg，脉搏：次/分。无特殊阳性体征。", "辅助检查：2026-03-06,上腹部薄层CT平扫+增强扫描检查意见：“肝癌”综合", "治疗后，较2025-12-07日腹部CT：肝右叶肿块较前大小相仿，无明显血供；肿", "块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大，下腔静脉癌栓形", "成；余较前相仿。", "诊断：1.肝细胞癌(BCLC B期，CNLC IIb期)；2.恶性肿瘤靶向治疗；3.恶性肿瘤", "免疫治疗；4.肝癌介入治疗；5.慢性肝炎", "处理：", "下转情况：◎不下转 ○转县级院 ○转社区卫生服务机构/乡镇卫生院", "医生签名：陈天翔", ""]
2026-08-10 15:43:57,736 INFO     29 [qwen-vl-parser] page=4 text: 19 lines (bbox 65-83)
2026-08-10 15:43:57,736 INFO     29 [qwen-vl-parser] page=4 text: 19 sections
2026-08-10 15:43:57,943 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1890541, prompt_len=764
2026-08-10 15:43:59,509 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:43:59,509 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 15:43:59,524 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1890541, prompt_len=401
2026-08-10 15:44:06,325 INFO     29 [qwen-vl-parser] text API response (len=1160):
["入院日期：2025年08月02日", "出院日期：2025年08月06日", "住院天数：4", "入院情况(简要病史\体格检查及主要辅助检查)：患者男性57岁，因肝癌于我院行综合治疗，现为返", "院复诊，无头晕头痛，胸闷气促，恶心呕吐等不适，于我院门诊就诊，门诊拟\"肝癌介入治疗\"收入我", "科。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。查体：神志清楚，", "皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压", "痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨", "中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：暂无。", "入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.肝细胞癌4.恶性肿瘤靶向治疗5.", "恶性肿瘤免疫治疗6.慢性乙型病毒性肝炎。", "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "验检查：主要化验：2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞", "计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l,", "2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶", "原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋", "白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。特殊检查：", "2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层", "194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。", "2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶", "肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆", "管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。有手术指征，排除手术禁忌症后，于2025", "年08月04日行肝动脉栓塞术 肝动脉造影术 腹腔动脉灌注化疗药物，术后给予患者止吐、护胃、止", "痛、补液等对症治疗，今患者术后恢复可，予以免疫治疗后，患者无特殊不适，给予出院。"]
2026-08-10 15:44:06,327 INFO     29 [qwen-vl-parser] page=5 text: 24 lines (bbox 84-107)
2026-08-10 15:44:06,327 INFO     29 [qwen-vl-parser] page=5 text: 24 sections
2026-08-10 15:44:06,528 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1753685, prompt_len=764
2026-08-10 15:44:07,939 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:44:07,940 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 15:44:07,958 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1753685, prompt_len=401
2026-08-10 15:44:16,062 INFO     29 [qwen-vl-parser] text API response (len=1045):
["诊疗经过(包括手术日期和手术名称,植入类医用耗材名称、型号及数量):入院后予以完善相关检", "验检查:主要化验:2025-06-02肝功能五项:γ-谷氨酰基转移酶67.30U/L。2025-06-02血清总蛋白+", "白蛋白测定:白蛋白39.40g/L。2025-06-02超敏C反应蛋白测定+金标法加收(全程,快):超敏C反应", "蛋白测定(全程)30.63mg/L。2025-06-02血常规(五分类法):红细胞计数7.01*10^12/L,血小板计数", "110*10^9/L。2025-06-02肝癌三项:甲胎蛋白测定4679.00ng/ml,甲胎蛋白异质体L3测定370.00ng/ml,", "异常凝血酶原测定>20000.00ng/ml。2025-06-04超敏C反应蛋白测定+金标法加收(全程,快):超敏C", "反应蛋白测定(全程)25.06mg/L。2025-06-04血常规(五分类法):红细胞计数6.19*10^12/L,血红蛋", "白119g/L,血小板计数113*10^9/L,中性粒细胞百分比89.8%。2025-06-04凝血四项:凝血酶原时间", "13.3sec。2025-06-04肝功能八项+白蛋白:天门冬氨酸氨基转移酶60.10U/L。余检验均未见明显异", "常。特殊检查:2025-06-03,上腹部CT平扫+增强扫描检查意见:肝癌综合治疗后,与2025-3-18片比", "较:肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及实验", "室资料;肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。术", "前诊断:原发性肝癌(BCLC B期,CNLC IIb期),有手术指征,排除手术禁忌症后,于2025-06-03行肝", "动脉栓塞术+肝局部灌注术,术后给予患者护胃、止吐、止痛、补液等对症治疗,今患者术后恢复可,", "给予出院。", "出院诊断:1.肝癌介入治疗2.原发性肝癌(BCLC B期,CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "出院情况:患者一般情况良好,生命体征平稳,无畏寒发热,无恶心呕吐,无头痛头晕,无胸闷心", "悸。查体:全身皮肤、巩膜未见黄染,腹平软,无压痛,未及反跳痛和肌紧张,肠鸣音正常,股动脉", "穿刺点无渗血,双下肢动脉搏动良好。", "出院医嘱:", "I"]
2026-08-10 15:44:16,063 INFO     29 [qwen-vl-parser] page=6 text: 22 lines (bbox 108-129)
2026-08-10 15:44:16,063 INFO     29 [qwen-vl-parser] page=6 text: 22 sections
2026-08-10 15:44:16,248 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1605449, prompt_len=764
2026-08-10 15:44:17,600 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:44:17,601 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 15:44:17,610 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1605449, prompt_len=401
2026-08-10 15:44:23,264 INFO     29 [qwen-vl-parser] text API response (len=982):
["肝区介入术后复查所见。", "入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "验检查：主要化验：2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,", "2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白", "44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性", "磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测", "定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。余检验均", "未见明显异常。特殊检查：2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大", "致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。术前诊断：1.肝癌介入治", "疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤靶向治疗5.恶性肿瘤免疫", "治疗6.肾结石。有手术指征，排除手术禁忌症后，于2025年04月27日局部麻醉下行肝动脉栓塞术,肝", "局部灌注术,肝动脉造影术,肝动脉置管术，术后给予患者止痛、补液等对症治疗，今患者术后恢复", "可，给予出院。", "出院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心", "悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉", "穿刺点无渗血，双下肢动脉搏动良好。", "出院医嘱：", "第1页", ""]
2026-08-10 15:44:23,264 INFO     29 [qwen-vl-parser] page=7 text: 22 lines (bbox 130-151)
2026-08-10 15:44:23,265 INFO     29 [qwen-vl-parser] page=7 text: 22 sections
2026-08-10 15:44:23,488 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1751211, prompt_len=764
2026-08-10 15:44:24,617 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:44:24.614+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:44:24,830 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:44:24,831 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 15:44:24,852 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1751211, prompt_len=401
2026-08-10 15:44:31,273 INFO     29 [qwen-vl-parser] text API response (len=1123):
["入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。", "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,", "2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白", "蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-", "谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,", "2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙", "肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,", "2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血", "酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+", "增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检", "查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。术前", "诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肾结石3.肺部感染4.慢性乙型病毒性肝炎，经讨论评", "估为不可切除，决定行转化治疗，排除手术禁忌症后，于2025年03月20日行肝动脉栓塞术,肝动脉造影", "术,动脉注射化疗药物,肝动脉置管术，术后给予患者抗感染、护肝等对症治疗，今患者术后恢复可，", "予以靶免治疗(仑伐替尼，3粒，qd；信迪利单抗200mg，q3w)后给予出院。", "出院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肝癌介入治疗3.恶性肿瘤靶向治疗4.恶性肿瘤免", "疫治疗5.肾结石6.肺部感染7.慢性乙型病毒性肝炎。", "出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心", "悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉", "穿刺点无渗血，双下肢动脉搏动良好。", "第1页"]
2026-08-10 15:44:31,274 INFO     29 [qwen-vl-parser] page=8 text: 22 lines (bbox 152-173)
2026-08-10 15:44:31,274 INFO     29 [qwen-vl-parser] page=8 text: 22 sections
2026-08-10 15:44:31,484 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1797688, prompt_len=764
2026-08-10 15:44:32,915 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 15:44:32,915 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 15:44:32,923 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1797688, prompt_len=401
2026-08-10 15:44:39,615 INFO     29 [qwen-vl-parser] text API response (len=1163):
["入院日期：2025年03月18日", "出院日期：2025年03月24日", "住院天数：6天", "入院情况(简要病史\体格检查及主要辅助检查)：患者男，57岁，因“反复右上腹部疼痛半年”入", "院。患者自诉半年余前开始无明显诱因下出现右上腹部疼痛，无恶心呕吐，无畏寒发热，自行缓解，1", "天前再发腹痛，至我院急诊就诊，行CT检查提示肝占位性病变，请我科医师会诊后，拟“肝占位性病", "变”收入我科住院。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。", "专科情况：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲", "张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓", "音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：", "2025-03-18上腹部CT平扫+增强扫描见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，", "请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺", "散在炎性灶。", "入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。", "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,", "2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白", "蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-", "谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，", "2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙", "肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，", "2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血", "酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+", "增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检"]
2026-08-10 15:44:39,615 INFO     29 [qwen-vl-parser] page=9 text: 24 lines (bbox 174-197)
2026-08-10 15:44:39,615 INFO     29 [qwen-vl-parser] page=9 text: 24 sections
2026-08-10 15:44:39,767 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1218824, prompt_len=764
2026-08-10 15:44:43,052 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-06"
}
```
2026-08-10 15:44:43,052 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2026-03-06
2026-08-10 15:44:43,069 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1218824, prompt_len=401
2026-08-10 15:44:47,533 INFO     29 [qwen-vl-parser] text API response (len=755):
["临床诊断:1.肝细胞癌(BCLC B期,CNLC IIb期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶", "向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗", "检查项目:上腹部薄层CT平扫+增强扫描", "检查所见:", "肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显", "强化,肿块边缘及邻近肝实质内多发稍低密度结节,边界欠清,部分融合,呈“快进快出”", "强化方式,部分与邻近肝内血管分界欠清,门静脉右后支纤细;肝右静脉显示不清,下腔静", "脉内见充盈缺损,肝中静脉受压推挤改变、局部显示欠清。另肝实质内见多发小圆形低密", "度,较大者直径约7mm,增强无强化。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积", "稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及", "腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见", "斑点状致密影。", "印象:", "“肝癌”综合治疗后,较2025-12-07日腹部CT:肝右叶肿块较前大小相仿,无明显血供;", "肿块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大,下腔静脉癌栓形成;余较前相", "仿。", "报告医师:梁利民", "审核医师:", "重要提示:本报告仅供临床医师诊断时参考 审核时间:2026-3-6 13:21:46", "医院咨询电话:0791-86120120(东湖):0791-87311120(红角洲):0791-85229772(青云谱)", "东湖影像科咨询电话:0791-86213393(登记室):0791-86301219(阅片室)", "红角洲影像科咨询电话:0791-86257676("]
2026-08-10 15:44:47,533 INFO     29 [qwen-vl-parser] page=10 text: 22 lines (bbox 198-219)
2026-08-10 15:44:47,533 INFO     29 [qwen-vl-parser] page=10 text: 22 sections
2026-08-10 15:44:47,693 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1271840, prompt_len=764
2026-08-10 15:44:49,104 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-12-07"
}
```
2026-08-10 15:44:49,105 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2025-12-07
2026-08-10 15:44:49,123 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1271840, prompt_len=401
2026-08-10 15:44:54,124 INFO     29 [qwen-vl-parser] text API response (len=801):
["临床诊断:1.肝细胞癌(BCLC B期,CNLC 11b期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶", "向治疗,4.恶性肿瘤免疫治疗", "检查项目:上腹部薄层CT平扫+增强扫描", "检查所见:", "肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显", "强化,肿块边缘及邻近肝实质内多个稍低密度结节,呈“快进快出”强化方式,大者大小约", "54mm×31mm,部分与邻近肝内血管分界欠清。另肝实质内见多发小圆形低密度,较大者直径", "约7mm,增强无强化。门静脉右后支纤细,似见条状充盈缺损;肝右静脉显示不清,肝中静", "脉受压推挤改变、局部显示欠清。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍", "大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹", "膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑", "点状致密影。", "印象:", "肝癌综合治疗后,对比2025-9-10日CT:肝右叶肿块较前大小相仿,无明显血供;新增肿块", "边缘及邻近肝实质内多个子灶或转移灶,有活性,个别病灶与肝中静脉分界不清;胆囊壁水", "肿基本缓解;余较前相仿。", "报告医师:冯梓妍", "审核医师:", "熊小丽", "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-12-7 16:33:54", "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)", "东南影像科咨询电话:0791-86213393(登记室);0791-86301219(阅片室)", "红角洲影像科咨询电话:0791-86357670(骨记室);0701:87357668(原片室)", "第1页 共1页"]
2026-08-10 15:44:54,125 INFO     29 [qwen-vl-parser] page=11 text: 24 lines (bbox 220-243)
2026-08-10 15:44:54,125 INFO     29 [qwen-vl-parser] page=11 text: 24 sections
2026-08-10 15:44:54,230 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=724144, prompt_len=764
2026-08-10 15:44:55,669 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-09-11"
}
```
2026-08-10 15:44:55,670 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2025-09-11
2026-08-10 15:44:55,690 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=724144, prompt_len=401
2026-08-10 15:44:56,418 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:44:56.416+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:44:58,333 INFO     29 [qwen-vl-parser] text API response (len=415):
["临床诊断:1.肝癌介入治疗,2.原发性肝癌", "检查项目:胸部CT平扫", "检查所见:", "两肺纹理增粗增多,右肺上叶见一类圆形小囊泡。两下肺见散在条索及条带状实变影,", "边界清;右下肺前基底段见不规则实性密度条片影(SE202IM184),大小约21mm×13mm;", "两肺散在少许直径约2-3mm微小结节影,界清。气管、主要支气管通畅,两肺门及纵隔未见", "明确肿大淋巴结。心脏不大,双侧胸膜无明显增厚,胸腔内未见积液。", "印象:", "对比2025-8-4胸部CT:右下肺实性结节影较前稍减小,请结合临床;两下肺胸膜下渗出", "及条索灶较前减少吸收;余大致同前。", "报告医师:肖轩", "审核医师:钟玉凤", "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-9-11 8:39:32", "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲)"]
2026-08-10 15:44:58,334 INFO     29 [qwen-vl-parser] page=12 text: 14 lines (bbox 244-257)
2026-08-10 15:44:58,334 INFO     29 [qwen-vl-parser] page=12 text: 14 sections
2026-08-10 15:44:58,480 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1120259, prompt_len=764
2026-08-10 15:44:59,982 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-06-03"
}
```
2026-08-10 15:44:59,983 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=2025-06-03
2026-08-10 15:44:59,993 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1120259, prompt_len=401
2026-08-10 15:45:03,769 INFO     29 [qwen-vl-parser] text API response (len=644):
["临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期),3.慢性乙型病毒性", "肝炎", "检查项目:上腹部CT平扫+增强扫描", "检查所见:", "肝内见团块状低密度影,其周围见多发斑片状高密度影,增强扫描动脉期肿瘤边缘无碘", "油沉积区见不均匀强化影,平衡期强化程度减低,病灶中心见无强化低密度区;另肝实质内", "见多发小圆形低密度,较大者直径约7mm,增强无强化。肝中及肝左静脉显示欠清,肝内外", "胆管无明显扩张。胆囊不大,壁无增厚。脾脏体积不大,实质密度强化均匀;胰腺大小、形", "态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短", "径约10mm,轻度强化。腹腔内未见积液。所示左肾盏见斑点高密度影。", "印象:", "肝癌综合治疗后,与2025-3-18片比较:", "肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及", "实验室资料;", "肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。", "报告医师:钟芳琴", "审核医师:邓军", "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-6-3 16:42:51", "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)", "东湖影像科咨询电话:0791 86212009(部门otn)"]
2026-08-10 15:45:03,770 INFO     29 [qwen-vl-parser] page=13 text: 20 lines (bbox 258-277)
2026-08-10 15:45:03,770 INFO     29 [qwen-vl-parser] page=13 text: 20 sections
2026-08-10 15:45:03,919 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1161817, prompt_len=764
2026-08-10 15:45:05,406 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-05"
}
```
2026-08-10 15:45:05,407 INFO     29 [qwen-vl-parser] page=14 classify=table report_date=2026-03-05
2026-08-10 15:45:05,419 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1161817, prompt_len=756
2026-08-10 15:45:18,134 INFO     29 [qwen-vl-parser] table API response (len=2202):
\begin{tabular}{llllllllllll}
\hline
五分类法) & 2026-03-05 11:08:21 & 异常报告 & 王辉 & 全 & 缩写 & 项目名称 & 结果 & 扩展结果 & 异常提示 & 多耐标志 & 辅助诊断 & 单位 & 参考范围 & 历次 \\
\hline
项+肝功能八项+白蛋 & 2026-03-05 13:50:21 & 异常报告 & 王辉 & 血 & WBC & 白细胞计数 & 6.47 & & & & & 10^9/L & 3.5-9.5 & 4.94 \\
\hline
 & 2026-03-05 14:44:11 & 异常报告 & 王辉 & 血 & RBC & 红细胞计数 & 6.90 & & H & & & 10^12/L & 4.3-5.8 & 6.56 \\
\hline
五分类法) & 2025-12-07 09:31:31 & 异常报告 & 王辉 & 全 & HGB & 血红蛋白 & 133 & & & & & g/L & 130-175 & 127 \\
\hline
项+肝功能八项+白蛋 & 2025-12-07 10:49:11 & 异常报告 & 王辉 & 血 & PLT & 血小板计数 & 142 & & & & & 10^9/L & 125-350 & 137 \\
\hline
 & 2025-12-08 09:35:51 & 异常报告 & 王辉 & 血 & NEUT\% & 中性粒细胞百分比 & 70.3 & & & & & \% & 40-75 & 64.0 \\
\hline
状腺激素(FT3,FT4,促甲) & 2025-09-21 12:48:01 & 正常报告 & 王辉 & 血 & LYM\% & 淋巴细胞百分比 & 19.5 & & L & & & \% & 20-50 & 24.9 \\
\hline
 & 2025-09-21 13:27:11 & 异常报告 & 王辉 & 血 & MONO\% & 单核细胞百分比 & 9.4 & & & & & \% & 3-10 & 10.1 \\
\hline
 & & & & & EO\% & 嗜酸性粒细胞百分比 & 0.50 & & & & & \% & 0.4-8 & 0.80 \\
\hline
 & & & & & BASO\% & 嗜碱性粒细胞百分比 & 0.3 & & & & & \% & 0-1 & 0.2 \\
\hline
 & & & & & NEUT\# & 中性粒细胞绝对值 & 4.55 & & & & & 10^9/L & 2-7 & 3.16 \\
\hline
 & & & & & LYM\# & 淋巴细胞绝对值 & 1.26 & & L & & & 10^9/L & 1.5-4 & 1.23 \\
\hline
 & & & & & MONO\# & 单核细胞绝对值 & 0.61 & & H & & & 10^9/L & 0-0.5 & 0.50 \\
\hline
 & & & & & EO\# & 嗜酸性粒细胞绝对值 & 0.03 & & L & & & 10^9/L & 0.1-0.4 & 0.04 \\
\hline
 & & & & & BASO\# & 嗜碱性粒细胞绝对值 & 0.02 & & & & & 10^9/L & 0-0.07 & 0.01 \\
\hline
 & & & & & HCT & 红细胞压积 & 44.80 & & & & & \% & 40-50 & 43.40 \\
\hline
 & & & & & MCV & 平均红细胞体积 & 64.9 & & L & & & fL & 82-100 & 66.2 \\
\hline
 & & & & & MCH & 平均红细胞Hb含量 & 19.3 & & L & & & pg & 27-34 & 19.4 \\
\hline
 & & & & & MCHC & 平均红细胞Hb浓度 & 297 & & L & & & g/L & 316-354 & 293 \\
\hline
 & & & & & RDW-CV & 红细胞分布宽度(CV) & 18.4 & & H & & & \% & 10.9-15.4 & 17.0 \\
\hline
 & & & & & RDW-SD & 红细胞分布宽度(SD) & 37.9 & & L & & & fl & 39-46 & 34.5 \\
\hline
 & & & & & PCT & 血小板压积 & ---- & & & & & \% & 0.1-0.28 & ---- \\
\hline
 & & & & & PDW & 血小板分布宽度 & ---- & & & & & fl & 11-26.5 & ---- \\
\hline
 & & & & & MPV & 平均血小板体积 & ---- & & & & & fL & 7.6-13.2 & ---- \\
\hline
 & & & & & P-LCR & 十血小板比值 & ---- & & & & & \% & 13-43 & \\
\hline
\end{tabular}
2026-08-10 15:45:18,136 INFO     29 [qwen-vl-parser] page=14 table: 54 LaTeX lines (bbox 278-331)
2026-08-10 15:45:18,136 INFO     29 [qwen-vl-parser] page=14 table: 54 sections
2026-08-10 15:45:18,257 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=862192, prompt_len=764
2026-08-10 15:45:19,774 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-03-05"}
```
2026-08-10 15:45:19,774 INFO     29 [qwen-vl-parser] page=15 classify=table report_date=2026-03-05
2026-08-10 15:45:19,803 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=862192, prompt_len=756
2026-08-10 15:45:27,223 INFO     29 [qwen-vl-parser] table API response (len=1627):
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{报告日期} & \textbf{报告状态} & \textbf{姓名} & \textbf{阅读} & \textbf{标} & \textbf{缩写} & \textbf{项目名称} & \textbf{结果} & \textbf{扩展结果} & \textbf{异常提示} & \textbf{多耐标志} & \textbf{辅助诊断} & \textbf{单位} & \textbf{参考范} \\
\hline
2026-03-05 11:08:21 & \textcolor{red}{异常报告} & 王腊 & & 全 & TP & 总蛋白 & 77.80 & & & & & g/L & 65-8 \\
\hline
2026-03-05 13:50:21 & \textcolor{red}{异常报告} & 王腊 & & 血 & ALB & 白蛋白 & 42.70 & & & & & g/L & 40-5 \\
\hline
2026-03-05 14:44:11 & \textcolor{red}{异常报告} & 王腊 & & 血 & GLB & 球蛋白 & 35.10 & & & & & g/L & 20-4 \\
\hline
2025-12-07 09:31:31 & \textcolor{red}{异常报告} & 王腊 & & 全 & A/G & 白球比例 & 1.22 & & & & & & 1.2- \\
\hline
2025-12-07 10:49:11 & \textcolor{red}{异常报告} & 王腊 & & 血 & TBIL & 总胆红素 & 31.70 & & H & & & \textmu mol/L & 0-20 \\
\hline
2025-12-08 09:35:51 & \textcolor{red}{异常报告} & 王腊 & & 血 & DBIL & 直接胆红素 & 13.30 & & H & & & \textmu mol/L & 0-6. \\
\hline
2025-09-21 12:48:01 & 正常报告 & 王腊 & & 血 & IBIL & 间接胆红素 & 18.40 & & H & & & \textmu mol/L & 0-18 \\
\hline
2025-09-21 13:27:11 & \textcolor{red}{异常报告} & 王腊 & & 血 & AST & 天门冬氨酸氨基转移酶 & 89.00 & & H & & & U/L & 15- \\
\hline
& & & & & ALT & 丙氨酸氨基转移酶 & 54.30 & & H & & & U/L & 9- \\
\hline
& & & & & ALP & 碱性磷酸酶 & 224.00 & & H & & & U/L & 45- \\
\hline
& & & & & \textgamma-GT & \textgamma-谷氨酰基转移酶 & 495.90 & & H & & & U/L & 10 \\
\hline
& & & & & UREA & 尿素 & 4.25 & & & & & mmol/L & 3.1 \\
\hline
& & & & & Cre & 肌酐 & 69.80 & & & & & \textmu mol/L & 57 \\
\hline
& & & & & eGFR & 估算肾小球滤过率 & 107.16 & & & & & & 仅适用 \\
\hline
& & & & & URIC & 尿酸 & 315.40 & & & & & \textmu mol/L & 208 \\
\hline
\end{tabular}
2026-08-10 15:45:27,224 INFO     29 [qwen-vl-parser] page=15 table: 36 LaTeX lines (bbox 332-367)
2026-08-10 15:45:27,224 INFO     29 [qwen-vl-parser] page=15 table: 36 sections
2026-08-10 15:45:27,330 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=702756, prompt_len=764
2026-08-10 15:45:28,257 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:45:28.256+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:45:28,772 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-03-05"}
```
2026-08-10 15:45:28,772 INFO     29 [qwen-vl-parser] page=16 classify=table report_date=2026-03-05
2026-08-10 15:45:28,792 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=702756, prompt_len=756
2026-08-10 15:45:34,071 INFO     29 [qwen-vl-parser] table API response (len=1107):
\begin{tabular}{ccccccccccc}
\hline
\multicolumn{1}{c}{报告日期} & \multicolumn{1}{c}{报告状态} & \multicolumn{1}{c}{姓名} & \multicolumn{1}{c}{阅读} & \multicolumn{1}{c}{标} & \multicolumn{1}{c}{缩写} & \multicolumn{1}{c}{项目名称} & \multicolumn{1}{c}{结果} & \multicolumn{1}{c}{扩展结果} & \multicolumn{1}{c}{异常提示} & \multicolumn{1}{c}{多瘤标志} & \multicolumn{1}{c}{辅助诊断} & \multicolumn{1}{c}{单位} & \multicolumn{1}{c}{参考范围} \\
\hline
2026-03-05 11:08:21 & 异常报告 & 王雄 & & 全 & AFP & 甲胎蛋白测定 & >240000.00 & & H & & & ng/ml & 0-7 \\
2026-03-05 13:50:21 & 异常报告 & 王雄 & & 血 & AFP-L3 & 甲胎蛋白异质体L3测定 & 53777.00 & & H & & & ng/ml & 0-1 \\
2026-03-05 14:44:11 & 异常报告 & 王雄 & & 血 & DCP & 异常凝血酶原测定 & >20000.00 & & H & & & ng/ml & 0-40 \\
2025-12-07 09:31:31 & 异常报告 & 王雄 & & 全 & AFP-L3\% & 甲胎蛋白异质体比率(L3\%) & >10\% & & H & & & & 0-10\% \\
2025-12-07 10:49:11 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\
2025-12-08 09:35:51 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\
2025-09-21 12:48:01 & 正常报告 & 王雄 & & 血 & C-GALAD & 肝癌辅助分析评分 & 99.91 & & & & & & 54以下偏低风险;54-66为肝部疾病中风险;>66判定偏高风险 \\
2025-09-21 13:27:11 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\
\hline
\end{tabular}
2026-08-10 15:45:34,072 INFO     29 [qwen-vl-parser] page=16 table: 15 LaTeX lines (bbox 368-382)
2026-08-10 15:45:34,072 INFO     29 [qwen-vl-parser] page=16 table: 15 sections
2026-08-10 15:45:34,072 INFO     29 [qwen-vl-parser] parse_pdf done: 383 sections from 16 pages.
2026-08-10 15:45:34,079 INFO     29 Close text detector.
2026-08-10 15:45:34,480 INFO     29 Close text recognizer.
2026-08-10 15:45:34,898 INFO     29 Close recognizer.
2026-08-10 15:45:35,332 INFO     29 Close recognizer.
2026-08-10 15:45:35,975 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 15:45:35,975 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Parser:MedLink | outputs={"html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "json"}
2026-08-10 15:45:35,975 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 15:45:36,017 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:45:36,017 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 族:汉族\n[BBOX-1] 婚姻:已婚\n[BBOX-2] 出生地:江西省南昌市湾里区\n[BBOX-3] 业:其他\n[BBOX-4] 现住址:江西省南昌市湾里区\n[BBOX-5] 史陈述者:本人及家属\n[BBOX-6] 与患者关系:其他\n[BBOX-7] 可靠程度:基本可靠\n[BBOX-8] 院时间:2025年09月16日 14:33\n[BBOX-9] 记录时间:2025年09月16日 15:59\n[BBOX-10] 诉:肝癌综合治疗5月余。\n[BBOX-11] 病史:患者5月余前开始因肝癌于我院行综合治疗(介入+靶向+免疫:TACE+仑伐替尼+信迪利单\n[BBOX-12] ), 后于2025年04月27日、2025年06月03日、2025年08月04日行肝动脉栓塞术。现患者为求下一周\n[BBOX-13] 治疗来我院就诊。门诊拟\"肝癌介入治疗\"收入我科。患者自起病来, 饮食睡眠一般, 大小便如常,\n[BBOX-14] 睡无明显变化。\n[BBOX-15] 注史:患者既往身体较差。否认高血压病史。否认糖尿病史。否认冠心病史。否认肾病史。有肝炎\n[BBOX-16] 史慢性乙型病毒性肝炎。否认结核病史。有手术史2025年03月20日、4月27日、06月03日、08月04日\n[BBOX-17] 行肝动脉栓塞术, 肝局部灌注术, 肝动脉造影术, 动脉注射化疗药物, 肝动脉置管术手术。否认外伤史\n[BBOX-18] 否认输血史。否认药物、食物过敏史。\n[BBOX-19] 人史:生于原籍, 久居本地, 否认疫区、疫水接触史。否认毒物、放射性物质接触史。否认烟酒嗜好\n[BBOX-20] 育史:已婚,[结婚年龄]适龄结婚, 配偶体健, 夫妻关系和睦。育有[育子数量]男、[育女数量]\n[BBOX-21] 均体健。\n[BBOX-22] 史:否认家族及遗传病史。\n[BBOX-23] 体格检查\n[BBOX-24] 体温:36.8℃ 脉搏:82次/分 呼吸:20次/分 血压:115/87mmHg\n[BBOX-25] 正常, 营养中等, 表情自然, 无贫血貌, 自主体位, 步入病房, 步态正常, 神志清楚, 查体合作\n[BBOX-26] 身皮肤黏膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣。全身浅表淋巴结未触及\n[BBOX-27] 。头颅无畸形, 双眼睑无水肿, 眼球无突出及震颤, 结膜无苍白、无充血、无出血、无水肿, 巩\n[BBOX-28] 工作单位或地址:湾里区\n[BBOX-29] 就诊科室:红角洲肝胆外科门诊\n[BBOX-30] 就诊时间:2025年12月07日 08:46\n[BBOX-31] 药物过敏史:无\n[BBOX-32] 主诉:肝Ca综合治疗后半年返院复查。\n[BBOX-33] 病史:肝Ca综合治疗后半年复查。未诉特殊不适。\n[BBOX-34] 既往史和其他病史:既往半年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。\n[BBOX-35] 体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。\n[BBOX-36] 助检查:暂缺。\n[BBOX-37] 诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿\n[BBOX-38] 靶向治疗;4.恶性肿瘤免疫治疗\n[BBOX-39] 理:1.胸部CT平扫\n[BBOX-40] 上腹部薄层CT平扫+增强扫描\n[BBOX-41] 肝癌三项:肝功能八项+白蛋白;血常规(五分类法);肾功能3项\n[BBOX-42] 碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶\n[BBOX-43] 用法:每次30g即时造影用1天\n[BBOX-44] CT静脉注药(留置针置管)每次1项\n[BBOX-45] 转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院\n[BBOX-46] 医生签名:\n[BBOX-47] 就诊科室:红角洲肝胆外科门诊\n[BBOX-48] 就诊时间:2026年03月05日 09:51\n[BBOX-49] 药物过敏史:无\n[BBOX-50] 主诉:肝Ca综合治疗后1年返院评估介入治疗。\n[BBOX-51] 现病史:肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。\n[BBOX-52] 既往史和其他病史:既往1年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。\n[BBOX-53] 查体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。\n[BBOX-54] 辅助检查:暂缺。\n[BBOX-55] 诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿\n[BBOX-56] 瘤靶向治疗;4.恶性肿瘤免疫治疗;5.肝癌介入治疗\n[BBOX-57] 处理:1.胸部CT平扫\n[BBOX-58] 2.上腹部薄层CT平扫+增强扫描\n[BBOX-59] 3.肝癌三项;肝功能八项+白蛋白:血常规(五分类法);肾功能3项\n[BBOX-60] 4.碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶\n[BBOX-61] 用法:每次30g即时造影用1天\n[BBOX-62] 5.CT静脉注药(留置针置管)每次1项\n[BBOX-63] 下转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院\n[BBOX-64] 医生签名:\n[BBOX-65] 职业：\n[BBOX-66] 出生日期：1968年01月06日\n[BBOX-67] 工作单位或地址：湾里区\n[BBOX-68] 就诊科室：红角洲肝胆外科门诊\n[BBOX-69] 就诊时间：2026年03月07日 14:40\n[BBOX-70] 药物过敏史：无\n[BBOX-71] 主诉：肝Ca综合治疗后1年返院评估介入治疗。\n[BBOX-72] 现病史：肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。\n[BBOX-73] 既往史和其他病史：既往1年前诊断肝CA，行介入+抗肿瘤靶向+免疫治疗。\n[BBOX-74] 查体：血压：/mmHg，脉搏：次/分。无特殊阳性体征。\n[BBOX-75] 辅助检查：2026-03-06,上腹部薄层CT平扫+增强扫描检查意见：“肝癌”综合\n[BBOX-76] 治疗后，较2025-12-07日腹部CT：肝右叶肿块较前大小相仿，无明显血供；肿\n[BBOX-77] 块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大，下腔静脉癌栓形\n[BBOX-78] 成；余较前相仿。\n[BBOX-79] 诊断：1.肝细胞癌(BCLC B期，CNLC IIb期)；2.恶性肿瘤靶向治疗；3.恶性肿瘤\n[BBOX-80] 免疫治疗；4.肝癌介入治疗；5.慢性肝炎\n[BBOX-81] 处理：\n[BBOX-82] 下转情况：◎不下转 ○转县级院 ○转社区卫生服务机构/乡镇卫生院\n[BBOX-83] 医生签名：陈天翔\n[BBOX-84] 入院日期：2025年08月02日\n[BBOX-85] 出院日期：2025年08月06日\n[BBOX-86] 住院天数：4\n[BBOX-87] 入院情况(简要病史\\体格检查及主要辅助检查)：患者男性57岁，因肝癌于我院行综合治疗，现为返\n[BBOX-88] 院复诊，无头晕头痛，胸闷气促，恶心呕吐等不适，于我院门诊就诊，门诊拟\"肝癌介入治疗\"收入我\n[BBOX-89] 科。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。查体：神志清楚，\n[BBOX-90] 皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压\n[BBOX-91] 痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨\n[BBOX-92] 中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：暂无。\n[BBOX-93] 入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.肝细胞癌4.恶性肿瘤靶向治疗5.\n[BBOX-94] 恶性肿瘤免疫治疗6.慢性乙型病毒性肝炎。\n[BBOX-95] 诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检\n[BBOX-96] 验检查：主要化验：2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞\n[BBOX-97] 计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l,\n[BBOX-98] 2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶\n[BBOX-99] 原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋\n[BBOX-100] 白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。特殊检查：\n[BBOX-101] 2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层\n[BBOX-102] 194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。\n[BBOX-103] 2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶\n[BBOX-104] 肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆\n[BBOX-105] 管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。有手术指征，排除手术禁忌症后，于2025\n[BBOX-106] 年08月04日行肝动脉栓塞术 肝动脉造影术 腹腔动脉灌注化疗药物，术后给予患者止吐、护胃、止\n[BBOX-107] 痛、补液等对症治疗，今患者术后恢复可，予以免疫治疗后，患者无特殊不适，给予出院。\n[BBOX-108] 诊疗经过(包括手术日期和手术名称,植入类医用耗材名称、型号及数量):入院后予以完善相关检\n[BBOX-109] 验检查:主要化验:2025-06-02肝功能五项:γ-谷氨酰基转移酶67.30U/L。2025-06-02血清总蛋白+\n[BBOX-110] 白蛋白测定:白蛋白39.40g/L。2025-06-02超敏C反应蛋白测定+金标法加收(全程,快):超敏C反应\n[BBOX-111] 蛋白测定(全程)30.63mg/L。2025-06-02血常规(五分类法):红细胞计数7.01*10^12/L,血小板计数\n[BBOX-112] 110*10^9/L。2025-06-02肝癌三项:甲胎蛋白测定4679.00ng/ml,甲胎蛋白异质体L3测定370.00ng/ml,\n[BBOX-113] 异常凝血酶原测定>20000.00ng/ml。2025-06-04超敏C反应蛋白测定+金标法加收(全程,快):超敏C\n[BBOX-114] 反应蛋白测定(全程)25.06mg/L。2025-06-04血常规(五分类法):红细胞计数6.19*10^12/L,血红蛋\n[BBOX-115] 白119g/L,血小板计数113*10^9/L,中性粒细胞百分比89.8%。2025-06-04凝血四项:凝血酶原时间\n[BBOX-116] 13.3sec。2025-06-04肝功能八项+白蛋白:天门冬氨酸氨基转移酶60.10U/L。余检验均未见明显异\n[BBOX-117] 常。特殊检查:2025-06-03,上腹部CT平扫+增强扫描检查意见:肝癌综合治疗后,与2025-3-18片比\n[BBOX-118] 较:肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及实验\n[BBOX-119] 室资料;肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。术\n[BBOX-120] 前诊断:原发性肝癌(BCLC B期,CNLC IIb期),有手术指征,排除手术禁忌症后,于2025-06-03行肝\n[BBOX-121] 动脉栓塞术+肝局部灌注术,术后给予患者护胃、止吐、止痛、补液等对症治疗,今患者术后恢复可,\n[BBOX-122] 给予出院。\n[BBOX-123] 出院诊断:1.肝癌介入治疗2.原发性肝癌(BCLC B期,CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤\n[BBOX-124] 靶向治疗5.恶性肿瘤免疫治疗6.肾结石。\n[BBOX-125] 出院情况:患者一般情况良好,生命体征平稳,无畏寒发热,无恶心呕吐,无头痛头晕,无胸闷心\n[BBOX-126] 悸。查体:全身皮肤、巩膜未见黄染,腹平软,无压痛,未及反跳痛和肌紧张,肠鸣音正常,股动脉\n[BBOX-127] 穿刺点无渗血,双下肢动脉搏动良好。\n[BBOX-128] 出院医嘱:\n[BBOX-129] I\n[BBOX-130] 肝区介入术后复查所见。\n[BBOX-131] 入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤\n[BBOX-132] 靶向治疗5.恶性肿瘤免疫治疗6.肾结石。\n[BBOX-133] 诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检\n[BBOX-134] 验检查：主要化验：2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,\n[BBOX-135] 2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白\n[BBOX-136] 44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性\n[BBOX-137] 磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测\n[BBOX-138] 定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。余检验均\n[BBOX-139] 未见明显异常。特殊检查：2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大\n[BBOX-140] 致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。术前诊断：1.肝癌介入治\n[BBOX-141] 疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤靶向治疗5.恶性肿瘤免疫\n[BBOX-142] 治疗6.肾结石。有手术指征，排除手术禁忌症后，于2025年04月27日局部麻醉下行肝动脉栓塞术,肝\n[BBOX-143] 局部灌注术,肝动脉造影术,肝动脉置管术，术后给予患者止痛、补液等对症治疗，今患者术后恢复\n[BBOX-144] 可，给予出院。\n[BBOX-145] 出院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤\n[BBOX-146] 靶向治疗5.恶性肿瘤免疫治疗6.肾结石。\n[BBOX-147] 出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心\n[BBOX-148] 悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉\n[BBOX-149] 穿刺点无渗血，双下肢动脉搏动良好。\n[BBOX-150] 出院医嘱：\n[BBOX-151] 第1页\n[BBOX-152] 入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。\n[BBOX-153] 诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检\n[BBOX-154] 验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,\n[BBOX-155] 2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白\n[BBOX-156] 蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-\n[BBOX-157] 谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,\n[BBOX-158] 2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙\n[BBOX-159] 肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,\n[BBOX-160] 2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血\n[BBOX-161] 酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+\n[BBOX-162] 增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检\n[BBOX-163] 查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。术前\n[BBOX-164] 诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肾结石3.肺部感染4.慢性乙型病毒性肝炎，经讨论评\n[BBOX-165] 估为不可切除，决定行转化治疗，排除手术禁忌症后，于2025年03月20日行肝动脉栓塞术,肝动脉造影\n[BBOX-166] 术,动脉注射化疗药物,肝动脉置管术，术后给予患者抗感染、护肝等对症治疗，今患者术后恢复可，\n[BBOX-167] 予以靶免治疗(仑伐替尼，3粒，qd；信迪利单抗200mg，q3w)后给予出院。\n[BBOX-168] 出院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肝癌介入治疗3.恶性肿瘤靶向治疗4.恶性肿瘤免\n[BBOX-169] 疫治疗5.肾结石6.肺部感染7.慢性乙型病毒性肝炎。\n[BBOX-170] 出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心\n[BBOX-171] 悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉\n[BBOX-172] 穿刺点无渗血，双下肢动脉搏动良好。\n[BBOX-173] 第1页\n[BBOX-174] 入院日期：2025年03月18日\n[BBOX-175] 出院日期：2025年03月24日\n[BBOX-176] 住院天数：6天\n[BBOX-177] 入院情况(简要病史\\体格检查及主要辅助检查)：患者男，57岁，因“反复右上腹部疼痛半年”入\n[BBOX-178] 院。患者自诉半年余前开始无明显诱因下出现右上腹部疼痛，无恶心呕吐，无畏寒发热，自行缓解，1\n[BBOX-179] 天前再发腹痛，至我院急诊就诊，行CT检查提示肝���位性病变，请我科医师会诊后，拟“肝占位性病\n[BBOX-180] 变”收入我科住院。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。\n[BBOX-181] 专科情况：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲\n[BBOX-182] 张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓\n[BBOX-183] 音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：\n[BBOX-184] 2025-03-18上腹部CT平扫+增强扫描见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，\n[BBOX-185] 请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺\n[BBOX-186] 散在炎性灶。\n[BBOX-187] 入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。\n[BBOX-188] 诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检\n[BBOX-189] 验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,\n[BBOX-190] 2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白\n[BBOX-191] 蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-\n[BBOX-192] 谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，\n[BBOX-193] 2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙\n[BBOX-194] 肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，\n[BBOX-195] 2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血\n[BBOX-196] 酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+\n[BBOX-197] 增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检\n[BBOX-198] 临床诊断:1.肝细胞癌(BCLC B期,CNLC IIb期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶\n[BBOX-199] 向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗\n[BBOX-200] 检查项目:上腹部薄层CT平扫+增强扫描\n[BBOX-201] 检查所见:\n[BBOX-202] 肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显\n[BBOX-203] 强化,肿块边缘及邻近肝实质内多发稍低密度结节,边界欠清,部分融合,呈“快进快出”\n[BBOX-204] 强化方式,部分与邻近肝内血管分界欠清,门静脉右后支纤细;肝右静脉显示不清,下腔静\n[BBOX-205] 脉内见充盈缺损,肝中静脉受压推挤改变、局部显示欠清。另肝实质内见多发小圆形低密\n[BBOX-206] 度,较大者直径约7mm,增强无强化。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积\n[BBOX-207] 稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及\n[BBOX-208] 腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见\n[BBOX-209] 斑点状致密影。\n[BBOX-210] 印象:\n[BBOX-211] “肝癌”综合治疗后,较2025-12-07日腹部CT:肝右叶肿块较前大小相仿,无明显血供;\n[BBOX-212] 肿块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大,下腔静脉癌栓形成;余较前相\n[BBOX-213] 仿。\n[BBOX-214] 报告医师:梁利民\n[BBOX-215] 审核医师:\n[BBOX-216] 重要提示:本报告仅供临床医师诊断时参考 审核时间:2026-3-6 13:21:46\n[BBOX-217] 医院咨询电话:0791-86120120(东湖):0791-87311120(红角洲):0791-85229772(青云谱)\n[BBOX-218] 东湖影像科咨询电话:0791-86213393(登记室):0791-86301219(阅片室)\n[BBOX-219] 红角洲影像科咨询电话:0791-86257676(\n[BBOX-220] 临床诊断:1.肝细胞癌(BCLC B期,CNLC 11b期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶\n[BBOX-221] 向治疗,4.恶性肿瘤免疫治疗\n[BBOX-222] 检查项目:上腹部薄层CT平扫+增强扫描\n[BBOX-223] 检查所见:\n[BBOX-224] 肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显\n[BBOX-225] 强化,肿块边缘及邻近肝实质内多个稍低密度结节,呈“快进快出”强化方式,大者大小约\n[BBOX-226] 54mm×31mm,部分与邻近肝内血管分界欠清。另肝实质内见多发小圆形低密度,较大者直径\n[BBOX-227] 约7mm,增强无强化。门静脉右后支纤细,似见条状充盈缺损;肝右静脉显示不清,肝中静\n[BBOX-228] 脉受压推挤改变、局部显示欠清。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍\n[BBOX-229] 大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹\n[BBOX-230] 膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑\n[BBOX-231] 点状致密影。\n[BBOX-232] 印象:\n[BBOX-233] 肝癌综合治疗后,对比2025-9-10日CT:肝右叶肿块较前大小相仿,无明显血供;新增肿块\n[BBOX-234] 边缘及邻近肝实质内多个子灶或转移灶,有活性,个别病灶与肝中静脉分界不清;胆囊壁水\n[BBOX-235] 肿基本缓解;余较前相仿。\n[BBOX-236] 报告医师:冯梓妍\n[BBOX-237] 审核医师:\n[BBOX-238] 熊小丽\n[BBOX-239] 重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-12-7 16:33:54\n[BBOX-240] 医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)\n[BBOX-241] 东南影像科咨询电话:0791-86213393(登记室);0791-86301219(阅片室)\n[BBOX-242] 红角洲影像科咨询电话:0791-86357670(骨记室);0701:87357668(原片室)\n[BBOX-243] 第1页 共1页\n[BBOX-244] 临床诊断:1.肝癌介入治疗,2.原发性肝癌\n[BBOX-245] 检查项目:胸部CT平扫\n[BBOX-246] 检查所见:\n[BBOX-247] 两肺纹理增粗增多,右肺上叶见一类圆形小囊泡。两下肺见散在条索及条带状实变影,\n[BBOX-248] 边界清;右下肺前基底段见不规则实性密度条片影(SE202IM184),大小约21mm×13mm;\n[BBOX-249] 两肺散在少许直径约2-3mm微小结节影,界清。气管、主要支气管通畅,两肺门及纵隔未见\n[BBOX-250] 明确肿大淋巴结。心脏不大,双侧胸膜无明显增厚,胸腔内未见积液。\n[BBOX-251] 印象:\n[BBOX-252] 对比2025-8-4胸部CT:右下肺实性结节影较前稍减小,请结合临床;两下肺胸膜下渗出\n[BBOX-253] 及条索灶较前减少吸收;余大致同前。\n[BBOX-254] 报告医师:肖轩\n[BBOX-255] 审核医师:钟玉凤\n[BBOX-256] 重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-9-11 8:39:32\n[BBOX-257] 医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲)\n[BBOX-258] 临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期),3.慢性乙型病毒性\n[BBOX-259] 肝炎\n[BBOX-260] 检查项目:上腹部CT平扫+增强扫描\n[BBOX-261] 检查所见:\n[BBOX-262] 肝内见团块状低密度影,其周围见多发斑片状高密度影,增强扫描动脉期肿瘤边缘无碘\n[BBOX-263] 油沉积区见不均匀强化影,平衡期强化程度减低,病灶中心见无强化低密度区;另肝实质内\n[BBOX-264] 见多发小圆形低密度,较大者直径约7mm,增强无强化。肝中及肝左静脉显示欠清,肝内外\n[BBOX-265] 胆管无明显扩张。胆囊不大,壁无增厚。脾脏体积不大,实质密度强化均匀;胰腺大小、形\n[BBOX-266] 态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短\n[BBOX-267] 径约10mm,轻度强化。腹腔内未见积液。所示左肾盏见斑点高密度影。\n[BBOX-268] 印象:\n[BBOX-269] 肝癌综合治疗后,与2025-3-18片比较:\n[BBOX-270] 肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及\n[BBOX-271] 实验室资料;\n[BBOX-272] 肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。\n[BBOX-273] 报告医师:钟芳琴\n[BBOX-274] 审核医师:邓军\n[BBOX-275] 重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-6-3 16:42:51\n[BBOX-276] 医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)\n[BBOX-277] 东湖影像科咨询电话:0791 86212009(部门otn)\n[BBOX-278] \\begin{tabular}{llllllllllll}\n[BBOX-279] 报告时间: 2026-03-05\n[BBOX-280] \\hline\n[BBOX-281] 五分类法) & 2026-03-05 11:08:21 & 异常报告 & 王辉 & 全 & 缩写 & 项目名称 & 结果 & 扩展结果 & 异常提示 & 多耐标志 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n[BBOX-282] \\hline\n[BBOX-283] 项+肝功能八项+白蛋 & 2026-03-05 13:50:21 & 异常报告 & 王辉 & 血 & WBC & 白细胞计数 & 6.47 & & & & & 10^9/L & 3.5-9.5 & 4.94 \\\\\n[BBOX-284] \\hline\n[BBOX-285] & 2026-03-05 14:44:11 & 异常报告 & 王辉 & 血 & RBC & 红细胞计数 & 6.90 & & H & & & 10^12/L & 4.3-5.8 & 6.56 \\\\\n[BBOX-286] \\hline\n[BBOX-287] 五分类法) & 2025-12-07 09:31:31 & 异常报告 & 王辉 & 全 & HGB & 血红蛋白 & 133 & & & & & g/L & 130-175 & 127 \\\\\n[BBOX-288] \\hline\n[BBOX-289] 项+肝功能八项+白蛋 & 2025-12-07 10:49:11 & 异常报告 & 王辉 & 血 & PLT & 血小板计数 & 142 & & & & & 10^9/L & 125-350 & 137 \\\\\n[BBOX-290] \\hline\n[BBOX-291] & 2025-12-08 09:35:51 & 异常报告 & 王辉 & 血 & NEUT\\% & 中性粒细胞百分比 & 70.3 & & & & & \\% & 40-75 & 64.0 \\\\\n[BBOX-292] \\hline\n[BBOX-293] 状腺激素(FT3,FT4,促甲) & 2025-09-21 12:48:01 & 正常报告 & 王辉 & 血 & LYM\\% & 淋巴细胞百分比 & 19.5 & & L & & & \\% & 20-50 & 24.9 \\\\\n[BBOX-294] \\hline\n[BBOX-295] & 2025-09-21 13:27:11 & 异常报告 & 王辉 & 血 & MONO\\% & 单核细胞百分比 & 9.4 & & & & & \\% & 3-10 & 10.1 \\\\\n[BBOX-296] \\hline\n[BBOX-297] & & & & & EO\\% & 嗜酸性粒细胞百分比 & 0.50 & & & & & \\% & 0.4-8 & 0.80 \\\\\n[BBOX-298] \\hline\n[BBOX-299] & & & & & BASO\\% & 嗜碱性粒细胞百分比 & 0.3 & & & & & \\% & 0-1 & 0.2 \\\\\n[BBOX-300] \\hline\n[BBOX-301] & & & & & NEUT\\# & 中性粒细胞绝对值 & 4.55 & & & & & 10^9/L & 2-7 & 3.16 \\\\\n[BBOX-302] \\hline\n[BBOX-303] & & & & & LYM\\# & 淋巴细胞绝对值 & 1.26 & & L & & & 10^9/L & 1.5-4 & 1.23 \\\\\n[BBOX-304] \\hline\n[BBOX-305] & & & & & MONO\\# & 单核细胞绝对值 & 0.61 & & H & & & 10^9/L & 0-0.5 & 0.50 \\\\\n[BBOX-306] \\hline\n[BBOX-307] & & & & & EO\\# & 嗜酸性粒细胞绝对值 & 0.03 & & L & & & 10^9/L & 0.1-0.4 & 0.04 \\\\\n[BBOX-308] \\hline\n[BBOX-309] & & & & & BASO\\# & 嗜碱性粒细胞绝对值 & 0.02 & & & & & 10^9/L & 0-0.07 & 0.01 \\\\\n[BBOX-310] \\hline\n[BBOX-311] & & & & & HCT & 红细胞压积 & 44.80 & & & & & \\% & 40-50 & 43.40 \\\\\n[BBOX-312] \\hline\n[BBOX-313] & & & & & MCV & 平均红细胞体积 & 64.9 & & L & & & fL & 82-100 & 66.2 \\\\\n[BBOX-314] \\hline\n[BBOX-315] & & & & & MCH & 平均红细胞Hb含量 & 19.3 & & L & & & pg & 27-34 & 19.4 \\\\\n[BBOX-316] \\hline\n[BBOX-317] & & & & & MCHC & 平均红细胞Hb浓度 & 297 & & L & & & g/L & 316-354 & 293 \\\\\n[BBOX-318] \\hline\n[BBOX-319] & & & & & RDW-CV & 红细胞分布宽度(CV) & 18.4 & & H & & & \\% & 10.9-15.4 & 17.0 \\\\\n[BBOX-320] \\hline\n[BBOX-321] & & & & & RDW-SD & 红细胞分布宽度(SD) & 37.9 & & L & & & fl & 39-46 & 34.5 \\\\\n[BBOX-322] \\hline\n[BBOX-323] & & & & & PCT & 血小板压积 & ---- & & & & & \\% & 0.1-0.28 & ---- \\\\\n[BBOX-324] \\hline\n[BBOX-325] & & & & & PDW & 血小板分布宽度 & ---- & & & & & fl & 11-26.5 & ---- \\\\\n[BBOX-326] \\hline\n[BBOX-327] & & & & & MPV & 平均血小板体积 & ---- & & & & & fL & 7.6-13.2 & ---- \\\\\n[BBOX-328] \\hline\n[BBOX-329] & & & & & P-LCR & 十血小板比值 & ---- & & & & & \\% & 13-43 & \\\\\n[BBOX-330] \\hline\n[BBOX-331] \\end{tabular}\n[BBOX-332] \\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|}\n[BBOX-333] 报告时间: 2026-03-05\n[BBOX-334] \\hline\n[BBOX-335] \\textbf{报告日期} & \\textbf{报告状态} & \\textbf{姓名} & \\textbf{阅读} & \\textbf{标} & \\textbf{缩写} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{扩展结果} & \\textbf{异常提示} & \\textbf{多耐标志} & \\textbf{辅助诊断} & \\textbf{单位} & \\textbf{参考范} \\\\\n[BBOX-336] \\hline\n[BBOX-337] 2026-03-05 11:08:21 & \\textcolor{red}{异常报告} & 王腊 & & 全 & TP & 总蛋白 & 77.80 & & & & & g/L & 65-8 \\\\\n[BBOX-338] \\hline\n[BBOX-339] 2026-03-05 13:50:21 & \\textcolor{red}{异常报告} & 王腊 & & 血 & ALB & 白蛋白 & 42.70 & & & & & g/L & 40-5 \\\\\n[BBOX-340] \\hline\n[BBOX-341] 2026-03-05 14:44:11 & \\textcolor{red}{异常报告} & 王腊 & & 血 & GLB & 球蛋白 & 35.10 & & & & & g/L & 20-4 \\\\\n[BBOX-342] \\hline\n[BBOX-343] 2025-12-07 09:31:31 & \\textcolor{red}{异常报告} & 王腊 & & 全 & A/G & 白球比例 & 1.22 & & & & & & 1.2- \\\\\n[BBOX-344] \\hline\n[BBOX-345] 2025-12-07 10:49:11 & \\textcolor{red}{异常报告} & 王腊 & & 血 & TBIL & 总胆红素 & 31.70 & & H & & & \\textmu mol/L & 0-20 \\\\\n[BBOX-346] \\hline\n[BBOX-347] 2025-12-08 09:35:51 & \\textcolor{red}{异常报告} & 王腊 & & 血 & DBIL & 直接胆红素 & 13.30 & & H & & & \\textmu mol/L & 0-6. \\\\\n[BBOX-348] \\hline\n[BBOX-349] 2025-09-21 12:48:01 & 正常报告 & 王腊 & & 血 & IBIL & 间接胆红素 & 18.40 & & H & & & \\textmu mol/L & 0-18 \\\\\n[BBOX-350] \\hline\n[BBOX-351] 2025-09-21 13:27:11 & \\textcolor{red}{异常报告} & 王腊 & & 血 & AST & 天门冬氨酸氨基转移酶 & 89.00 & & H & & & U/L & 15- \\\\\n[BBOX-352] \\hline\n[BBOX-353] & & & & & ALT & 丙氨酸氨基转移酶 & 54.30 & & H & & & U/L & 9- \\\\\n[BBOX-354] \\hline\n[BBOX-355] & & & & & ALP & 碱性磷酸酶 & 224.00 & & H & & & U/L & 45- \\\\\n[BBOX-356] \\hline\n[BBOX-357] & & & & & \\textgamma-GT & \\textgamma-谷氨酰基转移酶 & 495.90 & & H & & & U/L & 10 \\\\\n[BBOX-358] \\hline\n[BBOX-359] & & & & & UREA & 尿素 & 4.25 & & & & & mmol/L & 3.1 \\\\\n[BBOX-360] \\hline\n[BBOX-361] & & & & & Cre & 肌酐 & 69.80 & & & & & \\textmu mol/L & 57 \\\\\n[BBOX-362] \\hline\n[BBOX-363] & & & & & eGFR & 估算肾小球滤过率 & 107.16 & & & & & & 仅适用 \\\\\n[BBOX-364] \\hline\n[BBOX-365] & & & & & URIC & 尿酸 & 315.40 & & & & & \\textmu mol/L & 208 \\\\\n[BBOX-366] \\hline\n[BBOX-367] \\end{tabular}\n[BBOX-368] \\begin{tabular}{ccccccccccc}\n[BBOX-369] 报告时间: 2026-03-05\n[BBOX-370] \\hline\n[BBOX-371] \\multicolumn{1}{c}{报告日期} & \\multicolumn{1}{c}{报告状态} & \\multicolumn{1}{c}{姓名} & \\multicolumn{1}{c}{阅读} & \\multicolumn{1}{c}{标} & \\multicolumn{1}{c}{缩写} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{扩展结果} & \\multicolumn{1}{c}{异常提示} & \\multicolumn{1}{c}{多瘤标志} & \\multicolumn{1}{c}{辅助诊断} & \\multicolumn{1}{c}{单位} & \\multicolumn{1}{c}{参考范围} \\\\\n[BBOX-372] \\hline\n[BBOX-373] 2026-03-05 11:08:21 & 异常报告 & 王雄 & & 全 & AFP & 甲胎蛋白测定 & >240000.00 & & H & & & ng/ml & 0-7 \\\\\n[BBOX-374] 2026-03-05 13:50:21 & 异常报告 & 王雄 & & 血 & AFP-L3 & 甲胎蛋白异质体L3测定 & 53777.00 & & H & & & ng/ml & 0-1 \\\\\n[BBOX-375] 2026-03-05 14:44:11 & 异常报告 & 王雄 & & 血 & DCP & 异常凝血酶原测定 & >20000.00 & & H & & & ng/ml & 0-40 \\\\\n[BBOX-376] 2025-12-07 09:31:31 & 异常报告 & 王雄 & & 全 & AFP-L3\\% & 甲胎蛋白异质体比率(L3\\%) & >10\\% & & H & & & & 0-10\\% \\\\\n[BBOX-377] 2025-12-07 10:49:11 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\\\\n[BBOX-378] 2025-12-08 09:35:51 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\\\\n[BBOX-379] 2025-09-21 12:48:01 & 正常报告 & 王雄 & & 血 & C-GALAD & 肝癌辅助分析评分 & 99.91 & & & & & & 54以下偏低风险;54-66为肝部疾病中风险;>66判定偏高风险 \\\\\n[BBOX-380] 2025-09-21 13:27:11 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\\\\n[BBOX-381] \\hline\n[BBOX-382] \\end{tabular}"
  }
]
2026-08-10 15:45:56,515 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:45:56,541 INFO     29 [SmartSplitter] SmartSplitter done: 15 chunks from 15 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'OutpatientRecord': 3, 'DischargeRecord': 4, 'ExaminationReport': 4, 'LabReport': 3}
2026-08-10 15:45:56,555 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 15:45:56,556 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks": "15 items, types={'AdmissionRecord': 1, 'OutpatientRecord': 3, 'DischargeRecord': 4, 'ExaminationReport': 4, 'LabReport': 3}"}
2026-08-10 15:45:56,556 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 15:45:56,557 INFO     29 [ChunkRouter] Routed 15 chunks into 5 groups: {'chunks_Admission': 1, 'chunks_Clinical': 3, 'chunks_Discharge': 4, 'chunks_Examination': 4, 'chunks_LabExam': 3}
2026-08-10 15:45:56,570 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 15:45:56,571 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | ChunkRouter:Router | outputs={"html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks": "15 items, types={'AdmissionRecord': 1, 'OutpatientRecord': 3, 'DischargeRecord': 4, 'ExaminationReport': 4, 'LabReport': 3}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:45:56,571 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 15:45:56,576 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:45:56,577 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:45:56,577 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-10 15:45:56,577 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:45:56,747 INFO     29 [qwen-vl-table] page=13, rect=842x595, img=(2339x1653)
2026-08-10 15:45:56,747 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:45:56,748 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 278, \"bbox_end\": 331, \"encounter_dates\": [\"2026-03-05\", \"2025-12-07\", \"2025-12-08\", \"2025-09-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllllllll}\n报告时间: 2026-03-05\n\\hline\n五分类法) & 2026-03-05 11:08:21 & 异常报告 & 王辉 & 全 & 缩写 & 项目名称 & 结果 & 扩展结果 & 异常提示 & 多耐标志 & 辅助诊断 & 单位 & 参考范围 & 历次 \\\\\n\\hline\n项+肝功能八项+白蛋 & 2026-03-05 13:50:21 & 异常报告 & 王辉 & 血 & WBC & 白细胞计数 & 6.47 & & & & & 10^9/L & 3.5-9.5 & 4.94 \\\\\n\\hline\n& 2026-03-05 14:44:11 & 异常报告 & 王辉 & 血 & RBC & 红细胞计数 & 6.90 & & H & & & 10^12/L & 4.3-5.8 & 6.56 \\\\\n\\hline\n五分类法) & 2025-12-07 09:31:31 & 异常报告 & 王辉 & 全 & HGB & 血红蛋白 & 133 & & & & & g/L & 130-175 & 127 \\\\\n\\hline\n项+肝功能八项+白蛋 & 2025-12-07 10:49:11 & 异常报告 & 王辉 & 血 & PLT & 血小板计数 & 142 & & & & & 10^9/L & 125-350 & 137 \\\\\n\\hline\n& 2025-12-08 09:35:51 & 异常报告 & 王辉 & 血 & NEUT\\% & 中性粒细胞百分比 & 70.3 & & & & & \\% & 40-75 & 64.0 \\\\\n\\hline\n状腺激素(FT3,FT4,促甲) & 2025-09-21 12:48:01 & 正常报告 & 王辉 & 血 & LYM\\% & 淋巴细胞百分比 & 19.5 & & L & & & \\% & 20-50 & 24.9 \\\\\n\\hline\n& 2025-09-21 13:27:11 & 异常报告 & 王辉 & 血 & MONO\\% & 单核细胞百分比 & 9.4 & & & & & \\% & 3-10 & 10.1 \\\\\n\\hline\n& & & & & EO\\% & 嗜酸性粒细胞百分比 & 0.50 & & & & & \\% & 0.4-8 & 0.80 \\\\\n\\hline\n& & & & & BASO\\% & 嗜碱性粒细胞百分比 & 0.3 & & & & & \\% & 0-1 & 0.2 \\\\\n\\hline\n& & & & & NEUT\\# & 中性粒细胞绝对值 & 4.55 & & & & & 10^9/L & 2-7 & 3.16 \\\\\n\\hline\n& & & & & LYM\\# & 淋巴细胞绝对值 & 1.26 & & L & & & 10^9/L & 1.5-4 & 1.23 \\\\\n\\hline\n& & & & & MONO\\# & 单核细胞绝对值 & 0.61 & & H & & & 10^9/L & 0-0.5 & 0.50 \\\\\n\\hline\n& & & & & EO\\# & 嗜酸性粒细胞绝对值 & 0.03 & & L & & & 10^9/L & 0.1-0.4 & 0.04 \\\\\n\\hline\n& & & & & BASO\\# & 嗜碱性粒细胞绝对值 & 0.02 & & & & & 10^9/L & 0-0.07 & 0.01 \\\\\n\\hline\n& & & & & HCT & 红细胞压积 & 44.80 & & & & & \\% & 40-50 & 43.40 \\\\\n\\hline\n& & & & & MCV & 平均红细胞体积 & 64.9 & & L & & & fL & 82-100 & 66.2 \\\\\n\\hline\n& & & & & MCH & 平均红细胞Hb含量 & 19.3 & & L & & & pg & 27-34 & 19.4 \\\\\n\\hline\n& & & & & MCHC & 平均红细胞Hb浓度 & 297 & & L & & & g/L & 316-354 & 293 \\\\\n\\hline\n& & & & & RDW-CV & 红细胞分布宽度(CV) & 18.4 & & H & & & \\% & 10.9-15.4 & 17.0 \\\\\n\\hline\n& & & & & RDW-SD & 红细胞分布宽度(SD) & 37.9 & & L & & & fl & 39-46 & 34.5 \\\\\n\\hline\n& & & & & PCT & 血小板压积 & ---- & & & & & \\% & 0.1-0.28 & ---- \\\\\n\\hline\n& & & & & PDW & 血小板分布宽度 & ---- & & & & & fl & 11-26.5 & ---- \\\\\n\\hline\n& & & & & MPV & 平均血小板体积 & ---- & & & & & fL & 7.6-13.2 & ---- \\\\\n\\hline\n& & & & & P-LCR & 十血小板比值 & ---- & & & & & \\% & 13-43 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:46:00,089 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:46:00.087+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:46:09,755 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:09,755 INFO     29 [qwen-vl-table] page=13 LLM output (len=4074):
{
  "report_date": "2026-03-05",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "6.47",
      "unit": "10^9/L",
      "reference_range": "3.5-9.5",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "6.90",
      "unit": "10^12/L",
      "reference_range": "4.3-5.8",
      "abnormal": true
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "133",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "142",
      "unit": "10^9/L",
      "reference_range": "125-350",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "NEUT%",
      "value": "70.3",
      "unit": "%",
      "reference_range": "40-75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "LYM%",
      "value": "19.5",
      "unit": "%",
      "reference_range": "20-50",
      "abnormal": true
    },
    {
      "name": "单核细胞百分比",
      "item_code": "MONO%",
      "value": "9.4",
      "unit": "%",
      "reference_range": "3-10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分比",
      "item_code": "EO%",
      "value": "0.50",
      "unit": "%",
      "reference_range": "0.4-8",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分比",
      "item_code": "BASO%",
      "value": "0.3",
      "unit": "%",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NEUT#",
      "value": "4.55",
      "unit": "10^9/L",
      "reference_range": "2-7",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LYM#",
      "value": "1.26",
      "unit": "10^9/L",
      "reference_range": "1.5-4",
      "abnormal": true
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MONO#",
      "value": "0.61",
      "unit": "10^9/L",
      "reference_range": "0-0.5",
      "abnormal": true
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": "EO#",
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0.1-0.4",
      "abnormal": true
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": "BASO#",
      "value": "0.02",
      "unit": "10^9/L",
      "reference_range": "0-0.07",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "44.80",
      "unit": "%",
      "reference_range": "40-50",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "64.9",
      "unit": "fL",
      "reference_range": "82-100",
      "abnormal": true
    },
    {
      "name": "平均红细胞Hb含量",
      "item_code": "MCH",
      "value": "19.3",
      "unit": "pg",
      "reference_range": "27-34",
      "abnormal": true
    },
    {
      "name": "平均红细胞Hb浓度",
      "item_code": "MCHC",
      "value": "297",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度(CV)",
      "item_code": "RDW-CV",
      "value": "18.4",
      "unit": "%",
      "reference_range": "10.9-15.4",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度(SD)",
      "item_code": "RDW-SD",
      "value": "37.9",
      "unit": "fl",
      "reference_range": "39-46",
      "abnormal": true
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "----",
      "unit": "%",
      "reference_range": "0.1-0.28",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "----",
      "unit": "fl",
      "reference_range": "11-26.5",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "----",
      "unit": "fL",
      "reference_range": "7.6-13.2",
      "abnormal": false
    },
    {
      "name": "十血小板比值",
      "item_code": "P-LCR",
      "value": "----",
      "unit": "%",
      "reference_range": "13-43",
      "abnormal": false
    }
  ]
}
2026-08-10 15:46:09,755 INFO     29 [qwen-vl-table] coord grouping: {13: 24}
2026-08-10 15:46:09,758 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1298281, prompt_len=706
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、红细胞计数、血红蛋白、血小板计数、中性粒细胞百分比、淋巴细胞百分比、单核细胞百分比、嗜酸性粒细胞百分比、嗜碱性粒细胞百分比、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、红细胞压积、平均红细胞体积、平均红细胞Hb含量、平均红细胞Hb浓度、红细胞分布宽度(CV)、红细胞分布宽度(SD)、血小板压积、血小板分布宽度、平均血小板体积、十血小板比值

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
2026-08-10 15:46:17,718 INFO     29 [qwen-vl-table] coord API raw response (len=1258):
[
	{"text": "白细胞计数", "bbox": [418, 112, 466, 126]},
	{"text": "红细胞计数", "bbox": [418, 143, 466, 157]},
	{"text": "血红蛋白", "bbox": [424, 172, 462, 186]},
	{"text": "血小板计数", "bbox": [418, 203, 466, 217]},
	{"text": "中性粒细胞百分比", "bbox": [405, 234, 481, 248]},
	{"text": "淋巴细胞百分比", "bbox": [409, 264, 476, 278]},
	{"text": "单核细胞百分比", "bbox": [409, 295, 476, 309]},
	{"text": "嗜酸性粒细胞百分比", "bbox": [405, 319, 481, 333]},
	{"text": "嗜碱性粒细胞百分比", "bbox": [405, 351, 481, 365]},
	{"text": "中性粒细胞绝对值", "bbox": [405, 390, 481, 404]},
	{"text": "淋巴细胞绝对值", "bbox": [409, 420, 476, 434]},
	{"text": "单核细胞绝对值", "bbox": [409, 450, 476, 464]},
	{"text": "嗜酸性粒细胞绝对值", "bbox": [405, 473, 481, 487]},
	{"text": "嗜碱性粒细胞绝对值", "bbox": [405, 505, 481, 519]},
	{"text": "红细胞压积", "bbox": [418, 545, 466, 559]},
	{"text": "平均红细胞体积", "bbox": [410, 575, 477, 589]},
	{"text": "平均红细胞Hb含量", "bbox": [409, 600, 477, 628]},
	{"text": "平均红细胞Hb浓度", "bbox": [409, 632, 477, 660]},
	{"text": "红细胞分布宽度(CV)", "bbox": [409, 667, 477, 695]},
	{"text": "红细胞分布宽度(SD)", "bbox": [409, 698, 477, 726]},
	{"text": "血小板压积", "bbox": [420, 737, 468, 751]},
	{"text": "血小板分布宽度", "bbox": [410, 767, 477, 781]},
	{"text": "平均血小板体积", "bbox": [410, 797, 477, 811]},
	{"text": "十血小板比值", "bbox": [416, 827, 473, 841]}
]
2026-08-10 15:46:17,718 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=8.0s
2026-08-10 15:46:17,718 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[418, 112, 466, 126]
2026-08-10 15:46:17,718 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞计数, bbox=[418, 143, 466, 157]
2026-08-10 15:46:17,718 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白, bbox=[424, 172, 462, 186]
2026-08-10 15:46:17,718 INFO     29 [qwen-vl-table] coord item[3]: text=血小板计数, bbox=[418, 203, 466, 217]
2026-08-10 15:46:17,718 INFO     29 [qwen-vl-table] coord item[4]: text=中性粒细胞百分比, bbox=[405, 234, 481, 248]
2026-08-10 15:46:17,718 INFO     29 [qwen-vl-table] coord item[5]: text=淋巴细胞百分比, bbox=[409, 264, 476, 278]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[6]: text=单核细胞百分比, bbox=[409, 295, 476, 309]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[7]: text=嗜酸性粒细胞百分比, bbox=[405, 319, 481, 333]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[8]: text=嗜碱性粒细胞百分比, bbox=[405, 351, 481, 365]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[9]: text=中性粒细胞绝对值, bbox=[405, 390, 481, 404]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[10]: text=淋巴细胞绝对值, bbox=[409, 420, 476, 434]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[11]: text=单核细胞绝对值, bbox=[409, 450, 476, 464]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[12]: text=嗜酸性粒细胞绝对值, bbox=[405, 473, 481, 487]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[13]: text=嗜碱性粒细胞绝对值, bbox=[405, 505, 481, 519]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞压积, bbox=[418, 545, 466, 559]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞体积, bbox=[410, 575, 477, 589]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[16]: text=平均红细胞Hb含量, bbox=[409, 600, 477, 628]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[17]: text=平均红细胞Hb浓度, bbox=[409, 632, 477, 660]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度(CV), bbox=[409, 667, 477, 695]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[19]: text=红细胞分布宽度(SD), bbox=[409, 698, 477, 726]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[20]: text=血小板压积, bbox=[420, 737, 468, 751]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[21]: text=血小板分布宽度, bbox=[410, 767, 477, 781]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[22]: text=平均血小板体积, bbox=[410, 797, 477, 811]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] coord item[23]: text=十血小板比值, bbox=[416, 827, 473, 841]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] page=13 coord: matched 24/24, time=8.0s
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] new_positions (24):
[[14, 351.95599999999996, 392.372, 66.64, 74.97], [14, 351.95599999999996, 392.372, 85.085, 93.41499999999999], [14, 357.008, 389.00399999999996, 102.33999999999999, 110.67], [14, 351.95599999999996, 392.372, 120.785, 129.11499999999998], [14, 341.01, 405.002, 139.23, 147.56], [14, 344.378, 400.792, 157.07999999999998, 165.41], [14, 344.378, 400.792, 175.525, 183.855], [14, 341.01, 405.002, 189.80499999999998, 198.135], [14, 341.01, 405.002, 208.845, 217.17499999999998], [14, 341.01, 405.002, 232.04999999999998, 240.38], [14, 344.378, 400.792, 249.89999999999998, 258.22999999999996], [14, 344.378, 400.792, 267.75, 276.08], [14, 341.01, 405.002, 281.435, 289.765], [14, 341.01, 405.002, 300.47499999999997, 308.805], [14, 351.95599999999996, 392.372, 324.275, 332.60499999999996], [14, 345.21999999999997, 401.63399999999996, 342.125, 350.455], [14, 344.378, 401.63399999999996, 357.0, 373.65999999999997], [14, 344.378, 401.63399999999996, 376.03999999999996, 392.7], [14, 344.378, 401.63399999999996, 396.865, 413.525], [14, 344.378, 401.63399999999996, 415.31, 431.96999999999997], [14, 353.64, 394.056, 438.515, 446.84499999999997], [14, 345.21999999999997, 401.63399999999996, 456.36499999999995, 464.695], [14, 345.21999999999997, 401.63399999999996, 474.215, 482.54499999999996], [14, 350.272, 398.26599999999996, 492.065, 500.395]]
2026-08-10 15:46:17,719 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=24, matched=24, pages=1, time=21.1s
2026-08-10 15:46:17,720 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:46:17,721 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:46:17,721 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[14]
2026-08-10 15:46:17,721 INFO     29 [qwen-vl-table] positions ： [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:46:17,875 INFO     29 [qwen-vl-table] page=14, rect=842x595, img=(2339x1653)
2026-08-10 15:46:17,875 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:17,876 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 332, \"bbox_end\": 367, \"encounter_dates\": [\"2026-03-05\", \"2025-12-07\", \"2025-12-08\", \"2025-09-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|}\n报告时间: 2026-03-05\n\\hline\n\\textbf{报告日期} & \\textbf{报告状态} & \\textbf{姓名} & \\textbf{阅读} & \\textbf{标} & \\textbf{缩写} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{扩展结果} & \\textbf{异常提示} & \\textbf{多耐标志} & \\textbf{辅助诊断} & \\textbf{单位} & \\textbf{参考范} \\\\\n\\hline\n2026-03-05 11:08:21 & \\textcolor{red}{异常报告} & 王腊 & & 全 & TP & 总蛋白 & 77.80 & & & & & g/L & 65-8 \\\\\n\\hline\n2026-03-05 13:50:21 & \\textcolor{red}{异常报告} & 王腊 & & 血 & ALB & 白蛋白 & 42.70 & & & & & g/L & 40-5 \\\\\n\\hline\n2026-03-05 14:44:11 & \\textcolor{red}{异常报告} & 王腊 & & 血 & GLB & 球蛋白 & 35.10 & & & & & g/L & 20-4 \\\\\n\\hline\n2025-12-07 09:31:31 & \\textcolor{red}{异常报告} & 王腊 & & 全 & A/G & 白球比例 & 1.22 & & & & & & 1.2- \\\\\n\\hline\n2025-12-07 10:49:11 & \\textcolor{red}{异常报告} & 王腊 & & 血 & TBIL & 总胆红素 & 31.70 & & H & & & \\textmu mol/L & 0-20 \\\\\n\\hline\n2025-12-08 09:35:51 & \\textcolor{red}{异常报告} & 王腊 & & 血 & DBIL & 直接胆红素 & 13.30 & & H & & & \\textmu mol/L & 0-6. \\\\\n\\hline\n2025-09-21 12:48:01 & 正常报告 & 王腊 & & 血 & IBIL & 间接胆红素 & 18.40 & & H & & & \\textmu mol/L & 0-18 \\\\\n\\hline\n2025-09-21 13:27:11 & \\textcolor{red}{异常报告} & 王腊 & & 血 & AST & 天门冬氨酸氨基转移酶 & 89.00 & & H & & & U/L & 15- \\\\\n\\hline\n& & & & & ALT & 丙氨酸氨基转移酶 & 54.30 & & H & & & U/L & 9- \\\\\n\\hline\n& & & & & ALP & 碱性磷酸酶 & 224.00 & & H & & & U/L & 45- \\\\\n\\hline\n& & & & & \\textgamma-GT & \\textgamma-谷氨酰基转移酶 & 495.90 & & H & & & U/L & 10 \\\\\n\\hline\n& & & & & UREA & 尿素 & 4.25 & & & & & mmol/L & 3.1 \\\\\n\\hline\n& & & & & Cre & 肌酐 & 69.80 & & & & & \\textmu mol/L & 57 \\\\\n\\hline\n& & & & & eGFR & 估算肾小球滤过率 & 107.16 & & & & & & 仅适用 \\\\\n\\hline\n& & & & & URIC & 尿酸 & 315.40 & & & & & \\textmu mol/L & 208 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:46:26,677 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:26,677 INFO     29 [qwen-vl-table] page=14 LLM output (len=2549):
{
  "report_date": "2026-03-05",
  "items": [
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "77.80",
      "unit": "g/L",
      "reference_range": "65-8",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "42.70",
      "unit": "g/L",
      "reference_range": "40-5",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLB",
      "value": "35.10",
      "unit": "g/L",
      "reference_range": "20-4",
      "abnormal": false
    },
    {
      "name": "白球比例",
      "item_code": "A/G",
      "value": "1.22",
      "unit": null,
      "reference_range": "1.2-",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "31.70",
      "unit": "\u00b5mol/L",
      "reference_range": "0-20",
      "abnormal": true
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "13.30",
      "unit": "\u00b5mol/L",
      "reference_range": "0-6.",
      "abnormal": true
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "18.40",
      "unit": "\u00b5mol/L",
      "reference_range": "0-18",
      "abnormal": true
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": "AST",
      "value": "89.00",
      "unit": "U/L",
      "reference_range": "15-",
      "abnormal": true
    },
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": "ALT",
      "value": "54.30",
      "unit": "U/L",
      "reference_range": "9-",
      "abnormal": true
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "224.00",
      "unit": "U/L",
      "reference_range": "45-",
      "abnormal": true
    },
    {
      "name": "\u03b3-谷氨酰基转移酶",
      "item_code": "\u03b3-GT",
      "value": "495.90",
      "unit": "U/L",
      "reference_range": "10",
      "abnormal": true
    },
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "4.25",
      "unit": "mmol/L",
      "reference_range": "3.1",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": "Cre",
      "value": "69.80",
      "unit": "\u00b5mol/L",
      "reference_range": "57",
      "abnormal": false
    },
    {
      "name": "估算肾小球滤过率",
      "item_code": "eGFR",
      "value": "107.16",
      "unit": null,
      "reference_range": "仅适用",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "URIC",
      "value": "315.40",
      "unit": "\u00b5mol/L",
      "reference_range": "208",
      "abnormal": false
    }
  ]
}
2026-08-10 15:46:26,677 INFO     29 [qwen-vl-table] coord grouping: {14: 15}
2026-08-10 15:46:26,679 INFO     29 [qwen-vl-table] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=936805, prompt_len=594
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
总蛋白、白蛋白、球蛋白、白球比例、总胆红素、直接胆红素、间接胆红素、天门冬氨酸氨基转移酶、丙氨酸氨基转移酶、碱性磷酸酶、γ-谷氨酰基转移酶、尿素、肌酐、估算肾小球滤过率、尿酸

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
2026-08-10 15:46:31,325 INFO     29 [qwen-vl-table] coord API raw response (len=750):
[
	{"text": "总蛋白", "bbox": [438, 217, 472, 234]},
	{"text": "白蛋白", "bbox": [438, 252, 472, 269]},
	{"text": "球蛋白", "bbox": [438, 286, 472, 303]},
	{"text": "白球比例", "bbox": [432, 321, 477, 338]},
	{"text": "总胆红素", "bbox": [432, 356, 477, 373]},
	{"text": "直接胆红素", "bbox": [427, 390, 483, 407]},
	{"text": "间接胆红素", "bbox": [427, 424, 483, 441]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [410, 452, 498, 469]},
	{"text": "丙氨酸氨基转移酶", "bbox": [410, 495, 498, 512]},
	{"text": "碱性磷酸酶", "bbox": [427, 530, 483, 547]},
	{"text": "γ-谷氨酰基转移酶", "bbox": [410, 565, 498, 582]},
	{"text": "尿素", "bbox": [443, 600, 467, 617]},
	{"text": "肌酐", "bbox": [443, 635, 467, 652]},
	{"text": "估算肾小球滤过率", "bbox": [410, 670, 498, 687]},
	{"text": "尿酸", "bbox": [443, 705, 467, 722]}
]
2026-08-10 15:46:31,325 INFO     29 [qwen-vl-table] coord API: raw_items=15, valid_items=15, elapsed=4.6s
2026-08-10 15:46:31,325 INFO     29 [qwen-vl-table] coord item[0]: text=总蛋白, bbox=[438, 217, 472, 234]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[1]: text=白蛋白, bbox=[438, 252, 472, 269]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[2]: text=球蛋白, bbox=[438, 286, 472, 303]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[3]: text=白球比例, bbox=[432, 321, 477, 338]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[4]: text=总胆红素, bbox=[432, 356, 477, 373]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[5]: text=直接胆红素, bbox=[427, 390, 483, 407]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[6]: text=间接胆红素, bbox=[427, 424, 483, 441]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[7]: text=天门冬氨酸氨基转移酶, bbox=[410, 452, 498, 469]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[8]: text=丙氨酸氨基转移酶, bbox=[410, 495, 498, 512]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[9]: text=碱性磷酸酶, bbox=[427, 530, 483, 547]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[10]: text=γ-谷氨酰基转移酶, bbox=[410, 565, 498, 582]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[11]: text=尿素, bbox=[443, 600, 467, 617]
2026-08-10 15:46:31,326 INFO     29 [qwen-vl-table] coord item[12]: text=肌酐, bbox=[443, 635, 467, 652]
2026-08-10 15:46:31,327 INFO     29 [qwen-vl-table] coord item[13]: text=估算肾小球滤过率, bbox=[410, 670, 498, 687]
2026-08-10 15:46:31,327 INFO     29 [qwen-vl-table] coord item[14]: text=尿酸, bbox=[443, 705, 467, 722]
2026-08-10 15:46:31,327 INFO     29 [qwen-vl-table] page=14 coord: matched 15/15, time=4.6s
2026-08-10 15:46:31,327 INFO     29 [qwen-vl-table] new_positions (15):
[[15, 368.796, 397.424, 129.11499999999998, 139.23], [15, 368.796, 397.424, 149.94, 160.055], [15, 368.796, 397.424, 170.17, 180.285], [15, 363.74399999999997, 401.63399999999996, 190.995, 201.10999999999999], [15, 363.74399999999997, 401.63399999999996, 211.82, 221.935], [15, 359.534, 406.686, 232.04999999999998, 242.165], [15, 359.534, 406.686, 252.28, 262.395], [15, 345.21999999999997, 419.316, 268.94, 279.055], [15, 345.21999999999997, 419.316, 294.525, 304.64], [15, 359.534, 406.686, 315.34999999999997, 325.465], [15, 345.21999999999997, 419.316, 336.175, 346.28999999999996], [15, 373.006, 393.214, 357.0, 367.115], [15, 373.006, 393.214, 377.825, 387.94], [15, 345.21999999999997, 419.316, 398.65, 408.765], [15, 373.006, 393.214, 419.47499999999997, 429.59]]
2026-08-10 15:46:31,327 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=15, matched=15, pages=1, time=13.6s
2026-08-10 15:46:31,329 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:46:31,331 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:46:31,332 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[15]
2026-08-10 15:46:31,332 INFO     29 [qwen-vl-table] positions ： [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:46:31,477 INFO     29 [qwen-vl-table] page=15, rect=842x595, img=(2339x1653)
2026-08-10 15:46:31,477 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:31,478 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 368, \"bbox_end\": 382, \"encounter_dates\": [\"2026-03-05\", \"2025-12-07\", \"2025-12-08\", \"2025-09-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccccc}\n报告时间: 2026-03-05\n\\hline\n\\multicolumn{1}{c}{报告日期} & \\multicolumn{1}{c}{报告状态} & \\multicolumn{1}{c}{姓名} & \\multicolumn{1}{c}{阅读} & \\multicolumn{1}{c}{标} & \\multicolumn{1}{c}{缩写} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{扩展结果} & \\multicolumn{1}{c}{异常提示} & \\multicolumn{1}{c}{多瘤标志} & \\multicolumn{1}{c}{辅助诊断} & \\multicolumn{1}{c}{单位} & \\multicolumn{1}{c}{参考范围} \\\\\n\\hline\n2026-03-05 11:08:21 & 异常报告 & 王雄 & & 全 & AFP & 甲胎蛋白测定 & >240000.00 & & H & & & ng/ml & 0-7 \\\\\n2026-03-05 13:50:21 & 异常报告 & 王雄 & & 血 & AFP-L3 & 甲胎蛋白异质体L3测定 & 53777.00 & & H & & & ng/ml & 0-1 \\\\\n2026-03-05 14:44:11 & 异常报告 & 王雄 & & 血 & DCP & 异常凝血酶原测定 & >20000.00 & & H & & & ng/ml & 0-40 \\\\\n2025-12-07 09:31:31 & 异常报告 & 王雄 & & 全 & AFP-L3\\% & 甲胎蛋白异质体比率(L3\\%) & >10\\% & & H & & & & 0-10\\% \\\\\n2025-12-07 10:49:11 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\\\\n2025-12-08 09:35:51 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\\\\n2025-09-21 12:48:01 & 正常报告 & 王雄 & & 血 & C-GALAD & 肝癌辅助分析评分 & 99.91 & & & & & & 54以下偏低风险;54-66为肝部疾病中风险;>66判定偏高风险 \\\\\n2025-09-21 13:27:11 & 异常报告 & 王雄 & & 血 & & & & & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:46:31,480 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:46:31.479+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:46:35,020 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:35,021 INFO     29 [qwen-vl-table] page=15 LLM output (len=941):
{
  "report_date": "2026-03-05",
  "items": [
    {
      "name": "甲胎蛋白测定",
      "item_code": "AFP",
      "value": ">240000.00",
      "unit": "ng/ml",
      "reference_range": "0-7",
      "abnormal": true
    },
    {
      "name": "甲胎蛋白异质体L3测定",
      "item_code": "AFP-L3",
      "value": "53777.00",
      "unit": "ng/ml",
      "reference_range": "0-1",
      "abnormal": true
    },
    {
      "name": "异常凝血酶原测定",
      "item_code": "DCP",
      "value": ">20000.00",
      "unit": "ng/ml",
      "reference_range": "0-40",
      "abnormal": true
    },
    {
      "name": "甲胎蛋白异质体比率(L3%)",
      "item_code": "AFP-L3%",
      "value": ">10%",
      "unit": null,
      "reference_range": "0-10%",
      "abnormal": true
    },
    {
      "name": "肝癌辅助分析评分",
      "item_code": "C-GALAD",
      "value": "99.91",
      "unit": null,
      "reference_range": "54以下偏低风险;54-66为肝部疾病中风险;>66判定偏高风险",
      "abnormal": false
    }
  ]
}
2026-08-10 15:46:35,021 INFO     29 [qwen-vl-table] coord grouping: {15: 5}
2026-08-10 15:46:35,022 INFO     29 [qwen-vl-table] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=784496, prompt_len=558
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
甲胎蛋白测定、甲胎蛋白异质体L3测定、异常凝血酶原测定、甲胎蛋白异质体比率(L3%)、肝癌辅助分析评分

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
2026-08-10 15:46:37,571 INFO     29 [qwen-vl-table] coord API raw response (len=286):
```json
[
	{"text": "甲胎蛋白测定", "bbox": [362, 255, 427, 273]},
	{"text": "甲胎蛋白异质体L3测定", "bbox": [351, 282, 437, 317]},
	{"text": "异常凝血酶原测定", "bbox": [352, 329, 438, 347]},
	{"text": "甲胎蛋白异质体比率(L3%)", "bbox": [352, 357, 438, 391]},
	{"text": "肝癌辅助分析评分", "bbox": [352, 430, 437, 448]}
]
```
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=2.5s
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] coord item[0]: text=甲胎蛋白测定, bbox=[362, 255, 427, 273]
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] coord item[1]: text=甲胎蛋白异质体L3测定, bbox=[351, 282, 437, 317]
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] coord item[2]: text=异常凝血酶原测定, bbox=[352, 329, 438, 347]
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] coord item[3]: text=甲胎蛋白异质体比率(L3%), bbox=[352, 357, 438, 391]
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] coord item[4]: text=肝癌辅助分析评分, bbox=[352, 430, 437, 448]
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] page=15 coord: matched 5/5, time=2.5s
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] new_positions (5):
[[16, 304.804, 359.534, 151.725, 162.435], [16, 295.542, 367.954, 167.79, 188.61499999999998], [16, 296.384, 368.796, 195.755, 206.465], [16, 296.384, 368.796, 212.415, 232.64499999999998], [16, 296.384, 367.954, 255.85, 266.56]]
2026-08-10 15:46:37,572 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=5, matched=5, pages=1, time=6.2s
2026-08-10 15:46:37,583 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 15:46:37,583 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:LabExam | outputs={"chunks": "3 items, types={'LabReport': 3}", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:46:37,583 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 15:46:37,593 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:37,593 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:46:38,402 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:38,408 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 15:46:38,408 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:46:38,408 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 15:46:38,415 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:46:38,416 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:46:38,416 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 15:46:38,417 INFO     29 [qwen-vl-text] positions(19): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:46:38,417 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [19]
2026-08-10 15:46:38,571 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:46:38,572 INFO     29 [qwen-vl-text] LLM extraction start, text_len=393
2026-08-10 15:46:38,572 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:38,573 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 28, \"bbox_end\": 46, \"encounter_dates\": [\"2025-12-07\"], \"department\": \"红角洲肝胆外科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "工作单位或地址:湾里区\n就诊科室:红角洲肝胆外科门诊\n就诊时间:2025年12月07日 08:46\n药物过敏史:无\n主诉:肝Ca综合治疗后半年返院复查。\n病史:肝Ca综合治疗后半年复查。未诉特殊不适。\n既往史和其他病史:既往半年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。\n体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。\n助检查:暂缺。\n诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿\n靶向治疗;4.恶性肿瘤免疫治疗\n理:1.胸部CT平扫\n上腹部薄层CT平扫+增强扫描\n肝癌三项:肝功能八项+白蛋白;血常规(五分类法);肾功能3项\n碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶\n用法:每次30g即时造影用1天\nCT静脉注药(留置针置管)每次1项\n转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院\n医生签名:",
    "role": "user"
  }
]
2026-08-10 15:46:41,196 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:41,196 INFO     29 [qwen-vl-text] LLM output (len=561):
{
  "encounter_date": "2025-12-07",
  "chief_complaint": "肝Ca综合治疗后半年返院复查。",
  "present_illness": "肝Ca综合治疗后半年复查。未诉特殊不适。",
  "past_history": "既往半年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。",
  "diagnosis": "1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿靶向治疗;4.恶性肿瘤免疫治疗",
  "treatment_plan": [
    {
      "name": "碘海醇注射液(基)[100ml:30g](广东阿哌集采)",
      "dosage": "30g",
      "frequency": "1天",
      "route": "即时造影用",
      "quantity": "1瓶"
    },
    {
      "name": "CT静脉注药(留置针置管)",
      "dosage": "1项",
      "frequency": "每次",
      "route": null,
      "quantity": null
    }
  ]
}
2026-08-10 15:46:41,196 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-07]
2026-08-10 15:46:41,198 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=861386, prompt_len=1063
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["工作单位或地址:湾里区", "就诊科室:红角洲肝胆外科门诊", "就诊时间:2025年12月07日 08:46", "药物过敏史:无", "主诉:肝Ca综合治疗后半年返院复查。", "病史:肝Ca综合治疗后半年复查。未诉特殊不适。", "既往史和其他病史:既往半年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。", "体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。", "助检查:暂缺。", "诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿", "靶向治疗;4.恶性肿瘤免疫治疗", "理:1.胸部CT平扫", "上腹部薄层CT平扫+增强扫描", "肝癌三项:肝功能八项+白蛋白;血常规(五分类法);肾功能3项", "碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶", "用法:每次30g即时造影用1天", "CT静脉注药(留置针置管)每次1项", "转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院", "医生签名:"]

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
2026-08-10 15:46:51,012 INFO     29 [qwen-vl-text] coord API raw response (len=1226):
[
	{"text": "工作单位或地址:湾里区", "bbox": [151, 25, 364, 54]},
	{"text": "就诊科室:红角洲肝胆外科门诊", "bbox": [151, 67, 417, 96]},
	{"text": "就诊时间:2025年12月07日 08:46", "bbox": [507, 67, 808, 96]},
	{"text": "药物过敏史:无", "bbox": [151, 111, 280, 140]},
	{"text": "主诉:肝Ca综合治疗后半年返院复查。", "bbox": [151, 154, 480, 183]},
	{"text": "病史:肝Ca综合治疗后半年复查。未诉特殊不适。", "bbox": [151, 197, 603, 226]},
	{"text": "既往史和其他病史:既往半年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。", "bbox": [151, 240, 816, 269]},
	{"text": "体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。", "bbox": [157, 285, 626, 314]},
	{"text": "助检查:暂缺。", "bbox": [160, 327, 300, 356]},
	{"text": "诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿", "bbox": [160, 370, 837, 400]},
	{"text": "靶向治疗;4.恶性肿瘤免疫治疗", "bbox": [157, 412, 433, 441]},
	{"text": "理:1.胸部CT平扫", "bbox": [160, 457, 338, 486]},
	{"text": "上腹部薄层CT平扫+增强扫描", "bbox": [169, 497, 421, 526]},
	{"text": "肝癌三项:肝功能八项+白蛋白;血常规(五分类法);肾功能3项", "bbox": [168, 539, 737, 569]},
	{"text": "碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶", "bbox": [168, 582, 645, 611]},
	{"text": "用法:每次30g即时造影用1天", "bbox": [168, 625, 493, 655]},
	{"text": "CT静脉注药(留置针置管)每次1项", "bbox": [160, 668, 493, 697]},
	{"text": "转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院", "bbox": [160, 754, 772, 784]},
	{"text": "医生签名:", "bbox": [503, 820, 598, 850]}
]
2026-08-10 15:46:51,012 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=9.8s
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[0]: text=工作单位或地址:湾里区, bbox=[151, 25, 364, 54]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[1]: text=就诊科室:红角洲肝胆外科门诊, bbox=[151, 67, 417, 96]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[2]: text=就诊时间:2025年12月07日 08:46, bbox=[507, 67, 808, 96]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[3]: text=药物过敏史:无, bbox=[151, 111, 280, 140]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[4]: text=主诉:肝Ca综合治疗后半年返院复查。, bbox=[151, 154, 480, 183]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[5]: text=病史:肝Ca综合治疗后半年复查。未诉特殊不适。, bbox=[151, 197, 603, 226]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[6]: text=既往史和其他病史:既往半年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。, bbox=[151, 240, 816, 269]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[7]: text=体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。, bbox=[157, 285, 626, 314]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[8]: text=助检查:暂缺。, bbox=[160, 327, 300, 356]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[9]: text=诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿, bbox=[160, 370, 837, 400]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[10]: text=靶向治疗;4.恶性肿瘤免疫治疗, bbox=[157, 412, 433, 441]
2026-08-10 15:46:51,013 INFO     29 [qwen-vl-text] coord item[11]: text=理:1.胸部CT平扫, bbox=[160, 457, 338, 486]
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] coord item[12]: text=上腹部薄层CT平扫+增强扫描, bbox=[169, 497, 421, 526]
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] coord item[13]: text=肝癌三项:肝功能八项+白蛋白;血常规(五分类法);肾功能3项, bbox=[168, 539, 737, 569]
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] coord item[14]: text=碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶, bbox=[168, 582, 645, 611]
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] coord item[15]: text=用法:每次30g即时造影用1天, bbox=[168, 625, 493, 655]
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] coord item[16]: text=CT静脉注药(留置针置管)每次1项, bbox=[160, 668, 493, 697]
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] coord item[17]: text=转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院, bbox=[160, 754, 772, 784]
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] coord item[18]: text=医生签名:, bbox=[503, 820, 598, 850]
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] page=1 — 19/19 coords, api_time=9.8s
2026-08-10 15:46:51,014 INFO     29 [qwen-vl-text] new_positions (19):
[[1, 127.142, 306.488, 14.875, 32.129999999999995], [1, 127.142, 351.114, 39.864999999999995, 57.12], [1, 426.894, 680.336, 39.864999999999995, 57.12], [1, 127.142, 235.76, 66.045, 83.3], [1, 127.142, 404.15999999999997, 91.63, 108.88499999999999], [1, 127.142, 507.726, 117.21499999999999, 134.47], [1, 127.142, 687.072, 142.79999999999998, 160.055], [1, 132.194, 527.092, 169.575, 186.82999999999998], [1, 134.72, 252.6, 194.565, 211.82], [1, 134.72, 704.754, 220.14999999999998, 238.0], [1, 132.194, 364.586, 245.14, 262.395], [1, 134.72, 284.596, 271.91499999999996, 289.16999999999996], [1, 142.298, 354.48199999999997, 295.715, 312.96999999999997], [1, 141.456, 620.554, 320.705, 338.555], [1, 141.456, 543.09, 346.28999999999996, 363.54499999999996], [1, 141.456, 415.106, 371.875, 389.72499999999997], [1, 134.72, 415.106, 397.46, 414.715], [1, 134.72, 650.024, 448.63, 466.47999999999996], [1, 423.526, 503.51599999999996, 487.9, 505.75]]
2026-08-10 15:46:51,015 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=12.6s
2026-08-10 15:46:51,015 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:46:51,017 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:46:51,017 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 15:46:51,018 INFO     29 [qwen-vl-text] positions(18): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:46:51,018 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [18]
2026-08-10 15:46:51,184 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:46:51,186 INFO     29 [qwen-vl-text] LLM extraction start, text_len=414
2026-08-10 15:46:51,186 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:51,186 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 47, \"bbox_end\": 64, \"encounter_dates\": [\"2026-03-05\"], \"department\": \"红角洲肝胆外科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "就诊科室:红角洲肝胆外科门诊\n就诊时间:2026年03月05日 09:51\n药物过敏史:无\n主诉:肝Ca综合治疗后1年返院评估介入治疗。\n现病史:肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。\n既往史和其他病史:既往1年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。\n查体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。\n辅助检查:暂缺。\n诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿\n瘤靶向治疗;4.恶性肿瘤免疫治疗;5.肝癌介入治疗\n处理:1.胸部CT平扫\n2.上腹部薄层CT平扫+增强扫描\n3.肝癌三项;肝功能八项+白蛋白:血常规(五分类法);肾功能3项\n4.碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶\n用法:每次30g即时造影用1天\n5.CT静脉注药(留置针置管)每次1项\n下转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院\n医生签名:",
    "role": "user"
  }
]
2026-08-10 15:46:54,068 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:46:54,068 INFO     29 [qwen-vl-text] LLM output (len=446):
{
  "encounter_date": "2026-03-05",
  "chief_complaint": "肝Ca综合治疗后1年返院评估介入治疗。",
  "present_illness": "肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。",
  "past_history": "既往1年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。",
  "diagnosis": "1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿瘤靶向治疗;4.恶性肿瘤免疫治疗;5.肝癌介入治疗",
  "treatment_plan": [
    "胸部CT平扫",
    "上腹部薄层CT平扫+增强扫描",
    "肝癌三项;肝功能八项+白蛋白:血常规(五分类法);肾功能3项",
    "碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶 用法:每次30g即时造影用1天",
    "CT静脉注药(留置针置管)每次1项"
  ]
}
2026-08-10 15:46:54,068 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-05]
2026-08-10 15:46:54,071 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=900988, prompt_len=1081
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["就诊科室:红角洲肝胆外科门诊", "就诊时间:2026年03月05日 09:51", "药物过敏史:无", "主诉:肝Ca综合治疗后1年返院评估介入治疗。", "现病史:肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。", "既往史和其他病史:既往1年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。", "查体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。", "辅助检查:暂缺。", "诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿", "瘤靶向治疗;4.恶性肿瘤免疫治疗;5.肝癌介入治疗", "处理:1.胸部CT平扫", "2.上腹部薄层CT平扫+增强扫描", "3.肝癌三项;肝功能八项+白蛋白:血常规(五分类法);肾功能3项", "4.碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶", "用法:每次30g即时造影用1天", "5.CT静脉注药(留置针置管)每次1项", "下转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院", "医生签名:"]

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
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord API raw response (len=1203):
[
	{"text": "就诊科室:红角洲肝胆外科门诊", "bbox": [146, 22, 429, 51]},
	{"text": "就诊时间:2026年03月05日 09:51", "bbox": [521, 22, 828, 51]},
	{"text": "药物过敏史:无", "bbox": [146, 68, 290, 97]},
	{"text": "主诉:肝Ca综合治疗后1年返院评估介入治疗。", "bbox": [146, 111, 567, 140]},
	{"text": "现病史:肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。", "bbox": [146, 155, 735, 184]},
	{"text": "既往史和其他病史:既往1年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。", "bbox": [146, 199, 828, 228]},
	{"text": "查体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。", "bbox": [146, 245, 645, 274]},
	{"text": "辅助检查:暂缺。", "bbox": [146, 288, 312, 317]},
	{"text": "诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿", "bbox": [146, 334, 860, 363]},
	{"text": "瘤靶向治疗;4.恶性肿瘤免疫治疗;5.肝癌介入治疗", "bbox": [146, 377, 602, 406]},
	{"text": "处理:1.胸部CT平扫", "bbox": [146, 423, 350, 452]},
	{"text": "2.上腹部薄层CT平扫+增强扫描", "bbox": [146, 465, 437, 494]},
	{"text": "3.肝癌三项;肝功能八项+白蛋白:血常规(五分类法);肾功能3项", "bbox": [146, 509, 760, 538]},
	{"text": "4.碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶", "bbox": [146, 553, 667, 582]},
	{"text": "用法:每次30g即时造影用1天", "bbox": [176, 597, 510, 626]},
	{"text": "5.CT静脉注药(留置针置管)每次1项", "bbox": [146, 641, 510, 670]},
	{"text": "下转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院", "bbox": [146, 731, 799, 760]},
	{"text": "医生签名:", "bbox": [521, 778, 750, 860]}
]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=7.0s
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[0]: text=就诊科室:红角洲肝胆外科门诊, bbox=[146, 22, 429, 51]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2026年03月05日 09:51, bbox=[521, 22, 828, 51]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[2]: text=药物过敏史:无, bbox=[146, 68, 290, 97]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[3]: text=主诉:肝Ca综合治疗后1年返院评估介入治疗。, bbox=[146, 111, 567, 140]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[4]: text=现病史:肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。, bbox=[146, 155, 735, 184]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[5]: text=既往史和其他病史:既往1年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。, bbox=[146, 199, 828, 228]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[6]: text=查体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。, bbox=[146, 245, 645, 274]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[7]: text=辅助检查:暂缺。, bbox=[146, 288, 312, 317]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[8]: text=诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿, bbox=[146, 334, 860, 363]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[9]: text=瘤靶向治疗;4.恶性肿瘤免疫治疗;5.肝癌介入治疗, bbox=[146, 377, 602, 406]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[10]: text=处理:1.胸部CT平扫, bbox=[146, 423, 350, 452]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[11]: text=2.上腹部薄层CT平扫+增强扫描, bbox=[146, 465, 437, 494]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[12]: text=3.肝癌三项;肝功能八项+白蛋白:血常规(五分类法);肾功能3项, bbox=[146, 509, 760, 538]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[13]: text=4.碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶, bbox=[146, 553, 667, 582]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[14]: text=用法:每次30g即时造影用1天, bbox=[176, 597, 510, 626]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[15]: text=5.CT静脉注药(留置针置管)每次1项, bbox=[146, 641, 510, 670]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[16]: text=下转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院, bbox=[146, 731, 799, 760]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] coord item[17]: text=医生签名:, bbox=[521, 778, 750, 860]
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] page=2 — 18/18 coords, api_time=7.0s
2026-08-10 15:47:01,034 INFO     29 [qwen-vl-text] new_positions (18):
[[2, 122.932, 361.21799999999996, 13.09, 30.345], [2, 438.68199999999996, 697.1759999999999, 13.09, 30.345], [2, 122.932, 244.17999999999998, 40.46, 57.714999999999996], [2, 122.932, 477.414, 66.045, 83.3], [2, 122.932, 618.87, 92.225, 109.47999999999999], [2, 122.932, 697.1759999999999, 118.405, 135.66], [2, 122.932, 543.09, 145.775, 163.03], [2, 122.932, 262.704, 171.35999999999999, 188.61499999999998], [2, 122.932, 724.12, 198.73, 215.98499999999999], [2, 122.932, 506.88399999999996, 224.315, 241.57], [2, 122.932, 294.7, 251.685, 268.94], [2, 122.932, 367.954, 276.675, 293.93], [2, 122.932, 639.92, 302.85499999999996, 320.11], [2, 122.932, 561.614, 329.03499999999997, 346.28999999999996], [2, 148.192, 429.41999999999996, 355.215, 372.46999999999997], [2, 122.932, 429.41999999999996, 381.395, 398.65], [2, 122.932, 672.7579999999999, 434.945, 452.2], [2, 438.68199999999996, 631.5, 462.90999999999997, 511.7]]
2026-08-10 15:47:01,035 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=10.0s
2026-08-10 15:47:01,035 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:47:01,035 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:47:01,035 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 15:47:01,035 INFO     29 [qwen-vl-text] positions(19): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:47:01,036 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [19]
2026-08-10 15:47:01,213 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:47:01,214 INFO     29 [qwen-vl-text] LLM extraction start, text_len=436
2026-08-10 15:47:01,214 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:01,214 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 65, \"bbox_end\": 83, \"encounter_dates\": [\"2026-03-07\"], \"department\": \"红角洲肝胆外科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "职业：\n出生日期：1968年01月06日\n工作单位或地址：湾里区\n就诊科室：红角洲肝胆外科门诊\n就诊时间：2026年03月07日 14:40\n药物过敏史：无\n主诉：肝Ca综合治疗后1年返院评估介入治疗。\n现病史：肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。\n既往史和其他病史：既往1年前诊断肝CA，行介入+抗肿瘤靶向+免疫治疗。\n查体：血压：/mmHg，脉搏：次/分。无特殊阳性体征。\n辅助检查：2026-03-06,上腹部薄层CT平扫+增强扫描检查意见：“肝癌”综合\n治疗后，较2025-12-07日腹部CT：肝右叶肿块较前大小相仿，无明显血供；肿\n块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大，下腔静脉癌栓形\n成；余较前相仿。\n诊断：1.肝细胞癌(BCLC B期，CNLC IIb期)；2.恶性肿瘤靶向治疗；3.恶性肿瘤\n免疫治疗；4.肝癌介入治疗；5.慢性肝炎\n处理：\n下转情况：◎不下转 ○转县级院 ○转社区卫生服务机构/乡镇卫生院\n医生签名：陈天翔",
    "role": "user"
  }
]
2026-08-10 15:47:03,329 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:03,330 INFO     29 [qwen-vl-text] LLM output (len=287):
{
  "encounter_date": "2026-03-07",
  "chief_complaint": "肝Ca综合治疗后1年返院评估介入治疗。",
  "present_illness": "肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。",
  "past_history": "既往1年前诊断肝CA，行介入+抗肿瘤靶向+免疫治疗。",
  "diagnosis": "1.肝细胞癌(BCLC B期，CNLC IIb期)；2.恶性肿瘤靶向治疗；3.恶性肿瘤免疫治疗；4.肝癌介入治疗；5.慢性肝炎",
  "treatment_plan": null
}
2026-08-10 15:47:03,330 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-07]
2026-08-10 15:47:03,335 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=979838, prompt_len=1106
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["职业：", "出生日期：1968年01月06日", "工作单位或地址：湾里区", "就诊科室：红角洲肝胆外科门诊", "就诊时间：2026年03月07日 14:40", "药物过敏史：无", "主诉：肝Ca综合治疗后1年返院评估介入治疗。", "现病史：肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。", "既往史和其他病史：既往1年前诊断肝CA，行介入+抗肿瘤靶向+免疫治疗。", "查体：血压：/mmHg，脉搏：次/分。无特殊阳性体征。", "辅助检查：2026-03-06,上腹部薄层CT平扫+增强扫描检查意见：“肝癌”综合", "治疗后，较2025-12-07日腹部CT：肝右叶肿块较前大小相仿，无明显血供；肿", "块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大，下腔静脉癌栓形", "成；余较前相仿。", "诊断：1.肝细胞癌(BCLC B期，CNLC IIb期)；2.恶性肿瘤靶向治疗；3.恶性肿瘤", "免疫治疗；4.肝癌介入治疗；5.慢性肝炎", "处理：", "下转情况：◎不下转 ○转县级院 ○转社区卫生服务机构/乡镇卫生院", "医生签名：陈天翔"]

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
2026-08-10 15:47:10,741 INFO     29 [qwen-vl-text] coord API raw response (len=1269):
[
	{"text": "职业：", "bbox": [143, 15, 197, 43]},
	{"text": "出生日期：1968年01月06日", "bbox": [529, 15, 778, 43]},
	{"text": "工作单位或地址：湾里区", "bbox": [143, 61, 377, 90]},
	{"text": "就诊科室：红角洲肝胆外科门诊", "bbox": [143, 105, 432, 134]},
	{"text": "就诊时间：2026年03月07日 14:40", "bbox": [527, 105, 845, 134]},
	{"text": "药物过敏史：无", "bbox": [143, 154, 289, 183]},
	{"text": "主诉：肝Ca综合治疗后1年返院评估介入治疗。", "bbox": [143, 199, 574, 228]},
	{"text": "现病史：肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。", "bbox": [143, 244, 748, 274]},
	{"text": "既往史和其他病史：既往1年前诊断肝CA，行介入+抗肿瘤靶向+免疫治疗。", "bbox": [143, 290, 844, 320]},
	{"text": "查体：血压：/mmHg，脉搏：次/分。无特殊阳性体征。", "bbox": [143, 337, 655, 367]},
	{"text": "辅助检查：2026-03-06,上腹部薄层CT平扫+增强扫描检查意见：“肝癌”综合", "bbox": [143, 380, 869, 410]},
	{"text": "治疗后，较2025-12-07日腹部CT：肝右叶肿块较前大小相仿，无明显血供；肿", "bbox": [143, 425, 869, 455]},
	{"text": "块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大，下腔静脉癌栓形", "bbox": [143, 470, 848, 500]},
	{"text": "成；余较前相仿。", "bbox": [143, 516, 305, 545]},
	{"text": "诊断：1.肝细胞癌(BCLC B期，CNLC IIb期)；2.恶性肿瘤靶向治疗；3.恶性肿瘤", "bbox": [143, 564, 876, 594]},
	{"text": "免疫治疗；4.肝癌介入治疗；5.慢性肝炎", "bbox": [143, 610, 502, 640]},
	{"text": "处理：", "bbox": [143, 657, 192, 685]},
	{"text": "下转情况：◎不下转 ○转县级院 ○转社区卫生服务机构/乡镇卫生院", "bbox": [143, 745, 810, 775]},
	{"text": "医生签名：陈天翔", "bbox": [524, 807, 753, 862]}
]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=7.4s
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[0]: text=职业：, bbox=[143, 15, 197, 43]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[1]: text=出生日期：1968年01月06日, bbox=[529, 15, 778, 43]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[2]: text=工作单位或地址：湾里区, bbox=[143, 61, 377, 90]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[3]: text=就诊科室：红角洲肝胆外科门诊, bbox=[143, 105, 432, 134]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间：2026年03月07日 14:40, bbox=[527, 105, 845, 134]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[5]: text=药物过敏史：无, bbox=[143, 154, 289, 183]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：肝Ca综合治疗后1年返院评估介入治疗。, bbox=[143, 199, 574, 228]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。, bbox=[143, 244, 748, 274]
2026-08-10 15:47:10,742 INFO     29 [qwen-vl-text] coord item[8]: text=既往史和其他病史：既往1年前诊断肝CA，行介入+抗肿瘤靶向+免疫治疗。, bbox=[143, 290, 844, 320]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[9]: text=查体：血压：/mmHg，脉搏：次/分。无特殊阳性体征。, bbox=[143, 337, 655, 367]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[10]: text=辅助检查：2026-03-06,上腹部薄层CT平扫+增强扫描检查意见：“肝癌”综合, bbox=[143, 380, 869, 410]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[11]: text=治疗后，较2025-12-07日腹部CT：肝右叶肿块较前大小相仿，无明显血供；肿, bbox=[143, 425, 869, 455]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[12]: text=块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大，下腔静脉癌栓形, bbox=[143, 470, 848, 500]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[13]: text=成；余较前相仿。, bbox=[143, 516, 305, 545]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[14]: text=诊断：1.肝细胞癌(BCLC B期，CNLC IIb期)；2.恶性肿瘤靶向治疗；3.恶性肿瘤, bbox=[143, 564, 876, 594]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[15]: text=免疫治疗；4.肝癌介入治疗；5.慢性肝炎, bbox=[143, 610, 502, 640]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[16]: text=处理：, bbox=[143, 657, 192, 685]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[17]: text=下转情况：◎不下转 ○转县级院 ○转社区卫生服务机构/乡镇卫生院, bbox=[143, 745, 810, 775]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] coord item[18]: text=医生签名：陈天翔, bbox=[524, 807, 753, 862]
2026-08-10 15:47:10,743 INFO     29 [qwen-vl-text] page=3 — 19/19 coords, api_time=7.4s
2026-08-10 15:47:10,744 INFO     29 [qwen-vl-text] new_positions (19):
[[3, 120.40599999999999, 165.874, 8.924999999999999, 25.584999999999997], [3, 445.418, 655.076, 8.924999999999999, 25.584999999999997], [3, 120.40599999999999, 317.43399999999997, 36.295, 53.55], [3, 120.40599999999999, 363.74399999999997, 62.474999999999994, 79.72999999999999], [3, 443.734, 711.49, 62.474999999999994, 79.72999999999999], [3, 120.40599999999999, 243.338, 91.63, 108.88499999999999], [3, 120.40599999999999, 483.308, 118.405, 135.66], [3, 120.40599999999999, 629.816, 145.18, 163.03], [3, 120.40599999999999, 710.648, 172.54999999999998, 190.39999999999998], [3, 120.40599999999999, 551.51, 200.515, 218.36499999999998], [3, 120.40599999999999, 731.698, 226.1, 243.95], [3, 120.40599999999999, 731.698, 252.875, 270.72499999999997], [3, 120.40599999999999, 714.016, 279.65, 297.5], [3, 120.40599999999999, 256.81, 307.02, 324.275], [3, 120.40599999999999, 737.592, 335.58, 353.43], [3, 120.40599999999999, 422.68399999999997, 362.95, 380.79999999999995], [3, 120.40599999999999, 161.664, 390.91499999999996, 407.575], [3, 120.40599999999999, 682.02, 443.275, 461.125], [3, 441.20799999999997, 634.026, 480.16499999999996, 512.89]]
2026-08-10 15:47:10,744 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=9.7s
2026-08-10 15:47:10,759 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 15:47:10,759 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:Clinical | outputs={"chunks": "3 items, types={'OutpatientRecord': 3}", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:47:10,759 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 15:47:10,761 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:47:10.759+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:47:10,772 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:10,773 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:47:11,901 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:11,909 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 15:47:11,909 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:47:11,909 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 15:47:11,917 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:11,917 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:47:12,378 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:12,395 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 15:47:12,396 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:47:12,396 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 15:47:12,410 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:47:12,412 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:47:12,412 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:47:12,412 INFO     29 [qwen-vl-text] positions(46): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:47:12,412 INFO     29 [qwen-vl-text] page grouping: [4, 5], lines per page: [24, 22]
2026-08-10 15:47:12,650 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:47:12,884 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:47:12,885 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2064
2026-08-10 15:47:12,886 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:12,886 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 84, \"bbox_end\": 129, \"encounter_dates\": [\"2025-08-02\", \"2025-08-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "入院日期：2025年08月02日\n出院日期：2025年08月06日\n住院天数：4\n入院情况(简要病史\\体格检查及主要辅助检查)：患者男性57岁，因肝癌于我院行综合治疗，现为返\n院复诊，无头晕头痛，胸闷气促，恶心呕吐等不适，于我院门诊就诊，门诊拟\"肝癌介入治疗\"收入我\n科。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。查体：神志清楚，\n皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压\n痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨\n中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：暂无。\n入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.肝细胞癌4.恶性肿瘤靶向治疗5.\n恶性肿瘤免疫治疗6.慢性乙型病毒性肝炎。\n诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检\n验检查：主要化验：2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞\n计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l,\n2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶\n原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋\n白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。特殊检查：\n2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层\n194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。\n2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶\n肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆\n管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。有手术指征，排除手术禁忌症后，于2025\n年08月04日行肝动脉栓塞术 肝动脉造影术 腹腔动脉灌注化疗药物，术后给予患者止吐、护胃、止\n痛、补液等对症治疗，今患者术后恢复可，予以免疫治疗后，患者无特殊不适，给予出院。\n诊疗经过(包括手术日期和手术名称,植入类医用耗材名称、型号及数量):入院后予以完善相关检\n验检查:主要化验:2025-06-02肝功能五项:γ-谷氨酰基转移酶67.30U/L。2025-06-02血清总蛋白+\n白蛋白测定:白蛋白39.40g/L。2025-06-02超敏C反应蛋白测定+金标法加收(全程,快):超敏C反应\n蛋白测定(全程)30.63mg/L。2025-06-02血常规(五分类法):红细胞计数7.01*10^12/L,血小板计数\n110*10^9/L。2025-06-02肝癌三项:甲胎蛋白测定4679.00ng/ml,甲胎蛋白异质体L3测定370.00ng/ml,\n异常凝血酶原测定>20000.00ng/ml。2025-06-04超敏C反应蛋白测定+金标法加收(全程,快):超敏C\n反应蛋白测定(全程)25.06mg/L。2025-06-04血常规(五分类法):红细胞计数6.19*10^12/L,血红蛋\n白119g/L,血小板计数113*10^9/L,中性粒细胞百分比89.8%。2025-06-04凝血四项:凝血酶原时间\n13.3sec。2025-06-04肝功能八项+白蛋白:天门冬氨酸氨基转移酶60.10U/L。余检验均未见明显异\n常。特殊检查:2025-06-03,上腹部CT平扫+增强扫描检查意见:肝癌综合治疗后,与2025-3-18片比\n较:肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及实验\n室资料;肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。术\n前诊断:原发性肝癌(BCLC B期,CNLC IIb期),有手术指征,排除手术禁忌症后,于2025-06-03行肝\n动脉栓塞术+肝局部灌注术,术后给予患者护胃、止吐、止痛、补液等对症治疗,今患者术后恢复可,\n给予出院。\n出院诊断:1.肝癌介入治疗2.原发性肝癌(BCLC B期,CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤\n靶向治疗5.恶性肿瘤免疫治疗6.肾结石。\n出院情况:患者一般情况良好,生命体征平稳,无畏寒发热,无恶心呕吐,无头痛头晕,无胸闷心\n悸。查体:全身皮肤、巩膜未见黄染,腹平软,无压痛,未及反跳痛和肌紧张,肠鸣音正常,股动脉\n穿刺点无渗血,双下肢动脉搏动良好。\n出院医嘱:\nI",
    "role": "user"
  }
]
2026-08-10 15:47:27,986 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:27,986 INFO     29 [qwen-vl-text] LLM output (len=3103):
{
  "encounter_date": "2025-08-06",
  "admission_date": "2025-08-02",
  "discharge_date": "2025-08-06",
  "hospital_days": 4,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者男性57岁，因肝癌于我院行综合治疗，现为返院复诊，无头晕头痛，胸闷气促，恶心呕吐等不适，于我院门诊就诊，门诊拟\"肝癌介入治疗\"收入我科。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。查体：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：暂无。",
  "admission_diagnoses": [
    {
      "name": "肝癌介入治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "原发性肝癌(BCLC B期，CNLC IIb期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝细胞癌",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶向治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "慢性乙型病毒性肝炎",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后予以完善相关检验检查：主要化验：2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l, 2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。特殊检查：2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。有手术指征，排除手术禁忌症后，于2025年08月04日行肝动脉栓塞术 肝动脉造影术 腹腔动脉灌注化疗药物，术后给予患者止吐、护胃、止痛、补液等对症治疗，今患者术后恢复可，予以免疫治疗后，患者无特殊不适，给予出院。",
  "auxiliary_exams": "2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l, 2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。",
  "imaging_findings": "2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。",
  "discharge_diagnoses": [
    {
      "name": "肝癌介入治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "原发性肝癌(BCLC B期,CNLC IIb期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "慢性乙型病毒性肝炎",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶向治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肾结石",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者一般情况良好,生命体征平稳,无畏寒发热,无恶心呕吐,无头痛头晕,无胸闷心悸。查体:全身皮肤、巩膜未见黄染,腹平软,无压痛,未及反跳痛和肌紧张,肠鸣音正常,股动脉穿刺点无渗血,双下肢动脉搏动良好。",
  "outcome": "好转",
  "discharge_orders": null,
  "do_medications": [],
  "do_follow_up": null,
  "do_precautions": [],
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
2026-08-10 15:47:27,986 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-08-06]
2026-08-10 15:47:27,990 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1796291, prompt_len=1773
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["入院日期：2025年08月02日", "出院日期：2025年08月06日", "住院天数：4", "入院情况(简要病史\\体格检查及主要辅助检查)：患者男性57岁，因肝癌于我院行综合治疗，现为返", "院复诊，无头晕头痛，胸闷气促，恶心呕吐等不适，于我院门诊就诊，门诊拟\"肝癌介入治疗\"收入我", "科。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。查体：神志清楚，", "皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压", "痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨", "中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：暂无。", "入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.肝细胞癌4.恶性肿瘤靶向治疗5.", "恶性肿瘤免疫治疗6.慢性乙型病毒性肝炎。", "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "验检查：主要化验：2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞", "计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l,", "2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶", "原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋", "白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。特殊检查：", "2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层", "194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。", "2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶", "肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆", "管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。有手术指征，排除手术禁忌症后，于2025", "年08月04日行肝动脉栓塞术 肝动脉造影术 腹腔动脉灌注化疗药物，术后给予患者止吐、护胃、止", "痛、补液等对症治疗，今患者术后恢复可，予以免疫治疗后，患者无特殊不适，给予出院。"]

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
2026-08-10 15:47:42,263 INFO     29 [qwen-vl-text] coord API raw response (len=2139):
[
	{"text": "入院日期：2025年08月02日", "bbox": [135, 18, 327, 43]},
	{"text": "出院日期：2025年08月06日", "bbox": [375, 18, 570, 43]},
	{"text": "住院天数：4", "bbox": [620, 18, 712, 43]},
	{"text": "入院情况(简要病史\\体格检查及主要辅助检查)：患者男性57岁，因肝癌于我院行综合治疗，现为返", "bbox": [135, 59, 843, 85]},
	{"text": "院复诊，无头晕头痛，胸闷气促，恶心呕吐等不适，于我院门诊就诊，门诊拟\"肝癌介入治疗\"收入我", "bbox": [135, 100, 854, 125]},
	{"text": "科。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。查体：神志清楚，", "bbox": [135, 140, 844, 165]},
	{"text": "皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压", "bbox": [135, 180, 853, 206]},
	{"text": "痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨", "bbox": [135, 190, 861, 230]},
	{"text": "中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：暂无。", "bbox": [135, 261, 697, 287]},
	{"text": "入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.肝细胞癌4.恶性肿瘤靶向治疗5.", "bbox": [135, 303, 850, 328]},
	{"text": "恶性肿瘤免疫治疗6.慢性乙型病毒性肝炎。", "bbox": [135, 344, 433, 369]},
	{"text": "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "bbox": [135, 384, 833, 409]},
	{"text": "验检查：主要化验：2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞", "bbox": [135, 425, 853, 450]},
	{"text": "计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l,", "bbox": [135, 465, 799, 490]},
	{"text": "2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶", "bbox": [135, 505, 861, 531]},
	{"text": "原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋", "bbox": [135, 545, 852, 571]},
	{"text": "白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。特殊检查：", "bbox": [135, 585, 826, 611]},
	{"text": "2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层", "bbox": [135, 626, 843, 651]},
	{"text": "194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。", "bbox": [135, 666, 835, 691]},
	{"text": "2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶", "bbox": [135, 706, 851, 732]},
	{"text": "肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆", "bbox": [135, 746, 851, 772]},
	{"text": "管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。有手术指征，排除手术禁忌症后，于2025", "bbox": [135, 786, 851, 812]},
	{"text": "年08月04日行肝动脉栓塞术 肝动脉造影术 腹腔动脉灌注化疗药物，术后给予患者止吐、护胃、止", "bbox": [135, 827, 834, 852]},
	{"text": "痛、补液等对症治疗，今患者术后恢复可，予以免疫治疗后，患者无特殊不适，给予出院。", "bbox": [135, 867, 775, 893]}
]
2026-08-10 15:47:42,263 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=14.3s
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[0]: text=入院日期：2025年08月02日, bbox=[135, 18, 327, 43]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[1]: text=出院日期：2025年08月06日, bbox=[375, 18, 570, 43]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[2]: text=住院天数：4, bbox=[620, 18, 712, 43]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[3]: text=入院情况(简要病史\体格检查及主要辅助检查)：患者男性57岁，因肝癌于我院行综合治疗，现为返, bbox=[135, 59, 843, 85]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[4]: text=院复诊，无头晕头痛，胸闷气促，恶心呕吐等不适，于我院门诊就诊，门诊拟"肝癌介入治疗"收入我, bbox=[135, 100, 854, 125]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[5]: text=科。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。查体：神志清楚，, bbox=[135, 140, 844, 165]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[6]: text=皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压, bbox=[135, 180, 853, 206]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[7]: text=痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨, bbox=[135, 190, 861, 230]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[8]: text=中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：暂无。, bbox=[135, 261, 697, 287]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[9]: text=入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.肝细胞癌4.恶性肿瘤靶向治疗5., bbox=[135, 303, 850, 328]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[10]: text=恶性肿瘤免疫治疗6.慢性乙型病毒性肝炎。, bbox=[135, 344, 433, 369]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[11]: text=诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检, bbox=[135, 384, 833, 409]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[12]: text=验检查：主要化验：2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞, bbox=[135, 425, 853, 450]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[13]: text=计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l,, bbox=[135, 465, 799, 490]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[14]: text=2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶, bbox=[135, 505, 861, 531]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[15]: text=原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋, bbox=[135, 545, 852, 571]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[16]: text=白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。特殊检查：, bbox=[135, 585, 826, 611]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[17]: text=2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层, bbox=[135, 626, 843, 651]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[18]: text=194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。, bbox=[135, 666, 835, 691]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[19]: text=2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶, bbox=[135, 706, 851, 732]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[20]: text=肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆, bbox=[135, 746, 851, 772]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[21]: text=管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。有手术指征，排除手术禁忌症后，于2025, bbox=[135, 786, 851, 812]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[22]: text=年08月04日行肝动脉栓塞术 肝动脉造影术 腹腔动脉灌注化疗药物，术后给予患者止吐、护胃、止, bbox=[135, 827, 834, 852]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] coord item[23]: text=痛、补液等对症治疗，今患者术后恢复可，予以免疫治疗后，患者无特殊不适，给予出院。, bbox=[135, 867, 775, 893]
2026-08-10 15:47:42,264 INFO     29 [qwen-vl-text] page=4 — 24/24 coords, api_time=14.3s
2026-08-10 15:47:42,267 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1601649, prompt_len=1657
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["诊疗经过(包括手术日期和手术名称,植入类医用耗材名称、型号及数量):入院后予以完善相关检", "验检查:主要化验:2025-06-02肝功能五项:γ-谷氨酰基转移酶67.30U/L。2025-06-02血清总蛋白+", "白蛋白测定:白蛋白39.40g/L。2025-06-02超敏C反应蛋白测定+金标法加收(全程,快):超敏C反应", "蛋白测定(全程)30.63mg/L。2025-06-02血常规(五分类法):红细胞计数7.01*10^12/L,血小板计数", "110*10^9/L。2025-06-02肝癌三项:甲胎蛋白测定4679.00ng/ml,甲胎蛋白异质体L3测定370.00ng/ml,", "异常凝血酶原测定>20000.00ng/ml。2025-06-04超敏C反应蛋白测定+金标法加收(全程,快):超敏C", "反应蛋白测定(全程)25.06mg/L。2025-06-04血常规(五分类法):红细胞计数6.19*10^12/L,血红蛋", "白119g/L,血小板计数113*10^9/L,中性粒细胞百分比89.8%。2025-06-04凝血四项:凝血酶原时间", "13.3sec。2025-06-04肝功能八项+白蛋白:天门冬氨酸氨基转移酶60.10U/L。余检验均未见明显异", "常。特殊检查:2025-06-03,上腹部CT平扫+增强扫描检查意见:肝癌综合治疗后,与2025-3-18片比", "较:肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及实验", "室资料;肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。术", "前诊断:原发性肝癌(BCLC B期,CNLC IIb期),有手术指征,排除手术禁忌症后,于2025-06-03行肝", "动脉栓塞术+肝局部灌注术,术后给予患者护胃、止吐、止痛、补液等对症治疗,今患者术后恢复可,", "给予出院。", "出院诊断:1.肝癌介入治疗2.原发性肝癌(BCLC B期,CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "出院情况:患者一般情况良好,生命体征平稳,无畏寒发热,无恶心呕吐,无头痛头晕,无胸闷心", "悸。查体:全身皮肤、巩膜未见黄染,腹平软,无压痛,未及反跳痛和肌紧张,肠鸣音正常,股动脉", "穿刺点无渗血,双下肢动脉搏动良好。", "出院医嘱:", "I"]

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
2026-08-10 15:47:53,158 INFO     29 [qwen-vl-text] coord API raw response (len=1944):
[
	{"text": "诊疗经过(包括手术日期和手术名称,植入类医用耗材名称、型号及数量):入院后予以完善相关检", "bbox": [124, 12, 856, 40]},
	{"text": "验检查:主要化验:2025-06-02肝功能五项:γ-谷氨酰基转移酶67.30U/L。2025-06-02血清总蛋白+", "bbox": [124, 54, 886, 82]},
	{"text": "白蛋白测定:白蛋白39.40g/L。2025-06-02超敏C反应蛋白测定+金标法加收(全程,快):超敏C反应", "bbox": [124, 95, 876, 122]},
	{"text": "蛋白测定(全程)30.63mg/L。2025-06-02血常规(五分类法):红细胞计数7.01*10^12/L,血小板计数", "bbox": [124, 137, 882, 165]},
	{"text": "110*10^9/L。2025-06-02肝癌三项:甲胎蛋白测定4679.00ng/ml,甲胎蛋白异质体L3测定370.00ng/ml,", "bbox": [124, 178, 889, 206]},
	{"text": "异常凝血酶原测定>20000.00ng/ml。2025-06-04超敏C反应蛋白测定+金标法加收(全程,快):超敏C", "bbox": [124, 220, 877, 248]},
	{"text": "反应蛋白测定(全程)25.06mg/L。2025-06-04血常规(五分类法):红细胞计数6.19*10^12/L,血红蛋", "bbox": [124, 262, 881, 290]},
	{"text": "白119g/L,血小板计数113*10^9/L,中性粒细胞百分比89.8%。2025-06-04凝血四项:凝血酶原时间", "bbox": [124, 304, 864, 332]},
	{"text": "13.3sec。2025-06-04肝功能八项+白蛋白:天门冬氨酸氨基转移酶60.10U/L。余检验均未见明显异", "bbox": [124, 346, 866, 374]},
	{"text": "常。特殊检查:2025-06-03,上腹部CT平扫+增强扫描检查意见:肝癌综合治疗后,与2025-3-18片比", "bbox": [124, 388, 856, 416]},
	{"text": "较:肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及实验", "bbox": [124, 430, 873, 458]},
	{"text": "室资料;肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。术", "bbox": [124, 472, 873, 500]},
	{"text": "前诊断:原发性肝癌(BCLC B期,CNLC IIb期),有手术指征,排除手术禁忌症后,于2025-06-03行肝", "bbox": [124, 514, 872, 542]},
	{"text": "动脉栓塞术+肝局部灌注术,术后给予患者护胃、止吐、止痛、补液等对症治疗,今患者术后恢复可,", "bbox": [124, 556, 871, 584]},
	{"text": "给予出院。", "bbox": [124, 601, 196, 625]},
	{"text": "出院诊断:1.肝癌介入治疗2.原发性肝癌(BCLC B期,CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "bbox": [124, 641, 872, 669]},
	{"text": "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "bbox": [124, 683, 417, 711]},
	{"text": "出院情况:患者一般情况良好,生命体征平稳,无畏寒发热,无恶心呕吐,无头痛头晕,无胸闷心", "bbox": [124, 724, 854, 752]},
	{"text": "悸。查体:全身皮肤、巩膜未见黄染,腹平软,无压痛,未及反跳痛和肌紧张,肠鸣音正常,股动脉", "bbox": [124, 766, 870, 794]},
	{"text": "穿刺点无渗血,双下肢动脉搏动良好。", "bbox": [124, 808, 400, 836]},
	{"text": "出院医嘱:", "bbox": [124, 849, 194, 874]},
	{"text": "I", "bbox": [890, 583, 899, 605]}
]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=10.9s
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[0]: text=诊疗经过(包括手术日期和手术名称,植入类医用耗材名称、型号及数量):入院后予以完善相关检, bbox=[124, 12, 856, 40]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[1]: text=验检查:主要化验:2025-06-02肝功能五项:γ-谷氨酰基转移酶67.30U/L。2025-06-02血清总蛋白+, bbox=[124, 54, 886, 82]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[2]: text=白蛋白测定:白蛋白39.40g/L。2025-06-02超敏C反应蛋白测定+金标法加收(全程,快):超敏C反应, bbox=[124, 95, 876, 122]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[3]: text=蛋白测定(全程)30.63mg/L。2025-06-02血常规(五分类法):红细胞计数7.01*10^12/L,血小板计数, bbox=[124, 137, 882, 165]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[4]: text=110*10^9/L。2025-06-02肝癌三项:甲胎蛋白测定4679.00ng/ml,甲胎蛋白异质体L3测定370.00ng/ml,, bbox=[124, 178, 889, 206]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[5]: text=异常凝血酶原测定>20000.00ng/ml。2025-06-04超敏C反应蛋白测定+金标法加收(全程,快):超敏C, bbox=[124, 220, 877, 248]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[6]: text=反应蛋白测定(全程)25.06mg/L。2025-06-04血常规(五分类法):红细胞计数6.19*10^12/L,血红蛋, bbox=[124, 262, 881, 290]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[7]: text=白119g/L,血小板计数113*10^9/L,中性粒细胞百分比89.8%。2025-06-04凝血四项:凝血酶原时间, bbox=[124, 304, 864, 332]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[8]: text=13.3sec。2025-06-04肝功能八项+白蛋白:天门冬氨酸氨基转移酶60.10U/L。余检验均未见明显异, bbox=[124, 346, 866, 374]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[9]: text=常。特殊检查:2025-06-03,上腹部CT平扫+增强扫描检查意见:肝癌综合治疗后,与2025-3-18片比, bbox=[124, 388, 856, 416]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[10]: text=较:肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及实验, bbox=[124, 430, 873, 458]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[11]: text=室资料;肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。术, bbox=[124, 472, 873, 500]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[12]: text=前诊断:原发性肝癌(BCLC B期,CNLC IIb期),有手术指征,排除手术禁忌症后,于2025-06-03行肝, bbox=[124, 514, 872, 542]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[13]: text=动脉栓塞术+肝局部灌注术,术后给予患者护胃、止吐、止痛、补液等对症治疗,今患者术后恢复可,, bbox=[124, 556, 871, 584]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[14]: text=给予出院。, bbox=[124, 601, 196, 625]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[15]: text=出院诊断:1.肝癌介入治疗2.原发性肝癌(BCLC B期,CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤, bbox=[124, 641, 872, 669]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[16]: text=靶向治疗5.恶性肿瘤免疫治疗6.肾结石。, bbox=[124, 683, 417, 711]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[17]: text=出院情况:患者一般情况良好,生命体征平稳,无畏寒发热,无恶心呕吐,无头痛头晕,无胸闷心, bbox=[124, 724, 854, 752]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[18]: text=悸。查体:全身皮肤、巩膜未见黄染,腹平软,无压痛,未及反跳痛和肌紧张,肠鸣音正常,股动脉, bbox=[124, 766, 870, 794]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[19]: text=穿刺点无渗血,双下肢动脉搏动良好。, bbox=[124, 808, 400, 836]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[20]: text=出院医嘱:, bbox=[124, 849, 194, 874]
2026-08-10 15:47:53,159 INFO     29 [qwen-vl-text] coord item[21]: text=I, bbox=[890, 583, 899, 605]
2026-08-10 15:47:53,160 INFO     29 [qwen-vl-text] page=5 — 22/22 coords, api_time=10.9s
2026-08-10 15:47:53,160 INFO     29 [qwen-vl-text] new_positions (46):
[[4, 113.67, 275.334, 10.709999999999999, 25.584999999999997], [4, 315.75, 479.94, 10.709999999999999, 25.584999999999997], [4, 522.04, 599.504, 10.709999999999999, 25.584999999999997], [4, 113.67, 709.8059999999999, 35.105, 50.574999999999996], [4, 113.67, 719.068, 59.5, 74.375], [4, 113.67, 710.648, 83.3, 98.175], [4, 113.67, 718.226, 107.1, 122.57], [4, 113.67, 724.962, 113.05, 136.85], [4, 113.67, 586.874, 155.295, 170.765], [4, 113.67, 715.6999999999999, 180.285, 195.16], [4, 113.67, 364.586, 204.67999999999998, 219.55499999999998], [4, 113.67, 701.386, 228.48, 243.355], [4, 113.67, 718.226, 252.875, 267.75], [4, 113.67, 672.7579999999999, 276.675, 291.55], [4, 113.67, 724.962, 300.47499999999997, 315.945], [4, 113.67, 717.384, 324.275, 339.745], [4, 113.67, 695.492, 348.075, 363.54499999999996], [4, 113.67, 709.8059999999999, 372.46999999999997, 387.34499999999997], [4, 113.67, 703.0699999999999, 396.27, 411.145], [4, 113.67, 716.542, 420.07, 435.53999999999996], [4, 113.67, 716.542, 443.87, 459.34], [4, 113.67, 716.542, 467.66999999999996, 483.14], [4, 113.67, 702.228, 492.065, 506.94], [4, 113.67, 652.55, 515.865, 531.3349999999999], [5, 104.408, 720.752, 7.14, 23.799999999999997], [5, 104.408, 746.012, 32.129999999999995, 48.79], [5, 104.408, 737.592, 56.525, 72.59], [5, 104.408, 742.644, 81.515, 98.175], [5, 104.408, 748.538, 105.91, 122.57], [5, 104.408, 738.434, 130.9, 147.56], [5, 104.408, 741.802, 155.89, 172.54999999999998], [5, 104.408, 727.4879999999999, 180.88, 197.54], [5, 104.408, 729.172, 205.87, 222.53], [5, 104.408, 720.752, 230.85999999999999, 247.51999999999998], [5, 104.408, 735.066, 255.85, 272.51], [5, 104.408, 735.066, 280.84, 297.5], [5, 104.408, 734.2239999999999, 305.83, 322.49], [5, 104.408, 733.382, 330.82, 347.47999999999996], [5, 104.408, 165.03199999999998, 357.59499999999997, 371.875], [5, 104.408, 734.2239999999999, 381.395, 398.055], [5, 104.408, 351.114, 406.385, 423.04499999999996], [5, 104.408, 719.068, 430.78, 447.44], [5, 104.408, 732.54, 455.77, 472.43], [5, 104.408, 336.8, 480.76, 497.41999999999996], [5, 104.408, 163.34799999999998, 505.155, 520.03], [5, 749.38, 756.958, 346.885, 359.97499999999997]]
2026-08-10 15:47:53,160 INFO     29 [qwen-vl-text] ═══ DONE ═══ 46 positions, pages=2, time=40.8s
2026-08-10 15:47:53,160 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:47:53,168 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:47:53,168 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:47:53,168 INFO     29 [qwen-vl-text] positions(21): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:47:53,168 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [21]
2026-08-10 15:47:53,378 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:47:53,379 INFO     29 [qwen-vl-text] LLM extraction start, text_len=907
2026-08-10 15:47:53,379 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:47:53,379 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 130, \"bbox_end\": 150, \"encounter_dates\": [\"2025-04-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "肝区介入术后复查所见。\n入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤\n靶向治疗5.恶性肿瘤免疫治疗6.肾结石。\n诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检\n验检查：主要化验：2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,\n2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白\n44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性\n磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测\n定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。余检验均\n未见明显异常。特殊检查：2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大\n致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。术前诊断：1.肝癌介入治\n疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤靶向治疗5.恶性肿瘤免疫\n治疗6.肾结石。有手术指征，排除手术禁忌症后，于2025年04月27日局部麻醉下行肝动脉栓塞术,肝\n局部灌注术,肝动脉造影术,肝动脉置管术，术后给予患者止痛、补液等对症治疗，今患者术后恢复\n可，给予出院。\n出院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤\n靶向治疗5.恶性肿瘤免疫治疗6.肾结石。\n出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心\n悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉\n穿刺点无渗血，双下肢动脉搏动良好。\n出院医嘱：",
    "role": "user"
  }
]
2026-08-10 15:47:53,381 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:47:53.381+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:48:04,977 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:48:04,977 INFO     29 [qwen-vl-text] LLM output (len=2642):
{
  "encounter_date": "2025-04-27",
  "admission_date": null,
  "discharge_date": "2025-04-27",
  "hospital_days": null,
  "department": null,
  "bed_number": null,
  "admission_condition": null,
  "admission_diagnoses": [
    {
      "name": "肝癌介入治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "原发性肝癌(BCLC B期，CNLC IIb期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "慢性乙型病毒性肝炎",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶向治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肾结石",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后予以完善相关检验检查：主要化验：2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。余检验均未见明显异常。特殊检查：2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。术前诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤靶向治疗5.恶性肿瘤免疫治疗6.肾结石。有手术指征，排除手术禁忌症后，于2025年04月27日局部麻醉下行肝动脉栓塞术,肝局部灌注术,肝动脉造影术,肝动脉置管术，术后给予患者止痛、补液等对症治疗，今患者术后恢复可，给予出院。",
  "auxiliary_exams": "2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。",
  "imaging_findings": "2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。",
  "discharge_diagnoses": [
    {
      "name": "肝癌介入治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "原发性肝癌(BCLC B期，CNLC IIb期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "慢性乙型病毒性肝炎",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶向治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肾结石",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉穿刺点无渗血，双下肢动脉搏动良好。",
  "outcome": "好转",
  "discharge_orders": null,
  "do_medications": [],
  "do_follow_up": null,
  "do_precautions": [],
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
2026-08-10 15:48:04,977 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-27]
2026-08-10 15:48:04,982 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1506202, prompt_len=1583
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["肝区介入术后复查所见。", "入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "验检查：主要化验：2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,", "2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白", "44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性", "磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测", "定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。余检验均", "未见明显异常。特殊检查：2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大", "致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。术前诊断：1.肝癌介入治", "疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤靶向治疗5.恶性肿瘤免疫", "治疗6.肾结石。有手术指征，排除手术禁忌症后，于2025年04月27日局部麻醉下行肝动脉栓塞术,肝", "局部灌注术,肝动脉造影术,肝动脉置管术，术后给予患者止痛、补液等对症治疗，今患者术后恢复", "可，给予出院。", "出院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心", "悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉", "穿刺点无渗血，双下肢动脉搏动良好。", "出院医嘱："]

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
2026-08-10 15:48:17,395 INFO     29 [qwen-vl-text] coord API raw response (len=1828):
[
	{"text": "肝区介入术后复查所见。", "bbox": [124, 0, 304, 23]},
	{"text": "入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "bbox": [124, 40, 871, 67]},
	{"text": "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "bbox": [124, 82, 418, 106]},
	{"text": "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "bbox": [124, 122, 850, 148]},
	{"text": "验检查：主要化验：2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,", "bbox": [124, 165, 791, 191]},
	{"text": "2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白", "bbox": [124, 206, 851, 232]},
	{"text": "44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性", "bbox": [124, 250, 880, 276]},
	{"text": "磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测", "bbox": [124, 292, 880, 318]},
	{"text": "定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。余检验均", "bbox": [124, 334, 871, 360]},
	{"text": "未见明显异常。特殊检查：2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大", "bbox": [124, 376, 871, 402]},
	{"text": "致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。术前诊断：1.肝癌介入治", "bbox": [124, 418, 871, 444]},
	{"text": "疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤靶向治疗5.恶性肿瘤免疫", "bbox": [124, 460, 871, 486]},
	{"text": "治疗6.肾结石。有手术指征，排除手术禁忌症后，于2025年04月27日局部麻醉下行肝动脉栓塞术,肝", "bbox": [124, 502, 871, 528]},
	{"text": "局部灌注术,肝动脉造影术,肝动脉置管术，术后给予患者止痛、补液等对症治疗，今患者术后恢复", "bbox": [124, 544, 855, 570]},
	{"text": "可，给予出院。", "bbox": [124, 588, 232, 613]},
	{"text": "出院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤", "bbox": [124, 629, 873, 655]},
	{"text": "靶向治疗5.恶性肿瘤免疫治疗6.肾结石。", "bbox": [124, 672, 418, 697]},
	{"text": "出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心", "bbox": [124, 713, 857, 739]},
	{"text": "悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉", "bbox": [124, 755, 871, 781]},
	{"text": "穿刺点无渗血，双下肢动脉搏动良好。", "bbox": [124, 797, 404, 823]},
	{"text": "出院医嘱：", "bbox": [124, 840, 196, 864]}
]
2026-08-10 15:48:17,396 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=12.4s
2026-08-10 15:48:17,396 INFO     29 [qwen-vl-text] coord item[0]: text=肝区介入术后复查所见。, bbox=[124, 0, 304, 23]
2026-08-10 15:48:17,396 INFO     29 [qwen-vl-text] coord item[1]: text=入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤, bbox=[124, 40, 871, 67]
2026-08-10 15:48:17,396 INFO     29 [qwen-vl-text] coord item[2]: text=靶向治疗5.恶性肿瘤免疫治疗6.肾结石。, bbox=[124, 82, 418, 106]
2026-08-10 15:48:17,396 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检, bbox=[124, 122, 850, 148]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[4]: text=验检查：主要化验：2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,, bbox=[124, 165, 791, 191]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[5]: text=2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白, bbox=[124, 206, 851, 232]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[6]: text=44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性, bbox=[124, 250, 880, 276]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[7]: text=磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测, bbox=[124, 292, 880, 318]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[8]: text=定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。余检验均, bbox=[124, 334, 871, 360]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[9]: text=未见明显异常。特殊检查：2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大, bbox=[124, 376, 871, 402]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[10]: text=致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。术前诊断：1.肝癌介入治, bbox=[124, 418, 871, 444]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[11]: text=疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤靶向治疗5.恶性肿瘤免疫, bbox=[124, 460, 871, 486]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[12]: text=治疗6.肾结石。有手术指征，排除手术禁忌症后，于2025年04月27日局部麻醉下行肝动脉栓塞术,肝, bbox=[124, 502, 871, 528]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[13]: text=局部灌注术,肝动脉造影术,肝动脉置管术，术后给予患者止痛、补液等对症治疗，今患者术后恢复, bbox=[124, 544, 855, 570]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[14]: text=可，给予出院。, bbox=[124, 588, 232, 613]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[15]: text=出院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤, bbox=[124, 629, 873, 655]
2026-08-10 15:48:17,397 INFO     29 [qwen-vl-text] coord item[16]: text=靶向治疗5.恶性肿瘤免疫治疗6.肾结石。, bbox=[124, 672, 418, 697]
2026-08-10 15:48:17,398 INFO     29 [qwen-vl-text] coord item[17]: text=出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心, bbox=[124, 713, 857, 739]
2026-08-10 15:48:17,398 INFO     29 [qwen-vl-text] coord item[18]: text=悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉, bbox=[124, 755, 871, 781]
2026-08-10 15:48:17,398 INFO     29 [qwen-vl-text] coord item[19]: text=穿刺点无渗血，双下肢动脉搏动良好。, bbox=[124, 797, 404, 823]
2026-08-10 15:48:17,398 INFO     29 [qwen-vl-text] coord item[20]: text=出院医嘱：, bbox=[124, 840, 196, 864]
2026-08-10 15:48:17,398 INFO     29 [qwen-vl-text] page=6 — 21/21 coords, api_time=12.4s
2026-08-10 15:48:17,398 INFO     29 [qwen-vl-text] new_positions (21):
[[6, 104.408, 255.968, 0.0, 13.684999999999999], [6, 104.408, 733.382, 23.799999999999997, 39.864999999999995], [6, 104.408, 351.95599999999996, 48.79, 63.07], [6, 104.408, 715.6999999999999, 72.59, 88.06], [6, 104.408, 666.0219999999999, 98.175, 113.645], [6, 104.408, 716.542, 122.57, 138.04], [6, 104.408, 740.9599999999999, 148.75, 164.22], [6, 104.408, 740.9599999999999, 173.73999999999998, 189.20999999999998], [6, 104.408, 733.382, 198.73, 214.2], [6, 104.408, 733.382, 223.72, 239.19], [6, 104.408, 733.382, 248.70999999999998, 264.18], [6, 104.408, 733.382, 273.7, 289.16999999999996], [6, 104.408, 733.382, 298.69, 314.15999999999997], [6, 104.408, 719.91, 323.68, 339.15], [6, 104.408, 195.344, 349.85999999999996, 364.73499999999996], [6, 104.408, 735.066, 374.255, 389.72499999999997], [6, 104.408, 351.95599999999996, 399.84, 414.715], [6, 104.408, 721.5939999999999, 424.23499999999996, 439.705], [6, 104.408, 733.382, 449.22499999999997, 464.695], [6, 104.408, 340.168, 474.215, 489.685], [6, 104.408, 165.03199999999998, 499.79999999999995, 514.0799999999999]]
2026-08-10 15:48:17,399 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=24.2s
2026-08-10 15:48:17,399 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:48:17,401 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:48:17,401 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:48:17,401 INFO     29 [qwen-vl-text] positions(22): [[6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:48:17,401 INFO     29 [qwen-vl-text] page grouping: [6, 7], lines per page: [1, 21]
2026-08-10 15:48:17,615 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:48:17,846 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:48:17,847 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1056
2026-08-10 15:48:17,848 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:48:17,848 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 151, \"bbox_end\": 172, \"encounter_dates\": [\"2025-03-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "第1页\n入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。\n诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检\n验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,\n2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白\n蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-\n谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,\n2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙\n肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,\n2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血\n酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+\n增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检\n查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。术前\n诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肾结石3.肺部感染4.慢性乙型病毒性肝炎，经讨论评\n估为不可切除，决定行转化治疗，排除手术禁忌症后，于2025年03月20日行肝动脉栓塞术,肝动脉造影\n术,动脉注射化疗药物,肝动脉置管术，术后给予患者抗感染、护肝等对症治疗，今患者术后恢复可，\n予以靶免治疗(仑伐替尼，3粒，qd；信迪利单抗200mg，q3w)后给予出院。\n出院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肝癌介入治疗3.恶性肿瘤靶向治疗4.恶性肿瘤免\n疫治疗5.肾结石6.肺部感染7.慢性乙型病毒性肝炎。\n出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心\n悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉\n穿刺点无渗血，双下肢动脉搏动良好。",
    "role": "user"
  }
]
2026-08-10 15:48:25,146 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:48:25.143+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:48:31,275 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:48:31,275 INFO     29 [qwen-vl-text] LLM output (len=2905):
{
  "encounter_date": "2025-03-20",
  "admission_date": null,
  "discharge_date": "2025-03-20",
  "hospital_days": null,
  "department": null,
  "bed_number": null,
  "admission_condition": null,
  "admission_diagnoses": [
    {
      "name": "原发性肝癌(BCLC B期，CNLC IIb期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "左肾结石",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺部感染",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后予以完善相关检验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。术前诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肾结石3.肺部感染4.慢性乙型病毒性肝炎，经讨论评估为不可切除，决定行转化治疗，排除手术禁忌症后，于2025年03月20日行肝动脉栓塞术,肝动脉造影术,动脉注射化疗药物,肝动脉置管术，术后给予患者抗感染、护肝等对症治疗，今患者术后恢复可，予以靶免治疗(仑伐替尼，3粒，qd；信迪利单抗200mg，q3w)后给予出院。",
  "auxiliary_exams": "2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。",
  "imaging_findings": "2025-03-18,上腹部CT平扫+增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。",
  "discharge_diagnoses": [
    {
      "name": "原发性肝癌(BCLC B期，CNLC IIb期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝癌介入治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶向治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肾结石",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺部感染",
      "diagnosis_type": "西医"
    },
    {
      "name": "慢性乙型病毒性肝炎",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉穿刺点无渗血，双下肢动脉搏动良好。",
  "outcome": "好转",
  "discharge_orders": null,
  "do_medications": [
    "仑伐替尼 3粒 qd",
    "信迪利单抗 200mg q3w"
  ],
  "do_follow_up": null,
  "do_precautions": [],
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
2026-08-10 15:48:31,275 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-20]
2026-08-10 15:48:31,277 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1506202, prompt_len=618
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["第1页"]

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
2026-08-10 15:48:31,943 INFO     29 [qwen-vl-text] coord API raw response (len=62):
```json
[
	{"text": "第1页", "bbox": [484, 897, 543, 920]}
]
```
2026-08-10 15:48:31,944 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 15:48:31,944 INFO     29 [qwen-vl-text] coord item[0]: text=第1页, bbox=[484, 897, 543, 920]
2026-08-10 15:48:31,945 INFO     29 [qwen-vl-text] page=6 — 1/1 coords, api_time=0.7s
2026-08-10 15:48:31,953 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1669928, prompt_len=1728
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。", "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,", "2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白", "蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-", "谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,", "2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙", "肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,", "2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血", "酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+", "增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检", "查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。术前", "诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肾结石3.肺部感染4.慢性乙型病毒性肝炎，经讨论评", "估为不可切除，决定行转化治疗，排除手术禁忌症后，于2025年03月20日行肝动脉栓塞术,肝动脉造影", "术,动脉注射化疗药物,肝动脉置管术，术后给予患者抗感染、护肝等对症治疗，今患者术后恢复可，", "予以靶免治疗(仑伐替尼，3粒，qd；信迪利单抗200mg，q3w)后给予出院。", "出院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肝癌介入治疗3.恶性肿瘤靶向治疗4.恶性肿瘤免", "疫治疗5.肾结石6.肺部感染7.慢性乙型病毒性肝炎。", "出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心", "悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉", "穿刺点无渗血，双下肢动脉搏动良好。"]

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
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord API raw response (len=1974):
[
	{"text": "入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。", "bbox": [130, 10, 663, 32]},
	{"text": "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "bbox": [130, 49, 829, 73]},
	{"text": "验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,", "bbox": [130, 88, 806, 111]},
	{"text": "2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白", "bbox": [130, 128, 857, 151]},
	{"text": "蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-", "bbox": [130, 168, 851, 192]},
	{"text": "谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,", "bbox": [130, 208, 782, 231]},
	{"text": "2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙", "bbox": [130, 249, 849, 273]},
	{"text": "肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,", "bbox": [130, 290, 772, 313]},
	{"text": "2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血", "bbox": [130, 331, 857, 354]},
	{"text": "酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+", "bbox": [130, 371, 857, 394]},
	{"text": "增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检", "bbox": [130, 412, 849, 435]},
	{"text": "查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。术前", "bbox": [130, 452, 849, 475]},
	{"text": "诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肾结石3.肺部感染4.慢性乙型病毒性肝炎，经讨论评", "bbox": [130, 493, 849, 516]},
	{"text": "估为不可切除，决定行转化治疗，排除手术禁忌症后，于2025年03月20日行肝动脉栓塞术,肝动脉造影", "bbox": [130, 533, 857, 557]},
	{"text": "术,动脉注射化疗药物,肝动脉置管术，术后给予患者抗感染、护肝等对症治疗，今患者术后恢复可，", "bbox": [130, 574, 839, 597]},
	{"text": "予以靶免治疗(仑伐替尼，3粒，qd；信迪利单抗200mg，q3w)后给予出院。", "bbox": [130, 614, 667, 638]},
	{"text": "出院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肝癌介入治疗3.恶性肿瘤靶向治疗4.恶性肿瘤免", "bbox": [130, 656, 849, 679]},
	{"text": "疫治疗5.肾结石6.肺部感染7.慢性乙型病毒性肝炎。", "bbox": [130, 696, 500, 719]},
	{"text": "出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心", "bbox": [130, 737, 840, 760]},
	{"text": "悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉", "bbox": [130, 777, 847, 800]},
	{"text": "穿刺点无渗血，双下肢动脉搏动良好。", "bbox": [130, 818, 400, 841]}
]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=11.5s
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[0]: text=入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。, bbox=[130, 10, 663, 32]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[1]: text=诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检, bbox=[130, 49, 829, 73]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[2]: text=验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,, bbox=[130, 88, 806, 111]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[3]: text=2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白, bbox=[130, 128, 857, 151]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[4]: text=蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-, bbox=[130, 168, 851, 192]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[5]: text=谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,, bbox=[130, 208, 782, 231]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[6]: text=2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙, bbox=[130, 249, 849, 273]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[7]: text=肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,, bbox=[130, 290, 772, 313]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[8]: text=2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血, bbox=[130, 331, 857, 354]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[9]: text=酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+, bbox=[130, 371, 857, 394]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[10]: text=增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检, bbox=[130, 412, 849, 435]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[11]: text=查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。术前, bbox=[130, 452, 849, 475]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[12]: text=诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肾结石3.肺部感染4.慢性乙型病毒性肝炎，经讨论评, bbox=[130, 493, 849, 516]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[13]: text=估为不可切除，决定行转化治疗，排除手术禁忌症后，于2025年03月20日行肝动脉栓塞术,肝动脉造影, bbox=[130, 533, 857, 557]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[14]: text=术,动脉注射化疗药物,肝动脉置管术，术后给予患者抗感染、护肝等对症治疗，今患者术后恢复可，, bbox=[130, 574, 839, 597]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[15]: text=予以靶免治疗(仑伐替尼，3粒，qd；信迪利单抗200mg，q3w)后给予出院。, bbox=[130, 614, 667, 638]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[16]: text=出院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肝癌介入治疗3.恶性肿瘤靶向治疗4.恶性肿瘤免, bbox=[130, 656, 849, 679]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[17]: text=疫治疗5.肾结石6.肺部感染7.慢性乙型病毒性肝炎。, bbox=[130, 696, 500, 719]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[18]: text=出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心, bbox=[130, 737, 840, 760]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[19]: text=悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉, bbox=[130, 777, 847, 800]
2026-08-10 15:48:43,409 INFO     29 [qwen-vl-text] coord item[20]: text=穿刺点无渗血，双下肢动脉搏动良好。, bbox=[130, 818, 400, 841]
2026-08-10 15:48:43,410 INFO     29 [qwen-vl-text] page=7 — 21/21 coords, api_time=11.5s
2026-08-10 15:48:43,410 INFO     29 [qwen-vl-text] new_positions (22):
[[6, 407.52799999999996, 457.20599999999996, 533.715, 547.4], [7, 109.46, 558.246, 5.949999999999999, 19.04], [7, 109.46, 698.018, 29.154999999999998, 43.434999999999995], [7, 109.46, 678.6519999999999, 52.36, 66.045], [7, 109.46, 721.5939999999999, 76.16, 89.845], [7, 109.46, 716.542, 99.96, 114.24], [7, 109.46, 658.444, 123.75999999999999, 137.445], [7, 109.46, 714.858, 148.155, 162.435], [7, 109.46, 650.024, 172.54999999999998, 186.23499999999999], [7, 109.46, 721.5939999999999, 196.945, 210.63], [7, 109.46, 721.5939999999999, 220.74499999999998, 234.42999999999998], [7, 109.46, 714.858, 245.14, 258.825], [7, 109.46, 714.858, 268.94, 282.625], [7, 109.46, 714.858, 293.335, 307.02], [7, 109.46, 721.5939999999999, 317.135, 331.41499999999996], [7, 109.46, 706.438, 341.53, 355.215], [7, 109.46, 561.614, 365.33, 379.60999999999996], [7, 109.46, 714.858, 390.32, 404.005], [7, 109.46, 421.0, 414.12, 427.805], [7, 109.46, 707.28, 438.515, 452.2], [7, 109.46, 713.174, 462.315, 476.0], [7, 109.46, 336.8, 486.71, 500.395]]
2026-08-10 15:48:43,410 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=2, time=26.0s
2026-08-10 15:48:43,410 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:48:43,411 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:48:43,411 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:48:43,411 INFO     29 [qwen-vl-text] positions(26): [[7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:48:43,411 INFO     29 [qwen-vl-text] page grouping: [7, 8, 9], lines per page: [1, 24, 1]
2026-08-10 15:48:43,634 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:48:43,888 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:48:44,087 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:48:44,088 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1145
2026-08-10 15:48:44,088 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:48:44,089 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 173, \"bbox_end\": 198, \"encounter_dates\": [\"2025-03-18\", \"2025-03-24\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "第1页\n入院日期：2025年03月18日\n出院日期：2025年03月24日\n住院天数：6天\n入院情况(简要病史\\体格检查及主要辅助检查)：患者男，57岁，因“反复右上腹部疼痛半年”入\n院。患者自诉半年余前开始无明显诱因下出现右上腹部疼痛，无恶心呕吐，无畏寒发热，自行缓解，1\n天前再发腹痛，至我院急诊就诊，行CT检查提示肝占位性病变，请我科医师会诊后，拟“肝占位性病\n变”收入我科住院。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。\n专科情况：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲\n张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓\n音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：\n2025-03-18上腹部CT平扫+增强扫描见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，\n请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺\n散在炎性灶。\n入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。\n诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检\n验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,\n2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白\n蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-\n谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，\n2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙\n肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，\n2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血\n酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+\n增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检\n临床诊断:1.肝细胞癌(BCLC B期,CNLC IIb期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶",
    "role": "user"
  }
]
2026-08-10 15:48:57,593 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:48:57.590+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:48:59,269 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:48:59,269 INFO     29 [qwen-vl-text] LLM output (len=2549):
{
  "encounter_date": "2025-03-24",
  "admission_date": "2025-03-18",
  "discharge_date": "2025-03-24",
  "hospital_days": 6,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者男，57岁，因“反复右上腹部疼痛半年”入院。患者自诉半年余前开始无明显诱因下出现右上腹部疼痛，无恶心呕吐，无畏寒发热，自行缓解，1天前再发腹痛，至我院急诊就诊，行CT检查提示肝占位性病变，请我科医师会诊后，拟“肝占位性病变”收入我科住院。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。专科情况：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。",
  "admission_diagnoses": [
    {
      "name": "原发性肝癌(BCLC B期，CNLC IIb期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "左肾结石",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺部感染",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后予以完善相关检验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检",
  "auxiliary_exams": "2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。",
  "imaging_findings": "2025-03-18上腹部CT平扫+增强扫描见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。",
  "discharge_diagnoses": [
    {
      "name": "肝细胞癌(BCLC B期,CNLC IIb期)",
      "diagnosis_type": "西医"
    },
    {
      "name": "慢性乙型病毒性肝炎",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤靶",
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
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 15:48:59,269 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-24]
2026-08-10 15:48:59,274 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1669928, prompt_len=618
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["第1页"]

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
2026-08-10 15:48:59,945 INFO     29 [qwen-vl-text] coord API raw response (len=62):
```json
[
	{"text": "第1页", "bbox": [473, 873, 531, 897]}
]
```
2026-08-10 15:48:59,945 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 15:48:59,945 INFO     29 [qwen-vl-text] coord item[0]: text=第1页, bbox=[473, 873, 531, 897]
2026-08-10 15:48:59,945 INFO     29 [qwen-vl-text] page=7 — 1/1 coords, api_time=0.7s
2026-08-10 15:48:59,950 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1580389, prompt_len=1776
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["入院日期：2025年03月18日", "出院日期：2025年03月24日", "住院天数：6天", "入院情况(简要病史\\体格检查及主要辅助检查)：患者男，57岁，因“反复右上腹部疼痛半年”入", "院。患者自诉半年余前开始无明显诱因下出现右上腹部疼痛，无恶心呕吐，无畏寒发热，自行缓解，1", "天前再发腹痛，至我院急诊就诊，行CT检查提示肝占位性病变，请我科医师会诊后，拟“肝占位性病", "变”收入我科住院。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。", "专科情况：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲", "张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓", "音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：", "2025-03-18上腹部CT平扫+增强扫描见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，", "请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺", "散在炎性灶。", "入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。", "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,", "2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白", "蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-", "谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，", "2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙", "肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，", "2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血", "酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+", "增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检"]

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
2026-08-10 15:49:11,817 INFO     29 [qwen-vl-text] coord API raw response (len=2141):
[
	{"text": "入院日期：2025年03月18日", "bbox": [113, 10, 312, 34]},
	{"text": "出院日期：2025年03月24日", "bbox": [363, 10, 564, 34]},
	{"text": "住院天数：6天", "bbox": [617, 10, 727, 34]},
	{"text": "入院情况(简要病史\\体格检查及主要辅助检查)：患者男，57岁，因“反复右上腹部疼痛半年”入", "bbox": [113, 51, 830, 77]},
	{"text": "院。患者自诉半年余前开始无明显诱因下出现右上腹部疼痛，无恶心呕吐，无畏寒发热，自行缓解，1", "bbox": [113, 93, 867, 118]},
	{"text": "天前再发腹痛，至我院急诊就诊，行CT检查提示肝占位性病变，请我科医师会诊后，拟“肝占位性病", "bbox": [113, 134, 858, 160]},
	{"text": "变”收入我科住院。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。", "bbox": [113, 176, 833, 202]},
	{"text": "专科情况：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲", "bbox": [113, 218, 857, 244]},
	{"text": "张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓", "bbox": [113, 260, 867, 286]},
	{"text": "音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：", "bbox": [113, 302, 813, 327]},
	{"text": "2025-03-18上腹部CT平扫+增强扫描见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，", "bbox": [113, 345, 848, 370]},
	{"text": "请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺", "bbox": [113, 386, 867, 412]},
	{"text": "散在炎性灶。", "bbox": [113, 428, 204, 454]},
	{"text": "入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。", "bbox": [113, 470, 662, 496]},
	{"text": "诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检", "bbox": [113, 512, 837, 538]},
	{"text": "验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,", "bbox": [113, 554, 812, 580]},
	{"text": "2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白", "bbox": [113, 595, 865, 621]},
	{"text": "蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-", "bbox": [113, 637, 858, 663]},
	{"text": "谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，", "bbox": [113, 679, 787, 705]},
	{"text": "2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙", "bbox": [113, 720, 857, 746]},
	{"text": "肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，", "bbox": [113, 762, 777, 788]},
	{"text": "2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血", "bbox": [113, 804, 864, 830]},
	{"text": "酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+", "bbox": [113, 846, 864, 872]},
	{"text": "增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检", "bbox": [113, 888, 855, 914]}
]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=11.9s
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[0]: text=入院日期：2025年03月18日, bbox=[113, 10, 312, 34]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[1]: text=出院日期：2025年03月24日, bbox=[363, 10, 564, 34]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[2]: text=住院天数：6天, bbox=[617, 10, 727, 34]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[3]: text=入院情况(简要病史\体格检查及主要辅助检查)：患者男，57岁，因“反复右上腹部疼痛半年”入, bbox=[113, 51, 830, 77]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[4]: text=院。患者自诉半年余前开始无明显诱因下出现右上腹部疼痛，无恶心呕吐，无畏寒发热，自行缓解，1, bbox=[113, 93, 867, 118]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[5]: text=天前再发腹痛，至我院急诊就诊，行CT检查提示肝占位性病变，请我科医师会诊后，拟“肝占位性病, bbox=[113, 134, 858, 160]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[6]: text=变”收入我科住院。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。, bbox=[113, 176, 833, 202]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[7]: text=专科情况：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲, bbox=[113, 218, 857, 244]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[8]: text=张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓, bbox=[113, 260, 867, 286]
2026-08-10 15:49:11,818 INFO     29 [qwen-vl-text] coord item[9]: text=音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：, bbox=[113, 302, 813, 327]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[10]: text=2025-03-18上腹部CT平扫+增强扫描见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，, bbox=[113, 345, 848, 370]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[11]: text=请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺, bbox=[113, 386, 867, 412]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[12]: text=散在炎性灶。, bbox=[113, 428, 204, 454]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[13]: text=入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。, bbox=[113, 470, 662, 496]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[14]: text=诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检, bbox=[113, 512, 837, 538]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[15]: text=验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,, bbox=[113, 554, 812, 580]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[16]: text=2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白, bbox=[113, 595, 865, 621]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[17]: text=蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-, bbox=[113, 637, 858, 663]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[18]: text=谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，, bbox=[113, 679, 787, 705]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[19]: text=2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙, bbox=[113, 720, 857, 746]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[20]: text=肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，, bbox=[113, 762, 777, 788]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[21]: text=2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血, bbox=[113, 804, 864, 830]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[22]: text=酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+, bbox=[113, 846, 864, 872]
2026-08-10 15:49:11,819 INFO     29 [qwen-vl-text] coord item[23]: text=增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检, bbox=[113, 888, 855, 914]
2026-08-10 15:49:11,820 INFO     29 [qwen-vl-text] page=8 — 24/24 coords, api_time=11.9s
2026-08-10 15:49:11,822 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1031383, prompt_len=665
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["临床诊断:1.肝细胞癌(BCLC B期,CNLC IIb期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶"]

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
2026-08-10 15:49:13,416 INFO     29 [qwen-vl-text] coord API raw response (len=107):
```json
[
	{"text": "临床诊断:1.肝细胞癌(BCLC B期,CNLC IIb期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶", "bbox": [48, 95, 926, 128]}
]
```
2026-08-10 15:49:13,416 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-10 15:49:13,416 INFO     29 [qwen-vl-text] coord item[0]: text=临床诊断:1.肝细胞癌(BCLC B期,CNLC IIb期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶, bbox=[48, 95, 926, 128]
2026-08-10 15:49:13,417 INFO     29 [qwen-vl-text] page=9 — 1/1 coords, api_time=1.6s
2026-08-10 15:49:13,417 INFO     29 [qwen-vl-text] new_positions (26):
[[7, 398.26599999999996, 447.102, 519.435, 533.715], [8, 95.146, 262.704, 5.949999999999999, 20.23], [8, 305.646, 474.888, 5.949999999999999, 20.23], [8, 519.514, 612.134, 5.949999999999999, 20.23], [8, 95.146, 698.86, 30.345, 45.815], [8, 95.146, 730.014, 55.335, 70.21], [8, 95.146, 722.4359999999999, 79.72999999999999, 95.19999999999999], [8, 95.146, 701.386, 104.72, 120.19], [8, 95.146, 721.5939999999999, 129.71, 145.18], [8, 95.146, 730.014, 154.7, 170.17], [8, 95.146, 684.5459999999999, 179.69, 194.565], [8, 95.146, 714.016, 205.27499999999998, 220.14999999999998], [8, 95.146, 730.014, 229.67, 245.14], [8, 95.146, 171.768, 254.66, 270.13], [8, 95.146, 557.404, 279.65, 295.12], [8, 95.146, 704.754, 304.64, 320.11], [8, 95.146, 683.704, 329.63, 345.09999999999997], [8, 95.146, 728.3299999999999, 354.025, 369.495], [8, 95.146, 722.4359999999999, 379.015, 394.48499999999996], [8, 95.146, 662.654, 404.005, 419.47499999999997], [8, 95.146, 721.5939999999999, 428.4, 443.87], [8, 95.146, 654.2339999999999, 453.39, 468.85999999999996], [8, 95.146, 727.4879999999999, 478.38, 493.84999999999997], [8, 95.146, 727.4879999999999, 503.37, 518.84], [8, 95.146, 719.91, 528.36, 543.8299999999999], [9, 28.56, 550.97, 79.99, 107.776]]
2026-08-10 15:49:13,417 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=3, time=30.0s
2026-08-10 15:49:13,441 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 15:49:13,442 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:Discharge | outputs={"chunks": "4 items, types={'DischargeRecord': 4}", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:49:13,442 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 15:49:13,449 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:49:13,450 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:49:13,450 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 15:49:13,450 INFO     29 [qwen-vl-text] positions(28): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:49:13,450 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [28]
2026-08-10 15:49:13,637 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 15:49:13,638 INFO     29 [qwen-vl-text] LLM extraction start, text_len=756
2026-08-10 15:49:13,638 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:49:13,639 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 27, \"encounter_dates\": [\"2025-09-16\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "族:汉族\n婚姻:已婚\n出生地:江西省南昌市湾里区\n业:其他\n现住址:江西省南昌市湾里区\n史陈述者:本人及家属\n与患者关系:其他\n可靠程度:基本可靠\n院时间:2025年09月16日 14:33\n记录时间:2025年09月16日 15:59\n诉:肝癌综合治疗5月余。\n病史:患者5月余前开始因肝癌于我院行综合治疗(介入+靶向+免疫:TACE+仑伐替尼+信迪利单\n), 后于2025年04月27日、2025年06月03日、2025年08月04日行肝动脉栓塞术。现患者为求下一周\n治疗来我院就诊。门诊拟\"肝癌介入治疗\"收入我科。患者自起病来, 饮食睡眠一般, 大小便如常,\n睡无明显变化。\n注史:患者既往身体较差。否认高血压病史。否认糖尿病史。否认冠心病史。否认肾病史。有肝炎\n史慢性乙型病毒性肝炎。否认结核病史。有手术史2025年03月20日、4月27日、06月03日、08月04日\n行肝动脉栓塞术, 肝局部灌注术, 肝动脉造影术, 动脉注射化疗药物, 肝动脉置管术手术。否认外伤史\n否认输血史。否认药物、食物过敏史。\n人史:生于原籍, 久居本地, 否认疫区、疫水接触史。否认毒物、放射性物质接触史。否认烟酒嗜好\n育史:已婚,[结婚年龄]适龄结婚, 配偶体健, 夫妻关系和睦。育有[育子数量]男、[育女数量]\n均体健。\n史:否认家族及遗传病史。\n体格检查\n体温:36.8℃ 脉搏:82次/分 呼吸:20次/分 血压:115/87mmHg\n正常, 营养中等, 表情自然, 无贫血貌, 自主体位, 步入病房, 步态正常, 神志清楚, 查体合作\n身皮肤黏膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣。全身浅表淋巴结未触及\n。头颅无畸形, 双眼睑无水肿, 眼球无突出及震颤, 结膜无苍白、无充血、无出血、无水肿, 巩",
    "role": "user"
  }
]
2026-08-10 15:49:20,982 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:49:20,982 INFO     29 [qwen-vl-text] LLM output (len=1597):
{
  "encounter_date": "2025-09-16",
  "dm_name": null,
  "dm_gender": null,
  "dm_age": null,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "其他",
  "dm_admission_time": "2025-09-16 14:33",
  "dm_record_time": "2025-09-16 15:59",
  "dm_history_provider": "本人及家属",
  "cc_text": "肝癌综合治疗5月余。",
  "cc_main_symptoms": [
    "肝癌"
  ],
  "cc_duration": "5月余",
  "pi_text": "患者5月余前开始因肝癌于我院行综合治疗(介入+靶向+免疫:TACE+仑伐替尼+信迪利单抗), 后于2025年04月27日、2025年06月03日、2025年08月04日行肝动脉栓塞术。现患者为求下一周期治疗来我院就诊。门诊拟\"肝癌介入治疗\"收入我科。患者自起病来, 饮食睡眠一般, 大小便如常, 体重无明显变化。",
  "pmh_disease_history": [
    "慢性乙型病毒性肝炎"
  ],
  "pmh_allergy_history": [],
  "pmh_surgery_trauma_history": [
    "2025年03月20日、4月27日、06月03日、08月04日行肝动脉栓塞术, 肝局部灌注术, 肝动脉造影术, 动脉注射化疗药物, 肝动脉置管术手术"
  ],
  "ph_smoking": "否认",
  "ph_drinking": "否认",
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "否认家族及遗传病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.8,
  "vs_pulse_bpm": 82,
  "vs_respiration_rpm": 20,
  "vs_systolic_bp_mmhg": 115,
  "vs_diastolic_bp_mmhg": 87,
  "pe_general_condition": "正常, 营养中等, 表情自然, 无贫血貌, 自主体位, 步入病房, 步态正常, 神志清楚, 查体合作",
  "pe_skin_mucosa": "全身皮肤黏膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣",
  "pe_lymph_nodes": "全身浅表淋巴结未触及",
  "pe_lungs": null,
  "pe_heart": null,
  "pe_abdomen": null,
  "pe_extremities": null,
  "pe_nervous_system": null,
  "pe_specialist_exam": null,
  "pe_ecog_score": null,
  "pat_text": null,
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "肝癌",
      "diagnosis_type": "西医",
      "is_primary": true
    }
  ],
  "department": null
}
2026-08-10 15:49:20,983 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-16]
2026-08-10 15:49:20,988 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1969210, prompt_len=1455
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["族:汉族", "婚姻:已婚", "出生地:江西省南昌市湾里区", "业:其他", "现住址:江西省南昌市湾里区", "史陈述者:本人及家属", "与患者关系:其他", "可靠程度:基本可靠", "院时间:2025年09月16日 14:33", "记录时间:2025年09月16日 15:59", "诉:肝癌综合治疗5月余。", "病史:患者5月余前开始因肝癌于我院行综合治疗(介入+靶向+免疫:TACE+仑伐替尼+信迪利单", "), 后于2025年04月27日、2025年06月03日、2025年08月04日行肝动脉栓塞术。现患者为求下一周", "治疗来我院就诊。门诊拟\"肝癌介入治疗\"收入我科。患者自起病来, 饮食睡眠一般, 大小便如常,", "睡无明显变化。", "注史:患者既往身体较差。否认高血压病史。否认糖尿病史。否认冠心病史。否认肾病史。有肝炎", "史慢性乙型病毒性肝炎。否认结核病史。有手术史2025年03月20日、4月27日、06月03日、08月04日", "行肝动脉栓塞术, 肝局部灌注术, 肝动脉造影术, 动脉注射化疗药物, 肝动脉置管术手术。否认外伤史", "否认输血史。否认药物、食物过敏史。", "人史:生于原籍, 久居本地, 否认疫区、疫水接触史。否认毒物、放射性物质接触史。否认烟酒嗜好", "育史:已婚,[结婚年龄]适龄结婚, 配偶体健, 夫妻关系和睦。育有[育子数量]男、[育女数量]", "均体健。", "史:否认家族及遗传病史。", "体格检查", "体温:36.8℃ 脉搏:82次/分 呼吸:20次/分 血压:115/87mmHg", "正常, 营养中等, 表情自然, 无贫血貌, 自主体位, 步入病房, 步态正常, 神志清楚, 查体合作", "身皮肤黏膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣。全身浅表淋巴结未触及", "。头颅无畸形, 双眼睑无水肿, 眼球无突出及震颤, 结膜无苍白、无充血、无出血、无水肿, 巩"]

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
2026-08-10 15:49:34,111 INFO     29 [qwen-vl-text] coord API raw response (len=1977):
[
	{"text": "族:汉族", "bbox": [138, 2, 192, 24]},
	{"text": "婚姻:已婚", "bbox": [398, 2, 471, 24]},
	{"text": "出生地:江西省南昌市湾里区", "bbox": [626, 2, 823, 24]},
	{"text": "业:其他", "bbox": [138, 41, 192, 63]},
	{"text": "现住址:江西省南昌市湾里区", "bbox": [398, 41, 593, 63]},
	{"text": "史陈述者:本人及家属", "bbox": [138, 81, 285, 103]},
	{"text": "与患者关系:其他", "bbox": [398, 81, 517, 103]},
	{"text": "可靠程度:基本可靠", "bbox": [626, 81, 760, 103]},
	{"text": "院时间:2025年09月16日 14:33", "bbox": [138, 120, 348, 142]},
	{"text": "记录时间:2025年09月16日 15:59", "bbox": [398, 120, 628, 142]},
	{"text": "诉:肝癌综合治疗5月余。", "bbox": [138, 160, 304, 182]},
	{"text": "病史:患者5月余前开始因肝癌于我院行综合治疗(介入+靶向+免疫:TACE+仑伐替尼+信迪利单", "bbox": [138, 197, 848, 219]},
	{"text": "), 后于2025年04月27日、2025年06月03日、2025年08月04日行肝动脉栓塞术。现患者为求下一周", "bbox": [138, 237, 848, 259]},
	{"text": "治疗来我院就诊。门诊拟\"肝癌介入治疗\"收入我科。患者自起病来, 饮食睡眠一般, 大小便如常,", "bbox": [138, 276, 839, 298]},
	{"text": "睡无明显变化。", "bbox": [138, 315, 237, 337]},
	{"text": "注史:患者既往身体较差。否认高血压病史。否认糖尿病史。否认冠心病史。否认肾病史。有肝炎", "bbox": [138, 354, 848, 376]},
	{"text": "史慢性乙型病毒性肝炎。否认结核病史。有手术史2025年03月20日、4月27日、06月03日、08月04日", "bbox": [138, 393, 847, 415]},
	{"text": "行肝动脉栓塞术, 肝局部灌注术, 肝动脉造影术, 动脉注射化疗药物, 肝动脉置管术手术。否认外伤史", "bbox": [138, 432, 847, 454]},
	{"text": "否认输血史。否认药物、食物过敏史。", "bbox": [138, 471, 393, 493]},
	{"text": "人史:生于原籍, 久居本地, 否认疫区、疫水接触史。否认毒物、放射性物质接触史。否认烟酒嗜好", "bbox": [138, 509, 847, 531]},
	{"text": "育史:已婚,[结婚年龄]适龄结婚, 配偶体健, 夫妻关系和睦。育有[育子数量]男、[育女数量]", "bbox": [138, 584, 845, 606]},
	{"text": "均体健。", "bbox": [148, 623, 202, 645]},
	{"text": "史:否认家族及遗传病史。", "bbox": [138, 662, 329, 684]},
	{"text": "体格检查", "bbox": [435, 700, 522, 722]},
	{"text": "体温:36.8℃ 脉搏:82次/分 呼吸:20次/分 血压:115/87mmHg", "bbox": [148, 738, 587, 760]},
	{"text": "正常, 营养中等, 表情自然, 无贫血貌, 自主体位, 步入病房, 步态正常, 神志清楚, 查体合作", "bbox": [148, 777, 845, 799]},
	{"text": "身皮肤黏膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣。全身浅表淋巴结未触及", "bbox": [148, 816, 845, 838]},
	{"text": "。头颅无畸形, 双眼睑无水肿, 眼球无突出及震颤, 结膜无苍白、无充血、无出血、无水肿, 巩", "bbox": [148, 855, 845, 877]}
]
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=13.1s
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord item[0]: text=族:汉族, bbox=[138, 2, 192, 24]
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord item[1]: text=婚姻:已婚, bbox=[398, 2, 471, 24]
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord item[2]: text=出生地:江西省南昌市湾里区, bbox=[626, 2, 823, 24]
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord item[3]: text=业:其他, bbox=[138, 41, 192, 63]
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord item[4]: text=现住址:江西省南昌市湾里区, bbox=[398, 41, 593, 63]
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord item[5]: text=史陈述者:本人及家属, bbox=[138, 81, 285, 103]
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord item[6]: text=与患者关系:其他, bbox=[398, 81, 517, 103]
2026-08-10 15:49:34,112 INFO     29 [qwen-vl-text] coord item[7]: text=可靠程度:基本可靠, bbox=[626, 81, 760, 103]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[8]: text=院时间:2025年09月16日 14:33, bbox=[138, 120, 348, 142]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[9]: text=记录时间:2025年09月16日 15:59, bbox=[398, 120, 628, 142]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[10]: text=诉:肝癌综合治疗5月余。, bbox=[138, 160, 304, 182]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[11]: text=病史:患者5月余前开始因肝癌于我院行综合治疗(介入+靶向+免疫:TACE+仑伐替尼+信迪利单, bbox=[138, 197, 848, 219]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[12]: text=), 后于2025年04月27日、2025年06月03日、2025年08月04日行肝动脉栓塞术。现患者为求下一周, bbox=[138, 237, 848, 259]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[13]: text=治疗来我院就诊。门诊拟"肝癌介入治疗"收入我科。患者自起病来, 饮食睡眠一般, 大小便如常,, bbox=[138, 276, 839, 298]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[14]: text=睡无明显变化。, bbox=[138, 315, 237, 337]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[15]: text=注史:患者既往身体较差。否认高血压病史。否认糖尿病史。否认冠心病史。否认肾病史。有肝炎, bbox=[138, 354, 848, 376]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[16]: text=史慢性乙型病毒性肝炎。否认结核病史。有手术史2025年03月20日、4月27日、06月03日、08月04日, bbox=[138, 393, 847, 415]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[17]: text=行肝动脉栓塞术, 肝局部灌注术, 肝动脉造影术, 动脉注射化疗药物, 肝动脉置管术手术。否认外伤史, bbox=[138, 432, 847, 454]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[18]: text=否认输血史。否认药物、食物过敏史。, bbox=[138, 471, 393, 493]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[19]: text=人史:生于原籍, 久居本地, 否认疫区、疫水接触史。否认毒物、放射性物质接触史。否认烟酒嗜好, bbox=[138, 509, 847, 531]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[20]: text=育史:已婚,[结婚年龄]适龄结婚, 配偶体健, 夫妻关系和睦。育有[育子数量]男、[育女数量], bbox=[138, 584, 845, 606]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[21]: text=均体健。, bbox=[148, 623, 202, 645]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[22]: text=史:否认家族及遗传病史。, bbox=[138, 662, 329, 684]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[23]: text=体格检查, bbox=[435, 700, 522, 722]
2026-08-10 15:49:34,113 INFO     29 [qwen-vl-text] coord item[24]: text=体温:36.8℃ 脉搏:82次/分 呼吸:20次/分 血压:115/87mmHg, bbox=[148, 738, 587, 760]
2026-08-10 15:49:34,114 INFO     29 [qwen-vl-text] coord item[25]: text=正常, 营养中等, 表情自然, 无贫血貌, 自主体位, 步入病房, 步态正常, 神志清楚, 查体合作, bbox=[148, 777, 845, 799]
2026-08-10 15:49:34,114 INFO     29 [qwen-vl-text] coord item[26]: text=身皮肤黏膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣。全身浅表淋巴结未触及, bbox=[148, 816, 845, 838]
2026-08-10 15:49:34,114 INFO     29 [qwen-vl-text] coord item[27]: text=。头颅无畸形, 双眼睑无水肿, 眼球无突出及震颤, 结膜无苍白、无充血、无出血、无水肿, 巩, bbox=[148, 855, 845, 877]
2026-08-10 15:49:34,115 INFO     29 [qwen-vl-text] page=0 — 28/28 coords, api_time=13.1s
2026-08-10 15:49:34,115 INFO     29 [qwen-vl-text] new_positions (28):
[[0, 116.196, 161.664, 1.19, 14.28], [0, 335.116, 396.582, 1.19, 14.28], [0, 527.092, 692.966, 1.19, 14.28], [0, 116.196, 161.664, 24.395, 37.485], [0, 335.116, 499.306, 24.395, 37.485], [0, 116.196, 239.97, 48.195, 61.285], [0, 335.116, 435.31399999999996, 48.195, 61.285], [0, 527.092, 639.92, 48.195, 61.285], [0, 116.196, 293.01599999999996, 71.39999999999999, 84.49], [0, 335.116, 528.776, 71.39999999999999, 84.49], [0, 116.196, 255.968, 95.19999999999999, 108.28999999999999], [0, 116.196, 714.016, 117.21499999999999, 130.305], [0, 116.196, 714.016, 141.015, 154.105], [0, 116.196, 706.438, 164.22, 177.31], [0, 116.196, 199.554, 187.42499999999998, 200.515], [0, 116.196, 714.016, 210.63, 223.72], [0, 116.196, 713.174, 233.83499999999998, 246.92499999999998], [0, 116.196, 713.174, 257.03999999999996, 270.13], [0, 116.196, 330.906, 280.245, 293.335], [0, 116.196, 713.174, 302.85499999999996, 315.945], [0, 116.196, 711.49, 347.47999999999996, 360.57], [0, 124.616, 170.084, 370.685, 383.775], [0, 116.196, 277.018, 393.89, 406.97999999999996], [0, 366.27, 439.524, 416.5, 429.59], [0, 124.616, 494.25399999999996, 439.10999999999996, 452.2], [0, 124.616, 711.49, 462.315, 475.405], [0, 124.616, 711.49, 485.52, 498.60999999999996], [0, 124.616, 711.49, 508.72499999999997, 521.8149999999999]]
2026-08-10 15:49:34,115 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=20.7s
2026-08-10 15:49:34,129 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 15:49:34,129 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:49:34,130 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 15:49:34,131 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:49:34.130+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:49:34,140 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:49:34,140 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:49:34,141 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:49:34,141 INFO     29 [qwen-vl-text] positions(20): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:49:34,141 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [20]
2026-08-10 15:49:34,339 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:49:34,341 INFO     29 [qwen-vl-text] LLM extraction start, text_len=611
2026-08-10 15:49:34,341 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:49:34,341 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 199, \"bbox_end\": 218, \"encounter_dates\": [\"2026-03-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗\n检查项目:上腹部薄层CT平扫+增强扫描\n检查所见:\n肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显\n强化,肿块边缘及邻近肝实质内多发稍低密度结节,边界欠清,部分融合,呈“快进快出”\n强化方式,部分与邻近肝内血管分界欠清,门静脉右后支纤细;肝右静脉显示不清,下腔静\n脉内见充盈缺损,肝中静脉受压推挤改变、局部显示欠清。另肝实质内见多发小圆形低密\n度,较大者直径约7mm,增强无强化。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积\n稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及\n腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见\n斑点状致密影。\n印象:\n“肝癌”综合治疗后,较2025-12-07日腹部CT:肝右叶肿块较前大小相仿,无明显血供;\n肿块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大,下腔静脉癌栓形成;余较前相\n仿。\n报告医师:梁利民\n审核医师:\n重要提示:本报告仅供临床医师诊断时参考 审核时间:2026-3-6 13:21:46\n医院咨询电话:0791-86120120(东湖):0791-87311120(红角洲):0791-85229772(青云谱)\n东湖影像科咨询电话:0791-86213393(登记室):0791-86301219(阅片室)",
    "role": "user"
  }
]
2026-08-10 15:49:38,265 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:49:38,265 INFO     29 [qwen-vl-text] LLM output (len=700):
{
  "exam_date": "2026-03-06",
  "report_date": "2026-03-06",
  "exam_name": "上腹部薄层CT平扫+增强扫描",
  "exam_category": "imaging",
  "body_part": "上腹部",
  "patient_name": null,
  "patient_gender": null,
  "department": "影像科",
  "bed_number": null,
  "findings": "肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显强化,肿块边缘及邻近肝实质内多发稍低密度结节,边界欠清,部分融合,呈“快进快出”强化方式,部分与邻近肝内血管分界欠清,门静脉右后支纤细;肝右静脉显示不清,下腔静脉内见充盈缺损,肝中静脉受压推挤改变、局部显示欠清。另肝实质内见多发小圆形低密度,较大者直径约7mm,增强无强化。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑点状致密影。",
  "conclusion": "“肝癌”综合治疗后,较2025-12-07日腹部CT:肝右叶肿块较前大小相仿,无明显血供;肿块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大,下腔静脉癌栓形成;余较前相仿。",
  "physician": "梁利民",
  "reviewer": null
}
2026-08-10 15:49:38,268 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1031383, prompt_len=1284
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗", "检查项目:上腹部薄层CT平扫+增强扫描", "检查所见:", "肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显", "强化,肿块边缘及邻近肝实质内多发稍低密度结节,边界欠清,部分融合,呈“快进快出”", "强化方式,部分与邻近肝内血管分界欠清,门静脉右后支纤细;肝右静脉显示不清,下腔静", "脉内见充盈缺损,肝中静脉受压推挤改变、局部显示欠清。另肝实质内见多发小圆形低密", "度,较大者直径约7mm,增强无强化。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积", "稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及", "腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见", "斑点状致密影。", "印象:", "“肝癌”综合治疗后,较2025-12-07日腹部CT:肝右叶肿块较前大小相仿,无明显血供;", "肿块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大,下腔静脉癌栓形成;余较前相", "仿。", "报告医师:梁利民", "审核医师:", "重要提示:本报告仅供临床医师诊断时参考 审核时间:2026-3-6 13:21:46", "医院咨询电话:0791-86120120(东湖):0791-87311120(红角洲):0791-85229772(青云谱)", "东湖影像科咨询电话:0791-86213393(登记室):0791-86301219(阅片室)"]

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
2026-08-10 15:49:46,294 INFO     29 [qwen-vl-text] coord API raw response (len=1552):
[
	{"text": "向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗", "bbox": [150, 111, 617, 128]},
	{"text": "检查项目:上腹部薄层CT平扫+增强扫描", "bbox": [47, 145, 451, 164]},
	{"text": "检查所见:", "bbox": [47, 188, 150, 206]},
	{"text": "肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显", "bbox": [47, 219, 934, 238]},
	{"text": "强化,肿块边缘及邻近肝实质内多发稍低密度结节,边界欠清,部分融合,呈“快进快出”", "bbox": [47, 240, 924, 259]},
	{"text": "强化方式,部分与邻近肝内血管分界欠清,门静脉右后支纤细;肝右静脉显示不清,下腔静", "bbox": [47, 262, 934, 280]},
	{"text": "脉内见充盈缺损,肝中静脉受压推挤改变、局部显示欠清。另肝实质内见多发小圆形低密", "bbox": [47, 283, 910, 301]},
	{"text": "度,较大者直径约7mm,增强无强化。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积", "bbox": [47, 304, 923, 323]},
	{"text": "稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及", "bbox": [47, 326, 934, 344]},
	{"text": "腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见", "bbox": [47, 347, 934, 365]},
	{"text": "斑点状致密影。", "bbox": [47, 369, 187, 386]},
	{"text": "印象:", "bbox": [47, 466, 103, 484]},
	{"text": "“肝癌”综合治疗后,较2025-12-07日腹部CT:肝右叶肿块较前大小相仿,无明显血供;", "bbox": [77, 491, 918, 509]},
	{"text": "肿块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大,下腔静脉癌栓形成;余较前相", "bbox": [47, 512, 933, 530]},
	{"text": "仿。", "bbox": [47, 533, 79, 551]},
	{"text": "报告医师:梁利民", "bbox": [50, 757, 238, 775]},
	{"text": "审核医师:", "bbox": [591, 757, 695, 775]},
	{"text": "重要提示:本报告仅供临床医师诊断时参考 审核时间:2026-3-6 13:21:46", "bbox": [147, 797, 875, 815]},
	{"text": "医院咨询电话:0791-86120120(东湖):0791-87311120(红角洲):0791-85229772(青云谱)", "bbox": [147, 819, 853, 834]},
	{"text": "东湖影像科咨询电话:0791-86213393(登记室):0791-86301219(阅片室)", "bbox": [147, 834, 716, 849]},
	{"text": "红角洲影像科咨询电话:0791-86257676(阅片室)", "bbox": [147, 849, 527, 862]}
]
2026-08-10 15:49:46,295 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=8.0s
2026-08-10 15:49:46,295 INFO     29 [qwen-vl-text] coord item[0]: text=向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗, bbox=[150, 111, 617, 128]
2026-08-10 15:49:46,295 INFO     29 [qwen-vl-text] coord item[1]: text=检查项目:上腹部薄层CT平扫+增强扫描, bbox=[47, 145, 451, 164]
2026-08-10 15:49:46,295 INFO     29 [qwen-vl-text] coord item[2]: text=检查所见:, bbox=[47, 188, 150, 206]
2026-08-10 15:49:46,295 INFO     29 [qwen-vl-text] coord item[3]: text=肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显, bbox=[47, 219, 934, 238]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[4]: text=强化,肿块边缘及邻近肝实质内多发稍低密度结节,边界欠清,部分融合,呈“快进快出”, bbox=[47, 240, 924, 259]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[5]: text=强化方式,部分与邻近肝内血管分界欠清,门静脉右后支纤细;肝右静脉显示不清,下腔静, bbox=[47, 262, 934, 280]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[6]: text=脉内见充盈缺损,肝中静脉受压推挤改变、局部显示欠清。另肝实质内见多发小圆形低密, bbox=[47, 283, 910, 301]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[7]: text=度,较大者直径约7mm,增强无强化。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积, bbox=[47, 304, 923, 323]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[8]: text=稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及, bbox=[47, 326, 934, 344]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[9]: text=腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见, bbox=[47, 347, 934, 365]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[10]: text=斑点状致密影。, bbox=[47, 369, 187, 386]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[11]: text=印象:, bbox=[47, 466, 103, 484]
2026-08-10 15:49:46,296 INFO     29 [qwen-vl-text] coord item[12]: text=“肝癌”综合治疗后,较2025-12-07日腹部CT:肝右叶肿块较前大小相仿,无明显血供;, bbox=[77, 491, 918, 509]
2026-08-10 15:49:46,297 INFO     29 [qwen-vl-text] coord item[13]: text=肿块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大,下腔静脉癌栓形成;余较前相, bbox=[47, 512, 933, 530]
2026-08-10 15:49:46,297 INFO     29 [qwen-vl-text] coord item[14]: text=仿。, bbox=[47, 533, 79, 551]
2026-08-10 15:49:46,297 INFO     29 [qwen-vl-text] coord item[15]: text=报告医师:梁利民, bbox=[50, 757, 238, 775]
2026-08-10 15:49:46,297 INFO     29 [qwen-vl-text] coord item[16]: text=审核医师:, bbox=[591, 757, 695, 775]
2026-08-10 15:49:46,297 INFO     29 [qwen-vl-text] coord item[17]: text=重要提示:本报告仅供临床医师诊断时参考 审核时间:2026-3-6 13:21:46, bbox=[147, 797, 875, 815]
2026-08-10 15:49:46,297 INFO     29 [qwen-vl-text] coord item[18]: text=医院咨询电话:0791-86120120(东湖):0791-87311120(红角洲):0791-85229772(青云谱), bbox=[147, 819, 853, 834]
2026-08-10 15:49:46,297 INFO     29 [qwen-vl-text] coord item[19]: text=东湖影像科咨询电话:0791-86213393(登记室):0791-86301219(阅片室), bbox=[147, 834, 716, 849]
2026-08-10 15:49:46,297 INFO     29 [qwen-vl-text] coord item[20]: text=红角洲影像科咨询电话:0791-86257676(阅片室), bbox=[147, 849, 527, 862]
2026-08-10 15:49:46,298 INFO     29 [qwen-vl-text] page=9 — 20/20 coords, api_time=8.0s
2026-08-10 15:49:46,298 INFO     29 [qwen-vl-text] new_positions (20):
[[9, 89.25, 367.115, 93.462, 107.776], [9, 27.965, 268.34499999999997, 122.08999999999999, 138.088], [9, 27.965, 89.25, 158.296, 173.452], [9, 27.965, 555.73, 184.398, 200.396], [9, 27.965, 549.78, 202.07999999999998, 218.078], [9, 27.965, 555.73, 220.60399999999998, 235.76], [9, 27.965, 541.4499999999999, 238.286, 253.44199999999998], [9, 27.965, 549.185, 255.968, 271.966], [9, 27.965, 555.73, 274.492, 289.64799999999997], [9, 27.965, 555.73, 292.174, 307.33], [9, 27.965, 111.265, 310.698, 325.012], [9, 27.965, 61.285, 392.372, 407.52799999999996], [9, 45.815, 546.2099999999999, 413.42199999999997, 428.578], [9, 27.965, 555.135, 431.104, 446.26], [9, 27.965, 47.004999999999995, 448.786, 463.942], [9, 29.75, 141.60999999999999, 637.394, 652.55], [9, 351.645, 413.525, 637.394, 652.55], [9, 87.46499999999999, 520.625, 671.074, 686.23], [9, 87.46499999999999, 507.53499999999997, 689.598, 702.228], [9, 87.46499999999999, 426.02, 702.228, 714.858]]
2026-08-10 15:49:46,298 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=1, time=12.2s
2026-08-10 15:49:46,298 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:49:46,310 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:49:46,310 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:49:46,310 INFO     29 [qwen-vl-text] positions(24): [[9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:49:46,310 INFO     29 [qwen-vl-text] page grouping: [9, 10], lines per page: [1, 23]
2026-08-10 15:49:46,505 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:49:46,708 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:49:46,709 INFO     29 [qwen-vl-text] LLM extraction start, text_len=746
2026-08-10 15:49:46,709 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:49:46,710 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 219, \"bbox_end\": 242, \"encounter_dates\": [\"2025-12-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "红角洲影像科咨询电话:0791-86257676(\n临床诊断:1.肝细胞癌(BCLC B期,CNLC 11b期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶\n向治疗,4.恶性肿瘤免疫治疗\n检查项目:上腹部薄层CT平扫+增强扫描\n检查所见:\n肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显\n强化,肿块边缘及邻近肝实质内多个稍低密度结节,呈“快进快出”强化方式,大者大小约\n54mm×31mm,部分与邻近肝内血管分界欠清。另肝实质内见多发小圆形低密度,较大者直径\n约7mm,增强无强化。门静脉右后支纤细,似见条状充盈缺损;肝右静脉显示不清,肝中静\n脉受压推挤改变、局部显示欠清。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍\n大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹\n膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑\n点状致密影。\n印象:\n肝癌综合治疗后,对比2025-9-10日CT:肝右叶肿块较前大小相仿,无明显血供;新增肿块\n边缘及邻近肝实质内多个子灶或转移灶,有活性,个别病灶与肝中静脉分界不清;胆囊壁水\n肿基本缓解;余较前相仿。\n报告医师:冯梓妍\n审核医师:\n熊小丽\n重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-12-7 16:33:54\n医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)\n东南影像科咨询电话:0791-86213393(登记室);0791-86301219(阅片室)\n红角洲影像科咨询电话:0791-86357670(骨记室);0701:87357668(原片室)",
    "role": "user"
  }
]
2026-08-10 15:49:50,644 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:49:50,644 INFO     29 [qwen-vl-text] LLM output (len=713):
{
  "exam_date": "2025-12-07",
  "report_date": "2025-12-07",
  "exam_name": "上腹部薄层CT平扫+增强扫描",
  "exam_category": "imaging",
  "body_part": "上腹部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显强化,肿块边缘及邻近肝实质内多个稍低密度结节,呈“快进快出”强化方式,大者大小约54mm×31mm,部分与邻近肝内血管分界欠清。另肝实质内见多发小圆形低密度,较大者直径约7mm,增强无强化。门静脉右后支纤细,似见条状充盈缺损;肝右静脉显示不清,肝中静脉受压推挤改变、局部显示欠清。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑点状致密影。",
  "conclusion": "肝癌综合治疗后,对比2025-9-10日CT:肝右叶肿块较前大小相仿,无明显血供;新增肿块边缘及邻近肝实质内多个子灶或转移灶,有活性,个别病灶与肝中静脉分界不清;胆囊壁水肿基本缓解;余较前相仿。",
  "physician": "冯梓妍",
  "reviewer": "熊小丽"
}
2026-08-10 15:49:50,649 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1031383, prompt_len=640
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["红角洲影像科咨询电话:0791-86257676("]

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
2026-08-10 15:49:51,440 INFO     29 [qwen-vl-text] coord API raw response (len=84):
```json
[
	{"text": "红角洲影像科咨询电话:0791-86257676(", "bbox": [147, 847, 528, 862]}
]
```
2026-08-10 15:49:51,440 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.8s
2026-08-10 15:49:51,440 INFO     29 [qwen-vl-text] coord item[0]: text=红角洲影像科咨询电话:0791-86257676(, bbox=[147, 847, 528, 862]
2026-08-10 15:49:51,441 INFO     29 [qwen-vl-text] page=9 — 1/1 coords, api_time=0.8s
2026-08-10 15:49:51,447 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1099485, prompt_len=1402
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["临床诊断:1.肝细胞癌(BCLC B期,CNLC 11b期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶", "向治疗,4.恶性肿瘤免疫治疗", "检查项目:上腹部薄层CT平扫+增强扫描", "检查所见:", "肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显", "强化,肿块边缘及邻近肝实质内多个稍低密度结节,呈“快进快出”强化方式,大者大小约", "54mm×31mm,部分与邻近肝内血管分界欠清。另肝实质内见多发小圆形低密度,较大者直径", "约7mm,增强无强化。门静脉右后支纤细,似见条状充盈缺损;肝右静脉显示不清,肝中静", "脉受压推挤改变、局部显示欠清。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍", "大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹", "膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑", "点状致密影。", "印象:", "肝癌综合治疗后,对比2025-9-10日CT:肝右叶肿块较前大小相仿,无明显血供;新增肿块", "边缘及邻近肝实质内多个子灶或转移灶,有活性,个别病灶与肝中静脉分界不清;胆囊壁水", "肿基本缓解;余较前相仿。", "报告医师:冯梓妍", "审核医师:", "熊小丽", "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-12-7 16:33:54", "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)", "东南影像科咨询电话:0791-86213393(登记室);0791-86301219(阅片室)", "红角洲影像科咨询电话:0791-86357670(骨记室);0701:87357668(原片室)"]

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
2026-08-10 15:50:03,146 INFO     29 [qwen-vl-text] coord API raw response (len=1717):
[
	{"text": "临床诊断:1.肝细胞癌(BCLC B期,CNLC 11b期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶", "bbox": [40, 90, 921, 109]},
	{"text": "向治疗,4.恶性肿瘤免疫治疗", "bbox": [142, 107, 437, 123]},
	{"text": "检查项目:上腹部薄层CT平扫+增强扫描", "bbox": [40, 140, 445, 158]},
	{"text": "检查所见:", "bbox": [40, 182, 144, 200]},
	{"text": "肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显", "bbox": [40, 214, 929, 232]},
	{"text": "强化,肿块边缘及邻近肝实质内多个稍低密度结节,呈“快进快出”强化方式,大者大小约", "bbox": [40, 235, 929, 253]},
	{"text": "54mm×31mm,部分与邻近肝内血管分界欠清。另肝实质内见多发小圆形低密度,较大者直径", "bbox": [40, 257, 929, 275]},
	{"text": "约7mm,增强无强化。门静脉右后支纤细,似见条状充盈缺损;肝右静脉显示不清,肝中静", "bbox": [40, 278, 917, 296]},
	{"text": "脉受压推挤改变、局部显示欠清。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍", "bbox": [40, 299, 906, 317]},
	{"text": "大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹", "bbox": [40, 321, 929, 339]},
	{"text": "膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑", "bbox": [40, 342, 929, 360]},
	{"text": "点状致密影。", "bbox": [40, 364, 159, 381]},
	{"text": "印象:", "bbox": [40, 452, 95, 469]},
	{"text": "肝癌综合治疗后,对比2025-9-10日CT:肝右叶肿块较前大小相仿,无明显血供;新增肿块", "bbox": [40, 477, 917, 495]},
	{"text": "边缘及邻近肝实质内多个子灶或转移灶,有活性,个别病灶与肝中静脉分界不清;胆囊壁水", "bbox": [40, 499, 927, 517]},
	{"text": "肿基本缓解;余较前相仿。", "bbox": [40, 520, 292, 537]},
	{"text": "报告医师:冯梓妍", "bbox": [44, 754, 231, 772]},
	{"text": "审核医师:", "bbox": [585, 754, 690, 772]},
	{"text": "熊小丽", "bbox": [724, 740, 853, 780]},
	{"text": "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-12-7 16:33:54", "bbox": [142, 795, 881, 812]},
	{"text": "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)", "bbox": [142, 817, 848, 831]},
	{"text": "东南影像科咨询电话:0791-86213393(登记室);0791-86301219(阅片室)", "bbox": [142, 831, 711, 845]},
	{"text": "红角洲影像科咨询电话:0791-86357670(骨记室);0701:87357668(原片室)", "bbox": [142, 845, 728, 859]}
]
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=11.7s
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord item[0]: text=临床诊断:1.肝细胞癌(BCLC B期,CNLC 11b期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶, bbox=[40, 90, 921, 109]
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord item[1]: text=向治疗,4.恶性肿瘤免疫治疗, bbox=[142, 107, 437, 123]
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord item[2]: text=检查项目:上腹部薄层CT平扫+增强扫描, bbox=[40, 140, 445, 158]
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord item[3]: text=检查所见:, bbox=[40, 182, 144, 200]
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord item[4]: text=肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显, bbox=[40, 214, 929, 232]
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord item[5]: text=强化,肿块边缘及邻近肝实质内多个稍低密度结节,呈“快进快出”强化方式,大者大小约, bbox=[40, 235, 929, 253]
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord item[6]: text=54mm×31mm,部分与邻近肝内血管分界欠清。另肝实质内见多发小圆形低密度,较大者直径, bbox=[40, 257, 929, 275]
2026-08-10 15:50:03,147 INFO     29 [qwen-vl-text] coord item[7]: text=约7mm,增强无强化。门静脉右后支纤细,似见条状充盈缺损;肝右静脉显示不清,肝中静, bbox=[40, 278, 917, 296]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[8]: text=脉受压推挤改变、局部显示欠清。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍, bbox=[40, 299, 906, 317]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[9]: text=大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹, bbox=[40, 321, 929, 339]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[10]: text=膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑, bbox=[40, 342, 929, 360]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[11]: text=点状致密影。, bbox=[40, 364, 159, 381]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[12]: text=印象:, bbox=[40, 452, 95, 469]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[13]: text=肝癌综合治疗后,对比2025-9-10日CT:肝右叶肿块较前大小相仿,无明显血供;新增肿块, bbox=[40, 477, 917, 495]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[14]: text=边缘及邻近肝实质内多个子灶或转移灶,有活性,个别病灶与肝中静脉分界不清;胆囊壁水, bbox=[40, 499, 927, 517]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[15]: text=肿基本缓解;余较前相仿。, bbox=[40, 520, 292, 537]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[16]: text=报告医师:冯梓妍, bbox=[44, 754, 231, 772]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[17]: text=审核医师:, bbox=[585, 754, 690, 772]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[18]: text=熊小丽, bbox=[724, 740, 853, 780]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[19]: text=重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-12-7 16:33:54, bbox=[142, 795, 881, 812]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[20]: text=医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱), bbox=[142, 817, 848, 831]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[21]: text=东南影像科咨询电话:0791-86213393(登记室);0791-86301219(阅片室), bbox=[142, 831, 711, 845]
2026-08-10 15:50:03,148 INFO     29 [qwen-vl-text] coord item[22]: text=红角洲影像科咨询电话:0791-86357670(骨记室);0701:87357668(原片室), bbox=[142, 845, 728, 859]
2026-08-10 15:50:03,149 INFO     29 [qwen-vl-text] page=10 — 23/23 coords, api_time=11.7s
2026-08-10 15:50:03,149 INFO     29 [qwen-vl-text] new_positions (24):
[[9, 87.46499999999999, 314.15999999999997, 713.174, 725.804], [10, 23.799999999999997, 547.995, 75.78, 91.77799999999999], [10, 84.49, 260.015, 90.094, 103.566], [10, 23.799999999999997, 264.775, 117.88, 133.036], [10, 23.799999999999997, 85.67999999999999, 153.244, 168.4], [10, 23.799999999999997, 552.755, 180.188, 195.344], [10, 23.799999999999997, 552.755, 197.87, 213.02599999999998], [10, 23.799999999999997, 552.755, 216.394, 231.54999999999998], [10, 23.799999999999997, 545.615, 234.076, 249.232], [10, 23.799999999999997, 539.0699999999999, 251.75799999999998, 266.914], [10, 23.799999999999997, 552.755, 270.282, 285.438], [10, 23.799999999999997, 552.755, 287.964, 303.12], [10, 23.799999999999997, 94.60499999999999, 306.488, 320.80199999999996], [10, 23.799999999999997, 56.525, 380.584, 394.89799999999997], [10, 23.799999999999997, 545.615, 401.63399999999996, 416.78999999999996], [10, 23.799999999999997, 551.5649999999999, 420.15799999999996, 435.31399999999996], [10, 23.799999999999997, 173.73999999999998, 437.84, 452.154], [10, 26.18, 137.445, 634.8679999999999, 650.024], [10, 348.075, 410.54999999999995, 634.8679999999999, 650.024], [10, 430.78, 507.53499999999997, 623.0799999999999, 656.76], [10, 84.49, 524.1949999999999, 669.39, 683.704], [10, 84.49, 504.56, 687.914, 699.702], [10, 84.49, 423.04499999999996, 699.702, 711.49], [10, 84.49, 433.15999999999997, 711.49, 723.278]]
2026-08-10 15:50:03,149 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=2, time=16.9s
2026-08-10 15:50:03,149 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:50:03,151 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:50:03,151 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:50:03,151 INFO     29 [qwen-vl-text] positions(15): [[10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:50:03,152 INFO     29 [qwen-vl-text] page grouping: [10, 11], lines per page: [1, 14]
2026-08-10 15:50:03,360 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:50:03,514 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:50:03,515 INFO     29 [qwen-vl-text] LLM extraction start, text_len=380
2026-08-10 15:50:03,515 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:50:03,515 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 243, \"bbox_end\": 257, \"encounter_dates\": [\"2025-09-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "第1页 共1页\n临床诊断:1.肝癌介入治疗,2.原发性肝癌\n检查项目:胸部CT平扫\n检查所见:\n两肺纹理增粗增多,右肺上叶见一类圆形小囊泡。两下肺见散在条索及条带状实变影,\n边界清;右下肺前基底段见不规则实性密度条片影(SE202IM184),大小约21mm×13mm;\n两肺散在少许直径约2-3mm微小结节影,界清。气管、主要支气管通畅,两肺门及纵隔未见\n明确肿大淋巴结。心脏不大,双侧胸膜无明显增厚,胸腔内未见积液。\n印象:\n对比2025-8-4胸部CT:右下肺实性结节影较前稍减小,请结合临床;两下肺胸膜下渗出\n及条索灶较前减少吸收;余大致同前。\n报告医师:肖轩\n审核医师:钟玉凤\n重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-9-11 8:39:32\n医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲)",
    "role": "user"
  }
]
2026-08-10 15:50:06,074 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:50:06.071+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 69, "failed": 0, "current": {"3d95d73c94d211f1bd9827cf206dfa2d": {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:50:06,537 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:50:06,537 INFO     29 [qwen-vl-text] LLM output (len=531):
{
  "exam_date": "2025-09-11",
  "report_date": "2025-09-11",
  "exam_name": "胸部CT平扫",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "两肺纹理增粗增多,右肺上叶见一类圆形小囊泡。两下肺见散在条索及条带状实变影,边界清;右下肺前基底段见不规则实性密度条片影(SE202IM184),大小约21mm×13mm;两肺散在少许直径约2-3mm微小结节影,界清。气管、主要支气管通畅,两肺门及纵隔未见明确肿大淋巴结。心脏不大,双侧胸膜无明显增厚,胸腔内未见积液。",
  "conclusion": "对比2025-8-4胸部CT:右下肺实性结节影较前稍减小,请结合临床;两下肺胸膜下渗出及条索灶较前减少吸收;余大致同前。",
  "physician": "肖轩",
  "reviewer": "钟玉凤"
}
2026-08-10 15:50:06,539 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1099485, prompt_len=622
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["第1页 共1页"]

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
2026-08-10 15:50:07,243 INFO     29 [qwen-vl-text] coord API raw response (len=66):
```json
[
	{"text": "第1页 共1页", "bbox": [802, 844, 930, 857]}
]
```
2026-08-10 15:50:07,243 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 15:50:07,244 INFO     29 [qwen-vl-text] coord item[0]: text=第1页 共1页, bbox=[802, 844, 930, 857]
2026-08-10 15:50:07,244 INFO     29 [qwen-vl-text] page=10 — 1/1 coords, api_time=0.7s
2026-08-10 15:50:07,247 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=623088, prompt_len=1027
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["临床诊断:1.肝癌介入治疗,2.原发性肝癌", "检查项目:胸部CT平扫", "检查所见:", "两肺纹理增粗增多,右肺上叶见一类圆形小囊泡。两下肺见散在条索及条带状实变影,", "边界清;右下肺前基底段见不规则实性密度条片影(SE202IM184),大小约21mm×13mm;", "两肺散在少许直径约2-3mm微小结节影,界清。气管、主要支气管通畅,两肺门及纵隔未见", "明确肿大淋巴结。心脏不大,双侧胸膜无明显增厚,胸腔内未见积液。", "印象:", "对比2025-8-4胸部CT:右下肺实性结节影较前稍减小,请结合临床;两下肺胸膜下渗出", "及条索灶较前减少吸收;余大致同前。", "报告医师:肖轩", "审核医师:钟玉凤", "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-9-11 8:39:32", "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲)"]

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
2026-08-10 15:50:13,245 INFO     29 [qwen-vl-text] coord API raw response (len=981):
[
	{"text": "临床诊断:1.肝癌介入治疗,2.原发性肝癌", "bbox": [72, 101, 503, 119]},
	{"text": "检查项目:胸部CT平扫", "bbox": [71, 142, 305, 160]},
	{"text": "检查所见:", "bbox": [71, 184, 177, 202]},
	{"text": "两肺纹理增粗增多,右肺上叶见一类圆形小囊泡。两下肺见散在条索及条带状实变影,", "bbox": [71, 216, 969, 235]},
	{"text": "边界清;右下肺前基底段见不规则实性密度条片影(SE202IM184),大小约21mm×13mm;", "bbox": [71, 238, 957, 257]},
	{"text": "两肺散在少许直径约2-3mm微小结节影,界清。气管、主要支气管通畅,两肺门及纵隔未见", "bbox": [71, 260, 971, 279]},
	{"text": "明确肿大淋巴结。心脏不大,双侧胸膜无明显增厚,胸腔内未见积液。", "bbox": [71, 282, 763, 300]},
	{"text": "印象:", "bbox": [69, 458, 124, 476]},
	{"text": "对比2025-8-4胸部CT:右下肺实性结节影较前稍减小,请结合临床;两下肺胸膜下渗出", "bbox": [100, 485, 965, 503]},
	{"text": "及条索灶较前减少吸收;余大致同前。", "bbox": [68, 507, 438, 524]},
	{"text": "报告医师:肖轩", "bbox": [67, 774, 235, 792]},
	{"text": "审核医师:钟玉凤", "bbox": [621, 774, 728, 792]},
	{"text": "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-9-11 8:39:32", "bbox": [165, 816, 915, 834]},
	{"text": "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲)", "bbox": [165, 838, 677, 854]}
]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=6.0s
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[0]: text=临床诊断:1.肝癌介入治疗,2.原发性肝癌, bbox=[72, 101, 503, 119]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[1]: text=检查项目:胸部CT平扫, bbox=[71, 142, 305, 160]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[2]: text=检查所见:, bbox=[71, 184, 177, 202]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[3]: text=两肺纹理增粗增多,右肺上叶见一类圆形小囊泡。两下肺见散在条索及条带状实变影,, bbox=[71, 216, 969, 235]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[4]: text=边界清;右下肺前基底段见不规则实性密度条片影(SE202IM184),大小约21mm×13mm;, bbox=[71, 238, 957, 257]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[5]: text=两肺散在少许直径约2-3mm微小结节影,界清。气管、主要支气管通畅,两肺门及纵隔未见, bbox=[71, 260, 971, 279]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[6]: text=明确肿大淋巴结。心脏不大,双侧胸膜无明显增厚,胸腔内未见积液。, bbox=[71, 282, 763, 300]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[7]: text=印象:, bbox=[69, 458, 124, 476]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[8]: text=对比2025-8-4胸部CT:右下肺实性结节影较前稍减小,请结合临床;两下肺胸膜下渗出, bbox=[100, 485, 965, 503]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[9]: text=及条索灶较前减少吸收;余大致同前。, bbox=[68, 507, 438, 524]
2026-08-10 15:50:13,246 INFO     29 [qwen-vl-text] coord item[10]: text=报告医师:肖轩, bbox=[67, 774, 235, 792]
2026-08-10 15:50:13,247 INFO     29 [qwen-vl-text] coord item[11]: text=审核医师:钟玉凤, bbox=[621, 774, 728, 792]
2026-08-10 15:50:13,247 INFO     29 [qwen-vl-text] coord item[12]: text=重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-9-11 8:39:32, bbox=[165, 816, 915, 834]
2026-08-10 15:50:13,247 INFO     29 [qwen-vl-text] coord item[13]: text=医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲), bbox=[165, 838, 677, 854]
2026-08-10 15:50:13,247 INFO     29 [qwen-vl-text] page=11 — 14/14 coords, api_time=6.0s
2026-08-10 15:50:13,247 INFO     29 [qwen-vl-text] new_positions (15):
[[10, 477.19, 553.35, 710.648, 721.5939999999999], [11, 42.839999999999996, 299.28499999999997, 85.042, 100.198], [11, 42.245, 181.475, 119.564, 134.72], [11, 42.245, 105.315, 154.928, 170.084], [11, 42.245, 576.555, 181.87199999999999, 197.87], [11, 42.245, 569.415, 200.396, 216.394], [11, 42.245, 577.745, 218.92, 234.91799999999998], [11, 42.245, 453.98499999999996, 237.444, 252.6], [11, 41.055, 73.78, 385.63599999999997, 400.792], [11, 59.5, 574.175, 408.37, 423.526], [11, 40.46, 260.61, 426.894, 441.20799999999997], [11, 39.864999999999995, 139.825, 651.708, 666.864], [11, 369.495, 433.15999999999997, 651.708, 666.864], [11, 98.175, 544.425, 687.072, 702.228], [11, 98.175, 402.815, 705.596, 719.068]]
2026-08-10 15:50:13,247 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=2, time=10.1s
2026-08-10 15:50:13,248 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:50:13,249 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:50:13,250 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:50:13,250 INFO     29 [qwen-vl-text] positions(20): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:50:13,250 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [20]
2026-08-10 15:50:13,432 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 15:50:13,434 INFO     29 [qwen-vl-text] LLM extraction start, text_len=583
2026-08-10 15:50:13,434 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:50:13,434 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 258, \"bbox_end\": 277, \"encounter_dates\": [\"2025-06-03\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期),3.慢性乙型病毒性\n肝炎\n检查项目:上腹部CT平扫+增强扫描\n检查所见:\n肝内见团块状低密度影,其周围见多发斑片状高密度影,增强扫描动脉期肿瘤边缘无碘\n油沉积区见不均匀强化影,平衡期强化程度减低,病灶中心见无强化低密度区;另肝实质内\n见多发小圆形低密度,较大者直径约7mm,增强无强化。肝中及肝左静脉显示欠清,肝内外\n胆管无明显扩张。胆囊不大,壁无增厚。脾脏体积不大,实质密度强化均匀;胰腺大小、形\n态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短\n径约10mm,轻度强化。腹腔内未见积液。所示左肾盏见斑点高密度影。\n印象:\n肝癌综合治疗后,与2025-3-18片比较:\n肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及\n实验室资料;\n肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。\n报告医师:钟芳琴\n审核医师:邓军\n重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-6-3 16:42:51\n医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)\n东湖影像科咨询电话:0791 86212009(部门otn)",
    "role": "user"
  }
]
2026-08-10 15:50:17,038 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:50:17,038 INFO     29 [qwen-vl-text] LLM output (len=665):
{
  "exam_date": "2025-06-03",
  "report_date": "2025-06-03",
  "exam_name": "上腹部CT平扫+增强扫描",
  "exam_category": "imaging",
  "body_part": "上腹部",
  "patient_name": null,
  "patient_gender": null,
  "department": "东湖影像科",
  "bed_number": null,
  "findings": "肝内见团块状低密度影,其周围见多发斑片状高密度影,增强扫描动脉期肿瘤边缘无碘油沉积区见不均匀强化影,平衡期强化程度减低,病灶中心见无强化低密度区;另肝实质内见多发小圆形低密度,较大者直径约7mm,增强无强化。肝中及肝左静脉显示欠清,肝内外胆管无明显扩张。胆囊不大,壁无增厚。脾脏体积不大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短径约10mm,轻度强化。腹腔内未见积液。所示左肾盏见斑点高密度影。",
  "conclusion": "肝癌综合治疗后,与2025-3-18片比较:\n肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及实验室资料;\n肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。",
  "physician": "钟芳琴",
  "reviewer": "邓军"
}
2026-08-10 15:50:17,041 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=953927, prompt_len=1256
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期),3.慢性乙型病毒性", "肝炎", "检查项目:上腹部CT平扫+增强扫描", "检查所见:", "肝内见团块状低密度影,其周围见多发斑片状高密度影,增强扫描动脉期肿瘤边缘无碘", "油沉积区见不均匀强化影,平衡期强化程度减低,病灶中心见无强化低密度区;另肝实质内", "见多发小圆形低密度,较大者直径约7mm,增强无强化。肝中及肝左静脉显示欠清,肝内外", "胆管无明显扩张。胆囊不大,壁无增厚。脾脏体积不大,实质密度强化均匀;胰腺大小、形", "态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短", "径约10mm,轻度强化。腹腔内未见积液。所示左肾盏见斑点高密度影。", "印象:", "肝癌综合治疗后,与2025-3-18片比较:", "肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及", "实验室资料;", "肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。", "报告医师:钟芳琴", "审核医师:邓军", "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-6-3 16:42:51", "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)", "东湖影像科咨询电话:0791 86212009(部门otn)"]

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
2026-08-10 15:50:25,179 INFO     29 [qwen-vl-text] coord API raw response (len=1445):
[
	{"text": "临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期),3.慢性乙型病毒性", "bbox": [40, 76, 952, 97]},
	{"text": "肝炎", "bbox": [145, 95, 193, 111]},
	{"text": "检查项目:上腹部CT平扫+增强扫描", "bbox": [40, 129, 410, 147]},
	{"text": "检查所见:", "bbox": [40, 171, 147, 189]},
	{"text": "肝内见团块状低密度影,其周围见多发斑片状高密度影,增强扫描动脉期肿瘤边缘无碘", "bbox": [40, 204, 950, 223]},
	{"text": "油沉积区见不均匀强化影,平衡期强化程度减低,病灶中心见无强化低密度区;另肝实质内", "bbox": [40, 226, 958, 245]},
	{"text": "见多发小圆形低密度,较大者直径约7mm,增强无强化。肝中及肝左静脉显示欠清,肝内外", "bbox": [40, 248, 950, 267]},
	{"text": "胆管无明显扩张。胆囊不大,壁无增厚。脾脏体积不大,实质密度强化均匀;胰腺大小、形", "bbox": [40, 270, 961, 289]},
	{"text": "态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短", "bbox": [40, 292, 961, 311]},
	{"text": "径约10mm,轻度强化。腹腔内未见积液。所示左肾盏见斑点高密度影。", "bbox": [40, 314, 740, 333]},
	{"text": "印象:", "bbox": [40, 451, 97, 469]},
	{"text": "肝癌综合治疗后,与2025-3-18片比较:", "bbox": [40, 477, 425, 495]},
	{"text": "肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及", "bbox": [40, 502, 960, 520]},
	{"text": "实验室资料;", "bbox": [40, 523, 160, 541]},
	{"text": "肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。", "bbox": [40, 548, 924, 567]},
	{"text": "报告医师:钟芳琴", "bbox": [43, 768, 238, 787]},
	{"text": "审核医师:", "bbox": [605, 768, 714, 787]},
	{"text": "重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-6-3 16:42:51", "bbox": [144, 811, 902, 829]},
	{"text": "医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)", "bbox": [145, 834, 880, 849]},
	{"text": "东湖影像科咨询电话:0791 86212009(部门otn)", "bbox": [145, 849, 521, 862]}
]
2026-08-10 15:50:25,179 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=8.1s
2026-08-10 15:50:25,179 INFO     29 [qwen-vl-text] coord item[0]: text=临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期),3.慢性乙型病毒性, bbox=[40, 76, 952, 97]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[1]: text=肝炎, bbox=[145, 95, 193, 111]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[2]: text=检查项目:上腹部CT平扫+增强扫描, bbox=[40, 129, 410, 147]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[3]: text=检查所见:, bbox=[40, 171, 147, 189]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[4]: text=肝内见团块状低密度影,其周围见多发斑片状高密度影,增强扫描动脉期肿瘤边缘无碘, bbox=[40, 204, 950, 223]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[5]: text=油沉积区见不均匀强化影,平衡期强化程度减低,病灶中心见无强化低密度区;另肝实质内, bbox=[40, 226, 958, 245]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[6]: text=见多发小圆形低密度,较大者直径约7mm,增强无强化。肝中及肝左静脉显示欠清,肝内外, bbox=[40, 248, 950, 267]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[7]: text=胆管无明显扩张。胆囊不大,壁无增厚。脾脏体积不大,实质密度强化均匀;胰腺大小、形, bbox=[40, 270, 961, 289]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[8]: text=态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短, bbox=[40, 292, 961, 311]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[9]: text=径约10mm,轻度强化。腹腔内未见积液。所示左肾盏见斑点高密度影。, bbox=[40, 314, 740, 333]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[10]: text=印象:, bbox=[40, 451, 97, 469]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[11]: text=肝癌综合治疗后,与2025-3-18片比较:, bbox=[40, 477, 425, 495]
2026-08-10 15:50:25,180 INFO     29 [qwen-vl-text] coord item[12]: text=肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及, bbox=[40, 502, 960, 520]
2026-08-10 15:50:25,181 INFO     29 [qwen-vl-text] coord item[13]: text=实验室资料;, bbox=[40, 523, 160, 541]
2026-08-10 15:50:25,181 INFO     29 [qwen-vl-text] coord item[14]: text=肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。, bbox=[40, 548, 924, 567]
2026-08-10 15:50:25,181 INFO     29 [qwen-vl-text] coord item[15]: text=报告医师:钟芳琴, bbox=[43, 768, 238, 787]
2026-08-10 15:50:25,181 INFO     29 [qwen-vl-text] coord item[16]: text=审核医师:, bbox=[605, 768, 714, 787]
2026-08-10 15:50:25,181 INFO     29 [qwen-vl-text] coord item[17]: text=重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-6-3 16:42:51, bbox=[144, 811, 902, 829]
2026-08-10 15:50:25,182 INFO     29 [qwen-vl-text] coord item[18]: text=医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱), bbox=[145, 834, 880, 849]
2026-08-10 15:50:25,182 INFO     29 [qwen-vl-text] coord item[19]: text=东湖影像科咨询电话:0791 86212009(部门otn), bbox=[145, 849, 521, 862]
2026-08-10 15:50:25,182 INFO     29 [qwen-vl-text] page=12 — 20/20 coords, api_time=8.1s
2026-08-10 15:50:25,183 INFO     29 [qwen-vl-text] new_positions (20):
[[12, 23.799999999999997, 566.4399999999999, 63.992, 81.67399999999999], [12, 86.27499999999999, 114.835, 79.99, 93.462], [12, 23.799999999999997, 243.95, 108.618, 123.774], [12, 23.799999999999997, 87.46499999999999, 143.982, 159.138], [12, 23.799999999999997, 565.25, 171.768, 187.766], [12, 23.799999999999997, 570.01, 190.292, 206.29], [12, 23.799999999999997, 565.25, 208.816, 224.814], [12, 23.799999999999997, 571.795, 227.34, 243.338], [12, 23.799999999999997, 571.795, 245.864, 261.86199999999997], [12, 23.799999999999997, 440.29999999999995, 264.388, 280.38599999999997], [12, 23.799999999999997, 57.714999999999996, 379.74199999999996, 394.89799999999997], [12, 23.799999999999997, 252.875, 401.63399999999996, 416.78999999999996], [12, 23.799999999999997, 571.1999999999999, 422.68399999999997, 437.84], [12, 23.799999999999997, 95.19999999999999, 440.366, 455.522], [12, 23.799999999999997, 549.78, 461.416, 477.414], [12, 25.584999999999997, 141.60999999999999, 646.656, 662.654], [12, 359.97499999999997, 424.83, 646.656, 662.654], [12, 85.67999999999999, 536.6899999999999, 682.862, 698.018], [12, 86.27499999999999, 523.6, 702.228, 714.858], [12, 86.27499999999999, 309.995, 714.858, 725.804]]
2026-08-10 15:50:25,183 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=1, time=11.9s
2026-08-10 15:50:25,198 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 15:50:25,198 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:ExaminationReport | outputs={"chunks": "4 items, types={'ExaminationReport': 4}", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:50:25,199 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 15:50:25,210 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:50:25,210 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:50:26,062 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:50:26,073 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 15:50:26,073 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "383 items", "markdown": "", "text": "", "name": "Wlge-肝癌-男-57岁.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Discharge": "4 items, types={'DischargeRecord': 4}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Clinical\": 3, \"chunks_Discharge\": 4, \"chunks_Examination\": 4, \"chunks_LabExam\": 3}"}
2026-08-10 15:50:26,073 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 15:50:26,075 INFO     29 [ChunkMerger] Merged 15 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 4, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 4, 'Extractor:Progress': 1} (filtered 4 noise chunks)
2026-08-10 15:50:26,089 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 15:50:26,089 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "15 items, types={'LabReport': 3, 'OutpatientRecord': 3, 'DischargeRecord': 4, 'AdmissionRecord': 1, 'ExaminationReport': 4}", "name": "Wlge-肝癌-男-57岁.pdf"}
2026-08-10 15:50:26,090 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 15:50:26,270 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786376615718, 'update_date': datetime.datetime(2026, 8, 10, 15, 43, 35), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1180882, 'status': '1'}
2026-08-10 15:50:26,490 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞计数  WBC  6.47  10^9/L  3.5-9.5  False    红细胞计数  RBC  6.90  10^12/L  4.3-5.8  True    血红蛋白  HGB  133  g/L  130-175  False    血小板计数  PLT  142  10^9/L  125-350  False    中性粒细胞百分比  NEUT%  70.3  %  40-75  False    淋巴细胞百分比  LYM%  19.5  %  20-50  True    单核细胞百分比  MONO%  9.4  %  3-10  False    嗜酸性粒细胞百分比  EO%  0.50  %  0.4-8  False    嗜碱性粒细胞百分比  BASO%  0.3  %  0-1  False    中性粒细胞绝对值  NEUT#  4.55  10^9/L  2-7  False    淋巴细胞绝对值  LYM#  1.26  10^9/L  1.5-4  True    单核细胞绝对值  MONO#  0.61  10^9/L  0-0.5  True    嗜酸性粒细胞绝对值  EO#  0.03  10^9/L  0.1-0.4  True    嗜碱性粒细胞绝对值  BASO#  0.02  10^9/L  0-0.07  False    红细胞压积  HCT  44.80  %  40-50  False    平均红细胞体积  MCV  64.9  fL  82-100  True    平均红细胞Hb含量  MCH  19.3  pg  27-34  True    平均红细胞Hb浓度  MCHC  297  g/L  316-354  True    红细胞分布宽度(CV)  RDW-CV  18.4  %  10.9-15.4  True    红细胞分布宽度(SD)  RDW-SD  37.9  fl  39-46  True    血小板压积  PCT  ----  %  0.1-0.28  False    血小板分布宽度  PDW  ----  fl  11-26.5  False    平均血小板体积  MPV  ----  fL  7.6-13.2  False    十血小板比值  P-LCR  ----  %  13-43  False   
---
   总蛋白  TP  77.80  g/L  65-8  False    白蛋白  ALB  42.70  g/L  40-5  False    球蛋白  GLB  35.10  g/L  20-4  False    白球比例  A/G  1.22  None  1.2-  False    总胆红素  TBIL  31.70  µmol/L  0-20  True    直接胆红素  DBIL  13.30  µmol/L  0-6.  True    间接胆红素  IBIL  18.40  µmol/L  0-18  True    天门冬氨酸氨基转移酶  AST  89.00  U/L  15-  True    丙氨酸氨基转移酶  ALT  54.30  U/L  9-  True    碱性磷酸酶  ALP  224.00  U/L  45-  True    γ-谷氨酰基转移酶  γ-GT  495.90  U/L  10  True    尿素  UREA  4.25  mmol/L  3.1  False    肌酐  Cre  69.80  µmol/L  57  False    估算肾小球滤过率  eGFR  107.16  None  仅适用  False    尿酸  URIC  315.40  µmol/L  208  False   
---
   甲胎蛋白测定  AFP  >240000.00  ng/ml  0-7  True    甲胎蛋白异质体L3测定  AFP-L3  53777.00  ng/ml  0-1  True    异常凝血酶原测定  DCP  >20000.00  ng/ml  0-40  True    甲胎蛋白异质体比率(L3%)  AFP-L3%  >10%  None  0-10%  True    肝癌辅助分析评分  C-GALAD  99.91  None  54以下偏低风险;54-66为肝部疾病中风险;>66判定偏高风险  False   
---
工作单位或地址:湾里区
就诊科室:红角洲肝胆外科门诊
就诊时间:2025年12月07日 08:46
药物过敏史:无
主诉:肝Ca综合治疗后半年返院复查。
病史:肝Ca综合治疗后半年复查。未诉特殊不适。
既往史和其他病史:既往半年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。
体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。
助检查:暂缺。
诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿
靶向治疗;4.恶性肿瘤免疫治疗
理:1.胸部CT平扫
上腹部薄层CT平扫+增强扫描
肝癌三项:肝功能八项+白蛋白;血常规(五分类法);肾功能3项
碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶
用法:每次30g即时造影用1天
CT静脉注药(留置针置管)每次1项
转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院
医生签名:
---
就诊科室:红角洲肝胆外科门诊
就诊时间:2026年03月05日 09:51
药物过敏史:无
主诉:肝Ca综合治疗后1年返院评估介入治疗。
现病史:肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。
既往史和其他病史:既往1年前诊断肝CA,行介入+抗肿瘤靶向+免疫治疗。
查体:血压:/mmHg,脉搏:次/分。无特殊阳性体征。
辅助检查:暂缺。
诊断:1.肝细胞癌(BCLC B期,CNLC IIb期);2.慢性乙型病毒性肝炎;3.恶性肿
瘤靶向治疗;4.恶性肿瘤免疫治疗;5.肝癌介入治疗
处理:1.胸部CT平扫
2.上腹部薄层CT平扫+增强扫描
3.肝癌三项;肝功能八项+白蛋白:血常规(五分类法);肾功能3项
4.碘海醇注射液(基)[100ml:30g](广东阿哌集采)X1瓶
用法:每次30g即时造影用1天
5.CT静脉注药(留置针置管)每次1项
下转情况:◎不下转○转县级院○转社区卫生服务机构/乡镇卫生院
医生签名:
---
职业：
出生日期：1968年01月06日
工作单位或地址：湾里区
就诊科室：红角洲肝胆外科门诊
就诊时间：2026年03月07日 14:40
药物过敏史：无
主诉：肝Ca综合治疗后1年返院评估介入治疗。
现病史：肝Ca综合治疗后1年返院评估介入治疗。未诉特殊不适。
既往史和其他病史：既往1年前诊断肝CA，行介入+抗肿瘤靶向+免疫治疗。
查体：血压：/mmHg，脉搏：次/分。无特殊阳性体征。
辅助检查：2026-03-06,上腹部薄层CT平扫+增强扫描检查意见：“肝癌”综合
治疗后，较2025-12-07日腹部CT：肝右叶肿块较前大小相仿，无明显血供；肿
块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大，下腔静脉癌栓形
成；余较前相仿。
诊断：1.肝细胞癌(BCLC B期，CNLC IIb期)；2.恶性肿瘤靶向治疗；3.恶性肿瘤
免疫治疗；4.肝癌介入治疗；5.慢性肝炎
处理：
下转情况：◎不下转 ○转县级院 ○转社区卫生服务机构/乡镇卫生院
医生签名：陈天翔
---
入院日期：2025年08月02日
出院日期：2025年08月06日
住院天数：4
入院情况(简要病史\体格检查及主要辅助检查)：患者男性57岁，因肝癌于我院行综合治疗，现为返
院复诊，无头晕头痛，胸闷气促，恶心呕吐等不适，于我院门诊就诊，门诊拟"肝癌介入治疗"收入我
科。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。查体：神志清楚，
皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲张，腹肌软，腹部无压
痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓音，肝上界位于右锁骨
中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：暂无。
入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.肝细胞癌4.恶性肿瘤靶向治疗5.
恶性肿瘤免疫治疗6.慢性乙型病毒性肝炎。
诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检
验检查：主要化验：2025-08-02血常规(五分类法)：超敏C反应蛋白测定(全程) 15.25mg/L,红细胞
计数 7.21*10^12/L,单核细胞百分比 11.3%，2025-08-02凝血四项：纤维蛋白原浓度 4.16g/l,
2025-08-02肝癌三项：甲胎蛋白测定 5931.00ng/ml,甲胎蛋白异质体L3测定 804.30ng/ml,异常凝血酶
原测定 24560.00ng/ml,甲胎蛋白异质体比率(L3%) 13.56%，2025-08-02肝功能八项+白蛋白：白蛋
白 38.70g/L,白球比例 0.97,碱性磷酸酶 171.40U/L,γ-谷氨酰基转移酶 243.20U/L。特殊检查：
2025-08-04,胸部CT平扫检查意见:对比2025-6-16胸部CT：右下肺实性结节影较前稍增大（平扫薄层
194），拟转移与机化性肺炎鉴别，请结合临床；两下肺胸膜下渗出及条索灶稍增多；余大致同前。
2025-08-04,上腹部薄层CT平扫+增强扫描检查意见:肝癌综合治疗后，对比2025-6-16日CT：1.肝右叶
肿块较前略缩小，病灶内实性异常强化部分较前增多，请结合临床。2.肝内多发小囊肿，部分肝内胆
管稍扩张。3.肝门部及腹膜后数个稍大淋巴结，较前相仿。有手术指征，排除手术禁忌症后，于2025
年08月04日行肝动脉栓塞术 肝动脉造影术 腹腔动脉灌注化疗药物，术后给予患者止吐、护胃、止
痛、补液等对症治疗，今患者术后恢复可，予以免疫治疗后，患者无特殊不适，给予出院。
诊疗经过(包括手术日期和手术名称,植入类医用耗材名称、型号及数量):入院后予以完善相关检
验检查:主要化验:2025-06-02肝功能五项:γ-谷氨酰基转移酶67.30U/L。2025-06-02血清总蛋白+
白蛋白测定:白蛋白39.40g/L。2025-06-02超敏C反应蛋白测定+金标法加收(全程,快):超敏C反应
蛋白测定(全程)30.63mg/L。2025-06-02血常规(五分类法):红细胞计数7.01*10^12/L,血小板计数
110*10^9/L。2025-06-02肝癌三项:甲胎蛋白测定4679.00ng/ml,甲胎蛋白异质体L3测定370.00ng/ml,
异常凝血酶原测定>20000.00ng/ml。2025-06-04超敏C反应蛋白测定+金标法加收(全程,快):超敏C
反应蛋白测定(全程)25.06mg/L。2025-06-04血常规(五分类法):红细胞计数6.19*10^12/L,血红蛋
白119g/L,血小板计数113*10^9/L,中性粒细胞百分比89.8%。2025-06-04凝血四项:凝血酶原时间
13.3sec。2025-06-04肝功能八项+白蛋白:天门冬氨酸氨基转移酶60.10U/L。余检验均未见明显异
常。特殊检查:2025-06-03,上腹部CT平扫+增强扫描检查意见:肝癌综合治疗后,与2025-3-18片比
较:肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及实验
室资料;肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。术
前诊断:原发性肝癌(BCLC B期,CNLC IIb期),有手术指征,排除手术禁忌症后,于2025-06-03行肝
动脉栓塞术+肝局部灌注术,术后给予患者护胃、止吐、止痛、补液等对症治疗,今患者术后恢复可,
给予出院。
出院诊断:1.肝癌介入治疗2.原发性肝癌(BCLC B期,CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤
靶向治疗5.恶性肿瘤免疫治疗6.肾结石。
出院情况:患者一般情况良好,生命体征平稳,无畏寒发热,无恶心呕吐,无头痛头晕,无胸闷心
悸。查体:全身皮肤、巩膜未见黄染,腹平软,无压痛,未及反跳痛和肌紧张,肠鸣音正常,股动脉
穿刺点无渗血,双下肢动脉搏动良好。
出院医嘱:
I
---
肝区介入术后复查所见。
入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤
靶向治疗5.恶性肿瘤免疫治疗6.肾结石。
诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检
验检查：主要化验：2025-04-25凝血四项：凝血酶原时间13.6sec,D-二聚体0.81mg/l FEU,
2025-04-25血常规(五分类法)：红细胞计数6.55*10^12/L，2025-04-25肝功能八项+白蛋白：球蛋白
44.40g/L,直接胆红素7.70μmol/L,天门冬氨酸氨基转移酶88.90U/L,丙氨酸氨基转移酶79.70U/L,碱性
磷酸酶182.30U/L,γ-谷氨酰基转移酶114.40U/L,钠136.90mmol/L，2025-04-25肝癌三项：甲胎蛋白测
定26695.00ng/ml,甲胎蛋白异质体L3测定2670.00ng/ml,异常凝血酶原测定95400.00ng/ml。余检验均
未见明显异常。特殊检查：2025-04-25,常规心电图检查十二通道(床边)检查意见:1、窦性心律2、大
致正常心电图。2025-04-25,胸部正位DR检查意见:肝区介入术后复查所见。术前诊断：1.肝癌介入治
疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤靶向治疗5.恶性肿瘤免疫
治疗6.肾结石。有手术指征，排除手术禁忌症后，于2025年04月27日局部麻醉下行肝动脉栓塞术,肝
局部灌注术,肝动脉造影术,肝动脉置管术，术后给予患者止痛、补液等对症治疗，今患者术后恢复
可，给予出院。
出院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC B期，CNLC IIb期)3.慢性乙型病毒性肝炎4.恶性肿瘤
靶向治疗5.恶性肿瘤免疫治疗6.肾结石。
出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心
悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉
穿刺点无渗血，双下肢动脉搏动良好。
出院医嘱：
---
第1页
入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。
诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检
验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,
2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21,2025-03-18肝功能八项+白蛋白：白
蛋白39.40g/L,直接胆红素8.70umol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-
谷氨酰基转移酶402.20U/L,2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L,
2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L,2025-03-18乙肝五项(定量)：乙
肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml,
2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血
酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+
增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检
查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺散在炎性灶。术前
诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肾结石3.肺部感染4.慢性乙型病毒性肝炎，经讨论评
估为不可切除，决定行转化治疗，排除手术禁忌症后，于2025年03月20日行肝动脉栓塞术,肝动脉造影
术,动脉注射化疗药物,肝动脉置管术，术后给予患者抗感染、护肝等对症治疗，今患者术后恢复可，
予以靶免治疗(仑伐替尼，3粒，qd；信迪利单抗200mg，q3w)后给予出院。
出院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.肝癌介入治疗3.恶性肿瘤靶向治疗4.恶性肿瘤免
疫治疗5.肾结石6.肺部感染7.慢性乙型病毒性肝炎。
出院情况：患者一般情况良好，生命体征平稳，无畏寒发热，无恶心呕吐，无头痛头晕，无胸闷心
悸。查体：全身皮肤、巩膜未见黄染，腹平软，无压痛，未及反跳痛和肌紧张，肠鸣音正常，股动脉
穿刺点无渗血，双下肢动脉搏动良好。
---
第1页
入院日期：2025年03月18日
出院日期：2025年03月24日
住院天数：6天
入院情况(简要病史\体格检查及主要辅助检查)：患者男，57岁，因“反复右上腹部疼痛半年”入
院。患者自诉半年余前开始无明显诱因下出现右上腹部疼痛，无恶心呕吐，无畏寒发热，自行缓解，1
天前再发腹痛，至我院急诊就诊，行CT检查提示肝占位性病变，请我科医师会诊后，拟“肝占位性病
变”收入我科住院。患者自起病以来，精神、睡眠、饮食尚可，大小便正常，体重未见明显增减。
专科情况：神志清楚，皮肤巩膜未见明显黄染，腹平坦，未见胃肠型和胃肠蠕动波，未见腹壁静脉曲
张，腹肌软，腹部无压痛及反跳痛，未触及肿物，肝脾肋下未及，胆囊未触及，Muphy征阴性，叩诊鼓
音，肝上界位于右锁骨中线第五肋间，肝区未及叩痛，无移动性浊音，肠鸣音正常。辅助检查：
2025-03-18上腹部CT平扫+增强扫描见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，
请结合临床、AFP检查。肝门部及腹膜后数个小、稍大淋巴结。肝脏囊性灶；左肾小结石。附见：两肺
散在炎性灶。
入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结石3.肺部感染。
诊疗经过(包括手术日期和手术名称，植入类医用耗材名称、型号及数量)：入院后予以完善相关检
验检查：主要化验：2025-03-18血常规(五分类法)：血红蛋白111g/L,中性粒细胞百分比77.5%,
2025-03-18凝血四项：凝血酶原时间13.7sec,国际标准比率1.21，2025-03-18肝功能八项+白蛋白：白
蛋白39.40g/L,直接胆红素8.70μmol/L,天门冬氨酸氨基转移酶101.40U/L,碱性磷酸酶195.90U/L,γ-
谷氨酰基转移酶402.20U/L，2025-03-18血脂五项(体检)：高密度脂蛋白胆固醇1.08mmol/L，
2025-03-18C反应蛋白测定(慢，免疫)：血清C反应蛋白9.810mg/L，2025-03-18乙肝五项(定量)：乙
肝表面抗原(定量检测)>250.000IU/ml,乙肝病毒核心抗体(定量检测)115.518PEIU/ml，
2025-03-18肝癌三项：甲胎蛋白测定331427.00ng/ml,甲胎蛋白异质体L3测定40487.00ng/ml,异常凝血
酶原测定14420.00ng/ml,甲胎蛋白异质体比率(L3%)12.22%。特殊检查：2025-03-18,上腹部CT平扫+
增强扫描检查意见：肝内巨大占位，考虑肿瘤性病变，肝Ca可能伴周围子灶形成，请结合临床、AFP检
临床诊断:1.肝细胞癌(BCLC B期,CNLC IIb期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶
---
族:汉族
婚姻:已婚
出生地:江西省南昌市湾里区
业:其他
现住址:江西省南昌市湾里区
史陈述者:本人及家属
与患者关系:其他
可靠程度:基本可靠
院时间:2025年09月16日 14:33
记录时间:2025年09月16日 15:59
诉:肝癌综合治疗5月余。
病史:患者5月余前开始因肝癌于我院行综合治疗(介入+靶向+免疫:TACE+仑伐替尼+信迪利单
), 后于2025年04月27日、2025年06月03日、2025年08月04日行肝动脉栓塞术。现患者为求下一周
治疗来我院就诊。门诊拟"肝癌介入治疗"收入我科。患者自起病来, 饮食睡眠一般, 大小便如常,
睡无明显变化。
注史:患者既往身体较差。否认高血压病史。否认糖尿病史。否认冠心病史。否认肾病史。有肝炎
史慢性乙型病毒性肝炎。否认结核病史。有手术史2025年03月20日、4月27日、06月03日、08月04日
行肝动脉栓塞术, 肝局部灌注术, 肝动脉造影术, 动脉注射化疗药物, 肝动脉置管术手术。否认外伤史
否认输血史。否认药物、食物过敏史。
人史:生于原籍, 久居本地, 否认疫区、疫水接触史。否认毒物、放射性物质接触史。否认烟酒嗜好
育史:已婚,[结婚年龄]适龄结婚, 配偶体健, 夫妻关系和睦。育有[育子数量]男、[育女数量]
均体健。
史:否认家族及遗传病史。
体格检查
体温:36.8℃ 脉搏:82次/分 呼吸:20次/分 血压:115/87mmHg
正常, 营养中等, 表情自然, 无贫血貌, 自主体位, 步入病房, 步态正常, 神志清楚, 查体合作
身皮肤黏膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣。全身浅表淋巴结未触及
。头颅无畸形, 双眼睑无水肿, 眼球无突出及震颤, 结膜无苍白、无充血、无出血、无水肿, 巩
---
向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗
检查项目:上腹部薄层CT平扫+增强扫描
检查所见:
肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显
强化,肿块边缘及邻近肝实质内多发稍低密度结节,边界欠清,部分融合,呈“快进快出”
强化方式,部分与邻近肝内血管分界欠清,门静脉右后支纤细;肝右静脉显示不清,下腔静
脉内见充盈缺损,肝中静脉受压推挤改变、局部显示欠清。另肝实质内见多发小圆形低密
度,较大者直径约7mm,增强无强化。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积
稍大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及
腹膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见
斑点状致密影。
印象:
“肝癌”综合治疗后,较2025-12-07日腹部CT:肝右叶肿块较前大小相仿,无明显血供;
肿块边缘及邻近肝实质内多个子灶或转移灶明显增多、增大,下腔静脉癌栓形成;余较前相
仿。
报告医师:梁利民
审核医师:
重要提示:本报告仅供临床医师诊断时参考 审核时间:2026-3-6 13:21:46
医院咨询电话:0791-86120120(东湖):0791-87311120(红角洲):0791-85229772(青云谱)
东湖影像科咨询电话:0791-86213393(登记室):0791-86301219(阅片室)
---
红角洲影像科咨询电话:0791-86257676(
临床诊断:1.肝细胞癌(BCLC B期,CNLC 11b期),2.慢性乙型病毒性肝炎,3.恶性肿瘤靶
向治疗,4.恶性肿瘤免疫治疗
检查项目:上腹部薄层CT平扫+增强扫描
检查所见:
肝内见巨块状混杂高低密度影,最大截面大小约98mm×95mm,肿块碘油沉积可,无明显
强化,肿块边缘及邻近肝实质内多个稍低密度结节,呈“快进快出”强化方式,大者大小约
54mm×31mm,部分与邻近肝内血管分界欠清。另肝实质内见多发小圆形低密度,较大者直径
约7mm,增强无强化。门静脉右后支纤细,似见条状充盈缺损;肝右静脉显示不清,肝中静
脉受压推挤改变、局部显示欠清。肝右叶胆管轻度扩张。胆囊不大,壁不厚。脾脏体积稍
大,实质密度强化均匀;胰腺大小、形态和密度未见异常,实质密度强化均匀。肝门部及腹
膜后见数个小、稍大淋巴结,较大者短径约11mm,均匀强化。腹腔内未见积液。左肾盏见斑
点状致密影。
印象:
肝癌综合治疗后,对比2025-9-10日CT:肝右叶肿块较前大小相仿,无明显血供;新增肿块
边缘及邻近肝实质内多个子灶或转移灶,有活性,个别病灶与肝中静脉分界不清;胆囊壁水
肿基本缓解;余较前相仿。
报告医师:冯梓妍
审核医师:
熊小丽
重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-12-7 16:33:54
医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)
东南影像科咨询电话:0791-86213393(登记室);0791-86301219(阅片室)
红角洲影像科咨询电话:0791-86357670(骨记室);0701:87357668(原片室)
---
第1页 共1页
临床诊断:1.肝癌介入治疗,2.原发性肝癌
检查项目:胸部CT平扫
检查所见:
两肺纹理增粗增多,右肺上叶见一类圆形小囊泡。两下肺见散在条索及条带状实变影,
边界清;右下肺前基底段见不规则实性密度条片影(SE202IM184),大小约21mm×13mm;
两肺散在少许直径约2-3mm微小结节影,界清。气管、主要支气管通畅,两肺门及纵隔未见
明确肿大淋巴结。心脏不大,双侧胸膜无明显增厚,胸腔内未见积液。
印象:
对比2025-8-4胸部CT:右下肺实性结节影较前稍减小,请结合临床;两下肺胸膜下渗出
及条索灶较前减少吸收;余大致同前。
报告医师:肖轩
审核医师:钟玉凤
重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-9-11 8:39:32
医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲)
---
临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期),3.慢性乙型病毒性
肝炎
检查项目:上腹部CT平扫+增强扫描
检查所见:
肝内见团块状低密度影,其周围见多发斑片状高密度影,增强扫描动脉期肿瘤边缘无碘
油沉积区见不均匀强化影,平衡期强化程度减低,病灶中心见无强化低密度区;另肝实质内
见多发小圆形低密度,较大者直径约7mm,增强无强化。肝中及肝左静脉显示欠清,肝内外
胆管无明显扩张。胆囊不大,壁无增厚。脾脏体积不大,实质密度强化均匀;胰腺大小、形
态和密度未见异常,实质密度强化均匀。肝门部及腹膜后见数个小、稍大淋巴结,较大者短
径约10mm,轻度强化。腹腔内未见积液。所示左肾盏见斑点高密度影。
印象:
肝癌综合治疗后,与2025-3-18片比较:
肝内巨块病灶明显缩小,边缘强化影提示肿瘤存活;肝内多发子灶较前缩小;请结合专科及
实验室资料;
肝门部及腹膜后数个稍大淋巴结,部分较前缩小;肝囊肿;左肾小结石,较前大致相仿。
报告医师:钟芳琴
审核医师:邓军
重要提示:本报告仅供临床医师诊断时参考 审核时间:2025-6-3 16:42:51
医院咨询电话:0791-86120120(东湖);0791-87311120(红角洲);0791-85229772(青云谱)
东湖影像科咨询电话:0791 86212009(部门otn)
2026-08-10 15:50:27,346 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 15:50:27,346 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "15 items, types={'LabReport': 3, 'OutpatientRecord': 3, 'DischargeRecord': 4, 'AdmissionRecord': 1, 'ExaminationReport': 4}", "name": "Wlge-肝癌-男-57岁.pdf", "embedding_token_consumption": 8897}
2026-08-10 15:50:27,347 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 15:50:27,661 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 15:50:27,661 INFO     29 [Trace] task=3d95d73c | doc=Wlge-肝癌-男-57岁.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":15,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int len=24 row[0]=(14, 351, 392, 66, 74) row[-1]=(14, 350, 398, 492, 500)
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int len=15 row[0]=(15, 368, 397, 129, 139) row[-1]=(15, 373, 393, 419, 429)
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int len=5 row[0]=(16, 304, 359, 151, 162) row[-1]=(16, 296, 367, 255, 266)
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,667 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,668 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,668 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,668 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,668 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,668 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:50:27,675 INFO     29 set_progress(3d95d73c94d211f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 15:50:27 [DOC Engine]:
Start to index...
2026-08-10 15:50:27,703 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.022s]
2026-08-10 15:50:27,708 INFO     29 set_progress(3d95d73c94d211f1bd9827cf206dfa2d), progress: 0.8066666666666668, progress_msg: 
2026-08-10 15:50:27,731 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 15:50:27,755 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-10 15:50:27,779 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 15:50:27,787 INFO     29 set_progress(3d95d73c94d211f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 15:50:27 Indexing done (0.11s). Task done (389.75s)
2026-08-10 15:50:27,793 INFO     29 [Done], chunks(15), token(8897), elapsed:389.75
2026-08-10 15:50:28,003 INFO     29 handle_task done for task {"id": "3d95d73c94d211f1bd9827cf206dfa2d", "doc_id": "3d4248b094d211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf", "type": "pdf", "location": "Wlge-\u809d\u764c-\u7537-57\u5c81.pdf_", "size": 7886802, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786376612250, "task_type": "dataflow", "root_trace_id": "c72ae088dfee47d186e2a54eafcfa2b1", "root_traceparent": "00-c72ae088dfee47d186e2a54eafcfa2b1-d002a0e058cf761a-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
