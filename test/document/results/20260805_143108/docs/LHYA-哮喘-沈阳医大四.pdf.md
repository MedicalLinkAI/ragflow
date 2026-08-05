# 基准结果：LHYA-哮喘-沈阳医大四.pdf

## 基本信息

- 文件：`LHYA-哮喘-沈阳医大四.pdf`
- 大小：4483.0 KB
- PDF 总页数：7
- doc_id：`1f329962908911f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:12  完成时间：2026-08-05T14:31:13  耗时：0.9s
- progress_msg：`04:52:49 Indexing done (0.05s). Task done (152.07s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 2cee7de0 | 1 | 1-1 | 四平市中心人民医院 门诊诊断书 0003316 (患者保管) SPZXYy-JL |
| 2 | d0049d71 | 1 | 2-2 | 四平市中医医院 门诊病历 初诊 2025年11月26日 肾病糖尿病科 姓名 性别 |
| 3 | bba9d46d | 1 | 3-3 | 四平市中医医院 内二疗区 门诊病历 初诊 2025年12月31日 姓名 性别：女 |
| 4 | 7c02fb7f | 2 | 4-5 | 报告时间: 2023-12-27 \multicolumn{2}{c}{预计值} |
| 5 | 161c4f7d | 1 | 6-6 | 信康大药房--佳合分店 单号：250927207100156 日期：2025-0 |
| 6 | 280397df | 1 | 7-7 | 信康大药房--佳合分店 单号：251128207100163 日期：2025-1 |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6, 7]`
- 覆盖页数：7 / 7；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 3 | 0 | 3 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 3, "ExaminationReport": 1, "MedicationRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 6, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 3, "Extractor:Medication": 2, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 04:52:48,701 INFO     29 [ChunkMerger] Merged 6 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 04:50:05,620 INFO     29 handle_task begin for task {"id": "1f65e538908911f1a3da71efcdd7cc1f", "doc_id": "1f329962908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4590577, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905403691, "task_type": "dataflow", "root_trace_id": "171541281f15450ca1ea9d4184057967", "root_traceparent": "00-171541281f15450ca1ea9d4184057967-6239d56a1db4ab47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 04:50:05,933 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-05 04:50:05,975 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 04:50:05,986 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 04:50:05,986 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 04:50:05,999 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 04:50:05,999 INFO     29 ============================================================
2026-08-05 04:50:05,999 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 04:50:05,999 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 04:50:05,999 INFO     29 ============================================================
2026-08-05 04:50:05,999 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 04:50:05,999 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 04:50:06,002 INFO     29 No torch found.
2026-08-05 04:50:06,750 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=7
2026-08-05 04:50:07,000 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1304753, prompt_len=644
2026-08-05 04:50:08,696 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:50:08,696 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-05 04:50:08,703 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1304753, prompt_len=401
2026-08-05 04:50:10,275 INFO     29 [qwen-vl-parser] text API response (len=252):
["四平市中心人民医院", "门诊诊断书", "0003316", "(患者保管)", "SPZXYy-JLLC-042", "姓名", "性别", "女", "年龄", "54岁", "单位", "诊断", "支气管哮喘", "病情诊断摘要依据", "发作性喘息30余年，双肺干", "啰音，诊断支气管哮喘", "医生处理意见", "1.平喘治疗", "2.随访", "医生签字：", "门诊部负责人签字：", "科主任签字：", "门诊部盖章：2023年12月27日", "(无公章和医生章无效)"]
2026-08-05 04:50:10,275 INFO     29 [qwen-vl-parser] page=1 text: 24 lines (bbox 0-23)
2026-08-05 04:50:10,276 INFO     29 [qwen-vl-parser] page=1 text: 24 sections
2026-08-05 04:50:10,439 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1191939, prompt_len=644
2026-08-05 04:50:11,833 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:50:11,834 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 04:50:11,848 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1191939, prompt_len=401
2026-08-05 04:50:14,133 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:50:14.131+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 11, "failed": 0, "current": {"1f65e538908911f1a3da71efcdd7cc1f": {"id": "1f65e538908911f1a3da71efcdd7cc1f", "doc_id": "1f329962908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4590577, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905403691, "task_type": "dataflow", "root_trace_id": "171541281f15450ca1ea9d4184057967", "root_traceparent": "00-171541281f15450ca1ea9d4184057967-6239d56a1db4ab47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:50:15,327 INFO     29 [qwen-vl-parser] text API response (len=599):
["四平市中医医院", "门诊病历", "初诊", "2025年11月26日", "肾病糖尿病科", "姓名", "性别 女性", "年龄 55岁", "门诊号码 202511260272 (1)", "发病日期 2025-11-26", "类别 自费", "保险卡号", "就诊方式 便民门诊费", "医生 王亚新", "联系地址 四平铁西", "联系电话 13689710485", "身份证号", "职业", "体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分", "药物过敏史 无", "主诉: 自述糖尿病4年，支气管哮喘30余年", "病史: 糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/l.，糖化：", "10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。", "临床诊断：2型糖尿病 支气管哮喘急性发作", "治疗方案:", "建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，", "每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。", "结论:", "病程记录:", "医生（印章）：王亚新", "2025年11月27日 11:18"]
2026-08-05 04:50:15,328 INFO     29 [qwen-vl-parser] page=2 text: 31 lines (bbox 24-54)
2026-08-05 04:50:15,329 INFO     29 [qwen-vl-parser] page=2 text: 31 sections
2026-08-05 04:50:15,610 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1442178, prompt_len=644
2026-08-05 04:50:17,087 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-31"}
```
2026-08-05 04:50:17,088 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2025-12-31
2026-08-05 04:50:17,099 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1442178, prompt_len=401
2026-08-05 04:50:22,803 INFO     29 [qwen-vl-parser] text API response (len=488):
["四平市中医医院", "内二疗区", "门诊病历", "初诊", "2025年12月31日", "姓名", "性别：女性", "年龄：55岁", "门诊号码：202512310183", "（1）", "发病日期：2025-12-31", "类别：自费", "保险卡号", "就诊方式：服务号", "医生：张楷婷", "联系地址：吉林省四平市", "联系电话：13689710485", "身份证号：220303197009242283", "职业：", "体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分", "药物过敏史：否", "主诉：发现血糖升高4年", "病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。", "临床诊断：2型糖尿病", "治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊", "结论：", "病程记录：", "医生（印章）：", "2025年12月31日 15:12"]
2026-08-05 04:50:22,803 INFO     29 [qwen-vl-parser] page=3 text: 29 lines (bbox 55-83)
2026-08-05 04:50:22,803 INFO     29 [qwen-vl-parser] page=3 text: 29 sections
2026-08-05 04:50:23,044 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1049499, prompt_len=644
2026-08-05 04:50:24,836 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2023-12-27"
}
```
2026-08-05 04:50:24,836 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2023-12-27
2026-08-05 04:50:24,847 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1049499, prompt_len=756
2026-08-05 04:50:29,401 INFO     29 [qwen-vl-parser] table API response (len=898):
\begin{tabular}{ccccccc}
\hline
\multicolumn{2}{c}{\textbf{预计值}} & \textbf{药前} & \textbf{前/预\%} & \textbf{药后} & \multicolumn{2}{c}{\textbf{后/预\% 改善率 (\%)}} \\
\hline
\textbf{测试日期} & & 23/12/27 & & 23/12/27 & & \\
\textbf{测试时间} & & 15:36:14 & & 15:51:45 & & \\
\hline
MV & [L/min] & 11.71 & 27.39 & 233.8 & & 7.6 \\
VC MAX & [L] & 3.28 & 3.52 & 107.3 & 3.78 & 115.4 \\
FVC & [L] & 3.17 & 3.52 & 110.8 & 3.78 & 119.2 \\
FEV 1 & [L] & 2.71 & 2.11 & 77.7 & 2.39 & 88.3 \\
FEV 1 \% FVC & [\%] & & & & 63.29 & \\
FEV 1 \% VC MAX & [\%] & 79.03 & 59.91 & 75.8 & 63.29 & 80.1 \\
PEF & [L/s] & 6.54 & 4.76 & 72.7 & 4.54 & 69.4 \\
MEF 75 & [L/s] & 5.68 & 2.64 & 46.4 & 3.29 & 58.0 \\
MEF 50 & [L/s] & 3.95 & 1.40 & 35.4 & 1.80 & 45.5 \\
MEF 25 & [L/s] & 1.55 & 0.53 & 34.2 & 0.65 & 42.1 \\
MMEF 75/25 & [L/s] & 3.22 & 1.15 & 35.8 & 1.44 & 44.6 \\
\hline
MVV & [L/min] & 100.45 & & & & \\
\hline
\end{tabular}
2026-08-05 04:50:29,403 INFO     29 [qwen-vl-parser] page=4 table: 23 LaTeX lines (bbox 84-106)
2026-08-05 04:50:29,403 INFO     29 [qwen-vl-parser] page=4 table: 23 sections
2026-08-05 04:50:29,605 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910983, prompt_len=644
2026-08-05 04:50:31,330 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2023-12-27"
}
```
2026-08-05 04:50:31,331 INFO     29 [qwen-vl-parser] page=5 classify=table report_date=2023-12-27
2026-08-05 04:50:31,337 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=910983, prompt_len=756
2026-08-05 04:50:35,705 INFO     29 [qwen-vl-parser] table API response (len=835):
\begin{tabular}{l c c c c}
\hline
& & 预计值 & 实测值 & 实/预 \\
\hline
VT & [L] & 0.59 & 1.51 & 258.6 \\
BF & [1/min] & 20.00 & 18.08 & 90.4 \\
MV & [L/min] & 11.71 & 27.39 & 233.8 \\
VC MAX & [L] & 3.28 & 3.52 & 107.3 \\
ERV & [L] & 0.93 & 1.39 & 149.9 \\
IC & [L] & 2.35 & 2.13 & 90.5 \\
FVC & [L] & 3.17 & 3.52 & 110.8 \\
FEV 1 & [L] & 2.71 & 2.11 & 77.7 \\
FEV 1 \% FVC & [\%] & & 59.91 & \\
FEV 1 \% VC MAX & [\%] & 79.03 & 59.91 & 75.8 \\
PEF & [L/s] & 6.54 & 4.76 & 72.7 \\
MEF 75 & [L/s] & 5.68 & 2.64 & 46.4 \\
MEF 50 & [L/s] & 3.95 & 1.40 & 35.4 \\
MEF 25 & [L/s] & 1.55 & 0.53 & 34.2 \\
MMEF 75/25 & [L/s] & 3.22 & 1.15 & 35.8 \\
FEF 75/85 & [L/s] & 0.85 & 0.35 & 41.0 \\
PIF & [L/s] & & 2.16 & \\
FEF50 \% FIF50 & [\%] & & 78.19 & \\
MVV & [L/min] & 100.45 & & \\
FEV 1*30 & [L/min] & 100.45 & 63.19 & 62.9 \\
\hline
\end{tabular}
2026-08-05 04:50:35,706 INFO     29 [qwen-vl-parser] page=5 table: 27 LaTeX lines (bbox 107-133)
2026-08-05 04:50:35,706 INFO     29 [qwen-vl-parser] page=5 table: 27 sections
2026-08-05 04:50:36,170 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2333855, prompt_len=644
2026-08-05 04:50:41,257 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:50:41,258 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 04:50:41,266 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2333855, prompt_len=401
2026-08-05 04:50:43,980 INFO     29 [qwen-vl-parser] text API response (len=435):
["信康大药房--佳合分店", "单号：250927207100156", "日期：2025-09-27 17:52:20", "会员卡号：13689710485", "姓名：", "积分：37", "总积分：47", "药品名称", "规格", "生产企业/药品上市许可持有人", "产地", "剂型", "批号", "有效期", "数量", "单价", "金额", "12534", "185.00", "沙美特罗替卡松吸入粉雾剂", "50微克/250微克/60泡/盒", "葛兰素史克集团吸入粉雾剂", "JD6K", "2027-06-18", "2盒", "185.00", "370.00", "信康大药房温馨提示：您购买的", "药品需要常温储存(10℃-30℃)", "合计：", "370.00", "实收：", "370.00", "开票员：王影", "营业员：7139", "药品售出无质量问题不退不换！", "电话：0434-3333658"]
2026-08-05 04:50:43,981 INFO     29 [qwen-vl-parser] page=6 text: 37 lines (bbox 134-170)
2026-08-05 04:50:43,981 INFO     29 [qwen-vl-parser] page=6 text: 37 sections
2026-08-05 04:50:44,431 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2194781, prompt_len=644
2026-08-05 04:50:46,779 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:50:46,779 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 04:50:46,791 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2194781, prompt_len=401
2026-08-05 04:50:46,915 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:50:46.914+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 11, "failed": 0, "current": {"1f65e538908911f1a3da71efcdd7cc1f": {"id": "1f65e538908911f1a3da71efcdd7cc1f", "doc_id": "1f329962908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4590577, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905403691, "task_type": "dataflow", "root_trace_id": "171541281f15450ca1ea9d4184057967", "root_traceparent": "00-171541281f15450ca1ea9d4184057967-6239d56a1db4ab47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:50:49,489 INFO     29 [qwen-vl-parser] text API response (len=435):
["信康大药房--佳合分店", "单号：251128207100163", "日期：2025-11-28 16:38:41", "会员卡号：13689710485", "姓名：", "积分：37", "总积分：84", "药品名称", "规格", "生产企业/药品上市许可持有人", "产地", "剂型", "批号", "有效期", "数量", "单价", "金额", "12534", "185.00", "沙美特罗替卡松吸入粉雾剂", "50微克/250微克/60泡/盒", "葛兰素史克集团吸入粉雾剂", "JD6K", "2027-06-18", "2盒", "185.00", "370.00", "信康大药房温馨提示：您购买的", "药品需要常温储存（10℃-30℃）", "合计：", "370.00", "实收：", "370.00", "开票员：张欣", "营业员：7140", "药品售出无质量问题不退不换！", "电话：0434-3333658"]
2026-08-05 04:50:49,490 INFO     29 [qwen-vl-parser] page=7 text: 37 lines (bbox 171-207)
2026-08-05 04:50:49,490 INFO     29 [qwen-vl-parser] page=7 text: 37 sections
2026-08-05 04:50:49,490 INFO     29 [qwen-vl-parser] parse_pdf done: 208 sections from 7 pages.
2026-08-05 04:50:49,503 INFO     29 Close text detector.
2026-08-05 04:50:49,863 INFO     29 Close text recognizer.
2026-08-05 04:50:50,221 INFO     29 Close recognizer.
2026-08-05 04:50:50,552 INFO     29 Close recognizer.
2026-08-05 04:50:51,146 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 04:50:51,146 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Parser:MedLink | outputs={"html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "json"}
2026-08-05 04:50:51,146 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 04:50:51,165 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:50:51,165 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 四平市中心人民医院\n[BBOX-1] 门诊诊断书\n[BBOX-2] 0003316\n[BBOX-3] (患者保管)\n[BBOX-4] SPZXYy-JLLC-042\n[BBOX-5] 姓名\n[BBOX-6] 性别\n[BBOX-7] 女\n[BBOX-8] 年龄\n[BBOX-9] 54岁\n[BBOX-10] 单位\n[BBOX-11] 诊断\n[BBOX-12] 支气管哮喘\n[BBOX-13] 病情诊断摘要依据\n[BBOX-14] 发作性喘息30余年，双肺干\n[BBOX-15] 啰音，诊断支气管哮喘\n[BBOX-16] 医生处理意见\n[BBOX-17] 1.平喘治疗\n[BBOX-18] 2.随访\n[BBOX-19] 医生签字：\n[BBOX-20] 门诊部负责人签字：\n[BBOX-21] 科主任签字：\n[BBOX-22] 门诊部盖章：2023年12月27日\n[BBOX-23] (无公章和医生章无效)\n[BBOX-24] 四平市中医医院\n[BBOX-25] 门诊病历\n[BBOX-26] 初诊\n[BBOX-27] 2025年11月26日\n[BBOX-28] 肾病糖尿病科\n[BBOX-29] 姓名\n[BBOX-30] 性别 女性\n[BBOX-31] 年龄 55岁\n[BBOX-32] 门诊号码 202511260272 (1)\n[BBOX-33] 发病日期 2025-11-26\n[BBOX-34] 类别 自费\n[BBOX-35] 保险卡号\n[BBOX-36] 就诊方式 便民门诊费\n[BBOX-37] 医生 王亚新\n[BBOX-38] 联系地址 四平铁西\n[BBOX-39] 联系电话 13689710485\n[BBOX-40] 身份证号\n[BBOX-41] 职业\n[BBOX-42] 体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分\n[BBOX-43] 药物过敏史 无\n[BBOX-44] 主诉: 自述糖尿病4年，支气管哮喘30余年\n[BBOX-45] 病史: 糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/l.，糖化：\n[BBOX-46] 10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。\n[BBOX-47] 临床诊断：2型糖尿病 支气管哮喘急性发作\n[BBOX-48] 治疗方案:\n[BBOX-49] 建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，\n[BBOX-50] 每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。\n[BBOX-51] 结论:\n[BBOX-52] 病程记录:\n[BBOX-53] 医生（印章）：王亚新\n[BBOX-54] 2025年11月27日 11:18\n[BBOX-55] 四平市中医医院\n[BBOX-56] 内二疗区\n[BBOX-57] 门诊病历\n[BBOX-58] 初诊\n[BBOX-59] 2025年12月31日\n[BBOX-60] 姓名\n[BBOX-61] 性别：女性\n[BBOX-62] 年龄：55岁\n[BBOX-63] 门诊号码：202512310183\n[BBOX-64] （1）\n[BBOX-65] 发病日期：2025-12-31\n[BBOX-66] 类别：自费\n[BBOX-67] 保险卡号\n[BBOX-68] 就诊方式：服务号\n[BBOX-69] 医生：张楷婷\n[BBOX-70] 联系地址：吉林省四平市\n[BBOX-71] 联系电话：13689710485\n[BBOX-72] 身份证号：220303197009242283\n[BBOX-73] 职业：\n[BBOX-74] 体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分\n[BBOX-75] 药物过敏史：否\n[BBOX-76] 主诉：发现血糖升高4年\n[BBOX-77] 病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。\n[BBOX-78] 临床诊断：2型糖尿病\n[BBOX-79] 治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊\n[BBOX-80] 结论：\n[BBOX-81] 病程记录：\n[BBOX-82] 医生（印章）：\n[BBOX-83] 2025年12月31日 15:12\n[BBOX-84] \\begin{tabular}{ccccccc}\n[BBOX-85] 报告时间: 2023-12-27\n[BBOX-86] \\hline\n[BBOX-87] \\multicolumn{2}{c}{\\textbf{预计值}} & \\textbf{药前} & \\textbf{前/预\\%} & \\textbf{药后} & \\multicolumn{2}{c}{\\textbf{后/预\\% 改善率 (\\%)}} \\\\\n[BBOX-88] \\hline\n[BBOX-89] \\textbf{测试日期} & & 23/12/27 & & 23/12/27 & & \\\\\n[BBOX-90] \\textbf{测试时间} & & 15:36:14 & & 15:51:45 & & \\\\\n[BBOX-91] \\hline\n[BBOX-92] MV & [L/min] & 11.71 & 27.39 & 233.8 & & 7.6 \\\\\n[BBOX-93] VC MAX & [L] & 3.28 & 3.52 & 107.3 & 3.78 & 115.4 \\\\\n[BBOX-94] FVC & [L] & 3.17 & 3.52 & 110.8 & 3.78 & 119.2 \\\\\n[BBOX-95] FEV 1 & [L] & 2.71 & 2.11 & 77.7 & 2.39 & 88.3 \\\\\n[BBOX-96] FEV 1 \\% FVC & [\\%] & & & & 63.29 & \\\\\n[BBOX-97] FEV 1 \\% VC MAX & [\\%] & 79.03 & 59.91 & 75.8 & 63.29 & 80.1 \\\\\n[BBOX-98] PEF & [L/s] & 6.54 & 4.76 & 72.7 & 4.54 & 69.4 \\\\\n[BBOX-99] MEF 75 & [L/s] & 5.68 & 2.64 & 46.4 & 3.29 & 58.0 \\\\\n[BBOX-100] MEF 50 & [L/s] & 3.95 & 1.40 & 35.4 & 1.80 & 45.5 \\\\\n[BBOX-101] MEF 25 & [L/s] & 1.55 & 0.53 & 34.2 & 0.65 & 42.1 \\\\\n[BBOX-102] MMEF 75/25 & [L/s] & 3.22 & 1.15 & 35.8 & 1.44 & 44.6 \\\\\n[BBOX-103] \\hline\n[BBOX-104] MVV & [L/min] & 100.45 & & & & \\\\\n[BBOX-105] \\hline\n[BBOX-106] \\end{tabular}\n[BBOX-107] \\begin{tabular}{l c c c c}\n[BBOX-108] 报告时间: 2023-12-27\n[BBOX-109] \\hline\n[BBOX-110] & & 预计值 & 实测值 & 实/预 \\\\\n[BBOX-111] \\hline\n[BBOX-112] VT & [L] & 0.59 & 1.51 & 258.6 \\\\\n[BBOX-113] BF & [1/min] & 20.00 & 18.08 & 90.4 \\\\\n[BBOX-114] MV & [L/min] & 11.71 & 27.39 & 233.8 \\\\\n[BBOX-115] VC MAX & [L] & 3.28 & 3.52 & 107.3 \\\\\n[BBOX-116] ERV & [L] & 0.93 & 1.39 & 149.9 \\\\\n[BBOX-117] IC & [L] & 2.35 & 2.13 & 90.5 \\\\\n[BBOX-118] FVC & [L] & 3.17 & 3.52 & 110.8 \\\\\n[BBOX-119] FEV 1 & [L] & 2.71 & 2.11 & 77.7 \\\\\n[BBOX-120] FEV 1 \\% FVC & [\\%] & & 59.91 & \\\\\n[BBOX-121] FEV 1 \\% VC MAX & [\\%] & 79.03 & 59.91 & 75.8 \\\\\n[BBOX-122] PEF & [L/s] & 6.54 & 4.76 & 72.7 \\\\\n[BBOX-123] MEF 75 & [L/s] & 5.68 & 2.64 & 46.4 \\\\\n[BBOX-124] MEF 50 & [L/s] & 3.95 & 1.40 & 35.4 \\\\\n[BBOX-125] MEF 25 & [L/s] & 1.55 & 0.53 & 34.2 \\\\\n[BBOX-126] MMEF 75/25 & [L/s] & 3.22 & 1.15 & 35.8 \\\\\n[BBOX-127] FEF 75/85 & [L/s] & 0.85 & 0.35 & 41.0 \\\\\n[BBOX-128] PIF & [L/s] & & 2.16 & \\\\\n[BBOX-129] FEF50 \\% FIF50 & [\\%] & & 78.19 & \\\\\n[BBOX-130] MVV & [L/min] & 100.45 & & \\\\\n[BBOX-131] FEV 1*30 & [L/min] & 100.45 & 63.19 & 62.9 \\\\\n[BBOX-132] \\hline\n[BBOX-133] \\end{tabular}\n[BBOX-134] 信康大药房--佳合分店\n[BBOX-135] 单号：250927207100156\n[BBOX-136] 日期：2025-09-27 17:52:20\n[BBOX-137] 会员卡号：13689710485\n[BBOX-138] 姓名：\n[BBOX-139] 积分：37\n[BBOX-140] 总积分：47\n[BBOX-141] 药品名称\n[BBOX-142] 规格\n[BBOX-143] 生产企业/药品上市许可持有人\n[BBOX-144] 产地\n[BBOX-145] 剂型\n[BBOX-146] 批号\n[BBOX-147] 有效期\n[BBOX-148] 数量\n[BBOX-149] 单价\n[BBOX-150] 金额\n[BBOX-151] 12534\n[BBOX-152] 185.00\n[BBOX-153] 沙美特罗替卡松吸入粉雾剂\n[BBOX-154] 50微克/250微克/60泡/盒\n[BBOX-155] 葛兰素史克集团吸入粉雾剂\n[BBOX-156] JD6K\n[BBOX-157] 2027-06-18\n[BBOX-158] 2盒\n[BBOX-159] 185.00\n[BBOX-160] 370.00\n[BBOX-161] 信康大药房温馨提示：您购买的\n[BBOX-162] 药品需要常温储存(10℃-30℃)\n[BBOX-163] 合计：\n[BBOX-164] 370.00\n[BBOX-165] 实收：\n[BBOX-166] 370.00\n[BBOX-167] 开票员：王影\n[BBOX-168] 营业员：7139\n[BBOX-169] 药品售出无质量问题不退不换！\n[BBOX-170] 电话：0434-3333658\n[BBOX-171] 信康大药房--佳合分店\n[BBOX-172] 单号：251128207100163\n[BBOX-173] 日期：2025-11-28 16:38:41\n[BBOX-174] 会员卡号：13689710485\n[BBOX-175] 姓名：\n[BBOX-176] 积分：37\n[BBOX-177] 总积分：84\n[BBOX-178] 药品名称\n[BBOX-179] 规格\n[BBOX-180] 生产企业/药品上市许可持有人\n[BBOX-181] 产地\n[BBOX-182] 剂型\n[BBOX-183] 批号\n[BBOX-184] 有效期\n[BBOX-185] 数量\n[BBOX-186] 单价\n[BBOX-187] 金额\n[BBOX-188] 12534\n[BBOX-189] 185.00\n[BBOX-190] 沙美特罗替卡松吸入粉雾剂\n[BBOX-191] 50微克/250微克/60泡/盒\n[BBOX-192] 葛兰素史克集团吸入粉雾剂\n[BBOX-193] JD6K\n[BBOX-194] 2027-06-18\n[BBOX-195] 2盒\n[BBOX-196] 185.00\n[BBOX-197] 370.00\n[BBOX-198] 信康大药房温馨提示：您购买的\n[BBOX-199] 药品需要常温储存（10℃-30℃）\n[BBOX-200] 合计：\n[BBOX-201] 370.00\n[BBOX-202] 实收：\n[BBOX-203] 370.00\n[BBOX-204] 开票员：张欣\n[BBOX-205] 营业员：7140\n[BBOX-206] 药品售出无质量问题不退不换！\n[BBOX-207] 电话：0434-3333658"
  }
]
2026-08-05 04:50:59,967 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:50:59,982 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'OutpatientRecord': 3, 'ExaminationReport': 1, 'MedicationRecord': 2}
2026-08-05 04:50:59,991 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 04:50:59,991 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 3, 'ExaminationReport': 1, 'MedicationRecord': 2}"}
2026-08-05 04:50:59,991 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 04:50:59,992 INFO     29 [ChunkRouter] Routed 6 chunks into 3 groups: {'chunks_Clinical': 3, 'chunks_Examination': 1, 'chunks_Medication': 2}
2026-08-05 04:51:00,000 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 04:51:00,000 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | ChunkRouter:Router | outputs={"html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 3, 'ExaminationReport': 1, 'MedicationRecord': 2}", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:51:00,000 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 04:51:00,004 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:51:00,004 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:51:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:00,005 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:01,206 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:51:01,211 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 04:51:01,212 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:51:01,212 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 04:51:01,216 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:51:01,216 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:51:01 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:01,217 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:02,054 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:51:02,059 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 04:51:02,059 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:51:02,059 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 04:51:02,063 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:51:02,063 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:51:02,063 INFO     29 [qwen-vl-text] positions(24): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:51:02,063 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [24]
2026-08-05 04:51:02,291 INFO     29 [qwen-vl-text] page=0, rect=595x1058, img=(1654x2940), dpi=200
2026-08-05 04:51:02,292 INFO     29 [qwen-vl-text] LLM extraction start, text_len=179
2026-08-05 04:51:02,292 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:51:02,292 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 23, \"encounter_dates\": [\"2023-12-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四平市中心人民医院\n门诊诊断书\n0003316\n(患者保管)\nSPZXYy-JLLC-042\n姓名\n性别\n女\n年龄\n54岁\n单位\n诊断\n支气管哮喘\n病情诊断摘要依据\n发作性喘息30余年，双肺干\n啰音，诊断支气管哮喘\n医生处理意见\n1.平喘治疗\n2.随访\n医生签字：\n门诊部负责人签字：\n科主任签字：\n门诊部盖章：2023年12月27日\n(无公章和医生章无效)",
    "role": "user"
  }
]
[92m04:51:02 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:02,293 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:03,618 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:51:03,618 INFO     29 [qwen-vl-text] LLM output (len=186):
{
  "encounter_date": "2023-12-27",
  "chief_complaint": null,
  "present_illness": "发作性喘息30余年，双肺干啰音",
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": "1.平喘治疗 2.随访"
}
2026-08-05 04:51:03,618 INFO     29 [qwen-vl-text] Updated encounter_dates=[2023-12-27]
2026-08-05 04:51:03,621 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1984927, prompt_len=864
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["四平市中心人民医院", "门诊诊断书", "0003316", "(患者保管)", "SPZXYy-JLLC-042", "姓名", "性别", "女", "年龄", "54岁", "单位", "诊断", "支气管哮喘", "病情诊断摘要依据", "发作性喘息30余年，双肺干", "啰音，诊断支气管哮喘", "医生处理意见", "1.平喘治疗", "2.随访", "医生签字：", "门诊部负责人签字：", "科主任签字：", "门诊部盖章：2023年12月27日", "(无公章和医生章无效)"]

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
2026-08-05 04:51:11,034 INFO     29 [qwen-vl-text] coord API raw response (len=1262):
[
	{"text": "四平市中心人民医院", "bbox": [246, 197, 580, 214]},
	{"text": "门诊诊断书", "bbox": [122, 223, 381, 250]},
	{"text": "0003316", "bbox": [598, 230, 781, 252]},
	{"text": "(患者保管)", "bbox": [50, 272, 195, 289]},
	{"text": "SPZXYy-JLLC-042", "bbox": [575, 268, 831, 282]},
	{"text": "姓名", "bbox": [71, 300, 145, 318]},
	{"text": "性别", "bbox": [365, 300, 423, 317],
	"bbox": [515, 303, 554, 322]},
	{"text": "女", "bbox": [515, 303, 554, 322]},
	{"text": "年龄", "bbox": [615, 300, 672, 316]},
	{"text": "54岁", "bbox": [743, 298, 809, 324]},
	{"text": "单位", "bbox": [70, 334, 144, 351]},
	{"text": "诊断", "bbox": [67, 367, 142, 384]},
	{"text": "支气管哮喘", "bbox": [300, 366, 501, 398]},
	{"text": "病情诊断摘要依据", "bbox": [64, 451, 138, 536]},
	{"text": "发作性喘息30余年，双肺干", "bbox": [275, 400, 777, 440]},
	{"text": "啰音，诊断支气管哮喘", "bbox": [203, 437, 651, 477]},
	{"text": "医生处理意见", "bbox": [78, 631, 108, 769]},
	{"text": "1.平喘治疗", "bbox": [323, 608, 517, 644]},
	{"text": "2.随访", "bbox": [325, 647, 460, 687]},
	{"text": "医生签字：", "bbox": [183, 748, 291, 765]},
	{"text": "门诊部负责人签字：", "bbox": [497, 748, 704, 767]},
	{"text": "科主任签字：", "bbox": [182, 777, 315, 795]},
	{"text": "门诊部盖章：2023年12月27日", "bbox": [498, 777, 828, 798]},
	{"text": "(无公章和医生章无效)", "bbox": [75, 817, 378, 836]}
]
2026-08-05 04:51:11,035 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=7.4s
2026-08-05 04:51:11,035 INFO     29 [qwen-vl-text] coord item[0]: text=四平市中心人民医院, bbox=[246, 197, 580, 214]
2026-08-05 04:51:11,035 INFO     29 [qwen-vl-text] coord item[1]: text=门诊诊断书, bbox=[122, 223, 381, 250]
2026-08-05 04:51:11,035 INFO     29 [qwen-vl-text] coord item[2]: text=0003316, bbox=[598, 230, 781, 252]
2026-08-05 04:51:11,035 INFO     29 [qwen-vl-text] coord item[3]: text=(患者保管), bbox=[50, 272, 195, 289]
2026-08-05 04:51:11,035 INFO     29 [qwen-vl-text] coord item[4]: text=SPZXYy-JLLC-042, bbox=[575, 268, 831, 282]
2026-08-05 04:51:11,035 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[71, 300, 145, 318]
2026-08-05 04:51:11,035 INFO     29 [qwen-vl-text] coord item[6]: text=性别, bbox=[515, 303, 554, 322]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[7]: text=女, bbox=[515, 303, 554, 322]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[8]: text=年龄, bbox=[615, 300, 672, 316]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[9]: text=54岁, bbox=[743, 298, 809, 324]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[10]: text=单位, bbox=[70, 334, 144, 351]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[11]: text=诊断, bbox=[67, 367, 142, 384]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[12]: text=支气管哮喘, bbox=[300, 366, 501, 398]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[13]: text=病情诊断摘要依据, bbox=[64, 451, 138, 536]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[14]: text=发作性喘息30余年，双肺干, bbox=[275, 400, 777, 440]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[15]: text=啰音，诊断支气管哮喘, bbox=[203, 437, 651, 477]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[16]: text=医生处理意见, bbox=[78, 631, 108, 769]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[17]: text=1.平喘治疗, bbox=[323, 608, 517, 644]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[18]: text=2.随访, bbox=[325, 647, 460, 687]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[19]: text=医生签字：, bbox=[183, 748, 291, 765]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[20]: text=门诊部负责人签字：, bbox=[497, 748, 704, 767]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[21]: text=科主任签字：, bbox=[182, 777, 315, 795]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[22]: text=门诊部盖章：2023年12月27日, bbox=[498, 777, 828, 798]
2026-08-05 04:51:11,036 INFO     29 [qwen-vl-text] coord item[23]: text=(无公章和医生章无效), bbox=[75, 817, 378, 836]
2026-08-05 04:51:11,037 INFO     29 [qwen-vl-text] page=0 — 24/24 coords, api_time=7.4s
2026-08-05 04:51:11,037 INFO     29 [qwen-vl-text] new_positions (24):
[[0, 146.43780615234374, 345.2598681640625, 208.47876098632813, 226.46931396484374], [0, 72.62362744140624, 226.8000168457031, 235.99372436523439, 264.56695556640625], [0, 355.9748295898437, 464.9102707519531, 243.40159912109374, 266.6834912109375], [0, 29.763781738281246, 116.07874877929686, 287.84884765625, 305.83940063476564], [0, 342.28348999023433, 494.6740524902343, 283.6157763671875, 298.43152587890626], [0, 42.26457006835937, 86.31496704101562, 317.4803466796875, 336.52916748046874], [0, 306.56695190429684, 329.78270166015625, 320.65515014648435, 340.7622387695312], [0, 306.56695190429684, 329.78270166015625, 320.65515014648435, 340.7622387695312], [0, 366.0945153808593, 400.02522656249994, 317.4803466796875, 334.4126318359375], [0, 442.2897966308593, 481.5779885253906, 315.36381103515623, 342.8787744140625], [0, 41.66929443359375, 85.71969140624999, 353.4614526367188, 371.4520056152344], [0, 39.88346752929687, 84.52914013671874, 388.38429077148436, 406.37484374999997], [0, 178.5826904296875, 298.2330930175781, 387.3260229492187, 421.19059326171873], [0, 38.097640625, 82.14803759765624, 477.2787878417969, 567.231552734375], [0, 163.70079956054687, 462.52916821289057, 423.30712890625, 465.637841796875], [0, 120.84095385742187, 387.52443823242186, 462.4630383300781, 504.79375122070314], [0, 46.43149951171875, 64.2897685546875, 667.7669958496093, 813.8079553222656], [0, 192.27403002929685, 307.7575031738281, 643.4268359375, 681.5244775390624], [0, 193.4645812988281, 273.82679199218745, 684.6992810058593, 727.0299938964844], [0, 108.93544116210937, 173.22520971679685, 791.5843310546875, 809.5748840332031], [0, 295.8519904785156, 419.07404687499996, 791.5843310546875, 811.6914196777344], [0, 108.34016552734374, 187.51182495117186, 822.2740979003906, 841.3229187011718], [0, 296.4472661132812, 492.88822558593745, 822.2740979003906, 844.4977221679687], [0, 44.64567260742187, 225.01418994140624, 864.6048107910157, 884.7118994140625]]
2026-08-05 04:51:11,038 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=9.0s
2026-08-05 04:51:11,038 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:51:11,038 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:51:11,038 INFO     29 [qwen-vl-text] positions(31): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:51:11,038 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [31]
2026-08-05 04:51:11,209 INFO     29 [qwen-vl-text] page=1, rect=842x592, img=(2339x1644), dpi=200
2026-08-05 04:51:11,210 INFO     29 [qwen-vl-text] LLM extraction start, text_len=505
2026-08-05 04:51:11,210 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:51:11,210 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 24, \"bbox_end\": 54, \"encounter_dates\": [\"2025-11-26\"], \"department\": \"肾病糖尿病科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四平市中医医院\n门诊病历\n初诊\n2025年11月26日\n肾病糖尿病科\n姓名\n性别 女性\n年龄 55岁\n门诊号码 202511260272 (1)\n发病日期 2025-11-26\n类别 自费\n保险卡号\n就诊方式 便民门诊费\n医生 王亚新\n联系地址 四平铁西\n联系电话 13689710485\n身份证号\n职业\n体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分\n药物过敏史 无\n主诉: 自述糖尿病4年，支气管哮喘30余年\n病史: 糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/l.，糖化：\n10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。\n临床诊断：2型糖尿病 支气管哮喘急性发作\n治疗方案:\n建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，\n每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。\n结论:\n病程记录:\n医生（印章）：王亚新\n2025年11月27日 11:18",
    "role": "user"
  }
]
[92m04:51:11 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:11,211 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:14,991 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:51:14,991 INFO     29 [qwen-vl-text] LLM output (len=404):
{
  "encounter_date": "2025-11-26",
  "chief_complaint": "自述糖尿病4年，支气管哮喘30余年",
  "present_illness": "糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/l.，糖化：10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。",
  "past_history": "药物过敏史 无",
  "diagnosis": "2型糖尿病 支气管哮喘急性发作",
  "treatment_plan": "建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。"
}
2026-08-05 04:51:14,992 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-26]
2026-08-05 04:51:14,994 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1405624, prompt_len=1211
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["四平市中医医院", "门诊病历", "初诊", "2025年11月26日", "肾病糖尿病科", "姓名", "性别 女性", "年龄 55岁", "门诊号码 202511260272 (1)", "发病日期 2025-11-26", "类别 自费", "保险卡号", "就诊方式 便民门诊费", "医生 王亚新", "联系地址 四平铁西", "联系电话 13689710485", "身份证号", "职业", "体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分", "药物过敏史 无", "主诉: 自述糖尿病4年，支气管哮喘30余年", "病史: 糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/l.，糖化：", "10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。", "临床诊断：2型糖尿病 支气管哮喘急性发作", "治疗方案:", "建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，", "每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。", "结论:", "病程记录:", "医生（印章）：王亚新", "2025年11月27日 11:18"]

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
2026-08-05 04:51:27,707 INFO     29 [qwen-vl-text] coord API raw response (len=1860):
[
	{"text": "四平市中医医院", "bbox": [448, 123, 566, 150]},
	{"text": "门诊病历", "bbox": [458, 159, 555, 196]},
	{"text": "初诊", "bbox": [818, 118, 854, 143]},
	{"text": "2025年11月26日", "bbox": [774, 155, 895, 185]},
	{"text": "肾病糖尿病科", "bbox": [93, 178, 193, 204]},
	{"text": "姓名", "bbox": [86, 228, 115, 248]},
	{"text": "性别 女性", "bbox": [276, 224, 321, 245]},
	{"text": "年龄 55岁", "bbox": [385, 222, 416, 243]},
	{"text": "门诊号码 202511260272 (1)", "bbox": [502, 218, 686, 242]},
	{"text": "发病日期 2025-11-26", "bbox": [765, 207, 919, 233]},
	{"text": "类别 自费", "bbox": [87, 273, 115, 294]},
	{"text": "保险卡号", "bbox": [271, 270, 330, 290]},
	{"text": "就诊方式 便民门诊费", "bbox": [502, 265, 707, 287]},
	{"text": "医生 王亚新", "bbox": [792, 257, 902, 278]},
	{"text": "联系地址 四平铁西", "bbox": [97, 321, 236, 343]},
	{"text": "联系电话 13689710485", "bbox": [581, 312, 740, 335]},
	{"text": "身份证号", "bbox": [97, 366, 152, 387]},
	{"text": "职业", "bbox": [354, 363, 384, 384]},
	{"text": "体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分", "bbox": [578, 349, 918, 377]},
	{"text": "药物过敏史 无", "bbox": [90, 411, 194, 433]},
	{"text": "主诉: 自述糖尿病4年，支气管哮喘30余年", "bbox": [87, 452, 353, 473]},
	{"text": "病史: 糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/l.，糖化:", "bbox": [87, 477, 897, 500]},
	{"text": "10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。", "bbox": [146, 504, 780, 525]},
	{"text": "临床诊断：2型糖尿病 支气管哮喘急性发作", "bbox": [85, 634, 329, 654]},
	{"text": "治疗方案:", "bbox": [85, 669, 144, 689]},
	{"text": "建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，", "bbox": [112, 690, 852, 711]},
	{"text": "每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。", "bbox": [111, 711, 521, 733]},
	{"text": "结论:", "bbox": [86, 908, 118, 928]},
	{"text": "病程记录:", "bbox": [87, 950, 144, 970]},
	{"text": "医生（印章）：王亚新", "bbox": [519, 918, 712, 974]},
	{"text": "2025年11月27日 11:18", "bbox": [764, 956, 908, 979]}
]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=12.7s
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[0]: text=四平市中医医院, bbox=[448, 123, 566, 150]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[458, 159, 555, 196]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[2]: text=初诊, bbox=[818, 118, 854, 143]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[3]: text=2025年11月26日, bbox=[774, 155, 895, 185]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[4]: text=肾病糖尿病科, bbox=[93, 178, 193, 204]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[86, 228, 115, 248]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[6]: text=性别 女性, bbox=[276, 224, 321, 245]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[7]: text=年龄 55岁, bbox=[385, 222, 416, 243]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[8]: text=门诊号码 202511260272 (1), bbox=[502, 218, 686, 242]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[9]: text=发病日期 2025-11-26, bbox=[765, 207, 919, 233]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[10]: text=类别 自费, bbox=[87, 273, 115, 294]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[11]: text=保险卡号, bbox=[271, 270, 330, 290]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[12]: text=就诊方式 便民门诊费, bbox=[502, 265, 707, 287]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[13]: text=医生 王亚新, bbox=[792, 257, 902, 278]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[14]: text=联系地址 四平铁西, bbox=[97, 321, 236, 343]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[15]: text=联系电话 13689710485, bbox=[581, 312, 740, 335]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[16]: text=身份证号, bbox=[97, 366, 152, 387]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[17]: text=职业, bbox=[354, 363, 384, 384]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[18]: text=体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分, bbox=[578, 349, 918, 377]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[19]: text=药物过敏史 无, bbox=[90, 411, 194, 433]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[20]: text=主诉: 自述糖尿病4年，支气管哮喘30余年, bbox=[87, 452, 353, 473]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[21]: text=病史: 糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/l.，糖化:, bbox=[87, 477, 897, 500]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[22]: text=10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。, bbox=[146, 504, 780, 525]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[23]: text=临床诊断：2型糖尿病 支气管哮喘急性发作, bbox=[85, 634, 329, 654]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[24]: text=治疗方案:, bbox=[85, 669, 144, 689]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[25]: text=建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，, bbox=[112, 690, 852, 711]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[26]: text=每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。, bbox=[111, 711, 521, 733]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[27]: text=结论:, bbox=[86, 908, 118, 928]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[28]: text=病程记录:, bbox=[87, 950, 144, 970]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[29]: text=医生（印章）：王亚新, bbox=[519, 918, 712, 974]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] coord item[30]: text=2025年11月27日 11:18, bbox=[764, 956, 908, 979]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] page=1 — 31/31 coords, api_time=12.7s
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] new_positions (31):
[[1, 377.16661718750004, 476.5096101074219, 72.78809527587892, 88.76596984863282], [1, 385.58551489257815, 467.248822631836, 94.0919280395508, 115.98753393554688], [1, 688.6658322753907, 718.9738640136719, 69.82922961425781, 84.62355792236329], [1, 651.6226823730469, 753.4913446044923, 91.72483551025391, 109.47802947998048], [1, 78.29574865722657, 162.48472570800783, 105.33561755371095, 120.72171899414063], [1, 72.40252026367187, 96.81732360839844, 134.9242741699219, 146.75973681640627], [1, 232.36157666015626, 270.2466163330078, 132.557181640625, 144.9844174194336], [1, 324.12756164550785, 350.22614453125004, 131.37363537597656, 143.80087115478517], [1, 422.6286647949219, 577.5363825683594, 129.0065428466797, 143.20909802246095], [1, 644.0456744384766, 773.6966990966797, 122.49703839111329, 137.883139831543], [1, 73.2444100341797, 96.81732360839844, 161.55406512451174, 173.98130090332032], [1, 228.1521278076172, 277.82362426757817, 159.77874572753908, 171.61420837402346], [1, 422.6286647949219, 595.2160677490235, 156.81988006591797, 169.8388889770508], [1, 666.7766982421875, 759.3845729980469, 152.08569500732423, 164.5129307861328], [1, 81.66330773925782, 198.68598583984377, 189.95917547607422, 202.97818438720705], [1, 489.1379566650391, 622.9984301757813, 184.63321728515626, 198.24399932861328], [1, 81.66330773925782, 127.9672451171875, 216.58896643066407, 229.01620220947268], [1, 298.02897875976566, 323.28567187500005, 214.8136470336914, 227.24088281250002], [1, 486.6122873535157, 772.8548093261719, 206.52882318115235, 223.09847088623047], [1, 75.77007934570312, 163.32661547851563, 243.21875738525392, 256.2377662963867], [1, 73.2444100341797, 297.18708898925786, 267.4814558105469, 279.9086915893555], [1, 73.2444100341797, 755.1751241455079, 282.2757841186524, 295.8865661621094], [1, 122.91590649414063, 656.6740209960938, 298.25365869140626, 310.68089447021487], [1, 71.56063049316407, 276.9817344970703, 375.18416589355473, 387.0196285400391], [1, 71.56063049316407, 121.232126953125, 395.8962255249024, 407.73168817138674], [1, 94.29165429687501, 717.2900844726563, 408.323461303711, 420.7506970825196], [1, 93.44976452636719, 438.62457043457033, 420.7506970825196, 433.7697059936524], [1, 72.40252026367187, 99.34299291992188, 537.3300041503907, 549.1654667968751], [1, 73.2444100341797, 121.232126953125, 562.1844757080079, 574.0199383544922], [1, 436.9407908935547, 599.4255166015625, 543.2477354736328, 576.3870308837891], [1, 643.2037846679688, 764.4359116210939, 565.7351145019531, 579.3458965454103]]
2026-08-05 04:51:27,708 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=16.7s
2026-08-05 04:51:27,708 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:51:27,709 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:51:27,709 INFO     29 [qwen-vl-text] positions(29): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:51:27,709 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [29]
2026-08-05 04:51:27,967 INFO     29 [qwen-vl-text] page=2, rect=842x611, img=(2339x1697), dpi=200
2026-08-05 04:51:27,968 INFO     29 [qwen-vl-text] LLM extraction start, text_len=400
2026-08-05 04:51:27,968 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:51:27,968 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 55, \"bbox_end\": 83, \"encounter_dates\": [\"2025-12-31\"], \"department\": \"内二疗区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "四平市中医医院\n内二疗区\n门诊病历\n初诊\n2025年12月31日\n姓名\n性别：女性\n年龄：55岁\n门诊号码：202512310183\n（1）\n发病日期：2025-12-31\n类别：自费\n保险卡号\n就诊方式：服务号\n医生：张楷婷\n联系地址：吉林省四平市\n联系电话：13689710485\n身份证号：220303197009242283\n职业：\n体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分\n药物过敏史：否\n主诉：发现血糖升高4年\n病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。\n临床诊断：2型糖尿病\n治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊\n结论：\n病程记录：\n医生（印章）：\n2025年12月31日 15:12",
    "role": "user"
  }
]
[92m04:51:27 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:27,969 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:27,970 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:51:27.968+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 11, "failed": 0, "current": {"1f65e538908911f1a3da71efcdd7cc1f": {"id": "1f65e538908911f1a3da71efcdd7cc1f", "doc_id": "1f329962908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4590577, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905403691, "task_type": "dataflow", "root_trace_id": "171541281f15450ca1ea9d4184057967", "root_traceparent": "00-171541281f15450ca1ea9d4184057967-6239d56a1db4ab47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:51:30,691 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:51:30,691 INFO     29 [qwen-vl-text] LLM output (len=284):
{
  "encounter_date": "2025-12-31",
  "chief_complaint": "发现血糖升高4年",
  "present_illness": "发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。",
  "past_history": null,
  "diagnosis": "2型糖尿病",
  "treatment_plan": "建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊"
}
2026-08-05 04:51:30,692 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-31]
2026-08-05 04:51:30,695 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1984789, prompt_len=1100
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["四平市中医医院", "内二疗区", "门诊病历", "初诊", "2025年12月31日", "姓名", "性别：女性", "年龄：55岁", "门诊号码：202512310183", "（1）", "发病日期：2025-12-31", "类别：自费", "保险卡号", "就诊方式：服务号", "医生：张楷婷", "联系地址：吉林省四平市", "联系电话：13689710485", "身份证号：220303197009242283", "职业：", "体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分", "药物过敏史：否", "主诉：发现血糖升高4年", "病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。", "临床诊断：2型糖尿病", "治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊", "结论：", "病程记录：", "医生（印章）：", "2025年12月31日 15:12"]

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
2026-08-05 04:51:39,744 INFO     29 [qwen-vl-text] coord API raw response (len=1668):
[
	{"text": "四平市中医医院", "bbox": [453, 103, 575, 131]},
	{"text": "内二疗区", "bbox": [92, 143, 163, 168]},
	{"text": "门诊病历", "bbox": [463, 140, 563, 176]},
	{"text": "初诊", "bbox": [825, 122, 860, 145]},
	{"text": "2025年12月31日", "bbox": [782, 157, 903, 180]},
	{"text": "姓名", "bbox": [86, 187, 118, 208]},
	{"text": "性别：女性", "bbox": [281, 190, 366, 215]},
	{"text": "年龄：55岁", "bbox": [388, 193, 482, 218]},
	{"text": "门诊号码：202512310183", "bbox": [508, 197, 697, 222]},
	{"text": "（1）", "bbox": [714, 199, 759, 224]},
	{"text": "发病日期：2025-12-31", "bbox": [772, 199, 926, 225]},
	{"text": "类别：自费", "bbox": [85, 233, 214, 257]},
	{"text": "保险卡号", "bbox": [277, 237, 335, 260]},
	{"text": "就诊方式：服务号", "bbox": [508, 243, 702, 267]},
	{"text": "医生：张楷婷", "bbox": [800, 247, 910, 269]},
	{"text": "联系地址：吉林省四平市", "bbox": [95, 280, 272, 303]},
	{"text": "联系电话：13689710485", "bbox": [590, 290, 750, 312]},
	{"text": "身份证号：220303197009242283", "bbox": [95, 322, 317, 346]},
	{"text": "职业：", "bbox": [359, 328, 391, 349]},
	{"text": "体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分", "bbox": [585, 330, 928, 355]},
	{"text": "药物过敏史：否", "bbox": [87, 365, 197, 388]},
	{"text": "主诉：发现血糖升高4年", "bbox": [85, 405, 258, 428]},
	{"text": "病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。", "bbox": [84, 438, 794, 478]},
	{"text": "临床诊断：2型糖尿病", "bbox": [82, 577, 221, 599]},
	{"text": "治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊", "bbox": [111, 636, 874, 666]},
	{"text": "结论：", "bbox": [82, 846, 117, 867]},
	{"text": "病程记录：", "bbox": [82, 886, 145, 907]},
	{"text": "医生（印章）：", "bbox": [528, 888, 621, 914]},
	{"text": "2025年12月31日 15:12", "bbox": [780, 897, 923, 918]}
]
2026-08-05 04:51:39,744 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=9.0s
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[0]: text=四平市中医医院, bbox=[453, 103, 575, 131]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[1]: text=内二疗区, bbox=[92, 143, 163, 168]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[2]: text=门诊病历, bbox=[463, 140, 563, 176]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[3]: text=初诊, bbox=[825, 122, 860, 145]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[4]: text=2025年12月31日, bbox=[782, 157, 903, 180]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[86, 187, 118, 208]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女性, bbox=[281, 190, 366, 215]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：55岁, bbox=[388, 193, 482, 218]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[8]: text=门诊号码：202512310183, bbox=[508, 197, 697, 222]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[9]: text=（1）, bbox=[714, 199, 759, 224]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[10]: text=发病日期：2025-12-31, bbox=[772, 199, 926, 225]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[11]: text=类别：自费, bbox=[85, 233, 214, 257]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[12]: text=保险卡号, bbox=[277, 237, 335, 260]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[13]: text=就诊方式：服务号, bbox=[508, 243, 702, 267]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[14]: text=医生：张楷婷, bbox=[800, 247, 910, 269]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[15]: text=联系地址：吉林省四平市, bbox=[95, 280, 272, 303]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[16]: text=联系电话：13689710485, bbox=[590, 290, 750, 312]
2026-08-05 04:51:39,745 INFO     29 [qwen-vl-text] coord item[17]: text=身份证号：220303197009242283, bbox=[95, 322, 317, 346]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[18]: text=职业：, bbox=[359, 328, 391, 349]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[19]: text=体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分, bbox=[585, 330, 928, 355]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[20]: text=药物过敏史：否, bbox=[87, 365, 197, 388]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[21]: text=主诉：发现血糖升高4年, bbox=[85, 405, 258, 428]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[22]: text=病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。, bbox=[84, 438, 794, 478]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[23]: text=临床诊断：2型糖尿病, bbox=[82, 577, 221, 599]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[24]: text=治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊, bbox=[111, 636, 874, 666]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[25]: text=结论：, bbox=[82, 846, 117, 867]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[26]: text=病程记录：, bbox=[82, 886, 145, 907]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[27]: text=医生（印章）：, bbox=[528, 888, 621, 914]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] coord item[28]: text=2025年12月31日 15:12, bbox=[780, 897, 923, 918]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] page=2 — 29/29 coords, api_time=9.0s
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] new_positions (29):
[[2, 381.37606604003906, 484.0866180419922, 62.908695922851564, 80.01008898925781], [2, 77.45385888671875, 137.22803259277345, 87.33925744628907, 102.6083583984375], [2, 389.79496374511723, 473.9839407958985, 85.50696533203124, 107.494470703125], [2, 694.5590606689453, 724.0252026367187, 74.51321264648438, 88.56078552246093], [2, 658.3578005371094, 760.2264627685547, 95.88995397949219, 109.93752685546875], [2, 72.40252026367187, 99.34299291992188, 114.21287512207032, 127.03891992187499], [2, 236.57102551269531, 308.1316560058594, 116.04516723632813, 131.31426818847655], [2, 326.65323095703127, 405.79086938476564, 117.87745935058594, 133.14656030273437], [2, 427.68000341796875, 586.7971700439454, 120.32051550292968, 135.58961645507813], [2, 601.1092961425782, 638.9943358154297, 121.54204357910156, 136.81114453125], [2, 649.9389028320313, 779.5899274902345, 121.54204357910156, 137.42190856933593], [2, 71.56063049316407, 180.16441088867188, 142.30802087402344, 156.96635778808593], [2, 233.20346643066407, 282.0330731201172, 144.7510770263672, 158.79864990234375], [2, 427.68000341796875, 591.0066188964844, 148.41566125488282, 163.0739981689453], [2, 673.5118164062501, 766.1196911621095, 150.85871740722655, 164.29552624511717], [2, 79.97952819824219, 228.994017578125, 171.01393066406249, 185.06150354003907], [2, 496.7149645996094, 631.4173278808594, 177.12157104492186, 190.5583798828125], [2, 79.97952819824219, 266.8790572509766, 196.66602026367187, 211.32435717773438], [2, 302.2384276123047, 329.1789002685547, 200.3306044921875, 213.15664929199218], [2, 492.5055157470703, 781.2737070312501, 201.55213256835938, 216.8212335205078], [2, 73.2444100341797, 165.85228479003908, 222.92887390136718, 236.97644677734374], [2, 71.56063049316407, 217.20756079101565, 247.35943542480467, 261.40700830078123], [2, 70.71874072265625, 668.4604777832031, 267.5146486816406, 291.9452102050781], [2, 69.03496118164063, 186.05763928222657, 352.4108499755859, 365.8476588134765], [2, 93.44976452636719, 735.8116594238281, 388.4459282226562, 406.76884936523436], [2, 69.03496118164063, 98.50110314941406, 516.7063762207031, 529.5324210205079], [2, 69.03496118164063, 122.07401672363282, 541.1369377441406, 553.9629825439453], [2, 444.517798828125, 522.8135474853516, 542.3584658203125, 558.2383308105468], [2, 656.6740209960938, 777.0642581787109, 547.8553421630859, 560.6813869628907]]
2026-08-05 04:51:39,746 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=12.0s
2026-08-05 04:51:39,754 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 04:51:39,755 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Clinical | outputs={"chunks": "3 items, types={'OutpatientRecord': 3}", "html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:51:39,755 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 04:51:39,760 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:51:39,760 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 04:51:39,760 INFO     29 [qwen-vl-text] positions(37): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:51:39,760 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [37]
2026-08-05 04:51:40,237 INFO     29 [qwen-vl-text] page=5, rect=595x1492, img=(1654x4145), dpi=200
2026-08-05 04:51:40,237 INFO     29 [qwen-vl-text] LLM extraction start, text_len=323
2026-08-05 04:51:40,238 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:51:40,238 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 134, \"bbox_end\": 170, \"encounter_dates\": [\"2025-09-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "信康大药房--佳合分店\n单号：250927207100156\n日期：2025-09-27 17:52:20\n会员卡号：13689710485\n姓名：\n积分：37\n总积分：47\n药品名称\n规格\n生产企业/药品上市许可持有人\n产地\n剂型\n批号\n有效期\n数量\n单价\n金额\n12534\n185.00\n沙美特罗替卡松吸入粉雾剂\n50微克/250微克/60泡/盒\n葛兰素史克集团吸入粉雾剂\nJD6K\n2027-06-18\n2盒\n185.00\n370.00\n信康大药房温馨提示：您购买的\n药品需要常温储存(10℃-30℃)\n合计：\n370.00\n实收：\n370.00\n开票员：王影\n营业员：7139\n药品售出无质量问题不退不换！\n电话：0434-3333658",
    "role": "user"
  }
]
[92m04:51:40 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:40,239 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:42,788 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:51:42,788 INFO     29 [qwen-vl-text] LLM output (len=436):
{
  "encounter_date": "2025-09-27",
  "pharmacy": "信康大药房--佳合分店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": "50微克/250微克/60泡/盒",
      "dosage": null,
      "quantity": 2,
      "unit_price": 185.00,
      "total_price": 370.00,
      "frequency": null,
      "route": null,
      "manufacturer": "葛兰素史克集团",
      "approval_number": null
    }
  ],
  "payment_total": 370.00,
  "payment_method": null
}
2026-08-05 04:51:42,788 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-27]
2026-08-05 04:51:42,793 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3298411, prompt_len=1047
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["信康大药房--佳合分店", "单号：250927207100156", "日期：2025-09-27 17:52:20", "会员卡号：13689710485", "姓名：", "积分：37", "总积分：47", "药品名称", "规格", "生产企业/药品上市许可持有人", "产地", "剂型", "批号", "有效期", "数量", "单价", "金额", "12534", "185.00", "沙美特罗替卡松吸入粉雾剂", "50微克/250微克/60泡/盒", "葛兰素史克集团吸入粉雾剂", "JD6K", "2027-06-18", "2盒", "185.00", "370.00", "信康大药房温馨提示：您购买的", "药品需要常温储存(10℃-30℃)", "合计：", "370.00", "实收：", "370.00", "开票员：王影", "营业员：7139", "药品售出无质量问题不退不换！", "电话：0434-3333658"]

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
2026-08-05 04:51:54,244 INFO     29 [qwen-vl-text] coord API raw response (len=1954):
[
	{"text": "信康大药房--佳合分店", "bbox": [216, 191, 685, 219]},
	{"text": "单号：250927207100156", "bbox": [120, 220, 627, 245]},
	{"text": "日期：2025-09-27 17:52:20", "bbox": [122, 246, 728, 272]},
	{"text": "会员卡号：13689710485", "bbox": [122, 274, 598, 299]},
	{"text": "姓名：", "bbox": [122, 301, 222, 326]},
	{"text": "积分：37", "bbox": [122, 329, 291, 352]},
	{"text": "总积分：47", "bbox": [124, 355, 339, 378]},
	{"text": "药品名称", "bbox": [127, 400, 315, 422]},
	{"text": "规格", "bbox": [622, 397, 719, 420]},
	{"text": "生产企业/药品上市许可持有人", "bbox": [127, 428, 757, 453]},
	{"text": "产地", "bbox": [127, 460, 218, 481]},
	{"text": "剂型", "bbox": [267, 460, 359, 481]},
	{"text": "批号", "bbox": [408, 460, 496, 481]},
	{"text": "有效期", "bbox": [575, 460, 720, 481]},
	{"text": "数量", "bbox": [127, 489, 218, 511]},
	{"text": "单价", "bbox": [385, 489, 475, 510]},
	{"text": "金额", "bbox": [600, 489, 693, 510]},
	{"text": "12534", "bbox": [130, 533, 258, 553]},
	{"text": "185.00", "bbox": [313, 533, 468, 553]},
	{"text": "沙美特罗替卡松吸入粉雾剂", "bbox": [127, 559, 764, 584]},
	{"text": "50微克/250微克/60泡/盒", "bbox": [127, 590, 719, 614]},
	{"text": "葛兰素史克集团吸入粉雾剂", "bbox": [130, 620, 802, 645]},
	{"text": "JD6K", "bbox": [127, 656, 225, 674]},
	{"text": "2027-06-18", "bbox": [270, 655, 518, 674]},
	{"text": "2盒", "bbox": [127, 684, 212, 705]},
	{"text": "185.00", "bbox": [288, 684, 432, 703]},
	{"text": "370.00", "bbox": [525, 684, 675, 702]},
	{"text": "信康大药房温馨提示：您购买的", "bbox": [132, 710, 864, 734]},
	{"text": "药品需要常温储存(10℃-30℃)", "bbox": [132, 736, 861, 760]},
	{"text": "合计：", "bbox": [135, 781, 252, 807]},
	{"text": "370.00", "bbox": [568, 781, 722, 803]},
	{"text": "实收：", "bbox": [135, 808, 247, 834]},
	{"text": "370.00", "bbox": [568, 807, 724, 829]},
	{"text": "开票员：王影", "bbox": [135, 832, 447, 859]},
	{"text": "营业员：7139", "bbox": [496, 830, 796, 855]},
	{"text": "药品售出无质量问题不退不换！", "bbox": [135, 853, 810, 882]},
	{"text": "电话：0434-3333658", "bbox": [137, 876, 545, 907]}
]
2026-08-05 04:51:54,244 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=11.5s
2026-08-05 04:51:54,244 INFO     29 [qwen-vl-text] coord item[0]: text=信康大药房--佳合分店, bbox=[216, 191, 685, 219]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[1]: text=单号：250927207100156, bbox=[120, 220, 627, 245]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[2]: text=日期：2025-09-27 17:52:20, bbox=[122, 246, 728, 272]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[3]: text=会员卡号：13689710485, bbox=[122, 274, 598, 299]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[122, 301, 222, 326]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[5]: text=积分：37, bbox=[122, 329, 291, 352]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[6]: text=总积分：47, bbox=[124, 355, 339, 378]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[7]: text=药品名称, bbox=[127, 400, 315, 422]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[8]: text=规格, bbox=[622, 397, 719, 420]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[9]: text=生产企业/药品上市许可持有人, bbox=[127, 428, 757, 453]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[10]: text=产地, bbox=[127, 460, 218, 481]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[11]: text=剂型, bbox=[267, 460, 359, 481]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[12]: text=批号, bbox=[408, 460, 496, 481]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[13]: text=有效期, bbox=[575, 460, 720, 481]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[127, 489, 218, 511]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[385, 489, 475, 510]
2026-08-05 04:51:54,245 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[600, 489, 693, 510]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[17]: text=12534, bbox=[130, 533, 258, 553]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[18]: text=185.00, bbox=[313, 533, 468, 553]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[19]: text=沙美特罗替卡松吸入粉雾剂, bbox=[127, 559, 764, 584]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[20]: text=50微克/250微克/60泡/盒, bbox=[127, 590, 719, 614]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[21]: text=葛兰素史克集团吸入粉雾剂, bbox=[130, 620, 802, 645]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[22]: text=JD6K, bbox=[127, 656, 225, 674]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[23]: text=2027-06-18, bbox=[270, 655, 518, 674]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[24]: text=2盒, bbox=[127, 684, 212, 705]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[25]: text=185.00, bbox=[288, 684, 432, 703]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[26]: text=370.00, bbox=[525, 684, 675, 702]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[27]: text=信康大药房温馨提示：您购买的, bbox=[132, 710, 864, 734]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[28]: text=药品需要常温储存(10℃-30℃), bbox=[132, 736, 861, 760]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[29]: text=合计：, bbox=[135, 781, 252, 807]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[30]: text=370.00, bbox=[568, 781, 722, 803]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[31]: text=实收：, bbox=[135, 808, 247, 834]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[32]: text=370.00, bbox=[568, 807, 724, 829]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[33]: text=开票员：王影, bbox=[135, 832, 447, 859]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[34]: text=营业员：7139, bbox=[496, 830, 796, 855]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[35]: text=药品售出无质量问题不退不换！, bbox=[135, 853, 810, 882]
2026-08-05 04:51:54,246 INFO     29 [qwen-vl-text] coord item[36]: text=电话：0434-3333658, bbox=[137, 876, 545, 907]
2026-08-05 04:51:54,247 INFO     29 [qwen-vl-text] page=5 — 37/37 coords, api_time=11.5s
2026-08-05 04:51:54,247 INFO     29 [qwen-vl-text] new_positions (37):
[[5, 128.579537109375, 407.7638098144531, 284.95472326660155, 326.7281905517578], [5, 71.433076171875, 373.23782299804685, 328.22010009765626, 365.51783874511716], [5, 72.62362744140624, 433.36066210937497, 367.0097482910156, 405.799396484375], [5, 72.62362744140624, 355.9748295898437, 408.78321557617187, 446.08095422363283], [5, 72.62362744140624, 132.15119091796873, 449.0647733154297, 486.3625119628906], [5, 72.62362744140624, 173.22520971679685, 490.83824060058595, 525.15216015625], [5, 73.8141787109375, 201.79844018554687, 529.6278887939453, 563.9418083496093], [5, 75.60000561523437, 187.51182495117186, 596.763818359375, 629.5858283691406], [5, 370.2614448242187, 428.00318139648436, 592.2880897216797, 626.6020092773438], [5, 75.60000561523437, 450.6236555175781, 638.5372856445313, 675.8350242919922], [5, 75.60000561523437, 129.77008837890625, 686.2783911132813, 717.6084915771485], [5, 158.93859448242185, 213.70395288085936, 686.2783911132813, 717.6084915771485], [5, 242.872458984375, 295.25671484375, 686.2783911132813, 717.6084915771485], [5, 342.28348999023433, 428.59845703124995, 686.2783911132813, 717.6084915771485], [5, 75.60000561523437, 129.77008837890625, 729.543767944336, 762.3657779541015], [5, 229.1811193847656, 282.75592651367185, 729.543767944336, 760.8738684082031], [5, 357.165380859375, 412.5260148925781, 729.543767944336, 760.8738684082031], [5, 77.38583251953125, 153.58111376953124, 795.1877879638672, 825.025978881836], [5, 186.3212736816406, 278.5889970703125, 795.1877879638672, 825.025978881836], [5, 75.60000561523437, 454.79058496093745, 833.9774361572265, 871.2751748046875], [5, 75.60000561523437, 428.00318139648436, 880.2266320800782, 916.0324611816407], [5, 77.38583251953125, 477.4110590820312, 924.9839184570312, 962.2816571044922], [5, 75.60000561523437, 133.9370178222656, 978.692662109375, 1005.5470339355469], [5, 160.72442138671875, 308.3527788085937, 977.2007525634766, 1005.5470339355469], [5, 75.60000561523437, 126.19843457031249, 1020.4661293945312, 1051.7962298583984], [5, 171.43938281249999, 257.15907421875, 1020.4661293945312, 1048.8124107666015], [5, 312.5197082519531, 401.81105346679686, 1020.4661293945312, 1047.3205012207031], [5, 78.57638378906249, 514.3181484375, 1059.2557775878906, 1095.0616066894531], [5, 78.57638378906249, 512.5323215332031, 1098.04542578125, 1133.8512548828126], [5, 80.36221069335937, 150.00945996093748, 1165.1813553466798, 1203.971003540039], [5, 338.11656054687495, 429.78900830078123, 1165.1813553466798, 1198.0033653564453], [5, 80.36221069335937, 147.03308178710935, 1205.4629130859375, 1244.252561279297], [5, 338.11656054687495, 430.97955957031246, 1203.971003540039, 1236.7930135498048], [5, 80.36221069335937, 266.08820874023434, 1241.2687421875, 1281.5502999267578], [5, 295.25671484375, 473.8394052734375, 1238.284923095703, 1275.582661743164], [5, 80.36221069335937, 482.17326416015624, 1272.5988426513672, 1315.864219482422], [5, 81.55276196289061, 324.4252209472656, 1306.9127622070312, 1353.1619581298828]]
2026-08-05 04:51:54,247 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=14.5s
2026-08-05 04:51:54,247 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:51:54,247 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 04:51:54,247 INFO     29 [qwen-vl-text] positions(37): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:51:54,247 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [37]
2026-08-05 04:51:54,703 INFO     29 [qwen-vl-text] page=6, rect=595x1387, img=(1654x3853), dpi=200
2026-08-05 04:51:54,704 INFO     29 [qwen-vl-text] LLM extraction start, text_len=323
2026-08-05 04:51:54,704 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:51:54,704 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 171, \"bbox_end\": 207, \"encounter_dates\": [\"2025-11-28\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "信康大药房--佳合分店\n单号：251128207100163\n日期：2025-11-28 16:38:41\n会员卡号：13689710485\n姓名：\n积分：37\n总积分：84\n药品名称\n规格\n生产企业/药品上市许可持有人\n产地\n剂型\n批号\n有效期\n数量\n单价\n金额\n12534\n185.00\n沙美特罗替卡松吸入粉雾剂\n50微克/250微克/60泡/盒\n葛兰素史克集团吸入粉雾剂\nJD6K\n2027-06-18\n2盒\n185.00\n370.00\n信康大药房温馨提示：您购买的\n药品需要常温储存（10℃-30℃）\n合计：\n370.00\n实收：\n370.00\n开票员：张欣\n营业员：7140\n药品售出无质量问题不退不换！\n电话：0434-3333658",
    "role": "user"
  }
]
[92m04:51:54 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:51:54,706 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:52:00,003 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:52:00,003 INFO     29 [qwen-vl-text] LLM output (len=436):
{
  "encounter_date": "2025-11-28",
  "pharmacy": "信康大药房--佳合分店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂",
      "specification": "50微克/250微克/60泡/盒",
      "dosage": null,
      "quantity": 2,
      "unit_price": 185.00,
      "total_price": 370.00,
      "frequency": null,
      "route": null,
      "manufacturer": "葛兰素史克集团",
      "approval_number": null
    }
  ],
  "payment_total": 370.00,
  "payment_method": null
}
2026-08-05 04:52:00,004 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-28]
2026-08-05 04:52:00,014 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3086331, prompt_len=1047
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["信康大药房--佳合分店", "单号：251128207100163", "日期：2025-11-28 16:38:41", "会员卡号：13689710485", "姓名：", "积分：37", "总积分：84", "药品名称", "规格", "生产企业/药品上市许可持有人", "产地", "剂型", "批号", "有效期", "数量", "单价", "金额", "12534", "185.00", "沙美特罗替卡松吸入粉雾剂", "50微克/250微克/60泡/盒", "葛兰素史克集团吸入粉雾剂", "JD6K", "2027-06-18", "2盒", "185.00", "370.00", "信康大药房温馨提示：您购买的", "药品需要常温储存（10℃-30℃）", "合计：", "370.00", "实收：", "370.00", "开票员：张欣", "营业员：7140", "药品售出无质量问题不退不换！", "电话：0434-3333658"]

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
2026-08-05 04:52:11,298 INFO     29 [qwen-vl-text] coord API raw response (len=1953):
[
	{"text": "信康大药房--佳合分店", "bbox": [252, 174, 692, 201]},
	{"text": "单号：251128207100163", "bbox": [159, 203, 638, 227]},
	{"text": "日期：2025-11-28 16:38:41", "bbox": [161, 230, 725, 254]},
	{"text": "会员卡号：13689710485", "bbox": [161, 257, 612, 279],
	{"text": "姓名：", "bbox": [161, 283, 252, 307]},
	{"text": "积分：37", "bbox": [161, 311, 320, 334]},
	{"text": "总积分：84", "bbox": [161, 338, 364, 360]},
	{"text": "药品名称", "bbox": [161, 382, 340, 405]},
	{"text": "规格", "bbox": [638, 380, 725, 403]},
	{"text": "生产企业/药品上市许可持有人", "bbox": [161, 411, 764, 435]},
	{"text": "产地", "bbox": [161, 444, 250, 466]},
	{"text": "剂型", "bbox": [296, 444, 385, 466]},
	{"text": "批号", "bbox": [431, 444, 519, 466]},
	{"text": "有效期", "bbox": [594, 443, 729, 465]},
	{"text": "数量", "bbox": [161, 474, 250, 496]},
	{"text": "单价", "bbox": [409, 473, 496, 495]},
	{"text": "金额", "bbox": [614, 473, 701, 494]},
	{"text": "12534", "bbox": [165, 518, 288, 537]},
	{"text": "185.00", "bbox": [340, 517, 486, 536]},
	{"text": "沙美特罗替卡松吸入粉雾剂", "bbox": [161, 545, 762, 568]},
	{"text": "50微克/250微克/60泡/盒", "bbox": [161, 575, 714, 598]},
	{"text": "葛兰素史克集团吸入粉雾剂", "bbox": [167, 606, 786, 629]},
	{"text": "JD6K", "bbox": [165, 641, 258, 659]},
	{"text": "2027-06-18", "bbox": [298, 640, 524, 658]},
	{"text": "2盒", "bbox": [165, 670, 244, 690]},
	{"text": "185.00", "bbox": [314, 670, 448, 688]},
	{"text": "370.00", "bbox": [535, 669, 673, 687]},
	{"text": "信康大药房温馨提示：您购买的", "bbox": [167, 696, 845, 718]},
	{"text": "药品需要常温储存（10℃-30℃）", "bbox": [167, 723, 845, 745]},
	{"text": "合计：", "bbox": [171, 770, 280, 793]},
	{"text": "370.00", "bbox": [573, 767, 714, 787]},
	{"text": "实收：", "bbox": [171, 795, 275, 820]},
	{"text": "370.00", "bbox": [573, 791, 714, 811]},
	{"text": "开票员：张欣", "bbox": [171, 817, 458, 845]},
	{"text": "营业员：7140", "bbox": [505, 815, 788, 840]},
	{"text": "药品售出无质量问题不退不换！", "bbox": [171, 840, 800, 867]},
	{"text": "电话：0434-3333658", "bbox": [171, 863, 550, 888]}
]
2026-08-05 04:52:11,298 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-05 04:52:11,299 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=11.3s
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[0]: text=信康大药房--佳合分店, bbox=[252, 174, 692, 201]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[1]: text=单号：251128207100163, bbox=[159, 203, 638, 227]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[2]: text=日期：2025-11-28 16:38:41, bbox=[161, 230, 725, 254]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[3]: text=会员卡号：13689710485, bbox=[161, 257, 612, 279]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[161, 283, 252, 307]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[5]: text=积分：37, bbox=[161, 311, 320, 334]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[6]: text=总积分：84, bbox=[161, 338, 364, 360]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[7]: text=药品名称, bbox=[161, 382, 340, 405]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[8]: text=规格, bbox=[638, 380, 725, 403]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[9]: text=生产企业/药品上市许可持有人, bbox=[161, 411, 764, 435]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[10]: text=产地, bbox=[161, 444, 250, 466]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[11]: text=剂型, bbox=[296, 444, 385, 466]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[12]: text=批号, bbox=[431, 444, 519, 466]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[13]: text=有效期, bbox=[594, 443, 729, 465]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[161, 474, 250, 496]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[409, 473, 496, 495]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[614, 473, 701, 494]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[17]: text=12534, bbox=[165, 518, 288, 537]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[18]: text=185.00, bbox=[340, 517, 486, 536]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[19]: text=沙美特罗替卡松吸入粉雾剂, bbox=[161, 545, 762, 568]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[20]: text=50微克/250微克/60泡/盒, bbox=[161, 575, 714, 598]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[21]: text=葛兰素史克集团吸入粉雾剂, bbox=[167, 606, 786, 629]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[22]: text=JD6K, bbox=[165, 641, 258, 659]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[23]: text=2027-06-18, bbox=[298, 640, 524, 658]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[24]: text=2盒, bbox=[165, 670, 244, 690]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[25]: text=185.00, bbox=[314, 670, 448, 688]
2026-08-05 04:52:11,300 INFO     29 [qwen-vl-text] coord item[26]: text=370.00, bbox=[535, 669, 673, 687]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[27]: text=信康大药房温馨提示：您购买的, bbox=[167, 696, 845, 718]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[28]: text=药品需要常温储存（10℃-30℃）, bbox=[167, 723, 845, 745]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[29]: text=合计：, bbox=[171, 770, 280, 793]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[30]: text=370.00, bbox=[573, 767, 714, 787]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[31]: text=实收：, bbox=[171, 795, 275, 820]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[32]: text=370.00, bbox=[573, 791, 714, 811]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[33]: text=开票员：张欣, bbox=[171, 817, 458, 845]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[34]: text=营业员：7140, bbox=[505, 815, 788, 840]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[35]: text=药品售出无质量问题不退不换！, bbox=[171, 840, 800, 867]
2026-08-05 04:52:11,301 INFO     29 [qwen-vl-text] coord item[36]: text=电话：0434-3333658, bbox=[171, 863, 550, 888]
2026-08-05 04:52:11,302 INFO     29 [qwen-vl-text] page=6 — 37/37 coords, api_time=11.3s
2026-08-05 04:52:11,302 INFO     29 [qwen-vl-text] new_positions (37):
[[6, 150.00945996093748, 411.9307392578125, 241.3042917480469, 278.7480611572266], [6, 94.64882592773436, 379.78585498046874, 281.5216737060547, 314.8050242919922], [6, 95.83937719726562, 431.5748352050781, 318.9654431152344, 352.2487937011719], [6, 95.83937719726562, 364.30868847656245, 356.4092125244141, 386.91895056152345], [6, 95.83937719726562, 150.00945996093748, 392.4661756591797, 425.7495262451172], [6, 95.83937719726562, 190.48820312499998, 431.29675134277346, 463.1932956542969], [6, 95.83937719726562, 216.68033105468749, 468.74052075195317, 499.2502587890625], [6, 95.83937719726562, 202.39371582031248, 529.7599968261719, 561.6565411376953], [6, 379.78585498046874, 431.5748352050781, 526.9863842773437, 558.8829285888672], [6, 95.83937719726562, 454.79058496093745, 569.9773787841797, 603.2607293701172], [6, 95.83937719726562, 148.81890869140625, 615.7419858398438, 646.2517238769532], [6, 176.20158789062498, 229.1811193847656, 615.7419858398438, 646.2517238769532], [6, 256.56379858398435, 308.94805444335935, 615.7419858398438, 646.2517238769532], [6, 353.59372705078124, 433.9559377441406, 614.3551795654297, 644.8649176025391], [6, 95.83937719726562, 148.81890869140625, 657.3461740722656, 687.855912109375], [6, 243.4677346191406, 295.25671484375, 655.9593677978515, 686.4691058349609], [6, 365.49923974609374, 417.2882199707031, 655.9593677978515, 685.0822995605469], [6, 98.22047973632812, 171.43938281249999, 718.3656501464844, 744.7149693603516], [6, 202.39371582031248, 289.30395849609374, 716.9788438720703, 743.3281630859375], [6, 95.83937719726562, 453.6000336914062, 755.8094195556641, 787.7059638671875], [6, 95.83937719726562, 425.0268032226562, 797.413607788086, 829.3101520996095], [6, 99.41103100585937, 467.88664892578123, 840.4046022949219, 872.3011466064454], [6, 98.22047973632812, 153.58111376953124, 888.9428218994141, 913.9053348388672], [6, 177.39213916015623, 311.92443261718745, 887.5560156250001, 912.5185285644532], [6, 98.22047973632812, 145.24725488281248, 929.160203857422, 956.8963293457032], [6, 186.91654931640625, 266.683484375, 929.160203857422, 954.122716796875], [6, 318.47246459960934, 400.6205021972656, 927.7733975830079, 952.735910522461], [6, 99.41103100585937, 503.0079113769531, 965.2171669921876, 995.726905029297], [6, 99.41103100585937, 503.0079113769531, 1002.6609364013673, 1033.1706744384767], [6, 101.79213354492187, 166.677177734375, 1067.840831298828, 1099.7373756103516], [6, 341.0929387207031, 425.0268032226562, 1063.680412475586, 1091.4165379638673], [6, 101.79213354492187, 163.70079956054687, 1102.5109881591798, 1137.1811450195314], [6, 341.0929387207031, 425.0268032226562, 1096.9637630615234, 1124.6998885498047], [6, 101.79213354492187, 272.6362407226562, 1133.0207261962892, 1171.8513018798828], [6, 300.6141955566406, 469.07720019531246, 1130.247113647461, 1164.9172705078126], [6, 101.79213354492187, 476.22050781249993, 1164.9172705078126, 1202.3610399169922], [6, 101.79213354492187, 327.40159912109374, 1196.813814819336, 1231.4839716796876]]
2026-08-05 04:52:11,302 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=17.1s
2026-08-05 04:52:11,321 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 04:52:11,321 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:52:11,321 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 04:52:11,322 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:52:11.321+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 11, "failed": 0, "current": {"1f65e538908911f1a3da71efcdd7cc1f": {"id": "1f65e538908911f1a3da71efcdd7cc1f", "doc_id": "1f329962908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4590577, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905403691, "task_type": "dataflow", "root_trace_id": "171541281f15450ca1ea9d4184057967", "root_traceparent": "00-171541281f15450ca1ea9d4184057967-6239d56a1db4ab47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:52:11,328 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:52:11,328 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:52:11 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:52:11,329 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:52:12,456 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:52:12,463 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 04:52:12,464 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:52:12,464 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 04:52:12,468 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:52:12,469 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:52:12 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:52:12,470 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:52:15,575 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:52:15,579 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 04:52:15,579 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:52:15,579 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 04:52:15,583 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:52:15,584 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 04:52:16,091 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:52:16,096 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 04:52:16,096 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:52:16,096 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 04:52:16,101 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:52:16,101 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 04:52:16,101 INFO     29 [qwen-vl-text] positions(50): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:52:16,101 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [16, 22]
2026-08-05 04:52:16,329 INFO     29 [qwen-vl-text] page=3, rect=595x1058, img=(1654x2940), dpi=200
2026-08-05 04:52:16,530 INFO     29 [qwen-vl-text] page=4, rect=595x1058, img=(1654x2940), dpi=200
2026-08-05 04:52:16,531 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1104
2026-08-05 04:52:16,531 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:52:16,531 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 84, \"bbox_end\": 133, \"encounter_dates\": [\"2023-12-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告时间: 2023-12-27\n\\multicolumn{2}{c}{预计值} 药前 前/预% 药后 \\multicolumn{2}{c}{后/预% 改善率 (%)}\n测试日期 23/12/27 23/12/27\n测试时间 15:36:14 15:51:45\nMV [L/min] 11.71 27.39 233.8 7.6\nVC MAX [L] 3.28 3.52 107.3 3.78 115.4\nFVC [L] 3.17 3.52 110.8 3.78 119.2\nFEV 1 [L] 2.71 2.11 77.7 2.39 88.3\nFEV 1 % FVC [%] 63.29\nFEV 1 % VC MAX [%] 79.03 59.91 75.8 63.29 80.1\nPEF [L/s] 6.54 4.76 72.7 4.54 69.4\nMEF 75 [L/s] 5.68 2.64 46.4 3.29 58.0\nMEF 50 [L/s] 3.95 1.40 35.4 1.80 45.5\nMEF 25 [L/s] 1.55 0.53 34.2 0.65 42.1\nMMEF 75/25 [L/s] 3.22 1.15 35.8 1.44 44.6\nMVV [L/min] 100.45\n报告时间: 2023-12-27\n预计值 实测值 实/预\nVT [L] 0.59 1.51 258.6\nBF [1/min] 20.00 18.08 90.4\nMV [L/min] 11.71 27.39 233.8\nVC MAX [L] 3.28 3.52 107.3\nERV [L] 0.93 1.39 149.9\nIC [L] 2.35 2.13 90.5\nFVC [L] 3.17 3.52 110.8\nFEV 1 [L] 2.71 2.11 77.7\nFEV 1 % FVC [%] 59.91\nFEV 1 % VC MAX [%] 79.03 59.91 75.8\nPEF [L/s] 6.54 4.76 72.7\nMEF 75 [L/s] 5.68 2.64 46.4\nMEF 50 [L/s] 3.95 1.40 35.4\nMEF 25 [L/s] 1.55 0.53 34.2\nMMEF 75/25 [L/s] 3.22 1.15 35.8\nFEF 75/85 [L/s] 0.85 0.35 41.0\nPIF [L/s] 2.16\nFEF50 % FIF50 [%] 78.19\nMVV [L/min] 100.45\nFEV 1*30 [L/min] 100.45 63.19 62.9",
    "role": "user"
  }
]
[92m04:52:16 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:52:16,532 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:52:29,390 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:52:29,390 INFO     29 [qwen-vl-text] LLM output (len=1883):
{
  "exam_date": "2023-12-27",
  "report_date": "2023-12-27",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "| 指标 | 预计值 | 药前 | 前/预% | 药后 | 后/预% | 改善率(%) |\n|---|---|---|---|---|---|---|\n| 测试日期 | | 23/12/27 | | 23/12/27 | | |\n| 测试时间 | | 15:36:14 | | 15:51:45 | | |\n| MV [L/min] | 11.71 | 27.39 | 233.8 | 7.6 | | |\n| VC MAX [L] | 3.28 | 3.52 | 107.3 | 3.78 | 115.4 | |\n| FVC [L] | 3.17 | 3.52 | 110.8 | 3.78 | 119.2 | |\n| FEV 1 [L] | 2.71 | 2.11 | 77.7 | 2.39 | 88.3 | |\n| FEV 1 % FVC [%] | | 63.29 | | | | |\n| FEV 1 % VC MAX [%] | 79.03 | 59.91 | 75.8 | 63.29 | 80.1 | |\n| PEF [L/s] | 6.54 | 4.76 | 72.7 | 4.54 | 69.4 | |\n| MEF 75 [L/s] | 5.68 | 2.64 | 46.4 | 3.29 | 58.0 | |\n| MEF 50 [L/s] | 3.95 | 1.40 | 35.4 | 1.80 | 45.5 | |\n| MEF 25 [L/s] | 1.55 | 0.53 | 34.2 | 0.65 | 42.1 | |\n| MMEF 75/25 [L/s] | 3.22 | 1.15 | 35.8 | 1.44 | 44.6 | |\n| MVV [L/min] | 100.45 | | | | | |\n\n| 指标 | 预计值 | 实测值 | 实/预% |\n|---|---|---|---|\n| VT [L] | 0.59 | 1.51 | 258.6 |\n| BF [1/min] | 20.00 | 18.08 | 90.4 |\n| MV [L/min] | 11.71 | 27.39 | 233.8 |\n| VC MAX [L] | 3.28 | 3.52 | 107.3 |\n| ERV [L] | 0.93 | 1.39 | 149.9 |\n| IC [L] | 2.35 | 2.13 | 90.5 |\n| FVC [L] | 3.17 | 3.52 | 110.8 |\n| FEV 1 [L] | 2.71 | 2.11 | 77.7 |\n| FEV 1 % FVC [%] | | 59.91 | |\n| FEV 1 % VC MAX [%] | 79.03 | 59.91 | 75.8 |\n| PEF [L/s] | 6.54 | 4.76 | 72.7 |\n| MEF 75 [L/s] | 5.68 | 2.64 | 46.4 |\n| MEF 50 [L/s] | 3.95 | 1.40 | 35.4 |\n| MEF 25 [L/s] | 1.55 | 0.53 | 34.2 |\n| MMEF 75/25 [L/s] | 3.22 | 1.15 | 35.8 |\n| FEF 75/85 [L/s] | 0.85 | 0.35 | 41.0 |\n| PIF [L/s] | | 2.16 | |\n| FEF50 % FIF50 [%] | | 78.19 | |\n| MVV [L/min] | 100.45 | | |\n| FEV 1*30 [L/min] | 100.45 | 63.19 | 62.9 |",
  "conclusion": null,
  "physician": null,
  "reviewer": null
}
2026-08-05 04:52:29,394 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1505638, prompt_len=1213
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["报告时间: 2023-12-27", "\\multicolumn{2}{c}{预计值} 药前 前/预% 药后 \\multicolumn{2}{c}{后/预% 改善率 (%)}", "测试日期 23/12/27 23/12/27", "测试时间 15:36:14 15:51:45", "MV [L/min] 11.71 27.39 233.8 7.6", "VC MAX [L] 3.28 3.52 107.3 3.78 115.4", "FVC [L] 3.17 3.52 110.8 3.78 119.2", "FEV 1 [L] 2.71 2.11 77.7 2.39 88.3", "FEV 1 % FVC [%] 63.29", "FEV 1 % VC MAX [%] 79.03 59.91 75.8 63.29 80.1", "PEF [L/s] 6.54 4.76 72.7 4.54 69.4", "MEF 75 [L/s] 5.68 2.64 46.4 3.29 58.0", "MEF 50 [L/s] 3.95 1.40 35.4 1.80 45.5", "MEF 25 [L/s] 1.55 0.53 34.2 0.65 42.1", "MMEF 75/25 [L/s] 3.22 1.15 35.8 1.44 44.6", "MVV [L/min] 100.45"]

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
2026-08-05 04:52:39,278 INFO     29 [qwen-vl-text] coord API raw response (len=1536):
```json
[
	{"text": "报告时间: 2023-12-27", "bbox": [450, 357, 522, 366]},
	{"text": "\\multicolumn{2}{c}{预计值} 药前 前/预% 药后 \\multicolumn{2}{c}{后/预% 改善率 (%)}", "bbox": [384, 345, 868, 360]},
	{"text": "测试日期 23/12/27 23/12/27", "bbox": [133, 363, 522, 375], "label": "测试日期"},
	{"text": "测试时间 15:36:14 15:51:45", "bbox": [133, 373, 522, 384], "label": "测试时间"},
	{"text": "MV [L/min] 11.71 27.39 233.8 7.6", "bbox": [133, 387, 881, 400], "label": "MV"},
	{"text": "VC MAX [L] 3.28 3.52 107.3 3.78 115.4", "bbox": [133, 398, 881, 410], "label": "VC MAX"},
	{"text": "FVC [L] 3.17 3.52 110.8 3.78 119.2", "bbox": [133, 410, 881, 423], "label": "FVC"},
	{"text": "FEV 1 [L] 2.71 2.11 77.7 2.39 88.3", "bbox": [133, 422, 881, 434], "label": "FEV 1"},
	{"text": "FEV 1 % FVC [%] 63.29", "bbox": [133, 434, 881, 446], "label": "FEV 1 % FVC"},
	{"text": "FEV 1 % VC MAX [%] 79.03 59.91 75.8 63.29 80.1", "bbox": [133, 445, 881, 457], "label": "FEV 1 % VC MAX"},
	{"text": "PEF [L/s] 6.54 4.76 72.7 4.54 69.4", "bbox": [133, 457, 881, 469], "label": "PEF"},
	{"text": "MEF 75 [L/s] 5.68 2.64 46.4 3.29 58.0", "bbox": [133, 468, 881, 480], "label": "MEF 75"},
	{"text": "MEF 50 [L/s] 3.95 1.40 35.4 1.80 45.5", "bbox": [133, 480, 881, 492], "label": "MEF 50"},
	{"text": "MEF 25 [L/s] 1.55 0.53 34.2 0.65 42.1", "bbox": [133, 491, 881, 503], "label": "MEF 25"},
	{"text": "MMEF 75/25 [L/s] 3.22 1.15 35.8 1.44 44.6", "bbox": [133, 502, 881, 514], "label": "MMEF 75/25"},
	{"text": "MVV [L/min] 100.45", "bbox": [133, 514, 454, 525], "label": "MVV"}
]
```
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=9.9s
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间: 2023-12-27, bbox=[450, 357, 522, 366]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[1]: text=\multicolumn{2}{c}{预计值} 药前 前/预% 药后 \multicolumn{2}{c}{后/预% 改善率 (%)}, bbox=[384, 345, 868, 360]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[2]: text=测试日期 23/12/27 23/12/27, bbox=[133, 363, 522, 375]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[3]: text=测试时间 15:36:14 15:51:45, bbox=[133, 373, 522, 384]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[4]: text=MV [L/min] 11.71 27.39 233.8 7.6, bbox=[133, 387, 881, 400]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[5]: text=VC MAX [L] 3.28 3.52 107.3 3.78 115.4, bbox=[133, 398, 881, 410]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[6]: text=FVC [L] 3.17 3.52 110.8 3.78 119.2, bbox=[133, 410, 881, 423]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[7]: text=FEV 1 [L] 2.71 2.11 77.7 2.39 88.3, bbox=[133, 422, 881, 434]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[8]: text=FEV 1 % FVC [%] 63.29, bbox=[133, 434, 881, 446]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[9]: text=FEV 1 % VC MAX [%] 79.03 59.91 75.8 63.29 80.1, bbox=[133, 445, 881, 457]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[10]: text=PEF [L/s] 6.54 4.76 72.7 4.54 69.4, bbox=[133, 457, 881, 469]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[11]: text=MEF 75 [L/s] 5.68 2.64 46.4 3.29 58.0, bbox=[133, 468, 881, 480]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[12]: text=MEF 50 [L/s] 3.95 1.40 35.4 1.80 45.5, bbox=[133, 480, 881, 492]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[13]: text=MEF 25 [L/s] 1.55 0.53 34.2 0.65 42.1, bbox=[133, 491, 881, 503]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[14]: text=MMEF 75/25 [L/s] 3.22 1.15 35.8 1.44 44.6, bbox=[133, 502, 881, 514]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] coord item[15]: text=MVV [L/min] 100.45, bbox=[133, 514, 454, 525]
2026-08-05 04:52:39,279 INFO     29 [qwen-vl-text] page=3 — 16/16 coords, api_time=9.9s
2026-08-05 04:52:39,281 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1356301, prompt_len=1232
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["报告时间: 2023-12-27", "预计值 实测值 实/预", "VT [L] 0.59 1.51 258.6", "BF [1/min] 20.00 18.08 90.4", "MV [L/min] 11.71 27.39 233.8", "VC MAX [L] 3.28 3.52 107.3", "ERV [L] 0.93 1.39 149.9", "IC [L] 2.35 2.13 90.5", "FVC [L] 3.17 3.52 110.8", "FEV 1 [L] 2.71 2.11 77.7", "FEV 1 % FVC [%] 59.91", "FEV 1 % VC MAX [%] 79.03 59.91 75.8", "PEF [L/s] 6.54 4.76 72.7", "MEF 75 [L/s] 5.68 2.64 46.4", "MEF 50 [L/s] 3.95 1.40 35.4", "MEF 25 [L/s] 1.55 0.53 34.2", "MMEF 75/25 [L/s] 3.22 1.15 35.8", "FEF 75/85 [L/s] 0.85 0.35 41.0", "PIF [L/s] 2.16", "FEF50 % FIF50 [%] 78.19", "MVV [L/min] 100.45", "FEV 1*30 [L/min] 100.45 63.19 62.9"]

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
2026-08-05 04:52:48,684 INFO     29 [qwen-vl-text] coord API raw response (len=1524):
[
	{"text": "报告时间: 2023-12-27", "bbox": [559, 308, 677, 320]},
	{"text": "预计值 实测值 实/预", "bbox": [487, 298, 804, 310]},
	{"text": "VT [L] 0.59 1.51 258.6", "bbox": [164, 343, 807, 355]},
	{"text": "BF [1/min] 20.00 18.08 90.4", "bbox": [164, 355, 807, 367]},
	{"text": "MV [L/min] 11.71 27.39 233.8", "bbox": [164, 367, 807, 378]},
	{"text": "VC MAX [L] 3.28 3.52 107.3", "bbox": [164, 378, 807, 389]},
	{"text": "ERV [L] 0.93 1.39 149.9", "bbox": [164, 389, 807, 400]},
	{"text": "IC [L] 2.35 2.13 90.5", "bbox": [164, 400, 807, 411]},
	{"text": "FVC [L] 3.17 3.52 110.8", "bbox": [164, 416, 807, 427]},
	{"text": "FEV 1 [L] 2.71 2.11 77.7", "bbox": [164, 427, 807, 438]},
	{"text": "FEV 1 % FVC [%] 59.91", "bbox": [164, 438, 807, 449]},
	{"text": "FEV 1 % VC MAX [%] 79.03 59.91 75.8", "bbox": [164, 449, 807, 460]},
	{"text": "PEF [L/s] 6.54 4.76 72.7", "bbox": [164, 460, 807, 471]},
	{"text": "MEF 75 [L/s] 5.68 2.64 46.4", "bbox": [164, 471, 807, 482]},
	{"text": "MEF 50 [L/s] 3.95 1.40 35.4", "bbox": [164, 482, 807, 493]},
	{"text": "MEF 25 [L/s] 1.55 0.53 34.2", "bbox": [164, 493, 807, 504]},
	{"text": "MMEF 75/25 [L/s] 3.22 1.15 35.8", "bbox": [164, 504, 807, 515]},
	{"text": "FEF 75/85 [L/s] 0.85 0.35 41.0", "bbox": [164, 515, 807, 526]},
	{"text": "PIF [L/s] 2.16", "bbox": [164, 526, 689, 537]},
	{"text": "FEF50 % FIF50 [%] 78.19", "bbox": [164, 537, 689, 548]},
	{"text": "MVV [L/min] 100.45", "bbox": [164, 548, 559, 559]},
	{"text": "FEV 1*30 [L/min] 100.45 63.19 62.9", "bbox": [164, 559, 819, 570]}
]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=9.4s
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间: 2023-12-27, bbox=[559, 308, 677, 320]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[1]: text=预计值 实测值 实/预, bbox=[487, 298, 804, 310]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[2]: text=VT [L] 0.59 1.51 258.6, bbox=[164, 343, 807, 355]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[3]: text=BF [1/min] 20.00 18.08 90.4, bbox=[164, 355, 807, 367]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[4]: text=MV [L/min] 11.71 27.39 233.8, bbox=[164, 367, 807, 378]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[5]: text=VC MAX [L] 3.28 3.52 107.3, bbox=[164, 378, 807, 389]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[6]: text=ERV [L] 0.93 1.39 149.9, bbox=[164, 389, 807, 400]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[7]: text=IC [L] 2.35 2.13 90.5, bbox=[164, 400, 807, 411]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[8]: text=FVC [L] 3.17 3.52 110.8, bbox=[164, 416, 807, 427]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[9]: text=FEV 1 [L] 2.71 2.11 77.7, bbox=[164, 427, 807, 438]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[10]: text=FEV 1 % FVC [%] 59.91, bbox=[164, 438, 807, 449]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[11]: text=FEV 1 % VC MAX [%] 79.03 59.91 75.8, bbox=[164, 449, 807, 460]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[12]: text=PEF [L/s] 6.54 4.76 72.7, bbox=[164, 460, 807, 471]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[13]: text=MEF 75 [L/s] 5.68 2.64 46.4, bbox=[164, 471, 807, 482]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[14]: text=MEF 50 [L/s] 3.95 1.40 35.4, bbox=[164, 482, 807, 493]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[15]: text=MEF 25 [L/s] 1.55 0.53 34.2, bbox=[164, 493, 807, 504]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[16]: text=MMEF 75/25 [L/s] 3.22 1.15 35.8, bbox=[164, 504, 807, 515]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[17]: text=FEF 75/85 [L/s] 0.85 0.35 41.0, bbox=[164, 515, 807, 526]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[18]: text=PIF [L/s] 2.16, bbox=[164, 526, 689, 537]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[19]: text=FEF50 % FIF50 [%] 78.19, bbox=[164, 537, 689, 548]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[20]: text=MVV [L/min] 100.45, bbox=[164, 548, 559, 559]
2026-08-05 04:52:48,685 INFO     29 [qwen-vl-text] coord item[21]: text=FEV 1*30 [L/min] 100.45 63.19 62.9, bbox=[164, 559, 819, 570]
2026-08-05 04:52:48,686 INFO     29 [qwen-vl-text] page=4 — 22/22 coords, api_time=9.4s
2026-08-05 04:52:48,686 INFO     29 [qwen-vl-text] new_positions (38):
[[3, 267.8740356445312, 310.7338813476562, 377.80161254882813, 387.3260229492187], [3, 228.58584374999998, 516.6992509765624, 365.10239868164064, 380.976416015625], [3, 79.17165942382812, 310.7338813476562, 384.1512194824219, 396.8504333496094], [3, 79.17165942382812, 310.7338813476562, 394.7338977050781, 406.37484374999997], [3, 79.17165942382812, 524.4378342285156, 409.54964721679687, 423.30712890625], [3, 79.17165942382812, 524.4378342285156, 421.19059326171873, 433.8898071289062], [3, 79.17165942382812, 524.4378342285156, 433.8898071289062, 447.64728881835936], [3, 79.17165942382812, 524.4378342285156, 446.5890209960937, 459.2882348632812], [3, 79.17165942382812, 524.4378342285156, 459.2882348632812, 471.98744873046877], [3, 79.17165942382812, 524.4378342285156, 470.92918090820314, 483.62839477539063], [3, 79.17165942382812, 524.4378342285156, 483.62839477539063, 496.3276086425781], [3, 79.17165942382812, 524.4378342285156, 495.2693408203125, 507.9685546875], [3, 79.17165942382812, 524.4378342285156, 507.9685546875, 520.6677685546875], [3, 79.17165942382812, 524.4378342285156, 519.6095007324219, 532.3087145996094], [3, 79.17165942382812, 524.4378342285156, 531.2504467773438, 543.9496606445313], [3, 79.17165942382812, 270.2551381835937, 543.9496606445313, 555.5906066894531], [4, 332.75907983398434, 403.0016047363281, 325.9464892578125, 338.645703125], [4, 289.8992341308593, 478.60161035156244, 315.36381103515623, 328.0630249023437], [4, 97.62520410156249, 480.3874372558593, 362.98586303710937, 375.68507690429686], [4, 97.62520410156249, 480.3874372558593, 375.68507690429686, 388.38429077148436], [4, 97.62520410156249, 480.3874372558593, 388.38429077148436, 400.0252368164062], [4, 97.62520410156249, 480.3874372558593, 400.0252368164062, 411.66618286132814], [4, 97.62520410156249, 480.3874372558593, 411.66618286132814, 423.30712890625], [4, 97.62520410156249, 480.3874372558593, 423.30712890625, 434.94807495117186], [4, 97.62520410156249, 480.3874372558593, 440.2394140625, 451.8803601074219], [4, 97.62520410156249, 480.3874372558593, 451.8803601074219, 463.52130615234375], [4, 97.62520410156249, 480.3874372558593, 463.52130615234375, 475.1622521972656], [4, 97.62520410156249, 480.3874372558593, 475.1622521972656, 486.8031982421875], [4, 97.62520410156249, 480.3874372558593, 486.8031982421875, 498.4441442871094], [4, 97.62520410156249, 480.3874372558593, 498.4441442871094, 510.08509033203126], [4, 97.62520410156249, 480.3874372558593, 510.08509033203126, 521.7260363769532], [4, 97.62520410156249, 480.3874372558593, 521.7260363769532, 533.366982421875], [4, 97.62520410156249, 480.3874372558593, 533.366982421875, 545.0079284667969], [4, 97.62520410156249, 480.3874372558593, 545.0079284667969, 556.6488745117188], [4, 97.62520410156249, 410.14491235351556, 556.6488745117188, 568.2898205566406], [4, 97.62520410156249, 410.14491235351556, 568.2898205566406, 579.9307666015625], [4, 97.62520410156249, 332.75907983398434, 579.9307666015625, 591.5717126464843], [4, 97.62520410156249, 487.53074487304684, 591.5717126464843, 603.2126586914062]]
2026-08-05 04:52:48,686 INFO     29 [qwen-vl-text] ═══ DONE ═══ 38 positions, pages=2, time=32.6s
2026-08-05 04:52:48,699 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 04:52:48,699 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "208 items", "markdown": "", "text": "", "name": "LHYA-哮喘-沈阳医大四.pdf", "output_format": "chunks", "chunks_Clinical": "3 items, types={'OutpatientRecord': 3}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 3, \"chunks_Examination\": 1, \"chunks_Medication\": 2}"}
2026-08-05 04:52:48,699 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 04:52:48,700 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:52:48.699+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 11, "failed": 0, "current": {"1f65e538908911f1a3da71efcdd7cc1f": {"id": "1f65e538908911f1a3da71efcdd7cc1f", "doc_id": "1f329962908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4590577, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785905403691, "task_type": "dataflow", "root_trace_id": "171541281f15450ca1ea9d4184057967", "root_traceparent": "00-171541281f15450ca1ea9d4184057967-6239d56a1db4ab47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:52:48,701 INFO     29 [ChunkMerger] Merged 6 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 3, 'Extractor:Medication': 2, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 5 noise chunks)
2026-08-05 04:52:49,109 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 04:52:49,110 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 3, 'MedicationRecord': 2, 'ExaminationReport': 1}", "name": "LHYA-哮喘-沈阳医大四.pdf"}
2026-08-05 04:52:49,110 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 04:52:49,188 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785905405928, 'update_date': datetime.datetime(2026, 8, 5, 4, 50, 5), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 169011, 'status': '1'}
2026-08-05 04:52:49,396 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=四平市中心人民医院
门诊诊断书
0003316
(患者保管)
SPZXYy-JLLC-042
姓名
性别
女
年龄
54岁
单位
诊断
支气管哮喘
病情诊断摘要依据
发作性喘息30余年，双肺干
啰音，诊断支气管哮喘
医生处理意见
1.平喘治疗
2.随访
医生签字：
门诊部负责人签字：
科主任签字：
门诊部盖章：2023年12月27日
(无公章和医生章无效)
---
四平市中医医院
门诊病历
初诊
2025年11月26日
肾病糖尿病科
姓名
性别 女性
年龄 55岁
门诊号码 202511260272 (1)
发病日期 2025-11-26
类别 自费
保险卡号
就诊方式 便民门诊费
医生 王亚新
联系地址 四平铁西
联系电话 13689710485
身份证号
职业
体温 36.5 ℃ 血压 130、80 mmHg 脉搏 70 次/分
药物过敏史 无
主诉: 自述糖尿病4年，支气管哮喘30余年
病史: 糖尿病4年，尿中有沫。伴双下肢水肿+。现二甲双胍片，0.5，日3次，口服。血糖控制不佳。葡萄糖：12.39mmol/l.，糖化：
10.1%，一周前感冒山现间断咳嗽气短胸闷，活动后加重，有夜间憋醒史，咳白痰，无发热，饮食尚可，大小便正常。
临床诊断：2型糖尿病 支气管哮喘急性发作
治疗方案:
建议入院治疗，拒绝。糖尿病饮食，监测血糖，继续用药治疗，有变化随诊。沙美特罗卡替松粉吸入剂50微克/250微克/揿/盒，
每瓶60揿（30个用药计量），甲泼尼龙片4mg×24片/盒（口服5天）。
结论:
病程记录:
医生（印章）：王亚新
2025年11月27日 11:18
---
四平市中医医院
内二疗区
门诊病历
初诊
2025年12月31日
姓名
性别：女性
年龄：55岁
门诊号码：202512310183
（1）
发病日期：2025-12-31
类别：自费
保险卡号
就诊方式：服务号
医生：张楷婷
联系地址：吉林省四平市
联系电话：13689710485
身份证号：220303197009242283
职业：
体温 36.4 ℃ 血压 120/78 mmHg 脉搏 66 次/分
药物过敏史：否
主诉：发现血糖升高4年
病史：发现血糖升高4年，现二甲双胍片0.5g日3次口服控制血糖。测空腹血糖11.41mmol/L，糖化血红蛋白8.9%，尿糖3+。
临床诊断：2型糖尿病
治疗方案：建议患者入院治疗，患者暂拒；糖尿病饮食，口服二甲双胍片0.5g日3次，适当饮水，监测血糖，定期复查，病情变化随诊
结论：
病程记录：
医生（印章）：
2025年12月31日 15:12
---
信康大药房--佳合分店
单号：250927207100156
日期：2025-09-27 17:52:20
会员卡号：13689710485
姓名：
积分：37
总积分：47
药品名称
规格
生产企业/药品上市许可持有人
产地
剂型
批号
有效期
数量
单价
金额
12534
185.00
沙美特罗替卡松吸入粉雾剂
50微克/250微克/60泡/盒
葛兰素史克集团吸入粉雾剂
JD6K
2027-06-18
2盒
185.00
370.00
信康大药房温馨提示：您购买的
药品需要常温储存(10℃-30℃)
合计：
370.00
实收：
370.00
开票员：王影
营业员：7139
药品售出无质量问题不退不换！
电话：0434-3333658
---
信康大药房--佳合分店
单号：251128207100163
日期：2025-11-28 16:38:41
会员卡号：13689710485
姓名：
积分：37
总积分：84
药品名称
规格
生产企业/药品上市许可持有人
产地
剂型
批号
有效期
数量
单价
金额
12534
185.00
沙美特罗替卡松吸入粉雾剂
50微克/250微克/60泡/盒
葛兰素史克集团吸入粉雾剂
JD6K
2027-06-18
2盒
185.00
370.00
信康大药房温馨提示：您购买的
药品需要常温储存（10℃-30℃）
合计：
370.00
实收：
370.00
开票员：张欣
营业员：7140
药品售出无质量问题不退不换！
电话：0434-3333658
---
报告时间: 2023-12-27
\multicolumn{2}{c}{预计值} 药前 前/预% 药后 \multicolumn{2}{c}{后/预% 改善率 (%)}
测试日期 23/12/27 23/12/27
测试时间 15:36:14 15:51:45
MV [L/min] 11.71 27.39 233.8 7.6
VC MAX [L] 3.28 3.52 107.3 3.78 115.4
FVC [L] 3.17 3.52 110.8 3.78 119.2
FEV 1 [L] 2.71 2.11 77.7 2.39 88.3
FEV 1 % FVC [%] 63.29
FEV 1 % VC MAX [%] 79.03 59.91 75.8 63.29 80.1
PEF [L/s] 6.54 4.76 72.7 4.54 69.4
MEF 75 [L/s] 5.68 2.64 46.4 3.29 58.0
MEF 50 [L/s] 3.95 1.40 35.4 1.80 45.5
MEF 25 [L/s] 1.55 0.53 34.2 0.65 42.1
MMEF 75/25 [L/s] 3.22 1.15 35.8 1.44 44.6
MVV [L/min] 100.45
报告时间: 2023-12-27
预计值 实测值 实/预
VT [L] 0.59 1.51 258.6
BF [1/min] 20.00 18.08 90.4
MV [L/min] 11.71 27.39 233.8
VC MAX [L] 3.28 3.52 107.3
ERV [L] 0.93 1.39 149.9
IC [L] 2.35 2.13 90.5
FVC [L] 3.17 3.52 110.8
FEV 1 [L] 2.71 2.11 77.7
FEV 1 % FVC [%] 59.91
FEV 1 % VC MAX [%] 79.03 59.91 75.8
PEF [L/s] 6.54 4.76 72.7
MEF 75 [L/s] 5.68 2.64 46.4
MEF 50 [L/s] 3.95 1.40 35.4
MEF 25 [L/s] 1.55 0.53 34.2
MMEF 75/25 [L/s] 3.22 1.15 35.8
FEF 75/85 [L/s] 0.85 0.35 41.0
PIF [L/s] 2.16
FEF50 % FIF50 [%] 78.19
MVV [L/min] 100.45
FEV 1*30 [L/min] 100.45 63.19 62.9
2026-08-05 04:52:49,761 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 04:52:49,761 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 3, 'MedicationRecord': 2, 'ExaminationReport': 1}", "name": "LHYA-哮喘-沈阳医大四.pdf", "embedding_token_consumption": 2385}
2026-08-05 04:52:49,761 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 04:52:49,868 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 04:52:49,868 INFO     29 [Trace] task=1f65e538 | doc=LHYA-哮喘-沈阳医大四.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 04:52:49,871 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:52:49,871 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:52:49,871 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:52:49,871 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:52:49,871 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:52:49,872 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:52:49,875 INFO     29 set_progress(1f65e538908911f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 04:52:49 [DOC Engine]:
Start to index...
2026-08-05 04:52:49,898 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-05 04:52:49,902 INFO     29 set_progress(1f65e538908911f1a3da71efcdd7cc1f), progress: 0.8166666666666668, progress_msg: 
2026-08-05 04:52:49,916 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-05 04:52:49,924 INFO     29 set_progress(1f65e538908911f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 04:52:49 Indexing done (0.05s). Task done (152.07s)
2026-08-05 04:52:49,927 INFO     29 [Done], chunks(6), token(2385), elapsed:152.07
2026-08-05 04:52:50,017 INFO     29 handle_task done for task {"id": "1f65e538908911f1a3da71efcdd7cc1f", "doc_id": "1f329962908911f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "type": "pdf", "location": "LHYA-\u54ee\u5598-\u6c88\u9633\u533b\u5927\u56db.pdf", "size": 4590577, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785905403691, "task_type": "dataflow", "root_trace_id": "171541281f15450ca1ea9d4184057967", "root_traceparent": "00-171541281f15450ca1ea9d4184057967-6239d56a1db4ab47-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
