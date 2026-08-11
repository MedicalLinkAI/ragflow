# 基准结果：LIQU高血糖郑州.pdf

## 基本信息

- 文件：`LIQU高血糖郑州.pdf`
- 大小：9368.0 KB
- PDF 总页数：12
- doc_id：`479f3c48948a11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:08:23  完成时间：2026-08-10T15:12:14  耗时：230.9s
- progress_msg：`07:12:10 Indexing done (0.21s). Task done (222.22s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 6f4ea167 | 1 | 1-1 | 郑州市金水区国基路沙门社区卫生服务中心门诊电子病历 No: 2024111600 |
| 2 | 30e72b26 | 1 | 5-5 | 金水区国基路沙门社区卫生服务中心 Jinshui Gaoji Street Sh |
| 3 | 6362bb45 | 1 | 5-5 | ◆泌尿系彩超（男） (彩超检查) 检查医生：高培利 项目 结果 单位 双肾 双肾 |
| 4 | c98a10b5 | 1 | 5-5 | ◆心电图12号 (心电图) 检查医生：李天柱 项目 结果 单位 心电图 T波异常 |
| 5 | b590ff29 | 1 | 5-5 | ◆胸部正位检查DR(不出片) (DR拍片) 检查医生：申静 项目 结果 单位 胸 |
| 6 | be0fc8c5 | 1 | 7-7 | 越人大药房 祝您身体健康 日期：2025-04-02 NO：1.2468223  |
| 7 | 898af62b | 1 | 8-8 | 越人大药房 祝您身体健康 日期：2025-02-13 NO：1.2467129  |
| 8 | 6cb2bf11 | 1 | 9-9 | 郑州市金水区国基路沙门社区卫生服务中心门诊电子病历 No: 2025041700 |
| 9 | 911fcb64 | 1 | 10-10 | 郑州市金水区国基路沙门社区 卫生服务中心处方笺 医保证号: 费别:自费 门诊号: |
| 10 | 880a752d | 1 | 6-6 | <table><tr><td>红细胞平均分布宽度标准差</td><td>None |
| 11 | f6336b23 | 1 | 6-6 | <table><tr><td>空腹血糖</td><td>None</td><td |
| 12 | ee9442ae | 1 | 6-6 | <table><tr><td>尿酸</td><td>None</td><td>2 |
| 13 | 1886c480 | 1 | 6-6 | <table><tr><td>丙氨酸氨基转移酶</td><td>None</td |
| 14 | 6f0872ac | 1 | 6-6 | <table><tr><td>酸碱度</td><td>None</td><td> |
| 15 | c9a20791 | 1 | 12-12 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 16 | f6f7047a | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>2461</td>< |
| 17 | c7869044 | 1 | 3-3 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |

- chunks 总数：17
- 各 chunk 页数合计（含跨页重复）：17
- 页码并集：`[1, 2, 3, 5, 6, 7, 8, 9, 10, 12]`
- 覆盖页数：10 / 12；缺失页：`[4, 11]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 10/12 页，缺失 [4, 11]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 1 | 1 | 1 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 4 | 4 | 4 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 13 | 0 | 13 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "LabReport": 13, "ExaminationReport": 4, "MedicationRecord": 2, "PrescriptionRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 22, "sources": 8, "stats": {"Extractor:LabExam": 13, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 2, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 4}, "filtered_noise": 3}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 07:12:07,994 INFO     29 [ChunkMerger] Merged 22 chunks from 8 sources: {'Extractor:LabExam': 13, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 2, 'Extractor:Pres`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 07:08:27,225 INFO     29 handle_task begin for task {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 07:08:27,444 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 07:08:27,564 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 07:08:27,582 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:08:27,582 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 07:08:27,582 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 07:08:27,592 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 07:08:27,592 INFO     29 ============================================================
2026-08-10 07:08:27,592 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 07:08:27,592 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 07:08:27,592 INFO     29 ============================================================
2026-08-10 07:08:27,592 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 07:08:27,592 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 07:08:27,594 INFO     29 No torch found.
2026-08-10 07:08:29,144 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=12
2026-08-10 07:08:29,323 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1237654, prompt_len=764
2026-08-10 07:08:30,811 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 07:08:30,811 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 07:08:30,819 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1237654, prompt_len=401
2026-08-10 07:08:34,352 INFO     29 [qwen-vl-parser] text API response (len=580):
["郑州市金水区国基路沙门社区卫生服务中心门诊电子病历", "No: 20241116000027", "就诊类型：初诊", "科别：内科", "就诊时间：2024/11/16 8:09:23", "姓名：.", "性别：男", "年龄：27岁", "电话：", "家庭住址：沙门", "药敏史：无", "发病日期：", "诊断：2型糖尿病", "主诉：发现口渴.口干.多饮多尿.3个月余.", "现病史：患者三个月前发现自己口渴.口干.多饮多尿自测空腹血糖", "11.0mmol/L.规律口服二甲双胍每次0.5g每日三次 血糖控", "制不理想.前来就诊", "既往史：否认药物过敏史，否认传染病史。", "体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，", "心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，", "肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射", "未引出。", "辅助检查：血糖10.6mmol/L. 糖化10%", "初步诊断：二型糖尿病", "处理措施：1.糖尿病饮食.2.适当运动.3.规律服用二甲双胍 4.定期复查", "医师签名：李层", "打印时间：2025/3/19 17:04:36", "症状", "体征", "金水区国基路沙门社区卫生服务中心", "健康管", "理部", ""]
2026-08-10 07:08:34,353 INFO     29 [qwen-vl-parser] page=1 text: 32 lines (bbox 0-31)
2026-08-10 07:08:34,353 INFO     29 [qwen-vl-parser] page=1 text: 32 sections
2026-08-10 07:08:34,484 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=648599, prompt_len=764
2026-08-10 07:08:35,901 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-11-16"
}
```
2026-08-10 07:08:35,902 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2024-11-16
2026-08-10 07:08:35,919 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=648599, prompt_len=756
2026-08-10 07:08:37,249 INFO     29 [qwen-vl-parser] table API response (len=202):
\begin{tabular}{ccccccccc}
\hline
代码 & 项目 & 值 & 单位 & 参考值 & 代码 & 项目 & 值 & 参考 \\
\hline
2461 & 糖化血红蛋白 & 10 & \% & 4.5~5.9 & & & & \\
1056 & 葡萄糖 & 10.60 & mmol/L & 3.89~6.11 & & & & \\
\hline
\end{tabular}
2026-08-10 07:08:37,250 INFO     29 [qwen-vl-parser] page=2 table: 9 LaTeX lines (bbox 32-40)
2026-08-10 07:08:37,250 INFO     29 [qwen-vl-parser] page=2 table: 9 sections
2026-08-10 07:08:37,331 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:08:37.331+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"48638ddc948a11f1bd9827cf206dfa2d": {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:08:37,401 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1096670, prompt_len=764
2026-08-10 07:08:38,926 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 07:08:38,927 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=None
2026-08-10 07:08:38,940 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1096670, prompt_len=756
2026-08-10 07:08:45,012 INFO     29 [qwen-vl-parser] table API response (len=1160):
\begin{tabular}{|c|c|c|c|c|c|}
\hline
乙肝表面抗原 (HBsAg) & 乙肝表面抗体 (HBsAb) & 乙肝e抗原 (HBeAg) & 乙肝e抗体 (HBeAb) & 乙肝核心抗体 (HBcAb) & 临床意义 \\
\hline
阳性 (+) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 乙肝感染早期 \\
\hline
阳性 (+) & 阴性 (-) & 阳性 (+) & 阴性 (-) & 阳性 (+) & 急性或慢性乙型肝炎 \\
\hline
阳性 (+) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 阳性 (+) & 慢性乙肝或乙肝趋向恢复或乙肝病毒携带者 \\
\hline
阳性 (+) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 慢性乙型肝炎或乙肝病毒携带者 \\
\hline
阴性 (-) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 各性乙肝病毒感染“核心窗口期”或既往感染或过乙肝 \\
\hline
阴性 (-) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 阳性 (+) & 乙肝恢复期 \\
\hline
阴性 (-) & 阳性 (+) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 乙肝病毒既往感染, 有免疫力 \\
\hline
阴性 (-) & 阳性 (+) & 阴性 (-) & 阳性 (+) & 阳性 (+) & 乙肝病毒既往感染, 有免疫力 \\
\hline
阴性 (-) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 未乙肝感染应及时接种乙肝疫苗 \\
\hline
阴性 (-) & 阳性 (+) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 有乙肝免疫力 \\
\hline
\end{tabular}

\begin{tabular}{|l|l|}
\hline
\multicolumn{2}{|c|}{\textbf{乙肝五项 (免疫检测)}} \\
\hline
\multicolumn{2}{|r|}{检查医生: 朱凯莉} \\
\hline
项目 & 结果 \\
\hline
乙型肝炎病毒表面抗原 (HBsAg) & 阳性 \\
\hline
乙型肝炎病毒表面抗体 (HBsAb) & 阴性 \\
\hline
乙型肝炎病毒e抗原 (HBeAg) & 阴性 \\
\hline
乙型肝炎病毒e抗体 (HBeAb) & 阳性 \\
\hline
乙型肝炎病毒核心抗体 (HBcAb) & 阳性 \\
\hline
\end{tabular}
2026-08-10 07:08:45,014 INFO     29 [qwen-vl-parser] page=3 table: 44 LaTeX lines (bbox 41-84)
2026-08-10 07:08:45,014 INFO     29 [qwen-vl-parser] page=3 table: 44 sections
2026-08-10 07:08:45,199 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=893038, prompt_len=764
2026-08-10 07:08:46,569 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 07:08:46,570 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=None
2026-08-10 07:08:46,582 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=893038, prompt_len=756
2026-08-10 07:08:53,657 INFO     29 [qwen-vl-parser] table API response (len=1566):
\begin{tabular}{l c c c c c}
\hline
\multicolumn{2}{l}{\textbf{金水区国基路沙门社区卫生服务中心}} & \multicolumn{2}{l}{\textbf{姓名:}} & \multicolumn{2}{l}{\textbf{条码号: 1001241021000001}} \\
\multicolumn{2}{l}{\textbf{Jinshui Guoji Road Sha Men Community Services Center}} & \multicolumn{2}{l}{} & \multicolumn{2}{l}{} \\
\hline
\multicolumn{2}{l}{红细胞平均分布宽度标准差} & 42.6 & fL & & 35.0-56.0 \\
\multicolumn{2}{l}{红细胞平均分布宽度变异系数} & 11.6 & \% & & 11.0-16.0 \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
\multicolumn{5}{l}{\textbf{◆空腹血糖 (生化检验) \quad 检查医生: 朱凯莉}} \\
\hline
项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\
\hline
空腹血糖 & 16.93 $\uparrow$ & mmol/L & 偏高 & 3.89-6.11 \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
\multicolumn{5}{l}{\textbf{◆肾功能 3 项 (生化检验) \quad 检查医生: 朱凯莉}} \\
\hline
项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\
\hline
尿酸 & 254.9 & $\mu$mol/L & & 202-416 \\
肌酐 & 57.0 & $\mu$mol/L & & 57-97 \\
尿素 & 3.29 $\downarrow$ & mmol/L & 偏低 & 3.6-9.5 \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
\multicolumn{5}{l}{\textbf{◆肝功七项 (生化检验) \quad 检查医生: 朱凯莉}} \\
\hline
项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\
\hline
丙氨酸氨基转移酶 & 43.7 & U/L & & 9-50 \\
门冬氨酸氨基转移酶 & 20.5 & U/L & & 0-40 \\
谷氨酰转肽酶 & 53.5 & U/L & & 11-61 \\
总蛋白 & 78.7 & g/L & & 66-87 \\
白蛋白 & 44.4 & g/L & & 40-55 \\
总胆红素 & 10.4 & $\mu$mol/L & & 5.1-19 \\
直接胆红素 & 2.6 & $\mu$mol/L & & 1.7-6.8 \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
\multicolumn{5}{l}{\textbf{◆尿常规 \quad 检查医生: 朱凯莉}} \\
\hline
项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\
\hline
酸碱度 & 5.5 & & & 5.4-8.4 \\
亚硝酸盐 & - & & & 阴性 \\
\hline
\end{tabular}
2026-08-10 07:08:53,659 INFO     29 [qwen-vl-parser] page=4 table: 54 LaTeX lines (bbox 85-138)
2026-08-10 07:08:53,659 INFO     29 [qwen-vl-parser] page=4 table: 54 sections
2026-08-10 07:08:53,782 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=710767, prompt_len=764
2026-08-10 07:08:55,107 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 07:08:55,107 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 07:08:55,126 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=710767, prompt_len=401
2026-08-10 07:08:58,980 INFO     29 [qwen-vl-parser] text API response (len=720):
["金水区国基路沙门社区卫生服务中心", "Jinshui Gaoji Street Shamen Community Health Services Center", "0001", "姓名：", "条码号：1001241021000001", "流借号：", "胆", "胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增", "宽。", "胰", "胰腺形态、大小正常，内部光点均匀，主胰管无扩张。", "脾", "脾脏大小形态正常，实质回声均匀。", "科室小结：", "脂肪肝", "◆泌尿系彩超（男）", "(彩超检查)", "检查医生：高培利", "项目", "结果", "单位", "双肾", "双肾形态大小正常、包膜完整光滑，肾实质回声光点均匀，肾盂肾", "盏未见扩张。", "前列腺", "前列腺形态大小正常，轮廓整齐，实质回声均匀。", "膀胱", "膀胱充盈欠佳，壁光滑，其内未见明显异常回声。", "输尿管", "输尿管未见显示扩张。", "科室小结：", "未见明显异常", "◆心电图12号 (心电图)", "检查医生：李天柱", "项目", "结果", "单位", "心电图", "T波异常", "科室小结：", "T波异常", "◆胸部正位检查DR(不出片) (DR拍片)", "检查医生：申静", "项目", "结果", "单位", "胸部正位检查（DR）", "胸廓对称，纵隔及气管居中，未见增宽。肺门形态、大小、位置未", "见异常。两肺纹理走行自然，未见明显异常密度影。心影形态、大", "小未见异常。两膈面光整，两肋膈角锐利。", "科室小结：", "未见明显异常", "第-5-页"]
2026-08-10 07:08:58,981 INFO     29 [qwen-vl-parser] page=5 text: 53 lines (bbox 139-191)
2026-08-10 07:08:58,981 INFO     29 [qwen-vl-parser] page=5 text: 53 sections
2026-08-10 07:08:59,142 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=893283, prompt_len=764
2026-08-10 07:09:00,539 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 07:09:00,540 INFO     29 [qwen-vl-parser] page=6 classify=table report_date=None
2026-08-10 07:09:00,569 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=893283, prompt_len=756
2026-08-10 07:09:07,158 INFO     29 [qwen-vl-parser] table API response (len=1441):
\begin{tabular}{l c c c c}
\hline
\multicolumn{2}{l}{\textbf{红细胞平均分布宽度标准差}} & 42.6 & fL & 35.0-56.0 \\
\hline
\multicolumn{2}{l}{\textbf{红细胞平均分布宽度变异系数}} & 11.6 & \% & 11.0-16.0 \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
\multicolumn{5}{c}{\textbf{◆空腹血糖 (生化检验)}} \\
\multicolumn{5}{r}{检查医生: 朱凯莉} \\
\hline
项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\
\hline
空腹血糖 & 16.93 $\uparrow$ & mmol/L & 偏高 & 3.89-6.11 \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
\multicolumn{5}{c}{\textbf{◆肾功能 3 项 (生化检验)}} \\
\multicolumn{5}{r}{检查医生: 朱凯莉} \\
\hline
项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\
\hline
尿酸 & 254.9 & $\mu$mol/L & & 202-416 \\
\hline
肌酐 & 57.0 & $\mu$mol/L & & 57-97 \\
\hline
尿素 & 3.29 $\downarrow$ & mmol/L & 偏低 & 3.6-9.5 \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
\multicolumn{5}{c}{\textbf{◆肝功七项 (生化检验)}} \\
\multicolumn{5}{r}{检查医生: 朱凯莉} \\
\hline
项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\
\hline
丙氨酸氨基转移酶 & 43.7 & U/L & & 9-50 \\
\hline
门冬氨酸氨基转移酶 & 20.5 & U/L & & 0-40 \\
\hline
谷氨酰转肽酶 & 53.5 & U/L & & 11-61 \\
\hline
总蛋白 & 78.7 & g/L & & 66-87 \\
\hline
白蛋白 & 44.4 & g/L & & 40-55 \\
\hline
总胆红素 & 10.4 & $\mu$mol/L & & 5.1-19 \\
\hline
直接胆红素 & 2.6 & $\mu$mol/L & & 1.7-6.8 \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
\multicolumn{5}{c}{\textbf{◆尿常规}} \\
\multicolumn{5}{r}{检查医生: 朱凯莉} \\
\hline
项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\
\hline
酸碱度 & 5.5 & & & 5.4-8.4 \\
\hline
亚硝酸盐 & - & & & 阴性 \\
\hline
\end{tabular}
2026-08-10 07:09:07,159 INFO     29 [qwen-vl-parser] page=6 table: 65 LaTeX lines (bbox 192-256)
2026-08-10 07:09:07,159 INFO     29 [qwen-vl-parser] page=6 table: 65 sections
2026-08-10 07:09:07,280 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=868370, prompt_len=764
2026-08-10 07:09:07,417 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:09:07.415+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"48638ddc948a11f1bd9827cf206dfa2d": {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:09:08,630 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 07:09:08,630 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 07:09:08,641 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=868370, prompt_len=401
2026-08-10 07:09:10,913 INFO     29 [qwen-vl-parser] text API response (len=275):
["越人大药房", "祝您身体健康", "日期：2025-04-02 NO：1.2468223", "会员：  会员卡：1004832", "药品名称 数量 单位 单价 金额", "盐酸二甲双胍 0.25*60 片", "生产厂商：上海信谊", "批号：", "2 5.50 11.00", "应收：11.00 收款：11.00", "找零：0.00 找零：0.00", "付款方式：现金 实收：11.00", "收款：刘丽婷 时间：11：06：25", "地址：三全路渠东路东岸尚景", "电话：63222645", "药品无质量问题概不退换！"]
2026-08-10 07:09:10,914 INFO     29 [qwen-vl-parser] page=7 text: 16 lines (bbox 257-272)
2026-08-10 07:09:10,914 INFO     29 [qwen-vl-parser] page=7 text: 16 sections
2026-08-10 07:09:11,018 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=673949, prompt_len=764
2026-08-10 07:09:12,522 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 07:09:12,523 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 07:09:12,534 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=673949, prompt_len=401
2026-08-10 07:09:14,520 INFO     29 [qwen-vl-parser] text API response (len=283):
["越人大药房", "祝您身体健康", "日期：2025-02-13 NO：1.2467129", "会员：", "会员卡：1004832", "药品名称 数量 单位 单价 金额", "盐酸二甲双胍 规格：0.25*60片", "生产厂商：上海信宜", "批号：", "5 盒 5.50 27.50", "应收：27.50 收款：27.50", "找零：0.00 折扣：0.00", "付款方式：a 现金 实收：27.50", "收款：刘丽婷 时间：16:27:56", "地址：三全路渠东路东岸尚景", "电话：63222645", "药品无质量问题概不退换！"]
2026-08-10 07:09:14,520 INFO     29 [qwen-vl-parser] page=8 text: 17 lines (bbox 273-289)
2026-08-10 07:09:14,520 INFO     29 [qwen-vl-parser] page=8 text: 17 sections
2026-08-10 07:09:14,684 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1326544, prompt_len=764
2026-08-10 07:09:16,039 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 07:09:16,040 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 07:09:16,051 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1326544, prompt_len=401
2026-08-10 07:09:19,552 INFO     29 [qwen-vl-parser] text API response (len=545):
["郑州市金水区国基路沙门社区卫生服务中心门诊电子病历", "No: 20250417000042", "就诊类型：初诊 科别：内科 就诊时间：2025/4/17 8:14:34", "姓名： 性别：男 年龄：27岁 电话：13673657585", "家庭住址：沙门 药敏史：无", "发病日期：2025-04-17 诊断：糖尿病", "主诉：患糖尿病1年余", "现病史：患者1年前发现自己口渴，口干，多饮多尿，自测空腹血糖", "11.0mmol/1，规律口服二甲双胍 每次0.5，每日三次，现来复查", "就诊", "既往史：否认药物过敏史，否认传染病史。", "体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，", "心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，", "肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射", "未引出。", "辅助检查：血糖11.15mmol/1 糖化血红蛋白9%", "初步诊断：二型糖尿病", "处理措施：1，糖尿病饮食 保持心情愉悦 2，适量运动 3.继续规律服用 二", "甲双胍片 4，定期检测血糖 5.不适随诊", "医师签名：李层 打印时间：2025/4/22 17:08:28", "健康管理部门"]
2026-08-10 07:09:19,552 INFO     29 [qwen-vl-parser] page=9 text: 21 lines (bbox 290-310)
2026-08-10 07:09:19,553 INFO     29 [qwen-vl-parser] page=9 text: 21 sections
2026-08-10 07:09:19,640 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=462543, prompt_len=764
2026-08-10 07:09:20,929 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 07:09:20,930 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 07:09:20,939 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=462543, prompt_len=401
2026-08-10 07:09:22,853 INFO     29 [qwen-vl-parser] text API response (len=292):
["郑州市金水区国基路沙门社区", "卫生服务中心处方笺", "医保证号:", "费别:自费", "门诊号:20250417000042", "日期:2025-04-17", "姓名:", "性别:男", "年龄:27岁", "科别:内科", "住址:沙门", "临床诊断:糖尿病", "Rp:", "1 (基)(集)盐酸二甲双胍缓释片(0.5g*60S)", "2瓶", "用法:每次0.5g口服一天三次*30天", "医师(签字/盖章):李层", "审核、调配:", "核对、发药:", "药费:10.34", "执行科室:西药房", "打印日期:2025/04/17", ""]
2026-08-10 07:09:22,853 INFO     29 [qwen-vl-parser] page=10 text: 22 lines (bbox 311-332)
2026-08-10 07:09:22,853 INFO     29 [qwen-vl-parser] page=10 text: 22 sections
2026-08-10 07:09:23,014 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1118214, prompt_len=764
2026-08-10 07:09:24,499 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-17"}
```
2026-08-10 07:09:24,499 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2025-04-17
2026-08-10 07:09:24,508 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1118214, prompt_len=401
2026-08-10 07:09:27,995 INFO     29 [qwen-vl-parser] text API response (len=561):
["No 20250417000C", "郑州市金水区国基路沙门社区", "自费及其他", "No 20250417000062", "2025-04-17", "自费费用:", "西药费", "10.34", "先行自付:", "10.34", "超限价自付:", "医疗救助:", "统筹记账:", "0.00", "大额记账:", "0.00", "公务员记账:", "0.00", "微信: 10.34", "个人账户: 0.00", "(共济支付)", "现金支付: 10.34", "其他支出:", "(大病补充:", "贫困救助:", "政府兜底:)", "壹拾元叁角肆分", "10.34", "总合计: 10.34", "诊间结算 2025-04-17", "诊间结算 2025-04-17", "0", "0.00", "0.00", "10.34", "2025-0", "No 202504170000", "郑州市金水区国基路沙门社区", "000108", "No 2025041", "自费及其他", "西药房", "内科", "李层", "刘权", "西药费", "10.34", "壹拾元叁角肆分", "10.34", "0.00", "10.34", "2025-04-17", ""]
2026-08-10 07:09:27,995 INFO     29 [qwen-vl-parser] page=11 text: 52 lines (bbox 333-384)
2026-08-10 07:09:27,995 INFO     29 [qwen-vl-parser] page=11 text: 52 sections
2026-08-10 07:09:28,155 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=825496, prompt_len=764
2026-08-10 07:09:29,749 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-17"
}
```
2026-08-10 07:09:29,749 INFO     29 [qwen-vl-parser] page=12 classify=table report_date=2025-04-17
2026-08-10 07:09:29,759 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=825496, prompt_len=756
2026-08-10 07:09:31,037 INFO     29 [qwen-vl-parser] table API response (len=179):
\begin{tabular}{cccccc}
\hline
代码 & 项目 & 值 & 单位 & 参考值 & \\
\hline
2461 & 糖化血红蛋白 & 9 & \% & 4.5$\sim$5.9 & \\
1056 & 葡萄糖 & 11.15 & mmol/L & 3.89$\sim$6.11 & \\
\hline
\end{tabular}
2026-08-10 07:09:31,038 INFO     29 [qwen-vl-parser] page=12 table: 9 LaTeX lines (bbox 385-393)
2026-08-10 07:09:31,039 INFO     29 [qwen-vl-parser] page=12 table: 9 sections
2026-08-10 07:09:31,039 INFO     29 [qwen-vl-parser] parse_pdf done: 394 sections from 12 pages.
2026-08-10 07:09:31,059 INFO     29 Close text detector.
2026-08-10 07:09:31,461 INFO     29 Close text recognizer.
2026-08-10 07:09:31,923 INFO     29 Close recognizer.
2026-08-10 07:09:32,385 INFO     29 Close recognizer.
2026-08-10 07:09:32,854 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 07:09:32,855 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Parser:MedLink | outputs={"html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "json"}
2026-08-10 07:09:32,855 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 07:09:32,884 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:09:32,884 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 郑州市金水区国基路沙门社区卫生服务中心门诊电子病历\n[BBOX-1] No: 20241116000027\n[BBOX-2] 就诊类型：初诊\n[BBOX-3] 科别：内科\n[BBOX-4] 就诊时间：2024/11/16 8:09:23\n[BBOX-5] 姓名：.\n[BBOX-6] 性别：男\n[BBOX-7] 年龄：27岁\n[BBOX-8] 电话：\n[BBOX-9] 家庭住址：沙门\n[BBOX-10] 药敏史：无\n[BBOX-11] 发病日期：\n[BBOX-12] 诊断：2型糖尿病\n[BBOX-13] 主诉：发现口渴.口干.多饮多尿.3个月余.\n[BBOX-14] 现病史：患者三个月前发现自己口渴.口干.多饮多尿自测空腹血糖\n[BBOX-15] 11.0mmol/L.规律口服二甲双胍每次0.5g每日三次 血糖控\n[BBOX-16] 制不理想.前来就诊\n[BBOX-17] 既往史：否认药物过敏史，否认传染病史。\n[BBOX-18] 体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，\n[BBOX-19] 心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，\n[BBOX-20] 肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射\n[BBOX-21] 未引出。\n[BBOX-22] 辅助检查：血糖10.6mmol/L. 糖化10%\n[BBOX-23] 初步诊断：二型糖尿病\n[BBOX-24] 处理措施：1.糖尿病饮食.2.适当运动.3.规律服用二甲双胍 4.定期复查\n[BBOX-25] 医师签名：李层\n[BBOX-26] 打印时间：2025/3/19 17:04:36\n[BBOX-27] 症状\n[BBOX-28] 体征\n[BBOX-29] 金水区国基路沙门社区卫生服务中心\n[BBOX-30] 健康管\n[BBOX-31] 理部\n[BBOX-32] \\begin{tabular}{ccccccccc}\n[BBOX-33] 报告时间: 2024-11-16\n[BBOX-34] \\hline\n[BBOX-35] 代码 & 项目 & 值 & 单位 & 参考值 & 代码 & 项目 & 值 & 参考 \\\\\n[BBOX-36] \\hline\n[BBOX-37] 2461 & 糖化血红蛋白 & 10 & \\% & 4.5~5.9 & & & & \\\\\n[BBOX-38] 1056 & 葡萄糖 & 10.60 & mmol/L & 3.89~6.11 & & & & \\\\\n[BBOX-39] \\hline\n[BBOX-40] \\end{tabular}\n[BBOX-41] \\begin{tabular}{|c|c|c|c|c|c|}\n[BBOX-42] \\hline\n[BBOX-43] 乙肝表面抗原 (HBsAg) & 乙肝表面抗体 (HBsAb) & 乙肝e抗原 (HBeAg) & 乙肝e抗体 (HBeAb) & 乙肝核心抗体 (HBcAb) & 临床意义 \\\\\n[BBOX-44] \\hline\n[BBOX-45] 阳性 (+) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 乙肝感染早期 \\\\\n[BBOX-46] \\hline\n[BBOX-47] 阳性 (+) & 阴性 (-) & 阳性 (+) & 阴性 (-) & 阳性 (+) & 急性或慢性乙型肝炎 \\\\\n[BBOX-48] \\hline\n[BBOX-49] 阳性 (+) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 阳性 (+) & 慢性乙肝或乙肝趋向恢复或乙肝病毒携带者 \\\\\n[BBOX-50] \\hline\n[BBOX-51] 阳性 (+) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 慢性乙型肝炎或乙肝病毒携带者 \\\\\n[BBOX-52] \\hline\n[BBOX-53] 阴性 (-) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 各性乙肝病毒感染“核心窗口期”或既往感染或过乙肝 \\\\\n[BBOX-54] \\hline\n[BBOX-55] 阴性 (-) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 阳性 (+) & 乙肝恢复期 \\\\\n[BBOX-56] \\hline\n[BBOX-57] 阴性 (-) & 阳性 (+) & 阴性 (-) & 阴性 (-) & 阳性 (+) & 乙肝病毒既往感染, 有免疫力 \\\\\n[BBOX-58] \\hline\n[BBOX-59] 阴性 (-) & 阳性 (+) & 阴性 (-) & 阳性 (+) & 阳性 (+) & 乙肝病毒既往感染, 有免疫力 \\\\\n[BBOX-60] \\hline\n[BBOX-61] 阴性 (-) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 未乙肝感染应及时接种乙肝疫苗 \\\\\n[BBOX-62] \\hline\n[BBOX-63] 阴性 (-) & 阳性 (+) & 阴性 (-) & 阴性 (-) & 阴性 (-) & 有乙肝免疫力 \\\\\n[BBOX-64] \\hline\n[BBOX-65] \\end{tabular}\n[BBOX-66] \\begin{tabular}{|l|l|}\n[BBOX-67] \\hline\n[BBOX-68] \\multicolumn{2}{|c|}{\\textbf{乙肝五项 (免疫检测)}} \\\\\n[BBOX-69] \\hline\n[BBOX-70] \\multicolumn{2}{|r|}{检查医生: 朱凯莉} \\\\\n[BBOX-71] \\hline\n[BBOX-72] 项目 & 结果 \\\\\n[BBOX-73] \\hline\n[BBOX-74] 乙型肝炎病毒表面抗原 (HBsAg) & 阳性 \\\\\n[BBOX-75] \\hline\n[BBOX-76] 乙型肝炎病毒表面抗体 (HBsAb) & 阴性 \\\\\n[BBOX-77] \\hline\n[BBOX-78] 乙型肝炎病毒e抗原 (HBeAg) & 阴性 \\\\\n[BBOX-79] \\hline\n[BBOX-80] 乙型肝炎病毒e抗体 (HBeAb) & 阳性 \\\\\n[BBOX-81] \\hline\n[BBOX-82] 乙型肝炎病毒核心抗体 (HBcAb) & 阳性 \\\\\n[BBOX-83] \\hline\n[BBOX-84] \\end{tabular}\n[BBOX-85] \\begin{tabular}{l c c c c c}\n[BBOX-86] \\hline\n[BBOX-87] \\multicolumn{2}{l}{\\textbf{金水区国基路沙门社区卫生服务中心}} & \\multicolumn{2}{l}{\\textbf{姓名:}} & \\multicolumn{2}{l}{\\textbf{条码号: 1001241021000001}} \\\\\n[BBOX-88] \\multicolumn{2}{l}{\\textbf{Jinshui Guoji Road Sha Men Community Services Center}} & \\multicolumn{2}{l}{} & \\multicolumn{2}{l}{} \\\\\n[BBOX-89] \\hline\n[BBOX-90] \\multicolumn{2}{l}{红细胞平均分布宽度标准差} & 42.6 & fL & & 35.0-56.0 \\\\\n[BBOX-91] \\multicolumn{2}{l}{红细胞平均分布宽度变异系数} & 11.6 & \\% & & 11.0-16.0 \\\\\n[BBOX-92] \\hline\n[BBOX-93] \\end{tabular}\n[BBOX-94] \\begin{tabular}{l c c c c}\n[BBOX-95] \\hline\n[BBOX-96] \\multicolumn{5}{l}{\\textbf{◆空腹血糖 (生化检验) \\quad 检查医生: 朱凯莉}} \\\\\n[BBOX-97] \\hline\n[BBOX-98] 项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n[BBOX-99] \\hline\n[BBOX-100] 空腹血糖 & 16.93 $\\uparrow$ & mmol/L & 偏高 & 3.89-6.11 \\\\\n[BBOX-101] \\hline\n[BBOX-102] \\end{tabular}\n[BBOX-103] \\begin{tabular}{l c c c c}\n[BBOX-104] \\hline\n[BBOX-105] \\multicolumn{5}{l}{\\textbf{◆肾功能 3 项 (生化检验) \\quad 检查医生: 朱凯莉}} \\\\\n[BBOX-106] \\hline\n[BBOX-107] 项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n[BBOX-108] \\hline\n[BBOX-109] 尿酸 & 254.9 & $\\mu$mol/L & & 202-416 \\\\\n[BBOX-110] 肌酐 & 57.0 & $\\mu$mol/L & & 57-97 \\\\\n[BBOX-111] 尿素 & 3.29 $\\downarrow$ & mmol/L & 偏低 & 3.6-9.5 \\\\\n[BBOX-112] \\hline\n[BBOX-113] \\end{tabular}\n[BBOX-114] \\begin{tabular}{l c c c c}\n[BBOX-115] \\hline\n[BBOX-116] \\multicolumn{5}{l}{\\textbf{◆肝功七项 (生化检验) \\quad 检查医生: 朱凯莉}} \\\\\n[BBOX-117] \\hline\n[BBOX-118] 项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n[BBOX-119] \\hline\n[BBOX-120] 丙氨酸氨基转移酶 & 43.7 & U/L & & 9-50 \\\\\n[BBOX-121] 门冬氨酸氨基转移酶 & 20.5 & U/L & & 0-40 \\\\\n[BBOX-122] 谷氨酰转肽酶 & 53.5 & U/L & & 11-61 \\\\\n[BBOX-123] 总蛋白 & 78.7 & g/L & & 66-87 \\\\\n[BBOX-124] 白蛋白 & 44.4 & g/L & & 40-55 \\\\\n[BBOX-125] 总胆红素 & 10.4 & $\\mu$mol/L & & 5.1-19 \\\\\n[BBOX-126] 直接胆红素 & 2.6 & $\\mu$mol/L & & 1.7-6.8 \\\\\n[BBOX-127] \\hline\n[BBOX-128] \\end{tabular}\n[BBOX-129] \\begin{tabular}{l c c c c}\n[BBOX-130] \\hline\n[BBOX-131] \\multicolumn{5}{l}{\\textbf{◆尿常规 \\quad 检查医生: 朱凯莉}} \\\\\n[BBOX-132] \\hline\n[BBOX-133] 项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n[BBOX-134] \\hline\n[BBOX-135] 酸碱度 & 5.5 & & & 5.4-8.4 \\\\\n[BBOX-136] 亚硝酸盐 & - & & & 阴性 \\\\\n[BBOX-137] \\hline\n[BBOX-138] \\end{tabular}\n[BBOX-139] 金水区国基路沙门社区卫生服务中心\n[BBOX-140] Jinshui Gaoji Street Shamen Community Health Services Center\n[BBOX-141] 0001\n[BBOX-142] 姓名：\n[BBOX-143] 条码号：1001241021000001\n[BBOX-144] 流借号：\n[BBOX-145] 胆\n[BBOX-146] 胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增\n[BBOX-147] 宽。\n[BBOX-148] 胰\n[BBOX-149] 胰腺形态、大小正常，内部光点均匀，主胰管无扩张。\n[BBOX-150] 脾\n[BBOX-151] 脾脏大小形态正常，实质回声均匀。\n[BBOX-152] 科室小结：\n[BBOX-153] 脂肪肝\n[BBOX-154] ◆泌尿系彩超（男）\n[BBOX-155] (彩超检查)\n[BBOX-156] 检查医生：高培利\n[BBOX-157] 项目\n[BBOX-158] 结果\n[BBOX-159] 单位\n[BBOX-160] 双肾\n[BBOX-161] 双肾形态大小正常、包膜完整光滑，肾实质回声光点均匀，肾盂肾\n[BBOX-162] 盏未见扩张。\n[BBOX-163] 前列腺\n[BBOX-164] 前列腺形态大小正常，轮廓整齐，实质回声均匀。\n[BBOX-165] 膀胱\n[BBOX-166] 膀胱充盈欠佳，壁光滑，其内未见明显异常回声。\n[BBOX-167] 输尿管\n[BBOX-168] 输尿管未见显示扩张。\n[BBOX-169] 科室小结：\n[BBOX-170] 未见明显异常\n[BBOX-171] ◆心电图12号 (心电图)\n[BBOX-172] 检查医生：李天柱\n[BBOX-173] 项目\n[BBOX-174] 结果\n[BBOX-175] 单位\n[BBOX-176] 心电图\n[BBOX-177] T波异常\n[BBOX-178] 科室小结：\n[BBOX-179] T波异常\n[BBOX-180] ◆胸部正位检查DR(不出片) (DR拍片)\n[BBOX-181] 检查医生：申静\n[BBOX-182] 项目\n[BBOX-183] 结果\n[BBOX-184] 单位\n[BBOX-185] 胸部正位检查（DR）\n[BBOX-186] 胸廓对称，纵隔及气管居中，未见增宽。肺门形态、大小、位置未\n[BBOX-187] 见异常。两肺纹理走行自然，未见明显异常密度影。心影形态、大\n[BBOX-188] 小未见异常。两膈面光整，两肋膈角锐利。\n[BBOX-189] 科室小结：\n[BBOX-190] 未见明显异常\n[BBOX-191] 第-5-页\n[BBOX-192] \\begin{tabular}{l c c c c}\n[BBOX-193] \\hline\n[BBOX-194] \\multicolumn{2}{l}{\\textbf{红细胞平均分布宽度标准差}} & 42.6 & fL & 35.0-56.0 \\\\\n[BBOX-195] \\hline\n[BBOX-196] \\multicolumn{2}{l}{\\textbf{红细胞平均分布宽度变异系数}} & 11.6 & \\% & 11.0-16.0 \\\\\n[BBOX-197] \\hline\n[BBOX-198] \\end{tabular}\n[BBOX-199] \\begin{tabular}{l c c c c}\n[BBOX-200] \\hline\n[BBOX-201] \\multicolumn{5}{c}{\\textbf{◆空腹血糖 (生化检验)}} \\\\\n[BBOX-202] \\multicolumn{5}{r}{检查医生: 朱凯莉} \\\\\n[BBOX-203] \\hline\n[BBOX-204] 项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n[BBOX-205] \\hline\n[BBOX-206] 空腹血糖 & 16.93 $\\uparrow$ & mmol/L & 偏高 & 3.89-6.11 \\\\\n[BBOX-207] \\hline\n[BBOX-208] \\end{tabular}\n[BBOX-209] \\begin{tabular}{l c c c c}\n[BBOX-210] \\hline\n[BBOX-211] \\multicolumn{5}{c}{\\textbf{◆肾功能 3 项 (生化检验)}} \\\\\n[BBOX-212] \\multicolumn{5}{r}{检查医生: 朱凯莉} \\\\\n[BBOX-213] \\hline\n[BBOX-214] 项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n[BBOX-215] \\hline\n[BBOX-216] 尿酸 & 254.9 & $\\mu$mol/L & & 202-416 \\\\\n[BBOX-217] \\hline\n[BBOX-218] 肌酐 & 57.0 & $\\mu$mol/L & & 57-97 \\\\\n[BBOX-219] \\hline\n[BBOX-220] 尿素 & 3.29 $\\downarrow$ & mmol/L & 偏低 & 3.6-9.5 \\\\\n[BBOX-221] \\hline\n[BBOX-222] \\end{tabular}\n[BBOX-223] \\begin{tabular}{l c c c c}\n[BBOX-224] \\hline\n[BBOX-225] \\multicolumn{5}{c}{\\textbf{◆肝功七项 (生化检验)}} \\\\\n[BBOX-226] \\multicolumn{5}{r}{检查医生: 朱凯莉} \\\\\n[BBOX-227] \\hline\n[BBOX-228] 项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n[BBOX-229] \\hline\n[BBOX-230] 丙氨酸氨基转移酶 & 43.7 & U/L & & 9-50 \\\\\n[BBOX-231] \\hline\n[BBOX-232] 门冬氨酸氨基转移酶 & 20.5 & U/L & & 0-40 \\\\\n[BBOX-233] \\hline\n[BBOX-234] 谷氨酰转肽酶 & 53.5 & U/L & & 11-61 \\\\\n[BBOX-235] \\hline\n[BBOX-236] 总蛋白 & 78.7 & g/L & & 66-87 \\\\\n[BBOX-237] \\hline\n[BBOX-238] 白蛋白 & 44.4 & g/L & & 40-55 \\\\\n[BBOX-239] \\hline\n[BBOX-240] 总胆红素 & 10.4 & $\\mu$mol/L & & 5.1-19 \\\\\n[BBOX-241] \\hline\n[BBOX-242] 直接胆红素 & 2.6 & $\\mu$mol/L & & 1.7-6.8 \\\\\n[BBOX-243] \\hline\n[BBOX-244] \\end{tabular}\n[BBOX-245] \\begin{tabular}{l c c c c}\n[BBOX-246] \\hline\n[BBOX-247] \\multicolumn{5}{c}{\\textbf{◆尿常规}} \\\\\n[BBOX-248] \\multicolumn{5}{r}{检查医生: 朱凯莉} \\\\\n[BBOX-249] \\hline\n[BBOX-250] 项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n[BBOX-251] \\hline\n[BBOX-252] 酸碱度 & 5.5 & & & 5.4-8.4 \\\\\n[BBOX-253] \\hline\n[BBOX-254] 亚硝酸盐 & - & & & 阴性 \\\\\n[BBOX-255] \\hline\n[BBOX-256] \\end{tabular}\n[BBOX-257] 越人大药房\n[BBOX-258] 祝您身体健康\n[BBOX-259] 日期：2025-04-02 NO：1.2468223\n[BBOX-260] 会员：  会员卡：1004832\n[BBOX-261] 药品名称 数量 单位 单价 金额\n[BBOX-262] 盐酸二甲双胍 0.25*60 片\n[BBOX-263] 生产厂商：上海信谊\n[BBOX-264] 批号：\n[BBOX-265] 2 5.50 11.00\n[BBOX-266] 应收：11.00 收款：11.00\n[BBOX-267] 找零：0.00 找零：0.00\n[BBOX-268] 付款方式：现金 实收：11.00\n[BBOX-269] 收款：刘丽婷 时间：11：06：25\n[BBOX-270] 地址：三全路渠东路东岸尚景\n[BBOX-271] 电话：63222645\n[BBOX-272] 药品无质量问题概不退换！\n[BBOX-273] 越人大药房\n[BBOX-274] 祝您身体健康\n[BBOX-275] 日期：2025-02-13 NO：1.2467129\n[BBOX-276] 会员：\n[BBOX-277] 会员卡：1004832\n[BBOX-278] 药品名称 数量 单位 单价 金额\n[BBOX-279] 盐酸二甲双胍 规格：0.25*60片\n[BBOX-280] 生产厂商：上海信宜\n[BBOX-281] 批号：\n[BBOX-282] 5 盒 5.50 27.50\n[BBOX-283] 应收：27.50 收款：27.50\n[BBOX-284] 找零：0.00 折扣：0.00\n[BBOX-285] 付款方式：a 现金 实收：27.50\n[BBOX-286] 收款：刘丽婷 时间：16:27:56\n[BBOX-287] 地址：三全路渠东路东岸尚景\n[BBOX-288] 电话：63222645\n[BBOX-289] 药品无质量问题概不退换！\n[BBOX-290] 郑州市金水区国基路沙门社区卫生服务中心门诊电子病历\n[BBOX-291] No: 20250417000042\n[BBOX-292] 就诊类型：初诊 科别：内科 就诊时间：2025/4/17 8:14:34\n[BBOX-293] 姓名： 性别：男 年龄：27岁 电话：13673657585\n[BBOX-294] 家庭住址：沙门 药敏史：无\n[BBOX-295] 发病日期：2025-04-17 诊断：糖尿病\n[BBOX-296] 主诉：患糖尿病1年余\n[BBOX-297] 现病史：患者1年前发现自己口渴，口干，多饮多尿，自测空腹血糖\n[BBOX-298] 11.0mmol/1，规律口服二甲双胍 每次0.5，每日三次，现来复查\n[BBOX-299] 就诊\n[BBOX-300] 既往史：否认药物过敏史，否认传染病史。\n[BBOX-301] 体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，\n[BBOX-302] 心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，\n[BBOX-303] 肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射\n[BBOX-304] 未引出。\n[BBOX-305] 辅助检查：血糖11.15mmol/1 糖化血红蛋白9%\n[BBOX-306] 初步诊断：二型糖尿病\n[BBOX-307] 处理措施：1，糖尿病饮食 保持心情愉悦 2，适量运动 3.继续规律服用 二\n[BBOX-308] 甲双胍片 4，定期检测血糖 5.不适随诊\n[BBOX-309] 医师签名：李层 打印时间：2025/4/22 17:08:28\n[BBOX-310] 健康管理部门\n[BBOX-311] 郑州市金水区国基路沙门社区\n[BBOX-312] 卫生服务中心处方笺\n[BBOX-313] 医保证号:\n[BBOX-314] 费别:自费\n[BBOX-315] 门诊号:20250417000042\n[BBOX-316] 日期:2025-04-17\n[BBOX-317] 姓名:\n[BBOX-318] 性别:男\n[BBOX-319] 年龄:27岁\n[BBOX-320] 科别:内科\n[BBOX-321] 住址:沙门\n[BBOX-322] 临床诊断:糖尿病\n[BBOX-323] Rp:\n[BBOX-324] 1 (基)(集)盐酸二甲双胍缓释片(0.5g*60S)\n[BBOX-325] 2瓶\n[BBOX-326] 用法:每次0.5g口服一天三次*30天\n[BBOX-327] 医师(签字/盖章):李层\n[BBOX-328] 审核、调配:\n[BBOX-329] 核对、发药:\n[BBOX-330] 药费:10.34\n[BBOX-331] 执行科室:西药房\n[BBOX-332] 打印日期:2025/04/17\n[BBOX-333] No 20250417000C\n[BBOX-334] 郑州市金水区国基路沙门社区\n[BBOX-335] 自费及其他\n[BBOX-336] No 20250417000062\n[BBOX-337] 2025-04-17\n[BBOX-338] 自费费用:\n[BBOX-339] 西药费\n[BBOX-340] 10.34\n[BBOX-341] 先行自付:\n[BBOX-342] 10.34\n[BBOX-343] 超限价自付:\n[BBOX-344] 医疗救助:\n[BBOX-345] 统筹记账:\n[BBOX-346] 0.00\n[BBOX-347] 大额记账:\n[BBOX-348] 0.00\n[BBOX-349] 公务员记账:\n[BBOX-350] 0.00\n[BBOX-351] 微信: 10.34\n[BBOX-352] 个人账户: 0.00\n[BBOX-353] (共济支付)\n[BBOX-354] 现金支付: 10.34\n[BBOX-355] 其他支出:\n[BBOX-356] (大病补充:\n[BBOX-357] 贫困救助:\n[BBOX-358] 政府兜底:)\n[BBOX-359] 壹拾元叁角肆分\n[BBOX-360] 10.34\n[BBOX-361] 总合计: 10.34\n[BBOX-362] 诊间结算 2025-04-17\n[BBOX-363] 诊间结算 2025-04-17\n[BBOX-364] 0\n[BBOX-365] 0.00\n[BBOX-366] 0.00\n[BBOX-367] 10.34\n[BBOX-368] 2025-0\n[BBOX-369] No 202504170000\n[BBOX-370] 郑州市金水区国基路沙门社区\n[BBOX-371] 000108\n[BBOX-372] No 2025041\n[BBOX-373] 自费及其他\n[BBOX-374] 西药房\n[BBOX-375] 内科\n[BBOX-376] 李层\n[BBOX-377] 刘权\n[BBOX-378] 西药费\n[BBOX-379] 10.34\n[BBOX-380] 壹拾元叁角肆分\n[BBOX-381] 10.34\n[BBOX-382] 0.00\n[BBOX-383] 10.34\n[BBOX-384] 2025-04-17\n[BBOX-385] \\begin{tabular}{cccccc}\n[BBOX-386] 报告时间: 2025-04-17\n[BBOX-387] \\hline\n[BBOX-388] 代码 & 项目 & 值 & 单位 & 参考值 & \\\\\n[BBOX-389] \\hline\n[BBOX-390] 2461 & 糖化血红蛋白 & 9 & \\% & 4.5$\\sim$5.9 & \\\\\n[BBOX-391] 1056 & 葡萄糖 & 11.15 & mmol/L & 3.89$\\sim$6.11 & \\\\\n[BBOX-392] \\hline\n[BBOX-393] \\end{tabular}"
  }
]
2026-08-10 07:09:37,622 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:09:37.620+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"48638ddc948a11f1bd9827cf206dfa2d": {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:09:50,001 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:09:50,028 INFO     29 [SmartSplitter] SmartSplitter done: 22 chunks from 22 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'LabReport': 13, 'ExaminationReport': 4, 'MedicationRecord': 2, 'PrescriptionRecord': 1}
2026-08-10 07:09:50,043 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 07:09:50,043 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks": "22 items, types={'OutpatientRecord': 2, 'LabReport': 13, 'ExaminationReport': 4, 'MedicationRecord': 2, 'PrescriptionRecord': 1}"}
2026-08-10 07:09:50,043 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 07:09:50,044 INFO     29 [ChunkRouter] Routed 22 chunks into 5 groups: {'chunks_Clinical': 2, 'chunks_LabExam': 13, 'chunks_Examination': 4, 'chunks_Medication': 2, 'chunks_Prescription': 1}
2026-08-10 07:09:50,063 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 07:09:50,063 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | ChunkRouter:Router | outputs={"html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks": "22 items, types={'OutpatientRecord': 2, 'LabReport': 13, 'ExaminationReport': 4, 'MedicationRecord': 2, 'PrescriptionRecord': 1}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:09:50,063 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 07:09:50,070 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:09:50,071 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:09:50,071 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[1]
2026-08-10 07:09:50,071 INFO     29 [qwen-vl-table] positions ： [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:09:50,230 INFO     29 [qwen-vl-table] page=1, rect=842x595, img=(2339x1653)
2026-08-10 07:09:50,231 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:09:50,231 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 32, \"bbox_end\": 40, \"encounter_dates\": [\"2024-11-16\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2024-11-16\n\\hline\n代码 & 项目 & 值 & 单位 & 参考值 & 代码 & 项目 & 值 & 参考 \\\\\n\\hline\n2461 & 糖化血红蛋白 & 10 & \\% & 4.5~5.9 & & & & \\\\\n1056 & 葡萄糖 & 10.60 & mmol/L & 3.89~6.11 & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:09:52,222 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:09:52,223 INFO     29 [qwen-vl-table] page=1 LLM output (len=383):
{
  "report_date": "2024-11-16",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "2461",
      "value": "10",
      "unit": "%",
      "reference_range": "4.5~5.9",
      "abnormal": true
    },
    {
      "name": "葡萄糖",
      "item_code": "1056",
      "value": "10.60",
      "unit": "mmol/L",
      "reference_range": "3.89~6.11",
      "abnormal": true
    }
  ]
}
2026-08-10 07:09:52,223 INFO     29 [qwen-vl-table] coord grouping: {1: 2}
2026-08-10 07:09:52,224 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=697777, prompt_len=517
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白、葡萄糖

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
2026-08-10 07:09:54,026 INFO     29 [qwen-vl-table] coord API raw response (len=113):
```json
[
	{"text": "糖化血红蛋白", "bbox": [126, 338, 214, 362]},
	{"text": "葡萄糖", "bbox": [126, 367, 170, 390]}
]
```
2026-08-10 07:09:54,026 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=1.8s
2026-08-10 07:09:54,026 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[126, 338, 214, 362]
2026-08-10 07:09:54,026 INFO     29 [qwen-vl-table] coord item[1]: text=葡萄糖, bbox=[126, 367, 170, 390]
2026-08-10 07:09:54,026 INFO     29 [qwen-vl-table] page=1 coord: matched 2/2, time=1.8s
2026-08-10 07:09:54,026 INFO     29 [qwen-vl-table] new_positions (2):
[[2, 106.092, 180.188, 201.10999999999999, 215.39], [2, 106.092, 143.14, 218.36499999999998, 232.04999999999998]]
2026-08-10 07:09:54,026 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=4.0s
2026-08-10 07:09:54,028 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:09:54,029 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:09:54,029 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[2]
2026-08-10 07:09:54,029 INFO     29 [qwen-vl-table] positions ： [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:09:54,221 INFO     29 [qwen-vl-table] page=2, rect=595x842, img=(1653x2339)
2026-08-10 07:09:54,222 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:09:54,222 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 66, \"bbox_end\": 84, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{|l|l|}\n\\hline\n\\multicolumn{2}{|c|}{\\textbf{乙肝五项 (免疫检测)}} \\\\\n\\hline\n\\multicolumn{2}{|r|}{检查医生: 朱凯莉} \\\\\n\\hline\n项目 & 结果 \\\\\n\\hline\n乙型肝炎病毒表面抗原 (HBsAg) & 阳性 \\\\\n\\hline\n乙型肝炎病毒表面抗体 (HBsAb) & 阴性 \\\\\n\\hline\n乙型肝炎病毒e抗原 (HBeAg) & 阴性 \\\\\n\\hline\n乙型肝炎病毒e抗体 (HBeAb) & 阳性 \\\\\n\\hline\n乙型肝炎病毒核心抗体 (HBcAb) & 阳性 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:09:57,161 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:09:57,161 INFO     29 [qwen-vl-table] page=2 LLM output (len=862):
{
  "report_date": null,
  "items": [
    {
      "name": "乙型肝炎病毒表面抗原",
      "item_code": "HBsAg",
      "value": "阳性",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "乙型肝炎病毒表面抗体",
      "item_code": "HBsAb",
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "乙型肝炎病毒e抗原",
      "item_code": "HBeAg",
      "value": "阴性",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "乙型肝炎病毒e抗体",
      "item_code": "HBeAb",
      "value": "阳性",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "乙型肝炎病毒核心抗体",
      "item_code": "HBcAb",
      "value": "阳性",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    }
  ]
}
2026-08-10 07:09:57,161 INFO     29 [qwen-vl-table] coord grouping: {2: 5}
2026-08-10 07:09:57,167 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1093662, prompt_len=559
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
乙型肝炎病毒表面抗原、乙型肝炎病毒表面抗体、乙型肝炎病毒e抗原、乙型肝炎病毒e抗体、乙型肝炎病毒核心抗体

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
2026-08-10 07:10:00,014 INFO     29 [qwen-vl-table] coord API raw response (len=287):
```json
[
	{"text": "乙型肝炎病毒表面抗原", "bbox": [228, 557, 400, 570]},
	{"text": "乙型肝炎病毒表面抗体", "bbox": [228, 582, 400, 595]},
	{"text": "乙型肝炎病毒e抗原", "bbox": [228, 607, 388, 620]},
	{"text": "乙型肝炎病毒e抗体", "bbox": [228, 632, 388, 645]},
	{"text": "乙型肝炎病毒核心抗体", "bbox": [228, 657, 400, 670]}
]
```
2026-08-10 07:10:00,014 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=2.8s
2026-08-10 07:10:00,014 INFO     29 [qwen-vl-table] coord item[0]: text=乙型肝炎病毒表面抗原, bbox=[228, 557, 400, 570]
2026-08-10 07:10:00,014 INFO     29 [qwen-vl-table] coord item[1]: text=乙型肝炎病毒表面抗体, bbox=[228, 582, 400, 595]
2026-08-10 07:10:00,014 INFO     29 [qwen-vl-table] coord item[2]: text=乙型肝炎病毒e抗原, bbox=[228, 607, 388, 620]
2026-08-10 07:10:00,014 INFO     29 [qwen-vl-table] coord item[3]: text=乙型肝炎病毒e抗体, bbox=[228, 632, 388, 645]
2026-08-10 07:10:00,014 INFO     29 [qwen-vl-table] coord item[4]: text=乙型肝炎病毒核心抗体, bbox=[228, 657, 400, 670]
2026-08-10 07:10:00,015 INFO     29 [qwen-vl-table] page=2 coord: matched 5/5, time=2.8s
2026-08-10 07:10:00,015 INFO     29 [qwen-vl-table] new_positions (5):
[[3, 135.66, 238.0, 468.99399999999997, 479.94], [3, 135.66, 238.0, 490.044, 500.99], [3, 135.66, 230.85999999999999, 511.094, 522.04], [3, 135.66, 230.85999999999999, 532.144, 543.09], [3, 135.66, 238.0, 553.194, 564.14]]
2026-08-10 07:10:00,015 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=5, matched=5, pages=1, time=6.0s
2026-08-10 07:10:00,017 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:00,020 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:00,021 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 07:10:00,021 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:00,226 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 07:10:00,227 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:00,227 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 85, \"bbox_end\": 93, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c c}\n\\hline\n\\multicolumn{2}{l}{\\textbf{金水区国基路沙门社区卫生服务中心}} & \\multicolumn{2}{l}{\\textbf{姓名:}} & \\multicolumn{2}{l}{\\textbf{条码号: 1001241021000001}} \\\\\n\\multicolumn{2}{l}{\\textbf{Jinshui Guoji Road Sha Men Community Services Center}} & \\multicolumn{2}{l}{} & \\multicolumn{2}{l}{} \\\\\n\\hline\n\\multicolumn{2}{l}{红细胞平均分布宽度标准差} & 42.6 & fL & & 35.0-56.0 \\\\\n\\multicolumn{2}{l}{红细胞平均分布宽度变异系数} & 11.6 & \\% & & 11.0-16.0 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:01,974 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:01,974 INFO     29 [qwen-vl-table] page=3 LLM output (len=388):
{
  "report_date": null,
  "items": [
    {
      "name": "红细胞平均分布宽度标准差",
      "item_code": null,
      "value": "42.6",
      "unit": "fL",
      "reference_range": "35.0-56.0",
      "abnormal": false
    },
    {
      "name": "红细胞平均分布宽度变异系数",
      "item_code": null,
      "value": "11.6",
      "unit": "%",
      "reference_range": "11.0-16.0",
      "abnormal": false
    }
  ]
}
2026-08-10 07:10:01,975 INFO     29 [qwen-vl-table] coord grouping: {3: 2}
2026-08-10 07:10:01,977 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038347, prompt_len=533
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
红细胞平均分布宽度标准差、红细胞平均分布宽度变异系数

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
2026-08-10 07:10:03,949 INFO     29 [qwen-vl-table] coord API raw response (len=129):
```json
[
	{"text": "红细胞平均分布宽度标准差", "bbox": [264, 147, 405, 159]},
	{"text": "红细胞平均分布宽度变异系数", "bbox": [264, 169, 416, 181]}
]
```
2026-08-10 07:10:03,950 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=2.0s
2026-08-10 07:10:03,950 INFO     29 [qwen-vl-table] coord item[0]: text=红细胞平均分布宽度标准差, bbox=[264, 147, 405, 159]
2026-08-10 07:10:03,950 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞平均分布宽度变异系数, bbox=[264, 169, 416, 181]
2026-08-10 07:10:03,950 INFO     29 [qwen-vl-table] page=3 coord: matched 2/2, time=2.0s
2026-08-10 07:10:03,951 INFO     29 [qwen-vl-table] new_positions (2):
[[4, 157.07999999999998, 240.975, 123.774, 133.878], [4, 157.07999999999998, 247.51999999999998, 142.298, 152.402]]
2026-08-10 07:10:03,951 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=3.9s
2026-08-10 07:10:03,952 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:03,954 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:03,954 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 07:10:03,954 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:04,125 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 07:10:04,126 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:04,126 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 94, \"bbox_end\": 102, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{5}{l}{\\textbf{◆空腹血糖 (生化检验) \\quad 检查医生: 朱凯莉}} \\\\\n\\hline\n项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n\\hline\n空腹血糖 & 16.93 $\\uparrow$ & mmol/L & 偏高 & 3.89-6.11 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:05,306 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:05,307 INFO     29 [qwen-vl-table] page=3 LLM output (len=211):
{
  "report_date": null,
  "items": [
    {
      "name": "空腹血糖",
      "item_code": null,
      "value": "16.93",
      "unit": "mmol/L",
      "reference_range": "3.89-6.11",
      "abnormal": true
    }
  ]
}
2026-08-10 07:10:05,307 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 07:10:05,310 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038347, prompt_len=511
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
空腹血糖

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
2026-08-10 07:10:05,982 INFO     29 [qwen-vl-table] coord API raw response (len=63):
```json
[
	{"text": "空腹血糖", "bbox": [265, 222, 331, 236]}
]
```
2026-08-10 07:10:05,983 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 07:10:05,983 INFO     29 [qwen-vl-table] coord item[0]: text=空腹血糖, bbox=[265, 222, 331, 236]
2026-08-10 07:10:05,983 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=0.7s
2026-08-10 07:10:05,983 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 157.67499999999998, 196.945, 186.924, 198.712]]
2026-08-10 07:10:05,983 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.0s
2026-08-10 07:10:05,984 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:05,985 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:05,985 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 07:10:05,985 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:06,162 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 07:10:06,162 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:06,162 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 103, \"bbox_end\": 113, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{5}{l}{\\textbf{◆肾功能 3 项 (生化检验) \\quad 检查医生: 朱凯莉}} \\\\\n\\hline\n项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n\\hline\n尿酸 & 254.9 & $\\mu$mol/L & & 202-416 \\\\\n肌酐 & 57.0 & $\\mu$mol/L & & 57-97 \\\\\n尿素 & 3.29 $\\downarrow$ & mmol/L & 偏低 & 3.6-9.5 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:07,708 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:10:07.706+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"48638ddc948a11f1bd9827cf206dfa2d": {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:10:08,291 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:08,292 INFO     29 [qwen-vl-table] page=3 LLM output (len=535):
{
  "report_date": null,
  "items": [
    {
      "name": "尿酸",
      "item_code": null,
      "value": "254.9",
      "unit": "μmol/L",
      "reference_range": "202-416",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": null,
      "value": "57.0",
      "unit": "μmol/L",
      "reference_range": "57-97",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": null,
      "value": "3.29",
      "unit": "mmol/L",
      "reference_range": "3.6-9.5",
      "abnormal": true
    }
  ]
}
2026-08-10 07:10:08,292 INFO     29 [qwen-vl-table] coord grouping: {3: 3}
2026-08-10 07:10:08,295 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038347, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
尿酸、肌酐、尿素

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
2026-08-10 07:10:09,427 INFO     29 [qwen-vl-table] coord API raw response (len=155):
```json
[
	{"text": "尿酸", "bbox": [266, 367, 292, 379]},
	{"text": "肌酐", "bbox": [266, 389, 292, 401]},
	{"text": "尿素", "bbox": [266, 410, 292, 422]}
]
```
2026-08-10 07:10:09,428 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=1.1s
2026-08-10 07:10:09,428 INFO     29 [qwen-vl-table] coord item[0]: text=尿酸, bbox=[266, 367, 292, 379]
2026-08-10 07:10:09,428 INFO     29 [qwen-vl-table] coord item[1]: text=肌酐, bbox=[266, 389, 292, 401]
2026-08-10 07:10:09,428 INFO     29 [qwen-vl-table] coord item[2]: text=尿素, bbox=[266, 410, 292, 422]
2026-08-10 07:10:09,428 INFO     29 [qwen-vl-table] page=3 coord: matched 3/3, time=1.1s
2026-08-10 07:10:09,428 INFO     29 [qwen-vl-table] new_positions (3):
[[4, 158.26999999999998, 173.73999999999998, 309.014, 319.118], [4, 158.26999999999998, 173.73999999999998, 327.538, 337.642], [4, 158.26999999999998, 173.73999999999998, 345.21999999999997, 355.324]]
2026-08-10 07:10:09,428 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=3.4s
2026-08-10 07:10:09,429 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:09,430 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:09,430 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 07:10:09,430 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:09,599 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 07:10:09,600 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:09,600 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 114, \"bbox_end\": 128, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{5}{l}{\\textbf{◆肝功七项 (生化检验) \\quad 检查医生: 朱凯莉}} \\\\\n\\hline\n项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n\\hline\n丙氨酸氨基转移酶 & 43.7 & U/L & & 9-50 \\\\\n门冬氨酸氨基转移酶 & 20.5 & U/L & & 0-40 \\\\\n谷氨酰转肽酶 & 53.5 & U/L & & 11-61 \\\\\n总蛋白 & 78.7 & g/L & & 66-87 \\\\\n白蛋白 & 44.4 & g/L & & 40-55 \\\\\n总胆红素 & 10.4 & $\\mu$mol/L & & 5.1-19 \\\\\n直接胆红素 & 2.6 & $\\mu$mol/L & & 1.7-6.8 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:13,677 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:13,677 INFO     29 [qwen-vl-table] page=3 LLM output (len=1192):
{
  "report_date": null,
  "items": [
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": null,
      "value": "43.7",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "门冬氨酸氨基转移酶",
      "item_code": null,
      "value": "20.5",
      "unit": "U/L",
      "reference_range": "0-40",
      "abnormal": false
    },
    {
      "name": "谷氨酰转肽酶",
      "item_code": null,
      "value": "53.5",
      "unit": "U/L",
      "reference_range": "11-61",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": null,
      "value": "78.7",
      "unit": "g/L",
      "reference_range": "66-87",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": null,
      "value": "44.4",
      "unit": "g/L",
      "reference_range": "40-55",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": null,
      "value": "10.4",
      "unit": "μmol/L",
      "reference_range": "5.1-19",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": null,
      "value": "2.6",
      "unit": "μmol/L",
      "reference_range": "1.7-6.8",
      "abnormal": false
    }
  ]
}
2026-08-10 07:10:13,677 INFO     29 [qwen-vl-table] coord grouping: {3: 7}
2026-08-10 07:10:13,680 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038347, prompt_len=551
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
丙氨酸氨基转移酶、门冬氨酸氨基转移酶、谷氨酰转肽酶、总蛋白、白蛋白、总胆红素、直接胆红素

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
2026-08-10 07:10:15,928 INFO     29 [qwen-vl-table] coord API raw response (len=367):
```json
[
	{"text": "丙氨酸氨基转移酶", "bbox": [267, 508, 361, 519]},
	{"text": "门冬氨酸氨基转移酶", "bbox": [267, 529, 372, 540]},
	{"text": "谷氨酰转肽酶", "bbox": [267, 551, 338, 562]},
	{"text": "总蛋白", "bbox": [267, 573, 303, 584]},
	{"text": "白蛋白", "bbox": [267, 595, 303, 606]},
	{"text": "总胆红素", "bbox": [267, 617, 314, 628]},
	{"text": "直接胆红素", "bbox": [267, 638, 325, 649]}
]
```
2026-08-10 07:10:15,928 INFO     29 [qwen-vl-table] coord API: raw_items=7, valid_items=7, elapsed=2.2s
2026-08-10 07:10:15,928 INFO     29 [qwen-vl-table] coord item[0]: text=丙氨酸氨基转移酶, bbox=[267, 508, 361, 519]
2026-08-10 07:10:15,928 INFO     29 [qwen-vl-table] coord item[1]: text=门冬氨酸氨基转移酶, bbox=[267, 529, 372, 540]
2026-08-10 07:10:15,928 INFO     29 [qwen-vl-table] coord item[2]: text=谷氨酰转肽酶, bbox=[267, 551, 338, 562]
2026-08-10 07:10:15,928 INFO     29 [qwen-vl-table] coord item[3]: text=总蛋白, bbox=[267, 573, 303, 584]
2026-08-10 07:10:15,928 INFO     29 [qwen-vl-table] coord item[4]: text=白蛋白, bbox=[267, 595, 303, 606]
2026-08-10 07:10:15,929 INFO     29 [qwen-vl-table] coord item[5]: text=总胆红素, bbox=[267, 617, 314, 628]
2026-08-10 07:10:15,929 INFO     29 [qwen-vl-table] coord item[6]: text=直接胆红素, bbox=[267, 638, 325, 649]
2026-08-10 07:10:15,929 INFO     29 [qwen-vl-table] page=3 coord: matched 7/7, time=2.2s
2026-08-10 07:10:15,929 INFO     29 [qwen-vl-table] new_positions (7):
[[4, 158.86499999999998, 214.795, 427.736, 436.998], [4, 158.86499999999998, 221.34, 445.418, 454.68], [4, 158.86499999999998, 201.10999999999999, 463.942, 473.204], [4, 158.86499999999998, 180.285, 482.466, 491.728], [4, 158.86499999999998, 180.285, 500.99, 510.252], [4, 158.86499999999998, 186.82999999999998, 519.514, 528.776], [4, 158.86499999999998, 193.375, 537.196, 546.458]]
2026-08-10 07:10:15,929 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=7, matched=7, pages=1, time=6.5s
2026-08-10 07:10:15,930 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:15,931 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:15,931 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 07:10:15,931 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:16,111 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 07:10:16,111 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:16,111 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 129, \"bbox_end\": 138, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{5}{l}{\\textbf{◆尿常规 \\quad 检查医生: 朱凯莉}} \\\\\n\\hline\n项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n\\hline\n酸碱度 & 5.5 & & & 5.4-8.4 \\\\\n亚硝酸盐 & - & & & 阴性 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:17,612 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:17,612 INFO     29 [qwen-vl-table] page=3 LLM output (len=358):
{
  "report_date": null,
  "items": [
    {
      "name": "酸碱度",
      "item_code": null,
      "value": "5.5",
      "unit": null,
      "reference_range": "5.4-8.4",
      "abnormal": false
    },
    {
      "name": "亚硝酸盐",
      "item_code": null,
      "value": "-",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    }
  ]
}
2026-08-10 07:10:17,612 INFO     29 [qwen-vl-table] coord grouping: {3: 2}
2026-08-10 07:10:17,618 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038347, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
酸碱度、亚硝酸盐

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
2026-08-10 07:10:18,568 INFO     29 [qwen-vl-table] coord API raw response (len=111):
```json
[
	{"text": "酸碱度", "bbox": [268, 737, 302, 749]},
	{"text": "亚硝酸盐", "bbox": [268, 760, 314, 771]}
]
```
2026-08-10 07:10:18,569 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=0.9s
2026-08-10 07:10:18,569 INFO     29 [qwen-vl-table] coord item[0]: text=酸碱度, bbox=[268, 737, 302, 749]
2026-08-10 07:10:18,569 INFO     29 [qwen-vl-table] coord item[1]: text=亚硝酸盐, bbox=[268, 760, 314, 771]
2026-08-10 07:10:18,569 INFO     29 [qwen-vl-table] page=3 coord: matched 2/2, time=0.9s
2026-08-10 07:10:18,569 INFO     29 [qwen-vl-table] new_positions (2):
[[4, 159.45999999999998, 179.69, 620.554, 630.658], [4, 159.45999999999998, 186.82999999999998, 639.92, 649.182]]
2026-08-10 07:10:18,569 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=2.6s
2026-08-10 07:10:18,571 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:18,574 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:18,574 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 07:10:18,574 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:18,756 INFO     29 [qwen-vl-table] page=5, rect=595x842, img=(1653x2339)
2026-08-10 07:10:18,757 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:18,757 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 192, \"bbox_end\": 198, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{2}{l}{\\textbf{红细胞平均分布宽度标准差}} & 42.6 & fL & 35.0-56.0 \\\\\n\\hline\n\\multicolumn{2}{l}{\\textbf{红细胞平均分布宽度变异系数}} & 11.6 & \\% & 11.0-16.0 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:20,444 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:20,444 INFO     29 [qwen-vl-table] page=5 LLM output (len=388):
{
  "report_date": null,
  "items": [
    {
      "name": "红细胞平均分布宽度标准差",
      "item_code": null,
      "value": "42.6",
      "unit": "fL",
      "reference_range": "35.0-56.0",
      "abnormal": false
    },
    {
      "name": "红细胞平均分布宽度变异系数",
      "item_code": null,
      "value": "11.6",
      "unit": "%",
      "reference_range": "11.0-16.0",
      "abnormal": false
    }
  ]
}
2026-08-10 07:10:20,444 INFO     29 [qwen-vl-table] coord grouping: {5: 2}
2026-08-10 07:10:20,447 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038656, prompt_len=533
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
红细胞平均分布宽度标准差、红细胞平均分布宽度变异系数

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
2026-08-10 07:10:22,265 INFO     29 [qwen-vl-table] coord API raw response (len=129):
```json
[
	{"text": "红细胞平均分布宽度标准差", "bbox": [264, 147, 405, 159]},
	{"text": "红细胞平均分布宽度变异系数", "bbox": [264, 169, 416, 181]}
]
```
2026-08-10 07:10:22,265 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=1.8s
2026-08-10 07:10:22,266 INFO     29 [qwen-vl-table] coord item[0]: text=红细胞平均分布宽度标准差, bbox=[264, 147, 405, 159]
2026-08-10 07:10:22,266 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞平均分布宽度变异系数, bbox=[264, 169, 416, 181]
2026-08-10 07:10:22,266 INFO     29 [qwen-vl-table] page=5 coord: matched 2/2, time=1.8s
2026-08-10 07:10:22,266 INFO     29 [qwen-vl-table] new_positions (2):
[[6, 157.07999999999998, 240.975, 123.774, 133.878], [6, 157.07999999999998, 247.51999999999998, 142.298, 152.402]]
2026-08-10 07:10:22,267 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=3.7s
2026-08-10 07:10:22,269 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:22,272 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:22,272 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 07:10:22,273 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:22,527 INFO     29 [qwen-vl-table] page=5, rect=595x842, img=(1653x2339)
2026-08-10 07:10:22,527 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:22,528 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 199, \"bbox_end\": 208, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{5}{c}{\\textbf{◆空腹血糖 (生化检验)}} \\\\\n\\multicolumn{5}{r}{检查医生: 朱凯莉} \\\\\n\\hline\n项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n\\hline\n空腹血糖 & 16.93 $\\uparrow$ & mmol/L & 偏高 & 3.89-6.11 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:23,685 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:23,686 INFO     29 [qwen-vl-table] page=5 LLM output (len=211):
{
  "report_date": null,
  "items": [
    {
      "name": "空腹血糖",
      "item_code": null,
      "value": "16.93",
      "unit": "mmol/L",
      "reference_range": "3.89-6.11",
      "abnormal": true
    }
  ]
}
2026-08-10 07:10:23,686 INFO     29 [qwen-vl-table] coord grouping: {5: 1}
2026-08-10 07:10:23,688 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038656, prompt_len=511
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
空腹血糖

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
2026-08-10 07:10:24,365 INFO     29 [qwen-vl-table] coord API raw response (len=63):
```json
[
	{"text": "空腹血糖", "bbox": [265, 222, 331, 236]}
]
```
2026-08-10 07:10:24,365 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 07:10:24,365 INFO     29 [qwen-vl-table] coord item[0]: text=空腹血糖, bbox=[265, 222, 331, 236]
2026-08-10 07:10:24,365 INFO     29 [qwen-vl-table] page=5 coord: matched 1/1, time=0.7s
2026-08-10 07:10:24,365 INFO     29 [qwen-vl-table] new_positions (1):
[[6, 157.67499999999998, 196.945, 186.924, 198.712]]
2026-08-10 07:10:24,365 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.1s
2026-08-10 07:10:24,367 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:24,368 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:24,369 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 07:10:24,369 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:24,549 INFO     29 [qwen-vl-table] page=5, rect=595x842, img=(1653x2339)
2026-08-10 07:10:24,549 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:24,549 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 209, \"bbox_end\": 222, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{5}{c}{\\textbf{◆肾功能 3 项 (生化检验)}} \\\\\n\\multicolumn{5}{r}{检查医生: 朱凯莉} \\\\\n\\hline\n项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n\\hline\n尿酸 & 254.9 & $\\mu$mol/L & & 202-416 \\\\\n\\hline\n肌酐 & 57.0 & $\\mu$mol/L & & 57-97 \\\\\n\\hline\n尿素 & 3.29 $\\downarrow$ & mmol/L & 偏低 & 3.6-9.5 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:26,648 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:26,648 INFO     29 [qwen-vl-table] page=5 LLM output (len=535):
{
  "report_date": null,
  "items": [
    {
      "name": "尿酸",
      "item_code": null,
      "value": "254.9",
      "unit": "μmol/L",
      "reference_range": "202-416",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": null,
      "value": "57.0",
      "unit": "μmol/L",
      "reference_range": "57-97",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": null,
      "value": "3.29",
      "unit": "mmol/L",
      "reference_range": "3.6-9.5",
      "abnormal": true
    }
  ]
}
2026-08-10 07:10:26,649 INFO     29 [qwen-vl-table] coord grouping: {5: 3}
2026-08-10 07:10:26,653 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038656, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
尿酸、肌酐、尿素

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
2026-08-10 07:10:27,821 INFO     29 [qwen-vl-table] coord API raw response (len=155):
```json
[
	{"text": "尿酸", "bbox": [266, 367, 292, 378]},
	{"text": "肌酐", "bbox": [266, 390, 292, 400]},
	{"text": "尿素", "bbox": [266, 411, 292, 421]}
]
```
2026-08-10 07:10:27,821 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=1.2s
2026-08-10 07:10:27,822 INFO     29 [qwen-vl-table] coord item[0]: text=尿酸, bbox=[266, 367, 292, 378]
2026-08-10 07:10:27,822 INFO     29 [qwen-vl-table] coord item[1]: text=肌酐, bbox=[266, 390, 292, 400]
2026-08-10 07:10:27,822 INFO     29 [qwen-vl-table] coord item[2]: text=尿素, bbox=[266, 411, 292, 421]
2026-08-10 07:10:27,822 INFO     29 [qwen-vl-table] page=5 coord: matched 3/3, time=1.2s
2026-08-10 07:10:27,822 INFO     29 [qwen-vl-table] new_positions (3):
[[6, 158.26999999999998, 173.73999999999998, 309.014, 318.276], [6, 158.26999999999998, 173.73999999999998, 328.38, 336.8], [6, 158.26999999999998, 173.73999999999998, 346.062, 354.48199999999997]]
2026-08-10 07:10:27,822 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=3.5s
2026-08-10 07:10:27,824 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:27,826 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:27,826 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 07:10:27,826 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:27,999 INFO     29 [qwen-vl-table] page=5, rect=595x842, img=(1653x2339)
2026-08-10 07:10:28,000 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:28,000 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 223, \"bbox_end\": 244, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{5}{c}{\\textbf{◆肝功七项 (生化检验)}} \\\\\n\\multicolumn{5}{r}{检查医生: 朱凯莉} \\\\\n\\hline\n项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n\\hline\n丙氨酸氨基转移酶 & 43.7 & U/L & & 9-50 \\\\\n\\hline\n门冬氨酸氨基转移酶 & 20.5 & U/L & & 0-40 \\\\\n\\hline\n谷氨酰转肽酶 & 53.5 & U/L & & 11-61 \\\\\n\\hline\n总蛋白 & 78.7 & g/L & & 66-87 \\\\\n\\hline\n白蛋白 & 44.4 & g/L & & 40-55 \\\\\n\\hline\n总胆红素 & 10.4 & $\\mu$mol/L & & 5.1-19 \\\\\n\\hline\n直接胆红素 & 2.6 & $\\mu$mol/L & & 1.7-6.8 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:32,042 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:32,042 INFO     29 [qwen-vl-table] page=5 LLM output (len=1192):
{
  "report_date": null,
  "items": [
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": null,
      "value": "43.7",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "门冬氨酸氨基转移酶",
      "item_code": null,
      "value": "20.5",
      "unit": "U/L",
      "reference_range": "0-40",
      "abnormal": false
    },
    {
      "name": "谷氨酰转肽酶",
      "item_code": null,
      "value": "53.5",
      "unit": "U/L",
      "reference_range": "11-61",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": null,
      "value": "78.7",
      "unit": "g/L",
      "reference_range": "66-87",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": null,
      "value": "44.4",
      "unit": "g/L",
      "reference_range": "40-55",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": null,
      "value": "10.4",
      "unit": "μmol/L",
      "reference_range": "5.1-19",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": null,
      "value": "2.6",
      "unit": "μmol/L",
      "reference_range": "1.7-6.8",
      "abnormal": false
    }
  ]
}
2026-08-10 07:10:32,043 INFO     29 [qwen-vl-table] coord grouping: {5: 7}
2026-08-10 07:10:32,047 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038656, prompt_len=551
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
丙氨酸氨基转移酶、门冬氨酸氨基转移酶、谷氨酰转肽酶、总蛋白、白蛋白、总胆红素、直接胆红素

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
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord API raw response (len=367):
```json
[
	{"text": "丙氨酸氨基转移酶", "bbox": [267, 508, 361, 519]},
	{"text": "门冬氨酸氨基转移酶", "bbox": [267, 530, 372, 540]},
	{"text": "谷氨酰转肽酶", "bbox": [267, 552, 338, 562]},
	{"text": "总蛋白", "bbox": [267, 574, 303, 584]},
	{"text": "白蛋白", "bbox": [267, 596, 303, 606]},
	{"text": "总胆红素", "bbox": [267, 618, 314, 628]},
	{"text": "直接胆红素", "bbox": [267, 639, 325, 649]}
]
```
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord API: raw_items=7, valid_items=7, elapsed=2.1s
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord item[0]: text=丙氨酸氨基转移酶, bbox=[267, 508, 361, 519]
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord item[1]: text=门冬氨酸氨基转移酶, bbox=[267, 530, 372, 540]
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord item[2]: text=谷氨酰转肽酶, bbox=[267, 552, 338, 562]
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord item[3]: text=总蛋白, bbox=[267, 574, 303, 584]
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord item[4]: text=白蛋白, bbox=[267, 596, 303, 606]
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord item[5]: text=总胆红素, bbox=[267, 618, 314, 628]
2026-08-10 07:10:34,190 INFO     29 [qwen-vl-table] coord item[6]: text=直接胆红素, bbox=[267, 639, 325, 649]
2026-08-10 07:10:34,191 INFO     29 [qwen-vl-table] page=5 coord: matched 7/7, time=2.1s
2026-08-10 07:10:34,191 INFO     29 [qwen-vl-table] new_positions (7):
[[6, 158.86499999999998, 214.795, 427.736, 436.998], [6, 158.86499999999998, 221.34, 446.26, 454.68], [6, 158.86499999999998, 201.10999999999999, 464.784, 473.204], [6, 158.86499999999998, 180.285, 483.308, 491.728], [6, 158.86499999999998, 180.285, 501.832, 510.252], [6, 158.86499999999998, 186.82999999999998, 520.356, 528.776], [6, 158.86499999999998, 193.375, 538.038, 546.458]]
2026-08-10 07:10:34,191 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=7, matched=7, pages=1, time=6.4s
2026-08-10 07:10:34,192 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:34,193 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:34,193 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 07:10:34,193 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:34,369 INFO     29 [qwen-vl-table] page=5, rect=595x842, img=(1653x2339)
2026-08-10 07:10:34,370 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:34,370 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 245, \"bbox_end\": 256, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n\\hline\n\\multicolumn{5}{c}{\\textbf{◆尿常规}} \\\\\n\\multicolumn{5}{r}{检查医生: 朱凯莉} \\\\\n\\hline\n项目 & 结果 & 单位 & 异常描述 & 正常参考值 \\\\\n\\hline\n酸碱度 & 5.5 & & & 5.4-8.4 \\\\\n\\hline\n亚硝酸盐 & - & & & 阴性 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:35,812 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:35,812 INFO     29 [qwen-vl-table] page=5 LLM output (len=358):
{
  "report_date": null,
  "items": [
    {
      "name": "酸碱度",
      "item_code": null,
      "value": "5.5",
      "unit": null,
      "reference_range": "5.4-8.4",
      "abnormal": false
    },
    {
      "name": "亚硝酸盐",
      "item_code": null,
      "value": "-",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    }
  ]
}
2026-08-10 07:10:35,812 INFO     29 [qwen-vl-table] coord grouping: {5: 2}
2026-08-10 07:10:35,815 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1038656, prompt_len=515
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
酸碱度、亚硝酸盐

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
2026-08-10 07:10:36,753 INFO     29 [qwen-vl-table] coord API raw response (len=111):
```json
[
	{"text": "酸碱度", "bbox": [268, 737, 302, 749]},
	{"text": "亚硝酸盐", "bbox": [268, 760, 314, 771]}
]
```
2026-08-10 07:10:36,754 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=0.9s
2026-08-10 07:10:36,754 INFO     29 [qwen-vl-table] coord item[0]: text=酸碱度, bbox=[268, 737, 302, 749]
2026-08-10 07:10:36,754 INFO     29 [qwen-vl-table] coord item[1]: text=亚硝酸盐, bbox=[268, 760, 314, 771]
2026-08-10 07:10:36,754 INFO     29 [qwen-vl-table] page=5 coord: matched 2/2, time=0.9s
2026-08-10 07:10:36,755 INFO     29 [qwen-vl-table] new_positions (2):
[[6, 159.45999999999998, 179.69, 620.554, 630.658], [6, 159.45999999999998, 186.82999999999998, 639.92, 649.182]]
2026-08-10 07:10:36,755 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=2.6s
2026-08-10 07:10:36,756 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:36,758 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:36,759 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[11]
2026-08-10 07:10:36,759 INFO     29 [qwen-vl-table] positions ： [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:36,968 INFO     29 [qwen-vl-table] page=11, rect=842x595, img=(2339x1653)
2026-08-10 07:10:36,968 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:36,968 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 385, \"bbox_end\": 393, \"encounter_dates\": [\"2025-04-17\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2025-04-17\n\\hline\n代码 & 项目 & 值 & 单位 & 参考值 & \\\\\n\\hline\n2461 & 糖化血红蛋白 & 9 & \\% & 4.5$\\sim$5.9 & \\\\\n1056 & 葡萄糖 & 11.15 & mmol/L & 3.89$\\sim$6.11 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 07:10:37,669 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:10:37.668+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"48638ddc948a11f1bd9827cf206dfa2d": {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:10:38,667 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:38,667 INFO     29 [qwen-vl-table] page=11 LLM output (len=378):
{
  "report_date": "2025-04-17",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": null,
      "value": "9",
      "unit": "%",
      "reference_range": "4.5~5.9",
      "abnormal": true
    },
    {
      "name": "葡萄糖",
      "item_code": null,
      "value": "11.15",
      "unit": "mmol/L",
      "reference_range": "3.89~6.11",
      "abnormal": true
    }
  ]
}
2026-08-10 07:10:38,667 INFO     29 [qwen-vl-table] coord grouping: {11: 2}
2026-08-10 07:10:38,669 INFO     29 [qwen-vl-table] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1027959, prompt_len=517
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白、葡萄糖

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
2026-08-10 07:10:40,564 INFO     29 [qwen-vl-table] coord API raw response (len=113):
```json
[
	{"text": "糖化血红蛋白", "bbox": [122, 361, 199, 381]},
	{"text": "葡萄糖", "bbox": [122, 388, 161, 407]}
]
```
2026-08-10 07:10:40,564 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=1.9s
2026-08-10 07:10:40,564 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[122, 361, 199, 381]
2026-08-10 07:10:40,564 INFO     29 [qwen-vl-table] coord item[1]: text=葡萄糖, bbox=[122, 388, 161, 407]
2026-08-10 07:10:40,565 INFO     29 [qwen-vl-table] page=11 coord: matched 2/2, time=1.9s
2026-08-10 07:10:40,565 INFO     29 [qwen-vl-table] new_positions (2):
[[12, 102.72399999999999, 167.558, 214.795, 226.695], [12, 102.72399999999999, 135.56199999999998, 230.85999999999999, 242.165]]
2026-08-10 07:10:40,565 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=3.8s
2026-08-10 07:10:40,579 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 07:10:40,580 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Extractor:LabExam | outputs={"chunks": "13 items, types={'LabReport': 13}", "html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:10:40,580 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 07:10:40,591 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:40,591 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 07:10:41,861 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:41,870 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 07:10:41,870 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:10:41,870 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 07:10:41,881 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:41,882 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:41,882 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 07:10:41,882 INFO     29 [qwen-vl-text] positions(27): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:41,882 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [27]
2026-08-10 07:10:42,137 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:10:42,139 INFO     29 [qwen-vl-text] LLM extraction start, text_len=449
2026-08-10 07:10:42,139 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:42,139 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 26, \"encounter_dates\": [\"2024-11-16\"], \"department\": \"内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "郑州市金水区国基路沙门社区卫生服务中心门诊电子病历\nNo: 20241116000027\n就诊类型：初诊\n科别：内科\n就诊时间：2024/11/16 8:09:23\n姓名：.\n性别：男\n年龄：27岁\n电话：\n家庭住址：沙门\n药敏史：无\n发病日期：\n诊断：2型糖尿病\n主诉：发现口渴.口干.多饮多尿.3个月余.\n现病史：患者三个月前发现自己口渴.口干.多饮多尿自测空腹血糖\n11.0mmol/L.规律口服二甲双胍每次0.5g每日三次 血糖控\n制不理想.前来就诊\n既往史：否认药物过敏史，否认传染病史。\n体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，\n心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，\n肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射\n未引出。\n辅助检查：血糖10.6mmol/L. 糖化10%\n初步诊断：二型糖尿病\n处理措施：1.糖尿病饮食.2.适当运动.3.规律服用二甲双胍 4.定期复查\n医师签名：李层\n打印时间：2025/3/19 17:04:36",
    "role": "user"
  }
]
2026-08-10 07:10:43,987 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:43,988 INFO     29 [qwen-vl-text] LLM output (len=289):
{
  "encounter_date": "2024-11-16",
  "chief_complaint": "发现口渴.口干.多饮多尿.3个月余.",
  "present_illness": "患者三个月前发现自己口渴.口干.多饮多尿自测空腹血糖11.0mmol/L.规律口服二甲双胍每次0.5g每日三次 血糖控制不理想.前来就诊",
  "past_history": "否认药物过敏史，否认传染病史。",
  "diagnosis": "二型糖尿病",
  "treatment_plan": "1.糖尿病饮食.2.适当运动.3.规律服用二甲双胍 4.定期复查"
}
2026-08-10 07:10:43,988 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-11-16]
2026-08-10 07:10:43,990 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1172933, prompt_len=1143
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["郑州市金水区国基路沙门社区卫生服务中心门诊电子病历", "No: 20241116000027", "就诊类型：初诊", "科别：内科", "就诊时间：2024/11/16 8:09:23", "姓名：.", "性别：男", "年龄：27岁", "电话：", "家庭住址：沙门", "药敏史：无", "发病日期：", "诊断：2型糖尿病", "主诉：发现口渴.口干.多饮多尿.3个月余.", "现病史：患者三个月前发现自己口渴.口干.多饮多尿自测空腹血糖", "11.0mmol/L.规律口服二甲双胍每次0.5g每日三次 血糖控", "制不理想.前来就诊", "既往史：否认药物过敏史，否认传染病史。", "体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，", "心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，", "肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射", "未引出。", "辅助检查：血糖10.6mmol/L. 糖化10%", "初步诊断：二型糖尿病", "处理措施：1.糖尿病饮食.2.适当运动.3.规律服用二甲双胍 4.定期复查", "医师签名：李层", "打印时间：2025/3/19 17:04:36"]

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
2026-08-10 07:10:57,791 INFO     29 [qwen-vl-text] coord API raw response (len=2358):
[
	{"text": "郑州市金水区国基路沙门社区卫生服务中心门诊电子病历", "bbox": [121, 67, 767, 88]},
	{"text": "No: 20241116000027", "bbox": [594, 94, 831, 111]},
	{"text": "就诊类型：初诊", "bbox": [3, 117, 190, 139], "bbox": [3, 117, 190, 139]},
	{"text": "科别：内科", "bbox": [269, 117, 396, 139], "bbox": [269, 117, 396, 139]},
	{"text": "就诊时间：2024/11/16 8:09:23", "bbox": [543, 117, 886, 139], "bbox": [543, 117, 886, 139]},
	{"text": "姓名：.", "bbox": [3, 147, 100, 168], "bbox": [3, 147, 100, 168]},
	{"text": "性别：男", "bbox": [269, 147, 369, 168], "bbox": [269, 147, 369, 168]},
	{"text": "年龄：27岁", "bbox": [407, 147, 530, 168], "bbox": [407, 147, 530, 168]},
	{"text": "电话：", "bbox": [596, 147, 654, 168], "bbox": [596, 147, 654, 168]},
	{"text": "家庭住址：沙门", "bbox": [3, 177, 189, 199], "bbox": [3, 177, 189, 199]},
	{"text": "药敏史：无", "bbox": [543, 177, 674, 199], "bbox": [543, 177, 674, 199]},
	{"text": "发病日期：", "bbox": [3, 206, 119, 228], "bbox": [3, 206, 119, 228]},
	{"text": "诊断：2型糖尿病", "bbox": [348, 206, 545, 228], "bbox": [348, 206, 545, 228]},
	{"text": "主诉：发现口渴.口干.多饮多尿.3个月余.", "bbox": [89, 238, 637, 260], "bbox": [89, 238, 637, 260]},
	{"text": "现病史：患者三个月前发现自己口渴.口干.多饮多尿自测空腹血糖", "bbox": [60, 277, 852, 298], "bbox": [60, 277, 852, 298]},
	{"text": "11.0mmol/L.规律口服二甲双胍每次0.5g 每日三次 血糖控", "bbox": [170, 298, 876, 319], "bbox": [170, 298, 876, 319]},
	{"text": "制不理想.前来就诊", "bbox": [170, 318, 399, 339], "bbox": [170, 318, 399, 339]},
	{"text": "既往史：否认药物过敏史，否认传染病史。", "bbox": [58, 358, 554, 379], "bbox": [58, 358, 554, 379]},
	{"text": "体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，", "bbox": [29, 405, 857, 426], "bbox": [29, 405, 857, 426]},
	{"text": "心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，", "bbox": [170, 425, 857, 446], "bbox": [170, 425, 857, 446]},
	{"text": "肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射", "bbox": [169, 445, 874, 466], "bbox": [169, 445, 874, 466]},
	{"text": "未引出。", "bbox": [169, 465, 264, 486], "bbox": [169, 465, 264, 486]},
	{"text": "辅助检查：血糖10.6mmol/L. 糖化10%", "bbox": [24, 506, 469, 527], "bbox": [24, 506, 469, 527]},
	{"text": "初步诊断：二型糖尿病", "bbox": [23, 553, 306, 575], "bbox": [23, 553, 306, 575]},
	{"text": "处理措施：1.糖尿病饮食.2.适当运动.3.规律服用二甲双胍 4.定期复查", "bbox": [21, 602, 856, 624], "bbox": [21, 602, 856, 624]},
	{"text": "医师签名：李层", "bbox": [198, 668, 395, 689], "bbox": [198, 668, 395, 689]},
	{"text": "打印时间：2025/3/19 17:04:36", "bbox": [471, 668, 821, 689], "bbox": [471, 668, 821, 689]}
]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=13.8s
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市金水区国基路沙门社区卫生服务中心门诊电子病历, bbox=[121, 67, 767, 88]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[1]: text=No: 20241116000027, bbox=[594, 94, 831, 111]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[2]: text=就诊类型：初诊, bbox=[3, 117, 190, 139]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[3]: text=科别：内科, bbox=[269, 117, 396, 139]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间：2024/11/16 8:09:23, bbox=[543, 117, 886, 139]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[5]: text=姓名：., bbox=[3, 147, 100, 168]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[6]: text=性别：男, bbox=[269, 147, 369, 168]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：27岁, bbox=[407, 147, 530, 168]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[8]: text=电话：, bbox=[596, 147, 654, 168]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[9]: text=家庭住址：沙门, bbox=[3, 177, 189, 199]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[10]: text=药敏史：无, bbox=[543, 177, 674, 199]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[11]: text=发病日期：, bbox=[3, 206, 119, 228]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[12]: text=诊断：2型糖尿病, bbox=[348, 206, 545, 228]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[13]: text=主诉：发现口渴.口干.多饮多尿.3个月余., bbox=[89, 238, 637, 260]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[14]: text=现病史：患者三个月前发现自己口渴.口干.多饮多尿自测空腹血糖, bbox=[60, 277, 852, 298]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[15]: text=11.0mmol/L.规律口服二甲双胍每次0.5g 每日三次 血糖控, bbox=[170, 298, 876, 319]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[16]: text=制不理想.前来就诊, bbox=[170, 318, 399, 339]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：否认药物过敏史，否认传染病史。, bbox=[58, 358, 554, 379]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[18]: text=体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，, bbox=[29, 405, 857, 426]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[19]: text=心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，, bbox=[170, 425, 857, 446]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[20]: text=肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射, bbox=[169, 445, 874, 466]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[21]: text=未引出。, bbox=[169, 465, 264, 486]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[22]: text=辅助检查：血糖10.6mmol/L. 糖化10%, bbox=[24, 506, 469, 527]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[23]: text=初步诊断：二型糖尿病, bbox=[23, 553, 306, 575]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[24]: text=处理措施：1.糖尿病饮食.2.适当运动.3.规律服用二甲双胍 4.定期复查, bbox=[21, 602, 856, 624]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[25]: text=医师签名：李层, bbox=[198, 668, 395, 689]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] coord item[26]: text=打印时间：2025/3/19 17:04:36, bbox=[471, 668, 821, 689]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] page=0 — 27/27 coords, api_time=13.8s
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] new_positions (27):
[[0, 71.99499999999999, 456.36499999999995, 56.414, 74.096], [0, 353.43, 494.445, 79.148, 93.462], [0, 1.785, 113.05, 98.514, 117.038], [0, 160.055, 235.61999999999998, 98.514, 117.038], [0, 323.085, 527.17, 98.514, 117.038], [0, 1.785, 59.5, 123.774, 141.456], [0, 160.055, 219.55499999999998, 123.774, 141.456], [0, 242.165, 315.34999999999997, 123.774, 141.456], [0, 354.62, 389.13, 123.774, 141.456], [0, 1.785, 112.455, 149.034, 167.558], [0, 323.085, 401.03, 149.034, 167.558], [0, 1.785, 70.80499999999999, 173.452, 191.976], [0, 207.06, 324.275, 173.452, 191.976], [0, 52.955, 379.015, 200.396, 218.92], [0, 35.699999999999996, 506.94, 233.23399999999998, 250.916], [0, 101.14999999999999, 521.22, 250.916, 268.598], [0, 101.14999999999999, 237.405, 267.756, 285.438], [0, 34.51, 329.63, 301.436, 319.118], [0, 17.255, 509.91499999999996, 341.01, 358.692], [0, 101.14999999999999, 509.91499999999996, 357.84999999999997, 375.532], [0, 100.55499999999999, 520.03, 374.69, 392.372], [0, 100.55499999999999, 157.07999999999998, 391.53, 409.212], [0, 14.28, 279.055, 426.05199999999996, 443.734], [0, 13.684999999999999, 182.07, 465.626, 484.15], [0, 12.495, 509.32, 506.88399999999996, 525.408], [0, 117.80999999999999, 235.02499999999998, 562.456, 580.138], [0, 280.245, 488.495, 562.456, 580.138]]
2026-08-10 07:10:57,792 INFO     29 [qwen-vl-text] ═══ DONE ═══ 27 positions, pages=1, time=15.9s
2026-08-10 07:10:57,793 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:10:57,794 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:10:57,794 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 07:10:57,794 INFO     29 [qwen-vl-text] positions(21): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:10:57,794 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [21]
2026-08-10 07:10:57,998 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:10:57,999 INFO     29 [qwen-vl-text] LLM extraction start, text_len=481
2026-08-10 07:10:57,999 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:10:57,999 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 290, \"bbox_end\": 310, \"encounter_dates\": [\"2025-04-17\"], \"department\": \"内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "郑州市金水区国基路沙门社区卫生服务中心门诊电子病历\nNo: 20250417000042\n就诊类型：初诊 科别：内科 就诊时间：2025/4/17 8:14:34\n姓名： 性别：男 年龄：27岁 电话：13673657585\n家庭住址：沙门 药敏史：无\n发病日期：2025-04-17 诊断：糖尿病\n主诉：患糖尿病1年余\n现病史：患者1年前发现自己口渴，口干，多饮多尿，自测空腹血糖\n11.0mmol/1，规律口服二甲双胍 每次0.5，每日三次，现来复查\n就诊\n既往史：否认药物过敏史，否认传染病史。\n体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，\n心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，\n肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射\n未引出。\n辅助检查：血糖11.15mmol/1 糖化血红蛋白9%\n初步诊断：二型糖尿病\n处理措施：1，糖尿病饮食 保持心情愉悦 2，适量运动 3.继续规律服用 二\n甲双胍片 4，定期检测血糖 5.不适随诊\n医师签名：李层 打印时间：2025/4/22 17:08:28\n健康管理部门",
    "role": "user"
  }
]
2026-08-10 07:11:00,748 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:00,748 INFO     29 [qwen-vl-text] LLM output (len=293):
{
  "encounter_date": "2025-04-17",
  "chief_complaint": "患糖尿病1年余",
  "present_illness": "患者1年前发现自己口渴，口干，多饮多尿，自测空腹血糖11.0mmol/1，规律口服二甲双胍 每次0.5，每日三次，现来复查就诊",
  "past_history": "否认药物过敏史，否认传染病史。",
  "diagnosis": "二型糖尿病",
  "treatment_plan": "1，糖尿病饮食 保持心情愉悦 2，适量运动 3.继续规律服用 二甲双胍片 4，定期检测血糖 5.不适随诊"
}
2026-08-10 07:11:00,748 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-17]
2026-08-10 07:11:00,751 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1230341, prompt_len=1157
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["郑州市金水区国基路沙门社区卫生服务中心门诊电子病历", "No: 20250417000042", "就诊类型：初诊 科别：内科 就诊时间：2025/4/17 8:14:34", "姓名： 性别：男 年龄：27岁 电话：13673657585", "家庭住址：沙门 药敏史：无", "发病日期：2025-04-17 诊断：糖尿病", "主诉：患糖尿病1年余", "现病史：患者1年前发现自己口渴，口干，多饮多尿，自测空腹血糖", "11.0mmol/1，规律口服二甲双胍 每次0.5，每日三次，现来复查", "就诊", "既往史：否认药物过敏史，否认传染病史。", "体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，", "心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，", "肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射", "未引出。", "辅助检查：血糖11.15mmol/1 糖化血红蛋白9%", "初步诊断：二型糖尿病", "处理措施：1，糖尿病饮食 保持心情愉悦 2，适量运动 3.继续规律服用 二", "甲双胍片 4，定期检测血糖 5.不适随诊", "医师签名：李层 打印时间：2025/4/22 17:08:28", "健康管理部门"]

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
2026-08-10 07:11:09,307 INFO     29 [qwen-vl-text] coord API raw response (len=1397):
[
	{"text": "郑州市金水区国基路沙门社区卫生服务中心门诊电子病历", "bbox": [155, 80, 840, 103]},
	{"text": "No: 20250417000042", "bbox": [657, 109, 908, 127]},
	{"text": "就诊类型：初诊 科别：内科 就诊时间：2025/4/17 8:14:34", "bbox": [31, 131, 954, 154]},
	{"text": "姓名： 性别：男 年龄：27岁 电话：13673657585", "bbox": [31, 160, 895, 183]},
	{"text": "家庭住址：沙门 药敏史：无", "bbox": [32, 191, 742, 215]},
	{"text": "发病日期：2025-04-17 诊断：糖尿病", "bbox": [32, 222, 561, 245]},
	{"text": "主诉：患糖尿病1年余", "bbox": [121, 256, 402, 279]},
	{"text": "现病史：患者1年前发现自己口渴，口干，多饮多尿，自测空腹血糖", "bbox": [92, 297, 911, 320]},
	{"text": "11.0mmol/1，规律口服二甲双胍 每次0.5，每日三次，现来复查", "bbox": [208, 320, 965, 341]},
	{"text": "就诊", "bbox": [208, 341, 266, 362]},
	{"text": "既往史：否认药物过敏史，否认传染病史。", "bbox": [93, 382, 609, 405]},
	{"text": "体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，", "bbox": [64, 432, 938, 455]},
	{"text": "心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，", "bbox": [208, 454, 938, 476]},
	{"text": "肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射", "bbox": [208, 475, 954, 497]},
	{"text": "未引出。", "bbox": [208, 497, 307, 517]},
	{"text": "辅助检查：血糖11.15mmol/1 糖化血红蛋白9%", "bbox": [62, 538, 614, 561]},
	{"text": "初步诊断：二型糖尿病", "bbox": [62, 589, 351, 612]},
	{"text": "处理措施：1，糖尿病饮食 保持心情愉悦 2，适量运动 3.继续规律服用 二", "bbox": [62, 640, 978, 663]},
	{"text": "甲双胍片 4，定期检测血糖 5.不适随诊", "bbox": [208, 661, 692, 683]},
	{"text": "医师签名：李层 打印时间：2025/4/22 17:08:28", "bbox": [238, 707, 900, 730]},
	{"text": "健康管理部门", "bbox": [703, 805, 870, 863]}
]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=8.6s
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市金水区国基路沙门社区卫生服务中心门诊电子病历, bbox=[155, 80, 840, 103]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[1]: text=No: 20250417000042, bbox=[657, 109, 908, 127]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[2]: text=就诊类型：初诊 科别：内科 就诊时间：2025/4/17 8:14:34, bbox=[31, 131, 954, 154]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[3]: text=姓名： 性别：男 年龄：27岁 电话：13673657585, bbox=[31, 160, 895, 183]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[4]: text=家庭住址：沙门 药敏史：无, bbox=[32, 191, 742, 215]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[5]: text=发病日期：2025-04-17 诊断：糖尿病, bbox=[32, 222, 561, 245]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：患糖尿病1年余, bbox=[121, 256, 402, 279]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：患者1年前发现自己口渴，口干，多饮多尿，自测空腹血糖, bbox=[92, 297, 911, 320]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[8]: text=11.0mmol/1，规律口服二甲双胍 每次0.5，每日三次，现来复查, bbox=[208, 320, 965, 341]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[9]: text=就诊, bbox=[208, 341, 266, 362]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[10]: text=既往史：否认药物过敏史，否认传染病史。, bbox=[93, 382, 609, 405]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[11]: text=体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，, bbox=[64, 432, 938, 455]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[12]: text=心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，, bbox=[208, 454, 938, 476]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[13]: text=肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射, bbox=[208, 475, 954, 497]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[14]: text=未引出。, bbox=[208, 497, 307, 517]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[15]: text=辅助检查：血糖11.15mmol/1 糖化血红蛋白9%, bbox=[62, 538, 614, 561]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[16]: text=初步诊断：二型糖尿病, bbox=[62, 589, 351, 612]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[17]: text=处理措施：1，糖尿病饮食 保持心情愉悦 2，适量运动 3.继续规律服用 二, bbox=[62, 640, 978, 663]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[18]: text=甲双胍片 4，定期检测血糖 5.不适随诊, bbox=[208, 661, 692, 683]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[19]: text=医师签名：李层 打印时间：2025/4/22 17:08:28, bbox=[238, 707, 900, 730]
2026-08-10 07:11:09,308 INFO     29 [qwen-vl-text] coord item[20]: text=健康管理部门, bbox=[703, 805, 870, 863]
2026-08-10 07:11:09,309 INFO     29 [qwen-vl-text] page=8 — 21/21 coords, api_time=8.6s
2026-08-10 07:11:09,309 INFO     29 [qwen-vl-text] new_positions (21):
[[8, 92.225, 499.79999999999995, 67.36, 86.726], [8, 390.91499999999996, 540.26, 91.77799999999999, 106.934], [8, 18.445, 567.63, 110.30199999999999, 129.668], [8, 18.445, 532.525, 134.72, 154.08599999999998], [8, 19.04, 441.48999999999995, 160.822, 181.03], [8, 19.04, 333.79499999999996, 186.924, 206.29], [8, 71.99499999999999, 239.19, 215.552, 234.91799999999998], [8, 54.739999999999995, 542.045, 250.07399999999998, 269.44], [8, 123.75999999999999, 574.175, 269.44, 287.122], [8, 123.75999999999999, 158.26999999999998, 287.122, 304.804], [8, 55.335, 362.35499999999996, 321.644, 341.01], [8, 38.08, 558.11, 363.74399999999997, 383.11], [8, 123.75999999999999, 558.11, 382.268, 400.792], [8, 123.75999999999999, 567.63, 399.95, 418.474], [8, 123.75999999999999, 182.665, 418.474, 435.31399999999996], [8, 36.89, 365.33, 452.996, 472.36199999999997], [8, 36.89, 208.845, 495.938, 515.304], [8, 36.89, 581.91, 538.88, 558.246], [8, 123.75999999999999, 411.74, 556.562, 575.086], [8, 141.60999999999999, 535.5, 595.294, 614.66], [8, 418.28499999999997, 517.65, 677.81, 726.646]]
2026-08-10 07:11:09,309 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=11.5s
2026-08-10 07:11:09,324 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 07:11:09,324 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:11:09,324 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 07:11:09,325 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:11:09.324+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"48638ddc948a11f1bd9827cf206dfa2d": {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:11:09,333 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:11:09,334 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:11:09,334 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 07:11:09,334 INFO     29 [qwen-vl-text] positions(16): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:11:09,334 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [16]
2026-08-10 07:11:09,537 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:11:09,538 INFO     29 [qwen-vl-text] LLM extraction start, text_len=226
2026-08-10 07:11:09,538 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:09,538 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 257, \"bbox_end\": 272, \"encounter_dates\": [\"2025-04-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "越人大药房\n祝您身体健康\n日期：2025-04-02 NO：1.2468223\n会员：  会员卡：1004832\n药品名称 数量 单位 单价 金额\n盐酸二甲双胍 0.25*60 片\n生产厂商：上海信谊\n批号：\n2 5.50 11.00\n应收：11.00 收款：11.00\n找零：0.00 找零：0.00\n付款方式：现金 实收：11.00\n收款：刘丽婷 时间：11：06：25\n地址：三全路渠东路东岸尚景\n电话：63222645\n药品无质量问题概不退换！",
    "role": "user"
  }
]
2026-08-10 07:11:12,168 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:12,168 INFO     29 [qwen-vl-text] LLM output (len=409):
{
  "encounter_date": "2025-04-02",
  "pharmacy": "越人大药房",
  "medications": [
    {
      "name": "盐酸二甲双胍",
      "specification": "0.25*60片",
      "dosage": null,
      "quantity": 2,
      "unit_price": 5.50,
      "total_price": 11.00,
      "frequency": null,
      "route": null,
      "manufacturer": "上海信谊",
      "approval_number": null
    }
  ],
  "payment_total": 11.00,
  "payment_method": "现金"
}
2026-08-10 07:11:12,168 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-02]
2026-08-10 07:11:12,170 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=893003, prompt_len=887
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["越人大药房", "祝您身体健康", "日期：2025-04-02 NO：1.2468223", "会员：  会员卡：1004832", "药品名称 数量 单位 单价 金额", "盐酸二甲双胍 0.25*60 片", "生产厂商：上海信谊", "批号：", "2 5.50 11.00", "应收：11.00 收款：11.00", "找零：0.00 找零：0.00", "付款方式：现金 实收：11.00", "收款：刘丽婷 时间：11：06：25", "地址：三全路渠东路东岸尚景", "电话：63222645", "药品无质量问题概不退换！"]

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
2026-08-10 07:11:18,313 INFO     29 [qwen-vl-text] coord API raw response (len=931):
[
	{"text": "越人大药房", "bbox": [357, 42, 662, 81]},
	{"text": "祝您身体健康", "bbox": [357, 108, 725, 147]},
	{"text": "日期：2025-04-02 NO：1.2468223", "bbox": [169, 165, 930, 197]},
	{"text": "会员：  会员卡：1004832", "bbox": [167, 216, 930, 250]},
	{"text": "药品名称 数量 单位 单价 金额", "bbox": [167, 267, 928, 301]},
	{"text": "盐酸二甲双胍 0.25*60 片", "bbox": [172, 369, 925, 403]},
	{"text": "生产厂商：上海信谊", "bbox": [170, 419, 646, 451]},
	{"text": "批号：", "bbox": [170, 470, 300, 500]},
	{"text": "2 5.50 11.00", "bbox": [389, 521, 925, 549]},
	{"text": "应收：11.00 收款：11.00", "bbox": [172, 568, 842, 599]},
	{"text": "找零：0.00 找零：0.00", "bbox": [170, 620, 789, 652]},
	{"text": "付款方式：现金 实收：11.00", "bbox": [172, 669, 925, 703]},
	{"text": "收款：刘丽婷 时间：11：06：25", "bbox": [167, 721, 925, 754]},
	{"text": "地址：三全路渠东路东岸尚景", "bbox": [167, 762, 868, 796]},
	{"text": "电话：63222645", "bbox": [167, 803, 545, 835]},
	{"text": "药品无质量问题概不退换！", "bbox": [167, 838, 784, 872]}
]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=6.1s
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[0]: text=越人大药房, bbox=[357, 42, 662, 81]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[1]: text=祝您身体健康, bbox=[357, 108, 725, 147]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[2]: text=日期：2025-04-02 NO：1.2468223, bbox=[169, 165, 930, 197]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[3]: text=会员：  会员卡：1004832, bbox=[167, 216, 930, 250]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[4]: text=药品名称 数量 单位 单价 金额, bbox=[167, 267, 928, 301]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[5]: text=盐酸二甲双胍 0.25*60 片, bbox=[172, 369, 925, 403]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[6]: text=生产厂商：上海信谊, bbox=[170, 419, 646, 451]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[7]: text=批号：, bbox=[170, 470, 300, 500]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[8]: text=2 5.50 11.00, bbox=[389, 521, 925, 549]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[9]: text=应收：11.00 收款：11.00, bbox=[172, 568, 842, 599]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[10]: text=找零：0.00 找零：0.00, bbox=[170, 620, 789, 652]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[11]: text=付款方式：现金 实收：11.00, bbox=[172, 669, 925, 703]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[12]: text=收款：刘丽婷 时间：11：06：25, bbox=[167, 721, 925, 754]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[13]: text=地址：三全路渠东路东岸尚景, bbox=[167, 762, 868, 796]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[14]: text=电话：63222645, bbox=[167, 803, 545, 835]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] coord item[15]: text=药品无质量问题概不退换！, bbox=[167, 838, 784, 872]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] page=6 — 16/16 coords, api_time=6.1s
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] new_positions (16):
[[6, 212.415, 393.89, 35.364, 68.202], [6, 212.415, 431.375, 90.93599999999999, 123.774], [6, 100.55499999999999, 553.35, 138.93, 165.874], [6, 99.365, 553.35, 181.87199999999999, 210.5], [6, 99.365, 552.16, 224.814, 253.44199999999998], [6, 102.33999999999999, 550.375, 310.698, 339.32599999999996], [6, 101.14999999999999, 384.37, 352.798, 379.74199999999996], [6, 101.14999999999999, 178.5, 395.74, 421.0], [6, 231.45499999999998, 550.375, 438.68199999999996, 462.258], [6, 102.33999999999999, 500.98999999999995, 478.256, 504.358], [6, 101.14999999999999, 469.455, 522.04, 548.984], [6, 102.33999999999999, 550.375, 563.298, 591.9259999999999], [6, 99.365, 550.375, 607.082, 634.8679999999999], [6, 99.365, 516.4599999999999, 641.6039999999999, 670.232], [6, 99.365, 324.275, 676.126, 703.0699999999999], [6, 99.365, 466.47999999999996, 705.596, 734.2239999999999]]
2026-08-10 07:11:18,314 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=9.0s
2026-08-10 07:11:18,315 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:11:18,316 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:11:18,316 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 07:11:18,316 INFO     29 [qwen-vl-text] positions(17): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:11:18,316 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [17]
2026-08-10 07:11:18,461 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:11:18,462 INFO     29 [qwen-vl-text] LLM extraction start, text_len=231
2026-08-10 07:11:18,462 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:18,462 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 273, \"bbox_end\": 289, \"encounter_dates\": [\"2025-02-13\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "越人大药房\n祝您身体健康\n日期：2025-02-13 NO：1.2467129\n会员：\n会员卡：1004832\n药品名称 数量 单位 单价 金额\n盐酸二甲双胍 规格：0.25*60片\n生产厂商：上海信宜\n批号：\n5 盒 5.50 27.50\n应收：27.50 收款：27.50\n找零：0.00 折扣：0.00\n付款方式：a 现金 实收：27.50\n收款：刘丽婷 时间：16:27:56\n地址：三全路渠东路东岸尚景\n电话：63222645\n药品无质量问题概不退换！",
    "role": "user"
  }
]
2026-08-10 07:11:21,845 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:21,846 INFO     29 [qwen-vl-text] LLM output (len=409):
{
  "encounter_date": "2025-02-13",
  "pharmacy": "越人大药房",
  "medications": [
    {
      "name": "盐酸二甲双胍",
      "specification": "0.25*60片",
      "dosage": null,
      "quantity": 5,
      "unit_price": 5.50,
      "total_price": 27.50,
      "frequency": null,
      "route": null,
      "manufacturer": "上海信宜",
      "approval_number": null
    }
  ],
  "payment_total": 27.50,
  "payment_method": "现金"
}
2026-08-10 07:11:21,846 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-13]
2026-08-10 07:11:21,851 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=704752, prompt_len=895
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["越人大药房", "祝您身体健康", "日期：2025-02-13 NO：1.2467129", "会员：", "会员卡：1004832", "药品名称 数量 单位 单价 金额", "盐酸二甲双胍 规格：0.25*60片", "生产厂商：上海信宜", "批号：", "5 盒 5.50 27.50", "应收：27.50 收款：27.50", "找零：0.00 折扣：0.00", "付款方式：a 现金 实收：27.50", "收款：刘丽婷 时间：16:27:56", "地址：三全路渠东路东岸尚景", "电话：63222645", "药品无质量问题概不退换！"]

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
2026-08-10 07:11:28,130 INFO     29 [qwen-vl-text] coord API raw response (len=981):
[
	{"text": "越人大药房", "bbox": [385, 97, 631, 132]},
	{"text": "祝您身体健康", "bbox": [386, 157, 684, 195]},
	{"text": "日期：2025-02-13 NO：1.2467129", "bbox": [234, 211, 853, 243]},
	{"text": "会员：", "bbox": [232, 261, 340, 293]},
	{"text": "会员卡：1004832", "bbox": [515, 261, 853, 293]},
	{"text": "药品名称 数量 单位 单价 金额", "bbox": [232, 308, 851, 342]},
	{"text": "盐酸二甲双胍 规格：0.25*60片", "bbox": [234, 408, 851, 442]},
	{"text": "生产厂商：上海信宜", "bbox": [234, 457, 619, 489]},
	{"text": "批号：", "bbox": [234, 507, 338, 540]},
	{"text": "5 盒 5.50 27.50", "bbox": [410, 561, 851, 591]},
	{"text": "应收：27.50 收款：27.50", "bbox": [234, 607, 780, 639]},
	{"text": "找零：0.00 折扣：0.00", "bbox": [234, 657, 736, 689]},
	{"text": "付款方式：a 现金 实收：27.50", "bbox": [236, 707, 851, 740]},
	{"text": "收款：刘丽婷 时间：16:27:56", "bbox": [234, 757, 851, 790]},
	{"text": "地址：三全路渠东路东岸尚景", "bbox": [234, 798, 799, 832]},
	{"text": "电话：63222645", "bbox": [236, 837, 537, 869]},
	{"text": "药品无质量问题概不退换！", "bbox": [236, 870, 730, 904]}
]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=6.3s
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[0]: text=越人大药房, bbox=[385, 97, 631, 132]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[1]: text=祝您身体健康, bbox=[386, 157, 684, 195]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[2]: text=日期：2025-02-13 NO：1.2467129, bbox=[234, 211, 853, 243]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[3]: text=会员：, bbox=[232, 261, 340, 293]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[4]: text=会员卡：1004832, bbox=[515, 261, 853, 293]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[5]: text=药品名称 数量 单位 单价 金额, bbox=[232, 308, 851, 342]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[6]: text=盐酸二甲双胍 规格：0.25*60片, bbox=[234, 408, 851, 442]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[7]: text=生产厂商：上海信宜, bbox=[234, 457, 619, 489]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[8]: text=批号：, bbox=[234, 507, 338, 540]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[9]: text=5 盒 5.50 27.50, bbox=[410, 561, 851, 591]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[10]: text=应收：27.50 收款：27.50, bbox=[234, 607, 780, 639]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[11]: text=找零：0.00 折扣：0.00, bbox=[234, 657, 736, 689]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[12]: text=付款方式：a 现金 实收：27.50, bbox=[236, 707, 851, 740]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[13]: text=收款：刘丽婷 时间：16:27:56, bbox=[234, 757, 851, 790]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[14]: text=地址：三全路渠东路东岸尚景, bbox=[234, 798, 799, 832]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[15]: text=电话：63222645, bbox=[236, 837, 537, 869]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] coord item[16]: text=药品无质量问题概不退换！, bbox=[236, 870, 730, 904]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] page=7 — 17/17 coords, api_time=6.3s
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] new_positions (17):
[[7, 229.075, 375.445, 81.67399999999999, 111.14399999999999], [7, 229.67, 406.97999999999996, 132.194, 164.19], [7, 139.23, 507.53499999999997, 177.662, 204.606], [7, 138.04, 202.29999999999998, 219.762, 246.706], [7, 306.425, 507.53499999999997, 219.762, 246.706], [7, 138.04, 506.34499999999997, 259.336, 287.964], [7, 139.23, 506.34499999999997, 343.536, 372.164], [7, 139.23, 368.305, 384.794, 411.738], [7, 139.23, 201.10999999999999, 426.894, 454.68], [7, 243.95, 506.34499999999997, 472.36199999999997, 497.62199999999996], [7, 139.23, 464.09999999999997, 511.094, 538.038], [7, 139.23, 437.91999999999996, 553.194, 580.138], [7, 140.42, 506.34499999999997, 595.294, 623.0799999999999], [7, 139.23, 506.34499999999997, 637.394, 665.18], [7, 139.23, 475.405, 671.9159999999999, 700.544], [7, 140.42, 319.515, 704.754, 731.698], [7, 140.42, 434.34999999999997, 732.54, 761.168]]
2026-08-10 07:11:28,131 INFO     29 [qwen-vl-text] ═══ DONE ═══ 17 positions, pages=1, time=9.8s
2026-08-10 07:11:28,143 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 07:11:28,143 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:11:28,143 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 07:11:28,152 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:11:28,153 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:11:28,154 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 07:11:28,154 INFO     29 [qwen-vl-text] positions(22): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:11:28,154 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [22]
2026-08-10 07:11:28,329 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:11:28,330 INFO     29 [qwen-vl-text] LLM extraction start, text_len=221
2026-08-10 07:11:28,330 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:28,330 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 311, \"bbox_end\": 332, \"encounter_dates\": [\"2025-04-17\"], \"department\": \"内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "郑州市金水区国基路沙门社区\n卫生服务中心处方笺\n医保证号:\n费别:自费\n门诊号:20250417000042\n日期:2025-04-17\n姓名:\n性别:男\n年龄:27岁\n科别:内科\n住址:沙门\n临床诊断:糖尿病\nRp:\n1 (基)(集)盐酸二甲双胍缓释片(0.5g*60S)\n2瓶\n用法:每次0.5g口服一天三次*30天\n医师(签字/盖章):李层\n审核、调配:\n核对、发药:\n药费:10.34\n执行科室:西药房\n打印日期:2025/04/17",
    "role": "user"
  }
]
2026-08-10 07:11:31,347 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:31,347 INFO     29 [qwen-vl-text] LLM output (len=405):
{
  "encounter_date": "2025-04-17",
  "prescription_type": "门诊处方",
  "prescriber": "李层",
  "department": "内科",
  "diagnosis": "糖尿病",
  "items": [
    {
      "drug_generic_name": "盐酸二甲双胍缓释片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "tid",
      "route": "口服",
      "duration_days": 30,
      "quantity": "2瓶",
      "notes": null
    }
  ]
}
2026-08-10 07:11:31,347 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-17]
2026-08-10 07:11:31,348 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=434754, prompt_len=900
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["郑州市金水区国基路沙门社区", "卫生服务中心处方笺", "医保证号:", "费别:自费", "门诊号:20250417000042", "日期:2025-04-17", "姓名:", "性别:男", "年龄:27岁", "科别:内科", "住址:沙门", "临床诊断:糖尿病", "Rp:", "1 (基)(集)盐酸二甲双胍缓释片(0.5g*60S)", "2瓶", "用法:每次0.5g口服一天三次*30天", "医师(签字/盖章):李层", "审核、调配:", "核对、发药:", "药费:10.34", "执行科室:西药房", "打印日期:2025/04/17"]

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
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord API raw response (len=1188):
[
	{"text": "郑州市金水区国基路沙门社区", "bbox": [276, 38, 758, 65]},
	{"text": "卫生服务中心处方笺", "bbox": [350, 65, 684, 89]},
	{"text": "医保证号:", "bbox": [137, 118, 236, 135]},
	{"text": "费别:自费", "bbox": [532, 117, 640, 135]},
	{"text": "门诊号:20250417000042", "bbox": [136, 150, 398, 168]},
	{"text": "日期:2025-04-17", "bbox": [534, 150, 722, 168]},
	{"text": "姓名:", "bbox": [135, 180, 187, 198]},
	{"text": "性别:男", "bbox": [395, 180, 484, 198]},
	{"text": "年龄:27岁", "bbox": [560, 179, 678, 196]},
	{"text": "科别:内科", "bbox": [135, 207, 244, 225]},
	{"text": "住址:沙门", "bbox": [393, 207, 507, 225]},
	{"text": "临床诊断:糖尿病", "bbox": [135, 234, 340, 252]},
	{"text": "Rp:", "bbox": [138, 262, 185, 285]},
	{"text": "1 (基)(集)盐酸二甲双胍缓释片(0.5g*60S)", "bbox": [169, 296, 580, 314]},
	{"text": "2瓶", "bbox": [764, 297, 800, 313]},
	{"text": "用法:每次0.5g口服一天三次*30天", "bbox": [312, 323, 646, 340]},
	{"text": "医师(签字/盖章):李层", "bbox": [434, 580, 657, 597]},
	{"text": "审核、调配:", "bbox": [153, 607, 275, 624]},
	{"text": "核对、发药:", "bbox": [399, 607, 522, 624]},
	{"text": "药费:10.34", "bbox": [645, 606, 775, 623]},
	{"text": "执行科室:西药房", "bbox": [153, 633, 336, 651]},
	{"text": "打印日期:2025/04/17", "bbox": [454, 633, 689, 651]}
]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=7.0s
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市金水区国基路沙门社区, bbox=[276, 38, 758, 65]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[1]: text=卫生服务中心处方笺, bbox=[350, 65, 684, 89]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[2]: text=医保证号:, bbox=[137, 118, 236, 135]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[3]: text=费别:自费, bbox=[532, 117, 640, 135]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[4]: text=门诊号:20250417000042, bbox=[136, 150, 398, 168]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[5]: text=日期:2025-04-17, bbox=[534, 150, 722, 168]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[6]: text=姓名:, bbox=[135, 180, 187, 198]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[7]: text=性别:男, bbox=[395, 180, 484, 198]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[8]: text=年龄:27岁, bbox=[560, 179, 678, 196]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[9]: text=科别:内科, bbox=[135, 207, 244, 225]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[10]: text=住址:沙门, bbox=[393, 207, 507, 225]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[11]: text=临床诊断:糖尿病, bbox=[135, 234, 340, 252]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[12]: text=Rp:, bbox=[138, 262, 185, 285]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[13]: text=1 (基)(集)盐酸二甲双胍缓释片(0.5g*60S), bbox=[169, 296, 580, 314]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[14]: text=2瓶, bbox=[764, 297, 800, 313]
2026-08-10 07:11:38,397 INFO     29 [qwen-vl-text] coord item[15]: text=用法:每次0.5g口服一天三次*30天, bbox=[312, 323, 646, 340]
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] coord item[16]: text=医师(签字/盖章):李层, bbox=[434, 580, 657, 597]
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] coord item[17]: text=审核、调配:, bbox=[153, 607, 275, 624]
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] coord item[18]: text=核对、发药:, bbox=[399, 607, 522, 624]
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] coord item[19]: text=药费:10.34, bbox=[645, 606, 775, 623]
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] coord item[20]: text=执行科室:西药房, bbox=[153, 633, 336, 651]
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] coord item[21]: text=打印日期:2025/04/17, bbox=[454, 633, 689, 651]
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] page=9 — 22/22 coords, api_time=7.0s
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] new_positions (22):
[[9, 164.22, 451.01, 31.996, 54.73], [9, 208.25, 406.97999999999996, 54.73, 74.938], [9, 81.515, 140.42, 99.356, 113.67], [9, 316.53999999999996, 380.79999999999995, 98.514, 113.67], [9, 80.92, 236.81, 126.3, 141.456], [9, 317.72999999999996, 429.59, 126.3, 141.456], [9, 80.325, 111.265, 151.56, 166.716], [9, 235.02499999999998, 287.97999999999996, 151.56, 166.716], [9, 333.2, 403.40999999999997, 150.718, 165.03199999999998], [9, 80.325, 145.18, 174.29399999999998, 189.45], [9, 233.83499999999998, 301.66499999999996, 174.29399999999998, 189.45], [9, 80.325, 202.29999999999998, 197.028, 212.184], [9, 82.11, 110.07499999999999, 220.60399999999998, 239.97], [9, 100.55499999999999, 345.09999999999997, 249.232, 264.388], [9, 454.58, 476.0, 250.07399999999998, 263.546], [9, 185.64, 384.37, 271.966, 286.28], [9, 258.22999999999996, 390.91499999999996, 488.35999999999996, 502.674], [9, 91.035, 163.625, 511.094, 525.408], [9, 237.405, 310.59, 511.094, 525.408], [9, 383.775, 461.125, 510.252, 524.566], [9, 91.035, 199.92, 532.986, 548.1419999999999], [9, 270.13, 409.955, 532.986, 548.1419999999999]]
2026-08-10 07:11:38,398 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=10.2s
2026-08-10 07:11:38,411 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 07:11:38,411 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Extractor:Prescription | outputs={"chunks": "1 items, types={'PrescriptionRecord': 1}", "html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:11:38,411 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 07:11:38,422 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:38,422 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 07:11:39,386 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:11:39.385+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"48638ddc948a11f1bd9827cf206dfa2d": {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:11:39,832 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:39,840 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 07:11:39,841 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:11:39,841 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 07:11:39,850 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:39,850 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 07:11:40,466 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:40,481 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 07:11:40,482 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:11:40,482 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 07:11:40,489 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:11:40,490 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:11:40,490 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 07:11:40,490 INFO     29 [qwen-vl-text] positions(15): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:11:40,490 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [15]
2026-08-10 07:11:40,652 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:11:40,653 INFO     29 [qwen-vl-text] LLM extraction start, text_len=203
2026-08-10 07:11:40,653 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:40,654 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 139, \"bbox_end\": 153, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "金水区国基路沙门社区卫生服务中心\nJinshui Gaoji Street Shamen Community Health Services Center\n0001\n姓名：\n条码号：1001241021000001\n流借号：\n胆\n胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增\n宽。\n胰\n胰腺形态、大小正常，内部光点均匀，主胰管无扩张。\n脾\n脾脏大小形态正常，实质回声均匀。\n科室小结：\n脂肪肝",
    "role": "user"
  }
]
2026-08-10 07:11:43,061 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:43,061 INFO     29 [qwen-vl-text] LLM output (len=396):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "腹部超声",
  "exam_category": "imaging",
  "body_part": "肝胆胰脾",
  "patient_name": null,
  "patient_gender": null,
  "department": "金水区国基路沙门社区卫生服务中心",
  "bed_number": null,
  "findings": "胆\n胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增宽。\n胰\n胰腺形态、大小正常，内部光点均匀，主胰管无扩张。\n脾\n脾脏大小形态正常，实质回声均匀。",
  "conclusion": "脂肪肝",
  "physician": null,
  "reviewer": null
}
2026-08-10 07:11:43,063 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=718464, prompt_len=861
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共15行）
["金水区国基路沙门社区卫生服务中心", "Jinshui Gaoji Street Shamen Community Health Services Center", "0001", "姓名：", "条码号：1001241021000001", "流借号：", "胆", "胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增", "宽。", "胰", "胰腺形态、大小正常，内部光点均匀，主胰管无扩张。", "脾", "脾脏大小形态正常，实质回声均匀。", "科室小结：", "脂肪肝"]

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
2026-08-10 07:11:49,694 INFO     29 [qwen-vl-text] coord API raw response (len=1143):
```json
[
	{"text": "金水区国基路沙门社区卫生服务中心", "bbox": [307, 191, 487, 200]},
	{"text": "Jinshui Gaoji Street Shamen Community Health Services Center", "bbox": [307, 204, 487, 211]},
	{"text": "0001", "bbox": [122, 200, 155, 210]},
	{"text": "姓名：", "bbox": [587, 210, 620, 222], "label": "姓名："},
	{"text": "条码号：1001241021000001", "bbox": [668, 210, 823, 221], "label": "条码号：1001241021000001"},
	{"text": "流借号：", "bbox": [385, 230, 429, 241], "label": "流借号："},
	{"text": "胆", "bbox": [244, 251, 257, 261], "label": "胆"},
	{"text": "胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增", "bbox": [385, 251, 752, 262], "label": "胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增"},
	{"text": "宽。", "bbox": [385, 272, 404, 282], "label": "宽。"},
	{"text": "胰", "bbox": [244, 294, 257, 304], "label": "胰"},
	{"text": "胰腺形态、大小正常，内部光点均匀，主胰管无扩张。", "bbox": [385, 294, 682, 304], "label": "胰腺形态、大小正常，内部光点均匀，主胰管无扩张。"},
	{"text": "脾", "bbox": [244, 316, 257, 326], "label": "脾"},
	{"text": "脾脏大小形态正常，实质回声均匀。", "bbox": [385, 316, 581, 326], "label": "脾脏大小形态正常，实质回声均匀。"},
	{"text": "科室小结：", "bbox": [244, 337, 300, 348], "label": "科室小结："},
	{"text": "脂肪肝", "bbox": [385, 337, 424, 348], "label": "脂肪肝"}
]
```
2026-08-10 07:11:49,694 INFO     29 [qwen-vl-text] coord API: raw_items=15, valid_items=15, elapsed=6.6s
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[0]: text=金水区国基路沙门社区卫生服务中心, bbox=[307, 191, 487, 200]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[1]: text=Jinshui Gaoji Street Shamen Community Health Services Center, bbox=[307, 204, 487, 211]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[2]: text=0001, bbox=[122, 200, 155, 210]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[587, 210, 620, 222]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[4]: text=条码号：1001241021000001, bbox=[668, 210, 823, 221]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[5]: text=流借号：, bbox=[385, 230, 429, 241]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[6]: text=胆, bbox=[244, 251, 257, 261]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[7]: text=胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增, bbox=[385, 251, 752, 262]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[8]: text=宽。, bbox=[385, 272, 404, 282]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[9]: text=胰, bbox=[244, 294, 257, 304]
2026-08-10 07:11:49,695 INFO     29 [qwen-vl-text] coord item[10]: text=胰腺形态、大小正常，内部光点均匀，主胰管无扩张。, bbox=[385, 294, 682, 304]
2026-08-10 07:11:49,696 INFO     29 [qwen-vl-text] coord item[11]: text=脾, bbox=[244, 316, 257, 326]
2026-08-10 07:11:49,696 INFO     29 [qwen-vl-text] coord item[12]: text=脾脏大小形态正常，实质回声均匀。, bbox=[385, 316, 581, 326]
2026-08-10 07:11:49,696 INFO     29 [qwen-vl-text] coord item[13]: text=科室小结：, bbox=[244, 337, 300, 348]
2026-08-10 07:11:49,696 INFO     29 [qwen-vl-text] coord item[14]: text=脂肪肝, bbox=[385, 337, 424, 348]
2026-08-10 07:11:49,696 INFO     29 [qwen-vl-text] page=4 — 15/15 coords, api_time=6.6s
2026-08-10 07:11:49,697 INFO     29 [qwen-vl-text] new_positions (15):
[[4, 182.665, 289.765, 160.822, 168.4], [4, 182.665, 289.765, 171.768, 177.662], [4, 72.59, 92.225, 168.4, 176.82], [4, 349.265, 368.9, 176.82, 186.924], [4, 397.46, 489.685, 176.82, 186.082], [4, 229.075, 255.255, 193.66, 202.922], [4, 145.18, 152.915, 211.34199999999998, 219.762], [4, 229.075, 447.44, 211.34199999999998, 220.60399999999998], [4, 229.075, 240.38, 229.024, 237.444], [4, 145.18, 152.915, 247.548, 255.968], [4, 229.075, 405.78999999999996, 247.548, 255.968], [4, 145.18, 152.915, 266.072, 274.492], [4, 229.075, 345.695, 266.072, 274.492], [4, 145.18, 178.5, 283.75399999999996, 293.01599999999996], [4, 229.075, 252.28, 283.75399999999996, 293.01599999999996]]
2026-08-10 07:11:49,697 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=1, time=9.2s
2026-08-10 07:11:49,697 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:11:49,699 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:11:49,699 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 07:11:49,699 INFO     29 [qwen-vl-text] positions(17): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:11:49,700 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [17]
2026-08-10 07:11:49,858 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:11:49,859 INFO     29 [qwen-vl-text] LLM extraction start, text_len=155
2026-08-10 07:11:49,859 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:49,860 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 154, \"bbox_end\": 170, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "◆泌尿系彩超（男）\n(彩超检查)\n检查医生：高培利\n项目\n结果\n单位\n双肾\n双肾形态大小正常、包膜完整光滑，肾实质回声光点均匀，肾盂肾\n盏未见扩张。\n前列腺\n前列腺形态大小正常，轮廓整齐，实质回声均匀。\n膀胱\n膀胱充盈欠佳，壁光滑，其内未见明显异常回声。\n输尿管\n输尿管未见显示扩张。\n科室小结：\n未见明显异常",
    "role": "user"
  }
]
2026-08-10 07:11:52,551 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:52,551 INFO     29 [qwen-vl-text] LLM output (len=427):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "泌尿系彩超（男）",
  "exam_category": "imaging",
  "body_part": "双肾、前列腺、膀胱、输尿管",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "双肾\n双肾形态大小正常、包膜完整光滑，肾实质回声光点均匀，肾盂肾盏未见扩张。\n前列腺\n前列腺形态大小正常，轮廓整齐，实质回声均匀。\n膀胱\n膀胱充盈欠佳，壁光滑，其内未见明显异常回声。\n输尿管\n输尿管未见显示扩张。",
  "conclusion": "未见明显异常",
  "physician": "高培利",
  "reviewer": null
}
2026-08-10 07:11:52,553 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=718464, prompt_len=819
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["◆泌尿系彩超（男）", "(彩超检查)", "检查医生：高培利", "项目", "结果", "单位", "双肾", "双肾形态大小正常、包膜完整光滑，肾实质回声光点均匀，肾盂肾", "盏未见扩张。", "前列腺", "前列腺形态大小正常，轮廓整齐，实质回声均匀。", "膀胱", "膀胱充盈欠佳，壁光滑，其内未见明显异常回声。", "输尿管", "输尿管未见显示扩张。", "科室小结：", "未见明显异常"]

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
2026-08-10 07:11:57,418 INFO     29 [qwen-vl-text] coord API raw response (len=906):
[
	{"text": "◆泌尿系彩超（男）", "bbox": [245, 389, 366, 403]},
	{"text": "(彩超检查)", "bbox": [389, 390, 461, 403]},
	{"text": "检查医生：高培利", "bbox": [648, 389, 770, 402]},
	{"text": "项目", "bbox": [244, 414, 269, 425]},
	{"text": "结果", "bbox": [384, 414, 412, 425]},
	{"text": "单位", "bbox": [763, 414, 789, 425]},
	{"text": "双肾", "bbox": [244, 436, 269, 447]},
	{"text": "双肾形态大小正常、包膜完整光滑，肾实质回声光点均匀，肾盂肾", "bbox": [384, 436, 750, 447]},
	{"text": "盏未见扩张。", "bbox": [384, 457, 455, 468]},
	{"text": "前列腺", "bbox": [244, 477, 281, 488]},
	{"text": "前列腺形态大小正常，轮廓整齐，实质回声均匀。", "bbox": [384, 477, 656, 488]},
	{"text": "膀胱", "bbox": [244, 498, 270, 509]},
	{"text": "膀胱充盈欠佳，壁光滑，其内未见明显异常回声。", "bbox": [384, 498, 656, 509]},
	{"text": "输尿管", "bbox": [244, 519, 281, 529]},
	{"text": "输尿管未见显示扩张。", "bbox": [384, 519, 505, 529]},
	{"text": "科室小结：", "bbox": [244, 540, 300, 551]},
	{"text": "未见明显异常", "bbox": [384, 540, 462, 551]}
]
2026-08-10 07:11:57,418 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=4.9s
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[0]: text=◆泌尿系彩超（男）, bbox=[245, 389, 366, 403]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[1]: text=(彩超检查), bbox=[389, 390, 461, 403]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[2]: text=检查医生：高培利, bbox=[648, 389, 770, 402]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[3]: text=项目, bbox=[244, 414, 269, 425]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[4]: text=结果, bbox=[384, 414, 412, 425]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[5]: text=单位, bbox=[763, 414, 789, 425]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[6]: text=双肾, bbox=[244, 436, 269, 447]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[7]: text=双肾形态大小正常、包膜完整光滑，肾实质回声光点均匀，肾盂肾, bbox=[384, 436, 750, 447]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[8]: text=盏未见扩张。, bbox=[384, 457, 455, 468]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[9]: text=前列腺, bbox=[244, 477, 281, 488]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[10]: text=前列腺形态大小正常，轮廓整齐，实质回声均匀。, bbox=[384, 477, 656, 488]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[11]: text=膀胱, bbox=[244, 498, 270, 509]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[12]: text=膀胱充盈欠佳，壁光滑，其内未见明显异常回声。, bbox=[384, 498, 656, 509]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[13]: text=输尿管, bbox=[244, 519, 281, 529]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[14]: text=输尿管未见显示扩张。, bbox=[384, 519, 505, 529]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[15]: text=科室小结：, bbox=[244, 540, 300, 551]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] coord item[16]: text=未见明显异常, bbox=[384, 540, 462, 551]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] page=4 — 17/17 coords, api_time=4.9s
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] new_positions (17):
[[4, 145.775, 217.76999999999998, 327.538, 339.32599999999996], [4, 231.45499999999998, 274.295, 328.38, 339.32599999999996], [4, 385.56, 458.15, 327.538, 338.484], [4, 145.18, 160.055, 348.58799999999997, 357.84999999999997], [4, 228.48, 245.14, 348.58799999999997, 357.84999999999997], [4, 453.98499999999996, 469.455, 348.58799999999997, 357.84999999999997], [4, 145.18, 160.055, 367.11199999999997, 376.37399999999997], [4, 228.48, 446.25, 367.11199999999997, 376.37399999999997], [4, 228.48, 270.72499999999997, 384.794, 394.056], [4, 145.18, 167.195, 401.63399999999996, 410.89599999999996], [4, 228.48, 390.32, 401.63399999999996, 410.89599999999996], [4, 145.18, 160.65, 419.316, 428.578], [4, 228.48, 390.32, 419.316, 428.578], [4, 145.18, 167.195, 436.998, 445.418], [4, 228.48, 300.47499999999997, 436.998, 445.418], [4, 145.18, 178.5, 454.68, 463.942], [4, 228.48, 274.89, 454.68, 463.942]]
2026-08-10 07:11:57,419 INFO     29 [qwen-vl-text] ═══ DONE ═══ 17 positions, pages=1, time=7.7s
2026-08-10 07:11:57,419 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:11:57,420 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:11:57,420 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 07:11:57,420 INFO     29 [qwen-vl-text] positions(9): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:11:57,421 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [9]
2026-08-10 07:11:57,590 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:11:57,591 INFO     29 [qwen-vl-text] LLM extraction start, text_len=51
2026-08-10 07:11:57,591 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:57,592 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 171, \"bbox_end\": 179, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "◆心电图12号 (心电图)\n检查医生：李天柱\n项目\n结果\n单位\n心电图\nT波异常\n科室小结：\nT波异常",
    "role": "user"
  }
]
2026-08-10 07:11:59,785 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:11:59,786 INFO     29 [qwen-vl-text] LLM output (len=323):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "心电图",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "项目\n结果\n单位\n心电图\nT波异常",
  "conclusion": "科室小结：\nT波异常",
  "physician": "李天柱",
  "reviewer": null
}
2026-08-10 07:11:59,789 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=718464, prompt_len=690
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共9行）
["◆心电图12号 (心电图)", "检查医生：李天柱", "项目", "结果", "单位", "心电图", "T波异常", "科室小结：", "T波异常"]

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
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord API raw response (len=450):
[
	{"text": "◆心电图12号 (心电图)", "bbox": [246, 591, 412, 606]},
	{"text": "检查医生：李天柱", "bbox": [620, 592, 744, 605]},
	{"text": "项目", "bbox": [245, 617, 270, 628]},
	{"text": "结果", "bbox": [384, 617, 412, 628]},
	{"text": "单位", "bbox": [763, 617, 789, 628]},
	{"text": "心电图", "bbox": [245, 639, 282, 650]},
	{"text": "T波异常", "bbox": [384, 639, 434, 650]},
	{"text": "科室小结：", "bbox": [245, 660, 300, 671]},
	{"text": "T波异常", "bbox": [384, 660, 434, 671]}
]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord API: raw_items=9, valid_items=9, elapsed=2.6s
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[0]: text=◆心电图12号 (心电图), bbox=[246, 591, 412, 606]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[1]: text=检查医生：李天柱, bbox=[620, 592, 744, 605]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[2]: text=项目, bbox=[245, 617, 270, 628]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[3]: text=结果, bbox=[384, 617, 412, 628]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[4]: text=单位, bbox=[763, 617, 789, 628]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[5]: text=心电图, bbox=[245, 639, 282, 650]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[6]: text=T波异常, bbox=[384, 639, 434, 650]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[7]: text=科室小结：, bbox=[245, 660, 300, 671]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] coord item[8]: text=T波异常, bbox=[384, 660, 434, 671]
2026-08-10 07:12:02,424 INFO     29 [qwen-vl-text] page=4 — 9/9 coords, api_time=2.6s
2026-08-10 07:12:02,425 INFO     29 [qwen-vl-text] new_positions (9):
[[4, 146.37, 245.14, 497.62199999999996, 510.252], [4, 368.9, 442.68, 498.464, 509.40999999999997], [4, 145.775, 160.65, 519.514, 528.776], [4, 228.48, 245.14, 519.514, 528.776], [4, 453.98499999999996, 469.455, 519.514, 528.776], [4, 145.775, 167.79, 538.038, 547.3], [4, 228.48, 258.22999999999996, 538.038, 547.3], [4, 145.775, 178.5, 555.72, 564.982], [4, 228.48, 258.22999999999996, 555.72, 564.982]]
2026-08-10 07:12:02,425 INFO     29 [qwen-vl-text] ═══ DONE ═══ 9 positions, pages=1, time=5.0s
2026-08-10 07:12:02,425 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 07:12:02,426 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 07:12:02,426 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 07:12:02,426 INFO     29 [qwen-vl-text] positions(11): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 07:12:02,427 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [11]
2026-08-10 07:12:02,600 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 07:12:02,601 INFO     29 [qwen-vl-text] LLM extraction start, text_len=142
2026-08-10 07:12:02,601 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:12:02,601 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 180, \"bbox_end\": 190, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "◆胸部正位检查DR(不出片) (DR拍片)\n检查医生：申静\n项目\n结果\n单位\n胸部正位检查（DR）\n胸廓对称，纵隔及气管居中，未见增宽。肺门形态、大小、位置未\n见异常。两肺纹理走行自然，未见明显异常密度影。心影形态、大\n小未见异常。两膈面光整，两肋膈角锐利。\n科室小结：\n未见明显异常",
    "role": "user"
  }
]
2026-08-10 07:12:04,416 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 07:12:04,417 INFO     29 [qwen-vl-text] LLM output (len=380):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "胸部正位检查DR",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "胸廓对称，纵隔及气管居中，未见增宽。肺门形态、大小、位置未见异常。两肺纹理走行自然，未见明显异常密度影。心影形态、大小未见异常。两膈面光整，两肋膈角锐利。",
  "conclusion": "未见明显异常",
  "physician": "申静",
  "reviewer": null
}
2026-08-10 07:12:04,419 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=718464, prompt_len=788
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共11行）
["◆胸部正位检查DR(不出片) (DR拍片)", "检查医生：申静", "项目", "结果", "单位", "胸部正位检查（DR）", "胸廓对称，纵隔及气管居中，未见增宽。肺门形态、大小、位置未", "见异常。两肺纹理走行自然，未见明显异常密度影。心影形态、大", "小未见异常。两膈面光整，两肋膈角锐利。", "科室小结：", "未见明显异常"]

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
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord API raw response (len=628):
[
	{"text": "◆胸部正位检查DR(不出片) (DR拍片)", "bbox": [245, 713, 517, 727]},
	{"text": "检查医生：申静", "bbox": [666, 713, 772, 726],
	{"text": "项目", "bbox": [245, 738, 270, 750]},
	{"text": "结果", "bbox": [384, 738, 412, 750]},
	{"text": "单位", "bbox": [763, 738, 790, 750]},
	{"text": "胸部正位检查（DR）", "bbox": [245, 760, 351, 771]},
	{"text": "胸廓对称，纵隔及气管居中，未见增宽。肺门形态、大小、位置未", "bbox": [385, 760, 751, 771]},
	{"text": "见异常。两肺纹理走行自然，未见明显异常密度影。心影形态、大", "bbox": [385, 781, 751, 793]},
	{"text": "小未见异常。两膈面光整，两肋膈角锐利。", "bbox": [385, 803, 618, 814]},
	{"text": "科室小结：", "bbox": [245, 824, 300, 836]},
	{"text": "未见明显异常", "bbox": [385, 824, 463, 836]}
]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord API: raw_items=11, valid_items=11, elapsed=3.6s
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[0]: text=◆胸部正位检查DR(不出片) (DR拍片), bbox=[245, 713, 517, 727]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[1]: text=检查医生：申静, bbox=[666, 713, 772, 726]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[2]: text=项目, bbox=[245, 738, 270, 750]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[3]: text=结果, bbox=[384, 738, 412, 750]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[4]: text=单位, bbox=[763, 738, 790, 750]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[5]: text=胸部正位检查（DR）, bbox=[245, 760, 351, 771]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[6]: text=胸廓对称，纵隔及气管居中，未见增宽。肺门形态、大小、位置未, bbox=[385, 760, 751, 771]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[7]: text=见异常。两肺纹理走行自然，未见明显异常密度影。心影形态、大, bbox=[385, 781, 751, 793]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[8]: text=小未见异常。两膈面光整，两肋膈角锐利。, bbox=[385, 803, 618, 814]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[9]: text=科室小结：, bbox=[245, 824, 300, 836]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] coord item[10]: text=未见明显异常, bbox=[385, 824, 463, 836]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] page=4 — 11/11 coords, api_time=3.6s
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] new_positions (11):
[[4, 145.775, 307.615, 600.346, 612.134], [4, 396.27, 459.34, 600.346, 611.292], [4, 145.775, 160.65, 621.396, 631.5], [4, 228.48, 245.14, 621.396, 631.5], [4, 453.98499999999996, 470.04999999999995, 621.396, 631.5], [4, 145.775, 208.845, 639.92, 649.182], [4, 229.075, 446.84499999999997, 639.92, 649.182], [4, 229.075, 446.84499999999997, 657.602, 667.706], [4, 229.075, 367.71, 676.126, 685.3879999999999], [4, 145.775, 178.5, 693.808, 703.9119999999999], [4, 229.075, 275.485, 693.808, 703.9119999999999]]
2026-08-10 07:12:07,984 INFO     29 [qwen-vl-text] ═══ DONE ═══ 11 positions, pages=1, time=5.6s
2026-08-10 07:12:07,993 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 07:12:07,993 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Extractor:ExaminationReport | outputs={"chunks": "4 items, types={'ExaminationReport': 4}", "html": "", "json": "394 items", "markdown": "", "text": "", "name": "LIQU高血糖郑州.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 13, \"chunks_Examination\": 4, \"chunks_Medication\": 2, \"chunks_Prescription\": 1}"}
2026-08-10 07:12:07,993 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 07:12:07,994 INFO     29 [ChunkMerger] Merged 22 chunks from 8 sources: {'Extractor:LabExam': 13, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 2, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 4} (filtered 3 noise chunks)
2026-08-10 07:12:08,146 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 07:12:08,146 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "22 items, types={'LabReport': 13, 'OutpatientRecord': 2, 'MedicationRecord': 2, 'PrescriptionRecord': 1, 'ExaminationReport': 4}", "name": "LIQU高血糖郑州.pdf"}
2026-08-10 07:12:08,147 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 07:12:08,259 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786345707439, 'update_date': datetime.datetime(2026, 8, 10, 7, 8, 27), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 815265, 'status': '1'}
2026-08-10 07:12:08,520 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白  2461  10  %  4.5~5.9  True    葡萄糖  1056  10.60  mmol/L  3.89~6.11  True   
---
   乙型肝炎病毒表面抗原  HBsAg  阳性  None  None  True    乙型肝炎病毒表面抗体  HBsAb  阴性  None  None  False    乙型肝炎病毒e抗原  HBeAg  阴性  None  None  False    乙型肝炎病毒e抗体  HBeAb  阳性  None  None  True    乙型肝炎病毒核心抗体  HBcAb  阳性  None  None  True   
---
   红细胞平均分布宽度标准差  None  42.6  fL  35.0-56.0  False    红细胞平均分布宽度变异系数  None  11.6  %  11.0-16.0  False   
---
   空腹血糖  None  16.93  mmol/L  3.89-6.11  True   
---
   尿酸  None  254.9  μmol/L  202-416  False    肌酐  None  57.0  μmol/L  57-97  False    尿素  None  3.29  mmol/L  3.6-9.5  True   
---
   丙氨酸氨基转移酶  None  43.7  U/L  9-50  False    门冬氨酸氨基转移酶  None  20.5  U/L  0-40  False    谷氨酰转肽酶  None  53.5  U/L  11-61  False    总蛋白  None  78.7  g/L  66-87  False    白蛋白  None  44.4  g/L  40-55  False    总胆红素  None  10.4  μmol/L  5.1-19  False    直接胆红素  None  2.6  μmol/L  1.7-6.8  False   
---
   酸碱度  None  5.5  None  5.4-8.4  False    亚硝酸盐  None  -  None  阴性  False   
---
   红细胞平均分布宽度标准差  None  42.6  fL  35.0-56.0  False    红细胞平均分布宽度变异系数  None  11.6  %  11.0-16.0  False   
---
   空腹血糖  None  16.93  mmol/L  3.89-6.11  True   
---
   尿酸  None  254.9  μmol/L  202-416  False    肌酐  None  57.0  μmol/L  57-97  False    尿素  None  3.29  mmol/L  3.6-9.5  True   
---
   丙氨酸氨基转移酶  None  43.7  U/L  9-50  False    门冬氨酸氨基转移酶  None  20.5  U/L  0-40  False    谷氨酰转肽酶  None  53.5  U/L  11-61  False    总蛋白  None  78.7  g/L  66-87  False    白蛋白  None  44.4  g/L  40-55  False    总胆红素  None  10.4  μmol/L  5.1-19  False    直接胆红素  None  2.6  μmol/L  1.7-6.8  False   
---
   酸碱度  None  5.5  None  5.4-8.4  False    亚硝酸盐  None  -  None  阴性  False   
---
   糖化血红蛋白  None  9  %  4.5~5.9  True    葡萄糖  None  11.15  mmol/L  3.89~6.11  True   
---
郑州市金水区国基路沙门社区卫生服务中心门诊电子病历
No: 20241116000027
就诊类型：初诊
科别：内科
就诊时间：2024/11/16 8:09:23
姓名：.
性别：男
年龄：27岁
电话：
家庭住址：沙门
药敏史：无
发病日期：
诊断：2型糖尿病
主诉：发现口渴.口干.多饮多尿.3个月余.
现病史：患者三个月前发现自己口渴.口干.多饮多尿自测空腹血糖
11.0mmol/L.规律口服二甲双胍每次0.5g每日三次 血糖控
制不理想.前来就诊
既往史：否认药物过敏史，否认传染病史。
体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，
心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，
肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射
未引出。
辅助检查：血糖10.6mmol/L. 糖化10%
初步诊断：二型糖尿病
处理措施：1.糖尿病饮食.2.适当运动.3.规律服用二甲双胍 4.定期复查
医师签名：李层
打印时间：2025/3/19 17:04:36
---
郑州市金水区国基路沙门社区卫生服务中心门诊电子病历
No: 20250417000042
就诊类型：初诊 科别：内科 就诊时间：2025/4/17 8:14:34
姓名： 性别：男 年龄：27岁 电话：13673657585
家庭住址：沙门 药敏史：无
发病日期：2025-04-17 诊断：糖尿病
主诉：患糖尿病1年余
现病史：患者1年前发现自己口渴，口干，多饮多尿，自测空腹血糖
11.0mmol/1，规律口服二甲双胍 每次0.5，每日三次，现来复查
就诊
既往史：否认药物过敏史，否认传染病史。
体格检查：神清、精神可，查体合作。双肺呼吸音清，未闻及干湿啰音，
心律齐，各瓣膜未闻及病理性杂音，腹软，无压痛，反跳痛，
肝脾肋下未触及，双下肢无水肿，生理性反射存在，病理反射
未引出。
辅助检查：血糖11.15mmol/1 糖化血红蛋白9%
初步诊断：二型糖尿病
处理措施：1，糖尿病饮食 保持心情愉悦 2，适量运动 3.继续规律服用 二
甲双胍片 4，定期检测血糖 5.不适随诊
医师签名：李层 打印时间：2025/4/22 17:08:28
健康管理部门
---
越人大药房
祝您身体健康
日期：2025-04-02 NO：1.2468223
会员：  会员卡：1004832
药品名称 数量 单位 单价 金额
盐酸二甲双胍 0.25*60 片
生产厂商：上海信谊
批号：
2 5.50 11.00
应收：11.00 收款：11.00
找零：0.00 找零：0.00
付款方式：现金 实收：11.00
收款：刘丽婷 时间：11：06：25
地址：三全路渠东路东岸尚景
电话：63222645
药品无质量问题概不退换！
2026-08-10 07:12:09,064 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=越人大药房
祝您身体健康
日期：2025-02-13 NO：1.2467129
会员：
会员卡：1004832
药品名称 数量 单位 单价 金额
盐酸二甲双胍 规格：0.25*60片
生产厂商：上海信宜
批号：
5 盒 5.50 27.50
应收：27.50 收款：27.50
找零：0.00 折扣：0.00
付款方式：a 现金 实收：27.50
收款：刘丽婷 时间：16:27:56
地址：三全路渠东路东岸尚景
电话：63222645
药品无质量问题概不退换！
---
郑州市金水区国基路沙门社区
卫生服务中心处方笺
医保证号:
费别:自费
门诊号:20250417000042
日期:2025-04-17
姓名:
性别:男
年龄:27岁
科别:内科
住址:沙门
临床诊断:糖尿病
Rp:
1 (基)(集)盐酸二甲双胍缓释片(0.5g*60S)
2瓶
用法:每次0.5g口服一天三次*30天
医师(签字/盖章):李层
审核、调配:
核对、发药:
药费:10.34
执行科室:西药房
打印日期:2025/04/17
---
金水区国基路沙门社区卫生服务中心
Jinshui Gaoji Street Shamen Community Health Services Center
0001
姓名：
条码号：1001241021000001
流借号：
胆
胆囊大小形态正常，壁光滑，囊内未见异常回声。胆总管内径无增
宽。
胰
胰腺形态、大小正常，内部光点均匀，主胰管无扩张。
脾
脾脏大小形态正常，实质回声均匀。
科室小结：
脂肪肝
---
◆泌尿系彩超（男）
(彩超检查)
检查医生：高培利
项目
结果
单位
双肾
双肾形态大小正常、包膜完整光滑，肾实质回声光点均匀，肾盂肾
盏未见扩张。
前列腺
前列腺形态大小正常，轮廓整齐，实质回声均匀。
膀胱
膀胱充盈欠佳，壁光滑，其内未见明显异常回声。
输尿管
输尿管未见显示扩张。
科室小结：
未见明显异常
---
◆心电图12号 (心电图)
检查医生：李天柱
项目
结果
单位
心电图
T波异常
科室小结：
T波异常
---
◆胸部正位检查DR(不出片) (DR拍片)
检查医生：申静
项目
结果
单位
胸部正位检查（DR）
胸廓对称，纵隔及气管居中，未见增宽。肺门形态、大小、位置未
见异常。两肺纹理走行自然，未见明显异常密度影。心影形态、大
小未见异常。两膈面光整，两肋膈角锐利。
科室小结：
未见明显异常
2026-08-10 07:12:09,472 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T07:12:09.471+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 10, "failed": 0, "current": {"48638ddc948a11f1bd9827cf206dfa2d": {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 07:12:09,656 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 07:12:09,657 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "22 items, types={'LabReport': 13, 'OutpatientRecord': 2, 'MedicationRecord': 2, 'PrescriptionRecord': 1, 'ExaminationReport': 4}", "name": "LIQU高血糖郑州.pdf", "embedding_token_consumption": 2818}
2026-08-10 07:12:09,657 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 07:12:09,994 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 07:12:09,994 INFO     29 [Trace] task=48638ddc | doc=LIQU高血糖郑州.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":17,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(2, 106, 180, 201, 215) row[-1]=(2, 106, 143, 218, 232)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=5 row[0]=(3, 135, 238, 468, 479) row[-1]=(3, 135, 238, 553, 564)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(4, 157, 240, 123, 133) row[-1]=(4, 157, 247, 142, 152)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 157, 196, 186, 198) row[-1]=(4, 157, 196, 186, 198)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(4, 158, 173, 309, 319) row[-1]=(4, 158, 173, 345, 355)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=7 row[0]=(4, 158, 214, 427, 436) row[-1]=(4, 158, 193, 537, 546)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(4, 159, 179, 620, 630) row[-1]=(4, 159, 186, 639, 649)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(6, 157, 240, 123, 133) row[-1]=(6, 157, 247, 142, 152)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(6, 157, 196, 186, 198) row[-1]=(6, 157, 196, 186, 198)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(6, 158, 173, 309, 318) row[-1]=(6, 158, 173, 346, 354)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=7 row[0]=(6, 158, 214, 427, 436) row[-1]=(6, 158, 193, 538, 546)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(6, 159, 179, 620, 630) row[-1]=(6, 159, 186, 639, 649)
2026-08-10 07:12:10,002 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(12, 102, 167, 214, 226) row[-1]=(12, 102, 135, 230, 242)
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,003 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 07:12:10,015 INFO     29 set_progress(48638ddc948a11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 07:12:10 [DOC Engine]:
Start to index...
2026-08-10 07:12:10,052 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.032s]
2026-08-10 07:12:10,057 INFO     29 set_progress(48638ddc948a11f1bd9827cf206dfa2d), progress: 0.8045454545454546, progress_msg: 
2026-08-10 07:12:10,091 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.027s]
2026-08-10 07:12:10,121 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.019s]
2026-08-10 07:12:10,147 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 07:12:10,184 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.028s]
2026-08-10 07:12:10,206 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 07:12:10,220 INFO     29 set_progress(48638ddc948a11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 07:12:10 Indexing done (0.21s). Task done (222.22s)
2026-08-10 07:12:10,228 INFO     29 [Done], chunks(22), token(2818), elapsed:222.22
2026-08-10 07:12:10,406 INFO     29 handle_task done for task {"id": "48638ddc948a11f1bd9827cf206dfa2d", "doc_id": "479f3c48948a11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "type": "pdf", "location": "LIQU\u9ad8\u8840\u7cd6\u90d1\u5dde.pdf", "size": 9592803, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786345706612, "task_type": "dataflow", "root_trace_id": "dfb21ad569bd41eb9566d076be6e8ba7", "root_traceparent": "00-dfb21ad569bd41eb9566d076be6e8ba7-09fd7afee4cde403-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
