# 基准结果：SYQI肺鳞癌.pdf

## 基本信息

- 文件：`SYQI肺鳞癌.pdf`
- 大小：6541.0 KB
- PDF 总页数：14
- doc_id：`737f81ac94f211f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T03:34:05  完成时间：2026-08-11T03:42:39  耗时：514.2s
- progress_msg：`19:42:35 Indexing done (0.08s). Task done (472.00s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 12ae427a | 1 | 1-1 | 空军军医大学唐都医院 查阅电子胶片 CT检查报告单 ID号：62893718 检 |
| 2 | 76549e72 | 1 | 3-3 | 空军军医大学第二附属医院(唐都医院) 病理图文诊断报告单 病理号: 261044 |
| 3 | ca9c89db | 1 | 4-4 | 中国人民解放军联勤保障部队第九八九医院 出院证 姓名 性别 男 年龄 55岁 费 |
| 4 | 311c7c7d | 1 | 5-5 | 中国人民解放军联勤保障部队第九八九医院 姓名:水月强 病区(科):肿瘤科病区 床 |
| 5 | 1def1326 | 1 | 8-8 | <table><tr><td>白细胞计数(8-HR)</td><td>WBC</ |
| 6 | c6510ee1 | 1 | 9-9 | <table><tr><td>乙肝表面抗原</td><td>HBsAg</td> |
| 7 | fb312758 | 1 | 11-11 | <table><tr><td>游离三碘甲状腺原氨酸(8-HR)</td><td> |
| 8 | 77869164 | 1 | 14-14 | <table><tr><td>血糖(空腹)(8-HR)</td><td>GLU< |
| 9 | f1f94273 | 1 | 6-6 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 10 | 3e48fae1 | 1 | 7-7 | <table><tr><td>乙肝肝炎病毒表面抗原</td><td>HBsAg< |
| 11 | 0315c5f2 | 1 | 10-10 | <table><tr><td>ABO血型鉴定</td><td>ABO</td>< |
| 12 | d64e3918 | 1 | 12-12 | <table><tr><td>肌酸激酶同工酶</td><td>CK-MB</td |
| 13 | 344bc689 | 1 | 6-6 | <table><tr><td>凝血酶原时间</td><td>PT-1</td>< |
| 14 | d4666ac9 | 1 | 13-13 | <table><tr><td>凝血酶原时间(陕HR)</td><td>PT</t |

- chunks 总数：14
- 各 chunk 页数合计（含跨页重复）：14
- 页码并集：`[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：13 / 14；缺失页：`[2]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 13/14 页，缺失 [2]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 2 | 2 | 2 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 11 | 0 | 11 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"ExaminationReport": 2, "LabReport": 11, "DischargeRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 15, "sources": 9, "stats": {"Extractor:LabExam": 11, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 2, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 19:42:34,176 INFO     29 [ChunkMerger] Merged 15 chunks from 9 sources: {'Extractor:LabExam': 11, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Pres`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 19:34:06,963 INFO     29 handle_task begin for task {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 19:34:07,153 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 19:34:07,270 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 19:34:07,285 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:34:07,286 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 19:34:07,286 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 19:34:07,304 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 19:34:07,304 INFO     29 ============================================================
2026-08-10 19:34:07,304 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 19:34:07,304 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 19:34:07,304 INFO     29 ============================================================
2026-08-10 19:34:07,304 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 19:34:07,304 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 19:34:07,315 INFO     29 No torch found.
2026-08-10 19:34:08,658 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=14
2026-08-10 19:34:08,904 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2022226, prompt_len=764
2026-08-10 19:34:10,459 INFO     29 [qwen-vl-parser] classify API response (len=67):
```json
{
    "type": "text",
    "report_date": "2026-03-04"
}
```
2026-08-10 19:34:10,461 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2026-03-04
2026-08-10 19:34:10,474 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2022226, prompt_len=401
2026-08-10 19:34:16,138 INFO     29 [qwen-vl-parser] text API response (len=1022):
["空军军医大学唐都医院", "查阅电子胶片", "CT检查报告单", "ID号：62893718", "检查时间：2026-03-04", "检查号：CT2603030254", "住院", "报告日期：2026-03-04", "影像号：62893718", "姓名", "性别：男", "年龄：55岁", "申请科室：肿瘤科三病区", "床号：", "检查项目：盆腔CT平扫|胸部CT平扫|胸部CT增强|上腹部CT平扫(肝胆胰脾)|下腹部CT平扫", "检查方法：平扫+增强", "影像所见：", "左肺上叶尖后段支气管狭窄，可见不规则团块状软组织密度影，大小约", "4.5×4.0×5.9cm，局部紧贴叶间胸膜，可见“胸膜凹陷征”，平扫CT值约32HU，增", "强扫描呈不均匀强化，两期CT值约33HU、59HU；右肺下叶前基底段可见局限性无肺纹", "理区；余双肺野清晰，肺纹理走行自然，双肺门影不大。气管及纵隔位置居中，纵隔", "可见多发增大淋巴结，较大者短径约0.6cm。心膈影未见异常，双侧胸膜无增厚，未见", "胸腔积液。骨性胸廓骨质结构完整。", "肝随边缘光滑，各叶大小比例正常，肝实质内密度均匀，未见明显异常密度影及", "占位性病变，肝内外胆管未见扩张，肝门部结构清晰，未见占位性病变，胆囊不大，", "壁薄且均匀，腔内未见阳性结石影。胰腺大小、形态及密度未见异常。脾不大，实质", "密度均匀，双肾大小形态良好，实质密度均匀，双侧肾盂未见扩张，右肾可见阳性结", "石影。腹腔内及腹膜后未见明显肿大淋巴结影，未见腹水征象。", "膀胱充盈良好，壁厚薄均匀，未见占位性病变。前列腺大小、形态及密度未见异", "常。双侧精囊腺大小、形态及密度未见异常。直肠形态正常，未见占位性病变。盆腔", "淋巴结无肿大，盆腔内未见积液征象。", "诊断意见：", "1、左肺上叶尖后段占位性病变，多考虑周围型肺癌；纵隔多发增大淋巴结；", "2、右肾结石；肝、胆、胰、脾及左肾CT扫描未见明显异常。", "3、膀胱、前列腺、双侧精囊腺及直肠CT扫描未见明确病变。", "本意见仅供临床医生参考，盖章或签字后生效！", "报告医师：杨露", "审核医师：", "该信息经过北京CA数字签名认证", "签名验证的信息摘要值为：3BFB10562BBC74DF5F886274A0100FAG。检查号：CT2603030254。"]
2026-08-10 19:34:16,139 INFO     29 [qwen-vl-parser] page=1 text: 40 lines (bbox 0-39)
2026-08-10 19:34:16,140 INFO     29 [qwen-vl-parser] page=1 text: 40 sections
2026-08-10 19:34:16,336 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1649509, prompt_len=764
2026-08-10 19:34:17,904 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-04"
}
```
2026-08-10 19:34:17,905 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2026-03-04
2026-08-10 19:34:17,913 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1649509, prompt_len=756
2026-08-10 19:34:27,149 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:34:27.146+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:34:28,711 INFO     29 [qwen-vl-parser] table API response (len=1701):
\begin{tabular}{lllllllll}
\hline
No. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\
\hline
1 & 血糖(空腹)(8-HR) & & GLU & 5.56 & 3.9-6.1 & mmol/L & 己糖激酶法 \\
2 & 钾(8-HR) & & K & 4.36 & 3.5-5.3 & mmol/L & 间接离子选择电极法 \\
3 & 钠(8-HR) & & Na & 137.8 & 137-147 & mmol/L & 间接离子选择电极法 \\
4 & 氯(8-HR) & & Cl & 100.9 & 99-110 & mmol/L & 间接离子选择电极法 \\
5 & 总蛋白(8-HR) & & TP & 73.0 & 65-85 & g/L & 双缩脲比色法 \\
6 & 白蛋白(8-HR) & & ALB & 42.4 & 40-55 & g/L & 溴甲酚绿法 \\
7 & 球蛋白 & & GLO & 30.6 & 20-40 & g/L & 计算法 \\
8 & 白球比 & & A/G & 1.4 & 1.2-2.4 & & 计算法 \\
9 & 总胆红素(8-HR) & & T-BIL & 12.1 & 0-26 & $\mu$mol/L & 钒酸盐氧化法 \\
10 & 直接胆红素(8-HR) & & D-BIL & 3.5 & 0-6.8 & $\mu$mol/L & 钒酸盐氧化法 \\
11 & 间接胆红素 & & I-BIL & 8.6 & 0-14 & $\mu$mol/L & 计算法 \\
12 & 丙氨酸氨基转移酶(8-HR) & & ALT & 26 & 9-50 & U/L & 紫外-乳酸脱氢酶法 \\
13 & 天门冬氨酸氨基转移酶(8-HR) & & AST & 21 & 15-40 & U/L & 紫外-苹果酸脱氢酶法 \\
14 & AST/ALT & & & 0.81 & & & 计算法 \\
15 & 碱性磷酸酶(8-HR) & & ALP & 106 & 45-125 & U/L & AMP缓冲液法 \\
16 & 总胆汁酸(陕HR) & & TBA & 12.6 & 0-10 & $\mu$mol/L & 循环酶法 \\
17 & 胆碱酯酶(陕HR) & & CHE & 6970 & 5000-12000 & U/L & 丁酰硫代胆碱/铁氰化钾 \\
18 & $\gamma$-谷氨酰转移酶(8-HR) & & GGT & 23 & 10-60 & U/L & 速率法 \\
19 & eGFR(CKD-EPI) & & eGFR & 93.12 & >90 & ml/min/1.73m2 & 计算法 \\
20 & 尿酸(8-HR) & & UA & 263.0 & 208-428 & $\mu$mol/L & 氧化酶法 \\
21 & 尿素(8-HR) & & UREA & 6.7 & 3.1-8.0 & mmol/L & 紫外-谷氨酸脱氢酶法 \\
22 & 肌酐(8-HR) & & CRE & 81.0 & 57-97 & $\mu$mol/L & 肌氨酸氧化酶法 \\
23 & 肌酸激酶(8-HR) & & CK & 84 & 50-310 & U/L & N-乙酰半胱氨酸法 \\
24 & 肌酸激酶同功酶 & & CK-MB & 12.43 & <25 & U/L & 免疫抑制法 \\
25 & 乳酸脱氢酶(8-HR) & & LDH & 186 & 120-250 & U/L & 乳酸法 \\
26 & $\alpha$-羟丁酸脱氢酶(陕HR) & & $\alpha$-HBDH & 140 & 72-182 & U/L & DGKC法 \\
27 & 钙(8-HR) & & Ca & 2.26 & 2.2-2.7 & mmol/L & 偶氮胂III法 \\
\hline
\end{tabular}
2026-08-10 19:34:28,713 INFO     29 [qwen-vl-parser] page=2 table: 34 LaTeX lines (bbox 40-73)
2026-08-10 19:34:28,713 INFO     29 [qwen-vl-parser] page=2 table: 34 sections
2026-08-10 19:34:29,013 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2106219, prompt_len=764
2026-08-10 19:34:30,446 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-06"
}
```
2026-08-10 19:34:30,448 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2026-03-06
2026-08-10 19:34:30,466 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2106219, prompt_len=401
2026-08-10 19:34:33,079 INFO     29 [qwen-vl-parser] text API response (len=424):
["空军军医大学第二附属医院(唐都医院)", "病理图文诊断报告单", "病理号: 2610441", "ID号: 62893718", "住院号:", "姓名", "性别: 男", "年龄: 55", "送检单位: 唐都医院", "科室: 肿瘤科三病区", "床号:", "送检日期: 2026-03-05", "报告时间: 2026-03-06", "肉眼所见:", "支气管镜活检标本。", "光镜所见:", "病理诊断:", "(左肺上叶尖段)鳞状上皮中-重度异型增生并局部癌变(鳞状细胞癌)。", "[注: 此例仅为小组织活检标本, 有一定局限性, 有可能不能代表病变全貌特征]", "初诊医师: 苟晨靓 签名:", "苟晨靓", "主诊医师: 富金 签名:", "富金", "此报告签名医生信息已经过北京CA数字认证, 涂改无效。如对此报告有任何疑问, 请立即与病理科联系。", "此报告仅此一份, 请妥善保管, 遗失不补。", ""]
2026-08-10 19:34:33,080 INFO     29 [qwen-vl-parser] page=3 text: 25 lines (bbox 74-98)
2026-08-10 19:34:33,080 INFO     29 [qwen-vl-parser] page=3 text: 25 sections
2026-08-10 19:34:33,330 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1300896, prompt_len=764
2026-08-10 19:34:34,714 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 19:34:34,715 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 19:34:34,730 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1300896, prompt_len=401
2026-08-10 19:34:36,403 INFO     29 [qwen-vl-parser] text API response (len=292):
["中国人民解放军联勤保障部队第九八九医院", "出院证", "姓名", "性别", "男", "年龄", "55岁", "费别", "ID号", "2019131", "住院号", "A28146", "入院日期", "2026-02-22", "出院日期", "2026-03-02", "住院天数", "8", "出院科室", "肿瘤科病区", "出院诊断:", "肺占位", "出院情况:", "一般情况可", "出院医嘱:", "他院继续治疗", "经治医生:", "刘佳", "日期:", "2026-03-02", "费川已核LY-16", "审核人:于德艳", ""]
2026-08-10 19:34:36,404 INFO     29 [qwen-vl-parser] page=4 text: 32 lines (bbox 99-130)
2026-08-10 19:34:36,404 INFO     29 [qwen-vl-parser] page=4 text: 32 sections
2026-08-10 19:34:36,807 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3510653, prompt_len=764
2026-08-10 19:34:38,193 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 19:34:38,194 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 19:34:38,206 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3510653, prompt_len=401
2026-08-10 19:34:43,149 INFO     29 [qwen-vl-parser] text API response (len=912):
["中国人民解放军联勤保障部队第九八九医院", "姓名:水月强", "病区(科):肿瘤科病区", "床号:11", "出院记录", "姓名:", "性别:男", "年龄:55岁", "入院时间:2026-02-22 08:42", "出院时间:2026-03-02", "住院天数:8天", "入院情况:2025年12月无明显诱因出现胸闷,无发热、咳嗽、盗汗不适,未在意。2天前出现咯血,", "色鲜红,量约10ml,2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大", "淋巴结,双肺肺气肿,胸骨陈旧性骨折。入院当天再次出现咯血,急诊入院。入院查体:神志清楚,精", "神好,双肺呼吸音清,未闻及干湿性罗音,心律齐,心音低钝,各瓣膜听诊区未闻及病理性杂音。", "入院诊断:1、{肺肿物}", "2、肺气肿", "诊疗经过:患者入科后查血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝", "肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。", "心电图:正常。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气", "肿;3.上腹部CT增强未见明显异常。进一步行CT引导下穿刺活检,病理:(左肺穿刺组织)慢性炎症,间", "质纤维组织增生、淋巴细胞浸润,请结合临床综合考虑。免疫组化结果:CK7(+),TTF-1(+),NapsinA", "(+),CK-Pan(+),Ki-67(5%),P63(-)。建议患者再次穿刺活检或手术治疗,但家属要求出院,经请", "示潘雪峰主任后同意,为患者办理出院手续。", "出院诊断:1、{肺肿物}", "2、肺气肿", "出院情况:目前患者生命体征平稳,病情稳定。", "出院医嘱及健康指导:", "他院继续治疗。", "/刘佳}", "x", "√", "※", "N", "□", "☐", "I", "II", "III", "IV", "V", "(", "{", "[", "(", "更多", ""]
2026-08-10 19:34:43,152 INFO     29 [qwen-vl-parser] page=5 text: 46 lines (bbox 131-176)
2026-08-10 19:34:43,152 INFO     29 [qwen-vl-parser] page=5 text: 46 sections
2026-08-10 19:34:43,288 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1191531, prompt_len=764
2026-08-10 19:34:44,751 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-02-23"
}
```
2026-08-10 19:34:44,752 INFO     29 [qwen-vl-parser] page=6 classify=table report_date=2026-02-23
2026-08-10 19:34:44,765 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1191531, prompt_len=756
2026-08-10 19:34:59,439 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:34:59.436+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:34:59,506 INFO     29 [qwen-vl-parser] table API response (len=2740):
\begin{tabular}{llllllll}
\hline
\multicolumn{8}{c}{\textbf{联勤保障部队第九八九医院检验报告单}} \\
\multicolumn{4}{l}{迈琪7500} & \multicolumn{4}{r}{住院} \\
\hline
\textbf{姓} & : & \textbf{性} & 别:男 & \textbf{年} & 龄:55岁 & \textbf{标本编号:}56 & \\
\textbf{ID} & :J.2015101 & \textbf{费} & 别:自费 & \textbf{诊} & 断:肺肿物 & \textbf{标本种类:}静脉血 & \\
\textbf{科} & 室:肿瘤科病区 & \textbf{床} & 号:30 & \textbf{备} & 注: & & \\
\hline
\textbf{NO} & \textbf{代号} & \textbf{名称} & \textbf{结果} & \textbf{参考值} & \textbf{单位} & & \\
\hline
1 & WBC & 白细胞计数 & 9.63 & ↑ 3.5-9.5 & 10⁹/L & & \\
2 & RBC & 红细胞计数 & 4.36 & 4.3-5.8 & 10¹²/L & & \\
3 & HGB & 血红蛋白 & 141 & 130-175 & g/L & & \\
4 & HCT & 红细胞比积 & 42.7 & 40-50 & \% & & \\
5 & MCV & 平均红细胞体积 & 97.9 & 82-100 & fL & & \\
6 & MCH & 平均血红蛋白量 & 32.4 & 27-34 & pg & & \\
7 & MCHC & 平均血红蛋白浓度 & 330.0 & 316-354 & g/L & & \\
8 & PLT & 血小板计数 & 268 & 100-350 & 10⁹/L & & \\
9 & LYMPH\% & 淋巴细胞比例 & 15.3 & ↓ 20-50 & \% & & \\
10 & MONO\% & 单核细胞比例 & 6.1 & 3-10 & \% & & \\
11 & NEUT\% & 中性粒细胞比例 & 71.5 & 40-75 & \% & & \\
12 & E0\% & 嗜酸性细胞比例 & 6.7 & 0.4-8 & \% & & \\
13 & BASO\% & 嗜碱性细胞比例 & 0.4 & 0-1 & \% & & \\
14 & LYMPH\# & 淋巴细胞计数 & 1.47 & 1.1-3.2 & 10⁹/L & & \\
15 & MONO\# & 单核细胞计数 & 0.6 & 0.1-0.6 & 10⁹/L & & \\
16 & NEUT\# & 中性粒细胞计数 & 6.88 & ↑ 1.8-6.3 & 10⁹/L & & \\
17 & E0\# & 嗜酸性细胞计数 & 0.65 & ↑ 0.02-0.62 & 10⁹/L & & \\
18 & BASO\# & 嗜碱性细胞计数 & 0.04 & 0-0.06 & 10⁹/L & & \\
19 & RDW-CV & 红细胞分布宽度CV & 14.0 & 11-15.5 & \% & & \\
20 & RDW-SD & 红细胞分布宽度SD & 49.5 & 37-50 & fL & & \\
21 & PCT & 血小板压积 & 0.28 & 0.11-0.28 & & & \\
\hline
\textbf{NO} & \textbf{代号} & \textbf{名称} & \textbf{结果} & \textbf{参考值} & \textbf{单位} & & \\
\hline
22 & MPV & 平均血小板体积 & 10.4 & 6-13 & fL & & \\
23 & PDW & 血小板分布宽度 & 16.4 & 9-17 & fL & & \\
24 & P-LCR & 大血小板比例 & 28.6 & 13-43 & \% & & \\
25 & IGM & 幼稚粒细胞绝对值 & 0.01 & 0-0.06 & 10⁹/L & & \\
26 & IGC & 幼稚粒细胞百分比 & 0.10 & 0-0.6 & \% & & \\
\hline
\end{tabular}

\begin{tabular}{llllllll}
\hline
\multicolumn{8}{c}{\textbf{联勤保障部队第九八九医院检验报告单}} \\
\multicolumn{4}{l}{血凝Denting-1} & \multicolumn{4}{r}{住院} \\
\hline
\textbf{姓} & : & \textbf{性} & 别:男 & \textbf{年} & 龄:55岁 & \textbf{标本编号:}20 & \\
\textbf{ID} & :J.2015101 & \textbf{费} & 别:自费 & \textbf{诊} & 断:肺肿物 & \textbf{标本种类:}静脉血 & \\
\textbf{科} & 室:肿瘤科病区 & \textbf{床} & 号:30 & \textbf{备} & 注: & & \\
\hline
\textbf{No} & \textbf{项目代号} & \textbf{项目名称} & \textbf{结果} & \textbf{参考范围} & \textbf{单位} & & \\
\hline
1 & PT-1 & 凝血酶原时间 & 10.4 & 9.2-13.9 & SEC & & \\
2 & PIR-1 & PT报告活动度 & 117 & 70-130 & \% & & \\
3 & INR & 国际标准化比值（INR） & 0.88 & 0.8-1.2 & & & \\
4 & APTT-1 & 活化部分凝血活酶时间(APTT) & 33.3 & 21.2-35.7 & soc & & \\
5 & FIB & 纤维蛋白原 & 3.7 & 2-4 & g/L & & \\
6 & TT-1 & 凝血酶时间 & 14.8 & 10.2-20.1 & soc & & \\
7 & D-DIMER-1 & D-二聚体 & 446 & 0-550 & ug/L & & \\
\hline
\end{tabular}
2026-08-10 19:34:59,507 INFO     29 [qwen-vl-parser] page=6 table: 64 LaTeX lines (bbox 177-240)
2026-08-10 19:34:59,507 INFO     29 [qwen-vl-parser] page=6 table: 64 sections
2026-08-10 19:34:59,592 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=598056, prompt_len=764
2026-08-10 19:35:01,014 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-02-23"
}
```
2026-08-10 19:35:01,015 INFO     29 [qwen-vl-parser] page=7 classify=table report_date=2026-02-23
2026-08-10 19:35:01,027 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=598056, prompt_len=756
2026-08-10 19:35:03,273 INFO     29 [qwen-vl-parser] table API response (len=415):
\begin{tabular}{llllll}
\hline
No & 项目代号 & 项目名称 & 结果 & 参考范围 & 单位 \\
\hline
1 & HBsAg & 乙肝肝炎病毒表面抗原 & 阴性 & 阴性 & \\
2 & HBsAb & 乙肝肝炎病毒表面抗体 & 阳性(+) & 阴性-阳性 & \\
3 & HBeAg & 乙肝肝炎病毒e抗原 & 阴性 & 阴性 & \\
4 & HBeAb & 乙肝肝炎病毒e抗体 & 阴性 & 阴性 & \\
5 & HBcAb & 乙肝肝炎病毒核心抗体(IgG) & 弱阳性(±) & 阴性 & \\
6 & TP-Ab & 梅毒螺旋体特异抗体(酶免) & 阴性 & 阴性 & \\
7 & HIV-Ab & 人类免疫缺陷病毒抗体 & 阴性 & 阴性 & \\
8 & HCV-Ab & 丙肝肝炎病毒抗体 & 阴性 & 阴性 & \\
\hline
\end{tabular}
2026-08-10 19:35:03,274 INFO     29 [qwen-vl-parser] page=7 table: 15 LaTeX lines (bbox 241-255)
2026-08-10 19:35:03,275 INFO     29 [qwen-vl-parser] page=7 table: 15 sections
2026-08-10 19:35:03,396 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=971541, prompt_len=764
2026-08-10 19:35:04,785 INFO     29 [qwen-vl-parser] classify API response (len=56):
```json
{
  "type": "table",
  "report_date": null
}
```
2026-08-10 19:35:04,785 INFO     29 [qwen-vl-parser] page=8 classify=table report_date=None
2026-08-10 19:35:04,794 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=971541, prompt_len=756
2026-08-10 19:35:12,686 INFO     29 [qwen-vl-parser] table API response (len=1622):
\begin{tabular}{lllllllll}
\hline
No. & 项 & 目 & 英文名称 & 结果 & & 参考值 & 单位 & 检测方法 \\
\hline
1 & 白细胞计数(8-HR) & & WBC & 11.44 & $\uparrow$ & 3.5-9.5 & E+09/L & 半导体激光流式细胞术 \\
2 & 淋巴细胞百分率 & & LYMPH\% & 14.4 & $\downarrow$ & 20-50 & \% & 计算法 \\
3 & 单核细胞百分率 & & MONO\% & 7.4 & & 3-10 & \% & 计算法 \\
4 & 中性粒细胞百分率 & & NEUT\% & 73.7 & & 40-75 & \% & 计算法 \\
5 & 嗜酸性粒细胞百分率 & & E0\% & 4.2 & & 0.4-8.0 & \% & 计算法 \\
6 & 嗜碱性粒细胞百分率 & & BASO\% & 0.3 & & 0-1 & \% & 计算法 \\
7 & 淋巴细胞绝对值 & & LYMPH\# & 1.65 & & 1.1-3.2 & E+09/L & 半导体激光流式细胞术 \\
8 & 单核细胞绝对值 & & MONO\# & 0.85 & $\uparrow$ & 0.1-0.6 & E+09/L & 半导体激光流式细胞术 \\
9 & 中性粒细胞绝对值 & & NEUT\# & 8.43 & $\uparrow$ & 1.8-6.3 & E+09/L & 半导体激光流式细胞术 \\
10 & 嗜酸性粒细胞绝对值 & & E0\# & 0.48 & & 0.02-0.52 & E+09/L & 半导体激光流式细胞术 \\
11 & 嗜碱性粒细胞绝对值 & & BASO\# & 0.03 & & 0-0.06 & E+09/L & 半导体激光流式细胞术 \\
12 & 血小板计数(8-HR) & & PLT & 269 & & 125-350 & E+09/L & 鞘流电阻抗法 \\
13 & 血小板分布宽度 & & PDW & 11.3 & $\downarrow$ & 15.5-18.1 & fL & 计算法 \\
14 & 平均血小板体积 & & MPV & 10.1 & & 9.4-12.5 & fL & 计算法 \\
15 & 大血小板比率 & & P-LCR & 25.3 & & 13-43 & \% & 计算法 \\
16 & 血小板比积 & & PCT & 0.270 & & 0.11-0.28 & \% & 计算法 \\
17 & 红细胞计数(8-HR) & & RBC & 4.56 & & 4.3-5.8 & E+12/L & 鞘流电阻抗法 \\
18 & 血红蛋白(8-HR) & & HGB & 148 & & 130-175 & g/L & SLS-血测定法 \\
19 & 红细胞压积(8-HR) & & HCT & 44.8 & & 40-50 & \% & 鞘流电阻抗法 \\
20 & 平均红细胞体积(8-HR) & & MCV & 98.2 & & 82-100 & fL & 计算法 \\
21 & 平均血红蛋白含量(8-HR) & & MCH & 32.5 & & 27-34 & pg & 计算法 \\
22 & 平均血红蛋白浓度(8-HR) & & MCHC & 330 & & 316-354 & g/L & 计算法 \\
23 & 红细胞分布宽度CV & & RDW\% & 13.4 & & 10.9-15.4 & \% & 计算法 \\
24 & 红细胞分布宽度SD & & RDW & 49.0 & $\uparrow$ & 39-46 & fL & 计算法 \\
\hline
\end{tabular}
2026-08-10 19:35:12,687 INFO     29 [qwen-vl-parser] page=8 table: 30 LaTeX lines (bbox 256-285)
2026-08-10 19:35:12,687 INFO     29 [qwen-vl-parser] page=8 table: 30 sections
2026-08-10 19:35:12,777 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=692824, prompt_len=764
2026-08-10 19:35:14,205 INFO     29 [qwen-vl-parser] classify API response (len=56):
```json
{
  "type": "table",
  "report_date": null
}
```
2026-08-10 19:35:14,205 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=None
2026-08-10 19:35:14,219 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=692824, prompt_len=756
2026-08-10 19:35:16,757 INFO     29 [qwen-vl-parser] table API response (len=545):
\begin{tabular}{ccccccc}
\hline
No. 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\
\hline
1 & 乙肝表面抗原 & HBsAg & 0.00 & (-) & $<$0.03 & IU/mL \\
2 & 乙肝表面抗体 & Anti-HBs & 16.90 & (+) & $<$5.00 & mIU/mL \\
3 & 乙肝e抗原 & HBeAg & 0.00 & (-) & $<$1.00 & C.O.I \\
4 & 乙肝e抗体 & Anti-HBe & 49.60 & (-) & $<$50.00 & Inh\% \\
5 & 乙肝核心抗体 & Anti-HBc & 4.40 & (+) & $<$1.00 & C.O.I \\
6 & 丙型肝炎抗体 & HCVAb & 0.10 & (-) & $<$1.00 & C.O.I \\
7 & 人免疫缺陷病毒抗原抗体 & HIVAg+Ab & 0.00 & (-) & $<$1.00 & C.O.I \\
8 & 梅毒抗体 & Anti-TP & 0.00 & (-) & $<$1.00 & C.O.I \\
\hline
\end{tabular}
2026-08-10 19:35:16,759 INFO     29 [qwen-vl-parser] page=9 table: 14 LaTeX lines (bbox 286-299)
2026-08-10 19:35:16,759 INFO     29 [qwen-vl-parser] page=9 table: 14 sections
2026-08-10 19:35:16,838 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=404193, prompt_len=764
2026-08-10 19:35:18,061 INFO     29 [qwen-vl-parser] classify API response (len=56):
```json
{
  "type": "table",
  "report_date": null
}
```
2026-08-10 19:35:18,062 INFO     29 [qwen-vl-parser] page=10 classify=table report_date=None
2026-08-10 19:35:18,073 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=404193, prompt_len=756
2026-08-10 19:35:19,166 INFO     29 [qwen-vl-parser] table API response (len=185):
\begin{tabular}{ccccccccc}
\hline
No & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\
\hline
1 & ABO血型鉴定 & & ABO & O型 & & & 微柱凝胶法、微孔板法 \\
2 & RH(D)血型鉴定 & & Rh & 阳性 & & & \\
\hline
\end{tabular}
2026-08-10 19:35:19,168 INFO     29 [qwen-vl-parser] page=10 table: 8 LaTeX lines (bbox 300-307)
2026-08-10 19:35:19,168 INFO     29 [qwen-vl-parser] page=10 table: 8 sections
2026-08-10 19:35:19,261 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=609123, prompt_len=764
2026-08-10 19:35:20,504 INFO     29 [qwen-vl-parser] classify API response (len=56):
```json
{
  "type": "table",
  "report_date": null
}
```
2026-08-10 19:35:20,505 INFO     29 [qwen-vl-parser] page=11 classify=table report_date=None
2026-08-10 19:35:20,518 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=609123, prompt_len=756
2026-08-10 19:35:23,052 INFO     29 [qwen-vl-parser] table API response (len=518):
\begin{tabular}{ccccccll}
\hline
No. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\
\hline
1 & \multicolumn{2}{l}{游离三碘甲状腺原氨酸(8-HR)} & FT3 & 4.31 & 3.85-6.3 & pmol/L & 电化学发光法 \\
2 & \multicolumn{2}{l}{游离甲状腺素(8-HR)} & FT4 & 14.90 & 12.8-21.3 & pmol/L & 电化学发光法 \\
3 & \multicolumn{2}{l}{三碘甲状腺原氨酸(8-HR)} & T3 & 1.81 & 1.3-2.4 & nmol/L & 电化学发光法 \\
4 & \multicolumn{2}{l}{甲状腺素(8-HR)} & T4 & 102.00 & 70-140 & nmol/L & 电化学发光法 \\
5 & \multicolumn{2}{l}{促甲状腺素(8-HR)} & TSH & 2.45 & 0.27-4.20 & uIU/mL & 电化学发光法 \\
\hline
\end{tabular}
2026-08-10 19:35:23,053 INFO     29 [qwen-vl-parser] page=11 table: 11 LaTeX lines (bbox 308-318)
2026-08-10 19:35:23,053 INFO     29 [qwen-vl-parser] page=11 table: 11 sections
2026-08-10 19:35:23,139 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=603259, prompt_len=764
2026-08-10 19:35:24,397 INFO     29 [qwen-vl-parser] classify API response (len=56):
```json
{
  "type": "table",
  "report_date": null
}
```
2026-08-10 19:35:24,398 INFO     29 [qwen-vl-parser] page=12 classify=table report_date=None
2026-08-10 19:35:24,411 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=603259, prompt_len=756
2026-08-10 19:35:26,310 INFO     29 [qwen-vl-parser] table API response (len=345):
\begin{tabular}{ccccccl}
\hline
No. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\
\hline
1 & 肌酸激酶同工酶 & & CK-MB & $<$0.22 & 0-2.37 & ng/mL & 化学发光法 \\
2 & 肌钙蛋白I & & cTnI & $<$0.012 & 0-0.034 & ng/mL & 化学发光法 \\
3 & 肌红蛋白 & & MYO & 45.94 & 0-121 & ng/mL & 化学发光法 \\
4 & N端脑利钠肽前体 & & NT-proBNP & $<$20.00 & 健康人群$<$125 & pg/mL & 化学发光法 \\
\hline
\end{tabular}
2026-08-10 19:35:26,312 INFO     29 [qwen-vl-parser] page=12 table: 10 LaTeX lines (bbox 319-328)
2026-08-10 19:35:26,312 INFO     29 [qwen-vl-parser] page=12 table: 10 sections
2026-08-10 19:35:26,417 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=770568, prompt_len=764
2026-08-10 19:35:27,843 INFO     29 [qwen-vl-parser] classify API response (len=56):
```json
{
  "type": "table",
  "report_date": null
}
```
2026-08-10 19:35:27,843 INFO     29 [qwen-vl-parser] page=13 classify=table report_date=None
2026-08-10 19:35:27,852 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=770568, prompt_len=756
2026-08-10 19:35:31,733 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:35:31.730+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:35:33,094 INFO     29 [qwen-vl-parser] table API response (len=547):
\begin{tabular}{ccccccc}
\hline
No & 项 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\
\hline
1 & 凝血酶原时间(陕HR) & PT & 11.2 & 9.8-12.1 & sec & 凝固法 \\
2 & 凝血酶原活动度 & PTA & 98.2 & 70-130 & \% & 凝固法 \\
3 & 国际标准化比值(陕HR) & INR & 0.97 & 0.7-1.3 & & 凝固法 \\
4 & 活化部分凝血活酶时间(陕HR) & APTT & 36.1 & 22.7-31.8 & sec & 凝固法 \\
5 & 纤维蛋白原含量(陕HR) & Fib & 6.680 & 1.8-3.5 & g/L & 凝固法 \\
6 & 凝血酶时间(陕HR) & TT & 15.5 & 14-21 & sec & 凝固法 \\
7 & 纤维蛋白(原)降解产物(定量) & FDP & 4.50 & 0-5 & $\mu$g/mL & 胶乳免疫比浊法 \\
8 & D-二聚体(定量)(陕HR) & D D & 1.185 & 0-1 & $\mu$g/mL & 胶乳免疫比浊法 \\
\hline
\end{tabular}
2026-08-10 19:35:33,095 INFO     29 [qwen-vl-parser] page=13 table: 14 LaTeX lines (bbox 329-342)
2026-08-10 19:35:33,095 INFO     29 [qwen-vl-parser] page=13 table: 14 sections
2026-08-10 19:35:33,218 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1130002, prompt_len=764
2026-08-10 19:35:34,629 INFO     29 [qwen-vl-parser] classify API response (len=56):
```json
{
  "type": "table",
  "report_date": null
}
```
2026-08-10 19:35:34,629 INFO     29 [qwen-vl-parser] page=14 classify=table report_date=None
2026-08-10 19:35:34,643 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1130002, prompt_len=756
2026-08-10 19:35:43,104 INFO     29 [qwen-vl-parser] table API response (len=1700):
\begin{tabular}{llllllll}
\hline
No. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\
\hline
1 & 血糖(空腹)(8-HR) & & GLU & 5.56 & 3.9-6.1 & mmol/L & 己糖激酶法 \\
2 & 钾(8-HR) & & K & 4.36 & 3.5-5.3 & mmol/L & 间接离子选择电极法 \\
3 & 钠(8-HR) & & Na & 137.8 & 137-147 & mmol/L & 间接离子选择电极法 \\
4 & 氯(8-HR) & & Cl & 100.9 & 99-110 & mmol/L & 间接离子选择电极法 \\
5 & 总蛋白(8-HR) & & TP & 73.0 & 65-85 & g/L & 双缩脲比色法 \\
6 & 白蛋白(8-HR) & & ALB & 42.4 & 40-55 & g/L & 溴甲酚绿法 \\
7 & 球蛋白 & & GLO & 30.6 & 20-40 & g/L & 计算法 \\
8 & 白球比 & & A/G & 1.4 & 1.2-2.4 & & 计算法 \\
9 & 总胆红素(8-HR) & & T-BIL & 12.1 & 0-26 & $\mu$mol/L & 钒酸盐氧化法 \\
10 & 直接胆红素(8-HR) & & D-BIL & 3.5 & 0-6.8 & $\mu$mol/L & 钒酸盐氧化法 \\
11 & 间接胆红素 & & I-BIL & 8.6 & 0-14 & $\mu$mol/L & 计算法 \\
12 & 丙氨酸氨基转移酶(8-HR) & & ALT & 26 & 9-50 & U/L & 紫外-乳酸脱氢酶法 \\
13 & 天门冬氨酸氨基转移酶(8-HR) & & AST & 21 & 15-40 & U/L & 紫外-苹果酸脱氢酶法 \\
14 & AST/ALT & & & 0.81 & & & 计算法 \\
15 & 碱性磷酸酶(8-HR) & & ALP & 106 & 45-125 & U/L & AMP缓冲液法 \\
16 & 总胆汁酸(陕HR) & & TBA & 12.6 & 0-10 & $\mu$mol/L & 循环酶法 \\
17 & 胆碱酯酶(陕HR) & & CHE & 6970 & 5000-12000 & U/L & 丁酰硫代胆碱/铁氰化钾 \\
18 & $\gamma$-谷氨酰转移酶(8-HR) & & GGT & 23 & 10-60 & U/L & 速率法 \\
19 & eGFR(CKD-EPI) & & eGFR & 93.12 & >90 & ml/min/1.73m2 & 计算法 \\
20 & 尿酸(8-HR) & & UA & 263.0 & 208-428 & $\mu$mol/L & 氧化酶法 \\
21 & 尿素(8-HR) & & UREA & 6.7 & 3.1-8.0 & mmol/L & 紫外-谷氨酸脱氢酶法 \\
22 & 肌酐(8-HR) & & CRE & 81.0 & 57-97 & $\mu$mol/L & 肌氨酸氧化酶法 \\
23 & 肌酸激酶(8-HR) & & CK & 84 & 50-310 & U/L & N-乙酰半胱氨酸法 \\
24 & 肌酸激酶同功酶 & & CK-MB & 12.43 & <25 & U/L & 免疫抑制法 \\
25 & 乳酸脱氢酶(8-HR) & & LDH & 186 & 120-250 & U/L & 乳酸法 \\
26 & $\alpha$-羟丁酸脱氢酶(陕HR) & & $\alpha$-HBDH & 140 & 72-182 & U/L & DGKC法 \\
27 & 钙(8-HR) & & Ca & 2.26 & 2.2-2.7 & mmol/L & 偶氮胂III法 \\
\hline
\end{tabular}
2026-08-10 19:35:43,106 INFO     29 [qwen-vl-parser] page=14 table: 33 LaTeX lines (bbox 343-375)
2026-08-10 19:35:43,107 INFO     29 [qwen-vl-parser] page=14 table: 33 sections
2026-08-10 19:35:43,107 INFO     29 [qwen-vl-parser] parse_pdf done: 376 sections from 14 pages.
2026-08-10 19:35:43,117 INFO     29 Close text detector.
2026-08-10 19:35:43,545 INFO     29 Close text recognizer.
2026-08-10 19:35:43,957 INFO     29 Close recognizer.
2026-08-10 19:35:44,356 INFO     29 Close recognizer.
2026-08-10 19:35:44,758 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 19:35:44,758 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Parser:MedLink | outputs={"html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "json"}
2026-08-10 19:35:44,758 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 19:35:44,774 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:35:44,775 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 空军军医大学唐都医院\n[BBOX-1] 查阅电子胶片\n[BBOX-2] CT检查报告单\n[BBOX-3] ID号：62893718\n[BBOX-4] 检查时间：2026-03-04\n[BBOX-5] 检查号：CT2603030254\n[BBOX-6] 住院\n[BBOX-7] 报告日期：2026-03-04\n[BBOX-8] 影像号：62893718\n[BBOX-9] 姓名\n[BBOX-10] 性别：男\n[BBOX-11] 年龄：55岁\n[BBOX-12] 申请科室：肿瘤科三病区\n[BBOX-13] 床号：\n[BBOX-14] 检查项目：盆腔CT平扫|胸部CT平扫|胸部CT增强|上腹部CT平扫(肝胆胰脾)|下腹部CT平扫\n[BBOX-15] 检查方法：平扫+增强\n[BBOX-16] 影像所见：\n[BBOX-17] 左肺上叶尖后段支气管狭窄，可见不规则团块状软组织密度影，大小约\n[BBOX-18] 4.5×4.0×5.9cm，局部紧贴叶间胸膜，可见“胸膜凹陷征”，平扫CT值约32HU，增\n[BBOX-19] 强扫描呈不均匀强化，两期CT值约33HU、59HU；右肺下叶前基底段可见局限性无肺纹\n[BBOX-20] 理区；余双肺野清晰，肺纹理走行自然，双肺门影不大。气管及纵隔位置居中，纵隔\n[BBOX-21] 可见多发增大淋巴结，较大者短径约0.6cm。心膈影未见异常，双侧胸膜无增厚，未见\n[BBOX-22] 胸腔积液。骨性胸廓骨质结构完整。\n[BBOX-23] 肝随边缘光滑，各叶大小比例正常，肝实质内密度均匀，未见明显异常密度影及\n[BBOX-24] 占位性病变，肝内外胆管未见扩张，肝门部结构清晰，未见占位性病变，胆囊不大，\n[BBOX-25] 壁薄且均匀，腔内未见阳性结石影。胰腺大小、形态及密度未见异常。脾不大，实质\n[BBOX-26] 密度均匀，双肾大小形态良好，实质密度均匀，双侧肾盂未见扩张，右肾可见阳性结\n[BBOX-27] 石影。腹腔内及腹膜后未见明显肿大淋巴结影，未见腹水征象。\n[BBOX-28] 膀胱充盈良好，壁厚薄均匀，未见占位性病变。前列腺大小、形态及密度未见异\n[BBOX-29] 常。双侧精囊腺大小、形态及密度未见异常。直肠形态正常，未见占位性病变。盆腔\n[BBOX-30] 淋巴结无肿大，盆腔内未见积液征象。\n[BBOX-31] 诊断意见：\n[BBOX-32] 1、左肺上叶尖后段占位性病变，多考虑周围型肺癌；纵隔多发增大淋巴结；\n[BBOX-33] 2、右肾结石；肝、胆、胰、脾及左肾CT扫描未见明显异常。\n[BBOX-34] 3、膀胱、前列腺、双侧精囊腺及直肠CT扫描未见明确病变。\n[BBOX-35] 本意见仅供临床医生参考，盖章或签字后生效！\n[BBOX-36] 报告医师：杨露\n[BBOX-37] 审核医师：\n[BBOX-38] 该信息经过北京CA数字签名认证\n[BBOX-39] 签名验证的信息摘要值为：3BFB10562BBC74DF5F886274A0100FAG。检查号：CT2603030254。\n[BBOX-40] \\begin{tabular}{lllllllll}\n[BBOX-41] 报告时间: 2026-03-04\n[BBOX-42] \\hline\n[BBOX-43] No. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n[BBOX-44] \\hline\n[BBOX-45] 1 & 血糖(空腹)(8-HR) & & GLU & 5.56 & 3.9-6.1 & mmol/L & 己糖激酶法 \\\\\n[BBOX-46] 2 & 钾(8-HR) & & K & 4.36 & 3.5-5.3 & mmol/L & 间接离子选择电极法 \\\\\n[BBOX-47] 3 & 钠(8-HR) & & Na & 137.8 & 137-147 & mmol/L & 间接离子选择电极法 \\\\\n[BBOX-48] 4 & 氯(8-HR) & & Cl & 100.9 & 99-110 & mmol/L & 间接离子选择电极法 \\\\\n[BBOX-49] 5 & 总蛋白(8-HR) & & TP & 73.0 & 65-85 & g/L & 双缩脲比色法 \\\\\n[BBOX-50] 6 & 白蛋白(8-HR) & & ALB & 42.4 & 40-55 & g/L & 溴甲酚绿法 \\\\\n[BBOX-51] 7 & 球蛋白 & & GLO & 30.6 & 20-40 & g/L & 计算法 \\\\\n[BBOX-52] 8 & 白球比 & & A/G & 1.4 & 1.2-2.4 & & 计算法 \\\\\n[BBOX-53] 9 & 总胆红素(8-HR) & & T-BIL & 12.1 & 0-26 & $\\mu$mol/L & 钒酸盐氧化法 \\\\\n[BBOX-54] 10 & 直接胆红素(8-HR) & & D-BIL & 3.5 & 0-6.8 & $\\mu$mol/L & 钒酸盐氧化法 \\\\\n[BBOX-55] 11 & 间接胆红素 & & I-BIL & 8.6 & 0-14 & $\\mu$mol/L & 计算法 \\\\\n[BBOX-56] 12 & 丙氨酸氨基转移酶(8-HR) & & ALT & 26 & 9-50 & U/L & 紫外-乳酸脱氢酶法 \\\\\n[BBOX-57] 13 & 天门冬氨酸氨基转移酶(8-HR) & & AST & 21 & 15-40 & U/L & 紫外-苹果酸脱氢酶法 \\\\\n[BBOX-58] 14 & AST/ALT & & & 0.81 & & & 计算法 \\\\\n[BBOX-59] 15 & 碱性磷酸酶(8-HR) & & ALP & 106 & 45-125 & U/L & AMP缓冲液法 \\\\\n[BBOX-60] 16 & 总胆汁酸(陕HR) & & TBA & 12.6 & 0-10 & $\\mu$mol/L & 循环酶法 \\\\\n[BBOX-61] 17 & 胆碱酯酶(陕HR) & & CHE & 6970 & 5000-12000 & U/L & 丁酰硫代胆碱/铁氰化钾 \\\\\n[BBOX-62] 18 & $\\gamma$-谷氨酰转移酶(8-HR) & & GGT & 23 & 10-60 & U/L & 速率法 \\\\\n[BBOX-63] 19 & eGFR(CKD-EPI) & & eGFR & 93.12 & >90 & ml/min/1.73m2 & 计算法 \\\\\n[BBOX-64] 20 & 尿酸(8-HR) & & UA & 263.0 & 208-428 & $\\mu$mol/L & 氧化酶法 \\\\\n[BBOX-65] 21 & 尿素(8-HR) & & UREA & 6.7 & 3.1-8.0 & mmol/L & 紫外-谷氨酸脱氢酶法 \\\\\n[BBOX-66] 22 & 肌酐(8-HR) & & CRE & 81.0 & 57-97 & $\\mu$mol/L & 肌氨酸氧化酶法 \\\\\n[BBOX-67] 23 & 肌酸激酶(8-HR) & & CK & 84 & 50-310 & U/L & N-乙酰半胱氨酸法 \\\\\n[BBOX-68] 24 & 肌酸激酶同功酶 & & CK-MB & 12.43 & <25 & U/L & 免疫抑制法 \\\\\n[BBOX-69] 25 & 乳酸脱氢酶(8-HR) & & LDH & 186 & 120-250 & U/L & 乳酸法 \\\\\n[BBOX-70] 26 & $\\alpha$-羟丁酸脱氢酶(陕HR) & & $\\alpha$-HBDH & 140 & 72-182 & U/L & DGKC法 \\\\\n[BBOX-71] 27 & 钙(8-HR) & & Ca & 2.26 & 2.2-2.7 & mmol/L & 偶氮胂III法 \\\\\n[BBOX-72] \\hline\n[BBOX-73] \\end{tabular}\n[BBOX-74] 空军军医大学第二附属医院(唐都医院)\n[BBOX-75] 病理图文诊断报告单\n[BBOX-76] 病理号: 2610441\n[BBOX-77] ID号: 62893718\n[BBOX-78] 住院号:\n[BBOX-79] 姓名\n[BBOX-80] 性别: 男\n[BBOX-81] 年龄: 55\n[BBOX-82] 送检单位: 唐都医院\n[BBOX-83] 科室: 肿瘤科三病区\n[BBOX-84] 床号:\n[BBOX-85] 送检日期: 2026-03-05\n[BBOX-86] 报告时间: 2026-03-06\n[BBOX-87] 肉眼所见:\n[BBOX-88] 支气管镜活检标本。\n[BBOX-89] 光镜所见:\n[BBOX-90] 病理诊断:\n[BBOX-91] (左肺上叶尖段)鳞状上皮中-重度异型增生并局部癌变(鳞状细胞癌)。\n[BBOX-92] [注: 此例仅为小组织活检标本, 有一定局限性, 有可能不能代表病变全貌特征]\n[BBOX-93] 初诊医师: 苟晨靓 签名:\n[BBOX-94] 苟晨靓\n[BBOX-95] 主诊医师: 富金 签名:\n[BBOX-96] 富金\n[BBOX-97] 此报告签名医生信息已经过北京CA数字认证, 涂改无效。如对此报告有任何疑问, 请立即与病理科联系。\n[BBOX-98] 此报告仅此一份, 请妥善保管, 遗失不补。\n[BBOX-99] 中国人民解放军联勤保障部队第九八九医院\n[BBOX-100] 出院证\n[BBOX-101] 姓名\n[BBOX-102] 性别\n[BBOX-103] 男\n[BBOX-104] 年龄\n[BBOX-105] 55岁\n[BBOX-106] 费别\n[BBOX-107] ID号\n[BBOX-108] 2019131\n[BBOX-109] 住院号\n[BBOX-110] A28146\n[BBOX-111] 入院日期\n[BBOX-112] 2026-02-22\n[BBOX-113] 出院日期\n[BBOX-114] 2026-03-02\n[BBOX-115] 住院天数\n[BBOX-116] 8\n[BBOX-117] 出院科室\n[BBOX-118] 肿瘤科病区\n[BBOX-119] 出院诊断:\n[BBOX-120] 肺占位\n[BBOX-121] 出院情况:\n[BBOX-122] 一般情况可\n[BBOX-123] 出院医嘱:\n[BBOX-124] 他院继续治疗\n[BBOX-125] 经治医生:\n[BBOX-126] 刘佳\n[BBOX-127] 日期:\n[BBOX-128] 2026-03-02\n[BBOX-129] 费川已核LY-16\n[BBOX-130] 审核人:于德艳\n[BBOX-131] 中国人民解放军联勤保障部队第九八九医院\n[BBOX-132] 姓名:水月强\n[BBOX-133] 病区(科):肿瘤科病区\n[BBOX-134] 床号:11\n[BBOX-135] 出院记录\n[BBOX-136] 姓名:\n[BBOX-137] 性别:男\n[BBOX-138] 年龄:55岁\n[BBOX-139] 入院时间:2026-02-22 08:42\n[BBOX-140] 出院时间:2026-03-02\n[BBOX-141] 住院天数:8天\n[BBOX-142] 入院情况:2025年12月无明显诱因出现胸闷,无发热、咳嗽、盗汗不适,未在意。2天前出现咯血,\n[BBOX-143] 色鲜红,量约10ml,2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大\n[BBOX-144] 淋巴结,双肺肺气肿,胸骨陈旧性骨折。入院当天再次出现咯血,急诊入院。入院查体:神志清楚,精\n[BBOX-145] 神好,双肺呼吸音清,未闻及干湿性罗音,心律齐,心音低钝,各瓣膜听诊区未闻及病理性杂音。\n[BBOX-146] 入院诊断:1、{肺肿物}\n[BBOX-147] 2、肺气肿\n[BBOX-148] 诊疗经过:患者入科后查血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝\n[BBOX-149] 肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。\n[BBOX-150] 心电图:正常。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气\n[BBOX-151] 肿;3.上腹部CT增强未见明显异常。进一步行CT引导下穿刺活检,病理:(左肺穿刺组织)慢性炎症,间\n[BBOX-152] 质纤维组织增生、淋巴细胞浸润,请结合临床综合考虑。免疫组化结果:CK7(+),TTF-1(+),NapsinA\n[BBOX-153] (+),CK-Pan(+),Ki-67(5%),P63(-)。建议患者再次穿刺活检或手术治疗,但家属要求出院,经请\n[BBOX-154] 示潘雪峰主任后同意,为患者办理出院手续。\n[BBOX-155] 出院诊断:1、{肺肿物}\n[BBOX-156] 2、肺气肿\n[BBOX-157] 出院情况:目前患者生命体征平稳,病情稳定。\n[BBOX-158] 出院医嘱及健康指导:\n[BBOX-159] 他院继续治疗。\n[BBOX-160] /刘佳}\n[BBOX-161] x\n[BBOX-162] √\n[BBOX-163] ※\n[BBOX-164] N\n[BBOX-165] □\n[BBOX-166] ☐\n[BBOX-167] I\n[BBOX-168] II\n[BBOX-169] III\n[BBOX-170] IV\n[BBOX-171] V\n[BBOX-172] (\n[BBOX-173] {\n[BBOX-174] [\n[BBOX-175] (\n[BBOX-176] 更多\n[BBOX-177] \\begin{tabular}{llllllll}\n[BBOX-178] 报告时间: 2026-02-23\n[BBOX-179] \\hline\n[BBOX-180] \\multicolumn{8}{c}{\\textbf{联勤保障部队第九八九医院检验报告单}} \\\\\n[BBOX-181] \\multicolumn{4}{l}{迈琪7500} & \\multicolumn{4}{r}{住院} \\\\\n[BBOX-182] \\hline\n[BBOX-183] \\textbf{姓} & : & \\textbf{性} & 别:男 & \\textbf{年} & 龄:55岁 & \\textbf{标本编号:}56 & \\\\\n[BBOX-184] \\textbf{ID} & :J.2015101 & \\textbf{费} & 别:自费 & \\textbf{诊} & 断:肺肿物 & \\textbf{标本种类:}静脉血 & \\\\\n[BBOX-185] \\textbf{科} & 室:肿瘤科病区 & \\textbf{床} & 号:30 & \\textbf{备} & 注: & & \\\\\n[BBOX-186] \\hline\n[BBOX-187] \\textbf{NO} & \\textbf{代号} & \\textbf{名称} & \\textbf{结果} & \\textbf{参考值} & \\textbf{单位} & & \\\\\n[BBOX-188] \\hline\n[BBOX-189] 1 & WBC & 白细胞计数 & 9.63 & ↑ 3.5-9.5 & 10⁹/L & & \\\\\n[BBOX-190] 2 & RBC & 红细胞计数 & 4.36 & 4.3-5.8 & 10¹²/L & & \\\\\n[BBOX-191] 3 & HGB & 血红蛋白 & 141 & 130-175 & g/L & & \\\\\n[BBOX-192] 4 & HCT & 红细胞比积 & 42.7 & 40-50 & \\% & & \\\\\n[BBOX-193] 5 & MCV & 平均红细胞体积 & 97.9 & 82-100 & fL & & \\\\\n[BBOX-194] 6 & MCH & 平均血红蛋白量 & 32.4 & 27-34 & pg & & \\\\\n[BBOX-195] 7 & MCHC & 平均血红蛋白浓度 & 330.0 & 316-354 & g/L & & \\\\\n[BBOX-196] 8 & PLT & 血小板计数 & 268 & 100-350 & 10⁹/L & & \\\\\n[BBOX-197] 9 & LYMPH\\% & 淋巴细胞比例 & 15.3 & ↓ 20-50 & \\% & & \\\\\n[BBOX-198] 10 & MONO\\% & 单核细胞比例 & 6.1 & 3-10 & \\% & & \\\\\n[BBOX-199] 11 & NEUT\\% & 中性粒细胞比例 & 71.5 & 40-75 & \\% & & \\\\\n[BBOX-200] 12 & E0\\% & 嗜酸性细胞比例 & 6.7 & 0.4-8 & \\% & & \\\\\n[BBOX-201] 13 & BASO\\% & 嗜碱性细胞比例 & 0.4 & 0-1 & \\% & & \\\\\n[BBOX-202] 14 & LYMPH\\# & 淋巴细胞计数 & 1.47 & 1.1-3.2 & 10⁹/L & & \\\\\n[BBOX-203] 15 & MONO\\# & 单核细胞计数 & 0.6 & 0.1-0.6 & 10⁹/L & & \\\\\n[BBOX-204] 16 & NEUT\\# & 中性粒细胞计数 & 6.88 & ↑ 1.8-6.3 & 10⁹/L & & \\\\\n[BBOX-205] 17 & E0\\# & 嗜酸性细胞计数 & 0.65 & ↑ 0.02-0.62 & 10⁹/L & & \\\\\n[BBOX-206] 18 & BASO\\# & 嗜碱性细胞计数 & 0.04 & 0-0.06 & 10⁹/L & & \\\\\n[BBOX-207] 19 & RDW-CV & 红细胞分布宽度CV & 14.0 & 11-15.5 & \\% & & \\\\\n[BBOX-208] 20 & RDW-SD & 红细胞分布宽度SD & 49.5 & 37-50 & fL & & \\\\\n[BBOX-209] 21 & PCT & 血小板压积 & 0.28 & 0.11-0.28 & & & \\\\\n[BBOX-210] \\hline\n[BBOX-211] \\textbf{NO} & \\textbf{代号} & \\textbf{名称} & \\textbf{结果} & \\textbf{参考值} & \\textbf{单位} & & \\\\\n[BBOX-212] \\hline\n[BBOX-213] 22 & MPV & 平均血小板体积 & 10.4 & 6-13 & fL & & \\\\\n[BBOX-214] 23 & PDW & 血小板分布宽度 & 16.4 & 9-17 & fL & & \\\\\n[BBOX-215] 24 & P-LCR & 大血小板比例 & 28.6 & 13-43 & \\% & & \\\\\n[BBOX-216] 25 & IGM & 幼稚粒细胞绝对值 & 0.01 & 0-0.06 & 10⁹/L & & \\\\\n[BBOX-217] 26 & IGC & 幼稚粒细胞百分比 & 0.10 & 0-0.6 & \\% & & \\\\\n[BBOX-218] \\hline\n[BBOX-219] \\end{tabular}\n[BBOX-220] \\begin{tabular}{llllllll}\n[BBOX-221] 报告时间: 2026-02-23\n[BBOX-222] \\hline\n[BBOX-223] \\multicolumn{8}{c}{\\textbf{联勤保障部队第九八九医院检验报告单}} \\\\\n[BBOX-224] \\multicolumn{4}{l}{血凝Denting-1} & \\multicolumn{4}{r}{住院} \\\\\n[BBOX-225] \\hline\n[BBOX-226] \\textbf{姓} & : & \\textbf{性} & 别:男 & \\textbf{年} & 龄:55岁 & \\textbf{标本编号:}20 & \\\\\n[BBOX-227] \\textbf{ID} & :J.2015101 & \\textbf{费} & 别:自费 & \\textbf{诊} & 断:肺肿物 & \\textbf{标本种类:}静脉血 & \\\\\n[BBOX-228] \\textbf{科} & 室:肿瘤科病区 & \\textbf{床} & 号:30 & \\textbf{备} & 注: & & \\\\\n[BBOX-229] \\hline\n[BBOX-230] \\textbf{No} & \\textbf{项目代号} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{参考范围} & \\textbf{单位} & & \\\\\n[BBOX-231] \\hline\n[BBOX-232] 1 & PT-1 & 凝血酶原时间 & 10.4 & 9.2-13.9 & SEC & & \\\\\n[BBOX-233] 2 & PIR-1 & PT报告活动度 & 117 & 70-130 & \\% & & \\\\\n[BBOX-234] 3 & INR & 国际标准化比值（INR） & 0.88 & 0.8-1.2 & & & \\\\\n[BBOX-235] 4 & APTT-1 & 活化部分凝血活酶时间(APTT) & 33.3 & 21.2-35.7 & soc & & \\\\\n[BBOX-236] 5 & FIB & 纤维蛋白原 & 3.7 & 2-4 & g/L & & \\\\\n[BBOX-237] 6 & TT-1 & 凝血酶时间 & 14.8 & 10.2-20.1 & soc & & \\\\\n[BBOX-238] 7 & D-DIMER-1 & D-二聚体 & 446 & 0-550 & ug/L & & \\\\\n[BBOX-239] \\hline\n[BBOX-240] \\end{tabular}\n[BBOX-241] \\begin{tabular}{llllll}\n[BBOX-242] 报告时间: 2026-02-23\n[BBOX-243] \\hline\n[BBOX-244] No & 项目代号 & 项目名称 & 结果 & 参考范围 & 单位 \\\\\n[BBOX-245] \\hline\n[BBOX-246] 1 & HBsAg & 乙肝肝炎病毒表面抗原 & 阴性 & 阴性 & \\\\\n[BBOX-247] 2 & HBsAb & 乙肝肝炎病毒表面抗体 & 阳性(+) & 阴性-阳性 & \\\\\n[BBOX-248] 3 & HBeAg & 乙肝肝炎病毒e抗原 & 阴性 & 阴性 & \\\\\n[BBOX-249] 4 & HBeAb & 乙肝肝炎病毒e抗体 & 阴性 & 阴性 & \\\\\n[BBOX-250] 5 & HBcAb & 乙肝肝炎病毒核心抗体(IgG) & 弱阳性(±) & 阴性 & \\\\\n[BBOX-251] 6 & TP-Ab & 梅毒螺旋体特异抗体(酶免) & 阴性 & 阴性 & \\\\\n[BBOX-252] 7 & HIV-Ab & 人类免疫缺陷病毒抗体 & 阴性 & 阴性 & \\\\\n[BBOX-253] 8 & HCV-Ab & 丙肝肝炎病毒抗体 & 阴性 & 阴性 & \\\\\n[BBOX-254] \\hline\n[BBOX-255] \\end{tabular}\n[BBOX-256] \\begin{tabular}{lllllllll}\n[BBOX-257] \\hline\n[BBOX-258] No. & 项 & 目 & 英文名称 & 结果 & & 参考值 & 单位 & 检测方法 \\\\\n[BBOX-259] \\hline\n[BBOX-260] 1 & 白细胞计数(8-HR) & & WBC & 11.44 & $\\uparrow$ & 3.5-9.5 & E+09/L & 半导体激光流式细胞术 \\\\\n[BBOX-261] 2 & 淋巴细胞百分率 & & LYMPH\\% & 14.4 & $\\downarrow$ & 20-50 & \\% & 计算法 \\\\\n[BBOX-262] 3 & 单核细胞百分率 & & MONO\\% & 7.4 & & 3-10 & \\% & 计算法 \\\\\n[BBOX-263] 4 & 中性粒细胞百分率 & & NEUT\\% & 73.7 & & 40-75 & \\% & 计算法 \\\\\n[BBOX-264] 5 & 嗜酸性粒细胞百分率 & & E0\\% & 4.2 & & 0.4-8.0 & \\% & 计算法 \\\\\n[BBOX-265] 6 & 嗜碱性粒细胞百分率 & & BASO\\% & 0.3 & & 0-1 & \\% & 计算法 \\\\\n[BBOX-266] 7 & 淋巴细胞绝对值 & & LYMPH\\# & 1.65 & & 1.1-3.2 & E+09/L & 半导体激光流式细胞术 \\\\\n[BBOX-267] 8 & 单核细胞绝对值 & & MONO\\# & 0.85 & $\\uparrow$ & 0.1-0.6 & E+09/L & 半导体激光流式细胞术 \\\\\n[BBOX-268] 9 & 中性粒细胞绝对值 & & NEUT\\# & 8.43 & $\\uparrow$ & 1.8-6.3 & E+09/L & 半导体激光流式细胞术 \\\\\n[BBOX-269] 10 & 嗜酸性粒细胞绝对值 & & E0\\# & 0.48 & & 0.02-0.52 & E+09/L & 半导体激光流式细胞术 \\\\\n[BBOX-270] 11 & 嗜碱性粒细胞绝对值 & & BASO\\# & 0.03 & & 0-0.06 & E+09/L & 半导体激光流式细胞术 \\\\\n[BBOX-271] 12 & 血小板计数(8-HR) & & PLT & 269 & & 125-350 & E+09/L & 鞘流电阻抗法 \\\\\n[BBOX-272] 13 & 血小板分布宽度 & & PDW & 11.3 & $\\downarrow$ & 15.5-18.1 & fL & 计算法 \\\\\n[BBOX-273] 14 & 平均血小板体积 & & MPV & 10.1 & & 9.4-12.5 & fL & 计算法 \\\\\n[BBOX-274] 15 & 大血小板比率 & & P-LCR & 25.3 & & 13-43 & \\% & 计算法 \\\\\n[BBOX-275] 16 & 血小板比积 & & PCT & 0.270 & & 0.11-0.28 & \\% & 计算法 \\\\\n[BBOX-276] 17 & 红细胞计数(8-HR) & & RBC & 4.56 & & 4.3-5.8 & E+12/L & 鞘流电阻抗法 \\\\\n[BBOX-277] 18 & 血红蛋白(8-HR) & & HGB & 148 & & 130-175 & g/L & SLS-血测定法 \\\\\n[BBOX-278] 19 & 红细胞压积(8-HR) & & HCT & 44.8 & & 40-50 & \\% & 鞘流电阻抗法 \\\\\n[BBOX-279] 20 & 平均红细胞体积(8-HR) & & MCV & 98.2 & & 82-100 & fL & 计算法 \\\\\n[BBOX-280] 21 & 平均血红蛋白含量(8-HR) & & MCH & 32.5 & & 27-34 & pg & 计算法 \\\\\n[BBOX-281] 22 & 平均血红蛋白浓度(8-HR) & & MCHC & 330 & & 316-354 & g/L & 计算法 \\\\\n[BBOX-282] 23 & 红细胞分布宽度CV & & RDW\\% & 13.4 & & 10.9-15.4 & \\% & 计算法 \\\\\n[BBOX-283] 24 & 红细胞分布宽度SD & & RDW & 49.0 & $\\uparrow$ & 39-46 & fL & 计算法 \\\\\n[BBOX-284] \\hline\n[BBOX-285] \\end{tabular}\n[BBOX-286] \\begin{tabular}{ccccccc}\n[BBOX-287] \\hline\n[BBOX-288] No. 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n[BBOX-289] \\hline\n[BBOX-290] 1 & 乙肝表面抗原 & HBsAg & 0.00 & (-) & $<$0.03 & IU/mL \\\\\n[BBOX-291] 2 & 乙肝表面抗体 & Anti-HBs & 16.90 & (+) & $<$5.00 & mIU/mL \\\\\n[BBOX-292] 3 & 乙肝e抗原 & HBeAg & 0.00 & (-) & $<$1.00 & C.O.I \\\\\n[BBOX-293] 4 & 乙肝e抗体 & Anti-HBe & 49.60 & (-) & $<$50.00 & Inh\\% \\\\\n[BBOX-294] 5 & 乙肝核心抗体 & Anti-HBc & 4.40 & (+) & $<$1.00 & C.O.I \\\\\n[BBOX-295] 6 & 丙型肝炎抗体 & HCVAb & 0.10 & (-) & $<$1.00 & C.O.I \\\\\n[BBOX-296] 7 & 人免疫缺陷病毒抗原抗体 & HIVAg+Ab & 0.00 & (-) & $<$1.00 & C.O.I \\\\\n[BBOX-297] 8 & 梅毒抗体 & Anti-TP & 0.00 & (-) & $<$1.00 & C.O.I \\\\\n[BBOX-298] \\hline\n[BBOX-299] \\end{tabular}\n[BBOX-300] \\begin{tabular}{ccccccccc}\n[BBOX-301] \\hline\n[BBOX-302] No & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n[BBOX-303] \\hline\n[BBOX-304] 1 & ABO血型鉴定 & & ABO & O型 & & & 微柱凝胶法、微孔板法 \\\\\n[BBOX-305] 2 & RH(D)血型鉴定 & & Rh & 阳性 & & & \\\\\n[BBOX-306] \\hline\n[BBOX-307] \\end{tabular}\n[BBOX-308] \\begin{tabular}{ccccccll}\n[BBOX-309] \\hline\n[BBOX-310] No. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n[BBOX-311] \\hline\n[BBOX-312] 1 & \\multicolumn{2}{l}{游离三碘甲状腺原氨酸(8-HR)} & FT3 & 4.31 & 3.85-6.3 & pmol/L & 电化学发光法 \\\\\n[BBOX-313] 2 & \\multicolumn{2}{l}{游离甲状腺素(8-HR)} & FT4 & 14.90 & 12.8-21.3 & pmol/L & 电化学发光法 \\\\\n[BBOX-314] 3 & \\multicolumn{2}{l}{三碘甲状腺原氨酸(8-HR)} & T3 & 1.81 & 1.3-2.4 & nmol/L & 电化学发光法 \\\\\n[BBOX-315] 4 & \\multicolumn{2}{l}{甲状腺素(8-HR)} & T4 & 102.00 & 70-140 & nmol/L & 电化学发光法 \\\\\n[BBOX-316] 5 & \\multicolumn{2}{l}{促甲状腺素(8-HR)} & TSH & 2.45 & 0.27-4.20 & uIU/mL & 电化学发光法 \\\\\n[BBOX-317] \\hline\n[BBOX-318] \\end{tabular}\n[BBOX-319] \\begin{tabular}{ccccccl}\n[BBOX-320] \\hline\n[BBOX-321] No. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n[BBOX-322] \\hline\n[BBOX-323] 1 & 肌酸激酶同工酶 & & CK-MB & $<$0.22 & 0-2.37 & ng/mL & 化学发光法 \\\\\n[BBOX-324] 2 & 肌钙蛋白I & & cTnI & $<$0.012 & 0-0.034 & ng/mL & 化学发光法 \\\\\n[BBOX-325] 3 & 肌红蛋白 & & MYO & 45.94 & 0-121 & ng/mL & 化学发光法 \\\\\n[BBOX-326] 4 & N端脑利钠肽前体 & & NT-proBNP & $<$20.00 & 健康人群$<$125 & pg/mL & 化学发光法 \\\\\n[BBOX-327] \\hline\n[BBOX-328] \\end{tabular}\n[BBOX-329] \\begin{tabular}{ccccccc}\n[BBOX-330] \\hline\n[BBOX-331] No & 项 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n[BBOX-332] \\hline\n[BBOX-333] 1 & 凝血酶原时间(陕HR) & PT & 11.2 & 9.8-12.1 & sec & 凝固法 \\\\\n[BBOX-334] 2 & 凝血酶原活动度 & PTA & 98.2 & 70-130 & \\% & 凝固法 \\\\\n[BBOX-335] 3 & 国际标准化比值(陕HR) & INR & 0.97 & 0.7-1.3 & & 凝固法 \\\\\n[BBOX-336] 4 & 活化部分凝血活酶时间(陕HR) & APTT & 36.1 & 22.7-31.8 & sec & 凝固法 \\\\\n[BBOX-337] 5 & 纤维蛋白原含量(陕HR) & Fib & 6.680 & 1.8-3.5 & g/L & 凝固法 \\\\\n[BBOX-338] 6 & 凝血酶时间(陕HR) & TT & 15.5 & 14-21 & sec & 凝固法 \\\\\n[BBOX-339] 7 & 纤维蛋白(原)降解产物(定量) & FDP & 4.50 & 0-5 & $\\mu$g/mL & 胶乳免疫比浊法 \\\\\n[BBOX-340] 8 & D-二聚体(定量)(陕HR) & D D & 1.185 & 0-1 & $\\mu$g/mL & 胶乳免疫比浊法 \\\\\n[BBOX-341] \\hline\n[BBOX-342] \\end{tabular}\n[BBOX-343] \\begin{tabular}{llllllll}\n[BBOX-344] \\hline\n[BBOX-345] No. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n[BBOX-346] \\hline\n[BBOX-347] 1 & 血糖(空腹)(8-HR) & & GLU & 5.56 & 3.9-6.1 & mmol/L & 己糖激酶法 \\\\\n[BBOX-348] 2 & 钾(8-HR) & & K & 4.36 & 3.5-5.3 & mmol/L & 间接离子选择电极法 \\\\\n[BBOX-349] 3 & 钠(8-HR) & & Na & 137.8 & 137-147 & mmol/L & 间接离子选择电极法 \\\\\n[BBOX-350] 4 & 氯(8-HR) & & Cl & 100.9 & 99-110 & mmol/L & 间接离子选择电极法 \\\\\n[BBOX-351] 5 & 总蛋白(8-HR) & & TP & 73.0 & 65-85 & g/L & 双缩脲比色法 \\\\\n[BBOX-352] 6 & 白蛋白(8-HR) & & ALB & 42.4 & 40-55 & g/L & 溴甲酚绿法 \\\\\n[BBOX-353] 7 & 球蛋白 & & GLO & 30.6 & 20-40 & g/L & 计算法 \\\\\n[BBOX-354] 8 & 白球比 & & A/G & 1.4 & 1.2-2.4 & & 计算法 \\\\\n[BBOX-355] 9 & 总胆红素(8-HR) & & T-BIL & 12.1 & 0-26 & $\\mu$mol/L & 钒酸盐氧化法 \\\\\n[BBOX-356] 10 & 直接胆红素(8-HR) & & D-BIL & 3.5 & 0-6.8 & $\\mu$mol/L & 钒酸盐氧化法 \\\\\n[BBOX-357] 11 & 间接胆红素 & & I-BIL & 8.6 & 0-14 & $\\mu$mol/L & 计算法 \\\\\n[BBOX-358] 12 & 丙氨酸氨基转移酶(8-HR) & & ALT & 26 & 9-50 & U/L & 紫外-乳酸脱氢酶法 \\\\\n[BBOX-359] 13 & 天门冬氨酸氨基转移酶(8-HR) & & AST & 21 & 15-40 & U/L & 紫外-苹果酸脱氢酶法 \\\\\n[BBOX-360] 14 & AST/ALT & & & 0.81 & & & 计算法 \\\\\n[BBOX-361] 15 & 碱性磷酸酶(8-HR) & & ALP & 106 & 45-125 & U/L & AMP缓冲液法 \\\\\n[BBOX-362] 16 & 总胆汁酸(陕HR) & & TBA & 12.6 & 0-10 & $\\mu$mol/L & 循环酶法 \\\\\n[BBOX-363] 17 & 胆碱酯酶(陕HR) & & CHE & 6970 & 5000-12000 & U/L & 丁酰硫代胆碱/铁氰化钾 \\\\\n[BBOX-364] 18 & $\\gamma$-谷氨酰转移酶(8-HR) & & GGT & 23 & 10-60 & U/L & 速率法 \\\\\n[BBOX-365] 19 & eGFR(CKD-EPI) & & eGFR & 93.12 & >90 & ml/min/1.73m2 & 计算法 \\\\\n[BBOX-366] 20 & 尿酸(8-HR) & & UA & 263.0 & 208-428 & $\\mu$mol/L & 氧化酶法 \\\\\n[BBOX-367] 21 & 尿素(8-HR) & & UREA & 6.7 & 3.1-8.0 & mmol/L & 紫外-谷氨酸脱氢酶法 \\\\\n[BBOX-368] 22 & 肌酐(8-HR) & & CRE & 81.0 & 57-97 & $\\mu$mol/L & 肌氨酸氧化酶法 \\\\\n[BBOX-369] 23 & 肌酸激酶(8-HR) & & CK & 84 & 50-310 & U/L & N-乙酰半胱氨酸法 \\\\\n[BBOX-370] 24 & 肌酸激酶同功酶 & & CK-MB & 12.43 & <25 & U/L & 免疫抑制法 \\\\\n[BBOX-371] 25 & 乳酸脱氢酶(8-HR) & & LDH & 186 & 120-250 & U/L & 乳酸法 \\\\\n[BBOX-372] 26 & $\\alpha$-羟丁酸脱氢酶(陕HR) & & $\\alpha$-HBDH & 140 & 72-182 & U/L & DGKC法 \\\\\n[BBOX-373] 27 & 钙(8-HR) & & Ca & 2.26 & 2.2-2.7 & mmol/L & 偶氮胂III法 \\\\\n[BBOX-374] \\hline\n[BBOX-375] \\end{tabular}"
  }
]
2026-08-10 19:36:03,998 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:36:03.997+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:36:12,559 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:36:12,582 INFO     29 [SmartSplitter] SmartSplitter done: 15 chunks from 15 LLM segments (all bbox_id). Types: {'ExaminationReport': 2, 'LabReport': 11, 'DischargeRecord': 2}
2026-08-10 19:36:12,591 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 19:36:12,591 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks": "15 items, types={'ExaminationReport': 2, 'LabReport': 11, 'DischargeRecord': 2}"}
2026-08-10 19:36:12,591 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 19:36:12,592 INFO     29 [ChunkRouter] Routed 15 chunks into 3 groups: {'chunks_Examination': 2, 'chunks_LabExam': 11, 'chunks_Discharge': 2}
2026-08-10 19:36:12,599 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 19:36:12,599 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | ChunkRouter:Router | outputs={"html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks": "15 items, types={'ExaminationReport': 2, 'LabReport': 11, 'DischargeRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:36:12,599 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 19:36:12,603 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:36:12,604 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:36:12,604 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[1]
2026-08-10 19:36:12,604 INFO     29 [qwen-vl-table] positions ： [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:36:12,789 INFO     29 [qwen-vl-table] page=1, rect=595x842, img=(1653x2339)
2026-08-10 19:36:12,790 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:36:12,791 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 40, \"bbox_end\": 73, \"encounter_dates\": [\"2026-03-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{lllllllll}\n报告时间: 2026-03-04\n\\hline\nNo. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n\\hline\n1 & 血糖(空腹)(8-HR) & & GLU & 5.56 & 3.9-6.1 & mmol/L & 己糖激酶法 \\\\\n2 & 钾(8-HR) & & K & 4.36 & 3.5-5.3 & mmol/L & 间接离子选择电极法 \\\\\n3 & 钠(8-HR) & & Na & 137.8 & 137-147 & mmol/L & 间接离子选择电极法 \\\\\n4 & 氯(8-HR) & & Cl & 100.9 & 99-110 & mmol/L & 间接离子选择电极法 \\\\\n5 & 总蛋白(8-HR) & & TP & 73.0 & 65-85 & g/L & 双缩脲比色法 \\\\\n6 & 白蛋白(8-HR) & & ALB & 42.4 & 40-55 & g/L & 溴甲酚绿法 \\\\\n7 & 球蛋白 & & GLO & 30.6 & 20-40 & g/L & 计算法 \\\\\n8 & 白球比 & & A/G & 1.4 & 1.2-2.4 & & 计算法 \\\\\n9 & 总胆红素(8-HR) & & T-BIL & 12.1 & 0-26 & $\\mu$mol/L & 钒酸盐氧化法 \\\\\n10 & 直接胆红素(8-HR) & & D-BIL & 3.5 & 0-6.8 & $\\mu$mol/L & 钒酸盐氧化法 \\\\\n11 & 间接胆红素 & & I-BIL & 8.6 & 0-14 & $\\mu$mol/L & 计算法 \\\\\n12 & 丙氨酸氨基转移酶(8-HR) & & ALT & 26 & 9-50 & U/L & 紫外-乳酸脱氢酶法 \\\\\n13 & 天门冬氨酸氨基转移酶(8-HR) & & AST & 21 & 15-40 & U/L & 紫外-苹果酸脱氢酶法 \\\\\n14 & AST/ALT & & & 0.81 & & & 计算法 \\\\\n15 & 碱性磷酸酶(8-HR) & & ALP & 106 & 45-125 & U/L & AMP缓冲液法 \\\\\n16 & 总胆汁酸(陕HR) & & TBA & 12.6 & 0-10 & $\\mu$mol/L & 循环酶法 \\\\\n17 & 胆碱酯酶(陕HR) & & CHE & 6970 & 5000-12000 & U/L & 丁酰硫代胆碱/铁氰化钾 \\\\\n18 & $\\gamma$-谷氨酰转移酶(8-HR) & & GGT & 23 & 10-60 & U/L & 速率法 \\\\\n19 & eGFR(CKD-EPI) & & eGFR & 93.12 & >90 & ml/min/1.73m2 & 计算法 \\\\\n20 & 尿酸(8-HR) & & UA & 263.0 & 208-428 & $\\mu$mol/L & 氧化酶法 \\\\\n21 & 尿素(8-HR) & & UREA & 6.7 & 3.1-8.0 & mmol/L & 紫外-谷氨酸脱氢酶法 \\\\\n22 & 肌酐(8-HR) & & CRE & 81.0 & 57-97 & $\\mu$mol/L & 肌氨酸氧化酶法 \\\\\n23 & 肌酸激酶(8-HR) & & CK & 84 & 50-310 & U/L & N-乙酰半胱氨酸法 \\\\\n24 & 肌酸激酶同功酶 & & CK-MB & 12.43 & <25 & U/L & 免疫抑制法 \\\\\n25 & 乳酸脱氢酶(8-HR) & & LDH & 186 & 120-250 & U/L & 乳酸法 \\\\\n26 & $\\alpha$-羟丁酸脱氢酶(陕HR) & & $\\alpha$-HBDH & 140 & 72-182 & U/L & DGKC法 \\\\\n27 & 钙(8-HR) & & Ca & 2.26 & 2.2-2.7 & mmol/L & 偶氮胂III法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:36:36,242 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:36:36.240+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:37:02,768 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:37:02,768 INFO     29 [qwen-vl-table] page=1 LLM output (len=4642):
{
  "report_date": "2026-03-04",
  "items": [
    {
      "name": "血糖(空腹)(8-HR)",
      "item_code": "GLU",
      "value": "5.56",
      "unit": "mmol/L",
      "reference_range": "3.9-6.1",
      "abnormal": false
    },
    {
      "name": "钾(8-HR)",
      "item_code": "K",
      "value": "4.36",
      "unit": "mmol/L",
      "reference_range": "3.5-5.3",
      "abnormal": false
    },
    {
      "name": "钠(8-HR)",
      "item_code": "Na",
      "value": "137.8",
      "unit": "mmol/L",
      "reference_range": "137-147",
      "abnormal": false
    },
    {
      "name": "氯(8-HR)",
      "item_code": "Cl",
      "value": "100.9",
      "unit": "mmol/L",
      "reference_range": "99-110",
      "abnormal": false
    },
    {
      "name": "总蛋白(8-HR)",
      "item_code": "TP",
      "value": "73.0",
      "unit": "g/L",
      "reference_range": "65-85",
      "abnormal": false
    },
    {
      "name": "白蛋白(8-HR)",
      "item_code": "ALB",
      "value": "42.4",
      "unit": "g/L",
      "reference_range": "40-55",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLO",
      "value": "30.6",
      "unit": "g/L",
      "reference_range": "20-40",
      "abnormal": false
    },
    {
      "name": "白球比",
      "item_code": "A/G",
      "value": "1.4",
      "unit": null,
      "reference_range": "1.2-2.4",
      "abnormal": false
    },
    {
      "name": "总胆红素(8-HR)",
      "item_code": "T-BIL",
      "value": "12.1",
      "unit": "μmol/L",
      "reference_range": "0-26",
      "abnormal": false
    },
    {
      "name": "直接胆红素(8-HR)",
      "item_code": "D-BIL",
      "value": "3.5",
      "unit": "μmol/L",
      "reference_range": "0-6.8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "I-BIL",
      "value": "8.6",
      "unit": "μmol/L",
      "reference_range": "0-14",
      "abnormal": false
    },
    {
      "name": "丙氨酸氨基转移酶(8-HR)",
      "item_code": "ALT",
      "value": "26",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "天门冬氨酸氨基转移酶(8-HR)",
      "item_code": "AST",
      "value": "21",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "AST/ALT",
      "item_code": null,
      "value": "0.81",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶(8-HR)",
      "item_code": "ALP",
      "value": "106",
      "unit": "U/L",
      "reference_range": "45-125",
      "abnormal": false
    },
    {
      "name": "总胆汁酸(陕HR)",
      "item_code": "TBA",
      "value": "12.6",
      "unit": "μmol/L",
      "reference_range": "0-10",
      "abnormal": true
    },
    {
      "name": "胆碱酯酶(陕HR)",
      "item_code": "CHE",
      "value": "6970",
      "unit": "U/L",
      "reference_range": "5000-12000",
      "abnormal": false
    },
    {
      "name": "γ-谷氨酰转移酶(8-HR)",
      "item_code": "GGT",
      "value": "23",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": false
    },
    {
      "name": "eGFR(CKD-EPI)",
      "item_code": "eGFR",
      "value": "93.12",
      "unit": "ml/min/1.73m2",
      "reference_range": ">90",
      "abnormal": false
    },
    {
      "name": "尿酸(8-HR)",
      "item_code": "UA",
      "value": "263.0",
      "unit": "μmol/L",
      "reference_range": "208-428",
      "abnormal": false
    },
    {
      "name": "尿素(8-HR)",
      "item_code": "UREA",
      "value": "6.7",
      "unit": "mmol/L",
      "reference_range": "3.1-8.0",
      "abnormal": false
    },
    {
      "name": "肌酐(8-HR)",
      "item_code": "CRE",
      "value": "81.0",
      "unit": "μmol/L",
      "reference_range": "57-97",
      "abnormal": false
    },
    {
      "name": "肌酸激酶(8-HR)",
      "item_code": "CK",
      "value": "84",
      "unit": "U/L",
      "reference_range": "50-310",
      "abnormal": false
    },
    {
      "name": "肌酸激酶同功酶",
      "item_code": "CK-MB",
      "value": "12.43",
      "unit": "U/L",
      "reference_range": "<25",
      "abnormal": false
    },
    {
      "name": "乳酸脱氢酶(8-HR)",
      "item_code": "LDH",
      "value": "186",
      "unit": "U/L",
      "reference_range": "120-250",
      "abnormal": false
    },
    {
      "name": "α-羟丁酸脱氢酶(陕HR)",
      "item_code": "α-HBDH",
      "value": "140",
      "unit": "U/L",
      "reference_range": "72-182",
      "abnormal": false
    },
    {
      "name": "钙(8-HR)",
      "item_code": "Ca",
      "value": "2.26",
      "unit": "mmol/L",
      "reference_range": "2.2-2.7",
      "abnormal": false
    }
  ]
}
2026-08-10 19:37:02,769 INFO     29 [qwen-vl-table] coord grouping: {1: 27}
2026-08-10 19:37:02,774 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2023200, prompt_len=781
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
血糖(空腹)(8-HR)、钾(8-HR)、钠(8-HR)、氯(8-HR)、总蛋白(8-HR)、白蛋白(8-HR)、球蛋白、白球比、总胆红素(8-HR)、直接胆红素(8-HR)、间接胆红素、丙氨酸氨基转移酶(8-HR)、天门冬氨酸氨基转移酶(8-HR)、AST/ALT、碱性磷酸酶(8-HR)、总胆汁酸(陕HR)、胆碱酯酶(陕HR)、γ-谷氨酰转移酶(8-HR)、eGFR(CKD-EPI)、尿酸(8-HR)、尿素(8-HR)、肌酐(8-HR)、肌酸激酶(8-HR)、肌酸激酶同功酶、乳酸脱氢酶(8-HR)、α-羟丁酸脱氢酶(陕HR)、钙(8-HR)

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
2026-08-10 19:37:12,892 INFO     29 [qwen-vl-table] coord API raw response (len=1448):
[
	{"text": "血糖(空腹)(8-HR)", "bbox": [62, 212, 204, 228]},
	{"text": "钾(8-HR)", "bbox": [64, 229, 134, 244]},
	{"text": "钠(8-HR)", "bbox": [66, 245, 136, 260]},
	{"text": "氯(8-HR)", "bbox": [67, 261, 138, 276]},
	{"text": "总蛋白(8-HR)", "bbox": [71, 278, 175, 293]},
	{"text": "白蛋白(8-HR)", "bbox": [74, 294, 177, 309]},
	{"text": "球蛋白", "bbox": [77, 310, 130, 324]},
	{"text": "白球比", "bbox": [80, 326, 133, 340]},
	{"text": "总胆红素(8-HR)", "bbox": [84, 341, 201, 355]},
	{"text": "直接胆红素(8-HR)", "bbox": [86, 356, 220, 370]},
	{"text": "间接胆红素", "bbox": [77, 370, 175, 384]},
	{"text": "丙氨酸氨基转移酶(8-HR)", "bbox": [90, 384, 275, 398]},
	{"text": "天门冬氨酸氨基转移酶(8-HR)", "bbox": [92, 398, 310, 412]},
	{"text": "AST/ALT", "bbox": [82, 409, 160, 422]},
	{"text": "碱性磷酸酶(8-HR)", "bbox": [95, 422, 232, 435]},
	{"text": "总胆汁酸(陕HR)", "bbox": [100, 435, 219, 447]},
	{"text": "胆碱酯酶(陕HR)", "bbox": [100, 447, 220, 459]},
	{"text": "γ-谷氨酰转移酶(8-HR)", "bbox": [95, 459, 279, 471]},
	{"text": "eGFR(CKD-EPI)", "bbox": [98, 470, 219, 482]},
	{"text": "尿酸(8-HR)", "bbox": [100, 481, 199, 493]},
	{"text": "尿素(8-HR)", "bbox": [102, 492, 201, 504]},
	{"text": "肌酐(8-HR)", "bbox": [104, 503, 203, 515]},
	{"text": "肌酸激酶(8-HR)", "bbox": [107, 515, 235, 527]},
	{"text": "肌酸激酶同功酶", "bbox": [109, 527, 238, 539]},
	{"text": "乳酸脱氢酶(8-HR)", "bbox": [110, 539, 250, 551]},
	{"text": "α-羟丁酸脱氢酶(陕HR)", "bbox": [110, 551, 285, 564]},
	{"text": "钙(8-HR)", "bbox": [107, 564, 188, 576]}
]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord API: raw_items=27, valid_items=27, elapsed=10.1s
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[0]: text=血糖(空腹)(8-HR), bbox=[62, 212, 204, 228]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[1]: text=钾(8-HR), bbox=[64, 229, 134, 244]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[2]: text=钠(8-HR), bbox=[66, 245, 136, 260]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[3]: text=氯(8-HR), bbox=[67, 261, 138, 276]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[4]: text=总蛋白(8-HR), bbox=[71, 278, 175, 293]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[5]: text=白蛋白(8-HR), bbox=[74, 294, 177, 309]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[6]: text=球蛋白, bbox=[77, 310, 130, 324]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[7]: text=白球比, bbox=[80, 326, 133, 340]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[8]: text=总胆红素(8-HR), bbox=[84, 341, 201, 355]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[9]: text=直接胆红素(8-HR), bbox=[86, 356, 220, 370]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[10]: text=间接胆红素, bbox=[77, 370, 175, 384]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[11]: text=丙氨酸氨基转移酶(8-HR), bbox=[90, 384, 275, 398]
2026-08-10 19:37:12,893 INFO     29 [qwen-vl-table] coord item[12]: text=天门冬氨酸氨基转移酶(8-HR), bbox=[92, 398, 310, 412]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[13]: text=AST/ALT, bbox=[82, 409, 160, 422]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[14]: text=碱性磷酸酶(8-HR), bbox=[95, 422, 232, 435]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[15]: text=总胆汁酸(陕HR), bbox=[100, 435, 219, 447]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[16]: text=胆碱酯酶(陕HR), bbox=[100, 447, 220, 459]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[17]: text=γ-谷氨酰转移酶(8-HR), bbox=[95, 459, 279, 471]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[18]: text=eGFR(CKD-EPI), bbox=[98, 470, 219, 482]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[19]: text=尿酸(8-HR), bbox=[100, 481, 199, 493]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[20]: text=尿素(8-HR), bbox=[102, 492, 201, 504]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[21]: text=肌酐(8-HR), bbox=[104, 503, 203, 515]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[22]: text=肌酸激酶(8-HR), bbox=[107, 515, 235, 527]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[23]: text=肌酸激酶同功酶, bbox=[109, 527, 238, 539]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[24]: text=乳酸脱氢酶(8-HR), bbox=[110, 539, 250, 551]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[25]: text=α-羟丁酸脱氢酶(陕HR), bbox=[110, 551, 285, 564]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] coord item[26]: text=钙(8-HR), bbox=[107, 564, 188, 576]
2026-08-10 19:37:12,894 INFO     29 [qwen-vl-table] page=1 coord: matched 27/27, time=10.1s
2026-08-10 19:37:12,895 INFO     29 [qwen-vl-table] new_positions (27):
[[2, 36.89, 121.38, 178.504, 191.976], [2, 38.08, 79.72999999999999, 192.81799999999998, 205.44799999999998], [2, 39.269999999999996, 80.92, 206.29, 218.92], [2, 39.864999999999995, 82.11, 219.762, 232.392], [2, 42.245, 104.125, 234.076, 246.706], [2, 44.03, 105.315, 247.548, 260.178], [2, 45.815, 77.35, 261.02, 272.808], [2, 47.599999999999994, 79.13499999999999, 274.492, 286.28], [2, 49.98, 119.595, 287.122, 298.90999999999997], [2, 51.169999999999995, 130.9, 299.752, 311.53999999999996], [2, 45.815, 104.125, 311.53999999999996, 323.328], [2, 53.55, 163.625, 323.328, 335.116], [2, 54.739999999999995, 184.45, 335.116, 346.904], [2, 48.79, 95.19999999999999, 344.378, 355.324], [2, 56.525, 138.04, 355.324, 366.27], [2, 59.5, 130.305, 366.27, 376.37399999999997], [2, 59.5, 130.9, 376.37399999999997, 386.478], [2, 56.525, 166.005, 386.478, 396.582], [2, 58.309999999999995, 130.305, 395.74, 405.844], [2, 59.5, 118.405, 405.002, 415.106], [2, 60.69, 119.595, 414.264, 424.368], [2, 61.879999999999995, 120.785, 423.526, 433.63], [2, 63.665, 139.825, 433.63, 443.734], [2, 64.855, 141.60999999999999, 443.734, 453.83799999999997], [2, 65.45, 148.75, 453.83799999999997, 463.942], [2, 65.45, 169.575, 463.942, 474.888], [2, 63.665, 111.86, 474.888, 484.99199999999996]]
2026-08-10 19:37:12,895 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=27, matched=27, pages=1, time=60.3s
2026-08-10 19:37:12,896 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:37:12,899 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:37:12,899 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 19:37:12,899 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:37:13,090 INFO     29 [qwen-vl-table] page=5, rect=595x842, img=(1653x2339)
2026-08-10 19:37:13,091 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:37:13,091 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 177, \"bbox_end\": 219, \"encounter_dates\": [\"2026-02-23\"], \"department\": \"肿瘤科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-02-23\n\\hline\n\\multicolumn{8}{c}{\\textbf{联勤保障部队第九八九医院检验报告单}} \\\\\n\\multicolumn{4}{l}{迈琪7500} & \\multicolumn{4}{r}{住院} \\\\\n\\hline\n\\textbf{姓} & : & \\textbf{性} & 别:男 & \\textbf{年} & 龄:55岁 & \\textbf{标本编号:}56 & \\\\\n\\textbf{ID} & :J.2015101 & \\textbf{费} & 别:自费 & \\textbf{诊} & 断:肺肿物 & \\textbf{标本种类:}静脉血 & \\\\\n\\textbf{科} & 室:肿瘤科病区 & \\textbf{床} & 号:30 & \\textbf{备} & 注: & & \\\\\n\\hline\n\\textbf{NO} & \\textbf{代号} & \\textbf{名称} & \\textbf{结果} & \\textbf{参考值} & \\textbf{单位} & & \\\\\n\\hline\n1 & WBC & 白细胞计数 & 9.63 & ↑ 3.5-9.5 & 10⁹/L & & \\\\\n2 & RBC & 红细胞计数 & 4.36 & 4.3-5.8 & 10¹²/L & & \\\\\n3 & HGB & 血红蛋白 & 141 & 130-175 & g/L & & \\\\\n4 & HCT & 红细胞比积 & 42.7 & 40-50 & \\% & & \\\\\n5 & MCV & 平均红细胞体积 & 97.9 & 82-100 & fL & & \\\\\n6 & MCH & 平均血红蛋白量 & 32.4 & 27-34 & pg & & \\\\\n7 & MCHC & 平均血红蛋白浓度 & 330.0 & 316-354 & g/L & & \\\\\n8 & PLT & 血小板计数 & 268 & 100-350 & 10⁹/L & & \\\\\n9 & LYMPH\\% & 淋巴细胞比例 & 15.3 & ↓ 20-50 & \\% & & \\\\\n10 & MONO\\% & 单核细胞比例 & 6.1 & 3-10 & \\% & & \\\\\n11 & NEUT\\% & 中性粒细胞比例 & 71.5 & 40-75 & \\% & & \\\\\n12 & E0\\% & 嗜酸性细胞比例 & 6.7 & 0.4-8 & \\% & & \\\\\n13 & BASO\\% & 嗜碱性细胞比例 & 0.4 & 0-1 & \\% & & \\\\\n14 & LYMPH\\# & 淋巴细胞计数 & 1.47 & 1.1-3.2 & 10⁹/L & & \\\\\n15 & MONO\\# & 单核细胞计数 & 0.6 & 0.1-0.6 & 10⁹/L & & \\\\\n16 & NEUT\\# & 中性粒细胞计数 & 6.88 & ↑ 1.8-6.3 & 10⁹/L & & \\\\\n17 & E0\\# & 嗜酸性细胞计数 & 0.65 & ↑ 0.02-0.62 & 10⁹/L & & \\\\\n18 & BASO\\# & 嗜碱性细胞计数 & 0.04 & 0-0.06 & 10⁹/L & & \\\\\n19 & RDW-CV & 红细胞分布宽度CV & 14.0 & 11-15.5 & \\% & & \\\\\n20 & RDW-SD & 红细胞分布宽度SD & 49.5 & 37-50 & fL & & \\\\\n21 & PCT & 血小板压积 & 0.28 & 0.11-0.28 & & & \\\\\n\\hline\n\\textbf{NO} & \\textbf{代号} & \\textbf{名称} & \\textbf{结果} & \\textbf{参考值} & \\textbf{单位} & & \\\\\n\\hline\n22 & MPV & 平均血小板体积 & 10.4 & 6-13 & fL & & \\\\\n23 & PDW & 血小板分布宽度 & 16.4 & 9-17 & fL & & \\\\\n24 & P-LCR & 大血小板比例 & 28.6 & 13-43 & \\% & & \\\\\n25 & IGM & 幼稚粒细胞绝对值 & 0.01 & 0-0.06 & 10⁹/L & & \\\\\n26 & IGC & 幼稚粒细胞百分比 & 0.10 & 0-0.6 & \\% & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:37:13,093 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:37:13.092+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:37:45,390 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:37:45.389+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:37:53,342 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:37:53,342 INFO     29 [qwen-vl-table] page=5 LLM output (len=4392):
{
  "report_date": "2026-02-23",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "9.63",
      "unit": "10⁹/L",
      "reference_range": "3.5-9.5",
      "abnormal": true
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "4.36",
      "unit": "10¹²/L",
      "reference_range": "4.3-5.8",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "141",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": false
    },
    {
      "name": "红细胞比积",
      "item_code": "HCT",
      "value": "42.7",
      "unit": "%",
      "reference_range": "40-50",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "97.9",
      "unit": "fL",
      "reference_range": "82-100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": "MCH",
      "value": "32.4",
      "unit": "pg",
      "reference_range": "27-34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": "MCHC",
      "value": "330.0",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "268",
      "unit": "10⁹/L",
      "reference_range": "100-350",
      "abnormal": false
    },
    {
      "name": "淋巴细胞比例",
      "item_code": "LYMPH%",
      "value": "15.3",
      "unit": "%",
      "reference_range": "20-50",
      "abnormal": true
    },
    {
      "name": "单核细胞比例",
      "item_code": "MONO%",
      "value": "6.1",
      "unit": "%",
      "reference_range": "3-10",
      "abnormal": false
    },
    {
      "name": "中性粒细胞比例",
      "item_code": "NEUT%",
      "value": "71.5",
      "unit": "%",
      "reference_range": "40-75",
      "abnormal": false
    },
    {
      "name": "嗜酸性细胞比例",
      "item_code": "E0%",
      "value": "6.7",
      "unit": "%",
      "reference_range": "0.4-8",
      "abnormal": false
    },
    {
      "name": "嗜碱性细胞比例",
      "item_code": "BASO%",
      "value": "0.4",
      "unit": "%",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "淋巴细胞计数",
      "item_code": "LYMPH#",
      "value": "1.47",
      "unit": "10⁹/L",
      "reference_range": "1.1-3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞计数",
      "item_code": "MONO#",
      "value": "0.6",
      "unit": "10⁹/L",
      "reference_range": "0.1-0.6",
      "abnormal": false
    },
    {
      "name": "中性粒细胞计数",
      "item_code": "NEUT#",
      "value": "6.88",
      "unit": "10⁹/L",
      "reference_range": "1.8-6.3",
      "abnormal": true
    },
    {
      "name": "嗜酸性细胞计数",
      "item_code": "E0#",
      "value": "0.65",
      "unit": "10⁹/L",
      "reference_range": "0.02-0.62",
      "abnormal": true
    },
    {
      "name": "嗜碱性细胞计数",
      "item_code": "BASO#",
      "value": "0.04",
      "unit": "10⁹/L",
      "reference_range": "0-0.06",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度CV",
      "item_code": "RDW-CV",
      "value": "14.0",
      "unit": "%",
      "reference_range": "11-15.5",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度SD",
      "item_code": "RDW-SD",
      "value": "49.5",
      "unit": "fL",
      "reference_range": "37-50",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.28",
      "unit": null,
      "reference_range": "0.11-0.28",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "10.4",
      "unit": "fL",
      "reference_range": "6-13",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "16.4",
      "unit": "fL",
      "reference_range": "9-17",
      "abnormal": false
    },
    {
      "name": "大血小板比例",
      "item_code": "P-LCR",
      "value": "28.6",
      "unit": "%",
      "reference_range": "13-43",
      "abnormal": false
    },
    {
      "name": "幼稚粒细胞绝对值",
      "item_code": "IGM",
      "value": "0.01",
      "unit": "10⁹/L",
      "reference_range": "0-0.06",
      "abnormal": false
    },
    {
      "name": "幼稚粒细胞百分比",
      "item_code": "IGC",
      "value": "0.10",
      "unit": "%",
      "reference_range": "0-0.6",
      "abnormal": false
    }
  ]
}
2026-08-10 19:37:53,343 INFO     29 [qwen-vl-table] coord grouping: {5: 26}
2026-08-10 19:37:53,344 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1061186, prompt_len=703
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、红细胞计数、血红蛋白、红细胞比积、平均红细胞体积、平均血红蛋白量、平均血红蛋白浓度、血小板计数、淋巴细胞比例、单核细胞比例、中性粒细胞比例、嗜酸性细胞比例、嗜碱性细胞比例、淋巴细胞计数、单核细胞计数、中性粒细胞计数、嗜酸性细胞计数、嗜碱性细胞计数、红细胞分布宽度CV、红细胞分布宽度SD、血小板压积、平均血小板体积、血小板分布宽度、大血小板比例、幼稚粒细胞绝对值、幼稚粒细胞百分比

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
2026-08-10 19:38:00,610 INFO     29 [qwen-vl-table] coord API raw response (len=1343):
[
	{"text": "白细胞计数", "bbox": [145, 114, 217, 125]},
	{"text": "红细胞计数", "bbox": [145, 129, 217, 140]},
	{"text": "血红蛋白", "bbox": [145, 143, 202, 154]},
	{"text": "红细胞比积", "bbox": [145, 157, 217, 168]},
	{"text": "平均红细胞体积", "bbox": [145, 171, 246, 182]},
	{"text": "平均血红蛋白量", "bbox": [145, 186, 246, 197]},
	{"text": "平均血红蛋白浓度", "bbox": [145, 200, 261, 211]},
	{"text": "血小板计数", "bbox": [145, 214, 217, 225]},
	{"text": "淋巴细胞比例", "bbox": [145, 228, 231, 239]},
	{"text": "单核细胞比例", "bbox": [145, 242, 231, 253]},
	{"text": "中性粒细胞比例", "bbox": [145, 256, 246, 267]},
	{"text": "嗜酸性细胞比例", "bbox": [145, 270, 246, 281]},
	{"text": "嗜碱性细胞比例", "bbox": [145, 284, 246, 295]},
	{"text": "淋巴细胞计数", "bbox": [145, 298, 231, 309]},
	{"text": "单核细胞计数", "bbox": [145, 312, 231, 323]},
	{"text": "中性粒细胞计数", "bbox": [145, 326, 246, 337]},
	{"text": "嗜酸性细胞计数", "bbox": [145, 340, 246, 351]},
	{"text": "嗜碱性细胞计数", "bbox": [145, 355, 246, 366]},
	{"text": "红细胞分布宽度CV", "bbox": [145, 369, 261, 380]},
	{"text": "红细胞分布宽度SD", "bbox": [145, 383, 261, 394]},
	{"text": "血小板压积", "bbox": [145, 397, 217, 408]},
	{"text": "平均血小板体积", "bbox": [585, 114, 685, 125]},
	{"text": "血小板分布宽度", "bbox": [585, 129, 685, 140]},
	{"text": "大血小板比例", "bbox": [585, 143, 669, 154]},
	{"text": "幼稚粒细胞绝对值", "bbox": [585, 157, 699, 168]},
	{"text": "幼稚粒细胞百分比", "bbox": [585, 171, 699, 182]}
]
2026-08-10 19:38:00,610 INFO     29 [qwen-vl-table] coord API: raw_items=26, valid_items=26, elapsed=7.3s
2026-08-10 19:38:00,610 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[145, 114, 217, 125]
2026-08-10 19:38:00,610 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞计数, bbox=[145, 129, 217, 140]
2026-08-10 19:38:00,610 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白, bbox=[145, 143, 202, 154]
2026-08-10 19:38:00,610 INFO     29 [qwen-vl-table] coord item[3]: text=红细胞比积, bbox=[145, 157, 217, 168]
2026-08-10 19:38:00,610 INFO     29 [qwen-vl-table] coord item[4]: text=平均红细胞体积, bbox=[145, 171, 246, 182]
2026-08-10 19:38:00,610 INFO     29 [qwen-vl-table] coord item[5]: text=平均血红蛋白量, bbox=[145, 186, 246, 197]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[6]: text=平均血红蛋白浓度, bbox=[145, 200, 261, 211]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[7]: text=血小板计数, bbox=[145, 214, 217, 225]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[8]: text=淋巴细胞比例, bbox=[145, 228, 231, 239]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[9]: text=单核细胞比例, bbox=[145, 242, 231, 253]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[10]: text=中性粒细胞比例, bbox=[145, 256, 246, 267]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[11]: text=嗜酸性细胞比例, bbox=[145, 270, 246, 281]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[12]: text=嗜碱性细胞比例, bbox=[145, 284, 246, 295]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[13]: text=淋巴细胞计数, bbox=[145, 298, 231, 309]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[14]: text=单核细胞计数, bbox=[145, 312, 231, 323]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[15]: text=中性粒细胞计数, bbox=[145, 326, 246, 337]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[16]: text=嗜酸性细胞计数, bbox=[145, 340, 246, 351]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[17]: text=嗜碱性细胞计数, bbox=[145, 355, 246, 366]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度CV, bbox=[145, 369, 261, 380]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[19]: text=红细胞分布宽度SD, bbox=[145, 383, 261, 394]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[20]: text=血小板压积, bbox=[145, 397, 217, 408]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[21]: text=平均血小板体积, bbox=[585, 114, 685, 125]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[22]: text=血小板分布宽度, bbox=[585, 129, 685, 140]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[23]: text=大血小板比例, bbox=[585, 143, 669, 154]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[24]: text=幼稚粒细胞绝对值, bbox=[585, 157, 699, 168]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] coord item[25]: text=幼稚粒细胞百分比, bbox=[585, 171, 699, 182]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] page=5 coord: matched 26/26, time=7.3s
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] new_positions (26):
[[6, 86.27499999999999, 129.11499999999998, 95.988, 105.25], [6, 86.27499999999999, 129.11499999999998, 108.618, 117.88], [6, 86.27499999999999, 120.19, 120.40599999999999, 129.668], [6, 86.27499999999999, 129.11499999999998, 132.194, 141.456], [6, 86.27499999999999, 146.37, 143.982, 153.244], [6, 86.27499999999999, 146.37, 156.612, 165.874], [6, 86.27499999999999, 155.295, 168.4, 177.662], [6, 86.27499999999999, 129.11499999999998, 180.188, 189.45], [6, 86.27499999999999, 137.445, 191.976, 201.238], [6, 86.27499999999999, 137.445, 203.76399999999998, 213.02599999999998], [6, 86.27499999999999, 146.37, 215.552, 224.814], [6, 86.27499999999999, 146.37, 227.34, 236.602], [6, 86.27499999999999, 146.37, 239.128, 248.39], [6, 86.27499999999999, 137.445, 250.916, 260.178], [6, 86.27499999999999, 137.445, 262.704, 271.966], [6, 86.27499999999999, 146.37, 274.492, 283.75399999999996], [6, 86.27499999999999, 146.37, 286.28, 295.542], [6, 86.27499999999999, 146.37, 298.90999999999997, 308.17199999999997], [6, 86.27499999999999, 155.295, 310.698, 319.96], [6, 86.27499999999999, 155.295, 322.486, 331.748], [6, 86.27499999999999, 129.11499999999998, 334.274, 343.536], [6, 348.075, 407.575, 95.988, 105.25], [6, 348.075, 407.575, 108.618, 117.88], [6, 348.075, 398.055, 120.40599999999999, 129.668], [6, 348.075, 415.905, 132.194, 141.456], [6, 348.075, 415.905, 143.982, 153.244]]
2026-08-10 19:38:00,611 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=26, matched=26, pages=1, time=47.7s
2026-08-10 19:38:00,612 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:38:00,613 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:38:00,613 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 19:38:00,613 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:38:00,803 INFO     29 [qwen-vl-table] page=5, rect=595x842, img=(1653x2339)
2026-08-10 19:38:00,803 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:38:00,803 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 220, \"bbox_end\": 240, \"encounter_dates\": [\"2026-02-23\"], \"department\": \"肿瘤科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-02-23\n\\hline\n\\multicolumn{8}{c}{\\textbf{联勤保障部队第九八九医院检验报告单}} \\\\\n\\multicolumn{4}{l}{血凝Denting-1} & \\multicolumn{4}{r}{住院} \\\\\n\\hline\n\\textbf{姓} & : & \\textbf{性} & 别:男 & \\textbf{年} & 龄:55岁 & \\textbf{标本编号:}20 & \\\\\n\\textbf{ID} & :J.2015101 & \\textbf{费} & 别:自费 & \\textbf{诊} & 断:肺肿物 & \\textbf{标本种类:}静脉血 & \\\\\n\\textbf{科} & 室:肿瘤科病区 & \\textbf{床} & 号:30 & \\textbf{备} & 注: & & \\\\\n\\hline\n\\textbf{No} & \\textbf{项目代号} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{参考范围} & \\textbf{单位} & & \\\\\n\\hline\n1 & PT-1 & 凝血酶原时间 & 10.4 & 9.2-13.9 & SEC & & \\\\\n2 & PIR-1 & PT报告活动度 & 117 & 70-130 & \\% & & \\\\\n3 & INR & 国际标准化比值（INR） & 0.88 & 0.8-1.2 & & & \\\\\n4 & APTT-1 & 活化部分凝血活酶时间(APTT) & 33.3 & 21.2-35.7 & soc & & \\\\\n5 & FIB & 纤维蛋白原 & 3.7 & 2-4 & g/L & & \\\\\n6 & TT-1 & 凝血酶时间 & 14.8 & 10.2-20.1 & soc & & \\\\\n7 & D-DIMER-1 & D-二聚体 & 446 & 0-550 & ug/L & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:38:15,511 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:38:15,511 INFO     29 [qwen-vl-table] page=5 LLM output (len=1239):
{
  "report_date": "2026-02-23",
  "items": [
    {
      "name": "凝血酶原时间",
      "item_code": "PT-1",
      "value": "10.4",
      "unit": "SEC",
      "reference_range": "9.2-13.9",
      "abnormal": false
    },
    {
      "name": "PT报告活动度",
      "item_code": "PIR-1",
      "value": "117",
      "unit": "%",
      "reference_range": "70-130",
      "abnormal": false
    },
    {
      "name": "国际标准化比值（INR）",
      "item_code": "INR",
      "value": "0.88",
      "unit": null,
      "reference_range": "0.8-1.2",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间(APTT)",
      "item_code": "APTT-1",
      "value": "33.3",
      "unit": "sec",
      "reference_range": "21.2-35.7",
      "abnormal": false
    },
    {
      "name": "纤维蛋白原",
      "item_code": "FIB",
      "value": "3.7",
      "unit": "g/L",
      "reference_range": "2-4",
      "abnormal": false
    },
    {
      "name": "凝血酶时间",
      "item_code": "TT-1",
      "value": "14.8",
      "unit": "sec",
      "reference_range": "10.2-20.1",
      "abnormal": false
    },
    {
      "name": "D-二聚体",
      "item_code": "D-DIMER-1",
      "value": "446",
      "unit": "ug/L",
      "reference_range": "0-550",
      "abnormal": false
    }
  ]
}
2026-08-10 19:38:15,511 INFO     29 [qwen-vl-table] coord grouping: {5: 7}
2026-08-10 19:38:15,515 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1061186, prompt_len=569
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间、PT报告活动度、国际标准化比值（INR）、活化部分凝血活酶时间(APTT)、纤维蛋白原、凝血酶时间、D-二聚体

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
2026-08-10 19:38:17,651 INFO     29 [qwen-vl-table] coord API raw response (len=385):
```json
[
	{"text": "凝血酶原时间", "bbox": [203, 570, 290, 583]},
	{"text": "PT报告活动度", "bbox": [203, 587, 290, 600]},
	{"text": "国际标准化比值（INR）", "bbox": [203, 604, 347, 617]},
	{"text": "活化部分凝血活酶时间(APTT)", "bbox": [203, 621, 387, 634]},
	{"text": "纤维蛋白原", "bbox": [203, 638, 276, 651]},
	{"text": "凝血酶时间", "bbox": [203, 655, 276, 668]},
	{"text": "D-二聚体", "bbox": [203, 672, 262, 685]}
]
```
2026-08-10 19:38:17,651 INFO     29 [qwen-vl-table] coord API: raw_items=7, valid_items=7, elapsed=2.1s
2026-08-10 19:38:17,652 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[203, 570, 290, 583]
2026-08-10 19:38:17,652 INFO     29 [qwen-vl-table] coord item[1]: text=PT报告活动度, bbox=[203, 587, 290, 600]
2026-08-10 19:38:17,652 INFO     29 [qwen-vl-table] coord item[2]: text=国际标准化比值（INR）, bbox=[203, 604, 347, 617]
2026-08-10 19:38:17,652 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间(APTT), bbox=[203, 621, 387, 634]
2026-08-10 19:38:17,652 INFO     29 [qwen-vl-table] coord item[4]: text=纤维蛋白原, bbox=[203, 638, 276, 651]
2026-08-10 19:38:17,652 INFO     29 [qwen-vl-table] coord item[5]: text=凝血酶时间, bbox=[203, 655, 276, 668]
2026-08-10 19:38:17,652 INFO     29 [qwen-vl-table] coord item[6]: text=D-二聚体, bbox=[203, 672, 262, 685]
2026-08-10 19:38:17,652 INFO     29 [qwen-vl-table] page=5 coord: matched 7/7, time=2.1s
2026-08-10 19:38:17,653 INFO     29 [qwen-vl-table] new_positions (7):
[[6, 120.785, 172.54999999999998, 479.94, 490.88599999999997], [6, 120.785, 172.54999999999998, 494.25399999999996, 505.2], [6, 120.785, 206.465, 508.568, 519.514], [6, 120.785, 230.265, 522.882, 533.828], [6, 120.785, 164.22, 537.196, 548.1419999999999], [6, 120.785, 164.22, 551.51, 562.456], [6, 120.785, 155.89, 565.824, 576.77]]
2026-08-10 19:38:17,653 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=7, matched=7, pages=1, time=17.0s
2026-08-10 19:38:17,654 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:38:17,656 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:38:17,656 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[6]
2026-08-10 19:38:17,656 INFO     29 [qwen-vl-table] positions ： [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:38:17,823 INFO     29 [qwen-vl-table] page=6, rect=842x595, img=(2339x1653)
2026-08-10 19:38:17,823 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:38:17,824 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 241, \"bbox_end\": 255, \"encounter_dates\": [\"2026-02-23\"], \"department\": \"肿瘤科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllll}\n报告时间: 2026-02-23\n\\hline\nNo & 项目代号 & 项目名称 & 结果 & 参考范围 & 单位 \\\\\n\\hline\n1 & HBsAg & 乙肝肝炎病毒表面抗原 & 阴性 & 阴性 & \\\\\n2 & HBsAb & 乙肝肝炎病毒表面抗体 & 阳性(+) & 阴性-阳性 & \\\\\n3 & HBeAg & 乙肝肝炎病毒e抗原 & 阴性 & 阴性 & \\\\\n4 & HBeAb & 乙肝肝炎病毒e抗体 & 阴性 & 阴性 & \\\\\n5 & HBcAb & 乙肝肝炎病毒核心抗体(IgG) & 弱阳性(±) & 阴性 & \\\\\n6 & TP-Ab & 梅毒螺旋体特异抗体(酶免) & 阴性 & 阴性 & \\\\\n7 & HIV-Ab & 人类免疫缺陷病毒抗体 & 阴性 & 阴性 & \\\\\n8 & HCV-Ab & 丙肝肝炎病毒抗体 & 阴性 & 阴性 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:38:17,826 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:38:17.825+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:38:29,316 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:38:29,316 INFO     29 [qwen-vl-table] page=6 LLM output (len=1385):
{
  "report_date": "2026-02-23",
  "items": [
    {
      "name": "乙肝肝炎病毒表面抗原",
      "item_code": "HBsAg",
      "value": "阴性",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "乙肝肝炎病毒表面抗体",
      "item_code": "HBsAb",
      "value": "阳性(+)",
      "unit": null,
      "reference_range": "阴性-阳性",
      "abnormal": false
    },
    {
      "name": "乙肝肝炎病毒e抗原",
      "item_code": "HBeAg",
      "value": "阴性",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "乙肝肝炎病毒e抗体",
      "item_code": "HBeAb",
      "value": "阴性",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "乙肝肝炎病毒核心抗体(IgG)",
      "item_code": "HBcAb",
      "value": "弱阳性(±)",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": true
    },
    {
      "name": "梅毒螺旋体特异抗体(酶免)",
      "item_code": "TP-Ab",
      "value": "阴性",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "人类免疫缺陷病毒抗体",
      "item_code": "HIV-Ab",
      "value": "阴性",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "丙肝肝炎病毒抗体",
      "item_code": "HCV-Ab",
      "value": "阴性",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    }
  ]
}
2026-08-10 19:38:29,316 INFO     29 [qwen-vl-table] coord grouping: {6: 8}
2026-08-10 19:38:29,319 INFO     29 [qwen-vl-table] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=583062, prompt_len=598
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
乙肝肝炎病毒表面抗原、乙肝肝炎病毒表面抗体、乙肝肝炎病毒e抗原、乙肝肝炎病毒e抗体、乙肝肝炎病毒核心抗体(IgG)、梅毒螺旋体特异抗体(酶免)、人类免疫缺陷病毒抗体、丙肝肝炎病毒抗体

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
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord API raw response (len=446):
[
	{"text": "乙肝肝炎病毒表面抗原", "bbox": [239, 195, 363, 211]},
	{"text": "乙肝肝炎病毒表面抗体", "bbox": [239, 222, 363, 238]},
	{"text": "乙肝肝炎病毒e抗原", "bbox": [239, 250, 344, 266]},
	{"text": "乙肝肝炎病毒e抗体", "bbox": [239, 276, 344, 292]},
	{"text": "乙肝肝炎病毒核心抗体(IgG)", "bbox": [239, 304, 391, 320]},
	{"text": "梅毒螺旋体特异抗体(酶免)", "bbox": [239, 331, 385, 347]},
	{"text": "人类免疫缺陷病毒抗体", "bbox": [239, 358, 363, 374]},
	{"text": "丙肝肝炎病毒抗体", "bbox": [239, 385, 339, 401]}
]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=3.1s
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord item[0]: text=乙肝肝炎病毒表面抗原, bbox=[239, 195, 363, 211]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord item[1]: text=乙肝肝炎病毒表面抗体, bbox=[239, 222, 363, 238]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord item[2]: text=乙肝肝炎病毒e抗原, bbox=[239, 250, 344, 266]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord item[3]: text=乙肝肝炎病毒e抗体, bbox=[239, 276, 344, 292]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord item[4]: text=乙肝肝炎病毒核心抗体(IgG), bbox=[239, 304, 391, 320]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord item[5]: text=梅毒螺旋体特异抗体(酶免), bbox=[239, 331, 385, 347]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord item[6]: text=人类免疫缺陷病毒抗体, bbox=[239, 358, 363, 374]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] coord item[7]: text=丙肝肝炎病毒抗体, bbox=[239, 385, 339, 401]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] page=6 coord: matched 8/8, time=3.1s
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] new_positions (8):
[[7, 201.238, 305.646, 116.02499999999999, 125.54499999999999], [7, 201.238, 305.646, 132.09, 141.60999999999999], [7, 201.238, 289.64799999999997, 148.75, 158.26999999999998], [7, 201.238, 289.64799999999997, 164.22, 173.73999999999998], [7, 201.238, 329.222, 180.88, 190.39999999999998], [7, 201.238, 324.17, 196.945, 206.465], [7, 201.238, 305.646, 213.01, 222.53], [7, 201.238, 285.438, 229.075, 238.595]]
2026-08-10 19:38:32,444 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=8, matched=8, pages=1, time=14.8s
2026-08-10 19:38:32,445 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:38:32,446 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:38:32,446 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[7]
2026-08-10 19:38:32,446 INFO     29 [qwen-vl-table] positions ： [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:38:32,623 INFO     29 [qwen-vl-table] page=7, rect=842x595, img=(2339x1653)
2026-08-10 19:38:32,624 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:38:32,624 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 256, \"bbox_end\": 285, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{lllllllll}\n\\hline\nNo. & 项 & 目 & 英文名称 & 结果 & & 参考值 & 单位 & 检测方法 \\\\\n\\hline\n1 & 白细胞计数(8-HR) & & WBC & 11.44 & $\\uparrow$ & 3.5-9.5 & E+09/L & 半导体激光流式细胞术 \\\\\n2 & 淋巴细胞百分率 & & LYMPH\\% & 14.4 & $\\downarrow$ & 20-50 & \\% & 计算法 \\\\\n3 & 单核细胞百分率 & & MONO\\% & 7.4 & & 3-10 & \\% & 计算法 \\\\\n4 & 中性粒细胞百分率 & & NEUT\\% & 73.7 & & 40-75 & \\% & 计算法 \\\\\n5 & 嗜酸性粒细胞百分率 & & E0\\% & 4.2 & & 0.4-8.0 & \\% & 计算法 \\\\\n6 & 嗜碱性粒细胞百分率 & & BASO\\% & 0.3 & & 0-1 & \\% & 计算法 \\\\\n7 & 淋巴细胞绝对值 & & LYMPH\\# & 1.65 & & 1.1-3.2 & E+09/L & 半导体激光流式细胞术 \\\\\n8 & 单核细胞绝对值 & & MONO\\# & 0.85 & $\\uparrow$ & 0.1-0.6 & E+09/L & 半导体激光流式细胞术 \\\\\n9 & 中性粒细胞绝对值 & & NEUT\\# & 8.43 & $\\uparrow$ & 1.8-6.3 & E+09/L & 半导体激光流式细胞术 \\\\\n10 & 嗜酸性粒细胞绝对值 & & E0\\# & 0.48 & & 0.02-0.52 & E+09/L & 半导体激光流式细胞术 \\\\\n11 & 嗜碱性粒细胞绝对值 & & BASO\\# & 0.03 & & 0-0.06 & E+09/L & 半导体激光流式细胞术 \\\\\n12 & 血小板计数(8-HR) & & PLT & 269 & & 125-350 & E+09/L & 鞘流电阻抗法 \\\\\n13 & 血小板分布宽度 & & PDW & 11.3 & $\\downarrow$ & 15.5-18.1 & fL & 计算法 \\\\\n14 & 平均血小板体积 & & MPV & 10.1 & & 9.4-12.5 & fL & 计算法 \\\\\n15 & 大血小板比率 & & P-LCR & 25.3 & & 13-43 & \\% & 计算法 \\\\\n16 & 血小板比积 & & PCT & 0.270 & & 0.11-0.28 & \\% & 计算法 \\\\\n17 & 红细胞计数(8-HR) & & RBC & 4.56 & & 4.3-5.8 & E+12/L & 鞘流电阻抗法 \\\\\n18 & 血红蛋白(8-HR) & & HGB & 148 & & 130-175 & g/L & SLS-血测定法 \\\\\n19 & 红细胞压积(8-HR) & & HCT & 44.8 & & 40-50 & \\% & 鞘流电阻抗法 \\\\\n20 & 平均红细胞体积(8-HR) & & MCV & 98.2 & & 82-100 & fL & 计算法 \\\\\n21 & 平均血红蛋白含量(8-HR) & & MCH & 32.5 & & 27-34 & pg & 计算法 \\\\\n22 & 平均血红蛋白浓度(8-HR) & & MCHC & 330 & & 316-354 & g/L & 计算法 \\\\\n23 & 红细胞分布宽度CV & & RDW\\% & 13.4 & & 10.9-15.4 & \\% & 计算法 \\\\\n24 & 红细胞分布宽度SD & & RDW & 49.0 & $\\uparrow$ & 39-46 & fL & 计算法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:38:50,176 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:38:50.174+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:39:11,281 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:11,281 INFO     29 [qwen-vl-table] page=7 LLM output (len=4125):
{
  "report_date": null,
  "items": [
    {
      "name": "白细胞计数(8-HR)",
      "item_code": "WBC",
      "value": "11.44",
      "unit": "E+09/L",
      "reference_range": "3.5-9.5",
      "abnormal": true
    },
    {
      "name": "淋巴细胞百分率",
      "item_code": "LYMPH%",
      "value": "14.4",
      "unit": "%",
      "reference_range": "20-50",
      "abnormal": true
    },
    {
      "name": "单核细胞百分率",
      "item_code": "MONO%",
      "value": "7.4",
      "unit": "%",
      "reference_range": "3-10",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分率",
      "item_code": "NEUT%",
      "value": "73.7",
      "unit": "%",
      "reference_range": "40-75",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分率",
      "item_code": "E0%",
      "value": "4.2",
      "unit": "%",
      "reference_range": "0.4-8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分率",
      "item_code": "BASO%",
      "value": "0.3",
      "unit": "%",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LYMPH#",
      "value": "1.65",
      "unit": "E+09/L",
      "reference_range": "1.1-3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MONO#",
      "value": "0.85",
      "unit": "E+09/L",
      "reference_range": "0.1-0.6",
      "abnormal": true
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NEUT#",
      "value": "8.43",
      "unit": "E+09/L",
      "reference_range": "1.8-6.3",
      "abnormal": true
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": "E0#",
      "value": "0.48",
      "unit": "E+09/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": "BASO#",
      "value": "0.03",
      "unit": "E+09/L",
      "reference_range": "0-0.06",
      "abnormal": false
    },
    {
      "name": "血小板计数(8-HR)",
      "item_code": "PLT",
      "value": "269",
      "unit": "E+09/L",
      "reference_range": "125-350",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "11.3",
      "unit": "fL",
      "reference_range": "15.5-18.1",
      "abnormal": true
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "10.1",
      "unit": "fL",
      "reference_range": "9.4-12.5",
      "abnormal": false
    },
    {
      "name": "大血小板比率",
      "item_code": "P-LCR",
      "value": "25.3",
      "unit": "%",
      "reference_range": "13-43",
      "abnormal": false
    },
    {
      "name": "血小板比积",
      "item_code": "PCT",
      "value": "0.270",
      "unit": "%",
      "reference_range": "0.11-0.28",
      "abnormal": false
    },
    {
      "name": "红细胞计数(8-HR)",
      "item_code": "RBC",
      "value": "4.56",
      "unit": "E+12/L",
      "reference_range": "4.3-5.8",
      "abnormal": false
    },
    {
      "name": "血红蛋白(8-HR)",
      "item_code": "HGB",
      "value": "148",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": false
    },
    {
      "name": "红细胞压积(8-HR)",
      "item_code": "HCT",
      "value": "44.8",
      "unit": "%",
      "reference_range": "40-50",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积(8-HR)",
      "item_code": "MCV",
      "value": "98.2",
      "unit": "fL",
      "reference_range": "82-100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白含量(8-HR)",
      "item_code": "MCH",
      "value": "32.5",
      "unit": "pg",
      "reference_range": "27-34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度(8-HR)",
      "item_code": "MCHC",
      "value": "330",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度CV",
      "item_code": "RDW%",
      "value": "13.4",
      "unit": "%",
      "reference_range": "10.9-15.4",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度SD",
      "item_code": "RDW",
      "value": "49.0",
      "unit": "fL",
      "reference_range": "39-46",
      "abnormal": true
    }
  ]
}
2026-08-10 19:39:11,282 INFO     29 [qwen-vl-table] coord grouping: {7: 24}
2026-08-10 19:39:11,283 INFO     29 [qwen-vl-table] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=916144, prompt_len=748
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数(8-HR)、淋巴细胞百分率、单核细胞百分率、中性粒细胞百分率、嗜酸性粒细胞百分率、嗜碱性粒细胞百分率、淋巴细胞绝对值、单核细胞绝对值、中性粒细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、血小板计数(8-HR)、血小板分布宽度、平均血小板体积、大血小板比率、血小板比积、红细胞计数(8-HR)、血红蛋白(8-HR)、红细胞压积(8-HR)、平均红细胞体积(8-HR)、平均血红蛋白含量(8-HR)、平均血红蛋白浓度(8-HR)、红细胞分布宽度CV、红细胞分布宽度SD

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
2026-08-10 19:39:20,724 INFO     29 [qwen-vl-table] coord API raw response (len=1300):
[
	{"text": "白细胞计数(8-HR)", "bbox": [209, 218, 304, 236]},
	{"text": "淋巴细胞百分率", "bbox": [209, 242, 293, 260]},
	{"text": "单核细胞百分率", "bbox": [209, 266, 293, 284]},
	{"text": "中性粒细胞百分率", "bbox": [209, 290, 304, 308]},
	{"text": "嗜酸性粒细胞百分率", "bbox": [209, 314, 316, 332]},
	{"text": "嗜碱性粒细胞百分率", "bbox": [209, 338, 316, 356]},
	{"text": "淋巴细胞绝对值", "bbox": [209, 362, 293, 380]},
	{"text": "单核细胞绝对值", "bbox": [209, 386, 293, 404]},
	{"text": "中性粒细胞绝对值", "bbox": [209, 410, 304, 428]},
	{"text": "嗜酸性粒细胞绝对值", "bbox": [209, 434, 316, 452]},
	{"text": "嗜碱性粒细胞绝对值", "bbox": [209, 458, 316, 476]},
	{"text": "血小板计数(8-HR)", "bbox": [209, 482, 304, 500]},
	{"text": "血小板分布宽度", "bbox": [209, 506, 293, 524]},
	{"text": "平均血小板体积", "bbox": [209, 530, 293, 548]},
	{"text": "大血小板比率", "bbox": [209, 554, 281, 572]},
	{"text": "血小板比积", "bbox": [209, 578, 269, 596]},
	{"text": "红细胞计数(8-HR)", "bbox": [209, 603, 304, 621]},
	{"text": "血红蛋白(8-HR)", "bbox": [209, 627, 291, 645]},
	{"text": "红细胞压积(8-HR)", "bbox": [209, 651, 304, 669]},
	{"text": "平均红细胞体积(8-HR)", "bbox": [209, 675, 327, 693]},
	{"text": "平均血红蛋白含量(8-HR)", "bbox": [209, 700, 340, 718]},
	{"text": "平均血红蛋白浓度(8-HR)", "bbox": [209, 724, 340, 742]},
	{"text": "红细胞分布宽度CV", "bbox": [209, 748, 304, 766]},
	{"text": "红细胞分布宽度SD", "bbox": [209, 772, 304, 790]}
]
2026-08-10 19:39:20,724 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=9.4s
2026-08-10 19:39:20,724 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数(8-HR), bbox=[209, 218, 304, 236]
2026-08-10 19:39:20,724 INFO     29 [qwen-vl-table] coord item[1]: text=淋巴细胞百分率, bbox=[209, 242, 293, 260]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[2]: text=单核细胞百分率, bbox=[209, 266, 293, 284]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[3]: text=中性粒细胞百分率, bbox=[209, 290, 304, 308]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞百分率, bbox=[209, 314, 316, 332]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞百分率, bbox=[209, 338, 316, 356]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[6]: text=淋巴细胞绝对值, bbox=[209, 362, 293, 380]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[7]: text=单核细胞绝对值, bbox=[209, 386, 293, 404]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[8]: text=中性粒细胞绝对值, bbox=[209, 410, 304, 428]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞绝对值, bbox=[209, 434, 316, 452]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞绝对值, bbox=[209, 458, 316, 476]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[11]: text=血小板计数(8-HR), bbox=[209, 482, 304, 500]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[12]: text=血小板分布宽度, bbox=[209, 506, 293, 524]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[13]: text=平均血小板体积, bbox=[209, 530, 293, 548]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[14]: text=大血小板比率, bbox=[209, 554, 281, 572]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[15]: text=血小板比积, bbox=[209, 578, 269, 596]
2026-08-10 19:39:20,725 INFO     29 [qwen-vl-table] coord item[16]: text=红细胞计数(8-HR), bbox=[209, 603, 304, 621]
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] coord item[17]: text=血红蛋白(8-HR), bbox=[209, 627, 291, 645]
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞压积(8-HR), bbox=[209, 651, 304, 669]
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] coord item[19]: text=平均红细胞体积(8-HR), bbox=[209, 675, 327, 693]
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] coord item[20]: text=平均血红蛋白含量(8-HR), bbox=[209, 700, 340, 718]
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] coord item[21]: text=平均血红蛋白浓度(8-HR), bbox=[209, 724, 340, 742]
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] coord item[22]: text=红细胞分布宽度CV, bbox=[209, 748, 304, 766]
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] coord item[23]: text=红细胞分布宽度SD, bbox=[209, 772, 304, 790]
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] page=7 coord: matched 24/24, time=9.4s
2026-08-10 19:39:20,726 INFO     29 [qwen-vl-table] new_positions (24):
[[8, 175.97799999999998, 255.968, 129.71, 140.42], [8, 175.97799999999998, 246.706, 143.98999999999998, 154.7], [8, 175.97799999999998, 246.706, 158.26999999999998, 168.98], [8, 175.97799999999998, 255.968, 172.54999999999998, 183.26], [8, 175.97799999999998, 266.072, 186.82999999999998, 197.54], [8, 175.97799999999998, 266.072, 201.10999999999999, 211.82], [8, 175.97799999999998, 246.706, 215.39, 226.1], [8, 175.97799999999998, 246.706, 229.67, 240.38], [8, 175.97799999999998, 255.968, 243.95, 254.66], [8, 175.97799999999998, 266.072, 258.22999999999996, 268.94], [8, 175.97799999999998, 266.072, 272.51, 283.21999999999997], [8, 175.97799999999998, 255.968, 286.78999999999996, 297.5], [8, 175.97799999999998, 246.706, 301.07, 311.78], [8, 175.97799999999998, 246.706, 315.34999999999997, 326.06], [8, 175.97799999999998, 236.602, 329.63, 340.34], [8, 175.97799999999998, 226.498, 343.90999999999997, 354.62], [8, 175.97799999999998, 255.968, 358.78499999999997, 369.495], [8, 175.97799999999998, 245.022, 373.065, 383.775], [8, 175.97799999999998, 255.968, 387.34499999999997, 398.055], [8, 175.97799999999998, 275.334, 401.625, 412.335], [8, 175.97799999999998, 286.28, 416.5, 427.21], [8, 175.97799999999998, 286.28, 430.78, 441.48999999999995], [8, 175.97799999999998, 255.968, 445.06, 455.77], [8, 175.97799999999998, 255.968, 459.34, 470.04999999999995]]
2026-08-10 19:39:20,727 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=24, matched=24, pages=1, time=48.3s
2026-08-10 19:39:20,728 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:39:20,730 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:39:20,730 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[8]
2026-08-10 19:39:20,731 INFO     29 [qwen-vl-table] positions ： [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:39:20,886 INFO     29 [qwen-vl-table] page=8, rect=842x595, img=(2339x1653)
2026-08-10 19:39:20,886 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:20,887 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 286, \"bbox_end\": 299, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n\\hline\nNo. 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n\\hline\n1 & 乙肝表面抗原 & HBsAg & 0.00 & (-) & $<$0.03 & IU/mL \\\\\n2 & 乙肝表面抗体 & Anti-HBs & 16.90 & (+) & $<$5.00 & mIU/mL \\\\\n3 & 乙肝e抗原 & HBeAg & 0.00 & (-) & $<$1.00 & C.O.I \\\\\n4 & 乙肝e抗体 & Anti-HBe & 49.60 & (-) & $<$50.00 & Inh\\% \\\\\n5 & 乙肝核心抗体 & Anti-HBc & 4.40 & (+) & $<$1.00 & C.O.I \\\\\n6 & 丙型肝炎抗体 & HCVAb & 0.10 & (-) & $<$1.00 & C.O.I \\\\\n7 & 人免疫缺陷病毒抗原抗体 & HIVAg+Ab & 0.00 & (-) & $<$1.00 & C.O.I \\\\\n8 & 梅毒抗体 & Anti-TP & 0.00 & (-) & $<$1.00 & C.O.I \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:39:22,482 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:39:22.479+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:39:33,810 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:33,810 INFO     29 [qwen-vl-table] page=8 LLM output (len=1410):
{
  "report_date": null,
  "items": [
    {
      "name": "乙肝表面抗原",
      "item_code": "HBsAg",
      "value": "0.00",
      "unit": "IU/mL",
      "reference_range": "<0.03",
      "abnormal": false
    },
    {
      "name": "乙肝表面抗体",
      "item_code": "Anti-HBs",
      "value": "16.90",
      "unit": "mIU/mL",
      "reference_range": "<5.00",
      "abnormal": true
    },
    {
      "name": "乙肝e抗原",
      "item_code": "HBeAg",
      "value": "0.00",
      "unit": "C.O.I",
      "reference_range": "<1.00",
      "abnormal": false
    },
    {
      "name": "乙肝e抗体",
      "item_code": "Anti-HBe",
      "value": "49.60",
      "unit": "Inh%",
      "reference_range": "<50.00",
      "abnormal": false
    },
    {
      "name": "乙肝核心抗体",
      "item_code": "Anti-HBc",
      "value": "4.40",
      "unit": "C.O.I",
      "reference_range": "<1.00",
      "abnormal": true
    },
    {
      "name": "丙型肝炎抗体",
      "item_code": "HCVAb",
      "value": "0.10",
      "unit": "C.O.I",
      "reference_range": "<1.00",
      "abnormal": false
    },
    {
      "name": "人免疫缺陷病毒抗原抗体",
      "item_code": "HIVAg+Ab",
      "value": "0.00",
      "unit": "C.O.I",
      "reference_range": "<1.00",
      "abnormal": false
    },
    {
      "name": "梅毒抗体",
      "item_code": "Anti-TP",
      "value": "0.00",
      "unit": "C.O.I",
      "reference_range": "<1.00",
      "abnormal": false
    }
  ]
}
2026-08-10 19:39:33,810 INFO     29 [qwen-vl-table] coord grouping: {8: 8}
2026-08-10 19:39:33,811 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=636528, prompt_len=563
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
乙肝表面抗原、乙肝表面抗体、乙肝e抗原、乙肝e抗体、乙肝核心抗体、丙型肝炎抗体、人免疫缺陷病毒抗原抗体、梅毒抗体

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
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord API raw response (len=411):
[
	{"text": "乙肝表面抗原", "bbox": [105, 389, 203, 411]},
	{"text": "乙肝表面抗体", "bbox": [105, 418, 203, 440]},
	{"text": "乙肝e抗原", "bbox": [105, 448, 178, 470]},
	{"text": "乙肝e抗体", "bbox": [105, 478, 178, 500]},
	{"text": "乙肝核心抗体", "bbox": [105, 508, 203, 530]},
	{"text": "丙型肝炎抗体", "bbox": [105, 538, 203, 560]},
	{"text": "人免疫缺陷病毒抗原抗体", "bbox": [105, 568, 287, 590]},
	{"text": "梅毒抗体", "bbox": [105, 598, 170, 620]}
]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=3.0s
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord item[0]: text=乙肝表面抗原, bbox=[105, 389, 203, 411]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord item[1]: text=乙肝表面抗体, bbox=[105, 418, 203, 440]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord item[2]: text=乙肝e抗原, bbox=[105, 448, 178, 470]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord item[3]: text=乙肝e抗体, bbox=[105, 478, 178, 500]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord item[4]: text=乙肝核心抗体, bbox=[105, 508, 203, 530]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord item[5]: text=丙型肝炎抗体, bbox=[105, 538, 203, 560]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord item[6]: text=人免疫缺陷病毒抗原抗体, bbox=[105, 568, 287, 590]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] coord item[7]: text=梅毒抗体, bbox=[105, 598, 170, 620]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] page=8 coord: matched 8/8, time=3.0s
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] new_positions (8):
[[9, 88.41, 170.926, 231.45499999999998, 244.545], [9, 88.41, 170.926, 248.70999999999998, 261.8], [9, 88.41, 149.876, 266.56, 279.65], [9, 88.41, 149.876, 284.40999999999997, 297.5], [9, 88.41, 170.926, 302.26, 315.34999999999997], [9, 88.41, 170.926, 320.11, 333.2], [9, 88.41, 241.654, 337.96, 351.05], [9, 88.41, 143.14, 355.81, 368.9]]
2026-08-10 19:39:36,809 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=8, matched=8, pages=1, time=16.1s
2026-08-10 19:39:36,810 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:39:36,811 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:39:36,811 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-10 19:39:36,811 INFO     29 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:39:36,935 INFO     29 [qwen-vl-table] page=9, rect=842x595, img=(2339x1653)
2026-08-10 19:39:36,936 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:36,937 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 300, \"bbox_end\": 307, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n\\hline\nNo & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n\\hline\n1 & ABO血型鉴定 & & ABO & O型 & & & 微柱凝胶法、微孔板法 \\\\\n2 & RH(D)血型鉴定 & & Rh & 阳性 & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:39:40,520 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:40,520 INFO     29 [qwen-vl-table] page=9 LLM output (len=363):
{
  "report_date": null,
  "items": [
    {
      "name": "ABO血型鉴定",
      "item_code": "ABO",
      "value": "O型",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "RH(D)血型鉴定",
      "item_code": "Rh",
      "value": "阳性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 19:39:40,520 INFO     29 [qwen-vl-table] coord grouping: {9: 2}
2026-08-10 19:39:40,521 INFO     29 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=388683, prompt_len=524
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
ABO血型鉴定、RH(D)血型鉴定

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
2026-08-10 19:39:42,242 INFO     29 [qwen-vl-table] coord API raw response (len=120):
```json
[
	{"text": "ABO血型鉴定", "bbox": [109, 306, 202, 329]},
	{"text": "RH(D)血型鉴定", "bbox": [109, 331, 218, 354]}
]
```
2026-08-10 19:39:42,243 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=1.7s
2026-08-10 19:39:42,243 INFO     29 [qwen-vl-table] coord item[0]: text=ABO血型鉴定, bbox=[109, 306, 202, 329]
2026-08-10 19:39:42,243 INFO     29 [qwen-vl-table] coord item[1]: text=RH(D)血型鉴定, bbox=[109, 331, 218, 354]
2026-08-10 19:39:42,243 INFO     29 [qwen-vl-table] page=9 coord: matched 2/2, time=1.7s
2026-08-10 19:39:42,244 INFO     29 [qwen-vl-table] new_positions (2):
[[10, 91.77799999999999, 170.084, 182.07, 195.755], [10, 91.77799999999999, 183.55599999999998, 196.945, 210.63]]
2026-08-10 19:39:42,244 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=5.4s
2026-08-10 19:39:42,245 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:39:42,255 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:39:42,255 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[10]
2026-08-10 19:39:42,255 INFO     29 [qwen-vl-table] positions ： [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:39:42,392 INFO     29 [qwen-vl-table] page=10, rect=842x595, img=(2339x1653)
2026-08-10 19:39:42,392 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:42,393 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 308, \"bbox_end\": 318, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccll}\n\\hline\nNo. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n\\hline\n1 & \\multicolumn{2}{l}{游离三碘甲状腺原氨酸(8-HR)} & FT3 & 4.31 & 3.85-6.3 & pmol/L & 电化学发光法 \\\\\n2 & \\multicolumn{2}{l}{游离甲状腺素(8-HR)} & FT4 & 14.90 & 12.8-21.3 & pmol/L & 电化学发光法 \\\\\n3 & \\multicolumn{2}{l}{三碘甲状腺原氨酸(8-HR)} & T3 & 1.81 & 1.3-2.4 & nmol/L & 电化学发光法 \\\\\n4 & \\multicolumn{2}{l}{甲状腺素(8-HR)} & T4 & 102.00 & 70-140 & nmol/L & 电化学发光法 \\\\\n5 & \\multicolumn{2}{l}{促甲状腺素(8-HR)} & TSH & 2.45 & 0.27-4.20 & uIU/mL & 电化学发光法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:39:53,985 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:53,985 INFO     29 [qwen-vl-table] page=10 LLM output (len=930):
{
  "report_date": null,
  "items": [
    {
      "name": "游离三碘甲状腺原氨酸(8-HR)",
      "item_code": "FT3",
      "value": "4.31",
      "unit": "pmol/L",
      "reference_range": "3.85-6.3",
      "abnormal": false
    },
    {
      "name": "游离甲状腺素(8-HR)",
      "item_code": "FT4",
      "value": "14.90",
      "unit": "pmol/L",
      "reference_range": "12.8-21.3",
      "abnormal": false
    },
    {
      "name": "三碘甲状腺原氨酸(8-HR)",
      "item_code": "T3",
      "value": "1.81",
      "unit": "nmol/L",
      "reference_range": "1.3-2.4",
      "abnormal": false
    },
    {
      "name": "甲状腺素(8-HR)",
      "item_code": "T4",
      "value": "102.00",
      "unit": "nmol/L",
      "reference_range": "70-140",
      "abnormal": false
    },
    {
      "name": "促甲状腺素(8-HR)",
      "item_code": "TSH",
      "value": "2.45",
      "unit": "uIU/mL",
      "reference_range": "0.27-4.20",
      "abnormal": false
    }
  ]
}
2026-08-10 19:39:53,985 INFO     29 [qwen-vl-table] coord grouping: {10: 5}
2026-08-10 19:39:53,988 INFO     29 [qwen-vl-table] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=553930, prompt_len=574
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
游离三碘甲状腺原氨酸(8-HR)、游离甲状腺素(8-HR)、三碘甲状腺原氨酸(8-HR)、甲状腺素(8-HR)、促甲状腺素(8-HR)

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
2026-08-10 19:39:56,438 INFO     29 [qwen-vl-table] coord API raw response (len=285):
[
	{"text": "游离三碘甲状腺原氨酸(8-HR)", "bbox": [98, 380, 308, 403]},
	{"text": "游离甲状腺素(8-HR)", "bbox": [98, 410, 241, 433]},
	{"text": "三碘甲状腺原氨酸(8-HR)", "bbox": [98, 441, 275, 464]},
	{"text": "甲状腺素(8-HR)", "bbox": [98, 472, 208, 495]},
	{"text": "促甲状腺素(8-HR)", "bbox": [98, 503, 224, 526]}
]
2026-08-10 19:39:56,438 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=2.4s
2026-08-10 19:39:56,439 INFO     29 [qwen-vl-table] coord item[0]: text=游离三碘甲状腺原氨酸(8-HR), bbox=[98, 380, 308, 403]
2026-08-10 19:39:56,439 INFO     29 [qwen-vl-table] coord item[1]: text=游离甲状腺素(8-HR), bbox=[98, 410, 241, 433]
2026-08-10 19:39:56,439 INFO     29 [qwen-vl-table] coord item[2]: text=三碘甲状腺原氨酸(8-HR), bbox=[98, 441, 275, 464]
2026-08-10 19:39:56,439 INFO     29 [qwen-vl-table] coord item[3]: text=甲状腺素(8-HR), bbox=[98, 472, 208, 495]
2026-08-10 19:39:56,439 INFO     29 [qwen-vl-table] coord item[4]: text=促甲状腺素(8-HR), bbox=[98, 503, 224, 526]
2026-08-10 19:39:56,439 INFO     29 [qwen-vl-table] page=10 coord: matched 5/5, time=2.4s
2026-08-10 19:39:56,440 INFO     29 [qwen-vl-table] new_positions (5):
[[11, 82.51599999999999, 259.336, 226.1, 239.785], [11, 82.51599999999999, 202.922, 243.95, 257.635], [11, 82.51599999999999, 231.54999999999998, 262.395, 276.08], [11, 82.51599999999999, 175.136, 280.84, 294.525], [11, 82.51599999999999, 188.608, 299.28499999999997, 312.96999999999997]]
2026-08-10 19:39:56,440 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=5, matched=5, pages=1, time=14.2s
2026-08-10 19:39:56,441 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:39:56,443 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:39:56,443 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[11]
2026-08-10 19:39:56,444 INFO     29 [qwen-vl-table] positions ： [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:39:56,581 INFO     29 [qwen-vl-table] page=11, rect=842x595, img=(2339x1653)
2026-08-10 19:39:56,581 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:56,582 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 319, \"bbox_end\": 328, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccl}\n\\hline\nNo. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n\\hline\n1 & 肌酸激酶同工酶 & & CK-MB & $<$0.22 & 0-2.37 & ng/mL & 化学发光法 \\\\\n2 & 肌钙蛋白I & & cTnI & $<$0.012 & 0-0.034 & ng/mL & 化学发光法 \\\\\n3 & 肌红蛋白 & & MYO & 45.94 & 0-121 & ng/mL & 化学发光法 \\\\\n4 & N端脑利钠肽前体 & & NT-proBNP & $<$20.00 & 健康人群$<$125 & pg/mL & 化学发光法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:39:56,583 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:39:56.583+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:39:59,210 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:39:59,210 INFO     29 [qwen-vl-table] page=11 LLM output (len=731):
{
  "report_date": null,
  "items": [
    {
      "name": "肌酸激酶同工酶",
      "item_code": "CK-MB",
      "value": "<0.22",
      "unit": "ng/mL",
      "reference_range": "0-2.37",
      "abnormal": false
    },
    {
      "name": "肌钙蛋白I",
      "item_code": "cTnI",
      "value": "<0.012",
      "unit": "ng/mL",
      "reference_range": "0-0.034",
      "abnormal": false
    },
    {
      "name": "肌红蛋白",
      "item_code": "MYO",
      "value": "45.94",
      "unit": "ng/mL",
      "reference_range": "0-121",
      "abnormal": false
    },
    {
      "name": "N端脑利钠肽前体",
      "item_code": "NT-proBNP",
      "value": "<20.00",
      "unit": "pg/mL",
      "reference_range": "健康人群<125",
      "abnormal": false
    }
  ]
}
2026-08-10 19:39:59,210 INFO     29 [qwen-vl-table] coord grouping: {11: 4}
2026-08-10 19:39:59,211 INFO     29 [qwen-vl-table] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=551443, prompt_len=534
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
肌酸激酶同工酶、肌钙蛋白I、肌红蛋白、N端脑利钠肽前体

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
2026-08-10 19:40:01,292 INFO     29 [qwen-vl-table] coord API raw response (len=206):
[
	{"text": "肌酸激酶同工酶", "bbox": [104, 387, 222, 411]},
	{"text": "肌钙蛋白I", "bbox": [104, 420, 180, 444]},
	{"text": "肌红蛋白", "bbox": [104, 453, 171, 477]},
	{"text": "N端脑利钠肽前体", "bbox": [104, 486, 228, 510]}
]
2026-08-10 19:40:01,293 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=2.1s
2026-08-10 19:40:01,293 INFO     29 [qwen-vl-table] coord item[0]: text=肌酸激酶同工酶, bbox=[104, 387, 222, 411]
2026-08-10 19:40:01,293 INFO     29 [qwen-vl-table] coord item[1]: text=肌钙蛋白I, bbox=[104, 420, 180, 444]
2026-08-10 19:40:01,293 INFO     29 [qwen-vl-table] coord item[2]: text=肌红蛋白, bbox=[104, 453, 171, 477]
2026-08-10 19:40:01,293 INFO     29 [qwen-vl-table] coord item[3]: text=N端脑利钠肽前体, bbox=[104, 486, 228, 510]
2026-08-10 19:40:01,293 INFO     29 [qwen-vl-table] page=11 coord: matched 4/4, time=2.1s
2026-08-10 19:40:01,294 INFO     29 [qwen-vl-table] new_positions (4):
[[12, 87.568, 186.924, 230.265, 244.545], [12, 87.568, 151.56, 249.89999999999998, 264.18], [12, 87.568, 143.982, 269.53499999999997, 283.815], [12, 87.568, 191.976, 289.16999999999996, 303.45]]
2026-08-10 19:40:01,294 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=4, matched=4, pages=1, time=4.9s
2026-08-10 19:40:01,296 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:40:01,297 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:40:01,298 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[12]
2026-08-10 19:40:01,298 INFO     29 [qwen-vl-table] positions ： [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:40:01,462 INFO     29 [qwen-vl-table] page=12, rect=842x595, img=(2339x1653)
2026-08-10 19:40:01,463 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:40:01,463 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 329, \"bbox_end\": 342, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n\\hline\nNo & 项 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n\\hline\n1 & 凝血酶原时间(陕HR) & PT & 11.2 & 9.8-12.1 & sec & 凝固法 \\\\\n2 & 凝血酶原活动度 & PTA & 98.2 & 70-130 & \\% & 凝固法 \\\\\n3 & 国际标准化比值(陕HR) & INR & 0.97 & 0.7-1.3 & & 凝固法 \\\\\n4 & 活化部分凝血活酶时间(陕HR) & APTT & 36.1 & 22.7-31.8 & sec & 凝固法 \\\\\n5 & 纤维蛋白原含量(陕HR) & Fib & 6.680 & 1.8-3.5 & g/L & 凝固法 \\\\\n6 & 凝血酶时间(陕HR) & TT & 15.5 & 14-21 & sec & 凝固法 \\\\\n7 & 纤维蛋白(原)降解产物(定量) & FDP & 4.50 & 0-5 & $\\mu$g/mL & 胶乳免疫比浊法 \\\\\n8 & D-二聚体(定量)(陕HR) & D D & 1.185 & 0-1 & $\\mu$g/mL & 胶乳免疫比浊法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:40:06,024 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:40:06,024 INFO     29 [qwen-vl-table] page=12 LLM output (len=1417):
{
  "report_date": null,
  "items": [
    {
      "name": "凝血酶原时间(陕HR)",
      "item_code": "PT",
      "value": "11.2",
      "unit": "sec",
      "reference_range": "9.8-12.1",
      "abnormal": false
    },
    {
      "name": "凝血酶原活动度",
      "item_code": "PTA",
      "value": "98.2",
      "unit": "%",
      "reference_range": "70-130",
      "abnormal": false
    },
    {
      "name": "国际标准化比值(陕HR)",
      "item_code": "INR",
      "value": "0.97",
      "unit": null,
      "reference_range": "0.7-1.3",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间(陕HR)",
      "item_code": "APTT",
      "value": "36.1",
      "unit": "sec",
      "reference_range": "22.7-31.8",
      "abnormal": true
    },
    {
      "name": "纤维蛋白原含量(陕HR)",
      "item_code": "Fib",
      "value": "6.680",
      "unit": "g/L",
      "reference_range": "1.8-3.5",
      "abnormal": true
    },
    {
      "name": "凝血酶时间(陕HR)",
      "item_code": "TT",
      "value": "15.5",
      "unit": "sec",
      "reference_range": "14-21",
      "abnormal": false
    },
    {
      "name": "纤维蛋白(原)降解产物(定量)",
      "item_code": "FDP",
      "value": "4.50",
      "unit": "μg/mL",
      "reference_range": "0-5",
      "abnormal": false
    },
    {
      "name": "D-二聚体(定量)(陕HR)",
      "item_code": "D D",
      "value": "1.185",
      "unit": "μg/mL",
      "reference_range": "0-1",
      "abnormal": true
    }
  ]
}
2026-08-10 19:40:06,024 INFO     29 [qwen-vl-table] coord grouping: {12: 8}
2026-08-10 19:40:06,027 INFO     29 [qwen-vl-table] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=746158, prompt_len=610
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间(陕HR)、凝血酶原活动度、国际标准化比值(陕HR)、活化部分凝血活酶时间(陕HR)、纤维蛋白原含量(陕HR)、凝血酶时间(陕HR)、纤维蛋白(原)降解产物(定量)、D-二聚体(定量)(陕HR)

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
2026-08-10 19:40:09,154 INFO     29 [qwen-vl-table] coord API raw response (len=450):
[
	{"text": "凝血酶原时间(陕HR)", "bbox": [95, 337, 243, 362]},
	{"text": "凝血酶原活动度", "bbox": [95, 386, 211, 411]},
	{"text": "国际标准化比值(陕HR)", "bbox": [95, 436, 260, 461]},
	{"text": "活化部分凝血活酶时间(陕HR)", "bbox": [95, 486, 313, 511]},
	{"text": "纤维蛋白原含量(陕HR)", "bbox": [95, 535, 261, 560]},
	{"text": "凝血酶时间(陕HR)", "bbox": [95, 586, 227, 611]},
	{"text": "纤维蛋白(原)降解产物(定量)", "bbox": [95, 636, 317, 661]},
	{"text": "D-二聚体(定量)(陕HR)", "bbox": [95, 686, 271, 711]}
]
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=3.1s
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间(陕HR), bbox=[95, 337, 243, 362]
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord item[1]: text=凝血酶原活动度, bbox=[95, 386, 211, 411]
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord item[2]: text=国际标准化比值(陕HR), bbox=[95, 436, 260, 461]
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间(陕HR), bbox=[95, 486, 313, 511]
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord item[4]: text=纤维蛋白原含量(陕HR), bbox=[95, 535, 261, 560]
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord item[5]: text=凝血酶时间(陕HR), bbox=[95, 586, 227, 611]
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord item[6]: text=纤维蛋白(原)降解产物(定量), bbox=[95, 636, 317, 661]
2026-08-10 19:40:09,155 INFO     29 [qwen-vl-table] coord item[7]: text=D-二聚体(定量)(陕HR), bbox=[95, 686, 271, 711]
2026-08-10 19:40:09,156 INFO     29 [qwen-vl-table] page=12 coord: matched 8/8, time=3.1s
2026-08-10 19:40:09,156 INFO     29 [qwen-vl-table] new_positions (8):
[[13, 79.99, 204.606, 200.515, 215.39], [13, 79.99, 177.662, 229.67, 244.545], [13, 79.99, 218.92, 259.42, 274.295], [13, 79.99, 263.546, 289.16999999999996, 304.04499999999996], [13, 79.99, 219.762, 318.325, 333.2], [13, 79.99, 191.134, 348.66999999999996, 363.54499999999996], [13, 79.99, 266.914, 378.41999999999996, 393.29499999999996], [13, 79.99, 228.182, 408.16999999999996, 423.04499999999996]]
2026-08-10 19:40:09,156 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=8, matched=8, pages=1, time=7.9s
2026-08-10 19:40:09,157 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:40:09,159 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:40:09,159 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-10 19:40:09,159 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:40:09,344 INFO     29 [qwen-vl-table] page=13, rect=842x595, img=(2339x1653)
2026-08-10 19:40:09,345 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:40:09,345 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 343, \"bbox_end\": 375, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n\\hline\nNo. & 项 & 目 & 英文名称 & 结果 & 参考值 & 单位 & 检测方法 \\\\\n\\hline\n1 & 血糖(空腹)(8-HR) & & GLU & 5.56 & 3.9-6.1 & mmol/L & 己糖激酶法 \\\\\n2 & 钾(8-HR) & & K & 4.36 & 3.5-5.3 & mmol/L & 间接离子选择电极法 \\\\\n3 & 钠(8-HR) & & Na & 137.8 & 137-147 & mmol/L & 间接离子选择电极法 \\\\\n4 & 氯(8-HR) & & Cl & 100.9 & 99-110 & mmol/L & 间接离子选择电极法 \\\\\n5 & 总蛋白(8-HR) & & TP & 73.0 & 65-85 & g/L & 双缩脲比色法 \\\\\n6 & 白蛋白(8-HR) & & ALB & 42.4 & 40-55 & g/L & 溴甲酚绿法 \\\\\n7 & 球蛋白 & & GLO & 30.6 & 20-40 & g/L & 计算法 \\\\\n8 & 白球比 & & A/G & 1.4 & 1.2-2.4 & & 计算法 \\\\\n9 & 总胆红素(8-HR) & & T-BIL & 12.1 & 0-26 & $\\mu$mol/L & 钒酸盐氧化法 \\\\\n10 & 直接胆红素(8-HR) & & D-BIL & 3.5 & 0-6.8 & $\\mu$mol/L & 钒酸盐氧化法 \\\\\n11 & 间接胆红素 & & I-BIL & 8.6 & 0-14 & $\\mu$mol/L & 计算法 \\\\\n12 & 丙氨酸氨基转移酶(8-HR) & & ALT & 26 & 9-50 & U/L & 紫外-乳酸脱氢酶法 \\\\\n13 & 天门冬氨酸氨基转移酶(8-HR) & & AST & 21 & 15-40 & U/L & 紫外-苹果酸脱氢酶法 \\\\\n14 & AST/ALT & & & 0.81 & & & 计算法 \\\\\n15 & 碱性磷酸酶(8-HR) & & ALP & 106 & 45-125 & U/L & AMP缓冲液法 \\\\\n16 & 总胆汁酸(陕HR) & & TBA & 12.6 & 0-10 & $\\mu$mol/L & 循环酶法 \\\\\n17 & 胆碱酯酶(陕HR) & & CHE & 6970 & 5000-12000 & U/L & 丁酰硫代胆碱/铁氰化钾 \\\\\n18 & $\\gamma$-谷氨酰转移酶(8-HR) & & GGT & 23 & 10-60 & U/L & 速率法 \\\\\n19 & eGFR(CKD-EPI) & & eGFR & 93.12 & >90 & ml/min/1.73m2 & 计算法 \\\\\n20 & 尿酸(8-HR) & & UA & 263.0 & 208-428 & $\\mu$mol/L & 氧化酶法 \\\\\n21 & 尿素(8-HR) & & UREA & 6.7 & 3.1-8.0 & mmol/L & 紫外-谷氨酸脱氢酶法 \\\\\n22 & 肌酐(8-HR) & & CRE & 81.0 & 57-97 & $\\mu$mol/L & 肌氨酸氧化酶法 \\\\\n23 & 肌酸激酶(8-HR) & & CK & 84 & 50-310 & U/L & N-乙酰半胱氨酸法 \\\\\n24 & 肌酸激酶同功酶 & & CK-MB & 12.43 & <25 & U/L & 免疫抑制法 \\\\\n25 & 乳酸脱氢酶(8-HR) & & LDH & 186 & 120-250 & U/L & 乳酸法 \\\\\n26 & $\\alpha$-羟丁酸脱氢酶(陕HR) & & $\\alpha$-HBDH & 140 & 72-182 & U/L & DGKC法 \\\\\n27 & 钙(8-HR) & & Ca & 2.26 & 2.2-2.7 & mmol/L & 偶氮胂III法 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 19:40:28,866 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:40:28.865+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:40:56,367 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:40:56,368 INFO     29 [qwen-vl-table] page=13 LLM output (len=4634):
{
  "report_date": null,
  "items": [
    {
      "name": "血糖(空腹)(8-HR)",
      "item_code": "GLU",
      "value": "5.56",
      "unit": "mmol/L",
      "reference_range": "3.9-6.1",
      "abnormal": false
    },
    {
      "name": "钾(8-HR)",
      "item_code": "K",
      "value": "4.36",
      "unit": "mmol/L",
      "reference_range": "3.5-5.3",
      "abnormal": false
    },
    {
      "name": "钠(8-HR)",
      "item_code": "Na",
      "value": "137.8",
      "unit": "mmol/L",
      "reference_range": "137-147",
      "abnormal": false
    },
    {
      "name": "氯(8-HR)",
      "item_code": "Cl",
      "value": "100.9",
      "unit": "mmol/L",
      "reference_range": "99-110",
      "abnormal": false
    },
    {
      "name": "总蛋白(8-HR)",
      "item_code": "TP",
      "value": "73.0",
      "unit": "g/L",
      "reference_range": "65-85",
      "abnormal": false
    },
    {
      "name": "白蛋白(8-HR)",
      "item_code": "ALB",
      "value": "42.4",
      "unit": "g/L",
      "reference_range": "40-55",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLO",
      "value": "30.6",
      "unit": "g/L",
      "reference_range": "20-40",
      "abnormal": false
    },
    {
      "name": "白球比",
      "item_code": "A/G",
      "value": "1.4",
      "unit": null,
      "reference_range": "1.2-2.4",
      "abnormal": false
    },
    {
      "name": "总胆红素(8-HR)",
      "item_code": "T-BIL",
      "value": "12.1",
      "unit": "μmol/L",
      "reference_range": "0-26",
      "abnormal": false
    },
    {
      "name": "直接胆红素(8-HR)",
      "item_code": "D-BIL",
      "value": "3.5",
      "unit": "μmol/L",
      "reference_range": "0-6.8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "I-BIL",
      "value": "8.6",
      "unit": "μmol/L",
      "reference_range": "0-14",
      "abnormal": false
    },
    {
      "name": "丙氨酸氨基转移酶(8-HR)",
      "item_code": "ALT",
      "value": "26",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "天门冬氨酸氨基转移酶(8-HR)",
      "item_code": "AST",
      "value": "21",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "AST/ALT",
      "item_code": null,
      "value": "0.81",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶(8-HR)",
      "item_code": "ALP",
      "value": "106",
      "unit": "U/L",
      "reference_range": "45-125",
      "abnormal": false
    },
    {
      "name": "总胆汁酸(陕HR)",
      "item_code": "TBA",
      "value": "12.6",
      "unit": "μmol/L",
      "reference_range": "0-10",
      "abnormal": true
    },
    {
      "name": "胆碱酯酶(陕HR)",
      "item_code": "CHE",
      "value": "6970",
      "unit": "U/L",
      "reference_range": "5000-12000",
      "abnormal": false
    },
    {
      "name": "γ-谷氨酰转移酶(8-HR)",
      "item_code": "GGT",
      "value": "23",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": false
    },
    {
      "name": "eGFR(CKD-EPI)",
      "item_code": "eGFR",
      "value": "93.12",
      "unit": "ml/min/1.73m2",
      "reference_range": ">90",
      "abnormal": false
    },
    {
      "name": "尿酸(8-HR)",
      "item_code": "UA",
      "value": "263.0",
      "unit": "μmol/L",
      "reference_range": "208-428",
      "abnormal": false
    },
    {
      "name": "尿素(8-HR)",
      "item_code": "UREA",
      "value": "6.7",
      "unit": "mmol/L",
      "reference_range": "3.1-8.0",
      "abnormal": false
    },
    {
      "name": "肌酐(8-HR)",
      "item_code": "CRE",
      "value": "81.0",
      "unit": "μmol/L",
      "reference_range": "57-97",
      "abnormal": false
    },
    {
      "name": "肌酸激酶(8-HR)",
      "item_code": "CK",
      "value": "84",
      "unit": "U/L",
      "reference_range": "50-310",
      "abnormal": false
    },
    {
      "name": "肌酸激酶同功酶",
      "item_code": "CK-MB",
      "value": "12.43",
      "unit": "U/L",
      "reference_range": "<25",
      "abnormal": false
    },
    {
      "name": "乳酸脱氢酶(8-HR)",
      "item_code": "LDH",
      "value": "186",
      "unit": "U/L",
      "reference_range": "120-250",
      "abnormal": false
    },
    {
      "name": "α-羟丁酸脱氢酶(陕HR)",
      "item_code": "α-HBDH",
      "value": "140",
      "unit": "U/L",
      "reference_range": "72-182",
      "abnormal": false
    },
    {
      "name": "钙(8-HR)",
      "item_code": "Ca",
      "value": "2.26",
      "unit": "mmol/L",
      "reference_range": "2.2-2.7",
      "abnormal": false
    }
  ]
}
2026-08-10 19:40:56,368 INFO     29 [qwen-vl-table] coord grouping: {13: 27}
2026-08-10 19:40:56,371 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1054317, prompt_len=781
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
血糖(空腹)(8-HR)、钾(8-HR)、钠(8-HR)、氯(8-HR)、总蛋白(8-HR)、白蛋白(8-HR)、球蛋白、白球比、总胆红素(8-HR)、直接胆红素(8-HR)、间接胆红素、丙氨酸氨基转移酶(8-HR)、天门冬氨酸氨基转移酶(8-HR)、AST/ALT、碱性磷酸酶(8-HR)、总胆汁酸(陕HR)、胆碱酯酶(陕HR)、γ-谷氨酰转移酶(8-HR)、eGFR(CKD-EPI)、尿酸(8-HR)、尿素(8-HR)、肌酐(8-HR)、肌酸激酶(8-HR)、肌酸激酶同功酶、乳酸脱氢酶(8-HR)、α-羟丁酸脱氢酶(陕HR)、钙(8-HR)

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
2026-08-10 19:41:04,348 INFO     29 [qwen-vl-table] coord API raw response (len=1465):
[
	{"text": "血糖(空腹)(8-HR)", "bbox": [186, 221, 287, 240]},
	{"text": "钾(8-HR)", "bbox": [186, 243, 235, 262]},
	{"text": "钠(8-HR)", "bbox": [186, 265, 235, 284]},
	{"text": "氯(8-HR)", "bbox": [186, 288, 235, 306]},
	{"text": "总蛋白(8-HR)", "bbox": [186, 310, 261, 329]},
	{"text": "白蛋白(8-HR)", "bbox": [186, 333, 261, 351]},
	{"text": "球蛋白", "bbox": [186, 355, 224, 373]},
	{"text": "白球比", "bbox": [186, 377, 224, 395]},
	{"text": "总胆红素(8-HR)", "bbox": [186, 399, 275, 417]},
	{"text": "直接胆红素(8-HR)", "bbox": [186, 421, 287, 439]},
	{"text": "间接胆红素", "bbox": [186, 443, 251, 461]},
	{"text": "丙氨酸氨基转移酶(8-HR)", "bbox": [186, 465, 327, 483]},
	{"text": "天门冬氨酸氨基转移酶(8-HR)", "bbox": [186, 487, 353, 505]},
	{"text": "AST/ALT", "bbox": [186, 510, 232, 528]},
	{"text": "碱性磷酸酶(8-HR)", "bbox": [186, 532, 287, 550]},
	{"text": "总胆汁酸(陕HR)", "bbox": [186, 554, 275, 573]},
	{"text": "胆碱酯酶(陕HR)", "bbox": [186, 577, 275, 595]},
	{"text": "γ-谷氨酰转移酶(8-HR)", "bbox": [186, 599, 320, 617]},
	{"text": "eGFR(CKD-EPI)", "bbox": [186, 621, 269, 640]},
	{"text": "尿酸(8-HR)", "bbox": [186, 644, 250, 662]},
	{"text": "尿素(8-HR)", "bbox": [186, 666, 250, 685]},
	{"text": "肌酐(8-HR)", "bbox": [186, 688, 250, 707]},
	{"text": "肌酸激酶(8-HR)", "bbox": [186, 711, 275, 729]},
	{"text": "肌酸激酶同功酶", "bbox": [186, 733, 278, 751]},
	{"text": "乳酸脱氢酶(8-HR)", "bbox": [186, 755, 290, 774]},
	{"text": "α-羟丁酸脱氢酶(陕HR)", "bbox": [186, 777, 322, 796]},
	{"text": "钙(8-HR)", "bbox": [186, 800, 238, 818]}
]
2026-08-10 19:41:04,349 INFO     29 [qwen-vl-table] coord API: raw_items=27, valid_items=27, elapsed=8.0s
2026-08-10 19:41:04,349 INFO     29 [qwen-vl-table] coord item[0]: text=血糖(空腹)(8-HR), bbox=[186, 221, 287, 240]
2026-08-10 19:41:04,349 INFO     29 [qwen-vl-table] coord item[1]: text=钾(8-HR), bbox=[186, 243, 235, 262]
2026-08-10 19:41:04,349 INFO     29 [qwen-vl-table] coord item[2]: text=钠(8-HR), bbox=[186, 265, 235, 284]
2026-08-10 19:41:04,349 INFO     29 [qwen-vl-table] coord item[3]: text=氯(8-HR), bbox=[186, 288, 235, 306]
2026-08-10 19:41:04,349 INFO     29 [qwen-vl-table] coord item[4]: text=总蛋白(8-HR), bbox=[186, 310, 261, 329]
2026-08-10 19:41:04,349 INFO     29 [qwen-vl-table] coord item[5]: text=白蛋白(8-HR), bbox=[186, 333, 261, 351]
2026-08-10 19:41:04,349 INFO     29 [qwen-vl-table] coord item[6]: text=球蛋白, bbox=[186, 355, 224, 373]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[7]: text=白球比, bbox=[186, 377, 224, 395]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[8]: text=总胆红素(8-HR), bbox=[186, 399, 275, 417]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[9]: text=直接胆红素(8-HR), bbox=[186, 421, 287, 439]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[10]: text=间接胆红素, bbox=[186, 443, 251, 461]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[11]: text=丙氨酸氨基转移酶(8-HR), bbox=[186, 465, 327, 483]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[12]: text=天门冬氨酸氨基转移酶(8-HR), bbox=[186, 487, 353, 505]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[13]: text=AST/ALT, bbox=[186, 510, 232, 528]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[14]: text=碱性磷酸酶(8-HR), bbox=[186, 532, 287, 550]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[15]: text=总胆汁酸(陕HR), bbox=[186, 554, 275, 573]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[16]: text=胆碱酯酶(陕HR), bbox=[186, 577, 275, 595]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[17]: text=γ-谷氨酰转移酶(8-HR), bbox=[186, 599, 320, 617]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[18]: text=eGFR(CKD-EPI), bbox=[186, 621, 269, 640]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[19]: text=尿酸(8-HR), bbox=[186, 644, 250, 662]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[20]: text=尿素(8-HR), bbox=[186, 666, 250, 685]
2026-08-10 19:41:04,350 INFO     29 [qwen-vl-table] coord item[21]: text=肌酐(8-HR), bbox=[186, 688, 250, 707]
2026-08-10 19:41:04,351 INFO     29 [qwen-vl-table] coord item[22]: text=肌酸激酶(8-HR), bbox=[186, 711, 275, 729]
2026-08-10 19:41:04,351 INFO     29 [qwen-vl-table] coord item[23]: text=肌酸激酶同功酶, bbox=[186, 733, 278, 751]
2026-08-10 19:41:04,351 INFO     29 [qwen-vl-table] coord item[24]: text=乳酸脱氢酶(8-HR), bbox=[186, 755, 290, 774]
2026-08-10 19:41:04,351 INFO     29 [qwen-vl-table] coord item[25]: text=α-羟丁酸脱氢酶(陕HR), bbox=[186, 777, 322, 796]
2026-08-10 19:41:04,351 INFO     29 [qwen-vl-table] coord item[26]: text=钙(8-HR), bbox=[186, 800, 238, 818]
2026-08-10 19:41:04,351 INFO     29 [qwen-vl-table] page=13 coord: matched 27/27, time=8.0s
2026-08-10 19:41:04,351 INFO     29 [qwen-vl-table] new_positions (27):
[[14, 156.612, 241.654, 131.495, 142.79999999999998], [14, 156.612, 197.87, 144.58499999999998, 155.89], [14, 156.612, 197.87, 157.67499999999998, 168.98], [14, 156.612, 197.87, 171.35999999999999, 182.07], [14, 156.612, 219.762, 184.45, 195.755], [14, 156.612, 219.762, 198.135, 208.845], [14, 156.612, 188.608, 211.225, 221.935], [14, 156.612, 188.608, 224.315, 235.02499999999998], [14, 156.612, 231.54999999999998, 237.405, 248.11499999999998], [14, 156.612, 241.654, 250.49499999999998, 261.205], [14, 156.612, 211.34199999999998, 263.585, 274.295], [14, 156.612, 275.334, 276.675, 287.385], [14, 156.612, 297.226, 289.765, 300.47499999999997], [14, 156.612, 195.344, 303.45, 314.15999999999997], [14, 156.612, 241.654, 316.53999999999996, 327.25], [14, 156.612, 231.54999999999998, 329.63, 340.935], [14, 156.612, 231.54999999999998, 343.315, 354.025], [14, 156.612, 269.44, 356.405, 367.115], [14, 156.612, 226.498, 369.495, 380.79999999999995], [14, 156.612, 210.5, 383.18, 393.89], [14, 156.612, 210.5, 396.27, 407.575], [14, 156.612, 210.5, 409.35999999999996, 420.66499999999996], [14, 156.612, 231.54999999999998, 423.04499999999996, 433.755], [14, 156.612, 234.076, 436.135, 446.84499999999997], [14, 156.612, 244.17999999999998, 449.22499999999997, 460.53], [14, 156.612, 271.12399999999997, 462.315, 473.62], [14, 156.612, 200.396, 476.0, 486.71]]
2026-08-10 19:41:04,352 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=27, matched=27, pages=1, time=55.2s
2026-08-10 19:41:04,364 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 19:41:04,364 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:LabExam | outputs={"chunks": "11 items, types={'LabReport': 11}", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:41:04,365 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 19:41:04,366 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:41:04.365+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:41:04,372 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:04,372 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:41:05,179 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:05,185 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 19:41:05,186 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:41:05,186 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 19:41:05,192 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:05,192 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:41:05,942 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:05,950 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 19:41:05,951 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:41:05,951 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 19:41:05,956 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:05,957 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:41:06,595 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:06,605 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 19:41:06,605 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:41:06,605 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 19:41:06,610 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:06,611 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:41:07,031 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:07,037 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 19:41:07,037 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:41:07,037 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 19:41:07,041 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:41:07,042 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:41:07,042 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 19:41:07,042 INFO     29 [qwen-vl-text] positions(32): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:41:07,042 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [32]
2026-08-10 19:41:07,197 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 19:41:07,197 INFO     29 [qwen-vl-text] LLM extraction start, text_len=191
2026-08-10 19:41:07,198 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:07,198 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 99, \"bbox_end\": 130, \"encounter_dates\": [\"2026-03-02\"], \"department\": \"肿瘤科病区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "中国人民解放军联勤保障部队第九八九医院\n出院证\n姓名\n性别\n男\n年龄\n55岁\n费别\nID号\n2019131\n住院号\nA28146\n入院日期\n2026-02-22\n出院日期\n2026-03-02\n住院天数\n8\n出院科室\n肿瘤科病区\n出院诊断:\n肺占位\n出院情况:\n一般情况可\n出院医嘱:\n他院继续治疗\n经治医生:\n刘佳\n日期:\n2026-03-02\n费川已核LY-16\n审核人:于德艳",
    "role": "user"
  }
]
2026-08-10 19:41:15,113 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:15,113 INFO     29 [qwen-vl-text] LLM output (len=832):
{
  "encounter_date": "2026-03-02",
  "admission_date": "2026-02-22",
  "discharge_date": "2026-03-02",
  "hospital_days": 8,
  "department": "肿瘤科病区",
  "bed_number": null,
  "admission_condition": null,
  "admission_diagnoses": [],
  "treatment_summary": null,
  "auxiliary_exams": null,
  "imaging_findings": null,
  "discharge_diagnoses": [
    {
      "name": "肺占位",
      "diagnosis_type": null
    }
  ],
  "condition_at_discharge": "一般情况可",
  "outcome": null,
  "discharge_orders": "他院继续治疗",
  "do_medications": [],
  "do_follow_up": null,
  "do_precautions": [],
  "next_treatment_date": null,
  "attending_physician": "刘佳",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 19:41:15,113 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-02]
2026-08-10 19:41:15,117 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2189265, prompt_len=900
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["中国人民解放军联勤保障部队第九八九医院", "出院证", "姓名", "性别", "男", "年龄", "55岁", "费别", "ID号", "2019131", "住院号", "A28146", "入院日期", "2026-02-22", "出院日期", "2026-03-02", "住院天数", "8", "出院科室", "肿瘤科病区", "出院诊断:", "肺占位", "出院情况:", "一般情况可", "出院医嘱:", "他院继续治疗", "经治医生:", "刘佳", "日期:", "2026-03-02", "费川已核LY-16", "审核人:于德艳"]

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
2026-08-10 19:41:31,435 INFO     29 [qwen-vl-text] coord API raw response (len=2654):
[
	{"text": "中国人民解放军联勤保障部队第九八九医院", "bbox": [356, 177, 728, 207]},
	{"text": "出院证", "bbox": [506, 228, 586, 257]},
	{"text": "姓名", "bbox": [253, 273, 270, 293], "bbox": [253, 273, 270, 293]},
	{"text": "名", "bbox": [295, 274, 309, 294], "bbox": [295, 274, 309, 294]},
	{"text": "性别", "bbox": [484, 278, 499, 298], "bbox": [484, 278, 499, 298]},
	{"text": "男", "bbox": [574, 280, 586, 300], "bbox": [574, 280, 586, 300]},
	{"text": "年龄", "bbox": [666, 280, 682, 300], "bbox": [666, 280, 682, 300]},
	{"text": "55岁", "bbox": [770, 283, 797, 301], "bbox": [770, 283, 797, 301]},
	{"text": "费别", "bbox": [253, 316, 267, 336], "bbox": [253, 316, 267, 336]},
	{"text": "别", "bbox": [294, 317, 308, 337], "bbox": [294, 317, 308, 337]},
	{"text": "ID号", "bbox": [484, 321, 538, 341], "bbox": [484, 321, 538, 341]},
	{"text": "2019131", "bbox": [572, 324, 619, 341], "bbox": [572, 324, 619, 341]},
	{"text": "住院号", "bbox": [667, 324, 721, 344], "bbox": [667, 324, 721, 344]},
	{"text": "A28146", "bbox": [770, 327, 812, 343], "bbox": [770, 327, 812, 343]},
	{"text": "入院日期", "bbox": [251, 357, 307, 377], "bbox": [251, 357, 307, 377]},
	{"text": "2026-02-22", "bbox": [339, 361, 408, 378], "bbox": [339, 361, 408, 378]},
	{"text": "出院日期", "bbox": [484, 362, 538, 382], "bbox": [484, 362, 538, 382]},
	{"text": "2026-03-02", "bbox": [572, 365, 640, 382], "bbox": [572, 365, 640, 382]},
	{"text": "住院天数", "bbox": [667, 365, 721, 385], "bbox": [667, 365, 721, 385]},
	{"text": "8", "bbox": [770, 368, 779, 384], "bbox": [770, 368, 779, 384]},
	{"text": "出院科室", "bbox": [250, 398, 306, 418], "bbox": [250, 398, 306, 418]},
	{"text": "肿瘤科病区", "bbox": [338, 400, 406, 420], "bbox": [338, 400, 406, 420]},
	{"text": "出院诊断:", "bbox": [248, 439, 309, 459], "bbox": [248, 439, 309, 459]},
	{"text": "肺占位", "bbox": [337, 441, 378, 461], "bbox": [337, 441, 378, 461]},
	{"text": "出院情况:", "bbox": [247, 480, 308, 500], "bbox": [247, 480, 308, 500]},
	{"text": "一般情况可", "bbox": [337, 482, 404, 502], "bbox": [337, 482, 404, 502]},
	{"text": "出院医嘱:", "bbox": [245, 521, 306, 541], "bbox": [245, 521, 306, 541]},
	{"text": "他院继续治疗", "bbox": [335, 523, 416, 543], "bbox": [335, 523, 416, 543]},
	{"text": "经治医生:", "bbox": [570, 570, 632, 590], "bbox": [570, 570, 632, 590]},
	{"text": "刘佳", "bbox": [668, 573, 697, 592], "bbox": [668, 573, 697, 592]},
	{"text": "日期:", "bbox": [572, 614, 633, 634], "bbox": [572, 614, 633, 634]},
	{"text": "2026-03-02", "bbox": [668, 617, 738, 635], "bbox": [668, 617, 738, 635]},
	{"text": "费川已核LY-16", "bbox": [695, 680, 835, 745], "bbox": [695, 680, 835, 745]},
	{"text": "审核人:于德艳", "bbox": [690, 732, 835, 804], "bbox": [690, 732, 835, 804]}
]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=16.3s
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[0]: text=中国人民解放军联勤保障部队第九八九医院, bbox=[356, 177, 728, 207]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[1]: text=出院证, bbox=[506, 228, 586, 257]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[253, 273, 270, 293]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[3]: text=名, bbox=[295, 274, 309, 294]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[4]: text=性别, bbox=[484, 278, 499, 298]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[5]: text=男, bbox=[574, 280, 586, 300]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[6]: text=年龄, bbox=[666, 280, 682, 300]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[7]: text=55岁, bbox=[770, 283, 797, 301]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[8]: text=费别, bbox=[253, 316, 267, 336]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[9]: text=别, bbox=[294, 317, 308, 337]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[10]: text=ID号, bbox=[484, 321, 538, 341]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[11]: text=2019131, bbox=[572, 324, 619, 341]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[12]: text=住院号, bbox=[667, 324, 721, 344]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[13]: text=A28146, bbox=[770, 327, 812, 343]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[14]: text=入院日期, bbox=[251, 357, 307, 377]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[15]: text=2026-02-22, bbox=[339, 361, 408, 378]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[16]: text=出院日期, bbox=[484, 362, 538, 382]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[17]: text=2026-03-02, bbox=[572, 365, 640, 382]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[18]: text=住院天数, bbox=[667, 365, 721, 385]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[19]: text=8, bbox=[770, 368, 779, 384]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[20]: text=出院科室, bbox=[250, 398, 306, 418]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[21]: text=肿瘤科病区, bbox=[338, 400, 406, 420]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[22]: text=出院诊断:, bbox=[248, 439, 309, 459]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[23]: text=肺占位, bbox=[337, 441, 378, 461]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[24]: text=出院情况:, bbox=[247, 480, 308, 500]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[25]: text=一般情况可, bbox=[337, 482, 404, 502]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[26]: text=出院医嘱:, bbox=[245, 521, 306, 541]
2026-08-10 19:41:31,436 INFO     29 [qwen-vl-text] coord item[27]: text=他院继续治疗, bbox=[335, 523, 416, 543]
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] coord item[28]: text=经治医生:, bbox=[570, 570, 632, 590]
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] coord item[29]: text=刘佳, bbox=[668, 573, 697, 592]
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] coord item[30]: text=日期:, bbox=[572, 614, 633, 634]
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] coord item[31]: text=2026-03-02, bbox=[668, 617, 738, 635]
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] coord item[32]: text=费川已核LY-16, bbox=[695, 680, 835, 745]
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] coord item[33]: text=审核人:于德艳, bbox=[690, 732, 835, 804]
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] page=3 — 32/32 coords, api_time=16.3s
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] new_positions (32):
[[3, 299.752, 612.976, 105.315, 123.16499999999999], [3, 426.05199999999996, 493.412, 135.66, 152.915], [3, 213.02599999999998, 227.34, 162.435, 174.33499999999998], [3, 248.39, 260.178, 163.03, 174.92999999999998], [3, 407.52799999999996, 420.15799999999996, 165.41, 177.31], [3, 483.308, 493.412, 166.6, 178.5], [3, 560.7719999999999, 574.244, 166.6, 178.5], [3, 648.34, 671.074, 168.385, 179.095], [3, 213.02599999999998, 224.814, 188.01999999999998, 199.92], [3, 247.548, 259.336, 188.61499999999998, 200.515], [3, 407.52799999999996, 452.996, 190.995, 202.89499999999998], [3, 481.62399999999997, 521.198, 192.78, 202.89499999999998], [3, 561.614, 607.082, 192.78, 204.67999999999998], [3, 648.34, 683.704, 194.565, 204.08499999999998], [3, 211.34199999999998, 258.49399999999997, 212.415, 224.315], [3, 285.438, 343.536, 214.795, 224.91], [3, 407.52799999999996, 452.996, 215.39, 227.29], [3, 481.62399999999997, 538.88, 217.17499999999998, 227.29], [3, 561.614, 607.082, 217.17499999999998, 229.075], [3, 648.34, 655.918, 218.95999999999998, 228.48], [3, 210.5, 257.652, 236.81, 248.70999999999998], [3, 284.596, 341.852, 238.0, 249.89999999999998], [3, 208.816, 260.178, 261.205, 273.10499999999996], [3, 283.75399999999996, 318.276, 262.395, 274.295], [3, 207.974, 259.336, 285.59999999999997, 297.5], [3, 283.75399999999996, 340.168, 286.78999999999996, 298.69], [3, 206.29, 257.652, 309.995, 321.895], [3, 282.07, 350.272, 311.185, 323.085], [3, 479.94, 532.144, 339.15, 351.05], [3, 562.456, 586.874, 340.935, 352.24], [3, 481.62399999999997, 532.986, 365.33, 377.22999999999996], [3, 562.456, 621.396, 367.115, 377.825]]
2026-08-10 19:41:31,437 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=24.4s
2026-08-10 19:41:31,437 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:41:31,443 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:41:31,443 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 19:41:31,443 INFO     29 [qwen-vl-text] positions(46): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:41:31,444 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [46]
2026-08-10 19:41:31,724 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:41:31,725 INFO     29 [qwen-vl-text] LLM extraction start, text_len=769
2026-08-10 19:41:31,726 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:31,726 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 131, \"bbox_end\": 176, \"encounter_dates\": [\"2026-03-02\"], \"department\": \"肿瘤科病区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "中国人民解放军联勤保障部队第九八九医院\n姓名:水月强\n病区(科):肿瘤科病区\n床号:11\n出院记录\n姓名:\n性别:男\n年龄:55岁\n入院时间:2026-02-22 08:42\n出院时间:2026-03-02\n住院天数:8天\n入院情况:2025年12月无明显诱因出现胸闷,无发热、咳嗽、盗汗不适,未在意。2天前出现咯血,\n色鲜红,量约10ml,2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大\n淋巴结,双肺肺气肿,胸骨陈旧性骨折。入院当天再次出现咯血,急诊入院。入院查体:神志清楚,精\n神好,双肺呼吸音清,未闻及干湿性罗音,心律齐,心音低钝,各瓣膜听诊区未闻及病理性杂音。\n入院诊断:1、{肺肿物}\n2、肺气肿\n诊疗经过:患者入科后查血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝\n肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。\n心电图:正常。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气\n肿;3.上腹部CT增强未见明显异常。进一步行CT引导下穿刺活检,病理:(左肺穿刺组织)慢性炎症,间\n质纤维组织增生、淋巴细胞浸润,请结合临床综合考虑。免疫组化结果:CK7(+),TTF-1(+),NapsinA\n(+),CK-Pan(+),Ki-67(5%),P63(-)。建议患者再次穿刺活检或手术治疗,但家属要求出院,经请\n示潘雪峰主任后同意,为患者办理出院手续。\n出院诊断:1、{肺肿物}\n2、肺气肿\n出院情况:目前患者生命体征平稳,病情稳定。\n出院医嘱及健康指导:\n他院继续治疗。\n/刘佳}\nx\n√\n※\nN\n□\n☐\nI\nII\nIII\nIV\nV\n(\n{\n[\n(\n更多",
    "role": "user"
  }
]
2026-08-10 19:41:36,590 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:41:36.589+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:41:39,674 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:39,675 INFO     29 [qwen-vl-text] LLM output (len=1865):
{
  "encounter_date": "2026-03-02",
  "admission_date": "2026-02-22",
  "discharge_date": "2026-03-02",
  "hospital_days": 8,
  "department": "肿瘤科病区",
  "bed_number": "11",
  "admission_condition": "2025年12月无明显诱因出现胸闷,无发热、咳嗽、盗汗不适,未在意。2天前出现咯血,色鲜红,量约10ml,2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大淋巴结,双肺肺气肿,胸骨陈旧性骨折。入院当天再次出现咯血,急诊入院。入院查体:神志清楚,精神好,双肺呼吸音清,未闻及干湿性罗音,心律齐,心音低钝,各瓣膜听诊区未闻及病理性杂音。",
  "admission_diagnoses": [
    {
      "name": "{肺肿物}",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺气肿",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "患者入科后查血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。心电图:正常。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气肿;3.上腹部CT增强未见明显异常。进一步行CT引导下穿刺活检,病理:(左肺穿刺组织)慢性炎症,间质纤维组织增生、淋巴细胞浸润,请结合临床综合考虑。免疫组化结果:CK7(+),TTF-1(+),NapsinA(+),CK-Pan(+),Ki-67(5%),P63(-)。建议患者再次穿刺活检或手术治疗,但家属要求出院,经请示潘雪峰主任后同意,为患者办理出院手续。",
  "auxiliary_exams": "血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。心电图:正常。病理:(左肺穿刺组织)慢性炎症,间质纤维组织增生、淋巴细胞浸润。免疫组化结果:CK7(+),TTF-1(+),NapsinA(+),CK-Pan(+),Ki-67(5%),P63(-)。",
  "imaging_findings": "2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大淋巴结,双肺肺气肿,胸骨陈旧性骨折。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气肿;3.上腹部CT增强未见明显异常。",
  "discharge_diagnoses": [
    {
      "name": "{肺肿物}",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺气肿",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "目前患者生命体征平稳,病情稳定。",
  "outcome": null,
  "discharge_orders": "他院继续治疗。",
  "do_medications": [],
  "do_follow_up": null,
  "do_precautions": [],
  "next_treatment_date": null,
  "attending_physician": "潘雪峰",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 19:41:39,675 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-02]
2026-08-10 19:41:39,686 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4236636, prompt_len=1520
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共46行）
["中国人民解放军联勤保障部队第九八九医院", "姓名:水月强", "病区(科):肿瘤科病区", "床号:11", "出院记录", "姓名:", "性别:男", "年龄:55岁", "入院时间:2026-02-22 08:42", "出院时间:2026-03-02", "住院天数:8天", "入院情况:2025年12月无明显诱因出现胸闷,无发热、咳嗽、盗汗不适,未在意。2天前出现咯血,", "色鲜红,量约10ml,2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大", "淋巴结,双肺肺气肿,胸骨陈旧性骨折。入院当天再次出现咯血,急诊入院。入院查体:神志清楚,精", "神好,双肺呼吸音清,未闻及干湿性罗音,心律齐,心音低钝,各瓣膜听诊区未闻及病理性杂音。", "入院诊断:1、{肺肿物}", "2、肺气肿", "诊疗经过:患者入科后查血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝", "肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。", "心电图:正常。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气", "肿;3.上腹部CT增强未见明显异常。进一步行CT引导下穿刺活检,病理:(左肺穿刺组织)慢性炎症,间", "质纤维组织增生、淋巴细胞浸润,请结合临床综合考虑。免疫组化结果:CK7(+),TTF-1(+),NapsinA", "(+),CK-Pan(+),Ki-67(5%),P63(-)。建议患者再次穿刺活检或手术治疗,但家属要求出院,经请", "示潘雪峰主任后同意,为患者办理出院手续。", "出院诊断:1、{肺肿物}", "2、肺气肿", "出院情况:目前患者生命体征平稳,病情稳定。", "出院医嘱及健康指导:", "他院继续治疗。", "/刘佳}", "x", "√", "※", "N", "□", "☐", "I", "II", "III", "IV", "V", "(", "{", "[", "(", "更多"]

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
2026-08-10 19:41:54,297 INFO     29 [qwen-vl-text] coord API raw response (len=2796):
[
	{"text": "中国人民解放军联勤保障部队第九八九医院", "bbox": [199, 199, 804, 223]},
	{"text": "姓名:水月强", "bbox": [146, 244, 234, 259]},
	{"text": "病区(科):肿瘤科病区", "bbox": [271, 244, 444, 259]},
	{"text": "床号:11", "bbox": [525, 244, 614, 259]},
	{"text": "出院记录", "bbox": [446, 273, 555, 292]},
	{"text": "姓名:", "bbox": [165, 303, 225, 318]},
	{"text": "性别:男", "bbox": [165, 328, 304, 343]},
	{"text": "年龄:55岁", "bbox": [165, 352, 320, 367]},
	{"text": "入院时间:2026-02-22 08:42", "bbox": [502, 303, 773, 318]},
	{"text": "出院时间:2026-03-02", "bbox": [502, 328, 728, 343]},
	{"text": "住院天数:8天", "bbox": [502, 352, 674, 367]},
	{"text": "入院情况:2025年12月无明显诱因出现胸闷,无发热、咳嗽、盗汗不适,未在意。2天前出现咯血,", "bbox": [171, 375, 852, 390]},
	{"text": "色鲜红,量约10ml,2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大", "bbox": [138, 400, 861, 415]},
	{"text": "淋巴结,双肺肺气肿,胸骨陈旧性骨折。入院当天再次出现咯血,急诊入院。入院查体:神志清楚,精", "bbox": [138, 424, 861, 439]},
	{"text": "神好,双肺呼吸音清,未闻及干湿性罗音,心律齐,心音低钝,各瓣膜听诊区未闻及病理性杂音。", "bbox": [138, 448, 824, 463]},
	{"text": "入院诊断:1、{肺肿物}", "bbox": [171, 472, 352, 487]},
	{"text": "2、肺气肿", "bbox": [254, 497, 334, 511]},
	{"text": "诊疗经过:患者入科后查血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝", "bbox": [171, 521, 864, 536]},
	{"text": "肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。", "bbox": [134, 546, 857, 561]},
	{"text": "心电图:正常。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气", "bbox": [134, 570, 864, 585]},
	{"text": "肿;3.上腹部CT增强未见明显异常。进一步行CT引导下穿刺活检,病理:(左肺穿刺组织)慢性炎症,间", "bbox": [134, 595, 864, 610]},
	{"text": "质纤维组织增生、淋巴细胞浸润,请结合临床综合考虑。免疫组化结果:CK7(+),TTF-1(+),NapsinA", "bbox": [134, 619, 857, 634]},
	{"text": "(+),CK-Pan(+),Ki-67(5%),P63(-)。建议患者再次穿刺活检或手术治疗,但家属要求出院,经请", "bbox": [134, 644, 864, 660]},
	{"text": "示潘雪峰主任后同意,为患者办理出院手续。", "bbox": [131, 670, 459, 685]},
	{"text": "出院诊断:1、{肺肿物}", "bbox": [165, 696, 347, 711]},
	{"text": "2、肺气肿", "bbox": [250, 722, 327, 737]},
	{"text": "出院情况:目前患者生命体征平稳,病情稳定。", "bbox": [161, 747, 513, 762]},
	{"text": "出院医嘱及健康指导:", "bbox": [161, 772, 342, 787]},
	{"text": "他院继续治疗。", "bbox": [153, 798, 275, 813]},
	{"text": "/刘佳}", "bbox": [812, 827, 867, 841]},
	{"text": "x", "bbox": [121, 868, 131, 880]},
	{"text": "√", "bbox": [173, 868, 187, 880]},
	{"text": "※", "bbox": [203, 868, 218, 880]},
	{"text": "N", "bbox": [230, 868, 249, 880]},
	{"text": "□", "bbox": [262, 868, 275, 880]},
	{"text": "☐", "bbox": [288, 868, 306, 880]},
	{"text": "I", "bbox": [406, 868, 417, 880]},
	{"text": "II", "bbox": [434, 868, 447, 880]},
	{"text": "III", "bbox": [462, 868, 477, 880]},
	{"text": "IV", "bbox": [490, 868, 506, 880]},
	{"text": "V", "bbox": [519, 868, 534, 880]},
	{"text": "(", "bbox": [613, 868, 623, 880]},
	{"text": "{", "bbox": [642, 868, 653, 880]},
	{"text": "[", "bbox": [672, 868, 680, 880]},
	{"text": "(", "bbox": [725, 868, 736, 880]},
	{"text": "更多", "bbox": [750, 868, 778, 880]}
]
2026-08-10 19:41:54,298 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=14.6s
2026-08-10 19:41:54,298 INFO     29 [qwen-vl-text] coord item[0]: text=中国人民解放军联勤保障部队第九八九医院, bbox=[199, 199, 804, 223]
2026-08-10 19:41:54,298 INFO     29 [qwen-vl-text] coord item[1]: text=姓名:水月强, bbox=[146, 244, 234, 259]
2026-08-10 19:41:54,298 INFO     29 [qwen-vl-text] coord item[2]: text=病区(科):肿瘤科病区, bbox=[271, 244, 444, 259]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[3]: text=床号:11, bbox=[525, 244, 614, 259]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[4]: text=出院记录, bbox=[446, 273, 555, 292]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[5]: text=姓名:, bbox=[165, 303, 225, 318]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[6]: text=性别:男, bbox=[165, 328, 304, 343]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[7]: text=年龄:55岁, bbox=[165, 352, 320, 367]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[8]: text=入院时间:2026-02-22 08:42, bbox=[502, 303, 773, 318]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[9]: text=出院时间:2026-03-02, bbox=[502, 328, 728, 343]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[10]: text=住院天数:8天, bbox=[502, 352, 674, 367]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[11]: text=入院情况:2025年12月无明显诱因出现胸闷,无发热、咳嗽、盗汗不适,未在意。2天前出现咯血,, bbox=[171, 375, 852, 390]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[12]: text=色鲜红,量约10ml,2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大, bbox=[138, 400, 861, 415]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[13]: text=淋巴结,双肺肺气肿,胸骨陈旧性骨折。入院当天再次出现咯血,急诊入院。入院查体:神志清楚,精, bbox=[138, 424, 861, 439]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[14]: text=神好,双肺呼吸音清,未闻及干湿性罗音,心律齐,心音低钝,各瓣膜听诊区未闻及病理性杂音。, bbox=[138, 448, 824, 463]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[15]: text=入院诊断:1、{肺肿物}, bbox=[171, 472, 352, 487]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[16]: text=2、肺气肿, bbox=[254, 497, 334, 511]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[17]: text=诊疗经过:患者入科后查血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝, bbox=[171, 521, 864, 536]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[18]: text=肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。, bbox=[134, 546, 857, 561]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[19]: text=心电图:正常。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气, bbox=[134, 570, 864, 585]
2026-08-10 19:41:54,299 INFO     29 [qwen-vl-text] coord item[20]: text=肿;3.上腹部CT增强未见明显异常。进一步行CT引导下穿刺活检,病理:(左肺穿刺组织)慢性炎症,间, bbox=[134, 595, 864, 610]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[21]: text=质纤维组织增生、淋巴细胞浸润,请结合临床综合考虑。免疫组化结果:CK7(+),TTF-1(+),NapsinA, bbox=[134, 619, 857, 634]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[22]: text=(+),CK-Pan(+),Ki-67(5%),P63(-)。建议患者再次穿刺活检或手术治疗,但家属要求出院,经请, bbox=[134, 644, 864, 660]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[23]: text=示潘雪峰主任后同意,为患者办理出院手续。, bbox=[131, 670, 459, 685]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[24]: text=出院诊断:1、{肺肿物}, bbox=[165, 696, 347, 711]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[25]: text=2、肺气肿, bbox=[250, 722, 327, 737]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[26]: text=出院情况:目前患者生命体征平稳,病情稳定。, bbox=[161, 747, 513, 762]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[27]: text=出院医嘱及健康指导:, bbox=[161, 772, 342, 787]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[28]: text=他院继续治疗。, bbox=[153, 798, 275, 813]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[29]: text=/刘佳}, bbox=[812, 827, 867, 841]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[30]: text=x, bbox=[121, 868, 131, 880]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[31]: text=√, bbox=[173, 868, 187, 880]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[32]: text=※, bbox=[203, 868, 218, 880]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[33]: text=N, bbox=[230, 868, 249, 880]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[34]: text=□, bbox=[262, 868, 275, 880]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[35]: text=☐, bbox=[288, 868, 306, 880]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[36]: text=I, bbox=[406, 868, 417, 880]
2026-08-10 19:41:54,300 INFO     29 [qwen-vl-text] coord item[37]: text=II, bbox=[434, 868, 447, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] coord item[38]: text=III, bbox=[462, 868, 477, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] coord item[39]: text=IV, bbox=[490, 868, 506, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] coord item[40]: text=V, bbox=[519, 868, 534, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] coord item[41]: text=(, bbox=[613, 868, 623, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] coord item[42]: text={, bbox=[642, 868, 653, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] coord item[43]: text=[, bbox=[672, 868, 680, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] coord item[44]: text=(, bbox=[725, 868, 736, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] coord item[45]: text=更多, bbox=[750, 868, 778, 880]
2026-08-10 19:41:54,301 INFO     29 [qwen-vl-text] page=4 — 46/46 coords, api_time=14.6s
2026-08-10 19:41:54,302 INFO     29 [qwen-vl-text] new_positions (46):
[[4, 118.405, 478.38, 167.558, 187.766], [4, 86.86999999999999, 139.23, 205.44799999999998, 218.078], [4, 161.245, 264.18, 205.44799999999998, 218.078], [4, 312.375, 365.33, 205.44799999999998, 218.078], [4, 265.37, 330.22499999999997, 229.86599999999999, 245.864], [4, 98.175, 133.875, 255.126, 267.756], [4, 98.175, 180.88, 276.176, 288.806], [4, 98.175, 190.39999999999998, 296.384, 309.014], [4, 298.69, 459.935, 255.126, 267.756], [4, 298.69, 433.15999999999997, 276.176, 288.806], [4, 298.69, 401.03, 296.384, 309.014], [4, 101.74499999999999, 506.94, 315.75, 328.38], [4, 82.11, 512.295, 336.8, 349.43], [4, 82.11, 512.295, 357.008, 369.638], [4, 82.11, 490.28, 377.216, 389.846], [4, 101.74499999999999, 209.44, 397.424, 410.054], [4, 151.13, 198.73, 418.474, 430.262], [4, 101.74499999999999, 514.0799999999999, 438.68199999999996, 451.312], [4, 79.72999999999999, 509.91499999999996, 459.73199999999997, 472.36199999999997], [4, 79.72999999999999, 514.0799999999999, 479.94, 492.57], [4, 79.72999999999999, 514.0799999999999, 500.99, 513.62], [4, 79.72999999999999, 509.91499999999996, 521.198, 533.828], [4, 79.72999999999999, 514.0799999999999, 542.2479999999999, 555.72], [4, 77.945, 273.10499999999996, 564.14, 576.77], [4, 98.175, 206.465, 586.0319999999999, 598.662], [4, 148.75, 194.565, 607.924, 620.554], [4, 95.795, 305.235, 628.9739999999999, 641.6039999999999], [4, 95.795, 203.48999999999998, 650.024, 662.654], [4, 91.035, 163.625, 671.9159999999999, 684.5459999999999], [4, 483.14, 515.865, 696.334, 708.122], [4, 71.99499999999999, 77.945, 730.856, 740.9599999999999], [4, 102.935, 111.265, 730.856, 740.9599999999999], [4, 120.785, 129.71, 730.856, 740.9599999999999], [4, 136.85, 148.155, 730.856, 740.9599999999999], [4, 155.89, 163.625, 730.856, 740.9599999999999], [4, 171.35999999999999, 182.07, 730.856, 740.9599999999999], [4, 241.57, 248.11499999999998, 730.856, 740.9599999999999], [4, 258.22999999999996, 265.965, 730.856, 740.9599999999999], [4, 274.89, 283.815, 730.856, 740.9599999999999], [4, 291.55, 301.07, 730.856, 740.9599999999999], [4, 308.805, 317.72999999999996, 730.856, 740.9599999999999], [4, 364.73499999999996, 370.685, 730.856, 740.9599999999999], [4, 381.99, 388.53499999999997, 730.856, 740.9599999999999], [4, 399.84, 404.59999999999997, 730.856, 740.9599999999999], [4, 431.375, 437.91999999999996, 730.856, 740.9599999999999], [4, 446.25, 462.90999999999997, 730.856, 740.9599999999999]]
2026-08-10 19:41:54,302 INFO     29 [qwen-vl-text] ═══ DONE ═══ 46 positions, pages=1, time=22.9s
2026-08-10 19:41:54,314 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 19:41:54,314 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:Discharge | outputs={"chunks": "2 items, types={'DischargeRecord': 2}", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:41:54,314 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 19:41:54,319 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:54,319 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:41:55,194 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:55,199 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 19:41:55,199 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:41:55,199 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 19:41:55,204 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:41:55,204 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:41:55,204 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:41:55,204 INFO     29 [qwen-vl-text] positions(40): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:41:55,205 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [40]
2026-08-10 19:41:55,430 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:41:55,432 INFO     29 [qwen-vl-text] LLM extraction start, text_len=901
2026-08-10 19:41:55,432 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:41:55,432 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 39, \"encounter_dates\": [\"2026-03-04\"], \"department\": \"肿瘤科三病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "空军军医大学唐都医院\n查阅电子胶片\nCT检查报告单\nID号：62893718\n检查时间：2026-03-04\n检查号：CT2603030254\n住院\n报告日期：2026-03-04\n影像号：62893718\n姓名\n性别：男\n年龄：55岁\n申请科室：肿瘤科三病区\n床号：\n检查项目：盆腔CT平扫|胸部CT平扫|胸部CT增强|上腹部CT平扫(肝胆胰脾)|下腹部CT平扫\n检查方法：平扫+增强\n影像所见：\n左肺上叶尖后段支气管狭窄，可见不规则团块状软组织密度影，大小约\n4.5×4.0×5.9cm，局部紧贴叶间胸膜，可见“胸膜凹陷征”，平扫CT值约32HU，增\n强扫描呈不均匀强化，两期CT值约33HU、59HU；右肺下叶前基底段可见局限性无肺纹\n理区；余双肺野清晰，肺纹理走行自然，双肺门影不大。气管及纵隔位置居中，纵隔\n可见多发增大淋巴结，较大者短径约0.6cm。心膈影未见异常，双侧胸膜无增厚，未见\n胸腔积液。骨性胸廓骨质结构完整。\n肝随边缘光滑，各叶大小比例正常，肝实质内密度均匀，未见明显异常密度影及\n占位性病变，肝内外胆管未见扩张，肝门部结构清晰，未见占位性病变，胆囊不大，\n壁薄且均匀，腔内未见阳性结石影。胰腺大小、形态及密度未见异常。脾不大，实质\n密度均匀，双肾大小形态良好，实质密度均匀，双侧肾盂未见扩张，右肾可见阳性结\n石影。腹腔内及腹膜后未见明显肿大淋巴结影，未见腹水征象。\n膀胱充盈良好，壁厚薄均匀，未见占位性病变。前列腺大小、形态及密度未见异\n常。双侧精囊腺大小、形态及密度未见异常。直肠形态正常，未见占位性病变。盆腔\n淋巴结无肿大，盆腔内未见积液征象。\n诊断意见：\n1、左肺上叶尖后段占位性病变，多考虑周围型肺癌；纵隔多发增大淋巴结；\n2、右肾结石；肝、胆、胰、脾及左肾CT扫描未见明显异常。\n3、膀胱、前列腺、双侧精囊腺及直肠CT扫描未见明确病变。\n本意见仅供临床医生参考，盖章或签字后生效！\n报告医师：杨露\n审核医师：\n该信息经过北京CA数字签名认证\n签名验证的信息摘要值为：3BFB10562BBC74DF5F886274A0100FAG。检查号：CT2603030254。",
    "role": "user"
  }
]
2026-08-10 19:42:02,396 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:42:02,397 INFO     29 [qwen-vl-text] LLM output (len=933):
{
  "exam_date": "2026-03-04",
  "report_date": "2026-03-04",
  "exam_name": "盆腔CT平扫|胸部CT平扫|胸部CT增强|上腹部CT平扫(肝胆胰脾)|下腹部CT平扫",
  "exam_category": "imaging",
  "body_part": "盆腔|胸部|上腹部|下腹部",
  "patient_name": null,
  "patient_gender": "男",
  "department": "肿瘤科三病区",
  "bed_number": null,
  "findings": "左肺上叶尖后段支气管狭窄，可见不规则团块状软组织密度影，大小约4.5×4.0×5.9cm，局部紧贴叶间胸膜，可见“胸膜凹陷征”，平扫CT值约32HU，增强扫描呈不均匀强化，两期CT值约33HU、59HU；右肺下叶前基底段可见局限性无肺纹理区；余双肺野清晰，肺纹理走行自然，双肺门影不大。气管及纵隔位置居中，纵隔可见多发增大淋巴结，较大者短径约0.6cm。心膈影未见异常，双侧胸膜无增厚，未见胸腔积液。骨性胸廓骨质结构完整。\n肝随边缘光滑，各叶大小比例正常，肝实质内密度均匀，未见明显异常密度影及占位性病变，肝内外胆管未见扩张，肝门部结构清晰，未见占位性病变，胆囊不大，壁薄且均匀，腔内未见阳性结石影。胰腺大小、形态及密度未见异常。脾不大，实质密度均匀，双肾大小形态良好，实质密度均匀，双侧肾盂未见扩张，右肾可见阳性结石影。腹腔内及腹膜后未见明显肿大淋巴结影，未见腹水征象。\n膀胱充盈良好，壁厚薄均匀，未见占位性病变。前列腺大小、形态及密度未见异常。双侧精囊腺大小、形态及密度未见异常。直肠形态正常，未见占位性病变。盆腔淋巴结无肿大，盆腔内未见积液征象。",
  "conclusion": "1、左肺上叶尖后段占位性病变，多考虑周围型肺癌；纵隔多发增大淋巴结；\n2、右肾结石；肝、胆、胰、脾及左肾CT扫描未见明显异常。\n3、膀胱、前列腺、双侧精囊腺及直肠CT扫描未见明确病变。",
  "physician": "杨露",
  "reviewer": null
}
2026-08-10 19:42:02,402 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2311400, prompt_len=1634
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["空军军医大学唐都医院", "查阅电子胶片", "CT检查报告单", "ID号：62893718", "检查时间：2026-03-04", "检查号：CT2603030254", "住院", "报告日期：2026-03-04", "影像号：62893718", "姓名", "性别：男", "年龄：55岁", "申请科室：肿瘤科三病区", "床号：", "检查项目：盆腔CT平扫|胸部CT平扫|胸部CT增强|上腹部CT平扫(肝胆胰脾)|下腹部CT平扫", "检查方法：平扫+增强", "影像所见：", "左肺上叶尖后段支气管狭窄，可见不规则团块状软组织密度影，大小约", "4.5×4.0×5.9cm，局部紧贴叶间胸膜，可见“胸膜凹陷征”，平扫CT值约32HU，增", "强扫描呈不均匀强化，两期CT值约33HU、59HU；右肺下叶前基底段可见局限性无肺纹", "理区；余双肺野清晰，肺纹理走行自然，双肺门影不大。气管及纵隔位置居中，纵隔", "可见多发增大淋巴结，较大者短径约0.6cm。心膈影未见异常，双侧胸膜无增厚，未见", "胸腔积液。骨性胸廓骨质结构完整。", "肝随边缘光滑，各叶大小比例正常，肝实质内密度均匀，未见明显异常密度影及", "占位性病变，肝内外胆管未见扩张，肝门部结构清晰，未见占位性病变，胆囊不大，", "壁薄且均匀，腔内未见阳性结石影。胰腺大小、形态及密度未见异常。脾不大，实质", "密度均匀，双肾大小形态良好，实质密度均匀，双侧肾盂未见扩张，右肾可见阳性结", "石影。腹腔内及腹膜后未见明显肿大淋巴结影，未见腹水征象。", "膀胱充盈良好，壁厚薄均匀，未见占位性病变。前列腺大小、形态及密度未见异", "常。双侧精囊腺大小、形态及密度未见异常。直肠形态正常，未见占位性病变。盆腔", "淋巴结无肿大，盆腔内未见积液征象。", "诊断意见：", "1、左肺上叶尖后段占位性病变，多考虑周围型肺癌；纵隔多发增大淋巴结；", "2、右肾结石；肝、胆、胰、脾及左肾CT扫描未见明显异常。", "3、膀胱、前列腺、双侧精囊腺及直肠CT扫描未见明确病变。", "本意见仅供临床医生参考，盖章或签字后生效！", "报告医师：杨露", "审核医师：", "该信息经过北京CA数字签名认证", "签名验证的信息摘要值为：3BFB10562BBC74DF5F886274A0100FAG。检查号：CT2603030254。"]

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
2026-08-10 19:42:16,330 INFO     29 [qwen-vl-text] coord API raw response (len=2646):
[
	{"text": "空军军医大学唐都医院", "bbox": [277, 44, 698, 76]},
	{"text": "查阅电子胶片", "bbox": [43, 98, 151, 113]},
	{"text": "CT检查报告单", "bbox": [408, 120, 580, 141]},
	{"text": "ID号：62893718", "bbox": [43, 158, 192, 176]},
	{"text": "检查时间：2026-03-04", "bbox": [343, 155, 550, 171]},
	{"text": "检查号：CT2603030254", "bbox": [701, 153, 902, 169]},
	{"text": "住院", "bbox": [45, 179, 104, 195]},
	{"text": "报告日期：2026-03-04", "bbox": [343, 175, 550, 190]},
	{"text": "影像号：62893718", "bbox": [701, 172, 860, 188]},
	{"text": "姓名", "bbox": [48, 202, 91, 218]},
	{"text": "性别：男", "bbox": [234, 199, 314, 214]},
	{"text": "年龄：55岁", "bbox": [368, 197, 474, 212]},
	{"text": "申请科室：肿瘤科三病区", "bbox": [527, 195, 745, 210]},
	{"text": "床号：", "bbox": [797, 194, 844, 208]},
	{"text": "检查项目：盆腔CT平扫|胸部CT平扫|胸部CT增强|上腹部CT平扫(肝胆胰脾)|下腹部CT平扫", "bbox": [52, 214, 890, 238]},
	{"text": "检查方法：平扫+增强", "bbox": [58, 247, 291, 264]},
	{"text": "影像所见：", "bbox": [65, 276, 168, 294]},
	{"text": "左肺上叶尖后段支气管狭窄，可见不规则团块状软组织密度影，大小约", "bbox": [120, 300, 819, 324]},
	{"text": "4.5×4.0×5.9cm，局部紧贴叶间胸膜，可见“胸膜凹陷征”，平扫CT值约32HU，增", "bbox": [80, 321, 908, 348]},
	{"text": "强扫描呈不均匀强化，两期CT值约33HU、59HU；右肺下叶前基底段可见局限性无肺纹", "bbox": [88, 343, 907, 369]},
	{"text": "理区；余双肺野清晰，肺纹理走行自然，双肺门影不大。气管及纵隔位置居中，纵隔", "bbox": [95, 364, 892, 389]},
	{"text": "可见多发增大淋巴结，较大者短径约0.6cm。心膈影未见异常，双侧胸膜无增厚，未见", "bbox": [103, 384, 895, 408]},
	{"text": "胸腔积液。骨性胸廓骨质结构完整。", "bbox": [110, 407, 436, 425]},
	{"text": "肝随边缘光滑，各叶大小比例正常，肝实质内密度均匀，未见明显异常密度影及", "bbox": [159, 422, 872, 441]},
	{"text": "占位性病变，肝内外胆管未见扩张，肝门部结构清晰，未见占位性病变，胆囊不大，", "bbox": [127, 440, 858, 460]},
	{"text": "壁薄且均匀，腔内未见阳性结石影。胰腺大小、形态及密度未见异常。脾不大，实质", "bbox": [126, 459, 870, 478]},
	{"text": "密度均匀，双肾大小形态良好，实质密度均匀，双侧肾盂未见扩张，右肾可见阳性结", "bbox": [121, 478, 875, 497]},
	{"text": "石影。腹腔内及腹膜后未见明显肿大淋巴结影，未见腹水征象。", "bbox": [115, 497, 683, 515]},
	{"text": "膀胱充盈良好，壁厚薄均匀，未见占位性病变。前列腺大小、形态及密度未见异", "bbox": [151, 517, 885, 535]},
	{"text": "常。双侧精囊腺大小、形态及密度未见异常。直肠形态正常，未见占位性病变。盆腔", "bbox": [105, 536, 890, 555]},
	{"text": "淋巴结无肿大，盆腔内未见积液征象。", "bbox": [98, 558, 455, 577]},
	{"text": "诊断意见：", "bbox": [93, 587, 189, 604]},
	{"text": "1、左肺上叶尖后段占位性病变，多考虑周围型肺癌；纵隔多发增大淋巴结；", "bbox": [131, 615, 858, 634]},
	{"text": "2、右肾结石；肝、胆、胰、脾及左肾CT扫描未见明显异常。", "bbox": [127, 638, 719, 658]},
	{"text": "3、膀胱、前列腺、双侧精囊腺及直肠CT扫描未见明确病变。", "bbox": [124, 663, 721, 682]},
	{"text": "本意见仅供临床医生参考，盖章或签字后生效！", "bbox": [56, 851, 371, 866]},
	{"text": "报告医师：杨露", "bbox": [417, 847, 585, 866]},
	{"text": "审核医师：", "bbox": [684, 844, 790, 865]},
	{"text": "该信息经过北京CA数字签名认证", "bbox": [52, 875, 275, 890]},
	{"text": "签名验证的信息摘要值为：3BFB10562BBC74DF5F886274A0100FAG。检查号：CT2603030254。", "bbox": [324, 873, 952, 890]}
]
2026-08-10 19:42:16,331 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=13.9s
2026-08-10 19:42:16,331 INFO     29 [qwen-vl-text] coord item[0]: text=空军军医大学唐都医院, bbox=[277, 44, 698, 76]
2026-08-10 19:42:16,331 INFO     29 [qwen-vl-text] coord item[1]: text=查阅电子胶片, bbox=[43, 98, 151, 113]
2026-08-10 19:42:16,331 INFO     29 [qwen-vl-text] coord item[2]: text=CT检查报告单, bbox=[408, 120, 580, 141]
2026-08-10 19:42:16,331 INFO     29 [qwen-vl-text] coord item[3]: text=ID号：62893718, bbox=[43, 158, 192, 176]
2026-08-10 19:42:16,331 INFO     29 [qwen-vl-text] coord item[4]: text=检查时间：2026-03-04, bbox=[343, 155, 550, 171]
2026-08-10 19:42:16,331 INFO     29 [qwen-vl-text] coord item[5]: text=检查号：CT2603030254, bbox=[701, 153, 902, 169]
2026-08-10 19:42:16,332 INFO     29 [qwen-vl-text] coord item[6]: text=住院, bbox=[45, 179, 104, 195]
2026-08-10 19:42:16,332 INFO     29 [qwen-vl-text] coord item[7]: text=报告日期：2026-03-04, bbox=[343, 175, 550, 190]
2026-08-10 19:42:16,332 INFO     29 [qwen-vl-text] coord item[8]: text=影像号：62893718, bbox=[701, 172, 860, 188]
2026-08-10 19:42:16,332 INFO     29 [qwen-vl-text] coord item[9]: text=姓名, bbox=[48, 202, 91, 218]
2026-08-10 19:42:16,332 INFO     29 [qwen-vl-text] coord item[10]: text=性别：男, bbox=[234, 199, 314, 214]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[11]: text=年龄：55岁, bbox=[368, 197, 474, 212]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[12]: text=申请科室：肿瘤科三病区, bbox=[527, 195, 745, 210]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[13]: text=床号：, bbox=[797, 194, 844, 208]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[14]: text=检查项目：盆腔CT平扫|胸部CT平扫|胸部CT增强|上腹部CT平扫(肝胆胰脾)|下腹部CT平扫, bbox=[52, 214, 890, 238]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[15]: text=检查方法：平扫+增强, bbox=[58, 247, 291, 264]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[16]: text=影像所见：, bbox=[65, 276, 168, 294]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[17]: text=左肺上叶尖后段支气管狭窄，可见不规则团块状软组织密度影，大小约, bbox=[120, 300, 819, 324]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[18]: text=4.5×4.0×5.9cm，局部紧贴叶间胸膜，可见“胸膜凹陷征”，平扫CT值约32HU，增, bbox=[80, 321, 908, 348]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[19]: text=强扫描呈不均匀强化，两期CT值约33HU、59HU；右肺下叶前基底段可见局限性无肺纹, bbox=[88, 343, 907, 369]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[20]: text=理区；余双肺野清晰，肺纹理走行自然，双肺门影不大。气管及纵隔位置居中，纵隔, bbox=[95, 364, 892, 389]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[21]: text=可见多发增大淋巴结，较大者短径约0.6cm。心膈影未见异常，双侧胸膜无增厚，未见, bbox=[103, 384, 895, 408]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[22]: text=胸腔积液。骨性胸廓骨质结构完整。, bbox=[110, 407, 436, 425]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[23]: text=肝随边缘光滑，各叶大小比例正常，肝实质内密度均匀，未见明显异常密度影及, bbox=[159, 422, 872, 441]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[24]: text=占位性病变，肝内外胆管未见扩张，肝门部结构清晰，未见占位性病变，胆囊不大，, bbox=[127, 440, 858, 460]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[25]: text=壁薄且均匀，腔内未见阳性结石影。胰腺大小、形态及密度未见异常。脾不大，实质, bbox=[126, 459, 870, 478]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[26]: text=密度均匀，双肾大小形态良好，实质密度均匀，双侧肾盂未见扩张，右肾可见阳性结, bbox=[121, 478, 875, 497]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[27]: text=石影。腹腔内及腹膜后未见明显肿大淋巴结影，未见腹水征象。, bbox=[115, 497, 683, 515]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[28]: text=膀胱充盈良好，壁厚薄均匀，未见占位性病变。前列腺大小、形态及密度未见异, bbox=[151, 517, 885, 535]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[29]: text=常。双侧精囊腺大小、形态及密度未见异常。直肠形态正常，未见占位性病变。盆腔, bbox=[105, 536, 890, 555]
2026-08-10 19:42:16,333 INFO     29 [qwen-vl-text] coord item[30]: text=淋巴结无肿大，盆腔内未见积液征象。, bbox=[98, 558, 455, 577]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[31]: text=诊断意见：, bbox=[93, 587, 189, 604]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[32]: text=1、左肺上叶尖后段占位性病变，多考虑周围型肺癌；纵隔多发增大淋巴结；, bbox=[131, 615, 858, 634]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[33]: text=2、右肾结石；肝、胆、胰、脾及左肾CT扫描未见明显异常。, bbox=[127, 638, 719, 658]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[34]: text=3、膀胱、前列腺、双侧精囊腺及直肠CT扫描未见明确病变。, bbox=[124, 663, 721, 682]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[35]: text=本意见仅供临床医生参考，盖章或签字后生效！, bbox=[56, 851, 371, 866]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[36]: text=报告医师：杨露, bbox=[417, 847, 585, 866]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[37]: text=审核医师：, bbox=[684, 844, 790, 865]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[38]: text=该信息经过北京CA数字签名认证, bbox=[52, 875, 275, 890]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] coord item[39]: text=签名验证的信息摘要值为：3BFB10562BBC74DF5F886274A0100FAG。检查号：CT2603030254。, bbox=[324, 873, 952, 890]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] page=0 — 40/40 coords, api_time=13.9s
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] new_positions (40):
[[0, 164.815, 415.31, 37.048, 63.992], [0, 25.584999999999997, 89.845, 82.51599999999999, 95.146], [0, 242.76, 345.09999999999997, 101.03999999999999, 118.722], [0, 25.584999999999997, 114.24, 133.036, 148.192], [0, 204.08499999999998, 327.25, 130.51, 143.982], [0, 417.09499999999997, 536.6899999999999, 128.826, 142.298], [0, 26.775, 61.879999999999995, 150.718, 164.19], [0, 204.08499999999998, 327.25, 147.35, 159.98], [0, 417.09499999999997, 511.7, 144.82399999999998, 158.296], [0, 28.56, 54.144999999999996, 170.084, 183.55599999999998], [0, 139.23, 186.82999999999998, 167.558, 180.188], [0, 218.95999999999998, 282.03, 165.874, 178.504], [0, 313.565, 443.275, 164.19, 176.82], [0, 474.215, 502.17999999999995, 163.34799999999998, 175.136], [0, 30.939999999999998, 529.55, 180.188, 200.396], [0, 34.51, 173.14499999999998, 207.974, 222.28799999999998], [0, 38.675, 99.96, 232.392, 247.548], [0, 71.39999999999999, 487.30499999999995, 252.6, 272.808], [0, 47.599999999999994, 540.26, 270.282, 293.01599999999996], [0, 52.36, 539.665, 288.806, 310.698], [0, 56.525, 530.74, 306.488, 327.538], [0, 61.285, 532.525, 323.328, 343.536], [0, 65.45, 259.42, 342.69399999999996, 357.84999999999997], [0, 94.60499999999999, 518.84, 355.324, 371.322], [0, 75.565, 510.51, 370.47999999999996, 387.32], [0, 74.97, 517.65, 386.478, 402.476], [0, 71.99499999999999, 520.625, 402.476, 418.474], [0, 68.425, 406.385, 418.474, 433.63], [0, 89.845, 526.5749999999999, 435.31399999999996, 450.46999999999997], [0, 62.474999999999994, 529.55, 451.312, 467.31], [0, 58.309999999999995, 270.72499999999997, 469.83599999999996, 485.834], [0, 55.335, 112.455, 494.25399999999996, 508.568], [0, 77.945, 510.51, 517.8299999999999, 533.828], [0, 75.565, 427.805, 537.196, 554.036], [0, 73.78, 428.995, 558.246, 574.244], [0, 33.32, 220.74499999999998, 716.542, 729.172], [0, 248.11499999999998, 348.075, 713.174, 729.172], [0, 406.97999999999996, 470.04999999999995, 710.648, 728.3299999999999], [0, 30.939999999999998, 163.625, 736.75, 749.38], [0, 192.78, 566.4399999999999, 735.066, 749.38]]
2026-08-10 19:42:16,334 INFO     29 [qwen-vl-text] ═══ DONE ═══ 40 positions, pages=1, time=21.1s
2026-08-10 19:42:16,335 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 19:42:16,337 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 19:42:16,338 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 19:42:16,338 INFO     29 [qwen-vl-text] positions(25): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 19:42:16,338 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [25]
2026-08-10 19:42:16,530 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 19:42:16,531 INFO     29 [qwen-vl-text] LLM extraction start, text_len=344
2026-08-10 19:42:16,531 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:42:16,531 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 74, \"bbox_end\": 98, \"encounter_dates\": [\"2026-03-06\"], \"department\": \"肿瘤科三病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "空军军医大学第二附属医院(唐都医院)\n病理图文诊断报告单\n病理号: 2610441\nID号: 62893718\n住院号:\n姓名\n性别: 男\n年龄: 55\n送检单位: 唐都医院\n科室: 肿瘤科三病区\n床号:\n送检日期: 2026-03-05\n报告时间: 2026-03-06\n肉眼所见:\n支气管镜活检标本。\n光镜所见:\n病理诊断:\n(左肺上叶尖段)鳞状上皮中-重度异型增生并局部癌变(鳞状细胞癌)。\n[注: 此例仅为小组织活检标本, 有一定局限性, 有可能不能代表病变全貌特征]\n初诊医师: 苟晨靓 签名:\n苟晨靓\n主诊医师: 富金 签名:\n富金\n此报告签名医生信息已经过北京CA数字认证, 涂改无效。如对此报告有任何疑问, 请立即与病理科联系。\n此报告仅此一份, 请妥善保管, 遗失不补。",
    "role": "user"
  }
]
2026-08-10 19:42:16,533 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T19:42:16.532+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 92, "failed": 0, "current": {"73b6bae694f211f1bd9827cf206dfa2d": {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 19:42:22,610 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:42:22,610 INFO     29 [qwen-vl-text] LLM output (len=421):
{
  "exam_date": "2026-03-05",
  "report_date": "2026-03-06",
  "exam_name": "病理图文诊断报告单",
  "exam_category": "pathology",
  "body_part": "左肺上叶尖段",
  "patient_name": null,
  "patient_gender": "男",
  "department": "肿瘤科三病区",
  "bed_number": null,
  "findings": "肉眼所见:\n支气管镜活检标本。",
  "conclusion": "病理诊断:\n(左肺上叶尖段)鳞状上皮中-重度异型增生并局部癌变(鳞状细胞癌)。\n[注: 此例仅为小组织活检标本, 有一定局限性, 有可能不能代表病变全貌特征]",
  "physician": "苟晨靓",
  "reviewer": "富金"
}
2026-08-10 19:42:22,616 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3283430, prompt_len=1032
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["空军军医大学第二附属医院(唐都医院)", "病理图文诊断报告单", "病理号: 2610441", "ID号: 62893718", "住院号:", "姓名", "性别: 男", "年龄: 55", "送检单位: 唐都医院", "科室: 肿瘤科三病区", "床号:", "送检日期: 2026-03-05", "报告时间: 2026-03-06", "肉眼所见:", "支气管镜活检标本。", "光镜所见:", "病理诊断:", "(左肺上叶尖段)鳞状上皮中-重度异型增生并局部癌变(鳞状细胞癌)。", "[注: 此例仅为小组织活检标本, 有一定局限性, 有可能不能代表病变全貌特征]", "初诊医师: 苟晨靓 签名:", "苟晨靓", "主诊医师: 富金 签名:", "富金", "此报告签名医生信息已经过北京CA数字认证, 涂改无效。如对此报告有任何疑问, 请立即与病理科联系。", "此报告仅此一份, 请妥善保管, 遗失不补。"]

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
2026-08-10 19:42:33,129 INFO     29 [qwen-vl-text] coord API raw response (len=1444):
[
	{"text": "空军军医大学第二附属医院(唐都医院)", "bbox": [220, 63, 752, 98]},
	{"text": "病理图文诊断报告单", "bbox": [358, 94, 569, 115]},
	{"text": "病理号: 2610441", "bbox": [129, 130, 274, 144]},
	{"text": "ID号: 62893718", "bbox": [368, 134, 505, 148]},
	{"text": "住院号:", "bbox": [635, 142, 695, 155]},
	{"text": "姓名", "bbox": [130, 153, 158, 167]},
	{"text": "性别: 男", "bbox": [367, 156, 450, 170]},
	{"text": "年龄: 55", "bbox": [637, 163, 716, 176]},
	{"text": "送检单位: 唐都医院", "bbox": [130, 178, 296, 192]},
	{"text": "科室: 肿瘤科三病区", "bbox": [367, 180, 539, 194]},
	{"text": "床号:", "bbox": [637, 185, 680, 198]},
	{"text": "送检日期: 2026-03-05", "bbox": [132, 204, 309, 218]},
	{"text": "报告时间: 2026-03-06", "bbox": [638, 208, 810, 223]},
	{"text": "肉眼所见:", "bbox": [134, 230, 212, 244]},
	{"text": "支气管镜活检标本。", "bbox": [140, 250, 290, 265]},
	{"text": "光镜所见:", "bbox": [140, 316, 218, 330]},
	{"text": "病理诊断:", "bbox": [124, 592, 207, 607]},
	{"text": "(左肺上叶尖段)鳞状上皮中-重度异型增生并局部癌变(鳞状细胞癌)。", "bbox": [137, 608, 725, 624]},
	{"text": "[注: 此例仅为小组织活检标本, 有一定局限性, 有可能不能代表病变全貌特征]", "bbox": [130, 648, 780, 666]},
	{"text": "初诊医师: 苟晨靓 签名:", "bbox": [135, 835, 352, 851]},
	{"text": "苟晨靓", "bbox": [385, 835, 478, 863]},
	{"text": "主诊医师: 富金 签名:", "bbox": [487, 835, 621, 851]},
	{"text": "富金", "bbox": [755, 835, 798, 856]},
	{"text": "此报告签名医生信息已经过北京CA数字认证, 涂改无效。如对此报告有任何疑问, 请立即与病理科联系。", "bbox": [119, 863, 830, 879]},
	{"text": "此报告仅此一份, 请妥善保管, 遗失不补。", "bbox": [118, 883, 408, 898]}
]
2026-08-10 19:42:33,130 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=10.5s
2026-08-10 19:42:33,130 INFO     29 [qwen-vl-text] coord item[0]: text=空军军医大学第二附属医院(唐都医院), bbox=[220, 63, 752, 98]
2026-08-10 19:42:33,130 INFO     29 [qwen-vl-text] coord item[1]: text=病理图文诊断报告单, bbox=[358, 94, 569, 115]
2026-08-10 19:42:33,130 INFO     29 [qwen-vl-text] coord item[2]: text=病理号: 2610441, bbox=[129, 130, 274, 144]
2026-08-10 19:42:33,130 INFO     29 [qwen-vl-text] coord item[3]: text=ID号: 62893718, bbox=[368, 134, 505, 148]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[4]: text=住院号:, bbox=[635, 142, 695, 155]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[130, 153, 158, 167]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[6]: text=性别: 男, bbox=[367, 156, 450, 170]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[7]: text=年龄: 55, bbox=[637, 163, 716, 176]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[8]: text=送检单位: 唐都医院, bbox=[130, 178, 296, 192]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[9]: text=科室: 肿瘤科三病区, bbox=[367, 180, 539, 194]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[10]: text=床号:, bbox=[637, 185, 680, 198]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[11]: text=送检日期: 2026-03-05, bbox=[132, 204, 309, 218]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[12]: text=报告时间: 2026-03-06, bbox=[638, 208, 810, 223]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[13]: text=肉眼所见:, bbox=[134, 230, 212, 244]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[14]: text=支气管镜活检标本。, bbox=[140, 250, 290, 265]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[15]: text=光镜所见:, bbox=[140, 316, 218, 330]
2026-08-10 19:42:33,131 INFO     29 [qwen-vl-text] coord item[16]: text=病理诊断:, bbox=[124, 592, 207, 607]
2026-08-10 19:42:33,132 INFO     29 [qwen-vl-text] coord item[17]: text=(左肺上叶尖段)鳞状上皮中-重度异型增生并局部癌变(鳞状细胞癌)。, bbox=[137, 608, 725, 624]
2026-08-10 19:42:33,132 INFO     29 [qwen-vl-text] coord item[18]: text=[注: 此例仅为小组织活检标本, 有一定局限性, 有可能不能代表病变全貌特征], bbox=[130, 648, 780, 666]
2026-08-10 19:42:33,132 INFO     29 [qwen-vl-text] coord item[19]: text=初诊医师: 苟晨靓 签名:, bbox=[135, 835, 352, 851]
2026-08-10 19:42:33,132 INFO     29 [qwen-vl-text] coord item[20]: text=苟晨靓, bbox=[385, 835, 478, 863]
2026-08-10 19:42:33,132 INFO     29 [qwen-vl-text] coord item[21]: text=主诊医师: 富金 签名:, bbox=[487, 835, 621, 851]
2026-08-10 19:42:33,132 INFO     29 [qwen-vl-text] coord item[22]: text=富金, bbox=[755, 835, 798, 856]
2026-08-10 19:42:33,132 INFO     29 [qwen-vl-text] coord item[23]: text=此报告签名医生信息已经过北京CA数字认证, 涂改无效。如对此报告有任何疑问, 请立即与病理科联系。, bbox=[119, 863, 830, 879]
2026-08-10 19:42:33,132 INFO     29 [qwen-vl-text] coord item[24]: text=此报告仅此一份, 请妥善保管, 遗失不补。, bbox=[118, 883, 408, 898]
2026-08-10 19:42:33,133 INFO     29 [qwen-vl-text] page=2 — 25/25 coords, api_time=10.5s
2026-08-10 19:42:33,133 INFO     29 [qwen-vl-text] new_positions (25):
[[2, 130.9, 447.44, 53.046, 82.51599999999999], [2, 213.01, 338.555, 79.148, 96.83], [2, 76.755, 163.03, 109.46, 121.24799999999999], [2, 218.95999999999998, 300.47499999999997, 112.828, 124.616], [2, 377.825, 413.525, 119.564, 130.51], [2, 77.35, 94.00999999999999, 128.826, 140.614], [2, 218.36499999999998, 267.75, 131.352, 143.14], [2, 379.015, 426.02, 137.246, 148.192], [2, 77.35, 176.12, 149.876, 161.664], [2, 218.36499999999998, 320.705, 151.56, 163.34799999999998], [2, 379.015, 404.59999999999997, 155.76999999999998, 166.716], [2, 78.53999999999999, 183.855, 171.768, 183.55599999999998], [2, 379.60999999999996, 481.95, 175.136, 187.766], [2, 79.72999999999999, 126.14, 193.66, 205.44799999999998], [2, 83.3, 172.54999999999998, 210.5, 223.13], [2, 83.3, 129.71, 266.072, 277.86], [2, 73.78, 123.16499999999999, 498.464, 511.094], [2, 81.515, 431.375, 511.936, 525.408], [2, 77.35, 464.09999999999997, 545.616, 560.7719999999999], [2, 80.325, 209.44, 703.0699999999999, 716.542], [2, 229.075, 284.40999999999997, 703.0699999999999, 726.646], [2, 289.765, 369.495, 703.0699999999999, 716.542], [2, 449.22499999999997, 474.81, 703.0699999999999, 720.752], [2, 70.80499999999999, 493.84999999999997, 726.646, 740.1179999999999], [2, 70.21, 242.76, 743.486, 756.116]]
2026-08-10 19:42:33,133 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=16.8s
2026-08-10 19:42:33,146 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 19:42:33,146 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:42:33,146 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 19:42:33,151 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:42:33,151 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 19:42:34,164 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 19:42:34,175 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 19:42:34,175 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "376 items", "markdown": "", "text": "", "name": "SYQI肺鳞癌.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "11 items, types={'LabReport': 11}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_LabExam\": 11, \"chunks_Discharge\": 2}"}
2026-08-10 19:42:34,175 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 19:42:34,176 INFO     29 [ChunkMerger] Merged 15 chunks from 9 sources: {'Extractor:LabExam': 11, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 2, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 19:42:34,186 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 19:42:34,186 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "15 items, types={'LabReport': 11, 'DischargeRecord': 2, 'ExaminationReport': 2}", "name": "SYQI肺鳞癌.pdf"}
2026-08-10 19:42:34,187 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 19:42:34,311 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786390447150, 'update_date': datetime.datetime(2026, 8, 10, 19, 34, 7), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1423393, 'status': '1'}
2026-08-10 19:42:34,533 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   血糖(空腹)(8-HR)  GLU  5.56  mmol/L  3.9-6.1  False    钾(8-HR)  K  4.36  mmol/L  3.5-5.3  False    钠(8-HR)  Na  137.8  mmol/L  137-147  False    氯(8-HR)  Cl  100.9  mmol/L  99-110  False    总蛋白(8-HR)  TP  73.0  g/L  65-85  False    白蛋白(8-HR)  ALB  42.4  g/L  40-55  False    球蛋白  GLO  30.6  g/L  20-40  False    白球比  A/G  1.4  None  1.2-2.4  False    总胆红素(8-HR)  T-BIL  12.1  μmol/L  0-26  False    直接胆红素(8-HR)  D-BIL  3.5  μmol/L  0-6.8  False    间接胆红素  I-BIL  8.6  μmol/L  0-14  False    丙氨酸氨基转移酶(8-HR)  ALT  26  U/L  9-50  False    天门冬氨酸氨基转移酶(8-HR)  AST  21  U/L  15-40  False    AST/ALT  None  0.81  None  None  False    碱性磷酸酶(8-HR)  ALP  106  U/L  45-125  False    总胆汁酸(陕HR)  TBA  12.6  μmol/L  0-10  True    胆碱酯酶(陕HR)  CHE  6970  U/L  5000-12000  False    γ-谷氨酰转移酶(8-HR)  GGT  23  U/L  10-60  False    eGFR(CKD-EPI)  eGFR  93.12  ml/min/1.73m2  >90  False    尿酸(8-HR)  UA  263.0  μmol/L  208-428  False    尿素(8-HR)  UREA  6.7  mmol/L  3.1-8.0  False    肌酐(8-HR)  CRE  81.0  μmol/L  57-97  False    肌酸激酶(8-HR)  CK  84  U/L  50-310  False    肌酸激酶同功酶  CK-MB  12.43  U/L  <25  False    乳酸脱氢酶(8-HR)  LDH  186  U/L  120-250  False    α-羟丁酸脱氢酶(陕HR)  α-HBDH  140  U/L  72-182  False    钙(8-HR)  Ca  2.26  mmol/L  2.2-2.7  False   
---
   白细胞计数  WBC  9.63  10⁹/L  3.5-9.5  True    红细胞计数  RBC  4.36  10¹²/L  4.3-5.8  False    血红蛋白  HGB  141  g/L  130-175  False    红细胞比积  HCT  42.7  %  40-50  False    平均红细胞体积  MCV  97.9  fL  82-100  False    平均血红蛋白量  MCH  32.4  pg  27-34  False    平均血红蛋白浓度  MCHC  330.0  g/L  316-354  False    血小板计数  PLT  268  10⁹/L  100-350  False    淋巴细胞比例  LYMPH%  15.3  %  20-50  True    单核细胞比例  MONO%  6.1  %  3-10  False    中性粒细胞比例  NEUT%  71.5  %  40-75  False    嗜酸性细胞比例  E0%  6.7  %  0.4-8  False    嗜碱性细胞比例  BASO%  0.4  %  0-1  False    淋巴细胞计数  LYMPH#  1.47  10⁹/L  1.1-3.2  False    单核细胞计数  MONO#  0.6  10⁹/L  0.1-0.6  False    中性粒细胞计数  NEUT#  6.88  10⁹/L  1.8-6.3  True    嗜酸性细胞计数  E0#  0.65  10⁹/L  0.02-0.62  True    嗜碱性细胞计数  BASO#  0.04  10⁹/L  0-0.06  False    红细胞分布宽度CV  RDW-CV  14.0  %  11-15.5  False    红细胞分布宽度SD  RDW-SD  49.5  fL  37-50  False    血小板压积  PCT  0.28  None  0.11-0.28  False    平均血小板体积  MPV  10.4  fL  6-13  False    血小板分布宽度  PDW  16.4  fL  9-17  False    大血小板比例  P-LCR  28.6  %  13-43  False    幼稚粒细胞绝对值  IGM  0.01  10⁹/L  0-0.06  False    幼稚粒细胞百分比  IGC  0.10  %  0-0.6  False   
---
   凝血酶原时间  PT-1  10.4  SEC  9.2-13.9  False    PT报告活动度  PIR-1  117  %  70-130  False    国际标准化比值（INR）  INR  0.88  None  0.8-1.2  False    活化部分凝血活酶时间(APTT)  APTT-1  33.3  sec  21.2-35.7  False    纤维蛋白原  FIB  3.7  g/L  2-4  False    凝血酶时间  TT-1  14.8  sec  10.2-20.1  False    D-二聚体  D-DIMER-1  446  ug/L  0-550  False   
---
   乙肝肝炎病毒表面抗原  HBsAg  阴性  None  阴性  False    乙肝肝炎病毒表面抗体  HBsAb  阳性(+)  None  阴性-阳性  False    乙肝肝炎病毒e抗原  HBeAg  阴性  None  阴性  False    乙肝肝炎病毒e抗体  HBeAb  阴性  None  阴性  False    乙肝肝炎病毒核心抗体(IgG)  HBcAb  弱阳性(±)  None  阴性  True    梅毒螺旋体特异抗体(酶免)  TP-Ab  阴性  None  阴性  False    人类免疫缺陷病毒抗体  HIV-Ab  阴性  None  阴性  False    丙肝肝炎病毒抗体  HCV-Ab  阴性  None  阴性  False   
---
   白细胞计数(8-HR)  WBC  11.44  E+09/L  3.5-9.5  True    淋巴细胞百分率  LYMPH%  14.4  %  20-50  True    单核细胞百分率  MONO%  7.4  %  3-10  False    中性粒细胞百分率  NEUT%  73.7  %  40-75  False    嗜酸性粒细胞百分率  E0%  4.2  %  0.4-8.0  False    嗜碱性粒细胞百分率  BASO%  0.3  %  0-1  False    淋巴细胞绝对值  LYMPH#  1.65  E+09/L  1.1-3.2  False    单核细胞绝对值  MONO#  0.85  E+09/L  0.1-0.6  True    中性粒细胞绝对值  NEUT#  8.43  E+09/L  1.8-6.3  True    嗜酸性粒细胞绝对值  E0#  0.48  E+09/L  0.02-0.52  False    嗜碱性粒细胞绝对值  BASO#  0.03  E+09/L  0-0.06  False    血小板计数(8-HR)  PLT  269  E+09/L  125-350  False    血小板分布宽度  PDW  11.3  fL  15.5-18.1  True    平均血小板体积  MPV  10.1  fL  9.4-12.5  False    大血小板比率  P-LCR  25.3  %  13-43  False    血小板比积  PCT  0.270  %  0.11-0.28  False    红细胞计数(8-HR)  RBC  4.56  E+12/L  4.3-5.8  False    血红蛋白(8-HR)  HGB  148  g/L  130-175  False    红细胞压积(8-HR)  HCT  44.8  %  40-50  False    平均红细胞体积(8-HR)  MCV  98.2  fL  82-100  False    平均血红蛋白含量(8-HR)  MCH  32.5  pg  27-34  False    平均血红蛋白浓度(8-HR)  MCHC  330  g/L  316-354  False    红细胞分布宽度CV  RDW%  13.4  %  10.9-15.4  False    红细胞分布宽度SD  RDW  49.0  fL  39-46  True   
---
   乙肝表面抗原  HBsAg  0.00  IU/mL  <0.03  False    乙肝表面抗体  Anti-HBs  16.90  mIU/mL  <5.00  True    乙肝e抗原  HBeAg  0.00  C.O.I  <1.00  False    乙肝e抗体  Anti-HBe  49.60  Inh%  <50.00  False    乙肝核心抗体  Anti-HBc  4.40  C.O.I  <1.00  True    丙型肝炎抗体  HCVAb  0.10  C.O.I  <1.00  False    人免疫缺陷病毒抗原抗体  HIVAg+Ab  0.00  C.O.I  <1.00  False    梅毒抗体  Anti-TP  0.00  C.O.I  <1.00  False   
---
   ABO血型鉴定  ABO  O型  None  None  False    RH(D)血型鉴定  Rh  阳性  None  None  False   
---
   游离三碘甲状腺原氨酸(8-HR)  FT3  4.31  pmol/L  3.85-6.3  False    游离甲状腺素(8-HR)  FT4  14.90  pmol/L  12.8-21.3  False    三碘甲状腺原氨酸(8-HR)  T3  1.81  nmol/L  1.3-2.4  False    甲状腺素(8-HR)  T4  102.00  nmol/L  70-140  False    促甲状腺素(8-HR)  TSH  2.45  uIU/mL  0.27-4.20  False   
---
   肌酸激酶同工酶  CK-MB  <0.22  ng/mL  0-2.37  False    肌钙蛋白I  cTnI  <0.012  ng/mL  0-0.034  False    肌红蛋白  MYO  45.94  ng/mL  0-121  False    N端脑利钠肽前体  NT-proBNP  <20.00  pg/mL  健康人群<125  False   
---
   凝血酶原时间(陕HR)  PT  11.2  sec  9.8-12.1  False    凝血酶原活动度  PTA  98.2  %  70-130  False    国际标准化比值(陕HR)  INR  0.97  None  0.7-1.3  False    活化部分凝血活酶时间(陕HR)  APTT  36.1  sec  22.7-31.8  True    纤维蛋白原含量(陕HR)  Fib  6.680  g/L  1.8-3.5  True    凝血酶时间(陕HR)  TT  15.5  sec  14-21  False    纤维蛋白(原)降解产物(定量)  FDP  4.50  μg/mL  0-5  False    D-二聚体(定量)(陕HR)  D D  1.185  μg/mL  0-1  True   
---
   血糖(空腹)(8-HR)  GLU  5.56  mmol/L  3.9-6.1  False    钾(8-HR)  K  4.36  mmol/L  3.5-5.3  False    钠(8-HR)  Na  137.8  mmol/L  137-147  False    氯(8-HR)  Cl  100.9  mmol/L  99-110  False    总蛋白(8-HR)  TP  73.0  g/L  65-85  False    白蛋白(8-HR)  ALB  42.4  g/L  40-55  False    球蛋白  GLO  30.6  g/L  20-40  False    白球比  A/G  1.4  None  1.2-2.4  False    总胆红素(8-HR)  T-BIL  12.1  μmol/L  0-26  False    直接胆红素(8-HR)  D-BIL  3.5  μmol/L  0-6.8  False    间接胆红素  I-BIL  8.6  μmol/L  0-14  False    丙氨酸氨基转移酶(8-HR)  ALT  26  U/L  9-50  False    天门冬氨酸氨基转移酶(8-HR)  AST  21  U/L  15-40  False    AST/ALT  None  0.81  None  None  False    碱性磷酸酶(8-HR)  ALP  106  U/L  45-125  False    总胆汁酸(陕HR)  TBA  12.6  μmol/L  0-10  True    胆碱酯酶(陕HR)  CHE  6970  U/L  5000-12000  False    γ-谷氨酰转移酶(8-HR)  GGT  23  U/L  10-60  False    eGFR(CKD-EPI)  eGFR  93.12  ml/min/1.73m2  >90  False    尿酸(8-HR)  UA  263.0  μmol/L  208-428  False    尿素(8-HR)  UREA  6.7  mmol/L  3.1-8.0  False    肌酐(8-HR)  CRE  81.0  μmol/L  57-97  False    肌酸激酶(8-HR)  CK  84  U/L  50-310  False    肌酸激酶同功酶  CK-MB  12.43  U/L  <25  False    乳酸脱氢酶(8-HR)  LDH  186  U/L  120-250  False    α-羟丁酸脱氢酶(陕HR)  α-HBDH  140  U/L  72-182  False    钙(8-HR)  Ca  2.26  mmol/L  2.2-2.7  False   
---
中国人民解放军联勤保障部队第九八九医院
出院证
姓名
性别
男
年龄
55岁
费别
ID号
2019131
住院号
A28146
入院日期
2026-02-22
出院日期
2026-03-02
住院天数
8
出院科室
肿瘤科病区
出院诊断:
肺占位
出院情况:
一般情况可
出院医嘱:
他院继续治疗
经治医生:
刘佳
日期:
2026-03-02
费川已核LY-16
审核人:于德艳
---
中国人民解放军联勤保障部队第九八九医院
姓名:水月强
病区(科):肿瘤科病区
床号:11
出院记录
姓名:
性别:男
年龄:55岁
入院时间:2026-02-22 08:42
出院时间:2026-03-02
住院天数:8天
入院情况:2025年12月无明显诱因出现胸闷,无发热、咳嗽、盗汗不适,未在意。2天前出现咯血,
色鲜红,量约10ml,2026-2-20至黄河三门峡医院查胸部CT提示:左肺上叶近肺门处占位,纵膈内稍肿大
淋巴结,双肺肺气肿,胸骨陈旧性骨折。入院当天再次出现咯血,急诊入院。入院查体:神志清楚,精
神好,双肺呼吸音清,未闻及干湿性罗音,心律齐,心音低钝,各瓣膜听诊区未闻及病理性杂音。
入院诊断:1、{肺肿物}
2、肺气肿
诊疗经过:患者入科后查血常规:白细胞计数9.63×10^9/L、中性粒细胞计数6.88×10^9/L,肝
肾功、生化:正常,凝血正常,细胞角蛋白19片段抗原21-1:3.47ng/mL、鳞状细胞癌抗原4.67ng/mL。
心电图:正常。胸腹部CT:1.左肺上叶占位,建议CT引导下穿刺活检;2.慢性支气管炎、局限性肺气
肿;3.上腹部CT增强未见明显异常。进一步行CT引导下穿刺活检,病理:(左肺穿刺组织)慢性炎症,间
质纤维组织增生、淋巴细胞浸润,请结合临床综合考虑。免疫组化结果:CK7(+),TTF-1(+),NapsinA
(+),CK-Pan(+),Ki-67(5%),P63(-)。建议患者再次穿刺活检或手术治疗,但家属要求出院,经请
示潘雪峰主任后同意,为患者办理出院手续。
出院诊断:1、{肺肿物}
2、肺气肿
出院情况:目前患者生命体征平稳,病情稳定。
出院医嘱及健康指导:
他院继续治疗。
/刘佳}
x
√
※
N
□
☐
I
II
III
IV
V
(
{
[
(
更多
---
空军军医大学唐都医院
查阅电子胶片
CT检查报告单
ID号：62893718
检查时间：2026-03-04
检查号：CT2603030254
住院
报告日期：2026-03-04
影像号：62893718
姓名
性别：男
年龄：55岁
申请科室：肿瘤科三病区
床号：
检查项目：盆腔CT平扫|胸部CT平扫|胸部CT增强|上腹部CT平扫(肝胆胰脾)|下腹部CT平扫
检查方法：平扫+增强
影像所见：
左肺上叶尖后段支气管狭窄，可见不规则团块状软组织密度影，大小约
4.5×4.0×5.9cm，局部紧贴叶间胸膜，可见“胸膜凹陷征”，平扫CT值约32HU，增
强扫描呈不均匀强化，两期CT值约33HU、59HU；右肺下叶前基底段可见局限性无肺纹
理区；余双肺野清晰，肺纹理走行自然，双肺门影不大。气管及纵隔位置居中，纵隔
可见多发增大淋巴结，较大者短径约0.6cm。心膈影未见异常，双侧胸膜无增厚，未见
胸腔积液。骨性胸廓骨质结构完整。
肝随边缘光滑，各叶大小比例正常，肝实质内密度均匀，未见明显异常密度影及
占位性病变，肝内外胆管未见扩张，肝门部结构清晰，未见占位性病变，胆囊不大，
壁薄且均匀，腔内未见阳性结石影。胰腺大小、形态及密度未见异常。脾不大，实质
密度均匀，双肾大小形态良好，实质密度均匀，双侧肾盂未见扩张，右肾可见阳性结
石影。腹腔内及腹膜后未见明显肿大淋巴结影，未见腹水征象。
膀胱充盈良好，壁厚薄均匀，未见占位性病变。前列腺大小、形态及密度未见异
常。双侧精囊腺大小、形态及密度未见异常。直肠形态正常，未见占位性病变。盆腔
淋巴结无肿大，盆腔内未见积液征象。
诊断意见：
1、左肺上叶尖后段占位性病变，多考虑周围型肺癌；纵隔多发增大淋巴结；
2、右肾结石；肝、胆、胰、脾及左肾CT扫描未见明显异常。
3、膀胱、前列腺、双侧精囊腺及直肠CT扫描未见明确病变。
本意见仅供临床医生参考，盖章或签字后生效！
报告医师：杨露
审核医师：
该信息经过北京CA数字签名认证
签名验证的信息摘要值为：3BFB10562BBC74DF5F886274A0100FAG。检查号：CT2603030254。
---
空军军医大学第二附属医院(唐都医院)
病理图文诊断报告单
病理号: 2610441
ID号: 62893718
住院号:
姓名
性别: 男
年龄: 55
送检单位: 唐都医院
科室: 肿瘤科三病区
床号:
送检日期: 2026-03-05
报告时间: 2026-03-06
肉眼所见:
支气管镜活检标本。
光镜所见:
病理诊断:
(左肺上叶尖段)鳞状上皮中-重度异型增生并局部癌变(鳞状细胞癌)。
[注: 此例仅为小组织活检标本, 有一定局限性, 有可能不能代表病变全貌特征]
初诊医师: 苟晨靓 签名:
苟晨靓
主诊医师: 富金 签名:
富金
此报告签名医生信息已经过北京CA数字认证, 涂改无效。如对此报告有任何疑问, 请立即与病理科联系。
此报告仅此一份, 请妥善保管, 遗失不补。
2026-08-10 19:42:35,235 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 19:42:35,235 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "15 items, types={'LabReport': 11, 'DischargeRecord': 2, 'ExaminationReport': 2}", "name": "SYQI肺鳞癌.pdf", "embedding_token_consumption": 6344}
2026-08-10 19:42:35,235 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 19:42:35,525 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 19:42:35,525 INFO     29 [Trace] task=73b6bae6 | doc=SYQI肺鳞癌.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":14,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 19:42:35,531 INFO     29 [DIAG-EXECUTOR] row_position_int len=27 row[0]=(2, 36, 121, 178, 191) row[-1]=(2, 63, 111, 474, 484)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(6, 86, 129, 95, 105) row[-1]=(6, 348, 415, 143, 153)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=7 row[0]=(6, 120, 172, 479, 490) row[-1]=(6, 120, 155, 565, 576)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(7, 201, 305, 116, 125) row[-1]=(7, 201, 285, 229, 238)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=24 row[0]=(8, 175, 255, 129, 140) row[-1]=(8, 175, 255, 459, 470)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(9, 88, 170, 231, 244) row[-1]=(9, 88, 143, 355, 368)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(10, 91, 170, 182, 195) row[-1]=(10, 91, 183, 196, 210)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=5 row[0]=(11, 82, 259, 226, 239) row[-1]=(11, 82, 188, 299, 312)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(12, 87, 186, 230, 244) row[-1]=(12, 87, 191, 289, 303)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(13, 79, 204, 200, 215) row[-1]=(13, 79, 228, 408, 423)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int len=27 row[0]=(14, 156, 241, 131, 142) row[-1]=(14, 156, 200, 476, 486)
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:42:35,532 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 19:42:35,537 INFO     29 set_progress(73b6bae694f211f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 19:42:35 [DOC Engine]:
Start to index...
2026-08-10 19:42:35,557 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-10 19:42:35,562 INFO     29 set_progress(73b6bae694f211f1bd9827cf206dfa2d), progress: 0.8066666666666668, progress_msg: 
2026-08-10 19:42:35,575 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 19:42:35,593 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-10 19:42:35,608 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.008s]
2026-08-10 19:42:35,615 INFO     29 set_progress(73b6bae694f211f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 19:42:35 Indexing done (0.08s). Task done (472.00s)
2026-08-10 19:42:35,618 INFO     29 [Done], chunks(15), token(6344), elapsed:472.00
2026-08-10 19:42:35,802 INFO     29 handle_task done for task {"id": "73b6bae694f211f1bd9827cf206dfa2d", "doc_id": "737f81ac94f211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SYQI\u80ba\u9cde\u764c.pdf", "type": "pdf", "location": "SYQI\u80ba\u9cde\u764c.pdf", "size": 6697938, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786390446957, "task_type": "dataflow", "root_trace_id": "b189486cc1e346ada7fe75589235f3af", "root_traceparent": "00-b189486cc1e346ada7fe75589235f3af-9eebbf1c31986074-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
