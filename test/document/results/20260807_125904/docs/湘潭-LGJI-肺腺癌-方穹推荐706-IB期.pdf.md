# 基准结果：湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf

## 基本信息

- 文件：`湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf`
- 大小：2015.3 KB
- PDF 总页数：9
- doc_id：`0e185858918611f18dbe1f8f96f1c395`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-07T12:59:11  完成时间：2026-08-07T12:59:12  耗时：1.0s
- progress_msg：`11:04:05 Indexing done (0.10s). Task done (204.18s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 1fb2ade9 | 6 | 1-6 | 金域医学 KngMed Diagnostics 病理诊断报告书 1/1 标本条码 |
| 2 | cf58ab48 | 1 | 7-7 | 长沙益康肿瘤医院 出院记录 性别 男 年龄 49岁 病区 号 入院时间：2026 |
| 3 | d9d9eb95 | 1 | 9-9 | 长沙市第四医院（长沙市中西医结合医院） CT 诊断报告单 湖南HR 姓名： 性别 |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：8
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 9]`
- 覆盖页数：8 / 9；缺失页：`[8]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 8/9 页，缺失 [8]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"ExaminationReport": 2, "DischargeRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 3, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-06 11:04:03,167 INFO     30 [ChunkMerger] Merged 3 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-06 11:00:40,971 INFO     30 handle_task begin for task {"id": "0f25d360918611f18dbe1f8f96f1c395", "doc_id": "0e185858918611f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 2063705, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786014039116, "task_type": "dataflow", "root_trace_id": "bb104829c20d4dd6b02c65ac578dd1d9", "root_traceparent": "00-bb104829c20d4dd6b02c65ac578dd1d9-5f56a5362076019b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-06 11:00:41,226 INFO     30 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.003s]
2026-08-06 11:00:41,534 INFO     30 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-06 11:00:41,570 INFO     30 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-06 11:00:41,570 INFO     30 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-06 11:00:41,588 INFO     30 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-06 11:00:41,588 INFO     30 ============================================================
2026-08-06 11:00:41,588 INFO     30 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-06 11:00:41,588 INFO     30    model_dir : /ragflow/rag/res/deepdoc
2026-08-06 11:00:41,588 INFO     30 ============================================================
2026-08-06 11:00:41,588 INFO     30 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-06 11:00:41,589 INFO     30 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-06 11:00:41,592 INFO     30 No torch found.
2026-08-06 11:00:43,683 INFO     30 [qwen-vl-parser] parse_pdf start, total_pages=9
2026-08-06 11:00:44,103 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=936185, prompt_len=764
2026-08-06 11:00:46,521 INFO     30 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-04"
}
```
2026-08-06 11:00:46,522 INFO     30 [qwen-vl-parser] page=1 classify=text report_date=2026-03-04
2026-08-06 11:00:46,578 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=936185, prompt_len=401
2026-08-06 11:00:49,187 INFO     30 [qwen-vl-parser] text API response (len=446):
["金域医学", "KngMed Diagnostics", "病理诊断报告书", "1/1", "标本条码", "医院", "病人姓名", "科室", "性别", "男", "房/床号", "病理号", "年龄", "49岁", "接收时间", "2026-03-04 15:21:00", "住院/门诊号", "采样时间", "2026-03-03 15:05:43", "患者电话", "申请医生", "项目名称", "免疫组化10项", "送检材料", "临床诊断", "大体描述:", "灰红碎组织一堆，大小1*0.8*0.5cm。取1盒全", "镜下所见:", "诊断意见:", "(左肺穿刺活检)低分化腺癌。", "1号蜡块免疫组化: CK (+++)、CK5/6 (-)、P40 (-)、CK7 (+++)、TTF-1 (+++)、NapsinA (灶+)、Syn (-)、P5", "3 (++80%倾向野生型)、Ki-67 (++30%)、SMARCA4 (+++)。"]
2026-08-06 11:00:49,188 INFO     30 [qwen-vl-parser] page=1 text: 32 lines (bbox 0-31)
2026-08-06 11:00:49,188 INFO     30 [qwen-vl-parser] page=1 text: 32 sections
2026-08-06 11:00:49,348 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=272194, prompt_len=764
2026-08-06 11:00:50,827 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 11:00:50,828 INFO     30 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-06 11:00:50,868 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=272194, prompt_len=401
2026-08-06 11:00:53,035 INFO     30 [qwen-vl-parser] text API response (len=410):
["基本信息", "受检者基本信息", "受检者姓名：", "性别：男", "年龄：49岁", "病理诊断*：肺腺癌", "用药史*：/", "处方医师：/", "医疗机构：/", "样本基本信息", "肿瘤样本编号：", "肿瘤样本类型：石蜡切片", "肿瘤样本采集部位：/", "肿瘤样本采集日期：/", "样本接收日期：2026-03-12", "注*：以上受检者基本信息来自患者送检时提供信息，而非来自本次检测结果，本次检测不对此内容进行解读。", "结果概览", "项目分类", "检测项目", "检测结果", "基因组变异检测结果", "明确/潜在临床意义的变异", "KRAS p.G13D; TP53 p.G154V", "临床意义不明的变异", "未见变异", "微卫星不稳定评估（MSI）", "微卫星不稳定评估（MSI）", "微卫星稳定型（MSS）", "NGS 质量控制评估结果", "合格"]
2026-08-06 11:00:53,035 INFO     30 [qwen-vl-parser] page=2 text: 30 lines (bbox 32-61)
2026-08-06 11:00:53,036 INFO     30 [qwen-vl-parser] page=2 text: 30 sections
2026-08-06 11:00:53,481 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=659926, prompt_len=764
2026-08-06 11:00:56,348 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 11:00:56,349 INFO     30 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-06 11:00:56,375 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=659926, prompt_len=401
2026-08-06 11:01:01,458 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T11:01:01.454+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"0f25d360918611f18dbe1f8f96f1c395": {"id": "0f25d360918611f18dbe1f8f96f1c395", "doc_id": "0e185858918611f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 2063705, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786014039116, "task_type": "dataflow", "root_trace_id": "bb104829c20d4dd6b02c65ac578dd1d9", "root_traceparent": "00-bb104829c20d4dd6b02c65ac578dd1d9-5f56a5362076019b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 11:01:03,162 INFO     30 [qwen-vl-parser] text API response (len=1336):
["检测结果及详细解析", "变异检测结果及临床获益", "明确/潜在临床意义的基因变异（靶药）", "基因", "检测结果", "突变频率/拷贝数", "可能获益靶药", "可能耐药靶药", "KRAS", "c.38G>A", "Avutometinib+Defactinib(II-C)", "厄洛替尼*(II-C)", "p.G13D", "吉非替尼*(II-C)", "NM_004985.3", "exon2", "6.73%", "Avutometinib+Defactinib(II-C)", "拉罗替尼*(II-C)", "错义突变", "芦康沙妥珠单抗*(II-C)", "佐利替尼*(II-C)", "曲美替尼*(II-C)", "阿法替尼*(II-C)", "Defactinib(II-C)", "阿美替尼*(II-C)", "TVB-2640(II-C)", "贝福替尼*(II-C)", "塞利尼索*(II-C)", "达可替尼*(II-C)", "曲美替尼*+安罗替尼*(II-C)", "厄洛替尼*+贝伐珠单抗*(II-C)", "Lifirafenib(II-C)", "厄洛替尼*+雷莫西尤单抗", "(II-C)", "JYP0015(II-C)", "伏美替尼*(II-C)", "MRTX0902(II-C)", "埃克替尼*(II-C)", "RMC-6236(II-C)", "利厄替尼*(II-C)", "芦沃美替尼*(II-D)", "奥希替尼*(II-C)", "妥拉美替尼*(II-D)", "瑞齐替尼*(II-C)", "Avutometinib(II-D)", "瑞厄替尼*(II-C)", "Cobimetinib(II-D)", "克唑替尼*(II-D)", "特泊替尼*(II-D)", "Sotorasib(II-D)", "TP53", "c.461G>T", "MK-1775(II-C)", "/", "p.G154V", "NM_000546.5", "exon5", "7.69%", "A196+Barasertib(II-D)", "错义突变", "明确/潜在临床意义的基因变异（分型/预后）", "基因", "检测结果", "突变频率/拷贝数", "分型/预后提示", "TP53", "c.461G>T", "临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53", "p.G154V", "或 STK11 突变的发生可能与较差的生存相关", "NM_000546.5", "exon5", "7.69%", "[PMID:30885352]。", "错义突变", "KRAS", "c.38G>A", "临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53", "p.G13D", "或 STK11 突变的发生可能与较差的生存相关", "NM_004985.3", "exon2", "6.73%", "[PMID:30885352]", "错义突变", "NCCN《非小细胞肺癌临床实践指南》提示，检出 KRAS", "突变与未检出该基因突变的患者相比生存预后较差。"]
2026-08-06 11:01:03,164 INFO     30 [qwen-vl-parser] page=3 text: 88 lines (bbox 62-149)
2026-08-06 11:01:03,164 INFO     30 [qwen-vl-parser] page=3 text: 88 sections
2026-08-06 11:01:03,297 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=110422, prompt_len=764
2026-08-06 11:01:03,894 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 11:01:03,894 INFO     30 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-06 11:01:03,933 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=110422, prompt_len=401
2026-08-06 11:01:04,845 INFO     30 [qwen-vl-parser] text API response (len=159):
["MSI 微卫星不稳定检测结果", "BIOMARKER", "癌种", "检测结果", "免疫治疗相关意义", "MSI", "实体瘤", "微卫星稳定型", "微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。", "(MSS)", "注：免疫治疗疗效影响因子较多，需综合评估，用药谨遵医嘱。"]
2026-08-06 11:01:04,846 INFO     30 [qwen-vl-parser] page=4 text: 11 lines (bbox 150-160)
2026-08-06 11:01:04,846 INFO     30 [qwen-vl-parser] page=4 text: 11 sections
2026-08-06 11:01:05,188 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=868769, prompt_len=764
2026-08-06 11:01:07,875 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 11:01:07,876 INFO     30 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-06 11:01:07,914 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=868769, prompt_len=401
2026-08-06 11:01:14,567 INFO     30 [qwen-vl-parser] text API response (len=1229):
["-实体瘤78基因（组织版）-报告解读", "患者基础信息：患者为肺腺癌，样本类型为石蜡切片。", "基因检测结果：检出KRAS p.G13D、TP53 p.G154V为明确/潜在临床意义的", "变异，检出0个临床意义不明的变异。微卫星稳定型（MSS）。", "结果解读：", "• 分型/预后评估：", "1） 该患者本次检出TP53 p.G154V变异，临床研究表明，在携带KRAS突", "变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P", "MID:30885352]。为临床提供参考。", "2） 该患者本次检出KRAS p.G13D变异，临床研究表明，在携带KRAS突", "变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P", "MID:30885352]。", "NCCN《非小细胞肺癌临床实践指南》提示，检出KRAS突变与未检出", "该基因突变的患者相比生存预后较差。为临床提供参考。", "• 靶向药物：", "1） 该患者本次检出KRAS p.G13D变异，匹配到潜在获益的靶向药物：Av", "utometinib+Defactinib(II-C)，芦康沙妥珠单抗*(II-C)，曲美替尼*(II-", "C)，Defactinib(II-C)，TVB-2640(II-C)，塞利尼索*(II-C)，曲美替尼", "*+安罗替尼*(II-C)，Lifirafenib(II-C)，JYP0015(II-C)，MRTX0902(", "II-C)，RMC-6236(II-C)，芦沃美替尼*(II-D)，妥拉美替尼*(II-D)，Av", "utometinib(II-D)，Cobimetinib(II-D);匹配到潜在耐药的靶向药物：", "厄洛替尼*(II-C)，吉非替尼*(II-C)，拉罗替尼*(II-C)，佐利替尼*(II-", "C)，阿法替尼*(II-C)，阿美替尼*(II-C)，贝福替尼*(II-C)，达可替尼*(II", "-C)，厄洛替尼*+贝伐珠单抗*(II-C)，厄洛替尼*+雷莫西尤单抗*(II-", "C)，伏美替尼*(II-C)，埃克替尼*(II-C)，利厄替尼*(II-C)，奥希替尼*(II", "-C)，瑞齐替尼*(II-C)，瑞厄替尼*(II-C)，克唑替尼*(II-D)，特泊替尼*(I", "I-D)，Sotorasib(II-D)。", "2） 该患者本次检出TP53 p.G154V变异，匹配到潜在获益的靶向药物：M", "K-1775(II-C)，A196+Barasertib(II-D)。", "• 免疫治疗：", "该样本微卫星不稳定性为微卫星稳定型（MSS），提示可能从免疫检查点", "抑制剂单药中获益较小。", "未检测出免疫治疗相关基因变异。", "免疫治疗也需要综合考虑多种因素，以及患者自身临床情况，综合评估，"]
2026-08-06 11:01:14,568 INFO     30 [qwen-vl-parser] page=5 text: 34 lines (bbox 161-194)
2026-08-06 11:01:14,568 INFO     30 [qwen-vl-parser] page=5 text: 34 sections
2026-08-06 11:01:14,672 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=137780, prompt_len=764
2026-08-06 11:01:15,336 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 11:01:15,337 INFO     30 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-06 11:01:15,384 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=137780, prompt_len=401
2026-08-06 11:01:16,415 INFO     30 [qwen-vl-parser] text API response (len=148):
["以上仅供参考。", "• 化疗药物：", "伊立替康，药物敏感性可能较低。卡培他滨、氟尿嘧啶类药物为基础的化", "疗方案，可能有较低的药物毒副风险。伊立替康，可能有较高的药物剂量需", "求。化疗药物的选择需结合患者的临床情况，具体用药方案还请医生综合判", "断，该检测结果仅供参考。"]
2026-08-06 11:01:16,417 INFO     30 [qwen-vl-parser] page=6 text: 6 lines (bbox 195-200)
2026-08-06 11:01:16,417 INFO     30 [qwen-vl-parser] page=6 text: 6 sections
2026-08-06 11:01:16,854 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1131559, prompt_len=764
2026-08-06 11:01:18,970 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 11:01:18,971 INFO     30 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-06 11:01:19,012 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1131559, prompt_len=401
2026-08-06 11:01:26,227 INFO     30 [qwen-vl-parser] text API response (len=1163):
["长沙益康肿瘤医院", "出院记录", "性别 男 年龄 49岁 病区", "号", "入院时间：2026-03-02", "出院时间：2026-03-09", "住院天数：7天", "入院诊断：1.左肺占位性质待查", "入院时情况：患者，男，49岁，因咳嗽2月余，发现肺部占位4天入院，目前症见：时有咳嗽，", "夜间咳甚，咳吐黄白痰，时有痰中夹带血丝，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一", "般，二便可，近期体重无减轻。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动", "正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。辅助检", "查：（2026年1月26日 长沙市第四医院）胸部CT：1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议", "CT增强。2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。3.右肺中叶内侧段慢性炎症，", "肺气肿、肺大泡。4.双肺下垂部坠积性炎症。5.心包少许积液。左冠状动脉少许钙化。6.右侧第8、9", "后肋陈旧性骨折可能。", "诊疗经过：入院完善相关检查：血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性", "粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00", "g/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、", "输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。", "排除禁忌，于2026年3月3日行CT引导下左肺占位穿刺活检术，配合止血，止咳等对症支持治疗，", "术后病理：（左肺穿刺活检）低分化腺癌。1号蜡块免疫组化：CK(+++)、CK5/6(-)、P40(-)、CK7(++", "+)、TTF-1(+++)、NapsinA(灶+)、Syn(-)、P53(++80%倾向野生型)、Ki-67(++30%)、SMARCA4(+++)。现患者肺癌", "诊断明确，暂不考虑抗肿瘤治疗，要求出院，经上级医师同意后予以办理出院。", "出院情况：患者咳嗽较前好转，无痰中带血，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，", "夜寐一般，二便可。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，", "无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。", "出院诊断：肺恶性肿瘤 左肺 低分化腺癌", "出院医嘱：建议行抗肿瘤专科治疗。", "上级/经治医师签名："]
2026-08-06 11:01:26,228 INFO     30 [qwen-vl-parser] page=7 text: 30 lines (bbox 201-230)
2026-08-06 11:01:26,229 INFO     30 [qwen-vl-parser] page=7 text: 30 sections
2026-08-06 11:01:26,580 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=467659, prompt_len=764
2026-08-06 11:01:27,961 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 11:01:27,962 INFO     30 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-06 11:01:28,001 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=467659, prompt_len=401
2026-08-06 11:01:29,085 INFO     30 [qwen-vl-parser] text API response (len=145):
["疾病诊断书", "交病人收", "长沙盈康肿瘤医院住院病人疾病诊断书", "姓名", "性别 男", "年龄 49岁", "住院号", "职业", "出院诊断：肺恶性肿瘤 左肺 低分化腺癌", "出院医嘱：建议行抗肿瘤专科治疗。", "住院医生", "签发日期 2026-03-09"]
2026-08-06 11:01:29,086 INFO     30 [qwen-vl-parser] page=8 text: 12 lines (bbox 231-242)
2026-08-06 11:01:29,086 INFO     30 [qwen-vl-parser] page=8 text: 12 sections
2026-08-06 11:01:29,550 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=979692, prompt_len=764
2026-08-06 11:01:31,495 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T11:01:31.491+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"0f25d360918611f18dbe1f8f96f1c395": {"id": "0f25d360918611f18dbe1f8f96f1c395", "doc_id": "0e185858918611f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 2063705, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786014039116, "task_type": "dataflow", "root_trace_id": "bb104829c20d4dd6b02c65ac578dd1d9", "root_traceparent": "00-bb104829c20d4dd6b02c65ac578dd1d9-5f56a5362076019b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 11:01:32,045 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-01-26"}
```
2026-08-06 11:01:32,046 INFO     30 [qwen-vl-parser] page=9 classify=text report_date=2026-01-26
2026-08-06 11:01:32,089 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=979692, prompt_len=401
2026-08-06 11:01:36,848 INFO     30 [qwen-vl-parser] text API response (len=726):
["长沙市第四医院（长沙市中西医结合医院）", "CT 诊断报告单", "湖南HR", "姓名：", "性别：男", "年龄：49 岁", "门诊号：20260126", "科室：", "水新城)", "床号：", "住院号：", "摄片、", "检查日期：2026/1/26 19:56:46", "报告日期：2026-01-26 20:14:00", "检查项目：(CT)平扫一薄层扫描（加收）,(CT)平扫-胸部", "检查方法：", "影像表现：", "双侧胸廓对称。双肺支气管-血管束稍增多。双肺见散在囊状透亮影，大者位于左肺上叶大小约29×25mm。右肺中", "叶内侧段可见斑点状、条索状高密度影，边界清晰。双肺下垂部见斑片状稍高密度影，边界模糊。左肺上叶尖后段-下", "叶背段见肿块影，大小约80×44×82mm，边缘见分叶，CT值约14HU；余双肺见多发结节影，较大者位于左肺上叶前段", "(IM72)，大小约12×8mm，CT值约32HU。左肺上叶尖后段-下叶背段欠通畅。心脏及大血管界面清晰，心包少许积", "液。左肺门见肿大淋巴结，大者短径约12mm。纵隔见散在小淋巴结影。双侧胸膜无增厚，双侧胸腔未见积液。右侧第", "8、9后肋骨质不规则。左冠状动脉钙化。", "影像诊断：", "1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。", "2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。", "3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。", "4.双肺下垂部坠积性炎症。", "5.心包少许积液。左冠状动脉少许钙化。", "6.右侧第8、9后肋陈旧性骨折可能。", "报告医生：", "审核医生："]
2026-08-06 11:01:36,849 INFO     30 [qwen-vl-parser] page=9 text: 32 lines (bbox 243-274)
2026-08-06 11:01:36,849 INFO     30 [qwen-vl-parser] page=9 text: 32 sections
2026-08-06 11:01:36,850 INFO     30 [qwen-vl-parser] parse_pdf done: 275 sections from 9 pages.
2026-08-06 11:01:36,892 INFO     30 Close text detector.
2026-08-06 11:01:37,571 INFO     30 Close text recognizer.
2026-08-06 11:01:38,155 INFO     30 Close recognizer.
2026-08-06 11:01:39,056 INFO     30 Close recognizer.
2026-08-06 11:01:40,385 INFO     30 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-06 11:01:40,385 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Parser:MedLink | outputs={"html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "json"}
2026-08-06 11:01:40,386 INFO     30 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-06 11:01:40,490 INFO     30 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:40,491 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n⚠️ 住院病程文书归属：病程记录、查房记录、术前小结、术后首次病程记录等住院期间病程文书，与入院记录同属一次住院事件；当它们与入院记录页相邻时，必须合并为一个 AdmissionRecord 片段，不得单独成段、不得归入 DischargeRecord。\n- 病程文书识别特征：标题含\"病程记录\"/\"查房记录\"/\"术前小结\"/\"术后首次病程记录\"，带住院患者信息（科室/床号/住院号），有\"入院时间\"（如\"2020年07月08日 08:36:09入院\"），无\"出院诊断\"/\"出院医嘱\"\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 金域医学\n[BBOX-1] KngMed Diagnostics\n[BBOX-2] 病理诊断报告书\n[BBOX-3] 1/1\n[BBOX-4] 标本条码\n[BBOX-5] 医院\n[BBOX-6] 病人姓名\n[BBOX-7] 科室\n[BBOX-8] 性别\n[BBOX-9] 男\n[BBOX-10] 房/床号\n[BBOX-11] 病理号\n[BBOX-12] 年龄\n[BBOX-13] 49岁\n[BBOX-14] 接收时间\n[BBOX-15] 2026-03-04 15:21:00\n[BBOX-16] 住院/门诊号\n[BBOX-17] 采样时间\n[BBOX-18] 2026-03-03 15:05:43\n[BBOX-19] 患者电话\n[BBOX-20] 申请医生\n[BBOX-21] 项目名称\n[BBOX-22] 免疫组化10项\n[BBOX-23] 送检材料\n[BBOX-24] 临床诊断\n[BBOX-25] 大体描述:\n[BBOX-26] 灰红碎组织一堆，大小1*0.8*0.5cm。取1盒全\n[BBOX-27] 镜下所见:\n[BBOX-28] 诊断意见:\n[BBOX-29] (左肺穿刺活检)低分化腺癌。\n[BBOX-30] 1号蜡块免疫组化: CK (+++)、CK5/6 (-)、P40 (-)、CK7 (+++)、TTF-1 (+++)、NapsinA (灶+)、Syn (-)、P5\n[BBOX-31] 3 (++80%倾向野生型)、Ki-67 (++30%)、SMARCA4 (+++)。\n[BBOX-32] 基本信息\n[BBOX-33] 受检者基本信息\n[BBOX-34] 受检者姓名：\n[BBOX-35] 性别：男\n[BBOX-36] 年龄：49岁\n[BBOX-37] 病理诊断*：肺腺癌\n[BBOX-38] 用药史*：/\n[BBOX-39] 处方医师：/\n[BBOX-40] 医疗机构：/\n[BBOX-41] 样本基本信息\n[BBOX-42] 肿瘤样本编号：\n[BBOX-43] 肿瘤样本类型：石蜡切片\n[BBOX-44] 肿瘤样本采集部位：/\n[BBOX-45] 肿瘤样本采集日期：/\n[BBOX-46] 样本接收日期：2026-03-12\n[BBOX-47] 注*：以上受检者基本信息来自患者送检时提供信息，而非来自本次检测结果，本次检测不对此内容进行解读。\n[BBOX-48] 结果概览\n[BBOX-49] 项目分类\n[BBOX-50] 检测项目\n[BBOX-51] 检测结果\n[BBOX-52] 基因组变异检测结果\n[BBOX-53] 明确/潜在临床意义的变异\n[BBOX-54] KRAS p.G13D; TP53 p.G154V\n[BBOX-55] 临床意义不明的变异\n[BBOX-56] 未见变异\n[BBOX-57] 微卫星不稳定评估（MSI）\n[BBOX-58] 微卫星不稳定评估（MSI）\n[BBOX-59] 微卫星稳定型（MSS）\n[BBOX-60] NGS 质量控制评估结果\n[BBOX-61] 合格\n[BBOX-62] 检测结果及详细解析\n[BBOX-63] 变异检测结果及临床获益\n[BBOX-64] 明确/潜在临床意义的基因变异（靶药）\n[BBOX-65] 基因\n[BBOX-66] 检测结果\n[BBOX-67] 突变频率/拷贝数\n[BBOX-68] 可能获益靶药\n[BBOX-69] 可能耐药靶药\n[BBOX-70] KRAS\n[BBOX-71] c.38G>A\n[BBOX-72] Avutometinib+Defactinib(II-C)\n[BBOX-73] 厄洛替尼*(II-C)\n[BBOX-74] p.G13D\n[BBOX-75] 吉非替尼*(II-C)\n[BBOX-76] NM_004985.3\n[BBOX-77] exon2\n[BBOX-78] 6.73%\n[BBOX-79] Avutometinib+Defactinib(II-C)\n[BBOX-80] 拉罗替尼*(II-C)\n[BBOX-81] 错义突变\n[BBOX-82] 芦康沙妥珠单抗*(II-C)\n[BBOX-83] 佐利替尼*(II-C)\n[BBOX-84] 曲美替尼*(II-C)\n[BBOX-85] 阿法替尼*(II-C)\n[BBOX-86] Defactinib(II-C)\n[BBOX-87] 阿美替尼*(II-C)\n[BBOX-88] TVB-2640(II-C)\n[BBOX-89] 贝福替尼*(II-C)\n[BBOX-90] 塞利尼索*(II-C)\n[BBOX-91] 达可替尼*(II-C)\n[BBOX-92] 曲美替尼*+安罗替尼*(II-C)\n[BBOX-93] 厄洛替尼*+贝伐珠单抗*(II-C)\n[BBOX-94] Lifirafenib(II-C)\n[BBOX-95] 厄洛替尼*+雷莫西尤单抗\n[BBOX-96] (II-C)\n[BBOX-97] JYP0015(II-C)\n[BBOX-98] 伏美替尼*(II-C)\n[BBOX-99] MRTX0902(II-C)\n[BBOX-100] 埃克替尼*(II-C)\n[BBOX-101] RMC-6236(II-C)\n[BBOX-102] 利厄替尼*(II-C)\n[BBOX-103] 芦沃美替尼*(II-D)\n[BBOX-104] 奥希替尼*(II-C)\n[BBOX-105] 妥拉美替尼*(II-D)\n[BBOX-106] 瑞齐替尼*(II-C)\n[BBOX-107] Avutometinib(II-D)\n[BBOX-108] 瑞厄替尼*(II-C)\n[BBOX-109] Cobimetinib(II-D)\n[BBOX-110] 克唑替尼*(II-D)\n[BBOX-111] 特泊替尼*(II-D)\n[BBOX-112] Sotorasib(II-D)\n[BBOX-113] TP53\n[BBOX-114] c.461G>T\n[BBOX-115] MK-1775(II-C)\n[BBOX-116] /\n[BBOX-117] p.G154V\n[BBOX-118] NM_000546.5\n[BBOX-119] exon5\n[BBOX-120] 7.69%\n[BBOX-121] A196+Barasertib(II-D)\n[BBOX-122] 错义突变\n[BBOX-123] 明确/潜在临床意义的基因变异（分型/预后）\n[BBOX-124] 基因\n[BBOX-125] 检测结果\n[BBOX-126] 突变频率/拷贝数\n[BBOX-127] 分型/预后提示\n[BBOX-128] TP53\n[BBOX-129] c.461G>T\n[BBOX-130] 临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53\n[BBOX-131] p.G154V\n[BBOX-132] 或 STK11 突变的发生可能与较差的生存相关\n[BBOX-133] NM_000546.5\n[BBOX-134] exon5\n[BBOX-135] 7.69%\n[BBOX-136] [PMID:30885352]。\n[BBOX-137] 错义突变\n[BBOX-138] KRAS\n[BBOX-139] c.38G>A\n[BBOX-140] 临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53\n[BBOX-141] p.G13D\n[BBOX-142] 或 STK11 突变的发生可能与较差的生存相关\n[BBOX-143] NM_004985.3\n[BBOX-144] exon2\n[BBOX-145] 6.73%\n[BBOX-146] [PMID:30885352]\n[BBOX-147] 错义突变\n[BBOX-148] NCCN《非小细胞肺癌临床实践指南》提示，检出 KRAS\n[BBOX-149] 突变与未检出该基因突变的患者相比生存预后较差。\n[BBOX-150] MSI 微卫星不稳定检测结果\n[BBOX-151] BIOMARKER\n[BBOX-152] 癌种\n[BBOX-153] 检测结果\n[BBOX-154] 免疫治疗相关意义\n[BBOX-155] MSI\n[BBOX-156] 实体瘤\n[BBOX-157] 微卫星稳定型\n[BBOX-158] 微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。\n[BBOX-159] (MSS)\n[BBOX-160] 注：免疫治疗疗效影响因子较多，需综合评估，用药谨遵医嘱。\n[BBOX-161] -实体瘤78基因（组织版）-报告解读\n[BBOX-162] 患者基础信息：患者为肺腺癌，样本类型为石蜡切片。\n[BBOX-163] 基因检测结果：检出KRAS p.G13D、TP53 p.G154V为明确/潜在临床意义的\n[BBOX-164] 变异，检出0个临床意义不明的变异。微卫星稳定型（MSS）。\n[BBOX-165] 结果解读：\n[BBOX-166] • 分型/预后评估：\n[BBOX-167] 1） 该患者本次检出TP53 p.G154V变异，临床研究表明，在携带KRAS突\n[BBOX-168] 变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P\n[BBOX-169] MID:30885352]。为临床提供参考。\n[BBOX-170] 2） 该患者本次检出KRAS p.G13D变异，临床研究表明，在携带KRAS突\n[BBOX-171] 变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P\n[BBOX-172] MID:30885352]。\n[BBOX-173] NCCN《非小细胞肺癌临床实践指南》提示，检出KRAS突变与未检出\n[BBOX-174] 该基因突变的患者相比生存预后较差。为临床提供参考。\n[BBOX-175] • 靶向药物：\n[BBOX-176] 1） 该患者本次检出KRAS p.G13D变异，匹配到潜在获益的靶向药物：Av\n[BBOX-177] utometinib+Defactinib(II-C)，芦康沙妥珠单抗*(II-C)，曲美替尼*(II-\n[BBOX-178] C)，Defactinib(II-C)，TVB-2640(II-C)，塞利尼索*(II-C)，曲美替尼\n[BBOX-179] *+安罗替尼*(II-C)，Lifirafenib(II-C)，JYP0015(II-C)，MRTX0902(\n[BBOX-180] II-C)，RMC-6236(II-C)，芦沃美替尼*(II-D)，妥拉美替尼*(II-D)，Av\n[BBOX-181] utometinib(II-D)，Cobimetinib(II-D);匹配到潜在耐药的靶向药物：\n[BBOX-182] 厄洛替尼*(II-C)，吉非替尼*(II-C)，拉罗替尼*(II-C)，佐利替尼*(II-\n[BBOX-183] C)，阿法替尼*(II-C)，阿美替尼*(II-C)，贝福替尼*(II-C)，达可替尼*(II\n[BBOX-184] -C)，厄洛替尼*+贝伐珠单抗*(II-C)，厄洛替尼*+雷莫西尤单抗*(II-\n[BBOX-185] C)，伏美替尼*(II-C)，埃克替尼*(II-C)，利厄替尼*(II-C)，奥希替尼*(II\n[BBOX-186] -C)，瑞齐替尼*(II-C)，瑞厄替尼*(II-C)，克唑替尼*(II-D)，特泊替尼*(I\n[BBOX-187] I-D)，Sotorasib(II-D)。\n[BBOX-188] 2） 该患者本次检出TP53 p.G154V变异，匹配到潜在获益的靶向药物：M\n[BBOX-189] K-1775(II-C)，A196+Barasertib(II-D)。\n[BBOX-190] • 免疫治疗：\n[BBOX-191] 该样本微卫星不稳定性为微卫星稳定型（MSS），提示可能从免疫检查点\n[BBOX-192] 抑制剂单药中获益较小。\n[BBOX-193] 未检测出免疫治疗相关基因变异。\n[BBOX-194] 免疫治疗也需要综合考虑多种因素，以及患者自身临床情况，综合评估，\n[BBOX-195] 以上仅供参考。\n[BBOX-196] • 化疗药物：\n[BBOX-197] 伊立替康，药物敏感性可能较低。卡培他滨、氟尿嘧啶类药物为基础的化\n[BBOX-198] 疗方案，可能有较低的药物毒副风险。伊立替康，可能有较高的药物剂量需\n[BBOX-199] 求。化疗药物的选择需结合患者的临床情况，具体用药方案还请医生综合判\n[BBOX-200] 断，该检测结果仅供参考。\n[BBOX-201] 长沙益康肿瘤医院\n[BBOX-202] 出院记录\n[BBOX-203] 性别 男 年龄 49岁 病区\n[BBOX-204] 号\n[BBOX-205] 入院时间：2026-03-02\n[BBOX-206] 出院时间：2026-03-09\n[BBOX-207] 住院天数：7天\n[BBOX-208] 入院诊断：1.左肺占位性质待查\n[BBOX-209] 入院时情况：患者，男，49岁，因咳嗽2月余，发现肺部占位4天入院，目前症见：时有咳嗽，\n[BBOX-210] 夜间咳甚，咳吐黄白痰，时有痰中夹带血丝，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一\n[BBOX-211] 般，二便可，近期体重无减轻。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动\n[BBOX-212] 正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。辅助检\n[BBOX-213] 查：（2026年1月26日 长沙市第四医院）胸部CT：1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议\n[BBOX-214] CT增强。2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。3.右肺中叶内侧段慢性炎症，\n[BBOX-215] 肺气肿、肺大泡。4.双肺下垂部坠积性炎症。5.心包少许积液。左冠状动脉少许钙化。6.右侧第8、9\n[BBOX-216] 后肋陈旧性骨折可能。\n[BBOX-217] 诊疗经过：入院完善相关检查：血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性\n[BBOX-218] 粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00\n[BBOX-219] g/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、\n[BBOX-220] 输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。\n[BBOX-221] 排除禁忌，于2026年3月3日行CT引导下左肺占位穿刺活检术，配合止血，止咳等对症支持治疗，\n[BBOX-222] 术后病理：（左肺穿刺活检）低分化腺癌。1号蜡块免疫组化：CK(+++)、CK5/6(-)、P40(-)、CK7(++\n[BBOX-223] +)、TTF-1(+++)、NapsinA(灶+)、Syn(-)、P53(++80%倾向野生型)、Ki-67(++30%)、SMARCA4(+++)。现患者肺癌\n[BBOX-224] 诊断明确，暂不考虑抗肿瘤治疗，要求出院，经上级医师同意后予以办理出院。\n[BBOX-225] 出院情况：患者咳嗽较前好转，无痰中带血，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，\n[BBOX-226] 夜寐一般，二便可。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，\n[BBOX-227] 无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。\n[BBOX-228] 出院诊断：肺恶性肿瘤 左肺 低分化腺癌\n[BBOX-229] 出院医嘱：建议行抗肿瘤专科治疗。\n[BBOX-230] 上级/经治医师签名：\n[BBOX-231] 疾病诊断书\n[BBOX-232] 交病人收\n[BBOX-233] 长沙盈康肿瘤医院住院病人疾病诊断书\n[BBOX-234] 姓名\n[BBOX-235] 性别 男\n[BBOX-236] 年龄 49岁\n[BBOX-237] 住院号\n[BBOX-238] 职业\n[BBOX-239] 出院诊断：肺恶性肿瘤 左肺 低分化腺癌\n[BBOX-240] 出院医嘱：建议行抗肿瘤专科治疗。\n[BBOX-241] 住院医生\n[BBOX-242] 签发日期 2026-03-09\n[BBOX-243] 长沙市第四医院（长沙市中西医结合医院）\n[BBOX-244] CT 诊断报告单\n[BBOX-245] 湖南HR\n[BBOX-246] 姓名：\n[BBOX-247] 性别：男\n[BBOX-248] 年龄：49 岁\n[BBOX-249] 门诊号：20260126\n[BBOX-250] 科室：\n[BBOX-251] 水新城)\n[BBOX-252] 床号：\n[BBOX-253] 住院号：\n[BBOX-254] 摄片、\n[BBOX-255] 检查日期：2026/1/26 19:56:46\n[BBOX-256] 报告日期：2026-01-26 20:14:00\n[BBOX-257] 检查项目：(CT)平扫一薄层扫描（加收）,(CT)平扫-胸部\n[BBOX-258] 检查方法：\n[BBOX-259] 影像表现：\n[BBOX-260] 双侧胸廓对称。双肺支气管-血管束稍增多。双肺见散在囊状透亮影，大者位于左肺上叶大小约29×25mm。右肺中\n[BBOX-261] 叶内侧段可见斑点状、条索状高密度影，边界清晰。双肺下垂部见斑片状稍高密度影，边界模糊。左肺上叶尖后段-下\n[BBOX-262] 叶背段见肿块影，大小约80×44×82mm，边缘见分叶，CT值约14HU；余双肺见多发结节影，较大者位于左肺上叶前段\n[BBOX-263] (IM72)，大小约12×8mm，CT值约32HU。左肺上叶尖后段-下叶背段欠通畅。心脏及大血管界面清晰，心包少许积\n[BBOX-264] 液。左肺门见肿大淋巴结，大者短径约12mm。纵隔见散在小淋巴结影。双侧胸膜无增厚，双侧胸腔未见积液。右侧第\n[BBOX-265] 8、9后肋骨质不规则。左冠状动脉钙化。\n[BBOX-266] 影像诊断：\n[BBOX-267] 1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。\n[BBOX-268] 2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。\n[BBOX-269] 3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。\n[BBOX-270] 4.双肺下垂部坠积性炎症。\n[BBOX-271] 5.心包少许积液。左冠状动脉少许钙化。\n[BBOX-272] 6.右侧第8、9后肋陈旧性骨折可能。\n[BBOX-273] 报告医生：\n[BBOX-274] 审核医生："
  }
]
2026-08-06 11:01:46,128 INFO     30 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:46,220 INFO     30 [SmartSplitter] SmartSplitter done: 3 chunks from 3 LLM segments (all bbox_id). Types: {'ExaminationReport': 2, 'DischargeRecord': 1}
2026-08-06 11:01:46,262 INFO     30 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-06 11:01:46,263 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks": "3 items, types={'ExaminationReport': 2, 'DischargeRecord': 1}"}
2026-08-06 11:01:46,263 INFO     30 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-06 11:01:46,266 INFO     30 [ChunkRouter] Routed 3 chunks into 2 groups: {'chunks_Examination': 2, 'chunks_Discharge': 1}
2026-08-06 11:01:46,306 INFO     30 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-06 11:01:46,307 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | ChunkRouter:Router | outputs={"html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks": "3 items, types={'ExaminationReport': 2, 'DischargeRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:01:46,307 INFO     30 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-06 11:01:46,331 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:46,332 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 11:01:47,134 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:47,151 INFO     30 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-06 11:01:47,151 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:01:47,152 INFO     30 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-06 11:01:47,166 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:47,166 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 11:01:47,624 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:47,641 INFO     30 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-06 11:01:47,641 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:01:47,642 INFO     30 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-06 11:01:47,656 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:47,656 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 11:01:48,360 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:48,378 INFO     30 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-06 11:01:48,378 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:01:48,379 INFO     30 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-06 11:01:48,396 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:48,396 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 11:01:48,875 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:48,901 INFO     30 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-06 11:01:48,902 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:01:48,902 INFO     30 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-06 11:01:48,929 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:48,930 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 11:01:49,892 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:49,906 INFO     30 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-06 11:01:49,907 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:01:49,907 INFO     30 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-06 11:01:49,925 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 11:01:49,925 INFO     30 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-06 11:01:49,925 INFO     30 [qwen-vl-text] positions(30): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 11:01:49,926 INFO     30 [qwen-vl-text] page grouping: [6], lines per page: [30]
2026-08-06 11:01:50,330 INFO     30 [qwen-vl-text] page=6, rect=804x868, img=(2234x2413), dpi=200
2026-08-06 11:01:50,332 INFO     30 [qwen-vl-text] LLM extraction start, text_len=1072
2026-08-06 11:01:50,332 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:01:50,332 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 201, \"bbox_end\": 230, \"encounter_dates\": [\"2026-03-02\", \"2026-03-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "长沙益康肿瘤医院\n出院记录\n性别 男 年龄 49岁 病区\n号\n入院时间：2026-03-02\n出院时间：2026-03-09\n住院天数：7天\n入院诊断：1.左肺占位性质待查\n入院时情况：患者，男，49岁，因咳嗽2月余，发现肺部占位4天入院，目前症见：时有咳嗽，\n夜间咳甚，咳吐黄白痰，时有痰中夹带血丝，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一\n般，二便可，近期体重无减轻。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动\n正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。辅助检\n查：（2026年1月26日 长沙市第四医院）胸部CT：1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议\nCT增强。2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。3.右肺中叶内侧段慢性炎症，\n肺气肿、肺大泡。4.双肺下垂部坠积性炎症。5.心包少许积液。左冠状动脉少许钙化。6.右侧第8、9\n后肋陈旧性骨折可能。\n诊疗经过：入院完善相关检查：血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性\n粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00\ng/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、\n输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。\n排除禁忌，于2026年3月3日行CT引导下左肺占位穿刺活检术，配合止血，止咳等对症支持治疗，\n术后病理：（左肺穿刺活检）低分化腺癌。1号蜡块免疫组化：CK(+++)、CK5/6(-)、P40(-)、CK7(++\n+)、TTF-1(+++)、NapsinA(灶+)、Syn(-)、P53(++80%倾向野生型)、Ki-67(++30%)、SMARCA4(+++)。现患者肺癌\n诊断明确，暂不考虑抗肿瘤治疗，要求出院，经上级医师同意后予以办理出院。\n出院情况：患者咳嗽较前好转，无痰中带血，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，\n夜寐一般，二便可。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，\n无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。\n出院诊断：肺恶性肿瘤 左肺 低分化腺癌\n出院医嘱：建议行抗肿瘤专科治疗。\n上级/经治医师签名：",
    "role": "user"
  }
]
2026-08-06 11:02:01,062 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:02:01,063 INFO     30 [qwen-vl-text] LLM output (len=2026):
{
  "encounter_date": "2026-03-09",
  "admission_date": "2026-03-02",
  "discharge_date": "2026-03-09",
  "hospital_days": 7,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者，男，49岁，因咳嗽2月余，发现肺部占位4天入院，目前症见：时有咳嗽，夜间咳甚，咳吐黄白痰，时有痰中夹带血丝，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一般，二便可，近期体重无减轻。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。",
  "admission_diagnoses": [
    {
      "name": "左肺占位性质待查",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院完善相关检查：血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00 g/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。排除禁忌，于2026年3月3日行CT引导下左肺占位穿刺活检术，配合止血，止咳等对症支持治疗，术后病理：（左肺穿刺活检）低分化腺癌。1号蜡块免疫组化：CK(+++)、CK5/6(-)、P40(-)、CK7(+++)、TTF-1(+++)、NapsinA(灶+)、Syn(-)、P53(++80%倾向野生型)、Ki-67(++30%)、SMARCA4(+++)。现患者肺癌诊断明确，暂不考虑抗肿瘤治疗，要求出院，经上级医师同意后予以办理出院。",
  "auxiliary_exams": "血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00 g/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。",
  "imaging_findings": "（2026年1月26日 长沙市第四医院）胸部CT：1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。4.双肺下垂部坠积性炎症。5.心包少许积液。左冠状动脉少许钙化。6.右侧第8、9后肋陈旧性骨折可能。",
  "discharge_diagnoses": [
    {
      "name": "肺恶性肿瘤 左肺 低分化腺癌",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者咳嗽较前好转，无痰中带血，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一般，二便可。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。",
  "outcome": "好转",
  "discharge_orders": "建议行抗肿瘤专科治疗。",
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
2026-08-06 11:02:01,063 INFO     30 [qwen-vl-text] Updated encounter_dates=[2026-03-09]
2026-08-06 11:02:01,072 INFO     30 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1399554, prompt_len=1775
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["长沙益康肿瘤医院", "出院记录", "性别 男 年龄 49岁 病区", "号", "入院时间：2026-03-02", "出院时间：2026-03-09", "住院天数：7天", "入院诊断：1.左肺占位性质待查", "入院时情况：患者，男，49岁，因咳嗽2月余，发现肺部占位4天入院，目前症见：时有咳嗽，", "夜间咳甚，咳吐黄白痰，时有痰中夹带血丝，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一", "般，二便可，近期体重无减轻。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动", "正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。辅助检", "查：（2026年1月26日 长沙市第四医院）胸部CT：1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议", "CT增强。2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。3.右肺中叶内侧段慢性炎症，", "肺气肿、肺大泡。4.双肺下垂部坠积性炎症。5.心包少许积液。左冠状动脉少许钙化。6.右侧第8、9", "后肋陈旧性骨折可能。", "诊疗经过：入院完善相关检查：血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性", "粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00", "g/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、", "输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。", "排除禁忌，于2026年3月3日行CT引导下左肺占位穿刺活检术，配合止血，止咳等对症支持治疗，", "术后病理：（左肺穿刺活检）低分化腺癌。1号蜡块免疫组化：CK(+++)、CK5/6(-)、P40(-)、CK7(++", "+)、TTF-1(+++)、NapsinA(灶+)、Syn(-)、P53(++80%倾向野生型)、Ki-67(++30%)、SMARCA4(+++)。现患者肺癌", "诊断明确，暂不考虑抗肿瘤治疗，要求出院，经上级医师同意后予以办理出院。", "出院情况：患者咳嗽较前好转，无痰中带血，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，", "夜寐一般，二便可。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，", "无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。", "出院诊断：肺恶性肿瘤 左肺 低分化腺癌", "出院医嘱：建议行抗肿瘤专科治疗。", "上级/经治医师签名："]

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
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord API raw response (len=2364):
[
	{"text": "长沙益康肿瘤医院", "bbox": [368, 0, 587, 26]},
	{"text": "出院记录", "bbox": [345, 34, 605, 95]},
	{"text": "性别 男 年龄 49岁 病区", "bbox": [153, 89, 450, 127]},
	{"text": "号", "bbox": [618, 114, 654, 136]},
	{"text": "入院时间：2026-03-02", "bbox": [57, 170, 263, 197]},
	{"text": "出院时间：2026-03-09", "bbox": [56, 207, 263, 234]},
	{"text": "住院天数：7天", "bbox": [55, 244, 190, 270]},
	{"text": "入院诊断：1.左肺占位性质待查", "bbox": [54, 282, 355, 310]},
	{"text": "入院时情况：患者，男，49岁，因咳嗽2月余，发现肺部占位4天入院，目前症见：时有咳嗽，", "bbox": [48, 352, 954, 380]},
	{"text": "夜间咳甚，咳吐黄白痰，时有痰中夹带血丝，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一", "bbox": [27, 379, 945, 408]},
	{"text": "般，二便可，近期体重无减轻。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动", "bbox": [26, 406, 945, 434]},
	{"text": "正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。辅助检", "bbox": [26, 433, 945, 461]},
	{"text": "查：（2026年1月26日 长沙市第四医院）胸部CT：1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议", "bbox": [25, 460, 942, 488]},
	{"text": "CT增强。2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。3.右肺中叶内侧段慢性炎症，", "bbox": [25, 487, 951, 515]},
	{"text": "肺气肿、肺大泡。4.双肺下垂部坠积性炎症。5.心包少许积液。左冠状动脉少许钙化。6.右侧第8、9", "bbox": [25, 513, 943, 541]},
	{"text": "后肋陈旧性骨折可能。", "bbox": [25, 538, 230, 562]},
	{"text": "诊疗经过：入院完善相关检查：血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性", "bbox": [25, 564, 940, 593]},
	{"text": "粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00", "bbox": [25, 591, 940, 619]},
	{"text": "g/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、", "bbox": [25, 617, 935, 645]},
	{"text": "输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。", "bbox": [25, 643, 924, 672]},
	{"text": "排除禁忌，于2026年3月3日行CT引导下左肺占位穿刺活检术，配合止血，止咳等对症支持治疗，", "bbox": [27, 670, 922, 698]},
	{"text": "术后病理：（左肺穿刺活检）低分化腺癌。1号蜡块免疫组化：CK(+++)、CK5/6(-)、P40(-)、CK7(++", "bbox": [27, 696, 935, 724]},
	{"text": "+)、TTF-1(+++)、NapsinA(灶+)、Syn(-)、P53(++80%倾向野生型)、Ki-67(++30%)、SMARCA4(+++)。现患者肺癌", "bbox": [27, 722, 934, 750]},
	{"text": "诊断明确，暂不考虑抗肿瘤治疗，要求出院，经上级医师同意后予以办理出院。", "bbox": [29, 745, 757, 770]},
	{"text": "出院情况：患者咳嗽较前好转，无痰中带血，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，", "bbox": [75, 773, 934, 801]},
	{"text": "夜寐一般，二便可。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，", "bbox": [20, 798, 934, 826]},
	{"text": "无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。", "bbox": [20, 823, 829, 851]},
	{"text": "出院诊断：肺恶性肿瘤 左肺 低分化腺癌", "bbox": [75, 855, 454, 876]},
	{"text": "出院医嘱：建议行抗肿瘤专科治疗。", "bbox": [74, 915, 397, 936]},
	{"text": "上级/经治医师签名：", "bbox": [573, 949, 753, 977]}
]
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=14.8s
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord item[0]: text=长沙益康肿瘤医院, bbox=[368, 0, 587, 26]
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord item[1]: text=出院记录, bbox=[345, 34, 605, 95]
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord item[2]: text=性别 男 年龄 49岁 病区, bbox=[153, 89, 450, 127]
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord item[3]: text=号, bbox=[618, 114, 654, 136]
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord item[4]: text=入院时间：2026-03-02, bbox=[57, 170, 263, 197]
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord item[5]: text=出院时间：2026-03-09, bbox=[56, 207, 263, 234]
2026-08-06 11:02:15,910 INFO     30 [qwen-vl-text] coord item[6]: text=住院天数：7天, bbox=[55, 244, 190, 270]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[7]: text=入院诊断：1.左肺占位性质待查, bbox=[54, 282, 355, 310]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[8]: text=入院时情况：患者，男，49岁，因咳嗽2月余，发现肺部占位4天入院，目前症见：时有咳嗽，, bbox=[48, 352, 954, 380]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[9]: text=夜间咳甚，咳吐黄白痰，时有痰中夹带血丝，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一, bbox=[27, 379, 945, 408]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[10]: text=般，二便可，近期体重无减轻。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动, bbox=[26, 406, 945, 434]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[11]: text=正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。辅助检, bbox=[26, 433, 945, 461]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[12]: text=查：（2026年1月26日 长沙市第四医院）胸部CT：1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议, bbox=[25, 460, 942, 488]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[13]: text=CT增强。2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。3.右肺中叶内侧段慢性炎症，, bbox=[25, 487, 951, 515]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[14]: text=肺气肿、肺大泡。4.双肺下垂部坠积性炎症。5.心包少许积液。左冠状动脉少许钙化。6.右侧第8、9, bbox=[25, 513, 943, 541]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[15]: text=后肋陈旧性骨折可能。, bbox=[25, 538, 230, 562]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[16]: text=诊疗经过：入院完善相关检查：血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性, bbox=[25, 564, 940, 593]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[17]: text=粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00, bbox=[25, 591, 940, 619]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[18]: text=g/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、, bbox=[25, 617, 935, 645]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[19]: text=输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。, bbox=[25, 643, 924, 672]
2026-08-06 11:02:15,911 INFO     30 [qwen-vl-text] coord item[20]: text=排除禁忌，于2026年3月3日行CT引导下左肺占位穿刺活检术，配合止血，止咳等对症支持治疗，, bbox=[27, 670, 922, 698]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[21]: text=术后病理：（左肺穿刺活检）低分化腺癌。1号蜡块免疫组化：CK(+++)、CK5/6(-)、P40(-)、CK7(++, bbox=[27, 696, 935, 724]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[22]: text=+)、TTF-1(+++)、NapsinA(灶+)、Syn(-)、P53(++80%倾向野生型)、Ki-67(++30%)、SMARCA4(+++)。现患者肺癌, bbox=[27, 722, 934, 750]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[23]: text=诊断明确，暂不考虑抗肿瘤治疗，要求出院，经上级医师同意后予以办理出院。, bbox=[29, 745, 757, 770]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[24]: text=出院情况：患者咳嗽较前好转，无痰中带血，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，, bbox=[75, 773, 934, 801]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[25]: text=夜寐一般，二便可。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，, bbox=[20, 798, 934, 826]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[26]: text=无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。, bbox=[20, 823, 829, 851]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[27]: text=出院诊断：肺恶性肿瘤 左肺 低分化腺癌, bbox=[75, 855, 454, 876]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[28]: text=出院医嘱：建议行抗肿瘤专科治疗。, bbox=[74, 915, 397, 936]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] coord item[29]: text=上级/经治医师签名：, bbox=[573, 949, 753, 977]
2026-08-06 11:02:15,912 INFO     30 [qwen-vl-text] page=6 — 30/30 coords, api_time=14.8s
2026-08-06 11:02:15,913 INFO     30 [qwen-vl-text] new_positions (30):
[[6, 295.872, 471.94800000000004, 0.0, 22.581000000000003], [6, 277.38, 486.42, 29.529000000000003, 82.50750000000001], [6, 123.012, 361.8, 77.29650000000001, 110.29950000000001], [6, 496.872, 525.816, 99.009, 118.11600000000001], [6, 45.828, 211.45200000000003, 147.645, 171.0945], [6, 45.024, 211.45200000000003, 179.7795, 203.229], [6, 44.220000000000006, 152.76000000000002, 211.91400000000002, 234.495], [6, 43.416000000000004, 285.42, 244.917, 269.235], [6, 38.592, 767.0160000000001, 305.712, 330.03000000000003], [6, 21.708000000000002, 759.7800000000001, 329.16150000000005, 354.348], [6, 20.904, 759.7800000000001, 352.61100000000005, 376.92900000000003], [6, 20.904, 759.7800000000001, 376.06050000000005, 400.37850000000003], [6, 20.1, 757.368, 399.51000000000005, 423.82800000000003], [6, 20.1, 764.604, 422.95950000000005, 447.27750000000003], [6, 20.1, 758.172, 445.5405, 469.85850000000005], [6, 20.1, 184.92000000000002, 467.25300000000004, 488.09700000000004], [6, 20.1, 755.76, 489.834, 515.0205000000001], [6, 20.1, 755.76, 513.2835, 537.6015], [6, 20.1, 751.74, 535.8645, 560.1825], [6, 20.1, 742.8960000000001, 558.4455, 583.6320000000001], [6, 21.708000000000002, 741.288, 581.895, 606.2130000000001], [6, 21.708000000000002, 751.74, 604.476, 628.794], [6, 21.708000000000002, 750.936, 627.057, 651.375], [6, 23.316000000000003, 608.628, 647.0325, 668.745], [6, 60.300000000000004, 750.936, 671.3505, 695.6685], [6, 16.080000000000002, 750.936, 693.063, 717.3810000000001], [6, 16.080000000000002, 666.5160000000001, 714.7755000000001, 739.0935000000001], [6, 60.300000000000004, 365.016, 742.5675, 760.806], [6, 59.496, 319.18800000000005, 794.6775, 812.916], [6, 460.692, 605.412, 824.2065, 848.5245000000001]]
2026-08-06 11:02:15,913 INFO     30 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=26.0s
2026-08-06 11:02:15,954 INFO     30 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-06 11:02:15,954 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:02:15,954 INFO     30 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-06 11:02:15,956 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T11:02:15.955+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"0f25d360918611f18dbe1f8f96f1c395": {"id": "0f25d360918611f18dbe1f8f96f1c395", "doc_id": "0e185858918611f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 2063705, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786014039116, "task_type": "dataflow", "root_trace_id": "bb104829c20d4dd6b02c65ac578dd1d9", "root_traceparent": "00-bb104829c20d4dd6b02c65ac578dd1d9-5f56a5362076019b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 11:02:15,974 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:02:15,974 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 11:02:16,977 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:02:16,995 INFO     30 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-06 11:02:16,995 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:02:16,996 INFO     30 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-06 11:02:17,014 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 11:02:17,014 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 11:02:17,015 INFO     30 [qwen-vl-text] positions(201): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 11:02:17,015 INFO     30 [qwen-vl-text] page grouping: [0, 1, 2, 3, 4, 5], lines per page: [32, 30, 88, 11, 34, 6]
2026-08-06 11:02:17,445 INFO     30 [qwen-vl-text] page=0, rect=808x957, img=(2246x2659), dpi=200
2026-08-06 11:02:17,594 INFO     30 [qwen-vl-text] page=1, rect=915x592, img=(2542x1646), dpi=200
2026-08-06 11:02:17,876 INFO     30 [qwen-vl-text] page=2, rect=915x1096, img=(2542x3046), dpi=200
2026-08-06 11:02:17,934 INFO     30 [qwen-vl-text] page=3, rect=915x158, img=(2542x440), dpi=200
2026-08-06 11:02:18,326 INFO     30 [qwen-vl-text] page=4, rect=901x1096, img=(2503x3044), dpi=200
2026-08-06 11:02:18,393 INFO     30 [qwen-vl-text] page=5, rect=915x203, img=(2542x565), dpi=200
2026-08-06 11:02:18,394 INFO     30 [qwen-vl-text] LLM extraction start, text_len=3124
2026-08-06 11:02:18,394 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:02:18,394 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 200, \"encounter_dates\": [\"2026-03-04\", \"2026-03-03\", \"2026-03-12\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "金域医学\nKngMed Diagnostics\n病理诊断报告书\n1/1\n标本条码\n医院\n病人姓名\n科室\n性别\n男\n房/床号\n病理号\n年龄\n49岁\n接收时间\n2026-03-04 15:21:00\n住院/门诊号\n采样时间\n2026-03-03 15:05:43\n患者电话\n申请医生\n项目名称\n免疫组化10项\n送检材料\n临床诊断\n大体描述:\n灰红碎组织一堆，大小1*0.8*0.5cm。取1盒全\n镜下所见:\n诊断意见:\n(左肺穿刺活检)低分化腺癌。\n1号蜡块免疫组化: CK (+++)、CK5/6 (-)、P40 (-)、CK7 (+++)、TTF-1 (+++)、NapsinA (灶+)、Syn (-)、P5\n3 (++80%倾向野生型)、Ki-67 (++30%)、SMARCA4 (+++)。\n基本信息\n受检者基本信息\n受检者姓名：\n性别：男\n年龄：49岁\n病理诊断*：肺腺癌\n用药史*：/\n处方医师：/\n医疗机构：/\n样本基本信息\n肿瘤样本编号：\n肿瘤样本类型：石蜡切片\n肿瘤样本采集部位：/\n肿瘤样本采集日期：/\n样本接收日期：2026-03-12\n注*：以上受检者基本信息来自患者送检时提供信息，而非来自本次检测结果，本次检测不对此内容进行解读。\n结果概览\n项目分类\n检测项目\n检测结果\n基因组变异检测结果\n明确/潜在临床意义的变异\nKRAS p.G13D; TP53 p.G154V\n临床意义不明的变异\n未见变异\n微卫星不稳定评估（MSI）\n微卫星不稳定评估（MSI）\n微卫星稳定型（MSS）\nNGS 质量控制评估结果\n合格\n检测结果及详细解析\n变异检测结果及临床获益\n明确/潜在临床意义的基因变异（靶药）\n基因\n检测结果\n突变频率/拷贝数\n可能获益靶药\n可能耐药靶药\nKRAS\nc.38G>A\nAvutometinib+Defactinib(II-C)\n厄洛替尼*(II-C)\np.G13D\n吉非替尼*(II-C)\nNM_004985.3\nexon2\n6.73%\nAvutometinib+Defactinib(II-C)\n拉罗替尼*(II-C)\n错义突变\n芦康沙妥珠单抗*(II-C)\n佐利替尼*(II-C)\n曲美替尼*(II-C)\n阿法替尼*(II-C)\nDefactinib(II-C)\n阿美替尼*(II-C)\nTVB-2640(II-C)\n贝福替尼*(II-C)\n塞利尼索*(II-C)\n达可替尼*(II-C)\n曲美替尼*+安罗替尼*(II-C)\n厄洛替尼*+贝伐珠单抗*(II-C)\nLifirafenib(II-C)\n厄洛替尼*+雷莫西尤单抗\n(II-C)\nJYP0015(II-C)\n伏美替尼*(II-C)\nMRTX0902(II-C)\n埃克替尼*(II-C)\nRMC-6236(II-C)\n利厄替尼*(II-C)\n芦沃美替尼*(II-D)\n奥希替尼*(II-C)\n妥拉美替尼*(II-D)\n瑞齐替尼*(II-C)\nAvutometinib(II-D)\n瑞厄替尼*(II-C)\nCobimetinib(II-D)\n克唑替尼*(II-D)\n特泊替尼*(II-D)\nSotorasib(II-D)\nTP53\nc.461G>T\nMK-1775(II-C)\n/\np.G154V\nNM_000546.5\nexon5\n7.69%\nA196+Barasertib(II-D)\n错义突变\n明确/潜在临床意义的基因变异（分型/预后）\n基因\n检测结果\n突变频率/拷贝数\n分型/预后提示\nTP53\nc.461G>T\n临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53\np.G154V\n或 STK11 突变的发生可能与较差的生存相关\nNM_000546.5\nexon5\n7.69%\n[PMID:30885352]。\n错义突变\nKRAS\nc.38G>A\n临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53\np.G13D\n或 STK11 突变的发生可能与较差的生存相关\nNM_004985.3\nexon2\n6.73%\n[PMID:30885352]\n错义突变\nNCCN《非小细胞肺癌临床实践指南》提示，检出 KRAS\n突变与未检出该基因突变的患者相比生存预后较差。\nMSI 微卫星不稳定检测结果\nBIOMARKER\n癌种\n检测结果\n免疫治疗相关意义\nMSI\n实体瘤\n微卫星稳定型\n微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。\n(MSS)\n注：免疫治疗疗效影响因子较多，需综合评估，用药谨遵医嘱。\n-实体瘤78基因（组织版）-报告解读\n患者基础信息：患者为肺腺癌，样本类型为石蜡切片。\n基因检测结果：检出KRAS p.G13D、TP53 p.G154V为明确/潜在临床意义的\n变异，检出0个临床意义不明的变异。微卫星稳定型（MSS）。\n结果解读：\n• 分型/预后评估：\n1） 该患者本次检出TP53 p.G154V变异，临床研究表明，在携带KRAS突\n变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P\nMID:30885352]。为临床提供参考。\n2） 该患者本次检出KRAS p.G13D变异，临床研究表明，在携带KRAS突\n变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P\nMID:30885352]。\nNCCN《非小细胞肺癌临床实践指南》提示，检出KRAS突变与未检出\n该基因突变的患者相比生存预后较差。为临床提供参考。\n• 靶向药物：\n1） 该患者本次检出KRAS p.G13D变异，匹配到潜在获益的靶向药物：Av\nutometinib+Defactinib(II-C)，芦康沙妥珠单抗*(II-C)，曲美替尼*(II-\nC)，Defactinib(II-C)，TVB-2640(II-C)，塞利尼索*(II-C)，曲美替尼\n*+安罗替尼*(II-C)，Lifirafenib(II-C)，JYP0015(II-C)，MRTX0902(\nII-C)，RMC-6236(II-C)，芦沃美替尼*(II-D)，妥拉美替尼*(II-D)，Av\nutometinib(II-D)，Cobimetinib(II-D);匹配到潜在耐药的靶向药物：\n厄洛替尼*(II-C)，吉非替尼*(II-C)，拉罗替尼*(II-C)，佐利替尼*(II-\nC)，阿法替尼*(II-C)，阿美替尼*(II-C)，贝福替尼*(II-C)，达可替尼*(II\n-C)，厄洛替尼*+贝伐珠单抗*(II-C)，厄洛替尼*+雷莫西尤单抗*(II-\nC)，伏美替尼*(II-C)，埃克替尼*(II-C)，利厄替尼*(II-C)，奥希替尼*(II\n-C)，瑞齐替尼*(II-C)，瑞厄替尼*(II-C)，克唑替尼*(II-D)，特泊替尼*(I\nI-D)，Sotorasib(II-D)。\n2） 该患者本次检出TP53 p.G154V变异，匹配到潜在获益的靶向药物：M\nK-1775(II-C)，A196+Barasertib(II-D)。\n• 免疫治疗：\n该样本微卫星不稳定性为微卫星稳定型（MSS），提示可能从免疫检查点\n抑制剂单药中获益较小。\n未检测出免疫治疗相关基因变异。\n免疫治疗也需要综合考虑多种因素，以及患者自身临床情况，综合评估，\n以上仅供参考。\n• 化疗药物：\n伊立替康，药物敏感性可能较低。卡培他滨、氟尿嘧啶类药物为基础的化\n疗方案，可能有较低的药物毒副风险。伊立替康，可能有较高的药物剂量需\n求。化疗药物的选择需结合患者的临床情况，具体用药方案还请医生综合判\n断，该检测结果仅供参考。",
    "role": "user"
  }
]
2026-08-06 11:02:35,818 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:02:35,818 INFO     30 [qwen-vl-text] LLM output (len=3279):
{
  "exam_date": "2026-03-04",
  "report_date": null,
  "exam_name": "免疫组化10项; 分子检测",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "大体描述:\n灰红碎组织一堆，大小1*0.8*0.5cm。取1盒全",
  "conclusion": "诊断意见:\n(左肺穿刺活检)低分化腺癌。\n\n1号蜡块免疫组化: CK (+++)、CK5/6 (-)、P40 (-)、CK7 (+++)、TTF-1 (+++)、NapsinA (灶+)、Syn (-)、P53 (++80%倾向野生型)、Ki-67 (++30%)、SMARCA4 (+++)。\n\n结果概览\n项目分类 | 检测项目 | 检测结果\n--- | --- | ---\n基因组变异检测结果 | 明确/潜在临床意义的变异 | KRAS p.G13D; TP53 p.G154V\n | 临床意义不明的变异 | 未见变异\n微卫星不稳定评估（MSI） | 微卫星不稳定评估（MSI） | 微卫星稳定型（MSS）\nNGS 质量控制评估结果 | | 合格\n\n检测结果及详细解析\n变异检测结果及临床获益\n明确/潜在临床意义的基因变异（靶药）\n基因 | 检测结果 | 突变频率/拷贝数 | 可能获益靶药 | 可能耐药靶药\n--- | --- | --- | --- | ---\nKRAS | c.38G>A p.G13D NM_004985.3 exon2 错义突变 | 6.73% | Avutometinib+Defactinib(II-C), 芦康沙妥珠单抗*(II-C), 曲美替尼*(II-C), Defactinib(II-C), TVB-2640(II-C), 塞利尼索*(II-C), 曲美替尼*+安罗替尼*(II-C), Lifirafenib(II-C), JYP0015(II-C), MRTX0902(II-C), RMC-6236(II-C), 芦沃美替尼*(II-D), 妥拉美替尼*(II-D), Avutometinib(II-D), Cobimetinib(II-D) | 厄洛替尼*(II-C), 吉非替尼*(II-C), 拉罗替尼*(II-C), 佐利替尼*(II-C), 阿法替尼*(II-C), 阿美替尼*(II-C), 贝福替尼*(II-C), 达可替尼*(II-C), 厄洛替尼*+贝伐珠单抗*(II-C), 厄洛替尼*+雷莫西尤单抗*(II-C), 伏美替尼*(II-C), 埃克替尼*(II-C), 利厄替尼*(II-C), 奥希替尼*(II-C), 瑞齐替尼*(II-C), 瑞厄替尼*(II-C), 克唑替尼*(II-D), 特泊替尼*(II-D), Sotorasib(II-D)\nTP53 | c.461G>T p.G154V NM_000546.5 exon5 错义突变 | 7.69% | MK-1775(II-C), A196+Barasertib(II-D) | /\n\n明确/潜在临床意义的基因变异（分型/预后）\n基因 | 检测结果 | 突变频率/拷贝数 | 分型/预后提示\n--- | --- | --- | ---\nTP53 | c.461G>T p.G154V NM_000546.5 exon5 错义突变 | 7.69% | 临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53 或 STK11 突变的发生可能与较差的生存相关 [PMID:30885352]。\nKRAS | c.38G>A p.G13D NM_004985.3 exon2 错义突变 | 6.73% | 临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53 或 STK11 突变的发生可能与较差的生存相关 [PMID:30885352]。NCCN《非小细胞肺癌临床实践指南》提示，检出 KRAS 突变与未检出该基因突变的患者相比生存预后较差。\n\nMSI 微卫星不稳定检测结果\nBIOMARKER | 癌种 | 检测结果 | 免疫治疗相关意义\n--- | --- | --- | ---\nMSI (MSS) | 实体瘤 | 微卫星稳定型 | 微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。\n\n注：免疫治疗疗效影响因子较多，需综合评估，用药谨遵医嘱。\n\n-实体瘤78基因（组织版）-报告解读\n患者基础信息：患者为肺腺癌，样本类型为石蜡切片。\n基因检测结果：检出KRAS p.G13D、TP53 p.G154V为明确/潜在临床意义的变异，检出0个临床意义不明的变异。微卫星稳定型（MSS）。\n结果解读：\n• 分型/预后评估：\n1） 该患者本次检出TP53 p.G154V变异，临床研究表明，在携带KRAS突变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[PMID:30885352]。为临床提供参考。\n2） 该患者本次检出KRAS p.G13D变异，临床研究表明，在携带KRAS突变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[PMID:30885352]。NCCN《非小细胞肺癌临床实践指南》提示，检出KRAS突变与未检出该基因突变的患者相比生存预后较差。为临床提供参考。\n• 靶向药物：\n1） 该患者本次检出KRAS p.G13D变异，匹配到潜在获益的靶向药物：Avutometinib+Defactinib(II-C)，芦康沙妥珠单抗*(II-C)，曲美替尼*(II-C)，Defactinib(II-C)，TVB-2640(II-C)，塞利尼索*(II-C)，曲美替尼*+安罗替尼*(II-C)，Lifirafenib(II-C)，JYP0015(II-C)，MRTX0902(II-C)，RMC-6236(II-C)，芦沃美替尼*(II-D)，妥拉美替尼*(II-D)，Avutometinib(II-D)，Cobimetinib(II-D);匹配到潜在耐药的靶向药物：厄洛替尼*(II-C)，吉非替尼*(II-C)，拉罗替尼*(II-C)，佐利替尼*(II-C)，阿法替尼*(II-C)，阿美替尼*(II-C)，贝福替尼*(II-C)，达可替尼*(II-C)，厄洛替尼*+贝伐珠单抗*(II-C)，厄洛替尼*+雷莫西尤单抗*(II-C)，伏美替尼*(II-C)，埃克替尼*(II-C)，利厄替尼*(II-C)，奥希替尼*(II-C)，瑞齐替尼*(II-C)，瑞厄替尼*(II-C)，克唑替尼*(II-D)，特泊替尼*(II-D)，Sotorasib(II-D)。\n2） 该患者本次检出TP53 p.G154V变异，匹配到潜在获益的靶向药物：MK-1775(II-C)，A196+Barasertib(II-D)。\n• 免疫治疗：\n该样本微卫星不稳定性为微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。未检测出免疫治疗相关基因变异。免疫治疗也需要综合考虑多种因素，以及患者自身临床情况，综合评估，以上仅供参考。\n• 化疗药物：\n伊立替康，药物敏感性可能较低。卡培他滨、氟尿嘧啶类药物为基础的化疗方案，可能有较低的药物毒副风险。伊立替康，可能有较高的药物剂量需求。化疗药物的选择需结合患者的临床情况，具体用药方案还请医生综合判断，该检测结果仅供参考。",
  "physician": null,
  "reviewer": null
}
2026-08-06 11:02:35,827 INFO     30 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1244620, prompt_len=1058
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["金域医学", "KngMed Diagnostics", "病理诊断报告书", "1/1", "标本条码", "医院", "病人姓名", "科室", "性别", "男", "房/床号", "病理号", "年龄", "49岁", "接收时间", "2026-03-04 15:21:00", "住院/门诊号", "采样时间", "2026-03-03 15:05:43", "患者电话", "申请医生", "项目名称", "免疫组化10项", "送检材料", "临床诊断", "大体描述:", "灰红碎组织一堆，大小1*0.8*0.5cm。取1盒全", "镜下所见:", "诊断意见:", "(左肺穿刺活检)低分化腺癌。", "1号蜡块免疫组化: CK (+++)、CK5/6 (-)、P40 (-)、CK7 (+++)、TTF-1 (+++)、NapsinA (灶+)、Syn (-)、P5", "3 (++80%倾向野生型)、Ki-67 (++30%)、SMARCA4 (+++)。"]

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
2026-08-06 11:02:46,157 INFO     30 [qwen-vl-text] coord API raw response (len=1721):
[
	{"text": "金域医学", "bbox": [37, 7, 144, 32]},
	{"text": "KngMed Diagnostics", "bbox": [65, 34, 144, 44]},
	{"text": "病理诊断报告书", "bbox": [398, 15, 598, 41]},
	{"text": "1/1", "bbox": [952, 42, 980, 54]},
	{"text": "标本条码", "bbox": [13, 84, 81, 101]},
	{"text": "医院", "bbox": [308, 78, 354, 95]},
	{"text": "病人姓名", "bbox": [13, 106, 81, 122]},
	{"text": "科室", "bbox": [308, 100, 354, 117]},
	{"text": "性别", "bbox": [13, 127, 57, 144]},
	{"text": "男", "bbox": [110, 127, 127, 144]},
	{"text": "房/床号", "bbox": [308, 121, 368, 138]},
	{"text": "病理号", "bbox": [644, 95, 700, 112]},
	{"text": "年龄", "bbox": [13, 149, 57, 166]},
	{"text": "49岁", "bbox": [110, 149, 144, 166]},
	{"text": "接收时间", "bbox": [308, 143, 380, 160]},
	{"text": "2026-03-04 15:21:00", "bbox": [412, 144, 594, 159]},
	{"text": "住院/门诊号", "bbox": [644, 116, 741, 133]},
	{"text": "采样时间", "bbox": [13, 170, 81, 187]},
	{"text": "2026-03-03 15:05:43", "bbox": [110, 170, 285, 185]},
	{"text": "患者电话", "bbox": [308, 165, 380, 182]},
	{"text": "申请医生", "bbox": [644, 139, 717, 156]},
	{"text": "项目名称", "bbox": [13, 192, 81, 209]},
	{"text": "免疫组化10项", "bbox": [110, 191, 212, 207]},
	{"text": "送检材料", "bbox": [644, 162, 717, 179]},
	{"text": "临床诊断", "bbox": [13, 213, 81, 230]},
	{"text": "大体描述:", "bbox": [16, 240, 90, 256]},
	{"text": "灰红碎组织一堆，大小1*0.8*0.5cm。取1盒全", "bbox": [16, 259, 366, 275]},
	{"text": "镜下所见:", "bbox": [16, 325, 92, 341]},
	{"text": "诊断意见:", "bbox": [25, 661, 98, 677]},
	{"text": "(左肺穿刺活检)低分化腺癌。", "bbox": [33, 682, 250, 698]},
	{"text": "1号蜡块免疫组化: CK (+++)、CK5/6 (-)、P40 (-)、CK7 (+++)、TTF-1 (+++)、NapsinA (灶+)、Syn (-)、P5", "bbox": [27, 702, 948, 720]},
	{"text": "3 (++80%倾向野生型)、Ki-67 (++30%)、SMARCA4 (+++)。", "bbox": [27, 717, 490, 734]}
]
2026-08-06 11:02:46,158 INFO     30 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=10.3s
2026-08-06 11:02:46,158 INFO     30 [qwen-vl-text] coord item[0]: text=金域医学, bbox=[37, 7, 144, 32]
2026-08-06 11:02:46,158 INFO     30 [qwen-vl-text] coord item[1]: text=KngMed Diagnostics, bbox=[65, 34, 144, 44]
2026-08-06 11:02:46,158 INFO     30 [qwen-vl-text] coord item[2]: text=病理诊断报告书, bbox=[398, 15, 598, 41]
2026-08-06 11:02:46,158 INFO     30 [qwen-vl-text] coord item[3]: text=1/1, bbox=[952, 42, 980, 54]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[4]: text=标本条码, bbox=[13, 84, 81, 101]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[5]: text=医院, bbox=[308, 78, 354, 95]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[6]: text=病人姓名, bbox=[13, 106, 81, 122]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[7]: text=科室, bbox=[308, 100, 354, 117]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[8]: text=性别, bbox=[13, 127, 57, 144]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[9]: text=男, bbox=[110, 127, 127, 144]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[10]: text=房/床号, bbox=[308, 121, 368, 138]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[11]: text=病理号, bbox=[644, 95, 700, 112]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[12]: text=年龄, bbox=[13, 149, 57, 166]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[13]: text=49岁, bbox=[110, 149, 144, 166]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[14]: text=接收时间, bbox=[308, 143, 380, 160]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[15]: text=2026-03-04 15:21:00, bbox=[412, 144, 594, 159]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[16]: text=住院/门诊号, bbox=[644, 116, 741, 133]
2026-08-06 11:02:46,159 INFO     30 [qwen-vl-text] coord item[17]: text=采样时间, bbox=[13, 170, 81, 187]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[18]: text=2026-03-03 15:05:43, bbox=[110, 170, 285, 185]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[19]: text=患者电话, bbox=[308, 165, 380, 182]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[20]: text=申请医生, bbox=[644, 139, 717, 156]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[21]: text=项目名称, bbox=[13, 192, 81, 209]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[22]: text=免疫组化10项, bbox=[110, 191, 212, 207]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[23]: text=送检材料, bbox=[644, 162, 717, 179]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[24]: text=临床诊断, bbox=[13, 213, 81, 230]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[25]: text=大体描述:, bbox=[16, 240, 90, 256]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[26]: text=灰红碎组织一堆，大小1*0.8*0.5cm。取1盒全, bbox=[16, 259, 366, 275]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[27]: text=镜下所见:, bbox=[16, 325, 92, 341]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[28]: text=诊断意见:, bbox=[25, 661, 98, 677]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[29]: text=(左肺穿刺活检)低分化腺癌。, bbox=[33, 682, 250, 698]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[30]: text=1号蜡块免疫组化: CK (+++)、CK5/6 (-)、P40 (-)、CK7 (+++)、TTF-1 (+++)、NapsinA (灶+)、Syn (-)、P5, bbox=[27, 702, 948, 720]
2026-08-06 11:02:46,160 INFO     30 [qwen-vl-text] coord item[31]: text=3 (++80%倾向野生型)、Ki-67 (++30%)、SMARCA4 (+++)。, bbox=[27, 717, 490, 734]
2026-08-06 11:02:46,161 INFO     30 [qwen-vl-text] page=0 — 32/32 coords, api_time=10.3s
2026-08-06 11:02:46,165 INFO     30 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=261835, prompt_len=1022
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["基本信息", "受检者基本信息", "受检者姓名：", "性别：男", "年龄：49岁", "病理诊断*：肺腺癌", "用药史*：/", "处方医师：/", "医疗机构：/", "样本基本信息", "肿瘤样本编号：", "肿瘤样本类型：石蜡切片", "肿瘤样本采集部位：/", "肿瘤样本采集日期：/", "样本接收日期：2026-03-12", "注*：以上受检者基本信息来自患者送检时提供信息，而非来自本次检测结果，本次检测不对此内容进行解读。", "结果概览", "项目分类", "检测项目", "检测结果", "基因组变异检测结果", "明确/潜在临床意义的变异", "KRAS p.G13D; TP53 p.G154V", "临床意义不明的变异", "未见变异", "微卫星不稳定评估（MSI）", "微卫星不稳定评估（MSI）", "微卫星稳定型（MSS）", "NGS 质量控制评估结果", "合格"]

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
2026-08-06 11:02:55,283 INFO     30 [qwen-vl-text] coord API raw response (len=1635):
[
	{"text": "基本信息", "bbox": [106, 63, 180, 93]},
	{"text": "受检者基本信息", "bbox": [226, 148, 356, 176]},
	{"text": "受检者姓名：", "bbox": [101, 216, 174, 238]},
	{"text": "性别：男", "bbox": [101, 262, 268, 284]},
	{"text": "年龄：49岁", "bbox": [101, 304, 288, 327]},
	{"text": "病理诊断*：肺腺癌", "bbox": [101, 349, 294, 371]},
	{"text": "用药史*：/", "bbox": [101, 392, 262, 414]},
	{"text": "处方医师：/", "bbox": [101, 435, 262, 457]},
	{"text": "医疗机构：/", "bbox": [101, 478, 262, 500]},
	{"text": "样本基本信息", "bbox": [652, 145, 760, 170]},
	{"text": "肿瘤样本编号：", "bbox": [515, 215, 601, 237]},
	{"text": "肿瘤样本类型：石蜡切片", "bbox": [515, 260, 731, 282]},
	{"text": "肿瘤样本采集部位：/", "bbox": [515, 304, 626, 326]},
	{"text": "肿瘤样本采集日期：/", "bbox": [515, 348, 626, 370]},
	{"text": "样本接收日期：2026-03-12", "bbox": [515, 392, 754, 414]},
	{"text": "注*：以上受检者基本信息来自患者送检时提供信息，而非来自本次检测结果，本次检测不对此内容进行解读。", "bbox": [94, 529, 698, 551]},
	{"text": "结果概览", "bbox": [106, 648, 180, 677]},
	{"text": "项目分类", "bbox": [94, 708, 155, 731]},
	{"text": "检测项目", "bbox": [300, 708, 360, 731]},
	{"text": "检测结果", "bbox": [537, 708, 598, 731]},
	{"text": "基因组变异检测结果", "bbox": [94, 787, 214, 809]},
	{"text": "明确/潜在临床意义的变异", "bbox": [300, 760, 454, 782]},
	{"text": "KRAS p.G13D; TP53 p.G154V", "bbox": [537, 760, 731, 782]},
	{"text": "临床意义不明的变异", "bbox": [300, 813, 421, 835]},
	{"text": "未见变异", "bbox": [537, 813, 591, 835]},
	{"text": "微卫星不稳定评估（MSI）", "bbox": [94, 867, 244, 889]},
	{"text": "微卫星不稳定评估（MSI）", "bbox": [300, 867, 450, 889]},
	{"text": "微卫星稳定型（MSS）", "bbox": [537, 867, 667, 889]},
	{"text": "NGS 质量控制评估结果", "bbox": [94, 920, 234, 942]},
	{"text": "合格", "bbox": [537, 920, 564, 942]}
]
2026-08-06 11:02:55,284 INFO     30 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=9.1s
2026-08-06 11:02:55,284 INFO     30 [qwen-vl-text] coord item[0]: text=基本信息, bbox=[106, 63, 180, 93]
2026-08-06 11:02:55,285 INFO     30 [qwen-vl-text] coord item[1]: text=受检者基本信息, bbox=[226, 148, 356, 176]
2026-08-06 11:02:55,285 INFO     30 [qwen-vl-text] coord item[2]: text=受检者姓名：, bbox=[101, 216, 174, 238]
2026-08-06 11:02:55,285 INFO     30 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[101, 262, 268, 284]
2026-08-06 11:02:55,285 INFO     30 [qwen-vl-text] coord item[4]: text=年龄：49岁, bbox=[101, 304, 288, 327]
2026-08-06 11:02:55,285 INFO     30 [qwen-vl-text] coord item[5]: text=病理诊断*：肺腺癌, bbox=[101, 349, 294, 371]
2026-08-06 11:02:55,286 INFO     30 [qwen-vl-text] coord item[6]: text=用药史*：/, bbox=[101, 392, 262, 414]
2026-08-06 11:02:55,286 INFO     30 [qwen-vl-text] coord item[7]: text=处方医师：/, bbox=[101, 435, 262, 457]
2026-08-06 11:02:55,286 INFO     30 [qwen-vl-text] coord item[8]: text=医疗机构：/, bbox=[101, 478, 262, 500]
2026-08-06 11:02:55,286 INFO     30 [qwen-vl-text] coord item[9]: text=样本基本信息, bbox=[652, 145, 760, 170]
2026-08-06 11:02:55,286 INFO     30 [qwen-vl-text] coord item[10]: text=肿瘤样本编号：, bbox=[515, 215, 601, 237]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[11]: text=肿瘤样本类型：石蜡切片, bbox=[515, 260, 731, 282]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[12]: text=肿瘤样本采集部位：/, bbox=[515, 304, 626, 326]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[13]: text=肿瘤样本采集日期：/, bbox=[515, 348, 626, 370]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[14]: text=样本接收日期：2026-03-12, bbox=[515, 392, 754, 414]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[15]: text=注*：以上受检者基本信息来自患者送检时提供信息，而非来自本次检测结果，本次检测不对此内容进行解读。, bbox=[94, 529, 698, 551]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[16]: text=结果概览, bbox=[106, 648, 180, 677]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[17]: text=项目分类, bbox=[94, 708, 155, 731]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[18]: text=检测项目, bbox=[300, 708, 360, 731]
2026-08-06 11:02:55,287 INFO     30 [qwen-vl-text] coord item[19]: text=检测结果, bbox=[537, 708, 598, 731]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[20]: text=基因组变异检测结果, bbox=[94, 787, 214, 809]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[21]: text=明确/潜在临床意义的变异, bbox=[300, 760, 454, 782]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[22]: text=KRAS p.G13D; TP53 p.G154V, bbox=[537, 760, 731, 782]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[23]: text=临床意义不明的变异, bbox=[300, 813, 421, 835]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[24]: text=未见变异, bbox=[537, 813, 591, 835]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[25]: text=微卫星不稳定评估（MSI）, bbox=[94, 867, 244, 889]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[26]: text=微卫星不稳定评估（MSI）, bbox=[300, 867, 450, 889]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[27]: text=微卫星稳定型（MSS）, bbox=[537, 867, 667, 889]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[28]: text=NGS 质量控制评估结果, bbox=[94, 920, 234, 942]
2026-08-06 11:02:55,288 INFO     30 [qwen-vl-text] coord item[29]: text=合格, bbox=[537, 920, 564, 942]
2026-08-06 11:02:55,289 INFO     30 [qwen-vl-text] page=1 — 30/30 coords, api_time=9.1s
2026-08-06 11:02:55,293 INFO     30 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=610211, prompt_len=1948
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共88行）
["检测结果及详细解析", "变异检测结果及临床获益", "明确/潜在临床意义的基因变异（靶药）", "基因", "检测结果", "突变频率/拷贝数", "可能获益靶药", "可能耐药靶药", "KRAS", "c.38G>A", "Avutometinib+Defactinib(II-C)", "厄洛替尼*(II-C)", "p.G13D", "吉非替尼*(II-C)", "NM_004985.3", "exon2", "6.73%", "Avutometinib+Defactinib(II-C)", "拉罗替尼*(II-C)", "错义突变", "芦康沙妥珠单抗*(II-C)", "佐利替尼*(II-C)", "曲美替尼*(II-C)", "阿法替尼*(II-C)", "Defactinib(II-C)", "阿美替尼*(II-C)", "TVB-2640(II-C)", "贝福替尼*(II-C)", "塞利尼索*(II-C)", "达可替尼*(II-C)", "曲美替尼*+安罗替尼*(II-C)", "厄洛替尼*+贝伐珠单抗*(II-C)", "Lifirafenib(II-C)", "厄洛替尼*+雷莫西尤单抗", "(II-C)", "JYP0015(II-C)", "伏美替尼*(II-C)", "MRTX0902(II-C)", "埃克替尼*(II-C)", "RMC-6236(II-C)", "利厄替尼*(II-C)", "芦沃美替尼*(II-D)", "奥希替尼*(II-C)", "妥拉美替尼*(II-D)", "瑞齐替尼*(II-C)", "Avutometinib(II-D)", "瑞厄替尼*(II-C)", "Cobimetinib(II-D)", "克唑替尼*(II-D)", "特泊替尼*(II-D)", "Sotorasib(II-D)", "TP53", "c.461G>T", "MK-1775(II-C)", "/", "p.G154V", "NM_000546.5", "exon5", "7.69%", "A196+Barasertib(II-D)", "错义突变", "明确/潜在临床意义的基因变异（分型/预后）", "基因", "检测结果", "突变频率/拷贝数", "分型/预后提示", "TP53", "c.461G>T", "临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53", "p.G154V", "或 STK11 突变的发生可能与较差的生存相关", "NM_000546.5", "exon5", "7.69%", "[PMID:30885352]。", "错义突变", "KRAS", "c.38G>A", "临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53", "p.G13D", "或 STK11 突变的发生可能与较差的生存相关", "NM_004985.3", "exon2", "6.73%", "[PMID:30885352]", "错义突变", "NCCN《非小细胞肺癌临床实践指南》提示，检出 KRAS", "突变与未检出该基因突变的患者相比生存预后较差。"]

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
2026-08-06 11:03:22,598 INFO     30 [qwen-vl-text] coord API raw response (len=4927):
[
	{"text": "检测结果及详细解析", "bbox": [94, 0, 307, 20]},
	{"text": "变异检测结果及临床获益", "bbox": [100, 45, 305, 63]},
	{"text": "明确/潜在临床意义的基因变异（靶药）", "bbox": [95, 98, 410, 115]},
	{"text": "基因", "bbox": [98, 135, 125, 148]},
	{"text": "检测结果", "bbox": [251, 135, 307, 148]},
	{"text": "突变频率/拷贝数", "bbox": [395, 135, 497, 148]},
	{"text": "可能获益靶药", "bbox": [538, 135, 619, 148]},
	{"text": "可能耐药靶药", "bbox": [728, 135, 809, 148]},
	{"text": "KRAS", "bbox": [98, 331, 139, 343]},
	{"text": "c.38G>A", "bbox": [251, 311, 310, 323]},
	{"text": "Avutometinib+Defactinib(II-C)", "bbox": [538, 202, 719, 235]},
	{"text": "厄洛替尼*(II-C)", "bbox": [728, 164, 822, 176]},
	{"text": "p.G13D", "bbox": [251, 331, 299, 343]},
	{"text": "吉非替尼*(II-C)", "bbox": [728, 183, 822, 195]},
	{"text": "NM_004985.3", "bbox": [98, 351, 193, 363]},
	{"text": "exon2", "bbox": [251, 351, 293, 363]},
	{"text": "6.73%", "bbox": [395, 351, 435, 363]},
	{"text": "Avutometinib+Defactinib(II-C)", "bbox": [538, 202, 719, 235]},
	{"text": "拉罗替尼*(II-C)", "bbox": [728, 202, 822, 214]},
	{"text": "错义突变", "bbox": [251, 370, 307, 382]},
	{"text": "芦康沙妥珠单抗*(II-C)", "bbox": [538, 241, 673, 253]},
	{"text": "佐利替尼*(II-C)", "bbox": [728, 222, 822, 234]},
	{"text": "曲美替尼*(II-C)", "bbox": [538, 261, 632, 273]},
	{"text": "阿法替尼*(II-C)", "bbox": [728, 241, 822, 253]},
	{"text": "Defactinib(II-C)", "bbox": [538, 281, 641, 293]},
	{"text": "阿美替尼*(II-C)", "bbox": [728, 261, 822, 273]},
	{"text": "TVB-2640(II-C)", "bbox": [538, 300, 642, 312]},
	{"text": "贝福替尼*(II-C)", "bbox": [728, 281, 822, 293]},
	{"text": "塞利尼索*(II-C)", "bbox": [538, 320, 632, 332]},
	{"text": "达可替尼*(II-C)", "bbox": [728, 300, 822, 312]},
	{"text": "曲美替尼*+安罗替尼*(II-C)", "bbox": [538, 340, 700, 352]},
	{"text": "厄洛替尼*+贝伐珠单抗*(II-C)", "bbox": [728, 320, 901, 332]},
	{"text": "Lifirafenib(II-C)", "bbox": [538, 360, 641, 372]},
	{"text": "厄洛替尼*+雷莫西尤单抗", "bbox": [728, 340, 877, 352]},
	{"text": "(II-C)", "bbox": [728, 360, 768, 372]},
	{"text": "JYP0015(II-C)", "bbox": [538, 380, 631, 392]},
	{"text": "伏美替尼*(II-C)", "bbox": [728, 380, 822, 392]},
	{"text": "MRTX0902(II-C)", "bbox": [538, 399, 649, 411]},
	{"text": "埃克替尼*(II-C)", "bbox": [728, 399, 822, 411]},
	{"text": "RMC-6236(II-C)", "bbox": [538, 419, 644, 431]},
	{"text": "利厄替尼*(II-C)", "bbox": [728, 419, 822, 431]},
	{"text": "芦沃美替尼*(II-D)", "bbox": [538, 438, 646, 450]},
	{"text": "奥希替尼*(II-C)", "bbox": [728, 438, 822, 450]},
	{"text": "妥拉美替尼*(II-D)", "bbox": [538, 458, 646, 470]},
	{"text": "瑞齐替尼*(II-C)", "bbox": [728, 458, 822, 470]},
	{"text": "Avutometinib(II-D)", "bbox": [538, 477, 665, 489]},
	{"text": "瑞厄替尼*(II-C)", "bbox": [728, 477, 822, 489]},
	{"text": "Cobimetinib(II-D)", "bbox": [538, 497, 655, 509]},
	{"text": "克唑替尼*(II-D)", "bbox": [728, 497, 822, 509]},
	{"text": "特泊替尼*(II-D)", "bbox": [728, 516, 822, 528]},
	{"text": "Sotorasib(II-D)", "bbox": [728, 536, 827, 548]},
	{"text": "TP53", "bbox": [98, 581, 135, 593]},
	{"text": "c.461G>T", "bbox": [251, 562, 314, 574]},
	{"text": "MK-1775(II-C)", "bbox": [538, 591, 628, 603]},
	{"text": "/", "bbox": [728, 601, 736, 613]},
	{"text": "p.G154V", "bbox": [251, 581, 307, 593]},
	{"text": "NM_000546.5", "bbox": [98, 601, 193, 613]},
	{"text": "exon5", "bbox": [251, 601, 293, 613]},
	{"text": "7.69%", "bbox": [395, 601, 435, 613]},
	{"text": "A196+Barasertib(II-D)", "bbox": [538, 611, 683, 623]},
	{"text": "错义突变", "bbox": [251, 621, 307, 633]},
	{"text": "明确/潜在临床意义的基因变异（分型/预后）", "bbox": [95, 715, 455, 732]},
	{"text": "基因", "bbox": [95, 752, 122, 765]},
	{"text": "检测结果", "bbox": [237, 752, 293, 765]},
	{"text": "突变频率/拷贝数", "bbox": [383, 752, 485, 765]},
	{"text": "分型/预后提示", "bbox": [558, 752, 647, 765]},
	{"text": "TP53", "bbox": [98, 801, 131, 813]},
	{"text": "c.461G>T", "bbox": [237, 781, 300, 793]},
	{"text": "临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53", "bbox": [558, 801, 902, 813]},
	{"text": "p.G154V", "bbox": [237, 801, 293, 813]},
	{"text": "或 STK11 突变的发生可能与较差的生存相关", "bbox": [558, 820, 902, 833]},
	{"text": "NM_000546.5", "bbox": [95, 820, 190, 833]},
	{"text": "exon5", "bbox": [237, 820, 279, 833]},
	{"text": "7.69%", "bbox": [383, 820, 423, 833]},
	{"text": "[PMID:30885352]。", "bbox": [558, 839, 682, 852]},
	{"text": "错义突变", "bbox": [237, 840, 293, 852]},
	{"text": "KRAS", "bbox": [95, 905, 135, 917]},
	{"text": "c.38G>A", "bbox": [237, 885, 296, 897]},
	{"text": "临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53", "bbox": [558, 885, 902, 897]},
	{"text": "p.G13D", "bbox": [237, 905, 285, 917]},
	{"text": "或 STK11 突变的发生可能与较差的生存相关", "bbox": [558, 905, 902, 917]},
	{"text": "NM_004985.3", "bbox": [95, 924, 190, 937]},
	{"text": "exon2", "bbox": [237, 924, 279, 937]},
	{"text": "6.73%", "bbox": [383, 924, 423, 937]},
	{"text": "[PMID:30885352]", "bbox": [558, 924, 676, 937]},
	{"text": "错义突变", "bbox": [237, 944, 293, 956]},
	{"text": "NCCN《非小细胞肺癌临床实践指南》提示，检出 KRAS", "bbox": [558, 944, 902, 956]},
	{"text": "突变与未检出该基因突变的患者相比生存预后较差。", "bbox": [558, 963, 860, 976]}
]
2026-08-06 11:03:22,599 INFO     30 [qwen-vl-text] coord API: raw_items=88, valid_items=88, elapsed=27.3s
2026-08-06 11:03:22,599 INFO     30 [qwen-vl-text] coord item[0]: text=检测结果及详细解析, bbox=[94, 0, 307, 20]
2026-08-06 11:03:22,599 INFO     30 [qwen-vl-text] coord item[1]: text=变异检测结果及临床获益, bbox=[100, 45, 305, 63]
2026-08-06 11:03:22,599 INFO     30 [qwen-vl-text] coord item[2]: text=明确/潜在临床意义的基因变异（靶药）, bbox=[95, 98, 410, 115]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[3]: text=基因, bbox=[98, 135, 125, 148]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[4]: text=检测结果, bbox=[251, 135, 307, 148]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[5]: text=突变频率/拷贝数, bbox=[395, 135, 497, 148]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[6]: text=可能获益靶药, bbox=[538, 135, 619, 148]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[7]: text=可能耐药靶药, bbox=[728, 135, 809, 148]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[8]: text=KRAS, bbox=[98, 331, 139, 343]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[9]: text=c.38G>A, bbox=[251, 311, 310, 323]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[10]: text=Avutometinib+Defactinib(II-C), bbox=[538, 202, 719, 235]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[11]: text=厄洛替尼*(II-C), bbox=[728, 164, 822, 176]
2026-08-06 11:03:22,600 INFO     30 [qwen-vl-text] coord item[12]: text=p.G13D, bbox=[251, 331, 299, 343]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[13]: text=吉非替尼*(II-C), bbox=[728, 183, 822, 195]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[14]: text=NM_004985.3, bbox=[98, 351, 193, 363]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[15]: text=exon2, bbox=[251, 351, 293, 363]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[16]: text=6.73%, bbox=[395, 351, 435, 363]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[17]: text=Avutometinib+Defactinib(II-C), bbox=[538, 202, 719, 235]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[18]: text=拉罗替尼*(II-C), bbox=[728, 202, 822, 214]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[19]: text=错义突变, bbox=[251, 370, 307, 382]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[20]: text=芦康沙妥珠单抗*(II-C), bbox=[538, 241, 673, 253]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[21]: text=佐利替尼*(II-C), bbox=[728, 222, 822, 234]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[22]: text=曲美替尼*(II-C), bbox=[538, 261, 632, 273]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[23]: text=阿法替尼*(II-C), bbox=[728, 241, 822, 253]
2026-08-06 11:03:22,601 INFO     30 [qwen-vl-text] coord item[24]: text=Defactinib(II-C), bbox=[538, 281, 641, 293]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[25]: text=阿美替尼*(II-C), bbox=[728, 261, 822, 273]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[26]: text=TVB-2640(II-C), bbox=[538, 300, 642, 312]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[27]: text=贝福替尼*(II-C), bbox=[728, 281, 822, 293]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[28]: text=塞利尼索*(II-C), bbox=[538, 320, 632, 332]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[29]: text=达可替尼*(II-C), bbox=[728, 300, 822, 312]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[30]: text=曲美替尼*+安罗替尼*(II-C), bbox=[538, 340, 700, 352]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[31]: text=厄洛替尼*+贝伐珠单抗*(II-C), bbox=[728, 320, 901, 332]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[32]: text=Lifirafenib(II-C), bbox=[538, 360, 641, 372]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[33]: text=厄洛替尼*+雷莫西尤单抗, bbox=[728, 340, 877, 352]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[34]: text=(II-C), bbox=[728, 360, 768, 372]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[35]: text=JYP0015(II-C), bbox=[538, 380, 631, 392]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[36]: text=伏美替尼*(II-C), bbox=[728, 380, 822, 392]
2026-08-06 11:03:22,602 INFO     30 [qwen-vl-text] coord item[37]: text=MRTX0902(II-C), bbox=[538, 399, 649, 411]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[38]: text=埃克替尼*(II-C), bbox=[728, 399, 822, 411]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[39]: text=RMC-6236(II-C), bbox=[538, 419, 644, 431]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[40]: text=利厄替尼*(II-C), bbox=[728, 419, 822, 431]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[41]: text=芦沃美替尼*(II-D), bbox=[538, 438, 646, 450]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[42]: text=奥希替尼*(II-C), bbox=[728, 438, 822, 450]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[43]: text=妥拉美替尼*(II-D), bbox=[538, 458, 646, 470]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[44]: text=瑞齐替尼*(II-C), bbox=[728, 458, 822, 470]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[45]: text=Avutometinib(II-D), bbox=[538, 477, 665, 489]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[46]: text=瑞厄替尼*(II-C), bbox=[728, 477, 822, 489]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[47]: text=Cobimetinib(II-D), bbox=[538, 497, 655, 509]
2026-08-06 11:03:22,603 INFO     30 [qwen-vl-text] coord item[48]: text=克唑替尼*(II-D), bbox=[728, 497, 822, 509]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[49]: text=特泊替尼*(II-D), bbox=[728, 516, 822, 528]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[50]: text=Sotorasib(II-D), bbox=[728, 536, 827, 548]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[51]: text=TP53, bbox=[98, 581, 135, 593]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[52]: text=c.461G>T, bbox=[251, 562, 314, 574]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[53]: text=MK-1775(II-C), bbox=[538, 591, 628, 603]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[54]: text=/, bbox=[728, 601, 736, 613]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[55]: text=p.G154V, bbox=[251, 581, 307, 593]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[56]: text=NM_000546.5, bbox=[98, 601, 193, 613]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[57]: text=exon5, bbox=[251, 601, 293, 613]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[58]: text=7.69%, bbox=[395, 601, 435, 613]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[59]: text=A196+Barasertib(II-D), bbox=[538, 611, 683, 623]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[60]: text=错义突变, bbox=[251, 621, 307, 633]
2026-08-06 11:03:22,604 INFO     30 [qwen-vl-text] coord item[61]: text=明确/潜在临床意义的基因变异（分型/预后）, bbox=[95, 715, 455, 732]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[62]: text=基因, bbox=[95, 752, 122, 765]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[63]: text=检测结果, bbox=[237, 752, 293, 765]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[64]: text=突变频率/拷贝数, bbox=[383, 752, 485, 765]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[65]: text=分型/预后提示, bbox=[558, 752, 647, 765]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[66]: text=TP53, bbox=[98, 801, 131, 813]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[67]: text=c.461G>T, bbox=[237, 781, 300, 793]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[68]: text=临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53, bbox=[558, 801, 902, 813]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[69]: text=p.G154V, bbox=[237, 801, 293, 813]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[70]: text=或 STK11 突变的发生可能与较差的生存相关, bbox=[558, 820, 902, 833]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[71]: text=NM_000546.5, bbox=[95, 820, 190, 833]
2026-08-06 11:03:22,605 INFO     30 [qwen-vl-text] coord item[72]: text=exon5, bbox=[237, 820, 279, 833]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[73]: text=7.69%, bbox=[383, 820, 423, 833]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[74]: text=[PMID:30885352]。, bbox=[558, 839, 682, 852]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[75]: text=错义突变, bbox=[237, 840, 293, 852]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[76]: text=KRAS, bbox=[95, 905, 135, 917]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[77]: text=c.38G>A, bbox=[237, 885, 296, 897]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[78]: text=临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53, bbox=[558, 885, 902, 897]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[79]: text=p.G13D, bbox=[237, 905, 285, 917]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[80]: text=或 STK11 突变的发生可能与较差的生存相关, bbox=[558, 905, 902, 917]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[81]: text=NM_004985.3, bbox=[95, 924, 190, 937]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[82]: text=exon2, bbox=[237, 924, 279, 937]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[83]: text=6.73%, bbox=[383, 924, 423, 937]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[84]: text=[PMID:30885352], bbox=[558, 924, 676, 937]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[85]: text=错义突变, bbox=[237, 944, 293, 956]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[86]: text=NCCN《非小细胞肺癌临床实践指南》提示，检出 KRAS, bbox=[558, 944, 902, 956]
2026-08-06 11:03:22,606 INFO     30 [qwen-vl-text] coord item[87]: text=突变与未检出该基因突变的患者相比生存预后较差。, bbox=[558, 963, 860, 976]
2026-08-06 11:03:22,607 INFO     30 [qwen-vl-text] page=2 — 88/88 coords, api_time=27.3s
2026-08-06 11:03:22,607 INFO     30 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=107259, prompt_len=771
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共11行）
["MSI 微卫星不稳定检测结果", "BIOMARKER", "癌种", "检测结果", "免疫治疗相关意义", "MSI", "实体瘤", "微卫星稳定型", "微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。", "(MSS)", "注：免疫治疗疗效影响因子较多，需综合评估，用药谨遵医嘱。"]

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
2026-08-06 11:03:26,073 INFO     30 [qwen-vl-text] coord API raw response (len=607):
[
	{"text": "MSI 微卫星不稳定检测结果", "bbox": [94, 70, 317, 166]},
	{"text": "BIOMARKER", "bbox": [94, 327, 179, 398]},
	{"text": "癌种", "bbox": [203, 327, 232, 398]},
	{"text": "检测结果", "bbox": [288, 327, 344, 398]},
	{"text": "免疫治疗相关意义", "bbox": [502, 327, 609, 398]},
	{"text": "MSI", "bbox": [94, 587, 119, 658]},
	{"text": "实体瘤", "bbox": [203, 587, 244, 658]},
	{"text": "微卫星稳定型", "bbox": [288, 516, 370, 587]},
	{"text": "微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。", "bbox": [502, 516, 904, 727]},
	{"text": "(MSS)", "bbox": [288, 658, 337, 727]},
	{"text": "注：免疫治疗疗效影响因子较多，需综合评估，用药谨遵医嘱。", "bbox": [94, 827, 394, 898]}
]
2026-08-06 11:03:26,073 INFO     30 [qwen-vl-text] coord API: raw_items=11, valid_items=11, elapsed=3.5s
2026-08-06 11:03:26,074 INFO     30 [qwen-vl-text] coord item[0]: text=MSI 微卫星不稳定检测结果, bbox=[94, 70, 317, 166]
2026-08-06 11:03:26,074 INFO     30 [qwen-vl-text] coord item[1]: text=BIOMARKER, bbox=[94, 327, 179, 398]
2026-08-06 11:03:26,074 INFO     30 [qwen-vl-text] coord item[2]: text=癌种, bbox=[203, 327, 232, 398]
2026-08-06 11:03:26,074 INFO     30 [qwen-vl-text] coord item[3]: text=检测结果, bbox=[288, 327, 344, 398]
2026-08-06 11:03:26,074 INFO     30 [qwen-vl-text] coord item[4]: text=免疫治疗相关意义, bbox=[502, 327, 609, 398]
2026-08-06 11:03:26,074 INFO     30 [qwen-vl-text] coord item[5]: text=MSI, bbox=[94, 587, 119, 658]
2026-08-06 11:03:26,074 INFO     30 [qwen-vl-text] coord item[6]: text=实体瘤, bbox=[203, 587, 244, 658]
2026-08-06 11:03:26,074 INFO     30 [qwen-vl-text] coord item[7]: text=微卫星稳定型, bbox=[288, 516, 370, 587]
2026-08-06 11:03:26,075 INFO     30 [qwen-vl-text] coord item[8]: text=微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。, bbox=[502, 516, 904, 727]
2026-08-06 11:03:26,075 INFO     30 [qwen-vl-text] coord item[9]: text=(MSS), bbox=[288, 658, 337, 727]
2026-08-06 11:03:26,075 INFO     30 [qwen-vl-text] coord item[10]: text=注：免疫治疗疗效影响因子较多，需综合评估，用药谨遵医嘱。, bbox=[94, 827, 394, 898]
2026-08-06 11:03:26,076 INFO     30 [qwen-vl-text] page=3 — 11/11 coords, api_time=3.5s
2026-08-06 11:03:26,081 INFO     30 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=879551, prompt_len=1841
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["-实体瘤78基因（组织版）-报告解读", "患者基础信息：患者为肺腺癌，样本类型为石蜡切片。", "基因检测结果：检出KRAS p.G13D、TP53 p.G154V为明确/潜在临床意义的", "变异，检出0个临床意义不明的变异。微卫星稳定型（MSS）。", "结果解读：", "• 分型/预后评估：", "1） 该患者本次检出TP53 p.G154V变异，临床研究表明，在携带KRAS突", "变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P", "MID:30885352]。为临床提供参考。", "2） 该患者本次检出KRAS p.G13D变异，临床研究表明，在携带KRAS突", "变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P", "MID:30885352]。", "NCCN《非小细胞肺癌临床实践指南》提示，检出KRAS突变与未检出", "该基因突变的患者相比生存预后较差。为临床提供参考。", "• 靶向药物：", "1） 该患者本次检出KRAS p.G13D变异，匹配到潜在获益的靶向药物：Av", "utometinib+Defactinib(II-C)，芦康沙妥珠单抗*(II-C)，曲美替尼*(II-", "C)，Defactinib(II-C)，TVB-2640(II-C)，塞利尼索*(II-C)，曲美替尼", "*+安罗替尼*(II-C)，Lifirafenib(II-C)，JYP0015(II-C)，MRTX0902(", "II-C)，RMC-6236(II-C)，芦沃美替尼*(II-D)，妥拉美替尼*(II-D)，Av", "utometinib(II-D)，Cobimetinib(II-D);匹配到潜在耐药的靶向药物：", "厄洛替尼*(II-C)，吉非替尼*(II-C)，拉罗替尼*(II-C)，佐利替尼*(II-", "C)，阿法替尼*(II-C)，阿美替尼*(II-C)，贝福替尼*(II-C)，达可替尼*(II", "-C)，厄洛替尼*+贝伐珠单抗*(II-C)，厄洛替尼*+雷莫西尤单抗*(II-", "C)，伏美替尼*(II-C)，埃克替尼*(II-C)，利厄替尼*(II-C)，奥希替尼*(II", "-C)，瑞齐替尼*(II-C)，瑞厄替尼*(II-C)，克唑替尼*(II-D)，特泊替尼*(I", "I-D)，Sotorasib(II-D)。", "2） 该患者本次检出TP53 p.G154V变异，匹配到潜在获益的靶向药物：M", "K-1775(II-C)，A196+Barasertib(II-D)。", "• 免疫治疗：", "该样本微卫星不稳定性为微卫星稳定型（MSS），提示可能从免疫检查点", "抑制剂单药中获益较小。", "未检测出免疫治疗相关基因变异。", "免疫治疗也需要综合考虑多种因素，以及患者自身临床情况，综合评估，"]

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
2026-08-06 11:03:42,071 INFO     30 [qwen-vl-text] coord API raw response (len=2618):
[
	{"text": "-实体瘤78基因（组织版）-报告解读", "bbox": [430, 13, 773, 31]},
	{"text": "患者基础信息：患者为肺腺癌，样本类型为石蜡切片。", "bbox": [137, 41, 620, 60]},
	{"text": "基因检测结果：检出KRAS p.G13D、TP53 p.G154V为明确/潜在临床意义的", "bbox": [137, 68, 845, 88]},
	{"text": "变异，检出0个临床意义不明的变异。微卫星稳定型（MSS）。", "bbox": [137, 97, 700, 115]},
	{"text": "结果解读：", "bbox": [137, 140, 228, 158]},
	{"text": "• 分型/预后评估：", "bbox": [137, 168, 315, 187]},
	{"text": "1） 该患者本次检出TP53 p.G154V变异，临床研究表明，在携带KRAS突", "bbox": [172, 196, 845, 215]},
	{"text": "变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P", "bbox": [208, 225, 845, 244]},
	{"text": "MID:30885352]。为临床提供参考。", "bbox": [208, 253, 542, 272]},
	{"text": "2） 该患者本次检出KRAS p.G13D变异，临床研究表明，在携带KRAS突", "bbox": [172, 281, 845, 300]},
	{"text": "变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P", "bbox": [208, 310, 845, 329]},
	{"text": "MID:30885352]。", "bbox": [208, 339, 377, 357]},
	{"text": "NCCN《非小细胞肺癌临床实践指南》提示，检出KRAS突变与未检出", "bbox": [208, 367, 845, 386]},
	{"text": "该基因突变的患者相比生存预后较差。为临床提供参考。", "bbox": [208, 395, 712, 414]},
	{"text": "• 靶向药物：", "bbox": [137, 424, 264, 442]},
	{"text": "1） 该患者本次检出KRAS p.G13D变异，匹配到潜在获益的靶向药物：Av", "bbox": [172, 452, 845, 471]},
	{"text": "utometinib+Defactinib(II-C)，芦康沙妥珠单抗*(II-C)，曲美替尼*(II-", "bbox": [208, 480, 845, 500]},
	{"text": "C)，Defactinib(II-C)，TVB-2640(II-C)，塞利尼索*(II-C)，曲美替尼", "bbox": [208, 509, 845, 528]},
	{"text": "*+安罗替尼*(II-C)，Lifirafenib(II-C)，JYP0015(II-C)，MRTX0902(", "bbox": [208, 537, 845, 556]},
	{"text": "II-C)，RMC-6236(II-C)，芦沃美替尼*(II-D)，妥拉美替尼*(II-D)，Av", "bbox": [208, 565, 845, 584]},
	{"text": "utometinib(II-D)，Cobimetinib(II-D);匹配到潜在耐药的靶向药物：", "bbox": [208, 593, 834, 613]},
	{"text": "厄洛替尼*(II-C)，吉非替尼*(II-C)，拉罗替尼*(II-C)，佐利替尼*(II-", "bbox": [208, 622, 845, 641]},
	{"text": "C)，阿法替尼*(II-C)，阿美替尼*(II-C)，贝福替尼*(II-C)，达可替尼*(II", "bbox": [208, 650, 845, 670]},
	{"text": "-C)，厄洛替尼*+贝伐珠单抗*(II-C)，厄洛替尼*+雷莫西尤单抗*(II-", "bbox": [208, 678, 845, 698]},
	{"text": "C)，伏美替尼*(II-C)，埃克替尼*(II-C)，利厄替尼*(II-C)，奥希替尼*(II", "bbox": [208, 707, 845, 726]},
	{"text": "-C)，瑞齐替尼*(II-C)，瑞厄替尼*(II-C)，克唑替尼*(II-D)，特泊替尼*(I", "bbox": [208, 735, 845, 755]},
	{"text": "I-D)，Sotorasib(II-D)。", "bbox": [208, 764, 421, 783]},
	{"text": "2） 该患者本次检出TP53 p.G154V变异，匹配到潜在获益的靶向药物：M", "bbox": [172, 792, 845, 811]},
	{"text": "K-1775(II-C)，A196+Barasertib(II-D)。", "bbox": [208, 820, 576, 840]},
	{"text": "• 免疫治疗：", "bbox": [137, 850, 264, 868]},
	{"text": "该样本微卫星不稳定性为微卫星稳定型（MSS），提示可能从免疫检查点", "bbox": [165, 878, 845, 897]},
	{"text": "抑制剂单药中获益较小。", "bbox": [137, 906, 352, 925]},
	{"text": "未检测出免疫治疗相关基因变异。", "bbox": [177, 935, 475, 954]},
	{"text": "免疫治疗也需要综合考虑多种因素，以及患者自身临床情况，综合评估，", "bbox": [190, 963, 834, 982]}
]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=16.0s
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[0]: text=-实体瘤78基因（组织版）-报告解读, bbox=[430, 13, 773, 31]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[1]: text=患者基础信息：患者为肺腺癌，样本类型为石蜡切片。, bbox=[137, 41, 620, 60]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[2]: text=基因检测结果：检出KRAS p.G13D、TP53 p.G154V为明确/潜在临床意义的, bbox=[137, 68, 845, 88]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[3]: text=变异，检出0个临床意义不明的变异。微卫星稳定型（MSS）。, bbox=[137, 97, 700, 115]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[4]: text=结果解读：, bbox=[137, 140, 228, 158]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[5]: text=• 分型/预后评估：, bbox=[137, 168, 315, 187]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[6]: text=1） 该患者本次检出TP53 p.G154V变异，临床研究表明，在携带KRAS突, bbox=[172, 196, 845, 215]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[7]: text=变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P, bbox=[208, 225, 845, 244]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[8]: text=MID:30885352]。为临床提供参考。, bbox=[208, 253, 542, 272]
2026-08-06 11:03:42,072 INFO     30 [qwen-vl-text] coord item[9]: text=2） 该患者本次检出KRAS p.G13D变异，临床研究表明，在携带KRAS突, bbox=[172, 281, 845, 300]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[10]: text=变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P, bbox=[208, 310, 845, 329]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[11]: text=MID:30885352]。, bbox=[208, 339, 377, 357]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[12]: text=NCCN《非小细胞肺癌临床实践指南》提示，检出KRAS突变与未检出, bbox=[208, 367, 845, 386]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[13]: text=该基因突变的患者相比生存预后较差。为临床提供参考。, bbox=[208, 395, 712, 414]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[14]: text=• 靶向药物：, bbox=[137, 424, 264, 442]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[15]: text=1） 该患者本次检出KRAS p.G13D变异，匹配到潜在获益的靶向药物：Av, bbox=[172, 452, 845, 471]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[16]: text=utometinib+Defactinib(II-C)，芦康沙妥珠单抗*(II-C)，曲美替尼*(II-, bbox=[208, 480, 845, 500]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[17]: text=C)，Defactinib(II-C)，TVB-2640(II-C)，塞利尼索*(II-C)，曲美替尼, bbox=[208, 509, 845, 528]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[18]: text=*+安罗替尼*(II-C)，Lifirafenib(II-C)，JYP0015(II-C)，MRTX0902(, bbox=[208, 537, 845, 556]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[19]: text=II-C)，RMC-6236(II-C)，芦沃美替尼*(II-D)，妥拉美替尼*(II-D)，Av, bbox=[208, 565, 845, 584]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[20]: text=utometinib(II-D)，Cobimetinib(II-D);匹配到潜在耐药的靶向药物：, bbox=[208, 593, 834, 613]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[21]: text=厄洛替尼*(II-C)，吉非替尼*(II-C)，拉罗替尼*(II-C)，佐利替尼*(II-, bbox=[208, 622, 845, 641]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[22]: text=C)，阿法替尼*(II-C)，阿美替尼*(II-C)，贝福替尼*(II-C)，达可替尼*(II, bbox=[208, 650, 845, 670]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[23]: text=-C)，厄洛替尼*+贝伐珠单抗*(II-C)，厄洛替尼*+雷莫西尤单抗*(II-, bbox=[208, 678, 845, 698]
2026-08-06 11:03:42,073 INFO     30 [qwen-vl-text] coord item[24]: text=C)，伏美替尼*(II-C)，埃克替尼*(II-C)，利厄替尼*(II-C)，奥希替尼*(II, bbox=[208, 707, 845, 726]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[25]: text=-C)，瑞齐替尼*(II-C)，瑞厄替尼*(II-C)，克唑替尼*(II-D)，特泊替尼*(I, bbox=[208, 735, 845, 755]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[26]: text=I-D)，Sotorasib(II-D)。, bbox=[208, 764, 421, 783]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[27]: text=2） 该患者本次检出TP53 p.G154V变异，匹配到潜在获益的靶向药物：M, bbox=[172, 792, 845, 811]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[28]: text=K-1775(II-C)，A196+Barasertib(II-D)。, bbox=[208, 820, 576, 840]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[29]: text=• 免疫治疗：, bbox=[137, 850, 264, 868]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[30]: text=该样本微卫星不稳定性为微卫星稳定型（MSS），提示可能从免疫检查点, bbox=[165, 878, 845, 897]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[31]: text=抑制剂单药中获益较小。, bbox=[137, 906, 352, 925]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[32]: text=未检测出免疫治疗相关基因变异。, bbox=[177, 935, 475, 954]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] coord item[33]: text=免疫治疗也需要综合考虑多种因素，以及患者自身临床情况，综合评估，, bbox=[190, 963, 834, 982]
2026-08-06 11:03:42,074 INFO     30 [qwen-vl-text] page=4 — 34/34 coords, api_time=16.0s
2026-08-06 11:03:42,075 INFO     30 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=132773, prompt_len=759
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共6行）
["以上仅供参考。", "• 化疗药物：", "伊立替康，药物敏感性可能较低。卡培他滨、氟尿嘧啶类药物为基础的化", "疗方案，可能有较低的药物毒副风险。伊立替康，可能有较高的药物剂量需", "求。化疗药物的选择需结合患者的临床情况，具体用药方案还请医生综合判", "断，该检测结果仅供参考。"]

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
2026-08-06 11:03:44,628 INFO     30 [qwen-vl-text] coord API raw response (len=395):
[
	{"text": "以上仅供参考。", "bbox": [151, 85, 283, 170]},
	{"text": "• 化疗药物：", "bbox": [151, 238, 274, 328]},
	{"text": "伊立替康，药物敏感性可能较低。卡培他滨、氟尿嘧啶类药物为基础的化", "bbox": [184, 388, 848, 480]},
	{"text": "疗方案，可能有较低的药物毒副风险。伊立替康，可能有较高的药物剂量需", "bbox": [148, 538, 848, 630]},
	{"text": "求。化疗药物的选择需结合患者的临床情况，具体用药方案还请医生综合判", "bbox": [148, 688, 848, 780]},
	{"text": "断，该检测结果仅供参考。", "bbox": [150, 848, 383, 938]}
]
2026-08-06 11:03:44,628 INFO     30 [qwen-vl-text] coord API: raw_items=6, valid_items=6, elapsed=2.6s
2026-08-06 11:03:44,628 INFO     30 [qwen-vl-text] coord item[0]: text=以上仅供参考。, bbox=[151, 85, 283, 170]
2026-08-06 11:03:44,628 INFO     30 [qwen-vl-text] coord item[1]: text=• 化疗药物：, bbox=[151, 238, 274, 328]
2026-08-06 11:03:44,628 INFO     30 [qwen-vl-text] coord item[2]: text=伊立替康，药物敏感性可能较低。卡培他滨、氟尿嘧啶类药物为基础的化, bbox=[184, 388, 848, 480]
2026-08-06 11:03:44,629 INFO     30 [qwen-vl-text] coord item[3]: text=疗方案，可能有较低的药物毒副风险。伊立替康，可能有较高的药物剂量需, bbox=[148, 538, 848, 630]
2026-08-06 11:03:44,629 INFO     30 [qwen-vl-text] coord item[4]: text=求。化疗药物的选择需结合患者的临床情况，具体用药方案还请医生综合判, bbox=[148, 688, 848, 780]
2026-08-06 11:03:44,629 INFO     30 [qwen-vl-text] coord item[5]: text=断，该检测结果仅供参考。, bbox=[150, 848, 383, 938]
2026-08-06 11:03:44,630 INFO     30 [qwen-vl-text] page=5 — 6/6 coords, api_time=2.6s
2026-08-06 11:03:44,630 INFO     30 [qwen-vl-text] new_positions (201):
[[0, 29.9145, 116.424, 6.699, 30.624], [0, 52.5525, 116.424, 32.538, 42.108], [0, 321.783, 483.483, 14.354999999999999, 39.237], [0, 769.692, 792.33, 40.193999999999996, 51.678], [0, 10.5105, 65.4885, 80.38799999999999, 96.657], [0, 249.018, 286.209, 74.646, 90.91499999999999], [0, 10.5105, 65.4885, 101.442, 116.75399999999999], [0, 249.018, 286.209, 95.7, 111.969], [0, 10.5105, 46.0845, 121.539, 137.808], [0, 88.935, 102.6795, 121.539, 137.808], [0, 249.018, 297.528, 115.797, 132.066], [0, 520.674, 565.95, 90.91499999999999, 107.184], [0, 10.5105, 46.0845, 142.593, 158.862], [0, 88.935, 116.424, 142.593, 158.862], [0, 249.018, 307.23, 136.851, 153.12], [0, 333.102, 480.249, 137.808, 152.16299999999998], [0, 520.674, 599.0985, 111.012, 127.28099999999999], [0, 10.5105, 65.4885, 162.69, 178.959], [0, 88.935, 230.42249999999999, 162.69, 177.045], [0, 249.018, 307.23, 157.905, 174.174], [0, 520.674, 579.6945, 133.023, 149.292], [0, 10.5105, 65.4885, 183.744, 200.013], [0, 88.935, 171.402, 182.787, 198.099], [0, 520.674, 579.6945, 155.034, 171.303], [0, 10.5105, 65.4885, 203.84099999999998, 220.10999999999999], [0, 12.936, 72.765, 229.67999999999998, 244.992], [0, 12.936, 295.911, 247.863, 263.175], [0, 12.936, 74.382, 311.025, 326.337], [0, 20.2125, 79.233, 632.577, 647.889], [0, 26.6805, 202.125, 652.674, 667.986], [0, 21.8295, 766.458, 671.814, 689.04], [0, 21.8295, 396.165, 686.169, 702.438], [1, 96.99000000000001, 164.70000000000002, 37.3275, 55.1025], [1, 206.79000000000002, 325.74, 87.69, 104.28], [1, 92.415, 159.21, 127.98, 141.01500000000001], [1, 92.415, 245.22, 155.235, 168.27], [1, 92.415, 263.52, 180.12, 193.7475], [1, 92.415, 269.01, 206.7825, 219.81750000000002], [1, 92.415, 239.73000000000002, 232.26000000000002, 245.29500000000002], [1, 92.415, 239.73000000000002, 257.7375, 270.77250000000004], [1, 92.415, 239.73000000000002, 283.21500000000003, 296.25], [1, 596.58, 695.4, 85.91250000000001, 100.72500000000001], [1, 471.225, 549.9150000000001, 127.3875, 140.4225], [1, 471.225, 668.865, 154.05, 167.085], [1, 471.225, 572.7900000000001, 180.12, 193.155], [1, 471.225, 572.7900000000001, 206.19, 219.22500000000002], [1, 471.225, 689.9100000000001, 232.26000000000002, 245.29500000000002], [1, 86.01, 638.6700000000001, 313.4325, 326.46750000000003], [1, 96.99000000000001, 164.70000000000002, 383.94, 401.1225], [1, 86.01, 141.82500000000002, 419.49, 433.1175], [1, 274.5, 329.40000000000003, 419.49, 433.1175], [1, 491.355, 547.1700000000001, 419.49, 433.1175], [1, 86.01, 195.81, 466.2975, 479.33250000000004], [1, 274.5, 415.41, 450.3, 463.33500000000004], [1, 491.355, 668.865, 450.3, 463.33500000000004], [1, 274.5, 385.21500000000003, 481.70250000000004, 494.7375], [1, 491.355, 540.765, 481.70250000000004, 494.7375], [1, 86.01, 223.26000000000002, 513.6975, 526.7325000000001], [1, 274.5, 411.75, 513.6975, 526.7325000000001], [1, 491.355, 610.3050000000001, 513.6975, 526.7325000000001], [1, 86.01, 214.11, 545.1, 558.135], [1, 491.355, 516.0600000000001, 545.1, 558.135], [2, 86.01, 280.90500000000003, 0.0, 21.93], [2, 91.5, 279.075, 49.3425, 69.0795], [2, 86.925, 375.15000000000003, 107.45700000000001, 126.0975], [2, 89.67, 114.375, 148.0275, 162.282], [2, 229.66500000000002, 280.90500000000003, 148.0275, 162.282], [2, 361.425, 454.755, 148.0275, 162.282], [2, 492.27000000000004, 566.385, 148.0275, 162.282], [2, 666.12, 740.235, 148.0275, 162.282], [2, 89.67, 127.185, 362.9415, 376.09950000000003], [2, 229.66500000000002, 283.65000000000003, 341.0115, 354.1695], [2, 492.27000000000004, 657.885, 221.493, 257.6775], [2, 666.12, 752.13, 179.826, 192.984], [2, 229.66500000000002, 273.58500000000004, 362.9415, 376.09950000000003], [2, 666.12, 752.13, 200.6595, 213.8175], [2, 89.67, 176.595, 384.8715, 398.0295], [2, 229.66500000000002, 268.095, 384.8715, 398.0295], [2, 361.425, 398.02500000000003, 384.8715, 398.0295], [2, 492.27000000000004, 657.885, 221.493, 257.6775], [2, 666.12, 752.13, 221.493, 234.651], [2, 229.66500000000002, 280.90500000000003, 405.705, 418.863], [2, 492.27000000000004, 615.7950000000001, 264.2565, 277.41450000000003], [2, 666.12, 752.13, 243.423, 256.581], [2, 492.27000000000004, 578.28, 286.1865, 299.3445], [2, 666.12, 752.13, 264.2565, 277.41450000000003], [2, 492.27000000000004, 586.515, 308.11650000000003, 321.2745], [2, 666.12, 752.13, 286.1865, 299.3445], [2, 492.27000000000004, 587.4300000000001, 328.95, 342.108], [2, 666.12, 752.13, 308.11650000000003, 321.2745], [2, 492.27000000000004, 578.28, 350.88, 364.038], [2, 666.12, 752.13, 328.95, 342.108], [2, 492.27000000000004, 640.5, 372.81, 385.968], [2, 666.12, 824.4150000000001, 350.88, 364.038], [2, 492.27000000000004, 586.515, 394.74, 407.898], [2, 666.12, 802.455, 372.81, 385.968], [2, 666.12, 702.72, 394.74, 407.898], [2, 492.27000000000004, 577.365, 416.67, 429.82800000000003], [2, 666.12, 752.13, 416.67, 429.82800000000003], [2, 492.27000000000004, 593.835, 437.50350000000003, 450.6615], [2, 666.12, 752.13, 437.50350000000003, 450.6615], [2, 492.27000000000004, 589.26, 459.43350000000004, 472.5915], [2, 666.12, 752.13, 459.43350000000004, 472.5915], [2, 492.27000000000004, 591.09, 480.267, 493.425], [2, 666.12, 752.13, 480.267, 493.425], [2, 492.27000000000004, 591.09, 502.197, 515.355], [2, 666.12, 752.13, 502.197, 515.355], [2, 492.27000000000004, 608.475, 523.0305, 536.1885], [2, 666.12, 752.13, 523.0305, 536.1885], [2, 492.27000000000004, 599.325, 544.9605, 558.1185], [2, 666.12, 752.13, 544.9605, 558.1185], [2, 666.12, 752.13, 565.794, 578.952], [2, 666.12, 756.705, 587.724, 600.8820000000001], [2, 89.67, 123.525, 637.0665, 650.2245], [2, 229.66500000000002, 287.31, 616.2330000000001, 629.391], [2, 492.27000000000004, 574.62, 648.0315, 661.1895000000001], [2, 666.12, 673.44, 658.9965, 672.1545], [2, 229.66500000000002, 280.90500000000003, 637.0665, 650.2245], [2, 89.67, 176.595, 658.9965, 672.1545], [2, 229.66500000000002, 268.095, 658.9965, 672.1545], [2, 361.425, 398.02500000000003, 658.9965, 672.1545], [2, 492.27000000000004, 624.945, 669.9615, 683.1195], [2, 229.66500000000002, 280.90500000000003, 680.9265, 694.0845], [2, 86.925, 416.325, 783.9975000000001, 802.638], [2, 86.925, 111.63000000000001, 824.568, 838.8225], [2, 216.85500000000002, 268.095, 824.568, 838.8225], [2, 350.445, 443.77500000000003, 824.568, 838.8225], [2, 510.57, 592.005, 824.568, 838.8225], [2, 89.67, 119.86500000000001, 878.2965, 891.4545], [2, 216.85500000000002, 274.5, 856.3665, 869.5245], [2, 510.57, 825.33, 878.2965, 891.4545], [2, 216.85500000000002, 268.095, 878.2965, 891.4545], [2, 510.57, 825.33, 899.13, 913.3845], [2, 86.925, 173.85, 899.13, 913.3845], [2, 216.85500000000002, 255.285, 899.13, 913.3845], [2, 350.445, 387.045, 899.13, 913.3845], [2, 510.57, 624.03, 919.9635000000001, 934.2180000000001], [2, 216.85500000000002, 268.095, 921.0600000000001, 934.2180000000001], [2, 86.925, 123.525, 992.3325, 1005.4905], [2, 216.85500000000002, 270.84000000000003, 970.4025, 983.5605], [2, 510.57, 825.33, 970.4025, 983.5605], [2, 216.85500000000002, 260.77500000000003, 992.3325, 1005.4905], [2, 510.57, 825.33, 992.3325, 1005.4905], [2, 86.925, 173.85, 1013.166, 1027.4205], [2, 216.85500000000002, 255.285, 1013.166, 1027.4205], [2, 350.445, 387.045, 1013.166, 1027.4205], [2, 510.57, 618.5400000000001, 1013.166, 1027.4205], [2, 216.85500000000002, 268.095, 1035.096, 1048.2540000000001], [2, 510.57, 825.33, 1035.096, 1048.2540000000001], [2, 510.57, 786.9, 1055.9295, 1070.184], [3, 86.01, 290.055, 11.0775, 26.2695], [3, 86.01, 163.785, 51.74775, 62.9835], [3, 185.745, 212.28, 51.74775, 62.9835], [3, 263.52, 314.76, 51.74775, 62.9835], [3, 459.33000000000004, 557.235, 51.74775, 62.9835], [3, 86.01, 108.885, 92.89275, 104.1285], [3, 185.745, 223.26000000000002, 92.89275, 104.1285], [3, 263.52, 338.55, 81.657, 92.89275], [3, 459.33000000000004, 827.1600000000001, 81.657, 115.04775000000001], [3, 263.52, 308.355, 104.1285, 115.04775000000001], [3, 86.01, 360.51, 130.87275, 142.1085], [4, 387.32250000000005, 696.27975, 14.24475, 33.96825], [4, 123.40275000000001, 558.465, 44.92575, 65.745], [4, 123.40275000000001, 761.1337500000001, 74.511, 96.426], [4, 123.40275000000001, 630.5250000000001, 106.28775, 126.01125], [4, 123.40275000000001, 205.371, 153.405, 173.1285], [4, 123.40275000000001, 283.73625000000004, 184.086, 204.90525], [4, 154.929, 761.1337500000001, 214.767, 235.58625], [4, 187.35600000000002, 761.1337500000001, 246.54375, 267.363], [4, 187.35600000000002, 488.2065, 277.22475000000003, 298.044], [4, 154.929, 761.1337500000001, 307.90575, 328.725], [4, 187.35600000000002, 761.1337500000001, 339.6825, 360.50175], [4, 187.35600000000002, 339.58275000000003, 371.45925, 391.18275], [4, 187.35600000000002, 761.1337500000001, 402.14025, 422.9595], [4, 187.35600000000002, 641.3340000000001, 432.82125, 453.6405], [4, 123.40275000000001, 237.798, 464.598, 484.3215], [4, 154.929, 761.1337500000001, 495.279, 516.09825], [4, 187.35600000000002, 761.1337500000001, 525.96, 547.875], [4, 187.35600000000002, 761.1337500000001, 557.73675, 578.556], [4, 187.35600000000002, 761.1337500000001, 588.41775, 609.237], [4, 187.35600000000002, 761.1337500000001, 619.09875, 639.918], [4, 187.35600000000002, 751.2255, 649.77975, 671.69475], [4, 187.35600000000002, 761.1337500000001, 681.5565, 702.37575], [4, 187.35600000000002, 761.1337500000001, 712.2375, 734.1525], [4, 187.35600000000002, 761.1337500000001, 742.9185, 764.8335], [4, 187.35600000000002, 761.1337500000001, 774.69525, 795.5145], [4, 187.35600000000002, 761.1337500000001, 805.37625, 827.29125], [4, 187.35600000000002, 379.21575, 837.153, 857.97225], [4, 154.929, 761.1337500000001, 867.834, 888.65325], [4, 187.35600000000002, 518.832, 898.515, 920.43], [4, 123.40275000000001, 237.798, 931.3875, 951.111], [4, 148.62375, 761.1337500000001, 962.0685, 982.88775], [4, 123.40275000000001, 317.064, 992.7495, 1013.56875], [4, 159.43275, 427.85625000000005, 1024.52625, 1045.3455], [4, 171.1425, 751.2255, 1055.20725, 1076.0265], [5, 138.165, 258.945, 17.276249999999997, 34.552499999999995], [5, 138.165, 250.71, 48.3735, 66.666], [5, 168.36, 775.9200000000001, 78.86099999999999, 97.55999999999999], [5, 135.42000000000002, 775.9200000000001, 109.34849999999999, 128.04749999999999], [5, 135.42000000000002, 775.9200000000001, 139.83599999999998, 158.535], [5, 137.25, 350.445, 172.356, 190.64849999999998]]
2026-08-06 11:03:44,631 INFO     30 [qwen-vl-text] ═══ DONE ═══ 201 positions, pages=6, time=87.6s
2026-08-06 11:03:44,631 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 11:03:44,631 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 11:03:44,631 INFO     30 [qwen-vl-text] positions(32): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 11:03:44,632 INFO     30 [qwen-vl-text] page grouping: [8], lines per page: [32]
2026-08-06 11:03:45,227 INFO     30 [qwen-vl-text] page=8, rect=796x1036, img=(2211x2878), dpi=200
2026-08-06 11:03:45,229 INFO     30 [qwen-vl-text] LLM extraction start, text_len=629
2026-08-06 11:03:45,229 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:03:45,229 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 243, \"bbox_end\": 274, \"encounter_dates\": [\"2026-01-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "长沙市第四医院（长沙市中西医结合医院）\nCT 诊断报告单\n湖南HR\n姓名：\n性别：男\n年龄：49 岁\n门诊号：20260126\n科室：\n水新城)\n床号：\n住院号：\n摄片、\n检查日期：2026/1/26 19:56:46\n报告日期：2026-01-26 20:14:00\n检查项目：(CT)平扫一薄层扫描（加收）,(CT)平扫-胸部\n检查方法：\n影像表现：\n双侧胸廓对称。双肺支气管-血管束稍增多。双肺见散在囊状透亮影，大者位于左肺上叶大小约29×25mm。右肺中\n叶内侧段可见斑点状、条索状高密度影，边界清晰。双肺下垂部见斑片状稍高密度影，边界模糊。左肺上叶尖后段-下\n叶背段见肿块影，大小约80×44×82mm，边缘见分叶，CT值约14HU；余双肺见多发结节影，较大者位于左肺上叶前段\n(IM72)，大小约12×8mm，CT值约32HU。左肺上叶尖后段-下叶背段欠通畅。心脏及大血管界面清晰，心包少许积\n液。左肺门见肿大淋巴结，大者短径约12mm。纵隔见散在小淋巴结影。双侧胸膜无增厚，双侧胸腔未见积液。右侧第\n8、9后肋骨质不规则。左冠状动脉钙化。\n影像诊断：\n1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。\n2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。\n3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。\n4.双肺下垂部坠积性炎症。\n5.心包少许积液。左冠状动脉少许钙化。\n6.右侧第8、9后肋陈旧性骨折可能。\n报告医生：\n审核医生：",
    "role": "user"
  }
]
2026-08-06 11:03:45,233 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T11:03:45.231+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"0f25d360918611f18dbe1f8f96f1c395": {"id": "0f25d360918611f18dbe1f8f96f1c395", "doc_id": "0e185858918611f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 2063705, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786014039116, "task_type": "dataflow", "root_trace_id": "bb104829c20d4dd6b02c65ac578dd1d9", "root_traceparent": "00-bb104829c20d4dd6b02c65ac578dd1d9-5f56a5362076019b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 11:03:50,127 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 11:03:50,127 INFO     30 [qwen-vl-text] LLM output (len=761):
{
  "exam_date": "2026-01-26",
  "report_date": "2026-01-26",
  "exam_name": "(CT)平扫一薄层扫描（加收）,(CT)平扫-胸部",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "双侧胸廓对称。双肺支气管-血管束稍增多。双肺见散在囊状透亮影，大者位于左肺上叶大小约29×25mm。右肺中叶内侧段可见斑点状、条索状高密度影，边界清晰。双肺下垂部见斑片状稍高密度影，边界模糊。左肺上叶尖后段-下叶背段见肿块影，大小约80×44×82mm，边缘见分叶，CT值约14HU；余双肺见多发结节影，较大者位于左肺上叶前段(IM72)，大小约12×8mm，CT值约32HU。左肺上叶尖后段-下叶背段欠通畅。心脏及大血管界面清晰，心包少许积液。左肺门见肿大淋巴结，大者短径约12mm。纵隔见散在小淋巴结影。双侧胸膜无增厚，双侧胸腔未见积液。右侧第8、9后肋骨质不规则。左冠状动脉钙化。",
  "conclusion": "1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。\n2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。\n3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。\n4.双肺下垂部坠积性炎症。\n5.心包少许积液。左冠状动脉少许钙化。\n6.右侧第8、9后肋陈旧性骨折可能。",
  "physician": null,
  "reviewer": null
}
2026-08-06 11:03:50,134 INFO     30 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1216393, prompt_len=1338
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["长沙市第四医院（长沙市中西医结合医院）", "CT 诊断报告单", "湖南HR", "姓名：", "性别：男", "年龄：49 岁", "门诊号：20260126", "科室：", "水新城)", "床号：", "住院号：", "摄片、", "检查日期：2026/1/26 19:56:46", "报告日期：2026-01-26 20:14:00", "检查项目：(CT)平扫一薄层扫描（加收）,(CT)平扫-胸部", "检查方法：", "影像表现：", "双侧胸廓对称。双肺支气管-血管束稍增多。双肺见散在囊状透亮影，大者位于左肺上叶大小约29×25mm。右肺中", "叶内侧段可见斑点状、条索状高密度影，边界清晰。双肺下垂部见斑片状稍高密度影，边界模糊。左肺上叶尖后段-下", "叶背段见肿块影，大小约80×44×82mm，边缘见分叶，CT值约14HU；余双肺见多发结节影，较大者位于左肺上叶前段", "(IM72)，大小约12×8mm，CT值约32HU。左肺上叶尖后段-下叶背段欠通畅。心脏及大血管界面清晰，心包少许积", "液。左肺门见肿大淋巴结，大者短径约12mm。纵隔见散在小淋巴结影。双侧胸膜无增厚，双侧胸腔未见积液。右侧第", "8、9后肋骨质不规则。左冠状动脉钙化。", "影像诊断：", "1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。", "2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。", "3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。", "4.双肺下垂部坠积性炎症。", "5.心包少许积液。左冠状动脉少许钙化。", "6.右侧第8、9后肋陈旧性骨折可能。", "报告医生：", "审核医生："]

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
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord API raw response (len=2013):
[
	{"text": "长沙市第四医院（长沙市中西医结合医院）", "bbox": [111, 15, 738, 71]},
	{"text": "CT 诊断报告单", "bbox": [317, 96, 518, 130]},
	{"text": "湖南HR", "bbox": [18, 118, 103, 140]},
	{"text": "姓名：", "bbox": [20, 155, 71, 173]},
	{"text": "性别：男", "bbox": [245, 146, 315, 166]},
	{"text": "年龄：49 岁", "bbox": [387, 138, 516, 160]},
	{"text": "门诊号：20260126", "bbox": [555, 125, 724, 150]},
	{"text": "科室：", "bbox": [23, 183, 73, 200]},
	{"text": "水新城)", "bbox": [217, 174, 284, 194]},
	{"text": "床号：", "bbox": [389, 167, 440, 187]},
	{"text": "住院号：", "bbox": [555, 157, 627, 178]},
	{"text": "摄片、", "bbox": [25, 210, 81, 228]},
	{"text": "检查日期：2026/1/26 19:56:46", "bbox": [248, 192, 525, 220]},
	{"text": "报告日期：2026-01-26 20:14:00", "bbox": [556, 171, 858, 205]},
	{"text": "检查项目：(CT)平扫一薄层扫描（加收）,(CT)平扫-胸部", "bbox": [28, 232, 455, 265]},
	{"text": "检查方法：", "bbox": [31, 291, 120, 311]},
	{"text": "影像表现：", "bbox": [34, 328, 122, 348]},
	{"text": "双侧胸廓对称。双肺支气管-血管束稍增多。双肺见散在囊状透亮影，大者位于左肺上叶大小约29×25mm。右肺中", "bbox": [69, 323, 910, 369]},
	{"text": "叶内侧段可见斑点状、条索状高密度影，边界清晰。双肺下垂部见斑片状稍高密度影，边界模糊。左肺上叶尖后段-下", "bbox": [37, 338, 910, 387]},
	{"text": "叶背段见肿块影，大小约80×44×82mm，边缘见分叶，CT值约14HU；余双肺见多发结节影，较大者位于左肺上叶前段", "bbox": [38, 353, 904, 400]},
	{"text": "(IM72)，大小约12×8mm，CT值约32HU。左肺上叶尖后段-下叶背段欠通畅。心脏及大血管界面清晰，心包少许积", "bbox": [46, 368, 887, 414]},
	{"text": "液。左肺门见肿大淋巴结，大者短径约12mm。纵隔见散在小淋巴结影。双侧胸膜无增厚，双侧胸腔未见积液。右侧第", "bbox": [40, 383, 904, 428]},
	{"text": "8、9后肋骨质不规则。左冠状动脉钙化。", "bbox": [40, 419, 328, 443]},
	{"text": "影像诊断：", "bbox": [55, 677, 139, 695]},
	{"text": "1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。", "bbox": [55, 687, 489, 711]},
	{"text": "2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。", "bbox": [55, 702, 554, 727]},
	{"text": "3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。", "bbox": [55, 719, 426, 742]},
	{"text": "4.双肺下垂部坠积性炎症。", "bbox": [55, 738, 261, 758]},
	{"text": "5.心包少许积液。左冠状动脉少许钙化。", "bbox": [55, 752, 372, 774]},
	{"text": "6.右侧第8、9后肋陈旧性骨折可能。", "bbox": [55, 770, 337, 790]},
	{"text": "报告医生：", "bbox": [70, 957, 150, 977]},
	{"text": "审核医生：", "bbox": [596, 956, 675, 975]}
]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=13.0s
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[0]: text=长沙市第四医院（长沙市中西医结合医院）, bbox=[111, 15, 738, 71]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[1]: text=CT 诊断报告单, bbox=[317, 96, 518, 130]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[2]: text=湖南HR, bbox=[18, 118, 103, 140]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[20, 155, 71, 173]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[245, 146, 315, 166]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[5]: text=年龄：49 岁, bbox=[387, 138, 516, 160]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[6]: text=门诊号：20260126, bbox=[555, 125, 724, 150]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[7]: text=科室：, bbox=[23, 183, 73, 200]
2026-08-06 11:04:03,145 INFO     30 [qwen-vl-text] coord item[8]: text=水新城), bbox=[217, 174, 284, 194]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[9]: text=床号：, bbox=[389, 167, 440, 187]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[10]: text=住院号：, bbox=[555, 157, 627, 178]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[11]: text=摄片、, bbox=[25, 210, 81, 228]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[12]: text=检查日期：2026/1/26 19:56:46, bbox=[248, 192, 525, 220]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[13]: text=报告日期：2026-01-26 20:14:00, bbox=[556, 171, 858, 205]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[14]: text=检查项目：(CT)平扫一薄层扫描（加收）,(CT)平扫-胸部, bbox=[28, 232, 455, 265]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[15]: text=检查方法：, bbox=[31, 291, 120, 311]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[16]: text=影像表现：, bbox=[34, 328, 122, 348]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[17]: text=双侧胸廓对称。双肺支气管-血管束稍增多。双肺见散在囊状透亮影，大者位于左肺上叶大小约29×25mm。右肺中, bbox=[69, 323, 910, 369]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[18]: text=叶内侧段可见斑点状、条索状高密度影，边界清晰。双肺下垂部见斑片状稍高密度影，边界模糊。左肺上叶尖后段-下, bbox=[37, 338, 910, 387]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[19]: text=叶背段见肿块影，大小约80×44×82mm，边缘见分叶，CT值约14HU；余双肺见多发结节影，较大者位于左肺上叶前段, bbox=[38, 353, 904, 400]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[20]: text=(IM72)，大小约12×8mm，CT值约32HU。左肺上叶尖后段-下叶背段欠通畅。心脏及大血管界面清晰，心包少许积, bbox=[46, 368, 887, 414]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[21]: text=液。左肺门见肿大淋巴结，大者短径约12mm。纵隔见散在小淋巴结影。双侧胸膜无增厚，双侧胸腔未见积液。右侧第, bbox=[40, 383, 904, 428]
2026-08-06 11:04:03,146 INFO     30 [qwen-vl-text] coord item[22]: text=8、9后肋骨质不规则。左冠状动脉钙化。, bbox=[40, 419, 328, 443]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[23]: text=影像诊断：, bbox=[55, 677, 139, 695]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[24]: text=1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。, bbox=[55, 687, 489, 711]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[25]: text=2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。, bbox=[55, 702, 554, 727]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[26]: text=3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。, bbox=[55, 719, 426, 742]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[27]: text=4.双肺下垂部坠积性炎症。, bbox=[55, 738, 261, 758]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[28]: text=5.心包少许积液。左冠状动脉少许钙化。, bbox=[55, 752, 372, 774]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[29]: text=6.右侧第8、9后肋陈旧性骨折可能。, bbox=[55, 770, 337, 790]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[30]: text=报告医生：, bbox=[70, 957, 150, 977]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] coord item[31]: text=审核医生：, bbox=[596, 956, 675, 975]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] page=8 — 32/32 coords, api_time=13.0s
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] new_positions (32):
[[8, 88.32825, 587.2635, 15.536249999999999, 73.53824999999999], [8, 252.25275, 412.19849999999997, 99.43199999999999, 134.64749999999998], [8, 14.3235, 81.96225, 122.21849999999999, 145.005], [8, 15.915, 56.49825, 160.54125, 179.18474999999998], [8, 194.95874999999998, 250.66125, 151.21949999999998, 171.93449999999999], [8, 307.95525, 410.60699999999997, 142.93349999999998, 165.72], [8, 441.64124999999996, 576.1229999999999, 129.46875, 155.36249999999998], [8, 18.30225, 58.089749999999995, 189.54225, 207.14999999999998], [8, 172.67775, 225.993, 180.2205, 200.9355], [8, 309.54675, 350.13, 172.97025, 193.68525], [8, 441.64124999999996, 498.93525, 162.61275, 184.3635], [8, 19.893749999999997, 64.45575, 217.5075, 236.15099999999998], [8, 197.346, 417.76874999999995, 198.86399999999998, 227.86499999999998], [8, 442.43699999999995, 682.7534999999999, 177.11325, 212.32874999999999], [8, 22.281, 362.06624999999997, 240.29399999999998, 274.47375], [8, 24.66825, 95.49, 301.40324999999996, 322.11825], [8, 27.0555, 97.08149999999999, 339.726, 360.441], [8, 54.906749999999995, 724.1324999999999, 334.54724999999996, 382.19174999999996], [8, 29.442749999999997, 724.1324999999999, 350.08349999999996, 400.83525], [8, 30.2385, 719.358, 365.61974999999995, 414.29999999999995], [8, 36.6045, 705.83025, 381.156, 428.8005], [8, 31.83, 719.358, 396.69225, 443.301], [8, 31.83, 261.006, 433.97925, 458.83725], [8, 43.76625, 110.60924999999999, 701.2027499999999, 719.8462499999999], [8, 43.76625, 389.12174999999996, 711.56025, 736.41825], [8, 43.76625, 440.84549999999996, 727.0965, 752.99025], [8, 43.76625, 338.98949999999996, 744.70425, 768.5264999999999], [8, 43.76625, 207.69074999999998, 764.3834999999999, 785.0985], [8, 43.76625, 296.019, 778.884, 801.6705], [8, 43.76625, 268.16775, 797.5274999999999, 818.2425], [8, 55.7025, 119.3625, 991.2127499999999, 1011.92775], [8, 474.267, 537.13125, 990.1769999999999, 1009.8562499999999]]
2026-08-06 11:04:03,147 INFO     30 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=18.5s
2026-08-06 11:04:03,165 INFO     30 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-06 11:04:03,166 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "275 items", "markdown": "", "text": "", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "output_format": "chunks", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 2, \"chunks_Discharge\": 1}"}
2026-08-06 11:04:03,166 INFO     30 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-06 11:04:03,167 INFO     30 [ChunkMerger] Merged 3 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2} (filtered 6 noise chunks)
2026-08-06 11:04:03,582 INFO     30 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-06 11:04:03,583 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "3 items, types={'DischargeRecord': 1, 'ExaminationReport': 2}", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf"}
2026-08-06 11:04:03,583 INFO     30 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-06 11:04:03,915 INFO     30 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786014041216, 'update_date': datetime.datetime(2026, 8, 6, 11, 0, 41), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 638069, 'status': '1'}
2026-08-06 11:04:04,289 INFO     30 [EMBED-PIPELINE] batch[0:16] text_for_embed=长沙益康肿瘤医院
出院记录
性别 男 年龄 49岁 病区
号
入院时间：2026-03-02
出院时间：2026-03-09
住院天数：7天
入院诊断：1.左肺占位性质待查
入院时情况：患者，男，49岁，因咳嗽2月余，发现肺部占位4天入院，目前症见：时有咳嗽，
夜间咳甚，咳吐黄白痰，时有痰中夹带血丝，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，夜寐一
般，二便可，近期体重无减轻。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动
正常，无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。辅助检
查：（2026年1月26日 长沙市第四医院）胸部CT：1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议
CT增强。2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。3.右肺中叶内侧段慢性炎症，
肺气肿、肺大泡。4.双肺下垂部坠积性炎症。5.心包少许积液。左冠状动脉少许钙化。6.右侧第8、9
后肋陈旧性骨折可能。
诊疗经过：入院完善相关检查：血常规：白细胞数目 853×10^9/L；中性粒细胞百分比 56.00%；中性
粒细胞数量 4.78×10^9/L；血小板数目 225.00×10^9/L；红细胞数目 5.25×10^12/L；血红蛋白浓度 163.00
g/L；红细胞压积 48.80%；凝血常规检查：FIB 5.00 g/l；癌胚抗原(CEA) 18.27 ng/mL；鳞状细胞癌相关抗原、
输血前常规检查、肝功能、肾功能、电解质、心肌酶无异常。心电图：1.窦性心律；2.正常心电图。
排除禁忌，于2026年3月3日行CT引导下左肺占位穿刺活检术，配合止血，止咳等对症支持治疗，
术后病理：（左肺穿刺活检）低分化腺癌。1号蜡块免疫组化：CK(+++)、CK5/6(-)、P40(-)、CK7(++
+)、TTF-1(+++)、NapsinA(灶+)、Syn(-)、P53(++80%倾向野生型)、Ki-67(++30%)、SMARCA4(+++)。现患者肺癌
诊断明确，暂不考虑抗肿瘤治疗，要求出院，经上级医师同意后予以办理出院。
出院情况：患者咳嗽较前好转，无痰中带血，食纳可，无恶心呕吐、恶寒发热、腹痛腹胀等不适，
夜寐一般，二便可。查体：浅表淋巴结未扪及，胸廓对称无畸形，胸骨无压痛，两侧呼吸运动正常，
无胸膜摩擦感，双侧语颤正常，叩诊呈清音，未闻及明显干湿啰音，未闻及胸膜摩擦音。
出院诊断：肺恶性肿瘤 左肺 低分化腺癌
出院医嘱：建议行抗肿瘤专科治疗。
上级/经治医师签名：
---
金域医学
KngMed Diagnostics
病理诊断报告书
1/1
标本条码
医院
病人姓名
科室
性别
男
房/床号
病理号
年龄
49岁
接收时间
2026-03-04 15:21:00
住院/门诊号
采样时间
2026-03-03 15:05:43
患者电话
申请医生
项目名称
免疫组化10项
送检材料
临床诊断
大体描述:
灰红碎组织一堆，大小1*0.8*0.5cm。取1盒全
镜下所见:
诊断意见:
(左肺穿刺活检)低分化腺癌。
1号蜡块免疫组化: CK (+++)、CK5/6 (-)、P40 (-)、CK7 (+++)、TTF-1 (+++)、NapsinA (灶+)、Syn (-)、P5
3 (++80%倾向野生型)、Ki-67 (++30%)、SMARCA4 (+++)。
基本信息
受检者基本信息
受检者姓名：
性别：男
年龄：49岁
病理诊断*：肺腺癌
用药史*：/
处方医师：/
医疗机构：/
样本基本信息
肿瘤样本编号：
肿瘤样本类型：石蜡切片
肿瘤样本采集部位：/
肿瘤样本采集日期：/
样本接收日期：2026-03-12
注*：以上受检者基本信息来自患者送检时提供信息，而非来自本次检测结果，本次检测不对此内容进行解读。
结果概览
项目分类
检测项目
检测结果
基因组变异检测结果
明确/潜在临床意义的变异
KRAS p.G13D; TP53 p.G154V
临床意义不明的变异
未见变异
微卫星不稳定评估（MSI）
微卫星不稳定评估（MSI）
微卫星稳定型（MSS）
NGS 质量控制评估结果
合格
检测结果及详细解析
变异检测结果及临床获益
明确/潜在临床意义的基因变异（靶药）
基因
检测结果
突变频率/拷贝数
可能获益靶药
可能耐药靶药
KRAS
c.38G>A
Avutometinib+Defactinib(II-C)
厄洛替尼*(II-C)
p.G13D
吉非替尼*(II-C)
NM_004985.3
exon2
6.73%
Avutometinib+Defactinib(II-C)
拉罗替尼*(II-C)
错义突变
芦康沙妥珠单抗*(II-C)
佐利替尼*(II-C)
曲美替尼*(II-C)
阿法替尼*(II-C)
Defactinib(II-C)
阿美替尼*(II-C)
TVB-2640(II-C)
贝福替尼*(II-C)
塞利尼索*(II-C)
达可替尼*(II-C)
曲美替尼*+安罗替尼*(II-C)
厄洛替尼*+贝伐珠单抗*(II-C)
Lifirafenib(II-C)
厄洛替尼*+雷莫西尤单抗
(II-C)
JYP0015(II-C)
伏美替尼*(II-C)
MRTX0902(II-C)
埃克替尼*(II-C)
RMC-6236(II-C)
利厄替尼*(II-C)
芦沃美替尼*(II-D)
奥希替尼*(II-C)
妥拉美替尼*(II-D)
瑞齐替尼*(II-C)
Avutometinib(II-D)
瑞厄替尼*(II-C)
Cobimetinib(II-D)
克唑替尼*(II-D)
特泊替尼*(II-D)
Sotorasib(II-D)
TP53
c.461G>T
MK-1775(II-C)
/
p.G154V
NM_000546.5
exon5
7.69%
A196+Barasertib(II-D)
错义突变
明确/潜在临床意义的基因变异（分型/预后）
基因
检测结果
突变频率/拷贝数
分型/预后提示
TP53
c.461G>T
临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53
p.G154V
或 STK11 突变的发生可能与较差的生存相关
NM_000546.5
exon5
7.69%
[PMID:30885352]。
错义突变
KRAS
c.38G>A
临床研究表明，在携带 KRAS 突变的肺癌患者中，TP53
p.G13D
或 STK11 突变的发生可能与较差的生存相关
NM_004985.3
exon2
6.73%
[PMID:30885352]
错义突变
NCCN《非小细胞肺癌临床实践指南》提示，检出 KRAS
突变与未检出该基因突变的患者相比生存预后较差。
MSI 微卫星不稳定检测结果
BIOMARKER
癌种
检测结果
免疫治疗相关意义
MSI
实体瘤
微卫星稳定型
微卫星稳定型（MSS），提示可能从免疫检查点抑制剂单药中获益较小。
(MSS)
注：免疫治疗疗效影响因子较多，需综合评估，用药谨遵医嘱。
-实体瘤78基因（组织版）-报告解读
患者基础信息：患者为肺腺癌，样本类型为石蜡切片。
基因检测结果：检出KRAS p.G13D、TP53 p.G154V为明确/潜在临床意义的
变异，检出0个临床意义不明的变异。微卫星稳定型（MSS）。
结果解读：
• 分型/预后评估：
1） 该患者本次检出TP53 p.G154V变异，临床研究表明，在携带KRAS突
变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P
MID:30885352]。为临床提供参考。
2） 该患者本次检出KRAS p.G13D变异，临床研究表明，在携带KRAS突
变的肺癌患者中，TP53或STK11突变的发生可能与较差的生存相关[P
MID:30885352]。
NCCN《非小细胞肺癌临床实践指南》提示，检出KRAS突变与未检出
该基因突变的患者相比生存预后较差。为临床提供参考。
• 靶向药物：
1） 该患者本次检出KRAS p.G13D变异，匹配到潜在获益的靶向药物：Av
utometinib+Defactinib(II-C)，芦康沙妥珠单抗*(II-C)，曲美替尼*(II-
C)，Defactinib(II-C)，TVB-2640(II-C)，塞利尼索*(II-C)，曲美替尼
*+安罗替尼*(II-C)，Lifirafenib(II-C)，JYP0015(II-C)，MRTX0902(
II-C)，RMC-6236(II-C)，芦沃美替尼*(II-D)，妥拉美替尼*(II-D)，Av
utometinib(II-D)，Cobimetinib(II-D);匹配到潜在耐药的靶向药物：
厄洛替尼*(II-C)，吉非替尼*(II-C)，拉罗替尼*(II-C)，佐利替尼*(II-
C)，阿法替尼*(II-C)，阿美替尼*(II-C)，贝福替尼*(II-C)，达可替尼*(II
-C)，厄洛替尼*+贝伐珠单抗*(II-C)，厄洛替尼*+雷莫西尤单抗*(II-
C)，伏美替尼*(II-C)，埃克替尼*(II-C)，利厄替尼*(II-C)，奥希替尼*(II
-C)，瑞齐替尼*(II-C)，瑞厄替尼*(II-C)，克唑替尼*(II-D)，特泊替尼*(I
I-D)，Sotorasib(II-D)。
2） 该患者本次检出TP53 p.G154V变异，匹配到潜在获益的靶向药物：M
K-1775(II-C)，A196+Barasertib(II-D)。
• 免疫治疗：
该样本微卫星不稳定性为微卫星稳定型（MSS），提示可能从免疫检查点
抑制剂单药中获益较小。
未检测出免疫治疗相关基因变异。
免疫治疗也需要综合考虑多种因素，以及患者自身临床情况，综合评估，
以上仅供参考。
• 化疗药物：
伊立替康，药物敏感性可能较低。卡培他滨、氟尿嘧啶类药物为基础的化
疗方案，可能有较低的药物毒副风险。伊立替康，可能有较高的药物剂量需
求。化疗药物的选择需结合患者的临床情况，具体用药方案还请医生综合判
断，该检测结果仅供参考。
---
长沙市第四医院（长沙市中西医结合医院）
CT 诊断报告单
湖南HR
姓名：
性别：男
年龄：49 岁
门诊号：20260126
科室：
水新城)
床号：
住院号：
摄片、
检查日期：2026/1/26 19:56:46
报告日期：2026-01-26 20:14:00
检查项目：(CT)平扫一薄层扫描（加收）,(CT)平扫-胸部
检查方法：
影像表现：
双侧胸廓对称。双肺支气管-血管束稍增多。双肺见散在囊状透亮影，大者位于左肺上叶大小约29×25mm。右肺中
叶内侧段可见斑点状、条索状高密度影，边界清晰。双肺下垂部见斑片状稍高密度影，边界模糊。左肺上叶尖后段-下
叶背段见肿块影，大小约80×44×82mm，边缘见分叶，CT值约14HU；余双肺见多发结节影，较大者位于左肺上叶前段
(IM72)，大小约12×8mm，CT值约32HU。左肺上叶尖后段-下叶背段欠通畅。心脏及大血管界面清晰，心包少许积
液。左肺门见肿大淋巴结，大者短径约12mm。纵隔见散在小淋巴结影。双侧胸膜无增厚，双侧胸腔未见积液。右侧第
8、9后肋骨质不规则。左冠状动脉钙化。
影像诊断：
1.左肺上叶尖后段-下叶背段肿块，肺Ca？建议CT增强。
2.余双肺多发结节，性质待定，建议复查。左肺门淋巴结肿大。
3.右肺中叶内侧段慢性炎症，肺气肿、肺大泡。
4.双肺下垂部坠积性炎症。
5.心包少许积液。左冠状动脉少许钙化。
6.右侧第8、9后肋陈旧性骨折可能。
报告医生：
审核医生：
2026-08-06 11:04:04,781 INFO     30 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-06 11:04:04,781 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "3 items, types={'DischargeRecord': 1, 'ExaminationReport': 2}", "name": "湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf", "embedding_token_consumption": 3538}
2026-08-06 11:04:04,782 INFO     30 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-06 11:04:05,413 INFO     30 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-06 11:04:05,414 INFO     30 [Trace] task=0f25d360 | doc=湘潭-LGJI-肺腺癌-方穹推荐706-IB期.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":3,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-06 11:04:05,422 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 11:04:05,423 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 11:04:05,423 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 11:04:05,441 INFO     30 set_progress(0f25d360918611f18dbe1f8f96f1c395), progress: 0.82, progress_msg: 11:04:05 [DOC Engine]:
Start to index...
2026-08-06 11:04:05,499 INFO     30 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.042s]
2026-08-06 11:04:05,514 INFO     30 set_progress(0f25d360918611f18dbe1f8f96f1c395), progress: 0.8333333333333334, progress_msg: 
2026-08-06 11:04:05,533 INFO     30 set_progress(0f25d360918611f18dbe1f8f96f1c395), progress: 1.0, progress_msg: 11:04:05 Indexing done (0.10s). Task done (204.18s)
2026-08-06 11:04:05,545 INFO     30 [Done], chunks(3), token(3538), elapsed:204.18
2026-08-06 11:04:05,898 INFO     30 handle_task done for task {"id": "0f25d360918611f18dbe1f8f96f1c395", "doc_id": "0e185858918611f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "type": "pdf", "location": "\u6e58\u6f6d-LGJI-\u80ba\u817a\u764c-\u65b9\u7a79\u63a8\u8350706-IB\u671f.pdf", "size": 2063705, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786014039116, "task_type": "dataflow", "root_trace_id": "bb104829c20d4dd6b02c65ac578dd1d9", "root_traceparent": "00-bb104829c20d4dd6b02c65ac578dd1d9-5f56a5362076019b-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
