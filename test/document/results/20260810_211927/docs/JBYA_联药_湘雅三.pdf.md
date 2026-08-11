# 基准结果：JBYA 联药 湘雅三.pdf

## 基本信息

- 文件：`JBYA 联药 湘雅三.pdf`
- 大小：775.7 KB
- PDF 总页数：8
- doc_id：`580c255294bf11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:28:14  完成时间：2026-08-10T21:30:29  耗时：135.0s
- progress_msg：`13:30:27 Indexing done (0.05s). Task done (122.18s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 214afe22 | 1 | 3-3 | 长沙市岳麓区观沙岭街道社区卫生服务中心 门诊病历 科室 门诊全科 就诊日期 20 |
| 2 | 08fea967 | 1 | 6-6 | 养天和大药房 流水号：806581202503230257 收银员：唐红娟 日期 |
| 3 | 05702d47 | 1 | 7-7 | 养天和大药房 流水号：806581202501220207 收银员：唐红娟 日期 |
| 4 | 1403c843 | 1 | 8-8 | 长沙市岳麓区观沙岭街道社区卫生服务中心 门诊病历 科室 门诊全科 就诊日期 20 |
| 5 | 7a7bd3b7 | 1 | 1-1 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 6 | 6952f5a4 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>GllbA1c</t |
| 7 | 6f85a621 | 1 | 4-4 | <table><tr><td>葡萄糖餐前</td><td>BS(餐前)</td> |
| 8 | 999ffd1d | 1 | 5-5 | <table><tr><td>GLU</td><td>GLU</td><td>1 |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：8
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8]`
- 覆盖页数：8 / 8；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 4 | 0 | 4 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"LabReport": 4, "OutpatientRecord": 2, "MedicationRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 8, "sources": 9, "stats": {"Extractor:LabExam": 4, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 2, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:30:26,313 INFO     29 [ChunkMerger] Merged 8 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:28:19,057 INFO     29 handle_task begin for task {"id": "583868d894bf11f1bd9827cf206dfa2d", "doc_id": "580c255294bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "type": "pdf", "location": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "size": 794325, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368496497, "task_type": "dataflow", "root_trace_id": "49d7d387da1c49cda1501856908b3841", "root_traceparent": "00-49d7d387da1c49cda1501856908b3841-5cab0f312536d09e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:28:19,262 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 13:28:19,384 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:28:19,392 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:28:19,393 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:28:19,393 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:28:19,397 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:28:19,397 INFO     29 ============================================================
2026-08-10 13:28:19,397 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:28:19,397 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:28:19,397 INFO     29 ============================================================
2026-08-10 13:28:19,397 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:28:19,397 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:28:19,399 INFO     29 No torch found.
2026-08-10 13:28:20,027 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=8
2026-08-10 13:28:20,095 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=367450, prompt_len=764
2026-08-10 13:28:21,440 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-03-01"
}
```
2026-08-10 13:28:21,441 INFO     29 [qwen-vl-parser] page=1 classify=table report_date=2025-03-01
2026-08-10 13:28:21,447 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=367450, prompt_len=756
2026-08-10 13:28:24,391 INFO     29 [qwen-vl-parser] table API response (len=576):
\begin{tabular}{ccccccc}
\hline
\multicolumn{7}{c}{\textbf{观沙岭街道社区卫生服务中心检验报告单}} \\
\hline
姓名: & & 送检科室: 全科门诊三 & 就诊类型: 门诊 & \multicolumn{3}{c}{标本类型: 全血} \\
性别: 女 & & 病历号: 20250301000049 & 送检医生: 朱素如 & \multicolumn{3}{c}{标本号: 2} \\
年龄: 59岁 & & 床号: & 临床诊断: 健康查体 & \multicolumn{3}{c}{} \\
\hline
\multicolumn{2}{c}{检验项目名称} & 英文名称 & 检验结果 & 状态 & 参考区间 & 单位 \\
\hline
1 & 糖化血红蛋白 & HbA1c & 9.93 & $\uparrow$ & 4.2-6.2 & \% \\
\hline
\end{tabular}

检验时间: 2025-03-01 09:10:45 \quad 审核时间: 2025-03-01 10:41:34 \\
备注: \\
注: 结合临床结果仅供参考, 此次结果仅对本次标本负责! \quad 检验者: 张雅琪 \quad 审核者: 夏美芳 \\
扫描全能王 创建
2026-08-10 13:28:24,394 INFO     29 [qwen-vl-parser] page=1 table: 18 LaTeX lines (bbox 0-17)
2026-08-10 13:28:24,394 INFO     29 [qwen-vl-parser] page=1 table: 18 sections
2026-08-10 13:28:24,488 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=426902, prompt_len=764
2026-08-10 13:28:25,827 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-04-01"
}
```
2026-08-10 13:28:25,827 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2024-04-01
2026-08-10 13:28:25,840 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=426902, prompt_len=756
2026-08-10 13:28:27,991 INFO     29 [qwen-vl-parser] table API response (len=389):
\begin{tabular}{cccccccc}
\hline
项目名称 & 英文 & 结果 & 单位 & 参考区间 & & & \\
\hline
1 & *糖化血红蛋白 & GllbA1c & 10.70 & ! & \% & 4.2-6.3 & \\
\hline
\end{tabular}

\begin{tabular}{llllllll}
采样时间: 2024/4/1 8:44:04 & 接收时间: 2024/4/1 & 09:22 & 检验者: & 甘柳亮 & 审核者: & 陈 & \\
检验时间: 2024-04-01 09:23 & 报告时间: 2024-04-01 09:43 & & & & & & \\
备 & 注: & & & & & & \\
\end{tabular}

声明: 此报告仅对所检验标本结果负责。项目名称前注“*”为互认项目。
2026-08-10 13:28:27,991 INFO     29 [qwen-vl-parser] page=2 table: 15 LaTeX lines (bbox 18-32)
2026-08-10 13:28:27,992 INFO     29 [qwen-vl-parser] page=2 table: 15 sections
2026-08-10 13:28:28,132 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=965886, prompt_len=764
2026-08-10 13:28:29,495 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-03-01"}
```
2026-08-10 13:28:29,495 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2025-03-01
2026-08-10 13:28:29,501 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=965886, prompt_len=401
2026-08-10 13:28:32,540 INFO     29 [qwen-vl-parser] text API response (len=561):
["长沙市岳麓区观沙岭街道社区卫生服务中心", "门诊病历", "科室", "门诊全科", "就诊日期", "2025-03-01", "就诊时间", "14:12:26", "姓名", "性别", "女", "年龄", "58岁", "联系电话", "身份证", "详细地址", "湖南省岳阳市湘阴县岭北镇夹洲村夹洲十组", "主诉", "糖尿病患者常规监测血糖。", "现病史", "患者诉多年前发现血糖高，伴有口干，多饮，多尿，在上级医院诊断“2型糖尿病”，血糖控制一般，", "血压控制良好，今前来常规复诊。", "既往史", "2型糖尿病，高血压2级", "个人史", "无", "家族史", "否认家族中有类似病史，否认家族中有其他遗传病史。", "过敏史", "无", "体格检查", "体温：36℃，血压：135/86mmHg，一般情况可，心肺腹（-）。", "辅助检查", "", "诊断", "1.诊断：2型糖尿病", "处理意见", "1.盐酸二甲双胍缓释片 0.5g 口服：1次1片 3次/日。", "苯磺酸氨氯地平片 5mg，口服：1次1片 1次/日。", "2.低盐低脂糖尿病饮食；", "3.注意监测血糖情况；", "4.糖尿病专科随诊，不适随诊。", "医生姓名：", "朱素如", ""]
2026-08-10 13:28:32,540 INFO     29 [qwen-vl-parser] page=3 text: 43 lines (bbox 33-75)
2026-08-10 13:28:32,540 INFO     29 [qwen-vl-parser] page=3 text: 43 sections
2026-08-10 13:28:32,624 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=418141, prompt_len=764
2026-08-10 13:28:33,924 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-04-01"
}
```
2026-08-10 13:28:33,925 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2024-04-01
2026-08-10 13:28:33,938 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=418141, prompt_len=756
2026-08-10 13:28:35,076 INFO     29 [qwen-vl-parser] table API response (len=186):
\begin{tabular}{cccccccc}
\hline
项目名称 & 英文 & 结果 & 单位 & 参考区间 \\
\hline
1 & 葡萄糖餐前 & BS(餐前) & 11.60 & mmol/L & 3.90-6.1 \\
2 & 空腹C肽 & CPS000 & 3.24 & ng/ml & 1.1-4.4 \\
\hline
\end{tabular}
2026-08-10 13:28:35,079 INFO     29 [qwen-vl-parser] page=4 table: 9 LaTeX lines (bbox 76-84)
2026-08-10 13:28:35,079 INFO     29 [qwen-vl-parser] page=4 table: 9 sections
2026-08-10 13:28:35,157 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=408864, prompt_len=764
2026-08-10 13:28:36,442 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-03-01"
}
```
2026-08-10 13:28:36,443 INFO     29 [qwen-vl-parser] page=5 classify=table report_date=2025-03-01
2026-08-10 13:28:36,460 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=408864, prompt_len=756
2026-08-10 13:28:39,695 INFO     29 [qwen-vl-parser] table API response (len=736):
\begin{tabular}{ccccccc}
\hline
\multicolumn{7}{c}{\textbf{观沙岭街道社区卫生服务中心检验报告单}} \\
\hline
\multicolumn{2}{l}{\textbf{送检科室: 全科门诊三}} & \multicolumn{2}{l}{\textbf{就诊类型: 门诊}} & \multicolumn{3}{l}{\textbf{标本类型: 血清}} \\
\multicolumn{2}{l}{\textbf{病历号: 20250301000049}} & \multicolumn{2}{l}{\textbf{送检医生: 朱素如}} & \multicolumn{3}{l}{\textbf{标本号: 14}} \\
\multicolumn{2}{l}{\textbf{年龄: 59岁}} & \multicolumn{2}{l}{\textbf{床号:}} & \multicolumn{3}{l}{\textbf{临床诊断: 健康查体}} \\
\hline
\textbf{检验项目名称} & \textbf{英文名称} & \textbf{检验结果} & \textbf{状态} & \textbf{参考区间} & \textbf{单位} & \\
\hline
1 & GLU & 12.67 & ! & 3.9-6.1 & mmol/L & \\
2 & OGTT 1h & 32.31 & ! & 3.89-11.1 & mmol/L & \\
3 & OGTT 2h & 32.20 & ! & 3.9-7.9 & mmol/L & \\
\hline
\end{tabular}
2026-08-10 13:28:39,697 INFO     29 [qwen-vl-parser] page=5 table: 16 LaTeX lines (bbox 85-100)
2026-08-10 13:28:39,698 INFO     29 [qwen-vl-parser] page=5 table: 16 sections
2026-08-10 13:28:39,813 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=861230, prompt_len=764
2026-08-10 13:28:41,272 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-03-23"}
```
2026-08-10 13:28:41,272 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2025-03-23
2026-08-10 13:28:41,288 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=861230, prompt_len=401
2026-08-10 13:28:45,875 INFO     29 [qwen-vl-parser] text API response (len=524):
["养天和大药房", "流水号：806581202503230257", "收银员：唐红娟", "日期：2025-03-23 10:21:15", "品名", "批号", "厂家/产地", "规格", "零售价", "数量", "金额", "优惠", "1 盐酸二甲双胍缓释片", "20051289", "悦康药业", "0.5g*30", "16.00", "6", "96.00", "0", "2.苯磺酸氨氯地平片", "20103551", "四川省百草生物药业", "5mg*24", "26.00", "3", "78.00", "0", "零售总额：174.00", "价格优惠： 0.00", "应收金额：174.00", "付款：174.00", "找零：0", "顾客姓名：姜必言", "会员卡号：8036545742", "会员积分：1253.50", "门店名称：岳麓区春江店", "门店地址：长沙市观沙岭街道春江郦城 S8-166", "门店电话：13308478346", "监督电话：0731-82961371", "药品属于特殊商品，无质量问题恕不退换！", "本小票只作为购货凭证使用，不作为报销凭据", ""]
2026-08-10 13:28:45,875 INFO     29 [qwen-vl-parser] page=6 text: 42 lines (bbox 101-142)
2026-08-10 13:28:45,875 INFO     29 [qwen-vl-parser] page=6 text: 42 sections
2026-08-10 13:28:45,989 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=870386, prompt_len=764
2026-08-10 13:28:47,455 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-01-22"}
```
2026-08-10 13:28:47,455 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2025-01-22
2026-08-10 13:28:47,463 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=870386, prompt_len=401
2026-08-10 13:28:48,163 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:28:48.160+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 50, "failed": 0, "current": {"583868d894bf11f1bd9827cf206dfa2d": {"id": "583868d894bf11f1bd9827cf206dfa2d", "doc_id": "580c255294bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "type": "pdf", "location": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "size": 794325, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368496497, "task_type": "dataflow", "root_trace_id": "49d7d387da1c49cda1501856908b3841", "root_traceparent": "00-49d7d387da1c49cda1501856908b3841-5cab0f312536d09e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:28:50,571 INFO     29 [qwen-vl-parser] text API response (len=523):
["养天和大药房", "流水号：806581202501220207", "收银员：唐红娟", "日期：2025-01-22 09:36:13", "品名", "批号", "厂家/产地", "规格", "零售价", "数量", "金额", "优惠", "1 盐酸二甲双胍缓释片", "20051289", "悦康药业", "0.5g*30", "16.00", "6", "96.00", "0", "2.苯磺酸氨氯地平片", "20103551", "四川省百草生物药业", "5mg*24", "26.00", "3", "78.00", "0", "零售总额：174.00", "价格优惠：0.00", "应收金额：174.00", "付款：174.00", "找零：0", "顾客姓名：姜必白", "会员卡号：8036545742", "会员积分：1035.60", "门店名称：岳麓区春江店", "门店地址：长沙市观沙岭街道春江郦城 S8-166", "门店电话：13308478346", "监督电话：0731-82961371", "药品属于特殊商品，无质量问题恕不退换！", "本小票只作为购货凭证使用，不作为报销凭据", ""]
2026-08-10 13:28:50,571 INFO     29 [qwen-vl-parser] page=7 text: 42 lines (bbox 143-184)
2026-08-10 13:28:50,572 INFO     29 [qwen-vl-parser] page=7 text: 42 sections
2026-08-10 13:28:50,721 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=984237, prompt_len=764
2026-08-10 13:28:52,197 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-04-02"}
```
2026-08-10 13:28:52,198 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2024-04-02
2026-08-10 13:28:52,220 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=984237, prompt_len=401
2026-08-10 13:28:55,058 INFO     29 [qwen-vl-parser] text API response (len=531):
["长沙市岳麓区观沙岭街道社区卫生服务中心", "门诊病历", "科室", "门诊全科", "就诊日期", "2024-04-02", "就诊时间", "09:32:37", "姓名", "性别", "女", "年龄", "57岁", "联系电话", "身份证", "详细地址", "观沙岭", "主诉", "糖尿病患者常规监测血糖及购药。", "现病史", "患者糖尿病多年，规律使用降糖药，血糖控制不住，血压控制良好，今前来常规监测血糖血压及", "购药。", "既往史", "2型糖尿病，高血压2级", "个人史", "", "家族史", "否认家族中有类似病史，否认家族中有其他遗传病史，否认家族性肿瘤病史。", "过敏史", "无", "体格检查", "体温：36℃，血压：132/89mmHg、一般情况可，心肺腹-。", "辅助检查", "", "诊断", "主诊断：2型糖尿病", "处理意见", "1.盐酸二甲双胍缓释片0.5g 口服：1次1片 3次/日。", "苯磺酸氨氯地平片5mg，口服：1次1片 1次/日。", "2.低盐低脂糖尿病饮食，适当锻炼，按时吃药。", "3.定时监测血压血糖血脂，不适随诊。", "医生姓名：", "刘成海"]
2026-08-10 13:28:55,058 INFO     29 [qwen-vl-parser] page=8 text: 41 lines (bbox 185-225)
2026-08-10 13:28:55,059 INFO     29 [qwen-vl-parser] page=8 text: 41 sections
2026-08-10 13:28:55,059 INFO     29 [qwen-vl-parser] parse_pdf done: 226 sections from 8 pages.
2026-08-10 13:28:55,072 INFO     29 Close text detector.
2026-08-10 13:28:55,500 INFO     29 Close text recognizer.
2026-08-10 13:28:55,913 INFO     29 Close recognizer.
2026-08-10 13:28:56,327 INFO     29 Close recognizer.
2026-08-10 13:28:56,783 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:28:56,783 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Parser:MedLink | outputs={"html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "json"}
2026-08-10 13:28:56,783 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:28:56,799 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:28:56,799 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] \\begin{tabular}{ccccccc}\n[BBOX-1] 报告时间: 2025-03-01\n[BBOX-2] \\hline\n[BBOX-3] \\multicolumn{7}{c}{\\textbf{观沙岭街道社区卫生服务中心检验报告单}} \\\\\n[BBOX-4] \\hline\n[BBOX-5] 姓名: & & 送检科室: 全科门诊三 & 就诊类型: 门诊 & \\multicolumn{3}{c}{标本类型: 全血} \\\\\n[BBOX-6] 性别: 女 & & 病历号: 20250301000049 & 送检医生: 朱素如 & \\multicolumn{3}{c}{标本号: 2} \\\\\n[BBOX-7] 年龄: 59岁 & & 床号: & 临床诊断: 健康查体 & \\multicolumn{3}{c}{} \\\\\n[BBOX-8] \\hline\n[BBOX-9] \\multicolumn{2}{c}{检验项目名称} & 英文名称 & 检验结果 & 状态 & 参考区间 & 单位 \\\\\n[BBOX-10] \\hline\n[BBOX-11] 1 & 糖化血红蛋白 & HbA1c & 9.93 & $\\uparrow$ & 4.2-6.2 & \\% \\\\\n[BBOX-12] \\hline\n[BBOX-13] \\end{tabular}\n[BBOX-14] 检验时间: 2025-03-01 09:10:45 \\quad 审核时间: 2025-03-01 10:41:34 \\\\\n[BBOX-15] 备注: \\\\\n[BBOX-16] 注: 结合临床结果仅供参考, 此次结果仅对本次标本负责! \\quad 检验者: 张雅琪 \\quad 审核者: 夏美芳 \\\\\n[BBOX-17] 扫描全能王 创建\n[BBOX-18] \\begin{tabular}{cccccccc}\n[BBOX-19] 报告时间: 2024-04-01\n[BBOX-20] \\hline\n[BBOX-21] 项目名称 & 英文 & 结果 & 单位 & 参考区间 & & & \\\\\n[BBOX-22] \\hline\n[BBOX-23] 1 & *糖化血红蛋白 & GllbA1c & 10.70 & ! & \\% & 4.2-6.3 & \\\\\n[BBOX-24] \\hline\n[BBOX-25] \\end{tabular}\n[BBOX-26] \\begin{tabular}{llllllll}\n[BBOX-27] 报告时间: 2024-04-01\n[BBOX-28] 采样时间: 2024/4/1 8:44:04 & 接收时间: 2024/4/1 & 09:22 & 检验者: & 甘柳亮 & 审核者: & 陈 & \\\\\n[BBOX-29] 检验时间: 2024-04-01 09:23 & 报告时间: 2024-04-01 09:43 & & & & & & \\\\\n[BBOX-30] 备 & 注: & & & & & & \\\\\n[BBOX-31] \\end{tabular}\n[BBOX-32] 声明: 此报告仅对所检验标本结果负责。项目名称前注“*”为互认项目。\n[BBOX-33] 长沙市岳麓区观沙岭街道社区卫生服务中心\n[BBOX-34] 门诊病历\n[BBOX-35] 科室\n[BBOX-36] 门诊全科\n[BBOX-37] 就诊日期\n[BBOX-38] 2025-03-01\n[BBOX-39] 就诊时间\n[BBOX-40] 14:12:26\n[BBOX-41] 姓名\n[BBOX-42] 性别\n[BBOX-43] 女\n[BBOX-44] 年龄\n[BBOX-45] 58岁\n[BBOX-46] 联系电话\n[BBOX-47] 身份证\n[BBOX-48] 详细地址\n[BBOX-49] 湖南省岳阳市湘阴县岭北镇夹洲村夹洲十组\n[BBOX-50] 主诉\n[BBOX-51] 糖尿病患者常规监测血糖。\n[BBOX-52] 现病史\n[BBOX-53] 患者诉多年前发现血糖高，伴有口干，多饮，多尿，在上级医院诊断“2型糖尿病”，血糖控制一般，\n[BBOX-54] 血压控制良好，今前来常规复诊。\n[BBOX-55] 既往史\n[BBOX-56] 2型糖尿病，高血压2级\n[BBOX-57] 个人史\n[BBOX-58] 无\n[BBOX-59] 家族史\n[BBOX-60] 否认家族中有类似病史，否认家族中有其他遗传病史。\n[BBOX-61] 过敏史\n[BBOX-62] 无\n[BBOX-63] 体格检查\n[BBOX-64] 体温：36℃，血压：135/86mmHg，一般情况可，心肺腹（-）。\n[BBOX-65] 辅助检查\n[BBOX-66] 诊断\n[BBOX-67] 1.诊断：2型糖尿病\n[BBOX-68] 处理意见\n[BBOX-69] 1.盐酸二甲双胍缓释片 0.5g 口服：1次1片 3次/日。\n[BBOX-70] 苯磺酸氨氯地平片 5mg，口服：1次1片 1次/日。\n[BBOX-71] 2.低盐低脂糖尿病饮食；\n[BBOX-72] 3.注意监测血糖情况；\n[BBOX-73] 4.糖尿病专科随诊，不适随诊。\n[BBOX-74] 医生姓名：\n[BBOX-75] 朱素如\n[BBOX-76] \\begin{tabular}{cccccccc}\n[BBOX-77] 报告时间: 2024-04-01\n[BBOX-78] \\hline\n[BBOX-79] 项目名称 & 英文 & 结果 & 单位 & 参考区间 \\\\\n[BBOX-80] \\hline\n[BBOX-81] 1 & 葡萄糖餐前 & BS(餐前) & 11.60 & mmol/L & 3.90-6.1 \\\\\n[BBOX-82] 2 & 空腹C肽 & CPS000 & 3.24 & ng/ml & 1.1-4.4 \\\\\n[BBOX-83] \\hline\n[BBOX-84] \\end{tabular}\n[BBOX-85] \\begin{tabular}{ccccccc}\n[BBOX-86] 报告时间: 2025-03-01\n[BBOX-87] \\hline\n[BBOX-88] \\multicolumn{7}{c}{\\textbf{观沙岭街道社区卫生服务中心检验报告单}} \\\\\n[BBOX-89] \\hline\n[BBOX-90] \\multicolumn{2}{l}{\\textbf{送检科室: 全科门诊三}} & \\multicolumn{2}{l}{\\textbf{就诊类型: 门诊}} & \\multicolumn{3}{l}{\\textbf{标本类型: 血清}} \\\\\n[BBOX-91] \\multicolumn{2}{l}{\\textbf{病历号: 20250301000049}} & \\multicolumn{2}{l}{\\textbf{送检医生: 朱素如}} & \\multicolumn{3}{l}{\\textbf{标本号: 14}} \\\\\n[BBOX-92] \\multicolumn{2}{l}{\\textbf{年龄: 59岁}} & \\multicolumn{2}{l}{\\textbf{床号:}} & \\multicolumn{3}{l}{\\textbf{临床诊断: 健康查体}} \\\\\n[BBOX-93] \\hline\n[BBOX-94] \\textbf{检验项目名称} & \\textbf{英文名称} & \\textbf{检验结果} & \\textbf{状态} & \\textbf{参考区间} & \\textbf{单位} & \\\\\n[BBOX-95] \\hline\n[BBOX-96] 1 & GLU & 12.67 & ! & 3.9-6.1 & mmol/L & \\\\\n[BBOX-97] 2 & OGTT 1h & 32.31 & ! & 3.89-11.1 & mmol/L & \\\\\n[BBOX-98] 3 & OGTT 2h & 32.20 & ! & 3.9-7.9 & mmol/L & \\\\\n[BBOX-99] \\hline\n[BBOX-100] \\end{tabular}\n[BBOX-101] 养天和大药房\n[BBOX-102] 流水号：806581202503230257\n[BBOX-103] 收银员：唐红娟\n[BBOX-104] 日期：2025-03-23 10:21:15\n[BBOX-105] 品名\n[BBOX-106] 批号\n[BBOX-107] 厂家/产地\n[BBOX-108] 规格\n[BBOX-109] 零售价\n[BBOX-110] 数量\n[BBOX-111] 金额\n[BBOX-112] 优惠\n[BBOX-113] 1 盐酸二甲双胍缓释片\n[BBOX-114] 20051289\n[BBOX-115] 悦康药业\n[BBOX-116] 0.5g*30\n[BBOX-117] 16.00\n[BBOX-118] 6\n[BBOX-119] 96.00\n[BBOX-120] 0\n[BBOX-121] 2.苯磺酸氨氯地平片\n[BBOX-122] 20103551\n[BBOX-123] 四川省百草生物药业\n[BBOX-124] 5mg*24\n[BBOX-125] 26.00\n[BBOX-126] 3\n[BBOX-127] 78.00\n[BBOX-128] 0\n[BBOX-129] 零售总额：174.00\n[BBOX-130] 价格优惠： 0.00\n[BBOX-131] 应收金额：174.00\n[BBOX-132] 付款：174.00\n[BBOX-133] 找零：0\n[BBOX-134] 顾客姓名：姜必言\n[BBOX-135] 会员卡号：8036545742\n[BBOX-136] 会员积分：1253.50\n[BBOX-137] 门店名称：岳麓区春江店\n[BBOX-138] 门店地址：长沙市观沙岭街道春江郦城 S8-166\n[BBOX-139] 门店电话：13308478346\n[BBOX-140] 监督电话：0731-82961371\n[BBOX-141] 药品属于特殊商品，无质量问题恕不退换！\n[BBOX-142] 本小票只作为购货凭证使用，不作为报销凭据\n[BBOX-143] 养天和大药房\n[BBOX-144] 流水号：806581202501220207\n[BBOX-145] 收银员：唐红娟\n[BBOX-146] 日期：2025-01-22 09:36:13\n[BBOX-147] 品名\n[BBOX-148] 批号\n[BBOX-149] 厂家/产地\n[BBOX-150] 规格\n[BBOX-151] 零售价\n[BBOX-152] 数量\n[BBOX-153] 金额\n[BBOX-154] 优惠\n[BBOX-155] 1 盐酸二甲双胍缓释片\n[BBOX-156] 20051289\n[BBOX-157] 悦康药业\n[BBOX-158] 0.5g*30\n[BBOX-159] 16.00\n[BBOX-160] 6\n[BBOX-161] 96.00\n[BBOX-162] 0\n[BBOX-163] 2.苯磺酸氨氯地平片\n[BBOX-164] 20103551\n[BBOX-165] 四川省百草生物药业\n[BBOX-166] 5mg*24\n[BBOX-167] 26.00\n[BBOX-168] 3\n[BBOX-169] 78.00\n[BBOX-170] 0\n[BBOX-171] 零售总额：174.00\n[BBOX-172] 价格优惠：0.00\n[BBOX-173] 应收金额：174.00\n[BBOX-174] 付款：174.00\n[BBOX-175] 找零：0\n[BBOX-176] 顾客姓名：姜必白\n[BBOX-177] 会员卡号：8036545742\n[BBOX-178] 会员积分：1035.60\n[BBOX-179] 门店名称：岳麓区春江店\n[BBOX-180] 门店地址：长沙市观沙岭街道春江郦城 S8-166\n[BBOX-181] 门店电话：13308478346\n[BBOX-182] 监督电话：0731-82961371\n[BBOX-183] 药品属于特殊商品，无质量问题恕不退换！\n[BBOX-184] 本小票只作为购货凭证使用，不作为报销凭据\n[BBOX-185] 长沙市岳麓区观沙岭街道社区卫生服务中心\n[BBOX-186] 门诊病历\n[BBOX-187] 科室\n[BBOX-188] 门诊全科\n[BBOX-189] 就诊日期\n[BBOX-190] 2024-04-02\n[BBOX-191] 就诊时间\n[BBOX-192] 09:32:37\n[BBOX-193] 姓名\n[BBOX-194] 性别\n[BBOX-195] 女\n[BBOX-196] 年龄\n[BBOX-197] 57岁\n[BBOX-198] 联系电话\n[BBOX-199] 身份证\n[BBOX-200] 详细地址\n[BBOX-201] 观沙岭\n[BBOX-202] 主诉\n[BBOX-203] 糖尿病患者常规监测血糖及购药。\n[BBOX-204] 现病史\n[BBOX-205] 患者糖尿病多年，规律使用降糖药，血糖控制不住，血压控制良好，今前来常规监测血糖血压及\n[BBOX-206] 购药。\n[BBOX-207] 既往史\n[BBOX-208] 2型糖尿病，高血压2级\n[BBOX-209] 个人史\n[BBOX-210] 家族史\n[BBOX-211] 否认家族中有类似病史，否认家族中有其他遗传病史，否认家族性肿瘤病史。\n[BBOX-212] 过敏史\n[BBOX-213] 无\n[BBOX-214] 体格检查\n[BBOX-215] 体温：36℃，血压：132/89mmHg、一般情况可，心肺腹-。\n[BBOX-216] 辅助检查\n[BBOX-217] 诊断\n[BBOX-218] 主诊断：2型糖尿病\n[BBOX-219] 处理意见\n[BBOX-220] 1.盐酸二甲双胍缓释片0.5g 口服：1次1片 3次/日。\n[BBOX-221] 苯磺酸氨氯地平片5mg，口服：1次1片 1次/日。\n[BBOX-222] 2.低盐低脂糖尿病饮食，适当锻炼，按时吃药。\n[BBOX-223] 3.定时监测血压血糖血脂，不适随诊。\n[BBOX-224] 医生姓名：\n[BBOX-225] 刘成海"
  }
]
2026-08-10 13:29:04,332 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:04,354 INFO     29 [SmartSplitter] SmartSplitter done: 8 chunks from 8 LLM segments (all bbox_id). Types: {'LabReport': 4, 'OutpatientRecord': 2, 'MedicationRecord': 2}
2026-08-10 13:29:04,363 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:29:04,363 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks": "8 items, types={'LabReport': 4, 'OutpatientRecord': 2, 'MedicationRecord': 2}"}
2026-08-10 13:29:04,363 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:29:04,363 INFO     29 [ChunkRouter] Routed 8 chunks into 3 groups: {'chunks_LabExam': 4, 'chunks_Clinical': 2, 'chunks_Medication': 2}
2026-08-10 13:29:04,370 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:29:04,370 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | ChunkRouter:Router | outputs={"html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks": "8 items, types={'LabReport': 4, 'OutpatientRecord': 2, 'MedicationRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:29:04,371 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:29:04,375 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:29:04,375 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:29:04,375 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[0]
2026-08-10 13:29:04,375 INFO     29 [qwen-vl-table] positions ： [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:29:04,473 INFO     29 [qwen-vl-table] page=0, rect=595x842, img=(1653x2339)
2026-08-10 13:29:04,474 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:04,474 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 0, \"bbox_end\": 17, \"encounter_dates\": [\"2025-03-01\"], \"department\": \"全科门诊三\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2025-03-01\n\\hline\n\\multicolumn{7}{c}{\\textbf{观沙岭街道社区卫生服务中心检验报告单}} \\\\\n\\hline\n姓名: & & 送检科室: 全科门诊三 & 就诊类型: 门诊 & \\multicolumn{3}{c}{标本类型: 全血} \\\\\n性别: 女 & & 病历号: 20250301000049 & 送检医生: 朱素如 & \\multicolumn{3}{c}{标本号: 2} \\\\\n年龄: 59岁 & & 床号: & 临床诊断: 健康查体 & \\multicolumn{3}{c}{} \\\\\n\\hline\n\\multicolumn{2}{c}{检验项目名称} & 英文名称 & 检验结果 & 状态 & 参考区间 & 单位 \\\\\n\\hline\n1 & 糖化血红蛋白 & HbA1c & 9.93 & $\\uparrow$ & 4.2-6.2 & \\% \\\\\n\\hline\n\\end{tabular}\n检验时间: 2025-03-01 09:10:45 \\quad 审核时间: 2025-03-01 10:41:34 \\\\\n备注: \\\\\n注: 结合临床结果仅供参考, 此次结果仅对本次标本负责! \\quad 检验者: 张雅琪 \\quad 审核者: 夏美芳 \\\\\n扫描全能王 创建",
    "role": "user"
  }
]
2026-08-10 13:29:05,801 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:05,801 INFO     29 [qwen-vl-table] page=0 LLM output (len=216):
{
  "report_date": "2025-03-01",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1c",
      "value": "9.93",
      "unit": "%",
      "reference_range": "4.2-6.2",
      "abnormal": true
    }
  ]
}
2026-08-10 13:29:05,802 INFO     29 [qwen-vl-table] coord grouping: {0: 1}
2026-08-10 13:29:05,803 INFO     29 [qwen-vl-table] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=404238, prompt_len=513
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白

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
2026-08-10 13:29:07,282 INFO     29 [qwen-vl-table] coord API raw response (len=64):
```json
[
	{"text": "糖化血红蛋白", "bbox": [94, 355, 196, 368]}
]
```
2026-08-10 13:29:07,282 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 13:29:07,282 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[94, 355, 196, 368]
2026-08-10 13:29:07,283 INFO     29 [qwen-vl-table] page=0 coord: matched 1/1, time=1.5s
2026-08-10 13:29:07,283 INFO     29 [qwen-vl-table] new_positions (1):
[[1, 55.93, 116.61999999999999, 298.90999999999997, 309.856]]
2026-08-10 13:29:07,283 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.9s
2026-08-10 13:29:07,285 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:29:07,287 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:29:07,287 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[1]
2026-08-10 13:29:07,287 INFO     29 [qwen-vl-table] positions ： [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:29:07,411 INFO     29 [qwen-vl-table] page=1, rect=595x842, img=(1653x2339)
2026-08-10 13:29:07,411 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:07,412 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 18, \"bbox_end\": 32, \"encounter_dates\": [\"2024-04-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccc}\n报告时间: 2024-04-01\n\\hline\n项目名称 & 英文 & 结果 & 单位 & 参考区间 & & & \\\\\n\\hline\n1 & *糖化血红蛋白 & GllbA1c & 10.70 & ! & \\% & 4.2-6.3 & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{llllllll}\n报告时间: 2024-04-01\n采样时间: 2024/4/1 8:44:04 & 接收时间: 2024/4/1 & 09:22 & 检验者: & 甘柳亮 & 审核者: & 陈 & \\\\\n检验时间: 2024-04-01 09:23 & 报告时间: 2024-04-01 09:43 & & & & & & \\\\\n备 & 注: & & & & & & \\\\\n\\end{tabular}\n声明: 此报告仅对所检验标本结果负责。项目名称前注“*”为互认项目。",
    "role": "user"
  }
]
2026-08-10 13:29:08,646 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:08,646 INFO     29 [qwen-vl-table] page=1 LLM output (len=219):
{
  "report_date": "2024-04-01",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "GllbA1c",
      "value": "10.70",
      "unit": "%",
      "reference_range": "4.2-6.3",
      "abnormal": true
    }
  ]
}
2026-08-10 13:29:08,647 INFO     29 [qwen-vl-table] coord grouping: {1: 1}
2026-08-10 13:29:08,647 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=498347, prompt_len=513
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白

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
2026-08-10 13:29:10,085 INFO     29 [qwen-vl-table] coord API raw response (len=64):
```json
[
	{"text": "糖化血红蛋白", "bbox": [125, 93, 224, 106]}
]
```
2026-08-10 13:29:10,085 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.4s
2026-08-10 13:29:10,085 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[125, 93, 224, 106]
2026-08-10 13:29:10,086 INFO     29 [qwen-vl-table] page=1 coord: matched 1/1, time=1.4s
2026-08-10 13:29:10,086 INFO     29 [qwen-vl-table] new_positions (1):
[[2, 74.375, 133.28, 78.306, 89.252]]
2026-08-10 13:29:10,086 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.8s
2026-08-10 13:29:10,086 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:29:10,087 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:29:10,087 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:29:10,087 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:29:10,205 INFO     29 [qwen-vl-table] page=3, rect=595x842, img=(1653x2339)
2026-08-10 13:29:10,205 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:10,206 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 76, \"bbox_end\": 84, \"encounter_dates\": [\"2024-04-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccccc}\n报告时间: 2024-04-01\n\\hline\n项目名称 & 英文 & 结果 & 单位 & 参考区间 \\\\\n\\hline\n1 & 葡萄糖餐前 & BS(餐前) & 11.60 & mmol/L & 3.90-6.1 \\\\\n2 & 空腹C肽 & CPS000 & 3.24 & ng/ml & 1.1-4.4 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:29:11,890 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:11,890 INFO     29 [qwen-vl-table] page=3 LLM output (len=393):
{
  "report_date": "2024-04-01",
  "items": [
    {
      "name": "葡萄糖餐前",
      "item_code": "BS(餐前)",
      "value": "11.60",
      "unit": "mmol/L",
      "reference_range": "3.90-6.1",
      "abnormal": true
    },
    {
      "name": "空腹C肽",
      "item_code": "CPS000",
      "value": "3.24",
      "unit": "ng/ml",
      "reference_range": "1.1-4.4",
      "abnormal": false
    }
  ]
}
2026-08-10 13:29:11,890 INFO     29 [qwen-vl-table] coord grouping: {3: 2}
2026-08-10 13:29:11,891 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=474993, prompt_len=517
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
葡萄糖餐前、空腹C肽

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
2026-08-10 13:29:15,014 INFO     29 [qwen-vl-table] coord API raw response (len=110):
```json
[
	{"text": "葡萄糖餐前", "bbox": [97, 88, 175, 100]},
	{"text": "空腹C肽", "bbox": [97, 102, 152, 114]}
]
```
2026-08-10 13:29:15,014 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=3.1s
2026-08-10 13:29:15,015 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖餐前, bbox=[97, 88, 175, 100]
2026-08-10 13:29:15,015 INFO     29 [qwen-vl-table] coord item[1]: text=空腹C肽, bbox=[97, 102, 152, 114]
2026-08-10 13:29:15,015 INFO     29 [qwen-vl-table] page=3 coord: matched 2/2, time=3.1s
2026-08-10 13:29:15,015 INFO     29 [qwen-vl-table] new_positions (2):
[[4, 57.714999999999996, 104.125, 74.096, 84.2], [4, 57.714999999999996, 90.44, 85.884, 95.988]]
2026-08-10 13:29:15,015 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=4.9s
2026-08-10 13:29:15,016 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:29:15,018 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:29:15,018 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[4]
2026-08-10 13:29:15,018 INFO     29 [qwen-vl-table] positions ： [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:29:15,129 INFO     29 [qwen-vl-table] page=4, rect=595x842, img=(1653x2339)
2026-08-10 13:29:15,129 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:15,129 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 85, \"bbox_end\": 100, \"encounter_dates\": [\"2025-03-01\"], \"department\": \"全科门诊三\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2025-03-01\n\\hline\n\\multicolumn{7}{c}{\\textbf{观沙岭街道社区卫生服务中心检验报告单}} \\\\\n\\hline\n\\multicolumn{2}{l}{\\textbf{送检科室: 全科门诊三}} & \\multicolumn{2}{l}{\\textbf{就诊类型: 门诊}} & \\multicolumn{3}{l}{\\textbf{标本类型: 血清}} \\\\\n\\multicolumn{2}{l}{\\textbf{病历号: 20250301000049}} & \\multicolumn{2}{l}{\\textbf{送检医生: 朱素如}} & \\multicolumn{3}{l}{\\textbf{标本号: 14}} \\\\\n\\multicolumn{2}{l}{\\textbf{年龄: 59岁}} & \\multicolumn{2}{l}{\\textbf{床号:}} & \\multicolumn{3}{l}{\\textbf{临床诊断: 健康查体}} \\\\\n\\hline\n\\textbf{检验项目名称} & \\textbf{英文名称} & \\textbf{检验结果} & \\textbf{状态} & \\textbf{参考区间} & \\textbf{单位} & \\\\\n\\hline\n1 & GLU & 12.67 & ! & 3.9-6.1 & mmol/L & \\\\\n2 & OGTT 1h & 32.31 & ! & 3.89-11.1 & mmol/L & \\\\\n3 & OGTT 2h & 32.20 & ! & 3.9-7.9 & mmol/L & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:29:17,517 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:17,518 INFO     29 [qwen-vl-table] page=4 LLM output (len=569):
{
  "report_date": "2025-03-01",
  "items": [
    {
      "name": "GLU",
      "item_code": "GLU",
      "value": "12.67",
      "unit": "mmol/L",
      "reference_range": "3.9-6.1",
      "abnormal": true
    },
    {
      "name": "OGTT 1h",
      "item_code": "OGTT 1h",
      "value": "32.31",
      "unit": "mmol/L",
      "reference_range": "3.89-11.1",
      "abnormal": true
    },
    {
      "name": "OGTT 2h",
      "item_code": "OGTT 2h",
      "value": "32.20",
      "unit": "mmol/L",
      "reference_range": "3.9-7.9",
      "abnormal": true
    }
  ]
}
2026-08-10 13:29:17,518 INFO     29 [qwen-vl-table] coord grouping: {4: 3}
2026-08-10 13:29:17,520 INFO     29 [qwen-vl-table] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=442474, prompt_len=526
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
GLU、OGTT 1h、OGTT 2h

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
2026-08-10 13:29:19,532 INFO     29 [qwen-vl-table] coord API raw response (len=166):
```json
[
	{"text": "GLU", "bbox": [328, 363, 357, 375]},
	{"text": "OGTT 1h", "bbox": [328, 380, 391, 393]},
	{"text": "OGTT 2h", "bbox": [328, 398, 391, 410]}
]
```
2026-08-10 13:29:19,533 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=2.0s
2026-08-10 13:29:19,533 INFO     29 [qwen-vl-table] coord item[0]: text=GLU, bbox=[328, 363, 357, 375]
2026-08-10 13:29:19,533 INFO     29 [qwen-vl-table] coord item[1]: text=OGTT 1h, bbox=[328, 380, 391, 393]
2026-08-10 13:29:19,533 INFO     29 [qwen-vl-table] coord item[2]: text=OGTT 2h, bbox=[328, 398, 391, 410]
2026-08-10 13:29:19,534 INFO     29 [qwen-vl-table] page=4 coord: matched 3/3, time=2.0s
2026-08-10 13:29:19,534 INFO     29 [qwen-vl-table] new_positions (3):
[[5, 195.16, 212.415, 305.646, 315.75], [5, 195.16, 232.64499999999998, 319.96, 330.906], [5, 195.16, 232.64499999999998, 335.116, 345.21999999999997]]
2026-08-10 13:29:19,534 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=4.5s
2026-08-10 13:29:19,549 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:29:19,549 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:LabExam | outputs={"chunks": "4 items, types={'LabReport': 4}", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:29:19,549 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:29:19,557 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:19,557 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:29:19,645 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:29:19.643+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 50, "failed": 0, "current": {"583868d894bf11f1bd9827cf206dfa2d": {"id": "583868d894bf11f1bd9827cf206dfa2d", "doc_id": "580c255294bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "type": "pdf", "location": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "size": 794325, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368496497, "task_type": "dataflow", "root_trace_id": "49d7d387da1c49cda1501856908b3841", "root_traceparent": "00-49d7d387da1c49cda1501856908b3841-5cab0f312536d09e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:29:19,987 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:19,998 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:29:19,998 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:29:19,999 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:29:20,007 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:29:20,008 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:29:20,008 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:29:20,008 INFO     29 [qwen-vl-text] positions(43): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:29:20,008 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [43]
2026-08-10 13:29:20,162 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:29:20,164 INFO     29 [qwen-vl-text] LLM extraction start, text_len=423
2026-08-10 13:29:20,164 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:20,166 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 33, \"bbox_end\": 75, \"encounter_dates\": [\"2025-03-01\"], \"department\": \"门诊全科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "长沙市岳麓区观沙岭街道社区卫生服务中心\n门诊病历\n科室\n门诊全科\n就诊日期\n2025-03-01\n就诊时间\n14:12:26\n姓名\n性别\n女\n年龄\n58岁\n联系电话\n身份证\n详细地址\n湖南省岳阳市湘阴县岭北镇夹洲村夹洲十组\n主诉\n糖尿病患者常规监测血糖。\n现病史\n患者诉多年前发现血糖高，伴有口干，多饮，多尿，在上级医院诊断“2型糖尿病”，血糖控制一般，\n血压控制良好，今前来常规复诊。\n既往史\n2型糖尿病，高血压2级\n个人史\n无\n家族史\n否认家族中有类似病史，否认家族中有其他遗传病史。\n过敏史\n无\n体格检查\n体温：36℃，血压：135/86mmHg，一般情况可，心肺腹（-）。\n辅助检查\n诊断\n1.诊断：2型糖尿病\n处理意见\n1.盐酸二甲双胍缓释片 0.5g 口服：1次1片 3次/日。\n苯磺酸氨氯地平片 5mg，口服：1次1片 1次/日。\n2.低盐低脂糖尿病饮食；\n3.注意监测血糖情况；\n4.糖尿病专科随诊，不适随诊。\n医生姓名：\n朱素如",
    "role": "user"
  }
]
2026-08-10 13:29:22,442 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:22,442 INFO     29 [qwen-vl-text] LLM output (len=367):
{
  "encounter_date": "2025-03-01",
  "chief_complaint": "糖尿病患者常规监测血糖。",
  "present_illness": "患者诉多年前发现血糖高，伴有口干，多饮，多尿，在上级医院诊断“2型糖尿病”，血糖控制一般，血压控制良好，今前来常规复诊。",
  "past_history": "2型糖尿病，高血压2级",
  "diagnosis": "2型糖尿病",
  "treatment_plan": [
    "盐酸二甲双胍缓释片 0.5g 口服：1次1片 3次/日。",
    "苯磺酸氨氯地平片 5mg，口服：1次1片 1次/日。",
    "低盐低脂糖尿病饮食；",
    "注意监测血糖情况；",
    "糖尿病专科随诊，不适随诊。"
  ]
}
2026-08-10 13:29:22,442 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-01]
2026-08-10 13:29:22,444 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1233439, prompt_len=1165
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["长沙市岳麓区观沙岭街道社区卫生服务中心", "门诊病历", "科室", "门诊全科", "就诊日期", "2025-03-01", "就诊时间", "14:12:26", "姓名", "性别", "女", "年龄", "58岁", "联系电话", "身份证", "详细地址", "湖南省岳阳市湘阴县岭北镇夹洲村夹洲十组", "主诉", "糖尿病患者常规监测血糖。", "现病史", "患者诉多年前发现血糖高，伴有口干，多饮，多尿，在上级医院诊断“2型糖尿病”，血糖控制一般，", "血压控制良好，今前来常规复诊。", "既往史", "2型糖尿病，高血压2级", "个人史", "无", "家族史", "否认家族中有类似病史，否认家族中有其他遗传病史。", "过敏史", "无", "体格检查", "体温：36℃，血压：135/86mmHg，一般情况可，心肺腹（-）。", "辅助检查", "诊断", "1.诊断：2型糖尿病", "处理意见", "1.盐酸二甲双胍缓释片 0.5g 口服：1次1片 3次/日。", "苯磺酸氨氯地平片 5mg，口服：1次1片 1次/日。", "2.低盐低脂糖尿病饮食；", "3.注意监测血糖情况；", "4.糖尿病专科随诊，不适随诊。", "医生姓名：", "朱素如"]

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
2026-08-10 13:29:34,617 INFO     29 [qwen-vl-text] coord API raw response (len=2314):
[
	{"text": "长沙市岳麓区观沙岭街道社区卫生服务中心", "bbox": [270, 69, 729, 90]},
	{"text": "门诊病历", "bbox": [464, 96, 534, 110]},
	{"text": "科室", "bbox": [109, 123, 144, 137]},
	{"text": "门诊全科", "bbox": [227, 124, 298, 138]},
	{"text": "就诊日期", "bbox": [373, 125, 444, 138]},
	{"text": "2025-03-01", "bbox": [520, 127, 606, 139]},
	{"text": "就诊时间", "bbox": [669, 127, 739, 140]},
	{"text": "14:12:26", "bbox": [775, 129, 845, 141]},
	{"text": "姓名", "bbox": [107, 159, 142, 172]},
	{"text": "性别", "bbox": [357, 161, 393, 174]},
	{"text": "女", "bbox": [440, 161, 458, 175]},
	{"text": "年龄", "bbox": [505, 162, 540, 175]},
	{"text": "58岁", "bbox": [584, 163, 623, 176]},
	{"text": "联系电话", "bbox": [668, 164, 739, 177]},
	{"text": "身份证", "bbox": [102, 195, 152, 209]},
	{"text": "详细地址", "bbox": [94, 232, 163, 246]},
	{"text": "湖南省岳阳市湘阴县岭北镇夹洲村夹洲十组", "bbox": [203, 233, 533, 249]},
	{"text": "主诉", "bbox": [114, 268, 148, 282]},
	{"text": "糖尿病患者常规监测血糖。", "bbox": [205, 269, 404, 284]},
	{"text": "现病史", "bbox": [108, 315, 160, 329]},
	{"text": "患者诉多年前发现血糖高，伴有口干，多饮，多尿，在上级医院诊断“2型糖尿病”，血糖控制一般，", "bbox": [207, 304, 923, 324]},
	{"text": "血压控制良好，今前来常规复诊。", "bbox": [210, 329, 458, 344]},
	{"text": "既往史", "bbox": [110, 362, 163, 375]},
	{"text": "2型糖尿病，高血压2级", "bbox": [210, 364, 395, 378]},
	{"text": "个人史", "bbox": [112, 398, 163, 411]},
	{"text": "无", "bbox": [212, 399, 231, 412]},
	{"text": "家族史", "bbox": [113, 433, 164, 446]},
	{"text": "否认家族中有类似病史，否认家族中有其他遗传病史。", "bbox": [214, 434, 610, 449]},
	{"text": "过敏史", "bbox": [113, 467, 165, 480]},
	{"text": "无", "bbox": [215, 468, 233, 481]},
	{"text": "体格检查", "bbox": [105, 507, 172, 520]},
	{"text": "体温：36℃，血压：135/86mmHg，一般情况可，心肺腹（-）。", "bbox": [215, 495, 662, 511]},
	{"text": "辅助检查", "bbox": [105, 545, 172, 558]},
	{"text": "诊断", "bbox": [122, 579, 156, 592]},
	{"text": "1.诊断：2型糖尿病", "bbox": [219, 579, 364, 593]},
	{"text": "处理意见", "bbox": [104, 688, 172, 701]},
	{"text": "1.盐酸二甲双胍缓释片 0.5g 口服：1次1片 3次/日。", "bbox": [215, 614, 637, 629]},
	{"text": "苯磺酸氨氯地平片 5mg，口服：1次1片 1次/日。", "bbox": [233, 638, 610, 653]},
	{"text": "2.低盐低脂糖尿病饮食；", "bbox": [214, 663, 392, 676]},
	{"text": "3.注意监测血糖情况；", "bbox": [214, 687, 375, 700]},
	{"text": "4.糖尿病专科随诊，不适随诊。", "bbox": [214, 710, 444, 724]},
	{"text": "医生姓名：", "bbox": [345, 789, 420, 802]},
	{"text": "朱素如", "bbox": [464, 790, 515, 804]}
]
2026-08-10 13:29:34,618 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=12.2s
2026-08-10 13:29:34,618 INFO     29 [qwen-vl-text] coord item[0]: text=长沙市岳麓区观沙岭街道社区卫生服务中心, bbox=[270, 69, 729, 90]
2026-08-10 13:29:34,618 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[464, 96, 534, 110]
2026-08-10 13:29:34,618 INFO     29 [qwen-vl-text] coord item[2]: text=科室, bbox=[109, 123, 144, 137]
2026-08-10 13:29:34,618 INFO     29 [qwen-vl-text] coord item[3]: text=门诊全科, bbox=[227, 124, 298, 138]
2026-08-10 13:29:34,618 INFO     29 [qwen-vl-text] coord item[4]: text=就诊日期, bbox=[373, 125, 444, 138]
2026-08-10 13:29:34,618 INFO     29 [qwen-vl-text] coord item[5]: text=2025-03-01, bbox=[520, 127, 606, 139]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[6]: text=就诊时间, bbox=[669, 127, 739, 140]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[7]: text=14:12:26, bbox=[775, 129, 845, 141]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[8]: text=姓名, bbox=[107, 159, 142, 172]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[9]: text=性别, bbox=[357, 161, 393, 174]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[10]: text=女, bbox=[440, 161, 458, 175]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[11]: text=年龄, bbox=[505, 162, 540, 175]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[12]: text=58岁, bbox=[584, 163, 623, 176]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[13]: text=联系电话, bbox=[668, 164, 739, 177]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[14]: text=身份证, bbox=[102, 195, 152, 209]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[15]: text=详细地址, bbox=[94, 232, 163, 246]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[16]: text=湖南省岳阳市湘阴县岭北镇夹洲村夹洲十组, bbox=[203, 233, 533, 249]
2026-08-10 13:29:34,619 INFO     29 [qwen-vl-text] coord item[17]: text=主诉, bbox=[114, 268, 148, 282]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[18]: text=糖尿病患者常规监测血糖。, bbox=[205, 269, 404, 284]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[19]: text=现病史, bbox=[108, 315, 160, 329]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[20]: text=患者诉多年前发现血糖高，伴有口干，多饮，多尿，在上级医院诊断“2型糖尿病”，血糖控制一般，, bbox=[207, 304, 923, 324]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[21]: text=血压控制良好，今前来常规复诊。, bbox=[210, 329, 458, 344]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[22]: text=既往史, bbox=[110, 362, 163, 375]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[23]: text=2型糖尿病，高血压2级, bbox=[210, 364, 395, 378]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[24]: text=个人史, bbox=[112, 398, 163, 411]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[25]: text=无, bbox=[212, 399, 231, 412]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[26]: text=家族史, bbox=[113, 433, 164, 446]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[27]: text=否认家族中有类似病史，否认家族中有其他遗传病史。, bbox=[214, 434, 610, 449]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[28]: text=过敏史, bbox=[113, 467, 165, 480]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[29]: text=无, bbox=[215, 468, 233, 481]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[30]: text=体格检查, bbox=[105, 507, 172, 520]
2026-08-10 13:29:34,620 INFO     29 [qwen-vl-text] coord item[31]: text=体温：36℃，血压：135/86mmHg，一般情况可，心肺腹（-）。, bbox=[215, 495, 662, 511]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[32]: text=辅助检查, bbox=[105, 545, 172, 558]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[33]: text=诊断, bbox=[122, 579, 156, 592]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[34]: text=1.诊断：2型糖尿病, bbox=[219, 579, 364, 593]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[35]: text=处理意见, bbox=[104, 688, 172, 701]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[36]: text=1.盐酸二甲双胍缓释片 0.5g 口服：1次1片 3次/日。, bbox=[215, 614, 637, 629]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[37]: text=苯磺酸氨氯地平片 5mg，口服：1次1片 1次/日。, bbox=[233, 638, 610, 653]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[38]: text=2.低盐低脂糖尿病饮食；, bbox=[214, 663, 392, 676]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[39]: text=3.注意监测血糖情况；, bbox=[214, 687, 375, 700]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[40]: text=4.糖尿病专科随诊，不适随诊。, bbox=[214, 710, 444, 724]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[41]: text=医生姓名：, bbox=[345, 789, 420, 802]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] coord item[42]: text=朱素如, bbox=[464, 790, 515, 804]
2026-08-10 13:29:34,621 INFO     29 [qwen-vl-text] page=2 — 43/43 coords, api_time=12.2s
2026-08-10 13:29:34,622 INFO     29 [qwen-vl-text] new_positions (43):
[[2, 160.65, 433.755, 58.098, 75.78], [2, 276.08, 317.72999999999996, 80.832, 92.61999999999999], [2, 64.855, 85.67999999999999, 103.566, 115.354], [2, 135.065, 177.31, 104.408, 116.196], [2, 221.935, 264.18, 105.25, 116.196], [2, 309.4, 360.57, 106.934, 117.038], [2, 398.055, 439.705, 106.934, 117.88], [2, 461.125, 502.775, 108.618, 118.722], [2, 63.665, 84.49, 133.878, 144.82399999999998], [2, 212.415, 233.83499999999998, 135.56199999999998, 146.50799999999998], [2, 261.8, 272.51, 135.56199999999998, 147.35], [2, 300.47499999999997, 321.3, 136.404, 147.35], [2, 347.47999999999996, 370.685, 137.246, 148.192], [2, 397.46, 439.705, 138.088, 149.034], [2, 60.69, 90.44, 164.19, 175.97799999999998], [2, 55.93, 96.985, 195.344, 207.132], [2, 120.785, 317.135, 196.186, 209.658], [2, 67.83, 88.06, 225.656, 237.444], [2, 121.975, 240.38, 226.498, 239.128], [2, 64.25999999999999, 95.19999999999999, 265.23, 277.018], [2, 123.16499999999999, 549.185, 255.968, 272.808], [2, 124.94999999999999, 272.51, 277.018, 289.64799999999997], [2, 65.45, 96.985, 304.804, 315.75], [2, 124.94999999999999, 235.02499999999998, 306.488, 318.276], [2, 66.64, 96.985, 335.116, 346.062], [2, 126.14, 137.445, 335.95799999999997, 346.904], [2, 67.235, 97.58, 364.586, 375.532], [2, 127.33, 362.95, 365.428, 378.058], [2, 67.235, 98.175, 393.214, 404.15999999999997], [2, 127.925, 138.635, 394.056, 405.002], [2, 62.474999999999994, 102.33999999999999, 426.894, 437.84], [2, 127.925, 393.89, 416.78999999999996, 430.262], [2, 62.474999999999994, 102.33999999999999, 458.89, 469.83599999999996], [2, 72.59, 92.82, 487.518, 498.464], [2, 130.305, 216.57999999999998, 487.518, 499.306], [2, 61.879999999999995, 102.33999999999999, 579.2959999999999, 590.242], [2, 127.925, 379.015, 516.9879999999999, 529.6179999999999], [2, 138.635, 362.95, 537.196, 549.826], [2, 127.33, 233.23999999999998, 558.246, 569.192], [2, 127.33, 223.125, 578.454, 589.4], [2, 127.33, 264.18, 597.8199999999999, 609.608], [2, 205.27499999999998, 249.89999999999998, 664.338, 675.284], [2, 276.08, 306.425, 665.18, 676.968]]
2026-08-10 13:29:34,622 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=14.6s
2026-08-10 13:29:34,622 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:29:34,624 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:29:34,625 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:29:34,625 INFO     29 [qwen-vl-text] positions(41): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:29:34,625 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [41]
2026-08-10 13:29:34,792 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:29:34,794 INFO     29 [qwen-vl-text] LLM extraction start, text_len=399
2026-08-10 13:29:34,794 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:34,795 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 185, \"bbox_end\": 225, \"encounter_dates\": [\"2024-04-02\"], \"department\": \"门诊全科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "长沙市岳麓区观沙岭街道社区卫生服务中心\n门诊病历\n科室\n门诊全科\n就诊日期\n2024-04-02\n就诊时间\n09:32:37\n姓名\n性别\n女\n年龄\n57岁\n联系电话\n身份证\n详细地址\n观沙岭\n主诉\n糖尿病患者常规监测血糖及购药。\n现病史\n患者糖尿病多年，规律使用降糖药，血糖控制不住，血压控制良好，今前来常规监测血糖血压及\n购药。\n既往史\n2型糖尿病，高血压2级\n个人史\n家族史\n否认家族中有类似病史，否认家族中有其他遗传病史，否认家族性肿瘤病史。\n过敏史\n无\n体格检查\n体温：36℃，血压：132/89mmHg、一般情况可，心肺腹-。\n辅助检查\n诊断\n主诊断：2型糖尿病\n处理意见\n1.盐酸二甲双胍缓释片0.5g 口服：1次1片 3次/日。\n苯磺酸氨氯地平片5mg，口服：1次1片 1次/日。\n2.低盐低脂糖尿病饮食，适当锻炼，按时吃药。\n3.定时监测血压血糖血脂，不适随诊。\n医生姓名：\n刘成海",
    "role": "user"
  }
]
2026-08-10 13:29:37,537 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:37,537 INFO     29 [qwen-vl-text] LLM output (len=349):
{
  "encounter_date": "2024-04-02",
  "chief_complaint": "糖尿病患者常规监测血糖及购药。",
  "present_illness": "患者糖尿病多年，规律使用降糖药，血糖控制不住，血压控制良好，今前来常规监测血糖血压及购药。",
  "past_history": "2型糖尿病，高血压2级",
  "diagnosis": "2型糖尿病",
  "treatment_plan": [
    "盐酸二甲双胍缓释片0.5g 口服：1次1片 3次/日。",
    "苯磺酸氨氯地平片5mg，口服：1次1片 1次/日。",
    "低盐低脂糖尿病饮食，适当锻炼，按时吃药。",
    "定时监测血压血糖血脂，不适随诊。"
  ]
}
2026-08-10 13:29:37,537 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-04-02]
2026-08-10 13:29:37,540 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1341933, prompt_len=1135
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共41行）
["长沙市岳麓区观沙岭街道社区卫生服务中心", "门诊病历", "科室", "门诊全科", "就诊日期", "2024-04-02", "就诊时间", "09:32:37", "姓名", "性别", "女", "年龄", "57岁", "联系电话", "身份证", "详细地址", "观沙岭", "主诉", "糖尿病患者常规监测血糖及购药。", "现病史", "患者糖尿病多年，规律使用降糖药，血糖控制不住，血压控制良好，今前来常规监测血糖血压及", "购药。", "既往史", "2型糖尿病，高血压2级", "个人史", "家族史", "否认家族中有类似病史，否认家族中有其他遗传病史，否认家族性肿瘤病史。", "过敏史", "无", "体格检查", "体温：36℃，血压：132/89mmHg、一般情况可，心肺腹-。", "辅助检查", "诊断", "主诊断：2型糖尿病", "处理意见", "1.盐酸二甲双胍缓释片0.5g 口服：1次1片 3次/日。", "苯磺酸氨氯地平片5mg，口服：1次1片 1次/日。", "2.低盐低脂糖尿病饮食，适当锻炼，按时吃药。", "3.定时监测血压血糖血脂，不适随诊。", "医生姓名：", "刘成海"]

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
2026-08-10 13:29:50,534 INFO     29 [qwen-vl-text] coord API raw response (len=2202):
[
	{"text": "长沙市岳麓区观沙岭街道社区卫生服务中心", "bbox": [274, 69, 730, 94]},
	{"text": "门诊病历", "bbox": [468, 98, 538, 112]},
	{"text": "科室", "bbox": [114, 120, 149, 135]},
	{"text": "门诊全科", "bbox": [233, 123, 303, 138]},
	{"text": "就诊日期", "bbox": [378, 125, 449, 140]},
	{"text": "2024-04-02", "bbox": [523, 129, 611, 142]},
	{"text": "就诊时间", "bbox": [671, 131, 740, 145]},
	{"text": "09:32:37", "bbox": [773, 134, 843, 147]},
	{"text": "姓名", "bbox": [114, 157, 149, 171]},
	{"text": "性别", "bbox": [361, 160, 398, 175]},
	{"text": "女", "bbox": [445, 162, 463, 177]},
	{"text": "年龄", "bbox": [510, 163, 544, 177]},
	{"text": "57岁", "bbox": [588, 165, 625, 178]},
	{"text": "联系电话", "bbox": [670, 166, 739, 180]},
	{"text": "身份证", "bbox": [107, 193, 158, 207]},
	{"text": "详细地址", "bbox": [98, 230, 166, 244]},
	{"text": "观沙岭", "bbox": [208, 232, 260, 246]},
	{"text": "主诉", "bbox": [116, 266, 150, 280]},
	{"text": "糖尿病患者常规监测血糖及购药。", "bbox": [208, 268, 460, 285]},
	{"text": "现病史", "bbox": [111, 313, 162, 327]},
	{"text": "患者糖尿病多年，规律使用降糖药，血糖控制不住，血压控制良好，今前来常规监测血糖血压及", "bbox": [211, 298, 924, 324]},
	{"text": "购药。", "bbox": [211, 323, 255, 338]},
	{"text": "既往史", "bbox": [114, 359, 166, 373]},
	{"text": "2型糖尿病，高血压2级", "bbox": [213, 362, 398, 377]},
	{"text": "个人史", "bbox": [116, 395, 167, 409]},
	{"text": "家族史", "bbox": [116, 429, 167, 443]},
	{"text": "否认家族中有类似病史，否认家族中有其他遗传病史，否认家族性肿瘤病史。", "bbox": [217, 431, 779, 453]},
	{"text": "过敏史", "bbox": [118, 463, 169, 477]},
	{"text": "无", "bbox": [217, 465, 236, 478]},
	{"text": "体格检查", "bbox": [110, 502, 177, 516]},
	{"text": "体温：36℃，血压：132/89mmHg、一般情况可，心肺腹-。", "bbox": [217, 491, 635, 513]},
	{"text": "辅助检查", "bbox": [108, 539, 175, 553]},
	{"text": "诊断", "bbox": [122, 573, 156, 587]},
	{"text": "主诊断：2型糖尿病", "bbox": [215, 575, 362, 591]},
	{"text": "处理意见", "bbox": [103, 682, 170, 696]},
	{"text": "1.盐酸二甲双胍缓释片0.5g 口服：1次1片 3次/日。", "bbox": [213, 611, 634, 632]},
	{"text": "苯磺酸氨氯地平片5mg，口服：1次1片 1次/日。", "bbox": [230, 635, 608, 656]},
	{"text": "2.低盐低脂糖尿病饮食，适当锻炼，按时吃药。", "bbox": [211, 660, 557, 679]},
	{"text": "3.定时监测血压血糖血脂，不适随诊。", "bbox": [211, 684, 498, 701]},
	{"text": "医生姓名：", "bbox": [340, 785, 415, 800]},
	{"text": "刘成海", "bbox": [487, 787, 534, 804]}
]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord API: raw_items=41, valid_items=41, elapsed=13.0s
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[0]: text=长沙市岳麓区观沙岭街道社区卫生服务中心, bbox=[274, 69, 730, 94]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[468, 98, 538, 112]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[2]: text=科室, bbox=[114, 120, 149, 135]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[3]: text=门诊全科, bbox=[233, 123, 303, 138]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[4]: text=就诊日期, bbox=[378, 125, 449, 140]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[5]: text=2024-04-02, bbox=[523, 129, 611, 142]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[6]: text=就诊时间, bbox=[671, 131, 740, 145]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[7]: text=09:32:37, bbox=[773, 134, 843, 147]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[8]: text=姓名, bbox=[114, 157, 149, 171]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[9]: text=性别, bbox=[361, 160, 398, 175]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[10]: text=女, bbox=[445, 162, 463, 177]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[11]: text=年龄, bbox=[510, 163, 544, 177]
2026-08-10 13:29:50,535 INFO     29 [qwen-vl-text] coord item[12]: text=57岁, bbox=[588, 165, 625, 178]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[13]: text=联系电话, bbox=[670, 166, 739, 180]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[14]: text=身份证, bbox=[107, 193, 158, 207]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[15]: text=详细地址, bbox=[98, 230, 166, 244]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[16]: text=观沙岭, bbox=[208, 232, 260, 246]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[17]: text=主诉, bbox=[116, 266, 150, 280]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[18]: text=糖尿病患者常规监测血糖及购药。, bbox=[208, 268, 460, 285]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[19]: text=现病史, bbox=[111, 313, 162, 327]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[20]: text=患者糖尿病多年，规律使用降糖药，血糖控制不住，血压控制良好，今前来常规监测血糖血压及, bbox=[211, 298, 924, 324]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[21]: text=购药。, bbox=[211, 323, 255, 338]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[22]: text=既往史, bbox=[114, 359, 166, 373]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[23]: text=2型糖尿病，高血压2级, bbox=[213, 362, 398, 377]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[24]: text=个人史, bbox=[116, 395, 167, 409]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[25]: text=家族史, bbox=[116, 429, 167, 443]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[26]: text=否认家族中有类似病史，否认家族中有其他遗传病史，否认家族性肿瘤病史。, bbox=[217, 431, 779, 453]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[27]: text=过敏史, bbox=[118, 463, 169, 477]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[28]: text=无, bbox=[217, 465, 236, 478]
2026-08-10 13:29:50,536 INFO     29 [qwen-vl-text] coord item[29]: text=体格检查, bbox=[110, 502, 177, 516]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[30]: text=体温：36℃，血压：132/89mmHg、一般情况可，心肺腹-。, bbox=[217, 491, 635, 513]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[31]: text=辅助检查, bbox=[108, 539, 175, 553]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[32]: text=诊断, bbox=[122, 573, 156, 587]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[33]: text=主诊断：2型糖尿病, bbox=[215, 575, 362, 591]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[34]: text=处理意见, bbox=[103, 682, 170, 696]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[35]: text=1.盐酸二甲双胍缓释片0.5g 口服：1次1片 3次/日。, bbox=[213, 611, 634, 632]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[36]: text=苯磺酸氨氯地平片5mg，口服：1次1片 1次/日。, bbox=[230, 635, 608, 656]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[37]: text=2.低盐低脂糖尿病饮食，适当锻炼，按时吃药。, bbox=[211, 660, 557, 679]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[38]: text=3.定时监测血压血糖血脂，不适随诊。, bbox=[211, 684, 498, 701]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[39]: text=医生姓名：, bbox=[340, 785, 415, 800]
2026-08-10 13:29:50,537 INFO     29 [qwen-vl-text] coord item[40]: text=刘成海, bbox=[487, 787, 534, 804]
2026-08-10 13:29:50,538 INFO     29 [qwen-vl-text] page=7 — 41/41 coords, api_time=13.0s
2026-08-10 13:29:50,538 INFO     29 [qwen-vl-text] new_positions (41):
[[7, 163.03, 434.34999999999997, 58.098, 79.148], [7, 278.46, 320.11, 82.51599999999999, 94.304], [7, 67.83, 88.655, 101.03999999999999, 113.67], [7, 138.635, 180.285, 103.566, 116.196], [7, 224.91, 267.155, 105.25, 117.88], [7, 311.185, 363.54499999999996, 108.618, 119.564], [7, 399.245, 440.29999999999995, 110.30199999999999, 122.08999999999999], [7, 459.935, 501.585, 112.828, 123.774], [7, 67.83, 88.655, 132.194, 143.982], [7, 214.795, 236.81, 134.72, 147.35], [7, 264.775, 275.485, 136.404, 149.034], [7, 303.45, 323.68, 137.246, 149.034], [7, 349.85999999999996, 371.875, 138.93, 149.876], [7, 398.65, 439.705, 139.772, 151.56], [7, 63.665, 94.00999999999999, 162.506, 174.29399999999998], [7, 58.309999999999995, 98.77, 193.66, 205.44799999999998], [7, 123.75999999999999, 154.7, 195.344, 207.132], [7, 69.02, 89.25, 223.97199999999998, 235.76], [7, 123.75999999999999, 273.7, 225.656, 239.97], [7, 66.045, 96.39, 263.546, 275.334], [7, 125.54499999999999, 549.78, 250.916, 272.808], [7, 125.54499999999999, 151.725, 271.966, 284.596], [7, 67.83, 98.77, 302.27799999999996, 314.066], [7, 126.735, 236.81, 304.804, 317.43399999999997], [7, 69.02, 99.365, 332.59, 344.378], [7, 69.02, 99.365, 361.21799999999996, 373.006], [7, 129.11499999999998, 463.505, 362.902, 381.426], [7, 70.21, 100.55499999999999, 389.846, 401.63399999999996], [7, 129.11499999999998, 140.42, 391.53, 402.476], [7, 65.45, 105.315, 422.68399999999997, 434.472], [7, 129.11499999999998, 377.825, 413.42199999999997, 431.94599999999997], [7, 64.25999999999999, 104.125, 453.83799999999997, 465.626], [7, 72.59, 92.82, 482.466, 494.25399999999996], [7, 127.925, 215.39, 484.15, 497.62199999999996], [7, 61.285, 101.14999999999999, 574.244, 586.0319999999999], [7, 126.735, 377.22999999999996, 514.462, 532.144], [7, 136.85, 361.76, 534.67, 552.352], [7, 125.54499999999999, 331.41499999999996, 555.72, 571.718], [7, 125.54499999999999, 296.31, 575.928, 590.242], [7, 202.29999999999998, 246.92499999999998, 660.97, 673.6], [7, 289.765, 317.72999999999996, 662.654, 676.968]]
2026-08-10 13:29:50,538 INFO     29 [qwen-vl-text] ═══ DONE ═══ 41 positions, pages=1, time=15.9s
2026-08-10 13:29:50,551 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:29:50,551 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:29:50,552 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:29:50,556 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:29:50,557 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:29:50,557 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:29:50,557 INFO     29 [qwen-vl-text] positions(42): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:29:50,557 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [42]
2026-08-10 13:29:50,694 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:29:50,695 INFO     29 [qwen-vl-text] LLM extraction start, text_len=393
2026-08-10 13:29:50,695 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:50,696 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 101, \"bbox_end\": 142, \"encounter_dates\": [\"2025-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "养天和大药房\n流水号：806581202503230257\n收银员：唐红娟\n日期：2025-03-23 10:21:15\n品名\n批号\n厂家/产地\n规格\n零售价\n数量\n金额\n优惠\n1 盐酸二甲双胍缓释片\n20051289\n悦康药业\n0.5g*30\n16.00\n6\n96.00\n0\n2.苯磺酸氨氯地平片\n20103551\n四川省百草生物药业\n5mg*24\n26.00\n3\n78.00\n0\n零售总额：174.00\n价格优惠： 0.00\n应收金额：174.00\n付款：174.00\n找零：0\n顾客姓名：姜必言\n会员卡号：8036545742\n会员积分：1253.50\n门店名称：岳麓区春江店\n门店地址：长沙市观沙岭街道春江郦城 S8-166\n门店电话：13308478346\n监督电话：0731-82961371\n药品属于特殊商品，无质量问题恕不退换！\n本小票只作为购货凭证使用，不作为报销凭据",
    "role": "user"
  }
]
2026-08-10 13:29:51,476 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:29:51.476+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 50, "failed": 0, "current": {"583868d894bf11f1bd9827cf206dfa2d": {"id": "583868d894bf11f1bd9827cf206dfa2d", "doc_id": "580c255294bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "type": "pdf", "location": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "size": 794325, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368496497, "task_type": "dataflow", "root_trace_id": "49d7d387da1c49cda1501856908b3841", "root_traceparent": "00-49d7d387da1c49cda1501856908b3841-5cab0f312536d09e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:29:53,995 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:29:53,995 INFO     29 [qwen-vl-text] LLM output (len=695):
{
  "encounter_date": "2025-03-23",
  "pharmacy": "养天和大药房",
  "medications": [
    {
      "name": "盐酸二甲双胍缓释片",
      "specification": "0.5g*30",
      "dosage": null,
      "quantity": 6,
      "unit_price": 16.00,
      "total_price": 96.00,
      "frequency": null,
      "route": null,
      "manufacturer": "悦康药业",
      "approval_number": null
    },
    {
      "name": "苯磺酸氨氯地平片",
      "specification": "5mg*24",
      "dosage": null,
      "quantity": 3,
      "unit_price": 26.00,
      "total_price": 78.00,
      "frequency": null,
      "route": null,
      "manufacturer": "四川省百草生物药业",
      "approval_number": null
    }
  ],
  "payment_total": 174.00,
  "payment_method": null
}
2026-08-10 13:29:53,995 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-23]
2026-08-10 13:29:53,997 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=912581, prompt_len=1132
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共42行）
["养天和大药房", "流水号：806581202503230257", "收银员：唐红娟", "日期：2025-03-23 10:21:15", "品名", "批号", "厂家/产地", "规格", "零售价", "数量", "金额", "优惠", "1 盐酸二甲双胍缓释片", "20051289", "悦康药业", "0.5g*30", "16.00", "6", "96.00", "0", "2.苯磺酸氨氯地平片", "20103551", "四川省百草生物药业", "5mg*24", "26.00", "3", "78.00", "0", "零售总额：174.00", "价格优惠： 0.00", "应收金额：174.00", "付款：174.00", "找零：0", "顾客姓名：姜必言", "会员卡号：8036545742", "会员积分：1253.50", "门店名称：岳麓区春江店", "门店地址：长沙市观沙岭街道春江郦城 S8-166", "门店电话：13308478346", "监督电话：0731-82961371", "药品属于特殊商品，无质量问题恕不退换！", "本小票只作为购货凭证使用，不作为报销凭据"]

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
2026-08-10 13:30:05,917 INFO     29 [qwen-vl-text] coord API raw response (len=2244):
[
	{"text": "养天和大药房", "bbox": [402, 136, 620, 163]},
	{"text": "流水号：806581202503230257", "bbox": [206, 168, 565, 187]},
	{"text": "收银员：唐红娟", "bbox": [206, 193, 402, 212]},
	{"text": "日期：2025-03-23 10:21:15", "bbox": [206, 218, 552, 237]},
	{"text": "品名", "bbox": [206, 268, 260, 288]},
	{"text": "批号", "bbox": [662, 267, 715, 287]},
	{"text": "厂家/产地", "bbox": [206, 292, 330, 312]},
	{"text": "规格", "bbox": [662, 291, 717, 311]},
	{"text": "零售价", "bbox": [206, 318, 287, 338]},
	{"text": "数量", "bbox": [330, 318, 384, 338]},
	{"text": "金额", "bbox": [497, 318, 550, 338]},
	{"text": "优惠", "bbox": [662, 317, 717, 337]},
	{"text": "1 盐酸二甲双胍缓释片", "bbox": [204, 367, 473, 387]},
	{"text": "20051289", "bbox": [613, 368, 723, 385]},
	{"text": "悦康药业", "bbox": [204, 391, 315, 410]},
	{"text": "0.5g*30", "bbox": [619, 391, 718, 410]},
	{"text": "16.00", "bbox": [203, 417, 272, 435]},
	{"text": "6", "bbox": [355, 417, 372, 435]},
	{"text": "96.00", "bbox": [509, 417, 579, 435]},
	{"text": "0", "bbox": [675, 417, 690, 435]},
	{"text": "2.苯磺酸氨氯地平片", "bbox": [202, 442, 452, 462]},
	{"text": "20103551", "bbox": [606, 443, 715, 460]},
	{"text": "四川省百草生物药业", "bbox": [202, 467, 452, 486]},
	{"text": "5mg*24", "bbox": [633, 467, 718, 486]},
	{"text": "26.00", "bbox": [201, 493, 271, 510]},
	{"text": "3", "bbox": [355, 493, 370, 510]},
	{"text": "78.00", "bbox": [509, 493, 579, 510]},
	{"text": "0", "bbox": [675, 493, 690, 510]},
	{"text": "零售总额：174.00", "bbox": [201, 542, 424, 562]},
	{"text": "价格优惠： 0.00", "bbox": [200, 568, 424, 588]},
	{"text": "应收金额：174.00", "bbox": [200, 593, 424, 613]},
	{"text": "付款：174.00", "bbox": [200, 619, 367, 638]},
	{"text": "找零：0", "bbox": [563, 618, 662, 638]},
	{"text": "顾客姓名：姜必言", "bbox": [200, 670, 420, 690]},
	{"text": "会员卡号：8036545742", "bbox": [200, 695, 479, 714]},
	{"text": "会员积分：1253.50", "bbox": [200, 719, 439, 738]},
	{"text": "门店名称：岳麓区春江店", "bbox": [200, 769, 494, 789]},
	{"text": "门店地址：长沙市观沙岭街道春江郦城 S8-166", "bbox": [200, 794, 768, 814]},
	{"text": "门店电话：13308478346", "bbox": [200, 820, 496, 839]},
	{"text": "监督电话：0731-82961371", "bbox": [200, 869, 519, 889]},
	{"text": "药品属于特殊商品，无质量问题恕不退换！", "bbox": [201, 894, 715, 914]},
	{"text": "本小票只作为购货凭证使用，不作为报销凭据", "bbox": [201, 917, 757, 938]}
]
2026-08-10 13:30:05,918 INFO     29 [qwen-vl-text] coord API: raw_items=42, valid_items=42, elapsed=11.9s
2026-08-10 13:30:05,918 INFO     29 [qwen-vl-text] coord item[0]: text=养天和大药房, bbox=[402, 136, 620, 163]
2026-08-10 13:30:05,918 INFO     29 [qwen-vl-text] coord item[1]: text=流水号：806581202503230257, bbox=[206, 168, 565, 187]
2026-08-10 13:30:05,918 INFO     29 [qwen-vl-text] coord item[2]: text=收银员：唐红娟, bbox=[206, 193, 402, 212]
2026-08-10 13:30:05,918 INFO     29 [qwen-vl-text] coord item[3]: text=日期：2025-03-23 10:21:15, bbox=[206, 218, 552, 237]
2026-08-10 13:30:05,918 INFO     29 [qwen-vl-text] coord item[4]: text=品名, bbox=[206, 268, 260, 288]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[5]: text=批号, bbox=[662, 267, 715, 287]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[6]: text=厂家/产地, bbox=[206, 292, 330, 312]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[7]: text=规格, bbox=[662, 291, 717, 311]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[8]: text=零售价, bbox=[206, 318, 287, 338]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[9]: text=数量, bbox=[330, 318, 384, 338]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[10]: text=金额, bbox=[497, 318, 550, 338]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[11]: text=优惠, bbox=[662, 317, 717, 337]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[12]: text=1 盐酸二甲双胍缓释片, bbox=[204, 367, 473, 387]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[13]: text=20051289, bbox=[613, 368, 723, 385]
2026-08-10 13:30:05,919 INFO     29 [qwen-vl-text] coord item[14]: text=悦康药业, bbox=[204, 391, 315, 410]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[15]: text=0.5g*30, bbox=[619, 391, 718, 410]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[16]: text=16.00, bbox=[203, 417, 272, 435]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[17]: text=6, bbox=[355, 417, 372, 435]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[18]: text=96.00, bbox=[509, 417, 579, 435]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[19]: text=0, bbox=[675, 417, 690, 435]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[20]: text=2.苯磺酸氨氯地平片, bbox=[202, 442, 452, 462]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[21]: text=20103551, bbox=[606, 443, 715, 460]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[22]: text=四川省百草生物药业, bbox=[202, 467, 452, 486]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[23]: text=5mg*24, bbox=[633, 467, 718, 486]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[24]: text=26.00, bbox=[201, 493, 271, 510]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[25]: text=3, bbox=[355, 493, 370, 510]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[26]: text=78.00, bbox=[509, 493, 579, 510]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[27]: text=0, bbox=[675, 493, 690, 510]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[28]: text=零售总额：174.00, bbox=[201, 542, 424, 562]
2026-08-10 13:30:05,920 INFO     29 [qwen-vl-text] coord item[29]: text=价格优惠： 0.00, bbox=[200, 568, 424, 588]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[30]: text=应收金额：174.00, bbox=[200, 593, 424, 613]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[31]: text=付款：174.00, bbox=[200, 619, 367, 638]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[32]: text=找零：0, bbox=[563, 618, 662, 638]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[33]: text=顾客姓名：姜必言, bbox=[200, 670, 420, 690]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[34]: text=会员卡号：8036545742, bbox=[200, 695, 479, 714]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[35]: text=会员积分：1253.50, bbox=[200, 719, 439, 738]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[36]: text=门店名称：岳麓区春江店, bbox=[200, 769, 494, 789]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[37]: text=门店地址：长沙市观沙岭街道春江郦城 S8-166, bbox=[200, 794, 768, 814]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[38]: text=门店电话：13308478346, bbox=[200, 820, 496, 839]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[39]: text=监督电话：0731-82961371, bbox=[200, 869, 519, 889]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[40]: text=药品属于特殊商品，无质量问题恕不退换！, bbox=[201, 894, 715, 914]
2026-08-10 13:30:05,921 INFO     29 [qwen-vl-text] coord item[41]: text=本小票只作为购货凭证使用，不作为报销凭据, bbox=[201, 917, 757, 938]
2026-08-10 13:30:05,922 INFO     29 [qwen-vl-text] page=5 — 42/42 coords, api_time=11.9s
2026-08-10 13:30:05,922 INFO     29 [qwen-vl-text] new_positions (42):
[[5, 239.19, 368.9, 114.512, 137.246], [5, 122.57, 336.175, 141.456, 157.454], [5, 122.57, 239.19, 162.506, 178.504], [5, 122.57, 328.44, 183.55599999999998, 199.554], [5, 122.57, 154.7, 225.656, 242.49599999999998], [5, 393.89, 425.42499999999995, 224.814, 241.654], [5, 122.57, 196.35, 245.864, 262.704], [5, 393.89, 426.615, 245.022, 261.86199999999997], [5, 122.57, 170.765, 267.756, 284.596], [5, 196.35, 228.48, 267.756, 284.596], [5, 295.715, 327.25, 267.756, 284.596], [5, 393.89, 426.615, 266.914, 283.75399999999996], [5, 121.38, 281.435, 309.014, 325.854], [5, 364.73499999999996, 430.185, 309.856, 324.17], [5, 121.38, 187.42499999999998, 329.222, 345.21999999999997], [5, 368.305, 427.21, 329.222, 345.21999999999997], [5, 120.785, 161.84, 351.114, 366.27], [5, 211.225, 221.34, 351.114, 366.27], [5, 302.85499999999996, 344.505, 351.114, 366.27], [5, 401.625, 410.54999999999995, 351.114, 366.27], [5, 120.19, 268.94, 372.164, 389.00399999999996], [5, 360.57, 425.42499999999995, 373.006, 387.32], [5, 120.19, 268.94, 393.214, 409.212], [5, 376.635, 427.21, 393.214, 409.212], [5, 119.595, 161.245, 415.106, 429.41999999999996], [5, 211.225, 220.14999999999998, 415.106, 429.41999999999996], [5, 302.85499999999996, 344.505, 415.106, 429.41999999999996], [5, 401.625, 410.54999999999995, 415.106, 429.41999999999996], [5, 119.595, 252.28, 456.364, 473.204], [5, 119.0, 252.28, 478.256, 495.096], [5, 119.0, 252.28, 499.306, 516.146], [5, 119.0, 218.36499999999998, 521.198, 537.196], [5, 334.98499999999996, 393.89, 520.356, 537.196], [5, 119.0, 249.89999999999998, 564.14, 580.98], [5, 119.0, 285.005, 585.1899999999999, 601.188], [5, 119.0, 261.205, 605.398, 621.396], [5, 119.0, 293.93, 647.4979999999999, 664.338], [5, 119.0, 456.96, 668.548, 685.3879999999999], [5, 119.0, 295.12, 690.4399999999999, 706.438], [5, 119.0, 308.805, 731.698, 748.538], [5, 119.595, 425.42499999999995, 752.7479999999999, 769.588], [5, 119.595, 450.41499999999996, 772.1139999999999, 789.7959999999999]]
2026-08-10 13:30:05,922 INFO     29 [qwen-vl-text] ═══ DONE ═══ 42 positions, pages=1, time=15.4s
2026-08-10 13:30:05,922 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:30:05,924 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:30:05,924 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:30:05,924 INFO     29 [qwen-vl-text] positions(42): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:30:05,924 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [42]
2026-08-10 13:30:06,057 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:30:06,057 INFO     29 [qwen-vl-text] LLM extraction start, text_len=392
2026-08-10 13:30:06,058 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:06,058 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 143, \"bbox_end\": 184, \"encounter_dates\": [\"2025-01-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "养天和大药房\n流水号：806581202501220207\n收银员：唐红娟\n日期：2025-01-22 09:36:13\n品名\n批号\n厂家/产地\n规格\n零售价\n数量\n金额\n优惠\n1 盐酸二甲双胍缓释片\n20051289\n悦康药业\n0.5g*30\n16.00\n6\n96.00\n0\n2.苯磺酸氨氯地平片\n20103551\n四川省百草生物药业\n5mg*24\n26.00\n3\n78.00\n0\n零售总额：174.00\n价格优惠：0.00\n应收金额：174.00\n付款：174.00\n找零：0\n顾客姓名：姜必白\n会员卡号：8036545742\n会员积分：1035.60\n门店名称：岳麓区春江店\n门店地址：长沙市观沙岭街道春江郦城 S8-166\n门店电话：13308478346\n监督电话：0731-82961371\n药品属于特殊商品，无质量问题恕不退换！\n本小票只作为购货凭证使用，不作为报销凭据",
    "role": "user"
  }
]
2026-08-10 13:30:09,108 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:09,108 INFO     29 [qwen-vl-text] LLM output (len=695):
{
  "encounter_date": "2025-01-22",
  "pharmacy": "养天和大药房",
  "medications": [
    {
      "name": "盐酸二甲双胍缓释片",
      "specification": "0.5g*30",
      "dosage": null,
      "quantity": 6,
      "unit_price": 16.00,
      "total_price": 96.00,
      "frequency": null,
      "route": null,
      "manufacturer": "悦康药业",
      "approval_number": null
    },
    {
      "name": "苯磺酸氨氯地平片",
      "specification": "5mg*24",
      "dosage": null,
      "quantity": 3,
      "unit_price": 26.00,
      "total_price": 78.00,
      "frequency": null,
      "route": null,
      "manufacturer": "四川省百草生物药业",
      "approval_number": null
    }
  ],
  "payment_total": 174.00,
  "payment_method": null
}
2026-08-10 13:30:09,108 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-22]
2026-08-10 13:30:09,110 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=966739, prompt_len=1131
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共42行）
["养天和大药房", "流水号：806581202501220207", "收银员：唐红娟", "日期：2025-01-22 09:36:13", "品名", "批号", "厂家/产地", "规格", "零售价", "数量", "金额", "优惠", "1 盐酸二甲双胍缓释片", "20051289", "悦康药业", "0.5g*30", "16.00", "6", "96.00", "0", "2.苯磺酸氨氯地平片", "20103551", "四川省百草生物药业", "5mg*24", "26.00", "3", "78.00", "0", "零售总额：174.00", "价格优惠：0.00", "应收金额：174.00", "付款：174.00", "找零：0", "顾客姓名：姜必白", "会员卡号：8036545742", "会员积分：1035.60", "门店名称：岳麓区春江店", "门店地址：长沙市观沙岭街道春江郦城 S8-166", "门店电话：13308478346", "监督电话：0731-82961371", "药品属于特殊商品，无质量问题恕不退换！", "本小票只作为购货凭证使用，不作为报销凭据"]

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
2026-08-10 13:30:22,647 INFO     29 [qwen-vl-text] coord API raw response (len=2243):
[
	{"text": "养天和大药房", "bbox": [400, 128, 621, 159]},
	{"text": "流水号：806581202501220207", "bbox": [205, 162, 565, 188]},
	{"text": "收银员：唐红娟", "bbox": [205, 190, 400, 212]},
	{"text": "日期：2025-01-22 09:36:13", "bbox": [205, 212, 551, 238]},
	{"text": "品名", "bbox": [204, 269, 258, 289]},
	{"text": "批号", "bbox": [663, 259, 720, 280]},
	{"text": "厂家/产地", "bbox": [204, 292, 329, 312]},
	{"text": "规格", "bbox": [663, 284, 720, 305]},
	{"text": "零售价", "bbox": [204, 318, 285, 338]},
	{"text": "数量", "bbox": [328, 317, 383, 337]},
	{"text": "金额", "bbox": [495, 314, 550, 334]},
	{"text": "优惠", "bbox": [663, 310, 720, 331]},
	{"text": "1 盐酸二甲双胍缓释片", "bbox": [204, 366, 473, 387]},
	{"text": "20051289", "bbox": [613, 364, 727, 381]},
	{"text": "悦康药业", "bbox": [203, 392, 314, 412]},
	{"text": "0.5g*30", "bbox": [619, 389, 720, 408]},
	{"text": "16.00", "bbox": [203, 418, 271, 435]},
	{"text": "6", "bbox": [354, 418, 370, 435]},
	{"text": "96.00", "bbox": [508, 415, 579, 433]},
	{"text": "0", "bbox": [677, 414, 692, 431]},
	{"text": "2.苯磺酸氨氯地平片", "bbox": [202, 441, 452, 462]},
	{"text": "20103551", "bbox": [606, 440, 717, 457]},
	{"text": "四川省百草生物药业", "bbox": [202, 466, 452, 487]},
	{"text": "5mg*24", "bbox": [634, 464, 720, 483]},
	{"text": "26.00", "bbox": [202, 494, 271, 511]},
	{"text": "3", "bbox": [354, 494, 370, 510]},
	{"text": "78.00", "bbox": [508, 491, 579, 508]},
	{"text": "0", "bbox": [677, 490, 692, 507]},
	{"text": "零售总额：174.00", "bbox": [202, 542, 424, 562]},
	{"text": "价格优惠：0.00", "bbox": [202, 567, 424, 587]},
	{"text": "应收金额：174.00", "bbox": [202, 592, 424, 612]},
	{"text": "付款：174.00", "bbox": [202, 618, 368, 638]},
	{"text": "找零：0", "bbox": [563, 617, 663, 638]},
	{"text": "顾客姓名：姜必白", "bbox": [202, 667, 419, 687]},
	{"text": "会员卡号：8036545742", "bbox": [202, 692, 479, 712]},
	{"text": "会员积分：1035.60", "bbox": [202, 718, 439, 737]},
	{"text": "门店名称：岳麓区春江店", "bbox": [202, 767, 492, 787]},
	{"text": "门店地址：长沙市观沙岭街道春江郦城 S8-166", "bbox": [202, 791, 767, 811]},
	{"text": "门店电话：13308478346", "bbox": [202, 817, 495, 836]},
	{"text": "监督电话：0731-82961371", "bbox": [202, 867, 518, 887]},
	{"text": "药品属于特殊商品，无质量问题恕不退换！", "bbox": [202, 893, 716, 913]},
	{"text": "本小票只作为购货凭证使用，不作为报销凭据", "bbox": [202, 917, 759, 938]}
]
2026-08-10 13:30:22,647 INFO     29 [qwen-vl-text] coord API: raw_items=42, valid_items=42, elapsed=13.5s
2026-08-10 13:30:22,647 INFO     29 [qwen-vl-text] coord item[0]: text=养天和大药房, bbox=[400, 128, 621, 159]
2026-08-10 13:30:22,647 INFO     29 [qwen-vl-text] coord item[1]: text=流水号：806581202501220207, bbox=[205, 162, 565, 188]
2026-08-10 13:30:22,647 INFO     29 [qwen-vl-text] coord item[2]: text=收银员：唐红娟, bbox=[205, 190, 400, 212]
2026-08-10 13:30:22,647 INFO     29 [qwen-vl-text] coord item[3]: text=日期：2025-01-22 09:36:13, bbox=[205, 212, 551, 238]
2026-08-10 13:30:22,647 INFO     29 [qwen-vl-text] coord item[4]: text=品名, bbox=[204, 269, 258, 289]
2026-08-10 13:30:22,647 INFO     29 [qwen-vl-text] coord item[5]: text=批号, bbox=[663, 259, 720, 280]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[6]: text=厂家/产地, bbox=[204, 292, 329, 312]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[7]: text=规格, bbox=[663, 284, 720, 305]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[8]: text=零售价, bbox=[204, 318, 285, 338]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[9]: text=数量, bbox=[328, 317, 383, 337]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[10]: text=金额, bbox=[495, 314, 550, 334]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[11]: text=优惠, bbox=[663, 310, 720, 331]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[12]: text=1 盐酸二甲双胍缓释片, bbox=[204, 366, 473, 387]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[13]: text=20051289, bbox=[613, 364, 727, 381]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[14]: text=悦康药业, bbox=[203, 392, 314, 412]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[15]: text=0.5g*30, bbox=[619, 389, 720, 408]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[16]: text=16.00, bbox=[203, 418, 271, 435]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[17]: text=6, bbox=[354, 418, 370, 435]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[18]: text=96.00, bbox=[508, 415, 579, 433]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[19]: text=0, bbox=[677, 414, 692, 431]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[20]: text=2.苯磺酸氨氯地平片, bbox=[202, 441, 452, 462]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[21]: text=20103551, bbox=[606, 440, 717, 457]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[22]: text=四川省百草生物药业, bbox=[202, 466, 452, 487]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[23]: text=5mg*24, bbox=[634, 464, 720, 483]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[24]: text=26.00, bbox=[202, 494, 271, 511]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[25]: text=3, bbox=[354, 494, 370, 510]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[26]: text=78.00, bbox=[508, 491, 579, 508]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[27]: text=0, bbox=[677, 490, 692, 507]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[28]: text=零售总额：174.00, bbox=[202, 542, 424, 562]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[29]: text=价格优惠：0.00, bbox=[202, 567, 424, 587]
2026-08-10 13:30:22,648 INFO     29 [qwen-vl-text] coord item[30]: text=应收金额：174.00, bbox=[202, 592, 424, 612]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[31]: text=付款：174.00, bbox=[202, 618, 368, 638]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[32]: text=找零：0, bbox=[563, 617, 663, 638]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[33]: text=顾客姓名：姜必白, bbox=[202, 667, 419, 687]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[34]: text=会员卡号：8036545742, bbox=[202, 692, 479, 712]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[35]: text=会员积分：1035.60, bbox=[202, 718, 439, 737]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[36]: text=门店名称：岳麓区春江店, bbox=[202, 767, 492, 787]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[37]: text=门店地址：长沙市观沙岭街道春江郦城 S8-166, bbox=[202, 791, 767, 811]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[38]: text=门店电话：13308478346, bbox=[202, 817, 495, 836]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[39]: text=监督电话：0731-82961371, bbox=[202, 867, 518, 887]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[40]: text=药品属于特殊商品，无质量问题恕不退换！, bbox=[202, 893, 716, 913]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] coord item[41]: text=本小票只作为购货凭证使用，不作为报销凭据, bbox=[202, 917, 759, 938]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] page=6 — 42/42 coords, api_time=13.5s
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] new_positions (42):
[[6, 238.0, 369.495, 107.776, 133.878], [6, 121.975, 336.175, 136.404, 158.296], [6, 121.975, 238.0, 159.98, 178.504], [6, 121.975, 327.84499999999997, 178.504, 200.396], [6, 121.38, 153.51, 226.498, 243.338], [6, 394.48499999999996, 428.4, 218.078, 235.76], [6, 121.38, 195.755, 245.864, 262.704], [6, 394.48499999999996, 428.4, 239.128, 256.81], [6, 121.38, 169.575, 267.756, 284.596], [6, 195.16, 227.885, 266.914, 283.75399999999996], [6, 294.525, 327.25, 264.388, 281.228], [6, 394.48499999999996, 428.4, 261.02, 278.702], [6, 121.38, 281.435, 308.17199999999997, 325.854], [6, 364.73499999999996, 432.565, 306.488, 320.80199999999996], [6, 120.785, 186.82999999999998, 330.06399999999996, 346.904], [6, 368.305, 428.4, 327.538, 343.536], [6, 120.785, 161.245, 351.95599999999996, 366.27], [6, 210.63, 220.14999999999998, 351.95599999999996, 366.27], [6, 302.26, 344.505, 349.43, 364.586], [6, 402.815, 411.74, 348.58799999999997, 362.902], [6, 120.19, 268.94, 371.322, 389.00399999999996], [6, 360.57, 426.615, 370.47999999999996, 384.794], [6, 120.19, 268.94, 392.372, 410.054], [6, 377.22999999999996, 428.4, 390.688, 406.686], [6, 120.19, 161.245, 415.948, 430.262], [6, 210.63, 220.14999999999998, 415.948, 429.41999999999996], [6, 302.26, 344.505, 413.42199999999997, 427.736], [6, 402.815, 411.74, 412.58, 426.894], [6, 120.19, 252.28, 456.364, 473.204], [6, 120.19, 252.28, 477.414, 494.25399999999996], [6, 120.19, 252.28, 498.464, 515.304], [6, 120.19, 218.95999999999998, 520.356, 537.196], [6, 334.98499999999996, 394.48499999999996, 519.514, 537.196], [6, 120.19, 249.30499999999998, 561.614, 578.454], [6, 120.19, 285.005, 582.664, 599.504], [6, 120.19, 261.205, 604.5559999999999, 620.554], [6, 120.19, 292.74, 645.814, 662.654], [6, 120.19, 456.36499999999995, 666.0219999999999, 682.862], [6, 120.19, 294.525, 687.914, 703.9119999999999], [6, 120.19, 308.21, 730.014, 746.8539999999999], [6, 120.19, 426.02, 751.906, 768.746], [6, 120.19, 451.60499999999996, 772.1139999999999, 789.7959999999999]]
2026-08-10 13:30:22,649 INFO     29 [qwen-vl-text] ═══ DONE ═══ 42 positions, pages=1, time=16.7s
2026-08-10 13:30:22,658 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:30:22,658 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:30:22,658 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:30:22,664 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:22,664 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:30:23,061 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:30:23.060+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 50, "failed": 0, "current": {"583868d894bf11f1bd9827cf206dfa2d": {"id": "583868d894bf11f1bd9827cf206dfa2d", "doc_id": "580c255294bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "type": "pdf", "location": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "size": 794325, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368496497, "task_type": "dataflow", "root_trace_id": "49d7d387da1c49cda1501856908b3841", "root_traceparent": "00-49d7d387da1c49cda1501856908b3841-5cab0f312536d09e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:30:23,580 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:23,586 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:30:23,587 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:30:23,587 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:30:23,594 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:23,595 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:30:24,043 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:24,050 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:30:24,050 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:30:24,051 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:30:24,055 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:24,055 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:30:24,582 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:24,587 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:30:24,587 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:30:24,588 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:30:24,592 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:24,592 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:30:25,741 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:25,750 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:30:25,751 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:30:25,751 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:30:25,756 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:25,756 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:30:26,302 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:30:26,312 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:30:26,312 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "226 items", "markdown": "", "text": "", "name": "JBYA 联药 湘雅三.pdf", "output_format": "chunks", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_LabExam\": 4, \"chunks_Clinical\": 2, \"chunks_Medication\": 2}"}
2026-08-10 13:30:26,312 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:30:26,313 INFO     29 [ChunkMerger] Merged 8 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 2, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 13:30:26,327 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:30:26,328 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "8 items, types={'LabReport': 4, 'OutpatientRecord': 2, 'MedicationRecord': 2}", "name": "JBYA 联药 湘雅三.pdf"}
2026-08-10 13:30:26,329 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:30:26,378 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786368499257, 'update_date': datetime.datetime(2026, 8, 10, 13, 28, 19), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1040047, 'status': '1'}
2026-08-10 13:30:26,602 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   糖化血红蛋白  HbA1c  9.93  %  4.2-6.2  True   
---
   糖化血红蛋白  GllbA1c  10.70  %  4.2-6.3  True   
---
   葡萄糖餐前  BS(餐前)  11.60  mmol/L  3.90-6.1  True    空腹C肽  CPS000  3.24  ng/ml  1.1-4.4  False   
---
   GLU  GLU  12.67  mmol/L  3.9-6.1  True    OGTT 1h  OGTT 1h  32.31  mmol/L  3.89-11.1  True    OGTT 2h  OGTT 2h  32.20  mmol/L  3.9-7.9  True   
---
长沙市岳麓区观沙岭街道社区卫生服务中心
门诊病历
科室
门诊全科
就诊日期
2025-03-01
就诊时间
14:12:26
姓名
性别
女
年龄
58岁
联系电话
身份证
详细地址
湖南省岳阳市湘阴县岭北镇夹洲村夹洲十组
主诉
糖尿病患者常规监测血糖。
现病史
患者诉多年前发现血糖高，伴有口干，多饮，多尿，在上级医院诊断“2型糖尿病”，血糖控制一般，
血压控制良好，今前来常规复诊。
既往史
2型糖尿病，高血压2级
个人史
无
家族史
否认家族中有类似病史，否认家族中有其他遗传病史。
过敏史
无
体格检查
体温：36℃，血压：135/86mmHg，一般情况可，心肺腹（-）。
辅助检查
诊断
1.诊断：2型糖尿病
处理意见
1.盐酸二甲双胍缓释片 0.5g 口服：1次1片 3次/日。
苯磺酸氨氯地平片 5mg，口服：1次1片 1次/日。
2.低盐低脂糖尿病饮食；
3.注意监测血糖情况；
4.糖尿病专科随诊，不适随诊。
医生姓名：
朱素如
---
长沙市岳麓区观沙岭街道社区卫生服务中心
门诊病历
科室
门诊全科
就诊日期
2024-04-02
就诊时间
09:32:37
姓名
性别
女
年龄
57岁
联系电话
身份证
详细地址
观沙岭
主诉
糖尿病患者常规监测血糖及购药。
现病史
患者糖尿病多年，规律使用降糖药，血糖控制不住，血压控制良好，今前来常规监测血糖血压及
购药。
既往史
2型糖尿病，高血压2级
个人史
家族史
否认家族中有类似病史，否认家族中有其他遗传病史，否认家族性肿瘤病史。
过敏史
无
体格检查
体温：36℃，血压：132/89mmHg、一般情况可，心肺腹-。
辅助检查
诊断
主诊断：2型糖尿病
处理意见
1.盐酸二甲双胍缓释片0.5g 口服：1次1片 3次/日。
苯磺酸氨氯地平片5mg，口服：1次1片 1次/日。
2.低盐低脂糖尿病饮食，适当锻炼，按时吃药。
3.定时监测血压血糖血脂，不适随诊。
医生姓名：
刘成海
---
养天和大药房
流水号：806581202503230257
收银员：唐红娟
日期：2025-03-23 10:21:15
品名
批号
厂家/产地
规格
零售价
数量
金额
优惠
1 盐酸二甲双胍缓释片
20051289
悦康药业
0.5g*30
16.00
6
96.00
0
2.苯磺酸氨氯地平片
20103551
四川省百草生物药业
5mg*24
26.00
3
78.00
0
零售总额：174.00
价格优惠： 0.00
应收金额：174.00
付款：174.00
找零：0
顾客姓名：姜必言
会员卡号：8036545742
会员积分：1253.50
门店名称：岳麓区春江店
门店地址：长沙市观沙岭街道春江郦城 S8-166
门店电话：13308478346
监督电话：0731-82961371
药品属于特殊商品，无质量问题恕不退换！
本小票只作为购货凭证使用，不作为报销凭据
---
养天和大药房
流水号：806581202501220207
收银员：唐红娟
日期：2025-01-22 09:36:13
品名
批号
厂家/产地
规格
零售价
数量
金额
优惠
1 盐酸二甲双胍缓释片
20051289
悦康药业
0.5g*30
16.00
6
96.00
0
2.苯磺酸氨氯地平片
20103551
四川省百草生物药业
5mg*24
26.00
3
78.00
0
零售总额：174.00
价格优惠：0.00
应收金额：174.00
付款：174.00
找零：0
顾客姓名：姜必白
会员卡号：8036545742
会员积分：1035.60
门店名称：岳麓区春江店
门店地址：长沙市观沙岭街道春江郦城 S8-166
门店电话：13308478346
监督电话：0731-82961371
药品属于特殊商品，无质量问题恕不退换！
本小票只作为购货凭证使用，不作为报销凭据
2026-08-10 13:30:27,000 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:30:27,001 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "8 items, types={'LabReport': 4, 'OutpatientRecord': 2, 'MedicationRecord': 2}", "name": "JBYA 联药 湘雅三.pdf", "embedding_token_consumption": 1549}
2026-08-10 13:30:27,001 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:30:27,327 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:30:27,327 INFO     29 [Trace] task=583868d8 | doc=JBYA 联药 湘雅三.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":8,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:30:27,330 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(1, 55, 116, 298, 309) row[-1]=(1, 55, 116, 298, 309)
2026-08-10 13:30:27,330 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(2, 74, 133, 78, 89) row[-1]=(2, 74, 133, 78, 89)
2026-08-10 13:30:27,330 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(4, 57, 104, 74, 84) row[-1]=(4, 57, 90, 85, 95)
2026-08-10 13:30:27,331 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(5, 195, 212, 305, 315) row[-1]=(5, 195, 232, 335, 345)
2026-08-10 13:30:27,331 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:30:27,331 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:30:27,331 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:30:27,331 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:30:27,335 INFO     29 set_progress(583868d894bf11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:30:27 [DOC Engine]:
Start to index...
2026-08-10 13:30:27,353 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 13:30:27,357 INFO     29 set_progress(583868d894bf11f1bd9827cf206dfa2d), progress: 0.8125, progress_msg: 
2026-08-10 13:30:27,377 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 13:30:27,384 INFO     29 set_progress(583868d894bf11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:30:27 Indexing done (0.05s). Task done (122.18s)
2026-08-10 13:30:27,388 INFO     29 [Done], chunks(8), token(1549), elapsed:122.18
2026-08-10 13:30:27,486 INFO     29 handle_task done for task {"id": "583868d894bf11f1bd9827cf206dfa2d", "doc_id": "580c255294bf11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "type": "pdf", "location": "JBYA \u8054\u836f \u6e58\u96c5\u4e09.pdf", "size": 794325, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786368496497, "task_type": "dataflow", "root_trace_id": "49d7d387da1c49cda1501856908b3841", "root_traceparent": "00-49d7d387da1c49cda1501856908b3841-5cab0f312536d09e-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
